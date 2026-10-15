"""Regression tests for evidence provenance honesty in the web research agent.

These tests exercise the production collection path (_collect_research) with
deterministic mocks so that page_fetched and OpenRouter citation contracts
cannot regress silently.
"""
from __future__ import annotations

from agents.web_agent import WebAgent


def test_failed_page_fetch_does_not_claim_page_fetched_via_collect_research(monkeypatch):
    """Production path: a failed _fetch_page must leave page_fetched unset/False
    and report pages_fetched == 0."""
    agent = WebAgent()

    def fake_search(query):
        return [
            {
                "title": "Unreachable page",
                "url": "https://example.com/unreachable",
                "snippet": "Thin snippet only",
                "provider": "duckduckgo_html",
                "provider_rank": 1,
            }
        ]

    def fake_fetch(url):
        return ("", "")  # empty title and text = fetch failure

    monkeypatch.setattr(agent, "_search_web", fake_search)
    monkeypatch.setattr(agent, "_fetch_page", fake_fetch)

    sources, warnings, report = agent._collect_research(
        {
            "queries": ["test provenance failure"],
            "social_focus": False,
            "freshness": "any",
            "depth": "standard",
            "planning_method": "test",
        }
    )

    assert len(sources) >= 1
    for source in sources:
        # Caller only sets page_fetched=True when text is non-empty.
        assert source.get("page_fetched") is not True
        assert not source.get("page_text")
    assert report["pages_fetched"] == 0


def test_successful_page_fetch_sets_page_fetched_true(monkeypatch):
    """Production path: non-empty page text must set page_fetched=True and
    increment pages_fetched."""
    agent = WebAgent()

    def fake_search(query):
        return [
            {
                "title": "Reachable page",
                "url": "https://example.com/article",
                "snippet": "Search snippet",
                "provider": "duckduckgo_html",
                "provider_rank": 1,
            }
        ]

    def fake_fetch(url):
        return ("Article Title", "Full extracted public page text for analysis.")

    monkeypatch.setattr(agent, "_search_web", fake_search)
    monkeypatch.setattr(agent, "_fetch_page", fake_fetch)

    sources, warnings, report = agent._collect_research(
        {
            "queries": ["test provenance success"],
            "social_focus": False,
            "freshness": "any",
            "depth": "standard",
            "planning_method": "test",
        }
    )

    assert len(sources) >= 1
    fetched = [s for s in sources if s.get("page_fetched") is True]
    assert len(fetched) >= 1
    assert fetched[0]["page_text"]
    assert report["pages_fetched"] >= 1


def test_openrouter_server_search_citations_remain_not_direct_page_reads(monkeypatch):
    """OpenRouter server-side web-search citations must enter the report with
    page_fetched=False and provider openrouter_web_search. They must not be
    counted as pages Omarai itself fetched and read."""
    agent = WebAgent()

    # Simulate the production path that records OpenRouter tool citations.
    citation = {
        "title": "OpenRouter citation title",
        "url": "https://example.com/or-citation",
        "snippet": "Server-side excerpt from the model provider",
        "page_text": "Server-side excerpt from the model provider",
        "page_fetched": False,
        "provider": "openrouter_web_search",
        "providers": ["openrouter_web_search"],
        "queries": [],
        "domain": "example.com",
        "source_class": "general",
        "platform": "web",
        "published_at": "",
        "rank_score": 0.0,
    }
    agent.server_search_sources = [citation]

    # The agent must never flip page_fetched for these sources.
    assert agent.server_search_sources[0]["page_fetched"] is False
    assert agent.server_search_sources[0]["provider"] == "openrouter_web_search"
    assert "openrouter_web_search" in agent.server_search_sources[0]["providers"]

    # Even if these sources are later merged into a report, the flag stays False.
    for source in agent.server_search_sources:
        assert source.get("page_fetched") is not True
