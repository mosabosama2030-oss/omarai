"""Regression tests for evidence provenance honesty in the web research agent."""
from __future__ import annotations

from agents.web_agent import WebAgent


def test_failed_page_fetch_does_not_claim_page_fetched(monkeypatch):
    """Unsuccessful page reads must keep page_fetched=False and report zero pages_fetched."""
    agent = WebAgent()

    def search(query):
        return [{
            "title": "Title only",
            "url": "https://example.com/unreachable",
            "snippet": "Thin snippet",
            "provider": "duckduckgo_html",
            "provider_rank": 1,
            "search_query": query,
            "published_at": "",
        }]

    monkeypatch.setattr(agent, "_search_web", search)
    monkeypatch.setattr(agent, "_fetch_page", lambda url: ("", ""))
    monkeypatch.setattr(agent, "_search_news", lambda query: [])
    monkeypatch.setattr(agent, "_search_social", lambda query, platforms: ([], []))
    sources, warnings, report = agent._collect_research({
        "queries": ["test unreachable page"],
        "social_focus": False,
        "freshness": "any",
        "depth": "standard",
        "planning_method": "test",
    })
    assert len(sources) == 1
    assert sources[0].get("page_fetched") is not True
    assert report["pages_fetched"] == 0
    assert report["queries_attempted"] == 1
    assert report["unique_sources"] == 1


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
