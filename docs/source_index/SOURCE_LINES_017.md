# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **017**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L006289 إلى SRC-EEF2E6447C-L000452
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L006289](../../agents/web_agent.py#L6289) | 6289 | `"                        \"لا تعتبر التغطية مكتملة دون مراجعة المحور المذكور.\""` | — |
| [SRC-1AE03B9EC3-L006290](../../agents/web_agent.py#L6290) | 6290 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006291](../../agents/web_agent.py#L6291) | 6291 | `"                except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L006292](../../agents/web_agent.py#L6292) | 6292 | `"                    coverage_repair_status = \"unavailable\""` | — |
| [SRC-1AE03B9EC3-L006293](../../agents/web_agent.py#L6293) | 6293 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006294](../../agents/web_agent.py#L6294) | 6294 | `"                        \"تعذرت محاولة إصلاح محور قد يكون ناقصًا (\""` | — |
| [SRC-1AE03B9EC3-L006295](../../agents/web_agent.py#L6295) | 6295 | `"                        + type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L006296](../../agents/web_agent.py#L6296) | 6296 | `"                        + \")؛ راجع المحاور المطلوبة قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L006297](../../agents/web_agent.py#L6297) | 6297 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006298](../../agents/web_agent.py#L6298) | 6298 | `"        elif coverage_targets and review_status == \"model_claim_audit_completed\" and not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L006299](../../agents/web_agent.py#L6299) | 6299 | `"            coverage_repair_status = \"skipped_no_model_configuration\""` | — |
| [SRC-1AE03B9EC3-L006300](../../agents/web_agent.py#L6300) | 6300 | `"        elif coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L006301](../../agents/web_agent.py#L6301) | 6301 | `"            coverage_repair_status = \"skipped_review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006302](../../agents/web_agent.py#L6302) | 6302 | `""` | — |
| [SRC-1AE03B9EC3-L006303](../../agents/web_agent.py#L6303) | 6303 | `"        if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L006304](../../agents/web_agent.py#L6304) | 6304 | `"            answer += \"\\n\\nروابط إضافية من البحث المباشر عبر الويب:\""` | — |
| [SRC-1AE03B9EC3-L006305](../../agents/web_agent.py#L6305) | 6305 | `"            for source in self.server_search_sources[:8]:"` | — |
| [SRC-1AE03B9EC3-L006306](../../agents/web_agent.py#L6306) | 6306 | `"                answer += \"\\n- \" + source[\"title\"] + \" — \" + source[\"url\"]"` | — |
| [SRC-1AE03B9EC3-L006307](../../agents/web_agent.py#L6307) | 6307 | `"        max_citable_sources = min(MAX_LLM_CITED_SOURCES, len(sources))"` | — |
| [SRC-1AE03B9EC3-L006308](../../agents/web_agent.py#L6308) | 6308 | `"        answer, citation_warnings = self._remove_invalid_citations("` | — |
| [SRC-1AE03B9EC3-L006309](../../agents/web_agent.py#L6309) | 6309 | `"            answer, max_citable_sources"` | — |
| [SRC-1AE03B9EC3-L006310](../../agents/web_agent.py#L6310) | 6310 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006311](../../agents/web_agent.py#L6311) | 6311 | `"        citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L006312](../../agents/web_agent.py#L6312) | 6312 | `"            answer, max_citable_sources, citation_warnings, review_status"` | — |
| [SRC-1AE03B9EC3-L006313](../../agents/web_agent.py#L6313) | 6313 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006314](../../agents/web_agent.py#L6314) | 6314 | `"        report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006315](../../agents/web_agent.py#L6315) | 6315 | `"        report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L006316](../../agents/web_agent.py#L6316) | 6316 | `"        report[\"second_pass_review\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L006317](../../agents/web_agent.py#L6317) | 6317 | `"        report[\"claim_audit\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L006318](../../agents/web_agent.py#L6318) | 6318 | `"        answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L006319](../../agents/web_agent.py#L6319) | 6319 | `"            \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L006320](../../agents/web_agent.py#L6320) | 6320 | `"            \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L006321](../../agents/web_agent.py#L6321) | 6321 | `"            \"review_prompted\": review_status == \"model_claim_audit_completed\","` | — |
| [SRC-1AE03B9EC3-L006322](../../agents/web_agent.py#L6322) | 6322 | `"            \"status\": ("` | — |
| [SRC-1AE03B9EC3-L006323](../../agents/web_agent.py#L6323) | 6323 | `"                \"model_review_requested_not_machine_verified\""` | — |
| [SRC-1AE03B9EC3-L006324](../../agents/web_agent.py#L6324) | 6324 | `"                if coverage_targets and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006325](../../agents/web_agent.py#L6325) | 6325 | `"                else \"review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006326](../../agents/web_agent.py#L6326) | 6326 | `"                if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L006327](../../agents/web_agent.py#L6327) | 6327 | `"                else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L006328](../../agents/web_agent.py#L6328) | 6328 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L006329](../../agents/web_agent.py#L6329) | 6329 | `"            \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L006330](../../agents/web_agent.py#L6330) | 6330 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006331](../../agents/web_agent.py#L6331) | 6331 | `"        report[\"answer_coverage\"] = answer_coverage"` | — |
| [SRC-1AE03B9EC3-L006332](../../agents/web_agent.py#L6332) | 6332 | `"        report[\"coverage_repair_status\"] = coverage_repair_status"` | — |
| [SRC-1AE03B9EC3-L006333](../../agents/web_agent.py#L6333) | 6333 | `"        report[\"coverage_repair_warning\"] = coverage_repair_warning"` | — |
| [SRC-1AE03B9EC3-L006334](../../agents/web_agent.py#L6334) | 6334 | `"        answer_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets, plan.get(\"requirement_queries\"))"` | — |
| [SRC-1AE03B9EC3-L006335](../../agents/web_agent.py#L6335) | 6335 | `"        answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L006336](../../agents/web_agent.py#L6336) | 6336 | `"        answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L006337](../../agents/web_agent.py#L6337) | 6337 | `"        answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L006338](../../agents/web_agent.py#L6338) | 6338 | `"        answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L006339](../../agents/web_agent.py#L6339) | 6339 | `"        requirements_without_candidates = int("` | — |
| [SRC-1AE03B9EC3-L006340](../../agents/web_agent.py#L6340) | 6340 | `"            answer_integrity.get(\"requirements_without_candidate_evidence_count\", 0) or 0"` | — |
| [SRC-1AE03B9EC3-L006341](../../agents/web_agent.py#L6341) | 6341 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006342](../../agents/web_agent.py#L6342) | 6342 | `"        task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L006343](../../agents/web_agent.py#L6343) | 6343 | `"            \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L006344](../../agents/web_agent.py#L6344) | 6344 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L006345](../../agents/web_agent.py#L6345) | 6345 | `"                answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006346](../../agents/web_agent.py#L6346) | 6346 | `"                or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006347](../../agents/web_agent.py#L6347) | 6347 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006348](../../agents/web_agent.py#L6348) | 6348 | `"            else \"candidate_evidence_gaps_or_linkage_unknown\""` | — |
| [SRC-1AE03B9EC3-L006349](../../agents/web_agent.py#L6349) | 6349 | `"            if coverage_targets and requirements_without_candidates > 0"` | — |
| [SRC-1AE03B9EC3-L006350](../../agents/web_agent.py#L6350) | 6350 | `"            else \"lexical_signals_found_not_semantically_verified\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L006351](../../agents/web_agent.py#L6351) | 6351 | `"            else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L006352](../../agents/web_agent.py#L6352) | 6352 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006353](../../agents/web_agent.py#L6353) | 6353 | `"        answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L006354](../../agents/web_agent.py#L6354) | 6354 | `"        report[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L006355](../../agents/web_agent.py#L6355) | 6355 | `"        report[\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L006356](../../agents/web_agent.py#L6356) | 6356 | `"        report[\"requirement_evidence\"] = answer_integrity.get(\"requirement_evidence\", [])"` | — |
| [SRC-1AE03B9EC3-L006357](../../agents/web_agent.py#L6357) | 6357 | `"        report[\"connector_summary\"] = self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L006358](../../agents/web_agent.py#L6358) | 6358 | `"            list(self._provider_diagnostics), sources"` | — |
| [SRC-1AE03B9EC3-L006359](../../agents/web_agent.py#L6359) | 6359 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006360](../../agents/web_agent.py#L6360) | 6360 | `"        report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L006361](../../agents/web_agent.py#L6361) | 6361 | `"        distinct_providers = {"` | — |
| [SRC-1AE03B9EC3-L006362](../../agents/web_agent.py#L6362) | 6362 | `"            provider for source in sources for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L006363](../../agents/web_agent.py#L6363) | 6363 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006364](../../agents/web_agent.py#L6364) | 6364 | `"        distinct_domains = {"` | — |
| [SRC-1AE03B9EC3-L006365](../../agents/web_agent.py#L6365) | 6365 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L006366](../../agents/web_agent.py#L6366) | 6366 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L006367](../../agents/web_agent.py#L6367) | 6367 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L006368](../../agents/web_agent.py#L6368) | 6368 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L006369](../../agents/web_agent.py#L6369) | 6369 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006370](../../agents/web_agent.py#L6370) | 6370 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L006371](../../agents/web_agent.py#L6371) | 6371 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006372](../../agents/web_agent.py#L6372) | 6372 | `"        distinct_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L006373](../../agents/web_agent.py#L6373) | 6373 | `"        fetched_pages = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L006374](../../agents/web_agent.py#L6374) | 6374 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L006375](../../agents/web_agent.py#L6375) | 6375 | `"            len(sources) >= 4 and len(distinct_domains) >= 3"` | — |
| [SRC-1AE03B9EC3-L006376](../../agents/web_agent.py#L6376) | 6376 | `"            and len(distinct_providers) >= 2 and fetched_pages >= 1"` | — |
| [SRC-1AE03B9EC3-L006377](../../agents/web_agent.py#L6377) | 6377 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006378](../../agents/web_agent.py#L6378) | 6378 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006379](../../agents/web_agent.py#L6379) | 6379 | `"            research_quality = \"excellent\""` | — |
| [SRC-1AE03B9EC3-L006380](../../agents/web_agent.py#L6380) | 6380 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L006381](../../agents/web_agent.py#L6381) | 6381 | `"            len(sources) >= 2 and len(distinct_domains) >= 2"` | — |
| [SRC-1AE03B9EC3-L006382](../../agents/web_agent.py#L6382) | 6382 | `"            and (len(distinct_providers) >= 2 or fetched_pages >= 1)"` | — |
| [SRC-1AE03B9EC3-L006383](../../agents/web_agent.py#L6383) | 6383 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006384](../../agents/web_agent.py#L6384) | 6384 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006385](../../agents/web_agent.py#L6385) | 6385 | `"            research_quality = \"good\""` | — |
| [SRC-1AE03B9EC3-L006386](../../agents/web_agent.py#L6386) | 6386 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L006387](../../agents/web_agent.py#L6387) | 6387 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L006388](../../agents/web_agent.py#L6388) | 6388 | `""` | — |
| [SRC-1AE03B9EC3-L006389](../../agents/web_agent.py#L6389) | 6389 | `"        # Source breadth and a completed model-assisted review do not justify a"` | — |
| [SRC-1AE03B9EC3-L006390](../../agents/web_agent.py#L6390) | 6390 | `"        # positive research-quality label if the final answer has no valid source"` | — |
| [SRC-1AE03B9EC3-L006391](../../agents/web_agent.py#L6391) | 6391 | `"        # citation markers. This is a deterministic presentation guard, not a"` | — |
| [SRC-1AE03B9EC3-L006392](../../agents/web_agent.py#L6392) | 6392 | `"        # semantic entailment check."` | — |
| [SRC-1AE03B9EC3-L006393](../../agents/web_agent.py#L6393) | 6393 | `"        uncited_reviewed_answer = ("` | — |
| [SRC-1AE03B9EC3-L006394](../../agents/web_agent.py#L6394) | 6394 | `"            used_llm"` | — |
| [SRC-1AE03B9EC3-L006395](../../agents/web_agent.py#L6395) | 6395 | `"            and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L006396](../../agents/web_agent.py#L6396) | 6396 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006397](../../agents/web_agent.py#L6397) | 6397 | `"            and citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L006398](../../agents/web_agent.py#L6398) | 6398 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006399](../../agents/web_agent.py#L6399) | 6399 | `"        if uncited_reviewed_answer:"` | — |
| [SRC-1AE03B9EC3-L006400](../../agents/web_agent.py#L6400) | 6400 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L006401](../../agents/web_agent.py#L6401) | 6401 | `"            citation_validation[\"claim_support\"] = \"not_established_no_valid_source_citations\""` | — |
| [SRC-1AE03B9EC3-L006402](../../agents/web_agent.py#L6402) | 6402 | `"            answer_evidence_status = \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-1AE03B9EC3-L006403](../../agents/web_agent.py#L6403) | 6403 | `"            uncited_answer_warning = ("` | — |
| [SRC-1AE03B9EC3-L006404](../../agents/web_agent.py#L6404) | 6404 | `"                \"اكتملت مراجعة النموذج، لكن الإجابة النهائية لا تحتوي على إحالات صالحة \""` | — |
| [SRC-1AE03B9EC3-L006405](../../agents/web_agent.py#L6405) | 6405 | `"                \"إلى قائمة المصادر؛ لذلك صُنّفت جودة البحث «جزئية». وجود المصادر أو \""` | — |
| [SRC-1AE03B9EC3-L006406](../../agents/web_agent.py#L6406) | 6406 | `"                \"اكتمال مراجعة النموذج لا يثبت دعم كل ادعاء.\""` | — |
| [SRC-1AE03B9EC3-L006407](../../agents/web_agent.py#L6407) | 6407 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006408](../../agents/web_agent.py#L6408) | 6408 | `"        elif citation_validation[\"valid_citation_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L006409](../../agents/web_agent.py#L6409) | 6409 | `"            answer_evidence_status = \"citation_indices_validated_only\""` | — |
| [SRC-1AE03B9EC3-L006410](../../agents/web_agent.py#L6410) | 6410 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L006411](../../agents/web_agent.py#L6411) | 6411 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L006412](../../agents/web_agent.py#L6412) | 6412 | `"            answer_evidence_status = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L006413](../../agents/web_agent.py#L6413) | 6413 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L006414](../../agents/web_agent.py#L6414) | 6414 | `""` | — |
| [SRC-1AE03B9EC3-L006415](../../agents/web_agent.py#L6415) | 6415 | `"        search_attempted = search_attempted or bool(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L006416](../../agents/web_agent.py#L6416) | 6416 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L006417](../../agents/web_agent.py#L6417) | 6417 | `"        prior_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L006418](../../agents/web_agent.py#L6418) | 6418 | `"        if prior_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L006419](../../agents/web_agent.py#L6419) | 6419 | `"            # Preserve a known pipeline failure instead of relabeling it as an ordinary"` | — |
| [SRC-1AE03B9EC3-L006420](../../agents/web_agent.py#L6420) | 6420 | `"            # zero-result search merely because the outer request reached its return path."` | — |
| [SRC-1AE03B9EC3-L006421](../../agents/web_agent.py#L6421) | 6421 | `"            report[\"search_outcome\"] = prior_search_outcome"` | — |
| [SRC-1AE03B9EC3-L006422](../../agents/web_agent.py#L6422) | 6422 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L006423](../../agents/web_agent.py#L6423) | 6423 | `"            report[\"search_outcome\"] = ("` | — |
| [SRC-1AE03B9EC3-L006424](../../agents/web_agent.py#L6424) | 6424 | `"                \"attempted_with_usable_sources\" if search_attempted and sources"` | — |
| [SRC-1AE03B9EC3-L006425](../../agents/web_agent.py#L6425) | 6425 | `"                else \"attempted_no_usable_sources\" if search_attempted"` | — |
| [SRC-1AE03B9EC3-L006426](../../agents/web_agent.py#L6426) | 6426 | `"                else \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L006427](../../agents/web_agent.py#L6427) | 6427 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006428](../../agents/web_agent.py#L6428) | 6428 | `"        report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006429](../../agents/web_agent.py#L6429) | 6429 | `"        report[\"research_quality\"] = research_quality"` | — |
| [SRC-1AE03B9EC3-L006430](../../agents/web_agent.py#L6430) | 6430 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L006431](../../agents/web_agent.py#L6431) | 6431 | `"        report[\"answer_evidence_status\"] = answer_evidence_status"` | — |
| [SRC-1AE03B9EC3-L006432](../../agents/web_agent.py#L6432) | 6432 | `"        report[\"distinct_registrable_domains\"] = len(distinct_domains)"` | — |
| [SRC-1AE03B9EC3-L006433](../../agents/web_agent.py#L6433) | 6433 | `"        report[\"independent_sources\"] = len(distinct_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L006434](../../agents/web_agent.py#L6434) | 6434 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L006435](../../agents/web_agent.py#L6435) | 6435 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L006436](../../agents/web_agent.py#L6436) | 6436 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006437](../../agents/web_agent.py#L6437) | 6437 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L006438](../../agents/web_agent.py#L6438) | 6438 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L006439](../../agents/web_agent.py#L6439) | 6439 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006440](../../agents/web_agent.py#L6440) | 6440 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L006441](../../agents/web_agent.py#L6441) | 6441 | `"        report[\"claim_audit_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L006442](../../agents/web_agent.py#L6442) | 6442 | `"            \"model_assisted_not_independent_fact_check\""` | — |
| [SRC-1AE03B9EC3-L006443](../../agents/web_agent.py#L6443) | 6443 | `"            if review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006444](../../agents/web_agent.py#L6444) | 6444 | `"            else \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L006445](../../agents/web_agent.py#L6445) | 6445 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006446](../../agents/web_agent.py#L6446) | 6446 | `"        report[\"insufficient_evidence\"] = bool("` | — |
| [SRC-1AE03B9EC3-L006447](../../agents/web_agent.py#L6447) | 6447 | `"            report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L006448](../../agents/web_agent.py#L6448) | 6448 | `"            or not sources"` | — |
| [SRC-1AE03B9EC3-L006449](../../agents/web_agent.py#L6449) | 6449 | `"            or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006450](../../agents/web_agent.py#L6450) | 6450 | `"            or ("` | — |
| [SRC-1AE03B9EC3-L006451](../../agents/web_agent.py#L6451) | 6451 | `"                bool(coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L006452](../../agents/web_agent.py#L6452) | 6452 | `"                and answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006453](../../agents/web_agent.py#L6453) | 6453 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006454](../../agents/web_agent.py#L6454) | 6454 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006455](../../agents/web_agent.py#L6455) | 6455 | `"        report[\"valid_citation_range\"] = [1, max_citable_sources] if max_citable_sources else []"` | — |
| [SRC-1AE03B9EC3-L006456](../../agents/web_agent.py#L6456) | 6456 | `"        report[\"citation_count\"] = citation_validation[\"valid_citation_count\"]"` | — |
| [SRC-1AE03B9EC3-L006457](../../agents/web_agent.py#L6457) | 6457 | `"        report[\"citation_check\"] = citation_validation[\"status\"]"` | — |
| [SRC-1AE03B9EC3-L006458](../../agents/web_agent.py#L6458) | 6458 | `"        report[\"citation_validation\"] = citation_validation"` | — |
| [SRC-1AE03B9EC3-L006459](../../agents/web_agent.py#L6459) | 6459 | `"        warnings = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L006460](../../agents/web_agent.py#L6460) | 6460 | `"            search_warnings"` | — |
| [SRC-1AE03B9EC3-L006461](../../agents/web_agent.py#L6461) | 6461 | `"            + ([llm_warning] if llm_warning else [])"` | — |
| [SRC-1AE03B9EC3-L006462](../../agents/web_agent.py#L6462) | 6462 | `"            + ([review_warning] if review_warning else [])"` | — |
| [SRC-1AE03B9EC3-L006463](../../agents/web_agent.py#L6463) | 6463 | `"            + ([coverage_repair_warning] if coverage_repair_warning else [])"` | — |
| [SRC-1AE03B9EC3-L006464](../../agents/web_agent.py#L6464) | 6464 | `"            + citation_warnings"` | — |
| [SRC-1AE03B9EC3-L006465](../../agents/web_agent.py#L6465) | 6465 | `"            + ([uncited_answer_warning] if uncited_answer_warning else [])"` | — |
| [SRC-1AE03B9EC3-L006466](../../agents/web_agent.py#L6466) | 6466 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L006467](../../agents/web_agent.py#L6467) | 6467 | `"        report[\"model_calls\"] = list(self.model_usage)"` | — |
| [SRC-1AE03B9EC3-L006468](../../agents/web_agent.py#L6468) | 6468 | `"        report[\"openrouter_web_search_enabled\"] = self.openrouter_web_search_enabled"` | — |
| [SRC-1AE03B9EC3-L006469](../../agents/web_agent.py#L6469) | 6469 | `"        report[\"openrouter_web_search_results\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L006470](../../agents/web_agent.py#L6470) | 6470 | `"        if generation_budget_exhausted or review_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L006471](../../agents/web_agent.py#L6471) | 6471 | `"            final_answer_status = \"budget_exhausted_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L006472](../../agents/web_agent.py#L6472) | 6472 | `"        elif llm_warning:"` | — |
| [SRC-1AE03B9EC3-L006473](../../agents/web_agent.py#L6473) | 6473 | `"            final_answer_status = ("` | — |
| [SRC-1AE03B9EC3-L006474](../../agents/web_agent.py#L6474) | 6474 | `"                \"model_not_configured_fallback\""` | — |
| [SRC-1AE03B9EC3-L006475](../../agents/web_agent.py#L6475) | 6475 | `"                if not self.api_key"` | — |
| [SRC-1AE03B9EC3-L006476](../../agents/web_agent.py#L6476) | 6476 | `"                else \"generation_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L006477](../../agents/web_agent.py#L6477) | 6477 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006478](../../agents/web_agent.py#L6478) | 6478 | `"        elif review_warning:"` | — |
| [SRC-1AE03B9EC3-L006479](../../agents/web_agent.py#L6479) | 6479 | `"            final_answer_status = \"review_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L006480](../../agents/web_agent.py#L6480) | 6480 | `"        elif coverage_repair_status == \"no_change_gap_unresolved\":"` | — |
| [SRC-1AE03B9EC3-L006481](../../agents/web_agent.py#L6481) | 6481 | `"            final_answer_status = \"coverage_repair_left_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L006482](../../agents/web_agent.py#L6482) | 6482 | `"        elif coverage_repair_status == \"budget_exhausted\":"` | — |
| [SRC-1AE03B9EC3-L006483](../../agents/web_agent.py#L6483) | 6483 | `"            final_answer_status = \"coverage_repair_budget_exhausted_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L006484](../../agents/web_agent.py#L6484) | 6484 | `"        elif coverage_repair_status == \"unavailable\":"` | — |
| [SRC-1AE03B9EC3-L006485](../../agents/web_agent.py#L6485) | 6485 | `"            final_answer_status = \"coverage_repair_unavailable_with_possible_gap\""` | — |
| [SRC-1AE03B9EC3-L006486](../../agents/web_agent.py#L6486) | 6486 | `"        elif used_llm:"` | — |
| [SRC-1AE03B9EC3-L006487](../../agents/web_agent.py#L6487) | 6487 | `"            final_answer_status = \"model_answer_generated\""` | — |
| [SRC-1AE03B9EC3-L006488](../../agents/web_agent.py#L6488) | 6488 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L006489](../../agents/web_agent.py#L6489) | 6489 | `"            final_answer_status = \"source_fallback\""` | — |
| [SRC-1AE03B9EC3-L006490](../../agents/web_agent.py#L6490) | 6490 | `""` | — |
| [SRC-1AE03B9EC3-L006491](../../agents/web_agent.py#L6491) | 6491 | `"        # Report pipeline completion separately from factual correctness. A successful"` | — |
| [SRC-1AE03B9EC3-L006492](../../agents/web_agent.py#L6492) | 6492 | `"        # retrieval or model review is not an independent semantic fact check."` | — |
| [SRC-1AE03B9EC3-L006493](../../agents/web_agent.py#L6493) | 6493 | `"        if report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L006494](../../agents/web_agent.py#L6494) | 6494 | `"            pipeline_completion_status = \"execution_failed\""` | — |
| [SRC-1AE03B9EC3-L006495](../../agents/web_agent.py#L6495) | 6495 | `"        elif not search_attempted:"` | — |
| [SRC-1AE03B9EC3-L006496](../../agents/web_agent.py#L6496) | 6496 | `"            pipeline_completion_status = \"not_verified\""` | — |
| [SRC-1AE03B9EC3-L006497](../../agents/web_agent.py#L6497) | 6497 | `"        elif not sources:"` | — |
| [SRC-1AE03B9EC3-L006498](../../agents/web_agent.py#L6498) | 6498 | `"            pipeline_completion_status = \"insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L006499](../../agents/web_agent.py#L6499) | 6499 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L006500](../../agents/web_agent.py#L6500) | 6500 | `"            llm_warning"` | — |
| [SRC-1AE03B9EC3-L006501](../../agents/web_agent.py#L6501) | 6501 | `"            or review_warning"` | — |
| [SRC-1AE03B9EC3-L006502](../../agents/web_agent.py#L6502) | 6502 | `"            or review_status != \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006503](../../agents/web_agent.py#L6503) | 6503 | `"            or answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006504](../../agents/web_agent.py#L6504) | 6504 | `"            or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006505](../../agents/web_agent.py#L6505) | 6505 | `"            or citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L006506](../../agents/web_agent.py#L6506) | 6506 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006507](../../agents/web_agent.py#L6507) | 6507 | `"            pipeline_completion_status = \"partial\""` | — |
| [SRC-1AE03B9EC3-L006508](../../agents/web_agent.py#L6508) | 6508 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L006509](../../agents/web_agent.py#L6509) | 6509 | `"            pipeline_completion_status = \"completed\""` | — |
| [SRC-1AE03B9EC3-L006510](../../agents/web_agent.py#L6510) | 6510 | `"        completion_stages = {"` | — |
| [SRC-1AE03B9EC3-L006511](../../agents/web_agent.py#L6511) | 6511 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L006512](../../agents/web_agent.py#L6512) | 6512 | `"            \"accepted_sources\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L006513](../../agents/web_agent.py#L6513) | 6513 | `"            \"pages_read\": fetched_pages,"` | — |
| [SRC-1AE03B9EC3-L006514](../../agents/web_agent.py#L6514) | 6514 | `"            \"answer_generated_by_model\": bool(used_llm),"` | — |
| [SRC-1AE03B9EC3-L006515](../../agents/web_agent.py#L6515) | 6515 | `"            \"claim_review\": review_status,"` | — |
| [SRC-1AE03B9EC3-L006516](../../agents/web_agent.py#L6516) | 6516 | `"            \"valid_citations\": citation_validation[\"valid_citation_count\"],"` | — |
| [SRC-1AE03B9EC3-L006517](../../agents/web_agent.py#L6517) | 6517 | `"            \"semantic_fact_check\": \"not_performed\","` | — |
| [SRC-1AE03B9EC3-L006518](../../agents/web_agent.py#L6518) | 6518 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006519](../../agents/web_agent.py#L6519) | 6519 | `"        report[\"pipeline_completion_status\"] = pipeline_completion_status"` | — |
| [SRC-1AE03B9EC3-L006520](../../agents/web_agent.py#L6520) | 6520 | `"        report[\"completion_stages\"] = completion_stages"` | — |
| [SRC-1AE03B9EC3-L006521](../../agents/web_agent.py#L6521) | 6521 | `"        report[\"pipeline_completion_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L006522](../../agents/web_agent.py#L6522) | 6522 | `"            \"pipeline stage completion only; not a guarantee of factual correctness\""` | — |
| [SRC-1AE03B9EC3-L006523](../../agents/web_agent.py#L6523) | 6523 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006524](../../agents/web_agent.py#L6524) | 6524 | `""` | — |
| [SRC-1AE03B9EC3-L006525](../../agents/web_agent.py#L6525) | 6525 | `"        public_sources = []"` | — |
| [SRC-1AE03B9EC3-L006526](../../agents/web_agent.py#L6526) | 6526 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L006527](../../agents/web_agent.py#L6527) | 6527 | `"            public_sources.append({"` | — |
| [SRC-1AE03B9EC3-L006528](../../agents/web_agent.py#L6528) | 6528 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L006529](../../agents/web_agent.py#L6529) | 6529 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L006530](../../agents/web_agent.py#L6530) | 6530 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L006531](../../agents/web_agent.py#L6531) | 6531 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L006532](../../agents/web_agent.py#L6532) | 6532 | `"                \"readable_page_text_available\": bool(source.get(\"page_fetched\")) and bool(str(source.get(\"page_text\") or \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L006533](../../agents/web_agent.py#L6533) | 6533 | `"                \"page_text_present_without_fetch_flag\": bool(str(source.get(\"page_text\") or \"\").strip()) and not bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L006534](../../agents/web_agent.py#L6534) | 6534 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L006535](../../agents/web_agent.py#L6535) | 6535 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L006536](../../agents/web_agent.py#L6536) | 6536 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L006537](../../agents/web_agent.py#L6537) | 6537 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L006538](../../agents/web_agent.py#L6538) | 6538 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L006539](../../agents/web_agent.py#L6539) | 6539 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L006540](../../agents/web_agent.py#L6540) | 6540 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L006541](../../agents/web_agent.py#L6541) | 6541 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L006542](../../agents/web_agent.py#L6542) | 6542 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L006543](../../agents/web_agent.py#L6543) | 6543 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L006544](../../agents/web_agent.py#L6544) | 6544 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L006545](../../agents/web_agent.py#L6545) | 6545 | `"            })"` | — |
| [SRC-1AE03B9EC3-L006546](../../agents/web_agent.py#L6546) | 6546 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L006547](../../agents/web_agent.py#L6547) | 6547 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L006548](../../agents/web_agent.py#L6548) | 6548 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L006549](../../agents/web_agent.py#L6549) | 6549 | `"            \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L006550](../../agents/web_agent.py#L6550) | 6550 | `"            \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L006551](../../agents/web_agent.py#L6551) | 6551 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L006552](../../agents/web_agent.py#L6552) | 6552 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L006553](../../agents/web_agent.py#L6553) | 6553 | `"                \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L006554](../../agents/web_agent.py#L6554) | 6554 | `"                \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L006555](../../agents/web_agent.py#L6555) | 6555 | `"                \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L006556](../../agents/web_agent.py#L6556) | 6556 | `"                \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L006557](../../agents/web_agent.py#L6557) | 6557 | `"                \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L006558](../../agents/web_agent.py#L6558) | 6558 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L006559](../../agents/web_agent.py#L6559) | 6559 | `"                \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L006560](../../agents/web_agent.py#L6560) | 6560 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L006561](../../agents/web_agent.py#L6561) | 6561 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L006562](../../agents/web_agent.py#L6562) | 6562 | `"            },"` | — |
| [SRC-1AE03B9EC3-L006563](../../agents/web_agent.py#L6563) | 6563 | `"            \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L006564](../../agents/web_agent.py#L6564) | 6564 | `"            \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L006565](../../agents/web_agent.py#L6565) | 6565 | `"            \"research_quality\": research_quality,"` | — |
| [SRC-1AE03B9EC3-L006566](../../agents/web_agent.py#L6566) | 6566 | `"            \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L006567](../../agents/web_agent.py#L6567) | 6567 | `"            \"answer_evidence_status\": answer_evidence_status,"` | — |
| [SRC-1AE03B9EC3-L006568](../../agents/web_agent.py#L6568) | 6568 | `"            \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L006569](../../agents/web_agent.py#L6569) | 6569 | `"            \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L006570](../../agents/web_agent.py#L6570) | 6570 | `"            \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L006571](../../agents/web_agent.py#L6571) | 6571 | `"            \"coverage_repair_status\": coverage_repair_status,"` | — |
| [SRC-1AE03B9EC3-L006572](../../agents/web_agent.py#L6572) | 6572 | `"            \"used_language_model\": used_llm,"` | — |
| [SRC-1AE03B9EC3-L006573](../../agents/web_agent.py#L6573) | 6573 | `"            \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L006574](../../agents/web_agent.py#L6574) | 6574 | `"            \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L006575](../../agents/web_agent.py#L6575) | 6575 | `"            \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L006576](../../agents/web_agent.py#L6576) | 6576 | `"            \"warnings\": warnings,"` | — |
| [SRC-1AE03B9EC3-L006577](../../agents/web_agent.py#L6577) | 6577 | `"            \"kind\": \"web_research\" if used_llm else \"web_fallback\","` | — |
| [SRC-1AE03B9EC3-L006578](../../agents/web_agent.py#L6578) | 6578 | `"            \"final_answer_status\": final_answer_status,"` | — |
| [SRC-1AE03B9EC3-L006579](../../agents/web_agent.py#L6579) | 6579 | `"            \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L006580](../../agents/web_agent.py#L6580) | 6580 | `"            \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L006581](../../agents/web_agent.py#L6581) | 6581 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006582](../../agents/web_agent.py#L6582) | 6582 | `""` | — |
| [SRC-1AE03B9EC3-L006583](../../agents/web_agent.py#L6583) | 6583 | `""` | — |
| [SRC-1AE03B9EC3-L006584](../../agents/web_agent.py#L6584) | 6584 | `"def _normalized_provider_usage("` | — |
| [SRC-1AE03B9EC3-L006585](../../agents/web_agent.py#L6585) | 6585 | `"    usage: Any, *, provider_base_url: str = \"\""` | — |
| [SRC-1AE03B9EC3-L006586](../../agents/web_agent.py#L6586) | 6586 | `") -> dict[str, int \| float] \| None:"` | — |
| [SRC-1AE03B9EC3-L006587](../../agents/web_agent.py#L6587) | 6587 | `"    \"\"\"Allowlist safe counters; interpret generic 'cost' as USD only for OpenRouter.\"\"\""` | — |
| [SRC-1AE03B9EC3-L006588](../../agents/web_agent.py#L6588) | 6588 | `"    if not isinstance(usage, dict):"` | — |
| [SRC-1AE03B9EC3-L006589](../../agents/web_agent.py#L6589) | 6589 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L006590](../../agents/web_agent.py#L6590) | 6590 | `"    normalized: dict[str, int \| float] = {}"` | — |
| [SRC-1AE03B9EC3-L006591](../../agents/web_agent.py#L6591) | 6591 | `"    for source_key in (\"prompt_tokens\", \"completion_tokens\", \"total_tokens\"):"` | — |
| [SRC-1AE03B9EC3-L006592](../../agents/web_agent.py#L6592) | 6592 | `"        value = usage.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L006593](../../agents/web_agent.py#L6593) | 6593 | `"        if isinstance(value, int) and not isinstance(value, bool) and value >= 0:"` | — |
| [SRC-1AE03B9EC3-L006594](../../agents/web_agent.py#L6594) | 6594 | `"            normalized[source_key] = value"` | — |
| [SRC-1AE03B9EC3-L006595](../../agents/web_agent.py#L6595) | 6595 | `"    cost_keys = [\"cost_usd\"]"` | — |
| [SRC-1AE03B9EC3-L006596](../../agents/web_agent.py#L6596) | 6596 | `"    provider_host = \"\""` | — |
| [SRC-1AE03B9EC3-L006597](../../agents/web_agent.py#L6597) | 6597 | `"    if isinstance(provider_base_url, str):"` | — |
| [SRC-1AE03B9EC3-L006598](../../agents/web_agent.py#L6598) | 6598 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L006599](../../agents/web_agent.py#L6599) | 6599 | `"            provider_host = (urllib.parse.urlsplit(provider_base_url.strip()).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L006600](../../agents/web_agent.py#L6600) | 6600 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L006601](../../agents/web_agent.py#L6601) | 6601 | `"            provider_host = \"\""` | — |
| [SRC-1AE03B9EC3-L006602](../../agents/web_agent.py#L6602) | 6602 | `"    is_openrouter = ("` | — |
| [SRC-1AE03B9EC3-L006603](../../agents/web_agent.py#L6603) | 6603 | `"        provider_host == \"openrouter.ai\""` | — |
| [SRC-1AE03B9EC3-L006604](../../agents/web_agent.py#L6604) | 6604 | `"        or provider_host.endswith(\".openrouter.ai\")"` | — |
| [SRC-1AE03B9EC3-L006605](../../agents/web_agent.py#L6605) | 6605 | `"    )"` | — |
| [SRC-1AE03B9EC3-L006606](../../agents/web_agent.py#L6606) | 6606 | `"    if is_openrouter:"` | — |
| [SRC-1AE03B9EC3-L006607](../../agents/web_agent.py#L6607) | 6607 | `"        cost_keys.extend([\"cost\", \"total_cost\"])"` | — |
| [SRC-1AE03B9EC3-L006608](../../agents/web_agent.py#L6608) | 6608 | `"    for source_key in cost_keys:"` | — |
| [SRC-1AE03B9EC3-L006609](../../agents/web_agent.py#L6609) | 6609 | `"        value = usage.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L006610](../../agents/web_agent.py#L6610) | 6610 | `"        if isinstance(value, (int, float)) and not isinstance(value, bool):"` | — |
| [SRC-1AE03B9EC3-L006611](../../agents/web_agent.py#L6611) | 6611 | `"            number = float(value)"` | — |
| [SRC-1AE03B9EC3-L006612](../../agents/web_agent.py#L6612) | 6612 | `"            if number >= 0 and math.isfinite(number):"` | — |
| [SRC-1AE03B9EC3-L006613](../../agents/web_agent.py#L6613) | 6613 | `"                normalized[\"cost_usd\"] = number"` | — |
| [SRC-1AE03B9EC3-L006614](../../agents/web_agent.py#L6614) | 6614 | `"                break"` | — |
| [SRC-1AE03B9EC3-L006615](../../agents/web_agent.py#L6615) | 6615 | `"    return normalized or None"` | — |
| [SRC-1AE03B9EC3-L006616](../../agents/web_agent.py#L6616) | 6616 | `""` | — |
| [SRC-1AE03B9EC3-L006617](../../agents/web_agent.py#L6617) | 6617 | `""` | — |
| [SRC-1AE03B9EC3-L006618](../../agents/web_agent.py#L6618) | 6618 | `"def _model_usage_record("` | — |
| [SRC-1AE03B9EC3-L006619](../../agents/web_agent.py#L6619) | 6619 | `"    requested_model: str,"` | — |
| [SRC-1AE03B9EC3-L006620](../../agents/web_agent.py#L6620) | 6620 | `"    candidate_model: str,"` | — |
| [SRC-1AE03B9EC3-L006621](../../agents/web_agent.py#L6621) | 6621 | `"    response_data: dict[str, Any],"` | — |
| [SRC-1AE03B9EC3-L006622](../../agents/web_agent.py#L6622) | 6622 | `"    provider_base_url: str,"` | — |
| [SRC-1AE03B9EC3-L006623](../../agents/web_agent.py#L6623) | 6623 | `") -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L006624](../../agents/web_agent.py#L6624) | 6624 | `"    \"\"\"Return only allowlisted provider usage metadata, never raw prompts/responses.\"\"\""` | — |
| [SRC-1AE03B9EC3-L006625](../../agents/web_agent.py#L6625) | 6625 | `"    record: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L006626](../../agents/web_agent.py#L6626) | 6626 | `"        \"requested_model\": requested_model,"` | — |
| [SRC-1AE03B9EC3-L006627](../../agents/web_agent.py#L6627) | 6627 | `"        \"used_model\": candidate_model,"` | — |
| [SRC-1AE03B9EC3-L006628](../../agents/web_agent.py#L6628) | 6628 | `"        \"fallback_used\": \"true\" if candidate_model != requested_model else \"false\","` | — |
| [SRC-1AE03B9EC3-L006629](../../agents/web_agent.py#L6629) | 6629 | `"    }"` | — |
| [SRC-1AE03B9EC3-L006630](../../agents/web_agent.py#L6630) | 6630 | `"    provider_usage = _normalized_provider_usage("` | — |
| [SRC-1AE03B9EC3-L006631](../../agents/web_agent.py#L6631) | 6631 | `"        response_data.get(\"usage\"), provider_base_url=provider_base_url"` | — |
| [SRC-1AE03B9EC3-L006632](../../agents/web_agent.py#L6632) | 6632 | `"    )"` | — |
| [SRC-1AE03B9EC3-L006633](../../agents/web_agent.py#L6633) | 6633 | `"    if provider_usage is not None:"` | — |
| [SRC-1AE03B9EC3-L006634](../../agents/web_agent.py#L6634) | 6634 | `"        record[\"provider_usage\"] = provider_usage"` | — |
| [SRC-1AE03B9EC3-L006635](../../agents/web_agent.py#L6635) | 6635 | `"    return record"` | — |
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
| [SRC-EEF2E6447C-L000010](../../api/omarai.py#L10) | 10 | `"import re"` | — |
| [SRC-EEF2E6447C-L000011](../../api/omarai.py#L11) | 11 | `"import threading"` | — |
| [SRC-EEF2E6447C-L000012](../../api/omarai.py#L12) | 12 | `"import time"` | — |
| [SRC-EEF2E6447C-L000013](../../api/omarai.py#L13) | 13 | `"from collections import defaultdict, deque"` | — |
| [SRC-EEF2E6447C-L000014](../../api/omarai.py#L14) | 14 | `"from functools import lru_cache"` | — |
| [SRC-EEF2E6447C-L000015](../../api/omarai.py#L15) | 15 | `"from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer"` | — |
| [SRC-EEF2E6447C-L000016](../../api/omarai.py#L16) | 16 | `"from pathlib import Path"` | — |
| [SRC-EEF2E6447C-L000017](../../api/omarai.py#L17) | 17 | `"from typing import ClassVar"` | — |
| [SRC-EEF2E6447C-L000018](../../api/omarai.py#L18) | 18 | `"from urllib.parse import parse_qs, urlparse"` | — |
| [SRC-EEF2E6447C-L000019](../../api/omarai.py#L19) | 19 | `""` | — |
| [SRC-EEF2E6447C-L000020](../../api/omarai.py#L20) | 20 | `"from agents.omarai import LeadStore, analyze, normalize"` | — |
| [SRC-EEF2E6447C-L000021](../../api/omarai.py#L21) | 21 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-EEF2E6447C-L000022](../../api/omarai.py#L22) | 22 | `""` | — |
| [SRC-EEF2E6447C-L000023](../../api/omarai.py#L23) | 23 | `"ROOT = Path(__file__).resolve().parents[1] / \"web\""` | — |
| [SRC-EEF2E6447C-L000024](../../api/omarai.py#L24) | 24 | `"AGENT_DASHBOARD = ROOT / \"agent.html\""` | — |
| [SRC-EEF2E6447C-L000025](../../api/omarai.py#L25) | 25 | `"LEADS_DASHBOARD = ROOT / \"dashboard.html\""` | — |
| [SRC-EEF2E6447C-L000026](../../api/omarai.py#L26) | 26 | `"MAX_REQUEST_BODY_BYTES = 200_000"` | — |
| [SRC-EEF2E6447C-L000027](../../api/omarai.py#L27) | 27 | `""` | — |
| [SRC-EEF2E6447C-L000028](../../api/omarai.py#L28) | 28 | `""` | — |
| [SRC-EEF2E6447C-L000029](../../api/omarai.py#L29) | 29 | `"def _csp_hash_source(value: str) -> str:"` | — |
| [SRC-EEF2E6447C-L000030](../../api/omarai.py#L30) | 30 | `"    digest = base64.b64encode(hashlib.sha256(value.encode(\"utf-8\")).digest()).decode(\"ascii\")"` | — |
| [SRC-EEF2E6447C-L000031](../../api/omarai.py#L31) | 31 | `"    return f\"'sha256-{digest}'\""` | — |
| [SRC-EEF2E6447C-L000032](../../api/omarai.py#L32) | 32 | `""` | — |
| [SRC-EEF2E6447C-L000033](../../api/omarai.py#L33) | 33 | `""` | — |
| [SRC-EEF2E6447C-L000034](../../api/omarai.py#L34) | 34 | `"@lru_cache(maxsize=1)"` | — |
| [SRC-EEF2E6447C-L000035](../../api/omarai.py#L35) | 35 | `"def _content_security_policy() -> str:"` | — |
| [SRC-EEF2E6447C-L000036](../../api/omarai.py#L36) | 36 | `"    \"\"\"Allow only known inline blocks/attributes from the static first-party HTML."` | — |
| [SRC-EEF2E6447C-L000037](../../api/omarai.py#L37) | 37 | `""` | — |
| [SRC-EEF2E6447C-L000038](../../api/omarai.py#L38) | 38 | `"    Hashes deliberately replace unsafe-inline. Updating an inline script/style means its"` | — |
| [SRC-EEF2E6447C-L000039](../../api/omarai.py#L39) | 39 | `"    hash changes automatically with the served source. This is not a sanitizer for"` | — |
| [SRC-EEF2E6447C-L000040](../../api/omarai.py#L40) | 40 | `"    untrusted HTML; callers must never splice untrusted input into these static files."` | — |
| [SRC-EEF2E6447C-L000041](../../api/omarai.py#L41) | 41 | `"    \"\"\""` | — |
| [SRC-EEF2E6447C-L000042](../../api/omarai.py#L42) | 42 | `"    script_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000043](../../api/omarai.py#L43) | 43 | `"    style_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000044](../../api/omarai.py#L44) | 44 | `"    event_handler_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000045](../../api/omarai.py#L45) | 45 | `"    style_attribute_hashes: set[str] = set()"` | — |
| [SRC-EEF2E6447C-L000046](../../api/omarai.py#L46) | 46 | `""` | — |
| [SRC-EEF2E6447C-L000047](../../api/omarai.py#L47) | 47 | `"    for html_path in sorted(ROOT.glob(\"*.html\")):"` | — |
| [SRC-EEF2E6447C-L000048](../../api/omarai.py#L48) | 48 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000049](../../api/omarai.py#L49) | 49 | `"            document = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-EEF2E6447C-L000050](../../api/omarai.py#L50) | 50 | `"        except (OSError, UnicodeError):"` | — |
| [SRC-EEF2E6447C-L000051](../../api/omarai.py#L51) | 51 | `"            continue"` | — |
| [SRC-EEF2E6447C-L000052](../../api/omarai.py#L52) | 52 | `""` | — |
| [SRC-EEF2E6447C-L000053](../../api/omarai.py#L53) | 53 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000054](../../api/omarai.py#L54) | 54 | `"            r\"<script\\b(?P<attrs>[^>]*)>(?P<body>.*?)</script\\s*>\","` | — |
| [SRC-EEF2E6447C-L000055](../../api/omarai.py#L55) | 55 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000056](../../api/omarai.py#L56) | 56 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000057](../../api/omarai.py#L57) | 57 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000058](../../api/omarai.py#L58) | 58 | `"            if re.search(r\"\\bsrc\\s*=\", match.group(\"attrs\"), re.IGNORECASE):"` | — |
| [SRC-EEF2E6447C-L000059](../../api/omarai.py#L59) | 59 | `"                continue"` | — |
| [SRC-EEF2E6447C-L000060](../../api/omarai.py#L60) | 60 | `"            script_hashes.add(_csp_hash_source(match.group(\"body\")))"` | — |
| [SRC-EEF2E6447C-L000061](../../api/omarai.py#L61) | 61 | `""` | — |
| [SRC-EEF2E6447C-L000062](../../api/omarai.py#L62) | 62 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000063](../../api/omarai.py#L63) | 63 | `"            r\"<style\\b[^>]*>(?P<body>.*?)</style\\s*>\","` | — |
| [SRC-EEF2E6447C-L000064](../../api/omarai.py#L64) | 64 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000065](../../api/omarai.py#L65) | 65 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000066](../../api/omarai.py#L66) | 66 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000067](../../api/omarai.py#L67) | 67 | `"            style_hashes.add(_csp_hash_source(match.group(\"body\")))"` | — |
| [SRC-EEF2E6447C-L000068](../../api/omarai.py#L68) | 68 | `""` | — |
| [SRC-EEF2E6447C-L000069](../../api/omarai.py#L69) | 69 | `"        # This scan intentionally includes style/event attributes embedded in"` | — |
| [SRC-EEF2E6447C-L000070](../../api/omarai.py#L70) | 70 | `"        # trusted first-party HTML templates assembled by inline scripts."` | — |
| [SRC-EEF2E6447C-L000071](../../api/omarai.py#L71) | 71 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000072](../../api/omarai.py#L72) | 72 | `"            r\"\"\"\\bstyle\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-EEF2E6447C-L000073](../../api/omarai.py#L73) | 73 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000074](../../api/omarai.py#L74) | 74 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000075](../../api/omarai.py#L75) | 75 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000076](../../api/omarai.py#L76) | 76 | `"            style_attribute_hashes.add(_csp_hash_source(match.group(2).strip()))"` | — |
| [SRC-EEF2E6447C-L000077](../../api/omarai.py#L77) | 77 | `""` | — |
| [SRC-EEF2E6447C-L000078](../../api/omarai.py#L78) | 78 | `"        for match in re.finditer("` | — |
| [SRC-EEF2E6447C-L000079](../../api/omarai.py#L79) | 79 | `"            r\"\"\"\\bon[a-z]+\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-EEF2E6447C-L000080](../../api/omarai.py#L80) | 80 | `"            document,"` | — |
| [SRC-EEF2E6447C-L000081](../../api/omarai.py#L81) | 81 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-EEF2E6447C-L000082](../../api/omarai.py#L82) | 82 | `"        ):"` | — |
| [SRC-EEF2E6447C-L000083](../../api/omarai.py#L83) | 83 | `"            event_handler_hashes.add(_csp_hash_source(match.group(2).strip()))"` | — |
| [SRC-EEF2E6447C-L000084](../../api/omarai.py#L84) | 84 | `""` | — |
| [SRC-EEF2E6447C-L000085](../../api/omarai.py#L85) | 85 | `"    script_sources = [\"'self'\", *sorted(script_hashes)]"` | — |
| [SRC-EEF2E6447C-L000086](../../api/omarai.py#L86) | 86 | `"    style_sources = [\"'self'\", *sorted(style_hashes)]"` | — |
| [SRC-EEF2E6447C-L000087](../../api/omarai.py#L87) | 87 | `"    if event_handler_hashes:"` | — |
| [SRC-EEF2E6447C-L000088](../../api/omarai.py#L88) | 88 | `"        script_sources.extend([\"'unsafe-hashes'\", *sorted(event_handler_hashes)])"` | — |
| [SRC-EEF2E6447C-L000089](../../api/omarai.py#L89) | 89 | `"    if style_attribute_hashes:"` | — |
| [SRC-EEF2E6447C-L000090](../../api/omarai.py#L90) | 90 | `"        style_sources.extend([\"'unsafe-hashes'\", *sorted(style_attribute_hashes)])"` | — |
| [SRC-EEF2E6447C-L000091](../../api/omarai.py#L91) | 91 | `""` | — |
| [SRC-EEF2E6447C-L000092](../../api/omarai.py#L92) | 92 | `"    return ("` | — |
| [SRC-EEF2E6447C-L000093](../../api/omarai.py#L93) | 93 | `"        \"default-src 'self'; base-uri 'self'; object-src 'none'; frame-ancestors 'none'; \""` | — |
| [SRC-EEF2E6447C-L000094](../../api/omarai.py#L94) | 94 | `"        \"form-action 'self'; connect-src 'self'; img-src 'self' data:; \""` | — |
| [SRC-EEF2E6447C-L000095](../../api/omarai.py#L95) | 95 | `"        f\"script-src {' '.join(script_sources)}; \""` | — |
| [SRC-EEF2E6447C-L000096](../../api/omarai.py#L96) | 96 | `"        f\"style-src {' '.join(style_sources)}; font-src 'self' data:\""` | — |
| [SRC-EEF2E6447C-L000097](../../api/omarai.py#L97) | 97 | `"    )"` | — |
| [SRC-EEF2E6447C-L000098](../../api/omarai.py#L98) | 98 | `"# Bound request-line + header parsing before application code or body processing."` | — |
| [SRC-EEF2E6447C-L000099](../../api/omarai.py#L99) | 99 | `"REQUEST_HEADER_READ_TIMEOUT_SECONDS = 8.0"` | — |
| [SRC-EEF2E6447C-L000100](../../api/omarai.py#L100) | 100 | `"REQUEST_HEADER_IDLE_TIMEOUT_SECONDS = 2.0"` | — |
| [SRC-EEF2E6447C-L000101](../../api/omarai.py#L101) | 101 | `"MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS = 15.0"` | — |
| [SRC-EEF2E6447C-L000102](../../api/omarai.py#L102) | 102 | `"# Absolute deadline for reading the entire body, not merely a per-read idle timeout."` | — |
| [SRC-EEF2E6447C-L000103](../../api/omarai.py#L103) | 103 | `"REQUEST_BODY_READ_TIMEOUT_SECONDS = 10.0"` | — |
| [SRC-EEF2E6447C-L000104](../../api/omarai.py#L104) | 104 | `"REQUEST_BODY_IDLE_TIMEOUT_SECONDS = 2.0"` | — |
| [SRC-EEF2E6447C-L000105](../../api/omarai.py#L105) | 105 | `"MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS = 30.0"` | — |
| [SRC-EEF2E6447C-L000106](../../api/omarai.py#L106) | 106 | `"REQUEST_BODY_READ_CHUNK_BYTES = 8_192"` | — |
| [SRC-EEF2E6447C-L000107](../../api/omarai.py#L107) | 107 | `""` | — |
| [SRC-EEF2E6447C-L000108](../../api/omarai.py#L108) | 108 | `""` | — |
| [SRC-EEF2E6447C-L000109](../../api/omarai.py#L109) | 109 | `""` | — |
| [SRC-EEF2E6447C-L000110](../../api/omarai.py#L110) | 110 | `"def _lead_store_from_environment() -> LeadStore:"` | — |
| [SRC-EEF2E6447C-L000111](../../api/omarai.py#L111) | 111 | `"    \"\"\"Use an operator-configured database path when a persistent volume is available.\"\"\""` | — |
| [SRC-EEF2E6447C-L000112](../../api/omarai.py#L112) | 112 | `"    configured_path = os.getenv(\"OMARAI_DB_PATH\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000113](../../api/omarai.py#L113) | 113 | `"    return LeadStore(configured_path or None)"` | — |
| [SRC-EEF2E6447C-L000114](../../api/omarai.py#L114) | 114 | `""` | — |
| [SRC-EEF2E6447C-L000115](../../api/omarai.py#L115) | 115 | `""` | — |
| [SRC-EEF2E6447C-L000116](../../api/omarai.py#L116) | 116 | `"class _DeadlineRequestReader:"` | — |
| [SRC-EEF2E6447C-L000117](../../api/omarai.py#L117) | 117 | `"    \"\"\"Read HTTP header lines with one absolute deadline across all fragments."` | — |
| [SRC-EEF2E6447C-L000118](../../api/omarai.py#L118) | 118 | `""` | — |
| [SRC-EEF2E6447C-L000119](../../api/omarai.py#L119) | 119 | `"    The standard buffered readline can wait indefinitely for a newline if a"` | — |
| [SRC-EEF2E6447C-L000120](../../api/omarai.py#L120) | 120 | `"    client keeps trickling bytes. This reader checks the same deadline before"` | — |
| [SRC-EEF2E6447C-L000121](../../api/omarai.py#L121) | 121 | `"    every socket read and buffers only bounded look-ahead so request body bytes"` | — |
| [SRC-EEF2E6447C-L000122](../../api/omarai.py#L122) | 122 | `"    received with the headers are preserved for read1()."` | — |
| [SRC-EEF2E6447C-L000123](../../api/omarai.py#L123) | 123 | `"    \"\"\""` | — |
| [SRC-EEF2E6447C-L000124](../../api/omarai.py#L124) | 124 | `""` | — |
| [SRC-EEF2E6447C-L000125](../../api/omarai.py#L125) | 125 | `"    def __init__(self, connection, handler):"` | — |
| [SRC-EEF2E6447C-L000126](../../api/omarai.py#L126) | 126 | `"        self.connection = connection"` | — |
| [SRC-EEF2E6447C-L000127](../../api/omarai.py#L127) | 127 | `"        self.handler = handler"` | — |
| [SRC-EEF2E6447C-L000128](../../api/omarai.py#L128) | 128 | `"        self._buffer = bytearray()"` | — |
| [SRC-EEF2E6447C-L000129](../../api/omarai.py#L129) | 129 | `""` | — |
| [SRC-EEF2E6447C-L000130](../../api/omarai.py#L130) | 130 | `"    def readline(self, limit=-1):"` | — |
| [SRC-EEF2E6447C-L000131](../../api/omarai.py#L131) | 131 | `"        if limit == 0:"` | — |
| [SRC-EEF2E6447C-L000132](../../api/omarai.py#L132) | 132 | `"            return b\"\""` | — |
| [SRC-EEF2E6447C-L000133](../../api/omarai.py#L133) | 133 | `"        max_bytes = int(limit) if limit is not None and limit > 0 else 65_537"` | — |
| [SRC-EEF2E6447C-L000134](../../api/omarai.py#L134) | 134 | `"        previous_timeout = self.connection.gettimeout()"` | — |
| [SRC-EEF2E6447C-L000135](../../api/omarai.py#L135) | 135 | `"        line = bytearray()"` | — |
| [SRC-EEF2E6447C-L000136](../../api/omarai.py#L136) | 136 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000137](../../api/omarai.py#L137) | 137 | `"            while len(line) < max_bytes:"` | — |
| [SRC-EEF2E6447C-L000138](../../api/omarai.py#L138) | 138 | `"                deadline = getattr(self.handler, \"_request_header_deadline\", None)"` | — |
| [SRC-EEF2E6447C-L000139](../../api/omarai.py#L139) | 139 | `"                if deadline is None:"` | — |
| [SRC-EEF2E6447C-L000140](../../api/omarai.py#L140) | 140 | `"                    raise TimeoutError(\"request-header deadline is not active\")"` | — |
| [SRC-EEF2E6447C-L000141](../../api/omarai.py#L141) | 141 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000142](../../api/omarai.py#L142) | 142 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000143](../../api/omarai.py#L143) | 143 | `"                    raise TimeoutError(\"absolute request-header deadline exceeded\")"` | — |
| [SRC-EEF2E6447C-L000144](../../api/omarai.py#L144) | 144 | `""` | — |
| [SRC-EEF2E6447C-L000145](../../api/omarai.py#L145) | 145 | `"                newline_index = self._buffer.find(b\"\\n\")"` | — |
| [SRC-EEF2E6447C-L000146](../../api/omarai.py#L146) | 146 | `"                if newline_index >= 0:"` | — |
| [SRC-EEF2E6447C-L000147](../../api/omarai.py#L147) | 147 | `"                    take = min(newline_index + 1, max_bytes - len(line))"` | — |
| [SRC-EEF2E6447C-L000148](../../api/omarai.py#L148) | 148 | `"                    line.extend(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000149](../../api/omarai.py#L149) | 149 | `"                    del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000150](../../api/omarai.py#L150) | 150 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000151](../../api/omarai.py#L151) | 151 | `""` | — |
| [SRC-EEF2E6447C-L000152](../../api/omarai.py#L152) | 152 | `"                if self._buffer:"` | — |
| [SRC-EEF2E6447C-L000153](../../api/omarai.py#L153) | 153 | `"                    take = min(len(self._buffer), max_bytes - len(line))"` | — |
| [SRC-EEF2E6447C-L000154](../../api/omarai.py#L154) | 154 | `"                    line.extend(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000155](../../api/omarai.py#L155) | 155 | `"                    del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000156](../../api/omarai.py#L156) | 156 | `"                    if len(line) >= max_bytes:"` | — |
| [SRC-EEF2E6447C-L000157](../../api/omarai.py#L157) | 157 | `"                        break"` | — |
| [SRC-EEF2E6447C-L000158](../../api/omarai.py#L158) | 158 | `""` | — |
| [SRC-EEF2E6447C-L000159](../../api/omarai.py#L159) | 159 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000160](../../api/omarai.py#L160) | 160 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000161](../../api/omarai.py#L161) | 161 | `"                    raise TimeoutError(\"absolute request-header deadline exceeded\")"` | — |
| [SRC-EEF2E6447C-L000162](../../api/omarai.py#L162) | 162 | `"                idle_timeout = max("` | — |
| [SRC-EEF2E6447C-L000163](../../api/omarai.py#L163) | 163 | `"                    0.1,"` | — |
| [SRC-EEF2E6447C-L000164](../../api/omarai.py#L164) | 164 | `"                    min("` | — |
| [SRC-EEF2E6447C-L000165](../../api/omarai.py#L165) | 165 | `"                        float(REQUEST_HEADER_IDLE_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000166](../../api/omarai.py#L166) | 166 | `"                        MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000167](../../api/omarai.py#L167) | 167 | `"                    ),"` | — |
| [SRC-EEF2E6447C-L000168](../../api/omarai.py#L168) | 168 | `"                )"` | — |
| [SRC-EEF2E6447C-L000169](../../api/omarai.py#L169) | 169 | `"                self.connection.settimeout(min(idle_timeout, remaining))"` | — |
| [SRC-EEF2E6447C-L000170](../../api/omarai.py#L170) | 170 | `"                chunk = self.connection.recv(min(4_096, max_bytes - len(line)))"` | — |
| [SRC-EEF2E6447C-L000171](../../api/omarai.py#L171) | 171 | `"                if not chunk:"` | — |
| [SRC-EEF2E6447C-L000172](../../api/omarai.py#L172) | 172 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000173](../../api/omarai.py#L173) | 173 | `"                self._buffer.extend(chunk)"` | — |
| [SRC-EEF2E6447C-L000174](../../api/omarai.py#L174) | 174 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000175](../../api/omarai.py#L175) | 175 | `"            try:"` | — |
| [SRC-EEF2E6447C-L000176](../../api/omarai.py#L176) | 176 | `"                self.connection.settimeout(previous_timeout)"` | — |
| [SRC-EEF2E6447C-L000177](../../api/omarai.py#L177) | 177 | `"            except OSError:"` | — |
| [SRC-EEF2E6447C-L000178](../../api/omarai.py#L178) | 178 | `"                pass"` | — |
| [SRC-EEF2E6447C-L000179](../../api/omarai.py#L179) | 179 | `"        return bytes(line)"` | — |
| [SRC-EEF2E6447C-L000180](../../api/omarai.py#L180) | 180 | `""` | — |
| [SRC-EEF2E6447C-L000181](../../api/omarai.py#L181) | 181 | `"    def read1(self, size=-1):"` | — |
| [SRC-EEF2E6447C-L000182](../../api/omarai.py#L182) | 182 | `"        \"\"\"Read one chunk; body code applies its own idle and absolute deadlines.\"\"\""` | — |
| [SRC-EEF2E6447C-L000183](../../api/omarai.py#L183) | 183 | `"        if size == 0:"` | — |
| [SRC-EEF2E6447C-L000184](../../api/omarai.py#L184) | 184 | `"            return b\"\""` | — |
| [SRC-EEF2E6447C-L000185](../../api/omarai.py#L185) | 185 | `"        if size is None or size < 0:"` | — |
| [SRC-EEF2E6447C-L000186](../../api/omarai.py#L186) | 186 | `"            size = 8_192"` | — |
| [SRC-EEF2E6447C-L000187](../../api/omarai.py#L187) | 187 | `"        if self._buffer:"` | — |
| [SRC-EEF2E6447C-L000188](../../api/omarai.py#L188) | 188 | `"            take = min(len(self._buffer), size)"` | — |
| [SRC-EEF2E6447C-L000189](../../api/omarai.py#L189) | 189 | `"            data = bytes(self._buffer[:take])"` | — |
| [SRC-EEF2E6447C-L000190](../../api/omarai.py#L190) | 190 | `"            del self._buffer[:take]"` | — |
| [SRC-EEF2E6447C-L000191](../../api/omarai.py#L191) | 191 | `"            return data"` | — |
| [SRC-EEF2E6447C-L000192](../../api/omarai.py#L192) | 192 | `"        return self.connection.recv(size)"` | — |
| [SRC-EEF2E6447C-L000193](../../api/omarai.py#L193) | 193 | `""` | — |
| [SRC-EEF2E6447C-L000194](../../api/omarai.py#L194) | 194 | `"    def close(self):"` | — |
| [SRC-EEF2E6447C-L000195](../../api/omarai.py#L195) | 195 | `"        # The request handler owns the socket and closes its output stream."` | — |
| [SRC-EEF2E6447C-L000196](../../api/omarai.py#L196) | 196 | `"        return None"` | — |
| [SRC-EEF2E6447C-L000197](../../api/omarai.py#L197) | 197 | `""` | — |
| [SRC-EEF2E6447C-L000198](../../api/omarai.py#L198) | 198 | `""` | — |
| [SRC-EEF2E6447C-L000199](../../api/omarai.py#L199) | 199 | `"def _configured_agent_concurrency_limit() -> int:"` | — |
| [SRC-EEF2E6447C-L000200](../../api/omarai.py#L200) | 200 | `"    \"\"\"Return a process-local cap for expensive research and diagnostics operations.\"\"\""` | — |
| [SRC-EEF2E6447C-L000201](../../api/omarai.py#L201) | 201 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000202](../../api/omarai.py#L202) | 202 | `"        configured = int(os.getenv(\"OMARAI_MAX_CONCURRENT_AGENT_REQUESTS\", \"4\").strip())"` | — |
| [SRC-EEF2E6447C-L000203](../../api/omarai.py#L203) | 203 | `"    except ValueError:"` | — |
| [SRC-EEF2E6447C-L000204](../../api/omarai.py#L204) | 204 | `"        configured = 4"` | — |
| [SRC-EEF2E6447C-L000205](../../api/omarai.py#L205) | 205 | `"    return max(1, min(configured, 8))"` | — |
| [SRC-EEF2E6447C-L000206](../../api/omarai.py#L206) | 206 | `""` | — |
| [SRC-EEF2E6447C-L000207](../../api/omarai.py#L207) | 207 | `""` | — |
| [SRC-EEF2E6447C-L000208](../../api/omarai.py#L208) | 208 | `"DEFAULT_HTTP_CONNECTION_LIMIT = 32"` | — |
| [SRC-EEF2E6447C-L000209](../../api/omarai.py#L209) | 209 | `"MAX_HTTP_CONNECTION_LIMIT = 128"` | — |
| [SRC-EEF2E6447C-L000210](../../api/omarai.py#L210) | 210 | `""` | — |
| [SRC-EEF2E6447C-L000211](../../api/omarai.py#L211) | 211 | `""` | — |
| [SRC-EEF2E6447C-L000212](../../api/omarai.py#L212) | 212 | `"def _configured_http_connection_limit() -> int:"` | — |
| [SRC-EEF2E6447C-L000213](../../api/omarai.py#L213) | 213 | `"    \"\"\"Return the bounded number of live HTTP handler threads for this process.\"\"\""` | — |
| [SRC-EEF2E6447C-L000214](../../api/omarai.py#L214) | 214 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000215](../../api/omarai.py#L215) | 215 | `"        configured = int(os.getenv(\"OMARAI_MAX_CONCURRENT_HTTP_CONNECTIONS\", \"32\").strip())"` | — |
| [SRC-EEF2E6447C-L000216](../../api/omarai.py#L216) | 216 | `"    except ValueError:"` | — |
| [SRC-EEF2E6447C-L000217](../../api/omarai.py#L217) | 217 | `"        configured = DEFAULT_HTTP_CONNECTION_LIMIT"` | — |
| [SRC-EEF2E6447C-L000218](../../api/omarai.py#L218) | 218 | `"    return max(1, min(configured, MAX_HTTP_CONNECTION_LIMIT))"` | — |
| [SRC-EEF2E6447C-L000219](../../api/omarai.py#L219) | 219 | `""` | — |
| [SRC-EEF2E6447C-L000220](../../api/omarai.py#L220) | 220 | `""` | — |
| [SRC-EEF2E6447C-L000221](../../api/omarai.py#L221) | 221 | `"BUILD_SHA_FILE = Path(__file__).resolve().parents[1] / \"BUILD_SHA\""` | — |
| [SRC-EEF2E6447C-L000222](../../api/omarai.py#L222) | 222 | `"_PLATFORM_BUILD_SHA_ENVIRONMENTS = ("` | — |
| [SRC-EEF2E6447C-L000223](../../api/omarai.py#L223) | 223 | `"    (\"RAILWAY_GIT_COMMIT_SHA\", \"platform:railway\"),"` | — |
| [SRC-EEF2E6447C-L000224](../../api/omarai.py#L224) | 224 | `"    (\"RENDER_GIT_COMMIT\", \"platform:render\"),"` | — |
| [SRC-EEF2E6447C-L000225](../../api/omarai.py#L225) | 225 | `")"` | — |
| [SRC-EEF2E6447C-L000226](../../api/omarai.py#L226) | 226 | `""` | — |
| [SRC-EEF2E6447C-L000227](../../api/omarai.py#L227) | 227 | `""` | — |
| [SRC-EEF2E6447C-L000228](../../api/omarai.py#L228) | 228 | `"def _valid_build_sha(value: str) -> bool:"` | — |
| [SRC-EEF2E6447C-L000229](../../api/omarai.py#L229) | 229 | `"    candidate = value.strip().lower()"` | — |
| [SRC-EEF2E6447C-L000230](../../api/omarai.py#L230) | 230 | `"    return len(candidate) == 40 and all(char in \"0123456789abcdef\" for char in candidate)"` | — |
| [SRC-EEF2E6447C-L000231](../../api/omarai.py#L231) | 231 | `""` | — |
| [SRC-EEF2E6447C-L000232](../../api/omarai.py#L232) | 232 | `""` | — |
| [SRC-EEF2E6447C-L000233](../../api/omarai.py#L233) | 233 | `"def _build_identity() -> tuple[str, str]:"` | — |
| [SRC-EEF2E6447C-L000234](../../api/omarai.py#L234) | 234 | `"    \"\"\"Prefer immutable image metadata, then documented hosting-provided Git SHAs.\"\"\""` | — |
| [SRC-EEF2E6447C-L000235](../../api/omarai.py#L235) | 235 | `"    try:"` | — |
| [SRC-EEF2E6447C-L000236](../../api/omarai.py#L236) | 236 | `"        baked = BUILD_SHA_FILE.read_text(encoding=\"ascii\").strip().lower()"` | — |
| [SRC-EEF2E6447C-L000237](../../api/omarai.py#L237) | 237 | `"    except (OSError, UnicodeError):"` | — |
| [SRC-EEF2E6447C-L000238](../../api/omarai.py#L238) | 238 | `"        baked = \"\""` | — |
| [SRC-EEF2E6447C-L000239](../../api/omarai.py#L239) | 239 | `"    if _valid_build_sha(baked):"` | — |
| [SRC-EEF2E6447C-L000240](../../api/omarai.py#L240) | 240 | `"        return baked, \"image_baked\""` | — |
| [SRC-EEF2E6447C-L000241](../../api/omarai.py#L241) | 241 | `""` | — |
| [SRC-EEF2E6447C-L000242](../../api/omarai.py#L242) | 242 | `"    for environment_name, source in _PLATFORM_BUILD_SHA_ENVIRONMENTS:"` | — |
| [SRC-EEF2E6447C-L000243](../../api/omarai.py#L243) | 243 | `"        candidate = os.getenv(environment_name, \"\").strip().lower()"` | — |
| [SRC-EEF2E6447C-L000244](../../api/omarai.py#L244) | 244 | `"        if _valid_build_sha(candidate):"` | — |
| [SRC-EEF2E6447C-L000245](../../api/omarai.py#L245) | 245 | `"            return candidate, source"` | — |
| [SRC-EEF2E6447C-L000246](../../api/omarai.py#L246) | 246 | `"    return \"unknown\", \"unknown\""` | — |
| [SRC-EEF2E6447C-L000247](../../api/omarai.py#L247) | 247 | `""` | — |
| [SRC-EEF2E6447C-L000248](../../api/omarai.py#L248) | 248 | `""` | — |
| [SRC-EEF2E6447C-L000249](../../api/omarai.py#L249) | 249 | `"def _build_sha() -> str:"` | — |
| [SRC-EEF2E6447C-L000250](../../api/omarai.py#L250) | 250 | `"    \"\"\"Return a validated source SHA, or 'unknown' when no trusted build evidence exists.\"\"\""` | — |
| [SRC-EEF2E6447C-L000251](../../api/omarai.py#L251) | 251 | `"    return _build_identity()[0]"` | — |
| [SRC-EEF2E6447C-L000252](../../api/omarai.py#L252) | 252 | `""` | — |
| [SRC-EEF2E6447C-L000253](../../api/omarai.py#L253) | 253 | `""` | — |
| [SRC-EEF2E6447C-L000254](../../api/omarai.py#L254) | 254 | `"class Handler(BaseHTTPRequestHandler):"` | — |
| [SRC-EEF2E6447C-L000255](../../api/omarai.py#L255) | 255 | `"    def setup(self):"` | — |
| [SRC-EEF2E6447C-L000256](../../api/omarai.py#L256) | 256 | `"        \"\"\"Install a reader with a strict deadline for the request line and headers.\"\"\""` | — |
| [SRC-EEF2E6447C-L000257](../../api/omarai.py#L257) | 257 | `"        self.connection = self.request"` | — |
| [SRC-EEF2E6447C-L000258](../../api/omarai.py#L258) | 258 | `"        if self.timeout is not None:"` | — |
| [SRC-EEF2E6447C-L000259](../../api/omarai.py#L259) | 259 | `"            self.connection.settimeout(self.timeout)"` | — |
| [SRC-EEF2E6447C-L000260](../../api/omarai.py#L260) | 260 | `"        self._request_header_deadline = None"` | — |
| [SRC-EEF2E6447C-L000261](../../api/omarai.py#L261) | 261 | `"        self.rfile = _DeadlineRequestReader(self.connection, self)"` | — |
| [SRC-EEF2E6447C-L000262](../../api/omarai.py#L262) | 262 | `"        self.wfile = self.connection.makefile(\"wb\", self.wbufsize)"` | — |
| [SRC-EEF2E6447C-L000263](../../api/omarai.py#L263) | 263 | `""` | — |
| [SRC-EEF2E6447C-L000264](../../api/omarai.py#L264) | 264 | `"    def handle_one_request(self):"` | — |
| [SRC-EEF2E6447C-L000265](../../api/omarai.py#L265) | 265 | `"        timeout = max("` | — |
| [SRC-EEF2E6447C-L000266](../../api/omarai.py#L266) | 266 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000267](../../api/omarai.py#L267) | 267 | `"            min("` | — |
| [SRC-EEF2E6447C-L000268](../../api/omarai.py#L268) | 268 | `"                float(REQUEST_HEADER_READ_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000269](../../api/omarai.py#L269) | 269 | `"                MAX_REQUEST_HEADER_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000270](../../api/omarai.py#L270) | 270 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000271](../../api/omarai.py#L271) | 271 | `"        )"` | — |
| [SRC-EEF2E6447C-L000272](../../api/omarai.py#L272) | 272 | `"        self._request_header_deadline = time.monotonic() + timeout"` | — |
| [SRC-EEF2E6447C-L000273](../../api/omarai.py#L273) | 273 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000274](../../api/omarai.py#L274) | 274 | `"            super().handle_one_request()"` | — |
| [SRC-EEF2E6447C-L000275](../../api/omarai.py#L275) | 275 | `"        except TimeoutError:"` | — |
| [SRC-EEF2E6447C-L000276](../../api/omarai.py#L276) | 276 | `"            # Incomplete request line/headers are untrusted protocol input;"` | — |
| [SRC-EEF2E6447C-L000277](../../api/omarai.py#L277) | 277 | `"            # close the socket without trying to parse or answer a partial request."` | — |
| [SRC-EEF2E6447C-L000278](../../api/omarai.py#L278) | 278 | `"            self.close_connection = True"` | — |
| [SRC-EEF2E6447C-L000279](../../api/omarai.py#L279) | 279 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000280](../../api/omarai.py#L280) | 280 | `"            self._request_header_deadline = None"` | — |
| [SRC-EEF2E6447C-L000281](../../api/omarai.py#L281) | 281 | `""` | — |
| [SRC-EEF2E6447C-L000282](../../api/omarai.py#L282) | 282 | `"    store = _lead_store_from_environment()"` | — |
| [SRC-EEF2E6447C-L000283](../../api/omarai.py#L283) | 283 | `"    _rate_lock = threading.Lock()"` | — |
| [SRC-EEF2E6447C-L000284](../../api/omarai.py#L284) | 284 | `"    _request_times: ClassVar[dict[str, deque[float]]] = defaultdict(deque)"` | — |
| [SRC-EEF2E6447C-L000285](../../api/omarai.py#L285) | 285 | `"    _rate_last_cleanup: ClassVar[float] = 0.0"` | — |
| [SRC-EEF2E6447C-L000286](../../api/omarai.py#L286) | 286 | `"    RATE_LIMIT_REQUESTS = 20"` | — |
| [SRC-EEF2E6447C-L000287](../../api/omarai.py#L287) | 287 | `"    RATE_LIMIT_WINDOW_SECONDS = 60"` | — |
| [SRC-EEF2E6447C-L000288](../../api/omarai.py#L288) | 288 | `"    RATE_LIMIT_CLEANUP_INTERVAL_SECONDS = 60"` | — |
| [SRC-EEF2E6447C-L000289](../../api/omarai.py#L289) | 289 | `"    # Reserve the final bucket for clients beyond the per-process tracking ceiling."` | — |
| [SRC-EEF2E6447C-L000290](../../api/omarai.py#L290) | 290 | `"    MAX_RATE_LIMIT_CLIENT_BUCKETS = 4096"` | — |
| [SRC-EEF2E6447C-L000291](../../api/omarai.py#L291) | 291 | `"    RATE_LIMIT_OVERFLOW_KEY = \"__omarai_overflow__\""` | — |
| [SRC-EEF2E6447C-L000292](../../api/omarai.py#L292) | 292 | `"    AGENT_CONCURRENCY_LIMIT = _configured_agent_concurrency_limit()"` | — |
| [SRC-EEF2E6447C-L000293](../../api/omarai.py#L293) | 293 | `"    _agent_semaphore = threading.BoundedSemaphore(AGENT_CONCURRENCY_LIMIT)"` | — |
| [SRC-EEF2E6447C-L000294](../../api/omarai.py#L294) | 294 | `""` | — |
| [SRC-EEF2E6447C-L000295](../../api/omarai.py#L295) | 295 | `"    def _run_bounded_agent_operation(self, operation):"` | — |
| [SRC-EEF2E6447C-L000296](../../api/omarai.py#L296) | 296 | `"        \"\"\"Run an expensive operation only when a process-local slot is available.\"\"\""` | — |
| [SRC-EEF2E6447C-L000297](../../api/omarai.py#L297) | 297 | `"        cls = type(self)"` | — |
| [SRC-EEF2E6447C-L000298](../../api/omarai.py#L298) | 298 | `"        if not cls._agent_semaphore.acquire(blocking=False):"` | — |
| [SRC-EEF2E6447C-L000299](../../api/omarai.py#L299) | 299 | `"            return self.respond("` | — |
| [SRC-EEF2E6447C-L000300](../../api/omarai.py#L300) | 300 | `"                503,"` | — |
| [SRC-EEF2E6447C-L000301](../../api/omarai.py#L301) | 301 | `"                {"` | — |
| [SRC-EEF2E6447C-L000302](../../api/omarai.py#L302) | 302 | `"                    \"error\": \"خدمة البحث مشغولة حاليًا؛ أعد المحاولة بعد قليل.\","` | — |
| [SRC-EEF2E6447C-L000303](../../api/omarai.py#L303) | 303 | `"                    \"retry_after_seconds\": 5,"` | — |
| [SRC-EEF2E6447C-L000304](../../api/omarai.py#L304) | 304 | `"                    \"process_concurrency_limit\": cls.AGENT_CONCURRENCY_LIMIT,"` | — |
| [SRC-EEF2E6447C-L000305](../../api/omarai.py#L305) | 305 | `"                },"` | — |
| [SRC-EEF2E6447C-L000306](../../api/omarai.py#L306) | 306 | `"            )"` | — |
| [SRC-EEF2E6447C-L000307](../../api/omarai.py#L307) | 307 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000308](../../api/omarai.py#L308) | 308 | `"            return self.respond(200, operation())"` | — |
| [SRC-EEF2E6447C-L000309](../../api/omarai.py#L309) | 309 | `"        finally:"` | — |
| [SRC-EEF2E6447C-L000310](../../api/omarai.py#L310) | 310 | `"            cls._agent_semaphore.release()"` | — |
| [SRC-EEF2E6447C-L000311](../../api/omarai.py#L311) | 311 | `""` | — |
| [SRC-EEF2E6447C-L000312](../../api/omarai.py#L312) | 312 | `"    def _authorized(self):"` | — |
| [SRC-EEF2E6447C-L000313](../../api/omarai.py#L313) | 313 | `"        expected = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000314](../../api/omarai.py#L314) | 314 | `"        if not expected:"` | — |
| [SRC-EEF2E6447C-L000315](../../api/omarai.py#L315) | 315 | `"            return os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() != \"1\""` | — |
| [SRC-EEF2E6447C-L000316](../../api/omarai.py#L316) | 316 | `"        supplied = self.headers.get(\"Authorization\", \"\")"` | — |
| [SRC-EEF2E6447C-L000317](../../api/omarai.py#L317) | 317 | `"        if not supplied.startswith(\"Bearer \"):"` | — |
| [SRC-EEF2E6447C-L000318](../../api/omarai.py#L318) | 318 | `"            return False"` | — |
| [SRC-EEF2E6447C-L000319](../../api/omarai.py#L319) | 319 | `"        return hmac.compare_digest(supplied[7:].strip(), expected)"` | — |
| [SRC-EEF2E6447C-L000320](../../api/omarai.py#L320) | 320 | `""` | — |
| [SRC-EEF2E6447C-L000321](../../api/omarai.py#L321) | 321 | `"    def _allowed_origins(self):"` | — |
| [SRC-EEF2E6447C-L000322](../../api/omarai.py#L322) | 322 | `"        \"\"\"Return configured browser origins plus this service’s own origin."` | — |
| [SRC-EEF2E6447C-L000323](../../api/omarai.py#L323) | 323 | `""` | — |
| [SRC-EEF2E6447C-L000324](../../api/omarai.py#L324) | 324 | `"        OMARAI_ALLOWED_ORIGINS is a comma-separated list of trusted origins"` | — |
| [SRC-EEF2E6447C-L000325](../../api/omarai.py#L325) | 325 | `"        (scheme + host + optional port; no path and no wildcard)."` | — |
| [SRC-EEF2E6447C-L000326](../../api/omarai.py#L326) | 326 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000327](../../api/omarai.py#L327) | 327 | `"        configured = os.getenv(\"OMARAI_ALLOWED_ORIGINS\", \"\")"` | — |
| [SRC-EEF2E6447C-L000328](../../api/omarai.py#L328) | 328 | `"        origins = {"` | — |
| [SRC-EEF2E6447C-L000329](../../api/omarai.py#L329) | 329 | `"            item.strip().rstrip(\"/\")"` | — |
| [SRC-EEF2E6447C-L000330](../../api/omarai.py#L330) | 330 | `"            for item in configured.split(\",\")"` | — |
| [SRC-EEF2E6447C-L000331](../../api/omarai.py#L331) | 331 | `"            if item.strip()"` | — |
| [SRC-EEF2E6447C-L000332](../../api/omarai.py#L332) | 332 | `"        }"` | — |
| [SRC-EEF2E6447C-L000333](../../api/omarai.py#L333) | 333 | `"        if os.getenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"\").strip() == \"1\":"` | — |
| [SRC-EEF2E6447C-L000334](../../api/omarai.py#L334) | 334 | `"            # Host identifies the requested service origin. Do not derive allowed"` | — |
| [SRC-EEF2E6447C-L000335](../../api/omarai.py#L335) | 335 | `"            # origins from X-Forwarded-Host: direct clients can spoof that header"` | — |
| [SRC-EEF2E6447C-L000336](../../api/omarai.py#L336) | 336 | `"            # unless the reverse proxy is separately configured to overwrite it."` | — |
| [SRC-EEF2E6447C-L000337](../../api/omarai.py#L337) | 337 | `"            scheme = self.headers.get(\"X-Forwarded-Proto\", \"https\").split(\",\", 1)[0].strip().lower()"` | — |
| [SRC-EEF2E6447C-L000338](../../api/omarai.py#L338) | 338 | `"            host = self.headers.get(\"Host\", \"\").split(\",\", 1)[0].strip()"` | — |
| [SRC-EEF2E6447C-L000339](../../api/omarai.py#L339) | 339 | `"            if host:"` | — |
| [SRC-EEF2E6447C-L000340](../../api/omarai.py#L340) | 340 | `"                origins.add(f\"https://{host}\".rstrip(\"/\"))"` | — |
| [SRC-EEF2E6447C-L000341](../../api/omarai.py#L341) | 341 | `"                origins.add(f\"{scheme}://{host}\".rstrip(\"/\"))"` | — |
| [SRC-EEF2E6447C-L000342](../../api/omarai.py#L342) | 342 | `"        else:"` | — |
| [SRC-EEF2E6447C-L000343](../../api/omarai.py#L343) | 343 | `"            port = self.server.server_port"` | — |
| [SRC-EEF2E6447C-L000344](../../api/omarai.py#L344) | 344 | `"            origins.update("` | — |
| [SRC-EEF2E6447C-L000345](../../api/omarai.py#L345) | 345 | `"                {"` | — |
| [SRC-EEF2E6447C-L000346](../../api/omarai.py#L346) | 346 | `"                    f\"http://127.0.0.1:{port}\","` | — |
| [SRC-EEF2E6447C-L000347](../../api/omarai.py#L347) | 347 | `"                    f\"http://localhost:{port}\","` | — |
| [SRC-EEF2E6447C-L000348](../../api/omarai.py#L348) | 348 | `"                    f\"http://[::1]:{port}\","` | — |
| [SRC-EEF2E6447C-L000349](../../api/omarai.py#L349) | 349 | `"                }"` | — |
| [SRC-EEF2E6447C-L000350](../../api/omarai.py#L350) | 350 | `"            )"` | — |
| [SRC-EEF2E6447C-L000351](../../api/omarai.py#L351) | 351 | `"        return origins"` | — |
| [SRC-EEF2E6447C-L000352](../../api/omarai.py#L352) | 352 | `""` | — |
| [SRC-EEF2E6447C-L000353](../../api/omarai.py#L353) | 353 | `"    def _origin_allowed(self, origin):"` | — |
| [SRC-EEF2E6447C-L000354](../../api/omarai.py#L354) | 354 | `"        return bool(origin) and origin.rstrip(\"/\") in self._allowed_origins()"` | — |
| [SRC-EEF2E6447C-L000355](../../api/omarai.py#L355) | 355 | `""` | — |
| [SRC-EEF2E6447C-L000356](../../api/omarai.py#L356) | 356 | `"    def _rate_limit_client_key(self):"` | — |
| [SRC-EEF2E6447C-L000357](../../api/omarai.py#L357) | 357 | `"        \"\"\"Choose a rate-limit identity without trusting spoofable proxy headers by default."` | — |
| [SRC-EEF2E6447C-L000358](../../api/omarai.py#L358) | 358 | `""` | — |
| [SRC-EEF2E6447C-L000359](../../api/omarai.py#L359) | 359 | `"        Set OMARAI_TRUST_PROXY_HEADERS=1 only when the deployment's trusted reverse"` | — |
| [SRC-EEF2E6447C-L000360](../../api/omarai.py#L360) | 360 | `"        proxy appends the actual client IP as the rightmost X-Forwarded-For value."` | — |
| [SRC-EEF2E6447C-L000361](../../api/omarai.py#L361) | 361 | `"        \"\"\""` | — |
| [SRC-EEF2E6447C-L000362](../../api/omarai.py#L362) | 362 | `"        direct_ip = self.client_address[0]"` | — |
| [SRC-EEF2E6447C-L000363](../../api/omarai.py#L363) | 363 | `"        if os.getenv(\"OMARAI_TRUST_PROXY_HEADERS\", \"\").strip() != \"1\":"` | — |
| [SRC-EEF2E6447C-L000364](../../api/omarai.py#L364) | 364 | `"            return direct_ip"` | — |
| [SRC-EEF2E6447C-L000365](../../api/omarai.py#L365) | 365 | `"        forwarded = self.headers.get(\"X-Forwarded-For\", \"\")"` | — |
| [SRC-EEF2E6447C-L000366](../../api/omarai.py#L366) | 366 | `"        candidate = forwarded.rsplit(\",\", 1)[-1].strip() if forwarded else \"\""` | — |
| [SRC-EEF2E6447C-L000367](../../api/omarai.py#L367) | 367 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000368](../../api/omarai.py#L368) | 368 | `"            return str(ipaddress.ip_address(candidate))"` | — |
| [SRC-EEF2E6447C-L000369](../../api/omarai.py#L369) | 369 | `"        except ValueError:"` | — |
| [SRC-EEF2E6447C-L000370](../../api/omarai.py#L370) | 370 | `"            return direct_ip"` | — |
| [SRC-EEF2E6447C-L000371](../../api/omarai.py#L371) | 371 | `""` | — |
| [SRC-EEF2E6447C-L000372](../../api/omarai.py#L372) | 372 | `"    def _rate_limit_ok(self):"` | — |
| [SRC-EEF2E6447C-L000373](../../api/omarai.py#L373) | 373 | `"        client_ip = self._rate_limit_client_key()"` | — |
| [SRC-EEF2E6447C-L000374](../../api/omarai.py#L374) | 374 | `"        now = time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000375](../../api/omarai.py#L375) | 375 | `"        cls = type(self)"` | — |
| [SRC-EEF2E6447C-L000376](../../api/omarai.py#L376) | 376 | `"        with self._rate_lock:"` | — |
| [SRC-EEF2E6447C-L000377](../../api/omarai.py#L377) | 377 | `"            # Periodically remove IP buckets whose entire sliding window has expired."` | — |
| [SRC-EEF2E6447C-L000378](../../api/omarai.py#L378) | 378 | `"            # Without this sweep, a public endpoint could retain one empty deque per"` | — |
| [SRC-EEF2E6447C-L000379](../../api/omarai.py#L379) | 379 | `"            # distinct client IP forever, even though the rate-limit window is 60 sec."` | — |
| [SRC-EEF2E6447C-L000380](../../api/omarai.py#L380) | 380 | `"            if now - cls._rate_last_cleanup >= cls.RATE_LIMIT_CLEANUP_INTERVAL_SECONDS:"` | — |
| [SRC-EEF2E6447C-L000381](../../api/omarai.py#L381) | 381 | `"                cutoff = now - cls.RATE_LIMIT_WINDOW_SECONDS"` | — |
| [SRC-EEF2E6447C-L000382](../../api/omarai.py#L382) | 382 | `"                for key, timestamps in list(cls._request_times.items()):"` | — |
| [SRC-EEF2E6447C-L000383](../../api/omarai.py#L383) | 383 | `"                    while timestamps and timestamps[0] <= cutoff:"` | — |
| [SRC-EEF2E6447C-L000384](../../api/omarai.py#L384) | 384 | `"                        timestamps.popleft()"` | — |
| [SRC-EEF2E6447C-L000385](../../api/omarai.py#L385) | 385 | `"                    if not timestamps:"` | — |
| [SRC-EEF2E6447C-L000386](../../api/omarai.py#L386) | 386 | `"                        cls._request_times.pop(key, None)"` | — |
| [SRC-EEF2E6447C-L000387](../../api/omarai.py#L387) | 387 | `"                cls._rate_last_cleanup = now"` | — |
| [SRC-EEF2E6447C-L000388](../../api/omarai.py#L388) | 388 | `""` | — |
| [SRC-EEF2E6447C-L000389](../../api/omarai.py#L389) | 389 | `"            if ("` | — |
| [SRC-EEF2E6447C-L000390](../../api/omarai.py#L390) | 390 | `"                client_ip not in cls._request_times"` | — |
| [SRC-EEF2E6447C-L000391](../../api/omarai.py#L391) | 391 | `"                and len(cls._request_times) >= max(1, cls.MAX_RATE_LIMIT_CLIENT_BUCKETS) - 1"` | — |
| [SRC-EEF2E6447C-L000392](../../api/omarai.py#L392) | 392 | `"            ):"` | — |
| [SRC-EEF2E6447C-L000393](../../api/omarai.py#L393) | 393 | `"                # Bound attacker-controlled cardinality. Excess identities share a"` | — |
| [SRC-EEF2E6447C-L000394](../../api/omarai.py#L394) | 394 | `"                # conservative overflow bucket instead of allocating one deque per IP."` | — |
| [SRC-EEF2E6447C-L000395](../../api/omarai.py#L395) | 395 | `"                client_ip = cls.RATE_LIMIT_OVERFLOW_KEY"` | — |
| [SRC-EEF2E6447C-L000396](../../api/omarai.py#L396) | 396 | `"            events = cls._request_times[client_ip]"` | — |
| [SRC-EEF2E6447C-L000397](../../api/omarai.py#L397) | 397 | `"            while events and now - events[0] >= cls.RATE_LIMIT_WINDOW_SECONDS:"` | — |
| [SRC-EEF2E6447C-L000398](../../api/omarai.py#L398) | 398 | `"                events.popleft()"` | — |
| [SRC-EEF2E6447C-L000399](../../api/omarai.py#L399) | 399 | `"            if len(events) >= cls.RATE_LIMIT_REQUESTS:"` | — |
| [SRC-EEF2E6447C-L000400](../../api/omarai.py#L400) | 400 | `"                return False"` | — |
| [SRC-EEF2E6447C-L000401](../../api/omarai.py#L401) | 401 | `"            events.append(now)"` | — |
| [SRC-EEF2E6447C-L000402](../../api/omarai.py#L402) | 402 | `"            return True"` | — |
| [SRC-EEF2E6447C-L000403](../../api/omarai.py#L403) | 403 | `""` | — |
| [SRC-EEF2E6447C-L000404](../../api/omarai.py#L404) | 404 | `"    def _read_request_body(self) -> bytes \| None:"` | — |
| [SRC-EEF2E6447C-L000405](../../api/omarai.py#L405) | 405 | `"        \"\"\"Read a bounded body with both idle and absolute wall-clock deadlines.\"\"\""` | — |
| [SRC-EEF2E6447C-L000406](../../api/omarai.py#L406) | 406 | `"        raw_size = self.headers.get(\"Content-Length\", \"\").strip()"` | — |
| [SRC-EEF2E6447C-L000407](../../api/omarai.py#L407) | 407 | `"        if not raw_size or not raw_size.isascii() or not raw_size.isdecimal():"` | — |
| [SRC-EEF2E6447C-L000408](../../api/omarai.py#L408) | 408 | `"            self.respond(400, {\"error\": \"valid Content-Length is required\"})"` | — |
| [SRC-EEF2E6447C-L000409](../../api/omarai.py#L409) | 409 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000410](../../api/omarai.py#L410) | 410 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000411](../../api/omarai.py#L411) | 411 | `"            size = int(raw_size)"` | — |
| [SRC-EEF2E6447C-L000412](../../api/omarai.py#L412) | 412 | `"        except ValueError:"` | — |
| [SRC-EEF2E6447C-L000413](../../api/omarai.py#L413) | 413 | `"            self.respond(400, {\"error\": \"valid Content-Length is required\"})"` | — |
| [SRC-EEF2E6447C-L000414](../../api/omarai.py#L414) | 414 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000415](../../api/omarai.py#L415) | 415 | `"        if size <= 0:"` | — |
| [SRC-EEF2E6447C-L000416](../../api/omarai.py#L416) | 416 | `"            self.respond(400, {\"error\": \"request body is required\"})"` | — |
| [SRC-EEF2E6447C-L000417](../../api/omarai.py#L417) | 417 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000418](../../api/omarai.py#L418) | 418 | `"        if size > MAX_REQUEST_BODY_BYTES:"` | — |
| [SRC-EEF2E6447C-L000419](../../api/omarai.py#L419) | 419 | `"            self.respond(413, {\"error\": \"request too large\"})"` | — |
| [SRC-EEF2E6447C-L000420](../../api/omarai.py#L420) | 420 | `"            return None"` | — |
| [SRC-EEF2E6447C-L000421](../../api/omarai.py#L421) | 421 | `""` | — |
| [SRC-EEF2E6447C-L000422](../../api/omarai.py#L422) | 422 | `"        total_timeout = max("` | — |
| [SRC-EEF2E6447C-L000423](../../api/omarai.py#L423) | 423 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000424](../../api/omarai.py#L424) | 424 | `"            min("` | — |
| [SRC-EEF2E6447C-L000425](../../api/omarai.py#L425) | 425 | `"                float(REQUEST_BODY_READ_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000426](../../api/omarai.py#L426) | 426 | `"                MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000427](../../api/omarai.py#L427) | 427 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000428](../../api/omarai.py#L428) | 428 | `"        )"` | — |
| [SRC-EEF2E6447C-L000429](../../api/omarai.py#L429) | 429 | `"        idle_timeout = max("` | — |
| [SRC-EEF2E6447C-L000430](../../api/omarai.py#L430) | 430 | `"            0.1,"` | — |
| [SRC-EEF2E6447C-L000431](../../api/omarai.py#L431) | 431 | `"            min("` | — |
| [SRC-EEF2E6447C-L000432](../../api/omarai.py#L432) | 432 | `"                float(REQUEST_BODY_IDLE_TIMEOUT_SECONDS),"` | — |
| [SRC-EEF2E6447C-L000433](../../api/omarai.py#L433) | 433 | `"                MAX_REQUEST_BODY_READ_TIMEOUT_SECONDS,"` | — |
| [SRC-EEF2E6447C-L000434](../../api/omarai.py#L434) | 434 | `"            ),"` | — |
| [SRC-EEF2E6447C-L000435](../../api/omarai.py#L435) | 435 | `"        )"` | — |
| [SRC-EEF2E6447C-L000436](../../api/omarai.py#L436) | 436 | `"        deadline = time.monotonic() + total_timeout"` | — |
| [SRC-EEF2E6447C-L000437](../../api/omarai.py#L437) | 437 | `"        previous_timeout = self.connection.gettimeout()"` | — |
| [SRC-EEF2E6447C-L000438](../../api/omarai.py#L438) | 438 | `"        body = bytearray()"` | — |
| [SRC-EEF2E6447C-L000439](../../api/omarai.py#L439) | 439 | `"        timed_out = False"` | — |
| [SRC-EEF2E6447C-L000440](../../api/omarai.py#L440) | 440 | `"        try:"` | — |
| [SRC-EEF2E6447C-L000441](../../api/omarai.py#L441) | 441 | `"            while len(body) < size:"` | — |
| [SRC-EEF2E6447C-L000442](../../api/omarai.py#L442) | 442 | `"                remaining = deadline - time.monotonic()"` | — |
| [SRC-EEF2E6447C-L000443](../../api/omarai.py#L443) | 443 | `"                if remaining <= 0:"` | — |
| [SRC-EEF2E6447C-L000444](../../api/omarai.py#L444) | 444 | `"                    timed_out = True"` | — |
| [SRC-EEF2E6447C-L000445](../../api/omarai.py#L445) | 445 | `"                    break"` | — |
| [SRC-EEF2E6447C-L000446](../../api/omarai.py#L446) | 446 | `"                self.connection.settimeout(min(idle_timeout, remaining))"` | — |
| [SRC-EEF2E6447C-L000447](../../api/omarai.py#L447) | 447 | `"                try:"` | — |
| [SRC-EEF2E6447C-L000448](../../api/omarai.py#L448) | 448 | `"                    # read1 performs at most one underlying read, letting us re-check"` | — |
| [SRC-EEF2E6447C-L000449](../../api/omarai.py#L449) | 449 | `"                    # the absolute deadline between body fragments."` | — |
| [SRC-EEF2E6447C-L000450](../../api/omarai.py#L450) | 450 | `"                    chunk = self.rfile.read1("` | — |
| [SRC-EEF2E6447C-L000451](../../api/omarai.py#L451) | 451 | `"                        min(size - len(body), REQUEST_BODY_READ_CHUNK_BYTES)"` | — |
| [SRC-EEF2E6447C-L000452](../../api/omarai.py#L452) | 452 | `"                    )"` | — |
