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
        if self.path == "/":
            self.respond(200, {"page": "dashboard"})
        elif self.path == "/api/health":
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
                "answer_evidence_status": "citation_indices_validated_only",
                "request_budget": {"profile": "hosted_smoke", "timeout_seconds": 75, "budget_exhausted": False, "deadline_exceeded": False, "limits": {"search_queries": 3, "search_calls": 12, "model_calls": 6, "page_fetches": 4, "tool_calls": 0}, "counts": {"search_queries": 2, "search_calls": 4, "model_calls": 4, "page_fetches": 1, "tool_calls": 0}},
                "search_report": {
                    "providers_used": ["bing_rss"], "pages_fetched": 1,
                    "pipeline_completion_status": "completed",
                    "semantic_claim_verification": {"status": "completed_all_claims_supported"},
                    "insufficient_evidence": False,
                    "claim_audit_semantics": "distinct_model_assessed_source_support_not_ground_truth",
                },
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


def test_smoke_checks_health_auth_and_single_agent_search(hosted_server):
    result = run_smoke(
        hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5
    )
    assert result["result"] == "passed"
    assert result["checks"]["health"] == "passed"
    assert result["checks"]["authentication"] == "passed"
    assert result["checks"]["search"]["providers_reported"] == ["bing_rss"]
    assert result["checks"]["agent_request"]["source_count"] == 1
    assert result["checks"]["agent_request"]["pipeline_completion_status"] == "completed"


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



def test_http_403_report_contains_only_safe_response_metadata():
    class ForbiddenHandler(BaseHTTPRequestHandler):
        def log_message(self, format: str, *args: object) -> None:
            return

        def do_GET(self) -> None:
            body = b"<html>blocked</html>"
            self.send_response(403)
            self.send_header("Content-Type", "text/html")
            self.send_header("X-Request-ID", "request-123")
            self.send_header("CF-Ray", "ray-456")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    server = ThreadingHTTPServer(("127.0.0.1", 0), ForbiddenHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        status, payload = hosted_smoke_test.request_json(
            f"http://127.0.0.1:{server.server_port}/api/health",
            token=TOKEN,
            timeout=3,
        )
        assert status == 403
        assert payload["_smoke_http"]["status"] == 403
        assert payload["_smoke_http"]["request_id"] == "request-123"
        assert payload["_smoke_http"]["cf_ray"] == "ray-456"
        assert payload["_smoke_http"]["body_bytes_sampled"] == len(b"<html>blocked</html>")
        assert "body_sha256" in payload["_smoke_http"]
        assert "blocked" not in str(payload)
        assert TOKEN not in str(payload)
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)



def test_health_403_metadata_is_preserved_in_failure_report(monkeypatch):
    metadata = {
        "status": 403,
        "content_type": "text/html",
        "server": "edge-gateway",
        "request_id": "request-403",
        "correlation_id": "",
        "cf_ray": "ray-403",
        "via": "",
        "body_bytes_sampled": 19,
        "body_sha256": "a" * 64,
    }

    def forbidden_health(url: str, **kwargs):
        return 403, {"_smoke_http": metadata}

    monkeypatch.setattr(hosted_smoke_test, "request_json", forbidden_health)
    with pytest.raises(SmokeError, match="Health check failed") as failure:
        run_smoke("https://omarai.example.test", TOKEN, allow_provider_usage=False)
    assert failure.value.report["http_response"] == metadata
    assert "blocked" not in str(failure.value.report)



def test_hosted_preflight_allows_remote_no_token_and_still_checks_auth_rejection(monkeypatch):
    calls = []

    def fake_request(url: str, *, token="", payload=None, timeout=90):
        path = urlsplit(url).path
        calls.append((path, token, payload))
        if path == "/":
            return 200, None
        if path == "/api/health":
            return 200, {"ok": True, "build": {"sha": "a" * 40}}
        if path == "/api/agent" and not token:
            assert payload == {"question": ""}
            return 401, None
        raise AssertionError("preflight must not call authenticated agent/search/model paths")

    monkeypatch.setattr(hosted_smoke_test, "request_json", fake_request)
    result = run_smoke(
        "https://omarai.example.test",
        "",
        preflight_only=True,
        allow_provider_usage=False,
    )
    assert result["result"] == "preflight_passed"
    assert result["auth_mode"] == "preflight_no_token"
    assert result["checks"]["authentication"] == "passed"
    assert result["checks"]["homepage"] == "passed"
    assert result["endpoint_diagnostics"]["homepage"]["http_status"] == 200
    assert result["endpoint_diagnostics"]["health"]["http_status"] == 200
    assert result["endpoint_diagnostics"]["unauthenticated_agent"]["http_status"] == 401
    assert calls == [("/", "", None), ("/api/health", "", None), ("/api/agent", "", {"question": ""})]




