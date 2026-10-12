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

    def collect(query):
        seen["query"] = query
        return [sample_source()], None

    def generate(question, history, sources, search_warning):
        seen["question"] = question
        seen["history"] = history
        seen["sources"] = sources
        return "الإجابة: التقنية مناسبة للأسباب التالية [المصدر 1]."

    monkeypatch.setattr(agent, "_collect_sources", collect)
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
    monkeypatch.setattr(agent, "_collect_sources", lambda query: ([sample_source()], None))

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
