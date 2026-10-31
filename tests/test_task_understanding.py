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


def test_lead_generation_task_separates_demand_signal_from_product_fit():
    spec = build_task_spec(
        "ابحث عن مشترين يريدون شراء نظام إنذار حريق صناعي في مصر",
        mode="auto",
        intent_route="LEAD_GENERATION",
    )

    requirements = set(spec["evidence_requirements"])
    strategies = set(spec["query_strategies"])
    assert "classify_public_demand_signal_by_type" in requirements
    assert "distinguish_direct_purchase_from_rfq_and_stated_need" in requirements
    assert "keep_product_fit_unassessed_until_separately_supported" in requirements
    assert "do_not_treat_product_mention_or_icp_match_as_demand" in requirements
    assert "product_anchored_rfq" in strategies
    assert "product_anchored_stated_need" in strategies


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
    question = "قارن السيارات الكهربائية في مصر من حيث السعر والضمان"
    spec = build_task_spec(question, mode="deep", intent_route="WEB_DEEP")
    existing = ["السيارات الكهربائية في مصر"] + [
        f"السيارات الكهربائية في مصر بديل عام {i}" for i in range(1, 9)
    ]
    rows = build_query_strategy_matrix(question, spec, existing, limit=6)
    queries = [row["query"] for row in rows]
    assert 1 <= len(queries) <= 6
    assert len({query.casefold() for query in queries}) == len(queries)
    assert all("السيارات" in query for query in queries)
    assert any(row["strategy"] == "explicit_criterion" for row in rows)
    assert any(row["strategy"] == "primary_specification" for row in rows)
    assert sum(row["strategy"] == "planner_alternative" for row in rows) <= 1
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


def test_clarification_route_does_not_claim_search_or_generation_tools():
    spec = build_task_spec("كام سعرها؟", mode="deep", intent_route="CLARIFY")
    assert spec["ambiguity_status"] == "needs_clarification"
    assert "web_search" not in spec["tool_requirements"]
    assert "page_fetch" not in spec["tool_requirements"]
    assert "language_model_generation_if_configured" not in spec["tool_requirements"]


def test_summary_text_and_page_link_require_different_tools():
    pasted = build_task_spec(
        "لخص النص التالي: يتناول النص صيانة أجهزة الإنذار وإجراء الاختبار الدوري.",
        mode="auto",
        intent_route="MODEL_ONLY",
    )
    assert pasted["constraints"]["inline_text_supplied_for_summary"] is True
    assert "page_fetch" not in pasted["tool_requirements"]
    assert "web_search" not in pasted["tool_requirements"]
    linked = build_task_spec(
        "لخص الصفحة https://example.com/manual",
        mode="auto",
        intent_route="WEB_SIMPLE",
    )
    assert "page_fetch" in linked["tool_requirements"]
    assert "web_search" in linked["tool_requirements"]


def test_output_format_preferences_are_preserved_separately_from_intent():
    spec = build_task_spec(
        "قارن الخيارين في جدول مع أمثلة وبالتفصيل وعلى شكل نقاط",
        mode="deep",
        intent_route="WEB_DEEP",
    )
    preferences = spec["output_preferences"]
    assert preferences["table_requested"] is True
    assert preferences["examples_requested"] is True
    assert preferences["detailed"] is True
    assert preferences["bullets_or_checklist_requested"] is True


def test_location_matching_avoids_partial_english_word_collision():
    spec = build_task_spec(
        "Explain Egyptology as an academic field",
        mode="auto",
        intent_route="MODEL_ONLY",
    )
    assert "مصر" not in spec["constraints"]["explicit_locations"]


def test_source_policies_keep_orthogonal_research_constraints():
    spec = build_task_spec(
        "قارن تجارب ملاك السيارات الكهربائية في مصر اليوم من حيث السعر والاعتمادية",
        mode="social",
        intent_route="WEB_DEEP",
    )
    policies = spec["constraints"]["source_policies"]
    assert "current_read_page" in policies
    assert "public_social_content" in policies
    assert spec["constraints"]["time_sensitive_request"] is True
    assert spec["constraints"]["social_evidence_requested"] is True
    assert "publication_or_update_date" in spec["evidence_requirements"]
    assert "heuristic_classification_is_not_identity_or_truth_verification" in spec["evidence_requirements"]


