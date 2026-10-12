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


def test_user_supplied_url_is_prioritized_and_page_content_is_extracted(monkeypatch):
    agent = WebAgent()
    monkeypatch.setattr(agent, "_search_web", lambda query: [])
    monkeypatch.setattr(
        agent,
        "_fetch_page",
        lambda url: ("User page title", "Full public page text supplied for analysis"),
    )
    sources, warnings, report = agent._collect_research({
        "queries": ["لخص هذه الصفحة"],
        "direct_urls": ["https://example.com/article"],
        "social_focus": False,
        "freshness": "any",
        "depth": "deep",
        "planning_method": "test",
    })
    assert warnings == []
    assert len(sources) == 1
    assert sources[0]["url"] == "https://example.com/article"
    assert sources[0]["title"] == "User page title"
    assert sources[0]["page_fetched"] is True
    assert "user_supplied_url" in report["providers_used"]



def test_official_x_search_is_used_only_with_explicit_bearer_token(monkeypatch):
    import httpx

    monkeypatch.setenv("X_BEARER_TOKEN", "test-token")

    class FakeResponse:
        status_code = 200

        def json(self):
            return {
                "data": [{
                    "id": "1840000000000000000",
                    "text": "تجربة علنية لاستهلاك سيارة كهربائية",
                    "created_at": "2026-10-12T10:00:00Z",
                    "author_id": "u1",
                }],
                "includes": {
                    "users": [{"id": "u1", "username": "driver", "name": "Driver"}]
                },
            }

    calls = []

    def fake_get(url, **kwargs):
        calls.append((url, kwargs))
        return FakeResponse()

    monkeypatch.setattr(httpx, "get", fake_get)
    results, warnings = WebAgent()._search_social(
        "سيارة كهربائية", ["x"]
    )
    assert warnings == []
    assert len(results) == 1
    assert results[0]["provider"] == "x_official_api"
    assert results[0]["url"] == "https://x.com/driver/status/1840000000000000000"
    assert calls[0][1]["headers"]["Authorization"] == "Bearer test-token"



def test_instagram_graph_api_returns_only_public_hashtag_media(monkeypatch):
    import httpx

    monkeypatch.setenv("INSTAGRAM_USER_ID", "ig-user-123")
    monkeypatch.setenv("INSTAGRAM_ACCESS_TOKEN", "test-ig-token")
    monkeypatch.setenv("META_GRAPH_VERSION", "v25.0")

    class FakeResponse:
        status_code = 200

        def __init__(self, payload):
            self.payload = payload

        def json(self):
            return self.payload

    calls = []

    def fake_get(url, **kwargs):
        calls.append((url, kwargs))
        if url.endswith("/ig_hashtag_search"):
            return FakeResponse({"data": [{"id": "tag-7", "name": "cars"}]})
        if url.endswith("/tag-7/recent_media"):
            return FakeResponse({"data": [{
                "permalink": "https://www.instagram.com/p/ABC123/",
                "caption": "Owner shared an electric car review",
                "media_type": "IMAGE",
                "timestamp": "2026-10-12T10:00:00+0000",
                "like_count": 17,
                "comments_count": 4,
            }]})
        raise AssertionError(f"Unexpected URL {url}")

    monkeypatch.setattr(httpx, "get", fake_get)
    results, warnings = WebAgent()._search_social(
        "Instagram #cars", ["instagram"]
    )
    assert warnings == []
    assert len(results) == 1
    assert results[0]["provider"] == "instagram_graph_api"
    assert results[0]["url"] == "https://www.instagram.com/p/ABC123/"
    assert "likes=17" in results[0]["snippet"]
    assert calls[0][1]["params"]["q"] == "cars"
    assert calls[0][1]["params"]["access_token"] == "test-ig-token"
    assert "test-ig-token" not in str(results)


def test_instagram_api_not_configured_uses_honest_fallback_warning(monkeypatch):
    monkeypatch.delenv("INSTAGRAM_USER_ID", raising=False)
    monkeypatch.delenv("INSTAGRAM_ACCESS_TOKEN", raising=False)
    results, warnings = WebAgent()._search_social(
        "تجارب عامة على Instagram", ["instagram"]
    )
    assert results == []
    assert any("indexed public Instagram" in warning for warning in warnings)


def test_facebook_pages_api_reads_only_operator_configured_pages(monkeypatch):
    import httpx

    monkeypatch.setenv("FACEBOOK_PAGE_ACCESS_TOKEN", "test-page-token")
    monkeypatch.setenv("FACEBOOK_PAGE_IDS", "page-1,page-2")

    class FakeResponse:
        status_code = 200

        def json(self):
            return {"data": [{
                "message": "Electric car owners looking for charging advice",
                "permalink_url": "https://www.facebook.com/example/posts/123",
                "created_time": "2026-10-12T12:00:00+0000",
                "comments": {"data": [
                    {"message": "What is the current price?", "like_count": 3}
                ]},
            }]}

    calls = []

    def fake_get(url, **kwargs):
        calls.append((url, kwargs))
        return FakeResponse()

    monkeypatch.setattr(httpx, "get", fake_get)
    results, warnings = WebAgent()._search_social(
        "electric car", ["facebook"]
    )
    assert len(results) == 2  # one matching post for each explicitly configured page
    assert warnings == []
    assert all(item["provider"] == "facebook_pages_api" for item in results)
    assert all("Electric car owners" in item["snippet"] for item in results)
    assert len(calls) == 2
    assert all("Bearer test-page-token" == call[1]["headers"]["Authorization"] for call in calls)


