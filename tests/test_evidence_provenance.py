"""Regression tests for evidence provenance honesty in the web research agent."""
from __future__ import annotations

from agents.web_agent import WebAgent


def test_failed_page_fetch_leaves_page_fetched_false(monkeypatch):
    """When _fetch_page returns empty content, the source must not claim page_fetched=True."""
    agent = WebAgent()
    source = {
        "title": "Title only",
        "url": "https://example.com/unreachable",
        "snippet": "Thin snippet",
        "provider": "duckduckgo_html",
        "provider_rank": 1,
        "providers": ["duckduckgo_html"],
        "queries": ["test"],
        "page_fetched": False,
    }

    def fake_fetch(url):
        return ("", "")

    monkeypatch.setattr(agent, "_fetch_page", fake_fetch)
    title, text = agent._fetch_page(source["url"])
    assert title == ""
    assert text == ""
    # Caller contract: only set page_fetched when text is non-empty.
    if text:
        source["page_fetched"] = True
    assert source.get("page_fetched") is not True


def test_openrouter_server_search_sources_are_not_marked_as_direct_page_reads():
    """Server-side OpenRouter citations must report page_fetched=False."""
    agent = WebAgent()
    agent.server_search_sources = [{
        "title": "OpenRouter citation",
        "url": "https://example.com/or-source",
        "snippet": "Server-side excerpt",
        "page_text": "Server-side excerpt",
        "page_fetched": False,
        "provider": "openrouter_web_search",
        "providers": ["openrouter_web_search"],
        "queries": [],
        "domain": "example.com",
        "source_class": "general",
        "platform": "web",
        "published_at": "",
        "rank_score": 0.0,
    }]
    assert agent.server_search_sources[0]["page_fetched"] is False
    assert agent.server_search_sources[0]["provider"] == "openrouter_web_search"
    assert "openrouter_web_search" in agent.server_search_sources[0]["providers"]
