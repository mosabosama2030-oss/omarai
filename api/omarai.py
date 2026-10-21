"""HTTP API for Omarai's web-research agent and lead workspace."""
from __future__ import annotations

import hmac
import ipaddress
import json
import os
import threading
import time
from collections import defaultdict, deque
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import ClassVar
from urllib.parse import parse_qs, urlparse

from agents.omarai import LeadStore, analyze, normalize
from agents.web_agent import WebAgent

ROOT = Path(__file__).resolve().parents[1] / "web"
AGENT_DASHBOARD = ROOT / "agent.html"
LEADS_DASHBOARD = ROOT / "dashboard.html"
MAX_REQUEST_BODY_BYTES = 200_000
# Bound request-line + header parsing before application code or body processing.
REQUEST_HEADER_READ_TIMEOUT_SECONDS = 8.0
REQUEST_HEADER_IDLE_TIMEOUT_SECONDS = 2.0
MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS = 15.0
# Absolute deadline for reading the entire body, not merely a per-read idle timeout.
REQUEST_BODY_READ_TIMEOUT_SECONDS = 10.0
REQUEST_BODY_IDLE_TIMEOUT_SECONDS = 2.0
MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS = 30.0
REQUEST_BODY_READ_CHUNK_BYTES = 8_192



class _DeadlineRequestReader:
    """Read HTTP header lines with one absolute deadline across all fragments.

    The standard buffered readline can wait indefinitely for a newline if a
    client keeps trickling bytes. This reader checks the same deadline before
    every socket read and buffers only bounded look-ahead so request body bytes
    received with the headers are preserved for read1().
    """

    def __init__(self, connection, handler):
        self.connection = connection
        self.handler = handler
        self._buffer = bytearray()

    def readline(self, limit=-1):
        if limit == 0:
            return b""
        max_bytes = int(limit) if limit is not None and limit > 0 else 65_537
        previous_timeout = self.connection.gettimeout()
        line = bytearray()
        try:
            while len(line) < max_bytes:
                deadline = getattr(self.handler, "_request_header_deadline", None)
                if deadline is None:
                    raise TimeoutError("request-header deadline is not active")
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise TimeoutError("absolute request-header deadline exceeded")

                newline_index = self._buffer.find(b"\n")
                if newline_index >= 0:
                    take = min(newline_index + 1, max_bytes - len(line))
                    line.extend(self._buffer[:take])
                    del self._buffer[:take]
                    break

                if self._buffer:
                    take = min(len(self._buffer), max_bytes - len(line))
                    line.extend(self._buffer[:take])
                    del self._buffer[:take]
                    if len(line) >= max_bytes:
                        break

                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise TimeoutError("absolute request-header deadline exceeded")
                idle_timeout = max(
                    0.1,
                    min(
                        float(REQUEST_HEADER_IDLE_TIMEOUT_SECONDS),
                        MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,
                    ),
                )
                self.connection.settimeout(min(idle_timeout, remaining))
                chunk = self.connection.recv(min(4_096, max_bytes - len(line)))
                if not chunk:
                    break
                self._buffer.extend(chunk)
        finally:
            try:
                self.connection.settimeout(previous_timeout)
            except OSError:
                pass
        return bytes(line)

    def read1(self, size=-1):
        """Read one chunk; body code applies its own idle and absolute deadlines."""
        if size == 0:
            return b""
        if size is None or size < 0:
            size = 8_192
        if self._buffer:
            take = min(len(self._buffer), size)
            data = bytes(self._buffer[:take])
            del self._buffer[:take]
            return data
        return self.connection.recv(size)

    def close(self):
        # The request handler owns the socket and closes its output stream.
        return None


def _configured_agent_concurrency_limit() -> int:
    """Return a process-local cap for expensive research and diagnostics operations."""
    try:
        configured = int(os.getenv("OMARAI_MAX_CONCURRENT_AGENT_REQUESTS", "4").strip())
    except ValueError:
        configured = 4
    return max(1, min(configured, 8))


