# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **008**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L003497 إلى SRC-1AE03B9EC3-L004296
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L003497](../../agents/web_agent.py#L3497) | 3497 | `"                f\"{base_query} case studies recent analysis\","` | — |
| [SRC-1AE03B9EC3-L003498](../../agents/web_agent.py#L3498) | 3498 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L003499](../../agents/web_agent.py#L3499) | 3499 | `"            # Keep query budget for evidence-gap searches if first-round coverage is weak."` | — |
| [SRC-1AE03B9EC3-L003500](../../agents/web_agent.py#L3500) | 3500 | `"            plan[\"queries\"] = list(dict.fromkeys((plan.get(\"queries\") or [])[:3] + candidates))["` | — |
| [SRC-1AE03B9EC3-L003501](../../agents/web_agent.py#L3501) | 3501 | `"                :MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L003502](../../agents/web_agent.py#L3502) | 3502 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L003503](../../agents/web_agent.py#L3503) | 3503 | `"        elif clean_mode == \"latest\":"` | — |
| [SRC-1AE03B9EC3-L003504](../../agents/web_agent.py#L3504) | 3504 | `"            plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L003505](../../agents/web_agent.py#L3505) | 3505 | `"            candidates = ["` | — |
| [SRC-1AE03B9EC3-L003506](../../agents/web_agent.py#L3506) | 3506 | `"                f\"{base_query} latest news updates {dt.datetime.now().year}\","` | — |
| [SRC-1AE03B9EC3-L003507](../../agents/web_agent.py#L3507) | 3507 | `"                f\"{base_query} recent official announcement\","` | — |
| [SRC-1AE03B9EC3-L003508](../../agents/web_agent.py#L3508) | 3508 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L003509](../../agents/web_agent.py#L3509) | 3509 | `"            plan[\"queries\"] = list(dict.fromkeys((plan.get(\"queries\") or [])[:6] + candidates))["` | — |
| [SRC-1AE03B9EC3-L003510](../../agents/web_agent.py#L3510) | 3510 | `"                :MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L003511](../../agents/web_agent.py#L3511) | 3511 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L003512](../../agents/web_agent.py#L3512) | 3512 | `"        elif clean_mode == \"social\":"` | — |
| [SRC-1AE03B9EC3-L003513](../../agents/web_agent.py#L3513) | 3513 | `"            plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L003514](../../agents/web_agent.py#L3514) | 3514 | `"            if not plan.get(\"platforms\"):"` | — |
| [SRC-1AE03B9EC3-L003515](../../agents/web_agent.py#L3515) | 3515 | `"                plan[\"platforms\"] = [\"reddit\", \"bluesky\", \"youtube\"]"` | — |
| [SRC-1AE03B9EC3-L003516](../../agents/web_agent.py#L3516) | 3516 | `"            from agents.research import SOCIAL_DOMAINS"` | — |
| [SRC-1AE03B9EC3-L003517](../../agents/web_agent.py#L3517) | 3517 | `"            candidates = ["` | — |
| [SRC-1AE03B9EC3-L003518](../../agents/web_agent.py#L3518) | 3518 | `"                f\"site:{SOCIAL_DOMAINS[name]} {base_query}\""` | — |
| [SRC-1AE03B9EC3-L003519](../../agents/web_agent.py#L3519) | 3519 | `"                for name in plan[\"platforms\"][:3]"` | — |
| [SRC-1AE03B9EC3-L003520](../../agents/web_agent.py#L3520) | 3520 | `"                if name in SOCIAL_DOMAINS"` | — |
| [SRC-1AE03B9EC3-L003521](../../agents/web_agent.py#L3521) | 3521 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L003522](../../agents/web_agent.py#L3522) | 3522 | `"            plan[\"queries\"] = list(dict.fromkeys((plan.get(\"queries\") or [])[:5] + candidates))["` | — |
| [SRC-1AE03B9EC3-L003523](../../agents/web_agent.py#L3523) | 3523 | `"                :MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L003524](../../agents/web_agent.py#L3524) | 3524 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L003525](../../agents/web_agent.py#L3525) | 3525 | `"        if intent_route == \"LEAD_GENERATION\" and clean_mode == \"auto\":"` | — |
| [SRC-1AE03B9EC3-L003526](../../agents/web_agent.py#L3526) | 3526 | `"            # Prospect discovery needs buyer-intent queries and public social signals,"` | — |
| [SRC-1AE03B9EC3-L003527](../../agents/web_agent.py#L3527) | 3527 | `"            # not just broad pages advertising the requested product."` | — |
| [SRC-1AE03B9EC3-L003528](../../agents/web_agent.py#L3528) | 3528 | `"            plan[\"queries\"] = self._lead_generation_queries(question, plan.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L003529](../../agents/web_agent.py#L3529) | 3529 | `"            plan[\"depth\"] = \"standard\""` | — |
| [SRC-1AE03B9EC3-L003530](../../agents/web_agent.py#L3530) | 3530 | `"            plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L003531](../../agents/web_agent.py#L3531) | 3531 | `"            plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L003532](../../agents/web_agent.py#L3532) | 3532 | `"            allowed_public_platforms = [\"reddit\", \"bluesky\"]"` | — |
| [SRC-1AE03B9EC3-L003533](../../agents/web_agent.py#L3533) | 3533 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L003534](../../agents/web_agent.py#L3534) | 3534 | `"                os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003535](../../agents/web_agent.py#L3535) | 3535 | `"                and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003536](../../agents/web_agent.py#L3536) | 3536 | `"            ):"` | — |
| [SRC-1AE03B9EC3-L003537](../../agents/web_agent.py#L3537) | 3537 | `"                allowed_public_platforms.append(\"facebook\")"` | — |
| [SRC-1AE03B9EC3-L003538](../../agents/web_agent.py#L3538) | 3538 | `"            if os.getenv(\"X_BEARER_TOKEN\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L003539](../../agents/web_agent.py#L3539) | 3539 | `"                allowed_public_platforms.append(\"x\")"` | — |
| [SRC-1AE03B9EC3-L003540](../../agents/web_agent.py#L3540) | 3540 | `"            if os.getenv(\"YOUTUBE_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L003541](../../agents/web_agent.py#L3541) | 3541 | `"                allowed_public_platforms.append(\"youtube\")"` | — |
| [SRC-1AE03B9EC3-L003542](../../agents/web_agent.py#L3542) | 3542 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L003543](../../agents/web_agent.py#L3543) | 3543 | `"                os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003544](../../agents/web_agent.py#L3544) | 3544 | `"                and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003545](../../agents/web_agent.py#L3545) | 3545 | `"            ):"` | — |
| [SRC-1AE03B9EC3-L003546](../../agents/web_agent.py#L3546) | 3546 | `"                allowed_public_platforms.append(\"instagram\")"` | — |
| [SRC-1AE03B9EC3-L003547](../../agents/web_agent.py#L3547) | 3547 | `"            plan[\"platforms\"] = list(dict.fromkeys(allowed_public_platforms))"` | — |
| [SRC-1AE03B9EC3-L003548](../../agents/web_agent.py#L3548) | 3548 | `""` | — |
| [SRC-1AE03B9EC3-L003549](../../agents/web_agent.py#L3549) | 3549 | `"        sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L003550](../../agents/web_agent.py#L3550) | 3550 | `"        search_warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L003551](../../agents/web_agent.py#L3551) | 3551 | `"        report: dict[str, Any] = {}"` | — |
| [SRC-1AE03B9EC3-L003552](../../agents/web_agent.py#L3552) | 3552 | `"        # Scope diagnostic evidence to this research attempt; a reused WebAgent must not"` | — |
| [SRC-1AE03B9EC3-L003553](../../agents/web_agent.py#L3553) | 3553 | `"        # accidentally inherit provider attempts from an earlier question."` | — |
| [SRC-1AE03B9EC3-L003554](../../agents/web_agent.py#L3554) | 3554 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L003555](../../agents/web_agent.py#L3555) | 3555 | `"            research_diagnostic_baseline = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L003556](../../agents/web_agent.py#L3556) | 3556 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L003557](../../agents/web_agent.py#L3557) | 3557 | `"            sources, search_warnings, report = self._collect_research(plan)"` | — |
| [SRC-1AE03B9EC3-L003558](../../agents/web_agent.py#L3558) | 3558 | `"        except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003559](../../agents/web_agent.py#L3559) | 3559 | `"            search_warnings.append(str(exc))"` | — |
| [SRC-1AE03B9EC3-L003560](../../agents/web_agent.py#L3560) | 3560 | `"            baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L003561](../../agents/web_agent.py#L3561) | 3561 | `"            with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L003562](../../agents/web_agent.py#L3562) | 3562 | `"                failure_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L003563](../../agents/web_agent.py#L3563) | 3563 | `"                    item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L003564](../../agents/web_agent.py#L3564) | 3564 | `"                    if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L003565](../../agents/web_agent.py#L3565) | 3565 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L003566](../../agents/web_agent.py#L3566) | 3566 | `"            provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L003567](../../agents/web_agent.py#L3567) | 3567 | `"                item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L003568](../../agents/web_agent.py#L3568) | 3568 | `"                for item in failure_diagnostics"` | — |
| [SRC-1AE03B9EC3-L003569](../../agents/web_agent.py#L3569) | 3569 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003570](../../agents/web_agent.py#L3570) | 3570 | `"            report = {"` | — |
| [SRC-1AE03B9EC3-L003571](../../agents/web_agent.py#L3571) | 3571 | `"                \"queries_planned\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-1AE03B9EC3-L003572](../../agents/web_agent.py#L3572) | 3572 | `"                # The exact query count is unknowable when the pipeline fails before it"` | — |
| [SRC-1AE03B9EC3-L003573](../../agents/web_agent.py#L3573) | 3573 | `"                # returns its report. A provider diagnostic may still prove an attempt."` | — |
| [SRC-1AE03B9EC3-L003574](../../agents/web_agent.py#L3574) | 3574 | `"                \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L003575](../../agents/web_agent.py#L3575) | 3575 | `"                \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L003576](../../agents/web_agent.py#L3576) | 3576 | `"                \"search_attempted\": True if provider_attempt_observed else None,"` | — |
| [SRC-1AE03B9EC3-L003577](../../agents/web_agent.py#L3577) | 3577 | `"                \"search_outcome\": ("` | — |
| [SRC-1AE03B9EC3-L003578](../../agents/web_agent.py#L3578) | 3578 | `"                    \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L003579](../../agents/web_agent.py#L3579) | 3579 | `"                    if provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L003580](../../agents/web_agent.py#L3580) | 3580 | `"                    else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L003581](../../agents/web_agent.py#L3581) | 3581 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L003582](../../agents/web_agent.py#L3582) | 3582 | `"                \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L003583](../../agents/web_agent.py#L3583) | 3583 | `"                \"unique_sources\": None,"` | — |
| [SRC-1AE03B9EC3-L003584](../../agents/web_agent.py#L3584) | 3584 | `"                \"pages_fetched\": None,"` | — |
| [SRC-1AE03B9EC3-L003585](../../agents/web_agent.py#L3585) | 3585 | `"                \"providers_used\": [],"` | — |
| [SRC-1AE03B9EC3-L003586](../../agents/web_agent.py#L3586) | 3586 | `"                \"provider_counts\": None,"` | — |
| [SRC-1AE03B9EC3-L003587](../../agents/web_agent.py#L3587) | 3587 | `"                \"platform_counts\": {},"` | — |
| [SRC-1AE03B9EC3-L003588](../../agents/web_agent.py#L3588) | 3588 | `"                \"social_direct_results\": None,"` | — |
| [SRC-1AE03B9EC3-L003589](../../agents/web_agent.py#L3589) | 3589 | `"                \"provider_diagnostics\": failure_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L003590](../../agents/web_agent.py#L3590) | 3590 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L003591](../../agents/web_agent.py#L3591) | 3591 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L003592](../../agents/web_agent.py#L3592) | 3592 | `"                \"evidence_signals\": evidence_signal_report([], plan.get(\"freshness\", \"any\")),"` | — |
| [SRC-1AE03B9EC3-L003593](../../agents/web_agent.py#L3593) | 3593 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003594](../../agents/web_agent.py#L3594) | 3594 | `"        # Final relevance check is intentionally repeated after fusion, before any answer LLM call."` | — |
| [SRC-1AE03B9EC3-L003595](../../agents/web_agent.py#L3595) | 3595 | `"        filtered_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L003596](../../agents/web_agent.py#L3596) | 3596 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L003597](../../agents/web_agent.py#L3597) | 3597 | `"            if \"user_supplied_url\" in source.get(\"providers\", []):"` | — |
| [SRC-1AE03B9EC3-L003598](../../agents/web_agent.py#L3598) | 3598 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L003599](../../agents/web_agent.py#L3599) | 3599 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L003600](../../agents/web_agent.py#L3600) | 3600 | `"            candidate_queries = source.get(\"queries\") or plan.get(\"queries\") or [question]"` | — |
| [SRC-1AE03B9EC3-L003601](../../agents/web_agent.py#L3601) | 3601 | `"            if any(self._source_matches_query(str(q), source) for q in candidate_queries):"` | — |
| [SRC-1AE03B9EC3-L003602](../../agents/web_agent.py#L3602) | 3602 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L003603](../../agents/web_agent.py#L3603) | 3603 | `"        sources = filtered_sources"` | — |
| [SRC-1AE03B9EC3-L003604](../../agents/web_agent.py#L3604) | 3604 | `"        search_warning = \"؛ \".join(search_warnings) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L003605](../../agents/web_agent.py#L3605) | 3605 | `"        independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L003606](../../agents/web_agent.py#L3606) | 3606 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L003607](../../agents/web_agent.py#L3607) | 3607 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L003608](../../agents/web_agent.py#L3608) | 3608 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L003609](../../agents/web_agent.py#L3609) | 3609 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L003610](../../agents/web_agent.py#L3610) | 3610 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003611](../../agents/web_agent.py#L3611) | 3611 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L003612](../../agents/web_agent.py#L3612) | 3612 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003613](../../agents/web_agent.py#L3613) | 3613 | `"        independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L003614](../../agents/web_agent.py#L3614) | 3614 | `"        # A user-requested page summary is a different task from open-ended research:"` | — |
| [SRC-1AE03B9EC3-L003615](../../agents/web_agent.py#L3615) | 3615 | `"        # one successfully extracted, explicitly supplied page can support a summary,"` | — |
| [SRC-1AE03B9EC3-L003616](../../agents/web_agent.py#L3616) | 3616 | `"        # but must never be presented as independently corroborated research."` | — |
| [SRC-1AE03B9EC3-L003617](../../agents/web_agent.py#L3617) | 3617 | `"        has_read_user_supplied_page = any("` | — |
| [SRC-1AE03B9EC3-L003618](../../agents/web_agent.py#L3618) | 3618 | `"            \"user_supplied_url\" in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L003619](../../agents/web_agent.py#L3619) | 3619 | `"            and bool(source.get(\"page_fetched\"))"` | — |
| [SRC-1AE03B9EC3-L003620](../../agents/web_agent.py#L3620) | 3620 | `"            and bool(str(source.get(\"page_text\") or \"\").strip())"` | — |
| [SRC-1AE03B9EC3-L003621](../../agents/web_agent.py#L3621) | 3621 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L003622](../../agents/web_agent.py#L3622) | 3622 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003623](../../agents/web_agent.py#L3623) | 3623 | `"        single_source_page_summary = ("` | — |
| [SRC-1AE03B9EC3-L003624](../../agents/web_agent.py#L3624) | 3624 | `"            has_read_user_supplied_page"` | — |
| [SRC-1AE03B9EC3-L003625](../../agents/web_agent.py#L3625) | 3625 | `"            and len(sources) == 1"` | — |
| [SRC-1AE03B9EC3-L003626](../../agents/web_agent.py#L3626) | 3626 | `"            and len(independent_domains) == 1"` | — |
| [SRC-1AE03B9EC3-L003627](../../agents/web_agent.py#L3627) | 3627 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003628](../../agents/web_agent.py#L3628) | 3628 | `"        if single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L003629](../../agents/web_agent.py#L3629) | 3629 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L003630](../../agents/web_agent.py#L3630) | 3630 | `"                \"هذا ملخص للرابط الذي قدمته فقط؛ لم يتم تأكيد محتواه من مصدر مستقل آخر.\""` | — |
| [SRC-1AE03B9EC3-L003631](../../agents/web_agent.py#L3631) | 3631 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003632](../../agents/web_agent.py#L3632) | 3632 | `"            search_warning = \"؛ \".join(search_warnings)"` | — |
| [SRC-1AE03B9EC3-L003633](../../agents/web_agent.py#L3633) | 3633 | `"        # Link-finding and lead-discovery are actionable discovery tasks, not broad"` | — |
| [SRC-1AE03B9EC3-L003634](../../agents/web_agent.py#L3634) | 3634 | `"        # fact-checking. Keep useful candidates visible while explicitly labelling them"` | — |
| [SRC-1AE03B9EC3-L003635](../../agents/web_agent.py#L3635) | 3635 | `"        # as uncorroborated instead of refusing a lone result as if it were no result."` | — |
| [SRC-1AE03B9EC3-L003636](../../agents/web_agent.py#L3636) | 3636 | `"        navigation_request = self._is_navigation_request(question)"` | — |
| [SRC-1AE03B9EC3-L003637](../../agents/web_agent.py#L3637) | 3637 | `"        lead_request = intent_route == \"LEAD_GENERATION\" or self._is_lead_search(question)"` | — |
| [SRC-1AE03B9EC3-L003638](../../agents/web_agent.py#L3638) | 3638 | `"        listing_request = self._is_listing_discovery(question)"` | — |
| [SRC-1AE03B9EC3-L003639](../../agents/web_agent.py#L3639) | 3639 | `"        lead_evidence_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L003640](../../agents/web_agent.py#L3640) | 3640 | `"        related_lead_results_count = 0"` | — |
| [SRC-1AE03B9EC3-L003641](../../agents/web_agent.py#L3641) | 3641 | `"        if lead_request:"` | — |
| [SRC-1AE03B9EC3-L003642](../../agents/web_agent.py#L3642) | 3642 | `"            related_lead_results_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L003643](../../agents/web_agent.py#L3643) | 3643 | `"            for source in sources:"` | — |
| [SRC-1AE03B9EC3-L003644](../../agents/web_agent.py#L3644) | 3644 | `"                signal = self._lead_intent_evidence(source)"` | — |
| [SRC-1AE03B9EC3-L003645](../../agents/web_agent.py#L3645) | 3645 | `"                if signal:"` | — |
| [SRC-1AE03B9EC3-L003646](../../agents/web_agent.py#L3646) | 3646 | `"                    source[\"lead_qualification\"] = \"public_buyer_intent_signal\""` | — |
| [SRC-1AE03B9EC3-L003647](../../agents/web_agent.py#L3647) | 3647 | `"                    source[\"lead_intent_evidence\"] = signal"` | — |
| [SRC-1AE03B9EC3-L003648](../../agents/web_agent.py#L3648) | 3648 | `"                    lead_evidence_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L003649](../../agents/web_agent.py#L3649) | 3649 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L003650](../../agents/web_agent.py#L3650) | 3650 | `"                    source[\"lead_qualification\"] = \"related_result_not_lead\""` | — |
| [SRC-1AE03B9EC3-L003651](../../agents/web_agent.py#L3651) | 3651 | `"            lead_research_incomplete = ("` | — |
| [SRC-1AE03B9EC3-L003652](../../agents/web_agent.py#L3652) | 3652 | `"                not sources"` | — |
| [SRC-1AE03B9EC3-L003653](../../agents/web_agent.py#L3653) | 3653 | `"                and report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L003654](../../agents/web_agent.py#L3654) | 3654 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003655](../../agents/web_agent.py#L3655) | 3655 | `"            report[\"lead_generation\"] = {"` | — |
| [SRC-1AE03B9EC3-L003656](../../agents/web_agent.py#L3656) | 3656 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L003657](../../agents/web_agent.py#L3657) | 3657 | `"                    \"research_incomplete\" if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L003658](../../agents/web_agent.py#L3658) | 3658 | `"                    else \"candidate_signals_found\" if lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L003659](../../agents/web_agent.py#L3659) | 3659 | `"                    else \"no_qualified_candidates_found\""` | — |
| [SRC-1AE03B9EC3-L003660](../../agents/web_agent.py#L3660) | 3660 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L003661](../../agents/web_agent.py#L3661) | 3661 | `"                \"candidate_signal_count\": ("` | — |
| [SRC-1AE03B9EC3-L003662](../../agents/web_agent.py#L3662) | 3662 | `"                    None if lead_research_incomplete else len(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L003663](../../agents/web_agent.py#L3663) | 3663 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L003664](../../agents/web_agent.py#L3664) | 3664 | `"                \"related_results_reviewed\": ("` | — |
| [SRC-1AE03B9EC3-L003665](../../agents/web_agent.py#L3665) | 3665 | `"                    None if lead_research_incomplete else related_lead_results_count"` | — |
| [SRC-1AE03B9EC3-L003666](../../agents/web_agent.py#L3666) | 3666 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L003667](../../agents/web_agent.py#L3667) | 3667 | `"                \"qualification_rule\": \"explicit_public_buyer_intent_phrase\","` | — |
| [SRC-1AE03B9EC3-L003668](../../agents/web_agent.py#L3668) | 3668 | `"                \"identity_verified\": False,"` | — |
| [SRC-1AE03B9EC3-L003669](../../agents/web_agent.py#L3669) | 3669 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003670](../../agents/web_agent.py#L3670) | 3670 | `"            if not lead_evidence_sources:"` | — |
| [SRC-1AE03B9EC3-L003671](../../agents/web_agent.py#L3671) | 3671 | `"                if sources:"` | — |
| [SRC-1AE03B9EC3-L003672](../../agents/web_agent.py#L3672) | 3672 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L003673](../../agents/web_agent.py#L3673) | 3673 | `"                        \"لم أعثر على إشارة نصية واضحة تثبت أن أي نتيجة في هذه الجولة تتعلق بشخص \""` | — |
| [SRC-1AE03B9EC3-L003674](../../agents/web_agent.py#L3674) | 3674 | `"                        \"يريد الشراء. راجعت \""` | — |
| [SRC-1AE03B9EC3-L003675](../../agents/web_agent.py#L3675) | 3675 | `"                        + str(len(sources))"` | — |
| [SRC-1AE03B9EC3-L003676](../../agents/web_agent.py#L3676) | 3676 | `"                        + \" نتيجة مرتبطة بالموضوع، لكنني لم أعتبر إعلانات البيع أو صفحات السوق \""` | — |
| [SRC-1AE03B9EC3-L003677](../../agents/web_agent.py#L3677) | 3677 | `"                        \"عملاء محتملين. الروابط أدناه نتائج مرتبطة بالموضوع فقط وليست عملاء.\""` | — |
| [SRC-1AE03B9EC3-L003678](../../agents/web_agent.py#L3678) | 3678 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003679](../../agents/web_agent.py#L3679) | 3679 | `"                elif report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L003680](../../agents/web_agent.py#L3680) | 3680 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L003681](../../agents/web_agent.py#L3681) | 3681 | `"                        \"تعطل مسار البحث أو لم يمكن تأكيد اكتماله؛ لذلك لا أستطيع تحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L003682](../../agents/web_agent.py#L3682) | 3682 | `"                        \"كانت هناك نتائج تصلح كعملاء محتملين في هذه الجولة.\""` | — |
| [SRC-1AE03B9EC3-L003683](../../agents/web_agent.py#L3683) | 3683 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003684](../../agents/web_agent.py#L3684) | 3684 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L003685](../../agents/web_agent.py#L3685) | 3685 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L003686](../../agents/web_agent.py#L3686) | 3686 | `"                        \"لم تظهر نتائج قابلة للاستخدام تثبت نية شراء في هذه الجولة. هذا لا يثبت \""` | — |
| [SRC-1AE03B9EC3-L003687](../../agents/web_agent.py#L3687) | 3687 | `"                        \"عدم وجود عملاء؛ بل يعني أن البحث الحالي لم يعثر على دليل كافٍ.\""` | — |
| [SRC-1AE03B9EC3-L003688](../../agents/web_agent.py#L3688) | 3688 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003689](../../agents/web_agent.py#L3689) | 3689 | `"                report[\"research_quality\"] = \"failed\""` | — |
| [SRC-1AE03B9EC3-L003690](../../agents/web_agent.py#L3690) | 3690 | `"                # Distinguish zero qualified signals from unknown counts after an exception."` | — |
| [SRC-1AE03B9EC3-L003691](../../agents/web_agent.py#L3691) | 3691 | `"                report[\"usable_sources_after_filtering\"] = ("` | — |
| [SRC-1AE03B9EC3-L003692](../../agents/web_agent.py#L3692) | 3692 | `"                    None if lead_research_incomplete else len(sources)"` | — |
| [SRC-1AE03B9EC3-L003693](../../agents/web_agent.py#L3693) | 3693 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003694](../../agents/web_agent.py#L3694) | 3694 | `"                report[\"evidence_signals\"] = ("` | — |
| [SRC-1AE03B9EC3-L003695](../../agents/web_agent.py#L3695) | 3695 | `"                    None if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L003696](../../agents/web_agent.py#L3696) | 3696 | `"                    else evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L003697](../../agents/web_agent.py#L3697) | 3697 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003698](../../agents/web_agent.py#L3698) | 3698 | `"                public_related_sources = [{"` | — |
| [SRC-1AE03B9EC3-L003699](../../agents/web_agent.py#L3699) | 3699 | `"                    \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L003700](../../agents/web_agent.py#L3700) | 3700 | `"                    \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L003701](../../agents/web_agent.py#L3701) | 3701 | `"                    \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L003702](../../agents/web_agent.py#L3702) | 3702 | `"                    \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L003703](../../agents/web_agent.py#L3703) | 3703 | `"                    \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L003704](../../agents/web_agent.py#L3704) | 3704 | `"                    \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L003705](../../agents/web_agent.py#L3705) | 3705 | `"                    \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L003706](../../agents/web_agent.py#L3706) | 3706 | `"                    \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L003707](../../agents/web_agent.py#L3707) | 3707 | `"                    \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L003708](../../agents/web_agent.py#L3708) | 3708 | `"                    \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L003709](../../agents/web_agent.py#L3709) | 3709 | `"                    \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L003710](../../agents/web_agent.py#L3710) | 3710 | `"                    \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L003711](../../agents/web_agent.py#L3711) | 3711 | `"                    \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L003712](../../agents/web_agent.py#L3712) | 3712 | `"                    \"lead_qualification\": \"related_result_not_lead\","` | — |
| [SRC-1AE03B9EC3-L003713](../../agents/web_agent.py#L3713) | 3713 | `"                } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L003714](../../agents/web_agent.py#L3714) | 3714 | `"                return {"` | — |
| [SRC-1AE03B9EC3-L003715](../../agents/web_agent.py#L3715) | 3715 | `"                    \"answer\": lead_answer,"` | — |
| [SRC-1AE03B9EC3-L003716](../../agents/web_agent.py#L3716) | 3716 | `"                    \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L003717](../../agents/web_agent.py#L3717) | 3717 | `"                    \"search_query\": (plan.get(\"queries\") or [question])[0],"` | — |
| [SRC-1AE03B9EC3-L003718](../../agents/web_agent.py#L3718) | 3718 | `"                    \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L003719](../../agents/web_agent.py#L3719) | 3719 | `"                    \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L003720](../../agents/web_agent.py#L3720) | 3720 | `"                        \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L003721](../../agents/web_agent.py#L3721) | 3721 | `"                        \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L003722](../../agents/web_agent.py#L3722) | 3722 | `"                        \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L003723](../../agents/web_agent.py#L3723) | 3723 | `"                        \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L003724](../../agents/web_agent.py#L3724) | 3724 | `"                        \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L003725](../../agents/web_agent.py#L3725) | 3725 | `"                        \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L003726](../../agents/web_agent.py#L3726) | 3726 | `"                        \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L003727](../../agents/web_agent.py#L3727) | 3727 | `"                        \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L003728](../../agents/web_agent.py#L3728) | 3728 | `"                        \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L003729](../../agents/web_agent.py#L3729) | 3729 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L003730](../../agents/web_agent.py#L3730) | 3730 | `"                    \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L003731](../../agents/web_agent.py#L3731) | 3731 | `"                    \"sources\": public_related_sources,"` | — |
| [SRC-1AE03B9EC3-L003732](../../agents/web_agent.py#L3732) | 3732 | `"                    \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L003733](../../agents/web_agent.py#L3733) | 3733 | `"                    \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L003734](../../agents/web_agent.py#L3734) | 3734 | `"                    \"search_attempted\": report.get("` | — |
| [SRC-1AE03B9EC3-L003735](../../agents/web_agent.py#L3735) | 3735 | `"                        \"search_attempted\","` | — |
| [SRC-1AE03B9EC3-L003736](../../agents/web_agent.py#L3736) | 3736 | `"                        bool(report.get(\"queries_attempted\", 0)),"` | — |
| [SRC-1AE03B9EC3-L003737](../../agents/web_agent.py#L3737) | 3737 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L003738](../../agents/web_agent.py#L3738) | 3738 | `"                    \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L003739](../../agents/web_agent.py#L3739) | 3739 | `"                    \"warnings\": [lead_answer],"` | — |
| [SRC-1AE03B9EC3-L003740](../../agents/web_agent.py#L3740) | 3740 | `"                    \"kind\": \"lead_discovery_no_qualified_candidates\","` | — |
| [SRC-1AE03B9EC3-L003741](../../agents/web_agent.py#L3741) | 3741 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L003742](../../agents/web_agent.py#L3742) | 3742 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L003743](../../agents/web_agent.py#L3743) | 3743 | `"                    \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L003744](../../agents/web_agent.py#L3744) | 3744 | `"                }"` | — |
| [SRC-1AE03B9EC3-L003745](../../agents/web_agent.py#L3745) | 3745 | `"            # Only explicit public buyer-intent signals may be synthesized as lead candidates."` | — |
| [SRC-1AE03B9EC3-L003746](../../agents/web_agent.py#L3746) | 3746 | `"            sources = lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L003747](../../agents/web_agent.py#L3747) | 3747 | `"            report[\"evidence_signals\"] = evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L003748](../../agents/web_agent.py#L3748) | 3748 | `"            report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L003749](../../agents/web_agent.py#L3749) | 3749 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L003750](../../agents/web_agent.py#L3750) | 3750 | `"            report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L003751](../../agents/web_agent.py#L3751) | 3751 | `"            independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L003752](../../agents/web_agent.py#L3752) | 3752 | `"                registrable_domain("` | — |
| [SRC-1AE03B9EC3-L003753](../../agents/web_agent.py#L3753) | 3753 | `"                    source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L003754](../../agents/web_agent.py#L3754) | 3754 | `"                    or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L003755](../../agents/web_agent.py#L3755) | 3755 | `"                    or \"\""` | — |
| [SRC-1AE03B9EC3-L003756](../../agents/web_agent.py#L3756) | 3756 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003757](../../agents/web_agent.py#L3757) | 3757 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L003758](../../agents/web_agent.py#L3758) | 3758 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003759](../../agents/web_agent.py#L3759) | 3759 | `"            independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L003760](../../agents/web_agent.py#L3760) | 3760 | `"        single_source_navigation = navigation_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L003761](../../agents/web_agent.py#L3761) | 3761 | `"        single_source_social = bool(plan.get(\"social_focus\")) and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L003762](../../agents/web_agent.py#L3762) | 3762 | `"        single_source_lead = lead_request and bool(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L003763](../../agents/web_agent.py#L3763) | 3763 | `"        single_source_listing = listing_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L003764](../../agents/web_agent.py#L3764) | 3764 | `"        task_specific_partial_evidence = ("` | — |
| [SRC-1AE03B9EC3-L003765](../../agents/web_agent.py#L3765) | 3765 | `"            single_source_page_summary"` | — |
| [SRC-1AE03B9EC3-L003766](../../agents/web_agent.py#L3766) | 3766 | `"            or single_source_navigation"` | — |
| [SRC-1AE03B9EC3-L003767](../../agents/web_agent.py#L3767) | 3767 | `"            or single_source_social"` | — |
| [SRC-1AE03B9EC3-L003768](../../agents/web_agent.py#L3768) | 3768 | `"            or single_source_lead"` | — |
| [SRC-1AE03B9EC3-L003769](../../agents/web_agent.py#L3769) | 3769 | `"            or single_source_listing"` | — |
| [SRC-1AE03B9EC3-L003770](../../agents/web_agent.py#L3770) | 3770 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003771](../../agents/web_agent.py#L3771) | 3771 | `"        needs_corroboration = len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L003772](../../agents/web_agent.py#L3772) | 3772 | `"        evidence_repair: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L003773](../../agents/web_agent.py#L3773) | 3773 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L003774](../../agents/web_agent.py#L3774) | 3774 | `"            \"max_extra_queries\": 1,"` | — |
| [SRC-1AE03B9EC3-L003775](../../agents/web_agent.py#L3775) | 3775 | `"            \"reason\": \"initial_evidence_gate_satisfied\" if not needs_corroboration else \"not_attempted\","` | — |
| [SRC-1AE03B9EC3-L003776](../../agents/web_agent.py#L3776) | 3776 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003777](../../agents/web_agent.py#L3777) | 3777 | `"        if needs_corroboration:"` | — |
| [SRC-1AE03B9EC3-L003778](../../agents/web_agent.py#L3778) | 3778 | `"            if task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L003779](../../agents/web_agent.py#L3779) | 3779 | `"                evidence_repair[\"reason\"] = \"task_specific_partial_evidence\""` | — |
| [SRC-1AE03B9EC3-L003780](../../agents/web_agent.py#L3780) | 3780 | `"            elif plan.get(\"social_focus\"):"` | — |
| [SRC-1AE03B9EC3-L003781](../../agents/web_agent.py#L3781) | 3781 | `"                evidence_repair[\"reason\"] = \"social_search_not_retried\""` | — |
| [SRC-1AE03B9EC3-L003782](../../agents/web_agent.py#L3782) | 3782 | `"            elif plan.get(\"depth\") == \"deep\" or report.get(\"expansion_queries\"):"` | — |
| [SRC-1AE03B9EC3-L003783](../../agents/web_agent.py#L3783) | 3783 | `"                evidence_repair[\"reason\"] = \"deep_research_already_expanded\""` | — |
| [SRC-1AE03B9EC3-L003784](../../agents/web_agent.py#L3784) | 3784 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L003785](../../agents/web_agent.py#L3785) | 3785 | `"                original_queries = ["` | — |
| [SRC-1AE03B9EC3-L003786](../../agents/web_agent.py#L3786) | 3786 | `"                    str(item).strip()"` | — |
| [SRC-1AE03B9EC3-L003787](../../agents/web_agent.py#L3787) | 3787 | `"                    for item in plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L003788](../../agents/web_agent.py#L3788) | 3788 | `"                    if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L003789](../../agents/web_agent.py#L3789) | 3789 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L003790](../../agents/web_agent.py#L3790) | 3790 | `"                base_query = original_queries[0] if original_queries else question"` | — |
| [SRC-1AE03B9EC3-L003791](../../agents/web_agent.py#L3791) | 3791 | `"                suffix = ("` | — |
| [SRC-1AE03B9EC3-L003792](../../agents/web_agent.py#L3792) | 3792 | `"                    \"latest official primary source\""` | — |
| [SRC-1AE03B9EC3-L003793](../../agents/web_agent.py#L3793) | 3793 | `"                    if plan.get(\"freshness\") == \"current\""` | — |
| [SRC-1AE03B9EC3-L003794](../../agents/web_agent.py#L3794) | 3794 | `"                    else \"official primary source data\""` | — |
| [SRC-1AE03B9EC3-L003795](../../agents/web_agent.py#L3795) | 3795 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003796](../../agents/web_agent.py#L3796) | 3796 | `"                repair_query = f\"{base_query} {suffix}\"[:500].strip()"` | — |
| [SRC-1AE03B9EC3-L003797](../../agents/web_agent.py#L3797) | 3797 | `"                known_queries = {"` | — |
| [SRC-1AE03B9EC3-L003798](../../agents/web_agent.py#L3798) | 3798 | `"                    _normalize_search_query(item).casefold()"` | — |
| [SRC-1AE03B9EC3-L003799](../../agents/web_agent.py#L3799) | 3799 | `"                    for item in original_queries"` | — |
| [SRC-1AE03B9EC3-L003800](../../agents/web_agent.py#L3800) | 3800 | `"                }"` | — |
| [SRC-1AE03B9EC3-L003801](../../agents/web_agent.py#L3801) | 3801 | `"                if _normalize_search_query(repair_query).casefold() in known_queries:"` | — |
| [SRC-1AE03B9EC3-L003802](../../agents/web_agent.py#L3802) | 3802 | `"                    repair_query = f\"{base_query} independent corroborating evidence\"[:500].strip()"` | — |
| [SRC-1AE03B9EC3-L003803](../../agents/web_agent.py#L3803) | 3803 | `"                if _normalize_search_query(repair_query).casefold() not in known_queries:"` | — |
| [SRC-1AE03B9EC3-L003804](../../agents/web_agent.py#L3804) | 3804 | `"                    initial_source_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L003805](../../agents/web_agent.py#L3805) | 3805 | `"                    initial_domain_count = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L003806](../../agents/web_agent.py#L3806) | 3806 | `"                    evidence_repair[\"attempted\"] = True"` | — |
| [SRC-1AE03B9EC3-L003807](../../agents/web_agent.py#L3807) | 3807 | `"                    evidence_repair[\"reason\"] = \"thin_or_unrelated_initial_evidence\""` | — |
| [SRC-1AE03B9EC3-L003808](../../agents/web_agent.py#L3808) | 3808 | `"                    evidence_repair[\"query\"] = repair_query"` | — |
| [SRC-1AE03B9EC3-L003809](../../agents/web_agent.py#L3809) | 3809 | `"                    repair_plan = dict(plan)"` | — |
| [SRC-1AE03B9EC3-L003810](../../agents/web_agent.py#L3810) | 3810 | `"                    repair_plan.update({"` | — |
| [SRC-1AE03B9EC3-L003811](../../agents/web_agent.py#L3811) | 3811 | `"                        \"queries\": [repair_query],"` | — |
| [SRC-1AE03B9EC3-L003812](../../agents/web_agent.py#L3812) | 3812 | `"                        \"depth\": \"standard\","` | — |
| [SRC-1AE03B9EC3-L003813](../../agents/web_agent.py#L3813) | 3813 | `"                        \"social_focus\": False,"` | — |
| [SRC-1AE03B9EC3-L003814](../../agents/web_agent.py#L3814) | 3814 | `"                        \"platforms\": [],"` | — |
| [SRC-1AE03B9EC3-L003815](../../agents/web_agent.py#L3815) | 3815 | `"                        \"direct_urls\": [],"` | — |
| [SRC-1AE03B9EC3-L003816](../../agents/web_agent.py#L3816) | 3816 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L003817](../../agents/web_agent.py#L3817) | 3817 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L003818](../../agents/web_agent.py#L3818) | 3818 | `"                        repair_sources, repair_warnings, repair_report = self._collect_research("` | — |
| [SRC-1AE03B9EC3-L003819](../../agents/web_agent.py#L3819) | 3819 | `"                            repair_plan"` | — |
| [SRC-1AE03B9EC3-L003820](../../agents/web_agent.py#L3820) | 3820 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003821](../../agents/web_agent.py#L3821) | 3821 | `"                    except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003822](../../agents/web_agent.py#L3822) | 3822 | `"                        repair_sources = []"` | — |
| [SRC-1AE03B9EC3-L003823](../../agents/web_agent.py#L3823) | 3823 | `"                        repair_warnings = []"` | — |
| [SRC-1AE03B9EC3-L003824](../../agents/web_agent.py#L3824) | 3824 | `"                        repair_report = {"` | — |
| [SRC-1AE03B9EC3-L003825](../../agents/web_agent.py#L3825) | 3825 | `"                            \"queries_planned\": 1,"` | — |
| [SRC-1AE03B9EC3-L003826](../../agents/web_agent.py#L3826) | 3826 | `"                            \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L003827](../../agents/web_agent.py#L3827) | 3827 | `"                            \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L003828](../../agents/web_agent.py#L3828) | 3828 | `"                            \"search_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L003829](../../agents/web_agent.py#L3829) | 3829 | `"                            \"search_outcome\": \"unknown_after_research_error\","` | — |
| [SRC-1AE03B9EC3-L003830](../../agents/web_agent.py#L3830) | 3830 | `"                            \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L003831](../../agents/web_agent.py#L3831) | 3831 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L003832](../../agents/web_agent.py#L3832) | 3832 | `"                        search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L003833](../../agents/web_agent.py#L3833) | 3833 | `"                            \"تعذر تنفيذ محاولة البحث الإضافية المحدودة (\""` | — |
| [SRC-1AE03B9EC3-L003834](../../agents/web_agent.py#L3834) | 3834 | `"                            + type(exc).__name__ + \").\""` | — |
| [SRC-1AE03B9EC3-L003835](../../agents/web_agent.py#L3835) | 3835 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003836](../../agents/web_agent.py#L3836) | 3836 | `"                    search_warnings.extend(repair_warnings)"` | — |
| [SRC-1AE03B9EC3-L003837](../../agents/web_agent.py#L3837) | 3837 | `"                    evidence_repair[\"attempted_query_count\"] = 1"` | — |
| [SRC-1AE03B9EC3-L003838](../../agents/web_agent.py#L3838) | 3838 | `"                    evidence_repair[\"initial_source_count\"] = initial_source_count"` | — |
| [SRC-1AE03B9EC3-L003839](../../agents/web_agent.py#L3839) | 3839 | `"                    evidence_repair[\"initial_independent_domain_count\"] = initial_domain_count"` | — |
| [SRC-1AE03B9EC3-L003840](../../agents/web_agent.py#L3840) | 3840 | `"                    evidence_repair[\"new_sources_added\"] = 0"` | — |
| [SRC-1AE03B9EC3-L003841](../../agents/web_agent.py#L3841) | 3841 | `"                    source_indexes: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L003842](../../agents/web_agent.py#L3842) | 3842 | `"                    for source_index, source in enumerate(sources):"` | — |
| [SRC-1AE03B9EC3-L003843](../../agents/web_agent.py#L3843) | 3843 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L003844](../../agents/web_agent.py#L3844) | 3844 | `"                        if source_key:"` | — |
| [SRC-1AE03B9EC3-L003845](../../agents/web_agent.py#L3845) | 3845 | `"                            source_indexes.setdefault(source_key, source_index)"` | — |
| [SRC-1AE03B9EC3-L003846](../../agents/web_agent.py#L3846) | 3846 | `"                    relevant_queries = list(dict.fromkeys([question] + original_queries))"` | — |
| [SRC-1AE03B9EC3-L003847](../../agents/web_agent.py#L3847) | 3847 | `"                    for source in repair_sources:"` | — |
| [SRC-1AE03B9EC3-L003848](../../agents/web_agent.py#L3848) | 3848 | `"                        if not isinstance(source, dict):"` | — |
| [SRC-1AE03B9EC3-L003849](../../agents/web_agent.py#L3849) | 3849 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L003850](../../agents/web_agent.py#L3850) | 3850 | `"                        if not any("` | — |
| [SRC-1AE03B9EC3-L003851](../../agents/web_agent.py#L3851) | 3851 | `"                            self._source_matches_query(candidate, source)"` | — |
| [SRC-1AE03B9EC3-L003852](../../agents/web_agent.py#L3852) | 3852 | `"                            for candidate in relevant_queries if candidate"` | — |
| [SRC-1AE03B9EC3-L003853](../../agents/web_agent.py#L3853) | 3853 | `"                        ):"` | — |
| [SRC-1AE03B9EC3-L003854](../../agents/web_agent.py#L3854) | 3854 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L003855](../../agents/web_agent.py#L3855) | 3855 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L003856](../../agents/web_agent.py#L3856) | 3856 | `"                        if not source_key:"` | — |
| [SRC-1AE03B9EC3-L003857](../../agents/web_agent.py#L3857) | 3857 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L003858](../../agents/web_agent.py#L3858) | 3858 | `"                        existing_index = source_indexes.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L003859](../../agents/web_agent.py#L3859) | 3859 | `"                        if existing_index is None:"` | — |
| [SRC-1AE03B9EC3-L003860](../../agents/web_agent.py#L3860) | 3860 | `"                            source_indexes[source_key] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L003861](../../agents/web_agent.py#L3861) | 3861 | `"                            sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L003862](../../agents/web_agent.py#L3862) | 3862 | `"                            evidence_repair[\"new_sources_added\"] += 1"` | — |
| [SRC-1AE03B9EC3-L003863](../../agents/web_agent.py#L3863) | 3863 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L003864](../../agents/web_agent.py#L3864) | 3864 | `"                        existing_source = sources[existing_index]"` | — |
| [SRC-1AE03B9EC3-L003865](../../agents/web_agent.py#L3865) | 3865 | `"                        providers = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L003866](../../agents/web_agent.py#L3866) | 3866 | `"                            list(existing_source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L003867](../../agents/web_agent.py#L3867) | 3867 | `"                            + list(source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L003868](../../agents/web_agent.py#L3868) | 3868 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L003869](../../agents/web_agent.py#L3869) | 3869 | `"                        source_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L003870](../../agents/web_agent.py#L3870) | 3870 | `"                            list(existing_source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L003871](../../agents/web_agent.py#L3871) | 3871 | `"                            + list(source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L003872](../../agents/web_agent.py#L3872) | 3872 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L003873](../../agents/web_agent.py#L3873) | 3873 | `"                        if source.get(\"page_fetched\") and not existing_source.get(\"page_fetched\"):"` | — |
| [SRC-1AE03B9EC3-L003874](../../agents/web_agent.py#L3874) | 3874 | `"                            merged_source = dict(existing_source)"` | — |
| [SRC-1AE03B9EC3-L003875](../../agents/web_agent.py#L3875) | 3875 | `"                            merged_source.update(source)"` | — |
| [SRC-1AE03B9EC3-L003876](../../agents/web_agent.py#L3876) | 3876 | `"                            merged_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L003877](../../agents/web_agent.py#L3877) | 3877 | `"                            merged_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L003878](../../agents/web_agent.py#L3878) | 3878 | `"                            sources[existing_index] = merged_source"` | — |
| [SRC-1AE03B9EC3-L003879](../../agents/web_agent.py#L3879) | 3879 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L003880](../../agents/web_agent.py#L3880) | 3880 | `"                            existing_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L003881](../../agents/web_agent.py#L3881) | 3881 | `"                            existing_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L003882](../../agents/web_agent.py#L3882) | 3882 | `"                    sources.sort("` | — |
| [SRC-1AE03B9EC3-L003883](../../agents/web_agent.py#L3883) | 3883 | `"                        key=lambda item: float(item.get(\"rank_score\", 0) or 0),"` | — |
| [SRC-1AE03B9EC3-L003884](../../agents/web_agent.py#L3884) | 3884 | `"                        reverse=True,"` | — |
| [SRC-1AE03B9EC3-L003885](../../agents/web_agent.py#L3885) | 3885 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003886](../../agents/web_agent.py#L3886) | 3886 | `"                    plan[\"queries\"] = list(dict.fromkeys(original_queries + [repair_query]))"` | — |
| [SRC-1AE03B9EC3-L003887](../../agents/web_agent.py#L3887) | 3887 | `"                    independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L003888](../../agents/web_agent.py#L3888) | 3888 | `"                        registrable_domain("` | — |
| [SRC-1AE03B9EC3-L003889](../../agents/web_agent.py#L3889) | 3889 | `"                            source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L003890](../../agents/web_agent.py#L3890) | 3890 | `"                            or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L003891](../../agents/web_agent.py#L3891) | 3891 | `"                            or \"\""` | — |
| [SRC-1AE03B9EC3-L003892](../../agents/web_agent.py#L3892) | 3892 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003893](../../agents/web_agent.py#L3893) | 3893 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L003894](../../agents/web_agent.py#L3894) | 3894 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L003895](../../agents/web_agent.py#L3895) | 3895 | `"                    independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L003896](../../agents/web_agent.py#L3896) | 3896 | `"                    needs_corroboration = ("` | — |
| [SRC-1AE03B9EC3-L003897](../../agents/web_agent.py#L3897) | 3897 | `"                        len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L003898](../../agents/web_agent.py#L3898) | 3898 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003899](../../agents/web_agent.py#L3899) | 3899 | `"                    evidence_repair.update({"` | — |
| [SRC-1AE03B9EC3-L003900](../../agents/web_agent.py#L3900) | 3900 | `"                        \"final_source_count\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L003901](../../agents/web_agent.py#L3901) | 3901 | `"                        \"final_independent_domain_count\": len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L003902](../../agents/web_agent.py#L3902) | 3902 | `"                        \"recovered\": not needs_corroboration,"` | — |
| [SRC-1AE03B9EC3-L003903](../../agents/web_agent.py#L3903) | 3903 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L003904](../../agents/web_agent.py#L3904) | 3904 | `"                    evidence_repair[\"reason\"] = ("` | — |
| [SRC-1AE03B9EC3-L003905](../../agents/web_agent.py#L3905) | 3905 | `"                        \"single_bounded_retry_still_insufficient\""` | — |
| [SRC-1AE03B9EC3-L003906](../../agents/web_agent.py#L3906) | 3906 | `"                        if needs_corroboration else \"evidence_gate_recovered\""` | — |
| [SRC-1AE03B9EC3-L003907](../../agents/web_agent.py#L3907) | 3907 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003908](../../agents/web_agent.py#L3908) | 3908 | `"                    report[\"queries_planned\"] = int(report.get(\"queries_planned\", 0) or 0) + int("` | — |
| [SRC-1AE03B9EC3-L003909](../../agents/web_agent.py#L3909) | 3909 | `"                        repair_report.get(\"queries_planned\", 1) or 0"` | — |
| [SRC-1AE03B9EC3-L003910](../../agents/web_agent.py#L3910) | 3910 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003911](../../agents/web_agent.py#L3911) | 3911 | `"                    initial_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L003912](../../agents/web_agent.py#L3912) | 3912 | `"                    repair_attempt_count = repair_report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L003913](../../agents/web_agent.py#L3913) | 3913 | `"                    if initial_attempt_count is None or repair_attempt_count is None:"` | — |
| [SRC-1AE03B9EC3-L003914](../../agents/web_agent.py#L3914) | 3914 | `"                        report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L003915](../../agents/web_agent.py#L3915) | 3915 | `"                        report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L003916](../../agents/web_agent.py#L3916) | 3916 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L003917](../../agents/web_agent.py#L3917) | 3917 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L003918](../../agents/web_agent.py#L3918) | 3918 | `"                            report[\"queries_attempted\"] = max(0, int(initial_attempt_count or 0)) + max("` | — |
| [SRC-1AE03B9EC3-L003919](../../agents/web_agent.py#L3919) | 3919 | `"                                0, int(repair_attempt_count or 0)"` | — |
| [SRC-1AE03B9EC3-L003920](../../agents/web_agent.py#L3920) | 3920 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L003921](../../agents/web_agent.py#L3921) | 3921 | `"                            report[\"queries_attempted_known\"] = True"` | — |
| [SRC-1AE03B9EC3-L003922](../../agents/web_agent.py#L3922) | 3922 | `"                        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L003923](../../agents/web_agent.py#L3923) | 3923 | `"                            report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L003924](../../agents/web_agent.py#L3924) | 3924 | `"                            report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L003925](../../agents/web_agent.py#L3925) | 3925 | `"                    report[\"query_results\"] = list(report.get(\"query_results\", [])) + list("` | — |
| [SRC-1AE03B9EC3-L003926](../../agents/web_agent.py#L3926) | 3926 | `"                        repair_report.get(\"query_results\", [])"` | — |
| [SRC-1AE03B9EC3-L003927](../../agents/web_agent.py#L3927) | 3927 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003928](../../agents/web_agent.py#L3928) | 3928 | `"                    merged_providers = {"` | — |
| [SRC-1AE03B9EC3-L003929](../../agents/web_agent.py#L3929) | 3929 | `"                        provider"` | — |
| [SRC-1AE03B9EC3-L003930](../../agents/web_agent.py#L3930) | 3930 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L003931](../../agents/web_agent.py#L3931) | 3931 | `"                        for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L003932](../../agents/web_agent.py#L3932) | 3932 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L003933](../../agents/web_agent.py#L3933) | 3933 | `"                    report[\"providers_used\"] = sorted(merged_providers)"` | — |
| [SRC-1AE03B9EC3-L003934](../../agents/web_agent.py#L3934) | 3934 | `"                    report[\"provider_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L003935](../../agents/web_agent.py#L3935) | 3935 | `"                        provider: sum("` | — |
| [SRC-1AE03B9EC3-L003936](../../agents/web_agent.py#L3936) | 3936 | `"                            provider in source.get(\"providers\", []) for source in sources"` | — |
| [SRC-1AE03B9EC3-L003937](../../agents/web_agent.py#L3937) | 3937 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003938](../../agents/web_agent.py#L3938) | 3938 | `"                        for provider in merged_providers"` | — |
| [SRC-1AE03B9EC3-L003939](../../agents/web_agent.py#L3939) | 3939 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L003940](../../agents/web_agent.py#L3940) | 3940 | `"                    report[\"platform_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L003941](../../agents/web_agent.py#L3941) | 3941 | `"                        str(source.get(\"platform\", \"web\")): sum("` | — |
| [SRC-1AE03B9EC3-L003942](../../agents/web_agent.py#L3942) | 3942 | `"                            str(other.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L003943](../../agents/web_agent.py#L3943) | 3943 | `"                            == str(source.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L003944](../../agents/web_agent.py#L3944) | 3944 | `"                            for other in sources"` | — |
| [SRC-1AE03B9EC3-L003945](../../agents/web_agent.py#L3945) | 3945 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003946](../../agents/web_agent.py#L3946) | 3946 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L003947](../../agents/web_agent.py#L3947) | 3947 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L003948](../../agents/web_agent.py#L3948) | 3948 | `"                    report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L003949](../../agents/web_agent.py#L3949) | 3949 | `"                    report[\"pages_fetched\"] = sum("` | — |
| [SRC-1AE03B9EC3-L003950](../../agents/web_agent.py#L3950) | 3950 | `"                        bool(source.get(\"page_fetched\")) for source in sources"` | — |
| [SRC-1AE03B9EC3-L003951](../../agents/web_agent.py#L3951) | 3951 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003952](../../agents/web_agent.py#L3952) | 3952 | `"                    report[\"independent_sources\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L003953](../../agents/web_agent.py#L3953) | 3953 | `"                    report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L003954](../../agents/web_agent.py#L3954) | 3954 | `"                    report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L003955](../../agents/web_agent.py#L3955) | 3955 | `"                        sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L003956](../../agents/web_agent.py#L3956) | 3956 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003957](../../agents/web_agent.py#L3957) | 3957 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L003958](../../agents/web_agent.py#L3958) | 3958 | `"                    evidence_repair[\"reason\"] = \"repair_query_was_not_distinct\""` | — |
| [SRC-1AE03B9EC3-L003959](../../agents/web_agent.py#L3959) | 3959 | `"        report[\"evidence_repair\"] = evidence_repair"` | — |
| [SRC-1AE03B9EC3-L003960](../../agents/web_agent.py#L3960) | 3960 | `"        baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L003961](../../agents/web_agent.py#L3961) | 3961 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L003962](../../agents/web_agent.py#L3962) | 3962 | `"            current_research_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L003963](../../agents/web_agent.py#L3963) | 3963 | `"                item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L003964](../../agents/web_agent.py#L3964) | 3964 | `"                if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L003965](../../agents/web_agent.py#L3965) | 3965 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L003966](../../agents/web_agent.py#L3966) | 3966 | `"        report[\"provider_diagnostics\"] = current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L003967](../../agents/web_agent.py#L3967) | 3967 | `"        provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L003968](../../agents/web_agent.py#L3968) | 3968 | `"            item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L003969](../../agents/web_agent.py#L3969) | 3969 | `"            for item in current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L003970](../../agents/web_agent.py#L3970) | 3970 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003971](../../agents/web_agent.py#L3971) | 3971 | `"        raw_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L003972](../../agents/web_agent.py#L3972) | 3972 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L003973](../../agents/web_agent.py#L3973) | 3973 | `"            queries_attempted = ("` | — |
| [SRC-1AE03B9EC3-L003974](../../agents/web_agent.py#L3974) | 3974 | `"                None if raw_attempt_count is None"` | — |
| [SRC-1AE03B9EC3-L003975](../../agents/web_agent.py#L3975) | 3975 | `"                else max(0, int(raw_attempt_count or 0))"` | — |
| [SRC-1AE03B9EC3-L003976](../../agents/web_agent.py#L3976) | 3976 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003977](../../agents/web_agent.py#L3977) | 3977 | `"        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L003978](../../agents/web_agent.py#L3978) | 3978 | `"            queries_attempted = None"` | — |
| [SRC-1AE03B9EC3-L003979](../../agents/web_agent.py#L3979) | 3979 | `"        if queries_attempted is not None:"` | — |
| [SRC-1AE03B9EC3-L003980](../../agents/web_agent.py#L3980) | 3980 | `"            search_attempted = ("` | — |
| [SRC-1AE03B9EC3-L003981](../../agents/web_agent.py#L3981) | 3981 | `"                queries_attempted > 0"` | — |
| [SRC-1AE03B9EC3-L003982](../../agents/web_agent.py#L3982) | 3982 | `"                or provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L003983](../../agents/web_agent.py#L3983) | 3983 | `"                or report.get(\"search_attempted\") is True"` | — |
| [SRC-1AE03B9EC3-L003984](../../agents/web_agent.py#L3984) | 3984 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003985](../../agents/web_agent.py#L3985) | 3985 | `"        elif provider_attempt_observed or report.get(\"search_attempted\") is True:"` | — |
| [SRC-1AE03B9EC3-L003986](../../agents/web_agent.py#L3986) | 3986 | `"            search_attempted = True"` | — |
| [SRC-1AE03B9EC3-L003987](../../agents/web_agent.py#L3987) | 3987 | `"        elif isinstance(report.get(\"search_attempted\"), bool):"` | — |
| [SRC-1AE03B9EC3-L003988](../../agents/web_agent.py#L3988) | 3988 | `"            search_attempted = report[\"search_attempted\"]"` | — |
| [SRC-1AE03B9EC3-L003989](../../agents/web_agent.py#L3989) | 3989 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L003990](../../agents/web_agent.py#L3990) | 3990 | `"            search_attempted = None"` | — |
| [SRC-1AE03B9EC3-L003991](../../agents/web_agent.py#L3991) | 3991 | `"        report[\"queries_attempted\"] = queries_attempted"` | — |
| [SRC-1AE03B9EC3-L003992](../../agents/web_agent.py#L3992) | 3992 | `"        report[\"queries_attempted_known\"] = queries_attempted is not None"` | — |
| [SRC-1AE03B9EC3-L003993](../../agents/web_agent.py#L3993) | 3993 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L003994](../../agents/web_agent.py#L3994) | 3994 | `"        previous_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L003995](../../agents/web_agent.py#L3995) | 3995 | `"        if previous_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L003996](../../agents/web_agent.py#L3996) | 3996 | `"            if provider_attempt_observed or search_attempted is True:"` | — |
| [SRC-1AE03B9EC3-L003997](../../agents/web_agent.py#L3997) | 3997 | `"                search_outcome = \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L003998](../../agents/web_agent.py#L3998) | 3998 | `"            elif search_attempted is False:"` | — |
| [SRC-1AE03B9EC3-L003999](../../agents/web_agent.py#L3999) | 3999 | `"                search_outcome = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L004000](../../agents/web_agent.py#L4000) | 4000 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004001](../../agents/web_agent.py#L4001) | 4001 | `"                search_outcome = \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L004002](../../agents/web_agent.py#L4002) | 4002 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L004003](../../agents/web_agent.py#L4003) | 4003 | `"            search_outcome = ("` | — |
| [SRC-1AE03B9EC3-L004004](../../agents/web_agent.py#L4004) | 4004 | `"                \"attempted_with_usable_sources\" if search_attempted is True and sources"` | — |
| [SRC-1AE03B9EC3-L004005](../../agents/web_agent.py#L4005) | 4005 | `"                else \"attempted_no_usable_sources\" if search_attempted is True"` | — |
| [SRC-1AE03B9EC3-L004006](../../agents/web_agent.py#L4006) | 4006 | `"                else \"not_attempted\" if search_attempted is False"` | — |
| [SRC-1AE03B9EC3-L004007](../../agents/web_agent.py#L4007) | 4007 | `"                else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L004008](../../agents/web_agent.py#L4008) | 4008 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004009](../../agents/web_agent.py#L4009) | 4009 | `"        report[\"search_outcome\"] = search_outcome"` | — |
| [SRC-1AE03B9EC3-L004010](../../agents/web_agent.py#L4010) | 4010 | `"        if search_outcome in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L004011](../../agents/web_agent.py#L4011) | 4011 | `"            report[\"usable_sources_after_filtering\"] = None"` | — |
| [SRC-1AE03B9EC3-L004012](../../agents/web_agent.py#L4012) | 4012 | `"            report[\"unique_sources\"] = None"` | — |
| [SRC-1AE03B9EC3-L004013](../../agents/web_agent.py#L4013) | 4013 | `"            report[\"pages_fetched\"] = None"` | — |
| [SRC-1AE03B9EC3-L004014](../../agents/web_agent.py#L4014) | 4014 | `"            report[\"provider_counts\"] = None"` | — |
| [SRC-1AE03B9EC3-L004015](../../agents/web_agent.py#L4015) | 4015 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L004016](../../agents/web_agent.py#L4016) | 4016 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004017](../../agents/web_agent.py#L4017) | 4017 | `"            if report.get(\"unique_sources\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L004018](../../agents/web_agent.py#L4018) | 4018 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004019](../../agents/web_agent.py#L4019) | 4019 | `"            if report.get(\"pages_fetched\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L004020](../../agents/web_agent.py#L4020) | 4020 | `"                report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L004021](../../agents/web_agent.py#L4021) | 4021 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L004022](../../agents/web_agent.py#L4022) | 4022 | `"        report[\"distinct_registrable_domains\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L004023](../../agents/web_agent.py#L4023) | 4023 | `"        report[\"independent_sources\"] = len(independent_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L004024](../../agents/web_agent.py#L4024) | 4024 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L004025](../../agents/web_agent.py#L4025) | 4025 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L004026](../../agents/web_agent.py#L4026) | 4026 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004027](../../agents/web_agent.py#L4027) | 4027 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L004028](../../agents/web_agent.py#L4028) | 4028 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L004029](../../agents/web_agent.py#L4029) | 4029 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004030](../../agents/web_agent.py#L4030) | 4030 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L004031](../../agents/web_agent.py#L4031) | 4031 | `"        if len(independent_domains) >= 2:"` | — |
| [SRC-1AE03B9EC3-L004032](../../agents/web_agent.py#L4032) | 4032 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004033](../../agents/web_agent.py#L4033) | 4033 | `"                \"تعدد النطاقات المسجلة لا يثبت الاستقلال التحريري؛ قد تنقل المواقع عن المصدر الأصلي نفسه.\""` | — |
| [SRC-1AE03B9EC3-L004034](../../agents/web_agent.py#L4034) | 4034 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004035](../../agents/web_agent.py#L4035) | 4035 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L004036](../../agents/web_agent.py#L4036) | 4036 | `"        if needs_corroboration and single_source_navigation and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L004037](../../agents/web_agent.py#L4037) | 4037 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004038](../../agents/web_agent.py#L4038) | 4038 | `"                \"هذه نتيجة مرشحة لطلب العثور على موقع/رابط؛ لم تُثبت رسميتها أو صحتها \""` | — |
| [SRC-1AE03B9EC3-L004039](../../agents/web_agent.py#L4039) | 4039 | `"                \"من مصدر مستقل، لذا راجع الرابط قبل الاعتماد عليه.\""` | — |
| [SRC-1AE03B9EC3-L004040](../../agents/web_agent.py#L4040) | 4040 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004041](../../agents/web_agent.py#L4041) | 4041 | `"        if needs_corroboration and (single_source_social or single_source_lead) and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L004042](../../agents/web_agent.py#L4042) | 4042 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004043](../../agents/web_agent.py#L4043) | 4043 | `"                \"هذه إشارات بحث أولية وليست تحققًا مستقلًا من هوية العميل أو نيته؛ \""` | — |
| [SRC-1AE03B9EC3-L004044](../../agents/web_agent.py#L4044) | 4044 | `"                \"راجع المنشور وتاريخه وسياقه قبل التواصل أو اتخاذ قرار.\""` | — |
| [SRC-1AE03B9EC3-L004045](../../agents/web_agent.py#L4045) | 4045 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004046](../../agents/web_agent.py#L4046) | 4046 | `"        if needs_corroboration and single_source_listing and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L004047](../../agents/web_agent.py#L4047) | 4047 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004048](../../agents/web_agent.py#L4048) | 4048 | `"                \"هذه إعلانات/قوائم مرشحة فقط. قد تكون منتهية أو غير دقيقة؛ تحقق من السعر \""` | — |
| [SRC-1AE03B9EC3-L004049](../../agents/web_agent.py#L4049) | 4049 | `"                \"والتوافر ومصدر الإعلان واطلب تأكيدًا حديثًا قبل دفع مال أو مشاركة بيانات.\""` | — |
| [SRC-1AE03B9EC3-L004050](../../agents/web_agent.py#L4050) | 4050 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004051](../../agents/web_agent.py#L4051) | 4051 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L004052](../../agents/web_agent.py#L4052) | 4052 | `"        if needs_corroboration and not task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L004053](../../agents/web_agent.py#L4053) | 4053 | `"            if search_outcome == \"unknown_after_research_error\":"` | — |
| [SRC-1AE03B9EC3-L004054](../../agents/web_agent.py#L4054) | 4054 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004055](../../agents/web_agent.py#L4055) | 4055 | `"                    \"تعذر إكمال مسار البحث بسبب خطأ، ولا توجد بيانات كافية لتحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L004056](../../agents/web_agent.py#L4056) | 4056 | `"                    \"كانت محاولة البحث قد اكتملت أو كم نتيجة جُمعت. لذلك لا أستطيع الجزم \""` | — |
| [SRC-1AE03B9EC3-L004057](../../agents/web_agent.py#L4057) | 4057 | `"                    \"بأن البحث لم يُنفّذ أو أن الإنترنت لم يُعد نتائج. لم أتمكن من تقديم \""` | — |
| [SRC-1AE03B9EC3-L004058](../../agents/web_agent.py#L4058) | 4058 | `"                    \"إجابة مكتملة؛ أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L004059](../../agents/web_agent.py#L4059) | 4059 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004060](../../agents/web_agent.py#L4060) | 4060 | `"            elif search_outcome == \"attempted_research_error\":"` | — |
| [SRC-1AE03B9EC3-L004061](../../agents/web_agent.py#L4061) | 4061 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004062](../../agents/web_agent.py#L4062) | 4062 | `"                    \"توجد قرائن تشغيلية على بدء محاولة بحث، لكن مسار البحث فشل قبل إنتاج \""` | — |
| [SRC-1AE03B9EC3-L004063](../../agents/web_agent.py#L4063) | 4063 | `"                    \"تقرير مكتمل. لا أستطيع تحديد عدد النتائج أو المصادر القابلة للاستخدام، \""` | — |
| [SRC-1AE03B9EC3-L004064](../../agents/web_agent.py#L4064) | 4064 | `"                    \"لذلك لن أخمّن. أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L004065](../../agents/web_agent.py#L4065) | 4065 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004066](../../agents/web_agent.py#L4066) | 4066 | `"            elif search_outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-1AE03B9EC3-L004067](../../agents/web_agent.py#L4067) | 4067 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004068](../../agents/web_agent.py#L4068) | 4068 | `"                    \"جرت محاولة البحث، لكن لم تتوفر مصادر صالحة وكافية للإجابة بعد تصفية \""` | — |
| [SRC-1AE03B9EC3-L004069](../../agents/web_agent.py#L4069) | 4069 | `"                    \"النتائج. هذا لا يثبت أن جميع المواقع أو الإنترنت غير متاح؛ لن أخمّن \""` | — |
| [SRC-1AE03B9EC3-L004070](../../agents/web_agent.py#L4070) | 4070 | `"                    \"أو أقدّم نتيجة غير مدعومة. جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L004071](../../agents/web_agent.py#L4071) | 4071 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004072](../../agents/web_agent.py#L4072) | 4072 | `"            elif search_outcome == \"not_attempted\":"` | — |
| [SRC-1AE03B9EC3-L004073](../../agents/web_agent.py#L4073) | 4073 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004074](../../agents/web_agent.py#L4074) | 4074 | `"                    \"لم تبدأ محاولة بحث ويب لهذا الطلب، لذلك لا تتوفر لدي أدلة ويب حالية \""` | — |
| [SRC-1AE03B9EC3-L004075](../../agents/web_agent.py#L4075) | 4075 | `"                    \"كافية للإجابة. لن أقدّم نتيجة غير مدعومة؛ أعد المحاولة أو اطلب بحثًا \""` | — |
| [SRC-1AE03B9EC3-L004076](../../agents/web_agent.py#L4076) | 4076 | `"                    \"صريحًا إذا كان ذلك مناسبًا.\""` | — |
| [SRC-1AE03B9EC3-L004077](../../agents/web_agent.py#L4077) | 4077 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004078](../../agents/web_agent.py#L4078) | 4078 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004079](../../agents/web_agent.py#L4079) | 4079 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004080](../../agents/web_agent.py#L4080) | 4080 | `"                    \"لم أجد معلومات موثوقة كافية مرتبطة بسؤالك من نطاقين مسجلين مختلفين على الأقل. \""` | — |
| [SRC-1AE03B9EC3-L004081](../../agents/web_agent.py#L4081) | 4081 | `"                    \"اختلاف النطاقات لا يثبت الاستقلال التحريري. لن أخمّن أو أقدّم نتيجة غير مدعومة؛ \""` | — |
| [SRC-1AE03B9EC3-L004082](../../agents/web_agent.py#L4082) | 4082 | `"                    \"جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L004083](../../agents/web_agent.py#L4083) | 4083 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004084](../../agents/web_agent.py#L4084) | 4084 | `"            public_sources = [{"` | — |
| [SRC-1AE03B9EC3-L004085](../../agents/web_agent.py#L4085) | 4085 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L004086](../../agents/web_agent.py#L4086) | 4086 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L004087](../../agents/web_agent.py#L4087) | 4087 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004088](../../agents/web_agent.py#L4088) | 4088 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L004089](../../agents/web_agent.py#L4089) | 4089 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L004090](../../agents/web_agent.py#L4090) | 4090 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L004091](../../agents/web_agent.py#L4091) | 4091 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L004092](../../agents/web_agent.py#L4092) | 4092 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004093](../../agents/web_agent.py#L4093) | 4093 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L004094](../../agents/web_agent.py#L4094) | 4094 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004095](../../agents/web_agent.py#L4095) | 4095 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004096](../../agents/web_agent.py#L4096) | 4096 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004097](../../agents/web_agent.py#L4097) | 4097 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L004098](../../agents/web_agent.py#L4098) | 4098 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L004099](../../agents/web_agent.py#L4099) | 4099 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L004100](../../agents/web_agent.py#L4100) | 4100 | `"            } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L004101](../../agents/web_agent.py#L4101) | 4101 | `"            citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L004102](../../agents/web_agent.py#L4102) | 4102 | `"                reason, 0, [], \"not_run\""` | — |
| [SRC-1AE03B9EC3-L004103](../../agents/web_agent.py#L4103) | 4103 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004104](../../agents/web_agent.py#L4104) | 4104 | `"            citation_validation[\"status\"] = \"not_applicable_no_generated_answer\""` | — |
| [SRC-1AE03B9EC3-L004105](../../agents/web_agent.py#L4105) | 4105 | `"            coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L004106](../../agents/web_agent.py#L4106) | 4106 | `"            answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L004107](../../agents/web_agent.py#L4107) | 4107 | `"                \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L004108](../../agents/web_agent.py#L4108) | 4108 | `"                \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L004109](../../agents/web_agent.py#L4109) | 4109 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L004110](../../agents/web_agent.py#L4110) | 4110 | `"                    \"not_reviewed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L004111](../../agents/web_agent.py#L4111) | 4111 | `"                    if coverage_targets else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L004112](../../agents/web_agent.py#L4112) | 4112 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004113](../../agents/web_agent.py#L4113) | 4113 | `"                \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L004114](../../agents/web_agent.py#L4114) | 4114 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004115](../../agents/web_agent.py#L4115) | 4115 | `"            research_failed = search_outcome in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L004116](../../agents/web_agent.py#L4116) | 4116 | `"            report.update({"` | — |
| [SRC-1AE03B9EC3-L004117](../../agents/web_agent.py#L4117) | 4117 | `"                # When collection failed, an empty local list is not evidence that"` | — |
| [SRC-1AE03B9EC3-L004118](../../agents/web_agent.py#L4118) | 4118 | `"                # the remote search returned zero sources; preserve unknown counts."` | — |
| [SRC-1AE03B9EC3-L004119](../../agents/web_agent.py#L4119) | 4119 | `"                \"unique_sources\": None if research_failed else len(sources),"` | — |
| [SRC-1AE03B9EC3-L004120](../../agents/web_agent.py#L4120) | 4120 | `"                \"independent_sources\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L004121](../../agents/web_agent.py#L4121) | 4121 | `"                \"distinct_registrable_domains\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L004122](../../agents/web_agent.py#L4122) | 4122 | `"                \"pages_fetched\": ("` | — |
| [SRC-1AE03B9EC3-L004123](../../agents/web_agent.py#L4123) | 4123 | `"                    None if research_failed"` | — |
| [SRC-1AE03B9EC3-L004124](../../agents/web_agent.py#L4124) | 4124 | `"                    else sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L004125](../../agents/web_agent.py#L4125) | 4125 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004126](../../agents/web_agent.py#L4126) | 4126 | `"                \"provider_diagnostics\": current_research_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L004127](../../agents/web_agent.py#L4127) | 4127 | `"                \"insufficient_evidence\": True,"` | — |
| [SRC-1AE03B9EC3-L004128](../../agents/web_agent.py#L4128) | 4128 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L004129](../../agents/web_agent.py#L4129) | 4129 | `"                \"citation_check\": citation_validation[\"status\"],"` | — |
| [SRC-1AE03B9EC3-L004130](../../agents/web_agent.py#L4130) | 4130 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L004131](../../agents/web_agent.py#L4131) | 4131 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L004132](../../agents/web_agent.py#L4132) | 4132 | `"            })"` | — |
| [SRC-1AE03B9EC3-L004133](../../agents/web_agent.py#L4133) | 4133 | `"            return {"` | — |
| [SRC-1AE03B9EC3-L004134](../../agents/web_agent.py#L4134) | 4134 | `"                \"answer\": reason,"` | — |
| [SRC-1AE03B9EC3-L004135](../../agents/web_agent.py#L4135) | 4135 | `"                \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L004136](../../agents/web_agent.py#L4136) | 4136 | `"                \"search_query\": plan.get(\"queries\", [question])[0],"` | — |
| [SRC-1AE03B9EC3-L004137](../../agents/web_agent.py#L4137) | 4137 | `"                \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L004138](../../agents/web_agent.py#L4138) | 4138 | `"                \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L004139](../../agents/web_agent.py#L4139) | 4139 | `"                    \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L004140](../../agents/web_agent.py#L4140) | 4140 | `"                    \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L004141](../../agents/web_agent.py#L4141) | 4141 | `"                    \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L004142](../../agents/web_agent.py#L4142) | 4142 | `"                    \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L004143](../../agents/web_agent.py#L4143) | 4143 | `"                    \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L004144](../../agents/web_agent.py#L4144) | 4144 | `"                    \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L004145](../../agents/web_agent.py#L4145) | 4145 | `"                    \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L004146](../../agents/web_agent.py#L4146) | 4146 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L004147](../../agents/web_agent.py#L4147) | 4147 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L004148](../../agents/web_agent.py#L4148) | 4148 | `"                },"` | — |
| [SRC-1AE03B9EC3-L004149](../../agents/web_agent.py#L4149) | 4149 | `"                \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L004150](../../agents/web_agent.py#L4150) | 4150 | `"                \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L004151](../../agents/web_agent.py#L4151) | 4151 | `"                \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L004152](../../agents/web_agent.py#L4152) | 4152 | `"                \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L004153](../../agents/web_agent.py#L4153) | 4153 | `"                \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L004154](../../agents/web_agent.py#L4154) | 4154 | `"                \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L004155](../../agents/web_agent.py#L4155) | 4155 | `"                \"warnings\": list(dict.fromkeys(search_warnings + [reason])),"` | — |
| [SRC-1AE03B9EC3-L004156](../../agents/web_agent.py#L4156) | 4156 | `"                \"kind\": \"insufficient_evidence\","` | — |
| [SRC-1AE03B9EC3-L004157](../../agents/web_agent.py#L4157) | 4157 | `"                \"final_answer_status\": \"insufficient_evidence_no_generation\","` | — |
| [SRC-1AE03B9EC3-L004158](../../agents/web_agent.py#L4158) | 4158 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L004159](../../agents/web_agent.py#L4159) | 4159 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L004160](../../agents/web_agent.py#L4160) | 4160 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L004161](../../agents/web_agent.py#L4161) | 4161 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L004162](../../agents/web_agent.py#L4162) | 4162 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L004163](../../agents/web_agent.py#L4163) | 4163 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004164](../../agents/web_agent.py#L4164) | 4164 | `""` | — |
| [SRC-1AE03B9EC3-L004165](../../agents/web_agent.py#L4165) | 4165 | `"        answer = \"\""` | — |
| [SRC-1AE03B9EC3-L004166](../../agents/web_agent.py#L4166) | 4166 | `"        used_llm = False"` | — |
| [SRC-1AE03B9EC3-L004167](../../agents/web_agent.py#L4167) | 4167 | `"        llm_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L004168](../../agents/web_agent.py#L4168) | 4168 | `"        generation_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L004169](../../agents/web_agent.py#L4169) | 4169 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L004170](../../agents/web_agent.py#L4170) | 4170 | `"            answer = self._generate("` | — |
| [SRC-1AE03B9EC3-L004171](../../agents/web_agent.py#L4171) | 4171 | `"                question,"` | — |
| [SRC-1AE03B9EC3-L004172](../../agents/web_agent.py#L4172) | 4172 | `"                clean_history,"` | — |
| [SRC-1AE03B9EC3-L004173](../../agents/web_agent.py#L4173) | 4173 | `"                sources,"` | — |
| [SRC-1AE03B9EC3-L004174](../../agents/web_agent.py#L4174) | 4174 | `"                search_warning,"` | — |
| [SRC-1AE03B9EC3-L004175](../../agents/web_agent.py#L4175) | 4175 | `"                research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L004176](../../agents/web_agent.py#L4176) | 4176 | `"                search_report=report,"` | — |
| [SRC-1AE03B9EC3-L004177](../../agents/web_agent.py#L4177) | 4177 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004178](../../agents/web_agent.py#L4178) | 4178 | `"            used_llm = True"` | — |
| [SRC-1AE03B9EC3-L004179](../../agents/web_agent.py#L4179) | 4179 | `"            if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L004180](../../agents/web_agent.py#L4180) | 4180 | `"                existing_urls = {item.get(\"url\") for item in sources}"` | — |
| [SRC-1AE03B9EC3-L004181](../../agents/web_agent.py#L4181) | 4181 | `"                for item in self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L004182](../../agents/web_agent.py#L4182) | 4182 | `"                    if ("` | — |
| [SRC-1AE03B9EC3-L004183](../../agents/web_agent.py#L4183) | 4183 | `"                        item[\"url\"] not in existing_urls"` | — |
| [SRC-1AE03B9EC3-L004184](../../agents/web_agent.py#L4184) | 4184 | `"                        and not _blocked_source_url(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L004185](../../agents/web_agent.py#L4185) | 4185 | `"                        and _relevance_ratio("` | — |
| [SRC-1AE03B9EC3-L004186](../../agents/web_agent.py#L4186) | 4186 | `"                            question, \" \".join((item.get(\"title\", \"\"), item.get(\"snippet\", \"\")))"` | — |
| [SRC-1AE03B9EC3-L004187](../../agents/web_agent.py#L4187) | 4187 | `"                        ) >= 0.20"` | — |
| [SRC-1AE03B9EC3-L004188](../../agents/web_agent.py#L4188) | 4188 | `"                    ):"` | — |
| [SRC-1AE03B9EC3-L004189](../../agents/web_agent.py#L4189) | 4189 | `"                        sources.append(item)"` | — |
| [SRC-1AE03B9EC3-L004190](../../agents/web_agent.py#L4190) | 4190 | `"                        existing_urls.add(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L004191](../../agents/web_agent.py#L4191) | 4191 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004192](../../agents/web_agent.py#L4192) | 4192 | `"                provider_counts = dict(report.get(\"provider_counts\", {}))"` | — |
| [SRC-1AE03B9EC3-L004193](../../agents/web_agent.py#L4193) | 4193 | `"                provider_counts[\"openrouter_web_search\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L004194](../../agents/web_agent.py#L4194) | 4194 | `"                report[\"provider_counts\"] = provider_counts"` | — |
| [SRC-1AE03B9EC3-L004195](../../agents/web_agent.py#L4195) | 4195 | `"                providers_used = list(report.get(\"providers_used\", []))"` | — |
| [SRC-1AE03B9EC3-L004196](../../agents/web_agent.py#L4196) | 4196 | `"                if \"openrouter_web_search\" not in providers_used:"` | — |
| [SRC-1AE03B9EC3-L004197](../../agents/web_agent.py#L4197) | 4197 | `"                    providers_used.append(\"openrouter_web_search\")"` | — |
| [SRC-1AE03B9EC3-L004198](../../agents/web_agent.py#L4198) | 4198 | `"                report[\"providers_used\"] = providers_used"` | — |
| [SRC-1AE03B9EC3-L004199](../../agents/web_agent.py#L4199) | 4199 | `"                report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L004200](../../agents/web_agent.py#L4200) | 4200 | `"                    sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L004201](../../agents/web_agent.py#L4201) | 4201 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004202](../../agents/web_agent.py#L4202) | 4202 | `"        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L004203](../../agents/web_agent.py#L4203) | 4203 | `"            llm_warning = str(exc)"` | — |
| [SRC-1AE03B9EC3-L004204](../../agents/web_agent.py#L4204) | 4204 | `"            generation_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L004205](../../agents/web_agent.py#L4205) | 4205 | `"            if generation_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L004206](../../agents/web_agent.py#L4206) | 4206 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004207](../../agents/web_agent.py#L4207) | 4207 | `"                    \"استُنفدت ميزانية محاولات النماذج قبل اكتمال الإجابة التحليلية. \""` | — |
| [SRC-1AE03B9EC3-L004208](../../agents/web_agent.py#L4208) | 4208 | `"                    \"أعرض مقتطفات المصادر المتاحة فقط، ولا أعتبر المهمة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L004209](../../agents/web_agent.py#L4209) | 4209 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004210](../../agents/web_agent.py#L4210) | 4210 | `"            elif not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L004211](../../agents/web_agent.py#L4211) | 4211 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004212](../../agents/web_agent.py#L4212) | 4212 | `"                    \"تم البحث، لكن الفهم التوليدي غير مفعّل بعد. اضبط OPENROUTER_API_KEY \""` | — |
| [SRC-1AE03B9EC3-L004213](../../agents/web_agent.py#L4213) | 4213 | `"                    \"في Termux لتفعيل تخطيط البحث والإجابة باللغة الطبيعية.\""` | — |
| [SRC-1AE03B9EC3-L004214](../../agents/web_agent.py#L4214) | 4214 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004215](../../agents/web_agent.py#L4215) | 4215 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004216](../../agents/web_agent.py#L4216) | 4216 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004217](../../agents/web_agent.py#L4217) | 4217 | `"                    \"اكتمل البحث، لكن تعذر توليد إجابة تحليلية. أعرض لك مقتطفات المصادر \""` | — |
| [SRC-1AE03B9EC3-L004218](../../agents/web_agent.py#L4218) | 4218 | `"                    \"المتاحة بدلًا من اختلاق إجابة.\""` | — |
| [SRC-1AE03B9EC3-L004219](../../agents/web_agent.py#L4219) | 4219 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004220](../../agents/web_agent.py#L4220) | 4220 | `"            answer = _fallback_answer(sources, reason)"` | — |
| [SRC-1AE03B9EC3-L004221](../../agents/web_agent.py#L4221) | 4221 | `""` | — |
| [SRC-1AE03B9EC3-L004222](../../agents/web_agent.py#L4222) | 4222 | `"        review_status = \"not_run\""` | — |
| [SRC-1AE03B9EC3-L004223](../../agents/web_agent.py#L4223) | 4223 | `"        review_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L004224](../../agents/web_agent.py#L4224) | 4224 | `"        review_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L004225](../../agents/web_agent.py#L4225) | 4225 | `"        if used_llm and sources:"` | — |
| [SRC-1AE03B9EC3-L004226](../../agents/web_agent.py#L4226) | 4226 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L004227](../../agents/web_agent.py#L4227) | 4227 | `"                answer = self._review_answer(question, answer, sources[:MAX_LLM_CITED_SOURCES])"` | — |
| [SRC-1AE03B9EC3-L004228](../../agents/web_agent.py#L4228) | 4228 | `"                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L004229](../../agents/web_agent.py#L4229) | 4229 | `"            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L004230](../../agents/web_agent.py#L4230) | 4230 | `"                review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L004231](../../agents/web_agent.py#L4231) | 4231 | `"                review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L004232](../../agents/web_agent.py#L4232) | 4232 | `"                review_warning = ("` | — |
| [SRC-1AE03B9EC3-L004233](../../agents/web_agent.py#L4233) | 4233 | `"                    \"استُنفدت ميزانية النماذج قبل اكتمال تدقيق الإجابة؛ لذلك لن أعرض المسودة \""` | — |
| [SRC-1AE03B9EC3-L004234](../../agents/web_agent.py#L4234) | 4234 | `"                    \"بوصفها إجابة مكتملة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد عليها.\""` | — |
| [SRC-1AE03B9EC3-L004235](../../agents/web_agent.py#L4235) | 4235 | `"                    if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L004236](../../agents/web_agent.py#L4236) | 4236 | `"                    else"` | — |
| [SRC-1AE03B9EC3-L004237](../../agents/web_agent.py#L4237) | 4237 | `"                    \"تعذر تدقيق الادعاءات مقابل نصوص المصادر؛ لذلك لن أتعامل مع المسودة \""` | — |
| [SRC-1AE03B9EC3-L004238](../../agents/web_agent.py#L4238) | 4238 | `"                    \"كإجابة مؤكدة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد على المسودة.\""` | — |
| [SRC-1AE03B9EC3-L004239](../../agents/web_agent.py#L4239) | 4239 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004240](../../agents/web_agent.py#L4240) | 4240 | `"                answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L004241](../../agents/web_agent.py#L4241) | 4241 | `"        if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L004242](../../agents/web_agent.py#L4242) | 4242 | `"            answer += \"\\n\\nروابط إضافية من البحث المباشر عبر الويب:\""` | — |
| [SRC-1AE03B9EC3-L004243](../../agents/web_agent.py#L4243) | 4243 | `"            for source in self.server_search_sources[:8]:"` | — |
| [SRC-1AE03B9EC3-L004244](../../agents/web_agent.py#L4244) | 4244 | `"                answer += \"\\n- \" + source[\"title\"] + \" — \" + source[\"url\"]"` | — |
| [SRC-1AE03B9EC3-L004245](../../agents/web_agent.py#L4245) | 4245 | `"        max_citable_sources = min(MAX_LLM_CITED_SOURCES, len(sources))"` | — |
| [SRC-1AE03B9EC3-L004246](../../agents/web_agent.py#L4246) | 4246 | `"        answer, citation_warnings = self._remove_invalid_citations("` | — |
| [SRC-1AE03B9EC3-L004247](../../agents/web_agent.py#L4247) | 4247 | `"            answer, max_citable_sources"` | — |
| [SRC-1AE03B9EC3-L004248](../../agents/web_agent.py#L4248) | 4248 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004249](../../agents/web_agent.py#L4249) | 4249 | `"        citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L004250](../../agents/web_agent.py#L4250) | 4250 | `"            answer, max_citable_sources, citation_warnings, review_status"` | — |
| [SRC-1AE03B9EC3-L004251](../../agents/web_agent.py#L4251) | 4251 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004252](../../agents/web_agent.py#L4252) | 4252 | `"        report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004253](../../agents/web_agent.py#L4253) | 4253 | `"        report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L004254](../../agents/web_agent.py#L4254) | 4254 | `"        report[\"second_pass_review\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L004255](../../agents/web_agent.py#L4255) | 4255 | `"        report[\"claim_audit\"] = review_status"` | — |
| [SRC-1AE03B9EC3-L004256](../../agents/web_agent.py#L4256) | 4256 | `"        coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L004257](../../agents/web_agent.py#L4257) | 4257 | `"        answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L004258](../../agents/web_agent.py#L4258) | 4258 | `"            \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L004259](../../agents/web_agent.py#L4259) | 4259 | `"            \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L004260](../../agents/web_agent.py#L4260) | 4260 | `"            \"review_prompted\": review_status == \"model_claim_audit_completed\","` | — |
| [SRC-1AE03B9EC3-L004261](../../agents/web_agent.py#L4261) | 4261 | `"            \"status\": ("` | — |
| [SRC-1AE03B9EC3-L004262](../../agents/web_agent.py#L4262) | 4262 | `"                \"model_review_requested_not_machine_verified\""` | — |
| [SRC-1AE03B9EC3-L004263](../../agents/web_agent.py#L4263) | 4263 | `"                if coverage_targets and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L004264](../../agents/web_agent.py#L4264) | 4264 | `"                else \"review_unavailable\""` | — |
| [SRC-1AE03B9EC3-L004265](../../agents/web_agent.py#L4265) | 4265 | `"                if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L004266](../../agents/web_agent.py#L4266) | 4266 | `"                else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L004267](../../agents/web_agent.py#L4267) | 4267 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L004268](../../agents/web_agent.py#L4268) | 4268 | `"            \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L004269](../../agents/web_agent.py#L4269) | 4269 | `"        }"` | — |
| [SRC-1AE03B9EC3-L004270](../../agents/web_agent.py#L4270) | 4270 | `"        report[\"answer_coverage\"] = answer_coverage"` | — |
| [SRC-1AE03B9EC3-L004271](../../agents/web_agent.py#L4271) | 4271 | `"        report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L004272](../../agents/web_agent.py#L4272) | 4272 | `"        distinct_providers = {"` | — |
| [SRC-1AE03B9EC3-L004273](../../agents/web_agent.py#L4273) | 4273 | `"            provider for source in sources for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L004274](../../agents/web_agent.py#L4274) | 4274 | `"        }"` | — |
| [SRC-1AE03B9EC3-L004275](../../agents/web_agent.py#L4275) | 4275 | `"        distinct_domains = {"` | — |
| [SRC-1AE03B9EC3-L004276](../../agents/web_agent.py#L4276) | 4276 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L004277](../../agents/web_agent.py#L4277) | 4277 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L004278](../../agents/web_agent.py#L4278) | 4278 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L004279](../../agents/web_agent.py#L4279) | 4279 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L004280](../../agents/web_agent.py#L4280) | 4280 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004281](../../agents/web_agent.py#L4281) | 4281 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L004282](../../agents/web_agent.py#L4282) | 4282 | `"        }"` | — |
| [SRC-1AE03B9EC3-L004283](../../agents/web_agent.py#L4283) | 4283 | `"        distinct_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L004284](../../agents/web_agent.py#L4284) | 4284 | `"        fetched_pages = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L004285](../../agents/web_agent.py#L4285) | 4285 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L004286](../../agents/web_agent.py#L4286) | 4286 | `"            len(sources) >= 4 and len(distinct_domains) >= 3"` | — |
| [SRC-1AE03B9EC3-L004287](../../agents/web_agent.py#L4287) | 4287 | `"            and len(distinct_providers) >= 2 and fetched_pages >= 1"` | — |
| [SRC-1AE03B9EC3-L004288](../../agents/web_agent.py#L4288) | 4288 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L004289](../../agents/web_agent.py#L4289) | 4289 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L004290](../../agents/web_agent.py#L4290) | 4290 | `"            research_quality = \"excellent\""` | — |
| [SRC-1AE03B9EC3-L004291](../../agents/web_agent.py#L4291) | 4291 | `"        elif ("` | — |
| [SRC-1AE03B9EC3-L004292](../../agents/web_agent.py#L4292) | 4292 | `"            len(sources) >= 2 and len(distinct_domains) >= 2"` | — |
| [SRC-1AE03B9EC3-L004293](../../agents/web_agent.py#L4293) | 4293 | `"            and (len(distinct_providers) >= 2 or fetched_pages >= 1)"` | — |
| [SRC-1AE03B9EC3-L004294](../../agents/web_agent.py#L4294) | 4294 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L004295](../../agents/web_agent.py#L4295) | 4295 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L004296](../../agents/web_agent.py#L4296) | 4296 | `"            research_quality = \"good\""` | — |
