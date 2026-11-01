# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **018**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L006087 إلى SRC-1AE03B9EC3-L006886
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L006087](../../agents/web_agent.py#L6087) | 6087 | `"                    \"اختلاف النطاقات لا يثبت الاستقلال التحريري. لن أخمّن أو أقدّم نتيجة غير مدعومة؛ \""` | — |
| [SRC-1AE03B9EC3-L006088](../../agents/web_agent.py#L6088) | 6088 | `"                    \"جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L006089](../../agents/web_agent.py#L6089) | 6089 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006090](../../agents/web_agent.py#L6090) | 6090 | `"            public_sources = [{"` | — |
| [SRC-1AE03B9EC3-L006091](../../agents/web_agent.py#L6091) | 6091 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L006092](../../agents/web_agent.py#L6092) | 6092 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L006093](../../agents/web_agent.py#L6093) | 6093 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L006094](../../agents/web_agent.py#L6094) | 6094 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L006095](../../agents/web_agent.py#L6095) | 6095 | `"                \"readable_page_text_available\": bool(source.get(\"page_fetched\")) and bool(str(source.get(\"page_text\") or \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L006096](../../agents/web_agent.py#L6096) | 6096 | `"                \"page_text_present_without_fetch_flag\": bool(str(source.get(\"page_text\") or \"\").strip()) and not bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L006097](../../agents/web_agent.py#L6097) | 6097 | `"                \"page_fetch_status\": source.get(\"page_fetch_status\", \"unknown\"),"` | — |
| [SRC-1AE03B9EC3-L006098](../../agents/web_agent.py#L6098) | 6098 | `"                \"page_fetch_error_class\": source.get(\"page_fetch_error_class\"),"` | — |
| [SRC-1AE03B9EC3-L006099](../../agents/web_agent.py#L6099) | 6099 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L006100](../../agents/web_agent.py#L6100) | 6100 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L006101](../../agents/web_agent.py#L6101) | 6101 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L006102](../../agents/web_agent.py#L6102) | 6102 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L006103](../../agents/web_agent.py#L6103) | 6103 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L006104](../../agents/web_agent.py#L6104) | 6104 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L006105](../../agents/web_agent.py#L6105) | 6105 | `"                \"opinion_source_classification\": source.get(\"opinion_source_classification\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L006106](../../agents/web_agent.py#L6106) | 6106 | `"                \"opinion_classification_basis\": source.get(\"opinion_classification_basis\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L006107](../../agents/web_agent.py#L6107) | 6107 | `"                \"opinion_classification_method\": source.get(\"opinion_classification_method\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L006108](../../agents/web_agent.py#L6108) | 6108 | `"                \"current_evidence_assessment\": source.get(\"current_evidence_assessment\", {}),"` | — |
| [SRC-1AE03B9EC3-L006109](../../agents/web_agent.py#L6109) | 6109 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L006110](../../agents/web_agent.py#L6110) | 6110 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L006111](../../agents/web_agent.py#L6111) | 6111 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L006112](../../agents/web_agent.py#L6112) | 6112 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L006113](../../agents/web_agent.py#L6113) | 6113 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L006114](../../agents/web_agent.py#L6114) | 6114 | `"            } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L006115](../../agents/web_agent.py#L6115) | 6115 | `"            citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L006116](../../agents/web_agent.py#L6116) | 6116 | `"                reason, 0, [], \"not_run\""` | — |
| [SRC-1AE03B9EC3-L006117](../../agents/web_agent.py#L6117) | 6117 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006118](../../agents/web_agent.py#L6118) | 6118 | `"            citation_validation[\"status\"] = \"not_applicable_no_generated_answer\""` | — |
| [SRC-1AE03B9EC3-L006119](../../agents/web_agent.py#L6119) | 6119 | `"            coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L006120](../../agents/web_agent.py#L6120) | 6120 | `"            answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L006121](../../agents/web_agent.py#L6121) | 6121 | `"                \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L006122](../../agents/web_agent.py#L6122) | 6122 | `"                \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L006123](../../agents/web_agent.py#L6123) | 6123 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L006124](../../agents/web_agent.py#L6124) | 6124 | `"                    \"not_reviewed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L006125](../../agents/web_agent.py#L6125) | 6125 | `"                    if coverage_targets else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L006126](../../agents/web_agent.py#L6126) | 6126 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L006127](../../agents/web_agent.py#L6127) | 6127 | `"                \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L006128](../../agents/web_agent.py#L6128) | 6128 | `"            }"` | — |
| [SRC-1AE03B9EC3-L006129](../../agents/web_agent.py#L6129) | 6129 | `"            answer_integrity = audit_answer_integrity(working_question, reason, sources, coverage_targets, plan.get(\"requirement_queries\"))"` | — |
| [SRC-1AE03B9EC3-L006130](../../agents/web_agent.py#L6130) | 6130 | `"            answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L006131](../../agents/web_agent.py#L6131) | 6131 | `"            answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L006132](../../agents/web_agent.py#L6132) | 6132 | `"            answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L006133](../../agents/web_agent.py#L6133) | 6133 | `"            answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L006134](../../agents/web_agent.py#L6134) | 6134 | `"            task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L006135](../../agents/web_agent.py#L6135) | 6135 | `"                \"not_assessed_insufficient_evidence\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L006136](../../agents/web_agent.py#L6136) | 6136 | `"                else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L006137](../../agents/web_agent.py#L6137) | 6137 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006138](../../agents/web_agent.py#L6138) | 6138 | `"            answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L006139](../../agents/web_agent.py#L6139) | 6139 | `"            research_failed = search_outcome in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L006140](../../agents/web_agent.py#L6140) | 6140 | `"            report.update({"` | — |
| [SRC-1AE03B9EC3-L006141](../../agents/web_agent.py#L6141) | 6141 | `"                # When collection failed, an empty local list is not evidence that"` | — |
| [SRC-1AE03B9EC3-L006142](../../agents/web_agent.py#L6142) | 6142 | `"                # the remote search returned zero sources; preserve unknown counts."` | — |
| [SRC-1AE03B9EC3-L006143](../../agents/web_agent.py#L6143) | 6143 | `"                \"unique_sources\": None if research_failed else len(sources),"` | — |
| [SRC-1AE03B9EC3-L006144](../../agents/web_agent.py#L6144) | 6144 | `"                \"independent_sources\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L006145](../../agents/web_agent.py#L6145) | 6145 | `"                \"distinct_registrable_domains\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L006146](../../agents/web_agent.py#L6146) | 6146 | `"                \"pages_fetched\": ("` | — |
| [SRC-1AE03B9EC3-L006147](../../agents/web_agent.py#L6147) | 6147 | `"                    None if research_failed"` | — |
| [SRC-1AE03B9EC3-L006148](../../agents/web_agent.py#L6148) | 6148 | `"                    else sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L006149](../../agents/web_agent.py#L6149) | 6149 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L006150](../../agents/web_agent.py#L6150) | 6150 | `"                \"provider_diagnostics\": current_research_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L006151](../../agents/web_agent.py#L6151) | 6151 | `"                \"insufficient_evidence\": True,"` | — |
| [SRC-1AE03B9EC3-L006152](../../agents/web_agent.py#L6152) | 6152 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L006153](../../agents/web_agent.py#L6153) | 6153 | `"                \"citation_check\": citation_validation[\"status\"],"` | — |
| [SRC-1AE03B9EC3-L006154](../../agents/web_agent.py#L6154) | 6154 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L006155](../../agents/web_agent.py#L6155) | 6155 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L006156](../../agents/web_agent.py#L6156) | 6156 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L006157](../../agents/web_agent.py#L6157) | 6157 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L006158](../../agents/web_agent.py#L6158) | 6158 | `"                \"connector_summary\": report.get(\"connector_summary\") or self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L006159](../../agents/web_agent.py#L6159) | 6159 | `"                    current_research_diagnostics, sources"` | — |
| [SRC-1AE03B9EC3-L006160](../../agents/web_agent.py#L6160) | 6160 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L006161](../../agents/web_agent.py#L6161) | 6161 | `"            })"` | — |
| [SRC-1AE03B9EC3-L006162](../../agents/web_agent.py#L6162) | 6162 | `"            return {"` | — |
| [SRC-1AE03B9EC3-L006163](../../agents/web_agent.py#L6163) | 6163 | `"                \"answer\": reason,"` | — |
| [SRC-1AE03B9EC3-L006164](../../agents/web_agent.py#L6164) | 6164 | `"                \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L006165](../../agents/web_agent.py#L6165) | 6165 | `"                \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L006166](../../agents/web_agent.py#L6166) | 6166 | `"                \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L006167](../../agents/web_agent.py#L6167) | 6167 | `"                \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L006168](../../agents/web_agent.py#L6168) | 6168 | `"                    \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L006169](../../agents/web_agent.py#L6169) | 6169 | `"                    \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L006170](../../agents/web_agent.py#L6170) | 6170 | `"                    \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L006171](../../agents/web_agent.py#L6171) | 6171 | `"                    \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L006172](../../agents/web_agent.py#L6172) | 6172 | `"                    \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L006173](../../agents/web_agent.py#L6173) | 6173 | `"                    \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L006174](../../agents/web_agent.py#L6174) | 6174 | `"                    \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L006175](../../agents/web_agent.py#L6175) | 6175 | `"                    \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L006176](../../agents/web_agent.py#L6176) | 6176 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L006177](../../agents/web_agent.py#L6177) | 6177 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L006178](../../agents/web_agent.py#L6178) | 6178 | `"                },"` | — |
| [SRC-1AE03B9EC3-L006179](../../agents/web_agent.py#L6179) | 6179 | `"                \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L006180](../../agents/web_agent.py#L6180) | 6180 | `"                \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L006181](../../agents/web_agent.py#L6181) | 6181 | `"                \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L006182](../../agents/web_agent.py#L6182) | 6182 | `"                \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L006183](../../agents/web_agent.py#L6183) | 6183 | `"                \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L006184](../../agents/web_agent.py#L6184) | 6184 | `"                \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L006185](../../agents/web_agent.py#L6185) | 6185 | `"                \"warnings\": list(dict.fromkeys(search_warnings + [reason])),"` | — |
| [SRC-1AE03B9EC3-L006186](../../agents/web_agent.py#L6186) | 6186 | `"                \"kind\": \"insufficient_evidence\","` | — |
| [SRC-1AE03B9EC3-L006187](../../agents/web_agent.py#L6187) | 6187 | `"                \"final_answer_status\": \"insufficient_evidence_no_generation\","` | — |
| [SRC-1AE03B9EC3-L006188](../../agents/web_agent.py#L6188) | 6188 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L006189](../../agents/web_agent.py#L6189) | 6189 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L006190](../../agents/web_agent.py#L6190) | 6190 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L006191](../../agents/web_agent.py#L6191) | 6191 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L006192](../../agents/web_agent.py#L6192) | 6192 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L006193](../../agents/web_agent.py#L6193) | 6193 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L006194](../../agents/web_agent.py#L6194) | 6194 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L006195](../../agents/web_agent.py#L6195) | 6195 | `"            }"` | — |
| [SRC-1AE03B9EC3-L006196](../../agents/web_agent.py#L6196) | 6196 | `""` | — |
| [SRC-1AE03B9EC3-L006197](../../agents/web_agent.py#L6197) | 6197 | `"        answer = \"\""` | — |
| [SRC-1AE03B9EC3-L006198](../../agents/web_agent.py#L6198) | 6198 | `"        used_llm = False"` | — |
| [SRC-1AE03B9EC3-L006199](../../agents/web_agent.py#L6199) | 6199 | `"        llm_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L006200](../../agents/web_agent.py#L6200) | 6200 | `"        generation_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L006201](../../agents/web_agent.py#L6201) | 6201 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L006202](../../agents/web_agent.py#L6202) | 6202 | `"            answer = self._generate("` | — |
| [SRC-1AE03B9EC3-L006203](../../agents/web_agent.py#L6203) | 6203 | `"                working_question,"` | — |
| [SRC-1AE03B9EC3-L006204](../../agents/web_agent.py#L6204) | 6204 | `"                clean_history,"` | — |
| [SRC-1AE03B9EC3-L006205](../../agents/web_agent.py#L6205) | 6205 | `"                sources,"` | — |
| [SRC-1AE03B9EC3-L006206](../../agents/web_agent.py#L6206) | 6206 | `"                search_warning,"` | — |
| [SRC-1AE03B9EC3-L006207](../../agents/web_agent.py#L6207) | 6207 | `"                research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L006208](../../agents/web_agent.py#L6208) | 6208 | `"                search_report=report,"` | — |
| [SRC-1AE03B9EC3-L006209](../../agents/web_agent.py#L6209) | 6209 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006210](../../agents/web_agent.py#L6210) | 6210 | `"            used_llm = True"` | — |
| [SRC-1AE03B9EC3-L006211](../../agents/web_agent.py#L6211) | 6211 | `"            if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L006212](../../agents/web_agent.py#L6212) | 6212 | `"                existing_urls = {item.get(\"url\") for item in sources}"` | — |
| [SRC-1AE03B9EC3-L006213](../../agents/web_agent.py#L6213) | 6213 | `"                relevance_queries = []"` | — |
| [SRC-1AE03B9EC3-L006214](../../agents/web_agent.py#L6214) | 6214 | `"                planned_queries = plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L006215](../../agents/web_agent.py#L6215) | 6215 | `"                if not isinstance(planned_queries, list):"` | — |
| [SRC-1AE03B9EC3-L006216](../../agents/web_agent.py#L6216) | 6216 | `"                    planned_queries = []"` | — |
| [SRC-1AE03B9EC3-L006217](../../agents/web_agent.py#L6217) | 6217 | `"                for candidate_query in [working_question, *planned_queries]:"` | — |
| [SRC-1AE03B9EC3-L006218](../../agents/web_agent.py#L6218) | 6218 | `"                    if not isinstance(candidate_query, str):"` | — |
| [SRC-1AE03B9EC3-L006219](../../agents/web_agent.py#L6219) | 6219 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L006220](../../agents/web_agent.py#L6220) | 6220 | `"                    compacted_query = compact_search_query(candidate_query)"` | — |
| [SRC-1AE03B9EC3-L006221](../../agents/web_agent.py#L6221) | 6221 | `"                    if compacted_query and compacted_query not in relevance_queries:"` | — |
| [SRC-1AE03B9EC3-L006222](../../agents/web_agent.py#L6222) | 6222 | `"                        relevance_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L006223](../../agents/web_agent.py#L6223) | 6223 | `"                for item in self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L006224](../../agents/web_agent.py#L6224) | 6224 | `"                    source_text = \" \".join(("` | — |
| [SRC-1AE03B9EC3-L006225](../../agents/web_agent.py#L6225) | 6225 | `"                        item.get(\"title\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L006226](../../agents/web_agent.py#L6226) | 6226 | `"                        item.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L006227](../../agents/web_agent.py#L6227) | 6227 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L006228](../../agents/web_agent.py#L6228) | 6228 | `"                    if ("` | — |
| [SRC-1AE03B9EC3-L006229](../../agents/web_agent.py#L6229) | 6229 | `"                        relevance_queries"` | — |
| [SRC-1AE03B9EC3-L006230](../../agents/web_agent.py#L6230) | 6230 | `"                        and item[\"url\"] not in existing_urls"` | — |
| [SRC-1AE03B9EC3-L006231](../../agents/web_agent.py#L6231) | 6231 | `"                        and not _blocked_source_url(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L006232](../../agents/web_agent.py#L6232) | 6232 | `"                        and any("` | — |
| [SRC-1AE03B9EC3-L006233](../../agents/web_agent.py#L6233) | 6233 | `"                            _relevance_ratio(candidate_query, source_text) >= 0.20"` | — |
| [SRC-1AE03B9EC3-L006234](../../agents/web_agent.py#L6234) | 6234 | `"                            for candidate_query in relevance_queries"` | — |
| [SRC-1AE03B9EC3-L006235](../../agents/web_agent.py#L6235) | 6235 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006236](../../agents/web_agent.py#L6236) | 6236 | `"                    ):"` | — |
| [SRC-1AE03B9EC3-L006237](../../agents/web_agent.py#L6237) | 6237 | `"                        sources.append(item)"` | — |
| [SRC-1AE03B9EC3-L006238](../../agents/web_agent.py#L6238) | 6238 | `"                        existing_urls.add(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L006239](../../agents/web_agent.py#L6239) | 6239 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006240](../../agents/web_agent.py#L6240) | 6240 | `"                provider_counts = dict(report.get(\"provider_counts\", {}))"` | — |
| [SRC-1AE03B9EC3-L006241](../../agents/web_agent.py#L6241) | 6241 | `"                provider_counts[\"openrouter_web_search\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L006242](../../agents/web_agent.py#L6242) | 6242 | `"                report[\"provider_counts\"] = provider_counts"` | — |
| [SRC-1AE03B9EC3-L006243](../../agents/web_agent.py#L6243) | 6243 | `"                providers_used = list(report.get(\"providers_used\", []))"` | — |
| [SRC-1AE03B9EC3-L006244](../../agents/web_agent.py#L6244) | 6244 | `"                if \"openrouter_web_search\" not in providers_used:"` | — |
| [SRC-1AE03B9EC3-L006245](../../agents/web_agent.py#L6245) | 6245 | `"                    providers_used.append(\"openrouter_web_search\")"` | — |
| [SRC-1AE03B9EC3-L006246](../../agents/web_agent.py#L6246) | 6246 | `"                report[\"providers_used\"] = providers_used"` | — |
| [SRC-1AE03B9EC3-L006247](../../agents/web_agent.py#L6247) | 6247 | `"                report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L006248](../../agents/web_agent.py#L6248) | 6248 | `"                    sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L006249](../../agents/web_agent.py#L6249) | 6249 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006250](../../agents/web_agent.py#L6250) | 6250 | `"        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L006251](../../agents/web_agent.py#L6251) | 6251 | `"            llm_warning = str(exc)"` | — |
| [SRC-1AE03B9EC3-L006252](../../agents/web_agent.py#L6252) | 6252 | `"            generation_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L006253](../../agents/web_agent.py#L6253) | 6253 | `"            if generation_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L006254](../../agents/web_agent.py#L6254) | 6254 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L006255](../../agents/web_agent.py#L6255) | 6255 | `"                    \"استُنفدت ميزانية محاولات النماذج قبل اكتمال الإجابة التحليلية. \""` | — |
| [SRC-1AE03B9EC3-L006256](../../agents/web_agent.py#L6256) | 6256 | `"                    \"أعرض مقتطفات المصادر المتاحة فقط، ولا أعتبر المهمة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L006257](../../agents/web_agent.py#L6257) | 6257 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006258](../../agents/web_agent.py#L6258) | 6258 | `"            elif not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L006259](../../agents/web_agent.py#L6259) | 6259 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L006260](../../agents/web_agent.py#L6260) | 6260 | `"                    \"تم البحث، لكن الفهم التوليدي غير مفعّل بعد. اضبط OPENROUTER_API_KEY \""` | — |
| [SRC-1AE03B9EC3-L006261](../../agents/web_agent.py#L6261) | 6261 | `"                    \"في Termux لتفعيل تخطيط البحث والإجابة باللغة الطبيعية.\""` | — |
| [SRC-1AE03B9EC3-L006262](../../agents/web_agent.py#L6262) | 6262 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006263](../../agents/web_agent.py#L6263) | 6263 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L006264](../../agents/web_agent.py#L6264) | 6264 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L006265](../../agents/web_agent.py#L6265) | 6265 | `"                    \"اكتمل البحث، لكن تعذر توليد إجابة تحليلية. أعرض لك مقتطفات المصادر \""` | — |
| [SRC-1AE03B9EC3-L006266](../../agents/web_agent.py#L6266) | 6266 | `"                    \"المتاحة بدلًا من اختلاق إجابة.\""` | — |
| [SRC-1AE03B9EC3-L006267](../../agents/web_agent.py#L6267) | 6267 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006268](../../agents/web_agent.py#L6268) | 6268 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L006269](../../agents/web_agent.py#L6269) | 6269 | `"                _fallback_lead_answer(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L006270](../../agents/web_agent.py#L6270) | 6270 | `"                if lead_request and lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L006271](../../agents/web_agent.py#L6271) | 6271 | `"                else _fallback_answer(sources, reason)"` | — |
| [SRC-1AE03B9EC3-L006272](../../agents/web_agent.py#L6272) | 6272 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006273](../../agents/web_agent.py#L6273) | 6273 | `""` | — |
| [SRC-1AE03B9EC3-L006274](../../agents/web_agent.py#L6274) | 6274 | `"        coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L006275](../../agents/web_agent.py#L6275) | 6275 | `"        coverage_repair_status = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L006276](../../agents/web_agent.py#L6276) | 6276 | `"        coverage_repair_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L006277](../../agents/web_agent.py#L6277) | 6277 | `"        review_status = \"not_run\""` | — |
| [SRC-1AE03B9EC3-L006278](../../agents/web_agent.py#L6278) | 6278 | `"        review_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L006279](../../agents/web_agent.py#L6279) | 6279 | `"        review_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L006280](../../agents/web_agent.py#L6280) | 6280 | `"        if used_llm and sources:"` | — |
| [SRC-1AE03B9EC3-L006281](../../agents/web_agent.py#L6281) | 6281 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L006282](../../agents/web_agent.py#L6282) | 6282 | `"                answer = self._review_answer(working_question, answer, sources[:MAX_LLM_CITED_SOURCES])"` | — |
| [SRC-1AE03B9EC3-L006283](../../agents/web_agent.py#L6283) | 6283 | `"                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006284](../../agents/web_agent.py#L6284) | 6284 | `"            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L006285](../../agents/web_agent.py#L6285) | 6285 | `"                review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006286](../../agents/web_agent.py#L6286) | 6286 | `"                review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L006287](../../agents/web_agent.py#L6287) | 6287 | `"                review_warning = ("` | — |
| [SRC-1AE03B9EC3-L006288](../../agents/web_agent.py#L6288) | 6288 | `"                    \"استُنفدت ميزانية النماذج قبل اكتمال تدقيق الإجابة؛ لذلك لن أعرض المسودة \""` | — |
| [SRC-1AE03B9EC3-L006289](../../agents/web_agent.py#L6289) | 6289 | `"                    \"بوصفها إجابة مكتملة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد عليها.\""` | — |
| [SRC-1AE03B9EC3-L006290](../../agents/web_agent.py#L6290) | 6290 | `"                    if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L006291](../../agents/web_agent.py#L6291) | 6291 | `"                    else"` | — |
| [SRC-1AE03B9EC3-L006292](../../agents/web_agent.py#L6292) | 6292 | `"                    \"تعذر تدقيق الادعاءات مقابل نصوص المصادر؛ لذلك لن أتعامل مع المسودة \""` | — |
| [SRC-1AE03B9EC3-L006293](../../agents/web_agent.py#L6293) | 6293 | `"                    \"كإجابة مؤكدة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد على المسودة.\""` | — |
| [SRC-1AE03B9EC3-L006294](../../agents/web_agent.py#L6294) | 6294 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006295](../../agents/web_agent.py#L6295) | 6295 | `"                answer = ("` | — |
| [SRC-1AE03B9EC3-L006296](../../agents/web_agent.py#L6296) | 6296 | `"                    _fallback_lead_answer(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L006297](../../agents/web_agent.py#L6297) | 6297 | `"                    if lead_request and lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L006298](../../agents/web_agent.py#L6298) | 6298 | `"                    else _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L006299](../../agents/web_agent.py#L6299) | 6299 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006300](../../agents/web_agent.py#L6300) | 6300 | `"        criterion_gap_research: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L006301](../../agents/web_agent.py#L6301) | 6301 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L006302](../../agents/web_agent.py#L6302) | 6302 | `"            \"status\": \"not_needed\","` | — |
| [SRC-1AE03B9EC3-L006303](../../agents/web_agent.py#L6303) | 6303 | `"            \"targets\": [],"` | — |
| [SRC-1AE03B9EC3-L006304](../../agents/web_agent.py#L6304) | 6304 | `"            \"new_sources_added\": 0,"` | — |
| [SRC-1AE03B9EC3-L006305](../../agents/web_agent.py#L6305) | 6305 | `"            \"evidence_sources_enriched\": 0,"` | — |
| [SRC-1AE03B9EC3-L006306](../../agents/web_agent.py#L6306) | 6306 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006307](../../agents/web_agent.py#L6307) | 6307 | `"        # Close the loop from an answer-stage gap back to the source layer. A criterion"` | — |
| [SRC-1AE03B9EC3-L006308](../../agents/web_agent.py#L6308) | 6308 | `"        # that appears in the draft but has no source signal triggers one bounded query"` | — |
| [SRC-1AE03B9EC3-L006309](../../agents/web_agent.py#L6309) | 6309 | `"        # when the reserved request-budget slot remains available."` | — |
| [SRC-1AE03B9EC3-L006310](../../agents/web_agent.py#L6310) | 6310 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L006311](../../agents/web_agent.py#L6311) | 6311 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L006312](../../agents/web_agent.py#L6312) | 6312 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006313](../../agents/web_agent.py#L6313) | 6313 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L006314](../../agents/web_agent.py#L6314) | 6314 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L006315](../../agents/web_agent.py#L6315) | 6315 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006316](../../agents/web_agent.py#L6316) | 6316 | `"            presearch_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets, plan.get(\"requirement_queries\"))"` | — |
| [SRC-1AE03B9EC3-L006317](../../agents/web_agent.py#L6317) | 6317 | `"            source_gap_targets = ["` | — |
| [SRC-1AE03B9EC3-L006318](../../agents/web_agent.py#L6318) | 6318 | `"                item[\"target\"]"` | — |
| [SRC-1AE03B9EC3-L006319](../../agents/web_agent.py#L6319) | 6319 | `"                for item in presearch_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L006320](../../agents/web_agent.py#L6320) | 6320 | `"                if item.get(\"source_evidence_status\") == \"no_source_lexical_signal\""` | — |
| [SRC-1AE03B9EC3-L006321](../../agents/web_agent.py#L6321) | 6321 | `"            ][:3]"` | — |
| [SRC-1AE03B9EC3-L006322](../../agents/web_agent.py#L6322) | 6322 | `"            if source_gap_targets:"` | — |
| [SRC-1AE03B9EC3-L006323](../../agents/web_agent.py#L6323) | 6323 | `"                criterion_gap_research[\"targets\"] = source_gap_targets"` | — |
| [SRC-1AE03B9EC3-L006324](../../agents/web_agent.py#L6324) | 6324 | `"                budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L006325](../../agents/web_agent.py#L6325) | 6325 | `"                if not plan.get(\"coverage_gap_repair_slot_reserved\"):"` | — |
| [SRC-1AE03B9EC3-L006326](../../agents/web_agent.py#L6326) | 6326 | `"                    criterion_gap_research[\"status\"] = \"skipped_no_reserved_search_slot\""` | — |
| [SRC-1AE03B9EC3-L006327](../../agents/web_agent.py#L6327) | 6327 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006328](../../agents/web_agent.py#L6328) | 6328 | `"                        \"رُصدت محاور بلا إشارة لفظية في المصادر، لكن لم تُحجز ميزانية \""` | — |
| [SRC-1AE03B9EC3-L006329](../../agents/web_agent.py#L6329) | 6329 | `"                        \"استعلام إضافي لهذه المهمة؛ لذلك ستظل المحاور غير المحسومة ظاهرة.\""` | — |
| [SRC-1AE03B9EC3-L006330](../../agents/web_agent.py#L6330) | 6330 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006331](../../agents/web_agent.py#L6331) | 6331 | `"                elif budget is None:"` | — |
| [SRC-1AE03B9EC3-L006332](../../agents/web_agent.py#L6332) | 6332 | `"                    criterion_gap_research[\"status\"] = \"skipped_no_request_budget\""` | — |
| [SRC-1AE03B9EC3-L006333](../../agents/web_agent.py#L6333) | 6333 | `"                elif budget.remaining_units(\"search_queries\") < 1:"` | — |
| [SRC-1AE03B9EC3-L006334](../../agents/web_agent.py#L6334) | 6334 | `"                    criterion_gap_research[\"status\"] = \"skipped_search_budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L006335](../../agents/web_agent.py#L6335) | 6335 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006336](../../agents/web_agent.py#L6336) | 6336 | `"                        \"رُصدت محاور بلا إشارة لفظية في المصادر، لكن ميزانية البحث لم تترك \""` | — |
| [SRC-1AE03B9EC3-L006337](../../agents/web_agent.py#L6337) | 6337 | `"                        \"استعلامًا إضافيًا للتحقق منها؛ لذلك لا تُعدّ الإجابة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L006338](../../agents/web_agent.py#L6338) | 6338 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006339](../../agents/web_agent.py#L6339) | 6339 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L006340](../../agents/web_agent.py#L6340) | 6340 | `"                    fallback_queries = fallback_plan(working_question, clean_history).get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L006341](../../agents/web_agent.py#L6341) | 6341 | `"                    topic_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L006342](../../agents/web_agent.py#L6342) | 6342 | `"                        fallback_queries[0] if fallback_queries else working_question"` | — |
| [SRC-1AE03B9EC3-L006343](../../agents/web_agent.py#L6343) | 6343 | `"                    ) or compact_search_query(working_question)"` | — |
| [SRC-1AE03B9EC3-L006344](../../agents/web_agent.py#L6344) | 6344 | `"                    gap_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L006345](../../agents/web_agent.py#L6345) | 6345 | `"                        f\"{topic_query} {' '.join(source_gap_targets)} official specific evidence data\""` | — |
| [SRC-1AE03B9EC3-L006346](../../agents/web_agent.py#L6346) | 6346 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006347](../../agents/web_agent.py#L6347) | 6347 | `"                    known_query_keys = {"` | — |
| [SRC-1AE03B9EC3-L006348](../../agents/web_agent.py#L6348) | 6348 | `"                        _normalize_search_query(item).casefold()"` | — |
| [SRC-1AE03B9EC3-L006349](../../agents/web_agent.py#L6349) | 6349 | `"                        for item in plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L006350](../../agents/web_agent.py#L6350) | 6350 | `"                        if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L006351](../../agents/web_agent.py#L6351) | 6351 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L006352](../../agents/web_agent.py#L6352) | 6352 | `"                    if not gap_query or not _relevance_query_tokens(gap_query):"` | — |
| [SRC-1AE03B9EC3-L006353](../../agents/web_agent.py#L6353) | 6353 | `"                        criterion_gap_research[\"status\"] = \"skipped_no_valid_query\""` | — |
| [SRC-1AE03B9EC3-L006354](../../agents/web_agent.py#L6354) | 6354 | `"                    elif _normalize_search_query(gap_query).casefold() in known_query_keys:"` | — |
| [SRC-1AE03B9EC3-L006355](../../agents/web_agent.py#L6355) | 6355 | `"                        criterion_gap_research[\"status\"] = \"skipped_query_not_distinct\""` | — |
| [SRC-1AE03B9EC3-L006356](../../agents/web_agent.py#L6356) | 6356 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L006357](../../agents/web_agent.py#L6357) | 6357 | `"                        criterion_gap_research.update({"` | — |
| [SRC-1AE03B9EC3-L006358](../../agents/web_agent.py#L6358) | 6358 | `"                            \"attempted\": True,"` | — |
| [SRC-1AE03B9EC3-L006359](../../agents/web_agent.py#L6359) | 6359 | `"                            \"status\": \"searching_for_missing_criterion_evidence\","` | — |
| [SRC-1AE03B9EC3-L006360](../../agents/web_agent.py#L6360) | 6360 | `"                            \"query\": gap_query,"` | — |
| [SRC-1AE03B9EC3-L006361](../../agents/web_agent.py#L6361) | 6361 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L006362](../../agents/web_agent.py#L6362) | 6362 | `"                        gap_plan = dict(plan)"` | — |
| [SRC-1AE03B9EC3-L006363](../../agents/web_agent.py#L6363) | 6363 | `"                        gap_plan.update({"` | — |
| [SRC-1AE03B9EC3-L006364](../../agents/web_agent.py#L6364) | 6364 | `"                            \"queries\": [gap_query],"` | — |
| [SRC-1AE03B9EC3-L006365](../../agents/web_agent.py#L6365) | 6365 | `"                            \"query_limit\": 1,"` | — |
| [SRC-1AE03B9EC3-L006366](../../agents/web_agent.py#L6366) | 6366 | `"                            \"depth\": \"standard\","` | — |
| [SRC-1AE03B9EC3-L006367](../../agents/web_agent.py#L6367) | 6367 | `"                            \"social_focus\": False,"` | — |
| [SRC-1AE03B9EC3-L006368](../../agents/web_agent.py#L6368) | 6368 | `"                            \"platforms\": [],"` | — |
| [SRC-1AE03B9EC3-L006369](../../agents/web_agent.py#L6369) | 6369 | `"                            \"direct_urls\": [],"` | — |
| [SRC-1AE03B9EC3-L006370](../../agents/web_agent.py#L6370) | 6370 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L006371](../../agents/web_agent.py#L6371) | 6371 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L006372](../../agents/web_agent.py#L6372) | 6372 | `"                            gap_sources, gap_warnings, gap_report = self._collect_research(gap_plan)"` | — |
| [SRC-1AE03B9EC3-L006373](../../agents/web_agent.py#L6373) | 6373 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L006374](../../agents/web_agent.py#L6374) | 6374 | `"                            gap_sources, gap_warnings = [], []"` | — |
| [SRC-1AE03B9EC3-L006375](../../agents/web_agent.py#L6375) | 6375 | `"                            gap_report = {"` | — |
| [SRC-1AE03B9EC3-L006376](../../agents/web_agent.py#L6376) | 6376 | `"                                \"queries_planned\": 1,"` | — |
| [SRC-1AE03B9EC3-L006377](../../agents/web_agent.py#L6377) | 6377 | `"                                \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L006378](../../agents/web_agent.py#L6378) | 6378 | `"                                \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L006379](../../agents/web_agent.py#L6379) | 6379 | `"                                \"search_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L006380](../../agents/web_agent.py#L6380) | 6380 | `"                                \"search_outcome\": \"unknown_after_research_error\","` | — |
| [SRC-1AE03B9EC3-L006381](../../agents/web_agent.py#L6381) | 6381 | `"                                \"query_results\": [],"` | — |
| [SRC-1AE03B9EC3-L006382](../../agents/web_agent.py#L6382) | 6382 | `"                            }"` | — |
| [SRC-1AE03B9EC3-L006383](../../agents/web_agent.py#L6383) | 6383 | `"                            criterion_gap_research[\"status\"] = \"search_failed\""` | — |
| [SRC-1AE03B9EC3-L006384](../../agents/web_agent.py#L6384) | 6384 | `"                            criterion_gap_research[\"error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L006385](../../agents/web_agent.py#L6385) | 6385 | `"                        search_warnings.extend("` | — |
| [SRC-1AE03B9EC3-L006386](../../agents/web_agent.py#L6386) | 6386 | `"                            item for item in gap_warnings if isinstance(item, str)"` | — |
| [SRC-1AE03B9EC3-L006387](../../agents/web_agent.py#L6387) | 6387 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006388](../../agents/web_agent.py#L6388) | 6388 | `"                        source_indexes: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L006389](../../agents/web_agent.py#L6389) | 6389 | `"                        for source_index, source in enumerate(sources):"` | — |
| [SRC-1AE03B9EC3-L006390](../../agents/web_agent.py#L6390) | 6390 | `"                            source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L006391](../../agents/web_agent.py#L6391) | 6391 | `"                            if source_key:"` | — |
| [SRC-1AE03B9EC3-L006392](../../agents/web_agent.py#L6392) | 6392 | `"                                source_indexes.setdefault(source_key, source_index)"` | — |
| [SRC-1AE03B9EC3-L006393](../../agents/web_agent.py#L6393) | 6393 | `"                        # A criterion-gap search is a second retrieval path, not a"` | — |
| [SRC-1AE03B9EC3-L006394](../../agents/web_agent.py#L6394) | 6394 | `"                        # trusted bypass. Apply the same task-specific source policy before"` | — |
| [SRC-1AE03B9EC3-L006395](../../agents/web_agent.py#L6395) | 6395 | `"                        # merging candidates into the evidence set or regenerating an answer."` | — |
| [SRC-1AE03B9EC3-L006396](../../agents/web_agent.py#L6396) | 6396 | `"                        pre_gap_source_keys = set(source_indexes)"` | — |
| [SRC-1AE03B9EC3-L006397](../../agents/web_agent.py#L6397) | 6397 | `"                        gap_sources_before_guardrails = len(gap_sources)"` | — |
| [SRC-1AE03B9EC3-L006398](../../agents/web_agent.py#L6398) | 6398 | `"                        gap_sources, gap_guardrail_report = apply_source_guardrails("` | — |
| [SRC-1AE03B9EC3-L006399](../../agents/web_agent.py#L6399) | 6399 | `"                            working_question, clean_mode, plan, gap_sources"` | — |
| [SRC-1AE03B9EC3-L006400](../../agents/web_agent.py#L6400) | 6400 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006401](../../agents/web_agent.py#L6401) | 6401 | `"                        report.setdefault(\"source_guardrails\", {})["` | — |
| [SRC-1AE03B9EC3-L006402](../../agents/web_agent.py#L6402) | 6402 | `"                            \"criterion_gap_repair\""` | — |
| [SRC-1AE03B9EC3-L006403](../../agents/web_agent.py#L6403) | 6403 | `"                        ] = {"` | — |
| [SRC-1AE03B9EC3-L006404](../../agents/web_agent.py#L6404) | 6404 | `"                            **gap_guardrail_report,"` | — |
| [SRC-1AE03B9EC3-L006405](../../agents/web_agent.py#L6405) | 6405 | `"                            \"candidates_before_filter\": gap_sources_before_guardrails,"` | — |
| [SRC-1AE03B9EC3-L006406](../../agents/web_agent.py#L6406) | 6406 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L006407](../../agents/web_agent.py#L6407) | 6407 | `"                        if gap_guardrail_report[\"rejected_sources\"]:"` | — |
| [SRC-1AE03B9EC3-L006408](../../agents/web_agent.py#L6408) | 6408 | `"                            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L006409](../../agents/web_agent.py#L6409) | 6409 | `"                                \"رُفضت بعض نتائج البحث الإضافي لأنها لم تستوفِ شروط قبول \""` | — |
| [SRC-1AE03B9EC3-L006410](../../agents/web_agent.py#L6410) | 6410 | `"                                \"الأدلة الخاصة بالسؤال.\""` | — |
| [SRC-1AE03B9EC3-L006411](../../agents/web_agent.py#L6411) | 6411 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006412](../../agents/web_agent.py#L6412) | 6412 | `"                        evidence_updated = False"` | — |
| [SRC-1AE03B9EC3-L006413](../../agents/web_agent.py#L6413) | 6413 | `"                        for candidate in gap_sources:"` | — |
| [SRC-1AE03B9EC3-L006414](../../agents/web_agent.py#L6414) | 6414 | `"                            if not isinstance(candidate, dict):"` | — |
| [SRC-1AE03B9EC3-L006415](../../agents/web_agent.py#L6415) | 6415 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L006416](../../agents/web_agent.py#L6416) | 6416 | `"                            if not self._source_matches_query(gap_query, candidate):"` | — |
| [SRC-1AE03B9EC3-L006417](../../agents/web_agent.py#L6417) | 6417 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L006418](../../agents/web_agent.py#L6418) | 6418 | `"                            source_key = self._normalized_source_url_key(candidate.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L006419](../../agents/web_agent.py#L6419) | 6419 | `"                            if not source_key:"` | — |
| [SRC-1AE03B9EC3-L006420](../../agents/web_agent.py#L6420) | 6420 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L006421](../../agents/web_agent.py#L6421) | 6421 | `"                            existing_index = source_indexes.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L006422](../../agents/web_agent.py#L6422) | 6422 | `"                            if existing_index is None:"` | — |
| [SRC-1AE03B9EC3-L006423](../../agents/web_agent.py#L6423) | 6423 | `"                                source_indexes[source_key] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006424](../../agents/web_agent.py#L6424) | 6424 | `"                                sources.append(candidate)"` | — |
| [SRC-1AE03B9EC3-L006425](../../agents/web_agent.py#L6425) | 6425 | `"                                criterion_gap_research[\"new_sources_added\"] += 1"` | — |
| [SRC-1AE03B9EC3-L006426](../../agents/web_agent.py#L6426) | 6426 | `"                                evidence_updated = True"` | — |
| [SRC-1AE03B9EC3-L006427](../../agents/web_agent.py#L6427) | 6427 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L006428](../../agents/web_agent.py#L6428) | 6428 | `"                            existing_source = sources[existing_index]"` | — |
| [SRC-1AE03B9EC3-L006429](../../agents/web_agent.py#L6429) | 6429 | `"                            merged = dict(existing_source)"` | — |
| [SRC-1AE03B9EC3-L006430](../../agents/web_agent.py#L6430) | 6430 | `"                            source_enriched = False"` | — |
| [SRC-1AE03B9EC3-L006431](../../agents/web_agent.py#L6431) | 6431 | `"                            for text_key in (\"title\", \"snippet\", \"page_text\"):"` | — |
| [SRC-1AE03B9EC3-L006432](../../agents/web_agent.py#L6432) | 6432 | `"                                old_text = str(merged.get(text_key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L006433](../../agents/web_agent.py#L6433) | 6433 | `"                                new_text = str(candidate.get(text_key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L006434](../../agents/web_agent.py#L6434) | 6434 | `"                                if len(new_text) > len(old_text):"` | — |
| [SRC-1AE03B9EC3-L006435](../../agents/web_agent.py#L6435) | 6435 | `"                                    merged[text_key] = candidate[text_key]"` | — |
| [SRC-1AE03B9EC3-L006436](../../agents/web_agent.py#L6436) | 6436 | `"                                    source_enriched = True"` | — |
| [SRC-1AE03B9EC3-L006437](../../agents/web_agent.py#L6437) | 6437 | `"                            if candidate.get(\"page_fetched\") and not existing_source.get(\"page_fetched\"):"` | — |
| [SRC-1AE03B9EC3-L006438](../../agents/web_agent.py#L6438) | 6438 | `"                                merged[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L006439](../../agents/web_agent.py#L6439) | 6439 | `"                                source_enriched = True"` | — |
| [SRC-1AE03B9EC3-L006440](../../agents/web_agent.py#L6440) | 6440 | `"                            if source_enriched:"` | — |
| [SRC-1AE03B9EC3-L006441](../../agents/web_agent.py#L6441) | 6441 | `"                                evidence_updated = True"` | — |
| [SRC-1AE03B9EC3-L006442](../../agents/web_agent.py#L6442) | 6442 | `"                                criterion_gap_research[\"evidence_sources_enriched\"] += 1"` | — |
| [SRC-1AE03B9EC3-L006443](../../agents/web_agent.py#L6443) | 6443 | `"                            merged[\"providers\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L006444](../../agents/web_agent.py#L6444) | 6444 | `"                                list(existing_source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L006445](../../agents/web_agent.py#L6445) | 6445 | `"                                + list(candidate.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L006446](../../agents/web_agent.py#L6446) | 6446 | `"                            ))"` | — |
| [SRC-1AE03B9EC3-L006447](../../agents/web_agent.py#L6447) | 6447 | `"                            merged[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L006448](../../agents/web_agent.py#L6448) | 6448 | `"                                list(existing_source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L006449](../../agents/web_agent.py#L6449) | 6449 | `"                                + list(candidate.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L006450](../../agents/web_agent.py#L6450) | 6450 | `"                                + [gap_query]"` | — |
| [SRC-1AE03B9EC3-L006451](../../agents/web_agent.py#L6451) | 6451 | `"                            ))"` | — |
| [SRC-1AE03B9EC3-L006452](../../agents/web_agent.py#L6452) | 6452 | `"                            sources[existing_index] = merged"` | — |
| [SRC-1AE03B9EC3-L006453](../../agents/web_agent.py#L6453) | 6453 | `"                        # Re-apply the guardrails to the merged set as a final safety"` | — |
| [SRC-1AE03B9EC3-L006454](../../agents/web_agent.py#L6454) | 6454 | `"                        # boundary. Count newly added sources only after this filter."` | — |
| [SRC-1AE03B9EC3-L006455](../../agents/web_agent.py#L6455) | 6455 | `"                        sources, merged_guardrail_report = apply_source_guardrails("` | — |
| [SRC-1AE03B9EC3-L006456](../../agents/web_agent.py#L6456) | 6456 | `"                            working_question, clean_mode, plan, sources"` | — |
| [SRC-1AE03B9EC3-L006457](../../agents/web_agent.py#L6457) | 6457 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006458](../../agents/web_agent.py#L6458) | 6458 | `"                        report[\"source_guardrails\"][\"after_criterion_gap_repair\"] = ("` | — |
| [SRC-1AE03B9EC3-L006459](../../agents/web_agent.py#L6459) | 6459 | `"                            merged_guardrail_report"` | — |
| [SRC-1AE03B9EC3-L006460](../../agents/web_agent.py#L6460) | 6460 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006461](../../agents/web_agent.py#L6461) | 6461 | `"                        accepted_source_keys = {"` | — |
| [SRC-1AE03B9EC3-L006462](../../agents/web_agent.py#L6462) | 6462 | `"                            self._normalized_source_url_key(item.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L006463](../../agents/web_agent.py#L6463) | 6463 | `"                            for item in sources"` | — |
| [SRC-1AE03B9EC3-L006464](../../agents/web_agent.py#L6464) | 6464 | `"                            if self._normalized_source_url_key(item.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L006465](../../agents/web_agent.py#L6465) | 6465 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L006466](../../agents/web_agent.py#L6466) | 6466 | `"                        criterion_gap_research[\"new_sources_added\"] = len("` | — |
| [SRC-1AE03B9EC3-L006467](../../agents/web_agent.py#L6467) | 6467 | `"                            accepted_source_keys - pre_gap_source_keys"` | — |
| [SRC-1AE03B9EC3-L006468](../../agents/web_agent.py#L6468) | 6468 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006469](../../agents/web_agent.py#L6469) | 6469 | `"                        criterion_gap_research[\"source_count_after\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006470](../../agents/web_agent.py#L6470) | 6470 | `"                        plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L006471](../../agents/web_agent.py#L6471) | 6471 | `"                            list(plan.get(\"queries\", [])) + [gap_query]"` | — |
| [SRC-1AE03B9EC3-L006472](../../agents/web_agent.py#L6472) | 6472 | `"                        ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L006473](../../agents/web_agent.py#L6473) | 6473 | `"                        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L006474](../../agents/web_agent.py#L6474) | 6474 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L006475](../../agents/web_agent.py#L6475) | 6475 | `"                            report[\"queries_planned\"] = max("` | — |
| [SRC-1AE03B9EC3-L006476](../../agents/web_agent.py#L6476) | 6476 | `"                                0, int(report.get(\"queries_planned\", 0) or 0)"` | — |
| [SRC-1AE03B9EC3-L006477](../../agents/web_agent.py#L6477) | 6477 | `"                            ) + max(0, int(gap_report.get(\"queries_planned\", 1) or 0))"` | — |
| [SRC-1AE03B9EC3-L006478](../../agents/web_agent.py#L6478) | 6478 | `"                        except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L006479](../../agents/web_agent.py#L6479) | 6479 | `"                            report[\"queries_planned\"] = None"` | — |
| [SRC-1AE03B9EC3-L006480](../../agents/web_agent.py#L6480) | 6480 | `"                        previous_attempts = report.get(\"queries_attempted\")"` | — |
| [SRC-1AE03B9EC3-L006481](../../agents/web_agent.py#L6481) | 6481 | `"                        extra_attempts = gap_report.get(\"queries_attempted\")"` | — |
| [SRC-1AE03B9EC3-L006482](../../agents/web_agent.py#L6482) | 6482 | `"                        if isinstance(previous_attempts, int) and isinstance(extra_attempts, int):"` | — |
| [SRC-1AE03B9EC3-L006483](../../agents/web_agent.py#L6483) | 6483 | `"                            report[\"queries_attempted\"] = max(0, previous_attempts) + max(0, extra_attempts)"` | — |
| [SRC-1AE03B9EC3-L006484](../../agents/web_agent.py#L6484) | 6484 | `"                            report[\"queries_attempted_known\"] = True"` | — |
| [SRC-1AE03B9EC3-L006485](../../agents/web_agent.py#L6485) | 6485 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L006486](../../agents/web_agent.py#L6486) | 6486 | `"                            report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L006487](../../agents/web_agent.py#L6487) | 6487 | `"                            report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L006488](../../agents/web_agent.py#L6488) | 6488 | `"                        old_query_results = report.get(\"query_results\")"` | — |
| [SRC-1AE03B9EC3-L006489](../../agents/web_agent.py#L6489) | 6489 | `"                        new_query_results = gap_report.get(\"query_results\")"` | — |
| [SRC-1AE03B9EC3-L006490](../../agents/web_agent.py#L6490) | 6490 | `"                        report[\"query_results\"] = ("` | — |
| [SRC-1AE03B9EC3-L006491](../../agents/web_agent.py#L6491) | 6491 | `"                            (old_query_results if isinstance(old_query_results, list) else [])"` | — |
| [SRC-1AE03B9EC3-L006492](../../agents/web_agent.py#L6492) | 6492 | `"                            + (new_query_results if isinstance(new_query_results, list) else [])"` | — |
| [SRC-1AE03B9EC3-L006493](../../agents/web_agent.py#L6493) | 6493 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006494](../../agents/web_agent.py#L6494) | 6494 | `"                        if evidence_updated:"` | — |
| [SRC-1AE03B9EC3-L006495](../../agents/web_agent.py#L6495) | 6495 | `"                            sources.sort("` | — |
| [SRC-1AE03B9EC3-L006496](../../agents/web_agent.py#L6496) | 6496 | `"                                key=lambda item: float(item.get(\"rank_score\", 0) or 0),"` | — |
| [SRC-1AE03B9EC3-L006497](../../agents/web_agent.py#L6497) | 6497 | `"                                reverse=True,"` | — |
| [SRC-1AE03B9EC3-L006498](../../agents/web_agent.py#L6498) | 6498 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006499](../../agents/web_agent.py#L6499) | 6499 | `"                            try:"` | — |
| [SRC-1AE03B9EC3-L006500](../../agents/web_agent.py#L6500) | 6500 | `"                                revised_draft = self._generate("` | — |
| [SRC-1AE03B9EC3-L006501](../../agents/web_agent.py#L6501) | 6501 | `"                                    working_question,"` | — |
| [SRC-1AE03B9EC3-L006502](../../agents/web_agent.py#L6502) | 6502 | `"                                    clean_history,"` | — |
| [SRC-1AE03B9EC3-L006503](../../agents/web_agent.py#L6503) | 6503 | `"                                    sources,"` | — |
| [SRC-1AE03B9EC3-L006504](../../agents/web_agent.py#L6504) | 6504 | `"                                    search_warning,"` | — |
| [SRC-1AE03B9EC3-L006505](../../agents/web_agent.py#L6505) | 6505 | `"                                    research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L006506](../../agents/web_agent.py#L6506) | 6506 | `"                                    search_report=report,"` | — |
| [SRC-1AE03B9EC3-L006507](../../agents/web_agent.py#L6507) | 6507 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L006508](../../agents/web_agent.py#L6508) | 6508 | `"                                revised_answer = self._review_answer("` | — |
| [SRC-1AE03B9EC3-L006509](../../agents/web_agent.py#L6509) | 6509 | `"                                    working_question, revised_draft, sources[:MAX_LLM_CITED_SOURCES]"` | — |
| [SRC-1AE03B9EC3-L006510](../../agents/web_agent.py#L6510) | 6510 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L006511](../../agents/web_agent.py#L6511) | 6511 | `"                                answer = revised_answer"` | — |
| [SRC-1AE03B9EC3-L006512](../../agents/web_agent.py#L6512) | 6512 | `"                                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006513](../../agents/web_agent.py#L6513) | 6513 | `"                                criterion_gap_research[\"status\"] = \"evidence_added_and_answer_regenerated\""` | — |
| [SRC-1AE03B9EC3-L006514](../../agents/web_agent.py#L6514) | 6514 | `"                            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L006515](../../agents/web_agent.py#L6515) | 6515 | `"                                criterion_gap_research[\"status\"] = \"evidence_added_but_regeneration_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006516](../../agents/web_agent.py#L6516) | 6516 | `"                                criterion_gap_research[\"regeneration_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L006517](../../agents/web_agent.py#L6517) | 6517 | `"                                coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006518](../../agents/web_agent.py#L6518) | 6518 | `"                                    \"وصلت أدلة إضافية لمحور مطلوب، لكن تعذرت إعادة توليد الإجابة \""` | — |
| [SRC-1AE03B9EC3-L006519](../../agents/web_agent.py#L6519) | 6519 | `"                                    \"وتدقيقها ضمن الميزانية؛ راجع هذا المحور قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L006520](../../agents/web_agent.py#L6520) | 6520 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L006521](../../agents/web_agent.py#L6521) | 6521 | `"                        elif criterion_gap_research.get(\"status\") != \"search_failed\":"` | — |
| [SRC-1AE03B9EC3-L006522](../../agents/web_agent.py#L6522) | 6522 | `"                            criterion_gap_research[\"status\"] = \"search_completed_no_new_criterion_evidence\""` | — |
| [SRC-1AE03B9EC3-L006523](../../agents/web_agent.py#L6523) | 6523 | `"                            coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006524](../../agents/web_agent.py#L6524) | 6524 | `"                                \"أُجري بحث إضافي لمحاور ناقصة، لكنه لم يضف نص مصدر يمكن تمييزه \""` | — |
| [SRC-1AE03B9EC3-L006525](../../agents/web_agent.py#L6525) | 6525 | `"                                \"كدليل جديد؛ ستظل هذه المحاور غير محسومة.\""` | — |
| [SRC-1AE03B9EC3-L006526](../../agents/web_agent.py#L6526) | 6526 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006527](../../agents/web_agent.py#L6527) | 6527 | `"                        criterion_gap_research[\"source_count_after\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006528](../../agents/web_agent.py#L6528) | 6528 | `"                        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L006529](../../agents/web_agent.py#L6529) | 6529 | `""` | — |
| [SRC-1AE03B9EC3-L006530](../../agents/web_agent.py#L6530) | 6530 | `"        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L006531](../../agents/web_agent.py#L6531) | 6531 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L006532](../../agents/web_agent.py#L6532) | 6532 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L006533](../../agents/web_agent.py#L6533) | 6533 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006534](../../agents/web_agent.py#L6534) | 6534 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L006535](../../agents/web_agent.py#L6535) | 6535 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L006536](../../agents/web_agent.py#L6536) | 6536 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006537](../../agents/web_agent.py#L6537) | 6537 | `"            initial_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets, plan.get(\"requirement_queries\"))"` | — |
| [SRC-1AE03B9EC3-L006538](../../agents/web_agent.py#L6538) | 6538 | `"            missing_targets = ["` | — |
| [SRC-1AE03B9EC3-L006539](../../agents/web_agent.py#L6539) | 6539 | `"                item[\"target\"] for item in initial_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L006540](../../agents/web_agent.py#L6540) | 6540 | `"                if item[\"status\"] == \"possibly_missing\""` | — |
| [SRC-1AE03B9EC3-L006541](../../agents/web_agent.py#L6541) | 6541 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L006542](../../agents/web_agent.py#L6542) | 6542 | `"            remaining_source_gap_targets = ["` | — |
| [SRC-1AE03B9EC3-L006543](../../agents/web_agent.py#L6543) | 6543 | `"                item[\"target\"] for item in initial_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L006544](../../agents/web_agent.py#L6544) | 6544 | `"                if item.get(\"source_evidence_status\") == \"no_source_lexical_signal\""` | — |
| [SRC-1AE03B9EC3-L006545](../../agents/web_agent.py#L6545) | 6545 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L006546](../../agents/web_agent.py#L6546) | 6546 | `"            if not missing_targets and remaining_source_gap_targets:"` | — |
| [SRC-1AE03B9EC3-L006547](../../agents/web_agent.py#L6547) | 6547 | `"                coverage_repair_status = \"source_evidence_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L006548](../../agents/web_agent.py#L6548) | 6548 | `"                if not coverage_repair_warning:"` | — |
| [SRC-1AE03B9EC3-L006549](../../agents/web_agent.py#L6549) | 6549 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006550](../../agents/web_agent.py#L6550) | 6550 | `"                        \"ذُكرت المحاور في الإجابة، لكن لم تظهر لها إشارات لفظية في المصادر؛ \""` | — |
| [SRC-1AE03B9EC3-L006551](../../agents/web_agent.py#L6551) | 6551 | `"                        \"ذكر المحور لا يُعد دليلًا، لذلك تظل المهمة غير مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L006552](../../agents/web_agent.py#L6552) | 6552 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006553](../../agents/web_agent.py#L6553) | 6553 | `"            elif not missing_targets:"` | — |
| [SRC-1AE03B9EC3-L006554](../../agents/web_agent.py#L6554) | 6554 | `"                coverage_repair_status = \"not_needed_lexical_signals_found\""` | — |
| [SRC-1AE03B9EC3-L006555](../../agents/web_agent.py#L6555) | 6555 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L006556](../../agents/web_agent.py#L6556) | 6556 | `"                coverage_repair_status = \"attempted\""` | — |
| [SRC-1AE03B9EC3-L006557](../../agents/web_agent.py#L6557) | 6557 | `"                try:"` | — |
| [SRC-1AE03B9EC3-L006558](../../agents/web_agent.py#L6558) | 6558 | `"                    repaired_answer = self._repair_answer_coverage("` | — |
| [SRC-1AE03B9EC3-L006559](../../agents/web_agent.py#L6559) | 6559 | `"                        working_question, answer, sources, missing_targets"` | — |
| [SRC-1AE03B9EC3-L006560](../../agents/web_agent.py#L6560) | 6560 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006561](../../agents/web_agent.py#L6561) | 6561 | `"                    if repaired_answer.strip() != answer.strip():"` | — |
| [SRC-1AE03B9EC3-L006562](../../agents/web_agent.py#L6562) | 6562 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L006563](../../agents/web_agent.py#L6563) | 6563 | `"                            reaudit_answer = self._review_answer("` | — |
| [SRC-1AE03B9EC3-L006564](../../agents/web_agent.py#L6564) | 6564 | `"                                working_question,"` | — |
| [SRC-1AE03B9EC3-L006565](../../agents/web_agent.py#L6565) | 6565 | `"                                repaired_answer,"` | — |
| [SRC-1AE03B9EC3-L006566](../../agents/web_agent.py#L6566) | 6566 | `"                                sources[:MAX_LLM_CITED_SOURCES],"` | — |
| [SRC-1AE03B9EC3-L006567](../../agents/web_agent.py#L6567) | 6567 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006568](../../agents/web_agent.py#L6568) | 6568 | `"                            answer = reaudit_answer"` | — |
| [SRC-1AE03B9EC3-L006569](../../agents/web_agent.py#L6569) | 6569 | `"                            reaudit_integrity = audit_answer_integrity("` | — |
| [SRC-1AE03B9EC3-L006570](../../agents/web_agent.py#L6570) | 6570 | `"                                question, answer, sources, coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L006571](../../agents/web_agent.py#L6571) | 6571 | `"                                plan.get(\"requirement_queries\"),"` | — |
| [SRC-1AE03B9EC3-L006572](../../agents/web_agent.py#L6572) | 6572 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006573](../../agents/web_agent.py#L6573) | 6573 | `"                            if reaudit_integrity[\"potentially_missing_target_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L006574](../../agents/web_agent.py#L6574) | 6574 | `"                                coverage_repair_status = \"revised_and_reaudited_remaining_gaps\""` | — |
| [SRC-1AE03B9EC3-L006575](../../agents/web_agent.py#L6575) | 6575 | `"                                coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006576](../../agents/web_agent.py#L6576) | 6576 | `"                                    \"خضعت الإجابة المعدلة لمراجعة ثانية، لكن الفحص اللفظي ما زال يرصد محورًا محتمل النقص؛ \""` | — |
| [SRC-1AE03B9EC3-L006577](../../agents/web_agent.py#L6577) | 6577 | `"                                    \"لا تعتبر المهمة مكتملة دون مراجعة هذا المحور والأدلة الأصلية.\""` | — |
| [SRC-1AE03B9EC3-L006578](../../agents/web_agent.py#L6578) | 6578 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L006579](../../agents/web_agent.py#L6579) | 6579 | `"                            else:"` | — |
| [SRC-1AE03B9EC3-L006580](../../agents/web_agent.py#L6580) | 6580 | `"                                coverage_repair_status = \"revised_and_reaudited\""` | — |
| [SRC-1AE03B9EC3-L006581](../../agents/web_agent.py#L6581) | 6581 | `"                            review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006582](../../agents/web_agent.py#L6582) | 6582 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L006583](../../agents/web_agent.py#L6583) | 6583 | `"                            review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006584](../../agents/web_agent.py#L6584) | 6584 | `"                            review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L006585](../../agents/web_agent.py#L6585) | 6585 | `"                            coverage_repair_status = ("` | — |
| [SRC-1AE03B9EC3-L006586](../../agents/web_agent.py#L6586) | 6586 | `"                                \"reaudit_budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L006587](../../agents/web_agent.py#L6587) | 6587 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L006588](../../agents/web_agent.py#L6588) | 6588 | `"                                else \"reaudit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006589](../../agents/web_agent.py#L6589) | 6589 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006590](../../agents/web_agent.py#L6590) | 6590 | `"                            review_warning = ("` | — |
| [SRC-1AE03B9EC3-L006591](../../agents/web_agent.py#L6591) | 6591 | `"                                \"استُنفدت ميزانية النماذج قبل إعادة تدقيق الإجابة المعدلة؛ \""` | — |
| [SRC-1AE03B9EC3-L006592](../../agents/web_agent.py#L6592) | 6592 | `"                                \"لذلك لن أعرض النص المعدل بوصفه إجابة مكتملة، وأعرض مقتطفات المصادر بدلًا منه.\""` | — |
| [SRC-1AE03B9EC3-L006593](../../agents/web_agent.py#L6593) | 6593 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L006594](../../agents/web_agent.py#L6594) | 6594 | `"                                else"` | — |
| [SRC-1AE03B9EC3-L006595](../../agents/web_agent.py#L6595) | 6595 | `"                                \"تعذرت إعادة تدقيق الإجابة المعدلة مقابل الأدلة؛ لذلك لن أعرضها بوصفها إجابة مكتملة، \""` | — |
| [SRC-1AE03B9EC3-L006596](../../agents/web_agent.py#L6596) | 6596 | `"                                \"وأعرض مقتطفات المصادر بدلًا منها.\""` | — |
| [SRC-1AE03B9EC3-L006597](../../agents/web_agent.py#L6597) | 6597 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006598](../../agents/web_agent.py#L6598) | 6598 | `"                            answer = ("` | — |
| [SRC-1AE03B9EC3-L006599](../../agents/web_agent.py#L6599) | 6599 | `"                                _fallback_lead_answer(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L006600](../../agents/web_agent.py#L6600) | 6600 | `"                                if lead_request and lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L006601](../../agents/web_agent.py#L6601) | 6601 | `"                                else _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L006602](../../agents/web_agent.py#L6602) | 6602 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006603](../../agents/web_agent.py#L6603) | 6603 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L006604](../../agents/web_agent.py#L6604) | 6604 | `"                        coverage_repair_status = \"no_change_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L006605](../../agents/web_agent.py#L6605) | 6605 | `"                        coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006606](../../agents/web_agent.py#L6606) | 6606 | `"                            \"رصد الفحص اللفظي محورًا قد يكون ناقصًا، لكن محاولة الإصلاح لم تغيّر الإجابة؛ \""` | — |
| [SRC-1AE03B9EC3-L006607](../../agents/web_agent.py#L6607) | 6607 | `"                            \"تحقق من تغطية هذا المحور يدويًا.\""` | — |
| [SRC-1AE03B9EC3-L006608](../../agents/web_agent.py#L6608) | 6608 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006609](../../agents/web_agent.py#L6609) | 6609 | `"                except RequestBudgetExceeded:"` | — |
| [SRC-1AE03B9EC3-L006610](../../agents/web_agent.py#L6610) | 6610 | `"                    coverage_repair_status = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L006611](../../agents/web_agent.py#L6611) | 6611 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006612](../../agents/web_agent.py#L6612) | 6612 | `"                        \"استُنفدت ميزانية النماذج قبل محاولة إصلاح محور قد يكون ناقصًا؛ \""` | — |
| [SRC-1AE03B9EC3-L006613](../../agents/web_agent.py#L6613) | 6613 | `"                        \"لا تعتبر التغطية مكتملة دون مراجعة المحور المذكور.\""` | — |
| [SRC-1AE03B9EC3-L006614](../../agents/web_agent.py#L6614) | 6614 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006615](../../agents/web_agent.py#L6615) | 6615 | `"                except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L006616](../../agents/web_agent.py#L6616) | 6616 | `"                    coverage_repair_status = \"unavailable\""` | — |
| [SRC-1AE03B9EC3-L006617](../../agents/web_agent.py#L6617) | 6617 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006618](../../agents/web_agent.py#L6618) | 6618 | `"                        \"تعذرت محاولة إصلاح محور قد يكون ناقصًا (\""` | — |
| [SRC-1AE03B9EC3-L006619](../../agents/web_agent.py#L6619) | 6619 | `"                        + type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L006620](../../agents/web_agent.py#L6620) | 6620 | `"                        + \")؛ راجع المحاور المطلوبة قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L006621](../../agents/web_agent.py#L6621) | 6621 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006622](../../agents/web_agent.py#L6622) | 6622 | `"        elif coverage_targets and review_status == \"model_claim_audit_completed\" and not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L006623](../../agents/web_agent.py#L6623) | 6623 | `"            coverage_repair_status = \"skipped_no_model_configuration\""` | — |
| [SRC-1AE03B9EC3-L006624](../../agents/web_agent.py#L6624) | 6624 | `"        elif coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L006625](../../agents/web_agent.py#L6625) | 6625 | `"            coverage_repair_status = \"skipped_review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006626](../../agents/web_agent.py#L6626) | 6626 | `""` | — |
| [SRC-1AE03B9EC3-L006627](../../agents/web_agent.py#L6627) | 6627 | `"        if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L006628](../../agents/web_agent.py#L6628) | 6628 | `"            answer += \"\\n\\nروابط إضافية من البحث المباشر عبر الويب:\""` | — |
| [SRC-1AE03B9EC3-L006629](../../agents/web_agent.py#L6629) | 6629 | `"            for source in self.server_search_sources[:8]:"` | — |
| [SRC-1AE03B9EC3-L006630](../../agents/web_agent.py#L6630) | 6630 | `"                answer += \"\\n- \" + source[\"title\"] + \" — \" + source[\"url\"]"` | — |
| [SRC-1AE03B9EC3-L006631](../../agents/web_agent.py#L6631) | 6631 | `"        max_citable_sources = min(MAX_LLM_CITED_SOURCES, len(sources))"` | — |
| [SRC-1AE03B9EC3-L006632](../../agents/web_agent.py#L6632) | 6632 | `"        answer, citation_warnings = self._remove_invalid_citations("` | — |
| [SRC-1AE03B9EC3-L006633](../../agents/web_agent.py#L6633) | 6633 | `"            answer, max_citable_sources"` | — |
| [SRC-1AE03B9EC3-L006634](../../agents/web_agent.py#L6634) | 6634 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006635](../../agents/web_agent.py#L6635) | 6635 | `"        citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L006636](../../agents/web_agent.py#L6636) | 6636 | `"            answer, max_citable_sources, citation_warnings, review_status"` | — |
| [SRC-1AE03B9EC3-L006637](../../agents/web_agent.py#L6637) | 6637 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006638](../../agents/web_agent.py#L6638) | 6638 | `"        semantic_claim_verification: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L006639](../../agents/web_agent.py#L6639) | 6639 | `"            \"status\": \"not_run_review_unavailable\","` | — |
| [SRC-1AE03B9EC3-L006640](../../agents/web_agent.py#L6640) | 6640 | `"            \"withhold_answer\": False,"` | — |
| [SRC-1AE03B9EC3-L006641](../../agents/web_agent.py#L6641) | 6641 | `"            \"semantic_verification\": \"not_performed\","` | — |
| [SRC-1AE03B9EC3-L006642](../../agents/web_agent.py#L6642) | 6642 | `"            \"fact_correctness\": \"not_verified\","` | — |
| [SRC-1AE03B9EC3-L006643](../../agents/web_agent.py#L6643) | 6643 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006644](../../agents/web_agent.py#L6644) | 6644 | `"        semantic_answer_withheld = False"` | — |
| [SRC-1AE03B9EC3-L006645](../../agents/web_agent.py#L6645) | 6645 | `"        if used_llm and sources and review_status == \"model_claim_audit_completed\":"` | — |
| [SRC-1AE03B9EC3-L006646](../../agents/web_agent.py#L6646) | 6646 | `"            if citation_warnings:"` | — |
| [SRC-1AE03B9EC3-L006647](../../agents/web_agent.py#L6647) | 6647 | `"                semantic_claim_verification = {"` | — |
| [SRC-1AE03B9EC3-L006648](../../agents/web_agent.py#L6648) | 6648 | `"                    \"status\": \"not_verifiable\","` | — |
| [SRC-1AE03B9EC3-L006649](../../agents/web_agent.py#L6649) | 6649 | `"                    \"withhold_answer\": True,"` | — |
| [SRC-1AE03B9EC3-L006650](../../agents/web_agent.py#L6650) | 6650 | `"                    \"reason\": \"invalid_citation_references_were_removed\","` | — |
| [SRC-1AE03B9EC3-L006651](../../agents/web_agent.py#L6651) | 6651 | `"                    \"semantic_verification\": \"not_completed\","` | — |
| [SRC-1AE03B9EC3-L006652](../../agents/web_agent.py#L6652) | 6652 | `"                    \"fact_correctness\": \"not_verified\","` | — |
| [SRC-1AE03B9EC3-L006653](../../agents/web_agent.py#L6653) | 6653 | `"                }"` | — |
| [SRC-1AE03B9EC3-L006654](../../agents/web_agent.py#L6654) | 6654 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L006655](../../agents/web_agent.py#L6655) | 6655 | `"                semantic_claim_verification = self._verify_semantic_claims("` | — |
| [SRC-1AE03B9EC3-L006656](../../agents/web_agent.py#L6656) | 6656 | `"                    working_question, answer, sources"` | — |
| [SRC-1AE03B9EC3-L006657](../../agents/web_agent.py#L6657) | 6657 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006658](../../agents/web_agent.py#L6658) | 6658 | `"            if semantic_claim_verification.get(\"status\") not in {"` | — |
| [SRC-1AE03B9EC3-L006659](../../agents/web_agent.py#L6659) | 6659 | `"                \"completed_all_claims_supported\","` | — |
| [SRC-1AE03B9EC3-L006660](../../agents/web_agent.py#L6660) | 6660 | `"                \"completed_no_factual_claims\","` | — |
| [SRC-1AE03B9EC3-L006661](../../agents/web_agent.py#L6661) | 6661 | `"            }:"` | — |
| [SRC-1AE03B9EC3-L006662](../../agents/web_agent.py#L6662) | 6662 | `"                semantic_answer_withheld = True"` | — |
| [SRC-1AE03B9EC3-L006663](../../agents/web_agent.py#L6663) | 6663 | `"                semantic_warning = ("` | — |
| [SRC-1AE03B9EC3-L006664](../../agents/web_agent.py#L6664) | 6664 | `"                    \"حُجبت صياغة النموذج لأن مراجع دعم الادعاءات لم يستطع إثبات دعم \""` | — |
| [SRC-1AE03B9EC3-L006665](../../agents/web_agent.py#L6665) | 6665 | `"                    \"كل ادعاء واقعي بمصدره المحدد دون تعارض. المقتطفات أدناه مواد مصدرية \""` | — |
| [SRC-1AE03B9EC3-L006666](../../agents/web_agent.py#L6666) | 6666 | `"                    \"للمراجعة وليست إجابة متحققة.\""` | — |
| [SRC-1AE03B9EC3-L006667](../../agents/web_agent.py#L6667) | 6667 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006668](../../agents/web_agent.py#L6668) | 6668 | `"                answer = ("` | — |
| [SRC-1AE03B9EC3-L006669](../../agents/web_agent.py#L6669) | 6669 | `"                    _fallback_lead_answer(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L006670](../../agents/web_agent.py#L6670) | 6670 | `"                    if lead_request and lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L006671](../../agents/web_agent.py#L6671) | 6671 | `"                    else _fallback_answer(sources, semantic_warning)"` | — |
| [SRC-1AE03B9EC3-L006672](../../agents/web_agent.py#L6672) | 6672 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006673](../../agents/web_agent.py#L6673) | 6673 | `"                answer, fallback_citation_warnings = self._remove_invalid_citations("` | — |
| [SRC-1AE03B9EC3-L006674](../../agents/web_agent.py#L6674) | 6674 | `"                    answer, max_citable_sources"` | — |
| [SRC-1AE03B9EC3-L006675](../../agents/web_agent.py#L6675) | 6675 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006676](../../agents/web_agent.py#L6676) | 6676 | `"                citation_warnings = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L006677](../../agents/web_agent.py#L6677) | 6677 | `"                    citation_warnings + fallback_citation_warnings"` | — |
| [SRC-1AE03B9EC3-L006678](../../agents/web_agent.py#L6678) | 6678 | `"                ))"` | — |
| [SRC-1AE03B9EC3-L006679](../../agents/web_agent.py#L6679) | 6679 | `"                citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L006680](../../agents/web_agent.py#L6680) | 6680 | `"                    answer, max_citable_sources, citation_warnings, review_status"` | — |
| [SRC-1AE03B9EC3-L006681](../../agents/web_agent.py#L6681) | 6681 | `"                )"` | — |
| [SRC-1AE03B9EC3-L006682](../../agents/web_agent.py#L6682) | 6682 | `"        report[\"semantic_claim_verification\"] = semantic_claim_verification"` | — |
| [SRC-1AE03B9EC3-L006683](../../agents/web_agent.py#L6683) | 6683 | `"        report[\"answer_was_withheld\"] = semantic_answer_withheld"` | — |
| [SRC-1AE03B9EC3-L006684](../../agents/web_agent.py#L6684) | 6684 | `"        report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006685](../../agents/web_agent.py#L6685) | 6685 | `"        report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L006686](../../agents/web_agent.py#L6686) | 6686 | `"        report[\"second_pass_review\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L006687](../../agents/web_agent.py#L6687) | 6687 | `"        report[\"claim_audit\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L006688](../../agents/web_agent.py#L6688) | 6688 | `"        answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L006689](../../agents/web_agent.py#L6689) | 6689 | `"            \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L006690](../../agents/web_agent.py#L6690) | 6690 | `"            \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L006691](../../agents/web_agent.py#L6691) | 6691 | `"            \"review_prompted\": review_status == \"model_claim_audit_completed\","` | — |
| [SRC-1AE03B9EC3-L006692](../../agents/web_agent.py#L6692) | 6692 | `"            \"status\": ("` | — |
| [SRC-1AE03B9EC3-L006693](../../agents/web_agent.py#L6693) | 6693 | `"                \"model_review_requested_not_machine_verified\""` | — |
| [SRC-1AE03B9EC3-L006694](../../agents/web_agent.py#L6694) | 6694 | `"                if coverage_targets and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006695](../../agents/web_agent.py#L6695) | 6695 | `"                else \"review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006696](../../agents/web_agent.py#L6696) | 6696 | `"                if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L006697](../../agents/web_agent.py#L6697) | 6697 | `"                else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L006698](../../agents/web_agent.py#L6698) | 6698 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L006699](../../agents/web_agent.py#L6699) | 6699 | `"            \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L006700](../../agents/web_agent.py#L6700) | 6700 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006701](../../agents/web_agent.py#L6701) | 6701 | `"        report[\"answer_coverage\"] = answer_coverage"` | — |
| [SRC-1AE03B9EC3-L006702](../../agents/web_agent.py#L6702) | 6702 | `"        report[\"coverage_repair_status\"] = coverage_repair_status"` | — |
| [SRC-1AE03B9EC3-L006703](../../agents/web_agent.py#L6703) | 6703 | `"        report[\"coverage_repair_warning\"] = coverage_repair_warning"` | — |
| [SRC-1AE03B9EC3-L006704](../../agents/web_agent.py#L6704) | 6704 | `"        answer_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets, plan.get(\"requirement_queries\"))"` | — |
| [SRC-1AE03B9EC3-L006705](../../agents/web_agent.py#L6705) | 6705 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L006706](../../agents/web_agent.py#L6706) | 6706 | `"            answer_coverage[\"status\"] = \"semantic_support_unverified_answer_withheld\""` | — |
| [SRC-1AE03B9EC3-L006707](../../agents/web_agent.py#L6707) | 6707 | `"            answer_coverage[\"semantic_verification_status\"] = semantic_claim_verification.get(\"status\")"` | — |
| [SRC-1AE03B9EC3-L006708](../../agents/web_agent.py#L6708) | 6708 | `"        answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L006709](../../agents/web_agent.py#L6709) | 6709 | `"        answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L006710](../../agents/web_agent.py#L6710) | 6710 | `"        answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L006711](../../agents/web_agent.py#L6711) | 6711 | `"        answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L006712](../../agents/web_agent.py#L6712) | 6712 | `"        requirements_without_candidates = int("` | — |
| [SRC-1AE03B9EC3-L006713](../../agents/web_agent.py#L6713) | 6713 | `"            answer_integrity.get(\"requirements_without_candidate_evidence_count\", 0) or 0"` | — |
| [SRC-1AE03B9EC3-L006714](../../agents/web_agent.py#L6714) | 6714 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006715](../../agents/web_agent.py#L6715) | 6715 | `"        task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L006716](../../agents/web_agent.py#L6716) | 6716 | `"            \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L006717](../../agents/web_agent.py#L6717) | 6717 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L006718](../../agents/web_agent.py#L6718) | 6718 | `"                answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006719](../../agents/web_agent.py#L6719) | 6719 | `"                or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006720](../../agents/web_agent.py#L6720) | 6720 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006721](../../agents/web_agent.py#L6721) | 6721 | `"            else \"candidate_evidence_gaps_or_linkage_unknown\""` | — |
| [SRC-1AE03B9EC3-L006722](../../agents/web_agent.py#L6722) | 6722 | `"            if coverage_targets and requirements_without_candidates > 0"` | — |
| [SRC-1AE03B9EC3-L006723](../../agents/web_agent.py#L6723) | 6723 | `"            else \"lexical_signals_found_not_semantically_verified\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L006724](../../agents/web_agent.py#L6724) | 6724 | `"            else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L006725](../../agents/web_agent.py#L6725) | 6725 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006726](../../agents/web_agent.py#L6726) | 6726 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L006727](../../agents/web_agent.py#L6727) | 6727 | `"            task_fulfillment_status = \"not_assessed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L006728](../../agents/web_agent.py#L6728) | 6728 | `"        answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L006729](../../agents/web_agent.py#L6729) | 6729 | `"        answer_coverage[\"semantic_verification_status\"] = semantic_claim_verification.get(\"status\")"` | — |
| [SRC-1AE03B9EC3-L006730](../../agents/web_agent.py#L6730) | 6730 | `"        report[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L006731](../../agents/web_agent.py#L6731) | 6731 | `"        report[\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L006732](../../agents/web_agent.py#L6732) | 6732 | `"        report[\"requirement_evidence\"] = answer_integrity.get(\"requirement_evidence\", [])"` | — |
| [SRC-1AE03B9EC3-L006733](../../agents/web_agent.py#L6733) | 6733 | `"        report[\"connector_summary\"] = self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L006734](../../agents/web_agent.py#L6734) | 6734 | `"            list(self._provider_diagnostics), sources"` | — |
| [SRC-1AE03B9EC3-L006735](../../agents/web_agent.py#L6735) | 6735 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006736](../../agents/web_agent.py#L6736) | 6736 | `"        report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L006737](../../agents/web_agent.py#L6737) | 6737 | `"        distinct_providers = {"` | — |
| [SRC-1AE03B9EC3-L006738](../../agents/web_agent.py#L6738) | 6738 | `"            provider for source in sources for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L006739](../../agents/web_agent.py#L6739) | 6739 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006740](../../agents/web_agent.py#L6740) | 6740 | `"        distinct_domains = {"` | — |
| [SRC-1AE03B9EC3-L006741](../../agents/web_agent.py#L6741) | 6741 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L006742](../../agents/web_agent.py#L6742) | 6742 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L006743](../../agents/web_agent.py#L6743) | 6743 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L006744](../../agents/web_agent.py#L6744) | 6744 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L006745](../../agents/web_agent.py#L6745) | 6745 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006746](../../agents/web_agent.py#L6746) | 6746 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L006747](../../agents/web_agent.py#L6747) | 6747 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006748](../../agents/web_agent.py#L6748) | 6748 | `"        distinct_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L006749](../../agents/web_agent.py#L6749) | 6749 | `"        fetched_pages = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L006750](../../agents/web_agent.py#L6750) | 6750 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L006751](../../agents/web_agent.py#L6751) | 6751 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L006752](../../agents/web_agent.py#L6752) | 6752 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L006753](../../agents/web_agent.py#L6753) | 6753 | `"            len(sources) >= 4 and len(distinct_domains) >= 3"` | — |
| [SRC-1AE03B9EC3-L006754](../../agents/web_agent.py#L6754) | 6754 | `"            and len(distinct_providers) >= 2 and fetched_pages >= 1"` | — |
| [SRC-1AE03B9EC3-L006755](../../agents/web_agent.py#L6755) | 6755 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006756](../../agents/web_agent.py#L6756) | 6756 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006757](../../agents/web_agent.py#L6757) | 6757 | `"            research_quality = \"excellent\""` | — |
| [SRC-1AE03B9EC3-L006758](../../agents/web_agent.py#L6758) | 6758 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L006759](../../agents/web_agent.py#L6759) | 6759 | `"            len(sources) >= 2 and len(distinct_domains) >= 2"` | — |
| [SRC-1AE03B9EC3-L006760](../../agents/web_agent.py#L6760) | 6760 | `"            and (len(distinct_providers) >= 2 or fetched_pages >= 1)"` | — |
| [SRC-1AE03B9EC3-L006761](../../agents/web_agent.py#L6761) | 6761 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006762](../../agents/web_agent.py#L6762) | 6762 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006763](../../agents/web_agent.py#L6763) | 6763 | `"            research_quality = \"good\""` | — |
| [SRC-1AE03B9EC3-L006764](../../agents/web_agent.py#L6764) | 6764 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L006765](../../agents/web_agent.py#L6765) | 6765 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L006766](../../agents/web_agent.py#L6766) | 6766 | `""` | — |
| [SRC-1AE03B9EC3-L006767](../../agents/web_agent.py#L6767) | 6767 | `"        # Source breadth and a completed model-assisted review do not justify a"` | — |
| [SRC-1AE03B9EC3-L006768](../../agents/web_agent.py#L6768) | 6768 | `"        # positive research-quality label if the final answer has no valid source"` | — |
| [SRC-1AE03B9EC3-L006769](../../agents/web_agent.py#L6769) | 6769 | `"        # citation markers. This is a deterministic presentation guard, not a"` | — |
| [SRC-1AE03B9EC3-L006770](../../agents/web_agent.py#L6770) | 6770 | `"        # semantic entailment check."` | — |
| [SRC-1AE03B9EC3-L006771](../../agents/web_agent.py#L6771) | 6771 | `"        uncited_reviewed_answer = ("` | — |
| [SRC-1AE03B9EC3-L006772](../../agents/web_agent.py#L6772) | 6772 | `"            used_llm"` | — |
| [SRC-1AE03B9EC3-L006773](../../agents/web_agent.py#L6773) | 6773 | `"            and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L006774](../../agents/web_agent.py#L6774) | 6774 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006775](../../agents/web_agent.py#L6775) | 6775 | `"            and citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L006776](../../agents/web_agent.py#L6776) | 6776 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006777](../../agents/web_agent.py#L6777) | 6777 | `"        if uncited_reviewed_answer:"` | — |
| [SRC-1AE03B9EC3-L006778](../../agents/web_agent.py#L6778) | 6778 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L006779](../../agents/web_agent.py#L6779) | 6779 | `"            citation_validation[\"claim_support\"] = \"not_established_no_valid_source_citations\""` | — |
| [SRC-1AE03B9EC3-L006780](../../agents/web_agent.py#L6780) | 6780 | `"            answer_evidence_status = \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-1AE03B9EC3-L006781](../../agents/web_agent.py#L6781) | 6781 | `"            uncited_answer_warning = ("` | — |
| [SRC-1AE03B9EC3-L006782](../../agents/web_agent.py#L6782) | 6782 | `"                \"اكتملت مراجعة النموذج، لكن الإجابة النهائية لا تحتوي على إحالات صالحة \""` | — |
| [SRC-1AE03B9EC3-L006783](../../agents/web_agent.py#L6783) | 6783 | `"                \"إلى قائمة المصادر؛ لذلك صُنّفت جودة البحث «جزئية». وجود المصادر أو \""` | — |
| [SRC-1AE03B9EC3-L006784](../../agents/web_agent.py#L6784) | 6784 | `"                \"اكتمال مراجعة النموذج لا يثبت دعم كل ادعاء.\""` | — |
| [SRC-1AE03B9EC3-L006785](../../agents/web_agent.py#L6785) | 6785 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006786](../../agents/web_agent.py#L6786) | 6786 | `"        elif citation_validation[\"valid_citation_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L006787](../../agents/web_agent.py#L6787) | 6787 | `"            answer_evidence_status = ("` | — |
| [SRC-1AE03B9EC3-L006788](../../agents/web_agent.py#L6788) | 6788 | `"                \"semantic_support_unverified_answer_withheld\""` | — |
| [SRC-1AE03B9EC3-L006789](../../agents/web_agent.py#L6789) | 6789 | `"                if semantic_answer_withheld else \"citation_indices_validated_only\""` | — |
| [SRC-1AE03B9EC3-L006790](../../agents/web_agent.py#L6790) | 6790 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006791](../../agents/web_agent.py#L6791) | 6791 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L006792](../../agents/web_agent.py#L6792) | 6792 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L006793](../../agents/web_agent.py#L6793) | 6793 | `"            answer_evidence_status = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L006794](../../agents/web_agent.py#L6794) | 6794 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L006795](../../agents/web_agent.py#L6795) | 6795 | `""` | — |
| [SRC-1AE03B9EC3-L006796](../../agents/web_agent.py#L6796) | 6796 | `"        search_attempted = search_attempted or bool(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L006797](../../agents/web_agent.py#L6797) | 6797 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L006798](../../agents/web_agent.py#L6798) | 6798 | `"        prior_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L006799](../../agents/web_agent.py#L6799) | 6799 | `"        if prior_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L006800](../../agents/web_agent.py#L6800) | 6800 | `"            # Preserve a known pipeline failure instead of relabeling it as an ordinary"` | — |
| [SRC-1AE03B9EC3-L006801](../../agents/web_agent.py#L6801) | 6801 | `"            # zero-result search merely because the outer request reached its return path."` | — |
| [SRC-1AE03B9EC3-L006802](../../agents/web_agent.py#L6802) | 6802 | `"            report[\"search_outcome\"] = prior_search_outcome"` | — |
| [SRC-1AE03B9EC3-L006803](../../agents/web_agent.py#L6803) | 6803 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L006804](../../agents/web_agent.py#L6804) | 6804 | `"            report[\"search_outcome\"] = ("` | — |
| [SRC-1AE03B9EC3-L006805](../../agents/web_agent.py#L6805) | 6805 | `"                \"attempted_with_usable_sources\" if search_attempted and sources"` | — |
| [SRC-1AE03B9EC3-L006806](../../agents/web_agent.py#L6806) | 6806 | `"                else \"attempted_no_usable_sources\" if search_attempted"` | — |
| [SRC-1AE03B9EC3-L006807](../../agents/web_agent.py#L6807) | 6807 | `"                else \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L006808](../../agents/web_agent.py#L6808) | 6808 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006809](../../agents/web_agent.py#L6809) | 6809 | `"        report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006810](../../agents/web_agent.py#L6810) | 6810 | `"        report[\"research_quality\"] = research_quality"` | — |
| [SRC-1AE03B9EC3-L006811](../../agents/web_agent.py#L6811) | 6811 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L006812](../../agents/web_agent.py#L6812) | 6812 | `"        report[\"answer_evidence_status\"] = answer_evidence_status"` | — |
| [SRC-1AE03B9EC3-L006813](../../agents/web_agent.py#L6813) | 6813 | `"        report[\"distinct_registrable_domains\"] = len(distinct_domains)"` | — |
| [SRC-1AE03B9EC3-L006814](../../agents/web_agent.py#L6814) | 6814 | `"        report[\"independent_sources\"] = len(distinct_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L006815](../../agents/web_agent.py#L6815) | 6815 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L006816](../../agents/web_agent.py#L6816) | 6816 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L006817](../../agents/web_agent.py#L6817) | 6817 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006818](../../agents/web_agent.py#L6818) | 6818 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L006819](../../agents/web_agent.py#L6819) | 6819 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L006820](../../agents/web_agent.py#L6820) | 6820 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006821](../../agents/web_agent.py#L6821) | 6821 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L006822](../../agents/web_agent.py#L6822) | 6822 | `"        report[\"claim_audit_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L006823](../../agents/web_agent.py#L6823) | 6823 | `"            \"distinct_model_assessed_source_support_not_ground_truth\""` | — |
| [SRC-1AE03B9EC3-L006824](../../agents/web_agent.py#L6824) | 6824 | `"            if semantic_claim_verification.get(\"status\") in {"` | — |
| [SRC-1AE03B9EC3-L006825](../../agents/web_agent.py#L6825) | 6825 | `"                \"completed_all_claims_supported\", \"completed_no_factual_claims\""` | — |
| [SRC-1AE03B9EC3-L006826](../../agents/web_agent.py#L6826) | 6826 | `"            }"` | — |
| [SRC-1AE03B9EC3-L006827](../../agents/web_agent.py#L6827) | 6827 | `"            else \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L006828](../../agents/web_agent.py#L6828) | 6828 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006829](../../agents/web_agent.py#L6829) | 6829 | `"        report[\"insufficient_evidence\"] = bool("` | — |
| [SRC-1AE03B9EC3-L006830](../../agents/web_agent.py#L6830) | 6830 | `"            report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L006831](../../agents/web_agent.py#L6831) | 6831 | `"            or not sources"` | — |
| [SRC-1AE03B9EC3-L006832](../../agents/web_agent.py#L6832) | 6832 | `"            or semantic_answer_withheld"` | — |
| [SRC-1AE03B9EC3-L006833](../../agents/web_agent.py#L6833) | 6833 | `"            or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006834](../../agents/web_agent.py#L6834) | 6834 | `"            or ("` | — |
| [SRC-1AE03B9EC3-L006835](../../agents/web_agent.py#L6835) | 6835 | `"                bool(coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L006836](../../agents/web_agent.py#L6836) | 6836 | `"                and answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006837](../../agents/web_agent.py#L6837) | 6837 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006838](../../agents/web_agent.py#L6838) | 6838 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006839](../../agents/web_agent.py#L6839) | 6839 | `"        report[\"valid_citation_range\"] = [1, max_citable_sources] if max_citable_sources else []"` | — |
| [SRC-1AE03B9EC3-L006840](../../agents/web_agent.py#L6840) | 6840 | `"        report[\"citation_count\"] = citation_validation[\"valid_citation_count\"]"` | — |
| [SRC-1AE03B9EC3-L006841](../../agents/web_agent.py#L6841) | 6841 | `"        report[\"citation_check\"] = citation_validation[\"status\"]"` | — |
| [SRC-1AE03B9EC3-L006842](../../agents/web_agent.py#L6842) | 6842 | `"        report[\"citation_validation\"] = citation_validation"` | — |
| [SRC-1AE03B9EC3-L006843](../../agents/web_agent.py#L6843) | 6843 | `"        warnings = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L006844](../../agents/web_agent.py#L6844) | 6844 | `"            search_warnings"` | — |
| [SRC-1AE03B9EC3-L006845](../../agents/web_agent.py#L6845) | 6845 | `"            + ([llm_warning] if llm_warning else [])"` | — |
| [SRC-1AE03B9EC3-L006846](../../agents/web_agent.py#L6846) | 6846 | `"            + ([review_warning] if review_warning else [])"` | — |
| [SRC-1AE03B9EC3-L006847](../../agents/web_agent.py#L6847) | 6847 | `"            + ([coverage_repair_warning] if coverage_repair_warning else [])"` | — |
| [SRC-1AE03B9EC3-L006848](../../agents/web_agent.py#L6848) | 6848 | `"            + citation_warnings"` | — |
| [SRC-1AE03B9EC3-L006849](../../agents/web_agent.py#L6849) | 6849 | `"            + ([uncited_answer_warning] if uncited_answer_warning else [])"` | — |
| [SRC-1AE03B9EC3-L006850](../../agents/web_agent.py#L6850) | 6850 | `"            + (["` | — |
| [SRC-1AE03B9EC3-L006851](../../agents/web_agent.py#L6851) | 6851 | `"                \"حُجبت الإجابة المولدة لعدم اكتمال التحقق الدلالي المستقل عن نموذج الصياغة.\""` | — |
| [SRC-1AE03B9EC3-L006852](../../agents/web_agent.py#L6852) | 6852 | `"            ] if semantic_answer_withheld else [])"` | — |
| [SRC-1AE03B9EC3-L006853](../../agents/web_agent.py#L6853) | 6853 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L006854](../../agents/web_agent.py#L6854) | 6854 | `"        report[\"model_calls\"] = list(self.model_usage)"` | — |
| [SRC-1AE03B9EC3-L006855](../../agents/web_agent.py#L6855) | 6855 | `"        report[\"openrouter_web_search_enabled\"] = self.openrouter_web_search_enabled"` | — |
| [SRC-1AE03B9EC3-L006856](../../agents/web_agent.py#L6856) | 6856 | `"        report[\"openrouter_web_search_results\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L006857](../../agents/web_agent.py#L6857) | 6857 | `"        if semantic_answer_withheld:"` | — |
| [SRC-1AE03B9EC3-L006858](../../agents/web_agent.py#L6858) | 6858 | `"            final_answer_status = \"semantic_verification_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L006859](../../agents/web_agent.py#L6859) | 6859 | `"        elif generation_budget_exhausted or review_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L006860](../../agents/web_agent.py#L6860) | 6860 | `"            final_answer_status = \"budget_exhausted_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L006861](../../agents/web_agent.py#L6861) | 6861 | `"        elif llm_warning:"` | — |
| [SRC-1AE03B9EC3-L006862](../../agents/web_agent.py#L6862) | 6862 | `"            final_answer_status = ("` | — |
| [SRC-1AE03B9EC3-L006863](../../agents/web_agent.py#L6863) | 6863 | `"                \"model_not_configured_fallback\""` | — |
| [SRC-1AE03B9EC3-L006864](../../agents/web_agent.py#L6864) | 6864 | `"                if not self.api_key"` | — |
| [SRC-1AE03B9EC3-L006865](../../agents/web_agent.py#L6865) | 6865 | `"                else \"generation_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L006866](../../agents/web_agent.py#L6866) | 6866 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006867](../../agents/web_agent.py#L6867) | 6867 | `"        elif review_warning:"` | — |
| [SRC-1AE03B9EC3-L006868](../../agents/web_agent.py#L6868) | 6868 | `"            final_answer_status = \"review_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L006869](../../agents/web_agent.py#L6869) | 6869 | `"        elif coverage_repair_status == \"no_change_gap_unresolved\":"` | — |
| [SRC-1AE03B9EC3-L006870](../../agents/web_agent.py#L6870) | 6870 | `"            final_answer_status = \"coverage_repair_left_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L006871](../../agents/web_agent.py#L6871) | 6871 | `"        elif coverage_repair_status == \"budget_exhausted\":"` | — |
| [SRC-1AE03B9EC3-L006872](../../agents/web_agent.py#L6872) | 6872 | `"            final_answer_status = \"coverage_repair_budget_exhausted_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L006873](../../agents/web_agent.py#L6873) | 6873 | `"        elif coverage_repair_status == \"unavailable\":"` | — |
| [SRC-1AE03B9EC3-L006874](../../agents/web_agent.py#L6874) | 6874 | `"            final_answer_status = \"coverage_repair_unavailable_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L006875](../../agents/web_agent.py#L6875) | 6875 | `"        elif used_llm:"` | — |
| [SRC-1AE03B9EC3-L006876](../../agents/web_agent.py#L6876) | 6876 | `"            final_answer_status = \"model_answer_generated\""` | — |
| [SRC-1AE03B9EC3-L006877](../../agents/web_agent.py#L6877) | 6877 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L006878](../../agents/web_agent.py#L6878) | 6878 | `"            final_answer_status = \"source_fallback\""` | — |
| [SRC-1AE03B9EC3-L006879](../../agents/web_agent.py#L6879) | 6879 | `""` | — |
| [SRC-1AE03B9EC3-L006880](../../agents/web_agent.py#L6880) | 6880 | `"        # Report pipeline completion separately from factual correctness. A successful"` | — |
| [SRC-1AE03B9EC3-L006881](../../agents/web_agent.py#L6881) | 6881 | `"        # retrieval or model review is not an independent semantic fact check."` | — |
| [SRC-1AE03B9EC3-L006882](../../agents/web_agent.py#L6882) | 6882 | `"        if report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L006883](../../agents/web_agent.py#L6883) | 6883 | `"            pipeline_completion_status = \"execution_failed\""` | — |
| [SRC-1AE03B9EC3-L006884](../../agents/web_agent.py#L6884) | 6884 | `"        elif not search_attempted:"` | — |
| [SRC-1AE03B9EC3-L006885](../../agents/web_agent.py#L6885) | 6885 | `"            pipeline_completion_status = \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L006886](../../agents/web_agent.py#L6886) | 6886 | `"        elif not sources:"` | — |
