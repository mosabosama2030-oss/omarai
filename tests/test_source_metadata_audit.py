from __future__ import annotations

from agents.answer_validation import audit_answer_integrity


def test_population_question_reports_missing_url_publication_date_period_and_scope():
    result = audit_answer_integrity(
        "ما عدد سكان القاهرة؟",
        "حسب التقديرات، العدد 9.7 مليون.",
        [{
            "title": "تقديرات سكانية",
            "snippet": "عدد السكان 9.7 مليون",
            "page_fetched": False,
        }],
    )

    audit = result["source_metadata_audit"]
    assert audit["status"] == "metadata_gaps_found"
    assert audit["population_claim_context_detected"] is True
    assert audit["sources_missing_or_invalid_url_count"] == 1
    assert audit["sources_missing_publication_date_count"] == 1
    assert audit["sources_missing_data_reference_period_count"] == 1
    assert audit["sources_missing_publication_or_data_date_count"] == 1
    assert audit["sources_missing_geographic_scope_count"] == 1
    assert audit["semantic_verification"] is False
    assert audit["source_entailment_verified"] is False


def test_population_source_metadata_presence_does_not_claim_truth_verification():
    result = audit_answer_integrity(
        "ما عدد سكان القاهرة؟",
        "العدد وفق المصدر [المصدر 1].",
        [{
            "title": "Population report",
            "url": "https://example.org/population",
            "published_at": "2025-06-01",
            "data_reference_period": "2025 estimate",
            "geographic_scope": "Cairo Governorate administrative boundary",
            "snippet": "Population estimate for Cairo Governorate.",
            "page_fetched": False,
        }],
    )

    audit = result["source_metadata_audit"]
    assert audit["status"] == "minimum_metadata_present"
    assert audit["sources_missing_or_invalid_url_count"] == 0
    assert audit["sources_missing_publication_date_count"] == 0
    assert audit["sources_missing_data_reference_period_count"] == 0
    assert audit["sources_missing_publication_or_data_date_count"] == 0
    assert audit["sources_missing_geographic_scope_count"] == 0
    assert audit["semantic_verification"] is False
    assert audit["source_entailment_verified"] is False


def test_zero_sources_are_not_reported_as_metadata_complete():
    result = audit_answer_integrity(
        "ما عدد سكان القاهرة؟",
        "لا تتوفر لدي مصادر قابلة للمراجعة.",
        [],
    )

    audit = result["source_metadata_audit"]
    assert audit["status"] == "no_sources_to_audit"
    assert audit["source_count_checked"] == 0
    assert audit["semantic_verification"] is False
    assert audit["source_entailment_verified"] is False


def test_population_scope_is_required_even_when_answer_uses_only_a_number():
    result = audit_answer_integrity(
        "How many people live in Cairo?",
        "The estimate is 9.7 million.",
        [{
            "title": "Population estimate",
            "url": "https://example.org/cairo",
            "published_at": "2025-06-01",
            "data_year": 2025,
            "snippet": "An estimate for Cairo.",
            "page_fetched": False,
        }],
    )

    audit = result["source_metadata_audit"]
    assert audit["population_claim_context_detected"] is True
    assert audit["sources_missing_geographic_scope_count"] == 1
    assert "missing_explicit_geographic_scope_for_population_claim" in audit["sources"][0]["missing_fields"]
