from __future__ import annotations

import pytest

from agents.web_agent import WebAgent, _public_http_url


def sample_source():
    return {
        "title": "مقالة اختبار",
        "url": "https://example.com/research",
        "snippet": "مقتطف مفيد من المصدر.",
        "page_text": "نص مستخرج من الصفحة.",
        "page_fetched": True,
    }


def test_agent_synthesizes_with_sources_without_live_network(monkeypatch):
    agent = WebAgent()
    agent.api_key = "test-key"
    seen = {}

    def plan(question, history):
        return {
            "queries": [question],
            "social_focus": False,
            "freshness": "any",
            "depth": "deep",
            "platforms": [],
            "planning_method": "test",
        }

    def collect(research_plan):
        seen["plan"] = research_plan
        return [sample_source()], [], {
            "queries_planned": 1,
            "queries_attempted": 1,
            "query_results": [{"query": research_plan["queries"][0], "results": 1}],
            "unique_sources": 1,
            "pages_fetched": 1,
            "providers_used": ["test"],
            "platform_counts": {"web": 1},
            "social_direct_results": 0,
            "depth": "deep",
            "planning_method": "test",
        }

    def generate(question, history, sources, search_warning, research_plan=None, search_report=None):
        seen["question"] = question
        seen["history"] = history
        seen["sources"] = sources
        seen["report"] = search_report
        return "الإجابة: التقنية مناسبة للأسباب التالية [المصدر 1]."

    monkeypatch.setattr(agent, "_plan_search", plan)
    monkeypatch.setattr(agent, "_collect_research", collect)
    monkeypatch.setattr(agent, "_review_answer", lambda question, answer, sources: answer)
    monkeypatch.setattr(agent, "_generate", generate)
    result = agent.answer(
        "قارن هذه التقنية",
        history=[{"role": "user", "content": "ما هي التقنية؟"}],
    )

    assert result["used_web_search"] is True
    assert result["used_language_model"] is True
    assert result["sources"][0]["url"] == "https://example.com/research"
    assert "[المصدر 1]" in result["answer"]
    assert seen["question"] == "قارن هذه التقنية"
    assert seen["history"] == [{"role": "user", "content": "ما هي التقنية؟"}]


def test_agent_returns_search_snippets_if_model_not_configured(monkeypatch):
    agent = WebAgent()
    agent.api_key = ""
    monkeypatch.setattr(
        agent,
        "_collect_research",
        lambda plan: (
            [sample_source()],
            [],
            {
                "queries_planned": 1,
                "queries_attempted": 1,
                "query_results": [],
                "unique_sources": 1,
                "pages_fetched": 1,
                "providers_used": ["test"],
                "platform_counts": {"web": 1},
                "social_direct_results": 0,
                "depth": "standard",
                "planning_method": "test",
            },
        ),
    )

    result = agent.answer("ما الذي يقوله المصدر؟")

    assert result["used_web_search"] is True
    assert result["used_language_model"] is False
    assert "OPENROUTER_API_KEY" in result["answer"]
    assert result["sources"][0]["page_fetched"] is True


def test_agent_rejects_empty_or_oversized_question():
    agent = WebAgent()
    with pytest.raises(ValueError):
        agent.answer("   ")
    with pytest.raises(ValueError):
        agent.answer("س" * 4001)


def test_history_search_query_expands_short_follow_up():
    history = [{"role": "user", "content": "قارن أسعار السيارات الكهربائية في مصر"}]
    query = WebAgent._history_search_query("والسعر؟", history)
    assert "السيارات الكهربائية" in query
    assert "والسعر؟" in query


def test_public_url_filter_rejects_local_and_credential_urls():
    assert _public_http_url("http://127.0.0.1/admin") is None
    assert _public_http_url("http://localhost:8000/") is None
    assert _public_http_url("https://user:pass@example.com/private") is None
    assert _public_http_url("file:///etc/passwd") is None


def test_public_url_filter_accepts_basic_https_url():
    assert _public_http_url("https://example.com/path#section") == "https://example.com/path"


def test_search_web_parses_duckduckgo_and_bing_without_ddgs(monkeypatch):
    import httpx

    html = """
    <html><body>
      <div class="result">
        <a class="result__a" href="https://example.com/first">صفحة أولى</a>
        <a class="result__snippet">مقتطف أول</a>
      </div>
    </body></html>
    """
    rss = """
    <rss><channel><item>
      <title>صفحة ثانية</title>
      <link>https://example.net/second</link>
      <description>مقتطف ثاني</description>
    </item></channel></rss>
    """

    class FakeResponse:
        status_code = 200

        def __init__(self, text):
            self.text = text
            self.content = text.encode("utf-8")

    calls = []

    def fake_get(url, **kwargs):
        calls.append(url)
        return FakeResponse(html if "duckduckgo.com" in url else rss)

    monkeypatch.setattr(httpx, "get", fake_get)
    results = WebAgent()._search_web("سؤال بحث تجريبي")

    assert len(results) == 2
    assert results[0]["title"] == "صفحة أولى"
    assert results[0]["url"] == "https://example.com/first"
    assert results[1]["title"] == "صفحة ثانية"
    assert results[1]["url"] == "https://example.net/second"
    assert len(calls) == 2



