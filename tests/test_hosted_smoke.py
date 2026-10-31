from __future__ import annotations

import json
import threading
from pathlib import Path
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
        self.rfile.read(length)
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
    result = run_smoke(
        hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5
    )
    assert result["result"] == "passed"
    assert result["checks"]["health"] == "passed"
    assert result["checks"]["authentication"] == "passed"
    assert result["checks"]["live_search"]["result_count"] == 2
    assert result["checks"]["agent_request"]["source_count"] == 1


def test_smoke_never_forwards_bearer_to_cross_origin_redirect():
    received_authorizations = []

    class RedirectHandler(BaseHTTPRequestHandler):
        def log_message(self, format: str, *args: object) -> None:
            return

        def do_GET(self) -> None:
            self.send_response(302)
            self.send_header("Location", self.server.redirect_destination)
            self.send_header("Content-Length", "0")
            self.end_headers()

    class DestinationHandler(BaseHTTPRequestHandler):
        def log_message(self, format: str, *args: object) -> None:
            return

        def do_GET(self) -> None:
            received_authorizations.append(self.headers.get("Authorization"))
            self.send_response(200)
            self.send_header("Content-Length", "0")
            self.end_headers()

    destination = ThreadingHTTPServer(("127.0.0.1", 0), DestinationHandler)
    source = ThreadingHTTPServer(("127.0.0.1", 0), RedirectHandler)
    destination_thread = threading.Thread(target=destination.serve_forever, daemon=True)
    source_thread = threading.Thread(target=source.serve_forever, daemon=True)
    source.redirect_destination = (
        f"http://127.0.0.1:{destination.server_port}/capture"
    )
    destination_thread.start()
    source_thread.start()
    try:
        status, payload = hosted_smoke_test.request_json(
            f"http://127.0.0.1:{source.server_port}/redirect",
            token=TOKEN,
            timeout=3,
        )
        assert status == 302
        assert payload is None
        assert received_authorizations == []
    finally:
        source.shutdown()
        destination.shutdown()
        source.server_close()
        destination.server_close()
        source_thread.join(timeout=2)
        destination_thread.join(timeout=2)


def test_smoke_refuses_missing_or_short_access_token(hosted_server):
    with pytest.raises(SmokeError, match="OMARAI_ACCESS_TOKEN"):
        run_smoke(hosted_server, "", allow_http=True, allow_provider_usage=True, timeout=5)


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
    with pytest.raises(SmokeError, match="usable source URLs") as failure:
        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)
    assert failure.value.report["transcript"][0]["question"] == (
        hosted_smoke_test.LIVE_TEST_QUESTION
    )
    assert failure.value.report["transcript"][0]["answer"] == "إجابة بلا مصادر"


def test_smoke_rejects_invalid_expected_source_sha(hosted_server):
    with pytest.raises(SmokeError, match="40-character Git SHA"):
        run_smoke(
            hosted_server, TOKEN, allow_http=True, timeout=5, expected_sha="main"
        )


def test_smoke_rejects_deployed_build_sha_mismatch(hosted_server):
    with pytest.raises(SmokeError, match="does not match the expected Git commit"):
        run_smoke(
            hosted_server,
            TOKEN,
            allow_http=True,
            allow_provider_usage=True,
            timeout=5,
            expected_sha="a" * 40,
        )


def test_smoke_requires_explicit_provider_usage_approval_before_network(monkeypatch):
    calls = []

    def unexpected_request(*args, **kwargs):
        calls.append((args, kwargs))
        raise AssertionError("network must not be called without explicit approval")

    monkeypatch.setattr(hosted_smoke_test, "request_json", unexpected_request)
    with pytest.raises(SmokeError, match="explicit human approval"):
        run_smoke(
            "https://omarai.example.test",
            TOKEN,
            allow_provider_usage=False,
            expected_sha="a" * 40,
        )
    assert calls == []


def test_hosted_smoke_workflow_is_manual_and_cost_gated():
    workflow = Path(".github/workflows/hosted-smoke.yml").read_text(encoding="utf-8")
    assert "schedule:" not in workflow
    assert "allow_provider_usage:" in workflow
    assert "default: false" in workflow
    assert "--allow-provider-usage" in workflow
