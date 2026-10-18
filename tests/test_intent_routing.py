"""P0 intent routing regression tests (deterministic; no network)."""
from __future__ import annotations

from agents.web_agent import WebAgent


def _agent() -> WebAgent:
    agent = WebAgent()
    agent.api_key = ""  # force no model calls on LOCAL/CLARIFY/MODEL_ONLY fallback
    return agent


def test_greeting_is_local_without_search():
    agent = _agent()
    result = agent.answer("ازيك؟")
    assert result["intent_route"]["route"] == "LOCAL"
    assert result["used_web_search"] is False
    assert result["used_language_model"] is False
    assert result["sources"] == []
    assert result["kind"] in {"greeting", "capability_answer"}


def test_capability_question_is_local_without_search():
    agent = _agent()
    result = agent.answer("ازاي تقدر تساعدني؟")
    assert result["intent_route"]["route"] == "LOCAL"
    assert result["used_web_search"] is False
    assert result["used_language_model"] is False
    assert "أقدر" in result["answer"] or "بحث" in result["answer"]


def test_ambiguous_price_without_context_is_clarify():
    agent = _agent()
    result = agent.answer("كام سعرها؟")
    assert result["intent_route"]["route"] == "CLARIFY"
    assert result["used_web_search"] is False
    assert result["used_language_model"] is False
    assert result["sources"] == []
    assert result["kind"] == "clarify"
    assert "مرجع" in result["answer"] or "referent" in result["answer"].casefold()


def test_ambiguous_price_with_history_resolves_to_web_route():
    agent = _agent()
    history = [{"role": "user", "content": "هكلم عن سعر آيفون 16 في مصر"}]
    intent = agent._classify_intent_route("كام سعرها؟", history, "auto")
    assert intent["route"] in {"WEB_SIMPLE", "WEB_DEEP"}
    assert intent["web_search"] is True
    assert "آيفون" in intent["resolved_question"] or "ايفون" in intent["resolved_question"].casefold() or "16" in intent["resolved_question"]


def test_fresh_price_question_is_web_simple():
    agent = _agent()
    intent = agent._classify_intent_route("ما سعر الهاتف اليوم في مصر؟", None, "auto")
    assert intent["route"] == "WEB_SIMPLE"
    assert intent["web_search"] is True


def test_multipart_compare_is_web_deep():
    agent = _agent()
    intent = agent._classify_intent_route(
        "قارن بين هذه الخيارات من حيث السعر والبطارية والكاميرا",
        None,
        "auto",
    )
    assert intent["route"] == "WEB_DEEP"
    assert intent["web_search"] is True


def test_web_simple_does_not_call_search_when_monkeypatched_collect_unused_for_clarify():
    """CLARIFY must not invoke _collect_research."""
    agent = _agent()
    called = {"collect": 0, "plan": 0}

    def boom_plan(*args, **kwargs):
        called["plan"] += 1
        raise AssertionError("plan should not run on CLARIFY")

    def boom_collect(*args, **kwargs):
        called["collect"] += 1
        raise AssertionError("collect should not run on CLARIFY")

    agent._plan_search = boom_plan  # type: ignore[method-assign]
    agent._collect_research = boom_collect  # type: ignore[method-assign]
    result = agent.answer("كام سعرها؟")
    assert result["intent_route"]["route"] == "CLARIFY"
    assert called["plan"] == 0
    assert called["collect"] == 0


def test_explicit_deep_mode_forces_web_deep():
    agent = _agent()
    intent = agent._classify_intent_route("موضوع عام", None, "deep")
    assert intent["route"] == "WEB_DEEP"


def test_english_ambiguous_is_clarify():
    agent = _agent()
    result = agent.answer("Is it good?")
    assert result["intent_route"]["route"] == "CLARIFY"
    assert result["used_web_search"] is False


def test_model_only_preferred_when_no_live_terms():
    agent = _agent()
    intent = agent._classify_intent_route(
        "What is photosynthesis in one sentence?", None, "auto"
    )
    assert intent["route"] == "MODEL_ONLY"
    assert intent["web_search"] is False


def test_model_only_without_api_key_may_degrade_to_web_path(monkeypatch):
    """Without a model key, legacy behaviour continues into search rather than inventing text."""
    agent = _agent()
    monkeypatch.setattr(
        agent,
        "_plan_search",
        lambda question, history: {
            "queries": [question],
            "direct_urls": [],
            "social_focus": False,
            "freshness": "any",
            "depth": "standard",
            "platforms": [],
            "planning_method": "test",
        },
    )
    monkeypatch.setattr(
        agent,
        "_collect_research",
        lambda plan: ([], ["no results"], {
            "queries_planned": 1,
            "queries_attempted": 1,
            "query_results": [],
            "unique_sources": 0,
            "pages_fetched": 0,
            "providers_used": [],
            "platform_counts": {},
            "social_direct_results": 0,
            "depth": "standard",
            "planning_method": "test",
        }),
    )
    result = agent.answer("What is photosynthesis in one sentence?")
    assert result["intent_route"]["route"] == "WEB_SIMPLE"
    assert result["intent_route"].get("reason") == "model_unavailable_fallback_to_web"
