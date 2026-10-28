from __future__ import annotations

import pytest

from agents.task_understanding import build_query_strategy_matrix, build_task_spec


@pytest.mark.parametrize(
    ("question", "family"),
    [
        ("ابحث عن الموقع الرسمي لوزارة الاتصالات في مصر", "official_site_lookup"),
        ("مواعيد عمل مكتب الجوازات اليوم في العباسية", "current_information"),
        ("قارن نيسان صني 2022 وهيونداي أكسنت من حيث السعر والصيانة", "compare"),
        ("عايز تجارب ملاك BYD Dolphin في مصر", "social_opinions"),
        ("ازاي أصلح خطأ الشبكة في لوحة إنذار الحريق؟", "troubleshoot"),
        ("اشرح خطوات صيانة حساس الدخان", "how_to"),
        ("لخص الصفحة https://example.com/article", "summarize"),
        ("ابحث عن مشترين يريدون شراء شقة في القاهرة", "lead_generation"),
        ("رشح لي أفضل سيارة بميزانية أقل من 500000 جنيه", "recommendation"),
        ("ما معنى نظام الإنذار المعنون؟", "explain_or_define"),
    ],
)
def test_task_family_covers_diverse_natural_language_patterns(question, family):
    spec = build_task_spec(question, mode="auto", intent_route="WEB_SIMPLE")
    assert spec["task_family"] == family
    assert spec["classification_is_probability"] is False
    assert spec["decision_checks"]


def test_task_spec_preserves_only_explicit_constraints():
    spec = build_task_spec(
        "قارن نيسان صني 2022 مع BYD Dolphin في مصر، بميزانية أقل من 400 ألف جنيه",
        mode="deep",
        intent_route="WEB_DEEP",
    )
    constraints = spec["constraints"]
    assert "2022" in constraints["explicit_years"]
    assert "مصر" in constraints["explicit_locations"]
    assert constraints["explicit_budgets"]
    assert constraints["language_profile"] in {"ar", "mixed"}


def test_latest_mode_requires_current_evidence_for_stateful_facts():
    spec = build_task_spec(
        "مواعيد عمل مكتب الجوازات اليوم",
        mode="latest",
        intent_route="WEB_SIMPLE",
    )
    assert spec["constraints"]["time_sensitive_request"] is True
    assert "page_text_successfully_read" in spec["evidence_requirements"]
    assert "date_check" in spec["query_strategies"]


def test_official_site_navigation_is_not_misclassified_as_current_news():
    spec = build_task_spec(
        "ابحث عن الموقع الرسمي لوزارة الاتصالات في مصر",
        mode="latest",
        intent_route="WEB_SIMPLE",
    )
    assert spec["task_family"] == "official_site_lookup"
    assert spec["constraints"]["official_site_required"] is True
    assert spec["constraints"]["time_sensitive_request"] is False


def test_social_request_separates_experience_from_truth_verification():
    spec = build_task_spec(
        "أريد آراء وتجارب ملاك نيسان صني 2022 في مصر",
        mode="social",
        intent_route="WEB_DEEP",
    )
    assert spec["constraints"]["social_evidence_requested"] is True
    assert "heuristic_classification_is_not_identity_or_truth_verification" in spec["evidence_requirements"]
    assert "personal_experience" in spec["query_strategies"]


def test_ambiguous_followup_is_not_reported_as_a_confident_interpretation():
    spec = build_task_spec(
        "كام سعرها؟",
        mode="auto",
        intent_route="CLARIFY",
        dialogue_context={"needs_clarification": True},
    )
    assert spec["task_family"] == "ambiguous_or_incomplete"
    assert spec["ambiguity_status"] == "needs_clarification"


def test_query_strategy_matrix_is_bounded_deduplicated_and_topic_anchored():
    spec = build_task_spec(
        "قارن السيارات الكهربائية في مصر من حيث السعر والضمان",
        mode="deep",
        intent_route="WEB_DEEP",
    )
    rows = build_query_strategy_matrix(
        "قارن السيارات الكهربائية في مصر من حيث السعر والضمان",
        spec,
        ["السيارات الكهربائية في مصر", "السيارات الكهربائية في مصر"],
        limit=6,
    )
    queries = [row["query"] for row in rows]
    assert 1 <= len(queries) <= 6
    assert len({query.casefold() for query in queries}) == len(queries)
    assert all("السيارات" in query for query in queries)
    assert any(row["strategy"] == "primary_specification" for row in rows)
    assert all(row["rationale"] for row in rows)


def test_strategy_matrix_does_not_create_generic_queries_without_topic():
    spec = build_task_spec("قارنهم", mode="deep", intent_route="CLARIFY")
    rows = build_query_strategy_matrix("قارنهم", spec, [], limit=8)
    assert rows == []


def test_mixed_language_is_supported_and_urls_are_explicit_constraints():
    spec = build_task_spec(
        "Compare Nissan Sunny 2022 with BYD Dolphin في مصر https://example.com/specs",
        mode="auto",
        intent_route="WEB_DEEP",
    )
    assert spec["constraints"]["language_profile"] == "mixed"
    assert spec["constraints"]["explicit_urls"] == ["https://example.com/specs"]
    assert "2022" in spec["constraints"]["explicit_years"]


def test_task_spec_validator_does_not_accept_untrusted_arbitrary_objects():
    from agents.task_understanding import validate_task_spec

    invalid = validate_task_spec({"schema": "wrong", "tool_requirements": ["delete files"]})
    assert invalid["status"] == "not_available"


def test_compound_task_keeps_current_social_and_comparison_requirements_together():
    spec = build_task_spec(
        "قارن تجارب ملاك نيسان صني 2022 في مصر اليوم من حيث السعر والأعطال",
        mode="social",
        intent_route="WEB_DEEP",
    )
    assert spec["task_family"] in {"social_opinions", "compare"}
    assert spec["constraints"]["time_sensitive_request"] is True
    assert spec["constraints"]["social_evidence_requested"] is True
    assert "publication_or_update_date" in spec["evidence_requirements"]
    assert "preserve_explicit_comparison_criteria" in spec["evidence_requirements"] or "preserve_each_explicit_comparison_criterion" in spec["evidence_requirements"]
    assert "personal_experience" in spec["query_strategies"]
    assert "date_check" in spec["query_strategies"]


def test_alarm_word_does_not_trigger_current_information_pattern():
    spec = build_task_spec("ما معنى نظام الإنذار المعنون؟", mode="auto", intent_route="MODEL_ONLY")
    assert spec["constraints"]["time_sensitive_request"] is False
    assert spec["task_family"] == "explain_or_define"