def test_preflight_fails_closed_if_unauthenticated_agent_probe_reaches_validation(monkeypatch):
    calls = []

    def auth_bypass(url: str, *, token="", payload=None, timeout=90):
        path = urlsplit(url).path
        calls.append((path, token, payload))
        if path == "/":
            return 200, None
        if path == "/api/health":
            return 200, {"ok": True}
        if path == "/api/agent" and not token:
            assert payload == {"question": ""}
            # The API reached question validation, so its auth gate did not reject first.
            return 400, {"error": "question must be a non-empty string"}
        raise AssertionError("no authenticated agent request is allowed in preflight")

    monkeypatch.setattr(hosted_smoke_test, "request_json", auth_bypass)
    with pytest.raises(SmokeError, match="per-endpoint HTTP diagnostics") as failure:
        run_smoke("https://omarai.example.test", "", preflight_only=True)
    assert calls == [("/", "", None), ("/api/health", "", None), ("/api/agent", "", {"question": ""})]
    assert failure.value.report["endpoint_diagnostics"]["unauthenticated_agent"]["http_status"] == 400




def test_no_cost_preflight_rejects_a_mismatched_expected_build_sha(monkeypatch):
    def request_with_wrong_sha(url: str, *, token="", payload=None, timeout=90):
        path = urlsplit(url).path
        if path == "/":
            return 200, None
        if path == "/api/health":
            return 200, {"ok": True, "build": {"sha": "b" * 40}}
        if path == "/api/agent":
            assert payload == {"question": ""}
            return 401, None
        raise AssertionError(path)

    monkeypatch.setattr(hosted_smoke_test, "request_json", request_with_wrong_sha)
    with pytest.raises(SmokeError, match="per-endpoint HTTP diagnostics") as failure:
        run_smoke(
            "https://omarai.example.test", "",
            expected_sha="a" * 40, preflight_only=True,
        )
    assert failure.value.report["checks"]["build_identity"]["status"] == "failed"


def test_no_cost_preflight_collects_all_endpoint_failures_without_request_bodies(monkeypatch):
    calls = []
    body_digest = "b" * 64
    metadata = {
        "status": 403,
        "content_type": "application/json",
        "server": "cloudflare",
        "request_id": "",
        "correlation_id": "",
        "cf_ray": "ray-example-403",
        "via": "",
        "body_bytes_sampled": 128,
        "body_sha256": body_digest,
    }

    def blocked_request(url: str, *, token="", payload=None, timeout=90):
        path = urlsplit(url).path
        calls.append((path, token, payload))
        if path in {"/", "/api/health"}:
            return 403, {"_smoke_http": metadata}
        if path == "/api/agent":
            assert payload == {"question": ""}
            return 403, {"_smoke_http": {**metadata, "cf_ray": "ray-example-agent"}}
        raise AssertionError(f"unexpected preflight request: {path}")

    monkeypatch.setattr(hosted_smoke_test, "request_json", blocked_request)
    with pytest.raises(SmokeError, match="per-endpoint HTTP diagnostics") as failure:
        run_smoke("https://omarai.example.test", "", preflight_only=True)

    report = failure.value.report
    assert calls == [
        ("/", "", None),
        ("/api/health", "", None),
        ("/api/agent", "", {"question": ""}),
    ]
    assert set(report["http_responses"]) == {
        "homepage", "health", "unauthenticated_agent"
    }
    assert report["endpoint_diagnostics"]["homepage"]["http_status"] == 403
    assert report["endpoint_diagnostics"]["health"]["http_status"] == 403
    assert report["endpoint_diagnostics"]["unauthenticated_agent"]["http_status"] == 403
    assert report["http_responses"]["health"]["cf_ray"] == "ray-example-403"
    assert "body_sha256" in report["http_responses"]["health"]
    assert "blocked" not in str(report)
    assert "b" * 128 not in str(report)
    assert TOKEN not in str(report)


