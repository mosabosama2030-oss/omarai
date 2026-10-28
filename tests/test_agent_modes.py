from __future__ import annotations

from agents.research import evidence_signal_report
from agents.web_agent import WebAgent


def test_deep_mode_expands_search_angles_and_returns_coverage_signals(monkeypatch):
    agent = WebAgent()
    agent.api_key = "test-key"
    seen = {}

    def plan(question, history):
        return {
            "queries": ["topic summary"],
            "direct_urls": [],
            "social_focus": False,
            "freshness": "any",
            "depth": "standard",
            "platforms": [],
            "planning_method": "test",
        }

    source = {
        "title": "Topic summary public report",
        "url": "https://example.org/report",
        "snippet": "Evidence snippet about topic summary",
        "page_text": "Fetched text about topic summary",
        "page_fetched": True,
        "provider": "test_search",
        "providers": ["test_search"],
        "queries": ["topic summary"],
        "domain": "example.org",
        "source_class": "general",
        "platform": "web",
        "published_at": "2026-10-10",
        "rank_score": 1.0,
    }

    def collect(research_plan):
        seen["plan"] = dict(research_plan)
        report = {
            "queries_planned": len(research_plan["queries"]),
            "queries_attempted": len(research_plan["queries"]),
            "query_results": [],
            "unique_sources": 1,
            "pages_fetched": 1,
            "providers_used": ["test_search"],
            "provider_counts": {"test_search": 1},
            "platform_counts": {"web": 1},
            "social_direct_results": 0,
            "depth": research_plan["depth"],
            "planning_method": "test",
            "evidence_signals": evidence_signal_report([source]),
        }
        return [source], [], report

    monkeypatch.setattr(agent, "_plan_search", plan)
    monkeypatch.setattr(agent, "_collect_research", collect)
    monkeypatch.setattr(agent, "_generate", lambda *args, **kwargs: "الخلاصة [المصدر 1]")
    monkeypatch.setattr(agent, "_review_answer", lambda question, answer, sources: answer)

    result = agent.answer("حلل الموضوع", mode="deep")

    assert seen["plan"]["depth"] == "deep"
    assert len(seen["plan"]["queries"]) > 1
    assert result["research_plan"]["mode"] == "deep"
    assert "evidence_signals" in result["search_report"]
    assert result["search_report"]["evidence_repair"]["attempted"] is False
    assert result["search_report"]["evidence_repair"]["reason"] == "deep_research_already_expanded"
    assert result["search_report"]["evidence_signals"]["unique_domains"] == 1
