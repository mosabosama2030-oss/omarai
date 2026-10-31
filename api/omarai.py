"""HTTP API for Omarai's web-research agent and lead workspace."""
from __future__ import annotations

import base64
import hashlib
import hmac
import ipaddress
import json
import os
import re
import threading
import time
from collections import defaultdict, deque
from functools import lru_cache
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


def _csp_hash_source(value: str) -> str:
    digest = base64.b64encode(hashlib.sha256(value.encode("utf-8")).digest()).decode("ascii")
    return f"'sha256-{digest}'"


@lru_cache(maxsize=1)
def _content_security_policy() -> str:
    """Allow only known inline blocks/attributes from the static first-party HTML.

    Hashes deliberately replace unsafe-inline. Updating an inline script/style means its
    hash changes automatically with the served source. This is not a sanitizer for
    untrusted HTML; callers must never splice untrusted input into these static files.
    """
    script_hashes: set[str] = set()
    style_hashes: set[str] = set()
    event_handler_hashes: set[str] = set()
    style_attribute_hashes: set[str] = set()

    for html_path in sorted(ROOT.glob("*.html")):
        try:
            document = html_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue

        for match in re.finditer(
            r"<script\b(?P<attrs>[^>]*)>(?P<body>.*?)</script\s*>",
            document,
            re.IGNORECASE | re.DOTALL,
        ):
            if re.search(r"\bsrc\s*=", match.group("attrs"), re.IGNORECASE):
                continue
            script_hashes.add(_csp_hash_source(match.group("body")))

        for match in re.finditer(
            r"<style\b[^>]*>(?P<body>.*?)</style\s*>",
            document,
            re.IGNORECASE | re.DOTALL,
        ):
            style_hashes.add(_csp_hash_source(match.group("body")))

        # This scan intentionally includes style/event attributes embedded in
        # trusted first-party HTML templates assembled by inline scripts.
        for match in re.finditer(
            r"""\bstyle\s*=\s*(["'])(.*?)\1""",
            document,
            re.IGNORECASE | re.DOTALL,
        ):
            style_attribute_hashes.add(_csp_hash_source(match.group(2).strip()))

        for match in re.finditer(
            r"""\bon[a-z]+\s*=\s*(["'])(.*?)\1""",
            document,
            re.IGNORECASE | re.DOTALL,
        ):
            event_handler_hashes.add(_csp_hash_source(match.group(2).strip()))

    script_sources = ["'self'", *sorted(script_hashes)]
    style_sources = ["'self'", *sorted(style_hashes)]
    if event_handler_hashes:
        script_sources.extend(["'unsafe-hashes'", *sorted(event_handler_hashes)])
    if style_attribute_hashes:
        style_sources.extend(["'unsafe-hashes'", *sorted(style_attribute_hashes)])

    return (
        "default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'; "
        "form-action 'self'; connect-src 'self'; img-src 'self' data:; "
        f"script-src {' '.join(script_sources)}; "
        f"style-src {' '.join(style_sources)}; font-src 'self' data:"
    )
# Bound request-line + header parsing before application code or body processing.
REQUEST_HEADER_READ_TIMEOUT_SECONDS = 8.0
REQUEST_HEADER_IDLE_TIMEOUT_SECONDS = 2.0
MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS = 15.0
# Absolute deadline for reading the entire body, not merely a per-read idle timeout.
REQUEST_BODY_READ_TIMEOUT_SECONDS = 10.0
REQUEST_BODY_IDLE_TIMEOUT_SECONDS = 2.0
MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS = 30.0
REQUEST_BODY_READ_CHUNK_BYTES = 8_192



def _lead_store_from_environment() -> LeadStore:
    """Use the configured database and the initial single-company tenant identity."""
    configured_path = os.getenv("OMARAI_DB_PATH", "").strip()
    return LeadStore(
        configured_path or None,
        default_tenant_id=os.getenv("OMARAI_DEFAULT_TENANT_ID", "default").strip() or "default",
        default_tenant_name=os.getenv(
            "OMARAI_DEFAULT_TENANT_NAME", "المنشأة الرئيسية"
        ).strip() or "المنشأة الرئيسية",
    )


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


DEFAULT_HTTP_CONNECTION_LIMIT = 32
MAX_HTTP_CONNECTION_LIMIT = 128


def _configured_http_connection_limit() -> int:
    """Return the bounded number of live HTTP handler threads for this process."""
    try:
        configured = int(os.getenv("OMARAI_MAX_CONCURRENT_HTTP_CONNECTIONS", "32").strip())
    except ValueError:
        configured = DEFAULT_HTTP_CONNECTION_LIMIT
    return max(1, min(configured, MAX_HTTP_CONNECTION_LIMIT))


BUILD_SHA_FILE = Path(__file__).resolve().parents[1] / "BUILD_SHA"
_PLATFORM_BUILD_SHA_ENVIRONMENTS = (
    ("RAILWAY_GIT_COMMIT_SHA", "platform:railway"),
    ("RENDER_GIT_COMMIT", "platform:render"),
)


