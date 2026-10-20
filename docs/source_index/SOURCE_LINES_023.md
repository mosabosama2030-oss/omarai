# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **023**
- سجلات الأسطر: **800**
- النطاق: SRC-1A176AD4F0-L000152 إلى SRC-01E35ABC46-L000047
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-1A176AD4F0 — [tests/test_hosted_smoke.py](../../tests/test_hosted_smoke.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1A176AD4F0-L000152](../../tests/test_hosted_smoke.py#L152) | 152 | `"        source_thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000153](../../tests/test_hosted_smoke.py#L153) | 153 | `"        destination_thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000154](../../tests/test_hosted_smoke.py#L154) | 154 | `""` | — |
| [SRC-1A176AD4F0-L000155](../../tests/test_hosted_smoke.py#L155) | 155 | `""` | — |
| [SRC-1A176AD4F0-L000156](../../tests/test_hosted_smoke.py#L156) | 156 | `"def test_smoke_refuses_missing_or_short_access_token(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000157](../../tests/test_hosted_smoke.py#L157) | 157 | `"    with pytest.raises(SmokeError, match=\"OMARAI_ACCESS_TOKEN\"):"` | — |
| [SRC-1A176AD4F0-L000158](../../tests/test_hosted_smoke.py#L158) | 158 | `"        run_smoke(hosted_server, \"\", allow_http=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000159](../../tests/test_hosted_smoke.py#L159) | 159 | `""` | — |
| [SRC-1A176AD4F0-L000160](../../tests/test_hosted_smoke.py#L160) | 160 | `""` | — |
| [SRC-1A176AD4F0-L000161](../../tests/test_hosted_smoke.py#L161) | 161 | `"def test_smoke_fails_when_agent_returns_no_live_source(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000162](../../tests/test_hosted_smoke.py#L162) | 162 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000163](../../tests/test_hosted_smoke.py#L163) | 163 | `""` | — |
| [SRC-1A176AD4F0-L000164](../../tests/test_hosted_smoke.py#L164) | 164 | `"    def without_sources(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000165](../../tests/test_hosted_smoke.py#L165) | 165 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000166](../../tests/test_hosted_smoke.py#L166) | 166 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000167](../../tests/test_hosted_smoke.py#L167) | 167 | `"                \"answer\": \"إجابة بلا مصادر\", \"used_web_search\": False,"` | — |
| [SRC-1A176AD4F0-L000168](../../tests/test_hosted_smoke.py#L168) | 168 | `"                \"used_language_model\": True, \"sources\": [],"` | — |
| [SRC-1A176AD4F0-L000169](../../tests/test_hosted_smoke.py#L169) | 169 | `"            }"` | — |
| [SRC-1A176AD4F0-L000170](../../tests/test_hosted_smoke.py#L170) | 170 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000171](../../tests/test_hosted_smoke.py#L171) | 171 | `""` | — |
| [SRC-1A176AD4F0-L000172](../../tests/test_hosted_smoke.py#L172) | 172 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", without_sources)"` | — |
| [SRC-1A176AD4F0-L000173](../../tests/test_hosted_smoke.py#L173) | 173 | `"    with pytest.raises(SmokeError, match=\"usable source URLs\"):"` | — |
| [SRC-1A176AD4F0-L000174](../../tests/test_hosted_smoke.py#L174) | 174 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, timeout=5)"` | — |
## اختبارات

### FILE-EA6EC52573 — [tests/test_intent_router.py](../../tests/test_intent_router.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-EA6EC52573-L000001](../../tests/test_intent_router.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-EA6EC52573-L000002](../../tests/test_intent_router.py#L2) | 2 | `""` | — |
| [SRC-EA6EC52573-L000003](../../tests/test_intent_router.py#L3) | 3 | `"import pytest"` | — |
| [SRC-EA6EC52573-L000004](../../tests/test_intent_router.py#L4) | 4 | `""` | — |
| [SRC-EA6EC52573-L000005](../../tests/test_intent_router.py#L5) | 5 | `"from agents.intent_router import route_intent"` | — |
| [SRC-EA6EC52573-L000006](../../tests/test_intent_router.py#L6) | 6 | `""` | — |
| [SRC-EA6EC52573-L000007](../../tests/test_intent_router.py#L7) | 7 | `""` | — |
| [SRC-EA6EC52573-L000008](../../tests/test_intent_router.py#L8) | 8 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000009](../../tests/test_intent_router.py#L9) | 9 | `"    (\"question\", \"expected\"),"` | — |
| [SRC-EA6EC52573-L000010](../../tests/test_intent_router.py#L10) | 10 | `"    ["` | — |
| [SRC-EA6EC52573-L000011](../../tests/test_intent_router.py#L11) | 11 | `"        (\"ازيك؟ عامل ايه النهاردة؟\", \"LOCAL\"),"` | — |
| [SRC-EA6EC52573-L000012](../../tests/test_intent_router.py#L12) | 12 | `"        (\"Thanks, that helps.\", \"LOCAL\"),"` | — |
| [SRC-EA6EC52573-L000013](../../tests/test_intent_router.py#L13) | 13 | `"        (\"ما عاصمة مصر؟\", \"MODEL_ONLY\"),"` | — |
| [SRC-EA6EC52573-L000014](../../tests/test_intent_router.py#L14) | 14 | `"        (\"كام سعرها؟\", \"CLARIFY\"),"` | — |
| [SRC-EA6EC52573-L000015](../../tests/test_intent_router.py#L15) | 15 | `"        (\"قارنهم\", \"CLARIFY\"),"` | — |
| [SRC-EA6EC52573-L000016](../../tests/test_intent_router.py#L16) | 16 | `"        (\"ما سعر الهاتف اليوم في مصر؟\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000017](../../tests/test_intent_router.py#L17) | 17 | `"        ("` | — |
| [SRC-EA6EC52573-L000018](../../tests/test_intent_router.py#L18) | 18 | `"            \"قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية والكاميرا\","` | — |
| [SRC-EA6EC52573-L000019](../../tests/test_intent_router.py#L19) | 19 | `"            \"WEB_DEEP\","` | — |
| [SRC-EA6EC52573-L000020](../../tests/test_intent_router.py#L20) | 20 | `"        ),"` | — |
| [SRC-EA6EC52573-L000021](../../tests/test_intent_router.py#L21) | 21 | `"    ],"` | — |
| [SRC-EA6EC52573-L000022](../../tests/test_intent_router.py#L22) | 22 | `")"` | — |
| [SRC-EA6EC52573-L000023](../../tests/test_intent_router.py#L23) | 23 | `"def test_deterministic_intent_routes(question: str, expected: str) -> None:"` | — |
| [SRC-EA6EC52573-L000024](../../tests/test_intent_router.py#L24) | 24 | `"    decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000025](../../tests/test_intent_router.py#L25) | 25 | `"    assert decision[\"route\"] == expected"` | — |
| [SRC-EA6EC52573-L000026](../../tests/test_intent_router.py#L26) | 26 | `"    assert decision[\"reason\"]"` | — |
| [SRC-EA6EC52573-L000027](../../tests/test_intent_router.py#L27) | 27 | `""` | — |
| [SRC-EA6EC52573-L000028](../../tests/test_intent_router.py#L28) | 28 | `""` | — |
| [SRC-EA6EC52573-L000029](../../tests/test_intent_router.py#L29) | 29 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000030](../../tests/test_intent_router.py#L30) | 30 | `"    (\"question\", \"expected\"),"` | — |
| [SRC-EA6EC52573-L000031](../../tests/test_intent_router.py#L31) | 31 | `"    ["` | — |
| [SRC-EA6EC52573-L000032](../../tests/test_intent_router.py#L32) | 32 | `"        (\"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\", \"LEAD_GENERATION\"),"` | — |
| [SRC-EA6EC52573-L000033](../../tests/test_intent_router.py#L33) | 33 | `"        (\"ابحث عن شقق للبيع في العاصمة الإدارية\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000034](../../tests/test_intent_router.py#L34) | 34 | `"        (\"Find buyers looking to buy apartments in New Capital\", \"LEAD_GENERATION\"),"` | — |
| [SRC-EA6EC52573-L000035](../../tests/test_intent_router.py#L35) | 35 | `"        (\"لخص الصفحة https://example.com/article\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000036](../../tests/test_intent_router.py#L36) | 36 | `"        (\"Summarize this page https://example.com/article\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000037](../../tests/test_intent_router.py#L37) | 37 | `"        (\"لخص النص التالي: هذا نص تجريبي\", \"MODEL_ONLY\"),"` | — |
| [SRC-EA6EC52573-L000038](../../tests/test_intent_router.py#L38) | 38 | `"    ],"` | — |
| [SRC-EA6EC52573-L000039](../../tests/test_intent_router.py#L39) | 39 | `")"` | — |
| [SRC-EA6EC52573-L000040](../../tests/test_intent_router.py#L40) | 40 | `"def test_lead_generation_and_summarization_routes(question: str, expected: str) -> None:"` | — |
| [SRC-EA6EC52573-L000041](../../tests/test_intent_router.py#L41) | 41 | `"    decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000042](../../tests/test_intent_router.py#L42) | 42 | `"    assert decision[\"route\"] == expected"` | — |
| [SRC-EA6EC52573-L000043](../../tests/test_intent_router.py#L43) | 43 | `"    assert decision[\"reason\"]"` | — |
| [SRC-EA6EC52573-L000044](../../tests/test_intent_router.py#L44) | 44 | `""` | — |
| [SRC-EA6EC52573-L000045](../../tests/test_intent_router.py#L45) | 45 | `""` | — |
| [SRC-EA6EC52573-L000046](../../tests/test_intent_router.py#L46) | 46 | `"def test_generic_explanation_of_lead_generation_is_not_a_lead_search() -> None:"` | — |
| [SRC-EA6EC52573-L000047](../../tests/test_intent_router.py#L47) | 47 | `"    assert route_intent(\"What is lead generation?\")[\"route\"] == \"MODEL_ONLY\""` | — |
| [SRC-EA6EC52573-L000048](../../tests/test_intent_router.py#L48) | 48 | `"    assert route_intent(\"Create a prospect list for apartment buyers\")[\"route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-EA6EC52573-L000049](../../tests/test_intent_router.py#L49) | 49 | `""` | — |
| [SRC-EA6EC52573-L000050](../../tests/test_intent_router.py#L50) | 50 | `""` | — |
| [SRC-EA6EC52573-L000051](../../tests/test_intent_router.py#L51) | 51 | `""` | — |
| [SRC-EA6EC52573-L000052](../../tests/test_intent_router.py#L52) | 52 | `"def test_capability_question_is_local() -> None:"` | — |
| [SRC-EA6EC52573-L000053](../../tests/test_intent_router.py#L53) | 53 | `"    decision = route_intent("` | — |
| [SRC-EA6EC52573-L000054](../../tests/test_intent_router.py#L54) | 54 | `"        \"كيف تستطيع مساعدتي؟\","` | — |
| [SRC-EA6EC52573-L000055](../../tests/test_intent_router.py#L55) | 55 | `"        capability_question=True,"` | — |
| [SRC-EA6EC52573-L000056](../../tests/test_intent_router.py#L56) | 56 | `"        requires_web=False,"` | — |
| [SRC-EA6EC52573-L000057](../../tests/test_intent_router.py#L57) | 57 | `"    )"` | — |
| [SRC-EA6EC52573-L000058](../../tests/test_intent_router.py#L58) | 58 | `"    assert decision[\"route\"] == \"LOCAL\""` | — |
| [SRC-EA6EC52573-L000059](../../tests/test_intent_router.py#L59) | 59 | `"    assert decision[\"reason\"] == \"capability_question\""` | — |
| [SRC-EA6EC52573-L000060](../../tests/test_intent_router.py#L60) | 60 | `""` | — |
| [SRC-EA6EC52573-L000061](../../tests/test_intent_router.py#L61) | 61 | `""` | — |
| [SRC-EA6EC52573-L000062](../../tests/test_intent_router.py#L62) | 62 | `"def test_ambiguous_followup_uses_existing_conversation_context() -> None:"` | — |
| [SRC-EA6EC52573-L000063](../../tests/test_intent_router.py#L63) | 63 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000064](../../tests/test_intent_router.py#L64) | 64 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000065](../../tests/test_intent_router.py#L65) | 65 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن هاتف iPhone 17 في السوق المصري.\"},"` | — |
| [SRC-EA6EC52573-L000066](../../tests/test_intent_router.py#L66) | 66 | `"    ]"` | — |
| [SRC-EA6EC52573-L000067](../../tests/test_intent_router.py#L67) | 67 | `"    decision = route_intent(\"كام سعرها؟\", history, requires_web=True)"` | — |
| [SRC-EA6EC52573-L000068](../../tests/test_intent_router.py#L68) | 68 | `"    assert decision[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000069](../../tests/test_intent_router.py#L69) | 69 | `"    assert decision[\"context_available\"] is True"` | — |
| [SRC-EA6EC52573-L000070](../../tests/test_intent_router.py#L70) | 70 | `"    assert decision[\"needs_clarification\"] is False"` | — |
| [SRC-EA6EC52573-L000071](../../tests/test_intent_router.py#L71) | 71 | `""` | — |
| [SRC-EA6EC52573-L000072](../../tests/test_intent_router.py#L72) | 72 | `""` | — |
| [SRC-EA6EC52573-L000073](../../tests/test_intent_router.py#L73) | 73 | `"def test_comparison_followup_requires_context_before_deep_search() -> None:"` | — |
| [SRC-EA6EC52573-L000074](../../tests/test_intent_router.py#L74) | 74 | `"    assert route_intent(\"قارنهم\")[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000075](../../tests/test_intent_router.py#L75) | 75 | `"    history = [{\"role\": \"user\", \"content\": \"قارن iPhone 17 وSamsung S26\"}]"` | — |
| [SRC-EA6EC52573-L000076](../../tests/test_intent_router.py#L76) | 76 | `"    decision = route_intent(\"قارنهم\", history)"` | — |
| [SRC-EA6EC52573-L000077](../../tests/test_intent_router.py#L77) | 77 | `"    assert decision[\"route\"] == \"WEB_DEEP\""` | — |
| [SRC-EA6EC52573-L000078](../../tests/test_intent_router.py#L78) | 78 | `"    assert decision[\"context_available\"] is True"` | — |
| [SRC-EA6EC52573-L000079](../../tests/test_intent_router.py#L79) | 79 | `""` | — |
| [SRC-EA6EC52573-L000080](../../tests/test_intent_router.py#L80) | 80 | `""` | — |
| [SRC-EA6EC52573-L000081](../../tests/test_intent_router.py#L81) | 81 | `"def test_ambiguous_followup_does_not_reuse_stale_topic_after_acknowledgment() -> None:"` | — |
| [SRC-EA6EC52573-L000082](../../tests/test_intent_router.py#L82) | 82 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000083](../../tests/test_intent_router.py#L83) | 83 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000084](../../tests/test_intent_router.py#L84) | 84 | `"        {\"role\": \"assistant\", \"content\": \"سأساعدك في العثور على أسعار حديثة.\"},"` | — |
| [SRC-EA6EC52573-L000085](../../tests/test_intent_router.py#L85) | 85 | `"        {\"role\": \"user\", \"content\": \"شكرا\"},"` | — |
| [SRC-EA6EC52573-L000086](../../tests/test_intent_router.py#L86) | 86 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-EA6EC52573-L000087](../../tests/test_intent_router.py#L87) | 87 | `"    ]"` | — |
| [SRC-EA6EC52573-L000088](../../tests/test_intent_router.py#L88) | 88 | `"    decision = route_intent(\"كام سعرها؟\", history, requires_web=True)"` | — |
| [SRC-EA6EC52573-L000089](../../tests/test_intent_router.py#L89) | 89 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000090](../../tests/test_intent_router.py#L90) | 90 | `"    assert decision[\"context_available\"] is False"` | — |
| [SRC-EA6EC52573-L000091](../../tests/test_intent_router.py#L91) | 91 | `""` | — |
| [SRC-EA6EC52573-L000092](../../tests/test_intent_router.py#L92) | 92 | `""` | — |
| [SRC-EA6EC52573-L000093](../../tests/test_intent_router.py#L93) | 93 | `"def test_explicit_mode_overrides_conversational_shortcuts() -> None:"` | — |
| [SRC-EA6EC52573-L000094](../../tests/test_intent_router.py#L94) | 94 | `"    assert route_intent(\"ازيك؟\", mode=\"deep\")[\"route\"] == \"WEB_DEEP\""` | — |
| [SRC-EA6EC52573-L000095](../../tests/test_intent_router.py#L95) | 95 | `"    assert route_intent(\"ما سعر الهاتف؟\", mode=\"latest\")[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000096](../../tests/test_intent_router.py#L96) | 96 | `""` | — |
| [SRC-EA6EC52573-L000097](../../tests/test_intent_router.py#L97) | 97 | `""` | — |
| [SRC-EA6EC52573-L000098](../../tests/test_intent_router.py#L98) | 98 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000099](../../tests/test_intent_router.py#L99) | 99 | `"    (\"question\", \"expected_route\", \"expected_reason\"),"` | — |
| [SRC-EA6EC52573-L000100](../../tests/test_intent_router.py#L100) | 100 | `"    ["` | — |
| [SRC-EA6EC52573-L000101](../../tests/test_intent_router.py#L101) | 101 | `"        ("` | — |
| [SRC-EA6EC52573-L000102](../../tests/test_intent_router.py#L102) | 102 | `"            \"لخص الصفحة https://example.com/article\","` | — |
| [SRC-EA6EC52573-L000103](../../tests/test_intent_router.py#L103) | 103 | `"            \"WEB_SIMPLE\","` | — |
| [SRC-EA6EC52573-L000104](../../tests/test_intent_router.py#L104) | 104 | `"            \"summarization_request\","` | — |
| [SRC-EA6EC52573-L000105](../../tests/test_intent_router.py#L105) | 105 | `"        ),"` | — |
| [SRC-EA6EC52573-L000106](../../tests/test_intent_router.py#L106) | 106 | `"        ("` | — |
| [SRC-EA6EC52573-L000107](../../tests/test_intent_router.py#L107) | 107 | `"            \"Summarize this page https://example.com/article\","` | — |
| [SRC-EA6EC52573-L000108](../../tests/test_intent_router.py#L108) | 108 | `"            \"WEB_SIMPLE\","` | — |
| [SRC-EA6EC52573-L000109](../../tests/test_intent_router.py#L109) | 109 | `"            \"summarization_request\","` | — |
| [SRC-EA6EC52573-L000110](../../tests/test_intent_router.py#L110) | 110 | `"        ),"` | — |
| [SRC-EA6EC52573-L000111](../../tests/test_intent_router.py#L111) | 111 | `"        (\"لخص الصفحة\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000112](../../tests/test_intent_router.py#L112) | 112 | `"        (\"لخص لي هذا الرابط\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000113](../../tests/test_intent_router.py#L113) | 113 | `"        (\"summarize the page\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000114](../../tests/test_intent_router.py#L114) | 114 | `"        (\"تلخيص المقال\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000115](../../tests/test_intent_router.py#L115) | 115 | `"        (\"لخص النص التالي: هذا نص تجريبي\", \"MODEL_ONLY\", \"stable_knowledge_or_conversation\"),"` | — |
| [SRC-EA6EC52573-L000116](../../tests/test_intent_router.py#L116) | 116 | `"        (\"Summarize this text: the test content is here\", \"MODEL_ONLY\", \"stable_knowledge_or_conversation\"),"` | — |
| [SRC-EA6EC52573-L000117](../../tests/test_intent_router.py#L117) | 117 | `"    ],"` | — |
| [SRC-EA6EC52573-L000118](../../tests/test_intent_router.py#L118) | 118 | `")"` | — |
| [SRC-EA6EC52573-L000119](../../tests/test_intent_router.py#L119) | 119 | `"def test_summarization_routing_respects_page_text_and_missing_input("` | — |
| [SRC-EA6EC52573-L000120](../../tests/test_intent_router.py#L120) | 120 | `"    question: str, expected_route: str, expected_reason: str"` | — |
| [SRC-EA6EC52573-L000121](../../tests/test_intent_router.py#L121) | 121 | `") -> None:"` | — |
| [SRC-EA6EC52573-L000122](../../tests/test_intent_router.py#L122) | 122 | `"    decision = route_intent(question, [])"` | — |
| [SRC-EA6EC52573-L000123](../../tests/test_intent_router.py#L123) | 123 | `"    assert decision[\"route\"] == expected_route"` | — |
| [SRC-EA6EC52573-L000124](../../tests/test_intent_router.py#L124) | 124 | `"    assert decision[\"reason\"] == expected_reason"` | — |
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
| [SRC-4397BC2CD2-L000102](../../tests/test_intent_router_integration.py#L102) | 102 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"توجد أسعار مختلفة حسب النسخة [المصدر 1].\")"` | — |
| [SRC-4397BC2CD2-L000103](../../tests/test_intent_router_integration.py#L103) | 103 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-4397BC2CD2-L000104](../../tests/test_intent_router_integration.py#L104) | 104 | `""` | — |
| [SRC-4397BC2CD2-L000105](../../tests/test_intent_router_integration.py#L105) | 105 | `"    result = agent.answer(\"كام سعرها؟\", history=history)"` | — |
| [SRC-4397BC2CD2-L000106](../../tests/test_intent_router_integration.py#L106) | 106 | `""` | — |
| [SRC-4397BC2CD2-L000107](../../tests/test_intent_router_integration.py#L107) | 107 | `"    assert result[\"intent_route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-4397BC2CD2-L000108](../../tests/test_intent_router_integration.py#L108) | 108 | `"    assert result[\"research_plan\"][\"intent_route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-4397BC2CD2-L000109](../../tests/test_intent_router_integration.py#L109) | 109 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-4397BC2CD2-L000110](../../tests/test_intent_router_integration.py#L110) | 110 | `"    assert result[\"citation_validation\"][\"method\"] == \"numeric_source_index_range_only\""` | — |
| [SRC-4397BC2CD2-L000111](../../tests/test_intent_router_integration.py#L111) | 111 | `"    assert result[\"search_report\"][\"citation_validation\"] == result[\"citation_validation\"]"` | — |
| [SRC-4397BC2CD2-L000112](../../tests/test_intent_router_integration.py#L112) | 112 | `"    assert any(\"iPhone 17\" in query for query in seen[\"plan\"][\"queries\"])"` | — |
| [SRC-4397BC2CD2-L000113](../../tests/test_intent_router_integration.py#L113) | 113 | `""` | — |
| [SRC-4397BC2CD2-L000114](../../tests/test_intent_router_integration.py#L114) | 114 | `""` | — |
| [SRC-4397BC2CD2-L000115](../../tests/test_intent_router_integration.py#L115) | 115 | `"def test_multi_part_comparison_forces_deep_plan_and_multiple_angles(monkeypatch) -> None:"` | — |
| [SRC-4397BC2CD2-L000116](../../tests/test_intent_router_integration.py#L116) | 116 | `"    agent = WebAgent()"` | — |
| [SRC-4397BC2CD2-L000117](../../tests/test_intent_router_integration.py#L117) | 117 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-4397BC2CD2-L000118](../../tests/test_intent_router_integration.py#L118) | 118 | `"    seen: dict = {}"` | — |
| [SRC-4397BC2CD2-L000119](../../tests/test_intent_router_integration.py#L119) | 119 | `"    history = []"` | — |
| [SRC-4397BC2CD2-L000120](../../tests/test_intent_router_integration.py#L120) | 120 | `""` | — |
| [SRC-4397BC2CD2-L000121](../../tests/test_intent_router_integration.py#L121) | 121 | `"    def plan(question, prior_history):"` | — |
| [SRC-4397BC2CD2-L000122](../../tests/test_intent_router_integration.py#L122) | 122 | `"        return {"` | — |
| [SRC-4397BC2CD2-L000123](../../tests/test_intent_router_integration.py#L123) | 123 | `"            \"queries\": [\"iPhone 17 versus Samsung S26\"],"` | — |
| [SRC-4397BC2CD2-L000124](../../tests/test_intent_router_integration.py#L124) | 124 | `"            \"direct_urls\": [],"` | — |
| [SRC-4397BC2CD2-L000125](../../tests/test_intent_router_integration.py#L125) | 125 | `"            \"social_focus\": False,"` | — |
| [SRC-4397BC2CD2-L000126](../../tests/test_intent_router_integration.py#L126) | 126 | `"            \"freshness\": \"any\","` | — |
| [SRC-4397BC2CD2-L000127](../../tests/test_intent_router_integration.py#L127) | 127 | `"            \"depth\": \"standard\","` | — |
| [SRC-4397BC2CD2-L000128](../../tests/test_intent_router_integration.py#L128) | 128 | `"            \"platforms\": [],"` | — |
| [SRC-4397BC2CD2-L000129](../../tests/test_intent_router_integration.py#L129) | 129 | `"            \"planning_method\": \"test_single_query\","` | — |
| [SRC-4397BC2CD2-L000130](../../tests/test_intent_router_integration.py#L130) | 130 | `"        }"` | — |
| [SRC-4397BC2CD2-L000131](../../tests/test_intent_router_integration.py#L131) | 131 | `""` | — |
| [SRC-4397BC2CD2-L000132](../../tests/test_intent_router_integration.py#L132) | 132 | `"    def collect(research_plan):"` | — |
| [SRC-4397BC2CD2-L000133](../../tests/test_intent_router_integration.py#L133) | 133 | `"        seen[\"plan\"] = dict(research_plan)"` | — |
| [SRC-4397BC2CD2-L000134](../../tests/test_intent_router_integration.py#L134) | 134 | `"        sources = ["` | — |
| [SRC-4397BC2CD2-L000135](../../tests/test_intent_router_integration.py#L135) | 135 | `"            _evidence(\"example.com\", research_plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000136](../../tests/test_intent_router_integration.py#L136) | 136 | `"            _evidence(\"example.net\", research_plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000137](../../tests/test_intent_router_integration.py#L137) | 137 | `"        ]"` | — |
| [SRC-4397BC2CD2-L000138](../../tests/test_intent_router_integration.py#L138) | 138 | `"        return sources, [], _report(research_plan, sources)"` | — |
| [SRC-4397BC2CD2-L000139](../../tests/test_intent_router_integration.py#L139) | 139 | `""` | — |
| [SRC-4397BC2CD2-L000140](../../tests/test_intent_router_integration.py#L140) | 140 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-4397BC2CD2-L000141](../../tests/test_intent_router_integration.py#L141) | 141 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-4397BC2CD2-L000142](../../tests/test_intent_router_integration.py#L142) | 142 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-4397BC2CD2-L000143](../../tests/test_intent_router_integration.py#L143) | 143 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"مقارنة أولية [المصدر 1].\")"` | — |
| [SRC-4397BC2CD2-L000144](../../tests/test_intent_router_integration.py#L144) | 144 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-4397BC2CD2-L000145](../../tests/test_intent_router_integration.py#L145) | 145 | `""` | — |
| [SRC-4397BC2CD2-L000146](../../tests/test_intent_router_integration.py#L146) | 146 | `"    result = agent.answer("` | — |
| [SRC-4397BC2CD2-L000147](../../tests/test_intent_router_integration.py#L147) | 147 | `"        \"قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية والكاميرا\","` | — |
| [SRC-4397BC2CD2-L000148](../../tests/test_intent_router_integration.py#L148) | 148 | `"        history=history,"` | — |
| [SRC-4397BC2CD2-L000149](../../tests/test_intent_router_integration.py#L149) | 149 | `"    )"` | — |
| [SRC-4397BC2CD2-L000150](../../tests/test_intent_router_integration.py#L150) | 150 | `""` | — |
| [SRC-4397BC2CD2-L000151](../../tests/test_intent_router_integration.py#L151) | 151 | `"    assert result[\"intent_route\"] == \"WEB_DEEP\""` | — |
| [SRC-4397BC2CD2-L000152](../../tests/test_intent_router_integration.py#L152) | 152 | `"    assert result[\"research_plan\"][\"intent_route\"] == \"WEB_DEEP\""` | — |
| [SRC-4397BC2CD2-L000153](../../tests/test_intent_router_integration.py#L153) | 153 | `"    assert result[\"research_plan\"][\"depth\"] == \"deep\""` | — |
| [SRC-4397BC2CD2-L000154](../../tests/test_intent_router_integration.py#L154) | 154 | `"    assert len(seen[\"plan\"][\"queries\"]) > 1"` | — |
| [SRC-4397BC2CD2-L000155](../../tests/test_intent_router_integration.py#L155) | 155 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-4397BC2CD2-L000156](../../tests/test_intent_router_integration.py#L156) | 156 | `"    coverage = result[\"answer_coverage\"]"` | — |
| [SRC-4397BC2CD2-L000157](../../tests/test_intent_router_integration.py#L157) | 157 | `"    assert coverage[\"method\"] == \"explicit_criteria_heuristic\""` | — |
| [SRC-4397BC2CD2-L000158](../../tests/test_intent_router_integration.py#L158) | 158 | `"    assert coverage[\"targets\"] == [\"السعر\", \"البطارية\", \"الكاميرا\"]"` | — |
| [SRC-4397BC2CD2-L000159](../../tests/test_intent_router_integration.py#L159) | 159 | `"    assert coverage[\"status\"] == \"model_review_requested_not_machine_verified\""` | — |
| [SRC-4397BC2CD2-L000160](../../tests/test_intent_router_integration.py#L160) | 160 | `"    assert coverage[\"automatically_graded\"] is False"` | — |
## اختبارات

### FILE-62DC597310 — [tests/test_live_search_connectors.py](../../tests/test_live_search_connectors.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-62DC597310-L000001](../../tests/test_live_search_connectors.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-62DC597310-L000002](../../tests/test_live_search_connectors.py#L2) | 2 | `""` | — |
| [SRC-62DC597310-L000003](../../tests/test_live_search_connectors.py#L3) | 3 | `"import httpx"` | — |
| [SRC-62DC597310-L000004](../../tests/test_live_search_connectors.py#L4) | 4 | `""` | — |
| [SRC-62DC597310-L000005](../../tests/test_live_search_connectors.py#L5) | 5 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-62DC597310-L000006](../../tests/test_live_search_connectors.py#L6) | 6 | `""` | — |
| [SRC-62DC597310-L000007](../../tests/test_live_search_connectors.py#L7) | 7 | `""` | — |
| [SRC-62DC597310-L000008](../../tests/test_live_search_connectors.py#L8) | 8 | `"class FakeResponse:"` | — |
| [SRC-62DC597310-L000009](../../tests/test_live_search_connectors.py#L9) | 9 | `"    def __init__(self, payload):"` | — |
| [SRC-62DC597310-L000010](../../tests/test_live_search_connectors.py#L10) | 10 | `"        self.payload = payload"` | — |
| [SRC-62DC597310-L000011](../../tests/test_live_search_connectors.py#L11) | 11 | `"        self.status_code = 200"` | — |
| [SRC-62DC597310-L000012](../../tests/test_live_search_connectors.py#L12) | 12 | `""` | — |
| [SRC-62DC597310-L000013](../../tests/test_live_search_connectors.py#L13) | 13 | `"    def raise_for_status(self):"` | — |
| [SRC-62DC597310-L000014](../../tests/test_live_search_connectors.py#L14) | 14 | `"        return None"` | — |
| [SRC-62DC597310-L000015](../../tests/test_live_search_connectors.py#L15) | 15 | `""` | — |
| [SRC-62DC597310-L000016](../../tests/test_live_search_connectors.py#L16) | 16 | `"    def json(self):"` | — |
| [SRC-62DC597310-L000017](../../tests/test_live_search_connectors.py#L17) | 17 | `"        return self.payload"` | — |
| [SRC-62DC597310-L000018](../../tests/test_live_search_connectors.py#L18) | 18 | `""` | — |
| [SRC-62DC597310-L000019](../../tests/test_live_search_connectors.py#L19) | 19 | `""` | — |
| [SRC-62DC597310-L000020](../../tests/test_live_search_connectors.py#L20) | 20 | `"def test_brave_search_adapter_normalizes_real_api_response(monkeypatch):"` | — |
| [SRC-62DC597310-L000021](../../tests/test_live_search_connectors.py#L21) | 21 | `"    monkeypatch.setenv(\"BRAVE_SEARCH_API_KEY\", \"unit-test-secret\")"` | — |
| [SRC-62DC597310-L000022](../../tests/test_live_search_connectors.py#L22) | 22 | `"    requested = {}"` | — |
| [SRC-62DC597310-L000023](../../tests/test_live_search_connectors.py#L23) | 23 | `""` | — |
| [SRC-62DC597310-L000024](../../tests/test_live_search_connectors.py#L24) | 24 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-62DC597310-L000025](../../tests/test_live_search_connectors.py#L25) | 25 | `"        requested[\"url\"] = url"` | — |
| [SRC-62DC597310-L000026](../../tests/test_live_search_connectors.py#L26) | 26 | `"        requested.update(kwargs)"` | — |
| [SRC-62DC597310-L000027](../../tests/test_live_search_connectors.py#L27) | 27 | `"        return FakeResponse({"` | — |
| [SRC-62DC597310-L000028](../../tests/test_live_search_connectors.py#L28) | 28 | `"            \"web\": {"` | — |
| [SRC-62DC597310-L000029](../../tests/test_live_search_connectors.py#L29) | 29 | `"                \"results\": [{"` | — |
| [SRC-62DC597310-L000030](../../tests/test_live_search_connectors.py#L30) | 30 | `"                    \"title\": \"Current research\","` | — |
| [SRC-62DC597310-L000031](../../tests/test_live_search_connectors.py#L31) | 31 | `"                    \"url\": \"https://example.org/research\","` | — |
| [SRC-62DC597310-L000032](../../tests/test_live_search_connectors.py#L32) | 32 | `"                    \"description\": \"A substantive search result.\","` | — |
| [SRC-62DC597310-L000033](../../tests/test_live_search_connectors.py#L33) | 33 | `"                    \"page_age\": \"October 10, 2026\","` | — |
| [SRC-62DC597310-L000034](../../tests/test_live_search_connectors.py#L34) | 34 | `"                }]"` | — |
| [SRC-62DC597310-L000035](../../tests/test_live_search_connectors.py#L35) | 35 | `"            }"` | — |
| [SRC-62DC597310-L000036](../../tests/test_live_search_connectors.py#L36) | 36 | `"        })"` | — |
| [SRC-62DC597310-L000037](../../tests/test_live_search_connectors.py#L37) | 37 | `""` | — |
| [SRC-62DC597310-L000038](../../tests/test_live_search_connectors.py#L38) | 38 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-62DC597310-L000039](../../tests/test_live_search_connectors.py#L39) | 39 | `"    rows = WebAgent()._search_brave(\"بحث حديث\")"` | — |
| [SRC-62DC597310-L000040](../../tests/test_live_search_connectors.py#L40) | 40 | `"    assert requested[\"url\"] == \"https://api.search.brave.com/res/v1/web/search\""` | — |
| [SRC-62DC597310-L000041](../../tests/test_live_search_connectors.py#L41) | 41 | `"    assert requested[\"headers\"][\"X-Subscription-Token\"] == \"unit-test-secret\""` | — |
| [SRC-62DC597310-L000042](../../tests/test_live_search_connectors.py#L42) | 42 | `"    assert requested[\"params\"][\"country\"] == \"EG\""` | — |
| [SRC-62DC597310-L000043](../../tests/test_live_search_connectors.py#L43) | 43 | `"    assert rows[0][\"provider\"] == \"brave_search_api\""` | — |
| [SRC-62DC597310-L000044](../../tests/test_live_search_connectors.py#L44) | 44 | `"    assert rows[0][\"published_at\"] == \"October 10, 2026\""` | — |
| [SRC-62DC597310-L000045](../../tests/test_live_search_connectors.py#L45) | 45 | `"    assert \"unit-test-secret\" not in str(rows)"` | — |
| [SRC-62DC597310-L000046](../../tests/test_live_search_connectors.py#L46) | 46 | `""` | — |
| [SRC-62DC597310-L000047](../../tests/test_live_search_connectors.py#L47) | 47 | `""` | — |
| [SRC-62DC597310-L000048](../../tests/test_live_search_connectors.py#L48) | 48 | `"def test_tavily_search_adapter_normalizes_live_search_results(monkeypatch):"` | — |
| [SRC-62DC597310-L000049](../../tests/test_live_search_connectors.py#L49) | 49 | `"    monkeypatch.setenv(\"TAVILY_API_KEY\", \"unit-test-tavily-secret\")"` | — |
| [SRC-62DC597310-L000050](../../tests/test_live_search_connectors.py#L50) | 50 | `"    requested = {}"` | — |
| [SRC-62DC597310-L000051](../../tests/test_live_search_connectors.py#L51) | 51 | `""` | — |
| [SRC-62DC597310-L000052](../../tests/test_live_search_connectors.py#L52) | 52 | `"    def fake_post(url, **kwargs):"` | — |
| [SRC-62DC597310-L000053](../../tests/test_live_search_connectors.py#L53) | 53 | `"        requested[\"url\"] = url"` | — |
| [SRC-62DC597310-L000054](../../tests/test_live_search_connectors.py#L54) | 54 | `"        requested.update(kwargs)"` | — |
| [SRC-62DC597310-L000055](../../tests/test_live_search_connectors.py#L55) | 55 | `"        return FakeResponse({"` | — |
| [SRC-62DC597310-L000056](../../tests/test_live_search_connectors.py#L56) | 56 | `"            \"results\": [{"` | — |
| [SRC-62DC597310-L000057](../../tests/test_live_search_connectors.py#L57) | 57 | `"                \"title\": \"Official report\","` | — |
| [SRC-62DC597310-L000058](../../tests/test_live_search_connectors.py#L58) | 58 | `"                \"url\": \"https://example.org/report\","` | — |
| [SRC-62DC597310-L000059](../../tests/test_live_search_connectors.py#L59) | 59 | `"                \"content\": \"A source excerpt from the search response.\","` | — |
| [SRC-62DC597310-L000060](../../tests/test_live_search_connectors.py#L60) | 60 | `"                \"published_date\": \"2026-10-11\","` | — |
| [SRC-62DC597310-L000061](../../tests/test_live_search_connectors.py#L61) | 61 | `"            }]"` | — |
| [SRC-62DC597310-L000062](../../tests/test_live_search_connectors.py#L62) | 62 | `"        })"` | — |
| [SRC-62DC597310-L000063](../../tests/test_live_search_connectors.py#L63) | 63 | `""` | — |
| [SRC-62DC597310-L000064](../../tests/test_live_search_connectors.py#L64) | 64 | `"    monkeypatch.setattr(httpx, \"post\", fake_post)"` | — |
| [SRC-62DC597310-L000065](../../tests/test_live_search_connectors.py#L65) | 65 | `"    rows = WebAgent()._search_tavily(\"official sources report\")"` | — |
| [SRC-62DC597310-L000066](../../tests/test_live_search_connectors.py#L66) | 66 | `"    assert requested[\"url\"] == \"https://api.tavily.com/search\""` | — |
| [SRC-62DC597310-L000067](../../tests/test_live_search_connectors.py#L67) | 67 | `"    assert requested[\"json\"][\"api_key\"] == \"unit-test-tavily-secret\""` | — |
| [SRC-62DC597310-L000068](../../tests/test_live_search_connectors.py#L68) | 68 | `"    assert requested[\"json\"][\"include_answer\"] is False"` | — |
| [SRC-62DC597310-L000069](../../tests/test_live_search_connectors.py#L69) | 69 | `"    assert rows[0][\"provider\"] == \"tavily_search_api\""` | — |
| [SRC-62DC597310-L000070](../../tests/test_live_search_connectors.py#L70) | 70 | `"    assert rows[0][\"snippet\"].startswith(\"A source excerpt\")"` | — |
| [SRC-62DC597310-L000071](../../tests/test_live_search_connectors.py#L71) | 71 | `"    assert \"unit-test-tavily-secret\" not in str(rows)"` | — |
| [SRC-62DC597310-L000072](../../tests/test_live_search_connectors.py#L72) | 72 | `""` | — |
| [SRC-62DC597310-L000073](../../tests/test_live_search_connectors.py#L73) | 73 | `""` | — |
| [SRC-62DC597310-L000074](../../tests/test_live_search_connectors.py#L74) | 74 | `"def test_search_api_setup_status_reports_only_presence_not_secret_values(monkeypatch):"` | — |
| [SRC-62DC597310-L000075](../../tests/test_live_search_connectors.py#L75) | 75 | `"    monkeypatch.setenv(\"BRAVE_SEARCH_API_KEY\", \"brave-secret\")"` | — |
| [SRC-62DC597310-L000076](../../tests/test_live_search_connectors.py#L76) | 76 | `"    monkeypatch.setenv(\"TAVILY_API_KEY\", \"tavily-secret\")"` | — |
| [SRC-62DC597310-L000077](../../tests/test_live_search_connectors.py#L77) | 77 | `"    status = WebAgent.status()"` | — |
| [SRC-62DC597310-L000078](../../tests/test_live_search_connectors.py#L78) | 78 | `"    assert status[\"brave_search_api_configured\"] is True"` | — |
| [SRC-62DC597310-L000079](../../tests/test_live_search_connectors.py#L79) | 79 | `"    assert status[\"tavily_search_api_configured\"] is True"` | — |
| [SRC-62DC597310-L000080](../../tests/test_live_search_connectors.py#L80) | 80 | `"    assert \"brave-secret\" not in str(status)"` | — |
| [SRC-62DC597310-L000081](../../tests/test_live_search_connectors.py#L81) | 81 | `"    assert \"tavily-secret\" not in str(status)"` | — |
## اختبارات

### FILE-44CDA52D01 — [tests/test_omarai.py](../../tests/test_omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-44CDA52D01-L000001](../../tests/test_omarai.py#L1) | 1 | `"import csv"` | — |
| [SRC-44CDA52D01-L000002](../../tests/test_omarai.py#L2) | 2 | `""` | — |
| [SRC-44CDA52D01-L000003](../../tests/test_omarai.py#L3) | 3 | `"import pytest"` | — |
| [SRC-44CDA52D01-L000004](../../tests/test_omarai.py#L4) | 4 | `""` | — |
| [SRC-44CDA52D01-L000005](../../tests/test_omarai.py#L5) | 5 | `"from agents.omarai import LeadStore, analyze, normalize"` | — |
| [SRC-44CDA52D01-L000006](../../tests/test_omarai.py#L6) | 6 | `""` | — |
| [SRC-44CDA52D01-L000007](../../tests/test_omarai.py#L7) | 7 | `""` | — |
| [SRC-44CDA52D01-L000008](../../tests/test_omarai.py#L8) | 8 | `"def test_arabic_normalization():"` | — |
| [SRC-44CDA52D01-L000009](../../tests/test_omarai.py#L9) | 9 | `"    assert normalize(\"إيجارٌ ـ شقة\") == normalize(\"ايجار شقة\")"` | — |
| [SRC-44CDA52D01-L000010](../../tests/test_omarai.py#L10) | 10 | `""` | — |
| [SRC-44CDA52D01-L000011](../../tests/test_omarai.py#L11) | 11 | `"def test_high_intent_with_next_step():"` | — |
| [SRC-44CDA52D01-L000012](../../tests/test_omarai.py#L12) | 12 | `"    result=analyze(\"بدور على شقة وممكن معاينة\")"` | — |
| [SRC-44CDA52D01-L000013](../../tests/test_omarai.py#L13) | 13 | `"    assert result[\"label\"]==\"high_intent\""` | — |
| [SRC-44CDA52D01-L000014](../../tests/test_omarai.py#L14) | 14 | `"    assert result[\"score\"]>=55"` | — |
| [SRC-44CDA52D01-L000015](../../tests/test_omarai.py#L15) | 15 | `""` | — |
| [SRC-44CDA52D01-L000016](../../tests/test_omarai.py#L16) | 16 | `"def test_non_buyer_override():"` | — |
| [SRC-44CDA52D01-L000017](../../tests/test_omarai.py#L17) | 17 | `"    result=analyze(\"مش عايز اشتري، عايز ابيع شقة\")"` | — |
| [SRC-44CDA52D01-L000018](../../tests/test_omarai.py#L18) | 18 | `"    assert result[\"label\"]==\"not_buyer_signal\""` | — |
| [SRC-44CDA52D01-L000019](../../tests/test_omarai.py#L19) | 19 | `"    assert result[\"score\"]==0"` | — |
| [SRC-44CDA52D01-L000020](../../tests/test_omarai.py#L20) | 20 | `""` | — |
| [SRC-44CDA52D01-L000021](../../tests/test_omarai.py#L21) | 21 | `"def test_empty_text_rejected():"` | — |
| [SRC-44CDA52D01-L000022](../../tests/test_omarai.py#L22) | 22 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000023](../../tests/test_omarai.py#L23) | 23 | `"        analyze(\" \")"` | — |
| [SRC-44CDA52D01-L000024](../../tests/test_omarai.py#L24) | 24 | `""` | — |
| [SRC-44CDA52D01-L000025](../../tests/test_omarai.py#L25) | 25 | `"def test_url_required_and_validated(tmp_path):"` | — |
| [SRC-44CDA52D01-L000026](../../tests/test_omarai.py#L26) | 26 | `"    store=LeadStore(tmp_path/\"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000027](../../tests/test_omarai.py#L27) | 27 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000028](../../tests/test_omarai.py#L28) | 28 | `"        store.add(\"بدور على شقة\",\"\",\"manual\")"` | — |
| [SRC-44CDA52D01-L000029](../../tests/test_omarai.py#L29) | 29 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000030](../../tests/test_omarai.py#L30) | 30 | `"        store.add(\"بدور على شقة\",\"file:///tmp/private\",\"manual\")"` | — |
| [SRC-44CDA52D01-L000031](../../tests/test_omarai.py#L31) | 31 | `""` | — |
| [SRC-44CDA52D01-L000032](../../tests/test_omarai.py#L32) | 32 | `"def test_duplicate_is_idempotent(tmp_path):"` | — |
| [SRC-44CDA52D01-L000033](../../tests/test_omarai.py#L33) | 33 | `"    store=LeadStore(tmp_path/\"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000034](../../tests/test_omarai.py#L34) | 34 | `"    one,created1=store.add(\"بدور على شقة\",\"https://example.com/post/1\",\"facebook\")"` | — |
| [SRC-44CDA52D01-L000035](../../tests/test_omarai.py#L35) | 35 | `"    two,created2=store.add(\"بدور على شقة\",\"https://example.com/post/1\",\"facebook\")"` | — |
| [SRC-44CDA52D01-L000036](../../tests/test_omarai.py#L36) | 36 | `"    assert created1 is True and created2 is False"` | — |
| [SRC-44CDA52D01-L000037](../../tests/test_omarai.py#L37) | 37 | `"    assert one[\"id\"]==two[\"id\"]"` | — |
| [SRC-44CDA52D01-L000038](../../tests/test_omarai.py#L38) | 38 | `"    assert len(store.list())==1"` | — |
| [SRC-44CDA52D01-L000039](../../tests/test_omarai.py#L39) | 39 | `""` | — |
| [SRC-44CDA52D01-L000040](../../tests/test_omarai.py#L40) | 40 | `"def test_status_updates_are_explicit(tmp_path):"` | — |
| [SRC-44CDA52D01-L000041](../../tests/test_omarai.py#L41) | 41 | `"    store=LeadStore(tmp_path/\"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000042](../../tests/test_omarai.py#L42) | 42 | `"    lead,_=store.add(\"بدور على شقة\",\"https://example.com/p\",\"manual\")"` | — |
| [SRC-44CDA52D01-L000043](../../tests/test_omarai.py#L43) | 43 | `"    updated=store.update_status(lead[\"id\"],\"qualified\")"` | — |
| [SRC-44CDA52D01-L000044](../../tests/test_omarai.py#L44) | 44 | `"    assert updated[\"status\"]==\"qualified\""` | — |
| [SRC-44CDA52D01-L000045](../../tests/test_omarai.py#L45) | 45 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000046](../../tests/test_omarai.py#L46) | 46 | `"        store.update_status(lead[\"id\"],\"magic\")"` | — |
| [SRC-44CDA52D01-L000047](../../tests/test_omarai.py#L47) | 47 | `""` | — |
| [SRC-44CDA52D01-L000048](../../tests/test_omarai.py#L48) | 48 | `"def test_csv_requires_columns(tmp_path):"` | — |
| [SRC-44CDA52D01-L000049](../../tests/test_omarai.py#L49) | 49 | `"    bad=tmp_path/\"bad.csv\""` | — |
| [SRC-44CDA52D01-L000050](../../tests/test_omarai.py#L50) | 50 | `"    bad.write_text(\"foo,bar\\na,b\\n\",encoding=\"utf-8\")"` | — |
| [SRC-44CDA52D01-L000051](../../tests/test_omarai.py#L51) | 51 | `"    store=LeadStore(tmp_path/\"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000052](../../tests/test_omarai.py#L52) | 52 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000053](../../tests/test_omarai.py#L53) | 53 | `"        store.import_csv(bad)"` | — |
| [SRC-44CDA52D01-L000054](../../tests/test_omarai.py#L54) | 54 | `""` | — |
| [SRC-44CDA52D01-L000055](../../tests/test_omarai.py#L55) | 55 | `"def test_csv_export_neutralizes_spreadsheet_formula_injection(tmp_path):"` | — |
| [SRC-44CDA52D01-L000056](../../tests/test_omarai.py#L56) | 56 | `"    store = LeadStore(tmp_path / \"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000057](../../tests/test_omarai.py#L57) | 57 | `"    store.add("` | — |
| [SRC-44CDA52D01-L000058](../../tests/test_omarai.py#L58) | 58 | `"        '=HYPERLINK(\"https://evil.example\",\"click\")',"` | — |
| [SRC-44CDA52D01-L000059](../../tests/test_omarai.py#L59) | 59 | `"        \"https://example.com/post/1\","` | — |
| [SRC-44CDA52D01-L000060](../../tests/test_omarai.py#L60) | 60 | `"        platform=\"manual\","` | — |
| [SRC-44CDA52D01-L000061](../../tests/test_omarai.py#L61) | 61 | `"        note=\"  +SUM(1,1)\","` | — |
| [SRC-44CDA52D01-L000062](../../tests/test_omarai.py#L62) | 62 | `"    )"` | — |
| [SRC-44CDA52D01-L000063](../../tests/test_omarai.py#L63) | 63 | `"    store.add("` | — |
| [SRC-44CDA52D01-L000064](../../tests/test_omarai.py#L64) | 64 | `"        \"\\u00a0\\ufeff=1+1\","` | — |
| [SRC-44CDA52D01-L000065](../../tests/test_omarai.py#L65) | 65 | `"        \"https://example.com/post/2\","` | — |
| [SRC-44CDA52D01-L000066](../../tests/test_omarai.py#L66) | 66 | `"        platform=\"manual\","` | — |
| [SRC-44CDA52D01-L000067](../../tests/test_omarai.py#L67) | 67 | `"        note=\"\\u00a0\\ufeff=SUM(1,1)\","` | — |
| [SRC-44CDA52D01-L000068](../../tests/test_omarai.py#L68) | 68 | `"    )"` | — |
| [SRC-44CDA52D01-L000069](../../tests/test_omarai.py#L69) | 69 | `"    destination = tmp_path / \"export.csv\""` | — |
| [SRC-44CDA52D01-L000070](../../tests/test_omarai.py#L70) | 70 | `"    assert store.export_csv(destination) == 2"` | — |
| [SRC-44CDA52D01-L000071](../../tests/test_omarai.py#L71) | 71 | `"    raw_csv = destination.read_text(encoding=\"utf-8-sig\")"` | — |
| [SRC-44CDA52D01-L000072](../../tests/test_omarai.py#L72) | 72 | `"    assert '\"\\t=HYPERLINK(' in raw_csv"` | — |
| [SRC-44CDA52D01-L000073](../../tests/test_omarai.py#L73) | 73 | `"    assert '\"\\t  +SUM' in raw_csv"` | — |
| [SRC-44CDA52D01-L000074](../../tests/test_omarai.py#L74) | 74 | `""` | — |
| [SRC-44CDA52D01-L000075](../../tests/test_omarai.py#L75) | 75 | `"    with destination.open(newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-44CDA52D01-L000076](../../tests/test_omarai.py#L76) | 76 | `"        rows = list(csv.DictReader(stream))"` | — |
| [SRC-44CDA52D01-L000077](../../tests/test_omarai.py#L77) | 77 | `""` | — |
| [SRC-44CDA52D01-L000078](../../tests/test_omarai.py#L78) | 78 | `"    row1 = next(row for row in rows if row[\"source_url\"] == \"https://example.com/post/1\")"` | — |
| [SRC-44CDA52D01-L000079](../../tests/test_omarai.py#L79) | 79 | `"    row2 = next(row for row in rows if row[\"source_url\"] == \"https://example.com/post/2\")"` | — |
| [SRC-44CDA52D01-L000080](../../tests/test_omarai.py#L80) | 80 | `"    assert row1[\"text\"].startswith(\"\\t=\")"` | — |
| [SRC-44CDA52D01-L000081](../../tests/test_omarai.py#L81) | 81 | `"    assert row1[\"note\"].startswith(\"\\t  +\")"` | — |
| [SRC-44CDA52D01-L000082](../../tests/test_omarai.py#L82) | 82 | `"    assert row2[\"text\"].startswith(\"\\t\\ufeff=\")"` | — |
| [SRC-44CDA52D01-L000083](../../tests/test_omarai.py#L83) | 83 | `"    assert row2[\"note\"].startswith(\"\\t\\u00a0\\ufeff=\")"` | — |
| [SRC-44CDA52D01-L000084](../../tests/test_omarai.py#L84) | 84 | `""` | — |
## اختبارات

### FILE-B106ADC5EF — [tests/test_proxy_origin.py](../../tests/test_proxy_origin.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-B106ADC5EF-L000001](../../tests/test_proxy_origin.py#L1) | 1 | `"\"\"\"Regression tests for the proxy-aware Origin check. OMARAI-PROXY-ORIGIN-PATCH\"\"\""` | — |
| [SRC-B106ADC5EF-L000002](../../tests/test_proxy_origin.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-B106ADC5EF-L000003](../../tests/test_proxy_origin.py#L3) | 3 | `"import http.client"` | — |
| [SRC-B106ADC5EF-L000004](../../tests/test_proxy_origin.py#L4) | 4 | `"import threading"` | — |
| [SRC-B106ADC5EF-L000005](../../tests/test_proxy_origin.py#L5) | 5 | `"from http.server import ThreadingHTTPServer"` | — |
| [SRC-B106ADC5EF-L000006](../../tests/test_proxy_origin.py#L6) | 6 | `"import pytest"` | — |
| [SRC-B106ADC5EF-L000007](../../tests/test_proxy_origin.py#L7) | 7 | `"from agents.omarai import LeadStore"` | — |
| [SRC-B106ADC5EF-L000008](../../tests/test_proxy_origin.py#L8) | 8 | `"from api.omarai import Handler"` | — |
| [SRC-B106ADC5EF-L000009](../../tests/test_proxy_origin.py#L9) | 9 | `""` | — |
| [SRC-B106ADC5EF-L000010](../../tests/test_proxy_origin.py#L10) | 10 | `"TOKEN = \"t\" * 40"` | — |
| [SRC-B106ADC5EF-L000011](../../tests/test_proxy_origin.py#L11) | 11 | `"PUBLIC_NAME = \"app-1234.hosting.example\""` | — |
| [SRC-B106ADC5EF-L000012](../../tests/test_proxy_origin.py#L12) | 12 | `""` | — |
| [SRC-B106ADC5EF-L000013](../../tests/test_proxy_origin.py#L13) | 13 | `"@pytest.fixture"` | — |
| [SRC-B106ADC5EF-L000014](../../tests/test_proxy_origin.py#L14) | 14 | `"def port(tmp_path, monkeypatch):"` | — |
| [SRC-B106ADC5EF-L000015](../../tests/test_proxy_origin.py#L15) | 15 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-B106ADC5EF-L000016](../../tests/test_proxy_origin.py#L16) | 16 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", TOKEN)"` | — |
| [SRC-B106ADC5EF-L000017](../../tests/test_proxy_origin.py#L17) | 17 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-B106ADC5EF-L000018](../../tests/test_proxy_origin.py#L18) | 18 | `"    monkeypatch.setattr(Handler, \"store\", LeadStore(tmp_path / \"origin-test.sqlite3\"))"` | — |
| [SRC-B106ADC5EF-L000019](../../tests/test_proxy_origin.py#L19) | 19 | `"    monkeypatch.setattr(Handler, \"RATE_LIMIT_REQUESTS\", 10_000)"` | — |
| [SRC-B106ADC5EF-L000020](../../tests/test_proxy_origin.py#L20) | 20 | `"    server = ThreadingHTTPServer((\"127.0.0.1\", 0), Handler)"` | — |
| [SRC-B106ADC5EF-L000021](../../tests/test_proxy_origin.py#L21) | 21 | `"    thread = threading.Thread(target=server.serve_forever, daemon=True)"` | — |
| [SRC-B106ADC5EF-L000022](../../tests/test_proxy_origin.py#L22) | 22 | `"    thread.start()"` | — |
| [SRC-B106ADC5EF-L000023](../../tests/test_proxy_origin.py#L23) | 23 | `"    try:"` | — |
| [SRC-B106ADC5EF-L000024](../../tests/test_proxy_origin.py#L24) | 24 | `"        yield server.server_port"` | — |
| [SRC-B106ADC5EF-L000025](../../tests/test_proxy_origin.py#L25) | 25 | `"    finally:"` | — |
| [SRC-B106ADC5EF-L000026](../../tests/test_proxy_origin.py#L26) | 26 | `"        server.shutdown()"` | — |
| [SRC-B106ADC5EF-L000027](../../tests/test_proxy_origin.py#L27) | 27 | `"        server.server_close()"` | — |
| [SRC-B106ADC5EF-L000028](../../tests/test_proxy_origin.py#L28) | 28 | `"        thread.join(timeout=3)"` | — |
| [SRC-B106ADC5EF-L000029](../../tests/test_proxy_origin.py#L29) | 29 | `""` | — |
| [SRC-B106ADC5EF-L000030](../../tests/test_proxy_origin.py#L30) | 30 | `"def call(port, method, extra):"` | — |
| [SRC-B106ADC5EF-L000031](../../tests/test_proxy_origin.py#L31) | 31 | `"    body = b'{\"question\": \"x\"}' if method == \"POST\" else b\"\""` | — |
| [SRC-B106ADC5EF-L000032](../../tests/test_proxy_origin.py#L32) | 32 | `"    headers = {\"Content-Type\": \"application/json\", \"Authorization\": \"Bearer \" + TOKEN, **extra}"` | — |
| [SRC-B106ADC5EF-L000033](../../tests/test_proxy_origin.py#L33) | 33 | `"    connection = http.client.HTTPConnection(\"127.0.0.1\", port, timeout=5)"` | — |
| [SRC-B106ADC5EF-L000034](../../tests/test_proxy_origin.py#L34) | 34 | `"    connection.putrequest(method, \"/api/ask\", skip_host=True)"` | — |
| [SRC-B106ADC5EF-L000035](../../tests/test_proxy_origin.py#L35) | 35 | `"    for name, value in headers.items():"` | — |
| [SRC-B106ADC5EF-L000036](../../tests/test_proxy_origin.py#L36) | 36 | `"        connection.putheader(name, value)"` | — |
| [SRC-B106ADC5EF-L000037](../../tests/test_proxy_origin.py#L37) | 37 | `"    connection.putheader(\"Content-Length\", str(len(body)))"` | — |
| [SRC-B106ADC5EF-L000038](../../tests/test_proxy_origin.py#L38) | 38 | `"    connection.endheaders()"` | — |
| [SRC-B106ADC5EF-L000039](../../tests/test_proxy_origin.py#L39) | 39 | `"    if body:"` | — |
| [SRC-B106ADC5EF-L000040](../../tests/test_proxy_origin.py#L40) | 40 | `"        connection.send(body)"` | — |
| [SRC-B106ADC5EF-L000041](../../tests/test_proxy_origin.py#L41) | 41 | `"    response = connection.getresponse()"` | — |
| [SRC-B106ADC5EF-L000042](../../tests/test_proxy_origin.py#L42) | 42 | `"    response.read()"` | — |
| [SRC-B106ADC5EF-L000043](../../tests/test_proxy_origin.py#L43) | 43 | `"    connection.close()"` | — |
| [SRC-B106ADC5EF-L000044](../../tests/test_proxy_origin.py#L44) | 44 | `"    return response.status"` | — |
| [SRC-B106ADC5EF-L000045](../../tests/test_proxy_origin.py#L45) | 45 | `""` | — |
| [SRC-B106ADC5EF-L000046](../../tests/test_proxy_origin.py#L46) | 46 | `"ALLOWED_SHAPES = {"` | — |
| [SRC-B106ADC5EF-L000047](../../tests/test_proxy_origin.py#L47) | 47 | `"    \"proxy keeps Host, forwards https\": {\"Host\": PUBLIC_NAME, \"X-Forwarded-Proto\": \"https\"},"` | — |
| [SRC-B106ADC5EF-L000048](../../tests/test_proxy_origin.py#L48) | 48 | `"    \"proxy keeps Host, sends no proto header\": {\"Host\": PUBLIC_NAME},"` | — |
| [SRC-B106ADC5EF-L000049](../../tests/test_proxy_origin.py#L49) | 49 | `"    \"proxy forwards plain http\": {\"Host\": PUBLIC_NAME, \"X-Forwarded-Proto\": \"http\"},"` | — |
| [SRC-B106ADC5EF-L000050](../../tests/test_proxy_origin.py#L50) | 50 | `"    \"proxy rewrites Host, public name in X-Forwarded-Host\": {"` | — |
| [SRC-B106ADC5EF-L000051](../../tests/test_proxy_origin.py#L51) | 51 | `"        \"Host\": \"127.0.0.1:8000\", \"X-Forwarded-Host\": PUBLIC_NAME, \"X-Forwarded-Proto\": \"http\"},"` | — |
| [SRC-B106ADC5EF-L000052](../../tests/test_proxy_origin.py#L52) | 52 | `"}"` | — |
| [SRC-B106ADC5EF-L000053](../../tests/test_proxy_origin.py#L53) | 53 | `""` | — |
| [SRC-B106ADC5EF-L000054](../../tests/test_proxy_origin.py#L54) | 54 | `"@pytest.mark.parametrize(\"shape\", ALLOWED_SHAPES)"` | — |
| [SRC-B106ADC5EF-L000055](../../tests/test_proxy_origin.py#L55) | 55 | `"def test_own_origin_is_accepted_behind_a_proxy(port, shape):"` | — |
| [SRC-B106ADC5EF-L000056](../../tests/test_proxy_origin.py#L56) | 56 | `"    headers = {**ALLOWED_SHAPES[shape], \"Origin\": \"https://\" + PUBLIC_NAME}"` | — |
| [SRC-B106ADC5EF-L000057](../../tests/test_proxy_origin.py#L57) | 57 | `"    assert call(port, \"POST\", headers) == 200"` | — |
| [SRC-B106ADC5EF-L000058](../../tests/test_proxy_origin.py#L58) | 58 | `"    assert call(port, \"OPTIONS\", {k: v for k, v in headers.items() if k != \"Authorization\"}) == 204"` | — |
| [SRC-B106ADC5EF-L000059](../../tests/test_proxy_origin.py#L59) | 59 | `""` | — |
| [SRC-B106ADC5EF-L000060](../../tests/test_proxy_origin.py#L60) | 60 | `"@pytest.mark.parametrize(\"shape\", ALLOWED_SHAPES)"` | — |
| [SRC-B106ADC5EF-L000061](../../tests/test_proxy_origin.py#L61) | 61 | `"def test_a_foreign_site_is_still_refused(port, shape):"` | — |
| [SRC-B106ADC5EF-L000062](../../tests/test_proxy_origin.py#L62) | 62 | `"    headers = {**ALLOWED_SHAPES[shape], \"Origin\": \"https://evil.example\"}"` | — |
| [SRC-B106ADC5EF-L000063](../../tests/test_proxy_origin.py#L63) | 63 | `"    assert call(port, \"POST\", headers) == 403"` | — |
| [SRC-B106ADC5EF-L000064](../../tests/test_proxy_origin.py#L64) | 64 | `"    assert call(port, \"OPTIONS\", headers) == 403"` | — |
| [SRC-B106ADC5EF-L000065](../../tests/test_proxy_origin.py#L65) | 65 | `""` | — |
| [SRC-B106ADC5EF-L000066](../../tests/test_proxy_origin.py#L66) | 66 | `"def test_configured_origin_still_works_without_any_proxy_headers(port, monkeypatch):"` | — |
| [SRC-B106ADC5EF-L000067](../../tests/test_proxy_origin.py#L67) | 67 | `"    monkeypatch.setenv(\"OMARAI_ALLOWED_ORIGINS\", \"https://frontend.example\")"` | — |
| [SRC-B106ADC5EF-L000068](../../tests/test_proxy_origin.py#L68) | 68 | `"    headers = {\"Host\": \"127.0.0.1:8000\", \"Origin\": \"https://frontend.example\"}"` | — |
| [SRC-B106ADC5EF-L000069](../../tests/test_proxy_origin.py#L69) | 69 | `"    assert call(port, \"POST\", headers) == 200"` | — |
## اختبارات

### FILE-C353AAAC10 — [tests/test_request_budget.py](../../tests/test_request_budget.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C353AAAC10-L000001](../../tests/test_request_budget.py#L1) | 1 | `"\"\"\"Unit tests for Omarai's per-request resource budget.\"\"\""` | — |
| [SRC-C353AAAC10-L000002](../../tests/test_request_budget.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-C353AAAC10-L000003](../../tests/test_request_budget.py#L3) | 3 | `""` | — |
| [SRC-C353AAAC10-L000004](../../tests/test_request_budget.py#L4) | 4 | `"import pytest"` | — |
| [SRC-C353AAAC10-L000005](../../tests/test_request_budget.py#L5) | 5 | `""` | — |
| [SRC-C353AAAC10-L000006](../../tests/test_request_budget.py#L6) | 6 | `"from agents.request_budget import RequestBudget, RequestBudgetExceeded"` | — |
| [SRC-C353AAAC10-L000007](../../tests/test_request_budget.py#L7) | 7 | `""` | — |
| [SRC-C353AAAC10-L000008](../../tests/test_request_budget.py#L8) | 8 | `""` | — |
| [SRC-C353AAAC10-L000009](../../tests/test_request_budget.py#L9) | 9 | `"class FakeClock:"` | — |
| [SRC-C353AAAC10-L000010](../../tests/test_request_budget.py#L10) | 10 | `"    def __init__(self, value: float = 100.0) -> None:"` | — |
| [SRC-C353AAAC10-L000011](../../tests/test_request_budget.py#L11) | 11 | `"        self.value = value"` | — |
| [SRC-C353AAAC10-L000012](../../tests/test_request_budget.py#L12) | 12 | `""` | — |
| [SRC-C353AAAC10-L000013](../../tests/test_request_budget.py#L13) | 13 | `"    def __call__(self) -> float:"` | — |
| [SRC-C353AAAC10-L000014](../../tests/test_request_budget.py#L14) | 14 | `"        return self.value"` | — |
| [SRC-C353AAAC10-L000015](../../tests/test_request_budget.py#L15) | 15 | `""` | — |
| [SRC-C353AAAC10-L000016](../../tests/test_request_budget.py#L16) | 16 | `""` | — |
| [SRC-C353AAAC10-L000017](../../tests/test_request_budget.py#L17) | 17 | `"def test_resource_reservations_are_bounded_and_thread_safe_in_snapshot():"` | — |
| [SRC-C353AAAC10-L000018](../../tests/test_request_budget.py#L18) | 18 | `"    clock = FakeClock()"` | — |
| [SRC-C353AAAC10-L000019](../../tests/test_request_budget.py#L19) | 19 | `"    budget = RequestBudget("` | — |
| [SRC-C353AAAC10-L000020](../../tests/test_request_budget.py#L20) | 20 | `"        timeout_seconds=10,"` | — |
| [SRC-C353AAAC10-L000021](../../tests/test_request_budget.py#L21) | 21 | `"        limits={\"search_calls\": 1},"` | — |
| [SRC-C353AAAC10-L000022](../../tests/test_request_budget.py#L22) | 22 | `"        clock=clock,"` | — |
| [SRC-C353AAAC10-L000023](../../tests/test_request_budget.py#L23) | 23 | `"    )"` | — |
| [SRC-C353AAAC10-L000024](../../tests/test_request_budget.py#L24) | 24 | `""` | — |
| [SRC-C353AAAC10-L000025](../../tests/test_request_budget.py#L25) | 25 | `"    budget.reserve(\"search_calls\")"` | — |
| [SRC-C353AAAC10-L000026](../../tests/test_request_budget.py#L26) | 26 | `"    with pytest.raises(RequestBudgetExceeded, match=\"search_calls\"):"` | — |
| [SRC-C353AAAC10-L000027](../../tests/test_request_budget.py#L27) | 27 | `"        budget.reserve(\"search_calls\")"` | — |
| [SRC-C353AAAC10-L000028](../../tests/test_request_budget.py#L28) | 28 | `""` | — |
| [SRC-C353AAAC10-L000029](../../tests/test_request_budget.py#L29) | 29 | `"    snapshot = budget.snapshot()"` | — |
| [SRC-C353AAAC10-L000030](../../tests/test_request_budget.py#L30) | 30 | `"    assert snapshot[\"counts\"][\"search_calls\"] == 1"` | — |
| [SRC-C353AAAC10-L000031](../../tests/test_request_budget.py#L31) | 31 | `"    assert snapshot[\"limits\"][\"search_calls\"] == 1"` | — |
| [SRC-C353AAAC10-L000032](../../tests/test_request_budget.py#L32) | 32 | `"    assert snapshot[\"deadline_exceeded\"] is False"` | — |
| [SRC-C353AAAC10-L000033](../../tests/test_request_budget.py#L33) | 33 | `""` | — |
| [SRC-C353AAAC10-L000034](../../tests/test_request_budget.py#L34) | 34 | `""` | — |
| [SRC-C353AAAC10-L000035](../../tests/test_request_budget.py#L35) | 35 | `"def test_deadline_blocks_new_work_and_caps_outbound_timeout():"` | — |
| [SRC-C353AAAC10-L000036](../../tests/test_request_budget.py#L36) | 36 | `"    clock = FakeClock()"` | — |
| [SRC-C353AAAC10-L000037](../../tests/test_request_budget.py#L37) | 37 | `"    budget = RequestBudget(timeout_seconds=10, clock=clock)"` | — |
| [SRC-C353AAAC10-L000038](../../tests/test_request_budget.py#L38) | 38 | `""` | — |
| [SRC-C353AAAC10-L000039](../../tests/test_request_budget.py#L39) | 39 | `"    clock.value += 7"` | — |
| [SRC-C353AAAC10-L000040](../../tests/test_request_budget.py#L40) | 40 | `"    assert budget.timeout_for(30) == pytest.approx(3)"` | — |
| [SRC-C353AAAC10-L000041](../../tests/test_request_budget.py#L41) | 41 | `"    assert budget.timeout_for(1) == pytest.approx(1)"` | — |
| [SRC-C353AAAC10-L000042](../../tests/test_request_budget.py#L42) | 42 | `""` | — |
| [SRC-C353AAAC10-L000043](../../tests/test_request_budget.py#L43) | 43 | `"    clock.value += 4"` | — |
| [SRC-C353AAAC10-L000044](../../tests/test_request_budget.py#L44) | 44 | `"    assert budget.remaining_seconds() == 0"` | — |
| [SRC-C353AAAC10-L000045](../../tests/test_request_budget.py#L45) | 45 | `"    with pytest.raises(RequestBudgetExceeded, match=\"وقت الطلب\"):"` | — |
| [SRC-C353AAAC10-L000046](../../tests/test_request_budget.py#L46) | 46 | `"        budget.reserve(\"model_calls\")"` | — |
| [SRC-C353AAAC10-L000047](../../tests/test_request_budget.py#L47) | 47 | `"    with pytest.raises(RequestBudgetExceeded, match=\"وقت الطلب\"):"` | — |
| [SRC-C353AAAC10-L000048](../../tests/test_request_budget.py#L48) | 48 | `"        budget.timeout_for(3)"` | — |
| [SRC-C353AAAC10-L000049](../../tests/test_request_budget.py#L49) | 49 | `""` | — |
| [SRC-C353AAAC10-L000050](../../tests/test_request_budget.py#L50) | 50 | `""` | — |
| [SRC-C353AAAC10-L000051](../../tests/test_request_budget.py#L51) | 51 | `"def test_environment_overrides_are_clamped(monkeypatch):"` | — |
| [SRC-C353AAAC10-L000052](../../tests/test_request_budget.py#L52) | 52 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_BUDGET_SECONDS\", \"999\")"` | — |
| [SRC-C353AAAC10-L000053](../../tests/test_request_budget.py#L53) | 53 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_SEARCH_CALLS\", \"999\")"` | — |
| [SRC-C353AAAC10-L000054](../../tests/test_request_budget.py#L54) | 54 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_MODEL_CALLS\", \"-1\")"` | — |
| [SRC-C353AAAC10-L000055](../../tests/test_request_budget.py#L55) | 55 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_TOOL_CALLS\", \"-1\")"` | — |
| [SRC-C353AAAC10-L000056](../../tests/test_request_budget.py#L56) | 56 | `""` | — |
| [SRC-C353AAAC10-L000057](../../tests/test_request_budget.py#L57) | 57 | `"    snapshot = RequestBudget.from_environment().snapshot()"` | — |
| [SRC-C353AAAC10-L000058](../../tests/test_request_budget.py#L58) | 58 | `""` | — |
| [SRC-C353AAAC10-L000059](../../tests/test_request_budget.py#L59) | 59 | `"    assert snapshot[\"timeout_seconds\"] == 120"` | — |
| [SRC-C353AAAC10-L000060](../../tests/test_request_budget.py#L60) | 60 | `"    assert snapshot[\"limits\"][\"search_calls\"] == 40"` | — |
| [SRC-C353AAAC10-L000061](../../tests/test_request_budget.py#L61) | 61 | `"    assert snapshot[\"limits\"][\"model_calls\"] == 1"` | — |
| [SRC-C353AAAC10-L000062](../../tests/test_request_budget.py#L62) | 62 | `"    assert snapshot[\"limits\"][\"tool_calls\"] == 0"` | — |
| [SRC-C353AAAC10-L000063](../../tests/test_request_budget.py#L63) | 63 | `""` | — |
| [SRC-C353AAAC10-L000064](../../tests/test_request_budget.py#L64) | 64 | `""` | — |
| [SRC-C353AAAC10-L000065](../../tests/test_request_budget.py#L65) | 65 | `"def test_web_agent_reserves_search_model_and_page_work_before_io(monkeypatch):"` | — |
| [SRC-C353AAAC10-L000066](../../tests/test_request_budget.py#L66) | 66 | `"    from agents.web_agent import WebAgent"` | — |
| [SRC-C353AAAC10-L000067](../../tests/test_request_budget.py#L67) | 67 | `""` | — |
| [SRC-C353AAAC10-L000068](../../tests/test_request_budget.py#L68) | 68 | `"    agent = WebAgent()"` | — |
| [SRC-C353AAAC10-L000069](../../tests/test_request_budget.py#L69) | 69 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-C353AAAC10-L000070](../../tests/test_request_budget.py#L70) | 70 | `""` | — |
| [SRC-C353AAAC10-L000071](../../tests/test_request_budget.py#L71) | 71 | `"    agent._request_budget = RequestBudget(limits={\"search_queries\": 0})"` | — |
| [SRC-C353AAAC10-L000072](../../tests/test_request_budget.py#L72) | 72 | `"    with pytest.raises(RequestBudgetExceeded, match=\"search_queries\"):"` | — |
| [SRC-C353AAAC10-L000073](../../tests/test_request_budget.py#L73) | 73 | `"        agent._search_web(\"budget test\")"` | — |
| [SRC-C353AAAC10-L000074](../../tests/test_request_budget.py#L74) | 74 | `""` | — |
| [SRC-C353AAAC10-L000075](../../tests/test_request_budget.py#L75) | 75 | `"    agent._request_budget = RequestBudget(limits={\"model_calls\": 0})"` | — |
| [SRC-C353AAAC10-L000076](../../tests/test_request_budget.py#L76) | 76 | `"    monkeypatch.setattr("` | — |
| [SRC-C353AAAC10-L000077](../../tests/test_request_budget.py#L77) | 77 | `"        \"agents.web_agent.urllib.request.urlopen\","` | — |
| [SRC-C353AAAC10-L000078](../../tests/test_request_budget.py#L78) | 78 | `"        lambda *args, **kwargs: pytest.fail(\"model HTTP request must not start\"),"` | — |
| [SRC-C353AAAC10-L000079](../../tests/test_request_budget.py#L79) | 79 | `"    )"` | — |
| [SRC-C353AAAC10-L000080](../../tests/test_request_budget.py#L80) | 80 | `"    with pytest.raises(RequestBudgetExceeded, match=\"model_calls\"):"` | — |
| [SRC-C353AAAC10-L000081](../../tests/test_request_budget.py#L81) | 81 | `"        agent._request_completion([{\"role\": \"user\", \"content\": \"test\"}])"` | — |
| [SRC-C353AAAC10-L000082](../../tests/test_request_budget.py#L82) | 82 | `""` | — |
| [SRC-C353AAAC10-L000083](../../tests/test_request_budget.py#L83) | 83 | `"    agent._request_budget = RequestBudget(limits={\"page_fetches\": 0})"` | — |
| [SRC-C353AAAC10-L000084](../../tests/test_request_budget.py#L84) | 84 | `"    with pytest.raises(RequestBudgetExceeded, match=\"page_fetches\"):"` | — |
| [SRC-C353AAAC10-L000085](../../tests/test_request_budget.py#L85) | 85 | `"        agent._fetch_page(\"https://example.com/\")"` | — |
| [SRC-C353AAAC10-L000086](../../tests/test_request_budget.py#L86) | 86 | `""` | — |
| [SRC-C353AAAC10-L000087](../../tests/test_request_budget.py#L87) | 87 | `""` | — |
| [SRC-C353AAAC10-L000088](../../tests/test_request_budget.py#L88) | 88 | `"def test_social_provider_reserves_budget_before_network_io(monkeypatch):"` | — |
| [SRC-C353AAAC10-L000089](../../tests/test_request_budget.py#L89) | 89 | `"    from agents.web_agent import WebAgent"` | — |
| [SRC-C353AAAC10-L000090](../../tests/test_request_budget.py#L90) | 90 | `""` | — |
| [SRC-C353AAAC10-L000091](../../tests/test_request_budget.py#L91) | 91 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_ID\", \"test-client\")"` | — |
| [SRC-C353AAAC10-L000092](../../tests/test_request_budget.py#L92) | 92 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_SECRET\", \"test-secret\")"` | — |
| [SRC-C353AAAC10-L000093](../../tests/test_request_budget.py#L93) | 93 | `"    agent = WebAgent()"` | — |
| [SRC-C353AAAC10-L000094](../../tests/test_request_budget.py#L94) | 94 | `"    agent._request_budget = RequestBudget(limits={\"search_calls\": 0})"` | — |
| [SRC-C353AAAC10-L000095](../../tests/test_request_budget.py#L95) | 95 | `""` | — |
| [SRC-C353AAAC10-L000096](../../tests/test_request_budget.py#L96) | 96 | `"    monkeypatch.setattr("` | — |
| [SRC-C353AAAC10-L000097](../../tests/test_request_budget.py#L97) | 97 | `"        \"httpx.post\","` | — |
| [SRC-C353AAAC10-L000098](../../tests/test_request_budget.py#L98) | 98 | `"        lambda *args, **kwargs: pytest.fail(\"social HTTP request must not start\"),"` | — |
| [SRC-C353AAAC10-L000099](../../tests/test_request_budget.py#L99) | 99 | `"    )"` | — |
| [SRC-C353AAAC10-L000100](../../tests/test_request_budget.py#L100) | 100 | `"    with pytest.raises(RequestBudgetExceeded, match=\"search_calls\"):"` | — |
| [SRC-C353AAAC10-L000101](../../tests/test_request_budget.py#L101) | 101 | `"        agent._search_social(\"budget test\", [\"reddit\"])"` | — |
## اختبارات

### FILE-6BF96689A8 — [tests/test_research.py](../../tests/test_research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6BF96689A8-L000001](../../tests/test_research.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-6BF96689A8-L000002](../../tests/test_research.py#L2) | 2 | `""` | — |
| [SRC-6BF96689A8-L000003](../../tests/test_research.py#L3) | 3 | `"from agents.research import ("` | — |
| [SRC-6BF96689A8-L000004](../../tests/test_research.py#L4) | 4 | `"    evidence_signal_report,"` | — |
| [SRC-6BF96689A8-L000005](../../tests/test_research.py#L5) | 5 | `"    fallback_plan,"` | — |
| [SRC-6BF96689A8-L000006](../../tests/test_research.py#L6) | 6 | `"    fuse_ranked_results,"` | — |
| [SRC-6BF96689A8-L000007](../../tests/test_research.py#L7) | 7 | `"    registrable_domain,"` | — |
| [SRC-6BF96689A8-L000008](../../tests/test_research.py#L8) | 8 | `"    validate_plan,"` | — |
| [SRC-6BF96689A8-L000009](../../tests/test_research.py#L9) | 9 | `")"` | — |
| [SRC-6BF96689A8-L000010](../../tests/test_research.py#L10) | 10 | `""` | — |
| [SRC-6BF96689A8-L000011](../../tests/test_research.py#L11) | 11 | `""` | — |
| [SRC-6BF96689A8-L000012](../../tests/test_research.py#L12) | 12 | `"def test_social_question_gets_platform_targeted_queries():"` | — |
| [SRC-6BF96689A8-L000013](../../tests/test_research.py#L13) | 13 | `"    plan = fallback_plan(\"ابحث في Reddit عن تجارب العملاء مع السيارات الكهربائية\")"` | — |
| [SRC-6BF96689A8-L000014](../../tests/test_research.py#L14) | 14 | `"    assert plan[\"social_focus\"] is True"` | — |
| [SRC-6BF96689A8-L000015](../../tests/test_research.py#L15) | 15 | `"    assert \"reddit\" in plan[\"platforms\"]"` | — |
| [SRC-6BF96689A8-L000016](../../tests/test_research.py#L16) | 16 | `"    assert any(\"site:reddit.com\" in query for query in plan[\"queries\"])"` | — |
| [SRC-6BF96689A8-L000017](../../tests/test_research.py#L17) | 17 | `"    assert len(plan[\"queries\"]) <= 8"` | — |
| [SRC-6BF96689A8-L000018](../../tests/test_research.py#L18) | 18 | `""` | — |
| [SRC-6BF96689A8-L000019](../../tests/test_research.py#L19) | 19 | `""` | — |
| [SRC-6BF96689A8-L000020](../../tests/test_research.py#L20) | 20 | `"def test_follow_up_query_keeps_prior_topic():"` | — |
| [SRC-6BF96689A8-L000021](../../tests/test_research.py#L21) | 21 | `"    history = [{\"role\": \"user\", \"content\": \"قارن سوق السيارات الكهربائية في مصر\"}]"` | — |
| [SRC-6BF96689A8-L000022](../../tests/test_research.py#L22) | 22 | `"    plan = fallback_plan(\"وطب الأسعار الحالية؟\", history)"` | — |
| [SRC-6BF96689A8-L000023](../../tests/test_research.py#L23) | 23 | `"    assert \"السيارات الكهربائية\" in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000024](../../tests/test_research.py#L24) | 24 | `"    assert plan[\"freshness\"] == \"current\""` | — |
| [SRC-6BF96689A8-L000025](../../tests/test_research.py#L25) | 25 | `""` | — |
| [SRC-6BF96689A8-L000026](../../tests/test_research.py#L26) | 26 | `""` | — |
| [SRC-6BF96689A8-L000027](../../tests/test_research.py#L27) | 27 | `"def test_plan_validation_caps_queries_and_rejects_non_string_values():"` | — |
| [SRC-6BF96689A8-L000028](../../tests/test_research.py#L28) | 28 | `"    candidate = {"` | — |
| [SRC-6BF96689A8-L000029](../../tests/test_research.py#L29) | 29 | `"        \"queries\": [\"بحث أ\", \"بحث ب\", None, \"بحث ج\", \"بحث د\", \"بحث هـ\", \"بحث سادس\", \"بحث سابع\", \"بحث ثامن\", \"بحث تاسع\"],"` | — |
| [SRC-6BF96689A8-L000030](../../tests/test_research.py#L30) | 30 | `"        \"social_focus\": True,"` | — |
| [SRC-6BF96689A8-L000031](../../tests/test_research.py#L31) | 31 | `"        \"freshness\": \"current\","` | — |
| [SRC-6BF96689A8-L000032](../../tests/test_research.py#L32) | 32 | `"        \"depth\": \"deep\","` | — |
| [SRC-6BF96689A8-L000033](../../tests/test_research.py#L33) | 33 | `"        \"platforms\": [\"reddit\", \"unknown\"],"` | — |
| [SRC-6BF96689A8-L000034](../../tests/test_research.py#L34) | 34 | `"    }"` | — |
| [SRC-6BF96689A8-L000035](../../tests/test_research.py#L35) | 35 | `"    plan = validate_plan(candidate, \"بحث عن منشورات\")"` | — |
| [SRC-6BF96689A8-L000036](../../tests/test_research.py#L36) | 36 | `"    assert len(plan[\"queries\"]) <= 8"` | — |
| [SRC-6BF96689A8-L000037](../../tests/test_research.py#L37) | 37 | `"    assert \"unknown\" not in plan[\"platforms\"]"` | — |
| [SRC-6BF96689A8-L000038](../../tests/test_research.py#L38) | 38 | `"    assert plan[\"social_focus\"] is True"` | — |
| [SRC-6BF96689A8-L000039](../../tests/test_research.py#L39) | 39 | `"    assert plan[\"freshness\"] == \"current\""` | — |
| [SRC-6BF96689A8-L000040](../../tests/test_research.py#L40) | 40 | `""` | — |
| [SRC-6BF96689A8-L000041](../../tests/test_research.py#L41) | 41 | `""` | — |
| [SRC-6BF96689A8-L000042](../../tests/test_research.py#L42) | 42 | `"def test_rank_fusion_promotes_cross_provider_consensus_and_deduplicates():"` | — |
| [SRC-6BF96689A8-L000043](../../tests/test_research.py#L43) | 43 | `"    batches = ["` | — |
| [SRC-6BF96689A8-L000044](../../tests/test_research.py#L44) | 44 | `"        {"` | — |
| [SRC-6BF96689A8-L000045](../../tests/test_research.py#L45) | 45 | `"            \"query\": \"cars Egypt\","` | — |
| [SRC-6BF96689A8-L000046](../../tests/test_research.py#L46) | 46 | `"            \"provider\": \"ddg\","` | — |
| [SRC-6BF96689A8-L000047](../../tests/test_research.py#L47) | 47 | `"            \"results\": ["` | — |
| [SRC-6BF96689A8-L000048](../../tests/test_research.py#L48) | 48 | `"                {\"title\": \"A\", \"url\": \"https://www.example.com/a?utm_source=x\", \"snippet\": \"A\"},"` | — |
| [SRC-6BF96689A8-L000049](../../tests/test_research.py#L49) | 49 | `"                {\"title\": \"B\", \"url\": \"https://example.com/b\", \"snippet\": \"B\"},"` | — |
| [SRC-6BF96689A8-L000050](../../tests/test_research.py#L50) | 50 | `"            ],"` | — |
| [SRC-6BF96689A8-L000051](../../tests/test_research.py#L51) | 51 | `"        },"` | — |
| [SRC-6BF96689A8-L000052](../../tests/test_research.py#L52) | 52 | `"        {"` | — |
| [SRC-6BF96689A8-L000053](../../tests/test_research.py#L53) | 53 | `"            \"query\": \"electric vehicles Egypt\","` | — |
| [SRC-6BF96689A8-L000054](../../tests/test_research.py#L54) | 54 | `"            \"provider\": \"bing\","` | — |
| [SRC-6BF96689A8-L000055](../../tests/test_research.py#L55) | 55 | `"            \"results\": ["` | — |
| [SRC-6BF96689A8-L000056](../../tests/test_research.py#L56) | 56 | `"                {\"title\": \"A better title\", \"url\": \"https://example.com/a\", \"snippet\": \"Longer evidence snippet\"},"` | — |
| [SRC-6BF96689A8-L000057](../../tests/test_research.py#L57) | 57 | `"                {\"title\": \"C\", \"url\": \"https://example.com/c\", \"snippet\": \"C\"},"` | — |
| [SRC-6BF96689A8-L000058](../../tests/test_research.py#L58) | 58 | `"            ],"` | — |
| [SRC-6BF96689A8-L000059](../../tests/test_research.py#L59) | 59 | `"        },"` | — |
| [SRC-6BF96689A8-L000060](../../tests/test_research.py#L60) | 60 | `"    ]"` | — |
| [SRC-6BF96689A8-L000061](../../tests/test_research.py#L61) | 61 | `"    ranked = fuse_ranked_results(batches)"` | — |
| [SRC-6BF96689A8-L000062](../../tests/test_research.py#L62) | 62 | `"    urls = [source[\"url\"] for source in ranked]"` | — |
| [SRC-6BF96689A8-L000063](../../tests/test_research.py#L63) | 63 | `"    assert len(urls) == 3"` | — |
| [SRC-6BF96689A8-L000064](../../tests/test_research.py#L64) | 64 | `"    source_a = next(source for source in ranked if \"example.com/a\" in source[\"url\"])"` | — |
| [SRC-6BF96689A8-L000065](../../tests/test_research.py#L65) | 65 | `"    assert len(source_a[\"providers\"]) == 2"` | — |
| [SRC-6BF96689A8-L000066](../../tests/test_research.py#L66) | 66 | `"    assert len(source_a[\"queries\"]) == 2"` | — |
| [SRC-6BF96689A8-L000067](../../tests/test_research.py#L67) | 67 | `"    assert source_a[\"rank_score\"] > next("` | — |
| [SRC-6BF96689A8-L000068](../../tests/test_research.py#L68) | 68 | `"        source[\"rank_score\"] for source in ranked if \"example.com/c\" in source[\"url\"]"` | — |
| [SRC-6BF96689A8-L000069](../../tests/test_research.py#L69) | 69 | `"    )"` | — |
| [SRC-6BF96689A8-L000070](../../tests/test_research.py#L70) | 70 | `""` | — |
| [SRC-6BF96689A8-L000071](../../tests/test_research.py#L71) | 71 | `""` | — |
| [SRC-6BF96689A8-L000072](../../tests/test_research.py#L72) | 72 | `"def test_source_classification_distinguishes_social_and_government():"` | — |
| [SRC-6BF96689A8-L000073](../../tests/test_research.py#L73) | 73 | `"    from agents.research import classify_source"` | — |
| [SRC-6BF96689A8-L000074](../../tests/test_research.py#L74) | 74 | `""` | — |
| [SRC-6BF96689A8-L000075](../../tests/test_research.py#L75) | 75 | `"    assert classify_source(\"https://www.reddit.com/r/example/comments/1\")[\"platform\"] == \"reddit\""` | — |
| [SRC-6BF96689A8-L000076](../../tests/test_research.py#L76) | 76 | `"    assert classify_source(\"https://example.gov.eg/page\")[\"source_class\"] == \"government\""` | — |
| [SRC-6BF96689A8-L000077](../../tests/test_research.py#L77) | 77 | `""` | — |
| [SRC-6BF96689A8-L000078](../../tests/test_research.py#L78) | 78 | `""` | — |
| [SRC-6BF96689A8-L000079](../../tests/test_research.py#L79) | 79 | `"def test_explicit_page_urls_are_extracted_and_not_left_in_search_terms():"` | — |
| [SRC-6BF96689A8-L000080](../../tests/test_research.py#L80) | 80 | `"    from agents.research import extract_urls"` | — |
| [SRC-6BF96689A8-L000081](../../tests/test_research.py#L81) | 81 | `""` | — |
| [SRC-6BF96689A8-L000082](../../tests/test_research.py#L82) | 82 | `"    question = \"حلل هذه الصفحة بالتفصيل https://example.com/a?utm_source=chat#section.\""` | — |
| [SRC-6BF96689A8-L000083](../../tests/test_research.py#L83) | 83 | `"    plan = fallback_plan(question)"` | — |
| [SRC-6BF96689A8-L000084](../../tests/test_research.py#L84) | 84 | `"    assert extract_urls(question) == [\"https://example.com/a?utm_source=chat#section\"]"` | — |
| [SRC-6BF96689A8-L000085](../../tests/test_research.py#L85) | 85 | `"    assert plan[\"direct_urls\"] == [\"https://example.com/a?utm_source=chat#section\"]"` | — |
| [SRC-6BF96689A8-L000086](../../tests/test_research.py#L86) | 86 | `"    assert \"https://\" not in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000087](../../tests/test_research.py#L87) | 87 | `""` | — |
| [SRC-6BF96689A8-L000088](../../tests/test_research.py#L88) | 88 | `"def test_registrable_domain_groups_subdomains_and_respects_public_suffixes():"` | — |
| [SRC-6BF96689A8-L000089](../../tests/test_research.py#L89) | 89 | `"    assert registrable_domain(\"news.example.com\") == \"example.com\""` | — |
| [SRC-6BF96689A8-L000090](../../tests/test_research.py#L90) | 90 | `"    assert registrable_domain(\"offers.example.com\") == \"example.com\""` | — |
| [SRC-6BF96689A8-L000091](../../tests/test_research.py#L91) | 91 | `"    assert registrable_domain(\"news.example.co.uk\") == \"example.co.uk\""` | — |
| [SRC-6BF96689A8-L000092](../../tests/test_research.py#L92) | 92 | `"    assert registrable_domain(\"other.co.uk\") == \"other.co.uk\""` | — |
| [SRC-6BF96689A8-L000093](../../tests/test_research.py#L93) | 93 | `"    assert registrable_domain(\"alice.github.io\") == \"alice.github.io\""` | — |
| [SRC-6BF96689A8-L000094](../../tests/test_research.py#L94) | 94 | `"    assert registrable_domain(\"https://www.example.com/path\") == \"example.com\""` | — |
| [SRC-6BF96689A8-L000095](../../tests/test_research.py#L95) | 95 | `""` | — |
| [SRC-6BF96689A8-L000096](../../tests/test_research.py#L96) | 96 | `""` | — |
| [SRC-6BF96689A8-L000097](../../tests/test_research.py#L97) | 97 | `"def test_evidence_coverage_does_not_count_sibling_subdomains_as_independent():"` | — |
| [SRC-6BF96689A8-L000098](../../tests/test_research.py#L98) | 98 | `"    report = evidence_signal_report(["` | — |
| [SRC-6BF96689A8-L000099](../../tests/test_research.py#L99) | 99 | `"        {"` | — |
| [SRC-6BF96689A8-L000100](../../tests/test_research.py#L100) | 100 | `"            \"url\": \"https://news.example.com/story\","` | — |
| [SRC-6BF96689A8-L000101](../../tests/test_research.py#L101) | 101 | `"            \"domain\": \"news.example.com\","` | — |
| [SRC-6BF96689A8-L000102](../../tests/test_research.py#L102) | 102 | `"            \"providers\": [\"search_a\"],"` | — |
| [SRC-6BF96689A8-L000103](../../tests/test_research.py#L103) | 103 | `"        },"` | — |
| [SRC-6BF96689A8-L000104](../../tests/test_research.py#L104) | 104 | `"        {"` | — |
| [SRC-6BF96689A8-L000105](../../tests/test_research.py#L105) | 105 | `"            \"url\": \"https://offers.example.com/second-story\","` | — |
| [SRC-6BF96689A8-L000106](../../tests/test_research.py#L106) | 106 | `"            \"domain\": \"offers.example.com\","` | — |
| [SRC-6BF96689A8-L000107](../../tests/test_research.py#L107) | 107 | `"            \"providers\": [\"search_b\"],"` | — |
| [SRC-6BF96689A8-L000108](../../tests/test_research.py#L108) | 108 | `"        },"` | — |
| [SRC-6BF96689A8-L000109](../../tests/test_research.py#L109) | 109 | `"    ])"` | — |
| [SRC-6BF96689A8-L000110](../../tests/test_research.py#L110) | 110 | `"    assert report[\"unique_domains\"] == 1"` | — |
| [SRC-6BF96689A8-L000111](../../tests/test_research.py#L111) | 111 | `"    assert report[\"coverage_level\"] == \"محدود\""` | — |
## اختبارات

### FILE-01E35ABC46 — [tests/test_research_guardrails.py](../../tests/test_research_guardrails.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-01E35ABC46-L000001](../../tests/test_research_guardrails.py#L1) | 1 | `"\"\"\"Regression and adversarial tests for depth, freshness, relevance, evidence.\"\"\""` | — |
| [SRC-01E35ABC46-L000002](../../tests/test_research_guardrails.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-01E35ABC46-L000003](../../tests/test_research_guardrails.py#L3) | 3 | `""` | — |
| [SRC-01E35ABC46-L000004](../../tests/test_research_guardrails.py#L4) | 4 | `"from agents.research import ("` | — |
| [SRC-01E35ABC46-L000005](../../tests/test_research_guardrails.py#L5) | 5 | `"    decide_evidence_status,"` | — |
| [SRC-01E35ABC46-L000006](../../tests/test_research_guardrails.py#L6) | 6 | `"    detect_depth,"` | — |
| [SRC-01E35ABC46-L000007](../../tests/test_research_guardrails.py#L7) | 7 | `"    detect_freshness,"` | — |
| [SRC-01E35ABC46-L000008](../../tests/test_research_guardrails.py#L8) | 8 | `"    filter_relevant_sources,"` | — |
| [SRC-01E35ABC46-L000009](../../tests/test_research_guardrails.py#L9) | 9 | `"    source_relevance_score,"` | — |
| [SRC-01E35ABC46-L000010](../../tests/test_research_guardrails.py#L10) | 10 | `")"` | — |
| [SRC-01E35ABC46-L000011](../../tests/test_research_guardrails.py#L11) | 11 | `""` | — |
| [SRC-01E35ABC46-L000012](../../tests/test_research_guardrails.py#L12) | 12 | `""` | — |
| [SRC-01E35ABC46-L000013](../../tests/test_research_guardrails.py#L13) | 13 | `"# --- detect_depth -----------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000014](../../tests/test_research_guardrails.py#L14) | 14 | `""` | — |
| [SRC-01E35ABC46-L000015](../../tests/test_research_guardrails.py#L15) | 15 | `"def test_depth_deep_english_phrases():"` | — |
| [SRC-01E35ABC46-L000016](../../tests/test_research_guardrails.py#L16) | 16 | `"    assert detect_depth(\"Please do a deep research on climate policy\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000017](../../tests/test_research_guardrails.py#L17) | 17 | `"    assert detect_depth(\"in-depth comparison of EV batteries\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000018](../../tests/test_research_guardrails.py#L18) | 18 | `"    assert detect_depth(\"comprehensive analysis of market risks\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000019](../../tests/test_research_guardrails.py#L19) | 19 | `""` | — |
| [SRC-01E35ABC46-L000020](../../tests/test_research_guardrails.py#L20) | 20 | `""` | — |
| [SRC-01E35ABC46-L000021](../../tests/test_research_guardrails.py#L21) | 21 | `"def test_depth_deep_arabic_phrases():"` | — |
| [SRC-01E35ABC46-L000022](../../tests/test_research_guardrails.py#L22) | 22 | `"    assert detect_depth(\"أريد بحث عميق عن الذكاء الاصطناعي\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000023](../../tests/test_research_guardrails.py#L23) | 23 | `"    assert detect_depth(\"قارن بين السيارات الكهربائية والبنزين\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000024](../../tests/test_research_guardrails.py#L24) | 24 | `"    assert detect_depth(\"بحث شامل بالتفصيل عن الذهب\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000025](../../tests/test_research_guardrails.py#L25) | 25 | `""` | — |
| [SRC-01E35ABC46-L000026](../../tests/test_research_guardrails.py#L26) | 26 | `""` | — |
| [SRC-01E35ABC46-L000027](../../tests/test_research_guardrails.py#L27) | 27 | `"def test_depth_standard_ordinary_questions():"` | — |
| [SRC-01E35ABC46-L000028](../../tests/test_research_guardrails.py#L28) | 28 | `"    assert detect_depth(\"what is the capital of France\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000029](../../tests/test_research_guardrails.py#L29) | 29 | `"    assert detect_depth(\"ما عاصمة مصر\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000030](../../tests/test_research_guardrails.py#L30) | 30 | `"    assert detect_depth(\"I know about electric cars\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000031](../../tests/test_research_guardrails.py#L31) | 31 | `"    assert detect_depth(\"hello\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000032](../../tests/test_research_guardrails.py#L32) | 32 | `"    assert detect_depth(\"\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000033](../../tests/test_research_guardrails.py#L33) | 33 | `""` | — |
| [SRC-01E35ABC46-L000034](../../tests/test_research_guardrails.py#L34) | 34 | `""` | — |
| [SRC-01E35ABC46-L000035](../../tests/test_research_guardrails.py#L35) | 35 | `"def test_depth_does_not_trigger_on_partial_words():"` | — |
| [SRC-01E35ABC46-L000036](../../tests/test_research_guardrails.py#L36) | 36 | `"    # \"sources\" is a deep term; ensure isolated ordinary use still works via whole-word"` | — |
| [SRC-01E35ABC46-L000037](../../tests/test_research_guardrails.py#L37) | 37 | `"    assert detect_depth(\"the river sources of the Nile\") in {\"deep\", \"standard\"}  # may match"` | — |
| [SRC-01E35ABC46-L000038](../../tests/test_research_guardrails.py#L38) | 38 | `"    assert detect_depth(\"tell me a joke\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000039](../../tests/test_research_guardrails.py#L39) | 39 | `""` | — |
| [SRC-01E35ABC46-L000040](../../tests/test_research_guardrails.py#L40) | 40 | `""` | — |
| [SRC-01E35ABC46-L000041](../../tests/test_research_guardrails.py#L41) | 41 | `"# --- detect_freshness -------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000042](../../tests/test_research_guardrails.py#L42) | 42 | `""` | — |
| [SRC-01E35ABC46-L000043](../../tests/test_research_guardrails.py#L43) | 43 | `"def test_freshness_positive_english():"` | — |
| [SRC-01E35ABC46-L000044](../../tests/test_research_guardrails.py#L44) | 44 | `"    assert detect_freshness(\"what is happening now\") is True"` | — |
| [SRC-01E35ABC46-L000045](../../tests/test_research_guardrails.py#L45) | 45 | `"    assert detect_freshness(\"latest news about Egypt\") is True"` | — |
| [SRC-01E35ABC46-L000046](../../tests/test_research_guardrails.py#L46) | 46 | `"    assert detect_freshness(\"price today of gold\") is True"` | — |
| [SRC-01E35ABC46-L000047](../../tests/test_research_guardrails.py#L47) | 47 | `"    assert detect_freshness(\"breaking news\") is True"` | — |
