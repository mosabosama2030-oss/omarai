# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **044**
- سجلات الأسطر: **800**
- النطاق: SRC-01E35ABC46-L000099 إلى SRC-D033B34F41-L000064
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-01E35ABC46 — [tests/test_research_guardrails.py](../../tests/test_research_guardrails.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-01E35ABC46-L000450](../../tests/test_research_guardrails.py#L450) | 450 | `"    candidates = ["` | — |
| [SRC-01E35ABC46-L000451](../../tests/test_research_guardrails.py#L451) | 451 | `"        _guardrail_source("` | — |
| [SRC-01E35ABC46-L000452](../../tests/test_research_guardrails.py#L452) | 452 | `"            \"https://news.example.com/passport-hours\","` | — |
| [SRC-01E35ABC46-L000453](../../tests/test_research_guardrails.py#L453) | 453 | `"            title=\"مواعيد الجوازات اليوم\","` | — |
| [SRC-01E35ABC46-L000454](../../tests/test_research_guardrails.py#L454) | 454 | `"            snippet=\"ساعات العمل الحالية لمكتب الجوازات\","` | — |
| [SRC-01E35ABC46-L000455](../../tests/test_research_guardrails.py#L455) | 455 | `"        ),"` | — |
| [SRC-01E35ABC46-L000456](../../tests/test_research_guardrails.py#L456) | 456 | `"        _guardrail_source("` | — |
| [SRC-01E35ABC46-L000457](../../tests/test_research_guardrails.py#L457) | 457 | `"            \"https://moi.gov.eg/\","` | — |
| [SRC-01E35ABC46-L000458](../../tests/test_research_guardrails.py#L458) | 458 | `"            title=\"بوابة وزارة الداخلية\","` | — |
| [SRC-01E35ABC46-L000459](../../tests/test_research_guardrails.py#L459) | 459 | `"            snippet=\"مواعيد عمل خدمات الجوازات\","` | — |
| [SRC-01E35ABC46-L000460](../../tests/test_research_guardrails.py#L460) | 460 | `"        ),"` | — |
| [SRC-01E35ABC46-L000461](../../tests/test_research_guardrails.py#L461) | 461 | `"    ]"` | — |
| [SRC-01E35ABC46-L000462](../../tests/test_research_guardrails.py#L462) | 462 | `"    accepted, report = apply_source_guardrails("` | — |
| [SRC-01E35ABC46-L000463](../../tests/test_research_guardrails.py#L463) | 463 | `"        question, \"auto\", {\"freshness\": \"any\"}, candidates, now=_GUARDRAIL_NOW"` | — |
| [SRC-01E35ABC46-L000464](../../tests/test_research_guardrails.py#L464) | 464 | `"    )"` | — |
| [SRC-01E35ABC46-L000465](../../tests/test_research_guardrails.py#L465) | 465 | `"    assert [item[\"url\"] for item in accepted] == [\"https://moi.gov.eg/\"]"` | — |
| [SRC-01E35ABC46-L000466](../../tests/test_research_guardrails.py#L466) | 466 | `"    assert report[\"official_government_domain_required\"] is True"` | — |
| [SRC-01E35ABC46-L000467](../../tests/test_research_guardrails.py#L467) | 467 | `"    assert report[\"official_government_domain_reason\"] == \"current_government_service_hours\""` | — |
| [SRC-01E35ABC46-L000468](../../tests/test_research_guardrails.py#L468) | 468 | `"    assert report[\"current_evidence_required\"] is True"` | — |
| [SRC-01E35ABC46-L000469](../../tests/test_research_guardrails.py#L469) | 469 | `"    assert report[\"rejection_counts\"] == {\"not_an_official_government_domain\": 1}"` | — |
| [SRC-01E35ABC46-L000470](../../tests/test_research_guardrails.py#L470) | 470 | `""` | — |
| [SRC-01E35ABC46-L000471](../../tests/test_research_guardrails.py#L471) | 471 | `""` | — |
| [SRC-01E35ABC46-L000472](../../tests/test_research_guardrails.py#L472) | 472 | `"def test_government_service_hour_request_rejects_undated_official_page() -> None:"` | — |
| [SRC-01E35ABC46-L000473](../../tests/test_research_guardrails.py#L473) | 473 | `"    question = \"مواعيد عمل مكتب الجوازات اليوم\""` | — |
| [SRC-01E35ABC46-L000474](../../tests/test_research_guardrails.py#L474) | 474 | `"    official = _guardrail_source(\"https://moi.gov.eg/\", published_at=\"\")"` | — |
| [SRC-01E35ABC46-L000475](../../tests/test_research_guardrails.py#L475) | 475 | `"    accepted, report = apply_source_guardrails("` | — |
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
