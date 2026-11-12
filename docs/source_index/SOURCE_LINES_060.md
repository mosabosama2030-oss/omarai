# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **060**
- سجلات الأسطر: **800**
- النطاق: SRC-AFEDC2645A-L000008 إلى SRC-AFEDC2645A-L000807
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-AFEDC2645A — [tests/test_task_understanding.py](../../tests/test_task_understanding.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-AFEDC2645A-L000008](../../tests/test_task_understanding.py#L8) | 8 | `"@pytest.mark.parametrize("` | — |
| [SRC-AFEDC2645A-L000009](../../tests/test_task_understanding.py#L9) | 9 | `"    (\"question\", \"family\"),"` | — |
| [SRC-AFEDC2645A-L000010](../../tests/test_task_understanding.py#L10) | 10 | `"    ["` | — |
| [SRC-AFEDC2645A-L000011](../../tests/test_task_understanding.py#L11) | 11 | `"        (\"ابحث عن الموقع الرسمي لوزارة الاتصالات في مصر\", \"official_site_lookup\"),"` | — |
| [SRC-AFEDC2645A-L000012](../../tests/test_task_understanding.py#L12) | 12 | `"        (\"مواعيد عمل مكتب الجوازات اليوم في العباسية\", \"current_information\"),"` | — |
| [SRC-AFEDC2645A-L000013](../../tests/test_task_understanding.py#L13) | 13 | `"        (\"قارن نيسان صني 2022 وهيونداي أكسنت من حيث السعر والصيانة\", \"compare\"),"` | — |
| [SRC-AFEDC2645A-L000014](../../tests/test_task_understanding.py#L14) | 14 | `"        (\"عايز تجارب ملاك BYD Dolphin في مصر\", \"social_opinions\"),"` | — |
| [SRC-AFEDC2645A-L000015](../../tests/test_task_understanding.py#L15) | 15 | `"        (\"ازاي أصلح خطأ الشبكة في لوحة إنذار الحريق؟\", \"troubleshoot\"),"` | — |
| [SRC-AFEDC2645A-L000016](../../tests/test_task_understanding.py#L16) | 16 | `"        (\"اشرح خطوات صيانة حساس الدخان\", \"how_to\"),"` | — |
| [SRC-AFEDC2645A-L000017](../../tests/test_task_understanding.py#L17) | 17 | `"        (\"لخص الصفحة https://example.com/article\", \"summarize\"),"` | — |
| [SRC-AFEDC2645A-L000018](../../tests/test_task_understanding.py#L18) | 18 | `"        (\"ابحث عن مشترين يريدون شراء شقة في القاهرة\", \"lead_generation\"),"` | — |
| [SRC-AFEDC2645A-L000019](../../tests/test_task_understanding.py#L19) | 19 | `"        (\"رشح لي أفضل سيارة بميزانية أقل من 500000 جنيه\", \"recommendation\"),"` | — |
| [SRC-AFEDC2645A-L000020](../../tests/test_task_understanding.py#L20) | 20 | `"        (\"ما معنى نظام الإنذار المعنون؟\", \"explain_or_define\"),"` | — |
| [SRC-AFEDC2645A-L000021](../../tests/test_task_understanding.py#L21) | 21 | `"    ],"` | — |
| [SRC-AFEDC2645A-L000022](../../tests/test_task_understanding.py#L22) | 22 | `")"` | — |
| [SRC-AFEDC2645A-L000023](../../tests/test_task_understanding.py#L23) | 23 | `"def test_task_family_covers_diverse_natural_language_patterns(question, family):"` | — |
| [SRC-AFEDC2645A-L000024](../../tests/test_task_understanding.py#L24) | 24 | `"    spec = build_task_spec(question, mode=\"auto\", intent_route=\"WEB_SIMPLE\")"` | — |
| [SRC-AFEDC2645A-L000025](../../tests/test_task_understanding.py#L25) | 25 | `"    assert spec[\"task_family\"] == family"` | — |
| [SRC-AFEDC2645A-L000026](../../tests/test_task_understanding.py#L26) | 26 | `"    assert spec[\"classification_is_probability\"] is False"` | — |
| [SRC-AFEDC2645A-L000027](../../tests/test_task_understanding.py#L27) | 27 | `"    assert spec[\"decision_checks\"]"` | — |
| [SRC-AFEDC2645A-L000028](../../tests/test_task_understanding.py#L28) | 28 | `""` | — |
| [SRC-AFEDC2645A-L000029](../../tests/test_task_understanding.py#L29) | 29 | `""` | — |
| [SRC-AFEDC2645A-L000030](../../tests/test_task_understanding.py#L30) | 30 | `"def test_lead_generation_task_separates_demand_signal_from_product_fit():"` | — |
| [SRC-AFEDC2645A-L000031](../../tests/test_task_understanding.py#L31) | 31 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000032](../../tests/test_task_understanding.py#L32) | 32 | `"        \"ابحث عن مشترين يريدون شراء نظام إنذار حريق صناعي في مصر\","` | — |
| [SRC-AFEDC2645A-L000033](../../tests/test_task_understanding.py#L33) | 33 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000034](../../tests/test_task_understanding.py#L34) | 34 | `"        intent_route=\"LEAD_GENERATION\","` | — |
| [SRC-AFEDC2645A-L000035](../../tests/test_task_understanding.py#L35) | 35 | `"    )"` | — |
| [SRC-AFEDC2645A-L000036](../../tests/test_task_understanding.py#L36) | 36 | `"    requirements = set(spec[\"evidence_requirements\"])"` | — |
| [SRC-AFEDC2645A-L000037](../../tests/test_task_understanding.py#L37) | 37 | `"    strategies = set(spec[\"query_strategies\"])"` | — |
| [SRC-AFEDC2645A-L000038](../../tests/test_task_understanding.py#L38) | 38 | `"    assert \"classify_public_demand_signal_by_type\" in requirements"` | — |
| [SRC-AFEDC2645A-L000039](../../tests/test_task_understanding.py#L39) | 39 | `"    assert \"distinguish_direct_purchase_from_rfq_and_stated_need\" in requirements"` | — |
| [SRC-AFEDC2645A-L000040](../../tests/test_task_understanding.py#L40) | 40 | `"    assert \"keep_product_fit_unassessed_until_separately_supported\" in requirements"` | — |
| [SRC-AFEDC2645A-L000041](../../tests/test_task_understanding.py#L41) | 41 | `"    assert \"do_not_treat_product_mention_or_icp_match_as_demand\" in requirements"` | — |
| [SRC-AFEDC2645A-L000042](../../tests/test_task_understanding.py#L42) | 42 | `"    assert \"product_anchored_rfq\" in strategies"` | — |
| [SRC-AFEDC2645A-L000043](../../tests/test_task_understanding.py#L43) | 43 | `"    assert \"product_anchored_stated_need\" in strategies"` | — |
| [SRC-AFEDC2645A-L000044](../../tests/test_task_understanding.py#L44) | 44 | `""` | — |
| [SRC-AFEDC2645A-L000045](../../tests/test_task_understanding.py#L45) | 45 | `""` | — |
| [SRC-AFEDC2645A-L000046](../../tests/test_task_understanding.py#L46) | 46 | `"def test_lead_generation_query_matrix_preserves_only_buyer_language_queries():"` | — |
| [SRC-AFEDC2645A-L000047](../../tests/test_task_understanding.py#L47) | 47 | `"    # Structured product profiles can arrive without buyer wording in the original prompt."` | — |
| [SRC-AFEDC2645A-L000048](../../tests/test_task_understanding.py#L48) | 48 | `"    question = \"نظام إنذار حريق صناعي في مصر\""` | — |
| [SRC-AFEDC2645A-L000049](../../tests/test_task_understanding.py#L49) | 49 | `"    buyer_queries = ["` | — |
| [SRC-AFEDC2645A-L000050](../../tests/test_task_understanding.py#L50) | 50 | `"        '\"مطلوب شراء\" \"نظام إنذار حريق صناعي\" مصر',"` | — |
| [SRC-AFEDC2645A-L000051](../../tests/test_task_understanding.py#L51) | 51 | `"        '\"طلب عرض سعر\" \"نظام إنذار حريق صناعي\" مصر',"` | — |
| [SRC-AFEDC2645A-L000052](../../tests/test_task_understanding.py#L52) | 52 | `"        '\"looking to buy\" \"industrial fire alarm system\" Egypt',"` | — |
| [SRC-AFEDC2645A-L000053](../../tests/test_task_understanding.py#L53) | 53 | `"    ]"` | — |
| [SRC-AFEDC2645A-L000054](../../tests/test_task_understanding.py#L54) | 54 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000055](../../tests/test_task_understanding.py#L55) | 55 | `"        question,"` | — |
| [SRC-AFEDC2645A-L000056](../../tests/test_task_understanding.py#L56) | 56 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000057](../../tests/test_task_understanding.py#L57) | 57 | `"        intent_route=\"LEAD_GENERATION\","` | — |
| [SRC-AFEDC2645A-L000058](../../tests/test_task_understanding.py#L58) | 58 | `"    )"` | — |
| [SRC-AFEDC2645A-L000059](../../tests/test_task_understanding.py#L59) | 59 | `""` | — |
| [SRC-AFEDC2645A-L000060](../../tests/test_task_understanding.py#L60) | 60 | `"    rows = build_query_strategy_matrix(question, spec, buyer_queries, limit=8)"` | — |
| [SRC-AFEDC2645A-L000061](../../tests/test_task_understanding.py#L61) | 61 | `""` | — |
| [SRC-AFEDC2645A-L000062](../../tests/test_task_understanding.py#L62) | 62 | `"    assert spec[\"task_family\"] == \"lead_generation\""` | — |
| [SRC-AFEDC2645A-L000063](../../tests/test_task_understanding.py#L63) | 63 | `"    assert [row[\"query\"] for row in rows] == buyer_queries"` | — |
| [SRC-AFEDC2645A-L000064](../../tests/test_task_understanding.py#L64) | 64 | `"    assert all(row[\"strategy\"] == \"buyer_intent\" for row in rows)"` | — |
| [SRC-AFEDC2645A-L000065](../../tests/test_task_understanding.py#L65) | 65 | `"    assert all(row[\"rationale\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000066](../../tests/test_task_understanding.py#L66) | 66 | `"    assert not any("` | — |
| [SRC-AFEDC2645A-L000067](../../tests/test_task_understanding.py#L67) | 67 | `"        marker in row[\"query\"].casefold()"` | — |
| [SRC-AFEDC2645A-L000068](../../tests/test_task_understanding.py#L68) | 68 | `"        for row in rows"` | — |
| [SRC-AFEDC2645A-L000069](../../tests/test_task_understanding.py#L69) | 69 | `"        for marker in (\"risk\", \"risks\", \"report\", \"reports\", \"مخاطر\", \"تقارير\")"` | — |
| [SRC-AFEDC2645A-L000070](../../tests/test_task_understanding.py#L70) | 70 | `"    )"` | — |
| [SRC-AFEDC2645A-L000071](../../tests/test_task_understanding.py#L71) | 71 | `""` | — |
| [SRC-AFEDC2645A-L000072](../../tests/test_task_understanding.py#L72) | 72 | `""` | — |
| [SRC-AFEDC2645A-L000073](../../tests/test_task_understanding.py#L73) | 73 | `"def test_discovery_strategy_has_no_hardcoded_property_only_query_angles():"` | — |
| [SRC-AFEDC2645A-L000074](../../tests/test_task_understanding.py#L74) | 74 | `"    question = \"ابحث عن شقق للبيع في العاصمة الإدارية\""` | — |
| [SRC-AFEDC2645A-L000075](../../tests/test_task_understanding.py#L75) | 75 | `"    spec = build_task_spec(question, mode=\"deep\", intent_route=\"WEB_DEEP\")"` | — |
| [SRC-AFEDC2645A-L000076](../../tests/test_task_understanding.py#L76) | 76 | `""` | — |
| [SRC-AFEDC2645A-L000077](../../tests/test_task_understanding.py#L77) | 77 | `"    rows = build_query_strategy_matrix(question, spec, [question], limit=8)"` | — |
| [SRC-AFEDC2645A-L000078](../../tests/test_task_understanding.py#L78) | 78 | `"    queries = [row[\"query\"] for row in rows]"` | — |
| [SRC-AFEDC2645A-L000079](../../tests/test_task_understanding.py#L79) | 79 | `""` | — |
| [SRC-AFEDC2645A-L000080](../../tests/test_task_understanding.py#L80) | 80 | `"    assert not any("` | — |
| [SRC-AFEDC2645A-L000081](../../tests/test_task_understanding.py#L81) | 81 | `"        marker in query"` | — |
| [SRC-AFEDC2645A-L000082](../../tests/test_task_understanding.py#L82) | 82 | `"        for query in queries"` | — |
| [SRC-AFEDC2645A-L000083](../../tests/test_task_understanding.py#L83) | 83 | `"        for marker in (\"إعلانات عقارية\", \"متوسط أسعار السوق للمتر\", \"أسعار البيع الفعلية\")"` | — |
| [SRC-AFEDC2645A-L000084](../../tests/test_task_understanding.py#L84) | 84 | `"    )"` | — |
| [SRC-AFEDC2645A-L000085](../../tests/test_task_understanding.py#L85) | 85 | `""` | — |
| [SRC-AFEDC2645A-L000086](../../tests/test_task_understanding.py#L86) | 86 | `""` | — |
| [SRC-AFEDC2645A-L000087](../../tests/test_task_understanding.py#L87) | 87 | `"def test_task_spec_preserves_only_explicit_constraints():"` | — |
| [SRC-AFEDC2645A-L000088](../../tests/test_task_understanding.py#L88) | 88 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000089](../../tests/test_task_understanding.py#L89) | 89 | `"        \"قارن نيسان صني 2022 مع BYD Dolphin في مصر، بميزانية أقل من 400 ألف جنيه\","` | — |
| [SRC-AFEDC2645A-L000090](../../tests/test_task_understanding.py#L90) | 90 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000091](../../tests/test_task_understanding.py#L91) | 91 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000092](../../tests/test_task_understanding.py#L92) | 92 | `"    )"` | — |
| [SRC-AFEDC2645A-L000093](../../tests/test_task_understanding.py#L93) | 93 | `"    constraints = spec[\"constraints\"]"` | — |
| [SRC-AFEDC2645A-L000094](../../tests/test_task_understanding.py#L94) | 94 | `"    assert \"2022\" in constraints[\"explicit_years\"]"` | — |
| [SRC-AFEDC2645A-L000095](../../tests/test_task_understanding.py#L95) | 95 | `"    assert \"مصر\" in constraints[\"explicit_locations\"]"` | — |
| [SRC-AFEDC2645A-L000096](../../tests/test_task_understanding.py#L96) | 96 | `"    assert constraints[\"explicit_budgets\"]"` | — |
| [SRC-AFEDC2645A-L000097](../../tests/test_task_understanding.py#L97) | 97 | `"    assert constraints[\"language_profile\"] in {\"ar\", \"mixed\"}"` | — |
| [SRC-AFEDC2645A-L000098](../../tests/test_task_understanding.py#L98) | 98 | `""` | — |
| [SRC-AFEDC2645A-L000099](../../tests/test_task_understanding.py#L99) | 99 | `""` | — |
| [SRC-AFEDC2645A-L000100](../../tests/test_task_understanding.py#L100) | 100 | `"def test_latest_mode_requires_current_evidence_for_stateful_facts():"` | — |
| [SRC-AFEDC2645A-L000101](../../tests/test_task_understanding.py#L101) | 101 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000102](../../tests/test_task_understanding.py#L102) | 102 | `"        \"مواعيد عمل مكتب الجوازات اليوم\","` | — |
| [SRC-AFEDC2645A-L000103](../../tests/test_task_understanding.py#L103) | 103 | `"        mode=\"latest\","` | — |
| [SRC-AFEDC2645A-L000104](../../tests/test_task_understanding.py#L104) | 104 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000105](../../tests/test_task_understanding.py#L105) | 105 | `"    )"` | — |
| [SRC-AFEDC2645A-L000106](../../tests/test_task_understanding.py#L106) | 106 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is True"` | — |
| [SRC-AFEDC2645A-L000107](../../tests/test_task_understanding.py#L107) | 107 | `"    assert \"page_text_successfully_read\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000108](../../tests/test_task_understanding.py#L108) | 108 | `"    assert \"date_check\" in spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000109](../../tests/test_task_understanding.py#L109) | 109 | `""` | — |
| [SRC-AFEDC2645A-L000110](../../tests/test_task_understanding.py#L110) | 110 | `""` | — |
| [SRC-AFEDC2645A-L000111](../../tests/test_task_understanding.py#L111) | 111 | `"def test_official_site_navigation_is_not_misclassified_as_current_news():"` | — |
| [SRC-AFEDC2645A-L000112](../../tests/test_task_understanding.py#L112) | 112 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000113](../../tests/test_task_understanding.py#L113) | 113 | `"        \"ابحث عن الموقع الرسمي لوزارة الاتصالات في مصر\","` | — |
| [SRC-AFEDC2645A-L000114](../../tests/test_task_understanding.py#L114) | 114 | `"        mode=\"latest\","` | — |
| [SRC-AFEDC2645A-L000115](../../tests/test_task_understanding.py#L115) | 115 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000116](../../tests/test_task_understanding.py#L116) | 116 | `"    )"` | — |
| [SRC-AFEDC2645A-L000117](../../tests/test_task_understanding.py#L117) | 117 | `"    assert spec[\"task_family\"] == \"official_site_lookup\""` | — |
| [SRC-AFEDC2645A-L000118](../../tests/test_task_understanding.py#L118) | 118 | `"    assert spec[\"constraints\"][\"official_site_required\"] is True"` | — |
| [SRC-AFEDC2645A-L000119](../../tests/test_task_understanding.py#L119) | 119 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is False"` | — |
| [SRC-AFEDC2645A-L000120](../../tests/test_task_understanding.py#L120) | 120 | `""` | — |
| [SRC-AFEDC2645A-L000121](../../tests/test_task_understanding.py#L121) | 121 | `""` | — |
| [SRC-AFEDC2645A-L000122](../../tests/test_task_understanding.py#L122) | 122 | `"def test_social_request_separates_experience_from_truth_verification():"` | — |
| [SRC-AFEDC2645A-L000123](../../tests/test_task_understanding.py#L123) | 123 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000124](../../tests/test_task_understanding.py#L124) | 124 | `"        \"أريد آراء وتجارب ملاك نيسان صني 2022 في مصر\","` | — |
| [SRC-AFEDC2645A-L000125](../../tests/test_task_understanding.py#L125) | 125 | `"        mode=\"social\","` | — |
| [SRC-AFEDC2645A-L000126](../../tests/test_task_understanding.py#L126) | 126 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000127](../../tests/test_task_understanding.py#L127) | 127 | `"    )"` | — |
| [SRC-AFEDC2645A-L000128](../../tests/test_task_understanding.py#L128) | 128 | `"    assert spec[\"constraints\"][\"social_evidence_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000129](../../tests/test_task_understanding.py#L129) | 129 | `"    assert \"heuristic_classification_is_not_identity_or_truth_verification\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000130](../../tests/test_task_understanding.py#L130) | 130 | `"    assert \"personal_experience\" in spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000131](../../tests/test_task_understanding.py#L131) | 131 | `""` | — |
| [SRC-AFEDC2645A-L000132](../../tests/test_task_understanding.py#L132) | 132 | `""` | — |
| [SRC-AFEDC2645A-L000133](../../tests/test_task_understanding.py#L133) | 133 | `"def test_ambiguous_followup_is_not_reported_as_a_confident_interpretation():"` | — |
| [SRC-AFEDC2645A-L000134](../../tests/test_task_understanding.py#L134) | 134 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000135](../../tests/test_task_understanding.py#L135) | 135 | `"        \"كام سعرها؟\","` | — |
| [SRC-AFEDC2645A-L000136](../../tests/test_task_understanding.py#L136) | 136 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000137](../../tests/test_task_understanding.py#L137) | 137 | `"        intent_route=\"CLARIFY\","` | — |
| [SRC-AFEDC2645A-L000138](../../tests/test_task_understanding.py#L138) | 138 | `"        dialogue_context={\"needs_clarification\": True},"` | — |
| [SRC-AFEDC2645A-L000139](../../tests/test_task_understanding.py#L139) | 139 | `"    )"` | — |
| [SRC-AFEDC2645A-L000140](../../tests/test_task_understanding.py#L140) | 140 | `"    assert spec[\"task_family\"] == \"ambiguous_or_incomplete\""` | — |
| [SRC-AFEDC2645A-L000141](../../tests/test_task_understanding.py#L141) | 141 | `"    assert spec[\"ambiguity_status\"] == \"needs_clarification\""` | — |
| [SRC-AFEDC2645A-L000142](../../tests/test_task_understanding.py#L142) | 142 | `""` | — |
| [SRC-AFEDC2645A-L000143](../../tests/test_task_understanding.py#L143) | 143 | `""` | — |
| [SRC-AFEDC2645A-L000144](../../tests/test_task_understanding.py#L144) | 144 | `"def test_query_strategy_matrix_is_bounded_deduplicated_and_topic_anchored():"` | — |
| [SRC-AFEDC2645A-L000145](../../tests/test_task_understanding.py#L145) | 145 | `"    question = \"قارن السيارات الكهربائية في مصر من حيث السعر والضمان\""` | — |
| [SRC-AFEDC2645A-L000146](../../tests/test_task_understanding.py#L146) | 146 | `"    spec = build_task_spec(question, mode=\"deep\", intent_route=\"WEB_DEEP\")"` | — |
| [SRC-AFEDC2645A-L000147](../../tests/test_task_understanding.py#L147) | 147 | `"    existing = [\"السيارات الكهربائية في مصر\"] + ["` | — |
| [SRC-AFEDC2645A-L000148](../../tests/test_task_understanding.py#L148) | 148 | `"        f\"السيارات الكهربائية في مصر بديل عام {i}\" for i in range(1, 9)"` | — |
| [SRC-AFEDC2645A-L000149](../../tests/test_task_understanding.py#L149) | 149 | `"    ]"` | — |
| [SRC-AFEDC2645A-L000150](../../tests/test_task_understanding.py#L150) | 150 | `"    rows = build_query_strategy_matrix(question, spec, existing, limit=6)"` | — |
| [SRC-AFEDC2645A-L000151](../../tests/test_task_understanding.py#L151) | 151 | `"    queries = [row[\"query\"] for row in rows]"` | — |
| [SRC-AFEDC2645A-L000152](../../tests/test_task_understanding.py#L152) | 152 | `"    assert 1 <= len(queries) <= 6"` | — |
| [SRC-AFEDC2645A-L000153](../../tests/test_task_understanding.py#L153) | 153 | `"    assert len({query.casefold() for query in queries}) == len(queries)"` | — |
| [SRC-AFEDC2645A-L000154](../../tests/test_task_understanding.py#L154) | 154 | `"    assert all(\"السيارات\" in query for query in queries)"` | — |
| [SRC-AFEDC2645A-L000155](../../tests/test_task_understanding.py#L155) | 155 | `"    assert any(row[\"strategy\"] == \"explicit_criterion\" for row in rows)"` | — |
| [SRC-AFEDC2645A-L000156](../../tests/test_task_understanding.py#L156) | 156 | `"    assert any(row[\"strategy\"] == \"primary_specification\" for row in rows)"` | — |
| [SRC-AFEDC2645A-L000157](../../tests/test_task_understanding.py#L157) | 157 | `"    assert sum(row[\"strategy\"] == \"planner_alternative\" for row in rows) <= 1"` | — |
| [SRC-AFEDC2645A-L000158](../../tests/test_task_understanding.py#L158) | 158 | `"    assert all(row[\"rationale\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000159](../../tests/test_task_understanding.py#L159) | 159 | `""` | — |
| [SRC-AFEDC2645A-L000160](../../tests/test_task_understanding.py#L160) | 160 | `"def test_strategy_matrix_does_not_create_generic_queries_without_topic():"` | — |
| [SRC-AFEDC2645A-L000161](../../tests/test_task_understanding.py#L161) | 161 | `"    spec = build_task_spec(\"قارنهم\", mode=\"deep\", intent_route=\"CLARIFY\")"` | — |
| [SRC-AFEDC2645A-L000162](../../tests/test_task_understanding.py#L162) | 162 | `"    rows = build_query_strategy_matrix(\"قارنهم\", spec, [], limit=8)"` | — |
| [SRC-AFEDC2645A-L000163](../../tests/test_task_understanding.py#L163) | 163 | `"    assert rows == []"` | — |
| [SRC-AFEDC2645A-L000164](../../tests/test_task_understanding.py#L164) | 164 | `""` | — |
| [SRC-AFEDC2645A-L000165](../../tests/test_task_understanding.py#L165) | 165 | `""` | — |
| [SRC-AFEDC2645A-L000166](../../tests/test_task_understanding.py#L166) | 166 | `"def test_mixed_language_is_supported_and_urls_are_explicit_constraints():"` | — |
| [SRC-AFEDC2645A-L000167](../../tests/test_task_understanding.py#L167) | 167 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000168](../../tests/test_task_understanding.py#L168) | 168 | `"        \"Compare Nissan Sunny 2022 with BYD Dolphin في مصر https://example.com/specs\","` | — |
| [SRC-AFEDC2645A-L000169](../../tests/test_task_understanding.py#L169) | 169 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000170](../../tests/test_task_understanding.py#L170) | 170 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000171](../../tests/test_task_understanding.py#L171) | 171 | `"    )"` | — |
| [SRC-AFEDC2645A-L000172](../../tests/test_task_understanding.py#L172) | 172 | `"    assert spec[\"constraints\"][\"language_profile\"] == \"mixed\""` | — |
| [SRC-AFEDC2645A-L000173](../../tests/test_task_understanding.py#L173) | 173 | `"    assert spec[\"constraints\"][\"explicit_urls\"] == [\"https://example.com/specs\"]"` | — |
| [SRC-AFEDC2645A-L000174](../../tests/test_task_understanding.py#L174) | 174 | `"    assert \"2022\" in spec[\"constraints\"][\"explicit_years\"]"` | — |
| [SRC-AFEDC2645A-L000175](../../tests/test_task_understanding.py#L175) | 175 | `""` | — |
| [SRC-AFEDC2645A-L000176](../../tests/test_task_understanding.py#L176) | 176 | `""` | — |
| [SRC-AFEDC2645A-L000177](../../tests/test_task_understanding.py#L177) | 177 | `"def test_task_spec_validator_does_not_accept_untrusted_arbitrary_objects():"` | — |
| [SRC-AFEDC2645A-L000178](../../tests/test_task_understanding.py#L178) | 178 | `"    from agents.task_understanding import validate_task_spec"` | — |
| [SRC-AFEDC2645A-L000179](../../tests/test_task_understanding.py#L179) | 179 | `""` | — |
| [SRC-AFEDC2645A-L000180](../../tests/test_task_understanding.py#L180) | 180 | `"    invalid = validate_task_spec({\"schema\": \"wrong\", \"tool_requirements\": [\"delete files\"]})"` | — |
| [SRC-AFEDC2645A-L000181](../../tests/test_task_understanding.py#L181) | 181 | `"    assert invalid[\"status\"] == \"not_available\""` | — |
| [SRC-AFEDC2645A-L000182](../../tests/test_task_understanding.py#L182) | 182 | `""` | — |
| [SRC-AFEDC2645A-L000183](../../tests/test_task_understanding.py#L183) | 183 | `""` | — |
| [SRC-AFEDC2645A-L000184](../../tests/test_task_understanding.py#L184) | 184 | `"def test_compound_task_keeps_current_social_and_comparison_requirements_together():"` | — |
| [SRC-AFEDC2645A-L000185](../../tests/test_task_understanding.py#L185) | 185 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000186](../../tests/test_task_understanding.py#L186) | 186 | `"        \"قارن تجارب ملاك نيسان صني 2022 في مصر اليوم من حيث السعر والأعطال\","` | — |
| [SRC-AFEDC2645A-L000187](../../tests/test_task_understanding.py#L187) | 187 | `"        mode=\"social\","` | — |
| [SRC-AFEDC2645A-L000188](../../tests/test_task_understanding.py#L188) | 188 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000189](../../tests/test_task_understanding.py#L189) | 189 | `"    )"` | — |
| [SRC-AFEDC2645A-L000190](../../tests/test_task_understanding.py#L190) | 190 | `"    assert spec[\"task_family\"] in {\"social_opinions\", \"compare\"}"` | — |
| [SRC-AFEDC2645A-L000191](../../tests/test_task_understanding.py#L191) | 191 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is True"` | — |
| [SRC-AFEDC2645A-L000192](../../tests/test_task_understanding.py#L192) | 192 | `"    assert spec[\"constraints\"][\"social_evidence_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000193](../../tests/test_task_understanding.py#L193) | 193 | `"    assert \"publication_or_update_date\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000194](../../tests/test_task_understanding.py#L194) | 194 | `"    assert \"preserve_explicit_comparison_criteria\" in spec[\"evidence_requirements\"] or \"preserve_each_explicit_comparison_criterion\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000195](../../tests/test_task_understanding.py#L195) | 195 | `"    assert \"personal_experience\" in spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000196](../../tests/test_task_understanding.py#L196) | 196 | `"    assert \"date_check\" in spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000197](../../tests/test_task_understanding.py#L197) | 197 | `""` | — |
| [SRC-AFEDC2645A-L000198](../../tests/test_task_understanding.py#L198) | 198 | `""` | — |
| [SRC-AFEDC2645A-L000199](../../tests/test_task_understanding.py#L199) | 199 | `"def test_alarm_word_does_not_trigger_current_information_pattern():"` | — |
| [SRC-AFEDC2645A-L000200](../../tests/test_task_understanding.py#L200) | 200 | `"    spec = build_task_spec(\"ما معنى نظام الإنذار المعنون؟\", mode=\"auto\", intent_route=\"MODEL_ONLY\")"` | — |
| [SRC-AFEDC2645A-L000201](../../tests/test_task_understanding.py#L201) | 201 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is False"` | — |
| [SRC-AFEDC2645A-L000202](../../tests/test_task_understanding.py#L202) | 202 | `"    assert spec[\"task_family\"] == \"explain_or_define\""` | — |
| [SRC-AFEDC2645A-L000203](../../tests/test_task_understanding.py#L203) | 203 | `""` | — |
| [SRC-AFEDC2645A-L000204](../../tests/test_task_understanding.py#L204) | 204 | `""` | — |
| [SRC-AFEDC2645A-L000205](../../tests/test_task_understanding.py#L205) | 205 | `"def test_clarification_route_does_not_claim_search_or_generation_tools():"` | — |
| [SRC-AFEDC2645A-L000206](../../tests/test_task_understanding.py#L206) | 206 | `"    spec = build_task_spec(\"كام سعرها؟\", mode=\"deep\", intent_route=\"CLARIFY\")"` | — |
| [SRC-AFEDC2645A-L000207](../../tests/test_task_understanding.py#L207) | 207 | `"    assert spec[\"ambiguity_status\"] == \"needs_clarification\""` | — |
| [SRC-AFEDC2645A-L000208](../../tests/test_task_understanding.py#L208) | 208 | `"    assert \"web_search\" not in spec[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000209](../../tests/test_task_understanding.py#L209) | 209 | `"    assert \"page_fetch\" not in spec[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000210](../../tests/test_task_understanding.py#L210) | 210 | `"    assert \"language_model_generation_if_configured\" not in spec[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000211](../../tests/test_task_understanding.py#L211) | 211 | `""` | — |
| [SRC-AFEDC2645A-L000212](../../tests/test_task_understanding.py#L212) | 212 | `""` | — |
| [SRC-AFEDC2645A-L000213](../../tests/test_task_understanding.py#L213) | 213 | `"def test_summary_text_and_page_link_require_different_tools():"` | — |
| [SRC-AFEDC2645A-L000214](../../tests/test_task_understanding.py#L214) | 214 | `"    pasted = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000215](../../tests/test_task_understanding.py#L215) | 215 | `"        \"لخص النص التالي: يتناول النص صيانة أجهزة الإنذار وإجراء الاختبار الدوري.\","` | — |
| [SRC-AFEDC2645A-L000216](../../tests/test_task_understanding.py#L216) | 216 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000217](../../tests/test_task_understanding.py#L217) | 217 | `"        intent_route=\"MODEL_ONLY\","` | — |
| [SRC-AFEDC2645A-L000218](../../tests/test_task_understanding.py#L218) | 218 | `"    )"` | — |
| [SRC-AFEDC2645A-L000219](../../tests/test_task_understanding.py#L219) | 219 | `"    assert pasted[\"constraints\"][\"inline_text_supplied_for_summary\"] is True"` | — |
| [SRC-AFEDC2645A-L000220](../../tests/test_task_understanding.py#L220) | 220 | `"    assert \"page_fetch\" not in pasted[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000221](../../tests/test_task_understanding.py#L221) | 221 | `"    assert \"web_search\" not in pasted[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000222](../../tests/test_task_understanding.py#L222) | 222 | `"    linked = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000223](../../tests/test_task_understanding.py#L223) | 223 | `"        \"لخص الصفحة https://example.com/manual\","` | — |
| [SRC-AFEDC2645A-L000224](../../tests/test_task_understanding.py#L224) | 224 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000225](../../tests/test_task_understanding.py#L225) | 225 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000226](../../tests/test_task_understanding.py#L226) | 226 | `"    )"` | — |
| [SRC-AFEDC2645A-L000227](../../tests/test_task_understanding.py#L227) | 227 | `"    assert \"page_fetch\" in linked[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000228](../../tests/test_task_understanding.py#L228) | 228 | `"    assert \"web_search\" in linked[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000229](../../tests/test_task_understanding.py#L229) | 229 | `""` | — |
| [SRC-AFEDC2645A-L000230](../../tests/test_task_understanding.py#L230) | 230 | `""` | — |
| [SRC-AFEDC2645A-L000231](../../tests/test_task_understanding.py#L231) | 231 | `"def test_output_format_preferences_are_preserved_separately_from_intent():"` | — |
| [SRC-AFEDC2645A-L000232](../../tests/test_task_understanding.py#L232) | 232 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000233](../../tests/test_task_understanding.py#L233) | 233 | `"        \"قارن الخيارين في جدول مع أمثلة وبالتفصيل وعلى شكل نقاط\","` | — |
| [SRC-AFEDC2645A-L000234](../../tests/test_task_understanding.py#L234) | 234 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000235](../../tests/test_task_understanding.py#L235) | 235 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000236](../../tests/test_task_understanding.py#L236) | 236 | `"    )"` | — |
| [SRC-AFEDC2645A-L000237](../../tests/test_task_understanding.py#L237) | 237 | `"    preferences = spec[\"output_preferences\"]"` | — |
| [SRC-AFEDC2645A-L000238](../../tests/test_task_understanding.py#L238) | 238 | `"    assert preferences[\"table_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000239](../../tests/test_task_understanding.py#L239) | 239 | `"    assert preferences[\"examples_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000240](../../tests/test_task_understanding.py#L240) | 240 | `"    assert preferences[\"detailed\"] is True"` | — |
| [SRC-AFEDC2645A-L000241](../../tests/test_task_understanding.py#L241) | 241 | `"    assert preferences[\"bullets_or_checklist_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000242](../../tests/test_task_understanding.py#L242) | 242 | `""` | — |
| [SRC-AFEDC2645A-L000243](../../tests/test_task_understanding.py#L243) | 243 | `""` | — |
| [SRC-AFEDC2645A-L000244](../../tests/test_task_understanding.py#L244) | 244 | `"def test_location_matching_avoids_partial_english_word_collision():"` | — |
| [SRC-AFEDC2645A-L000245](../../tests/test_task_understanding.py#L245) | 245 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000246](../../tests/test_task_understanding.py#L246) | 246 | `"        \"Explain Egyptology as an academic field\","` | — |
| [SRC-AFEDC2645A-L000247](../../tests/test_task_understanding.py#L247) | 247 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000248](../../tests/test_task_understanding.py#L248) | 248 | `"        intent_route=\"MODEL_ONLY\","` | — |
| [SRC-AFEDC2645A-L000249](../../tests/test_task_understanding.py#L249) | 249 | `"    )"` | — |
| [SRC-AFEDC2645A-L000250](../../tests/test_task_understanding.py#L250) | 250 | `"    assert \"مصر\" not in spec[\"constraints\"][\"explicit_locations\"]"` | — |
| [SRC-AFEDC2645A-L000251](../../tests/test_task_understanding.py#L251) | 251 | `""` | — |
| [SRC-AFEDC2645A-L000252](../../tests/test_task_understanding.py#L252) | 252 | `""` | — |
| [SRC-AFEDC2645A-L000253](../../tests/test_task_understanding.py#L253) | 253 | `"def test_source_policies_keep_orthogonal_research_constraints():"` | — |
| [SRC-AFEDC2645A-L000254](../../tests/test_task_understanding.py#L254) | 254 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000255](../../tests/test_task_understanding.py#L255) | 255 | `"        \"قارن تجارب ملاك السيارات الكهربائية في مصر اليوم من حيث السعر والاعتمادية\","` | — |
| [SRC-AFEDC2645A-L000256](../../tests/test_task_understanding.py#L256) | 256 | `"        mode=\"social\","` | — |
| [SRC-AFEDC2645A-L000257](../../tests/test_task_understanding.py#L257) | 257 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000258](../../tests/test_task_understanding.py#L258) | 258 | `"    )"` | — |
| [SRC-AFEDC2645A-L000259](../../tests/test_task_understanding.py#L259) | 259 | `"    policies = spec[\"constraints\"][\"source_policies\"]"` | — |
| [SRC-AFEDC2645A-L000260](../../tests/test_task_understanding.py#L260) | 260 | `"    assert \"current_read_page\" in policies"` | — |
| [SRC-AFEDC2645A-L000261](../../tests/test_task_understanding.py#L261) | 261 | `"    assert \"public_social_content\" in policies"` | — |
| [SRC-AFEDC2645A-L000262](../../tests/test_task_understanding.py#L262) | 262 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is True"` | — |
| [SRC-AFEDC2645A-L000263](../../tests/test_task_understanding.py#L263) | 263 | `"    assert spec[\"constraints\"][\"social_evidence_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000264](../../tests/test_task_understanding.py#L264) | 264 | `"    assert \"publication_or_update_date\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000265](../../tests/test_task_understanding.py#L265) | 265 | `"    assert \"heuristic_classification_is_not_identity_or_truth_verification\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000266](../../tests/test_task_understanding.py#L266) | 266 | `""` | — |
| [SRC-AFEDC2645A-L000267](../../tests/test_task_understanding.py#L267) | 267 | `""` | — |
| [SRC-AFEDC2645A-L000268](../../tests/test_task_understanding.py#L268) | 268 | `"def test_official_site_request_without_a_target_marks_required_input():"` | — |
| [SRC-AFEDC2645A-L000269](../../tests/test_task_understanding.py#L269) | 269 | `"    spec = build_task_spec(\"هات الموقع الرسمي\", mode=\"auto\", intent_route=\"WEB_SIMPLE\")"` | — |
| [SRC-AFEDC2645A-L000270](../../tests/test_task_understanding.py#L270) | 270 | `"    assert spec[\"task_family\"] == \"official_site_lookup\""` | — |
| [SRC-AFEDC2645A-L000271](../../tests/test_task_understanding.py#L271) | 271 | `"    assert \"official_destination_target_entity\" in spec[\"missing_required_inputs\"]"` | — |
| [SRC-AFEDC2645A-L000272](../../tests/test_task_understanding.py#L272) | 272 | `"    assert spec[\"requires_clarification\"] is True"` | — |
| [SRC-AFEDC2645A-L000273](../../tests/test_task_understanding.py#L273) | 273 | `""` | — |
| [SRC-AFEDC2645A-L000274](../../tests/test_task_understanding.py#L274) | 274 | `""` | — |
| [SRC-AFEDC2645A-L000275](../../tests/test_task_understanding.py#L275) | 275 | `"def test_official_site_request_with_a_named_target_does_not_require_subject_clarification():"` | — |
| [SRC-AFEDC2645A-L000276](../../tests/test_task_understanding.py#L276) | 276 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000277](../../tests/test_task_understanding.py#L277) | 277 | `"        \"هات الموقع الرسمي لوزارة الاتصالات في مصر\","` | — |
| [SRC-AFEDC2645A-L000278](../../tests/test_task_understanding.py#L278) | 278 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000279](../../tests/test_task_understanding.py#L279) | 279 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000280](../../tests/test_task_understanding.py#L280) | 280 | `"    )"` | — |
| [SRC-AFEDC2645A-L000281](../../tests/test_task_understanding.py#L281) | 281 | `"    assert \"official_destination_target_entity\" not in spec[\"missing_required_inputs\"]"` | — |
| [SRC-AFEDC2645A-L000282](../../tests/test_task_understanding.py#L282) | 282 | `"    assert spec[\"constraints\"][\"official_destination_required\"] is True"` | — |
| [SRC-AFEDC2645A-L000283](../../tests/test_task_understanding.py#L283) | 283 | `""` | — |
| [SRC-AFEDC2645A-L000284](../../tests/test_task_understanding.py#L284) | 284 | `""` | — |
| [SRC-AFEDC2645A-L000285](../../tests/test_task_understanding.py#L285) | 285 | `"def test_summary_without_url_or_text_marks_required_input():"` | — |
| [SRC-AFEDC2645A-L000286](../../tests/test_task_understanding.py#L286) | 286 | `"    spec = build_task_spec(\"لخص\", mode=\"auto\", intent_route=\"MODEL_ONLY\")"` | — |
| [SRC-AFEDC2645A-L000287](../../tests/test_task_understanding.py#L287) | 287 | `"    assert \"summary_source_url_or_pasted_text\" in spec[\"missing_required_inputs\"]"` | — |
| [SRC-AFEDC2645A-L000288](../../tests/test_task_understanding.py#L288) | 288 | `"    assert spec[\"requires_clarification\"] is True"` | — |
| [SRC-AFEDC2645A-L000289](../../tests/test_task_understanding.py#L289) | 289 | `""` | — |
| [SRC-AFEDC2645A-L000290](../../tests/test_task_understanding.py#L290) | 290 | `""` | — |
| [SRC-AFEDC2645A-L000291](../../tests/test_task_understanding.py#L291) | 291 | `"def test_output_preferences_do_not_count_as_competing_intent_hypotheses():"` | — |
| [SRC-AFEDC2645A-L000292](../../tests/test_task_understanding.py#L292) | 292 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000293](../../tests/test_task_understanding.py#L293) | 293 | `"        \"قارن الخيارين في جدول مع أمثلة وبالتفصيل\","` | — |
| [SRC-AFEDC2645A-L000294](../../tests/test_task_understanding.py#L294) | 294 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000295](../../tests/test_task_understanding.py#L295) | 295 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000296](../../tests/test_task_understanding.py#L296) | 296 | `"    )"` | — |
| [SRC-AFEDC2645A-L000297](../../tests/test_task_understanding.py#L297) | 297 | `"    families = {row[\"family\"] for row in spec[\"hypothesis_interpretations\"]}"` | — |
| [SRC-AFEDC2645A-L000298](../../tests/test_task_understanding.py#L298) | 298 | `"    assert \"compare\" in families"` | — |
| [SRC-AFEDC2645A-L000299](../../tests/test_task_understanding.py#L299) | 299 | `"    assert not any(family.startswith(\"output_\") for family in families)"` | — |
| [SRC-AFEDC2645A-L000300](../../tests/test_task_understanding.py#L300) | 300 | `"    assert spec[\"ambiguity_status\"] == \"no_strong_lexical_conflict_detected\""` | — |
| [SRC-AFEDC2645A-L000301](../../tests/test_task_understanding.py#L301) | 301 | `""` | — |
| [SRC-AFEDC2645A-L000302](../../tests/test_task_understanding.py#L302) | 302 | `""` | — |
| [SRC-AFEDC2645A-L000303](../../tests/test_task_understanding.py#L303) | 303 | `"@pytest.mark.parametrize("` | — |
| [SRC-AFEDC2645A-L000304](../../tests/test_task_understanding.py#L304) | 304 | `"    (\"question\", \"family\"),"` | — |
| [SRC-AFEDC2645A-L000305](../../tests/test_task_understanding.py#L305) | 305 | `"    ["` | — |
| [SRC-AFEDC2645A-L000306](../../tests/test_task_understanding.py#L306) | 306 | `"        (\"ترجم هذا النص إلى الإنجليزية: Hello world\", \"translation\"),"` | — |
| [SRC-AFEDC2645A-L000307](../../tests/test_task_understanding.py#L307) | 307 | `"        (\"اكتب بريد إلكتروني للعميل بنبرة مهنية\", \"writing_or_editing\"),"` | — |
| [SRC-AFEDC2645A-L000308](../../tests/test_task_understanding.py#L308) | 308 | `"        (\"احسب 17 بالمئة من 500\", \"calculation\"),"` | — |
| [SRC-AFEDC2645A-L000309](../../tests/test_task_understanding.py#L309) | 309 | `"        (\"حلل البيانات في ملف CSV وحدد القيم الناقصة\", \"data_analysis\"),"` | — |
| [SRC-AFEDC2645A-L000310](../../tests/test_task_understanding.py#L310) | 310 | `"        (\"راجع كود Python الذي يعرض stack trace\", \"coding_or_technical_design\"),"` | — |
| [SRC-AFEDC2645A-L000311](../../tests/test_task_understanding.py#L311) | 311 | `"        (\"ضع خطة عمل لافتتاح متجر خلال شهر\", \"planning\"),"` | — |
| [SRC-AFEDC2645A-L000312](../../tests/test_task_understanding.py#L312) | 312 | `"        (\"ما أعراض الإنفلونزا؟\", \"medical_information\"),"` | — |
| [SRC-AFEDC2645A-L000313](../../tests/test_task_understanding.py#L313) | 313 | `"        (\"ما شروط العقد وفق القانون المصري؟\", \"legal_information\"),"` | — |
| [SRC-AFEDC2645A-L000314](../../tests/test_task_understanding.py#L314) | 314 | `"        (\"اكتب قصة قصيرة عن رحلة خيالية\", \"creative_generation\"),"` | — |
| [SRC-AFEDC2645A-L000315](../../tests/test_task_understanding.py#L315) | 315 | `"    ],"` | — |
| [SRC-AFEDC2645A-L000316](../../tests/test_task_understanding.py#L316) | 316 | `")"` | — |
| [SRC-AFEDC2645A-L000317](../../tests/test_task_understanding.py#L317) | 317 | `"def test_extended_task_families_cover_non_search_and_specialized_requests(question, family):"` | — |
| [SRC-AFEDC2645A-L000318](../../tests/test_task_understanding.py#L318) | 318 | `"    spec = build_task_spec(question, mode=\"auto\", intent_route=\"MODEL_ONLY\")"` | — |
| [SRC-AFEDC2645A-L000319](../../tests/test_task_understanding.py#L319) | 319 | `"    assert spec[\"task_family\"] == family"` | — |
| [SRC-AFEDC2645A-L000320](../../tests/test_task_understanding.py#L320) | 320 | `"    assert spec[\"classification_is_probability\"] is False"` | — |
| [SRC-AFEDC2645A-L000321](../../tests/test_task_understanding.py#L321) | 321 | `"    assert spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000322](../../tests/test_task_understanding.py#L322) | 322 | `"    assert spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000323](../../tests/test_task_understanding.py#L323) | 323 | `""` | — |
| [SRC-AFEDC2645A-L000324](../../tests/test_task_understanding.py#L324) | 324 | `""` | — |
| [SRC-AFEDC2645A-L000325](../../tests/test_task_understanding.py#L325) | 325 | `"def test_health_and_legal_tasks_attach_domain_specific_caution():"` | — |
| [SRC-AFEDC2645A-L000326](../../tests/test_task_understanding.py#L326) | 326 | `"    health = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000327](../../tests/test_task_understanding.py#L327) | 327 | `"        \"ما أعراض الإنفلونزا اليوم؟\","` | — |
| [SRC-AFEDC2645A-L000328](../../tests/test_task_understanding.py#L328) | 328 | `"        mode=\"latest\","` | — |
| [SRC-AFEDC2645A-L000329](../../tests/test_task_understanding.py#L329) | 329 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000330](../../tests/test_task_understanding.py#L330) | 330 | `"    )"` | — |
| [SRC-AFEDC2645A-L000331](../../tests/test_task_understanding.py#L331) | 331 | `"    assert \"authoritative_health_content\" in health[\"constraints\"][\"source_policies\"]"` | — |
| [SRC-AFEDC2645A-L000332](../../tests/test_task_understanding.py#L332) | 332 | `"    assert \"distinguish_general_health_information_from_personal_diagnosis\" in health[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000333](../../tests/test_task_understanding.py#L333) | 333 | `"    assert \"page_text_successfully_read\" in health[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000334](../../tests/test_task_understanding.py#L334) | 334 | `""` | — |
| [SRC-AFEDC2645A-L000335](../../tests/test_task_understanding.py#L335) | 335 | `"    legal = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000336](../../tests/test_task_understanding.py#L336) | 336 | `"        \"ما نص القانون الحالي المنظم للإيجار في مصر؟\","` | — |
| [SRC-AFEDC2645A-L000337](../../tests/test_task_understanding.py#L337) | 337 | `"        mode=\"latest\","` | — |
| [SRC-AFEDC2645A-L000338](../../tests/test_task_understanding.py#L338) | 338 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000339](../../tests/test_task_understanding.py#L339) | 339 | `"    )"` | — |
| [SRC-AFEDC2645A-L000340](../../tests/test_task_understanding.py#L340) | 340 | `"    assert \"official_legal_text\" in legal[\"constraints\"][\"source_policies\"]"` | — |
| [SRC-AFEDC2645A-L000341](../../tests/test_task_understanding.py#L341) | 341 | `"    assert \"identify_jurisdiction_and_effective_date_if_relevant\" in legal[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000342](../../tests/test_task_understanding.py#L342) | 342 | `""` | — |
| [SRC-AFEDC2645A-L000343](../../tests/test_task_understanding.py#L343) | 343 | `""` | — |
| [SRC-AFEDC2645A-L000344](../../tests/test_task_understanding.py#L344) | 344 | `"def test_output_audience_and_delivery_preferences_are_distinct_fields():"` | — |
| [SRC-AFEDC2645A-L000345](../../tests/test_task_understanding.py#L345) | 345 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000346](../../tests/test_task_understanding.py#L346) | 346 | `"        \"اشرح الموضوع ببساطة مع مصادر وروابط مباشرة وبصيغة JSON\","` | — |
| [SRC-AFEDC2645A-L000347](../../tests/test_task_understanding.py#L347) | 347 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000348](../../tests/test_task_understanding.py#L348) | 348 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000349](../../tests/test_task_understanding.py#L349) | 349 | `"    )"` | — |
| [SRC-AFEDC2645A-L000350](../../tests/test_task_understanding.py#L350) | 350 | `"    preferences = spec[\"output_preferences\"]"` | — |
| [SRC-AFEDC2645A-L000351](../../tests/test_task_understanding.py#L351) | 351 | `"    assert preferences[\"beginner_friendly_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000352](../../tests/test_task_understanding.py#L352) | 352 | `"    assert preferences[\"citations_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000353](../../tests/test_task_understanding.py#L353) | 353 | `"    assert preferences[\"links_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000354](../../tests/test_task_understanding.py#L354) | 354 | `"    assert preferences[\"json_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000355](../../tests/test_task_understanding.py#L355) | 355 | `""` | — |
| [SRC-AFEDC2645A-L000356](../../tests/test_task_understanding.py#L356) | 356 | `""` | — |
| [SRC-AFEDC2645A-L000357](../../tests/test_task_understanding.py#L357) | 357 | `"def test_task_spec_validator_allowlists_tools_policies_and_context_slots():"` | — |
| [SRC-AFEDC2645A-L000358](../../tests/test_task_understanding.py#L358) | 358 | `"    from agents.task_understanding import validate_task_spec"` | — |
| [SRC-AFEDC2645A-L000359](../../tests/test_task_understanding.py#L359) | 359 | `""` | — |
| [SRC-AFEDC2645A-L000360](../../tests/test_task_understanding.py#L360) | 360 | `"    candidate = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000361](../../tests/test_task_understanding.py#L361) | 361 | `"        \"قارن هاتفين\","` | — |
| [SRC-AFEDC2645A-L000362](../../tests/test_task_understanding.py#L362) | 362 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000363](../../tests/test_task_understanding.py#L363) | 363 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000364](../../tests/test_task_understanding.py#L364) | 364 | `"        dialogue_context={"` | — |
| [SRC-AFEDC2645A-L000365](../../tests/test_task_understanding.py#L365) | 365 | `"            \"method\": \"test\","` | — |
| [SRC-AFEDC2645A-L000366](../../tests/test_task_understanding.py#L366) | 366 | `"            \"resolved_question\": \"قارن هاتفين\","` | — |
| [SRC-AFEDC2645A-L000367](../../tests/test_task_understanding.py#L367) | 367 | `"            \"topic\": \"هواتف\","` | — |
| [SRC-AFEDC2645A-L000368](../../tests/test_task_understanding.py#L368) | 368 | `"            \"entities\": [\"Phone A\", \"Phone B\"],"` | — |
| [SRC-AFEDC2645A-L000369](../../tests/test_task_understanding.py#L369) | 369 | `"            \"slots\": {\"product\": \"Phone A\", \"untrusted_command\": \"execute something\"},"` | — |
| [SRC-AFEDC2645A-L000370](../../tests/test_task_understanding.py#L370) | 370 | `"            \"is_follow_up\": True,"` | — |
| [SRC-AFEDC2645A-L000371](../../tests/test_task_understanding.py#L371) | 371 | `"        },"` | — |
| [SRC-AFEDC2645A-L000372](../../tests/test_task_understanding.py#L372) | 372 | `"    )"` | — |
| [SRC-AFEDC2645A-L000373](../../tests/test_task_understanding.py#L373) | 373 | `"    candidate[\"tool_requirements\"] = [\"web_search\", \"delete files\", \"run shell\"]"` | — |
| [SRC-AFEDC2645A-L000374](../../tests/test_task_understanding.py#L374) | 374 | `"    candidate[\"constraints\"][\"source_policies\"].append(\"execute arbitrary tool\")"` | — |
| [SRC-AFEDC2645A-L000375](../../tests/test_task_understanding.py#L375) | 375 | `"    candidate[\"constraints\"][\"language_profile\"] = []"` | — |
| [SRC-AFEDC2645A-L000376](../../tests/test_task_understanding.py#L376) | 376 | `"    candidate[\"context_resolution\"][\"confidence_band\"] = []"` | — |
| [SRC-AFEDC2645A-L000377](../../tests/test_task_understanding.py#L377) | 377 | `"    candidate[\"extra_unexpected_key\"] = \"must not survive\""` | — |
| [SRC-AFEDC2645A-L000378](../../tests/test_task_understanding.py#L378) | 378 | `"    safe = validate_task_spec(candidate)"` | — |
| [SRC-AFEDC2645A-L000379](../../tests/test_task_understanding.py#L379) | 379 | `""` | — |
| [SRC-AFEDC2645A-L000380](../../tests/test_task_understanding.py#L380) | 380 | `"    assert safe[\"tool_requirements\"] == [\"web_search\"]"` | — |
| [SRC-AFEDC2645A-L000381](../../tests/test_task_understanding.py#L381) | 381 | `"    assert safe[\"constraints\"][\"source_policies\"] == [\"task_relevant_sources\"]"` | — |
| [SRC-AFEDC2645A-L000382](../../tests/test_task_understanding.py#L382) | 382 | `"    assert safe[\"constraints\"][\"language_profile\"] == \"und\""` | — |
| [SRC-AFEDC2645A-L000383](../../tests/test_task_understanding.py#L383) | 383 | `"    assert \"untrusted_command\" not in safe[\"context_resolution\"][\"slots\"]"` | — |
| [SRC-AFEDC2645A-L000384](../../tests/test_task_understanding.py#L384) | 384 | `"    assert safe[\"context_resolution\"][\"confidence_band\"] == \"unassessed\""` | — |
| [SRC-AFEDC2645A-L000385](../../tests/test_task_understanding.py#L385) | 385 | `"    assert \"extra_unexpected_key\" not in safe"` | — |
| [SRC-AFEDC2645A-L000386](../../tests/test_task_understanding.py#L386) | 386 | `""` | — |
| [SRC-AFEDC2645A-L000387](../../tests/test_task_understanding.py#L387) | 387 | `""` | — |
| [SRC-AFEDC2645A-L000388](../../tests/test_task_understanding.py#L388) | 388 | `"def test_reasoning_playbook_combines_primary_task_and_orthogonal_constraints():"` | — |
| [SRC-AFEDC2645A-L000389](../../tests/test_task_understanding.py#L389) | 389 | `"    from agents.task_understanding import reasoning_guidance_for_task_spec"` | — |
| [SRC-AFEDC2645A-L000390](../../tests/test_task_understanding.py#L390) | 390 | `""` | — |
| [SRC-AFEDC2645A-L000391](../../tests/test_task_understanding.py#L391) | 391 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000392](../../tests/test_task_understanding.py#L392) | 392 | `"        \"قارن تجارب ملاك السيارات الكهربائية في مصر اليوم من حيث السعر والأمان والتوفر\","` | — |
| [SRC-AFEDC2645A-L000393](../../tests/test_task_understanding.py#L393) | 393 | `"        mode=\"latest\","` | — |
| [SRC-AFEDC2645A-L000394](../../tests/test_task_understanding.py#L394) | 394 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000395](../../tests/test_task_understanding.py#L395) | 395 | `"        dialogue_context={"` | — |
| [SRC-AFEDC2645A-L000396](../../tests/test_task_understanding.py#L396) | 396 | `"            \"is_follow_up\": True,"` | — |
| [SRC-AFEDC2645A-L000397](../../tests/test_task_understanding.py#L397) | 397 | `"            \"topic_shift\": False,"` | — |
| [SRC-AFEDC2645A-L000398](../../tests/test_task_understanding.py#L398) | 398 | `"            \"resolved_question\": \"قارن تجارب ملاك السيارات الكهربائية في مصر اليوم من حيث السعر والأمان والتوفر\","` | — |
| [SRC-AFEDC2645A-L000399](../../tests/test_task_understanding.py#L399) | 399 | `"            \"method\": \"test_context\","` | — |
| [SRC-AFEDC2645A-L000400](../../tests/test_task_understanding.py#L400) | 400 | `"        },"` | — |
| [SRC-AFEDC2645A-L000401](../../tests/test_task_understanding.py#L401) | 401 | `"    )"` | — |
| [SRC-AFEDC2645A-L000402](../../tests/test_task_understanding.py#L402) | 402 | `""` | — |
| [SRC-AFEDC2645A-L000403](../../tests/test_task_understanding.py#L403) | 403 | `"    ids = set(spec[\"reasoning_strategy_ids\"])"` | — |
| [SRC-AFEDC2645A-L000404](../../tests/test_task_understanding.py#L404) | 404 | `"    assert spec[\"task_family\"] in {\"social_opinions\", \"compare\"}"` | — |
| [SRC-AFEDC2645A-L000405](../../tests/test_task_understanding.py#L405) | 405 | `"    assert \"separate_facts_inferences_hypotheses\" in ids"` | — |
| [SRC-AFEDC2645A-L000406](../../tests/test_task_understanding.py#L406) | 406 | `"    assert \"bounded_stop_rule\" in ids"` | — |
| [SRC-AFEDC2645A-L000407](../../tests/test_task_understanding.py#L407) | 407 | `"    assert \"separate_event_and_publication_dates\" in ids"` | — |
| [SRC-AFEDC2645A-L000408](../../tests/test_task_understanding.py#L408) | 408 | `"    assert \"reject_stale_current_claims\" in ids"` | — |
| [SRC-AFEDC2645A-L000409](../../tests/test_task_understanding.py#L409) | 409 | `"    assert \"balance_social_evidence\" in ids"` | — |
| [SRC-AFEDC2645A-L000410](../../tests/test_task_understanding.py#L410) | 410 | `"    assert \"resolve_followup_slots\" in ids"` | — |
| [SRC-AFEDC2645A-L000411](../../tests/test_task_understanding.py#L411) | 411 | `"    assert \"decompose_explicit_criteria\" in ids"` | — |
| [SRC-AFEDC2645A-L000412](../../tests/test_task_understanding.py#L412) | 412 | `"    assert len(spec[\"decision_matrix\"]) == 6"` | — |
| [SRC-AFEDC2645A-L000413](../../tests/test_task_understanding.py#L413) | 413 | `""` | — |
| [SRC-AFEDC2645A-L000414](../../tests/test_task_understanding.py#L414) | 414 | `"    guidance = reasoning_guidance_for_task_spec(spec)"` | — |
| [SRC-AFEDC2645A-L000415](../../tests/test_task_understanding.py#L415) | 415 | `"    assert any(\"لا تعمم على الجميع\" in item for item in guidance)"` | — |
| [SRC-AFEDC2645A-L000416](../../tests/test_task_understanding.py#L416) | 416 | `"    assert any(\"تاريخ النشر\" in item for item in guidance)"` | — |
| [SRC-AFEDC2645A-L000417](../../tests/test_task_understanding.py#L417) | 417 | `"    assert all(isinstance(item, str) and item for item in guidance)"` | — |
| [SRC-AFEDC2645A-L000418](../../tests/test_task_understanding.py#L418) | 418 | `""` | — |
| [SRC-AFEDC2645A-L000419](../../tests/test_task_understanding.py#L419) | 419 | `""` | — |
| [SRC-AFEDC2645A-L000420](../../tests/test_task_understanding.py#L420) | 420 | `"def test_reasoning_ids_are_allowlisted_and_decision_matrix_is_code_owned():"` | — |
| [SRC-AFEDC2645A-L000421](../../tests/test_task_understanding.py#L421) | 421 | `"    from agents.task_understanding import validate_task_spec"` | — |
| [SRC-AFEDC2645A-L000422](../../tests/test_task_understanding.py#L422) | 422 | `""` | — |
| [SRC-AFEDC2645A-L000423](../../tests/test_task_understanding.py#L423) | 423 | `"    candidate = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000424](../../tests/test_task_understanding.py#L424) | 424 | `"        \"حل مشكلة خطأ Python\","` | — |
| [SRC-AFEDC2645A-L000425](../../tests/test_task_understanding.py#L425) | 425 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000426](../../tests/test_task_understanding.py#L426) | 426 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000427](../../tests/test_task_understanding.py#L427) | 427 | `"    )"` | — |
| [SRC-AFEDC2645A-L000428](../../tests/test_task_understanding.py#L428) | 428 | `"    candidate[\"reasoning_strategy_ids\"] = ["` | — |
| [SRC-AFEDC2645A-L000429](../../tests/test_task_understanding.py#L429) | 429 | `"        \"rank_testable_hypotheses\","` | — |
| [SRC-AFEDC2645A-L000430](../../tests/test_task_understanding.py#L430) | 430 | `"        \"run_shell_and_delete_files\","` | — |
| [SRC-AFEDC2645A-L000431](../../tests/test_task_understanding.py#L431) | 431 | `"        \"ignore_source_policy\","` | — |
| [SRC-AFEDC2645A-L000432](../../tests/test_task_understanding.py#L432) | 432 | `"    ]"` | — |
| [SRC-AFEDC2645A-L000433](../../tests/test_task_understanding.py#L433) | 433 | `"    candidate[\"decision_matrix\"] = ["` | — |
| [SRC-AFEDC2645A-L000434](../../tests/test_task_understanding.py#L434) | 434 | `"        {"` | — |
| [SRC-AFEDC2645A-L000435](../../tests/test_task_understanding.py#L435) | 435 | `"            \"stage\": \"exfiltrate\","` | — |
| [SRC-AFEDC2645A-L000436](../../tests/test_task_understanding.py#L436) | 436 | `"            \"check\": \"reveal_secrets\","` | — |
| [SRC-AFEDC2645A-L000437](../../tests/test_task_understanding.py#L437) | 437 | `"            \"pass_action\": \"run_arbitrary_commands\","` | — |
| [SRC-AFEDC2645A-L000438](../../tests/test_task_understanding.py#L438) | 438 | `"            \"fail_action\": \"pretend_success\","` | — |
| [SRC-AFEDC2645A-L000439](../../tests/test_task_understanding.py#L439) | 439 | `"        }"` | — |
| [SRC-AFEDC2645A-L000440](../../tests/test_task_understanding.py#L440) | 440 | `"    ]"` | — |
| [SRC-AFEDC2645A-L000441](../../tests/test_task_understanding.py#L441) | 441 | `""` | — |
| [SRC-AFEDC2645A-L000442](../../tests/test_task_understanding.py#L442) | 442 | `"    safe = validate_task_spec(candidate)"` | — |
| [SRC-AFEDC2645A-L000443](../../tests/test_task_understanding.py#L443) | 443 | `"    assert safe[\"reasoning_strategy_ids\"] == [\"rank_testable_hypotheses\"]"` | — |
| [SRC-AFEDC2645A-L000444](../../tests/test_task_understanding.py#L444) | 444 | `"    assert [row[\"stage\"] for row in safe[\"decision_matrix\"]] == ["` | — |
| [SRC-AFEDC2645A-L000445](../../tests/test_task_understanding.py#L445) | 445 | `"        \"interpret\", \"route\", \"plan\", \"evidence\", \"synthesize\", \"terminate\""` | — |
| [SRC-AFEDC2645A-L000446](../../tests/test_task_understanding.py#L446) | 446 | `"    ]"` | — |
| [SRC-AFEDC2645A-L000447](../../tests/test_task_understanding.py#L447) | 447 | `"    assert not any(row.get(\"stage\") == \"exfiltrate\" for row in safe[\"decision_matrix\"])"` | — |
| [SRC-AFEDC2645A-L000448](../../tests/test_task_understanding.py#L448) | 448 | `"    assert \"reasoning_guidance\" not in safe"` | — |
| [SRC-AFEDC2645A-L000449](../../tests/test_task_understanding.py#L449) | 449 | `""` | — |
| [SRC-AFEDC2645A-L000450](../../tests/test_task_understanding.py#L450) | 450 | `""` | — |
| [SRC-AFEDC2645A-L000451](../../tests/test_task_understanding.py#L451) | 451 | `"def test_task_spec_merges_inherited_location_and_budget_slots_into_constraints():"` | — |
| [SRC-AFEDC2645A-L000452](../../tests/test_task_understanding.py#L452) | 452 | `"    question = \"مراكز صيانة لابتوب اليوم\""` | — |
| [SRC-AFEDC2645A-L000453](../../tests/test_task_understanding.py#L453) | 453 | `"    context = {"` | — |
| [SRC-AFEDC2645A-L000454](../../tests/test_task_understanding.py#L454) | 454 | `"        \"resolved_question\": \"مراكز صيانة لابتوب اليوم في الإسكندرية بميزانية أقل من 20000 جنيه\","` | — |
| [SRC-AFEDC2645A-L000455](../../tests/test_task_understanding.py#L455) | 455 | `"        \"topic\": \"مراكز صيانة لابتوب\","` | — |
| [SRC-AFEDC2645A-L000456](../../tests/test_task_understanding.py#L456) | 456 | `"        \"entities\": [\"لابتوب\"],"` | — |
| [SRC-AFEDC2645A-L000457](../../tests/test_task_understanding.py#L457) | 457 | `"        \"slots\": {"` | — |
| [SRC-AFEDC2645A-L000458](../../tests/test_task_understanding.py#L458) | 458 | `"            \"location\": \"الإسكندرية\","` | — |
| [SRC-AFEDC2645A-L000459](../../tests/test_task_understanding.py#L459) | 459 | `"            \"budget\": \"أقل من 20000 جنيه\","` | — |
| [SRC-AFEDC2645A-L000460](../../tests/test_task_understanding.py#L460) | 460 | `"        },"` | — |
| [SRC-AFEDC2645A-L000461](../../tests/test_task_understanding.py#L461) | 461 | `"        \"changed_slots\": [\"location\", \"budget\"],"` | — |
| [SRC-AFEDC2645A-L000462](../../tests/test_task_understanding.py#L462) | 462 | `"        \"is_follow_up\": True,"` | — |
| [SRC-AFEDC2645A-L000463](../../tests/test_task_understanding.py#L463) | 463 | `"        \"topic_shift\": False,"` | — |
| [SRC-AFEDC2645A-L000464](../../tests/test_task_understanding.py#L464) | 464 | `"        \"needs_clarification\": False,"` | — |
| [SRC-AFEDC2645A-L000465](../../tests/test_task_understanding.py#L465) | 465 | `"    }"` | — |
| [SRC-AFEDC2645A-L000466](../../tests/test_task_understanding.py#L466) | 466 | `""` | — |
| [SRC-AFEDC2645A-L000467](../../tests/test_task_understanding.py#L467) | 467 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000468](../../tests/test_task_understanding.py#L468) | 468 | `"        question,"` | — |
| [SRC-AFEDC2645A-L000469](../../tests/test_task_understanding.py#L469) | 469 | `"        mode=\"latest\","` | — |
| [SRC-AFEDC2645A-L000470](../../tests/test_task_understanding.py#L470) | 470 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000471](../../tests/test_task_understanding.py#L471) | 471 | `"        dialogue_context=context,"` | — |
| [SRC-AFEDC2645A-L000472](../../tests/test_task_understanding.py#L472) | 472 | `"    )"` | — |
| [SRC-AFEDC2645A-L000473](../../tests/test_task_understanding.py#L473) | 473 | `""` | — |
| [SRC-AFEDC2645A-L000474](../../tests/test_task_understanding.py#L474) | 474 | `"    assert \"الإسكندرية\" in spec[\"constraints\"][\"explicit_locations\"]"` | — |
| [SRC-AFEDC2645A-L000475](../../tests/test_task_understanding.py#L475) | 475 | `"    assert \"أقل من 20000 جنيه\" in spec[\"constraints\"][\"explicit_budgets\"]"` | — |
| [SRC-AFEDC2645A-L000476](../../tests/test_task_understanding.py#L476) | 476 | `""` | — |
| [SRC-AFEDC2645A-L000477](../../tests/test_task_understanding.py#L477) | 477 | `"    rows = build_query_strategy_matrix("` | — |
| [SRC-AFEDC2645A-L000478](../../tests/test_task_understanding.py#L478) | 478 | `"        question,"` | — |
| [SRC-AFEDC2645A-L000479](../../tests/test_task_understanding.py#L479) | 479 | `"        spec,"` | — |
| [SRC-AFEDC2645A-L000480](../../tests/test_task_understanding.py#L480) | 480 | `"        [spec[\"context_resolution\"][\"resolved_question\"]],"` | — |
| [SRC-AFEDC2645A-L000481](../../tests/test_task_understanding.py#L481) | 481 | `"        limit=8,"` | — |
| [SRC-AFEDC2645A-L000482](../../tests/test_task_understanding.py#L482) | 482 | `"    )"` | — |
| [SRC-AFEDC2645A-L000483](../../tests/test_task_understanding.py#L483) | 483 | `"    assert any(\"الإسكندرية\" in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000484](../../tests/test_task_understanding.py#L484) | 484 | `""` | — |
| [SRC-AFEDC2645A-L000485](../../tests/test_task_understanding.py#L485) | 485 | `""` | — |
| [SRC-AFEDC2645A-L000486](../../tests/test_task_understanding.py#L486) | 486 | `"def test_task_spec_does_not_inherit_location_or_budget_from_topic_shift():"` | — |
| [SRC-AFEDC2645A-L000487](../../tests/test_task_understanding.py#L487) | 487 | `"    question = \"مواصفات لاب توب ديل\""` | — |
| [SRC-AFEDC2645A-L000488](../../tests/test_task_understanding.py#L488) | 488 | `"    context = {"` | — |
| [SRC-AFEDC2645A-L000489](../../tests/test_task_understanding.py#L489) | 489 | `"        \"resolved_question\": question,"` | — |
| [SRC-AFEDC2645A-L000490](../../tests/test_task_understanding.py#L490) | 490 | `"        \"topic\": \"\","` | — |
| [SRC-AFEDC2645A-L000491](../../tests/test_task_understanding.py#L491) | 491 | `"        \"entities\": [],"` | — |
| [SRC-AFEDC2645A-L000492](../../tests/test_task_understanding.py#L492) | 492 | `"        \"slots\": {"` | — |
| [SRC-AFEDC2645A-L000493](../../tests/test_task_understanding.py#L493) | 493 | `"            \"location\": \"الإسكندرية\","` | — |
| [SRC-AFEDC2645A-L000494](../../tests/test_task_understanding.py#L494) | 494 | `"            \"budget\": \"أقل من 20000 جنيه\","` | — |
| [SRC-AFEDC2645A-L000495](../../tests/test_task_understanding.py#L495) | 495 | `"        },"` | — |
| [SRC-AFEDC2645A-L000496](../../tests/test_task_understanding.py#L496) | 496 | `"        \"changed_slots\": [],"` | — |
| [SRC-AFEDC2645A-L000497](../../tests/test_task_understanding.py#L497) | 497 | `"        \"is_follow_up\": False,"` | — |
| [SRC-AFEDC2645A-L000498](../../tests/test_task_understanding.py#L498) | 498 | `"        \"topic_shift\": True,"` | — |
| [SRC-AFEDC2645A-L000499](../../tests/test_task_understanding.py#L499) | 499 | `"        \"needs_clarification\": False,"` | — |
| [SRC-AFEDC2645A-L000500](../../tests/test_task_understanding.py#L500) | 500 | `"    }"` | — |
| [SRC-AFEDC2645A-L000501](../../tests/test_task_understanding.py#L501) | 501 | `""` | — |
| [SRC-AFEDC2645A-L000502](../../tests/test_task_understanding.py#L502) | 502 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000503](../../tests/test_task_understanding.py#L503) | 503 | `"        question,"` | — |
| [SRC-AFEDC2645A-L000504](../../tests/test_task_understanding.py#L504) | 504 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000505](../../tests/test_task_understanding.py#L505) | 505 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000506](../../tests/test_task_understanding.py#L506) | 506 | `"        dialogue_context=context,"` | — |
| [SRC-AFEDC2645A-L000507](../../tests/test_task_understanding.py#L507) | 507 | `"    )"` | — |
| [SRC-AFEDC2645A-L000508](../../tests/test_task_understanding.py#L508) | 508 | `""` | — |
| [SRC-AFEDC2645A-L000509](../../tests/test_task_understanding.py#L509) | 509 | `"    assert \"الإسكندرية\" not in spec[\"constraints\"][\"explicit_locations\"]"` | — |
| [SRC-AFEDC2645A-L000510](../../tests/test_task_understanding.py#L510) | 510 | `"    assert \"أقل من 20000 جنيه\" not in spec[\"constraints\"][\"explicit_budgets\"]"` | — |
| [SRC-AFEDC2645A-L000511](../../tests/test_task_understanding.py#L511) | 511 | `""` | — |
| [SRC-AFEDC2645A-L000512](../../tests/test_task_understanding.py#L512) | 512 | `""` | — |
| [SRC-AFEDC2645A-L000513](../../tests/test_task_understanding.py#L513) | 513 | `"def test_query_strategy_matrix_applies_inherited_location_and_budget_to_all_candidates():"` | — |
| [SRC-AFEDC2645A-L000514](../../tests/test_task_understanding.py#L514) | 514 | `"    question = \"رشح لي أفضل لابتوب للعمل\""` | — |
| [SRC-AFEDC2645A-L000515](../../tests/test_task_understanding.py#L515) | 515 | `"    context = {"` | — |
| [SRC-AFEDC2645A-L000516](../../tests/test_task_understanding.py#L516) | 516 | `"        \"resolved_question\": \"رشح لي أفضل لابتوب للعمل في الإسكندرية بميزانية أقل من 20000 جنيه\","` | — |
| [SRC-AFEDC2645A-L000517](../../tests/test_task_understanding.py#L517) | 517 | `"        \"topic\": \"لابتوب للعمل\","` | — |
| [SRC-AFEDC2645A-L000518](../../tests/test_task_understanding.py#L518) | 518 | `"        \"entities\": [\"لابتوب\"],"` | — |
| [SRC-AFEDC2645A-L000519](../../tests/test_task_understanding.py#L519) | 519 | `"        \"slots\": {"` | — |
| [SRC-AFEDC2645A-L000520](../../tests/test_task_understanding.py#L520) | 520 | `"            \"location\": \"الإسكندرية\","` | — |
| [SRC-AFEDC2645A-L000521](../../tests/test_task_understanding.py#L521) | 521 | `"            \"budget\": \"أقل من 20000 جنيه\","` | — |
| [SRC-AFEDC2645A-L000522](../../tests/test_task_understanding.py#L522) | 522 | `"        },"` | — |
| [SRC-AFEDC2645A-L000523](../../tests/test_task_understanding.py#L523) | 523 | `"        \"changed_slots\": [],"` | — |
| [SRC-AFEDC2645A-L000524](../../tests/test_task_understanding.py#L524) | 524 | `"        \"is_follow_up\": True,"` | — |
| [SRC-AFEDC2645A-L000525](../../tests/test_task_understanding.py#L525) | 525 | `"        \"topic_shift\": False,"` | — |
| [SRC-AFEDC2645A-L000526](../../tests/test_task_understanding.py#L526) | 526 | `"        \"needs_clarification\": False,"` | — |
| [SRC-AFEDC2645A-L000527](../../tests/test_task_understanding.py#L527) | 527 | `"    }"` | — |
| [SRC-AFEDC2645A-L000528](../../tests/test_task_understanding.py#L528) | 528 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000529](../../tests/test_task_understanding.py#L529) | 529 | `"        question,"` | — |
| [SRC-AFEDC2645A-L000530](../../tests/test_task_understanding.py#L530) | 530 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000531](../../tests/test_task_understanding.py#L531) | 531 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000532](../../tests/test_task_understanding.py#L532) | 532 | `"        dialogue_context=context,"` | — |
| [SRC-AFEDC2645A-L000533](../../tests/test_task_understanding.py#L533) | 533 | `"    )"` | — |
| [SRC-AFEDC2645A-L000534](../../tests/test_task_understanding.py#L534) | 534 | `""` | — |
| [SRC-AFEDC2645A-L000535](../../tests/test_task_understanding.py#L535) | 535 | `"    rows = build_query_strategy_matrix(question, spec, [question], limit=8)"` | — |
| [SRC-AFEDC2645A-L000536](../../tests/test_task_understanding.py#L536) | 536 | `""` | — |
| [SRC-AFEDC2645A-L000537](../../tests/test_task_understanding.py#L537) | 537 | `"    assert len(rows) >= 2"` | — |
| [SRC-AFEDC2645A-L000538](../../tests/test_task_understanding.py#L538) | 538 | `"    assert all(\"الإسكندرية\" in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000539](../../tests/test_task_understanding.py#L539) | 539 | `"    assert all(\"أقل من 20000 جنيه\" in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000540](../../tests/test_task_understanding.py#L540) | 540 | `""` | — |
| [SRC-AFEDC2645A-L000541](../../tests/test_task_understanding.py#L541) | 541 | `""` | — |
| [SRC-AFEDC2645A-L000542](../../tests/test_task_understanding.py#L542) | 542 | `"@pytest.mark.parametrize("` | — |
| [SRC-AFEDC2645A-L000543](../../tests/test_task_understanding.py#L543) | 543 | `"    (\"location\", \"seed_query\", \"location_alias\"),"` | — |
| [SRC-AFEDC2645A-L000544](../../tests/test_task_understanding.py#L544) | 544 | `"    ["` | — |
| [SRC-AFEDC2645A-L000545](../../tests/test_task_understanding.py#L545) | 545 | `"        (\"مصر\", \"industrial fire alarm system buyers in Egypt\", \"egypt\"),"` | — |
| [SRC-AFEDC2645A-L000546](../../tests/test_task_understanding.py#L546) | 546 | `"        (\"الإسكندرية\", \"best work laptop options in Alexandria\", \"alexandria\"),"` | — |
| [SRC-AFEDC2645A-L000547](../../tests/test_task_understanding.py#L547) | 547 | `"    ],"` | — |
| [SRC-AFEDC2645A-L000548](../../tests/test_task_understanding.py#L548) | 548 | `")"` | — |
| [SRC-AFEDC2645A-L000549](../../tests/test_task_understanding.py#L549) | 549 | `"def test_query_strategy_matrix_does_not_duplicate_location_in_another_language("` | — |
| [SRC-AFEDC2645A-L000550](../../tests/test_task_understanding.py#L550) | 550 | `"    location, seed_query, location_alias"` | — |
| [SRC-AFEDC2645A-L000551](../../tests/test_task_understanding.py#L551) | 551 | `"):"` | — |
| [SRC-AFEDC2645A-L000552](../../tests/test_task_understanding.py#L552) | 552 | `"    context = {"` | — |
| [SRC-AFEDC2645A-L000553](../../tests/test_task_understanding.py#L553) | 553 | `"        \"resolved_question\": f\"رشح لي منتجًا مناسبًا في {location}\","` | — |
| [SRC-AFEDC2645A-L000554](../../tests/test_task_understanding.py#L554) | 554 | `"        \"topic\": \"ترشيح منتج\","` | — |
| [SRC-AFEDC2645A-L000555](../../tests/test_task_understanding.py#L555) | 555 | `"        \"entities\": [\"منتج\"],"` | — |
| [SRC-AFEDC2645A-L000556](../../tests/test_task_understanding.py#L556) | 556 | `"        \"slots\": {\"location\": location},"` | — |
| [SRC-AFEDC2645A-L000557](../../tests/test_task_understanding.py#L557) | 557 | `"        \"changed_slots\": [\"location\"],"` | — |
| [SRC-AFEDC2645A-L000558](../../tests/test_task_understanding.py#L558) | 558 | `"        \"is_follow_up\": True,"` | — |
| [SRC-AFEDC2645A-L000559](../../tests/test_task_understanding.py#L559) | 559 | `"        \"topic_shift\": False,"` | — |
| [SRC-AFEDC2645A-L000560](../../tests/test_task_understanding.py#L560) | 560 | `"        \"needs_clarification\": False,"` | — |
| [SRC-AFEDC2645A-L000561](../../tests/test_task_understanding.py#L561) | 561 | `"    }"` | — |
| [SRC-AFEDC2645A-L000562](../../tests/test_task_understanding.py#L562) | 562 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000563](../../tests/test_task_understanding.py#L563) | 563 | `"        \"رشح لي أفضل لابتوب للعمل\","` | — |
| [SRC-AFEDC2645A-L000564](../../tests/test_task_understanding.py#L564) | 564 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000565](../../tests/test_task_understanding.py#L565) | 565 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000566](../../tests/test_task_understanding.py#L566) | 566 | `"        dialogue_context=context,"` | — |
| [SRC-AFEDC2645A-L000567](../../tests/test_task_understanding.py#L567) | 567 | `"    )"` | — |
| [SRC-AFEDC2645A-L000568](../../tests/test_task_understanding.py#L568) | 568 | `""` | — |
| [SRC-AFEDC2645A-L000569](../../tests/test_task_understanding.py#L569) | 569 | `"    rows = build_query_strategy_matrix("` | — |
| [SRC-AFEDC2645A-L000570](../../tests/test_task_understanding.py#L570) | 570 | `"        \"رشح لي أفضل لابتوب للعمل\","` | — |
| [SRC-AFEDC2645A-L000571](../../tests/test_task_understanding.py#L571) | 571 | `"        spec,"` | — |
| [SRC-AFEDC2645A-L000572](../../tests/test_task_understanding.py#L572) | 572 | `"        [seed_query],"` | — |
| [SRC-AFEDC2645A-L000573](../../tests/test_task_understanding.py#L573) | 573 | `"        limit=8,"` | — |
| [SRC-AFEDC2645A-L000574](../../tests/test_task_understanding.py#L574) | 574 | `"    )"` | — |
| [SRC-AFEDC2645A-L000575](../../tests/test_task_understanding.py#L575) | 575 | `""` | — |
| [SRC-AFEDC2645A-L000576](../../tests/test_task_understanding.py#L576) | 576 | `"    assert len(rows) >= 2"` | — |
| [SRC-AFEDC2645A-L000577](../../tests/test_task_understanding.py#L577) | 577 | `"    assert all(location_alias in row[\"query\"].casefold() for row in rows)"` | — |
| [SRC-AFEDC2645A-L000578](../../tests/test_task_understanding.py#L578) | 578 | `"    assert all(location not in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000579](../../tests/test_task_understanding.py#L579) | 579 | `""` | — |
| [SRC-AFEDC2645A-L000580](../../tests/test_task_understanding.py#L580) | 580 | `""` | — |
| [SRC-AFEDC2645A-L000581](../../tests/test_task_understanding.py#L581) | 581 | `"def test_long_query_reserves_space_for_inherited_location_and_budget():"` | — |
| [SRC-AFEDC2645A-L000582](../../tests/test_task_understanding.py#L582) | 582 | `"    question = \"رشح لي أفضل لابتوب للعمل \" + (\"مقارنة المواصفات والأداء والاستخدامات \" * 12)"` | — |
| [SRC-AFEDC2645A-L000583](../../tests/test_task_understanding.py#L583) | 583 | `"    context = {"` | — |
| [SRC-AFEDC2645A-L000584](../../tests/test_task_understanding.py#L584) | 584 | `"        \"resolved_question\": question,"` | — |
| [SRC-AFEDC2645A-L000585](../../tests/test_task_understanding.py#L585) | 585 | `"        \"topic\": \"لابتوب للعمل\","` | — |
| [SRC-AFEDC2645A-L000586](../../tests/test_task_understanding.py#L586) | 586 | `"        \"entities\": [\"لابتوب\"],"` | — |
| [SRC-AFEDC2645A-L000587](../../tests/test_task_understanding.py#L587) | 587 | `"        \"slots\": {"` | — |
| [SRC-AFEDC2645A-L000588](../../tests/test_task_understanding.py#L588) | 588 | `"            \"location\": \"الإسكندرية\","` | — |
| [SRC-AFEDC2645A-L000589](../../tests/test_task_understanding.py#L589) | 589 | `"            \"budget\": \"أقل من 20000 جنيه\","` | — |
| [SRC-AFEDC2645A-L000590](../../tests/test_task_understanding.py#L590) | 590 | `"        },"` | — |
| [SRC-AFEDC2645A-L000591](../../tests/test_task_understanding.py#L591) | 591 | `"        \"changed_slots\": [],"` | — |
| [SRC-AFEDC2645A-L000592](../../tests/test_task_understanding.py#L592) | 592 | `"        \"is_follow_up\": True,"` | — |
| [SRC-AFEDC2645A-L000593](../../tests/test_task_understanding.py#L593) | 593 | `"        \"topic_shift\": False,"` | — |
| [SRC-AFEDC2645A-L000594](../../tests/test_task_understanding.py#L594) | 594 | `"        \"needs_clarification\": False,"` | — |
| [SRC-AFEDC2645A-L000595](../../tests/test_task_understanding.py#L595) | 595 | `"    }"` | — |
| [SRC-AFEDC2645A-L000596](../../tests/test_task_understanding.py#L596) | 596 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000597](../../tests/test_task_understanding.py#L597) | 597 | `"        question,"` | — |
| [SRC-AFEDC2645A-L000598](../../tests/test_task_understanding.py#L598) | 598 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000599](../../tests/test_task_understanding.py#L599) | 599 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000600](../../tests/test_task_understanding.py#L600) | 600 | `"        dialogue_context=context,"` | — |
| [SRC-AFEDC2645A-L000601](../../tests/test_task_understanding.py#L601) | 601 | `"    )"` | — |
| [SRC-AFEDC2645A-L000602](../../tests/test_task_understanding.py#L602) | 602 | `""` | — |
| [SRC-AFEDC2645A-L000603](../../tests/test_task_understanding.py#L603) | 603 | `"    rows = build_query_strategy_matrix(question, spec, [question], limit=8)"` | — |
| [SRC-AFEDC2645A-L000604](../../tests/test_task_understanding.py#L604) | 604 | `""` | — |
| [SRC-AFEDC2645A-L000605](../../tests/test_task_understanding.py#L605) | 605 | `"    assert len(rows) >= 2"` | — |
| [SRC-AFEDC2645A-L000606](../../tests/test_task_understanding.py#L606) | 606 | `"    assert all(len(row[\"query\"]) <= 240 for row in rows)"` | — |
| [SRC-AFEDC2645A-L000607](../../tests/test_task_understanding.py#L607) | 607 | `"    assert all(\"الإسكندرية\" in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000608](../../tests/test_task_understanding.py#L608) | 608 | `"    assert all(\"أقل من 20000 جنيه\" in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000609](../../tests/test_task_understanding.py#L609) | 609 | `""` | — |
| [SRC-AFEDC2645A-L000610](../../tests/test_task_understanding.py#L610) | 610 | `""` | — |
| [SRC-AFEDC2645A-L000611](../../tests/test_task_understanding.py#L611) | 611 | `"def test_long_query_keeps_location_and_budget_that_appear_only_in_truncated_tail():"` | — |
| [SRC-AFEDC2645A-L000612](../../tests/test_task_understanding.py#L612) | 612 | `"    question = ("` | — |
| [SRC-AFEDC2645A-L000613](../../tests/test_task_understanding.py#L613) | 613 | `"        \"رشح لي أفضل لابتوب للعمل \""` | — |
| [SRC-AFEDC2645A-L000614](../../tests/test_task_understanding.py#L614) | 614 | `"        + (\"مقارنة المواصفات والأداء والاستخدامات \" * 10)"` | — |
| [SRC-AFEDC2645A-L000615](../../tests/test_task_understanding.py#L615) | 615 | `"        + \"في الإسكندرية بميزانية أقل من 20000 جنيه\""` | — |
| [SRC-AFEDC2645A-L000616](../../tests/test_task_understanding.py#L616) | 616 | `"    )"` | — |
| [SRC-AFEDC2645A-L000617](../../tests/test_task_understanding.py#L617) | 617 | `"    context = {"` | — |
| [SRC-AFEDC2645A-L000618](../../tests/test_task_understanding.py#L618) | 618 | `"        \"resolved_question\": question,"` | — |
| [SRC-AFEDC2645A-L000619](../../tests/test_task_understanding.py#L619) | 619 | `"        \"topic\": \"لابتوب للعمل\","` | — |
| [SRC-AFEDC2645A-L000620](../../tests/test_task_understanding.py#L620) | 620 | `"        \"entities\": [\"لابتوب\"],"` | — |
| [SRC-AFEDC2645A-L000621](../../tests/test_task_understanding.py#L621) | 621 | `"        \"slots\": {"` | — |
| [SRC-AFEDC2645A-L000622](../../tests/test_task_understanding.py#L622) | 622 | `"            \"location\": \"الإسكندرية\","` | — |
| [SRC-AFEDC2645A-L000623](../../tests/test_task_understanding.py#L623) | 623 | `"            \"budget\": \"أقل من 20000 جنيه\","` | — |
| [SRC-AFEDC2645A-L000624](../../tests/test_task_understanding.py#L624) | 624 | `"        },"` | — |
| [SRC-AFEDC2645A-L000625](../../tests/test_task_understanding.py#L625) | 625 | `"        \"changed_slots\": [],"` | — |
| [SRC-AFEDC2645A-L000626](../../tests/test_task_understanding.py#L626) | 626 | `"        \"is_follow_up\": True,"` | — |
| [SRC-AFEDC2645A-L000627](../../tests/test_task_understanding.py#L627) | 627 | `"        \"topic_shift\": False,"` | — |
| [SRC-AFEDC2645A-L000628](../../tests/test_task_understanding.py#L628) | 628 | `"        \"needs_clarification\": False,"` | — |
| [SRC-AFEDC2645A-L000629](../../tests/test_task_understanding.py#L629) | 629 | `"    }"` | — |
| [SRC-AFEDC2645A-L000630](../../tests/test_task_understanding.py#L630) | 630 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000631](../../tests/test_task_understanding.py#L631) | 631 | `"        question,"` | — |
| [SRC-AFEDC2645A-L000632](../../tests/test_task_understanding.py#L632) | 632 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000633](../../tests/test_task_understanding.py#L633) | 633 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000634](../../tests/test_task_understanding.py#L634) | 634 | `"        dialogue_context=context,"` | — |
| [SRC-AFEDC2645A-L000635](../../tests/test_task_understanding.py#L635) | 635 | `"    )"` | — |
| [SRC-AFEDC2645A-L000636](../../tests/test_task_understanding.py#L636) | 636 | `""` | — |
| [SRC-AFEDC2645A-L000637](../../tests/test_task_understanding.py#L637) | 637 | `"    rows = build_query_strategy_matrix(question, spec, [question], limit=8)"` | — |
| [SRC-AFEDC2645A-L000638](../../tests/test_task_understanding.py#L638) | 638 | `""` | — |
| [SRC-AFEDC2645A-L000639](../../tests/test_task_understanding.py#L639) | 639 | `"    assert rows"` | — |
| [SRC-AFEDC2645A-L000640](../../tests/test_task_understanding.py#L640) | 640 | `"    assert all(len(row[\"query\"]) <= 240 for row in rows)"` | — |
| [SRC-AFEDC2645A-L000641](../../tests/test_task_understanding.py#L641) | 641 | `"    assert all(\"الإسكندرية\" in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000642](../../tests/test_task_understanding.py#L642) | 642 | `"    assert all(\"أقل من 20000 جنيه\" in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000643](../../tests/test_task_understanding.py#L643) | 643 | `""` | — |
| [SRC-AFEDC2645A-L000644](../../tests/test_task_understanding.py#L644) | 644 | `""` | — |
| [SRC-AFEDC2645A-L000645](../../tests/test_task_understanding.py#L645) | 645 | `"def test_query_strategy_matrix_carries_confirmed_currency_capacity_and_aspect_slots():"` | — |
| [SRC-AFEDC2645A-L000646](../../tests/test_task_understanding.py#L646) | 646 | `"    question = \"سعره؟\""` | — |
| [SRC-AFEDC2645A-L000647](../../tests/test_task_understanding.py#L647) | 647 | `"    context = {"` | — |
| [SRC-AFEDC2645A-L000648](../../tests/test_task_understanding.py#L648) | 648 | `"        \"resolved_question\": \"ما سعر iPhone 17 سعة 256 جيجابايت باليورو مع الضمان؟\","` | — |
| [SRC-AFEDC2645A-L000649](../../tests/test_task_understanding.py#L649) | 649 | `"        \"topic\": \"سعر iPhone 17\","` | — |
| [SRC-AFEDC2645A-L000650](../../tests/test_task_understanding.py#L650) | 650 | `"        \"entities\": [\"iPhone 17\"],"` | — |
| [SRC-AFEDC2645A-L000651](../../tests/test_task_understanding.py#L651) | 651 | `"        \"slots\": {"` | — |
| [SRC-AFEDC2645A-L000652](../../tests/test_task_understanding.py#L652) | 652 | `"            \"product\": \"iPhone 17\","` | — |
| [SRC-AFEDC2645A-L000653](../../tests/test_task_understanding.py#L653) | 653 | `"            \"capacity\": \"256 جيجابايت\","` | — |
| [SRC-AFEDC2645A-L000654](../../tests/test_task_understanding.py#L654) | 654 | `"            \"currency\": \"اليورو\","` | — |
| [SRC-AFEDC2645A-L000655](../../tests/test_task_understanding.py#L655) | 655 | `"            \"aspect\": \"الضمان\","` | — |
| [SRC-AFEDC2645A-L000656](../../tests/test_task_understanding.py#L656) | 656 | `"        },"` | — |
| [SRC-AFEDC2645A-L000657](../../tests/test_task_understanding.py#L657) | 657 | `"        \"changed_slots\": [\"currency\", \"aspect\"],"` | — |
| [SRC-AFEDC2645A-L000658](../../tests/test_task_understanding.py#L658) | 658 | `"        \"is_follow_up\": True,"` | — |
| [SRC-AFEDC2645A-L000659](../../tests/test_task_understanding.py#L659) | 659 | `"        \"topic_shift\": False,"` | — |
| [SRC-AFEDC2645A-L000660](../../tests/test_task_understanding.py#L660) | 660 | `"        \"needs_clarification\": False,"` | — |
| [SRC-AFEDC2645A-L000661](../../tests/test_task_understanding.py#L661) | 661 | `"    }"` | — |
| [SRC-AFEDC2645A-L000662](../../tests/test_task_understanding.py#L662) | 662 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000663](../../tests/test_task_understanding.py#L663) | 663 | `"        question,"` | — |
| [SRC-AFEDC2645A-L000664](../../tests/test_task_understanding.py#L664) | 664 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000665](../../tests/test_task_understanding.py#L665) | 665 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000666](../../tests/test_task_understanding.py#L666) | 666 | `"        dialogue_context=context,"` | — |
| [SRC-AFEDC2645A-L000667](../../tests/test_task_understanding.py#L667) | 667 | `"    )"` | — |
| [SRC-AFEDC2645A-L000668](../../tests/test_task_understanding.py#L668) | 668 | `""` | — |
| [SRC-AFEDC2645A-L000669](../../tests/test_task_understanding.py#L669) | 669 | `"    rows = build_query_strategy_matrix("` | — |
| [SRC-AFEDC2645A-L000670](../../tests/test_task_understanding.py#L670) | 670 | `"        question,"` | — |
| [SRC-AFEDC2645A-L000671](../../tests/test_task_understanding.py#L671) | 671 | `"        spec,"` | — |
| [SRC-AFEDC2645A-L000672](../../tests/test_task_understanding.py#L672) | 672 | `"        [\"iPhone 17 price\"],"` | — |
| [SRC-AFEDC2645A-L000673](../../tests/test_task_understanding.py#L673) | 673 | `"        limit=8,"` | — |
| [SRC-AFEDC2645A-L000674](../../tests/test_task_understanding.py#L674) | 674 | `"    )"` | — |
| [SRC-AFEDC2645A-L000675](../../tests/test_task_understanding.py#L675) | 675 | `""` | — |
| [SRC-AFEDC2645A-L000676](../../tests/test_task_understanding.py#L676) | 676 | `"    assert len(rows) >= 2"` | — |
| [SRC-AFEDC2645A-L000677](../../tests/test_task_understanding.py#L677) | 677 | `"    assert all(\"256 جيجابايت\" in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000678](../../tests/test_task_understanding.py#L678) | 678 | `"    assert all(\"اليورو\" in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000679](../../tests/test_task_understanding.py#L679) | 679 | `"    assert all(\"الضمان\" in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000680](../../tests/test_task_understanding.py#L680) | 680 | `""` | — |
| [SRC-AFEDC2645A-L000681](../../tests/test_task_understanding.py#L681) | 681 | `""` | — |
| [SRC-AFEDC2645A-L000682](../../tests/test_task_understanding.py#L682) | 682 | `"def test_query_strategy_matrix_recognizes_currency_capacity_and_aspect_aliases():"` | — |
| [SRC-AFEDC2645A-L000683](../../tests/test_task_understanding.py#L683) | 683 | `"    question = \"سعره؟\""` | — |
| [SRC-AFEDC2645A-L000684](../../tests/test_task_understanding.py#L684) | 684 | `"    context = {"` | — |
| [SRC-AFEDC2645A-L000685](../../tests/test_task_understanding.py#L685) | 685 | `"        \"resolved_question\": \"ما سعر iPhone 17 سعة 256 جيجابايت باليورو مع الضمان؟\","` | — |
| [SRC-AFEDC2645A-L000686](../../tests/test_task_understanding.py#L686) | 686 | `"        \"topic\": \"سعر iPhone 17\","` | — |
| [SRC-AFEDC2645A-L000687](../../tests/test_task_understanding.py#L687) | 687 | `"        \"entities\": [\"iPhone 17\"],"` | — |
| [SRC-AFEDC2645A-L000688](../../tests/test_task_understanding.py#L688) | 688 | `"        \"slots\": {"` | — |
| [SRC-AFEDC2645A-L000689](../../tests/test_task_understanding.py#L689) | 689 | `"            \"product\": \"iPhone 17\","` | — |
| [SRC-AFEDC2645A-L000690](../../tests/test_task_understanding.py#L690) | 690 | `"            \"capacity\": \"256 جيجابايت\","` | — |
| [SRC-AFEDC2645A-L000691](../../tests/test_task_understanding.py#L691) | 691 | `"            \"currency\": \"اليورو\","` | — |
| [SRC-AFEDC2645A-L000692](../../tests/test_task_understanding.py#L692) | 692 | `"            \"aspect\": \"الضمان\","` | — |
| [SRC-AFEDC2645A-L000693](../../tests/test_task_understanding.py#L693) | 693 | `"        },"` | — |
| [SRC-AFEDC2645A-L000694](../../tests/test_task_understanding.py#L694) | 694 | `"        \"changed_slots\": [\"currency\", \"aspect\"],"` | — |
| [SRC-AFEDC2645A-L000695](../../tests/test_task_understanding.py#L695) | 695 | `"        \"is_follow_up\": True,"` | — |
| [SRC-AFEDC2645A-L000696](../../tests/test_task_understanding.py#L696) | 696 | `"        \"topic_shift\": False,"` | — |
| [SRC-AFEDC2645A-L000697](../../tests/test_task_understanding.py#L697) | 697 | `"        \"needs_clarification\": False,"` | — |
| [SRC-AFEDC2645A-L000698](../../tests/test_task_understanding.py#L698) | 698 | `"    }"` | — |
| [SRC-AFEDC2645A-L000699](../../tests/test_task_understanding.py#L699) | 699 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000700](../../tests/test_task_understanding.py#L700) | 700 | `"        question,"` | — |
| [SRC-AFEDC2645A-L000701](../../tests/test_task_understanding.py#L701) | 701 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000702](../../tests/test_task_understanding.py#L702) | 702 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000703](../../tests/test_task_understanding.py#L703) | 703 | `"        dialogue_context=context,"` | — |
| [SRC-AFEDC2645A-L000704](../../tests/test_task_understanding.py#L704) | 704 | `"    )"` | — |
| [SRC-AFEDC2645A-L000705](../../tests/test_task_understanding.py#L705) | 705 | `""` | — |
| [SRC-AFEDC2645A-L000706](../../tests/test_task_understanding.py#L706) | 706 | `"    rows = build_query_strategy_matrix("` | — |
| [SRC-AFEDC2645A-L000707](../../tests/test_task_understanding.py#L707) | 707 | `"        question,"` | — |
| [SRC-AFEDC2645A-L000708](../../tests/test_task_understanding.py#L708) | 708 | `"        spec,"` | — |
| [SRC-AFEDC2645A-L000709](../../tests/test_task_understanding.py#L709) | 709 | `"        [\"iPhone 17 price 256GB EUR warranty\"],"` | — |
| [SRC-AFEDC2645A-L000710](../../tests/test_task_understanding.py#L710) | 710 | `"        limit=8,"` | — |
| [SRC-AFEDC2645A-L000711](../../tests/test_task_understanding.py#L711) | 711 | `"    )"` | — |
| [SRC-AFEDC2645A-L000712](../../tests/test_task_understanding.py#L712) | 712 | `""` | — |
| [SRC-AFEDC2645A-L000713](../../tests/test_task_understanding.py#L713) | 713 | `"    # The seed already contains English aliases for every inherited slot;"` | — |
| [SRC-AFEDC2645A-L000714](../../tests/test_task_understanding.py#L714) | 714 | `"    # no redundant Arabic-only query should be added."` | — |
| [SRC-AFEDC2645A-L000715](../../tests/test_task_understanding.py#L715) | 715 | `"    assert len(rows) >= 1"` | — |
| [SRC-AFEDC2645A-L000716](../../tests/test_task_understanding.py#L716) | 716 | `"    assert all(\"اليورو\" not in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000717](../../tests/test_task_understanding.py#L717) | 717 | `"    assert all(\"256 جيجابايت\" not in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000718](../../tests/test_task_understanding.py#L718) | 718 | `"    assert all(\"الضمان\" not in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000719](../../tests/test_task_understanding.py#L719) | 719 | `""` | — |
| [SRC-AFEDC2645A-L000720](../../tests/test_task_understanding.py#L720) | 720 | `""` | — |
| [SRC-AFEDC2645A-L000721](../../tests/test_task_understanding.py#L721) | 721 | `"def test_query_strategy_matrix_does_not_inherit_semantic_slots_after_topic_shift():"` | — |
| [SRC-AFEDC2645A-L000722](../../tests/test_task_understanding.py#L722) | 722 | `"    question = \"مواصفات لابتوب ديل\""` | — |
| [SRC-AFEDC2645A-L000723](../../tests/test_task_understanding.py#L723) | 723 | `"    context = {"` | — |
| [SRC-AFEDC2645A-L000724](../../tests/test_task_understanding.py#L724) | 724 | `"        \"resolved_question\": question,"` | — |
| [SRC-AFEDC2645A-L000725](../../tests/test_task_understanding.py#L725) | 725 | `"        \"topic\": \"\","` | — |
| [SRC-AFEDC2645A-L000726](../../tests/test_task_understanding.py#L726) | 726 | `"        \"entities\": [],"` | — |
| [SRC-AFEDC2645A-L000727](../../tests/test_task_understanding.py#L727) | 727 | `"        \"slots\": {"` | — |
| [SRC-AFEDC2645A-L000728](../../tests/test_task_understanding.py#L728) | 728 | `"            \"product\": \"iPhone 17\","` | — |
| [SRC-AFEDC2645A-L000729](../../tests/test_task_understanding.py#L729) | 729 | `"            \"capacity\": \"256 جيجابايت\","` | — |
| [SRC-AFEDC2645A-L000730](../../tests/test_task_understanding.py#L730) | 730 | `"            \"currency\": \"اليورو\","` | — |
| [SRC-AFEDC2645A-L000731](../../tests/test_task_understanding.py#L731) | 731 | `"            \"aspect\": \"الضمان\","` | — |
| [SRC-AFEDC2645A-L000732](../../tests/test_task_understanding.py#L732) | 732 | `"        },"` | — |
| [SRC-AFEDC2645A-L000733](../../tests/test_task_understanding.py#L733) | 733 | `"        \"changed_slots\": [],"` | — |
| [SRC-AFEDC2645A-L000734](../../tests/test_task_understanding.py#L734) | 734 | `"        \"is_follow_up\": False,"` | — |
| [SRC-AFEDC2645A-L000735](../../tests/test_task_understanding.py#L735) | 735 | `"        \"topic_shift\": True,"` | — |
| [SRC-AFEDC2645A-L000736](../../tests/test_task_understanding.py#L736) | 736 | `"        \"needs_clarification\": False,"` | — |
| [SRC-AFEDC2645A-L000737](../../tests/test_task_understanding.py#L737) | 737 | `"    }"` | — |
| [SRC-AFEDC2645A-L000738](../../tests/test_task_understanding.py#L738) | 738 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000739](../../tests/test_task_understanding.py#L739) | 739 | `"        question,"` | — |
| [SRC-AFEDC2645A-L000740](../../tests/test_task_understanding.py#L740) | 740 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000741](../../tests/test_task_understanding.py#L741) | 741 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000742](../../tests/test_task_understanding.py#L742) | 742 | `"        dialogue_context=context,"` | — |
| [SRC-AFEDC2645A-L000743](../../tests/test_task_understanding.py#L743) | 743 | `"    )"` | — |
| [SRC-AFEDC2645A-L000744](../../tests/test_task_understanding.py#L744) | 744 | `""` | — |
| [SRC-AFEDC2645A-L000745](../../tests/test_task_understanding.py#L745) | 745 | `"    rows = build_query_strategy_matrix(question, spec, [question], limit=8)"` | — |
| [SRC-AFEDC2645A-L000746](../../tests/test_task_understanding.py#L746) | 746 | `""` | — |
| [SRC-AFEDC2645A-L000747](../../tests/test_task_understanding.py#L747) | 747 | `"    assert len(rows) >= 1"` | — |
| [SRC-AFEDC2645A-L000748](../../tests/test_task_understanding.py#L748) | 748 | `"    assert all(\"iPhone 17\" not in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000749](../../tests/test_task_understanding.py#L749) | 749 | `"    assert all(\"اليورو\" not in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000750](../../tests/test_task_understanding.py#L750) | 750 | `"    assert all(\"256 جيجابايت\" not in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000751](../../tests/test_task_understanding.py#L751) | 751 | `"    assert all(\"الضمان\" not in row[\"query\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000752](../../tests/test_task_understanding.py#L752) | 752 | `""` | — |
| [SRC-AFEDC2645A-L000753](../../tests/test_task_understanding.py#L753) | 753 | `""` | — |
| [SRC-AFEDC2645A-L000754](../../tests/test_task_understanding.py#L754) | 754 | `"def test_query_strategy_matrix_uses_resolved_topic_instead_of_imperative_query_prefix():"` | — |
| [SRC-AFEDC2645A-L000755](../../tests/test_task_understanding.py#L755) | 755 | `"    spec = {"` | — |
| [SRC-AFEDC2645A-L000756](../../tests/test_task_understanding.py#L756) | 756 | `"        \"task_family\": \"recommendation\","` | — |
| [SRC-AFEDC2645A-L000757](../../tests/test_task_understanding.py#L757) | 757 | `"        \"mode\": \"deep\","` | — |
| [SRC-AFEDC2645A-L000758](../../tests/test_task_understanding.py#L758) | 758 | `"        \"intent_route\": \"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000759](../../tests/test_task_understanding.py#L759) | 759 | `"        \"hypothesis_interpretations\": [],"` | — |
| [SRC-AFEDC2645A-L000760](../../tests/test_task_understanding.py#L760) | 760 | `"        \"constraints\": {"` | — |
| [SRC-AFEDC2645A-L000761](../../tests/test_task_understanding.py#L761) | 761 | `"            \"explicit_aspects\": [],"` | — |
| [SRC-AFEDC2645A-L000762](../../tests/test_task_understanding.py#L762) | 762 | `"            \"explicit_locations\": [],"` | — |
| [SRC-AFEDC2645A-L000763](../../tests/test_task_understanding.py#L763) | 763 | `"            \"explicit_budgets\": [],"` | — |
| [SRC-AFEDC2645A-L000764](../../tests/test_task_understanding.py#L764) | 764 | `"        },"` | — |
| [SRC-AFEDC2645A-L000765](../../tests/test_task_understanding.py#L765) | 765 | `"        \"context_resolution\": {"` | — |
| [SRC-AFEDC2645A-L000766](../../tests/test_task_understanding.py#L766) | 766 | `"            \"topic\": \"لابتوب للعمل\","` | — |
| [SRC-AFEDC2645A-L000767](../../tests/test_task_understanding.py#L767) | 767 | `"            \"entities\": [\"Dell\"],"` | — |
| [SRC-AFEDC2645A-L000768](../../tests/test_task_understanding.py#L768) | 768 | `"            \"slots\": {\"product\": \"لابتوب\", \"model\": \"Dell\"},"` | — |
| [SRC-AFEDC2645A-L000769](../../tests/test_task_understanding.py#L769) | 769 | `"            \"is_follow_up\": True,"` | — |
| [SRC-AFEDC2645A-L000770](../../tests/test_task_understanding.py#L770) | 770 | `"            \"topic_shift\": False,"` | — |
| [SRC-AFEDC2645A-L000771](../../tests/test_task_understanding.py#L771) | 771 | `"            \"needs_clarification\": False,"` | — |
| [SRC-AFEDC2645A-L000772](../../tests/test_task_understanding.py#L772) | 772 | `"        },"` | — |
| [SRC-AFEDC2645A-L000773](../../tests/test_task_understanding.py#L773) | 773 | `"    }"` | — |
| [SRC-AFEDC2645A-L000774](../../tests/test_task_understanding.py#L774) | 774 | `""` | — |
| [SRC-AFEDC2645A-L000775](../../tests/test_task_understanding.py#L775) | 775 | `"    rows = build_query_strategy_matrix("` | — |
| [SRC-AFEDC2645A-L000776](../../tests/test_task_understanding.py#L776) | 776 | `"        \"في وضعي، أبدأ بإيه؟\","` | — |
| [SRC-AFEDC2645A-L000777](../../tests/test_task_understanding.py#L777) | 777 | `"        spec,"` | — |
| [SRC-AFEDC2645A-L000778](../../tests/test_task_understanding.py#L778) | 778 | `"        [\"ابحث لي عن أفضل لابتوب للعمل\"],"` | — |
| [SRC-AFEDC2645A-L000779](../../tests/test_task_understanding.py#L779) | 779 | `"        limit=6,"` | — |
| [SRC-AFEDC2645A-L000780](../../tests/test_task_understanding.py#L780) | 780 | `"    )"` | — |
| [SRC-AFEDC2645A-L000781](../../tests/test_task_understanding.py#L781) | 781 | `""` | — |
| [SRC-AFEDC2645A-L000782](../../tests/test_task_understanding.py#L782) | 782 | `"    assert any("` | — |
| [SRC-AFEDC2645A-L000783](../../tests/test_task_understanding.py#L783) | 783 | `"        row[\"strategy\"] == \"tradeoffs_ar\""` | — |
| [SRC-AFEDC2645A-L000784](../../tests/test_task_understanding.py#L784) | 784 | `"        and row[\"query\"].startswith(\"لابتوب للعمل Dell\")"` | — |
| [SRC-AFEDC2645A-L000785](../../tests/test_task_understanding.py#L785) | 785 | `"        for row in rows"` | — |
| [SRC-AFEDC2645A-L000786](../../tests/test_task_understanding.py#L786) | 786 | `"    )"` | — |
| [SRC-AFEDC2645A-L000787](../../tests/test_task_understanding.py#L787) | 787 | `""` | — |
| [SRC-AFEDC2645A-L000788](../../tests/test_task_understanding.py#L788) | 788 | `""` | — |
| [SRC-AFEDC2645A-L000789](../../tests/test_task_understanding.py#L789) | 789 | `"@pytest.mark.parametrize("` | — |
| [SRC-AFEDC2645A-L000790](../../tests/test_task_understanding.py#L790) | 790 | `"    (\"seed_query\", \"expected_source_phrase\"),"` | — |
| [SRC-AFEDC2645A-L000791](../../tests/test_task_understanding.py#L791) | 791 | `"    ["` | — |
| [SRC-AFEDC2645A-L000792](../../tests/test_task_understanding.py#L792) | 792 | `"        (\"ما سعر iPhone 17 باليورو؟\", \"مصدر رسمي\"),"` | — |
| [SRC-AFEDC2645A-L000793](../../tests/test_task_understanding.py#L793) | 793 | `"        (\"iPhone 17 price in euros\", \"official source\"),"` | — |
| [SRC-AFEDC2645A-L000794](../../tests/test_task_understanding.py#L794) | 794 | `"    ],"` | — |
| [SRC-AFEDC2645A-L000795](../../tests/test_task_understanding.py#L795) | 795 | `")"` | — |
| [SRC-AFEDC2645A-L000796](../../tests/test_task_understanding.py#L796) | 796 | `"def test_short_contextual_followup_adds_source_angle_in_seed_language("` | — |
| [SRC-AFEDC2645A-L000797](../../tests/test_task_understanding.py#L797) | 797 | `"    seed_query, expected_source_phrase"` | — |
| [SRC-AFEDC2645A-L000798](../../tests/test_task_understanding.py#L798) | 798 | `"):"` | — |
| [SRC-AFEDC2645A-L000799](../../tests/test_task_understanding.py#L799) | 799 | `"    question = \"سعره؟\""` | — |
| [SRC-AFEDC2645A-L000800](../../tests/test_task_understanding.py#L800) | 800 | `"    context = {"` | — |
| [SRC-AFEDC2645A-L000801](../../tests/test_task_understanding.py#L801) | 801 | `"        \"resolved_question\": \"ما سعر iPhone 17 باليورو؟\","` | — |
| [SRC-AFEDC2645A-L000802](../../tests/test_task_understanding.py#L802) | 802 | `"        \"topic\": \"سعر iPhone 17\","` | — |
| [SRC-AFEDC2645A-L000803](../../tests/test_task_understanding.py#L803) | 803 | `"        \"entities\": [\"iPhone 17\"],"` | — |
| [SRC-AFEDC2645A-L000804](../../tests/test_task_understanding.py#L804) | 804 | `"        \"slots\": {\"product\": \"iPhone 17\", \"currency\": \"اليورو\"},"` | — |
| [SRC-AFEDC2645A-L000805](../../tests/test_task_understanding.py#L805) | 805 | `"        \"changed_slots\": [\"currency\"],"` | — |
| [SRC-AFEDC2645A-L000806](../../tests/test_task_understanding.py#L806) | 806 | `"        \"is_follow_up\": True,"` | — |
| [SRC-AFEDC2645A-L000807](../../tests/test_task_understanding.py#L807) | 807 | `"        \"topic_shift\": False,"` | — |