def test_model_planner_preserves_social_intent_and_adds_targeted_query(monkeypatch):
    agent = WebAgent()
    agent.api_key = "test-key"
    monkeypatch.setattr(
        agent,
        "_request_completion",
        lambda *args, **kwargs: (
            '{"queries":["مراجعات السيارات الكهربائية"],"social_focus":true,'
            '"freshness":"any","depth":"deep","platforms":["reddit"]}'
        ),
    )
    plan = agent._plan_search(
        "ابحث في Reddit عن تجارب العملاء مع السيارات الكهربائية",
        [],
    )
    assert plan["planning_method"] == "language_model"
    assert plan["social_focus"] is True
    assert "reddit" in plan["platforms"]
    assert any("site:reddit.com" in query for query in plan["queries"])


def test_direct_social_search_reads_public_reddit_and_bluesky_results(monkeypatch):
    import httpx

    reddit_xml = """<rss><channel><item>
      <title>تجربة سيارة كهربائية</title>
      <link>https://www.reddit.com/r/cars/comments/abc123/test/</link>
      <description>استهلاك البطارية في الحر</description>
      <pubDate>Mon, 12 Oct 2026 10:00:00 GMT</pubDate>
    </item></channel></rss>"""

    class FakeResponse:
        status_code = 200

        def __init__(self, text="", data=None):
            self.text = text
            self.content = text.encode("utf-8")
            self._data = data or {}

        def json(self):
            return self._data

    def fake_get(url, **kwargs):
        if "reddit.com" in url:
            return FakeResponse(reddit_xml)
        if "bsky.app" in url or "public.api.bsky.app" in url:
            return FakeResponse(data={
                "posts": [{
                    "post": {
                        "uri": "at://did:plc:example/app.bsky.feed.post/rkey123",
                        "indexedAt": "2026-10-12T10:00:00Z",
                        "record": {"text": "استخدمت السيارة شهرًا"},
                        "author": {"handle": "driver.bsky.social", "displayName": "Driver"},
                    }
                }]
            })
        raise AssertionError(f"Unexpected URL: {url}")

    monkeypatch.setattr(httpx, "get", fake_get)
    results, warnings = WebAgent()._search_social(
        "سيارة كهربائية", ["reddit", "bluesky"]
    )
    assert warnings == []
    assert any(item["provider"] == "reddit_public_rss" for item in results)
    bsky = next(item for item in results if item["provider"] == "bluesky_public_search")
    assert bsky["url"] == "https://bsky.app/profile/driver.bsky.social/post/rkey123"
    assert bsky["snippet"] == "استخدمت السيارة شهرًا"


def test_research_collection_fuses_multiple_queries_and_reports_provenance(monkeypatch):
    agent = WebAgent()

    def search(query):
        if query == "query one":
            return [
                {"title": "Shared", "url": "https://example.com/shared", "snippet": "Some evidence", "provider": "ddg", "provider_rank": 1},
                {"title": "Unique A", "url": "https://example.com/a", "snippet": "Evidence A", "provider": "ddg", "provider_rank": 2},
            ]
        return [
            {"title": "Shared item", "url": "https://example.com/shared", "snippet": "More evidence about this result", "provider": "bing", "provider_rank": 1},
            {"title": "Unique B", "url": "https://example.com/b", "snippet": "Evidence B", "provider": "bing", "provider_rank": 2},
        ]

    monkeypatch.setattr(agent, "_search_web", search)
    monkeypatch.setattr(agent, "_fetch_page", lambda url: ("Read title", "Extracted public page text"))
    sources, warnings, report = agent._collect_research({
        "queries": ["query one", "query two"],
        "social_focus": False,
        "freshness": "any",
        "depth": "deep",
        "planning_method": "test",
    })
    shared = next(item for item in sources if "shared" in item["url"])
    assert warnings == []
    assert len(sources) == 3
    assert set(shared["providers"]) == {"ddg", "bing"}
    assert len(shared["queries"]) == 2
    assert report["queries_planned"] == 2
    assert report["pages_fetched"] == 3
    assert "ddg" in report["providers_used"]
    assert "bing" in report["providers_used"]



def test_invalid_citations_are_removed_and_valid_ones_preserved():
    answer, warnings = WebAgent._remove_invalid_citations(
        "النتيجة [المصدر 1] وادعاء آخر [المصدر 11].", 1
    )
    assert "[المصدر 1]" in answer
    assert "[المصدر 11]" not in answer
    assert len(warnings) == 1
