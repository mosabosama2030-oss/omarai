from __future__ import annotations

import json

from agents.web_agent import WebAgent


def test_connector_summary_reports_request_scope_worst_state_and_redacts_secrets(monkeypatch):
    agent = WebAgent()
    monkeypatch.delenv("BRAVE_SEARCH_API_KEY", raising=False)
    diagnostics = [
        {
            "provider": "duckduckgo_html",
            "query": "renewable energy",
            "status": "ok",
            "result_count": 3,
            "rejected_count": 1,
        },
        {
            "provider": "duckduckgo_html",
            "query": "renewable energy",
            "status": "failed",
            "result_count": 0,
            "rejected_count": 0,
            "error": "HTTP 500 token=secret-value",
        },
    ]
    sources = [
        {"url": "https://example.com/a", "providers": ["duckduckgo_html"]},
        {"url": "https://example.org/b", "providers": ["bing_rss"]},
    ]

    summary = agent._connector_status_summary(diagnostics, sources)

    duckduckgo = next(item for item in summary["connectors"] if item["name"] == "duckduckgo_html")
    brave = next(item for item in summary["connectors"] if item["name"] == "brave_search_api")
    assert summary["scope"] == "this_request_only"
    assert duckduckgo["attempted"] is True
    assert duckduckgo["status"] == "failed"
    assert duckduckgo["observed_statuses"] == ["ok", "failed"]
    assert duckduckgo["result_count"] == 3
    assert duckduckgo["useful_result_count"] == 1
    assert duckduckgo["rejected_count"] == 1
    assert "secret-value" not in json.dumps(summary)
    assert brave["configured"] is False
    assert brave["status"] == "not_configured"


def test_collect_research_distinguishes_raw_rows_unique_urls_and_page_extraction(monkeypatch):
    agent = WebAgent()
    query = "renewable energy storage"
    results = [
        {
            "title": "Renewable energy storage report",
            "url": "https://example.com/report",
            "snippet": "Renewable energy storage data from the report",
            "page_text": "",
            "page_fetched": False,
            "provider": "test_search",
            "provider_rank": 1,
            "search_query": query,
            "published_at": "",
        },
        {
            "title": "Renewable energy storage report (duplicate URL)",
            "url": "https://example.com/report?utm_source=test",
            "snippet": "Renewable energy storage data from a duplicate result",
            "page_text": "",
            "page_fetched": False,
            "provider": "test_search",
            "provider_rank": 2,
            "search_query": query,
            "published_at": "",
        },
        {
            "title": "Renewable energy storage statistics",
            "url": "https://example.org/statistics",
            "snippet": "Renewable energy storage statistics",
            "page_text": "",
            "page_fetched": False,
            "provider": "test_search",
            "provider_rank": 3,
            "search_query": query,
            "published_at": "",
        },
    ]

    monkeypatch.setattr(agent, "_search_web", lambda _query: results)
    def fetch(url: str):
        if "example.com" in url:
            return "Report page", "Renewable energy storage page body with extracted text."
        return "", ""

    monkeypatch.setattr(agent, "_fetch_page", fetch)
    sources, warnings, report = agent._collect_research({
        "queries": [query],
        "direct_urls": [],
        "social_focus": False,
        "freshness": "any",
        "depth": "standard",
        "platforms": [],
        "planning_method": "unit_test",
    })

    assert warnings
    assert report["raw_results"] == 3
    assert report["unique_urls"] == 2
    assert report["unique_sources"] == 2
    assert report["pages_fetch_attempted"] == 2
    assert report["pages_content_extracted"] == 1
    assert report["pages_extract_failed"] == 1
    assert report["page_fetch_status_counts"] == {
        "content_extracted": 1,
        "no_text_extracted": 1,
        "fetch_failed": 0,
    }
    assert sum(source["page_fetch_status"] == "content_extracted" for source in sources) == 1
    assert sum(source["page_fetch_status"] == "no_text_extracted" for source in sources) == 1
    assert report["connector_summary"]["scope"] == "this_request_only"


def test_connector_summary_does_not_claim_timeout_or_budget_exhaustion_was_a_confirmed_attempt(monkeypatch):
    agent = WebAgent()
    monkeypatch.setenv("TAVILY_API_KEY", "configured-test-key")
    timeout = agent._connector_status_summary(
        [{"provider": "tavily_search_api", "query": "query", "status": "timeout", "error": "request timed out"}],
        [],
    )
    exhausted = agent._connector_status_summary(
        [{"provider": "deepseek_search_api", "query": "query", "status": "budget_exhausted"}],
        [],
    )
    tavily = next(item for item in timeout["connectors"] if item["name"] == "tavily_search_api")
    deepseek = next(item for item in exhausted["connectors"] if item["name"] == "deepseek_search_api")
    assert tavily["configured"] is True
    assert tavily["attempted"] is None
    assert tavily["status"] == "timeout"
    assert deepseek["configured"] is False
    assert deepseek["attempted"] is False
    assert deepseek["status"] == "budget_exhausted"
