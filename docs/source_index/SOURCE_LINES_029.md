# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **029**
- سجلات الأسطر: **800**
- النطاق: SRC-3451CC474D-L000132 إلى SRC-6CBA87B20C-L000059
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-3451CC474D — [tests/test_api.py](../../tests/test_api.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3451CC474D-L000132](../../tests/test_api.py#L132) | 132 | `""` | — |
| [SRC-3451CC474D-L000133](../../tests/test_api.py#L133) | 133 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000134](../../tests/test_api.py#L134) | 134 | `"        local_api, \"/api/ask\", method=\"POST\", payload={\"question\": \"\"}"` | — |
| [SRC-3451CC474D-L000135](../../tests/test_api.py#L135) | 135 | `"    )"` | — |
| [SRC-3451CC474D-L000136](../../tests/test_api.py#L136) | 136 | `"    assert status == 400"` | — |
| [SRC-3451CC474D-L000137](../../tests/test_api.py#L137) | 137 | `"    assert \"question\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000138](../../tests/test_api.py#L138) | 138 | `""` | — |
| [SRC-3451CC474D-L000139](../../tests/test_api.py#L139) | 139 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000140](../../tests/test_api.py#L140) | 140 | `"        local_api, \"/api/leads\", method=\"POST\", payload={"` | — |
| [SRC-3451CC474D-L000141](../../tests/test_api.py#L141) | 141 | `"            \"text\": \"بدور على شقة\", \"source_url\": \"file:///private/data\", \"platform\": \"manual\""` | — |
| [SRC-3451CC474D-L000142](../../tests/test_api.py#L142) | 142 | `"        }"` | — |
| [SRC-3451CC474D-L000143](../../tests/test_api.py#L143) | 143 | `"    )"` | — |
| [SRC-3451CC474D-L000144](../../tests/test_api.py#L144) | 144 | `"    assert status == 400"` | — |
| [SRC-3451CC474D-L000145](../../tests/test_api.py#L145) | 145 | `"    assert \"absolute\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000146](../../tests/test_api.py#L146) | 146 | `""` | — |
| [SRC-3451CC474D-L000147](../../tests/test_api.py#L147) | 147 | `""` | — |
| [SRC-3451CC474D-L000148](../../tests/test_api.py#L148) | 148 | `"def test_api_blocks_non_json_and_cross_origin_posts(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000149](../../tests/test_api.py#L149) | 149 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000150](../../tests/test_api.py#L150) | 150 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000151](../../tests/test_api.py#L151) | 151 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000152](../../tests/test_api.py#L152) | 152 | `"        \"/api/ask\","` | — |
| [SRC-3451CC474D-L000153](../../tests/test_api.py#L153) | 153 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000154](../../tests/test_api.py#L154) | 154 | `"        payload={\"question\": \"كام عميل؟\"},"` | — |
| [SRC-3451CC474D-L000155](../../tests/test_api.py#L155) | 155 | `"        headers={\"Content-Type\": \"text/plain\"},"` | — |
| [SRC-3451CC474D-L000156](../../tests/test_api.py#L156) | 156 | `"    )"` | — |
| [SRC-3451CC474D-L000157](../../tests/test_api.py#L157) | 157 | `"    assert status == 415"` | — |
| [SRC-3451CC474D-L000158](../../tests/test_api.py#L158) | 158 | `"    assert \"Content-Type\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000159](../../tests/test_api.py#L159) | 159 | `""` | — |
| [SRC-3451CC474D-L000160](../../tests/test_api.py#L160) | 160 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000161](../../tests/test_api.py#L161) | 161 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000162](../../tests/test_api.py#L162) | 162 | `"        \"/api/ask\","` | — |
| [SRC-3451CC474D-L000163](../../tests/test_api.py#L163) | 163 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000164](../../tests/test_api.py#L164) | 164 | `"        payload={\"question\": \"كام عميل؟\"},"` | — |
| [SRC-3451CC474D-L000165](../../tests/test_api.py#L165) | 165 | `"        headers={\"Origin\": \"https://attacker.example\"},"` | — |
| [SRC-3451CC474D-L000166](../../tests/test_api.py#L166) | 166 | `"    )"` | — |
| [SRC-3451CC474D-L000167](../../tests/test_api.py#L167) | 167 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L000168](../../tests/test_api.py#L168) | 168 | `"    assert \"cross-origin\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000169](../../tests/test_api.py#L169) | 169 | `""` | — |
| [SRC-3451CC474D-L000170](../../tests/test_api.py#L170) | 170 | `""` | — |
| [SRC-3451CC474D-L000171](../../tests/test_api.py#L171) | 171 | `"def test_configured_frontend_origin_supports_preflight_and_post(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000172](../../tests/test_api.py#L172) | 172 | `"    origin = \"https://frontend.example\""` | — |
| [SRC-3451CC474D-L000173](../../tests/test_api.py#L173) | 173 | `"    monkeypatch.setenv(\"OMARAI_ALLOWED_ORIGINS\", origin)"` | — |
| [SRC-3451CC474D-L000174](../../tests/test_api.py#L174) | 174 | `""` | — |
| [SRC-3451CC474D-L000175](../../tests/test_api.py#L175) | 175 | `"    preflight = Request("` | — |
| [SRC-3451CC474D-L000176](../../tests/test_api.py#L176) | 176 | `"        local_api + \"/api/agent\","` | — |
| [SRC-3451CC474D-L000177](../../tests/test_api.py#L177) | 177 | `"        method=\"OPTIONS\","` | — |
| [SRC-3451CC474D-L000178](../../tests/test_api.py#L178) | 178 | `"        headers={"` | — |
| [SRC-3451CC474D-L000179](../../tests/test_api.py#L179) | 179 | `"            \"Origin\": origin,"` | — |
| [SRC-3451CC474D-L000180](../../tests/test_api.py#L180) | 180 | `"            \"Access-Control-Request-Method\": \"POST\","` | — |
| [SRC-3451CC474D-L000181](../../tests/test_api.py#L181) | 181 | `"            \"Access-Control-Request-Headers\": \"authorization,content-type\","` | — |
| [SRC-3451CC474D-L000182](../../tests/test_api.py#L182) | 182 | `"        },"` | — |
| [SRC-3451CC474D-L000183](../../tests/test_api.py#L183) | 183 | `"    )"` | — |
| [SRC-3451CC474D-L000184](../../tests/test_api.py#L184) | 184 | `"    with urlopen(preflight, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000185](../../tests/test_api.py#L185) | 185 | `"        assert response.status == 204"` | — |
| [SRC-3451CC474D-L000186](../../tests/test_api.py#L186) | 186 | `"        assert response.headers.get(\"Access-Control-Allow-Origin\") == origin"` | — |
| [SRC-3451CC474D-L000187](../../tests/test_api.py#L187) | 187 | `"        assert response.headers.get(\"Access-Control-Allow-Methods\") == \"GET, POST, OPTIONS\""` | — |
| [SRC-3451CC474D-L000188](../../tests/test_api.py#L188) | 188 | `"        assert response.headers.get(\"Access-Control-Allow-Headers\") == \"Authorization, Content-Type\""` | — |
| [SRC-3451CC474D-L000189](../../tests/test_api.py#L189) | 189 | `""` | — |
| [SRC-3451CC474D-L000190](../../tests/test_api.py#L190) | 190 | `"    body = json.dumps({\"question\": \"مين أفضل إشارة أراجعها؟\"}, ensure_ascii=False).encode(\"utf-8\")"` | — |
| [SRC-3451CC474D-L000191](../../tests/test_api.py#L191) | 191 | `"    post = Request("` | — |
| [SRC-3451CC474D-L000192](../../tests/test_api.py#L192) | 192 | `"        local_api + \"/api/ask\","` | — |
| [SRC-3451CC474D-L000193](../../tests/test_api.py#L193) | 193 | `"        data=body,"` | — |
| [SRC-3451CC474D-L000194](../../tests/test_api.py#L194) | 194 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000195](../../tests/test_api.py#L195) | 195 | `"        headers={\"Content-Type\": \"application/json\", \"Origin\": origin},"` | — |
| [SRC-3451CC474D-L000196](../../tests/test_api.py#L196) | 196 | `"    )"` | — |
| [SRC-3451CC474D-L000197](../../tests/test_api.py#L197) | 197 | `"    with urlopen(post, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000198](../../tests/test_api.py#L198) | 198 | `"        payload = json.loads(response.read().decode(\"utf-8\"))"` | — |
| [SRC-3451CC474D-L000199](../../tests/test_api.py#L199) | 199 | `"        assert response.status == 200"` | — |
| [SRC-3451CC474D-L000200](../../tests/test_api.py#L200) | 200 | `"        assert response.headers.get(\"Access-Control-Allow-Origin\") == origin"` | — |
| [SRC-3451CC474D-L000201](../../tests/test_api.py#L201) | 201 | `"        assert payload[\"kind\"] == \"no_data\""` | — |
| [SRC-3451CC474D-L000202](../../tests/test_api.py#L202) | 202 | `""` | — |
| [SRC-3451CC474D-L000203](../../tests/test_api.py#L203) | 203 | `""` | — |
| [SRC-3451CC474D-L000204](../../tests/test_api.py#L204) | 204 | `"def test_preflight_rejects_unconfigured_origin(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000205](../../tests/test_api.py#L205) | 205 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000206](../../tests/test_api.py#L206) | 206 | `"    preflight = Request("` | — |
| [SRC-3451CC474D-L000207](../../tests/test_api.py#L207) | 207 | `"        local_api + \"/api/agent\","` | — |
| [SRC-3451CC474D-L000208](../../tests/test_api.py#L208) | 208 | `"        method=\"OPTIONS\","` | — |
| [SRC-3451CC474D-L000209](../../tests/test_api.py#L209) | 209 | `"        headers={"` | — |
| [SRC-3451CC474D-L000210](../../tests/test_api.py#L210) | 210 | `"            \"Origin\": \"https://attacker.example\","` | — |
| [SRC-3451CC474D-L000211](../../tests/test_api.py#L211) | 211 | `"            \"Access-Control-Request-Method\": \"POST\","` | — |
| [SRC-3451CC474D-L000212](../../tests/test_api.py#L212) | 212 | `"        },"` | — |
| [SRC-3451CC474D-L000213](../../tests/test_api.py#L213) | 213 | `"    )"` | — |
| [SRC-3451CC474D-L000214](../../tests/test_api.py#L214) | 214 | `"    with pytest.raises(HTTPError) as error:"` | — |
| [SRC-3451CC474D-L000215](../../tests/test_api.py#L215) | 215 | `"        urlopen(preflight, timeout=3)"` | — |
| [SRC-3451CC474D-L000216](../../tests/test_api.py#L216) | 216 | `"    assert error.value.code == 403"` | — |
| [SRC-3451CC474D-L000217](../../tests/test_api.py#L217) | 217 | `""` | — |
| [SRC-3451CC474D-L000218](../../tests/test_api.py#L218) | 218 | `""` | — |
| [SRC-3451CC474D-L000219](../../tests/test_api.py#L219) | 219 | `"def test_ask_is_honest_when_database_is_empty(local_api):"` | — |
| [SRC-3451CC474D-L000220](../../tests/test_api.py#L220) | 220 | `"    status, answer = request_json("` | — |
| [SRC-3451CC474D-L000221](../../tests/test_api.py#L221) | 221 | `"        local_api, \"/api/ask\", method=\"POST\", payload={\"question\": \"مين أفضل إشارة أراجعها؟\"}"` | — |
| [SRC-3451CC474D-L000222](../../tests/test_api.py#L222) | 222 | `"    )"` | — |
| [SRC-3451CC474D-L000223](../../tests/test_api.py#L223) | 223 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000224](../../tests/test_api.py#L224) | 224 | `"    assert answer[\"kind\"] == \"no_data\""` | — |
| [SRC-3451CC474D-L000225](../../tests/test_api.py#L225) | 225 | `"    assert \"لا توجد إشارة\" in answer[\"answer\"]"` | — |
| [SRC-3451CC474D-L000226](../../tests/test_api.py#L226) | 226 | `""` | — |
| [SRC-3451CC474D-L000227](../../tests/test_api.py#L227) | 227 | `""` | — |
| [SRC-3451CC474D-L000228](../../tests/test_api.py#L228) | 228 | `""` | — |
| [SRC-3451CC474D-L000229](../../tests/test_api.py#L229) | 229 | `"def test_web_agent_endpoint_uses_agent_result(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000230](../../tests/test_api.py#L230) | 230 | `"    from api.omarai import WebAgent"` | — |
| [SRC-3451CC474D-L000231](../../tests/test_api.py#L231) | 231 | `""` | — |
| [SRC-3451CC474D-L000232](../../tests/test_api.py#L232) | 232 | `"    def fake_answer(self, question, history=None):"` | — |
| [SRC-3451CC474D-L000233](../../tests/test_api.py#L233) | 233 | `"        return {"` | — |
| [SRC-3451CC474D-L000234](../../tests/test_api.py#L234) | 234 | `"            \"answer\": \"إجابة اختبار [المصدر 1]\","` | — |
| [SRC-3451CC474D-L000235](../../tests/test_api.py#L235) | 235 | `"            \"question\": question,"` | — |
| [SRC-3451CC474D-L000236](../../tests/test_api.py#L236) | 236 | `"            \"search_query\": question,"` | — |
| [SRC-3451CC474D-L000237](../../tests/test_api.py#L237) | 237 | `"            \"sources\": [{\"title\": \"مصدر\", \"url\": \"https://example.com\", \"snippet\": \"نص\", \"page_fetched\": False}],"` | — |
| [SRC-3451CC474D-L000238](../../tests/test_api.py#L238) | 238 | `"            \"used_language_model\": True,"` | — |
| [SRC-3451CC474D-L000239](../../tests/test_api.py#L239) | 239 | `"            \"used_web_search\": True,"` | — |
| [SRC-3451CC474D-L000240](../../tests/test_api.py#L240) | 240 | `"            \"warnings\": [],"` | — |
| [SRC-3451CC474D-L000241](../../tests/test_api.py#L241) | 241 | `"            \"kind\": \"web_research\","` | — |
| [SRC-3451CC474D-L000242](../../tests/test_api.py#L242) | 242 | `"        }"` | — |
| [SRC-3451CC474D-L000243](../../tests/test_api.py#L243) | 243 | `""` | — |
| [SRC-3451CC474D-L000244](../../tests/test_api.py#L244) | 244 | `"    monkeypatch.setattr(WebAgent, \"answer\", fake_answer)"` | — |
| [SRC-3451CC474D-L000245](../../tests/test_api.py#L245) | 245 | `"    status, response = request_json("` | — |
| [SRC-3451CC474D-L000246](../../tests/test_api.py#L246) | 246 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000247](../../tests/test_api.py#L247) | 247 | `"        \"/api/agent\","` | — |
| [SRC-3451CC474D-L000248](../../tests/test_api.py#L248) | 248 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000249](../../tests/test_api.py#L249) | 249 | `"        payload={\"question\": \"ابحث عن موضوع\", \"history\": []},"` | — |
| [SRC-3451CC474D-L000250](../../tests/test_api.py#L250) | 250 | `"    )"` | — |
| [SRC-3451CC474D-L000251](../../tests/test_api.py#L251) | 251 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000252](../../tests/test_api.py#L252) | 252 | `"    assert response[\"kind\"] == \"web_research\""` | — |
| [SRC-3451CC474D-L000253](../../tests/test_api.py#L253) | 253 | `"    assert response[\"sources\"][0][\"url\"] == \"https://example.com\""` | — |
| [SRC-3451CC474D-L000254](../../tests/test_api.py#L254) | 254 | `""` | — |
| [SRC-3451CC474D-L000255](../../tests/test_api.py#L255) | 255 | `""` | — |
| [SRC-3451CC474D-L000256](../../tests/test_api.py#L256) | 256 | `""` | — |
| [SRC-3451CC474D-L000257](../../tests/test_api.py#L257) | 257 | `"def test_live_diagnostics_endpoint_returns_report_without_secrets(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000258](../../tests/test_api.py#L258) | 258 | `"    from api.omarai import WebAgent"` | — |
| [SRC-3451CC474D-L000259](../../tests/test_api.py#L259) | 259 | `""` | — |
| [SRC-3451CC474D-L000260](../../tests/test_api.py#L260) | 260 | `"    def fake_diagnostics(self, test_model=True, test_social=False):"` | — |
| [SRC-3451CC474D-L000261](../../tests/test_api.py#L261) | 261 | `"        return {"` | — |
| [SRC-3451CC474D-L000262](../../tests/test_api.py#L262) | 262 | `"            \"overall_status\": \"passed\","` | — |
| [SRC-3451CC474D-L000263](../../tests/test_api.py#L263) | 263 | `"            \"checks\": {"` | — |
| [SRC-3451CC474D-L000264](../../tests/test_api.py#L264) | 264 | `"                \"web_search\": {\"status\": \"passed\", \"result_count\": 4},"` | — |
| [SRC-3451CC474D-L000265](../../tests/test_api.py#L265) | 265 | `"                \"language_model\": {\"status\": \"passed\", \"response_received\": True},"` | — |
| [SRC-3451CC474D-L000266](../../tests/test_api.py#L266) | 266 | `"                \"social_search\": {\"status\": \"skipped\"},"` | — |
| [SRC-3451CC474D-L000267](../../tests/test_api.py#L267) | 267 | `"            },"` | — |
| [SRC-3451CC474D-L000268](../../tests/test_api.py#L268) | 268 | `"            \"model_usage\": [{"` | — |
| [SRC-3451CC474D-L000269](../../tests/test_api.py#L269) | 269 | `"                \"requested_model\": \"google/gemma-4-31b-it:free\","` | — |
| [SRC-3451CC474D-L000270](../../tests/test_api.py#L270) | 270 | `"                \"used_model\": \"google/gemma-4-31b-it:free\","` | — |
| [SRC-3451CC474D-L000271](../../tests/test_api.py#L271) | 271 | `"                \"fallback_used\": \"false\","` | — |
| [SRC-3451CC474D-L000272](../../tests/test_api.py#L272) | 272 | `"            }],"` | — |
| [SRC-3451CC474D-L000273](../../tests/test_api.py#L273) | 273 | `"        }"` | — |
| [SRC-3451CC474D-L000274](../../tests/test_api.py#L274) | 274 | `""` | — |
| [SRC-3451CC474D-L000275](../../tests/test_api.py#L275) | 275 | `"    monkeypatch.setattr(WebAgent, \"diagnostics\", fake_diagnostics)"` | — |
| [SRC-3451CC474D-L000276](../../tests/test_api.py#L276) | 276 | `"    status, report = request_json("` | — |
| [SRC-3451CC474D-L000277](../../tests/test_api.py#L277) | 277 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000278](../../tests/test_api.py#L278) | 278 | `"        \"/api/diagnostics\","` | — |
| [SRC-3451CC474D-L000279](../../tests/test_api.py#L279) | 279 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000280](../../tests/test_api.py#L280) | 280 | `"        payload={\"test_model\": True, \"test_social\": False},"` | — |
| [SRC-3451CC474D-L000281](../../tests/test_api.py#L281) | 281 | `"    )"` | — |
| [SRC-3451CC474D-L000282](../../tests/test_api.py#L282) | 282 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000283](../../tests/test_api.py#L283) | 283 | `"    assert report[\"overall_status\"] == \"passed\""` | — |
| [SRC-3451CC474D-L000284](../../tests/test_api.py#L284) | 284 | `"    assert report[\"checks\"][\"web_search\"][\"result_count\"] == 4"` | — |
| [SRC-3451CC474D-L000285](../../tests/test_api.py#L285) | 285 | `"    assert \"api_key\" not in report"` | — |
| [SRC-3451CC474D-L000286](../../tests/test_api.py#L286) | 286 | `"    assert \"secret\" not in str(report)"` | — |
| [SRC-3451CC474D-L000287](../../tests/test_api.py#L287) | 287 | `""` | — |
| [SRC-3451CC474D-L000288](../../tests/test_api.py#L288) | 288 | `""` | — |
| [SRC-3451CC474D-L000289](../../tests/test_api.py#L289) | 289 | `"def test_diagnostics_endpoint_requires_boolean_options(local_api):"` | — |
| [SRC-3451CC474D-L000290](../../tests/test_api.py#L290) | 290 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000291](../../tests/test_api.py#L291) | 291 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000292](../../tests/test_api.py#L292) | 292 | `"        \"/api/diagnostics\","` | — |
| [SRC-3451CC474D-L000293](../../tests/test_api.py#L293) | 293 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000294](../../tests/test_api.py#L294) | 294 | `"        payload={\"test_model\": \"yes\", \"test_social\": False},"` | — |
| [SRC-3451CC474D-L000295](../../tests/test_api.py#L295) | 295 | `"    )"` | — |
| [SRC-3451CC474D-L000296](../../tests/test_api.py#L296) | 296 | `"    assert status == 400"` | — |
| [SRC-3451CC474D-L000297](../../tests/test_api.py#L297) | 297 | `"    assert \"booleans\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000298](../../tests/test_api.py#L298) | 298 | `""` | — |
| [SRC-3451CC474D-L000299](../../tests/test_api.py#L299) | 299 | `""` | — |
| [SRC-3451CC474D-L000300](../../tests/test_api.py#L300) | 300 | `""` | — |
| [SRC-3451CC474D-L000301](../../tests/test_api.py#L301) | 301 | `"def test_rate_limit_ignores_spoofed_forwarded_for_by_default(monkeypatch):"` | — |
| [SRC-3451CC474D-L000302](../../tests/test_api.py#L302) | 302 | `"    monkeypatch.delenv(\"OMARAI_TRUST_PROXY_HEADERS\", raising=False)"` | — |
| [SRC-3451CC474D-L000303](../../tests/test_api.py#L303) | 303 | `"    handler = SimpleNamespace("` | — |
| [SRC-3451CC474D-L000304](../../tests/test_api.py#L304) | 304 | `"        headers={\"X-Forwarded-For\": \"198.51.100.77, 203.0.113.10\"},"` | — |
| [SRC-3451CC474D-L000305](../../tests/test_api.py#L305) | 305 | `"        client_address=(\"192.0.2.44\", 12345),"` | — |
| [SRC-3451CC474D-L000306](../../tests/test_api.py#L306) | 306 | `"    )"` | — |
| [SRC-3451CC474D-L000307](../../tests/test_api.py#L307) | 307 | `"    assert Handler._rate_limit_client_key(handler) == \"192.0.2.44\""` | — |
| [SRC-3451CC474D-L000308](../../tests/test_api.py#L308) | 308 | `""` | — |
| [SRC-3451CC474D-L000309](../../tests/test_api.py#L309) | 309 | `""` | — |
| [SRC-3451CC474D-L000310](../../tests/test_api.py#L310) | 310 | `"def test_rate_limit_uses_rightmost_valid_proxy_ip_only_when_enabled(monkeypatch):"` | — |
| [SRC-3451CC474D-L000311](../../tests/test_api.py#L311) | 311 | `"    monkeypatch.setenv(\"OMARAI_TRUST_PROXY_HEADERS\", \"1\")"` | — |
| [SRC-3451CC474D-L000312](../../tests/test_api.py#L312) | 312 | `"    handler = SimpleNamespace("` | — |
| [SRC-3451CC474D-L000313](../../tests/test_api.py#L313) | 313 | `"        headers={\"X-Forwarded-For\": \"198.51.100.77, 203.0.113.10\"},"` | — |
| [SRC-3451CC474D-L000314](../../tests/test_api.py#L314) | 314 | `"        client_address=(\"192.0.2.44\", 12345),"` | — |
| [SRC-3451CC474D-L000315](../../tests/test_api.py#L315) | 315 | `"    )"` | — |
| [SRC-3451CC474D-L000316](../../tests/test_api.py#L316) | 316 | `"    assert Handler._rate_limit_client_key(handler) == \"203.0.113.10\""` | — |
| [SRC-3451CC474D-L000317](../../tests/test_api.py#L317) | 317 | `""` | — |
| [SRC-3451CC474D-L000318](../../tests/test_api.py#L318) | 318 | `""` | — |
| [SRC-3451CC474D-L000319](../../tests/test_api.py#L319) | 319 | `"def test_rate_limit_proxy_header_invalid_value_falls_back_to_peer_ip(monkeypatch):"` | — |
| [SRC-3451CC474D-L000320](../../tests/test_api.py#L320) | 320 | `"    monkeypatch.setenv(\"OMARAI_TRUST_PROXY_HEADERS\", \"1\")"` | — |
| [SRC-3451CC474D-L000321](../../tests/test_api.py#L321) | 321 | `"    handler = SimpleNamespace("` | — |
| [SRC-3451CC474D-L000322](../../tests/test_api.py#L322) | 322 | `"        headers={\"X-Forwarded-For\": \"198.51.100.77, not-an-ip\"},"` | — |
| [SRC-3451CC474D-L000323](../../tests/test_api.py#L323) | 323 | `"        client_address=(\"192.0.2.44\", 12345),"` | — |
| [SRC-3451CC474D-L000324](../../tests/test_api.py#L324) | 324 | `"    )"` | — |
| [SRC-3451CC474D-L000325](../../tests/test_api.py#L325) | 325 | `"    assert Handler._rate_limit_client_key(handler) == \"192.0.2.44\""` | — |
| [SRC-3451CC474D-L000326](../../tests/test_api.py#L326) | 326 | `""` | — |
| [SRC-3451CC474D-L000327](../../tests/test_api.py#L327) | 327 | `""` | — |
| [SRC-3451CC474D-L000328](../../tests/test_api.py#L328) | 328 | `"def test_public_api_authentication_and_rate_limit_precede_json_parsing(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000329](../../tests/test_api.py#L329) | 329 | `"    \"\"\"Reject untrusted API calls before parsing bodies and throttle repeated failures.\"\"\""` | — |
| [SRC-3451CC474D-L000330](../../tests/test_api.py#L330) | 330 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000331](../../tests/test_api.py#L331) | 331 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"z\" * 48)"` | — |
| [SRC-3451CC474D-L000332](../../tests/test_api.py#L332) | 332 | `"    monkeypatch.setattr(Handler, \"RATE_LIMIT_REQUESTS\", 1)"` | — |
| [SRC-3451CC474D-L000333](../../tests/test_api.py#L333) | 333 | `"    with Handler._rate_lock:"` | — |
| [SRC-3451CC474D-L000334](../../tests/test_api.py#L334) | 334 | `"        Handler._request_times.clear()"` | — |
| [SRC-3451CC474D-L000335](../../tests/test_api.py#L335) | 335 | `"    request = Request("` | — |
| [SRC-3451CC474D-L000336](../../tests/test_api.py#L336) | 336 | `"        local_api + \"/api/agent\","` | — |
| [SRC-3451CC474D-L000337](../../tests/test_api.py#L337) | 337 | `"        data=b\"invalid-json-body\","` | — |
| [SRC-3451CC474D-L000338](../../tests/test_api.py#L338) | 338 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000339](../../tests/test_api.py#L339) | 339 | `"        headers={\"Content-Type\": \"application/json\"},"` | — |
| [SRC-3451CC474D-L000340](../../tests/test_api.py#L340) | 340 | `"    )"` | — |
| [SRC-3451CC474D-L000341](../../tests/test_api.py#L341) | 341 | `"    try:"` | — |
| [SRC-3451CC474D-L000342](../../tests/test_api.py#L342) | 342 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000343](../../tests/test_api.py#L343) | 343 | `"            first_status = response.status"` | — |
| [SRC-3451CC474D-L000344](../../tests/test_api.py#L344) | 344 | `"    except HTTPError as error:"` | — |
| [SRC-3451CC474D-L000345](../../tests/test_api.py#L345) | 345 | `"        first_status = error.code"` | — |
| [SRC-3451CC474D-L000346](../../tests/test_api.py#L346) | 346 | `"    assert first_status == 401"` | — |
| [SRC-3451CC474D-L000347](../../tests/test_api.py#L347) | 347 | `""` | — |
| [SRC-3451CC474D-L000348](../../tests/test_api.py#L348) | 348 | `"    try:"` | — |
| [SRC-3451CC474D-L000349](../../tests/test_api.py#L349) | 349 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000350](../../tests/test_api.py#L350) | 350 | `"            second_status = response.status"` | — |
| [SRC-3451CC474D-L000351](../../tests/test_api.py#L351) | 351 | `"    except HTTPError as error:"` | — |
| [SRC-3451CC474D-L000352](../../tests/test_api.py#L352) | 352 | `"        second_status = error.code"` | — |
| [SRC-3451CC474D-L000353](../../tests/test_api.py#L353) | 353 | `"    assert second_status == 429"` | — |
| [SRC-3451CC474D-L000354](../../tests/test_api.py#L354) | 354 | `""` | — |
| [SRC-3451CC474D-L000355](../../tests/test_api.py#L355) | 355 | `""` | — |
| [SRC-3451CC474D-L000356](../../tests/test_api.py#L356) | 356 | `"def test_hosted_api_requires_private_token_for_search_and_lead_data(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000357](../../tests/test_api.py#L357) | 357 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000358](../../tests/test_api.py#L358) | 358 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"x\" * 48)"` | — |
| [SRC-3451CC474D-L000359](../../tests/test_api.py#L359) | 359 | `""` | — |
| [SRC-3451CC474D-L000360](../../tests/test_api.py#L360) | 360 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000361](../../tests/test_api.py#L361) | 361 | `"        local_api, \"/api/analyze\", method=\"POST\", payload={\"text\": \"test\"}"` | — |
| [SRC-3451CC474D-L000362](../../tests/test_api.py#L362) | 362 | `"    )"` | — |
| [SRC-3451CC474D-L000363](../../tests/test_api.py#L363) | 363 | `"    assert status == 401"` | — |
| [SRC-3451CC474D-L000364](../../tests/test_api.py#L364) | 364 | `"    assert \"رمز الوصول\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000365](../../tests/test_api.py#L365) | 365 | `""` | — |
| [SRC-3451CC474D-L000366](../../tests/test_api.py#L366) | 366 | `"    status, error = request_json(local_api, \"/api/leads\")"` | — |
| [SRC-3451CC474D-L000367](../../tests/test_api.py#L367) | 367 | `"    assert status == 401"` | — |
| [SRC-3451CC474D-L000368](../../tests/test_api.py#L368) | 368 | `""` | — |
| [SRC-3451CC474D-L000369](../../tests/test_api.py#L369) | 369 | `"    headers = {\"Authorization\": \"Bearer \" + \"x\" * 48}"` | — |
| [SRC-3451CC474D-L000370](../../tests/test_api.py#L370) | 370 | `"    status, result = request_json("` | — |
| [SRC-3451CC474D-L000371](../../tests/test_api.py#L371) | 371 | `"        local_api, \"/api/analyze\", method=\"POST\", payload={\"text\": \"بدور على شقة\"}, headers=headers"` | — |
| [SRC-3451CC474D-L000372](../../tests/test_api.py#L372) | 372 | `"    )"` | — |
| [SRC-3451CC474D-L000373](../../tests/test_api.py#L373) | 373 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000374](../../tests/test_api.py#L374) | 374 | `"    assert \"score\" in result"` | — |
| [SRC-3451CC474D-L000375](../../tests/test_api.py#L375) | 375 | `""` | — |
| [SRC-3451CC474D-L000376](../../tests/test_api.py#L376) | 376 | `"    status, result = request_json(local_api, \"/api/leads\", headers=headers)"` | — |
| [SRC-3451CC474D-L000377](../../tests/test_api.py#L377) | 377 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000378](../../tests/test_api.py#L378) | 378 | `"    assert result[\"count\"] == 0"` | — |
| [SRC-3451CC474D-L000379](../../tests/test_api.py#L379) | 379 | `""` | — |
| [SRC-3451CC474D-L000380](../../tests/test_api.py#L380) | 380 | `""` | — |
| [SRC-3451CC474D-L000381](../../tests/test_api.py#L381) | 381 | `"def test_hosted_api_rate_limits_authenticated_requests(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000382](../../tests/test_api.py#L382) | 382 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000383](../../tests/test_api.py#L383) | 383 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"y\" * 48)"` | — |
| [SRC-3451CC474D-L000384](../../tests/test_api.py#L384) | 384 | `"    monkeypatch.setattr(Handler, \"RATE_LIMIT_REQUESTS\", 1)"` | — |
| [SRC-3451CC474D-L000385](../../tests/test_api.py#L385) | 385 | `"    with Handler._rate_lock:"` | — |
| [SRC-3451CC474D-L000386](../../tests/test_api.py#L386) | 386 | `"        Handler._request_times.clear()"` | — |
| [SRC-3451CC474D-L000387](../../tests/test_api.py#L387) | 387 | `"    headers = {\"Authorization\": \"Bearer \" + \"y\" * 48}"` | — |
| [SRC-3451CC474D-L000388](../../tests/test_api.py#L388) | 388 | `""` | — |
| [SRC-3451CC474D-L000389](../../tests/test_api.py#L389) | 389 | `"    status, _ = request_json("` | — |
| [SRC-3451CC474D-L000390](../../tests/test_api.py#L390) | 390 | `"        local_api, \"/api/analyze\", method=\"POST\", payload={\"text\": \"first\"}, headers=headers"` | — |
| [SRC-3451CC474D-L000391](../../tests/test_api.py#L391) | 391 | `"    )"` | — |
| [SRC-3451CC474D-L000392](../../tests/test_api.py#L392) | 392 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000393](../../tests/test_api.py#L393) | 393 | `""` | — |
| [SRC-3451CC474D-L000394](../../tests/test_api.py#L394) | 394 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000395](../../tests/test_api.py#L395) | 395 | `"        local_api, \"/api/analyze\", method=\"POST\", payload={\"text\": \"second\"}, headers=headers"` | — |
| [SRC-3451CC474D-L000396](../../tests/test_api.py#L396) | 396 | `"    )"` | — |
| [SRC-3451CC474D-L000397](../../tests/test_api.py#L397) | 397 | `"    assert status == 429"` | — |
| [SRC-3451CC474D-L000398](../../tests/test_api.py#L398) | 398 | `"    assert \"حد الطلبات\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000399](../../tests/test_api.py#L399) | 399 | `""` | — |
| [SRC-3451CC474D-L000400](../../tests/test_api.py#L400) | 400 | `""` | — |
| [SRC-3451CC474D-L000401](../../tests/test_api.py#L401) | 401 | `""` | — |
| [SRC-3451CC474D-L000402](../../tests/test_api.py#L402) | 402 | `"def test_public_binding_requires_explicit_deployment_flag_and_strong_token(monkeypatch):"` | — |
| [SRC-3451CC474D-L000403](../../tests/test_api.py#L403) | 403 | `"    from api.omarai import serve"` | — |
| [SRC-3451CC474D-L000404](../../tests/test_api.py#L404) | 404 | `""` | — |
| [SRC-3451CC474D-L000405](../../tests/test_api.py#L405) | 405 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000406](../../tests/test_api.py#L406) | 406 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000407](../../tests/test_api.py#L407) | 407 | `"    with pytest.raises(ValueError, match=\"Public binding requires\"):"` | — |
| [SRC-3451CC474D-L000408](../../tests/test_api.py#L408) | 408 | `"        serve(\"0.0.0.0\", 0)"` | — |
| [SRC-3451CC474D-L000409](../../tests/test_api.py#L409) | 409 | `""` | — |
| [SRC-3451CC474D-L000410](../../tests/test_api.py#L410) | 410 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000411](../../tests/test_api.py#L411) | 411 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"short\")"` | — |
| [SRC-3451CC474D-L000412](../../tests/test_api.py#L412) | 412 | `"    with pytest.raises(ValueError, match=\"at least 32 characters\"):"` | — |
| [SRC-3451CC474D-L000413](../../tests/test_api.py#L413) | 413 | `"        serve(\"0.0.0.0\", 0)"` | — |
| [SRC-3451CC474D-L000414](../../tests/test_api.py#L414) | 414 | `""` | — |
| [SRC-3451CC474D-L000415](../../tests/test_api.py#L415) | 415 | `"def test_rate_limiter_prunes_expired_client_buckets(monkeypatch):"` | — |
| [SRC-3451CC474D-L000416](../../tests/test_api.py#L416) | 416 | `"    \"\"\"Client IPs do not accumulate forever after their 60-second window expires.\"\"\""` | — |
| [SRC-3451CC474D-L000417](../../tests/test_api.py#L417) | 417 | `"    monkeypatch.delenv(\"OMARAI_TRUST_PROXY_HEADERS\", raising=False)"` | — |
| [SRC-3451CC474D-L000418](../../tests/test_api.py#L418) | 418 | `"    monkeypatch.setattr(Handler, \"_request_times\", defaultdict(deque))"` | — |
| [SRC-3451CC474D-L000419](../../tests/test_api.py#L419) | 419 | `"    monkeypatch.setattr(Handler, \"_rate_last_cleanup\", 0.0)"` | — |
| [SRC-3451CC474D-L000420](../../tests/test_api.py#L420) | 420 | `"    clock = {\"now\": 100.0}"` | — |
| [SRC-3451CC474D-L000421](../../tests/test_api.py#L421) | 421 | `"    monkeypatch.setattr(\"api.omarai.time.monotonic\", lambda: clock[\"now\"])"` | — |
| [SRC-3451CC474D-L000422](../../tests/test_api.py#L422) | 422 | `""` | — |
| [SRC-3451CC474D-L000423](../../tests/test_api.py#L423) | 423 | `"    class FakeHandler(Handler):"` | — |
| [SRC-3451CC474D-L000424](../../tests/test_api.py#L424) | 424 | `"        def __init__(self, ip):"` | — |
| [SRC-3451CC474D-L000425](../../tests/test_api.py#L425) | 425 | `"            self.headers = {}"` | — |
| [SRC-3451CC474D-L000426](../../tests/test_api.py#L426) | 426 | `"            self.client_address = (ip, 1234)"` | — |
| [SRC-3451CC474D-L000427](../../tests/test_api.py#L427) | 427 | `""` | — |
| [SRC-3451CC474D-L000428](../../tests/test_api.py#L428) | 428 | `"    first = FakeHandler(\"192.0.2.1\")"` | — |
| [SRC-3451CC474D-L000429](../../tests/test_api.py#L429) | 429 | `"    second = FakeHandler(\"192.0.2.2\")"` | — |
| [SRC-3451CC474D-L000430](../../tests/test_api.py#L430) | 430 | `"    assert first._rate_limit_ok() is True"` | — |
| [SRC-3451CC474D-L000431](../../tests/test_api.py#L431) | 431 | `"    assert \"192.0.2.1\" in Handler._request_times"` | — |
| [SRC-3451CC474D-L000432](../../tests/test_api.py#L432) | 432 | `""` | — |
| [SRC-3451CC474D-L000433](../../tests/test_api.py#L433) | 433 | `"    clock[\"now\"] = 161.0"` | — |
| [SRC-3451CC474D-L000434](../../tests/test_api.py#L434) | 434 | `"    assert second._rate_limit_ok() is True"` | — |
| [SRC-3451CC474D-L000435](../../tests/test_api.py#L435) | 435 | `"    assert \"192.0.2.1\" not in Handler._request_times"` | — |
| [SRC-3451CC474D-L000436](../../tests/test_api.py#L436) | 436 | `"    assert \"192.0.2.2\" in Handler._request_times"` | — |
| [SRC-3451CC474D-L000437](../../tests/test_api.py#L437) | 437 | `""` | — |
| [SRC-3451CC474D-L000438](../../tests/test_api.py#L438) | 438 | `""` | — |
| [SRC-3451CC474D-L000439](../../tests/test_api.py#L439) | 439 | `""` | — |
| [SRC-3451CC474D-L000440](../../tests/test_api.py#L440) | 440 | `"def test_agent_concurrency_cap_rejects_work_when_all_slots_are_busy(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000441](../../tests/test_api.py#L441) | 441 | `"    from api.omarai import WebAgent"` | — |
| [SRC-3451CC474D-L000442](../../tests/test_api.py#L442) | 442 | `""` | — |
| [SRC-3451CC474D-L000443](../../tests/test_api.py#L443) | 443 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000444](../../tests/test_api.py#L444) | 444 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000445](../../tests/test_api.py#L445) | 445 | `"    monkeypatch.setattr(Handler, \"_request_times\", defaultdict(deque))"` | — |
| [SRC-3451CC474D-L000446](../../tests/test_api.py#L446) | 446 | `"    monkeypatch.setattr(Handler, \"_rate_last_cleanup\", 0.0)"` | — |
| [SRC-3451CC474D-L000447](../../tests/test_api.py#L447) | 447 | `"    monkeypatch.setattr(Handler, \"_agent_semaphore\", threading.BoundedSemaphore(1))"` | — |
| [SRC-3451CC474D-L000448](../../tests/test_api.py#L448) | 448 | `""` | — |
| [SRC-3451CC474D-L000449](../../tests/test_api.py#L449) | 449 | `"    entered = threading.Event()"` | — |
| [SRC-3451CC474D-L000450](../../tests/test_api.py#L450) | 450 | `"    release = threading.Event()"` | — |
| [SRC-3451CC474D-L000451](../../tests/test_api.py#L451) | 451 | `"    first_result = {}"` | — |
| [SRC-3451CC474D-L000452](../../tests/test_api.py#L452) | 452 | `""` | — |
| [SRC-3451CC474D-L000453](../../tests/test_api.py#L453) | 453 | `"    def slow_answer(self, question, history=None, mode=\"auto\"):"` | — |
| [SRC-3451CC474D-L000454](../../tests/test_api.py#L454) | 454 | `"        entered.set()"` | — |
| [SRC-3451CC474D-L000455](../../tests/test_api.py#L455) | 455 | `"        assert release.wait(timeout=2), \"test did not release the held research slot\""` | — |
| [SRC-3451CC474D-L000456](../../tests/test_api.py#L456) | 456 | `"        return {"` | — |
| [SRC-3451CC474D-L000457](../../tests/test_api.py#L457) | 457 | `"            \"answer\": \"نتيجة اختبار محدودة\","` | — |
| [SRC-3451CC474D-L000458](../../tests/test_api.py#L458) | 458 | `"            \"question\": question,"` | — |
| [SRC-3451CC474D-L000459](../../tests/test_api.py#L459) | 459 | `"            \"search_query\": question,"` | — |
| [SRC-3451CC474D-L000460](../../tests/test_api.py#L460) | 460 | `"            \"search_queries\": [],"` | — |
| [SRC-3451CC474D-L000461](../../tests/test_api.py#L461) | 461 | `"            \"search_report\": {\"search_attempted\": False, \"search_outcome\": \"not_attempted\"},"` | — |
| [SRC-3451CC474D-L000462](../../tests/test_api.py#L462) | 462 | `"            \"sources\": [],"` | — |
| [SRC-3451CC474D-L000463](../../tests/test_api.py#L463) | 463 | `"            \"used_language_model\": False,"` | — |
| [SRC-3451CC474D-L000464](../../tests/test_api.py#L464) | 464 | `"            \"used_web_search\": False,"` | — |
| [SRC-3451CC474D-L000465](../../tests/test_api.py#L465) | 465 | `"            \"search_attempted\": False,"` | — |
| [SRC-3451CC474D-L000466](../../tests/test_api.py#L466) | 466 | `"            \"used_social_search\": False,"` | — |
| [SRC-3451CC474D-L000467](../../tests/test_api.py#L467) | 467 | `"            \"warnings\": [],"` | — |
| [SRC-3451CC474D-L000468](../../tests/test_api.py#L468) | 468 | `"            \"kind\": \"web_fallback\","` | — |
| [SRC-3451CC474D-L000469](../../tests/test_api.py#L469) | 469 | `"        }"` | — |
| [SRC-3451CC474D-L000470](../../tests/test_api.py#L470) | 470 | `""` | — |
| [SRC-3451CC474D-L000471](../../tests/test_api.py#L471) | 471 | `"    monkeypatch.setattr(WebAgent, \"answer\", slow_answer)"` | — |
| [SRC-3451CC474D-L000472](../../tests/test_api.py#L472) | 472 | `""` | — |
| [SRC-3451CC474D-L000473](../../tests/test_api.py#L473) | 473 | `"    def first_request():"` | — |
| [SRC-3451CC474D-L000474](../../tests/test_api.py#L474) | 474 | `"        first_result[\"response\"] = request_json("` | — |
| [SRC-3451CC474D-L000475](../../tests/test_api.py#L475) | 475 | `"            local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"السؤال الأول\"}"` | — |
| [SRC-3451CC474D-L000476](../../tests/test_api.py#L476) | 476 | `"        )"` | — |
| [SRC-3451CC474D-L000477](../../tests/test_api.py#L477) | 477 | `""` | — |
| [SRC-3451CC474D-L000478](../../tests/test_api.py#L478) | 478 | `"    worker = threading.Thread(target=first_request, daemon=True)"` | — |
| [SRC-3451CC474D-L000479](../../tests/test_api.py#L479) | 479 | `"    worker.start()"` | — |
| [SRC-3451CC474D-L000480](../../tests/test_api.py#L480) | 480 | `"    try:"` | — |
| [SRC-3451CC474D-L000481](../../tests/test_api.py#L481) | 481 | `"        assert entered.wait(timeout=1), \"first request did not acquire the research slot\""` | — |
| [SRC-3451CC474D-L000482](../../tests/test_api.py#L482) | 482 | `"        status, payload = request_json("` | — |
| [SRC-3451CC474D-L000483](../../tests/test_api.py#L483) | 483 | `"            local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"السؤال الثاني\"}"` | — |
| [SRC-3451CC474D-L000484](../../tests/test_api.py#L484) | 484 | `"        )"` | — |
| [SRC-3451CC474D-L000485](../../tests/test_api.py#L485) | 485 | `"        assert status == 503"` | — |
| [SRC-3451CC474D-L000486](../../tests/test_api.py#L486) | 486 | `"        assert payload[\"retry_after_seconds\"] == 5"` | — |
| [SRC-3451CC474D-L000487](../../tests/test_api.py#L487) | 487 | `"        assert \"مشغولة\" in payload[\"error\"]"` | — |
| [SRC-3451CC474D-L000488](../../tests/test_api.py#L488) | 488 | `"    finally:"` | — |
| [SRC-3451CC474D-L000489](../../tests/test_api.py#L489) | 489 | `"        release.set()"` | — |
| [SRC-3451CC474D-L000490](../../tests/test_api.py#L490) | 490 | `"        worker.join(timeout=3)"` | — |
| [SRC-3451CC474D-L000491](../../tests/test_api.py#L491) | 491 | `""` | — |
| [SRC-3451CC474D-L000492](../../tests/test_api.py#L492) | 492 | `"    assert not worker.is_alive()"` | — |
| [SRC-3451CC474D-L000493](../../tests/test_api.py#L493) | 493 | `"    assert first_result[\"response\"][0] == 200"` | — |
| [SRC-3451CC474D-L000494](../../tests/test_api.py#L494) | 494 | `""` | — |
| [SRC-3451CC474D-L000495](../../tests/test_api.py#L495) | 495 | `""` | — |
| [SRC-3451CC474D-L000496](../../tests/test_api.py#L496) | 496 | `"def test_agent_concurrency_limit_has_hard_bounds(monkeypatch):"` | — |
| [SRC-3451CC474D-L000497](../../tests/test_api.py#L497) | 497 | `"    from api.omarai import _configured_agent_concurrency_limit"` | — |
| [SRC-3451CC474D-L000498](../../tests/test_api.py#L498) | 498 | `""` | — |
| [SRC-3451CC474D-L000499](../../tests/test_api.py#L499) | 499 | `"    monkeypatch.setenv(\"OMARAI_MAX_CONCURRENT_AGENT_REQUESTS\", \"99\")"` | — |
| [SRC-3451CC474D-L000500](../../tests/test_api.py#L500) | 500 | `"    assert _configured_agent_concurrency_limit() == 8"` | — |
| [SRC-3451CC474D-L000501](../../tests/test_api.py#L501) | 501 | `"    monkeypatch.setenv(\"OMARAI_MAX_CONCURRENT_AGENT_REQUESTS\", \"invalid\")"` | — |
| [SRC-3451CC474D-L000502](../../tests/test_api.py#L502) | 502 | `"    assert _configured_agent_concurrency_limit() == 4"` | — |
| [SRC-3451CC474D-L000503](../../tests/test_api.py#L503) | 503 | `""` | — |
| [SRC-3451CC474D-L000504](../../tests/test_api.py#L504) | 504 | `""` | — |
| [SRC-3451CC474D-L000505](../../tests/test_api.py#L505) | 505 | `"def test_api_rejects_oversized_request_body(local_api):"` | — |
| [SRC-3451CC474D-L000506](../../tests/test_api.py#L506) | 506 | `"    status, payload = request_json("` | — |
| [SRC-3451CC474D-L000507](../../tests/test_api.py#L507) | 507 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000508](../../tests/test_api.py#L508) | 508 | `"        \"/api/analyze\","` | — |
| [SRC-3451CC474D-L000509](../../tests/test_api.py#L509) | 509 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000510](../../tests/test_api.py#L510) | 510 | `"        payload={\"text\": \"x\" * 200_001},"` | — |
| [SRC-3451CC474D-L000511](../../tests/test_api.py#L511) | 511 | `"    )"` | — |
| [SRC-3451CC474D-L000512](../../tests/test_api.py#L512) | 512 | `""` | — |
| [SRC-3451CC474D-L000513](../../tests/test_api.py#L513) | 513 | `"    assert status == 413"` | — |
| [SRC-3451CC474D-L000514](../../tests/test_api.py#L514) | 514 | `"    assert payload[\"error\"] == \"request too large\""` | — |
| [SRC-3451CC474D-L000515](../../tests/test_api.py#L515) | 515 | `""` | — |
| [SRC-3451CC474D-L000516](../../tests/test_api.py#L516) | 516 | `""` | — |
| [SRC-3451CC474D-L000517](../../tests/test_api.py#L517) | 517 | `"def test_api_rejects_malformed_content_length(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000518](../../tests/test_api.py#L518) | 518 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000519](../../tests/test_api.py#L519) | 519 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000520](../../tests/test_api.py#L520) | 520 | `"    host_port = local_api.rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000521](../../tests/test_api.py#L521) | 521 | `"    with socket.create_connection((host_port[0].removeprefix(\"http://\"), int(host_port[1])), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000522](../../tests/test_api.py#L522) | 522 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000523](../../tests/test_api.py#L523) | 523 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000524](../../tests/test_api.py#L524) | 524 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000525](../../tests/test_api.py#L525) | 525 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000526](../../tests/test_api.py#L526) | 526 | `"            b\"Content-Length: invalid\\r\\n\""` | — |
| [SRC-3451CC474D-L000527](../../tests/test_api.py#L527) | 527 | `"            b\"Connection: close\\r\\n\\r\\n\""` | — |
| [SRC-3451CC474D-L000528](../../tests/test_api.py#L528) | 528 | `"        )"` | — |
| [SRC-3451CC474D-L000529](../../tests/test_api.py#L529) | 529 | `"        response = b\"\""` | — |
| [SRC-3451CC474D-L000530](../../tests/test_api.py#L530) | 530 | `"        while True:"` | — |
| [SRC-3451CC474D-L000531](../../tests/test_api.py#L531) | 531 | `"            chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000532](../../tests/test_api.py#L532) | 532 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000533](../../tests/test_api.py#L533) | 533 | `"                break"` | — |
| [SRC-3451CC474D-L000534](../../tests/test_api.py#L534) | 534 | `"            response += chunk"` | — |
| [SRC-3451CC474D-L000535](../../tests/test_api.py#L535) | 535 | `""` | — |
| [SRC-3451CC474D-L000536](../../tests/test_api.py#L536) | 536 | `"    assert response.startswith(b\"HTTP/1.0 400\")"` | — |
| [SRC-3451CC474D-L000537](../../tests/test_api.py#L537) | 537 | `"    assert b\"valid Content-Length is required\" in response"` | — |
| [SRC-3451CC474D-L000538](../../tests/test_api.py#L538) | 538 | `""` | — |
| [SRC-3451CC474D-L000539](../../tests/test_api.py#L539) | 539 | `""` | — |
| [SRC-3451CC474D-L000540](../../tests/test_api.py#L540) | 540 | `"def test_api_returns_408_when_request_body_read_times_out(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000541](../../tests/test_api.py#L541) | 541 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000542](../../tests/test_api.py#L542) | 542 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000543](../../tests/test_api.py#L543) | 543 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_BODY_READ_TIMEOUT_SECONDS\", 0.1)"` | — |
| [SRC-3451CC474D-L000544](../../tests/test_api.py#L544) | 544 | `"    host_port = local_api.rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000545](../../tests/test_api.py#L545) | 545 | `"    with socket.create_connection((host_port[0].removeprefix(\"http://\"), int(host_port[1])), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000546](../../tests/test_api.py#L546) | 546 | `"        client.settimeout(2)"` | — |
| [SRC-3451CC474D-L000547](../../tests/test_api.py#L547) | 547 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000548](../../tests/test_api.py#L548) | 548 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000549](../../tests/test_api.py#L549) | 549 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000550](../../tests/test_api.py#L550) | 550 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000551](../../tests/test_api.py#L551) | 551 | `"            b\"Content-Length: 40\\r\\n\""` | — |
| [SRC-3451CC474D-L000552](../../tests/test_api.py#L552) | 552 | `"            b\"Connection: close\\r\\n\\r\\n\""` | — |
| [SRC-3451CC474D-L000553](../../tests/test_api.py#L553) | 553 | `"            b\"{}\""` | — |
| [SRC-3451CC474D-L000554](../../tests/test_api.py#L554) | 554 | `"        )"` | — |
| [SRC-3451CC474D-L000555](../../tests/test_api.py#L555) | 555 | `"        response = b\"\""` | — |
| [SRC-3451CC474D-L000556](../../tests/test_api.py#L556) | 556 | `"        while True:"` | — |
| [SRC-3451CC474D-L000557](../../tests/test_api.py#L557) | 557 | `"            chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000558](../../tests/test_api.py#L558) | 558 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000559](../../tests/test_api.py#L559) | 559 | `"                break"` | — |
| [SRC-3451CC474D-L000560](../../tests/test_api.py#L560) | 560 | `"            response += chunk"` | — |
| [SRC-3451CC474D-L000561](../../tests/test_api.py#L561) | 561 | `""` | — |
| [SRC-3451CC474D-L000562](../../tests/test_api.py#L562) | 562 | `"    assert response.startswith(b\"HTTP/1.0 408\")"` | — |
| [SRC-3451CC474D-L000563](../../tests/test_api.py#L563) | 563 | `"    assert b\"request body read timed out\" in response"` | — |
| [SRC-3451CC474D-L000564](../../tests/test_api.py#L564) | 564 | `""` | — |
| [SRC-3451CC474D-L000565](../../tests/test_api.py#L565) | 565 | `""` | — |
| [SRC-3451CC474D-L000566](../../tests/test_api.py#L566) | 566 | `"def test_api_absolute_body_deadline_stops_slow_trickle(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000567](../../tests/test_api.py#L567) | 567 | `"    \"\"\"A client must not evade the total deadline by sending before each idle timeout.\"\"\""` | — |
| [SRC-3451CC474D-L000568](../../tests/test_api.py#L568) | 568 | `"    import time"` | — |
| [SRC-3451CC474D-L000569](../../tests/test_api.py#L569) | 569 | `""` | — |
| [SRC-3451CC474D-L000570](../../tests/test_api.py#L570) | 570 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000571](../../tests/test_api.py#L571) | 571 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000572](../../tests/test_api.py#L572) | 572 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_BODY_READ_TIMEOUT_SECONDS\", 0.45)"` | — |
| [SRC-3451CC474D-L000573](../../tests/test_api.py#L573) | 573 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_BODY_IDLE_TIMEOUT_SECONDS\", 0.20)"` | — |
| [SRC-3451CC474D-L000574](../../tests/test_api.py#L574) | 574 | `"    host, port = local_api.removeprefix(\"http://\").rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000575](../../tests/test_api.py#L575) | 575 | `""` | — |
| [SRC-3451CC474D-L000576](../../tests/test_api.py#L576) | 576 | `"    with socket.create_connection((host, int(port)), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000577](../../tests/test_api.py#L577) | 577 | `"        client.settimeout(2)"` | — |
| [SRC-3451CC474D-L000578](../../tests/test_api.py#L578) | 578 | `"        started = time.monotonic()"` | — |
| [SRC-3451CC474D-L000579](../../tests/test_api.py#L579) | 579 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000580](../../tests/test_api.py#L580) | 580 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000581](../../tests/test_api.py#L581) | 581 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000582](../../tests/test_api.py#L582) | 582 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000583](../../tests/test_api.py#L583) | 583 | `"            b\"Content-Length: 100\\r\\n\""` | — |
| [SRC-3451CC474D-L000584](../../tests/test_api.py#L584) | 584 | `"            b\"Connection: close\\r\\n\\r\\n\""` | — |
| [SRC-3451CC474D-L000585](../../tests/test_api.py#L585) | 585 | `"            b\"{\""` | — |
| [SRC-3451CC474D-L000586](../../tests/test_api.py#L586) | 586 | `"        )"` | — |
| [SRC-3451CC474D-L000587](../../tests/test_api.py#L587) | 587 | `"        # Each fragment arrives before the 0.20s idle timeout, but the complete"` | — |
| [SRC-3451CC474D-L000588](../../tests/test_api.py#L588) | 588 | `"        # request body never arrives before the 0.45s absolute deadline."` | — |
| [SRC-3451CC474D-L000589](../../tests/test_api.py#L589) | 589 | `"        for fragment in (b'\"', b\"text\", b'\"', b\":\"):"` | — |
| [SRC-3451CC474D-L000590](../../tests/test_api.py#L590) | 590 | `"            time.sleep(0.08)"` | — |
| [SRC-3451CC474D-L000591](../../tests/test_api.py#L591) | 591 | `"            try:"` | — |
| [SRC-3451CC474D-L000592](../../tests/test_api.py#L592) | 592 | `"                client.sendall(fragment)"` | — |
| [SRC-3451CC474D-L000593](../../tests/test_api.py#L593) | 593 | `"            except OSError:"` | — |
| [SRC-3451CC474D-L000594](../../tests/test_api.py#L594) | 594 | `"                break"` | — |
| [SRC-3451CC474D-L000595](../../tests/test_api.py#L595) | 595 | `""` | — |
| [SRC-3451CC474D-L000596](../../tests/test_api.py#L596) | 596 | `"        response = bytearray()"` | — |
| [SRC-3451CC474D-L000597](../../tests/test_api.py#L597) | 597 | `"        while True:"` | — |
| [SRC-3451CC474D-L000598](../../tests/test_api.py#L598) | 598 | `"            try:"` | — |
| [SRC-3451CC474D-L000599](../../tests/test_api.py#L599) | 599 | `"                chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000600](../../tests/test_api.py#L600) | 600 | `"            except TimeoutError:"` | — |
| [SRC-3451CC474D-L000601](../../tests/test_api.py#L601) | 601 | `"                break"` | — |
| [SRC-3451CC474D-L000602](../../tests/test_api.py#L602) | 602 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000603](../../tests/test_api.py#L603) | 603 | `"                break"` | — |
| [SRC-3451CC474D-L000604](../../tests/test_api.py#L604) | 604 | `"            response.extend(chunk)"` | — |
| [SRC-3451CC474D-L000605](../../tests/test_api.py#L605) | 605 | `""` | — |
| [SRC-3451CC474D-L000606](../../tests/test_api.py#L606) | 606 | `"    elapsed = time.monotonic() - started"` | — |
| [SRC-3451CC474D-L000607](../../tests/test_api.py#L607) | 607 | `"    assert response.startswith(b\"HTTP/1.0 408\")"` | — |
| [SRC-3451CC474D-L000608](../../tests/test_api.py#L608) | 608 | `"    assert b\"request body read timed out\" in response"` | — |
| [SRC-3451CC474D-L000609](../../tests/test_api.py#L609) | 609 | `"    assert elapsed < 1.5"` | — |
| [SRC-3451CC474D-L000610](../../tests/test_api.py#L610) | 610 | `""` | — |
| [SRC-3451CC474D-L000611](../../tests/test_api.py#L611) | 611 | `""` | — |
| [SRC-3451CC474D-L000612](../../tests/test_api.py#L612) | 612 | `""` | — |
| [SRC-3451CC474D-L000613](../../tests/test_api.py#L613) | 613 | `"def test_api_absolute_header_deadline_stops_slow_trickle(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000614](../../tests/test_api.py#L614) | 614 | `"    \"\"\"Header bytes arriving before idle timeout must not extend the total deadline.\"\"\""` | — |
| [SRC-3451CC474D-L000615](../../tests/test_api.py#L615) | 615 | `"    import time"` | — |
| [SRC-3451CC474D-L000616](../../tests/test_api.py#L616) | 616 | `""` | — |
| [SRC-3451CC474D-L000617](../../tests/test_api.py#L617) | 617 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000618](../../tests/test_api.py#L618) | 618 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000619](../../tests/test_api.py#L619) | 619 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_HEADER_READ_TIMEOUT_SECONDS\", 0.5)"` | — |
| [SRC-3451CC474D-L000620](../../tests/test_api.py#L620) | 620 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_HEADER_IDLE_TIMEOUT_SECONDS\", 0.35)"` | — |
| [SRC-3451CC474D-L000621](../../tests/test_api.py#L621) | 621 | `"    host, port = local_api.removeprefix(\"http://\").rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000622](../../tests/test_api.py#L622) | 622 | `""` | — |
| [SRC-3451CC474D-L000623](../../tests/test_api.py#L623) | 623 | `"    with socket.create_connection((host, int(port)), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000624](../../tests/test_api.py#L624) | 624 | `"        client.settimeout(1.2)"` | — |
| [SRC-3451CC474D-L000625](../../tests/test_api.py#L625) | 625 | `"        started = time.monotonic()"` | — |
| [SRC-3451CC474D-L000626](../../tests/test_api.py#L626) | 626 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000627](../../tests/test_api.py#L627) | 627 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000628](../../tests/test_api.py#L628) | 628 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000629](../../tests/test_api.py#L629) | 629 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000630](../../tests/test_api.py#L630) | 630 | `"            b\"Content-Length: 40\\r\\n\""` | — |
| [SRC-3451CC474D-L000631](../../tests/test_api.py#L631) | 631 | `"            b\"X-Slow: \""` | — |
| [SRC-3451CC474D-L000632](../../tests/test_api.py#L632) | 632 | `"        )"` | — |
| [SRC-3451CC474D-L000633](../../tests/test_api.py#L633) | 633 | `"        # Each tiny fragment is sent well before the 0.35s idle timeout. No"` | — |
| [SRC-3451CC474D-L000634](../../tests/test_api.py#L634) | 634 | `"        # newline completes X-Slow, so only an absolute header deadline can stop it."` | — |
| [SRC-3451CC474D-L000635](../../tests/test_api.py#L635) | 635 | `"        for fragment in (b\"a\", b\"b\", b\"c\", b\"d\", b\"e\", b\"f\", b\"g\", b\"h\", b\"i\"):"` | — |
| [SRC-3451CC474D-L000636](../../tests/test_api.py#L636) | 636 | `"            time.sleep(0.12)"` | — |
| [SRC-3451CC474D-L000637](../../tests/test_api.py#L637) | 637 | `"            try:"` | — |
| [SRC-3451CC474D-L000638](../../tests/test_api.py#L638) | 638 | `"                client.sendall(fragment)"` | — |
| [SRC-3451CC474D-L000639](../../tests/test_api.py#L639) | 639 | `"            except OSError:"` | — |
| [SRC-3451CC474D-L000640](../../tests/test_api.py#L640) | 640 | `"                break"` | — |
| [SRC-3451CC474D-L000641](../../tests/test_api.py#L641) | 641 | `""` | — |
| [SRC-3451CC474D-L000642](../../tests/test_api.py#L642) | 642 | `"        response = bytearray()"` | — |
| [SRC-3451CC474D-L000643](../../tests/test_api.py#L643) | 643 | `"        while True:"` | — |
| [SRC-3451CC474D-L000644](../../tests/test_api.py#L644) | 644 | `"            try:"` | — |
| [SRC-3451CC474D-L000645](../../tests/test_api.py#L645) | 645 | `"                chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000646](../../tests/test_api.py#L646) | 646 | `"            except TimeoutError:"` | — |
| [SRC-3451CC474D-L000647](../../tests/test_api.py#L647) | 647 | `"                break"` | — |
| [SRC-3451CC474D-L000648](../../tests/test_api.py#L648) | 648 | `"            except OSError:"` | — |
| [SRC-3451CC474D-L000649](../../tests/test_api.py#L649) | 649 | `"                break"` | — |
| [SRC-3451CC474D-L000650](../../tests/test_api.py#L650) | 650 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000651](../../tests/test_api.py#L651) | 651 | `"                break"` | — |
| [SRC-3451CC474D-L000652](../../tests/test_api.py#L652) | 652 | `"            response.extend(chunk)"` | — |
| [SRC-3451CC474D-L000653](../../tests/test_api.py#L653) | 653 | `"        elapsed = time.monotonic() - started"` | — |
| [SRC-3451CC474D-L000654](../../tests/test_api.py#L654) | 654 | `""` | — |
| [SRC-3451CC474D-L000655](../../tests/test_api.py#L655) | 655 | `"    assert elapsed < 0.8"` | — |
| [SRC-3451CC474D-L000656](../../tests/test_api.py#L656) | 656 | `"    # The timed-out request never reached application dispatch; the handler closes silently."` | — |
| [SRC-3451CC474D-L000657](../../tests/test_api.py#L657) | 657 | `"    assert response == b\"\""` | — |
| [SRC-3451CC474D-L000658](../../tests/test_api.py#L658) | 658 | `""` | — |
| [SRC-3451CC474D-L000659](../../tests/test_api.py#L659) | 659 | `"def test_public_preflight_does_not_trust_spoofed_forwarded_host(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000660](../../tests/test_api.py#L660) | 660 | `"    \"\"\"A client-controlled X-Forwarded-Host must not grant an origin CORS access.\"\"\""` | — |
| [SRC-3451CC474D-L000661](../../tests/test_api.py#L661) | 661 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000662](../../tests/test_api.py#L662) | 662 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000663](../../tests/test_api.py#L663) | 663 | `""` | — |
| [SRC-3451CC474D-L000664](../../tests/test_api.py#L664) | 664 | `"    request = Request("` | — |
| [SRC-3451CC474D-L000665](../../tests/test_api.py#L665) | 665 | `"        local_api + \"/api/agent\","` | — |
| [SRC-3451CC474D-L000666](../../tests/test_api.py#L666) | 666 | `"        method=\"OPTIONS\","` | — |
| [SRC-3451CC474D-L000667](../../tests/test_api.py#L667) | 667 | `"        headers={"` | — |
| [SRC-3451CC474D-L000668](../../tests/test_api.py#L668) | 668 | `"            \"Origin\": \"https://attacker.example\","` | — |
| [SRC-3451CC474D-L000669](../../tests/test_api.py#L669) | 669 | `"            \"X-Forwarded-Host\": \"attacker.example\","` | — |
| [SRC-3451CC474D-L000670](../../tests/test_api.py#L670) | 670 | `"            \"X-Forwarded-Proto\": \"https\","` | — |
| [SRC-3451CC474D-L000671](../../tests/test_api.py#L671) | 671 | `"            \"Access-Control-Request-Method\": \"POST\","` | — |
| [SRC-3451CC474D-L000672](../../tests/test_api.py#L672) | 672 | `"            \"Access-Control-Request-Headers\": \"authorization,content-type\","` | — |
| [SRC-3451CC474D-L000673](../../tests/test_api.py#L673) | 673 | `"        },"` | — |
| [SRC-3451CC474D-L000674](../../tests/test_api.py#L674) | 674 | `"    )"` | — |
| [SRC-3451CC474D-L000675](../../tests/test_api.py#L675) | 675 | `"    with pytest.raises(HTTPError) as error:"` | — |
| [SRC-3451CC474D-L000676](../../tests/test_api.py#L676) | 676 | `"        urlopen(request, timeout=3)"` | — |
| [SRC-3451CC474D-L000677](../../tests/test_api.py#L677) | 677 | `"    assert error.value.code == 403"` | — |
| [SRC-3451CC474D-L000678](../../tests/test_api.py#L678) | 678 | `""` | — |
| [SRC-3451CC474D-L000679](../../tests/test_api.py#L679) | 679 | `""` | — |
| [SRC-3451CC474D-L000680](../../tests/test_api.py#L680) | 680 | `"def test_public_origin_still_allows_the_requested_host(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000681](../../tests/test_api.py#L681) | 681 | `"    \"\"\"Same-service public UI remains compatible when the request Host is trusted.\"\"\""` | — |
| [SRC-3451CC474D-L000682](../../tests/test_api.py#L682) | 682 | `"    from types import SimpleNamespace"` | — |
| [SRC-3451CC474D-L000683](../../tests/test_api.py#L683) | 683 | `""` | — |
| [SRC-3451CC474D-L000684](../../tests/test_api.py#L684) | 684 | `"    from api.omarai import Handler"` | — |
| [SRC-3451CC474D-L000685](../../tests/test_api.py#L685) | 685 | `""` | — |
| [SRC-3451CC474D-L000686](../../tests/test_api.py#L686) | 686 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000687](../../tests/test_api.py#L687) | 687 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000688](../../tests/test_api.py#L688) | 688 | `"    handler = SimpleNamespace("` | — |
| [SRC-3451CC474D-L000689](../../tests/test_api.py#L689) | 689 | `"        headers={"` | — |
| [SRC-3451CC474D-L000690](../../tests/test_api.py#L690) | 690 | `"            \"Host\": \"omarai.example\","` | — |
| [SRC-3451CC474D-L000691](../../tests/test_api.py#L691) | 691 | `"            \"X-Forwarded-Proto\": \"https\","` | — |
| [SRC-3451CC474D-L000692](../../tests/test_api.py#L692) | 692 | `"            \"X-Forwarded-Host\": \"attacker.example\","` | — |
| [SRC-3451CC474D-L000693](../../tests/test_api.py#L693) | 693 | `"        }"` | — |
| [SRC-3451CC474D-L000694](../../tests/test_api.py#L694) | 694 | `"    )"` | — |
| [SRC-3451CC474D-L000695](../../tests/test_api.py#L695) | 695 | `"    allowed = Handler._allowed_origins(handler)"` | — |
| [SRC-3451CC474D-L000696](../../tests/test_api.py#L696) | 696 | `"    assert \"https://omarai.example\" in allowed"` | — |
| [SRC-3451CC474D-L000697](../../tests/test_api.py#L697) | 697 | `"    assert \"https://attacker.example\" not in allowed"` | — |
| [SRC-3451CC474D-L000698](../../tests/test_api.py#L698) | 698 | `""` | — |
| [SRC-3451CC474D-L000699](../../tests/test_api.py#L699) | 699 | `""` | — |
| [SRC-3451CC474D-L000700](../../tests/test_api.py#L700) | 700 | `""` | — |
| [SRC-3451CC474D-L000701](../../tests/test_api.py#L701) | 701 | `"def test_security_headers_apply_to_json_and_html_responses(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000702](../../tests/test_api.py#L702) | 702 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000703](../../tests/test_api.py#L703) | 703 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000704](../../tests/test_api.py#L704) | 704 | `"    for path in (\"/api/health\", \"/\"):"` | — |
| [SRC-3451CC474D-L000705](../../tests/test_api.py#L705) | 705 | `"        request = Request(local_api + path)"` | — |
| [SRC-3451CC474D-L000706](../../tests/test_api.py#L706) | 706 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000707](../../tests/test_api.py#L707) | 707 | `"            headers = {name.lower(): value for name, value in response.headers.items()}"` | — |
| [SRC-3451CC474D-L000708](../../tests/test_api.py#L708) | 708 | `"            assert headers[\"x-content-type-options\"] == \"nosniff\""` | — |
| [SRC-3451CC474D-L000709](../../tests/test_api.py#L709) | 709 | `"            assert headers[\"x-frame-options\"] == \"DENY\""` | — |
| [SRC-3451CC474D-L000710](../../tests/test_api.py#L710) | 710 | `"            assert headers[\"referrer-policy\"] == \"strict-origin-when-cross-origin\""` | — |
| [SRC-3451CC474D-L000711](../../tests/test_api.py#L711) | 711 | `"            assert \"default-src 'self'\" in headers[\"content-security-policy\"]"` | — |
| [SRC-3451CC474D-L000712](../../tests/test_api.py#L712) | 712 | `"            policy = headers[\"content-security-policy\"]"` | — |
| [SRC-3451CC474D-L000713](../../tests/test_api.py#L713) | 713 | `"            assert \"frame-ancestors 'none'\" in policy"` | — |
| [SRC-3451CC474D-L000714](../../tests/test_api.py#L714) | 714 | `"            assert \"'unsafe-inline'\" not in policy"` | — |
| [SRC-3451CC474D-L000715](../../tests/test_api.py#L715) | 715 | `"            assert \"'sha256-\" in policy"` | — |
| [SRC-3451CC474D-L000716](../../tests/test_api.py#L716) | 716 | `"            assert headers[\"permissions-policy\"] == ("` | — |
| [SRC-3451CC474D-L000717](../../tests/test_api.py#L717) | 717 | `"                \"camera=(), microphone=(), geolocation=()\""` | — |
| [SRC-3451CC474D-L000718](../../tests/test_api.py#L718) | 718 | `"            )"` | — |
| [SRC-3451CC474D-L000719](../../tests/test_api.py#L719) | 719 | `""` | — |
| [SRC-3451CC474D-L000720](../../tests/test_api.py#L720) | 720 | `""` | — |
| [SRC-3451CC474D-L000721](../../tests/test_api.py#L721) | 721 | `"def test_health_exposes_only_validated_image_baked_sha(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L000722](../../tests/test_api.py#L722) | 722 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000723](../../tests/test_api.py#L723) | 723 | `""` | — |
| [SRC-3451CC474D-L000724](../../tests/test_api.py#L724) | 724 | `"    build_sha_file = tmp_path / \"BUILD_SHA\""` | — |
| [SRC-3451CC474D-L000725](../../tests/test_api.py#L725) | 725 | `"    monkeypatch.setattr(api_module, \"BUILD_SHA_FILE\", build_sha_file)"` | — |
| [SRC-3451CC474D-L000726](../../tests/test_api.py#L726) | 726 | `"    assert api_module._build_sha() == \"unknown\""` | — |
| [SRC-3451CC474D-L000727](../../tests/test_api.py#L727) | 727 | `"    build_sha_file.write_text(\"a\" * 40, encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000728](../../tests/test_api.py#L728) | 728 | `"    assert api_module._build_sha() == \"a\" * 40"` | — |
| [SRC-3451CC474D-L000729](../../tests/test_api.py#L729) | 729 | `"    build_sha_file.write_text(\"not-a-git-sha\", encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000730](../../tests/test_api.py#L730) | 730 | `"    assert api_module._build_sha() == \"unknown\""` | — |
| [SRC-3451CC474D-L000731](../../tests/test_api.py#L731) | 731 | `""` | — |
| [SRC-3451CC474D-L000732](../../tests/test_api.py#L732) | 732 | `""` | — |
| [SRC-3451CC474D-L000733](../../tests/test_api.py#L733) | 733 | `""` | — |
| [SRC-3451CC474D-L000734](../../tests/test_api.py#L734) | 734 | `"@pytest.mark.parametrize("` | — |
| [SRC-3451CC474D-L000735](../../tests/test_api.py#L735) | 735 | `"    (\"variable\", \"source\"),"` | — |
| [SRC-3451CC474D-L000736](../../tests/test_api.py#L736) | 736 | `"    ["` | — |
| [SRC-3451CC474D-L000737](../../tests/test_api.py#L737) | 737 | `"        (\"RAILWAY_GIT_COMMIT_SHA\", \"platform:railway\"),"` | — |
| [SRC-3451CC474D-L000738](../../tests/test_api.py#L738) | 738 | `"        (\"RENDER_GIT_COMMIT\", \"platform:render\"),"` | — |
| [SRC-3451CC474D-L000739](../../tests/test_api.py#L739) | 739 | `"    ],"` | — |
| [SRC-3451CC474D-L000740](../../tests/test_api.py#L740) | 740 | `")"` | — |
| [SRC-3451CC474D-L000741](../../tests/test_api.py#L741) | 741 | `"def test_build_identity_uses_validated_platform_commit_when_image_sha_is_unavailable("` | — |
| [SRC-3451CC474D-L000742](../../tests/test_api.py#L742) | 742 | `"    monkeypatch, tmp_path, variable, source"` | — |
| [SRC-3451CC474D-L000743](../../tests/test_api.py#L743) | 743 | `"):"` | — |
| [SRC-3451CC474D-L000744](../../tests/test_api.py#L744) | 744 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000745](../../tests/test_api.py#L745) | 745 | `""` | — |
| [SRC-3451CC474D-L000746](../../tests/test_api.py#L746) | 746 | `"    build_sha_file = tmp_path / \"BUILD_SHA\""` | — |
| [SRC-3451CC474D-L000747](../../tests/test_api.py#L747) | 747 | `"    monkeypatch.setattr(api_module, \"BUILD_SHA_FILE\", build_sha_file)"` | — |
| [SRC-3451CC474D-L000748](../../tests/test_api.py#L748) | 748 | `"    build_sha_file.write_text(\"unknown\", encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000749](../../tests/test_api.py#L749) | 749 | `"    for name, _label in api_module._PLATFORM_BUILD_SHA_ENVIRONMENTS:"` | — |
| [SRC-3451CC474D-L000750](../../tests/test_api.py#L750) | 750 | `"        monkeypatch.delenv(name, raising=False)"` | — |
| [SRC-3451CC474D-L000751](../../tests/test_api.py#L751) | 751 | `"    monkeypatch.setenv(variable, \"b\" * 40)"` | — |
| [SRC-3451CC474D-L000752](../../tests/test_api.py#L752) | 752 | `""` | — |
| [SRC-3451CC474D-L000753](../../tests/test_api.py#L753) | 753 | `"    assert api_module._build_identity() == (\"b\" * 40, source)"` | — |
| [SRC-3451CC474D-L000754](../../tests/test_api.py#L754) | 754 | `""` | — |
| [SRC-3451CC474D-L000755](../../tests/test_api.py#L755) | 755 | `""` | — |
| [SRC-3451CC474D-L000756](../../tests/test_api.py#L756) | 756 | `"def test_invalid_platform_commit_does_not_create_build_identity(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L000757](../../tests/test_api.py#L757) | 757 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000758](../../tests/test_api.py#L758) | 758 | `""` | — |
| [SRC-3451CC474D-L000759](../../tests/test_api.py#L759) | 759 | `"    monkeypatch.setattr(api_module, \"BUILD_SHA_FILE\", tmp_path / \"BUILD_SHA\")"` | — |
| [SRC-3451CC474D-L000760](../../tests/test_api.py#L760) | 760 | `"    api_module.BUILD_SHA_FILE.write_text(\"unknown\", encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000761](../../tests/test_api.py#L761) | 761 | `"    monkeypatch.setenv(\"RAILWAY_GIT_COMMIT_SHA\", \"not-a-sha\")"` | — |
| [SRC-3451CC474D-L000762](../../tests/test_api.py#L762) | 762 | `"    monkeypatch.setenv(\"RENDER_GIT_COMMIT\", \"also-not-a-sha\")"` | — |
| [SRC-3451CC474D-L000763](../../tests/test_api.py#L763) | 763 | `""` | — |
| [SRC-3451CC474D-L000764](../../tests/test_api.py#L764) | 764 | `"    assert api_module._build_identity() == (\"unknown\", \"unknown\")"` | — |
| [SRC-3451CC474D-L000765](../../tests/test_api.py#L765) | 765 | `""` | — |
| [SRC-3451CC474D-L000766](../../tests/test_api.py#L766) | 766 | `""` | — |
| [SRC-3451CC474D-L000767](../../tests/test_api.py#L767) | 767 | `""` | — |
| [SRC-3451CC474D-L000768](../../tests/test_api.py#L768) | 768 | `"def test_lead_store_uses_configured_database_path(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L000769](../../tests/test_api.py#L769) | 769 | `"    from api.omarai import _lead_store_from_environment"` | — |
| [SRC-3451CC474D-L000770](../../tests/test_api.py#L770) | 770 | `""` | — |
| [SRC-3451CC474D-L000771](../../tests/test_api.py#L771) | 771 | `"    database_path = tmp_path / \"persistent\" / \"omarai.sqlite3\""` | — |
| [SRC-3451CC474D-L000772](../../tests/test_api.py#L772) | 772 | `"    monkeypatch.setenv(\"OMARAI_DB_PATH\", str(database_path))"` | — |
| [SRC-3451CC474D-L000773](../../tests/test_api.py#L773) | 773 | `""` | — |
| [SRC-3451CC474D-L000774](../../tests/test_api.py#L774) | 774 | `"    store = _lead_store_from_environment()"` | — |
| [SRC-3451CC474D-L000775](../../tests/test_api.py#L775) | 775 | `""` | — |
| [SRC-3451CC474D-L000776](../../tests/test_api.py#L776) | 776 | `"    assert store.path == database_path"` | — |
| [SRC-3451CC474D-L000777](../../tests/test_api.py#L777) | 777 | `"    assert database_path.is_file()"` | — |
| [SRC-3451CC474D-L000778](../../tests/test_api.py#L778) | 778 | `""` | — |
| [SRC-3451CC474D-L000779](../../tests/test_api.py#L779) | 779 | `""` | — |
| [SRC-3451CC474D-L000780](../../tests/test_api.py#L780) | 780 | `""` | — |
| [SRC-3451CC474D-L000781](../../tests/test_api.py#L781) | 781 | `"def test_agent_concurrency_slot_released_after_operation_error(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000782](../../tests/test_api.py#L782) | 782 | `"    from api.omarai import WebAgent"` | — |
| [SRC-3451CC474D-L000783](../../tests/test_api.py#L783) | 783 | `""` | — |
| [SRC-3451CC474D-L000784](../../tests/test_api.py#L784) | 784 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000785](../../tests/test_api.py#L785) | 785 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000786](../../tests/test_api.py#L786) | 786 | `"    monkeypatch.setattr(Handler, \"_request_times\", defaultdict(deque))"` | — |
| [SRC-3451CC474D-L000787](../../tests/test_api.py#L787) | 787 | `"    monkeypatch.setattr(Handler, \"_rate_last_cleanup\", 0.0)"` | — |
| [SRC-3451CC474D-L000788](../../tests/test_api.py#L788) | 788 | `"    monkeypatch.setattr(Handler, \"_agent_semaphore\", threading.BoundedSemaphore(1))"` | — |
| [SRC-3451CC474D-L000789](../../tests/test_api.py#L789) | 789 | `"    state = {\"fail\": True}"` | — |
| [SRC-3451CC474D-L000790](../../tests/test_api.py#L790) | 790 | `""` | — |
| [SRC-3451CC474D-L000791](../../tests/test_api.py#L791) | 791 | `"    def answer_with_one_transient_failure(self, question, history=None, mode=\"auto\"):"` | — |
| [SRC-3451CC474D-L000792](../../tests/test_api.py#L792) | 792 | `"        if state[\"fail\"]:"` | — |
| [SRC-3451CC474D-L000793](../../tests/test_api.py#L793) | 793 | `"            raise RuntimeError(\"synthetic operation failure\")"` | — |
| [SRC-3451CC474D-L000794](../../tests/test_api.py#L794) | 794 | `"        return {"` | — |
| [SRC-3451CC474D-L000795](../../tests/test_api.py#L795) | 795 | `"            \"answer\": \"اختبار ناجح\","` | — |
| [SRC-3451CC474D-L000796](../../tests/test_api.py#L796) | 796 | `"            \"question\": question,"` | — |
| [SRC-3451CC474D-L000797](../../tests/test_api.py#L797) | 797 | `"            \"search_query\": question,"` | — |
| [SRC-3451CC474D-L000798](../../tests/test_api.py#L798) | 798 | `"            \"search_queries\": [],"` | — |
| [SRC-3451CC474D-L000799](../../tests/test_api.py#L799) | 799 | `"            \"search_report\": {"` | — |
| [SRC-3451CC474D-L000800](../../tests/test_api.py#L800) | 800 | `"                \"search_attempted\": False,"` | — |
| [SRC-3451CC474D-L000801](../../tests/test_api.py#L801) | 801 | `"                \"search_outcome\": \"not_attempted\","` | — |
| [SRC-3451CC474D-L000802](../../tests/test_api.py#L802) | 802 | `"            },"` | — |
| [SRC-3451CC474D-L000803](../../tests/test_api.py#L803) | 803 | `"            \"sources\": [],"` | — |
| [SRC-3451CC474D-L000804](../../tests/test_api.py#L804) | 804 | `"            \"used_language_model\": False,"` | — |
| [SRC-3451CC474D-L000805](../../tests/test_api.py#L805) | 805 | `"            \"used_web_search\": False,"` | — |
| [SRC-3451CC474D-L000806](../../tests/test_api.py#L806) | 806 | `"            \"search_attempted\": False,"` | — |
| [SRC-3451CC474D-L000807](../../tests/test_api.py#L807) | 807 | `"            \"used_social_search\": False,"` | — |
| [SRC-3451CC474D-L000808](../../tests/test_api.py#L808) | 808 | `"            \"warnings\": [],"` | — |
| [SRC-3451CC474D-L000809](../../tests/test_api.py#L809) | 809 | `"            \"kind\": \"web_fallback\","` | — |
| [SRC-3451CC474D-L000810](../../tests/test_api.py#L810) | 810 | `"        }"` | — |
| [SRC-3451CC474D-L000811](../../tests/test_api.py#L811) | 811 | `""` | — |
| [SRC-3451CC474D-L000812](../../tests/test_api.py#L812) | 812 | `"    monkeypatch.setattr(WebAgent, \"answer\", answer_with_one_transient_failure)"` | — |
| [SRC-3451CC474D-L000813](../../tests/test_api.py#L813) | 813 | `""` | — |
| [SRC-3451CC474D-L000814](../../tests/test_api.py#L814) | 814 | `"    status, payload = request_json("` | — |
| [SRC-3451CC474D-L000815](../../tests/test_api.py#L815) | 815 | `"        local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"الطلب الأول\"}"` | — |
| [SRC-3451CC474D-L000816](../../tests/test_api.py#L816) | 816 | `"    )"` | — |
| [SRC-3451CC474D-L000817](../../tests/test_api.py#L817) | 817 | `"    assert status == 500"` | — |
| [SRC-3451CC474D-L000818](../../tests/test_api.py#L818) | 818 | `"    assert payload[\"error\"] == \"internal server error\""` | — |
| [SRC-3451CC474D-L000819](../../tests/test_api.py#L819) | 819 | `""` | — |
| [SRC-3451CC474D-L000820](../../tests/test_api.py#L820) | 820 | `"    state[\"fail\"] = False"` | — |
| [SRC-3451CC474D-L000821](../../tests/test_api.py#L821) | 821 | `"    status, payload = request_json("` | — |
| [SRC-3451CC474D-L000822](../../tests/test_api.py#L822) | 822 | `"        local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"الطلب الثاني\"}"` | — |
| [SRC-3451CC474D-L000823](../../tests/test_api.py#L823) | 823 | `"    )"` | — |
| [SRC-3451CC474D-L000824](../../tests/test_api.py#L824) | 824 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000825](../../tests/test_api.py#L825) | 825 | `"    assert payload[\"answer\"] == \"اختبار ناجح\""` | — |
| [SRC-3451CC474D-L000826](../../tests/test_api.py#L826) | 826 | `""` | — |
| [SRC-3451CC474D-L000827](../../tests/test_api.py#L827) | 827 | `""` | — |
| [SRC-3451CC474D-L000828](../../tests/test_api.py#L828) | 828 | `"def test_csp_hashes_match_all_first_party_inline_content_and_attributes():"` | — |
| [SRC-3451CC474D-L000829](../../tests/test_api.py#L829) | 829 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000830](../../tests/test_api.py#L830) | 830 | `""` | — |
| [SRC-3451CC474D-L000831](../../tests/test_api.py#L831) | 831 | `"    policy = api_module._content_security_policy()"` | — |
| [SRC-3451CC474D-L000832](../../tests/test_api.py#L832) | 832 | `"    assert \"'unsafe-inline'\" not in policy"` | — |
| [SRC-3451CC474D-L000833](../../tests/test_api.py#L833) | 833 | `"    script_blocks = 0"` | — |
| [SRC-3451CC474D-L000834](../../tests/test_api.py#L834) | 834 | `"    style_blocks = 0"` | — |
| [SRC-3451CC474D-L000835](../../tests/test_api.py#L835) | 835 | `"    style_attributes = 0"` | — |
| [SRC-3451CC474D-L000836](../../tests/test_api.py#L836) | 836 | `"    for html_path in api_module.ROOT.glob(\"*.html\"):"` | — |
| [SRC-3451CC474D-L000837](../../tests/test_api.py#L837) | 837 | `"        document = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3451CC474D-L000838](../../tests/test_api.py#L838) | 838 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000839](../../tests/test_api.py#L839) | 839 | `"            r\"<script\\b(?P<attrs>[^>]*)>(?P<body>.*?)</script\\s*>\","` | — |
| [SRC-3451CC474D-L000840](../../tests/test_api.py#L840) | 840 | `"            document,"` | — |
| [SRC-3451CC474D-L000841](../../tests/test_api.py#L841) | 841 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L000842](../../tests/test_api.py#L842) | 842 | `"        ):"` | — |
| [SRC-3451CC474D-L000843](../../tests/test_api.py#L843) | 843 | `"            if re.search(r\"\\bsrc\\s*=\", match.group(\"attrs\"), re.IGNORECASE):"` | — |
| [SRC-3451CC474D-L000844](../../tests/test_api.py#L844) | 844 | `"                continue"` | — |
| [SRC-3451CC474D-L000845](../../tests/test_api.py#L845) | 845 | `"            script_blocks += 1"` | — |
| [SRC-3451CC474D-L000846](../../tests/test_api.py#L846) | 846 | `"            assert api_module._csp_hash_source(match.group(\"body\")) in policy"` | — |
| [SRC-3451CC474D-L000847](../../tests/test_api.py#L847) | 847 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000848](../../tests/test_api.py#L848) | 848 | `"            r\"<style\\b[^>]*>(?P<body>.*?)</style\\s*>\","` | — |
| [SRC-3451CC474D-L000849](../../tests/test_api.py#L849) | 849 | `"            document,"` | — |
| [SRC-3451CC474D-L000850](../../tests/test_api.py#L850) | 850 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L000851](../../tests/test_api.py#L851) | 851 | `"        ):"` | — |
| [SRC-3451CC474D-L000852](../../tests/test_api.py#L852) | 852 | `"            style_blocks += 1"` | — |
| [SRC-3451CC474D-L000853](../../tests/test_api.py#L853) | 853 | `"            assert api_module._csp_hash_source(match.group(\"body\")) in policy"` | — |
| [SRC-3451CC474D-L000854](../../tests/test_api.py#L854) | 854 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000855](../../tests/test_api.py#L855) | 855 | `"            r\"\"\"\\bstyle\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-3451CC474D-L000856](../../tests/test_api.py#L856) | 856 | `"            document,"` | — |
| [SRC-3451CC474D-L000857](../../tests/test_api.py#L857) | 857 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L000858](../../tests/test_api.py#L858) | 858 | `"        ):"` | — |
| [SRC-3451CC474D-L000859](../../tests/test_api.py#L859) | 859 | `"            style_attributes += 1"` | — |
| [SRC-3451CC474D-L000860](../../tests/test_api.py#L860) | 860 | `"            assert api_module._csp_hash_source(match.group(2).strip()) in policy"` | — |
| [SRC-3451CC474D-L000861](../../tests/test_api.py#L861) | 861 | `"    assert script_blocks >= 2"` | — |
| [SRC-3451CC474D-L000862](../../tests/test_api.py#L862) | 862 | `"    assert style_blocks >= 2"` | — |
| [SRC-3451CC474D-L000863](../../tests/test_api.py#L863) | 863 | `"    assert style_attributes >= 10"` | — |
| [SRC-3451CC474D-L000864](../../tests/test_api.py#L864) | 864 | `""` | — |
| [SRC-3451CC474D-L000865](../../tests/test_api.py#L865) | 865 | `""` | — |
| [SRC-3451CC474D-L000866](../../tests/test_api.py#L866) | 866 | `"def test_dashboard_uses_delegated_status_action_not_inline_onclick():"` | — |
| [SRC-3451CC474D-L000867](../../tests/test_api.py#L867) | 867 | `"    dashboard = (Path(__file__).resolve().parents[1] / \"web\" / \"dashboard.html\").read_text("` | — |
| [SRC-3451CC474D-L000868](../../tests/test_api.py#L868) | 868 | `"        encoding=\"utf-8\""` | — |
| [SRC-3451CC474D-L000869](../../tests/test_api.py#L869) | 869 | `"    )"` | — |
| [SRC-3451CC474D-L000870](../../tests/test_api.py#L870) | 870 | `"    assert 'data-action=\"save-status\"' in dashboard"` | — |
| [SRC-3451CC474D-L000871](../../tests/test_api.py#L871) | 871 | `"    assert 'onclick=\"saveStatus' not in dashboard"` | — |
| [SRC-3451CC474D-L000872](../../tests/test_api.py#L872) | 872 | `"    assert \"\"\"data-lead-id=\"'+esc(l.id)+'\">\"\"\" in dashboard"` | — |
## اختبارات

### FILE-6CBA87B20C — [tests/test_aspect_planning.py](../../tests/test_aspect_planning.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6CBA87B20C-L000001](../../tests/test_aspect_planning.py#L1) | 1 | `"\"\"\"Unit tests for aspect extraction and evidence ledger (no network).\"\"\""` | — |
| [SRC-6CBA87B20C-L000002](../../tests/test_aspect_planning.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-6CBA87B20C-L000003](../../tests/test_aspect_planning.py#L3) | 3 | `""` | — |
| [SRC-6CBA87B20C-L000004](../../tests/test_aspect_planning.py#L4) | 4 | `"from agents.aspect_planning import ("` | — |
| [SRC-6CBA87B20C-L000005](../../tests/test_aspect_planning.py#L5) | 5 | `"    arabic_aspect_diagnostics,"` | — |
| [SRC-6CBA87B20C-L000006](../../tests/test_aspect_planning.py#L6) | 6 | `"    build_aspect_queries,"` | — |
| [SRC-6CBA87B20C-L000007](../../tests/test_aspect_planning.py#L7) | 7 | `"    build_evidence_ledger,"` | — |
| [SRC-6CBA87B20C-L000008](../../tests/test_aspect_planning.py#L8) | 8 | `"    extract_aspects,"` | — |
| [SRC-6CBA87B20C-L000009](../../tests/test_aspect_planning.py#L9) | 9 | `"    repair_queries_for_missing_aspects,"` | — |
| [SRC-6CBA87B20C-L000010](../../tests/test_aspect_planning.py#L10) | 10 | `")"` | — |
| [SRC-6CBA87B20C-L000011](../../tests/test_aspect_planning.py#L11) | 11 | `""` | — |
| [SRC-6CBA87B20C-L000012](../../tests/test_aspect_planning.py#L12) | 12 | `""` | — |
| [SRC-6CBA87B20C-L000013](../../tests/test_aspect_planning.py#L13) | 13 | `"def test_extract_aspects_from_min_hayth():"` | — |
| [SRC-6CBA87B20C-L000014](../../tests/test_aspect_planning.py#L14) | 14 | `"    q = ("` | — |
| [SRC-6CBA87B20C-L000015](../../tests/test_aspect_planning.py#L15) | 15 | `"        \"حلل السيارات الكهربائية في مصر من حيث السعر، البطارية، والضمان. \""` | — |
| [SRC-6CBA87B20C-L000016](../../tests/test_aspect_planning.py#L16) | 16 | `"        \"اذكر مصادر موثوقة.\""` | — |
| [SRC-6CBA87B20C-L000017](../../tests/test_aspect_planning.py#L17) | 17 | `"    )"` | — |
| [SRC-6CBA87B20C-L000018](../../tests/test_aspect_planning.py#L18) | 18 | `"    aspects = extract_aspects(q)"` | — |
| [SRC-6CBA87B20C-L000019](../../tests/test_aspect_planning.py#L19) | 19 | `"    assert \"السعر\" in aspects or any(\"سعر\" in a for a in aspects)"` | — |
| [SRC-6CBA87B20C-L000020](../../tests/test_aspect_planning.py#L20) | 20 | `"    assert any(\"بطار\" in a for a in aspects)"` | — |
| [SRC-6CBA87B20C-L000021](../../tests/test_aspect_planning.py#L21) | 21 | `"    assert any(\"ضمان\" in a for a in aspects)"` | — |
| [SRC-6CBA87B20C-L000022](../../tests/test_aspect_planning.py#L22) | 22 | `"    assert len(aspects) >= 3"` | — |
| [SRC-6CBA87B20C-L000023](../../tests/test_aspect_planning.py#L23) | 23 | `""` | — |
| [SRC-6CBA87B20C-L000024](../../tests/test_aspect_planning.py#L24) | 24 | `""` | — |
| [SRC-6CBA87B20C-L000025](../../tests/test_aspect_planning.py#L25) | 25 | `"def test_extract_aspects_from_multi_question_marks():"` | — |
| [SRC-6CBA87B20C-L000026](../../tests/test_aspect_planning.py#L26) | 26 | `"    q = \"ما سعر الآيفون في مصر؟ وما مدة الضمان؟ وهل تتوفر صيانة محلية؟\""` | — |
| [SRC-6CBA87B20C-L000027](../../tests/test_aspect_planning.py#L27) | 27 | `"    aspects = extract_aspects(q)"` | — |
| [SRC-6CBA87B20C-L000028](../../tests/test_aspect_planning.py#L28) | 28 | `"    assert len(aspects) >= 2"` | — |
| [SRC-6CBA87B20C-L000029](../../tests/test_aspect_planning.py#L29) | 29 | `""` | — |
| [SRC-6CBA87B20C-L000030](../../tests/test_aspect_planning.py#L30) | 30 | `""` | — |
| [SRC-6CBA87B20C-L000031](../../tests/test_aspect_planning.py#L31) | 31 | `"def test_build_aspect_queries_prioritizes_topic():"` | — |
| [SRC-6CBA87B20C-L000032](../../tests/test_aspect_planning.py#L32) | 32 | `"    queries = build_aspect_queries("` | — |
| [SRC-6CBA87B20C-L000033](../../tests/test_aspect_planning.py#L33) | 33 | `"        \"السيارات الكهربائية في مصر\","` | — |
| [SRC-6CBA87B20C-L000034](../../tests/test_aspect_planning.py#L34) | 34 | `"        [\"السعر\", \"الضمان\"],"` | — |
| [SRC-6CBA87B20C-L000035](../../tests/test_aspect_planning.py#L35) | 35 | `"        limit=5,"` | — |
| [SRC-6CBA87B20C-L000036](../../tests/test_aspect_planning.py#L36) | 36 | `"    )"` | — |
| [SRC-6CBA87B20C-L000037](../../tests/test_aspect_planning.py#L37) | 37 | `"    assert queries[0] == \"السيارات الكهربائية في مصر\""` | — |
| [SRC-6CBA87B20C-L000038](../../tests/test_aspect_planning.py#L38) | 38 | `"    assert any(\"السعر\" in q for q in queries)"` | — |
| [SRC-6CBA87B20C-L000039](../../tests/test_aspect_planning.py#L39) | 39 | `"    assert any(\"الضمان\" in q for q in queries)"` | — |
| [SRC-6CBA87B20C-L000040](../../tests/test_aspect_planning.py#L40) | 40 | `"    assert len(queries) <= 5"` | — |
| [SRC-6CBA87B20C-L000041](../../tests/test_aspect_planning.py#L41) | 41 | `""` | — |
| [SRC-6CBA87B20C-L000042](../../tests/test_aspect_planning.py#L42) | 42 | `""` | — |
| [SRC-6CBA87B20C-L000043](../../tests/test_aspect_planning.py#L43) | 43 | `"def test_evidence_ledger_marks_missing_and_covered():"` | — |
| [SRC-6CBA87B20C-L000044](../../tests/test_aspect_planning.py#L44) | 44 | `"    aspects = [\"السعر\", \"الضمان\"]"` | — |
| [SRC-6CBA87B20C-L000045](../../tests/test_aspect_planning.py#L45) | 45 | `"    sources = ["` | — |
| [SRC-6CBA87B20C-L000046](../../tests/test_aspect_planning.py#L46) | 46 | `"        {"` | — |
| [SRC-6CBA87B20C-L000047](../../tests/test_aspect_planning.py#L47) | 47 | `"            \"title\": \"أسعار السيارات الكهربائية\","` | — |
| [SRC-6CBA87B20C-L000048](../../tests/test_aspect_planning.py#L48) | 48 | `"            \"url\": \"https://example.com/prices\","` | — |
| [SRC-6CBA87B20C-L000049](../../tests/test_aspect_planning.py#L49) | 49 | `"            \"snippet\": \"متوسط السعر في مصر لعام 2026\","` | — |
| [SRC-6CBA87B20C-L000050](../../tests/test_aspect_planning.py#L50) | 50 | `"            \"page_text\": \"\","` | — |
| [SRC-6CBA87B20C-L000051](../../tests/test_aspect_planning.py#L51) | 51 | `"            \"provider\": \"test\","` | — |
| [SRC-6CBA87B20C-L000052](../../tests/test_aspect_planning.py#L52) | 52 | `"        }"` | — |
| [SRC-6CBA87B20C-L000053](../../tests/test_aspect_planning.py#L53) | 53 | `"    ]"` | — |
| [SRC-6CBA87B20C-L000054](../../tests/test_aspect_planning.py#L54) | 54 | `"    ledger = build_evidence_ledger(aspects, sources)"` | — |
| [SRC-6CBA87B20C-L000055](../../tests/test_aspect_planning.py#L55) | 55 | `"    assert \"السعر\" in ledger[\"covered\"] or any("` | — |
| [SRC-6CBA87B20C-L000056](../../tests/test_aspect_planning.py#L56) | 56 | `"        \"سعر\" in c for c in ledger[\"covered\"]"` | — |
| [SRC-6CBA87B20C-L000057](../../tests/test_aspect_planning.py#L57) | 57 | `"    )"` | — |
| [SRC-6CBA87B20C-L000058](../../tests/test_aspect_planning.py#L58) | 58 | `"    assert \"الضمان\" in ledger[\"missing\"]"` | — |
| [SRC-6CBA87B20C-L000059](../../tests/test_aspect_planning.py#L59) | 59 | `"    assert 0 <= ledger[\"coverage_ratio\"] <= 1"` | — |
