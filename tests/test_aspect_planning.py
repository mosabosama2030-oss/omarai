"""Unit tests for aspect extraction and evidence ledger (no network)."""
from __future__ import annotations

from agents.aspect_planning import (
    arabic_aspect_diagnostics,
    build_aspect_queries,
    build_evidence_ledger,
    extract_aspects,
    repair_queries_for_missing_aspects,
)


def test_extract_aspects_from_min_hayth():
    q = (
        "حلل السيارات الكهربائية في مصر من حيث السعر، البطارية، والضمان. "
        "اذكر مصادر موثوقة."
    )
    aspects = extract_aspects(q)
    assert "السعر" in aspects or any("سعر" in a for a in aspects)
    assert any("بطار" in a for a in aspects)
    assert any("ضمان" in a for a in aspects)
    assert len(aspects) >= 3


def test_extract_aspects_from_multi_question_marks():
    q = "ما سعر الآيفون في مصر؟ وما مدة الضمان؟ وهل تتوفر صيانة محلية؟"
    aspects = extract_aspects(q)
    assert len(aspects) >= 2


def test_build_aspect_queries_prioritizes_topic():
    queries = build_aspect_queries(
        "السيارات الكهربائية في مصر",
        ["السعر", "الضمان"],
        limit=5,
    )
    assert queries[0] == "السيارات الكهربائية في مصر"
    assert any("السعر" in q for q in queries)
    assert any("الضمان" in q for q in queries)
    assert len(queries) <= 5


def test_evidence_ledger_marks_missing_and_covered():
    aspects = ["السعر", "الضمان"]
    sources = [
        {
            "title": "أسعار السيارات الكهربائية",
            "url": "https://example.com/prices",
            "snippet": "متوسط السعر في مصر لعام 2026",
            "page_text": "",
            "provider": "test",
        }
    ]
    ledger = build_evidence_ledger(aspects, sources)
    assert "السعر" in ledger["covered"] or any(
        "سعر" in c for c in ledger["covered"]
    )
    assert "الضمان" in ledger["missing"]
    assert 0 <= ledger["coverage_ratio"] <= 1


def test_repair_queries_for_missing():
    qs = repair_queries_for_missing_aspects(
        "السيارات الكهربائية مصر",
        ["الضمان", "الصيانة"],
        limit=2,
    )
    assert len(qs) == 2
    assert all("السيارات" in q for q in qs)


def test_arabic_diagnostics_not_truth_claim():
    ledger = {
        "covered": ["السعر"],
        "missing": ["الضمان"],
        "coverage_ratio": 0.5,
    }
    lines = arabic_aspect_diagnostics(ledger)
    assert any("ضمان" in line for line in lines)
    assert any("لا يثبت" in line for line in lines)


def test_extract_aspects_understands_compound_connectors_without_marker():
    question = (
        "قارن بين الأنظمة: السعر والبطارية، بالإضافة إلى الضمان والصيانة "
        "والخصوصية والاعتمادية والدعم والجودة"
    )
    aspects = extract_aspects(question)
    normalized = " ".join(aspects)
    for expected in ("السعر", "البطارية", "الضمان", "الصيانة", "الخصوصية", "الاعتمادية", "الدعم", "الجودة"):
        assert expected in normalized
    assert len(aspects) <= 8


def test_extracts_joined_facets_without_formal_comparison_marker():
    aspects = extract_aspects("ما سعر الهاتف ومدة الضمان والصيانة؟")
    joined = " ".join(aspects)
    assert "السعر" in joined
    assert "الضمان" in joined
    assert "الصيانة" in joined
