# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **037**
- سجلات الأسطر: **800**
- النطاق: SRC-AFEDC2645A-L000027 إلى SRC-F725E90B2A-L000677
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-AFEDC2645A — [tests/test_task_understanding.py](../../tests/test_task_understanding.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-AFEDC2645A-L000027](../../tests/test_task_understanding.py#L27) | 27 | `"    assert spec[\"decision_checks\"]"` | — |
| [SRC-AFEDC2645A-L000028](../../tests/test_task_understanding.py#L28) | 28 | `""` | — |
| [SRC-AFEDC2645A-L000029](../../tests/test_task_understanding.py#L29) | 29 | `""` | — |
| [SRC-AFEDC2645A-L000030](../../tests/test_task_understanding.py#L30) | 30 | `"def test_task_spec_preserves_only_explicit_constraints():"` | — |
| [SRC-AFEDC2645A-L000031](../../tests/test_task_understanding.py#L31) | 31 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000032](../../tests/test_task_understanding.py#L32) | 32 | `"        \"قارن نيسان صني 2022 مع BYD Dolphin في مصر، بميزانية أقل من 400 ألف جنيه\","` | — |
| [SRC-AFEDC2645A-L000033](../../tests/test_task_understanding.py#L33) | 33 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000034](../../tests/test_task_understanding.py#L34) | 34 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000035](../../tests/test_task_understanding.py#L35) | 35 | `"    )"` | — |
| [SRC-AFEDC2645A-L000036](../../tests/test_task_understanding.py#L36) | 36 | `"    constraints = spec[\"constraints\"]"` | — |
| [SRC-AFEDC2645A-L000037](../../tests/test_task_understanding.py#L37) | 37 | `"    assert \"2022\" in constraints[\"explicit_years\"]"` | — |
| [SRC-AFEDC2645A-L000038](../../tests/test_task_understanding.py#L38) | 38 | `"    assert \"مصر\" in constraints[\"explicit_locations\"]"` | — |
| [SRC-AFEDC2645A-L000039](../../tests/test_task_understanding.py#L39) | 39 | `"    assert constraints[\"explicit_budgets\"]"` | — |
| [SRC-AFEDC2645A-L000040](../../tests/test_task_understanding.py#L40) | 40 | `"    assert constraints[\"language_profile\"] in {\"ar\", \"mixed\"}"` | — |
| [SRC-AFEDC2645A-L000041](../../tests/test_task_understanding.py#L41) | 41 | `""` | — |
| [SRC-AFEDC2645A-L000042](../../tests/test_task_understanding.py#L42) | 42 | `""` | — |
| [SRC-AFEDC2645A-L000043](../../tests/test_task_understanding.py#L43) | 43 | `"def test_latest_mode_requires_current_evidence_for_stateful_facts():"` | — |
| [SRC-AFEDC2645A-L000044](../../tests/test_task_understanding.py#L44) | 44 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000045](../../tests/test_task_understanding.py#L45) | 45 | `"        \"مواعيد عمل مكتب الجوازات اليوم\","` | — |
| [SRC-AFEDC2645A-L000046](../../tests/test_task_understanding.py#L46) | 46 | `"        mode=\"latest\","` | — |
| [SRC-AFEDC2645A-L000047](../../tests/test_task_understanding.py#L47) | 47 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000048](../../tests/test_task_understanding.py#L48) | 48 | `"    )"` | — |
| [SRC-AFEDC2645A-L000049](../../tests/test_task_understanding.py#L49) | 49 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is True"` | — |
| [SRC-AFEDC2645A-L000050](../../tests/test_task_understanding.py#L50) | 50 | `"    assert \"page_text_successfully_read\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000051](../../tests/test_task_understanding.py#L51) | 51 | `"    assert \"date_check\" in spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000052](../../tests/test_task_understanding.py#L52) | 52 | `""` | — |
| [SRC-AFEDC2645A-L000053](../../tests/test_task_understanding.py#L53) | 53 | `""` | — |
| [SRC-AFEDC2645A-L000054](../../tests/test_task_understanding.py#L54) | 54 | `"def test_official_site_navigation_is_not_misclassified_as_current_news():"` | — |
| [SRC-AFEDC2645A-L000055](../../tests/test_task_understanding.py#L55) | 55 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000056](../../tests/test_task_understanding.py#L56) | 56 | `"        \"ابحث عن الموقع الرسمي لوزارة الاتصالات في مصر\","` | — |
| [SRC-AFEDC2645A-L000057](../../tests/test_task_understanding.py#L57) | 57 | `"        mode=\"latest\","` | — |
| [SRC-AFEDC2645A-L000058](../../tests/test_task_understanding.py#L58) | 58 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000059](../../tests/test_task_understanding.py#L59) | 59 | `"    )"` | — |
| [SRC-AFEDC2645A-L000060](../../tests/test_task_understanding.py#L60) | 60 | `"    assert spec[\"task_family\"] == \"official_site_lookup\""` | — |
| [SRC-AFEDC2645A-L000061](../../tests/test_task_understanding.py#L61) | 61 | `"    assert spec[\"constraints\"][\"official_site_required\"] is True"` | — |
| [SRC-AFEDC2645A-L000062](../../tests/test_task_understanding.py#L62) | 62 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is False"` | — |
| [SRC-AFEDC2645A-L000063](../../tests/test_task_understanding.py#L63) | 63 | `""` | — |
| [SRC-AFEDC2645A-L000064](../../tests/test_task_understanding.py#L64) | 64 | `""` | — |
| [SRC-AFEDC2645A-L000065](../../tests/test_task_understanding.py#L65) | 65 | `"def test_social_request_separates_experience_from_truth_verification():"` | — |
| [SRC-AFEDC2645A-L000066](../../tests/test_task_understanding.py#L66) | 66 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000067](../../tests/test_task_understanding.py#L67) | 67 | `"        \"أريد آراء وتجارب ملاك نيسان صني 2022 في مصر\","` | — |
| [SRC-AFEDC2645A-L000068](../../tests/test_task_understanding.py#L68) | 68 | `"        mode=\"social\","` | — |
| [SRC-AFEDC2645A-L000069](../../tests/test_task_understanding.py#L69) | 69 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000070](../../tests/test_task_understanding.py#L70) | 70 | `"    )"` | — |
| [SRC-AFEDC2645A-L000071](../../tests/test_task_understanding.py#L71) | 71 | `"    assert spec[\"constraints\"][\"social_evidence_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000072](../../tests/test_task_understanding.py#L72) | 72 | `"    assert \"heuristic_classification_is_not_identity_or_truth_verification\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000073](../../tests/test_task_understanding.py#L73) | 73 | `"    assert \"personal_experience\" in spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000074](../../tests/test_task_understanding.py#L74) | 74 | `""` | — |
| [SRC-AFEDC2645A-L000075](../../tests/test_task_understanding.py#L75) | 75 | `""` | — |
| [SRC-AFEDC2645A-L000076](../../tests/test_task_understanding.py#L76) | 76 | `"def test_ambiguous_followup_is_not_reported_as_a_confident_interpretation():"` | — |
| [SRC-AFEDC2645A-L000077](../../tests/test_task_understanding.py#L77) | 77 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000078](../../tests/test_task_understanding.py#L78) | 78 | `"        \"كام سعرها؟\","` | — |
| [SRC-AFEDC2645A-L000079](../../tests/test_task_understanding.py#L79) | 79 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000080](../../tests/test_task_understanding.py#L80) | 80 | `"        intent_route=\"CLARIFY\","` | — |
| [SRC-AFEDC2645A-L000081](../../tests/test_task_understanding.py#L81) | 81 | `"        dialogue_context={\"needs_clarification\": True},"` | — |
| [SRC-AFEDC2645A-L000082](../../tests/test_task_understanding.py#L82) | 82 | `"    )"` | — |
| [SRC-AFEDC2645A-L000083](../../tests/test_task_understanding.py#L83) | 83 | `"    assert spec[\"task_family\"] == \"ambiguous_or_incomplete\""` | — |
| [SRC-AFEDC2645A-L000084](../../tests/test_task_understanding.py#L84) | 84 | `"    assert spec[\"ambiguity_status\"] == \"needs_clarification\""` | — |
| [SRC-AFEDC2645A-L000085](../../tests/test_task_understanding.py#L85) | 85 | `""` | — |
| [SRC-AFEDC2645A-L000086](../../tests/test_task_understanding.py#L86) | 86 | `""` | — |
| [SRC-AFEDC2645A-L000087](../../tests/test_task_understanding.py#L87) | 87 | `"def test_query_strategy_matrix_is_bounded_deduplicated_and_topic_anchored():"` | — |
| [SRC-AFEDC2645A-L000088](../../tests/test_task_understanding.py#L88) | 88 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000089](../../tests/test_task_understanding.py#L89) | 89 | `"        \"قارن السيارات الكهربائية في مصر من حيث السعر والضمان\","` | — |
| [SRC-AFEDC2645A-L000090](../../tests/test_task_understanding.py#L90) | 90 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000091](../../tests/test_task_understanding.py#L91) | 91 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000092](../../tests/test_task_understanding.py#L92) | 92 | `"    )"` | — |
| [SRC-AFEDC2645A-L000093](../../tests/test_task_understanding.py#L93) | 93 | `"    rows = build_query_strategy_matrix("` | — |
| [SRC-AFEDC2645A-L000094](../../tests/test_task_understanding.py#L94) | 94 | `"        \"قارن السيارات الكهربائية في مصر من حيث السعر والضمان\","` | — |
| [SRC-AFEDC2645A-L000095](../../tests/test_task_understanding.py#L95) | 95 | `"        spec,"` | — |
| [SRC-AFEDC2645A-L000096](../../tests/test_task_understanding.py#L96) | 96 | `"        [\"السيارات الكهربائية في مصر\", \"السيارات الكهربائية في مصر\"],"` | — |
| [SRC-AFEDC2645A-L000097](../../tests/test_task_understanding.py#L97) | 97 | `"        limit=6,"` | — |
| [SRC-AFEDC2645A-L000098](../../tests/test_task_understanding.py#L98) | 98 | `"    )"` | — |
| [SRC-AFEDC2645A-L000099](../../tests/test_task_understanding.py#L99) | 99 | `"    queries = [row[\"query\"] for row in rows]"` | — |
| [SRC-AFEDC2645A-L000100](../../tests/test_task_understanding.py#L100) | 100 | `"    assert 1 <= len(queries) <= 6"` | — |
| [SRC-AFEDC2645A-L000101](../../tests/test_task_understanding.py#L101) | 101 | `"    assert len({query.casefold() for query in queries}) == len(queries)"` | — |
| [SRC-AFEDC2645A-L000102](../../tests/test_task_understanding.py#L102) | 102 | `"    assert all(\"السيارات\" in query for query in queries)"` | — |
| [SRC-AFEDC2645A-L000103](../../tests/test_task_understanding.py#L103) | 103 | `"    assert any(row[\"strategy\"] == \"primary_specification\" for row in rows)"` | — |
| [SRC-AFEDC2645A-L000104](../../tests/test_task_understanding.py#L104) | 104 | `"    assert all(row[\"rationale\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000105](../../tests/test_task_understanding.py#L105) | 105 | `""` | — |
| [SRC-AFEDC2645A-L000106](../../tests/test_task_understanding.py#L106) | 106 | `""` | — |
| [SRC-AFEDC2645A-L000107](../../tests/test_task_understanding.py#L107) | 107 | `"def test_strategy_matrix_does_not_create_generic_queries_without_topic():"` | — |
| [SRC-AFEDC2645A-L000108](../../tests/test_task_understanding.py#L108) | 108 | `"    spec = build_task_spec(\"قارنهم\", mode=\"deep\", intent_route=\"CLARIFY\")"` | — |
| [SRC-AFEDC2645A-L000109](../../tests/test_task_understanding.py#L109) | 109 | `"    rows = build_query_strategy_matrix(\"قارنهم\", spec, [], limit=8)"` | — |
| [SRC-AFEDC2645A-L000110](../../tests/test_task_understanding.py#L110) | 110 | `"    assert rows == []"` | — |
| [SRC-AFEDC2645A-L000111](../../tests/test_task_understanding.py#L111) | 111 | `""` | — |
| [SRC-AFEDC2645A-L000112](../../tests/test_task_understanding.py#L112) | 112 | `""` | — |
| [SRC-AFEDC2645A-L000113](../../tests/test_task_understanding.py#L113) | 113 | `"def test_mixed_language_is_supported_and_urls_are_explicit_constraints():"` | — |
| [SRC-AFEDC2645A-L000114](../../tests/test_task_understanding.py#L114) | 114 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000115](../../tests/test_task_understanding.py#L115) | 115 | `"        \"Compare Nissan Sunny 2022 with BYD Dolphin في مصر https://example.com/specs\","` | — |
| [SRC-AFEDC2645A-L000116](../../tests/test_task_understanding.py#L116) | 116 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000117](../../tests/test_task_understanding.py#L117) | 117 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000118](../../tests/test_task_understanding.py#L118) | 118 | `"    )"` | — |
| [SRC-AFEDC2645A-L000119](../../tests/test_task_understanding.py#L119) | 119 | `"    assert spec[\"constraints\"][\"language_profile\"] == \"mixed\""` | — |
| [SRC-AFEDC2645A-L000120](../../tests/test_task_understanding.py#L120) | 120 | `"    assert spec[\"constraints\"][\"explicit_urls\"] == [\"https://example.com/specs\"]"` | — |
| [SRC-AFEDC2645A-L000121](../../tests/test_task_understanding.py#L121) | 121 | `"    assert \"2022\" in spec[\"constraints\"][\"explicit_years\"]"` | — |
| [SRC-AFEDC2645A-L000122](../../tests/test_task_understanding.py#L122) | 122 | `""` | — |
| [SRC-AFEDC2645A-L000123](../../tests/test_task_understanding.py#L123) | 123 | `""` | — |
| [SRC-AFEDC2645A-L000124](../../tests/test_task_understanding.py#L124) | 124 | `"def test_task_spec_validator_does_not_accept_untrusted_arbitrary_objects():"` | — |
| [SRC-AFEDC2645A-L000125](../../tests/test_task_understanding.py#L125) | 125 | `"    from agents.task_understanding import validate_task_spec"` | — |
| [SRC-AFEDC2645A-L000126](../../tests/test_task_understanding.py#L126) | 126 | `""` | — |
| [SRC-AFEDC2645A-L000127](../../tests/test_task_understanding.py#L127) | 127 | `"    invalid = validate_task_spec({\"schema\": \"wrong\", \"tool_requirements\": [\"delete files\"]})"` | — |
| [SRC-AFEDC2645A-L000128](../../tests/test_task_understanding.py#L128) | 128 | `"    assert invalid[\"status\"] == \"not_available\""` | — |
| [SRC-AFEDC2645A-L000129](../../tests/test_task_understanding.py#L129) | 129 | `""` | — |
| [SRC-AFEDC2645A-L000130](../../tests/test_task_understanding.py#L130) | 130 | `""` | — |
| [SRC-AFEDC2645A-L000131](../../tests/test_task_understanding.py#L131) | 131 | `"def test_compound_task_keeps_current_social_and_comparison_requirements_together():"` | — |
| [SRC-AFEDC2645A-L000132](../../tests/test_task_understanding.py#L132) | 132 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000133](../../tests/test_task_understanding.py#L133) | 133 | `"        \"قارن تجارب ملاك نيسان صني 2022 في مصر اليوم من حيث السعر والأعطال\","` | — |
| [SRC-AFEDC2645A-L000134](../../tests/test_task_understanding.py#L134) | 134 | `"        mode=\"social\","` | — |
| [SRC-AFEDC2645A-L000135](../../tests/test_task_understanding.py#L135) | 135 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000136](../../tests/test_task_understanding.py#L136) | 136 | `"    )"` | — |
| [SRC-AFEDC2645A-L000137](../../tests/test_task_understanding.py#L137) | 137 | `"    assert spec[\"task_family\"] in {\"social_opinions\", \"compare\"}"` | — |
| [SRC-AFEDC2645A-L000138](../../tests/test_task_understanding.py#L138) | 138 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is True"` | — |
| [SRC-AFEDC2645A-L000139](../../tests/test_task_understanding.py#L139) | 139 | `"    assert spec[\"constraints\"][\"social_evidence_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000140](../../tests/test_task_understanding.py#L140) | 140 | `"    assert \"publication_or_update_date\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000141](../../tests/test_task_understanding.py#L141) | 141 | `"    assert \"preserve_explicit_comparison_criteria\" in spec[\"evidence_requirements\"] or \"preserve_each_explicit_comparison_criterion\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000142](../../tests/test_task_understanding.py#L142) | 142 | `"    assert \"personal_experience\" in spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000143](../../tests/test_task_understanding.py#L143) | 143 | `"    assert \"date_check\" in spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000144](../../tests/test_task_understanding.py#L144) | 144 | `""` | — |
| [SRC-AFEDC2645A-L000145](../../tests/test_task_understanding.py#L145) | 145 | `""` | — |
| [SRC-AFEDC2645A-L000146](../../tests/test_task_understanding.py#L146) | 146 | `"def test_alarm_word_does_not_trigger_current_information_pattern():"` | — |
| [SRC-AFEDC2645A-L000147](../../tests/test_task_understanding.py#L147) | 147 | `"    spec = build_task_spec(\"ما معنى نظام الإنذار المعنون؟\", mode=\"auto\", intent_route=\"MODEL_ONLY\")"` | — |
| [SRC-AFEDC2645A-L000148](../../tests/test_task_understanding.py#L148) | 148 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is False"` | — |
| [SRC-AFEDC2645A-L000149](../../tests/test_task_understanding.py#L149) | 149 | `"    assert spec[\"task_family\"] == \"explain_or_define\""` | — |
## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L000001](../../tests/test_web_agent.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-F725E90B2A-L000002](../../tests/test_web_agent.py#L2) | 2 | `""` | — |
| [SRC-F725E90B2A-L000003](../../tests/test_web_agent.py#L3) | 3 | `"from pathlib import Path"` | — |
| [SRC-F725E90B2A-L000004](../../tests/test_web_agent.py#L4) | 4 | `""` | — |
| [SRC-F725E90B2A-L000005](../../tests/test_web_agent.py#L5) | 5 | `"import pytest"` | — |
| [SRC-F725E90B2A-L000006](../../tests/test_web_agent.py#L6) | 6 | `""` | — |
| [SRC-F725E90B2A-L000007](../../tests/test_web_agent.py#L7) | 7 | `"from agents.research import compact_search_query"` | — |
| [SRC-F725E90B2A-L000008](../../tests/test_web_agent.py#L8) | 8 | `"from agents.request_budget import RequestBudgetExceeded"` | — |
| [SRC-F725E90B2A-L000009](../../tests/test_web_agent.py#L9) | 9 | `"from agents.web_agent import ("` | — |
| [SRC-F725E90B2A-L000010](../../tests/test_web_agent.py#L10) | 10 | `"    WebAgent,"` | — |
| [SRC-F725E90B2A-L000011](../../tests/test_web_agent.py#L11) | 11 | `"    _normalize_search_query,"` | — |
| [SRC-F725E90B2A-L000012](../../tests/test_web_agent.py#L12) | 12 | `"    _public_http_url,"` | — |
| [SRC-F725E90B2A-L000013](../../tests/test_web_agent.py#L13) | 13 | `"    _relevance_query_tokens,"` | — |
| [SRC-F725E90B2A-L000014](../../tests/test_web_agent.py#L14) | 14 | `"    _relevance_ratio,"` | — |
| [SRC-F725E90B2A-L000015](../../tests/test_web_agent.py#L15) | 15 | `")"` | — |
| [SRC-F725E90B2A-L000016](../../tests/test_web_agent.py#L16) | 16 | `""` | — |
| [SRC-F725E90B2A-L000017](../../tests/test_web_agent.py#L17) | 17 | `""` | — |
| [SRC-F725E90B2A-L000018](../../tests/test_web_agent.py#L18) | 18 | `"def sample_source(index=0):"` | — |
| [SRC-F725E90B2A-L000019](../../tests/test_web_agent.py#L19) | 19 | `"    domain = \"example.com\" if index == 0 else \"example.net\""` | — |
| [SRC-F725E90B2A-L000020](../../tests/test_web_agent.py#L20) | 20 | `"    return {"` | — |
| [SRC-F725E90B2A-L000021](../../tests/test_web_agent.py#L21) | 21 | `"        \"title\": \"مقالة عن التقنية\","` | — |
| [SRC-F725E90B2A-L000022](../../tests/test_web_agent.py#L22) | 22 | `"        \"url\": f\"https://{domain}/research\","` | — |
| [SRC-F725E90B2A-L000023](../../tests/test_web_agent.py#L23) | 23 | `"        \"snippet\": \"يشرح هذا المصدر التقنية وسبب المقارنة.\","` | — |
| [SRC-F725E90B2A-L000024](../../tests/test_web_agent.py#L24) | 24 | `"        \"page_text\": \"نص مستخرج من الصفحة يشرح التقنية وأسباب المقارنة.\","` | — |
| [SRC-F725E90B2A-L000025](../../tests/test_web_agent.py#L25) | 25 | `"        \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L000026](../../tests/test_web_agent.py#L26) | 26 | `"        \"providers\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L000027](../../tests/test_web_agent.py#L27) | 27 | `"        \"queries\": [\"قارن هذه التقنية\"],"` | — |
| [SRC-F725E90B2A-L000028](../../tests/test_web_agent.py#L28) | 28 | `"        \"domain\": domain,"` | — |
| [SRC-F725E90B2A-L000029](../../tests/test_web_agent.py#L29) | 29 | `"        \"source_class\": \"general\","` | — |
| [SRC-F725E90B2A-L000030](../../tests/test_web_agent.py#L30) | 30 | `"        \"platform\": \"web\","` | — |
| [SRC-F725E90B2A-L000031](../../tests/test_web_agent.py#L31) | 31 | `"    }"` | — |
| [SRC-F725E90B2A-L000032](../../tests/test_web_agent.py#L32) | 32 | `""` | — |
| [SRC-F725E90B2A-L000033](../../tests/test_web_agent.py#L33) | 33 | `""` | — |
| [SRC-F725E90B2A-L000034](../../tests/test_web_agent.py#L34) | 34 | `"def test_agent_synthesizes_with_sources_without_live_network(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000035](../../tests/test_web_agent.py#L35) | 35 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000036](../../tests/test_web_agent.py#L36) | 36 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000037](../../tests/test_web_agent.py#L37) | 37 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L000038](../../tests/test_web_agent.py#L38) | 38 | `""` | — |
| [SRC-F725E90B2A-L000039](../../tests/test_web_agent.py#L39) | 39 | `"    def plan(question, history):"` | — |
| [SRC-F725E90B2A-L000040](../../tests/test_web_agent.py#L40) | 40 | `"        return {"` | — |
| [SRC-F725E90B2A-L000041](../../tests/test_web_agent.py#L41) | 41 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L000042](../../tests/test_web_agent.py#L42) | 42 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L000043](../../tests/test_web_agent.py#L43) | 43 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L000044](../../tests/test_web_agent.py#L44) | 44 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000045](../../tests/test_web_agent.py#L45) | 45 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L000046](../../tests/test_web_agent.py#L46) | 46 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000047](../../tests/test_web_agent.py#L47) | 47 | `"        }"` | — |
| [SRC-F725E90B2A-L000048](../../tests/test_web_agent.py#L48) | 48 | `""` | — |
| [SRC-F725E90B2A-L000049](../../tests/test_web_agent.py#L49) | 49 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L000050](../../tests/test_web_agent.py#L50) | 50 | `"        seen[\"plan\"] = research_plan"` | — |
| [SRC-F725E90B2A-L000051](../../tests/test_web_agent.py#L51) | 51 | `"        return [sample_source(0), sample_source(1)], [], {"` | — |
| [SRC-F725E90B2A-L000052](../../tests/test_web_agent.py#L52) | 52 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L000053](../../tests/test_web_agent.py#L53) | 53 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L000054](../../tests/test_web_agent.py#L54) | 54 | `"            \"query_results\": [{\"query\": research_plan[\"queries\"][0], \"results\": 1}],"` | — |
| [SRC-F725E90B2A-L000055](../../tests/test_web_agent.py#L55) | 55 | `"            \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L000056](../../tests/test_web_agent.py#L56) | 56 | `"            \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L000057](../../tests/test_web_agent.py#L57) | 57 | `"            \"providers_used\": [\"test\"],"` | — |
| [SRC-F725E90B2A-L000058](../../tests/test_web_agent.py#L58) | 58 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L000059](../../tests/test_web_agent.py#L59) | 59 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L000060](../../tests/test_web_agent.py#L60) | 60 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000061](../../tests/test_web_agent.py#L61) | 61 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000062](../../tests/test_web_agent.py#L62) | 62 | `"        }"` | — |
| [SRC-F725E90B2A-L000063](../../tests/test_web_agent.py#L63) | 63 | `""` | — |
| [SRC-F725E90B2A-L000064](../../tests/test_web_agent.py#L64) | 64 | `"    def generate(question, history, sources, search_warning, research_plan=None, search_report=None):"` | — |
| [SRC-F725E90B2A-L000065](../../tests/test_web_agent.py#L65) | 65 | `"        seen[\"question\"] = question"` | — |
| [SRC-F725E90B2A-L000066](../../tests/test_web_agent.py#L66) | 66 | `"        seen[\"history\"] = history"` | — |
| [SRC-F725E90B2A-L000067](../../tests/test_web_agent.py#L67) | 67 | `"        seen[\"sources\"] = sources"` | — |
| [SRC-F725E90B2A-L000068](../../tests/test_web_agent.py#L68) | 68 | `"        seen[\"report\"] = search_report"` | — |
| [SRC-F725E90B2A-L000069](../../tests/test_web_agent.py#L69) | 69 | `"        return \"الإجابة: التقنية مناسبة للأسباب التالية [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L000070](../../tests/test_web_agent.py#L70) | 70 | `""` | — |
| [SRC-F725E90B2A-L000071](../../tests/test_web_agent.py#L71) | 71 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-F725E90B2A-L000072](../../tests/test_web_agent.py#L72) | 72 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L000073](../../tests/test_web_agent.py#L73) | 73 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L000074](../../tests/test_web_agent.py#L74) | 74 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-F725E90B2A-L000075](../../tests/test_web_agent.py#L75) | 75 | `"    result = agent.answer("` | — |
| [SRC-F725E90B2A-L000076](../../tests/test_web_agent.py#L76) | 76 | `"        \"قارن هذه التقنية\","` | — |
| [SRC-F725E90B2A-L000077](../../tests/test_web_agent.py#L77) | 77 | `"        history=[{\"role\": \"user\", \"content\": \"ما هي التقنية؟\"}],"` | — |
| [SRC-F725E90B2A-L000078](../../tests/test_web_agent.py#L78) | 78 | `"    )"` | — |
| [SRC-F725E90B2A-L000079](../../tests/test_web_agent.py#L79) | 79 | `""` | — |
| [SRC-F725E90B2A-L000080](../../tests/test_web_agent.py#L80) | 80 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-F725E90B2A-L000081](../../tests/test_web_agent.py#L81) | 81 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L000082](../../tests/test_web_agent.py#L82) | 82 | `"    assert result[\"search_report\"][\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L000083](../../tests/test_web_agent.py#L83) | 83 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_with_usable_sources\""` | — |
| [SRC-F725E90B2A-L000084](../../tests/test_web_agent.py#L84) | 84 | `"    assert result[\"search_report\"][\"pipeline_completion_status\"] == \"completed\""` | — |
| [SRC-F725E90B2A-L000085](../../tests/test_web_agent.py#L85) | 85 | `"    assert result[\"search_report\"][\"completion_stages\"][\"semantic_fact_check\"] == \"not_performed\""` | — |
| [SRC-F725E90B2A-L000086](../../tests/test_web_agent.py#L86) | 86 | `"    assert result[\"search_report\"][\"research_quality_semantics\"] == ("` | — |
| [SRC-F725E90B2A-L000087](../../tests/test_web_agent.py#L87) | 87 | `"        \"process_coverage_not_factual_probability\""` | — |
| [SRC-F725E90B2A-L000088](../../tests/test_web_agent.py#L88) | 88 | `"    )"` | — |
| [SRC-F725E90B2A-L000089](../../tests/test_web_agent.py#L89) | 89 | `"    assert result[\"search_report\"][\"claim_audit_semantics\"] == ("` | — |
| [SRC-F725E90B2A-L000090](../../tests/test_web_agent.py#L90) | 90 | `"        \"model_assisted_not_independent_fact_check\""` | — |
| [SRC-F725E90B2A-L000091](../../tests/test_web_agent.py#L91) | 91 | `"    )"` | — |
| [SRC-F725E90B2A-L000092](../../tests/test_web_agent.py#L92) | 92 | `"    assert result[\"search_report\"][\"distinct_registrable_domains\"] == 2"` | — |
| [SRC-F725E90B2A-L000093](../../tests/test_web_agent.py#L93) | 93 | `"    assert result[\"search_report\"][\"editorial_independence_status\"] == \"not_assessed\""` | — |
| [SRC-F725E90B2A-L000094](../../tests/test_web_agent.py#L94) | 94 | `"    assert result[\"search_report\"][\"independent_sources_field_semantics\"] == ("` | — |
| [SRC-F725E90B2A-L000095](../../tests/test_web_agent.py#L95) | 95 | `"        \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-F725E90B2A-L000096](../../tests/test_web_agent.py#L96) | 96 | `"    )"` | — |
| [SRC-F725E90B2A-L000097](../../tests/test_web_agent.py#L97) | 97 | `"    assert any(\"تعدد النطاقات المسجلة لا يثبت الاستقلال التحريري\" in warning"` | — |
| [SRC-F725E90B2A-L000098](../../tests/test_web_agent.py#L98) | 98 | `"               for warning in result[\"warnings\"])"` | — |
| [SRC-F725E90B2A-L000099](../../tests/test_web_agent.py#L99) | 99 | `"    assert result[\"used_language_model\"] is True"` | — |
| [SRC-F725E90B2A-L000100](../../tests/test_web_agent.py#L100) | 100 | `"    task_understanding = result[\"task_understanding\"]"` | — |
| [SRC-F725E90B2A-L000101](../../tests/test_web_agent.py#L101) | 101 | `"    assert task_understanding[\"task_spec\"][\"schema\"] == \"omarai.task_spec.v1\""` | — |
| [SRC-F725E90B2A-L000102](../../tests/test_web_agent.py#L102) | 102 | `"    assert task_understanding[\"task_spec\"][\"task_family\"] == \"compare\""` | — |
| [SRC-F725E90B2A-L000103](../../tests/test_web_agent.py#L103) | 103 | `"    assert task_understanding[\"task_spec\"][\"classification_is_probability\"] is False"` | — |
| [SRC-F725E90B2A-L000104](../../tests/test_web_agent.py#L104) | 104 | `"    assert task_understanding[\"tool_execution\"][\"search_outcome\"] == \"attempted_with_usable_sources\""` | — |
| [SRC-F725E90B2A-L000105](../../tests/test_web_agent.py#L105) | 105 | `"    assert task_understanding[\"tool_execution\"][\"accepted_source_count\"] == 2"` | — |
| [SRC-F725E90B2A-L000106](../../tests/test_web_agent.py#L106) | 106 | `"    assert task_understanding[\"query_strategy_matrix\"]"` | — |
| [SRC-F725E90B2A-L000107](../../tests/test_web_agent.py#L107) | 107 | `"    assert task_understanding[\"actual_queries\"] == result[\"search_queries\"]"` | — |
| [SRC-F725E90B2A-L000108](../../tests/test_web_agent.py#L108) | 108 | `"    assert result[\"search_report\"][\"task_understanding\"][\"task_spec\"][\"schema\"] == \"omarai.task_spec.v1\""` | — |
| [SRC-F725E90B2A-L000109](../../tests/test_web_agent.py#L109) | 109 | `"    assert result[\"sources\"][0][\"url\"] == \"https://example.com/research\""` | — |
| [SRC-F725E90B2A-L000110](../../tests/test_web_agent.py#L110) | 110 | `"    assert \"[المصدر 1]\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L000111](../../tests/test_web_agent.py#L111) | 111 | `"    assert seen[\"question\"] == \"قارن هذه التقنية\""` | — |
| [SRC-F725E90B2A-L000112](../../tests/test_web_agent.py#L112) | 112 | `"    assert seen[\"history\"] == [{\"role\": \"user\", \"content\": \"ما هي التقنية؟\"}]"` | — |
| [SRC-F725E90B2A-L000113](../../tests/test_web_agent.py#L113) | 113 | `""` | — |
| [SRC-F725E90B2A-L000114](../../tests/test_web_agent.py#L114) | 114 | `""` | — |
| [SRC-F725E90B2A-L000115](../../tests/test_web_agent.py#L115) | 115 | `"def test_agent_returns_search_snippets_if_model_not_configured(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000116](../../tests/test_web_agent.py#L116) | 116 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000117](../../tests/test_web_agent.py#L117) | 117 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L000118](../../tests/test_web_agent.py#L118) | 118 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000119](../../tests/test_web_agent.py#L119) | 119 | `"        agent,"` | — |
| [SRC-F725E90B2A-L000120](../../tests/test_web_agent.py#L120) | 120 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L000121](../../tests/test_web_agent.py#L121) | 121 | `"        lambda plan: ("` | — |
| [SRC-F725E90B2A-L000122](../../tests/test_web_agent.py#L122) | 122 | `"            [sample_source(0), sample_source(1)],"` | — |
| [SRC-F725E90B2A-L000123](../../tests/test_web_agent.py#L123) | 123 | `"            [],"` | — |
| [SRC-F725E90B2A-L000124](../../tests/test_web_agent.py#L124) | 124 | `"            {"` | — |
| [SRC-F725E90B2A-L000125](../../tests/test_web_agent.py#L125) | 125 | `"                \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L000126](../../tests/test_web_agent.py#L126) | 126 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L000127](../../tests/test_web_agent.py#L127) | 127 | `"                \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L000128](../../tests/test_web_agent.py#L128) | 128 | `"                \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L000129](../../tests/test_web_agent.py#L129) | 129 | `"                \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L000130](../../tests/test_web_agent.py#L130) | 130 | `"                \"providers_used\": [\"test\"],"` | — |
| [SRC-F725E90B2A-L000131](../../tests/test_web_agent.py#L131) | 131 | `"                \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L000132](../../tests/test_web_agent.py#L132) | 132 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L000133](../../tests/test_web_agent.py#L133) | 133 | `"                \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L000134](../../tests/test_web_agent.py#L134) | 134 | `"                \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000135](../../tests/test_web_agent.py#L135) | 135 | `"            },"` | — |
| [SRC-F725E90B2A-L000136](../../tests/test_web_agent.py#L136) | 136 | `"        ),"` | — |
| [SRC-F725E90B2A-L000137](../../tests/test_web_agent.py#L137) | 137 | `"    )"` | — |
| [SRC-F725E90B2A-L000138](../../tests/test_web_agent.py#L138) | 138 | `""` | — |
| [SRC-F725E90B2A-L000139](../../tests/test_web_agent.py#L139) | 139 | `"    result = agent.answer(\"ما الذي يقوله المصدر؟\")"` | — |
| [SRC-F725E90B2A-L000140](../../tests/test_web_agent.py#L140) | 140 | `""` | — |
| [SRC-F725E90B2A-L000141](../../tests/test_web_agent.py#L141) | 141 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-F725E90B2A-L000142](../../tests/test_web_agent.py#L142) | 142 | `"    assert result[\"used_language_model\"] is False"` | — |
| [SRC-F725E90B2A-L000143](../../tests/test_web_agent.py#L143) | 143 | `"    assert result[\"search_report\"][\"pipeline_completion_status\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L000144](../../tests/test_web_agent.py#L144) | 144 | `"    assert result[\"search_report\"][\"completion_stages\"][\"claim_review\"] == \"not_run\""` | — |
| [SRC-F725E90B2A-L000145](../../tests/test_web_agent.py#L145) | 145 | `"    assert \"OPENROUTER_API_KEY\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L000146](../../tests/test_web_agent.py#L146) | 146 | `"    assert result[\"sources\"][0][\"page_fetched\"] is True"` | — |
| [SRC-F725E90B2A-L000147](../../tests/test_web_agent.py#L147) | 147 | `""` | — |
| [SRC-F725E90B2A-L000148](../../tests/test_web_agent.py#L148) | 148 | `""` | — |
| [SRC-F725E90B2A-L000149](../../tests/test_web_agent.py#L149) | 149 | `"def test_agent_rejects_empty_or_oversized_question():"` | — |
| [SRC-F725E90B2A-L000150](../../tests/test_web_agent.py#L150) | 150 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000151](../../tests/test_web_agent.py#L151) | 151 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-F725E90B2A-L000152](../../tests/test_web_agent.py#L152) | 152 | `"        agent.answer(\"   \")"` | — |
| [SRC-F725E90B2A-L000153](../../tests/test_web_agent.py#L153) | 153 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-F725E90B2A-L000154](../../tests/test_web_agent.py#L154) | 154 | `"        agent.answer(\"س\" * 4001)"` | — |
| [SRC-F725E90B2A-L000155](../../tests/test_web_agent.py#L155) | 155 | `""` | — |
| [SRC-F725E90B2A-L000156](../../tests/test_web_agent.py#L156) | 156 | `""` | — |
| [SRC-F725E90B2A-L000157](../../tests/test_web_agent.py#L157) | 157 | `"def test_history_search_query_expands_short_follow_up():"` | — |
| [SRC-F725E90B2A-L000158](../../tests/test_web_agent.py#L158) | 158 | `"    history = [{\"role\": \"user\", \"content\": \"قارن أسعار السيارات الكهربائية في مصر\"}]"` | — |
| [SRC-F725E90B2A-L000159](../../tests/test_web_agent.py#L159) | 159 | `"    query = WebAgent._history_search_query(\"والسعر؟\", history)"` | — |
| [SRC-F725E90B2A-L000160](../../tests/test_web_agent.py#L160) | 160 | `"    assert \"السيارات الكهربائية\" in query"` | — |
| [SRC-F725E90B2A-L000161](../../tests/test_web_agent.py#L161) | 161 | `"    assert \"والسعر؟\" in query"` | — |
| [SRC-F725E90B2A-L000162](../../tests/test_web_agent.py#L162) | 162 | `""` | — |
| [SRC-F725E90B2A-L000163](../../tests/test_web_agent.py#L163) | 163 | `""` | — |
| [SRC-F725E90B2A-L000164](../../tests/test_web_agent.py#L164) | 164 | `"def test_public_url_filter_rejects_local_and_credential_urls():"` | — |
| [SRC-F725E90B2A-L000165](../../tests/test_web_agent.py#L165) | 165 | `"    assert _public_http_url(\"http://127.0.0.1/admin\") is None"` | — |
| [SRC-F725E90B2A-L000166](../../tests/test_web_agent.py#L166) | 166 | `"    assert _public_http_url(\"http://localhost:8000/\") is None"` | — |
| [SRC-F725E90B2A-L000167](../../tests/test_web_agent.py#L167) | 167 | `"    assert _public_http_url(\"https://user:pass@example.com/private\") is None"` | — |
| [SRC-F725E90B2A-L000168](../../tests/test_web_agent.py#L168) | 168 | `"    assert _public_http_url(\"file:///etc/passwd\") is None"` | — |
| [SRC-F725E90B2A-L000169](../../tests/test_web_agent.py#L169) | 169 | `""` | — |
| [SRC-F725E90B2A-L000170](../../tests/test_web_agent.py#L170) | 170 | `""` | — |
| [SRC-F725E90B2A-L000171](../../tests/test_web_agent.py#L171) | 171 | `"def test_public_url_filter_accepts_basic_https_url():"` | — |
| [SRC-F725E90B2A-L000172](../../tests/test_web_agent.py#L172) | 172 | `"    assert _public_http_url(\"https://example.com/path#section\") == \"https://example.com/path\""` | — |
| [SRC-F725E90B2A-L000173](../../tests/test_web_agent.py#L173) | 173 | `""` | — |
| [SRC-F725E90B2A-L000174](../../tests/test_web_agent.py#L174) | 174 | `""` | — |
| [SRC-F725E90B2A-L000175](../../tests/test_web_agent.py#L175) | 175 | `"def test_search_web_parses_duckduckgo_and_bing_without_ddgs(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000176](../../tests/test_web_agent.py#L176) | 176 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000177](../../tests/test_web_agent.py#L177) | 177 | `""` | — |
| [SRC-F725E90B2A-L000178](../../tests/test_web_agent.py#L178) | 178 | `"    html = \"\"\""` | — |
| [SRC-F725E90B2A-L000179](../../tests/test_web_agent.py#L179) | 179 | `"    <html><body>"` | — |
| [SRC-F725E90B2A-L000180](../../tests/test_web_agent.py#L180) | 180 | `"      <div class=\"result\">"` | — |
| [SRC-F725E90B2A-L000181](../../tests/test_web_agent.py#L181) | 181 | `"        <a class=\"result__a\" href=\"https://example.com/first\">صفحة أولى</a>"` | — |
| [SRC-F725E90B2A-L000182](../../tests/test_web_agent.py#L182) | 182 | `"        <a class=\"result__snippet\">سؤال بحث تجريبي مقتطف أول</a>"` | — |
| [SRC-F725E90B2A-L000183](../../tests/test_web_agent.py#L183) | 183 | `"      </div>"` | — |
| [SRC-F725E90B2A-L000184](../../tests/test_web_agent.py#L184) | 184 | `"    </body></html>"` | — |
| [SRC-F725E90B2A-L000185](../../tests/test_web_agent.py#L185) | 185 | `"    \"\"\""` | — |
| [SRC-F725E90B2A-L000186](../../tests/test_web_agent.py#L186) | 186 | `"    rss = \"\"\""` | — |
| [SRC-F725E90B2A-L000187](../../tests/test_web_agent.py#L187) | 187 | `"    <rss><channel><item>"` | — |
| [SRC-F725E90B2A-L000188](../../tests/test_web_agent.py#L188) | 188 | `"      <title>صفحة ثانية</title>"` | — |
| [SRC-F725E90B2A-L000189](../../tests/test_web_agent.py#L189) | 189 | `"      <link>https://example.net/second</link>"` | — |
| [SRC-F725E90B2A-L000190](../../tests/test_web_agent.py#L190) | 190 | `"      <description>سؤال بحث تجريبي مقتطف ثاني</description>"` | — |
| [SRC-F725E90B2A-L000191](../../tests/test_web_agent.py#L191) | 191 | `"    </item></channel></rss>"` | — |
| [SRC-F725E90B2A-L000192](../../tests/test_web_agent.py#L192) | 192 | `"    \"\"\""` | — |
| [SRC-F725E90B2A-L000193](../../tests/test_web_agent.py#L193) | 193 | `""` | — |
| [SRC-F725E90B2A-L000194](../../tests/test_web_agent.py#L194) | 194 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000195](../../tests/test_web_agent.py#L195) | 195 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000196](../../tests/test_web_agent.py#L196) | 196 | `""` | — |
| [SRC-F725E90B2A-L000197](../../tests/test_web_agent.py#L197) | 197 | `"        def __init__(self, text):"` | — |
| [SRC-F725E90B2A-L000198](../../tests/test_web_agent.py#L198) | 198 | `"            self.text = text"` | — |
| [SRC-F725E90B2A-L000199](../../tests/test_web_agent.py#L199) | 199 | `"            self.content = text.encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000200](../../tests/test_web_agent.py#L200) | 200 | `""` | — |
| [SRC-F725E90B2A-L000201](../../tests/test_web_agent.py#L201) | 201 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000202](../../tests/test_web_agent.py#L202) | 202 | `""` | — |
| [SRC-F725E90B2A-L000203](../../tests/test_web_agent.py#L203) | 203 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000204](../../tests/test_web_agent.py#L204) | 204 | `"        calls.append(url)"` | — |
| [SRC-F725E90B2A-L000205](../../tests/test_web_agent.py#L205) | 205 | `"        return FakeResponse(html if \"duckduckgo.com\" in url else rss)"` | — |
| [SRC-F725E90B2A-L000206](../../tests/test_web_agent.py#L206) | 206 | `""` | — |
| [SRC-F725E90B2A-L000207](../../tests/test_web_agent.py#L207) | 207 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000208](../../tests/test_web_agent.py#L208) | 208 | `"    results = WebAgent()._search_web(\"سؤال بحث تجريبي\")"` | — |
| [SRC-F725E90B2A-L000209](../../tests/test_web_agent.py#L209) | 209 | `""` | — |
| [SRC-F725E90B2A-L000210](../../tests/test_web_agent.py#L210) | 210 | `"    assert len(results) == 2"` | — |
| [SRC-F725E90B2A-L000211](../../tests/test_web_agent.py#L211) | 211 | `"    assert results[0][\"title\"] == \"صفحة أولى\""` | — |
| [SRC-F725E90B2A-L000212](../../tests/test_web_agent.py#L212) | 212 | `"    assert results[0][\"url\"] == \"https://example.com/first\""` | — |
| [SRC-F725E90B2A-L000213](../../tests/test_web_agent.py#L213) | 213 | `"    assert results[1][\"title\"] == \"صفحة ثانية\""` | — |
| [SRC-F725E90B2A-L000214](../../tests/test_web_agent.py#L214) | 214 | `"    assert results[1][\"url\"] == \"https://example.net/second\""` | — |
| [SRC-F725E90B2A-L000215](../../tests/test_web_agent.py#L215) | 215 | `"    assert len(calls) == 2"` | — |
| [SRC-F725E90B2A-L000216](../../tests/test_web_agent.py#L216) | 216 | `""` | — |
| [SRC-F725E90B2A-L000217](../../tests/test_web_agent.py#L217) | 217 | `""` | — |
| [SRC-F725E90B2A-L000218](../../tests/test_web_agent.py#L218) | 218 | `""` | — |
| [SRC-F725E90B2A-L000219](../../tests/test_web_agent.py#L219) | 219 | `"def test_model_planner_preserves_social_intent_and_adds_targeted_query(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000220](../../tests/test_web_agent.py#L220) | 220 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000221](../../tests/test_web_agent.py#L221) | 221 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000222](../../tests/test_web_agent.py#L222) | 222 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000223](../../tests/test_web_agent.py#L223) | 223 | `"        agent,"` | — |
| [SRC-F725E90B2A-L000224](../../tests/test_web_agent.py#L224) | 224 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L000225](../../tests/test_web_agent.py#L225) | 225 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-F725E90B2A-L000226](../../tests/test_web_agent.py#L226) | 226 | `"            '{\"queries\":[\"مراجعات السيارات الكهربائية\"],\"social_focus\":true,'"` | — |
| [SRC-F725E90B2A-L000227](../../tests/test_web_agent.py#L227) | 227 | `"            '\"freshness\":\"any\",\"depth\":\"deep\",\"platforms\":[\"reddit\"]}'"` | — |
| [SRC-F725E90B2A-L000228](../../tests/test_web_agent.py#L228) | 228 | `"        ),"` | — |
| [SRC-F725E90B2A-L000229](../../tests/test_web_agent.py#L229) | 229 | `"    )"` | — |
| [SRC-F725E90B2A-L000230](../../tests/test_web_agent.py#L230) | 230 | `"    plan = agent._plan_search("` | — |
| [SRC-F725E90B2A-L000231](../../tests/test_web_agent.py#L231) | 231 | `"        \"ابحث في Reddit عن تجارب العملاء مع السيارات الكهربائية\","` | — |
| [SRC-F725E90B2A-L000232](../../tests/test_web_agent.py#L232) | 232 | `"        [],"` | — |
| [SRC-F725E90B2A-L000233](../../tests/test_web_agent.py#L233) | 233 | `"    )"` | — |
| [SRC-F725E90B2A-L000234](../../tests/test_web_agent.py#L234) | 234 | `"    assert plan[\"planning_method\"] == \"language_model\""` | — |
| [SRC-F725E90B2A-L000235](../../tests/test_web_agent.py#L235) | 235 | `"    assert plan[\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L000236](../../tests/test_web_agent.py#L236) | 236 | `"    assert \"reddit\" in plan[\"platforms\"]"` | — |
| [SRC-F725E90B2A-L000237](../../tests/test_web_agent.py#L237) | 237 | `"    assert any(\"site:reddit.com\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L000238](../../tests/test_web_agent.py#L238) | 238 | `""` | — |
| [SRC-F725E90B2A-L000239](../../tests/test_web_agent.py#L239) | 239 | `""` | — |
| [SRC-F725E90B2A-L000240](../../tests/test_web_agent.py#L240) | 240 | `"def test_direct_social_search_reads_public_reddit_and_bluesky_results(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000241](../../tests/test_web_agent.py#L241) | 241 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000242](../../tests/test_web_agent.py#L242) | 242 | `""` | — |
| [SRC-F725E90B2A-L000243](../../tests/test_web_agent.py#L243) | 243 | `"    reddit_xml = \"\"\"<rss><channel><item>"` | — |
| [SRC-F725E90B2A-L000244](../../tests/test_web_agent.py#L244) | 244 | `"      <title>تجربة سيارة كهربائية</title>"` | — |
| [SRC-F725E90B2A-L000245](../../tests/test_web_agent.py#L245) | 245 | `"      <link>https://www.reddit.com/r/cars/comments/abc123/test/</link>"` | — |
| [SRC-F725E90B2A-L000246](../../tests/test_web_agent.py#L246) | 246 | `"      <description>استهلاك البطارية في الحر</description>"` | — |
| [SRC-F725E90B2A-L000247](../../tests/test_web_agent.py#L247) | 247 | `"      <pubDate>Mon, 12 Oct 2026 10:00:00 GMT</pubDate>"` | — |
| [SRC-F725E90B2A-L000248](../../tests/test_web_agent.py#L248) | 248 | `"    </item></channel></rss>\"\"\""` | — |
| [SRC-F725E90B2A-L000249](../../tests/test_web_agent.py#L249) | 249 | `""` | — |
| [SRC-F725E90B2A-L000250](../../tests/test_web_agent.py#L250) | 250 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000251](../../tests/test_web_agent.py#L251) | 251 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000252](../../tests/test_web_agent.py#L252) | 252 | `""` | — |
| [SRC-F725E90B2A-L000253](../../tests/test_web_agent.py#L253) | 253 | `"        def __init__(self, text=\"\", data=None):"` | — |
| [SRC-F725E90B2A-L000254](../../tests/test_web_agent.py#L254) | 254 | `"            self.text = text"` | — |
| [SRC-F725E90B2A-L000255](../../tests/test_web_agent.py#L255) | 255 | `"            self.content = text.encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000256](../../tests/test_web_agent.py#L256) | 256 | `"            self._data = data or {}"` | — |
| [SRC-F725E90B2A-L000257](../../tests/test_web_agent.py#L257) | 257 | `""` | — |
| [SRC-F725E90B2A-L000258](../../tests/test_web_agent.py#L258) | 258 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000259](../../tests/test_web_agent.py#L259) | 259 | `"            return self._data"` | — |
| [SRC-F725E90B2A-L000260](../../tests/test_web_agent.py#L260) | 260 | `""` | — |
| [SRC-F725E90B2A-L000261](../../tests/test_web_agent.py#L261) | 261 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000262](../../tests/test_web_agent.py#L262) | 262 | `"        if \"reddit.com\" in url:"` | — |
| [SRC-F725E90B2A-L000263](../../tests/test_web_agent.py#L263) | 263 | `"            return FakeResponse(reddit_xml)"` | — |
| [SRC-F725E90B2A-L000264](../../tests/test_web_agent.py#L264) | 264 | `"        if \"bsky.app\" in url or \"public.api.bsky.app\" in url:"` | — |
| [SRC-F725E90B2A-L000265](../../tests/test_web_agent.py#L265) | 265 | `"            return FakeResponse(data={"` | — |
| [SRC-F725E90B2A-L000266](../../tests/test_web_agent.py#L266) | 266 | `"                \"posts\": [{"` | — |
| [SRC-F725E90B2A-L000267](../../tests/test_web_agent.py#L267) | 267 | `"                    \"post\": {"` | — |
| [SRC-F725E90B2A-L000268](../../tests/test_web_agent.py#L268) | 268 | `"                        \"uri\": \"at://did:plc:example/app.bsky.feed.post/rkey123\","` | — |
| [SRC-F725E90B2A-L000269](../../tests/test_web_agent.py#L269) | 269 | `"                        \"indexedAt\": \"2026-10-12T10:00:00Z\","` | — |
| [SRC-F725E90B2A-L000270](../../tests/test_web_agent.py#L270) | 270 | `"                        \"record\": {\"text\": \"استخدمت السيارة شهرًا\"},"` | — |
| [SRC-F725E90B2A-L000271](../../tests/test_web_agent.py#L271) | 271 | `"                        \"author\": {\"handle\": \"driver.bsky.social\", \"displayName\": \"Driver\"},"` | — |
| [SRC-F725E90B2A-L000272](../../tests/test_web_agent.py#L272) | 272 | `"                    }"` | — |
| [SRC-F725E90B2A-L000273](../../tests/test_web_agent.py#L273) | 273 | `"                }]"` | — |
| [SRC-F725E90B2A-L000274](../../tests/test_web_agent.py#L274) | 274 | `"            })"` | — |
| [SRC-F725E90B2A-L000275](../../tests/test_web_agent.py#L275) | 275 | `"        raise AssertionError(f\"Unexpected URL: {url}\")"` | — |
| [SRC-F725E90B2A-L000276](../../tests/test_web_agent.py#L276) | 276 | `""` | — |
| [SRC-F725E90B2A-L000277](../../tests/test_web_agent.py#L277) | 277 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000278](../../tests/test_web_agent.py#L278) | 278 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000279](../../tests/test_web_agent.py#L279) | 279 | `"        \"سيارة كهربائية\", [\"reddit\", \"bluesky\"]"` | — |
| [SRC-F725E90B2A-L000280](../../tests/test_web_agent.py#L280) | 280 | `"    )"` | — |
| [SRC-F725E90B2A-L000281](../../tests/test_web_agent.py#L281) | 281 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000282](../../tests/test_web_agent.py#L282) | 282 | `"    assert any(item[\"provider\"] == \"reddit_public_rss\" for item in results)"` | — |
| [SRC-F725E90B2A-L000283](../../tests/test_web_agent.py#L283) | 283 | `"    bsky = next(item for item in results if item[\"provider\"] == \"bluesky_public_search\")"` | — |
| [SRC-F725E90B2A-L000284](../../tests/test_web_agent.py#L284) | 284 | `"    assert bsky[\"url\"] == \"https://bsky.app/profile/driver.bsky.social/post/rkey123\""` | — |
| [SRC-F725E90B2A-L000285](../../tests/test_web_agent.py#L285) | 285 | `"    assert bsky[\"snippet\"] == \"استخدمت السيارة شهرًا\""` | — |
| [SRC-F725E90B2A-L000286](../../tests/test_web_agent.py#L286) | 286 | `""` | — |
| [SRC-F725E90B2A-L000287](../../tests/test_web_agent.py#L287) | 287 | `""` | — |
| [SRC-F725E90B2A-L000288](../../tests/test_web_agent.py#L288) | 288 | `"def test_research_collection_fuses_multiple_queries_and_reports_provenance(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000289](../../tests/test_web_agent.py#L289) | 289 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000290](../../tests/test_web_agent.py#L290) | 290 | `""` | — |
| [SRC-F725E90B2A-L000291](../../tests/test_web_agent.py#L291) | 291 | `"    def search(query):"` | — |
| [SRC-F725E90B2A-L000292](../../tests/test_web_agent.py#L292) | 292 | `"        if query == \"query one\":"` | — |
| [SRC-F725E90B2A-L000293](../../tests/test_web_agent.py#L293) | 293 | `"            return ["` | — |
| [SRC-F725E90B2A-L000294](../../tests/test_web_agent.py#L294) | 294 | `"                {\"title\": \"Shared\", \"url\": \"https://example.com/shared\", \"snippet\": \"Some evidence\", \"provider\": \"ddg\", \"provider_rank\": 1},"` | — |
| [SRC-F725E90B2A-L000295](../../tests/test_web_agent.py#L295) | 295 | `"                {\"title\": \"Unique A\", \"url\": \"https://example.com/a\", \"snippet\": \"Evidence A\", \"provider\": \"ddg\", \"provider_rank\": 2},"` | — |
| [SRC-F725E90B2A-L000296](../../tests/test_web_agent.py#L296) | 296 | `"            ]"` | — |
| [SRC-F725E90B2A-L000297](../../tests/test_web_agent.py#L297) | 297 | `"        return ["` | — |
| [SRC-F725E90B2A-L000298](../../tests/test_web_agent.py#L298) | 298 | `"            {\"title\": \"Shared item\", \"url\": \"https://example.com/shared\", \"snippet\": \"More evidence about this result\", \"provider\": \"bing\", \"provider_rank\": 1},"` | — |
| [SRC-F725E90B2A-L000299](../../tests/test_web_agent.py#L299) | 299 | `"            {\"title\": \"Unique B\", \"url\": \"https://example.com/b\", \"snippet\": \"Evidence B\", \"provider\": \"bing\", \"provider_rank\": 2},"` | — |
| [SRC-F725E90B2A-L000300](../../tests/test_web_agent.py#L300) | 300 | `"        ]"` | — |
| [SRC-F725E90B2A-L000301](../../tests/test_web_agent.py#L301) | 301 | `""` | — |
| [SRC-F725E90B2A-L000302](../../tests/test_web_agent.py#L302) | 302 | `"    monkeypatch.setattr(agent, \"_search_web\", search)"` | — |
| [SRC-F725E90B2A-L000303](../../tests/test_web_agent.py#L303) | 303 | `"    monkeypatch.setattr(agent, \"_fetch_page\", lambda url: (\"Read title\", \"Extracted public page text\"))"` | — |
| [SRC-F725E90B2A-L000304](../../tests/test_web_agent.py#L304) | 304 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-F725E90B2A-L000305](../../tests/test_web_agent.py#L305) | 305 | `"        \"queries\": [\"query one\", \"query two\"],"` | — |
| [SRC-F725E90B2A-L000306](../../tests/test_web_agent.py#L306) | 306 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L000307](../../tests/test_web_agent.py#L307) | 307 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L000308](../../tests/test_web_agent.py#L308) | 308 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000309](../../tests/test_web_agent.py#L309) | 309 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000310](../../tests/test_web_agent.py#L310) | 310 | `"    })"` | — |
| [SRC-F725E90B2A-L000311](../../tests/test_web_agent.py#L311) | 311 | `"    shared = next(item for item in sources if \"shared\" in item[\"url\"])"` | — |
| [SRC-F725E90B2A-L000312](../../tests/test_web_agent.py#L312) | 312 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000313](../../tests/test_web_agent.py#L313) | 313 | `"    assert len(sources) == 3"` | — |
| [SRC-F725E90B2A-L000314](../../tests/test_web_agent.py#L314) | 314 | `"    assert set(shared[\"providers\"]) == {\"ddg\", \"bing\"}"` | — |
| [SRC-F725E90B2A-L000315](../../tests/test_web_agent.py#L315) | 315 | `"    assert {\"query one\", \"query two\"}.issubset(set(shared[\"queries\"]))"` | — |
| [SRC-F725E90B2A-L000316](../../tests/test_web_agent.py#L316) | 316 | `"    assert len(shared[\"queries\"]) >= 2"` | — |
| [SRC-F725E90B2A-L000317](../../tests/test_web_agent.py#L317) | 317 | `"    assert report[\"queries_planned\"] >= 2"` | — |
| [SRC-F725E90B2A-L000318](../../tests/test_web_agent.py#L318) | 318 | `"    assert report[\"queries_attempted\"] >= 2"` | — |
| [SRC-F725E90B2A-L000319](../../tests/test_web_agent.py#L319) | 319 | `"    assert report[\"expansion_queries\"]"` | — |
| [SRC-F725E90B2A-L000320](../../tests/test_web_agent.py#L320) | 320 | `"    assert report[\"pages_fetched\"] == 3"` | — |
| [SRC-F725E90B2A-L000321](../../tests/test_web_agent.py#L321) | 321 | `"    assert \"ddg\" in report[\"providers_used\"]"` | — |
| [SRC-F725E90B2A-L000322](../../tests/test_web_agent.py#L322) | 322 | `"    assert \"bing\" in report[\"providers_used\"]"` | — |
| [SRC-F725E90B2A-L000323](../../tests/test_web_agent.py#L323) | 323 | `""` | — |
| [SRC-F725E90B2A-L000324](../../tests/test_web_agent.py#L324) | 324 | `""` | — |
| [SRC-F725E90B2A-L000325](../../tests/test_web_agent.py#L325) | 325 | `"def test_research_collection_preserves_results_when_query_budget_is_exhausted(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000326](../../tests/test_web_agent.py#L326) | 326 | `"    \"\"\"A budget-limited query must not erase evidence returned by other queries.\"\"\""` | — |
| [SRC-F725E90B2A-L000327](../../tests/test_web_agent.py#L327) | 327 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000328](../../tests/test_web_agent.py#L328) | 328 | `""` | — |
| [SRC-F725E90B2A-L000329](../../tests/test_web_agent.py#L329) | 329 | `"    def search(query):"` | — |
| [SRC-F725E90B2A-L000330](../../tests/test_web_agent.py#L330) | 330 | `"        if query == \"query over budget\":"` | — |
| [SRC-F725E90B2A-L000331](../../tests/test_web_agent.py#L331) | 331 | `"            raise RequestBudgetExceeded(\"تم بلوغ حد موارد الطلب: search_queries.\")"` | — |
| [SRC-F725E90B2A-L000332](../../tests/test_web_agent.py#L332) | 332 | `"        return ["` | — |
| [SRC-F725E90B2A-L000333](../../tests/test_web_agent.py#L333) | 333 | `"            {"` | — |
| [SRC-F725E90B2A-L000334](../../tests/test_web_agent.py#L334) | 334 | `"                **sample_source(0),"` | — |
| [SRC-F725E90B2A-L000335](../../tests/test_web_agent.py#L335) | 335 | `"                \"provider\": \"test_provider\","` | — |
| [SRC-F725E90B2A-L000336](../../tests/test_web_agent.py#L336) | 336 | `"                \"provider_rank\": 1,"` | — |
| [SRC-F725E90B2A-L000337](../../tests/test_web_agent.py#L337) | 337 | `"                \"search_query\": query,"` | — |
| [SRC-F725E90B2A-L000338](../../tests/test_web_agent.py#L338) | 338 | `"                \"queries\": [query],"` | — |
| [SRC-F725E90B2A-L000339](../../tests/test_web_agent.py#L339) | 339 | `"            },"` | — |
| [SRC-F725E90B2A-L000340](../../tests/test_web_agent.py#L340) | 340 | `"            {"` | — |
| [SRC-F725E90B2A-L000341](../../tests/test_web_agent.py#L341) | 341 | `"                **sample_source(1),"` | — |
| [SRC-F725E90B2A-L000342](../../tests/test_web_agent.py#L342) | 342 | `"                \"provider\": \"test_provider\","` | — |
| [SRC-F725E90B2A-L000343](../../tests/test_web_agent.py#L343) | 343 | `"                \"provider_rank\": 2,"` | — |
| [SRC-F725E90B2A-L000344](../../tests/test_web_agent.py#L344) | 344 | `"                \"search_query\": query,"` | — |
| [SRC-F725E90B2A-L000345](../../tests/test_web_agent.py#L345) | 345 | `"                \"queries\": [query],"` | — |
| [SRC-F725E90B2A-L000346](../../tests/test_web_agent.py#L346) | 346 | `"            },"` | — |
| [SRC-F725E90B2A-L000347](../../tests/test_web_agent.py#L347) | 347 | `"        ]"` | — |
| [SRC-F725E90B2A-L000348](../../tests/test_web_agent.py#L348) | 348 | `""` | — |
| [SRC-F725E90B2A-L000349](../../tests/test_web_agent.py#L349) | 349 | `"    monkeypatch.setattr(agent, \"_search_web\", search)"` | — |
| [SRC-F725E90B2A-L000350](../../tests/test_web_agent.py#L350) | 350 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000351](../../tests/test_web_agent.py#L351) | 351 | `"        agent, \"_fetch_page\", lambda url: (\"Read title\", \"Extracted public page text\")"` | — |
| [SRC-F725E90B2A-L000352](../../tests/test_web_agent.py#L352) | 352 | `"    )"` | — |
| [SRC-F725E90B2A-L000353](../../tests/test_web_agent.py#L353) | 353 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-F725E90B2A-L000354](../../tests/test_web_agent.py#L354) | 354 | `"        \"queries\": [\"query over budget\", \"query success\"],"` | — |
| [SRC-F725E90B2A-L000355](../../tests/test_web_agent.py#L355) | 355 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L000356](../../tests/test_web_agent.py#L356) | 356 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L000357](../../tests/test_web_agent.py#L357) | 357 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L000358](../../tests/test_web_agent.py#L358) | 358 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000359](../../tests/test_web_agent.py#L359) | 359 | `"    })"` | — |
| [SRC-F725E90B2A-L000360](../../tests/test_web_agent.py#L360) | 360 | `""` | — |
| [SRC-F725E90B2A-L000361](../../tests/test_web_agent.py#L361) | 361 | `"    assert len(sources) == 2"` | — |
| [SRC-F725E90B2A-L000362](../../tests/test_web_agent.py#L362) | 362 | `"    assert report[\"pages_fetched\"] == 2"` | — |
| [SRC-F725E90B2A-L000363](../../tests/test_web_agent.py#L363) | 363 | `"    assert report[\"queries_planned\"] == 2"` | — |
| [SRC-F725E90B2A-L000364](../../tests/test_web_agent.py#L364) | 364 | `"    assert any(\"search_queries\" in warning for warning in warnings)"` | — |
| [SRC-F725E90B2A-L000365](../../tests/test_web_agent.py#L365) | 365 | `""` | — |
| [SRC-F725E90B2A-L000366](../../tests/test_web_agent.py#L366) | 366 | `""` | — |
| [SRC-F725E90B2A-L000367](../../tests/test_web_agent.py#L367) | 367 | `"def test_deep_expansion_budget_error_keeps_initial_evidence(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000368](../../tests/test_web_agent.py#L368) | 368 | `"    \"\"\"A failed deep-search expansion must leave its already collected source usable.\"\"\""` | — |
| [SRC-F725E90B2A-L000369](../../tests/test_web_agent.py#L369) | 369 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000370](../../tests/test_web_agent.py#L370) | 370 | `""` | — |
| [SRC-F725E90B2A-L000371](../../tests/test_web_agent.py#L371) | 371 | `"    def search(query):"` | — |
| [SRC-F725E90B2A-L000372](../../tests/test_web_agent.py#L372) | 372 | `"        if query == \"deep topic\":"` | — |
| [SRC-F725E90B2A-L000373](../../tests/test_web_agent.py#L373) | 373 | `"            return [{"` | — |
| [SRC-F725E90B2A-L000374](../../tests/test_web_agent.py#L374) | 374 | `"                **sample_source(0),"` | — |
| [SRC-F725E90B2A-L000375](../../tests/test_web_agent.py#L375) | 375 | `"                \"provider\": \"test_provider\","` | — |
| [SRC-F725E90B2A-L000376](../../tests/test_web_agent.py#L376) | 376 | `"                \"provider_rank\": 1,"` | — |
| [SRC-F725E90B2A-L000377](../../tests/test_web_agent.py#L377) | 377 | `"                \"search_query\": query,"` | — |
| [SRC-F725E90B2A-L000378](../../tests/test_web_agent.py#L378) | 378 | `"                \"queries\": [query],"` | — |
| [SRC-F725E90B2A-L000379](../../tests/test_web_agent.py#L379) | 379 | `"            }]"` | — |
| [SRC-F725E90B2A-L000380](../../tests/test_web_agent.py#L380) | 380 | `"        raise RequestBudgetExceeded(\"تم بلوغ حد موارد الطلب: search_queries.\")"` | — |
| [SRC-F725E90B2A-L000381](../../tests/test_web_agent.py#L381) | 381 | `""` | — |
| [SRC-F725E90B2A-L000382](../../tests/test_web_agent.py#L382) | 382 | `"    monkeypatch.setattr(agent, \"_search_web\", search)"` | — |
| [SRC-F725E90B2A-L000383](../../tests/test_web_agent.py#L383) | 383 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000384](../../tests/test_web_agent.py#L384) | 384 | `"        agent, \"_fetch_page\", lambda url: (\"Read title\", \"Extracted public page text\")"` | — |
| [SRC-F725E90B2A-L000385](../../tests/test_web_agent.py#L385) | 385 | `"    )"` | — |
| [SRC-F725E90B2A-L000386](../../tests/test_web_agent.py#L386) | 386 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-F725E90B2A-L000387](../../tests/test_web_agent.py#L387) | 387 | `"        \"queries\": [\"deep topic\"],"` | — |
| [SRC-F725E90B2A-L000388](../../tests/test_web_agent.py#L388) | 388 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L000389](../../tests/test_web_agent.py#L389) | 389 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L000390](../../tests/test_web_agent.py#L390) | 390 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000391](../../tests/test_web_agent.py#L391) | 391 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000392](../../tests/test_web_agent.py#L392) | 392 | `"    })"` | — |
| [SRC-F725E90B2A-L000393](../../tests/test_web_agent.py#L393) | 393 | `""` | — |
| [SRC-F725E90B2A-L000394](../../tests/test_web_agent.py#L394) | 394 | `"    assert len(sources) == 1"` | — |
| [SRC-F725E90B2A-L000395](../../tests/test_web_agent.py#L395) | 395 | `"    assert sources[0][\"page_fetched\"] is True"` | — |
| [SRC-F725E90B2A-L000396](../../tests/test_web_agent.py#L396) | 396 | `"    assert report[\"pages_fetched\"] == 1"` | — |
| [SRC-F725E90B2A-L000397](../../tests/test_web_agent.py#L397) | 397 | `"    assert report[\"expansion_queries\"]"` | — |
| [SRC-F725E90B2A-L000398](../../tests/test_web_agent.py#L398) | 398 | `"    assert any(\"search_queries\" in warning for warning in warnings)"` | — |
| [SRC-F725E90B2A-L000399](../../tests/test_web_agent.py#L399) | 399 | `""` | — |
| [SRC-F725E90B2A-L000400](../../tests/test_web_agent.py#L400) | 400 | `""` | — |
| [SRC-F725E90B2A-L000401](../../tests/test_web_agent.py#L401) | 401 | `""` | — |
| [SRC-F725E90B2A-L000402](../../tests/test_web_agent.py#L402) | 402 | `"def test_invalid_citations_are_removed_and_valid_ones_preserved():"` | — |
| [SRC-F725E90B2A-L000403](../../tests/test_web_agent.py#L403) | 403 | `"    answer, warnings = WebAgent._remove_invalid_citations("` | — |
| [SRC-F725E90B2A-L000404](../../tests/test_web_agent.py#L404) | 404 | `"        \"النتيجة [المصدر 1] وادعاء آخر [المصدر 11].\", 1"` | — |
| [SRC-F725E90B2A-L000405](../../tests/test_web_agent.py#L405) | 405 | `"    )"` | — |
| [SRC-F725E90B2A-L000406](../../tests/test_web_agent.py#L406) | 406 | `"    assert \"[المصدر 1]\" in answer"` | — |
| [SRC-F725E90B2A-L000407](../../tests/test_web_agent.py#L407) | 407 | `"    assert \"[المصدر 11]\" not in answer"` | — |
| [SRC-F725E90B2A-L000408](../../tests/test_web_agent.py#L408) | 408 | `"    assert len(warnings) == 1"` | — |
| [SRC-F725E90B2A-L000409](../../tests/test_web_agent.py#L409) | 409 | `""` | — |
| [SRC-F725E90B2A-L000410](../../tests/test_web_agent.py#L410) | 410 | `""` | — |
| [SRC-F725E90B2A-L000411](../../tests/test_web_agent.py#L411) | 411 | `"def test_citation_metadata_limits_claim_to_index_range_validation():"` | — |
| [SRC-F725E90B2A-L000412](../../tests/test_web_agent.py#L412) | 412 | `"    metadata = WebAgent._citation_validation_metadata("` | — |
| [SRC-F725E90B2A-L000413](../../tests/test_web_agent.py#L413) | 413 | `"        \"النتيجة المدعومة مبدئيًا [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L000414](../../tests/test_web_agent.py#L414) | 414 | `"        1,"` | — |
| [SRC-F725E90B2A-L000415](../../tests/test_web_agent.py#L415) | 415 | `"        [],"` | — |
| [SRC-F725E90B2A-L000416](../../tests/test_web_agent.py#L416) | 416 | `"        \"model_claim_audit_completed\","` | — |
| [SRC-F725E90B2A-L000417](../../tests/test_web_agent.py#L417) | 417 | `"    )"` | — |
| [SRC-F725E90B2A-L000418](../../tests/test_web_agent.py#L418) | 418 | `"    assert metadata == {"` | — |
| [SRC-F725E90B2A-L000419](../../tests/test_web_agent.py#L419) | 419 | `"        \"method\": \"numeric_source_index_range_only\","` | — |
| [SRC-F725E90B2A-L000420](../../tests/test_web_agent.py#L420) | 420 | `"        \"status\": \"index_range_check_passed\","` | — |
| [SRC-F725E90B2A-L000421](../../tests/test_web_agent.py#L421) | 421 | `"        \"valid_citation_count\": 1,"` | — |
| [SRC-F725E90B2A-L000422](../../tests/test_web_agent.py#L422) | 422 | `"        \"invalid_references_removed\": 0,"` | — |
| [SRC-F725E90B2A-L000423](../../tests/test_web_agent.py#L423) | 423 | `"        \"max_citable_source_index\": 1,"` | — |
| [SRC-F725E90B2A-L000424](../../tests/test_web_agent.py#L424) | 424 | `"        \"claim_support\": \"model_review_not_independent_fact_check\","` | — |
| [SRC-F725E90B2A-L000425](../../tests/test_web_agent.py#L425) | 425 | `"    }"` | — |
| [SRC-F725E90B2A-L000426](../../tests/test_web_agent.py#L426) | 426 | `""` | — |
| [SRC-F725E90B2A-L000427](../../tests/test_web_agent.py#L427) | 427 | `""` | — |
| [SRC-F725E90B2A-L000428](../../tests/test_web_agent.py#L428) | 428 | `"def test_citation_metadata_reports_invalid_reference_repair():"` | — |
| [SRC-F725E90B2A-L000429](../../tests/test_web_agent.py#L429) | 429 | `"    cleaned, warnings = WebAgent._remove_invalid_citations("` | — |
| [SRC-F725E90B2A-L000430](../../tests/test_web_agent.py#L430) | 430 | `"        \"صحيح [المصدر 1] وخاطئ [المصدر 9].\", 1"` | — |
| [SRC-F725E90B2A-L000431](../../tests/test_web_agent.py#L431) | 431 | `"    )"` | — |
| [SRC-F725E90B2A-L000432](../../tests/test_web_agent.py#L432) | 432 | `"    metadata = WebAgent._citation_validation_metadata("` | — |
| [SRC-F725E90B2A-L000433](../../tests/test_web_agent.py#L433) | 433 | `"        cleaned, 1, warnings, \"not_run\""` | — |
| [SRC-F725E90B2A-L000434](../../tests/test_web_agent.py#L434) | 434 | `"    )"` | — |
| [SRC-F725E90B2A-L000435](../../tests/test_web_agent.py#L435) | 435 | `"    assert metadata[\"status\"] == \"invalid_index_references_removed\""` | — |
| [SRC-F725E90B2A-L000436](../../tests/test_web_agent.py#L436) | 436 | `"    assert metadata[\"valid_citation_count\"] == 1"` | — |
| [SRC-F725E90B2A-L000437](../../tests/test_web_agent.py#L437) | 437 | `"    assert metadata[\"invalid_references_removed\"] == 1"` | — |
| [SRC-F725E90B2A-L000438](../../tests/test_web_agent.py#L438) | 438 | `"    assert metadata[\"claim_support\"] == \"not_verified\""` | — |
| [SRC-F725E90B2A-L000439](../../tests/test_web_agent.py#L439) | 439 | `""` | — |
| [SRC-F725E90B2A-L000440](../../tests/test_web_agent.py#L440) | 440 | `""` | — |
| [SRC-F725E90B2A-L000441](../../tests/test_web_agent.py#L441) | 441 | `"def test_citation_metadata_reports_absent_markers_and_empty_source_range():"` | — |
| [SRC-F725E90B2A-L000442](../../tests/test_web_agent.py#L442) | 442 | `"    metadata = WebAgent._citation_validation_metadata("` | — |
| [SRC-F725E90B2A-L000443](../../tests/test_web_agent.py#L443) | 443 | `"        \"لا توجد إحالات للمصادر.\", 0, [], \"not_run\""` | — |
| [SRC-F725E90B2A-L000444](../../tests/test_web_agent.py#L444) | 444 | `"    )"` | — |
| [SRC-F725E90B2A-L000445](../../tests/test_web_agent.py#L445) | 445 | `"    assert metadata[\"status\"] == \"no_citation_markers_present\""` | — |
| [SRC-F725E90B2A-L000446](../../tests/test_web_agent.py#L446) | 446 | `"    assert metadata[\"valid_citation_count\"] == 0"` | — |
| [SRC-F725E90B2A-L000447](../../tests/test_web_agent.py#L447) | 447 | `"    assert metadata[\"max_citable_source_index\"] == 0"` | — |
| [SRC-F725E90B2A-L000448](../../tests/test_web_agent.py#L448) | 448 | `""` | — |
| [SRC-F725E90B2A-L000449](../../tests/test_web_agent.py#L449) | 449 | `""` | — |
| [SRC-F725E90B2A-L000450](../../tests/test_web_agent.py#L450) | 450 | `"def test_user_supplied_url_is_prioritized_and_page_content_is_extracted(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000451](../../tests/test_web_agent.py#L451) | 451 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000452](../../tests/test_web_agent.py#L452) | 452 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: [])"` | — |
| [SRC-F725E90B2A-L000453](../../tests/test_web_agent.py#L453) | 453 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000454](../../tests/test_web_agent.py#L454) | 454 | `"        agent,"` | — |
| [SRC-F725E90B2A-L000455](../../tests/test_web_agent.py#L455) | 455 | `"        \"_fetch_page\","` | — |
| [SRC-F725E90B2A-L000456](../../tests/test_web_agent.py#L456) | 456 | `"        lambda url: (\"User page title\", \"Full public page text supplied for analysis\"),"` | — |
| [SRC-F725E90B2A-L000457](../../tests/test_web_agent.py#L457) | 457 | `"    )"` | — |
| [SRC-F725E90B2A-L000458](../../tests/test_web_agent.py#L458) | 458 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-F725E90B2A-L000459](../../tests/test_web_agent.py#L459) | 459 | `"        \"queries\": [\"لخص هذه الصفحة\"],"` | — |
| [SRC-F725E90B2A-L000460](../../tests/test_web_agent.py#L460) | 460 | `"        \"direct_urls\": [\"https://example.com/article\"],"` | — |
| [SRC-F725E90B2A-L000461](../../tests/test_web_agent.py#L461) | 461 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L000462](../../tests/test_web_agent.py#L462) | 462 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L000463](../../tests/test_web_agent.py#L463) | 463 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000464](../../tests/test_web_agent.py#L464) | 464 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000465](../../tests/test_web_agent.py#L465) | 465 | `"    })"` | — |
| [SRC-F725E90B2A-L000466](../../tests/test_web_agent.py#L466) | 466 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000467](../../tests/test_web_agent.py#L467) | 467 | `"    assert len(sources) == 1"` | — |
| [SRC-F725E90B2A-L000468](../../tests/test_web_agent.py#L468) | 468 | `"    assert sources[0][\"url\"] == \"https://example.com/article\""` | — |
| [SRC-F725E90B2A-L000469](../../tests/test_web_agent.py#L469) | 469 | `"    assert sources[0][\"title\"] == \"User page title\""` | — |
| [SRC-F725E90B2A-L000470](../../tests/test_web_agent.py#L470) | 470 | `"    assert sources[0][\"page_fetched\"] is True"` | — |
| [SRC-F725E90B2A-L000471](../../tests/test_web_agent.py#L471) | 471 | `"    assert \"user_supplied_url\" in report[\"providers_used\"]"` | — |
| [SRC-F725E90B2A-L000472](../../tests/test_web_agent.py#L472) | 472 | `""` | — |
| [SRC-F725E90B2A-L000473](../../tests/test_web_agent.py#L473) | 473 | `""` | — |
| [SRC-F725E90B2A-L000474](../../tests/test_web_agent.py#L474) | 474 | `""` | — |
| [SRC-F725E90B2A-L000475](../../tests/test_web_agent.py#L475) | 475 | `"def test_official_x_search_is_used_only_with_explicit_bearer_token(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000476](../../tests/test_web_agent.py#L476) | 476 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000477](../../tests/test_web_agent.py#L477) | 477 | `""` | — |
| [SRC-F725E90B2A-L000478](../../tests/test_web_agent.py#L478) | 478 | `"    monkeypatch.setenv(\"X_BEARER_TOKEN\", \"test-token\")"` | — |
| [SRC-F725E90B2A-L000479](../../tests/test_web_agent.py#L479) | 479 | `""` | — |
| [SRC-F725E90B2A-L000480](../../tests/test_web_agent.py#L480) | 480 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000481](../../tests/test_web_agent.py#L481) | 481 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000482](../../tests/test_web_agent.py#L482) | 482 | `""` | — |
| [SRC-F725E90B2A-L000483](../../tests/test_web_agent.py#L483) | 483 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000484](../../tests/test_web_agent.py#L484) | 484 | `"            return {"` | — |
| [SRC-F725E90B2A-L000485](../../tests/test_web_agent.py#L485) | 485 | `"                \"data\": [{"` | — |
| [SRC-F725E90B2A-L000486](../../tests/test_web_agent.py#L486) | 486 | `"                    \"id\": \"1840000000000000000\","` | — |
| [SRC-F725E90B2A-L000487](../../tests/test_web_agent.py#L487) | 487 | `"                    \"text\": \"تجربة علنية لاستهلاك سيارة كهربائية\","` | — |
| [SRC-F725E90B2A-L000488](../../tests/test_web_agent.py#L488) | 488 | `"                    \"created_at\": \"2026-10-12T10:00:00Z\","` | — |
| [SRC-F725E90B2A-L000489](../../tests/test_web_agent.py#L489) | 489 | `"                    \"author_id\": \"u1\","` | — |
| [SRC-F725E90B2A-L000490](../../tests/test_web_agent.py#L490) | 490 | `"                }],"` | — |
| [SRC-F725E90B2A-L000491](../../tests/test_web_agent.py#L491) | 491 | `"                \"includes\": {"` | — |
| [SRC-F725E90B2A-L000492](../../tests/test_web_agent.py#L492) | 492 | `"                    \"users\": [{\"id\": \"u1\", \"username\": \"driver\", \"name\": \"Driver\"}]"` | — |
| [SRC-F725E90B2A-L000493](../../tests/test_web_agent.py#L493) | 493 | `"                },"` | — |
| [SRC-F725E90B2A-L000494](../../tests/test_web_agent.py#L494) | 494 | `"            }"` | — |
| [SRC-F725E90B2A-L000495](../../tests/test_web_agent.py#L495) | 495 | `""` | — |
| [SRC-F725E90B2A-L000496](../../tests/test_web_agent.py#L496) | 496 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000497](../../tests/test_web_agent.py#L497) | 497 | `""` | — |
| [SRC-F725E90B2A-L000498](../../tests/test_web_agent.py#L498) | 498 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000499](../../tests/test_web_agent.py#L499) | 499 | `"        calls.append((url, kwargs))"` | — |
| [SRC-F725E90B2A-L000500](../../tests/test_web_agent.py#L500) | 500 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L000501](../../tests/test_web_agent.py#L501) | 501 | `""` | — |
| [SRC-F725E90B2A-L000502](../../tests/test_web_agent.py#L502) | 502 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000503](../../tests/test_web_agent.py#L503) | 503 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000504](../../tests/test_web_agent.py#L504) | 504 | `"        \"سيارة كهربائية\", [\"x\"]"` | — |
| [SRC-F725E90B2A-L000505](../../tests/test_web_agent.py#L505) | 505 | `"    )"` | — |
| [SRC-F725E90B2A-L000506](../../tests/test_web_agent.py#L506) | 506 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000507](../../tests/test_web_agent.py#L507) | 507 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L000508](../../tests/test_web_agent.py#L508) | 508 | `"    assert results[0][\"provider\"] == \"x_official_api\""` | — |
| [SRC-F725E90B2A-L000509](../../tests/test_web_agent.py#L509) | 509 | `"    assert results[0][\"url\"] == \"https://x.com/driver/status/1840000000000000000\""` | — |
| [SRC-F725E90B2A-L000510](../../tests/test_web_agent.py#L510) | 510 | `"    assert calls[0][1][\"headers\"][\"Authorization\"] == \"Bearer test-token\""` | — |
| [SRC-F725E90B2A-L000511](../../tests/test_web_agent.py#L511) | 511 | `""` | — |
| [SRC-F725E90B2A-L000512](../../tests/test_web_agent.py#L512) | 512 | `""` | — |
| [SRC-F725E90B2A-L000513](../../tests/test_web_agent.py#L513) | 513 | `""` | — |
| [SRC-F725E90B2A-L000514](../../tests/test_web_agent.py#L514) | 514 | `"def test_instagram_graph_api_returns_only_public_hashtag_media(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000515](../../tests/test_web_agent.py#L515) | 515 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000516](../../tests/test_web_agent.py#L516) | 516 | `""` | — |
| [SRC-F725E90B2A-L000517](../../tests/test_web_agent.py#L517) | 517 | `"    monkeypatch.setenv(\"INSTAGRAM_USER_ID\", \"ig-user-123\")"` | — |
| [SRC-F725E90B2A-L000518](../../tests/test_web_agent.py#L518) | 518 | `"    monkeypatch.setenv(\"INSTAGRAM_ACCESS_TOKEN\", \"test-ig-token\")"` | — |
| [SRC-F725E90B2A-L000519](../../tests/test_web_agent.py#L519) | 519 | `"    monkeypatch.setenv(\"META_GRAPH_VERSION\", \"v25.0\")"` | — |
| [SRC-F725E90B2A-L000520](../../tests/test_web_agent.py#L520) | 520 | `""` | — |
| [SRC-F725E90B2A-L000521](../../tests/test_web_agent.py#L521) | 521 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000522](../../tests/test_web_agent.py#L522) | 522 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000523](../../tests/test_web_agent.py#L523) | 523 | `""` | — |
| [SRC-F725E90B2A-L000524](../../tests/test_web_agent.py#L524) | 524 | `"        def __init__(self, payload):"` | — |
| [SRC-F725E90B2A-L000525](../../tests/test_web_agent.py#L525) | 525 | `"            self.payload = payload"` | — |
| [SRC-F725E90B2A-L000526](../../tests/test_web_agent.py#L526) | 526 | `""` | — |
| [SRC-F725E90B2A-L000527](../../tests/test_web_agent.py#L527) | 527 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000528](../../tests/test_web_agent.py#L528) | 528 | `"            return self.payload"` | — |
| [SRC-F725E90B2A-L000529](../../tests/test_web_agent.py#L529) | 529 | `""` | — |
| [SRC-F725E90B2A-L000530](../../tests/test_web_agent.py#L530) | 530 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000531](../../tests/test_web_agent.py#L531) | 531 | `""` | — |
| [SRC-F725E90B2A-L000532](../../tests/test_web_agent.py#L532) | 532 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000533](../../tests/test_web_agent.py#L533) | 533 | `"        calls.append((url, kwargs))"` | — |
| [SRC-F725E90B2A-L000534](../../tests/test_web_agent.py#L534) | 534 | `"        if url.endswith(\"/ig_hashtag_search\"):"` | — |
| [SRC-F725E90B2A-L000535](../../tests/test_web_agent.py#L535) | 535 | `"            return FakeResponse({\"data\": [{\"id\": \"tag-7\", \"name\": \"cars\"}]})"` | — |
| [SRC-F725E90B2A-L000536](../../tests/test_web_agent.py#L536) | 536 | `"        if url.endswith(\"/tag-7/recent_media\"):"` | — |
| [SRC-F725E90B2A-L000537](../../tests/test_web_agent.py#L537) | 537 | `"            return FakeResponse({\"data\": [{"` | — |
| [SRC-F725E90B2A-L000538](../../tests/test_web_agent.py#L538) | 538 | `"                \"permalink\": \"https://www.instagram.com/p/ABC123/\","` | — |
| [SRC-F725E90B2A-L000539](../../tests/test_web_agent.py#L539) | 539 | `"                \"caption\": \"Owner shared an electric car review\","` | — |
| [SRC-F725E90B2A-L000540](../../tests/test_web_agent.py#L540) | 540 | `"                \"media_type\": \"IMAGE\","` | — |
| [SRC-F725E90B2A-L000541](../../tests/test_web_agent.py#L541) | 541 | `"                \"timestamp\": \"2026-10-12T10:00:00+0000\","` | — |
| [SRC-F725E90B2A-L000542](../../tests/test_web_agent.py#L542) | 542 | `"                \"like_count\": 17,"` | — |
| [SRC-F725E90B2A-L000543](../../tests/test_web_agent.py#L543) | 543 | `"                \"comments_count\": 4,"` | — |
| [SRC-F725E90B2A-L000544](../../tests/test_web_agent.py#L544) | 544 | `"            }]})"` | — |
| [SRC-F725E90B2A-L000545](../../tests/test_web_agent.py#L545) | 545 | `"        raise AssertionError(f\"Unexpected URL {url}\")"` | — |
| [SRC-F725E90B2A-L000546](../../tests/test_web_agent.py#L546) | 546 | `""` | — |
| [SRC-F725E90B2A-L000547](../../tests/test_web_agent.py#L547) | 547 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000548](../../tests/test_web_agent.py#L548) | 548 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000549](../../tests/test_web_agent.py#L549) | 549 | `"        \"Instagram #cars\", [\"instagram\"]"` | — |
| [SRC-F725E90B2A-L000550](../../tests/test_web_agent.py#L550) | 550 | `"    )"` | — |
| [SRC-F725E90B2A-L000551](../../tests/test_web_agent.py#L551) | 551 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000552](../../tests/test_web_agent.py#L552) | 552 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L000553](../../tests/test_web_agent.py#L553) | 553 | `"    assert results[0][\"provider\"] == \"instagram_graph_api\""` | — |
| [SRC-F725E90B2A-L000554](../../tests/test_web_agent.py#L554) | 554 | `"    assert results[0][\"url\"] == \"https://www.instagram.com/p/ABC123/\""` | — |
| [SRC-F725E90B2A-L000555](../../tests/test_web_agent.py#L555) | 555 | `"    assert \"likes=17\" in results[0][\"snippet\"]"` | — |
| [SRC-F725E90B2A-L000556](../../tests/test_web_agent.py#L556) | 556 | `"    assert calls[0][1][\"params\"][\"q\"] == \"cars\""` | — |
| [SRC-F725E90B2A-L000557](../../tests/test_web_agent.py#L557) | 557 | `"    assert calls[0][1][\"params\"][\"access_token\"] == \"test-ig-token\""` | — |
| [SRC-F725E90B2A-L000558](../../tests/test_web_agent.py#L558) | 558 | `"    assert \"test-ig-token\" not in str(results)"` | — |
| [SRC-F725E90B2A-L000559](../../tests/test_web_agent.py#L559) | 559 | `""` | — |
| [SRC-F725E90B2A-L000560](../../tests/test_web_agent.py#L560) | 560 | `""` | — |
| [SRC-F725E90B2A-L000561](../../tests/test_web_agent.py#L561) | 561 | `"def test_instagram_api_not_configured_uses_honest_fallback_warning(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000562](../../tests/test_web_agent.py#L562) | 562 | `"    monkeypatch.delenv(\"INSTAGRAM_USER_ID\", raising=False)"` | — |
| [SRC-F725E90B2A-L000563](../../tests/test_web_agent.py#L563) | 563 | `"    monkeypatch.delenv(\"INSTAGRAM_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-F725E90B2A-L000564](../../tests/test_web_agent.py#L564) | 564 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000565](../../tests/test_web_agent.py#L565) | 565 | `"        \"تجارب عامة على Instagram\", [\"instagram\"]"` | — |
| [SRC-F725E90B2A-L000566](../../tests/test_web_agent.py#L566) | 566 | `"    )"` | — |
| [SRC-F725E90B2A-L000567](../../tests/test_web_agent.py#L567) | 567 | `"    assert results == []"` | — |
| [SRC-F725E90B2A-L000568](../../tests/test_web_agent.py#L568) | 568 | `"    assert any(\"indexed public Instagram\" in warning for warning in warnings)"` | — |
| [SRC-F725E90B2A-L000569](../../tests/test_web_agent.py#L569) | 569 | `""` | — |
| [SRC-F725E90B2A-L000570](../../tests/test_web_agent.py#L570) | 570 | `""` | — |
| [SRC-F725E90B2A-L000571](../../tests/test_web_agent.py#L571) | 571 | `"def test_facebook_pages_api_reads_only_operator_configured_pages(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000572](../../tests/test_web_agent.py#L572) | 572 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000573](../../tests/test_web_agent.py#L573) | 573 | `""` | — |
| [SRC-F725E90B2A-L000574](../../tests/test_web_agent.py#L574) | 574 | `"    monkeypatch.setenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"test-page-token\")"` | — |
| [SRC-F725E90B2A-L000575](../../tests/test_web_agent.py#L575) | 575 | `"    monkeypatch.setenv(\"FACEBOOK_PAGE_IDS\", \"page-1,page-2\")"` | — |
| [SRC-F725E90B2A-L000576](../../tests/test_web_agent.py#L576) | 576 | `""` | — |
| [SRC-F725E90B2A-L000577](../../tests/test_web_agent.py#L577) | 577 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000578](../../tests/test_web_agent.py#L578) | 578 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000579](../../tests/test_web_agent.py#L579) | 579 | `""` | — |
| [SRC-F725E90B2A-L000580](../../tests/test_web_agent.py#L580) | 580 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000581](../../tests/test_web_agent.py#L581) | 581 | `"            return {\"data\": [{"` | — |
| [SRC-F725E90B2A-L000582](../../tests/test_web_agent.py#L582) | 582 | `"                \"message\": \"Electric car owners looking for charging advice\","` | — |
| [SRC-F725E90B2A-L000583](../../tests/test_web_agent.py#L583) | 583 | `"                \"permalink_url\": \"https://www.facebook.com/example/posts/123\","` | — |
| [SRC-F725E90B2A-L000584](../../tests/test_web_agent.py#L584) | 584 | `"                \"created_time\": \"2026-10-12T12:00:00+0000\","` | — |
| [SRC-F725E90B2A-L000585](../../tests/test_web_agent.py#L585) | 585 | `"                \"comments\": {\"data\": ["` | — |
| [SRC-F725E90B2A-L000586](../../tests/test_web_agent.py#L586) | 586 | `"                    {\"message\": \"What is the current price?\", \"like_count\": 3}"` | — |
| [SRC-F725E90B2A-L000587](../../tests/test_web_agent.py#L587) | 587 | `"                ]},"` | — |
| [SRC-F725E90B2A-L000588](../../tests/test_web_agent.py#L588) | 588 | `"            }]}"` | — |
| [SRC-F725E90B2A-L000589](../../tests/test_web_agent.py#L589) | 589 | `""` | — |
| [SRC-F725E90B2A-L000590](../../tests/test_web_agent.py#L590) | 590 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000591](../../tests/test_web_agent.py#L591) | 591 | `""` | — |
| [SRC-F725E90B2A-L000592](../../tests/test_web_agent.py#L592) | 592 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000593](../../tests/test_web_agent.py#L593) | 593 | `"        calls.append((url, kwargs))"` | — |
| [SRC-F725E90B2A-L000594](../../tests/test_web_agent.py#L594) | 594 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L000595](../../tests/test_web_agent.py#L595) | 595 | `""` | — |
| [SRC-F725E90B2A-L000596](../../tests/test_web_agent.py#L596) | 596 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000597](../../tests/test_web_agent.py#L597) | 597 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000598](../../tests/test_web_agent.py#L598) | 598 | `"        \"electric car\", [\"facebook\"]"` | — |
| [SRC-F725E90B2A-L000599](../../tests/test_web_agent.py#L599) | 599 | `"    )"` | — |
| [SRC-F725E90B2A-L000600](../../tests/test_web_agent.py#L600) | 600 | `"    assert len(results) == 2  # one matching post for each explicitly configured page"` | — |
| [SRC-F725E90B2A-L000601](../../tests/test_web_agent.py#L601) | 601 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000602](../../tests/test_web_agent.py#L602) | 602 | `"    assert all(item[\"provider\"] == \"facebook_pages_api\" for item in results)"` | — |
| [SRC-F725E90B2A-L000603](../../tests/test_web_agent.py#L603) | 603 | `"    assert all(\"Electric car owners\" in item[\"snippet\"] for item in results)"` | — |
| [SRC-F725E90B2A-L000604](../../tests/test_web_agent.py#L604) | 604 | `"    assert len(calls) == 2"` | — |
| [SRC-F725E90B2A-L000605](../../tests/test_web_agent.py#L605) | 605 | `"    assert all(\"Bearer test-page-token\" == call[1][\"headers\"][\"Authorization\"] for call in calls)"` | — |
| [SRC-F725E90B2A-L000606](../../tests/test_web_agent.py#L606) | 606 | `""` | — |
| [SRC-F725E90B2A-L000607](../../tests/test_web_agent.py#L607) | 607 | `""` | — |
| [SRC-F725E90B2A-L000608](../../tests/test_web_agent.py#L608) | 608 | `"def test_reddit_oauth_api_is_preferred_when_credentials_are_configured(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000609](../../tests/test_web_agent.py#L609) | 609 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000610](../../tests/test_web_agent.py#L610) | 610 | `""` | — |
| [SRC-F725E90B2A-L000611](../../tests/test_web_agent.py#L611) | 611 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_ID\", \"client-test\")"` | — |
| [SRC-F725E90B2A-L000612](../../tests/test_web_agent.py#L612) | 612 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_SECRET\", \"secret-test\")"` | — |
| [SRC-F725E90B2A-L000613](../../tests/test_web_agent.py#L613) | 613 | `"    monkeypatch.setenv(\"REDDIT_USER_AGENT\", \"test:omarai:0.1\")"` | — |
| [SRC-F725E90B2A-L000614](../../tests/test_web_agent.py#L614) | 614 | `""` | — |
| [SRC-F725E90B2A-L000615](../../tests/test_web_agent.py#L615) | 615 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000616](../../tests/test_web_agent.py#L616) | 616 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000617](../../tests/test_web_agent.py#L617) | 617 | `""` | — |
| [SRC-F725E90B2A-L000618](../../tests/test_web_agent.py#L618) | 618 | `"        def __init__(self, payload):"` | — |
| [SRC-F725E90B2A-L000619](../../tests/test_web_agent.py#L619) | 619 | `"            self.payload = payload"` | — |
| [SRC-F725E90B2A-L000620](../../tests/test_web_agent.py#L620) | 620 | `""` | — |
| [SRC-F725E90B2A-L000621](../../tests/test_web_agent.py#L621) | 621 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000622](../../tests/test_web_agent.py#L622) | 622 | `"            return self.payload"` | — |
| [SRC-F725E90B2A-L000623](../../tests/test_web_agent.py#L623) | 623 | `""` | — |
| [SRC-F725E90B2A-L000624](../../tests/test_web_agent.py#L624) | 624 | `"        @property"` | — |
| [SRC-F725E90B2A-L000625](../../tests/test_web_agent.py#L625) | 625 | `"        def content(self):"` | — |
| [SRC-F725E90B2A-L000626](../../tests/test_web_agent.py#L626) | 626 | `"            import json"` | — |
| [SRC-F725E90B2A-L000627](../../tests/test_web_agent.py#L627) | 627 | `"            return json.dumps(self.payload).encode()"` | — |
| [SRC-F725E90B2A-L000628](../../tests/test_web_agent.py#L628) | 628 | `""` | — |
| [SRC-F725E90B2A-L000629](../../tests/test_web_agent.py#L629) | 629 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000630](../../tests/test_web_agent.py#L630) | 630 | `""` | — |
| [SRC-F725E90B2A-L000631](../../tests/test_web_agent.py#L631) | 631 | `"    def fake_post(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000632](../../tests/test_web_agent.py#L632) | 632 | `"        calls.append((\"POST\", url, kwargs))"` | — |
| [SRC-F725E90B2A-L000633](../../tests/test_web_agent.py#L633) | 633 | `"        return FakeResponse({\"access_token\": \"test-reddit-access-token\"})"` | — |
| [SRC-F725E90B2A-L000634](../../tests/test_web_agent.py#L634) | 634 | `""` | — |
| [SRC-F725E90B2A-L000635](../../tests/test_web_agent.py#L635) | 635 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000636](../../tests/test_web_agent.py#L636) | 636 | `"        calls.append((\"GET\", url, kwargs))"` | — |
| [SRC-F725E90B2A-L000637](../../tests/test_web_agent.py#L637) | 637 | `"        return FakeResponse({\"data\": {\"children\": [{"` | — |
| [SRC-F725E90B2A-L000638](../../tests/test_web_agent.py#L638) | 638 | `"            \"data\": {"` | — |
| [SRC-F725E90B2A-L000639](../../tests/test_web_agent.py#L639) | 639 | `"                \"title\": \"Electric vehicle owner discussion\","` | — |
| [SRC-F725E90B2A-L000640](../../tests/test_web_agent.py#L640) | 640 | `"                \"permalink\": \"/r/cars/comments/example/post/\","` | — |
| [SRC-F725E90B2A-L000641](../../tests/test_web_agent.py#L641) | 641 | `"                \"selftext\": \"Owners discuss battery range.\","` | — |
| [SRC-F725E90B2A-L000642](../../tests/test_web_agent.py#L642) | 642 | `"                \"created_utc\": 1791800000,"` | — |
| [SRC-F725E90B2A-L000643](../../tests/test_web_agent.py#L643) | 643 | `"                \"score\": 25,"` | — |
| [SRC-F725E90B2A-L000644](../../tests/test_web_agent.py#L644) | 644 | `"                \"num_comments\": 8,"` | — |
| [SRC-F725E90B2A-L000645](../../tests/test_web_agent.py#L645) | 645 | `"            }"` | — |
| [SRC-F725E90B2A-L000646](../../tests/test_web_agent.py#L646) | 646 | `"        }]}})"` | — |
| [SRC-F725E90B2A-L000647](../../tests/test_web_agent.py#L647) | 647 | `""` | — |
| [SRC-F725E90B2A-L000648](../../tests/test_web_agent.py#L648) | 648 | `"    monkeypatch.setattr(httpx, \"post\", fake_post)"` | — |
| [SRC-F725E90B2A-L000649](../../tests/test_web_agent.py#L649) | 649 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000650](../../tests/test_web_agent.py#L650) | 650 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000651](../../tests/test_web_agent.py#L651) | 651 | `"        \"electric vehicles\", [\"reddit\"]"` | — |
| [SRC-F725E90B2A-L000652](../../tests/test_web_agent.py#L652) | 652 | `"    )"` | — |
| [SRC-F725E90B2A-L000653](../../tests/test_web_agent.py#L653) | 653 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L000654](../../tests/test_web_agent.py#L654) | 654 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000655](../../tests/test_web_agent.py#L655) | 655 | `"    assert results[0][\"provider\"] == \"reddit_oauth_api\""` | — |
| [SRC-F725E90B2A-L000656](../../tests/test_web_agent.py#L656) | 656 | `"    assert results[0][\"url\"] == \"https://www.reddit.com/r/cars/comments/example/post/\""` | — |
| [SRC-F725E90B2A-L000657](../../tests/test_web_agent.py#L657) | 657 | `"    assert \"score=25\" in results[0][\"snippet\"]"` | — |
| [SRC-F725E90B2A-L000658](../../tests/test_web_agent.py#L658) | 658 | `"    assert len([call for call in calls if call[0] == \"POST\"]) == 1"` | — |
| [SRC-F725E90B2A-L000659](../../tests/test_web_agent.py#L659) | 659 | `"    assert any(\"oauth.reddit.com/search\" in call[1] for call in calls if call[0] == \"GET\")"` | — |
| [SRC-F725E90B2A-L000660](../../tests/test_web_agent.py#L660) | 660 | `"    assert \"test-reddit-access-token\" not in str(results)"` | — |
| [SRC-F725E90B2A-L000661](../../tests/test_web_agent.py#L661) | 661 | `""` | — |
| [SRC-F725E90B2A-L000662](../../tests/test_web_agent.py#L662) | 662 | `""` | — |
| [SRC-F725E90B2A-L000663](../../tests/test_web_agent.py#L663) | 663 | `""` | — |
| [SRC-F725E90B2A-L000664](../../tests/test_web_agent.py#L664) | 664 | `"def test_role_models_are_explicit_and_have_a_fallback(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000665](../../tests/test_web_agent.py#L665) | 665 | `"    for name in ("` | — |
| [SRC-F725E90B2A-L000666](../../tests/test_web_agent.py#L666) | 666 | `"        \"OMARAI_LLM_MODEL\","` | — |
| [SRC-F725E90B2A-L000667](../../tests/test_web_agent.py#L667) | 667 | `"        \"OMARAI_PLANNER_MODEL\","` | — |
| [SRC-F725E90B2A-L000668](../../tests/test_web_agent.py#L668) | 668 | `"        \"OMARAI_ANSWER_MODEL\","` | — |
| [SRC-F725E90B2A-L000669](../../tests/test_web_agent.py#L669) | 669 | `"        \"OMARAI_REVIEW_MODEL\","` | — |
| [SRC-F725E90B2A-L000670](../../tests/test_web_agent.py#L670) | 670 | `"        \"OMARAI_LLM_FALLBACK_MODEL\","` | — |
| [SRC-F725E90B2A-L000671](../../tests/test_web_agent.py#L671) | 671 | `"    ):"` | — |
| [SRC-F725E90B2A-L000672](../../tests/test_web_agent.py#L672) | 672 | `"        monkeypatch.delenv(name, raising=False)"` | — |
| [SRC-F725E90B2A-L000673](../../tests/test_web_agent.py#L673) | 673 | `""` | — |
| [SRC-F725E90B2A-L000674](../../tests/test_web_agent.py#L674) | 674 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000675](../../tests/test_web_agent.py#L675) | 675 | `"    assert agent.planner_model == \"nvidia/nemotron-3-ultra-550b-a55b:free\""` | — |
| [SRC-F725E90B2A-L000676](../../tests/test_web_agent.py#L676) | 676 | `"    assert agent.answer_model == \"google/gemma-4-31b-it:free\""` | — |
| [SRC-F725E90B2A-L000677](../../tests/test_web_agent.py#L677) | 677 | `"    assert agent.review_model == agent.answer_model"` | — |
