from __future__ import annotations

from agents.claim_evidence import audit_source_metadata, build_claim_evidence_ledger


def test_source_metadata_accepts_complete_population_metadata_without_asserting_truth():
    result = audit_source_metadata(
        {
            "url": "https://example.org/census",
            "title": "Population table",
            "publisher": "Example Statistics Office",
            "published_at": "2025-06-01",
            "data_reference_period": "2025 estimate",
            "geographic_scope": "Cairo Governorate administrative boundaries",
            "snippet": "Population estimate for the governorate.",
        },
        claim_text="عدد سكان محافظة القاهرة",
    )

    assert result["status"] == "metadata_complete"
    assert result["required_fields_missing"] == []
    assert result["claim_entailment"] == "not_checked"
    assert result["fact_correctness"] == "not_checked"
    assert result["semantic_verification"] is False


def test_source_metadata_flags_missing_publication_date_period_and_population_scope():
    result = audit_source_metadata(
        {
            "url": "https://example.org/census",
            "title": "Population table",
            "publisher": "Example Statistics Office",
            "snippet": "Population estimate.",
        },
        claim_text="عدد سكان القاهرة الكبرى",
    )

    assert result["status"] == "metadata_incomplete"
    assert "publication_date" in result["required_fields_missing"]
    assert "data_reference_period_for_population_claim" in result["required_fields_missing"]
    assert "geographic_scope_for_population_claim" in result["required_fields_missing"]


def test_source_metadata_rejects_non_http_urls_and_urls_with_credentials():
    for url in ("javascript:alert(1)", "https://user:password@example.org/data"):
        result = audit_source_metadata(
            {
                "url": url,
                "title": "Research report",
                "publisher": "Example Statistics Office",
                "published_at": "2025-06-01",
                "snippet": "A readable summary.",
            },
            claim_text="general research",
        )

        assert result["valid_http_url"] is False
        assert "valid_http_source_url" in result["required_fields_missing"]


def test_claim_evidence_ledger_uses_question_context_for_population_metadata():
    ledger = build_claim_evidence_ledger(
        "The estimate is 9.7 million [source 1].",
        [
            {
                "url": "https://example.org/census",
                "title": "Population table",
                "publisher": "Example Statistics Office",
                "published_at": "2025-06-01",
                "snippet": "The estimate is 9.7 million.",
            }
        ],
        question_context="How many people live in Cairo?",
    )

    audit = ledger["segments"][0]["sources"][0]["metadata_audit"]
    assert audit["population_scope_required"] is True
    assert "data_reference_period_for_population_claim" in audit["required_fields_missing"]
    assert "geographic_scope_for_population_claim" in audit["required_fields_missing"]
    assert ledger["fact_correctness"] == "not_checked"
