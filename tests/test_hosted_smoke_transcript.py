"""Tests for the hosted acceptance transcript contract."""
from __future__ import annotations

from scripts import hosted_smoke_test


def test_hosted_smoke_returns_exact_question_answer_and_sources(monkeypatch):
    calls = []

    def fake_request_json(url, *, token="", payload=None, timeout=90):
        calls.append((url, token, payload))
        if url.endswith("/api/health"):
            return 200, {"ok": True, "build": {"sha": "a" * 40}}
        if url.endswith("/api/agent") and not token:
            return 401, None
        if url.endswith("/api/diagnostics"):
            return 200, {
                "checks": {
                    "web_search": {
                        "status": "passed",
                        "result_count": 2,
                        "provider_counts": {"bing_rss": 2},
                    },
                    "language_model": {"status": "passed"},
                },
                "provider_diagnostics": [
                    {"provider": "bing_rss", "status": "ok", "accepted_count": 2}
                ],
                "configuration": {
                    "brave_search_api_configured": False,
                    "tavily_search_api_configured": False,
                    "deepseek_search_api_configured": False,
                },
                "warnings": [],
            }
        if url.endswith("/api/agent") and token:
            return 200, {
                "answer": "وجدت إشارة منشورة تطلب عرض سعر لنظام إنذار الحريق.",
                "used_web_search": True,
                "used_language_model": True,
                "answer_evidence_status": "citation_indices_validated_only",
                "sources": [
                    {
                        "title": "Fire alarm tender notice",
                        "url": "https://example.test/fire-alarm-tender",
                        "provider": "bing_rss",
                        "snippet": "طلب عرض سعر لنظام إنذار الحريق.",
                        "published_at": "",
                    }
                ],
                "request_budget": {"profile": "hosted_smoke", "timeout_seconds": 75, "budget_exhausted": False, "deadline_exceeded": False, "limits": {"search_queries": 3, "search_calls": 12, "model_calls": 6, "page_fetches": 4, "tool_calls": 0}, "counts": {"search_queries": 2, "search_calls": 4, "model_calls": 4, "page_fetches": 1, "tool_calls": 0}},
                "search_report": {
                    "pages_fetched": 1,
                    "providers_used": ["bing_rss"],
                    "pipeline_completion_status": "completed",
                    "semantic_claim_verification": {"status": "completed_all_claims_supported"},
                    "insufficient_evidence": False,
                    "claim_audit_semantics": "distinct_model_assessed_source_support_not_ground_truth",
                },
            }
        raise AssertionError(f"unexpected request: {url}")

    monkeypatch.setattr(hosted_smoke_test, "request_json", fake_request_json)
    report = hosted_smoke_test.run_smoke(
        "https://omarai.example", "T" * 40, expected_sha="a" * 40,
        allow_provider_usage=True,
    )

    transcript = report["transcript"][0]
    assert transcript["question"] == hosted_smoke_test.LIVE_TEST_QUESTION
    assert transcript["answer"] == "وجدت إشارة منشورة تطلب عرض سعر لنظام إنذار الحريق."
    assert transcript["sources"][0]["url"] == "https://example.test/fire-alarm-tender"
    assert transcript["pipeline_completion_status"] == "completed"
    assert transcript["request_budget"]["profile"] == "hosted_smoke"
    assert report["checks"]["request_budget"]["limits"]["search_calls"] <= 12
    assert report["checks"]["search"]["providers_reported"] == ["bing_rss"]
    assert all("T" * 40 not in str(item) for item in report.values())
    assert len(calls) == 3
    assert not any(call[0].endswith("/api/diagnostics") for call in calls)


def test_hosted_smoke_allows_no_token_only_for_loopback_dev(monkeypatch):
    def fake_request_json(url, *, token="", payload=None, timeout=90):
        if url.endswith("/api/health"):
            return 200, {"ok": True, "build": {"sha": "unknown"}}
        if url.endswith("/api/agent"):
            return 200, {
                "answer": "لا توجد إشارة شراء مؤكدة في المصادر التي تم فحصها.",
                "used_web_search": True,
                "used_language_model": True,
                "answer_evidence_status": "citation_indices_validated_only",
                "sources": [{"url": "https://example.test/egypt"}],
                "request_budget": {"profile": "hosted_smoke", "timeout_seconds": 75, "budget_exhausted": False, "deadline_exceeded": False, "limits": {"search_queries": 3, "search_calls": 12, "model_calls": 6, "page_fetches": 4, "tool_calls": 0}, "counts": {"search_queries": 1, "search_calls": 2, "model_calls": 3, "page_fetches": 1, "tool_calls": 0}},
                "search_report": {
                    "pipeline_completion_status": "completed",
                    "semantic_claim_verification": {"status": "completed_no_factual_claims"},
                    "insufficient_evidence": False,
                    "claim_audit_semantics": "distinct_model_assessed_source_support_not_ground_truth",
                },
            }
        raise AssertionError(url)

    monkeypatch.setattr(hosted_smoke_test, "request_json", fake_request_json)
    report = hosted_smoke_test.run_smoke(
        "http://127.0.0.1:8000",
        "",
        local_dev_no_token=True,
        allow_provider_usage=True,
    )
    assert report["auth_mode"] == "local_loopback_dev_bypass"
    assert report["transcript"][0]["answer"] == "لا توجد إشارة شراء مؤكدة في المصادر التي تم فحصها."


def test_hosted_smoke_rejects_no_token_for_remote_host():
    import pytest

    with pytest.raises(hosted_smoke_test.SmokeError, match="localhost/loopback"):
        hosted_smoke_test.run_smoke(
            "https://omarai.example",
            "",
            local_dev_no_token=True,
        )