BUILD_SHA_FILE = Path(__file__).resolve().parents[1] / "BUILD_SHA"


def _build_sha() -> str:
    """Read the source revision baked into the image; never trust a runtime env override."""
    try:
        candidate = BUILD_SHA_FILE.read_text(encoding="ascii").strip().lower()
    except (OSError, UnicodeError):
        return "unknown"
    if len(candidate) == 40 and all(char in "0123456789abcdef" for char in candidate):
        return candidate
    return "unknown"


class Handler(BaseHTTPRequestHandler):
    def setup(self):
        """Install a reader with a strict deadline for the request line and headers."""
        self.connection = self.request
        if self.timeout is not None:
            self.connection.settimeout(self.timeout)
        self._request_header_deadline = None
        self.rfile = _DeadlineRequestReader(self.connection, self)
        self.wfile = self.connection.makefile("wb", self.wbufsize)

    def handle_one_request(self):
        timeout = max(
            0.1,
            min(
                float(REQUEST_HEADER_READ_TIMEOUT_SECONDS),
                MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,
            ),
        )
        self._request_header_deadline = time.monotonic() + timeout
        try:
            super().handle_one_request()
        except TimeoutError:
            # Incomplete request line/headers are untrusted protocol input;
            # close the socket without trying to parse or answer a partial request.
            self.close_connection = True
        finally:
            self._request_header_deadline = None

    store = LeadStore()
    _rate_lock = threading.Lock()
    _request_times: ClassVar[dict[str, deque[float]]] = defaultdict(deque)
    _rate_last_cleanup: ClassVar[float] = 0.0
    RATE_LIMIT_REQUESTS = 20
    RATE_LIMIT_WINDOW_SECONDS = 60
    RATE_LIMIT_CLEANUP_INTERVAL_SECONDS = 60
    AGENT_CONCURRENCY_LIMIT = _configured_agent_concurrency_limit()
    _agent_semaphore = threading.BoundedSemaphore(AGENT_CONCURRENCY_LIMIT)

    def _run_bounded_agent_operation(self, operation):
        """Run an expensive operation only when a process-local slot is available."""
        cls = type(self)
        if not cls._agent_semaphore.acquire(blocking=False):
            return self.respond(
                503,
                {
                    "error": "خدمة البحث مشغولة حاليًا؛ أعد المحاولة بعد قليل.",
                    "retry_after_seconds": 5,
                    "process_concurrency_limit": cls.AGENT_CONCURRENCY_LIMIT,
                },
            )
        try:
            return self.respond(200, operation())
        finally:
            cls._agent_semaphore.release()

    def _authorized(self):
        expected = os.getenv("OMARAI_ACCESS_TOKEN", "").strip()
        if not expected:
            return os.getenv("OMARAI_PUBLIC_DEPLOYMENT", "").strip() != "1"
        supplied = self.headers.get("Authorization", "")
        if not supplied.startswith("Bearer "):
            return False
        return hmac.compare_digest(supplied[7:].strip(), expected)

    def _allowed_origins(self):
        """Return configured browser origins plus this service’s own origin.

        OMARAI_ALLOWED_ORIGINS is a comma-separated list of trusted origins
        (scheme + host + optional port; no path and no wildcard).
        """
        configured = os.getenv("OMARAI_ALLOWED_ORIGINS", "")
        origins = {
            item.strip().rstrip("/")
            for item in configured.split(",")
            if item.strip()
        }
        if os.getenv("OMARAI_PUBLIC_DEPLOYMENT", "").strip() == "1":
            # Host identifies the requested service origin. Do not derive allowed
            # origins from X-Forwarded-Host: direct clients can spoof that header
            # unless the reverse proxy is separately configured to overwrite it.
            scheme = self.headers.get("X-Forwarded-Proto", "https").split(",", 1)[0].strip().lower()
            host = self.headers.get("Host", "").split(",", 1)[0].strip()
            if host:
                origins.add(f"https://{host}".rstrip("/"))
                origins.add(f"{scheme}://{host}".rstrip("/"))
        else:
            port = self.server.server_port
            origins.update(
                {
                    f"http://127.0.0.1:{port}",
                    f"http://localhost:{port}",
                    f"http://[::1]:{port}",
                }
            )
        return origins

    def _origin_allowed(self, origin):
        return bool(origin) and origin.rstrip("/") in self._allowed_origins()

    def _rate_limit_client_key(self):
        """Choose a rate-limit identity without trusting spoofable proxy headers by default.

        Set OMARAI_TRUST_PROXY_HEADERS=1 only when the deployment's trusted reverse
        proxy appends the actual client IP as the rightmost X-Forwarded-For value.
        """
        direct_ip = self.client_address[0]
        if os.getenv("OMARAI_TRUST_PROXY_HEADERS", "").strip() != "1":
            return direct_ip
        forwarded = self.headers.get("X-Forwarded-For", "")
        candidate = forwarded.rsplit(",", 1)[-1].strip() if forwarded else ""
        try:
            return str(ipaddress.ip_address(candidate))
        except ValueError:
            return direct_ip

    def _rate_limit_ok(self):
        client_ip = self._rate_limit_client_key()
        now = time.monotonic()
        cls = type(self)
        with self._rate_lock:
            # Periodically remove IP buckets whose entire sliding window has expired.
            # Without this sweep, a public endpoint could retain one empty deque per
            # distinct client IP forever, even though the rate-limit window is 60 sec.
            if now - cls._rate_last_cleanup >= cls.RATE_LIMIT_CLEANUP_INTERVAL_SECONDS:
                cutoff = now - cls.RATE_LIMIT_WINDOW_SECONDS
                for key, timestamps in list(cls._request_times.items()):
                    while timestamps and timestamps[0] <= cutoff:
                        timestamps.popleft()
                    if not timestamps:
                        cls._request_times.pop(key, None)
                cls._rate_last_cleanup = now

            events = cls._request_times[client_ip]
            while events and now - events[0] >= cls.RATE_LIMIT_WINDOW_SECONDS:
                events.popleft()
            if len(events) >= cls.RATE_LIMIT_REQUESTS:
                return False
            events.append(now)
            return True

    def _read_request_body(self) -> bytes | None:
        """Read a bounded body with both idle and absolute wall-clock deadlines."""
        raw_size = self.headers.get("Content-Length", "").strip()
        if not raw_size or not raw_size.isascii() or not raw_size.isdecimal():
            self.respond(400, {"error": "valid Content-Length is required"})
            return None
        try:
            size = int(raw_size)
        except ValueError:
            self.respond(400, {"error": "valid Content-Length is required"})
            return None
        if size <= 0:
            self.respond(400, {"error": "request body is required"})
            return None
        if size > MAX_REQUEST_BODY_BYTES:
            self.respond(413, {"error": "request too large"})
            return None

        total_timeout = max(
            0.1,
            min(
                float(REQUEST_BODY_READ_TIMEOUT_SECONDS),
                MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS,
            ),
        )
        idle_timeout = max(
            0.1,
            min(
                float(REQUEST_BODY_IDLE_TIMEOUT_SECONDS),
                MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS,
            ),
        )
        deadline = time.monotonic() + total_timeout
        previous_timeout = self.connection.gettimeout()
        body = bytearray()
        timed_out = False
        try:
            while len(body) < size:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    timed_out = True
                    break
                self.connection.settimeout(min(idle_timeout, remaining))
                try:
                    # read1 performs at most one underlying read, letting us re-check
                    # the absolute deadline between body fragments.
                    chunk = self.rfile.read1(
                        min(size - len(body), REQUEST_BODY_READ_CHUNK_BYTES)
                    )
                except TimeoutError:
                    timed_out = True
                    break
                if not chunk:
                    break
                body.extend(chunk)
        finally:
            try:
                self.connection.settimeout(previous_timeout)
            except OSError:
                pass

        if timed_out:
            self.close_connection = True
            self.respond(408, {"error": "request body read timed out"})
            return None
        if len(body) != size:
            self.close_connection = True
            self.respond(400, {"error": "incomplete request body"})
            return None
        return bytes(body)

    def end_headers(self):
        """Apply defensive browser headers to successful and error responses alike."""
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'; "
            "form-action 'self'; connect-src 'self'; img-src 'self' data:; "
            "style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; font-src 'self' data:",
        )
        super().end_headers()

    def respond(self, status, payload, content_type="application/json; charset=utf-8"):
        body = payload.encode() if isinstance(payload, str) else json.dumps(payload, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        origin = self.headers.get("Origin")
        if origin and self._origin_allowed(origin):
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path in {"/", "/agent"}:
            if not AGENT_DASHBOARD.exists():
                return self.respond(404, {"error": "agent dashboard missing"})
            return self.respond(200, AGENT_DASHBOARD.read_text(encoding="utf-8"), "text/html; charset=utf-8")
        if parsed.path == "/leads":
            if not LEADS_DASHBOARD.exists():
                return self.respond(404, {"error": "leads dashboard missing"})
            return self.respond(200, LEADS_DASHBOARD.read_text(encoding="utf-8"), "text/html; charset=utf-8")
        if parsed.path == "/api/health":
            return self.respond(
                200,
                {
                    "ok": True,
                    "app": "Omarai",
                    "mode": "web-research",
                    "agent": WebAgent.status(),
                    "build": {
                        "sha": _build_sha(),
                        "sha_status": (
                            "available" if _build_sha() != "unknown" else "unknown"
                        ),
                    },
                },
            )
        if parsed.path == "/api/leads":
            if not self._rate_limit_ok():
                return self.respond(429, {"error": "تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة."})
            if not self._authorized():
                return self.respond(401, {"error": "يلزم رمز الوصول الخاص بالتطبيق."})
            q = parse_qs(parsed.query)
            try:
                limit = max(1, min(int(q.get("limit", ["100"])[0]), 500))
                leads = self.store.list(q.get("status", [None])[0], limit)
            except (ValueError, TypeError):
                return self.respond(400, {"error": "invalid status or limit"})
            return self.respond(200, {"leads": leads, "count": len(leads)})
        return self.respond(404, {"error": "not found"})

    def do_POST(self):
        try:
            # Count API attempts before origin/content-type/body validation so invalid
            # credentials and malformed requests cannot bypass per-client throttling.
            path = urlparse(self.path).path
            if path.startswith("/api/") and not self._rate_limit_ok():
                return self.respond(429, {"error": "تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة."})
            if path.startswith("/api/") and not self._authorized():
                return self.respond(401, {"error": "يلزم رمز الوصول الخاص بالتطبيق."})

            content_type = self.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()
            if content_type != "application/json":
                return self.respond(415, {"error": "Content-Type must be application/json"})
            origin = self.headers.get("Origin")
            if origin and not self._origin_allowed(origin):
                return self.respond(403, {"error": "cross-origin requests are not allowed"})

            raw_body = self._read_request_body()
            if raw_body is None:
                return
            data = json.loads(raw_body)
            if not isinstance(data, dict):
                return self.respond(400, {"error": "request body must be a JSON object"})
            if path == "/api/diagnostics":
                test_model = data.get("test_model", True)
                test_social = data.get("test_social", False)
                if not isinstance(test_model, bool) or not isinstance(test_social, bool):
                    return self.respond(
                        400,
                        {"error": "test_model and test_social must be booleans"},
                    )
                return self._run_bounded_agent_operation(
                    lambda: WebAgent().diagnostics(
                        test_model=test_model,
                        test_social=test_social,
                    )
                )

            if path == "/api/agent":
                question = data.get("question", "")
                if not isinstance(question, str) or not question.strip():
                    return self.respond(400, {"error": "question must be a non-empty string"})
                agent = WebAgent()
                history = data.get("history", [])
                if "mode" not in data:
                    return self._run_bounded_agent_operation(
                        lambda: agent.answer(question, history)
                    )
                return self._run_bounded_agent_operation(
                    lambda: agent.answer(question, history, data.get("mode"))
                )

            if path == "/api/ask":
                question = data.get("question", "")
                if not isinstance(question, str) or not question.strip():
                    return self.respond(400, {"error": "question must be a non-empty string"})
                if len(question) > 1000:
                    return self.respond(400, {"error": "question must be at most 1000 characters"})
                return self.respond(200, answer_question(question, self.store))
            if path == "/api/analyze":
                return self.respond(
                    200,
                    analyze(
                        data.get("text", ""),
                        data.get("product_terms", []),
                        data.get("location_terms", []),
                    ),
                )
            if path == "/api/leads":
                lead, created = self.store.add(
                    data.get("text", ""),
                    data.get("source_url", ""),
                    data.get("platform", "manual"),
                    data.get("observed_at"),
                    data.get("note", ""),
                    data.get("product_terms", []),
                    data.get("location_terms", []),
                )
                return self.respond(201 if created else 200, {"lead": lead, "created": created})
            route = path.split("/")
            if len(route) == 5 and route[1:3] == ["api", "leads"] and route[4] == "status":
                lead = self.store.update_status(route[3], data.get("status", "new"))
                return self.respond(200, {"lead": lead}) if lead else self.respond(404, {"error": "lead not found"})
            return self.respond(404, {"error": "not found"})
        except (ValueError, TypeError, json.JSONDecodeError) as exc:
            return self.respond(400, {"error": str(exc)})
        except Exception:  # noqa: BLE001 — keep unexpected details out of API responses
            return self.respond(500, {"error": "internal server error"})

    def do_OPTIONS(self):
        origin = self.headers.get("Origin")
        if not origin or not self._origin_allowed(origin):
            return self.respond(403, {"error": "cross-origin requests are not allowed"})
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", origin)
        self.send_header("Vary", "Origin")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Authorization, Content-Type")
        self.send_header("Access-Control-Max-Age", "600")
        self.send_header("Content-Length", "0")
        self.end_headers()

    def log_message(self, *args):
        pass


def answer_question(question, store):
    """Answer common operational questions from local records using explicit rules."""
    normalized = normalize(question)
    leads = store.list(limit=500)
    active = [lead for lead in leads if lead["status"] not in {"rejected", "converted"}]
    if any(term in normalized for term in ("افضل عميل", "احسن عميل", "افضل اشارة", "احسن اشارة", "اشارة اراجعها", "مين افضل", "مين اتابع", "اتابع مين", "اهم عميل")):
        if not active:
            return {"answer": "لا توجد إشارة نشطة محفوظة بعد. حلّل نصًا من مصدر مسموح واحفظه أولًا، ثم اسألني مرة أخرى.", "kind": "no_data", "lead_id": None}
        lead = max(active, key=lambda item: (item["assessment"]["score"], item["updated_at"]))
        assessment = lead["assessment"]
        answer = "الأولوية المقترحة للمراجعة هي الإشارة " + lead["id"][:8] + " بدرجة قواعد " + str(assessment["score"]) + "/100. السبب: " + assessment["summary"] + " المصدر: " + lead["source_url"] + ". هذه أولوية مراجعة وليست تأكيدًا أن صاحبه سيشتري."
        return {"answer": answer, "kind": "lead_recommendation", "lead_id": lead["id"]}
    if any(term in normalized for term in ("كام عميل", "كم عميل", "عدد العملاء", "عدد الاشارات", "الاحصائيات", "احصائيات")):
        keys = ("new", "qualified", "contacted", "converted", "needs_review", "rejected")
        by_status = {key: sum(lead["status"] == key for lead in leads) for key in keys}
        high = sum(lead["assessment"]["label"] == "high_intent" for lead in leads)
        answer = "في السجل المحلي " + str(len(leads)) + " إشارة، منها " + str(high) + " بإشارة قوية نسبيًا وفق القواعد. الحالات: جديد " + str(by_status["new"]) + "، مؤهل " + str(by_status["qualified"]) + "، تم التواصل " + str(by_status["contacted"]) + "، تم البيع " + str(by_status["converted"]) + "، تحتاج مراجعة " + str(by_status["needs_review"]) + "، مرفوض " + str(by_status["rejected"]) + "."
        return {"answer": answer, "kind": "local_statistics", "lead_id": None}
    if any(term in normalized for term in ("ليه الدرجه", "سبب الدرجه", "طريقة التقييم", "بتقيم ازاي", "معيار التقييم")):
        latest = max(leads, key=lambda item: item["updated_at"], default=None)
        if latest:
            signals = "، ".join(signal["phrase"] for signal in latest["assessment"]["matched_signals"]) or "لم تُطابق عبارات معروفة"
            answer = "الإشارة الأحدث درجتها " + str(latest["assessment"]["score"]) + "/100 لأن القواعد طابقت: " + signals + ". الدرجة ليست احتمالًا إحصائيًا ولا تثبت نية الكاتب."
        else:
            answer = "أحسب الدرجة بقواعد واضحة: تعبير الشراء، خطوة تجارية تالية، السعر أو الميزانية، وسياق المنتج والمكان. كل فئة تحتسب مرة واحدة فقط."
        return {"answer": answer, "kind": "scoring_explanation", "lead_id": latest["id"] if latest else None}
    if any(term in normalized for term in ("اكتب رساله", "اكتب رسالة", "رساله تواصل", "رسالة تواصل", "ابعتله", "اتواصل ازاي")):
        if not active:
            answer = "لا توجد إشارة محفوظة أخصص مسودة لها بعد. أدخل نصًا ومصدرًا أولًا."
        else:
            lead = max(active, key=lambda item: (item["assessment"]["score"], item["updated_at"]))
            answer = "مسودة للمراجعة البشرية فقط: «أهلًا، لاحظت سؤالك المنشور عن العقار/الوحدة. لو ما زلت مهتمًا، هل تحب الاطلاع على التفاصيل المتاحة وخيارات المعاينة؟» مرتبطة بالإشارة " + lead["id"][:8] + ". لم يتم إرسال أي رسالة."
        return {"answer": answer, "kind": "message_draft", "lead_id": active[0]["id"] if active else None}
    return {"answer": "أنا المساعد المحلي الخاص بسجل العملاء. استخدم وكيل البحث العام من الصفحة الرئيسية لطرح أسئلة مفتوحة والبحث في الويب.", "kind": "help", "lead_id": None}


def serve(host="127.0.0.1", port=8765):
    public_deployment = os.getenv("OMARAI_PUBLIC_DEPLOYMENT", "").strip() == "1"
    access_token = os.getenv("OMARAI_ACCESS_TOKEN", "").strip()
    if host not in ("127.0.0.1", "localhost", "::1") and (
        not public_deployment or len(access_token) < 32
    ):
        raise ValueError(
                "Public binding requires OMARAI_PUBLIC_DEPLOYMENT=1 and "
                "a private OMARAI_ACCESS_TOKEN of at least 32 characters."
            )
    server = ThreadingHTTPServer((host, port), Handler)
    server.daemon_threads = True
    print(f"Omarai running at http://{host}:{port} — Ctrl+C to stop")
    print("Web research agent: /   |   Lead workspace: /leads")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    serve()
