"""Deterministic lexical answer-integrity screens; these do not verify semantic truth."""
from __future__ import annotations

from agents.answer_validation import audit_answer_integrity


def test_numeric_screen_accepts_arabic_digits_and_thousands_formatting():
    result = audit_answer_integrity(
        "ما السعر المذكور في 2025؟",
        "السعر ١٠٠٬٠٠٠ جنيه في 2025 [المصدر 1].",
        [{
            "title": "تفاصيل السعر",
            "snippet": "السعر 100,000 جنيه",
            "page_text": "السعر 100,000 جنيه",
            "page_fetched": True,
            "published_at": "",
        }],
        ["السعر"],
    )
    assert result["numeric_check_status"] == "all_checked_numeric_literals_appear_in_source_text"
    assert result["potentially_unsupported_numeric_literals"] == []
    assert result["source_evidence_scope"] == "contains_extracted_page_text_and_or_snippets"
    assert result["citation_marker_count"] == 1
    assert result["semantic_verification"] is False


def test_numeric_screen_flags_number_absent_from_available_evidence():
    result = audit_answer_integrity(
        "ما السعر؟",
        "السعر 500 جنيه [المصدر 1].",
        [{
            "title": "تفاصيل السعر",
            "snippet": "السعر 300 جنيه",
            "page_fetched": False,
            "published_at": "",
        }],
    )
    assert result["numeric_check_status"] == "potentially_unsupported_numeric_literals"
    assert "500" in result["potentially_unsupported_numeric_literals"]
    assert result["citation_entailment"] == "not_checked"


def test_task_coverage_screen_flags_a_potentially_missing_target_without_claiming_failure():
    result = audit_answer_integrity(
        "قارن من حيث السعر والمساحة",
        "من حيث السعر، الخيار الأول أقل تكلفة.",
        [{
            "title": "إعلان",
            "snippet": "السعر والمساحة غير موضحين",
            "page_fetched": False,
        }],
        ["السعر", "المساحة"],
    )
    checks = {item["target"]: item for item in result["target_coverage"]}
    assert checks["السعر"]["status"] == "lexical_signal_found"
    assert checks["المساحة"]["status"] == "possibly_missing"
    assert result["potentially_missing_target_count"] == 1
    assert result["method"] == "deterministic_lexical_screen_only"
    assert result["independent_fact_check"] is False


def test_source_scope_does_not_confuse_snippet_with_fetched_page():
    result = audit_answer_integrity(
        "ما التفاصيل؟",
        "وجدت مقتطفًا.",
        [{"title": "نتيجة", "snippet": "مقتطف قصير", "page_fetched": False}],
    )
    assert result["source_evidence_scope"] == "search_snippets_only"
    assert result["pages_with_extracted_text"] == 0
    assert result["sources_with_snippets_only"] == 1


def test_citation_alignment_uses_fetched_page_text_and_flags_weak_overlap():
    page_source = {
        "title": "Report",
        "snippet": "completely unrelated snippet about fruit",
        "page_text": "Renewable energy storage costs decreased during the reporting period.",
        "page_fetched": True,
        "published_at": "",
    }
    good = audit_answer_integrity(
        "What changed?",
        "Renewable energy storage costs decreased [source 1].",
        [page_source],
    )
    assert good["citation_lexical_alignment_method"] == "content_word_overlap_heuristic_not_entailment"
    assert good["citation_lexical_alignment"][0]["status"] == "lexical_overlap_signal_found"
    assert good["citation_lexical_alignment"][0]["citations"][0]["evidence_basis"] == "extracted_page_text"
    assert good["citation_entailment"] == "not_checked"

    weak = audit_answer_integrity(
        "What happened?",
        "Mango harvest volume rose sharply [source 1].",
        [page_source],
    )
    assert weak["citation_lexical_alignment"][0]["status"] == "weak_lexical_overlap"
    assert weak["weak_citation_alignment_count"] == 1
    assert weak["independent_fact_check"] is False


def test_snippet_only_citation_alignment_is_labeled_as_snippet_evidence():
    result = audit_answer_integrity(
        "What was reported?",
        "The reported costs changed [المصدر 1].",
        [{
            "title": "Costs report",
            "snippet": "Reported costs changed in the new report.",
            "page_fetched": False,
        }],
    )
    assert result["citation_lexical_alignment"][0]["citations"][0]["evidence_basis"] == "search_snippet"
    assert result["citation_entailment"] == "not_checked"


def test_cited_number_must_appear_in_the_exact_cited_source_not_merely_some_source():
    result = audit_answer_integrity(
        "قارن أسعار المنتجين",
        "سعر المنتج الأول 500 جنيه [المصدر 1].",
        [
            {
                "title": "سعر المنتج الأول",
                "snippet": "سعر المنتج الأول 300 جنيه",
                "page_fetched": False,
            },
            {
                "title": "سعر المنتج الثاني",
                "snippet": "سعر المنتج الثاني 500 جنيه",
                "page_fetched": False,
            },
        ],
    )

    assert result["potentially_unsupported_numeric_literals"] == []
    assert result["potentially_unsupported_numeric_by_citation_count"] == 1
    cited_check = result["citation_numeric_support"][0]
    assert cited_check["cited_source_indexes"] == [1]
    assert cited_check["potentially_unsupported_numeric_literals"] == ["500"]
    assert cited_check["status"] == "potentially_unsupported_numeric_literals_for_cited_sources"


def test_different_price_values_are_flagged_for_review_not_called_contradictions():
    result = audit_answer_integrity(
        "قارن العروض",
        "العرض الأول أرخص من الثاني [المصدر 1] [المصدر 2].",
        [
            {
                "title": "شقة القاهرة",
                "snippet": "السعر 100000 جنيه",
                "page_fetched": False,
            },
            {
                "title": "شقة القاهرة",
                "snippet": "السعر 120000 جنيه",
                "page_fetched": False,
            },
        ],
    )

    price = next(
        item for item in result["potential_value_discrepancies"]
        if item["dimension"] == "price_or_cost"
    )
    assert {item["value"] for item in price["values"]} == {"100000", "120000"}
    assert price["status"] == "potential_variation_or_conflict_requires_entity_review"
    assert "contradiction" not in price["status"]
    assert result["independent_fact_check"] is False


def test_date_in_answer_missing_from_its_cited_source_is_flagged():
    result = audit_answer_integrity(
        "ما تاريخ التقرير؟",
        "صدر التقرير في 2026 [المصدر 1].",
        [{
            "title": "تقرير سابق",
            "snippet": "تقرير منشور في 2024.",
            "published_at": "2024",
            "page_fetched": False,
        }],
    )

    numeric_check = result["citation_numeric_support"][0]
    assert numeric_check["potentially_unsupported_numeric_literals"] == ["2026"]
    assert numeric_check["status"] == "potentially_unsupported_numeric_literals_for_cited_sources"
