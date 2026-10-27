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
    assert result["citation_validation"]["method"] == "numeric_source_index_range_only"
    assert result["search_report"]["citation_validation"] == result["citation_validation"]
    assert any("iPhone 17" in query for query in seen["plan"]["queries"])


def test_multi_part_comparison_forces_deep_plan_and_multiple_angles(monkeypatch) -> None:
    agent = WebAgent()
    agent.api_key = "test-key"
    seen: dict = {"plans": []}
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
        seen["plans"].append(dict(research_plan))
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
    monkeypatch.setattr(agent, "_repair_answer_coverage", lambda _q, answer, _s, _m: answer)

    result = agent.answer(
        "قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية والكاميرا",
        history=history,
    )

    assert result["intent_route"] == "WEB_DEEP"
    assert result["research_plan"]["intent_route"] == "WEB_DEEP"
    assert result["research_plan"]["depth"] == "deep"
    initial_plan = seen["plans"][0]
    assert len(initial_plan["queries"]) > 1
    assert initial_plan["coverage_gap_repair_slot_reserved"] is True
    assert initial_plan["query_limit"] == 7
    # Each requested criterion gets a distinct search angle before generic deep
    # modifiers consume the bounded query budget.
    planned_queries = " ".join(initial_plan["queries"]).casefold()
    assert "السعر" in planned_queries
    assert "البطارية" in planned_queries
    assert "الكاميرا" in planned_queries
    assert len(initial_plan["queries"]) <= 7
    assert result["used_web_search"] is True
    coverage = result["answer_coverage"]
    assert coverage["method"] == "explicit_criteria_heuristic"
    assert coverage["targets"] == ["السعر", "البطارية", "الكاميرا"]
    assert coverage["status"] == "model_review_requested_not_machine_verified"
    assert coverage["automatically_graded"] is False
    # The mocked sources do not contain battery/camera evidence. The task must
    # remain visibly incomplete even if the planner generated multiple queries.
    assert coverage["source_evidence_gap_count"] == 2
    assert result["task_fulfillment_status"] == "possible_gap_detected"
    assert len(seen["plans"]) == 2
    assert "البطارية" in " ".join(seen["plans"][1]["queries"])
    assert result["search_report"]["criterion_gap_research"]["attempted"] is True
    assert result["search_report"]["criterion_gap_research"]["status"] == "search_completed_no_new_criterion_evidence"

def test_deep_plan_preserves_all_eight_explicit_criteria_within_query_budget(monkeypatch) -> None:
    agent = WebAgent()
    agent.api_key = "test-key"
    seen: dict = {"plans": []}
    question = (
        "قارن بين خدمات من حيث السعر، الخصوصية، الاعتمادية، الدعم، "
        "الأمان، السرعة، الجودة، والتوفر"
    )

    def plan(_question, _history):
        return {
            "queries": ["مقارنة الخدمات"],
            "direct_urls": [],
            "social_focus": False,
            "freshness": "any",
            "depth": "standard",
            "platforms": [],
            "planning_method": "test_single_query",
        }

    def collect(research_plan):
        seen["plans"].append(dict(research_plan))
        sources = [
            _evidence("example.com", research_plan["queries"]),
            _evidence("example.net", research_plan["queries"]),
        ]
        return sources, [], _report(research_plan, sources)

    monkeypatch.setattr(agent, "_plan_search", plan)
    monkeypatch.setattr(agent, "_collect_research", collect)
    monkeypatch.setattr(agent, "_source_matches_query", lambda _query, _source: True)
    monkeypatch.setattr(agent, "_generate", lambda *args, **kwargs: "مقارنة أولية [المصدر 1].")
    monkeypatch.setattr(agent, "_review_answer", lambda _question, answer, _sources: answer)
    monkeypatch.setattr(agent, "_repair_answer_coverage", lambda _q, answer, _s, _m: answer)

    agent.answer(question, history=[])

    # All eight explicit criteria consume the bounded initial query allowance;
    # the system must not launch an unbudgeted ninth query for coverage repair.
    assert len(seen["plans"]) == 1
    targets = WebAgent._question_coverage_targets(question)
    assert len(targets) == 8
    initial_plan = seen["plans"][0]
    queries = initial_plan["queries"]
    assert initial_plan["coverage_gap_repair_slot_reserved"] is False
    assert initial_plan["query_limit"] == 8
    assert len(queries) == 8
    for target in targets:
        assert any(target in query for query in queries), f"Missing criterion query for {target!r}"

