"""Regression: citation tails without punctuation must not pollute topic queries."""
from __future__ import annotations

from agents.research import compact_search_query


def test_compact_search_query_strips_citation_tail_without_punctuation():
    query = compact_search_query(
        "السيارات الكهربائية في مصر واذكر مصادر وروابط موثوقة"
    )
    assert "السيارات الكهربائية" in query
    assert "مصر" in query
    assert "مصادر" not in query
    assert "روابط" not in query
    assert query

    query_en = compact_search_query(
        "electric vehicles in Egypt and please cite sources with links"
    )
    assert "egypt" in query_en.lower()
    assert "please cite" not in query_en.lower()
    assert not query_en.lower().endswith(" and")
