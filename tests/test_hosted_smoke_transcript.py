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
        if url.endswith("/api/agent") and token:
            return 200, {
                "answer": "وجدت إشارة منشورة تطلب عرض سعر لنظام إنذار الحريق. [المصدر 1]",
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
                "search_report": {
                    "search_outcome": "attempted_with_usable_sources",
                    "pages_fetched": 1,
                    "providers_used": ["bing_rss"],
                    "pipeline_completion_status": "completed",
                },
                "request_budget": {
                    "limits": {
                        "search_queries": 2, "search_calls": 8, "model_calls": 3,
                        "page_fetches": 2, "tool_calls": 0,
                    },
                    "counts": {
                        "search_queries": 1, "search_calls": 2, "model_calls": 2,
                        "page_fetches": 1, "tool_calls": 0,
                    },
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
    agent_call = next(call for call in calls if call[0].endswith("/api/agent") and call[2])
    assert agent_call[2]["execution_profile"] == "hosted_smoke"
    assert agent_call[2]["allow_provider_usage"] is True
    assert report["request_budget"]["limits"]["search_queries"] == 2
    assert all("T" * 40 not in str(item) for item in report.values())
    assert len(calls) == 3




def test_hosted_smoke_rejects_partial_pipeline_even_with_sources_and_answer(monkeypatch):
    def fake_request_json(url, *, token="", payload=None, timeout=90):
        if url.endswith("/api/health"):
            return 200, {"ok": True, "build": {"sha": "a" * 40}}
        if url.endswith("/api/agent") and not token:
            return 401, None
        if url.endswith("/api/agent"):
            return 200, {
                "answer": "إجابة غير مكتملة. [المصدر 1]",
                "used_web_search": True,
                "used_language_model": True,
                "answer_evidence_status": "citation_indices_validated_only",
                "sources": [{"url": "https://example.test/source"}],
                "search_report": {
                    "search_outcome": "attempted_with_usable_sources",
                    "pipeline_completion_status": "partial",
                },
                "request_budget": {
                    "limits": {
                        "search_queries": 2, "search_calls": 8, "model_calls": 3,
                        "page_fetches": 2, "tool_calls": 0,
                    },
                    "counts": {
                        "search_queries": 1, "search_calls": 2, "model_calls": 2,
                        "page_fetches": 1, "tool_calls": 0,
                    },
                },
            }
        raise AssertionError(url)

    monkeypatch.setattr(hosted_smoke_test, "request_json", fake_request_json)
    import pytest
    with pytest.raises(hosted_smoke_test.SmokeError, match="pipeline did not complete"):
        hosted_smoke_test.run_smoke(
            "https://omarai.example", "T" * 40, expected_sha="a" * 40,
            allow_provider_usage=True,
        )


def test_hosted_smoke_rejects_empty_answer_even_with_sources(monkeypatch):
    def fake_request_json(url, *, token="", payload=None, timeout=90):
        if url.endswith("/api/health"):
            return 200, {"ok": True, "build": {"sha": "a" * 40}}
        if url.endswith("/api/agent") and not token:
            return 401, None
        if url.endswith("/api/agent"):
            return 200, {
                "answer": "  ",
                "used_web_search": True,
                "used_language_model": True,
                "answer_evidence_status": "citation_indices_validated_only",
                "sources": [{"url": "https://example.test/source"}],
                "search_report": {
                    "search_outcome": "attempted_with_usable_sources",
                    "pipeline_completion_status": "completed",
                },
                "request_budget": {
                    "limits": {
                        "search_queries": 2, "search_calls": 8, "model_calls": 3,
                        "page_fetches": 2, "tool_calls": 0,
                    },
                    "counts": {
                        "search_queries": 1, "search_calls": 2, "model_calls": 2,
                        "page_fetches": 1, "tool_calls": 0,
                    },
                },
            }
        raise AssertionError(url)

    monkeypatch.setattr(hosted_smoke_test, "request_json", fake_request_json)
    import pytest
    with pytest.raises(hosted_smoke_test.SmokeError, match="empty answer"):
        hosted_smoke_test.run_smoke(
            "https://omarai.example", "T" * 40, expected_sha="a" * 40,
            allow_provider_usage=True,
        )


def test_hosted_smoke_rejects_unvalidated_answer_evidence(monkeypatch):
    def fake_request_json(url, *, token="", payload=None, timeout=90):
        if url.endswith("/api/health"):
            return 200, {"ok": True, "build": {"sha": "a" * 40}}
        if url.endswith("/api/agent") and not token:
            return 401, None
        if url.endswith("/api/agent"):
            return 200, {
                "answer": "إجابة. [المصدر 1]",
                "used_web_search": True,
                "used_language_model": True,
                "answer_evidence_status": "sources_present",
                "sources": [{"url": "https://example.test/source"}],
                "search_report": {
                    "search_outcome": "attempted_with_usable_sources",
                    "pipeline_completion_status": "completed",
                },
                "request_budget": {
                    "limits": {
                        "search_queries": 2, "search_calls": 8, "model_calls": 3,
                        "page_fetches": 2, "tool_calls": 0,
                    },
                    "counts": {
                        "search_queries": 1, "search_calls": 2, "model_calls": 2,
                        "page_fetches": 1, "tool_calls": 0,
                    },
                },
            }
        raise AssertionError(url)

    monkeypatch.setattr(hosted_smoke_test, "request_json", fake_request_json)
    import pytest
    with pytest.raises(hosted_smoke_test.SmokeError, match="citation-index validation"):
        hosted_smoke_test.run_smoke(
            "https://omarai.example", "T" * 40, expected_sha="a" * 40,
            allow_provider_usage=True,
        )


def test_hosted_smoke_allows_no_token_only_for_loopback_dev(monkeypatch):
    def fake_request_json(url, *, token="", payload=None, timeout=90):
        if url.endswith("/api/health"):
            return 200, {"ok": True, "build": {"sha": "unknown"}}
        if url.endswith("/api/agent"):
            return 200, {
                "answer": "لا توجد إشارة شراء مؤكدة في المصادر التي تم فحصها. [المصدر 1]",
                "used_web_search": True,
                "used_language_model": True,
                "answer_evidence_status": "citation_indices_validated_only",
                "sources": [{"url": "https://example.test/egypt"}],
                "search_report": {
                    "search_outcome": "attempted_with_usable_sources",
                    "pipeline_completion_status": "completed",
                    "pages_fetched": 1,
                    "providers_used": ["bing_rss"],
                },
                "request_budget": {
                    "limits": {
                        "search_queries": 2, "search_calls": 8, "model_calls": 3,
                        "page_fetches": 2, "tool_calls": 0,
                    },
                    "counts": {
                        "search_queries": 1, "search_calls": 2, "model_calls": 2,
                        "page_fetches": 1, "tool_calls": 0,
                    },
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
