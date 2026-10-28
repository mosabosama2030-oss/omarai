# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **010**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L004415 إلى SRC-1AE03B9EC3-L005214
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L004415](../../agents/web_agent.py#L4415) | 4415 | `"        plan[\"queries\"] = list(dict.fromkeys(final_topic_queries))[:query_limit]"` | — |
| [SRC-1AE03B9EC3-L004416](../../agents/web_agent.py#L4416) | 4416 | `""` | — |
| [SRC-1AE03B9EC3-L004417](../../agents/web_agent.py#L4417) | 4417 | `"        sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L004418](../../agents/web_agent.py#L4418) | 4418 | `"        search_warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L004419](../../agents/web_agent.py#L4419) | 4419 | `"        report: dict[str, Any] = {}"` | — |
| [SRC-1AE03B9EC3-L004420](../../agents/web_agent.py#L4420) | 4420 | `"        # Scope diagnostic evidence to this research attempt; a reused WebAgent must not"` | — |
| [SRC-1AE03B9EC3-L004421](../../agents/web_agent.py#L4421) | 4421 | `"        # accidentally inherit provider attempts from an earlier question."` | — |
| [SRC-1AE03B9EC3-L004422](../../agents/web_agent.py#L4422) | 4422 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L004423](../../agents/web_agent.py#L4423) | 4423 | `"            research_diagnostic_baseline = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L004424](../../agents/web_agent.py#L4424) | 4424 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L004425](../../agents/web_agent.py#L4425) | 4425 | `"            sources, search_warnings, report = self._collect_research(plan)"` | — |
| [SRC-1AE03B9EC3-L004426](../../agents/web_agent.py#L4426) | 4426 | `"        except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L004427](../../agents/web_agent.py#L4427) | 4427 | `"            search_warnings.append(str(exc))"` | — |
| [SRC-1AE03B9EC3-L004428](../../agents/web_agent.py#L4428) | 4428 | `"            baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L004429](../../agents/web_agent.py#L4429) | 4429 | `"            with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L004430](../../agents/web_agent.py#L4430) | 4430 | `"                failure_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L004431](../../agents/web_agent.py#L4431) | 4431 | `"                    item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004432](../../agents/web_agent.py#L4432) | 4432 | `"                    if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L004433](../../agents/web_agent.py#L4433) | 4433 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004434](../../agents/web_agent.py#L4434) | 4434 | `"            provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L004435](../../agents/web_agent.py#L4435) | 4435 | `"                item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L004436](../../agents/web_agent.py#L4436) | 4436 | `"                for item in failure_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004437](../../agents/web_agent.py#L4437) | 4437 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004438](../../agents/web_agent.py#L4438) | 4438 | `"            report = {"` | — |
| [SRC-1AE03B9EC3-L004439](../../agents/web_agent.py#L4439) | 4439 | `"                \"queries_planned\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-1AE03B9EC3-L004440](../../agents/web_agent.py#L4440) | 4440 | `"                # The exact query count is unknowable when the pipeline fails before it"` | — |
| [SRC-1AE03B9EC3-L004441](../../agents/web_agent.py#L4441) | 4441 | `"                # returns its report. A provider diagnostic may still prove an attempt."` | — |
| [SRC-1AE03B9EC3-L004442](../../agents/web_agent.py#L4442) | 4442 | `"                \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L004443](../../agents/web_agent.py#L4443) | 4443 | `"                \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L004444](../../agents/web_agent.py#L4444) | 4444 | `"                \"search_attempted\": True if provider_attempt_observed else None,"` | — |
| [SRC-1AE03B9EC3-L004445](../../agents/web_agent.py#L4445) | 4445 | `"                \"search_outcome\": ("` | — |
| [SRC-1AE03B9EC3-L004446](../../agents/web_agent.py#L4446) | 4446 | `"                    \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L004447](../../agents/web_agent.py#L4447) | 4447 | `"                    if provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L004448](../../agents/web_agent.py#L4448) | 4448 | `"                    else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L004449](../../agents/web_agent.py#L4449) | 4449 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004450](../../agents/web_agent.py#L4450) | 4450 | `"                \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L004451](../../agents/web_agent.py#L4451) | 4451 | `"                \"unique_sources\": None,"` | — |
| [SRC-1AE03B9EC3-L004452](../../agents/web_agent.py#L4452) | 4452 | `"                \"pages_fetched\": None,"` | — |
| [SRC-1AE03B9EC3-L004453](../../agents/web_agent.py#L4453) | 4453 | `"                \"providers_used\": [],"` | — |
| [SRC-1AE03B9EC3-L004454](../../agents/web_agent.py#L4454) | 4454 | `"                \"provider_counts\": None,"` | — |
| [SRC-1AE03B9EC3-L004455](../../agents/web_agent.py#L4455) | 4455 | `"                \"platform_counts\": {},"` | — |
| [SRC-1AE03B9EC3-L004456](../../agents/web_agent.py#L4456) | 4456 | `"                \"social_direct_results\": None,"` | — |
| [SRC-1AE03B9EC3-L004457](../../agents/web_agent.py#L4457) | 4457 | `"                \"provider_diagnostics\": failure_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L004458](../../agents/web_agent.py#L4458) | 4458 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L004459](../../agents/web_agent.py#L4459) | 4459 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L004460](../../agents/web_agent.py#L4460) | 4460 | `"                \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L004461](../../agents/web_agent.py#L4461) | 4461 | `"                \"evidence_signals\": evidence_signal_report([], plan.get(\"freshness\", \"any\")),"` | — |
| [SRC-1AE03B9EC3-L004462](../../agents/web_agent.py#L4462) | 4462 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004463](../../agents/web_agent.py#L4463) | 4463 | `"        if isinstance(report, dict):"` | — |
| [SRC-1AE03B9EC3-L004464](../../agents/web_agent.py#L4464) | 4464 | `"            report[\"dialogue_context\"] = plan.get(\"dialogue_context\", {})"` | — |
| [SRC-1AE03B9EC3-L004465](../../agents/web_agent.py#L4465) | 4465 | `"        # Final relevance check is intentionally repeated after fusion, before any answer LLM call."` | — |
| [SRC-1AE03B9EC3-L004466](../../agents/web_agent.py#L4466) | 4466 | `"        filtered_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L004467](../../agents/web_agent.py#L4467) | 4467 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L004468](../../agents/web_agent.py#L4468) | 4468 | `"            if \"user_supplied_url\" in source.get(\"providers\", []):"` | — |
| [SRC-1AE03B9EC3-L004469](../../agents/web_agent.py#L4469) | 4469 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004470](../../agents/web_agent.py#L4470) | 4470 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L004471](../../agents/web_agent.py#L4471) | 4471 | `"            candidate_queries = ("` | — |
| [SRC-1AE03B9EC3-L004472](../../agents/web_agent.py#L4472) | 4472 | `"                source.get(\"queries\")"` | — |
| [SRC-1AE03B9EC3-L004473](../../agents/web_agent.py#L4473) | 4473 | `"                or plan.get(\"queries\")"` | — |
| [SRC-1AE03B9EC3-L004474](../../agents/web_agent.py#L4474) | 4474 | `"                or [compact_search_query(working_question)]"` | — |
| [SRC-1AE03B9EC3-L004475](../../agents/web_agent.py#L4475) | 4475 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004476](../../agents/web_agent.py#L4476) | 4476 | `"            if any(self._source_matches_query(str(q), source) for q in candidate_queries):"` | — |
| [SRC-1AE03B9EC3-L004477](../../agents/web_agent.py#L4477) | 4477 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004478](../../agents/web_agent.py#L4478) | 4478 | `"        sources = filtered_sources"` | — |
| [SRC-1AE03B9EC3-L004479](../../agents/web_agent.py#L4479) | 4479 | `"        search_warning = \"؛ \".join(search_warnings) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L004480](../../agents/web_agent.py#L4480) | 4480 | `"        independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L004481](../../agents/web_agent.py#L4481) | 4481 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L004482](../../agents/web_agent.py#L4482) | 4482 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L004483](../../agents/web_agent.py#L4483) | 4483 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L004484](../../agents/web_agent.py#L4484) | 4484 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L004485](../../agents/web_agent.py#L4485) | 4485 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004486](../../agents/web_agent.py#L4486) | 4486 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L004487](../../agents/web_agent.py#L4487) | 4487 | `"        }"` | — |
| [SRC-1AE03B9EC3-L004488](../../agents/web_agent.py#L4488) | 4488 | `"        independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L004489](../../agents/web_agent.py#L4489) | 4489 | `"        # A user-requested page summary is a different task from open-ended research:"` | — |
| [SRC-1AE03B9EC3-L004490](../../agents/web_agent.py#L4490) | 4490 | `"        # one successfully extracted, explicitly supplied page can support a summary,"` | — |
| [SRC-1AE03B9EC3-L004491](../../agents/web_agent.py#L4491) | 4491 | `"        # but must never be presented as independently corroborated research."` | — |
| [SRC-1AE03B9EC3-L004492](../../agents/web_agent.py#L4492) | 4492 | `"        has_read_user_supplied_page = any("` | — |
| [SRC-1AE03B9EC3-L004493](../../agents/web_agent.py#L4493) | 4493 | `"            \"user_supplied_url\" in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L004494](../../agents/web_agent.py#L4494) | 4494 | `"            and bool(source.get(\"page_fetched\"))"` | — |
| [SRC-1AE03B9EC3-L004495](../../agents/web_agent.py#L4495) | 4495 | `"            and bool(str(source.get(\"page_text\") or \"\").strip())"` | — |
| [SRC-1AE03B9EC3-L004496](../../agents/web_agent.py#L4496) | 4496 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L004497](../../agents/web_agent.py#L4497) | 4497 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004498](../../agents/web_agent.py#L4498) | 4498 | `"        single_source_page_summary = ("` | — |
| [SRC-1AE03B9EC3-L004499](../../agents/web_agent.py#L4499) | 4499 | `"            has_read_user_supplied_page"` | — |
| [SRC-1AE03B9EC3-L004500](../../agents/web_agent.py#L4500) | 4500 | `"            and len(sources) == 1"` | — |
| [SRC-1AE03B9EC3-L004501](../../agents/web_agent.py#L4501) | 4501 | `"            and len(independent_domains) == 1"` | — |
| [SRC-1AE03B9EC3-L004502](../../agents/web_agent.py#L4502) | 4502 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004503](../../agents/web_agent.py#L4503) | 4503 | `"        if single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L004504](../../agents/web_agent.py#L4504) | 4504 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004505](../../agents/web_agent.py#L4505) | 4505 | `"                \"هذا ملخص للرابط الذي قدمته فقط؛ لم يتم تأكيد محتواه من مصدر مستقل آخر.\""` | — |
| [SRC-1AE03B9EC3-L004506](../../agents/web_agent.py#L4506) | 4506 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004507](../../agents/web_agent.py#L4507) | 4507 | `"            search_warning = \"؛ \".join(search_warnings)"` | — |
| [SRC-1AE03B9EC3-L004508](../../agents/web_agent.py#L4508) | 4508 | `"        # Link-finding and lead-discovery are actionable discovery tasks, not broad"` | — |
| [SRC-1AE03B9EC3-L004509](../../agents/web_agent.py#L4509) | 4509 | `"        # fact-checking. Keep useful candidates visible while explicitly labelling them"` | — |
| [SRC-1AE03B9EC3-L004510](../../agents/web_agent.py#L4510) | 4510 | `"        # as uncorroborated instead of refusing a lone result as if it were no result."` | — |
| [SRC-1AE03B9EC3-L004511](../../agents/web_agent.py#L4511) | 4511 | `"        navigation_request = self._is_navigation_request(working_question)"` | — |
| [SRC-1AE03B9EC3-L004512](../../agents/web_agent.py#L4512) | 4512 | `"        lead_request = intent_route == \"LEAD_GENERATION\" or self._is_lead_search(working_question)"` | — |
| [SRC-1AE03B9EC3-L004513](../../agents/web_agent.py#L4513) | 4513 | `"        listing_request = self._is_listing_discovery(working_question)"` | — |
| [SRC-1AE03B9EC3-L004514](../../agents/web_agent.py#L4514) | 4514 | `"        lead_evidence_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L004515](../../agents/web_agent.py#L4515) | 4515 | `"        related_lead_results_count = 0"` | — |
| [SRC-1AE03B9EC3-L004516](../../agents/web_agent.py#L4516) | 4516 | `"        if lead_request:"` | — |
| [SRC-1AE03B9EC3-L004517](../../agents/web_agent.py#L4517) | 4517 | `"            related_lead_results_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004518](../../agents/web_agent.py#L4518) | 4518 | `"            for source in sources:"` | — |
| [SRC-1AE03B9EC3-L004519](../../agents/web_agent.py#L4519) | 4519 | `"                signal = self._lead_intent_evidence(source)"` | — |
| [SRC-1AE03B9EC3-L004520](../../agents/web_agent.py#L4520) | 4520 | `"                if signal:"` | — |
| [SRC-1AE03B9EC3-L004521](../../agents/web_agent.py#L4521) | 4521 | `"                    source[\"lead_qualification\"] = \"public_buyer_intent_signal\""` | — |
| [SRC-1AE03B9EC3-L004522](../../agents/web_agent.py#L4522) | 4522 | `"                    source[\"lead_intent_evidence\"] = signal"` | — |
| [SRC-1AE03B9EC3-L004523](../../agents/web_agent.py#L4523) | 4523 | `"                    lead_evidence_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004524](../../agents/web_agent.py#L4524) | 4524 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L004525](../../agents/web_agent.py#L4525) | 4525 | `"                    source[\"lead_qualification\"] = \"related_result_not_lead\""` | — |
| [SRC-1AE03B9EC3-L004526](../../agents/web_agent.py#L4526) | 4526 | `"            lead_research_incomplete = ("` | — |
| [SRC-1AE03B9EC3-L004527](../../agents/web_agent.py#L4527) | 4527 | `"                not sources"` | — |
| [SRC-1AE03B9EC3-L004528](../../agents/web_agent.py#L4528) | 4528 | `"                and report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L004529](../../agents/web_agent.py#L4529) | 4529 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004530](../../agents/web_agent.py#L4530) | 4530 | `"            report[\"lead_generation\"] = {"` | — |
| [SRC-1AE03B9EC3-L004531](../../agents/web_agent.py#L4531) | 4531 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L004532](../../agents/web_agent.py#L4532) | 4532 | `"                    \"research_incomplete\" if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L004533](../../agents/web_agent.py#L4533) | 4533 | `"                    else \"candidate_signals_found\" if lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L004534](../../agents/web_agent.py#L4534) | 4534 | `"                    else \"no_qualified_candidates_found\""` | — |
| [SRC-1AE03B9EC3-L004535](../../agents/web_agent.py#L4535) | 4535 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004536](../../agents/web_agent.py#L4536) | 4536 | `"                \"candidate_signal_count\": ("` | — |
| [SRC-1AE03B9EC3-L004537](../../agents/web_agent.py#L4537) | 4537 | `"                    None if lead_research_incomplete else len(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L004538](../../agents/web_agent.py#L4538) | 4538 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004539](../../agents/web_agent.py#L4539) | 4539 | `"                \"related_results_reviewed\": ("` | — |
| [SRC-1AE03B9EC3-L004540](../../agents/web_agent.py#L4540) | 4540 | `"                    None if lead_research_incomplete else related_lead_results_count"` | — |
| [SRC-1AE03B9EC3-L004541](../../agents/web_agent.py#L4541) | 4541 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004542](../../agents/web_agent.py#L4542) | 4542 | `"                \"qualification_rule\": \"explicit_public_buyer_intent_phrase\","` | — |
| [SRC-1AE03B9EC3-L004543](../../agents/web_agent.py#L4543) | 4543 | `"                \"identity_verified\": False,"` | — |
| [SRC-1AE03B9EC3-L004544](../../agents/web_agent.py#L4544) | 4544 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004545](../../agents/web_agent.py#L4545) | 4545 | `"            if not lead_evidence_sources:"` | — |
| [SRC-1AE03B9EC3-L004546](../../agents/web_agent.py#L4546) | 4546 | `"                if sources:"` | — |
| [SRC-1AE03B9EC3-L004547](../../agents/web_agent.py#L4547) | 4547 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L004548](../../agents/web_agent.py#L4548) | 4548 | `"                        \"لم أعثر على إشارة نصية واضحة تثبت أن أي نتيجة في هذه الجولة تتعلق بشخص \""` | — |
| [SRC-1AE03B9EC3-L004549](../../agents/web_agent.py#L4549) | 4549 | `"                        \"يريد الشراء. راجعت \""` | — |
| [SRC-1AE03B9EC3-L004550](../../agents/web_agent.py#L4550) | 4550 | `"                        + str(len(sources))"` | — |
| [SRC-1AE03B9EC3-L004551](../../agents/web_agent.py#L4551) | 4551 | `"                        + \" نتيجة مرتبطة بالموضوع، لكنني لم أعتبر إعلانات البيع أو صفحات السوق \""` | — |
| [SRC-1AE03B9EC3-L004552](../../agents/web_agent.py#L4552) | 4552 | `"                        \"عملاء محتملين. الروابط أدناه نتائج مرتبطة بالموضوع فقط وليست عملاء.\""` | — |
| [SRC-1AE03B9EC3-L004553](../../agents/web_agent.py#L4553) | 4553 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004554](../../agents/web_agent.py#L4554) | 4554 | `"                elif report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L004555](../../agents/web_agent.py#L4555) | 4555 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L004556](../../agents/web_agent.py#L4556) | 4556 | `"                        \"تعطل مسار البحث أو لم يمكن تأكيد اكتماله؛ لذلك لا أستطيع تحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L004557](../../agents/web_agent.py#L4557) | 4557 | `"                        \"كانت هناك نتائج تصلح كعملاء محتملين في هذه الجولة.\""` | — |
| [SRC-1AE03B9EC3-L004558](../../agents/web_agent.py#L4558) | 4558 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004559](../../agents/web_agent.py#L4559) | 4559 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L004560](../../agents/web_agent.py#L4560) | 4560 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L004561](../../agents/web_agent.py#L4561) | 4561 | `"                        \"لم تظهر نتائج قابلة للاستخدام تثبت نية شراء في هذه الجولة. هذا لا يثبت \""` | — |
| [SRC-1AE03B9EC3-L004562](../../agents/web_agent.py#L4562) | 4562 | `"                        \"عدم وجود عملاء؛ بل يعني أن البحث الحالي لم يعثر على دليل كافٍ.\""` | — |
| [SRC-1AE03B9EC3-L004563](../../agents/web_agent.py#L4563) | 4563 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004564](../../agents/web_agent.py#L4564) | 4564 | `"                report[\"research_quality\"] = \"failed\""` | — |
| [SRC-1AE03B9EC3-L004565](../../agents/web_agent.py#L4565) | 4565 | `"                # Distinguish zero qualified signals from unknown counts after an exception."` | — |
| [SRC-1AE03B9EC3-L004566](../../agents/web_agent.py#L4566) | 4566 | `"                report[\"usable_sources_after_filtering\"] = ("` | — |
| [SRC-1AE03B9EC3-L004567](../../agents/web_agent.py#L4567) | 4567 | `"                    None if lead_research_incomplete else len(sources)"` | — |
| [SRC-1AE03B9EC3-L004568](../../agents/web_agent.py#L4568) | 4568 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004569](../../agents/web_agent.py#L4569) | 4569 | `"                report[\"evidence_signals\"] = ("` | — |
| [SRC-1AE03B9EC3-L004570](../../agents/web_agent.py#L4570) | 4570 | `"                    None if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L004571](../../agents/web_agent.py#L4571) | 4571 | `"                    else evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L004572](../../agents/web_agent.py#L4572) | 4572 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004573](../../agents/web_agent.py#L4573) | 4573 | `"                public_related_sources = [{"` | — |
| [SRC-1AE03B9EC3-L004574](../../agents/web_agent.py#L4574) | 4574 | `"                    \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L004575](../../agents/web_agent.py#L4575) | 4575 | `"                    \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L004576](../../agents/web_agent.py#L4576) | 4576 | `"                    \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004577](../../agents/web_agent.py#L4577) | 4577 | `"                    \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L004578](../../agents/web_agent.py#L4578) | 4578 | `"                    \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L004579](../../agents/web_agent.py#L4579) | 4579 | `"                    \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L004580](../../agents/web_agent.py#L4580) | 4580 | `"                    \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L004581](../../agents/web_agent.py#L4581) | 4581 | `"                    \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004582](../../agents/web_agent.py#L4582) | 4582 | `"                    \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L004583](../../agents/web_agent.py#L4583) | 4583 | `"                    \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004584](../../agents/web_agent.py#L4584) | 4584 | `"                    \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004585](../../agents/web_agent.py#L4585) | 4585 | `"                    \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004586](../../agents/web_agent.py#L4586) | 4586 | `"                    \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L004587](../../agents/web_agent.py#L4587) | 4587 | `"                    \"lead_qualification\": \"related_result_not_lead\","` | — |
| [SRC-1AE03B9EC3-L004588](../../agents/web_agent.py#L4588) | 4588 | `"                } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L004589](../../agents/web_agent.py#L4589) | 4589 | `"                return {"` | — |
| [SRC-1AE03B9EC3-L004590](../../agents/web_agent.py#L4590) | 4590 | `"                    \"answer\": lead_answer,"` | — |
| [SRC-1AE03B9EC3-L004591](../../agents/web_agent.py#L4591) | 4591 | `"                    \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L004592](../../agents/web_agent.py#L4592) | 4592 | `"                    \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L004593](../../agents/web_agent.py#L4593) | 4593 | `"                    \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L004594](../../agents/web_agent.py#L4594) | 4594 | `"                    \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L004595](../../agents/web_agent.py#L4595) | 4595 | `"                        \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L004596](../../agents/web_agent.py#L4596) | 4596 | `"                        \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L004597](../../agents/web_agent.py#L4597) | 4597 | `"                        \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L004598](../../agents/web_agent.py#L4598) | 4598 | `"                        \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L004599](../../agents/web_agent.py#L4599) | 4599 | `"                        \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L004600](../../agents/web_agent.py#L4600) | 4600 | `"                        \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L004601](../../agents/web_agent.py#L4601) | 4601 | `"                        \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L004602](../../agents/web_agent.py#L4602) | 4602 | `"                        \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L004603](../../agents/web_agent.py#L4603) | 4603 | `"                        \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L004604](../../agents/web_agent.py#L4604) | 4604 | `"                        \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L004605](../../agents/web_agent.py#L4605) | 4605 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L004606](../../agents/web_agent.py#L4606) | 4606 | `"                    \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L004607](../../agents/web_agent.py#L4607) | 4607 | `"                    \"sources\": public_related_sources,"` | — |
| [SRC-1AE03B9EC3-L004608](../../agents/web_agent.py#L4608) | 4608 | `"                    \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L004609](../../agents/web_agent.py#L4609) | 4609 | `"                    \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L004610](../../agents/web_agent.py#L4610) | 4610 | `"                    \"search_attempted\": report.get("` | — |
| [SRC-1AE03B9EC3-L004611](../../agents/web_agent.py#L4611) | 4611 | `"                        \"search_attempted\","` | — |
| [SRC-1AE03B9EC3-L004612](../../agents/web_agent.py#L4612) | 4612 | `"                        bool(report.get(\"queries_attempted\", 0)),"` | — |
| [SRC-1AE03B9EC3-L004613](../../agents/web_agent.py#L4613) | 4613 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L004614](../../agents/web_agent.py#L4614) | 4614 | `"                    \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L004615](../../agents/web_agent.py#L4615) | 4615 | `"                    \"warnings\": [lead_answer],"` | — |
| [SRC-1AE03B9EC3-L004616](../../agents/web_agent.py#L4616) | 4616 | `"                    \"kind\": \"lead_discovery_no_qualified_candidates\","` | — |
| [SRC-1AE03B9EC3-L004617](../../agents/web_agent.py#L4617) | 4617 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L004618](../../agents/web_agent.py#L4618) | 4618 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L004619](../../agents/web_agent.py#L4619) | 4619 | `"                    \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L004620](../../agents/web_agent.py#L4620) | 4620 | `"                }"` | — |
| [SRC-1AE03B9EC3-L004621](../../agents/web_agent.py#L4621) | 4621 | `"            # Only explicit public buyer-intent signals may be synthesized as lead candidates."` | — |
| [SRC-1AE03B9EC3-L004622](../../agents/web_agent.py#L4622) | 4622 | `"            sources = lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L004623](../../agents/web_agent.py#L4623) | 4623 | `"            report[\"evidence_signals\"] = evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L004624](../../agents/web_agent.py#L4624) | 4624 | `"            report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004625](../../agents/web_agent.py#L4625) | 4625 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004626](../../agents/web_agent.py#L4626) | 4626 | `"            report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L004627](../../agents/web_agent.py#L4627) | 4627 | `"            independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L004628](../../agents/web_agent.py#L4628) | 4628 | `"                registrable_domain("` | — |
| [SRC-1AE03B9EC3-L004629](../../agents/web_agent.py#L4629) | 4629 | `"                    source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L004630](../../agents/web_agent.py#L4630) | 4630 | `"                    or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L004631](../../agents/web_agent.py#L4631) | 4631 | `"                    or \"\""` | — |
| [SRC-1AE03B9EC3-L004632](../../agents/web_agent.py#L4632) | 4632 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004633](../../agents/web_agent.py#L4633) | 4633 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L004634](../../agents/web_agent.py#L4634) | 4634 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004635](../../agents/web_agent.py#L4635) | 4635 | `"            independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L004636](../../agents/web_agent.py#L4636) | 4636 | `"        single_source_navigation = navigation_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L004637](../../agents/web_agent.py#L4637) | 4637 | `"        single_source_social = bool(plan.get(\"social_focus\")) and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L004638](../../agents/web_agent.py#L4638) | 4638 | `"        single_source_lead = lead_request and bool(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L004639](../../agents/web_agent.py#L4639) | 4639 | `"        single_source_listing = listing_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L004640](../../agents/web_agent.py#L4640) | 4640 | `"        task_specific_partial_evidence = ("` | — |
| [SRC-1AE03B9EC3-L004641](../../agents/web_agent.py#L4641) | 4641 | `"            single_source_page_summary"` | — |
| [SRC-1AE03B9EC3-L004642](../../agents/web_agent.py#L4642) | 4642 | `"            or single_source_navigation"` | — |
| [SRC-1AE03B9EC3-L004643](../../agents/web_agent.py#L4643) | 4643 | `"            or single_source_social"` | — |
| [SRC-1AE03B9EC3-L004644](../../agents/web_agent.py#L4644) | 4644 | `"            or single_source_lead"` | — |
| [SRC-1AE03B9EC3-L004645](../../agents/web_agent.py#L4645) | 4645 | `"            or single_source_listing"` | — |
| [SRC-1AE03B9EC3-L004646](../../agents/web_agent.py#L4646) | 4646 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004647](../../agents/web_agent.py#L4647) | 4647 | `"        needs_corroboration = len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L004648](../../agents/web_agent.py#L4648) | 4648 | `"        evidence_repair: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L004649](../../agents/web_agent.py#L4649) | 4649 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L004650](../../agents/web_agent.py#L4650) | 4650 | `"            \"max_extra_queries\": 1,"` | — |
| [SRC-1AE03B9EC3-L004651](../../agents/web_agent.py#L4651) | 4651 | `"            \"reason\": \"initial_evidence_gate_satisfied\" if not needs_corroboration else \"not_attempted\","` | — |
| [SRC-1AE03B9EC3-L004652](../../agents/web_agent.py#L4652) | 4652 | `"        }"` | — |
| [SRC-1AE03B9EC3-L004653](../../agents/web_agent.py#L4653) | 4653 | `"        if needs_corroboration and not plan.get(\"queries\"):"` | — |
| [SRC-1AE03B9EC3-L004654](../../agents/web_agent.py#L4654) | 4654 | `"            evidence_repair[\"reason\"] = \"no_topic_query_available\""` | — |
| [SRC-1AE03B9EC3-L004655](../../agents/web_agent.py#L4655) | 4655 | `"        elif needs_corroboration:"` | — |
| [SRC-1AE03B9EC3-L004656](../../agents/web_agent.py#L4656) | 4656 | `"            if task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L004657](../../agents/web_agent.py#L4657) | 4657 | `"                evidence_repair[\"reason\"] = \"task_specific_partial_evidence\""` | — |
| [SRC-1AE03B9EC3-L004658](../../agents/web_agent.py#L4658) | 4658 | `"            elif plan.get(\"social_focus\"):"` | — |
| [SRC-1AE03B9EC3-L004659](../../agents/web_agent.py#L4659) | 4659 | `"                evidence_repair[\"reason\"] = \"social_search_not_retried\""` | — |
| [SRC-1AE03B9EC3-L004660](../../agents/web_agent.py#L4660) | 4660 | `"            elif plan.get(\"depth\") == \"deep\" or report.get(\"expansion_queries\"):"` | — |
| [SRC-1AE03B9EC3-L004661](../../agents/web_agent.py#L4661) | 4661 | `"                evidence_repair[\"reason\"] = \"deep_research_already_expanded\""` | — |
| [SRC-1AE03B9EC3-L004662](../../agents/web_agent.py#L4662) | 4662 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004663](../../agents/web_agent.py#L4663) | 4663 | `"                original_queries = ["` | — |
| [SRC-1AE03B9EC3-L004664](../../agents/web_agent.py#L4664) | 4664 | `"                    str(item).strip()"` | — |
| [SRC-1AE03B9EC3-L004665](../../agents/web_agent.py#L4665) | 4665 | `"                    for item in plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L004666](../../agents/web_agent.py#L4666) | 4666 | `"                    if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L004667](../../agents/web_agent.py#L4667) | 4667 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004668](../../agents/web_agent.py#L4668) | 4668 | `"                base_query = ("` | — |
| [SRC-1AE03B9EC3-L004669](../../agents/web_agent.py#L4669) | 4669 | `"                    original_queries[0]"` | — |
| [SRC-1AE03B9EC3-L004670](../../agents/web_agent.py#L4670) | 4670 | `"                    if original_queries"` | — |
| [SRC-1AE03B9EC3-L004671](../../agents/web_agent.py#L4671) | 4671 | `"                    else compact_search_query(working_question)"` | — |
| [SRC-1AE03B9EC3-L004672](../../agents/web_agent.py#L4672) | 4672 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004673](../../agents/web_agent.py#L4673) | 4673 | `"                suffix = ("` | — |
| [SRC-1AE03B9EC3-L004674](../../agents/web_agent.py#L4674) | 4674 | `"                    \"latest official primary source\""` | — |
| [SRC-1AE03B9EC3-L004675](../../agents/web_agent.py#L4675) | 4675 | `"                    if plan.get(\"freshness\") == \"current\""` | — |
| [SRC-1AE03B9EC3-L004676](../../agents/web_agent.py#L4676) | 4676 | `"                    else \"official primary source data\""` | — |
| [SRC-1AE03B9EC3-L004677](../../agents/web_agent.py#L4677) | 4677 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004678](../../agents/web_agent.py#L4678) | 4678 | `"                repair_query = compact_search_query(f\"{base_query} {suffix}\")"` | — |
| [SRC-1AE03B9EC3-L004679](../../agents/web_agent.py#L4679) | 4679 | `"                if not repair_query or not _relevance_query_tokens(repair_query):"` | — |
| [SRC-1AE03B9EC3-L004680](../../agents/web_agent.py#L4680) | 4680 | `"                    evidence_repair[\"reason\"] = \"no_topic_query_available\""` | — |
| [SRC-1AE03B9EC3-L004681](../../agents/web_agent.py#L4681) | 4681 | `"                    repair_query = \"\""` | — |
| [SRC-1AE03B9EC3-L004682](../../agents/web_agent.py#L4682) | 4682 | `"                known_queries = {"` | — |
| [SRC-1AE03B9EC3-L004683](../../agents/web_agent.py#L4683) | 4683 | `"                    _normalize_search_query(item).casefold()"` | — |
| [SRC-1AE03B9EC3-L004684](../../agents/web_agent.py#L4684) | 4684 | `"                    for item in original_queries"` | — |
| [SRC-1AE03B9EC3-L004685](../../agents/web_agent.py#L4685) | 4685 | `"                }"` | — |
| [SRC-1AE03B9EC3-L004686](../../agents/web_agent.py#L4686) | 4686 | `"                if repair_query and _normalize_search_query(repair_query).casefold() in known_queries:"` | — |
| [SRC-1AE03B9EC3-L004687](../../agents/web_agent.py#L4687) | 4687 | `"                    repair_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L004688](../../agents/web_agent.py#L4688) | 4688 | `"                        f\"{base_query} independent corroborating evidence\""` | — |
| [SRC-1AE03B9EC3-L004689](../../agents/web_agent.py#L4689) | 4689 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004690](../../agents/web_agent.py#L4690) | 4690 | `"                if repair_query and _relevance_query_tokens(repair_query) and ("` | — |
| [SRC-1AE03B9EC3-L004691](../../agents/web_agent.py#L4691) | 4691 | `"                    _normalize_search_query(repair_query).casefold() not in known_queries"` | — |
| [SRC-1AE03B9EC3-L004692](../../agents/web_agent.py#L4692) | 4692 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004693](../../agents/web_agent.py#L4693) | 4693 | `"                    initial_source_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004694](../../agents/web_agent.py#L4694) | 4694 | `"                    initial_domain_count = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L004695](../../agents/web_agent.py#L4695) | 4695 | `"                    evidence_repair[\"attempted\"] = True"` | — |
| [SRC-1AE03B9EC3-L004696](../../agents/web_agent.py#L4696) | 4696 | `"                    evidence_repair[\"reason\"] = \"thin_or_unrelated_initial_evidence\""` | — |
| [SRC-1AE03B9EC3-L004697](../../agents/web_agent.py#L4697) | 4697 | `"                    evidence_repair[\"query\"] = repair_query"` | — |
| [SRC-1AE03B9EC3-L004698](../../agents/web_agent.py#L4698) | 4698 | `"                    repair_plan = dict(plan)"` | — |
| [SRC-1AE03B9EC3-L004699](../../agents/web_agent.py#L4699) | 4699 | `"                    repair_plan.update({"` | — |
| [SRC-1AE03B9EC3-L004700](../../agents/web_agent.py#L4700) | 4700 | `"                        \"queries\": [repair_query],"` | — |
| [SRC-1AE03B9EC3-L004701](../../agents/web_agent.py#L4701) | 4701 | `"                        \"depth\": \"standard\","` | — |
| [SRC-1AE03B9EC3-L004702](../../agents/web_agent.py#L4702) | 4702 | `"                        \"social_focus\": False,"` | — |
| [SRC-1AE03B9EC3-L004703](../../agents/web_agent.py#L4703) | 4703 | `"                        \"platforms\": [],"` | — |
| [SRC-1AE03B9EC3-L004704](../../agents/web_agent.py#L4704) | 4704 | `"                        \"direct_urls\": [],"` | — |
| [SRC-1AE03B9EC3-L004705](../../agents/web_agent.py#L4705) | 4705 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L004706](../../agents/web_agent.py#L4706) | 4706 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L004707](../../agents/web_agent.py#L4707) | 4707 | `"                        repair_sources, repair_warnings, repair_report = self._collect_research("` | — |
| [SRC-1AE03B9EC3-L004708](../../agents/web_agent.py#L4708) | 4708 | `"                            repair_plan"` | — |
| [SRC-1AE03B9EC3-L004709](../../agents/web_agent.py#L4709) | 4709 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004710](../../agents/web_agent.py#L4710) | 4710 | `"                    except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L004711](../../agents/web_agent.py#L4711) | 4711 | `"                        repair_sources = []"` | — |
| [SRC-1AE03B9EC3-L004712](../../agents/web_agent.py#L4712) | 4712 | `"                        repair_warnings = []"` | — |
| [SRC-1AE03B9EC3-L004713](../../agents/web_agent.py#L4713) | 4713 | `"                        repair_report = {"` | — |
| [SRC-1AE03B9EC3-L004714](../../agents/web_agent.py#L4714) | 4714 | `"                            \"queries_planned\": 1,"` | — |
| [SRC-1AE03B9EC3-L004715](../../agents/web_agent.py#L4715) | 4715 | `"                            \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L004716](../../agents/web_agent.py#L4716) | 4716 | `"                            \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L004717](../../agents/web_agent.py#L4717) | 4717 | `"                            \"search_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L004718](../../agents/web_agent.py#L4718) | 4718 | `"                            \"search_outcome\": \"unknown_after_research_error\","` | — |
| [SRC-1AE03B9EC3-L004719](../../agents/web_agent.py#L4719) | 4719 | `"                            \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L004720](../../agents/web_agent.py#L4720) | 4720 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L004721](../../agents/web_agent.py#L4721) | 4721 | `"                        search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004722](../../agents/web_agent.py#L4722) | 4722 | `"                            \"تعذر تنفيذ محاولة البحث الإضافية المحدودة (\""` | — |
| [SRC-1AE03B9EC3-L004723](../../agents/web_agent.py#L4723) | 4723 | `"                            + type(exc).__name__ + \").\""` | — |
| [SRC-1AE03B9EC3-L004724](../../agents/web_agent.py#L4724) | 4724 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004725](../../agents/web_agent.py#L4725) | 4725 | `"                    search_warnings.extend(repair_warnings)"` | — |
| [SRC-1AE03B9EC3-L004726](../../agents/web_agent.py#L4726) | 4726 | `"                    evidence_repair[\"attempted_query_count\"] = 1"` | — |
| [SRC-1AE03B9EC3-L004727](../../agents/web_agent.py#L4727) | 4727 | `"                    evidence_repair[\"initial_source_count\"] = initial_source_count"` | — |
| [SRC-1AE03B9EC3-L004728](../../agents/web_agent.py#L4728) | 4728 | `"                    evidence_repair[\"initial_independent_domain_count\"] = initial_domain_count"` | — |
| [SRC-1AE03B9EC3-L004729](../../agents/web_agent.py#L4729) | 4729 | `"                    evidence_repair[\"new_sources_added\"] = 0"` | — |
| [SRC-1AE03B9EC3-L004730](../../agents/web_agent.py#L4730) | 4730 | `"                    source_indexes: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L004731](../../agents/web_agent.py#L4731) | 4731 | `"                    for source_index, source in enumerate(sources):"` | — |
| [SRC-1AE03B9EC3-L004732](../../agents/web_agent.py#L4732) | 4732 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L004733](../../agents/web_agent.py#L4733) | 4733 | `"                        if source_key:"` | — |
| [SRC-1AE03B9EC3-L004734](../../agents/web_agent.py#L4734) | 4734 | `"                            source_indexes.setdefault(source_key, source_index)"` | — |
| [SRC-1AE03B9EC3-L004735](../../agents/web_agent.py#L4735) | 4735 | `"                    relevant_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004736](../../agents/web_agent.py#L4736) | 4736 | `"                        query"` | — |
| [SRC-1AE03B9EC3-L004737](../../agents/web_agent.py#L4737) | 4737 | `"                        for query in ("` | — |
| [SRC-1AE03B9EC3-L004738](../../agents/web_agent.py#L4738) | 4738 | `"                            compact_search_query(working_question),"` | — |
| [SRC-1AE03B9EC3-L004739](../../agents/web_agent.py#L4739) | 4739 | `"                            *("` | — |
| [SRC-1AE03B9EC3-L004740](../../agents/web_agent.py#L4740) | 4740 | `"                                compact_search_query(candidate)"` | — |
| [SRC-1AE03B9EC3-L004741](../../agents/web_agent.py#L4741) | 4741 | `"                                for candidate in original_queries"` | — |
| [SRC-1AE03B9EC3-L004742](../../agents/web_agent.py#L4742) | 4742 | `"                                if isinstance(candidate, str)"` | — |
| [SRC-1AE03B9EC3-L004743](../../agents/web_agent.py#L4743) | 4743 | `"                            ),"` | — |
| [SRC-1AE03B9EC3-L004744](../../agents/web_agent.py#L4744) | 4744 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004745](../../agents/web_agent.py#L4745) | 4745 | `"                        if query"` | — |
| [SRC-1AE03B9EC3-L004746](../../agents/web_agent.py#L4746) | 4746 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L004747](../../agents/web_agent.py#L4747) | 4747 | `"                    for source in repair_sources:"` | — |
| [SRC-1AE03B9EC3-L004748](../../agents/web_agent.py#L4748) | 4748 | `"                        if not isinstance(source, dict):"` | — |
| [SRC-1AE03B9EC3-L004749](../../agents/web_agent.py#L4749) | 4749 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L004750](../../agents/web_agent.py#L4750) | 4750 | `"                        if not any("` | — |
| [SRC-1AE03B9EC3-L004751](../../agents/web_agent.py#L4751) | 4751 | `"                            self._source_matches_query(candidate, source)"` | — |
| [SRC-1AE03B9EC3-L004752](../../agents/web_agent.py#L4752) | 4752 | `"                            for candidate in relevant_queries if candidate"` | — |
| [SRC-1AE03B9EC3-L004753](../../agents/web_agent.py#L4753) | 4753 | `"                        ):"` | — |
| [SRC-1AE03B9EC3-L004754](../../agents/web_agent.py#L4754) | 4754 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L004755](../../agents/web_agent.py#L4755) | 4755 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L004756](../../agents/web_agent.py#L4756) | 4756 | `"                        if not source_key:"` | — |
| [SRC-1AE03B9EC3-L004757](../../agents/web_agent.py#L4757) | 4757 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L004758](../../agents/web_agent.py#L4758) | 4758 | `"                        existing_index = source_indexes.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L004759](../../agents/web_agent.py#L4759) | 4759 | `"                        if existing_index is None:"` | — |
| [SRC-1AE03B9EC3-L004760](../../agents/web_agent.py#L4760) | 4760 | `"                            source_indexes[source_key] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004761](../../agents/web_agent.py#L4761) | 4761 | `"                            sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004762](../../agents/web_agent.py#L4762) | 4762 | `"                            evidence_repair[\"new_sources_added\"] += 1"` | — |
| [SRC-1AE03B9EC3-L004763](../../agents/web_agent.py#L4763) | 4763 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L004764](../../agents/web_agent.py#L4764) | 4764 | `"                        existing_source = sources[existing_index]"` | — |
| [SRC-1AE03B9EC3-L004765](../../agents/web_agent.py#L4765) | 4765 | `"                        providers = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004766](../../agents/web_agent.py#L4766) | 4766 | `"                            list(existing_source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L004767](../../agents/web_agent.py#L4767) | 4767 | `"                            + list(source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L004768](../../agents/web_agent.py#L4768) | 4768 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L004769](../../agents/web_agent.py#L4769) | 4769 | `"                        source_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004770](../../agents/web_agent.py#L4770) | 4770 | `"                            list(existing_source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L004771](../../agents/web_agent.py#L4771) | 4771 | `"                            + list(source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L004772](../../agents/web_agent.py#L4772) | 4772 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L004773](../../agents/web_agent.py#L4773) | 4773 | `"                        if source.get(\"page_fetched\") and not existing_source.get(\"page_fetched\"):"` | — |
| [SRC-1AE03B9EC3-L004774](../../agents/web_agent.py#L4774) | 4774 | `"                            merged_source = dict(existing_source)"` | — |
| [SRC-1AE03B9EC3-L004775](../../agents/web_agent.py#L4775) | 4775 | `"                            merged_source.update(source)"` | — |
| [SRC-1AE03B9EC3-L004776](../../agents/web_agent.py#L4776) | 4776 | `"                            merged_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L004777](../../agents/web_agent.py#L4777) | 4777 | `"                            merged_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L004778](../../agents/web_agent.py#L4778) | 4778 | `"                            sources[existing_index] = merged_source"` | — |
| [SRC-1AE03B9EC3-L004779](../../agents/web_agent.py#L4779) | 4779 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L004780](../../agents/web_agent.py#L4780) | 4780 | `"                            existing_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L004781](../../agents/web_agent.py#L4781) | 4781 | `"                            existing_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L004782](../../agents/web_agent.py#L4782) | 4782 | `"                    sources.sort("` | — |
| [SRC-1AE03B9EC3-L004783](../../agents/web_agent.py#L4783) | 4783 | `"                        key=lambda item: float(item.get(\"rank_score\", 0) or 0),"` | — |
| [SRC-1AE03B9EC3-L004784](../../agents/web_agent.py#L4784) | 4784 | `"                        reverse=True,"` | — |
| [SRC-1AE03B9EC3-L004785](../../agents/web_agent.py#L4785) | 4785 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004786](../../agents/web_agent.py#L4786) | 4786 | `"                    plan[\"queries\"] = list(dict.fromkeys(original_queries + [repair_query]))"` | — |
| [SRC-1AE03B9EC3-L004787](../../agents/web_agent.py#L4787) | 4787 | `"                    independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L004788](../../agents/web_agent.py#L4788) | 4788 | `"                        registrable_domain("` | — |
| [SRC-1AE03B9EC3-L004789](../../agents/web_agent.py#L4789) | 4789 | `"                            source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L004790](../../agents/web_agent.py#L4790) | 4790 | `"                            or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L004791](../../agents/web_agent.py#L4791) | 4791 | `"                            or \"\""` | — |
| [SRC-1AE03B9EC3-L004792](../../agents/web_agent.py#L4792) | 4792 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004793](../../agents/web_agent.py#L4793) | 4793 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L004794](../../agents/web_agent.py#L4794) | 4794 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L004795](../../agents/web_agent.py#L4795) | 4795 | `"                    independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L004796](../../agents/web_agent.py#L4796) | 4796 | `"                    needs_corroboration = ("` | — |
| [SRC-1AE03B9EC3-L004797](../../agents/web_agent.py#L4797) | 4797 | `"                        len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L004798](../../agents/web_agent.py#L4798) | 4798 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004799](../../agents/web_agent.py#L4799) | 4799 | `"                    evidence_repair.update({"` | — |
| [SRC-1AE03B9EC3-L004800](../../agents/web_agent.py#L4800) | 4800 | `"                        \"final_source_count\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L004801](../../agents/web_agent.py#L4801) | 4801 | `"                        \"final_independent_domain_count\": len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L004802](../../agents/web_agent.py#L4802) | 4802 | `"                        \"recovered\": not needs_corroboration,"` | — |
| [SRC-1AE03B9EC3-L004803](../../agents/web_agent.py#L4803) | 4803 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L004804](../../agents/web_agent.py#L4804) | 4804 | `"                    evidence_repair[\"reason\"] = ("` | — |
| [SRC-1AE03B9EC3-L004805](../../agents/web_agent.py#L4805) | 4805 | `"                        \"single_bounded_retry_still_insufficient\""` | — |
| [SRC-1AE03B9EC3-L004806](../../agents/web_agent.py#L4806) | 4806 | `"                        if needs_corroboration else \"evidence_gate_recovered\""` | — |
| [SRC-1AE03B9EC3-L004807](../../agents/web_agent.py#L4807) | 4807 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004808](../../agents/web_agent.py#L4808) | 4808 | `"                    report[\"queries_planned\"] = int(report.get(\"queries_planned\", 0) or 0) + int("` | — |
| [SRC-1AE03B9EC3-L004809](../../agents/web_agent.py#L4809) | 4809 | `"                        repair_report.get(\"queries_planned\", 1) or 0"` | — |
| [SRC-1AE03B9EC3-L004810](../../agents/web_agent.py#L4810) | 4810 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004811](../../agents/web_agent.py#L4811) | 4811 | `"                    initial_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L004812](../../agents/web_agent.py#L4812) | 4812 | `"                    repair_attempt_count = repair_report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L004813](../../agents/web_agent.py#L4813) | 4813 | `"                    if initial_attempt_count is None or repair_attempt_count is None:"` | — |
| [SRC-1AE03B9EC3-L004814](../../agents/web_agent.py#L4814) | 4814 | `"                        report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L004815](../../agents/web_agent.py#L4815) | 4815 | `"                        report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L004816](../../agents/web_agent.py#L4816) | 4816 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L004817](../../agents/web_agent.py#L4817) | 4817 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L004818](../../agents/web_agent.py#L4818) | 4818 | `"                            report[\"queries_attempted\"] = max(0, int(initial_attempt_count or 0)) + max("` | — |
| [SRC-1AE03B9EC3-L004819](../../agents/web_agent.py#L4819) | 4819 | `"                                0, int(repair_attempt_count or 0)"` | — |
| [SRC-1AE03B9EC3-L004820](../../agents/web_agent.py#L4820) | 4820 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L004821](../../agents/web_agent.py#L4821) | 4821 | `"                            report[\"queries_attempted_known\"] = True"` | — |
| [SRC-1AE03B9EC3-L004822](../../agents/web_agent.py#L4822) | 4822 | `"                        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L004823](../../agents/web_agent.py#L4823) | 4823 | `"                            report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L004824](../../agents/web_agent.py#L4824) | 4824 | `"                            report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L004825](../../agents/web_agent.py#L4825) | 4825 | `"                    report[\"query_results\"] = list(report.get(\"query_results\", [])) + list("` | — |
| [SRC-1AE03B9EC3-L004826](../../agents/web_agent.py#L4826) | 4826 | `"                        repair_report.get(\"query_results\", [])"` | — |
| [SRC-1AE03B9EC3-L004827](../../agents/web_agent.py#L4827) | 4827 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004828](../../agents/web_agent.py#L4828) | 4828 | `"                    merged_providers = {"` | — |
| [SRC-1AE03B9EC3-L004829](../../agents/web_agent.py#L4829) | 4829 | `"                        provider"` | — |
| [SRC-1AE03B9EC3-L004830](../../agents/web_agent.py#L4830) | 4830 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L004831](../../agents/web_agent.py#L4831) | 4831 | `"                        for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L004832](../../agents/web_agent.py#L4832) | 4832 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L004833](../../agents/web_agent.py#L4833) | 4833 | `"                    report[\"providers_used\"] = sorted(merged_providers)"` | — |
| [SRC-1AE03B9EC3-L004834](../../agents/web_agent.py#L4834) | 4834 | `"                    report[\"provider_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L004835](../../agents/web_agent.py#L4835) | 4835 | `"                        provider: sum("` | — |
| [SRC-1AE03B9EC3-L004836](../../agents/web_agent.py#L4836) | 4836 | `"                            provider in source.get(\"providers\", []) for source in sources"` | — |
| [SRC-1AE03B9EC3-L004837](../../agents/web_agent.py#L4837) | 4837 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004838](../../agents/web_agent.py#L4838) | 4838 | `"                        for provider in merged_providers"` | — |
| [SRC-1AE03B9EC3-L004839](../../agents/web_agent.py#L4839) | 4839 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L004840](../../agents/web_agent.py#L4840) | 4840 | `"                    report[\"platform_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L004841](../../agents/web_agent.py#L4841) | 4841 | `"                        str(source.get(\"platform\", \"web\")): sum("` | — |
| [SRC-1AE03B9EC3-L004842](../../agents/web_agent.py#L4842) | 4842 | `"                            str(other.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L004843](../../agents/web_agent.py#L4843) | 4843 | `"                            == str(source.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L004844](../../agents/web_agent.py#L4844) | 4844 | `"                            for other in sources"` | — |
| [SRC-1AE03B9EC3-L004845](../../agents/web_agent.py#L4845) | 4845 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004846](../../agents/web_agent.py#L4846) | 4846 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L004847](../../agents/web_agent.py#L4847) | 4847 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L004848](../../agents/web_agent.py#L4848) | 4848 | `"                    report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004849](../../agents/web_agent.py#L4849) | 4849 | `"                    report[\"pages_fetched\"] = sum("` | — |
| [SRC-1AE03B9EC3-L004850](../../agents/web_agent.py#L4850) | 4850 | `"                        bool(source.get(\"page_fetched\")) for source in sources"` | — |
| [SRC-1AE03B9EC3-L004851](../../agents/web_agent.py#L4851) | 4851 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004852](../../agents/web_agent.py#L4852) | 4852 | `"                    report[\"independent_sources\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L004853](../../agents/web_agent.py#L4853) | 4853 | `"                    report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L004854](../../agents/web_agent.py#L4854) | 4854 | `"                    report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L004855](../../agents/web_agent.py#L4855) | 4855 | `"                        sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L004856](../../agents/web_agent.py#L4856) | 4856 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004857](../../agents/web_agent.py#L4857) | 4857 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L004858](../../agents/web_agent.py#L4858) | 4858 | `"                    evidence_repair[\"reason\"] = \"repair_query_was_not_distinct\""` | — |
| [SRC-1AE03B9EC3-L004859](../../agents/web_agent.py#L4859) | 4859 | `"        report[\"evidence_repair\"] = evidence_repair"` | — |
| [SRC-1AE03B9EC3-L004860](../../agents/web_agent.py#L4860) | 4860 | `"        baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L004861](../../agents/web_agent.py#L4861) | 4861 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L004862](../../agents/web_agent.py#L4862) | 4862 | `"            current_research_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L004863](../../agents/web_agent.py#L4863) | 4863 | `"                item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004864](../../agents/web_agent.py#L4864) | 4864 | `"                if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L004865](../../agents/web_agent.py#L4865) | 4865 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L004866](../../agents/web_agent.py#L4866) | 4866 | `"        report[\"provider_diagnostics\"] = current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004867](../../agents/web_agent.py#L4867) | 4867 | `"        provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L004868](../../agents/web_agent.py#L4868) | 4868 | `"            item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L004869](../../agents/web_agent.py#L4869) | 4869 | `"            for item in current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004870](../../agents/web_agent.py#L4870) | 4870 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004871](../../agents/web_agent.py#L4871) | 4871 | `"        raw_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L004872](../../agents/web_agent.py#L4872) | 4872 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L004873](../../agents/web_agent.py#L4873) | 4873 | `"            queries_attempted = ("` | — |
| [SRC-1AE03B9EC3-L004874](../../agents/web_agent.py#L4874) | 4874 | `"                None if raw_attempt_count is None"` | — |
| [SRC-1AE03B9EC3-L004875](../../agents/web_agent.py#L4875) | 4875 | `"                else max(0, int(raw_attempt_count or 0))"` | — |
| [SRC-1AE03B9EC3-L004876](../../agents/web_agent.py#L4876) | 4876 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004877](../../agents/web_agent.py#L4877) | 4877 | `"        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L004878](../../agents/web_agent.py#L4878) | 4878 | `"            queries_attempted = None"` | — |
| [SRC-1AE03B9EC3-L004879](../../agents/web_agent.py#L4879) | 4879 | `"        if queries_attempted is not None:"` | — |
| [SRC-1AE03B9EC3-L004880](../../agents/web_agent.py#L4880) | 4880 | `"            search_attempted = ("` | — |
| [SRC-1AE03B9EC3-L004881](../../agents/web_agent.py#L4881) | 4881 | `"                queries_attempted > 0"` | — |
| [SRC-1AE03B9EC3-L004882](../../agents/web_agent.py#L4882) | 4882 | `"                or provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L004883](../../agents/web_agent.py#L4883) | 4883 | `"                or report.get(\"search_attempted\") is True"` | — |
| [SRC-1AE03B9EC3-L004884](../../agents/web_agent.py#L4884) | 4884 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004885](../../agents/web_agent.py#L4885) | 4885 | `"        elif provider_attempt_observed or report.get(\"search_attempted\") is True:"` | — |
| [SRC-1AE03B9EC3-L004886](../../agents/web_agent.py#L4886) | 4886 | `"            search_attempted = True"` | — |
| [SRC-1AE03B9EC3-L004887](../../agents/web_agent.py#L4887) | 4887 | `"        elif isinstance(report.get(\"search_attempted\"), bool):"` | — |
| [SRC-1AE03B9EC3-L004888](../../agents/web_agent.py#L4888) | 4888 | `"            search_attempted = report[\"search_attempted\"]"` | — |
| [SRC-1AE03B9EC3-L004889](../../agents/web_agent.py#L4889) | 4889 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L004890](../../agents/web_agent.py#L4890) | 4890 | `"            search_attempted = None"` | — |
| [SRC-1AE03B9EC3-L004891](../../agents/web_agent.py#L4891) | 4891 | `"        report[\"queries_attempted\"] = queries_attempted"` | — |
| [SRC-1AE03B9EC3-L004892](../../agents/web_agent.py#L4892) | 4892 | `"        report[\"queries_attempted_known\"] = queries_attempted is not None"` | — |
| [SRC-1AE03B9EC3-L004893](../../agents/web_agent.py#L4893) | 4893 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L004894](../../agents/web_agent.py#L4894) | 4894 | `"        previous_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L004895](../../agents/web_agent.py#L4895) | 4895 | `"        if previous_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L004896](../../agents/web_agent.py#L4896) | 4896 | `"            if provider_attempt_observed or search_attempted is True:"` | — |
| [SRC-1AE03B9EC3-L004897](../../agents/web_agent.py#L4897) | 4897 | `"                search_outcome = \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L004898](../../agents/web_agent.py#L4898) | 4898 | `"            elif search_attempted is False:"` | — |
| [SRC-1AE03B9EC3-L004899](../../agents/web_agent.py#L4899) | 4899 | `"                search_outcome = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L004900](../../agents/web_agent.py#L4900) | 4900 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004901](../../agents/web_agent.py#L4901) | 4901 | `"                search_outcome = \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L004902](../../agents/web_agent.py#L4902) | 4902 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L004903](../../agents/web_agent.py#L4903) | 4903 | `"            search_outcome = ("` | — |
| [SRC-1AE03B9EC3-L004904](../../agents/web_agent.py#L4904) | 4904 | `"                \"attempted_with_usable_sources\" if search_attempted is True and sources"` | — |
| [SRC-1AE03B9EC3-L004905](../../agents/web_agent.py#L4905) | 4905 | `"                else \"attempted_no_usable_sources\" if search_attempted is True"` | — |
| [SRC-1AE03B9EC3-L004906](../../agents/web_agent.py#L4906) | 4906 | `"                else \"not_attempted\" if search_attempted is False"` | — |
| [SRC-1AE03B9EC3-L004907](../../agents/web_agent.py#L4907) | 4907 | `"                else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L004908](../../agents/web_agent.py#L4908) | 4908 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004909](../../agents/web_agent.py#L4909) | 4909 | `"        report[\"search_outcome\"] = search_outcome"` | — |
| [SRC-1AE03B9EC3-L004910](../../agents/web_agent.py#L4910) | 4910 | `"        if search_outcome in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L004911](../../agents/web_agent.py#L4911) | 4911 | `"            report[\"usable_sources_after_filtering\"] = None"` | — |
| [SRC-1AE03B9EC3-L004912](../../agents/web_agent.py#L4912) | 4912 | `"            report[\"unique_sources\"] = None"` | — |
| [SRC-1AE03B9EC3-L004913](../../agents/web_agent.py#L4913) | 4913 | `"            report[\"pages_fetched\"] = None"` | — |
| [SRC-1AE03B9EC3-L004914](../../agents/web_agent.py#L4914) | 4914 | `"            report[\"provider_counts\"] = None"` | — |
| [SRC-1AE03B9EC3-L004915](../../agents/web_agent.py#L4915) | 4915 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L004916](../../agents/web_agent.py#L4916) | 4916 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004917](../../agents/web_agent.py#L4917) | 4917 | `"            if report.get(\"unique_sources\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L004918](../../agents/web_agent.py#L4918) | 4918 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004919](../../agents/web_agent.py#L4919) | 4919 | `"            if report.get(\"pages_fetched\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L004920](../../agents/web_agent.py#L4920) | 4920 | `"                report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L004921](../../agents/web_agent.py#L4921) | 4921 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L004922](../../agents/web_agent.py#L4922) | 4922 | `"        report[\"distinct_registrable_domains\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L004923](../../agents/web_agent.py#L4923) | 4923 | `"        report[\"independent_sources\"] = len(independent_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L004924](../../agents/web_agent.py#L4924) | 4924 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L004925](../../agents/web_agent.py#L4925) | 4925 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L004926](../../agents/web_agent.py#L4926) | 4926 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004927](../../agents/web_agent.py#L4927) | 4927 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L004928](../../agents/web_agent.py#L4928) | 4928 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L004929](../../agents/web_agent.py#L4929) | 4929 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004930](../../agents/web_agent.py#L4930) | 4930 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L004931](../../agents/web_agent.py#L4931) | 4931 | `"        if len(independent_domains) >= 2:"` | — |
| [SRC-1AE03B9EC3-L004932](../../agents/web_agent.py#L4932) | 4932 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004933](../../agents/web_agent.py#L4933) | 4933 | `"                \"تعدد النطاقات المسجلة لا يثبت الاستقلال التحريري؛ قد تنقل المواقع عن المصدر الأصلي نفسه.\""` | — |
| [SRC-1AE03B9EC3-L004934](../../agents/web_agent.py#L4934) | 4934 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004935](../../agents/web_agent.py#L4935) | 4935 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L004936](../../agents/web_agent.py#L4936) | 4936 | `"        if needs_corroboration and single_source_navigation and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L004937](../../agents/web_agent.py#L4937) | 4937 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004938](../../agents/web_agent.py#L4938) | 4938 | `"                \"هذه نتيجة مرشحة لطلب العثور على موقع/رابط؛ لم تُثبت رسميتها أو صحتها \""` | — |
| [SRC-1AE03B9EC3-L004939](../../agents/web_agent.py#L4939) | 4939 | `"                \"من مصدر مستقل، لذا راجع الرابط قبل الاعتماد عليه.\""` | — |
| [SRC-1AE03B9EC3-L004940](../../agents/web_agent.py#L4940) | 4940 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004941](../../agents/web_agent.py#L4941) | 4941 | `"        if needs_corroboration and (single_source_social or single_source_lead) and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L004942](../../agents/web_agent.py#L4942) | 4942 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004943](../../agents/web_agent.py#L4943) | 4943 | `"                \"هذه إشارات بحث أولية وليست تحققًا مستقلًا من هوية العميل أو نيته؛ \""` | — |
| [SRC-1AE03B9EC3-L004944](../../agents/web_agent.py#L4944) | 4944 | `"                \"راجع المنشور وتاريخه وسياقه قبل التواصل أو اتخاذ قرار.\""` | — |
| [SRC-1AE03B9EC3-L004945](../../agents/web_agent.py#L4945) | 4945 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004946](../../agents/web_agent.py#L4946) | 4946 | `"        if needs_corroboration and single_source_listing and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L004947](../../agents/web_agent.py#L4947) | 4947 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004948](../../agents/web_agent.py#L4948) | 4948 | `"                \"هذه إعلانات/قوائم مرشحة فقط. قد تكون منتهية أو غير دقيقة؛ تحقق من السعر \""` | — |
| [SRC-1AE03B9EC3-L004949](../../agents/web_agent.py#L4949) | 4949 | `"                \"والتوافر ومصدر الإعلان واطلب تأكيدًا حديثًا قبل دفع مال أو مشاركة بيانات.\""` | — |
| [SRC-1AE03B9EC3-L004950](../../agents/web_agent.py#L4950) | 4950 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004951](../../agents/web_agent.py#L4951) | 4951 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L004952](../../agents/web_agent.py#L4952) | 4952 | `"        if needs_corroboration and not task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L004953](../../agents/web_agent.py#L4953) | 4953 | `"            if search_outcome == \"unknown_after_research_error\":"` | — |
| [SRC-1AE03B9EC3-L004954](../../agents/web_agent.py#L4954) | 4954 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004955](../../agents/web_agent.py#L4955) | 4955 | `"                    \"تعذر إكمال مسار البحث بسبب خطأ، ولا توجد بيانات كافية لتحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L004956](../../agents/web_agent.py#L4956) | 4956 | `"                    \"كانت محاولة البحث قد اكتملت أو كم نتيجة جُمعت. لذلك لا أستطيع الجزم \""` | — |
| [SRC-1AE03B9EC3-L004957](../../agents/web_agent.py#L4957) | 4957 | `"                    \"بأن البحث لم يُنفّذ أو أن الإنترنت لم يُعد نتائج. لم أتمكن من تقديم \""` | — |
| [SRC-1AE03B9EC3-L004958](../../agents/web_agent.py#L4958) | 4958 | `"                    \"إجابة مكتملة؛ أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L004959](../../agents/web_agent.py#L4959) | 4959 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004960](../../agents/web_agent.py#L4960) | 4960 | `"            elif search_outcome == \"attempted_research_error\":"` | — |
| [SRC-1AE03B9EC3-L004961](../../agents/web_agent.py#L4961) | 4961 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004962](../../agents/web_agent.py#L4962) | 4962 | `"                    \"توجد قرائن تشغيلية على بدء محاولة بحث، لكن مسار البحث فشل قبل إنتاج \""` | — |
| [SRC-1AE03B9EC3-L004963](../../agents/web_agent.py#L4963) | 4963 | `"                    \"تقرير مكتمل. لا أستطيع تحديد عدد النتائج أو المصادر القابلة للاستخدام، \""` | — |
| [SRC-1AE03B9EC3-L004964](../../agents/web_agent.py#L4964) | 4964 | `"                    \"لذلك لن أخمّن. أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L004965](../../agents/web_agent.py#L4965) | 4965 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004966](../../agents/web_agent.py#L4966) | 4966 | `"            elif search_outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-1AE03B9EC3-L004967](../../agents/web_agent.py#L4967) | 4967 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004968](../../agents/web_agent.py#L4968) | 4968 | `"                    \"جرت محاولة البحث، لكن لم تتوفر مصادر صالحة وكافية للإجابة بعد تصفية \""` | — |
| [SRC-1AE03B9EC3-L004969](../../agents/web_agent.py#L4969) | 4969 | `"                    \"النتائج. هذا لا يثبت أن جميع المواقع أو الإنترنت غير متاح؛ لن أخمّن \""` | — |
| [SRC-1AE03B9EC3-L004970](../../agents/web_agent.py#L4970) | 4970 | `"                    \"أو أقدّم نتيجة غير مدعومة. جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L004971](../../agents/web_agent.py#L4971) | 4971 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004972](../../agents/web_agent.py#L4972) | 4972 | `"            elif search_outcome == \"not_attempted\":"` | — |
| [SRC-1AE03B9EC3-L004973](../../agents/web_agent.py#L4973) | 4973 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004974](../../agents/web_agent.py#L4974) | 4974 | `"                    \"لم تبدأ محاولة بحث ويب لهذا الطلب، لذلك لا تتوفر لدي أدلة ويب حالية \""` | — |
| [SRC-1AE03B9EC3-L004975](../../agents/web_agent.py#L4975) | 4975 | `"                    \"كافية للإجابة. لن أقدّم نتيجة غير مدعومة؛ أعد المحاولة أو اطلب بحثًا \""` | — |
| [SRC-1AE03B9EC3-L004976](../../agents/web_agent.py#L4976) | 4976 | `"                    \"صريحًا إذا كان ذلك مناسبًا.\""` | — |
| [SRC-1AE03B9EC3-L004977](../../agents/web_agent.py#L4977) | 4977 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004978](../../agents/web_agent.py#L4978) | 4978 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004979](../../agents/web_agent.py#L4979) | 4979 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004980](../../agents/web_agent.py#L4980) | 4980 | `"                    \"لم أجد معلومات موثوقة كافية مرتبطة بسؤالك من نطاقين مسجلين مختلفين على الأقل. \""` | — |
| [SRC-1AE03B9EC3-L004981](../../agents/web_agent.py#L4981) | 4981 | `"                    \"اختلاف النطاقات لا يثبت الاستقلال التحريري. لن أخمّن أو أقدّم نتيجة غير مدعومة؛ \""` | — |
| [SRC-1AE03B9EC3-L004982](../../agents/web_agent.py#L4982) | 4982 | `"                    \"جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L004983](../../agents/web_agent.py#L4983) | 4983 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004984](../../agents/web_agent.py#L4984) | 4984 | `"            public_sources = [{"` | — |
| [SRC-1AE03B9EC3-L004985](../../agents/web_agent.py#L4985) | 4985 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L004986](../../agents/web_agent.py#L4986) | 4986 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L004987](../../agents/web_agent.py#L4987) | 4987 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004988](../../agents/web_agent.py#L4988) | 4988 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L004989](../../agents/web_agent.py#L4989) | 4989 | `"                \"page_fetch_status\": source.get(\"page_fetch_status\", \"unknown\"),"` | — |
| [SRC-1AE03B9EC3-L004990](../../agents/web_agent.py#L4990) | 4990 | `"                \"page_fetch_error_class\": source.get(\"page_fetch_error_class\"),"` | — |
| [SRC-1AE03B9EC3-L004991](../../agents/web_agent.py#L4991) | 4991 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L004992](../../agents/web_agent.py#L4992) | 4992 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L004993](../../agents/web_agent.py#L4993) | 4993 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L004994](../../agents/web_agent.py#L4994) | 4994 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004995](../../agents/web_agent.py#L4995) | 4995 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L004996](../../agents/web_agent.py#L4996) | 4996 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004997](../../agents/web_agent.py#L4997) | 4997 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004998](../../agents/web_agent.py#L4998) | 4998 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004999](../../agents/web_agent.py#L4999) | 4999 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L005000](../../agents/web_agent.py#L5000) | 5000 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L005001](../../agents/web_agent.py#L5001) | 5001 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L005002](../../agents/web_agent.py#L5002) | 5002 | `"            } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L005003](../../agents/web_agent.py#L5003) | 5003 | `"            citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L005004](../../agents/web_agent.py#L5004) | 5004 | `"                reason, 0, [], \"not_run\""` | — |
| [SRC-1AE03B9EC3-L005005](../../agents/web_agent.py#L5005) | 5005 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005006](../../agents/web_agent.py#L5006) | 5006 | `"            citation_validation[\"status\"] = \"not_applicable_no_generated_answer\""` | — |
| [SRC-1AE03B9EC3-L005007](../../agents/web_agent.py#L5007) | 5007 | `"            coverage_targets = self._question_coverage_targets(working_question)"` | — |
| [SRC-1AE03B9EC3-L005008](../../agents/web_agent.py#L5008) | 5008 | `"            answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L005009](../../agents/web_agent.py#L5009) | 5009 | `"                \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L005010](../../agents/web_agent.py#L5010) | 5010 | `"                \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L005011](../../agents/web_agent.py#L5011) | 5011 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L005012](../../agents/web_agent.py#L5012) | 5012 | `"                    \"not_reviewed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L005013](../../agents/web_agent.py#L5013) | 5013 | `"                    if coverage_targets else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005014](../../agents/web_agent.py#L5014) | 5014 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005015](../../agents/web_agent.py#L5015) | 5015 | `"                \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L005016](../../agents/web_agent.py#L5016) | 5016 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005017](../../agents/web_agent.py#L5017) | 5017 | `"            answer_integrity = audit_answer_integrity(working_question, reason, sources, coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L005018](../../agents/web_agent.py#L5018) | 5018 | `"            answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005019](../../agents/web_agent.py#L5019) | 5019 | `"            answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L005020](../../agents/web_agent.py#L5020) | 5020 | `"            answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L005021](../../agents/web_agent.py#L5021) | 5021 | `"            answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L005022](../../agents/web_agent.py#L5022) | 5022 | `"            task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L005023](../../agents/web_agent.py#L5023) | 5023 | `"                \"not_assessed_insufficient_evidence\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005024](../../agents/web_agent.py#L5024) | 5024 | `"                else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005025](../../agents/web_agent.py#L5025) | 5025 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005026](../../agents/web_agent.py#L5026) | 5026 | `"            answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L005027](../../agents/web_agent.py#L5027) | 5027 | `"            research_failed = search_outcome in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L005028](../../agents/web_agent.py#L5028) | 5028 | `"            report.update({"` | — |
| [SRC-1AE03B9EC3-L005029](../../agents/web_agent.py#L5029) | 5029 | `"                # When collection failed, an empty local list is not evidence that"` | — |
| [SRC-1AE03B9EC3-L005030](../../agents/web_agent.py#L5030) | 5030 | `"                # the remote search returned zero sources; preserve unknown counts."` | — |
| [SRC-1AE03B9EC3-L005031](../../agents/web_agent.py#L5031) | 5031 | `"                \"unique_sources\": None if research_failed else len(sources),"` | — |
| [SRC-1AE03B9EC3-L005032](../../agents/web_agent.py#L5032) | 5032 | `"                \"independent_sources\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L005033](../../agents/web_agent.py#L5033) | 5033 | `"                \"distinct_registrable_domains\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L005034](../../agents/web_agent.py#L5034) | 5034 | `"                \"pages_fetched\": ("` | — |
| [SRC-1AE03B9EC3-L005035](../../agents/web_agent.py#L5035) | 5035 | `"                    None if research_failed"` | — |
| [SRC-1AE03B9EC3-L005036](../../agents/web_agent.py#L5036) | 5036 | `"                    else sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005037](../../agents/web_agent.py#L5037) | 5037 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005038](../../agents/web_agent.py#L5038) | 5038 | `"                \"provider_diagnostics\": current_research_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L005039](../../agents/web_agent.py#L5039) | 5039 | `"                \"insufficient_evidence\": True,"` | — |
| [SRC-1AE03B9EC3-L005040](../../agents/web_agent.py#L5040) | 5040 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L005041](../../agents/web_agent.py#L5041) | 5041 | `"                \"citation_check\": citation_validation[\"status\"],"` | — |
| [SRC-1AE03B9EC3-L005042](../../agents/web_agent.py#L5042) | 5042 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L005043](../../agents/web_agent.py#L5043) | 5043 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L005044](../../agents/web_agent.py#L5044) | 5044 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L005045](../../agents/web_agent.py#L5045) | 5045 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L005046](../../agents/web_agent.py#L5046) | 5046 | `"                \"connector_summary\": report.get(\"connector_summary\") or self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L005047](../../agents/web_agent.py#L5047) | 5047 | `"                    current_research_diagnostics, sources"` | — |
| [SRC-1AE03B9EC3-L005048](../../agents/web_agent.py#L5048) | 5048 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005049](../../agents/web_agent.py#L5049) | 5049 | `"            })"` | — |
| [SRC-1AE03B9EC3-L005050](../../agents/web_agent.py#L5050) | 5050 | `"            return {"` | — |
| [SRC-1AE03B9EC3-L005051](../../agents/web_agent.py#L5051) | 5051 | `"                \"answer\": reason,"` | — |
| [SRC-1AE03B9EC3-L005052](../../agents/web_agent.py#L5052) | 5052 | `"                \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L005053](../../agents/web_agent.py#L5053) | 5053 | `"                \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L005054](../../agents/web_agent.py#L5054) | 5054 | `"                \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005055](../../agents/web_agent.py#L5055) | 5055 | `"                \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L005056](../../agents/web_agent.py#L5056) | 5056 | `"                    \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L005057](../../agents/web_agent.py#L5057) | 5057 | `"                    \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L005058](../../agents/web_agent.py#L5058) | 5058 | `"                    \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L005059](../../agents/web_agent.py#L5059) | 5059 | `"                    \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L005060](../../agents/web_agent.py#L5060) | 5060 | `"                    \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L005061](../../agents/web_agent.py#L5061) | 5061 | `"                    \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L005062](../../agents/web_agent.py#L5062) | 5062 | `"                    \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L005063](../../agents/web_agent.py#L5063) | 5063 | `"                    \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L005064](../../agents/web_agent.py#L5064) | 5064 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005065](../../agents/web_agent.py#L5065) | 5065 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005066](../../agents/web_agent.py#L5066) | 5066 | `"                },"` | — |
| [SRC-1AE03B9EC3-L005067](../../agents/web_agent.py#L5067) | 5067 | `"                \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L005068](../../agents/web_agent.py#L5068) | 5068 | `"                \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L005069](../../agents/web_agent.py#L5069) | 5069 | `"                \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L005070](../../agents/web_agent.py#L5070) | 5070 | `"                \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L005071](../../agents/web_agent.py#L5071) | 5071 | `"                \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L005072](../../agents/web_agent.py#L5072) | 5072 | `"                \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L005073](../../agents/web_agent.py#L5073) | 5073 | `"                \"warnings\": list(dict.fromkeys(search_warnings + [reason])),"` | — |
| [SRC-1AE03B9EC3-L005074](../../agents/web_agent.py#L5074) | 5074 | `"                \"kind\": \"insufficient_evidence\","` | — |
| [SRC-1AE03B9EC3-L005075](../../agents/web_agent.py#L5075) | 5075 | `"                \"final_answer_status\": \"insufficient_evidence_no_generation\","` | — |
| [SRC-1AE03B9EC3-L005076](../../agents/web_agent.py#L5076) | 5076 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005077](../../agents/web_agent.py#L5077) | 5077 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005078](../../agents/web_agent.py#L5078) | 5078 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L005079](../../agents/web_agent.py#L5079) | 5079 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L005080](../../agents/web_agent.py#L5080) | 5080 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L005081](../../agents/web_agent.py#L5081) | 5081 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L005082](../../agents/web_agent.py#L5082) | 5082 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L005083](../../agents/web_agent.py#L5083) | 5083 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005084](../../agents/web_agent.py#L5084) | 5084 | `""` | — |
| [SRC-1AE03B9EC3-L005085](../../agents/web_agent.py#L5085) | 5085 | `"        answer = \"\""` | — |
| [SRC-1AE03B9EC3-L005086](../../agents/web_agent.py#L5086) | 5086 | `"        used_llm = False"` | — |
| [SRC-1AE03B9EC3-L005087](../../agents/web_agent.py#L5087) | 5087 | `"        llm_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005088](../../agents/web_agent.py#L5088) | 5088 | `"        generation_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L005089](../../agents/web_agent.py#L5089) | 5089 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L005090](../../agents/web_agent.py#L5090) | 5090 | `"            answer = self._generate("` | — |
| [SRC-1AE03B9EC3-L005091](../../agents/web_agent.py#L5091) | 5091 | `"                working_question,"` | — |
| [SRC-1AE03B9EC3-L005092](../../agents/web_agent.py#L5092) | 5092 | `"                clean_history,"` | — |
| [SRC-1AE03B9EC3-L005093](../../agents/web_agent.py#L5093) | 5093 | `"                sources,"` | — |
| [SRC-1AE03B9EC3-L005094](../../agents/web_agent.py#L5094) | 5094 | `"                search_warning,"` | — |
| [SRC-1AE03B9EC3-L005095](../../agents/web_agent.py#L5095) | 5095 | `"                research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L005096](../../agents/web_agent.py#L5096) | 5096 | `"                search_report=report,"` | — |
| [SRC-1AE03B9EC3-L005097](../../agents/web_agent.py#L5097) | 5097 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005098](../../agents/web_agent.py#L5098) | 5098 | `"            used_llm = True"` | — |
| [SRC-1AE03B9EC3-L005099](../../agents/web_agent.py#L5099) | 5099 | `"            if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L005100](../../agents/web_agent.py#L5100) | 5100 | `"                existing_urls = {item.get(\"url\") for item in sources}"` | — |
| [SRC-1AE03B9EC3-L005101](../../agents/web_agent.py#L5101) | 5101 | `"                relevance_queries = []"` | — |
| [SRC-1AE03B9EC3-L005102](../../agents/web_agent.py#L5102) | 5102 | `"                planned_queries = plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005103](../../agents/web_agent.py#L5103) | 5103 | `"                if not isinstance(planned_queries, list):"` | — |
| [SRC-1AE03B9EC3-L005104](../../agents/web_agent.py#L5104) | 5104 | `"                    planned_queries = []"` | — |
| [SRC-1AE03B9EC3-L005105](../../agents/web_agent.py#L5105) | 5105 | `"                for candidate_query in [working_question, *planned_queries]:"` | — |
| [SRC-1AE03B9EC3-L005106](../../agents/web_agent.py#L5106) | 5106 | `"                    if not isinstance(candidate_query, str):"` | — |
| [SRC-1AE03B9EC3-L005107](../../agents/web_agent.py#L5107) | 5107 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L005108](../../agents/web_agent.py#L5108) | 5108 | `"                    compacted_query = compact_search_query(candidate_query)"` | — |
| [SRC-1AE03B9EC3-L005109](../../agents/web_agent.py#L5109) | 5109 | `"                    if compacted_query and compacted_query not in relevance_queries:"` | — |
| [SRC-1AE03B9EC3-L005110](../../agents/web_agent.py#L5110) | 5110 | `"                        relevance_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L005111](../../agents/web_agent.py#L5111) | 5111 | `"                for item in self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L005112](../../agents/web_agent.py#L5112) | 5112 | `"                    source_text = \" \".join(("` | — |
| [SRC-1AE03B9EC3-L005113](../../agents/web_agent.py#L5113) | 5113 | `"                        item.get(\"title\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005114](../../agents/web_agent.py#L5114) | 5114 | `"                        item.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005115](../../agents/web_agent.py#L5115) | 5115 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L005116](../../agents/web_agent.py#L5116) | 5116 | `"                    if ("` | — |
| [SRC-1AE03B9EC3-L005117](../../agents/web_agent.py#L5117) | 5117 | `"                        relevance_queries"` | — |
| [SRC-1AE03B9EC3-L005118](../../agents/web_agent.py#L5118) | 5118 | `"                        and item[\"url\"] not in existing_urls"` | — |
| [SRC-1AE03B9EC3-L005119](../../agents/web_agent.py#L5119) | 5119 | `"                        and not _blocked_source_url(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L005120](../../agents/web_agent.py#L5120) | 5120 | `"                        and any("` | — |
| [SRC-1AE03B9EC3-L005121](../../agents/web_agent.py#L5121) | 5121 | `"                            _relevance_ratio(candidate_query, source_text) >= 0.20"` | — |
| [SRC-1AE03B9EC3-L005122](../../agents/web_agent.py#L5122) | 5122 | `"                            for candidate_query in relevance_queries"` | — |
| [SRC-1AE03B9EC3-L005123](../../agents/web_agent.py#L5123) | 5123 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005124](../../agents/web_agent.py#L5124) | 5124 | `"                    ):"` | — |
| [SRC-1AE03B9EC3-L005125](../../agents/web_agent.py#L5125) | 5125 | `"                        sources.append(item)"` | — |
| [SRC-1AE03B9EC3-L005126](../../agents/web_agent.py#L5126) | 5126 | `"                        existing_urls.add(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L005127](../../agents/web_agent.py#L5127) | 5127 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005128](../../agents/web_agent.py#L5128) | 5128 | `"                provider_counts = dict(report.get(\"provider_counts\", {}))"` | — |
| [SRC-1AE03B9EC3-L005129](../../agents/web_agent.py#L5129) | 5129 | `"                provider_counts[\"openrouter_web_search\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L005130](../../agents/web_agent.py#L5130) | 5130 | `"                report[\"provider_counts\"] = provider_counts"` | — |
| [SRC-1AE03B9EC3-L005131](../../agents/web_agent.py#L5131) | 5131 | `"                providers_used = list(report.get(\"providers_used\", []))"` | — |
| [SRC-1AE03B9EC3-L005132](../../agents/web_agent.py#L5132) | 5132 | `"                if \"openrouter_web_search\" not in providers_used:"` | — |
| [SRC-1AE03B9EC3-L005133](../../agents/web_agent.py#L5133) | 5133 | `"                    providers_used.append(\"openrouter_web_search\")"` | — |
| [SRC-1AE03B9EC3-L005134](../../agents/web_agent.py#L5134) | 5134 | `"                report[\"providers_used\"] = providers_used"` | — |
| [SRC-1AE03B9EC3-L005135](../../agents/web_agent.py#L5135) | 5135 | `"                report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L005136](../../agents/web_agent.py#L5136) | 5136 | `"                    sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L005137](../../agents/web_agent.py#L5137) | 5137 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005138](../../agents/web_agent.py#L5138) | 5138 | `"        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005139](../../agents/web_agent.py#L5139) | 5139 | `"            llm_warning = str(exc)"` | — |
| [SRC-1AE03B9EC3-L005140](../../agents/web_agent.py#L5140) | 5140 | `"            generation_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L005141](../../agents/web_agent.py#L5141) | 5141 | `"            if generation_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L005142](../../agents/web_agent.py#L5142) | 5142 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005143](../../agents/web_agent.py#L5143) | 5143 | `"                    \"استُنفدت ميزانية محاولات النماذج قبل اكتمال الإجابة التحليلية. \""` | — |
| [SRC-1AE03B9EC3-L005144](../../agents/web_agent.py#L5144) | 5144 | `"                    \"أعرض مقتطفات المصادر المتاحة فقط، ولا أعتبر المهمة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L005145](../../agents/web_agent.py#L5145) | 5145 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005146](../../agents/web_agent.py#L5146) | 5146 | `"            elif not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L005147](../../agents/web_agent.py#L5147) | 5147 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005148](../../agents/web_agent.py#L5148) | 5148 | `"                    \"تم البحث، لكن الفهم التوليدي غير مفعّل بعد. اضبط OPENROUTER_API_KEY \""` | — |
| [SRC-1AE03B9EC3-L005149](../../agents/web_agent.py#L5149) | 5149 | `"                    \"في Termux لتفعيل تخطيط البحث والإجابة باللغة الطبيعية.\""` | — |
| [SRC-1AE03B9EC3-L005150](../../agents/web_agent.py#L5150) | 5150 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005151](../../agents/web_agent.py#L5151) | 5151 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005152](../../agents/web_agent.py#L5152) | 5152 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005153](../../agents/web_agent.py#L5153) | 5153 | `"                    \"اكتمل البحث، لكن تعذر توليد إجابة تحليلية. أعرض لك مقتطفات المصادر \""` | — |
| [SRC-1AE03B9EC3-L005154](../../agents/web_agent.py#L5154) | 5154 | `"                    \"المتاحة بدلًا من اختلاق إجابة.\""` | — |
| [SRC-1AE03B9EC3-L005155](../../agents/web_agent.py#L5155) | 5155 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005156](../../agents/web_agent.py#L5156) | 5156 | `"            answer = _fallback_answer(sources, reason)"` | — |
| [SRC-1AE03B9EC3-L005157](../../agents/web_agent.py#L5157) | 5157 | `""` | — |
| [SRC-1AE03B9EC3-L005158](../../agents/web_agent.py#L5158) | 5158 | `"        coverage_targets = self._question_coverage_targets(working_question)"` | — |
| [SRC-1AE03B9EC3-L005159](../../agents/web_agent.py#L5159) | 5159 | `"        coverage_repair_status = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L005160](../../agents/web_agent.py#L5160) | 5160 | `"        coverage_repair_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005161](../../agents/web_agent.py#L5161) | 5161 | `"        review_status = \"not_run\""` | — |
| [SRC-1AE03B9EC3-L005162](../../agents/web_agent.py#L5162) | 5162 | `"        review_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005163](../../agents/web_agent.py#L5163) | 5163 | `"        review_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L005164](../../agents/web_agent.py#L5164) | 5164 | `"        if used_llm and sources:"` | — |
| [SRC-1AE03B9EC3-L005165](../../agents/web_agent.py#L5165) | 5165 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L005166](../../agents/web_agent.py#L5166) | 5166 | `"                answer = self._review_answer(working_question, answer, sources[:MAX_LLM_CITED_SOURCES])"` | — |
| [SRC-1AE03B9EC3-L005167](../../agents/web_agent.py#L5167) | 5167 | `"                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005168](../../agents/web_agent.py#L5168) | 5168 | `"            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005169](../../agents/web_agent.py#L5169) | 5169 | `"                review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005170](../../agents/web_agent.py#L5170) | 5170 | `"                review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L005171](../../agents/web_agent.py#L5171) | 5171 | `"                review_warning = ("` | — |
| [SRC-1AE03B9EC3-L005172](../../agents/web_agent.py#L5172) | 5172 | `"                    \"استُنفدت ميزانية النماذج قبل اكتمال تدقيق الإجابة؛ لذلك لن أعرض المسودة \""` | — |
| [SRC-1AE03B9EC3-L005173](../../agents/web_agent.py#L5173) | 5173 | `"                    \"بوصفها إجابة مكتملة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد عليها.\""` | — |
| [SRC-1AE03B9EC3-L005174](../../agents/web_agent.py#L5174) | 5174 | `"                    if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L005175](../../agents/web_agent.py#L5175) | 5175 | `"                    else"` | — |
| [SRC-1AE03B9EC3-L005176](../../agents/web_agent.py#L5176) | 5176 | `"                    \"تعذر تدقيق الادعاءات مقابل نصوص المصادر؛ لذلك لن أتعامل مع المسودة \""` | — |
| [SRC-1AE03B9EC3-L005177](../../agents/web_agent.py#L5177) | 5177 | `"                    \"كإجابة مؤكدة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد على المسودة.\""` | — |
| [SRC-1AE03B9EC3-L005178](../../agents/web_agent.py#L5178) | 5178 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005179](../../agents/web_agent.py#L5179) | 5179 | `"                answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L005180](../../agents/web_agent.py#L5180) | 5180 | `"        criterion_gap_research: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L005181](../../agents/web_agent.py#L5181) | 5181 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L005182](../../agents/web_agent.py#L5182) | 5182 | `"            \"status\": \"not_needed\","` | — |
| [SRC-1AE03B9EC3-L005183](../../agents/web_agent.py#L5183) | 5183 | `"            \"targets\": [],"` | — |
| [SRC-1AE03B9EC3-L005184](../../agents/web_agent.py#L5184) | 5184 | `"            \"new_sources_added\": 0,"` | — |
| [SRC-1AE03B9EC3-L005185](../../agents/web_agent.py#L5185) | 5185 | `"            \"evidence_sources_enriched\": 0,"` | — |
| [SRC-1AE03B9EC3-L005186](../../agents/web_agent.py#L5186) | 5186 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005187](../../agents/web_agent.py#L5187) | 5187 | `"        # Close the loop from an answer-stage gap back to the source layer. A criterion"` | — |
| [SRC-1AE03B9EC3-L005188](../../agents/web_agent.py#L5188) | 5188 | `"        # that appears in the draft but has no source signal triggers one bounded query"` | — |
| [SRC-1AE03B9EC3-L005189](../../agents/web_agent.py#L5189) | 5189 | `"        # when the reserved request-budget slot remains available."` | — |
| [SRC-1AE03B9EC3-L005190](../../agents/web_agent.py#L5190) | 5190 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L005191](../../agents/web_agent.py#L5191) | 5191 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005192](../../agents/web_agent.py#L5192) | 5192 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005193](../../agents/web_agent.py#L5193) | 5193 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L005194](../../agents/web_agent.py#L5194) | 5194 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L005195](../../agents/web_agent.py#L5195) | 5195 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L005196](../../agents/web_agent.py#L5196) | 5196 | `"            presearch_integrity = audit_answer_integrity("` | — |
| [SRC-1AE03B9EC3-L005197](../../agents/web_agent.py#L5197) | 5197 | `"                working_question, answer, sources, coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005198](../../agents/web_agent.py#L5198) | 5198 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005199](../../agents/web_agent.py#L5199) | 5199 | `"            source_gap_targets = ["` | — |
| [SRC-1AE03B9EC3-L005200](../../agents/web_agent.py#L5200) | 5200 | `"                item[\"target\"]"` | — |
| [SRC-1AE03B9EC3-L005201](../../agents/web_agent.py#L5201) | 5201 | `"                for item in presearch_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005202](../../agents/web_agent.py#L5202) | 5202 | `"                if item.get(\"source_evidence_status\") == \"no_source_lexical_signal\""` | — |
| [SRC-1AE03B9EC3-L005203](../../agents/web_agent.py#L5203) | 5203 | `"            ][:3]"` | — |
| [SRC-1AE03B9EC3-L005204](../../agents/web_agent.py#L5204) | 5204 | `"            if source_gap_targets:"` | — |
| [SRC-1AE03B9EC3-L005205](../../agents/web_agent.py#L5205) | 5205 | `"                criterion_gap_research[\"targets\"] = source_gap_targets"` | — |
| [SRC-1AE03B9EC3-L005206](../../agents/web_agent.py#L5206) | 5206 | `"                budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L005207](../../agents/web_agent.py#L5207) | 5207 | `"                if not plan.get(\"coverage_gap_repair_slot_reserved\"):"` | — |
| [SRC-1AE03B9EC3-L005208](../../agents/web_agent.py#L5208) | 5208 | `"                    criterion_gap_research[\"status\"] = \"skipped_no_reserved_search_slot\""` | — |
| [SRC-1AE03B9EC3-L005209](../../agents/web_agent.py#L5209) | 5209 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005210](../../agents/web_agent.py#L5210) | 5210 | `"                        \"رُصدت محاور بلا إشارة لفظية في المصادر، لكن لم تُحجز ميزانية \""` | — |
| [SRC-1AE03B9EC3-L005211](../../agents/web_agent.py#L5211) | 5211 | `"                        \"استعلام إضافي لهذه المهمة؛ لذلك ستظل المحاور غير المحسومة ظاهرة.\""` | — |
| [SRC-1AE03B9EC3-L005212](../../agents/web_agent.py#L5212) | 5212 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005213](../../agents/web_agent.py#L5213) | 5213 | `"                elif budget is None:"` | — |
| [SRC-1AE03B9EC3-L005214](../../agents/web_agent.py#L5214) | 5214 | `"                    criterion_gap_research[\"status\"] = \"skipped_no_request_budget\""` | — |
