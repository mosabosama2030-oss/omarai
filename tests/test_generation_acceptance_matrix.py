from __future__ import annotations

import json

import pytest

from agents.request_budget import RequestBudget, RequestBudgetExceeded
from agents.web_agent import WebAgent


class FakeCompletionResponse:
    def __init__(
        self,
        content: str,
        finish_reason: str | None,
        *,
        include_reason: bool = True,
    ) -> None:
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


def source(
    url: str,
    domain: str,
    *,
    page_fetched: bool,
    page_text: str = "",
    snippet: str = "",
    provider: str = "test_provider",
) -> dict:
    return {
        "title": f"نتيجة عن {domain}",
        "url": url,
        "snippet": snippet or page_text[:200],
        "page_text": page_text,
        "page_fetched": page_fetched,
        "providers": [provider],
        "queries": ["قارن بين سعر المنتج ومساحته"],
        "domain": domain,
        "source_class": "general",
        "platform": "web",
        "published_at": "",
        "rank_score": 0.8,
    }


@pytest.mark.parametrize(
    "finish_reason",
    ["tool_calls", "function_call", "error", "abort", "cancelled", "vendor_specific_done"],
)
def test_only_normal_stop_is_accepted_as_a_complete_text_answer(
    monkeypatch, finish_reason
):
    agent = WebAgent()
    agent.api_key = "test-key"
    agent.fallback_model = ""
    partial_text = "نص لا يجب قبوله كإجابة نهائية"
    monkeypatch.setattr(
        "agents.web_agent.urllib.request.urlopen",
        lambda request, timeout: FakeCompletionResponse(partial_text, finish_reason),
    )

    with pytest.raises(RuntimeError):
        agent._request_completion(
            [{"role": "user", "content": "اختبار"}],
            model="primary/model",
        )

    assert agent.model_usage == []
    assert agent.generation_diagnostics == [
        {
            "attempt_number": 1,
            "requested_model": "primary/model",
            "attempted_model": "primary/model",
            "fallback_used": False,
            "request_started": True,
            "remote_response_received": True,
            "status": "finish_reason_not_accepted",
            "finish_reason": finish_reason,
        }
    ]


def test_both_models_truncated_fail_without_returning_either_partial_answer(monkeypatch):
    agent = WebAgent()
    agent.api_key = "test-key"
    agent.fallback_model = "fallback/model"
    calls: list[str] = []

    def fake_urlopen(request, timeout):
        model = json.loads(request.data.decode("utf-8"))["model"]
        calls.append(model)
        return FakeCompletionResponse(f"نص مبتور من {model}", "length")

    monkeypatch.setattr("agents.web_agent.urllib.request.urlopen", fake_urlopen)

    with pytest.raises(RuntimeError, match="مبتورة"):
        agent._request_completion(
            [{"role": "user", "content": "اختبار"}],
            model="primary/model",
        )

    assert calls == ["primary/model", "fallback/model"]
    assert agent.model_usage == []
    assert [item["status"] for item in agent.generation_diagnostics] == [
        "truncated",
        "truncated",
    ]
    assert all("مبتور" not in str(item) for item in agent.generation_diagnostics)


def test_model_fallback_cannot_exceed_request_model_call_budget(monkeypatch):
    agent = WebAgent()
    agent.api_key = "test-key"
    agent.fallback_model = "fallback/model"
    budget = RequestBudget(timeout_seconds=60, limits={"model_calls": 1})
    agent._request_budget = budget
    calls: list[str] = []

    def fake_urlopen(request, timeout):
        model = json.loads(request.data.decode("utf-8"))["model"]
        calls.append(model)
        return FakeCompletionResponse("محتوى مبتور", "length")

    monkeypatch.setattr("agents.web_agent.urllib.request.urlopen", fake_urlopen)

    with pytest.raises(RequestBudgetExceeded):
        agent._request_completion(
            [{"role": "user", "content": "اختبار"}],
            model="primary/model",
        )

    assert calls == ["primary/model"]
    assert budget.snapshot()["counts"]["model_calls"] == 1
    assert [item["status"] for item in agent.generation_diagnostics] == [
        "truncated",
        "budget_exhausted",
    ]
    assert agent.generation_diagnostics[1]["request_started"] is False
    assert agent.generation_diagnostics[1]["remote_response_received"] is False
    assert agent.model_usage == []