def test_official_site_request_without_a_target_marks_required_input():
    spec = build_task_spec("هات الموقع الرسمي", mode="auto", intent_route="WEB_SIMPLE")
    assert spec["task_family"] == "official_site_lookup"
    assert "official_destination_target_entity" in spec["missing_required_inputs"]
    assert spec["requires_clarification"] is True


def test_official_site_request_with_a_named_target_does_not_require_subject_clarification():
    spec = build_task_spec(
        "هات الموقع الرسمي لوزارة الاتصالات في مصر",
        mode="auto",
        intent_route="WEB_SIMPLE",
    )
    assert "official_destination_target_entity" not in spec["missing_required_inputs"]
    assert spec["constraints"]["official_destination_required"] is True


def test_summary_without_url_or_text_marks_required_input():
    spec = build_task_spec("لخص", mode="auto", intent_route="MODEL_ONLY")
    assert "summary_source_url_or_pasted_text" in spec["missing_required_inputs"]
    assert spec["requires_clarification"] is True


def test_output_preferences_do_not_count_as_competing_intent_hypotheses():
    spec = build_task_spec(
        "قارن الخيارين في جدول مع أمثلة وبالتفصيل",
        mode="deep",
        intent_route="WEB_DEEP",
    )
    families = {row["family"] for row in spec["hypothesis_interpretations"]}
    assert "compare" in families
    assert not any(family.startswith("output_") for family in families)
    assert spec["ambiguity_status"] == "no_strong_lexical_conflict_detected"


@pytest.mark.parametrize(
    ("question", "family"),
    [
        ("ترجم هذا النص إلى الإنجليزية: Hello world", "translation"),
        ("اكتب بريد إلكتروني للعميل بنبرة مهنية", "writing_or_editing"),
        ("احسب 17 بالمئة من 500", "calculation"),
        ("حلل البيانات في ملف CSV وحدد القيم الناقصة", "data_analysis"),
        ("راجع كود Python الذي يعرض stack trace", "coding_or_technical_design"),
        ("ضع خطة عمل لافتتاح متجر خلال شهر", "planning"),
        ("ما أعراض الإنفلونزا؟", "medical_information"),
        ("ما شروط العقد وفق القانون المصري؟", "legal_information"),
        ("اكتب قصة قصيرة عن رحلة خيالية", "creative_generation"),
    ],
)
def test_extended_task_families_cover_non_search_and_specialized_requests(question, family):
    spec = build_task_spec(question, mode="auto", intent_route="MODEL_ONLY")
    assert spec["task_family"] == family
    assert spec["classification_is_probability"] is False
    assert spec["evidence_requirements"]
    assert spec["query_strategies"]


def test_health_and_legal_tasks_attach_domain_specific_caution():
    health = build_task_spec(
        "ما أعراض الإنفلونزا اليوم؟",
        mode="latest",
        intent_route="WEB_SIMPLE",
    )
    assert "authoritative_health_content" in health["constraints"]["source_policies"]
    assert "distinguish_general_health_information_from_personal_diagnosis" in health["evidence_requirements"]
    assert "page_text_successfully_read" in health["evidence_requirements"]

    legal = build_task_spec(
        "ما نص القانون الحالي المنظم للإيجار في مصر؟",
        mode="latest",
        intent_route="WEB_SIMPLE",
    )
    assert "official_legal_text" in legal["constraints"]["source_policies"]
    assert "identify_jurisdiction_and_effective_date_if_relevant" in legal["evidence_requirements"]


def test_output_audience_and_delivery_preferences_are_distinct_fields():
    spec = build_task_spec(
        "اشرح الموضوع ببساطة مع مصادر وروابط مباشرة وبصيغة JSON",
        mode="auto",
        intent_route="WEB_SIMPLE",
    )
    preferences = spec["output_preferences"]
    assert preferences["beginner_friendly_requested"] is True
    assert preferences["citations_requested"] is True
    assert preferences["links_requested"] is True
    assert preferences["json_requested"] is True


