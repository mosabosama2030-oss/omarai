from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

import pytest

from scripts import hosted_smoke_test
from scripts.hosted_smoke_test import SmokeError, normalize_origin, run_smoke

TOKEN = "local-test-token-long-enough-for-the-32-character-rule"


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        return

    def respond(self, status: int, payload: dict[str, object]) -> None:
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/api/health":
            self.respond(200, {"ok": True, "app": "Omarai", "agent": {}})
        else:
            self.respond(404, {"error": "not found"})

    def do_POST(self) -> None:
        if self.headers.get("Authorization") != f"Bearer {TOKEN}":
            self.respond(401, {"error": "unauthorized"})
            return
        length = int(self.headers.get("Content-Length", "0"))
        request = json.loads(self.rfile.read(length) or b"{}")
        if self.path == "/api/diagnostics":
            self.respond(200, {
                "overall_status": "passed",
                "checks": {
                    "web_search": {
                        "status": "passed", "result_count": 2,
                        "provider_counts": {"bing_rss": 1, "duckduckgo_html": 1},
                    },
                    "language_model": {"status": "passed", "response_received": True},
                    "social_search": {"status": "skipped"},
                },
            })
        elif self.path == "/api/agent":
            self.respond(200, {
                "answer": "القاهرة هي عاصمة مصر. [المصدر 1]",
                "used_web_search": True,
                "used_language_model": True,
                "sources": [{"title": "مصدر اختبار", "url": "https://example.com/source"}],
                "search_report": {"providers_used": ["bing_rss"], "pages_fetched": 1},
            })
        else:
            self.respond(404, {"error": "not found"})


@pytest.fixture
def hosted_server():
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


def test_normalize_origin_requires_https_and_rejects_credentials_or_paths():
    assert normalize_origin("https://example.com/") == "https://example.com"
    for invalid in (
        "http://example.com",
        "https://user:password@example.com",
        "https://example.com/path",
        "https://example.com/?token=secret",
    ):
        with pytest.raises(SmokeError):
            normalize_origin(invalid)


def test_normalize_origin_allows_plain_http_only_for_local_test():
    assert normalize_origin("http://127.0.0.1:8765", allow_http=True) == (
        "http://127.0.0.1:8765"
    )
    with pytest.raises(SmokeError):
        normalize_origin("http://example.com", allow_http=True)


def test_smoke_checks_health_auth_live_diagnostics_and_agent(hosted_server):
    result = run_smoke(hosted_server, TOKEN, allow_http=True, timeout=5)
    assert result["result"] == "passed"
    assert result["checks"]["health"] == "passed"
    assert result["checks"]["authentication"] == "passed"
    assert result["checks"]["live_search"]["result_count"] == 2
    assert result["checks"]["agent_request"]["source_count"] == 1


def test_smoke_refuses_missing_or_short_access_token(hosted_server):
    with pytest.raises(SmokeError, match="OMARAI_ACCESS_TOKEN"):
        run_smoke(hosted_server, "", allow_http=True, timeout=5)


def test_smoke_fails_when_agent_returns_no_live_source(hosted_server, monkeypatch):
    original = hosted_smoke_test.request_json

    def without_sources(url: str, **kwargs):
        if urlsplit(url).path == "/api/agent" and kwargs.get("token") == TOKEN:
            return 200, {
                "answer": "إجابة بلا مصادر", "used_web_search": False,
                "used_language_model": True, "sources": [],
            }
        return original(url, **kwargs)

    monkeypatch.setattr(hosted_smoke_test, "request_json", without_sources)
    with pytest.raises(SmokeError, match="usable source URLs"):
        run_smoke(hosted_server, TOKEN, allow_http=True, timeout=5)
