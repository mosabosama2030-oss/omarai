from __future__ import annotations

from agents.answer_validation import audit_answer_integrity


def test_population_answer_reports_missing_source_url_date_and_geographic_scope():
    result = audit_answer_integrity(
        "ما عدد سكان القاهرة؟",
        "حسب تقديرات 2024، عدد السكان 9.7 مليون.",
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
    assert audit["sources_missing_publication_or_data_date_count"] == 1
    assert audit["sources_missing_geographic_scope_count"] == 1
    assert audit["semantic_verification"] is False
    assert audit["source_entailment_verified"] is False


def test_population_source_metadata_presence_does_not_claim_truth_verification():
    result = audit_answer_integrity(
        "ما عدد سكان القاهرة؟",
        "عدد السكان وفق المصدر [المصدر 1].",
        [{
            "title": "Population report",
            "url": "https://example.org/population",
            "published_at": "2025-06-01",
            "geographic_scope": "Cairo Governorate administrative boundary",
            "snippet": "Population estimate for Cairo Governorate.",
            "page_fetched": False,
        }],
    )

    audit = result["source_metadata_audit"]
    assert audit["status"] == "minimum_metadata_present"
    assert audit["sources_missing_or_invalid_url_count"] == 0
    assert audit["sources_missing_publication_or_data_date_count"] == 0
    assert audit["sources_missing_geographic_scope_count"] == 0
    assert audit["semantic_verification"] is False
    assert audit["source_entailment_verified"] is False
