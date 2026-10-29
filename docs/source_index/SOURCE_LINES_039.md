# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **039**
- سجلات الأسطر: **800**
- النطاق: SRC-6BF96689A8-L000172 إلى SRC-01E35ABC46-L000449
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-6BF96689A8 — [tests/test_research.py](../../tests/test_research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6BF96689A8-L000172](../../tests/test_research.py#L172) | 172 | `"    ]"` | — |
| [SRC-6BF96689A8-L000173](../../tests/test_research.py#L173) | 173 | `"    for question, required_terms, removed_terms in cases:"` | — |
| [SRC-6BF96689A8-L000174](../../tests/test_research.py#L174) | 174 | `"        query = compact_search_query(question)"` | — |
| [SRC-6BF96689A8-L000175](../../tests/test_research.py#L175) | 175 | `"        assert 2 <= len(query) <= 240"` | — |
| [SRC-6BF96689A8-L000176](../../tests/test_research.py#L176) | 176 | `"        for term in required_terms:"` | — |
| [SRC-6BF96689A8-L000177](../../tests/test_research.py#L177) | 177 | `"            assert term in query, f\"topic term was lost: {term!r} in {query!r}\""` | — |
| [SRC-6BF96689A8-L000178](../../tests/test_research.py#L178) | 178 | `"        for term in removed_terms:"` | — |
| [SRC-6BF96689A8-L000179](../../tests/test_research.py#L179) | 179 | `"            assert term not in query, f\"format instruction remains: {term!r} in {query!r}\""` | — |
| [SRC-6BF96689A8-L000180](../../tests/test_research.py#L180) | 180 | `""` | — |
| [SRC-6BF96689A8-L000181](../../tests/test_research.py#L181) | 181 | `""` | — |
| [SRC-6BF96689A8-L000182](../../tests/test_research.py#L182) | 182 | `"def test_fallback_plan_compacts_four_representative_arabic_tasks_before_expansion():"` | — |
| [SRC-6BF96689A8-L000183](../../tests/test_research.py#L183) | 183 | `"    questions = ["` | — |
| [SRC-6BF96689A8-L000184](../../tests/test_research.py#L184) | 184 | `"        \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\","` | — |
| [SRC-6BF96689A8-L000185](../../tests/test_research.py#L185) | 185 | `"        \"حلل أهم التحديات التي تواجه السيارات الكهربائية في مصر، وقارن بين التكلفة والبنية التحتية والشحن. استخدم مصادر متعددة، وميز بين الحقائق والاستنتاجات، واذكر روابط المصادر.\","` | — |
| [SRC-6BF96689A8-L000186](../../tests/test_research.py#L186) | 186 | `"        \"ما أحدث التطورات في وكلاء الذكاء الاصطناعي خلال الأيام السبعة الماضية؟ اذكر تواريخ الأخبار وروابط المصادر، ولا تعرض معلومات قديمة باعتبارها جديدة.\","` | — |
| [SRC-6BF96689A8-L000187](../../tests/test_research.py#L187) | 187 | `"        \"اجمع آراء وتجارب المستخدمين العامة حول السيارات الكهربائية في مصر. اعرض الآراء الإيجابية والسلبية، واذكر روابط المنشورات أو المصادر المتاحة. وضح إذا كانت النتائج غير كافية لتمثيل آراء المستخدمين عمومًا.\","` | — |
| [SRC-6BF96689A8-L000188](../../tests/test_research.py#L188) | 188 | `"    ]"` | — |
| [SRC-6BF96689A8-L000189](../../tests/test_research.py#L189) | 189 | `"    for question in questions:"` | — |
| [SRC-6BF96689A8-L000190](../../tests/test_research.py#L190) | 190 | `"        plan = fallback_plan(question)"` | — |
| [SRC-6BF96689A8-L000191](../../tests/test_research.py#L191) | 191 | `"        assert plan[\"queries\"]"` | — |
| [SRC-6BF96689A8-L000192](../../tests/test_research.py#L192) | 192 | `"        assert all(2 <= len(query) <= 240 for query in plan[\"queries\"])"` | — |
| [SRC-6BF96689A8-L000193](../../tests/test_research.py#L193) | 193 | `""` | — |
| [SRC-6BF96689A8-L000194](../../tests/test_research.py#L194) | 194 | `""` | — |
| [SRC-6BF96689A8-L000195](../../tests/test_research.py#L195) | 195 | `"def test_compact_search_query_preserves_site_operator_and_discards_separate_citation_instruction():"` | — |
| [SRC-6BF96689A8-L000196](../../tests/test_research.py#L196) | 196 | `"    query = compact_search_query("` | — |
| [SRC-6BF96689A8-L000197](../../tests/test_research.py#L197) | 197 | `"        'site:reddit.com electric car reviews Egypt. Cite the original posts and provide links.'"` | — |
| [SRC-6BF96689A8-L000198](../../tests/test_research.py#L198) | 198 | `"    )"` | — |
| [SRC-6BF96689A8-L000199](../../tests/test_research.py#L199) | 199 | `"    assert query.startswith(\"site:reddit.com\")"` | — |
| [SRC-6BF96689A8-L000200](../../tests/test_research.py#L200) | 200 | `"    assert \"electric car reviews Egypt\" in query"` | — |
| [SRC-6BF96689A8-L000201](../../tests/test_research.py#L201) | 201 | `"    assert \"Cite the original posts\" not in query"` | — |
| [SRC-6BF96689A8-L000202](../../tests/test_research.py#L202) | 202 | `"    assert len(query) <= 240"` | — |
| [SRC-6BF96689A8-L000203](../../tests/test_research.py#L203) | 203 | `""` | — |
| [SRC-6BF96689A8-L000204](../../tests/test_research.py#L204) | 204 | `""` | — |
| [SRC-6BF96689A8-L000205](../../tests/test_research.py#L205) | 205 | `"def test_compact_search_query_bounds_length_without_leaving_partial_tail_word():"` | — |
| [SRC-6BF96689A8-L000206](../../tests/test_research.py#L206) | 206 | `"    query = compact_search_query("` | — |
| [SRC-6BF96689A8-L000207](../../tests/test_research.py#L207) | 207 | `"        \"Electric vehicles in Egypt charging infrastructure costs and ownership experiences\","` | — |
| [SRC-6BF96689A8-L000208](../../tests/test_research.py#L208) | 208 | `"        limit=42,"` | — |
| [SRC-6BF96689A8-L000209](../../tests/test_research.py#L209) | 209 | `"    )"` | — |
| [SRC-6BF96689A8-L000210](../../tests/test_research.py#L210) | 210 | `"    assert len(query) <= 42"` | — |
| [SRC-6BF96689A8-L000211](../../tests/test_research.py#L211) | 211 | `"    assert not query.endswith(\"infrastructur\")"` | — |
| [SRC-6BF96689A8-L000212](../../tests/test_research.py#L212) | 212 | `""` | — |
| [SRC-6BF96689A8-L000213](../../tests/test_research.py#L213) | 213 | `""` | — |
| [SRC-6BF96689A8-L000214](../../tests/test_research.py#L214) | 214 | `"def test_compact_search_query_preserves_subject_when_prompt_starts_with_action_verb():"` | — |
| [SRC-6BF96689A8-L000215](../../tests/test_research.py#L215) | 215 | `"    query = compact_search_query("` | — |
| [SRC-6BF96689A8-L000216](../../tests/test_research.py#L216) | 216 | `"        \"وضح أهمية السيارات الكهربائية في مصر. ما تأثير الشحن على المدى الطويل؟ اذكر مصادر موثوقة.\""` | — |
| [SRC-6BF96689A8-L000217](../../tests/test_research.py#L217) | 217 | `"    )"` | — |
| [SRC-6BF96689A8-L000218](../../tests/test_research.py#L218) | 218 | `"    assert \"السيارات الكهربائية في مصر\" in query"` | — |
| [SRC-6BF96689A8-L000219](../../tests/test_research.py#L219) | 219 | `"    assert \"الشحن على المدى الطويل\" in query"` | — |
| [SRC-6BF96689A8-L000220](../../tests/test_research.py#L220) | 220 | `"    assert \"مصادر موثوقة\" not in query"` | — |
| [SRC-6BF96689A8-L000221](../../tests/test_research.py#L221) | 221 | `""` | — |
| [SRC-6BF96689A8-L000222](../../tests/test_research.py#L222) | 222 | `"    query = compact_search_query("` | — |
| [SRC-6BF96689A8-L000223](../../tests/test_research.py#L223) | 223 | `"        \"اذكر أبرز السيارات الكهربائية في مصر. قارن بين أسعارها.\""` | — |
| [SRC-6BF96689A8-L000224](../../tests/test_research.py#L224) | 224 | `"    )"` | — |
| [SRC-6BF96689A8-L000225](../../tests/test_research.py#L225) | 225 | `"    assert \"السيارات الكهربائية في مصر\" in query"` | — |
| [SRC-6BF96689A8-L000226](../../tests/test_research.py#L226) | 226 | `"    assert \"أسعارها\" in query"` | — |
| [SRC-6BF96689A8-L000227](../../tests/test_research.py#L227) | 227 | `"    assert \"اذكر أبرز\" not in query"` | — |
| [SRC-6BF96689A8-L000228](../../tests/test_research.py#L228) | 228 | `""` | — |
| [SRC-6BF96689A8-L000229](../../tests/test_research.py#L229) | 229 | `""` | — |
| [SRC-6BF96689A8-L000230](../../tests/test_research.py#L230) | 230 | `""` | — |
| [SRC-6BF96689A8-L000231](../../tests/test_research.py#L231) | 231 | `"def test_compact_search_query_returns_empty_for_instruction_only_request():"` | — |
| [SRC-6BF96689A8-L000232](../../tests/test_research.py#L232) | 232 | `"    query = compact_search_query(\"اذكر مصادر موثوقة، روابط مباشرة، باختصار\")"` | — |
| [SRC-6BF96689A8-L000233](../../tests/test_research.py#L233) | 233 | `"    assert query == \"\""` | — |
| [SRC-6BF96689A8-L000234](../../tests/test_research.py#L234) | 234 | `""` | — |
| [SRC-6BF96689A8-L000235](../../tests/test_research.py#L235) | 235 | `""` | — |
| [SRC-6BF96689A8-L000236](../../tests/test_research.py#L236) | 236 | `"def test_compact_search_query_removes_diacritic_uncertainty_instruction():"` | — |
| [SRC-6BF96689A8-L000237](../../tests/test_research.py#L237) | 237 | `"    question = ("` | — |
| [SRC-6BF96689A8-L000238](../../tests/test_research.py#L238) | 238 | `"        \"اجمع آراء العملاء عن السيارات الكهربائية. \""` | — |
| [SRC-6BF96689A8-L000239](../../tests/test_research.py#L239) | 239 | `"        \"وَضِّحْ إِذَا كَانَتِ النَّتَائِجُ غَيْرَ كَافِيَةٍ \""` | — |
| [SRC-6BF96689A8-L000240](../../tests/test_research.py#L240) | 240 | `"        \"لِتَمْثِيلِ آراء المستخدمين عمومًا.\""` | — |
| [SRC-6BF96689A8-L000241](../../tests/test_research.py#L241) | 241 | `"    )"` | — |
| [SRC-6BF96689A8-L000242](../../tests/test_research.py#L242) | 242 | `"    query = compact_search_query(question)"` | — |
| [SRC-6BF96689A8-L000243](../../tests/test_research.py#L243) | 243 | `"    assert \"السيارات الكهربائية\" in query"` | — |
| [SRC-6BF96689A8-L000244](../../tests/test_research.py#L244) | 244 | `"    assert \"النتائج\" not in query"` | — |
| [SRC-6BF96689A8-L000245](../../tests/test_research.py#L245) | 245 | `"    assert \"تمثيل آراء المستخدمين\" not in query"` | — |
| [SRC-6BF96689A8-L000246](../../tests/test_research.py#L246) | 246 | `""` | — |
| [SRC-6BF96689A8-L000247](../../tests/test_research.py#L247) | 247 | `""` | — |
| [SRC-6BF96689A8-L000248](../../tests/test_research.py#L248) | 248 | `"def test_compact_search_query_preserves_topic_after_source_quality_lead_in():"` | — |
| [SRC-6BF96689A8-L000249](../../tests/test_research.py#L249) | 249 | `"    cases = ("` | — |
| [SRC-6BF96689A8-L000250](../../tests/test_research.py#L250) | 250 | `"        ("` | — |
| [SRC-6BF96689A8-L000251](../../tests/test_research.py#L251) | 251 | `"            \"استخدم مصادر متعددة للبحث عن السيارات الكهربائية في مصر\","` | — |
| [SRC-6BF96689A8-L000252](../../tests/test_research.py#L252) | 252 | `"            (\"السيارات الكهربائية\", \"مصر\"),"` | — |
| [SRC-6BF96689A8-L000253](../../tests/test_research.py#L253) | 253 | `"        ),"` | — |
| [SRC-6BF96689A8-L000254](../../tests/test_research.py#L254) | 254 | `"        ("` | — |
| [SRC-6BF96689A8-L000255](../../tests/test_research.py#L255) | 255 | `"            \"Use multiple sources to research electric vehicle charging in Egypt\","` | — |
| [SRC-6BF96689A8-L000256](../../tests/test_research.py#L256) | 256 | `"            (\"electric vehicle charging\", \"Egypt\"),"` | — |
| [SRC-6BF96689A8-L000257](../../tests/test_research.py#L257) | 257 | `"        ),"` | — |
| [SRC-6BF96689A8-L000258](../../tests/test_research.py#L258) | 258 | `"    )"` | — |
| [SRC-6BF96689A8-L000259](../../tests/test_research.py#L259) | 259 | `"    for question, required_terms in cases:"` | — |
| [SRC-6BF96689A8-L000260](../../tests/test_research.py#L260) | 260 | `"        query = compact_search_query(question)"` | — |
| [SRC-6BF96689A8-L000261](../../tests/test_research.py#L261) | 261 | `"        assert query"` | — |
| [SRC-6BF96689A8-L000262](../../tests/test_research.py#L262) | 262 | `"        for term in required_terms:"` | — |
| [SRC-6BF96689A8-L000263](../../tests/test_research.py#L263) | 263 | `"            assert term in query, f\"lost topic term {term!r}: {query!r}\""` | — |
| [SRC-6BF96689A8-L000264](../../tests/test_research.py#L264) | 264 | `""` | — |
| [SRC-6BF96689A8-L000265](../../tests/test_research.py#L265) | 265 | `""` | — |
| [SRC-6BF96689A8-L000266](../../tests/test_research.py#L266) | 266 | `"def test_compact_search_query_preserves_topic_after_distinguish_action():"` | — |
| [SRC-6BF96689A8-L000267](../../tests/test_research.py#L267) | 267 | `"    query = compact_search_query(\"ميّز بين السيارات الكهربائية وسيارات البنزين في مصر\")"` | — |
| [SRC-6BF96689A8-L000268](../../tests/test_research.py#L268) | 268 | `"    assert \"السيارات الكهربائية\" in query"` | — |
| [SRC-6BF96689A8-L000269](../../tests/test_research.py#L269) | 269 | `"    assert \"سيارات البنزين\" in query"` | — |
| [SRC-6BF96689A8-L000270](../../tests/test_research.py#L270) | 270 | `"    assert \"مصر\" in query"` | — |
| [SRC-6BF96689A8-L000271](../../tests/test_research.py#L271) | 271 | `""` | — |
| [SRC-6BF96689A8-L000272](../../tests/test_research.py#L272) | 272 | `""` | — |
| [SRC-6BF96689A8-L000273](../../tests/test_research.py#L273) | 273 | `"def test_compact_search_query_discards_standalone_fact_vs_inference_instruction():"` | — |
| [SRC-6BF96689A8-L000274](../../tests/test_research.py#L274) | 274 | `"    assert compact_search_query(\"ميّز بين الحقائق والاستنتاجات.\") == \"\""` | — |
| [SRC-6BF96689A8-L000275](../../tests/test_research.py#L275) | 275 | `""` | — |
| [SRC-6BF96689A8-L000276](../../tests/test_research.py#L276) | 276 | `""` | — |
| [SRC-6BF96689A8-L000277](../../tests/test_research.py#L277) | 277 | `"def test_fallback_plan_does_not_invent_query_for_instruction_only_prompt():"` | — |
| [SRC-6BF96689A8-L000278](../../tests/test_research.py#L278) | 278 | `"    plan = fallback_plan(\"اذكر مصادر موثوقة، روابط مباشرة، باختصار\")"` | — |
| [SRC-6BF96689A8-L000279](../../tests/test_research.py#L279) | 279 | `"    assert plan[\"queries\"] == []"` | — |
| [SRC-6BF96689A8-L000280](../../tests/test_research.py#L280) | 280 | `""` | — |
| [SRC-6BF96689A8-L000281](../../tests/test_research.py#L281) | 281 | `""` | — |
| [SRC-6BF96689A8-L000282](../../tests/test_research.py#L282) | 282 | `"def test_collect_research_compacts_queries_before_provider_calls(monkeypatch):"` | — |
| [SRC-6BF96689A8-L000283](../../tests/test_research.py#L283) | 283 | `"    from agents.web_agent import WebAgent"` | — |
| [SRC-6BF96689A8-L000284](../../tests/test_research.py#L284) | 284 | `""` | — |
| [SRC-6BF96689A8-L000285](../../tests/test_research.py#L285) | 285 | `"    agent = WebAgent()"` | — |
| [SRC-6BF96689A8-L000286](../../tests/test_research.py#L286) | 286 | `"    seen = []"` | — |
| [SRC-6BF96689A8-L000287](../../tests/test_research.py#L287) | 287 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: seen.append(query) or [])"` | — |
| [SRC-6BF96689A8-L000288](../../tests/test_research.py#L288) | 288 | `"    sources, _warnings, report = agent._collect_research({"` | — |
| [SRC-6BF96689A8-L000289](../../tests/test_research.py#L289) | 289 | `"        \"queries\": ["` | — |
| [SRC-6BF96689A8-L000290](../../tests/test_research.py#L290) | 290 | `"            \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\""` | — |
| [SRC-6BF96689A8-L000291](../../tests/test_research.py#L291) | 291 | `"        ],"` | — |
| [SRC-6BF96689A8-L000292](../../tests/test_research.py#L292) | 292 | `"        \"direct_urls\": [],"` | — |
| [SRC-6BF96689A8-L000293](../../tests/test_research.py#L293) | 293 | `"        \"social_focus\": False,"` | — |
| [SRC-6BF96689A8-L000294](../../tests/test_research.py#L294) | 294 | `"        \"freshness\": \"any\","` | — |
| [SRC-6BF96689A8-L000295](../../tests/test_research.py#L295) | 295 | `"        \"depth\": \"standard\","` | — |
| [SRC-6BF96689A8-L000296](../../tests/test_research.py#L296) | 296 | `"        \"platforms\": [],"` | — |
| [SRC-6BF96689A8-L000297](../../tests/test_research.py#L297) | 297 | `"    })"` | — |
| [SRC-6BF96689A8-L000298](../../tests/test_research.py#L298) | 298 | `""` | — |
| [SRC-6BF96689A8-L000299](../../tests/test_research.py#L299) | 299 | `"    assert sources == []"` | — |
| [SRC-6BF96689A8-L000300](../../tests/test_research.py#L300) | 300 | `"    assert seen == [\"ما عاصمة مصر؟\"]"` | — |
| [SRC-6BF96689A8-L000301](../../tests/test_research.py#L301) | 301 | `"    assert report[\"queries_planned\"] == 1"` | — |
| [SRC-6BF96689A8-L000302](../../tests/test_research.py#L302) | 302 | `"    assert report[\"queries_attempted\"] == 1"` | — |
| [SRC-6BF96689A8-L000303](../../tests/test_research.py#L303) | 303 | `""` | — |
| [SRC-6BF96689A8-L000304](../../tests/test_research.py#L304) | 304 | `""` | — |
| [SRC-6BF96689A8-L000305](../../tests/test_research.py#L305) | 305 | `"def test_collect_research_skips_provider_calls_without_topic_or_direct_url(monkeypatch):"` | — |
| [SRC-6BF96689A8-L000306](../../tests/test_research.py#L306) | 306 | `"    from agents.web_agent import WebAgent"` | — |
| [SRC-6BF96689A8-L000307](../../tests/test_research.py#L307) | 307 | `""` | — |
| [SRC-6BF96689A8-L000308](../../tests/test_research.py#L308) | 308 | `"    agent = WebAgent()"` | — |
| [SRC-6BF96689A8-L000309](../../tests/test_research.py#L309) | 309 | `"    seen = []"` | — |
| [SRC-6BF96689A8-L000310](../../tests/test_research.py#L310) | 310 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: seen.append(query) or [])"` | — |
| [SRC-6BF96689A8-L000311](../../tests/test_research.py#L311) | 311 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-6BF96689A8-L000312](../../tests/test_research.py#L312) | 312 | `"        \"queries\": [\"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"],"` | — |
| [SRC-6BF96689A8-L000313](../../tests/test_research.py#L313) | 313 | `"        \"direct_urls\": [],"` | — |
| [SRC-6BF96689A8-L000314](../../tests/test_research.py#L314) | 314 | `"        \"social_focus\": False,"` | — |
| [SRC-6BF96689A8-L000315](../../tests/test_research.py#L315) | 315 | `"        \"freshness\": \"any\","` | — |
| [SRC-6BF96689A8-L000316](../../tests/test_research.py#L316) | 316 | `"        \"depth\": \"standard\","` | — |
| [SRC-6BF96689A8-L000317](../../tests/test_research.py#L317) | 317 | `"        \"platforms\": [],"` | — |
| [SRC-6BF96689A8-L000318](../../tests/test_research.py#L318) | 318 | `"    })"` | — |
| [SRC-6BF96689A8-L000319](../../tests/test_research.py#L319) | 319 | `""` | — |
| [SRC-6BF96689A8-L000320](../../tests/test_research.py#L320) | 320 | `"    assert sources == []"` | — |
| [SRC-6BF96689A8-L000321](../../tests/test_research.py#L321) | 321 | `"    assert report[\"queries_planned\"] == 0"` | — |
| [SRC-6BF96689A8-L000322](../../tests/test_research.py#L322) | 322 | `"    assert report[\"queries_attempted\"] == 0"` | — |
| [SRC-6BF96689A8-L000323](../../tests/test_research.py#L323) | 323 | `"    assert seen == []"` | — |
| [SRC-6BF96689A8-L000324](../../tests/test_research.py#L324) | 324 | `"    assert any(\"لم تُستدعَ محركات البحث\" in warning for warning in warnings)"` | — |
| [SRC-6BF96689A8-L000325](../../tests/test_research.py#L325) | 325 | `""` | — |
| [SRC-6BF96689A8-L000326](../../tests/test_research.py#L326) | 326 | `""` | — |
| [SRC-6BF96689A8-L000327](../../tests/test_research.py#L327) | 327 | `"def test_fallback_plan_keeps_direct_url_without_generic_keyword_query():"` | — |
| [SRC-6BF96689A8-L000328](../../tests/test_research.py#L328) | 328 | `"    plan = fallback_plan(\"https://example.com/research\")"` | — |
| [SRC-6BF96689A8-L000329](../../tests/test_research.py#L329) | 329 | `"    assert plan[\"direct_urls\"] == [\"https://example.com/research\"]"` | — |
| [SRC-6BF96689A8-L000330](../../tests/test_research.py#L330) | 330 | `"    assert plan[\"queries\"] == []"` | — |
| [SRC-6BF96689A8-L000331](../../tests/test_research.py#L331) | 331 | `""` | — |
| [SRC-6BF96689A8-L000332](../../tests/test_research.py#L332) | 332 | `""` | — |
| [SRC-6BF96689A8-L000333](../../tests/test_research.py#L333) | 333 | `""` | — |
| [SRC-6BF96689A8-L000334](../../tests/test_research.py#L334) | 334 | `"def test_followup_plan_keeps_topic_across_chained_turns():"` | — |
| [SRC-6BF96689A8-L000335](../../tests/test_research.py#L335) | 335 | `"    history = ["` | — |
| [SRC-6BF96689A8-L000336](../../tests/test_research.py#L336) | 336 | `"        {\"role\": \"user\", \"content\": \"ما سعر iPhone 16 في مصر؟\"},"` | — |
| [SRC-6BF96689A8-L000337](../../tests/test_research.py#L337) | 337 | `"        {\"role\": \"assistant\", \"content\": \"السعر يختلف حسب المتجر.\"},"` | — |
| [SRC-6BF96689A8-L000338](../../tests/test_research.py#L338) | 338 | `"        {\"role\": \"user\", \"content\": \"والضمان؟\"},"` | — |
| [SRC-6BF96689A8-L000339](../../tests/test_research.py#L339) | 339 | `"        {\"role\": \"assistant\", \"content\": \"سأوضح الضمان.\"},"` | — |
| [SRC-6BF96689A8-L000340](../../tests/test_research.py#L340) | 340 | `"    ]"` | — |
| [SRC-6BF96689A8-L000341](../../tests/test_research.py#L341) | 341 | `"    plan = fallback_plan(\"والبطارية؟\", history)"` | — |
| [SRC-6BF96689A8-L000342](../../tests/test_research.py#L342) | 342 | `"    assert plan[\"queries\"]"` | — |
| [SRC-6BF96689A8-L000343](../../tests/test_research.py#L343) | 343 | `"    assert \"iPhone 16\" in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000344](../../tests/test_research.py#L344) | 344 | `"    assert \"البطارية\" in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000345](../../tests/test_research.py#L345) | 345 | `""` | — |
| [SRC-6BF96689A8-L000346](../../tests/test_research.py#L346) | 346 | `""` | — |
| [SRC-6BF96689A8-L000347](../../tests/test_research.py#L347) | 347 | `"def test_followup_plan_does_not_inherit_unrelated_social_intent():"` | — |
| [SRC-6BF96689A8-L000348](../../tests/test_research.py#L348) | 348 | `"    history = ["` | — |
| [SRC-6BF96689A8-L000349](../../tests/test_research.py#L349) | 349 | `"        {\"role\": \"user\", \"content\": \"اجمع آراء مستخدمي السيارات الكهربائية على Reddit\"},"` | — |
| [SRC-6BF96689A8-L000350](../../tests/test_research.py#L350) | 350 | `"        {\"role\": \"assistant\", \"content\": \"هذه النتائج.\"},"` | — |
| [SRC-6BF96689A8-L000351](../../tests/test_research.py#L351) | 351 | `"    ]"` | — |
| [SRC-6BF96689A8-L000352](../../tests/test_research.py#L352) | 352 | `"    plan = fallback_plan(\"اشرح طريقة عمل المحرك الكهربائي\", history)"` | — |
| [SRC-6BF96689A8-L000353](../../tests/test_research.py#L353) | 353 | `"    assert plan[\"social_focus\"] is False"` | — |
| [SRC-6BF96689A8-L000354](../../tests/test_research.py#L354) | 354 | `"    assert plan[\"platforms\"] == []"` | — |
| [SRC-6BF96689A8-L000355](../../tests/test_research.py#L355) | 355 | `""` | — |
| [SRC-6BF96689A8-L000356](../../tests/test_research.py#L356) | 356 | `""` | — |
| [SRC-6BF96689A8-L000357](../../tests/test_research.py#L357) | 357 | `""` | — |
| [SRC-6BF96689A8-L000358](../../tests/test_research.py#L358) | 358 | `"def test_source_classification_does_not_trust_lookalike_news_domains():"` | — |
| [SRC-6BF96689A8-L000359](../../tests/test_research.py#L359) | 359 | `"    assert classify_source(\"https://www.reuters.com/world/article\")[\"source_class\"] == \"news\""` | — |
| [SRC-6BF96689A8-L000360](../../tests/test_research.py#L360) | 360 | `"    lookalike = classify_source(\"https://reuters.com.attacker.example/article\")"` | — |
| [SRC-6BF96689A8-L000361](../../tests/test_research.py#L361) | 361 | `"    assert lookalike[\"source_class\"] == \"general\""` | — |
| [SRC-6BF96689A8-L000362](../../tests/test_research.py#L362) | 362 | `"    assert lookalike[\"domain\"] == \"reuters.com.attacker.example\""` | — |
## اختبارات

### FILE-AFFCF23BD4 — [tests/test_research_completion.py](../../tests/test_research_completion.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-AFFCF23BD4-L000001](../../tests/test_research_completion.py#L1) | 1 | `"\"\"\"Tests for truthful research completion states and counter reconciliation.\"\"\""` | — |
| [SRC-AFFCF23BD4-L000002](../../tests/test_research_completion.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-AFFCF23BD4-L000003](../../tests/test_research_completion.py#L3) | 3 | `""` | — |
| [SRC-AFFCF23BD4-L000004](../../tests/test_research_completion.py#L4) | 4 | `"from agents.research_completion import build_research_completion"` | — |
| [SRC-AFFCF23BD4-L000005](../../tests/test_research_completion.py#L5) | 5 | `""` | — |
| [SRC-AFFCF23BD4-L000006](../../tests/test_research_completion.py#L6) | 6 | `""` | — |
| [SRC-AFFCF23BD4-L000007](../../tests/test_research_completion.py#L7) | 7 | `"def test_non_research_answer_is_not_reported_as_web_research_complete() -> None:"` | — |
| [SRC-AFFCF23BD4-L000008](../../tests/test_research_completion.py#L8) | 8 | `"    result = build_research_completion({\"kind\": \"local_conversation\", \"answer\": \"مرحبا\"})"` | — |
| [SRC-AFFCF23BD4-L000009](../../tests/test_research_completion.py#L9) | 9 | `"    assert result[\"status\"] == \"not_applicable\""` | — |
| [SRC-AFFCF23BD4-L000010](../../tests/test_research_completion.py#L10) | 10 | `"    assert result[\"semantic_verification\"] == \"not_performed\""` | — |
| [SRC-AFFCF23BD4-L000011](../../tests/test_research_completion.py#L11) | 11 | `""` | — |
| [SRC-AFFCF23BD4-L000012](../../tests/test_research_completion.py#L12) | 12 | `""` | — |
| [SRC-AFFCF23BD4-L000013](../../tests/test_research_completion.py#L13) | 13 | `"def test_empty_results_distinguish_zero_results_from_tool_failure() -> None:"` | — |
| [SRC-AFFCF23BD4-L000014](../../tests/test_research_completion.py#L14) | 14 | `"    no_results = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000015](../../tests/test_research_completion.py#L15) | 15 | `"        \"kind\": \"insufficient_evidence\","` | — |
| [SRC-AFFCF23BD4-L000016](../../tests/test_research_completion.py#L16) | 16 | `"        \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000017](../../tests/test_research_completion.py#L17) | 17 | `"        \"sources\": [],"` | — |
| [SRC-AFFCF23BD4-L000018](../../tests/test_research_completion.py#L18) | 18 | `"        \"search_report\": {"` | — |
| [SRC-AFFCF23BD4-L000019](../../tests/test_research_completion.py#L19) | 19 | `"            \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000020](../../tests/test_research_completion.py#L20) | 20 | `"            \"query_results\": [{\"query\": \"topic\", \"results\": 0}],"` | — |
| [SRC-AFFCF23BD4-L000021](../../tests/test_research_completion.py#L21) | 21 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-AFFCF23BD4-L000022](../../tests/test_research_completion.py#L22) | 22 | `"            \"queries_planned\": 1,"` | — |
| [SRC-AFFCF23BD4-L000023](../../tests/test_research_completion.py#L23) | 23 | `"        },"` | — |
| [SRC-AFFCF23BD4-L000024](../../tests/test_research_completion.py#L24) | 24 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000025](../../tests/test_research_completion.py#L25) | 25 | `"    failure = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000026](../../tests/test_research_completion.py#L26) | 26 | `"        \"kind\": \"web_fallback\","` | — |
| [SRC-AFFCF23BD4-L000027](../../tests/test_research_completion.py#L27) | 27 | `"        \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000028](../../tests/test_research_completion.py#L28) | 28 | `"        \"sources\": [],"` | — |
| [SRC-AFFCF23BD4-L000029](../../tests/test_research_completion.py#L29) | 29 | `"        \"search_report\": {"` | — |
| [SRC-AFFCF23BD4-L000030](../../tests/test_research_completion.py#L30) | 30 | `"            \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000031](../../tests/test_research_completion.py#L31) | 31 | `"            \"search_outcome\": \"attempted_research_error\","` | — |
| [SRC-AFFCF23BD4-L000032](../../tests/test_research_completion.py#L32) | 32 | `"            \"provider_diagnostics\": [{\"provider\": \"test\", \"status\": \"timeout\"}],"` | — |
| [SRC-AFFCF23BD4-L000033](../../tests/test_research_completion.py#L33) | 33 | `"        },"` | — |
| [SRC-AFFCF23BD4-L000034](../../tests/test_research_completion.py#L34) | 34 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000035](../../tests/test_research_completion.py#L35) | 35 | `"    assert no_results[\"status\"] == \"no_results_returned\""` | — |
| [SRC-AFFCF23BD4-L000036](../../tests/test_research_completion.py#L36) | 36 | `"    assert no_results[\"phases\"][\"search\"] == \"completed_no_results\""` | — |
| [SRC-AFFCF23BD4-L000037](../../tests/test_research_completion.py#L37) | 37 | `"    assert failure[\"status\"] == \"search_failed_or_incomplete\""` | — |
| [SRC-AFFCF23BD4-L000038](../../tests/test_research_completion.py#L38) | 38 | `"    assert failure[\"counters\"][\"connector_failure_count\"] == 1"` | — |
| [SRC-AFFCF23BD4-L000039](../../tests/test_research_completion.py#L39) | 39 | `""` | — |
| [SRC-AFFCF23BD4-L000040](../../tests/test_research_completion.py#L40) | 40 | `""` | — |
| [SRC-AFFCF23BD4-L000041](../../tests/test_research_completion.py#L41) | 41 | `"def test_all_rejected_sources_are_not_mislabeled_as_no_results() -> None:"` | — |
| [SRC-AFFCF23BD4-L000042](../../tests/test_research_completion.py#L42) | 42 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000043](../../tests/test_research_completion.py#L43) | 43 | `"        \"kind\": \"insufficient_evidence\","` | — |
| [SRC-AFFCF23BD4-L000044](../../tests/test_research_completion.py#L44) | 44 | `"        \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000045](../../tests/test_research_completion.py#L45) | 45 | `"        \"sources\": [],"` | — |
| [SRC-AFFCF23BD4-L000046](../../tests/test_research_completion.py#L46) | 46 | `"        \"search_report\": {"` | — |
| [SRC-AFFCF23BD4-L000047](../../tests/test_research_completion.py#L47) | 47 | `"            \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000048](../../tests/test_research_completion.py#L48) | 48 | `"            \"source_guardrails\": {"` | — |
| [SRC-AFFCF23BD4-L000049](../../tests/test_research_completion.py#L49) | 49 | `"                \"final\": {\"rejection_counts\": {\"stale\": 2, \"date_unavailable\": 1}},"` | — |
| [SRC-AFFCF23BD4-L000050](../../tests/test_research_completion.py#L50) | 50 | `"            },"` | — |
| [SRC-AFFCF23BD4-L000051](../../tests/test_research_completion.py#L51) | 51 | `"        },"` | — |
| [SRC-AFFCF23BD4-L000052](../../tests/test_research_completion.py#L52) | 52 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000053](../../tests/test_research_completion.py#L53) | 53 | `"    assert result[\"status\"] == \"no_eligible_sources_after_filtering\""` | — |
| [SRC-AFFCF23BD4-L000054](../../tests/test_research_completion.py#L54) | 54 | `"    assert result[\"counters\"][\"guardrail_rejected_candidate_count\"] == 3"` | — |
| [SRC-AFFCF23BD4-L000055](../../tests/test_research_completion.py#L55) | 55 | `""` | — |
| [SRC-AFFCF23BD4-L000056](../../tests/test_research_completion.py#L56) | 56 | `""` | — |
| [SRC-AFFCF23BD4-L000057](../../tests/test_research_completion.py#L57) | 57 | `"def test_snippet_only_results_do_not_claim_pages_were_read() -> None:"` | — |
| [SRC-AFFCF23BD4-L000058](../../tests/test_research_completion.py#L58) | 58 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000059](../../tests/test_research_completion.py#L59) | 59 | `"        \"kind\": \"web_fallback\","` | — |
| [SRC-AFFCF23BD4-L000060](../../tests/test_research_completion.py#L60) | 60 | `"        \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000061](../../tests/test_research_completion.py#L61) | 61 | `"        \"used_language_model\": False,"` | — |
| [SRC-AFFCF23BD4-L000062](../../tests/test_research_completion.py#L62) | 62 | `"        \"sources\": ["` | — |
| [SRC-AFFCF23BD4-L000063](../../tests/test_research_completion.py#L63) | 63 | `"            {\"url\": \"https://example.com/a\", \"snippet\": \"Search snippet\", \"page_fetched\": False}"` | — |
| [SRC-AFFCF23BD4-L000064](../../tests/test_research_completion.py#L64) | 64 | `"        ],"` | — |
| [SRC-AFFCF23BD4-L000065](../../tests/test_research_completion.py#L65) | 65 | `"        \"search_report\": {\"unique_sources\": 1, \"pages_fetched\": 0},"` | — |
| [SRC-AFFCF23BD4-L000066](../../tests/test_research_completion.py#L66) | 66 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000067](../../tests/test_research_completion.py#L67) | 67 | `"    assert result[\"status\"] == \"source_snippets_only_generation_not_completed\""` | — |
| [SRC-AFFCF23BD4-L000068](../../tests/test_research_completion.py#L68) | 68 | `"    assert result[\"phases\"][\"page_reading\"] == \"no_final_source_page_read\""` | — |
| [SRC-AFFCF23BD4-L000069](../../tests/test_research_completion.py#L69) | 69 | `"    assert result[\"counters\"][\"pages_read_with_text_count\"] == 0"` | — |
| [SRC-AFFCF23BD4-L000070](../../tests/test_research_completion.py#L70) | 70 | `""` | — |
| [SRC-AFFCF23BD4-L000071](../../tests/test_research_completion.py#L71) | 71 | `""` | — |
| [SRC-AFFCF23BD4-L000072](../../tests/test_research_completion.py#L72) | 72 | `"def test_answer_with_valid_citation_indices_still_discloses_semantic_gap() -> None:"` | — |
| [SRC-AFFCF23BD4-L000073](../../tests/test_research_completion.py#L73) | 73 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000074](../../tests/test_research_completion.py#L74) | 74 | `"        \"kind\": \"web_research\","` | — |
| [SRC-AFFCF23BD4-L000075](../../tests/test_research_completion.py#L75) | 75 | `"        \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000076](../../tests/test_research_completion.py#L76) | 76 | `"        \"used_language_model\": True,"` | — |
| [SRC-AFFCF23BD4-L000077](../../tests/test_research_completion.py#L77) | 77 | `"        \"final_answer_status\": \"model_answer_generated\","` | — |
| [SRC-AFFCF23BD4-L000078](../../tests/test_research_completion.py#L78) | 78 | `"        \"citation_validation\": {\"status\": \"index_range_check_passed\", \"valid_citation_count\": 2},"` | — |
| [SRC-AFFCF23BD4-L000079](../../tests/test_research_completion.py#L79) | 79 | `"        \"sources\": ["` | — |
| [SRC-AFFCF23BD4-L000080](../../tests/test_research_completion.py#L80) | 80 | `"            {\"url\": \"https://example.com/a\", \"snippet\": \"text\", \"page_fetched\": True, \"page_text\": \"read\"}"` | — |
| [SRC-AFFCF23BD4-L000081](../../tests/test_research_completion.py#L81) | 81 | `"        ],"` | — |
| [SRC-AFFCF23BD4-L000082](../../tests/test_research_completion.py#L82) | 82 | `"        \"search_report\": {"` | — |
| [SRC-AFFCF23BD4-L000083](../../tests/test_research_completion.py#L83) | 83 | `"            \"unique_sources\": 1, \"pages_fetched\": 1,"` | — |
| [SRC-AFFCF23BD4-L000084](../../tests/test_research_completion.py#L84) | 84 | `"            \"query_results\": [{\"query\": \"topic\", \"results\": 1}],"` | — |
| [SRC-AFFCF23BD4-L000085](../../tests/test_research_completion.py#L85) | 85 | `"        },"` | — |
| [SRC-AFFCF23BD4-L000086](../../tests/test_research_completion.py#L86) | 86 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000087](../../tests/test_research_completion.py#L87) | 87 | `"    assert result[\"status\"] == \"answer_generated_citations_range_checked_semantic_support_unverified\""` | — |
| [SRC-AFFCF23BD4-L000088](../../tests/test_research_completion.py#L88) | 88 | `"    assert result[\"phases\"][\"semantic_verification\"] == \"not_performed\""` | — |
| [SRC-AFFCF23BD4-L000089](../../tests/test_research_completion.py#L89) | 89 | `"    assert result[\"semantic_verification\"] == \"not_performed\""` | — |
| [SRC-AFFCF23BD4-L000090](../../tests/test_research_completion.py#L90) | 90 | `""` | — |
| [SRC-AFFCF23BD4-L000091](../../tests/test_research_completion.py#L91) | 91 | `""` | — |
| [SRC-AFFCF23BD4-L000092](../../tests/test_research_completion.py#L92) | 92 | `"def test_normalized_url_counters_and_mismatched_legacy_counters_are_exposed() -> None:"` | — |
| [SRC-AFFCF23BD4-L000093](../../tests/test_research_completion.py#L93) | 93 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000094](../../tests/test_research_completion.py#L94) | 94 | `"        \"kind\": \"web_fallback\","` | — |
| [SRC-AFFCF23BD4-L000095](../../tests/test_research_completion.py#L95) | 95 | `"        \"search_attempted\": True,"` | — |
| [SRC-AFFCF23BD4-L000096](../../tests/test_research_completion.py#L96) | 96 | `"        \"sources\": ["` | — |
| [SRC-AFFCF23BD4-L000097](../../tests/test_research_completion.py#L97) | 97 | `"            {\"url\": \"https://example.com/path?utm_source=abc\", \"snippet\": \"a\"},"` | — |
| [SRC-AFFCF23BD4-L000098](../../tests/test_research_completion.py#L98) | 98 | `"            {\"url\": \"https://example.com/path#section\", \"snippet\": \"b\"},"` | — |
| [SRC-AFFCF23BD4-L000099](../../tests/test_research_completion.py#L99) | 99 | `"        ],"` | — |
| [SRC-AFFCF23BD4-L000100](../../tests/test_research_completion.py#L100) | 100 | `"        \"search_report\": {\"unique_sources\": 5, \"pages_fetched\": 4},"` | — |
| [SRC-AFFCF23BD4-L000101](../../tests/test_research_completion.py#L101) | 101 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000102](../../tests/test_research_completion.py#L102) | 102 | `"    assert result[\"counters\"][\"final_source_list_count\"] == 2"` | — |
| [SRC-AFFCF23BD4-L000103](../../tests/test_research_completion.py#L103) | 103 | `"    assert result[\"counters\"][\"unique_normalized_url_count\"] == 1"` | — |
| [SRC-AFFCF23BD4-L000104](../../tests/test_research_completion.py#L104) | 104 | `"    assert result[\"counters\"][\"duplicate_normalized_url_count\"] == 1"` | — |
| [SRC-AFFCF23BD4-L000105](../../tests/test_research_completion.py#L105) | 105 | `"    assert result[\"counter_consistency\"][\"status\"] == \"mismatch_detected\""` | — |
| [SRC-AFFCF23BD4-L000106](../../tests/test_research_completion.py#L106) | 106 | `"    assert len(result[\"counter_consistency\"][\"issues\"]) == 2"` | — |
| [SRC-AFFCF23BD4-L000107](../../tests/test_research_completion.py#L107) | 107 | `""` | — |
| [SRC-AFFCF23BD4-L000108](../../tests/test_research_completion.py#L108) | 108 | `""` | — |
| [SRC-AFFCF23BD4-L000109](../../tests/test_research_completion.py#L109) | 109 | `"def test_counter_consistency_is_not_claimed_when_legacy_counters_are_missing() -> None:"` | — |
| [SRC-AFFCF23BD4-L000110](../../tests/test_research_completion.py#L110) | 110 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000111](../../tests/test_research_completion.py#L111) | 111 | `"        \"kind\": \"web_fallback\", \"search_attempted\": True, \"sources\": [],"` | — |
| [SRC-AFFCF23BD4-L000112](../../tests/test_research_completion.py#L112) | 112 | `"        \"search_report\": {\"query_results\": []},"` | — |
| [SRC-AFFCF23BD4-L000113](../../tests/test_research_completion.py#L113) | 113 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000114](../../tests/test_research_completion.py#L114) | 114 | `"    assert result[\"counter_consistency\"][\"status\"] == \"not_computable\""` | — |
| [SRC-AFFCF23BD4-L000115](../../tests/test_research_completion.py#L115) | 115 | `""` | — |
| [SRC-AFFCF23BD4-L000116](../../tests/test_research_completion.py#L116) | 116 | `""` | — |
| [SRC-AFFCF23BD4-L000117](../../tests/test_research_completion.py#L117) | 117 | `""` | — |
| [SRC-AFFCF23BD4-L000118](../../tests/test_research_completion.py#L118) | 118 | `"def test_public_readability_marker_counts_read_page_without_exposing_text() -> None:"` | — |
| [SRC-AFFCF23BD4-L000119](../../tests/test_research_completion.py#L119) | 119 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000120](../../tests/test_research_completion.py#L120) | 120 | `"        \"kind\": \"web_research\","` | — |
| [SRC-AFFCF23BD4-L000121](../../tests/test_research_completion.py#L121) | 121 | `"        \"used_language_model\": True,"` | — |
| [SRC-AFFCF23BD4-L000122](../../tests/test_research_completion.py#L122) | 122 | `"        \"final_answer_status\": \"model_answer_generated\","` | — |
| [SRC-AFFCF23BD4-L000123](../../tests/test_research_completion.py#L123) | 123 | `"        \"sources\": [{"` | — |
| [SRC-AFFCF23BD4-L000124](../../tests/test_research_completion.py#L124) | 124 | `"            \"url\": \"https://example.com/a\","` | — |
| [SRC-AFFCF23BD4-L000125](../../tests/test_research_completion.py#L125) | 125 | `"            \"snippet\": \"summary\","` | — |
| [SRC-AFFCF23BD4-L000126](../../tests/test_research_completion.py#L126) | 126 | `"            \"page_fetched\": True,"` | — |
| [SRC-AFFCF23BD4-L000127](../../tests/test_research_completion.py#L127) | 127 | `"            \"readable_page_text_available\": True,"` | — |
| [SRC-AFFCF23BD4-L000128](../../tests/test_research_completion.py#L128) | 128 | `"        }],"` | — |
| [SRC-AFFCF23BD4-L000129](../../tests/test_research_completion.py#L129) | 129 | `"        \"search_report\": {\"unique_sources\": 1, \"pages_fetched\": 1},"` | — |
| [SRC-AFFCF23BD4-L000130](../../tests/test_research_completion.py#L130) | 130 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000131](../../tests/test_research_completion.py#L131) | 131 | `"    assert result[\"counters\"][\"pages_read_with_text_count\"] == 1"` | — |
| [SRC-AFFCF23BD4-L000132](../../tests/test_research_completion.py#L132) | 132 | `"    assert result[\"phases\"][\"page_reading\"] == \"all_final_sources_read\""` | — |
| [SRC-AFFCF23BD4-L000133](../../tests/test_research_completion.py#L133) | 133 | `""` | — |
| [SRC-AFFCF23BD4-L000134](../../tests/test_research_completion.py#L134) | 134 | `""` | — |
| [SRC-AFFCF23BD4-L000135](../../tests/test_research_completion.py#L135) | 135 | `"def test_ref_query_parameters_are_not_assumed_to_be_tracking_ids() -> None:"` | — |
| [SRC-AFFCF23BD4-L000136](../../tests/test_research_completion.py#L136) | 136 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000137](../../tests/test_research_completion.py#L137) | 137 | `"        \"kind\": \"web_fallback\","` | — |
| [SRC-AFFCF23BD4-L000138](../../tests/test_research_completion.py#L138) | 138 | `"        \"sources\": ["` | — |
| [SRC-AFFCF23BD4-L000139](../../tests/test_research_completion.py#L139) | 139 | `"            {\"url\": \"https://example.com/post?ref=one\"},"` | — |
| [SRC-AFFCF23BD4-L000140](../../tests/test_research_completion.py#L140) | 140 | `"            {\"url\": \"https://example.com/post?ref=two\"},"` | — |
| [SRC-AFFCF23BD4-L000141](../../tests/test_research_completion.py#L141) | 141 | `"        ],"` | — |
| [SRC-AFFCF23BD4-L000142](../../tests/test_research_completion.py#L142) | 142 | `"        \"search_report\": {},"` | — |
| [SRC-AFFCF23BD4-L000143](../../tests/test_research_completion.py#L143) | 143 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000144](../../tests/test_research_completion.py#L144) | 144 | `"    assert result[\"counters\"][\"unique_normalized_url_count\"] == 2"` | — |
| [SRC-AFFCF23BD4-L000145](../../tests/test_research_completion.py#L145) | 145 | `"    assert result[\"counters\"][\"duplicate_normalized_url_count\"] == 0"` | — |
| [SRC-AFFCF23BD4-L000146](../../tests/test_research_completion.py#L146) | 146 | `""` | — |
| [SRC-AFFCF23BD4-L000147](../../tests/test_research_completion.py#L147) | 147 | `""` | — |
| [SRC-AFFCF23BD4-L000148](../../tests/test_research_completion.py#L148) | 148 | `""` | — |
| [SRC-AFFCF23BD4-L000149](../../tests/test_research_completion.py#L149) | 149 | `"def test_unflagged_page_text_marker_is_counted_without_exposing_page_text() -> None:"` | — |
| [SRC-AFFCF23BD4-L000150](../../tests/test_research_completion.py#L150) | 150 | `"    result = build_research_completion({"` | — |
| [SRC-AFFCF23BD4-L000151](../../tests/test_research_completion.py#L151) | 151 | `"        \"kind\": \"web_fallback\","` | — |
| [SRC-AFFCF23BD4-L000152](../../tests/test_research_completion.py#L152) | 152 | `"        \"sources\": [{"` | — |
| [SRC-AFFCF23BD4-L000153](../../tests/test_research_completion.py#L153) | 153 | `"            \"url\": \"https://example.com/a\","` | — |
| [SRC-AFFCF23BD4-L000154](../../tests/test_research_completion.py#L154) | 154 | `"            \"snippet\": \"summary\","` | — |
| [SRC-AFFCF23BD4-L000155](../../tests/test_research_completion.py#L155) | 155 | `"            \"page_fetched\": False,"` | — |
| [SRC-AFFCF23BD4-L000156](../../tests/test_research_completion.py#L156) | 156 | `"            \"page_text_present_without_fetch_flag\": True,"` | — |
| [SRC-AFFCF23BD4-L000157](../../tests/test_research_completion.py#L157) | 157 | `"        }],"` | — |
| [SRC-AFFCF23BD4-L000158](../../tests/test_research_completion.py#L158) | 158 | `"        \"search_report\": {},"` | — |
| [SRC-AFFCF23BD4-L000159](../../tests/test_research_completion.py#L159) | 159 | `"    })"` | — |
| [SRC-AFFCF23BD4-L000160](../../tests/test_research_completion.py#L160) | 160 | `"    assert result[\"counters\"][\"page_text_without_fetched_flag_count\"] == 1"` | — |
## اختبارات

### FILE-01E35ABC46 — [tests/test_research_guardrails.py](../../tests/test_research_guardrails.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-01E35ABC46-L000001](../../tests/test_research_guardrails.py#L1) | 1 | `"\"\"\"Regression and adversarial tests for depth, freshness, relevance, evidence.\"\"\""` | — |
| [SRC-01E35ABC46-L000002](../../tests/test_research_guardrails.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-01E35ABC46-L000003](../../tests/test_research_guardrails.py#L3) | 3 | `""` | — |
| [SRC-01E35ABC46-L000004](../../tests/test_research_guardrails.py#L4) | 4 | `"from datetime import UTC, datetime"` | — |
| [SRC-01E35ABC46-L000005](../../tests/test_research_guardrails.py#L5) | 5 | `""` | — |
| [SRC-01E35ABC46-L000006](../../tests/test_research_guardrails.py#L6) | 6 | `"from agents.research_guardrails import ("` | — |
| [SRC-01E35ABC46-L000007](../../tests/test_research_guardrails.py#L7) | 7 | `"    apply_source_guardrails,"` | — |
| [SRC-01E35ABC46-L000008](../../tests/test_research_guardrails.py#L8) | 8 | `"    assess_current_source,"` | — |
| [SRC-01E35ABC46-L000009](../../tests/test_research_guardrails.py#L9) | 9 | `"    classify_social_source,"` | — |
| [SRC-01E35ABC46-L000010](../../tests/test_research_guardrails.py#L10) | 10 | `"    requires_official_government_domain,"` | — |
| [SRC-01E35ABC46-L000011](../../tests/test_research_guardrails.py#L11) | 11 | `"    requires_official_current_government_source,"` | — |
| [SRC-01E35ABC46-L000012](../../tests/test_research_guardrails.py#L12) | 12 | `")"` | — |
| [SRC-01E35ABC46-L000013](../../tests/test_research_guardrails.py#L13) | 13 | `"from agents.research import ("` | — |
| [SRC-01E35ABC46-L000014](../../tests/test_research_guardrails.py#L14) | 14 | `"    decide_evidence_status,"` | — |
| [SRC-01E35ABC46-L000015](../../tests/test_research_guardrails.py#L15) | 15 | `"    detect_depth,"` | — |
| [SRC-01E35ABC46-L000016](../../tests/test_research_guardrails.py#L16) | 16 | `"    detect_freshness,"` | — |
| [SRC-01E35ABC46-L000017](../../tests/test_research_guardrails.py#L17) | 17 | `"    filter_relevant_sources,"` | — |
| [SRC-01E35ABC46-L000018](../../tests/test_research_guardrails.py#L18) | 18 | `"    source_relevance_score,"` | — |
| [SRC-01E35ABC46-L000019](../../tests/test_research_guardrails.py#L19) | 19 | `")"` | — |
| [SRC-01E35ABC46-L000020](../../tests/test_research_guardrails.py#L20) | 20 | `""` | — |
| [SRC-01E35ABC46-L000021](../../tests/test_research_guardrails.py#L21) | 21 | `""` | — |
| [SRC-01E35ABC46-L000022](../../tests/test_research_guardrails.py#L22) | 22 | `"# --- detect_depth -----------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000023](../../tests/test_research_guardrails.py#L23) | 23 | `""` | — |
| [SRC-01E35ABC46-L000024](../../tests/test_research_guardrails.py#L24) | 24 | `"def test_depth_deep_english_phrases():"` | — |
| [SRC-01E35ABC46-L000025](../../tests/test_research_guardrails.py#L25) | 25 | `"    assert detect_depth(\"Please do a deep research on climate policy\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000026](../../tests/test_research_guardrails.py#L26) | 26 | `"    assert detect_depth(\"in-depth comparison of EV batteries\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000027](../../tests/test_research_guardrails.py#L27) | 27 | `"    assert detect_depth(\"comprehensive analysis of market risks\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000028](../../tests/test_research_guardrails.py#L28) | 28 | `""` | — |
| [SRC-01E35ABC46-L000029](../../tests/test_research_guardrails.py#L29) | 29 | `""` | — |
| [SRC-01E35ABC46-L000030](../../tests/test_research_guardrails.py#L30) | 30 | `"def test_depth_deep_arabic_phrases():"` | — |
| [SRC-01E35ABC46-L000031](../../tests/test_research_guardrails.py#L31) | 31 | `"    assert detect_depth(\"أريد بحث عميق عن الذكاء الاصطناعي\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000032](../../tests/test_research_guardrails.py#L32) | 32 | `"    assert detect_depth(\"قارن بين السيارات الكهربائية والبنزين\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000033](../../tests/test_research_guardrails.py#L33) | 33 | `"    assert detect_depth(\"بحث شامل بالتفصيل عن الذهب\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000034](../../tests/test_research_guardrails.py#L34) | 34 | `""` | — |
| [SRC-01E35ABC46-L000035](../../tests/test_research_guardrails.py#L35) | 35 | `""` | — |
| [SRC-01E35ABC46-L000036](../../tests/test_research_guardrails.py#L36) | 36 | `"def test_depth_standard_ordinary_questions():"` | — |
| [SRC-01E35ABC46-L000037](../../tests/test_research_guardrails.py#L37) | 37 | `"    assert detect_depth(\"what is the capital of France\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000038](../../tests/test_research_guardrails.py#L38) | 38 | `"    assert detect_depth(\"ما عاصمة مصر\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000039](../../tests/test_research_guardrails.py#L39) | 39 | `"    assert detect_depth(\"I know about electric cars\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000040](../../tests/test_research_guardrails.py#L40) | 40 | `"    assert detect_depth(\"hello\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000041](../../tests/test_research_guardrails.py#L41) | 41 | `"    assert detect_depth(\"\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000042](../../tests/test_research_guardrails.py#L42) | 42 | `""` | — |
| [SRC-01E35ABC46-L000043](../../tests/test_research_guardrails.py#L43) | 43 | `""` | — |
| [SRC-01E35ABC46-L000044](../../tests/test_research_guardrails.py#L44) | 44 | `"def test_depth_does_not_trigger_on_partial_words():"` | — |
| [SRC-01E35ABC46-L000045](../../tests/test_research_guardrails.py#L45) | 45 | `"    # \"sources\" is a deep term; ensure isolated ordinary use still works via whole-word"` | — |
| [SRC-01E35ABC46-L000046](../../tests/test_research_guardrails.py#L46) | 46 | `"    assert detect_depth(\"the river sources of the Nile\") in {\"deep\", \"standard\"}  # may match"` | — |
| [SRC-01E35ABC46-L000047](../../tests/test_research_guardrails.py#L47) | 47 | `"    assert detect_depth(\"tell me a joke\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000048](../../tests/test_research_guardrails.py#L48) | 48 | `""` | — |
| [SRC-01E35ABC46-L000049](../../tests/test_research_guardrails.py#L49) | 49 | `""` | — |
| [SRC-01E35ABC46-L000050](../../tests/test_research_guardrails.py#L50) | 50 | `"# --- detect_freshness -------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000051](../../tests/test_research_guardrails.py#L51) | 51 | `""` | — |
| [SRC-01E35ABC46-L000052](../../tests/test_research_guardrails.py#L52) | 52 | `"def test_freshness_positive_english():"` | — |
| [SRC-01E35ABC46-L000053](../../tests/test_research_guardrails.py#L53) | 53 | `"    assert detect_freshness(\"what is happening now\") is True"` | — |
| [SRC-01E35ABC46-L000054](../../tests/test_research_guardrails.py#L54) | 54 | `"    assert detect_freshness(\"latest news about Egypt\") is True"` | — |
| [SRC-01E35ABC46-L000055](../../tests/test_research_guardrails.py#L55) | 55 | `"    assert detect_freshness(\"price today of gold\") is True"` | — |
| [SRC-01E35ABC46-L000056](../../tests/test_research_guardrails.py#L56) | 56 | `"    assert detect_freshness(\"breaking news\") is True"` | — |
| [SRC-01E35ABC46-L000057](../../tests/test_research_guardrails.py#L57) | 57 | `""` | — |
| [SRC-01E35ABC46-L000058](../../tests/test_research_guardrails.py#L58) | 58 | `""` | — |
| [SRC-01E35ABC46-L000059](../../tests/test_research_guardrails.py#L59) | 59 | `"def test_freshness_positive_arabic():"` | — |
| [SRC-01E35ABC46-L000060](../../tests/test_research_guardrails.py#L60) | 60 | `"    assert detect_freshness(\"ما هي آخر الأخبار عن الذهب\") is True"` | — |
| [SRC-01E35ABC46-L000061](../../tests/test_research_guardrails.py#L61) | 61 | `"    assert detect_freshness(\"سعر اليوم للدولار\") is True"` | — |
| [SRC-01E35ABC46-L000062](../../tests/test_research_guardrails.py#L62) | 62 | `"    assert detect_freshness(\"مستجدات السوق حاليا\") is True"` | — |
| [SRC-01E35ABC46-L000063](../../tests/test_research_guardrails.py#L63) | 63 | `""` | — |
| [SRC-01E35ABC46-L000064](../../tests/test_research_guardrails.py#L64) | 64 | `""` | — |
| [SRC-01E35ABC46-L000065](../../tests/test_research_guardrails.py#L65) | 65 | `"def test_freshness_negative_know_and_snowden():"` | — |
| [SRC-01E35ABC46-L000066](../../tests/test_research_guardrails.py#L66) | 66 | `"    assert detect_freshness(\"I know about cars\") is False"` | — |
| [SRC-01E35ABC46-L000067](../../tests/test_research_guardrails.py#L67) | 67 | `"    assert detect_freshness(\"Snowden revelations summary\") is False"` | — |
| [SRC-01E35ABC46-L000068](../../tests/test_research_guardrails.py#L68) | 68 | `"    assert detect_freshness(\"knowledge graph basics\") is False"` | — |
| [SRC-01E35ABC46-L000069](../../tests/test_research_guardrails.py#L69) | 69 | `"    assert detect_freshness(\"ما عاصمة فرنسا\") is False"` | — |
| [SRC-01E35ABC46-L000070](../../tests/test_research_guardrails.py#L70) | 70 | `""` | — |
| [SRC-01E35ABC46-L000071](../../tests/test_research_guardrails.py#L71) | 71 | `""` | — |
| [SRC-01E35ABC46-L000072](../../tests/test_research_guardrails.py#L72) | 72 | `"# --- relevance gate ---------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000073](../../tests/test_research_guardrails.py#L73) | 73 | `""` | — |
| [SRC-01E35ABC46-L000074](../../tests/test_research_guardrails.py#L74) | 74 | `"def test_relevance_keeps_matching_source():"` | — |
| [SRC-01E35ABC46-L000075](../../tests/test_research_guardrails.py#L75) | 75 | `"    src = {"` | — |
| [SRC-01E35ABC46-L000076](../../tests/test_research_guardrails.py#L76) | 76 | `"        \"title\": \"أسعار السيارات الكهربائية في مصر 2026\","` | — |
| [SRC-01E35ABC46-L000077](../../tests/test_research_guardrails.py#L77) | 77 | `"        \"url\": \"https://example.com/ev-egypt\","` | — |
| [SRC-01E35ABC46-L000078](../../tests/test_research_guardrails.py#L78) | 78 | `"        \"snippet\": \"ارتفعت حصة السيارات الكهربائية في السوق المصري هذا العام.\","` | — |
| [SRC-01E35ABC46-L000079](../../tests/test_research_guardrails.py#L79) | 79 | `"        \"domain\": \"example.com\","` | — |
| [SRC-01E35ABC46-L000080](../../tests/test_research_guardrails.py#L80) | 80 | `"        \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000081](../../tests/test_research_guardrails.py#L81) | 81 | `"        \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000082](../../tests/test_research_guardrails.py#L82) | 82 | `"    }"` | — |
| [SRC-01E35ABC46-L000083](../../tests/test_research_guardrails.py#L83) | 83 | `"    rel = source_relevance_score(src, \"أسعار السيارات الكهربائية في مصر\")"` | — |
| [SRC-01E35ABC46-L000084](../../tests/test_research_guardrails.py#L84) | 84 | `"    assert rel[\"accepted\"] is True"` | — |
| [SRC-01E35ABC46-L000085](../../tests/test_research_guardrails.py#L85) | 85 | `"    assert rel[\"score\"] >= 18"` | — |
| [SRC-01E35ABC46-L000086](../../tests/test_research_guardrails.py#L86) | 86 | `""` | — |
| [SRC-01E35ABC46-L000087](../../tests/test_research_guardrails.py#L87) | 87 | `"    # English-English match"` | — |
| [SRC-01E35ABC46-L000088](../../tests/test_research_guardrails.py#L88) | 88 | `"    src_en = {"` | — |
| [SRC-01E35ABC46-L000089](../../tests/test_research_guardrails.py#L89) | 89 | `"        \"title\": \"Electric vehicles in Egypt 2026\","` | — |
| [SRC-01E35ABC46-L000090](../../tests/test_research_guardrails.py#L90) | 90 | `"        \"url\": \"https://example.com/ev-egypt-en\","` | — |
| [SRC-01E35ABC46-L000091](../../tests/test_research_guardrails.py#L91) | 91 | `"        \"snippet\": \"Market share of electric cars in Egypt rose this year.\","` | — |
| [SRC-01E35ABC46-L000092](../../tests/test_research_guardrails.py#L92) | 92 | `"        \"domain\": \"example.com\","` | — |
| [SRC-01E35ABC46-L000093](../../tests/test_research_guardrails.py#L93) | 93 | `"        \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000094](../../tests/test_research_guardrails.py#L94) | 94 | `"        \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000095](../../tests/test_research_guardrails.py#L95) | 95 | `"    }"` | — |
| [SRC-01E35ABC46-L000096](../../tests/test_research_guardrails.py#L96) | 96 | `"    rel_en = source_relevance_score(src_en, \"electric vehicles Egypt market share\")"` | — |
| [SRC-01E35ABC46-L000097](../../tests/test_research_guardrails.py#L97) | 97 | `"    assert rel_en[\"accepted\"] is True"` | — |
| [SRC-01E35ABC46-L000098](../../tests/test_research_guardrails.py#L98) | 98 | `""` | — |
| [SRC-01E35ABC46-L000099](../../tests/test_research_guardrails.py#L99) | 99 | `""` | — |
| [SRC-01E35ABC46-L000100](../../tests/test_research_guardrails.py#L100) | 100 | `"def test_relevance_rejects_unrelated():"` | — |
| [SRC-01E35ABC46-L000101](../../tests/test_research_guardrails.py#L101) | 101 | `"    src = {"` | — |
| [SRC-01E35ABC46-L000102](../../tests/test_research_guardrails.py#L102) | 102 | `"        \"title\": \"Best pasta recipes\","` | — |
| [SRC-01E35ABC46-L000103](../../tests/test_research_guardrails.py#L103) | 103 | `"        \"url\": \"https://cooking.example/pasta\","` | — |
| [SRC-01E35ABC46-L000104](../../tests/test_research_guardrails.py#L104) | 104 | `"        \"snippet\": \"How to make carbonara at home with eggs and cheese.\","` | — |
| [SRC-01E35ABC46-L000105](../../tests/test_research_guardrails.py#L105) | 105 | `"        \"domain\": \"cooking.example\","` | — |
| [SRC-01E35ABC46-L000106](../../tests/test_research_guardrails.py#L106) | 106 | `"        \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000107](../../tests/test_research_guardrails.py#L107) | 107 | `"        \"providers\": [\"bing\"],"` | — |
| [SRC-01E35ABC46-L000108](../../tests/test_research_guardrails.py#L108) | 108 | `"    }"` | — |
| [SRC-01E35ABC46-L000109](../../tests/test_research_guardrails.py#L109) | 109 | `"    rel = source_relevance_score(src, \"أسعار السيارات الكهربائية في مصر\")"` | — |
| [SRC-01E35ABC46-L000110](../../tests/test_research_guardrails.py#L110) | 110 | `"    assert rel[\"accepted\"] is False"` | — |
| [SRC-01E35ABC46-L000111](../../tests/test_research_guardrails.py#L111) | 111 | `""` | — |
| [SRC-01E35ABC46-L000112](../../tests/test_research_guardrails.py#L112) | 112 | `""` | — |
| [SRC-01E35ABC46-L000113](../../tests/test_research_guardrails.py#L113) | 113 | `"def test_relevance_keeps_official_despite_wording():"` | — |
| [SRC-01E35ABC46-L000114](../../tests/test_research_guardrails.py#L114) | 114 | `"    src = {"` | — |
| [SRC-01E35ABC46-L000115](../../tests/test_research_guardrails.py#L115) | 115 | `"        \"title\": \"Official statistical bulletin Q1\","` | — |
| [SRC-01E35ABC46-L000116](../../tests/test_research_guardrails.py#L116) | 116 | `"        \"url\": \"https://www.capmas.gov.eg/bulletin\","` | — |
| [SRC-01E35ABC46-L000117](../../tests/test_research_guardrails.py#L117) | 117 | `"        \"snippet\": \"National statistics release.\","` | — |
| [SRC-01E35ABC46-L000118](../../tests/test_research_guardrails.py#L118) | 118 | `"        \"domain\": \"capmas.gov.eg\","` | — |
| [SRC-01E35ABC46-L000119](../../tests/test_research_guardrails.py#L119) | 119 | `"        \"source_class\": \"government\","` | — |
| [SRC-01E35ABC46-L000120](../../tests/test_research_guardrails.py#L120) | 120 | `"        \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000121](../../tests/test_research_guardrails.py#L121) | 121 | `"    }"` | — |
| [SRC-01E35ABC46-L000122](../../tests/test_research_guardrails.py#L122) | 122 | `"    rel = source_relevance_score(src, \"أسعار السيارات الكهربائية في مصر\")"` | — |
| [SRC-01E35ABC46-L000123](../../tests/test_research_guardrails.py#L123) | 123 | `"    assert rel[\"accepted\"] is True"` | — |
| [SRC-01E35ABC46-L000124](../../tests/test_research_guardrails.py#L124) | 124 | `"    assert rel[\"reason\"] in {\"accepted\", \"kept_official_despite_low_overlap\"}"` | — |
| [SRC-01E35ABC46-L000125](../../tests/test_research_guardrails.py#L125) | 125 | `""` | — |
| [SRC-01E35ABC46-L000126](../../tests/test_research_guardrails.py#L126) | 126 | `""` | — |
| [SRC-01E35ABC46-L000127](../../tests/test_research_guardrails.py#L127) | 127 | `"def test_filter_deduplicates():"` | — |
| [SRC-01E35ABC46-L000128](../../tests/test_research_guardrails.py#L128) | 128 | `"    sources = ["` | — |
| [SRC-01E35ABC46-L000129](../../tests/test_research_guardrails.py#L129) | 129 | `"        {"` | — |
| [SRC-01E35ABC46-L000130](../../tests/test_research_guardrails.py#L130) | 130 | `"            \"title\": \"Same Article Title\","` | — |
| [SRC-01E35ABC46-L000131](../../tests/test_research_guardrails.py#L131) | 131 | `"            \"url\": \"https://a.example/1\","` | — |
| [SRC-01E35ABC46-L000132](../../tests/test_research_guardrails.py#L132) | 132 | `"            \"snippet\": \"electric vehicles Egypt market\","` | — |
| [SRC-01E35ABC46-L000133](../../tests/test_research_guardrails.py#L133) | 133 | `"            \"domain\": \"a.example\","` | — |
| [SRC-01E35ABC46-L000134](../../tests/test_research_guardrails.py#L134) | 134 | `"            \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000135](../../tests/test_research_guardrails.py#L135) | 135 | `"            \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000136](../../tests/test_research_guardrails.py#L136) | 136 | `"        },"` | — |
| [SRC-01E35ABC46-L000137](../../tests/test_research_guardrails.py#L137) | 137 | `"        {"` | — |
| [SRC-01E35ABC46-L000138](../../tests/test_research_guardrails.py#L138) | 138 | `"            \"title\": \"Same Article Title\","` | — |
| [SRC-01E35ABC46-L000139](../../tests/test_research_guardrails.py#L139) | 139 | `"            \"url\": \"https://a.example/1?utm=x\","` | — |
| [SRC-01E35ABC46-L000140](../../tests/test_research_guardrails.py#L140) | 140 | `"            \"snippet\": \"electric vehicles Egypt market again\","` | — |
| [SRC-01E35ABC46-L000141](../../tests/test_research_guardrails.py#L141) | 141 | `"            \"domain\": \"a.example\","` | — |
| [SRC-01E35ABC46-L000142](../../tests/test_research_guardrails.py#L142) | 142 | `"            \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000143](../../tests/test_research_guardrails.py#L143) | 143 | `"            \"providers\": [\"bing\"],"` | — |
| [SRC-01E35ABC46-L000144](../../tests/test_research_guardrails.py#L144) | 144 | `"        },"` | — |
| [SRC-01E35ABC46-L000145](../../tests/test_research_guardrails.py#L145) | 145 | `"    ]"` | — |
| [SRC-01E35ABC46-L000146](../../tests/test_research_guardrails.py#L146) | 146 | `"    kept, diag = filter_relevant_sources("` | — |
| [SRC-01E35ABC46-L000147](../../tests/test_research_guardrails.py#L147) | 147 | `"        sources, \"electric vehicles Egypt\", [\"electric vehicles Egypt\"]"` | — |
| [SRC-01E35ABC46-L000148](../../tests/test_research_guardrails.py#L148) | 148 | `"    )"` | — |
| [SRC-01E35ABC46-L000149](../../tests/test_research_guardrails.py#L149) | 149 | `"    assert len(kept) == 1"` | — |
| [SRC-01E35ABC46-L000150](../../tests/test_research_guardrails.py#L150) | 150 | `"    assert any(d[\"reason\"] == \"duplicate_title_domain\" for d in diag)"` | — |
| [SRC-01E35ABC46-L000151](../../tests/test_research_guardrails.py#L151) | 151 | `""` | — |
| [SRC-01E35ABC46-L000152](../../tests/test_research_guardrails.py#L152) | 152 | `""` | — |
| [SRC-01E35ABC46-L000153](../../tests/test_research_guardrails.py#L153) | 153 | `"def test_filter_empty_and_failed_extract():"` | — |
| [SRC-01E35ABC46-L000154](../../tests/test_research_guardrails.py#L154) | 154 | `"    kept, diag = filter_relevant_sources([], \"anything\")"` | — |
| [SRC-01E35ABC46-L000155](../../tests/test_research_guardrails.py#L155) | 155 | `"    assert kept == []"` | — |
| [SRC-01E35ABC46-L000156](../../tests/test_research_guardrails.py#L156) | 156 | `"    assert diag == []"` | — |
| [SRC-01E35ABC46-L000157](../../tests/test_research_guardrails.py#L157) | 157 | `"    src = {"` | — |
| [SRC-01E35ABC46-L000158](../../tests/test_research_guardrails.py#L158) | 158 | `"        \"title\": \"\","` | — |
| [SRC-01E35ABC46-L000159](../../tests/test_research_guardrails.py#L159) | 159 | `"        \"url\": \"https://example.com/x\","` | — |
| [SRC-01E35ABC46-L000160](../../tests/test_research_guardrails.py#L160) | 160 | `"        \"snippet\": \"\","` | — |
| [SRC-01E35ABC46-L000161](../../tests/test_research_guardrails.py#L161) | 161 | `"        \"page_text\": \"\","` | — |
| [SRC-01E35ABC46-L000162](../../tests/test_research_guardrails.py#L162) | 162 | `"        \"domain\": \"example.com\","` | — |
| [SRC-01E35ABC46-L000163](../../tests/test_research_guardrails.py#L163) | 163 | `"        \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000164](../../tests/test_research_guardrails.py#L164) | 164 | `"        \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000165](../../tests/test_research_guardrails.py#L165) | 165 | `"    }"` | — |
| [SRC-01E35ABC46-L000166](../../tests/test_research_guardrails.py#L166) | 166 | `"    _kept2, diag2 = filter_relevant_sources([src], \"unrelated pasta recipes\")"` | — |
| [SRC-01E35ABC46-L000167](../../tests/test_research_guardrails.py#L167) | 167 | `"    # May reject for low overlap"` | — |
| [SRC-01E35ABC46-L000168](../../tests/test_research_guardrails.py#L168) | 168 | `"    assert isinstance(diag2, list)"` | — |
| [SRC-01E35ABC46-L000169](../../tests/test_research_guardrails.py#L169) | 169 | `""` | — |
| [SRC-01E35ABC46-L000170](../../tests/test_research_guardrails.py#L170) | 170 | `""` | — |
| [SRC-01E35ABC46-L000171](../../tests/test_research_guardrails.py#L171) | 171 | `"# --- evidence status --------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000172](../../tests/test_research_guardrails.py#L172) | 172 | `""` | — |
| [SRC-01E35ABC46-L000173](../../tests/test_research_guardrails.py#L173) | 173 | `"def test_evidence_adequate():"` | — |
| [SRC-01E35ABC46-L000174](../../tests/test_research_guardrails.py#L174) | 174 | `"    sources = ["` | — |
| [SRC-01E35ABC46-L000175](../../tests/test_research_guardrails.py#L175) | 175 | `"        {\"url\": f\"https://a{i}.example/p\", \"domain\": f\"a{i}.example\","` | — |
| [SRC-01E35ABC46-L000176](../../tests/test_research_guardrails.py#L176) | 176 | `"         \"snippet\": \"content\", \"page_fetched\": True, \"source_class\": \"general\"}"` | — |
| [SRC-01E35ABC46-L000177](../../tests/test_research_guardrails.py#L177) | 177 | `"        for i in range(4)"` | — |
| [SRC-01E35ABC46-L000178](../../tests/test_research_guardrails.py#L178) | 178 | `"    ]"` | — |
| [SRC-01E35ABC46-L000179](../../tests/test_research_guardrails.py#L179) | 179 | `"    sources[0][\"source_class\"] = \"government\""` | — |
| [SRC-01E35ABC46-L000180](../../tests/test_research_guardrails.py#L180) | 180 | `"    decision = decide_evidence_status(sources, pages_read=2)"` | — |
| [SRC-01E35ABC46-L000181](../../tests/test_research_guardrails.py#L181) | 181 | `"    assert decision[\"evidence_status\"] == \"adequate\""` | — |
| [SRC-01E35ABC46-L000182](../../tests/test_research_guardrails.py#L182) | 182 | `"    assert decision[\"should_abstain\"] is False"` | — |
| [SRC-01E35ABC46-L000183](../../tests/test_research_guardrails.py#L183) | 183 | `""` | — |
| [SRC-01E35ABC46-L000184](../../tests/test_research_guardrails.py#L184) | 184 | `""` | — |
| [SRC-01E35ABC46-L000185](../../tests/test_research_guardrails.py#L185) | 185 | `"def test_evidence_insufficient_empty():"` | — |
| [SRC-01E35ABC46-L000186](../../tests/test_research_guardrails.py#L186) | 186 | `"    decision = decide_evidence_status([], search_attempted=True)"` | — |
| [SRC-01E35ABC46-L000187](../../tests/test_research_guardrails.py#L187) | 187 | `"    assert decision[\"evidence_status\"] == \"insufficient\""` | — |
| [SRC-01E35ABC46-L000188](../../tests/test_research_guardrails.py#L188) | 188 | `"    assert decision[\"should_abstain\"] is True"` | — |
| [SRC-01E35ABC46-L000189](../../tests/test_research_guardrails.py#L189) | 189 | `""` | — |
| [SRC-01E35ABC46-L000190](../../tests/test_research_guardrails.py#L190) | 190 | `""` | — |
| [SRC-01E35ABC46-L000191](../../tests/test_research_guardrails.py#L191) | 191 | `"def test_evidence_failed_provider():"` | — |
| [SRC-01E35ABC46-L000192](../../tests/test_research_guardrails.py#L192) | 192 | `"    decision = decide_evidence_status([], provider_failures=2, search_attempted=True)"` | — |
| [SRC-01E35ABC46-L000193](../../tests/test_research_guardrails.py#L193) | 193 | `"    assert decision[\"evidence_status\"] == \"failed\""` | — |
| [SRC-01E35ABC46-L000194](../../tests/test_research_guardrails.py#L194) | 194 | `"    assert decision[\"should_abstain\"] is True"` | — |
| [SRC-01E35ABC46-L000195](../../tests/test_research_guardrails.py#L195) | 195 | `""` | — |
| [SRC-01E35ABC46-L000196](../../tests/test_research_guardrails.py#L196) | 196 | `""` | — |
| [SRC-01E35ABC46-L000197](../../tests/test_research_guardrails.py#L197) | 197 | `"def test_evidence_partial_single_source():"` | — |
| [SRC-01E35ABC46-L000198](../../tests/test_research_guardrails.py#L198) | 198 | `"    sources = ["` | — |
| [SRC-01E35ABC46-L000199](../../tests/test_research_guardrails.py#L199) | 199 | `"        {\"url\": \"https://a.example/p\", \"domain\": \"a.example\","` | — |
| [SRC-01E35ABC46-L000200](../../tests/test_research_guardrails.py#L200) | 200 | `"         \"snippet\": \"some text\", \"page_fetched\": True, \"source_class\": \"general\"}"` | — |
| [SRC-01E35ABC46-L000201](../../tests/test_research_guardrails.py#L201) | 201 | `"    ]"` | — |
| [SRC-01E35ABC46-L000202](../../tests/test_research_guardrails.py#L202) | 202 | `"    decision = decide_evidence_status(sources, pages_read=1)"` | — |
| [SRC-01E35ABC46-L000203](../../tests/test_research_guardrails.py#L203) | 203 | `"    assert decision[\"evidence_status\"] == \"partial\""` | — |
| [SRC-01E35ABC46-L000204](../../tests/test_research_guardrails.py#L204) | 204 | `"    assert decision[\"should_abstain\"] is False"` | — |
| [SRC-01E35ABC46-L000205](../../tests/test_research_guardrails.py#L205) | 205 | `""` | — |
| [SRC-01E35ABC46-L000206](../../tests/test_research_guardrails.py#L206) | 206 | `""` | — |
| [SRC-01E35ABC46-L000207](../../tests/test_research_guardrails.py#L207) | 207 | `""` | — |
| [SRC-01E35ABC46-L000208](../../tests/test_research_guardrails.py#L208) | 208 | `"# --- task-specific evidence guardrails ---------------------------------------"` | — |
| [SRC-01E35ABC46-L000209](../../tests/test_research_guardrails.py#L209) | 209 | `""` | — |
| [SRC-01E35ABC46-L000210](../../tests/test_research_guardrails.py#L210) | 210 | `"_GUARDRAIL_NOW = datetime(2026, 10, 28, 12, 0, tzinfo=UTC)"` | — |
| [SRC-01E35ABC46-L000211](../../tests/test_research_guardrails.py#L211) | 211 | `""` | — |
| [SRC-01E35ABC46-L000212](../../tests/test_research_guardrails.py#L212) | 212 | `""` | — |
| [SRC-01E35ABC46-L000213](../../tests/test_research_guardrails.py#L213) | 213 | `"def _guardrail_source("` | — |
| [SRC-01E35ABC46-L000214](../../tests/test_research_guardrails.py#L214) | 214 | `"    url: str,"` | — |
| [SRC-01E35ABC46-L000215](../../tests/test_research_guardrails.py#L215) | 215 | `"    *,"` | — |
| [SRC-01E35ABC46-L000216](../../tests/test_research_guardrails.py#L216) | 216 | `"    title: str = \"معلومات عن وزارة الاتصالات\","` | — |
| [SRC-01E35ABC46-L000217](../../tests/test_research_guardrails.py#L217) | 217 | `"    snippet: str = \"معلومات عن وزارة الاتصالات وتكنولوجيا المعلومات في مصر\","` | — |
| [SRC-01E35ABC46-L000218](../../tests/test_research_guardrails.py#L218) | 218 | `"    published_at: str = \"2026-10-27T10:00:00Z\","` | — |
| [SRC-01E35ABC46-L000219](../../tests/test_research_guardrails.py#L219) | 219 | `"    page_fetched: bool = True,"` | — |
| [SRC-01E35ABC46-L000220](../../tests/test_research_guardrails.py#L220) | 220 | `"    page_text: str = \"نص مقروء من الصفحة عن وزارة الاتصالات\","` | — |
| [SRC-01E35ABC46-L000221](../../tests/test_research_guardrails.py#L221) | 221 | `") -> dict:"` | — |
| [SRC-01E35ABC46-L000222](../../tests/test_research_guardrails.py#L222) | 222 | `"    return {"` | — |
| [SRC-01E35ABC46-L000223](../../tests/test_research_guardrails.py#L223) | 223 | `"        \"title\": title,"` | — |
| [SRC-01E35ABC46-L000224](../../tests/test_research_guardrails.py#L224) | 224 | `"        \"url\": url,"` | — |
| [SRC-01E35ABC46-L000225](../../tests/test_research_guardrails.py#L225) | 225 | `"        \"snippet\": snippet,"` | — |
| [SRC-01E35ABC46-L000226](../../tests/test_research_guardrails.py#L226) | 226 | `"        \"published_at\": published_at,"` | — |
| [SRC-01E35ABC46-L000227](../../tests/test_research_guardrails.py#L227) | 227 | `"        \"page_fetched\": page_fetched,"` | — |
| [SRC-01E35ABC46-L000228](../../tests/test_research_guardrails.py#L228) | 228 | `"        \"page_text\": page_text,"` | — |
| [SRC-01E35ABC46-L000229](../../tests/test_research_guardrails.py#L229) | 229 | `"    }"` | — |
| [SRC-01E35ABC46-L000230](../../tests/test_research_guardrails.py#L230) | 230 | `""` | — |
| [SRC-01E35ABC46-L000231](../../tests/test_research_guardrails.py#L231) | 231 | `""` | — |
| [SRC-01E35ABC46-L000232](../../tests/test_research_guardrails.py#L232) | 232 | `"def test_official_government_website_request_rejects_tourism_domain() -> None:"` | — |
| [SRC-01E35ABC46-L000233](../../tests/test_research_guardrails.py#L233) | 233 | `"    question = \"ابحث عن الموقع الرسمي لوزارة الاتصالات وتكنولوجيا المعلومات المصرية\""` | — |
| [SRC-01E35ABC46-L000234](../../tests/test_research_guardrails.py#L234) | 234 | `"    assert requires_official_government_domain(question)"` | — |
| [SRC-01E35ABC46-L000235](../../tests/test_research_guardrails.py#L235) | 235 | `"    candidates = ["` | — |
| [SRC-01E35ABC46-L000236](../../tests/test_research_guardrails.py#L236) | 236 | `"        _guardrail_source("` | — |
| [SRC-01E35ABC46-L000237](../../tests/test_research_guardrails.py#L237) | 237 | `"            \"https://visitegypt.com/\","` | — |
| [SRC-01E35ABC46-L000238](../../tests/test_research_guardrails.py#L238) | 238 | `"            title=\"وزارة الاتصالات في مصر ومعلومات سياحية\","` | — |
| [SRC-01E35ABC46-L000239](../../tests/test_research_guardrails.py#L239) | 239 | `"        ),"` | — |
| [SRC-01E35ABC46-L000240](../../tests/test_research_guardrails.py#L240) | 240 | `"        _guardrail_source("` | — |
| [SRC-01E35ABC46-L000241](../../tests/test_research_guardrails.py#L241) | 241 | `"            \"https://mcit.gov.eg/\","` | — |
| [SRC-01E35ABC46-L000242](../../tests/test_research_guardrails.py#L242) | 242 | `"            title=\"وزارة الاتصالات وتكنولوجيا المعلومات - الموقع الرسمي\","` | — |
| [SRC-01E35ABC46-L000243](../../tests/test_research_guardrails.py#L243) | 243 | `"        ),"` | — |
| [SRC-01E35ABC46-L000244](../../tests/test_research_guardrails.py#L244) | 244 | `"    ]"` | — |
| [SRC-01E35ABC46-L000245](../../tests/test_research_guardrails.py#L245) | 245 | `""` | — |
| [SRC-01E35ABC46-L000246](../../tests/test_research_guardrails.py#L246) | 246 | `"    accepted, report = apply_source_guardrails("` | — |
| [SRC-01E35ABC46-L000247](../../tests/test_research_guardrails.py#L247) | 247 | `"        question, \"auto\", {\"freshness\": \"any\"}, candidates, now=_GUARDRAIL_NOW"` | — |
| [SRC-01E35ABC46-L000248](../../tests/test_research_guardrails.py#L248) | 248 | `"    )"` | — |
| [SRC-01E35ABC46-L000249](../../tests/test_research_guardrails.py#L249) | 249 | `""` | — |
| [SRC-01E35ABC46-L000250](../../tests/test_research_guardrails.py#L250) | 250 | `"    assert [item[\"url\"] for item in accepted] == [\"https://mcit.gov.eg/\"]"` | — |
| [SRC-01E35ABC46-L000251](../../tests/test_research_guardrails.py#L251) | 251 | `"    assert report[\"official_government_domain_required\"] is True"` | — |
| [SRC-01E35ABC46-L000252](../../tests/test_research_guardrails.py#L252) | 252 | `"    assert report[\"rejection_counts\"] == {\"not_an_official_government_domain\": 1}"` | — |
| [SRC-01E35ABC46-L000253](../../tests/test_research_guardrails.py#L253) | 253 | `"    assert \"not independently verified\" in report[\"official_domain_policy\"]"` | — |
| [SRC-01E35ABC46-L000254](../../tests/test_research_guardrails.py#L254) | 254 | `""` | — |
| [SRC-01E35ABC46-L000255](../../tests/test_research_guardrails.py#L255) | 255 | `""` | — |
| [SRC-01E35ABC46-L000256](../../tests/test_research_guardrails.py#L256) | 256 | `"def test_official_request_fails_closed_when_only_non_government_result_exists() -> None:"` | — |
| [SRC-01E35ABC46-L000257](../../tests/test_research_guardrails.py#L257) | 257 | `"    accepted, report = apply_source_guardrails("` | — |
| [SRC-01E35ABC46-L000258](../../tests/test_research_guardrails.py#L258) | 258 | `"        \"الموقع الرسمي لوزارة الاتصالات المصرية\","` | — |
| [SRC-01E35ABC46-L000259](../../tests/test_research_guardrails.py#L259) | 259 | `"        \"auto\","` | — |
| [SRC-01E35ABC46-L000260](../../tests/test_research_guardrails.py#L260) | 260 | `"        {\"freshness\": \"any\"},"` | — |
| [SRC-01E35ABC46-L000261](../../tests/test_research_guardrails.py#L261) | 261 | `"        [_guardrail_source(\"https://visitegypt.com/\")],"` | — |
| [SRC-01E35ABC46-L000262](../../tests/test_research_guardrails.py#L262) | 262 | `"        now=_GUARDRAIL_NOW,"` | — |
| [SRC-01E35ABC46-L000263](../../tests/test_research_guardrails.py#L263) | 263 | `"    )"` | — |
| [SRC-01E35ABC46-L000264](../../tests/test_research_guardrails.py#L264) | 264 | `""` | — |
| [SRC-01E35ABC46-L000265](../../tests/test_research_guardrails.py#L265) | 265 | `"    assert accepted == []"` | — |
| [SRC-01E35ABC46-L000266](../../tests/test_research_guardrails.py#L266) | 266 | `"    assert report[\"accepted_sources\"] == 0"` | — |
| [SRC-01E35ABC46-L000267](../../tests/test_research_guardrails.py#L267) | 267 | `"    assert report[\"current_evidence_status\"] == \"not_required\""` | — |
| [SRC-01E35ABC46-L000268](../../tests/test_research_guardrails.py#L268) | 268 | `""` | — |
| [SRC-01E35ABC46-L000269](../../tests/test_research_guardrails.py#L269) | 269 | `""` | — |
| [SRC-01E35ABC46-L000270](../../tests/test_research_guardrails.py#L270) | 270 | `"def test_current_evidence_requires_recent_date_and_readable_page() -> None:"` | — |
| [SRC-01E35ABC46-L000271](../../tests/test_research_guardrails.py#L271) | 271 | `"    recent = _guardrail_source(\"https://example.com/current\")"` | — |
| [SRC-01E35ABC46-L000272](../../tests/test_research_guardrails.py#L272) | 272 | `"    stale = _guardrail_source("` | — |
| [SRC-01E35ABC46-L000273](../../tests/test_research_guardrails.py#L273) | 273 | `"        \"https://example.org/old\", published_at=\"2024-06-01T10:00:00Z\""` | — |
| [SRC-01E35ABC46-L000274](../../tests/test_research_guardrails.py#L274) | 274 | `"    )"` | — |
| [SRC-01E35ABC46-L000275](../../tests/test_research_guardrails.py#L275) | 275 | `"    undated = _guardrail_source(\"https://example.net/undated\", published_at=\"\")"` | — |
| [SRC-01E35ABC46-L000276](../../tests/test_research_guardrails.py#L276) | 276 | `"    unread = _guardrail_source("` | — |
| [SRC-01E35ABC46-L000277](../../tests/test_research_guardrails.py#L277) | 277 | `"        \"https://example.edu/unread\", page_fetched=False, page_text=\"\""` | — |
| [SRC-01E35ABC46-L000278](../../tests/test_research_guardrails.py#L278) | 278 | `"    )"` | — |
| [SRC-01E35ABC46-L000279](../../tests/test_research_guardrails.py#L279) | 279 | `""` | — |
| [SRC-01E35ABC46-L000280](../../tests/test_research_guardrails.py#L280) | 280 | `"    assert assess_current_source(recent, now=_GUARDRAIL_NOW)[\"eligible\"] is True"` | — |
| [SRC-01E35ABC46-L000281](../../tests/test_research_guardrails.py#L281) | 281 | `"    assert assess_current_source(stale, now=_GUARDRAIL_NOW)[\"status\"] == \"stale\""` | — |
| [SRC-01E35ABC46-L000282](../../tests/test_research_guardrails.py#L282) | 282 | `"    assert assess_current_source(undated, now=_GUARDRAIL_NOW)[\"status\"] == \"date_unavailable\""` | — |
| [SRC-01E35ABC46-L000283](../../tests/test_research_guardrails.py#L283) | 283 | `"    assert assess_current_source(unread, now=_GUARDRAIL_NOW)[\"status\"] == \"page_not_read\""` | — |
| [SRC-01E35ABC46-L000284](../../tests/test_research_guardrails.py#L284) | 284 | `""` | — |
| [SRC-01E35ABC46-L000285](../../tests/test_research_guardrails.py#L285) | 285 | `""` | — |
| [SRC-01E35ABC46-L000286](../../tests/test_research_guardrails.py#L286) | 286 | `"def test_latest_mode_excludes_old_undated_and_unread_pages() -> None:"` | — |
| [SRC-01E35ABC46-L000287](../../tests/test_research_guardrails.py#L287) | 287 | `"    candidates = ["` | — |
| [SRC-01E35ABC46-L000288](../../tests/test_research_guardrails.py#L288) | 288 | `"        _guardrail_source(\"https://example.com/recent\"),"` | — |
| [SRC-01E35ABC46-L000289](../../tests/test_research_guardrails.py#L289) | 289 | `"        _guardrail_source("` | — |
| [SRC-01E35ABC46-L000290](../../tests/test_research_guardrails.py#L290) | 290 | `"            \"https://example.org/old\", published_at=\"2023-11-15T10:00:00Z\""` | — |
| [SRC-01E35ABC46-L000291](../../tests/test_research_guardrails.py#L291) | 291 | `"        ),"` | — |
| [SRC-01E35ABC46-L000292](../../tests/test_research_guardrails.py#L292) | 292 | `"        _guardrail_source(\"https://example.net/undated\", published_at=\"\"),"` | — |
| [SRC-01E35ABC46-L000293](../../tests/test_research_guardrails.py#L293) | 293 | `"        _guardrail_source("` | — |
| [SRC-01E35ABC46-L000294](../../tests/test_research_guardrails.py#L294) | 294 | `"            \"https://example.edu/unread\", page_fetched=False, page_text=\"\""` | — |
| [SRC-01E35ABC46-L000295](../../tests/test_research_guardrails.py#L295) | 295 | `"        ),"` | — |
| [SRC-01E35ABC46-L000296](../../tests/test_research_guardrails.py#L296) | 296 | `"    ]"` | — |
| [SRC-01E35ABC46-L000297](../../tests/test_research_guardrails.py#L297) | 297 | `"    accepted, report = apply_source_guardrails("` | — |
| [SRC-01E35ABC46-L000298](../../tests/test_research_guardrails.py#L298) | 298 | `"        \"سعر الذهب اليوم في مصر\","` | — |
| [SRC-01E35ABC46-L000299](../../tests/test_research_guardrails.py#L299) | 299 | `"        \"latest\","` | — |
| [SRC-01E35ABC46-L000300](../../tests/test_research_guardrails.py#L300) | 300 | `"        {\"freshness\": \"current\"},"` | — |
| [SRC-01E35ABC46-L000301](../../tests/test_research_guardrails.py#L301) | 301 | `"        candidates,"` | — |
| [SRC-01E35ABC46-L000302](../../tests/test_research_guardrails.py#L302) | 302 | `"        now=_GUARDRAIL_NOW,"` | — |
| [SRC-01E35ABC46-L000303](../../tests/test_research_guardrails.py#L303) | 303 | `"    )"` | — |
| [SRC-01E35ABC46-L000304](../../tests/test_research_guardrails.py#L304) | 304 | `""` | — |
| [SRC-01E35ABC46-L000305](../../tests/test_research_guardrails.py#L305) | 305 | `"    assert [item[\"url\"] for item in accepted] == [\"https://example.com/recent\"]"` | — |
| [SRC-01E35ABC46-L000306](../../tests/test_research_guardrails.py#L306) | 306 | `"    assert report[\"current_evidence_required\"] is True"` | — |
| [SRC-01E35ABC46-L000307](../../tests/test_research_guardrails.py#L307) | 307 | `"    assert report[\"current_evidence_status\"] == \"eligible_recent_read_pages_only\""` | — |
| [SRC-01E35ABC46-L000308](../../tests/test_research_guardrails.py#L308) | 308 | `"    assert report[\"rejection_counts\"] == {"` | — |
| [SRC-01E35ABC46-L000309](../../tests/test_research_guardrails.py#L309) | 309 | `"        \"stale\": 1,"` | — |
| [SRC-01E35ABC46-L000310](../../tests/test_research_guardrails.py#L310) | 310 | `"        \"date_unavailable\": 1,"` | — |
| [SRC-01E35ABC46-L000311](../../tests/test_research_guardrails.py#L311) | 311 | `"        \"page_not_read\": 1,"` | — |
| [SRC-01E35ABC46-L000312](../../tests/test_research_guardrails.py#L312) | 312 | `"    }"` | — |
| [SRC-01E35ABC46-L000313](../../tests/test_research_guardrails.py#L313) | 313 | `""` | — |
| [SRC-01E35ABC46-L000314](../../tests/test_research_guardrails.py#L314) | 314 | `""` | — |
| [SRC-01E35ABC46-L000315](../../tests/test_research_guardrails.py#L315) | 315 | `"def test_official_site_navigation_does_not_require_news_publication_date() -> None:"` | — |
| [SRC-01E35ABC46-L000316](../../tests/test_research_guardrails.py#L316) | 316 | `"    question = \"ابحث عن الموقع الرسمي لوزارة الاتصالات وتكنولوجيا المعلومات المصرية\""` | — |
| [SRC-01E35ABC46-L000317](../../tests/test_research_guardrails.py#L317) | 317 | `"    official_page = _guardrail_source("` | — |
| [SRC-01E35ABC46-L000318](../../tests/test_research_guardrails.py#L318) | 318 | `"        \"https://mcit.gov.eg/\","` | — |
| [SRC-01E35ABC46-L000319](../../tests/test_research_guardrails.py#L319) | 319 | `"        published_at=\"\","` | — |
| [SRC-01E35ABC46-L000320](../../tests/test_research_guardrails.py#L320) | 320 | `"        title=\"وزارة الاتصالات وتكنولوجيا المعلومات - الموقع الرسمي\","` | — |
| [SRC-01E35ABC46-L000321](../../tests/test_research_guardrails.py#L321) | 321 | `"    )"` | — |
| [SRC-01E35ABC46-L000322](../../tests/test_research_guardrails.py#L322) | 322 | `""` | — |
| [SRC-01E35ABC46-L000323](../../tests/test_research_guardrails.py#L323) | 323 | `"    accepted, report = apply_source_guardrails("` | — |
| [SRC-01E35ABC46-L000324](../../tests/test_research_guardrails.py#L324) | 324 | `"        question,"` | — |
| [SRC-01E35ABC46-L000325](../../tests/test_research_guardrails.py#L325) | 325 | `"        \"latest\","` | — |
| [SRC-01E35ABC46-L000326](../../tests/test_research_guardrails.py#L326) | 326 | `"        {\"freshness\": \"current\"},"` | — |
| [SRC-01E35ABC46-L000327](../../tests/test_research_guardrails.py#L327) | 327 | `"        [official_page],"` | — |
| [SRC-01E35ABC46-L000328](../../tests/test_research_guardrails.py#L328) | 328 | `"        now=_GUARDRAIL_NOW,"` | — |
| [SRC-01E35ABC46-L000329](../../tests/test_research_guardrails.py#L329) | 329 | `"    )"` | — |
| [SRC-01E35ABC46-L000330](../../tests/test_research_guardrails.py#L330) | 330 | `""` | — |
| [SRC-01E35ABC46-L000331](../../tests/test_research_guardrails.py#L331) | 331 | `"    assert len(accepted) == 1"` | — |
| [SRC-01E35ABC46-L000332](../../tests/test_research_guardrails.py#L332) | 332 | `"    assert report[\"current_evidence_required\"] is False"` | — |
| [SRC-01E35ABC46-L000333](../../tests/test_research_guardrails.py#L333) | 333 | `""` | — |
| [SRC-01E35ABC46-L000334](../../tests/test_research_guardrails.py#L334) | 334 | `""` | — |
| [SRC-01E35ABC46-L000335](../../tests/test_research_guardrails.py#L335) | 335 | `"def test_social_mode_rejects_non_social_sources_and_classifies_public_posts() -> None:"` | — |
| [SRC-01E35ABC46-L000336](../../tests/test_research_guardrails.py#L336) | 336 | `"    question = \"اجمع آراء وتجارب الناس حول نيسان صني 2022 في مصر\""` | — |
| [SRC-01E35ABC46-L000337](../../tests/test_research_guardrails.py#L337) | 337 | `"    personal_post = _guardrail_source("` | — |
| [SRC-01E35ABC46-L000338](../../tests/test_research_guardrails.py#L338) | 338 | `"        \"https://www.reddit.com/r/cars/comments/example\","` | — |
| [SRC-01E35ABC46-L000339](../../tests/test_research_guardrails.py#L339) | 339 | `"        title=\"تجربتي مع نيسان صني\","` | — |
| [SRC-01E35ABC46-L000340](../../tests/test_research_guardrails.py#L340) | 340 | `"        snippet=\"أنا امتلك السيارة واستخدمتها يوميًا لمدة عام\","` | — |
| [SRC-01E35ABC46-L000341](../../tests/test_research_guardrails.py#L341) | 341 | `"    )"` | — |
| [SRC-01E35ABC46-L000342](../../tests/test_research_guardrails.py#L342) | 342 | `"    promotional_post = _guardrail_source("` | — |
| [SRC-01E35ABC46-L000343](../../tests/test_research_guardrails.py#L343) | 343 | `"        \"https://www.reddit.com/r/cars/comments/ad\","` | — |
| [SRC-01E35ABC46-L000344](../../tests/test_research_guardrails.py#L344) | 344 | `"        title=\"نيسان صني 2022 للبيع\","` | — |
| [SRC-01E35ABC46-L000345](../../tests/test_research_guardrails.py#L345) | 345 | `"        snippet=\"سعر خاص، تواصل معنا عبر واتساب\","` | — |
| [SRC-01E35ABC46-L000346](../../tests/test_research_guardrails.py#L346) | 346 | `"    )"` | — |
| [SRC-01E35ABC46-L000347](../../tests/test_research_guardrails.py#L347) | 347 | `"    editorial_review = _guardrail_source("` | — |
| [SRC-01E35ABC46-L000348](../../tests/test_research_guardrails.py#L348) | 348 | `"        \"https://example.com/car-review\","` | — |
| [SRC-01E35ABC46-L000349](../../tests/test_research_guardrails.py#L349) | 349 | `"        title=\"مراجعة نيسان صني\","` | — |
| [SRC-01E35ABC46-L000350](../../tests/test_research_guardrails.py#L350) | 350 | `"    )"` | — |
| [SRC-01E35ABC46-L000351](../../tests/test_research_guardrails.py#L351) | 351 | `""` | — |
| [SRC-01E35ABC46-L000352](../../tests/test_research_guardrails.py#L352) | 352 | `"    accepted, report = apply_source_guardrails("` | — |
| [SRC-01E35ABC46-L000353](../../tests/test_research_guardrails.py#L353) | 353 | `"        question,"` | — |
| [SRC-01E35ABC46-L000354](../../tests/test_research_guardrails.py#L354) | 354 | `"        \"social\","` | — |
| [SRC-01E35ABC46-L000355](../../tests/test_research_guardrails.py#L355) | 355 | `"        {\"social_focus\": True, \"freshness\": \"any\"},"` | — |
| [SRC-01E35ABC46-L000356](../../tests/test_research_guardrails.py#L356) | 356 | `"        [personal_post, promotional_post, editorial_review],"` | — |
| [SRC-01E35ABC46-L000357](../../tests/test_research_guardrails.py#L357) | 357 | `"        now=_GUARDRAIL_NOW,"` | — |
| [SRC-01E35ABC46-L000358](../../tests/test_research_guardrails.py#L358) | 358 | `"    )"` | — |
| [SRC-01E35ABC46-L000359](../../tests/test_research_guardrails.py#L359) | 359 | `""` | — |
| [SRC-01E35ABC46-L000360](../../tests/test_research_guardrails.py#L360) | 360 | `"    labels = {item[\"url\"]: item[\"opinion_source_classification\"] for item in accepted}"` | — |
| [SRC-01E35ABC46-L000361](../../tests/test_research_guardrails.py#L361) | 361 | `"    assert labels[personal_post[\"url\"]] == \"personal_experience_candidate\""` | — |
| [SRC-01E35ABC46-L000362](../../tests/test_research_guardrails.py#L362) | 362 | `"    assert labels[promotional_post[\"url\"]] == \"promotional_or_commercial\""` | — |
| [SRC-01E35ABC46-L000363](../../tests/test_research_guardrails.py#L363) | 363 | `"    assert editorial_review[\"url\"] not in labels"` | — |
| [SRC-01E35ABC46-L000364](../../tests/test_research_guardrails.py#L364) | 364 | `"    assert report[\"social_platform_only\"] is True"` | — |
| [SRC-01E35ABC46-L000365](../../tests/test_research_guardrails.py#L365) | 365 | `"    assert report[\"rejection_counts\"] == {\"not_a_social_platform_source\": 1}"` | — |
| [SRC-01E35ABC46-L000366](../../tests/test_research_guardrails.py#L366) | 366 | `"    assert all("` | — |
| [SRC-01E35ABC46-L000367](../../tests/test_research_guardrails.py#L367) | 367 | `"        item[\"opinion_classification_method\"] == \"heuristic_only\""` | — |
| [SRC-01E35ABC46-L000368](../../tests/test_research_guardrails.py#L368) | 368 | `"        for item in accepted"` | — |
| [SRC-01E35ABC46-L000369](../../tests/test_research_guardrails.py#L369) | 369 | `"    )"` | — |
| [SRC-01E35ABC46-L000370](../../tests/test_research_guardrails.py#L370) | 370 | `""` | — |
| [SRC-01E35ABC46-L000371](../../tests/test_research_guardrails.py#L371) | 371 | `""` | — |
| [SRC-01E35ABC46-L000372](../../tests/test_research_guardrails.py#L372) | 372 | `"def test_social_classification_does_not_claim_unknown_post_is_verified_experience() -> None:"` | — |
| [SRC-01E35ABC46-L000373](../../tests/test_research_guardrails.py#L373) | 373 | `"    result = classify_social_source("` | — |
| [SRC-01E35ABC46-L000374](../../tests/test_research_guardrails.py#L374) | 374 | `"        _guardrail_source("` | — |
| [SRC-01E35ABC46-L000375](../../tests/test_research_guardrails.py#L375) | 375 | `"            \"https://www.youtube.com/watch?v=example\","` | — |
| [SRC-01E35ABC46-L000376](../../tests/test_research_guardrails.py#L376) | 376 | `"            title=\"Nissan Sunny 2022\","` | — |
| [SRC-01E35ABC46-L000377](../../tests/test_research_guardrails.py#L377) | 377 | `"            snippet=\"معلومات ومقاطع عن السيارة\","` | — |
| [SRC-01E35ABC46-L000378](../../tests/test_research_guardrails.py#L378) | 378 | `"        )"` | — |
| [SRC-01E35ABC46-L000379](../../tests/test_research_guardrails.py#L379) | 379 | `"    )"` | — |
| [SRC-01E35ABC46-L000380](../../tests/test_research_guardrails.py#L380) | 380 | `""` | — |
| [SRC-01E35ABC46-L000381](../../tests/test_research_guardrails.py#L381) | 381 | `"    assert result[\"opinion_source_classification\"] == \"social_post_unclassified\""` | — |
| [SRC-01E35ABC46-L000382](../../tests/test_research_guardrails.py#L382) | 382 | `"    assert result[\"opinion_classification_method\"] == \"heuristic_only\""` | — |
| [SRC-01E35ABC46-L000383](../../tests/test_research_guardrails.py#L383) | 383 | `"    assert \"manual review\" in result[\"opinion_classification_basis\"]"` | — |
| [SRC-01E35ABC46-L000384](../../tests/test_research_guardrails.py#L384) | 384 | `""` | — |
| [SRC-01E35ABC46-L000385](../../tests/test_research_guardrails.py#L385) | 385 | `""` | — |
| [SRC-01E35ABC46-L000386](../../tests/test_research_guardrails.py#L386) | 386 | `"def test_today_query_requires_current_evidence_even_in_auto_mode() -> None:"` | — |
| [SRC-01E35ABC46-L000387](../../tests/test_research_guardrails.py#L387) | 387 | `"    accepted, report = apply_source_guardrails("` | — |
| [SRC-01E35ABC46-L000388](../../tests/test_research_guardrails.py#L388) | 388 | `"        \"ما مواعيد العمل اليوم؟\","` | — |
| [SRC-01E35ABC46-L000389](../../tests/test_research_guardrails.py#L389) | 389 | `"        \"auto\","` | — |
| [SRC-01E35ABC46-L000390](../../tests/test_research_guardrails.py#L390) | 390 | `"        {\"freshness\": \"current\"},"` | — |
| [SRC-01E35ABC46-L000391](../../tests/test_research_guardrails.py#L391) | 391 | `"        ["` | — |
| [SRC-01E35ABC46-L000392](../../tests/test_research_guardrails.py#L392) | 392 | `"            _guardrail_source("` | — |
| [SRC-01E35ABC46-L000393](../../tests/test_research_guardrails.py#L393) | 393 | `"                \"https://example.com/old\", published_at=\"2024-01-01T10:00:00Z\""` | — |
| [SRC-01E35ABC46-L000394](../../tests/test_research_guardrails.py#L394) | 394 | `"            )"` | — |
| [SRC-01E35ABC46-L000395](../../tests/test_research_guardrails.py#L395) | 395 | `"        ],"` | — |
| [SRC-01E35ABC46-L000396](../../tests/test_research_guardrails.py#L396) | 396 | `"        now=_GUARDRAIL_NOW,"` | — |
| [SRC-01E35ABC46-L000397](../../tests/test_research_guardrails.py#L397) | 397 | `"    )"` | — |
| [SRC-01E35ABC46-L000398](../../tests/test_research_guardrails.py#L398) | 398 | `""` | — |
| [SRC-01E35ABC46-L000399](../../tests/test_research_guardrails.py#L399) | 399 | `"    assert accepted == []"` | — |
| [SRC-01E35ABC46-L000400](../../tests/test_research_guardrails.py#L400) | 400 | `"    assert report[\"current_evidence_required\"] is True"` | — |
| [SRC-01E35ABC46-L000401](../../tests/test_research_guardrails.py#L401) | 401 | `"    assert report[\"rejection_counts\"] == {\"stale\": 1}"` | — |
| [SRC-01E35ABC46-L000402](../../tests/test_research_guardrails.py#L402) | 402 | `""` | — |
| [SRC-01E35ABC46-L000403](../../tests/test_research_guardrails.py#L403) | 403 | `""` | — |
| [SRC-01E35ABC46-L000404](../../tests/test_research_guardrails.py#L404) | 404 | `"def test_recent_source_date_is_not_enough_without_readable_page_text() -> None:"` | — |
| [SRC-01E35ABC46-L000405](../../tests/test_research_guardrails.py#L405) | 405 | `"    item = _guardrail_source("` | — |
| [SRC-01E35ABC46-L000406](../../tests/test_research_guardrails.py#L406) | 406 | `"        \"https://example.com/unread\","` | — |
| [SRC-01E35ABC46-L000407](../../tests/test_research_guardrails.py#L407) | 407 | `"        published_at=\"2026-10-27T10:00:00Z\","` | — |
| [SRC-01E35ABC46-L000408](../../tests/test_research_guardrails.py#L408) | 408 | `"        page_fetched=True,"` | — |
| [SRC-01E35ABC46-L000409](../../tests/test_research_guardrails.py#L409) | 409 | `"        page_text=\"   \","` | — |
| [SRC-01E35ABC46-L000410](../../tests/test_research_guardrails.py#L410) | 410 | `"    )"` | — |
| [SRC-01E35ABC46-L000411](../../tests/test_research_guardrails.py#L411) | 411 | `"    assert assess_current_source(item, now=_GUARDRAIL_NOW)[\"status\"] == \"page_not_read\""` | — |
| [SRC-01E35ABC46-L000412](../../tests/test_research_guardrails.py#L412) | 412 | `""` | — |
| [SRC-01E35ABC46-L000413](../../tests/test_research_guardrails.py#L413) | 413 | `""` | — |
| [SRC-01E35ABC46-L000414](../../tests/test_research_guardrails.py#L414) | 414 | `""` | — |
| [SRC-01E35ABC46-L000415](../../tests/test_research_guardrails.py#L415) | 415 | `"def test_social_classification_matches_english_first_person_phrases_case_insensitively() -> None:"` | — |
| [SRC-01E35ABC46-L000416](../../tests/test_research_guardrails.py#L416) | 416 | `"    result = classify_social_source("` | — |
| [SRC-01E35ABC46-L000417](../../tests/test_research_guardrails.py#L417) | 417 | `"        _guardrail_source("` | — |
| [SRC-01E35ABC46-L000418](../../tests/test_research_guardrails.py#L418) | 418 | `"            \"https://www.reddit.com/r/cars/comments/owner\","` | — |
| [SRC-01E35ABC46-L000419](../../tests/test_research_guardrails.py#L419) | 419 | `"            title=\"Nissan Sunny ownership\","` | — |
| [SRC-01E35ABC46-L000420](../../tests/test_research_guardrails.py#L420) | 420 | `"            snippet=\"I OWN the car and I use it for my daily commute\","` | — |
| [SRC-01E35ABC46-L000421](../../tests/test_research_guardrails.py#L421) | 421 | `"        )"` | — |
| [SRC-01E35ABC46-L000422](../../tests/test_research_guardrails.py#L422) | 422 | `"    )"` | — |
| [SRC-01E35ABC46-L000423](../../tests/test_research_guardrails.py#L423) | 423 | `""` | — |
| [SRC-01E35ABC46-L000424](../../tests/test_research_guardrails.py#L424) | 424 | `"    assert result[\"opinion_source_classification\"] == \"personal_experience_candidate\""` | — |
| [SRC-01E35ABC46-L000425](../../tests/test_research_guardrails.py#L425) | 425 | `""` | — |
| [SRC-01E35ABC46-L000426](../../tests/test_research_guardrails.py#L426) | 426 | `""` | — |
| [SRC-01E35ABC46-L000427](../../tests/test_research_guardrails.py#L427) | 427 | `"def test_official_domain_check_rejects_suffix_spoofing() -> None:"` | — |
| [SRC-01E35ABC46-L000428](../../tests/test_research_guardrails.py#L428) | 428 | `"    question = \"ابحث عن الموقع الرسمي لوزارة الاتصالات المصرية\""` | — |
| [SRC-01E35ABC46-L000429](../../tests/test_research_guardrails.py#L429) | 429 | `"    accepted, report = apply_source_guardrails("` | — |
| [SRC-01E35ABC46-L000430](../../tests/test_research_guardrails.py#L430) | 430 | `"        question,"` | — |
| [SRC-01E35ABC46-L000431](../../tests/test_research_guardrails.py#L431) | 431 | `"        \"auto\","` | — |
| [SRC-01E35ABC46-L000432](../../tests/test_research_guardrails.py#L432) | 432 | `"        {\"freshness\": \"any\"},"` | — |
| [SRC-01E35ABC46-L000433](../../tests/test_research_guardrails.py#L433) | 433 | `"        ["` | — |
| [SRC-01E35ABC46-L000434](../../tests/test_research_guardrails.py#L434) | 434 | `"            _guardrail_source("` | — |
| [SRC-01E35ABC46-L000435](../../tests/test_research_guardrails.py#L435) | 435 | `"                \"https://mcit.gov.eg.attacker.example/\","` | — |
| [SRC-01E35ABC46-L000436](../../tests/test_research_guardrails.py#L436) | 436 | `"                title=\"وزارة الاتصالات المصرية الموقع الرسمي\","` | — |
| [SRC-01E35ABC46-L000437](../../tests/test_research_guardrails.py#L437) | 437 | `"            )"` | — |
| [SRC-01E35ABC46-L000438](../../tests/test_research_guardrails.py#L438) | 438 | `"        ],"` | — |
| [SRC-01E35ABC46-L000439](../../tests/test_research_guardrails.py#L439) | 439 | `"        now=_GUARDRAIL_NOW,"` | — |
| [SRC-01E35ABC46-L000440](../../tests/test_research_guardrails.py#L440) | 440 | `"    )"` | — |
| [SRC-01E35ABC46-L000441](../../tests/test_research_guardrails.py#L441) | 441 | `""` | — |
| [SRC-01E35ABC46-L000442](../../tests/test_research_guardrails.py#L442) | 442 | `"    assert accepted == []"` | — |
| [SRC-01E35ABC46-L000443](../../tests/test_research_guardrails.py#L443) | 443 | `"    assert report[\"rejection_counts\"] == {\"not_an_official_government_domain\": 1}"` | — |
| [SRC-01E35ABC46-L000444](../../tests/test_research_guardrails.py#L444) | 444 | `""` | — |
| [SRC-01E35ABC46-L000445](../../tests/test_research_guardrails.py#L445) | 445 | `""` | — |
| [SRC-01E35ABC46-L000446](../../tests/test_research_guardrails.py#L446) | 446 | `""` | — |
| [SRC-01E35ABC46-L000447](../../tests/test_research_guardrails.py#L447) | 447 | `"def test_current_government_office_hours_require_official_fresh_page_in_auto_mode() -> None:"` | — |
| [SRC-01E35ABC46-L000448](../../tests/test_research_guardrails.py#L448) | 448 | `"    question = \"مواعيد عمل مكتب الجوازات بالعباسية اليوم\""` | — |
| [SRC-01E35ABC46-L000449](../../tests/test_research_guardrails.py#L449) | 449 | `"    assert requires_official_current_government_source(question)"` | — |
