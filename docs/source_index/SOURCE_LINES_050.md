# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **050**
- سجلات الأسطر: **800**
- النطاق: SRC-EA6EC52573-L000294 إلى SRC-1521F490CA-L000076
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-EA6EC52573 — [tests/test_intent_router.py](../../tests/test_intent_router.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-EA6EC52573-L000294](../../tests/test_intent_router.py#L294) | 294 | `"    assert module_source.count(\"def _strip_followup_leadin\") == 1"` | — |
| [SRC-EA6EC52573-L000295](../../tests/test_intent_router.py#L295) | 295 | `""` | — |
## اختبارات

### FILE-4397BC2CD2 — [tests/test_intent_router_integration.py](../../tests/test_intent_router_integration.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-4397BC2CD2-L000001](../../tests/test_intent_router_integration.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-4397BC2CD2-L000002](../../tests/test_intent_router_integration.py#L2) | 2 | `""` | — |
| [SRC-4397BC2CD2-L000003](../../tests/test_intent_router_integration.py#L3) | 3 | `"import pytest"` | — |
| [SRC-4397BC2CD2-L000004](../../tests/test_intent_router_integration.py#L4) | 4 | `""` | — |
| [SRC-4397BC2CD2-L000005](../../tests/test_intent_router_integration.py#L5) | 5 | `"from agents.research import evidence_signal_report"` | — |
| [SRC-4397BC2CD2-L000006](../../tests/test_intent_router_integration.py#L6) | 6 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-4397BC2CD2-L000007](../../tests/test_intent_router_integration.py#L7) | 7 | `""` | — |
| [SRC-4397BC2CD2-L000008](../../tests/test_intent_router_integration.py#L8) | 8 | `""` | — |
| [SRC-4397BC2CD2-L000009](../../tests/test_intent_router_integration.py#L9) | 9 | `"def _evidence(domain: str, queries: list[str]) -> dict:"` | — |
| [SRC-4397BC2CD2-L000010](../../tests/test_intent_router_integration.py#L10) | 10 | `"    return {"` | — |
| [SRC-4397BC2CD2-L000011](../../tests/test_intent_router_integration.py#L11) | 11 | `"        \"title\": \"iPhone 17 price information in Egypt\","` | — |
| [SRC-4397BC2CD2-L000012](../../tests/test_intent_router_integration.py#L12) | 12 | `"        \"url\": f\"https://{domain}/iphone-17-price\","` | — |
| [SRC-4397BC2CD2-L000013](../../tests/test_intent_router_integration.py#L13) | 13 | `"        \"snippet\": \"Published price information for iPhone 17 in Egypt.\","` | — |
| [SRC-4397BC2CD2-L000014](../../tests/test_intent_router_integration.py#L14) | 14 | `"        \"page_text\": \"Price information for iPhone 17 in Egypt.\","` | — |
| [SRC-4397BC2CD2-L000015](../../tests/test_intent_router_integration.py#L15) | 15 | `"        \"page_fetched\": True,"` | — |
| [SRC-4397BC2CD2-L000016](../../tests/test_intent_router_integration.py#L16) | 16 | `"        \"providers\": [\"test_search\"],"` | — |
| [SRC-4397BC2CD2-L000017](../../tests/test_intent_router_integration.py#L17) | 17 | `"        \"queries\": list(queries),"` | — |
| [SRC-4397BC2CD2-L000018](../../tests/test_intent_router_integration.py#L18) | 18 | `"        \"domain\": domain,"` | — |
| [SRC-4397BC2CD2-L000019](../../tests/test_intent_router_integration.py#L19) | 19 | `"        \"source_class\": \"general\","` | — |
| [SRC-4397BC2CD2-L000020](../../tests/test_intent_router_integration.py#L20) | 20 | `"        \"platform\": \"web\","` | — |
| [SRC-4397BC2CD2-L000021](../../tests/test_intent_router_integration.py#L21) | 21 | `"        \"published_at\": \"\","` | — |
| [SRC-4397BC2CD2-L000022](../../tests/test_intent_router_integration.py#L22) | 22 | `"        \"rank_score\": 1.0,"` | — |
| [SRC-4397BC2CD2-L000023](../../tests/test_intent_router_integration.py#L23) | 23 | `"    }"` | — |
| [SRC-4397BC2CD2-L000024](../../tests/test_intent_router_integration.py#L24) | 24 | `""` | — |
| [SRC-4397BC2CD2-L000025](../../tests/test_intent_router_integration.py#L25) | 25 | `""` | — |
| [SRC-4397BC2CD2-L000026](../../tests/test_intent_router_integration.py#L26) | 26 | `"def _report(plan: dict, sources: list[dict]) -> dict:"` | — |
| [SRC-4397BC2CD2-L000027](../../tests/test_intent_router_integration.py#L27) | 27 | `"    return {"` | — |
| [SRC-4397BC2CD2-L000028](../../tests/test_intent_router_integration.py#L28) | 28 | `"        \"queries_planned\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-4397BC2CD2-L000029](../../tests/test_intent_router_integration.py#L29) | 29 | `"        \"queries_attempted\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-4397BC2CD2-L000030](../../tests/test_intent_router_integration.py#L30) | 30 | `"        \"query_results\": [],"` | — |
| [SRC-4397BC2CD2-L000031](../../tests/test_intent_router_integration.py#L31) | 31 | `"        \"unique_sources\": len(sources),"` | — |
| [SRC-4397BC2CD2-L000032](../../tests/test_intent_router_integration.py#L32) | 32 | `"        \"pages_fetched\": len(sources),"` | — |
| [SRC-4397BC2CD2-L000033](../../tests/test_intent_router_integration.py#L33) | 33 | `"        \"providers_used\": [\"test_search\"],"` | — |
| [SRC-4397BC2CD2-L000034](../../tests/test_intent_router_integration.py#L34) | 34 | `"        \"provider_counts\": {\"test_search\": len(sources)},"` | — |
| [SRC-4397BC2CD2-L000035](../../tests/test_intent_router_integration.py#L35) | 35 | `"        \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-4397BC2CD2-L000036](../../tests/test_intent_router_integration.py#L36) | 36 | `"        \"social_direct_results\": 0,"` | — |
| [SRC-4397BC2CD2-L000037](../../tests/test_intent_router_integration.py#L37) | 37 | `"        \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-4397BC2CD2-L000038](../../tests/test_intent_router_integration.py#L38) | 38 | `"        \"planning_method\": plan.get(\"planning_method\", \"test\"),"` | — |
| [SRC-4397BC2CD2-L000039](../../tests/test_intent_router_integration.py#L39) | 39 | `"        \"evidence_signals\": evidence_signal_report(sources),"` | — |
| [SRC-4397BC2CD2-L000040](../../tests/test_intent_router_integration.py#L40) | 40 | `"    }"` | — |
| [SRC-4397BC2CD2-L000041](../../tests/test_intent_router_integration.py#L41) | 41 | `""` | — |
| [SRC-4397BC2CD2-L000042](../../tests/test_intent_router_integration.py#L42) | 42 | `""` | — |
| [SRC-4397BC2CD2-L000043](../../tests/test_intent_router_integration.py#L43) | 43 | `"def test_greeting_is_local_without_model_or_search(monkeypatch) -> None:"` | — |
| [SRC-4397BC2CD2-L000044](../../tests/test_intent_router_integration.py#L44) | 44 | `"    agent = WebAgent()"` | — |
| [SRC-4397BC2CD2-L000045](../../tests/test_intent_router_integration.py#L45) | 45 | `""` | — |
| [SRC-4397BC2CD2-L000046](../../tests/test_intent_router_integration.py#L46) | 46 | `"    def unexpected(*args, **kwargs):"` | — |
| [SRC-4397BC2CD2-L000047](../../tests/test_intent_router_integration.py#L47) | 47 | `"        pytest.fail(\"Greeting must not call the model or search.\")"` | — |
| [SRC-4397BC2CD2-L000048](../../tests/test_intent_router_integration.py#L48) | 48 | `""` | — |
| [SRC-4397BC2CD2-L000049](../../tests/test_intent_router_integration.py#L49) | 49 | `"    monkeypatch.setattr(agent, \"_answer_without_search\", unexpected)"` | — |
| [SRC-4397BC2CD2-L000050](../../tests/test_intent_router_integration.py#L50) | 50 | `"    monkeypatch.setattr(agent, \"_plan_search\", unexpected)"` | — |
| [SRC-4397BC2CD2-L000051](../../tests/test_intent_router_integration.py#L51) | 51 | `""` | — |
| [SRC-4397BC2CD2-L000052](../../tests/test_intent_router_integration.py#L52) | 52 | `"    result = agent.answer(\"ازيك؟ عامل ايه النهاردة؟\")"` | — |
| [SRC-4397BC2CD2-L000053](../../tests/test_intent_router_integration.py#L53) | 53 | `""` | — |
| [SRC-4397BC2CD2-L000054](../../tests/test_intent_router_integration.py#L54) | 54 | `"    assert result[\"kind\"] == \"local_conversation\""` | — |
| [SRC-4397BC2CD2-L000055](../../tests/test_intent_router_integration.py#L55) | 55 | `"    assert result[\"intent_route\"] == \"LOCAL\""` | — |
| [SRC-4397BC2CD2-L000056](../../tests/test_intent_router_integration.py#L56) | 56 | `"    assert result[\"research_plan\"][\"intent_route\"] == \"LOCAL\""` | — |
| [SRC-4397BC2CD2-L000057](../../tests/test_intent_router_integration.py#L57) | 57 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-4397BC2CD2-L000058](../../tests/test_intent_router_integration.py#L58) | 58 | `"    assert result[\"used_language_model\"] is False"` | — |
| [SRC-4397BC2CD2-L000059](../../tests/test_intent_router_integration.py#L59) | 59 | `"    assert result[\"sources\"] == []"` | — |
| [SRC-4397BC2CD2-L000060](../../tests/test_intent_router_integration.py#L60) | 60 | `""` | — |
| [SRC-4397BC2CD2-L000061](../../tests/test_intent_router_integration.py#L61) | 61 | `""` | — |
| [SRC-4397BC2CD2-L000062](../../tests/test_intent_router_integration.py#L62) | 62 | `"def test_ambiguous_question_clarifies_without_model_or_search(monkeypatch) -> None:"` | — |
| [SRC-4397BC2CD2-L000063](../../tests/test_intent_router_integration.py#L63) | 63 | `"    agent = WebAgent()"` | — |
| [SRC-4397BC2CD2-L000064](../../tests/test_intent_router_integration.py#L64) | 64 | `""` | — |
| [SRC-4397BC2CD2-L000065](../../tests/test_intent_router_integration.py#L65) | 65 | `"    def unexpected(*args, **kwargs):"` | — |
| [SRC-4397BC2CD2-L000066](../../tests/test_intent_router_integration.py#L66) | 66 | `"        pytest.fail(\"An unresolved referent must be clarified without model/search.\")"` | — |
| [SRC-4397BC2CD2-L000067](../../tests/test_intent_router_integration.py#L67) | 67 | `""` | — |
| [SRC-4397BC2CD2-L000068](../../tests/test_intent_router_integration.py#L68) | 68 | `"    monkeypatch.setattr(agent, \"_answer_without_search\", unexpected)"` | — |
| [SRC-4397BC2CD2-L000069](../../tests/test_intent_router_integration.py#L69) | 69 | `"    monkeypatch.setattr(agent, \"_plan_search\", unexpected)"` | — |
| [SRC-4397BC2CD2-L000070](../../tests/test_intent_router_integration.py#L70) | 70 | `"    monkeypatch.setattr(agent, \"_collect_research\", unexpected)"` | — |
| [SRC-4397BC2CD2-L000071](../../tests/test_intent_router_integration.py#L71) | 71 | `""` | — |
| [SRC-4397BC2CD2-L000072](../../tests/test_intent_router_integration.py#L72) | 72 | `"    result = agent.answer(\"كام سعرها؟\")"` | — |
| [SRC-4397BC2CD2-L000073](../../tests/test_intent_router_integration.py#L73) | 73 | `""` | — |
| [SRC-4397BC2CD2-L000074](../../tests/test_intent_router_integration.py#L74) | 74 | `"    assert result[\"kind\"] == \"clarification_needed\""` | — |
| [SRC-4397BC2CD2-L000075](../../tests/test_intent_router_integration.py#L75) | 75 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-4397BC2CD2-L000076](../../tests/test_intent_router_integration.py#L76) | 76 | `"    assert result[\"research_plan\"][\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-4397BC2CD2-L000077](../../tests/test_intent_router_integration.py#L77) | 77 | `"    assert \"تقصد\" in result[\"answer\"]"` | — |
| [SRC-4397BC2CD2-L000078](../../tests/test_intent_router_integration.py#L78) | 78 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-4397BC2CD2-L000079](../../tests/test_intent_router_integration.py#L79) | 79 | `"    assert result[\"used_language_model\"] is False"` | — |
| [SRC-4397BC2CD2-L000080](../../tests/test_intent_router_integration.py#L80) | 80 | `"    assert result[\"sources\"] == []"` | — |
| [SRC-4397BC2CD2-L000081](../../tests/test_intent_router_integration.py#L81) | 81 | `""` | — |
| [SRC-4397BC2CD2-L000082](../../tests/test_intent_router_integration.py#L82) | 82 | `""` | — |
| [SRC-4397BC2CD2-L000083](../../tests/test_intent_router_integration.py#L83) | 83 | `"def test_contextual_price_followup_searches_with_previous_subject(monkeypatch) -> None:"` | — |
| [SRC-4397BC2CD2-L000084](../../tests/test_intent_router_integration.py#L84) | 84 | `"    agent = WebAgent()"` | — |
| [SRC-4397BC2CD2-L000085](../../tests/test_intent_router_integration.py#L85) | 85 | `"    agent.api_key = \"\"  # Keep this acceptance test deterministic and offline."` | — |
| [SRC-4397BC2CD2-L000086](../../tests/test_intent_router_integration.py#L86) | 86 | `"    seen: dict = {}"` | — |
| [SRC-4397BC2CD2-L000087](../../tests/test_intent_router_integration.py#L87) | 87 | `"    history = ["` | — |
| [SRC-4397BC2CD2-L000088](../../tests/test_intent_router_integration.py#L88) | 88 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-4397BC2CD2-L000089](../../tests/test_intent_router_integration.py#L89) | 89 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن هاتف iPhone 17 في السوق المصري.\"},"` | — |
| [SRC-4397BC2CD2-L000090](../../tests/test_intent_router_integration.py#L90) | 90 | `"    ]"` | — |
| [SRC-4397BC2CD2-L000091](../../tests/test_intent_router_integration.py#L91) | 91 | `""` | — |
| [SRC-4397BC2CD2-L000092](../../tests/test_intent_router_integration.py#L92) | 92 | `"    def collect(plan):"` | — |
| [SRC-4397BC2CD2-L000093](../../tests/test_intent_router_integration.py#L93) | 93 | `"        seen[\"plan\"] = dict(plan)"` | — |
| [SRC-4397BC2CD2-L000094](../../tests/test_intent_router_integration.py#L94) | 94 | `"        sources = ["` | — |
| [SRC-4397BC2CD2-L000095](../../tests/test_intent_router_integration.py#L95) | 95 | `"            _evidence(\"example.com\", plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000096](../../tests/test_intent_router_integration.py#L96) | 96 | `"            _evidence(\"example.net\", plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000097](../../tests/test_intent_router_integration.py#L97) | 97 | `"        ]"` | — |
| [SRC-4397BC2CD2-L000098](../../tests/test_intent_router_integration.py#L98) | 98 | `"        return sources, [], _report(plan, sources)"` | — |
| [SRC-4397BC2CD2-L000099](../../tests/test_intent_router_integration.py#L99) | 99 | `""` | — |
| [SRC-4397BC2CD2-L000100](../../tests/test_intent_router_integration.py#L100) | 100 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-4397BC2CD2-L000101](../../tests/test_intent_router_integration.py#L101) | 101 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-4397BC2CD2-L000102](../../tests/test_intent_router_integration.py#L102) | 102 | `"    def generate(resolved_question, *args, **kwargs):"` | — |
| [SRC-4397BC2CD2-L000103](../../tests/test_intent_router_integration.py#L103) | 103 | `"        seen[\"generation_question\"] = resolved_question"` | — |
| [SRC-4397BC2CD2-L000104](../../tests/test_intent_router_integration.py#L104) | 104 | `"        return \"توجد أسعار مختلفة حسب النسخة [المصدر 1].\""` | — |
| [SRC-4397BC2CD2-L000105](../../tests/test_intent_router_integration.py#L105) | 105 | `""` | — |
| [SRC-4397BC2CD2-L000106](../../tests/test_intent_router_integration.py#L106) | 106 | `"    def review(resolved_question, answer, sources):"` | — |
| [SRC-4397BC2CD2-L000107](../../tests/test_intent_router_integration.py#L107) | 107 | `"        seen[\"review_question\"] = resolved_question"` | — |
| [SRC-4397BC2CD2-L000108](../../tests/test_intent_router_integration.py#L108) | 108 | `"        return answer"` | — |
| [SRC-4397BC2CD2-L000109](../../tests/test_intent_router_integration.py#L109) | 109 | `""` | — |
| [SRC-4397BC2CD2-L000110](../../tests/test_intent_router_integration.py#L110) | 110 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-4397BC2CD2-L000111](../../tests/test_intent_router_integration.py#L111) | 111 | `"    monkeypatch.setattr(agent, \"_review_answer\", review)"` | — |
| [SRC-4397BC2CD2-L000112](../../tests/test_intent_router_integration.py#L112) | 112 | `""` | — |
| [SRC-4397BC2CD2-L000113](../../tests/test_intent_router_integration.py#L113) | 113 | `"    result = agent.answer(\"كام سعرها؟\", history=history)"` | — |
| [SRC-4397BC2CD2-L000114](../../tests/test_intent_router_integration.py#L114) | 114 | `""` | — |
| [SRC-4397BC2CD2-L000115](../../tests/test_intent_router_integration.py#L115) | 115 | `"    assert result[\"intent_route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-4397BC2CD2-L000116](../../tests/test_intent_router_integration.py#L116) | 116 | `"    assert result[\"research_plan\"][\"intent_route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-4397BC2CD2-L000117](../../tests/test_intent_router_integration.py#L117) | 117 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-4397BC2CD2-L000118](../../tests/test_intent_router_integration.py#L118) | 118 | `"    assert result[\"citation_validation\"][\"method\"] == \"numeric_source_index_range_only\""` | — |
| [SRC-4397BC2CD2-L000119](../../tests/test_intent_router_integration.py#L119) | 119 | `"    assert result[\"search_report\"][\"citation_validation\"] == result[\"citation_validation\"]"` | — |
| [SRC-4397BC2CD2-L000120](../../tests/test_intent_router_integration.py#L120) | 120 | `"    assert any(\"iPhone 17\" in query for query in seen[\"plan\"][\"queries\"])"` | — |
| [SRC-4397BC2CD2-L000121](../../tests/test_intent_router_integration.py#L121) | 121 | `"    # The plan already resolved the follow-up for search, but historically generation"` | — |
| [SRC-4397BC2CD2-L000122](../../tests/test_intent_router_integration.py#L122) | 122 | `"    # still received only \"كام سعرها؟\". All answer stages must receive the same context."` | — |
| [SRC-4397BC2CD2-L000123](../../tests/test_intent_router_integration.py#L123) | 123 | `"    assert \"iPhone 17\" in seen[\"generation_question\"]"` | — |
| [SRC-4397BC2CD2-L000124](../../tests/test_intent_router_integration.py#L124) | 124 | `"    assert \"كام سعرها\" in seen[\"generation_question\"]"` | — |
| [SRC-4397BC2CD2-L000125](../../tests/test_intent_router_integration.py#L125) | 125 | `"    assert seen[\"review_question\"] == seen[\"generation_question\"]"` | — |
| [SRC-4397BC2CD2-L000126](../../tests/test_intent_router_integration.py#L126) | 126 | `""` | — |
| [SRC-4397BC2CD2-L000127](../../tests/test_intent_router_integration.py#L127) | 127 | `""` | — |
| [SRC-4397BC2CD2-L000128](../../tests/test_intent_router_integration.py#L128) | 128 | `"def test_multi_part_comparison_forces_deep_plan_and_multiple_angles(monkeypatch) -> None:"` | — |
| [SRC-4397BC2CD2-L000129](../../tests/test_intent_router_integration.py#L129) | 129 | `"    agent = WebAgent()"` | — |
| [SRC-4397BC2CD2-L000130](../../tests/test_intent_router_integration.py#L130) | 130 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-4397BC2CD2-L000131](../../tests/test_intent_router_integration.py#L131) | 131 | `"    seen: dict = {\"plans\": []}"` | — |
| [SRC-4397BC2CD2-L000132](../../tests/test_intent_router_integration.py#L132) | 132 | `"    history = []"` | — |
| [SRC-4397BC2CD2-L000133](../../tests/test_intent_router_integration.py#L133) | 133 | `""` | — |
| [SRC-4397BC2CD2-L000134](../../tests/test_intent_router_integration.py#L134) | 134 | `"    def plan(question, prior_history):"` | — |
| [SRC-4397BC2CD2-L000135](../../tests/test_intent_router_integration.py#L135) | 135 | `"        return {"` | — |
| [SRC-4397BC2CD2-L000136](../../tests/test_intent_router_integration.py#L136) | 136 | `"            \"queries\": [\"iPhone 17 versus Samsung S26\"],"` | — |
| [SRC-4397BC2CD2-L000137](../../tests/test_intent_router_integration.py#L137) | 137 | `"            \"direct_urls\": [],"` | — |
| [SRC-4397BC2CD2-L000138](../../tests/test_intent_router_integration.py#L138) | 138 | `"            \"social_focus\": False,"` | — |
| [SRC-4397BC2CD2-L000139](../../tests/test_intent_router_integration.py#L139) | 139 | `"            \"freshness\": \"any\","` | — |
| [SRC-4397BC2CD2-L000140](../../tests/test_intent_router_integration.py#L140) | 140 | `"            \"depth\": \"standard\","` | — |
| [SRC-4397BC2CD2-L000141](../../tests/test_intent_router_integration.py#L141) | 141 | `"            \"platforms\": [],"` | — |
| [SRC-4397BC2CD2-L000142](../../tests/test_intent_router_integration.py#L142) | 142 | `"            \"planning_method\": \"test_single_query\","` | — |
| [SRC-4397BC2CD2-L000143](../../tests/test_intent_router_integration.py#L143) | 143 | `"        }"` | — |
| [SRC-4397BC2CD2-L000144](../../tests/test_intent_router_integration.py#L144) | 144 | `""` | — |
| [SRC-4397BC2CD2-L000145](../../tests/test_intent_router_integration.py#L145) | 145 | `"    def collect(research_plan):"` | — |
| [SRC-4397BC2CD2-L000146](../../tests/test_intent_router_integration.py#L146) | 146 | `"        seen[\"plans\"].append(dict(research_plan))"` | — |
| [SRC-4397BC2CD2-L000147](../../tests/test_intent_router_integration.py#L147) | 147 | `"        sources = ["` | — |
| [SRC-4397BC2CD2-L000148](../../tests/test_intent_router_integration.py#L148) | 148 | `"            _evidence(\"example.com\", research_plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000149](../../tests/test_intent_router_integration.py#L149) | 149 | `"            _evidence(\"example.net\", research_plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000150](../../tests/test_intent_router_integration.py#L150) | 150 | `"        ]"` | — |
| [SRC-4397BC2CD2-L000151](../../tests/test_intent_router_integration.py#L151) | 151 | `"        return sources, [], _report(research_plan, sources)"` | — |
| [SRC-4397BC2CD2-L000152](../../tests/test_intent_router_integration.py#L152) | 152 | `""` | — |
| [SRC-4397BC2CD2-L000153](../../tests/test_intent_router_integration.py#L153) | 153 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-4397BC2CD2-L000154](../../tests/test_intent_router_integration.py#L154) | 154 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-4397BC2CD2-L000155](../../tests/test_intent_router_integration.py#L155) | 155 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-4397BC2CD2-L000156](../../tests/test_intent_router_integration.py#L156) | 156 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"مقارنة أولية [المصدر 1].\")"` | — |
| [SRC-4397BC2CD2-L000157](../../tests/test_intent_router_integration.py#L157) | 157 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-4397BC2CD2-L000158](../../tests/test_intent_router_integration.py#L158) | 158 | `"    monkeypatch.setattr(agent, \"_repair_answer_coverage\", lambda _q, answer, _s, _m: answer)"` | — |
| [SRC-4397BC2CD2-L000159](../../tests/test_intent_router_integration.py#L159) | 159 | `"    monkeypatch.setattr(agent, \"_verify_semantic_claims\", lambda *args, **kwargs: {"` | — |
| [SRC-4397BC2CD2-L000160](../../tests/test_intent_router_integration.py#L160) | 160 | `"        \"status\": \"completed_all_claims_supported\","` | — |
| [SRC-4397BC2CD2-L000161](../../tests/test_intent_router_integration.py#L161) | 161 | `"        \"withhold_answer\": False,"` | — |
| [SRC-4397BC2CD2-L000162](../../tests/test_intent_router_integration.py#L162) | 162 | `"        \"semantic_verification\": \"model_assessed_source_support\","` | — |
| [SRC-4397BC2CD2-L000163](../../tests/test_intent_router_integration.py#L163) | 163 | `"        \"fact_correctness\": \"not_verified\","` | — |
| [SRC-4397BC2CD2-L000164](../../tests/test_intent_router_integration.py#L164) | 164 | `"    })"` | — |
| [SRC-4397BC2CD2-L000165](../../tests/test_intent_router_integration.py#L165) | 165 | `""` | — |
| [SRC-4397BC2CD2-L000166](../../tests/test_intent_router_integration.py#L166) | 166 | `"    result = agent.answer("` | — |
| [SRC-4397BC2CD2-L000167](../../tests/test_intent_router_integration.py#L167) | 167 | `"        \"قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية والكاميرا\","` | — |
| [SRC-4397BC2CD2-L000168](../../tests/test_intent_router_integration.py#L168) | 168 | `"        history=history,"` | — |
| [SRC-4397BC2CD2-L000169](../../tests/test_intent_router_integration.py#L169) | 169 | `"    )"` | — |
| [SRC-4397BC2CD2-L000170](../../tests/test_intent_router_integration.py#L170) | 170 | `""` | — |
| [SRC-4397BC2CD2-L000171](../../tests/test_intent_router_integration.py#L171) | 171 | `"    assert result[\"intent_route\"] == \"WEB_DEEP\""` | — |
| [SRC-4397BC2CD2-L000172](../../tests/test_intent_router_integration.py#L172) | 172 | `"    assert result[\"research_plan\"][\"intent_route\"] == \"WEB_DEEP\""` | — |
| [SRC-4397BC2CD2-L000173](../../tests/test_intent_router_integration.py#L173) | 173 | `"    assert result[\"research_plan\"][\"depth\"] == \"deep\""` | — |
| [SRC-4397BC2CD2-L000174](../../tests/test_intent_router_integration.py#L174) | 174 | `"    initial_plan = seen[\"plans\"][0]"` | — |
| [SRC-4397BC2CD2-L000175](../../tests/test_intent_router_integration.py#L175) | 175 | `"    assert len(initial_plan[\"queries\"]) > 1"` | — |
| [SRC-4397BC2CD2-L000176](../../tests/test_intent_router_integration.py#L176) | 176 | `"    assert initial_plan[\"coverage_gap_repair_slot_reserved\"] is True"` | — |
| [SRC-4397BC2CD2-L000177](../../tests/test_intent_router_integration.py#L177) | 177 | `"    assert initial_plan[\"query_limit\"] == 7"` | — |
| [SRC-4397BC2CD2-L000178](../../tests/test_intent_router_integration.py#L178) | 178 | `"    # Each requested criterion gets a distinct search angle before generic deep"` | — |
| [SRC-4397BC2CD2-L000179](../../tests/test_intent_router_integration.py#L179) | 179 | `"    # modifiers consume the bounded query budget."` | — |
| [SRC-4397BC2CD2-L000180](../../tests/test_intent_router_integration.py#L180) | 180 | `"    planned_queries = \" \".join(initial_plan[\"queries\"]).casefold()"` | — |
| [SRC-4397BC2CD2-L000181](../../tests/test_intent_router_integration.py#L181) | 181 | `"    assert \"السعر\" in planned_queries"` | — |
| [SRC-4397BC2CD2-L000182](../../tests/test_intent_router_integration.py#L182) | 182 | `"    assert \"البطارية\" in planned_queries"` | — |
| [SRC-4397BC2CD2-L000183](../../tests/test_intent_router_integration.py#L183) | 183 | `"    assert \"الكاميرا\" in planned_queries"` | — |
| [SRC-4397BC2CD2-L000184](../../tests/test_intent_router_integration.py#L184) | 184 | `"    assert len(initial_plan[\"queries\"]) <= 7"` | — |
| [SRC-4397BC2CD2-L000185](../../tests/test_intent_router_integration.py#L185) | 185 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-4397BC2CD2-L000186](../../tests/test_intent_router_integration.py#L186) | 186 | `"    coverage = result[\"answer_coverage\"]"` | — |
| [SRC-4397BC2CD2-L000187](../../tests/test_intent_router_integration.py#L187) | 187 | `"    assert coverage[\"method\"] == \"explicit_criteria_heuristic\""` | — |
| [SRC-4397BC2CD2-L000188](../../tests/test_intent_router_integration.py#L188) | 188 | `"    assert coverage[\"targets\"] == [\"السعر\", \"البطارية\", \"الكاميرا\"]"` | — |
| [SRC-4397BC2CD2-L000189](../../tests/test_intent_router_integration.py#L189) | 189 | `"    assert coverage[\"status\"] == \"model_review_requested_not_machine_verified\""` | — |
| [SRC-4397BC2CD2-L000190](../../tests/test_intent_router_integration.py#L190) | 190 | `"    assert coverage[\"automatically_graded\"] is False"` | — |
| [SRC-4397BC2CD2-L000191](../../tests/test_intent_router_integration.py#L191) | 191 | `"    # The mocked sources do not contain battery/camera evidence. The task must"` | — |
| [SRC-4397BC2CD2-L000192](../../tests/test_intent_router_integration.py#L192) | 192 | `"    # remain visibly incomplete even if the planner generated multiple queries."` | — |
| [SRC-4397BC2CD2-L000193](../../tests/test_intent_router_integration.py#L193) | 193 | `"    assert coverage[\"source_evidence_gap_count\"] == 2"` | — |
| [SRC-4397BC2CD2-L000194](../../tests/test_intent_router_integration.py#L194) | 194 | `"    assert result[\"task_fulfillment_status\"] == \"possible_gap_detected\""` | — |
| [SRC-4397BC2CD2-L000195](../../tests/test_intent_router_integration.py#L195) | 195 | `"    assert len(seen[\"plans\"]) == 2"` | — |
| [SRC-4397BC2CD2-L000196](../../tests/test_intent_router_integration.py#L196) | 196 | `"    assert \"البطارية\" in \" \".join(seen[\"plans\"][1][\"queries\"])"` | — |
| [SRC-4397BC2CD2-L000197](../../tests/test_intent_router_integration.py#L197) | 197 | `"    assert result[\"search_report\"][\"criterion_gap_research\"][\"attempted\"] is True"` | — |
| [SRC-4397BC2CD2-L000198](../../tests/test_intent_router_integration.py#L198) | 198 | `"    assert result[\"search_report\"][\"criterion_gap_research\"][\"status\"] == \"search_completed_no_new_criterion_evidence\""` | — |
| [SRC-4397BC2CD2-L000199](../../tests/test_intent_router_integration.py#L199) | 199 | `""` | — |
| [SRC-4397BC2CD2-L000200](../../tests/test_intent_router_integration.py#L200) | 200 | `"def test_deep_plan_preserves_all_eight_explicit_criteria_within_query_budget(monkeypatch) -> None:"` | — |
| [SRC-4397BC2CD2-L000201](../../tests/test_intent_router_integration.py#L201) | 201 | `"    agent = WebAgent()"` | — |
| [SRC-4397BC2CD2-L000202](../../tests/test_intent_router_integration.py#L202) | 202 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-4397BC2CD2-L000203](../../tests/test_intent_router_integration.py#L203) | 203 | `"    seen: dict = {\"plans\": []}"` | — |
| [SRC-4397BC2CD2-L000204](../../tests/test_intent_router_integration.py#L204) | 204 | `"    question = ("` | — |
| [SRC-4397BC2CD2-L000205](../../tests/test_intent_router_integration.py#L205) | 205 | `"        \"قارن بين خدمات من حيث السعر، الخصوصية، الاعتمادية، الدعم، \""` | — |
| [SRC-4397BC2CD2-L000206](../../tests/test_intent_router_integration.py#L206) | 206 | `"        \"الأمان، السرعة، الجودة، والتوفر\""` | — |
| [SRC-4397BC2CD2-L000207](../../tests/test_intent_router_integration.py#L207) | 207 | `"    )"` | — |
| [SRC-4397BC2CD2-L000208](../../tests/test_intent_router_integration.py#L208) | 208 | `""` | — |
| [SRC-4397BC2CD2-L000209](../../tests/test_intent_router_integration.py#L209) | 209 | `"    def plan(_question, _history):"` | — |
| [SRC-4397BC2CD2-L000210](../../tests/test_intent_router_integration.py#L210) | 210 | `"        return {"` | — |
| [SRC-4397BC2CD2-L000211](../../tests/test_intent_router_integration.py#L211) | 211 | `"            \"queries\": [\"مقارنة الخدمات\"],"` | — |
| [SRC-4397BC2CD2-L000212](../../tests/test_intent_router_integration.py#L212) | 212 | `"            \"direct_urls\": [],"` | — |
| [SRC-4397BC2CD2-L000213](../../tests/test_intent_router_integration.py#L213) | 213 | `"            \"social_focus\": False,"` | — |
| [SRC-4397BC2CD2-L000214](../../tests/test_intent_router_integration.py#L214) | 214 | `"            \"freshness\": \"any\","` | — |
| [SRC-4397BC2CD2-L000215](../../tests/test_intent_router_integration.py#L215) | 215 | `"            \"depth\": \"standard\","` | — |
| [SRC-4397BC2CD2-L000216](../../tests/test_intent_router_integration.py#L216) | 216 | `"            \"platforms\": [],"` | — |
| [SRC-4397BC2CD2-L000217](../../tests/test_intent_router_integration.py#L217) | 217 | `"            \"planning_method\": \"test_single_query\","` | — |
| [SRC-4397BC2CD2-L000218](../../tests/test_intent_router_integration.py#L218) | 218 | `"        }"` | — |
| [SRC-4397BC2CD2-L000219](../../tests/test_intent_router_integration.py#L219) | 219 | `""` | — |
| [SRC-4397BC2CD2-L000220](../../tests/test_intent_router_integration.py#L220) | 220 | `"    def collect(research_plan):"` | — |
| [SRC-4397BC2CD2-L000221](../../tests/test_intent_router_integration.py#L221) | 221 | `"        seen[\"plans\"].append(dict(research_plan))"` | — |
| [SRC-4397BC2CD2-L000222](../../tests/test_intent_router_integration.py#L222) | 222 | `"        sources = ["` | — |
| [SRC-4397BC2CD2-L000223](../../tests/test_intent_router_integration.py#L223) | 223 | `"            _evidence(\"example.com\", research_plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000224](../../tests/test_intent_router_integration.py#L224) | 224 | `"            _evidence(\"example.net\", research_plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000225](../../tests/test_intent_router_integration.py#L225) | 225 | `"        ]"` | — |
| [SRC-4397BC2CD2-L000226](../../tests/test_intent_router_integration.py#L226) | 226 | `"        return sources, [], _report(research_plan, sources)"` | — |
| [SRC-4397BC2CD2-L000227](../../tests/test_intent_router_integration.py#L227) | 227 | `""` | — |
| [SRC-4397BC2CD2-L000228](../../tests/test_intent_router_integration.py#L228) | 228 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-4397BC2CD2-L000229](../../tests/test_intent_router_integration.py#L229) | 229 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-4397BC2CD2-L000230](../../tests/test_intent_router_integration.py#L230) | 230 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda _query, _source: True)"` | — |
| [SRC-4397BC2CD2-L000231](../../tests/test_intent_router_integration.py#L231) | 231 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"مقارنة أولية [المصدر 1].\")"` | — |
| [SRC-4397BC2CD2-L000232](../../tests/test_intent_router_integration.py#L232) | 232 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-4397BC2CD2-L000233](../../tests/test_intent_router_integration.py#L233) | 233 | `"    monkeypatch.setattr(agent, \"_repair_answer_coverage\", lambda _q, answer, _s, _m: answer)"` | — |
| [SRC-4397BC2CD2-L000234](../../tests/test_intent_router_integration.py#L234) | 234 | `""` | — |
| [SRC-4397BC2CD2-L000235](../../tests/test_intent_router_integration.py#L235) | 235 | `"    agent.answer(question, history=[])"` | — |
| [SRC-4397BC2CD2-L000236](../../tests/test_intent_router_integration.py#L236) | 236 | `""` | — |
| [SRC-4397BC2CD2-L000237](../../tests/test_intent_router_integration.py#L237) | 237 | `"    # All eight explicit criteria consume the bounded initial query allowance;"` | — |
| [SRC-4397BC2CD2-L000238](../../tests/test_intent_router_integration.py#L238) | 238 | `"    # the system must not launch an unbudgeted ninth query for coverage repair."` | — |
| [SRC-4397BC2CD2-L000239](../../tests/test_intent_router_integration.py#L239) | 239 | `"    assert len(seen[\"plans\"]) == 1"` | — |
| [SRC-4397BC2CD2-L000240](../../tests/test_intent_router_integration.py#L240) | 240 | `"    targets = WebAgent._question_coverage_targets(question)"` | — |
| [SRC-4397BC2CD2-L000241](../../tests/test_intent_router_integration.py#L241) | 241 | `"    assert len(targets) == 8"` | — |
| [SRC-4397BC2CD2-L000242](../../tests/test_intent_router_integration.py#L242) | 242 | `"    initial_plan = seen[\"plans\"][0]"` | — |
| [SRC-4397BC2CD2-L000243](../../tests/test_intent_router_integration.py#L243) | 243 | `"    queries = initial_plan[\"queries\"]"` | — |
| [SRC-4397BC2CD2-L000244](../../tests/test_intent_router_integration.py#L244) | 244 | `"    assert initial_plan[\"coverage_gap_repair_slot_reserved\"] is False"` | — |
| [SRC-4397BC2CD2-L000245](../../tests/test_intent_router_integration.py#L245) | 245 | `"    assert initial_plan[\"query_limit\"] == 8"` | — |
| [SRC-4397BC2CD2-L000246](../../tests/test_intent_router_integration.py#L246) | 246 | `"    assert len(queries) == 8"` | — |
| [SRC-4397BC2CD2-L000247](../../tests/test_intent_router_integration.py#L247) | 247 | `"    for target in targets:"` | — |
| [SRC-4397BC2CD2-L000248](../../tests/test_intent_router_integration.py#L248) | 248 | `"        assert any(target in query for query in queries), f\"Missing criterion query for {target!r}\""` | — |
| [SRC-4397BC2CD2-L000249](../../tests/test_intent_router_integration.py#L249) | 249 | `""` | — |
## اختبارات

### FILE-62DC597310 — [tests/test_live_search_connectors.py](../../tests/test_live_search_connectors.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-62DC597310-L000001](../../tests/test_live_search_connectors.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-62DC597310-L000002](../../tests/test_live_search_connectors.py#L2) | 2 | `""` | — |
| [SRC-62DC597310-L000003](../../tests/test_live_search_connectors.py#L3) | 3 | `"import httpx"` | — |
| [SRC-62DC597310-L000004](../../tests/test_live_search_connectors.py#L4) | 4 | `"import pytest"` | — |
| [SRC-62DC597310-L000005](../../tests/test_live_search_connectors.py#L5) | 5 | `""` | — |
| [SRC-62DC597310-L000006](../../tests/test_live_search_connectors.py#L6) | 6 | `"from agents.web_agent import ("` | — |
| [SRC-62DC597310-L000007](../../tests/test_live_search_connectors.py#L7) | 7 | `"    MAX_PROVIDER_RESPONSE_BYTES,"` | — |
| [SRC-62DC597310-L000008](../../tests/test_live_search_connectors.py#L8) | 8 | `"    WebAgent,"` | — |
| [SRC-62DC597310-L000009](../../tests/test_live_search_connectors.py#L9) | 9 | `"    _bounded_http_request,"` | — |
| [SRC-62DC597310-L000010](../../tests/test_live_search_connectors.py#L10) | 10 | `")"` | — |
| [SRC-62DC597310-L000011](../../tests/test_live_search_connectors.py#L11) | 11 | `""` | — |
| [SRC-62DC597310-L000012](../../tests/test_live_search_connectors.py#L12) | 12 | `""` | — |
| [SRC-62DC597310-L000013](../../tests/test_live_search_connectors.py#L13) | 13 | `"class FakeResponse:"` | — |
| [SRC-62DC597310-L000014](../../tests/test_live_search_connectors.py#L14) | 14 | `"    def __init__(self, payload):"` | — |
| [SRC-62DC597310-L000015](../../tests/test_live_search_connectors.py#L15) | 15 | `"        self.payload = payload"` | — |
| [SRC-62DC597310-L000016](../../tests/test_live_search_connectors.py#L16) | 16 | `"        self.status_code = 200"` | — |
| [SRC-62DC597310-L000017](../../tests/test_live_search_connectors.py#L17) | 17 | `""` | — |
| [SRC-62DC597310-L000018](../../tests/test_live_search_connectors.py#L18) | 18 | `"    def raise_for_status(self):"` | — |
| [SRC-62DC597310-L000019](../../tests/test_live_search_connectors.py#L19) | 19 | `"        return None"` | — |
| [SRC-62DC597310-L000020](../../tests/test_live_search_connectors.py#L20) | 20 | `""` | — |
| [SRC-62DC597310-L000021](../../tests/test_live_search_connectors.py#L21) | 21 | `"    def json(self):"` | — |
| [SRC-62DC597310-L000022](../../tests/test_live_search_connectors.py#L22) | 22 | `"        return self.payload"` | — |
| [SRC-62DC597310-L000023](../../tests/test_live_search_connectors.py#L23) | 23 | `""` | — |
| [SRC-62DC597310-L000024](../../tests/test_live_search_connectors.py#L24) | 24 | `""` | — |
| [SRC-62DC597310-L000025](../../tests/test_live_search_connectors.py#L25) | 25 | `"def test_brave_search_adapter_normalizes_real_api_response(monkeypatch):"` | — |
| [SRC-62DC597310-L000026](../../tests/test_live_search_connectors.py#L26) | 26 | `"    monkeypatch.setenv(\"BRAVE_SEARCH_API_KEY\", \"unit-test-secret\")"` | — |
| [SRC-62DC597310-L000027](../../tests/test_live_search_connectors.py#L27) | 27 | `"    requested = {}"` | — |
| [SRC-62DC597310-L000028](../../tests/test_live_search_connectors.py#L28) | 28 | `""` | — |
| [SRC-62DC597310-L000029](../../tests/test_live_search_connectors.py#L29) | 29 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-62DC597310-L000030](../../tests/test_live_search_connectors.py#L30) | 30 | `"        requested[\"url\"] = url"` | — |
| [SRC-62DC597310-L000031](../../tests/test_live_search_connectors.py#L31) | 31 | `"        requested.update(kwargs)"` | — |
| [SRC-62DC597310-L000032](../../tests/test_live_search_connectors.py#L32) | 32 | `"        return FakeResponse({"` | — |
| [SRC-62DC597310-L000033](../../tests/test_live_search_connectors.py#L33) | 33 | `"            \"web\": {"` | — |
| [SRC-62DC597310-L000034](../../tests/test_live_search_connectors.py#L34) | 34 | `"                \"results\": [{"` | — |
| [SRC-62DC597310-L000035](../../tests/test_live_search_connectors.py#L35) | 35 | `"                    \"title\": \"Current research\","` | — |
| [SRC-62DC597310-L000036](../../tests/test_live_search_connectors.py#L36) | 36 | `"                    \"url\": \"https://example.org/research\","` | — |
| [SRC-62DC597310-L000037](../../tests/test_live_search_connectors.py#L37) | 37 | `"                    \"description\": \"A substantive search result.\","` | — |
| [SRC-62DC597310-L000038](../../tests/test_live_search_connectors.py#L38) | 38 | `"                    \"page_age\": \"October 10, 2026\","` | — |
| [SRC-62DC597310-L000039](../../tests/test_live_search_connectors.py#L39) | 39 | `"                }]"` | — |
| [SRC-62DC597310-L000040](../../tests/test_live_search_connectors.py#L40) | 40 | `"            }"` | — |
| [SRC-62DC597310-L000041](../../tests/test_live_search_connectors.py#L41) | 41 | `"        })"` | — |
| [SRC-62DC597310-L000042](../../tests/test_live_search_connectors.py#L42) | 42 | `""` | — |
| [SRC-62DC597310-L000043](../../tests/test_live_search_connectors.py#L43) | 43 | `"    monkeypatch.setattr("` | — |
| [SRC-62DC597310-L000044](../../tests/test_live_search_connectors.py#L44) | 44 | `"        \"agents.web_agent._bounded_http_request\","` | — |
| [SRC-62DC597310-L000045](../../tests/test_live_search_connectors.py#L45) | 45 | `"        lambda method, url, **kwargs: fake_get(url, **kwargs),"` | — |
| [SRC-62DC597310-L000046](../../tests/test_live_search_connectors.py#L46) | 46 | `"    )"` | — |
| [SRC-62DC597310-L000047](../../tests/test_live_search_connectors.py#L47) | 47 | `"    rows = WebAgent()._search_brave(\"بحث حديث\")"` | — |
| [SRC-62DC597310-L000048](../../tests/test_live_search_connectors.py#L48) | 48 | `"    assert requested[\"url\"] == \"https://api.search.brave.com/res/v1/web/search\""` | — |
| [SRC-62DC597310-L000049](../../tests/test_live_search_connectors.py#L49) | 49 | `"    assert requested[\"headers\"][\"X-Subscription-Token\"] == \"unit-test-secret\""` | — |
| [SRC-62DC597310-L000050](../../tests/test_live_search_connectors.py#L50) | 50 | `"    assert requested[\"params\"][\"country\"] == \"EG\""` | — |
| [SRC-62DC597310-L000051](../../tests/test_live_search_connectors.py#L51) | 51 | `"    assert rows[0][\"provider\"] == \"brave_search_api\""` | — |
| [SRC-62DC597310-L000052](../../tests/test_live_search_connectors.py#L52) | 52 | `"    assert rows[0][\"published_at\"] == \"October 10, 2026\""` | — |
| [SRC-62DC597310-L000053](../../tests/test_live_search_connectors.py#L53) | 53 | `"    assert \"unit-test-secret\" not in str(rows)"` | — |
| [SRC-62DC597310-L000054](../../tests/test_live_search_connectors.py#L54) | 54 | `""` | — |
| [SRC-62DC597310-L000055](../../tests/test_live_search_connectors.py#L55) | 55 | `""` | — |
| [SRC-62DC597310-L000056](../../tests/test_live_search_connectors.py#L56) | 56 | `"def test_tavily_search_adapter_normalizes_live_search_results(monkeypatch):"` | — |
| [SRC-62DC597310-L000057](../../tests/test_live_search_connectors.py#L57) | 57 | `"    monkeypatch.setenv(\"TAVILY_API_KEY\", \"unit-test-tavily-secret\")"` | — |
| [SRC-62DC597310-L000058](../../tests/test_live_search_connectors.py#L58) | 58 | `"    requested = {}"` | — |
| [SRC-62DC597310-L000059](../../tests/test_live_search_connectors.py#L59) | 59 | `""` | — |
| [SRC-62DC597310-L000060](../../tests/test_live_search_connectors.py#L60) | 60 | `"    def fake_post(url, **kwargs):"` | — |
| [SRC-62DC597310-L000061](../../tests/test_live_search_connectors.py#L61) | 61 | `"        requested[\"url\"] = url"` | — |
| [SRC-62DC597310-L000062](../../tests/test_live_search_connectors.py#L62) | 62 | `"        requested.update(kwargs)"` | — |
| [SRC-62DC597310-L000063](../../tests/test_live_search_connectors.py#L63) | 63 | `"        return FakeResponse({"` | — |
| [SRC-62DC597310-L000064](../../tests/test_live_search_connectors.py#L64) | 64 | `"            \"results\": [{"` | — |
| [SRC-62DC597310-L000065](../../tests/test_live_search_connectors.py#L65) | 65 | `"                \"title\": \"Official report\","` | — |
| [SRC-62DC597310-L000066](../../tests/test_live_search_connectors.py#L66) | 66 | `"                \"url\": \"https://example.org/report\","` | — |
| [SRC-62DC597310-L000067](../../tests/test_live_search_connectors.py#L67) | 67 | `"                \"content\": \"A source excerpt from the search response.\","` | — |
| [SRC-62DC597310-L000068](../../tests/test_live_search_connectors.py#L68) | 68 | `"                \"published_date\": \"2026-10-11\","` | — |
| [SRC-62DC597310-L000069](../../tests/test_live_search_connectors.py#L69) | 69 | `"            }]"` | — |
| [SRC-62DC597310-L000070](../../tests/test_live_search_connectors.py#L70) | 70 | `"        })"` | — |
| [SRC-62DC597310-L000071](../../tests/test_live_search_connectors.py#L71) | 71 | `""` | — |
| [SRC-62DC597310-L000072](../../tests/test_live_search_connectors.py#L72) | 72 | `"    monkeypatch.setattr("` | — |
| [SRC-62DC597310-L000073](../../tests/test_live_search_connectors.py#L73) | 73 | `"        \"agents.web_agent._bounded_http_request\","` | — |
| [SRC-62DC597310-L000074](../../tests/test_live_search_connectors.py#L74) | 74 | `"        lambda method, url, **kwargs: fake_post(url, **kwargs),"` | — |
| [SRC-62DC597310-L000075](../../tests/test_live_search_connectors.py#L75) | 75 | `"    )"` | — |
| [SRC-62DC597310-L000076](../../tests/test_live_search_connectors.py#L76) | 76 | `"    rows = WebAgent()._search_tavily(\"official sources report\")"` | — |
| [SRC-62DC597310-L000077](../../tests/test_live_search_connectors.py#L77) | 77 | `"    assert requested[\"url\"] == \"https://api.tavily.com/search\""` | — |
| [SRC-62DC597310-L000078](../../tests/test_live_search_connectors.py#L78) | 78 | `"    assert requested[\"json\"][\"api_key\"] == \"unit-test-tavily-secret\""` | — |
| [SRC-62DC597310-L000079](../../tests/test_live_search_connectors.py#L79) | 79 | `"    assert requested[\"json\"][\"include_answer\"] is False"` | — |
| [SRC-62DC597310-L000080](../../tests/test_live_search_connectors.py#L80) | 80 | `"    assert rows[0][\"provider\"] == \"tavily_search_api\""` | — |
| [SRC-62DC597310-L000081](../../tests/test_live_search_connectors.py#L81) | 81 | `"    assert rows[0][\"snippet\"].startswith(\"A source excerpt\")"` | — |
| [SRC-62DC597310-L000082](../../tests/test_live_search_connectors.py#L82) | 82 | `"    assert \"unit-test-tavily-secret\" not in str(rows)"` | — |
| [SRC-62DC597310-L000083](../../tests/test_live_search_connectors.py#L83) | 83 | `""` | — |
| [SRC-62DC597310-L000084](../../tests/test_live_search_connectors.py#L84) | 84 | `""` | — |
| [SRC-62DC597310-L000085](../../tests/test_live_search_connectors.py#L85) | 85 | `"def test_search_api_setup_status_reports_only_presence_not_secret_values(monkeypatch):"` | — |
| [SRC-62DC597310-L000086](../../tests/test_live_search_connectors.py#L86) | 86 | `"    monkeypatch.setenv(\"BRAVE_SEARCH_API_KEY\", \"brave-secret\")"` | — |
| [SRC-62DC597310-L000087](../../tests/test_live_search_connectors.py#L87) | 87 | `"    monkeypatch.setenv(\"TAVILY_API_KEY\", \"tavily-secret\")"` | — |
| [SRC-62DC597310-L000088](../../tests/test_live_search_connectors.py#L88) | 88 | `"    status = WebAgent.status()"` | — |
| [SRC-62DC597310-L000089](../../tests/test_live_search_connectors.py#L89) | 89 | `"    assert status[\"brave_search_api_configured\"] is True"` | — |
| [SRC-62DC597310-L000090](../../tests/test_live_search_connectors.py#L90) | 90 | `"    assert status[\"tavily_search_api_configured\"] is True"` | — |
| [SRC-62DC597310-L000091](../../tests/test_live_search_connectors.py#L91) | 91 | `"    assert \"brave-secret\" not in str(status)"` | — |
| [SRC-62DC597310-L000092](../../tests/test_live_search_connectors.py#L92) | 92 | `"    assert \"tavily-secret\" not in str(status)"` | — |
| [SRC-62DC597310-L000093](../../tests/test_live_search_connectors.py#L93) | 93 | `""` | — |
| [SRC-62DC597310-L000094](../../tests/test_live_search_connectors.py#L94) | 94 | `""` | — |
| [SRC-62DC597310-L000095](../../tests/test_live_search_connectors.py#L95) | 95 | `""` | — |
| [SRC-62DC597310-L000096](../../tests/test_live_search_connectors.py#L96) | 96 | `"def test_bounded_provider_transport_caps_streamed_bytes_even_when_length_lies(monkeypatch):"` | — |
| [SRC-62DC597310-L000097](../../tests/test_live_search_connectors.py#L97) | 97 | `"    chunks_read = []"` | — |
| [SRC-62DC597310-L000098](../../tests/test_live_search_connectors.py#L98) | 98 | `"    observed = {}"` | — |
| [SRC-62DC597310-L000099](../../tests/test_live_search_connectors.py#L99) | 99 | `""` | — |
| [SRC-62DC597310-L000100](../../tests/test_live_search_connectors.py#L100) | 100 | `"    class FakeResponse:"` | — |
| [SRC-62DC597310-L000101](../../tests/test_live_search_connectors.py#L101) | 101 | `"        status_code = 200"` | — |
| [SRC-62DC597310-L000102](../../tests/test_live_search_connectors.py#L102) | 102 | `""` | — |
| [SRC-62DC597310-L000103](../../tests/test_live_search_connectors.py#L103) | 103 | `"        def __init__(self):"` | — |
| [SRC-62DC597310-L000104](../../tests/test_live_search_connectors.py#L104) | 104 | `"            self.headers = {\"content-length\": \"1\"}"` | — |
| [SRC-62DC597310-L000105](../../tests/test_live_search_connectors.py#L105) | 105 | `"            self.request = httpx.Request(\"GET\", \"https://provider.example/search\")"` | — |
| [SRC-62DC597310-L000106](../../tests/test_live_search_connectors.py#L106) | 106 | `""` | — |
| [SRC-62DC597310-L000107](../../tests/test_live_search_connectors.py#L107) | 107 | `"        def __enter__(self):"` | — |
| [SRC-62DC597310-L000108](../../tests/test_live_search_connectors.py#L108) | 108 | `"            return self"` | — |
| [SRC-62DC597310-L000109](../../tests/test_live_search_connectors.py#L109) | 109 | `""` | — |
| [SRC-62DC597310-L000110](../../tests/test_live_search_connectors.py#L110) | 110 | `"        def __exit__(self, *_args):"` | — |
| [SRC-62DC597310-L000111](../../tests/test_live_search_connectors.py#L111) | 111 | `"            return False"` | — |
| [SRC-62DC597310-L000112](../../tests/test_live_search_connectors.py#L112) | 112 | `""` | — |
| [SRC-62DC597310-L000113](../../tests/test_live_search_connectors.py#L113) | 113 | `"        def iter_bytes(self):"` | — |
| [SRC-62DC597310-L000114](../../tests/test_live_search_connectors.py#L114) | 114 | `"            for chunk in ("` | — |
| [SRC-62DC597310-L000115](../../tests/test_live_search_connectors.py#L115) | 115 | `"                b\"A\" * MAX_PROVIDER_RESPONSE_BYTES,"` | — |
| [SRC-62DC597310-L000116](../../tests/test_live_search_connectors.py#L116) | 116 | `"                b\"B\","` | — |
| [SRC-62DC597310-L000117](../../tests/test_live_search_connectors.py#L117) | 117 | `"                b\"C\","` | — |
| [SRC-62DC597310-L000118](../../tests/test_live_search_connectors.py#L118) | 118 | `"            ):"` | — |
| [SRC-62DC597310-L000119](../../tests/test_live_search_connectors.py#L119) | 119 | `"                chunks_read.append(len(chunk))"` | — |
| [SRC-62DC597310-L000120](../../tests/test_live_search_connectors.py#L120) | 120 | `"                yield chunk"` | — |
| [SRC-62DC597310-L000121](../../tests/test_live_search_connectors.py#L121) | 121 | `""` | — |
| [SRC-62DC597310-L000122](../../tests/test_live_search_connectors.py#L122) | 122 | `"    class FakeClient:"` | — |
| [SRC-62DC597310-L000123](../../tests/test_live_search_connectors.py#L123) | 123 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-62DC597310-L000124](../../tests/test_live_search_connectors.py#L124) | 124 | `"            observed[\"client_options\"] = kwargs"` | — |
| [SRC-62DC597310-L000125](../../tests/test_live_search_connectors.py#L125) | 125 | `""` | — |
| [SRC-62DC597310-L000126](../../tests/test_live_search_connectors.py#L126) | 126 | `"        def __enter__(self):"` | — |
| [SRC-62DC597310-L000127](../../tests/test_live_search_connectors.py#L127) | 127 | `"            return self"` | — |
| [SRC-62DC597310-L000128](../../tests/test_live_search_connectors.py#L128) | 128 | `""` | — |
| [SRC-62DC597310-L000129](../../tests/test_live_search_connectors.py#L129) | 129 | `"        def __exit__(self, *_args):"` | — |
| [SRC-62DC597310-L000130](../../tests/test_live_search_connectors.py#L130) | 130 | `"            return False"` | — |
| [SRC-62DC597310-L000131](../../tests/test_live_search_connectors.py#L131) | 131 | `""` | — |
| [SRC-62DC597310-L000132](../../tests/test_live_search_connectors.py#L132) | 132 | `"        def stream(self, method, url, **kwargs):"` | — |
| [SRC-62DC597310-L000133](../../tests/test_live_search_connectors.py#L133) | 133 | `"            observed[\"method\"] = method"` | — |
| [SRC-62DC597310-L000134](../../tests/test_live_search_connectors.py#L134) | 134 | `"            observed[\"url\"] = url"` | — |
| [SRC-62DC597310-L000135](../../tests/test_live_search_connectors.py#L135) | 135 | `"            observed[\"request_options\"] = kwargs"` | — |
| [SRC-62DC597310-L000136](../../tests/test_live_search_connectors.py#L136) | 136 | `"            return FakeResponse()"` | — |
| [SRC-62DC597310-L000137](../../tests/test_live_search_connectors.py#L137) | 137 | `""` | — |
| [SRC-62DC597310-L000138](../../tests/test_live_search_connectors.py#L138) | 138 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-62DC597310-L000139](../../tests/test_live_search_connectors.py#L139) | 139 | `"    with pytest.raises(ValueError, match=\"size limit\"):"` | — |
| [SRC-62DC597310-L000140](../../tests/test_live_search_connectors.py#L140) | 140 | `"        _bounded_http_request("` | — |
| [SRC-62DC597310-L000141](../../tests/test_live_search_connectors.py#L141) | 141 | `"            \"GET\","` | — |
| [SRC-62DC597310-L000142](../../tests/test_live_search_connectors.py#L142) | 142 | `"            \"https://provider.example/search\","` | — |
| [SRC-62DC597310-L000143](../../tests/test_live_search_connectors.py#L143) | 143 | `"            timeout=4.0,"` | — |
| [SRC-62DC597310-L000144](../../tests/test_live_search_connectors.py#L144) | 144 | `"            follow_redirects=True,"` | — |
| [SRC-62DC597310-L000145](../../tests/test_live_search_connectors.py#L145) | 145 | `"            params={\"q\": \"test\"},"` | — |
| [SRC-62DC597310-L000146](../../tests/test_live_search_connectors.py#L146) | 146 | `"        )"` | — |
| [SRC-62DC597310-L000147](../../tests/test_live_search_connectors.py#L147) | 147 | `""` | — |
| [SRC-62DC597310-L000148](../../tests/test_live_search_connectors.py#L148) | 148 | `"    assert observed[\"client_options\"][\"timeout\"] == 4.0"` | — |
| [SRC-62DC597310-L000149](../../tests/test_live_search_connectors.py#L149) | 149 | `"    assert observed[\"client_options\"][\"follow_redirects\"] is False"` | — |
| [SRC-62DC597310-L000150](../../tests/test_live_search_connectors.py#L150) | 150 | `"    assert observed[\"client_options\"][\"trust_env\"] is False"` | — |
| [SRC-62DC597310-L000151](../../tests/test_live_search_connectors.py#L151) | 151 | `"    assert observed[\"method\"] == \"GET\""` | — |
| [SRC-62DC597310-L000152](../../tests/test_live_search_connectors.py#L152) | 152 | `"    assert observed[\"url\"] == \"https://provider.example/search\""` | — |
| [SRC-62DC597310-L000153](../../tests/test_live_search_connectors.py#L153) | 153 | `"    assert observed[\"request_options\"] == {\"params\": {\"q\": \"test\"}}"` | — |
| [SRC-62DC597310-L000154](../../tests/test_live_search_connectors.py#L154) | 154 | `"    assert chunks_read == [MAX_PROVIDER_RESPONSE_BYTES, 1]"` | — |
| [SRC-62DC597310-L000155](../../tests/test_live_search_connectors.py#L155) | 155 | `""` | — |
| [SRC-62DC597310-L000156](../../tests/test_live_search_connectors.py#L156) | 156 | `""` | — |
| [SRC-62DC597310-L000157](../../tests/test_live_search_connectors.py#L157) | 157 | `"def test_bounded_provider_transport_returns_buffered_response(monkeypatch):"` | — |
| [SRC-62DC597310-L000158](../../tests/test_live_search_connectors.py#L158) | 158 | `"    payload = b'{\"results\":[{\"title\":\"bounded\"}]}'"` | — |
| [SRC-62DC597310-L000159](../../tests/test_live_search_connectors.py#L159) | 159 | `"    observed = {}"` | — |
| [SRC-62DC597310-L000160](../../tests/test_live_search_connectors.py#L160) | 160 | `""` | — |
| [SRC-62DC597310-L000161](../../tests/test_live_search_connectors.py#L161) | 161 | `"    class FakeResponse:"` | — |
| [SRC-62DC597310-L000162](../../tests/test_live_search_connectors.py#L162) | 162 | `"        status_code = 200"` | — |
| [SRC-62DC597310-L000163](../../tests/test_live_search_connectors.py#L163) | 163 | `""` | — |
| [SRC-62DC597310-L000164](../../tests/test_live_search_connectors.py#L164) | 164 | `"        def __init__(self):"` | — |
| [SRC-62DC597310-L000165](../../tests/test_live_search_connectors.py#L165) | 165 | `"            self.headers = {\"content-type\": \"application/json\"}"` | — |
| [SRC-62DC597310-L000166](../../tests/test_live_search_connectors.py#L166) | 166 | `"            self.request = httpx.Request(\"POST\", \"https://provider.example/search\")"` | — |
| [SRC-62DC597310-L000167](../../tests/test_live_search_connectors.py#L167) | 167 | `""` | — |
| [SRC-62DC597310-L000168](../../tests/test_live_search_connectors.py#L168) | 168 | `"        def __enter__(self):"` | — |
| [SRC-62DC597310-L000169](../../tests/test_live_search_connectors.py#L169) | 169 | `"            return self"` | — |
| [SRC-62DC597310-L000170](../../tests/test_live_search_connectors.py#L170) | 170 | `""` | — |
| [SRC-62DC597310-L000171](../../tests/test_live_search_connectors.py#L171) | 171 | `"        def __exit__(self, *_args):"` | — |
| [SRC-62DC597310-L000172](../../tests/test_live_search_connectors.py#L172) | 172 | `"            return False"` | — |
| [SRC-62DC597310-L000173](../../tests/test_live_search_connectors.py#L173) | 173 | `""` | — |
| [SRC-62DC597310-L000174](../../tests/test_live_search_connectors.py#L174) | 174 | `"        def iter_bytes(self):"` | — |
| [SRC-62DC597310-L000175](../../tests/test_live_search_connectors.py#L175) | 175 | `"            yield payload[:10]"` | — |
| [SRC-62DC597310-L000176](../../tests/test_live_search_connectors.py#L176) | 176 | `"            yield payload[10:]"` | — |
| [SRC-62DC597310-L000177](../../tests/test_live_search_connectors.py#L177) | 177 | `""` | — |
| [SRC-62DC597310-L000178](../../tests/test_live_search_connectors.py#L178) | 178 | `"    class FakeClient:"` | — |
| [SRC-62DC597310-L000179](../../tests/test_live_search_connectors.py#L179) | 179 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-62DC597310-L000180](../../tests/test_live_search_connectors.py#L180) | 180 | `"            observed[\"client_options\"] = kwargs"` | — |
| [SRC-62DC597310-L000181](../../tests/test_live_search_connectors.py#L181) | 181 | `""` | — |
| [SRC-62DC597310-L000182](../../tests/test_live_search_connectors.py#L182) | 182 | `"        def __enter__(self):"` | — |
| [SRC-62DC597310-L000183](../../tests/test_live_search_connectors.py#L183) | 183 | `"            return self"` | — |
| [SRC-62DC597310-L000184](../../tests/test_live_search_connectors.py#L184) | 184 | `""` | — |
| [SRC-62DC597310-L000185](../../tests/test_live_search_connectors.py#L185) | 185 | `"        def __exit__(self, *_args):"` | — |
| [SRC-62DC597310-L000186](../../tests/test_live_search_connectors.py#L186) | 186 | `"            return False"` | — |
| [SRC-62DC597310-L000187](../../tests/test_live_search_connectors.py#L187) | 187 | `""` | — |
| [SRC-62DC597310-L000188](../../tests/test_live_search_connectors.py#L188) | 188 | `"        def stream(self, method, url, **kwargs):"` | — |
| [SRC-62DC597310-L000189](../../tests/test_live_search_connectors.py#L189) | 189 | `"            observed[\"method\"] = method"` | — |
| [SRC-62DC597310-L000190](../../tests/test_live_search_connectors.py#L190) | 190 | `"            observed[\"request_options\"] = kwargs"` | — |
| [SRC-62DC597310-L000191](../../tests/test_live_search_connectors.py#L191) | 191 | `"            return FakeResponse()"` | — |
| [SRC-62DC597310-L000192](../../tests/test_live_search_connectors.py#L192) | 192 | `""` | — |
| [SRC-62DC597310-L000193](../../tests/test_live_search_connectors.py#L193) | 193 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-62DC597310-L000194](../../tests/test_live_search_connectors.py#L194) | 194 | `"    response = _bounded_http_request("` | — |
| [SRC-62DC597310-L000195](../../tests/test_live_search_connectors.py#L195) | 195 | `"        \"POST\","` | — |
| [SRC-62DC597310-L000196](../../tests/test_live_search_connectors.py#L196) | 196 | `"        \"https://provider.example/search\","` | — |
| [SRC-62DC597310-L000197](../../tests/test_live_search_connectors.py#L197) | 197 | `"        timeout=3.0,"` | — |
| [SRC-62DC597310-L000198](../../tests/test_live_search_connectors.py#L198) | 198 | `"        json={\"query\": \"test\"},"` | — |
| [SRC-62DC597310-L000199](../../tests/test_live_search_connectors.py#L199) | 199 | `"    )"` | — |
| [SRC-62DC597310-L000200](../../tests/test_live_search_connectors.py#L200) | 200 | `""` | — |
| [SRC-62DC597310-L000201](../../tests/test_live_search_connectors.py#L201) | 201 | `"    assert response.status_code == 200"` | — |
| [SRC-62DC597310-L000202](../../tests/test_live_search_connectors.py#L202) | 202 | `"    assert response.json() == {\"results\": [{\"title\": \"bounded\"}]}"` | — |
| [SRC-62DC597310-L000203](../../tests/test_live_search_connectors.py#L203) | 203 | `"    assert observed[\"method\"] == \"POST\""` | — |
| [SRC-62DC597310-L000204](../../tests/test_live_search_connectors.py#L204) | 204 | `"    assert observed[\"request_options\"] == {\"json\": {\"query\": \"test\"}}"` | — |
| [SRC-62DC597310-L000205](../../tests/test_live_search_connectors.py#L205) | 205 | `"    assert observed[\"client_options\"][\"follow_redirects\"] is False"` | — |
| [SRC-62DC597310-L000206](../../tests/test_live_search_connectors.py#L206) | 206 | `"    assert observed[\"client_options\"][\"trust_env\"] is False"` | — |
| [SRC-62DC597310-L000207](../../tests/test_live_search_connectors.py#L207) | 207 | `""` | — |
| [SRC-62DC597310-L000208](../../tests/test_live_search_connectors.py#L208) | 208 | `""` | — |
| [SRC-62DC597310-L000209](../../tests/test_live_search_connectors.py#L209) | 209 | `""` | — |
| [SRC-62DC597310-L000210](../../tests/test_live_search_connectors.py#L210) | 210 | `"def test_bounded_provider_transport_enforces_absolute_total_deadline(monkeypatch):"` | — |
| [SRC-62DC597310-L000211](../../tests/test_live_search_connectors.py#L211) | 211 | `"    chunks_read = []"` | — |
| [SRC-62DC597310-L000212](../../tests/test_live_search_connectors.py#L212) | 212 | `""` | — |
| [SRC-62DC597310-L000213](../../tests/test_live_search_connectors.py#L213) | 213 | `"    class FakeResponse:"` | — |
| [SRC-62DC597310-L000214](../../tests/test_live_search_connectors.py#L214) | 214 | `"        status_code = 200"` | — |
| [SRC-62DC597310-L000215](../../tests/test_live_search_connectors.py#L215) | 215 | `""` | — |
| [SRC-62DC597310-L000216](../../tests/test_live_search_connectors.py#L216) | 216 | `"        def __init__(self):"` | — |
| [SRC-62DC597310-L000217](../../tests/test_live_search_connectors.py#L217) | 217 | `"            self.request = httpx.Request(\"GET\", \"https://provider.example/slow\")"` | — |
| [SRC-62DC597310-L000218](../../tests/test_live_search_connectors.py#L218) | 218 | `"            self.headers = {}"` | — |
| [SRC-62DC597310-L000219](../../tests/test_live_search_connectors.py#L219) | 219 | `""` | — |
| [SRC-62DC597310-L000220](../../tests/test_live_search_connectors.py#L220) | 220 | `"        def __enter__(self):"` | — |
| [SRC-62DC597310-L000221](../../tests/test_live_search_connectors.py#L221) | 221 | `"            return self"` | — |
| [SRC-62DC597310-L000222](../../tests/test_live_search_connectors.py#L222) | 222 | `""` | — |
| [SRC-62DC597310-L000223](../../tests/test_live_search_connectors.py#L223) | 223 | `"        def __exit__(self, *_args):"` | — |
| [SRC-62DC597310-L000224](../../tests/test_live_search_connectors.py#L224) | 224 | `"            return False"` | — |
| [SRC-62DC597310-L000225](../../tests/test_live_search_connectors.py#L225) | 225 | `""` | — |
| [SRC-62DC597310-L000226](../../tests/test_live_search_connectors.py#L226) | 226 | `"        def iter_bytes(self):"` | — |
| [SRC-62DC597310-L000227](../../tests/test_live_search_connectors.py#L227) | 227 | `"            for chunk in (b\"first\", b\"second\"):"` | — |
| [SRC-62DC597310-L000228](../../tests/test_live_search_connectors.py#L228) | 228 | `"                chunks_read.append(chunk)"` | — |
| [SRC-62DC597310-L000229](../../tests/test_live_search_connectors.py#L229) | 229 | `"                yield chunk"` | — |
| [SRC-62DC597310-L000230](../../tests/test_live_search_connectors.py#L230) | 230 | `""` | — |
| [SRC-62DC597310-L000231](../../tests/test_live_search_connectors.py#L231) | 231 | `"    class FakeClient:"` | — |
| [SRC-62DC597310-L000232](../../tests/test_live_search_connectors.py#L232) | 232 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-62DC597310-L000233](../../tests/test_live_search_connectors.py#L233) | 233 | `"            assert kwargs[\"timeout\"] == 9.0"` | — |
| [SRC-62DC597310-L000234](../../tests/test_live_search_connectors.py#L234) | 234 | `"            assert kwargs[\"follow_redirects\"] is False"` | — |
| [SRC-62DC597310-L000235](../../tests/test_live_search_connectors.py#L235) | 235 | `""` | — |
| [SRC-62DC597310-L000236](../../tests/test_live_search_connectors.py#L236) | 236 | `"        def __enter__(self):"` | — |
| [SRC-62DC597310-L000237](../../tests/test_live_search_connectors.py#L237) | 237 | `"            return self"` | — |
| [SRC-62DC597310-L000238](../../tests/test_live_search_connectors.py#L238) | 238 | `""` | — |
| [SRC-62DC597310-L000239](../../tests/test_live_search_connectors.py#L239) | 239 | `"        def __exit__(self, *_args):"` | — |
| [SRC-62DC597310-L000240](../../tests/test_live_search_connectors.py#L240) | 240 | `"            return False"` | — |
| [SRC-62DC597310-L000241](../../tests/test_live_search_connectors.py#L241) | 241 | `""` | — |
| [SRC-62DC597310-L000242](../../tests/test_live_search_connectors.py#L242) | 242 | `"        def stream(self, method, url, **kwargs):"` | — |
| [SRC-62DC597310-L000243](../../tests/test_live_search_connectors.py#L243) | 243 | `"            assert method == \"GET\""` | — |
| [SRC-62DC597310-L000244](../../tests/test_live_search_connectors.py#L244) | 244 | `"            return FakeResponse()"` | — |
| [SRC-62DC597310-L000245](../../tests/test_live_search_connectors.py#L245) | 245 | `""` | — |
| [SRC-62DC597310-L000246](../../tests/test_live_search_connectors.py#L246) | 246 | `"    # Start at t=0; the first chunk arrives before the deadline."` | — |
| [SRC-62DC597310-L000247](../../tests/test_live_search_connectors.py#L247) | 247 | `"    # The deadline expires before requesting the second chunk."` | — |
| [SRC-62DC597310-L000248](../../tests/test_live_search_connectors.py#L248) | 248 | `"    clock = iter((0.0, 0.0, 2.0))"` | — |
| [SRC-62DC597310-L000249](../../tests/test_live_search_connectors.py#L249) | 249 | `"    monkeypatch.setattr(\"agents.web_agent.time.monotonic\", lambda: next(clock))"` | — |
| [SRC-62DC597310-L000250](../../tests/test_live_search_connectors.py#L250) | 250 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-62DC597310-L000251](../../tests/test_live_search_connectors.py#L251) | 251 | `""` | — |
| [SRC-62DC597310-L000252](../../tests/test_live_search_connectors.py#L252) | 252 | `"    with pytest.raises(TimeoutError, match=\"total request deadline\"):"` | — |
| [SRC-62DC597310-L000253](../../tests/test_live_search_connectors.py#L253) | 253 | `"        _bounded_http_request("` | — |
| [SRC-62DC597310-L000254](../../tests/test_live_search_connectors.py#L254) | 254 | `"            \"GET\","` | — |
| [SRC-62DC597310-L000255](../../tests/test_live_search_connectors.py#L255) | 255 | `"            \"https://provider.example/slow\","` | — |
| [SRC-62DC597310-L000256](../../tests/test_live_search_connectors.py#L256) | 256 | `"            timeout=9.0,"` | — |
| [SRC-62DC597310-L000257](../../tests/test_live_search_connectors.py#L257) | 257 | `"            total_timeout=1.5,"` | — |
| [SRC-62DC597310-L000258](../../tests/test_live_search_connectors.py#L258) | 258 | `"        )"` | — |
| [SRC-62DC597310-L000259](../../tests/test_live_search_connectors.py#L259) | 259 | `""` | — |
| [SRC-62DC597310-L000260](../../tests/test_live_search_connectors.py#L260) | 260 | `"    assert chunks_read == [b\"first\"]"` | — |
| [SRC-62DC597310-L000261](../../tests/test_live_search_connectors.py#L261) | 261 | `""` | — |
| [SRC-62DC597310-L000262](../../tests/test_live_search_connectors.py#L262) | 262 | `""` | — |
| [SRC-62DC597310-L000263](../../tests/test_live_search_connectors.py#L263) | 263 | `"@pytest.mark.parametrize(\"total_timeout\", [0, -1, float(\"inf\"), \"not-a-number\"])"` | — |
| [SRC-62DC597310-L000264](../../tests/test_live_search_connectors.py#L264) | 264 | `"def test_bounded_provider_transport_rejects_invalid_total_deadlines(total_timeout):"` | — |
| [SRC-62DC597310-L000265](../../tests/test_live_search_connectors.py#L265) | 265 | `"    with pytest.raises(ValueError, match=\"total_timeout\"):"` | — |
| [SRC-62DC597310-L000266](../../tests/test_live_search_connectors.py#L266) | 266 | `"        _bounded_http_request("` | — |
| [SRC-62DC597310-L000267](../../tests/test_live_search_connectors.py#L267) | 267 | `"            \"GET\","` | — |
| [SRC-62DC597310-L000268](../../tests/test_live_search_connectors.py#L268) | 268 | `"            \"https://provider.example/search\","` | — |
| [SRC-62DC597310-L000269](../../tests/test_live_search_connectors.py#L269) | 269 | `"            total_timeout=total_timeout,"` | — |
| [SRC-62DC597310-L000270](../../tests/test_live_search_connectors.py#L270) | 270 | `"        )"` | — |
## اختبارات

### FILE-D67DCEB693 — [tests/test_model_provider_failover.py](../../tests/test_model_provider_failover.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-D67DCEB693-L000001](../../tests/test_model_provider_failover.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-D67DCEB693-L000002](../../tests/test_model_provider_failover.py#L2) | 2 | `""` | — |
| [SRC-D67DCEB693-L000003](../../tests/test_model_provider_failover.py#L3) | 3 | `"import json"` | — |
| [SRC-D67DCEB693-L000004](../../tests/test_model_provider_failover.py#L4) | 4 | `"from urllib.error import HTTPError"` | — |
| [SRC-D67DCEB693-L000005](../../tests/test_model_provider_failover.py#L5) | 5 | `""` | — |
| [SRC-D67DCEB693-L000006](../../tests/test_model_provider_failover.py#L6) | 6 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-D67DCEB693-L000007](../../tests/test_model_provider_failover.py#L7) | 7 | `""` | — |
| [SRC-D67DCEB693-L000008](../../tests/test_model_provider_failover.py#L8) | 8 | `""` | — |
| [SRC-D67DCEB693-L000009](../../tests/test_model_provider_failover.py#L9) | 9 | `"class FakeCompletionResponse:"` | — |
| [SRC-D67DCEB693-L000010](../../tests/test_model_provider_failover.py#L10) | 10 | `"    def __init__(self, answer: str):"` | — |
| [SRC-D67DCEB693-L000011](../../tests/test_model_provider_failover.py#L11) | 11 | `"        self.answer = answer"` | — |
| [SRC-D67DCEB693-L000012](../../tests/test_model_provider_failover.py#L12) | 12 | `""` | — |
| [SRC-D67DCEB693-L000013](../../tests/test_model_provider_failover.py#L13) | 13 | `"    def __enter__(self):"` | — |
| [SRC-D67DCEB693-L000014](../../tests/test_model_provider_failover.py#L14) | 14 | `"        return self"` | — |
| [SRC-D67DCEB693-L000015](../../tests/test_model_provider_failover.py#L15) | 15 | `""` | — |
| [SRC-D67DCEB693-L000016](../../tests/test_model_provider_failover.py#L16) | 16 | `"    def __exit__(self, *_args):"` | — |
| [SRC-D67DCEB693-L000017](../../tests/test_model_provider_failover.py#L17) | 17 | `"        return False"` | — |
| [SRC-D67DCEB693-L000018](../../tests/test_model_provider_failover.py#L18) | 18 | `""` | — |
| [SRC-D67DCEB693-L000019](../../tests/test_model_provider_failover.py#L19) | 19 | `"    def read(self, _limit):"` | — |
| [SRC-D67DCEB693-L000020](../../tests/test_model_provider_failover.py#L20) | 20 | `"        return json.dumps({"` | — |
| [SRC-D67DCEB693-L000021](../../tests/test_model_provider_failover.py#L21) | 21 | `"            \"choices\": [{"` | — |
| [SRC-D67DCEB693-L000022](../../tests/test_model_provider_failover.py#L22) | 22 | `"                \"message\": {\"content\": self.answer},"` | — |
| [SRC-D67DCEB693-L000023](../../tests/test_model_provider_failover.py#L23) | 23 | `"                \"finish_reason\": \"stop\","` | — |
| [SRC-D67DCEB693-L000024](../../tests/test_model_provider_failover.py#L24) | 24 | `"            }]"` | — |
| [SRC-D67DCEB693-L000025](../../tests/test_model_provider_failover.py#L25) | 25 | `"        }).encode(\"utf-8\")"` | — |
| [SRC-D67DCEB693-L000026](../../tests/test_model_provider_failover.py#L26) | 26 | `""` | — |
| [SRC-D67DCEB693-L000027](../../tests/test_model_provider_failover.py#L27) | 27 | `""` | — |
| [SRC-D67DCEB693-L000028](../../tests/test_model_provider_failover.py#L28) | 28 | `"def _clear_model_environment(monkeypatch):"` | — |
| [SRC-D67DCEB693-L000029](../../tests/test_model_provider_failover.py#L29) | 29 | `"    for name in ("` | — |
| [SRC-D67DCEB693-L000030](../../tests/test_model_provider_failover.py#L30) | 30 | `"        \"OMARAI_LLM_API_KEY\","` | — |
| [SRC-D67DCEB693-L000031](../../tests/test_model_provider_failover.py#L31) | 31 | `"        \"OPENROUTER_API_KEY\","` | — |
| [SRC-D67DCEB693-L000032](../../tests/test_model_provider_failover.py#L32) | 32 | `"        \"OMARAI_LLM_BASE_URL\","` | — |
| [SRC-D67DCEB693-L000033](../../tests/test_model_provider_failover.py#L33) | 33 | `"        \"OMARAI_LLM_MODEL\","` | — |
| [SRC-D67DCEB693-L000034](../../tests/test_model_provider_failover.py#L34) | 34 | `"        \"OMARAI_ANSWER_MODEL\","` | — |
| [SRC-D67DCEB693-L000035](../../tests/test_model_provider_failover.py#L35) | 35 | `"        \"OMARAI_PLANNER_MODEL\","` | — |
| [SRC-D67DCEB693-L000036](../../tests/test_model_provider_failover.py#L36) | 36 | `"        \"OMARAI_REVIEW_MODEL\","` | — |
| [SRC-D67DCEB693-L000037](../../tests/test_model_provider_failover.py#L37) | 37 | `"        \"OMARAI_VERIFIER_MODEL\","` | — |
| [SRC-D67DCEB693-L000038](../../tests/test_model_provider_failover.py#L38) | 38 | `"        \"OMARAI_LLM_FALLBACK_MODEL\","` | — |
| [SRC-D67DCEB693-L000039](../../tests/test_model_provider_failover.py#L39) | 39 | `"        \"GEMINI_API_KEY\","` | — |
| [SRC-D67DCEB693-L000040](../../tests/test_model_provider_failover.py#L40) | 40 | `"        \"OMARAI_GEMINI_MODEL\","` | — |
| [SRC-D67DCEB693-L000041](../../tests/test_model_provider_failover.py#L41) | 41 | `"        \"MISTRAL_API_KEY\","` | — |
| [SRC-D67DCEB693-L000042](../../tests/test_model_provider_failover.py#L42) | 42 | `"        \"OMARAI_MISTRAL_MODEL\","` | — |
| [SRC-D67DCEB693-L000043](../../tests/test_model_provider_failover.py#L43) | 43 | `"        \"OMARAI_OPENROUTER_WEB_SEARCH\","` | — |
| [SRC-D67DCEB693-L000044](../../tests/test_model_provider_failover.py#L44) | 44 | `"    ):"` | — |
| [SRC-D67DCEB693-L000045](../../tests/test_model_provider_failover.py#L45) | 45 | `"        monkeypatch.delenv(name, raising=False)"` | — |
| [SRC-D67DCEB693-L000046](../../tests/test_model_provider_failover.py#L46) | 46 | `""` | — |
| [SRC-D67DCEB693-L000047](../../tests/test_model_provider_failover.py#L47) | 47 | `""` | — |
| [SRC-D67DCEB693-L000048](../../tests/test_model_provider_failover.py#L48) | 48 | `"def test_model_provider_configuration_uses_documented_model_defaults(monkeypatch):"` | — |
| [SRC-D67DCEB693-L000049](../../tests/test_model_provider_failover.py#L49) | 49 | `"    _clear_model_environment(monkeypatch)"` | — |
| [SRC-D67DCEB693-L000050](../../tests/test_model_provider_failover.py#L50) | 50 | `"    monkeypatch.setenv(\"OPENROUTER_API_KEY\", \"test-openrouter-secret\")"` | — |
| [SRC-D67DCEB693-L000051](../../tests/test_model_provider_failover.py#L51) | 51 | `"    monkeypatch.setenv(\"GEMINI_API_KEY\", \"test-gemini-secret\")"` | — |
| [SRC-D67DCEB693-L000052](../../tests/test_model_provider_failover.py#L52) | 52 | `"    monkeypatch.setenv(\"MISTRAL_API_KEY\", \"test-mistral-secret\")"` | — |
| [SRC-D67DCEB693-L000053](../../tests/test_model_provider_failover.py#L53) | 53 | `""` | — |
| [SRC-D67DCEB693-L000054](../../tests/test_model_provider_failover.py#L54) | 54 | `"    agent = WebAgent()"` | — |
| [SRC-D67DCEB693-L000055](../../tests/test_model_provider_failover.py#L55) | 55 | `"    status = WebAgent.status()"` | — |
| [SRC-D67DCEB693-L000056](../../tests/test_model_provider_failover.py#L56) | 56 | `""` | — |
| [SRC-D67DCEB693-L000057](../../tests/test_model_provider_failover.py#L57) | 57 | `"    assert [provider[\"name\"] for provider in agent.model_providers] == ["` | — |
| [SRC-D67DCEB693-L000058](../../tests/test_model_provider_failover.py#L58) | 58 | `"        \"openrouter\", \"gemini\", \"mistral\""` | — |
| [SRC-D67DCEB693-L000059](../../tests/test_model_provider_failover.py#L59) | 59 | `"    ]"` | — |
| [SRC-D67DCEB693-L000060](../../tests/test_model_provider_failover.py#L60) | 60 | `"    assert agent.model_providers[1][\"model\"] == \"gemini-3.1-flash-lite\""` | — |
| [SRC-D67DCEB693-L000061](../../tests/test_model_provider_failover.py#L61) | 61 | `"    assert agent.model_providers[2][\"model\"] == \"mistral-small-latest\""` | — |
| [SRC-D67DCEB693-L000062](../../tests/test_model_provider_failover.py#L62) | 62 | `"    assert [provider[\"name\"] for provider in status[\"model_providers\"]] == ["` | — |
| [SRC-D67DCEB693-L000063](../../tests/test_model_provider_failover.py#L63) | 63 | `"        \"openrouter\", \"gemini\", \"mistral\""` | — |
| [SRC-D67DCEB693-L000064](../../tests/test_model_provider_failover.py#L64) | 64 | `"    ]"` | — |
| [SRC-D67DCEB693-L000065](../../tests/test_model_provider_failover.py#L65) | 65 | `"    assert \"test-openrouter-secret\" not in repr(status)"` | — |
| [SRC-D67DCEB693-L000066](../../tests/test_model_provider_failover.py#L66) | 66 | `"    assert \"test-gemini-secret\" not in repr(status)"` | — |
| [SRC-D67DCEB693-L000067](../../tests/test_model_provider_failover.py#L67) | 67 | `"    assert \"test-mistral-secret\" not in repr(status)"` | — |
| [SRC-D67DCEB693-L000068](../../tests/test_model_provider_failover.py#L68) | 68 | `""` | — |
| [SRC-D67DCEB693-L000069](../../tests/test_model_provider_failover.py#L69) | 69 | `""` | — |
| [SRC-D67DCEB693-L000070](../../tests/test_model_provider_failover.py#L70) | 70 | `"def test_gemini_only_configuration_uses_gemini_models_without_openrouter_fallback(monkeypatch):"` | — |
| [SRC-D67DCEB693-L000071](../../tests/test_model_provider_failover.py#L71) | 71 | `"    _clear_model_environment(monkeypatch)"` | — |
| [SRC-D67DCEB693-L000072](../../tests/test_model_provider_failover.py#L72) | 72 | `"    monkeypatch.setenv(\"GEMINI_API_KEY\", \"test-gemini-secret\")"` | — |
| [SRC-D67DCEB693-L000073](../../tests/test_model_provider_failover.py#L73) | 73 | `""` | — |
| [SRC-D67DCEB693-L000074](../../tests/test_model_provider_failover.py#L74) | 74 | `"    agent = WebAgent()"` | — |
| [SRC-D67DCEB693-L000075](../../tests/test_model_provider_failover.py#L75) | 75 | `"    status = WebAgent.status()"` | — |
| [SRC-D67DCEB693-L000076](../../tests/test_model_provider_failover.py#L76) | 76 | `""` | — |
| [SRC-D67DCEB693-L000077](../../tests/test_model_provider_failover.py#L77) | 77 | `"    assert agent.primary_provider == \"gemini\""` | — |
| [SRC-D67DCEB693-L000078](../../tests/test_model_provider_failover.py#L78) | 78 | `"    assert agent.base_url == \"https://generativelanguage.googleapis.com/v1beta/openai\""` | — |
| [SRC-D67DCEB693-L000079](../../tests/test_model_provider_failover.py#L79) | 79 | `"    assert agent.answer_model == \"gemini-3.1-flash-lite\""` | — |
| [SRC-D67DCEB693-L000080](../../tests/test_model_provider_failover.py#L80) | 80 | `"    assert agent.planner_model == agent.answer_model"` | — |
| [SRC-D67DCEB693-L000081](../../tests/test_model_provider_failover.py#L81) | 81 | `"    assert agent.verifier_model == agent.answer_model"` | — |
| [SRC-D67DCEB693-L000082](../../tests/test_model_provider_failover.py#L82) | 82 | `"    assert agent.fallback_model == \"\""` | — |
| [SRC-D67DCEB693-L000083](../../tests/test_model_provider_failover.py#L83) | 83 | `"    assert status[\"language_model_configured\"] is True"` | — |
| [SRC-D67DCEB693-L000084](../../tests/test_model_provider_failover.py#L84) | 84 | `"    assert status[\"semantic_verifier_distinct_from_answer_model\"] is False"` | — |
| [SRC-D67DCEB693-L000085](../../tests/test_model_provider_failover.py#L85) | 85 | `""` | — |
| [SRC-D67DCEB693-L000086](../../tests/test_model_provider_failover.py#L86) | 86 | `""` | — |
| [SRC-D67DCEB693-L000087](../../tests/test_model_provider_failover.py#L87) | 87 | `"def test_model_provider_failover_uses_gemini_after_primary_failure(monkeypatch):"` | — |
| [SRC-D67DCEB693-L000088](../../tests/test_model_provider_failover.py#L88) | 88 | `"    _clear_model_environment(monkeypatch)"` | — |
| [SRC-D67DCEB693-L000089](../../tests/test_model_provider_failover.py#L89) | 89 | `"    monkeypatch.setenv(\"OPENROUTER_API_KEY\", \"test-openrouter-key\")"` | — |
| [SRC-D67DCEB693-L000090](../../tests/test_model_provider_failover.py#L90) | 90 | `"    monkeypatch.setenv(\"GEMINI_API_KEY\", \"test-gemini-key\")"` | — |
| [SRC-D67DCEB693-L000091](../../tests/test_model_provider_failover.py#L91) | 91 | `"    agent = WebAgent()"` | — |
| [SRC-D67DCEB693-L000092](../../tests/test_model_provider_failover.py#L92) | 92 | `"    calls = []"` | — |
| [SRC-D67DCEB693-L000093](../../tests/test_model_provider_failover.py#L93) | 93 | `""` | — |
| [SRC-D67DCEB693-L000094](../../tests/test_model_provider_failover.py#L94) | 94 | `"    def fake_open(request, timeout):"` | — |
| [SRC-D67DCEB693-L000095](../../tests/test_model_provider_failover.py#L95) | 95 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-D67DCEB693-L000096](../../tests/test_model_provider_failover.py#L96) | 96 | `"        calls.append((request.full_url, model, request.get_header(\"Authorization\")))"` | — |
| [SRC-D67DCEB693-L000097](../../tests/test_model_provider_failover.py#L97) | 97 | `"        if \"openrouter.ai\" in request.full_url:"` | — |
| [SRC-D67DCEB693-L000098](../../tests/test_model_provider_failover.py#L98) | 98 | `"            raise HTTPError(request.full_url, 503, \"temporary\", None, None)"` | — |
| [SRC-D67DCEB693-L000099](../../tests/test_model_provider_failover.py#L99) | 99 | `"        return FakeCompletionResponse(\"إجابة Gemini مكتملة\")"` | — |
| [SRC-D67DCEB693-L000100](../../tests/test_model_provider_failover.py#L100) | 100 | `""` | — |
| [SRC-D67DCEB693-L000101](../../tests/test_model_provider_failover.py#L101) | 101 | `"    monkeypatch.setattr(\"agents.web_agent._open_model_request\", fake_open)"` | — |
| [SRC-D67DCEB693-L000102](../../tests/test_model_provider_failover.py#L102) | 102 | `"    answer = agent._request_completion("` | — |
| [SRC-D67DCEB693-L000103](../../tests/test_model_provider_failover.py#L103) | 103 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}], model=agent.answer_model"` | — |
| [SRC-D67DCEB693-L000104](../../tests/test_model_provider_failover.py#L104) | 104 | `"    )"` | — |
| [SRC-D67DCEB693-L000105](../../tests/test_model_provider_failover.py#L105) | 105 | `""` | — |
| [SRC-D67DCEB693-L000106](../../tests/test_model_provider_failover.py#L106) | 106 | `"    assert answer == \"إجابة Gemini مكتملة\""` | — |
| [SRC-D67DCEB693-L000107](../../tests/test_model_provider_failover.py#L107) | 107 | `"    assert [call[1] for call in calls] == ["` | — |
| [SRC-D67DCEB693-L000108](../../tests/test_model_provider_failover.py#L108) | 108 | `"        \"google/gemma-4-31b-it:free\","` | — |
| [SRC-D67DCEB693-L000109](../../tests/test_model_provider_failover.py#L109) | 109 | `"        \"openrouter/free\","` | — |
| [SRC-D67DCEB693-L000110](../../tests/test_model_provider_failover.py#L110) | 110 | `"        \"gemini-3.1-flash-lite\","` | — |
| [SRC-D67DCEB693-L000111](../../tests/test_model_provider_failover.py#L111) | 111 | `"    ]"` | — |
| [SRC-D67DCEB693-L000112](../../tests/test_model_provider_failover.py#L112) | 112 | `"    assert calls[-1][0] == ("` | — |
| [SRC-D67DCEB693-L000113](../../tests/test_model_provider_failover.py#L113) | 113 | `"        \"https://generativelanguage.googleapis.com/v1beta/openai/chat/completions\""` | — |
| [SRC-D67DCEB693-L000114](../../tests/test_model_provider_failover.py#L114) | 114 | `"    )"` | — |
| [SRC-D67DCEB693-L000115](../../tests/test_model_provider_failover.py#L115) | 115 | `"    assert calls[-1][2] == \"Bearer test-gemini-key\""` | — |
| [SRC-D67DCEB693-L000116](../../tests/test_model_provider_failover.py#L116) | 116 | `"    assert agent.model_usage[-1][\"used_model\"] == \"gemini-3.1-flash-lite\""` | — |
| [SRC-D67DCEB693-L000117](../../tests/test_model_provider_failover.py#L117) | 117 | `""` | — |
| [SRC-D67DCEB693-L000118](../../tests/test_model_provider_failover.py#L118) | 118 | `""` | — |
| [SRC-D67DCEB693-L000119](../../tests/test_model_provider_failover.py#L119) | 119 | `"def test_model_provider_failover_reaches_mistral_after_gemini_failure(monkeypatch):"` | — |
| [SRC-D67DCEB693-L000120](../../tests/test_model_provider_failover.py#L120) | 120 | `"    _clear_model_environment(monkeypatch)"` | — |
| [SRC-D67DCEB693-L000121](../../tests/test_model_provider_failover.py#L121) | 121 | `"    monkeypatch.setenv(\"OPENROUTER_API_KEY\", \"test-openrouter-key\")"` | — |
| [SRC-D67DCEB693-L000122](../../tests/test_model_provider_failover.py#L122) | 122 | `"    monkeypatch.setenv(\"GEMINI_API_KEY\", \"test-gemini-key\")"` | — |
| [SRC-D67DCEB693-L000123](../../tests/test_model_provider_failover.py#L123) | 123 | `"    monkeypatch.setenv(\"MISTRAL_API_KEY\", \"test-mistral-key\")"` | — |
| [SRC-D67DCEB693-L000124](../../tests/test_model_provider_failover.py#L124) | 124 | `"    agent = WebAgent()"` | — |
| [SRC-D67DCEB693-L000125](../../tests/test_model_provider_failover.py#L125) | 125 | `"    calls = []"` | — |
| [SRC-D67DCEB693-L000126](../../tests/test_model_provider_failover.py#L126) | 126 | `""` | — |
| [SRC-D67DCEB693-L000127](../../tests/test_model_provider_failover.py#L127) | 127 | `"    def fake_open(request, timeout):"` | — |
| [SRC-D67DCEB693-L000128](../../tests/test_model_provider_failover.py#L128) | 128 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-D67DCEB693-L000129](../../tests/test_model_provider_failover.py#L129) | 129 | `"        calls.append((request.full_url, model, request.get_header(\"Authorization\")))"` | — |
| [SRC-D67DCEB693-L000130](../../tests/test_model_provider_failover.py#L130) | 130 | `"        if \"mistral.ai\" not in request.full_url:"` | — |
| [SRC-D67DCEB693-L000131](../../tests/test_model_provider_failover.py#L131) | 131 | `"            raise HTTPError(request.full_url, 503, \"temporary\", None, None)"` | — |
| [SRC-D67DCEB693-L000132](../../tests/test_model_provider_failover.py#L132) | 132 | `"        return FakeCompletionResponse(\"إجابة Mistral مكتملة\")"` | — |
| [SRC-D67DCEB693-L000133](../../tests/test_model_provider_failover.py#L133) | 133 | `""` | — |
| [SRC-D67DCEB693-L000134](../../tests/test_model_provider_failover.py#L134) | 134 | `"    monkeypatch.setattr(\"agents.web_agent._open_model_request\", fake_open)"` | — |
| [SRC-D67DCEB693-L000135](../../tests/test_model_provider_failover.py#L135) | 135 | `"    answer = agent._request_completion("` | — |
| [SRC-D67DCEB693-L000136](../../tests/test_model_provider_failover.py#L136) | 136 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}], model=agent.answer_model"` | — |
| [SRC-D67DCEB693-L000137](../../tests/test_model_provider_failover.py#L137) | 137 | `"    )"` | — |
| [SRC-D67DCEB693-L000138](../../tests/test_model_provider_failover.py#L138) | 138 | `""` | — |
| [SRC-D67DCEB693-L000139](../../tests/test_model_provider_failover.py#L139) | 139 | `"    assert answer == \"إجابة Mistral مكتملة\""` | — |
| [SRC-D67DCEB693-L000140](../../tests/test_model_provider_failover.py#L140) | 140 | `"    assert [call[1] for call in calls] == ["` | — |
| [SRC-D67DCEB693-L000141](../../tests/test_model_provider_failover.py#L141) | 141 | `"        \"google/gemma-4-31b-it:free\","` | — |
| [SRC-D67DCEB693-L000142](../../tests/test_model_provider_failover.py#L142) | 142 | `"        \"openrouter/free\","` | — |
| [SRC-D67DCEB693-L000143](../../tests/test_model_provider_failover.py#L143) | 143 | `"        \"gemini-3.1-flash-lite\","` | — |
| [SRC-D67DCEB693-L000144](../../tests/test_model_provider_failover.py#L144) | 144 | `"        \"mistral-small-latest\","` | — |
| [SRC-D67DCEB693-L000145](../../tests/test_model_provider_failover.py#L145) | 145 | `"    ]"` | — |
| [SRC-D67DCEB693-L000146](../../tests/test_model_provider_failover.py#L146) | 146 | `"    assert calls[-1][0] == \"https://api.mistral.ai/v1/chat/completions\""` | — |
| [SRC-D67DCEB693-L000147](../../tests/test_model_provider_failover.py#L147) | 147 | `"    assert calls[-1][2] == \"Bearer test-mistral-key\""` | — |
| [SRC-D67DCEB693-L000148](../../tests/test_model_provider_failover.py#L148) | 148 | `"    assert agent.model_usage[-1][\"used_model\"] == \"mistral-small-latest\""` | — |
| [SRC-D67DCEB693-L000149](../../tests/test_model_provider_failover.py#L149) | 149 | `""` | — |
| [SRC-D67DCEB693-L000150](../../tests/test_model_provider_failover.py#L150) | 150 | `""` | — |
| [SRC-D67DCEB693-L000151](../../tests/test_model_provider_failover.py#L151) | 151 | `"def test_semantic_verifier_request_does_not_fail_over_to_another_provider(monkeypatch):"` | — |
| [SRC-D67DCEB693-L000152](../../tests/test_model_provider_failover.py#L152) | 152 | `"    _clear_model_environment(monkeypatch)"` | — |
| [SRC-D67DCEB693-L000153](../../tests/test_model_provider_failover.py#L153) | 153 | `"    monkeypatch.setenv(\"OPENROUTER_API_KEY\", \"test-openrouter-key\")"` | — |
| [SRC-D67DCEB693-L000154](../../tests/test_model_provider_failover.py#L154) | 154 | `"    monkeypatch.setenv(\"GEMINI_API_KEY\", \"test-gemini-key\")"` | — |
| [SRC-D67DCEB693-L000155](../../tests/test_model_provider_failover.py#L155) | 155 | `"    agent = WebAgent()"` | — |
| [SRC-D67DCEB693-L000156](../../tests/test_model_provider_failover.py#L156) | 156 | `"    calls = []"` | — |
| [SRC-D67DCEB693-L000157](../../tests/test_model_provider_failover.py#L157) | 157 | `""` | — |
| [SRC-D67DCEB693-L000158](../../tests/test_model_provider_failover.py#L158) | 158 | `"    def fake_open(request, timeout):"` | — |
| [SRC-D67DCEB693-L000159](../../tests/test_model_provider_failover.py#L159) | 159 | `"        calls.append(request.full_url)"` | — |
| [SRC-D67DCEB693-L000160](../../tests/test_model_provider_failover.py#L160) | 160 | `"        raise HTTPError(request.full_url, 401, \"unauthorized\", None, None)"` | — |
| [SRC-D67DCEB693-L000161](../../tests/test_model_provider_failover.py#L161) | 161 | `""` | — |
| [SRC-D67DCEB693-L000162](../../tests/test_model_provider_failover.py#L162) | 162 | `"    monkeypatch.setattr(\"agents.web_agent._open_model_request\", fake_open)"` | — |
| [SRC-D67DCEB693-L000163](../../tests/test_model_provider_failover.py#L163) | 163 | `"    try:"` | — |
| [SRC-D67DCEB693-L000164](../../tests/test_model_provider_failover.py#L164) | 164 | `"        agent._request_completion("` | — |
| [SRC-D67DCEB693-L000165](../../tests/test_model_provider_failover.py#L165) | 165 | `"            [{\"role\": \"user\", \"content\": \"claim verification\"}],"` | — |
| [SRC-D67DCEB693-L000166](../../tests/test_model_provider_failover.py#L166) | 166 | `"            model=agent.verifier_model,"` | — |
| [SRC-D67DCEB693-L000167](../../tests/test_model_provider_failover.py#L167) | 167 | `"            allow_fallback=False,"` | — |
| [SRC-D67DCEB693-L000168](../../tests/test_model_provider_failover.py#L168) | 168 | `"        )"` | — |
| [SRC-D67DCEB693-L000169](../../tests/test_model_provider_failover.py#L169) | 169 | `"    except RuntimeError as exc:"` | — |
| [SRC-D67DCEB693-L000170](../../tests/test_model_provider_failover.py#L170) | 170 | `"        assert \"HTTP 401\" in str(exc)"` | — |
| [SRC-D67DCEB693-L000171](../../tests/test_model_provider_failover.py#L171) | 171 | `"    else:"` | — |
| [SRC-D67DCEB693-L000172](../../tests/test_model_provider_failover.py#L172) | 172 | `"        raise AssertionError(\"semantic verifier unexpectedly accepted a failed provider request\")"` | — |
| [SRC-D67DCEB693-L000173](../../tests/test_model_provider_failover.py#L173) | 173 | `""` | — |
| [SRC-D67DCEB693-L000174](../../tests/test_model_provider_failover.py#L174) | 174 | `"    assert calls == [\"https://openrouter.ai/api/v1/chat/completions\"]"` | — |
| [SRC-D67DCEB693-L000175](../../tests/test_model_provider_failover.py#L175) | 175 | `""` | — |
| [SRC-D67DCEB693-L000176](../../tests/test_model_provider_failover.py#L176) | 176 | `""` | — |
| [SRC-D67DCEB693-L000177](../../tests/test_model_provider_failover.py#L177) | 177 | `"def test_openrouter_web_search_tool_is_not_sent_to_fallback_provider(monkeypatch):"` | — |
| [SRC-D67DCEB693-L000178](../../tests/test_model_provider_failover.py#L178) | 178 | `"    _clear_model_environment(monkeypatch)"` | — |
| [SRC-D67DCEB693-L000179](../../tests/test_model_provider_failover.py#L179) | 179 | `"    monkeypatch.setenv(\"OPENROUTER_API_KEY\", \"test-openrouter-key\")"` | — |
| [SRC-D67DCEB693-L000180](../../tests/test_model_provider_failover.py#L180) | 180 | `"    monkeypatch.setenv(\"GEMINI_API_KEY\", \"test-gemini-key\")"` | — |
| [SRC-D67DCEB693-L000181](../../tests/test_model_provider_failover.py#L181) | 181 | `"    monkeypatch.setenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"1\")"` | — |
| [SRC-D67DCEB693-L000182](../../tests/test_model_provider_failover.py#L182) | 182 | `"    agent = WebAgent()"` | — |
| [SRC-D67DCEB693-L000183](../../tests/test_model_provider_failover.py#L183) | 183 | `"    observed = []"` | — |
| [SRC-D67DCEB693-L000184](../../tests/test_model_provider_failover.py#L184) | 184 | `""` | — |
| [SRC-D67DCEB693-L000185](../../tests/test_model_provider_failover.py#L185) | 185 | `"    def fake_open(request, timeout):"` | — |
| [SRC-D67DCEB693-L000186](../../tests/test_model_provider_failover.py#L186) | 186 | `"        payload = json.loads(request.data.decode(\"utf-8\"))"` | — |
| [SRC-D67DCEB693-L000187](../../tests/test_model_provider_failover.py#L187) | 187 | `"        observed.append((request.full_url, payload))"` | — |
| [SRC-D67DCEB693-L000188](../../tests/test_model_provider_failover.py#L188) | 188 | `"        if \"openrouter.ai\" in request.full_url:"` | — |
| [SRC-D67DCEB693-L000189](../../tests/test_model_provider_failover.py#L189) | 189 | `"            raise HTTPError(request.full_url, 503, \"temporary\", None, None)"` | — |
| [SRC-D67DCEB693-L000190](../../tests/test_model_provider_failover.py#L190) | 190 | `"        return FakeCompletionResponse(\"إجابة احتياطية\")"` | — |
| [SRC-D67DCEB693-L000191](../../tests/test_model_provider_failover.py#L191) | 191 | `""` | — |
| [SRC-D67DCEB693-L000192](../../tests/test_model_provider_failover.py#L192) | 192 | `"    monkeypatch.setattr(\"agents.web_agent._open_model_request\", fake_open)"` | — |
| [SRC-D67DCEB693-L000193](../../tests/test_model_provider_failover.py#L193) | 193 | `"    answer = agent._request_completion("` | — |
| [SRC-D67DCEB693-L000194](../../tests/test_model_provider_failover.py#L194) | 194 | `"        [{\"role\": \"user\", \"content\": \"ابحث\"}],"` | — |
| [SRC-D67DCEB693-L000195](../../tests/test_model_provider_failover.py#L195) | 195 | `"        model=agent.answer_model,"` | — |
| [SRC-D67DCEB693-L000196](../../tests/test_model_provider_failover.py#L196) | 196 | `"        enable_web_search=True,"` | — |
| [SRC-D67DCEB693-L000197](../../tests/test_model_provider_failover.py#L197) | 197 | `"    )"` | — |
| [SRC-D67DCEB693-L000198](../../tests/test_model_provider_failover.py#L198) | 198 | `""` | — |
| [SRC-D67DCEB693-L000199](../../tests/test_model_provider_failover.py#L199) | 199 | `"    assert answer == \"إجابة احتياطية\""` | — |
| [SRC-D67DCEB693-L000200](../../tests/test_model_provider_failover.py#L200) | 200 | `"    assert observed[0][0].startswith(\"https://openrouter.ai/\")"` | — |
| [SRC-D67DCEB693-L000201](../../tests/test_model_provider_failover.py#L201) | 201 | `"    assert observed[0][1][\"tools\"][0][\"type\"] == \"openrouter:web_search\""` | — |
| [SRC-D67DCEB693-L000202](../../tests/test_model_provider_failover.py#L202) | 202 | `"    assert observed[-1][0].startswith(\"https://generativelanguage.googleapis.com/\")"` | — |
| [SRC-D67DCEB693-L000203](../../tests/test_model_provider_failover.py#L203) | 203 | `"    assert \"tools\" not in observed[-1][1]"` | — |
## اختبارات

### FILE-1521F490CA — [tests/test_multitenant.py](../../tests/test_multitenant.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1521F490CA-L000001](../../tests/test_multitenant.py#L1) | 1 | `"\"\"\"Tenant isolation, migration, and scoped export regression tests.\"\"\""` | — |
| [SRC-1521F490CA-L000002](../../tests/test_multitenant.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-1521F490CA-L000003](../../tests/test_multitenant.py#L3) | 3 | `""` | — |
| [SRC-1521F490CA-L000004](../../tests/test_multitenant.py#L4) | 4 | `"import csv"` | — |
| [SRC-1521F490CA-L000005](../../tests/test_multitenant.py#L5) | 5 | `"import hashlib"` | — |
| [SRC-1521F490CA-L000006](../../tests/test_multitenant.py#L6) | 6 | `"import sqlite3"` | — |
| [SRC-1521F490CA-L000007](../../tests/test_multitenant.py#L7) | 7 | `""` | — |
| [SRC-1521F490CA-L000008](../../tests/test_multitenant.py#L8) | 8 | `"import pytest"` | — |
| [SRC-1521F490CA-L000009](../../tests/test_multitenant.py#L9) | 9 | `""` | — |
| [SRC-1521F490CA-L000010](../../tests/test_multitenant.py#L10) | 10 | `"from agents.omarai import DEFAULT_TENANT_ID, LeadStore, normalize"` | — |
| [SRC-1521F490CA-L000011](../../tests/test_multitenant.py#L11) | 11 | `""` | — |
| [SRC-1521F490CA-L000012](../../tests/test_multitenant.py#L12) | 12 | `""` | — |
| [SRC-1521F490CA-L000013](../../tests/test_multitenant.py#L13) | 13 | `"def _tenant_member(store: LeadStore, name: str, email: str, token: str):"` | — |
| [SRC-1521F490CA-L000014](../../tests/test_multitenant.py#L14) | 14 | `"    tenant_id = store.create_tenant(name, name.casefold())"` | — |
| [SRC-1521F490CA-L000015](../../tests/test_multitenant.py#L15) | 15 | `"    user_id = store.create_user(email, name + \" User\")"` | — |
| [SRC-1521F490CA-L000016](../../tests/test_multitenant.py#L16) | 16 | `"    store.add_membership(tenant_id, user_id, \"sales_agent\")"` | — |
| [SRC-1521F490CA-L000017](../../tests/test_multitenant.py#L17) | 17 | `"    store.create_api_token(token, tenant_id, user_id, label=name)"` | — |
| [SRC-1521F490CA-L000018](../../tests/test_multitenant.py#L18) | 18 | `"    return tenant_id, user_id"` | — |
| [SRC-1521F490CA-L000019](../../tests/test_multitenant.py#L19) | 19 | `""` | — |
| [SRC-1521F490CA-L000020](../../tests/test_multitenant.py#L20) | 20 | `""` | — |
| [SRC-1521F490CA-L000021](../../tests/test_multitenant.py#L21) | 21 | `"def test_tenant_scoped_fingerprints_reads_updates_and_exports(tmp_path):"` | — |
| [SRC-1521F490CA-L000022](../../tests/test_multitenant.py#L22) | 22 | `"    store = LeadStore(tmp_path / \"multi.sqlite3\")"` | — |
| [SRC-1521F490CA-L000023](../../tests/test_multitenant.py#L23) | 23 | `"    tenant_a, _, = _tenant_member("` | — |
| [SRC-1521F490CA-L000024](../../tests/test_multitenant.py#L24) | 24 | `"        store, \"Company A\", \"a@example.test\", \"A\" * 40"` | — |
| [SRC-1521F490CA-L000025](../../tests/test_multitenant.py#L25) | 25 | `"    )"` | — |
| [SRC-1521F490CA-L000026](../../tests/test_multitenant.py#L26) | 26 | `"    tenant_b, _, = _tenant_member("` | — |
| [SRC-1521F490CA-L000027](../../tests/test_multitenant.py#L27) | 27 | `"        store, \"Company B\", \"b@example.test\", \"B\" * 40"` | — |
| [SRC-1521F490CA-L000028](../../tests/test_multitenant.py#L28) | 28 | `"    )"` | — |
| [SRC-1521F490CA-L000029](../../tests/test_multitenant.py#L29) | 29 | `""` | — |
| [SRC-1521F490CA-L000030](../../tests/test_multitenant.py#L30) | 30 | `"    payload = (\"Buyer asks to purchase a product\", \"https://example.test/post/1\")"` | — |
| [SRC-1521F490CA-L000031](../../tests/test_multitenant.py#L31) | 31 | `"    lead_a, created_a = store.add("` | — |
| [SRC-1521F490CA-L000032](../../tests/test_multitenant.py#L32) | 32 | `"        *payload, tenant_id=tenant_a"` | — |
| [SRC-1521F490CA-L000033](../../tests/test_multitenant.py#L33) | 33 | `"    )"` | — |
| [SRC-1521F490CA-L000034](../../tests/test_multitenant.py#L34) | 34 | `"    lead_b, created_b = store.add("` | — |
| [SRC-1521F490CA-L000035](../../tests/test_multitenant.py#L35) | 35 | `"        *payload, tenant_id=tenant_b"` | — |
| [SRC-1521F490CA-L000036](../../tests/test_multitenant.py#L36) | 36 | `"    )"` | — |
| [SRC-1521F490CA-L000037](../../tests/test_multitenant.py#L37) | 37 | `""` | — |
| [SRC-1521F490CA-L000038](../../tests/test_multitenant.py#L38) | 38 | `"    assert created_a is True"` | — |
| [SRC-1521F490CA-L000039](../../tests/test_multitenant.py#L39) | 39 | `"    assert created_b is True"` | — |
| [SRC-1521F490CA-L000040](../../tests/test_multitenant.py#L40) | 40 | `"    assert lead_a[\"id\"] != lead_b[\"id\"]"` | — |
| [SRC-1521F490CA-L000041](../../tests/test_multitenant.py#L41) | 41 | `"    assert lead_a[\"tenant_id\"] == tenant_a"` | — |
| [SRC-1521F490CA-L000042](../../tests/test_multitenant.py#L42) | 42 | `"    assert lead_b[\"tenant_id\"] == tenant_b"` | — |
| [SRC-1521F490CA-L000043](../../tests/test_multitenant.py#L43) | 43 | `"    assert [row[\"id\"] for row in store.list(tenant_id=tenant_a)] == [lead_a[\"id\"]]"` | — |
| [SRC-1521F490CA-L000044](../../tests/test_multitenant.py#L44) | 44 | `"    assert [row[\"id\"] for row in store.list(tenant_id=tenant_b)] == [lead_b[\"id\"]]"` | — |
| [SRC-1521F490CA-L000045](../../tests/test_multitenant.py#L45) | 45 | `""` | — |
| [SRC-1521F490CA-L000046](../../tests/test_multitenant.py#L46) | 46 | `"    assert store.update_status("` | — |
| [SRC-1521F490CA-L000047](../../tests/test_multitenant.py#L47) | 47 | `"        lead_b[\"id\"], \"qualified\", tenant_id=tenant_a"` | — |
| [SRC-1521F490CA-L000048](../../tests/test_multitenant.py#L48) | 48 | `"    ) is None"` | — |
| [SRC-1521F490CA-L000049](../../tests/test_multitenant.py#L49) | 49 | `"    updated_b = store.update_status("` | — |
| [SRC-1521F490CA-L000050](../../tests/test_multitenant.py#L50) | 50 | `"        lead_b[\"id\"], \"qualified\", tenant_id=tenant_b"` | — |
| [SRC-1521F490CA-L000051](../../tests/test_multitenant.py#L51) | 51 | `"    )"` | — |
| [SRC-1521F490CA-L000052](../../tests/test_multitenant.py#L52) | 52 | `"    assert updated_b is not None"` | — |
| [SRC-1521F490CA-L000053](../../tests/test_multitenant.py#L53) | 53 | `"    assert updated_b[\"status\"] == \"qualified\""` | — |
| [SRC-1521F490CA-L000054](../../tests/test_multitenant.py#L54) | 54 | `""` | — |
| [SRC-1521F490CA-L000055](../../tests/test_multitenant.py#L55) | 55 | `"    export_path = tmp_path / \"company-a.csv\""` | — |
| [SRC-1521F490CA-L000056](../../tests/test_multitenant.py#L56) | 56 | `"    assert store.export_csv(export_path, tenant_id=tenant_a) == 1"` | — |
| [SRC-1521F490CA-L000057](../../tests/test_multitenant.py#L57) | 57 | `"    with export_path.open(newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-1521F490CA-L000058](../../tests/test_multitenant.py#L58) | 58 | `"        rows = list(csv.DictReader(stream))"` | — |
| [SRC-1521F490CA-L000059](../../tests/test_multitenant.py#L59) | 59 | `"    assert len(rows) == 1"` | — |
| [SRC-1521F490CA-L000060](../../tests/test_multitenant.py#L60) | 60 | `"    assert rows[0][\"tenant_id\"] == tenant_a"` | — |
| [SRC-1521F490CA-L000061](../../tests/test_multitenant.py#L61) | 61 | `"    assert rows[0][\"id\"] == lead_a[\"id\"]"` | — |
| [SRC-1521F490CA-L000062](../../tests/test_multitenant.py#L62) | 62 | `""` | — |
| [SRC-1521F490CA-L000063](../../tests/test_multitenant.py#L63) | 63 | `""` | — |
| [SRC-1521F490CA-L000064](../../tests/test_multitenant.py#L64) | 64 | `"def test_api_tokens_resolve_only_active_tenant_memberships(tmp_path):"` | — |
| [SRC-1521F490CA-L000065](../../tests/test_multitenant.py#L65) | 65 | `"    store = LeadStore(tmp_path / \"tokens.sqlite3\")"` | — |
| [SRC-1521F490CA-L000066](../../tests/test_multitenant.py#L66) | 66 | `"    tenant_id, user_id = _tenant_member("` | — |
| [SRC-1521F490CA-L000067](../../tests/test_multitenant.py#L67) | 67 | `"        store, \"Company\", \"owner@example.test\", \"C\" * 40"` | — |
| [SRC-1521F490CA-L000068](../../tests/test_multitenant.py#L68) | 68 | `"    )"` | — |
| [SRC-1521F490CA-L000069](../../tests/test_multitenant.py#L69) | 69 | `""` | — |
| [SRC-1521F490CA-L000070](../../tests/test_multitenant.py#L70) | 70 | `"    principal = store.resolve_api_token(\"C\" * 40)"` | — |
| [SRC-1521F490CA-L000071](../../tests/test_multitenant.py#L71) | 71 | `"    assert principal == {"` | — |
| [SRC-1521F490CA-L000072](../../tests/test_multitenant.py#L72) | 72 | `"        \"tenant_id\": tenant_id,"` | — |
| [SRC-1521F490CA-L000073](../../tests/test_multitenant.py#L73) | 73 | `"        \"user_id\": user_id,"` | — |
| [SRC-1521F490CA-L000074](../../tests/test_multitenant.py#L74) | 74 | `"        \"role\": \"sales_agent\","` | — |
| [SRC-1521F490CA-L000075](../../tests/test_multitenant.py#L75) | 75 | `"    }"` | — |
| [SRC-1521F490CA-L000076](../../tests/test_multitenant.py#L76) | 76 | `"    assert store.resolve_api_token(\"X\" * 40) is None"` | — |
