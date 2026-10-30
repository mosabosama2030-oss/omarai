from __future__ import annotations

from agents.web_agent import WebAgent


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

    for env_name in (
        "DEEPSEEK_SEARCH_API_KEY",
        "BRAVE_SEARCH_API_KEY",
        "TAVILY_API_KEY",
    ):
        monkeypatch.delenv(env_name, raising=False)

    monkeypatch.setattr(
        agent,
        "_search_duckduckgo_html",
        lambda _query: [dict(unrelated), dict(official)],
    )
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
    from agents.web_agent import _relevance_query_tokens, _relevance_ratio

    query = "climate policy emissions"
    assert len(_relevance_query_tokens(query)) == 3
    assert _relevance_ratio(query, "Climate report") == 0.0


def test_three_concept_query_documents_single_high_value_match_tradeoff():
    from agents.web_agent import _relevance_query_tokens, _relevance_ratio

    query = "central bank Egypt"
    assert len(_relevance_query_tokens(query)) == 3
    # A single country/entity match is insufficient without a second topical concept.
    assert _relevance_ratio(query, "Egypt") == 0.0


def test_short_two_concept_query_keeps_existing_relevance_floor():
    from agents.web_agent import _relevance_ratio

    assert _relevance_ratio("climate emissions", "Climate report") == 0.5
