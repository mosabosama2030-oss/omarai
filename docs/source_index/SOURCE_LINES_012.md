# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **012**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L002490 إلى SRC-1AE03B9EC3-L003289
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L002490](../../agents/web_agent.py#L2490) | 2490 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002491](../../agents/web_agent.py#L2491) | 2491 | `"        preliminary_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L002492](../../agents/web_agent.py#L2492) | 2492 | `"        preliminary_providers = {"` | — |
| [SRC-1AE03B9EC3-L002493](../../agents/web_agent.py#L2493) | 2493 | `"            provider for item in preliminary for provider in item.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L002494](../../agents/web_agent.py#L2494) | 2494 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002495](../../agents/web_agent.py#L2495) | 2495 | `"        needs_expansion = ("` | — |
| [SRC-1AE03B9EC3-L002496](../../agents/web_agent.py#L2496) | 2496 | `"            plan.get(\"depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L002497](../../agents/web_agent.py#L2497) | 2497 | `"            and (len(preliminary) < 8 or len(preliminary_domains) < 5 or len(preliminary_providers) < 2)"` | — |
| [SRC-1AE03B9EC3-L002498](../../agents/web_agent.py#L2498) | 2498 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002499](../../agents/web_agent.py#L2499) | 2499 | `"        preliminary_ledger = build_evidence_ledger(target_aspects, preliminary)"` | — |
| [SRC-1AE03B9EC3-L002500](../../agents/web_agent.py#L2500) | 2500 | `"        missing_aspects = list(preliminary_ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L002501](../../agents/web_agent.py#L2501) | 2501 | `"        expansion_queries: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002502](../../agents/web_agent.py#L2502) | 2502 | `"        # Do not issue generic repairs when a standard task already has per-requirement queries."` | — |
| [SRC-1AE03B9EC3-L002503](../../agents/web_agent.py#L2503) | 2503 | `"        # Legacy plans without those query records still need the bounded missing-aspect fallback;"` | — |
| [SRC-1AE03B9EC3-L002504](../../agents/web_agent.py#L2504) | 2504 | `"        # deep research may expand further even after targeted queries."` | — |
| [SRC-1AE03B9EC3-L002505](../../agents/web_agent.py#L2505) | 2505 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L002506](../../agents/web_agent.py#L2506) | 2506 | `"            (missing_aspects or needs_expansion)"` | — |
| [SRC-1AE03B9EC3-L002507](../../agents/web_agent.py#L2507) | 2507 | `"            and len(queries) < query_limit"` | — |
| [SRC-1AE03B9EC3-L002508](../../agents/web_agent.py#L2508) | 2508 | `"            and queries"` | — |
| [SRC-1AE03B9EC3-L002509](../../agents/web_agent.py#L2509) | 2509 | `"            and ("` | — |
| [SRC-1AE03B9EC3-L002510](../../agents/web_agent.py#L2510) | 2510 | `"                not plan.get(\"requirement_queries\")"` | — |
| [SRC-1AE03B9EC3-L002511](../../agents/web_agent.py#L2511) | 2511 | `"                or plan.get(\"depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L002512](../../agents/web_agent.py#L2512) | 2512 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002513](../../agents/web_agent.py#L2513) | 2513 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L002514](../../agents/web_agent.py#L2514) | 2514 | `"            base_query = (queries[0] if queries else \"\")"` | — |
| [SRC-1AE03B9EC3-L002515](../../agents/web_agent.py#L2515) | 2515 | `"            remaining_slots = max(0, query_limit - len(queries))"` | — |
| [SRC-1AE03B9EC3-L002516](../../agents/web_agent.py#L2516) | 2516 | `"            aspect_queries = repair_queries_for_missing_aspects("` | — |
| [SRC-1AE03B9EC3-L002517](../../agents/web_agent.py#L2517) | 2517 | `"                base_query,"` | — |
| [SRC-1AE03B9EC3-L002518](../../agents/web_agent.py#L2518) | 2518 | `"                missing_aspects,"` | — |
| [SRC-1AE03B9EC3-L002519](../../agents/web_agent.py#L2519) | 2519 | `"                limit=min(repair_slot_limit, remaining_slots),"` | — |
| [SRC-1AE03B9EC3-L002520](../../agents/web_agent.py#L2520) | 2520 | `"                compact_fn=compact_search_query,"` | — |
| [SRC-1AE03B9EC3-L002521](../../agents/web_agent.py#L2521) | 2521 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002522](../../agents/web_agent.py#L2522) | 2522 | `"            candidates = list(aspect_queries)"` | — |
| [SRC-1AE03B9EC3-L002523](../../agents/web_agent.py#L2523) | 2523 | `"            if needs_expansion:"` | — |
| [SRC-1AE03B9EC3-L002524](../../agents/web_agent.py#L2524) | 2524 | `"                candidates.extend(["` | — |
| [SRC-1AE03B9EC3-L002525](../../agents/web_agent.py#L2525) | 2525 | `"                    f\"{base_query} official sources data reports\","` | — |
| [SRC-1AE03B9EC3-L002526](../../agents/web_agent.py#L2526) | 2526 | `"                    f\"{base_query} limitations risks criticism alternatives\","` | — |
| [SRC-1AE03B9EC3-L002527](../../agents/web_agent.py#L2527) | 2527 | `"                    f\"{base_query} recent developments case studies analysis\","` | — |
| [SRC-1AE03B9EC3-L002528](../../agents/web_agent.py#L2528) | 2528 | `"                ])"` | — |
| [SRC-1AE03B9EC3-L002529](../../agents/web_agent.py#L2529) | 2529 | `"            existing = {item.casefold() for item in queries}"` | — |
| [SRC-1AE03B9EC3-L002530](../../agents/web_agent.py#L2530) | 2530 | `"            expansion_queries = []"` | — |
| [SRC-1AE03B9EC3-L002531](../../agents/web_agent.py#L2531) | 2531 | `"            seen_expansions = set(existing)"` | — |
| [SRC-1AE03B9EC3-L002532](../../agents/web_agent.py#L2532) | 2532 | `"            for candidate in candidates:"` | — |
| [SRC-1AE03B9EC3-L002533](../../agents/web_agent.py#L2533) | 2533 | `"                compacted = compact_search_query(candidate)"` | — |
| [SRC-1AE03B9EC3-L002534](../../agents/web_agent.py#L2534) | 2534 | `"                key = compacted.casefold()"` | — |
| [SRC-1AE03B9EC3-L002535](../../agents/web_agent.py#L2535) | 2535 | `"                if compacted and key not in seen_expansions:"` | — |
| [SRC-1AE03B9EC3-L002536](../../agents/web_agent.py#L2536) | 2536 | `"                    expansion_queries.append(compacted)"` | — |
| [SRC-1AE03B9EC3-L002537](../../agents/web_agent.py#L2537) | 2537 | `"                    seen_expansions.add(key)"` | — |
| [SRC-1AE03B9EC3-L002538](../../agents/web_agent.py#L2538) | 2538 | `"                if len(expansion_queries) >= remaining_slots:"` | — |
| [SRC-1AE03B9EC3-L002539](../../agents/web_agent.py#L2539) | 2539 | `"                    break"` | — |
| [SRC-1AE03B9EC3-L002540](../../agents/web_agent.py#L2540) | 2540 | `"            if expansion_queries:"` | — |
| [SRC-1AE03B9EC3-L002541](../../agents/web_agent.py#L2541) | 2541 | `"                with ThreadPoolExecutor("` | — |
| [SRC-1AE03B9EC3-L002542](../../agents/web_agent.py#L2542) | 2542 | `"                    max_workers=min(MAX_RESEARCH_WORKERS, len(expansion_queries))"` | — |
| [SRC-1AE03B9EC3-L002543](../../agents/web_agent.py#L2543) | 2543 | `"                ) as pool:"` | — |
| [SRC-1AE03B9EC3-L002544](../../agents/web_agent.py#L2544) | 2544 | `"                    futures = {"` | — |
| [SRC-1AE03B9EC3-L002545](../../agents/web_agent.py#L2545) | 2545 | `"                        pool.submit(self._search_web, query): query"` | — |
| [SRC-1AE03B9EC3-L002546](../../agents/web_agent.py#L2546) | 2546 | `"                        for query in expansion_queries"` | — |
| [SRC-1AE03B9EC3-L002547](../../agents/web_agent.py#L2547) | 2547 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L002548](../../agents/web_agent.py#L2548) | 2548 | `"                    for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002549](../../agents/web_agent.py#L2549) | 2549 | `"                        query = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002550](../../agents/web_agent.py#L2550) | 2550 | `"                        search_started_queries += 1"` | — |
| [SRC-1AE03B9EC3-L002551](../../agents/web_agent.py#L2551) | 2551 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L002552](../../agents/web_agent.py#L2552) | 2552 | `"                            results = future.result()"` | — |
| [SRC-1AE03B9EC3-L002553](../../agents/web_agent.py#L2553) | 2553 | `"                        except (RequestBudgetExceeded, RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002554](../../agents/web_agent.py#L2554) | 2554 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002555](../../agents/web_agent.py#L2555) | 2555 | `"                                f\"تعذر بحث زاوية إضافية «{query[:70]}»: {exc}\""` | — |
| [SRC-1AE03B9EC3-L002556](../../agents/web_agent.py#L2556) | 2556 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002557](../../agents/web_agent.py#L2557) | 2557 | `"                            query_counts.append({\"query\": query, \"results\": 0})"` | — |
| [SRC-1AE03B9EC3-L002558](../../agents/web_agent.py#L2558) | 2558 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002559](../../agents/web_agent.py#L2559) | 2559 | `"                        query_counts.append({\"query\": query, \"results\": len(results)})"` | — |
| [SRC-1AE03B9EC3-L002560](../../agents/web_agent.py#L2560) | 2560 | `"                        grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002561](../../agents/web_agent.py#L2561) | 2561 | `"                        for source in results:"` | — |
| [SRC-1AE03B9EC3-L002562](../../agents/web_agent.py#L2562) | 2562 | `"                            grouped.setdefault("` | — |
| [SRC-1AE03B9EC3-L002563](../../agents/web_agent.py#L2563) | 2563 | `"                                str(source.get(\"provider\") or \"web_search\"), []"` | — |
| [SRC-1AE03B9EC3-L002564](../../agents/web_agent.py#L2564) | 2564 | `"                            ).append(source)"` | — |
| [SRC-1AE03B9EC3-L002565](../../agents/web_agent.py#L2565) | 2565 | `"                        for provider, items in grouped.items():"` | — |
| [SRC-1AE03B9EC3-L002566](../../agents/web_agent.py#L2566) | 2566 | `"                            items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002567](../../agents/web_agent.py#L2567) | 2567 | `"                            batches.append({"` | — |
| [SRC-1AE03B9EC3-L002568](../../agents/web_agent.py#L2568) | 2568 | `"                                \"query\": query, \"provider\": provider, \"results\": items"` | — |
| [SRC-1AE03B9EC3-L002569](../../agents/web_agent.py#L2569) | 2569 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L002570](../../agents/web_agent.py#L2570) | 2570 | `"                queries.extend(expansion_queries)"` | — |
| [SRC-1AE03B9EC3-L002571](../../agents/web_agent.py#L2571) | 2571 | `"        # Report queries actually selected, not planned queries skipped to reserve repair capacity."` | — |
| [SRC-1AE03B9EC3-L002572](../../agents/web_agent.py#L2572) | 2572 | `"        plan[\"queries\"] = list(dict.fromkeys(queries))"` | — |
| [SRC-1AE03B9EC3-L002573](../../agents/web_agent.py#L2573) | 2573 | `""` | — |
| [SRC-1AE03B9EC3-L002574](../../agents/web_agent.py#L2574) | 2574 | `"        # Google News RSS is included concurrently by _search_web for freshness-bearing queries."` | — |
| [SRC-1AE03B9EC3-L002575](../../agents/web_agent.py#L2575) | 2575 | `""` | — |
| [SRC-1AE03B9EC3-L002576](../../agents/web_agent.py#L2576) | 2576 | `"        # A social-focused task uses public social endpoints in parallel with indexed"` | — |
| [SRC-1AE03B9EC3-L002577](../../agents/web_agent.py#L2577) | 2577 | `"        # public pages. No login, private profile, session cookie or anti-bot bypass."` | — |
| [SRC-1AE03B9EC3-L002578](../../agents/web_agent.py#L2578) | 2578 | `"        social_results: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002579](../../agents/web_agent.py#L2579) | 2579 | `"        if plan.get(\"social_focus\") and queries:"` | — |
| [SRC-1AE03B9EC3-L002580](../../agents/web_agent.py#L2580) | 2580 | `"            requested_platforms = plan.get(\"platforms\") or []"` | — |
| [SRC-1AE03B9EC3-L002581](../../agents/web_agent.py#L2581) | 2581 | `"            if requested_platforms:"` | — |
| [SRC-1AE03B9EC3-L002582](../../agents/web_agent.py#L2582) | 2582 | `"                platforms = list(dict.fromkeys(requested_platforms))"` | — |
| [SRC-1AE03B9EC3-L002583](../../agents/web_agent.py#L2583) | 2583 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002584](../../agents/web_agent.py#L2584) | 2584 | `"                # Broad social research: always try no-key public sources, and add"` | — |
| [SRC-1AE03B9EC3-L002585](../../agents/web_agent.py#L2585) | 2585 | `"                # official platform connectors only when they are configured."` | — |
| [SRC-1AE03B9EC3-L002586](../../agents/web_agent.py#L2586) | 2586 | `"                platforms = [\"reddit\", \"bluesky\"]"` | — |
| [SRC-1AE03B9EC3-L002587](../../agents/web_agent.py#L2587) | 2587 | `"                optional_connectors = {"` | — |
| [SRC-1AE03B9EC3-L002588](../../agents/web_agent.py#L2588) | 2588 | `"                    \"facebook\": bool("` | — |
| [SRC-1AE03B9EC3-L002589](../../agents/web_agent.py#L2589) | 2589 | `"                        os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002590](../../agents/web_agent.py#L2590) | 2590 | `"                        and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002591](../../agents/web_agent.py#L2591) | 2591 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L002592](../../agents/web_agent.py#L2592) | 2592 | `"                    \"instagram\": bool("` | — |
| [SRC-1AE03B9EC3-L002593](../../agents/web_agent.py#L2593) | 2593 | `"                        os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002594](../../agents/web_agent.py#L2594) | 2594 | `"                        and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002595](../../agents/web_agent.py#L2595) | 2595 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L002596](../../agents/web_agent.py#L2596) | 2596 | `"                    \"x\": bool(os.getenv(\"X_BEARER_TOKEN\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L002597](../../agents/web_agent.py#L2597) | 2597 | `"                    \"youtube\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L002598](../../agents/web_agent.py#L2598) | 2598 | `"                }"` | — |
| [SRC-1AE03B9EC3-L002599](../../agents/web_agent.py#L2599) | 2599 | `"                platforms.extend("` | — |
| [SRC-1AE03B9EC3-L002600](../../agents/web_agent.py#L2600) | 2600 | `"                    name for name, ready in optional_connectors.items()"` | — |
| [SRC-1AE03B9EC3-L002601](../../agents/web_agent.py#L2601) | 2601 | `"                    if ready and name not in platforms"` | — |
| [SRC-1AE03B9EC3-L002602](../../agents/web_agent.py#L2602) | 2602 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002603](../../agents/web_agent.py#L2603) | 2603 | `"            social_results, social_warnings = self._search_social((queries[0] if queries else \"\"), platforms)"` | — |
| [SRC-1AE03B9EC3-L002604](../../agents/web_agent.py#L2604) | 2604 | `"            warnings.extend(social_warnings)"` | — |
| [SRC-1AE03B9EC3-L002605](../../agents/web_agent.py#L2605) | 2605 | `"            social_groups: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002606](../../agents/web_agent.py#L2606) | 2606 | `"            for source in social_results:"` | — |
| [SRC-1AE03B9EC3-L002607](../../agents/web_agent.py#L2607) | 2607 | `"                social_groups.setdefault(str(source.get(\"provider\") or \"social\"), []).append(source)"` | — |
| [SRC-1AE03B9EC3-L002608](../../agents/web_agent.py#L2608) | 2608 | `"            for provider, items in social_groups.items():"` | — |
| [SRC-1AE03B9EC3-L002609](../../agents/web_agent.py#L2609) | 2609 | `"                items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002610](../../agents/web_agent.py#L2610) | 2610 | `"                batches.append({\"query\": (queries[0] if queries else \"\"), \"provider\": provider, \"results\": items})"` | — |
| [SRC-1AE03B9EC3-L002611](../../agents/web_agent.py#L2611) | 2611 | `""` | — |
| [SRC-1AE03B9EC3-L002612](../../agents/web_agent.py#L2612) | 2612 | `"        # Explicit URLs are first-class inputs: fetch the page the user actually asked about"` | — |
| [SRC-1AE03B9EC3-L002613](../../agents/web_agent.py#L2613) | 2613 | `"        # instead of relying on a search engine to rediscover it. URL and DNS checks still apply."` | — |
| [SRC-1AE03B9EC3-L002614](../../agents/web_agent.py#L2614) | 2614 | `"        direct_urls: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002615](../../agents/web_agent.py#L2615) | 2615 | `"        for value in plan.get(\"direct_urls\", [])[:5]:"` | — |
| [SRC-1AE03B9EC3-L002616](../../agents/web_agent.py#L2616) | 2616 | `"            safe_url = _public_http_url(value)"` | — |
| [SRC-1AE03B9EC3-L002617](../../agents/web_agent.py#L2617) | 2617 | `"            if safe_url and not _blocked_source_url(safe_url) and safe_url not in direct_urls:"` | — |
| [SRC-1AE03B9EC3-L002618](../../agents/web_agent.py#L2618) | 2618 | `"                direct_urls.append(safe_url)"` | — |
| [SRC-1AE03B9EC3-L002619](../../agents/web_agent.py#L2619) | 2619 | `"        for direct_url in direct_urls:"` | — |
| [SRC-1AE03B9EC3-L002620](../../agents/web_agent.py#L2620) | 2620 | `"            batches.append({"` | — |
| [SRC-1AE03B9EC3-L002621](../../agents/web_agent.py#L2621) | 2621 | `"                \"query\": (queries[0] if queries else \"\"),"` | — |
| [SRC-1AE03B9EC3-L002622](../../agents/web_agent.py#L2622) | 2622 | `"                \"provider\": \"user_supplied_url\","` | — |
| [SRC-1AE03B9EC3-L002623](../../agents/web_agent.py#L2623) | 2623 | `"                \"results\": [{"` | — |
| [SRC-1AE03B9EC3-L002624](../../agents/web_agent.py#L2624) | 2624 | `"                    \"title\": \"رابط قدمه المستخدم للتحليل\","` | — |
| [SRC-1AE03B9EC3-L002625](../../agents/web_agent.py#L2625) | 2625 | `"                    \"url\": direct_url,"` | — |
| [SRC-1AE03B9EC3-L002626](../../agents/web_agent.py#L2626) | 2626 | `"                    \"snippet\": \"\","` | — |
| [SRC-1AE03B9EC3-L002627](../../agents/web_agent.py#L2627) | 2627 | `"                    \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002628](../../agents/web_agent.py#L2628) | 2628 | `"                    \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002629](../../agents/web_agent.py#L2629) | 2629 | `"                    \"provider\": \"user_supplied_url\","` | — |
| [SRC-1AE03B9EC3-L002630](../../agents/web_agent.py#L2630) | 2630 | `"                    \"provider_rank\": 1,"` | — |
| [SRC-1AE03B9EC3-L002631](../../agents/web_agent.py#L2631) | 2631 | `"                    \"search_query\": (queries[0] if queries else \"\"),"` | — |
| [SRC-1AE03B9EC3-L002632](../../agents/web_agent.py#L2632) | 2632 | `"                    \"published_at\": \"\","` | — |
| [SRC-1AE03B9EC3-L002633](../../agents/web_agent.py#L2633) | 2633 | `"                }],"` | — |
| [SRC-1AE03B9EC3-L002634](../../agents/web_agent.py#L2634) | 2634 | `"            })"` | — |
| [SRC-1AE03B9EC3-L002635](../../agents/web_agent.py#L2635) | 2635 | `""` | — |
| [SRC-1AE03B9EC3-L002636](../../agents/web_agent.py#L2636) | 2636 | `"        raw_results_count = sum(len(batch.get(\"results\", [])) for batch in batches if isinstance(batch, dict) and isinstance(batch.get(\"results\", []), list))"` | — |
| [SRC-1AE03B9EC3-L002637](../../agents/web_agent.py#L2637) | 2637 | `"        sources = fuse_ranked_results(batches, limit=MAX_SEARCH_RESULTS)"` | — |
| [SRC-1AE03B9EC3-L002638](../../agents/web_agent.py#L2638) | 2638 | `""` | — |
| [SRC-1AE03B9EC3-L002639](../../agents/web_agent.py#L2639) | 2639 | `"        # Keep at least one returned source per explicit criterion query in the"` | — |
| [SRC-1AE03B9EC3-L002640](../../agents/web_agent.py#L2640) | 2640 | `"        # bounded source set sent to synthesis. Global fusion can otherwise crowd"` | — |
| [SRC-1AE03B9EC3-L002641](../../agents/web_agent.py#L2641) | 2641 | `"        # lower-ranked criterion results out before the model can inspect them."` | — |
| [SRC-1AE03B9EC3-L002642](../../agents/web_agent.py#L2642) | 2642 | `"        requirement_queries = plan.get(\"requirement_queries\", [])"` | — |
| [SRC-1AE03B9EC3-L002643](../../agents/web_agent.py#L2643) | 2643 | `"        if isinstance(requirement_queries, list) and requirement_queries:"` | — |
| [SRC-1AE03B9EC3-L002644](../../agents/web_agent.py#L2644) | 2644 | `"            globally_fused = sources"` | — |
| [SRC-1AE03B9EC3-L002645](../../agents/web_agent.py#L2645) | 2645 | `"            globally_fused_by_url = {"` | — |
| [SRC-1AE03B9EC3-L002646](../../agents/web_agent.py#L2646) | 2646 | `"                self._normalized_source_url_key(item.get(\"url\", \"\")): item"` | — |
| [SRC-1AE03B9EC3-L002647](../../agents/web_agent.py#L2647) | 2647 | `"                for item in globally_fused"` | — |
| [SRC-1AE03B9EC3-L002648](../../agents/web_agent.py#L2648) | 2648 | `"                if self._normalized_source_url_key(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002649](../../agents/web_agent.py#L2649) | 2649 | `"            }"` | — |
| [SRC-1AE03B9EC3-L002650](../../agents/web_agent.py#L2650) | 2650 | `"            pinned_by_url: dict[str, dict[str, Any]] = {}"` | — |
| [SRC-1AE03B9EC3-L002651](../../agents/web_agent.py#L2651) | 2651 | `"            pinned_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002652](../../agents/web_agent.py#L2652) | 2652 | `"            for requirement in requirement_queries[:MAX_PLAN_QUERIES]:"` | — |
| [SRC-1AE03B9EC3-L002653](../../agents/web_agent.py#L2653) | 2653 | `"                if not isinstance(requirement, dict):"` | — |
| [SRC-1AE03B9EC3-L002654](../../agents/web_agent.py#L2654) | 2654 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002655](../../agents/web_agent.py#L2655) | 2655 | `"                target_query = compact_search_query(str(requirement.get(\"query\") or \"\"))"` | — |
| [SRC-1AE03B9EC3-L002656](../../agents/web_agent.py#L2656) | 2656 | `"                if not target_query:"` | — |
| [SRC-1AE03B9EC3-L002657](../../agents/web_agent.py#L2657) | 2657 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002658](../../agents/web_agent.py#L2658) | 2658 | `"                query_key = re.sub(r\"\\s+\", \" \", target_query).strip().casefold()"` | — |
| [SRC-1AE03B9EC3-L002659](../../agents/web_agent.py#L2659) | 2659 | `"                criterion_batches = ["` | — |
| [SRC-1AE03B9EC3-L002660](../../agents/web_agent.py#L2660) | 2660 | `"                    batch for batch in batches"` | — |
| [SRC-1AE03B9EC3-L002661](../../agents/web_agent.py#L2661) | 2661 | `"                    if re.sub("` | — |
| [SRC-1AE03B9EC3-L002662](../../agents/web_agent.py#L2662) | 2662 | `"                        r\"\\s+\", \" \", str(batch.get(\"query\") or \"\")"` | — |
| [SRC-1AE03B9EC3-L002663](../../agents/web_agent.py#L2663) | 2663 | `"                    ).strip().casefold() == query_key"` | — |
| [SRC-1AE03B9EC3-L002664](../../agents/web_agent.py#L2664) | 2664 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L002665](../../agents/web_agent.py#L2665) | 2665 | `"                criterion_candidates = fuse_ranked_results("` | — |
| [SRC-1AE03B9EC3-L002666](../../agents/web_agent.py#L2666) | 2666 | `"                    criterion_batches, limit=MAX_SEARCH_RESULTS"` | — |
| [SRC-1AE03B9EC3-L002667](../../agents/web_agent.py#L2667) | 2667 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002668](../../agents/web_agent.py#L2668) | 2668 | `"                candidate = None"` | — |
| [SRC-1AE03B9EC3-L002669](../../agents/web_agent.py#L2669) | 2669 | `"                if criterion_candidates:"` | — |
| [SRC-1AE03B9EC3-L002670](../../agents/web_agent.py#L2670) | 2670 | `"                    criterion_ledger = build_requirement_evidence_ledger("` | — |
| [SRC-1AE03B9EC3-L002671](../../agents/web_agent.py#L2671) | 2671 | `"                        [str(requirement.get(\"target\") or \"\")],"` | — |
| [SRC-1AE03B9EC3-L002672](../../agents/web_agent.py#L2672) | 2672 | `"                        criterion_candidates,"` | — |
| [SRC-1AE03B9EC3-L002673](../../agents/web_agent.py#L2673) | 2673 | `"                        [requirement],"` | — |
| [SRC-1AE03B9EC3-L002674](../../agents/web_agent.py#L2674) | 2674 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002675](../../agents/web_agent.py#L2675) | 2675 | `"                    candidate_indexes = ("` | — |
| [SRC-1AE03B9EC3-L002676](../../agents/web_agent.py#L2676) | 2676 | `"                        criterion_ledger[0].get(\"candidate_source_indexes\", [])"` | — |
| [SRC-1AE03B9EC3-L002677](../../agents/web_agent.py#L2677) | 2677 | `"                        if criterion_ledger else []"` | — |
| [SRC-1AE03B9EC3-L002678](../../agents/web_agent.py#L2678) | 2678 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002679](../../agents/web_agent.py#L2679) | 2679 | `"                    if candidate_indexes:"` | — |
| [SRC-1AE03B9EC3-L002680](../../agents/web_agent.py#L2680) | 2680 | `"                        candidate = criterion_candidates[int(candidate_indexes[0]) - 1]"` | — |
| [SRC-1AE03B9EC3-L002681](../../agents/web_agent.py#L2681) | 2681 | `"                if candidate is None:"` | — |
| [SRC-1AE03B9EC3-L002682](../../agents/web_agent.py#L2682) | 2682 | `"                    candidate = next("` | — |
| [SRC-1AE03B9EC3-L002683](../../agents/web_agent.py#L2683) | 2683 | `"                        ("` | — |
| [SRC-1AE03B9EC3-L002684](../../agents/web_agent.py#L2684) | 2684 | `"                            item for item in globally_fused"` | — |
| [SRC-1AE03B9EC3-L002685](../../agents/web_agent.py#L2685) | 2685 | `"                            if query_key in {"` | — |
| [SRC-1AE03B9EC3-L002686](../../agents/web_agent.py#L2686) | 2686 | `"                                re.sub(r\"\\s+\", \" \", str(value)).strip().casefold()"` | — |
| [SRC-1AE03B9EC3-L002687](../../agents/web_agent.py#L2687) | 2687 | `"                                for value in item.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L002688](../../agents/web_agent.py#L2688) | 2688 | `"                            }"` | — |
| [SRC-1AE03B9EC3-L002689](../../agents/web_agent.py#L2689) | 2689 | `"                        ),"` | — |
| [SRC-1AE03B9EC3-L002690](../../agents/web_agent.py#L2690) | 2690 | `"                        criterion_candidates[0] if criterion_candidates else None,"` | — |
| [SRC-1AE03B9EC3-L002691](../../agents/web_agent.py#L2691) | 2691 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002692](../../agents/web_agent.py#L2692) | 2692 | `"                if not candidate:"` | — |
| [SRC-1AE03B9EC3-L002693](../../agents/web_agent.py#L2693) | 2693 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002694](../../agents/web_agent.py#L2694) | 2694 | `"                source_key = self._normalized_source_url_key(candidate.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002695](../../agents/web_agent.py#L2695) | 2695 | `"                if not source_key:"` | — |
| [SRC-1AE03B9EC3-L002696](../../agents/web_agent.py#L2696) | 2696 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002697](../../agents/web_agent.py#L2697) | 2697 | `"                selected = ("` | — |
| [SRC-1AE03B9EC3-L002698](../../agents/web_agent.py#L2698) | 2698 | `"                    pinned_by_url.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L002699](../../agents/web_agent.py#L2699) | 2699 | `"                    or globally_fused_by_url.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L002700](../../agents/web_agent.py#L2700) | 2700 | `"                    or candidate"` | — |
| [SRC-1AE03B9EC3-L002701](../../agents/web_agent.py#L2701) | 2701 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002702](../../agents/web_agent.py#L2702) | 2702 | `"                if source_key not in pinned_by_url:"` | — |
| [SRC-1AE03B9EC3-L002703](../../agents/web_agent.py#L2703) | 2703 | `"                    pinned_by_url[source_key] = selected"` | — |
| [SRC-1AE03B9EC3-L002704](../../agents/web_agent.py#L2704) | 2704 | `"                    pinned_sources.append(selected)"` | — |
| [SRC-1AE03B9EC3-L002705](../../agents/web_agent.py#L2705) | 2705 | `"                selected_queries = selected.setdefault(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L002706](../../agents/web_agent.py#L2706) | 2706 | `"                if target_query not in selected_queries:"` | — |
| [SRC-1AE03B9EC3-L002707](../../agents/web_agent.py#L2707) | 2707 | `"                    selected_queries.append(target_query)"` | — |
| [SRC-1AE03B9EC3-L002708](../../agents/web_agent.py#L2708) | 2708 | `"            pinned_keys = set(pinned_by_url)"` | — |
| [SRC-1AE03B9EC3-L002709](../../agents/web_agent.py#L2709) | 2709 | `"            sources = ("` | — |
| [SRC-1AE03B9EC3-L002710](../../agents/web_agent.py#L2710) | 2710 | `"                pinned_sources"` | — |
| [SRC-1AE03B9EC3-L002711](../../agents/web_agent.py#L2711) | 2711 | `"                + ["` | — |
| [SRC-1AE03B9EC3-L002712](../../agents/web_agent.py#L2712) | 2712 | `"                    item for item in globally_fused"` | — |
| [SRC-1AE03B9EC3-L002713](../../agents/web_agent.py#L2713) | 2713 | `"                    if self._normalized_source_url_key(item.get(\"url\", \"\")) not in pinned_keys"` | — |
| [SRC-1AE03B9EC3-L002714](../../agents/web_agent.py#L2714) | 2714 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L002715](../../agents/web_agent.py#L2715) | 2715 | `"            )[:MAX_SEARCH_RESULTS]"` | — |
| [SRC-1AE03B9EC3-L002716](../../agents/web_agent.py#L2716) | 2716 | `""` | — |
| [SRC-1AE03B9EC3-L002717](../../agents/web_agent.py#L2717) | 2717 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L002718](../../agents/web_agent.py#L2718) | 2718 | `"            source.setdefault(\"page_fetch_status\", \"not_attempted\")"` | — |
| [SRC-1AE03B9EC3-L002719](../../agents/web_agent.py#L2719) | 2719 | `"        # Fetch page text only for the best few public URLs; do it concurrently with strict bounds."` | — |
| [SRC-1AE03B9EC3-L002720](../../agents/web_agent.py#L2720) | 2720 | `"        fetch_targets = sources[:MAX_FETCHED_PAGES]"` | — |
| [SRC-1AE03B9EC3-L002721](../../agents/web_agent.py#L2721) | 2721 | `"        for source in fetch_targets:"` | — |
| [SRC-1AE03B9EC3-L002722](../../agents/web_agent.py#L2722) | 2722 | `"            source[\"page_fetch_status\"] = \"attempted\""` | — |
| [SRC-1AE03B9EC3-L002723](../../agents/web_agent.py#L2723) | 2723 | `"        fetched_count = 0"` | — |
| [SRC-1AE03B9EC3-L002724](../../agents/web_agent.py#L2724) | 2724 | `"        if fetch_targets:"` | — |
| [SRC-1AE03B9EC3-L002725](../../agents/web_agent.py#L2725) | 2725 | `"            with ThreadPoolExecutor(max_workers=min(4, len(fetch_targets))) as pool:"` | — |
| [SRC-1AE03B9EC3-L002726](../../agents/web_agent.py#L2726) | 2726 | `"                futures = {"` | — |
| [SRC-1AE03B9EC3-L002727](../../agents/web_agent.py#L2727) | 2727 | `"                    pool.submit(self._fetch_page, source[\"url\"]): source"` | — |
| [SRC-1AE03B9EC3-L002728](../../agents/web_agent.py#L2728) | 2728 | `"                    for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L002729](../../agents/web_agent.py#L2729) | 2729 | `"                }"` | — |
| [SRC-1AE03B9EC3-L002730](../../agents/web_agent.py#L2730) | 2730 | `"                for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002731](../../agents/web_agent.py#L2731) | 2731 | `"                    source = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002732](../../agents/web_agent.py#L2732) | 2732 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002733](../../agents/web_agent.py#L2733) | 2733 | `"                        fetch_result = future.result()"` | — |
| [SRC-1AE03B9EC3-L002734](../../agents/web_agent.py#L2734) | 2734 | `"                    except RequestBudgetExceeded as exc:"` | — |
| [SRC-1AE03B9EC3-L002735](../../agents/web_agent.py#L2735) | 2735 | `"                        source[\"page_fetch_status\"] = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L002736](../../agents/web_agent.py#L2736) | 2736 | `"                        source[\"page_fetch_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L002737](../../agents/web_agent.py#L2737) | 2737 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002738](../../agents/web_agent.py#L2738) | 2738 | `"                    except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002739](../../agents/web_agent.py#L2739) | 2739 | `"                        source[\"page_fetch_status\"] = \"fetch_failed\""` | — |
| [SRC-1AE03B9EC3-L002740](../../agents/web_agent.py#L2740) | 2740 | `"                        source[\"page_fetch_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L002741](../../agents/web_agent.py#L2741) | 2741 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002742](../../agents/web_agent.py#L2742) | 2742 | `"                    title, page_text = fetch_result"` | — |
| [SRC-1AE03B9EC3-L002743](../../agents/web_agent.py#L2743) | 2743 | `"                    observed_status = getattr(fetch_result, \"status\", None)"` | — |
| [SRC-1AE03B9EC3-L002744](../../agents/web_agent.py#L2744) | 2744 | `"                    error_class = getattr(fetch_result, \"error_class\", None)"` | — |
| [SRC-1AE03B9EC3-L002745](../../agents/web_agent.py#L2745) | 2745 | `"                    if title:"` | — |
| [SRC-1AE03B9EC3-L002746](../../agents/web_agent.py#L2746) | 2746 | `"                        source[\"title\"] = title"` | — |
| [SRC-1AE03B9EC3-L002747](../../agents/web_agent.py#L2747) | 2747 | `"                    if page_text and page_text.strip():"` | — |
| [SRC-1AE03B9EC3-L002748](../../agents/web_agent.py#L2748) | 2748 | `"                        source[\"page_text\"] = page_text"` | — |
| [SRC-1AE03B9EC3-L002749](../../agents/web_agent.py#L2749) | 2749 | `"                        source[\"snippet\"] = page_text[:1800]"` | — |
| [SRC-1AE03B9EC3-L002750](../../agents/web_agent.py#L2750) | 2750 | `"                        source[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L002751](../../agents/web_agent.py#L2751) | 2751 | `"                        source[\"page_fetch_status\"] = ("` | — |
| [SRC-1AE03B9EC3-L002752](../../agents/web_agent.py#L2752) | 2752 | `"                            observed_status"` | — |
| [SRC-1AE03B9EC3-L002753](../../agents/web_agent.py#L2753) | 2753 | `"                            if observed_status in {\"content_extracted\", \"partial_extraction\"}"` | — |
| [SRC-1AE03B9EC3-L002754](../../agents/web_agent.py#L2754) | 2754 | `"                            else \"partial_extraction\""` | — |
| [SRC-1AE03B9EC3-L002755](../../agents/web_agent.py#L2755) | 2755 | `"                            if len(page_text) >= MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L002756](../../agents/web_agent.py#L2756) | 2756 | `"                            else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L002757](../../agents/web_agent.py#L2757) | 2757 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002758](../../agents/web_agent.py#L2758) | 2758 | `"                        if error_class:"` | — |
| [SRC-1AE03B9EC3-L002759](../../agents/web_agent.py#L2759) | 2759 | `"                            source[\"page_fetch_error_class\"] = str(error_class)[:80]"` | — |
| [SRC-1AE03B9EC3-L002760](../../agents/web_agent.py#L2760) | 2760 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L002761](../../agents/web_agent.py#L2761) | 2761 | `"                            source.pop(\"page_fetch_error_class\", None)"` | — |
| [SRC-1AE03B9EC3-L002762](../../agents/web_agent.py#L2762) | 2762 | `"                        fetched_count += 1"` | — |
| [SRC-1AE03B9EC3-L002763](../../agents/web_agent.py#L2763) | 2763 | `"                        if source[\"page_fetch_status\"] == \"partial_extraction\":"` | — |
| [SRC-1AE03B9EC3-L002764](../../agents/web_agent.py#L2764) | 2764 | `"                            host = urllib.parse.urlparse(source.get(\"url\", \"\")).hostname or \"المصدر\""` | — |
| [SRC-1AE03B9EC3-L002765](../../agents/web_agent.py#L2765) | 2765 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002766](../../agents/web_agent.py#L2766) | 2766 | `"                                f\"استُخرج جزء من نص {host} فقط؛ قد تكون الصفحة أطول من الحد الآمن.\""` | — |
| [SRC-1AE03B9EC3-L002767](../../agents/web_agent.py#L2767) | 2767 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002768](../../agents/web_agent.py#L2768) | 2768 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L002769](../../agents/web_agent.py#L2769) | 2769 | `"                        source[\"page_fetched\"] = False"` | — |
| [SRC-1AE03B9EC3-L002770](../../agents/web_agent.py#L2770) | 2770 | `"                        if observed_status in {"` | — |
| [SRC-1AE03B9EC3-L002771](../../agents/web_agent.py#L2771) | 2771 | `"                            \"rejected_url\", \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L002772](../../agents/web_agent.py#L2772) | 2772 | `"                            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\", \"http_error\","` | — |
| [SRC-1AE03B9EC3-L002773](../../agents/web_agent.py#L2773) | 2773 | `"                            \"unsupported_content_type\", \"page_too_large\", \"network_error\","` | — |
| [SRC-1AE03B9EC3-L002774](../../agents/web_agent.py#L2774) | 2774 | `"                            \"empty_content\", \"no_text_extracted\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002775](../../agents/web_agent.py#L2775) | 2775 | `"                        }:"` | — |
| [SRC-1AE03B9EC3-L002776](../../agents/web_agent.py#L2776) | 2776 | `"                            source[\"page_fetch_status\"] = observed_status"` | — |
| [SRC-1AE03B9EC3-L002777](../../agents/web_agent.py#L2777) | 2777 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L002778](../../agents/web_agent.py#L2778) | 2778 | `"                            source[\"page_fetch_status\"] = \"no_text_extracted\""` | — |
| [SRC-1AE03B9EC3-L002779](../../agents/web_agent.py#L2779) | 2779 | `"                        if error_class:"` | — |
| [SRC-1AE03B9EC3-L002780](../../agents/web_agent.py#L2780) | 2780 | `"                            source[\"page_fetch_error_class\"] = str(error_class)[:80]"` | — |
| [SRC-1AE03B9EC3-L002781](../../agents/web_agent.py#L2781) | 2781 | `"                        host = urllib.parse.urlparse(source.get(\"url\", \"\")).hostname or \"المصدر\""` | — |
| [SRC-1AE03B9EC3-L002782](../../agents/web_agent.py#L2782) | 2782 | `"                        if source[\"page_fetch_status\"] in {\"no_text_extracted\", \"empty_content\"}:"` | — |
| [SRC-1AE03B9EC3-L002783](../../agents/web_agent.py#L2783) | 2783 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002784](../../agents/web_agent.py#L2784) | 2784 | `"                                f\"لم يمكن استخراج نص من {host}؛ جُلبت الصفحة أو جرت محاولة قراءتها لكن قد تكون ديناميكية أو محجوبة.\""` | — |
| [SRC-1AE03B9EC3-L002785](../../agents/web_agent.py#L2785) | 2785 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002786](../../agents/web_agent.py#L2786) | 2786 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L002787](../../agents/web_agent.py#L2787) | 2787 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002788](../../agents/web_agent.py#L2788) | 2788 | `"                                f\"تعذرت قراءة نص {host} بسبب حالة الجلب: {source['page_fetch_status']}.\""` | — |
| [SRC-1AE03B9EC3-L002789](../../agents/web_agent.py#L2789) | 2789 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002790](../../agents/web_agent.py#L2790) | 2790 | `""` | — |
| [SRC-1AE03B9EC3-L002791](../../agents/web_agent.py#L2791) | 2791 | `"        # Reorder on consensus first, and keep clear machine-readable provenance."` | — |
| [SRC-1AE03B9EC3-L002792](../../agents/web_agent.py#L2792) | 2792 | `"        sources.sort(key=lambda source: source.get(\"rank_score\", 0), reverse=True)"` | — |
| [SRC-1AE03B9EC3-L002793](../../agents/web_agent.py#L2793) | 2793 | `"        providers = sorted({"` | — |
| [SRC-1AE03B9EC3-L002794](../../agents/web_agent.py#L2794) | 2794 | `"            provider"` | — |
| [SRC-1AE03B9EC3-L002795](../../agents/web_agent.py#L2795) | 2795 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L002796](../../agents/web_agent.py#L2796) | 2796 | `"            for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L002797](../../agents/web_agent.py#L2797) | 2797 | `"        })"` | — |
| [SRC-1AE03B9EC3-L002798](../../agents/web_agent.py#L2798) | 2798 | `"        platform_counts: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L002799](../../agents/web_agent.py#L2799) | 2799 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L002800](../../agents/web_agent.py#L2800) | 2800 | `"            label = source.get(\"platform\", \"web\")"` | — |
| [SRC-1AE03B9EC3-L002801](../../agents/web_agent.py#L2801) | 2801 | `"            platform_counts[label] = platform_counts.get(label, 0) + 1"` | — |
| [SRC-1AE03B9EC3-L002802](../../agents/web_agent.py#L2802) | 2802 | `"        page_failure_statuses = {"` | — |
| [SRC-1AE03B9EC3-L002803](../../agents/web_agent.py#L2803) | 2803 | `"            \"fetch_failed\", \"no_text_extracted\", \"rejected_url\","` | — |
| [SRC-1AE03B9EC3-L002804](../../agents/web_agent.py#L2804) | 2804 | `"            \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L002805](../../agents/web_agent.py#L2805) | 2805 | `"            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\","` | — |
| [SRC-1AE03B9EC3-L002806](../../agents/web_agent.py#L2806) | 2806 | `"            \"http_error\", \"unsupported_content_type\", \"page_too_large\","` | — |
| [SRC-1AE03B9EC3-L002807](../../agents/web_agent.py#L2807) | 2807 | `"            \"network_error\", \"empty_content\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002808](../../agents/web_agent.py#L2808) | 2808 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002809](../../agents/web_agent.py#L2809) | 2809 | `"        page_status_values = ("` | — |
| [SRC-1AE03B9EC3-L002810](../../agents/web_agent.py#L2810) | 2810 | `"            \"not_attempted\", \"attempted\", \"content_extracted\", \"partial_extraction\","` | — |
| [SRC-1AE03B9EC3-L002811](../../agents/web_agent.py#L2811) | 2811 | `"            \"no_text_extracted\", \"fetch_failed\", \"rejected_url\","` | — |
| [SRC-1AE03B9EC3-L002812](../../agents/web_agent.py#L2812) | 2812 | `"            \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L002813](../../agents/web_agent.py#L2813) | 2813 | `"            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\","` | — |
| [SRC-1AE03B9EC3-L002814](../../agents/web_agent.py#L2814) | 2814 | `"            \"http_error\", \"unsupported_content_type\", \"page_too_large\","` | — |
| [SRC-1AE03B9EC3-L002815](../../agents/web_agent.py#L2815) | 2815 | `"            \"network_error\", \"empty_content\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002816](../../agents/web_agent.py#L2816) | 2816 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002817](../../agents/web_agent.py#L2817) | 2817 | `"        page_fetch_status_counts = {"` | — |
| [SRC-1AE03B9EC3-L002818](../../agents/web_agent.py#L2818) | 2818 | `"            status: sum(source.get(\"page_fetch_status\") == status for source in fetch_targets)"` | — |
| [SRC-1AE03B9EC3-L002819](../../agents/web_agent.py#L2819) | 2819 | `"            for status in page_status_values"` | — |
| [SRC-1AE03B9EC3-L002820](../../agents/web_agent.py#L2820) | 2820 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002821](../../agents/web_agent.py#L2821) | 2821 | `"        provider_diagnostics = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L002822](../../agents/web_agent.py#L2822) | 2822 | `"        provider_candidates_received = sum("` | — |
| [SRC-1AE03B9EC3-L002823](../../agents/web_agent.py#L2823) | 2823 | `"            max(0, int(row.get(\"result_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002824](../../agents/web_agent.py#L2824) | 2824 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L002825](../../agents/web_agent.py#L2825) | 2825 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002826](../../agents/web_agent.py#L2826) | 2826 | `"        provider_candidates_accepted = sum("` | — |
| [SRC-1AE03B9EC3-L002827](../../agents/web_agent.py#L2827) | 2827 | `"            max(0, int(row.get(\"accepted_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002828](../../agents/web_agent.py#L2828) | 2828 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L002829](../../agents/web_agent.py#L2829) | 2829 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002830](../../agents/web_agent.py#L2830) | 2830 | `"        provider_candidates_rejected = sum("` | — |
| [SRC-1AE03B9EC3-L002831](../../agents/web_agent.py#L2831) | 2831 | `"            max(0, int(row.get(\"rejected_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002832](../../agents/web_agent.py#L2832) | 2832 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L002833](../../agents/web_agent.py#L2833) | 2833 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002834](../../agents/web_agent.py#L2834) | 2834 | `"        report = {"` | — |
| [SRC-1AE03B9EC3-L002835](../../agents/web_agent.py#L2835) | 2835 | `"            \"raw_results\": raw_results_count,"` | — |
| [SRC-1AE03B9EC3-L002836](../../agents/web_agent.py#L2836) | 2836 | `"            \"provider_candidates_received\": provider_candidates_received,"` | — |
| [SRC-1AE03B9EC3-L002837](../../agents/web_agent.py#L2837) | 2837 | `"            \"provider_candidates_accepted\": provider_candidates_accepted,"` | — |
| [SRC-1AE03B9EC3-L002838](../../agents/web_agent.py#L2838) | 2838 | `"            \"provider_candidates_rejected\": provider_candidates_rejected,"` | — |
| [SRC-1AE03B9EC3-L002839](../../agents/web_agent.py#L2839) | 2839 | `"            \"unique_urls\": len({"` | — |
| [SRC-1AE03B9EC3-L002840](../../agents/web_agent.py#L2840) | 2840 | `"                self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L002841](../../agents/web_agent.py#L2841) | 2841 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L002842](../../agents/web_agent.py#L2842) | 2842 | `"                if self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L002843](../../agents/web_agent.py#L2843) | 2843 | `"            }),"` | — |
| [SRC-1AE03B9EC3-L002844](../../agents/web_agent.py#L2844) | 2844 | `"            \"pages_content_extracted\": fetched_count,"` | — |
| [SRC-1AE03B9EC3-L002845](../../agents/web_agent.py#L2845) | 2845 | `"            \"pages_partial_extracted\": sum("` | — |
| [SRC-1AE03B9EC3-L002846](../../agents/web_agent.py#L2846) | 2846 | `"                source.get(\"page_fetch_status\") == \"partial_extraction\""` | — |
| [SRC-1AE03B9EC3-L002847](../../agents/web_agent.py#L2847) | 2847 | `"                for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L002848](../../agents/web_agent.py#L2848) | 2848 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L002849](../../agents/web_agent.py#L2849) | 2849 | `"            \"pages_extract_failed\": sum("` | — |
| [SRC-1AE03B9EC3-L002850](../../agents/web_agent.py#L2850) | 2850 | `"                source.get(\"page_fetch_status\") in page_failure_statuses"` | — |
| [SRC-1AE03B9EC3-L002851](../../agents/web_agent.py#L2851) | 2851 | `"                for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L002852](../../agents/web_agent.py#L2852) | 2852 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L002853](../../agents/web_agent.py#L2853) | 2853 | `"            \"page_fetch_status_counts\": page_fetch_status_counts,"` | — |
| [SRC-1AE03B9EC3-L002854](../../agents/web_agent.py#L2854) | 2854 | `"            \"queries_planned\": len(queries),"` | — |
| [SRC-1AE03B9EC3-L002855](../../agents/web_agent.py#L2855) | 2855 | `"            \"queries_attempted\": search_started_queries,"` | — |
| [SRC-1AE03B9EC3-L002856](../../agents/web_agent.py#L2856) | 2856 | `"            \"query_results\": query_counts,"` | — |
| [SRC-1AE03B9EC3-L002857](../../agents/web_agent.py#L2857) | 2857 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L002858](../../agents/web_agent.py#L2858) | 2858 | `"            \"pages_fetched\": fetched_count,"` | — |
| [SRC-1AE03B9EC3-L002859](../../agents/web_agent.py#L2859) | 2859 | `"            \"providers_used\": providers,"` | — |
| [SRC-1AE03B9EC3-L002860](../../agents/web_agent.py#L2860) | 2860 | `"            \"provider_counts\": {"` | — |
| [SRC-1AE03B9EC3-L002861](../../agents/web_agent.py#L2861) | 2861 | `"                provider: sum(provider in source.get(\"providers\", []) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L002862](../../agents/web_agent.py#L2862) | 2862 | `"                for provider in providers"` | — |
| [SRC-1AE03B9EC3-L002863](../../agents/web_agent.py#L2863) | 2863 | `"            },"` | — |
| [SRC-1AE03B9EC3-L002864](../../agents/web_agent.py#L2864) | 2864 | `"            \"platform_counts\": platform_counts,"` | — |
| [SRC-1AE03B9EC3-L002865](../../agents/web_agent.py#L2865) | 2865 | `"            \"social_direct_results\": len(social_results),"` | — |
| [SRC-1AE03B9EC3-L002866](../../agents/web_agent.py#L2866) | 2866 | `"            \"expansion_queries\": expansion_queries,"` | — |
| [SRC-1AE03B9EC3-L002867](../../agents/web_agent.py#L2867) | 2867 | `"            \"evidence_signals\": evidence_signal_report(sources, plan.get(\"freshness\", \"any\")),"` | — |
| [SRC-1AE03B9EC3-L002868](../../agents/web_agent.py#L2868) | 2868 | `"            \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L002869](../../agents/web_agent.py#L2869) | 2869 | `"            \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L002870](../../agents/web_agent.py#L2870) | 2870 | `"            \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L002871](../../agents/web_agent.py#L2871) | 2871 | `"            \"provider_diagnostics\": provider_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L002872](../../agents/web_agent.py#L2872) | 2872 | `"            \"connector_summary\": self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L002873](../../agents/web_agent.py#L2873) | 2873 | `"                provider_diagnostics, sources"` | — |
| [SRC-1AE03B9EC3-L002874](../../agents/web_agent.py#L2874) | 2874 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L002875](../../agents/web_agent.py#L2875) | 2875 | `"            \"pages_fetch_attempted\": len(fetch_targets),"` | — |
| [SRC-1AE03B9EC3-L002876](../../agents/web_agent.py#L2876) | 2876 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002877](../../agents/web_agent.py#L2877) | 2877 | `"        coverage_targets = plan.get(\"coverage_targets\") or []"` | — |
| [SRC-1AE03B9EC3-L002878](../../agents/web_agent.py#L2878) | 2878 | `"        if isinstance(coverage_targets, list) and coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L002879](../../agents/web_agent.py#L2879) | 2879 | `"            safe_targets = ["` | — |
| [SRC-1AE03B9EC3-L002880](../../agents/web_agent.py#L2880) | 2880 | `"                target[:120]"` | — |
| [SRC-1AE03B9EC3-L002881](../../agents/web_agent.py#L2881) | 2881 | `"                for target in coverage_targets"` | — |
| [SRC-1AE03B9EC3-L002882](../../agents/web_agent.py#L2882) | 2882 | `"                if isinstance(target, str) and target.strip()"` | — |
| [SRC-1AE03B9EC3-L002883](../../agents/web_agent.py#L2883) | 2883 | `"            ][:8]"` | — |
| [SRC-1AE03B9EC3-L002884](../../agents/web_agent.py#L2884) | 2884 | `"            ledger = build_evidence_ledger(safe_targets, sources)"` | — |
| [SRC-1AE03B9EC3-L002885](../../agents/web_agent.py#L2885) | 2885 | `"            report[\"aspects\"] = safe_targets"` | — |
| [SRC-1AE03B9EC3-L002886](../../agents/web_agent.py#L2886) | 2886 | `"            report[\"evidence_ledger\"] = ledger"` | — |
| [SRC-1AE03B9EC3-L002887](../../agents/web_agent.py#L2887) | 2887 | `"            report[\"aspect_diagnostics_ar\"] = arabic_aspect_diagnostics(ledger)"` | — |
| [SRC-1AE03B9EC3-L002888](../../agents/web_agent.py#L2888) | 2888 | `"            report[\"aspect_evidence_gaps\"] = list(ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L002889](../../agents/web_agent.py#L2889) | 2889 | `"            report[\"aspect_coverage_lexical_ratio\"] = ledger.get(\"coverage_ratio\")"` | — |
| [SRC-1AE03B9EC3-L002890](../../agents/web_agent.py#L2890) | 2890 | `"            report[\"aspect_coverage_is_not_truth_score\"] = True"` | — |
| [SRC-1AE03B9EC3-L002891](../../agents/web_agent.py#L2891) | 2891 | `""` | — |
| [SRC-1AE03B9EC3-L002892](../../agents/web_agent.py#L2892) | 2892 | `"        return sources, list(dict.fromkeys(warnings)), report"` | — |
| [SRC-1AE03B9EC3-L002893](../../agents/web_agent.py#L2893) | 2893 | `""` | — |
| [SRC-1AE03B9EC3-L002894](../../agents/web_agent.py#L2894) | 2894 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L002895](../../agents/web_agent.py#L2895) | 2895 | `"    def _history_search_query(question: str, history: list[dict[str, str]]) -> str:"` | — |
| [SRC-1AE03B9EC3-L002896](../../agents/web_agent.py#L2896) | 2896 | `"        \"\"\"Backward-compatible wrapper for the shared follow-up resolver.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002897](../../agents/web_agent.py#L2897) | 2897 | `"        return resolve_followup_query(question, history)"` | — |
| [SRC-1AE03B9EC3-L002898](../../agents/web_agent.py#L2898) | 2898 | `""` | — |
| [SRC-1AE03B9EC3-L002899](../../agents/web_agent.py#L2899) | 2899 | `"    def _connector_status_summary(self, diagnostics: list[dict[str, Any]] \| None,"` | — |
| [SRC-1AE03B9EC3-L002900](../../agents/web_agent.py#L2900) | 2900 | `"                                  sources: list[dict[str, Any]] \| None = None) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L002901](../../agents/web_agent.py#L2901) | 2901 | `"        \"\"\"Summarize this request's connector states without exposing credentials.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002902](../../agents/web_agent.py#L2902) | 2902 | `"        optional = {"` | — |
| [SRC-1AE03B9EC3-L002903](../../agents/web_agent.py#L2903) | 2903 | `"            \"deepseek_search_api\": (\"DEEPSEEK_SEARCH_API_KEY\",), \"brave_search_api\": (\"BRAVE_SEARCH_API_KEY\",),"` | — |
| [SRC-1AE03B9EC3-L002904](../../agents/web_agent.py#L2904) | 2904 | `"            \"tavily_search_api\": (\"TAVILY_API_KEY\",), \"reddit_oauth_api\": (\"REDDIT_CLIENT_ID\", \"REDDIT_CLIENT_SECRET\"),"` | — |
| [SRC-1AE03B9EC3-L002905](../../agents/web_agent.py#L2905) | 2905 | `"            \"facebook_pages_api\": (\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"FACEBOOK_PAGE_IDS\"),"` | — |
| [SRC-1AE03B9EC3-L002906](../../agents/web_agent.py#L2906) | 2906 | `"            \"instagram_graph_api\": (\"INSTAGRAM_USER_ID\", \"INSTAGRAM_ACCESS_TOKEN\"),"` | — |
| [SRC-1AE03B9EC3-L002907](../../agents/web_agent.py#L2907) | 2907 | `"            \"x_official_api\": (\"X_BEARER_TOKEN\",), \"youtube_data_api\": (\"YOUTUBE_API_KEY\",),"` | — |
| [SRC-1AE03B9EC3-L002908](../../agents/web_agent.py#L2908) | 2908 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002909](../../agents/web_agent.py#L2909) | 2909 | `"        config: dict[str, tuple[bool, str]] = {"` | — |
| [SRC-1AE03B9EC3-L002910](../../agents/web_agent.py#L2910) | 2910 | `"            \"duckduckgo_html\": (True, \"built_in_no_api_key\"), \"bing_rss\": (True, \"built_in_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L002911](../../agents/web_agent.py#L2911) | 2911 | `"            \"google_news_rss\": (True, \"built_in_conditional_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L002912](../../agents/web_agent.py#L2912) | 2912 | `"            \"openalex\": (True, \"built_in_free_academic\"),"` | — |
| [SRC-1AE03B9EC3-L002913](../../agents/web_agent.py#L2913) | 2913 | `"            \"arxiv\": (True, \"built_in_free_academic\"),"` | — |
| [SRC-1AE03B9EC3-L002914](../../agents/web_agent.py#L2914) | 2914 | `"            \"crossref\": (True, \"built_in_free_academic\"),"` | — |
| [SRC-1AE03B9EC3-L002915](../../agents/web_agent.py#L2915) | 2915 | `"            \"reddit_public_rss\": (True, \"built_in_no_api_key\"), \"bluesky_public_search\": (True, \"built_in_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L002916](../../agents/web_agent.py#L2916) | 2916 | `"            \"openrouter_web_search\": (bool(self.openrouter_web_search_enabled),"` | — |
| [SRC-1AE03B9EC3-L002917](../../agents/web_agent.py#L2917) | 2917 | `"                \"enabled\" if self.openrouter_web_search_enabled else \"disabled\"),"` | — |
| [SRC-1AE03B9EC3-L002918](../../agents/web_agent.py#L2918) | 2918 | `"            \"user_supplied_url\": (True, \"request_driven\"),"` | — |
| [SRC-1AE03B9EC3-L002919](../../agents/web_agent.py#L2919) | 2919 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002920](../../agents/web_agent.py#L2920) | 2920 | `"        for name, keys in optional.items():"` | — |
| [SRC-1AE03B9EC3-L002921](../../agents/web_agent.py#L2921) | 2921 | `"            ready = all(bool(os.getenv(key, \"\").strip()) for key in keys)"` | — |
| [SRC-1AE03B9EC3-L002922](../../agents/web_agent.py#L2922) | 2922 | `"            config[name] = (ready, \"configured\" if ready else \"not_configured\")"` | — |
| [SRC-1AE03B9EC3-L002923](../../agents/web_agent.py#L2923) | 2923 | `"        grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002924](../../agents/web_agent.py#L2924) | 2924 | `"        for item in diagnostics or []:"` | — |
| [SRC-1AE03B9EC3-L002925](../../agents/web_agent.py#L2925) | 2925 | `"            if isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L002926](../../agents/web_agent.py#L2926) | 2926 | `"                name = _clean_text(item.get(\"provider\", \"unknown\"), 80) or \"unknown\""` | — |
| [SRC-1AE03B9EC3-L002927](../../agents/web_agent.py#L2927) | 2927 | `"                grouped.setdefault(name, []).append(item)"` | — |
| [SRC-1AE03B9EC3-L002928](../../agents/web_agent.py#L2928) | 2928 | `"        useful: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L002929](../../agents/web_agent.py#L2929) | 2929 | `"        for source in sources or []:"` | — |
| [SRC-1AE03B9EC3-L002930](../../agents/web_agent.py#L2930) | 2930 | `"            if not isinstance(source, dict):"` | — |
| [SRC-1AE03B9EC3-L002931](../../agents/web_agent.py#L2931) | 2931 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002932](../../agents/web_agent.py#L2932) | 2932 | `"            providers = source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L002933](../../agents/web_agent.py#L2933) | 2933 | `"            if isinstance(providers, str):"` | — |
| [SRC-1AE03B9EC3-L002934](../../agents/web_agent.py#L2934) | 2934 | `"                providers = [providers]"` | — |
| [SRC-1AE03B9EC3-L002935](../../agents/web_agent.py#L2935) | 2935 | `"            if not isinstance(providers, list):"` | — |
| [SRC-1AE03B9EC3-L002936](../../agents/web_agent.py#L2936) | 2936 | `"                providers = []"` | — |
| [SRC-1AE03B9EC3-L002937](../../agents/web_agent.py#L2937) | 2937 | `"            if isinstance(source.get(\"provider\"), str):"` | — |
| [SRC-1AE03B9EC3-L002938](../../agents/web_agent.py#L2938) | 2938 | `"                providers = providers + [source[\"provider\"]]"` | — |
| [SRC-1AE03B9EC3-L002939](../../agents/web_agent.py#L2939) | 2939 | `"            for name in {str(value) for value in providers if value}:"` | — |
| [SRC-1AE03B9EC3-L002940](../../agents/web_agent.py#L2940) | 2940 | `"                useful[name] = useful.get(name, 0) + 1"` | — |
| [SRC-1AE03B9EC3-L002941](../../agents/web_agent.py#L2941) | 2941 | `"        priority = {\"ok\": 0, \"no_results\": 1, \"filtered_all\": 2, \"not_attempted\": 3,"` | — |
| [SRC-1AE03B9EC3-L002942](../../agents/web_agent.py#L2942) | 2942 | `"                    \"disabled\": 4, \"not_configured\": 5, \"budget_exhausted\": 6,"` | — |
| [SRC-1AE03B9EC3-L002943](../../agents/web_agent.py#L2943) | 2943 | `"                    \"unknown\": 6, \"rate_limited\": 7, \"unauthorized\": 8, \"http_error\": 9,"` | — |
| [SRC-1AE03B9EC3-L002944](../../agents/web_agent.py#L2944) | 2944 | `"                    \"timeout\": 10, \"failed\": 11, \"error\": 11}"` | — |
| [SRC-1AE03B9EC3-L002945](../../agents/web_agent.py#L2945) | 2945 | `"        confirmed_attempt_statuses = _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES \| {"` | — |
| [SRC-1AE03B9EC3-L002946](../../agents/web_agent.py#L2946) | 2946 | `"            \"http_error\", \"unauthorized\", \"rate_limited\", \"invalid_response\""` | — |
| [SRC-1AE03B9EC3-L002947](../../agents/web_agent.py#L2947) | 2947 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002948](../../agents/web_agent.py#L2948) | 2948 | `"        uncertain_attempt_statuses = {\"timeout\", \"failed\", \"error\", \"unknown\", \"inconclusive\"}"` | — |
| [SRC-1AE03B9EC3-L002949](../../agents/web_agent.py#L2949) | 2949 | `""` | — |
| [SRC-1AE03B9EC3-L002950](../../agents/web_agent.py#L2950) | 2950 | `"        def redact(value: Any) -> str:"` | — |
| [SRC-1AE03B9EC3-L002951](../../agents/web_agent.py#L2951) | 2951 | `"            safe = _clean_text(str(value or \"\"), 180)"` | — |
| [SRC-1AE03B9EC3-L002952](../../agents/web_agent.py#L2952) | 2952 | `"            safe = re.sub(r\"(?i)(bearer\\s+)[A-Za-z0-9._~+/-]+=*\", r\"\\1[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L002953](../../agents/web_agent.py#L2953) | 2953 | `"            safe = re.sub(r\"(?i)\\b(api[_-]?key\|access[_-]?token\|refresh[_-]?token\|token\|secret\|password)\\s*[:=]\\s*[^\\s,;]+\", r\"\\1=[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L002954](../../agents/web_agent.py#L2954) | 2954 | `"            safe = re.sub(r\"(?i)([?&](?:api[_-]?key\|access[_-]?token\|token\|key)=)[^&\\s]+\", r\"\\1[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L002955](../../agents/web_agent.py#L2955) | 2955 | `"            return safe[:180]"` | — |
| [SRC-1AE03B9EC3-L002956](../../agents/web_agent.py#L2956) | 2956 | `""` | — |
| [SRC-1AE03B9EC3-L002957](../../agents/web_agent.py#L2957) | 2957 | `"        names = set(config) \| set(grouped) \| set(useful)"` | — |
| [SRC-1AE03B9EC3-L002958](../../agents/web_agent.py#L2958) | 2958 | `"        connectors = []"` | — |
| [SRC-1AE03B9EC3-L002959](../../agents/web_agent.py#L2959) | 2959 | `"        for name in sorted(names):"` | — |
| [SRC-1AE03B9EC3-L002960](../../agents/web_agent.py#L2960) | 2960 | `"            ready, config_status = config.get(name, (bool(grouped.get(name) or useful.get(name)), \"observed_in_code_path\"))"` | — |
| [SRC-1AE03B9EC3-L002961](../../agents/web_agent.py#L2961) | 2961 | `"            attempts = grouped.get(name, [])"` | — |
| [SRC-1AE03B9EC3-L002962](../../agents/web_agent.py#L2962) | 2962 | `"            statuses = [_clean_text(row.get(\"status\", \"unknown\"), 40).lower() or \"unknown\" for row in attempts]"` | — |
| [SRC-1AE03B9EC3-L002963](../../agents/web_agent.py#L2963) | 2963 | `"            status = max(statuses, key=lambda value: priority.get(value, 6)) if statuses else ("` | — |
| [SRC-1AE03B9EC3-L002964](../../agents/web_agent.py#L2964) | 2964 | `"                \"ok\" if useful.get(name, 0) else \"not_configured\" if not ready else \"not_attempted\")"` | — |
| [SRC-1AE03B9EC3-L002965](../../agents/web_agent.py#L2965) | 2965 | `"            if any(value in confirmed_attempt_statuses for value in statuses) or useful.get(name, 0):"` | — |
| [SRC-1AE03B9EC3-L002966](../../agents/web_agent.py#L2966) | 2966 | `"                attempted: bool \| None = True"` | — |
| [SRC-1AE03B9EC3-L002967](../../agents/web_agent.py#L2967) | 2967 | `"            elif any(value in uncertain_attempt_statuses for value in statuses):"` | — |
| [SRC-1AE03B9EC3-L002968](../../agents/web_agent.py#L2968) | 2968 | `"                attempted = None"` | — |
| [SRC-1AE03B9EC3-L002969](../../agents/web_agent.py#L2969) | 2969 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002970](../../agents/web_agent.py#L2970) | 2970 | `"                attempted = False"` | — |
| [SRC-1AE03B9EC3-L002971](../../agents/web_agent.py#L2971) | 2971 | `"            successful_statuses = set(statuses) & _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L002972](../../agents/web_agent.py#L2972) | 2972 | `"            error_response_statuses = set(statuses) & {\"http_error\", \"unauthorized\", \"rate_limited\"}"` | — |
| [SRC-1AE03B9EC3-L002973](../../agents/web_agent.py#L2973) | 2973 | `"            uncertain_failure_statuses = set(statuses) & {\"timeout\", \"failed\", \"error\", \"unknown\", \"inconclusive\"}"` | — |
| [SRC-1AE03B9EC3-L002974](../../agents/web_agent.py#L2974) | 2974 | `"            failure_observed = bool(error_response_statuses or uncertain_failure_statuses or \"budget_exhausted\" in statuses)"` | — |
| [SRC-1AE03B9EC3-L002975](../../agents/web_agent.py#L2975) | 2975 | `"            available: bool \| None = ("` | — |
| [SRC-1AE03B9EC3-L002976](../../agents/web_agent.py#L2976) | 2976 | `"                True if successful_statuses or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L002977](../../agents/web_agent.py#L2977) | 2977 | `"                else False if error_response_statuses or not ready or \"disabled\" in statuses or \"budget_exhausted\" in statuses"` | — |
| [SRC-1AE03B9EC3-L002978](../../agents/web_agent.py#L2978) | 2978 | `"                else None"` | — |
| [SRC-1AE03B9EC3-L002979](../../agents/web_agent.py#L2979) | 2979 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002980](../../agents/web_agent.py#L2980) | 2980 | `"            verified: bool \| None = ("` | — |
| [SRC-1AE03B9EC3-L002981](../../agents/web_agent.py#L2981) | 2981 | `"                True if successful_statuses or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L002982](../../agents/web_agent.py#L2982) | 2982 | `"                else False if error_response_statuses"` | — |
| [SRC-1AE03B9EC3-L002983](../../agents/web_agent.py#L2983) | 2983 | `"                else None"` | — |
| [SRC-1AE03B9EC3-L002984](../../agents/web_agent.py#L2984) | 2984 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002985](../../agents/web_agent.py#L2985) | 2985 | `"            implementation_status = ("` | — |
| [SRC-1AE03B9EC3-L002986](../../agents/web_agent.py#L2986) | 2986 | `"                \"implemented_in_code\" if name in config"` | — |
| [SRC-1AE03B9EC3-L002987](../../agents/web_agent.py#L2987) | 2987 | `"                else \"observed_runtime_path\" if attempts or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L002988](../../agents/web_agent.py#L2988) | 2988 | `"                else \"unknown\""` | — |
| [SRC-1AE03B9EC3-L002989](../../agents/web_agent.py#L2989) | 2989 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002990](../../agents/web_agent.py#L2990) | 2990 | `"            queries = list(dict.fromkeys(_clean_text(row.get(\"query\", \"\"), 180) for row in attempts if row.get(\"query\")))[:3]"` | — |
| [SRC-1AE03B9EC3-L002991](../../agents/web_agent.py#L2991) | 2991 | `"            errors = list(dict.fromkeys(redact(row.get(\"error\")) for row in attempts if row.get(\"error\")))[:3]"` | — |
| [SRC-1AE03B9EC3-L002992](../../agents/web_agent.py#L2992) | 2992 | `"            result_count = sum(max(0, int(row.get(\"result_count\", 0) or 0)) for row in attempts)"` | — |
| [SRC-1AE03B9EC3-L002993](../../agents/web_agent.py#L2993) | 2993 | `"            accepted_count = sum("` | — |
| [SRC-1AE03B9EC3-L002994](../../agents/web_agent.py#L2994) | 2994 | `"                max(0, int(row.get(\"accepted_count\", row.get(\"result_count\", 0)) or 0))"` | — |
| [SRC-1AE03B9EC3-L002995](../../agents/web_agent.py#L2995) | 2995 | `"                for row in attempts"` | — |
| [SRC-1AE03B9EC3-L002996](../../agents/web_agent.py#L2996) | 2996 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002997](../../agents/web_agent.py#L2997) | 2997 | `"            rejected_count = sum(max(0, int(row.get(\"rejected_count\", 0) or 0)) for row in attempts)"` | — |
| [SRC-1AE03B9EC3-L002998](../../agents/web_agent.py#L2998) | 2998 | `"            rejection_count_totals = {reason: 0 for reason in _PROVIDER_REJECTION_REASONS}"` | — |
| [SRC-1AE03B9EC3-L002999](../../agents/web_agent.py#L2999) | 2999 | `"            rejection_counts_seen = False"` | — |
| [SRC-1AE03B9EC3-L003000](../../agents/web_agent.py#L3000) | 3000 | `"            rejection_counts_complete = True"` | — |
| [SRC-1AE03B9EC3-L003001](../../agents/web_agent.py#L3001) | 3001 | `"            for row in attempts:"` | — |
| [SRC-1AE03B9EC3-L003002](../../agents/web_agent.py#L3002) | 3002 | `"                row_counts = row.get(\"rejection_counts\")"` | — |
| [SRC-1AE03B9EC3-L003003](../../agents/web_agent.py#L3003) | 3003 | `"                if not isinstance(row_counts, dict):"` | — |
| [SRC-1AE03B9EC3-L003004](../../agents/web_agent.py#L3004) | 3004 | `"                    # Legacy/incomplete records with actual rejections prevent claiming"` | — |
| [SRC-1AE03B9EC3-L003005](../../agents/web_agent.py#L3005) | 3005 | `"                    # that an aggregate breakdown covers every rejected candidate."` | — |
| [SRC-1AE03B9EC3-L003006](../../agents/web_agent.py#L3006) | 3006 | `"                    if max(0, int(row.get(\"rejected_count\", 0) or 0)) > 0:"` | — |
| [SRC-1AE03B9EC3-L003007](../../agents/web_agent.py#L3007) | 3007 | `"                        rejection_counts_complete = False"` | — |
| [SRC-1AE03B9EC3-L003008](../../agents/web_agent.py#L3008) | 3008 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L003009](../../agents/web_agent.py#L3009) | 3009 | `"                rejection_counts_seen = True"` | — |
| [SRC-1AE03B9EC3-L003010](../../agents/web_agent.py#L3010) | 3010 | `"                for reason in _PROVIDER_REJECTION_REASONS:"` | — |
| [SRC-1AE03B9EC3-L003011](../../agents/web_agent.py#L3011) | 3011 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L003012](../../agents/web_agent.py#L3012) | 3012 | `"                        rejection_count_totals[reason] += max(0, int(row_counts.get(reason, 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L003013](../../agents/web_agent.py#L3013) | 3013 | `"                    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L003014](../../agents/web_agent.py#L3014) | 3014 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L003015](../../agents/web_agent.py#L3015) | 3015 | `"            rejection_counts_observed = ("` | — |
| [SRC-1AE03B9EC3-L003016](../../agents/web_agent.py#L3016) | 3016 | `"                rejection_counts_seen"` | — |
| [SRC-1AE03B9EC3-L003017](../../agents/web_agent.py#L3017) | 3017 | `"                and rejection_counts_complete"` | — |
| [SRC-1AE03B9EC3-L003018](../../agents/web_agent.py#L3018) | 3018 | `"                and sum(rejection_count_totals.values()) == rejected_count"` | — |
| [SRC-1AE03B9EC3-L003019](../../agents/web_agent.py#L3019) | 3019 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003020](../../agents/web_agent.py#L3020) | 3020 | `"            candidate_rejection_observed = \"filtered_all\" in statuses or rejected_count > 0"` | — |
| [SRC-1AE03B9EC3-L003021](../../agents/web_agent.py#L3021) | 3021 | `"            connectors.append({"` | — |
| [SRC-1AE03B9EC3-L003022](../../agents/web_agent.py#L3022) | 3022 | `"                \"name\": name, \"in_codebase\": name in config or bool(attempts),"` | — |
| [SRC-1AE03B9EC3-L003023](../../agents/web_agent.py#L3023) | 3023 | `"                \"implementation_status\": implementation_status,"` | — |
| [SRC-1AE03B9EC3-L003024](../../agents/web_agent.py#L3024) | 3024 | `"                \"configured\": bool(ready), \"configuration_status\": config_status,"` | — |
| [SRC-1AE03B9EC3-L003025](../../agents/web_agent.py#L3025) | 3025 | `"                \"attempted\": attempted, \"available_for_this_request\": available,"` | — |
| [SRC-1AE03B9EC3-L003026](../../agents/web_agent.py#L3026) | 3026 | `"                \"verified_for_this_request\": verified, \"failure_observed\": failure_observed,"` | — |
| [SRC-1AE03B9EC3-L003027](../../agents/web_agent.py#L3027) | 3027 | `"                \"candidate_rejection_observed\": candidate_rejection_observed,"` | — |
| [SRC-1AE03B9EC3-L003028](../../agents/web_agent.py#L3028) | 3028 | `"                \"status\": status, \"observed_statuses\": list(dict.fromkeys(statuses))[:6],"` | — |
| [SRC-1AE03B9EC3-L003029](../../agents/web_agent.py#L3029) | 3029 | `"                \"result_count\": result_count, \"accepted_count\": accepted_count,"` | — |
| [SRC-1AE03B9EC3-L003030](../../agents/web_agent.py#L3030) | 3030 | `"                \"useful_result_count\": useful.get(name, 0),"` | — |
| [SRC-1AE03B9EC3-L003031](../../agents/web_agent.py#L3031) | 3031 | `"                \"rejected_count\": rejected_count,"` | — |
| [SRC-1AE03B9EC3-L003032](../../agents/web_agent.py#L3032) | 3032 | `"                \"rejection_counts_observed\": rejection_counts_observed,"` | — |
| [SRC-1AE03B9EC3-L003033](../../agents/web_agent.py#L3033) | 3033 | `"                \"rejection_counts\": rejection_count_totals if rejection_counts_observed else None,"` | — |
| [SRC-1AE03B9EC3-L003034](../../agents/web_agent.py#L3034) | 3034 | `"                \"queries\": queries, \"errors\": errors,"` | — |
| [SRC-1AE03B9EC3-L003035](../../agents/web_agent.py#L3035) | 3035 | `"            })"` | — |
| [SRC-1AE03B9EC3-L003036](../../agents/web_agent.py#L3036) | 3036 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L003037](../../agents/web_agent.py#L3037) | 3037 | `"            \"scope\": \"this_request_only\","` | — |
| [SRC-1AE03B9EC3-L003038](../../agents/web_agent.py#L3038) | 3038 | `"            \"semantics\": \"result_count is connector-reported rows; useful_result_count counts final fused source records attributed to a connector; neither proves factual accuracy or editorial independence.\","` | — |
| [SRC-1AE03B9EC3-L003039](../../agents/web_agent.py#L3039) | 3039 | `"            \"attempted_count\": sum(bool(item[\"attempted\"]) for item in connectors),"` | — |
| [SRC-1AE03B9EC3-L003040](../../agents/web_agent.py#L3040) | 3040 | `"            \"failed_count\": sum(item[\"status\"] in {\"failed\", \"error\", \"timeout\", \"http_error\", \"unauthorized\", \"rate_limited\"} for item in connectors),"` | — |
| [SRC-1AE03B9EC3-L003041](../../agents/web_agent.py#L3041) | 3041 | `"            \"connectors\": connectors[:24],"` | — |
| [SRC-1AE03B9EC3-L003042](../../agents/web_agent.py#L3042) | 3042 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003043](../../agents/web_agent.py#L3043) | 3043 | `""` | — |
| [SRC-1AE03B9EC3-L003044](../../agents/web_agent.py#L3044) | 3044 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L003045](../../agents/web_agent.py#L3045) | 3045 | `"    def _sanitize_history(history: Any) -> list[dict[str, str]]:"` | — |
| [SRC-1AE03B9EC3-L003046](../../agents/web_agent.py#L3046) | 3046 | `"        if not isinstance(history, list):"` | — |
| [SRC-1AE03B9EC3-L003047](../../agents/web_agent.py#L3047) | 3047 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L003048](../../agents/web_agent.py#L3048) | 3048 | `"        result: list[dict[str, str]] = []"` | — |
| [SRC-1AE03B9EC3-L003049](../../agents/web_agent.py#L3049) | 3049 | `"        for item in history[-MAX_HISTORY_ITEMS:]:"` | — |
| [SRC-1AE03B9EC3-L003050](../../agents/web_agent.py#L3050) | 3050 | `"            if not isinstance(item, dict) or item.get(\"role\") not in {\"user\", \"assistant\"}:"` | — |
| [SRC-1AE03B9EC3-L003051](../../agents/web_agent.py#L3051) | 3051 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L003052](../../agents/web_agent.py#L3052) | 3052 | `"            text = _clean_text(item.get(\"content\"), MAX_HISTORY_CHARS)"` | — |
| [SRC-1AE03B9EC3-L003053](../../agents/web_agent.py#L3053) | 3053 | `"            if text:"` | — |
| [SRC-1AE03B9EC3-L003054](../../agents/web_agent.py#L3054) | 3054 | `"                result.append({\"role\": item[\"role\"], \"content\": text})"` | — |
| [SRC-1AE03B9EC3-L003055](../../agents/web_agent.py#L3055) | 3055 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L003056](../../agents/web_agent.py#L3056) | 3056 | `""` | — |
| [SRC-1AE03B9EC3-L003057](../../agents/web_agent.py#L3057) | 3057 | `"    def _record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L003058](../../agents/web_agent.py#L3058) | 3058 | `"        self,"` | — |
| [SRC-1AE03B9EC3-L003059](../../agents/web_agent.py#L3059) | 3059 | `"        requested_model: str,"` | — |
| [SRC-1AE03B9EC3-L003060](../../agents/web_agent.py#L3060) | 3060 | `"        attempted_model: str,"` | — |
| [SRC-1AE03B9EC3-L003061](../../agents/web_agent.py#L3061) | 3061 | `"        status: str,"` | — |
| [SRC-1AE03B9EC3-L003062](../../agents/web_agent.py#L3062) | 3062 | `"        finish_reason: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L003063](../../agents/web_agent.py#L3063) | 3063 | `"        error_class: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L003064](../../agents/web_agent.py#L3064) | 3064 | `"        request_started: bool = True,"` | — |
| [SRC-1AE03B9EC3-L003065](../../agents/web_agent.py#L3065) | 3065 | `"        remote_response_received: bool \| None = None,"` | — |
| [SRC-1AE03B9EC3-L003066](../../agents/web_agent.py#L3066) | 3066 | `"    ) -> None:"` | — |
| [SRC-1AE03B9EC3-L003067](../../agents/web_agent.py#L3067) | 3067 | `"        \"\"\"Store bounded metadata for each model attempt; never retain prompts or output.\"\"\""` | — |
| [SRC-1AE03B9EC3-L003068](../../agents/web_agent.py#L3068) | 3068 | `"        self._generation_attempt_sequence = getattr(self, \"_generation_attempt_sequence\", 0) + 1"` | — |
| [SRC-1AE03B9EC3-L003069](../../agents/web_agent.py#L3069) | 3069 | `"        record: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L003070](../../agents/web_agent.py#L3070) | 3070 | `"            \"attempt_number\": self._generation_attempt_sequence,"` | — |
| [SRC-1AE03B9EC3-L003071](../../agents/web_agent.py#L3071) | 3071 | `"            \"requested_model\": str(requested_model)[:160],"` | — |
| [SRC-1AE03B9EC3-L003072](../../agents/web_agent.py#L3072) | 3072 | `"            \"attempted_model\": str(attempted_model)[:160],"` | — |
| [SRC-1AE03B9EC3-L003073](../../agents/web_agent.py#L3073) | 3073 | `"            \"fallback_used\": str(attempted_model) != str(requested_model),"` | — |
| [SRC-1AE03B9EC3-L003074](../../agents/web_agent.py#L3074) | 3074 | `"            \"request_started\": bool(request_started),"` | — |
| [SRC-1AE03B9EC3-L003075](../../agents/web_agent.py#L3075) | 3075 | `"            \"status\": str(status)[:48],"` | — |
| [SRC-1AE03B9EC3-L003076](../../agents/web_agent.py#L3076) | 3076 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003077](../../agents/web_agent.py#L3077) | 3077 | `"        if remote_response_received is None and isinstance(finish_reason, str) and finish_reason.strip():"` | — |
| [SRC-1AE03B9EC3-L003078](../../agents/web_agent.py#L3078) | 3078 | `"            # A concrete finish_reason can only be observed after a provider response was received."` | — |
| [SRC-1AE03B9EC3-L003079](../../agents/web_agent.py#L3079) | 3079 | `"            remote_response_received = True"` | — |
| [SRC-1AE03B9EC3-L003080](../../agents/web_agent.py#L3080) | 3080 | `"        if remote_response_received is not None:"` | — |
| [SRC-1AE03B9EC3-L003081](../../agents/web_agent.py#L3081) | 3081 | `"            record[\"remote_response_received\"] = bool(remote_response_received)"` | — |
| [SRC-1AE03B9EC3-L003082](../../agents/web_agent.py#L3082) | 3082 | `"        if isinstance(finish_reason, str) and finish_reason.strip():"` | — |
| [SRC-1AE03B9EC3-L003083](../../agents/web_agent.py#L3083) | 3083 | `"            record[\"finish_reason\"] = finish_reason.strip()[:48]"` | — |
| [SRC-1AE03B9EC3-L003084](../../agents/web_agent.py#L3084) | 3084 | `"        if isinstance(error_class, str) and error_class:"` | — |
| [SRC-1AE03B9EC3-L003085](../../agents/web_agent.py#L3085) | 3085 | `"            record[\"error_class\"] = error_class[:80]"` | — |
| [SRC-1AE03B9EC3-L003086](../../agents/web_agent.py#L3086) | 3086 | `"        self.generation_diagnostics.append(record)"` | — |
| [SRC-1AE03B9EC3-L003087](../../agents/web_agent.py#L3087) | 3087 | `"        self.generation_diagnostics = self.generation_diagnostics[-12:]"` | — |
| [SRC-1AE03B9EC3-L003088](../../agents/web_agent.py#L3088) | 3088 | `""` | — |
| [SRC-1AE03B9EC3-L003089](../../agents/web_agent.py#L3089) | 3089 | `"    def _request_completion("` | — |
| [SRC-1AE03B9EC3-L003090](../../agents/web_agent.py#L3090) | 3090 | `"        self,"` | — |
| [SRC-1AE03B9EC3-L003091](../../agents/web_agent.py#L3091) | 3091 | `"        messages: list[dict[str, str]],"` | — |
| [SRC-1AE03B9EC3-L003092](../../agents/web_agent.py#L3092) | 3092 | `"        max_tokens: int = 1400,"` | — |
| [SRC-1AE03B9EC3-L003093](../../agents/web_agent.py#L3093) | 3093 | `"        temperature: float = 0.2,"` | — |
| [SRC-1AE03B9EC3-L003094](../../agents/web_agent.py#L3094) | 3094 | `"        timeout: int \| None = None,"` | — |
| [SRC-1AE03B9EC3-L003095](../../agents/web_agent.py#L3095) | 3095 | `"        model: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L003096](../../agents/web_agent.py#L3096) | 3096 | `"        enable_web_search: bool = False,"` | — |
| [SRC-1AE03B9EC3-L003097](../../agents/web_agent.py#L3097) | 3097 | `"    ) -> str:"` | — |
| [SRC-1AE03B9EC3-L003098](../../agents/web_agent.py#L3098) | 3098 | `"        \"\"\"Call an OpenAI-compatible API with bounded fallback and optional live server search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L003099](../../agents/web_agent.py#L3099) | 3099 | `"        requested_model = (model or self.answer_model).strip()"` | — |
| [SRC-1AE03B9EC3-L003100](../../agents/web_agent.py#L3100) | 3100 | `"        if not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L003101](../../agents/web_agent.py#L3101) | 3101 | `"            self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L003102](../../agents/web_agent.py#L3102) | 3102 | `"                requested_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L003103](../../agents/web_agent.py#L3103) | 3103 | `"                attempted_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L003104](../../agents/web_agent.py#L3104) | 3104 | `"                status=\"not_configured\","` | — |
| [SRC-1AE03B9EC3-L003105](../../agents/web_agent.py#L3105) | 3105 | `"                error_class=\"MissingAPIKey\","` | — |
| [SRC-1AE03B9EC3-L003106](../../agents/web_agent.py#L3106) | 3106 | `"                request_started=False,"` | — |
| [SRC-1AE03B9EC3-L003107](../../agents/web_agent.py#L3107) | 3107 | `"                remote_response_received=False,"` | — |
| [SRC-1AE03B9EC3-L003108](../../agents/web_agent.py#L3108) | 3108 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003109](../../agents/web_agent.py#L3109) | 3109 | `"            raise RuntimeError(\"لم يتم ضبط مفتاح نموذج اللغة.\")"` | — |
| [SRC-1AE03B9EC3-L003110](../../agents/web_agent.py#L3110) | 3110 | `""` | — |
| [SRC-1AE03B9EC3-L003111](../../agents/web_agent.py#L3111) | 3111 | `"        model_candidates = [requested_model]"` | — |
| [SRC-1AE03B9EC3-L003112](../../agents/web_agent.py#L3112) | 3112 | `"        if self.fallback_model and self.fallback_model not in model_candidates:"` | — |
| [SRC-1AE03B9EC3-L003113](../../agents/web_agent.py#L3113) | 3113 | `"            model_candidates.append(self.fallback_model)"` | — |
| [SRC-1AE03B9EC3-L003114](../../agents/web_agent.py#L3114) | 3114 | `""` | — |
| [SRC-1AE03B9EC3-L003115](../../agents/web_agent.py#L3115) | 3115 | `"        last_error: RuntimeError \| None = None"` | — |
| [SRC-1AE03B9EC3-L003116](../../agents/web_agent.py#L3116) | 3116 | `"        for candidate_model in model_candidates:"` | — |
| [SRC-1AE03B9EC3-L003117](../../agents/web_agent.py#L3117) | 3117 | `"            budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L003118](../../agents/web_agent.py#L3118) | 3118 | `"            use_web_search = enable_web_search and self.openrouter_web_search_enabled"` | — |
| [SRC-1AE03B9EC3-L003119](../../agents/web_agent.py#L3119) | 3119 | `"            if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L003120](../../agents/web_agent.py#L3120) | 3120 | `"                try:"` | — |
| [SRC-1AE03B9EC3-L003121](../../agents/web_agent.py#L3121) | 3121 | `"                    budget.reserve(\"model_calls\")"` | — |
| [SRC-1AE03B9EC3-L003122](../../agents/web_agent.py#L3122) | 3122 | `"                    request_timeout = budget.timeout_for(timeout or self.timeout)"` | — |
| [SRC-1AE03B9EC3-L003123](../../agents/web_agent.py#L3123) | 3123 | `"                    if use_web_search and budget.remaining_units(\"tool_calls\") < 3:"` | — |
| [SRC-1AE03B9EC3-L003124](../../agents/web_agent.py#L3124) | 3124 | `"                        # The model may still answer, but the optional server-side search"` | — |
| [SRC-1AE03B9EC3-L003125](../../agents/web_agent.py#L3125) | 3125 | `"                        # tool is disabled when its separate budget is unavailable."` | — |
| [SRC-1AE03B9EC3-L003126](../../agents/web_agent.py#L3126) | 3126 | `"                        use_web_search = False"` | — |
| [SRC-1AE03B9EC3-L003127](../../agents/web_agent.py#L3127) | 3127 | `"                    elif use_web_search:"` | — |
| [SRC-1AE03B9EC3-L003128](../../agents/web_agent.py#L3128) | 3128 | `"                        # Reserve the maximum server-side tool calls offered by this request."` | — |
| [SRC-1AE03B9EC3-L003129](../../agents/web_agent.py#L3129) | 3129 | `"                        budget.reserve(\"tool_calls\", amount=3)"` | — |
| [SRC-1AE03B9EC3-L003130](../../agents/web_agent.py#L3130) | 3130 | `"                except RequestBudgetExceeded as exc:"` | — |
| [SRC-1AE03B9EC3-L003131](../../agents/web_agent.py#L3131) | 3131 | `"                    self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L003132](../../agents/web_agent.py#L3132) | 3132 | `"                        requested_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L003133](../../agents/web_agent.py#L3133) | 3133 | `"                        attempted_model=candidate_model,"` | — |
| [SRC-1AE03B9EC3-L003134](../../agents/web_agent.py#L3134) | 3134 | `"                        status=\"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L003135](../../agents/web_agent.py#L3135) | 3135 | `"                        error_class=type(exc).__name__,"` | — |
| [SRC-1AE03B9EC3-L003136](../../agents/web_agent.py#L3136) | 3136 | `"                        request_started=False,"` | — |
| [SRC-1AE03B9EC3-L003137](../../agents/web_agent.py#L3137) | 3137 | `"                        remote_response_received=False,"` | — |
| [SRC-1AE03B9EC3-L003138](../../agents/web_agent.py#L3138) | 3138 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003139](../../agents/web_agent.py#L3139) | 3139 | `"                    raise"` | — |
| [SRC-1AE03B9EC3-L003140](../../agents/web_agent.py#L3140) | 3140 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L003141](../../agents/web_agent.py#L3141) | 3141 | `"                request_timeout = timeout or self.timeout"` | — |
| [SRC-1AE03B9EC3-L003142](../../agents/web_agent.py#L3142) | 3142 | `"            request_payload: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L003143](../../agents/web_agent.py#L3143) | 3143 | `"                \"model\": candidate_model,"` | — |
| [SRC-1AE03B9EC3-L003144](../../agents/web_agent.py#L3144) | 3144 | `"                \"messages\": messages,"` | — |
| [SRC-1AE03B9EC3-L003145](../../agents/web_agent.py#L3145) | 3145 | `"                \"temperature\": temperature,"` | — |
| [SRC-1AE03B9EC3-L003146](../../agents/web_agent.py#L3146) | 3146 | `"                \"max_tokens\": max(100, min(int(max_tokens), 3000)),"` | — |
| [SRC-1AE03B9EC3-L003147](../../agents/web_agent.py#L3147) | 3147 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003148](../../agents/web_agent.py#L3148) | 3148 | `"            if use_web_search:"` | — |
| [SRC-1AE03B9EC3-L003149](../../agents/web_agent.py#L3149) | 3149 | `"                # OpenRouter executes these searches server-side and returns URL citations."` | — |
| [SRC-1AE03B9EC3-L003150](../../agents/web_agent.py#L3150) | 3150 | `"                # This is opt-in because provider search incurs usage charges."` | — |
| [SRC-1AE03B9EC3-L003151](../../agents/web_agent.py#L3151) | 3151 | `"                request_payload[\"tools\"] = [{"` | — |
| [SRC-1AE03B9EC3-L003152](../../agents/web_agent.py#L3152) | 3152 | `"                    \"type\": \"openrouter:web_search\","` | — |
| [SRC-1AE03B9EC3-L003153](../../agents/web_agent.py#L3153) | 3153 | `"                    \"parameters\": {"` | — |
| [SRC-1AE03B9EC3-L003154](../../agents/web_agent.py#L3154) | 3154 | `"                        \"engine\": \"auto\","` | — |
| [SRC-1AE03B9EC3-L003155](../../agents/web_agent.py#L3155) | 3155 | `"                        \"max_results\": 5,"` | — |
| [SRC-1AE03B9EC3-L003156](../../agents/web_agent.py#L3156) | 3156 | `"                        \"max_total_results\": 12,"` | — |
| [SRC-1AE03B9EC3-L003157](../../agents/web_agent.py#L3157) | 3157 | `"                        \"max_uses\": 3,"` | — |
| [SRC-1AE03B9EC3-L003158](../../agents/web_agent.py#L3158) | 3158 | `"                        \"search_context_size\": \"medium\","` | — |
| [SRC-1AE03B9EC3-L003159](../../agents/web_agent.py#L3159) | 3159 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L003160](../../agents/web_agent.py#L3160) | 3160 | `"                }]"` | — |
| [SRC-1AE03B9EC3-L003161](../../agents/web_agent.py#L3161) | 3161 | `"                request_payload[\"max_tool_calls\"] = 5"` | — |
| [SRC-1AE03B9EC3-L003162](../../agents/web_agent.py#L3162) | 3162 | `"            payload = json.dumps(request_payload, ensure_ascii=False).encode(\"utf-8\")"` | — |
| [SRC-1AE03B9EC3-L003163](../../agents/web_agent.py#L3163) | 3163 | `"            request = urllib.request.Request("` | — |
| [SRC-1AE03B9EC3-L003164](../../agents/web_agent.py#L3164) | 3164 | `"                self.base_url + \"/chat/completions\","` | — |
| [SRC-1AE03B9EC3-L003165](../../agents/web_agent.py#L3165) | 3165 | `"                data=payload,"` | — |
| [SRC-1AE03B9EC3-L003166](../../agents/web_agent.py#L3166) | 3166 | `"                headers={"` | — |
| [SRC-1AE03B9EC3-L003167](../../agents/web_agent.py#L3167) | 3167 | `"                    \"Authorization\": \"Bearer \" + self.api_key,"` | — |
| [SRC-1AE03B9EC3-L003168](../../agents/web_agent.py#L3168) | 3168 | `"                    \"Content-Type\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L003169](../../agents/web_agent.py#L3169) | 3169 | `"                    \"HTTP-Referer\": \"https://github.com/mosabosama2030-oss/omarai\","` | — |
| [SRC-1AE03B9EC3-L003170](../../agents/web_agent.py#L3170) | 3170 | `"                    \"X-Title\": \"Omarai Web Agent\","` | — |
| [SRC-1AE03B9EC3-L003171](../../agents/web_agent.py#L3171) | 3171 | `"                },"` | — |
| [SRC-1AE03B9EC3-L003172](../../agents/web_agent.py#L3172) | 3172 | `"                method=\"POST\","` | — |
| [SRC-1AE03B9EC3-L003173](../../agents/web_agent.py#L3173) | 3173 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003174](../../agents/web_agent.py#L3174) | 3174 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L003175](../../agents/web_agent.py#L3175) | 3175 | `"                with urllib.request.urlopen(request, timeout=request_timeout) as response:"` | — |
| [SRC-1AE03B9EC3-L003176](../../agents/web_agent.py#L3176) | 3176 | `"                    data = json.loads(response.read(2_000_000).decode(\"utf-8\"))"` | — |
| [SRC-1AE03B9EC3-L003177](../../agents/web_agent.py#L3177) | 3177 | `"                choice = data[\"choices\"][0]"` | — |
| [SRC-1AE03B9EC3-L003178](../../agents/web_agent.py#L3178) | 3178 | `"                if not isinstance(choice, dict):"` | — |
| [SRC-1AE03B9EC3-L003179](../../agents/web_agent.py#L3179) | 3179 | `"                    raise TypeError(\"invalid completion choice\")"` | — |
| [SRC-1AE03B9EC3-L003180](../../agents/web_agent.py#L3180) | 3180 | `"                finish_reason = choice.get(\"finish_reason\")"` | — |
| [SRC-1AE03B9EC3-L003181](../../agents/web_agent.py#L3181) | 3181 | `"                normalized_finish_reason = ("` | — |
| [SRC-1AE03B9EC3-L003182](../../agents/web_agent.py#L3182) | 3182 | `"                    finish_reason.strip().lower()"` | — |
| [SRC-1AE03B9EC3-L003183](../../agents/web_agent.py#L3183) | 3183 | `"                    if isinstance(finish_reason, str)"` | — |
| [SRC-1AE03B9EC3-L003184](../../agents/web_agent.py#L3184) | 3184 | `"                    else \"\""` | — |
| [SRC-1AE03B9EC3-L003185](../../agents/web_agent.py#L3185) | 3185 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003186](../../agents/web_agent.py#L3186) | 3186 | `"                # This application consumes a final text completion from an"` | — |
| [SRC-1AE03B9EC3-L003187](../../agents/web_agent.py#L3187) | 3187 | `"                # OpenAI-compatible /chat/completions endpoint. Fail closed when the"` | — |
| [SRC-1AE03B9EC3-L003188](../../agents/web_agent.py#L3188) | 3188 | `"                # provider does not explicitly report the standardized \"stop\" reason."` | — |
| [SRC-1AE03B9EC3-L003189](../../agents/web_agent.py#L3189) | 3189 | `"                if normalized_finish_reason != \"stop\":"` | — |
| [SRC-1AE03B9EC3-L003190](../../agents/web_agent.py#L3190) | 3190 | `"                    if normalized_finish_reason in {\"length\", \"max_tokens\"}:"` | — |
| [SRC-1AE03B9EC3-L003191](../../agents/web_agent.py#L3191) | 3191 | `"                        diagnostic_status = \"truncated\""` | — |
| [SRC-1AE03B9EC3-L003192](../../agents/web_agent.py#L3192) | 3192 | `"                        last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L003193](../../agents/web_agent.py#L3193) | 3193 | `"                            \"أعاد نموذج اللغة إجابة مبتورة بسبب الوصول إلى حد الرموز؛ \""` | — |
| [SRC-1AE03B9EC3-L003194](../../agents/web_agent.py#L3194) | 3194 | `"                            \"لم تُقبل كإجابة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L003195](../../agents/web_agent.py#L3195) | 3195 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003196](../../agents/web_agent.py#L3196) | 3196 | `"                    elif not normalized_finish_reason:"` | — |
| [SRC-1AE03B9EC3-L003197](../../agents/web_agent.py#L3197) | 3197 | `"                        diagnostic_status = \"finish_reason_missing\""` | — |
| [SRC-1AE03B9EC3-L003198](../../agents/web_agent.py#L3198) | 3198 | `"                        last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L003199](../../agents/web_agent.py#L3199) | 3199 | `"                            \"لم تقدم خدمة النموذج سبب انتهاء واضحًا؛ لم تُقبل الإجابة \""` | — |
| [SRC-1AE03B9EC3-L003200](../../agents/web_agent.py#L3200) | 3200 | `"                            \"كإجابة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L003201](../../agents/web_agent.py#L3201) | 3201 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003202](../../agents/web_agent.py#L3202) | 3202 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L003203](../../agents/web_agent.py#L3203) | 3203 | `"                        diagnostic_status = \"finish_reason_not_accepted\""` | — |
| [SRC-1AE03B9EC3-L003204](../../agents/web_agent.py#L3204) | 3204 | `"                        last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L003205](../../agents/web_agent.py#L3205) | 3205 | `"                            \"لم تُكمل خدمة النموذج إجابة نصية نهائية مقبولة \""` | — |
| [SRC-1AE03B9EC3-L003206](../../agents/web_agent.py#L3206) | 3206 | `"                            \"(حالة الإنهاء: \" + normalized_finish_reason[:40] + \").\""` | — |
| [SRC-1AE03B9EC3-L003207](../../agents/web_agent.py#L3207) | 3207 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003208](../../agents/web_agent.py#L3208) | 3208 | `"                    self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L003209](../../agents/web_agent.py#L3209) | 3209 | `"                        requested_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L003210](../../agents/web_agent.py#L3210) | 3210 | `"                        attempted_model=candidate_model,"` | — |
| [SRC-1AE03B9EC3-L003211](../../agents/web_agent.py#L3211) | 3211 | `"                        status=diagnostic_status,"` | — |
| [SRC-1AE03B9EC3-L003212](../../agents/web_agent.py#L3212) | 3212 | `"                        finish_reason=normalized_finish_reason or None,"` | — |
| [SRC-1AE03B9EC3-L003213](../../agents/web_agent.py#L3213) | 3213 | `"                        request_started=True,"` | — |
| [SRC-1AE03B9EC3-L003214](../../agents/web_agent.py#L3214) | 3214 | `"                        remote_response_received=True,"` | — |
| [SRC-1AE03B9EC3-L003215](../../agents/web_agent.py#L3215) | 3215 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003216](../../agents/web_agent.py#L3216) | 3216 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L003217](../../agents/web_agent.py#L3217) | 3217 | `"                message = choice[\"message\"]"` | — |
| [SRC-1AE03B9EC3-L003218](../../agents/web_agent.py#L3218) | 3218 | `"                answer = message[\"content\"]"` | — |
| [SRC-1AE03B9EC3-L003219](../../agents/web_agent.py#L3219) | 3219 | `"                if use_web_search:"` | — |
| [SRC-1AE03B9EC3-L003220](../../agents/web_agent.py#L3220) | 3220 | `"                    for annotation in message.get(\"annotations\", []):"` | — |
| [SRC-1AE03B9EC3-L003221](../../agents/web_agent.py#L3221) | 3221 | `"                        if not isinstance(annotation, dict) or annotation.get(\"type\") != \"url_citation\":"` | — |
| [SRC-1AE03B9EC3-L003222](../../agents/web_agent.py#L3222) | 3222 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L003223](../../agents/web_agent.py#L3223) | 3223 | `"                        citation = annotation.get(\"url_citation\", annotation)"` | — |
| [SRC-1AE03B9EC3-L003224](../../agents/web_agent.py#L3224) | 3224 | `"                        if not isinstance(citation, dict):"` | — |
| [SRC-1AE03B9EC3-L003225](../../agents/web_agent.py#L3225) | 3225 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L003226](../../agents/web_agent.py#L3226) | 3226 | `"                        url = _public_http_url(citation.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L003227](../../agents/web_agent.py#L3227) | 3227 | `"                        if not url or any(item.get(\"url\") == url for item in self.server_search_sources):"` | — |
| [SRC-1AE03B9EC3-L003228](../../agents/web_agent.py#L3228) | 3228 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L003229](../../agents/web_agent.py#L3229) | 3229 | `"                        parsed_url = urllib.parse.urlparse(url)"` | — |
| [SRC-1AE03B9EC3-L003230](../../agents/web_agent.py#L3230) | 3230 | `"                        excerpt = _clean_text(citation.get(\"content\", \"\"), 1800)"` | — |
| [SRC-1AE03B9EC3-L003231](../../agents/web_agent.py#L3231) | 3231 | `"                        self.server_search_sources.append({"` | — |
| [SRC-1AE03B9EC3-L003232](../../agents/web_agent.py#L3232) | 3232 | `"                            \"title\": _clean_text(citation.get(\"title\", \"\"), 300) or parsed_url.netloc,"` | — |
| [SRC-1AE03B9EC3-L003233](../../agents/web_agent.py#L3233) | 3233 | `"                            \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L003234](../../agents/web_agent.py#L3234) | 3234 | `"                            \"snippet\": excerpt,"` | — |
| [SRC-1AE03B9EC3-L003235](../../agents/web_agent.py#L3235) | 3235 | `"                            \"page_text\": excerpt,"` | — |
| [SRC-1AE03B9EC3-L003236](../../agents/web_agent.py#L3236) | 3236 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L003237](../../agents/web_agent.py#L3237) | 3237 | `"                            \"provider\": \"openrouter_web_search\","` | — |
| [SRC-1AE03B9EC3-L003238](../../agents/web_agent.py#L3238) | 3238 | `"                            \"providers\": [\"openrouter_web_search\"],"` | — |
| [SRC-1AE03B9EC3-L003239](../../agents/web_agent.py#L3239) | 3239 | `"                            \"queries\": [],"` | — |
| [SRC-1AE03B9EC3-L003240](../../agents/web_agent.py#L3240) | 3240 | `"                            \"domain\": parsed_url.netloc.lower(),"` | — |
| [SRC-1AE03B9EC3-L003241](../../agents/web_agent.py#L3241) | 3241 | `"                            \"source_class\": \"general\","` | — |
| [SRC-1AE03B9EC3-L003242](../../agents/web_agent.py#L3242) | 3242 | `"                            \"platform\": \"web\","` | — |
| [SRC-1AE03B9EC3-L003243](../../agents/web_agent.py#L3243) | 3243 | `"                            \"published_at\": \"\","` | — |
| [SRC-1AE03B9EC3-L003244](../../agents/web_agent.py#L3244) | 3244 | `"                            \"rank_score\": 0.0,"` | — |
| [SRC-1AE03B9EC3-L003245](../../agents/web_agent.py#L3245) | 3245 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L003246](../../agents/web_agent.py#L3246) | 3246 | `"                if isinstance(answer, list):"` | — |
| [SRC-1AE03B9EC3-L003247](../../agents/web_agent.py#L3247) | 3247 | `"                    answer = \"\".join("` | — |
| [SRC-1AE03B9EC3-L003248](../../agents/web_agent.py#L3248) | 3248 | `"                        item.get(\"text\", \"\") for item in answer if isinstance(item, dict)"` | — |
| [SRC-1AE03B9EC3-L003249](../../agents/web_agent.py#L3249) | 3249 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003250](../../agents/web_agent.py#L3250) | 3250 | `"                if not isinstance(answer, str) or not answer.strip():"` | — |
| [SRC-1AE03B9EC3-L003251](../../agents/web_agent.py#L3251) | 3251 | `"                    raise ValueError(\"empty model response\")"` | — |
| [SRC-1AE03B9EC3-L003252](../../agents/web_agent.py#L3252) | 3252 | `"                self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L003253](../../agents/web_agent.py#L3253) | 3253 | `"                    requested_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L003254](../../agents/web_agent.py#L3254) | 3254 | `"                    attempted_model=candidate_model,"` | — |
| [SRC-1AE03B9EC3-L003255](../../agents/web_agent.py#L3255) | 3255 | `"                    status=\"accepted\","` | — |
| [SRC-1AE03B9EC3-L003256](../../agents/web_agent.py#L3256) | 3256 | `"                    finish_reason=normalized_finish_reason,"` | — |
| [SRC-1AE03B9EC3-L003257](../../agents/web_agent.py#L3257) | 3257 | `"                    request_started=True,"` | — |
| [SRC-1AE03B9EC3-L003258](../../agents/web_agent.py#L3258) | 3258 | `"                    remote_response_received=True,"` | — |
| [SRC-1AE03B9EC3-L003259](../../agents/web_agent.py#L3259) | 3259 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003260](../../agents/web_agent.py#L3260) | 3260 | `"                self.model_usage.append(_model_usage_record("` | — |
| [SRC-1AE03B9EC3-L003261](../../agents/web_agent.py#L3261) | 3261 | `"                    requested_model, candidate_model,"` | — |
| [SRC-1AE03B9EC3-L003262](../../agents/web_agent.py#L3262) | 3262 | `"                    data, self.base_url,"` | — |
| [SRC-1AE03B9EC3-L003263](../../agents/web_agent.py#L3263) | 3263 | `"                    # Keep this to allowlisted usage counters, never raw provider data."` | — |
| [SRC-1AE03B9EC3-L003264](../../agents/web_agent.py#L3264) | 3264 | `"                ))"` | — |
| [SRC-1AE03B9EC3-L003265](../../agents/web_agent.py#L3265) | 3265 | `"                return answer.strip()"` | — |
| [SRC-1AE03B9EC3-L003266](../../agents/web_agent.py#L3266) | 3266 | `"            except urllib.error.HTTPError as exc:"` | — |
| [SRC-1AE03B9EC3-L003267](../../agents/web_agent.py#L3267) | 3267 | `"                # Never echo provider response bodies: they may contain private diagnostics."` | — |
| [SRC-1AE03B9EC3-L003268](../../agents/web_agent.py#L3268) | 3268 | `"                self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L003269](../../agents/web_agent.py#L3269) | 3269 | `"                    requested_model, candidate_model, \"provider_http_error\","` | — |
| [SRC-1AE03B9EC3-L003270](../../agents/web_agent.py#L3270) | 3270 | `"                    error_class=\"HTTPError\", request_started=True,"` | — |
| [SRC-1AE03B9EC3-L003271](../../agents/web_agent.py#L3271) | 3271 | `"                    remote_response_received=True,"` | — |
| [SRC-1AE03B9EC3-L003272](../../agents/web_agent.py#L3272) | 3272 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003273](../../agents/web_agent.py#L3273) | 3273 | `"                last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L003274](../../agents/web_agent.py#L3274) | 3274 | `"                    f\"خدمة نموذج اللغة رفضت الطلب (HTTP {exc.code}) على النموذج المحدد.\""` | — |
| [SRC-1AE03B9EC3-L003275](../../agents/web_agent.py#L3275) | 3275 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003276](../../agents/web_agent.py#L3276) | 3276 | `"            except (urllib.error.URLError, TimeoutError, OSError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003277](../../agents/web_agent.py#L3277) | 3277 | `"                self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L003278](../../agents/web_agent.py#L3278) | 3278 | `"                    requested_model, candidate_model, \"connection_error\","` | — |
| [SRC-1AE03B9EC3-L003279](../../agents/web_agent.py#L3279) | 3279 | `"                    error_class=type(exc).__name__, request_started=True,"` | — |
| [SRC-1AE03B9EC3-L003280](../../agents/web_agent.py#L3280) | 3280 | `"                    remote_response_received=None,"` | — |
| [SRC-1AE03B9EC3-L003281](../../agents/web_agent.py#L3281) | 3281 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003282](../../agents/web_agent.py#L3282) | 3282 | `"                last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L003283](../../agents/web_agent.py#L3283) | 3283 | `"                    \"تعذر الاتصال بخدمة نموذج اللغة؛ جرت محاولة استخدام النموذج الاحتياطي.\""` | — |
| [SRC-1AE03B9EC3-L003284](../../agents/web_agent.py#L3284) | 3284 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003285](../../agents/web_agent.py#L3285) | 3285 | `"            except (KeyError, IndexError, TypeError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003286](../../agents/web_agent.py#L3286) | 3286 | `"                self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L003287](../../agents/web_agent.py#L3287) | 3287 | `"                    requested_model, candidate_model, \"invalid_response\","` | — |
| [SRC-1AE03B9EC3-L003288](../../agents/web_agent.py#L3288) | 3288 | `"                    error_class=type(exc).__name__, request_started=True,"` | — |
| [SRC-1AE03B9EC3-L003289](../../agents/web_agent.py#L3289) | 3289 | `"                    remote_response_received=True,"` | — |