def test_reddit_oauth_api_is_preferred_when_credentials_are_configured(monkeypatch):
    import httpx

    monkeypatch.setenv("REDDIT_CLIENT_ID", "client-test")
    monkeypatch.setenv("REDDIT_CLIENT_SECRET", "secret-test")
    monkeypatch.setenv("REDDIT_USER_AGENT", "test:omarai:0.1")

    class FakeResponse:
        status_code = 200

        def __init__(self, payload):
            self.payload = payload

        def json(self):
            return self.payload

        @property
        def content(self):
            import json
            return json.dumps(self.payload).encode()

    calls = []

    def fake_post(url, **kwargs):
        calls.append(("POST", url, kwargs))
        return FakeResponse({"access_token": "test-reddit-access-token"})

    def fake_get(url, **kwargs):
        calls.append(("GET", url, kwargs))
        return FakeResponse({"data": {"children": [{
            "data": {
                "title": "Electric vehicle owner discussion",
                "permalink": "/r/cars/comments/example/post/",
                "selftext": "Owners discuss battery range.",
                "created_utc": 1791800000,
                "score": 25,
                "num_comments": 8,
            }
        }]}})

    monkeypatch.setattr(httpx, "post", fake_post)
    monkeypatch.setattr(httpx, "get", fake_get)
    results, warnings = WebAgent()._search_social(
        "electric vehicles", ["reddit"]
    )
    assert len(results) == 1
    assert warnings == []
    assert results[0]["provider"] == "reddit_oauth_api"
    assert results[0]["url"] == "https://www.reddit.com/r/cars/comments/example/post/"
    assert "score=25" in results[0]["snippet"]
    assert len([call for call in calls if call[0] == "POST"]) == 1
    assert any("oauth.reddit.com/search" in call[1] for call in calls if call[0] == "GET")
    assert "test-reddit-access-token" not in str(results)



def test_role_models_are_explicit_and_have_a_fallback(monkeypatch):
    for name in (
        "OMARAI_LLM_MODEL",
        "OMARAI_PLANNER_MODEL",
        "OMARAI_ANSWER_MODEL",
        "OMARAI_REVIEW_MODEL",
        "OMARAI_LLM_FALLBACK_MODEL",
    ):
        monkeypatch.delenv(name, raising=False)

    agent = WebAgent()
    assert agent.planner_model == "nvidia/nemotron-3-ultra-550b-a55b:free"
    assert agent.answer_model == "google/gemma-4-31b-it:free"
    assert agent.review_model == agent.answer_model
    assert agent.fallback_model == "openrouter/free"


def test_global_model_override_is_preserved_for_existing_users(monkeypatch):
    monkeypatch.setenv("OMARAI_LLM_MODEL", "example/custom-model")
    monkeypatch.delenv("OMARAI_PLANNER_MODEL", raising=False)
    monkeypatch.delenv("OMARAI_ANSWER_MODEL", raising=False)
    monkeypatch.delenv("OMARAI_REVIEW_MODEL", raising=False)

    agent = WebAgent()
    assert agent.planner_model == "example/custom-model"
    assert agent.answer_model == "example/custom-model"
    assert agent.review_model == "example/custom-model"


def test_completion_uses_fallback_model_after_primary_http_error(monkeypatch):
    import io
    import json
    import urllib.error

    agent = WebAgent()
    agent.api_key = "test-key"
    agent.fallback_model = "openrouter/free"
    called = []

    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, traceback):
            return False

        def read(self, limit):
            return json.dumps({
                "choices": [{"message": {"content": "إجابة من النموذج الاحتياطي"}}]
            }).encode("utf-8")

    def fake_urlopen(request, timeout):
        payload = json.loads(request.data.decode("utf-8"))
        called.append(payload["model"])
        if payload["model"] == "broken/primary":
            raise urllib.error.HTTPError(
                request.full_url,
                503,
                "service unavailable",
                hdrs=None,
                fp=io.BytesIO(b"private provider diagnostics"),
            )
        return FakeResponse()

    monkeypatch.setattr("agents.web_agent.urllib.request.urlopen", fake_urlopen)
    result = agent._request_completion(
        [{"role": "user", "content": "اختبار"}],
        model="broken/primary",
    )

    assert result == "إجابة من النموذج الاحتياطي"
    assert called == ["broken/primary", "openrouter/free"]
    assert agent.model_usage == [{
        "requested_model": "broken/primary",
        "used_model": "openrouter/free",
        "fallback_used": "true",
    }]


def test_health_status_reports_models_without_credentials(monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    monkeypatch.delenv("OMARAI_LLM_API_KEY", raising=False)
    status = WebAgent.status()
    assert status["planner_model"] == "nvidia/nemotron-3-ultra-550b-a55b:free"
    assert status["answer_model"] == "google/gemma-4-31b-it:free"
    assert status["fallback_model"] == "openrouter/free"
    assert status["language_model_configured"] is False
    assert "api_key" not in status
