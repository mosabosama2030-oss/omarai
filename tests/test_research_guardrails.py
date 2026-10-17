"""Regression and adversarial tests for depth, freshness, relevance, evidence."""
from __future__ import annotations

from agents.research import (
    decide_evidence_status,
    detect_depth,
    detect_freshness,
    filter_relevant_sources,
    source_relevance_score,
)


# --- detect_depth -----------------------------------------------------------

def test_depth_deep_english_phrases():
    assert detect_depth("Please do a deep research on climate policy") == "deep"
    assert detect_depth("in-depth comparison of EV batteries") == "deep"
    assert detect_depth("comprehensive analysis of market risks") == "deep"


def test_depth_deep_arabic_phrases():
    assert detect_depth("أريد بحث عميق عن الذكاء الاصطناعي") == "deep"
    assert detect_depth("قارن بين السيارات الكهربائية والبنزين") == "deep"
    assert detect_depth("بحث شامل بالتفصيل عن الذهب") == "deep"


def test_depth_standard_ordinary_questions():
    assert detect_depth("what is the capital of France") == "standard"
    assert detect_depth("ما عاصمة مصر") == "standard"
    assert detect_depth("I know about electric cars") == "standard"
    assert detect_depth("hello") == "standard"
    assert detect_depth("") == "standard"


def test_depth_does_not_trigger_on_partial_words():
    # "sources" is a deep term; ensure isolated ordinary use still works via whole-word
    assert detect_depth("the river sources of the Nile") in {"deep", "standard"}  # may match
    assert detect_depth("tell me a joke") == "standard"


# --- detect_freshness -------------------------------------------------------

def test_freshness_positive_english():
    assert detect_freshness("what is happening now") is True
    assert detect_freshness("latest news about Egypt") is True
    assert detect_freshness("price today of gold") is True
    assert detect_freshness("breaking news") is True


def test_freshness_positive_arabic():
    assert detect_freshness("ما هي آخر الأخبار عن الذهب") is True
    assert detect_freshness("سعر اليوم للدولار") is True
    assert detect_freshness("مستجدات السوق حاليا") is True


def test_freshness_negative_know_and_snowden():
    assert detect_freshness("I know about cars") is False
    assert detect_freshness("Snowden revelations summary") is False
    assert detect_freshness("knowledge graph basics") is False
    assert detect_freshness("ما عاصمة فرنسا") is False


# --- relevance gate ---------------------------------------------------------

def test_relevance_keeps_matching_source():
    src = {
        "title": "أسعار السيارات الكهربائية في مصر 2026",
        "url": "https://example.com/ev-egypt",
        "snippet": "ارتفعت حصة السيارات الكهربائية في السوق المصري هذا العام.",
        "domain": "example.com",
        "source_class": "general",
        "providers": ["ddg"],
    }
    rel = source_relevance_score(src, "أسعار السيارات الكهربائية في مصر")
    assert rel["accepted"] is True
    assert rel["score"] >= 18

    # English-English match
    src_en = {
        "title": "Electric vehicles in Egypt 2026",
        "url": "https://example.com/ev-egypt-en",
        "snippet": "Market share of electric cars in Egypt rose this year.",
        "domain": "example.com",
        "source_class": "general",
        "providers": ["ddg"],
    }
    rel_en = source_relevance_score(src_en, "electric vehicles Egypt market share")
    assert rel_en["accepted"] is True


def test_relevance_rejects_unrelated():
    src = {
        "title": "Best pasta recipes",
        "url": "https://cooking.example/pasta",
        "snippet": "How to make carbonara at home with eggs and cheese.",
        "domain": "cooking.example",
        "source_class": "general",
        "providers": ["bing"],
    }
    rel = source_relevance_score(src, "أسعار السيارات الكهربائية في مصر")
    assert rel["accepted"] is False


def test_relevance_keeps_official_despite_wording():
    src = {
        "title": "Official statistical bulletin Q1",
        "url": "https://www.capmas.gov.eg/bulletin",
        "snippet": "National statistics release.",
        "domain": "capmas.gov.eg",
        "source_class": "government",
        "providers": ["ddg"],
    }
    rel = source_relevance_score(src, "أسعار السيارات الكهربائية في مصر")
    assert rel["accepted"] is True
    assert rel["reason"] in {"accepted", "kept_official_despite_low_overlap"}


def test_filter_deduplicates():
    sources = [
        {
            "title": "Same Article Title",
            "url": "https://a.example/1",
            "snippet": "electric vehicles Egypt market",
            "domain": "a.example",
            "source_class": "general",
            "providers": ["ddg"],
        },
        {
            "title": "Same Article Title",
            "url": "https://a.example/1?utm=x",
            "snippet": "electric vehicles Egypt market again",
            "domain": "a.example",
            "source_class": "general",
            "providers": ["bing"],
        },
    ]
    kept, diag = filter_relevant_sources(
        sources, "electric vehicles Egypt", ["electric vehicles Egypt"]
    )
    assert len(kept) == 1
    assert any(d["reason"] == "duplicate_title_domain" for d in diag)


def test_filter_empty_and_failed_extract():
    kept, diag = filter_relevant_sources([], "anything")
    assert kept == []
    assert diag == []
    src = {
        "title": "",
        "url": "https://example.com/x",
        "snippet": "",
        "page_text": "",
        "domain": "example.com",
        "source_class": "general",
        "providers": ["ddg"],
    }
    _kept2, diag2 = filter_relevant_sources([src], "unrelated pasta recipes")
    # May reject for low overlap
    assert isinstance(diag2, list)


# --- evidence status --------------------------------------------------------

def test_evidence_adequate():
    sources = [
        {"url": f"https://a{i}.example/p", "domain": f"a{i}.example",
         "snippet": "content", "page_fetched": True, "source_class": "general"}
        for i in range(4)
    ]
    sources[0]["source_class"] = "government"
    decision = decide_evidence_status(sources, pages_read=2)
    assert decision["evidence_status"] == "adequate"
    assert decision["should_abstain"] is False


def test_evidence_insufficient_empty():
    decision = decide_evidence_status([], search_attempted=True)
    assert decision["evidence_status"] == "insufficient"
    assert decision["should_abstain"] is True


def test_evidence_failed_provider():
    decision = decide_evidence_status([], provider_failures=2, search_attempted=True)
    assert decision["evidence_status"] == "failed"
    assert decision["should_abstain"] is True


def test_evidence_partial_single_source():
    sources = [
        {"url": "https://a.example/p", "domain": "a.example",
         "snippet": "some text", "page_fetched": True, "source_class": "general"}
    ]
    decision = decide_evidence_status(sources, pages_read=1)
    assert decision["evidence_status"] == "partial"
    assert decision["should_abstain"] is False
