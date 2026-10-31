# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **042**
- سجلات الأسطر: **800**
- النطاق: SRC-EA6EC52573-L000179 إلى SRC-4405E7912C-L000138
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-EA6EC52573 — [tests/test_intent_router.py](../../tests/test_intent_router.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-1521F490CA-L000077](../../tests/test_multitenant.py#L77) | 77 | `""` | — |
| [SRC-1521F490CA-L000078](../../tests/test_multitenant.py#L78) | 78 | `"    with store.connect() as db:"` | — |
| [SRC-1521F490CA-L000079](../../tests/test_multitenant.py#L79) | 79 | `"        db.execute("` | — |
| [SRC-1521F490CA-L000080](../../tests/test_multitenant.py#L80) | 80 | `"            \"UPDATE tenant_memberships SET active=0 WHERE tenant_id=? AND user_id=?\","` | — |
| [SRC-1521F490CA-L000081](../../tests/test_multitenant.py#L81) | 81 | `"            (tenant_id, user_id),"` | — |
| [SRC-1521F490CA-L000082](../../tests/test_multitenant.py#L82) | 82 | `"        )"` | — |
| [SRC-1521F490CA-L000083](../../tests/test_multitenant.py#L83) | 83 | `"    assert store.resolve_api_token(\"C\" * 40) is None"` | — |
| [SRC-1521F490CA-L000084](../../tests/test_multitenant.py#L84) | 84 | `""` | — |
| [SRC-1521F490CA-L000085](../../tests/test_multitenant.py#L85) | 85 | `""` | — |
| [SRC-1521F490CA-L000086](../../tests/test_multitenant.py#L86) | 86 | `"def test_legacy_single_company_database_migrates_without_losing_leads(tmp_path):"` | — |
| [SRC-1521F490CA-L000087](../../tests/test_multitenant.py#L87) | 87 | `"    path = tmp_path / \"legacy.sqlite3\""` | — |
| [SRC-1521F490CA-L000088](../../tests/test_multitenant.py#L88) | 88 | `"    legacy_text = \"Old lead\""` | — |
| [SRC-1521F490CA-L000089](../../tests/test_multitenant.py#L89) | 89 | `"    legacy_url = \"https://example.test/legacy\""` | — |
| [SRC-1521F490CA-L000090](../../tests/test_multitenant.py#L90) | 90 | `"    legacy_fingerprint = hashlib.sha256("` | — |
| [SRC-1521F490CA-L000091](../../tests/test_multitenant.py#L91) | 91 | `"        (legacy_url.rstrip(\"/\") + \"\\n\" + normalize(legacy_text)).encode()"` | — |
| [SRC-1521F490CA-L000092](../../tests/test_multitenant.py#L92) | 92 | `"    ).hexdigest()"` | — |
| [SRC-1521F490CA-L000093](../../tests/test_multitenant.py#L93) | 93 | `"    with sqlite3.connect(path) as db:"` | — |
| [SRC-1521F490CA-L000094](../../tests/test_multitenant.py#L94) | 94 | `"        db.execute("` | — |
| [SRC-1521F490CA-L000095](../../tests/test_multitenant.py#L95) | 95 | `"            \"\"\"CREATE TABLE leads ("` | — |
| [SRC-1521F490CA-L000096](../../tests/test_multitenant.py#L96) | 96 | `"                id TEXT PRIMARY KEY,"` | — |
| [SRC-1521F490CA-L000097](../../tests/test_multitenant.py#L97) | 97 | `"                fingerprint TEXT UNIQUE NOT NULL,"` | — |
| [SRC-1521F490CA-L000098](../../tests/test_multitenant.py#L98) | 98 | `"                text TEXT NOT NULL,"` | — |
| [SRC-1521F490CA-L000099](../../tests/test_multitenant.py#L99) | 99 | `"                source_url TEXT NOT NULL,"` | — |
| [SRC-1521F490CA-L000100](../../tests/test_multitenant.py#L100) | 100 | `"                platform TEXT NOT NULL,"` | — |
| [SRC-1521F490CA-L000101](../../tests/test_multitenant.py#L101) | 101 | `"                observed_at TEXT NOT NULL,"` | — |
| [SRC-1521F490CA-L000102](../../tests/test_multitenant.py#L102) | 102 | `"                assessment TEXT NOT NULL,"` | — |
| [SRC-1521F490CA-L000103](../../tests/test_multitenant.py#L103) | 103 | `"                status TEXT NOT NULL,"` | — |
| [SRC-1521F490CA-L000104](../../tests/test_multitenant.py#L104) | 104 | `"                note TEXT NOT NULL,"` | — |
| [SRC-1521F490CA-L000105](../../tests/test_multitenant.py#L105) | 105 | `"                created_at TEXT NOT NULL,"` | — |
| [SRC-1521F490CA-L000106](../../tests/test_multitenant.py#L106) | 106 | `"                updated_at TEXT NOT NULL"` | — |
| [SRC-1521F490CA-L000107](../../tests/test_multitenant.py#L107) | 107 | `"            )\"\"\""` | — |
| [SRC-1521F490CA-L000108](../../tests/test_multitenant.py#L108) | 108 | `"        )"` | — |
| [SRC-1521F490CA-L000109](../../tests/test_multitenant.py#L109) | 109 | `"        db.execute("` | — |
| [SRC-1521F490CA-L000110](../../tests/test_multitenant.py#L110) | 110 | `"            \"\"\"INSERT INTO leads VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)\"\"\","` | — |
| [SRC-1521F490CA-L000111](../../tests/test_multitenant.py#L111) | 111 | `"            ("` | — |
| [SRC-1521F490CA-L000112](../../tests/test_multitenant.py#L112) | 112 | `"                \"legacy-lead\", legacy_fingerprint, legacy_text,"` | — |
| [SRC-1521F490CA-L000113](../../tests/test_multitenant.py#L113) | 113 | `"                legacy_url, \"manual\", \"2026-10-30T00:00:00Z\","` | — |
| [SRC-1521F490CA-L000114](../../tests/test_multitenant.py#L114) | 114 | `"                '{\"score\": 0}', \"new\", \"\", \"2026-10-30T00:00:00Z\","` | — |
| [SRC-1521F490CA-L000115](../../tests/test_multitenant.py#L115) | 115 | `"                \"2026-10-30T00:00:00Z\","` | — |
| [SRC-1521F490CA-L000116](../../tests/test_multitenant.py#L116) | 116 | `"            ),"` | — |
| [SRC-1521F490CA-L000117](../../tests/test_multitenant.py#L117) | 117 | `"        )"` | — |
| [SRC-1521F490CA-L000118](../../tests/test_multitenant.py#L118) | 118 | `""` | — |
| [SRC-1521F490CA-L000119](../../tests/test_multitenant.py#L119) | 119 | `"    store = LeadStore(path)"` | — |
| [SRC-1521F490CA-L000120](../../tests/test_multitenant.py#L120) | 120 | `"    leads = store.list(tenant_id=DEFAULT_TENANT_ID)"` | — |
| [SRC-1521F490CA-L000121](../../tests/test_multitenant.py#L121) | 121 | `"    assert len(leads) == 1"` | — |
| [SRC-1521F490CA-L000122](../../tests/test_multitenant.py#L122) | 122 | `"    assert leads[0][\"id\"] == \"legacy-lead\""` | — |
| [SRC-1521F490CA-L000123](../../tests/test_multitenant.py#L123) | 123 | `"    assert leads[0][\"tenant_id\"] == DEFAULT_TENANT_ID"` | — |
| [SRC-1521F490CA-L000124](../../tests/test_multitenant.py#L124) | 124 | `""` | — |
| [SRC-1521F490CA-L000125](../../tests/test_multitenant.py#L125) | 125 | `"    duplicate, created = store.add("` | — |
| [SRC-1521F490CA-L000126](../../tests/test_multitenant.py#L126) | 126 | `"        \"Old lead\", \"https://example.test/legacy\", tenant_id=DEFAULT_TENANT_ID"` | — |
| [SRC-1521F490CA-L000127](../../tests/test_multitenant.py#L127) | 127 | `"    )"` | — |
| [SRC-1521F490CA-L000128](../../tests/test_multitenant.py#L128) | 128 | `"    assert created is False"` | — |
| [SRC-1521F490CA-L000129](../../tests/test_multitenant.py#L129) | 129 | `"    assert duplicate[\"id\"] == \"legacy-lead\""` | — |
| [SRC-1521F490CA-L000130](../../tests/test_multitenant.py#L130) | 130 | `""` | — |
| [SRC-1521F490CA-L000131](../../tests/test_multitenant.py#L131) | 131 | `"    with store.connect() as db:"` | — |
| [SRC-1521F490CA-L000132](../../tests/test_multitenant.py#L132) | 132 | `"        columns = {row[\"name\"] for row in db.execute(\"PRAGMA table_info(leads)\")}"` | — |
| [SRC-1521F490CA-L000133](../../tests/test_multitenant.py#L133) | 133 | `"        unique_indexes = ["` | — |
| [SRC-1521F490CA-L000134](../../tests/test_multitenant.py#L134) | 134 | `"            row[\"name\"] for row in db.execute(\"PRAGMA index_list(leads)\")"` | — |
| [SRC-1521F490CA-L000135](../../tests/test_multitenant.py#L135) | 135 | `"            if row[\"unique\"]"` | — |
| [SRC-1521F490CA-L000136](../../tests/test_multitenant.py#L136) | 136 | `"        ]"` | — |
| [SRC-1521F490CA-L000137](../../tests/test_multitenant.py#L137) | 137 | `"        unique_columns = ["` | — |
| [SRC-1521F490CA-L000138](../../tests/test_multitenant.py#L138) | 138 | `"            ["` | — |
| [SRC-1521F490CA-L000139](../../tests/test_multitenant.py#L139) | 139 | `"                item[\"name\"]"` | — |
| [SRC-1521F490CA-L000140](../../tests/test_multitenant.py#L140) | 140 | `"                for item in db.execute(f\"PRAGMA index_info('{index_name}')\")"` | — |
| [SRC-1521F490CA-L000141](../../tests/test_multitenant.py#L141) | 141 | `"            ]"` | — |
| [SRC-1521F490CA-L000142](../../tests/test_multitenant.py#L142) | 142 | `"            for index_name in unique_indexes"` | — |
| [SRC-1521F490CA-L000143](../../tests/test_multitenant.py#L143) | 143 | `"        ]"` | — |
| [SRC-1521F490CA-L000144](../../tests/test_multitenant.py#L144) | 144 | `"    assert \"tenant_id\" in columns"` | — |
| [SRC-1521F490CA-L000145](../../tests/test_multitenant.py#L145) | 145 | `"    assert [\"fingerprint\"] not in unique_columns"` | — |
| [SRC-1521F490CA-L000146](../../tests/test_multitenant.py#L146) | 146 | `"    assert [\"tenant_id\", \"fingerprint\"] in unique_columns"` | — |
| [SRC-1521F490CA-L000147](../../tests/test_multitenant.py#L147) | 147 | `""` | — |
| [SRC-1521F490CA-L000148](../../tests/test_multitenant.py#L148) | 148 | `""` | — |
| [SRC-1521F490CA-L000149](../../tests/test_multitenant.py#L149) | 149 | `""` | — |
| [SRC-1521F490CA-L000150](../../tests/test_multitenant.py#L150) | 150 | `"def test_legacy_migration_rolls_back_and_keeps_original_table_on_copy_error(tmp_path):"` | — |
| [SRC-1521F490CA-L000151](../../tests/test_multitenant.py#L151) | 151 | `"    path = tmp_path / \"incomplete-legacy.sqlite3\""` | — |
| [SRC-1521F490CA-L000152](../../tests/test_multitenant.py#L152) | 152 | `"    with sqlite3.connect(path) as db:"` | — |
| [SRC-1521F490CA-L000153](../../tests/test_multitenant.py#L153) | 153 | `"        db.execute("` | — |
| [SRC-1521F490CA-L000154](../../tests/test_multitenant.py#L154) | 154 | `"            \"CREATE TABLE leads (id TEXT PRIMARY KEY, fingerprint TEXT UNIQUE NOT NULL, text TEXT NOT NULL)\""` | — |
| [SRC-1521F490CA-L000155](../../tests/test_multitenant.py#L155) | 155 | `"        )"` | — |
| [SRC-1521F490CA-L000156](../../tests/test_multitenant.py#L156) | 156 | `"        db.execute("` | — |
| [SRC-1521F490CA-L000157](../../tests/test_multitenant.py#L157) | 157 | `"            \"INSERT INTO leads (id, fingerprint, text) VALUES (?, ?, ?)\","` | — |
| [SRC-1521F490CA-L000158](../../tests/test_multitenant.py#L158) | 158 | `"            (\"legacy-1\", \"fingerprint-1\", \"preserve me\"),"` | — |
| [SRC-1521F490CA-L000159](../../tests/test_multitenant.py#L159) | 159 | `"        )"` | — |
| [SRC-1521F490CA-L000160](../../tests/test_multitenant.py#L160) | 160 | `""` | — |
| [SRC-1521F490CA-L000161](../../tests/test_multitenant.py#L161) | 161 | `"    import pytest"` | — |
| [SRC-1521F490CA-L000162](../../tests/test_multitenant.py#L162) | 162 | `""` | — |
| [SRC-1521F490CA-L000163](../../tests/test_multitenant.py#L163) | 163 | `"    with pytest.raises(sqlite3.OperationalError):"` | — |
| [SRC-1521F490CA-L000164](../../tests/test_multitenant.py#L164) | 164 | `"        LeadStore(path)"` | — |
| [SRC-1521F490CA-L000165](../../tests/test_multitenant.py#L165) | 165 | `""` | — |
| [SRC-1521F490CA-L000166](../../tests/test_multitenant.py#L166) | 166 | `"    with sqlite3.connect(path) as db:"` | — |
| [SRC-1521F490CA-L000167](../../tests/test_multitenant.py#L167) | 167 | `"        tables = {"` | — |
| [SRC-1521F490CA-L000168](../../tests/test_multitenant.py#L168) | 168 | `"            row[0]"` | — |
| [SRC-1521F490CA-L000169](../../tests/test_multitenant.py#L169) | 169 | `"            for row in db.execute("` | — |
| [SRC-1521F490CA-L000170](../../tests/test_multitenant.py#L170) | 170 | `"                \"SELECT name FROM sqlite_master WHERE type='table'\""` | — |
| [SRC-1521F490CA-L000171](../../tests/test_multitenant.py#L171) | 171 | `"            )"` | — |
| [SRC-1521F490CA-L000172](../../tests/test_multitenant.py#L172) | 172 | `"        }"` | — |
| [SRC-1521F490CA-L000173](../../tests/test_multitenant.py#L173) | 173 | `"        original = db.execute("` | — |
| [SRC-1521F490CA-L000174](../../tests/test_multitenant.py#L174) | 174 | `"            \"SELECT id, fingerprint, text FROM leads\""` | — |
| [SRC-1521F490CA-L000175](../../tests/test_multitenant.py#L175) | 175 | `"        ).fetchone()"` | — |
| [SRC-1521F490CA-L000176](../../tests/test_multitenant.py#L176) | 176 | `"    assert \"leads\" in tables"` | — |
| [SRC-1521F490CA-L000177](../../tests/test_multitenant.py#L177) | 177 | `"    assert \"leads_legacy_migration\" not in tables"` | — |
| [SRC-1521F490CA-L000178](../../tests/test_multitenant.py#L178) | 178 | `"    assert original == (\"legacy-1\", \"fingerprint-1\", \"preserve me\")"` | — |
| [SRC-1521F490CA-L000179](../../tests/test_multitenant.py#L179) | 179 | `""` | — |
| [SRC-1521F490CA-L000180](../../tests/test_multitenant.py#L180) | 180 | `""` | — |
| [SRC-1521F490CA-L000181](../../tests/test_multitenant.py#L181) | 181 | `"def test_api_token_expiry_is_normalized_to_utc(tmp_path):"` | — |
| [SRC-1521F490CA-L000182](../../tests/test_multitenant.py#L182) | 182 | `"    store = LeadStore(tmp_path / \"token-expiry.sqlite3\")"` | — |
| [SRC-1521F490CA-L000183](../../tests/test_multitenant.py#L183) | 183 | `"    tenant_id, user_id = _tenant_member("` | — |
| [SRC-1521F490CA-L000184](../../tests/test_multitenant.py#L184) | 184 | `"        store, \"Expiry Company\", \"expiry@example.test\", \"E\" * 40"` | — |
| [SRC-1521F490CA-L000185](../../tests/test_multitenant.py#L185) | 185 | `"    )"` | — |
| [SRC-1521F490CA-L000186](../../tests/test_multitenant.py#L186) | 186 | `"    token = \"F\" * 40"` | — |
| [SRC-1521F490CA-L000187](../../tests/test_multitenant.py#L187) | 187 | `"    store.create_api_token("` | — |
| [SRC-1521F490CA-L000188](../../tests/test_multitenant.py#L188) | 188 | `"        token,"` | — |
| [SRC-1521F490CA-L000189](../../tests/test_multitenant.py#L189) | 189 | `"        tenant_id,"` | — |
| [SRC-1521F490CA-L000190](../../tests/test_multitenant.py#L190) | 190 | `"        user_id,"` | — |
| [SRC-1521F490CA-L000191](../../tests/test_multitenant.py#L191) | 191 | `"        expires_at=\"2099-01-01T03:00:00+03:00\","` | — |
| [SRC-1521F490CA-L000192](../../tests/test_multitenant.py#L192) | 192 | `"    )"` | — |
| [SRC-1521F490CA-L000193](../../tests/test_multitenant.py#L193) | 193 | `"    with store.connect() as db:"` | — |
| [SRC-1521F490CA-L000194](../../tests/test_multitenant.py#L194) | 194 | `"        row = db.execute("` | — |
| [SRC-1521F490CA-L000195](../../tests/test_multitenant.py#L195) | 195 | `"            \"SELECT expires_at FROM api_tokens WHERE token_hash=?\","` | — |
| [SRC-1521F490CA-L000196](../../tests/test_multitenant.py#L196) | 196 | `"            (store._token_hash(token),),"` | — |
| [SRC-1521F490CA-L000197](../../tests/test_multitenant.py#L197) | 197 | `"        ).fetchone()"` | — |
| [SRC-1521F490CA-L000198](../../tests/test_multitenant.py#L198) | 198 | `"    assert row[\"expires_at\"] == \"2099-01-01T00:00:00Z\""` | — |
| [SRC-1521F490CA-L000199](../../tests/test_multitenant.py#L199) | 199 | `"    assert store.resolve_api_token(token) is not None"` | — |
| [SRC-1521F490CA-L000200](../../tests/test_multitenant.py#L200) | 200 | `""` | — |
| [SRC-1521F490CA-L000201](../../tests/test_multitenant.py#L201) | 201 | `"    # Expired tokens must stop resolving even when their membership stays active."` | — |
| [SRC-1521F490CA-L000202](../../tests/test_multitenant.py#L202) | 202 | `"    with store.connect() as db:"` | — |
| [SRC-1521F490CA-L000203](../../tests/test_multitenant.py#L203) | 203 | `"        db.execute("` | — |
| [SRC-1521F490CA-L000204](../../tests/test_multitenant.py#L204) | 204 | `"            \"UPDATE api_tokens SET expires_at=? WHERE token_hash=?\","` | — |
| [SRC-1521F490CA-L000205](../../tests/test_multitenant.py#L205) | 205 | `"            (\"2000-01-01T00:00:00Z\", store._token_hash(token)),"` | — |
| [SRC-1521F490CA-L000206](../../tests/test_multitenant.py#L206) | 206 | `"        )"` | — |
| [SRC-1521F490CA-L000207](../../tests/test_multitenant.py#L207) | 207 | `"    assert store.resolve_api_token(token) is None"` | — |
| [SRC-1521F490CA-L000208](../../tests/test_multitenant.py#L208) | 208 | `""` | — |
| [SRC-1521F490CA-L000209](../../tests/test_multitenant.py#L209) | 209 | `"    utc_token = \"J\" * 40"` | — |
| [SRC-1521F490CA-L000210](../../tests/test_multitenant.py#L210) | 210 | `"    store.create_api_token("` | — |
| [SRC-1521F490CA-L000211](../../tests/test_multitenant.py#L211) | 211 | `"        utc_token, tenant_id, user_id, expires_at=\"2099-01-01T00:00:00Z\""` | — |
| [SRC-1521F490CA-L000212](../../tests/test_multitenant.py#L212) | 212 | `"    )"` | — |
| [SRC-1521F490CA-L000213](../../tests/test_multitenant.py#L213) | 213 | `"    assert store.resolve_api_token(utc_token) is not None"` | — |
| [SRC-1521F490CA-L000214](../../tests/test_multitenant.py#L214) | 214 | `""` | — |
| [SRC-1521F490CA-L000215](../../tests/test_multitenant.py#L215) | 215 | `""` | — |
| [SRC-1521F490CA-L000216](../../tests/test_multitenant.py#L216) | 216 | `"def test_api_token_expiry_rejects_naive_malformed_and_past_values(tmp_path):"` | — |
| [SRC-1521F490CA-L000217](../../tests/test_multitenant.py#L217) | 217 | `"    store = LeadStore(tmp_path / \"invalid-token-expiry.sqlite3\")"` | — |
| [SRC-1521F490CA-L000218](../../tests/test_multitenant.py#L218) | 218 | `"    tenant_id, user_id = _tenant_member("` | — |
| [SRC-1521F490CA-L000219](../../tests/test_multitenant.py#L219) | 219 | `"        store, \"Expiry Validation Company\", \"expiry-validation@example.test\", \"G\" * 40"` | — |
| [SRC-1521F490CA-L000220](../../tests/test_multitenant.py#L220) | 220 | `"    )"` | — |
| [SRC-1521F490CA-L000221](../../tests/test_multitenant.py#L221) | 221 | `"    invalid_values = ("` | — |
| [SRC-1521F490CA-L000222](../../tests/test_multitenant.py#L222) | 222 | `"        \"2099-01-01T00:00:00\","` | — |
| [SRC-1521F490CA-L000223](../../tests/test_multitenant.py#L223) | 223 | `"        \"not-a-timestamp\","` | — |
| [SRC-1521F490CA-L000224](../../tests/test_multitenant.py#L224) | 224 | `"        \"2000-01-01T00:00:00Z\","` | — |
| [SRC-1521F490CA-L000225](../../tests/test_multitenant.py#L225) | 225 | `"        \"\","` | — |
| [SRC-1521F490CA-L000226](../../tests/test_multitenant.py#L226) | 226 | `"    )"` | — |
| [SRC-1521F490CA-L000227](../../tests/test_multitenant.py#L227) | 227 | `"    for index, expiry in enumerate(invalid_values):"` | — |
| [SRC-1521F490CA-L000228](../../tests/test_multitenant.py#L228) | 228 | `"        with pytest.raises(ValueError, match=\"expires_at\"):"` | — |
| [SRC-1521F490CA-L000229](../../tests/test_multitenant.py#L229) | 229 | `"            store.create_api_token("` | — |
| [SRC-1521F490CA-L000230](../../tests/test_multitenant.py#L230) | 230 | `"                (\"H\" * 39) + str(index),"` | — |
| [SRC-1521F490CA-L000231](../../tests/test_multitenant.py#L231) | 231 | `"                tenant_id,"` | — |
| [SRC-1521F490CA-L000232](../../tests/test_multitenant.py#L232) | 232 | `"                user_id,"` | — |
| [SRC-1521F490CA-L000233](../../tests/test_multitenant.py#L233) | 233 | `"                expires_at=expiry,"` | — |
| [SRC-1521F490CA-L000234](../../tests/test_multitenant.py#L234) | 234 | `"            )"` | — |
## اختبارات

### FILE-4405E7912C — [tests/test_multitenant_api.py](../../tests/test_multitenant_api.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-4405E7912C-L000001](../../tests/test_multitenant_api.py#L1) | 1 | `"\"\"\"HTTP-level tenant authorization regression tests.\"\"\""` | — |
| [SRC-4405E7912C-L000002](../../tests/test_multitenant_api.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-4405E7912C-L000003](../../tests/test_multitenant_api.py#L3) | 3 | `""` | — |
| [SRC-4405E7912C-L000004](../../tests/test_multitenant_api.py#L4) | 4 | `"import json"` | — |
| [SRC-4405E7912C-L000005](../../tests/test_multitenant_api.py#L5) | 5 | `"import threading"` | — |
| [SRC-4405E7912C-L000006](../../tests/test_multitenant_api.py#L6) | 6 | `"from http.server import ThreadingHTTPServer"` | — |
| [SRC-4405E7912C-L000007](../../tests/test_multitenant_api.py#L7) | 7 | `"from urllib.error import HTTPError"` | — |
| [SRC-4405E7912C-L000008](../../tests/test_multitenant_api.py#L8) | 8 | `"from urllib.request import Request, urlopen"` | — |
| [SRC-4405E7912C-L000009](../../tests/test_multitenant_api.py#L9) | 9 | `""` | — |
| [SRC-4405E7912C-L000010](../../tests/test_multitenant_api.py#L10) | 10 | `"import pytest"` | — |
| [SRC-4405E7912C-L000011](../../tests/test_multitenant_api.py#L11) | 11 | `""` | — |
| [SRC-4405E7912C-L000012](../../tests/test_multitenant_api.py#L12) | 12 | `"from agents.omarai import LeadStore"` | — |
| [SRC-4405E7912C-L000013](../../tests/test_multitenant_api.py#L13) | 13 | `"from api.omarai import Handler"` | — |
| [SRC-4405E7912C-L000014](../../tests/test_multitenant_api.py#L14) | 14 | `""` | — |
| [SRC-4405E7912C-L000015](../../tests/test_multitenant_api.py#L15) | 15 | `""` | — |
| [SRC-4405E7912C-L000016](../../tests/test_multitenant_api.py#L16) | 16 | `"@pytest.fixture"` | — |
| [SRC-4405E7912C-L000017](../../tests/test_multitenant_api.py#L17) | 17 | `"def tenant_api(tmp_path, monkeypatch):"` | — |
| [SRC-4405E7912C-L000018](../../tests/test_multitenant_api.py#L18) | 18 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-4405E7912C-L000019](../../tests/test_multitenant_api.py#L19) | 19 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-4405E7912C-L000020](../../tests/test_multitenant_api.py#L20) | 20 | `"    previous_store = Handler.store"` | — |
| [SRC-4405E7912C-L000021](../../tests/test_multitenant_api.py#L21) | 21 | `"    Handler.store = LeadStore(tmp_path / \"tenant-api.sqlite3\")"` | — |
| [SRC-4405E7912C-L000022](../../tests/test_multitenant_api.py#L22) | 22 | `"    server = ThreadingHTTPServer((\"127.0.0.1\", 0), Handler)"` | — |
| [SRC-4405E7912C-L000023](../../tests/test_multitenant_api.py#L23) | 23 | `"    thread = threading.Thread(target=server.serve_forever, daemon=True)"` | — |
| [SRC-4405E7912C-L000024](../../tests/test_multitenant_api.py#L24) | 24 | `"    thread.start()"` | — |
| [SRC-4405E7912C-L000025](../../tests/test_multitenant_api.py#L25) | 25 | `"    try:"` | — |
| [SRC-4405E7912C-L000026](../../tests/test_multitenant_api.py#L26) | 26 | `"        yield f\"http://127.0.0.1:{server.server_port}\", Handler.store"` | — |
| [SRC-4405E7912C-L000027](../../tests/test_multitenant_api.py#L27) | 27 | `"    finally:"` | — |
| [SRC-4405E7912C-L000028](../../tests/test_multitenant_api.py#L28) | 28 | `"        server.shutdown()"` | — |
| [SRC-4405E7912C-L000029](../../tests/test_multitenant_api.py#L29) | 29 | `"        server.server_close()"` | — |
| [SRC-4405E7912C-L000030](../../tests/test_multitenant_api.py#L30) | 30 | `"        thread.join(timeout=3)"` | — |
| [SRC-4405E7912C-L000031](../../tests/test_multitenant_api.py#L31) | 31 | `"        Handler.store = previous_store"` | — |
| [SRC-4405E7912C-L000032](../../tests/test_multitenant_api.py#L32) | 32 | `""` | — |
| [SRC-4405E7912C-L000033](../../tests/test_multitenant_api.py#L33) | 33 | `""` | — |
| [SRC-4405E7912C-L000034](../../tests/test_multitenant_api.py#L34) | 34 | `"def request_json(base, path, *, method=\"GET\", payload=None, token=\"\"):"` | — |
| [SRC-4405E7912C-L000035](../../tests/test_multitenant_api.py#L35) | 35 | `"    body = None if payload is None else json.dumps(payload).encode(\"utf-8\")"` | — |
| [SRC-4405E7912C-L000036](../../tests/test_multitenant_api.py#L36) | 36 | `"    headers = {}"` | — |
| [SRC-4405E7912C-L000037](../../tests/test_multitenant_api.py#L37) | 37 | `"    if body is not None:"` | — |
| [SRC-4405E7912C-L000038](../../tests/test_multitenant_api.py#L38) | 38 | `"        headers[\"Content-Type\"] = \"application/json\""` | — |
| [SRC-4405E7912C-L000039](../../tests/test_multitenant_api.py#L39) | 39 | `"    if token:"` | — |
| [SRC-4405E7912C-L000040](../../tests/test_multitenant_api.py#L40) | 40 | `"        headers[\"Authorization\"] = \"Bearer \" + token"` | — |
| [SRC-4405E7912C-L000041](../../tests/test_multitenant_api.py#L41) | 41 | `"    request = Request(base + path, data=body, method=method, headers=headers)"` | — |
| [SRC-4405E7912C-L000042](../../tests/test_multitenant_api.py#L42) | 42 | `"    try:"` | — |
| [SRC-4405E7912C-L000043](../../tests/test_multitenant_api.py#L43) | 43 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-4405E7912C-L000044](../../tests/test_multitenant_api.py#L44) | 44 | `"            return response.status, json.loads(response.read().decode(\"utf-8\"))"` | — |
| [SRC-4405E7912C-L000045](../../tests/test_multitenant_api.py#L45) | 45 | `"    except HTTPError as error:"` | — |
| [SRC-4405E7912C-L000046](../../tests/test_multitenant_api.py#L46) | 46 | `"        return error.code, json.loads(error.read().decode(\"utf-8\"))"` | — |
| [SRC-4405E7912C-L000047](../../tests/test_multitenant_api.py#L47) | 47 | `""` | — |
| [SRC-4405E7912C-L000048](../../tests/test_multitenant_api.py#L48) | 48 | `""` | — |
| [SRC-4405E7912C-L000049](../../tests/test_multitenant_api.py#L49) | 49 | `"def _tenant(store, name, email, token):"` | — |
| [SRC-4405E7912C-L000050](../../tests/test_multitenant_api.py#L50) | 50 | `"    tenant_id = store.create_tenant(name, name.casefold())"` | — |
| [SRC-4405E7912C-L000051](../../tests/test_multitenant_api.py#L51) | 51 | `"    user_id = store.create_user(email, name + \" User\")"` | — |
| [SRC-4405E7912C-L000052](../../tests/test_multitenant_api.py#L52) | 52 | `"    store.add_membership(tenant_id, user_id, \"sales_agent\")"` | — |
| [SRC-4405E7912C-L000053](../../tests/test_multitenant_api.py#L53) | 53 | `"    store.create_api_token(token, tenant_id, user_id, label=name)"` | — |
| [SRC-4405E7912C-L000054](../../tests/test_multitenant_api.py#L54) | 54 | `"    return tenant_id"` | — |
| [SRC-4405E7912C-L000055](../../tests/test_multitenant_api.py#L55) | 55 | `""` | — |
| [SRC-4405E7912C-L000056](../../tests/test_multitenant_api.py#L56) | 56 | `""` | — |
| [SRC-4405E7912C-L000057](../../tests/test_multitenant_api.py#L57) | 57 | `"def test_api_ignores_client_tenant_id_and_blocks_cross_tenant_reads_and_updates(tenant_api):"` | — |
| [SRC-4405E7912C-L000058](../../tests/test_multitenant_api.py#L58) | 58 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000059](../../tests/test_multitenant_api.py#L59) | 59 | `"    token_a = \"tenant-a-token-\" + \"A\" * 32"` | — |
| [SRC-4405E7912C-L000060](../../tests/test_multitenant_api.py#L60) | 60 | `"    token_b = \"tenant-b-token-\" + \"B\" * 32"` | — |
| [SRC-4405E7912C-L000061](../../tests/test_multitenant_api.py#L61) | 61 | `"    tenant_a = _tenant(store, \"Company A\", \"api-a@example.test\", token_a)"` | — |
| [SRC-4405E7912C-L000062](../../tests/test_multitenant_api.py#L62) | 62 | `"    tenant_b = _tenant(store, \"Company B\", \"api-b@example.test\", token_b)"` | — |
| [SRC-4405E7912C-L000063](../../tests/test_multitenant_api.py#L63) | 63 | `""` | — |
| [SRC-4405E7912C-L000064](../../tests/test_multitenant_api.py#L64) | 64 | `"    status, created_a = request_json("` | — |
| [SRC-4405E7912C-L000065](../../tests/test_multitenant_api.py#L65) | 65 | `"        base,"` | — |
| [SRC-4405E7912C-L000066](../../tests/test_multitenant_api.py#L66) | 66 | `"        \"/api/leads\","` | — |
| [SRC-4405E7912C-L000067](../../tests/test_multitenant_api.py#L67) | 67 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000068](../../tests/test_multitenant_api.py#L68) | 68 | `"        token=token_a,"` | — |
| [SRC-4405E7912C-L000069](../../tests/test_multitenant_api.py#L69) | 69 | `"        payload={"` | — |
| [SRC-4405E7912C-L000070](../../tests/test_multitenant_api.py#L70) | 70 | `"            \"tenant_id\": tenant_b,"` | — |
| [SRC-4405E7912C-L000071](../../tests/test_multitenant_api.py#L71) | 71 | `"            \"text\": \"Buyer A wants to purchase\","` | — |
| [SRC-4405E7912C-L000072](../../tests/test_multitenant_api.py#L72) | 72 | `"            \"source_url\": \"https://example.test/a\","` | — |
| [SRC-4405E7912C-L000073](../../tests/test_multitenant_api.py#L73) | 73 | `"            \"platform\": \"public\","` | — |
| [SRC-4405E7912C-L000074](../../tests/test_multitenant_api.py#L74) | 74 | `"        },"` | — |
| [SRC-4405E7912C-L000075](../../tests/test_multitenant_api.py#L75) | 75 | `"    )"` | — |
| [SRC-4405E7912C-L000076](../../tests/test_multitenant_api.py#L76) | 76 | `"    assert status == 201"` | — |
| [SRC-4405E7912C-L000077](../../tests/test_multitenant_api.py#L77) | 77 | `"    assert created_a[\"lead\"][\"tenant_id\"] == tenant_a"` | — |
| [SRC-4405E7912C-L000078](../../tests/test_multitenant_api.py#L78) | 78 | `""` | — |
| [SRC-4405E7912C-L000079](../../tests/test_multitenant_api.py#L79) | 79 | `"    status, created_b = request_json("` | — |
| [SRC-4405E7912C-L000080](../../tests/test_multitenant_api.py#L80) | 80 | `"        base,"` | — |
| [SRC-4405E7912C-L000081](../../tests/test_multitenant_api.py#L81) | 81 | `"        \"/api/leads\","` | — |
| [SRC-4405E7912C-L000082](../../tests/test_multitenant_api.py#L82) | 82 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000083](../../tests/test_multitenant_api.py#L83) | 83 | `"        token=token_b,"` | — |
| [SRC-4405E7912C-L000084](../../tests/test_multitenant_api.py#L84) | 84 | `"        payload={"` | — |
| [SRC-4405E7912C-L000085](../../tests/test_multitenant_api.py#L85) | 85 | `"            \"tenant_id\": tenant_a,"` | — |
| [SRC-4405E7912C-L000086](../../tests/test_multitenant_api.py#L86) | 86 | `"            \"text\": \"Buyer B wants to purchase\","` | — |
| [SRC-4405E7912C-L000087](../../tests/test_multitenant_api.py#L87) | 87 | `"            \"source_url\": \"https://example.test/b\","` | — |
| [SRC-4405E7912C-L000088](../../tests/test_multitenant_api.py#L88) | 88 | `"            \"platform\": \"public\","` | — |
| [SRC-4405E7912C-L000089](../../tests/test_multitenant_api.py#L89) | 89 | `"        },"` | — |
| [SRC-4405E7912C-L000090](../../tests/test_multitenant_api.py#L90) | 90 | `"    )"` | — |
| [SRC-4405E7912C-L000091](../../tests/test_multitenant_api.py#L91) | 91 | `"    assert status == 201"` | — |
| [SRC-4405E7912C-L000092](../../tests/test_multitenant_api.py#L92) | 92 | `"    assert created_b[\"lead\"][\"tenant_id\"] == tenant_b"` | — |
| [SRC-4405E7912C-L000093](../../tests/test_multitenant_api.py#L93) | 93 | `""` | — |
| [SRC-4405E7912C-L000094](../../tests/test_multitenant_api.py#L94) | 94 | `"    status, listing_a = request_json("` | — |
| [SRC-4405E7912C-L000095](../../tests/test_multitenant_api.py#L95) | 95 | `"        base, f\"/api/leads?tenant_id={tenant_b}\", token=token_a"` | — |
| [SRC-4405E7912C-L000096](../../tests/test_multitenant_api.py#L96) | 96 | `"    )"` | — |
| [SRC-4405E7912C-L000097](../../tests/test_multitenant_api.py#L97) | 97 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000098](../../tests/test_multitenant_api.py#L98) | 98 | `"    assert [lead[\"id\"] for lead in listing_a[\"leads\"]] == [created_a[\"lead\"][\"id\"]]"` | — |
| [SRC-4405E7912C-L000099](../../tests/test_multitenant_api.py#L99) | 99 | `""` | — |
| [SRC-4405E7912C-L000100](../../tests/test_multitenant_api.py#L100) | 100 | `"    status, listing_b = request_json(base, \"/api/leads\", token=token_b)"` | — |
| [SRC-4405E7912C-L000101](../../tests/test_multitenant_api.py#L101) | 101 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000102](../../tests/test_multitenant_api.py#L102) | 102 | `"    assert [lead[\"id\"] for lead in listing_b[\"leads\"]] == [created_b[\"lead\"][\"id\"]]"` | — |
| [SRC-4405E7912C-L000103](../../tests/test_multitenant_api.py#L103) | 103 | `""` | — |
| [SRC-4405E7912C-L000104](../../tests/test_multitenant_api.py#L104) | 104 | `"    status, denied = request_json("` | — |
| [SRC-4405E7912C-L000105](../../tests/test_multitenant_api.py#L105) | 105 | `"        base,"` | — |
| [SRC-4405E7912C-L000106](../../tests/test_multitenant_api.py#L106) | 106 | `"        f\"/api/leads/{created_b['lead']['id']}/status\","` | — |
| [SRC-4405E7912C-L000107](../../tests/test_multitenant_api.py#L107) | 107 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000108](../../tests/test_multitenant_api.py#L108) | 108 | `"        token=token_a,"` | — |
| [SRC-4405E7912C-L000109](../../tests/test_multitenant_api.py#L109) | 109 | `"        payload={\"status\": \"qualified\"},"` | — |
| [SRC-4405E7912C-L000110](../../tests/test_multitenant_api.py#L110) | 110 | `"    )"` | — |
| [SRC-4405E7912C-L000111](../../tests/test_multitenant_api.py#L111) | 111 | `"    assert status == 404"` | — |
| [SRC-4405E7912C-L000112](../../tests/test_multitenant_api.py#L112) | 112 | `"    assert denied[\"error\"] == \"lead not found\""` | — |
| [SRC-4405E7912C-L000113](../../tests/test_multitenant_api.py#L113) | 113 | `""` | — |
| [SRC-4405E7912C-L000114](../../tests/test_multitenant_api.py#L114) | 114 | `"    status, changed = request_json("` | — |
| [SRC-4405E7912C-L000115](../../tests/test_multitenant_api.py#L115) | 115 | `"        base,"` | — |
| [SRC-4405E7912C-L000116](../../tests/test_multitenant_api.py#L116) | 116 | `"        f\"/api/leads/{created_b['lead']['id']}/status\","` | — |
| [SRC-4405E7912C-L000117](../../tests/test_multitenant_api.py#L117) | 117 | `"        method=\"POST\","` | — |
| [SRC-4405E7912C-L000118](../../tests/test_multitenant_api.py#L118) | 118 | `"        token=token_b,"` | — |
| [SRC-4405E7912C-L000119](../../tests/test_multitenant_api.py#L119) | 119 | `"        payload={\"status\": \"qualified\"},"` | — |
| [SRC-4405E7912C-L000120](../../tests/test_multitenant_api.py#L120) | 120 | `"    )"` | — |
| [SRC-4405E7912C-L000121](../../tests/test_multitenant_api.py#L121) | 121 | `"    assert status == 200"` | — |
| [SRC-4405E7912C-L000122](../../tests/test_multitenant_api.py#L122) | 122 | `"    assert changed[\"lead\"][\"status\"] == \"qualified\""` | — |
| [SRC-4405E7912C-L000123](../../tests/test_multitenant_api.py#L123) | 123 | `""` | — |
| [SRC-4405E7912C-L000124](../../tests/test_multitenant_api.py#L124) | 124 | `""` | — |
| [SRC-4405E7912C-L000125](../../tests/test_multitenant_api.py#L125) | 125 | `"def test_public_api_rejects_unknown_token(tenant_api):"` | — |
| [SRC-4405E7912C-L000126](../../tests/test_multitenant_api.py#L126) | 126 | `"    base, _ = tenant_api"` | — |
| [SRC-4405E7912C-L000127](../../tests/test_multitenant_api.py#L127) | 127 | `"    status, error = request_json("` | — |
| [SRC-4405E7912C-L000128](../../tests/test_multitenant_api.py#L128) | 128 | `"        base,"` | — |
| [SRC-4405E7912C-L000129](../../tests/test_multitenant_api.py#L129) | 129 | `"        \"/api/leads\","` | — |
| [SRC-4405E7912C-L000130](../../tests/test_multitenant_api.py#L130) | 130 | `"        token=\"unknown-token-\" + \"X\" * 32,"` | — |
| [SRC-4405E7912C-L000131](../../tests/test_multitenant_api.py#L131) | 131 | `"    )"` | — |
| [SRC-4405E7912C-L000132](../../tests/test_multitenant_api.py#L132) | 132 | `"    assert status == 401"` | — |
| [SRC-4405E7912C-L000133](../../tests/test_multitenant_api.py#L133) | 133 | `"    assert \"رمز الوصول\" in error[\"error\"]"` | — |
| [SRC-4405E7912C-L000134](../../tests/test_multitenant_api.py#L134) | 134 | `""` | — |
| [SRC-4405E7912C-L000135](../../tests/test_multitenant_api.py#L135) | 135 | `""` | — |
| [SRC-4405E7912C-L000136](../../tests/test_multitenant_api.py#L136) | 136 | `"def test_viewer_membership_is_read_only(tenant_api):"` | — |
| [SRC-4405E7912C-L000137](../../tests/test_multitenant_api.py#L137) | 137 | `"    base, store = tenant_api"` | — |
| [SRC-4405E7912C-L000138](../../tests/test_multitenant_api.py#L138) | 138 | `"    tenant_id = store.create_tenant(\"Read Only Company\", \"read-only-company\")"` | — |
