# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **012**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L005166 إلى SRC-EEF2E6447C-L000009
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L005166](../../agents/web_agent.py#L5166) | 5166 | `"        if previous_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L005167](../../agents/web_agent.py#L5167) | 5167 | `"            if provider_attempt_observed or search_attempted is True:"` | — |
| [SRC-1AE03B9EC3-L005168](../../agents/web_agent.py#L5168) | 5168 | `"                search_outcome = \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L005169](../../agents/web_agent.py#L5169) | 5169 | `"            elif search_attempted is False:"` | — |
| [SRC-1AE03B9EC3-L005170](../../agents/web_agent.py#L5170) | 5170 | `"                search_outcome = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L005171](../../agents/web_agent.py#L5171) | 5171 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005172](../../agents/web_agent.py#L5172) | 5172 | `"                search_outcome = \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L005173](../../agents/web_agent.py#L5173) | 5173 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005174](../../agents/web_agent.py#L5174) | 5174 | `"            search_outcome = ("` | — |
| [SRC-1AE03B9EC3-L005175](../../agents/web_agent.py#L5175) | 5175 | `"                \"attempted_with_usable_sources\" if search_attempted is True and sources"` | — |
| [SRC-1AE03B9EC3-L005176](../../agents/web_agent.py#L5176) | 5176 | `"                else \"attempted_no_usable_sources\" if search_attempted is True"` | — |
| [SRC-1AE03B9EC3-L005177](../../agents/web_agent.py#L5177) | 5177 | `"                else \"not_attempted\" if search_attempted is False"` | — |
| [SRC-1AE03B9EC3-L005178](../../agents/web_agent.py#L5178) | 5178 | `"                else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L005179](../../agents/web_agent.py#L5179) | 5179 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005180](../../agents/web_agent.py#L5180) | 5180 | `"        report[\"search_outcome\"] = search_outcome"` | — |
| [SRC-1AE03B9EC3-L005181](../../agents/web_agent.py#L5181) | 5181 | `"        if search_outcome in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L005182](../../agents/web_agent.py#L5182) | 5182 | `"            report[\"usable_sources_after_filtering\"] = None"` | — |
| [SRC-1AE03B9EC3-L005183](../../agents/web_agent.py#L5183) | 5183 | `"            report[\"unique_sources\"] = None"` | — |
| [SRC-1AE03B9EC3-L005184](../../agents/web_agent.py#L5184) | 5184 | `"            report[\"pages_fetched\"] = None"` | — |
| [SRC-1AE03B9EC3-L005185](../../agents/web_agent.py#L5185) | 5185 | `"            report[\"provider_counts\"] = None"` | — |
| [SRC-1AE03B9EC3-L005186](../../agents/web_agent.py#L5186) | 5186 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005187](../../agents/web_agent.py#L5187) | 5187 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005188](../../agents/web_agent.py#L5188) | 5188 | `"            if report.get(\"unique_sources\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L005189](../../agents/web_agent.py#L5189) | 5189 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005190](../../agents/web_agent.py#L5190) | 5190 | `"            if report.get(\"pages_fetched\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L005191](../../agents/web_agent.py#L5191) | 5191 | `"                report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005192](../../agents/web_agent.py#L5192) | 5192 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L005193](../../agents/web_agent.py#L5193) | 5193 | `"        report[\"distinct_registrable_domains\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L005194](../../agents/web_agent.py#L5194) | 5194 | `"        report[\"independent_sources\"] = len(independent_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L005195](../../agents/web_agent.py#L5195) | 5195 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005196](../../agents/web_agent.py#L5196) | 5196 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L005197](../../agents/web_agent.py#L5197) | 5197 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005198](../../agents/web_agent.py#L5198) | 5198 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005199](../../agents/web_agent.py#L5199) | 5199 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L005200](../../agents/web_agent.py#L5200) | 5200 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005201](../../agents/web_agent.py#L5201) | 5201 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L005202](../../agents/web_agent.py#L5202) | 5202 | `"        if len(independent_domains) >= 2:"` | — |
| [SRC-1AE03B9EC3-L005203](../../agents/web_agent.py#L5203) | 5203 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005204](../../agents/web_agent.py#L5204) | 5204 | `"                \"تعدد النطاقات المسجلة لا يثبت الاستقلال التحريري؛ قد تنقل المواقع عن المصدر الأصلي نفسه.\""` | — |
| [SRC-1AE03B9EC3-L005205](../../agents/web_agent.py#L5205) | 5205 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005206](../../agents/web_agent.py#L5206) | 5206 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L005207](../../agents/web_agent.py#L5207) | 5207 | `"        if needs_corroboration and single_source_navigation and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005208](../../agents/web_agent.py#L5208) | 5208 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005209](../../agents/web_agent.py#L5209) | 5209 | `"                \"هذه نتيجة مرشحة لطلب العثور على موقع/رابط؛ لم تُثبت رسميتها أو صحتها \""` | — |
| [SRC-1AE03B9EC3-L005210](../../agents/web_agent.py#L5210) | 5210 | `"                \"من مصدر مستقل، لذا راجع الرابط قبل الاعتماد عليه.\""` | — |
| [SRC-1AE03B9EC3-L005211](../../agents/web_agent.py#L5211) | 5211 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005212](../../agents/web_agent.py#L5212) | 5212 | `"        if needs_corroboration and (single_source_social or single_source_lead) and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005213](../../agents/web_agent.py#L5213) | 5213 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005214](../../agents/web_agent.py#L5214) | 5214 | `"                \"هذه إشارات بحث أولية وليست تحققًا مستقلًا من هوية العميل أو نيته؛ \""` | — |
| [SRC-1AE03B9EC3-L005215](../../agents/web_agent.py#L5215) | 5215 | `"                \"راجع المنشور وتاريخه وسياقه قبل التواصل أو اتخاذ قرار.\""` | — |
| [SRC-1AE03B9EC3-L005216](../../agents/web_agent.py#L5216) | 5216 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005217](../../agents/web_agent.py#L5217) | 5217 | `"        if needs_corroboration and single_source_listing and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005218](../../agents/web_agent.py#L5218) | 5218 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005219](../../agents/web_agent.py#L5219) | 5219 | `"                \"هذه إعلانات/قوائم مرشحة فقط. قد تكون منتهية أو غير دقيقة؛ تحقق من السعر \""` | — |
| [SRC-1AE03B9EC3-L005220](../../agents/web_agent.py#L5220) | 5220 | `"                \"والتوافر ومصدر الإعلان واطلب تأكيدًا حديثًا قبل دفع مال أو مشاركة بيانات.\""` | — |
| [SRC-1AE03B9EC3-L005221](../../agents/web_agent.py#L5221) | 5221 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005222](../../agents/web_agent.py#L5222) | 5222 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L005223](../../agents/web_agent.py#L5223) | 5223 | `"        if needs_corroboration and not task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L005224](../../agents/web_agent.py#L5224) | 5224 | `"            if search_outcome == \"unknown_after_research_error\":"` | — |
| [SRC-1AE03B9EC3-L005225](../../agents/web_agent.py#L5225) | 5225 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005226](../../agents/web_agent.py#L5226) | 5226 | `"                    \"تعذر إكمال مسار البحث بسبب خطأ، ولا توجد بيانات كافية لتحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L005227](../../agents/web_agent.py#L5227) | 5227 | `"                    \"كانت محاولة البحث قد اكتملت أو كم نتيجة جُمعت. لذلك لا أستطيع الجزم \""` | — |
| [SRC-1AE03B9EC3-L005228](../../agents/web_agent.py#L5228) | 5228 | `"                    \"بأن البحث لم يُنفّذ أو أن الإنترنت لم يُعد نتائج. لم أتمكن من تقديم \""` | — |
| [SRC-1AE03B9EC3-L005229](../../agents/web_agent.py#L5229) | 5229 | `"                    \"إجابة مكتملة؛ أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005230](../../agents/web_agent.py#L5230) | 5230 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005231](../../agents/web_agent.py#L5231) | 5231 | `"            elif search_outcome == \"attempted_research_error\":"` | — |
| [SRC-1AE03B9EC3-L005232](../../agents/web_agent.py#L5232) | 5232 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005233](../../agents/web_agent.py#L5233) | 5233 | `"                    \"توجد قرائن تشغيلية على بدء محاولة بحث، لكن مسار البحث فشل قبل إنتاج \""` | — |
| [SRC-1AE03B9EC3-L005234](../../agents/web_agent.py#L5234) | 5234 | `"                    \"تقرير مكتمل. لا أستطيع تحديد عدد النتائج أو المصادر القابلة للاستخدام، \""` | — |
| [SRC-1AE03B9EC3-L005235](../../agents/web_agent.py#L5235) | 5235 | `"                    \"لذلك لن أخمّن. أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005236](../../agents/web_agent.py#L5236) | 5236 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005237](../../agents/web_agent.py#L5237) | 5237 | `"            elif search_outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-1AE03B9EC3-L005238](../../agents/web_agent.py#L5238) | 5238 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005239](../../agents/web_agent.py#L5239) | 5239 | `"                    \"جرت محاولة البحث، لكن لم تتوفر مصادر صالحة وكافية للإجابة بعد تصفية \""` | — |
| [SRC-1AE03B9EC3-L005240](../../agents/web_agent.py#L5240) | 5240 | `"                    \"النتائج. هذا لا يثبت أن جميع المواقع أو الإنترنت غير متاح؛ لن أخمّن \""` | — |
| [SRC-1AE03B9EC3-L005241](../../agents/web_agent.py#L5241) | 5241 | `"                    \"أو أقدّم نتيجة غير مدعومة. جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005242](../../agents/web_agent.py#L5242) | 5242 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005243](../../agents/web_agent.py#L5243) | 5243 | `"            elif search_outcome == \"not_attempted\":"` | — |
| [SRC-1AE03B9EC3-L005244](../../agents/web_agent.py#L5244) | 5244 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005245](../../agents/web_agent.py#L5245) | 5245 | `"                    \"لم تبدأ محاولة بحث ويب لهذا الطلب، لذلك لا تتوفر لدي أدلة ويب حالية \""` | — |
| [SRC-1AE03B9EC3-L005246](../../agents/web_agent.py#L5246) | 5246 | `"                    \"كافية للإجابة. لن أقدّم نتيجة غير مدعومة؛ أعد المحاولة أو اطلب بحثًا \""` | — |
| [SRC-1AE03B9EC3-L005247](../../agents/web_agent.py#L5247) | 5247 | `"                    \"صريحًا إذا كان ذلك مناسبًا.\""` | — |
| [SRC-1AE03B9EC3-L005248](../../agents/web_agent.py#L5248) | 5248 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005249](../../agents/web_agent.py#L5249) | 5249 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005250](../../agents/web_agent.py#L5250) | 5250 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005251](../../agents/web_agent.py#L5251) | 5251 | `"                    \"لم أجد معلومات موثوقة كافية مرتبطة بسؤالك من نطاقين مسجلين مختلفين على الأقل. \""` | — |
| [SRC-1AE03B9EC3-L005252](../../agents/web_agent.py#L5252) | 5252 | `"                    \"اختلاف النطاقات لا يثبت الاستقلال التحريري. لن أخمّن أو أقدّم نتيجة غير مدعومة؛ \""` | — |
| [SRC-1AE03B9EC3-L005253](../../agents/web_agent.py#L5253) | 5253 | `"                    \"جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005254](../../agents/web_agent.py#L5254) | 5254 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005255](../../agents/web_agent.py#L5255) | 5255 | `"            public_sources = [{"` | — |
| [SRC-1AE03B9EC3-L005256](../../agents/web_agent.py#L5256) | 5256 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L005257](../../agents/web_agent.py#L5257) | 5257 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L005258](../../agents/web_agent.py#L5258) | 5258 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005259](../../agents/web_agent.py#L5259) | 5259 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005260](../../agents/web_agent.py#L5260) | 5260 | `"                \"page_fetch_status\": source.get(\"page_fetch_status\", \"unknown\"),"` | — |
| [SRC-1AE03B9EC3-L005261](../../agents/web_agent.py#L5261) | 5261 | `"                \"page_fetch_error_class\": source.get(\"page_fetch_error_class\"),"` | — |
| [SRC-1AE03B9EC3-L005262](../../agents/web_agent.py#L5262) | 5262 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L005263](../../agents/web_agent.py#L5263) | 5263 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005264](../../agents/web_agent.py#L5264) | 5264 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L005265](../../agents/web_agent.py#L5265) | 5265 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005266](../../agents/web_agent.py#L5266) | 5266 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L005267](../../agents/web_agent.py#L5267) | 5267 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005268](../../agents/web_agent.py#L5268) | 5268 | `"                \"opinion_source_classification\": source.get(\"opinion_source_classification\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005269](../../agents/web_agent.py#L5269) | 5269 | `"                \"opinion_classification_basis\": source.get(\"opinion_classification_basis\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005270](../../agents/web_agent.py#L5270) | 5270 | `"                \"opinion_classification_method\": source.get(\"opinion_classification_method\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005271](../../agents/web_agent.py#L5271) | 5271 | `"                \"current_evidence_assessment\": source.get(\"current_evidence_assessment\", {}),"` | — |
| [SRC-1AE03B9EC3-L005272](../../agents/web_agent.py#L5272) | 5272 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005273](../../agents/web_agent.py#L5273) | 5273 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005274](../../agents/web_agent.py#L5274) | 5274 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L005275](../../agents/web_agent.py#L5275) | 5275 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L005276](../../agents/web_agent.py#L5276) | 5276 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L005277](../../agents/web_agent.py#L5277) | 5277 | `"            } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L005278](../../agents/web_agent.py#L5278) | 5278 | `"            citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L005279](../../agents/web_agent.py#L5279) | 5279 | `"                reason, 0, [], \"not_run\""` | — |
| [SRC-1AE03B9EC3-L005280](../../agents/web_agent.py#L5280) | 5280 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005281](../../agents/web_agent.py#L5281) | 5281 | `"            citation_validation[\"status\"] = \"not_applicable_no_generated_answer\""` | — |
| [SRC-1AE03B9EC3-L005282](../../agents/web_agent.py#L5282) | 5282 | `"            coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L005283](../../agents/web_agent.py#L5283) | 5283 | `"            answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L005284](../../agents/web_agent.py#L5284) | 5284 | `"                \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L005285](../../agents/web_agent.py#L5285) | 5285 | `"                \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L005286](../../agents/web_agent.py#L5286) | 5286 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L005287](../../agents/web_agent.py#L5287) | 5287 | `"                    \"not_reviewed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L005288](../../agents/web_agent.py#L5288) | 5288 | `"                    if coverage_targets else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005289](../../agents/web_agent.py#L5289) | 5289 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005290](../../agents/web_agent.py#L5290) | 5290 | `"                \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L005291](../../agents/web_agent.py#L5291) | 5291 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005292](../../agents/web_agent.py#L5292) | 5292 | `"            answer_integrity = audit_answer_integrity(working_question, reason, sources, coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L005293](../../agents/web_agent.py#L5293) | 5293 | `"            answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005294](../../agents/web_agent.py#L5294) | 5294 | `"            answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L005295](../../agents/web_agent.py#L5295) | 5295 | `"            answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L005296](../../agents/web_agent.py#L5296) | 5296 | `"            answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L005297](../../agents/web_agent.py#L5297) | 5297 | `"            task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L005298](../../agents/web_agent.py#L5298) | 5298 | `"                \"not_assessed_insufficient_evidence\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005299](../../agents/web_agent.py#L5299) | 5299 | `"                else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005300](../../agents/web_agent.py#L5300) | 5300 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005301](../../agents/web_agent.py#L5301) | 5301 | `"            answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L005302](../../agents/web_agent.py#L5302) | 5302 | `"            research_failed = search_outcome in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L005303](../../agents/web_agent.py#L5303) | 5303 | `"            report.update({"` | — |
| [SRC-1AE03B9EC3-L005304](../../agents/web_agent.py#L5304) | 5304 | `"                # When collection failed, an empty local list is not evidence that"` | — |
| [SRC-1AE03B9EC3-L005305](../../agents/web_agent.py#L5305) | 5305 | `"                # the remote search returned zero sources; preserve unknown counts."` | — |
| [SRC-1AE03B9EC3-L005306](../../agents/web_agent.py#L5306) | 5306 | `"                \"unique_sources\": None if research_failed else len(sources),"` | — |
| [SRC-1AE03B9EC3-L005307](../../agents/web_agent.py#L5307) | 5307 | `"                \"independent_sources\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L005308](../../agents/web_agent.py#L5308) | 5308 | `"                \"distinct_registrable_domains\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L005309](../../agents/web_agent.py#L5309) | 5309 | `"                \"pages_fetched\": ("` | — |
| [SRC-1AE03B9EC3-L005310](../../agents/web_agent.py#L5310) | 5310 | `"                    None if research_failed"` | — |
| [SRC-1AE03B9EC3-L005311](../../agents/web_agent.py#L5311) | 5311 | `"                    else sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005312](../../agents/web_agent.py#L5312) | 5312 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005313](../../agents/web_agent.py#L5313) | 5313 | `"                \"provider_diagnostics\": current_research_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L005314](../../agents/web_agent.py#L5314) | 5314 | `"                \"insufficient_evidence\": True,"` | — |
| [SRC-1AE03B9EC3-L005315](../../agents/web_agent.py#L5315) | 5315 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L005316](../../agents/web_agent.py#L5316) | 5316 | `"                \"citation_check\": citation_validation[\"status\"],"` | — |
| [SRC-1AE03B9EC3-L005317](../../agents/web_agent.py#L5317) | 5317 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L005318](../../agents/web_agent.py#L5318) | 5318 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L005319](../../agents/web_agent.py#L5319) | 5319 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L005320](../../agents/web_agent.py#L5320) | 5320 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L005321](../../agents/web_agent.py#L5321) | 5321 | `"                \"connector_summary\": report.get(\"connector_summary\") or self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L005322](../../agents/web_agent.py#L5322) | 5322 | `"                    current_research_diagnostics, sources"` | — |
| [SRC-1AE03B9EC3-L005323](../../agents/web_agent.py#L5323) | 5323 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005324](../../agents/web_agent.py#L5324) | 5324 | `"            })"` | — |
| [SRC-1AE03B9EC3-L005325](../../agents/web_agent.py#L5325) | 5325 | `"            return {"` | — |
| [SRC-1AE03B9EC3-L005326](../../agents/web_agent.py#L5326) | 5326 | `"                \"answer\": reason,"` | — |
| [SRC-1AE03B9EC3-L005327](../../agents/web_agent.py#L5327) | 5327 | `"                \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L005328](../../agents/web_agent.py#L5328) | 5328 | `"                \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L005329](../../agents/web_agent.py#L5329) | 5329 | `"                \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005330](../../agents/web_agent.py#L5330) | 5330 | `"                \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L005331](../../agents/web_agent.py#L5331) | 5331 | `"                    \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L005332](../../agents/web_agent.py#L5332) | 5332 | `"                    \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L005333](../../agents/web_agent.py#L5333) | 5333 | `"                    \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L005334](../../agents/web_agent.py#L5334) | 5334 | `"                    \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L005335](../../agents/web_agent.py#L5335) | 5335 | `"                    \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L005336](../../agents/web_agent.py#L5336) | 5336 | `"                    \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L005337](../../agents/web_agent.py#L5337) | 5337 | `"                    \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L005338](../../agents/web_agent.py#L5338) | 5338 | `"                    \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L005339](../../agents/web_agent.py#L5339) | 5339 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005340](../../agents/web_agent.py#L5340) | 5340 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005341](../../agents/web_agent.py#L5341) | 5341 | `"                },"` | — |
| [SRC-1AE03B9EC3-L005342](../../agents/web_agent.py#L5342) | 5342 | `"                \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L005343](../../agents/web_agent.py#L5343) | 5343 | `"                \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L005344](../../agents/web_agent.py#L5344) | 5344 | `"                \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L005345](../../agents/web_agent.py#L5345) | 5345 | `"                \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L005346](../../agents/web_agent.py#L5346) | 5346 | `"                \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L005347](../../agents/web_agent.py#L5347) | 5347 | `"                \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L005348](../../agents/web_agent.py#L5348) | 5348 | `"                \"warnings\": list(dict.fromkeys(search_warnings + [reason])),"` | — |
| [SRC-1AE03B9EC3-L005349](../../agents/web_agent.py#L5349) | 5349 | `"                \"kind\": \"insufficient_evidence\","` | — |
| [SRC-1AE03B9EC3-L005350](../../agents/web_agent.py#L5350) | 5350 | `"                \"final_answer_status\": \"insufficient_evidence_no_generation\","` | — |
| [SRC-1AE03B9EC3-L005351](../../agents/web_agent.py#L5351) | 5351 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005352](../../agents/web_agent.py#L5352) | 5352 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005353](../../agents/web_agent.py#L5353) | 5353 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L005354](../../agents/web_agent.py#L5354) | 5354 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L005355](../../agents/web_agent.py#L5355) | 5355 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L005356](../../agents/web_agent.py#L5356) | 5356 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L005357](../../agents/web_agent.py#L5357) | 5357 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L005358](../../agents/web_agent.py#L5358) | 5358 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005359](../../agents/web_agent.py#L5359) | 5359 | `""` | — |
| [SRC-1AE03B9EC3-L005360](../../agents/web_agent.py#L5360) | 5360 | `"        answer = \"\""` | — |
| [SRC-1AE03B9EC3-L005361](../../agents/web_agent.py#L5361) | 5361 | `"        used_llm = False"` | — |
| [SRC-1AE03B9EC3-L005362](../../agents/web_agent.py#L5362) | 5362 | `"        llm_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005363](../../agents/web_agent.py#L5363) | 5363 | `"        generation_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L005364](../../agents/web_agent.py#L5364) | 5364 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L005365](../../agents/web_agent.py#L5365) | 5365 | `"            answer = self._generate("` | — |
| [SRC-1AE03B9EC3-L005366](../../agents/web_agent.py#L5366) | 5366 | `"                working_question,"` | — |
| [SRC-1AE03B9EC3-L005367](../../agents/web_agent.py#L5367) | 5367 | `"                clean_history,"` | — |
| [SRC-1AE03B9EC3-L005368](../../agents/web_agent.py#L5368) | 5368 | `"                sources,"` | — |
| [SRC-1AE03B9EC3-L005369](../../agents/web_agent.py#L5369) | 5369 | `"                search_warning,"` | — |
| [SRC-1AE03B9EC3-L005370](../../agents/web_agent.py#L5370) | 5370 | `"                research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L005371](../../agents/web_agent.py#L5371) | 5371 | `"                search_report=report,"` | — |
| [SRC-1AE03B9EC3-L005372](../../agents/web_agent.py#L5372) | 5372 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005373](../../agents/web_agent.py#L5373) | 5373 | `"            used_llm = True"` | — |
| [SRC-1AE03B9EC3-L005374](../../agents/web_agent.py#L5374) | 5374 | `"            if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L005375](../../agents/web_agent.py#L5375) | 5375 | `"                existing_urls = {item.get(\"url\") for item in sources}"` | — |
| [SRC-1AE03B9EC3-L005376](../../agents/web_agent.py#L5376) | 5376 | `"                relevance_queries = []"` | — |
| [SRC-1AE03B9EC3-L005377](../../agents/web_agent.py#L5377) | 5377 | `"                planned_queries = plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005378](../../agents/web_agent.py#L5378) | 5378 | `"                if not isinstance(planned_queries, list):"` | — |
| [SRC-1AE03B9EC3-L005379](../../agents/web_agent.py#L5379) | 5379 | `"                    planned_queries = []"` | — |
| [SRC-1AE03B9EC3-L005380](../../agents/web_agent.py#L5380) | 5380 | `"                for candidate_query in [working_question, *planned_queries]:"` | — |
| [SRC-1AE03B9EC3-L005381](../../agents/web_agent.py#L5381) | 5381 | `"                    if not isinstance(candidate_query, str):"` | — |
| [SRC-1AE03B9EC3-L005382](../../agents/web_agent.py#L5382) | 5382 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L005383](../../agents/web_agent.py#L5383) | 5383 | `"                    compacted_query = compact_search_query(candidate_query)"` | — |
| [SRC-1AE03B9EC3-L005384](../../agents/web_agent.py#L5384) | 5384 | `"                    if compacted_query and compacted_query not in relevance_queries:"` | — |
| [SRC-1AE03B9EC3-L005385](../../agents/web_agent.py#L5385) | 5385 | `"                        relevance_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L005386](../../agents/web_agent.py#L5386) | 5386 | `"                for item in self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L005387](../../agents/web_agent.py#L5387) | 5387 | `"                    source_text = \" \".join(("` | — |
| [SRC-1AE03B9EC3-L005388](../../agents/web_agent.py#L5388) | 5388 | `"                        item.get(\"title\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005389](../../agents/web_agent.py#L5389) | 5389 | `"                        item.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005390](../../agents/web_agent.py#L5390) | 5390 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L005391](../../agents/web_agent.py#L5391) | 5391 | `"                    if ("` | — |
| [SRC-1AE03B9EC3-L005392](../../agents/web_agent.py#L5392) | 5392 | `"                        relevance_queries"` | — |
| [SRC-1AE03B9EC3-L005393](../../agents/web_agent.py#L5393) | 5393 | `"                        and item[\"url\"] not in existing_urls"` | — |
| [SRC-1AE03B9EC3-L005394](../../agents/web_agent.py#L5394) | 5394 | `"                        and not _blocked_source_url(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L005395](../../agents/web_agent.py#L5395) | 5395 | `"                        and any("` | — |
| [SRC-1AE03B9EC3-L005396](../../agents/web_agent.py#L5396) | 5396 | `"                            _relevance_ratio(candidate_query, source_text) >= 0.20"` | — |
| [SRC-1AE03B9EC3-L005397](../../agents/web_agent.py#L5397) | 5397 | `"                            for candidate_query in relevance_queries"` | — |
| [SRC-1AE03B9EC3-L005398](../../agents/web_agent.py#L5398) | 5398 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005399](../../agents/web_agent.py#L5399) | 5399 | `"                    ):"` | — |
| [SRC-1AE03B9EC3-L005400](../../agents/web_agent.py#L5400) | 5400 | `"                        sources.append(item)"` | — |
| [SRC-1AE03B9EC3-L005401](../../agents/web_agent.py#L5401) | 5401 | `"                        existing_urls.add(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L005402](../../agents/web_agent.py#L5402) | 5402 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005403](../../agents/web_agent.py#L5403) | 5403 | `"                provider_counts = dict(report.get(\"provider_counts\", {}))"` | — |
| [SRC-1AE03B9EC3-L005404](../../agents/web_agent.py#L5404) | 5404 | `"                provider_counts[\"openrouter_web_search\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L005405](../../agents/web_agent.py#L5405) | 5405 | `"                report[\"provider_counts\"] = provider_counts"` | — |
| [SRC-1AE03B9EC3-L005406](../../agents/web_agent.py#L5406) | 5406 | `"                providers_used = list(report.get(\"providers_used\", []))"` | — |
| [SRC-1AE03B9EC3-L005407](../../agents/web_agent.py#L5407) | 5407 | `"                if \"openrouter_web_search\" not in providers_used:"` | — |
| [SRC-1AE03B9EC3-L005408](../../agents/web_agent.py#L5408) | 5408 | `"                    providers_used.append(\"openrouter_web_search\")"` | — |
| [SRC-1AE03B9EC3-L005409](../../agents/web_agent.py#L5409) | 5409 | `"                report[\"providers_used\"] = providers_used"` | — |
| [SRC-1AE03B9EC3-L005410](../../agents/web_agent.py#L5410) | 5410 | `"                report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L005411](../../agents/web_agent.py#L5411) | 5411 | `"                    sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L005412](../../agents/web_agent.py#L5412) | 5412 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005413](../../agents/web_agent.py#L5413) | 5413 | `"        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005414](../../agents/web_agent.py#L5414) | 5414 | `"            llm_warning = str(exc)"` | — |
| [SRC-1AE03B9EC3-L005415](../../agents/web_agent.py#L5415) | 5415 | `"            generation_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L005416](../../agents/web_agent.py#L5416) | 5416 | `"            if generation_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L005417](../../agents/web_agent.py#L5417) | 5417 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005418](../../agents/web_agent.py#L5418) | 5418 | `"                    \"استُنفدت ميزانية محاولات النماذج قبل اكتمال الإجابة التحليلية. \""` | — |
| [SRC-1AE03B9EC3-L005419](../../agents/web_agent.py#L5419) | 5419 | `"                    \"أعرض مقتطفات المصادر المتاحة فقط، ولا أعتبر المهمة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L005420](../../agents/web_agent.py#L5420) | 5420 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005421](../../agents/web_agent.py#L5421) | 5421 | `"            elif not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L005422](../../agents/web_agent.py#L5422) | 5422 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005423](../../agents/web_agent.py#L5423) | 5423 | `"                    \"تم البحث، لكن الفهم التوليدي غير مفعّل بعد. اضبط OPENROUTER_API_KEY \""` | — |
| [SRC-1AE03B9EC3-L005424](../../agents/web_agent.py#L5424) | 5424 | `"                    \"في Termux لتفعيل تخطيط البحث والإجابة باللغة الطبيعية.\""` | — |
| [SRC-1AE03B9EC3-L005425](../../agents/web_agent.py#L5425) | 5425 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005426](../../agents/web_agent.py#L5426) | 5426 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005427](../../agents/web_agent.py#L5427) | 5427 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005428](../../agents/web_agent.py#L5428) | 5428 | `"                    \"اكتمل البحث، لكن تعذر توليد إجابة تحليلية. أعرض لك مقتطفات المصادر \""` | — |
| [SRC-1AE03B9EC3-L005429](../../agents/web_agent.py#L5429) | 5429 | `"                    \"المتاحة بدلًا من اختلاق إجابة.\""` | — |
| [SRC-1AE03B9EC3-L005430](../../agents/web_agent.py#L5430) | 5430 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005431](../../agents/web_agent.py#L5431) | 5431 | `"            answer = _fallback_answer(sources, reason)"` | — |
| [SRC-1AE03B9EC3-L005432](../../agents/web_agent.py#L5432) | 5432 | `""` | — |
| [SRC-1AE03B9EC3-L005433](../../agents/web_agent.py#L5433) | 5433 | `"        coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L005434](../../agents/web_agent.py#L5434) | 5434 | `"        coverage_repair_status = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L005435](../../agents/web_agent.py#L5435) | 5435 | `"        coverage_repair_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005436](../../agents/web_agent.py#L5436) | 5436 | `"        review_status = \"not_run\""` | — |
| [SRC-1AE03B9EC3-L005437](../../agents/web_agent.py#L5437) | 5437 | `"        review_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005438](../../agents/web_agent.py#L5438) | 5438 | `"        review_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L005439](../../agents/web_agent.py#L5439) | 5439 | `"        if used_llm and sources:"` | — |
| [SRC-1AE03B9EC3-L005440](../../agents/web_agent.py#L5440) | 5440 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L005441](../../agents/web_agent.py#L5441) | 5441 | `"                answer = self._review_answer(working_question, answer, sources[:MAX_LLM_CITED_SOURCES])"` | — |
| [SRC-1AE03B9EC3-L005442](../../agents/web_agent.py#L5442) | 5442 | `"                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005443](../../agents/web_agent.py#L5443) | 5443 | `"            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005444](../../agents/web_agent.py#L5444) | 5444 | `"                review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005445](../../agents/web_agent.py#L5445) | 5445 | `"                review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L005446](../../agents/web_agent.py#L5446) | 5446 | `"                review_warning = ("` | — |
| [SRC-1AE03B9EC3-L005447](../../agents/web_agent.py#L5447) | 5447 | `"                    \"استُنفدت ميزانية النماذج قبل اكتمال تدقيق الإجابة؛ لذلك لن أعرض المسودة \""` | — |
| [SRC-1AE03B9EC3-L005448](../../agents/web_agent.py#L5448) | 5448 | `"                    \"بوصفها إجابة مكتملة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد عليها.\""` | — |
| [SRC-1AE03B9EC3-L005449](../../agents/web_agent.py#L5449) | 5449 | `"                    if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L005450](../../agents/web_agent.py#L5450) | 5450 | `"                    else"` | — |
| [SRC-1AE03B9EC3-L005451](../../agents/web_agent.py#L5451) | 5451 | `"                    \"تعذر تدقيق الادعاءات مقابل نصوص المصادر؛ لذلك لن أتعامل مع المسودة \""` | — |
| [SRC-1AE03B9EC3-L005452](../../agents/web_agent.py#L5452) | 5452 | `"                    \"كإجابة مؤكدة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد على المسودة.\""` | — |
| [SRC-1AE03B9EC3-L005453](../../agents/web_agent.py#L5453) | 5453 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005454](../../agents/web_agent.py#L5454) | 5454 | `"                answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L005455](../../agents/web_agent.py#L5455) | 5455 | `"        criterion_gap_research: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L005456](../../agents/web_agent.py#L5456) | 5456 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L005457](../../agents/web_agent.py#L5457) | 5457 | `"            \"status\": \"not_needed\","` | — |
| [SRC-1AE03B9EC3-L005458](../../agents/web_agent.py#L5458) | 5458 | `"            \"targets\": [],"` | — |
| [SRC-1AE03B9EC3-L005459](../../agents/web_agent.py#L5459) | 5459 | `"            \"new_sources_added\": 0,"` | — |
| [SRC-1AE03B9EC3-L005460](../../agents/web_agent.py#L5460) | 5460 | `"            \"evidence_sources_enriched\": 0,"` | — |
| [SRC-1AE03B9EC3-L005461](../../agents/web_agent.py#L5461) | 5461 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005462](../../agents/web_agent.py#L5462) | 5462 | `"        # Close the loop from an answer-stage gap back to the source layer. A criterion"` | — |
| [SRC-1AE03B9EC3-L005463](../../agents/web_agent.py#L5463) | 5463 | `"        # that appears in the draft but has no source signal triggers one bounded query"` | — |
| [SRC-1AE03B9EC3-L005464](../../agents/web_agent.py#L5464) | 5464 | `"        # when the reserved request-budget slot remains available."` | — |
| [SRC-1AE03B9EC3-L005465](../../agents/web_agent.py#L5465) | 5465 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L005466](../../agents/web_agent.py#L5466) | 5466 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005467](../../agents/web_agent.py#L5467) | 5467 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005468](../../agents/web_agent.py#L5468) | 5468 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L005469](../../agents/web_agent.py#L5469) | 5469 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L005470](../../agents/web_agent.py#L5470) | 5470 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L005471](../../agents/web_agent.py#L5471) | 5471 | `"            presearch_integrity = audit_answer_integrity("` | — |
| [SRC-1AE03B9EC3-L005472](../../agents/web_agent.py#L5472) | 5472 | `"                working_question, answer, sources, coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005473](../../agents/web_agent.py#L5473) | 5473 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005474](../../agents/web_agent.py#L5474) | 5474 | `"            source_gap_targets = ["` | — |
| [SRC-1AE03B9EC3-L005475](../../agents/web_agent.py#L5475) | 5475 | `"                item[\"target\"]"` | — |
| [SRC-1AE03B9EC3-L005476](../../agents/web_agent.py#L5476) | 5476 | `"                for item in presearch_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005477](../../agents/web_agent.py#L5477) | 5477 | `"                if item.get(\"source_evidence_status\") == \"no_source_lexical_signal\""` | — |
| [SRC-1AE03B9EC3-L005478](../../agents/web_agent.py#L5478) | 5478 | `"            ][:3]"` | — |
| [SRC-1AE03B9EC3-L005479](../../agents/web_agent.py#L5479) | 5479 | `"            if source_gap_targets:"` | — |
| [SRC-1AE03B9EC3-L005480](../../agents/web_agent.py#L5480) | 5480 | `"                criterion_gap_research[\"targets\"] = source_gap_targets"` | — |
| [SRC-1AE03B9EC3-L005481](../../agents/web_agent.py#L5481) | 5481 | `"                budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L005482](../../agents/web_agent.py#L5482) | 5482 | `"                if not plan.get(\"coverage_gap_repair_slot_reserved\"):"` | — |
| [SRC-1AE03B9EC3-L005483](../../agents/web_agent.py#L5483) | 5483 | `"                    criterion_gap_research[\"status\"] = \"skipped_no_reserved_search_slot\""` | — |
| [SRC-1AE03B9EC3-L005484](../../agents/web_agent.py#L5484) | 5484 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005485](../../agents/web_agent.py#L5485) | 5485 | `"                        \"رُصدت محاور بلا إشارة لفظية في المصادر، لكن لم تُحجز ميزانية \""` | — |
| [SRC-1AE03B9EC3-L005486](../../agents/web_agent.py#L5486) | 5486 | `"                        \"استعلام إضافي لهذه المهمة؛ لذلك ستظل المحاور غير المحسومة ظاهرة.\""` | — |
| [SRC-1AE03B9EC3-L005487](../../agents/web_agent.py#L5487) | 5487 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005488](../../agents/web_agent.py#L5488) | 5488 | `"                elif budget is None:"` | — |
| [SRC-1AE03B9EC3-L005489](../../agents/web_agent.py#L5489) | 5489 | `"                    criterion_gap_research[\"status\"] = \"skipped_no_request_budget\""` | — |
| [SRC-1AE03B9EC3-L005490](../../agents/web_agent.py#L5490) | 5490 | `"                elif budget.remaining_units(\"search_queries\") < 1:"` | — |
| [SRC-1AE03B9EC3-L005491](../../agents/web_agent.py#L5491) | 5491 | `"                    criterion_gap_research[\"status\"] = \"skipped_search_budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L005492](../../agents/web_agent.py#L5492) | 5492 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005493](../../agents/web_agent.py#L5493) | 5493 | `"                        \"رُصدت محاور بلا إشارة لفظية في المصادر، لكن ميزانية البحث لم تترك \""` | — |
| [SRC-1AE03B9EC3-L005494](../../agents/web_agent.py#L5494) | 5494 | `"                        \"استعلامًا إضافيًا للتحقق منها؛ لذلك لا تُعدّ الإجابة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L005495](../../agents/web_agent.py#L5495) | 5495 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005496](../../agents/web_agent.py#L5496) | 5496 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L005497](../../agents/web_agent.py#L5497) | 5497 | `"                    fallback_queries = fallback_plan(working_question, clean_history).get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005498](../../agents/web_agent.py#L5498) | 5498 | `"                    topic_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L005499](../../agents/web_agent.py#L5499) | 5499 | `"                        fallback_queries[0] if fallback_queries else working_question"` | — |
| [SRC-1AE03B9EC3-L005500](../../agents/web_agent.py#L5500) | 5500 | `"                    ) or compact_search_query(working_question)"` | — |
| [SRC-1AE03B9EC3-L005501](../../agents/web_agent.py#L5501) | 5501 | `"                    gap_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L005502](../../agents/web_agent.py#L5502) | 5502 | `"                        f\"{topic_query} {' '.join(source_gap_targets)} official specific evidence data\""` | — |
| [SRC-1AE03B9EC3-L005503](../../agents/web_agent.py#L5503) | 5503 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005504](../../agents/web_agent.py#L5504) | 5504 | `"                    known_query_keys = {"` | — |
| [SRC-1AE03B9EC3-L005505](../../agents/web_agent.py#L5505) | 5505 | `"                        _normalize_search_query(item).casefold()"` | — |
| [SRC-1AE03B9EC3-L005506](../../agents/web_agent.py#L5506) | 5506 | `"                        for item in plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005507](../../agents/web_agent.py#L5507) | 5507 | `"                        if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L005508](../../agents/web_agent.py#L5508) | 5508 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L005509](../../agents/web_agent.py#L5509) | 5509 | `"                    if not gap_query or not _relevance_query_tokens(gap_query):"` | — |
| [SRC-1AE03B9EC3-L005510](../../agents/web_agent.py#L5510) | 5510 | `"                        criterion_gap_research[\"status\"] = \"skipped_no_valid_query\""` | — |
| [SRC-1AE03B9EC3-L005511](../../agents/web_agent.py#L5511) | 5511 | `"                    elif _normalize_search_query(gap_query).casefold() in known_query_keys:"` | — |
| [SRC-1AE03B9EC3-L005512](../../agents/web_agent.py#L5512) | 5512 | `"                        criterion_gap_research[\"status\"] = \"skipped_query_not_distinct\""` | — |
| [SRC-1AE03B9EC3-L005513](../../agents/web_agent.py#L5513) | 5513 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L005514](../../agents/web_agent.py#L5514) | 5514 | `"                        criterion_gap_research.update({"` | — |
| [SRC-1AE03B9EC3-L005515](../../agents/web_agent.py#L5515) | 5515 | `"                            \"attempted\": True,"` | — |
| [SRC-1AE03B9EC3-L005516](../../agents/web_agent.py#L5516) | 5516 | `"                            \"status\": \"searching_for_missing_criterion_evidence\","` | — |
| [SRC-1AE03B9EC3-L005517](../../agents/web_agent.py#L5517) | 5517 | `"                            \"query\": gap_query,"` | — |
| [SRC-1AE03B9EC3-L005518](../../agents/web_agent.py#L5518) | 5518 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L005519](../../agents/web_agent.py#L5519) | 5519 | `"                        gap_plan = dict(plan)"` | — |
| [SRC-1AE03B9EC3-L005520](../../agents/web_agent.py#L5520) | 5520 | `"                        gap_plan.update({"` | — |
| [SRC-1AE03B9EC3-L005521](../../agents/web_agent.py#L5521) | 5521 | `"                            \"queries\": [gap_query],"` | — |
| [SRC-1AE03B9EC3-L005522](../../agents/web_agent.py#L5522) | 5522 | `"                            \"query_limit\": 1,"` | — |
| [SRC-1AE03B9EC3-L005523](../../agents/web_agent.py#L5523) | 5523 | `"                            \"depth\": \"standard\","` | — |
| [SRC-1AE03B9EC3-L005524](../../agents/web_agent.py#L5524) | 5524 | `"                            \"social_focus\": False,"` | — |
| [SRC-1AE03B9EC3-L005525](../../agents/web_agent.py#L5525) | 5525 | `"                            \"platforms\": [],"` | — |
| [SRC-1AE03B9EC3-L005526](../../agents/web_agent.py#L5526) | 5526 | `"                            \"direct_urls\": [],"` | — |
| [SRC-1AE03B9EC3-L005527](../../agents/web_agent.py#L5527) | 5527 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L005528](../../agents/web_agent.py#L5528) | 5528 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L005529](../../agents/web_agent.py#L5529) | 5529 | `"                            gap_sources, gap_warnings, gap_report = self._collect_research(gap_plan)"` | — |
| [SRC-1AE03B9EC3-L005530](../../agents/web_agent.py#L5530) | 5530 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L005531](../../agents/web_agent.py#L5531) | 5531 | `"                            gap_sources, gap_warnings = [], []"` | — |
| [SRC-1AE03B9EC3-L005532](../../agents/web_agent.py#L5532) | 5532 | `"                            gap_report = {"` | — |
| [SRC-1AE03B9EC3-L005533](../../agents/web_agent.py#L5533) | 5533 | `"                                \"queries_planned\": 1,"` | — |
| [SRC-1AE03B9EC3-L005534](../../agents/web_agent.py#L5534) | 5534 | `"                                \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L005535](../../agents/web_agent.py#L5535) | 5535 | `"                                \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L005536](../../agents/web_agent.py#L5536) | 5536 | `"                                \"search_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L005537](../../agents/web_agent.py#L5537) | 5537 | `"                                \"search_outcome\": \"unknown_after_research_error\","` | — |
| [SRC-1AE03B9EC3-L005538](../../agents/web_agent.py#L5538) | 5538 | `"                                \"query_results\": [],"` | — |
| [SRC-1AE03B9EC3-L005539](../../agents/web_agent.py#L5539) | 5539 | `"                            }"` | — |
| [SRC-1AE03B9EC3-L005540](../../agents/web_agent.py#L5540) | 5540 | `"                            criterion_gap_research[\"status\"] = \"search_failed\""` | — |
| [SRC-1AE03B9EC3-L005541](../../agents/web_agent.py#L5541) | 5541 | `"                            criterion_gap_research[\"error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L005542](../../agents/web_agent.py#L5542) | 5542 | `"                        search_warnings.extend("` | — |
| [SRC-1AE03B9EC3-L005543](../../agents/web_agent.py#L5543) | 5543 | `"                            item for item in gap_warnings if isinstance(item, str)"` | — |
| [SRC-1AE03B9EC3-L005544](../../agents/web_agent.py#L5544) | 5544 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005545](../../agents/web_agent.py#L5545) | 5545 | `"                        source_indexes: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L005546](../../agents/web_agent.py#L5546) | 5546 | `"                        for source_index, source in enumerate(sources):"` | — |
| [SRC-1AE03B9EC3-L005547](../../agents/web_agent.py#L5547) | 5547 | `"                            source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L005548](../../agents/web_agent.py#L5548) | 5548 | `"                            if source_key:"` | — |
| [SRC-1AE03B9EC3-L005549](../../agents/web_agent.py#L5549) | 5549 | `"                                source_indexes.setdefault(source_key, source_index)"` | — |
| [SRC-1AE03B9EC3-L005550](../../agents/web_agent.py#L5550) | 5550 | `"                        evidence_updated = False"` | — |
| [SRC-1AE03B9EC3-L005551](../../agents/web_agent.py#L5551) | 5551 | `"                        for candidate in gap_sources:"` | — |
| [SRC-1AE03B9EC3-L005552](../../agents/web_agent.py#L5552) | 5552 | `"                            if not isinstance(candidate, dict):"` | — |
| [SRC-1AE03B9EC3-L005553](../../agents/web_agent.py#L5553) | 5553 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L005554](../../agents/web_agent.py#L5554) | 5554 | `"                            if not self._source_matches_query(gap_query, candidate):"` | — |
| [SRC-1AE03B9EC3-L005555](../../agents/web_agent.py#L5555) | 5555 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L005556](../../agents/web_agent.py#L5556) | 5556 | `"                            source_key = self._normalized_source_url_key(candidate.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L005557](../../agents/web_agent.py#L5557) | 5557 | `"                            if not source_key:"` | — |
| [SRC-1AE03B9EC3-L005558](../../agents/web_agent.py#L5558) | 5558 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L005559](../../agents/web_agent.py#L5559) | 5559 | `"                            existing_index = source_indexes.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L005560](../../agents/web_agent.py#L5560) | 5560 | `"                            if existing_index is None:"` | — |
| [SRC-1AE03B9EC3-L005561](../../agents/web_agent.py#L5561) | 5561 | `"                                source_indexes[source_key] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005562](../../agents/web_agent.py#L5562) | 5562 | `"                                sources.append(candidate)"` | — |
| [SRC-1AE03B9EC3-L005563](../../agents/web_agent.py#L5563) | 5563 | `"                                criterion_gap_research[\"new_sources_added\"] += 1"` | — |
| [SRC-1AE03B9EC3-L005564](../../agents/web_agent.py#L5564) | 5564 | `"                                evidence_updated = True"` | — |
| [SRC-1AE03B9EC3-L005565](../../agents/web_agent.py#L5565) | 5565 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L005566](../../agents/web_agent.py#L5566) | 5566 | `"                            existing_source = sources[existing_index]"` | — |
| [SRC-1AE03B9EC3-L005567](../../agents/web_agent.py#L5567) | 5567 | `"                            merged = dict(existing_source)"` | — |
| [SRC-1AE03B9EC3-L005568](../../agents/web_agent.py#L5568) | 5568 | `"                            source_enriched = False"` | — |
| [SRC-1AE03B9EC3-L005569](../../agents/web_agent.py#L5569) | 5569 | `"                            for text_key in (\"title\", \"snippet\", \"page_text\"):"` | — |
| [SRC-1AE03B9EC3-L005570](../../agents/web_agent.py#L5570) | 5570 | `"                                old_text = str(merged.get(text_key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L005571](../../agents/web_agent.py#L5571) | 5571 | `"                                new_text = str(candidate.get(text_key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L005572](../../agents/web_agent.py#L5572) | 5572 | `"                                if len(new_text) > len(old_text):"` | — |
| [SRC-1AE03B9EC3-L005573](../../agents/web_agent.py#L5573) | 5573 | `"                                    merged[text_key] = candidate[text_key]"` | — |
| [SRC-1AE03B9EC3-L005574](../../agents/web_agent.py#L5574) | 5574 | `"                                    source_enriched = True"` | — |
| [SRC-1AE03B9EC3-L005575](../../agents/web_agent.py#L5575) | 5575 | `"                            if candidate.get(\"page_fetched\") and not existing_source.get(\"page_fetched\"):"` | — |
| [SRC-1AE03B9EC3-L005576](../../agents/web_agent.py#L5576) | 5576 | `"                                merged[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L005577](../../agents/web_agent.py#L5577) | 5577 | `"                                source_enriched = True"` | — |
| [SRC-1AE03B9EC3-L005578](../../agents/web_agent.py#L5578) | 5578 | `"                            if source_enriched:"` | — |
| [SRC-1AE03B9EC3-L005579](../../agents/web_agent.py#L5579) | 5579 | `"                                evidence_updated = True"` | — |
| [SRC-1AE03B9EC3-L005580](../../agents/web_agent.py#L5580) | 5580 | `"                                criterion_gap_research[\"evidence_sources_enriched\"] += 1"` | — |
| [SRC-1AE03B9EC3-L005581](../../agents/web_agent.py#L5581) | 5581 | `"                            merged[\"providers\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005582](../../agents/web_agent.py#L5582) | 5582 | `"                                list(existing_source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L005583](../../agents/web_agent.py#L5583) | 5583 | `"                                + list(candidate.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L005584](../../agents/web_agent.py#L5584) | 5584 | `"                            ))"` | — |
| [SRC-1AE03B9EC3-L005585](../../agents/web_agent.py#L5585) | 5585 | `"                            merged[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005586](../../agents/web_agent.py#L5586) | 5586 | `"                                list(existing_source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L005587](../../agents/web_agent.py#L5587) | 5587 | `"                                + list(candidate.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L005588](../../agents/web_agent.py#L5588) | 5588 | `"                                + [gap_query]"` | — |
| [SRC-1AE03B9EC3-L005589](../../agents/web_agent.py#L5589) | 5589 | `"                            ))"` | — |
| [SRC-1AE03B9EC3-L005590](../../agents/web_agent.py#L5590) | 5590 | `"                            sources[existing_index] = merged"` | — |
| [SRC-1AE03B9EC3-L005591](../../agents/web_agent.py#L5591) | 5591 | `"                        criterion_gap_research[\"source_count_after\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005592](../../agents/web_agent.py#L5592) | 5592 | `"                        plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005593](../../agents/web_agent.py#L5593) | 5593 | `"                            list(plan.get(\"queries\", [])) + [gap_query]"` | — |
| [SRC-1AE03B9EC3-L005594](../../agents/web_agent.py#L5594) | 5594 | `"                        ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L005595](../../agents/web_agent.py#L5595) | 5595 | `"                        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L005596](../../agents/web_agent.py#L5596) | 5596 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L005597](../../agents/web_agent.py#L5597) | 5597 | `"                            report[\"queries_planned\"] = max("` | — |
| [SRC-1AE03B9EC3-L005598](../../agents/web_agent.py#L5598) | 5598 | `"                                0, int(report.get(\"queries_planned\", 0) or 0)"` | — |
| [SRC-1AE03B9EC3-L005599](../../agents/web_agent.py#L5599) | 5599 | `"                            ) + max(0, int(gap_report.get(\"queries_planned\", 1) or 0))"` | — |
| [SRC-1AE03B9EC3-L005600](../../agents/web_agent.py#L5600) | 5600 | `"                        except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L005601](../../agents/web_agent.py#L5601) | 5601 | `"                            report[\"queries_planned\"] = None"` | — |
| [SRC-1AE03B9EC3-L005602](../../agents/web_agent.py#L5602) | 5602 | `"                        previous_attempts = report.get(\"queries_attempted\")"` | — |
| [SRC-1AE03B9EC3-L005603](../../agents/web_agent.py#L5603) | 5603 | `"                        extra_attempts = gap_report.get(\"queries_attempted\")"` | — |
| [SRC-1AE03B9EC3-L005604](../../agents/web_agent.py#L5604) | 5604 | `"                        if isinstance(previous_attempts, int) and isinstance(extra_attempts, int):"` | — |
| [SRC-1AE03B9EC3-L005605](../../agents/web_agent.py#L5605) | 5605 | `"                            report[\"queries_attempted\"] = max(0, previous_attempts) + max(0, extra_attempts)"` | — |
| [SRC-1AE03B9EC3-L005606](../../agents/web_agent.py#L5606) | 5606 | `"                            report[\"queries_attempted_known\"] = True"` | — |
| [SRC-1AE03B9EC3-L005607](../../agents/web_agent.py#L5607) | 5607 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L005608](../../agents/web_agent.py#L5608) | 5608 | `"                            report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L005609](../../agents/web_agent.py#L5609) | 5609 | `"                            report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L005610](../../agents/web_agent.py#L5610) | 5610 | `"                        old_query_results = report.get(\"query_results\")"` | — |
| [SRC-1AE03B9EC3-L005611](../../agents/web_agent.py#L5611) | 5611 | `"                        new_query_results = gap_report.get(\"query_results\")"` | — |
| [SRC-1AE03B9EC3-L005612](../../agents/web_agent.py#L5612) | 5612 | `"                        report[\"query_results\"] = ("` | — |
| [SRC-1AE03B9EC3-L005613](../../agents/web_agent.py#L5613) | 5613 | `"                            (old_query_results if isinstance(old_query_results, list) else [])"` | — |
| [SRC-1AE03B9EC3-L005614](../../agents/web_agent.py#L5614) | 5614 | `"                            + (new_query_results if isinstance(new_query_results, list) else [])"` | — |
| [SRC-1AE03B9EC3-L005615](../../agents/web_agent.py#L5615) | 5615 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005616](../../agents/web_agent.py#L5616) | 5616 | `"                        if evidence_updated:"` | — |
| [SRC-1AE03B9EC3-L005617](../../agents/web_agent.py#L5617) | 5617 | `"                            sources.sort("` | — |
| [SRC-1AE03B9EC3-L005618](../../agents/web_agent.py#L5618) | 5618 | `"                                key=lambda item: float(item.get(\"rank_score\", 0) or 0),"` | — |
| [SRC-1AE03B9EC3-L005619](../../agents/web_agent.py#L5619) | 5619 | `"                                reverse=True,"` | — |
| [SRC-1AE03B9EC3-L005620](../../agents/web_agent.py#L5620) | 5620 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005621](../../agents/web_agent.py#L5621) | 5621 | `"                            try:"` | — |
| [SRC-1AE03B9EC3-L005622](../../agents/web_agent.py#L5622) | 5622 | `"                                revised_draft = self._generate("` | — |
| [SRC-1AE03B9EC3-L005623](../../agents/web_agent.py#L5623) | 5623 | `"                                    working_question,"` | — |
| [SRC-1AE03B9EC3-L005624](../../agents/web_agent.py#L5624) | 5624 | `"                                    clean_history,"` | — |
| [SRC-1AE03B9EC3-L005625](../../agents/web_agent.py#L5625) | 5625 | `"                                    sources,"` | — |
| [SRC-1AE03B9EC3-L005626](../../agents/web_agent.py#L5626) | 5626 | `"                                    search_warning,"` | — |
| [SRC-1AE03B9EC3-L005627](../../agents/web_agent.py#L5627) | 5627 | `"                                    research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L005628](../../agents/web_agent.py#L5628) | 5628 | `"                                    search_report=report,"` | — |
| [SRC-1AE03B9EC3-L005629](../../agents/web_agent.py#L5629) | 5629 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L005630](../../agents/web_agent.py#L5630) | 5630 | `"                                revised_answer = self._review_answer("` | — |
| [SRC-1AE03B9EC3-L005631](../../agents/web_agent.py#L5631) | 5631 | `"                                    working_question, revised_draft, sources[:MAX_LLM_CITED_SOURCES]"` | — |
| [SRC-1AE03B9EC3-L005632](../../agents/web_agent.py#L5632) | 5632 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L005633](../../agents/web_agent.py#L5633) | 5633 | `"                                answer = revised_answer"` | — |
| [SRC-1AE03B9EC3-L005634](../../agents/web_agent.py#L5634) | 5634 | `"                                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005635](../../agents/web_agent.py#L5635) | 5635 | `"                                criterion_gap_research[\"status\"] = \"evidence_added_and_answer_regenerated\""` | — |
| [SRC-1AE03B9EC3-L005636](../../agents/web_agent.py#L5636) | 5636 | `"                            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005637](../../agents/web_agent.py#L5637) | 5637 | `"                                criterion_gap_research[\"status\"] = \"evidence_added_but_regeneration_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005638](../../agents/web_agent.py#L5638) | 5638 | `"                                criterion_gap_research[\"regeneration_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L005639](../../agents/web_agent.py#L5639) | 5639 | `"                                coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005640](../../agents/web_agent.py#L5640) | 5640 | `"                                    \"وصلت أدلة إضافية لمحور مطلوب، لكن تعذرت إعادة توليد الإجابة \""` | — |
| [SRC-1AE03B9EC3-L005641](../../agents/web_agent.py#L5641) | 5641 | `"                                    \"وتدقيقها ضمن الميزانية؛ راجع هذا المحور قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L005642](../../agents/web_agent.py#L5642) | 5642 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L005643](../../agents/web_agent.py#L5643) | 5643 | `"                        elif criterion_gap_research.get(\"status\") != \"search_failed\":"` | — |
| [SRC-1AE03B9EC3-L005644](../../agents/web_agent.py#L5644) | 5644 | `"                            criterion_gap_research[\"status\"] = \"search_completed_no_new_criterion_evidence\""` | — |
| [SRC-1AE03B9EC3-L005645](../../agents/web_agent.py#L5645) | 5645 | `"                            coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005646](../../agents/web_agent.py#L5646) | 5646 | `"                                \"أُجري بحث إضافي لمحاور ناقصة، لكنه لم يضف نص مصدر يمكن تمييزه \""` | — |
| [SRC-1AE03B9EC3-L005647](../../agents/web_agent.py#L5647) | 5647 | `"                                \"كدليل جديد؛ ستظل هذه المحاور غير محسومة.\""` | — |
| [SRC-1AE03B9EC3-L005648](../../agents/web_agent.py#L5648) | 5648 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005649](../../agents/web_agent.py#L5649) | 5649 | `"                        criterion_gap_research[\"source_count_after\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005650](../../agents/web_agent.py#L5650) | 5650 | `"                        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L005651](../../agents/web_agent.py#L5651) | 5651 | `""` | — |
| [SRC-1AE03B9EC3-L005652](../../agents/web_agent.py#L5652) | 5652 | `"        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L005653](../../agents/web_agent.py#L5653) | 5653 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L005654](../../agents/web_agent.py#L5654) | 5654 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005655](../../agents/web_agent.py#L5655) | 5655 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005656](../../agents/web_agent.py#L5656) | 5656 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L005657](../../agents/web_agent.py#L5657) | 5657 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L005658](../../agents/web_agent.py#L5658) | 5658 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L005659](../../agents/web_agent.py#L5659) | 5659 | `"            initial_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L005660](../../agents/web_agent.py#L5660) | 5660 | `"            missing_targets = ["` | — |
| [SRC-1AE03B9EC3-L005661](../../agents/web_agent.py#L5661) | 5661 | `"                item[\"target\"] for item in initial_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005662](../../agents/web_agent.py#L5662) | 5662 | `"                if item[\"status\"] == \"possibly_missing\""` | — |
| [SRC-1AE03B9EC3-L005663](../../agents/web_agent.py#L5663) | 5663 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L005664](../../agents/web_agent.py#L5664) | 5664 | `"            remaining_source_gap_targets = ["` | — |
| [SRC-1AE03B9EC3-L005665](../../agents/web_agent.py#L5665) | 5665 | `"                item[\"target\"] for item in initial_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005666](../../agents/web_agent.py#L5666) | 5666 | `"                if item.get(\"source_evidence_status\") == \"no_source_lexical_signal\""` | — |
| [SRC-1AE03B9EC3-L005667](../../agents/web_agent.py#L5667) | 5667 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L005668](../../agents/web_agent.py#L5668) | 5668 | `"            if not missing_targets and remaining_source_gap_targets:"` | — |
| [SRC-1AE03B9EC3-L005669](../../agents/web_agent.py#L5669) | 5669 | `"                coverage_repair_status = \"source_evidence_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L005670](../../agents/web_agent.py#L5670) | 5670 | `"                if not coverage_repair_warning:"` | — |
| [SRC-1AE03B9EC3-L005671](../../agents/web_agent.py#L5671) | 5671 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005672](../../agents/web_agent.py#L5672) | 5672 | `"                        \"ذُكرت المحاور في الإجابة، لكن لم تظهر لها إشارات لفظية في المصادر؛ \""` | — |
| [SRC-1AE03B9EC3-L005673](../../agents/web_agent.py#L5673) | 5673 | `"                        \"ذكر المحور لا يُعد دليلًا، لذلك تظل المهمة غير مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L005674](../../agents/web_agent.py#L5674) | 5674 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005675](../../agents/web_agent.py#L5675) | 5675 | `"            elif not missing_targets:"` | — |
| [SRC-1AE03B9EC3-L005676](../../agents/web_agent.py#L5676) | 5676 | `"                coverage_repair_status = \"not_needed_lexical_signals_found\""` | — |
| [SRC-1AE03B9EC3-L005677](../../agents/web_agent.py#L5677) | 5677 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005678](../../agents/web_agent.py#L5678) | 5678 | `"                coverage_repair_status = \"attempted\""` | — |
| [SRC-1AE03B9EC3-L005679](../../agents/web_agent.py#L5679) | 5679 | `"                try:"` | — |
| [SRC-1AE03B9EC3-L005680](../../agents/web_agent.py#L5680) | 5680 | `"                    repaired_answer = self._repair_answer_coverage("` | — |
| [SRC-1AE03B9EC3-L005681](../../agents/web_agent.py#L5681) | 5681 | `"                        working_question, answer, sources, missing_targets"` | — |
| [SRC-1AE03B9EC3-L005682](../../agents/web_agent.py#L5682) | 5682 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005683](../../agents/web_agent.py#L5683) | 5683 | `"                    if repaired_answer.strip() != answer.strip():"` | — |
| [SRC-1AE03B9EC3-L005684](../../agents/web_agent.py#L5684) | 5684 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L005685](../../agents/web_agent.py#L5685) | 5685 | `"                            reaudit_answer = self._review_answer("` | — |
| [SRC-1AE03B9EC3-L005686](../../agents/web_agent.py#L5686) | 5686 | `"                                working_question,"` | — |
| [SRC-1AE03B9EC3-L005687](../../agents/web_agent.py#L5687) | 5687 | `"                                repaired_answer,"` | — |
| [SRC-1AE03B9EC3-L005688](../../agents/web_agent.py#L5688) | 5688 | `"                                sources[:MAX_LLM_CITED_SOURCES],"` | — |
| [SRC-1AE03B9EC3-L005689](../../agents/web_agent.py#L5689) | 5689 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005690](../../agents/web_agent.py#L5690) | 5690 | `"                            answer = reaudit_answer"` | — |
| [SRC-1AE03B9EC3-L005691](../../agents/web_agent.py#L5691) | 5691 | `"                            coverage_repair_status = \"revised_and_reaudited\""` | — |
| [SRC-1AE03B9EC3-L005692](../../agents/web_agent.py#L5692) | 5692 | `"                            review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005693](../../agents/web_agent.py#L5693) | 5693 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005694](../../agents/web_agent.py#L5694) | 5694 | `"                            review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005695](../../agents/web_agent.py#L5695) | 5695 | `"                            review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L005696](../../agents/web_agent.py#L5696) | 5696 | `"                            coverage_repair_status = ("` | — |
| [SRC-1AE03B9EC3-L005697](../../agents/web_agent.py#L5697) | 5697 | `"                                \"reaudit_budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L005698](../../agents/web_agent.py#L5698) | 5698 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L005699](../../agents/web_agent.py#L5699) | 5699 | `"                                else \"reaudit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005700](../../agents/web_agent.py#L5700) | 5700 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005701](../../agents/web_agent.py#L5701) | 5701 | `"                            review_warning = ("` | — |
| [SRC-1AE03B9EC3-L005702](../../agents/web_agent.py#L5702) | 5702 | `"                                \"استُنفدت ميزانية النماذج قبل إعادة تدقيق الإجابة المعدلة؛ \""` | — |
| [SRC-1AE03B9EC3-L005703](../../agents/web_agent.py#L5703) | 5703 | `"                                \"لذلك لن أعرض النص المعدل بوصفه إجابة مكتملة، وأعرض مقتطفات المصادر بدلًا منه.\""` | — |
| [SRC-1AE03B9EC3-L005704](../../agents/web_agent.py#L5704) | 5704 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L005705](../../agents/web_agent.py#L5705) | 5705 | `"                                else"` | — |
| [SRC-1AE03B9EC3-L005706](../../agents/web_agent.py#L5706) | 5706 | `"                                \"تعذرت إعادة تدقيق الإجابة المعدلة مقابل الأدلة؛ لذلك لن أعرضها بوصفها إجابة مكتملة، \""` | — |
| [SRC-1AE03B9EC3-L005707](../../agents/web_agent.py#L5707) | 5707 | `"                                \"وأعرض مقتطفات المصادر بدلًا منها.\""` | — |
| [SRC-1AE03B9EC3-L005708](../../agents/web_agent.py#L5708) | 5708 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005709](../../agents/web_agent.py#L5709) | 5709 | `"                            answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L005710](../../agents/web_agent.py#L5710) | 5710 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L005711](../../agents/web_agent.py#L5711) | 5711 | `"                        coverage_repair_status = \"no_change_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L005712](../../agents/web_agent.py#L5712) | 5712 | `"                        coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005713](../../agents/web_agent.py#L5713) | 5713 | `"                            \"رصد الفحص اللفظي محورًا قد يكون ناقصًا، لكن محاولة الإصلاح لم تغيّر الإجابة؛ \""` | — |
| [SRC-1AE03B9EC3-L005714](../../agents/web_agent.py#L5714) | 5714 | `"                            \"تحقق من تغطية هذا المحور يدويًا.\""` | — |
| [SRC-1AE03B9EC3-L005715](../../agents/web_agent.py#L5715) | 5715 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005716](../../agents/web_agent.py#L5716) | 5716 | `"                except RequestBudgetExceeded:"` | — |
| [SRC-1AE03B9EC3-L005717](../../agents/web_agent.py#L5717) | 5717 | `"                    coverage_repair_status = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L005718](../../agents/web_agent.py#L5718) | 5718 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005719](../../agents/web_agent.py#L5719) | 5719 | `"                        \"استُنفدت ميزانية النماذج قبل محاولة إصلاح محور قد يكون ناقصًا؛ \""` | — |
| [SRC-1AE03B9EC3-L005720](../../agents/web_agent.py#L5720) | 5720 | `"                        \"لا تعتبر التغطية مكتملة دون مراجعة المحور المذكور.\""` | — |
| [SRC-1AE03B9EC3-L005721](../../agents/web_agent.py#L5721) | 5721 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005722](../../agents/web_agent.py#L5722) | 5722 | `"                except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L005723](../../agents/web_agent.py#L5723) | 5723 | `"                    coverage_repair_status = \"unavailable\""` | — |
| [SRC-1AE03B9EC3-L005724](../../agents/web_agent.py#L5724) | 5724 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005725](../../agents/web_agent.py#L5725) | 5725 | `"                        \"تعذرت محاولة إصلاح محور قد يكون ناقصًا (\""` | — |
| [SRC-1AE03B9EC3-L005726](../../agents/web_agent.py#L5726) | 5726 | `"                        + type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L005727](../../agents/web_agent.py#L5727) | 5727 | `"                        + \")؛ راجع المحاور المطلوبة قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L005728](../../agents/web_agent.py#L5728) | 5728 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005729](../../agents/web_agent.py#L5729) | 5729 | `"        elif coverage_targets and review_status == \"model_claim_audit_completed\" and not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L005730](../../agents/web_agent.py#L5730) | 5730 | `"            coverage_repair_status = \"skipped_no_model_configuration\""` | — |
| [SRC-1AE03B9EC3-L005731](../../agents/web_agent.py#L5731) | 5731 | `"        elif coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L005732](../../agents/web_agent.py#L5732) | 5732 | `"            coverage_repair_status = \"skipped_review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005733](../../agents/web_agent.py#L5733) | 5733 | `""` | — |
| [SRC-1AE03B9EC3-L005734](../../agents/web_agent.py#L5734) | 5734 | `"        if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L005735](../../agents/web_agent.py#L5735) | 5735 | `"            answer += \"\\n\\nروابط إضافية من البحث المباشر عبر الويب:\""` | — |
| [SRC-1AE03B9EC3-L005736](../../agents/web_agent.py#L5736) | 5736 | `"            for source in self.server_search_sources[:8]:"` | — |
| [SRC-1AE03B9EC3-L005737](../../agents/web_agent.py#L5737) | 5737 | `"                answer += \"\\n- \" + source[\"title\"] + \" — \" + source[\"url\"]"` | — |
| [SRC-1AE03B9EC3-L005738](../../agents/web_agent.py#L5738) | 5738 | `"        max_citable_sources = min(MAX_LLM_CITED_SOURCES, len(sources))"` | — |
| [SRC-1AE03B9EC3-L005739](../../agents/web_agent.py#L5739) | 5739 | `"        answer, citation_warnings = self._remove_invalid_citations("` | — |
| [SRC-1AE03B9EC3-L005740](../../agents/web_agent.py#L5740) | 5740 | `"            answer, max_citable_sources"` | — |
| [SRC-1AE03B9EC3-L005741](../../agents/web_agent.py#L5741) | 5741 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005742](../../agents/web_agent.py#L5742) | 5742 | `"        citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L005743](../../agents/web_agent.py#L5743) | 5743 | `"            answer, max_citable_sources, citation_warnings, review_status"` | — |
| [SRC-1AE03B9EC3-L005744](../../agents/web_agent.py#L5744) | 5744 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005745](../../agents/web_agent.py#L5745) | 5745 | `"        report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005746](../../agents/web_agent.py#L5746) | 5746 | `"        report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005747](../../agents/web_agent.py#L5747) | 5747 | `"        report[\"second_pass_review\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L005748](../../agents/web_agent.py#L5748) | 5748 | `"        report[\"claim_audit\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L005749](../../agents/web_agent.py#L5749) | 5749 | `"        answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L005750](../../agents/web_agent.py#L5750) | 5750 | `"            \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L005751](../../agents/web_agent.py#L5751) | 5751 | `"            \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L005752](../../agents/web_agent.py#L5752) | 5752 | `"            \"review_prompted\": review_status == \"model_claim_audit_completed\","` | — |
| [SRC-1AE03B9EC3-L005753](../../agents/web_agent.py#L5753) | 5753 | `"            \"status\": ("` | — |
| [SRC-1AE03B9EC3-L005754](../../agents/web_agent.py#L5754) | 5754 | `"                \"model_review_requested_not_machine_verified\""` | — |
| [SRC-1AE03B9EC3-L005755](../../agents/web_agent.py#L5755) | 5755 | `"                if coverage_targets and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005756](../../agents/web_agent.py#L5756) | 5756 | `"                else \"review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005757](../../agents/web_agent.py#L5757) | 5757 | `"                if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005758](../../agents/web_agent.py#L5758) | 5758 | `"                else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005759](../../agents/web_agent.py#L5759) | 5759 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L005760](../../agents/web_agent.py#L5760) | 5760 | `"            \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L005761](../../agents/web_agent.py#L5761) | 5761 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005762](../../agents/web_agent.py#L5762) | 5762 | `"        report[\"answer_coverage\"] = answer_coverage"` | — |
| [SRC-1AE03B9EC3-L005763](../../agents/web_agent.py#L5763) | 5763 | `"        report[\"coverage_repair_status\"] = coverage_repair_status"` | — |
| [SRC-1AE03B9EC3-L005764](../../agents/web_agent.py#L5764) | 5764 | `"        answer_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L005765](../../agents/web_agent.py#L5765) | 5765 | `"        answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005766](../../agents/web_agent.py#L5766) | 5766 | `"        answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L005767](../../agents/web_agent.py#L5767) | 5767 | `"        answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L005768](../../agents/web_agent.py#L5768) | 5768 | `"        answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L005769](../../agents/web_agent.py#L5769) | 5769 | `"        task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L005770](../../agents/web_agent.py#L5770) | 5770 | `"            \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L005771](../../agents/web_agent.py#L5771) | 5771 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L005772](../../agents/web_agent.py#L5772) | 5772 | `"                answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L005773](../../agents/web_agent.py#L5773) | 5773 | `"                or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L005774](../../agents/web_agent.py#L5774) | 5774 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005775](../../agents/web_agent.py#L5775) | 5775 | `"            else \"lexical_signals_found_not_semantically_verified\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005776](../../agents/web_agent.py#L5776) | 5776 | `"            else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005777](../../agents/web_agent.py#L5777) | 5777 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005778](../../agents/web_agent.py#L5778) | 5778 | `"        answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L005779](../../agents/web_agent.py#L5779) | 5779 | `"        report[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L005780](../../agents/web_agent.py#L5780) | 5780 | `"        report[\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L005781](../../agents/web_agent.py#L5781) | 5781 | `"        report[\"connector_summary\"] = self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L005782](../../agents/web_agent.py#L5782) | 5782 | `"            list(self._provider_diagnostics), sources"` | — |
| [SRC-1AE03B9EC3-L005783](../../agents/web_agent.py#L5783) | 5783 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005784](../../agents/web_agent.py#L5784) | 5784 | `"        report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L005785](../../agents/web_agent.py#L5785) | 5785 | `"        distinct_providers = {"` | — |
| [SRC-1AE03B9EC3-L005786](../../agents/web_agent.py#L5786) | 5786 | `"            provider for source in sources for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L005787](../../agents/web_agent.py#L5787) | 5787 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005788](../../agents/web_agent.py#L5788) | 5788 | `"        distinct_domains = {"` | — |
| [SRC-1AE03B9EC3-L005789](../../agents/web_agent.py#L5789) | 5789 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L005790](../../agents/web_agent.py#L5790) | 5790 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L005791](../../agents/web_agent.py#L5791) | 5791 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L005792](../../agents/web_agent.py#L5792) | 5792 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L005793](../../agents/web_agent.py#L5793) | 5793 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005794](../../agents/web_agent.py#L5794) | 5794 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005795](../../agents/web_agent.py#L5795) | 5795 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005796](../../agents/web_agent.py#L5796) | 5796 | `"        distinct_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005797](../../agents/web_agent.py#L5797) | 5797 | `"        fetched_pages = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005798](../../agents/web_agent.py#L5798) | 5798 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L005799](../../agents/web_agent.py#L5799) | 5799 | `"            len(sources) >= 4 and len(distinct_domains) >= 3"` | — |
| [SRC-1AE03B9EC3-L005800](../../agents/web_agent.py#L5800) | 5800 | `"            and len(distinct_providers) >= 2 and fetched_pages >= 1"` | — |
| [SRC-1AE03B9EC3-L005801](../../agents/web_agent.py#L5801) | 5801 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005802](../../agents/web_agent.py#L5802) | 5802 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L005803](../../agents/web_agent.py#L5803) | 5803 | `"            research_quality = \"excellent\""` | — |
| [SRC-1AE03B9EC3-L005804](../../agents/web_agent.py#L5804) | 5804 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L005805](../../agents/web_agent.py#L5805) | 5805 | `"            len(sources) >= 2 and len(distinct_domains) >= 2"` | — |
| [SRC-1AE03B9EC3-L005806](../../agents/web_agent.py#L5806) | 5806 | `"            and (len(distinct_providers) >= 2 or fetched_pages >= 1)"` | — |
| [SRC-1AE03B9EC3-L005807](../../agents/web_agent.py#L5807) | 5807 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005808](../../agents/web_agent.py#L5808) | 5808 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L005809](../../agents/web_agent.py#L5809) | 5809 | `"            research_quality = \"good\""` | — |
| [SRC-1AE03B9EC3-L005810](../../agents/web_agent.py#L5810) | 5810 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005811](../../agents/web_agent.py#L5811) | 5811 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L005812](../../agents/web_agent.py#L5812) | 5812 | `""` | — |
| [SRC-1AE03B9EC3-L005813](../../agents/web_agent.py#L5813) | 5813 | `"        # Source breadth and a completed model-assisted review do not justify a"` | — |
| [SRC-1AE03B9EC3-L005814](../../agents/web_agent.py#L5814) | 5814 | `"        # positive research-quality label if the final answer has no valid source"` | — |
| [SRC-1AE03B9EC3-L005815](../../agents/web_agent.py#L5815) | 5815 | `"        # citation markers. This is a deterministic presentation guard, not a"` | — |
| [SRC-1AE03B9EC3-L005816](../../agents/web_agent.py#L5816) | 5816 | `"        # semantic entailment check."` | — |
| [SRC-1AE03B9EC3-L005817](../../agents/web_agent.py#L5817) | 5817 | `"        uncited_reviewed_answer = ("` | — |
| [SRC-1AE03B9EC3-L005818](../../agents/web_agent.py#L5818) | 5818 | `"            used_llm"` | — |
| [SRC-1AE03B9EC3-L005819](../../agents/web_agent.py#L5819) | 5819 | `"            and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L005820](../../agents/web_agent.py#L5820) | 5820 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005821](../../agents/web_agent.py#L5821) | 5821 | `"            and citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L005822](../../agents/web_agent.py#L5822) | 5822 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005823](../../agents/web_agent.py#L5823) | 5823 | `"        if uncited_reviewed_answer:"` | — |
| [SRC-1AE03B9EC3-L005824](../../agents/web_agent.py#L5824) | 5824 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L005825](../../agents/web_agent.py#L5825) | 5825 | `"            citation_validation[\"claim_support\"] = \"not_established_no_valid_source_citations\""` | — |
| [SRC-1AE03B9EC3-L005826](../../agents/web_agent.py#L5826) | 5826 | `"            answer_evidence_status = \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-1AE03B9EC3-L005827](../../agents/web_agent.py#L5827) | 5827 | `"            uncited_answer_warning = ("` | — |
| [SRC-1AE03B9EC3-L005828](../../agents/web_agent.py#L5828) | 5828 | `"                \"اكتملت مراجعة النموذج، لكن الإجابة النهائية لا تحتوي على إحالات صالحة \""` | — |
| [SRC-1AE03B9EC3-L005829](../../agents/web_agent.py#L5829) | 5829 | `"                \"إلى قائمة المصادر؛ لذلك صُنّفت جودة البحث «جزئية». وجود المصادر أو \""` | — |
| [SRC-1AE03B9EC3-L005830](../../agents/web_agent.py#L5830) | 5830 | `"                \"اكتمال مراجعة النموذج لا يثبت دعم كل ادعاء.\""` | — |
| [SRC-1AE03B9EC3-L005831](../../agents/web_agent.py#L5831) | 5831 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005832](../../agents/web_agent.py#L5832) | 5832 | `"        elif citation_validation[\"valid_citation_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L005833](../../agents/web_agent.py#L5833) | 5833 | `"            answer_evidence_status = \"citation_indices_validated_only\""` | — |
| [SRC-1AE03B9EC3-L005834](../../agents/web_agent.py#L5834) | 5834 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L005835](../../agents/web_agent.py#L5835) | 5835 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005836](../../agents/web_agent.py#L5836) | 5836 | `"            answer_evidence_status = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L005837](../../agents/web_agent.py#L5837) | 5837 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L005838](../../agents/web_agent.py#L5838) | 5838 | `""` | — |
| [SRC-1AE03B9EC3-L005839](../../agents/web_agent.py#L5839) | 5839 | `"        search_attempted = search_attempted or bool(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L005840](../../agents/web_agent.py#L5840) | 5840 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L005841](../../agents/web_agent.py#L5841) | 5841 | `"        report[\"search_outcome\"] = ("` | — |
| [SRC-1AE03B9EC3-L005842](../../agents/web_agent.py#L5842) | 5842 | `"            \"attempted_with_usable_sources\" if search_attempted and sources"` | — |
| [SRC-1AE03B9EC3-L005843](../../agents/web_agent.py#L5843) | 5843 | `"            else \"attempted_no_usable_sources\" if search_attempted"` | — |
| [SRC-1AE03B9EC3-L005844](../../agents/web_agent.py#L5844) | 5844 | `"            else \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L005845](../../agents/web_agent.py#L5845) | 5845 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005846](../../agents/web_agent.py#L5846) | 5846 | `"        report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005847](../../agents/web_agent.py#L5847) | 5847 | `"        report[\"research_quality\"] = research_quality"` | — |
| [SRC-1AE03B9EC3-L005848](../../agents/web_agent.py#L5848) | 5848 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L005849](../../agents/web_agent.py#L5849) | 5849 | `"        report[\"answer_evidence_status\"] = answer_evidence_status"` | — |
| [SRC-1AE03B9EC3-L005850](../../agents/web_agent.py#L5850) | 5850 | `"        report[\"distinct_registrable_domains\"] = len(distinct_domains)"` | — |
| [SRC-1AE03B9EC3-L005851](../../agents/web_agent.py#L5851) | 5851 | `"        report[\"independent_sources\"] = len(distinct_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L005852](../../agents/web_agent.py#L5852) | 5852 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005853](../../agents/web_agent.py#L5853) | 5853 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L005854](../../agents/web_agent.py#L5854) | 5854 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005855](../../agents/web_agent.py#L5855) | 5855 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005856](../../agents/web_agent.py#L5856) | 5856 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L005857](../../agents/web_agent.py#L5857) | 5857 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005858](../../agents/web_agent.py#L5858) | 5858 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L005859](../../agents/web_agent.py#L5859) | 5859 | `"        report[\"claim_audit_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005860](../../agents/web_agent.py#L5860) | 5860 | `"            \"model_assisted_not_independent_fact_check\""` | — |
| [SRC-1AE03B9EC3-L005861](../../agents/web_agent.py#L5861) | 5861 | `"            if review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005862](../../agents/web_agent.py#L5862) | 5862 | `"            else \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L005863](../../agents/web_agent.py#L5863) | 5863 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005864](../../agents/web_agent.py#L5864) | 5864 | `"        report[\"insufficient_evidence\"] = False"` | — |
| [SRC-1AE03B9EC3-L005865](../../agents/web_agent.py#L5865) | 5865 | `"        report[\"valid_citation_range\"] = [1, max_citable_sources] if max_citable_sources else []"` | — |
| [SRC-1AE03B9EC3-L005866](../../agents/web_agent.py#L5866) | 5866 | `"        report[\"citation_count\"] = citation_validation[\"valid_citation_count\"]"` | — |
| [SRC-1AE03B9EC3-L005867](../../agents/web_agent.py#L5867) | 5867 | `"        report[\"citation_check\"] = citation_validation[\"status\"]"` | — |
| [SRC-1AE03B9EC3-L005868](../../agents/web_agent.py#L5868) | 5868 | `"        report[\"citation_validation\"] = citation_validation"` | — |
| [SRC-1AE03B9EC3-L005869](../../agents/web_agent.py#L5869) | 5869 | `"        warnings = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005870](../../agents/web_agent.py#L5870) | 5870 | `"            search_warnings"` | — |
| [SRC-1AE03B9EC3-L005871](../../agents/web_agent.py#L5871) | 5871 | `"            + ([llm_warning] if llm_warning else [])"` | — |
| [SRC-1AE03B9EC3-L005872](../../agents/web_agent.py#L5872) | 5872 | `"            + ([review_warning] if review_warning else [])"` | — |
| [SRC-1AE03B9EC3-L005873](../../agents/web_agent.py#L5873) | 5873 | `"            + ([coverage_repair_warning] if coverage_repair_warning else [])"` | — |
| [SRC-1AE03B9EC3-L005874](../../agents/web_agent.py#L5874) | 5874 | `"            + citation_warnings"` | — |
| [SRC-1AE03B9EC3-L005875](../../agents/web_agent.py#L5875) | 5875 | `"            + ([uncited_answer_warning] if uncited_answer_warning else [])"` | — |
| [SRC-1AE03B9EC3-L005876](../../agents/web_agent.py#L5876) | 5876 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L005877](../../agents/web_agent.py#L5877) | 5877 | `"        report[\"model_calls\"] = list(self.model_usage)"` | — |
| [SRC-1AE03B9EC3-L005878](../../agents/web_agent.py#L5878) | 5878 | `"        report[\"openrouter_web_search_enabled\"] = self.openrouter_web_search_enabled"` | — |
| [SRC-1AE03B9EC3-L005879](../../agents/web_agent.py#L5879) | 5879 | `"        report[\"openrouter_web_search_results\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L005880](../../agents/web_agent.py#L5880) | 5880 | `"        if generation_budget_exhausted or review_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L005881](../../agents/web_agent.py#L5881) | 5881 | `"            final_answer_status = \"budget_exhausted_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L005882](../../agents/web_agent.py#L5882) | 5882 | `"        elif llm_warning:"` | — |
| [SRC-1AE03B9EC3-L005883](../../agents/web_agent.py#L5883) | 5883 | `"            final_answer_status = ("` | — |
| [SRC-1AE03B9EC3-L005884](../../agents/web_agent.py#L5884) | 5884 | `"                \"model_not_configured_fallback\""` | — |
| [SRC-1AE03B9EC3-L005885](../../agents/web_agent.py#L5885) | 5885 | `"                if not self.api_key"` | — |
| [SRC-1AE03B9EC3-L005886](../../agents/web_agent.py#L5886) | 5886 | `"                else \"generation_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L005887](../../agents/web_agent.py#L5887) | 5887 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005888](../../agents/web_agent.py#L5888) | 5888 | `"        elif review_warning:"` | — |
| [SRC-1AE03B9EC3-L005889](../../agents/web_agent.py#L5889) | 5889 | `"            final_answer_status = \"review_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L005890](../../agents/web_agent.py#L5890) | 5890 | `"        elif coverage_repair_status == \"no_change_gap_unresolved\":"` | — |
| [SRC-1AE03B9EC3-L005891](../../agents/web_agent.py#L5891) | 5891 | `"            final_answer_status = \"coverage_repair_left_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L005892](../../agents/web_agent.py#L5892) | 5892 | `"        elif coverage_repair_status == \"budget_exhausted\":"` | — |
| [SRC-1AE03B9EC3-L005893](../../agents/web_agent.py#L5893) | 5893 | `"            final_answer_status = \"coverage_repair_budget_exhausted_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L005894](../../agents/web_agent.py#L5894) | 5894 | `"        elif coverage_repair_status == \"unavailable\":"` | — |
| [SRC-1AE03B9EC3-L005895](../../agents/web_agent.py#L5895) | 5895 | `"            final_answer_status = \"coverage_repair_unavailable_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L005896](../../agents/web_agent.py#L5896) | 5896 | `"        elif used_llm:"` | — |
| [SRC-1AE03B9EC3-L005897](../../agents/web_agent.py#L5897) | 5897 | `"            final_answer_status = \"model_answer_generated\""` | — |
| [SRC-1AE03B9EC3-L005898](../../agents/web_agent.py#L5898) | 5898 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005899](../../agents/web_agent.py#L5899) | 5899 | `"            final_answer_status = \"source_fallback\""` | — |
| [SRC-1AE03B9EC3-L005900](../../agents/web_agent.py#L5900) | 5900 | `""` | — |
| [SRC-1AE03B9EC3-L005901](../../agents/web_agent.py#L5901) | 5901 | `"        public_sources = []"` | — |
| [SRC-1AE03B9EC3-L005902](../../agents/web_agent.py#L5902) | 5902 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L005903](../../agents/web_agent.py#L5903) | 5903 | `"            public_sources.append({"` | — |
| [SRC-1AE03B9EC3-L005904](../../agents/web_agent.py#L5904) | 5904 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L005905](../../agents/web_agent.py#L5905) | 5905 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L005906](../../agents/web_agent.py#L5906) | 5906 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005907](../../agents/web_agent.py#L5907) | 5907 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005908](../../agents/web_agent.py#L5908) | 5908 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L005909](../../agents/web_agent.py#L5909) | 5909 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005910](../../agents/web_agent.py#L5910) | 5910 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L005911](../../agents/web_agent.py#L5911) | 5911 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005912](../../agents/web_agent.py#L5912) | 5912 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L005913](../../agents/web_agent.py#L5913) | 5913 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005914](../../agents/web_agent.py#L5914) | 5914 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005915](../../agents/web_agent.py#L5915) | 5915 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005916](../../agents/web_agent.py#L5916) | 5916 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L005917](../../agents/web_agent.py#L5917) | 5917 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L005918](../../agents/web_agent.py#L5918) | 5918 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L005919](../../agents/web_agent.py#L5919) | 5919 | `"            })"` | — |
| [SRC-1AE03B9EC3-L005920](../../agents/web_agent.py#L5920) | 5920 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L005921](../../agents/web_agent.py#L5921) | 5921 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L005922](../../agents/web_agent.py#L5922) | 5922 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L005923](../../agents/web_agent.py#L5923) | 5923 | `"            \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L005924](../../agents/web_agent.py#L5924) | 5924 | `"            \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005925](../../agents/web_agent.py#L5925) | 5925 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L005926](../../agents/web_agent.py#L5926) | 5926 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L005927](../../agents/web_agent.py#L5927) | 5927 | `"                \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L005928](../../agents/web_agent.py#L5928) | 5928 | `"                \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L005929](../../agents/web_agent.py#L5929) | 5929 | `"                \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L005930](../../agents/web_agent.py#L5930) | 5930 | `"                \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L005931](../../agents/web_agent.py#L5931) | 5931 | `"                \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L005932](../../agents/web_agent.py#L5932) | 5932 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L005933](../../agents/web_agent.py#L5933) | 5933 | `"                \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L005934](../../agents/web_agent.py#L5934) | 5934 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005935](../../agents/web_agent.py#L5935) | 5935 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005936](../../agents/web_agent.py#L5936) | 5936 | `"            },"` | — |
| [SRC-1AE03B9EC3-L005937](../../agents/web_agent.py#L5937) | 5937 | `"            \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L005938](../../agents/web_agent.py#L5938) | 5938 | `"            \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L005939](../../agents/web_agent.py#L5939) | 5939 | `"            \"research_quality\": research_quality,"` | — |
| [SRC-1AE03B9EC3-L005940](../../agents/web_agent.py#L5940) | 5940 | `"            \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L005941](../../agents/web_agent.py#L5941) | 5941 | `"            \"answer_evidence_status\": answer_evidence_status,"` | — |
| [SRC-1AE03B9EC3-L005942](../../agents/web_agent.py#L5942) | 5942 | `"            \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L005943](../../agents/web_agent.py#L5943) | 5943 | `"            \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L005944](../../agents/web_agent.py#L5944) | 5944 | `"            \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L005945](../../agents/web_agent.py#L5945) | 5945 | `"            \"coverage_repair_status\": coverage_repair_status,"` | — |
| [SRC-1AE03B9EC3-L005946](../../agents/web_agent.py#L5946) | 5946 | `"            \"used_language_model\": used_llm,"` | — |
| [SRC-1AE03B9EC3-L005947](../../agents/web_agent.py#L5947) | 5947 | `"            \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L005948](../../agents/web_agent.py#L5948) | 5948 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L005949](../../agents/web_agent.py#L5949) | 5949 | `"            \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L005950](../../agents/web_agent.py#L5950) | 5950 | `"            \"warnings\": warnings,"` | — |
| [SRC-1AE03B9EC3-L005951](../../agents/web_agent.py#L5951) | 5951 | `"            \"kind\": \"web_research\" if used_llm else \"web_fallback\","` | — |
| [SRC-1AE03B9EC3-L005952](../../agents/web_agent.py#L5952) | 5952 | `"            \"final_answer_status\": final_answer_status,"` | — |
| [SRC-1AE03B9EC3-L005953](../../agents/web_agent.py#L5953) | 5953 | `"            \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005954](../../agents/web_agent.py#L5954) | 5954 | `"            \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005955](../../agents/web_agent.py#L5955) | 5955 | `"        }"` | — |
## واجهات API

### FILE-D8438CDB65 — [api/__init__.py](../../api/__init__.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-D8438CDB65-L000001](../../api/__init__.py#L1) | 1 | `"\"\"\"Omarai local API package.\"\"\""` | — |
## واجهات API

### FILE-EEF2E6447C — [api/omarai.py](../../api/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-EEF2E6447C-L000001](../../api/omarai.py#L1) | 1 | `"\"\"\"HTTP API for Omarai's web-research agent and lead workspace.\"\"\""` | — |
| [SRC-EEF2E6447C-L000002](../../api/omarai.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-EEF2E6447C-L000003](../../api/omarai.py#L3) | 3 | `""` | — |
| [SRC-EEF2E6447C-L000004](../../api/omarai.py#L4) | 4 | `"import base64"` | — |
| [SRC-EEF2E6447C-L000005](../../api/omarai.py#L5) | 5 | `"import hashlib"` | — |
| [SRC-EEF2E6447C-L000006](../../api/omarai.py#L6) | 6 | `"import hmac"` | — |
| [SRC-EEF2E6447C-L000007](../../api/omarai.py#L7) | 7 | `"import ipaddress"` | — |
| [SRC-EEF2E6447C-L000008](../../api/omarai.py#L8) | 8 | `"import json"` | — |
| [SRC-EEF2E6447C-L000009](../../api/omarai.py#L9) | 9 | `"import os"` | — |
