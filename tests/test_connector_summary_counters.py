"""Unit tests for per-request connector summary and split research counters."""

from __future__ import annotations

from agents.web_agent import WebAgent


def test_summarize_connector_distinguishes_configured_attempted_and_empty():
    diagnostics = [
        {
            "provider": "duckduckgo_html",
            "query": "شقق التجمع الخامس",
            "status": "ok",
            "result_count": 5,
            "rejected_count": 1,
        },
        {
            "provider": "bing_rss",
            "query": "شقق التجمع الخامس",
            "status": "no_results",
            "result_count": 0,
            "rejected_count": 0,
        },
        {
            "provider": "brave_search_api",
            "query": "شقق التجمع الخامس",
            "status": "not_configured",
            "result_count": 0,
        },
    ]
    summary = {
        row["name"]: row for row in WebAgent._summarize_connector_diagnostics(diagnostics)
    }
    assert summary["duckduckgo_html"]["attempted"] is True
    assert summary["duckduckgo_html"]["status"] == "returned_results"
    assert summary["duckduckgo_html"]["result_count"] == 5
    assert summary["bing_rss"]["attempted"] is True
    assert summary["bing_rss"]["status"] == "empty_or_filtered"
    assert summary["brave_search_api"]["attempted"] is False
    assert summary["brave_search_api"]["status"] == "not_configured"
    # Planned-but-not-executed is not implied by catalog-only rows without diagnostics.
    assert summary["tavily_search_api"]["status"] in {"not_configured", "not_attempted"}


def test_summarize_connector_failure_does_not_claim_results():
    diagnostics = [
        {
            "provider": "duckduckgo_html",
            "query": "x",
            "status": "failed",
            "result_count": 0,
            "error": "timeout",
        },
        {
            "provider": "bing_rss",
            "query": "x",
            "status": "ok",
            "result_count": 2,
        },
    ]
    summary = {
        row["name"]: row for row in WebAgent._summarize_connector_diagnostics(diagnostics)
    }
    assert summary["duckduckgo_html"]["status"] == "failed"
    assert summary["duckduckgo_html"]["result_count"] == 0
    assert summary["bing_rss"]["status"] == "returned_results"
    assert summary["bing_rss"]["result_count"] == 2


def test_enrich_search_report_splits_raw_unique_and_page_counters():
    sources = [
        {
            "url": "https://a.example/listing-1",
            "domain": "a.example",
            "page_fetched": True,
            "page_fetch_attempted": True,
            "page_text": "unit text",
            "content_extraction_status": "extracted",
        },
        {
            "url": "https://b.example/listing-2",
            "domain": "b.example",
            "page_fetched": False,
            "page_fetch_attempted": True,
            "content_extraction_status": "dynamic_or_unreadable",
        },
        {
            "url": "https://c.example/listing-3",
            "domain": "c.example",
            "page_fetched": False,
            "page_fetch_attempted": False,
            "content_extraction_status": "search_snippet_only",
            "snippet": "snippet only",
        },
    ]
    diagnostics = [
        {"provider": "duckduckgo_html", "status": "ok", "result_count": 4},
        {"provider": "bing_rss", "status": "ok", "result_count": 3},
    ]
    report: dict = {}
    WebAgent._enrich_search_report_counters(report, sources, diagnostics)
    assert report["raw_search_hits"] == 7
    assert report["unique_urls"] == 3
    assert report["unique_domains"] == 3
    assert report["pages_fetch_attempted"] == 2
    assert report["pages_content_extracted"] == 1
    assert report["pages_extraction_failed"] == 1
    assert report["pages_fetched"] == 1  # legacy alias for extracted only
    assert any(row["name"] == "duckduckgo_html" for row in report["connector_summary"])
    assert report["counter_semantics"]["pages_fetched"] == (
        "legacy_alias_for_pages_content_extracted"
    )


def test_enrich_does_not_treat_snippet_only_as_page_read():
    sources = [
        {
            "url": "https://news.example/story",
            "domain": "news.example",
            "page_fetched": False,
            "snippet": "A search engine snippet is not a page read.",
            "content_extraction_status": "search_snippet_only",
        }
    ]
    report: dict = {}
    WebAgent._enrich_search_report_counters(report, sources, [])
    assert report["pages_content_extracted"] == 0
    assert report["pages_fetched"] == 0
