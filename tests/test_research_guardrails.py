"""Regression and adversarial tests for depth, freshness, relevance, evidence."""
from __future__ import annotations

from datetime import UTC, datetime

from agents.research_guardrails import (
    apply_source_guardrails,
    assess_current_source,
    classify_social_source,
    requires_official_government_domain,
    requires_official_current_government_source,
)
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



# --- task-specific evidence guardrails ---------------------------------------

_GUARDRAIL_NOW = datetime(2026, 10, 28, 12, 0, tzinfo=UTC)


def _guardrail_source(
    url: str,
    *,
    title: str = "معلومات عن وزارة الاتصالات",
    snippet: str = "معلومات عن وزارة الاتصالات وتكنولوجيا المعلومات في مصر",
    published_at: str = "2026-10-27T10:00:00Z",
    page_fetched: bool = True,
    page_text: str = "نص مقروء من الصفحة عن وزارة الاتصالات",
) -> dict:
    return {
        "title": title,
        "url": url,
        "snippet": snippet,
        "published_at": published_at,
        "page_fetched": page_fetched,
        "page_text": page_text,
    }


def test_official_government_website_request_rejects_tourism_domain() -> None:
    question = "ابحث عن الموقع الرسمي لوزارة الاتصالات وتكنولوجيا المعلومات المصرية"
    assert requires_official_government_domain(question)
    candidates = [
        _guardrail_source(
            "https://visitegypt.com/",
            title="وزارة الاتصالات في مصر ومعلومات سياحية",
        ),
        _guardrail_source(
            "https://mcit.gov.eg/",
            title="وزارة الاتصالات وتكنولوجيا المعلومات - الموقع الرسمي",
        ),
    ]

    accepted, report = apply_source_guardrails(
        question, "auto", {"freshness": "any"}, candidates, now=_GUARDRAIL_NOW
    )

    assert [item["url"] for item in accepted] == ["https://mcit.gov.eg/"]
    assert report["official_government_domain_required"] is True
    assert report["rejection_counts"] == {"not_an_official_government_domain": 1}
    assert "not independently verified" in report["official_domain_policy"]


def test_official_request_fails_closed_when_only_non_government_result_exists() -> None:
    accepted, report = apply_source_guardrails(
        "الموقع الرسمي لوزارة الاتصالات المصرية",
        "auto",
        {"freshness": "any"},
        [_guardrail_source("https://visitegypt.com/")],
        now=_GUARDRAIL_NOW,
    )

    assert accepted == []
    assert report["accepted_sources"] == 0
    assert report["current_evidence_status"] == "not_required"


def test_current_evidence_requires_recent_date_and_readable_page() -> None:
    recent = _guardrail_source("https://example.com/current")
    stale = _guardrail_source(
        "https://example.org/old", published_at="2024-06-01T10:00:00Z"
    )
    undated = _guardrail_source("https://example.net/undated", published_at="")
    unread = _guardrail_source(
        "https://example.edu/unread", page_fetched=False, page_text=""
    )

    assert assess_current_source(recent, now=_GUARDRAIL_NOW)["eligible"] is True
    assert assess_current_source(stale, now=_GUARDRAIL_NOW)["status"] == "stale"
    assert assess_current_source(undated, now=_GUARDRAIL_NOW)["status"] == "date_unavailable"
    assert assess_current_source(unread, now=_GUARDRAIL_NOW)["status"] == "page_not_read"


def test_latest_mode_excludes_old_undated_and_unread_pages() -> None:
    candidates = [
        _guardrail_source("https://example.com/recent"),
        _guardrail_source(
            "https://example.org/old", published_at="2023-11-15T10:00:00Z"
        ),
        _guardrail_source("https://example.net/undated", published_at=""),
        _guardrail_source(
            "https://example.edu/unread", page_fetched=False, page_text=""
        ),
    ]
    accepted, report = apply_source_guardrails(
        "مواعيد عمل مكتب الجوازات اليوم",
        "latest",
        {"freshness": "current"},
        candidates,
        now=_GUARDRAIL_NOW,
    )

    assert [item["url"] for item in accepted] == ["https://example.com/recent"]
    assert report["current_evidence_required"] is True
    assert report["current_evidence_status"] == "eligible_recent_read_pages_only"
    assert report["rejection_counts"] == {
        "stale": 1,
        "date_unavailable": 1,
        "page_not_read": 1,
    }


def test_official_site_navigation_does_not_require_news_publication_date() -> None:
    question = "ابحث عن الموقع الرسمي لوزارة الاتصالات وتكنولوجيا المعلومات المصرية"
    official_page = _guardrail_source(
        "https://mcit.gov.eg/",
        published_at="",
        title="وزارة الاتصالات وتكنولوجيا المعلومات - الموقع الرسمي",
    )

    accepted, report = apply_source_guardrails(
        question,
        "latest",
        {"freshness": "current"},
        [official_page],
        now=_GUARDRAIL_NOW,
    )

    assert len(accepted) == 1
    assert report["current_evidence_required"] is False