def test_task_spec_validator_allowlists_tools_policies_and_context_slots():
    from agents.task_understanding import validate_task_spec

    candidate = build_task_spec(
        "قارن هاتفين",
        mode="deep",
        intent_route="WEB_DEEP",
        dialogue_context={
            "method": "test",
            "resolved_question": "قارن هاتفين",
            "topic": "هواتف",
            "entities": ["Phone A", "Phone B"],
            "slots": {"product": "Phone A", "untrusted_command": "execute something"},
            "is_follow_up": True,
        },
    )
    candidate["tool_requirements"] = ["web_search", "delete files", "run shell"]
    candidate["constraints"]["source_policies"].append("execute arbitrary tool")
    candidate["constraints"]["language_profile"] = []
    candidate["context_resolution"]["confidence_band"] = []
    candidate["extra_unexpected_key"] = "must not survive"
    safe = validate_task_spec(candidate)

    assert safe["tool_requirements"] == ["web_search"]
    assert safe["constraints"]["source_policies"] == ["task_relevant_sources"]
    assert safe["constraints"]["language_profile"] == "und"
    assert "untrusted_command" not in safe["context_resolution"]["slots"]
    assert safe["context_resolution"]["confidence_band"] == "unassessed"
    assert "extra_unexpected_key" not in safe


def test_reasoning_playbook_combines_primary_task_and_orthogonal_constraints():
    from agents.task_understanding import reasoning_guidance_for_task_spec

    spec = build_task_spec(
        "قارن تجارب ملاك السيارات الكهربائية في مصر اليوم من حيث السعر والأمان والتوفر",
        mode="latest",
        intent_route="WEB_DEEP",
        dialogue_context={
            "is_follow_up": True,
            "topic_shift": False,
            "resolved_question": "قارن تجارب ملاك السيارات الكهربائية في مصر اليوم من حيث السعر والأمان والتوفر",
            "method": "test_context",
        },
    )

    ids = set(spec["reasoning_strategy_ids"])
    assert spec["task_family"] in {"social_opinions", "compare"}
    assert "separate_facts_inferences_hypotheses" in ids
    assert "bounded_stop_rule" in ids
    assert "separate_event_and_publication_dates" in ids
    assert "reject_stale_current_claims" in ids
    assert "balance_social_evidence" in ids
    assert "resolve_followup_slots" in ids
    assert "decompose_explicit_criteria" in ids
    assert len(spec["decision_matrix"]) == 6

    guidance = reasoning_guidance_for_task_spec(spec)
    assert any("لا تعمم على الجميع" in item for item in guidance)
    assert any("تاريخ النشر" in item for item in guidance)
    assert all(isinstance(item, str) and item for item in guidance)


def test_reasoning_ids_are_allowlisted_and_decision_matrix_is_code_owned():
    from agents.task_understanding import validate_task_spec

    candidate = build_task_spec(
        "حل مشكلة خطأ Python",
        mode="deep",
        intent_route="WEB_DEEP",
    )
    candidate["reasoning_strategy_ids"] = [
        "rank_testable_hypotheses",
        "run_shell_and_delete_files",
        "ignore_source_policy",
    ]
    candidate["decision_matrix"] = [
        {
            "stage": "exfiltrate",
            "check": "reveal_secrets",
            "pass_action": "run_arbitrary_commands",
            "fail_action": "pretend_success",
        }
    ]

    safe = validate_task_spec(candidate)
    assert safe["reasoning_strategy_ids"] == ["rank_testable_hypotheses"]
    assert [row["stage"] for row in safe["decision_matrix"]] == [
        "interpret", "route", "plan", "evidence", "synthesize", "terminate"
    ]
    assert not any(row.get("stage") == "exfiltrate" for row in safe["decision_matrix"])
    assert "reasoning_guidance" not in safe