def test_capability_snapshot_separates_configuration_from_live_health(monkeypatch):
    agent = WebAgent()
    monkeypatch.setattr(
        agent,
        "status",
        lambda: {
            "web_search_ready": True,
            "language_model_configured": True,
            "deepseek_search_api_configured": True,
            "brave_search_api_configured": True,
            "tavily_search_api_configured": False,
            "openrouter_web_search_enabled": False,
        },
    )

    snapshot = agent._capability_status_snapshot()
    providers = {item["name"]: item for item in snapshot["web_search"]["providers"]}

    assert snapshot["web_search"]["implemented"] is True
    assert snapshot["web_search"]["local_dependencies_ready"] is True
    assert snapshot["web_search"]["runtime_status"] == "not_tested_in_this_response"
    assert providers["duckduckgo_html"]["configuration_status"] == "built_in_no_api_key"
    assert providers["duckduckgo_html"]["runtime_status"] == "not_tested_in_this_response"
    assert providers["deepseek_search_api"]["configuration_status"] == "configured"
    assert providers["deepseek_search_api"]["runtime_status"] == "not_tested_in_this_response"
    assert providers["brave_search_api"]["configuration_status"] == "configured"
    assert providers["brave_search_api"]["runtime_status"] == "not_tested_in_this_response"
    assert providers["tavily_search_api"]["configuration_status"] == "not_configured"
    assert providers["tavily_search_api"]["runtime_status"] == "not_configured"
    assert providers["openrouter_web_search"]["configuration_status"] == "disabled"
    assert providers["openrouter_web_search"]["runtime_status"] == "disabled"


def test_capability_answer_discloses_optional_deepseek_search_status(monkeypatch):
    agent = WebAgent()
    monkeypatch.setattr(
        agent,
        "status",
        lambda: {
            "web_search_ready": True,
            "language_model_configured": True,
            "deepseek_search_api_configured": True,
            "brave_search_api_configured": False,
            "tavily_search_api_configured": False,
            "openrouter_web_search_enabled": False,
        },
    )

    result = agent.answer("ما محركات البحث التي تستخدمها؟")

    assert result["kind"] == "capability_answer"
    assert "DeepSeek Search API" in result["answer"]
    assert "غير مختبر في هذه الإجابة" in result["answer"]
    assert "قد يستهلك استخدامًا مدفوعًا" in result["answer"]
    provider = next(
        item for item in result["capability_status"]["web_search"]["providers"]
        if item["name"] == "deepseek_search_api"
    )
    assert provider["configuration_status"] == "configured"
    assert provider["runtime_status"] == "not_tested_in_this_response"


def test_operational_truth_overrides_a_model_claim_about_this_request(monkeypatch):
    agent = WebAgent()
    model_calls: list[str] = []

    def dishonest_model(*args, **kwargs):
        model_calls.append("called")
        return "نعم، بحثت في الإنترنت وتحققت من المصادر."

    monkeypatch.setattr(agent, "_request_completion", dishonest_model)
    monkeypatch.setattr(
        agent,
        "_collect_research",
        lambda plan: pytest.fail("A current-search status question must stay local"),
    )

    result = agent.answer("هل بحثت في الانترنت للاجابة الحالية؟", mode="deep")

    assert model_calls == []
    assert result["search_attempted"] is False
    assert result["used_web_search"] is False
    assert result["request_execution_status"]["search_outcome"] == "not_attempted"
    assert "لم أنفّذ بحثًا حيًا للإجابة عن هذا السؤال تحديدًا" in result["answer"]
    assert "تحققت من المصادر" not in result["answer"]