def _valid_build_sha(value: str) -> bool:
    candidate = value.strip().lower()
    return len(candidate) == 40 and all(char in "0123456789abcdef" for char in candidate)


def _build_identity() -> tuple[str, str]:
    """Prefer immutable image metadata, then documented hosting-provided Git SHAs."""
    try:
        baked = BUILD_SHA_FILE.read_text(encoding="ascii").strip().lower()
    except (OSError, UnicodeError):
        baked = ""
    if _valid_build_sha(baked):
        return baked, "image_baked"

    for environment_name, source in _PLATFORM_BUILD_SHA_ENVIRONMENTS:
        candidate = os.getenv(environment_name, "").strip().lower()
        if _valid_build_sha(candidate):
            return candidate, source
    return "unknown", "unknown"


def _build_sha() -> str:
    """Return a validated source SHA, or 'unknown' when no trusted build evidence exists."""
    return _build_identity()[0]


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

    store = _lead_store_from_environment()
    _rate_lock = threading.Lock()
    _request_times: ClassVar[dict[str, deque[float]]] = defaultdict(deque)
    _rate_last_cleanup: ClassVar[float] = 0.0
    RATE_LIMIT_REQUESTS = 20
    RATE_LIMIT_WINDOW_SECONDS = 60
    RATE_LIMIT_CLEANUP_INTERVAL_SECONDS = 60
    # Reserve the final bucket for clients beyond the per-process tracking ceiling.
    MAX_RATE_LIMIT_CLIENT_BUCKETS = 4096
    RATE_LIMIT_OVERFLOW_KEY = "__omarai_overflow__"
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

    @staticmethod
    def _is_loopback_address(value: str) -> bool:
        try:
            address = ipaddress.ip_address(str(value).split("%", 1)[0])
        except ValueError:
            return False
        return address.is_loopback or bool(
            getattr(address, "ipv4_mapped", None)
            and address.ipv4_mapped.is_loopback
        )

    def _is_loopback_test_request(self) -> bool:
        """Allow the tokenless test identity only on a loopback-bound local server."""
        bind_host = self.server.server_address[0]
        peer_host = self.client_address[0]
        return (
            os.getenv("OMARAI_TEST_MODE", "").strip() == "1"
            and os.getenv("OMARAI_PUBLIC_DEPLOYMENT", "").strip() != "1"
            and self._is_loopback_address(bind_host)
            and self._is_loopback_address(peer_host)
        )

    def _authenticated_user_id(self) -> str | None:
        """Resolve a user identity from a token or the isolated loopback test harness."""
        expected = os.getenv("OMARAI_ACCESS_TOKEN", "").strip()
        supplied = self.headers.get("Authorization", "")
        if expected:
            if not supplied.startswith("Bearer "):
                return None
            if not hmac.compare_digest(supplied[7:].strip(), expected):
                return None
            user_id = os.getenv("OMARAI_ACCESS_USER_ID", "operator").strip()
            return user_id or None

        if self._is_loopback_test_request():
            user_id = (
                self.headers.get("X-Omarai-Test-User", "").strip()
                or os.getenv("OMARAI_TEST_USER_ID", "operator").strip()
            )
            return user_id or None
        return None

    def _authorized(self):
        return self._authenticated_user_id() is not None

    def _resolve_request_membership(self, requested_tenant_id: str | None = None):
        user_id = self._authenticated_user_id()
        if not user_id:
            return None
        try:
            return self.store.resolve_membership(user_id, requested_tenant_id)
        except ValueError:
            return None

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

            if (
                client_ip not in cls._request_times
                and len(cls._request_times) >= max(1, cls.MAX_RATE_LIMIT_CLIENT_BUCKETS) - 1
            ):
                # Bound attacker-controlled cardinality. Excess identities share a
                # conservative overflow bucket instead of allocating one deque per IP.
                client_ip = cls.RATE_LIMIT_OVERFLOW_KEY
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
        self.send_header("Content-Security-Policy", _content_security_policy())
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
                        "sha": _build_identity()[0],
                        "sha_status": (
                            "available" if _build_identity()[0] != "unknown" else "unknown"
                        ),
                        "sha_source": _build_identity()[1],
                    },
                },
            )
        if parsed.path in {"/api/leads", "/api/leads/export.csv"}:
            if not self._rate_limit_ok():
                return self.respond(429, {"error": "تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة."})
            if not self._authorized():
                return self.respond(401, {"error": "يلزم مستخدم مصرح به للوصول إلى بيانات العملاء."})
            q = parse_qs(parsed.query)
            requested_tenant = q.get("tenant_id", [None])[0]
            membership = self._resolve_request_membership(requested_tenant)
            if not membership:
                return self.respond(403, {"error": "لا توجد عضوية نشطة للمستخدم في الشركة المطلوبة."})
            tenant_id = membership["tenant_id"]
            if parsed.path == "/api/leads/export.csv":
                if membership["role"] not in {"owner", "admin", "manager"}:
                    return self.respond(403, {"error": "تصدير بيانات العملاء يتطلب دور إدارة الشركة."})
                csv_text = "\ufeff" + self.store.export_csv_text(tenant_id=tenant_id)
                return self.respond(
                    200,
                    csv_text,
                    "text/csv; charset=utf-8",
                )
            try:
                limit = max(1, min(int(q.get("limit", ["100"])[0]), 500))
                leads = self.store.list(
                    q.get("status", [None])[0], limit, tenant_id=tenant_id
                )
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
                return self.respond(401, {"error": "يلزم رمز الوصول وهوية مستخدم مصرح بها، أو بيئة اختبار محلية."})

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

            user_id = self._authenticated_user_id()
            if path.startswith("/api/") and not user_id:
                return self.respond(401, {"error": "تعذر تحديد هوية المستخدم لهذا الطلب."})
            requested_tenant = data.get("tenant_id")
            header_tenant = self.headers.get("X-Omarai-Tenant-ID", "").strip()
            if requested_tenant is not None and not isinstance(requested_tenant, str):
                return self.respond(400, {"error": "tenant_id must be a string"})
            if requested_tenant and header_tenant and requested_tenant.strip() != header_tenant:
                return self.respond(400, {"error": "conflicting tenant selections"})
            requested_tenant = (requested_tenant or header_tenant or "").strip() or None
            membership = self._resolve_request_membership(requested_tenant)
            if path.startswith("/api/") and not membership:
                return self.respond(403, {"error": "لا توجد عضوية نشطة للمستخدم في الشركة المطلوبة."})
            tenant_id = membership["tenant_id"] if membership else None
            tenant_role = membership["role"] if membership else None
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
                return self.respond(
                    200, answer_question(question, self.store, tenant_id=tenant_id)
                )
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
                if tenant_role not in {"owner", "admin", "manager", "sales_agent"}:
                    return self.respond(403, {"error": "دور المستخدم لا يسمح بإضافة فرص إلى الشركة."})
                lead, created = self.store.add(
                    data.get("text", ""),
                    data.get("source_url", ""),
                    data.get("platform", "manual"),
                    data.get("observed_at"),
                    data.get("note", ""),
                    data.get("product_terms", []),
                    data.get("location_terms", []),
                    tenant_id=tenant_id,
                )
                return self.respond(201 if created else 200, {"lead": lead, "created": created})
            route = path.split("/")
            if len(route) == 5 and route[1:3] == ["api", "leads"] and route[4] == "status":
                if tenant_role not in {"owner", "admin", "manager", "sales_agent"}:
                    return self.respond(403, {"error": "دور المستخدم لا يسمح بتعديل الفرص."})
                lead = self.store.update_status(
                    route[3], data.get("status", "new"), tenant_id=tenant_id
                )
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
        self.send_header(
            "Access-Control-Allow-Headers",
            "Authorization, Content-Type, X-Omarai-Test-User, X-Omarai-Tenant-ID",
        )
        self.send_header("Access-Control-Max-Age", "600")
        self.send_header("Content-Length", "0")
        self.end_headers()

    def log_message(self, *args):
        pass


