"""HTTP integration tests for Omarai local API and assistant endpoints."""
from __future__ import annotations

import json
import re
import socket
import threading
from collections import defaultdict, deque
from http.server import ThreadingHTTPServer
from pathlib import Path
from types import SimpleNamespace
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import pytest

from agents.omarai import LeadStore
from api.omarai import Handler


@pytest.fixture
def local_api(tmp_path):
    """Run the real handler on an ephemeral loopback port with an isolated database."""
    previous_store = Handler.store
    Handler.store = LeadStore(tmp_path / "api-test.sqlite3")
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=3)
        Handler.store = previous_store


def request_json(base, path, method="GET", payload=None, headers=None):
    body = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request_headers = dict(headers or {})
    if body is not None and "Content-Type" not in request_headers:
        request_headers["Content-Type"] = "application/json"
    request = Request(base + path, data=body, method=method, headers=request_headers)
    try:
        with urlopen(request, timeout=3) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        return error.code, json.loads(error.read().decode("utf-8"))


def test_api_health_analyze_save_duplicate_list_and_status(local_api):
    status, health = request_json(local_api, "/api/health")
    assert status == 200
    assert health["app"] == "Omarai"
    assert health["mode"] == "web-research"
    assert health["agent"]["verification_scope"]["live_network_checks_performed"] is False
    assert health["agent"]["verification_scope"]["live_diagnostics_endpoint"] == "POST /api/diagnostics"

    text = "بدور على شقة في التجمع الخامس وممكن معاينة"
    status, assessment = request_json(
        local_api,
        "/api/analyze",
        method="POST",
        payload={"text": text, "product_terms": ["شقة"], "location_terms": ["التجمع الخامس"]},
    )
    assert status == 200
    assert assessment["label"] == "high_intent"
    assert {item["category"] for item in assessment["matched_signals"]} >= {
        "high", "next_step", "product_context", "location_context"
    }

    payload = {
        "text": text,
        "source_url": "https://example.com/posts/123",
        "platform": "Public website",
        "product_terms": ["شقة"],
        "location_terms": ["التجمع الخامس"],
    }
    status, saved = request_json(local_api, "/api/leads", method="POST", payload=payload)
    assert status == 201
    assert saved["created"] is True
    assert saved["lead"]["assessment"]["label"] == "high_intent"
    assert "product_context" in {
        item["category"] for item in saved["lead"]["assessment"]["matched_signals"]
    }
    status, duplicate = request_json(local_api, "/api/leads", method="POST", payload=payload)
    assert status == 200
    assert duplicate["created"] is False

    status, listing = request_json(local_api, "/api/leads?limit=25")
    assert status == 200
    assert listing["count"] == 1
    lead_id = listing["leads"][0]["id"]

    status, changed = request_json(
        local_api,
        f"/api/leads/{lead_id}/status",
        method="POST",
        payload={"status": "qualified"},
    )
    assert status == 200
    assert changed["lead"]["status"] == "qualified"

    status, stats = request_json(
        local_api, "/api/ask", method="POST", payload={"question": "كام عميل عندي؟"}
    )
    assert status == 200
    assert stats["kind"] == "local_statistics"
    assert "1 إشارة" in stats["answer"]

    status, recommendation = request_json(
        local_api,
        "/api/ask",
        method="POST",
        payload={"question": "مين أفضل إشارة أراجعها؟"},
    )
    assert status == 200
    assert recommendation["kind"] == "lead_recommendation"
    assert payload["source_url"] in recommendation["answer"]


def test_api_rejects_invalid_filters_and_request_shapes(local_api):
    status, error = request_json(local_api, "/api/leads?limit=not-a-number")
    assert status == 400
    assert "limit" in error["error"]

    status, error = request_json(
        local_api, "/api/analyze", method="POST", payload=["not", "an", "object"]
    )
    assert status == 400
    assert "object" in error["error"]

    status, error = request_json(
        local_api, "/api/ask", method="POST", payload={"question": ""}
    )
    assert status == 400
    assert "question" in error["error"]

    status, error = request_json(
        local_api, "/api/leads", method="POST", payload={
            "text": "بدور على شقة", "source_url": "file:///private/data", "platform": "manual"
        }
    )
    assert status == 400
    assert "absolute" in error["error"]