def test_generation_budget_exhaustion_preserves_partial_sources(monkeypatch):
    agent = WebAgent()
    agent.api_key = "test-key"
    question = "ابحث عن أحدث معلومات حول الطاقة المتجددة"
    monkeypatch.setenv("OMARAI_REQUEST_MAX_MODEL_CALLS", "1")
    sources = [
        source(
            "https://one.example/energy",
            "one.example",
            page_fetched=True,
            page_text="معلومة مستخرجة من المصدر الأول عن الطاقة المتجددة.",
            provider="duckduckgo_html",
        ),
        source(
            "https://two.example/energy",
            "two.example",
            page_fetched=False,
            snippet="مقتطف المصدر الثاني عن الطاقة المتجددة.",
            provider="bing_rss",
        ),
    ]
    monkeypatch.setattr(
        agent,
        "_plan_search",
        lambda question, history: {
            "queries": [question],
            "direct_urls": [],
            "social_focus": False,
            "freshness": "current",
            "depth": "standard",
            "platforms": [],
            "planning_method": "test",
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
                "search_attempted": True,
                "search_outcome": "attempted_with_usable_sources",
                "unique_sources": 2,
                "pages_fetched": 1,
                "providers_used": ["duckduckgo_html", "bing_rss"],
                "provider_counts": {"duckduckgo_html": 1, "bing_rss": 1},
                "platform_counts": {"web": 2},
                "social_direct_results": 0,
                "provider_diagnostics": [],
                "evidence_signals": {},
            },
        ),
    )
    monkeypatch.setattr(agent, "_source_matches_query", lambda query, item: True)
    calls: list[str] = []

    def fake_urlopen(request, timeout):
        model = json.loads(request.data.decode("utf-8"))["model"]
        calls.append(model)
        return FakeCompletionResponse("إجابة مبتورة لا يجوز عرضها", "length")

    monkeypatch.setattr("agents.web_agent.urllib.request.urlopen", fake_urlopen)

    result = agent.answer(question)

    assert len(calls) == 1
    assert result["request_budget"]["counts"]["model_calls"] == 1
    assert "model_calls" in result["request_budget"]["exhausted_reasons"]
    assert result["final_answer_status"] == "budget_exhausted_with_source_fallback"
    assert result["used_language_model"] is False
    assert result["search_attempted"] is True
    assert len(result["sources"]) == 2
    assert "إجابة مبتورة لا يجوز عرضها" not in result["answer"]
    assert "مقتطف المصدر الثاني عن الطاقة المتجددة" in result["answer"]
    assert result["generation_diagnostics"][0]["status"] == "truncated"


def test_review_budget_exhaustion_discards_draft_and_preserves_sources(monkeypatch):
    agent = WebAgent()
    agent.api_key = "test-key"
    question = "قارن بين الخيارات من حيث السعر، المساحة، والبيانات الناقصة"
    monkeypatch.setenv("OMARAI_REQUEST_MAX_MODEL_CALLS", "1")
    sources = [
        source(
            "https://one.example/product",
            "one.example",
            page_fetched=True,
            page_text="السعر الإجمالي 100000 جنيه والمساحة 100 متر.",
            provider="duckduckgo_html",
        ),
        source(
            "https://two.example/product",
            "two.example",
            page_fetched=False,
            snippet="إعلان يذكر سعرًا دون بيان المساحة.",
            provider="bing_rss",
        ),
    ]
    monkeypatch.setattr(
        agent,
        "_plan_search",
        lambda question, history: {
            "queries": [question],
            "direct_urls": [],
            "social_focus": False,
            "freshness": "any",
            "depth": "deep",
            "platforms": [],
            "planning_method": "test",
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
                "search_attempted": True,
                "search_outcome": "attempted_with_usable_sources",
                "unique_sources": 2,
                "pages_fetched": 1,
                "providers_used": ["duckduckgo_html", "bing_rss"],
                "provider_counts": {"duckduckgo_html": 1, "bing_rss": 1},
                "platform_counts": {"web": 2},
                "social_direct_results": 0,
                "provider_diagnostics": [],
                "evidence_signals": {},
            },
        ),
    )
    monkeypatch.setattr(agent, "_source_matches_query", lambda query, item: True)
    calls: list[str] = []

    def fake_urlopen(request, timeout):
        calls.append(json.loads(request.data.decode("utf-8"))["model"])
        return FakeCompletionResponse(
            "مسودة تحليل مولدة لكنها لم تخضع للتدقيق النهائي [المصدر 1].",
            "stop",
        )

    monkeypatch.setattr("agents.web_agent.urllib.request.urlopen", fake_urlopen)

    result = agent.answer(question)

    assert len(calls) == 1
    assert result["request_budget"]["counts"]["model_calls"] == 1
    assert "model_calls" in result["request_budget"]["exhausted_reasons"]
    assert result["final_answer_status"] == "budget_exhausted_with_source_fallback"
    assert result["search_report"]["second_pass_review"] == "model_claim_audit_unavailable"
    assert len(result["sources"]) == 2
    assert "مسودة تحليل مولدة لكنها لم تخضع للتدقيق النهائي" not in result["answer"]
    assert "السعر الإجمالي 100000 جنيه والمساحة 100 متر." in result["answer"]


