from __future__ import annotations

from agents.research import (
    classify_source,
    compact_search_query,
    evidence_signal_report,
    fallback_plan,
    fuse_ranked_results,
    registrable_domain,
    validate_plan,
)


def test_social_question_gets_platform_targeted_queries():
    plan = fallback_plan("ابحث في Reddit عن تجارب العملاء مع السيارات الكهربائية")
    assert plan["social_focus"] is True
    assert "reddit" in plan["platforms"]
    assert any("site:reddit.com" in query for query in plan["queries"])
    assert len(plan["queries"]) <= 8