def test_api_blocks_non_json_and_cross_origin_posts(local_api, monkeypatch):
    monkeypatch.delenv("OMARAI_ALLOWED_ORIGINS", raising=False)
    status, error = request_json(
        local_api,
        "/api/ask",
        method="POST",
        payload={"question": "كام عميل؟"},
        headers={"Content-Type": "text/plain"},
    )
    assert status == 415
    assert "Content-Type" in error["error"]

    status, error = request_json(
        local_api,
        "/api/ask",
        method="POST",
        payload={"question": "كام عميل؟"},
        headers={"Origin": "https://attacker.example"},
    )
    assert status == 403
    assert "cross-origin" in error["error"]


def test_configured_frontend_origin_supports_preflight_and_post(local_api, monkeypatch):
    origin = "https://frontend.example"
    monkeypatch.setenv("OMARAI_ALLOWED_ORIGINS", origin)

    preflight = Request(
        local_api + "/api/agent",
        method="OPTIONS",
        headers={
            "Origin": origin,
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "authorization,content-type",
        },
    )
    with urlopen(preflight, timeout=3) as response:
        assert response.status == 204
        assert response.headers.get("Access-Control-Allow-Origin") == origin
        assert response.headers.get("Access-Control-Allow-Methods") == "GET, POST, OPTIONS"
        assert response.headers.get("Access-Control-Allow-Headers") == "Authorization, Content-Type"

    body = json.dumps({"question": "مين أفضل إشارة أراجعها؟"}, ensure_ascii=False).encode("utf-8")
    post = Request(
        local_api + "/api/ask",
        data=body,
        method="POST",
        headers={"Content-Type": "application/json", "Origin": origin},
    )
    with urlopen(post, timeout=3) as response:
        payload = json.loads(response.read().decode("utf-8"))
        assert response.status == 200
        assert response.headers.get("Access-Control-Allow-Origin") == origin
        assert payload["kind"] == "no_data"


def test_preflight_rejects_unconfigured_origin(local_api, monkeypatch):
    monkeypatch.delenv("OMARAI_ALLOWED_ORIGINS", raising=False)
    preflight = Request(
        local_api + "/api/agent",
        method="OPTIONS",
        headers={
            "Origin": "https://attacker.example",
            "Access-Control-Request-Method": "POST",
        },
    )
    with pytest.raises(HTTPError) as error:
        urlopen(preflight, timeout=3)
    assert error.value.code == 403


def test_ask_is_honest_when_database_is_empty(local_api):
    status, answer = request_json(
        local_api, "/api/ask", method="POST", payload={"question": "مين أفضل إشارة أراجعها؟"}
    )
    assert status == 200
    assert answer["kind"] == "no_data"
    assert "لا توجد إشارة" in answer["answer"]



def test_web_agent_endpoint_uses_agent_result(local_api, monkeypatch):
    from api.omarai import WebAgent

    def fake_answer(self, question, history=None):
        return {
            "answer": "إجابة اختبار [المصدر 1]",
            "question": question,
            "search_query": question,
            "sources": [{"title": "مصدر", "url": "https://example.com", "snippet": "نص", "page_fetched": False}],
            "used_language_model": True,
            "used_web_search": True,
            "warnings": [],
            "kind": "web_research",
        }

    monkeypatch.setattr(WebAgent, "answer", fake_answer)
    status, response = request_json(
        local_api,
        "/api/agent",
        method="POST",
        payload={"question": "ابحث عن موضوع", "history": []},
    )
    assert status == 200
    assert response["kind"] == "web_research"
    assert response["sources"][0]["url"] == "https://example.com"



def test_live_diagnostics_endpoint_returns_report_without_secrets(local_api, monkeypatch):
    from api.omarai import WebAgent

    def fake_diagnostics(self, test_model=True, test_social=False):
        return {
            "overall_status": "passed",
            "checks": {
                "web_search": {"status": "passed", "result_count": 4},
                "language_model": {"status": "passed", "response_received": True},
                "social_search": {"status": "skipped"},
            },
            "model_usage": [{
                "requested_model": "google/gemma-4-31b-it:free",
                "used_model": "google/gemma-4-31b-it:free",
                "fallback_used": "false",
            }],
        }

    monkeypatch.setattr(WebAgent, "diagnostics", fake_diagnostics)
    status, report = request_json(
        local_api,
        "/api/diagnostics",
        method="POST",
        payload={"test_model": True, "test_social": False, "allow_provider_usage": True},
    )
    assert status == 200
    assert report["overall_status"] == "passed"
    assert report["checks"]["web_search"]["result_count"] == 4
    assert "api_key" not in report
    assert "secret" not in str(report)