def test_search_failure_is_not_reported_as_no_attempt_or_completed_answer(monkeypatch):
    agent = WebAgent()
    question = "ابحث عن أحدث معلومات حول الطاقة المتجددة"

    monkeypatch.setattr(
        agent,
        "_plan_search",
        lambda question, history: {
            "queries": [question],
            "direct_urls": [],
            "social_focus": False,
            "freshness": "current",
            "depth": "standard",
            "platforms": [],
            "planning_method": "test",
        },
    )
    monkeypatch.setattr(
        agent,
        "_collect_research",
        lambda plan: (
            [],
            ["تعذر الاتصال بموصلات البحث"],
            {
                "queries_planned": 1,
                "queries_attempted": 1,
                "search_attempted": True,
                "search_outcome": "attempted_no_usable_sources",
                "unique_sources": 0,
                "pages_fetched": 0,
                "providers_used": [],
                "provider_diagnostics": [
                    {"provider": "duckduckgo_html", "status": "failed"},
                    {"provider": "bing_rss", "status": "timeout"},
                ],
                "evidence_signals": {},
            },
        ),
    )
    monkeypatch.setattr(
        agent,
        "_generate",
        lambda *args, **kwargs: pytest.fail("No final synthesis without usable sources"),
    )

    result = agent.answer(question)

    assert result["search_attempted"] is True
    assert result["used_web_search"] is False
    assert result["search_report"]["search_outcome"] == "attempted_no_usable_sources"
    assert result["final_answer_status"] == "insufficient_evidence_no_generation"
    assert result["used_language_model"] is False
    assert result["research_quality"] == "failed"
    assert result["answer_integrity"]["method"] == "deterministic_lexical_screen_only"
    assert result["answer_integrity"]["independent_fact_check"] is False
    assert result["search_report"]["answer_integrity"] == result["answer_integrity"]


def test_research_exception_does_not_claim_no_results_or_no_search(monkeypatch):
    agent = WebAgent()
    question = "ابحث عن أحدث معلومات حول الطاقة المتجددة"

    monkeypatch.setattr(
        agent,
        "_plan_search",
        lambda question, history: {
            "queries": [question],
            "direct_urls": [],
            "social_focus": False,
            "freshness": "current",
            "depth": "standard",
            "platforms": [],
            "planning_method": "test",
        },
    )

    def collect_fails_before_diagnostics(plan):
        raise RuntimeError("collector failed before the attempt status was known")

    monkeypatch.setattr(agent, "_collect_research", collect_fails_before_diagnostics)
    monkeypatch.setattr(
        agent,
        "_generate",
        lambda *args, **kwargs: pytest.fail("No synthesis when the research state is unknown"),
    )

    result = agent.answer(question)

    assert result["search_report"]["search_outcome"] == "unknown_after_research_error"
    assert result["search_report"]["unique_sources"] is None
    assert result["search_report"]["pages_fetched"] is None
    assert result["search_attempted"] is None
    assert result["final_answer_status"] == "insufficient_evidence_no_generation"
    assert "لا أستطيع الجزم" in result["answer"]
    assert "لم أجد معلومات موثوقة كافية" not in result["answer"]


