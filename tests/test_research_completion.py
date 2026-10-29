"""Tests for truthful research completion states and counter reconciliation."""
from __future__ import annotations

from agents.research_completion import build_research_completion


def test_non_research_answer_is_not_reported_as_web_research_complete() -> None:
    result = build_research_completion({"kind": "local_conversation", "answer": "مرحبا"})
    assert result["status"] == "not_applicable"
    assert result["semantic_verification"] == "not_performed"


def test_empty_results_distinguish_zero_results_from_tool_failure() -> None:
    no_results = build_research_completion({
        "kind": "insufficient_evidence",
        "search_attempted": True,
        "sources": [],
        "search_report": {
            "search_attempted": True,
            "query_results": [{"query": "topic", "results": 0}],
            "queries_attempted": 1,
            "queries_planned": 1,
        },
    })
    failure = build_research_completion({
        "kind": "web_fallback",
        "search_attempted": True,
        "sources": [],
        "search_report": {
            "search_attempted": True,
            "search_outcome": "attempted_research_error",
            "provider_diagnostics": [{"provider": "test", "status": "timeout"}],
        },
    })
    assert no_results["status"] == "no_results_returned"
    assert no_results["phases"]["search"] == "completed_no_results"
    assert failure["status"] == "search_failed_or_incomplete"
    assert failure["counters"]["connector_failure_count"] == 1


def test_all_rejected_sources_are_not_mislabeled_as_no_results() -> None:
    result = build_research_completion({
        "kind": "insufficient_evidence",
        "search_attempted": True,
        "sources": [],
        "search_report": {
            "search_attempted": True,
            "source_guardrails": {
                "final": {"rejection_counts": {"stale": 2, "date_unavailable": 1}},
            },
        },
    })
    assert result["status"] == "no_eligible_sources_after_filtering"
    assert result["counters"]["guardrail_rejected_candidate_count"] == 3


def test_snippet_only_results_do_not_claim_pages_were_read() -> None:
    result = build_research_completion({
        "kind": "web_fallback",
        "search_attempted": True,
        "used_language_model": False,
        "sources": [
            {"url": "https://example.com/a", "snippet": "Search snippet", "page_fetched": False}
        ],
        "search_report": {"unique_sources": 1, "pages_fetched": 0},
    })
    assert result["status"] == "source_snippets_only_generation_not_completed"
    assert result["phases"]["page_reading"] == "no_final_source_page_read"
    assert result["counters"]["pages_read_with_text_count"] == 0


def test_answer_with_valid_citation_indices_still_discloses_semantic_gap() -> None:
    result = build_research_completion({
        "kind": "web_research",
        "search_attempted": True,
        "used_language_model": True,
        "final_answer_status": "model_answer_generated",
        "citation_validation": {"status": "index_range_check_passed", "valid_citation_count": 2},
        "sources": [
            {"url": "https://example.com/a", "snippet": "text", "page_fetched": True, "page_text": "read"}
        ],
        "search_report": {
            "unique_sources": 1, "pages_fetched": 1,
            "query_results": [{"query": "topic", "results": 1}],
        },
    })
    assert result["status"] == "answer_generated_citations_range_checked_semantic_support_unverified"
    assert result["phases"]["semantic_verification"] == "not_performed"
    assert result["semantic_verification"] == "not_performed"


def test_normalized_url_counters_and_mismatched_legacy_counters_are_exposed() -> None:
    result = build_research_completion({
        "kind": "web_fallback",
        "search_attempted": True,
        "sources": [
            {"url": "https://example.com/path?utm_source=abc", "snippet": "a"},
            {"url": "https://example.com/path#section", "snippet": "b"},
        ],
        "search_report": {"unique_sources": 5, "pages_fetched": 4},
    })
    assert result["counters"]["final_source_list_count"] == 2
    assert result["counters"]["unique_normalized_url_count"] == 1
    assert result["counters"]["duplicate_normalized_url_count"] == 1
    assert result["counter_consistency"]["status"] == "mismatch_detected"
    assert len(result["counter_consistency"]["issues"]) == 2


def test_counter_consistency_is_not_claimed_when_legacy_counters_are_missing() -> None:
    result = build_research_completion({
        "kind": "web_fallback", "search_attempted": True, "sources": [],
        "search_report": {"query_results": []},
    })
    assert result["counter_consistency"]["status"] == "not_computable"



def test_public_readability_marker_counts_read_page_without_exposing_text() -> None:
    result = build_research_completion({
        "kind": "web_research",
        "used_language_model": True,
        "final_answer_status": "model_answer_generated",
        "sources": [{
            "url": "https://example.com/a",
            "snippet": "summary",
            "page_fetched": True,
            "readable_page_text_available": True,
        }],
        "search_report": {"unique_sources": 1, "pages_fetched": 1},
    })
    assert result["counters"]["pages_read_with_text_count"] == 1
    assert result["phases"]["page_reading"] == "all_final_sources_read"


def test_ref_query_parameters_are_not_assumed_to_be_tracking_ids() -> None:
    result = build_research_completion({
        "kind": "web_fallback",
        "sources": [
            {"url": "https://example.com/post?ref=one"},
            {"url": "https://example.com/post?ref=two"},
        ],
        "search_report": {},
    })
    assert result["counters"]["unique_normalized_url_count"] == 2
    assert result["counters"]["duplicate_normalized_url_count"] == 0



def test_unflagged_page_text_marker_is_counted_without_exposing_page_text() -> None:
    result = build_research_completion({
        "kind": "web_fallback",
        "sources": [{
            "url": "https://example.com/a",
            "snippet": "summary",
            "page_fetched": False,
            "page_text_present_without_fetch_flag": True,
        }],
        "search_report": {},
    })
    assert result["counters"]["page_text_without_fetched_flag_count"] == 1