def test_diagnostics_endpoint_requires_boolean_options(local_api):
    status, error = request_json(
        local_api,
        "/api/diagnostics",
        method="POST",
        payload={"test_model": "yes", "test_social": False},
    )
    assert status == 400
    assert "booleans" in error["error"]



def test_rate_limit_ignores_spoofed_forwarded_for_by_default(monkeypatch):
    monkeypatch.delenv("OMARAI_TRUST_PROXY_HEADERS", raising=False)
    handler = SimpleNamespace(
        headers={"X-Forwarded-For": "198.51.100.77, 203.0.113.10"},
        client_address=("192.0.2.44", 12345),
    )
    assert Handler._rate_limit_client_key(handler) == "192.0.2.44"


def test_rate_limit_uses_rightmost_valid_proxy_ip_only_when_enabled(monkeypatch):
    monkeypatch.setenv("OMARAI_TRUST_PROXY_HEADERS", "1")
    handler = SimpleNamespace(
        headers={"X-Forwarded-For": "198.51.100.77, 203.0.113.10"},
        client_address=("192.0.2.44", 12345),
    )
    assert Handler._rate_limit_client_key(handler) == "203.0.113.10"


def test_rate_limit_proxy_header_invalid_value_falls_back_to_peer_ip(monkeypatch):
    monkeypatch.setenv("OMARAI_TRUST_PROXY_HEADERS", "1")
    handler = SimpleNamespace(
        headers={"X-Forwarded-For": "198.51.100.77, not-an-ip"},
        client_address=("192.0.2.44", 12345),
    )
    assert Handler._rate_limit_client_key(handler) == "192.0.2.44"


@pytest.mark.parametrize(
    ("configured", "expected"),
    [("", 32), ("invalid", 32), ("0", 1), ("12", 12), ("999", 128)],
)
def test_http_connection_limit_configuration_is_bounded(monkeypatch, configured, expected):
    from api.omarai import _configured_http_connection_limit

    monkeypatch.setenv("OMARAI_MAX_CONCURRENT_HTTP_CONNECTIONS", configured)

    assert _configured_http_connection_limit() == expected


def test_http_ingress_rejects_excess_connections_and_releases_capacity():
    from api.omarai import BoundedThreadingHTTPServer

    server = BoundedThreadingHTTPServer(
        ("127.0.0.1", 0),
        Handler,
        max_concurrent_connections=1,
    )
    first_client, first_request = socket.socketpair()
    second_client, second_request = socket.socketpair()
    worker_started = threading.Event()
    release_worker = threading.Event()
    worker_finished = threading.Event()

    def hold_handler(_request, _client_address):
        worker_started.set()
        release_worker.wait(timeout=2)

    server.finish_request = hold_handler
    original_worker = server.process_request_thread

    def track_worker(request, client_address):
        try:
            original_worker(request, client_address)
        finally:
            worker_finished.set()

    server.process_request_thread = track_worker
    try:
        server.process_request(first_request, ("127.0.0.1", 10001))
        assert worker_started.wait(timeout=1)

        # The saturated listener rejects before creating a second handler thread.
        server.process_request(second_request, ("127.0.0.1", 10002))
        response = second_client.recv(512)
        assert response.startswith(b"HTTP/1.1 503 Service Unavailable\r\n")
        assert b"Retry-After: 5\r\n" in response
        assert not server._connection_slots.acquire(blocking=False)

        release_worker.set()
        assert worker_finished.wait(timeout=1)
        assert server._connection_slots.acquire(blocking=False)
        server._connection_slots.release()
    finally:
        release_worker.set()
        first_client.close()
        second_client.close()
        server.server_close()