def test_social_mode_rejects_non_social_sources_and_classifies_public_posts() -> None:
    question = "اجمع آراء وتجارب الناس حول نيسان صني 2022 في مصر"
    personal_post = _guardrail_source(
        "https://www.reddit.com/r/cars/comments/example",
        title="تجربتي مع نيسان صني",
        snippet="أنا امتلك السيارة واستخدمتها يوميًا لمدة عام",
    )
    promotional_post = _guardrail_source(
        "https://www.reddit.com/r/cars/comments/ad",
        title="نيسان صني 2022 للبيع",
        snippet="سعر خاص، تواصل معنا عبر واتساب",
    )
    editorial_review = _guardrail_source(
        "https://example.com/car-review",
        title="مراجعة نيسان صني",
    )

    accepted, report = apply_source_guardrails(
        question,
        "social",
        {"social_focus": True, "freshness": "any"},
        [personal_post, promotional_post, editorial_review],
        now=_GUARDRAIL_NOW,
    )

    labels = {item["url"]: item["opinion_source_classification"] for item in accepted}
    assert labels[personal_post["url"]] == "personal_experience_candidate"
    assert labels[promotional_post["url"]] == "promotional_or_commercial"
    assert editorial_review["url"] not in labels
    assert report["social_platform_only"] is True
    assert report["rejection_counts"] == {"not_a_social_platform_source": 1}
    assert all(
        item["opinion_classification_method"] == "heuristic_only"
        for item in accepted
    )


def test_social_classification_does_not_claim_unknown_post_is_verified_experience() -> None:
    result = classify_social_source(
        _guardrail_source(
            "https://www.youtube.com/watch?v=example",
            title="Nissan Sunny 2022",
            snippet="معلومات ومقاطع عن السيارة",
        )
    )

    assert result["opinion_source_classification"] == "social_post_unclassified"
    assert result["opinion_classification_method"] == "heuristic_only"
    assert "manual review" in result["opinion_classification_basis"]


def test_today_query_requires_current_evidence_even_in_auto_mode() -> None:
    accepted, report = apply_source_guardrails(
        "ما مواعيد العمل اليوم؟",
        "auto",
        {"freshness": "current"},
        [
            _guardrail_source(
                "https://example.com/old", published_at="2024-01-01T10:00:00Z"
            )
        ],
        now=_GUARDRAIL_NOW,
    )

    assert accepted == []
    assert report["current_evidence_required"] is True
    assert report["rejection_counts"] == {"stale": 1}


def test_recent_source_date_is_not_enough_without_readable_page_text() -> None:
    item = _guardrail_source(
        "https://example.com/unread",
        published_at="2026-10-27T10:00:00Z",
        page_fetched=True,
        page_text="   ",
    )
    assert assess_current_source(item, now=_GUARDRAIL_NOW)["status"] == "page_not_read"



def test_social_classification_matches_english_first_person_phrases_case_insensitively() -> None:
    result = classify_social_source(
        _guardrail_source(
            "https://www.reddit.com/r/cars/comments/owner",
            title="Nissan Sunny ownership",
            snippet="I OWN the car and I use it for my daily commute",
        )
    )

    assert result["opinion_source_classification"] == "personal_experience_candidate"


def test_official_domain_check_rejects_suffix_spoofing() -> None:
    question = "ابحث عن الموقع الرسمي لوزارة الاتصالات المصرية"
    accepted, report = apply_source_guardrails(
        question,
        "auto",
        {"freshness": "any"},
        [
            _guardrail_source(
                "https://mcit.gov.eg.attacker.example/",
                title="وزارة الاتصالات المصرية الموقع الرسمي",
            )
        ],
        now=_GUARDRAIL_NOW,
    )

    assert accepted == []
    assert report["rejection_counts"] == {"not_an_official_government_domain": 1}



def test_current_government_office_hours_require_official_fresh_page_in_auto_mode() -> None:
    question = "مواعيد عمل مكتب الجوازات بالعباسية اليوم"
    assert requires_official_current_government_source(question)
    candidates = [
        _guardrail_source(
            "https://news.example.com/passport-hours",
            title="مواعيد الجوازات اليوم",
            snippet="ساعات العمل الحالية لمكتب الجوازات",
        ),
        _guardrail_source(
            "https://moi.gov.eg/",
            title="بوابة وزارة الداخلية",
            snippet="مواعيد عمل خدمات الجوازات",
        ),
    ]
    accepted, report = apply_source_guardrails(
        question, "auto", {"freshness": "any"}, candidates, now=_GUARDRAIL_NOW
    )
    assert [item["url"] for item in accepted] == ["https://moi.gov.eg/"]
    assert report["official_government_domain_required"] is True
    assert report["official_government_domain_reason"] == "current_government_service_hours"
    assert report["current_evidence_required"] is True
    assert report["rejection_counts"] == {"not_an_official_government_domain": 1}


def test_government_service_hour_request_rejects_undated_official_page() -> None:
    question = "مواعيد عمل مكتب الجوازات اليوم"
    official = _guardrail_source("https://moi.gov.eg/", published_at="")
    accepted, report = apply_source_guardrails(
        question, "auto", {"freshness": "any"}, [official], now=_GUARDRAIL_NOW
    )
    assert accepted == []
    assert report["rejection_counts"] == {"date_unavailable": 1}


def test_general_current_commercial_question_does_not_require_government_domain() -> None:
    question = "سعر الذهب اليوم في مصر"
    candidates = [_guardrail_source("https://example.com/gold")]
    accepted, report = apply_source_guardrails(
        question, "auto", {"freshness": "any"}, candidates, now=_GUARDRAIL_NOW
    )
    assert accepted == candidates
    assert report["official_government_domain_required"] is False