def test_no_cost_preflight_keeps_probing_when_only_health_route_is_blocked(monkeypatch):
    calls = []

    def request_with_health_block(url: str, *, token="", payload=None, timeout=90):
        path = urlsplit(url).path
        calls.append(path)
        if path == "/":
            return 200, None
        if path == "/api/health":
            return 403, {"_smoke_http": {"status": 403, "cf_ray": "health-ray"}}
        if path == "/api/agent":
            return 401, None
        raise AssertionError(path)

    monkeypatch.setattr(hosted_smoke_test, "request_json", request_with_health_block)
    with pytest.raises(SmokeError) as failure:
        run_smoke("https://omarai.example.test", "", preflight_only=True)

    assert calls == ["/", "/api/health", "/api/agent"]
    diagnostics = failure.value.report["endpoint_diagnostics"]
    assert diagnostics["homepage"]["status"] == "passed"
    assert diagnostics["health"]["status"] == "failed"
    assert diagnostics["unauthenticated_agent"]["status"] == "passed"




def test_smoke_preflight_runs_without_provider_usage_or_model_calls(hosted_server):
    result = run_smoke(
        hosted_server, TOKEN, allow_http=True, preflight_only=True, allow_provider_usage=False, timeout=5
    )
    assert result["result"] == "preflight_passed"
    assert result["checks"]["health"] == "passed"
    assert result["checks"]["authentication"] == "passed"
    assert result["checks"]["provider_usage"]["status"] == "skipped_not_approved"
    assert result["transcript"] == []


def test_smoke_requires_provider_approval_after_no_cost_preflight(monkeypatch):
    calls = []

    def fake_request(url, *, token="", payload=None, timeout=90):
        calls.append((urlsplit(url).path, token, payload))
        if url.endswith("/api/health"):
            return 200, {"ok": True}
        if url.endswith("/api/agent") and not token:
            assert payload == {"question": ""}
            return 401, None
        raise AssertionError("provider-dependent request must not run without approval")

    monkeypatch.setattr(hosted_smoke_test, "request_json", fake_request)
    with pytest.raises(SmokeError, match="explicit human approval") as failure:
        run_smoke("https://omarai.example.test", TOKEN, allow_provider_usage=False)
    assert calls == [("/api/health", "", None), ("/api/agent", "", {"question": ""})]
    assert failure.value.report["checks"]["authentication"] == "passed"
    assert failure.value.report["checks"]["provider_usage"]["status"] == "blocked_not_approved"


def test_smoke_rejects_empty_agent_answer(hosted_server, monkeypatch):
    original = hosted_smoke_test.request_json

    def empty_answer(url: str, **kwargs):
        if urlsplit(url).path == "/api/agent" and kwargs.get("token") == TOKEN:
            return 200, {
                "answer": "  ", "used_web_search": True, "used_language_model": True,
                "answer_evidence_status": "citation_indices_validated_only",
                "sources": [{"url": "https://example.com/source"}],
                "search_report": {
                    "pipeline_completion_status": "completed",
                    "semantic_claim_verification": {"status": "completed_all_claims_supported"},
                    "insufficient_evidence": False,
                    "claim_audit_semantics": "distinct_model_assessed_source_support_not_ground_truth",
                },
            }
        return original(url, **kwargs)

    monkeypatch.setattr(hosted_smoke_test, "request_json", empty_answer)
    with pytest.raises(SmokeError, match="empty or whitespace-only answer"):
        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)