def test_rate_limit_bounds_unique_client_buckets_and_shares_overflow_quota(monkeypatch):
    monkeypatch.delenv("OMARAI_TRUST_PROXY_HEADERS", raising=False)

    class RateLimitHarness:
        _rate_lock = threading.Lock()
        _request_times = None
        _rate_last_cleanup = 0.0
        RATE_LIMIT_REQUESTS = 1
        RATE_LIMIT_WINDOW_SECONDS = 60
        RATE_LIMIT_CLEANUP_INTERVAL_SECONDS = 60
        MAX_RATE_LIMIT_CLIENT_BUCKETS = 3
        RATE_LIMIT_OVERFLOW_KEY = Handler.RATE_LIMIT_OVERFLOW_KEY
        _rate_limit_client_key = Handler._rate_limit_client_key
        _rate_limit_ok = Handler._rate_limit_ok

        def __init__(self, address):
            self.client_address = (address, 12345)
            self.headers = {}

    RateLimitHarness._request_times = defaultdict(deque)

    assert RateLimitHarness("198.51.100.1")._rate_limit_ok() is True
    assert RateLimitHarness("198.51.100.2")._rate_limit_ok() is True
    assert RateLimitHarness("198.51.100.3")._rate_limit_ok() is True
    # New identities share the reserved overflow bucket and its rate ceiling.
    assert RateLimitHarness("198.51.100.4")._rate_limit_ok() is False
    assert len(RateLimitHarness._request_times) == 3
    assert RateLimitHarness.RATE_LIMIT_OVERFLOW_KEY in RateLimitHarness._request_times