def test_search_extraction_generation_and_task_review_remain_distinct(monkeypatch):
    agent = WebAgent()
    agent.api_key = "test-key"
    question = "قارن بين الخيارات من حيث السعر، المساحة، والبيانات الناقصة"
    sources = [
        source(
            "https://one.example/product",
            "one.example",
            page_fetched=True,
            page_text="السعر الإجمالي 100000 جنيه والمساحة 100 متر.",
            provider="duckduckgo_html",
        ),
        source(
            "https://two.example/product",
            "two.example",
            page_fetched=False,
            snippet="إعلان يذكر سعرًا دون بيان المساحة.",
            provider="bing_rss",
        ),
    ]
    monkeypatch.setattr(
        agent,
        "_plan_search",
        lambda question, history: {
            "queries": [question],
            "direct_urls": [],
            "social_focus": False,
            "freshness": "any",
            "depth": "deep",
            "platforms": [],
            "planning_method": "test",
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
                "search_attempted": True,
                "search_outcome": "attempted_with_usable_sources",
                "unique_sources": 2,
                "pages_fetched": 1,
                "providers_used": ["duckduckgo_html", "bing_rss"],
                "provider_counts": {"duckduckgo_html": 1, "bing_rss": 1},
                "platform_counts": {"web": 2},
                "social_direct_results": 0,
                "provider_diagnostics": [],
                "evidence_signals": {},
            },
        ),
    )
    monkeypatch.setattr(agent, "_source_matches_query", lambda query, item: True)
    final_draft = "الخلاصة: يوجد اختلاف في اكتمال البيانات، ولا يمكن حسم المقارنة من المقتطف وحده [المصدر 1]."
    repaired_answer = (
        "السعر الإجمالي 100000 جنيه والمساحة 100 متر في المصدر الأول [المصدر 1]. "
        "الإعلان الثاني يذكر سعرًا دون بيان المساحة، وهذه هي البيانات الناقصة [المصدر 2]."
    )
    monkeypatch.setattr(agent, "_generate", lambda *args, **kwargs: final_draft)
    monkeypatch.setattr(agent, "_review_answer", lambda question, answer, sources: answer)
    monkeypatch.setattr(
        agent,
        "_repair_answer_coverage",
        lambda question, answer, sources, missing_targets: repaired_answer,
    )

    result = agent.answer(question)

    assert result["search_attempted"] is True
    assert result["used_web_search"] is True
    assert len(result["sources"]) == 2
    assert result["search_report"]["search_outcome"] == "attempted_with_usable_sources"
    assert result["search_report"]["pages_fetched"] == 1
    assert result["final_answer_status"] == "model_answer_generated"
    assert result["coverage_repair_status"] == "revised_and_reaudited"
    assert result["search_report"]["second_pass_review"] == "model_claim_audit_completed"
    assert result["answer_coverage"]["automatically_graded"] is False
    assert result["answer_coverage"]["status"] == "model_review_requested_not_machine_verified"
    assert "السعر الإجمالي" in result["answer"]
    assert "البيانات الناقصة" in result["answer"]
    assert result["citation_validation"]["method"] == "numeric_source_index_range_only"
    assert result["answer_integrity"]["method"] == "deterministic_lexical_screen_only"
    assert result["answer_integrity"]["semantic_verification"] is False
    assert result["search_report"]["answer_integrity"] == result["answer_integrity"]
    assert result["answer_integrity"]["pages_with_extracted_text"] == 1
    assert result["answer_integrity"]["potentially_missing_target_count"] >= 0


@pytest.mark.parametrize(
    "malformed_review",
    [
        "إجابة من دون أي علامات فصل",
        "<<<OMARAI_FINAL_ANSWER>>>إجابة بلا علامة نهاية",
        "<<<OMARAI_FINAL_ANSWER>>>إجابة<<<END_OMARAI_FINAL_ANSWER>>> نص زائد خارج الإجابة",
    ],
)
def test_reviewer_rejects_missing_or_unbounded_final_answer_delimiters(
    monkeypatch, malformed_review
):
    agent = WebAgent()
    monkeypatch.setattr(
        agent,
        "_request_completion",
        lambda *args, **kwargs: malformed_review,
    )
    test_source = source(
        "https://one.example/page",
        "one.example",
        page_fetched=True,
        page_text="نص الصفحة",
    )

    with pytest.raises(RuntimeError, match="فصل الإجابة النهائية"):
        agent._review_answer("ما مضمون الصفحة؟", "مسودة", [test_source])
