from __future__ import annotations

import pytest

from agents.research import evidence_signal_report
from agents.web_agent import WebAgent


def _evidence(domain: str, queries: list[str]) -> dict:
    return {
        "title": "iPhone 17 price information in Egypt",
        "url": f"https://{domain}/iphone-17-price",
        "snippet": "Published price information for iPhone 17 in Egypt.",
        "page_text": "Price information for iPhone 17 in Egypt.",
        "page_fetched": True,
        "providers": ["test_search"],
        "queries": list(queries),
        "domain": domain,
        "source_class": "general",
        "platform": "web",
        "published_at": "",
        "rank_score": 1.0,
    }


def _report(plan: dict, sources: list[dict]) -> dict:
    return {
        "queries_planned": len(plan.get("queries", [])),
        "queries_attempted": len(plan.get("queries", [])),
        "query_results": [],
        "unique_sources": len(sources),
        "pages_fetched": len(sources),
        "providers_used": ["test_search"],
        "provider_counts": {"test_search": len(sources)},
        "platform_counts": {"web": len(sources)},
        "social_direct_results": 0,
        "depth": plan.get("depth", "standard"),
        "planning_method": plan.get("planning_method", "test"),
        "evidence_signals": evidence_signal_report(sources),
    }


def test_greeting_is_local_without_model_or_search(monkeypatch) -> None:
    agent = WebAgent()

    def unexpected(*args, **kwargs):
        pytest.fail("Greeting must not call the model or search.")

    monkeypatch.setattr(agent, "_answer_without_search", unexpected)
    monkeypatch.setattr(agent, "_plan_search", unexpected)

    result = agent.answer("ازيك؟ عامل ايه النهاردة؟")

    assert result["kind"] == "local_conversation"
    assert result["intent_route"] == "LOCAL"
    assert result["research_plan"]["intent_route"] == "LOCAL"
    assert result["used_web_search"] is False
    assert result["used_language_model"] is False
    assert result["sources"] == []


def test_ambiguous_question_clarifies_without_model_or_search(monkeypatch) -> None:
    agent = WebAgent()

    def unexpected(*args, **kwargs):
        pytest.fail("An unresolved referent must be clarified without model/search.")

    monkeypatch.setattr(agent, "_answer_without_search", unexpected)
    monkeypatch.setattr(agent, "_plan_search", unexpected)
    monkeypatch.setattr(agent, "_collect_research", unexpected)

    result = agent.answer("كام سعرها؟")

    assert result["kind"] == "clarification_needed"
    assert result["intent_route"] == "CLARIFY"
    assert result["research_plan"]["intent_route"] == "CLARIFY"
    assert "تقصد" in result["answer"]
    assert result["used_web_search"] is False
    assert result["used_language_model"] is False
    assert result["sources"] == []


def test_contextual_price_followup_searches_with_previous_subject(monkeypatch) -> None:
    agent = WebAgent()
    agent.api_key = ""  # Keep this acceptance test deterministic and offline.
    seen: dict = {}
    history = [
        {"role": "user", "content": "عايز أعرف سعر iPhone 17 في مصر"},
        {"role": "assistant", "content": "نتحدث عن هاتف iPhone 17 في السوق المصري."},
    ]

    def collect(plan):
        seen["plan"] = dict(plan)
        sources = [
            _evidence("example.com", plan["queries"]),
            _evidence("example.net", plan["queries"]),
        ]
        return sources, [], _report(plan, sources)

    monkeypatch.setattr(agent, "_collect_research", collect)
    monkeypatch.setattr(agent, "_source_matches_query", lambda query, source: True)
    monkeypatch.setattr(agent, "_generate", lambda *args, **kwargs: "توجد أسعار مختلفة حسب النسخة [المصدر 1].")
    monkeypatch.setattr(agent, "_review_answer", lambda question, answer, sources: answer)

    result = agent.answer("كام سعرها؟", history=history)

    assert result["intent_route"] == "WEB_SIMPLE"
    assert result["research_plan"]["intent_route"] == "WEB_SIMPLE"
    assert result["used_web_search"] is True
    assert any("iPhone 17" in query for query in seen["plan"]["queries"])


def test_multi_part_comparison_forces_deep_plan_and_multiple_angles(monkeypatch) -> None:
    agent = WebAgent()
    agent.api_key = "test-key"
    seen: dict = {}
    history = []

    def plan(question, prior_history):
        return {
            "queries": ["iPhone 17 versus Samsung S26"],
            "direct_urls": [],
            "social_focus": False,
            "freshness": "any",
            "depth": "standard",
            "platforms": [],
            "planning_method": "test_single_query",
        }

    def collect(research_plan):
        seen["plan"] = dict(research_plan)
        sources = [
            _evidence("example.com", research_plan["queries"]),
            _evidence("example.net", research_plan["queries"]),
        ]
        return sources, [], _report(research_plan, sources)

    monkeypatch.setattr(agent, "_plan_search", plan)
    monkeypatch.setattr(agent, "_collect_research", collect)
    monkeypatch.setattr(agent, "_source_matches_query", lambda query, source: True)
    monkeypatch.setattr(agent, "_generate", lambda *args, **kwargs: "مقارنة أولية [المصدر 1].")
    monkeypatch.setattr(agent, "_review_answer", lambda question, answer, sources: answer)

    result = agent.answer(
        "قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية والكاميرا",
        history=history,
    )

    assert result["intent_route"] == "WEB_DEEP"
    assert result["research_plan"]["intent_route"] == "WEB_DEEP"
    assert result["research_plan"]["depth"] == "deep"
    assert len(seen["plan"]["queries"]) > 1
    assert result["used_web_search"] is True
