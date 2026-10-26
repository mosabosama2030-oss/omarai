from __future__ import annotations

from agents.research import (
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


def test_follow_up_query_keeps_prior_topic():
    history = [{"role": "user", "content": "قارن سوق السيارات الكهربائية في مصر"}]
    plan = fallback_plan("وطب الأسعار الحالية؟", history)
    assert "السيارات الكهربائية" in plan["queries"][0]
    assert plan["freshness"] == "current"


def test_plan_validation_caps_queries_and_rejects_non_string_values():
    candidate = {
        "queries": ["بحث أ", "بحث ب", None, "بحث ج", "بحث د", "بحث هـ", "بحث سادس", "بحث سابع", "بحث ثامن", "بحث تاسع"],
        "social_focus": True,
        "freshness": "current",
        "depth": "deep",
        "platforms": ["reddit", "unknown"],
    }
    plan = validate_plan(candidate, "بحث عن منشورات")
    assert len(plan["queries"]) <= 8
    assert "unknown" not in plan["platforms"]
    assert plan["social_focus"] is True
    assert plan["freshness"] == "current"


def test_rank_fusion_promotes_cross_provider_consensus_and_deduplicates():
    batches = [
        {
            "query": "cars Egypt",
            "provider": "ddg",
            "results": [
                {"title": "A", "url": "https://www.example.com/a?utm_source=x", "snippet": "A"},
                {"title": "B", "url": "https://example.com/b", "snippet": "B"},
            ],
        },
        {
            "query": "electric vehicles Egypt",
            "provider": "bing",
            "results": [
                {"title": "A better title", "url": "https://example.com/a", "snippet": "Longer evidence snippet"},
                {"title": "C", "url": "https://example.com/c", "snippet": "C"},
            ],
        },
    ]
    ranked = fuse_ranked_results(batches)
    urls = [source["url"] for source in ranked]
    assert len(urls) == 3
    source_a = next(source for source in ranked if "example.com/a" in source["url"])
    assert len(source_a["providers"]) == 2
    assert len(source_a["queries"]) == 2
    assert source_a["rank_score"] > next(
        source["rank_score"] for source in ranked if "example.com/c" in source["url"]
    )


def test_source_classification_distinguishes_social_and_government():
    from agents.research import classify_source

    assert classify_source("https://www.reddit.com/r/example/comments/1")["platform"] == "reddit"
    assert classify_source("https://example.gov.eg/page")["source_class"] == "government"


def test_explicit_page_urls_are_extracted_and_not_left_in_search_terms():
    from agents.research import extract_urls

    question = "حلل هذه الصفحة بالتفصيل https://example.com/a?utm_source=chat#section."
    plan = fallback_plan(question)
    assert extract_urls(question) == ["https://example.com/a?utm_source=chat#section"]
    assert plan["direct_urls"] == ["https://example.com/a?utm_source=chat#section"]
    assert "https://" not in plan["queries"][0]

def test_registrable_domain_groups_subdomains_and_respects_public_suffixes():
    assert registrable_domain("news.example.com") == "example.com"
    assert registrable_domain("offers.example.com") == "example.com"
    assert registrable_domain("news.example.co.uk") == "example.co.uk"
    assert registrable_domain("other.co.uk") == "other.co.uk"
    assert registrable_domain("alice.github.io") == "alice.github.io"
    assert registrable_domain("https://www.example.com/path") == "example.com"


def test_evidence_coverage_does_not_count_sibling_subdomains_as_independent():
    report = evidence_signal_report([
        {
            "url": "https://news.example.com/story",
            "domain": "news.example.com",
            "providers": ["search_a"],
        },
        {
            "url": "https://offers.example.com/second-story",
            "domain": "offers.example.com",
            "providers": ["search_b"],
        },
    ])
    assert report["unique_domains"] == 1
    assert report["coverage_level"] == "محدود"



def test_standard_fallback_plan_does_not_add_deep_research_query():
    plan = fallback_plan("اشرح طريقة عمل المحرك الكهربائي")
    assert plan["depth"] == "standard"
    assert not any("مصادر موثوقة تقارير إحصاءات" in query for query in plan["queries"])


def test_deep_fallback_plan_adds_deep_research_query_for_explicit_comparison():
    plan = fallback_plan("قارن مميزات وعيوب المحرك الكهربائي")
    assert plan["depth"] == "deep"
    assert any("مصادر موثوقة تقارير إحصاءات" in query for query in plan["queries"])


def test_fallback_plan_expands_warranty_followup_with_previous_topic():
    history = [
        {"role": "user", "content": "سعر آيفون 16 في مصر"},
        {"role": "assistant", "content": "سأبحث عن معلومات حديثة."},
    ]
    plan = fallback_plan("هل فيه ضمان؟", history)
    assert "آيفون 16" in plan["queries"][0]
    assert "ضمان" in plan["queries"][0]


def test_fallback_plan_does_not_reuse_topic_after_acknowledgment():
    history = [
        {"role": "user", "content": "سعر آيفون 16 في مصر"},
        {"role": "assistant", "content": "سأبحث عن معلومات حديثة."},
        {"role": "user", "content": "شكرًا"},
        {"role": "assistant", "content": "العفو."},
    ]
    plan = fallback_plan("فين؟", history)
    assert "آيفون 16" not in plan["queries"][0]

def test_fallback_plan_compacts_arabic_questions_before_expansion():
    capital = fallback_plan(
        "ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز."
    )
    assert "عاصمة" in capital["queries"][0]
    assert "مصر" in capital["queries"][0]
    assert "اذكر مصدرًا" not in capital["queries"][0]
    assert "بإيجاز" not in capital["queries"][0]
    assert len(capital["queries"][0]) <= 240

    ev = fallback_plan(
        "حلّل أهم التحديات التي تواجه السيارات الكهربائية في مصر، وقارن بين "
        "التكلفة والبنية التحتية والشحن. استخدم مصادر متعددة، وميّز بين "
        "الحقائق والاستنتاجات، واذكر روابط المصادر."
    )
    assert "السيارات الكهربائية" in ev["queries"][0]
    assert "الشحن" in ev["queries"][0]
    assert "استخدم مصادر متعددة" not in ev["queries"][0]
    assert all(len(query) <= 240 for query in ev["queries"])


def test_compact_search_query_preserves_site_operator_and_social_sentiment():
    question = (
        "اجمع آراء وتجارب المستخدمين العامة حول السيارات الكهربائية في مصر. "
        "اعرض الآراء الإيجابية والسلبية، واذكر روابط المنشورات أو المصادر المتاحة. "
        "وضّح إذا كانت النتائج غير كافية لتمثيل آراء المستخدمين عمومًا."
    )
    query = compact_search_query(question)
    assert "السيارات الكهربائية" in query
    assert "مصر" in query
    assert "الإيجابية والسلبية" in query
    assert "وضّح إذا" not in query
    assert len(query) <= 240

    social_query = compact_search_query(
        'site:reddit.com "electric car reviews Egypt" cite the original posts'
    )
    assert social_query.startswith("site:reddit.com")
    assert "electric car reviews Egypt" in social_query
    assert len(social_query) <= 240
