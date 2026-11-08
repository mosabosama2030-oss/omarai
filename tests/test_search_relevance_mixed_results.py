from __future__ import annotations

import httpx
import pytest

from agents.web_agent import WebAgent, _minimum_relevance_ratio, _relevance_ratio, _relevance_query_tokens


def test_search_web_keeps_relevant_official_result_and_drops_maps_help(monkeypatch):
    agent = WebAgent()
    query = "الموقع الرسمي للبنك المركزي المصري"
    unrelated = {
        "title": "خرائط Google",
        "url": "https://support.google.com/maps/answer/2839911?hl=ar-sa",
        "snippet": "البحث عن موقعك الجغرافي وتحسين دقته في خرائط Google.",
        "provider": "test_provider",
        "provider_rank": 1,
    }
    official = {
        "title": "Central Bank of Egypt - Official Website",
        "url": "https://www.cbe.org.eg/en/Pages/default.aspx",
        "snippet": "Official website of the Central Bank of Egypt and its monetary policy decisions.",
        "provider": "test_provider",
        "provider_rank": 2,
    }

    for env_name in ("DEEPSEEK_SEARCH_API_KEY", "BRAVE_SEARCH_API_KEY", "TAVILY_API_KEY"):
        monkeypatch.delenv(env_name, raising=False)

    monkeypatch.setattr(agent, "_search_duckduckgo_html", lambda _query: [dict(unrelated), dict(official)])
    monkeypatch.setattr(agent, "_search_bing_rss", lambda _query: [dict(unrelated)])
    monkeypatch.setattr(agent, "_search_news", lambda _query: [])

    results = agent._search_web(query)

    assert [item["url"] for item in results] == [official["url"]]
    diagnostics = {
        row["provider"]: row
        for row in agent._provider_diagnostics
        if row.get("provider") in {"duckduckgo_html", "bing_rss"}
    }
    assert diagnostics["duckduckgo_html"]["status"] == "ok"
    assert diagnostics["duckduckgo_html"]["accepted_count"] == 1
    assert diagnostics["duckduckgo_html"]["rejection_counts"]["relevance_below_threshold"] == 1
    assert diagnostics["bing_rss"]["status"] == "filtered_all"
    assert diagnostics["bing_rss"]["accepted_count"] == 0
    assert diagnostics["bing_rss"]["rejection_counts"]["relevance_below_threshold"] == 1


def test_three_concept_query_rejects_candidate_matching_only_one_topic():
    query = "climate policy emissions"
    assert len(_relevance_query_tokens(query)) == 3
    assert _relevance_ratio(query, "Climate report") == 0.0


def test_three_concept_query_documents_single_high_value_match_tradeoff():
    query = "central bank Egypt"
    assert len(_relevance_query_tokens(query)) == 3
    assert _relevance_ratio(query, "Egypt") == 0.0


def test_short_two_concept_query_keeps_existing_relevance_floor():
    assert _relevance_ratio("climate emissions", "Climate report") >= _minimum_relevance_ratio("climate emissions")


def test_search_web_preserves_same_page_discovered_by_distinct_providers(monkeypatch):
    agent = WebAgent()
    query = "Central Bank of Egypt official website"
    candidate = {
        "title": "Central Bank of Egypt official website",
        "url": "https://example.com/cbe",
        "snippet": "Official Central Bank of Egypt website and monetary policy.",
    }
    for env_name in (
        "DEEPSEEK_SEARCH_API_KEY",
        "BRAVE_SEARCH_API_KEY",
        "TAVILY_API_KEY",
    ):
        monkeypatch.delenv(env_name, raising=False)

    monkeypatch.setattr(
        agent, "_search_duckduckgo_html",
        lambda _query: [
            {**candidate, "url": "https://example.com/cbe?utm_source=ddg#home"},
            dict(candidate),
        ],
    )
    monkeypatch.setattr(
        agent, "_search_bing_rss",
        lambda _query: [{**candidate, "url": "https://example.com/cbe?utm_source=bing"}],
    )
    monkeypatch.setattr(agent, "_search_news", lambda _query: [])

    results = agent._search_web(query)

    assert len(results) == 2
    assert {item["provider"] for item in results} == {
        "duckduckgo_html",
        "bing_rss",
    }
    assert len({
        agent._normalized_source_url_key(item["url"])
        for item in results
    }) == 1


