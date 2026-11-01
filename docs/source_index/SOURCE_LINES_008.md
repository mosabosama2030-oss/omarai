# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **008**
- سجلات الأسطر: **800**
- النطاق: SRC-686F71AA50-L000858 إلى SRC-0799EEEB02-L000199
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-686F71AA50 — [agents/task_understanding.py](../../agents/task_understanding.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-686F71AA50-L000858](../../agents/task_understanding.py#L858) | 858 | `"            + ([\"public_social_content\"] if social_required else [])"` | — |
| [SRC-686F71AA50-L000859](../../agents/task_understanding.py#L859) | 859 | `"            + ([\"authoritative_health_content\"] if matches[\"medical_information\"] else [])"` | — |
| [SRC-686F71AA50-L000860](../../agents/task_understanding.py#L860) | 860 | `"            + ([\"official_legal_text\"] if matches[\"legal_information\"] else [])"` | — |
| [SRC-686F71AA50-L000861](../../agents/task_understanding.py#L861) | 861 | `"            + ([\"task_relevant_sources\"] if not (government_official_site or official_destination or current_required or social_required or matches[\"medical_information\"] or matches[\"legal_information\"]) else [])"` | — |
| [SRC-686F71AA50-L000862](../../agents/task_understanding.py#L862) | 862 | `"        )),"` | — |
| [SRC-686F71AA50-L000863](../../agents/task_understanding.py#L863) | 863 | `"    }"` | — |
| [SRC-686F71AA50-L000864](../../agents/task_understanding.py#L864) | 864 | `"    spec = {"` | — |
| [SRC-686F71AA50-L000865](../../agents/task_understanding.py#L865) | 865 | `"        \"schema\": \"omarai.task_spec.v1\","` | — |
| [SRC-686F71AA50-L000866](../../agents/task_understanding.py#L866) | 866 | `"        \"task_family\": family,"` | — |
| [SRC-686F71AA50-L000867](../../agents/task_understanding.py#L867) | 867 | `"        \"mode\": clean_mode,"` | — |
| [SRC-686F71AA50-L000868](../../agents/task_understanding.py#L868) | 868 | `"        \"intent_route\": intent_route or \"unassessed\","` | — |
| [SRC-686F71AA50-L000869](../../agents/task_understanding.py#L869) | 869 | `"        \"normalization\": \"unicode_nfkc_arabic_diacritic_and_letter_normalization\","` | — |
| [SRC-686F71AA50-L000870](../../agents/task_understanding.py#L870) | 870 | `"        \"classification_method\": \"deterministic_multi_pattern_hypotheses\","` | — |
| [SRC-686F71AA50-L000871](../../agents/task_understanding.py#L871) | 871 | `"        \"classification_is_probability\": False,"` | — |
| [SRC-686F71AA50-L000872](../../agents/task_understanding.py#L872) | 872 | `"        \"ambiguity_status\": ambiguity_status,"` | — |
| [SRC-686F71AA50-L000873](../../agents/task_understanding.py#L873) | 873 | `"        \"missing_required_inputs\": list(dict.fromkeys(missing_required_inputs)),"` | — |
| [SRC-686F71AA50-L000874](../../agents/task_understanding.py#L874) | 874 | `"        \"requires_clarification\": ambiguity_status == \"needs_clarification\","` | — |
| [SRC-686F71AA50-L000875](../../agents/task_understanding.py#L875) | 875 | `"        \"context_resolution\": context_resolution,"` | — |
| [SRC-686F71AA50-L000876](../../agents/task_understanding.py#L876) | 876 | `"        \"secondary_task_types\": ["` | — |
| [SRC-686F71AA50-L000877](../../agents/task_understanding.py#L877) | 877 | `"            name for name, signals in matches.items()"` | — |
| [SRC-686F71AA50-L000878](../../agents/task_understanding.py#L878) | 878 | `"            if signals and name != family"` | — |
| [SRC-686F71AA50-L000879](../../agents/task_understanding.py#L879) | 879 | `"        ],"` | — |
| [SRC-686F71AA50-L000880](../../agents/task_understanding.py#L880) | 880 | `"        \"clarification_reason\": ("` | — |
| [SRC-686F71AA50-L000881](../../agents/task_understanding.py#L881) | 881 | `"            \"missing_required_input\""` | — |
| [SRC-686F71AA50-L000882](../../agents/task_understanding.py#L882) | 882 | `"            if missing_required_inputs"` | — |
| [SRC-686F71AA50-L000883](../../agents/task_understanding.py#L883) | 883 | `"            else \"no_strong_lexical_conflict_detected\""` | — |
| [SRC-686F71AA50-L000884](../../agents/task_understanding.py#L884) | 884 | `"        ),"` | — |
| [SRC-686F71AA50-L000885](../../agents/task_understanding.py#L885) | 885 | `"        \"hypothesis_interpretations\": hypothesis_rows,"` | — |
| [SRC-686F71AA50-L000886](../../agents/task_understanding.py#L886) | 886 | `"        \"constraints\": constraints,"` | — |
| [SRC-686F71AA50-L000887](../../agents/task_understanding.py#L887) | 887 | `"        \"output_preferences\": {"` | — |
| [SRC-686F71AA50-L000888](../../agents/task_understanding.py#L888) | 888 | `"            \"concise\": bool(output_matches[\"output_concise\"]),"` | — |
| [SRC-686F71AA50-L000889](../../agents/task_understanding.py#L889) | 889 | `"            \"detailed\": bool(output_matches[\"output_detailed\"]),"` | — |
| [SRC-686F71AA50-L000890](../../agents/task_understanding.py#L890) | 890 | `"            \"examples_requested\": bool(output_matches[\"output_examples\"]),"` | — |
| [SRC-686F71AA50-L000891](../../agents/task_understanding.py#L891) | 891 | `"            \"table_requested\": bool(output_matches[\"output_table\"]),"` | — |
| [SRC-686F71AA50-L000892](../../agents/task_understanding.py#L892) | 892 | `"            \"bullets_or_checklist_requested\": bool(output_matches[\"output_bullets\"]),"` | — |
| [SRC-686F71AA50-L000893](../../agents/task_understanding.py#L893) | 893 | `"            \"beginner_friendly_requested\": bool(output_matches[\"output_beginner_friendly\"]),"` | — |
| [SRC-686F71AA50-L000894](../../agents/task_understanding.py#L894) | 894 | `"            \"citations_requested\": bool(output_matches[\"output_citations\"]),"` | — |
| [SRC-686F71AA50-L000895](../../agents/task_understanding.py#L895) | 895 | `"            \"links_requested\": bool(output_matches[\"output_links\"]),"` | — |
| [SRC-686F71AA50-L000896](../../agents/task_understanding.py#L896) | 896 | `"            \"json_requested\": bool(output_matches[\"output_json\"]),"` | — |
| [SRC-686F71AA50-L000897](../../agents/task_understanding.py#L897) | 897 | `"        },"` | — |
| [SRC-686F71AA50-L000898](../../agents/task_understanding.py#L898) | 898 | `"        \"evidence_requirements\": evidence_requirements,"` | — |
| [SRC-686F71AA50-L000899](../../agents/task_understanding.py#L899) | 899 | `"        \"query_strategies\": query_strategies,"` | — |
| [SRC-686F71AA50-L000900](../../agents/task_understanding.py#L900) | 900 | `"        \"tool_requirements\": list(dict.fromkeys(tools)),"` | — |
| [SRC-686F71AA50-L000901](../../agents/task_understanding.py#L901) | 901 | `"        \"decision_checks\": ["` | — |
| [SRC-686F71AA50-L000902](../../agents/task_understanding.py#L902) | 902 | `"            \"resolve_context_without_carrying_stale_topic\","` | — |
| [SRC-686F71AA50-L000903](../../agents/task_understanding.py#L903) | 903 | `"            \"preserve_explicit_entities_and_constraints\","` | — |
| [SRC-686F71AA50-L000904](../../agents/task_understanding.py#L904) | 904 | `"            \"validate_topic_relevance\","` | — |
| [SRC-686F71AA50-L000905](../../agents/task_understanding.py#L905) | 905 | `"            \"check_tool_permission_and_configuration_before_execution\","` | — |
| [SRC-686F71AA50-L000906](../../agents/task_understanding.py#L906) | 906 | `"            \"bound_query_count_retries_concurrency_and_deadlines\","` | — |
| [SRC-686F71AA50-L000907](../../agents/task_understanding.py#L907) | 907 | `"            \"treat_retrieved_content_as_untrusted_data_not_tool_instructions\","` | — |
| [SRC-686F71AA50-L000908](../../agents/task_understanding.py#L908) | 908 | `"            \"apply_mode_specific_source_guardrails\","` | — |
| [SRC-686F71AA50-L000909](../../agents/task_understanding.py#L909) | 909 | `"            \"distinguish_planned_queries_from_queries_actually_attempted\","` | — |
| [SRC-686F71AA50-L000910](../../agents/task_understanding.py#L910) | 910 | `"            \"distinguish_search_snippets_from_successfully_read_pages\","` | — |
| [SRC-686F71AA50-L000911](../../agents/task_understanding.py#L911) | 911 | `"            \"separate_connector_success_from_evidence_validity\","` | — |
| [SRC-686F71AA50-L000912](../../agents/task_understanding.py#L912) | 912 | `"            \"report_each_failed_stage_without_claiming_unperformed_checks\","` | — |
| [SRC-686F71AA50-L000913](../../agents/task_understanding.py#L913) | 913 | `"            \"cite_claims_or_abstain_when_evidence_is_insufficient\","` | — |
| [SRC-686F71AA50-L000914](../../agents/task_understanding.py#L914) | 914 | `"        ],"` | — |
| [SRC-686F71AA50-L000915](../../agents/task_understanding.py#L915) | 915 | `"        \"reasoning_strategy_ids\": _reasoning_strategy_ids("` | — |
| [SRC-686F71AA50-L000916](../../agents/task_understanding.py#L916) | 916 | `"            family, constraints, context_resolution, missing_required_inputs"` | — |
| [SRC-686F71AA50-L000917](../../agents/task_understanding.py#L917) | 917 | `"        ),"` | — |
| [SRC-686F71AA50-L000918](../../agents/task_understanding.py#L918) | 918 | `"        \"decision_matrix\": [dict(row) for row in _DECISION_MATRIX],"` | — |
| [SRC-686F71AA50-L000919](../../agents/task_understanding.py#L919) | 919 | `"        \"limits\": {"` | — |
| [SRC-686F71AA50-L000920](../../agents/task_understanding.py#L920) | 920 | `"            \"max_question_chars\": MAX_TASK_CHARS,"` | — |
| [SRC-686F71AA50-L000921](../../agents/task_understanding.py#L921) | 921 | `"            \"max_aspects\": MAX_TASK_ASPECTS,"` | — |
| [SRC-686F71AA50-L000922](../../agents/task_understanding.py#L922) | 922 | `"            \"max_query_strategies\": MAX_STRATEGY_QUERIES,"` | — |
| [SRC-686F71AA50-L000923](../../agents/task_understanding.py#L923) | 923 | `"        },"` | — |
| [SRC-686F71AA50-L000924](../../agents/task_understanding.py#L924) | 924 | `"        \"claim\": \"task planning metadata only; not semantic certainty or factual verification\","` | — |
| [SRC-686F71AA50-L000925](../../agents/task_understanding.py#L925) | 925 | `"    }"` | — |
| [SRC-686F71AA50-L000926](../../agents/task_understanding.py#L926) | 926 | `"    if plan and isinstance(plan, dict):"` | — |
| [SRC-686F71AA50-L000927](../../agents/task_understanding.py#L927) | 927 | `"        spec[\"planner_freshness\"] = str(plan.get(\"freshness\") or \"unknown\")"` | — |
| [SRC-686F71AA50-L000928](../../agents/task_understanding.py#L928) | 928 | `"        spec[\"planner_depth\"] = str(plan.get(\"depth\") or \"unknown\")"` | — |
| [SRC-686F71AA50-L000929](../../agents/task_understanding.py#L929) | 929 | `"    return spec"` | — |
| [SRC-686F71AA50-L000930](../../agents/task_understanding.py#L930) | 930 | `""` | — |
| [SRC-686F71AA50-L000931](../../agents/task_understanding.py#L931) | 931 | `""` | — |
| [SRC-686F71AA50-L000932](../../agents/task_understanding.py#L932) | 932 | `"def _query_key(value: str) -> str:"` | — |
| [SRC-686F71AA50-L000933](../../agents/task_understanding.py#L933) | 933 | `"    return normalize_text(value)"` | — |
| [SRC-686F71AA50-L000934](../../agents/task_understanding.py#L934) | 934 | `""` | — |
| [SRC-686F71AA50-L000935](../../agents/task_understanding.py#L935) | 935 | `""` | — |
| [SRC-686F71AA50-L000936](../../agents/task_understanding.py#L936) | 936 | `"def _generated_strategy_candidates(topic: str, spec: dict[str, Any]) -> list[tuple[str, str, str]]:"` | — |
| [SRC-686F71AA50-L000937](../../agents/task_understanding.py#L937) | 937 | `"    family = str(spec.get(\"task_family\") or \"\")"` | — |
| [SRC-686F71AA50-L000938](../../agents/task_understanding.py#L938) | 938 | `"    constraints = spec.get(\"constraints\") if isinstance(spec.get(\"constraints\"), dict) else {}"` | — |
| [SRC-686F71AA50-L000939](../../agents/task_understanding.py#L939) | 939 | `"    aspects = constraints.get(\"explicit_aspects\") if isinstance(constraints.get(\"explicit_aspects\"), list) else []"` | — |
| [SRC-686F71AA50-L000940](../../agents/task_understanding.py#L940) | 940 | `"    candidates: list[tuple[str, str, str]] = []"` | — |
| [SRC-686F71AA50-L000941](../../agents/task_understanding.py#L941) | 941 | `"    if not topic.strip():"` | — |
| [SRC-686F71AA50-L000942](../../agents/task_understanding.py#L942) | 942 | `"        return candidates"` | — |
| [SRC-686F71AA50-L000943](../../agents/task_understanding.py#L943) | 943 | `"    locations = constraints.get(\"explicit_locations\") or []"` | — |
| [SRC-686F71AA50-L000944](../../agents/task_understanding.py#L944) | 944 | `"    location_suffix = \" \".join(str(item) for item in locations[:2])"` | — |
| [SRC-686F71AA50-L000945](../../agents/task_understanding.py#L945) | 945 | `"    hypotheses = spec.get(\"hypothesis_interpretations\")"` | — |
| [SRC-686F71AA50-L000946](../../agents/task_understanding.py#L946) | 946 | `"    hypothesis_families = {"` | — |
| [SRC-686F71AA50-L000947](../../agents/task_understanding.py#L947) | 947 | `"        str(item.get(\"family\"))"` | — |
| [SRC-686F71AA50-L000948](../../agents/task_understanding.py#L948) | 948 | `"        for item in hypotheses"` | — |
| [SRC-686F71AA50-L000949](../../agents/task_understanding.py#L949) | 949 | `"        if isinstance(item, dict) and item.get(\"family\")"` | — |
| [SRC-686F71AA50-L000950](../../agents/task_understanding.py#L950) | 950 | `"    } if isinstance(hypotheses, list) else set()"` | — |
| [SRC-686F71AA50-L000951](../../agents/task_understanding.py#L951) | 951 | `"    if family == \"official_site_lookup\" or constraints.get(\"official_destination_required\"):"` | — |
| [SRC-686F71AA50-L000952](../../agents/task_understanding.py#L952) | 952 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000953](../../agents/task_understanding.py#L953) | 953 | `"            (f\"{topic} الموقع الرسمي\", \"official_destination\", \"exact official-site discovery\"),"` | — |
| [SRC-686F71AA50-L000954](../../agents/task_understanding.py#L954) | 954 | `"            (f\"{topic} official website government portal\", \"official_domain\", \"cross-language destination discovery\"),"` | — |
| [SRC-686F71AA50-L000955](../../agents/task_understanding.py#L955) | 955 | `"        ])"` | — |
| [SRC-686F71AA50-L000956](../../agents/task_understanding.py#L956) | 956 | `"    if constraints.get(\"time_sensitive_request\"):"` | — |
| [SRC-686F71AA50-L000957](../../agents/task_understanding.py#L957) | 957 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000958](../../agents/task_understanding.py#L958) | 958 | `"            (f\"{topic} تحديث رسمي حديث {location_suffix}\".strip(), \"recent_official_update\", \"current-state fact requires fresh primary evidence\"),"` | — |
| [SRC-686F71AA50-L000959](../../agents/task_understanding.py#L959) | 959 | `"            (f\"{topic} latest official update {location_suffix}\".strip(), \"recent_official_update_en\", \"alternate language and source wording\"),"` | — |
| [SRC-686F71AA50-L000960](../../agents/task_understanding.py#L960) | 960 | `"        ])"` | — |
| [SRC-686F71AA50-L000961](../../agents/task_understanding.py#L961) | 961 | `"    if family == \"social_opinions\" or constraints.get(\"social_evidence_requested\"):"` | — |
| [SRC-686F71AA50-L000962](../../agents/task_understanding.py#L962) | 962 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000963](../../agents/task_understanding.py#L963) | 963 | `"            (f\"{topic} تجارب مستخدمين آراء الملاك {location_suffix}\".strip(), \"personal_experience_ar\", \"search for first-person experience rather than generic product mentions\"),"` | — |
| [SRC-686F71AA50-L000964](../../agents/task_understanding.py#L964) | 964 | `"            (f\"{topic} owner experience review {location_suffix}\".strip(), \"personal_experience_en\", \"cross-language owner-experience discovery\"),"` | — |
| [SRC-686F71AA50-L000965](../../agents/task_understanding.py#L965) | 965 | `"            (f\"{topic} common complaints discussion\", \"discussion_and_complaints\", \"look for contrasting experiences and discussions\"),"` | — |
| [SRC-686F71AA50-L000966](../../agents/task_understanding.py#L966) | 966 | `"        ])"` | — |
| [SRC-686F71AA50-L000967](../../agents/task_understanding.py#L967) | 967 | `"    if family == \"compare\" or \"compare\" in hypothesis_families:"` | — |
| [SRC-686F71AA50-L000968](../../agents/task_understanding.py#L968) | 968 | `"        for aspect in aspects[:MAX_TASK_ASPECTS]:"` | — |
| [SRC-686F71AA50-L000969](../../agents/task_understanding.py#L969) | 969 | `"            candidates.append((f\"{topic} {aspect}\", \"explicit_criterion\", f\"separate evidence retrieval for criterion: {aspect}\"))"` | — |
| [SRC-686F71AA50-L000970](../../agents/task_understanding.py#L970) | 970 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000971](../../agents/task_understanding.py#L971) | 971 | `"            (f\"{topic} official specifications\", \"primary_specification\", \"separate technical specifications from opinion\"),"` | — |
| [SRC-686F71AA50-L000972](../../agents/task_understanding.py#L972) | 972 | `"            (f\"{topic} independent comparison pros cons\", \"independent_comparison\", \"seek comparative analysis and trade-offs\"),"` | — |
| [SRC-686F71AA50-L000973](../../agents/task_understanding.py#L973) | 973 | `"        ])"` | — |
| [SRC-686F71AA50-L000974](../../agents/task_understanding.py#L974) | 974 | `"    if family == \"troubleshoot\" or \"troubleshoot\" in hypothesis_families:"` | — |
| [SRC-686F71AA50-L000975](../../agents/task_understanding.py#L975) | 975 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000976](../../agents/task_understanding.py#L976) | 976 | `"            (f\"{topic} الأعطال الشائعة الأسباب والحلول\", \"failure_modes_ar\", \"search causes and remedies without treating hypotheses as confirmed\"),"` | — |
| [SRC-686F71AA50-L000977](../../agents/task_understanding.py#L977) | 977 | `"            (f\"{topic} troubleshooting common failures official manual\", \"failure_modes_en\", \"technical cross-language search and primary manual\"),"` | — |
| [SRC-686F71AA50-L000978](../../agents/task_understanding.py#L978) | 978 | `"        ])"` | — |
| [SRC-686F71AA50-L000979](../../agents/task_understanding.py#L979) | 979 | `"    if family == \"how_to\" or \"how_to\" in hypothesis_families:"` | — |
| [SRC-686F71AA50-L000980](../../agents/task_understanding.py#L980) | 980 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000981](../../agents/task_understanding.py#L981) | 981 | `"            (f\"{topic} خطوات شرح دليل رسمي\", \"procedural_guide_ar\", \"seek stepwise procedure and applicable prerequisites\"),"` | — |
| [SRC-686F71AA50-L000982](../../agents/task_understanding.py#L982) | 982 | `"            (f\"{topic} official guide steps\", \"procedural_guide_en\", \"cross-language guide discovery\"),"` | — |
| [SRC-686F71AA50-L000983](../../agents/task_understanding.py#L983) | 983 | `"        ])"` | — |
| [SRC-686F71AA50-L000984](../../agents/task_understanding.py#L984) | 984 | `"    if family == \"recommendation\" or \"recommendation\" in hypothesis_families:"` | — |
| [SRC-686F71AA50-L000985](../../agents/task_understanding.py#L985) | 985 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000986](../../agents/task_understanding.py#L986) | 986 | `"            (f\"{topic} المميزات العيوب البدائل\", \"tradeoffs_ar\", \"compare trade-offs and alternatives\"),"` | — |
| [SRC-686F71AA50-L000987](../../agents/task_understanding.py#L987) | 987 | `"            (f\"{topic} pros cons alternatives review\", \"tradeoffs_en\", \"cross-language alternatives discovery\"),"` | — |
| [SRC-686F71AA50-L000988](../../agents/task_understanding.py#L988) | 988 | `"        ])"` | — |
| [SRC-686F71AA50-L000989](../../agents/task_understanding.py#L989) | 989 | `"    if family == \"lead_generation\" or \"lead_generation\" in hypothesis_families:"` | — |
| [SRC-686F71AA50-L000990](../../agents/task_understanding.py#L990) | 990 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000991](../../agents/task_understanding.py#L991) | 991 | `"            (f\"{topic} شخص يبحث عن شراء تجربة سؤال\", \"buyer_intent_ar\", \"distinguish explicit buyer intent from product advertisements\"),"` | — |
| [SRC-686F71AA50-L000992](../../agents/task_understanding.py#L992) | 992 | `"            (f\"{topic} looking to buy seeking recommendations\", \"buyer_intent_en\", \"search public discussions for intent signals\"),"` | — |
| [SRC-686F71AA50-L000993](../../agents/task_understanding.py#L993) | 993 | `"        ])"` | — |
| [SRC-686F71AA50-L000994](../../agents/task_understanding.py#L994) | 994 | `"    if family == \"medical_information\" and ("` | — |
| [SRC-686F71AA50-L000995](../../agents/task_understanding.py#L995) | 995 | `"        spec.get(\"mode\") in {\"deep\", \"latest\"} or spec.get(\"intent_route\") == \"WEB_DEEP\""` | — |
| [SRC-686F71AA50-L000996](../../agents/task_understanding.py#L996) | 996 | `"    ):"` | — |
| [SRC-686F71AA50-L000997](../../agents/task_understanding.py#L997) | 997 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000998](../../agents/task_understanding.py#L998) | 998 | `"            (f\"{topic} مصدر صحي رسمي إرشادات\", \"authoritative_health_source\", \"prefer current public health guidance, not a personal diagnosis\"),"` | — |
| [SRC-686F71AA50-L000999](../../agents/task_understanding.py#L999) | 999 | `"            (f\"{topic} clinical guidance evidence limitations\", \"clinical_evidence_context\", \"look for evidence quality and documented limitations\"),"` | — |
| [SRC-686F71AA50-L001000](../../agents/task_understanding.py#L1000) | 1000 | `"        ])"` | — |
| [SRC-686F71AA50-L001001](../../agents/task_understanding.py#L1001) | 1001 | `"    if family == \"legal_information\" and ("` | — |
| [SRC-686F71AA50-L001002](../../agents/task_understanding.py#L1002) | 1002 | `"        spec.get(\"mode\") in {\"deep\", \"latest\"} or spec.get(\"intent_route\") == \"WEB_DEEP\""` | — |
| [SRC-686F71AA50-L001003](../../agents/task_understanding.py#L1003) | 1003 | `"    ):"` | — |
| [SRC-686F71AA50-L001004](../../agents/task_understanding.py#L1004) | 1004 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L001005](../../agents/task_understanding.py#L1005) | 1005 | `"            (f\"{topic} نص قانوني رسمي التشريع\", \"official_legal_text\", \"seek primary law or regulator text and verify jurisdiction\"),"` | — |
| [SRC-686F71AA50-L001006](../../agents/task_understanding.py#L1006) | 1006 | `"            (f\"{topic} jurisdiction effective date legal interpretation\", \"jurisdiction_and_effective_date\", \"keep jurisdiction and effective date visible\"),"` | — |
| [SRC-686F71AA50-L001007](../../agents/task_understanding.py#L1007) | 1007 | `"        ])"` | — |
| [SRC-686F71AA50-L001008](../../agents/task_understanding.py#L1008) | 1008 | `"    if family == \"coding_or_technical_design\" and ("` | — |
| [SRC-686F71AA50-L001009](../../agents/task_understanding.py#L1009) | 1009 | `"        spec.get(\"mode\") in {\"deep\", \"latest\"} or spec.get(\"intent_route\") == \"WEB_DEEP\""` | — |
| [SRC-686F71AA50-L001010](../../agents/task_understanding.py#L1010) | 1010 | `"    ):"` | — |
| [SRC-686F71AA50-L001011](../../agents/task_understanding.py#L1011) | 1011 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L001012](../../agents/task_understanding.py#L1012) | 1012 | `"            (f\"{topic} official documentation\", \"official_technical_docs\", \"prefer the language/runtime's authoritative documentation\"),"` | — |
| [SRC-686F71AA50-L001013](../../agents/task_understanding.py#L1013) | 1013 | `"            (f\"{topic} exact error regression test\", \"error_and_regression_test\", \"look for a reproducible error and a testable fix\"),"` | — |
| [SRC-686F71AA50-L001014](../../agents/task_understanding.py#L1014) | 1014 | `"        ])"` | — |
| [SRC-686F71AA50-L001015](../../agents/task_understanding.py#L1015) | 1015 | `"    if family == \"planning\" and ("` | — |
| [SRC-686F71AA50-L001016](../../agents/task_understanding.py#L1016) | 1016 | `"        spec.get(\"mode\") in {\"deep\", \"latest\"} or spec.get(\"intent_route\") == \"WEB_DEEP\""` | — |
| [SRC-686F71AA50-L001017](../../agents/task_understanding.py#L1017) | 1017 | `"    ):"` | — |
| [SRC-686F71AA50-L001018](../../agents/task_understanding.py#L1018) | 1018 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L001019](../../agents/task_understanding.py#L1019) | 1019 | `"            (f\"{topic} risks dependencies feasibility\", \"feasibility_and_dependencies\", \"test assumptions, dependencies, and likely blockers\"),"` | — |
| [SRC-686F71AA50-L001020](../../agents/task_understanding.py#L1020) | 1020 | `"            (f\"{topic} alternative plan fallback\", \"alternatives_and_fallback\", \"seek alternatives and fallback approaches\"),"` | — |
| [SRC-686F71AA50-L001021](../../agents/task_understanding.py#L1021) | 1021 | `"        ])"` | — |
| [SRC-686F71AA50-L001022](../../agents/task_understanding.py#L1022) | 1022 | `"    normalized_topic = normalize_text(topic)"` | — |
| [SRC-686F71AA50-L001023](../../agents/task_understanding.py#L1023) | 1023 | `"    property_topic = any("` | — |
| [SRC-686F71AA50-L001024](../../agents/task_understanding.py#L1024) | 1024 | `"        cue in normalized_topic"` | — |
| [SRC-686F71AA50-L001025](../../agents/task_understanding.py#L1025) | 1025 | `"        for cue in (\"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"عقاري\", \"real estate\", \"apartment\", \"property\")"` | — |
| [SRC-686F71AA50-L001026](../../agents/task_understanding.py#L1026) | 1026 | `"    )"` | — |
| [SRC-686F71AA50-L001027](../../agents/task_understanding.py#L1027) | 1027 | `"    if family == \"find_or_discover\" and property_topic:"` | — |
| [SRC-686F71AA50-L001028](../../agents/task_understanding.py#L1028) | 1028 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L001029](../../agents/task_understanding.py#L1029) | 1029 | `"            (f\"{topic} إعلانات عقارية\", \"property_listings\", \"discover relevant listings without treating ads as independent price evidence\"),"` | — |
| [SRC-686F71AA50-L001030](../../agents/task_understanding.py#L1030) | 1030 | `"            (f\"{topic} متوسط أسعار السوق للمتر\", \"property_market_price_per_meter\", \"compare asking prices against market-level context\"),"` | — |
| [SRC-686F71AA50-L001031](../../agents/task_understanding.py#L1031) | 1031 | `"            (f\"{topic} أسعار البيع الفعلية والتقييم العقاري\", \"property_transaction_price_check\", \"distinguish asking prices from completed transaction prices\"),"` | — |
| [SRC-686F71AA50-L001032](../../agents/task_understanding.py#L1032) | 1032 | `"        ])"` | — |
| [SRC-686F71AA50-L001033](../../agents/task_understanding.py#L1033) | 1033 | `"    if ("` | — |
| [SRC-686F71AA50-L001034](../../agents/task_understanding.py#L1034) | 1034 | `"        family in {\"general_research\", \"web_research\", \"find_or_discover\"}"` | — |
| [SRC-686F71AA50-L001035](../../agents/task_understanding.py#L1035) | 1035 | `"        and ("` | — |
| [SRC-686F71AA50-L001036](../../agents/task_understanding.py#L1036) | 1036 | `"            spec.get(\"mode\") in {\"deep\", \"latest\", \"social\"}"` | — |
| [SRC-686F71AA50-L001037](../../agents/task_understanding.py#L1037) | 1037 | `"            or constraints.get(\"time_sensitive_request\")"` | — |
| [SRC-686F71AA50-L001038](../../agents/task_understanding.py#L1038) | 1038 | `"            or spec.get(\"planner_depth\") == \"deep\""` | — |
| [SRC-686F71AA50-L001039](../../agents/task_understanding.py#L1039) | 1039 | `"            or spec.get(\"intent_route\") in {\"WEB_DEEP\", \"LEAD_GENERATION\"}"` | — |
| [SRC-686F71AA50-L001040](../../agents/task_understanding.py#L1040) | 1040 | `"        )"` | — |
| [SRC-686F71AA50-L001041](../../agents/task_understanding.py#L1041) | 1041 | `"    ):"` | — |
| [SRC-686F71AA50-L001042](../../agents/task_understanding.py#L1042) | 1042 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L001043](../../agents/task_understanding.py#L1043) | 1043 | `"            (f\"{topic} مصدر رسمي\", \"primary_source_ar\", \"prefer an original or primary source when appropriate\"),"` | — |
| [SRC-686F71AA50-L001044](../../agents/task_understanding.py#L1044) | 1044 | `"            (f\"{topic} official source report\", \"primary_source_en\", \"alternate source-oriented search wording\"),"` | — |
| [SRC-686F71AA50-L001045](../../agents/task_understanding.py#L1045) | 1045 | `"            (f\"{topic} limitations risks independent analysis\", \"independent_analysis\", \"seek counterevidence and limitations\"),"` | — |
| [SRC-686F71AA50-L001046](../../agents/task_understanding.py#L1046) | 1046 | `"        ])"` | — |
| [SRC-686F71AA50-L001047](../../agents/task_understanding.py#L1047) | 1047 | `"    if ("` | — |
| [SRC-686F71AA50-L001048](../../agents/task_understanding.py#L1048) | 1048 | `"        not candidates"` | — |
| [SRC-686F71AA50-L001049](../../agents/task_understanding.py#L1049) | 1049 | `"        and family in {"` | — |
| [SRC-686F71AA50-L001050](../../agents/task_understanding.py#L1050) | 1050 | `"            \"official_site_lookup\", \"current_information\", \"social_opinions\","` | — |
| [SRC-686F71AA50-L001051](../../agents/task_understanding.py#L1051) | 1051 | `"            \"compare\", \"troubleshoot\", \"how_to\", \"recommendation\","` | — |
| [SRC-686F71AA50-L001052](../../agents/task_understanding.py#L1052) | 1052 | `"            \"lead_generation\", \"general_research\", \"web_research\", \"find_or_discover\","` | — |
| [SRC-686F71AA50-L001053](../../agents/task_understanding.py#L1053) | 1053 | `"            \"medical_information\", \"legal_information\", \"coding_or_technical_design\","` | — |
| [SRC-686F71AA50-L001054](../../agents/task_understanding.py#L1054) | 1054 | `"            \"planning\","` | — |
| [SRC-686F71AA50-L001055](../../agents/task_understanding.py#L1055) | 1055 | `"        }"` | — |
| [SRC-686F71AA50-L001056](../../agents/task_understanding.py#L1056) | 1056 | `"        and ("` | — |
| [SRC-686F71AA50-L001057](../../agents/task_understanding.py#L1057) | 1057 | `"            spec.get(\"mode\") in {\"deep\", \"latest\", \"social\"}"` | — |
| [SRC-686F71AA50-L001058](../../agents/task_understanding.py#L1058) | 1058 | `"            or spec.get(\"intent_route\") in {\"WEB_DEEP\", \"LEAD_GENERATION\"}"` | — |
| [SRC-686F71AA50-L001059](../../agents/task_understanding.py#L1059) | 1059 | `"        )"` | — |
| [SRC-686F71AA50-L001060](../../agents/task_understanding.py#L1060) | 1060 | `"    ):"` | — |
| [SRC-686F71AA50-L001061](../../agents/task_understanding.py#L1061) | 1061 | `"        candidates.append("` | — |
| [SRC-686F71AA50-L001062](../../agents/task_understanding.py#L1062) | 1062 | `"            (f\"{topic} مصدر موثوق\", \"source_oriented_alternative\", \"search wording is a hypothesis, not evidence\")"` | — |
| [SRC-686F71AA50-L001063](../../agents/task_understanding.py#L1063) | 1063 | `"        )"` | — |
| [SRC-686F71AA50-L001064](../../agents/task_understanding.py#L1064) | 1064 | `"    return candidates"` | — |
| [SRC-686F71AA50-L001065](../../agents/task_understanding.py#L1065) | 1065 | `""` | — |
| [SRC-686F71AA50-L001066](../../agents/task_understanding.py#L1066) | 1066 | `""` | — |
| [SRC-686F71AA50-L001067](../../agents/task_understanding.py#L1067) | 1067 | `"def _label_existing_query(query: str, index: int, spec: dict[str, Any]) -> tuple[str, str]:"` | — |
| [SRC-686F71AA50-L001068](../../agents/task_understanding.py#L1068) | 1068 | `"    \"\"\"Classify query wording for diagnostics; this is not a retrieval-success claim.\"\"\""` | — |
| [SRC-686F71AA50-L001069](../../agents/task_understanding.py#L1069) | 1069 | `"    normalized = normalize_text(query)"` | — |
| [SRC-686F71AA50-L001070](../../agents/task_understanding.py#L1070) | 1070 | `"    constraints = spec.get(\"constraints\") if isinstance(spec.get(\"constraints\"), dict) else {}"` | — |
| [SRC-686F71AA50-L001071](../../agents/task_understanding.py#L1071) | 1071 | `"    if re.search(r\"\\bsite\\s*:\", query, flags=re.IGNORECASE):"` | — |
| [SRC-686F71AA50-L001072](../../agents/task_understanding.py#L1072) | 1072 | `"        return \"platform_scoped\", \"query explicitly scopes a public site or platform\""` | — |
| [SRC-686F71AA50-L001073](../../agents/task_understanding.py#L1073) | 1073 | `"    if constraints.get(\"official_destination_required\") and any("` | — |
| [SRC-686F71AA50-L001074](../../agents/task_understanding.py#L1074) | 1074 | `"        marker in normalized for marker in (\"الموقع الرسمي\", \"official website\", \"official site\")"` | — |
| [SRC-686F71AA50-L001075](../../agents/task_understanding.py#L1075) | 1075 | `"    ):"` | — |
| [SRC-686F71AA50-L001076](../../agents/task_understanding.py#L1076) | 1076 | `"        return \"official_destination\", \"query wording seeks an official destination\""` | — |
| [SRC-686F71AA50-L001077](../../agents/task_understanding.py#L1077) | 1077 | `"    if constraints.get(\"time_sensitive_request\") and any("` | — |
| [SRC-686F71AA50-L001078](../../agents/task_understanding.py#L1078) | 1078 | `"        marker in normalized for marker in (\"latest\", \"recent\", \"today\", \"تحديث\", \"حديث\", \"احدث\", \"اخر\")"` | — |
| [SRC-686F71AA50-L001079](../../agents/task_understanding.py#L1079) | 1079 | `"    ):"` | — |
| [SRC-686F71AA50-L001080](../../agents/task_understanding.py#L1080) | 1080 | `"        return \"recent_information\", \"query wording seeks current information; dates and page readability still require validation\""` | — |
| [SRC-686F71AA50-L001081](../../agents/task_understanding.py#L1081) | 1081 | `"    if any(marker in normalized for marker in (\"تجارب\", \"اراء\", \"تجربه\", \"experience\", \"owner review\", \"user review\")):"` | — |
| [SRC-686F71AA50-L001082](../../agents/task_understanding.py#L1082) | 1082 | `"        return \"personal_experience\", \"query wording targets user experience; the author's identity and truth remain unverified\""` | — |
| [SRC-686F71AA50-L001083](../../agents/task_understanding.py#L1083) | 1083 | `"    if any(marker in normalized for marker in (\"اعطال\", \"الاسباب\", \"الحلول\", \"troubleshooting\", \"common failures\")):"` | — |
| [SRC-686F71AA50-L001084](../../agents/task_understanding.py#L1084) | 1084 | `"        return \"troubleshooting\", \"query wording targets symptoms, causes, or remedies\""` | — |
| [SRC-686F71AA50-L001085](../../agents/task_understanding.py#L1085) | 1085 | `"    if any(marker in normalized for marker in (\"المقارنة\", \"مقارنة\", \"قارن\", \"comparison\", \"versus\", \"pros cons\", \"trade offs\")):"` | — |
| [SRC-686F71AA50-L001086](../../agents/task_understanding.py#L1086) | 1086 | `"        return \"comparison\", \"query wording targets a comparison or trade-off analysis\""` | — |
| [SRC-686F71AA50-L001087](../../agents/task_understanding.py#L1087) | 1087 | `"    if any(marker in normalized for marker in (\"مصدر رسمي\", \"official source\", \"manual\", \"specifications\", \"مواصفات\")):"` | — |
| [SRC-686F71AA50-L001088](../../agents/task_understanding.py#L1088) | 1088 | `"        return \"primary_source\", \"query wording seeks a primary or technical source\""` | — |
| [SRC-686F71AA50-L001089](../../agents/task_understanding.py#L1089) | 1089 | `"    if index == 0:"` | — |
| [SRC-686F71AA50-L001090](../../agents/task_understanding.py#L1090) | 1090 | `"        return \"planner_seed\", \"initial planner query; relevance and source quality are validated later\""` | — |
| [SRC-686F71AA50-L001091](../../agents/task_understanding.py#L1091) | 1091 | `"    return \"planner_alternative\", \"alternate planner query; label is inferred from wording/position\""` | — |
| [SRC-686F71AA50-L001092](../../agents/task_understanding.py#L1092) | 1092 | `""` | — |
| [SRC-686F71AA50-L001093](../../agents/task_understanding.py#L1093) | 1093 | `""` | — |
| [SRC-686F71AA50-L001094](../../agents/task_understanding.py#L1094) | 1094 | `"def build_query_strategy_matrix("` | — |
| [SRC-686F71AA50-L001095](../../agents/task_understanding.py#L1095) | 1095 | `"    question: str,"` | — |
| [SRC-686F71AA50-L001096](../../agents/task_understanding.py#L1096) | 1096 | `"    task_spec: dict[str, Any],"` | — |
| [SRC-686F71AA50-L001097](../../agents/task_understanding.py#L1097) | 1097 | `"    existing_queries: Any,"` | — |
| [SRC-686F71AA50-L001098](../../agents/task_understanding.py#L1098) | 1098 | `"    *,"` | — |
| [SRC-686F71AA50-L001099](../../agents/task_understanding.py#L1099) | 1099 | `"    limit: int = MAX_STRATEGY_QUERIES,"` | — |
| [SRC-686F71AA50-L001100](../../agents/task_understanding.py#L1100) | 1100 | `"    compact_fn: Any = None,"` | — |
| [SRC-686F71AA50-L001101](../../agents/task_understanding.py#L1101) | 1101 | `") -> list[dict[str, str]]:"` | — |
| [SRC-686F71AA50-L001102](../../agents/task_understanding.py#L1102) | 1102 | `"    \"\"\"Return bounded query candidates, prioritizing task-specific evidence strategies."` | — |
| [SRC-686F71AA50-L001103](../../agents/task_understanding.py#L1103) | 1103 | `""` | — |
| [SRC-686F71AA50-L001104](../../agents/task_understanding.py#L1104) | 1104 | `"    The first existing planner query anchors the topic. Task-aware queries are then"` | — |
| [SRC-686F71AA50-L001105](../../agents/task_understanding.py#L1105) | 1105 | `"    considered before secondary planner queries, so generic alternatives cannot consume"` | — |
| [SRC-686F71AA50-L001106](../../agents/task_understanding.py#L1106) | 1106 | `"    the whole budget and crowd out explicit user criteria."` | — |
| [SRC-686F71AA50-L001107](../../agents/task_understanding.py#L1107) | 1107 | `"    \"\"\""` | — |
| [SRC-686F71AA50-L001108](../../agents/task_understanding.py#L1108) | 1108 | `"    maximum = max(1, min(int(limit), MAX_STRATEGY_QUERIES))"` | — |
| [SRC-686F71AA50-L001109](../../agents/task_understanding.py#L1109) | 1109 | `"    spec = task_spec if isinstance(task_spec, dict) else {}"` | — |
| [SRC-686F71AA50-L001110](../../agents/task_understanding.py#L1110) | 1110 | `"    queries = existing_queries if isinstance(existing_queries, list) else []"` | — |
| [SRC-686F71AA50-L001111](../../agents/task_understanding.py#L1111) | 1111 | `"    rows: list[dict[str, str]] = []"` | — |
| [SRC-686F71AA50-L001112](../../agents/task_understanding.py#L1112) | 1112 | `"    seen: set[str] = set()"` | — |
| [SRC-686F71AA50-L001113](../../agents/task_understanding.py#L1113) | 1113 | `""` | — |
| [SRC-686F71AA50-L001114](../../agents/task_understanding.py#L1114) | 1114 | `"    def add(query: Any, strategy: str, rationale: str, *, enforce_topic: bool = True) -> None:"` | — |
| [SRC-686F71AA50-L001115](../../agents/task_understanding.py#L1115) | 1115 | `"        if not isinstance(query, str) or not query.strip() or len(rows) >= maximum:"` | — |
| [SRC-686F71AA50-L001116](../../agents/task_understanding.py#L1116) | 1116 | `"            return"` | — |
| [SRC-686F71AA50-L001117](../../agents/task_understanding.py#L1117) | 1117 | `"        candidate = query.strip()"` | — |
| [SRC-686F71AA50-L001118](../../agents/task_understanding.py#L1118) | 1118 | `"        if compact_fn is not None:"` | — |
| [SRC-686F71AA50-L001119](../../agents/task_understanding.py#L1119) | 1119 | `"            try:"` | — |
| [SRC-686F71AA50-L001120](../../agents/task_understanding.py#L1120) | 1120 | `"                candidate = compact_fn(candidate) or \"\""` | — |
| [SRC-686F71AA50-L001121](../../agents/task_understanding.py#L1121) | 1121 | `"            except (TypeError, ValueError):"` | — |
| [SRC-686F71AA50-L001122](../../agents/task_understanding.py#L1122) | 1122 | `"                candidate = \"\""` | — |
| [SRC-686F71AA50-L001123](../../agents/task_understanding.py#L1123) | 1123 | `"        candidate = _SPACE.sub(\" \", candidate).strip()[:240]"` | — |
| [SRC-686F71AA50-L001124](../../agents/task_understanding.py#L1124) | 1124 | `"        key = _query_key(candidate)"` | — |
| [SRC-686F71AA50-L001125](../../agents/task_understanding.py#L1125) | 1125 | `"        if not candidate or not key or key in seen:"` | — |
| [SRC-686F71AA50-L001126](../../agents/task_understanding.py#L1126) | 1126 | `"            return"` | — |
| [SRC-686F71AA50-L001127](../../agents/task_understanding.py#L1127) | 1127 | `"        # Search modifications must preserve a subject anchor. Existing planner"` | — |
| [SRC-686F71AA50-L001128](../../agents/task_understanding.py#L1128) | 1128 | `"        # queries are retained because they may already contain resolved context."` | — |
| [SRC-686F71AA50-L001129](../../agents/task_understanding.py#L1129) | 1129 | `"        anchor_query = str(queries[0]).strip() if queries and isinstance(queries[0], str) else str(question or \"\")"` | — |
| [SRC-686F71AA50-L001130](../../agents/task_understanding.py#L1130) | 1130 | `"        topic_tokens = _TOKEN_RE.findall(_query_key(anchor_query))"` | — |
| [SRC-686F71AA50-L001131](../../agents/task_understanding.py#L1131) | 1131 | `"        query_tokens = _TOKEN_RE.findall(key)"` | — |
| [SRC-686F71AA50-L001132](../../agents/task_understanding.py#L1132) | 1132 | `"        if enforce_topic and len(topic_tokens) >= 2 and not any("` | — |
| [SRC-686F71AA50-L001133](../../agents/task_understanding.py#L1133) | 1133 | `"            token in query_tokens for token in topic_tokens[:3]"` | — |
| [SRC-686F71AA50-L001134](../../agents/task_understanding.py#L1134) | 1134 | `"        ):"` | — |
| [SRC-686F71AA50-L001135](../../agents/task_understanding.py#L1135) | 1135 | `"            return"` | — |
| [SRC-686F71AA50-L001136](../../agents/task_understanding.py#L1136) | 1136 | `"        seen.add(key)"` | — |
| [SRC-686F71AA50-L001137](../../agents/task_understanding.py#L1137) | 1137 | `"        rows.append({\"query\": candidate, \"strategy\": strategy, \"rationale\": rationale})"` | — |
| [SRC-686F71AA50-L001138](../../agents/task_understanding.py#L1138) | 1138 | `""` | — |
| [SRC-686F71AA50-L001139](../../agents/task_understanding.py#L1139) | 1139 | `"    constraints = spec.get(\"constraints\") if isinstance(spec.get(\"constraints\"), dict) else {}"` | — |
| [SRC-686F71AA50-L001140](../../agents/task_understanding.py#L1140) | 1140 | `"    explicit_aspects = ("` | — |
| [SRC-686F71AA50-L001141](../../agents/task_understanding.py#L1141) | 1141 | `"        constraints.get(\"explicit_aspects\")"` | — |
| [SRC-686F71AA50-L001142](../../agents/task_understanding.py#L1142) | 1142 | `"        if isinstance(constraints.get(\"explicit_aspects\"), list)"` | — |
| [SRC-686F71AA50-L001143](../../agents/task_understanding.py#L1143) | 1143 | `"        else []"` | — |
| [SRC-686F71AA50-L001144](../../agents/task_understanding.py#L1144) | 1144 | `"    )"` | — |
| [SRC-686F71AA50-L001145](../../agents/task_understanding.py#L1145) | 1145 | `"    # Use the dedicated aspect extractor as a second deterministic pass. This"` | — |
| [SRC-686F71AA50-L001146](../../agents/task_understanding.py#L1146) | 1146 | `"    # guards against a classifier losing the final criterion in a long list."` | — |
| [SRC-686F71AA50-L001147](../../agents/task_understanding.py#L1147) | 1147 | `"    try:"` | — |
| [SRC-686F71AA50-L001148](../../agents/task_understanding.py#L1148) | 1148 | `"        from agents.aspect_planning import extract_aspects"` | — |
| [SRC-686F71AA50-L001149](../../agents/task_understanding.py#L1149) | 1149 | `"        independently_extracted = extract_aspects(question)"` | — |
| [SRC-686F71AA50-L001150](../../agents/task_understanding.py#L1150) | 1150 | `"    except (ImportError, TypeError, ValueError):"` | — |
| [SRC-686F71AA50-L001151](../../agents/task_understanding.py#L1151) | 1151 | `"        independently_extracted = []"` | — |
| [SRC-686F71AA50-L001152](../../agents/task_understanding.py#L1152) | 1152 | `"    merged_aspects: list[str] = []"` | — |
| [SRC-686F71AA50-L001153](../../agents/task_understanding.py#L1153) | 1153 | `"    aspect_keys: set[str] = set()"` | — |
| [SRC-686F71AA50-L001154](../../agents/task_understanding.py#L1154) | 1154 | `"    for aspect in [*explicit_aspects, *independently_extracted]:"` | — |
| [SRC-686F71AA50-L001155](../../agents/task_understanding.py#L1155) | 1155 | `"        if not isinstance(aspect, str) or not aspect.strip():"` | — |
| [SRC-686F71AA50-L001156](../../agents/task_understanding.py#L1156) | 1156 | `"            continue"` | — |
| [SRC-686F71AA50-L001157](../../agents/task_understanding.py#L1157) | 1157 | `"        key = _query_key(aspect)"` | — |
| [SRC-686F71AA50-L001158](../../agents/task_understanding.py#L1158) | 1158 | `"        if key and key not in aspect_keys:"` | — |
| [SRC-686F71AA50-L001159](../../agents/task_understanding.py#L1159) | 1159 | `"            aspect_keys.add(key)"` | — |
| [SRC-686F71AA50-L001160](../../agents/task_understanding.py#L1160) | 1160 | `"            merged_aspects.append(aspect.strip())"` | — |
| [SRC-686F71AA50-L001161](../../agents/task_understanding.py#L1161) | 1161 | `"        if len(merged_aspects) >= MAX_TASK_ASPECTS:"` | — |
| [SRC-686F71AA50-L001162](../../agents/task_understanding.py#L1162) | 1162 | `"            break"` | — |
| [SRC-686F71AA50-L001163](../../agents/task_understanding.py#L1163) | 1163 | `"    explicit_aspects = merged_aspects"` | — |
| [SRC-686F71AA50-L001164](../../agents/task_understanding.py#L1164) | 1164 | `"    spec_for_candidates = dict(spec)"` | — |
| [SRC-686F71AA50-L001165](../../agents/task_understanding.py#L1165) | 1165 | `"    candidate_constraints = dict(constraints)"` | — |
| [SRC-686F71AA50-L001166](../../agents/task_understanding.py#L1166) | 1166 | `"    candidate_constraints[\"explicit_aspects\"] = explicit_aspects"` | — |
| [SRC-686F71AA50-L001167](../../agents/task_understanding.py#L1167) | 1167 | `"    spec_for_candidates[\"constraints\"] = candidate_constraints"` | — |
| [SRC-686F71AA50-L001168](../../agents/task_understanding.py#L1168) | 1168 | `"    # If every query slot is needed to represent explicit comparison criteria,"` | — |
| [SRC-686F71AA50-L001169](../../agents/task_understanding.py#L1169) | 1169 | `"    # spend the budget on those criteria rather than a generic planner seed."` | — |
| [SRC-686F71AA50-L001170](../../agents/task_understanding.py#L1170) | 1170 | `"    reserve_all_slots_for_criteria = ("` | — |
| [SRC-686F71AA50-L001171](../../agents/task_understanding.py#L1171) | 1171 | `"        spec.get(\"task_family\") == \"compare\""` | — |
| [SRC-686F71AA50-L001172](../../agents/task_understanding.py#L1172) | 1172 | `"        and len(explicit_aspects) >= maximum"` | — |
| [SRC-686F71AA50-L001173](../../agents/task_understanding.py#L1173) | 1173 | `"    )"` | — |
| [SRC-686F71AA50-L001174](../../agents/task_understanding.py#L1174) | 1174 | `"    if queries and not reserve_all_slots_for_criteria:"` | — |
| [SRC-686F71AA50-L001175](../../agents/task_understanding.py#L1175) | 1175 | `"        seed = queries[0]"` | — |
| [SRC-686F71AA50-L001176](../../agents/task_understanding.py#L1176) | 1176 | `"        strategy, rationale = ("` | — |
| [SRC-686F71AA50-L001177](../../agents/task_understanding.py#L1177) | 1177 | `"            _label_existing_query(seed, 0, spec)"` | — |
| [SRC-686F71AA50-L001178](../../agents/task_understanding.py#L1178) | 1178 | `"            if isinstance(seed, str)"` | — |
| [SRC-686F71AA50-L001179](../../agents/task_understanding.py#L1179) | 1179 | `"            else (\"malformed\", \"planner seed is not a string\")"` | — |
| [SRC-686F71AA50-L001180](../../agents/task_understanding.py#L1180) | 1180 | `"        )"` | — |
| [SRC-686F71AA50-L001181](../../agents/task_understanding.py#L1181) | 1181 | `"        add(seed, strategy, rationale, enforce_topic=False)"` | — |
| [SRC-686F71AA50-L001182](../../agents/task_understanding.py#L1182) | 1182 | `""` | — |
| [SRC-686F71AA50-L001183](../../agents/task_understanding.py#L1183) | 1183 | `"    if not rows and ("` | — |
| [SRC-686F71AA50-L001184](../../agents/task_understanding.py#L1184) | 1184 | `"        spec.get(\"ambiguity_status\") == \"needs_clarification\""` | — |
| [SRC-686F71AA50-L001185](../../agents/task_understanding.py#L1185) | 1185 | `"        or spec.get(\"task_family\") == \"ambiguous_or_incomplete\""` | — |
| [SRC-686F71AA50-L001186](../../agents/task_understanding.py#L1186) | 1186 | `"    ):"` | — |
| [SRC-686F71AA50-L001187](../../agents/task_understanding.py#L1187) | 1187 | `"        return rows"` | — |
| [SRC-686F71AA50-L001188](../../agents/task_understanding.py#L1188) | 1188 | `""` | — |
| [SRC-686F71AA50-L001189](../../agents/task_understanding.py#L1189) | 1189 | `"    base = str(queries[0]).strip() if queries and isinstance(queries[0], str) else \"\""` | — |
| [SRC-686F71AA50-L001190](../../agents/task_understanding.py#L1190) | 1190 | `"    if not base:"` | — |
| [SRC-686F71AA50-L001191](../../agents/task_understanding.py#L1191) | 1191 | `"        base = re.sub("` | — |
| [SRC-686F71AA50-L001192](../../agents/task_understanding.py#L1192) | 1192 | `"            r\"^(?:من فضلك\|لو سمحت\|ابحث لي\|ابحث\|دورلي\|دور\|اعثر على\|please\|search for\|find\|look up)\\s*\","` | — |
| [SRC-686F71AA50-L001193](../../agents/task_understanding.py#L1193) | 1193 | `"            \"\", str(question or \"\").strip(), flags=re.IGNORECASE,"` | — |
| [SRC-686F71AA50-L001194](../../agents/task_understanding.py#L1194) | 1194 | `"        )"` | — |
| [SRC-686F71AA50-L001195](../../agents/task_understanding.py#L1195) | 1195 | `"    base = _QUERY_STOP.sub(\"\", base).strip(\" \\t\\r\\n-،,؛;\")"` | — |
| [SRC-686F71AA50-L001196](../../agents/task_understanding.py#L1196) | 1196 | `"    if not base:"` | — |
| [SRC-686F71AA50-L001197](../../agents/task_understanding.py#L1197) | 1197 | `"        return rows"` | — |
| [SRC-686F71AA50-L001198](../../agents/task_understanding.py#L1198) | 1198 | `""` | — |
| [SRC-686F71AA50-L001199](../../agents/task_understanding.py#L1199) | 1199 | `"    candidates = _generated_strategy_candidates(base, spec_for_candidates)"` | — |
| [SRC-686F71AA50-L001200](../../agents/task_understanding.py#L1200) | 1200 | `"    for query, strategy, rationale in candidates:"` | — |
| [SRC-686F71AA50-L001201](../../agents/task_understanding.py#L1201) | 1201 | `"        add("` | — |
| [SRC-686F71AA50-L001202](../../agents/task_understanding.py#L1202) | 1202 | `"            query, strategy, rationale,"` | — |
| [SRC-686F71AA50-L001203](../../agents/task_understanding.py#L1203) | 1203 | `"            enforce_topic=(strategy != \"explicit_criterion\"),"` | — |
| [SRC-686F71AA50-L001204](../../agents/task_understanding.py#L1204) | 1204 | `"        )"` | — |
| [SRC-686F71AA50-L001205](../../agents/task_understanding.py#L1205) | 1205 | `"        if len(rows) >= maximum:"` | — |
| [SRC-686F71AA50-L001206](../../agents/task_understanding.py#L1206) | 1206 | `"            break"` | — |
| [SRC-686F71AA50-L001207](../../agents/task_understanding.py#L1207) | 1207 | `""` | — |
| [SRC-686F71AA50-L001208](../../agents/task_understanding.py#L1208) | 1208 | `"    # Preserve other planner alternatives only after task-targeted candidates."` | — |
| [SRC-686F71AA50-L001209](../../agents/task_understanding.py#L1209) | 1209 | `"    for index, query in enumerate(queries[1:], start=1):"` | — |
| [SRC-686F71AA50-L001210](../../agents/task_understanding.py#L1210) | 1210 | `"        if len(rows) >= maximum:"` | — |
| [SRC-686F71AA50-L001211](../../agents/task_understanding.py#L1211) | 1211 | `"            break"` | — |
| [SRC-686F71AA50-L001212](../../agents/task_understanding.py#L1212) | 1212 | `"        if isinstance(query, str):"` | — |
| [SRC-686F71AA50-L001213](../../agents/task_understanding.py#L1213) | 1213 | `"            strategy, rationale = _label_existing_query(query, index, spec)"` | — |
| [SRC-686F71AA50-L001214](../../agents/task_understanding.py#L1214) | 1214 | `"        else:"` | — |
| [SRC-686F71AA50-L001215](../../agents/task_understanding.py#L1215) | 1215 | `"            strategy, rationale = \"malformed\", \"planner alternative is not a string\""` | — |
| [SRC-686F71AA50-L001216](../../agents/task_understanding.py#L1216) | 1216 | `"        add(query, strategy, rationale, enforce_topic=False)"` | — |
| [SRC-686F71AA50-L001217](../../agents/task_understanding.py#L1217) | 1217 | `"    return rows"` | — |
| [SRC-686F71AA50-L001218](../../agents/task_understanding.py#L1218) | 1218 | `""` | — |
| [SRC-686F71AA50-L001219](../../agents/task_understanding.py#L1219) | 1219 | `"def validate_task_spec(value: Any) -> dict[str, Any]:"` | — |
| [SRC-686F71AA50-L001220](../../agents/task_understanding.py#L1220) | 1220 | `"    \"\"\"Return an allowlisted, bounded JSON representation of TaskSpec-like input.\"\"\""` | — |
| [SRC-686F71AA50-L001221](../../agents/task_understanding.py#L1221) | 1221 | `"    unavailable = {"` | — |
| [SRC-686F71AA50-L001222](../../agents/task_understanding.py#L1222) | 1222 | `"        \"schema\": \"omarai.task_spec.v1\","` | — |
| [SRC-686F71AA50-L001223](../../agents/task_understanding.py#L1223) | 1223 | `"        \"status\": \"not_available\","` | — |
| [SRC-686F71AA50-L001224](../../agents/task_understanding.py#L1224) | 1224 | `"        \"claim\": \"no validated task specification supplied\","` | — |
| [SRC-686F71AA50-L001225](../../agents/task_understanding.py#L1225) | 1225 | `"    }"` | — |
| [SRC-686F71AA50-L001226](../../agents/task_understanding.py#L1226) | 1226 | `"    if not isinstance(value, dict) or value.get(\"schema\") != \"omarai.task_spec.v1\":"` | — |
| [SRC-686F71AA50-L001227](../../agents/task_understanding.py#L1227) | 1227 | `"        return unavailable"` | — |
| [SRC-686F71AA50-L001228](../../agents/task_understanding.py#L1228) | 1228 | `""` | — |
| [SRC-686F71AA50-L001229](../../agents/task_understanding.py#L1229) | 1229 | `"    def clean_text(item: Any, limit: int = 160) -> str:"` | — |
| [SRC-686F71AA50-L001230](../../agents/task_understanding.py#L1230) | 1230 | `"        if not isinstance(item, str):"` | — |
| [SRC-686F71AA50-L001231](../../agents/task_understanding.py#L1231) | 1231 | `"            return \"\""` | — |
| [SRC-686F71AA50-L001232](../../agents/task_understanding.py#L1232) | 1232 | `"        return _SPACE.sub(\" \", unicodedata.normalize(\"NFKC\", item).replace(\"\\x00\", \" \")).strip()[:limit]"` | — |
| [SRC-686F71AA50-L001233](../../agents/task_understanding.py#L1233) | 1233 | `""` | — |
| [SRC-686F71AA50-L001234](../../agents/task_understanding.py#L1234) | 1234 | `"    def clean_list(item: Any, *, items: int = 16, chars: int = 160) -> list[str]:"` | — |
| [SRC-686F71AA50-L001235](../../agents/task_understanding.py#L1235) | 1235 | `"        if not isinstance(item, list):"` | — |
| [SRC-686F71AA50-L001236](../../agents/task_understanding.py#L1236) | 1236 | `"            return []"` | — |
| [SRC-686F71AA50-L001237](../../agents/task_understanding.py#L1237) | 1237 | `"        result: list[str] = []"` | — |
| [SRC-686F71AA50-L001238](../../agents/task_understanding.py#L1238) | 1238 | `"        seen: set[str] = set()"` | — |
| [SRC-686F71AA50-L001239](../../agents/task_understanding.py#L1239) | 1239 | `"        for raw_item in item[:items * 2]:"` | — |
| [SRC-686F71AA50-L001240](../../agents/task_understanding.py#L1240) | 1240 | `"            cleaned = clean_text(raw_item, chars)"` | — |
| [SRC-686F71AA50-L001241](../../agents/task_understanding.py#L1241) | 1241 | `"            key = cleaned.casefold()"` | — |
| [SRC-686F71AA50-L001242](../../agents/task_understanding.py#L1242) | 1242 | `"            if cleaned and key not in seen:"` | — |
| [SRC-686F71AA50-L001243](../../agents/task_understanding.py#L1243) | 1243 | `"                result.append(cleaned)"` | — |
| [SRC-686F71AA50-L001244](../../agents/task_understanding.py#L1244) | 1244 | `"                seen.add(key)"` | — |
| [SRC-686F71AA50-L001245](../../agents/task_understanding.py#L1245) | 1245 | `"            if len(result) >= items:"` | — |
| [SRC-686F71AA50-L001246](../../agents/task_understanding.py#L1246) | 1246 | `"                break"` | — |
| [SRC-686F71AA50-L001247](../../agents/task_understanding.py#L1247) | 1247 | `"        return result"` | — |
| [SRC-686F71AA50-L001248](../../agents/task_understanding.py#L1248) | 1248 | `""` | — |
| [SRC-686F71AA50-L001249](../../agents/task_understanding.py#L1249) | 1249 | `"    raw_constraints = value.get(\"constraints\")"` | — |
| [SRC-686F71AA50-L001250](../../agents/task_understanding.py#L1250) | 1250 | `"    raw_constraints = raw_constraints if isinstance(raw_constraints, dict) else {}"` | — |
| [SRC-686F71AA50-L001251](../../agents/task_understanding.py#L1251) | 1251 | `"    list_constraint_keys = ("` | — |
| [SRC-686F71AA50-L001252](../../agents/task_understanding.py#L1252) | 1252 | `"        \"explicit_locations\", \"explicit_years\", \"explicit_dates\","` | — |
| [SRC-686F71AA50-L001253](../../agents/task_understanding.py#L1253) | 1253 | `"        \"explicit_budgets\", \"explicit_urls\", \"explicit_aspects\", \"source_policies\","` | — |
| [SRC-686F71AA50-L001254](../../agents/task_understanding.py#L1254) | 1254 | `"    )"` | — |
| [SRC-686F71AA50-L001255](../../agents/task_understanding.py#L1255) | 1255 | `"    constraints: dict[str, Any] = {"` | — |
| [SRC-686F71AA50-L001256](../../agents/task_understanding.py#L1256) | 1256 | `"        key: clean_list(raw_constraints.get(key), items=8 if key == \"explicit_aspects\" else 5, chars=300 if key == \"explicit_urls\" else 120)"` | — |
| [SRC-686F71AA50-L001257](../../agents/task_understanding.py#L1257) | 1257 | `"        for key in list_constraint_keys"` | — |
| [SRC-686F71AA50-L001258](../../agents/task_understanding.py#L1258) | 1258 | `"    }"` | — |
| [SRC-686F71AA50-L001259](../../agents/task_understanding.py#L1259) | 1259 | `"    for key in ("` | — |
| [SRC-686F71AA50-L001260](../../agents/task_understanding.py#L1260) | 1260 | `"        \"inline_text_supplied_for_summary\","` | — |
| [SRC-686F71AA50-L001261](../../agents/task_understanding.py#L1261) | 1261 | `"        \"time_sensitive_request\","` | — |
| [SRC-686F71AA50-L001262](../../agents/task_understanding.py#L1262) | 1262 | `"        \"official_site_required\","` | — |
| [SRC-686F71AA50-L001263](../../agents/task_understanding.py#L1263) | 1263 | `"        \"official_destination_required\","` | — |
| [SRC-686F71AA50-L001264](../../agents/task_understanding.py#L1264) | 1264 | `"        \"social_evidence_requested\","` | — |
| [SRC-686F71AA50-L001265](../../agents/task_understanding.py#L1265) | 1265 | `"    ):"` | — |
| [SRC-686F71AA50-L001266](../../agents/task_understanding.py#L1266) | 1266 | `"        constraints[key] = raw_constraints.get(key) is True"` | — |
| [SRC-686F71AA50-L001267](../../agents/task_understanding.py#L1267) | 1267 | `"    language_profile = raw_constraints.get(\"language_profile\")"` | — |
| [SRC-686F71AA50-L001268](../../agents/task_understanding.py#L1268) | 1268 | `"    constraints[\"language_profile\"] = ("` | — |
| [SRC-686F71AA50-L001269](../../agents/task_understanding.py#L1269) | 1269 | `"        language_profile"` | — |
| [SRC-686F71AA50-L001270](../../agents/task_understanding.py#L1270) | 1270 | `"        if isinstance(language_profile, str) and language_profile in {\"ar\", \"en\", \"mixed\", \"und\"}"` | — |
| [SRC-686F71AA50-L001271](../../agents/task_understanding.py#L1271) | 1271 | `"        else \"und\""` | — |
| [SRC-686F71AA50-L001272](../../agents/task_understanding.py#L1272) | 1272 | `"    )"` | — |
| [SRC-686F71AA50-L001273](../../agents/task_understanding.py#L1273) | 1273 | `"    allowed_source_policies = {"` | — |
| [SRC-686F71AA50-L001274](../../agents/task_understanding.py#L1274) | 1274 | `"        \"government_official_destination\", \"official_destination\", \"current_read_page\","` | — |
| [SRC-686F71AA50-L001275](../../agents/task_understanding.py#L1275) | 1275 | `"        \"public_social_content\", \"authoritative_health_content\", \"official_legal_text\","` | — |
| [SRC-686F71AA50-L001276](../../agents/task_understanding.py#L1276) | 1276 | `"        \"task_relevant_sources\", \"unassessed\","` | — |
| [SRC-686F71AA50-L001277](../../agents/task_understanding.py#L1277) | 1277 | `"    }"` | — |
| [SRC-686F71AA50-L001278](../../agents/task_understanding.py#L1278) | 1278 | `"    source_policy = clean_text(raw_constraints.get(\"source_policy\"), 80)"` | — |
| [SRC-686F71AA50-L001279](../../agents/task_understanding.py#L1279) | 1279 | `"    constraints[\"source_policy\"] = source_policy if source_policy in allowed_source_policies else \"unassessed\""` | — |
| [SRC-686F71AA50-L001280](../../agents/task_understanding.py#L1280) | 1280 | `"    constraints[\"source_policies\"] = ["` | — |
| [SRC-686F71AA50-L001281](../../agents/task_understanding.py#L1281) | 1281 | `"        item for item in constraints[\"source_policies\"]"` | — |
| [SRC-686F71AA50-L001282](../../agents/task_understanding.py#L1282) | 1282 | `"        if item in allowed_source_policies"` | — |
| [SRC-686F71AA50-L001283](../../agents/task_understanding.py#L1283) | 1283 | `"    ]"` | — |
| [SRC-686F71AA50-L001284](../../agents/task_understanding.py#L1284) | 1284 | `""` | — |
| [SRC-686F71AA50-L001285](../../agents/task_understanding.py#L1285) | 1285 | `"    raw_preferences = value.get(\"output_preferences\")"` | — |
| [SRC-686F71AA50-L001286](../../agents/task_understanding.py#L1286) | 1286 | `"    raw_preferences = raw_preferences if isinstance(raw_preferences, dict) else {}"` | — |
| [SRC-686F71AA50-L001287](../../agents/task_understanding.py#L1287) | 1287 | `"    preference_keys = ("` | — |
| [SRC-686F71AA50-L001288](../../agents/task_understanding.py#L1288) | 1288 | `"        \"concise\", \"detailed\", \"examples_requested\", \"table_requested\","` | — |
| [SRC-686F71AA50-L001289](../../agents/task_understanding.py#L1289) | 1289 | `"        \"bullets_or_checklist_requested\", \"beginner_friendly_requested\","` | — |
| [SRC-686F71AA50-L001290](../../agents/task_understanding.py#L1290) | 1290 | `"        \"citations_requested\", \"links_requested\", \"json_requested\","` | — |
| [SRC-686F71AA50-L001291](../../agents/task_understanding.py#L1291) | 1291 | `"    )"` | — |
| [SRC-686F71AA50-L001292](../../agents/task_understanding.py#L1292) | 1292 | `"    output_preferences = {key: raw_preferences.get(key) is True for key in preference_keys}"` | — |
| [SRC-686F71AA50-L001293](../../agents/task_understanding.py#L1293) | 1293 | `""` | — |
| [SRC-686F71AA50-L001294](../../agents/task_understanding.py#L1294) | 1294 | `"    raw_context = value.get(\"context_resolution\")"` | — |
| [SRC-686F71AA50-L001295](../../agents/task_understanding.py#L1295) | 1295 | `"    raw_context = raw_context if isinstance(raw_context, dict) else {}"` | — |
| [SRC-686F71AA50-L001296](../../agents/task_understanding.py#L1296) | 1296 | `"    raw_slots = raw_context.get(\"slots\")"` | — |
| [SRC-686F71AA50-L001297](../../agents/task_understanding.py#L1297) | 1297 | `"    slots: dict[str, str] = {}"` | — |
| [SRC-686F71AA50-L001298](../../agents/task_understanding.py#L1298) | 1298 | `"    if isinstance(raw_slots, dict):"` | — |
| [SRC-686F71AA50-L001299](../../agents/task_understanding.py#L1299) | 1299 | `"        for raw_key, raw_value in list(raw_slots.items())[:16]:"` | — |
| [SRC-686F71AA50-L001300](../../agents/task_understanding.py#L1300) | 1300 | `"            key = clean_text(raw_key, 40)"` | — |
| [SRC-686F71AA50-L001301](../../agents/task_understanding.py#L1301) | 1301 | `"            item = clean_text(raw_value, 180)"` | — |
| [SRC-686F71AA50-L001302](../../agents/task_understanding.py#L1302) | 1302 | `"            if key and item:"` | — |
| [SRC-686F71AA50-L001303](../../agents/task_understanding.py#L1303) | 1303 | `"                slots[key] = item"` | — |
| [SRC-686F71AA50-L001304](../../agents/task_understanding.py#L1304) | 1304 | `"    context_resolution = {"` | — |
| [SRC-686F71AA50-L001305](../../agents/task_understanding.py#L1305) | 1305 | `"        \"method\": clean_text(raw_context.get(\"method\"), 80) or \"not_provided\","` | — |
| [SRC-686F71AA50-L001306](../../agents/task_understanding.py#L1306) | 1306 | `"        \"resolved_question\": clean_text(raw_context.get(\"resolved_question\"), MAX_TASK_CHARS),"` | — |
| [SRC-686F71AA50-L001307](../../agents/task_understanding.py#L1307) | 1307 | `"        \"topic\": clean_text(raw_context.get(\"topic\"), 180),"` | — |
| [SRC-686F71AA50-L001308](../../agents/task_understanding.py#L1308) | 1308 | `"        \"entities\": clean_list(raw_context.get(\"entities\"), items=8, chars=120),"` | — |
| [SRC-686F71AA50-L001309](../../agents/task_understanding.py#L1309) | 1309 | `"        \"slots\": slots,"` | — |
| [SRC-686F71AA50-L001310](../../agents/task_understanding.py#L1310) | 1310 | `"        \"changed_slots\": clean_list(raw_context.get(\"changed_slots\"), items=8, chars=40),"` | — |
| [SRC-686F71AA50-L001311](../../agents/task_understanding.py#L1311) | 1311 | `"        \"is_follow_up\": raw_context.get(\"is_follow_up\") is True,"` | — |
| [SRC-686F71AA50-L001312](../../agents/task_understanding.py#L1312) | 1312 | `"        \"topic_shift\": raw_context.get(\"topic_shift\") is True,"` | — |
| [SRC-686F71AA50-L001313](../../agents/task_understanding.py#L1313) | 1313 | `"        \"resolution_basis\": clean_text(raw_context.get(\"resolution_basis\"), 80) or \"unassessed\","` | — |
| [SRC-686F71AA50-L001314](../../agents/task_understanding.py#L1314) | 1314 | `"        \"confidence_band\": ("` | — |
| [SRC-686F71AA50-L001315](../../agents/task_understanding.py#L1315) | 1315 | `"            raw_context.get(\"confidence_band\")"` | — |
| [SRC-686F71AA50-L001316](../../agents/task_understanding.py#L1316) | 1316 | `"            if isinstance(raw_context.get(\"confidence_band\"), str)"` | — |
| [SRC-686F71AA50-L001317](../../agents/task_understanding.py#L1317) | 1317 | `"            and raw_context.get(\"confidence_band\") in {\"low\", \"medium\", \"high\", \"unassessed\"}"` | — |
| [SRC-686F71AA50-L001318](../../agents/task_understanding.py#L1318) | 1318 | `"            else \"unassessed\""` | — |
| [SRC-686F71AA50-L001319](../../agents/task_understanding.py#L1319) | 1319 | `"        ),"` | — |
| [SRC-686F71AA50-L001320](../../agents/task_understanding.py#L1320) | 1320 | `"        \"needs_clarification\": raw_context.get(\"needs_clarification\") is True,"` | — |
| [SRC-686F71AA50-L001321](../../agents/task_understanding.py#L1321) | 1321 | `"        \"unresolved_references\": clean_list(raw_context.get(\"unresolved_references\"), items=8, chars=100),"` | — |
| [SRC-686F71AA50-L001322](../../agents/task_understanding.py#L1322) | 1322 | `"    }"` | — |
| [SRC-686F71AA50-L001323](../../agents/task_understanding.py#L1323) | 1323 | `""` | — |
| [SRC-686F71AA50-L001324](../../agents/task_understanding.py#L1324) | 1324 | `"    raw_hypotheses = value.get(\"hypothesis_interpretations\")"` | — |
| [SRC-686F71AA50-L001325](../../agents/task_understanding.py#L1325) | 1325 | `"    hypotheses: list[dict[str, Any]] = []"` | — |
| [SRC-686F71AA50-L001326](../../agents/task_understanding.py#L1326) | 1326 | `"    if isinstance(raw_hypotheses, list):"` | — |
| [SRC-686F71AA50-L001327](../../agents/task_understanding.py#L1327) | 1327 | `"        for item in raw_hypotheses[:8]:"` | — |
| [SRC-686F71AA50-L001328](../../agents/task_understanding.py#L1328) | 1328 | `"            if not isinstance(item, dict):"` | — |
| [SRC-686F71AA50-L001329](../../agents/task_understanding.py#L1329) | 1329 | `"                continue"` | — |
| [SRC-686F71AA50-L001330](../../agents/task_understanding.py#L1330) | 1330 | `"            count = item.get(\"matched_signal_count\")"` | — |
| [SRC-686F71AA50-L001331](../../agents/task_understanding.py#L1331) | 1331 | `"            hypotheses.append({"` | — |
| [SRC-686F71AA50-L001332](../../agents/task_understanding.py#L1332) | 1332 | `"                \"family\": clean_text(item.get(\"family\"), 80),"` | — |
| [SRC-686F71AA50-L001333](../../agents/task_understanding.py#L1333) | 1333 | `"                \"matched_signal_count\": max(0, min(32, count)) if isinstance(count, int) else 0,"` | — |
| [SRC-686F71AA50-L001334](../../agents/task_understanding.py#L1334) | 1334 | `"                \"signals\": clean_list(item.get(\"signals\"), items=4, chars=100),"` | — |
| [SRC-686F71AA50-L001335](../../agents/task_understanding.py#L1335) | 1335 | `"                \"status\": clean_text(item.get(\"status\"), 60) or \"unassessed\","` | — |
| [SRC-686F71AA50-L001336](../../agents/task_understanding.py#L1336) | 1336 | `"                \"selected\": item.get(\"selected\") is True,"` | — |
| [SRC-686F71AA50-L001337](../../agents/task_understanding.py#L1337) | 1337 | `"            })"` | — |
| [SRC-686F71AA50-L001338](../../agents/task_understanding.py#L1338) | 1338 | `""` | — |
| [SRC-686F71AA50-L001339](../../agents/task_understanding.py#L1339) | 1339 | `"    allowed_families = {"` | — |
| [SRC-686F71AA50-L001340](../../agents/task_understanding.py#L1340) | 1340 | `"        name for name in _PATTERNS if not name.startswith(\"output_\")"` | — |
| [SRC-686F71AA50-L001341](../../agents/task_understanding.py#L1341) | 1341 | `"    } \| {\"general_question\", \"ambiguous_or_incomplete\", \"web_research\"}"` | — |
| [SRC-686F71AA50-L001342](../../agents/task_understanding.py#L1342) | 1342 | `"    raw_family = clean_text(value.get(\"task_family\"), 80)"` | — |
| [SRC-686F71AA50-L001343](../../agents/task_understanding.py#L1343) | 1343 | `"    raw_mode = clean_text(value.get(\"mode\"), 20)"` | — |
| [SRC-686F71AA50-L001344](../../agents/task_understanding.py#L1344) | 1344 | `"    raw_route = clean_text(value.get(\"intent_route\"), 40)"` | — |
| [SRC-686F71AA50-L001345](../../agents/task_understanding.py#L1345) | 1345 | `"    allowed_routes = {"` | — |
| [SRC-686F71AA50-L001346](../../agents/task_understanding.py#L1346) | 1346 | `"        \"LOCAL\", \"MODEL_ONLY\", \"CLARIFY\", \"WEB_SIMPLE\", \"WEB_DEEP\","` | — |
| [SRC-686F71AA50-L001347](../../agents/task_understanding.py#L1347) | 1347 | `"        \"LEAD_GENERATION\", \"BUDGET_EXHAUSTED\", \"deterministic_fallback\","` | — |
| [SRC-686F71AA50-L001348](../../agents/task_understanding.py#L1348) | 1348 | `"        \"validated_language_model_plan\", \"unassessed\","` | — |
| [SRC-686F71AA50-L001349](../../agents/task_understanding.py#L1349) | 1349 | `"    }"` | — |
| [SRC-686F71AA50-L001350](../../agents/task_understanding.py#L1350) | 1350 | `"    allowed_tools = {"` | — |
| [SRC-686F71AA50-L001351](../../agents/task_understanding.py#L1351) | 1351 | `"        \"web_search\", \"page_fetch\", \"public_social_search_if_configured\","` | — |
| [SRC-686F71AA50-L001352](../../agents/task_understanding.py#L1352) | 1352 | `"        \"language_model_generation_if_configured\", \"claim_review_if_configured\","` | — |
| [SRC-686F71AA50-L001353](../../agents/task_understanding.py#L1353) | 1353 | `"    }"` | — |
| [SRC-686F71AA50-L001354](../../agents/task_understanding.py#L1354) | 1354 | `"    allowed_slots = {"` | — |
| [SRC-686F71AA50-L001355](../../agents/task_understanding.py#L1355) | 1355 | `"        \"aspect\", \"audience\", \"budget\", \"capacity\", \"country\", \"currency\","` | — |
| [SRC-686F71AA50-L001356](../../agents/task_understanding.py#L1356) | 1356 | `"        \"entity\", \"goal\", \"language\", \"location\", \"model\", \"platform\","` | — |
| [SRC-686F71AA50-L001357](../../agents/task_understanding.py#L1357) | 1357 | `"        \"product\", \"time_range\", \"variant\", \"version\","` | — |
| [SRC-686F71AA50-L001358](../../agents/task_understanding.py#L1358) | 1358 | `"    }"` | — |
| [SRC-686F71AA50-L001359](../../agents/task_understanding.py#L1359) | 1359 | `"    context_resolution[\"slots\"] = {"` | — |
| [SRC-686F71AA50-L001360](../../agents/task_understanding.py#L1360) | 1360 | `"        key: item for key, item in context_resolution[\"slots\"].items()"` | — |
| [SRC-686F71AA50-L001361](../../agents/task_understanding.py#L1361) | 1361 | `"        if key in allowed_slots"` | — |
| [SRC-686F71AA50-L001362](../../agents/task_understanding.py#L1362) | 1362 | `"    }"` | — |
| [SRC-686F71AA50-L001363](../../agents/task_understanding.py#L1363) | 1363 | `"    hypotheses = ["` | — |
| [SRC-686F71AA50-L001364](../../agents/task_understanding.py#L1364) | 1364 | `"        item for item in hypotheses"` | — |
| [SRC-686F71AA50-L001365](../../agents/task_understanding.py#L1365) | 1365 | `"        if item.get(\"family\") in allowed_families"` | — |
| [SRC-686F71AA50-L001366](../../agents/task_understanding.py#L1366) | 1366 | `"    ]"` | — |
| [SRC-686F71AA50-L001367](../../agents/task_understanding.py#L1367) | 1367 | `"    raw_secondary = clean_list(value.get(\"secondary_task_types\"), items=16, chars=80)"` | — |
| [SRC-686F71AA50-L001368](../../agents/task_understanding.py#L1368) | 1368 | `"    spec = {"` | — |
| [SRC-686F71AA50-L001369](../../agents/task_understanding.py#L1369) | 1369 | `"        \"schema\": \"omarai.task_spec.v1\","` | — |
| [SRC-686F71AA50-L001370](../../agents/task_understanding.py#L1370) | 1370 | `"        \"task_family\": raw_family if raw_family in allowed_families else \"general_question\","` | — |
| [SRC-686F71AA50-L001371](../../agents/task_understanding.py#L1371) | 1371 | `"        \"mode\": raw_mode if raw_mode in SUPPORTED_MODES else \"auto\","` | — |
| [SRC-686F71AA50-L001372](../../agents/task_understanding.py#L1372) | 1372 | `"        \"intent_route\": raw_route if raw_route in allowed_routes else \"unassessed\","` | — |
| [SRC-686F71AA50-L001373](../../agents/task_understanding.py#L1373) | 1373 | `"        \"classification_method\": clean_text(value.get(\"classification_method\"), 100),"` | — |
| [SRC-686F71AA50-L001374](../../agents/task_understanding.py#L1374) | 1374 | `"        \"classification_is_probability\": False,"` | — |
| [SRC-686F71AA50-L001375](../../agents/task_understanding.py#L1375) | 1375 | `"        \"ambiguity_status\": clean_text(value.get(\"ambiguity_status\"), 80) or \"unassessed\","` | — |
| [SRC-686F71AA50-L001376](../../agents/task_understanding.py#L1376) | 1376 | `"        \"missing_required_inputs\": ["` | — |
| [SRC-686F71AA50-L001377](../../agents/task_understanding.py#L1377) | 1377 | `"            item for item in clean_list(value.get(\"missing_required_inputs\"), items=8, chars=100)"` | — |
| [SRC-686F71AA50-L001378](../../agents/task_understanding.py#L1378) | 1378 | `"            if item in {"` | — |
| [SRC-686F71AA50-L001379](../../agents/task_understanding.py#L1379) | 1379 | `"                \"unresolved_referent_or_incomplete_request\","` | — |
| [SRC-686F71AA50-L001380](../../agents/task_understanding.py#L1380) | 1380 | `"                \"official_destination_target_entity\","` | — |
| [SRC-686F71AA50-L001381](../../agents/task_understanding.py#L1381) | 1381 | `"                \"summary_source_url_or_pasted_text\","` | — |
| [SRC-686F71AA50-L001382](../../agents/task_understanding.py#L1382) | 1382 | `"            }"` | — |
| [SRC-686F71AA50-L001383](../../agents/task_understanding.py#L1383) | 1383 | `"        ],"` | — |
| [SRC-686F71AA50-L001384](../../agents/task_understanding.py#L1384) | 1384 | `"        \"requires_clarification\": value.get(\"requires_clarification\") is True,"` | — |
| [SRC-686F71AA50-L001385](../../agents/task_understanding.py#L1385) | 1385 | `"        \"clarification_reason\": clean_text(value.get(\"clarification_reason\"), 80) or \"unassessed\","` | — |
| [SRC-686F71AA50-L001386](../../agents/task_understanding.py#L1386) | 1386 | `"        \"context_resolution\": context_resolution,"` | — |
| [SRC-686F71AA50-L001387](../../agents/task_understanding.py#L1387) | 1387 | `"        \"secondary_task_types\": ["` | — |
| [SRC-686F71AA50-L001388](../../agents/task_understanding.py#L1388) | 1388 | `"            item for item in raw_secondary if item in allowed_families"` | — |
| [SRC-686F71AA50-L001389](../../agents/task_understanding.py#L1389) | 1389 | `"        ],"` | — |
| [SRC-686F71AA50-L001390](../../agents/task_understanding.py#L1390) | 1390 | `"        \"constraints\": constraints,"` | — |
| [SRC-686F71AA50-L001391](../../agents/task_understanding.py#L1391) | 1391 | `"        \"output_preferences\": output_preferences,"` | — |
| [SRC-686F71AA50-L001392](../../agents/task_understanding.py#L1392) | 1392 | `"        \"evidence_requirements\": clean_list(value.get(\"evidence_requirements\"), items=32, chars=180),"` | — |
| [SRC-686F71AA50-L001393](../../agents/task_understanding.py#L1393) | 1393 | `"        \"query_strategies\": clean_list(value.get(\"query_strategies\"), items=32, chars=100),"` | — |
| [SRC-686F71AA50-L001394](../../agents/task_understanding.py#L1394) | 1394 | `"        \"tool_requirements\": ["` | — |
| [SRC-686F71AA50-L001395](../../agents/task_understanding.py#L1395) | 1395 | `"            item for item in clean_list(value.get(\"tool_requirements\"), items=12, chars=100)"` | — |
| [SRC-686F71AA50-L001396](../../agents/task_understanding.py#L1396) | 1396 | `"            if item in allowed_tools"` | — |
| [SRC-686F71AA50-L001397](../../agents/task_understanding.py#L1397) | 1397 | `"        ],"` | — |
| [SRC-686F71AA50-L001398](../../agents/task_understanding.py#L1398) | 1398 | `"        \"decision_checks\": clean_list(value.get(\"decision_checks\"), items=24, chars=120),"` | — |
| [SRC-686F71AA50-L001399](../../agents/task_understanding.py#L1399) | 1399 | `"        \"reasoning_strategy_ids\": ["` | — |
| [SRC-686F71AA50-L001400](../../agents/task_understanding.py#L1400) | 1400 | `"            item for item in clean_list(value.get(\"reasoning_strategy_ids\"), items=12, chars=80)"` | — |
| [SRC-686F71AA50-L001401](../../agents/task_understanding.py#L1401) | 1401 | `"            if item in _REASONING_GUIDANCE"` | — |
| [SRC-686F71AA50-L001402](../../agents/task_understanding.py#L1402) | 1402 | `"        ],"` | — |
| [SRC-686F71AA50-L001403](../../agents/task_understanding.py#L1403) | 1403 | `"        # The matrix is code-owned. Ignore arbitrary incoming rows and return the"` | — |
| [SRC-686F71AA50-L001404](../../agents/task_understanding.py#L1404) | 1404 | `"        # canonical allowlisted policy so untrusted task/planner data cannot rewrite it."` | — |
| [SRC-686F71AA50-L001405](../../agents/task_understanding.py#L1405) | 1405 | `"        \"decision_matrix\": [dict(row) for row in _DECISION_MATRIX],"` | — |
| [SRC-686F71AA50-L001406](../../agents/task_understanding.py#L1406) | 1406 | `"        \"hypothesis_interpretations\": hypotheses,"` | — |
| [SRC-686F71AA50-L001407](../../agents/task_understanding.py#L1407) | 1407 | `"        \"limits\": {"` | — |
| [SRC-686F71AA50-L001408](../../agents/task_understanding.py#L1408) | 1408 | `"            \"max_question_chars\": MAX_TASK_CHARS,"` | — |
| [SRC-686F71AA50-L001409](../../agents/task_understanding.py#L1409) | 1409 | `"            \"max_aspects\": MAX_TASK_ASPECTS,"` | — |
| [SRC-686F71AA50-L001410](../../agents/task_understanding.py#L1410) | 1410 | `"            \"max_query_strategies\": MAX_STRATEGY_QUERIES,"` | — |
| [SRC-686F71AA50-L001411](../../agents/task_understanding.py#L1411) | 1411 | `"        },"` | — |
| [SRC-686F71AA50-L001412](../../agents/task_understanding.py#L1412) | 1412 | `"        \"claim\": \"task planning metadata only; not semantic certainty or factual verification\","` | — |
| [SRC-686F71AA50-L001413](../../agents/task_understanding.py#L1413) | 1413 | `"    }"` | — |
| [SRC-686F71AA50-L001414](../../agents/task_understanding.py#L1414) | 1414 | `"    for key in (\"planner_freshness\", \"planner_depth\"):"` | — |
| [SRC-686F71AA50-L001415](../../agents/task_understanding.py#L1415) | 1415 | `"        if key in value:"` | — |
| [SRC-686F71AA50-L001416](../../agents/task_understanding.py#L1416) | 1416 | `"            spec[key] = clean_text(value.get(key), 40) or \"unknown\""` | — |
| [SRC-686F71AA50-L001417](../../agents/task_understanding.py#L1417) | 1417 | `"    return spec"` | — |
## الوكيل والمنطق

### FILE-FC84E5B115 — [agents/text_normalization.py](../../agents/text_normalization.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-FC84E5B115-L000001](../../agents/text_normalization.py#L1) | 1 | `"\"\"\"Shared public text normalization primitives for Arabic and English matching."` | — |
| [SRC-FC84E5B115-L000002](../../agents/text_normalization.py#L2) | 2 | `""` | — |
| [SRC-FC84E5B115-L000003](../../agents/text_normalization.py#L3) | 3 | `"This module owns Unicode/Arabic normalization and token extraction. It has no knowledge"` | — |
| [SRC-FC84E5B115-L000004](../../agents/text_normalization.py#L4) | 4 | `"of search, sources, citations, or answer policy."` | — |
| [SRC-FC84E5B115-L000005](../../agents/text_normalization.py#L5) | 5 | `"\"\"\""` | — |
| [SRC-FC84E5B115-L000006](../../agents/text_normalization.py#L6) | 6 | `"from __future__ import annotations"` | — |
| [SRC-FC84E5B115-L000007](../../agents/text_normalization.py#L7) | 7 | `""` | — |
| [SRC-FC84E5B115-L000008](../../agents/text_normalization.py#L8) | 8 | `"import re"` | — |
| [SRC-FC84E5B115-L000009](../../agents/text_normalization.py#L9) | 9 | `"import unicodedata"` | — |
| [SRC-FC84E5B115-L000010](../../agents/text_normalization.py#L10) | 10 | `"from typing import Any"` | — |
| [SRC-FC84E5B115-L000011](../../agents/text_normalization.py#L11) | 11 | `""` | — |
| [SRC-FC84E5B115-L000012](../../agents/text_normalization.py#L12) | 12 | `"_DIGITS = str.maketrans(\"٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹\", \"01234567890123456789\")"` | — |
| [SRC-FC84E5B115-L000013](../../agents/text_normalization.py#L13) | 13 | `"_ARABIC_NORMALIZATION = str.maketrans({"` | — |
| [SRC-FC84E5B115-L000014](../../agents/text_normalization.py#L14) | 14 | `"    \"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ٱ\": \"ا\", \"ى\": \"ي\","` | — |
| [SRC-FC84E5B115-L000015](../../agents/text_normalization.py#L15) | 15 | `"    \"ؤ\": \"و\", \"ئ\": \"ي\", \"ة\": \"ه\", \"ـ\": \"\","` | — |
| [SRC-FC84E5B115-L000016](../../agents/text_normalization.py#L16) | 16 | `"})"` | — |
| [SRC-FC84E5B115-L000017](../../agents/text_normalization.py#L17) | 17 | `"_DIACRITICS = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-FC84E5B115-L000018](../../agents/text_normalization.py#L18) | 18 | `"_TOKEN = re.compile(r\"[a-z0-9]+\|[\\u0621-\\u064A\\u0660-\\u0669]+\", re.IGNORECASE)"` | — |
| [SRC-FC84E5B115-L000019](../../agents/text_normalization.py#L19) | 19 | `""` | — |
| [SRC-FC84E5B115-L000020](../../agents/text_normalization.py#L20) | 20 | `"_STOPWORDS = {"` | — |
| [SRC-FC84E5B115-L000021](../../agents/text_normalization.py#L21) | 21 | `"    \"من\", \"في\", \"على\", \"عن\", \"الى\", \"و\", \"او\", \"هل\", \"ما\", \"ماذا\", \"كيف\","` | — |
| [SRC-FC84E5B115-L000022](../../agents/text_normalization.py#L22) | 22 | `"    \"مع\", \"بين\", \"هذا\", \"هذه\", \"ذلك\", \"تلك\", \"الذي\", \"التي\", \"هو\", \"هي\","` | — |
| [SRC-FC84E5B115-L000023](../../agents/text_normalization.py#L23) | 23 | `"    \"the\", \"a\", \"an\", \"and\", \"or\", \"in\", \"on\", \"of\", \"to\", \"for\", \"with\","` | — |
| [SRC-FC84E5B115-L000024](../../agents/text_normalization.py#L24) | 24 | `"    \"from\", \"is\", \"are\", \"what\", \"which\", \"who\", \"how\", \"why\", \"when\","` | — |
| [SRC-FC84E5B115-L000025](../../agents/text_normalization.py#L25) | 25 | `"    \"where\", \"compare\", \"comparison\", \"based\", \"terms\", \"respect\","` | — |
| [SRC-FC84E5B115-L000026](../../agents/text_normalization.py#L26) | 26 | `"}"` | — |
| [SRC-FC84E5B115-L000027](../../agents/text_normalization.py#L27) | 27 | `""` | — |
| [SRC-FC84E5B115-L000028](../../agents/text_normalization.py#L28) | 28 | `""` | — |
| [SRC-FC84E5B115-L000029](../../agents/text_normalization.py#L29) | 29 | `"def normalize_text(value: Any) -> str:"` | — |
| [SRC-FC84E5B115-L000030](../../agents/text_normalization.py#L30) | 30 | `"    \"\"\"Normalize Unicode, Arabic letter variants, diacritics, and Arabic-Indic digits.\"\"\""` | — |
| [SRC-FC84E5B115-L000031](../../agents/text_normalization.py#L31) | 31 | `"    text = unicodedata.normalize(\"NFKC\", str(value or \"\")).casefold().translate(_DIGITS)"` | — |
| [SRC-FC84E5B115-L000032](../../agents/text_normalization.py#L32) | 32 | `"    text = _DIACRITICS.sub(\"\", text).translate(_ARABIC_NORMALIZATION)"` | — |
| [SRC-FC84E5B115-L000033](../../agents/text_normalization.py#L33) | 33 | `"    return text"` | — |
| [SRC-FC84E5B115-L000034](../../agents/text_normalization.py#L34) | 34 | `""` | — |
| [SRC-FC84E5B115-L000035](../../agents/text_normalization.py#L35) | 35 | `""` | — |
| [SRC-FC84E5B115-L000036](../../agents/text_normalization.py#L36) | 36 | `"def tokenize_text(value: Any, *, drop_stopwords: bool = False) -> list[str]:"` | — |
| [SRC-FC84E5B115-L000037](../../agents/text_normalization.py#L37) | 37 | `"    \"\"\"Tokenize normalized Arabic/English text with optional stopword removal.\"\"\""` | — |
| [SRC-FC84E5B115-L000038](../../agents/text_normalization.py#L38) | 38 | `"    tokens = _TOKEN.findall(normalize_text(value))"` | — |
| [SRC-FC84E5B115-L000039](../../agents/text_normalization.py#L39) | 39 | `"    if drop_stopwords:"` | — |
| [SRC-FC84E5B115-L000040](../../agents/text_normalization.py#L40) | 40 | `"        tokens = [token for token in tokens if token not in _STOPWORDS]"` | — |
| [SRC-FC84E5B115-L000041](../../agents/text_normalization.py#L41) | 41 | `"    return tokens"` | — |
## الوكيل والمنطق

### FILE-0799EEEB02 — [agents/tool_execution_status.py](../../agents/tool_execution_status.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-0799EEEB02-L000001](../../agents/tool_execution_status.py#L1) | 1 | `"\"\"\"Truthful task-tool execution status, separate from task planning and evidence quality.\"\"\""` | — |
| [SRC-0799EEEB02-L000002](../../agents/tool_execution_status.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-0799EEEB02-L000003](../../agents/tool_execution_status.py#L3) | 3 | `""` | — |
| [SRC-0799EEEB02-L000004](../../agents/tool_execution_status.py#L4) | 4 | `"from typing import Any"` | — |
| [SRC-0799EEEB02-L000005](../../agents/tool_execution_status.py#L5) | 5 | `""` | — |
| [SRC-0799EEEB02-L000006](../../agents/tool_execution_status.py#L6) | 6 | `"_TOOL_LABELS = {"` | — |
| [SRC-0799EEEB02-L000007](../../agents/tool_execution_status.py#L7) | 7 | `"    \"web_search\": \"البحث على الويب\","` | — |
| [SRC-0799EEEB02-L000008](../../agents/tool_execution_status.py#L8) | 8 | `"    \"page_fetch\": \"فتح الصفحات وقراءة النص\","` | — |
| [SRC-0799EEEB02-L000009](../../agents/tool_execution_status.py#L9) | 9 | `"    \"public_social_search_if_configured\": \"البحث في المحتوى الاجتماعي العام\","` | — |
| [SRC-0799EEEB02-L000010](../../agents/tool_execution_status.py#L10) | 10 | `"    \"language_model_generation_if_configured\": \"توليد الإجابة بالنموذج\","` | — |
| [SRC-0799EEEB02-L000011](../../agents/tool_execution_status.py#L11) | 11 | `"    \"claim_review_if_configured\": \"مراجعة الإجابة بمساعدة النموذج\","` | — |
| [SRC-0799EEEB02-L000012](../../agents/tool_execution_status.py#L12) | 12 | `"}"` | — |
| [SRC-0799EEEB02-L000013](../../agents/tool_execution_status.py#L13) | 13 | `"_ERROR_OUTCOMES = {"` | — |
| [SRC-0799EEEB02-L000014](../../agents/tool_execution_status.py#L14) | 14 | `"    \"attempted_research_error\","` | — |
| [SRC-0799EEEB02-L000015](../../agents/tool_execution_status.py#L15) | 15 | `"    \"unknown_after_research_error\","` | — |
| [SRC-0799EEEB02-L000016](../../agents/tool_execution_status.py#L16) | 16 | `"    \"unknown_after_budget_exhaustion\","` | — |
| [SRC-0799EEEB02-L000017](../../agents/tool_execution_status.py#L17) | 17 | `"}"` | — |
| [SRC-0799EEEB02-L000018](../../agents/tool_execution_status.py#L18) | 18 | `"_SOCIAL_PLATFORMS = {"` | — |
| [SRC-0799EEEB02-L000019](../../agents/tool_execution_status.py#L19) | 19 | `"    \"reddit\", \"youtube\", \"facebook\", \"instagram\", \"x\", \"twitter\","` | — |
| [SRC-0799EEEB02-L000020](../../agents/tool_execution_status.py#L20) | 20 | `"    \"tiktok\", \"linkedin\", \"threads\", \"bluesky\","` | — |
| [SRC-0799EEEB02-L000021](../../agents/tool_execution_status.py#L21) | 21 | `"}"` | — |
| [SRC-0799EEEB02-L000022](../../agents/tool_execution_status.py#L22) | 22 | `""` | — |
| [SRC-0799EEEB02-L000023](../../agents/tool_execution_status.py#L23) | 23 | `""` | — |
| [SRC-0799EEEB02-L000024](../../agents/tool_execution_status.py#L24) | 24 | `"def _nonnegative_int(value: Any) -> int \| None:"` | — |
| [SRC-0799EEEB02-L000025](../../agents/tool_execution_status.py#L25) | 25 | `"    if isinstance(value, bool):"` | — |
| [SRC-0799EEEB02-L000026](../../agents/tool_execution_status.py#L26) | 26 | `"        return None"` | — |
| [SRC-0799EEEB02-L000027](../../agents/tool_execution_status.py#L27) | 27 | `"    if isinstance(value, int):"` | — |
| [SRC-0799EEEB02-L000028](../../agents/tool_execution_status.py#L28) | 28 | `"        return max(0, value)"` | — |
| [SRC-0799EEEB02-L000029](../../agents/tool_execution_status.py#L29) | 29 | `"    if isinstance(value, float) and value.is_integer():"` | — |
| [SRC-0799EEEB02-L000030](../../agents/tool_execution_status.py#L30) | 30 | `"        return max(0, int(value))"` | — |
| [SRC-0799EEEB02-L000031](../../agents/tool_execution_status.py#L31) | 31 | `"    return None"` | — |
| [SRC-0799EEEB02-L000032](../../agents/tool_execution_status.py#L32) | 32 | `""` | — |
| [SRC-0799EEEB02-L000033](../../agents/tool_execution_status.py#L33) | 33 | `""` | — |
| [SRC-0799EEEB02-L000034](../../agents/tool_execution_status.py#L34) | 34 | `"def _status_row("` | — |
| [SRC-0799EEEB02-L000035](../../agents/tool_execution_status.py#L35) | 35 | `"    tool: str,"` | — |
| [SRC-0799EEEB02-L000036](../../agents/tool_execution_status.py#L36) | 36 | `"    required: bool,"` | — |
| [SRC-0799EEEB02-L000037](../../agents/tool_execution_status.py#L37) | 37 | `"    status: str,"` | — |
| [SRC-0799EEEB02-L000038](../../agents/tool_execution_status.py#L38) | 38 | `"    basis: dict[str, Any],"` | — |
| [SRC-0799EEEB02-L000039](../../agents/tool_execution_status.py#L39) | 39 | `") -> dict[str, Any]:"` | — |
| [SRC-0799EEEB02-L000040](../../agents/tool_execution_status.py#L40) | 40 | `"    return {"` | — |
| [SRC-0799EEEB02-L000041](../../agents/tool_execution_status.py#L41) | 41 | `"        \"tool\": tool,"` | — |
| [SRC-0799EEEB02-L000042](../../agents/tool_execution_status.py#L42) | 42 | `"        \"label_ar\": _TOOL_LABELS[tool],"` | — |
| [SRC-0799EEEB02-L000043](../../agents/tool_execution_status.py#L43) | 43 | `"        \"required_by_task_spec\": required,"` | — |
| [SRC-0799EEEB02-L000044](../../agents/tool_execution_status.py#L44) | 44 | `"        \"status\": status,"` | — |
| [SRC-0799EEEB02-L000045](../../agents/tool_execution_status.py#L45) | 45 | `"        \"basis\": basis,"` | — |
| [SRC-0799EEEB02-L000046](../../agents/tool_execution_status.py#L46) | 46 | `"        \"semantics\": ("` | — |
| [SRC-0799EEEB02-L000047](../../agents/tool_execution_status.py#L47) | 47 | `"            \"حالة مسار التنفيذ المرصودة فقط؛ لا تثبت صحة المحتوى أو كفاية الدليل.\""` | — |
| [SRC-0799EEEB02-L000048](../../agents/tool_execution_status.py#L48) | 48 | `"        ),"` | — |
| [SRC-0799EEEB02-L000049](../../agents/tool_execution_status.py#L49) | 49 | `"    }"` | — |
| [SRC-0799EEEB02-L000050](../../agents/tool_execution_status.py#L50) | 50 | `""` | — |
| [SRC-0799EEEB02-L000051](../../agents/tool_execution_status.py#L51) | 51 | `""` | — |
| [SRC-0799EEEB02-L000052](../../agents/tool_execution_status.py#L52) | 52 | `"def build_tool_execution_matrix("` | — |
| [SRC-0799EEEB02-L000053](../../agents/tool_execution_status.py#L53) | 53 | `"    task_spec: dict[str, Any] \| None,"` | — |
| [SRC-0799EEEB02-L000054](../../agents/tool_execution_status.py#L54) | 54 | `"    result: dict[str, Any] \| None,"` | — |
| [SRC-0799EEEB02-L000055](../../agents/tool_execution_status.py#L55) | 55 | `"    report: dict[str, Any] \| None,"` | — |
| [SRC-0799EEEB02-L000056](../../agents/tool_execution_status.py#L56) | 56 | `") -> list[dict[str, Any]]:"` | — |
| [SRC-0799EEEB02-L000057](../../agents/tool_execution_status.py#L57) | 57 | `"    \"\"\"Map planned tool requirements to observed outcomes without inferring success.\"\"\""` | — |
| [SRC-0799EEEB02-L000058](../../agents/tool_execution_status.py#L58) | 58 | `"    spec = task_spec if isinstance(task_spec, dict) else {}"` | — |
| [SRC-0799EEEB02-L000059](../../agents/tool_execution_status.py#L59) | 59 | `"    output = result if isinstance(result, dict) else {}"` | — |
| [SRC-0799EEEB02-L000060](../../agents/tool_execution_status.py#L60) | 60 | `"    search_report = report if isinstance(report, dict) else {}"` | — |
| [SRC-0799EEEB02-L000061](../../agents/tool_execution_status.py#L61) | 61 | `"    requirements = spec.get(\"tool_requirements\")"` | — |
| [SRC-0799EEEB02-L000062](../../agents/tool_execution_status.py#L62) | 62 | `"    required = {"` | — |
| [SRC-0799EEEB02-L000063](../../agents/tool_execution_status.py#L63) | 63 | `"        item for item in requirements"` | — |
| [SRC-0799EEEB02-L000064](../../agents/tool_execution_status.py#L64) | 64 | `"        if isinstance(item, str) and item in _TOOL_LABELS"` | — |
| [SRC-0799EEEB02-L000065](../../agents/tool_execution_status.py#L65) | 65 | `"    } if isinstance(requirements, list) else set()"` | — |
| [SRC-0799EEEB02-L000066](../../agents/tool_execution_status.py#L66) | 66 | `""` | — |
| [SRC-0799EEEB02-L000067](../../agents/tool_execution_status.py#L67) | 67 | `"    outcome = str(search_report.get(\"search_outcome\") or \"unknown\")"` | — |
| [SRC-0799EEEB02-L000068](../../agents/tool_execution_status.py#L68) | 68 | `"    attempted = output.get(\"search_attempted\", search_report.get(\"search_attempted\"))"` | — |
| [SRC-0799EEEB02-L000069](../../agents/tool_execution_status.py#L69) | 69 | `"    reported_accepted_sources = _nonnegative_int("` | — |
| [SRC-0799EEEB02-L000070](../../agents/tool_execution_status.py#L70) | 70 | `"        search_report.get(\"usable_sources_after_filtering\")"` | — |
| [SRC-0799EEEB02-L000071](../../agents/tool_execution_status.py#L71) | 71 | `"    )"` | — |
| [SRC-0799EEEB02-L000072](../../agents/tool_execution_status.py#L72) | 72 | `"    reported_pages_read = _nonnegative_int(search_report.get(\"pages_fetched\"))"` | — |
| [SRC-0799EEEB02-L000073](../../agents/tool_execution_status.py#L73) | 73 | `"    pages_attempted = _nonnegative_int(search_report.get(\"pages_fetch_attempted\"))"` | — |
| [SRC-0799EEEB02-L000074](../../agents/tool_execution_status.py#L74) | 74 | `"    raw_source_rows = output.get(\"sources\")"` | — |
| [SRC-0799EEEB02-L000075](../../agents/tool_execution_status.py#L75) | 75 | `"    returned_sources_known = isinstance(raw_source_rows, list)"` | — |
| [SRC-0799EEEB02-L000076](../../agents/tool_execution_status.py#L76) | 76 | `"    source_rows = raw_source_rows if returned_sources_known else []"` | — |
| [SRC-0799EEEB02-L000077](../../agents/tool_execution_status.py#L77) | 77 | `"    readable_page_rows = sum("` | — |
| [SRC-0799EEEB02-L000078](../../agents/tool_execution_status.py#L78) | 78 | `"        1 for source in source_rows"` | — |
| [SRC-0799EEEB02-L000079](../../agents/tool_execution_status.py#L79) | 79 | `"        if isinstance(source, dict)"` | — |
| [SRC-0799EEEB02-L000080](../../agents/tool_execution_status.py#L80) | 80 | `"        and source.get(\"page_fetched\") is True"` | — |
| [SRC-0799EEEB02-L000081](../../agents/tool_execution_status.py#L81) | 81 | `"    )"` | — |
| [SRC-0799EEEB02-L000082](../../agents/tool_execution_status.py#L82) | 82 | `"    # The public return value is the final accepted source set. Prefer it when"` | — |
| [SRC-0799EEEB02-L000083](../../agents/tool_execution_status.py#L83) | 83 | `"    # present; preserve report counters separately so disagreements stay visible."` | — |
| [SRC-0799EEEB02-L000084](../../agents/tool_execution_status.py#L84) | 84 | `"    returned_source_count = len(source_rows) if returned_sources_known else None"` | — |
| [SRC-0799EEEB02-L000085](../../agents/tool_execution_status.py#L85) | 85 | `"    accepted_sources = ("` | — |
| [SRC-0799EEEB02-L000086](../../agents/tool_execution_status.py#L86) | 86 | `"        returned_source_count if returned_sources_known else reported_accepted_sources"` | — |
| [SRC-0799EEEB02-L000087](../../agents/tool_execution_status.py#L87) | 87 | `"    )"` | — |
| [SRC-0799EEEB02-L000088](../../agents/tool_execution_status.py#L88) | 88 | `"    pages_read = reported_pages_read if reported_pages_read is not None else readable_page_rows"` | — |
| [SRC-0799EEEB02-L000089](../../agents/tool_execution_status.py#L89) | 89 | `"    source_count_mismatch = ("` | — |
| [SRC-0799EEEB02-L000090](../../agents/tool_execution_status.py#L90) | 90 | `"        returned_sources_known"` | — |
| [SRC-0799EEEB02-L000091](../../agents/tool_execution_status.py#L91) | 91 | `"        and reported_accepted_sources is not None"` | — |
| [SRC-0799EEEB02-L000092](../../agents/tool_execution_status.py#L92) | 92 | `"        and reported_accepted_sources != returned_source_count"` | — |
| [SRC-0799EEEB02-L000093](../../agents/tool_execution_status.py#L93) | 93 | `"    )"` | — |
| [SRC-0799EEEB02-L000094](../../agents/tool_execution_status.py#L94) | 94 | `"    page_count_mismatch = ("` | — |
| [SRC-0799EEEB02-L000095](../../agents/tool_execution_status.py#L95) | 95 | `"        returned_sources_known"` | — |
| [SRC-0799EEEB02-L000096](../../agents/tool_execution_status.py#L96) | 96 | `"        and reported_pages_read is not None"` | — |
| [SRC-0799EEEB02-L000097](../../agents/tool_execution_status.py#L97) | 97 | `"        and reported_pages_read != readable_page_rows"` | — |
| [SRC-0799EEEB02-L000098](../../agents/tool_execution_status.py#L98) | 98 | `"    )"` | — |
| [SRC-0799EEEB02-L000099](../../agents/tool_execution_status.py#L99) | 99 | `""` | — |
| [SRC-0799EEEB02-L000100](../../agents/tool_execution_status.py#L100) | 100 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-0799EEEB02-L000101](../../agents/tool_execution_status.py#L101) | 101 | `""` | — |
| [SRC-0799EEEB02-L000102](../../agents/tool_execution_status.py#L102) | 102 | `"    # Search completion and evidence acceptance are distinct: zero accepted sources"` | — |
| [SRC-0799EEEB02-L000103](../../agents/tool_execution_status.py#L103) | 103 | `"    # means this retrieval attempt supplied no eligible evidence, not that the fact"` | — |
| [SRC-0799EEEB02-L000104](../../agents/tool_execution_status.py#L104) | 104 | `"    # or source does not exist."` | — |
| [SRC-0799EEEB02-L000105](../../agents/tool_execution_status.py#L105) | 105 | `"    tool = \"web_search\""` | — |
| [SRC-0799EEEB02-L000106](../../agents/tool_execution_status.py#L106) | 106 | `"    if tool not in required:"` | — |
| [SRC-0799EEEB02-L000107](../../agents/tool_execution_status.py#L107) | 107 | `"        status = \"not_required\""` | — |
| [SRC-0799EEEB02-L000108](../../agents/tool_execution_status.py#L108) | 108 | `"    elif outcome == \"attempted_research_error\":"` | — |
| [SRC-0799EEEB02-L000109](../../agents/tool_execution_status.py#L109) | 109 | `"        status = \"failed\""` | — |
| [SRC-0799EEEB02-L000110](../../agents/tool_execution_status.py#L110) | 110 | `"    elif outcome in {\"unknown_after_research_error\", \"unknown_after_budget_exhaustion\"}:"` | — |
| [SRC-0799EEEB02-L000111](../../agents/tool_execution_status.py#L111) | 111 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000112](../../agents/tool_execution_status.py#L112) | 112 | `"    elif outcome == \"not_attempted\" or attempted is False:"` | — |
| [SRC-0799EEEB02-L000113](../../agents/tool_execution_status.py#L113) | 113 | `"        status = \"not_attempted\""` | — |
| [SRC-0799EEEB02-L000114](../../agents/tool_execution_status.py#L114) | 114 | `"    elif source_count_mismatch:"` | — |
| [SRC-0799EEEB02-L000115](../../agents/tool_execution_status.py#L115) | 115 | `"        status = \"counter_mismatch\""` | — |
| [SRC-0799EEEB02-L000116](../../agents/tool_execution_status.py#L116) | 116 | `"    elif attempted is True:"` | — |
| [SRC-0799EEEB02-L000117](../../agents/tool_execution_status.py#L117) | 117 | `"        if accepted_sources is not None:"` | — |
| [SRC-0799EEEB02-L000118](../../agents/tool_execution_status.py#L118) | 118 | `"            status = \"completed_with_results\" if accepted_sources > 0 else \"completed_no_usable_results\""` | — |
| [SRC-0799EEEB02-L000119](../../agents/tool_execution_status.py#L119) | 119 | `"        elif outcome == \"attempted_with_usable_sources\":"` | — |
| [SRC-0799EEEB02-L000120](../../agents/tool_execution_status.py#L120) | 120 | `"            status = \"completed_with_results\""` | — |
| [SRC-0799EEEB02-L000121](../../agents/tool_execution_status.py#L121) | 121 | `"        elif outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-0799EEEB02-L000122](../../agents/tool_execution_status.py#L122) | 122 | `"            status = \"completed_no_usable_results\""` | — |
| [SRC-0799EEEB02-L000123](../../agents/tool_execution_status.py#L123) | 123 | `"        else:"` | — |
| [SRC-0799EEEB02-L000124](../../agents/tool_execution_status.py#L124) | 124 | `"            status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000125](../../agents/tool_execution_status.py#L125) | 125 | `"    else:"` | — |
| [SRC-0799EEEB02-L000126](../../agents/tool_execution_status.py#L126) | 126 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000127](../../agents/tool_execution_status.py#L127) | 127 | `"    rows.append(_status_row(tool, tool in required, status, {"` | — |
| [SRC-0799EEEB02-L000128](../../agents/tool_execution_status.py#L128) | 128 | `"        \"search_outcome\": outcome,"` | — |
| [SRC-0799EEEB02-L000129](../../agents/tool_execution_status.py#L129) | 129 | `"        \"search_attempted\": attempted if isinstance(attempted, bool) else None,"` | — |
| [SRC-0799EEEB02-L000130](../../agents/tool_execution_status.py#L130) | 130 | `"        \"accepted_source_count\": accepted_sources,"` | — |
| [SRC-0799EEEB02-L000131](../../agents/tool_execution_status.py#L131) | 131 | `"        \"reported_accepted_source_count\": reported_accepted_sources,"` | — |
| [SRC-0799EEEB02-L000132](../../agents/tool_execution_status.py#L132) | 132 | `"        \"counter_consistency\": ("` | — |
| [SRC-0799EEEB02-L000133](../../agents/tool_execution_status.py#L133) | 133 | `"            \"mismatch\" if source_count_mismatch else \"consistent\""` | — |
| [SRC-0799EEEB02-L000134](../../agents/tool_execution_status.py#L134) | 134 | `"            if returned_sources_known and reported_accepted_sources is not None"` | — |
| [SRC-0799EEEB02-L000135](../../agents/tool_execution_status.py#L135) | 135 | `"            else \"not_comparable\""` | — |
| [SRC-0799EEEB02-L000136](../../agents/tool_execution_status.py#L136) | 136 | `"        ),"` | — |
| [SRC-0799EEEB02-L000137](../../agents/tool_execution_status.py#L137) | 137 | `"    }))"` | — |
| [SRC-0799EEEB02-L000138](../../agents/tool_execution_status.py#L138) | 138 | `""` | — |
| [SRC-0799EEEB02-L000139](../../agents/tool_execution_status.py#L139) | 139 | `"    tool = \"page_fetch\""` | — |
| [SRC-0799EEEB02-L000140](../../agents/tool_execution_status.py#L140) | 140 | `"    if tool not in required:"` | — |
| [SRC-0799EEEB02-L000141](../../agents/tool_execution_status.py#L141) | 141 | `"        status = \"not_required\""` | — |
| [SRC-0799EEEB02-L000142](../../agents/tool_execution_status.py#L142) | 142 | `"    elif page_count_mismatch:"` | — |
| [SRC-0799EEEB02-L000143](../../agents/tool_execution_status.py#L143) | 143 | `"        status = \"counter_mismatch\""` | — |
| [SRC-0799EEEB02-L000144](../../agents/tool_execution_status.py#L144) | 144 | `"    elif pages_read > 0:"` | — |
| [SRC-0799EEEB02-L000145](../../agents/tool_execution_status.py#L145) | 145 | `"        status = \"completed_with_read_pages\""` | — |
| [SRC-0799EEEB02-L000146](../../agents/tool_execution_status.py#L146) | 146 | `"    elif pages_attempted is not None and pages_attempted > 0:"` | — |
| [SRC-0799EEEB02-L000147](../../agents/tool_execution_status.py#L147) | 147 | `"        status = \"attempted_no_readable_pages\""` | — |
| [SRC-0799EEEB02-L000148](../../agents/tool_execution_status.py#L148) | 148 | `"    elif pages_attempted is None:"` | — |
| [SRC-0799EEEB02-L000149](../../agents/tool_execution_status.py#L149) | 149 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000150](../../agents/tool_execution_status.py#L150) | 150 | `"    elif outcome in _ERROR_OUTCOMES:"` | — |
| [SRC-0799EEEB02-L000151](../../agents/tool_execution_status.py#L151) | 151 | `"        status = \"not_attempted_after_search_error\""` | — |
| [SRC-0799EEEB02-L000152](../../agents/tool_execution_status.py#L152) | 152 | `"    elif attempted is True:"` | — |
| [SRC-0799EEEB02-L000153](../../agents/tool_execution_status.py#L153) | 153 | `"        status = \"not_attempted_no_fetchable_candidates\""` | — |
| [SRC-0799EEEB02-L000154](../../agents/tool_execution_status.py#L154) | 154 | `"    elif attempted is False:"` | — |
| [SRC-0799EEEB02-L000155](../../agents/tool_execution_status.py#L155) | 155 | `"        status = \"not_attempted\""` | — |
| [SRC-0799EEEB02-L000156](../../agents/tool_execution_status.py#L156) | 156 | `"    else:"` | — |
| [SRC-0799EEEB02-L000157](../../agents/tool_execution_status.py#L157) | 157 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000158](../../agents/tool_execution_status.py#L158) | 158 | `"    rows.append(_status_row(tool, tool in required, status, {"` | — |
| [SRC-0799EEEB02-L000159](../../agents/tool_execution_status.py#L159) | 159 | `"        \"pages_fetch_attempted\": pages_attempted,"` | — |
| [SRC-0799EEEB02-L000160](../../agents/tool_execution_status.py#L160) | 160 | `"        \"pages_read\": pages_read,"` | — |
| [SRC-0799EEEB02-L000161](../../agents/tool_execution_status.py#L161) | 161 | `"        \"reported_pages_fetched\": reported_pages_read,"` | — |
| [SRC-0799EEEB02-L000162](../../agents/tool_execution_status.py#L162) | 162 | `"        \"pages_read_from_returned_sources\": readable_page_rows,"` | — |
| [SRC-0799EEEB02-L000163](../../agents/tool_execution_status.py#L163) | 163 | `"        \"counter_consistency\": ("` | — |
| [SRC-0799EEEB02-L000164](../../agents/tool_execution_status.py#L164) | 164 | `"            \"mismatch\" if page_count_mismatch else \"consistent\""` | — |
| [SRC-0799EEEB02-L000165](../../agents/tool_execution_status.py#L165) | 165 | `"            if returned_sources_known and reported_pages_read is not None"` | — |
| [SRC-0799EEEB02-L000166](../../agents/tool_execution_status.py#L166) | 166 | `"            else \"not_comparable\""` | — |
| [SRC-0799EEEB02-L000167](../../agents/tool_execution_status.py#L167) | 167 | `"        ),"` | — |
| [SRC-0799EEEB02-L000168](../../agents/tool_execution_status.py#L168) | 168 | `"    }))"` | — |
| [SRC-0799EEEB02-L000169](../../agents/tool_execution_status.py#L169) | 169 | `""` | — |
| [SRC-0799EEEB02-L000170](../../agents/tool_execution_status.py#L170) | 170 | `"    tool = \"public_social_search_if_configured\""` | — |
| [SRC-0799EEEB02-L000171](../../agents/tool_execution_status.py#L171) | 171 | `"    raw_social_results = _nonnegative_int(search_report.get(\"social_direct_results\"))"` | — |
| [SRC-0799EEEB02-L000172](../../agents/tool_execution_status.py#L172) | 172 | `"    social_results = raw_social_results or 0"` | — |
| [SRC-0799EEEB02-L000173](../../agents/tool_execution_status.py#L173) | 173 | `"    social_sources = sum("` | — |
| [SRC-0799EEEB02-L000174](../../agents/tool_execution_status.py#L174) | 174 | `"        1 for source in source_rows"` | — |
| [SRC-0799EEEB02-L000175](../../agents/tool_execution_status.py#L175) | 175 | `"        if isinstance(source, dict)"` | — |
| [SRC-0799EEEB02-L000176](../../agents/tool_execution_status.py#L176) | 176 | `"        and ("` | — |
| [SRC-0799EEEB02-L000177](../../agents/tool_execution_status.py#L177) | 177 | `"            str(source.get(\"platform\") or \"\").lower() in _SOCIAL_PLATFORMS"` | — |
| [SRC-0799EEEB02-L000178](../../agents/tool_execution_status.py#L178) | 178 | `"            or str(source.get(\"source_class\") or \"\").lower() == \"social\""` | — |
| [SRC-0799EEEB02-L000179](../../agents/tool_execution_status.py#L179) | 179 | `"        )"` | — |
| [SRC-0799EEEB02-L000180](../../agents/tool_execution_status.py#L180) | 180 | `"    )"` | — |
| [SRC-0799EEEB02-L000181](../../agents/tool_execution_status.py#L181) | 181 | `"    connector_summary = search_report.get(\"connector_summary\")"` | — |
| [SRC-0799EEEB02-L000182](../../agents/tool_execution_status.py#L182) | 182 | `"    connector_summary = connector_summary if isinstance(connector_summary, dict) else {}"` | — |
| [SRC-0799EEEB02-L000183](../../agents/tool_execution_status.py#L183) | 183 | `"    connector_rows = connector_summary.get(\"connectors\")"` | — |
| [SRC-0799EEEB02-L000184](../../agents/tool_execution_status.py#L184) | 184 | `"    connector_rows = connector_rows if isinstance(connector_rows, list) else []"` | — |
| [SRC-0799EEEB02-L000185](../../agents/tool_execution_status.py#L185) | 185 | `"    social_connector_names = {"` | — |
| [SRC-0799EEEB02-L000186](../../agents/tool_execution_status.py#L186) | 186 | `"        \"reddit_public_rss\", \"bluesky_public_search\", \"reddit_oauth_api\","` | — |
| [SRC-0799EEEB02-L000187](../../agents/tool_execution_status.py#L187) | 187 | `"        \"facebook_pages_api\", \"instagram_graph_api\", \"x_official_api\","` | — |
| [SRC-0799EEEB02-L000188](../../agents/tool_execution_status.py#L188) | 188 | `"        \"youtube_data_api\","` | — |
| [SRC-0799EEEB02-L000189](../../agents/tool_execution_status.py#L189) | 189 | `"    }"` | — |
| [SRC-0799EEEB02-L000190](../../agents/tool_execution_status.py#L190) | 190 | `"    social_connector_states = ["` | — |
| [SRC-0799EEEB02-L000191](../../agents/tool_execution_status.py#L191) | 191 | `"        row for row in connector_rows"` | — |
| [SRC-0799EEEB02-L000192](../../agents/tool_execution_status.py#L192) | 192 | `"        if isinstance(row, dict) and row.get(\"name\") in social_connector_names"` | — |
| [SRC-0799EEEB02-L000193](../../agents/tool_execution_status.py#L193) | 193 | `"    ]"` | — |
| [SRC-0799EEEB02-L000194](../../agents/tool_execution_status.py#L194) | 194 | `"    attempted_social_connectors = ["` | — |
| [SRC-0799EEEB02-L000195](../../agents/tool_execution_status.py#L195) | 195 | `"        row for row in social_connector_states if row.get(\"attempted\") is True"` | — |
| [SRC-0799EEEB02-L000196](../../agents/tool_execution_status.py#L196) | 196 | `"    ]"` | — |
| [SRC-0799EEEB02-L000197](../../agents/tool_execution_status.py#L197) | 197 | `"    social_connector_errors = ["` | — |
| [SRC-0799EEEB02-L000198](../../agents/tool_execution_status.py#L198) | 198 | `"        row for row in social_connector_states"` | — |
| [SRC-0799EEEB02-L000199](../../agents/tool_execution_status.py#L199) | 199 | `"        if row.get(\"status\") in {"` | — |