def answer_question(question, store, *, tenant_id: str = LeadStore.DEFAULT_TENANT_ID):
    """Answer common operational questions using only the selected company records."""
    normalized = normalize(question)
    leads = store.list(limit=500, tenant_id=tenant_id)
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


class BoundedThreadingHTTPServer(ThreadingHTTPServer):
    """Threaded HTTP server with a hard process-local ceiling on handler threads."""

    daemon_threads = True
    overload_response = (
        b"HTTP/1.1 503 Service Unavailable\r\n"
        b"Connection: close\r\n"
        b"Retry-After: 5\r\n"
        b"Content-Length: 0\r\n\r\n"
    )

    def __init__(
        self,
        server_address,
        request_handler_class,
        bind_and_activate: bool = True,
        *,
        max_concurrent_connections: int | None = None,
    ):
        super().__init__(server_address, request_handler_class, bind_and_activate)
        configured = (
            _configured_http_connection_limit()
            if max_concurrent_connections is None
            else int(max_concurrent_connections)
        )
        limit = max(1, min(configured, MAX_HTTP_CONNECTION_LIMIT))
        self.max_concurrent_connections = limit
        self._connection_slots = threading.BoundedSemaphore(limit)

    def process_request(self, request, client_address):
        """Reject excess accepted sockets before creating another handler thread."""
        if not self._connection_slots.acquire(blocking=False):
            try:
                request.sendall(self.overload_response)
            except OSError:
                pass
            finally:
                self.shutdown_request(request)
            return
        try:
            super().process_request(request, client_address)
        except BaseException:
            # Thread creation can fail before a worker owns the reserved slot.
            self._connection_slots.release()
            raise

    def process_request_thread(self, request, client_address):
        """Return a slot after the handler has shut down the accepted socket."""
        try:
            super().process_request_thread(request, client_address)
        finally:
            self._connection_slots.release()


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
    server = BoundedThreadingHTTPServer((host, port), Handler)
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
