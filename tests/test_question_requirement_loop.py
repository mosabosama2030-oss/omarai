from __future__ import annotations

import json

from agents.answer_validation import audit_answer_integrity, build_requirement_evidence_ledger
from agents.research import (
    MAX_PLAN_QUERIES,
    extract_question_coverage_targets,
    fallback_plan,
    validate_plan,
)
from agents.web_agent import WebAgent


QUESTION = "قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية والكاميرا"


def test_compound_question_extracts_each_explicit_criterion() -> None:
    assert extract_question_coverage_targets(QUESTION) == ["السعر", "البطارية", "الكاميرا"]


def test_fallback_plan_assigns_a_bounded_query_to_every_criterion() -> None:
    plan = fallback_plan(QUESTION)
    requirement_queries = plan["requirement_queries"]
    assert [item["target"] for item in requirement_queries] == ["السعر", "البطارية", "الكاميرا"]
    assert all(item["query"] in plan["queries"] for item in requirement_queries)
    assert len(plan["queries"]) <= MAX_PLAN_QUERIES
    assert all(item["target"] in item["query"] for item in requirement_queries)


def test_validated_model_plan_cannot_drop_mandatory_criterion_queries() -> None:
    fallback = fallback_plan(QUESTION)
    candidate = {
        "queries": ["iPhone 17 Samsung S26 reviews"],
        "social_focus": False,
        "freshness": "any",
        "depth": "deep",
        "platforms": [],
    }

    validated = validate_plan(candidate, QUESTION)

    assert validated["coverage_targets"] == fallback["coverage_targets"]
    assert validated["requirement_queries"] == fallback["requirement_queries"]
    assert all(item["query"] in validated["queries"] for item in fallback["requirement_queries"])
    assert len(validated["queries"]) <= MAX_PLAN_QUERIES


def test_model_planner_cannot_replace_every_criterion_with_one_generic_query(monkeypatch) -> None:
    agent = WebAgent()
    agent.api_key = "test-key"
    monkeypatch.setattr(
        agent,
        "_request_completion",
        lambda *args, **kwargs: json.dumps(
            {
                "queries": ["iPhone Samsung review"],
                "social_focus": False,
                "freshness": "any",
                "depth": "deep",
                "platforms": [],
            }
        ),
    )

    plan = agent._plan_search(QUESTION, [])

    assert plan["coverage_targets"] == ["السعر", "البطارية", "الكاميرا"]
    assert all(item["query"] in plan["queries"] for item in plan["requirement_queries"])
    assert len(plan["queries"]) <= MAX_PLAN_QUERIES


def test_requirement_evidence_ledger_distinguishes_candidate_from_query_only_result() -> None:
    plan = fallback_plan(QUESTION)
    queries = plan["requirement_queries"]
    price_query = next(item["query"] for item in queries if item["target"] == "السعر")
    battery_query = next(item["query"] for item in queries if item["target"] == "البطارية")
    sources = [
        {
            "url": "https://example.com/price",
            "title": "Phone pricing",
            "snippet": "The current price is listed for both phone models.",
            "page_text": "The current price is 100 EGP.",
            "page_fetched": True,
            "queries": [price_query],
        },
        {
            "url": "https://example.net/specs",
            "title": "General technical specifications",
            "snippet": "Technical specifications for the two products are listed here.",
            "page_fetched": False,
            "queries": [battery_query],
        },
    ]

    ledger = build_requirement_evidence_ledger(plan["coverage_targets"], sources, queries)
    by_target = {item["target"]: item for item in ledger}

    assert by_target["السعر"]["status"] == "candidate_evidence_found_not_verified"
    assert by_target["السعر"]["candidate_source_indexes"] == [1]
    assert by_target["البطارية"]["status"] == "query_returned_candidates_no_lexical_signal"
    assert by_target["البطارية"]["query_result_source_indexes"] == [2]
    assert by_target["الكاميرا"]["status"] == "no_candidate_evidence_found"
    assert all(item["semantic_verification"] is False for item in ledger)
    assert all(item["source_entailment_verified"] is False for item in ledger)


def test_answer_integrity_exposes_requirement_evidence_separately_from_word_overlap() -> None:
    plan = fallback_plan(QUESTION)
    price_query = next(item["query"] for item in plan["requirement_queries"] if item["target"] == "السعر")
    sources = [
        {
            "url": "https://example.com/price",
            "title": "Phone pricing",
            "snippet": "The price is 100 EGP.",
            "page_fetched": False,
            "queries": [price_query],
        }
    ]

    result = audit_answer_integrity(
        QUESTION,
        "السعر غير محسوم والبطارية غير محسومة والكاميرا غير محسومة.",
        sources,
        plan["coverage_targets"],
        plan["requirement_queries"],
    )

    evidence = {item["target"]: item for item in result["requirement_evidence"]}
    assert evidence["السعر"]["status"] == "candidate_evidence_found_not_verified"
    assert evidence["البطارية"]["status"] == "no_candidate_evidence_found"
    assert result["semantic_verification"] is False
    assert result["requirements_without_candidate_evidence_count"] == 2
    assert result["target_coverage"][0]["evidence"]["status"] == "candidate_evidence_found_not_verified"
