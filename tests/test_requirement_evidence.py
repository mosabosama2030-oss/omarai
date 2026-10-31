"""Focused contract tests for the dedicated requirement-evidence module."""
from __future__ import annotations

from agents.answer_validation import build_requirement_evidence_ledger as legacy_builder
from agents.requirement_evidence import build_requirement_evidence_ledger
from agents.text_normalization import normalize_text, tokenize_text


def test_legacy_import_path_reexports_the_dedicated_builder() -> None:
    assert legacy_builder is build_requirement_evidence_ledger


def test_shared_normalizer_handles_arabic_diacritics_and_digits() -> None:
    assert normalize_text("أَهْلًا ١٢٣") == "اهلا 123"
    assert tokenize_text("The phone السعر ١٢", drop_stopwords=True) == ["phone", "السعر", "12"]


def test_requirement_ledger_links_query_provenance_and_lexical_candidates() -> None:
    targets = ["السعر", "البطارية"]
    queries = [
        {"target": "السعر", "query": "سعر الهاتف"},
        {"target": "البطارية", "query": "بطارية الهاتف"},
    ]
    sources = [
        {
            "title": "Phone price guide",
            "snippet": "The price and cost are listed for the phone.",
            "page_fetched": False,
            "queries": ["سعر الهاتف"],
        },
    ]

    ledger = build_requirement_evidence_ledger(targets, sources, queries)
    by_target = {item["target"]: item for item in ledger}

    price = by_target["السعر"]
    assert price["status"] == "candidate_evidence_found_not_verified"
    assert price["query_result_source_indexes"] == [1]
    assert price["candidate_source_indexes"] == [1]
    assert price["candidate_sources"][0]["evidence_basis"] == "search_snippet"
    assert price["semantic_verification"] is False
    assert price["source_entailment_verified"] is False

    battery = by_target["البطارية"]
    assert battery["status"] == "no_candidate_evidence_found"
    assert battery["candidate_source_indexes"] == []
    assert battery["semantic_verification"] is False


def test_title_only_match_remains_a_candidate_not_verified_evidence() -> None:
    ledger = build_requirement_evidence_ledger(
        ["battery"],
        [{"title": "Battery overview", "page_fetched": False}],
    )

    assert ledger[0]["status"] == "candidate_evidence_found_not_verified"
    assert ledger[0]["candidate_sources"][0]["evidence_basis"] == "title_only"
    assert ledger[0]["semantic_verification"] is False
    assert ledger[0]["source_entailment_verified"] is False
