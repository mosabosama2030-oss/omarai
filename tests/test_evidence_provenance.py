"""Regression tests for evidence provenance and pinned public-page retrieval."""
from __future__ import annotations

import socket

import pytest

from agents.web_agent import WebAgent, _public_ip_literals


def _addrinfo(ip: str):
    family = socket.AF_INET6 if ":" in ip else socket.AF_INET
    return [(family, socket.SOCK_STREAM, 6, "", (ip, 0))]


def test_failed_page_read_is_not_reported_as_fetched(monkeypatch):
    """An empty extraction must not set page_fetched through the real collector."""
    agent = WebAgent()

    def search(query):
        return [{
            "title": "عنوان فقط",
            "url": "https://example.com/unread",
            "snippet": "مقتطف محرك بحث",
            "provider": "duckduckgo_html",
            "provider_rank": 1,
            "search_query": query,
            "published_at": "",
        }]

    monkeypatch.setattr(agent, "_search_web", search)
    monkeypatch.setattr(agent, "_search_news", lambda query: [])
    monkeypatch.setattr(agent, "_search_social", lambda query, platforms: ([], []))
    monkeypatch.setattr(agent, "_fetch_page", lambda url: ("", ""))

    sources, warnings, report = agent._collect_research({
        "queries": ["سؤال دون قراءة صفحة"],
        "direct_urls": [],
        "social_focus": False,
        "freshness": "any",
        "depth": "standard",
        "platforms": [],
        "planning_method": "test",
    })

    assert warnings == []
    assert len(sources) == 1
    assert sources[0]["url"] == "https://example.com/unread"
    assert sources[0].get("page_fetched") is not True
    assert report["pages_fetched"] == 0
    assert report["queries_attempted"] == 1
    assert report["unique_sources"] == 1


def test_openrouter_citations_stay_unread_in_public_answer(monkeypatch):
    """Server-side citations merged into the answer must not claim a direct page read."""
    agent = WebAgent()
    agent.api_key = "test-key"

    def collect(plan):
        return [], [], {
            "queries_planned": 1,
            "queries_attempted": 1,
            "query_results": [],
            "unique_sources": 0,
            "pages_fetched": 0,
            "providers_used": [],
            "provider_counts": {},
            "platform_counts": {},
            "social_direct_results": 0,
            "expansion_queries": [],
            "evidence_signals": {},
            "depth": "standard",
            "planning_method": "test",
        }

    def generate(*args, **kwargs):
        agent.server_search_sources.append({
            "title": "اقتباس مزود",
            "url": "https://example.com/or-source",
            "snippet": "مقتطف أعاده المزود",
            "page_text": "مقتطف أعاده المزود",
            "page_fetched": False,
            "provider": "openrouter_web_search",
            "providers": ["openrouter_web_search"],
            "queries": [],
            "domain": "example.com",
            "source_class": "general",
            "platform": "web",
            "published_at": "",
            "rank_score": 0.0,
        })
        return "الخلاصة من الاقتباس [المصدر 1]."

    monkeypatch.setattr(agent, "_plan_search", lambda question, history: {
        "queries": [question],
        "direct_urls": [],
        "social_focus": False,
        "freshness": "any",
        "depth": "standard",
        "platforms": [],
        "planning_method": "test",
    })
    monkeypatch.setattr(agent, "_collect_research", collect)
    monkeypatch.setattr(agent, "_generate", generate)
    monkeypatch.setattr(agent, "_review_answer", lambda *args, **kwargs: pytest.fail("review"))

    result = agent.answer("ما آخر المعلومات؟", history=[], mode="auto")
    source = result["sources"][0]
    assert source["url"] == "https://example.com/or-source"
    assert source["page_fetched"] is False
    assert "openrouter_web_search" in source["providers"]
    assert result["search_report"]["pages_fetched"] == 0
    assert result["search_report"]["openrouter_web_search_results"] == 1


def test_private_resolution_blocks_page_fetch(monkeypatch):
    called = {"stream": 0}

    def fake_getaddrinfo(host, port, *args, **kwargs):
        return _addrinfo("127.0.0.1")

    class FakeClient:
        def __init__(self, *args, **kwargs):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def stream(self, *args, **kwargs):
            called["stream"] += 1
            raise AssertionError("private destinations must not be connected")

    monkeypatch.setattr(socket, "getaddrinfo", fake_getaddrinfo)
    monkeypatch.setattr("httpx.Client", FakeClient)
    assert _public_ip_literals("example.com") is None
    assert WebAgent()._fetch_page("https://example.com/secret") == ("", "")
    assert called["stream"] == 0


def test_page_fetch_connects_to_the_validated_public_ip(monkeypatch):
    seen = {}

    def fake_getaddrinfo(host, port, *args, **kwargs):
        assert host == "example.com"
        return _addrinfo("1.1.1.1")

    class FakeResponse:
        status_code = 200
        encoding = "utf-8"

        def __init__(self):
            self.headers = {"content-type": "text/plain; charset=utf-8"}

        def iter_bytes(self):
            yield "نص عام".encode()

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

    class FakeClient:
        def __init__(self, *args, **kwargs):
            assert kwargs.get("verify") is True
            assert kwargs.get("follow_redirects") is False

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def stream(self, method, url, headers=None, extensions=None):
            seen["method"] = method
            seen["url"] = url
            seen["headers"] = headers
            seen["extensions"] = extensions
            return FakeResponse()

    monkeypatch.setattr(socket, "getaddrinfo", fake_getaddrinfo)
    monkeypatch.setattr("httpx.Client", FakeClient)
    title, text = WebAgent()._fetch_page("https://example.com/article")
    assert title == ""
    assert "نص عام" in text
    assert seen["url"].startswith("https://1.1.1.1/")
    assert seen["headers"]["Host"] == "example.com"
    assert seen["extensions"]["sni_hostname"] == "example.com"