def test_public_api_authentication_and_rate_limit_precede_json_parsing(local_api, monkeypatch):
    """Reject untrusted API calls before parsing bodies and throttle repeated failures."""
    monkeypatch.setenv("OMARAI_PUBLIC_DEPLOYMENT", "1")
    monkeypatch.setenv("OMARAI_ACCESS_TOKEN", "z" * 48)
    monkeypatch.setattr(Handler, "RATE_LIMIT_REQUESTS", 1)
    with Handler._rate_lock:
        Handler._request_times.clear()
    request = Request(
        local_api + "/api/agent",
        data=b"invalid-json-body",
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    try:
        with urlopen(request, timeout=3) as response:
            first_status = response.status
    except HTTPError as error:
        first_status = error.code
    assert first_status == 401

    try:
        with urlopen(request, timeout=3) as response:
            second_status = response.status
    except HTTPError as error:
        second_status = error.code
    assert second_status == 429


def test_hosted_api_requires_private_token_for_search_and_lead_data(local_api, monkeypatch):
    monkeypatch.setenv("OMARAI_PUBLIC_DEPLOYMENT", "1")
    monkeypatch.setenv("OMARAI_ACCESS_TOKEN", "x" * 48)

    status, error = request_json(
        local_api, "/api/analyze", method="POST", payload={"text": "test"}
    )
    assert status == 401
    assert "رمز الوصول" in error["error"]

    status, error = request_json(local_api, "/api/leads")
    assert status == 401

    headers = {"Authorization": "Bearer " + "x" * 48}
    status, result = request_json(
        local_api, "/api/analyze", method="POST", payload={"text": "بدور على شقة"}, headers=headers
    )
    assert status == 200
    assert "score" in result

    status, result = request_json(local_api, "/api/leads", headers=headers)
    assert status == 200
    assert result["count"] == 0


def test_hosted_api_rate_limits_authenticated_requests(local_api, monkeypatch):
    monkeypatch.setenv("OMARAI_PUBLIC_DEPLOYMENT", "1")
    monkeypatch.setenv("OMARAI_ACCESS_TOKEN", "y" * 48)
    monkeypatch.setattr(Handler, "RATE_LIMIT_REQUESTS", 1)
    with Handler._rate_lock:
        Handler._request_times.clear()
    headers = {"Authorization": "Bearer " + "y" * 48}

    status, _ = request_json(
        local_api, "/api/analyze", method="POST", payload={"text": "first"}, headers=headers
    )
    assert status == 200

    status, error = request_json(
        local_api, "/api/analyze", method="POST", payload={"text": "second"}, headers=headers
    )
    assert status == 429
    assert "حد الطلبات" in error["error"]



def test_public_binding_requires_explicit_deployment_flag_and_strong_token(monkeypatch):
    from api.omarai import serve

    monkeypatch.delenv("OMARAI_PUBLIC_DEPLOYMENT", raising=False)
    monkeypatch.delenv("OMARAI_ACCESS_TOKEN", raising=False)
    with pytest.raises(ValueError, match="Public binding requires"):
        serve("0.0.0.0", 0)

    monkeypatch.setenv("OMARAI_PUBLIC_DEPLOYMENT", "1")
    monkeypatch.setenv("OMARAI_ACCESS_TOKEN", "short")
    with pytest.raises(ValueError, match="at least 32 characters"):
        serve("0.0.0.0", 0)

def test_rate_limiter_prunes_expired_client_buckets(monkeypatch):
    """Client IPs do not accumulate forever after their 60-second window expires."""
    monkeypatch.delenv("OMARAI_TRUST_PROXY_HEADERS", raising=False)
    monkeypatch.setattr(Handler, "_request_times", defaultdict(deque))
    monkeypatch.setattr(Handler, "_rate_last_cleanup", 0.0)
    clock = {"now": 100.0}
    monkeypatch.setattr("api.omarai.time.monotonic", lambda: clock["now"])

    class FakeHandler(Handler):
        def __init__(self, ip):
            self.headers = {}
            self.client_address = (ip, 1234)

    first = FakeHandler("192.0.2.1")
    second = FakeHandler("192.0.2.2")
    assert first._rate_limit_ok() is True
    assert "192.0.2.1" in Handler._request_times

    clock["now"] = 161.0
    assert second._rate_limit_ok() is True
    assert "192.0.2.1" not in Handler._request_times
    assert "192.0.2.2" in Handler._request_times



def test_agent_concurrency_cap_rejects_work_when_all_slots_are_busy(local_api, monkeypatch):
    from api.omarai import WebAgent

    monkeypatch.delenv("OMARAI_PUBLIC_DEPLOYMENT", raising=False)
    monkeypatch.delenv("OMARAI_ACCESS_TOKEN", raising=False)
    monkeypatch.setattr(Handler, "_request_times", defaultdict(deque))
    monkeypatch.setattr(Handler, "_rate_last_cleanup", 0.0)
    monkeypatch.setattr(Handler, "_agent_semaphore", threading.BoundedSemaphore(1))

    entered = threading.Event()
    release = threading.Event()
    first_result = {}

    def slow_answer(self, question, history=None, mode="auto"):
        entered.set()
        assert release.wait(timeout=2), "test did not release the held research slot"
        return {
            "answer": "نتيجة اختبار محدودة",
            "question": question,
            "search_query": question,
            "search_queries": [],
            "search_report": {"search_attempted": False, "search_outcome": "not_attempted"},
            "sources": [],
            "used_language_model": False,
            "used_web_search": False,
            "search_attempted": False,
            "used_social_search": False,
            "warnings": [],
            "kind": "web_fallback",
        }

    monkeypatch.setattr(WebAgent, "answer", slow_answer)

    def first_request():
        first_result["response"] = request_json(
            local_api, "/api/agent", method="POST", payload={"question": "السؤال الأول"}
        )

    worker = threading.Thread(target=first_request, daemon=True)
    worker.start()
    try:
        assert entered.wait(timeout=1), "first request did not acquire the research slot"
        status, payload = request_json(
            local_api, "/api/agent", method="POST", payload={"question": "السؤال الثاني"}
        )
        assert status == 503
        assert payload["retry_after_seconds"] == 5
        assert "مشغولة" in payload["error"]
    finally:
        release.set()
        worker.join(timeout=3)

    assert not worker.is_alive()
    assert first_result["response"][0] == 200


def test_agent_concurrency_limit_has_hard_bounds(monkeypatch):
    from api.omarai import _configured_agent_concurrency_limit

    monkeypatch.setenv("OMARAI_MAX_CONCURRENT_AGENT_REQUESTS", "99")
    assert _configured_agent_concurrency_limit() == 8
    monkeypatch.setenv("OMARAI_MAX_CONCURRENT_AGENT_REQUESTS", "invalid")
    assert _configured_agent_concurrency_limit() == 4


def test_api_rejects_oversized_request_body(local_api):
    status, payload = request_json(
        local_api,
        "/api/analyze",
        method="POST",
        payload={"text": "x" * 200_001},
    )

    assert status == 413
    assert payload["error"] == "request too large"


def test_api_rejects_malformed_content_length(local_api, monkeypatch):
    monkeypatch.delenv("OMARAI_PUBLIC_DEPLOYMENT", raising=False)
    monkeypatch.delenv("OMARAI_ACCESS_TOKEN", raising=False)
    host_port = local_api.rsplit(":", 1)
    with socket.create_connection((host_port[0].removeprefix("http://"), int(host_port[1])), timeout=2) as client:
        client.sendall(
            b"POST /api/analyze HTTP/1.1\r\n"
            b"Host: localhost\r\n"
            b"Content-Type: application/json\r\n"
            b"Content-Length: invalid\r\n"
            b"Connection: close\r\n\r\n"
        )
        response = b""
        while True:
            chunk = client.recv(4096)
            if not chunk:
                break
            response += chunk

    assert response.startswith(b"HTTP/1.0 400")
    assert b"valid Content-Length is required" in response


def test_api_returns_408_when_request_body_read_times_out(local_api, monkeypatch):
    monkeypatch.delenv("OMARAI_PUBLIC_DEPLOYMENT", raising=False)
    monkeypatch.delenv("OMARAI_ACCESS_TOKEN", raising=False)
    monkeypatch.setattr("api.omarai.REQUEST_BODY_READ_TIMEOUT_SECONDS", 0.1)
    host_port = local_api.rsplit(":", 1)
    with socket.create_connection((host_port[0].removeprefix("http://"), int(host_port[1])), timeout=2) as client:
        client.settimeout(2)
        client.sendall(
            b"POST /api/analyze HTTP/1.1\r\n"
            b"Host: localhost\r\n"
            b"Content-Type: application/json\r\n"
            b"Content-Length: 40\r\n"
            b"Connection: close\r\n\r\n"
            b"{}"
        )
        response = b""
        while True:
            chunk = client.recv(4096)
            if not chunk:
                break
            response += chunk

    assert response.startswith(b"HTTP/1.0 408")
    assert b"request body read timed out" in response


def test_api_absolute_body_deadline_stops_slow_trickle(local_api, monkeypatch):
    """A client must not evade the total deadline by sending before each idle timeout."""
    import time

    monkeypatch.delenv("OMARAI_PUBLIC_DEPLOYMENT", raising=False)
    monkeypatch.delenv("OMARAI_ACCESS_TOKEN", raising=False)
    monkeypatch.setattr("api.omarai.REQUEST_BODY_READ_TIMEOUT_SECONDS", 0.45)
    monkeypatch.setattr("api.omarai.REQUEST_BODY_IDLE_TIMEOUT_SECONDS", 0.20)
    host, port = local_api.removeprefix("http://").rsplit(":", 1)

    with socket.create_connection((host, int(port)), timeout=2) as client:
        client.settimeout(2)
        started = time.monotonic()
        client.sendall(
            b"POST /api/analyze HTTP/1.1\r\n"
            b"Host: localhost\r\n"
            b"Content-Type: application/json\r\n"
            b"Content-Length: 100\r\n"
            b"Connection: close\r\n\r\n"
            b"{"
        )
        # Each fragment arrives before the 0.20s idle timeout, but the complete
        # request body never arrives before the 0.45s absolute deadline.
        for fragment in (b'"', b"text", b'"', b":"):
            time.sleep(0.08)
            try:
                client.sendall(fragment)
            except OSError:
                break

        response = bytearray()
        while True:
            try:
                chunk = client.recv(4096)
            except TimeoutError:
                break
            if not chunk:
                break
            response.extend(chunk)

    elapsed = time.monotonic() - started
    assert response.startswith(b"HTTP/1.0 408")
    assert b"request body read timed out" in response
    assert elapsed < 1.5



def test_api_absolute_header_deadline_stops_slow_trickle(local_api, monkeypatch):
    """Header bytes arriving before idle timeout must not extend the total deadline."""
    import time

    monkeypatch.delenv("OMARAI_PUBLIC_DEPLOYMENT", raising=False)
    monkeypatch.delenv("OMARAI_ACCESS_TOKEN", raising=False)
    monkeypatch.setattr("api.omarai.REQUEST_HEADER_READ_TIMEOUT_SECONDS", 0.5)
    monkeypatch.setattr("api.omarai.REQUEST_HEADER_IDLE_TIMEOUT_SECONDS", 0.35)
    host, port = local_api.removeprefix("http://").rsplit(":", 1)

    with socket.create_connection((host, int(port)), timeout=2) as client:
        client.settimeout(1.2)
        started = time.monotonic()
        client.sendall(
            b"POST /api/analyze HTTP/1.1\r\n"
            b"Host: localhost\r\n"
            b"Content-Type: application/json\r\n"
            b"Content-Length: 40\r\n"
            b"X-Slow: "
        )
        # Each tiny fragment is sent well before the 0.35s idle timeout. No
        # newline completes X-Slow, so only an absolute header deadline can stop it.
        for fragment in (b"a", b"b", b"c", b"d", b"e", b"f", b"g", b"h", b"i"):
            time.sleep(0.12)
            try:
                client.sendall(fragment)
            except OSError:
                break

        response = bytearray()
        while True:
            try:
                chunk = client.recv(4096)
            except TimeoutError:
                break
            except OSError:
                break
            if not chunk:
                break
            response.extend(chunk)
        elapsed = time.monotonic() - started

    assert elapsed < 0.8
    # The timed-out request never reached application dispatch; the handler closes silently.
    assert response == b""

def test_public_preflight_does_not_trust_spoofed_forwarded_host(local_api, monkeypatch):
    """A client-controlled X-Forwarded-Host must not grant an origin CORS access."""
    monkeypatch.setenv("OMARAI_PUBLIC_DEPLOYMENT", "1")
    monkeypatch.delenv("OMARAI_ALLOWED_ORIGINS", raising=False)

    request = Request(
        local_api + "/api/agent",
        method="OPTIONS",
        headers={
            "Origin": "https://attacker.example",
            "X-Forwarded-Host": "attacker.example",
            "X-Forwarded-Proto": "https",
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "authorization,content-type",
        },
    )
    with pytest.raises(HTTPError) as error:
        urlopen(request, timeout=3)
    assert error.value.code == 403


def test_public_origin_still_allows_the_requested_host(local_api, monkeypatch):
    """Same-service public UI remains compatible when the request Host is trusted."""
    from types import SimpleNamespace

    from api.omarai import Handler

    monkeypatch.setenv("OMARAI_PUBLIC_DEPLOYMENT", "1")
    monkeypatch.delenv("OMARAI_ALLOWED_ORIGINS", raising=False)
    handler = SimpleNamespace(
        headers={
            "Host": "omarai.example",
            "X-Forwarded-Proto": "https",
            "X-Forwarded-Host": "attacker.example",
        }
    )
    allowed = Handler._allowed_origins(handler)
    assert "https://omarai.example" in allowed
    assert "https://attacker.example" not in allowed



def test_security_headers_apply_to_json_and_html_responses(local_api, monkeypatch):
    monkeypatch.delenv("OMARAI_PUBLIC_DEPLOYMENT", raising=False)
    monkeypatch.delenv("OMARAI_ACCESS_TOKEN", raising=False)
    for path in ("/api/health", "/"):
        request = Request(local_api + path)
        with urlopen(request, timeout=3) as response:
            headers = {name.lower(): value for name, value in response.headers.items()}
            assert headers["x-content-type-options"] == "nosniff"
            assert headers["x-frame-options"] == "DENY"
            assert headers["referrer-policy"] == "strict-origin-when-cross-origin"
            assert "default-src 'self'" in headers["content-security-policy"]
            policy = headers["content-security-policy"]
            assert "frame-ancestors 'none'" in policy
            assert "'unsafe-inline'" not in policy
            assert "'sha256-" in policy
            assert headers["permissions-policy"] == (
                "camera=(), microphone=(), geolocation=()"
            )


def test_health_exposes_only_validated_image_baked_sha(monkeypatch, tmp_path):
    import api.omarai as api_module

    build_sha_file = tmp_path / "BUILD_SHA"
    monkeypatch.setattr(api_module, "BUILD_SHA_FILE", build_sha_file)
    assert api_module._build_sha() == "unknown"
    build_sha_file.write_text("a" * 40, encoding="ascii")
    assert api_module._build_sha() == "a" * 40
    build_sha_file.write_text("not-a-git-sha", encoding="ascii")
    assert api_module._build_sha() == "unknown"



@pytest.mark.parametrize(
    ("variable", "source"),
    [
        ("RAILWAY_GIT_COMMIT_SHA", "platform:railway"),
        ("RENDER_GIT_COMMIT", "platform:render"),
    ],
)
def test_build_identity_uses_validated_platform_commit_when_image_sha_is_unavailable(
    monkeypatch, tmp_path, variable, source
):
    import api.omarai as api_module

    build_sha_file = tmp_path / "BUILD_SHA"
    monkeypatch.setattr(api_module, "BUILD_SHA_FILE", build_sha_file)
    build_sha_file.write_text("unknown", encoding="ascii")
    for name, _label in api_module._PLATFORM_BUILD_SHA_ENVIRONMENTS:
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setenv(variable, "b" * 40)

    assert api_module._build_identity() == ("b" * 40, source)


def test_invalid_platform_commit_does_not_create_build_identity(monkeypatch, tmp_path):
    import api.omarai as api_module

    monkeypatch.setattr(api_module, "BUILD_SHA_FILE", tmp_path / "BUILD_SHA")
    api_module.BUILD_SHA_FILE.write_text("unknown", encoding="ascii")
    monkeypatch.setenv("RAILWAY_GIT_COMMIT_SHA", "not-a-sha")
    monkeypatch.setenv("RENDER_GIT_COMMIT", "also-not-a-sha")

    assert api_module._build_identity() == ("unknown", "unknown")



def test_lead_store_uses_configured_database_path(monkeypatch, tmp_path):
    from api.omarai import _lead_store_from_environment

    database_path = tmp_path / "persistent" / "omarai.sqlite3"
    monkeypatch.setenv("OMARAI_DB_PATH", str(database_path))

    store = _lead_store_from_environment()

    assert store.path == database_path
    assert database_path.is_file()



def test_agent_concurrency_slot_released_after_operation_error(local_api, monkeypatch):
    from api.omarai import WebAgent

    monkeypatch.delenv("OMARAI_PUBLIC_DEPLOYMENT", raising=False)
    monkeypatch.delenv("OMARAI_ACCESS_TOKEN", raising=False)
    monkeypatch.setattr(Handler, "_request_times", defaultdict(deque))
    monkeypatch.setattr(Handler, "_rate_last_cleanup", 0.0)
    monkeypatch.setattr(Handler, "_agent_semaphore", threading.BoundedSemaphore(1))
    state = {"fail": True}

    def answer_with_one_transient_failure(self, question, history=None, mode="auto"):
        if state["fail"]:
            raise RuntimeError("synthetic operation failure")
        return {
            "answer": "اختبار ناجح",
            "question": question,
            "search_query": question,
            "search_queries": [],
            "search_report": {
                "search_attempted": False,
                "search_outcome": "not_attempted",
            },
            "sources": [],
            "used_language_model": False,
            "used_web_search": False,
            "search_attempted": False,
            "used_social_search": False,
            "warnings": [],
            "kind": "web_fallback",
        }

    monkeypatch.setattr(WebAgent, "answer", answer_with_one_transient_failure)

    status, payload = request_json(
        local_api, "/api/agent", method="POST", payload={"question": "الطلب الأول"}
    )
    assert status == 500
    assert payload["error"] == "internal server error"

    state["fail"] = False
    status, payload = request_json(
        local_api, "/api/agent", method="POST", payload={"question": "الطلب الثاني"}
    )
    assert status == 200
    assert payload["answer"] == "اختبار ناجح"


def test_csp_hashes_match_all_first_party_inline_content_and_attributes():
    import api.omarai as api_module

    policy = api_module._content_security_policy()
    assert "'unsafe-inline'" not in policy
    script_blocks = 0
    style_blocks = 0
    style_attributes = 0
    for html_path in api_module.ROOT.glob("*.html"):
        document = html_path.read_text(encoding="utf-8")
        for match in re.finditer(
            r"<script\b(?P<attrs>[^>]*)>(?P<body>.*?)</script\s*>",
            document,
            re.IGNORECASE | re.DOTALL,
        ):
            if re.search(r"\bsrc\s*=", match.group("attrs"), re.IGNORECASE):
                continue
            script_blocks += 1
            assert api_module._csp_hash_source(match.group("body")) in policy
        for match in re.finditer(
            r"<style\b[^>]*>(?P<body>.*?)</style\s*>",
            document,
            re.IGNORECASE | re.DOTALL,
        ):
            style_blocks += 1
            assert api_module._csp_hash_source(match.group("body")) in policy
        for match in re.finditer(
            r"""\bstyle\s*=\s*(["'])(.*?)\1""",
            document,
            re.IGNORECASE | re.DOTALL,
        ):
            style_attributes += 1
            assert api_module._csp_hash_source(match.group(2).strip()) in policy
    assert script_blocks >= 2
    assert style_blocks >= 2
    assert style_attributes >= 10


def test_dashboard_uses_delegated_status_action_not_inline_onclick():
    dashboard = (Path(__file__).resolve().parents[1] / "web" / "dashboard.html").read_text(
        encoding="utf-8"
    )
    assert 'data-action="save-status"' in dashboard
    assert 'onclick="saveStatus' not in dashboard
    assert """data-lead-id="'+esc(l.id)+'">""" in dashboard
