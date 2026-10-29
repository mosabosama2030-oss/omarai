from agents.claim_evidence import audit_source_metadata, build_claim_evidence_ledger


def test_source_metadata_audit_accepts_complete_population_source_metadata():
    result = audit_source_metadata(
        {
            "url": "https://example.org/census",
            "title": "Population table",
            "publisher": "Example Statistics Office",
            "published_at": "2025-06-01",
            "geographic_scope": "Cairo Governorate administrative boundaries",
        },
        claim_text="عدد سكان محافظة القاهرة",
    )

    assert result["status"] == "metadata_complete"
    assert result["required_fields_missing"] == []
    assert result["claim_entailment"] == "not_checked"
    assert result["fact_correctness"] == "not_checked"


def test_source_metadata_audit_flags_missing_date_and_population_scope():
    result = audit_source_metadata(
        {
            "url": "https://example.org/census",
            "title": "Population table",
            "publisher": "Example Statistics Office",
        },
        claim_text="عدد سكان القاهرة الكبرى",
    )

    assert result["status"] == "metadata_incomplete"
    assert "publication_or_data_date" in result["required_fields_missing"]
    assert "geographic_scope_for_population_claim" in result["required_fields_missing"]


def test_source_metadata_audit_rejects_non_http_or_missing_url():
    result = audit_source_metadata(
        {
            "url": "javascript:alert(1)",
            "title": "A title",
            "publisher": "A publisher",
            "published_at": "2025",
        }
    )

    assert result["valid_http_url"] is False
    assert "valid_http_source_url" in result["required_fields_missing"]


def test_claim_evidence_ledger_exposes_metadata_audit_without_claiming_truth():
    ledger = build_claim_evidence_ledger(
        "عدد سكان القاهرة الكبرى [المصدر 1]",
        [
            {
                "url": "https://example.org/population",
                "title": "Population page",
                "snippet": "Population estimates",
                "publisher": "Example Publisher",
            }
        ],
    )

    ref = ledger["segments"][0]["sources"][0]
    assert ref["metadata_audit"]["status"] == "metadata_incomplete"
    assert ref["metadata_audit"]["claim_entailment"] == "not_checked"
    assert ledger["fact_correctness"] == "not_checked"
