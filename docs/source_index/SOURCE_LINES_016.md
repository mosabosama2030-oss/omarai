# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **016**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L005224 إلى SRC-1AE03B9EC3-L006023
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L005224](../../agents/web_agent.py#L5224) | 5224 | `"        has_read_user_supplied_page = any("` | — |
| [SRC-1AE03B9EC3-L005225](../../agents/web_agent.py#L5225) | 5225 | `"            \"user_supplied_url\" in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L005226](../../agents/web_agent.py#L5226) | 5226 | `"            and bool(source.get(\"page_fetched\"))"` | — |
| [SRC-1AE03B9EC3-L005227](../../agents/web_agent.py#L5227) | 5227 | `"            and bool(str(source.get(\"page_text\") or \"\").strip())"` | — |
| [SRC-1AE03B9EC3-L005228](../../agents/web_agent.py#L5228) | 5228 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005229](../../agents/web_agent.py#L5229) | 5229 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005230](../../agents/web_agent.py#L5230) | 5230 | `"        single_source_page_summary = ("` | — |
| [SRC-1AE03B9EC3-L005231](../../agents/web_agent.py#L5231) | 5231 | `"            has_read_user_supplied_page"` | — |
| [SRC-1AE03B9EC3-L005232](../../agents/web_agent.py#L5232) | 5232 | `"            and len(sources) == 1"` | — |
| [SRC-1AE03B9EC3-L005233](../../agents/web_agent.py#L5233) | 5233 | `"            and len(independent_domains) == 1"` | — |
| [SRC-1AE03B9EC3-L005234](../../agents/web_agent.py#L5234) | 5234 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005235](../../agents/web_agent.py#L5235) | 5235 | `"        if single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005236](../../agents/web_agent.py#L5236) | 5236 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005237](../../agents/web_agent.py#L5237) | 5237 | `"                \"هذا ملخص للرابط الذي قدمته فقط؛ لم يتم تأكيد محتواه من مصدر مستقل آخر.\""` | — |
| [SRC-1AE03B9EC3-L005238](../../agents/web_agent.py#L5238) | 5238 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005239](../../agents/web_agent.py#L5239) | 5239 | `"            search_warning = \"؛ \".join(search_warnings)"` | — |
| [SRC-1AE03B9EC3-L005240](../../agents/web_agent.py#L5240) | 5240 | `"        # Link-finding and lead-discovery are actionable discovery tasks, not broad"` | — |
| [SRC-1AE03B9EC3-L005241](../../agents/web_agent.py#L5241) | 5241 | `"        # fact-checking. Keep useful candidates visible while explicitly labelling them"` | — |
| [SRC-1AE03B9EC3-L005242](../../agents/web_agent.py#L5242) | 5242 | `"        # as uncorroborated instead of refusing a lone result as if it were no result."` | — |
| [SRC-1AE03B9EC3-L005243](../../agents/web_agent.py#L5243) | 5243 | `"        navigation_request = self._is_navigation_request(working_question)"` | — |
| [SRC-1AE03B9EC3-L005244](../../agents/web_agent.py#L5244) | 5244 | `"        lead_request = intent_route == \"LEAD_GENERATION\" or self._is_lead_search(working_question)"` | — |
| [SRC-1AE03B9EC3-L005245](../../agents/web_agent.py#L5245) | 5245 | `"        listing_request = self._is_listing_discovery(working_question)"` | — |
| [SRC-1AE03B9EC3-L005246](../../agents/web_agent.py#L5246) | 5246 | `"        lead_evidence_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L005247](../../agents/web_agent.py#L5247) | 5247 | `"        related_lead_results_count = 0"` | — |
| [SRC-1AE03B9EC3-L005248](../../agents/web_agent.py#L5248) | 5248 | `"        if lead_request:"` | — |
| [SRC-1AE03B9EC3-L005249](../../agents/web_agent.py#L5249) | 5249 | `"            related_lead_results_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005250](../../agents/web_agent.py#L5250) | 5250 | `"            for source in sources:"` | — |
| [SRC-1AE03B9EC3-L005251](../../agents/web_agent.py#L5251) | 5251 | `"                signal = self._lead_intent_evidence(source)"` | — |
| [SRC-1AE03B9EC3-L005252](../../agents/web_agent.py#L5252) | 5252 | `"                if signal:"` | — |
| [SRC-1AE03B9EC3-L005253](../../agents/web_agent.py#L5253) | 5253 | `"                    source[\"lead_qualification\"] = \"public_buyer_intent_signal\""` | — |
| [SRC-1AE03B9EC3-L005254](../../agents/web_agent.py#L5254) | 5254 | `"                    source[\"lead_intent_evidence\"] = signal"` | — |
| [SRC-1AE03B9EC3-L005255](../../agents/web_agent.py#L5255) | 5255 | `"                    lead_evidence_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L005256](../../agents/web_agent.py#L5256) | 5256 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L005257](../../agents/web_agent.py#L5257) | 5257 | `"                    source[\"lead_qualification\"] = \"related_result_not_lead\""` | — |
| [SRC-1AE03B9EC3-L005258](../../agents/web_agent.py#L5258) | 5258 | `"            lead_research_incomplete = ("` | — |
| [SRC-1AE03B9EC3-L005259](../../agents/web_agent.py#L5259) | 5259 | `"                not sources"` | — |
| [SRC-1AE03B9EC3-L005260](../../agents/web_agent.py#L5260) | 5260 | `"                and report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L005261](../../agents/web_agent.py#L5261) | 5261 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005262](../../agents/web_agent.py#L5262) | 5262 | `"            report[\"lead_generation\"] = {"` | — |
| [SRC-1AE03B9EC3-L005263](../../agents/web_agent.py#L5263) | 5263 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L005264](../../agents/web_agent.py#L5264) | 5264 | `"                    \"research_incomplete\" if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L005265](../../agents/web_agent.py#L5265) | 5265 | `"                    else \"candidate_signals_found\" if lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L005266](../../agents/web_agent.py#L5266) | 5266 | `"                    else \"no_qualified_candidates_found\""` | — |
| [SRC-1AE03B9EC3-L005267](../../agents/web_agent.py#L5267) | 5267 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005268](../../agents/web_agent.py#L5268) | 5268 | `"                \"candidate_signal_count\": ("` | — |
| [SRC-1AE03B9EC3-L005269](../../agents/web_agent.py#L5269) | 5269 | `"                    None if lead_research_incomplete else len(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L005270](../../agents/web_agent.py#L5270) | 5270 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005271](../../agents/web_agent.py#L5271) | 5271 | `"                \"related_results_reviewed\": ("` | — |
| [SRC-1AE03B9EC3-L005272](../../agents/web_agent.py#L5272) | 5272 | `"                    None if lead_research_incomplete else related_lead_results_count"` | — |
| [SRC-1AE03B9EC3-L005273](../../agents/web_agent.py#L5273) | 5273 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005274](../../agents/web_agent.py#L5274) | 5274 | `"                \"qualification_rule\": \"explicit_public_buyer_intent_phrase\","` | — |
| [SRC-1AE03B9EC3-L005275](../../agents/web_agent.py#L5275) | 5275 | `"                \"identity_verified\": False,"` | — |
| [SRC-1AE03B9EC3-L005276](../../agents/web_agent.py#L5276) | 5276 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005277](../../agents/web_agent.py#L5277) | 5277 | `"            if not lead_evidence_sources:"` | — |
| [SRC-1AE03B9EC3-L005278](../../agents/web_agent.py#L5278) | 5278 | `"                if sources:"` | — |
| [SRC-1AE03B9EC3-L005279](../../agents/web_agent.py#L5279) | 5279 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L005280](../../agents/web_agent.py#L5280) | 5280 | `"                        \"لم أعثر على إشارة نصية واضحة تثبت أن أي نتيجة في هذه الجولة تتعلق بشخص \""` | — |
| [SRC-1AE03B9EC3-L005281](../../agents/web_agent.py#L5281) | 5281 | `"                        \"يريد الشراء. راجعت \""` | — |
| [SRC-1AE03B9EC3-L005282](../../agents/web_agent.py#L5282) | 5282 | `"                        + str(len(sources))"` | — |
| [SRC-1AE03B9EC3-L005283](../../agents/web_agent.py#L5283) | 5283 | `"                        + \" نتيجة مرتبطة بالموضوع، لكنني لم أعتبر إعلانات البيع أو صفحات السوق \""` | — |
| [SRC-1AE03B9EC3-L005284](../../agents/web_agent.py#L5284) | 5284 | `"                        \"عملاء محتملين. الروابط أدناه نتائج مرتبطة بالموضوع فقط وليست عملاء.\""` | — |
| [SRC-1AE03B9EC3-L005285](../../agents/web_agent.py#L5285) | 5285 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005286](../../agents/web_agent.py#L5286) | 5286 | `"                elif report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L005287](../../agents/web_agent.py#L5287) | 5287 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L005288](../../agents/web_agent.py#L5288) | 5288 | `"                        \"تعطل مسار البحث أو لم يمكن تأكيد اكتماله؛ لذلك لا أستطيع تحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L005289](../../agents/web_agent.py#L5289) | 5289 | `"                        \"كانت هناك نتائج تصلح كعملاء محتملين في هذه الجولة.\""` | — |
| [SRC-1AE03B9EC3-L005290](../../agents/web_agent.py#L5290) | 5290 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005291](../../agents/web_agent.py#L5291) | 5291 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L005292](../../agents/web_agent.py#L5292) | 5292 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L005293](../../agents/web_agent.py#L5293) | 5293 | `"                        \"لم تظهر نتائج قابلة للاستخدام تثبت نية شراء في هذه الجولة. هذا لا يثبت \""` | — |
| [SRC-1AE03B9EC3-L005294](../../agents/web_agent.py#L5294) | 5294 | `"                        \"عدم وجود عملاء؛ بل يعني أن البحث الحالي لم يعثر على دليل كافٍ.\""` | — |
| [SRC-1AE03B9EC3-L005295](../../agents/web_agent.py#L5295) | 5295 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005296](../../agents/web_agent.py#L5296) | 5296 | `"                report[\"research_quality\"] = \"failed\""` | — |
| [SRC-1AE03B9EC3-L005297](../../agents/web_agent.py#L5297) | 5297 | `"                # Distinguish zero qualified signals from unknown counts after an exception."` | — |
| [SRC-1AE03B9EC3-L005298](../../agents/web_agent.py#L5298) | 5298 | `"                report[\"usable_sources_after_filtering\"] = ("` | — |
| [SRC-1AE03B9EC3-L005299](../../agents/web_agent.py#L5299) | 5299 | `"                    None if lead_research_incomplete else len(sources)"` | — |
| [SRC-1AE03B9EC3-L005300](../../agents/web_agent.py#L5300) | 5300 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005301](../../agents/web_agent.py#L5301) | 5301 | `"                report[\"evidence_signals\"] = ("` | — |
| [SRC-1AE03B9EC3-L005302](../../agents/web_agent.py#L5302) | 5302 | `"                    None if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L005303](../../agents/web_agent.py#L5303) | 5303 | `"                    else evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L005304](../../agents/web_agent.py#L5304) | 5304 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005305](../../agents/web_agent.py#L5305) | 5305 | `"                public_related_sources = [{"` | — |
| [SRC-1AE03B9EC3-L005306](../../agents/web_agent.py#L5306) | 5306 | `"                    \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L005307](../../agents/web_agent.py#L5307) | 5307 | `"                    \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L005308](../../agents/web_agent.py#L5308) | 5308 | `"                    \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005309](../../agents/web_agent.py#L5309) | 5309 | `"                    \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005310](../../agents/web_agent.py#L5310) | 5310 | `"                \"readable_page_text_available\": bool(source.get(\"page_fetched\")) and bool(str(source.get(\"page_text\") or \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L005311](../../agents/web_agent.py#L5311) | 5311 | `"                \"page_text_present_without_fetch_flag\": bool(str(source.get(\"page_text\") or \"\").strip()) and not bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005312](../../agents/web_agent.py#L5312) | 5312 | `"                    \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L005313](../../agents/web_agent.py#L5313) | 5313 | `"                    \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005314](../../agents/web_agent.py#L5314) | 5314 | `"                    \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L005315](../../agents/web_agent.py#L5315) | 5315 | `"                    \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005316](../../agents/web_agent.py#L5316) | 5316 | `"                    \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L005317](../../agents/web_agent.py#L5317) | 5317 | `"                    \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005318](../../agents/web_agent.py#L5318) | 5318 | `"                    \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005319](../../agents/web_agent.py#L5319) | 5319 | `"                    \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005320](../../agents/web_agent.py#L5320) | 5320 | `"                    \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L005321](../../agents/web_agent.py#L5321) | 5321 | `"                    \"lead_qualification\": \"related_result_not_lead\","` | — |
| [SRC-1AE03B9EC3-L005322](../../agents/web_agent.py#L5322) | 5322 | `"                } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L005323](../../agents/web_agent.py#L5323) | 5323 | `"                return {"` | — |
| [SRC-1AE03B9EC3-L005324](../../agents/web_agent.py#L5324) | 5324 | `"                    \"answer\": lead_answer,"` | — |
| [SRC-1AE03B9EC3-L005325](../../agents/web_agent.py#L5325) | 5325 | `"                    \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L005326](../../agents/web_agent.py#L5326) | 5326 | `"                    \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L005327](../../agents/web_agent.py#L5327) | 5327 | `"                    \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005328](../../agents/web_agent.py#L5328) | 5328 | `"                    \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L005329](../../agents/web_agent.py#L5329) | 5329 | `"                        \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L005330](../../agents/web_agent.py#L5330) | 5330 | `"                        \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L005331](../../agents/web_agent.py#L5331) | 5331 | `"                        \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L005332](../../agents/web_agent.py#L5332) | 5332 | `"                        \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L005333](../../agents/web_agent.py#L5333) | 5333 | `"                        \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L005334](../../agents/web_agent.py#L5334) | 5334 | `"                        \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L005335](../../agents/web_agent.py#L5335) | 5335 | `"                        \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L005336](../../agents/web_agent.py#L5336) | 5336 | `"                        \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L005337](../../agents/web_agent.py#L5337) | 5337 | `"                        \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005338](../../agents/web_agent.py#L5338) | 5338 | `"                        \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005339](../../agents/web_agent.py#L5339) | 5339 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L005340](../../agents/web_agent.py#L5340) | 5340 | `"                    \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L005341](../../agents/web_agent.py#L5341) | 5341 | `"                    \"sources\": public_related_sources,"` | — |
| [SRC-1AE03B9EC3-L005342](../../agents/web_agent.py#L5342) | 5342 | `"                    \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L005343](../../agents/web_agent.py#L5343) | 5343 | `"                    \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L005344](../../agents/web_agent.py#L5344) | 5344 | `"                    \"search_attempted\": report.get("` | — |
| [SRC-1AE03B9EC3-L005345](../../agents/web_agent.py#L5345) | 5345 | `"                        \"search_attempted\","` | — |
| [SRC-1AE03B9EC3-L005346](../../agents/web_agent.py#L5346) | 5346 | `"                        bool(report.get(\"queries_attempted\", 0)),"` | — |
| [SRC-1AE03B9EC3-L005347](../../agents/web_agent.py#L5347) | 5347 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L005348](../../agents/web_agent.py#L5348) | 5348 | `"                    \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L005349](../../agents/web_agent.py#L5349) | 5349 | `"                    \"warnings\": [lead_answer],"` | — |
| [SRC-1AE03B9EC3-L005350](../../agents/web_agent.py#L5350) | 5350 | `"                    \"kind\": \"lead_discovery_no_qualified_candidates\","` | — |
| [SRC-1AE03B9EC3-L005351](../../agents/web_agent.py#L5351) | 5351 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005352](../../agents/web_agent.py#L5352) | 5352 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005353](../../agents/web_agent.py#L5353) | 5353 | `"                    \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L005354](../../agents/web_agent.py#L5354) | 5354 | `"                }"` | — |
| [SRC-1AE03B9EC3-L005355](../../agents/web_agent.py#L5355) | 5355 | `"            # Only explicit public buyer-intent signals may be synthesized as lead candidates."` | — |
| [SRC-1AE03B9EC3-L005356](../../agents/web_agent.py#L5356) | 5356 | `"            sources = lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L005357](../../agents/web_agent.py#L5357) | 5357 | `"            report[\"evidence_signals\"] = evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L005358](../../agents/web_agent.py#L5358) | 5358 | `"            report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005359](../../agents/web_agent.py#L5359) | 5359 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005360](../../agents/web_agent.py#L5360) | 5360 | `"            report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005361](../../agents/web_agent.py#L5361) | 5361 | `"            independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L005362](../../agents/web_agent.py#L5362) | 5362 | `"                registrable_domain("` | — |
| [SRC-1AE03B9EC3-L005363](../../agents/web_agent.py#L5363) | 5363 | `"                    source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L005364](../../agents/web_agent.py#L5364) | 5364 | `"                    or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L005365](../../agents/web_agent.py#L5365) | 5365 | `"                    or \"\""` | — |
| [SRC-1AE03B9EC3-L005366](../../agents/web_agent.py#L5366) | 5366 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005367](../../agents/web_agent.py#L5367) | 5367 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L005368](../../agents/web_agent.py#L5368) | 5368 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005369](../../agents/web_agent.py#L5369) | 5369 | `"            independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005370](../../agents/web_agent.py#L5370) | 5370 | `"        single_source_navigation = navigation_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L005371](../../agents/web_agent.py#L5371) | 5371 | `"        single_source_social = bool(plan.get(\"social_focus\")) and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L005372](../../agents/web_agent.py#L5372) | 5372 | `"        single_source_lead = lead_request and bool(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L005373](../../agents/web_agent.py#L5373) | 5373 | `"        single_source_listing = listing_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L005374](../../agents/web_agent.py#L5374) | 5374 | `"        task_specific_partial_evidence = ("` | — |
| [SRC-1AE03B9EC3-L005375](../../agents/web_agent.py#L5375) | 5375 | `"            single_source_page_summary"` | — |
| [SRC-1AE03B9EC3-L005376](../../agents/web_agent.py#L5376) | 5376 | `"            or single_source_navigation"` | — |
| [SRC-1AE03B9EC3-L005377](../../agents/web_agent.py#L5377) | 5377 | `"            or single_source_social"` | — |
| [SRC-1AE03B9EC3-L005378](../../agents/web_agent.py#L5378) | 5378 | `"            or single_source_lead"` | — |
| [SRC-1AE03B9EC3-L005379](../../agents/web_agent.py#L5379) | 5379 | `"            or single_source_listing"` | — |
| [SRC-1AE03B9EC3-L005380](../../agents/web_agent.py#L5380) | 5380 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005381](../../agents/web_agent.py#L5381) | 5381 | `"        needs_corroboration = len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L005382](../../agents/web_agent.py#L5382) | 5382 | `"        evidence_repair: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L005383](../../agents/web_agent.py#L5383) | 5383 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L005384](../../agents/web_agent.py#L5384) | 5384 | `"            \"max_extra_queries\": 1,"` | — |
| [SRC-1AE03B9EC3-L005385](../../agents/web_agent.py#L5385) | 5385 | `"            \"reason\": \"initial_evidence_gate_satisfied\" if not needs_corroboration else \"not_attempted\","` | — |
| [SRC-1AE03B9EC3-L005386](../../agents/web_agent.py#L5386) | 5386 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005387](../../agents/web_agent.py#L5387) | 5387 | `"        if needs_corroboration and not plan.get(\"queries\"):"` | — |
| [SRC-1AE03B9EC3-L005388](../../agents/web_agent.py#L5388) | 5388 | `"            evidence_repair[\"reason\"] = \"no_topic_query_available\""` | — |
| [SRC-1AE03B9EC3-L005389](../../agents/web_agent.py#L5389) | 5389 | `"        elif needs_corroboration:"` | — |
| [SRC-1AE03B9EC3-L005390](../../agents/web_agent.py#L5390) | 5390 | `"            if task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L005391](../../agents/web_agent.py#L5391) | 5391 | `"                evidence_repair[\"reason\"] = \"task_specific_partial_evidence\""` | — |
| [SRC-1AE03B9EC3-L005392](../../agents/web_agent.py#L5392) | 5392 | `"            elif plan.get(\"social_focus\"):"` | — |
| [SRC-1AE03B9EC3-L005393](../../agents/web_agent.py#L5393) | 5393 | `"                evidence_repair[\"reason\"] = \"social_search_not_retried\""` | — |
| [SRC-1AE03B9EC3-L005394](../../agents/web_agent.py#L5394) | 5394 | `"            elif plan.get(\"depth\") == \"deep\" or report.get(\"expansion_queries\"):"` | — |
| [SRC-1AE03B9EC3-L005395](../../agents/web_agent.py#L5395) | 5395 | `"                evidence_repair[\"reason\"] = \"deep_research_already_expanded\""` | — |
| [SRC-1AE03B9EC3-L005396](../../agents/web_agent.py#L5396) | 5396 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005397](../../agents/web_agent.py#L5397) | 5397 | `"                original_queries = ["` | — |
| [SRC-1AE03B9EC3-L005398](../../agents/web_agent.py#L5398) | 5398 | `"                    str(item).strip()"` | — |
| [SRC-1AE03B9EC3-L005399](../../agents/web_agent.py#L5399) | 5399 | `"                    for item in plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005400](../../agents/web_agent.py#L5400) | 5400 | `"                    if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L005401](../../agents/web_agent.py#L5401) | 5401 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L005402](../../agents/web_agent.py#L5402) | 5402 | `"                base_query = ("` | — |
| [SRC-1AE03B9EC3-L005403](../../agents/web_agent.py#L5403) | 5403 | `"                    original_queries[0]"` | — |
| [SRC-1AE03B9EC3-L005404](../../agents/web_agent.py#L5404) | 5404 | `"                    if original_queries"` | — |
| [SRC-1AE03B9EC3-L005405](../../agents/web_agent.py#L5405) | 5405 | `"                    else compact_search_query(working_question)"` | — |
| [SRC-1AE03B9EC3-L005406](../../agents/web_agent.py#L5406) | 5406 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005407](../../agents/web_agent.py#L5407) | 5407 | `"                suffix = ("` | — |
| [SRC-1AE03B9EC3-L005408](../../agents/web_agent.py#L5408) | 5408 | `"                    \"latest official primary source\""` | — |
| [SRC-1AE03B9EC3-L005409](../../agents/web_agent.py#L5409) | 5409 | `"                    if plan.get(\"freshness\") == \"current\""` | — |
| [SRC-1AE03B9EC3-L005410](../../agents/web_agent.py#L5410) | 5410 | `"                    else \"official primary source data\""` | — |
| [SRC-1AE03B9EC3-L005411](../../agents/web_agent.py#L5411) | 5411 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005412](../../agents/web_agent.py#L5412) | 5412 | `"                repair_query = compact_search_query(f\"{base_query} {suffix}\")"` | — |
| [SRC-1AE03B9EC3-L005413](../../agents/web_agent.py#L5413) | 5413 | `"                if not repair_query or not _relevance_query_tokens(repair_query):"` | — |
| [SRC-1AE03B9EC3-L005414](../../agents/web_agent.py#L5414) | 5414 | `"                    evidence_repair[\"reason\"] = \"no_topic_query_available\""` | — |
| [SRC-1AE03B9EC3-L005415](../../agents/web_agent.py#L5415) | 5415 | `"                    repair_query = \"\""` | — |
| [SRC-1AE03B9EC3-L005416](../../agents/web_agent.py#L5416) | 5416 | `"                known_queries = {"` | — |
| [SRC-1AE03B9EC3-L005417](../../agents/web_agent.py#L5417) | 5417 | `"                    _normalize_search_query(item).casefold()"` | — |
| [SRC-1AE03B9EC3-L005418](../../agents/web_agent.py#L5418) | 5418 | `"                    for item in original_queries"` | — |
| [SRC-1AE03B9EC3-L005419](../../agents/web_agent.py#L5419) | 5419 | `"                }"` | — |
| [SRC-1AE03B9EC3-L005420](../../agents/web_agent.py#L5420) | 5420 | `"                if repair_query and _normalize_search_query(repair_query).casefold() in known_queries:"` | — |
| [SRC-1AE03B9EC3-L005421](../../agents/web_agent.py#L5421) | 5421 | `"                    repair_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L005422](../../agents/web_agent.py#L5422) | 5422 | `"                        f\"{base_query} independent corroborating evidence\""` | — |
| [SRC-1AE03B9EC3-L005423](../../agents/web_agent.py#L5423) | 5423 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005424](../../agents/web_agent.py#L5424) | 5424 | `"                if repair_query and _relevance_query_tokens(repair_query) and ("` | — |
| [SRC-1AE03B9EC3-L005425](../../agents/web_agent.py#L5425) | 5425 | `"                    _normalize_search_query(repair_query).casefold() not in known_queries"` | — |
| [SRC-1AE03B9EC3-L005426](../../agents/web_agent.py#L5426) | 5426 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L005427](../../agents/web_agent.py#L5427) | 5427 | `"                    initial_source_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005428](../../agents/web_agent.py#L5428) | 5428 | `"                    initial_domain_count = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L005429](../../agents/web_agent.py#L5429) | 5429 | `"                    evidence_repair[\"attempted\"] = True"` | — |
| [SRC-1AE03B9EC3-L005430](../../agents/web_agent.py#L5430) | 5430 | `"                    evidence_repair[\"reason\"] = \"thin_or_unrelated_initial_evidence\""` | — |
| [SRC-1AE03B9EC3-L005431](../../agents/web_agent.py#L5431) | 5431 | `"                    evidence_repair[\"query\"] = repair_query"` | — |
| [SRC-1AE03B9EC3-L005432](../../agents/web_agent.py#L5432) | 5432 | `"                    repair_plan = dict(plan)"` | — |
| [SRC-1AE03B9EC3-L005433](../../agents/web_agent.py#L5433) | 5433 | `"                    repair_plan.update({"` | — |
| [SRC-1AE03B9EC3-L005434](../../agents/web_agent.py#L5434) | 5434 | `"                        \"queries\": [repair_query],"` | — |
| [SRC-1AE03B9EC3-L005435](../../agents/web_agent.py#L5435) | 5435 | `"                        \"depth\": \"standard\","` | — |
| [SRC-1AE03B9EC3-L005436](../../agents/web_agent.py#L5436) | 5436 | `"                        \"social_focus\": False,"` | — |
| [SRC-1AE03B9EC3-L005437](../../agents/web_agent.py#L5437) | 5437 | `"                        \"platforms\": [],"` | — |
| [SRC-1AE03B9EC3-L005438](../../agents/web_agent.py#L5438) | 5438 | `"                        \"direct_urls\": [],"` | — |
| [SRC-1AE03B9EC3-L005439](../../agents/web_agent.py#L5439) | 5439 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L005440](../../agents/web_agent.py#L5440) | 5440 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L005441](../../agents/web_agent.py#L5441) | 5441 | `"                        repair_sources, repair_warnings, repair_report = self._collect_research("` | — |
| [SRC-1AE03B9EC3-L005442](../../agents/web_agent.py#L5442) | 5442 | `"                            repair_plan"` | — |
| [SRC-1AE03B9EC3-L005443](../../agents/web_agent.py#L5443) | 5443 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005444](../../agents/web_agent.py#L5444) | 5444 | `"                    except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L005445](../../agents/web_agent.py#L5445) | 5445 | `"                        repair_sources = []"` | — |
| [SRC-1AE03B9EC3-L005446](../../agents/web_agent.py#L5446) | 5446 | `"                        repair_warnings = []"` | — |
| [SRC-1AE03B9EC3-L005447](../../agents/web_agent.py#L5447) | 5447 | `"                        repair_report = {"` | — |
| [SRC-1AE03B9EC3-L005448](../../agents/web_agent.py#L5448) | 5448 | `"                            \"queries_planned\": 1,"` | — |
| [SRC-1AE03B9EC3-L005449](../../agents/web_agent.py#L5449) | 5449 | `"                            \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L005450](../../agents/web_agent.py#L5450) | 5450 | `"                            \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L005451](../../agents/web_agent.py#L5451) | 5451 | `"                            \"search_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L005452](../../agents/web_agent.py#L5452) | 5452 | `"                            \"search_outcome\": \"unknown_after_research_error\","` | — |
| [SRC-1AE03B9EC3-L005453](../../agents/web_agent.py#L5453) | 5453 | `"                            \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L005454](../../agents/web_agent.py#L5454) | 5454 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L005455](../../agents/web_agent.py#L5455) | 5455 | `"                        search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005456](../../agents/web_agent.py#L5456) | 5456 | `"                            \"تعذر تنفيذ محاولة البحث الإضافية المحدودة (\""` | — |
| [SRC-1AE03B9EC3-L005457](../../agents/web_agent.py#L5457) | 5457 | `"                            + type(exc).__name__ + \").\""` | — |
| [SRC-1AE03B9EC3-L005458](../../agents/web_agent.py#L5458) | 5458 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005459](../../agents/web_agent.py#L5459) | 5459 | `"                    search_warnings.extend(repair_warnings)"` | — |
| [SRC-1AE03B9EC3-L005460](../../agents/web_agent.py#L5460) | 5460 | `"                    evidence_repair[\"attempted_query_count\"] = 1"` | — |
| [SRC-1AE03B9EC3-L005461](../../agents/web_agent.py#L5461) | 5461 | `"                    evidence_repair[\"initial_source_count\"] = initial_source_count"` | — |
| [SRC-1AE03B9EC3-L005462](../../agents/web_agent.py#L5462) | 5462 | `"                    evidence_repair[\"initial_independent_domain_count\"] = initial_domain_count"` | — |
| [SRC-1AE03B9EC3-L005463](../../agents/web_agent.py#L5463) | 5463 | `"                    evidence_repair[\"new_sources_added\"] = 0"` | — |
| [SRC-1AE03B9EC3-L005464](../../agents/web_agent.py#L5464) | 5464 | `"                    source_indexes: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L005465](../../agents/web_agent.py#L5465) | 5465 | `"                    for source_index, source in enumerate(sources):"` | — |
| [SRC-1AE03B9EC3-L005466](../../agents/web_agent.py#L5466) | 5466 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L005467](../../agents/web_agent.py#L5467) | 5467 | `"                        if source_key:"` | — |
| [SRC-1AE03B9EC3-L005468](../../agents/web_agent.py#L5468) | 5468 | `"                            source_indexes.setdefault(source_key, source_index)"` | — |
| [SRC-1AE03B9EC3-L005469](../../agents/web_agent.py#L5469) | 5469 | `"                    relevant_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005470](../../agents/web_agent.py#L5470) | 5470 | `"                        query"` | — |
| [SRC-1AE03B9EC3-L005471](../../agents/web_agent.py#L5471) | 5471 | `"                        for query in ("` | — |
| [SRC-1AE03B9EC3-L005472](../../agents/web_agent.py#L5472) | 5472 | `"                            compact_search_query(working_question),"` | — |
| [SRC-1AE03B9EC3-L005473](../../agents/web_agent.py#L5473) | 5473 | `"                            *("` | — |
| [SRC-1AE03B9EC3-L005474](../../agents/web_agent.py#L5474) | 5474 | `"                                compact_search_query(candidate)"` | — |
| [SRC-1AE03B9EC3-L005475](../../agents/web_agent.py#L5475) | 5475 | `"                                for candidate in original_queries"` | — |
| [SRC-1AE03B9EC3-L005476](../../agents/web_agent.py#L5476) | 5476 | `"                                if isinstance(candidate, str)"` | — |
| [SRC-1AE03B9EC3-L005477](../../agents/web_agent.py#L5477) | 5477 | `"                            ),"` | — |
| [SRC-1AE03B9EC3-L005478](../../agents/web_agent.py#L5478) | 5478 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005479](../../agents/web_agent.py#L5479) | 5479 | `"                        if query"` | — |
| [SRC-1AE03B9EC3-L005480](../../agents/web_agent.py#L5480) | 5480 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L005481](../../agents/web_agent.py#L5481) | 5481 | `"                    for source in repair_sources:"` | — |
| [SRC-1AE03B9EC3-L005482](../../agents/web_agent.py#L5482) | 5482 | `"                        if not isinstance(source, dict):"` | — |
| [SRC-1AE03B9EC3-L005483](../../agents/web_agent.py#L5483) | 5483 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L005484](../../agents/web_agent.py#L5484) | 5484 | `"                        if not any("` | — |
| [SRC-1AE03B9EC3-L005485](../../agents/web_agent.py#L5485) | 5485 | `"                            self._source_matches_query(candidate, source)"` | — |
| [SRC-1AE03B9EC3-L005486](../../agents/web_agent.py#L5486) | 5486 | `"                            for candidate in relevant_queries if candidate"` | — |
| [SRC-1AE03B9EC3-L005487](../../agents/web_agent.py#L5487) | 5487 | `"                        ):"` | — |
| [SRC-1AE03B9EC3-L005488](../../agents/web_agent.py#L5488) | 5488 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L005489](../../agents/web_agent.py#L5489) | 5489 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L005490](../../agents/web_agent.py#L5490) | 5490 | `"                        if not source_key:"` | — |
| [SRC-1AE03B9EC3-L005491](../../agents/web_agent.py#L5491) | 5491 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L005492](../../agents/web_agent.py#L5492) | 5492 | `"                        existing_index = source_indexes.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L005493](../../agents/web_agent.py#L5493) | 5493 | `"                        if existing_index is None:"` | — |
| [SRC-1AE03B9EC3-L005494](../../agents/web_agent.py#L5494) | 5494 | `"                            source_indexes[source_key] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005495](../../agents/web_agent.py#L5495) | 5495 | `"                            sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L005496](../../agents/web_agent.py#L5496) | 5496 | `"                            evidence_repair[\"new_sources_added\"] += 1"` | — |
| [SRC-1AE03B9EC3-L005497](../../agents/web_agent.py#L5497) | 5497 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L005498](../../agents/web_agent.py#L5498) | 5498 | `"                        existing_source = sources[existing_index]"` | — |
| [SRC-1AE03B9EC3-L005499](../../agents/web_agent.py#L5499) | 5499 | `"                        providers = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005500](../../agents/web_agent.py#L5500) | 5500 | `"                            list(existing_source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L005501](../../agents/web_agent.py#L5501) | 5501 | `"                            + list(source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L005502](../../agents/web_agent.py#L5502) | 5502 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L005503](../../agents/web_agent.py#L5503) | 5503 | `"                        source_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005504](../../agents/web_agent.py#L5504) | 5504 | `"                            list(existing_source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L005505](../../agents/web_agent.py#L5505) | 5505 | `"                            + list(source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L005506](../../agents/web_agent.py#L5506) | 5506 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L005507](../../agents/web_agent.py#L5507) | 5507 | `"                        if source.get(\"page_fetched\") and not existing_source.get(\"page_fetched\"):"` | — |
| [SRC-1AE03B9EC3-L005508](../../agents/web_agent.py#L5508) | 5508 | `"                            merged_source = dict(existing_source)"` | — |
| [SRC-1AE03B9EC3-L005509](../../agents/web_agent.py#L5509) | 5509 | `"                            merged_source.update(source)"` | — |
| [SRC-1AE03B9EC3-L005510](../../agents/web_agent.py#L5510) | 5510 | `"                            merged_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L005511](../../agents/web_agent.py#L5511) | 5511 | `"                            merged_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L005512](../../agents/web_agent.py#L5512) | 5512 | `"                            sources[existing_index] = merged_source"` | — |
| [SRC-1AE03B9EC3-L005513](../../agents/web_agent.py#L5513) | 5513 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L005514](../../agents/web_agent.py#L5514) | 5514 | `"                            existing_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L005515](../../agents/web_agent.py#L5515) | 5515 | `"                            existing_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L005516](../../agents/web_agent.py#L5516) | 5516 | `"                    sources.sort("` | — |
| [SRC-1AE03B9EC3-L005517](../../agents/web_agent.py#L5517) | 5517 | `"                        key=lambda item: float(item.get(\"rank_score\", 0) or 0),"` | — |
| [SRC-1AE03B9EC3-L005518](../../agents/web_agent.py#L5518) | 5518 | `"                        reverse=True,"` | — |
| [SRC-1AE03B9EC3-L005519](../../agents/web_agent.py#L5519) | 5519 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005520](../../agents/web_agent.py#L5520) | 5520 | `"                    plan[\"queries\"] = list(dict.fromkeys(original_queries + [repair_query]))"` | — |
| [SRC-1AE03B9EC3-L005521](../../agents/web_agent.py#L5521) | 5521 | `"                    independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L005522](../../agents/web_agent.py#L5522) | 5522 | `"                        registrable_domain("` | — |
| [SRC-1AE03B9EC3-L005523](../../agents/web_agent.py#L5523) | 5523 | `"                            source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L005524](../../agents/web_agent.py#L5524) | 5524 | `"                            or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L005525](../../agents/web_agent.py#L5525) | 5525 | `"                            or \"\""` | — |
| [SRC-1AE03B9EC3-L005526](../../agents/web_agent.py#L5526) | 5526 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005527](../../agents/web_agent.py#L5527) | 5527 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L005528](../../agents/web_agent.py#L5528) | 5528 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L005529](../../agents/web_agent.py#L5529) | 5529 | `"                    independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005530](../../agents/web_agent.py#L5530) | 5530 | `"                    needs_corroboration = ("` | — |
| [SRC-1AE03B9EC3-L005531](../../agents/web_agent.py#L5531) | 5531 | `"                        len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L005532](../../agents/web_agent.py#L5532) | 5532 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005533](../../agents/web_agent.py#L5533) | 5533 | `"                    evidence_repair.update({"` | — |
| [SRC-1AE03B9EC3-L005534](../../agents/web_agent.py#L5534) | 5534 | `"                        \"final_source_count\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L005535](../../agents/web_agent.py#L5535) | 5535 | `"                        \"final_independent_domain_count\": len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L005536](../../agents/web_agent.py#L5536) | 5536 | `"                        \"recovered\": not needs_corroboration,"` | — |
| [SRC-1AE03B9EC3-L005537](../../agents/web_agent.py#L5537) | 5537 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L005538](../../agents/web_agent.py#L5538) | 5538 | `"                    evidence_repair[\"reason\"] = ("` | — |
| [SRC-1AE03B9EC3-L005539](../../agents/web_agent.py#L5539) | 5539 | `"                        \"single_bounded_retry_still_insufficient\""` | — |
| [SRC-1AE03B9EC3-L005540](../../agents/web_agent.py#L5540) | 5540 | `"                        if needs_corroboration else \"evidence_gate_recovered\""` | — |
| [SRC-1AE03B9EC3-L005541](../../agents/web_agent.py#L5541) | 5541 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005542](../../agents/web_agent.py#L5542) | 5542 | `"                    report[\"queries_planned\"] = int(report.get(\"queries_planned\", 0) or 0) + int("` | — |
| [SRC-1AE03B9EC3-L005543](../../agents/web_agent.py#L5543) | 5543 | `"                        repair_report.get(\"queries_planned\", 1) or 0"` | — |
| [SRC-1AE03B9EC3-L005544](../../agents/web_agent.py#L5544) | 5544 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005545](../../agents/web_agent.py#L5545) | 5545 | `"                    initial_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L005546](../../agents/web_agent.py#L5546) | 5546 | `"                    repair_attempt_count = repair_report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L005547](../../agents/web_agent.py#L5547) | 5547 | `"                    if initial_attempt_count is None or repair_attempt_count is None:"` | — |
| [SRC-1AE03B9EC3-L005548](../../agents/web_agent.py#L5548) | 5548 | `"                        report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L005549](../../agents/web_agent.py#L5549) | 5549 | `"                        report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L005550](../../agents/web_agent.py#L5550) | 5550 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L005551](../../agents/web_agent.py#L5551) | 5551 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L005552](../../agents/web_agent.py#L5552) | 5552 | `"                            report[\"queries_attempted\"] = max(0, int(initial_attempt_count or 0)) + max("` | — |
| [SRC-1AE03B9EC3-L005553](../../agents/web_agent.py#L5553) | 5553 | `"                                0, int(repair_attempt_count or 0)"` | — |
| [SRC-1AE03B9EC3-L005554](../../agents/web_agent.py#L5554) | 5554 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005555](../../agents/web_agent.py#L5555) | 5555 | `"                            report[\"queries_attempted_known\"] = True"` | — |
| [SRC-1AE03B9EC3-L005556](../../agents/web_agent.py#L5556) | 5556 | `"                        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L005557](../../agents/web_agent.py#L5557) | 5557 | `"                            report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L005558](../../agents/web_agent.py#L5558) | 5558 | `"                            report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L005559](../../agents/web_agent.py#L5559) | 5559 | `"                    report[\"query_results\"] = list(report.get(\"query_results\", [])) + list("` | — |
| [SRC-1AE03B9EC3-L005560](../../agents/web_agent.py#L5560) | 5560 | `"                        repair_report.get(\"query_results\", [])"` | — |
| [SRC-1AE03B9EC3-L005561](../../agents/web_agent.py#L5561) | 5561 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005562](../../agents/web_agent.py#L5562) | 5562 | `"                    merged_providers = {"` | — |
| [SRC-1AE03B9EC3-L005563](../../agents/web_agent.py#L5563) | 5563 | `"                        provider"` | — |
| [SRC-1AE03B9EC3-L005564](../../agents/web_agent.py#L5564) | 5564 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L005565](../../agents/web_agent.py#L5565) | 5565 | `"                        for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L005566](../../agents/web_agent.py#L5566) | 5566 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L005567](../../agents/web_agent.py#L5567) | 5567 | `"                    report[\"providers_used\"] = sorted(merged_providers)"` | — |
| [SRC-1AE03B9EC3-L005568](../../agents/web_agent.py#L5568) | 5568 | `"                    report[\"provider_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L005569](../../agents/web_agent.py#L5569) | 5569 | `"                        provider: sum("` | — |
| [SRC-1AE03B9EC3-L005570](../../agents/web_agent.py#L5570) | 5570 | `"                            provider in source.get(\"providers\", []) for source in sources"` | — |
| [SRC-1AE03B9EC3-L005571](../../agents/web_agent.py#L5571) | 5571 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005572](../../agents/web_agent.py#L5572) | 5572 | `"                        for provider in merged_providers"` | — |
| [SRC-1AE03B9EC3-L005573](../../agents/web_agent.py#L5573) | 5573 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L005574](../../agents/web_agent.py#L5574) | 5574 | `"                    report[\"platform_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L005575](../../agents/web_agent.py#L5575) | 5575 | `"                        str(source.get(\"platform\", \"web\")): sum("` | — |
| [SRC-1AE03B9EC3-L005576](../../agents/web_agent.py#L5576) | 5576 | `"                            str(other.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L005577](../../agents/web_agent.py#L5577) | 5577 | `"                            == str(source.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L005578](../../agents/web_agent.py#L5578) | 5578 | `"                            for other in sources"` | — |
| [SRC-1AE03B9EC3-L005579](../../agents/web_agent.py#L5579) | 5579 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005580](../../agents/web_agent.py#L5580) | 5580 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L005581](../../agents/web_agent.py#L5581) | 5581 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L005582](../../agents/web_agent.py#L5582) | 5582 | `"                    report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005583](../../agents/web_agent.py#L5583) | 5583 | `"                    report[\"pages_fetched\"] = sum("` | — |
| [SRC-1AE03B9EC3-L005584](../../agents/web_agent.py#L5584) | 5584 | `"                        bool(source.get(\"page_fetched\")) for source in sources"` | — |
| [SRC-1AE03B9EC3-L005585](../../agents/web_agent.py#L5585) | 5585 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005586](../../agents/web_agent.py#L5586) | 5586 | `"                    report[\"independent_sources\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L005587](../../agents/web_agent.py#L5587) | 5587 | `"                    report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L005588](../../agents/web_agent.py#L5588) | 5588 | `"                    report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L005589](../../agents/web_agent.py#L5589) | 5589 | `"                        sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L005590](../../agents/web_agent.py#L5590) | 5590 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005591](../../agents/web_agent.py#L5591) | 5591 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L005592](../../agents/web_agent.py#L5592) | 5592 | `"                    evidence_repair[\"reason\"] = \"repair_query_was_not_distinct\""` | — |
| [SRC-1AE03B9EC3-L005593](../../agents/web_agent.py#L5593) | 5593 | `"        # Re-apply task guardrails after the optional repair query so stale,"` | — |
| [SRC-1AE03B9EC3-L005594](../../agents/web_agent.py#L5594) | 5594 | `"        # non-government, or non-social candidates cannot re-enter the answer."` | — |
| [SRC-1AE03B9EC3-L005595](../../agents/web_agent.py#L5595) | 5595 | `"        pre_final_guardrail_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005596](../../agents/web_agent.py#L5596) | 5596 | `"        sources, final_source_guardrails = apply_source_guardrails("` | — |
| [SRC-1AE03B9EC3-L005597](../../agents/web_agent.py#L5597) | 5597 | `"            working_question, clean_mode, plan, sources"` | — |
| [SRC-1AE03B9EC3-L005598](../../agents/web_agent.py#L5598) | 5598 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005599](../../agents/web_agent.py#L5599) | 5599 | `"        report[\"research_pipeline\"] = {"` | — |
| [SRC-1AE03B9EC3-L005600](../../agents/web_agent.py#L5600) | 5600 | `"            \"aspects\": pipeline[\"aspects\"],"` | — |
| [SRC-1AE03B9EC3-L005601](../../agents/web_agent.py#L5601) | 5601 | `"            \"evidence\": evaluate_research_evidence(pipeline[\"aspects\"], sources),"` | — |
| [SRC-1AE03B9EC3-L005602](../../agents/web_agent.py#L5602) | 5602 | `"            \"stages\": pipeline[\"stages\"],"` | — |
| [SRC-1AE03B9EC3-L005603](../../agents/web_agent.py#L5603) | 5603 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005604](../../agents/web_agent.py#L5604) | 5604 | `"        report[\"source_guardrails\"][\"final\"] = final_source_guardrails"` | — |
| [SRC-1AE03B9EC3-L005605](../../agents/web_agent.py#L5605) | 5605 | `"        report[\"source_guardrails\"][\"repair_candidates_before_final_filter\"] = ("` | — |
| [SRC-1AE03B9EC3-L005606](../../agents/web_agent.py#L5606) | 5606 | `"            pre_final_guardrail_count"` | — |
| [SRC-1AE03B9EC3-L005607](../../agents/web_agent.py#L5607) | 5607 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005608](../../agents/web_agent.py#L5608) | 5608 | `"        if final_source_guardrails[\"rejected_sources\"]:"` | — |
| [SRC-1AE03B9EC3-L005609](../../agents/web_agent.py#L5609) | 5609 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005610](../../agents/web_agent.py#L5610) | 5610 | `"                \"أُعيد تطبيق شروط قبول الأدلة بعد محاولة الإصلاح؛ لم تُستخدم النتائج \""` | — |
| [SRC-1AE03B9EC3-L005611](../../agents/web_agent.py#L5611) | 5611 | `"                \"التي أخفقت في شروط الرسمية أو الحداثة أو كونها منشورات اجتماعية.\""` | — |
| [SRC-1AE03B9EC3-L005612](../../agents/web_agent.py#L5612) | 5612 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005613](../../agents/web_agent.py#L5613) | 5613 | `"        if evidence_repair.get(\"attempted\") and \"final_source_count\" in evidence_repair:"` | — |
| [SRC-1AE03B9EC3-L005614](../../agents/web_agent.py#L5614) | 5614 | `"            final_domains = {"` | — |
| [SRC-1AE03B9EC3-L005615](../../agents/web_agent.py#L5615) | 5615 | `"                registrable_domain("` | — |
| [SRC-1AE03B9EC3-L005616](../../agents/web_agent.py#L5616) | 5616 | `"                    source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L005617](../../agents/web_agent.py#L5617) | 5617 | `"                    or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L005618](../../agents/web_agent.py#L5618) | 5618 | `"                    or \"\""` | — |
| [SRC-1AE03B9EC3-L005619](../../agents/web_agent.py#L5619) | 5619 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005620](../../agents/web_agent.py#L5620) | 5620 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L005621](../../agents/web_agent.py#L5621) | 5621 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005622](../../agents/web_agent.py#L5622) | 5622 | `"            final_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005623](../../agents/web_agent.py#L5623) | 5623 | `"            evidence_repair[\"final_source_count\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005624](../../agents/web_agent.py#L5624) | 5624 | `"            evidence_repair[\"final_independent_domain_count\"] = len(final_domains)"` | — |
| [SRC-1AE03B9EC3-L005625](../../agents/web_agent.py#L5625) | 5625 | `"            evidence_repair[\"recovered\"] = ("` | — |
| [SRC-1AE03B9EC3-L005626](../../agents/web_agent.py#L5626) | 5626 | `"                len(sources) >= 2 and len(final_domains) >= 2"` | — |
| [SRC-1AE03B9EC3-L005627](../../agents/web_agent.py#L5627) | 5627 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005628](../../agents/web_agent.py#L5628) | 5628 | `"            evidence_repair[\"new_sources_added\"] = max("` | — |
| [SRC-1AE03B9EC3-L005629](../../agents/web_agent.py#L5629) | 5629 | `"                0,"` | — |
| [SRC-1AE03B9EC3-L005630](../../agents/web_agent.py#L5630) | 5630 | `"                len(sources) - int("` | — |
| [SRC-1AE03B9EC3-L005631](../../agents/web_agent.py#L5631) | 5631 | `"                    report[\"source_guardrails\"].get(\"initial_eligible_source_count\", 0)"` | — |
| [SRC-1AE03B9EC3-L005632](../../agents/web_agent.py#L5632) | 5632 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005633](../../agents/web_agent.py#L5633) | 5633 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005634](../../agents/web_agent.py#L5634) | 5634 | `"        final_independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L005635](../../agents/web_agent.py#L5635) | 5635 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L005636](../../agents/web_agent.py#L5636) | 5636 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L005637](../../agents/web_agent.py#L5637) | 5637 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L005638](../../agents/web_agent.py#L5638) | 5638 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L005639](../../agents/web_agent.py#L5639) | 5639 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005640](../../agents/web_agent.py#L5640) | 5640 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005641](../../agents/web_agent.py#L5641) | 5641 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005642](../../agents/web_agent.py#L5642) | 5642 | `"        final_independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005643](../../agents/web_agent.py#L5643) | 5643 | `"        # All post-filter source metrics describe the sources that remain eligible"` | — |
| [SRC-1AE03B9EC3-L005644](../../agents/web_agent.py#L5644) | 5644 | `"        # for the answer. Connector-level received/accepted/rejected totals remain"` | — |
| [SRC-1AE03B9EC3-L005645](../../agents/web_agent.py#L5645) | 5645 | `"        # available in provider diagnostics and are intentionally separate."` | — |
| [SRC-1AE03B9EC3-L005646](../../agents/web_agent.py#L5646) | 5646 | `"        independent_domains = final_independent_domains"` | — |
| [SRC-1AE03B9EC3-L005647](../../agents/web_agent.py#L5647) | 5647 | `"        report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005648](../../agents/web_agent.py#L5648) | 5648 | `"        report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005649](../../agents/web_agent.py#L5649) | 5649 | `"        report[\"distinct_registrable_domains\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L005650](../../agents/web_agent.py#L5650) | 5650 | `"        report[\"independent_sources\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L005651](../../agents/web_agent.py#L5651) | 5651 | `"        report[\"providers_used\"] = sorted({"` | — |
| [SRC-1AE03B9EC3-L005652](../../agents/web_agent.py#L5652) | 5652 | `"            str(provider)"` | — |
| [SRC-1AE03B9EC3-L005653](../../agents/web_agent.py#L5653) | 5653 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005654](../../agents/web_agent.py#L5654) | 5654 | `"            for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L005655](../../agents/web_agent.py#L5655) | 5655 | `"            if provider"` | — |
| [SRC-1AE03B9EC3-L005656](../../agents/web_agent.py#L5656) | 5656 | `"        })"` | — |
| [SRC-1AE03B9EC3-L005657](../../agents/web_agent.py#L5657) | 5657 | `"        report[\"provider_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L005658](../../agents/web_agent.py#L5658) | 5658 | `"            provider: sum(provider in source.get(\"providers\", []) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005659](../../agents/web_agent.py#L5659) | 5659 | `"            for provider in report[\"providers_used\"]"` | — |
| [SRC-1AE03B9EC3-L005660](../../agents/web_agent.py#L5660) | 5660 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005661](../../agents/web_agent.py#L5661) | 5661 | `"        report[\"platform_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L005662](../../agents/web_agent.py#L5662) | 5662 | `"            str(source.get(\"platform\", \"web\")): sum("` | — |
| [SRC-1AE03B9EC3-L005663](../../agents/web_agent.py#L5663) | 5663 | `"                str(other.get(\"platform\", \"web\")) == str(source.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L005664](../../agents/web_agent.py#L5664) | 5664 | `"                for other in sources"` | — |
| [SRC-1AE03B9EC3-L005665](../../agents/web_agent.py#L5665) | 5665 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005666](../../agents/web_agent.py#L5666) | 5666 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005667](../../agents/web_agent.py#L5667) | 5667 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005668](../../agents/web_agent.py#L5668) | 5668 | `"        report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L005669](../../agents/web_agent.py#L5669) | 5669 | `"            sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L005670](../../agents/web_agent.py#L5670) | 5670 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005671](../../agents/web_agent.py#L5671) | 5671 | `"        needs_corroboration = ("` | — |
| [SRC-1AE03B9EC3-L005672](../../agents/web_agent.py#L5672) | 5672 | `"            len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L005673](../../agents/web_agent.py#L5673) | 5673 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005674](../../agents/web_agent.py#L5674) | 5674 | `"        report[\"evidence_repair\"] = evidence_repair"` | — |
| [SRC-1AE03B9EC3-L005675](../../agents/web_agent.py#L5675) | 5675 | `"        baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L005676](../../agents/web_agent.py#L5676) | 5676 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L005677](../../agents/web_agent.py#L5677) | 5677 | `"            current_research_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L005678](../../agents/web_agent.py#L5678) | 5678 | `"                item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L005679](../../agents/web_agent.py#L5679) | 5679 | `"                if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L005680](../../agents/web_agent.py#L5680) | 5680 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L005681](../../agents/web_agent.py#L5681) | 5681 | `"        report[\"provider_diagnostics\"] = current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L005682](../../agents/web_agent.py#L5682) | 5682 | `"        provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L005683](../../agents/web_agent.py#L5683) | 5683 | `"            item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L005684](../../agents/web_agent.py#L5684) | 5684 | `"            for item in current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L005685](../../agents/web_agent.py#L5685) | 5685 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005686](../../agents/web_agent.py#L5686) | 5686 | `"        raw_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L005687](../../agents/web_agent.py#L5687) | 5687 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L005688](../../agents/web_agent.py#L5688) | 5688 | `"            queries_attempted = ("` | — |
| [SRC-1AE03B9EC3-L005689](../../agents/web_agent.py#L5689) | 5689 | `"                None if raw_attempt_count is None"` | — |
| [SRC-1AE03B9EC3-L005690](../../agents/web_agent.py#L5690) | 5690 | `"                else max(0, int(raw_attempt_count or 0))"` | — |
| [SRC-1AE03B9EC3-L005691](../../agents/web_agent.py#L5691) | 5691 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005692](../../agents/web_agent.py#L5692) | 5692 | `"        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L005693](../../agents/web_agent.py#L5693) | 5693 | `"            queries_attempted = None"` | — |
| [SRC-1AE03B9EC3-L005694](../../agents/web_agent.py#L5694) | 5694 | `"        if queries_attempted is not None:"` | — |
| [SRC-1AE03B9EC3-L005695](../../agents/web_agent.py#L5695) | 5695 | `"            search_attempted = ("` | — |
| [SRC-1AE03B9EC3-L005696](../../agents/web_agent.py#L5696) | 5696 | `"                queries_attempted > 0"` | — |
| [SRC-1AE03B9EC3-L005697](../../agents/web_agent.py#L5697) | 5697 | `"                or provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L005698](../../agents/web_agent.py#L5698) | 5698 | `"                or report.get(\"search_attempted\") is True"` | — |
| [SRC-1AE03B9EC3-L005699](../../agents/web_agent.py#L5699) | 5699 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005700](../../agents/web_agent.py#L5700) | 5700 | `"        elif provider_attempt_observed or report.get(\"search_attempted\") is True:"` | — |
| [SRC-1AE03B9EC3-L005701](../../agents/web_agent.py#L5701) | 5701 | `"            search_attempted = True"` | — |
| [SRC-1AE03B9EC3-L005702](../../agents/web_agent.py#L5702) | 5702 | `"        elif isinstance(report.get(\"search_attempted\"), bool):"` | — |
| [SRC-1AE03B9EC3-L005703](../../agents/web_agent.py#L5703) | 5703 | `"            search_attempted = report[\"search_attempted\"]"` | — |
| [SRC-1AE03B9EC3-L005704](../../agents/web_agent.py#L5704) | 5704 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005705](../../agents/web_agent.py#L5705) | 5705 | `"            search_attempted = None"` | — |
| [SRC-1AE03B9EC3-L005706](../../agents/web_agent.py#L5706) | 5706 | `"        report[\"queries_attempted\"] = queries_attempted"` | — |
| [SRC-1AE03B9EC3-L005707](../../agents/web_agent.py#L5707) | 5707 | `"        report[\"queries_attempted_known\"] = queries_attempted is not None"` | — |
| [SRC-1AE03B9EC3-L005708](../../agents/web_agent.py#L5708) | 5708 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L005709](../../agents/web_agent.py#L5709) | 5709 | `"        previous_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L005710](../../agents/web_agent.py#L5710) | 5710 | `"        if previous_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L005711](../../agents/web_agent.py#L5711) | 5711 | `"            if provider_attempt_observed or search_attempted is True:"` | — |
| [SRC-1AE03B9EC3-L005712](../../agents/web_agent.py#L5712) | 5712 | `"                search_outcome = \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L005713](../../agents/web_agent.py#L5713) | 5713 | `"            elif search_attempted is False:"` | — |
| [SRC-1AE03B9EC3-L005714](../../agents/web_agent.py#L5714) | 5714 | `"                search_outcome = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L005715](../../agents/web_agent.py#L5715) | 5715 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005716](../../agents/web_agent.py#L5716) | 5716 | `"                search_outcome = \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L005717](../../agents/web_agent.py#L5717) | 5717 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005718](../../agents/web_agent.py#L5718) | 5718 | `"            search_outcome = ("` | — |
| [SRC-1AE03B9EC3-L005719](../../agents/web_agent.py#L5719) | 5719 | `"                \"attempted_with_usable_sources\" if search_attempted is True and sources"` | — |
| [SRC-1AE03B9EC3-L005720](../../agents/web_agent.py#L5720) | 5720 | `"                else \"attempted_no_usable_sources\" if search_attempted is True"` | — |
| [SRC-1AE03B9EC3-L005721](../../agents/web_agent.py#L5721) | 5721 | `"                else \"not_attempted\" if search_attempted is False"` | — |
| [SRC-1AE03B9EC3-L005722](../../agents/web_agent.py#L5722) | 5722 | `"                else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L005723](../../agents/web_agent.py#L5723) | 5723 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005724](../../agents/web_agent.py#L5724) | 5724 | `"        report[\"search_outcome\"] = search_outcome"` | — |
| [SRC-1AE03B9EC3-L005725](../../agents/web_agent.py#L5725) | 5725 | `"        if search_outcome in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L005726](../../agents/web_agent.py#L5726) | 5726 | `"            report[\"usable_sources_after_filtering\"] = None"` | — |
| [SRC-1AE03B9EC3-L005727](../../agents/web_agent.py#L5727) | 5727 | `"            report[\"unique_sources\"] = None"` | — |
| [SRC-1AE03B9EC3-L005728](../../agents/web_agent.py#L5728) | 5728 | `"            report[\"pages_fetched\"] = None"` | — |
| [SRC-1AE03B9EC3-L005729](../../agents/web_agent.py#L5729) | 5729 | `"            report[\"provider_counts\"] = None"` | — |
| [SRC-1AE03B9EC3-L005730](../../agents/web_agent.py#L5730) | 5730 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005731](../../agents/web_agent.py#L5731) | 5731 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005732](../../agents/web_agent.py#L5732) | 5732 | `"            if report.get(\"unique_sources\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L005733](../../agents/web_agent.py#L5733) | 5733 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005734](../../agents/web_agent.py#L5734) | 5734 | `"            if report.get(\"pages_fetched\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L005735](../../agents/web_agent.py#L5735) | 5735 | `"                report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005736](../../agents/web_agent.py#L5736) | 5736 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L005737](../../agents/web_agent.py#L5737) | 5737 | `"        report[\"distinct_registrable_domains\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L005738](../../agents/web_agent.py#L5738) | 5738 | `"        report[\"independent_sources\"] = len(independent_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L005739](../../agents/web_agent.py#L5739) | 5739 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005740](../../agents/web_agent.py#L5740) | 5740 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L005741](../../agents/web_agent.py#L5741) | 5741 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005742](../../agents/web_agent.py#L5742) | 5742 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005743](../../agents/web_agent.py#L5743) | 5743 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L005744](../../agents/web_agent.py#L5744) | 5744 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005745](../../agents/web_agent.py#L5745) | 5745 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L005746](../../agents/web_agent.py#L5746) | 5746 | `"        if len(independent_domains) >= 2:"` | — |
| [SRC-1AE03B9EC3-L005747](../../agents/web_agent.py#L5747) | 5747 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005748](../../agents/web_agent.py#L5748) | 5748 | `"                \"تعدد النطاقات المسجلة لا يثبت الاستقلال التحريري؛ قد تنقل المواقع عن المصدر الأصلي نفسه.\""` | — |
| [SRC-1AE03B9EC3-L005749](../../agents/web_agent.py#L5749) | 5749 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005750](../../agents/web_agent.py#L5750) | 5750 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L005751](../../agents/web_agent.py#L5751) | 5751 | `"        if needs_corroboration and single_source_navigation and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005752](../../agents/web_agent.py#L5752) | 5752 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005753](../../agents/web_agent.py#L5753) | 5753 | `"                \"هذه نتيجة مرشحة لطلب العثور على موقع/رابط؛ لم تُثبت رسميتها أو صحتها \""` | — |
| [SRC-1AE03B9EC3-L005754](../../agents/web_agent.py#L5754) | 5754 | `"                \"من مصدر مستقل، لذا راجع الرابط قبل الاعتماد عليه.\""` | — |
| [SRC-1AE03B9EC3-L005755](../../agents/web_agent.py#L5755) | 5755 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005756](../../agents/web_agent.py#L5756) | 5756 | `"        if needs_corroboration and (single_source_social or single_source_lead) and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005757](../../agents/web_agent.py#L5757) | 5757 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005758](../../agents/web_agent.py#L5758) | 5758 | `"                \"هذه إشارات بحث أولية وليست تحققًا مستقلًا من هوية العميل أو نيته؛ \""` | — |
| [SRC-1AE03B9EC3-L005759](../../agents/web_agent.py#L5759) | 5759 | `"                \"راجع المنشور وتاريخه وسياقه قبل التواصل أو اتخاذ قرار.\""` | — |
| [SRC-1AE03B9EC3-L005760](../../agents/web_agent.py#L5760) | 5760 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005761](../../agents/web_agent.py#L5761) | 5761 | `"        if needs_corroboration and single_source_listing and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005762](../../agents/web_agent.py#L5762) | 5762 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005763](../../agents/web_agent.py#L5763) | 5763 | `"                \"هذه إعلانات/قوائم مرشحة فقط. قد تكون منتهية أو غير دقيقة؛ تحقق من السعر \""` | — |
| [SRC-1AE03B9EC3-L005764](../../agents/web_agent.py#L5764) | 5764 | `"                \"والتوافر ومصدر الإعلان واطلب تأكيدًا حديثًا قبل دفع مال أو مشاركة بيانات.\""` | — |
| [SRC-1AE03B9EC3-L005765](../../agents/web_agent.py#L5765) | 5765 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005766](../../agents/web_agent.py#L5766) | 5766 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L005767](../../agents/web_agent.py#L5767) | 5767 | `"        if needs_corroboration and not task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L005768](../../agents/web_agent.py#L5768) | 5768 | `"            if search_outcome == \"unknown_after_research_error\":"` | — |
| [SRC-1AE03B9EC3-L005769](../../agents/web_agent.py#L5769) | 5769 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005770](../../agents/web_agent.py#L5770) | 5770 | `"                    \"تعذر إكمال مسار البحث بسبب خطأ، ولا توجد بيانات كافية لتحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L005771](../../agents/web_agent.py#L5771) | 5771 | `"                    \"كانت محاولة البحث قد اكتملت أو كم نتيجة جُمعت. لذلك لا أستطيع الجزم \""` | — |
| [SRC-1AE03B9EC3-L005772](../../agents/web_agent.py#L5772) | 5772 | `"                    \"بأن البحث لم يُنفّذ أو أن الإنترنت لم يُعد نتائج. لم أتمكن من تقديم \""` | — |
| [SRC-1AE03B9EC3-L005773](../../agents/web_agent.py#L5773) | 5773 | `"                    \"إجابة مكتملة؛ أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005774](../../agents/web_agent.py#L5774) | 5774 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005775](../../agents/web_agent.py#L5775) | 5775 | `"            elif search_outcome == \"attempted_research_error\":"` | — |
| [SRC-1AE03B9EC3-L005776](../../agents/web_agent.py#L5776) | 5776 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005777](../../agents/web_agent.py#L5777) | 5777 | `"                    \"توجد قرائن تشغيلية على بدء محاولة بحث، لكن مسار البحث فشل قبل إنتاج \""` | — |
| [SRC-1AE03B9EC3-L005778](../../agents/web_agent.py#L5778) | 5778 | `"                    \"تقرير مكتمل. لا أستطيع تحديد عدد النتائج أو المصادر القابلة للاستخدام، \""` | — |
| [SRC-1AE03B9EC3-L005779](../../agents/web_agent.py#L5779) | 5779 | `"                    \"لذلك لن أخمّن. أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005780](../../agents/web_agent.py#L5780) | 5780 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005781](../../agents/web_agent.py#L5781) | 5781 | `"            elif search_outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-1AE03B9EC3-L005782](../../agents/web_agent.py#L5782) | 5782 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005783](../../agents/web_agent.py#L5783) | 5783 | `"                    \"جرت محاولة البحث، لكن لم تتوفر مصادر صالحة وكافية للإجابة بعد تصفية \""` | — |
| [SRC-1AE03B9EC3-L005784](../../agents/web_agent.py#L5784) | 5784 | `"                    \"النتائج. هذا لا يثبت أن جميع المواقع أو الإنترنت غير متاح؛ لن أخمّن \""` | — |
| [SRC-1AE03B9EC3-L005785](../../agents/web_agent.py#L5785) | 5785 | `"                    \"أو أقدّم نتيجة غير مدعومة. جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005786](../../agents/web_agent.py#L5786) | 5786 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005787](../../agents/web_agent.py#L5787) | 5787 | `"            elif search_outcome == \"not_attempted\":"` | — |
| [SRC-1AE03B9EC3-L005788](../../agents/web_agent.py#L5788) | 5788 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005789](../../agents/web_agent.py#L5789) | 5789 | `"                    \"لم تبدأ محاولة بحث ويب لهذا الطلب، لذلك لا تتوفر لدي أدلة ويب حالية \""` | — |
| [SRC-1AE03B9EC3-L005790](../../agents/web_agent.py#L5790) | 5790 | `"                    \"كافية للإجابة. لن أقدّم نتيجة غير مدعومة؛ أعد المحاولة أو اطلب بحثًا \""` | — |
| [SRC-1AE03B9EC3-L005791](../../agents/web_agent.py#L5791) | 5791 | `"                    \"صريحًا إذا كان ذلك مناسبًا.\""` | — |
| [SRC-1AE03B9EC3-L005792](../../agents/web_agent.py#L5792) | 5792 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005793](../../agents/web_agent.py#L5793) | 5793 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005794](../../agents/web_agent.py#L5794) | 5794 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005795](../../agents/web_agent.py#L5795) | 5795 | `"                    \"لم أجد معلومات موثوقة كافية مرتبطة بسؤالك من نطاقين مسجلين مختلفين على الأقل. \""` | — |
| [SRC-1AE03B9EC3-L005796](../../agents/web_agent.py#L5796) | 5796 | `"                    \"اختلاف النطاقات لا يثبت الاستقلال التحريري. لن أخمّن أو أقدّم نتيجة غير مدعومة؛ \""` | — |
| [SRC-1AE03B9EC3-L005797](../../agents/web_agent.py#L5797) | 5797 | `"                    \"جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005798](../../agents/web_agent.py#L5798) | 5798 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005799](../../agents/web_agent.py#L5799) | 5799 | `"            public_sources = [{"` | — |
| [SRC-1AE03B9EC3-L005800](../../agents/web_agent.py#L5800) | 5800 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L005801](../../agents/web_agent.py#L5801) | 5801 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L005802](../../agents/web_agent.py#L5802) | 5802 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005803](../../agents/web_agent.py#L5803) | 5803 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005804](../../agents/web_agent.py#L5804) | 5804 | `"                \"readable_page_text_available\": bool(source.get(\"page_fetched\")) and bool(str(source.get(\"page_text\") or \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L005805](../../agents/web_agent.py#L5805) | 5805 | `"                \"page_text_present_without_fetch_flag\": bool(str(source.get(\"page_text\") or \"\").strip()) and not bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005806](../../agents/web_agent.py#L5806) | 5806 | `"                \"page_fetch_status\": source.get(\"page_fetch_status\", \"unknown\"),"` | — |
| [SRC-1AE03B9EC3-L005807](../../agents/web_agent.py#L5807) | 5807 | `"                \"page_fetch_error_class\": source.get(\"page_fetch_error_class\"),"` | — |
| [SRC-1AE03B9EC3-L005808](../../agents/web_agent.py#L5808) | 5808 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L005809](../../agents/web_agent.py#L5809) | 5809 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005810](../../agents/web_agent.py#L5810) | 5810 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L005811](../../agents/web_agent.py#L5811) | 5811 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005812](../../agents/web_agent.py#L5812) | 5812 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L005813](../../agents/web_agent.py#L5813) | 5813 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005814](../../agents/web_agent.py#L5814) | 5814 | `"                \"opinion_source_classification\": source.get(\"opinion_source_classification\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005815](../../agents/web_agent.py#L5815) | 5815 | `"                \"opinion_classification_basis\": source.get(\"opinion_classification_basis\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005816](../../agents/web_agent.py#L5816) | 5816 | `"                \"opinion_classification_method\": source.get(\"opinion_classification_method\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005817](../../agents/web_agent.py#L5817) | 5817 | `"                \"current_evidence_assessment\": source.get(\"current_evidence_assessment\", {}),"` | — |
| [SRC-1AE03B9EC3-L005818](../../agents/web_agent.py#L5818) | 5818 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005819](../../agents/web_agent.py#L5819) | 5819 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005820](../../agents/web_agent.py#L5820) | 5820 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L005821](../../agents/web_agent.py#L5821) | 5821 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L005822](../../agents/web_agent.py#L5822) | 5822 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L005823](../../agents/web_agent.py#L5823) | 5823 | `"            } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L005824](../../agents/web_agent.py#L5824) | 5824 | `"            citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L005825](../../agents/web_agent.py#L5825) | 5825 | `"                reason, 0, [], \"not_run\""` | — |
| [SRC-1AE03B9EC3-L005826](../../agents/web_agent.py#L5826) | 5826 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005827](../../agents/web_agent.py#L5827) | 5827 | `"            citation_validation[\"status\"] = \"not_applicable_no_generated_answer\""` | — |
| [SRC-1AE03B9EC3-L005828](../../agents/web_agent.py#L5828) | 5828 | `"            coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L005829](../../agents/web_agent.py#L5829) | 5829 | `"            answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L005830](../../agents/web_agent.py#L5830) | 5830 | `"                \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L005831](../../agents/web_agent.py#L5831) | 5831 | `"                \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L005832](../../agents/web_agent.py#L5832) | 5832 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L005833](../../agents/web_agent.py#L5833) | 5833 | `"                    \"not_reviewed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L005834](../../agents/web_agent.py#L5834) | 5834 | `"                    if coverage_targets else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005835](../../agents/web_agent.py#L5835) | 5835 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005836](../../agents/web_agent.py#L5836) | 5836 | `"                \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L005837](../../agents/web_agent.py#L5837) | 5837 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005838](../../agents/web_agent.py#L5838) | 5838 | `"            answer_integrity = audit_answer_integrity(working_question, reason, sources, coverage_targets, plan.get(\"requirement_queries\"))"` | — |
| [SRC-1AE03B9EC3-L005839](../../agents/web_agent.py#L5839) | 5839 | `"            answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005840](../../agents/web_agent.py#L5840) | 5840 | `"            answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L005841](../../agents/web_agent.py#L5841) | 5841 | `"            answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L005842](../../agents/web_agent.py#L5842) | 5842 | `"            answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L005843](../../agents/web_agent.py#L5843) | 5843 | `"            task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L005844](../../agents/web_agent.py#L5844) | 5844 | `"                \"not_assessed_insufficient_evidence\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005845](../../agents/web_agent.py#L5845) | 5845 | `"                else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005846](../../agents/web_agent.py#L5846) | 5846 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005847](../../agents/web_agent.py#L5847) | 5847 | `"            answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L005848](../../agents/web_agent.py#L5848) | 5848 | `"            research_failed = search_outcome in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L005849](../../agents/web_agent.py#L5849) | 5849 | `"            report.update({"` | — |
| [SRC-1AE03B9EC3-L005850](../../agents/web_agent.py#L5850) | 5850 | `"                # When collection failed, an empty local list is not evidence that"` | — |
| [SRC-1AE03B9EC3-L005851](../../agents/web_agent.py#L5851) | 5851 | `"                # the remote search returned zero sources; preserve unknown counts."` | — |
| [SRC-1AE03B9EC3-L005852](../../agents/web_agent.py#L5852) | 5852 | `"                \"unique_sources\": None if research_failed else len(sources),"` | — |
| [SRC-1AE03B9EC3-L005853](../../agents/web_agent.py#L5853) | 5853 | `"                \"independent_sources\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L005854](../../agents/web_agent.py#L5854) | 5854 | `"                \"distinct_registrable_domains\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L005855](../../agents/web_agent.py#L5855) | 5855 | `"                \"pages_fetched\": ("` | — |
| [SRC-1AE03B9EC3-L005856](../../agents/web_agent.py#L5856) | 5856 | `"                    None if research_failed"` | — |
| [SRC-1AE03B9EC3-L005857](../../agents/web_agent.py#L5857) | 5857 | `"                    else sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005858](../../agents/web_agent.py#L5858) | 5858 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005859](../../agents/web_agent.py#L5859) | 5859 | `"                \"provider_diagnostics\": current_research_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L005860](../../agents/web_agent.py#L5860) | 5860 | `"                \"insufficient_evidence\": True,"` | — |
| [SRC-1AE03B9EC3-L005861](../../agents/web_agent.py#L5861) | 5861 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L005862](../../agents/web_agent.py#L5862) | 5862 | `"                \"citation_check\": citation_validation[\"status\"],"` | — |
| [SRC-1AE03B9EC3-L005863](../../agents/web_agent.py#L5863) | 5863 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L005864](../../agents/web_agent.py#L5864) | 5864 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L005865](../../agents/web_agent.py#L5865) | 5865 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L005866](../../agents/web_agent.py#L5866) | 5866 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L005867](../../agents/web_agent.py#L5867) | 5867 | `"                \"connector_summary\": report.get(\"connector_summary\") or self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L005868](../../agents/web_agent.py#L5868) | 5868 | `"                    current_research_diagnostics, sources"` | — |
| [SRC-1AE03B9EC3-L005869](../../agents/web_agent.py#L5869) | 5869 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005870](../../agents/web_agent.py#L5870) | 5870 | `"            })"` | — |
| [SRC-1AE03B9EC3-L005871](../../agents/web_agent.py#L5871) | 5871 | `"            return {"` | — |
| [SRC-1AE03B9EC3-L005872](../../agents/web_agent.py#L5872) | 5872 | `"                \"answer\": reason,"` | — |
| [SRC-1AE03B9EC3-L005873](../../agents/web_agent.py#L5873) | 5873 | `"                \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L005874](../../agents/web_agent.py#L5874) | 5874 | `"                \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L005875](../../agents/web_agent.py#L5875) | 5875 | `"                \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005876](../../agents/web_agent.py#L5876) | 5876 | `"                \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L005877](../../agents/web_agent.py#L5877) | 5877 | `"                    \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L005878](../../agents/web_agent.py#L5878) | 5878 | `"                    \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L005879](../../agents/web_agent.py#L5879) | 5879 | `"                    \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L005880](../../agents/web_agent.py#L5880) | 5880 | `"                    \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L005881](../../agents/web_agent.py#L5881) | 5881 | `"                    \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L005882](../../agents/web_agent.py#L5882) | 5882 | `"                    \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L005883](../../agents/web_agent.py#L5883) | 5883 | `"                    \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L005884](../../agents/web_agent.py#L5884) | 5884 | `"                    \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L005885](../../agents/web_agent.py#L5885) | 5885 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005886](../../agents/web_agent.py#L5886) | 5886 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005887](../../agents/web_agent.py#L5887) | 5887 | `"                },"` | — |
| [SRC-1AE03B9EC3-L005888](../../agents/web_agent.py#L5888) | 5888 | `"                \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L005889](../../agents/web_agent.py#L5889) | 5889 | `"                \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L005890](../../agents/web_agent.py#L5890) | 5890 | `"                \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L005891](../../agents/web_agent.py#L5891) | 5891 | `"                \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L005892](../../agents/web_agent.py#L5892) | 5892 | `"                \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L005893](../../agents/web_agent.py#L5893) | 5893 | `"                \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L005894](../../agents/web_agent.py#L5894) | 5894 | `"                \"warnings\": list(dict.fromkeys(search_warnings + [reason])),"` | — |
| [SRC-1AE03B9EC3-L005895](../../agents/web_agent.py#L5895) | 5895 | `"                \"kind\": \"insufficient_evidence\","` | — |
| [SRC-1AE03B9EC3-L005896](../../agents/web_agent.py#L5896) | 5896 | `"                \"final_answer_status\": \"insufficient_evidence_no_generation\","` | — |
| [SRC-1AE03B9EC3-L005897](../../agents/web_agent.py#L5897) | 5897 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005898](../../agents/web_agent.py#L5898) | 5898 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005899](../../agents/web_agent.py#L5899) | 5899 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L005900](../../agents/web_agent.py#L5900) | 5900 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L005901](../../agents/web_agent.py#L5901) | 5901 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L005902](../../agents/web_agent.py#L5902) | 5902 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L005903](../../agents/web_agent.py#L5903) | 5903 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L005904](../../agents/web_agent.py#L5904) | 5904 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005905](../../agents/web_agent.py#L5905) | 5905 | `""` | — |
| [SRC-1AE03B9EC3-L005906](../../agents/web_agent.py#L5906) | 5906 | `"        answer = \"\""` | — |
| [SRC-1AE03B9EC3-L005907](../../agents/web_agent.py#L5907) | 5907 | `"        used_llm = False"` | — |
| [SRC-1AE03B9EC3-L005908](../../agents/web_agent.py#L5908) | 5908 | `"        llm_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005909](../../agents/web_agent.py#L5909) | 5909 | `"        generation_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L005910](../../agents/web_agent.py#L5910) | 5910 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L005911](../../agents/web_agent.py#L5911) | 5911 | `"            answer = self._generate("` | — |
| [SRC-1AE03B9EC3-L005912](../../agents/web_agent.py#L5912) | 5912 | `"                working_question,"` | — |
| [SRC-1AE03B9EC3-L005913](../../agents/web_agent.py#L5913) | 5913 | `"                clean_history,"` | — |
| [SRC-1AE03B9EC3-L005914](../../agents/web_agent.py#L5914) | 5914 | `"                sources,"` | — |
| [SRC-1AE03B9EC3-L005915](../../agents/web_agent.py#L5915) | 5915 | `"                search_warning,"` | — |
| [SRC-1AE03B9EC3-L005916](../../agents/web_agent.py#L5916) | 5916 | `"                research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L005917](../../agents/web_agent.py#L5917) | 5917 | `"                search_report=report,"` | — |
| [SRC-1AE03B9EC3-L005918](../../agents/web_agent.py#L5918) | 5918 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005919](../../agents/web_agent.py#L5919) | 5919 | `"            used_llm = True"` | — |
| [SRC-1AE03B9EC3-L005920](../../agents/web_agent.py#L5920) | 5920 | `"            if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L005921](../../agents/web_agent.py#L5921) | 5921 | `"                existing_urls = {item.get(\"url\") for item in sources}"` | — |
| [SRC-1AE03B9EC3-L005922](../../agents/web_agent.py#L5922) | 5922 | `"                relevance_queries = []"` | — |
| [SRC-1AE03B9EC3-L005923](../../agents/web_agent.py#L5923) | 5923 | `"                planned_queries = plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005924](../../agents/web_agent.py#L5924) | 5924 | `"                if not isinstance(planned_queries, list):"` | — |
| [SRC-1AE03B9EC3-L005925](../../agents/web_agent.py#L5925) | 5925 | `"                    planned_queries = []"` | — |
| [SRC-1AE03B9EC3-L005926](../../agents/web_agent.py#L5926) | 5926 | `"                for candidate_query in [working_question, *planned_queries]:"` | — |
| [SRC-1AE03B9EC3-L005927](../../agents/web_agent.py#L5927) | 5927 | `"                    if not isinstance(candidate_query, str):"` | — |
| [SRC-1AE03B9EC3-L005928](../../agents/web_agent.py#L5928) | 5928 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L005929](../../agents/web_agent.py#L5929) | 5929 | `"                    compacted_query = compact_search_query(candidate_query)"` | — |
| [SRC-1AE03B9EC3-L005930](../../agents/web_agent.py#L5930) | 5930 | `"                    if compacted_query and compacted_query not in relevance_queries:"` | — |
| [SRC-1AE03B9EC3-L005931](../../agents/web_agent.py#L5931) | 5931 | `"                        relevance_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L005932](../../agents/web_agent.py#L5932) | 5932 | `"                for item in self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L005933](../../agents/web_agent.py#L5933) | 5933 | `"                    source_text = \" \".join(("` | — |
| [SRC-1AE03B9EC3-L005934](../../agents/web_agent.py#L5934) | 5934 | `"                        item.get(\"title\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005935](../../agents/web_agent.py#L5935) | 5935 | `"                        item.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005936](../../agents/web_agent.py#L5936) | 5936 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L005937](../../agents/web_agent.py#L5937) | 5937 | `"                    if ("` | — |
| [SRC-1AE03B9EC3-L005938](../../agents/web_agent.py#L5938) | 5938 | `"                        relevance_queries"` | — |
| [SRC-1AE03B9EC3-L005939](../../agents/web_agent.py#L5939) | 5939 | `"                        and item[\"url\"] not in existing_urls"` | — |
| [SRC-1AE03B9EC3-L005940](../../agents/web_agent.py#L5940) | 5940 | `"                        and not _blocked_source_url(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L005941](../../agents/web_agent.py#L5941) | 5941 | `"                        and any("` | — |
| [SRC-1AE03B9EC3-L005942](../../agents/web_agent.py#L5942) | 5942 | `"                            _relevance_ratio(candidate_query, source_text) >= 0.20"` | — |
| [SRC-1AE03B9EC3-L005943](../../agents/web_agent.py#L5943) | 5943 | `"                            for candidate_query in relevance_queries"` | — |
| [SRC-1AE03B9EC3-L005944](../../agents/web_agent.py#L5944) | 5944 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005945](../../agents/web_agent.py#L5945) | 5945 | `"                    ):"` | — |
| [SRC-1AE03B9EC3-L005946](../../agents/web_agent.py#L5946) | 5946 | `"                        sources.append(item)"` | — |
| [SRC-1AE03B9EC3-L005947](../../agents/web_agent.py#L5947) | 5947 | `"                        existing_urls.add(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L005948](../../agents/web_agent.py#L5948) | 5948 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005949](../../agents/web_agent.py#L5949) | 5949 | `"                provider_counts = dict(report.get(\"provider_counts\", {}))"` | — |
| [SRC-1AE03B9EC3-L005950](../../agents/web_agent.py#L5950) | 5950 | `"                provider_counts[\"openrouter_web_search\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L005951](../../agents/web_agent.py#L5951) | 5951 | `"                report[\"provider_counts\"] = provider_counts"` | — |
| [SRC-1AE03B9EC3-L005952](../../agents/web_agent.py#L5952) | 5952 | `"                providers_used = list(report.get(\"providers_used\", []))"` | — |
| [SRC-1AE03B9EC3-L005953](../../agents/web_agent.py#L5953) | 5953 | `"                if \"openrouter_web_search\" not in providers_used:"` | — |
| [SRC-1AE03B9EC3-L005954](../../agents/web_agent.py#L5954) | 5954 | `"                    providers_used.append(\"openrouter_web_search\")"` | — |
| [SRC-1AE03B9EC3-L005955](../../agents/web_agent.py#L5955) | 5955 | `"                report[\"providers_used\"] = providers_used"` | — |
| [SRC-1AE03B9EC3-L005956](../../agents/web_agent.py#L5956) | 5956 | `"                report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L005957](../../agents/web_agent.py#L5957) | 5957 | `"                    sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L005958](../../agents/web_agent.py#L5958) | 5958 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005959](../../agents/web_agent.py#L5959) | 5959 | `"        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005960](../../agents/web_agent.py#L5960) | 5960 | `"            llm_warning = str(exc)"` | — |
| [SRC-1AE03B9EC3-L005961](../../agents/web_agent.py#L5961) | 5961 | `"            generation_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L005962](../../agents/web_agent.py#L5962) | 5962 | `"            if generation_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L005963](../../agents/web_agent.py#L5963) | 5963 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005964](../../agents/web_agent.py#L5964) | 5964 | `"                    \"استُنفدت ميزانية محاولات النماذج قبل اكتمال الإجابة التحليلية. \""` | — |
| [SRC-1AE03B9EC3-L005965](../../agents/web_agent.py#L5965) | 5965 | `"                    \"أعرض مقتطفات المصادر المتاحة فقط، ولا أعتبر المهمة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L005966](../../agents/web_agent.py#L5966) | 5966 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005967](../../agents/web_agent.py#L5967) | 5967 | `"            elif not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L005968](../../agents/web_agent.py#L5968) | 5968 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005969](../../agents/web_agent.py#L5969) | 5969 | `"                    \"تم البحث، لكن الفهم التوليدي غير مفعّل بعد. اضبط OPENROUTER_API_KEY \""` | — |
| [SRC-1AE03B9EC3-L005970](../../agents/web_agent.py#L5970) | 5970 | `"                    \"في Termux لتفعيل تخطيط البحث والإجابة باللغة الطبيعية.\""` | — |
| [SRC-1AE03B9EC3-L005971](../../agents/web_agent.py#L5971) | 5971 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005972](../../agents/web_agent.py#L5972) | 5972 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005973](../../agents/web_agent.py#L5973) | 5973 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005974](../../agents/web_agent.py#L5974) | 5974 | `"                    \"اكتمل البحث، لكن تعذر توليد إجابة تحليلية. أعرض لك مقتطفات المصادر \""` | — |
| [SRC-1AE03B9EC3-L005975](../../agents/web_agent.py#L5975) | 5975 | `"                    \"المتاحة بدلًا من اختلاق إجابة.\""` | — |
| [SRC-1AE03B9EC3-L005976](../../agents/web_agent.py#L5976) | 5976 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005977](../../agents/web_agent.py#L5977) | 5977 | `"            answer = _fallback_answer(sources, reason)"` | — |
| [SRC-1AE03B9EC3-L005978](../../agents/web_agent.py#L5978) | 5978 | `""` | — |
| [SRC-1AE03B9EC3-L005979](../../agents/web_agent.py#L5979) | 5979 | `"        coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L005980](../../agents/web_agent.py#L5980) | 5980 | `"        coverage_repair_status = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L005981](../../agents/web_agent.py#L5981) | 5981 | `"        coverage_repair_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005982](../../agents/web_agent.py#L5982) | 5982 | `"        review_status = \"not_run\""` | — |
| [SRC-1AE03B9EC3-L005983](../../agents/web_agent.py#L5983) | 5983 | `"        review_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005984](../../agents/web_agent.py#L5984) | 5984 | `"        review_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L005985](../../agents/web_agent.py#L5985) | 5985 | `"        if used_llm and sources:"` | — |
| [SRC-1AE03B9EC3-L005986](../../agents/web_agent.py#L5986) | 5986 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L005987](../../agents/web_agent.py#L5987) | 5987 | `"                answer = self._review_answer(working_question, answer, sources[:MAX_LLM_CITED_SOURCES])"` | — |
| [SRC-1AE03B9EC3-L005988](../../agents/web_agent.py#L5988) | 5988 | `"                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005989](../../agents/web_agent.py#L5989) | 5989 | `"            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005990](../../agents/web_agent.py#L5990) | 5990 | `"                review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005991](../../agents/web_agent.py#L5991) | 5991 | `"                review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L005992](../../agents/web_agent.py#L5992) | 5992 | `"                review_warning = ("` | — |
| [SRC-1AE03B9EC3-L005993](../../agents/web_agent.py#L5993) | 5993 | `"                    \"استُنفدت ميزانية النماذج قبل اكتمال تدقيق الإجابة؛ لذلك لن أعرض المسودة \""` | — |
| [SRC-1AE03B9EC3-L005994](../../agents/web_agent.py#L5994) | 5994 | `"                    \"بوصفها إجابة مكتملة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد عليها.\""` | — |
| [SRC-1AE03B9EC3-L005995](../../agents/web_agent.py#L5995) | 5995 | `"                    if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L005996](../../agents/web_agent.py#L5996) | 5996 | `"                    else"` | — |
| [SRC-1AE03B9EC3-L005997](../../agents/web_agent.py#L5997) | 5997 | `"                    \"تعذر تدقيق الادعاءات مقابل نصوص المصادر؛ لذلك لن أتعامل مع المسودة \""` | — |
| [SRC-1AE03B9EC3-L005998](../../agents/web_agent.py#L5998) | 5998 | `"                    \"كإجابة مؤكدة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد على المسودة.\""` | — |
| [SRC-1AE03B9EC3-L005999](../../agents/web_agent.py#L5999) | 5999 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006000](../../agents/web_agent.py#L6000) | 6000 | `"                answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L006001](../../agents/web_agent.py#L6001) | 6001 | `"        criterion_gap_research: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L006002](../../agents/web_agent.py#L6002) | 6002 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L006003](../../agents/web_agent.py#L6003) | 6003 | `"            \"status\": \"not_needed\","` | — |
| [SRC-1AE03B9EC3-L006004](../../agents/web_agent.py#L6004) | 6004 | `"            \"targets\": [],"` | — |
| [SRC-1AE03B9EC3-L006005](../../agents/web_agent.py#L6005) | 6005 | `"            \"new_sources_added\": 0,"` | — |
| [SRC-1AE03B9EC3-L006006](../../agents/web_agent.py#L6006) | 6006 | `"            \"evidence_sources_enriched\": 0,"` | — |
| [SRC-1AE03B9EC3-L006007](../../agents/web_agent.py#L6007) | 6007 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006008](../../agents/web_agent.py#L6008) | 6008 | `"        # Close the loop from an answer-stage gap back to the source layer. A criterion"` | — |
| [SRC-1AE03B9EC3-L006009](../../agents/web_agent.py#L6009) | 6009 | `"        # that appears in the draft but has no source signal triggers one bounded query"` | — |
| [SRC-1AE03B9EC3-L006010](../../agents/web_agent.py#L6010) | 6010 | `"        # when the reserved request-budget slot remains available."` | — |
| [SRC-1AE03B9EC3-L006011](../../agents/web_agent.py#L6011) | 6011 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L006012](../../agents/web_agent.py#L6012) | 6012 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L006013](../../agents/web_agent.py#L6013) | 6013 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006014](../../agents/web_agent.py#L6014) | 6014 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L006015](../../agents/web_agent.py#L6015) | 6015 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L006016](../../agents/web_agent.py#L6016) | 6016 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006017](../../agents/web_agent.py#L6017) | 6017 | `"            presearch_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets, plan.get(\"requirement_queries\"))"` | — |
| [SRC-1AE03B9EC3-L006018](../../agents/web_agent.py#L6018) | 6018 | `"            source_gap_targets = ["` | — |
| [SRC-1AE03B9EC3-L006019](../../agents/web_agent.py#L6019) | 6019 | `"                item[\"target\"]"` | — |
| [SRC-1AE03B9EC3-L006020](../../agents/web_agent.py#L6020) | 6020 | `"                for item in presearch_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L006021](../../agents/web_agent.py#L6021) | 6021 | `"                if item.get(\"source_evidence_status\") == \"no_source_lexical_signal\""` | — |
| [SRC-1AE03B9EC3-L006022](../../agents/web_agent.py#L6022) | 6022 | `"            ][:3]"` | — |
| [SRC-1AE03B9EC3-L006023](../../agents/web_agent.py#L6023) | 6023 | `"            if source_gap_targets:"` | — |