def test_smoke_rejects_non_string_agent_answer(hosted_server, monkeypatch):
    original = hosted_smoke_test.request_json

    def non_string_answer(url: str, **kwargs):
        if urlsplit(url).path == "/api/agent" and kwargs.get("token") == TOKEN:
            return 200, {
                "answer": None, "used_web_search": True, "used_language_model": True,
                "answer_evidence_status": "citation_indices_validated_only",
                "sources": [{"url": "https://example.com/source"}],
                "search_report": {
                    "pipeline_completion_status": "completed",
                    "semantic_claim_verification": {"status": "completed_all_claims_supported"},
                    "insufficient_evidence": False,
                    "claim_audit_semantics": "distinct_model_assessed_source_support_not_ground_truth",
                },
            }
        return original(url, **kwargs)

    monkeypatch.setattr(hosted_smoke_test, "request_json", non_string_answer)
    with pytest.raises(SmokeError, match="empty or whitespace-only answer"):
        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)


def test_smoke_rejects_partial_pipeline_even_with_sources(hosted_server, monkeypatch):
    original = hosted_smoke_test.request_json

    def partial_pipeline(url: str, **kwargs):
        if urlsplit(url).path == "/api/agent" and kwargs.get("token") == TOKEN:
            return 200, {
                "answer": "إجابة جزئية [المصدر 1]", "used_web_search": True,
                "used_language_model": True,
                "answer_evidence_status": "citation_indices_validated_only",
                "sources": [{"url": "https://example.com/source"}],
                "request_budget": {"profile": "hosted_smoke", "timeout_seconds": 75, "budget_exhausted": False, "deadline_exceeded": False, "limits": {"search_queries": 3, "search_calls": 12, "model_calls": 6, "page_fetches": 4, "tool_calls": 0}, "counts": {"search_queries": 2, "search_calls": 4, "model_calls": 4, "page_fetches": 1, "tool_calls": 0}},
                "search_report": {
                    "pipeline_completion_status": "partial",
                    "semantic_claim_verification": {"status": "completed_all_claims_supported"},
                    "insufficient_evidence": False,
                    "claim_audit_semantics": "distinct_model_assessed_source_support_not_ground_truth",
                },
            }
        return original(url, **kwargs)

    monkeypatch.setattr(hosted_smoke_test, "request_json", partial_pipeline)
    with pytest.raises(SmokeError, match="pipeline did not complete"):
        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)


def test_smoke_rejects_unvalidated_answer_evidence(hosted_server, monkeypatch):
    original = hosted_smoke_test.request_json

    def invalid_evidence(url: str, **kwargs):
        if urlsplit(url).path == "/api/agent" and kwargs.get("token") == TOKEN:
            return 200, {
                "answer": "إجابة بلا إحالات صالحة", "used_web_search": True,
                "used_language_model": True, "answer_evidence_status": "not_assessed",
                "sources": [{"url": "https://example.com/source"}],
                "request_budget": {"profile": "hosted_smoke", "timeout_seconds": 75, "budget_exhausted": False, "deadline_exceeded": False, "limits": {"search_queries": 3, "search_calls": 12, "model_calls": 6, "page_fetches": 4, "tool_calls": 0}, "counts": {"search_queries": 2, "search_calls": 4, "model_calls": 4, "page_fetches": 1, "tool_calls": 0}},
                "search_report": {
                    "pipeline_completion_status": "completed",
                    "semantic_claim_verification": {"status": "completed_all_claims_supported"},
                    "insufficient_evidence": False,
                    "claim_audit_semantics": "distinct_model_assessed_source_support_not_ground_truth",
                },
            }
        return original(url, **kwargs)

    monkeypatch.setattr(hosted_smoke_test, "request_json", invalid_evidence)
    with pytest.raises(SmokeError, match="evidence status"):
        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)




def test_smoke_rejects_missing_or_exceeded_server_budget_profile(hosted_server, monkeypatch):
    original = hosted_smoke_test.request_json

    def unbounded_budget(url: str, **kwargs):
        if urlsplit(url).path == "/api/agent" and kwargs.get("token") == TOKEN:
            status, payload = original(url, **kwargs)
            payload["request_budget"] = {
                "profile": "default",
                "budget_exhausted": False,
                "deadline_exceeded": False,
                "limits": {"search_queries": 8, "search_calls": 32, "model_calls": 8, "page_fetches": 8, "tool_calls": 3},
                "counts": {"search_queries": 1, "search_calls": 2, "model_calls": 2, "page_fetches": 1, "tool_calls": 0},
            }
            return status, payload
        return original(url, **kwargs)

    monkeypatch.setattr(hosted_smoke_test, "request_json", unbounded_budget)
    with pytest.raises(SmokeError, match="hosted_smoke request budget"):
        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)



