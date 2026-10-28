from __future__ import annotations

from agents.claim_evidence import build_claim_evidence_ledger
from agents.web_agent import WebAgent


def test_claim_ledger_maps_citations_to_exact_sources() -> None:
    sources = [
        {"title": "Price source", "url": "https://example.com/price",
         "snippet": "Solar battery price is 100 EGP.", "provider": "fixture"},
        {"title": "Warranty source", "url": "https://example.org/warranty",
         "page_text": "Warranty terms are listed here.", "page_fetched": True,
         "provider": "fixture"},
    ]
    result = build_claim_evidence_ledger(
        "The price is 100 EGP [source 1]. Warranty terms are shown [المصدر 2].",
        sources,
        {"citation_lexical_alignment": [
            {"sentence_number": 1, "status": "lexical_overlap_signal_found"},
            {"sentence_number": 2, "status": "weak_lexical_overlap"},
        ]},
    )
    assert result["semantic_verification"] is False
    assert result["claim_entailment"] == "not_checked"
    assert result["summary"]["segment_candidate_count"] == 2
    assert result["summary"]["valid_source_reference_count"] == 2
    assert result["segments"][0]["sources"][0]["url"] == "https://example.com/price"
    assert result["segments"][1]["sources"][0]["evidence_basis"] == "extracted_page_text"
    assert result["segments"][0]["lexical_audit_status"] == "lexical_overlap_signal_found"


def test_claim_ledger_marks_uncited_and_out_of_range_references() -> None:
    result = build_claim_evidence_ledger(
        "Uncited sentence. Bad reference [المصدر 2]. Valid [source 1].",
        [{"title": "Source", "url": "https://example.com", "snippet": "text"}],
    )
    assert result["summary"]["segments_without_citation_markers"] == 1
    assert result["summary"]["out_of_range_reference_count"] == 1
    assert result["segments"][0]["citation_status"] == "no_citation_marker"
    assert result["segments"][1]["citation_status"] == "citation_index_out_of_range"
    assert result["segments"][2]["citation_status"] == "cited_source_attached"


def test_claim_ledger_does_not_equate_valid_index_with_verification() -> None:
    result = build_claim_evidence_ledger(
        "Claim with a marker [المصدر 1].",
        [{"title": "Only a title", "url": "https://example.com"}],
    )
    assert result["segments"][0]["citation_status"] == "valid_index_without_readable_evidence"
    assert result["summary"]["cited_segments_with_readable_source_evidence"] == 0
    assert result["fact_correctness"] == "not_checked"
    assert any("do not prove" in item for item in result["limitations"])


def test_collect_research_retries_missing_aspect_within_query_limit(monkeypatch) -> None:
    agent = WebAgent()
    agent._request_budget = None
    queries: list[str] = []

    def fake_search(query: str):
        queries.append(query)
        if "warranty" in query.casefold():
            return [{
                "title": "Solar battery warranty terms",
                "url": "https://example.org/warranty",
                "snippet": "Solar battery warranty terms and coverage.",
                "provider": "fixture_search",
                "provider_rank": 1,
            }]
        return [{
            "title": "Solar battery price details",
            "url": "https://example.com/price",
            "snippet": "Solar battery price: 100 EGP.",
            "provider": "fixture_search",
            "provider_rank": 1,
        }]

    monkeypatch.setattr(agent, "_search_web", fake_search)
    monkeypatch.setattr(
        agent, "_fetch_page",
        lambda _url: ("Fixture page", "Solar battery price and warranty evidence text."),
    )
    sources, _warnings, report = agent._collect_research({
        "query_limit": 3,
        "queries": ["solar battery", "solar battery price", "solar battery warranty"],
        "coverage_targets": ["price", "warranty"],
        "depth": "standard",
        "social_focus": False,
        "platforms": [],
        "direct_urls": [],
    })
    assert len(queries) <= 3
    assert any("warranty" in query.casefold() for query in queries)
    assert report["queries_attempted"] == len(queries)
    assert any("warranty" in str(source.get("title", "")).casefold() for source in sources)
