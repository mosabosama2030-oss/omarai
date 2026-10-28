"""Integration regressions for budgeted academic fallback and compound facets."""
from __future__ import annotations

import pytest

import agents.web_agent as web_module
from agents.web_agent import WebAgent


def _academic_result(provider: str, query: str) -> dict:
    urls = {
        "openalex": "https://openalex.org/W123",
        "arxiv": "https://arxiv.org/abs/2401.00001",
        "crossref": "https://api.crossref.org/works/10.1000/example",
    }
    return {
        "title": "Peer reviewed research on lithium battery degradation",
        "url": urls[provider],
        "snippet": "Peer reviewed research on lithium battery degradation study.",
        "page_fetched": False,
        "provider": provider,
        "provider_rank": 1,
        "search_query": query,
        "published_at": "2025",
        "source_class": "academic",
    }


def test_sparse_academic_search_uses_budgeted_safe_connectors(monkeypatch) -> None:
    agent = WebAgent()
    agent._request_budget = None
    for key in ("DEEPSEEK_SEARCH_API_KEY", "BRAVE_SEARCH_API_KEY", "TAVILY_API_KEY"):
        monkeypatch.delenv(key, raising=False)
    monkeypatch.setattr(agent, "_search_duckduckgo_html", lambda _q: [])
    monkeypatch.setattr(agent, "_search_bing_rss", lambda _q: [])
    monkeypatch.setattr(web_module, "_public_http_url", lambda value: value)
    monkeypatch.setattr(web_module, "_blocked_source_url", lambda _value: False)
    monkeypatch.setattr(web_module, "_relevance_ratio", lambda _q, _text: 1.0)
    funcs = {"openalex": "search_openalex", "arxiv": "search_arxiv", "crossref": "search_crossref"}
    for provider, attr in funcs.items():
        monkeypatch.setattr(
            web_module, attr,
            lambda query, limit=3, p=provider: [_academic_result(p, query)],
        )
    results = agent._search_web("peer-reviewed research on lithium battery degradation")
    assert {"openalex", "arxiv", "crossref"} <= {row["provider"] for row in results}


def test_academic_connectors_are_not_called_for_ordinary_sparse_queries(monkeypatch) -> None:
    agent = WebAgent()
    agent._request_budget = None
    for key in ("DEEPSEEK_SEARCH_API_KEY", "BRAVE_SEARCH_API_KEY", "TAVILY_API_KEY"):
        monkeypatch.delenv(key, raising=False)
    monkeypatch.setattr(agent, "_search_duckduckgo_html", lambda _q: [{
        "title": "iPhone 17 price in Egypt",
        "url": "https://example.com/iphone-price",
        "snippet": "iPhone 17 price in Egypt.",
        "provider": "duckduckgo_html",
        "provider_rank": 1,
    }])
    monkeypatch.setattr(agent, "_search_bing_rss", lambda _q: [])
    monkeypatch.setattr(web_module, "_public_http_url", lambda value: value)
    monkeypatch.setattr(web_module, "_blocked_source_url", lambda _value: False)
    monkeypatch.setattr(web_module, "_relevance_ratio", lambda _q, _text: 1.0)

    def unexpected(*_args, **_kwargs):
        pytest.fail("Academic connectors must not run for ordinary product-price queries.")

    monkeypatch.setattr(web_module, "search_openalex", unexpected)
    monkeypatch.setattr(web_module, "search_arxiv", unexpected)
    monkeypatch.setattr(web_module, "search_crossref", unexpected)
    results = agent._search_web("iPhone 17 price in Egypt")
    assert len(results) == 1
    assert results[0]["provider"] == "duckduckgo_html"


def test_web_agent_extracts_joined_comparison_facets() -> None:
    targets = WebAgent._question_coverage_targets(
        "قارن بين الأنظمة: السعر والبطارية، بالإضافة إلى الضمان والصيانة "
        "والخصوصية والاعتمادية والدعم والجودة"
    )
    joined = " ".join(targets)
    for expected in ("السعر", "البطارية", "الضمان", "الصيانة", "الخصوصية", "الاعتمادية", "الدعم", "الجودة"):
        assert expected in joined