def test_search_web_keeps_best_duplicate_per_provider_without_erasing_other_providers(monkeypatch):
    agent = WebAgent()
    query = "Central Bank of Egypt official website"
    short = {
        "title": "Central Bank of Egypt official website",
        "url": "https://example.com/cbe",
        "snippet": "Central Bank of Egypt.",
    }
    longer = {
        **short,
        "url": "https://example.com/cbe?utm_source=ddg",
        "snippet": "Official Central Bank of Egypt website and monetary policy decisions.",
    }
    for env_name in (
        "DEEPSEEK_SEARCH_API_KEY",
        "BRAVE_SEARCH_API_KEY",
        "TAVILY_API_KEY",
    ):
        monkeypatch.delenv(env_name, raising=False)

    monkeypatch.setattr(
        agent, "_search_duckduckgo_html",
        lambda _query: [dict(short), dict(longer)],
    )
    monkeypatch.setattr(
        agent, "_search_bing_rss",
        lambda _query: [{**short, "provider": "bing_override"}],
    )
    monkeypatch.setattr(agent, "_search_news", lambda _query: [])

    results = agent._search_web(query)

    assert len(results) == 2
    ddg = next(item for item in results if item["provider"] == "duckduckgo_html")
    assert ddg["snippet"] == longer["snippet"]
    assert {item["provider"] for item in results} == {
        "duckduckgo_html",
        "bing_override",
    }


def test_search_web_stores_normalized_retrieval_relevance_for_fusion(monkeypatch):
    agent = WebAgent()
    query = "Central Bank of Egypt official website"
    candidate = {
        "title": "Central Bank of Egypt official website",
        "url": "https://example.com/cbe",
        "snippet": "Official Central Bank of Egypt website and monetary policy decisions.",
    }
    for env_name in (
        "DEEPSEEK_SEARCH_API_KEY",
        "BRAVE_SEARCH_API_KEY",
        "TAVILY_API_KEY",
    ):
        monkeypatch.delenv(env_name, raising=False)
    monkeypatch.setattr(agent, "_search_duckduckgo_html", lambda _query: [dict(candidate)])
    monkeypatch.setattr(agent, "_search_bing_rss", lambda _query: [])
    monkeypatch.setattr(agent, "_search_news", lambda _query: [])

    results = agent._search_web(query)

    assert len(results) == 1
    assert 0.0 <= results[0]["retrieval_relevance_score"] <= 1.0


def test_rank_fusion_uses_retrieval_relevance_only_for_exact_rrf_ties():
    from agents.research import fuse_ranked_results

    weak = {
        "title": "Egypt central bank",
        "url": "https://example.com/weak",
        "snippet": "Egypt central bank",
        "retrieval_relevance_score": 0.2,
    }
    strong = {
        "title": "Central Bank of Egypt official website",
        "url": "https://example.com/strong",
        "snippet": "Central Bank of Egypt official website and monetary policy.",
        "retrieval_relevance_score": 1.0,
    }
    batches = [
        {
            "query": "Central Bank of Egypt official website",
            "provider": "ddg",
            "results": [dict(weak), dict(strong)],
        },
        {
            "query": "Central Bank of Egypt official website",
            "provider": "bing",
            "results": [dict(strong), dict(weak)],
        },
    ]

    ranked = fuse_ranked_results(batches)

    assert ranked[0]["url"] == "https://example.com/strong"
    assert ranked[0]["rank_score"] == ranked[1]["rank_score"]
    assert ranked[0]["retrieval_relevance_score"] == 1.0
    assert set(ranked[0]["providers"]) == {"ddg", "bing"}


def test_rank_fusion_ignores_invalid_retrieval_relevance_scores():
    from agents.research import fuse_ranked_results

    for invalid in (True, -0.1, 1.1, float("nan"), float("inf"), "not-a-score"):
        ranked = fuse_ranked_results([{
            "query": "Central Bank of Egypt",
            "provider": "ddg",
            "results": [{
                "title": "Central Bank of Egypt",
                "url": "https://example.com/cbe",
                "snippet": "Central Bank of Egypt official website.",
                "retrieval_relevance_score": invalid,
            }],
        }])
        assert ranked[0]["retrieval_relevance_score"] is None


@pytest.mark.parametrize(
    ("status_code", "expected_status"),
    [
        (202, "http_error"),
        (301, "http_error"),
        (403, "unauthorized"),
        (429, "rate_limited"),
        (500, "http_error"),
    ],
)
def test_httpx_status_errors_are_classified_from_response_status(status_code, expected_status):
    request = httpx.Request("GET", "https://provider.example/search")
    response = httpx.Response(status_code, request=request)
    error = httpx.HTTPStatusError(
        "provider returned a non-success status",
        request=request,
        response=response,
    )

    status, detail = WebAgent._classify_provider_exception(error)

    assert status == expected_status
    assert str(status_code) in detail
    assert "provider.example" not in detail


def test_httpx_timeout_and_decoding_errors_are_not_reported_as_generic_failures():
    request = httpx.Request("GET", "https://provider.example/search")

    timeout_status, _ = WebAgent._classify_provider_exception(
        httpx.ReadTimeout("provider timed out", request=request)
    )
    decoding_status, _ = WebAgent._classify_provider_exception(
        httpx.DecodingError("invalid compressed response")
    )

    assert timeout_status == "timeout"
    assert decoding_status == "invalid_response"
