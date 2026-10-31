from __future__ import annotations

import json

import pytest

from agents.web_agent import WebAgent


class FakeResponse:
    def __init__(self, content: str, finish_reason: str | None = None, *, include_reason: bool = True):
        choice = {"message": {"content": content}}
        if include_reason:
            choice["finish_reason"] = finish_reason
        self.body = json.dumps({"choices": [choice]}).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def read(self, limit: int) -> bytes:
        return self.body[:limit]


def test_missing_finish_reason_is_rejected_and_bounded_fallback_is_used(monkeypatch):
    agent = WebAgent()
    agent.api_key = "test-key"
    agent.fallback_model = "backup/model"
    calls: list[str] = []

    def fake_urlopen(request, timeout):
        model = json.loads(request.data.decode("utf-8"))["model"]
        calls.append(model)
        if model == "primary/model":
            return FakeResponse("possibly incomplete response", include_reason=False)
        return FakeResponse("إجابة مكتملة من النموذج الاحتياطي", "stop")

    monkeypatch.setattr("agents.web_agent._open_model_request", fake_urlopen)

    answer = agent._request_completion(
        [{"role": "user", "content": "اختبار"}],
        model="primary/model",
    )

    assert answer == "إجابة مكتملة من النموذج الاحتياطي"
    assert calls == ["primary/model", "backup/model"]
    assert [item["status"] for item in agent.generation_diagnostics] == [
        "finish_reason_missing",
        "accepted",
    ]
    assert agent.generation_diagnostics[0]["attempted_model"] == "primary/model"
    assert agent.generation_diagnostics[1]["attempted_model"] == "backup/model"
    assert [item["attempt_number"] for item in agent.generation_diagnostics] == [1, 2]
    assert [item["fallback_used"] for item in agent.generation_diagnostics] == [False, True]
    assert all(item["request_started"] is True for item in agent.generation_diagnostics)
    assert all(item["remote_response_received"] is True for item in agent.generation_diagnostics)


def test_unknown_finish_reason_is_rejected_and_fallback_is_used(monkeypatch):
    agent = WebAgent()
    agent.api_key = "test-key"
    agent.fallback_model = "backup/model"
    calls: list[str] = []

    def fake_urlopen(request, timeout):
        model = json.loads(request.data.decode("utf-8"))["model"]
        calls.append(model)
        if model == "primary/model":
            return FakeResponse("response with unrecognized termination", "vendor_specific_done")
        return FakeResponse("إجابة مكتملة", "stop")

    monkeypatch.setattr("agents.web_agent._open_model_request", fake_urlopen)

    answer = agent._request_completion(
        [{"role": "user", "content": "اختبار"}],
        model="primary/model",
    )

    assert answer == "إجابة مكتملة"
    assert calls == ["primary/model", "backup/model"]
    assert agent.generation_diagnostics[0]["status"] == "finish_reason_not_accepted"
    assert agent.generation_diagnostics[0]["finish_reason"] == "vendor_specific_done"


def test_missing_finish_reason_from_all_models_fails_closed(monkeypatch):
    agent = WebAgent()
    agent.api_key = "test-key"
    agent.fallback_model = ""
    calls: list[str] = []

    def fake_urlopen(request, timeout):
        calls.append(json.loads(request.data.decode("utf-8"))["model"])
        return FakeResponse("may be incomplete", include_reason=False)

    monkeypatch.setattr("agents.web_agent._open_model_request", fake_urlopen)

    with pytest.raises(RuntimeError, match="سبب انتهاء واضحًا"):
        agent._request_completion(
            [{"role": "user", "content": "اختبار"}],
            model="primary/model",
        )

    assert calls == ["primary/model"]
    assert agent.model_usage == []
    assert agent.generation_diagnostics == [{
        "attempt_number": 1,
        "requested_model": "primary/model",
        "attempted_model": "primary/model",
        "fallback_used": False,
        "request_started": True,
        "remote_response_received": True,
        "status": "finish_reason_missing",
    }]


def test_capability_question_distinguishes_configuration_from_live_health(monkeypatch):
    agent = WebAgent()

    monkeypatch.setattr(
        agent,
        "_collect_research",
        lambda plan: pytest.fail("Capability questions must not run live search"),
    )

    result = agent.answer("هل تستطيع البحث على الانترنت؟")

    assert result["kind"] == "capability_answer"
    assert result["final_answer_status"] == "local_response_no_generation"
    assert result["search_attempted"] is False
    assert result["used_web_search"] is False
    capability = result["capability_status"]["web_search"]
    assert capability["implemented"] is True
    assert capability["runtime_status"] == "not_tested_in_this_response"
    assert capability["local_dependencies_ready"] is True
    assert "لم أنفّذ اختبار اتصال حي" in result["answer"]
    assert "DuckDuckGo HTML" in result["answer"]


