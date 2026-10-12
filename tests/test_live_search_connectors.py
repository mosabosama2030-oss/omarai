from __future__ import annotations

import httpx

from agents.web_agent import WebAgent


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload
        self.status_code = 200

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload


def test_brave_search_adapter_normalizes_real_api_response(monkeypatch):
    monkeypatch.setenv("BRAVE_SEARCH_API_KEY", "unit-test-secret")
    requested = {}

    def fake_get(url, **kwargs):
        requested["url"] = url
        requested.update(kwargs)
        return FakeResponse({
            "web": {
                "results": [{
                    "title": "Current research",
                    "url": "https://example.org/research",
                    "description": "A substantive search result.",
                    "page_age": "October 10, 2026",
                }]
            }
        })

    monkeypatch.setattr(httpx, "get", fake_get)
    rows = WebAgent()._search_brave("بحث حديث")
    assert requested["url"] == "https://api.search.brave.com/res/v1/web/search"
    assert requested["headers"]["X-Subscription-Token"] == "unit-test-secret"
    assert requested["params"]["country"] == "EG"
    assert rows[0]["provider"] == "brave_search_api"
    assert rows[0]["published_at"] == "October 10, 2026"
    assert "unit-test-secret" not in str(rows)


def test_tavily_search_adapter_normalizes_live_search_results(monkeypatch):
    monkeypatch.setenv("TAVILY_API_KEY", "unit-test-tavily-secret")
    requested = {}

    def fake_post(url, **kwargs):
        requested["url"] = url
        requested.update(kwargs)
        return FakeResponse({
            "results": [{
                "title": "Official report",
                "url": "https://example.org/report",
                "content": "A source excerpt from the search response.",
                "published_date": "2026-10-11",
            }]
        })

    monkeypatch.setattr(httpx, "post", fake_post)
    rows = WebAgent()._search_tavily("official sources report")
    assert requested["url"] == "https://api.tavily.com/search"
    assert requested["json"]["api_key"] == "unit-test-tavily-secret"
    assert requested["json"]["include_answer"] is False
    assert rows[0]["provider"] == "tavily_search_api"
    assert rows[0]["snippet"].startswith("A source excerpt")
    assert "unit-test-tavily-secret" not in str(rows)


def test_search_api_setup_status_reports_only_presence_not_secret_values(monkeypatch):
    monkeypatch.setenv("BRAVE_SEARCH_API_KEY", "brave-secret")
    monkeypatch.setenv("TAVILY_API_KEY", "tavily-secret")
    status = WebAgent.status()
    assert status["brave_search_api_configured"] is True
    assert status["tavily_search_api_configured"] is True
    assert "brave-secret" not in str(status)
    assert "tavily-secret" not in str(status)