def test_smoke_rejects_pipeline_complete_without_semantic_claim_support(hosted_server, monkeypatch):
    original = hosted_smoke_test.request_json

    def unverified_claims(url: str, **kwargs):
        if urlsplit(url).path == "/api/agent" and kwargs.get("token") == TOKEN:
            return 200, {
                "answer": "ادعاء غير متحقق [المصدر 1]", "used_web_search": True,
                "used_language_model": True,
                "answer_evidence_status": "citation_indices_validated_only",
                "sources": [{"url": "https://example.com/source"}],
                "request_budget": {"profile": "hosted_smoke", "timeout_seconds": 75, "budget_exhausted": False, "deadline_exceeded": False, "limits": {"search_queries": 3, "search_calls": 12, "model_calls": 6, "page_fetches": 4, "tool_calls": 0}, "counts": {"search_queries": 2, "search_calls": 4, "model_calls": 4, "page_fetches": 1, "tool_calls": 0}},
                "search_report": {
                    "pipeline_completion_status": "completed",
                    "semantic_claim_verification": {"status": "not_performed"},
                    "insufficient_evidence": False,
                    "claim_audit_semantics": "distinct_model_assessed_source_support_not_ground_truth",
                },
            }
        return original(url, **kwargs)

    monkeypatch.setattr(hosted_smoke_test, "request_json", unverified_claims)
    with pytest.raises(SmokeError, match="semantic claim-support review"):
        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)


def test_hosted_smoke_workflow_scopes_secrets_to_the_execution_step():
    workflow = Path(".github/workflows/hosted-smoke.yml").read_text(encoding="utf-8")
    job = workflow.split("jobs:", 1)[1].split("steps:", 1)[0]
    assert "OMARAI_ACCESS_TOKEN" not in job
    assert "OMARAI_BASE_URL" not in job
    assert "OMARAI_ACCESS_TOKEN:" in workflow
    assert "OMARAI_BASE_URL:" in workflow
    preflight_step = workflow.split("- name: Run no-cost hosted preflight", 1)[1].split(
        "- name: Run live hosted acceptance", 1
    )[0]
    live_step = workflow.split("- name: Run live hosted acceptance", 1)[1].split(
        "- name: Upload hosted question-and-answer transcript", 1
    )[0]
    assert "OMARAI_ACCESS_TOKEN" not in preflight_step
    assert "OMARAI_ACCESS_TOKEN:" in live_step
    assert "preflight-only" in workflow
    assert "default: false" in workflow


def test_hosted_smoke_workflow_is_manual_and_cost_gated():
    workflow = Path(".github/workflows/hosted-smoke.yml").read_text(encoding="utf-8")
    assert "schedule:" not in workflow
    assert "allow_provider_usage:" in workflow
    assert "default: false" in workflow
    assert "--allow-provider-usage" in workflow


def test_hosted_smoke_budget_caps_match_server_enforced_profile():
    from agents.request_budget import HOSTED_SMOKE_BUDGET_LIMITS

    assert hosted_smoke_test.HOSTED_SMOKE_BUDGET_MAX == HOSTED_SMOKE_BUDGET_LIMITS


def test_hosted_smoke_requires_successful_no_cost_preflight_before_live_usage():
    workflow = Path(".github/workflows/hosted-smoke.yml").read_text(encoding="utf-8")
    preflight_step = workflow.split("- name: Run no-cost hosted preflight", 1)[1].split(
        "- name: Run live hosted acceptance", 1
    )[0]
    live_step = workflow.split("- name: Run live hosted acceptance", 1)[1].split(
        "- name: Upload hosted question-and-answer transcript", 1
    )[0]

    assert "id: preflight" in preflight_step
    assert "if:" not in preflight_step
    assert '--expected-sha "$(git rev-parse HEAD)"' in preflight_step
    assert "steps.preflight.outcome == 'success'" in live_step
    assert "allow_provider_usage == true" in live_step
    assert "OMARAI_ACCESS_TOKEN" not in preflight_step
