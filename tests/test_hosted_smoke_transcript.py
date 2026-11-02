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
                "answer_evidence_status": "sources_present",
                "sources": [
                    {
                        "title": "Fire alarm tender notice",
                        "url": "https://example.test/fire-alarm-tender",
                        "provider": "bing_rss",
                        "snippet": "طلب عرض سعر لنظام إنذار الحريق.",
                        "published_at": "",
                    }
                ],
                "search_report": {
                    "pages_fetched": 1,
                    "providers_used": ["bing_rss"],
                    "pipeline_completion_status": "completed",
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
    assert report["provider_diagnostics"][0]["provider"] == "bing_rss"
    assert report["connector_configuration"]["brave_search_api_configured"] is False
    assert report["connector_check"]["provider_counts"] == {"bing_rss": 2}
    diagnostics_call = next(call for call in calls if call[0].endswith("/api/diagnostics"))
    assert diagnostics_call[2]["test_model"] is False
    assert all("T" * 40 not in str(item) for item in report.values())
    assert len(calls) == 4


def test_hosted_smoke_allows_no_token_only_for_loopback_dev(monkeypatch):
    def fake_request_json(url, *, token="", payload=None, timeout=90):
        if url.endswith("/api/health"):
            return 200, {"ok": True, "build": {"sha": "unknown"}}
        if url.endswith("/api/diagnostics"):
            return 200, {
                "checks": {
                    "web_search": {"status": "passed", "result_count": 1},
                    "language_model": {"status": "passed"},
                },
                "provider_diagnostics": [],
                "warnings": [],
            }
        if url.endswith("/api/agent"):
            return 200, {
                "answer": "لا توجد إشارة شراء مؤكدة في المصادر التي تم فحصها.",
                "used_web_search": True,
                "used_language_model": True,
                "sources": [{"url": "https://example.test/egypt"}],
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
