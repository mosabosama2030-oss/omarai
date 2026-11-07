from __future__ import annotations

from agents.research import fuse_ranked_results
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


def test_search_web_preserves_cross_provider_duplicates_for_rank_fusion(monkeypatch):
    agent = WebAgent()
    query = "Central Bank of Egypt official website"
    candidate = {
        "title": "Central Bank of Egypt official website",
        "url": "https://example.com/cbe",
        "snippet": "Official Central Bank of Egypt website and monetary policy.",
    }

    for env_name in ("DEEPSEEK_SEARCH_API_KEY", "BRAVE_SEARCH_API_KEY", "TAVILY_API_KEY"):
        monkeypatch.delenv(env_name, raising=False)

    monkeypatch.setattr(agent, "_search_duckduckgo_html", lambda _query: [dict(candidate)])
    monkeypatch.setattr(agent, "_search_bing_rss", lambda _query: [dict(candidate)])
    monkeypatch.setattr(agent, "_search_news", lambda _query: [])

    results = agent._search_web(query)

    assert len(results) == 2
    assert {item["provider"] for item in results} == {"duckduckgo_html", "bing_rss"}


def test_rank_fusion_uses_retrieval_relevance_to_break_near_rank_ties():
    batches = [{
        "query": "Central Bank of Egypt official website",
        "provider": "ddg",
        "results": [
            {
                "title": "Egypt central bank",
                "url": "https://example.com/weak",
                "snippet": "Egypt central bank",
                "retrieval_relevance_score": 0.20,
            },
            {
                "title": "Central Bank of Egypt official website",
                "url": "https://example.com/strong",
                "snippet": "Central Bank of Egypt official website and monetary policy.",
                "retrieval_relevance_score": 1.0,
            },
        ],
    }]

    ranked = fuse_ranked_results(batches)

    assert ranked[0]["url"] == "https://example.com/strong"
    assert ranked[0]["rank_score"] < ranked[1]["rank_score"]
    assert ranked[0]["retrieval_relevance_score"] == 1.0