@pytest.mark.parametrize("mode", ["auto", "deep", "latest", "social"])
def test_current_request_search_status_is_not_confused_with_capability(monkeypatch, mode):
    agent = WebAgent()
    monkeypatch.setattr(
        agent,
        "_collect_research",
        lambda plan: pytest.fail("This asks about the current response, not a web lookup"),
    )

    result = agent.answer("هل بحثت في الانترنت للاجابة الحالية؟", mode=mode)

    assert result["kind"] == "capability_answer"
    assert result["request_execution_status"] == {
        "search_attempted": False,
        "search_outcome": "not_attempted",
        "semantics": "status_of_this_request_only",
    }
    assert "لم أنفّذ بحثًا حيًا للإجابة عن هذا السؤال تحديدًا" in result["answer"]
    assert result["capability_status"]["web_search"]["runtime_status"] == (
        "not_tested_in_this_response"
    )
    assert result["search_attempted"] is False


def test_generation_failure_returns_partial_sources_and_diagnostics(monkeypatch):
    agent = WebAgent()
    agent.api_key = "test-key"
    question = "ابحث عن أحدث تقرير عن الذكاء الاصطناعي"

    sources = [
        {
            "title": "تقرير ذكاء اصطناعي",
            "url": "https://example.com/report",
            "snippet": "مقتطف تجريبي من المصدر الأول",
            "page_fetched": False,
            "providers": ["duckduckgo_html"],
            "queries": [question],
            "domain": "example.com",
            "source_class": "general",
            "platform": "web",
            "published_at": "",
            "rank_score": 0.9,
        },
        {
            "title": "مصدر ثان",
            "url": "https://example.net/report",
            "snippet": "مقتطف تجريبي من المصدر الثاني",
            "page_fetched": False,
            "providers": ["bing_rss"],
            "queries": [question],
            "domain": "example.net",
            "source_class": "general",
            "platform": "web",
            "published_at": "",
            "rank_score": 0.8,
        },
    ]

    monkeypatch.setattr(
        agent,
        "_plan_search",
        lambda question, history: {
            "queries": [question],
            "depth": "standard",
            "freshness": "any",
            "social_focus": False,
            "platforms": [],
            "planning_method": "test_fixture",
            "direct_urls": [],
        },
    )
    monkeypatch.setattr(
        agent,
        "_collect_research",
        lambda plan: (
            sources,
            [],
            {
                "queries_planned": 1,
                "queries_attempted": 1,
                "queries_attempted_known": True,
                "search_attempted": True,
                "search_outcome": "attempted_with_usable_sources",
                "unique_sources": 2,
                "pages_fetched": 0,
                "providers_used": ["duckduckgo_html", "bing_rss"],
                "provider_counts": {"duckduckgo_html": 1, "bing_rss": 1},
                "platform_counts": {"web": 2},
                "evidence_signals": {},
            },
        ),
    )
    monkeypatch.setattr(agent, "_source_matches_query", lambda query, source: True)

    def failed_generate(*args, **kwargs):
        agent._record_generation_diagnostic(
            requested_model="primary/model",
            attempted_model="fallback/model",
            status="truncated",
            finish_reason="length",
        )
        raise RuntimeError("اختبار: فشل التوليد بعد انتهاء حد الرموز")

    monkeypatch.setattr(agent, "_generate", failed_generate)

    result = agent.answer(question)

    assert result["used_web_search"] is True
    assert result["used_language_model"] is False
    assert result["final_answer_status"] == "generation_failed_with_source_fallback"
    assert len(result["sources"]) == 2
    assert "تعذر توليد إجابة تحليلية" in result["answer"]
    assert "مقتطف تجريبي من المصدر الأول" in result["answer"]
    assert result["generation_diagnostics"] == [
        {
            "attempt_number": 1,
            "requested_model": "primary/model",
            "attempted_model": "fallback/model",
            "fallback_used": True,
            "request_started": True,
            "remote_response_received": True,
            "status": "truncated",
            "finish_reason": "length",
        }
    ]
    assert result["search_report"]["research_quality"] == "partial"
    assert result["citation_validation"]["status"] != "validated_as_fact"


def test_missing_api_key_is_reported_as_not_configured_not_attempted(monkeypatch):
    agent = WebAgent()
    agent.api_key = ""
    agent.generation_diagnostics = []
    agent._generation_attempt_sequence = 0
    with pytest.raises(RuntimeError, match="لم يتم ضبط مفتاح"):
        agent._request_completion(
            [{"role": "user", "content": "اختبار"}],
            model="primary/model",
        )
    assert agent.generation_diagnostics == [{
        "attempt_number": 1,
        "requested_model": "primary/model",
        "attempted_model": "primary/model",
        "fallback_used": False,
        "request_started": False,
        "remote_response_received": False,
        "status": "not_configured",
        "error_class": "MissingAPIKey",
    }]
