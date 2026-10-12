"""Loopback-only HTTP API for Omarai's web-research agent and lead workspace."""
from __future__ import annotations

import hmac
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


class Handler(BaseHTTPRequestHandler):
    store = LeadStore()
    _rate_lock = threading.Lock()
    _request_times: ClassVar[dict[str, deque[float]]] = defaultdict(deque)
    RATE_LIMIT_REQUESTS = 20
    RATE_LIMIT_WINDOW_SECONDS = 60

    def _authorized(self):
        expected = os.getenv("OMARAI_ACCESS_TOKEN", "").strip()
        if not expected:
            return os.getenv("OMARAI_PUBLIC_DEPLOYMENT", "").strip() != "1"
        supplied = self.headers.get("Authorization", "")
        if not supplied.startswith("Bearer "):
            return False
        return hmac.compare_digest(supplied[7:].strip(), expected)

    def _rate_limit_ok(self):
        forwarded = self.headers.get("X-Forwarded-For", "")
        client_ip = forwarded.split(",", 1)[0].strip() if forwarded else self.client_address[0]
        now = time.monotonic()
        with self._rate_lock:
            events = self._request_times[client_ip]
            while events and now - events[0] >= self.RATE_LIMIT_WINDOW_SECONDS:
                events.popleft()
            if len(events) >= self.RATE_LIMIT_REQUESTS:
                return False
            events.append(now)
            return True

    def respond(self, status, payload, content_type="application/json; charset=utf-8"):
        body = payload.encode() if isinstance(payload, str) else json.dumps(payload, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-store")
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
                },
            )
        if parsed.path == "/api/leads":
            if not self._authorized():
                return self.respond(401, {"error": "يلزم رمز الوصول الخاص بالتطبيق."})
            if not self._rate_limit_ok():
                return self.respond(429, {"error": "تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة."})
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
            content_type = self.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()
            if content_type != "application/json":
                return self.respond(415, {"error": "Content-Type must be application/json"})
            origin = self.headers.get("Origin")
            port = self.server.server_port
            allowed_origins = {
                "http://127.0.0.1:" + str(port),
                "http://localhost:" + str(port),
                "http://[::1]:" + str(port),
            }
            if os.getenv("OMARAI_PUBLIC_DEPLOYMENT", "").strip() == "1":
                scheme = self.headers.get("X-Forwarded-Proto", "https").split(",", 1)[0].strip()
                host = self.headers.get("Host", "")
                if host:
                    allowed_origins.add(scheme + "://" + host)
            if origin and origin not in allowed_origins:
                return self.respond(403, {"error": "cross-origin requests are not allowed"})
            size = int(self.headers.get("Content-Length", "0"))
            if size <= 0:
                return self.respond(400, {"error": "request body is required"})
            if size > 200_000:
                return self.respond(413, {"error": "request too large"})
            data = json.loads(self.rfile.read(size))
            if not isinstance(data, dict):
                return self.respond(400, {"error": "request body must be a JSON object"})
            path = urlparse(self.path).path

            # Public deployments require the owner's private token and a request limit.
            if path.startswith("/api/") and not self._authorized():
                return self.respond(401, {"error": "يلزم رمز الوصول الخاص بالتطبيق."})
            if path.startswith("/api/") and not self._rate_limit_ok():
                return self.respond(429, {"error": "تجاوزت حد الطلبات المؤقت؛ حاول بعد دقيقة."})

            if path == "/api/diagnostics":
                test_model = data.get("test_model", True)
                test_social = data.get("test_social", False)
                if not isinstance(test_model, bool) or not isinstance(test_social, bool):
                    return self.respond(
                        400,
                        {"error": "test_model and test_social must be booleans"},
                    )
                return self.respond(
                    200,
                    WebAgent().diagnostics(
                        test_model=test_model,
                        test_social=test_social,
                    ),
                )

            if path == "/api/agent":
                question = data.get("question", "")
                if not isinstance(question, str) or not question.strip():
                    return self.respond(400, {"error": "question must be a non-empty string"})
                agent = WebAgent()
                history = data.get("history", [])
                if "mode" not in data:
                    return self.respond(200, agent.answer(question, history))
                return self.respond(200, agent.answer(question, history, data.get("mode")))

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
        return self.respond(405, {"error": "cross-origin requests are not supported"})

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
