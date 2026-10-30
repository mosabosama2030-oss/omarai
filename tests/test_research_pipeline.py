from __future__ import annotations

from agents.research_pipeline import build_research_pipeline


def test_pipeline_unifies_intent_aspects_queries_and_evidence():
    question = "حلل السيارات الكهربائية في مصر من حيث السعر والبطارية والضمان"
    sources = [
        {
            "title": "أسعار السيارات الكهربائية في مصر",
            "url": "https://example.com/ev-prices",
            "snippet": "تفاصيل أسعار السيارات الكهربائية في مصر",
            "provider": "fixture",
        }
    ]

    result = build_research_pipeline(
        question,
        {"queries": ["السيارات الكهربائية في مصر"]},
        intent_route="WEB_DEEP",
        sources=sources,
    )

    assert result["intent"]["route"] == "WEB_DEEP"
    assert {"السعر", "البطارية", "الضمان"}.issubset(set(result["aspects"]))
    assert result["queries"]
    assert len(result["queries"]) <= 8
    assert result["evidence_ledger"]["aspects"] == result["aspects"]
    assert result["evidence_ledger"]["missing"]
    assert result["stages"]["semantic_matching"] == "not_configured"
    assert result["stages"]["claim_verification"] == "delegated_to_existing_validator"


def test_pipeline_clarifies_elliptical_question_without_search_plan():
    result = build_research_pipeline("كام سعرها؟", {"queries": ["كام سعرها"]})

    assert result["intent"]["route"] == "CLARIFY"
    assert result["intent"]["needs_clarification"] is True
    assert result["queries"] == []
    assert result["stages"]["query_planning"] == "blocked_pending_clarification"


def test_pipeline_resolves_followup_using_latest_context_anchor():
    history = [
        {"role": "user", "content": "عايز أعرف سعر iPhone 17 في مصر"},
        {"role": "assistant", "content": "سأبحث عن السعر."},
    ]

    result = build_research_pipeline("والضمان؟", {"queries": ["iPhone 17 مصر"]}, history=history)

    assert "iPhone 17" in result["contextual_question"]
    assert "الضمان" in result["contextual_question"]
    assert result["intent"]["context_available"] is True


def test_pipeline_bounds_malformed_inputs_and_keeps_semantic_stage_unassessed():
    result = build_research_pipeline(
        "س" * 9000,
        {"queries": ["س" * 1000] * 20},
        sources=[None, "not-a-source", {}],
    )

    assert len(result["contextual_question"]) <= 4000
    assert len(result["queries"]) <= 8
    assert result["evidence_ledger"]["aspects"] == []
    assert result["stages"]["semantic_matching"] == "not_configured"
