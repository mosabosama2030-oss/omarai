# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **041**
- سجلات الأسطر: **800**
- النطاق: SRC-1A176AD4F0-L000186 إلى SRC-62DC597310-L000268
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-1A176AD4F0 — [tests/test_hosted_smoke.py](../../tests/test_hosted_smoke.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1A176AD4F0-L000186](../../tests/test_hosted_smoke.py#L186) | 186 | `"        run_smoke("` | — |
| [SRC-1A176AD4F0-L000187](../../tests/test_hosted_smoke.py#L187) | 187 | `"            hosted_server,"` | — |
| [SRC-1A176AD4F0-L000188](../../tests/test_hosted_smoke.py#L188) | 188 | `"            TOKEN,"` | — |
| [SRC-1A176AD4F0-L000189](../../tests/test_hosted_smoke.py#L189) | 189 | `"            allow_http=True,"` | — |
| [SRC-1A176AD4F0-L000190](../../tests/test_hosted_smoke.py#L190) | 190 | `"            timeout=5,"` | — |
| [SRC-1A176AD4F0-L000191](../../tests/test_hosted_smoke.py#L191) | 191 | `"            expected_sha=\"a\" * 40,"` | — |
| [SRC-1A176AD4F0-L000192](../../tests/test_hosted_smoke.py#L192) | 192 | `"        )"` | — |
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
| [SRC-EA6EC52573-L000005](../../tests/test_intent_router.py#L5) | 5 | `"from agents.intent_router import resolve_followup_query, route_intent"` | — |
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
| [SRC-EA6EC52573-L000125](../../tests/test_intent_router.py#L125) | 125 | `""` | — |
| [SRC-EA6EC52573-L000126](../../tests/test_intent_router.py#L126) | 126 | `""` | — |
| [SRC-EA6EC52573-L000127](../../tests/test_intent_router.py#L127) | 127 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000128](../../tests/test_intent_router.py#L128) | 128 | `"    \"question\","` | — |
| [SRC-EA6EC52573-L000129](../../tests/test_intent_router.py#L129) | 129 | `"    ["` | — |
| [SRC-EA6EC52573-L000130](../../tests/test_intent_router.py#L130) | 130 | `"        \"فين؟\","` | — |
| [SRC-EA6EC52573-L000131](../../tests/test_intent_router.py#L131) | 131 | `"        \"فين هي؟\","` | — |
| [SRC-EA6EC52573-L000132](../../tests/test_intent_router.py#L132) | 132 | `"        \"مكانها فين؟\","` | — |
| [SRC-EA6EC52573-L000133](../../tests/test_intent_router.py#L133) | 133 | `"        \"هل فيه ضمان؟\","` | — |
| [SRC-EA6EC52573-L000134](../../tests/test_intent_router.py#L134) | 134 | `"        \"هل لها ضمان؟\","` | — |
| [SRC-EA6EC52573-L000135](../../tests/test_intent_router.py#L135) | 135 | `"        \"ضمانها إيه؟\","` | — |
| [SRC-EA6EC52573-L000136](../../tests/test_intent_router.py#L136) | 136 | `"        \"Where is it?\","` | — |
| [SRC-EA6EC52573-L000137](../../tests/test_intent_router.py#L137) | 137 | `"        \"Does it have a warranty?\","` | — |
| [SRC-EA6EC52573-L000138](../../tests/test_intent_router.py#L138) | 138 | `"    ],"` | — |
| [SRC-EA6EC52573-L000139](../../tests/test_intent_router.py#L139) | 139 | `")"` | — |
| [SRC-EA6EC52573-L000140](../../tests/test_intent_router.py#L140) | 140 | `"def test_missing_referent_questions_clarify_without_context(question: str) -> None:"` | — |
| [SRC-EA6EC52573-L000141](../../tests/test_intent_router.py#L141) | 141 | `"    decision = route_intent(question, history=None, mode=\"auto\", requires_web=True)"` | — |
| [SRC-EA6EC52573-L000142](../../tests/test_intent_router.py#L142) | 142 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000143](../../tests/test_intent_router.py#L143) | 143 | `"    assert decision[\"needs_clarification\"] is True"` | — |
| [SRC-EA6EC52573-L000144](../../tests/test_intent_router.py#L144) | 144 | `"    assert decision[\"context_available\"] is False"` | — |
| [SRC-EA6EC52573-L000145](../../tests/test_intent_router.py#L145) | 145 | `""` | — |
| [SRC-EA6EC52573-L000146](../../tests/test_intent_router.py#L146) | 146 | `""` | — |
| [SRC-EA6EC52573-L000147](../../tests/test_intent_router.py#L147) | 147 | `"@pytest.mark.parametrize(\"question\", [\"فين؟\", \"هل فيه ضمان؟\", \"كام سعرها؟\"])"` | — |
| [SRC-EA6EC52573-L000148](../../tests/test_intent_router.py#L148) | 148 | `"def test_missing_referent_still_clarifies_in_explicit_search_mode(question: str) -> None:"` | — |
| [SRC-EA6EC52573-L000149](../../tests/test_intent_router.py#L149) | 149 | `"    decision = route_intent(question, history=None, mode=\"deep\")"` | — |
| [SRC-EA6EC52573-L000150](../../tests/test_intent_router.py#L150) | 150 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000151](../../tests/test_intent_router.py#L151) | 151 | `"    assert decision[\"needs_clarification\"] is True"` | — |
| [SRC-EA6EC52573-L000152](../../tests/test_intent_router.py#L152) | 152 | `""` | — |
| [SRC-EA6EC52573-L000153](../../tests/test_intent_router.py#L153) | 153 | `""` | — |
| [SRC-EA6EC52573-L000154](../../tests/test_intent_router.py#L154) | 154 | `"def test_followup_resolver_uses_topic_from_latest_user_turn() -> None:"` | — |
| [SRC-EA6EC52573-L000155](../../tests/test_intent_router.py#L155) | 155 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000156](../../tests/test_intent_router.py#L156) | 156 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر آيفون 16 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000157](../../tests/test_intent_router.py#L157) | 157 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن معلومات موثوقة.\"},"` | — |
| [SRC-EA6EC52573-L000158](../../tests/test_intent_router.py#L158) | 158 | `"    ]"` | — |
| [SRC-EA6EC52573-L000159](../../tests/test_intent_router.py#L159) | 159 | `"    resolved = resolve_followup_query(\"هل فيه ضمان؟\", history)"` | — |
| [SRC-EA6EC52573-L000160](../../tests/test_intent_router.py#L160) | 160 | `"    assert \"آيفون 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000161](../../tests/test_intent_router.py#L161) | 161 | `"    assert \"ضمان\" in resolved"` | — |
| [SRC-EA6EC52573-L000162](../../tests/test_intent_router.py#L162) | 162 | `""` | — |
| [SRC-EA6EC52573-L000163](../../tests/test_intent_router.py#L163) | 163 | `""` | — |
| [SRC-EA6EC52573-L000164](../../tests/test_intent_router.py#L164) | 164 | `"def test_followup_resolver_does_not_resurrect_topic_after_acknowledgment() -> None:"` | — |
| [SRC-EA6EC52573-L000165](../../tests/test_intent_router.py#L165) | 165 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000166](../../tests/test_intent_router.py#L166) | 166 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر آيفون 16 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000167](../../tests/test_intent_router.py#L167) | 167 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن معلومات موثوقة.\"},"` | — |
| [SRC-EA6EC52573-L000168](../../tests/test_intent_router.py#L168) | 168 | `"        {\"role\": \"user\", \"content\": \"شكرًا\"},"` | — |
| [SRC-EA6EC52573-L000169](../../tests/test_intent_router.py#L169) | 169 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-EA6EC52573-L000170](../../tests/test_intent_router.py#L170) | 170 | `"    ]"` | — |
| [SRC-EA6EC52573-L000171](../../tests/test_intent_router.py#L171) | 171 | `"    assert resolve_followup_query(\"فين؟\", history) == \"فين؟\""` | — |
| [SRC-EA6EC52573-L000172](../../tests/test_intent_router.py#L172) | 172 | `""` | — |
| [SRC-EA6EC52573-L000173](../../tests/test_intent_router.py#L173) | 173 | `""` | — |
| [SRC-EA6EC52573-L000174](../../tests/test_intent_router.py#L174) | 174 | `"def test_followup_resolver_bounds_output_and_handles_malformed_history() -> None:"` | — |
| [SRC-EA6EC52573-L000175](../../tests/test_intent_router.py#L175) | 175 | `"    history = [{\"role\": \"user\", \"content\": \"س\" * 4000}]"` | — |
| [SRC-EA6EC52573-L000176](../../tests/test_intent_router.py#L176) | 176 | `"    assert len(resolve_followup_query(\"والسعر؟\", history)) <= 500"` | — |
| [SRC-EA6EC52573-L000177](../../tests/test_intent_router.py#L177) | 177 | `"    assert resolve_followup_query(\"فين؟\", {\"role\": \"user\", \"content\": \"topic\"}) == \"فين؟\""` | — |
| [SRC-EA6EC52573-L000178](../../tests/test_intent_router.py#L178) | 178 | `""` | — |
| [SRC-EA6EC52573-L000179](../../tests/test_intent_router.py#L179) | 179 | `"def test_prefixed_elliptical_followup_is_clarified_without_topic():"` | — |
| [SRC-EA6EC52573-L000180](../../tests/test_intent_router.py#L180) | 180 | `"    for question in (\"طب هل فيه ضمان؟\", \"طيب كام سعرها؟\", \"والضمان؟\", \"والسعر؟\"):"` | — |
| [SRC-EA6EC52573-L000181](../../tests/test_intent_router.py#L181) | 181 | `"        decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000182](../../tests/test_intent_router.py#L182) | 182 | `"        assert decision[\"route\"] == \"CLARIFY\", question"` | — |
| [SRC-EA6EC52573-L000183](../../tests/test_intent_router.py#L183) | 183 | `""` | — |
| [SRC-EA6EC52573-L000184](../../tests/test_intent_router.py#L184) | 184 | `"def test_prefixed_elliptical_followup_uses_topic_when_available():"` | — |
| [SRC-EA6EC52573-L000185](../../tests/test_intent_router.py#L185) | 185 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000186](../../tests/test_intent_router.py#L186) | 186 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 16 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000187](../../tests/test_intent_router.py#L187) | 187 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن iPhone 16 في مصر.\"},"` | — |
| [SRC-EA6EC52573-L000188](../../tests/test_intent_router.py#L188) | 188 | `"    ]"` | — |
| [SRC-EA6EC52573-L000189](../../tests/test_intent_router.py#L189) | 189 | `"    for question in (\"طب هل فيه ضمان؟\", \"طيب كام سعرها؟\", \"والضمان؟\"):"` | — |
| [SRC-EA6EC52573-L000190](../../tests/test_intent_router.py#L190) | 190 | `"        decision = route_intent(question, history, requires_web=True)"` | — |
| [SRC-EA6EC52573-L000191](../../tests/test_intent_router.py#L191) | 191 | `"        assert decision[\"route\"] == \"WEB_SIMPLE\", question"` | — |
| [SRC-EA6EC52573-L000192](../../tests/test_intent_router.py#L192) | 192 | `"        resolved = resolve_followup_query(question, history)"` | — |
| [SRC-EA6EC52573-L000193](../../tests/test_intent_router.py#L193) | 193 | `"        assert \"iPhone 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000194](../../tests/test_intent_router.py#L194) | 194 | `"        assert \"مصر\" in resolved"` | — |
| [SRC-EA6EC52573-L000195](../../tests/test_intent_router.py#L195) | 195 | `""` | — |
| [SRC-EA6EC52573-L000196](../../tests/test_intent_router.py#L196) | 196 | `"def test_long_arabic_warranty_followup_resolves_with_context():"` | — |
| [SRC-EA6EC52573-L000197](../../tests/test_intent_router.py#L197) | 197 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000198](../../tests/test_intent_router.py#L198) | 198 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 نسخة 256 جيجابايت في مصر\"},"` | — |
| [SRC-EA6EC52573-L000199](../../tests/test_intent_router.py#L199) | 199 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن السعر.\"},"` | — |
| [SRC-EA6EC52573-L000200](../../tests/test_intent_router.py#L200) | 200 | `"    ]"` | — |
| [SRC-EA6EC52573-L000201](../../tests/test_intent_router.py#L201) | 201 | `"    question = \"وطب الضمان الدولي بيسري في مصر؟\""` | — |
| [SRC-EA6EC52573-L000202](../../tests/test_intent_router.py#L202) | 202 | `"    resolved = resolve_followup_query(question, history)"` | — |
| [SRC-EA6EC52573-L000203](../../tests/test_intent_router.py#L203) | 203 | `"    assert \"iPhone 17\" in resolved"` | — |
| [SRC-EA6EC52573-L000204](../../tests/test_intent_router.py#L204) | 204 | `"    assert question in resolved"` | — |
| [SRC-EA6EC52573-L000205](../../tests/test_intent_router.py#L205) | 205 | `""` | — |
| [SRC-EA6EC52573-L000206](../../tests/test_intent_router.py#L206) | 206 | `"def test_long_arabic_warranty_followup_without_context_clarifies():"` | — |
| [SRC-EA6EC52573-L000207](../../tests/test_intent_router.py#L207) | 207 | `"    question = \"وطب الضمان الدولي بيسري في مصر؟\""` | — |
| [SRC-EA6EC52573-L000208](../../tests/test_intent_router.py#L208) | 208 | `"    decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000209](../../tests/test_intent_router.py#L209) | 209 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000210](../../tests/test_intent_router.py#L210) | 210 | `"    assert decision[\"needs_clarification\"] is True"` | — |
| [SRC-EA6EC52573-L000211](../../tests/test_intent_router.py#L211) | 211 | `""` | — |
| [SRC-EA6EC52573-L000212](../../tests/test_intent_router.py#L212) | 212 | `"def test_new_question_starting_with_tayyib_does_not_inherit_old_topic():"` | — |
| [SRC-EA6EC52573-L000213](../../tests/test_intent_router.py#L213) | 213 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000214](../../tests/test_intent_router.py#L214) | 214 | `"        {\"role\": \"user\", \"content\": \"ما سعر iPhone 16 في مصر؟\"},"` | — |
| [SRC-EA6EC52573-L000215](../../tests/test_intent_router.py#L215) | 215 | `"        {\"role\": \"assistant\", \"content\": \"هذه بعض معلومات السعر.\"},"` | — |
| [SRC-EA6EC52573-L000216](../../tests/test_intent_router.py#L216) | 216 | `"    ]"` | — |
| [SRC-EA6EC52573-L000217](../../tests/test_intent_router.py#L217) | 217 | `"    question = \"طيب اشرح الذكاء الاصطناعي في المدارس\""` | — |
| [SRC-EA6EC52573-L000218](../../tests/test_intent_router.py#L218) | 218 | `"    assert resolve_followup_query(question, history) == question"` | — |
| [SRC-EA6EC52573-L000219](../../tests/test_intent_router.py#L219) | 219 | `"    decision = route_intent(question, history)"` | — |
| [SRC-EA6EC52573-L000220](../../tests/test_intent_router.py#L220) | 220 | `"    assert decision[\"route\"] == \"MODEL_ONLY\""` | — |
| [SRC-EA6EC52573-L000221](../../tests/test_intent_router.py#L221) | 221 | `""` | — |
| [SRC-EA6EC52573-L000222](../../tests/test_intent_router.py#L222) | 222 | `"def test_chained_followups_keep_the_last_substantive_topic():"` | — |
| [SRC-EA6EC52573-L000223](../../tests/test_intent_router.py#L223) | 223 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000224](../../tests/test_intent_router.py#L224) | 224 | `"        {\"role\": \"user\", \"content\": \"ما سعر iPhone 16 في مصر؟\"},"` | — |
| [SRC-EA6EC52573-L000225](../../tests/test_intent_router.py#L225) | 225 | `"        {\"role\": \"assistant\", \"content\": \"السعر يختلف حسب المتجر.\"},"` | — |
| [SRC-EA6EC52573-L000226](../../tests/test_intent_router.py#L226) | 226 | `"        {\"role\": \"user\", \"content\": \"والضمان؟\"},"` | — |
| [SRC-EA6EC52573-L000227](../../tests/test_intent_router.py#L227) | 227 | `"        {\"role\": \"assistant\", \"content\": \"سأوضح الضمان.\"},"` | — |
| [SRC-EA6EC52573-L000228](../../tests/test_intent_router.py#L228) | 228 | `"    ]"` | — |
| [SRC-EA6EC52573-L000229](../../tests/test_intent_router.py#L229) | 229 | `"    resolved = resolve_followup_query(\"والبطارية؟\", history)"` | — |
| [SRC-EA6EC52573-L000230](../../tests/test_intent_router.py#L230) | 230 | `"    assert \"iPhone 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000231](../../tests/test_intent_router.py#L231) | 231 | `"    assert \"البطارية\" in resolved"` | — |
| [SRC-EA6EC52573-L000232](../../tests/test_intent_router.py#L232) | 232 | `""` | — |
| [SRC-EA6EC52573-L000233](../../tests/test_intent_router.py#L233) | 233 | `"def test_answer_to_clarification_restores_original_intent():"` | — |
| [SRC-EA6EC52573-L000234](../../tests/test_intent_router.py#L234) | 234 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000235](../../tests/test_intent_router.py#L235) | 235 | `"        {\"role\": \"user\", \"content\": \"كام سعرها؟\"},"` | — |
| [SRC-EA6EC52573-L000236](../../tests/test_intent_router.py#L236) | 236 | `"        {"` | — |
| [SRC-EA6EC52573-L000237](../../tests/test_intent_router.py#L237) | 237 | `"            \"role\": \"assistant\","` | — |
| [SRC-EA6EC52573-L000238](../../tests/test_intent_router.py#L238) | 238 | `"            \"content\": \"تقصد إيه تحديدًا؟ اكتب اسم الشيء أو المنتج المقصود، أو ابعت الرابط، وأكمل معاك من غير ما أخمّن.\","` | — |
| [SRC-EA6EC52573-L000239](../../tests/test_intent_router.py#L239) | 239 | `"        },"` | — |
| [SRC-EA6EC52573-L000240](../../tests/test_intent_router.py#L240) | 240 | `"    ]"` | — |
| [SRC-EA6EC52573-L000241](../../tests/test_intent_router.py#L241) | 241 | `"    decision = route_intent(\"iPhone 16\", history)"` | — |
| [SRC-EA6EC52573-L000242](../../tests/test_intent_router.py#L242) | 242 | `"    assert decision[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000243](../../tests/test_intent_router.py#L243) | 243 | `"    assert decision[\"reason\"] == \"answer_to_pending_clarification\""` | — |
| [SRC-EA6EC52573-L000244](../../tests/test_intent_router.py#L244) | 244 | `"    resolved = resolve_followup_query(\"iPhone 16\", history)"` | — |
| [SRC-EA6EC52573-L000245](../../tests/test_intent_router.py#L245) | 245 | `"    assert \"سعرها\" in resolved"` | — |
| [SRC-EA6EC52573-L000246](../../tests/test_intent_router.py#L246) | 246 | `"    assert \"iPhone 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000247](../../tests/test_intent_router.py#L247) | 247 | `""` | — |
| [SRC-EA6EC52573-L000248](../../tests/test_intent_router.py#L248) | 248 | `"def test_topic_detection_does_not_inherit_old_social_or_depth_intent():"` | — |
| [SRC-EA6EC52573-L000249](../../tests/test_intent_router.py#L249) | 249 | `"    from agents.research import fallback_plan"` | — |
| [SRC-EA6EC52573-L000250](../../tests/test_intent_router.py#L250) | 250 | `""` | — |
| [SRC-EA6EC52573-L000251](../../tests/test_intent_router.py#L251) | 251 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000252](../../tests/test_intent_router.py#L252) | 252 | `"        {\"role\": \"user\", \"content\": \"اجمع آراء مستخدمي السيارات الكهربائية على Reddit\"},"` | — |
| [SRC-EA6EC52573-L000253](../../tests/test_intent_router.py#L253) | 253 | `"        {\"role\": \"assistant\", \"content\": \"هذه النتائج.\"},"` | — |
| [SRC-EA6EC52573-L000254](../../tests/test_intent_router.py#L254) | 254 | `"    ]"` | — |
| [SRC-EA6EC52573-L000255](../../tests/test_intent_router.py#L255) | 255 | `"    plan = fallback_plan(\"اشرح طريقة عمل المحرك الكهربائي\", history)"` | — |
| [SRC-EA6EC52573-L000256](../../tests/test_intent_router.py#L256) | 256 | `"    assert plan[\"social_focus\"] is False"` | — |
| [SRC-EA6EC52573-L000257](../../tests/test_intent_router.py#L257) | 257 | `"    assert plan[\"platforms\"] == []"` | — |
| [SRC-EA6EC52573-L000258](../../tests/test_intent_router.py#L258) | 258 | `"    assert plan[\"depth\"] == \"standard\""` | — |
| [SRC-EA6EC52573-L000259](../../tests/test_intent_router.py#L259) | 259 | `""` | — |
| [SRC-EA6EC52573-L000260](../../tests/test_intent_router.py#L260) | 260 | `"def test_explicit_request_for_reliable_sources_uses_web_search_in_auto_mode():"` | — |
| [SRC-EA6EC52573-L000261](../../tests/test_intent_router.py#L261) | 261 | `"    question = ("` | — |
| [SRC-EA6EC52573-L000262](../../tests/test_intent_router.py#L262) | 262 | `"        \"ما أهم استخدامات الذكاء الاصطناعي في الشركات الصغيرة؟ \""` | — |
| [SRC-EA6EC52573-L000263](../../tests/test_intent_router.py#L263) | 263 | `"        \"اذكر أمثلة ومصادر موثوقة.\""` | — |
| [SRC-EA6EC52573-L000264](../../tests/test_intent_router.py#L264) | 264 | `"    )"` | — |
| [SRC-EA6EC52573-L000265](../../tests/test_intent_router.py#L265) | 265 | `"    decision = route_intent(question, mode=\"auto\")"` | — |
| [SRC-EA6EC52573-L000266](../../tests/test_intent_router.py#L266) | 266 | `"    assert decision[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000267](../../tests/test_intent_router.py#L267) | 267 | `"    assert decision[\"reason\"] == \"explicit_evidence_request\""` | — |
| [SRC-EA6EC52573-L000268](../../tests/test_intent_router.py#L268) | 268 | `""` | — |
| [SRC-EA6EC52573-L000269](../../tests/test_intent_router.py#L269) | 269 | `"def test_stable_question_without_source_request_remains_model_only():"` | — |
| [SRC-EA6EC52573-L000270](../../tests/test_intent_router.py#L270) | 270 | `"    decision = route_intent(\"اشرح الفرق بين التعلم الخاضع للإشراف وغير الخاضع للإشراف\")"` | — |
| [SRC-EA6EC52573-L000271](../../tests/test_intent_router.py#L271) | 271 | `"    assert decision[\"route\"] == \"MODEL_ONLY\""` | — |
| [SRC-EA6EC52573-L000272](../../tests/test_intent_router.py#L272) | 272 | `""` | — |
| [SRC-EA6EC52573-L000273](../../tests/test_intent_router.py#L273) | 273 | `"def test_attached_arabic_object_pronoun_resolves_against_previous_subject() -> None:"` | — |
| [SRC-EA6EC52573-L000274](../../tests/test_intent_router.py#L274) | 274 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000275](../../tests/test_intent_router.py#L275) | 275 | `"        {\"role\": \"user\", \"content\": \"بفكر أشتري Lenovo ThinkPad E14 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000276](../../tests/test_intent_router.py#L276) | 276 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن Lenovo ThinkPad E14 في السوق المصري.\"},"` | — |
| [SRC-EA6EC52573-L000277](../../tests/test_intent_router.py#L277) | 277 | `"    ]"` | — |
| [SRC-EA6EC52573-L000278](../../tests/test_intent_router.py#L278) | 278 | `""` | — |
| [SRC-EA6EC52573-L000279](../../tests/test_intent_router.py#L279) | 279 | `"    resolved = resolve_followup_query(\"أقدر أشتريه منين؟\", history)"` | — |
| [SRC-EA6EC52573-L000280](../../tests/test_intent_router.py#L280) | 280 | `""` | — |
| [SRC-EA6EC52573-L000281](../../tests/test_intent_router.py#L281) | 281 | `"    assert \"Lenovo ThinkPad E14\" in resolved"` | — |
| [SRC-EA6EC52573-L000282](../../tests/test_intent_router.py#L282) | 282 | `"    assert \"أقدر أشتريه منين\" in resolved"` | — |
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
| [SRC-4397BC2CD2-L000159](../../tests/test_intent_router_integration.py#L159) | 159 | `""` | — |
| [SRC-4397BC2CD2-L000160](../../tests/test_intent_router_integration.py#L160) | 160 | `"    result = agent.answer("` | — |
| [SRC-4397BC2CD2-L000161](../../tests/test_intent_router_integration.py#L161) | 161 | `"        \"قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية والكاميرا\","` | — |
| [SRC-4397BC2CD2-L000162](../../tests/test_intent_router_integration.py#L162) | 162 | `"        history=history,"` | — |
| [SRC-4397BC2CD2-L000163](../../tests/test_intent_router_integration.py#L163) | 163 | `"    )"` | — |
| [SRC-4397BC2CD2-L000164](../../tests/test_intent_router_integration.py#L164) | 164 | `""` | — |
| [SRC-4397BC2CD2-L000165](../../tests/test_intent_router_integration.py#L165) | 165 | `"    assert result[\"intent_route\"] == \"WEB_DEEP\""` | — |
| [SRC-4397BC2CD2-L000166](../../tests/test_intent_router_integration.py#L166) | 166 | `"    assert result[\"research_plan\"][\"intent_route\"] == \"WEB_DEEP\""` | — |
| [SRC-4397BC2CD2-L000167](../../tests/test_intent_router_integration.py#L167) | 167 | `"    assert result[\"research_plan\"][\"depth\"] == \"deep\""` | — |
| [SRC-4397BC2CD2-L000168](../../tests/test_intent_router_integration.py#L168) | 168 | `"    initial_plan = seen[\"plans\"][0]"` | — |
| [SRC-4397BC2CD2-L000169](../../tests/test_intent_router_integration.py#L169) | 169 | `"    assert len(initial_plan[\"queries\"]) > 1"` | — |
| [SRC-4397BC2CD2-L000170](../../tests/test_intent_router_integration.py#L170) | 170 | `"    assert initial_plan[\"coverage_gap_repair_slot_reserved\"] is True"` | — |
| [SRC-4397BC2CD2-L000171](../../tests/test_intent_router_integration.py#L171) | 171 | `"    assert initial_plan[\"query_limit\"] == 7"` | — |
| [SRC-4397BC2CD2-L000172](../../tests/test_intent_router_integration.py#L172) | 172 | `"    # Each requested criterion gets a distinct search angle before generic deep"` | — |
| [SRC-4397BC2CD2-L000173](../../tests/test_intent_router_integration.py#L173) | 173 | `"    # modifiers consume the bounded query budget."` | — |
| [SRC-4397BC2CD2-L000174](../../tests/test_intent_router_integration.py#L174) | 174 | `"    planned_queries = \" \".join(initial_plan[\"queries\"]).casefold()"` | — |
| [SRC-4397BC2CD2-L000175](../../tests/test_intent_router_integration.py#L175) | 175 | `"    assert \"السعر\" in planned_queries"` | — |
| [SRC-4397BC2CD2-L000176](../../tests/test_intent_router_integration.py#L176) | 176 | `"    assert \"البطارية\" in planned_queries"` | — |
| [SRC-4397BC2CD2-L000177](../../tests/test_intent_router_integration.py#L177) | 177 | `"    assert \"الكاميرا\" in planned_queries"` | — |
| [SRC-4397BC2CD2-L000178](../../tests/test_intent_router_integration.py#L178) | 178 | `"    assert len(initial_plan[\"queries\"]) <= 7"` | — |
| [SRC-4397BC2CD2-L000179](../../tests/test_intent_router_integration.py#L179) | 179 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-4397BC2CD2-L000180](../../tests/test_intent_router_integration.py#L180) | 180 | `"    coverage = result[\"answer_coverage\"]"` | — |
| [SRC-4397BC2CD2-L000181](../../tests/test_intent_router_integration.py#L181) | 181 | `"    assert coverage[\"method\"] == \"explicit_criteria_heuristic\""` | — |
| [SRC-4397BC2CD2-L000182](../../tests/test_intent_router_integration.py#L182) | 182 | `"    assert coverage[\"targets\"] == [\"السعر\", \"البطارية\", \"الكاميرا\"]"` | — |
| [SRC-4397BC2CD2-L000183](../../tests/test_intent_router_integration.py#L183) | 183 | `"    assert coverage[\"status\"] == \"model_review_requested_not_machine_verified\""` | — |
| [SRC-4397BC2CD2-L000184](../../tests/test_intent_router_integration.py#L184) | 184 | `"    assert coverage[\"automatically_graded\"] is False"` | — |
| [SRC-4397BC2CD2-L000185](../../tests/test_intent_router_integration.py#L185) | 185 | `"    # The mocked sources do not contain battery/camera evidence. The task must"` | — |
| [SRC-4397BC2CD2-L000186](../../tests/test_intent_router_integration.py#L186) | 186 | `"    # remain visibly incomplete even if the planner generated multiple queries."` | — |
| [SRC-4397BC2CD2-L000187](../../tests/test_intent_router_integration.py#L187) | 187 | `"    assert coverage[\"source_evidence_gap_count\"] == 2"` | — |
| [SRC-4397BC2CD2-L000188](../../tests/test_intent_router_integration.py#L188) | 188 | `"    assert result[\"task_fulfillment_status\"] == \"possible_gap_detected\""` | — |
| [SRC-4397BC2CD2-L000189](../../tests/test_intent_router_integration.py#L189) | 189 | `"    assert len(seen[\"plans\"]) == 2"` | — |
| [SRC-4397BC2CD2-L000190](../../tests/test_intent_router_integration.py#L190) | 190 | `"    assert \"البطارية\" in \" \".join(seen[\"plans\"][1][\"queries\"])"` | — |
| [SRC-4397BC2CD2-L000191](../../tests/test_intent_router_integration.py#L191) | 191 | `"    assert result[\"search_report\"][\"criterion_gap_research\"][\"attempted\"] is True"` | — |
| [SRC-4397BC2CD2-L000192](../../tests/test_intent_router_integration.py#L192) | 192 | `"    assert result[\"search_report\"][\"criterion_gap_research\"][\"status\"] == \"search_completed_no_new_criterion_evidence\""` | — |
| [SRC-4397BC2CD2-L000193](../../tests/test_intent_router_integration.py#L193) | 193 | `""` | — |
| [SRC-4397BC2CD2-L000194](../../tests/test_intent_router_integration.py#L194) | 194 | `"def test_deep_plan_preserves_all_eight_explicit_criteria_within_query_budget(monkeypatch) -> None:"` | — |
| [SRC-4397BC2CD2-L000195](../../tests/test_intent_router_integration.py#L195) | 195 | `"    agent = WebAgent()"` | — |
| [SRC-4397BC2CD2-L000196](../../tests/test_intent_router_integration.py#L196) | 196 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-4397BC2CD2-L000197](../../tests/test_intent_router_integration.py#L197) | 197 | `"    seen: dict = {\"plans\": []}"` | — |
| [SRC-4397BC2CD2-L000198](../../tests/test_intent_router_integration.py#L198) | 198 | `"    question = ("` | — |
| [SRC-4397BC2CD2-L000199](../../tests/test_intent_router_integration.py#L199) | 199 | `"        \"قارن بين خدمات من حيث السعر، الخصوصية، الاعتمادية، الدعم، \""` | — |
| [SRC-4397BC2CD2-L000200](../../tests/test_intent_router_integration.py#L200) | 200 | `"        \"الأمان، السرعة، الجودة، والتوفر\""` | — |
| [SRC-4397BC2CD2-L000201](../../tests/test_intent_router_integration.py#L201) | 201 | `"    )"` | — |
| [SRC-4397BC2CD2-L000202](../../tests/test_intent_router_integration.py#L202) | 202 | `""` | — |
| [SRC-4397BC2CD2-L000203](../../tests/test_intent_router_integration.py#L203) | 203 | `"    def plan(_question, _history):"` | — |
| [SRC-4397BC2CD2-L000204](../../tests/test_intent_router_integration.py#L204) | 204 | `"        return {"` | — |
| [SRC-4397BC2CD2-L000205](../../tests/test_intent_router_integration.py#L205) | 205 | `"            \"queries\": [\"مقارنة الخدمات\"],"` | — |
| [SRC-4397BC2CD2-L000206](../../tests/test_intent_router_integration.py#L206) | 206 | `"            \"direct_urls\": [],"` | — |
| [SRC-4397BC2CD2-L000207](../../tests/test_intent_router_integration.py#L207) | 207 | `"            \"social_focus\": False,"` | — |
| [SRC-4397BC2CD2-L000208](../../tests/test_intent_router_integration.py#L208) | 208 | `"            \"freshness\": \"any\","` | — |
| [SRC-4397BC2CD2-L000209](../../tests/test_intent_router_integration.py#L209) | 209 | `"            \"depth\": \"standard\","` | — |
| [SRC-4397BC2CD2-L000210](../../tests/test_intent_router_integration.py#L210) | 210 | `"            \"platforms\": [],"` | — |
| [SRC-4397BC2CD2-L000211](../../tests/test_intent_router_integration.py#L211) | 211 | `"            \"planning_method\": \"test_single_query\","` | — |
| [SRC-4397BC2CD2-L000212](../../tests/test_intent_router_integration.py#L212) | 212 | `"        }"` | — |
| [SRC-4397BC2CD2-L000213](../../tests/test_intent_router_integration.py#L213) | 213 | `""` | — |
| [SRC-4397BC2CD2-L000214](../../tests/test_intent_router_integration.py#L214) | 214 | `"    def collect(research_plan):"` | — |
| [SRC-4397BC2CD2-L000215](../../tests/test_intent_router_integration.py#L215) | 215 | `"        seen[\"plans\"].append(dict(research_plan))"` | — |
| [SRC-4397BC2CD2-L000216](../../tests/test_intent_router_integration.py#L216) | 216 | `"        sources = ["` | — |
| [SRC-4397BC2CD2-L000217](../../tests/test_intent_router_integration.py#L217) | 217 | `"            _evidence(\"example.com\", research_plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000218](../../tests/test_intent_router_integration.py#L218) | 218 | `"            _evidence(\"example.net\", research_plan[\"queries\"]),"` | — |
| [SRC-4397BC2CD2-L000219](../../tests/test_intent_router_integration.py#L219) | 219 | `"        ]"` | — |
| [SRC-4397BC2CD2-L000220](../../tests/test_intent_router_integration.py#L220) | 220 | `"        return sources, [], _report(research_plan, sources)"` | — |
| [SRC-4397BC2CD2-L000221](../../tests/test_intent_router_integration.py#L221) | 221 | `""` | — |
| [SRC-4397BC2CD2-L000222](../../tests/test_intent_router_integration.py#L222) | 222 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-4397BC2CD2-L000223](../../tests/test_intent_router_integration.py#L223) | 223 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-4397BC2CD2-L000224](../../tests/test_intent_router_integration.py#L224) | 224 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda _query, _source: True)"` | — |
| [SRC-4397BC2CD2-L000225](../../tests/test_intent_router_integration.py#L225) | 225 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"مقارنة أولية [المصدر 1].\")"` | — |
| [SRC-4397BC2CD2-L000226](../../tests/test_intent_router_integration.py#L226) | 226 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-4397BC2CD2-L000227](../../tests/test_intent_router_integration.py#L227) | 227 | `"    monkeypatch.setattr(agent, \"_repair_answer_coverage\", lambda _q, answer, _s, _m: answer)"` | — |
| [SRC-4397BC2CD2-L000228](../../tests/test_intent_router_integration.py#L228) | 228 | `""` | — |
| [SRC-4397BC2CD2-L000229](../../tests/test_intent_router_integration.py#L229) | 229 | `"    agent.answer(question, history=[])"` | — |
| [SRC-4397BC2CD2-L000230](../../tests/test_intent_router_integration.py#L230) | 230 | `""` | — |
| [SRC-4397BC2CD2-L000231](../../tests/test_intent_router_integration.py#L231) | 231 | `"    # All eight explicit criteria consume the bounded initial query allowance;"` | — |
| [SRC-4397BC2CD2-L000232](../../tests/test_intent_router_integration.py#L232) | 232 | `"    # the system must not launch an unbudgeted ninth query for coverage repair."` | — |
| [SRC-4397BC2CD2-L000233](../../tests/test_intent_router_integration.py#L233) | 233 | `"    assert len(seen[\"plans\"]) == 1"` | — |
| [SRC-4397BC2CD2-L000234](../../tests/test_intent_router_integration.py#L234) | 234 | `"    targets = WebAgent._question_coverage_targets(question)"` | — |
| [SRC-4397BC2CD2-L000235](../../tests/test_intent_router_integration.py#L235) | 235 | `"    assert len(targets) == 8"` | — |
| [SRC-4397BC2CD2-L000236](../../tests/test_intent_router_integration.py#L236) | 236 | `"    initial_plan = seen[\"plans\"][0]"` | — |
| [SRC-4397BC2CD2-L000237](../../tests/test_intent_router_integration.py#L237) | 237 | `"    queries = initial_plan[\"queries\"]"` | — |
| [SRC-4397BC2CD2-L000238](../../tests/test_intent_router_integration.py#L238) | 238 | `"    assert initial_plan[\"coverage_gap_repair_slot_reserved\"] is False"` | — |
| [SRC-4397BC2CD2-L000239](../../tests/test_intent_router_integration.py#L239) | 239 | `"    assert initial_plan[\"query_limit\"] == 8"` | — |
| [SRC-4397BC2CD2-L000240](../../tests/test_intent_router_integration.py#L240) | 240 | `"    assert len(queries) == 8"` | — |
| [SRC-4397BC2CD2-L000241](../../tests/test_intent_router_integration.py#L241) | 241 | `"    for target in targets:"` | — |
| [SRC-4397BC2CD2-L000242](../../tests/test_intent_router_integration.py#L242) | 242 | `"        assert any(target in query for query in queries), f\"Missing criterion query for {target!r}\""` | — |
| [SRC-4397BC2CD2-L000243](../../tests/test_intent_router_integration.py#L243) | 243 | `""` | — |
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
| [SRC-62DC597310-L000215](../../tests/test_live_search_connectors.py#L215) | 215 | `"        request = httpx.Request(\"GET\", \"https://provider.example/slow\")"` | — |
| [SRC-62DC597310-L000216](../../tests/test_live_search_connectors.py#L216) | 216 | `"        headers = {}"` | — |
| [SRC-62DC597310-L000217](../../tests/test_live_search_connectors.py#L217) | 217 | `""` | — |
| [SRC-62DC597310-L000218](../../tests/test_live_search_connectors.py#L218) | 218 | `"        def __enter__(self):"` | — |
| [SRC-62DC597310-L000219](../../tests/test_live_search_connectors.py#L219) | 219 | `"            return self"` | — |
| [SRC-62DC597310-L000220](../../tests/test_live_search_connectors.py#L220) | 220 | `""` | — |
| [SRC-62DC597310-L000221](../../tests/test_live_search_connectors.py#L221) | 221 | `"        def __exit__(self, *_args):"` | — |
| [SRC-62DC597310-L000222](../../tests/test_live_search_connectors.py#L222) | 222 | `"            return False"` | — |
| [SRC-62DC597310-L000223](../../tests/test_live_search_connectors.py#L223) | 223 | `""` | — |
| [SRC-62DC597310-L000224](../../tests/test_live_search_connectors.py#L224) | 224 | `"        def iter_bytes(self):"` | — |
| [SRC-62DC597310-L000225](../../tests/test_live_search_connectors.py#L225) | 225 | `"            for chunk in (b\"first\", b\"second\"):"` | — |
| [SRC-62DC597310-L000226](../../tests/test_live_search_connectors.py#L226) | 226 | `"                chunks_read.append(chunk)"` | — |
| [SRC-62DC597310-L000227](../../tests/test_live_search_connectors.py#L227) | 227 | `"                yield chunk"` | — |
| [SRC-62DC597310-L000228](../../tests/test_live_search_connectors.py#L228) | 228 | `""` | — |
| [SRC-62DC597310-L000229](../../tests/test_live_search_connectors.py#L229) | 229 | `"    class FakeClient:"` | — |
| [SRC-62DC597310-L000230](../../tests/test_live_search_connectors.py#L230) | 230 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-62DC597310-L000231](../../tests/test_live_search_connectors.py#L231) | 231 | `"            assert kwargs[\"timeout\"] == 9.0"` | — |
| [SRC-62DC597310-L000232](../../tests/test_live_search_connectors.py#L232) | 232 | `"            assert kwargs[\"follow_redirects\"] is False"` | — |
| [SRC-62DC597310-L000233](../../tests/test_live_search_connectors.py#L233) | 233 | `""` | — |
| [SRC-62DC597310-L000234](../../tests/test_live_search_connectors.py#L234) | 234 | `"        def __enter__(self):"` | — |
| [SRC-62DC597310-L000235](../../tests/test_live_search_connectors.py#L235) | 235 | `"            return self"` | — |
| [SRC-62DC597310-L000236](../../tests/test_live_search_connectors.py#L236) | 236 | `""` | — |
| [SRC-62DC597310-L000237](../../tests/test_live_search_connectors.py#L237) | 237 | `"        def __exit__(self, *_args):"` | — |
| [SRC-62DC597310-L000238](../../tests/test_live_search_connectors.py#L238) | 238 | `"            return False"` | — |
| [SRC-62DC597310-L000239](../../tests/test_live_search_connectors.py#L239) | 239 | `""` | — |
| [SRC-62DC597310-L000240](../../tests/test_live_search_connectors.py#L240) | 240 | `"        def stream(self, method, url, **kwargs):"` | — |
| [SRC-62DC597310-L000241](../../tests/test_live_search_connectors.py#L241) | 241 | `"            assert method == \"GET\""` | — |
| [SRC-62DC597310-L000242](../../tests/test_live_search_connectors.py#L242) | 242 | `"            return FakeResponse()"` | — |
| [SRC-62DC597310-L000243](../../tests/test_live_search_connectors.py#L243) | 243 | `""` | — |
| [SRC-62DC597310-L000244](../../tests/test_live_search_connectors.py#L244) | 244 | `"    # Start at t=0; the first chunk arrives before the deadline."` | — |
| [SRC-62DC597310-L000245](../../tests/test_live_search_connectors.py#L245) | 245 | `"    # The deadline expires before requesting the second chunk."` | — |
| [SRC-62DC597310-L000246](../../tests/test_live_search_connectors.py#L246) | 246 | `"    clock = iter((0.0, 0.0, 2.0))"` | — |
| [SRC-62DC597310-L000247](../../tests/test_live_search_connectors.py#L247) | 247 | `"    monkeypatch.setattr(\"agents.web_agent.time.monotonic\", lambda: next(clock))"` | — |
| [SRC-62DC597310-L000248](../../tests/test_live_search_connectors.py#L248) | 248 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-62DC597310-L000249](../../tests/test_live_search_connectors.py#L249) | 249 | `""` | — |
| [SRC-62DC597310-L000250](../../tests/test_live_search_connectors.py#L250) | 250 | `"    with pytest.raises(TimeoutError, match=\"total request deadline\"):"` | — |
| [SRC-62DC597310-L000251](../../tests/test_live_search_connectors.py#L251) | 251 | `"        _bounded_http_request("` | — |
| [SRC-62DC597310-L000252](../../tests/test_live_search_connectors.py#L252) | 252 | `"            \"GET\","` | — |
| [SRC-62DC597310-L000253](../../tests/test_live_search_connectors.py#L253) | 253 | `"            \"https://provider.example/slow\","` | — |
| [SRC-62DC597310-L000254](../../tests/test_live_search_connectors.py#L254) | 254 | `"            timeout=9.0,"` | — |
| [SRC-62DC597310-L000255](../../tests/test_live_search_connectors.py#L255) | 255 | `"            total_timeout=1.5,"` | — |
| [SRC-62DC597310-L000256](../../tests/test_live_search_connectors.py#L256) | 256 | `"        )"` | — |
| [SRC-62DC597310-L000257](../../tests/test_live_search_connectors.py#L257) | 257 | `""` | — |
| [SRC-62DC597310-L000258](../../tests/test_live_search_connectors.py#L258) | 258 | `"    assert chunks_read == [b\"first\"]"` | — |
| [SRC-62DC597310-L000259](../../tests/test_live_search_connectors.py#L259) | 259 | `""` | — |
| [SRC-62DC597310-L000260](../../tests/test_live_search_connectors.py#L260) | 260 | `""` | — |
| [SRC-62DC597310-L000261](../../tests/test_live_search_connectors.py#L261) | 261 | `"@pytest.mark.parametrize(\"total_timeout\", [0, -1, float(\"inf\"), \"not-a-number\"])"` | — |
| [SRC-62DC597310-L000262](../../tests/test_live_search_connectors.py#L262) | 262 | `"def test_bounded_provider_transport_rejects_invalid_total_deadlines(total_timeout):"` | — |
| [SRC-62DC597310-L000263](../../tests/test_live_search_connectors.py#L263) | 263 | `"    with pytest.raises(ValueError, match=\"total_timeout\"):"` | — |
| [SRC-62DC597310-L000264](../../tests/test_live_search_connectors.py#L264) | 264 | `"        _bounded_http_request("` | — |
| [SRC-62DC597310-L000265](../../tests/test_live_search_connectors.py#L265) | 265 | `"            \"GET\","` | — |
| [SRC-62DC597310-L000266](../../tests/test_live_search_connectors.py#L266) | 266 | `"            \"https://provider.example/search\","` | — |
| [SRC-62DC597310-L000267](../../tests/test_live_search_connectors.py#L267) | 267 | `"            total_timeout=total_timeout,"` | — |
| [SRC-62DC597310-L000268](../../tests/test_live_search_connectors.py#L268) | 268 | `"        )"` | — |
