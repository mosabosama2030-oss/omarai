# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **014**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L005411 إلى SRC-1AE03B9EC3-L006210
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L005411](../../agents/web_agent.py#L5411) | 5411 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005412](../../agents/web_agent.py#L5412) | 5412 | `"        final_independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L005413](../../agents/web_agent.py#L5413) | 5413 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L005414](../../agents/web_agent.py#L5414) | 5414 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L005415](../../agents/web_agent.py#L5415) | 5415 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L005416](../../agents/web_agent.py#L5416) | 5416 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L005417](../../agents/web_agent.py#L5417) | 5417 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005418](../../agents/web_agent.py#L5418) | 5418 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005419](../../agents/web_agent.py#L5419) | 5419 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005420](../../agents/web_agent.py#L5420) | 5420 | `"        final_independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L005421](../../agents/web_agent.py#L5421) | 5421 | `"        # All post-filter source metrics describe the sources that remain eligible"` | — |
| [SRC-1AE03B9EC3-L005422](../../agents/web_agent.py#L5422) | 5422 | `"        # for the answer. Connector-level received/accepted/rejected totals remain"` | — |
| [SRC-1AE03B9EC3-L005423](../../agents/web_agent.py#L5423) | 5423 | `"        # available in provider diagnostics and are intentionally separate."` | — |
| [SRC-1AE03B9EC3-L005424](../../agents/web_agent.py#L5424) | 5424 | `"        independent_domains = final_independent_domains"` | — |
| [SRC-1AE03B9EC3-L005425](../../agents/web_agent.py#L5425) | 5425 | `"        report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005426](../../agents/web_agent.py#L5426) | 5426 | `"        report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005427](../../agents/web_agent.py#L5427) | 5427 | `"        report[\"distinct_registrable_domains\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L005428](../../agents/web_agent.py#L5428) | 5428 | `"        report[\"independent_sources\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L005429](../../agents/web_agent.py#L5429) | 5429 | `"        report[\"providers_used\"] = sorted({"` | — |
| [SRC-1AE03B9EC3-L005430](../../agents/web_agent.py#L5430) | 5430 | `"            str(provider)"` | — |
| [SRC-1AE03B9EC3-L005431](../../agents/web_agent.py#L5431) | 5431 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005432](../../agents/web_agent.py#L5432) | 5432 | `"            for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L005433](../../agents/web_agent.py#L5433) | 5433 | `"            if provider"` | — |
| [SRC-1AE03B9EC3-L005434](../../agents/web_agent.py#L5434) | 5434 | `"        })"` | — |
| [SRC-1AE03B9EC3-L005435](../../agents/web_agent.py#L5435) | 5435 | `"        report[\"provider_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L005436](../../agents/web_agent.py#L5436) | 5436 | `"            provider: sum(provider in source.get(\"providers\", []) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005437](../../agents/web_agent.py#L5437) | 5437 | `"            for provider in report[\"providers_used\"]"` | — |
| [SRC-1AE03B9EC3-L005438](../../agents/web_agent.py#L5438) | 5438 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005439](../../agents/web_agent.py#L5439) | 5439 | `"        report[\"platform_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L005440](../../agents/web_agent.py#L5440) | 5440 | `"            str(source.get(\"platform\", \"web\")): sum("` | — |
| [SRC-1AE03B9EC3-L005441](../../agents/web_agent.py#L5441) | 5441 | `"                str(other.get(\"platform\", \"web\")) == str(source.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L005442](../../agents/web_agent.py#L5442) | 5442 | `"                for other in sources"` | — |
| [SRC-1AE03B9EC3-L005443](../../agents/web_agent.py#L5443) | 5443 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005444](../../agents/web_agent.py#L5444) | 5444 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L005445](../../agents/web_agent.py#L5445) | 5445 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005446](../../agents/web_agent.py#L5446) | 5446 | `"        report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L005447](../../agents/web_agent.py#L5447) | 5447 | `"            sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L005448](../../agents/web_agent.py#L5448) | 5448 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005449](../../agents/web_agent.py#L5449) | 5449 | `"        needs_corroboration = ("` | — |
| [SRC-1AE03B9EC3-L005450](../../agents/web_agent.py#L5450) | 5450 | `"            len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L005451](../../agents/web_agent.py#L5451) | 5451 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005452](../../agents/web_agent.py#L5452) | 5452 | `"        report[\"evidence_repair\"] = evidence_repair"` | — |
| [SRC-1AE03B9EC3-L005453](../../agents/web_agent.py#L5453) | 5453 | `"        baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L005454](../../agents/web_agent.py#L5454) | 5454 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L005455](../../agents/web_agent.py#L5455) | 5455 | `"            current_research_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L005456](../../agents/web_agent.py#L5456) | 5456 | `"                item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L005457](../../agents/web_agent.py#L5457) | 5457 | `"                if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L005458](../../agents/web_agent.py#L5458) | 5458 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L005459](../../agents/web_agent.py#L5459) | 5459 | `"        report[\"provider_diagnostics\"] = current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L005460](../../agents/web_agent.py#L5460) | 5460 | `"        provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L005461](../../agents/web_agent.py#L5461) | 5461 | `"            item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L005462](../../agents/web_agent.py#L5462) | 5462 | `"            for item in current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L005463](../../agents/web_agent.py#L5463) | 5463 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005464](../../agents/web_agent.py#L5464) | 5464 | `"        raw_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L005465](../../agents/web_agent.py#L5465) | 5465 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L005466](../../agents/web_agent.py#L5466) | 5466 | `"            queries_attempted = ("` | — |
| [SRC-1AE03B9EC3-L005467](../../agents/web_agent.py#L5467) | 5467 | `"                None if raw_attempt_count is None"` | — |
| [SRC-1AE03B9EC3-L005468](../../agents/web_agent.py#L5468) | 5468 | `"                else max(0, int(raw_attempt_count or 0))"` | — |
| [SRC-1AE03B9EC3-L005469](../../agents/web_agent.py#L5469) | 5469 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005470](../../agents/web_agent.py#L5470) | 5470 | `"        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L005471](../../agents/web_agent.py#L5471) | 5471 | `"            queries_attempted = None"` | — |
| [SRC-1AE03B9EC3-L005472](../../agents/web_agent.py#L5472) | 5472 | `"        if queries_attempted is not None:"` | — |
| [SRC-1AE03B9EC3-L005473](../../agents/web_agent.py#L5473) | 5473 | `"            search_attempted = ("` | — |
| [SRC-1AE03B9EC3-L005474](../../agents/web_agent.py#L5474) | 5474 | `"                queries_attempted > 0"` | — |
| [SRC-1AE03B9EC3-L005475](../../agents/web_agent.py#L5475) | 5475 | `"                or provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L005476](../../agents/web_agent.py#L5476) | 5476 | `"                or report.get(\"search_attempted\") is True"` | — |
| [SRC-1AE03B9EC3-L005477](../../agents/web_agent.py#L5477) | 5477 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005478](../../agents/web_agent.py#L5478) | 5478 | `"        elif provider_attempt_observed or report.get(\"search_attempted\") is True:"` | — |
| [SRC-1AE03B9EC3-L005479](../../agents/web_agent.py#L5479) | 5479 | `"            search_attempted = True"` | — |
| [SRC-1AE03B9EC3-L005480](../../agents/web_agent.py#L5480) | 5480 | `"        elif isinstance(report.get(\"search_attempted\"), bool):"` | — |
| [SRC-1AE03B9EC3-L005481](../../agents/web_agent.py#L5481) | 5481 | `"            search_attempted = report[\"search_attempted\"]"` | — |
| [SRC-1AE03B9EC3-L005482](../../agents/web_agent.py#L5482) | 5482 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005483](../../agents/web_agent.py#L5483) | 5483 | `"            search_attempted = None"` | — |
| [SRC-1AE03B9EC3-L005484](../../agents/web_agent.py#L5484) | 5484 | `"        report[\"queries_attempted\"] = queries_attempted"` | — |
| [SRC-1AE03B9EC3-L005485](../../agents/web_agent.py#L5485) | 5485 | `"        report[\"queries_attempted_known\"] = queries_attempted is not None"` | — |
| [SRC-1AE03B9EC3-L005486](../../agents/web_agent.py#L5486) | 5486 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L005487](../../agents/web_agent.py#L5487) | 5487 | `"        previous_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L005488](../../agents/web_agent.py#L5488) | 5488 | `"        if previous_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L005489](../../agents/web_agent.py#L5489) | 5489 | `"            if provider_attempt_observed or search_attempted is True:"` | — |
| [SRC-1AE03B9EC3-L005490](../../agents/web_agent.py#L5490) | 5490 | `"                search_outcome = \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L005491](../../agents/web_agent.py#L5491) | 5491 | `"            elif search_attempted is False:"` | — |
| [SRC-1AE03B9EC3-L005492](../../agents/web_agent.py#L5492) | 5492 | `"                search_outcome = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L005493](../../agents/web_agent.py#L5493) | 5493 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005494](../../agents/web_agent.py#L5494) | 5494 | `"                search_outcome = \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L005495](../../agents/web_agent.py#L5495) | 5495 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005496](../../agents/web_agent.py#L5496) | 5496 | `"            search_outcome = ("` | — |
| [SRC-1AE03B9EC3-L005497](../../agents/web_agent.py#L5497) | 5497 | `"                \"attempted_with_usable_sources\" if search_attempted is True and sources"` | — |
| [SRC-1AE03B9EC3-L005498](../../agents/web_agent.py#L5498) | 5498 | `"                else \"attempted_no_usable_sources\" if search_attempted is True"` | — |
| [SRC-1AE03B9EC3-L005499](../../agents/web_agent.py#L5499) | 5499 | `"                else \"not_attempted\" if search_attempted is False"` | — |
| [SRC-1AE03B9EC3-L005500](../../agents/web_agent.py#L5500) | 5500 | `"                else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L005501](../../agents/web_agent.py#L5501) | 5501 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005502](../../agents/web_agent.py#L5502) | 5502 | `"        report[\"search_outcome\"] = search_outcome"` | — |
| [SRC-1AE03B9EC3-L005503](../../agents/web_agent.py#L5503) | 5503 | `"        if search_outcome in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L005504](../../agents/web_agent.py#L5504) | 5504 | `"            report[\"usable_sources_after_filtering\"] = None"` | — |
| [SRC-1AE03B9EC3-L005505](../../agents/web_agent.py#L5505) | 5505 | `"            report[\"unique_sources\"] = None"` | — |
| [SRC-1AE03B9EC3-L005506](../../agents/web_agent.py#L5506) | 5506 | `"            report[\"pages_fetched\"] = None"` | — |
| [SRC-1AE03B9EC3-L005507](../../agents/web_agent.py#L5507) | 5507 | `"            report[\"provider_counts\"] = None"` | — |
| [SRC-1AE03B9EC3-L005508](../../agents/web_agent.py#L5508) | 5508 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L005509](../../agents/web_agent.py#L5509) | 5509 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005510](../../agents/web_agent.py#L5510) | 5510 | `"            if report.get(\"unique_sources\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L005511](../../agents/web_agent.py#L5511) | 5511 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005512](../../agents/web_agent.py#L5512) | 5512 | `"            if report.get(\"pages_fetched\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L005513](../../agents/web_agent.py#L5513) | 5513 | `"                report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005514](../../agents/web_agent.py#L5514) | 5514 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L005515](../../agents/web_agent.py#L5515) | 5515 | `"        report[\"distinct_registrable_domains\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L005516](../../agents/web_agent.py#L5516) | 5516 | `"        report[\"independent_sources\"] = len(independent_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L005517](../../agents/web_agent.py#L5517) | 5517 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005518](../../agents/web_agent.py#L5518) | 5518 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L005519](../../agents/web_agent.py#L5519) | 5519 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005520](../../agents/web_agent.py#L5520) | 5520 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L005521](../../agents/web_agent.py#L5521) | 5521 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L005522](../../agents/web_agent.py#L5522) | 5522 | `"        )"` | — |
| [SRC-1AE03B9EC3-L005523](../../agents/web_agent.py#L5523) | 5523 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L005524](../../agents/web_agent.py#L5524) | 5524 | `"        if len(independent_domains) >= 2:"` | — |
| [SRC-1AE03B9EC3-L005525](../../agents/web_agent.py#L5525) | 5525 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005526](../../agents/web_agent.py#L5526) | 5526 | `"                \"تعدد النطاقات المسجلة لا يثبت الاستقلال التحريري؛ قد تنقل المواقع عن المصدر الأصلي نفسه.\""` | — |
| [SRC-1AE03B9EC3-L005527](../../agents/web_agent.py#L5527) | 5527 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005528](../../agents/web_agent.py#L5528) | 5528 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L005529](../../agents/web_agent.py#L5529) | 5529 | `"        if needs_corroboration and single_source_navigation and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005530](../../agents/web_agent.py#L5530) | 5530 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005531](../../agents/web_agent.py#L5531) | 5531 | `"                \"هذه نتيجة مرشحة لطلب العثور على موقع/رابط؛ لم تُثبت رسميتها أو صحتها \""` | — |
| [SRC-1AE03B9EC3-L005532](../../agents/web_agent.py#L5532) | 5532 | `"                \"من مصدر مستقل، لذا راجع الرابط قبل الاعتماد عليه.\""` | — |
| [SRC-1AE03B9EC3-L005533](../../agents/web_agent.py#L5533) | 5533 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005534](../../agents/web_agent.py#L5534) | 5534 | `"        if needs_corroboration and (single_source_social or single_source_lead) and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005535](../../agents/web_agent.py#L5535) | 5535 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005536](../../agents/web_agent.py#L5536) | 5536 | `"                \"هذه إشارات بحث أولية وليست تحققًا مستقلًا من هوية العميل أو نيته؛ \""` | — |
| [SRC-1AE03B9EC3-L005537](../../agents/web_agent.py#L5537) | 5537 | `"                \"راجع المنشور وتاريخه وسياقه قبل التواصل أو اتخاذ قرار.\""` | — |
| [SRC-1AE03B9EC3-L005538](../../agents/web_agent.py#L5538) | 5538 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005539](../../agents/web_agent.py#L5539) | 5539 | `"        if needs_corroboration and single_source_listing and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L005540](../../agents/web_agent.py#L5540) | 5540 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005541](../../agents/web_agent.py#L5541) | 5541 | `"                \"هذه إعلانات/قوائم مرشحة فقط. قد تكون منتهية أو غير دقيقة؛ تحقق من السعر \""` | — |
| [SRC-1AE03B9EC3-L005542](../../agents/web_agent.py#L5542) | 5542 | `"                \"والتوافر ومصدر الإعلان واطلب تأكيدًا حديثًا قبل دفع مال أو مشاركة بيانات.\""` | — |
| [SRC-1AE03B9EC3-L005543](../../agents/web_agent.py#L5543) | 5543 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005544](../../agents/web_agent.py#L5544) | 5544 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L005545](../../agents/web_agent.py#L5545) | 5545 | `"        if needs_corroboration and not task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L005546](../../agents/web_agent.py#L5546) | 5546 | `"            if search_outcome == \"unknown_after_research_error\":"` | — |
| [SRC-1AE03B9EC3-L005547](../../agents/web_agent.py#L5547) | 5547 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005548](../../agents/web_agent.py#L5548) | 5548 | `"                    \"تعذر إكمال مسار البحث بسبب خطأ، ولا توجد بيانات كافية لتحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L005549](../../agents/web_agent.py#L5549) | 5549 | `"                    \"كانت محاولة البحث قد اكتملت أو كم نتيجة جُمعت. لذلك لا أستطيع الجزم \""` | — |
| [SRC-1AE03B9EC3-L005550](../../agents/web_agent.py#L5550) | 5550 | `"                    \"بأن البحث لم يُنفّذ أو أن الإنترنت لم يُعد نتائج. لم أتمكن من تقديم \""` | — |
| [SRC-1AE03B9EC3-L005551](../../agents/web_agent.py#L5551) | 5551 | `"                    \"إجابة مكتملة؛ أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005552](../../agents/web_agent.py#L5552) | 5552 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005553](../../agents/web_agent.py#L5553) | 5553 | `"            elif search_outcome == \"attempted_research_error\":"` | — |
| [SRC-1AE03B9EC3-L005554](../../agents/web_agent.py#L5554) | 5554 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005555](../../agents/web_agent.py#L5555) | 5555 | `"                    \"توجد قرائن تشغيلية على بدء محاولة بحث، لكن مسار البحث فشل قبل إنتاج \""` | — |
| [SRC-1AE03B9EC3-L005556](../../agents/web_agent.py#L5556) | 5556 | `"                    \"تقرير مكتمل. لا أستطيع تحديد عدد النتائج أو المصادر القابلة للاستخدام، \""` | — |
| [SRC-1AE03B9EC3-L005557](../../agents/web_agent.py#L5557) | 5557 | `"                    \"لذلك لن أخمّن. أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005558](../../agents/web_agent.py#L5558) | 5558 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005559](../../agents/web_agent.py#L5559) | 5559 | `"            elif search_outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-1AE03B9EC3-L005560](../../agents/web_agent.py#L5560) | 5560 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005561](../../agents/web_agent.py#L5561) | 5561 | `"                    \"جرت محاولة البحث، لكن لم تتوفر مصادر صالحة وكافية للإجابة بعد تصفية \""` | — |
| [SRC-1AE03B9EC3-L005562](../../agents/web_agent.py#L5562) | 5562 | `"                    \"النتائج. هذا لا يثبت أن جميع المواقع أو الإنترنت غير متاح؛ لن أخمّن \""` | — |
| [SRC-1AE03B9EC3-L005563](../../agents/web_agent.py#L5563) | 5563 | `"                    \"أو أقدّم نتيجة غير مدعومة. جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005564](../../agents/web_agent.py#L5564) | 5564 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005565](../../agents/web_agent.py#L5565) | 5565 | `"            elif search_outcome == \"not_attempted\":"` | — |
| [SRC-1AE03B9EC3-L005566](../../agents/web_agent.py#L5566) | 5566 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005567](../../agents/web_agent.py#L5567) | 5567 | `"                    \"لم تبدأ محاولة بحث ويب لهذا الطلب، لذلك لا تتوفر لدي أدلة ويب حالية \""` | — |
| [SRC-1AE03B9EC3-L005568](../../agents/web_agent.py#L5568) | 5568 | `"                    \"كافية للإجابة. لن أقدّم نتيجة غير مدعومة؛ أعد المحاولة أو اطلب بحثًا \""` | — |
| [SRC-1AE03B9EC3-L005569](../../agents/web_agent.py#L5569) | 5569 | `"                    \"صريحًا إذا كان ذلك مناسبًا.\""` | — |
| [SRC-1AE03B9EC3-L005570](../../agents/web_agent.py#L5570) | 5570 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005571](../../agents/web_agent.py#L5571) | 5571 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005572](../../agents/web_agent.py#L5572) | 5572 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005573](../../agents/web_agent.py#L5573) | 5573 | `"                    \"لم أجد معلومات موثوقة كافية مرتبطة بسؤالك من نطاقين مسجلين مختلفين على الأقل. \""` | — |
| [SRC-1AE03B9EC3-L005574](../../agents/web_agent.py#L5574) | 5574 | `"                    \"اختلاف النطاقات لا يثبت الاستقلال التحريري. لن أخمّن أو أقدّم نتيجة غير مدعومة؛ \""` | — |
| [SRC-1AE03B9EC3-L005575](../../agents/web_agent.py#L5575) | 5575 | `"                    \"جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L005576](../../agents/web_agent.py#L5576) | 5576 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005577](../../agents/web_agent.py#L5577) | 5577 | `"            public_sources = [{"` | — |
| [SRC-1AE03B9EC3-L005578](../../agents/web_agent.py#L5578) | 5578 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L005579](../../agents/web_agent.py#L5579) | 5579 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L005580](../../agents/web_agent.py#L5580) | 5580 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005581](../../agents/web_agent.py#L5581) | 5581 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L005582](../../agents/web_agent.py#L5582) | 5582 | `"                \"page_fetch_status\": source.get(\"page_fetch_status\", \"unknown\"),"` | — |
| [SRC-1AE03B9EC3-L005583](../../agents/web_agent.py#L5583) | 5583 | `"                \"page_fetch_error_class\": source.get(\"page_fetch_error_class\"),"` | — |
| [SRC-1AE03B9EC3-L005584](../../agents/web_agent.py#L5584) | 5584 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L005585](../../agents/web_agent.py#L5585) | 5585 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005586](../../agents/web_agent.py#L5586) | 5586 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L005587](../../agents/web_agent.py#L5587) | 5587 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005588](../../agents/web_agent.py#L5588) | 5588 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L005589](../../agents/web_agent.py#L5589) | 5589 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005590](../../agents/web_agent.py#L5590) | 5590 | `"                \"opinion_source_classification\": source.get(\"opinion_source_classification\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005591](../../agents/web_agent.py#L5591) | 5591 | `"                \"opinion_classification_basis\": source.get(\"opinion_classification_basis\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005592](../../agents/web_agent.py#L5592) | 5592 | `"                \"opinion_classification_method\": source.get(\"opinion_classification_method\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005593](../../agents/web_agent.py#L5593) | 5593 | `"                \"current_evidence_assessment\": source.get(\"current_evidence_assessment\", {}),"` | — |
| [SRC-1AE03B9EC3-L005594](../../agents/web_agent.py#L5594) | 5594 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005595](../../agents/web_agent.py#L5595) | 5595 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005596](../../agents/web_agent.py#L5596) | 5596 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L005597](../../agents/web_agent.py#L5597) | 5597 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L005598](../../agents/web_agent.py#L5598) | 5598 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L005599](../../agents/web_agent.py#L5599) | 5599 | `"            } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L005600](../../agents/web_agent.py#L5600) | 5600 | `"            citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L005601](../../agents/web_agent.py#L5601) | 5601 | `"                reason, 0, [], \"not_run\""` | — |
| [SRC-1AE03B9EC3-L005602](../../agents/web_agent.py#L5602) | 5602 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005603](../../agents/web_agent.py#L5603) | 5603 | `"            citation_validation[\"status\"] = \"not_applicable_no_generated_answer\""` | — |
| [SRC-1AE03B9EC3-L005604](../../agents/web_agent.py#L5604) | 5604 | `"            coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L005605](../../agents/web_agent.py#L5605) | 5605 | `"            answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L005606](../../agents/web_agent.py#L5606) | 5606 | `"                \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L005607](../../agents/web_agent.py#L5607) | 5607 | `"                \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L005608](../../agents/web_agent.py#L5608) | 5608 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L005609](../../agents/web_agent.py#L5609) | 5609 | `"                    \"not_reviewed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L005610](../../agents/web_agent.py#L5610) | 5610 | `"                    if coverage_targets else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005611](../../agents/web_agent.py#L5611) | 5611 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005612](../../agents/web_agent.py#L5612) | 5612 | `"                \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L005613](../../agents/web_agent.py#L5613) | 5613 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005614](../../agents/web_agent.py#L5614) | 5614 | `"            answer_integrity = audit_answer_integrity(working_question, reason, sources, coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L005615](../../agents/web_agent.py#L5615) | 5615 | `"            answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005616](../../agents/web_agent.py#L5616) | 5616 | `"            answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L005617](../../agents/web_agent.py#L5617) | 5617 | `"            answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L005618](../../agents/web_agent.py#L5618) | 5618 | `"            answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L005619](../../agents/web_agent.py#L5619) | 5619 | `"            task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L005620](../../agents/web_agent.py#L5620) | 5620 | `"                \"not_assessed_insufficient_evidence\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005621](../../agents/web_agent.py#L5621) | 5621 | `"                else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L005622](../../agents/web_agent.py#L5622) | 5622 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005623](../../agents/web_agent.py#L5623) | 5623 | `"            answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L005624](../../agents/web_agent.py#L5624) | 5624 | `"            research_failed = search_outcome in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L005625](../../agents/web_agent.py#L5625) | 5625 | `"            report.update({"` | — |
| [SRC-1AE03B9EC3-L005626](../../agents/web_agent.py#L5626) | 5626 | `"                # When collection failed, an empty local list is not evidence that"` | — |
| [SRC-1AE03B9EC3-L005627](../../agents/web_agent.py#L5627) | 5627 | `"                # the remote search returned zero sources; preserve unknown counts."` | — |
| [SRC-1AE03B9EC3-L005628](../../agents/web_agent.py#L5628) | 5628 | `"                \"unique_sources\": None if research_failed else len(sources),"` | — |
| [SRC-1AE03B9EC3-L005629](../../agents/web_agent.py#L5629) | 5629 | `"                \"independent_sources\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L005630](../../agents/web_agent.py#L5630) | 5630 | `"                \"distinct_registrable_domains\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L005631](../../agents/web_agent.py#L5631) | 5631 | `"                \"pages_fetched\": ("` | — |
| [SRC-1AE03B9EC3-L005632](../../agents/web_agent.py#L5632) | 5632 | `"                    None if research_failed"` | — |
| [SRC-1AE03B9EC3-L005633](../../agents/web_agent.py#L5633) | 5633 | `"                    else sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L005634](../../agents/web_agent.py#L5634) | 5634 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005635](../../agents/web_agent.py#L5635) | 5635 | `"                \"provider_diagnostics\": current_research_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L005636](../../agents/web_agent.py#L5636) | 5636 | `"                \"insufficient_evidence\": True,"` | — |
| [SRC-1AE03B9EC3-L005637](../../agents/web_agent.py#L5637) | 5637 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L005638](../../agents/web_agent.py#L5638) | 5638 | `"                \"citation_check\": citation_validation[\"status\"],"` | — |
| [SRC-1AE03B9EC3-L005639](../../agents/web_agent.py#L5639) | 5639 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L005640](../../agents/web_agent.py#L5640) | 5640 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L005641](../../agents/web_agent.py#L5641) | 5641 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L005642](../../agents/web_agent.py#L5642) | 5642 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L005643](../../agents/web_agent.py#L5643) | 5643 | `"                \"connector_summary\": report.get(\"connector_summary\") or self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L005644](../../agents/web_agent.py#L5644) | 5644 | `"                    current_research_diagnostics, sources"` | — |
| [SRC-1AE03B9EC3-L005645](../../agents/web_agent.py#L5645) | 5645 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L005646](../../agents/web_agent.py#L5646) | 5646 | `"            })"` | — |
| [SRC-1AE03B9EC3-L005647](../../agents/web_agent.py#L5647) | 5647 | `"            return {"` | — |
| [SRC-1AE03B9EC3-L005648](../../agents/web_agent.py#L5648) | 5648 | `"                \"answer\": reason,"` | — |
| [SRC-1AE03B9EC3-L005649](../../agents/web_agent.py#L5649) | 5649 | `"                \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L005650](../../agents/web_agent.py#L5650) | 5650 | `"                \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L005651](../../agents/web_agent.py#L5651) | 5651 | `"                \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L005652](../../agents/web_agent.py#L5652) | 5652 | `"                \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L005653](../../agents/web_agent.py#L5653) | 5653 | `"                    \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L005654](../../agents/web_agent.py#L5654) | 5654 | `"                    \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L005655](../../agents/web_agent.py#L5655) | 5655 | `"                    \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L005656](../../agents/web_agent.py#L5656) | 5656 | `"                    \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L005657](../../agents/web_agent.py#L5657) | 5657 | `"                    \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L005658](../../agents/web_agent.py#L5658) | 5658 | `"                    \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L005659](../../agents/web_agent.py#L5659) | 5659 | `"                    \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L005660](../../agents/web_agent.py#L5660) | 5660 | `"                    \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L005661](../../agents/web_agent.py#L5661) | 5661 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005662](../../agents/web_agent.py#L5662) | 5662 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005663](../../agents/web_agent.py#L5663) | 5663 | `"                },"` | — |
| [SRC-1AE03B9EC3-L005664](../../agents/web_agent.py#L5664) | 5664 | `"                \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L005665](../../agents/web_agent.py#L5665) | 5665 | `"                \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L005666](../../agents/web_agent.py#L5666) | 5666 | `"                \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L005667](../../agents/web_agent.py#L5667) | 5667 | `"                \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L005668](../../agents/web_agent.py#L5668) | 5668 | `"                \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L005669](../../agents/web_agent.py#L5669) | 5669 | `"                \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L005670](../../agents/web_agent.py#L5670) | 5670 | `"                \"warnings\": list(dict.fromkeys(search_warnings + [reason])),"` | — |
| [SRC-1AE03B9EC3-L005671](../../agents/web_agent.py#L5671) | 5671 | `"                \"kind\": \"insufficient_evidence\","` | — |
| [SRC-1AE03B9EC3-L005672](../../agents/web_agent.py#L5672) | 5672 | `"                \"final_answer_status\": \"insufficient_evidence_no_generation\","` | — |
| [SRC-1AE03B9EC3-L005673](../../agents/web_agent.py#L5673) | 5673 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L005674](../../agents/web_agent.py#L5674) | 5674 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L005675](../../agents/web_agent.py#L5675) | 5675 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L005676](../../agents/web_agent.py#L5676) | 5676 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L005677](../../agents/web_agent.py#L5677) | 5677 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L005678](../../agents/web_agent.py#L5678) | 5678 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L005679](../../agents/web_agent.py#L5679) | 5679 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L005680](../../agents/web_agent.py#L5680) | 5680 | `"            }"` | — |
| [SRC-1AE03B9EC3-L005681](../../agents/web_agent.py#L5681) | 5681 | `""` | — |
| [SRC-1AE03B9EC3-L005682](../../agents/web_agent.py#L5682) | 5682 | `"        answer = \"\""` | — |
| [SRC-1AE03B9EC3-L005683](../../agents/web_agent.py#L5683) | 5683 | `"        used_llm = False"` | — |
| [SRC-1AE03B9EC3-L005684](../../agents/web_agent.py#L5684) | 5684 | `"        llm_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005685](../../agents/web_agent.py#L5685) | 5685 | `"        generation_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L005686](../../agents/web_agent.py#L5686) | 5686 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L005687](../../agents/web_agent.py#L5687) | 5687 | `"            answer = self._generate("` | — |
| [SRC-1AE03B9EC3-L005688](../../agents/web_agent.py#L5688) | 5688 | `"                working_question,"` | — |
| [SRC-1AE03B9EC3-L005689](../../agents/web_agent.py#L5689) | 5689 | `"                clean_history,"` | — |
| [SRC-1AE03B9EC3-L005690](../../agents/web_agent.py#L5690) | 5690 | `"                sources,"` | — |
| [SRC-1AE03B9EC3-L005691](../../agents/web_agent.py#L5691) | 5691 | `"                search_warning,"` | — |
| [SRC-1AE03B9EC3-L005692](../../agents/web_agent.py#L5692) | 5692 | `"                research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L005693](../../agents/web_agent.py#L5693) | 5693 | `"                search_report=report,"` | — |
| [SRC-1AE03B9EC3-L005694](../../agents/web_agent.py#L5694) | 5694 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005695](../../agents/web_agent.py#L5695) | 5695 | `"            used_llm = True"` | — |
| [SRC-1AE03B9EC3-L005696](../../agents/web_agent.py#L5696) | 5696 | `"            if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L005697](../../agents/web_agent.py#L5697) | 5697 | `"                existing_urls = {item.get(\"url\") for item in sources}"` | — |
| [SRC-1AE03B9EC3-L005698](../../agents/web_agent.py#L5698) | 5698 | `"                relevance_queries = []"` | — |
| [SRC-1AE03B9EC3-L005699](../../agents/web_agent.py#L5699) | 5699 | `"                planned_queries = plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005700](../../agents/web_agent.py#L5700) | 5700 | `"                if not isinstance(planned_queries, list):"` | — |
| [SRC-1AE03B9EC3-L005701](../../agents/web_agent.py#L5701) | 5701 | `"                    planned_queries = []"` | — |
| [SRC-1AE03B9EC3-L005702](../../agents/web_agent.py#L5702) | 5702 | `"                for candidate_query in [working_question, *planned_queries]:"` | — |
| [SRC-1AE03B9EC3-L005703](../../agents/web_agent.py#L5703) | 5703 | `"                    if not isinstance(candidate_query, str):"` | — |
| [SRC-1AE03B9EC3-L005704](../../agents/web_agent.py#L5704) | 5704 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L005705](../../agents/web_agent.py#L5705) | 5705 | `"                    compacted_query = compact_search_query(candidate_query)"` | — |
| [SRC-1AE03B9EC3-L005706](../../agents/web_agent.py#L5706) | 5706 | `"                    if compacted_query and compacted_query not in relevance_queries:"` | — |
| [SRC-1AE03B9EC3-L005707](../../agents/web_agent.py#L5707) | 5707 | `"                        relevance_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L005708](../../agents/web_agent.py#L5708) | 5708 | `"                for item in self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L005709](../../agents/web_agent.py#L5709) | 5709 | `"                    source_text = \" \".join(("` | — |
| [SRC-1AE03B9EC3-L005710](../../agents/web_agent.py#L5710) | 5710 | `"                        item.get(\"title\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005711](../../agents/web_agent.py#L5711) | 5711 | `"                        item.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L005712](../../agents/web_agent.py#L5712) | 5712 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L005713](../../agents/web_agent.py#L5713) | 5713 | `"                    if ("` | — |
| [SRC-1AE03B9EC3-L005714](../../agents/web_agent.py#L5714) | 5714 | `"                        relevance_queries"` | — |
| [SRC-1AE03B9EC3-L005715](../../agents/web_agent.py#L5715) | 5715 | `"                        and item[\"url\"] not in existing_urls"` | — |
| [SRC-1AE03B9EC3-L005716](../../agents/web_agent.py#L5716) | 5716 | `"                        and not _blocked_source_url(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L005717](../../agents/web_agent.py#L5717) | 5717 | `"                        and any("` | — |
| [SRC-1AE03B9EC3-L005718](../../agents/web_agent.py#L5718) | 5718 | `"                            _relevance_ratio(candidate_query, source_text) >= 0.20"` | — |
| [SRC-1AE03B9EC3-L005719](../../agents/web_agent.py#L5719) | 5719 | `"                            for candidate_query in relevance_queries"` | — |
| [SRC-1AE03B9EC3-L005720](../../agents/web_agent.py#L5720) | 5720 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005721](../../agents/web_agent.py#L5721) | 5721 | `"                    ):"` | — |
| [SRC-1AE03B9EC3-L005722](../../agents/web_agent.py#L5722) | 5722 | `"                        sources.append(item)"` | — |
| [SRC-1AE03B9EC3-L005723](../../agents/web_agent.py#L5723) | 5723 | `"                        existing_urls.add(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L005724](../../agents/web_agent.py#L5724) | 5724 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005725](../../agents/web_agent.py#L5725) | 5725 | `"                provider_counts = dict(report.get(\"provider_counts\", {}))"` | — |
| [SRC-1AE03B9EC3-L005726](../../agents/web_agent.py#L5726) | 5726 | `"                provider_counts[\"openrouter_web_search\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L005727](../../agents/web_agent.py#L5727) | 5727 | `"                report[\"provider_counts\"] = provider_counts"` | — |
| [SRC-1AE03B9EC3-L005728](../../agents/web_agent.py#L5728) | 5728 | `"                providers_used = list(report.get(\"providers_used\", []))"` | — |
| [SRC-1AE03B9EC3-L005729](../../agents/web_agent.py#L5729) | 5729 | `"                if \"openrouter_web_search\" not in providers_used:"` | — |
| [SRC-1AE03B9EC3-L005730](../../agents/web_agent.py#L5730) | 5730 | `"                    providers_used.append(\"openrouter_web_search\")"` | — |
| [SRC-1AE03B9EC3-L005731](../../agents/web_agent.py#L5731) | 5731 | `"                report[\"providers_used\"] = providers_used"` | — |
| [SRC-1AE03B9EC3-L005732](../../agents/web_agent.py#L5732) | 5732 | `"                report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L005733](../../agents/web_agent.py#L5733) | 5733 | `"                    sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L005734](../../agents/web_agent.py#L5734) | 5734 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005735](../../agents/web_agent.py#L5735) | 5735 | `"        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005736](../../agents/web_agent.py#L5736) | 5736 | `"            llm_warning = str(exc)"` | — |
| [SRC-1AE03B9EC3-L005737](../../agents/web_agent.py#L5737) | 5737 | `"            generation_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L005738](../../agents/web_agent.py#L5738) | 5738 | `"            if generation_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L005739](../../agents/web_agent.py#L5739) | 5739 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005740](../../agents/web_agent.py#L5740) | 5740 | `"                    \"استُنفدت ميزانية محاولات النماذج قبل اكتمال الإجابة التحليلية. \""` | — |
| [SRC-1AE03B9EC3-L005741](../../agents/web_agent.py#L5741) | 5741 | `"                    \"أعرض مقتطفات المصادر المتاحة فقط، ولا أعتبر المهمة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L005742](../../agents/web_agent.py#L5742) | 5742 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005743](../../agents/web_agent.py#L5743) | 5743 | `"            elif not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L005744](../../agents/web_agent.py#L5744) | 5744 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005745](../../agents/web_agent.py#L5745) | 5745 | `"                    \"تم البحث، لكن الفهم التوليدي غير مفعّل بعد. اضبط OPENROUTER_API_KEY \""` | — |
| [SRC-1AE03B9EC3-L005746](../../agents/web_agent.py#L5746) | 5746 | `"                    \"في Termux لتفعيل تخطيط البحث والإجابة باللغة الطبيعية.\""` | — |
| [SRC-1AE03B9EC3-L005747](../../agents/web_agent.py#L5747) | 5747 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005748](../../agents/web_agent.py#L5748) | 5748 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L005749](../../agents/web_agent.py#L5749) | 5749 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L005750](../../agents/web_agent.py#L5750) | 5750 | `"                    \"اكتمل البحث، لكن تعذر توليد إجابة تحليلية. أعرض لك مقتطفات المصادر \""` | — |
| [SRC-1AE03B9EC3-L005751](../../agents/web_agent.py#L5751) | 5751 | `"                    \"المتاحة بدلًا من اختلاق إجابة.\""` | — |
| [SRC-1AE03B9EC3-L005752](../../agents/web_agent.py#L5752) | 5752 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005753](../../agents/web_agent.py#L5753) | 5753 | `"            answer = _fallback_answer(sources, reason)"` | — |
| [SRC-1AE03B9EC3-L005754](../../agents/web_agent.py#L5754) | 5754 | `""` | — |
| [SRC-1AE03B9EC3-L005755](../../agents/web_agent.py#L5755) | 5755 | `"        coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L005756](../../agents/web_agent.py#L5756) | 5756 | `"        coverage_repair_status = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L005757](../../agents/web_agent.py#L5757) | 5757 | `"        coverage_repair_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005758](../../agents/web_agent.py#L5758) | 5758 | `"        review_status = \"not_run\""` | — |
| [SRC-1AE03B9EC3-L005759](../../agents/web_agent.py#L5759) | 5759 | `"        review_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L005760](../../agents/web_agent.py#L5760) | 5760 | `"        review_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L005761](../../agents/web_agent.py#L5761) | 5761 | `"        if used_llm and sources:"` | — |
| [SRC-1AE03B9EC3-L005762](../../agents/web_agent.py#L5762) | 5762 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L005763](../../agents/web_agent.py#L5763) | 5763 | `"                answer = self._review_answer(working_question, answer, sources[:MAX_LLM_CITED_SOURCES])"` | — |
| [SRC-1AE03B9EC3-L005764](../../agents/web_agent.py#L5764) | 5764 | `"                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005765](../../agents/web_agent.py#L5765) | 5765 | `"            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005766](../../agents/web_agent.py#L5766) | 5766 | `"                review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005767](../../agents/web_agent.py#L5767) | 5767 | `"                review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L005768](../../agents/web_agent.py#L5768) | 5768 | `"                review_warning = ("` | — |
| [SRC-1AE03B9EC3-L005769](../../agents/web_agent.py#L5769) | 5769 | `"                    \"استُنفدت ميزانية النماذج قبل اكتمال تدقيق الإجابة؛ لذلك لن أعرض المسودة \""` | — |
| [SRC-1AE03B9EC3-L005770](../../agents/web_agent.py#L5770) | 5770 | `"                    \"بوصفها إجابة مكتملة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد عليها.\""` | — |
| [SRC-1AE03B9EC3-L005771](../../agents/web_agent.py#L5771) | 5771 | `"                    if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L005772](../../agents/web_agent.py#L5772) | 5772 | `"                    else"` | — |
| [SRC-1AE03B9EC3-L005773](../../agents/web_agent.py#L5773) | 5773 | `"                    \"تعذر تدقيق الادعاءات مقابل نصوص المصادر؛ لذلك لن أتعامل مع المسودة \""` | — |
| [SRC-1AE03B9EC3-L005774](../../agents/web_agent.py#L5774) | 5774 | `"                    \"كإجابة مؤكدة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد على المسودة.\""` | — |
| [SRC-1AE03B9EC3-L005775](../../agents/web_agent.py#L5775) | 5775 | `"                )"` | — |
| [SRC-1AE03B9EC3-L005776](../../agents/web_agent.py#L5776) | 5776 | `"                answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L005777](../../agents/web_agent.py#L5777) | 5777 | `"        criterion_gap_research: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L005778](../../agents/web_agent.py#L5778) | 5778 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L005779](../../agents/web_agent.py#L5779) | 5779 | `"            \"status\": \"not_needed\","` | — |
| [SRC-1AE03B9EC3-L005780](../../agents/web_agent.py#L5780) | 5780 | `"            \"targets\": [],"` | — |
| [SRC-1AE03B9EC3-L005781](../../agents/web_agent.py#L5781) | 5781 | `"            \"new_sources_added\": 0,"` | — |
| [SRC-1AE03B9EC3-L005782](../../agents/web_agent.py#L5782) | 5782 | `"            \"evidence_sources_enriched\": 0,"` | — |
| [SRC-1AE03B9EC3-L005783](../../agents/web_agent.py#L5783) | 5783 | `"        }"` | — |
| [SRC-1AE03B9EC3-L005784](../../agents/web_agent.py#L5784) | 5784 | `"        # Close the loop from an answer-stage gap back to the source layer. A criterion"` | — |
| [SRC-1AE03B9EC3-L005785](../../agents/web_agent.py#L5785) | 5785 | `"        # that appears in the draft but has no source signal triggers one bounded query"` | — |
| [SRC-1AE03B9EC3-L005786](../../agents/web_agent.py#L5786) | 5786 | `"        # when the reserved request-budget slot remains available."` | — |
| [SRC-1AE03B9EC3-L005787](../../agents/web_agent.py#L5787) | 5787 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L005788](../../agents/web_agent.py#L5788) | 5788 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005789](../../agents/web_agent.py#L5789) | 5789 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005790](../../agents/web_agent.py#L5790) | 5790 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L005791](../../agents/web_agent.py#L5791) | 5791 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L005792](../../agents/web_agent.py#L5792) | 5792 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L005793](../../agents/web_agent.py#L5793) | 5793 | `"            presearch_integrity = audit_answer_integrity("` | — |
| [SRC-1AE03B9EC3-L005794](../../agents/web_agent.py#L5794) | 5794 | `"                working_question, answer, sources, coverage_targets"` | — |
| [SRC-1AE03B9EC3-L005795](../../agents/web_agent.py#L5795) | 5795 | `"            )"` | — |
| [SRC-1AE03B9EC3-L005796](../../agents/web_agent.py#L5796) | 5796 | `"            source_gap_targets = ["` | — |
| [SRC-1AE03B9EC3-L005797](../../agents/web_agent.py#L5797) | 5797 | `"                item[\"target\"]"` | — |
| [SRC-1AE03B9EC3-L005798](../../agents/web_agent.py#L5798) | 5798 | `"                for item in presearch_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L005799](../../agents/web_agent.py#L5799) | 5799 | `"                if item.get(\"source_evidence_status\") == \"no_source_lexical_signal\""` | — |
| [SRC-1AE03B9EC3-L005800](../../agents/web_agent.py#L5800) | 5800 | `"            ][:3]"` | — |
| [SRC-1AE03B9EC3-L005801](../../agents/web_agent.py#L5801) | 5801 | `"            if source_gap_targets:"` | — |
| [SRC-1AE03B9EC3-L005802](../../agents/web_agent.py#L5802) | 5802 | `"                criterion_gap_research[\"targets\"] = source_gap_targets"` | — |
| [SRC-1AE03B9EC3-L005803](../../agents/web_agent.py#L5803) | 5803 | `"                budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L005804](../../agents/web_agent.py#L5804) | 5804 | `"                if not plan.get(\"coverage_gap_repair_slot_reserved\"):"` | — |
| [SRC-1AE03B9EC3-L005805](../../agents/web_agent.py#L5805) | 5805 | `"                    criterion_gap_research[\"status\"] = \"skipped_no_reserved_search_slot\""` | — |
| [SRC-1AE03B9EC3-L005806](../../agents/web_agent.py#L5806) | 5806 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005807](../../agents/web_agent.py#L5807) | 5807 | `"                        \"رُصدت محاور بلا إشارة لفظية في المصادر، لكن لم تُحجز ميزانية \""` | — |
| [SRC-1AE03B9EC3-L005808](../../agents/web_agent.py#L5808) | 5808 | `"                        \"استعلام إضافي لهذه المهمة؛ لذلك ستظل المحاور غير المحسومة ظاهرة.\""` | — |
| [SRC-1AE03B9EC3-L005809](../../agents/web_agent.py#L5809) | 5809 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005810](../../agents/web_agent.py#L5810) | 5810 | `"                elif budget is None:"` | — |
| [SRC-1AE03B9EC3-L005811](../../agents/web_agent.py#L5811) | 5811 | `"                    criterion_gap_research[\"status\"] = \"skipped_no_request_budget\""` | — |
| [SRC-1AE03B9EC3-L005812](../../agents/web_agent.py#L5812) | 5812 | `"                elif budget.remaining_units(\"search_queries\") < 1:"` | — |
| [SRC-1AE03B9EC3-L005813](../../agents/web_agent.py#L5813) | 5813 | `"                    criterion_gap_research[\"status\"] = \"skipped_search_budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L005814](../../agents/web_agent.py#L5814) | 5814 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005815](../../agents/web_agent.py#L5815) | 5815 | `"                        \"رُصدت محاور بلا إشارة لفظية في المصادر، لكن ميزانية البحث لم تترك \""` | — |
| [SRC-1AE03B9EC3-L005816](../../agents/web_agent.py#L5816) | 5816 | `"                        \"استعلامًا إضافيًا للتحقق منها؛ لذلك لا تُعدّ الإجابة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L005817](../../agents/web_agent.py#L5817) | 5817 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005818](../../agents/web_agent.py#L5818) | 5818 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L005819](../../agents/web_agent.py#L5819) | 5819 | `"                    fallback_queries = fallback_plan(working_question, clean_history).get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005820](../../agents/web_agent.py#L5820) | 5820 | `"                    topic_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L005821](../../agents/web_agent.py#L5821) | 5821 | `"                        fallback_queries[0] if fallback_queries else working_question"` | — |
| [SRC-1AE03B9EC3-L005822](../../agents/web_agent.py#L5822) | 5822 | `"                    ) or compact_search_query(working_question)"` | — |
| [SRC-1AE03B9EC3-L005823](../../agents/web_agent.py#L5823) | 5823 | `"                    gap_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L005824](../../agents/web_agent.py#L5824) | 5824 | `"                        f\"{topic_query} {' '.join(source_gap_targets)} official specific evidence data\""` | — |
| [SRC-1AE03B9EC3-L005825](../../agents/web_agent.py#L5825) | 5825 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L005826](../../agents/web_agent.py#L5826) | 5826 | `"                    known_query_keys = {"` | — |
| [SRC-1AE03B9EC3-L005827](../../agents/web_agent.py#L5827) | 5827 | `"                        _normalize_search_query(item).casefold()"` | — |
| [SRC-1AE03B9EC3-L005828](../../agents/web_agent.py#L5828) | 5828 | `"                        for item in plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L005829](../../agents/web_agent.py#L5829) | 5829 | `"                        if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L005830](../../agents/web_agent.py#L5830) | 5830 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L005831](../../agents/web_agent.py#L5831) | 5831 | `"                    if not gap_query or not _relevance_query_tokens(gap_query):"` | — |
| [SRC-1AE03B9EC3-L005832](../../agents/web_agent.py#L5832) | 5832 | `"                        criterion_gap_research[\"status\"] = \"skipped_no_valid_query\""` | — |
| [SRC-1AE03B9EC3-L005833](../../agents/web_agent.py#L5833) | 5833 | `"                    elif _normalize_search_query(gap_query).casefold() in known_query_keys:"` | — |
| [SRC-1AE03B9EC3-L005834](../../agents/web_agent.py#L5834) | 5834 | `"                        criterion_gap_research[\"status\"] = \"skipped_query_not_distinct\""` | — |
| [SRC-1AE03B9EC3-L005835](../../agents/web_agent.py#L5835) | 5835 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L005836](../../agents/web_agent.py#L5836) | 5836 | `"                        criterion_gap_research.update({"` | — |
| [SRC-1AE03B9EC3-L005837](../../agents/web_agent.py#L5837) | 5837 | `"                            \"attempted\": True,"` | — |
| [SRC-1AE03B9EC3-L005838](../../agents/web_agent.py#L5838) | 5838 | `"                            \"status\": \"searching_for_missing_criterion_evidence\","` | — |
| [SRC-1AE03B9EC3-L005839](../../agents/web_agent.py#L5839) | 5839 | `"                            \"query\": gap_query,"` | — |
| [SRC-1AE03B9EC3-L005840](../../agents/web_agent.py#L5840) | 5840 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L005841](../../agents/web_agent.py#L5841) | 5841 | `"                        gap_plan = dict(plan)"` | — |
| [SRC-1AE03B9EC3-L005842](../../agents/web_agent.py#L5842) | 5842 | `"                        gap_plan.update({"` | — |
| [SRC-1AE03B9EC3-L005843](../../agents/web_agent.py#L5843) | 5843 | `"                            \"queries\": [gap_query],"` | — |
| [SRC-1AE03B9EC3-L005844](../../agents/web_agent.py#L5844) | 5844 | `"                            \"query_limit\": 1,"` | — |
| [SRC-1AE03B9EC3-L005845](../../agents/web_agent.py#L5845) | 5845 | `"                            \"depth\": \"standard\","` | — |
| [SRC-1AE03B9EC3-L005846](../../agents/web_agent.py#L5846) | 5846 | `"                            \"social_focus\": False,"` | — |
| [SRC-1AE03B9EC3-L005847](../../agents/web_agent.py#L5847) | 5847 | `"                            \"platforms\": [],"` | — |
| [SRC-1AE03B9EC3-L005848](../../agents/web_agent.py#L5848) | 5848 | `"                            \"direct_urls\": [],"` | — |
| [SRC-1AE03B9EC3-L005849](../../agents/web_agent.py#L5849) | 5849 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L005850](../../agents/web_agent.py#L5850) | 5850 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L005851](../../agents/web_agent.py#L5851) | 5851 | `"                            gap_sources, gap_warnings, gap_report = self._collect_research(gap_plan)"` | — |
| [SRC-1AE03B9EC3-L005852](../../agents/web_agent.py#L5852) | 5852 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L005853](../../agents/web_agent.py#L5853) | 5853 | `"                            gap_sources, gap_warnings = [], []"` | — |
| [SRC-1AE03B9EC3-L005854](../../agents/web_agent.py#L5854) | 5854 | `"                            gap_report = {"` | — |
| [SRC-1AE03B9EC3-L005855](../../agents/web_agent.py#L5855) | 5855 | `"                                \"queries_planned\": 1,"` | — |
| [SRC-1AE03B9EC3-L005856](../../agents/web_agent.py#L5856) | 5856 | `"                                \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L005857](../../agents/web_agent.py#L5857) | 5857 | `"                                \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L005858](../../agents/web_agent.py#L5858) | 5858 | `"                                \"search_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L005859](../../agents/web_agent.py#L5859) | 5859 | `"                                \"search_outcome\": \"unknown_after_research_error\","` | — |
| [SRC-1AE03B9EC3-L005860](../../agents/web_agent.py#L5860) | 5860 | `"                                \"query_results\": [],"` | — |
| [SRC-1AE03B9EC3-L005861](../../agents/web_agent.py#L5861) | 5861 | `"                            }"` | — |
| [SRC-1AE03B9EC3-L005862](../../agents/web_agent.py#L5862) | 5862 | `"                            criterion_gap_research[\"status\"] = \"search_failed\""` | — |
| [SRC-1AE03B9EC3-L005863](../../agents/web_agent.py#L5863) | 5863 | `"                            criterion_gap_research[\"error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L005864](../../agents/web_agent.py#L5864) | 5864 | `"                        search_warnings.extend("` | — |
| [SRC-1AE03B9EC3-L005865](../../agents/web_agent.py#L5865) | 5865 | `"                            item for item in gap_warnings if isinstance(item, str)"` | — |
| [SRC-1AE03B9EC3-L005866](../../agents/web_agent.py#L5866) | 5866 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005867](../../agents/web_agent.py#L5867) | 5867 | `"                        source_indexes: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L005868](../../agents/web_agent.py#L5868) | 5868 | `"                        for source_index, source in enumerate(sources):"` | — |
| [SRC-1AE03B9EC3-L005869](../../agents/web_agent.py#L5869) | 5869 | `"                            source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L005870](../../agents/web_agent.py#L5870) | 5870 | `"                            if source_key:"` | — |
| [SRC-1AE03B9EC3-L005871](../../agents/web_agent.py#L5871) | 5871 | `"                                source_indexes.setdefault(source_key, source_index)"` | — |
| [SRC-1AE03B9EC3-L005872](../../agents/web_agent.py#L5872) | 5872 | `"                        # A criterion-gap search is a second retrieval path, not a"` | — |
| [SRC-1AE03B9EC3-L005873](../../agents/web_agent.py#L5873) | 5873 | `"                        # trusted bypass. Apply the same task-specific source policy before"` | — |
| [SRC-1AE03B9EC3-L005874](../../agents/web_agent.py#L5874) | 5874 | `"                        # merging candidates into the evidence set or regenerating an answer."` | — |
| [SRC-1AE03B9EC3-L005875](../../agents/web_agent.py#L5875) | 5875 | `"                        pre_gap_source_keys = set(source_indexes)"` | — |
| [SRC-1AE03B9EC3-L005876](../../agents/web_agent.py#L5876) | 5876 | `"                        gap_sources_before_guardrails = len(gap_sources)"` | — |
| [SRC-1AE03B9EC3-L005877](../../agents/web_agent.py#L5877) | 5877 | `"                        gap_sources, gap_guardrail_report = apply_source_guardrails("` | — |
| [SRC-1AE03B9EC3-L005878](../../agents/web_agent.py#L5878) | 5878 | `"                            working_question, clean_mode, plan, gap_sources"` | — |
| [SRC-1AE03B9EC3-L005879](../../agents/web_agent.py#L5879) | 5879 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005880](../../agents/web_agent.py#L5880) | 5880 | `"                        report.setdefault(\"source_guardrails\", {})["` | — |
| [SRC-1AE03B9EC3-L005881](../../agents/web_agent.py#L5881) | 5881 | `"                            \"criterion_gap_repair\""` | — |
| [SRC-1AE03B9EC3-L005882](../../agents/web_agent.py#L5882) | 5882 | `"                        ] = {"` | — |
| [SRC-1AE03B9EC3-L005883](../../agents/web_agent.py#L5883) | 5883 | `"                            **gap_guardrail_report,"` | — |
| [SRC-1AE03B9EC3-L005884](../../agents/web_agent.py#L5884) | 5884 | `"                            \"candidates_before_filter\": gap_sources_before_guardrails,"` | — |
| [SRC-1AE03B9EC3-L005885](../../agents/web_agent.py#L5885) | 5885 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L005886](../../agents/web_agent.py#L5886) | 5886 | `"                        if gap_guardrail_report[\"rejected_sources\"]:"` | — |
| [SRC-1AE03B9EC3-L005887](../../agents/web_agent.py#L5887) | 5887 | `"                            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L005888](../../agents/web_agent.py#L5888) | 5888 | `"                                \"رُفضت بعض نتائج البحث الإضافي لأنها لم تستوفِ شروط قبول \""` | — |
| [SRC-1AE03B9EC3-L005889](../../agents/web_agent.py#L5889) | 5889 | `"                                \"الأدلة الخاصة بالسؤال.\""` | — |
| [SRC-1AE03B9EC3-L005890](../../agents/web_agent.py#L5890) | 5890 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005891](../../agents/web_agent.py#L5891) | 5891 | `"                        evidence_updated = False"` | — |
| [SRC-1AE03B9EC3-L005892](../../agents/web_agent.py#L5892) | 5892 | `"                        for candidate in gap_sources:"` | — |
| [SRC-1AE03B9EC3-L005893](../../agents/web_agent.py#L5893) | 5893 | `"                            if not isinstance(candidate, dict):"` | — |
| [SRC-1AE03B9EC3-L005894](../../agents/web_agent.py#L5894) | 5894 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L005895](../../agents/web_agent.py#L5895) | 5895 | `"                            if not self._source_matches_query(gap_query, candidate):"` | — |
| [SRC-1AE03B9EC3-L005896](../../agents/web_agent.py#L5896) | 5896 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L005897](../../agents/web_agent.py#L5897) | 5897 | `"                            source_key = self._normalized_source_url_key(candidate.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L005898](../../agents/web_agent.py#L5898) | 5898 | `"                            if not source_key:"` | — |
| [SRC-1AE03B9EC3-L005899](../../agents/web_agent.py#L5899) | 5899 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L005900](../../agents/web_agent.py#L5900) | 5900 | `"                            existing_index = source_indexes.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L005901](../../agents/web_agent.py#L5901) | 5901 | `"                            if existing_index is None:"` | — |
| [SRC-1AE03B9EC3-L005902](../../agents/web_agent.py#L5902) | 5902 | `"                                source_indexes[source_key] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005903](../../agents/web_agent.py#L5903) | 5903 | `"                                sources.append(candidate)"` | — |
| [SRC-1AE03B9EC3-L005904](../../agents/web_agent.py#L5904) | 5904 | `"                                criterion_gap_research[\"new_sources_added\"] += 1"` | — |
| [SRC-1AE03B9EC3-L005905](../../agents/web_agent.py#L5905) | 5905 | `"                                evidence_updated = True"` | — |
| [SRC-1AE03B9EC3-L005906](../../agents/web_agent.py#L5906) | 5906 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L005907](../../agents/web_agent.py#L5907) | 5907 | `"                            existing_source = sources[existing_index]"` | — |
| [SRC-1AE03B9EC3-L005908](../../agents/web_agent.py#L5908) | 5908 | `"                            merged = dict(existing_source)"` | — |
| [SRC-1AE03B9EC3-L005909](../../agents/web_agent.py#L5909) | 5909 | `"                            source_enriched = False"` | — |
| [SRC-1AE03B9EC3-L005910](../../agents/web_agent.py#L5910) | 5910 | `"                            for text_key in (\"title\", \"snippet\", \"page_text\"):"` | — |
| [SRC-1AE03B9EC3-L005911](../../agents/web_agent.py#L5911) | 5911 | `"                                old_text = str(merged.get(text_key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L005912](../../agents/web_agent.py#L5912) | 5912 | `"                                new_text = str(candidate.get(text_key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L005913](../../agents/web_agent.py#L5913) | 5913 | `"                                if len(new_text) > len(old_text):"` | — |
| [SRC-1AE03B9EC3-L005914](../../agents/web_agent.py#L5914) | 5914 | `"                                    merged[text_key] = candidate[text_key]"` | — |
| [SRC-1AE03B9EC3-L005915](../../agents/web_agent.py#L5915) | 5915 | `"                                    source_enriched = True"` | — |
| [SRC-1AE03B9EC3-L005916](../../agents/web_agent.py#L5916) | 5916 | `"                            if candidate.get(\"page_fetched\") and not existing_source.get(\"page_fetched\"):"` | — |
| [SRC-1AE03B9EC3-L005917](../../agents/web_agent.py#L5917) | 5917 | `"                                merged[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L005918](../../agents/web_agent.py#L5918) | 5918 | `"                                source_enriched = True"` | — |
| [SRC-1AE03B9EC3-L005919](../../agents/web_agent.py#L5919) | 5919 | `"                            if source_enriched:"` | — |
| [SRC-1AE03B9EC3-L005920](../../agents/web_agent.py#L5920) | 5920 | `"                                evidence_updated = True"` | — |
| [SRC-1AE03B9EC3-L005921](../../agents/web_agent.py#L5921) | 5921 | `"                                criterion_gap_research[\"evidence_sources_enriched\"] += 1"` | — |
| [SRC-1AE03B9EC3-L005922](../../agents/web_agent.py#L5922) | 5922 | `"                            merged[\"providers\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005923](../../agents/web_agent.py#L5923) | 5923 | `"                                list(existing_source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L005924](../../agents/web_agent.py#L5924) | 5924 | `"                                + list(candidate.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L005925](../../agents/web_agent.py#L5925) | 5925 | `"                            ))"` | — |
| [SRC-1AE03B9EC3-L005926](../../agents/web_agent.py#L5926) | 5926 | `"                            merged[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005927](../../agents/web_agent.py#L5927) | 5927 | `"                                list(existing_source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L005928](../../agents/web_agent.py#L5928) | 5928 | `"                                + list(candidate.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L005929](../../agents/web_agent.py#L5929) | 5929 | `"                                + [gap_query]"` | — |
| [SRC-1AE03B9EC3-L005930](../../agents/web_agent.py#L5930) | 5930 | `"                            ))"` | — |
| [SRC-1AE03B9EC3-L005931](../../agents/web_agent.py#L5931) | 5931 | `"                            sources[existing_index] = merged"` | — |
| [SRC-1AE03B9EC3-L005932](../../agents/web_agent.py#L5932) | 5932 | `"                        # Re-apply the guardrails to the merged set as a final safety"` | — |
| [SRC-1AE03B9EC3-L005933](../../agents/web_agent.py#L5933) | 5933 | `"                        # boundary. Count newly added sources only after this filter."` | — |
| [SRC-1AE03B9EC3-L005934](../../agents/web_agent.py#L5934) | 5934 | `"                        sources, merged_guardrail_report = apply_source_guardrails("` | — |
| [SRC-1AE03B9EC3-L005935](../../agents/web_agent.py#L5935) | 5935 | `"                            working_question, clean_mode, plan, sources"` | — |
| [SRC-1AE03B9EC3-L005936](../../agents/web_agent.py#L5936) | 5936 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005937](../../agents/web_agent.py#L5937) | 5937 | `"                        report[\"source_guardrails\"][\"after_criterion_gap_repair\"] = ("` | — |
| [SRC-1AE03B9EC3-L005938](../../agents/web_agent.py#L5938) | 5938 | `"                            merged_guardrail_report"` | — |
| [SRC-1AE03B9EC3-L005939](../../agents/web_agent.py#L5939) | 5939 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005940](../../agents/web_agent.py#L5940) | 5940 | `"                        accepted_source_keys = {"` | — |
| [SRC-1AE03B9EC3-L005941](../../agents/web_agent.py#L5941) | 5941 | `"                            self._normalized_source_url_key(item.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L005942](../../agents/web_agent.py#L5942) | 5942 | `"                            for item in sources"` | — |
| [SRC-1AE03B9EC3-L005943](../../agents/web_agent.py#L5943) | 5943 | `"                            if self._normalized_source_url_key(item.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L005944](../../agents/web_agent.py#L5944) | 5944 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L005945](../../agents/web_agent.py#L5945) | 5945 | `"                        criterion_gap_research[\"new_sources_added\"] = len("` | — |
| [SRC-1AE03B9EC3-L005946](../../agents/web_agent.py#L5946) | 5946 | `"                            accepted_source_keys - pre_gap_source_keys"` | — |
| [SRC-1AE03B9EC3-L005947](../../agents/web_agent.py#L5947) | 5947 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005948](../../agents/web_agent.py#L5948) | 5948 | `"                        criterion_gap_research[\"source_count_after\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L005949](../../agents/web_agent.py#L5949) | 5949 | `"                        plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L005950](../../agents/web_agent.py#L5950) | 5950 | `"                            list(plan.get(\"queries\", [])) + [gap_query]"` | — |
| [SRC-1AE03B9EC3-L005951](../../agents/web_agent.py#L5951) | 5951 | `"                        ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L005952](../../agents/web_agent.py#L5952) | 5952 | `"                        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L005953](../../agents/web_agent.py#L5953) | 5953 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L005954](../../agents/web_agent.py#L5954) | 5954 | `"                            report[\"queries_planned\"] = max("` | — |
| [SRC-1AE03B9EC3-L005955](../../agents/web_agent.py#L5955) | 5955 | `"                                0, int(report.get(\"queries_planned\", 0) or 0)"` | — |
| [SRC-1AE03B9EC3-L005956](../../agents/web_agent.py#L5956) | 5956 | `"                            ) + max(0, int(gap_report.get(\"queries_planned\", 1) or 0))"` | — |
| [SRC-1AE03B9EC3-L005957](../../agents/web_agent.py#L5957) | 5957 | `"                        except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L005958](../../agents/web_agent.py#L5958) | 5958 | `"                            report[\"queries_planned\"] = None"` | — |
| [SRC-1AE03B9EC3-L005959](../../agents/web_agent.py#L5959) | 5959 | `"                        previous_attempts = report.get(\"queries_attempted\")"` | — |
| [SRC-1AE03B9EC3-L005960](../../agents/web_agent.py#L5960) | 5960 | `"                        extra_attempts = gap_report.get(\"queries_attempted\")"` | — |
| [SRC-1AE03B9EC3-L005961](../../agents/web_agent.py#L5961) | 5961 | `"                        if isinstance(previous_attempts, int) and isinstance(extra_attempts, int):"` | — |
| [SRC-1AE03B9EC3-L005962](../../agents/web_agent.py#L5962) | 5962 | `"                            report[\"queries_attempted\"] = max(0, previous_attempts) + max(0, extra_attempts)"` | — |
| [SRC-1AE03B9EC3-L005963](../../agents/web_agent.py#L5963) | 5963 | `"                            report[\"queries_attempted_known\"] = True"` | — |
| [SRC-1AE03B9EC3-L005964](../../agents/web_agent.py#L5964) | 5964 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L005965](../../agents/web_agent.py#L5965) | 5965 | `"                            report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L005966](../../agents/web_agent.py#L5966) | 5966 | `"                            report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L005967](../../agents/web_agent.py#L5967) | 5967 | `"                        old_query_results = report.get(\"query_results\")"` | — |
| [SRC-1AE03B9EC3-L005968](../../agents/web_agent.py#L5968) | 5968 | `"                        new_query_results = gap_report.get(\"query_results\")"` | — |
| [SRC-1AE03B9EC3-L005969](../../agents/web_agent.py#L5969) | 5969 | `"                        report[\"query_results\"] = ("` | — |
| [SRC-1AE03B9EC3-L005970](../../agents/web_agent.py#L5970) | 5970 | `"                            (old_query_results if isinstance(old_query_results, list) else [])"` | — |
| [SRC-1AE03B9EC3-L005971](../../agents/web_agent.py#L5971) | 5971 | `"                            + (new_query_results if isinstance(new_query_results, list) else [])"` | — |
| [SRC-1AE03B9EC3-L005972](../../agents/web_agent.py#L5972) | 5972 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L005973](../../agents/web_agent.py#L5973) | 5973 | `"                        if evidence_updated:"` | — |
| [SRC-1AE03B9EC3-L005974](../../agents/web_agent.py#L5974) | 5974 | `"                            sources.sort("` | — |
| [SRC-1AE03B9EC3-L005975](../../agents/web_agent.py#L5975) | 5975 | `"                                key=lambda item: float(item.get(\"rank_score\", 0) or 0),"` | — |
| [SRC-1AE03B9EC3-L005976](../../agents/web_agent.py#L5976) | 5976 | `"                                reverse=True,"` | — |
| [SRC-1AE03B9EC3-L005977](../../agents/web_agent.py#L5977) | 5977 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L005978](../../agents/web_agent.py#L5978) | 5978 | `"                            try:"` | — |
| [SRC-1AE03B9EC3-L005979](../../agents/web_agent.py#L5979) | 5979 | `"                                revised_draft = self._generate("` | — |
| [SRC-1AE03B9EC3-L005980](../../agents/web_agent.py#L5980) | 5980 | `"                                    working_question,"` | — |
| [SRC-1AE03B9EC3-L005981](../../agents/web_agent.py#L5981) | 5981 | `"                                    clean_history,"` | — |
| [SRC-1AE03B9EC3-L005982](../../agents/web_agent.py#L5982) | 5982 | `"                                    sources,"` | — |
| [SRC-1AE03B9EC3-L005983](../../agents/web_agent.py#L5983) | 5983 | `"                                    search_warning,"` | — |
| [SRC-1AE03B9EC3-L005984](../../agents/web_agent.py#L5984) | 5984 | `"                                    research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L005985](../../agents/web_agent.py#L5985) | 5985 | `"                                    search_report=report,"` | — |
| [SRC-1AE03B9EC3-L005986](../../agents/web_agent.py#L5986) | 5986 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L005987](../../agents/web_agent.py#L5987) | 5987 | `"                                revised_answer = self._review_answer("` | — |
| [SRC-1AE03B9EC3-L005988](../../agents/web_agent.py#L5988) | 5988 | `"                                    working_question, revised_draft, sources[:MAX_LLM_CITED_SOURCES]"` | — |
| [SRC-1AE03B9EC3-L005989](../../agents/web_agent.py#L5989) | 5989 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L005990](../../agents/web_agent.py#L5990) | 5990 | `"                                answer = revised_answer"` | — |
| [SRC-1AE03B9EC3-L005991](../../agents/web_agent.py#L5991) | 5991 | `"                                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L005992](../../agents/web_agent.py#L5992) | 5992 | `"                                criterion_gap_research[\"status\"] = \"evidence_added_and_answer_regenerated\""` | — |
| [SRC-1AE03B9EC3-L005993](../../agents/web_agent.py#L5993) | 5993 | `"                            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L005994](../../agents/web_agent.py#L5994) | 5994 | `"                                criterion_gap_research[\"status\"] = \"evidence_added_but_regeneration_unavailable\""` | — |
| [SRC-1AE03B9EC3-L005995](../../agents/web_agent.py#L5995) | 5995 | `"                                criterion_gap_research[\"regeneration_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L005996](../../agents/web_agent.py#L5996) | 5996 | `"                                coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L005997](../../agents/web_agent.py#L5997) | 5997 | `"                                    \"وصلت أدلة إضافية لمحور مطلوب، لكن تعذرت إعادة توليد الإجابة \""` | — |
| [SRC-1AE03B9EC3-L005998](../../agents/web_agent.py#L5998) | 5998 | `"                                    \"وتدقيقها ضمن الميزانية؛ راجع هذا المحور قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L005999](../../agents/web_agent.py#L5999) | 5999 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L006000](../../agents/web_agent.py#L6000) | 6000 | `"                        elif criterion_gap_research.get(\"status\") != \"search_failed\":"` | — |
| [SRC-1AE03B9EC3-L006001](../../agents/web_agent.py#L6001) | 6001 | `"                            criterion_gap_research[\"status\"] = \"search_completed_no_new_criterion_evidence\""` | — |
| [SRC-1AE03B9EC3-L006002](../../agents/web_agent.py#L6002) | 6002 | `"                            coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006003](../../agents/web_agent.py#L6003) | 6003 | `"                                \"أُجري بحث إضافي لمحاور ناقصة، لكنه لم يضف نص مصدر يمكن تمييزه \""` | — |
| [SRC-1AE03B9EC3-L006004](../../agents/web_agent.py#L6004) | 6004 | `"                                \"كدليل جديد؛ ستظل هذه المحاور غير محسومة.\""` | — |
| [SRC-1AE03B9EC3-L006005](../../agents/web_agent.py#L6005) | 6005 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006006](../../agents/web_agent.py#L6006) | 6006 | `"                        criterion_gap_research[\"source_count_after\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006007](../../agents/web_agent.py#L6007) | 6007 | `"                        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L006008](../../agents/web_agent.py#L6008) | 6008 | `""` | — |
| [SRC-1AE03B9EC3-L006009](../../agents/web_agent.py#L6009) | 6009 | `"        report[\"criterion_gap_research\"] = dict(criterion_gap_research)"` | — |
| [SRC-1AE03B9EC3-L006010](../../agents/web_agent.py#L6010) | 6010 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L006011](../../agents/web_agent.py#L6011) | 6011 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L006012](../../agents/web_agent.py#L6012) | 6012 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006013](../../agents/web_agent.py#L6013) | 6013 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L006014](../../agents/web_agent.py#L6014) | 6014 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L006015](../../agents/web_agent.py#L6015) | 6015 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006016](../../agents/web_agent.py#L6016) | 6016 | `"            initial_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L006017](../../agents/web_agent.py#L6017) | 6017 | `"            missing_targets = ["` | — |
| [SRC-1AE03B9EC3-L006018](../../agents/web_agent.py#L6018) | 6018 | `"                item[\"target\"] for item in initial_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L006019](../../agents/web_agent.py#L6019) | 6019 | `"                if item[\"status\"] == \"possibly_missing\""` | — |
| [SRC-1AE03B9EC3-L006020](../../agents/web_agent.py#L6020) | 6020 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L006021](../../agents/web_agent.py#L6021) | 6021 | `"            remaining_source_gap_targets = ["` | — |
| [SRC-1AE03B9EC3-L006022](../../agents/web_agent.py#L6022) | 6022 | `"                item[\"target\"] for item in initial_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L006023](../../agents/web_agent.py#L6023) | 6023 | `"                if item.get(\"source_evidence_status\") == \"no_source_lexical_signal\""` | — |
| [SRC-1AE03B9EC3-L006024](../../agents/web_agent.py#L6024) | 6024 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L006025](../../agents/web_agent.py#L6025) | 6025 | `"            if not missing_targets and remaining_source_gap_targets:"` | — |
| [SRC-1AE03B9EC3-L006026](../../agents/web_agent.py#L6026) | 6026 | `"                coverage_repair_status = \"source_evidence_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L006027](../../agents/web_agent.py#L6027) | 6027 | `"                if not coverage_repair_warning:"` | — |
| [SRC-1AE03B9EC3-L006028](../../agents/web_agent.py#L6028) | 6028 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006029](../../agents/web_agent.py#L6029) | 6029 | `"                        \"ذُكرت المحاور في الإجابة، لكن لم تظهر لها إشارات لفظية في المصادر؛ \""` | — |
| [SRC-1AE03B9EC3-L006030](../../agents/web_agent.py#L6030) | 6030 | `"                        \"ذكر المحور لا يُعد دليلًا، لذلك تظل المهمة غير مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L006031](../../agents/web_agent.py#L6031) | 6031 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006032](../../agents/web_agent.py#L6032) | 6032 | `"            elif not missing_targets:"` | — |
| [SRC-1AE03B9EC3-L006033](../../agents/web_agent.py#L6033) | 6033 | `"                coverage_repair_status = \"not_needed_lexical_signals_found\""` | — |
| [SRC-1AE03B9EC3-L006034](../../agents/web_agent.py#L6034) | 6034 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L006035](../../agents/web_agent.py#L6035) | 6035 | `"                coverage_repair_status = \"attempted\""` | — |
| [SRC-1AE03B9EC3-L006036](../../agents/web_agent.py#L6036) | 6036 | `"                try:"` | — |
| [SRC-1AE03B9EC3-L006037](../../agents/web_agent.py#L6037) | 6037 | `"                    repaired_answer = self._repair_answer_coverage("` | — |
| [SRC-1AE03B9EC3-L006038](../../agents/web_agent.py#L6038) | 6038 | `"                        working_question, answer, sources, missing_targets"` | — |
| [SRC-1AE03B9EC3-L006039](../../agents/web_agent.py#L6039) | 6039 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006040](../../agents/web_agent.py#L6040) | 6040 | `"                    if repaired_answer.strip() != answer.strip():"` | — |
| [SRC-1AE03B9EC3-L006041](../../agents/web_agent.py#L6041) | 6041 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L006042](../../agents/web_agent.py#L6042) | 6042 | `"                            reaudit_answer = self._review_answer("` | — |
| [SRC-1AE03B9EC3-L006043](../../agents/web_agent.py#L6043) | 6043 | `"                                working_question,"` | — |
| [SRC-1AE03B9EC3-L006044](../../agents/web_agent.py#L6044) | 6044 | `"                                repaired_answer,"` | — |
| [SRC-1AE03B9EC3-L006045](../../agents/web_agent.py#L6045) | 6045 | `"                                sources[:MAX_LLM_CITED_SOURCES],"` | — |
| [SRC-1AE03B9EC3-L006046](../../agents/web_agent.py#L6046) | 6046 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006047](../../agents/web_agent.py#L6047) | 6047 | `"                            answer = reaudit_answer"` | — |
| [SRC-1AE03B9EC3-L006048](../../agents/web_agent.py#L6048) | 6048 | `"                            coverage_repair_status = \"revised_and_reaudited\""` | — |
| [SRC-1AE03B9EC3-L006049](../../agents/web_agent.py#L6049) | 6049 | `"                            review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006050](../../agents/web_agent.py#L6050) | 6050 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L006051](../../agents/web_agent.py#L6051) | 6051 | `"                            review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006052](../../agents/web_agent.py#L6052) | 6052 | `"                            review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L006053](../../agents/web_agent.py#L6053) | 6053 | `"                            coverage_repair_status = ("` | — |
| [SRC-1AE03B9EC3-L006054](../../agents/web_agent.py#L6054) | 6054 | `"                                \"reaudit_budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L006055](../../agents/web_agent.py#L6055) | 6055 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L006056](../../agents/web_agent.py#L6056) | 6056 | `"                                else \"reaudit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006057](../../agents/web_agent.py#L6057) | 6057 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006058](../../agents/web_agent.py#L6058) | 6058 | `"                            review_warning = ("` | — |
| [SRC-1AE03B9EC3-L006059](../../agents/web_agent.py#L6059) | 6059 | `"                                \"استُنفدت ميزانية النماذج قبل إعادة تدقيق الإجابة المعدلة؛ \""` | — |
| [SRC-1AE03B9EC3-L006060](../../agents/web_agent.py#L6060) | 6060 | `"                                \"لذلك لن أعرض النص المعدل بوصفه إجابة مكتملة، وأعرض مقتطفات المصادر بدلًا منه.\""` | — |
| [SRC-1AE03B9EC3-L006061](../../agents/web_agent.py#L6061) | 6061 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L006062](../../agents/web_agent.py#L6062) | 6062 | `"                                else"` | — |
| [SRC-1AE03B9EC3-L006063](../../agents/web_agent.py#L6063) | 6063 | `"                                \"تعذرت إعادة تدقيق الإجابة المعدلة مقابل الأدلة؛ لذلك لن أعرضها بوصفها إجابة مكتملة، \""` | — |
| [SRC-1AE03B9EC3-L006064](../../agents/web_agent.py#L6064) | 6064 | `"                                \"وأعرض مقتطفات المصادر بدلًا منها.\""` | — |
| [SRC-1AE03B9EC3-L006065](../../agents/web_agent.py#L6065) | 6065 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L006066](../../agents/web_agent.py#L6066) | 6066 | `"                            answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L006067](../../agents/web_agent.py#L6067) | 6067 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L006068](../../agents/web_agent.py#L6068) | 6068 | `"                        coverage_repair_status = \"no_change_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L006069](../../agents/web_agent.py#L6069) | 6069 | `"                        coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006070](../../agents/web_agent.py#L6070) | 6070 | `"                            \"رصد الفحص اللفظي محورًا قد يكون ناقصًا، لكن محاولة الإصلاح لم تغيّر الإجابة؛ \""` | — |
| [SRC-1AE03B9EC3-L006071](../../agents/web_agent.py#L6071) | 6071 | `"                            \"تحقق من تغطية هذا المحور يدويًا.\""` | — |
| [SRC-1AE03B9EC3-L006072](../../agents/web_agent.py#L6072) | 6072 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L006073](../../agents/web_agent.py#L6073) | 6073 | `"                except RequestBudgetExceeded:"` | — |
| [SRC-1AE03B9EC3-L006074](../../agents/web_agent.py#L6074) | 6074 | `"                    coverage_repair_status = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L006075](../../agents/web_agent.py#L6075) | 6075 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006076](../../agents/web_agent.py#L6076) | 6076 | `"                        \"استُنفدت ميزانية النماذج قبل محاولة إصلاح محور قد يكون ناقصًا؛ \""` | — |
| [SRC-1AE03B9EC3-L006077](../../agents/web_agent.py#L6077) | 6077 | `"                        \"لا تعتبر التغطية مكتملة دون مراجعة المحور المذكور.\""` | — |
| [SRC-1AE03B9EC3-L006078](../../agents/web_agent.py#L6078) | 6078 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006079](../../agents/web_agent.py#L6079) | 6079 | `"                except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L006080](../../agents/web_agent.py#L6080) | 6080 | `"                    coverage_repair_status = \"unavailable\""` | — |
| [SRC-1AE03B9EC3-L006081](../../agents/web_agent.py#L6081) | 6081 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L006082](../../agents/web_agent.py#L6082) | 6082 | `"                        \"تعذرت محاولة إصلاح محور قد يكون ناقصًا (\""` | — |
| [SRC-1AE03B9EC3-L006083](../../agents/web_agent.py#L6083) | 6083 | `"                        + type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L006084](../../agents/web_agent.py#L6084) | 6084 | `"                        + \")؛ راجع المحاور المطلوبة قبل اعتماد الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L006085](../../agents/web_agent.py#L6085) | 6085 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L006086](../../agents/web_agent.py#L6086) | 6086 | `"        elif coverage_targets and review_status == \"model_claim_audit_completed\" and not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L006087](../../agents/web_agent.py#L6087) | 6087 | `"            coverage_repair_status = \"skipped_no_model_configuration\""` | — |
| [SRC-1AE03B9EC3-L006088](../../agents/web_agent.py#L6088) | 6088 | `"        elif coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L006089](../../agents/web_agent.py#L6089) | 6089 | `"            coverage_repair_status = \"skipped_review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006090](../../agents/web_agent.py#L6090) | 6090 | `""` | — |
| [SRC-1AE03B9EC3-L006091](../../agents/web_agent.py#L6091) | 6091 | `"        if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L006092](../../agents/web_agent.py#L6092) | 6092 | `"            answer += \"\\n\\nروابط إضافية من البحث المباشر عبر الويب:\""` | — |
| [SRC-1AE03B9EC3-L006093](../../agents/web_agent.py#L6093) | 6093 | `"            for source in self.server_search_sources[:8]:"` | — |
| [SRC-1AE03B9EC3-L006094](../../agents/web_agent.py#L6094) | 6094 | `"                answer += \"\\n- \" + source[\"title\"] + \" — \" + source[\"url\"]"` | — |
| [SRC-1AE03B9EC3-L006095](../../agents/web_agent.py#L6095) | 6095 | `"        max_citable_sources = min(MAX_LLM_CITED_SOURCES, len(sources))"` | — |
| [SRC-1AE03B9EC3-L006096](../../agents/web_agent.py#L6096) | 6096 | `"        answer, citation_warnings = self._remove_invalid_citations("` | — |
| [SRC-1AE03B9EC3-L006097](../../agents/web_agent.py#L6097) | 6097 | `"            answer, max_citable_sources"` | — |
| [SRC-1AE03B9EC3-L006098](../../agents/web_agent.py#L6098) | 6098 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006099](../../agents/web_agent.py#L6099) | 6099 | `"        citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L006100](../../agents/web_agent.py#L6100) | 6100 | `"            answer, max_citable_sources, citation_warnings, review_status"` | — |
| [SRC-1AE03B9EC3-L006101](../../agents/web_agent.py#L6101) | 6101 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006102](../../agents/web_agent.py#L6102) | 6102 | `"        report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006103](../../agents/web_agent.py#L6103) | 6103 | `"        report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L006104](../../agents/web_agent.py#L6104) | 6104 | `"        report[\"second_pass_review\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L006105](../../agents/web_agent.py#L6105) | 6105 | `"        report[\"claim_audit\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L006106](../../agents/web_agent.py#L6106) | 6106 | `"        answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L006107](../../agents/web_agent.py#L6107) | 6107 | `"            \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L006108](../../agents/web_agent.py#L6108) | 6108 | `"            \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L006109](../../agents/web_agent.py#L6109) | 6109 | `"            \"review_prompted\": review_status == \"model_claim_audit_completed\","` | — |
| [SRC-1AE03B9EC3-L006110](../../agents/web_agent.py#L6110) | 6110 | `"            \"status\": ("` | — |
| [SRC-1AE03B9EC3-L006111](../../agents/web_agent.py#L6111) | 6111 | `"                \"model_review_requested_not_machine_verified\""` | — |
| [SRC-1AE03B9EC3-L006112](../../agents/web_agent.py#L6112) | 6112 | `"                if coverage_targets and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006113](../../agents/web_agent.py#L6113) | 6113 | `"                else \"review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L006114](../../agents/web_agent.py#L6114) | 6114 | `"                if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L006115](../../agents/web_agent.py#L6115) | 6115 | `"                else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L006116](../../agents/web_agent.py#L6116) | 6116 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L006117](../../agents/web_agent.py#L6117) | 6117 | `"            \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L006118](../../agents/web_agent.py#L6118) | 6118 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006119](../../agents/web_agent.py#L6119) | 6119 | `"        report[\"answer_coverage\"] = answer_coverage"` | — |
| [SRC-1AE03B9EC3-L006120](../../agents/web_agent.py#L6120) | 6120 | `"        report[\"coverage_repair_status\"] = coverage_repair_status"` | — |
| [SRC-1AE03B9EC3-L006121](../../agents/web_agent.py#L6121) | 6121 | `"        answer_integrity = audit_answer_integrity(working_question, answer, sources, coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L006122](../../agents/web_agent.py#L6122) | 6122 | `"        answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L006123](../../agents/web_agent.py#L6123) | 6123 | `"        answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L006124](../../agents/web_agent.py#L6124) | 6124 | `"        answer_coverage[\"source_evidence_gap_count\"] = answer_integrity[\"source_evidence_gap_count\"]"` | — |
| [SRC-1AE03B9EC3-L006125](../../agents/web_agent.py#L6125) | 6125 | `"        answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L006126](../../agents/web_agent.py#L6126) | 6126 | `"        task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L006127](../../agents/web_agent.py#L6127) | 6127 | `"            \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L006128](../../agents/web_agent.py#L6128) | 6128 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L006129](../../agents/web_agent.py#L6129) | 6129 | `"                answer_integrity[\"potentially_missing_target_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006130](../../agents/web_agent.py#L6130) | 6130 | `"                or answer_integrity[\"source_evidence_gap_count\"] > 0"` | — |
| [SRC-1AE03B9EC3-L006131](../../agents/web_agent.py#L6131) | 6131 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006132](../../agents/web_agent.py#L6132) | 6132 | `"            else \"lexical_signals_found_not_semantically_verified\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L006133](../../agents/web_agent.py#L6133) | 6133 | `"            else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L006134](../../agents/web_agent.py#L6134) | 6134 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006135](../../agents/web_agent.py#L6135) | 6135 | `"        answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L006136](../../agents/web_agent.py#L6136) | 6136 | `"        report[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L006137](../../agents/web_agent.py#L6137) | 6137 | `"        report[\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L006138](../../agents/web_agent.py#L6138) | 6138 | `"        report[\"connector_summary\"] = self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L006139](../../agents/web_agent.py#L6139) | 6139 | `"            list(self._provider_diagnostics), sources"` | — |
| [SRC-1AE03B9EC3-L006140](../../agents/web_agent.py#L6140) | 6140 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006141](../../agents/web_agent.py#L6141) | 6141 | `"        report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L006142](../../agents/web_agent.py#L6142) | 6142 | `"        distinct_providers = {"` | — |
| [SRC-1AE03B9EC3-L006143](../../agents/web_agent.py#L6143) | 6143 | `"            provider for source in sources for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L006144](../../agents/web_agent.py#L6144) | 6144 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006145](../../agents/web_agent.py#L6145) | 6145 | `"        distinct_domains = {"` | — |
| [SRC-1AE03B9EC3-L006146](../../agents/web_agent.py#L6146) | 6146 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L006147](../../agents/web_agent.py#L6147) | 6147 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L006148](../../agents/web_agent.py#L6148) | 6148 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L006149](../../agents/web_agent.py#L6149) | 6149 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L006150](../../agents/web_agent.py#L6150) | 6150 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006151](../../agents/web_agent.py#L6151) | 6151 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L006152](../../agents/web_agent.py#L6152) | 6152 | `"        }"` | — |
| [SRC-1AE03B9EC3-L006153](../../agents/web_agent.py#L6153) | 6153 | `"        distinct_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L006154](../../agents/web_agent.py#L6154) | 6154 | `"        fetched_pages = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L006155](../../agents/web_agent.py#L6155) | 6155 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L006156](../../agents/web_agent.py#L6156) | 6156 | `"            len(sources) >= 4 and len(distinct_domains) >= 3"` | — |
| [SRC-1AE03B9EC3-L006157](../../agents/web_agent.py#L6157) | 6157 | `"            and len(distinct_providers) >= 2 and fetched_pages >= 1"` | — |
| [SRC-1AE03B9EC3-L006158](../../agents/web_agent.py#L6158) | 6158 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006159](../../agents/web_agent.py#L6159) | 6159 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006160](../../agents/web_agent.py#L6160) | 6160 | `"            research_quality = \"excellent\""` | — |
| [SRC-1AE03B9EC3-L006161](../../agents/web_agent.py#L6161) | 6161 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L006162](../../agents/web_agent.py#L6162) | 6162 | `"            len(sources) >= 2 and len(distinct_domains) >= 2"` | — |
| [SRC-1AE03B9EC3-L006163](../../agents/web_agent.py#L6163) | 6163 | `"            and (len(distinct_providers) >= 2 or fetched_pages >= 1)"` | — |
| [SRC-1AE03B9EC3-L006164](../../agents/web_agent.py#L6164) | 6164 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006165](../../agents/web_agent.py#L6165) | 6165 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L006166](../../agents/web_agent.py#L6166) | 6166 | `"            research_quality = \"good\""` | — |
| [SRC-1AE03B9EC3-L006167](../../agents/web_agent.py#L6167) | 6167 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L006168](../../agents/web_agent.py#L6168) | 6168 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L006169](../../agents/web_agent.py#L6169) | 6169 | `""` | — |
| [SRC-1AE03B9EC3-L006170](../../agents/web_agent.py#L6170) | 6170 | `"        # Source breadth and a completed model-assisted review do not justify a"` | — |
| [SRC-1AE03B9EC3-L006171](../../agents/web_agent.py#L6171) | 6171 | `"        # positive research-quality label if the final answer has no valid source"` | — |
| [SRC-1AE03B9EC3-L006172](../../agents/web_agent.py#L6172) | 6172 | `"        # citation markers. This is a deterministic presentation guard, not a"` | — |
| [SRC-1AE03B9EC3-L006173](../../agents/web_agent.py#L6173) | 6173 | `"        # semantic entailment check."` | — |
| [SRC-1AE03B9EC3-L006174](../../agents/web_agent.py#L6174) | 6174 | `"        uncited_reviewed_answer = ("` | — |
| [SRC-1AE03B9EC3-L006175](../../agents/web_agent.py#L6175) | 6175 | `"            used_llm"` | — |
| [SRC-1AE03B9EC3-L006176](../../agents/web_agent.py#L6176) | 6176 | `"            and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L006177](../../agents/web_agent.py#L6177) | 6177 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L006178](../../agents/web_agent.py#L6178) | 6178 | `"            and citation_validation[\"valid_citation_count\"] == 0"` | — |
| [SRC-1AE03B9EC3-L006179](../../agents/web_agent.py#L6179) | 6179 | `"        )"` | — |
| [SRC-1AE03B9EC3-L006180](../../agents/web_agent.py#L6180) | 6180 | `"        if uncited_reviewed_answer:"` | — |
| [SRC-1AE03B9EC3-L006181](../../agents/web_agent.py#L6181) | 6181 | `"            research_quality = \"partial\""` | — |
| [SRC-1AE03B9EC3-L006182](../../agents/web_agent.py#L6182) | 6182 | `"            citation_validation[\"claim_support\"] = \"not_established_no_valid_source_citations\""` | — |
| [SRC-1AE03B9EC3-L006183](../../agents/web_agent.py#L6183) | 6183 | `"            answer_evidence_status = \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-1AE03B9EC3-L006184](../../agents/web_agent.py#L6184) | 6184 | `"            uncited_answer_warning = ("` | — |
| [SRC-1AE03B9EC3-L006185](../../agents/web_agent.py#L6185) | 6185 | `"                \"اكتملت مراجعة النموذج، لكن الإجابة النهائية لا تحتوي على إحالات صالحة \""` | — |
| [SRC-1AE03B9EC3-L006186](../../agents/web_agent.py#L6186) | 6186 | `"                \"إلى قائمة المصادر؛ لذلك صُنّفت جودة البحث «جزئية». وجود المصادر أو \""` | — |
| [SRC-1AE03B9EC3-L006187](../../agents/web_agent.py#L6187) | 6187 | `"                \"اكتمال مراجعة النموذج لا يثبت دعم كل ادعاء.\""` | — |
| [SRC-1AE03B9EC3-L006188](../../agents/web_agent.py#L6188) | 6188 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006189](../../agents/web_agent.py#L6189) | 6189 | `"        elif citation_validation[\"valid_citation_count\"] > 0:"` | — |
| [SRC-1AE03B9EC3-L006190](../../agents/web_agent.py#L6190) | 6190 | `"            answer_evidence_status = \"citation_indices_validated_only\""` | — |
| [SRC-1AE03B9EC3-L006191](../../agents/web_agent.py#L6191) | 6191 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L006192](../../agents/web_agent.py#L6192) | 6192 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L006193](../../agents/web_agent.py#L6193) | 6193 | `"            answer_evidence_status = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L006194](../../agents/web_agent.py#L6194) | 6194 | `"            uncited_answer_warning = None"` | — |
| [SRC-1AE03B9EC3-L006195](../../agents/web_agent.py#L6195) | 6195 | `""` | — |
| [SRC-1AE03B9EC3-L006196](../../agents/web_agent.py#L6196) | 6196 | `"        search_attempted = search_attempted or bool(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L006197](../../agents/web_agent.py#L6197) | 6197 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L006198](../../agents/web_agent.py#L6198) | 6198 | `"        prior_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L006199](../../agents/web_agent.py#L6199) | 6199 | `"        if prior_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L006200](../../agents/web_agent.py#L6200) | 6200 | `"            # Preserve a known pipeline failure instead of relabeling it as an ordinary"` | — |
| [SRC-1AE03B9EC3-L006201](../../agents/web_agent.py#L6201) | 6201 | `"            # zero-result search merely because the outer request reached its return path."` | — |
| [SRC-1AE03B9EC3-L006202](../../agents/web_agent.py#L6202) | 6202 | `"            report[\"search_outcome\"] = prior_search_outcome"` | — |
| [SRC-1AE03B9EC3-L006203](../../agents/web_agent.py#L6203) | 6203 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L006204](../../agents/web_agent.py#L6204) | 6204 | `"            report[\"search_outcome\"] = ("` | — |
| [SRC-1AE03B9EC3-L006205](../../agents/web_agent.py#L6205) | 6205 | `"                \"attempted_with_usable_sources\" if search_attempted and sources"` | — |
| [SRC-1AE03B9EC3-L006206](../../agents/web_agent.py#L6206) | 6206 | `"                else \"attempted_no_usable_sources\" if search_attempted"` | — |
| [SRC-1AE03B9EC3-L006207](../../agents/web_agent.py#L6207) | 6207 | `"                else \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L006208](../../agents/web_agent.py#L6208) | 6208 | `"            )"` | — |
| [SRC-1AE03B9EC3-L006209](../../agents/web_agent.py#L6209) | 6209 | `"        report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L006210](../../agents/web_agent.py#L6210) | 6210 | `"        report[\"research_quality\"] = research_quality"` | — |
