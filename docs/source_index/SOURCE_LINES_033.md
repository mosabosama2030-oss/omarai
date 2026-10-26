# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **033**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L002155 إلى SRC-F725E90B2A-L002954
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L002155](../../tests/test_web_agent.py#L2155) | 2155 | `"    assert result[\"search_report\"][\"lead_generation\"][\"related_results_reviewed\"] == 2"` | — |
| [SRC-F725E90B2A-L002156](../../tests/test_web_agent.py#L2156) | 2156 | `"    assert \"لم أعتبر إعلانات البيع\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L002157](../../tests/test_web_agent.py#L2157) | 2157 | `"    assert all(s[\"lead_qualification\"] == \"related_result_not_lead\" for s in result[\"sources\"])"` | — |
| [SRC-F725E90B2A-L002158](../../tests/test_web_agent.py#L2158) | 2158 | `""` | — |
| [SRC-F725E90B2A-L002159](../../tests/test_web_agent.py#L2159) | 2159 | `""` | — |
| [SRC-F725E90B2A-L002160](../../tests/test_web_agent.py#L2160) | 2160 | `"def test_lead_generation_search_plan_includes_high_intent_queries(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002161](../../tests/test_web_agent.py#L2161) | 2161 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002162](../../tests/test_web_agent.py#L2162) | 2162 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002163](../../tests/test_web_agent.py#L2163) | 2163 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002164](../../tests/test_web_agent.py#L2164) | 2164 | `"        \"queries\": [\"generic apartment listings\"],"` | — |
| [SRC-F725E90B2A-L002165](../../tests/test_web_agent.py#L2165) | 2165 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002166](../../tests/test_web_agent.py#L2166) | 2166 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002167](../../tests/test_web_agent.py#L2167) | 2167 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002168](../../tests/test_web_agent.py#L2168) | 2168 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002169](../../tests/test_web_agent.py#L2169) | 2169 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002170](../../tests/test_web_agent.py#L2170) | 2170 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002171](../../tests/test_web_agent.py#L2171) | 2171 | `"    }"` | — |
| [SRC-F725E90B2A-L002172](../../tests/test_web_agent.py#L2172) | 2172 | `""` | — |
| [SRC-F725E90B2A-L002173](../../tests/test_web_agent.py#L2173) | 2173 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L002174](../../tests/test_web_agent.py#L2174) | 2174 | `"        seen.update(research_plan)"` | — |
| [SRC-F725E90B2A-L002175](../../tests/test_web_agent.py#L2175) | 2175 | `"        source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002176](../../tests/test_web_agent.py#L2176) | 2176 | `"        source.update({"` | — |
| [SRC-F725E90B2A-L002177](../../tests/test_web_agent.py#L2177) | 2177 | `"            \"title\": \"مطلوب شقة تمليك في العاصمة الإدارية\","` | — |
| [SRC-F725E90B2A-L002178](../../tests/test_web_agent.py#L2178) | 2178 | `"            \"snippet\": \"صاحب المنشور يبحث عن شقة للشراء\","` | — |
| [SRC-F725E90B2A-L002179](../../tests/test_web_agent.py#L2179) | 2179 | `"            \"page_text\": \"مطلوب شقة تمليك في العاصمة الإدارية، أريد الشراء.\","` | — |
| [SRC-F725E90B2A-L002180](../../tests/test_web_agent.py#L2180) | 2180 | `"            \"queries\": list(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002181](../../tests/test_web_agent.py#L2181) | 2181 | `"        })"` | — |
| [SRC-F725E90B2A-L002182](../../tests/test_web_agent.py#L2182) | 2182 | `"        return [source], [], {"` | — |
| [SRC-F725E90B2A-L002183](../../tests/test_web_agent.py#L2183) | 2183 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002184](../../tests/test_web_agent.py#L2184) | 2184 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002185](../../tests/test_web_agent.py#L2185) | 2185 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L002186](../../tests/test_web_agent.py#L2186) | 2186 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L002187](../../tests/test_web_agent.py#L2187) | 2187 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L002188](../../tests/test_web_agent.py#L2188) | 2188 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L002189](../../tests/test_web_agent.py#L2189) | 2189 | `"            \"provider_counts\": {\"test_provider\": 1},"` | — |
| [SRC-F725E90B2A-L002190](../../tests/test_web_agent.py#L2190) | 2190 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L002191](../../tests/test_web_agent.py#L2191) | 2191 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002192](../../tests/test_web_agent.py#L2192) | 2192 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002193](../../tests/test_web_agent.py#L2193) | 2193 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002194](../../tests/test_web_agent.py#L2194) | 2194 | `"        }"` | — |
| [SRC-F725E90B2A-L002195](../../tests/test_web_agent.py#L2195) | 2195 | `""` | — |
| [SRC-F725E90B2A-L002196](../../tests/test_web_agent.py#L2196) | 2196 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda q, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002197](../../tests/test_web_agent.py#L2197) | 2197 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L002198](../../tests/test_web_agent.py#L2198) | 2198 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"عُثر على إشارة علنية محتملة [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L002199](../../tests/test_web_agent.py#L2199) | 2199 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L002200](../../tests/test_web_agent.py#L2200) | 2200 | `""` | — |
| [SRC-F725E90B2A-L002201](../../tests/test_web_agent.py#L2201) | 2201 | `"    result = agent.answer(\"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\")"` | — |
| [SRC-F725E90B2A-L002202](../../tests/test_web_agent.py#L2202) | 2202 | `""` | — |
| [SRC-F725E90B2A-L002203](../../tests/test_web_agent.py#L2203) | 2203 | `"    assert result[\"intent_route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-F725E90B2A-L002204](../../tests/test_web_agent.py#L2204) | 2204 | `"    assert seen[\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L002205](../../tests/test_web_agent.py#L2205) | 2205 | `"    assert len(seen[\"queries\"]) >= 4"` | — |
| [SRC-F725E90B2A-L002206](../../tests/test_web_agent.py#L2206) | 2206 | `"    assert any('\"مطلوب شراء\"' in q or '\"مطلوب شقه تمليك\"' in q for q in seen[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002207](../../tests/test_web_agent.py#L2207) | 2207 | `"    assert result[\"search_report\"][\"lead_generation\"][\"candidate_signal_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002208](../../tests/test_web_agent.py#L2208) | 2208 | `"    assert result[\"sources\"][0][\"lead_qualification\"] == \"public_buyer_intent_signal\""` | — |
| [SRC-F725E90B2A-L002209](../../tests/test_web_agent.py#L2209) | 2209 | `""` | — |
| [SRC-F725E90B2A-L002210](../../tests/test_web_agent.py#L2210) | 2210 | `""` | — |
| [SRC-F725E90B2A-L002211](../../tests/test_web_agent.py#L2211) | 2211 | `"def test_deepseek_search_adapter_normalizes_results_without_exposing_api_key(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002212](../../tests/test_web_agent.py#L2212) | 2212 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002213](../../tests/test_web_agent.py#L2213) | 2213 | `""` | — |
| [SRC-F725E90B2A-L002214](../../tests/test_web_agent.py#L2214) | 2214 | `"    monkeypatch.setenv(\"DEEPSEEK_SEARCH_API_KEY\", \"test-secret-key-that-must-not-appear\")"` | — |
| [SRC-F725E90B2A-L002215](../../tests/test_web_agent.py#L2215) | 2215 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002216](../../tests/test_web_agent.py#L2216) | 2216 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002217](../../tests/test_web_agent.py#L2217) | 2217 | `""` | — |
| [SRC-F725E90B2A-L002218](../../tests/test_web_agent.py#L2218) | 2218 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L002219](../../tests/test_web_agent.py#L2219) | 2219 | `"        def raise_for_status(self):"` | — |
| [SRC-F725E90B2A-L002220](../../tests/test_web_agent.py#L2220) | 2220 | `"            return None"` | — |
| [SRC-F725E90B2A-L002221](../../tests/test_web_agent.py#L2221) | 2221 | `""` | — |
| [SRC-F725E90B2A-L002222](../../tests/test_web_agent.py#L2222) | 2222 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L002223](../../tests/test_web_agent.py#L2223) | 2223 | `"            return {"` | — |
| [SRC-F725E90B2A-L002224](../../tests/test_web_agent.py#L2224) | 2224 | `"                \"results\": [{"` | — |
| [SRC-F725E90B2A-L002225](../../tests/test_web_agent.py#L2225) | 2225 | `"                    \"title\": \"Buyer wanted\","` | — |
| [SRC-F725E90B2A-L002226](../../tests/test_web_agent.py#L2226) | 2226 | `"                    \"url\": \"https://example.com/buyer\","` | — |
| [SRC-F725E90B2A-L002227](../../tests/test_web_agent.py#L2227) | 2227 | `"                    \"snippet\": \"Looking to buy a flat.\","` | — |
| [SRC-F725E90B2A-L002228](../../tests/test_web_agent.py#L2228) | 2228 | `"                    \"summary\": \"Looking to buy a flat in the requested area.\","` | — |
| [SRC-F725E90B2A-L002229](../../tests/test_web_agent.py#L2229) | 2229 | `"                    \"date\": \"2026-10-16T12:00:00Z\","` | — |
| [SRC-F725E90B2A-L002230](../../tests/test_web_agent.py#L2230) | 2230 | `"                    \"site_name\": \"Example\","` | — |
| [SRC-F725E90B2A-L002231](../../tests/test_web_agent.py#L2231) | 2231 | `"                    \"rerank_score\": 2.2,"` | — |
| [SRC-F725E90B2A-L002232](../../tests/test_web_agent.py#L2232) | 2232 | `"                    \"authority\": 2,"` | — |
| [SRC-F725E90B2A-L002233](../../tests/test_web_agent.py#L2233) | 2233 | `"                }]"` | — |
| [SRC-F725E90B2A-L002234](../../tests/test_web_agent.py#L2234) | 2234 | `"            }"` | — |
| [SRC-F725E90B2A-L002235](../../tests/test_web_agent.py#L2235) | 2235 | `""` | — |
| [SRC-F725E90B2A-L002236](../../tests/test_web_agent.py#L2236) | 2236 | `"    def fake_post(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002237](../../tests/test_web_agent.py#L2237) | 2237 | `"        seen[\"url\"] = url"` | — |
| [SRC-F725E90B2A-L002238](../../tests/test_web_agent.py#L2238) | 2238 | `"        seen.update(kwargs)"` | — |
| [SRC-F725E90B2A-L002239](../../tests/test_web_agent.py#L2239) | 2239 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L002240](../../tests/test_web_agent.py#L2240) | 2240 | `""` | — |
| [SRC-F725E90B2A-L002241](../../tests/test_web_agent.py#L2241) | 2241 | `"    monkeypatch.setattr(httpx, \"post\", fake_post)"` | — |
| [SRC-F725E90B2A-L002242](../../tests/test_web_agent.py#L2242) | 2242 | `"    rows = agent._search_deepseek_api(\"buyers looking to buy a flat\")"` | — |
| [SRC-F725E90B2A-L002243](../../tests/test_web_agent.py#L2243) | 2243 | `""` | — |
| [SRC-F725E90B2A-L002244](../../tests/test_web_agent.py#L2244) | 2244 | `"    assert seen[\"url\"] == \"https://api.deepseek.com/v1/tools/search\""` | — |
| [SRC-F725E90B2A-L002245](../../tests/test_web_agent.py#L2245) | 2245 | `"    assert seen[\"headers\"][\"Authorization\"] == \"Bearer test-secret-key-that-must-not-appear\""` | — |
| [SRC-F725E90B2A-L002246](../../tests/test_web_agent.py#L2246) | 2246 | `"    assert seen[\"json\"][\"count\"] == 6"` | — |
| [SRC-F725E90B2A-L002247](../../tests/test_web_agent.py#L2247) | 2247 | `"    assert rows[0][\"provider\"] == \"deepseek_search_api\""` | — |
| [SRC-F725E90B2A-L002248](../../tests/test_web_agent.py#L2248) | 2248 | `"    assert rows[0][\"snippet\"] == \"Looking to buy a flat in the requested area.\""` | — |
| [SRC-F725E90B2A-L002249](../../tests/test_web_agent.py#L2249) | 2249 | `"    assert rows[0][\"provider_rerank_score\"] == 2.2"` | — |
| [SRC-F725E90B2A-L002250](../../tests/test_web_agent.py#L2250) | 2250 | `"    assert \"test-secret-key-that-must-not-appear\" not in str(rows)"` | — |
| [SRC-F725E90B2A-L002251](../../tests/test_web_agent.py#L2251) | 2251 | `""` | — |
| [SRC-F725E90B2A-L002252](../../tests/test_web_agent.py#L2252) | 2252 | `""` | — |
| [SRC-F725E90B2A-L002253](../../tests/test_web_agent.py#L2253) | 2253 | `""` | — |
| [SRC-F725E90B2A-L002254](../../tests/test_web_agent.py#L2254) | 2254 | `"def test_diagnostics_distinguishes_connector_response_without_matches_from_offline(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002255](../../tests/test_web_agent.py#L2255) | 2255 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002256](../../tests/test_web_agent.py#L2256) | 2256 | `"    monkeypatch.setattr(agent, \"_request_completion\", lambda *args, **kwargs: \"OK\")"` | — |
| [SRC-F725E90B2A-L002257](../../tests/test_web_agent.py#L2257) | 2257 | `""` | — |
| [SRC-F725E90B2A-L002258](../../tests/test_web_agent.py#L2258) | 2258 | `"    def completed_empty_search(query):"` | — |
| [SRC-F725E90B2A-L002259](../../tests/test_web_agent.py#L2259) | 2259 | `"        agent._record_provider_diagnostic("` | — |
| [SRC-F725E90B2A-L002260](../../tests/test_web_agent.py#L2260) | 2260 | `"            \"bing_rss\", query, \"no_results\", result_count=0,"` | — |
| [SRC-F725E90B2A-L002261](../../tests/test_web_agent.py#L2261) | 2261 | `"            error=\"connector completed but returned no parseable results\","` | — |
| [SRC-F725E90B2A-L002262](../../tests/test_web_agent.py#L2262) | 2262 | `"        )"` | — |
| [SRC-F725E90B2A-L002263](../../tests/test_web_agent.py#L2263) | 2263 | `"        raise RuntimeError(\"no usable search matches\")"` | — |
| [SRC-F725E90B2A-L002264](../../tests/test_web_agent.py#L2264) | 2264 | `""` | — |
| [SRC-F725E90B2A-L002265](../../tests/test_web_agent.py#L2265) | 2265 | `"    monkeypatch.setattr(agent, \"_search_web\", completed_empty_search)"` | — |
| [SRC-F725E90B2A-L002266](../../tests/test_web_agent.py#L2266) | 2266 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L002267](../../tests/test_web_agent.py#L2267) | 2267 | `""` | — |
| [SRC-F725E90B2A-L002268](../../tests/test_web_agent.py#L2268) | 2268 | `"    assert report[\"checks\"][\"web_search\"][\"status\"] == \"degraded\""` | — |
| [SRC-F725E90B2A-L002269](../../tests/test_web_agent.py#L2269) | 2269 | `"    assert report[\"checks\"][\"web_search\"][\"result_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002270](../../tests/test_web_agent.py#L2270) | 2270 | `"    assert report[\"checks\"][\"web_search\"][\"completed_connector_responses\"] >= 1"` | — |
| [SRC-F725E90B2A-L002271](../../tests/test_web_agent.py#L2271) | 2271 | `"    assert \"completed a request\" in report[\"checks\"][\"web_search\"][\"note\"]"` | — |
| [SRC-F725E90B2A-L002272](../../tests/test_web_agent.py#L2272) | 2272 | `""` | — |
| [SRC-F725E90B2A-L002273](../../tests/test_web_agent.py#L2273) | 2273 | `""` | — |
| [SRC-F725E90B2A-L002274](../../tests/test_web_agent.py#L2274) | 2274 | `"def test_deepseek_search_request_budget_defaults_to_one_and_is_bounded(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002275](../../tests/test_web_agent.py#L2275) | 2275 | `"    monkeypatch.setenv(\"DEEPSEEK_SEARCH_API_KEY\", \"test-secret-key\")"` | — |
| [SRC-F725E90B2A-L002276](../../tests/test_web_agent.py#L2276) | 2276 | `"    monkeypatch.delenv(\"OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET\", raising=False)"` | — |
| [SRC-F725E90B2A-L002277](../../tests/test_web_agent.py#L2277) | 2277 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002278](../../tests/test_web_agent.py#L2278) | 2278 | `"    assert agent._reserve_deepseek_search_request() is True"` | — |
| [SRC-F725E90B2A-L002279](../../tests/test_web_agent.py#L2279) | 2279 | `"    assert agent._reserve_deepseek_search_request() is False"` | — |
| [SRC-F725E90B2A-L002280](../../tests/test_web_agent.py#L2280) | 2280 | `""` | — |
| [SRC-F725E90B2A-L002281](../../tests/test_web_agent.py#L2281) | 2281 | `"    monkeypatch.setenv(\"OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET\", \"2\")"` | — |
| [SRC-F725E90B2A-L002282](../../tests/test_web_agent.py#L2282) | 2282 | `"    other_agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002283](../../tests/test_web_agent.py#L2283) | 2283 | `"    assert other_agent._reserve_deepseek_search_request() is True"` | — |
| [SRC-F725E90B2A-L002284](../../tests/test_web_agent.py#L2284) | 2284 | `"    assert other_agent._reserve_deepseek_search_request() is True"` | — |
| [SRC-F725E90B2A-L002285](../../tests/test_web_agent.py#L2285) | 2285 | `"    assert other_agent._reserve_deepseek_search_request() is False"` | — |
| [SRC-F725E90B2A-L002286](../../tests/test_web_agent.py#L2286) | 2286 | `""` | — |
| [SRC-F725E90B2A-L002287](../../tests/test_web_agent.py#L2287) | 2287 | `""` | — |
| [SRC-F725E90B2A-L002288](../../tests/test_web_agent.py#L2288) | 2288 | `""` | — |
| [SRC-F725E90B2A-L002289](../../tests/test_web_agent.py#L2289) | 2289 | `"def test_diagnostics_distinguishes_completed_search_without_matches_from_connection_failure(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002290](../../tests/test_web_agent.py#L2290) | 2290 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002291](../../tests/test_web_agent.py#L2291) | 2291 | `"    # A stale record from a prior search must not make a new diagnostics call pass."` | — |
| [SRC-F725E90B2A-L002292](../../tests/test_web_agent.py#L2292) | 2292 | `"    agent._record_provider_diagnostic(\"old_provider\", \"old query\", \"ok\", 1)"` | — |
| [SRC-F725E90B2A-L002293](../../tests/test_web_agent.py#L2293) | 2293 | `""` | — |
| [SRC-F725E90B2A-L002294](../../tests/test_web_agent.py#L2294) | 2294 | `"    def no_results(query):"` | — |
| [SRC-F725E90B2A-L002295](../../tests/test_web_agent.py#L2295) | 2295 | `"        agent._record_provider_diagnostic(\"duckduckgo_html\", query, \"no_results\")"` | — |
| [SRC-F725E90B2A-L002296](../../tests/test_web_agent.py#L2296) | 2296 | `"        raise RuntimeError(\"no parseable results\")"` | — |
| [SRC-F725E90B2A-L002297](../../tests/test_web_agent.py#L2297) | 2297 | `""` | — |
| [SRC-F725E90B2A-L002298](../../tests/test_web_agent.py#L2298) | 2298 | `"    monkeypatch.setattr(agent, \"_search_web\", no_results)"` | — |
| [SRC-F725E90B2A-L002299](../../tests/test_web_agent.py#L2299) | 2299 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L002300](../../tests/test_web_agent.py#L2300) | 2300 | `""` | — |
| [SRC-F725E90B2A-L002301](../../tests/test_web_agent.py#L2301) | 2301 | `"    check = report[\"checks\"][\"web_search\"]"` | — |
| [SRC-F725E90B2A-L002302](../../tests/test_web_agent.py#L2302) | 2302 | `"    assert check[\"status\"] == \"degraded\""` | — |
| [SRC-F725E90B2A-L002303](../../tests/test_web_agent.py#L2303) | 2303 | `"    assert check[\"result_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002304](../../tests/test_web_agent.py#L2304) | 2304 | `"    assert check[\"completed_connector_responses\"] >= 1"` | — |
| [SRC-F725E90B2A-L002305](../../tests/test_web_agent.py#L2305) | 2305 | `"    assert \"completed a request\" in check[\"note\"]"` | — |
| [SRC-F725E90B2A-L002306](../../tests/test_web_agent.py#L2306) | 2306 | `"    assert \"old_provider\" not in str(check)"` | — |
| [SRC-F725E90B2A-L002307](../../tests/test_web_agent.py#L2307) | 2307 | `""` | — |
| [SRC-F725E90B2A-L002308](../../tests/test_web_agent.py#L2308) | 2308 | `""` | — |
| [SRC-F725E90B2A-L002309](../../tests/test_web_agent.py#L2309) | 2309 | `"def test_buyer_intent_phrase_inside_negated_text_is_not_a_lead_signal():"` | — |
| [SRC-F725E90B2A-L002310](../../tests/test_web_agent.py#L2310) | 2310 | `"    source = {"` | — |
| [SRC-F725E90B2A-L002311](../../tests/test_web_agent.py#L2311) | 2311 | `"        \"title\": \"Buyer discussion\","` | — |
| [SRC-F725E90B2A-L002312](../../tests/test_web_agent.py#L2312) | 2312 | `"        \"snippet\": \"I am not looking to buy an apartment this year.\","` | — |
| [SRC-F725E90B2A-L002313](../../tests/test_web_agent.py#L2313) | 2313 | `"        \"page_text\": \"I am not looking to buy an apartment this year.\","` | — |
| [SRC-F725E90B2A-L002314](../../tests/test_web_agent.py#L2314) | 2314 | `"    }"` | — |
| [SRC-F725E90B2A-L002315](../../tests/test_web_agent.py#L2315) | 2315 | `"    assert WebAgent._lead_intent_evidence(source) is None"` | — |
| [SRC-F725E90B2A-L002316](../../tests/test_web_agent.py#L2316) | 2316 | `""` | — |
| [SRC-F725E90B2A-L002317](../../tests/test_web_agent.py#L2317) | 2317 | `""` | — |
| [SRC-F725E90B2A-L002318](../../tests/test_web_agent.py#L2318) | 2318 | `""` | — |
| [SRC-F725E90B2A-L002319](../../tests/test_web_agent.py#L2319) | 2319 | `"def test_lead_generation_preserves_unknown_state_when_research_throws(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002320](../../tests/test_web_agent.py#L2320) | 2320 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002321](../../tests/test_web_agent.py#L2321) | 2321 | `"    question = \"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\""` | — |
| [SRC-F725E90B2A-L002322](../../tests/test_web_agent.py#L2322) | 2322 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002323](../../tests/test_web_agent.py#L2323) | 2323 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002324](../../tests/test_web_agent.py#L2324) | 2324 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002325](../../tests/test_web_agent.py#L2325) | 2325 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002326](../../tests/test_web_agent.py#L2326) | 2326 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002327](../../tests/test_web_agent.py#L2327) | 2327 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002328](../../tests/test_web_agent.py#L2328) | 2328 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002329](../../tests/test_web_agent.py#L2329) | 2329 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002330](../../tests/test_web_agent.py#L2330) | 2330 | `"    }"` | — |
| [SRC-F725E90B2A-L002331](../../tests/test_web_agent.py#L2331) | 2331 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda q, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002332](../../tests/test_web_agent.py#L2332) | 2332 | `""` | — |
| [SRC-F725E90B2A-L002333](../../tests/test_web_agent.py#L2333) | 2333 | `"    def fail_research(research_plan):"` | — |
| [SRC-F725E90B2A-L002334](../../tests/test_web_agent.py#L2334) | 2334 | `"        raise RuntimeError(\"mocked interrupted research\")"` | — |
| [SRC-F725E90B2A-L002335](../../tests/test_web_agent.py#L2335) | 2335 | `""` | — |
| [SRC-F725E90B2A-L002336](../../tests/test_web_agent.py#L2336) | 2336 | `"    monkeypatch.setattr(agent, \"_collect_research\", fail_research)"` | — |
| [SRC-F725E90B2A-L002337](../../tests/test_web_agent.py#L2337) | 2337 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002338](../../tests/test_web_agent.py#L2338) | 2338 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002339](../../tests/test_web_agent.py#L2339) | 2339 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L002340](../../tests/test_web_agent.py#L2340) | 2340 | `"        lambda *args, **kwargs: (_ for _ in ()).throw("` | — |
| [SRC-F725E90B2A-L002341](../../tests/test_web_agent.py#L2341) | 2341 | `"            AssertionError(\"must not generate a lead from an incomplete search\")"` | — |
| [SRC-F725E90B2A-L002342](../../tests/test_web_agent.py#L2342) | 2342 | `"        ),"` | — |
| [SRC-F725E90B2A-L002343](../../tests/test_web_agent.py#L2343) | 2343 | `"    )"` | — |
| [SRC-F725E90B2A-L002344](../../tests/test_web_agent.py#L2344) | 2344 | `""` | — |
| [SRC-F725E90B2A-L002345](../../tests/test_web_agent.py#L2345) | 2345 | `"    result = agent.answer(question)"` | — |
| [SRC-F725E90B2A-L002346](../../tests/test_web_agent.py#L2346) | 2346 | `"    lead = result[\"search_report\"][\"lead_generation\"]"` | — |
| [SRC-F725E90B2A-L002347](../../tests/test_web_agent.py#L2347) | 2347 | `""` | — |
| [SRC-F725E90B2A-L002348](../../tests/test_web_agent.py#L2348) | 2348 | `"    assert lead[\"status\"] == \"research_incomplete\""` | — |
| [SRC-F725E90B2A-L002349](../../tests/test_web_agent.py#L2349) | 2349 | `"    assert lead[\"candidate_signal_count\"] is None"` | — |
| [SRC-F725E90B2A-L002350](../../tests/test_web_agent.py#L2350) | 2350 | `"    assert lead[\"related_results_reviewed\"] is None"` | — |
| [SRC-F725E90B2A-L002351](../../tests/test_web_agent.py#L2351) | 2351 | `"    assert result[\"search_report\"][\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002352](../../tests/test_web_agent.py#L2352) | 2352 | `"    assert result[\"search_report\"][\"evidence_signals\"] is None"` | — |
| [SRC-F725E90B2A-L002353](../../tests/test_web_agent.py#L2353) | 2353 | `"    assert \"لم أستطع تحديد\" in result[\"answer\"] or \"تعطل مسار البحث\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L002354](../../tests/test_web_agent.py#L2354) | 2354 | `""` | — |
| [SRC-F725E90B2A-L002355](../../tests/test_web_agent.py#L2355) | 2355 | `""` | — |
| [SRC-F725E90B2A-L002356](../../tests/test_web_agent.py#L2356) | 2356 | `""` | — |
| [SRC-F725E90B2A-L002357](../../tests/test_web_agent.py#L2357) | 2357 | `"def test_local_answer_exposes_request_budget_without_claiming_live_search():"` | — |
| [SRC-F725E90B2A-L002358](../../tests/test_web_agent.py#L2358) | 2358 | `"    result = WebAgent().answer(\"مرحبا\")"` | — |
| [SRC-F725E90B2A-L002359](../../tests/test_web_agent.py#L2359) | 2359 | `""` | — |
| [SRC-F725E90B2A-L002360](../../tests/test_web_agent.py#L2360) | 2360 | `"    budget = result[\"request_budget\"]"` | — |
| [SRC-F725E90B2A-L002361](../../tests/test_web_agent.py#L2361) | 2361 | `"    assert budget[\"policy\"] == \"cooperative_per_request_budget\""` | — |
| [SRC-F725E90B2A-L002362](../../tests/test_web_agent.py#L2362) | 2362 | `"    assert budget[\"counts\"][\"search_queries\"] == 0"` | — |
| [SRC-F725E90B2A-L002363](../../tests/test_web_agent.py#L2363) | 2363 | `"    assert budget[\"counts\"][\"model_calls\"] == 0"` | — |
| [SRC-F725E90B2A-L002364](../../tests/test_web_agent.py#L2364) | 2364 | `"    assert budget[\"hard_cancellation_guaranteed\"] is False"` | — |
| [SRC-F725E90B2A-L002365](../../tests/test_web_agent.py#L2365) | 2365 | `""` | — |
| [SRC-F725E90B2A-L002366](../../tests/test_web_agent.py#L2366) | 2366 | `""` | — |
| [SRC-F725E90B2A-L002367](../../tests/test_web_agent.py#L2367) | 2367 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L002368](../../tests/test_web_agent.py#L2368) | 2368 | `"    \"draft_answer\","` | — |
| [SRC-F725E90B2A-L002369](../../tests/test_web_agent.py#L2369) | 2369 | `"    ["` | — |
| [SRC-F725E90B2A-L002370](../../tests/test_web_agent.py#L2370) | 2370 | `"        \"وفق المقارنة، الخيار الأول أفضل من الثاني.\","` | — |
| [SRC-F725E90B2A-L002371](../../tests/test_web_agent.py#L2371) | 2371 | `"        \"وفق المقارنة، الخيار الأول أفضل من الثاني [المصدر 99].\","` | — |
| [SRC-F725E90B2A-L002372](../../tests/test_web_agent.py#L2372) | 2372 | `"    ],"` | — |
| [SRC-F725E90B2A-L002373](../../tests/test_web_agent.py#L2373) | 2373 | `")"` | — |
| [SRC-F725E90B2A-L002374](../../tests/test_web_agent.py#L2374) | 2374 | `"def test_reviewed_answer_without_valid_citations_cannot_be_rated_good("` | — |
| [SRC-F725E90B2A-L002375](../../tests/test_web_agent.py#L2375) | 2375 | `"    monkeypatch, draft_answer"` | — |
| [SRC-F725E90B2A-L002376](../../tests/test_web_agent.py#L2376) | 2376 | `"):"` | — |
| [SRC-F725E90B2A-L002377](../../tests/test_web_agent.py#L2377) | 2377 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002378](../../tests/test_web_agent.py#L2378) | 2378 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002379](../../tests/test_web_agent.py#L2379) | 2379 | `"    domains = [\"alpha.org\", \"beta.net\", \"gamma.io\", \"delta.dev\"]"` | — |
| [SRC-F725E90B2A-L002380](../../tests/test_web_agent.py#L2380) | 2380 | `"    providers = [\"duckduckgo_html\", \"bing_rss\", \"duckduckgo_html\", \"bing_rss\"]"` | — |
| [SRC-F725E90B2A-L002381](../../tests/test_web_agent.py#L2381) | 2381 | `"    sources = []"` | — |
| [SRC-F725E90B2A-L002382](../../tests/test_web_agent.py#L2382) | 2382 | `"    for index, (domain, provider) in enumerate(zip(domains, providers, strict=True)):"` | — |
| [SRC-F725E90B2A-L002383](../../tests/test_web_agent.py#L2383) | 2383 | `"        source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002384](../../tests/test_web_agent.py#L2384) | 2384 | `"        source.update("` | — |
| [SRC-F725E90B2A-L002385](../../tests/test_web_agent.py#L2385) | 2385 | `"            {"` | — |
| [SRC-F725E90B2A-L002386](../../tests/test_web_agent.py#L2386) | 2386 | `"                \"title\": f\"مصدر اختبار {index + 1}\","` | — |
| [SRC-F725E90B2A-L002387](../../tests/test_web_agent.py#L2387) | 2387 | `"                \"url\": f\"https://{domain}/research\","` | — |
| [SRC-F725E90B2A-L002388](../../tests/test_web_agent.py#L2388) | 2388 | `"                \"domain\": domain,"` | — |
| [SRC-F725E90B2A-L002389](../../tests/test_web_agent.py#L2389) | 2389 | `"                \"providers\": [provider],"` | — |
| [SRC-F725E90B2A-L002390](../../tests/test_web_agent.py#L2390) | 2390 | `"                \"queries\": [\"قارن بالتفصيل بين طرق إدارة الميزانية\"],"` | — |
| [SRC-F725E90B2A-L002391](../../tests/test_web_agent.py#L2391) | 2391 | `"                \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L002392](../../tests/test_web_agent.py#L2392) | 2392 | `"                \"page_text\": f\"نص مصدر الاختبار رقم {index + 1}.\","` | — |
| [SRC-F725E90B2A-L002393](../../tests/test_web_agent.py#L2393) | 2393 | `"            }"` | — |
| [SRC-F725E90B2A-L002394](../../tests/test_web_agent.py#L2394) | 2394 | `"        )"` | — |
| [SRC-F725E90B2A-L002395](../../tests/test_web_agent.py#L2395) | 2395 | `"        sources.append(source)"` | — |
| [SRC-F725E90B2A-L002396](../../tests/test_web_agent.py#L2396) | 2396 | `""` | — |
| [SRC-F725E90B2A-L002397](../../tests/test_web_agent.py#L2397) | 2397 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002398](../../tests/test_web_agent.py#L2398) | 2398 | `"        \"queries\": [\"قارن بالتفصيل بين طرق إدارة الميزانية\"],"` | — |
| [SRC-F725E90B2A-L002399](../../tests/test_web_agent.py#L2399) | 2399 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002400](../../tests/test_web_agent.py#L2400) | 2400 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002401](../../tests/test_web_agent.py#L2401) | 2401 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002402](../../tests/test_web_agent.py#L2402) | 2402 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002403](../../tests/test_web_agent.py#L2403) | 2403 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002404](../../tests/test_web_agent.py#L2404) | 2404 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002405](../../tests/test_web_agent.py#L2405) | 2405 | `"    }"` | — |
| [SRC-F725E90B2A-L002406](../../tests/test_web_agent.py#L2406) | 2406 | `"    report = {"` | — |
| [SRC-F725E90B2A-L002407](../../tests/test_web_agent.py#L2407) | 2407 | `"        \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L002408](../../tests/test_web_agent.py#L2408) | 2408 | `"        \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L002409](../../tests/test_web_agent.py#L2409) | 2409 | `"        \"query_results\": [{\"query\": plan[\"queries\"][0], \"results\": 4}],"` | — |
| [SRC-F725E90B2A-L002410](../../tests/test_web_agent.py#L2410) | 2410 | `"        \"unique_sources\": 4,"` | — |
| [SRC-F725E90B2A-L002411](../../tests/test_web_agent.py#L2411) | 2411 | `"        \"pages_fetched\": 4,"` | — |
| [SRC-F725E90B2A-L002412](../../tests/test_web_agent.py#L2412) | 2412 | `"        \"providers_used\": providers,"` | — |
| [SRC-F725E90B2A-L002413](../../tests/test_web_agent.py#L2413) | 2413 | `"        \"provider_counts\": {\"duckduckgo_html\": 2, \"bing_rss\": 2},"` | — |
| [SRC-F725E90B2A-L002414](../../tests/test_web_agent.py#L2414) | 2414 | `"        \"platform_counts\": {\"web\": 4},"` | — |
| [SRC-F725E90B2A-L002415](../../tests/test_web_agent.py#L2415) | 2415 | `"        \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002416](../../tests/test_web_agent.py#L2416) | 2416 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002417](../../tests/test_web_agent.py#L2417) | 2417 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002418](../../tests/test_web_agent.py#L2418) | 2418 | `"        \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L002419](../../tests/test_web_agent.py#L2419) | 2419 | `"    }"` | — |
| [SRC-F725E90B2A-L002420](../../tests/test_web_agent.py#L2420) | 2420 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002421](../../tests/test_web_agent.py#L2421) | 2421 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002422](../../tests/test_web_agent.py#L2422) | 2422 | `"        agent, \"_collect_research\", lambda research_plan: (sources, [], dict(report))"` | — |
| [SRC-F725E90B2A-L002423](../../tests/test_web_agent.py#L2423) | 2423 | `"    )"` | — |
| [SRC-F725E90B2A-L002424](../../tests/test_web_agent.py#L2424) | 2424 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L002425](../../tests/test_web_agent.py#L2425) | 2425 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: draft_answer)"` | — |
| [SRC-F725E90B2A-L002426](../../tests/test_web_agent.py#L2426) | 2426 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002427](../../tests/test_web_agent.py#L2427) | 2427 | `"        agent, \"_review_answer\", lambda question, answer, review_sources: answer"` | — |
| [SRC-F725E90B2A-L002428](../../tests/test_web_agent.py#L2428) | 2428 | `"    )"` | — |
| [SRC-F725E90B2A-L002429](../../tests/test_web_agent.py#L2429) | 2429 | `""` | — |
| [SRC-F725E90B2A-L002430](../../tests/test_web_agent.py#L2430) | 2430 | `"    result = agent.answer(plan[\"queries\"][0], mode=\"deep\")"` | — |
| [SRC-F725E90B2A-L002431](../../tests/test_web_agent.py#L2431) | 2431 | `""` | — |
| [SRC-F725E90B2A-L002432](../../tests/test_web_agent.py#L2432) | 2432 | `"    assert result[\"used_language_model\"] is True"` | — |
| [SRC-F725E90B2A-L002433](../../tests/test_web_agent.py#L2433) | 2433 | `"    assert result[\"search_report\"][\"second_pass_review\"] == \"model_claim_audit_completed\""` | — |
| [SRC-F725E90B2A-L002434](../../tests/test_web_agent.py#L2434) | 2434 | `"    assert result[\"citation_validation\"][\"valid_citation_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002435](../../tests/test_web_agent.py#L2435) | 2435 | `"    assert result[\"research_quality\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L002436](../../tests/test_web_agent.py#L2436) | 2436 | `"    assert result[\"search_report\"][\"research_quality\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L002437](../../tests/test_web_agent.py#L2437) | 2437 | `"    assert result[\"answer_evidence_status\"] == \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-F725E90B2A-L002438](../../tests/test_web_agent.py#L2438) | 2438 | `"    assert result[\"citation_validation\"][\"claim_support\"] == ("` | — |
| [SRC-F725E90B2A-L002439](../../tests/test_web_agent.py#L2439) | 2439 | `"        \"not_established_no_valid_source_citations\""` | — |
| [SRC-F725E90B2A-L002440](../../tests/test_web_agent.py#L2440) | 2440 | `"    )"` | — |
| [SRC-F725E90B2A-L002441](../../tests/test_web_agent.py#L2441) | 2441 | `"    assert any(\"لا تحتوي على إحالات صالحة\" in warning for warning in result[\"warnings\"])"` | — |
| [SRC-F725E90B2A-L002442](../../tests/test_web_agent.py#L2442) | 2442 | `""` | — |
| [SRC-F725E90B2A-L002443](../../tests/test_web_agent.py#L2443) | 2443 | `"# Network-boundary regression tests. These use mocked transports and never make"` | — |
| [SRC-F725E90B2A-L002444](../../tests/test_web_agent.py#L2444) | 2444 | `"# an outbound connection; they protect against SSRF and redirect/DNS-rebinding regressions."` | — |
| [SRC-F725E90B2A-L002445](../../tests/test_web_agent.py#L2445) | 2445 | `"def test_public_ip_literals_rejects_mixed_public_and_private_dns_answers(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002446](../../tests/test_web_agent.py#L2446) | 2446 | `"    import socket"` | — |
| [SRC-F725E90B2A-L002447](../../tests/test_web_agent.py#L2447) | 2447 | `""` | — |
| [SRC-F725E90B2A-L002448](../../tests/test_web_agent.py#L2448) | 2448 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L002449](../../tests/test_web_agent.py#L2449) | 2449 | `""` | — |
| [SRC-F725E90B2A-L002450](../../tests/test_web_agent.py#L2450) | 2450 | `"    answers = ["` | — |
| [SRC-F725E90B2A-L002451](../../tests/test_web_agent.py#L2451) | 2451 | `"        (socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, \"\", (\"93.184.216.34\", 80)),"` | — |
| [SRC-F725E90B2A-L002452](../../tests/test_web_agent.py#L2452) | 2452 | `"        (socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, \"\", (\"10.10.0.8\", 80)),"` | — |
| [SRC-F725E90B2A-L002453](../../tests/test_web_agent.py#L2453) | 2453 | `"    ]"` | — |
| [SRC-F725E90B2A-L002454](../../tests/test_web_agent.py#L2454) | 2454 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002455](../../tests/test_web_agent.py#L2455) | 2455 | `"        web_agent.socket,"` | — |
| [SRC-F725E90B2A-L002456](../../tests/test_web_agent.py#L2456) | 2456 | `"        \"getaddrinfo\","` | — |
| [SRC-F725E90B2A-L002457](../../tests/test_web_agent.py#L2457) | 2457 | `"        lambda host, port, type: answers,"` | — |
| [SRC-F725E90B2A-L002458](../../tests/test_web_agent.py#L2458) | 2458 | `"    )"` | — |
| [SRC-F725E90B2A-L002459](../../tests/test_web_agent.py#L2459) | 2459 | `""` | — |
| [SRC-F725E90B2A-L002460](../../tests/test_web_agent.py#L2460) | 2460 | `"    # One private DNS answer must fail closed, even when another answer is public."` | — |
| [SRC-F725E90B2A-L002461](../../tests/test_web_agent.py#L2461) | 2461 | `"    assert web_agent._public_ip_literals(\"mixed.example\") is None"` | — |
| [SRC-F725E90B2A-L002462](../../tests/test_web_agent.py#L2462) | 2462 | `""` | — |
| [SRC-F725E90B2A-L002463](../../tests/test_web_agent.py#L2463) | 2463 | `""` | — |
| [SRC-F725E90B2A-L002464](../../tests/test_web_agent.py#L2464) | 2464 | `"def test_pinned_connect_url_uses_checked_ip_without_losing_logical_path():"` | — |
| [SRC-F725E90B2A-L002465](../../tests/test_web_agent.py#L2465) | 2465 | `"    from agents.web_agent import _pinned_connect_url"` | — |
| [SRC-F725E90B2A-L002466](../../tests/test_web_agent.py#L2466) | 2466 | `""` | — |
| [SRC-F725E90B2A-L002467](../../tests/test_web_agent.py#L2467) | 2467 | `"    assert _pinned_connect_url("` | — |
| [SRC-F725E90B2A-L002468](../../tests/test_web_agent.py#L2468) | 2468 | `"        \"https://example.test:443/path?q=1\","` | — |
| [SRC-F725E90B2A-L002469](../../tests/test_web_agent.py#L2469) | 2469 | `"        \"93.184.216.34\","` | — |
| [SRC-F725E90B2A-L002470](../../tests/test_web_agent.py#L2470) | 2470 | `"    ) == \"https://93.184.216.34:443/path?q=1\""` | — |
| [SRC-F725E90B2A-L002471](../../tests/test_web_agent.py#L2471) | 2471 | `""` | — |
| [SRC-F725E90B2A-L002472](../../tests/test_web_agent.py#L2472) | 2472 | `""` | — |
| [SRC-F725E90B2A-L002473](../../tests/test_web_agent.py#L2473) | 2473 | `"def test_fetch_page_rejects_private_redirect_before_connecting(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002474](../../tests/test_web_agent.py#L2474) | 2474 | `"    from contextlib import contextmanager"` | — |
| [SRC-F725E90B2A-L002475](../../tests/test_web_agent.py#L2475) | 2475 | `""` | — |
| [SRC-F725E90B2A-L002476](../../tests/test_web_agent.py#L2476) | 2476 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002477](../../tests/test_web_agent.py#L2477) | 2477 | `""` | — |
| [SRC-F725E90B2A-L002478](../../tests/test_web_agent.py#L2478) | 2478 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L002479](../../tests/test_web_agent.py#L2479) | 2479 | `""` | — |
| [SRC-F725E90B2A-L002480](../../tests/test_web_agent.py#L2480) | 2480 | `"    resolved_hosts = []"` | — |
| [SRC-F725E90B2A-L002481](../../tests/test_web_agent.py#L2481) | 2481 | `"    requests = []"` | — |
| [SRC-F725E90B2A-L002482](../../tests/test_web_agent.py#L2482) | 2482 | `""` | — |
| [SRC-F725E90B2A-L002483](../../tests/test_web_agent.py#L2483) | 2483 | `"    def resolve_public_ip(host):"` | — |
| [SRC-F725E90B2A-L002484](../../tests/test_web_agent.py#L2484) | 2484 | `"        resolved_hosts.append(host)"` | — |
| [SRC-F725E90B2A-L002485](../../tests/test_web_agent.py#L2485) | 2485 | `"        return [\"93.184.216.34\"] if host == \"first.example\" else None"` | — |
| [SRC-F725E90B2A-L002486](../../tests/test_web_agent.py#L2486) | 2486 | `""` | — |
| [SRC-F725E90B2A-L002487](../../tests/test_web_agent.py#L2487) | 2487 | `"    monkeypatch.setattr(web_agent, \"_public_ip_literals\", resolve_public_ip)"` | — |
| [SRC-F725E90B2A-L002488](../../tests/test_web_agent.py#L2488) | 2488 | `""` | — |
| [SRC-F725E90B2A-L002489](../../tests/test_web_agent.py#L2489) | 2489 | `"    class RedirectResponse:"` | — |
| [SRC-F725E90B2A-L002490](../../tests/test_web_agent.py#L2490) | 2490 | `"        status_code = 302"` | — |
| [SRC-F725E90B2A-L002491](../../tests/test_web_agent.py#L2491) | 2491 | `""` | — |
| [SRC-F725E90B2A-L002492](../../tests/test_web_agent.py#L2492) | 2492 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L002493](../../tests/test_web_agent.py#L2493) | 2493 | `"            self.headers = {\"location\": \"http://127.0.0.1/admin\"}"` | — |
| [SRC-F725E90B2A-L002494](../../tests/test_web_agent.py#L2494) | 2494 | `""` | — |
| [SRC-F725E90B2A-L002495](../../tests/test_web_agent.py#L2495) | 2495 | `"    @contextmanager"` | — |
| [SRC-F725E90B2A-L002496](../../tests/test_web_agent.py#L2496) | 2496 | `"    def fake_stream(self, method, url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002497](../../tests/test_web_agent.py#L2497) | 2497 | `"        requests.append((method, str(url), kwargs))"` | — |
| [SRC-F725E90B2A-L002498](../../tests/test_web_agent.py#L2498) | 2498 | `"        yield RedirectResponse()"` | — |
| [SRC-F725E90B2A-L002499](../../tests/test_web_agent.py#L2499) | 2499 | `""` | — |
| [SRC-F725E90B2A-L002500](../../tests/test_web_agent.py#L2500) | 2500 | `"    class FakeClient:"` | — |
| [SRC-F725E90B2A-L002501](../../tests/test_web_agent.py#L2501) | 2501 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-F725E90B2A-L002502](../../tests/test_web_agent.py#L2502) | 2502 | `"            self.options = kwargs"` | — |
| [SRC-F725E90B2A-L002503](../../tests/test_web_agent.py#L2503) | 2503 | `""` | — |
| [SRC-F725E90B2A-L002504](../../tests/test_web_agent.py#L2504) | 2504 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L002505](../../tests/test_web_agent.py#L2505) | 2505 | `"            return self"` | — |
| [SRC-F725E90B2A-L002506](../../tests/test_web_agent.py#L2506) | 2506 | `""` | — |
| [SRC-F725E90B2A-L002507](../../tests/test_web_agent.py#L2507) | 2507 | `"        def __exit__(self, *_args):"` | — |
| [SRC-F725E90B2A-L002508](../../tests/test_web_agent.py#L2508) | 2508 | `"            return False"` | — |
| [SRC-F725E90B2A-L002509](../../tests/test_web_agent.py#L2509) | 2509 | `""` | — |
| [SRC-F725E90B2A-L002510](../../tests/test_web_agent.py#L2510) | 2510 | `"        stream = fake_stream"` | — |
| [SRC-F725E90B2A-L002511](../../tests/test_web_agent.py#L2511) | 2511 | `""` | — |
| [SRC-F725E90B2A-L002512](../../tests/test_web_agent.py#L2512) | 2512 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-F725E90B2A-L002513](../../tests/test_web_agent.py#L2513) | 2513 | `""` | — |
| [SRC-F725E90B2A-L002514](../../tests/test_web_agent.py#L2514) | 2514 | `"    assert web_agent.WebAgent()._fetch_page(\"https://first.example/article\") == (\"\", \"\")"` | — |
| [SRC-F725E90B2A-L002515](../../tests/test_web_agent.py#L2515) | 2515 | `"    assert resolved_hosts == [\"first.example\"]"` | — |
| [SRC-F725E90B2A-L002516](../../tests/test_web_agent.py#L2516) | 2516 | `"    assert len(requests) == 1"` | — |
| [SRC-F725E90B2A-L002517](../../tests/test_web_agent.py#L2517) | 2517 | `"    assert requests[0][1] == \"https://93.184.216.34/article\""` | — |
| [SRC-F725E90B2A-L002518](../../tests/test_web_agent.py#L2518) | 2518 | `"    assert requests[0][2][\"headers\"][\"Host\"] == \"first.example\""` | — |
| [SRC-F725E90B2A-L002519](../../tests/test_web_agent.py#L2519) | 2519 | `"    assert requests[0][2][\"extensions\"][\"sni_hostname\"] == \"first.example\""` | — |
| [SRC-F725E90B2A-L002520](../../tests/test_web_agent.py#L2520) | 2520 | `""` | — |
| [SRC-F725E90B2A-L002521](../../tests/test_web_agent.py#L2521) | 2521 | `""` | — |
| [SRC-F725E90B2A-L002522](../../tests/test_web_agent.py#L2522) | 2522 | `"def test_fetch_page_revalidates_dns_for_each_redirect_destination(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002523](../../tests/test_web_agent.py#L2523) | 2523 | `"    from contextlib import contextmanager"` | — |
| [SRC-F725E90B2A-L002524](../../tests/test_web_agent.py#L2524) | 2524 | `""` | — |
| [SRC-F725E90B2A-L002525](../../tests/test_web_agent.py#L2525) | 2525 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002526](../../tests/test_web_agent.py#L2526) | 2526 | `""` | — |
| [SRC-F725E90B2A-L002527](../../tests/test_web_agent.py#L2527) | 2527 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L002528](../../tests/test_web_agent.py#L2528) | 2528 | `""` | — |
| [SRC-F725E90B2A-L002529](../../tests/test_web_agent.py#L2529) | 2529 | `"    resolved_hosts = []"` | — |
| [SRC-F725E90B2A-L002530](../../tests/test_web_agent.py#L2530) | 2530 | `"    requests = []"` | — |
| [SRC-F725E90B2A-L002531](../../tests/test_web_agent.py#L2531) | 2531 | `""` | — |
| [SRC-F725E90B2A-L002532](../../tests/test_web_agent.py#L2532) | 2532 | `"    def resolve_public_ip(host):"` | — |
| [SRC-F725E90B2A-L002533](../../tests/test_web_agent.py#L2533) | 2533 | `"        resolved_hosts.append(host)"` | — |
| [SRC-F725E90B2A-L002534](../../tests/test_web_agent.py#L2534) | 2534 | `"        if host == \"first.example\":"` | — |
| [SRC-F725E90B2A-L002535](../../tests/test_web_agent.py#L2535) | 2535 | `"            return [\"93.184.216.34\"]"` | — |
| [SRC-F725E90B2A-L002536](../../tests/test_web_agent.py#L2536) | 2536 | `"        # Model a redirect destination that resolves to no verified public IP."` | — |
| [SRC-F725E90B2A-L002537](../../tests/test_web_agent.py#L2537) | 2537 | `"        return None"` | — |
| [SRC-F725E90B2A-L002538](../../tests/test_web_agent.py#L2538) | 2538 | `""` | — |
| [SRC-F725E90B2A-L002539](../../tests/test_web_agent.py#L2539) | 2539 | `"    monkeypatch.setattr(web_agent, \"_public_ip_literals\", resolve_public_ip)"` | — |
| [SRC-F725E90B2A-L002540](../../tests/test_web_agent.py#L2540) | 2540 | `""` | — |
| [SRC-F725E90B2A-L002541](../../tests/test_web_agent.py#L2541) | 2541 | `"    class RedirectResponse:"` | — |
| [SRC-F725E90B2A-L002542](../../tests/test_web_agent.py#L2542) | 2542 | `"        status_code = 302"` | — |
| [SRC-F725E90B2A-L002543](../../tests/test_web_agent.py#L2543) | 2543 | `""` | — |
| [SRC-F725E90B2A-L002544](../../tests/test_web_agent.py#L2544) | 2544 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L002545](../../tests/test_web_agent.py#L2545) | 2545 | `"            self.headers = {\"location\": \"https://second.example/internal\"}"` | — |
| [SRC-F725E90B2A-L002546](../../tests/test_web_agent.py#L2546) | 2546 | `""` | — |
| [SRC-F725E90B2A-L002547](../../tests/test_web_agent.py#L2547) | 2547 | `"    @contextmanager"` | — |
| [SRC-F725E90B2A-L002548](../../tests/test_web_agent.py#L2548) | 2548 | `"    def fake_stream(self, method, url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002549](../../tests/test_web_agent.py#L2549) | 2549 | `"        requests.append((method, str(url), kwargs))"` | — |
| [SRC-F725E90B2A-L002550](../../tests/test_web_agent.py#L2550) | 2550 | `"        yield RedirectResponse()"` | — |
| [SRC-F725E90B2A-L002551](../../tests/test_web_agent.py#L2551) | 2551 | `""` | — |
| [SRC-F725E90B2A-L002552](../../tests/test_web_agent.py#L2552) | 2552 | `"    class FakeClient:"` | — |
| [SRC-F725E90B2A-L002553](../../tests/test_web_agent.py#L2553) | 2553 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-F725E90B2A-L002554](../../tests/test_web_agent.py#L2554) | 2554 | `"            self.options = kwargs"` | — |
| [SRC-F725E90B2A-L002555](../../tests/test_web_agent.py#L2555) | 2555 | `""` | — |
| [SRC-F725E90B2A-L002556](../../tests/test_web_agent.py#L2556) | 2556 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L002557](../../tests/test_web_agent.py#L2557) | 2557 | `"            return self"` | — |
| [SRC-F725E90B2A-L002558](../../tests/test_web_agent.py#L2558) | 2558 | `""` | — |
| [SRC-F725E90B2A-L002559](../../tests/test_web_agent.py#L2559) | 2559 | `"        def __exit__(self, *_args):"` | — |
| [SRC-F725E90B2A-L002560](../../tests/test_web_agent.py#L2560) | 2560 | `"            return False"` | — |
| [SRC-F725E90B2A-L002561](../../tests/test_web_agent.py#L2561) | 2561 | `""` | — |
| [SRC-F725E90B2A-L002562](../../tests/test_web_agent.py#L2562) | 2562 | `"        stream = fake_stream"` | — |
| [SRC-F725E90B2A-L002563](../../tests/test_web_agent.py#L2563) | 2563 | `""` | — |
| [SRC-F725E90B2A-L002564](../../tests/test_web_agent.py#L2564) | 2564 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-F725E90B2A-L002565](../../tests/test_web_agent.py#L2565) | 2565 | `""` | — |
| [SRC-F725E90B2A-L002566](../../tests/test_web_agent.py#L2566) | 2566 | `"    assert web_agent.WebAgent()._fetch_page(\"https://first.example/article\") == (\"\", \"\")"` | — |
| [SRC-F725E90B2A-L002567](../../tests/test_web_agent.py#L2567) | 2567 | `"    assert resolved_hosts == [\"first.example\", \"second.example\"]"` | — |
| [SRC-F725E90B2A-L002568](../../tests/test_web_agent.py#L2568) | 2568 | `"    # The second host is validated before any connection attempt to it."` | — |
| [SRC-F725E90B2A-L002569](../../tests/test_web_agent.py#L2569) | 2569 | `"    assert len(requests) == 1"` | — |
| [SRC-F725E90B2A-L002570](../../tests/test_web_agent.py#L2570) | 2570 | `""` | — |
| [SRC-F725E90B2A-L002571](../../tests/test_web_agent.py#L2571) | 2571 | `""` | — |
| [SRC-F725E90B2A-L002572](../../tests/test_web_agent.py#L2572) | 2572 | `""` | — |
| [SRC-F725E90B2A-L002573](../../tests/test_web_agent.py#L2573) | 2573 | `"def test_history_search_query_uses_shared_context_resolver():"` | — |
| [SRC-F725E90B2A-L002574](../../tests/test_web_agent.py#L2574) | 2574 | `"    history = ["` | — |
| [SRC-F725E90B2A-L002575](../../tests/test_web_agent.py#L2575) | 2575 | `"        {\"role\": \"user\", \"content\": \"سعر آيفون 16 في مصر\"},"` | — |
| [SRC-F725E90B2A-L002576](../../tests/test_web_agent.py#L2576) | 2576 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن السعر.\"},"` | — |
| [SRC-F725E90B2A-L002577](../../tests/test_web_agent.py#L2577) | 2577 | `"    ]"` | — |
| [SRC-F725E90B2A-L002578](../../tests/test_web_agent.py#L2578) | 2578 | `"    query = WebAgent._history_search_query(\"هل فيه ضمان؟\", history)"` | — |
| [SRC-F725E90B2A-L002579](../../tests/test_web_agent.py#L2579) | 2579 | `"    assert \"آيفون 16\" in query"` | — |
| [SRC-F725E90B2A-L002580](../../tests/test_web_agent.py#L2580) | 2580 | `"    assert \"ضمان\" in query"` | — |
| [SRC-F725E90B2A-L002581](../../tests/test_web_agent.py#L2581) | 2581 | `""` | — |
| [SRC-F725E90B2A-L002582](../../tests/test_web_agent.py#L2582) | 2582 | `""` | — |
| [SRC-F725E90B2A-L002583](../../tests/test_web_agent.py#L2583) | 2583 | `"def test_history_search_query_does_not_reuse_stale_topic_after_acknowledgment():"` | — |
| [SRC-F725E90B2A-L002584](../../tests/test_web_agent.py#L2584) | 2584 | `"    history = ["` | — |
| [SRC-F725E90B2A-L002585](../../tests/test_web_agent.py#L2585) | 2585 | `"        {\"role\": \"user\", \"content\": \"سعر آيفون 16 في مصر\"},"` | — |
| [SRC-F725E90B2A-L002586](../../tests/test_web_agent.py#L2586) | 2586 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن السعر.\"},"` | — |
| [SRC-F725E90B2A-L002587](../../tests/test_web_agent.py#L2587) | 2587 | `"        {\"role\": \"user\", \"content\": \"شكرا\"},"` | — |
| [SRC-F725E90B2A-L002588](../../tests/test_web_agent.py#L2588) | 2588 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-F725E90B2A-L002589](../../tests/test_web_agent.py#L2589) | 2589 | `"    ]"` | — |
| [SRC-F725E90B2A-L002590](../../tests/test_web_agent.py#L2590) | 2590 | `"    assert WebAgent._history_search_query(\"فين؟\", history) == \"فين؟\""` | — |
| [SRC-F725E90B2A-L002591](../../tests/test_web_agent.py#L2591) | 2591 | `""` | — |
| [SRC-F725E90B2A-L002592](../../tests/test_web_agent.py#L2592) | 2592 | `""` | — |
| [SRC-F725E90B2A-L002593](../../tests/test_web_agent.py#L2593) | 2593 | `"def test_frontend_exposes_structured_page_fetch_statuses():"` | — |
| [SRC-F725E90B2A-L002594](../../tests/test_web_agent.py#L2594) | 2594 | `"    html_path = Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\""` | — |
| [SRC-F725E90B2A-L002595](../../tests/test_web_agent.py#L2595) | 2595 | `"    html = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002596](../../tests/test_web_agent.py#L2596) | 2596 | `"    assert \"page_fetch_status\" in html"` | — |
| [SRC-F725E90B2A-L002597](../../tests/test_web_agent.py#L2597) | 2597 | `"    assert \"partial_extraction\" in html"` | — |
| [SRC-F725E90B2A-L002598](../../tests/test_web_agent.py#L2598) | 2598 | `"    assert \"لم يُستخرج نص؛ قد تكون الصفحة ديناميكية أو محجوبة\" in html"` | — |
| [SRC-F725E90B2A-L002599](../../tests/test_web_agent.py#L2599) | 2599 | `"    assert \"تشخيص الموصلات في هذا الطلب\" in html"` | — |
| [SRC-F725E90B2A-L002600](../../tests/test_web_agent.py#L2600) | 2600 | `""` | — |
| [SRC-F725E90B2A-L002601](../../tests/test_web_agent.py#L2601) | 2601 | `""` | — |
| [SRC-F725E90B2A-L002602](../../tests/test_web_agent.py#L2602) | 2602 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L002603](../../tests/test_web_agent.py#L2603) | 2603 | `"    \"method_name\","` | — |
| [SRC-F725E90B2A-L002604](../../tests/test_web_agent.py#L2604) | 2604 | `"    [\"_search_duckduckgo_html\", \"_search_bing_rss\", \"_search_news\"],"` | — |
| [SRC-F725E90B2A-L002605](../../tests/test_web_agent.py#L2605) | 2605 | `")"` | — |
| [SRC-F725E90B2A-L002606](../../tests/test_web_agent.py#L2606) | 2606 | `"def test_search_providers_do_not_follow_redirects_automatically("` | — |
| [SRC-F725E90B2A-L002607](../../tests/test_web_agent.py#L2607) | 2607 | `"    monkeypatch, method_name"` | — |
| [SRC-F725E90B2A-L002608](../../tests/test_web_agent.py#L2608) | 2608 | `"):"` | — |
| [SRC-F725E90B2A-L002609](../../tests/test_web_agent.py#L2609) | 2609 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002610](../../tests/test_web_agent.py#L2610) | 2610 | `""` | — |
| [SRC-F725E90B2A-L002611](../../tests/test_web_agent.py#L2611) | 2611 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002612](../../tests/test_web_agent.py#L2612) | 2612 | `"    observed = []"` | — |
| [SRC-F725E90B2A-L002613](../../tests/test_web_agent.py#L2613) | 2613 | `""` | — |
| [SRC-F725E90B2A-L002614](../../tests/test_web_agent.py#L2614) | 2614 | `"    class RedirectResponse:"` | — |
| [SRC-F725E90B2A-L002615](../../tests/test_web_agent.py#L2615) | 2615 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L002616](../../tests/test_web_agent.py#L2616) | 2616 | `"            self.status_code = 302"` | — |
| [SRC-F725E90B2A-L002617](../../tests/test_web_agent.py#L2617) | 2617 | `"            self.headers = {\"location\": \"http://127.0.0.1:8765/private\"}"` | — |
| [SRC-F725E90B2A-L002618](../../tests/test_web_agent.py#L2618) | 2618 | `"            self.text = \"redirect\""` | — |
| [SRC-F725E90B2A-L002619](../../tests/test_web_agent.py#L2619) | 2619 | `"            self.content = b\"redirect\""` | — |
| [SRC-F725E90B2A-L002620](../../tests/test_web_agent.py#L2620) | 2620 | `""` | — |
| [SRC-F725E90B2A-L002621](../../tests/test_web_agent.py#L2621) | 2621 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002622](../../tests/test_web_agent.py#L2622) | 2622 | `"        observed.append((url, kwargs.get(\"follow_redirects\")))"` | — |
| [SRC-F725E90B2A-L002623](../../tests/test_web_agent.py#L2623) | 2623 | `"        return RedirectResponse()"` | — |
| [SRC-F725E90B2A-L002624](../../tests/test_web_agent.py#L2624) | 2624 | `""` | — |
| [SRC-F725E90B2A-L002625](../../tests/test_web_agent.py#L2625) | 2625 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L002626](../../tests/test_web_agent.py#L2626) | 2626 | `"    method = getattr(agent, method_name)"` | — |
| [SRC-F725E90B2A-L002627](../../tests/test_web_agent.py#L2627) | 2627 | `"    with pytest.raises(RuntimeError, match=\"HTTP 302\"):"` | — |
| [SRC-F725E90B2A-L002628](../../tests/test_web_agent.py#L2628) | 2628 | `"        method(\"redirect regression test\")"` | — |
| [SRC-F725E90B2A-L002629](../../tests/test_web_agent.py#L2629) | 2629 | `""` | — |
| [SRC-F725E90B2A-L002630](../../tests/test_web_agent.py#L2630) | 2630 | `"    assert len(observed) == 1"` | — |
| [SRC-F725E90B2A-L002631](../../tests/test_web_agent.py#L2631) | 2631 | `"    assert observed[0][1] is False"` | — |
| [SRC-F725E90B2A-L002632](../../tests/test_web_agent.py#L2632) | 2632 | `""` | — |
| [SRC-F725E90B2A-L002633](../../tests/test_web_agent.py#L2633) | 2633 | `""` | — |
| [SRC-F725E90B2A-L002634](../../tests/test_web_agent.py#L2634) | 2634 | `""` | — |
| [SRC-F725E90B2A-L002635](../../tests/test_web_agent.py#L2635) | 2635 | `"@pytest.mark.parametrize(\"mode\", [\"deep\", \"latest\", \"social\"])"` | — |
| [SRC-F725E90B2A-L002636](../../tests/test_web_agent.py#L2636) | 2636 | `"def test_explicit_modes_survive_deterministic_planning(monkeypatch, mode):"` | — |
| [SRC-F725E90B2A-L002637](../../tests/test_web_agent.py#L2637) | 2637 | `"    \"\"\"A missing planner model must not erase a mode explicitly selected by the user.\"\"\""` | — |
| [SRC-F725E90B2A-L002638](../../tests/test_web_agent.py#L2638) | 2638 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002639](../../tests/test_web_agent.py#L2639) | 2639 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L002640](../../tests/test_web_agent.py#L2640) | 2640 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002641](../../tests/test_web_agent.py#L2641) | 2641 | `""` | — |
| [SRC-F725E90B2A-L002642](../../tests/test_web_agent.py#L2642) | 2642 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L002643](../../tests/test_web_agent.py#L2643) | 2643 | `"        seen[\"plan\"] = dict(research_plan)"` | — |
| [SRC-F725E90B2A-L002644](../../tests/test_web_agent.py#L2644) | 2644 | `"        sources = [sample_source(0), sample_source(1)]"` | — |
| [SRC-F725E90B2A-L002645](../../tests/test_web_agent.py#L2645) | 2645 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L002646](../../tests/test_web_agent.py#L2646) | 2646 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002647](../../tests/test_web_agent.py#L2647) | 2647 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002648](../../tests/test_web_agent.py#L2648) | 2648 | `"            \"query_results\": ["` | — |
| [SRC-F725E90B2A-L002649](../../tests/test_web_agent.py#L2649) | 2649 | `"                {\"query\": query, \"results\": 1}"` | — |
| [SRC-F725E90B2A-L002650](../../tests/test_web_agent.py#L2650) | 2650 | `"                for query in research_plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L002651](../../tests/test_web_agent.py#L2651) | 2651 | `"            ],"` | — |
| [SRC-F725E90B2A-L002652](../../tests/test_web_agent.py#L2652) | 2652 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-F725E90B2A-L002653](../../tests/test_web_agent.py#L2653) | 2653 | `"            \"pages_fetched\": len(sources),"` | — |
| [SRC-F725E90B2A-L002654](../../tests/test_web_agent.py#L2654) | 2654 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L002655](../../tests/test_web_agent.py#L2655) | 2655 | `"            \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-F725E90B2A-L002656](../../tests/test_web_agent.py#L2656) | 2656 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002657](../../tests/test_web_agent.py#L2657) | 2657 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L002658](../../tests/test_web_agent.py#L2658) | 2658 | `"            \"planning_method\": \"deterministic_fallback\","` | — |
| [SRC-F725E90B2A-L002659](../../tests/test_web_agent.py#L2659) | 2659 | `"        }"` | — |
| [SRC-F725E90B2A-L002660](../../tests/test_web_agent.py#L2660) | 2660 | `""` | — |
| [SRC-F725E90B2A-L002661](../../tests/test_web_agent.py#L2661) | 2661 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L002662](../../tests/test_web_agent.py#L2662) | 2662 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L002663](../../tests/test_web_agent.py#L2663) | 2663 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L002664](../../tests/test_web_agent.py#L2664) | 2664 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002665](../../tests/test_web_agent.py#L2665) | 2665 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002666](../../tests/test_web_agent.py#L2666) | 2666 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L002667](../../tests/test_web_agent.py#L2667) | 2667 | `"        lambda question, history, sources, search_warning, research_plan=None,"` | — |
| [SRC-F725E90B2A-L002668](../../tests/test_web_agent.py#L2668) | 2668 | `"               search_report=None: \"توجد نتائج أولية للمراجعة [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L002669](../../tests/test_web_agent.py#L2669) | 2669 | `"    )"` | — |
| [SRC-F725E90B2A-L002670](../../tests/test_web_agent.py#L2670) | 2670 | `""` | — |
| [SRC-F725E90B2A-L002671](../../tests/test_web_agent.py#L2671) | 2671 | `"    question = ("` | — |
| [SRC-F725E90B2A-L002672](../../tests/test_web_agent.py#L2672) | 2672 | `"        \"ابحث عن شقة في التجمع الخامس بسعر 5000000 جنيه\""` | — |
| [SRC-F725E90B2A-L002673](../../tests/test_web_agent.py#L2673) | 2673 | `"        if mode == \"deep\" else \"الطاقة المتجددة في مصر\""` | — |
| [SRC-F725E90B2A-L002674](../../tests/test_web_agent.py#L2674) | 2674 | `"    )"` | — |
| [SRC-F725E90B2A-L002675](../../tests/test_web_agent.py#L2675) | 2675 | `"    result = agent.answer(question, mode=mode)"` | — |
| [SRC-F725E90B2A-L002676](../../tests/test_web_agent.py#L2676) | 2676 | `"    plan = seen[\"plan\"]"` | — |
| [SRC-F725E90B2A-L002677](../../tests/test_web_agent.py#L2677) | 2677 | `""` | — |
| [SRC-F725E90B2A-L002678](../../tests/test_web_agent.py#L2678) | 2678 | `"    assert plan[\"mode\"] == mode"` | — |
| [SRC-F725E90B2A-L002679](../../tests/test_web_agent.py#L2679) | 2679 | `"    assert result[\"research_plan\"][\"mode\"] == mode"` | — |
| [SRC-F725E90B2A-L002680](../../tests/test_web_agent.py#L2680) | 2680 | `"    if mode == \"deep\":"` | — |
| [SRC-F725E90B2A-L002681](../../tests/test_web_agent.py#L2681) | 2681 | `"        assert plan[\"depth\"] == \"deep\""` | — |
| [SRC-F725E90B2A-L002682](../../tests/test_web_agent.py#L2682) | 2682 | `"        assert len(plan[\"queries\"]) >= 3"` | — |
| [SRC-F725E90B2A-L002683](../../tests/test_web_agent.py#L2683) | 2683 | `"        assert any(\"إعلانات عقارية\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002684](../../tests/test_web_agent.py#L2684) | 2684 | `"        assert any(\"متوسط أسعار السوق للمتر\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002685](../../tests/test_web_agent.py#L2685) | 2685 | `"    elif mode == \"latest\":"` | — |
| [SRC-F725E90B2A-L002686](../../tests/test_web_agent.py#L2686) | 2686 | `"        assert plan[\"freshness\"] == \"current\""` | — |
| [SRC-F725E90B2A-L002687](../../tests/test_web_agent.py#L2687) | 2687 | `"        assert any("` | — |
| [SRC-F725E90B2A-L002688](../../tests/test_web_agent.py#L2688) | 2688 | `"            \"latest\" in query.lower() or \"recent\" in query.lower()"` | — |
| [SRC-F725E90B2A-L002689](../../tests/test_web_agent.py#L2689) | 2689 | `"            for query in plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L002690](../../tests/test_web_agent.py#L2690) | 2690 | `"        )"` | — |
| [SRC-F725E90B2A-L002691](../../tests/test_web_agent.py#L2691) | 2691 | `"    else:"` | — |
| [SRC-F725E90B2A-L002692](../../tests/test_web_agent.py#L2692) | 2692 | `"        assert plan[\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L002693](../../tests/test_web_agent.py#L2693) | 2693 | `"        assert any(query.startswith(\"site:\") for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002694](../../tests/test_web_agent.py#L2694) | 2694 | `""` | — |
| [SRC-F725E90B2A-L002695](../../tests/test_web_agent.py#L2695) | 2695 | `""` | — |
| [SRC-F725E90B2A-L002696](../../tests/test_web_agent.py#L2696) | 2696 | `"def test_web_answer_integrity_is_attached_without_live_network(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002697](../../tests/test_web_agent.py#L2697) | 2697 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002698](../../tests/test_web_agent.py#L2698) | 2698 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002699](../../tests/test_web_agent.py#L2699) | 2699 | `"        agent, \"_question_coverage_targets\", lambda question: [\"السعر\", \"المساحة\"]"` | — |
| [SRC-F725E90B2A-L002700](../../tests/test_web_agent.py#L2700) | 2700 | `"    )"` | — |
| [SRC-F725E90B2A-L002701](../../tests/test_web_agent.py#L2701) | 2701 | `"    monkeypatch.setattr(agent, \"_answer_with_budget\", lambda question, history, mode: {"` | — |
| [SRC-F725E90B2A-L002702](../../tests/test_web_agent.py#L2702) | 2702 | `"        \"kind\": \"web_research\","` | — |
| [SRC-F725E90B2A-L002703](../../tests/test_web_agent.py#L2703) | 2703 | `"        \"answer\": \"السعر 500 جنيه [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L002704](../../tests/test_web_agent.py#L2704) | 2704 | `"        \"sources\": [{"` | — |
| [SRC-F725E90B2A-L002705](../../tests/test_web_agent.py#L2705) | 2705 | `"            \"title\": \"تفاصيل العرض\","` | — |
| [SRC-F725E90B2A-L002706](../../tests/test_web_agent.py#L2706) | 2706 | `"            \"url\": \"https://example.com/offer\","` | — |
| [SRC-F725E90B2A-L002707](../../tests/test_web_agent.py#L2707) | 2707 | `"            \"snippet\": \"السعر 300 جنيه\","` | — |
| [SRC-F725E90B2A-L002708](../../tests/test_web_agent.py#L2708) | 2708 | `"            \"page_fetched\": False,"` | — |
| [SRC-F725E90B2A-L002709](../../tests/test_web_agent.py#L2709) | 2709 | `"        }],"` | — |
| [SRC-F725E90B2A-L002710](../../tests/test_web_agent.py#L2710) | 2710 | `"        \"research_quality\": \"partial\","` | — |
| [SRC-F725E90B2A-L002711](../../tests/test_web_agent.py#L2711) | 2711 | `"        \"search_report\": {},"` | — |
| [SRC-F725E90B2A-L002712](../../tests/test_web_agent.py#L2712) | 2712 | `"        \"answer_coverage\": {},"` | — |
| [SRC-F725E90B2A-L002713](../../tests/test_web_agent.py#L2713) | 2713 | `"        \"used_language_model\": True,"` | — |
| [SRC-F725E90B2A-L002714](../../tests/test_web_agent.py#L2714) | 2714 | `"        \"used_web_search\": True,"` | — |
| [SRC-F725E90B2A-L002715](../../tests/test_web_agent.py#L2715) | 2715 | `"        \"warnings\": [],"` | — |
| [SRC-F725E90B2A-L002716](../../tests/test_web_agent.py#L2716) | 2716 | `"    })"` | — |
| [SRC-F725E90B2A-L002717](../../tests/test_web_agent.py#L2717) | 2717 | `""` | — |
| [SRC-F725E90B2A-L002718](../../tests/test_web_agent.py#L2718) | 2718 | `"    result = agent.answer(\"قارن السعر والمساحة\", mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L002719](../../tests/test_web_agent.py#L2719) | 2719 | `""` | — |
| [SRC-F725E90B2A-L002720](../../tests/test_web_agent.py#L2720) | 2720 | `"    assert result[\"answer_integrity\"][\"semantic_verification\"] is False"` | — |
| [SRC-F725E90B2A-L002721](../../tests/test_web_agent.py#L2721) | 2721 | `"    assert result[\"answer_integrity\"][\"independent_fact_check\"] is False"` | — |
| [SRC-F725E90B2A-L002722](../../tests/test_web_agent.py#L2722) | 2722 | `"    assert result[\"answer_integrity\"][\"potentially_unsupported_numeric_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002723](../../tests/test_web_agent.py#L2723) | 2723 | `"    assert result[\"answer_integrity\"][\"potentially_unsupported_numeric_by_citation_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002724](../../tests/test_web_agent.py#L2724) | 2724 | `"    assert result[\"answer_integrity\"][\"potentially_missing_target_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002725](../../tests/test_web_agent.py#L2725) | 2725 | `"    assert result[\"task_fulfillment_status\"] == \"possible_gap_detected\""` | — |
| [SRC-F725E90B2A-L002726](../../tests/test_web_agent.py#L2726) | 2726 | `"    assert result[\"answer_coverage\"][\"lexical_screen_method\"] == ("` | — |
| [SRC-F725E90B2A-L002727](../../tests/test_web_agent.py#L2727) | 2727 | `"        \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-F725E90B2A-L002728](../../tests/test_web_agent.py#L2728) | 2728 | `"    )"` | — |
| [SRC-F725E90B2A-L002729](../../tests/test_web_agent.py#L2729) | 2729 | `""` | — |
| [SRC-F725E90B2A-L002730](../../tests/test_web_agent.py#L2730) | 2730 | `""` | — |
| [SRC-F725E90B2A-L002731](../../tests/test_web_agent.py#L2731) | 2731 | `"def test_frontend_labels_answer_integrity_screen_as_non_semantic():"` | — |
| [SRC-F725E90B2A-L002732](../../tests/test_web_agent.py#L2732) | 2732 | `"    html = ("` | — |
| [SRC-F725E90B2A-L002733](../../tests/test_web_agent.py#L2733) | 2733 | `"        Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\""` | — |
| [SRC-F725E90B2A-L002734](../../tests/test_web_agent.py#L2734) | 2734 | `"    ).read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002735](../../tests/test_web_agent.py#L2735) | 2735 | `"    assert \"فحص لفظي أولي:\" in html"` | — |
| [SRC-F725E90B2A-L002736](../../tests/test_web_agent.py#L2736) | 2736 | `"    assert \"لا يثبت هذا الفحص صحة الوقائع أو دلالة الاستشهاد\" in html"` | — |
| [SRC-F725E90B2A-L002737](../../tests/test_web_agent.py#L2737) | 2737 | `"    assert \"potentially_unsupported_numeric_by_citation_count\" in html"` | — |
| [SRC-F725E90B2A-L002738](../../tests/test_web_agent.py#L2738) | 2738 | `"    assert \"potential_value_discrepancy_count\" in html"` | — |
| [SRC-F725E90B2A-L002739](../../tests/test_web_agent.py#L2739) | 2739 | `""` | — |
| [SRC-F725E90B2A-L002740](../../tests/test_web_agent.py#L2740) | 2740 | `""` | — |
| [SRC-F725E90B2A-L002741](../../tests/test_web_agent.py#L2741) | 2741 | `"def test_search_web_keeps_arabic_topic_matches_in_english_indexed_results(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002742](../../tests/test_web_agent.py#L2742) | 2742 | `"    cases = ["` | — |
| [SRC-F725E90B2A-L002743](../../tests/test_web_agent.py#L2743) | 2743 | `"        ("` | — |
| [SRC-F725E90B2A-L002744](../../tests/test_web_agent.py#L2744) | 2744 | `"            \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\","` | — |
| [SRC-F725E90B2A-L002745](../../tests/test_web_agent.py#L2745) | 2745 | `"            \"Egypt's capital is Cairo\","` | — |
| [SRC-F725E90B2A-L002746](../../tests/test_web_agent.py#L2746) | 2746 | `"            \"The capital city of Egypt is Cairo.\","` | — |
| [SRC-F725E90B2A-L002747](../../tests/test_web_agent.py#L2747) | 2747 | `"        ),"` | — |
| [SRC-F725E90B2A-L002748](../../tests/test_web_agent.py#L2748) | 2748 | `"        ("` | — |
| [SRC-F725E90B2A-L002749](../../tests/test_web_agent.py#L2749) | 2749 | `"            \"حلل أهم التحديات التي تواجه السيارات الكهربائية في مصر، وقارن بين التكلفة والبنية التحتية والشحن. استخدم مصادر متعددة، وميز بين الحقائق والاستنتاجات، واذكر روابط المصادر.\","` | — |
| [SRC-F725E90B2A-L002750](../../tests/test_web_agent.py#L2750) | 2750 | `"            \"Electric vehicles in Egypt: charging infrastructure and costs\","` | — |
| [SRC-F725E90B2A-L002751](../../tests/test_web_agent.py#L2751) | 2751 | `"            \"Electric cars face high costs and limited charging infrastructure in Egypt.\","` | — |
| [SRC-F725E90B2A-L002752](../../tests/test_web_agent.py#L2752) | 2752 | `"        ),"` | — |
| [SRC-F725E90B2A-L002753](../../tests/test_web_agent.py#L2753) | 2753 | `"        ("` | — |
| [SRC-F725E90B2A-L002754](../../tests/test_web_agent.py#L2754) | 2754 | `"            \"ما أحدث التطورات في وكلاء الذكاء الاصطناعي خلال الأيام السبعة الماضية؟ اذكر تواريخ الأخبار وروابط المصادر، ولا تعرض معلومات قديمة باعتبارها جديدة.\","` | — |
| [SRC-F725E90B2A-L002755](../../tests/test_web_agent.py#L2755) | 2755 | `"            \"Recent developments in AI agents\","` | — |
| [SRC-F725E90B2A-L002756](../../tests/test_web_agent.py#L2756) | 2756 | `"            \"New AI agent tools and launches this week.\","` | — |
| [SRC-F725E90B2A-L002757](../../tests/test_web_agent.py#L2757) | 2757 | `"        ),"` | — |
| [SRC-F725E90B2A-L002758](../../tests/test_web_agent.py#L2758) | 2758 | `"        ("` | — |
| [SRC-F725E90B2A-L002759](../../tests/test_web_agent.py#L2759) | 2759 | `"            \"اجمع آراء وتجارب المستخدمين العامة حول السيارات الكهربائية في مصر. اعرض الآراء الإيجابية والسلبية، واذكر روابط المنشورات أو المصادر المتاحة.\","` | — |
| [SRC-F725E90B2A-L002760](../../tests/test_web_agent.py#L2760) | 2760 | `"            \"Reddit users share electric car experiences in Egypt\","` | — |
| [SRC-F725E90B2A-L002761](../../tests/test_web_agent.py#L2761) | 2761 | `"            \"Owners discuss electric vehicles, charging and daily use.\","` | — |
| [SRC-F725E90B2A-L002762](../../tests/test_web_agent.py#L2762) | 2762 | `"        ),"` | — |
| [SRC-F725E90B2A-L002763](../../tests/test_web_agent.py#L2763) | 2763 | `"    ]"` | — |
| [SRC-F725E90B2A-L002764](../../tests/test_web_agent.py#L2764) | 2764 | `"    for index, (query, title, snippet) in enumerate(cases):"` | — |
| [SRC-F725E90B2A-L002765](../../tests/test_web_agent.py#L2765) | 2765 | `"        agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002766](../../tests/test_web_agent.py#L2766) | 2766 | `"        row = {"` | — |
| [SRC-F725E90B2A-L002767](../../tests/test_web_agent.py#L2767) | 2767 | `"            \"title\": title,"` | — |
| [SRC-F725E90B2A-L002768](../../tests/test_web_agent.py#L2768) | 2768 | `"            \"url\": f\"https://example.com/case-{index}\","` | — |
| [SRC-F725E90B2A-L002769](../../tests/test_web_agent.py#L2769) | 2769 | `"            \"snippet\": snippet,"` | — |
| [SRC-F725E90B2A-L002770](../../tests/test_web_agent.py#L2770) | 2770 | `"            \"provider\": \"fake_provider\","` | — |
| [SRC-F725E90B2A-L002771](../../tests/test_web_agent.py#L2771) | 2771 | `"            \"provider_rank\": 1,"` | — |
| [SRC-F725E90B2A-L002772](../../tests/test_web_agent.py#L2772) | 2772 | `"            \"search_query\": query,"` | — |
| [SRC-F725E90B2A-L002773](../../tests/test_web_agent.py#L2773) | 2773 | `"        }"` | — |
| [SRC-F725E90B2A-L002774](../../tests/test_web_agent.py#L2774) | 2774 | `"        monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _q, row=row: [dict(row)])"` | — |
| [SRC-F725E90B2A-L002775](../../tests/test_web_agent.py#L2775) | 2775 | `"        monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _q, row=row: [dict(row)])"` | — |
| [SRC-F725E90B2A-L002776](../../tests/test_web_agent.py#L2776) | 2776 | `"        # Current-news questions normally add Google News RSS; keep this unit test deterministic."` | — |
| [SRC-F725E90B2A-L002777](../../tests/test_web_agent.py#L2777) | 2777 | `"        monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L002778](../../tests/test_web_agent.py#L2778) | 2778 | `"        results = agent._search_web(query)"` | — |
| [SRC-F725E90B2A-L002779](../../tests/test_web_agent.py#L2779) | 2779 | `"        assert results, f\"Search candidates were all filtered for case {index}\""` | — |
| [SRC-F725E90B2A-L002780](../../tests/test_web_agent.py#L2780) | 2780 | `"        diagnostic = next("` | — |
| [SRC-F725E90B2A-L002781](../../tests/test_web_agent.py#L2781) | 2781 | `"            item for item in agent._provider_diagnostics if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L002782](../../tests/test_web_agent.py#L2782) | 2782 | `"        )"` | — |
| [SRC-F725E90B2A-L002783](../../tests/test_web_agent.py#L2783) | 2783 | `"        assert diagnostic[\"accepted_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002784](../../tests/test_web_agent.py#L2784) | 2784 | `"        assert diagnostic[\"result_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002785](../../tests/test_web_agent.py#L2785) | 2785 | `""` | — |
| [SRC-F725E90B2A-L002786](../../tests/test_web_agent.py#L2786) | 2786 | `""` | — |
| [SRC-F725E90B2A-L002787](../../tests/test_web_agent.py#L2787) | 2787 | `"def test_search_web_classifies_http_challenge_and_rate_limit_as_provider_degradation(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002788](../../tests/test_web_agent.py#L2788) | 2788 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002789](../../tests/test_web_agent.py#L2789) | 2789 | `""` | — |
| [SRC-F725E90B2A-L002790](../../tests/test_web_agent.py#L2790) | 2790 | `"    def http_202(_query):"` | — |
| [SRC-F725E90B2A-L002791](../../tests/test_web_agent.py#L2791) | 2791 | `"        raise RuntimeError(\"HTTP 202\")"` | — |
| [SRC-F725E90B2A-L002792](../../tests/test_web_agent.py#L2792) | 2792 | `""` | — |
| [SRC-F725E90B2A-L002793](../../tests/test_web_agent.py#L2793) | 2793 | `"    def http_429(_query):"` | — |
| [SRC-F725E90B2A-L002794](../../tests/test_web_agent.py#L2794) | 2794 | `"        raise RuntimeError(\"HTTP 429\")"` | — |
| [SRC-F725E90B2A-L002795](../../tests/test_web_agent.py#L2795) | 2795 | `""` | — |
| [SRC-F725E90B2A-L002796](../../tests/test_web_agent.py#L2796) | 2796 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", http_202)"` | — |
| [SRC-F725E90B2A-L002797](../../tests/test_web_agent.py#L2797) | 2797 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", http_429)"` | — |
| [SRC-F725E90B2A-L002798](../../tests/test_web_agent.py#L2798) | 2798 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L002799](../../tests/test_web_agent.py#L2799) | 2799 | `"        agent._search_web(\"renewable energy storage policy\")"` | — |
| [SRC-F725E90B2A-L002800](../../tests/test_web_agent.py#L2800) | 2800 | `""` | — |
| [SRC-F725E90B2A-L002801](../../tests/test_web_agent.py#L2801) | 2801 | `"    statuses = {"` | — |
| [SRC-F725E90B2A-L002802](../../tests/test_web_agent.py#L2802) | 2802 | `"        item[\"provider\"]: item[\"status\"]"` | — |
| [SRC-F725E90B2A-L002803](../../tests/test_web_agent.py#L2803) | 2803 | `"        for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L002804](../../tests/test_web_agent.py#L2804) | 2804 | `"        if item[\"provider\"] in {\"duckduckgo_html\", \"bing_rss\"}"` | — |
| [SRC-F725E90B2A-L002805](../../tests/test_web_agent.py#L2805) | 2805 | `"    }"` | — |
| [SRC-F725E90B2A-L002806](../../tests/test_web_agent.py#L2806) | 2806 | `"    assert statuses[\"duckduckgo_html\"] == \"http_error\""` | — |
| [SRC-F725E90B2A-L002807](../../tests/test_web_agent.py#L2807) | 2807 | `"    assert statuses[\"bing_rss\"] == \"rate_limited\""` | — |
| [SRC-F725E90B2A-L002808](../../tests/test_web_agent.py#L2808) | 2808 | `""` | — |
| [SRC-F725E90B2A-L002809](../../tests/test_web_agent.py#L2809) | 2809 | `""` | — |
| [SRC-F725E90B2A-L002810](../../tests/test_web_agent.py#L2810) | 2810 | `"def test_search_web_records_distinct_candidate_rejection_reasons(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002811](../../tests/test_web_agent.py#L2811) | 2811 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002812](../../tests/test_web_agent.py#L2812) | 2812 | `"    query = \"renewable energy storage\""` | — |
| [SRC-F725E90B2A-L002813](../../tests/test_web_agent.py#L2813) | 2813 | `"    candidates = ["` | — |
| [SRC-F725E90B2A-L002814](../../tests/test_web_agent.py#L2814) | 2814 | `"        \"malformed candidate\","` | — |
| [SRC-F725E90B2A-L002815](../../tests/test_web_agent.py#L2815) | 2815 | `"        {"` | — |
| [SRC-F725E90B2A-L002816](../../tests/test_web_agent.py#L2816) | 2816 | `"            \"title\": \"Unsafe scheme\","` | — |
| [SRC-F725E90B2A-L002817](../../tests/test_web_agent.py#L2817) | 2817 | `"            \"url\": \"javascript:alert(1)\","` | — |
| [SRC-F725E90B2A-L002818](../../tests/test_web_agent.py#L2818) | 2818 | `"            \"snippet\": \"Renewable energy storage report\","` | — |
| [SRC-F725E90B2A-L002819](../../tests/test_web_agent.py#L2819) | 2819 | `"        },"` | — |
| [SRC-F725E90B2A-L002820](../../tests/test_web_agent.py#L2820) | 2820 | `"        {"` | — |
| [SRC-F725E90B2A-L002821](../../tests/test_web_agent.py#L2821) | 2821 | `"            \"title\": \"Translated mirror\","` | — |
| [SRC-F725E90B2A-L002822](../../tests/test_web_agent.py#L2822) | 2822 | `"            \"url\": \"https://translate.google.com/translate?u=https%3A%2F%2Fexample.com\","` | — |
| [SRC-F725E90B2A-L002823](../../tests/test_web_agent.py#L2823) | 2823 | `"            \"snippet\": \"Renewable energy storage\","` | — |
| [SRC-F725E90B2A-L002824](../../tests/test_web_agent.py#L2824) | 2824 | `"        },"` | — |
| [SRC-F725E90B2A-L002825](../../tests/test_web_agent.py#L2825) | 2825 | `"        {"` | — |
| [SRC-F725E90B2A-L002826](../../tests/test_web_agent.py#L2826) | 2826 | `"            \"title\": \"Gardening tips\","` | — |
| [SRC-F725E90B2A-L002827](../../tests/test_web_agent.py#L2827) | 2827 | `"            \"url\": \"https://example.com/gardening\","` | — |
| [SRC-F725E90B2A-L002828](../../tests/test_web_agent.py#L2828) | 2828 | `"            \"snippet\": \"Gardening flowers and house plants\","` | — |
| [SRC-F725E90B2A-L002829](../../tests/test_web_agent.py#L2829) | 2829 | `"        },"` | — |
| [SRC-F725E90B2A-L002830](../../tests/test_web_agent.py#L2830) | 2830 | `"    ]"` | — |
| [SRC-F725E90B2A-L002831](../../tests/test_web_agent.py#L2831) | 2831 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _q: [dict(x) if isinstance(x, dict) else x for x in candidates])"` | — |
| [SRC-F725E90B2A-L002832](../../tests/test_web_agent.py#L2832) | 2832 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _q: [dict(x) if isinstance(x, dict) else x for x in candidates])"` | — |
| [SRC-F725E90B2A-L002833](../../tests/test_web_agent.py#L2833) | 2833 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L002834](../../tests/test_web_agent.py#L2834) | 2834 | `""` | — |
| [SRC-F725E90B2A-L002835](../../tests/test_web_agent.py#L2835) | 2835 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L002836](../../tests/test_web_agent.py#L2836) | 2836 | `"        agent._search_web(query)"` | — |
| [SRC-F725E90B2A-L002837](../../tests/test_web_agent.py#L2837) | 2837 | `""` | — |
| [SRC-F725E90B2A-L002838](../../tests/test_web_agent.py#L2838) | 2838 | `"    diagnostic = next("` | — |
| [SRC-F725E90B2A-L002839](../../tests/test_web_agent.py#L2839) | 2839 | `"        item for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L002840](../../tests/test_web_agent.py#L2840) | 2840 | `"        if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L002841](../../tests/test_web_agent.py#L2841) | 2841 | `"    )"` | — |
| [SRC-F725E90B2A-L002842](../../tests/test_web_agent.py#L2842) | 2842 | `"    assert diagnostic[\"status\"] == \"filtered_all\""` | — |
| [SRC-F725E90B2A-L002843](../../tests/test_web_agent.py#L2843) | 2843 | `"    assert diagnostic[\"result_count\"] == 4"` | — |
| [SRC-F725E90B2A-L002844](../../tests/test_web_agent.py#L2844) | 2844 | `"    assert diagnostic[\"accepted_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002845](../../tests/test_web_agent.py#L2845) | 2845 | `"    assert diagnostic[\"rejected_count\"] == 4"` | — |
| [SRC-F725E90B2A-L002846](../../tests/test_web_agent.py#L2846) | 2846 | `"    assert diagnostic[\"rejection_counts\"] == {"` | — |
| [SRC-F725E90B2A-L002847](../../tests/test_web_agent.py#L2847) | 2847 | `"        \"malformed_candidate\": 1,"` | — |
| [SRC-F725E90B2A-L002848](../../tests/test_web_agent.py#L2848) | 2848 | `"        \"invalid_url_or_unsafe_target\": 1,"` | — |
| [SRC-F725E90B2A-L002849](../../tests/test_web_agent.py#L2849) | 2849 | `"        \"blocked_domain\": 1,"` | — |
| [SRC-F725E90B2A-L002850](../../tests/test_web_agent.py#L2850) | 2850 | `"        \"relevance_below_threshold\": 1,"` | — |
| [SRC-F725E90B2A-L002851](../../tests/test_web_agent.py#L2851) | 2851 | `"    }"` | — |
| [SRC-F725E90B2A-L002852](../../tests/test_web_agent.py#L2852) | 2852 | `"    assert sum(diagnostic[\"rejection_counts\"].values()) == diagnostic[\"rejected_count\"]"` | — |
| [SRC-F725E90B2A-L002853](../../tests/test_web_agent.py#L2853) | 2853 | `""` | — |
| [SRC-F725E90B2A-L002854](../../tests/test_web_agent.py#L2854) | 2854 | `""` | — |
| [SRC-F725E90B2A-L002855](../../tests/test_web_agent.py#L2855) | 2855 | `"def test_search_web_classifies_http_302_as_degraded_without_following_provider_redirect(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002856](../../tests/test_web_agent.py#L2856) | 2856 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002857](../../tests/test_web_agent.py#L2857) | 2857 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L002858](../../tests/test_web_agent.py#L2858) | 2858 | `""` | — |
| [SRC-F725E90B2A-L002859](../../tests/test_web_agent.py#L2859) | 2859 | `"    def redirect_response(query):"` | — |
| [SRC-F725E90B2A-L002860](../../tests/test_web_agent.py#L2860) | 2860 | `"        calls.append((\"duckduckgo_html\", query))"` | — |
| [SRC-F725E90B2A-L002861](../../tests/test_web_agent.py#L2861) | 2861 | `"        raise RuntimeError(\"HTTP 302\")"` | — |
| [SRC-F725E90B2A-L002862](../../tests/test_web_agent.py#L2862) | 2862 | `""` | — |
| [SRC-F725E90B2A-L002863](../../tests/test_web_agent.py#L2863) | 2863 | `"    def no_results(query):"` | — |
| [SRC-F725E90B2A-L002864](../../tests/test_web_agent.py#L2864) | 2864 | `"        calls.append((\"bing_rss\", query))"` | — |
| [SRC-F725E90B2A-L002865](../../tests/test_web_agent.py#L2865) | 2865 | `"        return []"` | — |
| [SRC-F725E90B2A-L002866](../../tests/test_web_agent.py#L2866) | 2866 | `""` | — |
| [SRC-F725E90B2A-L002867](../../tests/test_web_agent.py#L2867) | 2867 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", redirect_response)"` | — |
| [SRC-F725E90B2A-L002868](../../tests/test_web_agent.py#L2868) | 2868 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", no_results)"` | — |
| [SRC-F725E90B2A-L002869](../../tests/test_web_agent.py#L2869) | 2869 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L002870](../../tests/test_web_agent.py#L2870) | 2870 | `""` | — |
| [SRC-F725E90B2A-L002871](../../tests/test_web_agent.py#L2871) | 2871 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L002872](../../tests/test_web_agent.py#L2872) | 2872 | `"        agent._search_web(\"renewable energy storage\")"` | — |
| [SRC-F725E90B2A-L002873](../../tests/test_web_agent.py#L2873) | 2873 | `""` | — |
| [SRC-F725E90B2A-L002874](../../tests/test_web_agent.py#L2874) | 2874 | `"    diagnostic = next("` | — |
| [SRC-F725E90B2A-L002875](../../tests/test_web_agent.py#L2875) | 2875 | `"        item for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L002876](../../tests/test_web_agent.py#L2876) | 2876 | `"        if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L002877](../../tests/test_web_agent.py#L2877) | 2877 | `"    )"` | — |
| [SRC-F725E90B2A-L002878](../../tests/test_web_agent.py#L2878) | 2878 | `"    assert diagnostic[\"status\"] == \"http_error\""` | — |
| [SRC-F725E90B2A-L002879](../../tests/test_web_agent.py#L2879) | 2879 | `"    assert diagnostic[\"error\"] == \"RuntimeError: HTTP 302\""` | — |
| [SRC-F725E90B2A-L002880](../../tests/test_web_agent.py#L2880) | 2880 | `"    assert sum(provider == \"duckduckgo_html\" for provider, _query in calls) == 1"` | — |
| [SRC-F725E90B2A-L002881](../../tests/test_web_agent.py#L2881) | 2881 | `""` | — |
| [SRC-F725E90B2A-L002882](../../tests/test_web_agent.py#L2882) | 2882 | `""` | — |
| [SRC-F725E90B2A-L002883](../../tests/test_web_agent.py#L2883) | 2883 | `"def test_relevance_filter_compacts_prompt_and_rejects_instruction_only_queries():"` | — |
| [SRC-F725E90B2A-L002884](../../tests/test_web_agent.py#L2884) | 2884 | `"    question = \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\""` | — |
| [SRC-F725E90B2A-L002885](../../tests/test_web_agent.py#L2885) | 2885 | `"    assert _relevance_ratio(question, \"عاصمة مصر القاهرة\") >= 0.20"` | — |
| [SRC-F725E90B2A-L002886](../../tests/test_web_agent.py#L2886) | 2886 | `"    assert _relevance_ratio("` | — |
| [SRC-F725E90B2A-L002887](../../tests/test_web_agent.py#L2887) | 2887 | `"        \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\","` | — |
| [SRC-F725E90B2A-L002888](../../tests/test_web_agent.py#L2888) | 2888 | `"        \"Football results and unrelated match reports\","` | — |
| [SRC-F725E90B2A-L002889](../../tests/test_web_agent.py#L2889) | 2889 | `"    ) == 0.0"` | — |
| [SRC-F725E90B2A-L002890](../../tests/test_web_agent.py#L2890) | 2890 | `""` | — |
| [SRC-F725E90B2A-L002891](../../tests/test_web_agent.py#L2891) | 2891 | `""` | — |
| [SRC-F725E90B2A-L002892](../../tests/test_web_agent.py#L2892) | 2892 | `"def test_search_web_compacts_request_before_provider_dispatch(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002893](../../tests/test_web_agent.py#L2893) | 2893 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002894](../../tests/test_web_agent.py#L2894) | 2894 | `"    seen = []"` | — |
| [SRC-F725E90B2A-L002895](../../tests/test_web_agent.py#L2895) | 2895 | `""` | — |
| [SRC-F725E90B2A-L002896](../../tests/test_web_agent.py#L2896) | 2896 | `"    def capture(query):"` | — |
| [SRC-F725E90B2A-L002897](../../tests/test_web_agent.py#L2897) | 2897 | `"        seen.append(query)"` | — |
| [SRC-F725E90B2A-L002898](../../tests/test_web_agent.py#L2898) | 2898 | `"        return []"` | — |
| [SRC-F725E90B2A-L002899](../../tests/test_web_agent.py#L2899) | 2899 | `""` | — |
| [SRC-F725E90B2A-L002900](../../tests/test_web_agent.py#L2900) | 2900 | `"    for env_name in ("` | — |
| [SRC-F725E90B2A-L002901](../../tests/test_web_agent.py#L2901) | 2901 | `"        \"DEEPSEEK_SEARCH_API_KEY\","` | — |
| [SRC-F725E90B2A-L002902](../../tests/test_web_agent.py#L2902) | 2902 | `"        \"BRAVE_SEARCH_API_KEY\","` | — |
| [SRC-F725E90B2A-L002903](../../tests/test_web_agent.py#L2903) | 2903 | `"        \"TAVILY_API_KEY\","` | — |
| [SRC-F725E90B2A-L002904](../../tests/test_web_agent.py#L2904) | 2904 | `"    ):"` | — |
| [SRC-F725E90B2A-L002905](../../tests/test_web_agent.py#L2905) | 2905 | `"        monkeypatch.delenv(env_name, raising=False)"` | — |
| [SRC-F725E90B2A-L002906](../../tests/test_web_agent.py#L2906) | 2906 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", capture)"` | — |
| [SRC-F725E90B2A-L002907](../../tests/test_web_agent.py#L2907) | 2907 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", capture)"` | — |
| [SRC-F725E90B2A-L002908](../../tests/test_web_agent.py#L2908) | 2908 | `""` | — |
| [SRC-F725E90B2A-L002909](../../tests/test_web_agent.py#L2909) | 2909 | `"    raw_question = ("` | — |
| [SRC-F725E90B2A-L002910](../../tests/test_web_agent.py#L2910) | 2910 | `"        \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\""` | — |
| [SRC-F725E90B2A-L002911](../../tests/test_web_agent.py#L2911) | 2911 | `"    )"` | — |
| [SRC-F725E90B2A-L002912](../../tests/test_web_agent.py#L2912) | 2912 | `"    agent._search_web(raw_question)"` | — |
| [SRC-F725E90B2A-L002913](../../tests/test_web_agent.py#L2913) | 2913 | `""` | — |
| [SRC-F725E90B2A-L002914](../../tests/test_web_agent.py#L2914) | 2914 | `"    expected = _normalize_search_query(compact_search_query(raw_question))"` | — |
| [SRC-F725E90B2A-L002915](../../tests/test_web_agent.py#L2915) | 2915 | `"    assert seen"` | — |
| [SRC-F725E90B2A-L002916](../../tests/test_web_agent.py#L2916) | 2916 | `"    assert set(seen) == {expected}"` | — |
| [SRC-F725E90B2A-L002917](../../tests/test_web_agent.py#L2917) | 2917 | `"    assert len(expected) <= 240"` | — |
| [SRC-F725E90B2A-L002918](../../tests/test_web_agent.py#L2918) | 2918 | `"    assert \"رابط مباشر\" not in \" \".join(seen)"` | — |
| [SRC-F725E90B2A-L002919](../../tests/test_web_agent.py#L2919) | 2919 | `""` | — |
| [SRC-F725E90B2A-L002920](../../tests/test_web_agent.py#L2920) | 2920 | `""` | — |
| [SRC-F725E90B2A-L002921](../../tests/test_web_agent.py#L2921) | 2921 | `"def test_search_web_does_not_dispatch_instruction_only_query(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002922](../../tests/test_web_agent.py#L2922) | 2922 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002923](../../tests/test_web_agent.py#L2923) | 2923 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002924](../../tests/test_web_agent.py#L2924) | 2924 | `"        agent, \"_search_duckduckgo_html\","` | — |
| [SRC-F725E90B2A-L002925](../../tests/test_web_agent.py#L2925) | 2925 | `"        lambda query: pytest.fail(f\"provider should not receive {query!r}\"),"` | — |
| [SRC-F725E90B2A-L002926](../../tests/test_web_agent.py#L2926) | 2926 | `"    )"` | — |
| [SRC-F725E90B2A-L002927](../../tests/test_web_agent.py#L2927) | 2927 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002928](../../tests/test_web_agent.py#L2928) | 2928 | `"        agent, \"_search_bing_rss\","` | — |
| [SRC-F725E90B2A-L002929](../../tests/test_web_agent.py#L2929) | 2929 | `"        lambda query: pytest.fail(f\"provider should not receive {query!r}\"),"` | — |
| [SRC-F725E90B2A-L002930](../../tests/test_web_agent.py#L2930) | 2930 | `"    )"` | — |
| [SRC-F725E90B2A-L002931](../../tests/test_web_agent.py#L2931) | 2931 | `"    results = agent._search_web(\"اذكر مصادر موثوقة، روابط مباشرة، باختصار\")"` | — |
| [SRC-F725E90B2A-L002932](../../tests/test_web_agent.py#L2932) | 2932 | `"    assert results == []"` | — |
| [SRC-F725E90B2A-L002933](../../tests/test_web_agent.py#L2933) | 2933 | `""` | — |
| [SRC-F725E90B2A-L002934](../../tests/test_web_agent.py#L2934) | 2934 | `""` | — |
| [SRC-F725E90B2A-L002935](../../tests/test_web_agent.py#L2935) | 2935 | `"def test_plan_search_does_not_call_planner_without_a_topic(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002936](../../tests/test_web_agent.py#L2936) | 2936 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002937](../../tests/test_web_agent.py#L2937) | 2937 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002938](../../tests/test_web_agent.py#L2938) | 2938 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002939](../../tests/test_web_agent.py#L2939) | 2939 | `"        agent, \"_request_completion\","` | — |
| [SRC-F725E90B2A-L002940](../../tests/test_web_agent.py#L2940) | 2940 | `"        lambda *args, **kwargs: pytest.fail(\"planner should not run without a topic\"),"` | — |
| [SRC-F725E90B2A-L002941](../../tests/test_web_agent.py#L2941) | 2941 | `"    )"` | — |
| [SRC-F725E90B2A-L002942](../../tests/test_web_agent.py#L2942) | 2942 | `"    plan = agent._plan_search("` | — |
| [SRC-F725E90B2A-L002943](../../tests/test_web_agent.py#L2943) | 2943 | `"        \"استخدم مصادر متعددة، واذكر روابط المصادر\","` | — |
| [SRC-F725E90B2A-L002944](../../tests/test_web_agent.py#L2944) | 2944 | `"        [],"` | — |
| [SRC-F725E90B2A-L002945](../../tests/test_web_agent.py#L2945) | 2945 | `"    )"` | — |
| [SRC-F725E90B2A-L002946](../../tests/test_web_agent.py#L2946) | 2946 | `"    assert plan[\"queries\"] == []"` | — |
| [SRC-F725E90B2A-L002947](../../tests/test_web_agent.py#L2947) | 2947 | `""` | — |
| [SRC-F725E90B2A-L002948](../../tests/test_web_agent.py#L2948) | 2948 | `""` | — |
| [SRC-F725E90B2A-L002949](../../tests/test_web_agent.py#L2949) | 2949 | `"def test_plan_search_compacts_followup_query_before_fallback(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002950](../../tests/test_web_agent.py#L2950) | 2950 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002951](../../tests/test_web_agent.py#L2951) | 2951 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L002952](../../tests/test_web_agent.py#L2952) | 2952 | `"    history = [{"` | — |
| [SRC-F725E90B2A-L002953](../../tests/test_web_agent.py#L2953) | 2953 | `"        \"role\": \"user\","` | — |
| [SRC-F725E90B2A-L002954](../../tests/test_web_agent.py#L2954) | 2954 | `"        \"content\": ("` | — |
