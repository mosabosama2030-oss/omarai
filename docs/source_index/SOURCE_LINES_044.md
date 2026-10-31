# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **044**
- سجلات الأسطر: **800**
- النطاق: SRC-01E35ABC46-L000476 إلى SRC-AFEDC2645A-L000247
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-01E35ABC46 — [tests/test_research_guardrails.py](../../tests/test_research_guardrails.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-01E35ABC46-L000476](../../tests/test_research_guardrails.py#L476) | 476 | `"        question, \"auto\", {\"freshness\": \"any\"}, [official], now=_GUARDRAIL_NOW"` | — |
| [SRC-01E35ABC46-L000477](../../tests/test_research_guardrails.py#L477) | 477 | `"    )"` | — |
| [SRC-01E35ABC46-L000478](../../tests/test_research_guardrails.py#L478) | 478 | `"    assert accepted == []"` | — |
| [SRC-01E35ABC46-L000479](../../tests/test_research_guardrails.py#L479) | 479 | `"    assert report[\"rejection_counts\"] == {\"date_unavailable\": 1}"` | — |
| [SRC-01E35ABC46-L000480](../../tests/test_research_guardrails.py#L480) | 480 | `""` | — |
| [SRC-01E35ABC46-L000481](../../tests/test_research_guardrails.py#L481) | 481 | `""` | — |
| [SRC-01E35ABC46-L000482](../../tests/test_research_guardrails.py#L482) | 482 | `"def test_general_current_commercial_question_does_not_require_government_domain() -> None:"` | — |
| [SRC-01E35ABC46-L000483](../../tests/test_research_guardrails.py#L483) | 483 | `"    question = \"سعر الذهب اليوم في مصر\""` | — |
| [SRC-01E35ABC46-L000484](../../tests/test_research_guardrails.py#L484) | 484 | `"    candidates = [_guardrail_source(\"https://example.com/gold\")]"` | — |
| [SRC-01E35ABC46-L000485](../../tests/test_research_guardrails.py#L485) | 485 | `"    accepted, report = apply_source_guardrails("` | — |
| [SRC-01E35ABC46-L000486](../../tests/test_research_guardrails.py#L486) | 486 | `"        question, \"auto\", {\"freshness\": \"any\"}, candidates, now=_GUARDRAIL_NOW"` | — |
| [SRC-01E35ABC46-L000487](../../tests/test_research_guardrails.py#L487) | 487 | `"    )"` | — |
| [SRC-01E35ABC46-L000488](../../tests/test_research_guardrails.py#L488) | 488 | `"    assert accepted == candidates"` | — |
| [SRC-01E35ABC46-L000489](../../tests/test_research_guardrails.py#L489) | 489 | `"    assert report[\"official_government_domain_required\"] is False"` | — |
## اختبارات

### FILE-96F6863E3C — [tests/test_research_pipeline.py](../../tests/test_research_pipeline.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-96F6863E3C-L000001](../../tests/test_research_pipeline.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-96F6863E3C-L000002](../../tests/test_research_pipeline.py#L2) | 2 | `""` | — |
| [SRC-96F6863E3C-L000003](../../tests/test_research_pipeline.py#L3) | 3 | `"from agents.research_pipeline import build_research_pipeline"` | — |
| [SRC-96F6863E3C-L000004](../../tests/test_research_pipeline.py#L4) | 4 | `""` | — |
| [SRC-96F6863E3C-L000005](../../tests/test_research_pipeline.py#L5) | 5 | `""` | — |
| [SRC-96F6863E3C-L000006](../../tests/test_research_pipeline.py#L6) | 6 | `"def test_pipeline_unifies_intent_aspects_queries_and_evidence():"` | — |
| [SRC-96F6863E3C-L000007](../../tests/test_research_pipeline.py#L7) | 7 | `"    question = \"حلل السيارات الكهربائية في مصر من حيث السعر والبطارية والضمان\""` | — |
| [SRC-96F6863E3C-L000008](../../tests/test_research_pipeline.py#L8) | 8 | `"    sources = ["` | — |
| [SRC-96F6863E3C-L000009](../../tests/test_research_pipeline.py#L9) | 9 | `"        {"` | — |
| [SRC-96F6863E3C-L000010](../../tests/test_research_pipeline.py#L10) | 10 | `"            \"title\": \"أسعار السيارات الكهربائية في مصر\","` | — |
| [SRC-96F6863E3C-L000011](../../tests/test_research_pipeline.py#L11) | 11 | `"            \"url\": \"https://example.com/ev-prices\","` | — |
| [SRC-96F6863E3C-L000012](../../tests/test_research_pipeline.py#L12) | 12 | `"            \"snippet\": \"تفاصيل أسعار السيارات الكهربائية في مصر\","` | — |
| [SRC-96F6863E3C-L000013](../../tests/test_research_pipeline.py#L13) | 13 | `"            \"provider\": \"fixture\","` | — |
| [SRC-96F6863E3C-L000014](../../tests/test_research_pipeline.py#L14) | 14 | `"        }"` | — |
| [SRC-96F6863E3C-L000015](../../tests/test_research_pipeline.py#L15) | 15 | `"    ]"` | — |
| [SRC-96F6863E3C-L000016](../../tests/test_research_pipeline.py#L16) | 16 | `""` | — |
| [SRC-96F6863E3C-L000017](../../tests/test_research_pipeline.py#L17) | 17 | `"    result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000018](../../tests/test_research_pipeline.py#L18) | 18 | `"        question,"` | — |
| [SRC-96F6863E3C-L000019](../../tests/test_research_pipeline.py#L19) | 19 | `"        {\"queries\": [\"السيارات الكهربائية في مصر\"]},"` | — |
| [SRC-96F6863E3C-L000020](../../tests/test_research_pipeline.py#L20) | 20 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-96F6863E3C-L000021](../../tests/test_research_pipeline.py#L21) | 21 | `"        sources=sources,"` | — |
| [SRC-96F6863E3C-L000022](../../tests/test_research_pipeline.py#L22) | 22 | `"    )"` | — |
| [SRC-96F6863E3C-L000023](../../tests/test_research_pipeline.py#L23) | 23 | `""` | — |
| [SRC-96F6863E3C-L000024](../../tests/test_research_pipeline.py#L24) | 24 | `"    assert result[\"intent\"][\"route\"] == \"WEB_DEEP\""` | — |
| [SRC-96F6863E3C-L000025](../../tests/test_research_pipeline.py#L25) | 25 | `"    assert {\"السعر\", \"البطارية\", \"الضمان\"}.issubset(set(result[\"aspects\"]))"` | — |
| [SRC-96F6863E3C-L000026](../../tests/test_research_pipeline.py#L26) | 26 | `"    assert result[\"queries\"]"` | — |
| [SRC-96F6863E3C-L000027](../../tests/test_research_pipeline.py#L27) | 27 | `"    assert len(result[\"queries\"]) <= 8"` | — |
| [SRC-96F6863E3C-L000028](../../tests/test_research_pipeline.py#L28) | 28 | `"    assert result[\"evidence_ledger\"][\"aspects\"] == result[\"aspects\"]"` | — |
| [SRC-96F6863E3C-L000029](../../tests/test_research_pipeline.py#L29) | 29 | `"    assert result[\"evidence_ledger\"][\"missing\"]"` | — |
| [SRC-96F6863E3C-L000030](../../tests/test_research_pipeline.py#L30) | 30 | `"    assert result[\"stages\"][\"semantic_matching\"] == \"not_configured\""` | — |
| [SRC-96F6863E3C-L000031](../../tests/test_research_pipeline.py#L31) | 31 | `"    assert result[\"stages\"][\"claim_verification\"] == \"delegated_to_existing_validator\""` | — |
| [SRC-96F6863E3C-L000032](../../tests/test_research_pipeline.py#L32) | 32 | `""` | — |
| [SRC-96F6863E3C-L000033](../../tests/test_research_pipeline.py#L33) | 33 | `""` | — |
| [SRC-96F6863E3C-L000034](../../tests/test_research_pipeline.py#L34) | 34 | `"def test_pipeline_clarifies_elliptical_question_without_search_plan():"` | — |
| [SRC-96F6863E3C-L000035](../../tests/test_research_pipeline.py#L35) | 35 | `"    result = build_research_pipeline(\"كام سعرها؟\", {\"queries\": [\"كام سعرها\"]})"` | — |
| [SRC-96F6863E3C-L000036](../../tests/test_research_pipeline.py#L36) | 36 | `""` | — |
| [SRC-96F6863E3C-L000037](../../tests/test_research_pipeline.py#L37) | 37 | `"    assert result[\"intent\"][\"route\"] == \"CLARIFY\""` | — |
| [SRC-96F6863E3C-L000038](../../tests/test_research_pipeline.py#L38) | 38 | `"    assert result[\"intent\"][\"needs_clarification\"] is True"` | — |
| [SRC-96F6863E3C-L000039](../../tests/test_research_pipeline.py#L39) | 39 | `"    assert result[\"queries\"] == []"` | — |
| [SRC-96F6863E3C-L000040](../../tests/test_research_pipeline.py#L40) | 40 | `"    assert result[\"stages\"][\"query_planning\"] == \"blocked_pending_clarification\""` | — |
| [SRC-96F6863E3C-L000041](../../tests/test_research_pipeline.py#L41) | 41 | `""` | — |
| [SRC-96F6863E3C-L000042](../../tests/test_research_pipeline.py#L42) | 42 | `""` | — |
| [SRC-96F6863E3C-L000043](../../tests/test_research_pipeline.py#L43) | 43 | `"def test_pipeline_resolves_followup_using_latest_context_anchor():"` | — |
| [SRC-96F6863E3C-L000044](../../tests/test_research_pipeline.py#L44) | 44 | `"    history = ["` | — |
| [SRC-96F6863E3C-L000045](../../tests/test_research_pipeline.py#L45) | 45 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-96F6863E3C-L000046](../../tests/test_research_pipeline.py#L46) | 46 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن السعر.\"},"` | — |
| [SRC-96F6863E3C-L000047](../../tests/test_research_pipeline.py#L47) | 47 | `"    ]"` | — |
| [SRC-96F6863E3C-L000048](../../tests/test_research_pipeline.py#L48) | 48 | `""` | — |
| [SRC-96F6863E3C-L000049](../../tests/test_research_pipeline.py#L49) | 49 | `"    result = build_research_pipeline(\"والضمان؟\", {\"queries\": [\"iPhone 17 مصر\"]}, history=history)"` | — |
| [SRC-96F6863E3C-L000050](../../tests/test_research_pipeline.py#L50) | 50 | `""` | — |
| [SRC-96F6863E3C-L000051](../../tests/test_research_pipeline.py#L51) | 51 | `"    assert \"iPhone 17\" in result[\"contextual_question\"]"` | — |
| [SRC-96F6863E3C-L000052](../../tests/test_research_pipeline.py#L52) | 52 | `"    assert \"الضمان\" in result[\"contextual_question\"]"` | — |
| [SRC-96F6863E3C-L000053](../../tests/test_research_pipeline.py#L53) | 53 | `"    assert result[\"intent\"][\"context_available\"] is True"` | — |
| [SRC-96F6863E3C-L000054](../../tests/test_research_pipeline.py#L54) | 54 | `""` | — |
| [SRC-96F6863E3C-L000055](../../tests/test_research_pipeline.py#L55) | 55 | `""` | — |
| [SRC-96F6863E3C-L000056](../../tests/test_research_pipeline.py#L56) | 56 | `"def test_pipeline_bounds_malformed_inputs_and_keeps_semantic_stage_unassessed():"` | — |
| [SRC-96F6863E3C-L000057](../../tests/test_research_pipeline.py#L57) | 57 | `"    result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000058](../../tests/test_research_pipeline.py#L58) | 58 | `"        \"س\" * 9000,"` | — |
| [SRC-96F6863E3C-L000059](../../tests/test_research_pipeline.py#L59) | 59 | `"        {\"queries\": [\"س\" * 1000] * 20},"` | — |
| [SRC-96F6863E3C-L000060](../../tests/test_research_pipeline.py#L60) | 60 | `"        sources=[None, \"not-a-source\", {}],"` | — |
| [SRC-96F6863E3C-L000061](../../tests/test_research_pipeline.py#L61) | 61 | `"    )"` | — |
| [SRC-96F6863E3C-L000062](../../tests/test_research_pipeline.py#L62) | 62 | `""` | — |
| [SRC-96F6863E3C-L000063](../../tests/test_research_pipeline.py#L63) | 63 | `"    assert len(result[\"contextual_question\"]) <= 4000"` | — |
| [SRC-96F6863E3C-L000064](../../tests/test_research_pipeline.py#L64) | 64 | `"    assert len(result[\"queries\"]) <= 8"` | — |
| [SRC-96F6863E3C-L000065](../../tests/test_research_pipeline.py#L65) | 65 | `"    assert result[\"evidence_ledger\"][\"aspects\"] == []"` | — |
| [SRC-96F6863E3C-L000066](../../tests/test_research_pipeline.py#L66) | 66 | `"    assert result[\"stages\"][\"semantic_matching\"] == \"not_configured\""` | — |
| [SRC-96F6863E3C-L000067](../../tests/test_research_pipeline.py#L67) | 67 | `""` | — |
| [SRC-96F6863E3C-L000068](../../tests/test_research_pipeline.py#L68) | 68 | `""` | — |
| [SRC-96F6863E3C-L000069](../../tests/test_research_pipeline.py#L69) | 69 | `""` | — |
| [SRC-96F6863E3C-L000070](../../tests/test_research_pipeline.py#L70) | 70 | `"def test_optional_semantic_matcher_only_ranks_candidates_and_rejects_bad_scores():"` | — |
| [SRC-96F6863E3C-L000071](../../tests/test_research_pipeline.py#L71) | 71 | `"    calls = []"` | — |
| [SRC-96F6863E3C-L000072](../../tests/test_research_pipeline.py#L72) | 72 | `""` | — |
| [SRC-96F6863E3C-L000073](../../tests/test_research_pipeline.py#L73) | 73 | `"    def matcher(aspect, source):"` | — |
| [SRC-96F6863E3C-L000074](../../tests/test_research_pipeline.py#L74) | 74 | `"        calls.append((aspect, source.get(\"url\")))"` | — |
| [SRC-96F6863E3C-L000075](../../tests/test_research_pipeline.py#L75) | 75 | `"        return 0.9 if source.get(\"url\", \"\").endswith(\"/relevant\") else float(\"nan\")"` | — |
| [SRC-96F6863E3C-L000076](../../tests/test_research_pipeline.py#L76) | 76 | `""` | — |
| [SRC-96F6863E3C-L000077](../../tests/test_research_pipeline.py#L77) | 77 | `"    result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000078](../../tests/test_research_pipeline.py#L78) | 78 | `"        \"ما سعر الهاتف ومدة الضمان؟\","` | — |
| [SRC-96F6863E3C-L000079](../../tests/test_research_pipeline.py#L79) | 79 | `"        {\"queries\": [\"الهاتف\"]},"` | — |
| [SRC-96F6863E3C-L000080](../../tests/test_research_pipeline.py#L80) | 80 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-96F6863E3C-L000081](../../tests/test_research_pipeline.py#L81) | 81 | `"        sources=["` | — |
| [SRC-96F6863E3C-L000082](../../tests/test_research_pipeline.py#L82) | 82 | `"            {\"title\": \"سعر الهاتف\", \"url\": \"https://example.com/relevant\", \"snippet\": \"السعر\"},"` | — |
| [SRC-96F6863E3C-L000083](../../tests/test_research_pipeline.py#L83) | 83 | `"            {\"title\": \"صفحة أخرى\", \"url\": \"https://example.com/other\", \"snippet\": \"عام\"},"` | — |
| [SRC-96F6863E3C-L000084](../../tests/test_research_pipeline.py#L84) | 84 | `"        ],"` | — |
| [SRC-96F6863E3C-L000085](../../tests/test_research_pipeline.py#L85) | 85 | `"        semantic_matcher=matcher,"` | — |
| [SRC-96F6863E3C-L000086](../../tests/test_research_pipeline.py#L86) | 86 | `"    )"` | — |
| [SRC-96F6863E3C-L000087](../../tests/test_research_pipeline.py#L87) | 87 | `""` | — |
| [SRC-96F6863E3C-L000088](../../tests/test_research_pipeline.py#L88) | 88 | `"    assert result[\"evidence\"][\"semantic_matching\"][\"status\"] == \"evaluated\""` | — |
| [SRC-96F6863E3C-L000089](../../tests/test_research_pipeline.py#L89) | 89 | `"    assert len(calls) == len(result[\"aspects\"]) * 2"` | — |
| [SRC-96F6863E3C-L000090](../../tests/test_research_pipeline.py#L90) | 90 | `"    for candidates in result[\"evidence\"][\"semantic_matching\"][\"candidates\"].values():"` | — |
| [SRC-96F6863E3C-L000091](../../tests/test_research_pipeline.py#L91) | 91 | `"        assert all(0.0 <= item[\"score\"] <= 1.0 for item in candidates)"` | — |
| [SRC-96F6863E3C-L000092](../../tests/test_research_pipeline.py#L92) | 92 | `"    # A semantic relevance score never promotes an aspect into the lexical evidence ledger."` | — |
| [SRC-96F6863E3C-L000093](../../tests/test_research_pipeline.py#L93) | 93 | `"    assert result[\"evidence\"][\"lexical_ledger\"][\"covered\"] != result[\"aspects\"]"` | — |
| [SRC-96F6863E3C-L000094](../../tests/test_research_pipeline.py#L94) | 94 | `""` | — |
| [SRC-96F6863E3C-L000095](../../tests/test_research_pipeline.py#L95) | 95 | `""` | — |
| [SRC-96F6863E3C-L000096](../../tests/test_research_pipeline.py#L96) | 96 | `"def test_fallback_plan_exposes_same_unified_pipeline_contract():"` | — |
| [SRC-96F6863E3C-L000097](../../tests/test_research_pipeline.py#L97) | 97 | `"    from agents.research import fallback_plan"` | — |
| [SRC-96F6863E3C-L000098](../../tests/test_research_pipeline.py#L98) | 98 | `""` | — |
| [SRC-96F6863E3C-L000099](../../tests/test_research_pipeline.py#L99) | 99 | `"    plan = fallback_plan(\"حلل السيارات الكهربائية في مصر من حيث السعر والضمان\")"` | — |
| [SRC-96F6863E3C-L000100](../../tests/test_research_pipeline.py#L100) | 100 | `""` | — |
| [SRC-96F6863E3C-L000101](../../tests/test_research_pipeline.py#L101) | 101 | `"    assert plan[\"research_pipeline\"][\"aspects\"]"` | — |
| [SRC-96F6863E3C-L000102](../../tests/test_research_pipeline.py#L102) | 102 | `"    assert plan[\"research_pipeline\"][\"stages\"][\"query_planning\"] == \"completed\""` | — |
| [SRC-96F6863E3C-L000103](../../tests/test_research_pipeline.py#L103) | 103 | `"    assert plan[\"query_strategy_matrix\"]"` | — |
| [SRC-96F6863E3C-L000104](../../tests/test_research_pipeline.py#L104) | 104 | `""` | — |
| [SRC-96F6863E3C-L000105](../../tests/test_research_pipeline.py#L105) | 105 | `""` | — |
| [SRC-96F6863E3C-L000106](../../tests/test_research_pipeline.py#L106) | 106 | `"def test_semantic_matcher_failure_is_degraded_without_aborting_pipeline():"` | — |
| [SRC-96F6863E3C-L000107](../../tests/test_research_pipeline.py#L107) | 107 | `"    result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000108](../../tests/test_research_pipeline.py#L108) | 108 | `"        \"ما سعر الهاتف ومدة الضمان؟\","` | — |
| [SRC-96F6863E3C-L000109](../../tests/test_research_pipeline.py#L109) | 109 | `"        {\"queries\": [\"الهاتف\"]},"` | — |
| [SRC-96F6863E3C-L000110](../../tests/test_research_pipeline.py#L110) | 110 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-96F6863E3C-L000111](../../tests/test_research_pipeline.py#L111) | 111 | `"        sources=[{\"title\": \"سعر الهاتف\", \"url\": \"https://example.com\"}],"` | — |
| [SRC-96F6863E3C-L000112](../../tests/test_research_pipeline.py#L112) | 112 | `"        semantic_matcher=lambda _aspect, _source: (_ for _ in ()).throw(RuntimeError(\"model timeout\")),"` | — |
| [SRC-96F6863E3C-L000113](../../tests/test_research_pipeline.py#L113) | 113 | `"    )"` | — |
| [SRC-96F6863E3C-L000114](../../tests/test_research_pipeline.py#L114) | 114 | `""` | — |
| [SRC-96F6863E3C-L000115](../../tests/test_research_pipeline.py#L115) | 115 | `"    assert result[\"stages\"][\"semantic_matching\"] == \"degraded\""` | — |
| [SRC-96F6863E3C-L000116](../../tests/test_research_pipeline.py#L116) | 116 | `"    assert result[\"evidence\"][\"semantic_matching\"][\"errors\"] == len(result[\"aspects\"])"` | — |
| [SRC-96F6863E3C-L000117](../../tests/test_research_pipeline.py#L117) | 117 | `"    assert result[\"evidence\"][\"lexical_ledger\"][\"aspects\"] == result[\"aspects\"]"` | — |
| [SRC-96F6863E3C-L000118](../../tests/test_research_pipeline.py#L118) | 118 | `""` | — |
| [SRC-96F6863E3C-L000119](../../tests/test_research_pipeline.py#L119) | 119 | `""` | — |
| [SRC-96F6863E3C-L000120](../../tests/test_research_pipeline.py#L120) | 120 | `""` | — |
| [SRC-96F6863E3C-L000121](../../tests/test_research_pipeline.py#L121) | 121 | `"def test_pipeline_preserves_planner_depth_and_freshness_metadata():"` | — |
| [SRC-96F6863E3C-L000122](../../tests/test_research_pipeline.py#L122) | 122 | `"    result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000123](../../tests/test_research_pipeline.py#L123) | 123 | `"        \"قارن السيارات الكهربائية في مصر من حيث السعر والبطارية\","` | — |
| [SRC-96F6863E3C-L000124](../../tests/test_research_pipeline.py#L124) | 124 | `"        {"` | — |
| [SRC-96F6863E3C-L000125](../../tests/test_research_pipeline.py#L125) | 125 | `"            \"queries\": [\"السيارات الكهربائية في مصر\"],"` | — |
| [SRC-96F6863E3C-L000126](../../tests/test_research_pipeline.py#L126) | 126 | `"            \"depth\": \"deep\","` | — |
| [SRC-96F6863E3C-L000127](../../tests/test_research_pipeline.py#L127) | 127 | `"            \"freshness\": \"current\","` | — |
| [SRC-96F6863E3C-L000128](../../tests/test_research_pipeline.py#L128) | 128 | `"        },"` | — |
| [SRC-96F6863E3C-L000129](../../tests/test_research_pipeline.py#L129) | 129 | `"        mode=\"deep\","` | — |
| [SRC-96F6863E3C-L000130](../../tests/test_research_pipeline.py#L130) | 130 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-96F6863E3C-L000131](../../tests/test_research_pipeline.py#L131) | 131 | `"    )"` | — |
| [SRC-96F6863E3C-L000132](../../tests/test_research_pipeline.py#L132) | 132 | `""` | — |
| [SRC-96F6863E3C-L000133](../../tests/test_research_pipeline.py#L133) | 133 | `"    assert result[\"task_spec\"][\"planner_depth\"] == \"deep\""` | — |
| [SRC-96F6863E3C-L000134](../../tests/test_research_pipeline.py#L134) | 134 | `"    assert result[\"task_spec\"][\"planner_freshness\"] == \"current\""` | — |
| [SRC-96F6863E3C-L000135](../../tests/test_research_pipeline.py#L135) | 135 | `""` | — |
| [SRC-96F6863E3C-L000136](../../tests/test_research_pipeline.py#L136) | 136 | `""` | — |
| [SRC-96F6863E3C-L000137](../../tests/test_research_pipeline.py#L137) | 137 | `"def test_pipeline_blocks_official_site_search_when_target_entity_is_missing():"` | — |
| [SRC-96F6863E3C-L000138](../../tests/test_research_pipeline.py#L138) | 138 | `"    result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000139](../../tests/test_research_pipeline.py#L139) | 139 | `"        \"هات الموقع الرسمي\","` | — |
| [SRC-96F6863E3C-L000140](../../tests/test_research_pipeline.py#L140) | 140 | `"        {\"queries\": [\"الموقع الرسمي\"]},"` | — |
| [SRC-96F6863E3C-L000141](../../tests/test_research_pipeline.py#L141) | 141 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-96F6863E3C-L000142](../../tests/test_research_pipeline.py#L142) | 142 | `"    )"` | — |
| [SRC-96F6863E3C-L000143](../../tests/test_research_pipeline.py#L143) | 143 | `""` | — |
| [SRC-96F6863E3C-L000144](../../tests/test_research_pipeline.py#L144) | 144 | `"    assert result[\"task_spec\"][\"requires_clarification\"] is True"` | — |
| [SRC-96F6863E3C-L000145](../../tests/test_research_pipeline.py#L145) | 145 | `"    assert result[\"intent\"][\"needs_clarification\"] is True"` | — |
| [SRC-96F6863E3C-L000146](../../tests/test_research_pipeline.py#L146) | 146 | `"    assert result[\"queries\"] == []"` | — |
| [SRC-96F6863E3C-L000147](../../tests/test_research_pipeline.py#L147) | 147 | `"    assert result[\"stages\"][\"query_planning\"] == \"blocked_pending_clarification\""` | — |
| [SRC-96F6863E3C-L000148](../../tests/test_research_pipeline.py#L148) | 148 | `""` | — |
| [SRC-96F6863E3C-L000149](../../tests/test_research_pipeline.py#L149) | 149 | `"def test_pipeline_marks_upstream_dialogue_context_resolution_as_completed():"` | — |
| [SRC-96F6863E3C-L000150](../../tests/test_research_pipeline.py#L150) | 150 | `"    result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000151](../../tests/test_research_pipeline.py#L151) | 151 | `"        \"والضمان؟\","` | — |
| [SRC-96F6863E3C-L000152](../../tests/test_research_pipeline.py#L152) | 152 | `"        {\"queries\": [\"iPhone 17 warranty Egypt\"]},"` | — |
| [SRC-96F6863E3C-L000153](../../tests/test_research_pipeline.py#L153) | 153 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-96F6863E3C-L000154](../../tests/test_research_pipeline.py#L154) | 154 | `"        dialogue_context={"` | — |
| [SRC-96F6863E3C-L000155](../../tests/test_research_pipeline.py#L155) | 155 | `"            \"method\": \"llm_semantic_context\","` | — |
| [SRC-96F6863E3C-L000156](../../tests/test_research_pipeline.py#L156) | 156 | `"            \"resolved_question\": \"ما ضمان iPhone 17 في مصر؟\","` | — |
| [SRC-96F6863E3C-L000157](../../tests/test_research_pipeline.py#L157) | 157 | `"            \"topic\": \"iPhone 17\","` | — |
| [SRC-96F6863E3C-L000158](../../tests/test_research_pipeline.py#L158) | 158 | `"            \"is_follow_up\": True,"` | — |
| [SRC-96F6863E3C-L000159](../../tests/test_research_pipeline.py#L159) | 159 | `"            \"topic_shift\": False,"` | — |
| [SRC-96F6863E3C-L000160](../../tests/test_research_pipeline.py#L160) | 160 | `"        },"` | — |
| [SRC-96F6863E3C-L000161](../../tests/test_research_pipeline.py#L161) | 161 | `"    )"` | — |
| [SRC-96F6863E3C-L000162](../../tests/test_research_pipeline.py#L162) | 162 | `""` | — |
| [SRC-96F6863E3C-L000163](../../tests/test_research_pipeline.py#L163) | 163 | `"    assert result[\"contextual_question\"] == \"ما ضمان iPhone 17 في مصر؟\""` | — |
| [SRC-96F6863E3C-L000164](../../tests/test_research_pipeline.py#L164) | 164 | `"    assert result[\"task_spec\"][\"context_resolution\"][\"resolved_question\"] == ("` | — |
| [SRC-96F6863E3C-L000165](../../tests/test_research_pipeline.py#L165) | 165 | `"        \"ما ضمان iPhone 17 في مصر؟\""` | — |
| [SRC-96F6863E3C-L000166](../../tests/test_research_pipeline.py#L166) | 166 | `"    )"` | — |
| [SRC-96F6863E3C-L000167](../../tests/test_research_pipeline.py#L167) | 167 | `"    assert result[\"stages\"][\"context_resolution\"] == \"completed\""` | — |
| [SRC-96F6863E3C-L000168](../../tests/test_research_pipeline.py#L168) | 168 | `"    assert result[\"intent\"][\"context_available\"] is True"` | — |
| [SRC-96F6863E3C-L000169](../../tests/test_research_pipeline.py#L169) | 169 | `"    assert result[\"query_strategy_matrix\"]"` | — |
| [SRC-96F6863E3C-L000170](../../tests/test_research_pipeline.py#L170) | 170 | `"    assert all(\"iPhone 17\" in item[\"query\"] for item in result[\"query_strategy_matrix\"])"` | — |
| [SRC-96F6863E3C-L000171](../../tests/test_research_pipeline.py#L171) | 171 | `""` | — |
| [SRC-96F6863E3C-L000172](../../tests/test_research_pipeline.py#L172) | 172 | `"def test_pipeline_does_not_reuse_resolved_question_after_explicit_topic_shift():"` | — |
| [SRC-96F6863E3C-L000173](../../tests/test_research_pipeline.py#L173) | 173 | `"    result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000174](../../tests/test_research_pipeline.py#L174) | 174 | `"        \"ما سعر سامسونج S26؟\","` | — |
| [SRC-96F6863E3C-L000175](../../tests/test_research_pipeline.py#L175) | 175 | `"        {\"queries\": [\"سعر سامسونج S26\"]},"` | — |
| [SRC-96F6863E3C-L000176](../../tests/test_research_pipeline.py#L176) | 176 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-96F6863E3C-L000177](../../tests/test_research_pipeline.py#L177) | 177 | `"        dialogue_context={"` | — |
| [SRC-96F6863E3C-L000178](../../tests/test_research_pipeline.py#L178) | 178 | `"            \"resolved_question\": \"ما ضمان iPhone 17 في مصر؟\","` | — |
| [SRC-96F6863E3C-L000179](../../tests/test_research_pipeline.py#L179) | 179 | `"            \"topic_shift\": True,"` | — |
| [SRC-96F6863E3C-L000180](../../tests/test_research_pipeline.py#L180) | 180 | `"        },"` | — |
| [SRC-96F6863E3C-L000181](../../tests/test_research_pipeline.py#L181) | 181 | `"    )"` | — |
| [SRC-96F6863E3C-L000182](../../tests/test_research_pipeline.py#L182) | 182 | `""` | — |
| [SRC-96F6863E3C-L000183](../../tests/test_research_pipeline.py#L183) | 183 | `"    assert result[\"contextual_question\"] == \"ما سعر سامسونج S26؟\""` | — |
| [SRC-96F6863E3C-L000184](../../tests/test_research_pipeline.py#L184) | 184 | `"    assert result[\"task_spec\"][\"context_resolution\"][\"resolved_question\"] == ("` | — |
| [SRC-96F6863E3C-L000185](../../tests/test_research_pipeline.py#L185) | 185 | `"        \"ما سعر سامسونج S26؟\""` | — |
| [SRC-96F6863E3C-L000186](../../tests/test_research_pipeline.py#L186) | 186 | `"    )"` | — |
| [SRC-96F6863E3C-L000187](../../tests/test_research_pipeline.py#L187) | 187 | `""` | — |
| [SRC-96F6863E3C-L000188](../../tests/test_research_pipeline.py#L188) | 188 | `"def test_pipeline_does_not_claim_context_resolution_for_unstructured_metadata():"` | — |
| [SRC-96F6863E3C-L000189](../../tests/test_research_pipeline.py#L189) | 189 | `"    result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000190](../../tests/test_research_pipeline.py#L190) | 190 | `"        \"ما سعر الهاتف؟\","` | — |
| [SRC-96F6863E3C-L000191](../../tests/test_research_pipeline.py#L191) | 191 | `"        {\"queries\": [\"سعر الهاتف\"]},"` | — |
| [SRC-96F6863E3C-L000192](../../tests/test_research_pipeline.py#L192) | 192 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-96F6863E3C-L000193](../../tests/test_research_pipeline.py#L193) | 193 | `"        dialogue_context={\"trace_label\": \"upstream_metadata_only\"},"` | — |
| [SRC-96F6863E3C-L000194](../../tests/test_research_pipeline.py#L194) | 194 | `"    )"` | — |
| [SRC-96F6863E3C-L000195](../../tests/test_research_pipeline.py#L195) | 195 | `""` | — |
| [SRC-96F6863E3C-L000196](../../tests/test_research_pipeline.py#L196) | 196 | `"    assert result[\"stages\"][\"context_resolution\"] == \"not_needed\""` | — |
| [SRC-96F6863E3C-L000197](../../tests/test_research_pipeline.py#L197) | 197 | `""` | — |
| [SRC-96F6863E3C-L000198](../../tests/test_research_pipeline.py#L198) | 198 | `"def test_pipeline_does_not_claim_lexical_matching_without_readable_source_text():"` | — |
| [SRC-96F6863E3C-L000199](../../tests/test_research_pipeline.py#L199) | 199 | `"    for sources in ("` | — |
| [SRC-96F6863E3C-L000200](../../tests/test_research_pipeline.py#L200) | 200 | `"        [None, \"not-a-source\", {}],"` | — |
| [SRC-96F6863E3C-L000201](../../tests/test_research_pipeline.py#L201) | 201 | `"        [{\"url\": \"https://example.com/no-text\"}],"` | — |
| [SRC-96F6863E3C-L000202](../../tests/test_research_pipeline.py#L202) | 202 | `"        [],"` | — |
| [SRC-96F6863E3C-L000203](../../tests/test_research_pipeline.py#L203) | 203 | `"    ):"` | — |
| [SRC-96F6863E3C-L000204](../../tests/test_research_pipeline.py#L204) | 204 | `"        result = build_research_pipeline("` | — |
| [SRC-96F6863E3C-L000205](../../tests/test_research_pipeline.py#L205) | 205 | `"            \"ما سعر الهاتف والضمان؟\","` | — |
| [SRC-96F6863E3C-L000206](../../tests/test_research_pipeline.py#L206) | 206 | `"            {\"queries\": [\"سعر الهاتف والضمان\"]},"` | — |
| [SRC-96F6863E3C-L000207](../../tests/test_research_pipeline.py#L207) | 207 | `"            intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-96F6863E3C-L000208](../../tests/test_research_pipeline.py#L208) | 208 | `"            sources=sources,"` | — |
| [SRC-96F6863E3C-L000209](../../tests/test_research_pipeline.py#L209) | 209 | `"        )"` | — |
| [SRC-96F6863E3C-L000210](../../tests/test_research_pipeline.py#L210) | 210 | `""` | — |
| [SRC-96F6863E3C-L000211](../../tests/test_research_pipeline.py#L211) | 211 | `"        assert result[\"stages\"][\"lexical_matching\"] == \"not_assessed\""` | — |
| [SRC-96F6863E3C-L000212](../../tests/test_research_pipeline.py#L212) | 212 | `"        assert result[\"evidence_ledger\"][\"covered\"] == []"` | — |
## اختبارات

### FILE-2614DCB6FB — [tests/test_search_code.py](../../tests/test_search_code.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2614DCB6FB-L000001](../../tests/test_search_code.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-2614DCB6FB-L000002](../../tests/test_search_code.py#L2) | 2 | `""` | — |
| [SRC-2614DCB6FB-L000003](../../tests/test_search_code.py#L3) | 3 | `"import importlib.util"` | — |
| [SRC-2614DCB6FB-L000004](../../tests/test_search_code.py#L4) | 4 | `"import re"` | — |
| [SRC-2614DCB6FB-L000005](../../tests/test_search_code.py#L5) | 5 | `"import sys"` | — |
| [SRC-2614DCB6FB-L000006](../../tests/test_search_code.py#L6) | 6 | `"from pathlib import Path"` | — |
| [SRC-2614DCB6FB-L000007](../../tests/test_search_code.py#L7) | 7 | `""` | — |
| [SRC-2614DCB6FB-L000008](../../tests/test_search_code.py#L8) | 8 | `"SEARCH_PATH = Path(__file__).resolve().parents[1] / \"docs\" / \"search_code.py\""` | — |
| [SRC-2614DCB6FB-L000009](../../tests/test_search_code.py#L9) | 9 | `"SEARCH_SPEC = importlib.util.spec_from_file_location(\"omarai_search_code_for_tests\", SEARCH_PATH)"` | — |
| [SRC-2614DCB6FB-L000010](../../tests/test_search_code.py#L10) | 10 | `"assert SEARCH_SPEC is not None"` | — |
| [SRC-2614DCB6FB-L000011](../../tests/test_search_code.py#L11) | 11 | `"assert SEARCH_SPEC.loader is not None"` | — |
| [SRC-2614DCB6FB-L000012](../../tests/test_search_code.py#L12) | 12 | `"SEARCH = importlib.util.module_from_spec(SEARCH_SPEC)"` | — |
| [SRC-2614DCB6FB-L000013](../../tests/test_search_code.py#L13) | 13 | `"sys.modules[SEARCH_SPEC.name] = SEARCH"` | — |
| [SRC-2614DCB6FB-L000014](../../tests/test_search_code.py#L14) | 14 | `"SEARCH_SPEC.loader.exec_module(SEARCH)"` | — |
| [SRC-2614DCB6FB-L000015](../../tests/test_search_code.py#L15) | 15 | `""` | — |
| [SRC-2614DCB6FB-L000016](../../tests/test_search_code.py#L16) | 16 | `""` | — |
| [SRC-2614DCB6FB-L000017](../../tests/test_search_code.py#L17) | 17 | `"def test_search_returns_stable_file_line_and_source_link(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000018](../../tests/test_search_code.py#L18) | 18 | `"    \"\"\"Text search returns the exact file and 1-based line without network access.\"\"\""` | — |
| [SRC-2614DCB6FB-L000019](../../tests/test_search_code.py#L19) | 19 | `"    source = tmp_path / \"app.py\""` | — |
| [SRC-2614DCB6FB-L000020](../../tests/test_search_code.py#L20) | 20 | `"    source.write_text(\"first = 1\\nneedle = 2\\nlast = 3\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000021](../../tests/test_search_code.py#L21) | 21 | `""` | — |
| [SRC-2614DCB6FB-L000022](../../tests/test_search_code.py#L22) | 22 | `"    hits = SEARCH.search_repository(tmp_path, \"needle\")"` | — |
| [SRC-2614DCB6FB-L000023](../../tests/test_search_code.py#L23) | 23 | `""` | — |
| [SRC-2614DCB6FB-L000024](../../tests/test_search_code.py#L24) | 24 | `"    assert len(hits) == 1"` | — |
| [SRC-2614DCB6FB-L000025](../../tests/test_search_code.py#L25) | 25 | `"    assert hits[0].file == \"app.py\""` | — |
| [SRC-2614DCB6FB-L000026](../../tests/test_search_code.py#L26) | 26 | `"    assert hits[0].line == 2"` | — |
| [SRC-2614DCB6FB-L000027](../../tests/test_search_code.py#L27) | 27 | `"    assert \"needle = 2\" in hits[0].text"` | — |
| [SRC-2614DCB6FB-L000028](../../tests/test_search_code.py#L28) | 28 | `"    assert hits[0].link.endswith(\"/app.py#L2\")"` | — |
| [SRC-2614DCB6FB-L000029](../../tests/test_search_code.py#L29) | 29 | `""` | — |
| [SRC-2614DCB6FB-L000030](../../tests/test_search_code.py#L30) | 30 | `""` | — |
| [SRC-2614DCB6FB-L000031](../../tests/test_search_code.py#L31) | 31 | `"def test_search_supports_multiline_context_and_regex(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000032](../../tests/test_search_code.py#L32) | 32 | `"    \"\"\"The context argument returns the requested number of adjacent lines.\"\"\""` | — |
| [SRC-2614DCB6FB-L000033](../../tests/test_search_code.py#L33) | 33 | `"    source = tmp_path / \"app.py\""` | — |
| [SRC-2614DCB6FB-L000034](../../tests/test_search_code.py#L34) | 34 | `"    source.write_text(\"before one\\nbefore two\\nVALUE_42 = 7\\nafter one\\nafter two\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000035](../../tests/test_search_code.py#L35) | 35 | `""` | — |
| [SRC-2614DCB6FB-L000036](../../tests/test_search_code.py#L36) | 36 | `"    hits = SEARCH.search_repository("` | — |
| [SRC-2614DCB6FB-L000037](../../tests/test_search_code.py#L37) | 37 | `"        tmp_path, r\"VALUE_\\d+\", use_regex=True, context=2"` | — |
| [SRC-2614DCB6FB-L000038](../../tests/test_search_code.py#L38) | 38 | `"    )"` | — |
| [SRC-2614DCB6FB-L000039](../../tests/test_search_code.py#L39) | 39 | `""` | — |
| [SRC-2614DCB6FB-L000040](../../tests/test_search_code.py#L40) | 40 | `"    assert len(hits) == 1"` | — |
| [SRC-2614DCB6FB-L000041](../../tests/test_search_code.py#L41) | 41 | `"    assert hits[0].context_before.splitlines() == [\"before one\", \"before two\"]"` | — |
| [SRC-2614DCB6FB-L000042](../../tests/test_search_code.py#L42) | 42 | `"    assert hits[0].context_after.splitlines() == [\"after one\", \"after two\"]"` | — |
| [SRC-2614DCB6FB-L000043](../../tests/test_search_code.py#L43) | 43 | `""` | — |
| [SRC-2614DCB6FB-L000044](../../tests/test_search_code.py#L44) | 44 | `""` | — |
| [SRC-2614DCB6FB-L000045](../../tests/test_search_code.py#L45) | 45 | `"def test_search_excludes_common_secret_files_and_runtime_directories(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000046](../../tests/test_search_code.py#L46) | 46 | `"    \"\"\"Local searches skip common secret paths and binary/runtime data.\"\"\""` | — |
| [SRC-2614DCB6FB-L000047](../../tests/test_search_code.py#L47) | 47 | `"    (tmp_path / \"app.py\").write_text(\"safe_value = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000048](../../tests/test_search_code.py#L48) | 48 | `"    (tmp_path / \".env\").write_text(\"TOKEN=private-value\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000049](../../tests/test_search_code.py#L49) | 49 | `"    (tmp_path / \"credentials.json\").write_text('{\"token\":\"private-value\"}\\n', encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000050](../../tests/test_search_code.py#L50) | 50 | `"    aws_dir = tmp_path / \".aws\""` | — |
| [SRC-2614DCB6FB-L000051](../../tests/test_search_code.py#L51) | 51 | `"    aws_dir.mkdir()"` | — |
| [SRC-2614DCB6FB-L000052](../../tests/test_search_code.py#L52) | 52 | `"    (aws_dir / \"credentials\").write_text(\"token=private-value\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000053](../../tests/test_search_code.py#L53) | 53 | `"    data_dir = tmp_path / \"data\""` | — |
| [SRC-2614DCB6FB-L000054](../../tests/test_search_code.py#L54) | 54 | `"    data_dir.mkdir()"` | — |
| [SRC-2614DCB6FB-L000055](../../tests/test_search_code.py#L55) | 55 | `"    (data_dir / \"records.sqlite3\").write_bytes(b\"database-token\")"` | — |
| [SRC-2614DCB6FB-L000056](../../tests/test_search_code.py#L56) | 56 | `"    (tmp_path / \"credentials.example\").write_text(\"TOKEN=replace-me\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000057](../../tests/test_search_code.py#L57) | 57 | `""` | — |
| [SRC-2614DCB6FB-L000058](../../tests/test_search_code.py#L58) | 58 | `"    hits = SEARCH.search_repository(tmp_path, \"private-value\")"` | — |
| [SRC-2614DCB6FB-L000059](../../tests/test_search_code.py#L59) | 59 | `"    safe_example = SEARCH.search_repository(tmp_path, \"replace-me\")"` | — |
| [SRC-2614DCB6FB-L000060](../../tests/test_search_code.py#L60) | 60 | `""` | — |
| [SRC-2614DCB6FB-L000061](../../tests/test_search_code.py#L61) | 61 | `"    assert hits == []"` | — |
| [SRC-2614DCB6FB-L000062](../../tests/test_search_code.py#L62) | 62 | `"    assert len(safe_example) == 1"` | — |
| [SRC-2614DCB6FB-L000063](../../tests/test_search_code.py#L63) | 63 | `"    assert safe_example[0].file == \"credentials.example\""` | — |
| [SRC-2614DCB6FB-L000064](../../tests/test_search_code.py#L64) | 64 | `""` | — |
| [SRC-2614DCB6FB-L000065](../../tests/test_search_code.py#L65) | 65 | `""` | — |
| [SRC-2614DCB6FB-L000066](../../tests/test_search_code.py#L66) | 66 | `"def test_search_validates_query_limits_and_reports_invalid_regex(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000067](../../tests/test_search_code.py#L67) | 67 | `"    \"\"\"Invalid search controls fail clearly instead of silently returning confusing results.\"\"\""` | — |
| [SRC-2614DCB6FB-L000068](../../tests/test_search_code.py#L68) | 68 | `"    try:"` | — |
| [SRC-2614DCB6FB-L000069](../../tests/test_search_code.py#L69) | 69 | `"        SEARCH.search_repository(tmp_path, \"\")"` | — |
| [SRC-2614DCB6FB-L000070](../../tests/test_search_code.py#L70) | 70 | `"    except ValueError as exc:"` | — |
| [SRC-2614DCB6FB-L000071](../../tests/test_search_code.py#L71) | 71 | `"        assert \"فارغ\" in str(exc)"` | — |
| [SRC-2614DCB6FB-L000072](../../tests/test_search_code.py#L72) | 72 | `"    else:"` | — |
| [SRC-2614DCB6FB-L000073](../../tests/test_search_code.py#L73) | 73 | `"        raise AssertionError(\"An empty search query should be rejected.\")"` | — |
| [SRC-2614DCB6FB-L000074](../../tests/test_search_code.py#L74) | 74 | `""` | — |
| [SRC-2614DCB6FB-L000075](../../tests/test_search_code.py#L75) | 75 | `"    for kwargs in ({\"max_results\": 0}, {\"context\": -1}):"` | — |
| [SRC-2614DCB6FB-L000076](../../tests/test_search_code.py#L76) | 76 | `"        try:"` | — |
| [SRC-2614DCB6FB-L000077](../../tests/test_search_code.py#L77) | 77 | `"            SEARCH.search_repository(tmp_path, \"needle\", **kwargs)"` | — |
| [SRC-2614DCB6FB-L000078](../../tests/test_search_code.py#L78) | 78 | `"        except ValueError:"` | — |
| [SRC-2614DCB6FB-L000079](../../tests/test_search_code.py#L79) | 79 | `"            continue"` | — |
| [SRC-2614DCB6FB-L000080](../../tests/test_search_code.py#L80) | 80 | `"        raise AssertionError(f\"Invalid search limits should be rejected: {kwargs}\")"` | — |
| [SRC-2614DCB6FB-L000081](../../tests/test_search_code.py#L81) | 81 | `""` | — |
| [SRC-2614DCB6FB-L000082](../../tests/test_search_code.py#L82) | 82 | `"    try:"` | — |
| [SRC-2614DCB6FB-L000083](../../tests/test_search_code.py#L83) | 83 | `"        SEARCH.search_repository(tmp_path, \"(\", use_regex=True)"` | — |
| [SRC-2614DCB6FB-L000084](../../tests/test_search_code.py#L84) | 84 | `"    except re.error:"` | — |
| [SRC-2614DCB6FB-L000085](../../tests/test_search_code.py#L85) | 85 | `"        pass"` | — |
| [SRC-2614DCB6FB-L000086](../../tests/test_search_code.py#L86) | 86 | `"    else:"` | — |
| [SRC-2614DCB6FB-L000087](../../tests/test_search_code.py#L87) | 87 | `"        raise AssertionError(\"An invalid regular expression should be rejected.\")"` | — |
| [SRC-2614DCB6FB-L000088](../../tests/test_search_code.py#L88) | 88 | `""` | — |
| [SRC-2614DCB6FB-L000089](../../tests/test_search_code.py#L89) | 89 | `"def test_search_links_use_the_requested_revision_not_main(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000090](../../tests/test_search_code.py#L90) | 90 | `"    source = tmp_path / \"app.py\""` | — |
| [SRC-2614DCB6FB-L000091](../../tests/test_search_code.py#L91) | 91 | `"    source.write_text(\"needle = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000092](../../tests/test_search_code.py#L92) | 92 | `""` | — |
| [SRC-2614DCB6FB-L000093](../../tests/test_search_code.py#L93) | 93 | `"    hits = SEARCH.search_repository("` | — |
| [SRC-2614DCB6FB-L000094](../../tests/test_search_code.py#L94) | 94 | `"        tmp_path, \"needle\", repository_ref=\"fix/review-branch\""` | — |
| [SRC-2614DCB6FB-L000095](../../tests/test_search_code.py#L95) | 95 | `"    )"` | — |
| [SRC-2614DCB6FB-L000096](../../tests/test_search_code.py#L96) | 96 | `""` | — |
| [SRC-2614DCB6FB-L000097](../../tests/test_search_code.py#L97) | 97 | `"    assert len(hits) == 1"` | — |
| [SRC-2614DCB6FB-L000098](../../tests/test_search_code.py#L98) | 98 | `"    assert hits[0].link == ("` | — |
| [SRC-2614DCB6FB-L000099](../../tests/test_search_code.py#L99) | 99 | `"        \"https://github.com/mosabosama2030-oss/omarai/\""` | — |
| [SRC-2614DCB6FB-L000100](../../tests/test_search_code.py#L100) | 100 | `"        \"blob/fix/review-branch/app.py#L1\""` | — |
| [SRC-2614DCB6FB-L000101](../../tests/test_search_code.py#L101) | 101 | `"    )"` | — |
| [SRC-2614DCB6FB-L000102](../../tests/test_search_code.py#L102) | 102 | `""` | — |
| [SRC-2614DCB6FB-L000103](../../tests/test_search_code.py#L103) | 103 | `""` | — |
| [SRC-2614DCB6FB-L000104](../../tests/test_search_code.py#L104) | 104 | `"def test_default_repository_ref_prefers_explicit_environment_override("` | — |
| [SRC-2614DCB6FB-L000105](../../tests/test_search_code.py#L105) | 105 | `"    monkeypatch, tmp_path: Path"` | — |
| [SRC-2614DCB6FB-L000106](../../tests/test_search_code.py#L106) | 106 | `") -> None:"` | — |
| [SRC-2614DCB6FB-L000107](../../tests/test_search_code.py#L107) | 107 | `"    monkeypatch.setenv(\"OMARAI_GITHUB_REF\", \"feature/current-review\")"` | — |
| [SRC-2614DCB6FB-L000108](../../tests/test_search_code.py#L108) | 108 | `"    monkeypatch.setenv(\"GITHUB_SHA\", \"a\" * 40)"` | — |
| [SRC-2614DCB6FB-L000109](../../tests/test_search_code.py#L109) | 109 | `""` | — |
| [SRC-2614DCB6FB-L000110](../../tests/test_search_code.py#L110) | 110 | `"    assert SEARCH.default_repository_ref(tmp_path) == \"feature/current-review\""` | — |
| [SRC-2614DCB6FB-L000111](../../tests/test_search_code.py#L111) | 111 | `""` | — |
| [SRC-2614DCB6FB-L000112](../../tests/test_search_code.py#L112) | 112 | `""` | — |
| [SRC-2614DCB6FB-L000113](../../tests/test_search_code.py#L113) | 113 | `"def test_default_repository_ref_uses_valid_ci_sha("` | — |
| [SRC-2614DCB6FB-L000114](../../tests/test_search_code.py#L114) | 114 | `"    monkeypatch, tmp_path: Path"` | — |
| [SRC-2614DCB6FB-L000115](../../tests/test_search_code.py#L115) | 115 | `") -> None:"` | — |
| [SRC-2614DCB6FB-L000116](../../tests/test_search_code.py#L116) | 116 | `"    monkeypatch.delenv(\"OMARAI_GITHUB_REF\", raising=False)"` | — |
| [SRC-2614DCB6FB-L000117](../../tests/test_search_code.py#L117) | 117 | `"    monkeypatch.setenv(\"GITHUB_SHA\", \"B\" * 40)"` | — |
| [SRC-2614DCB6FB-L000118](../../tests/test_search_code.py#L118) | 118 | `""` | — |
| [SRC-2614DCB6FB-L000119](../../tests/test_search_code.py#L119) | 119 | `"    assert SEARCH.default_repository_ref(tmp_path) == \"b\" * 40"` | — |
| [SRC-2614DCB6FB-L000120](../../tests/test_search_code.py#L120) | 120 | `""` | — |
| [SRC-2614DCB6FB-L000121](../../tests/test_search_code.py#L121) | 121 | `"def test_cli_uses_explicit_ref_for_source_links(tmp_path: Path, capsys) -> None:"` | — |
| [SRC-2614DCB6FB-L000122](../../tests/test_search_code.py#L122) | 122 | `"    source = tmp_path / \"app.py\""` | — |
| [SRC-2614DCB6FB-L000123](../../tests/test_search_code.py#L123) | 123 | `"    source.write_text(\"needle = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000124](../../tests/test_search_code.py#L124) | 124 | `""` | — |
| [SRC-2614DCB6FB-L000125](../../tests/test_search_code.py#L125) | 125 | `"    exit_code = SEARCH.main(["` | — |
| [SRC-2614DCB6FB-L000126](../../tests/test_search_code.py#L126) | 126 | `"        \"needle\", \"--root\", str(tmp_path), \"--ref\", \"fix/cli-review\""` | — |
| [SRC-2614DCB6FB-L000127](../../tests/test_search_code.py#L127) | 127 | `"    ])"` | — |
| [SRC-2614DCB6FB-L000128](../../tests/test_search_code.py#L128) | 128 | `""` | — |
| [SRC-2614DCB6FB-L000129](../../tests/test_search_code.py#L129) | 129 | `"    output = capsys.readouterr().out"` | — |
| [SRC-2614DCB6FB-L000130](../../tests/test_search_code.py#L130) | 130 | `"    assert exit_code == 0"` | — |
| [SRC-2614DCB6FB-L000131](../../tests/test_search_code.py#L131) | 131 | `"    assert \"blob/fix/cli-review/app.py#L1\" in output"` | — |
| [SRC-2614DCB6FB-L000132](../../tests/test_search_code.py#L132) | 132 | `"    assert \"blob/main/app.py#L1\" not in output"` | — |
| [SRC-2614DCB6FB-L000133](../../tests/test_search_code.py#L133) | 133 | `""` | — |
## اختبارات

### FILE-D033B34F41 — [tests/test_source_metadata_audit.py](../../tests/test_source_metadata_audit.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-D033B34F41-L000001](../../tests/test_source_metadata_audit.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-D033B34F41-L000002](../../tests/test_source_metadata_audit.py#L2) | 2 | `""` | — |
| [SRC-D033B34F41-L000003](../../tests/test_source_metadata_audit.py#L3) | 3 | `"from agents.answer_validation import audit_answer_integrity"` | — |
| [SRC-D033B34F41-L000004](../../tests/test_source_metadata_audit.py#L4) | 4 | `""` | — |
| [SRC-D033B34F41-L000005](../../tests/test_source_metadata_audit.py#L5) | 5 | `""` | — |
| [SRC-D033B34F41-L000006](../../tests/test_source_metadata_audit.py#L6) | 6 | `"def test_population_question_reports_missing_url_publication_date_period_and_scope():"` | — |
| [SRC-D033B34F41-L000007](../../tests/test_source_metadata_audit.py#L7) | 7 | `"    result = audit_answer_integrity("` | — |
| [SRC-D033B34F41-L000008](../../tests/test_source_metadata_audit.py#L8) | 8 | `"        \"ما عدد سكان القاهرة؟\","` | — |
| [SRC-D033B34F41-L000009](../../tests/test_source_metadata_audit.py#L9) | 9 | `"        \"حسب التقديرات، العدد 9.7 مليون.\","` | — |
| [SRC-D033B34F41-L000010](../../tests/test_source_metadata_audit.py#L10) | 10 | `"        [{"` | — |
| [SRC-D033B34F41-L000011](../../tests/test_source_metadata_audit.py#L11) | 11 | `"            \"title\": \"تقديرات سكانية\","` | — |
| [SRC-D033B34F41-L000012](../../tests/test_source_metadata_audit.py#L12) | 12 | `"            \"snippet\": \"عدد السكان 9.7 مليون\","` | — |
| [SRC-D033B34F41-L000013](../../tests/test_source_metadata_audit.py#L13) | 13 | `"            \"page_fetched\": False,"` | — |
| [SRC-D033B34F41-L000014](../../tests/test_source_metadata_audit.py#L14) | 14 | `"        }],"` | — |
| [SRC-D033B34F41-L000015](../../tests/test_source_metadata_audit.py#L15) | 15 | `"    )"` | — |
| [SRC-D033B34F41-L000016](../../tests/test_source_metadata_audit.py#L16) | 16 | `""` | — |
| [SRC-D033B34F41-L000017](../../tests/test_source_metadata_audit.py#L17) | 17 | `"    audit = result[\"source_metadata_audit\"]"` | — |
| [SRC-D033B34F41-L000018](../../tests/test_source_metadata_audit.py#L18) | 18 | `"    assert audit[\"status\"] == \"metadata_gaps_found\""` | — |
| [SRC-D033B34F41-L000019](../../tests/test_source_metadata_audit.py#L19) | 19 | `"    assert audit[\"population_claim_context_detected\"] is True"` | — |
| [SRC-D033B34F41-L000020](../../tests/test_source_metadata_audit.py#L20) | 20 | `"    assert audit[\"sources_missing_or_invalid_url_count\"] == 1"` | — |
| [SRC-D033B34F41-L000021](../../tests/test_source_metadata_audit.py#L21) | 21 | `"    assert audit[\"sources_missing_publication_date_count\"] == 1"` | — |
| [SRC-D033B34F41-L000022](../../tests/test_source_metadata_audit.py#L22) | 22 | `"    assert audit[\"sources_missing_data_reference_period_count\"] == 1"` | — |
| [SRC-D033B34F41-L000023](../../tests/test_source_metadata_audit.py#L23) | 23 | `"    assert audit[\"sources_missing_publication_or_data_date_count\"] == 1"` | — |
| [SRC-D033B34F41-L000024](../../tests/test_source_metadata_audit.py#L24) | 24 | `"    assert audit[\"sources_missing_geographic_scope_count\"] == 1"` | — |
| [SRC-D033B34F41-L000025](../../tests/test_source_metadata_audit.py#L25) | 25 | `"    assert audit[\"semantic_verification\"] is False"` | — |
| [SRC-D033B34F41-L000026](../../tests/test_source_metadata_audit.py#L26) | 26 | `"    assert audit[\"source_entailment_verified\"] is False"` | — |
| [SRC-D033B34F41-L000027](../../tests/test_source_metadata_audit.py#L27) | 27 | `""` | — |
| [SRC-D033B34F41-L000028](../../tests/test_source_metadata_audit.py#L28) | 28 | `""` | — |
| [SRC-D033B34F41-L000029](../../tests/test_source_metadata_audit.py#L29) | 29 | `"def test_population_source_metadata_presence_does_not_claim_truth_verification():"` | — |
| [SRC-D033B34F41-L000030](../../tests/test_source_metadata_audit.py#L30) | 30 | `"    result = audit_answer_integrity("` | — |
| [SRC-D033B34F41-L000031](../../tests/test_source_metadata_audit.py#L31) | 31 | `"        \"ما عدد سكان القاهرة؟\","` | — |
| [SRC-D033B34F41-L000032](../../tests/test_source_metadata_audit.py#L32) | 32 | `"        \"العدد وفق المصدر [المصدر 1].\","` | — |
| [SRC-D033B34F41-L000033](../../tests/test_source_metadata_audit.py#L33) | 33 | `"        [{"` | — |
| [SRC-D033B34F41-L000034](../../tests/test_source_metadata_audit.py#L34) | 34 | `"            \"title\": \"Population report\","` | — |
| [SRC-D033B34F41-L000035](../../tests/test_source_metadata_audit.py#L35) | 35 | `"            \"publisher\": \"Example Statistics Office\","` | — |
| [SRC-D033B34F41-L000036](../../tests/test_source_metadata_audit.py#L36) | 36 | `"            \"url\": \"https://example.org/population\","` | — |
| [SRC-D033B34F41-L000037](../../tests/test_source_metadata_audit.py#L37) | 37 | `"            \"published_at\": \"2025-06-01\","` | — |
| [SRC-D033B34F41-L000038](../../tests/test_source_metadata_audit.py#L38) | 38 | `"            \"data_reference_period\": \"2025 estimate\","` | — |
| [SRC-D033B34F41-L000039](../../tests/test_source_metadata_audit.py#L39) | 39 | `"            \"geographic_scope\": \"Cairo Governorate administrative boundary\","` | — |
| [SRC-D033B34F41-L000040](../../tests/test_source_metadata_audit.py#L40) | 40 | `"            \"snippet\": \"Population estimate for Cairo Governorate.\","` | — |
| [SRC-D033B34F41-L000041](../../tests/test_source_metadata_audit.py#L41) | 41 | `"            \"page_fetched\": False,"` | — |
| [SRC-D033B34F41-L000042](../../tests/test_source_metadata_audit.py#L42) | 42 | `"        }],"` | — |
| [SRC-D033B34F41-L000043](../../tests/test_source_metadata_audit.py#L43) | 43 | `"    )"` | — |
| [SRC-D033B34F41-L000044](../../tests/test_source_metadata_audit.py#L44) | 44 | `""` | — |
| [SRC-D033B34F41-L000045](../../tests/test_source_metadata_audit.py#L45) | 45 | `"    audit = result[\"source_metadata_audit\"]"` | — |
| [SRC-D033B34F41-L000046](../../tests/test_source_metadata_audit.py#L46) | 46 | `"    assert audit[\"status\"] == \"minimum_metadata_present\""` | — |
| [SRC-D033B34F41-L000047](../../tests/test_source_metadata_audit.py#L47) | 47 | `"    assert audit[\"sources_missing_or_invalid_url_count\"] == 0"` | — |
| [SRC-D033B34F41-L000048](../../tests/test_source_metadata_audit.py#L48) | 48 | `"    assert audit[\"sources_missing_publisher_identity_count\"] == 0"` | — |
| [SRC-D033B34F41-L000049](../../tests/test_source_metadata_audit.py#L49) | 49 | `"    assert audit[\"sources_missing_publication_date_count\"] == 0"` | — |
| [SRC-D033B34F41-L000050](../../tests/test_source_metadata_audit.py#L50) | 50 | `"    assert audit[\"sources_missing_data_reference_period_count\"] == 0"` | — |
| [SRC-D033B34F41-L000051](../../tests/test_source_metadata_audit.py#L51) | 51 | `"    assert audit[\"sources_missing_publication_or_data_date_count\"] == 0"` | — |
| [SRC-D033B34F41-L000052](../../tests/test_source_metadata_audit.py#L52) | 52 | `"    assert audit[\"sources_missing_geographic_scope_count\"] == 0"` | — |
| [SRC-D033B34F41-L000053](../../tests/test_source_metadata_audit.py#L53) | 53 | `"    assert audit[\"semantic_verification\"] is False"` | — |
| [SRC-D033B34F41-L000054](../../tests/test_source_metadata_audit.py#L54) | 54 | `"    assert audit[\"source_entailment_verified\"] is False"` | — |
| [SRC-D033B34F41-L000055](../../tests/test_source_metadata_audit.py#L55) | 55 | `""` | — |
| [SRC-D033B34F41-L000056](../../tests/test_source_metadata_audit.py#L56) | 56 | `""` | — |
| [SRC-D033B34F41-L000057](../../tests/test_source_metadata_audit.py#L57) | 57 | `"def test_zero_sources_are_not_reported_as_metadata_complete():"` | — |
| [SRC-D033B34F41-L000058](../../tests/test_source_metadata_audit.py#L58) | 58 | `"    result = audit_answer_integrity("` | — |
| [SRC-D033B34F41-L000059](../../tests/test_source_metadata_audit.py#L59) | 59 | `"        \"ما عدد سكان القاهرة؟\","` | — |
| [SRC-D033B34F41-L000060](../../tests/test_source_metadata_audit.py#L60) | 60 | `"        \"لا تتوفر لدي مصادر قابلة للمراجعة.\","` | — |
| [SRC-D033B34F41-L000061](../../tests/test_source_metadata_audit.py#L61) | 61 | `"        [],"` | — |
| [SRC-D033B34F41-L000062](../../tests/test_source_metadata_audit.py#L62) | 62 | `"    )"` | — |
| [SRC-D033B34F41-L000063](../../tests/test_source_metadata_audit.py#L63) | 63 | `""` | — |
| [SRC-D033B34F41-L000064](../../tests/test_source_metadata_audit.py#L64) | 64 | `"    audit = result[\"source_metadata_audit\"]"` | — |
| [SRC-D033B34F41-L000065](../../tests/test_source_metadata_audit.py#L65) | 65 | `"    assert audit[\"status\"] == \"no_sources_to_audit\""` | — |
| [SRC-D033B34F41-L000066](../../tests/test_source_metadata_audit.py#L66) | 66 | `"    assert audit[\"source_count_checked\"] == 0"` | — |
| [SRC-D033B34F41-L000067](../../tests/test_source_metadata_audit.py#L67) | 67 | `"    assert audit[\"semantic_verification\"] is False"` | — |
| [SRC-D033B34F41-L000068](../../tests/test_source_metadata_audit.py#L68) | 68 | `"    assert audit[\"source_entailment_verified\"] is False"` | — |
| [SRC-D033B34F41-L000069](../../tests/test_source_metadata_audit.py#L69) | 69 | `""` | — |
| [SRC-D033B34F41-L000070](../../tests/test_source_metadata_audit.py#L70) | 70 | `""` | — |
| [SRC-D033B34F41-L000071](../../tests/test_source_metadata_audit.py#L71) | 71 | `"def test_population_scope_is_required_even_when_answer_uses_only_a_number():"` | — |
| [SRC-D033B34F41-L000072](../../tests/test_source_metadata_audit.py#L72) | 72 | `"    result = audit_answer_integrity("` | — |
| [SRC-D033B34F41-L000073](../../tests/test_source_metadata_audit.py#L73) | 73 | `"        \"How many people live in Cairo?\","` | — |
| [SRC-D033B34F41-L000074](../../tests/test_source_metadata_audit.py#L74) | 74 | `"        \"The estimate is 9.7 million.\","` | — |
| [SRC-D033B34F41-L000075](../../tests/test_source_metadata_audit.py#L75) | 75 | `"        [{"` | — |
| [SRC-D033B34F41-L000076](../../tests/test_source_metadata_audit.py#L76) | 76 | `"            \"title\": \"Population estimate\","` | — |
| [SRC-D033B34F41-L000077](../../tests/test_source_metadata_audit.py#L77) | 77 | `"            \"publisher\": \"Example Statistics Office\","` | — |
| [SRC-D033B34F41-L000078](../../tests/test_source_metadata_audit.py#L78) | 78 | `"            \"url\": \"https://example.org/cairo\","` | — |
| [SRC-D033B34F41-L000079](../../tests/test_source_metadata_audit.py#L79) | 79 | `"            \"published_at\": \"2025-06-01\","` | — |
| [SRC-D033B34F41-L000080](../../tests/test_source_metadata_audit.py#L80) | 80 | `"            \"data_year\": 2025,"` | — |
| [SRC-D033B34F41-L000081](../../tests/test_source_metadata_audit.py#L81) | 81 | `"            \"snippet\": \"An estimate for Cairo.\","` | — |
| [SRC-D033B34F41-L000082](../../tests/test_source_metadata_audit.py#L82) | 82 | `"            \"page_fetched\": False,"` | — |
| [SRC-D033B34F41-L000083](../../tests/test_source_metadata_audit.py#L83) | 83 | `"        }],"` | — |
| [SRC-D033B34F41-L000084](../../tests/test_source_metadata_audit.py#L84) | 84 | `"    )"` | — |
| [SRC-D033B34F41-L000085](../../tests/test_source_metadata_audit.py#L85) | 85 | `""` | — |
| [SRC-D033B34F41-L000086](../../tests/test_source_metadata_audit.py#L86) | 86 | `"    audit = result[\"source_metadata_audit\"]"` | — |
| [SRC-D033B34F41-L000087](../../tests/test_source_metadata_audit.py#L87) | 87 | `"    assert audit[\"population_claim_context_detected\"] is True"` | — |
| [SRC-D033B34F41-L000088](../../tests/test_source_metadata_audit.py#L88) | 88 | `"    assert audit[\"sources_missing_geographic_scope_count\"] == 1"` | — |
| [SRC-D033B34F41-L000089](../../tests/test_source_metadata_audit.py#L89) | 89 | `"    assert \"geographic_scope_for_population_claim\" in audit[\"sources\"][0][\"missing_fields\"]"` | — |
## اختبارات

### FILE-1C0D3D1206 — [tests/test_sqlite_backup_restore.py](../../tests/test_sqlite_backup_restore.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1C0D3D1206-L000001](../../tests/test_sqlite_backup_restore.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-1C0D3D1206-L000002](../../tests/test_sqlite_backup_restore.py#L2) | 2 | `""` | — |
| [SRC-1C0D3D1206-L000003](../../tests/test_sqlite_backup_restore.py#L3) | 3 | `"import sqlite3"` | — |
| [SRC-1C0D3D1206-L000004](../../tests/test_sqlite_backup_restore.py#L4) | 4 | `""` | — |
| [SRC-1C0D3D1206-L000005](../../tests/test_sqlite_backup_restore.py#L5) | 5 | `"import pytest"` | — |
| [SRC-1C0D3D1206-L000006](../../tests/test_sqlite_backup_restore.py#L6) | 6 | `""` | — |
| [SRC-1C0D3D1206-L000007](../../tests/test_sqlite_backup_restore.py#L7) | 7 | `"from agents.omarai import LeadStore"` | — |
| [SRC-1C0D3D1206-L000008](../../tests/test_sqlite_backup_restore.py#L8) | 8 | `"from scripts.sqlite_backup_restore import BackupError, backup_database, restore_database"` | — |
| [SRC-1C0D3D1206-L000009](../../tests/test_sqlite_backup_restore.py#L9) | 9 | `""` | — |
| [SRC-1C0D3D1206-L000010](../../tests/test_sqlite_backup_restore.py#L10) | 10 | `""` | — |
| [SRC-1C0D3D1206-L000011](../../tests/test_sqlite_backup_restore.py#L11) | 11 | `"def test_backup_and_restore_preserve_omarai_leads(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000012](../../tests/test_sqlite_backup_restore.py#L12) | 12 | `"    source_path = tmp_path / \"live.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000013](../../tests/test_sqlite_backup_restore.py#L13) | 13 | `"    source = LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000014](../../tests/test_sqlite_backup_restore.py#L14) | 14 | `"    first, created_first = source.add("` | — |
| [SRC-1C0D3D1206-L000015](../../tests/test_sqlite_backup_restore.py#L15) | 15 | `"        \"بدور على شقة في التجمع وممكن معاينة\","` | — |
| [SRC-1C0D3D1206-L000016](../../tests/test_sqlite_backup_restore.py#L16) | 16 | `"        \"https://example.com/posts/1\","` | — |
| [SRC-1C0D3D1206-L000017](../../tests/test_sqlite_backup_restore.py#L17) | 17 | `"        platform=\"manual\","` | — |
| [SRC-1C0D3D1206-L000018](../../tests/test_sqlite_backup_restore.py#L18) | 18 | `"        note=\"سجل اختبار أول\","` | — |
| [SRC-1C0D3D1206-L000019](../../tests/test_sqlite_backup_restore.py#L19) | 19 | `"    )"` | — |
| [SRC-1C0D3D1206-L000020](../../tests/test_sqlite_backup_restore.py#L20) | 20 | `"    second, created_second = source.add("` | — |
| [SRC-1C0D3D1206-L000021](../../tests/test_sqlite_backup_restore.py#L21) | 21 | `"        \"محتاج شقة للإيجار الشهر القادم\","` | — |
| [SRC-1C0D3D1206-L000022](../../tests/test_sqlite_backup_restore.py#L22) | 22 | `"        \"https://example.com/posts/2\","` | — |
| [SRC-1C0D3D1206-L000023](../../tests/test_sqlite_backup_restore.py#L23) | 23 | `"        platform=\"manual\","` | — |
| [SRC-1C0D3D1206-L000024](../../tests/test_sqlite_backup_restore.py#L24) | 24 | `"        note=\"سجل اختبار ثان\","` | — |
| [SRC-1C0D3D1206-L000025](../../tests/test_sqlite_backup_restore.py#L25) | 25 | `"    )"` | — |
| [SRC-1C0D3D1206-L000026](../../tests/test_sqlite_backup_restore.py#L26) | 26 | `"    assert created_first and created_second"` | — |
| [SRC-1C0D3D1206-L000027](../../tests/test_sqlite_backup_restore.py#L27) | 27 | `"    source.update_status(first[\"id\"], \"qualified\")"` | — |
| [SRC-1C0D3D1206-L000028](../../tests/test_sqlite_backup_restore.py#L28) | 28 | `""` | — |
| [SRC-1C0D3D1206-L000029](../../tests/test_sqlite_backup_restore.py#L29) | 29 | `"    snapshot_path = tmp_path / \"backups\" / \"snapshot.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000030](../../tests/test_sqlite_backup_restore.py#L30) | 30 | `"    backup_report = backup_database(source_path, snapshot_path)"` | — |
| [SRC-1C0D3D1206-L000031](../../tests/test_sqlite_backup_restore.py#L31) | 31 | `"    assert backup_report[\"result\"] == \"passed\""` | — |
| [SRC-1C0D3D1206-L000032](../../tests/test_sqlite_backup_restore.py#L32) | 32 | `"    assert backup_report[\"integrity_check\"] == \"ok\""` | — |
| [SRC-1C0D3D1206-L000033](../../tests/test_sqlite_backup_restore.py#L33) | 33 | `"    assert backup_report[\"lead_count\"] == 2"` | — |
| [SRC-1C0D3D1206-L000034](../../tests/test_sqlite_backup_restore.py#L34) | 34 | `"    assert backup_report[\"overwrite\"] is False"` | — |
| [SRC-1C0D3D1206-L000035](../../tests/test_sqlite_backup_restore.py#L35) | 35 | `""` | — |
| [SRC-1C0D3D1206-L000036](../../tests/test_sqlite_backup_restore.py#L36) | 36 | `"    restored_path = tmp_path / \"restored\" / \"restored.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000037](../../tests/test_sqlite_backup_restore.py#L37) | 37 | `"    restore_report = restore_database(snapshot_path, restored_path)"` | — |
| [SRC-1C0D3D1206-L000038](../../tests/test_sqlite_backup_restore.py#L38) | 38 | `"    assert restore_report[\"result\"] == \"passed\""` | — |
| [SRC-1C0D3D1206-L000039](../../tests/test_sqlite_backup_restore.py#L39) | 39 | `"    assert restore_report[\"integrity_check\"] == \"ok\""` | — |
| [SRC-1C0D3D1206-L000040](../../tests/test_sqlite_backup_restore.py#L40) | 40 | `"    assert restore_report[\"lead_count\"] == 2"` | — |
| [SRC-1C0D3D1206-L000041](../../tests/test_sqlite_backup_restore.py#L41) | 41 | `""` | — |
| [SRC-1C0D3D1206-L000042](../../tests/test_sqlite_backup_restore.py#L42) | 42 | `"    restored = LeadStore(restored_path)"` | — |
| [SRC-1C0D3D1206-L000043](../../tests/test_sqlite_backup_restore.py#L43) | 43 | `"    original_rows = {row[\"id\"]: row for row in source.list(limit=500)}"` | — |
| [SRC-1C0D3D1206-L000044](../../tests/test_sqlite_backup_restore.py#L44) | 44 | `"    restored_rows = {row[\"id\"]: row for row in restored.list(limit=500)}"` | — |
| [SRC-1C0D3D1206-L000045](../../tests/test_sqlite_backup_restore.py#L45) | 45 | `"    assert restored_rows == original_rows"` | — |
| [SRC-1C0D3D1206-L000046](../../tests/test_sqlite_backup_restore.py#L46) | 46 | `"    assert restored_rows[first[\"id\"]][\"status\"] == \"qualified\""` | — |
| [SRC-1C0D3D1206-L000047](../../tests/test_sqlite_backup_restore.py#L47) | 47 | `"    assert second[\"id\"] in restored_rows"` | — |
| [SRC-1C0D3D1206-L000048](../../tests/test_sqlite_backup_restore.py#L48) | 48 | `""` | — |
| [SRC-1C0D3D1206-L000049](../../tests/test_sqlite_backup_restore.py#L49) | 49 | `""` | — |
| [SRC-1C0D3D1206-L000050](../../tests/test_sqlite_backup_restore.py#L50) | 50 | `"def test_backup_never_overwrites_an_existing_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000051](../../tests/test_sqlite_backup_restore.py#L51) | 51 | `"    source_path = tmp_path / \"source.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000052](../../tests/test_sqlite_backup_restore.py#L52) | 52 | `"    LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000053](../../tests/test_sqlite_backup_restore.py#L53) | 53 | `"    destination = tmp_path / \"keep-me.txt\""` | — |
| [SRC-1C0D3D1206-L000054](../../tests/test_sqlite_backup_restore.py#L54) | 54 | `"    destination.write_text(\"do not overwrite\", encoding=\"utf-8\")"` | — |
| [SRC-1C0D3D1206-L000055](../../tests/test_sqlite_backup_restore.py#L55) | 55 | `""` | — |
| [SRC-1C0D3D1206-L000056](../../tests/test_sqlite_backup_restore.py#L56) | 56 | `"    with pytest.raises(FileExistsError):"` | — |
| [SRC-1C0D3D1206-L000057](../../tests/test_sqlite_backup_restore.py#L57) | 57 | `"        backup_database(source_path, destination)"` | — |
| [SRC-1C0D3D1206-L000058](../../tests/test_sqlite_backup_restore.py#L58) | 58 | `""` | — |
| [SRC-1C0D3D1206-L000059](../../tests/test_sqlite_backup_restore.py#L59) | 59 | `"    assert destination.read_text(encoding=\"utf-8\") == \"do not overwrite\""` | — |
| [SRC-1C0D3D1206-L000060](../../tests/test_sqlite_backup_restore.py#L60) | 60 | `""` | — |
| [SRC-1C0D3D1206-L000061](../../tests/test_sqlite_backup_restore.py#L61) | 61 | `""` | — |
| [SRC-1C0D3D1206-L000062](../../tests/test_sqlite_backup_restore.py#L62) | 62 | `"def test_backup_rejects_non_omarai_sqlite_database_without_leaving_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000063](../../tests/test_sqlite_backup_restore.py#L63) | 63 | `"    source_path = tmp_path / \"unrelated.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000064](../../tests/test_sqlite_backup_restore.py#L64) | 64 | `"    with sqlite3.connect(source_path) as db:"` | — |
| [SRC-1C0D3D1206-L000065](../../tests/test_sqlite_backup_restore.py#L65) | 65 | `"        db.execute(\"CREATE TABLE unrelated (value TEXT)\")"` | — |
| [SRC-1C0D3D1206-L000066](../../tests/test_sqlite_backup_restore.py#L66) | 66 | `""` | — |
| [SRC-1C0D3D1206-L000067](../../tests/test_sqlite_backup_restore.py#L67) | 67 | `"    destination = tmp_path / \"should-not-exist.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000068](../../tests/test_sqlite_backup_restore.py#L68) | 68 | `"    with pytest.raises(BackupError, match=\"not an Omarai leads database\"):"` | — |
| [SRC-1C0D3D1206-L000069](../../tests/test_sqlite_backup_restore.py#L69) | 69 | `"        backup_database(source_path, destination)"` | — |
| [SRC-1C0D3D1206-L000070](../../tests/test_sqlite_backup_restore.py#L70) | 70 | `""` | — |
| [SRC-1C0D3D1206-L000071](../../tests/test_sqlite_backup_restore.py#L71) | 71 | `"    assert not destination.exists()"` | — |
| [SRC-1C0D3D1206-L000072](../../tests/test_sqlite_backup_restore.py#L72) | 72 | `""` | — |
| [SRC-1C0D3D1206-L000073](../../tests/test_sqlite_backup_restore.py#L73) | 73 | `""` | — |
| [SRC-1C0D3D1206-L000074](../../tests/test_sqlite_backup_restore.py#L74) | 74 | `"def test_backup_rejects_same_source_and_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000075](../../tests/test_sqlite_backup_restore.py#L75) | 75 | `"    source_path = tmp_path / \"source.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000076](../../tests/test_sqlite_backup_restore.py#L76) | 76 | `"    LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000077](../../tests/test_sqlite_backup_restore.py#L77) | 77 | `""` | — |
| [SRC-1C0D3D1206-L000078](../../tests/test_sqlite_backup_restore.py#L78) | 78 | `"    with pytest.raises(BackupError, match=\"different paths\"):"` | — |
| [SRC-1C0D3D1206-L000079](../../tests/test_sqlite_backup_restore.py#L79) | 79 | `"        backup_database(source_path, source_path)"` | — |
| [SRC-1C0D3D1206-L000080](../../tests/test_sqlite_backup_restore.py#L80) | 80 | `""` | — |
| [SRC-1C0D3D1206-L000081](../../tests/test_sqlite_backup_restore.py#L81) | 81 | `""` | — |
| [SRC-1C0D3D1206-L000082](../../tests/test_sqlite_backup_restore.py#L82) | 82 | `"def test_restore_rejects_corrupt_backup_without_overwriting_source(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000083](../../tests/test_sqlite_backup_restore.py#L83) | 83 | `"    backup_path = tmp_path / \"corrupt.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000084](../../tests/test_sqlite_backup_restore.py#L84) | 84 | `"    backup_path.write_bytes(b\"not a sqlite database\")"` | — |
| [SRC-1C0D3D1206-L000085](../../tests/test_sqlite_backup_restore.py#L85) | 85 | `"    destination = tmp_path / \"restore.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000086](../../tests/test_sqlite_backup_restore.py#L86) | 86 | `""` | — |
| [SRC-1C0D3D1206-L000087](../../tests/test_sqlite_backup_restore.py#L87) | 87 | `"    with pytest.raises(BackupError):"` | — |
| [SRC-1C0D3D1206-L000088](../../tests/test_sqlite_backup_restore.py#L88) | 88 | `"        restore_database(backup_path, destination)"` | — |
| [SRC-1C0D3D1206-L000089](../../tests/test_sqlite_backup_restore.py#L89) | 89 | `""` | — |
| [SRC-1C0D3D1206-L000090](../../tests/test_sqlite_backup_restore.py#L90) | 90 | `"    assert backup_path.read_bytes() == b\"not a sqlite database\""` | — |
| [SRC-1C0D3D1206-L000091](../../tests/test_sqlite_backup_restore.py#L91) | 91 | `"    assert not destination.exists()"` | — |
| [SRC-1C0D3D1206-L000092](../../tests/test_sqlite_backup_restore.py#L92) | 92 | `""` | — |
| [SRC-1C0D3D1206-L000093](../../tests/test_sqlite_backup_restore.py#L93) | 93 | `"def test_backup_rejects_dangling_symlink_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000094](../../tests/test_sqlite_backup_restore.py#L94) | 94 | `"    source_path = tmp_path / \"source.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000095](../../tests/test_sqlite_backup_restore.py#L95) | 95 | `"    LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000096](../../tests/test_sqlite_backup_restore.py#L96) | 96 | `"    target_path = tmp_path / \"target.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000097](../../tests/test_sqlite_backup_restore.py#L97) | 97 | `"    destination_link = tmp_path / \"backup-link.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000098](../../tests/test_sqlite_backup_restore.py#L98) | 98 | `"    destination_link.symlink_to(target_path)"` | — |
| [SRC-1C0D3D1206-L000099](../../tests/test_sqlite_backup_restore.py#L99) | 99 | `""` | — |
| [SRC-1C0D3D1206-L000100](../../tests/test_sqlite_backup_restore.py#L100) | 100 | `"    with pytest.raises(FileExistsError):"` | — |
| [SRC-1C0D3D1206-L000101](../../tests/test_sqlite_backup_restore.py#L101) | 101 | `"        backup_database(source_path, destination_link)"` | — |
| [SRC-1C0D3D1206-L000102](../../tests/test_sqlite_backup_restore.py#L102) | 102 | `""` | — |
| [SRC-1C0D3D1206-L000103](../../tests/test_sqlite_backup_restore.py#L103) | 103 | `"    assert destination_link.is_symlink()"` | — |
| [SRC-1C0D3D1206-L000104](../../tests/test_sqlite_backup_restore.py#L104) | 104 | `"    assert not target_path.exists()"` | — |
| [SRC-1C0D3D1206-L000105](../../tests/test_sqlite_backup_restore.py#L105) | 105 | `""` | — |
## اختبارات

### FILE-AFEDC2645A — [tests/test_task_understanding.py](../../tests/test_task_understanding.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-AFEDC2645A-L000001](../../tests/test_task_understanding.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-AFEDC2645A-L000002](../../tests/test_task_understanding.py#L2) | 2 | `""` | — |
| [SRC-AFEDC2645A-L000003](../../tests/test_task_understanding.py#L3) | 3 | `"import pytest"` | — |
| [SRC-AFEDC2645A-L000004](../../tests/test_task_understanding.py#L4) | 4 | `""` | — |
| [SRC-AFEDC2645A-L000005](../../tests/test_task_understanding.py#L5) | 5 | `"from agents.task_understanding import build_query_strategy_matrix, build_task_spec"` | — |
| [SRC-AFEDC2645A-L000006](../../tests/test_task_understanding.py#L6) | 6 | `""` | — |
| [SRC-AFEDC2645A-L000007](../../tests/test_task_understanding.py#L7) | 7 | `""` | — |
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
| [SRC-AFEDC2645A-L000088](../../tests/test_task_understanding.py#L88) | 88 | `"    question = \"قارن السيارات الكهربائية في مصر من حيث السعر والضمان\""` | — |
| [SRC-AFEDC2645A-L000089](../../tests/test_task_understanding.py#L89) | 89 | `"    spec = build_task_spec(question, mode=\"deep\", intent_route=\"WEB_DEEP\")"` | — |
| [SRC-AFEDC2645A-L000090](../../tests/test_task_understanding.py#L90) | 90 | `"    existing = [\"السيارات الكهربائية في مصر\"] + ["` | — |
| [SRC-AFEDC2645A-L000091](../../tests/test_task_understanding.py#L91) | 91 | `"        f\"السيارات الكهربائية في مصر بديل عام {i}\" for i in range(1, 9)"` | — |
| [SRC-AFEDC2645A-L000092](../../tests/test_task_understanding.py#L92) | 92 | `"    ]"` | — |
| [SRC-AFEDC2645A-L000093](../../tests/test_task_understanding.py#L93) | 93 | `"    rows = build_query_strategy_matrix(question, spec, existing, limit=6)"` | — |
| [SRC-AFEDC2645A-L000094](../../tests/test_task_understanding.py#L94) | 94 | `"    queries = [row[\"query\"] for row in rows]"` | — |
| [SRC-AFEDC2645A-L000095](../../tests/test_task_understanding.py#L95) | 95 | `"    assert 1 <= len(queries) <= 6"` | — |
| [SRC-AFEDC2645A-L000096](../../tests/test_task_understanding.py#L96) | 96 | `"    assert len({query.casefold() for query in queries}) == len(queries)"` | — |
| [SRC-AFEDC2645A-L000097](../../tests/test_task_understanding.py#L97) | 97 | `"    assert all(\"السيارات\" in query for query in queries)"` | — |
| [SRC-AFEDC2645A-L000098](../../tests/test_task_understanding.py#L98) | 98 | `"    assert any(row[\"strategy\"] == \"explicit_criterion\" for row in rows)"` | — |
| [SRC-AFEDC2645A-L000099](../../tests/test_task_understanding.py#L99) | 99 | `"    assert any(row[\"strategy\"] == \"primary_specification\" for row in rows)"` | — |
| [SRC-AFEDC2645A-L000100](../../tests/test_task_understanding.py#L100) | 100 | `"    assert sum(row[\"strategy\"] == \"planner_alternative\" for row in rows) <= 1"` | — |
| [SRC-AFEDC2645A-L000101](../../tests/test_task_understanding.py#L101) | 101 | `"    assert all(row[\"rationale\"] for row in rows)"` | — |
| [SRC-AFEDC2645A-L000102](../../tests/test_task_understanding.py#L102) | 102 | `""` | — |
| [SRC-AFEDC2645A-L000103](../../tests/test_task_understanding.py#L103) | 103 | `"def test_strategy_matrix_does_not_create_generic_queries_without_topic():"` | — |
| [SRC-AFEDC2645A-L000104](../../tests/test_task_understanding.py#L104) | 104 | `"    spec = build_task_spec(\"قارنهم\", mode=\"deep\", intent_route=\"CLARIFY\")"` | — |
| [SRC-AFEDC2645A-L000105](../../tests/test_task_understanding.py#L105) | 105 | `"    rows = build_query_strategy_matrix(\"قارنهم\", spec, [], limit=8)"` | — |
| [SRC-AFEDC2645A-L000106](../../tests/test_task_understanding.py#L106) | 106 | `"    assert rows == []"` | — |
| [SRC-AFEDC2645A-L000107](../../tests/test_task_understanding.py#L107) | 107 | `""` | — |
| [SRC-AFEDC2645A-L000108](../../tests/test_task_understanding.py#L108) | 108 | `""` | — |
| [SRC-AFEDC2645A-L000109](../../tests/test_task_understanding.py#L109) | 109 | `"def test_mixed_language_is_supported_and_urls_are_explicit_constraints():"` | — |
| [SRC-AFEDC2645A-L000110](../../tests/test_task_understanding.py#L110) | 110 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000111](../../tests/test_task_understanding.py#L111) | 111 | `"        \"Compare Nissan Sunny 2022 with BYD Dolphin في مصر https://example.com/specs\","` | — |
| [SRC-AFEDC2645A-L000112](../../tests/test_task_understanding.py#L112) | 112 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000113](../../tests/test_task_understanding.py#L113) | 113 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000114](../../tests/test_task_understanding.py#L114) | 114 | `"    )"` | — |
| [SRC-AFEDC2645A-L000115](../../tests/test_task_understanding.py#L115) | 115 | `"    assert spec[\"constraints\"][\"language_profile\"] == \"mixed\""` | — |
| [SRC-AFEDC2645A-L000116](../../tests/test_task_understanding.py#L116) | 116 | `"    assert spec[\"constraints\"][\"explicit_urls\"] == [\"https://example.com/specs\"]"` | — |
| [SRC-AFEDC2645A-L000117](../../tests/test_task_understanding.py#L117) | 117 | `"    assert \"2022\" in spec[\"constraints\"][\"explicit_years\"]"` | — |
| [SRC-AFEDC2645A-L000118](../../tests/test_task_understanding.py#L118) | 118 | `""` | — |
| [SRC-AFEDC2645A-L000119](../../tests/test_task_understanding.py#L119) | 119 | `""` | — |
| [SRC-AFEDC2645A-L000120](../../tests/test_task_understanding.py#L120) | 120 | `"def test_task_spec_validator_does_not_accept_untrusted_arbitrary_objects():"` | — |
| [SRC-AFEDC2645A-L000121](../../tests/test_task_understanding.py#L121) | 121 | `"    from agents.task_understanding import validate_task_spec"` | — |
| [SRC-AFEDC2645A-L000122](../../tests/test_task_understanding.py#L122) | 122 | `""` | — |
| [SRC-AFEDC2645A-L000123](../../tests/test_task_understanding.py#L123) | 123 | `"    invalid = validate_task_spec({\"schema\": \"wrong\", \"tool_requirements\": [\"delete files\"]})"` | — |
| [SRC-AFEDC2645A-L000124](../../tests/test_task_understanding.py#L124) | 124 | `"    assert invalid[\"status\"] == \"not_available\""` | — |
| [SRC-AFEDC2645A-L000125](../../tests/test_task_understanding.py#L125) | 125 | `""` | — |
| [SRC-AFEDC2645A-L000126](../../tests/test_task_understanding.py#L126) | 126 | `""` | — |
| [SRC-AFEDC2645A-L000127](../../tests/test_task_understanding.py#L127) | 127 | `"def test_compound_task_keeps_current_social_and_comparison_requirements_together():"` | — |
| [SRC-AFEDC2645A-L000128](../../tests/test_task_understanding.py#L128) | 128 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000129](../../tests/test_task_understanding.py#L129) | 129 | `"        \"قارن تجارب ملاك نيسان صني 2022 في مصر اليوم من حيث السعر والأعطال\","` | — |
| [SRC-AFEDC2645A-L000130](../../tests/test_task_understanding.py#L130) | 130 | `"        mode=\"social\","` | — |
| [SRC-AFEDC2645A-L000131](../../tests/test_task_understanding.py#L131) | 131 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000132](../../tests/test_task_understanding.py#L132) | 132 | `"    )"` | — |
| [SRC-AFEDC2645A-L000133](../../tests/test_task_understanding.py#L133) | 133 | `"    assert spec[\"task_family\"] in {\"social_opinions\", \"compare\"}"` | — |
| [SRC-AFEDC2645A-L000134](../../tests/test_task_understanding.py#L134) | 134 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is True"` | — |
| [SRC-AFEDC2645A-L000135](../../tests/test_task_understanding.py#L135) | 135 | `"    assert spec[\"constraints\"][\"social_evidence_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000136](../../tests/test_task_understanding.py#L136) | 136 | `"    assert \"publication_or_update_date\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000137](../../tests/test_task_understanding.py#L137) | 137 | `"    assert \"preserve_explicit_comparison_criteria\" in spec[\"evidence_requirements\"] or \"preserve_each_explicit_comparison_criterion\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000138](../../tests/test_task_understanding.py#L138) | 138 | `"    assert \"personal_experience\" in spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000139](../../tests/test_task_understanding.py#L139) | 139 | `"    assert \"date_check\" in spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000140](../../tests/test_task_understanding.py#L140) | 140 | `""` | — |
| [SRC-AFEDC2645A-L000141](../../tests/test_task_understanding.py#L141) | 141 | `""` | — |
| [SRC-AFEDC2645A-L000142](../../tests/test_task_understanding.py#L142) | 142 | `"def test_alarm_word_does_not_trigger_current_information_pattern():"` | — |
| [SRC-AFEDC2645A-L000143](../../tests/test_task_understanding.py#L143) | 143 | `"    spec = build_task_spec(\"ما معنى نظام الإنذار المعنون؟\", mode=\"auto\", intent_route=\"MODEL_ONLY\")"` | — |
| [SRC-AFEDC2645A-L000144](../../tests/test_task_understanding.py#L144) | 144 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is False"` | — |
| [SRC-AFEDC2645A-L000145](../../tests/test_task_understanding.py#L145) | 145 | `"    assert spec[\"task_family\"] == \"explain_or_define\""` | — |
| [SRC-AFEDC2645A-L000146](../../tests/test_task_understanding.py#L146) | 146 | `""` | — |
| [SRC-AFEDC2645A-L000147](../../tests/test_task_understanding.py#L147) | 147 | `""` | — |
| [SRC-AFEDC2645A-L000148](../../tests/test_task_understanding.py#L148) | 148 | `"def test_clarification_route_does_not_claim_search_or_generation_tools():"` | — |
| [SRC-AFEDC2645A-L000149](../../tests/test_task_understanding.py#L149) | 149 | `"    spec = build_task_spec(\"كام سعرها؟\", mode=\"deep\", intent_route=\"CLARIFY\")"` | — |
| [SRC-AFEDC2645A-L000150](../../tests/test_task_understanding.py#L150) | 150 | `"    assert spec[\"ambiguity_status\"] == \"needs_clarification\""` | — |
| [SRC-AFEDC2645A-L000151](../../tests/test_task_understanding.py#L151) | 151 | `"    assert \"web_search\" not in spec[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000152](../../tests/test_task_understanding.py#L152) | 152 | `"    assert \"page_fetch\" not in spec[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000153](../../tests/test_task_understanding.py#L153) | 153 | `"    assert \"language_model_generation_if_configured\" not in spec[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000154](../../tests/test_task_understanding.py#L154) | 154 | `""` | — |
| [SRC-AFEDC2645A-L000155](../../tests/test_task_understanding.py#L155) | 155 | `""` | — |
| [SRC-AFEDC2645A-L000156](../../tests/test_task_understanding.py#L156) | 156 | `"def test_summary_text_and_page_link_require_different_tools():"` | — |
| [SRC-AFEDC2645A-L000157](../../tests/test_task_understanding.py#L157) | 157 | `"    pasted = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000158](../../tests/test_task_understanding.py#L158) | 158 | `"        \"لخص النص التالي: يتناول النص صيانة أجهزة الإنذار وإجراء الاختبار الدوري.\","` | — |
| [SRC-AFEDC2645A-L000159](../../tests/test_task_understanding.py#L159) | 159 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000160](../../tests/test_task_understanding.py#L160) | 160 | `"        intent_route=\"MODEL_ONLY\","` | — |
| [SRC-AFEDC2645A-L000161](../../tests/test_task_understanding.py#L161) | 161 | `"    )"` | — |
| [SRC-AFEDC2645A-L000162](../../tests/test_task_understanding.py#L162) | 162 | `"    assert pasted[\"constraints\"][\"inline_text_supplied_for_summary\"] is True"` | — |
| [SRC-AFEDC2645A-L000163](../../tests/test_task_understanding.py#L163) | 163 | `"    assert \"page_fetch\" not in pasted[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000164](../../tests/test_task_understanding.py#L164) | 164 | `"    assert \"web_search\" not in pasted[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000165](../../tests/test_task_understanding.py#L165) | 165 | `"    linked = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000166](../../tests/test_task_understanding.py#L166) | 166 | `"        \"لخص الصفحة https://example.com/manual\","` | — |
| [SRC-AFEDC2645A-L000167](../../tests/test_task_understanding.py#L167) | 167 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000168](../../tests/test_task_understanding.py#L168) | 168 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000169](../../tests/test_task_understanding.py#L169) | 169 | `"    )"` | — |
| [SRC-AFEDC2645A-L000170](../../tests/test_task_understanding.py#L170) | 170 | `"    assert \"page_fetch\" in linked[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000171](../../tests/test_task_understanding.py#L171) | 171 | `"    assert \"web_search\" in linked[\"tool_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000172](../../tests/test_task_understanding.py#L172) | 172 | `""` | — |
| [SRC-AFEDC2645A-L000173](../../tests/test_task_understanding.py#L173) | 173 | `""` | — |
| [SRC-AFEDC2645A-L000174](../../tests/test_task_understanding.py#L174) | 174 | `"def test_output_format_preferences_are_preserved_separately_from_intent():"` | — |
| [SRC-AFEDC2645A-L000175](../../tests/test_task_understanding.py#L175) | 175 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000176](../../tests/test_task_understanding.py#L176) | 176 | `"        \"قارن الخيارين في جدول مع أمثلة وبالتفصيل وعلى شكل نقاط\","` | — |
| [SRC-AFEDC2645A-L000177](../../tests/test_task_understanding.py#L177) | 177 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000178](../../tests/test_task_understanding.py#L178) | 178 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000179](../../tests/test_task_understanding.py#L179) | 179 | `"    )"` | — |
| [SRC-AFEDC2645A-L000180](../../tests/test_task_understanding.py#L180) | 180 | `"    preferences = spec[\"output_preferences\"]"` | — |
| [SRC-AFEDC2645A-L000181](../../tests/test_task_understanding.py#L181) | 181 | `"    assert preferences[\"table_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000182](../../tests/test_task_understanding.py#L182) | 182 | `"    assert preferences[\"examples_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000183](../../tests/test_task_understanding.py#L183) | 183 | `"    assert preferences[\"detailed\"] is True"` | — |
| [SRC-AFEDC2645A-L000184](../../tests/test_task_understanding.py#L184) | 184 | `"    assert preferences[\"bullets_or_checklist_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000185](../../tests/test_task_understanding.py#L185) | 185 | `""` | — |
| [SRC-AFEDC2645A-L000186](../../tests/test_task_understanding.py#L186) | 186 | `""` | — |
| [SRC-AFEDC2645A-L000187](../../tests/test_task_understanding.py#L187) | 187 | `"def test_location_matching_avoids_partial_english_word_collision():"` | — |
| [SRC-AFEDC2645A-L000188](../../tests/test_task_understanding.py#L188) | 188 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000189](../../tests/test_task_understanding.py#L189) | 189 | `"        \"Explain Egyptology as an academic field\","` | — |
| [SRC-AFEDC2645A-L000190](../../tests/test_task_understanding.py#L190) | 190 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000191](../../tests/test_task_understanding.py#L191) | 191 | `"        intent_route=\"MODEL_ONLY\","` | — |
| [SRC-AFEDC2645A-L000192](../../tests/test_task_understanding.py#L192) | 192 | `"    )"` | — |
| [SRC-AFEDC2645A-L000193](../../tests/test_task_understanding.py#L193) | 193 | `"    assert \"مصر\" not in spec[\"constraints\"][\"explicit_locations\"]"` | — |
| [SRC-AFEDC2645A-L000194](../../tests/test_task_understanding.py#L194) | 194 | `""` | — |
| [SRC-AFEDC2645A-L000195](../../tests/test_task_understanding.py#L195) | 195 | `""` | — |
| [SRC-AFEDC2645A-L000196](../../tests/test_task_understanding.py#L196) | 196 | `"def test_source_policies_keep_orthogonal_research_constraints():"` | — |
| [SRC-AFEDC2645A-L000197](../../tests/test_task_understanding.py#L197) | 197 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000198](../../tests/test_task_understanding.py#L198) | 198 | `"        \"قارن تجارب ملاك السيارات الكهربائية في مصر اليوم من حيث السعر والاعتمادية\","` | — |
| [SRC-AFEDC2645A-L000199](../../tests/test_task_understanding.py#L199) | 199 | `"        mode=\"social\","` | — |
| [SRC-AFEDC2645A-L000200](../../tests/test_task_understanding.py#L200) | 200 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000201](../../tests/test_task_understanding.py#L201) | 201 | `"    )"` | — |
| [SRC-AFEDC2645A-L000202](../../tests/test_task_understanding.py#L202) | 202 | `"    policies = spec[\"constraints\"][\"source_policies\"]"` | — |
| [SRC-AFEDC2645A-L000203](../../tests/test_task_understanding.py#L203) | 203 | `"    assert \"current_read_page\" in policies"` | — |
| [SRC-AFEDC2645A-L000204](../../tests/test_task_understanding.py#L204) | 204 | `"    assert \"public_social_content\" in policies"` | — |
| [SRC-AFEDC2645A-L000205](../../tests/test_task_understanding.py#L205) | 205 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is True"` | — |
| [SRC-AFEDC2645A-L000206](../../tests/test_task_understanding.py#L206) | 206 | `"    assert spec[\"constraints\"][\"social_evidence_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000207](../../tests/test_task_understanding.py#L207) | 207 | `"    assert \"publication_or_update_date\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000208](../../tests/test_task_understanding.py#L208) | 208 | `"    assert \"heuristic_classification_is_not_identity_or_truth_verification\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000209](../../tests/test_task_understanding.py#L209) | 209 | `""` | — |
| [SRC-AFEDC2645A-L000210](../../tests/test_task_understanding.py#L210) | 210 | `""` | — |
| [SRC-AFEDC2645A-L000211](../../tests/test_task_understanding.py#L211) | 211 | `"def test_official_site_request_without_a_target_marks_required_input():"` | — |
| [SRC-AFEDC2645A-L000212](../../tests/test_task_understanding.py#L212) | 212 | `"    spec = build_task_spec(\"هات الموقع الرسمي\", mode=\"auto\", intent_route=\"WEB_SIMPLE\")"` | — |
| [SRC-AFEDC2645A-L000213](../../tests/test_task_understanding.py#L213) | 213 | `"    assert spec[\"task_family\"] == \"official_site_lookup\""` | — |
| [SRC-AFEDC2645A-L000214](../../tests/test_task_understanding.py#L214) | 214 | `"    assert \"official_destination_target_entity\" in spec[\"missing_required_inputs\"]"` | — |
| [SRC-AFEDC2645A-L000215](../../tests/test_task_understanding.py#L215) | 215 | `"    assert spec[\"requires_clarification\"] is True"` | — |
| [SRC-AFEDC2645A-L000216](../../tests/test_task_understanding.py#L216) | 216 | `""` | — |
| [SRC-AFEDC2645A-L000217](../../tests/test_task_understanding.py#L217) | 217 | `""` | — |
| [SRC-AFEDC2645A-L000218](../../tests/test_task_understanding.py#L218) | 218 | `"def test_official_site_request_with_a_named_target_does_not_require_subject_clarification():"` | — |
| [SRC-AFEDC2645A-L000219](../../tests/test_task_understanding.py#L219) | 219 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000220](../../tests/test_task_understanding.py#L220) | 220 | `"        \"هات الموقع الرسمي لوزارة الاتصالات في مصر\","` | — |
| [SRC-AFEDC2645A-L000221](../../tests/test_task_understanding.py#L221) | 221 | `"        mode=\"auto\","` | — |
| [SRC-AFEDC2645A-L000222](../../tests/test_task_understanding.py#L222) | 222 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000223](../../tests/test_task_understanding.py#L223) | 223 | `"    )"` | — |
| [SRC-AFEDC2645A-L000224](../../tests/test_task_understanding.py#L224) | 224 | `"    assert \"official_destination_target_entity\" not in spec[\"missing_required_inputs\"]"` | — |
| [SRC-AFEDC2645A-L000225](../../tests/test_task_understanding.py#L225) | 225 | `"    assert spec[\"constraints\"][\"official_destination_required\"] is True"` | — |
| [SRC-AFEDC2645A-L000226](../../tests/test_task_understanding.py#L226) | 226 | `""` | — |
| [SRC-AFEDC2645A-L000227](../../tests/test_task_understanding.py#L227) | 227 | `""` | — |
| [SRC-AFEDC2645A-L000228](../../tests/test_task_understanding.py#L228) | 228 | `"def test_summary_without_url_or_text_marks_required_input():"` | — |
| [SRC-AFEDC2645A-L000229](../../tests/test_task_understanding.py#L229) | 229 | `"    spec = build_task_spec(\"لخص\", mode=\"auto\", intent_route=\"MODEL_ONLY\")"` | — |
| [SRC-AFEDC2645A-L000230](../../tests/test_task_understanding.py#L230) | 230 | `"    assert \"summary_source_url_or_pasted_text\" in spec[\"missing_required_inputs\"]"` | — |
| [SRC-AFEDC2645A-L000231](../../tests/test_task_understanding.py#L231) | 231 | `"    assert spec[\"requires_clarification\"] is True"` | — |
| [SRC-AFEDC2645A-L000232](../../tests/test_task_understanding.py#L232) | 232 | `""` | — |
| [SRC-AFEDC2645A-L000233](../../tests/test_task_understanding.py#L233) | 233 | `""` | — |
| [SRC-AFEDC2645A-L000234](../../tests/test_task_understanding.py#L234) | 234 | `"def test_output_preferences_do_not_count_as_competing_intent_hypotheses():"` | — |
| [SRC-AFEDC2645A-L000235](../../tests/test_task_understanding.py#L235) | 235 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000236](../../tests/test_task_understanding.py#L236) | 236 | `"        \"قارن الخيارين في جدول مع أمثلة وبالتفصيل\","` | — |
| [SRC-AFEDC2645A-L000237](../../tests/test_task_understanding.py#L237) | 237 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000238](../../tests/test_task_understanding.py#L238) | 238 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000239](../../tests/test_task_understanding.py#L239) | 239 | `"    )"` | — |
| [SRC-AFEDC2645A-L000240](../../tests/test_task_understanding.py#L240) | 240 | `"    families = {row[\"family\"] for row in spec[\"hypothesis_interpretations\"]}"` | — |
| [SRC-AFEDC2645A-L000241](../../tests/test_task_understanding.py#L241) | 241 | `"    assert \"compare\" in families"` | — |
| [SRC-AFEDC2645A-L000242](../../tests/test_task_understanding.py#L242) | 242 | `"    assert not any(family.startswith(\"output_\") for family in families)"` | — |
| [SRC-AFEDC2645A-L000243](../../tests/test_task_understanding.py#L243) | 243 | `"    assert spec[\"ambiguity_status\"] == \"no_strong_lexical_conflict_detected\""` | — |
| [SRC-AFEDC2645A-L000244](../../tests/test_task_understanding.py#L244) | 244 | `""` | — |
| [SRC-AFEDC2645A-L000245](../../tests/test_task_understanding.py#L245) | 245 | `""` | — |
| [SRC-AFEDC2645A-L000246](../../tests/test_task_understanding.py#L246) | 246 | `"@pytest.mark.parametrize("` | — |
| [SRC-AFEDC2645A-L000247](../../tests/test_task_understanding.py#L247) | 247 | `"    (\"question\", \"family\"),"` | — |
