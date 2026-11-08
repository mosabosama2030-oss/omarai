from __future__ import annotations

import pytest

from agents.web_agent import WebAgent


class FakeResponse:
    status_code = 200

    def __init__(self, payload):
        self._payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self._payload


def test_firecrawl_search_normalizes_only_safe_described_web_results(monkeypatch):
    monkeypatch.setenv("FIRECRAWL_API_KEY", "test-firecrawl-secret")
    captured = {}

    def fake_request(method, url, **kwargs):
        captured.update(method=method, url=url, kwargs=kwargs)
        return FakeResponse({
            "success": True,
            "data": {
                "web": [
                    {
                        "title": "طلب شراء معدات",
                        "url": "https://example.com/request",
                        "description": "نبحث عن مورد لتوريد المعدات المطلوبة",
                    },
                    {
                        "title": "وجهة محلية",
                        "url": "http://127.0.0.1/internal",
                        "description": "طلب شراء معدات",
                    },
                    {
                        "title": "وصف فارغ",
                        "url": "https://example.net/empty",
                        "description": "",
                    },
                ]
            },
        })

    monkeypatch.setattr("agents.web_agent._bounded_http_request", fake_request)
    result = WebAgent()._search_firecrawl("طلب شراء معدات")

    assert len(result) == 1
    assert result[0]["provider"] == "firecrawl_search_api"
    assert result[0]["url"] == "https://example.com/request"
    assert result[0]["snippet"] == "نبحث عن مورد لتوريد المعدات المطلوبة"
    assert captured["method"] == "POST"
    assert captured["url"] == "https://api.firecrawl.dev/v2/search"
    assert captured["kwargs"]["json"]["sources"] == [{"type": "web"}]
    assert captured["kwargs"]["json"]["limit"] == 6
    assert captured["kwargs"]["json"]["country"] == "EG"
    assert captured["kwargs"]["headers"]["Authorization"] == "Bearer test-firecrawl-secret"
    assert captured["kwargs"]["follow_redirects"] is False


def test_firecrawl_search_does_not_call_network_without_api_key(monkeypatch):
    monkeypatch.delenv("FIRECRAWL_API_KEY", raising=False)

    def unexpected_request(*args, **kwargs):
        raise AssertionError("network must not be called without an API key")

    monkeypatch.setattr("agents.web_agent._bounded_http_request", unexpected_request)
    assert WebAgent()._search_firecrawl("query") == []


def test_firecrawl_provider_is_disabled_by_default(monkeypatch):
    monkeypatch.delenv("FIRECRAWL_API_KEY", raising=False)
    monkeypatch.delenv("FIRECRAWL_SEARCH_ENABLED", raising=False)
    monkeypatch.delenv("OMARAI_FIRECRAWL_SEARCH_REQUEST_BUDGET", raising=False)

    status = WebAgent.status()

    assert status["firecrawl_search_api_configured"] is False
    assert status["firecrawl_search_enabled"] is False
    assert status["firecrawl_search_request_budget"] == 0


def test_firecrawl_request_budget_is_opt_in_and_hard_capped_to_one(monkeypatch):
    agent = WebAgent()
    monkeypatch.setenv("FIRECRAWL_API_KEY", "test-firecrawl-secret")
    monkeypatch.setenv("FIRECRAWL_SEARCH_ENABLED", "1")
    monkeypatch.setenv("OMARAI_FIRECRAWL_SEARCH_REQUEST_BUDGET", "3")

    agent._reset_deepseek_search_budget()
    assert agent._reserve_firecrawl_search_request() is True
    assert agent._reserve_firecrawl_search_request() is False

    agent._reset_deepseek_search_budget()
    assert agent._reserve_firecrawl_search_request() is True


def test_firecrawl_request_budget_defaults_to_zero(monkeypatch):
    agent = WebAgent()
    monkeypatch.setenv("FIRECRAWL_API_KEY", "test-firecrawl-secret")
    monkeypatch.setenv("FIRECRAWL_SEARCH_ENABLED", "1")
    monkeypatch.delenv("OMARAI_FIRECRAWL_SEARCH_REQUEST_BUDGET", raising=False)

    agent._reset_deepseek_search_budget()

    assert agent._reserve_firecrawl_search_request() is False


def test_firecrawl_is_blocked_when_optional_providers_are_disabled(monkeypatch):
    agent = WebAgent()
    agent.allow_optional_providers = False
    monkeypatch.setenv("FIRECRAWL_API_KEY", "test-firecrawl-secret")
    monkeypatch.setenv("FIRECRAWL_SEARCH_ENABLED", "1")
    monkeypatch.setenv("OMARAI_FIRECRAWL_SEARCH_REQUEST_BUDGET", "1")
    monkeypatch.setattr(agent, "_search_duckduckgo_html", lambda _query: [])
    monkeypatch.setattr(agent, "_search_bing_rss", lambda _query: [])

    def forbidden_firecrawl(_query):
        pytest.fail("per-request optional-provider denial must block Firecrawl")

    monkeypatch.setattr(agent, "_search_firecrawl", forbidden_firecrawl)
    with pytest.raises(RuntimeError, match="لم تُرجع موصلات البحث"):
        agent._search_web("Find industrial fire alarm suppliers in Egypt")

    firecrawl_status = next(
        item["status"]
        for item in agent._provider_diagnostics
        if item["provider"] == "firecrawl_search_api"
    )
    assert firecrawl_status == "disabled_by_request"


@pytest.mark.parametrize(
    ("query", "expected"),
    [
        ("Find buyers for industrial fire alarms in Egypt", "EG"),
        ("موردون لأنظمة الإنذار في السعودية", "SA"),
        ("Find fire alarm suppliers in Dubai UAE", "AE"),
        ("Find suppliers in the United Kingdom", "UK"),
        ("ابحث عن موردين لأنظمة الإنذار", "EG"),
    ],
)
def test_firecrawl_search_uses_explicit_query_geography(query, expected):
    assert WebAgent._firecrawl_search_country(query) == expected
