# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **008**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L002368 إلى SRC-1AE03B9EC3-L003167
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L002368](../../agents/web_agent.py#L2368) | 2368 | `"        soup = BeautifulSoup(html, \"html.parser\")"` | — |
| [SRC-1AE03B9EC3-L002369](../../agents/web_agent.py#L2369) | 2369 | `"        title = _clean_text(soup.title.get_text(\" \", strip=True), 300) if soup.title else \"\""` | — |
| [SRC-1AE03B9EC3-L002370](../../agents/web_agent.py#L2370) | 2370 | `"        for element in soup(["` | — |
| [SRC-1AE03B9EC3-L002371](../../agents/web_agent.py#L2371) | 2371 | `"            \"script\", \"style\", \"nav\", \"footer\", \"header\", \"noscript\","` | — |
| [SRC-1AE03B9EC3-L002372](../../agents/web_agent.py#L2372) | 2372 | `"            \"svg\", \"form\", \"iframe\", \"template\""` | — |
| [SRC-1AE03B9EC3-L002373](../../agents/web_agent.py#L2373) | 2373 | `"        ]):"` | — |
| [SRC-1AE03B9EC3-L002374](../../agents/web_agent.py#L2374) | 2374 | `"            element.decompose()"` | — |
| [SRC-1AE03B9EC3-L002375](../../agents/web_agent.py#L2375) | 2375 | `"        main = soup.find(\"main\") or soup.find(\"article\") or soup.body or soup"` | — |
| [SRC-1AE03B9EC3-L002376](../../agents/web_agent.py#L2376) | 2376 | `"        bounded_text = _clean_text(main.get_text(\" \", strip=True), MAX_PAGE_TEXT_CHARS + 1)"` | — |
| [SRC-1AE03B9EC3-L002377](../../agents/web_agent.py#L2377) | 2377 | `"        text_truncated = len(bounded_text) > MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L002378](../../agents/web_agent.py#L2378) | 2378 | `"        page_text = _clean_text(bounded_text, MAX_PAGE_TEXT_CHARS)"` | — |
| [SRC-1AE03B9EC3-L002379](../../agents/web_agent.py#L2379) | 2379 | `"        status = ("` | — |
| [SRC-1AE03B9EC3-L002380](../../agents/web_agent.py#L2380) | 2380 | `"            \"no_text_extracted\" if not page_text"` | — |
| [SRC-1AE03B9EC3-L002381](../../agents/web_agent.py#L2381) | 2381 | `"            else \"partial_extraction\" if bytes_truncated or text_truncated"` | — |
| [SRC-1AE03B9EC3-L002382](../../agents/web_agent.py#L2382) | 2382 | `"            else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L002383](../../agents/web_agent.py#L2383) | 2383 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002384](../../agents/web_agent.py#L2384) | 2384 | `"        return result(title, page_text, status)"` | — |
| [SRC-1AE03B9EC3-L002385](../../agents/web_agent.py#L2385) | 2385 | `""` | — |
| [SRC-1AE03B9EC3-L002386](../../agents/web_agent.py#L2386) | 2386 | `"    def _collect_sources(self, query: str) -> tuple[list[dict[str, Any]], str \| None]:"` | — |
| [SRC-1AE03B9EC3-L002387](../../agents/web_agent.py#L2387) | 2387 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002388](../../agents/web_agent.py#L2388) | 2388 | `"            sources = self._search_web(query)"` | — |
| [SRC-1AE03B9EC3-L002389](../../agents/web_agent.py#L2389) | 2389 | `"        except (RuntimeError, AgentDependencyError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002390](../../agents/web_agent.py#L2390) | 2390 | `"            return [], str(exc)"` | — |
| [SRC-1AE03B9EC3-L002391](../../agents/web_agent.py#L2391) | 2391 | `"        for source in sources[:MAX_FETCHED_PAGES]:"` | — |
| [SRC-1AE03B9EC3-L002392](../../agents/web_agent.py#L2392) | 2392 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002393](../../agents/web_agent.py#L2393) | 2393 | `"                title, page_text = self._fetch_page(source[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L002394](../../agents/web_agent.py#L2394) | 2394 | `"            except (AgentDependencyError, RuntimeError):"` | — |
| [SRC-1AE03B9EC3-L002395](../../agents/web_agent.py#L2395) | 2395 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002396](../../agents/web_agent.py#L2396) | 2396 | `"            if title:"` | — |
| [SRC-1AE03B9EC3-L002397](../../agents/web_agent.py#L2397) | 2397 | `"                source[\"title\"] = title"` | — |
| [SRC-1AE03B9EC3-L002398](../../agents/web_agent.py#L2398) | 2398 | `"            if page_text:"` | — |
| [SRC-1AE03B9EC3-L002399](../../agents/web_agent.py#L2399) | 2399 | `"                source[\"page_text\"] = page_text"` | — |
| [SRC-1AE03B9EC3-L002400](../../agents/web_agent.py#L2400) | 2400 | `"                source[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L002401](../../agents/web_agent.py#L2401) | 2401 | `"                # Prefer extracted text over a thin search snippet."` | — |
| [SRC-1AE03B9EC3-L002402](../../agents/web_agent.py#L2402) | 2402 | `"                source[\"snippet\"] = page_text[:1800]"` | — |
| [SRC-1AE03B9EC3-L002403](../../agents/web_agent.py#L2403) | 2403 | `"        return sources, None"` | — |
| [SRC-1AE03B9EC3-L002404](../../agents/web_agent.py#L2404) | 2404 | `""` | — |
| [SRC-1AE03B9EC3-L002405](../../agents/web_agent.py#L2405) | 2405 | `"    def _collect_research("` | — |
| [SRC-1AE03B9EC3-L002406](../../agents/web_agent.py#L2406) | 2406 | `"        self, plan: dict[str, Any]"` | — |
| [SRC-1AE03B9EC3-L002407](../../agents/web_agent.py#L2407) | 2407 | `"    ) -> tuple[list[dict[str, Any]], list[str], dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L002408](../../agents/web_agent.py#L2408) | 2408 | `"        \"\"\"Run independent query searches concurrently, fuse evidence, then fetch top pages.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002409](../../agents/web_agent.py#L2409) | 2409 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002410](../../agents/web_agent.py#L2410) | 2410 | `"            query_limit = int(plan.get(\"query_limit\", MAX_PLAN_QUERIES))"` | — |
| [SRC-1AE03B9EC3-L002411](../../agents/web_agent.py#L2411) | 2411 | `"        except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L002412](../../agents/web_agent.py#L2412) | 2412 | `"            query_limit = MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L002413](../../agents/web_agent.py#L2413) | 2413 | `"        query_limit = max(1, min(query_limit, MAX_PLAN_QUERIES))"` | — |
| [SRC-1AE03B9EC3-L002414](../../agents/web_agent.py#L2414) | 2414 | `"        queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L002415](../../agents/web_agent.py#L2415) | 2415 | `"            compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L002416](../../agents/web_agent.py#L2416) | 2416 | `"            for query in plan.get(\"queries\", [])[:query_limit]"` | — |
| [SRC-1AE03B9EC3-L002417](../../agents/web_agent.py#L2417) | 2417 | `"            if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L002418](../../agents/web_agent.py#L2418) | 2418 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L002419](../../agents/web_agent.py#L2419) | 2419 | `"        queries = [query for query in queries if query]"` | — |
| [SRC-1AE03B9EC3-L002420](../../agents/web_agent.py#L2420) | 2420 | `"        warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002421](../../agents/web_agent.py#L2421) | 2421 | `"        if not queries and not plan.get(\"direct_urls\"):"` | — |
| [SRC-1AE03B9EC3-L002422](../../agents/web_agent.py#L2422) | 2422 | `"            warnings.append(\"لم يُنشأ استعلام موضوعي قابل للبحث؛ لم تُستدعَ محركات البحث.\")"` | — |
| [SRC-1AE03B9EC3-L002423](../../agents/web_agent.py#L2423) | 2423 | `"        batches: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002424](../../agents/web_agent.py#L2424) | 2424 | `"        query_counts: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002425](../../agents/web_agent.py#L2425) | 2425 | `"        search_started_queries = 0"` | — |
| [SRC-1AE03B9EC3-L002426](../../agents/web_agent.py#L2426) | 2426 | `""` | — |
| [SRC-1AE03B9EC3-L002427](../../agents/web_agent.py#L2427) | 2427 | `"        if queries:"` | — |
| [SRC-1AE03B9EC3-L002428](../../agents/web_agent.py#L2428) | 2428 | `"            with ThreadPoolExecutor(max_workers=min(MAX_RESEARCH_WORKERS, len(queries))) as pool:"` | — |
| [SRC-1AE03B9EC3-L002429](../../agents/web_agent.py#L2429) | 2429 | `"                futures = {pool.submit(self._search_web, query): query for query in queries}"` | — |
| [SRC-1AE03B9EC3-L002430](../../agents/web_agent.py#L2430) | 2430 | `"                for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002431](../../agents/web_agent.py#L2431) | 2431 | `"                    query = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002432](../../agents/web_agent.py#L2432) | 2432 | `"                    search_started_queries += 1"` | — |
| [SRC-1AE03B9EC3-L002433](../../agents/web_agent.py#L2433) | 2433 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002434](../../agents/web_agent.py#L2434) | 2434 | `"                        results = future.result()"` | — |
| [SRC-1AE03B9EC3-L002435](../../agents/web_agent.py#L2435) | 2435 | `"                    except (RequestBudgetExceeded, RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002436](../../agents/web_agent.py#L2436) | 2436 | `"                        warnings.append(f\"تعذر بحث الاستعلام «{query[:70]}»: {exc}\")"` | — |
| [SRC-1AE03B9EC3-L002437](../../agents/web_agent.py#L2437) | 2437 | `"                        query_counts.append({\"query\": query, \"results\": 0})"` | — |
| [SRC-1AE03B9EC3-L002438](../../agents/web_agent.py#L2438) | 2438 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002439](../../agents/web_agent.py#L2439) | 2439 | `"                    query_counts.append({\"query\": query, \"results\": len(results)})"` | — |
| [SRC-1AE03B9EC3-L002440](../../agents/web_agent.py#L2440) | 2440 | `"                    grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002441](../../agents/web_agent.py#L2441) | 2441 | `"                    for source in results:"` | — |
| [SRC-1AE03B9EC3-L002442](../../agents/web_agent.py#L2442) | 2442 | `"                        provider = str(source.get(\"provider\") or \"web_search\")"` | — |
| [SRC-1AE03B9EC3-L002443](../../agents/web_agent.py#L2443) | 2443 | `"                        grouped.setdefault(provider, []).append(source)"` | — |
| [SRC-1AE03B9EC3-L002444](../../agents/web_agent.py#L2444) | 2444 | `"                    for provider, items in grouped.items():"` | — |
| [SRC-1AE03B9EC3-L002445](../../agents/web_agent.py#L2445) | 2445 | `"                        items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002446](../../agents/web_agent.py#L2446) | 2446 | `"                        batches.append({\"query\": query, \"provider\": provider, \"results\": items})"` | — |
| [SRC-1AE03B9EC3-L002447](../../agents/web_agent.py#L2447) | 2447 | `""` | — |
| [SRC-1AE03B9EC3-L002448](../../agents/web_agent.py#L2448) | 2448 | `"        # Evidence-gap iteration: deep tasks get up to three targeted follow-up searches"` | — |
| [SRC-1AE03B9EC3-L002449](../../agents/web_agent.py#L2449) | 2449 | `"        # when initial coverage is thin. This uses observed source/domain/provider coverage,"` | — |
| [SRC-1AE03B9EC3-L002450](../../agents/web_agent.py#L2450) | 2450 | `"        # not the language model's subjective claim that it has enough evidence."` | — |
| [SRC-1AE03B9EC3-L002451](../../agents/web_agent.py#L2451) | 2451 | `"        preliminary = fuse_ranked_results(batches, limit=MAX_SEARCH_RESULTS)"` | — |
| [SRC-1AE03B9EC3-L002452](../../agents/web_agent.py#L2452) | 2452 | `"        preliminary_domains = {"` | — |
| [SRC-1AE03B9EC3-L002453](../../agents/web_agent.py#L2453) | 2453 | `"            registrable_domain(item.get(\"domain\") or urllib.parse.urlparse(item.get(\"url\", \"\")).hostname)"` | — |
| [SRC-1AE03B9EC3-L002454](../../agents/web_agent.py#L2454) | 2454 | `"            for item in preliminary"` | — |
| [SRC-1AE03B9EC3-L002455](../../agents/web_agent.py#L2455) | 2455 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002456](../../agents/web_agent.py#L2456) | 2456 | `"        preliminary_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L002457](../../agents/web_agent.py#L2457) | 2457 | `"        preliminary_providers = {"` | — |
| [SRC-1AE03B9EC3-L002458](../../agents/web_agent.py#L2458) | 2458 | `"            provider for item in preliminary for provider in item.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L002459](../../agents/web_agent.py#L2459) | 2459 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002460](../../agents/web_agent.py#L2460) | 2460 | `"        needs_expansion = ("` | — |
| [SRC-1AE03B9EC3-L002461](../../agents/web_agent.py#L2461) | 2461 | `"            plan.get(\"depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L002462](../../agents/web_agent.py#L2462) | 2462 | `"            and (len(preliminary) < 8 or len(preliminary_domains) < 5 or len(preliminary_providers) < 2)"` | — |
| [SRC-1AE03B9EC3-L002463](../../agents/web_agent.py#L2463) | 2463 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002464](../../agents/web_agent.py#L2464) | 2464 | `"        expansion_queries: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002465](../../agents/web_agent.py#L2465) | 2465 | `"        if needs_expansion and len(queries) < query_limit and queries:"` | — |
| [SRC-1AE03B9EC3-L002466](../../agents/web_agent.py#L2466) | 2466 | `"            base_query = (queries[0] if queries else \"\")"` | — |
| [SRC-1AE03B9EC3-L002467](../../agents/web_agent.py#L2467) | 2467 | `"            candidates = ["` | — |
| [SRC-1AE03B9EC3-L002468](../../agents/web_agent.py#L2468) | 2468 | `"                f\"{base_query} official sources data reports\","` | — |
| [SRC-1AE03B9EC3-L002469](../../agents/web_agent.py#L2469) | 2469 | `"                f\"{base_query} limitations risks criticism alternatives\","` | — |
| [SRC-1AE03B9EC3-L002470](../../agents/web_agent.py#L2470) | 2470 | `"                f\"{base_query} recent developments case studies analysis\","` | — |
| [SRC-1AE03B9EC3-L002471](../../agents/web_agent.py#L2471) | 2471 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L002472](../../agents/web_agent.py#L2472) | 2472 | `"            existing = {item.casefold() for item in queries}"` | — |
| [SRC-1AE03B9EC3-L002473](../../agents/web_agent.py#L2473) | 2473 | `"            expansion_queries = []"` | — |
| [SRC-1AE03B9EC3-L002474](../../agents/web_agent.py#L2474) | 2474 | `"            seen_expansions = set(existing)"` | — |
| [SRC-1AE03B9EC3-L002475](../../agents/web_agent.py#L2475) | 2475 | `"            for candidate in candidates:"` | — |
| [SRC-1AE03B9EC3-L002476](../../agents/web_agent.py#L2476) | 2476 | `"                compacted = compact_search_query(candidate)"` | — |
| [SRC-1AE03B9EC3-L002477](../../agents/web_agent.py#L2477) | 2477 | `"                key = compacted.casefold()"` | — |
| [SRC-1AE03B9EC3-L002478](../../agents/web_agent.py#L2478) | 2478 | `"                if compacted and key not in seen_expansions:"` | — |
| [SRC-1AE03B9EC3-L002479](../../agents/web_agent.py#L2479) | 2479 | `"                    expansion_queries.append(compacted)"` | — |
| [SRC-1AE03B9EC3-L002480](../../agents/web_agent.py#L2480) | 2480 | `"                    seen_expansions.add(key)"` | — |
| [SRC-1AE03B9EC3-L002481](../../agents/web_agent.py#L2481) | 2481 | `"                if len(expansion_queries) >= max(0, query_limit - len(queries)):"` | — |
| [SRC-1AE03B9EC3-L002482](../../agents/web_agent.py#L2482) | 2482 | `"                    break"` | — |
| [SRC-1AE03B9EC3-L002483](../../agents/web_agent.py#L2483) | 2483 | `"            if expansion_queries:"` | — |
| [SRC-1AE03B9EC3-L002484](../../agents/web_agent.py#L2484) | 2484 | `"                with ThreadPoolExecutor("` | — |
| [SRC-1AE03B9EC3-L002485](../../agents/web_agent.py#L2485) | 2485 | `"                    max_workers=min(MAX_RESEARCH_WORKERS, len(expansion_queries))"` | — |
| [SRC-1AE03B9EC3-L002486](../../agents/web_agent.py#L2486) | 2486 | `"                ) as pool:"` | — |
| [SRC-1AE03B9EC3-L002487](../../agents/web_agent.py#L2487) | 2487 | `"                    futures = {"` | — |
| [SRC-1AE03B9EC3-L002488](../../agents/web_agent.py#L2488) | 2488 | `"                        pool.submit(self._search_web, query): query"` | — |
| [SRC-1AE03B9EC3-L002489](../../agents/web_agent.py#L2489) | 2489 | `"                        for query in expansion_queries"` | — |
| [SRC-1AE03B9EC3-L002490](../../agents/web_agent.py#L2490) | 2490 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L002491](../../agents/web_agent.py#L2491) | 2491 | `"                    for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002492](../../agents/web_agent.py#L2492) | 2492 | `"                        query = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002493](../../agents/web_agent.py#L2493) | 2493 | `"                        search_started_queries += 1"` | — |
| [SRC-1AE03B9EC3-L002494](../../agents/web_agent.py#L2494) | 2494 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L002495](../../agents/web_agent.py#L2495) | 2495 | `"                            results = future.result()"` | — |
| [SRC-1AE03B9EC3-L002496](../../agents/web_agent.py#L2496) | 2496 | `"                        except (RequestBudgetExceeded, RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002497](../../agents/web_agent.py#L2497) | 2497 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002498](../../agents/web_agent.py#L2498) | 2498 | `"                                f\"تعذر بحث زاوية إضافية «{query[:70]}»: {exc}\""` | — |
| [SRC-1AE03B9EC3-L002499](../../agents/web_agent.py#L2499) | 2499 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002500](../../agents/web_agent.py#L2500) | 2500 | `"                            query_counts.append({\"query\": query, \"results\": 0})"` | — |
| [SRC-1AE03B9EC3-L002501](../../agents/web_agent.py#L2501) | 2501 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002502](../../agents/web_agent.py#L2502) | 2502 | `"                        query_counts.append({\"query\": query, \"results\": len(results)})"` | — |
| [SRC-1AE03B9EC3-L002503](../../agents/web_agent.py#L2503) | 2503 | `"                        grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002504](../../agents/web_agent.py#L2504) | 2504 | `"                        for source in results:"` | — |
| [SRC-1AE03B9EC3-L002505](../../agents/web_agent.py#L2505) | 2505 | `"                            grouped.setdefault("` | — |
| [SRC-1AE03B9EC3-L002506](../../agents/web_agent.py#L2506) | 2506 | `"                                str(source.get(\"provider\") or \"web_search\"), []"` | — |
| [SRC-1AE03B9EC3-L002507](../../agents/web_agent.py#L2507) | 2507 | `"                            ).append(source)"` | — |
| [SRC-1AE03B9EC3-L002508](../../agents/web_agent.py#L2508) | 2508 | `"                        for provider, items in grouped.items():"` | — |
| [SRC-1AE03B9EC3-L002509](../../agents/web_agent.py#L2509) | 2509 | `"                            items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002510](../../agents/web_agent.py#L2510) | 2510 | `"                            batches.append({"` | — |
| [SRC-1AE03B9EC3-L002511](../../agents/web_agent.py#L2511) | 2511 | `"                                \"query\": query, \"provider\": provider, \"results\": items"` | — |
| [SRC-1AE03B9EC3-L002512](../../agents/web_agent.py#L2512) | 2512 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L002513](../../agents/web_agent.py#L2513) | 2513 | `"                queries.extend(expansion_queries)"` | — |
| [SRC-1AE03B9EC3-L002514](../../agents/web_agent.py#L2514) | 2514 | `"                plan[\"queries\"] = list(queries)"` | — |
| [SRC-1AE03B9EC3-L002515](../../agents/web_agent.py#L2515) | 2515 | `""` | — |
| [SRC-1AE03B9EC3-L002516](../../agents/web_agent.py#L2516) | 2516 | `"        # Google News RSS is included concurrently by _search_web for freshness-bearing queries."` | — |
| [SRC-1AE03B9EC3-L002517](../../agents/web_agent.py#L2517) | 2517 | `""` | — |
| [SRC-1AE03B9EC3-L002518](../../agents/web_agent.py#L2518) | 2518 | `"        # A social-focused task uses public social endpoints in parallel with indexed"` | — |
| [SRC-1AE03B9EC3-L002519](../../agents/web_agent.py#L2519) | 2519 | `"        # public pages. No login, private profile, session cookie or anti-bot bypass."` | — |
| [SRC-1AE03B9EC3-L002520](../../agents/web_agent.py#L2520) | 2520 | `"        social_results: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002521](../../agents/web_agent.py#L2521) | 2521 | `"        if plan.get(\"social_focus\") and queries:"` | — |
| [SRC-1AE03B9EC3-L002522](../../agents/web_agent.py#L2522) | 2522 | `"            requested_platforms = plan.get(\"platforms\") or []"` | — |
| [SRC-1AE03B9EC3-L002523](../../agents/web_agent.py#L2523) | 2523 | `"            if requested_platforms:"` | — |
| [SRC-1AE03B9EC3-L002524](../../agents/web_agent.py#L2524) | 2524 | `"                platforms = list(dict.fromkeys(requested_platforms))"` | — |
| [SRC-1AE03B9EC3-L002525](../../agents/web_agent.py#L2525) | 2525 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002526](../../agents/web_agent.py#L2526) | 2526 | `"                # Broad social research: always try no-key public sources, and add"` | — |
| [SRC-1AE03B9EC3-L002527](../../agents/web_agent.py#L2527) | 2527 | `"                # official platform connectors only when they are configured."` | — |
| [SRC-1AE03B9EC3-L002528](../../agents/web_agent.py#L2528) | 2528 | `"                platforms = [\"reddit\", \"bluesky\"]"` | — |
| [SRC-1AE03B9EC3-L002529](../../agents/web_agent.py#L2529) | 2529 | `"                optional_connectors = {"` | — |
| [SRC-1AE03B9EC3-L002530](../../agents/web_agent.py#L2530) | 2530 | `"                    \"facebook\": bool("` | — |
| [SRC-1AE03B9EC3-L002531](../../agents/web_agent.py#L2531) | 2531 | `"                        os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002532](../../agents/web_agent.py#L2532) | 2532 | `"                        and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002533](../../agents/web_agent.py#L2533) | 2533 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L002534](../../agents/web_agent.py#L2534) | 2534 | `"                    \"instagram\": bool("` | — |
| [SRC-1AE03B9EC3-L002535](../../agents/web_agent.py#L2535) | 2535 | `"                        os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002536](../../agents/web_agent.py#L2536) | 2536 | `"                        and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002537](../../agents/web_agent.py#L2537) | 2537 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L002538](../../agents/web_agent.py#L2538) | 2538 | `"                    \"x\": bool(os.getenv(\"X_BEARER_TOKEN\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L002539](../../agents/web_agent.py#L2539) | 2539 | `"                    \"youtube\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L002540](../../agents/web_agent.py#L2540) | 2540 | `"                }"` | — |
| [SRC-1AE03B9EC3-L002541](../../agents/web_agent.py#L2541) | 2541 | `"                platforms.extend("` | — |
| [SRC-1AE03B9EC3-L002542](../../agents/web_agent.py#L2542) | 2542 | `"                    name for name, ready in optional_connectors.items()"` | — |
| [SRC-1AE03B9EC3-L002543](../../agents/web_agent.py#L2543) | 2543 | `"                    if ready and name not in platforms"` | — |
| [SRC-1AE03B9EC3-L002544](../../agents/web_agent.py#L2544) | 2544 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002545](../../agents/web_agent.py#L2545) | 2545 | `"            social_results, social_warnings = self._search_social((queries[0] if queries else \"\"), platforms)"` | — |
| [SRC-1AE03B9EC3-L002546](../../agents/web_agent.py#L2546) | 2546 | `"            warnings.extend(social_warnings)"` | — |
| [SRC-1AE03B9EC3-L002547](../../agents/web_agent.py#L2547) | 2547 | `"            social_groups: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002548](../../agents/web_agent.py#L2548) | 2548 | `"            for source in social_results:"` | — |
| [SRC-1AE03B9EC3-L002549](../../agents/web_agent.py#L2549) | 2549 | `"                social_groups.setdefault(str(source.get(\"provider\") or \"social\"), []).append(source)"` | — |
| [SRC-1AE03B9EC3-L002550](../../agents/web_agent.py#L2550) | 2550 | `"            for provider, items in social_groups.items():"` | — |
| [SRC-1AE03B9EC3-L002551](../../agents/web_agent.py#L2551) | 2551 | `"                items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002552](../../agents/web_agent.py#L2552) | 2552 | `"                batches.append({\"query\": (queries[0] if queries else \"\"), \"provider\": provider, \"results\": items})"` | — |
| [SRC-1AE03B9EC3-L002553](../../agents/web_agent.py#L2553) | 2553 | `""` | — |
| [SRC-1AE03B9EC3-L002554](../../agents/web_agent.py#L2554) | 2554 | `"        # Explicit URLs are first-class inputs: fetch the page the user actually asked about"` | — |
| [SRC-1AE03B9EC3-L002555](../../agents/web_agent.py#L2555) | 2555 | `"        # instead of relying on a search engine to rediscover it. URL and DNS checks still apply."` | — |
| [SRC-1AE03B9EC3-L002556](../../agents/web_agent.py#L2556) | 2556 | `"        direct_urls: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002557](../../agents/web_agent.py#L2557) | 2557 | `"        for value in plan.get(\"direct_urls\", [])[:5]:"` | — |
| [SRC-1AE03B9EC3-L002558](../../agents/web_agent.py#L2558) | 2558 | `"            safe_url = _public_http_url(value)"` | — |
| [SRC-1AE03B9EC3-L002559](../../agents/web_agent.py#L2559) | 2559 | `"            if safe_url and not _blocked_source_url(safe_url) and safe_url not in direct_urls:"` | — |
| [SRC-1AE03B9EC3-L002560](../../agents/web_agent.py#L2560) | 2560 | `"                direct_urls.append(safe_url)"` | — |
| [SRC-1AE03B9EC3-L002561](../../agents/web_agent.py#L2561) | 2561 | `"        for direct_url in direct_urls:"` | — |
| [SRC-1AE03B9EC3-L002562](../../agents/web_agent.py#L2562) | 2562 | `"            batches.append({"` | — |
| [SRC-1AE03B9EC3-L002563](../../agents/web_agent.py#L2563) | 2563 | `"                \"query\": (queries[0] if queries else \"\"),"` | — |
| [SRC-1AE03B9EC3-L002564](../../agents/web_agent.py#L2564) | 2564 | `"                \"provider\": \"user_supplied_url\","` | — |
| [SRC-1AE03B9EC3-L002565](../../agents/web_agent.py#L2565) | 2565 | `"                \"results\": [{"` | — |
| [SRC-1AE03B9EC3-L002566](../../agents/web_agent.py#L2566) | 2566 | `"                    \"title\": \"رابط قدمه المستخدم للتحليل\","` | — |
| [SRC-1AE03B9EC3-L002567](../../agents/web_agent.py#L2567) | 2567 | `"                    \"url\": direct_url,"` | — |
| [SRC-1AE03B9EC3-L002568](../../agents/web_agent.py#L2568) | 2568 | `"                    \"snippet\": \"\","` | — |
| [SRC-1AE03B9EC3-L002569](../../agents/web_agent.py#L2569) | 2569 | `"                    \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002570](../../agents/web_agent.py#L2570) | 2570 | `"                    \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002571](../../agents/web_agent.py#L2571) | 2571 | `"                    \"provider\": \"user_supplied_url\","` | — |
| [SRC-1AE03B9EC3-L002572](../../agents/web_agent.py#L2572) | 2572 | `"                    \"provider_rank\": 1,"` | — |
| [SRC-1AE03B9EC3-L002573](../../agents/web_agent.py#L2573) | 2573 | `"                    \"search_query\": (queries[0] if queries else \"\"),"` | — |
| [SRC-1AE03B9EC3-L002574](../../agents/web_agent.py#L2574) | 2574 | `"                    \"published_at\": \"\","` | — |
| [SRC-1AE03B9EC3-L002575](../../agents/web_agent.py#L2575) | 2575 | `"                }],"` | — |
| [SRC-1AE03B9EC3-L002576](../../agents/web_agent.py#L2576) | 2576 | `"            })"` | — |
| [SRC-1AE03B9EC3-L002577](../../agents/web_agent.py#L2577) | 2577 | `""` | — |
| [SRC-1AE03B9EC3-L002578](../../agents/web_agent.py#L2578) | 2578 | `"        raw_results_count = sum(len(batch.get(\"results\", [])) for batch in batches if isinstance(batch, dict) and isinstance(batch.get(\"results\", []), list))"` | — |
| [SRC-1AE03B9EC3-L002579](../../agents/web_agent.py#L2579) | 2579 | `"        sources = fuse_ranked_results(batches, limit=MAX_SEARCH_RESULTS)"` | — |
| [SRC-1AE03B9EC3-L002580](../../agents/web_agent.py#L2580) | 2580 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L002581](../../agents/web_agent.py#L2581) | 2581 | `"            source.setdefault(\"page_fetch_status\", \"not_attempted\")"` | — |
| [SRC-1AE03B9EC3-L002582](../../agents/web_agent.py#L2582) | 2582 | `"        # Fetch page text only for the best few public URLs; do it concurrently with strict bounds."` | — |
| [SRC-1AE03B9EC3-L002583](../../agents/web_agent.py#L2583) | 2583 | `"        fetch_targets = sources[:MAX_FETCHED_PAGES]"` | — |
| [SRC-1AE03B9EC3-L002584](../../agents/web_agent.py#L2584) | 2584 | `"        for source in fetch_targets:"` | — |
| [SRC-1AE03B9EC3-L002585](../../agents/web_agent.py#L2585) | 2585 | `"            source[\"page_fetch_status\"] = \"attempted\""` | — |
| [SRC-1AE03B9EC3-L002586](../../agents/web_agent.py#L2586) | 2586 | `"        fetched_count = 0"` | — |
| [SRC-1AE03B9EC3-L002587](../../agents/web_agent.py#L2587) | 2587 | `"        if fetch_targets:"` | — |
| [SRC-1AE03B9EC3-L002588](../../agents/web_agent.py#L2588) | 2588 | `"            with ThreadPoolExecutor(max_workers=min(4, len(fetch_targets))) as pool:"` | — |
| [SRC-1AE03B9EC3-L002589](../../agents/web_agent.py#L2589) | 2589 | `"                futures = {"` | — |
| [SRC-1AE03B9EC3-L002590](../../agents/web_agent.py#L2590) | 2590 | `"                    pool.submit(self._fetch_page, source[\"url\"]): source"` | — |
| [SRC-1AE03B9EC3-L002591](../../agents/web_agent.py#L2591) | 2591 | `"                    for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L002592](../../agents/web_agent.py#L2592) | 2592 | `"                }"` | — |
| [SRC-1AE03B9EC3-L002593](../../agents/web_agent.py#L2593) | 2593 | `"                for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002594](../../agents/web_agent.py#L2594) | 2594 | `"                    source = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002595](../../agents/web_agent.py#L2595) | 2595 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002596](../../agents/web_agent.py#L2596) | 2596 | `"                        fetch_result = future.result()"` | — |
| [SRC-1AE03B9EC3-L002597](../../agents/web_agent.py#L2597) | 2597 | `"                    except RequestBudgetExceeded as exc:"` | — |
| [SRC-1AE03B9EC3-L002598](../../agents/web_agent.py#L2598) | 2598 | `"                        source[\"page_fetch_status\"] = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L002599](../../agents/web_agent.py#L2599) | 2599 | `"                        source[\"page_fetch_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L002600](../../agents/web_agent.py#L2600) | 2600 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002601](../../agents/web_agent.py#L2601) | 2601 | `"                    except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002602](../../agents/web_agent.py#L2602) | 2602 | `"                        source[\"page_fetch_status\"] = \"fetch_failed\""` | — |
| [SRC-1AE03B9EC3-L002603](../../agents/web_agent.py#L2603) | 2603 | `"                        source[\"page_fetch_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L002604](../../agents/web_agent.py#L2604) | 2604 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002605](../../agents/web_agent.py#L2605) | 2605 | `"                    title, page_text = fetch_result"` | — |
| [SRC-1AE03B9EC3-L002606](../../agents/web_agent.py#L2606) | 2606 | `"                    observed_status = getattr(fetch_result, \"status\", None)"` | — |
| [SRC-1AE03B9EC3-L002607](../../agents/web_agent.py#L2607) | 2607 | `"                    error_class = getattr(fetch_result, \"error_class\", None)"` | — |
| [SRC-1AE03B9EC3-L002608](../../agents/web_agent.py#L2608) | 2608 | `"                    if title:"` | — |
| [SRC-1AE03B9EC3-L002609](../../agents/web_agent.py#L2609) | 2609 | `"                        source[\"title\"] = title"` | — |
| [SRC-1AE03B9EC3-L002610](../../agents/web_agent.py#L2610) | 2610 | `"                    if page_text and page_text.strip():"` | — |
| [SRC-1AE03B9EC3-L002611](../../agents/web_agent.py#L2611) | 2611 | `"                        source[\"page_text\"] = page_text"` | — |
| [SRC-1AE03B9EC3-L002612](../../agents/web_agent.py#L2612) | 2612 | `"                        source[\"snippet\"] = page_text[:1800]"` | — |
| [SRC-1AE03B9EC3-L002613](../../agents/web_agent.py#L2613) | 2613 | `"                        source[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L002614](../../agents/web_agent.py#L2614) | 2614 | `"                        source[\"page_fetch_status\"] = ("` | — |
| [SRC-1AE03B9EC3-L002615](../../agents/web_agent.py#L2615) | 2615 | `"                            observed_status"` | — |
| [SRC-1AE03B9EC3-L002616](../../agents/web_agent.py#L2616) | 2616 | `"                            if observed_status in {\"content_extracted\", \"partial_extraction\"}"` | — |
| [SRC-1AE03B9EC3-L002617](../../agents/web_agent.py#L2617) | 2617 | `"                            else \"partial_extraction\""` | — |
| [SRC-1AE03B9EC3-L002618](../../agents/web_agent.py#L2618) | 2618 | `"                            if len(page_text) >= MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L002619](../../agents/web_agent.py#L2619) | 2619 | `"                            else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L002620](../../agents/web_agent.py#L2620) | 2620 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002621](../../agents/web_agent.py#L2621) | 2621 | `"                        if error_class:"` | — |
| [SRC-1AE03B9EC3-L002622](../../agents/web_agent.py#L2622) | 2622 | `"                            source[\"page_fetch_error_class\"] = str(error_class)[:80]"` | — |
| [SRC-1AE03B9EC3-L002623](../../agents/web_agent.py#L2623) | 2623 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L002624](../../agents/web_agent.py#L2624) | 2624 | `"                            source.pop(\"page_fetch_error_class\", None)"` | — |
| [SRC-1AE03B9EC3-L002625](../../agents/web_agent.py#L2625) | 2625 | `"                        fetched_count += 1"` | — |
| [SRC-1AE03B9EC3-L002626](../../agents/web_agent.py#L2626) | 2626 | `"                        if source[\"page_fetch_status\"] == \"partial_extraction\":"` | — |
| [SRC-1AE03B9EC3-L002627](../../agents/web_agent.py#L2627) | 2627 | `"                            host = urllib.parse.urlparse(source.get(\"url\", \"\")).hostname or \"المصدر\""` | — |
| [SRC-1AE03B9EC3-L002628](../../agents/web_agent.py#L2628) | 2628 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002629](../../agents/web_agent.py#L2629) | 2629 | `"                                f\"استُخرج جزء من نص {host} فقط؛ قد تكون الصفحة أطول من الحد الآمن.\""` | — |
| [SRC-1AE03B9EC3-L002630](../../agents/web_agent.py#L2630) | 2630 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002631](../../agents/web_agent.py#L2631) | 2631 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L002632](../../agents/web_agent.py#L2632) | 2632 | `"                        source[\"page_fetched\"] = False"` | — |
| [SRC-1AE03B9EC3-L002633](../../agents/web_agent.py#L2633) | 2633 | `"                        if observed_status in {"` | — |
| [SRC-1AE03B9EC3-L002634](../../agents/web_agent.py#L2634) | 2634 | `"                            \"rejected_url\", \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L002635](../../agents/web_agent.py#L2635) | 2635 | `"                            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\", \"http_error\","` | — |
| [SRC-1AE03B9EC3-L002636](../../agents/web_agent.py#L2636) | 2636 | `"                            \"unsupported_content_type\", \"page_too_large\", \"network_error\","` | — |
| [SRC-1AE03B9EC3-L002637](../../agents/web_agent.py#L2637) | 2637 | `"                            \"empty_content\", \"no_text_extracted\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002638](../../agents/web_agent.py#L2638) | 2638 | `"                        }:"` | — |
| [SRC-1AE03B9EC3-L002639](../../agents/web_agent.py#L2639) | 2639 | `"                            source[\"page_fetch_status\"] = observed_status"` | — |
| [SRC-1AE03B9EC3-L002640](../../agents/web_agent.py#L2640) | 2640 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L002641](../../agents/web_agent.py#L2641) | 2641 | `"                            source[\"page_fetch_status\"] = \"no_text_extracted\""` | — |
| [SRC-1AE03B9EC3-L002642](../../agents/web_agent.py#L2642) | 2642 | `"                        if error_class:"` | — |
| [SRC-1AE03B9EC3-L002643](../../agents/web_agent.py#L2643) | 2643 | `"                            source[\"page_fetch_error_class\"] = str(error_class)[:80]"` | — |
| [SRC-1AE03B9EC3-L002644](../../agents/web_agent.py#L2644) | 2644 | `"                        host = urllib.parse.urlparse(source.get(\"url\", \"\")).hostname or \"المصدر\""` | — |
| [SRC-1AE03B9EC3-L002645](../../agents/web_agent.py#L2645) | 2645 | `"                        if source[\"page_fetch_status\"] in {\"no_text_extracted\", \"empty_content\"}:"` | — |
| [SRC-1AE03B9EC3-L002646](../../agents/web_agent.py#L2646) | 2646 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002647](../../agents/web_agent.py#L2647) | 2647 | `"                                f\"لم يمكن استخراج نص من {host}؛ جُلبت الصفحة أو جرت محاولة قراءتها لكن قد تكون ديناميكية أو محجوبة.\""` | — |
| [SRC-1AE03B9EC3-L002648](../../agents/web_agent.py#L2648) | 2648 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002649](../../agents/web_agent.py#L2649) | 2649 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L002650](../../agents/web_agent.py#L2650) | 2650 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002651](../../agents/web_agent.py#L2651) | 2651 | `"                                f\"تعذرت قراءة نص {host} بسبب حالة الجلب: {source['page_fetch_status']}.\""` | — |
| [SRC-1AE03B9EC3-L002652](../../agents/web_agent.py#L2652) | 2652 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002653](../../agents/web_agent.py#L2653) | 2653 | `""` | — |
| [SRC-1AE03B9EC3-L002654](../../agents/web_agent.py#L2654) | 2654 | `"        # Reorder on consensus first, and keep clear machine-readable provenance."` | — |
| [SRC-1AE03B9EC3-L002655](../../agents/web_agent.py#L2655) | 2655 | `"        sources.sort(key=lambda source: source.get(\"rank_score\", 0), reverse=True)"` | — |
| [SRC-1AE03B9EC3-L002656](../../agents/web_agent.py#L2656) | 2656 | `"        providers = sorted({"` | — |
| [SRC-1AE03B9EC3-L002657](../../agents/web_agent.py#L2657) | 2657 | `"            provider"` | — |
| [SRC-1AE03B9EC3-L002658](../../agents/web_agent.py#L2658) | 2658 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L002659](../../agents/web_agent.py#L2659) | 2659 | `"            for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L002660](../../agents/web_agent.py#L2660) | 2660 | `"        })"` | — |
| [SRC-1AE03B9EC3-L002661](../../agents/web_agent.py#L2661) | 2661 | `"        platform_counts: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L002662](../../agents/web_agent.py#L2662) | 2662 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L002663](../../agents/web_agent.py#L2663) | 2663 | `"            label = source.get(\"platform\", \"web\")"` | — |
| [SRC-1AE03B9EC3-L002664](../../agents/web_agent.py#L2664) | 2664 | `"            platform_counts[label] = platform_counts.get(label, 0) + 1"` | — |
| [SRC-1AE03B9EC3-L002665](../../agents/web_agent.py#L2665) | 2665 | `"        page_failure_statuses = {"` | — |
| [SRC-1AE03B9EC3-L002666](../../agents/web_agent.py#L2666) | 2666 | `"            \"fetch_failed\", \"no_text_extracted\", \"rejected_url\","` | — |
| [SRC-1AE03B9EC3-L002667](../../agents/web_agent.py#L2667) | 2667 | `"            \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L002668](../../agents/web_agent.py#L2668) | 2668 | `"            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\","` | — |
| [SRC-1AE03B9EC3-L002669](../../agents/web_agent.py#L2669) | 2669 | `"            \"http_error\", \"unsupported_content_type\", \"page_too_large\","` | — |
| [SRC-1AE03B9EC3-L002670](../../agents/web_agent.py#L2670) | 2670 | `"            \"network_error\", \"empty_content\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002671](../../agents/web_agent.py#L2671) | 2671 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002672](../../agents/web_agent.py#L2672) | 2672 | `"        page_status_values = ("` | — |
| [SRC-1AE03B9EC3-L002673](../../agents/web_agent.py#L2673) | 2673 | `"            \"not_attempted\", \"attempted\", \"content_extracted\", \"partial_extraction\","` | — |
| [SRC-1AE03B9EC3-L002674](../../agents/web_agent.py#L2674) | 2674 | `"            \"no_text_extracted\", \"fetch_failed\", \"rejected_url\","` | — |
| [SRC-1AE03B9EC3-L002675](../../agents/web_agent.py#L2675) | 2675 | `"            \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L002676](../../agents/web_agent.py#L2676) | 2676 | `"            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\","` | — |
| [SRC-1AE03B9EC3-L002677](../../agents/web_agent.py#L2677) | 2677 | `"            \"http_error\", \"unsupported_content_type\", \"page_too_large\","` | — |
| [SRC-1AE03B9EC3-L002678](../../agents/web_agent.py#L2678) | 2678 | `"            \"network_error\", \"empty_content\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002679](../../agents/web_agent.py#L2679) | 2679 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002680](../../agents/web_agent.py#L2680) | 2680 | `"        page_fetch_status_counts = {"` | — |
| [SRC-1AE03B9EC3-L002681](../../agents/web_agent.py#L2681) | 2681 | `"            status: sum(source.get(\"page_fetch_status\") == status for source in fetch_targets)"` | — |
| [SRC-1AE03B9EC3-L002682](../../agents/web_agent.py#L2682) | 2682 | `"            for status in page_status_values"` | — |
| [SRC-1AE03B9EC3-L002683](../../agents/web_agent.py#L2683) | 2683 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002684](../../agents/web_agent.py#L2684) | 2684 | `"        provider_diagnostics = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L002685](../../agents/web_agent.py#L2685) | 2685 | `"        provider_candidates_received = sum("` | — |
| [SRC-1AE03B9EC3-L002686](../../agents/web_agent.py#L2686) | 2686 | `"            max(0, int(row.get(\"result_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002687](../../agents/web_agent.py#L2687) | 2687 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L002688](../../agents/web_agent.py#L2688) | 2688 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002689](../../agents/web_agent.py#L2689) | 2689 | `"        provider_candidates_accepted = sum("` | — |
| [SRC-1AE03B9EC3-L002690](../../agents/web_agent.py#L2690) | 2690 | `"            max(0, int(row.get(\"accepted_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002691](../../agents/web_agent.py#L2691) | 2691 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L002692](../../agents/web_agent.py#L2692) | 2692 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002693](../../agents/web_agent.py#L2693) | 2693 | `"        provider_candidates_rejected = sum("` | — |
| [SRC-1AE03B9EC3-L002694](../../agents/web_agent.py#L2694) | 2694 | `"            max(0, int(row.get(\"rejected_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002695](../../agents/web_agent.py#L2695) | 2695 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L002696](../../agents/web_agent.py#L2696) | 2696 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002697](../../agents/web_agent.py#L2697) | 2697 | `"        report = {"` | — |
| [SRC-1AE03B9EC3-L002698](../../agents/web_agent.py#L2698) | 2698 | `"            \"raw_results\": raw_results_count,"` | — |
| [SRC-1AE03B9EC3-L002699](../../agents/web_agent.py#L2699) | 2699 | `"            \"provider_candidates_received\": provider_candidates_received,"` | — |
| [SRC-1AE03B9EC3-L002700](../../agents/web_agent.py#L2700) | 2700 | `"            \"provider_candidates_accepted\": provider_candidates_accepted,"` | — |
| [SRC-1AE03B9EC3-L002701](../../agents/web_agent.py#L2701) | 2701 | `"            \"provider_candidates_rejected\": provider_candidates_rejected,"` | — |
| [SRC-1AE03B9EC3-L002702](../../agents/web_agent.py#L2702) | 2702 | `"            \"unique_urls\": len({"` | — |
| [SRC-1AE03B9EC3-L002703](../../agents/web_agent.py#L2703) | 2703 | `"                self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L002704](../../agents/web_agent.py#L2704) | 2704 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L002705](../../agents/web_agent.py#L2705) | 2705 | `"                if self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L002706](../../agents/web_agent.py#L2706) | 2706 | `"            }),"` | — |
| [SRC-1AE03B9EC3-L002707](../../agents/web_agent.py#L2707) | 2707 | `"            \"pages_content_extracted\": fetched_count,"` | — |
| [SRC-1AE03B9EC3-L002708](../../agents/web_agent.py#L2708) | 2708 | `"            \"pages_partial_extracted\": sum("` | — |
| [SRC-1AE03B9EC3-L002709](../../agents/web_agent.py#L2709) | 2709 | `"                source.get(\"page_fetch_status\") == \"partial_extraction\""` | — |
| [SRC-1AE03B9EC3-L002710](../../agents/web_agent.py#L2710) | 2710 | `"                for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L002711](../../agents/web_agent.py#L2711) | 2711 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L002712](../../agents/web_agent.py#L2712) | 2712 | `"            \"pages_extract_failed\": sum("` | — |
| [SRC-1AE03B9EC3-L002713](../../agents/web_agent.py#L2713) | 2713 | `"                source.get(\"page_fetch_status\") in page_failure_statuses"` | — |
| [SRC-1AE03B9EC3-L002714](../../agents/web_agent.py#L2714) | 2714 | `"                for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L002715](../../agents/web_agent.py#L2715) | 2715 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L002716](../../agents/web_agent.py#L2716) | 2716 | `"            \"page_fetch_status_counts\": page_fetch_status_counts,"` | — |
| [SRC-1AE03B9EC3-L002717](../../agents/web_agent.py#L2717) | 2717 | `"            \"queries_planned\": len(queries),"` | — |
| [SRC-1AE03B9EC3-L002718](../../agents/web_agent.py#L2718) | 2718 | `"            \"queries_attempted\": search_started_queries,"` | — |
| [SRC-1AE03B9EC3-L002719](../../agents/web_agent.py#L2719) | 2719 | `"            \"query_results\": query_counts,"` | — |
| [SRC-1AE03B9EC3-L002720](../../agents/web_agent.py#L2720) | 2720 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L002721](../../agents/web_agent.py#L2721) | 2721 | `"            \"pages_fetched\": fetched_count,"` | — |
| [SRC-1AE03B9EC3-L002722](../../agents/web_agent.py#L2722) | 2722 | `"            \"providers_used\": providers,"` | — |
| [SRC-1AE03B9EC3-L002723](../../agents/web_agent.py#L2723) | 2723 | `"            \"provider_counts\": {"` | — |
| [SRC-1AE03B9EC3-L002724](../../agents/web_agent.py#L2724) | 2724 | `"                provider: sum(provider in source.get(\"providers\", []) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L002725](../../agents/web_agent.py#L2725) | 2725 | `"                for provider in providers"` | — |
| [SRC-1AE03B9EC3-L002726](../../agents/web_agent.py#L2726) | 2726 | `"            },"` | — |
| [SRC-1AE03B9EC3-L002727](../../agents/web_agent.py#L2727) | 2727 | `"            \"platform_counts\": platform_counts,"` | — |
| [SRC-1AE03B9EC3-L002728](../../agents/web_agent.py#L2728) | 2728 | `"            \"social_direct_results\": len(social_results),"` | — |
| [SRC-1AE03B9EC3-L002729](../../agents/web_agent.py#L2729) | 2729 | `"            \"expansion_queries\": expansion_queries,"` | — |
| [SRC-1AE03B9EC3-L002730](../../agents/web_agent.py#L2730) | 2730 | `"            \"evidence_signals\": evidence_signal_report(sources, plan.get(\"freshness\", \"any\")),"` | — |
| [SRC-1AE03B9EC3-L002731](../../agents/web_agent.py#L2731) | 2731 | `"            \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L002732](../../agents/web_agent.py#L2732) | 2732 | `"            \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L002733](../../agents/web_agent.py#L2733) | 2733 | `"            \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L002734](../../agents/web_agent.py#L2734) | 2734 | `"            \"provider_diagnostics\": provider_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L002735](../../agents/web_agent.py#L2735) | 2735 | `"            \"connector_summary\": self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L002736](../../agents/web_agent.py#L2736) | 2736 | `"                provider_diagnostics, sources"` | — |
| [SRC-1AE03B9EC3-L002737](../../agents/web_agent.py#L2737) | 2737 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L002738](../../agents/web_agent.py#L2738) | 2738 | `"            \"pages_fetch_attempted\": len(fetch_targets),"` | — |
| [SRC-1AE03B9EC3-L002739](../../agents/web_agent.py#L2739) | 2739 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002740](../../agents/web_agent.py#L2740) | 2740 | `"        coverage_targets = plan.get(\"coverage_targets\") or []"` | — |
| [SRC-1AE03B9EC3-L002741](../../agents/web_agent.py#L2741) | 2741 | `"        if isinstance(coverage_targets, list) and coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L002742](../../agents/web_agent.py#L2742) | 2742 | `"            safe_targets = ["` | — |
| [SRC-1AE03B9EC3-L002743](../../agents/web_agent.py#L2743) | 2743 | `"                target[:120]"` | — |
| [SRC-1AE03B9EC3-L002744](../../agents/web_agent.py#L2744) | 2744 | `"                for target in coverage_targets"` | — |
| [SRC-1AE03B9EC3-L002745](../../agents/web_agent.py#L2745) | 2745 | `"                if isinstance(target, str) and target.strip()"` | — |
| [SRC-1AE03B9EC3-L002746](../../agents/web_agent.py#L2746) | 2746 | `"            ][:8]"` | — |
| [SRC-1AE03B9EC3-L002747](../../agents/web_agent.py#L2747) | 2747 | `"            ledger = build_evidence_ledger(safe_targets, sources)"` | — |
| [SRC-1AE03B9EC3-L002748](../../agents/web_agent.py#L2748) | 2748 | `"            report[\"aspects\"] = safe_targets"` | — |
| [SRC-1AE03B9EC3-L002749](../../agents/web_agent.py#L2749) | 2749 | `"            report[\"evidence_ledger\"] = ledger"` | — |
| [SRC-1AE03B9EC3-L002750](../../agents/web_agent.py#L2750) | 2750 | `"            report[\"aspect_diagnostics_ar\"] = arabic_aspect_diagnostics(ledger)"` | — |
| [SRC-1AE03B9EC3-L002751](../../agents/web_agent.py#L2751) | 2751 | `"            report[\"aspect_evidence_gaps\"] = list(ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L002752](../../agents/web_agent.py#L2752) | 2752 | `"            report[\"aspect_coverage_lexical_ratio\"] = ledger.get(\"coverage_ratio\")"` | — |
| [SRC-1AE03B9EC3-L002753](../../agents/web_agent.py#L2753) | 2753 | `"            report[\"aspect_coverage_is_not_truth_score\"] = True"` | — |
| [SRC-1AE03B9EC3-L002754](../../agents/web_agent.py#L2754) | 2754 | `""` | — |
| [SRC-1AE03B9EC3-L002755](../../agents/web_agent.py#L2755) | 2755 | `"        return sources, list(dict.fromkeys(warnings)), report"` | — |
| [SRC-1AE03B9EC3-L002756](../../agents/web_agent.py#L2756) | 2756 | `""` | — |
| [SRC-1AE03B9EC3-L002757](../../agents/web_agent.py#L2757) | 2757 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L002758](../../agents/web_agent.py#L2758) | 2758 | `"    def _history_search_query(question: str, history: list[dict[str, str]]) -> str:"` | — |
| [SRC-1AE03B9EC3-L002759](../../agents/web_agent.py#L2759) | 2759 | `"        \"\"\"Backward-compatible wrapper for the shared follow-up resolver.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002760](../../agents/web_agent.py#L2760) | 2760 | `"        return resolve_followup_query(question, history)"` | — |
| [SRC-1AE03B9EC3-L002761](../../agents/web_agent.py#L2761) | 2761 | `""` | — |
| [SRC-1AE03B9EC3-L002762](../../agents/web_agent.py#L2762) | 2762 | `"    def _connector_status_summary(self, diagnostics: list[dict[str, Any]] \| None,"` | — |
| [SRC-1AE03B9EC3-L002763](../../agents/web_agent.py#L2763) | 2763 | `"                                  sources: list[dict[str, Any]] \| None = None) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L002764](../../agents/web_agent.py#L2764) | 2764 | `"        \"\"\"Summarize this request's connector states without exposing credentials.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002765](../../agents/web_agent.py#L2765) | 2765 | `"        optional = {"` | — |
| [SRC-1AE03B9EC3-L002766](../../agents/web_agent.py#L2766) | 2766 | `"            \"deepseek_search_api\": (\"DEEPSEEK_SEARCH_API_KEY\",), \"brave_search_api\": (\"BRAVE_SEARCH_API_KEY\",),"` | — |
| [SRC-1AE03B9EC3-L002767](../../agents/web_agent.py#L2767) | 2767 | `"            \"tavily_search_api\": (\"TAVILY_API_KEY\",), \"reddit_oauth_api\": (\"REDDIT_CLIENT_ID\", \"REDDIT_CLIENT_SECRET\"),"` | — |
| [SRC-1AE03B9EC3-L002768](../../agents/web_agent.py#L2768) | 2768 | `"            \"facebook_pages_api\": (\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"FACEBOOK_PAGE_IDS\"),"` | — |
| [SRC-1AE03B9EC3-L002769](../../agents/web_agent.py#L2769) | 2769 | `"            \"instagram_graph_api\": (\"INSTAGRAM_USER_ID\", \"INSTAGRAM_ACCESS_TOKEN\"),"` | — |
| [SRC-1AE03B9EC3-L002770](../../agents/web_agent.py#L2770) | 2770 | `"            \"x_official_api\": (\"X_BEARER_TOKEN\",), \"youtube_data_api\": (\"YOUTUBE_API_KEY\",),"` | — |
| [SRC-1AE03B9EC3-L002771](../../agents/web_agent.py#L2771) | 2771 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002772](../../agents/web_agent.py#L2772) | 2772 | `"        config: dict[str, tuple[bool, str]] = {"` | — |
| [SRC-1AE03B9EC3-L002773](../../agents/web_agent.py#L2773) | 2773 | `"            \"duckduckgo_html\": (True, \"built_in_no_api_key\"), \"bing_rss\": (True, \"built_in_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L002774](../../agents/web_agent.py#L2774) | 2774 | `"            \"google_news_rss\": (True, \"built_in_conditional_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L002775](../../agents/web_agent.py#L2775) | 2775 | `"            \"openalex\": (True, \"built_in_free_academic\"),"` | — |
| [SRC-1AE03B9EC3-L002776](../../agents/web_agent.py#L2776) | 2776 | `"            \"arxiv\": (True, \"built_in_free_academic\"),"` | — |
| [SRC-1AE03B9EC3-L002777](../../agents/web_agent.py#L2777) | 2777 | `"            \"crossref\": (True, \"built_in_free_academic\"),"` | — |
| [SRC-1AE03B9EC3-L002778](../../agents/web_agent.py#L2778) | 2778 | `"            \"reddit_public_rss\": (True, \"built_in_no_api_key\"), \"bluesky_public_search\": (True, \"built_in_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L002779](../../agents/web_agent.py#L2779) | 2779 | `"            \"openrouter_web_search\": (bool(self.openrouter_web_search_enabled),"` | — |
| [SRC-1AE03B9EC3-L002780](../../agents/web_agent.py#L2780) | 2780 | `"                \"enabled\" if self.openrouter_web_search_enabled else \"disabled\"),"` | — |
| [SRC-1AE03B9EC3-L002781](../../agents/web_agent.py#L2781) | 2781 | `"            \"user_supplied_url\": (True, \"request_driven\"),"` | — |
| [SRC-1AE03B9EC3-L002782](../../agents/web_agent.py#L2782) | 2782 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002783](../../agents/web_agent.py#L2783) | 2783 | `"        for name, keys in optional.items():"` | — |
| [SRC-1AE03B9EC3-L002784](../../agents/web_agent.py#L2784) | 2784 | `"            ready = all(bool(os.getenv(key, \"\").strip()) for key in keys)"` | — |
| [SRC-1AE03B9EC3-L002785](../../agents/web_agent.py#L2785) | 2785 | `"            config[name] = (ready, \"configured\" if ready else \"not_configured\")"` | — |
| [SRC-1AE03B9EC3-L002786](../../agents/web_agent.py#L2786) | 2786 | `"        grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002787](../../agents/web_agent.py#L2787) | 2787 | `"        for item in diagnostics or []:"` | — |
| [SRC-1AE03B9EC3-L002788](../../agents/web_agent.py#L2788) | 2788 | `"            if isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L002789](../../agents/web_agent.py#L2789) | 2789 | `"                name = _clean_text(item.get(\"provider\", \"unknown\"), 80) or \"unknown\""` | — |
| [SRC-1AE03B9EC3-L002790](../../agents/web_agent.py#L2790) | 2790 | `"                grouped.setdefault(name, []).append(item)"` | — |
| [SRC-1AE03B9EC3-L002791](../../agents/web_agent.py#L2791) | 2791 | `"        useful: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L002792](../../agents/web_agent.py#L2792) | 2792 | `"        for source in sources or []:"` | — |
| [SRC-1AE03B9EC3-L002793](../../agents/web_agent.py#L2793) | 2793 | `"            if not isinstance(source, dict):"` | — |
| [SRC-1AE03B9EC3-L002794](../../agents/web_agent.py#L2794) | 2794 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002795](../../agents/web_agent.py#L2795) | 2795 | `"            providers = source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L002796](../../agents/web_agent.py#L2796) | 2796 | `"            if isinstance(providers, str):"` | — |
| [SRC-1AE03B9EC3-L002797](../../agents/web_agent.py#L2797) | 2797 | `"                providers = [providers]"` | — |
| [SRC-1AE03B9EC3-L002798](../../agents/web_agent.py#L2798) | 2798 | `"            if not isinstance(providers, list):"` | — |
| [SRC-1AE03B9EC3-L002799](../../agents/web_agent.py#L2799) | 2799 | `"                providers = []"` | — |
| [SRC-1AE03B9EC3-L002800](../../agents/web_agent.py#L2800) | 2800 | `"            if isinstance(source.get(\"provider\"), str):"` | — |
| [SRC-1AE03B9EC3-L002801](../../agents/web_agent.py#L2801) | 2801 | `"                providers = providers + [source[\"provider\"]]"` | — |
| [SRC-1AE03B9EC3-L002802](../../agents/web_agent.py#L2802) | 2802 | `"            for name in {str(value) for value in providers if value}:"` | — |
| [SRC-1AE03B9EC3-L002803](../../agents/web_agent.py#L2803) | 2803 | `"                useful[name] = useful.get(name, 0) + 1"` | — |
| [SRC-1AE03B9EC3-L002804](../../agents/web_agent.py#L2804) | 2804 | `"        priority = {\"ok\": 0, \"no_results\": 1, \"filtered_all\": 2, \"not_attempted\": 3,"` | — |
| [SRC-1AE03B9EC3-L002805](../../agents/web_agent.py#L2805) | 2805 | `"                    \"disabled\": 4, \"not_configured\": 5, \"budget_exhausted\": 6,"` | — |
| [SRC-1AE03B9EC3-L002806](../../agents/web_agent.py#L2806) | 2806 | `"                    \"unknown\": 6, \"rate_limited\": 7, \"unauthorized\": 8, \"http_error\": 9,"` | — |
| [SRC-1AE03B9EC3-L002807](../../agents/web_agent.py#L2807) | 2807 | `"                    \"timeout\": 10, \"failed\": 11, \"error\": 11}"` | — |
| [SRC-1AE03B9EC3-L002808](../../agents/web_agent.py#L2808) | 2808 | `"        confirmed_attempt_statuses = _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES \| {"` | — |
| [SRC-1AE03B9EC3-L002809](../../agents/web_agent.py#L2809) | 2809 | `"            \"http_error\", \"unauthorized\", \"rate_limited\", \"invalid_response\""` | — |
| [SRC-1AE03B9EC3-L002810](../../agents/web_agent.py#L2810) | 2810 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002811](../../agents/web_agent.py#L2811) | 2811 | `"        uncertain_attempt_statuses = {\"timeout\", \"failed\", \"error\", \"unknown\", \"inconclusive\"}"` | — |
| [SRC-1AE03B9EC3-L002812](../../agents/web_agent.py#L2812) | 2812 | `""` | — |
| [SRC-1AE03B9EC3-L002813](../../agents/web_agent.py#L2813) | 2813 | `"        def redact(value: Any) -> str:"` | — |
| [SRC-1AE03B9EC3-L002814](../../agents/web_agent.py#L2814) | 2814 | `"            safe = _clean_text(str(value or \"\"), 180)"` | — |
| [SRC-1AE03B9EC3-L002815](../../agents/web_agent.py#L2815) | 2815 | `"            safe = re.sub(r\"(?i)(bearer\\s+)[A-Za-z0-9._~+/-]+=*\", r\"\\1[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L002816](../../agents/web_agent.py#L2816) | 2816 | `"            safe = re.sub(r\"(?i)\\b(api[_-]?key\|access[_-]?token\|refresh[_-]?token\|token\|secret\|password)\\s*[:=]\\s*[^\\s,;]+\", r\"\\1=[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L002817](../../agents/web_agent.py#L2817) | 2817 | `"            safe = re.sub(r\"(?i)([?&](?:api[_-]?key\|access[_-]?token\|token\|key)=)[^&\\s]+\", r\"\\1[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L002818](../../agents/web_agent.py#L2818) | 2818 | `"            return safe[:180]"` | — |
| [SRC-1AE03B9EC3-L002819](../../agents/web_agent.py#L2819) | 2819 | `""` | — |
| [SRC-1AE03B9EC3-L002820](../../agents/web_agent.py#L2820) | 2820 | `"        names = set(config) \| set(grouped) \| set(useful)"` | — |
| [SRC-1AE03B9EC3-L002821](../../agents/web_agent.py#L2821) | 2821 | `"        connectors = []"` | — |
| [SRC-1AE03B9EC3-L002822](../../agents/web_agent.py#L2822) | 2822 | `"        for name in sorted(names):"` | — |
| [SRC-1AE03B9EC3-L002823](../../agents/web_agent.py#L2823) | 2823 | `"            ready, config_status = config.get(name, (bool(grouped.get(name) or useful.get(name)), \"observed_in_code_path\"))"` | — |
| [SRC-1AE03B9EC3-L002824](../../agents/web_agent.py#L2824) | 2824 | `"            attempts = grouped.get(name, [])"` | — |
| [SRC-1AE03B9EC3-L002825](../../agents/web_agent.py#L2825) | 2825 | `"            statuses = [_clean_text(row.get(\"status\", \"unknown\"), 40).lower() or \"unknown\" for row in attempts]"` | — |
| [SRC-1AE03B9EC3-L002826](../../agents/web_agent.py#L2826) | 2826 | `"            status = max(statuses, key=lambda value: priority.get(value, 6)) if statuses else ("` | — |
| [SRC-1AE03B9EC3-L002827](../../agents/web_agent.py#L2827) | 2827 | `"                \"ok\" if useful.get(name, 0) else \"not_configured\" if not ready else \"not_attempted\")"` | — |
| [SRC-1AE03B9EC3-L002828](../../agents/web_agent.py#L2828) | 2828 | `"            if any(value in confirmed_attempt_statuses for value in statuses) or useful.get(name, 0):"` | — |
| [SRC-1AE03B9EC3-L002829](../../agents/web_agent.py#L2829) | 2829 | `"                attempted: bool \| None = True"` | — |
| [SRC-1AE03B9EC3-L002830](../../agents/web_agent.py#L2830) | 2830 | `"            elif any(value in uncertain_attempt_statuses for value in statuses):"` | — |
| [SRC-1AE03B9EC3-L002831](../../agents/web_agent.py#L2831) | 2831 | `"                attempted = None"` | — |
| [SRC-1AE03B9EC3-L002832](../../agents/web_agent.py#L2832) | 2832 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002833](../../agents/web_agent.py#L2833) | 2833 | `"                attempted = False"` | — |
| [SRC-1AE03B9EC3-L002834](../../agents/web_agent.py#L2834) | 2834 | `"            successful_statuses = set(statuses) & _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L002835](../../agents/web_agent.py#L2835) | 2835 | `"            error_response_statuses = set(statuses) & {\"http_error\", \"unauthorized\", \"rate_limited\"}"` | — |
| [SRC-1AE03B9EC3-L002836](../../agents/web_agent.py#L2836) | 2836 | `"            uncertain_failure_statuses = set(statuses) & {\"timeout\", \"failed\", \"error\", \"unknown\", \"inconclusive\"}"` | — |
| [SRC-1AE03B9EC3-L002837](../../agents/web_agent.py#L2837) | 2837 | `"            failure_observed = bool(error_response_statuses or uncertain_failure_statuses or \"budget_exhausted\" in statuses)"` | — |
| [SRC-1AE03B9EC3-L002838](../../agents/web_agent.py#L2838) | 2838 | `"            available: bool \| None = ("` | — |
| [SRC-1AE03B9EC3-L002839](../../agents/web_agent.py#L2839) | 2839 | `"                True if successful_statuses or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L002840](../../agents/web_agent.py#L2840) | 2840 | `"                else False if error_response_statuses or not ready or \"disabled\" in statuses or \"budget_exhausted\" in statuses"` | — |
| [SRC-1AE03B9EC3-L002841](../../agents/web_agent.py#L2841) | 2841 | `"                else None"` | — |
| [SRC-1AE03B9EC3-L002842](../../agents/web_agent.py#L2842) | 2842 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002843](../../agents/web_agent.py#L2843) | 2843 | `"            verified: bool \| None = ("` | — |
| [SRC-1AE03B9EC3-L002844](../../agents/web_agent.py#L2844) | 2844 | `"                True if successful_statuses or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L002845](../../agents/web_agent.py#L2845) | 2845 | `"                else False if error_response_statuses"` | — |
| [SRC-1AE03B9EC3-L002846](../../agents/web_agent.py#L2846) | 2846 | `"                else None"` | — |
| [SRC-1AE03B9EC3-L002847](../../agents/web_agent.py#L2847) | 2847 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002848](../../agents/web_agent.py#L2848) | 2848 | `"            implementation_status = ("` | — |
| [SRC-1AE03B9EC3-L002849](../../agents/web_agent.py#L2849) | 2849 | `"                \"implemented_in_code\" if name in config"` | — |
| [SRC-1AE03B9EC3-L002850](../../agents/web_agent.py#L2850) | 2850 | `"                else \"observed_runtime_path\" if attempts or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L002851](../../agents/web_agent.py#L2851) | 2851 | `"                else \"unknown\""` | — |
| [SRC-1AE03B9EC3-L002852](../../agents/web_agent.py#L2852) | 2852 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002853](../../agents/web_agent.py#L2853) | 2853 | `"            queries = list(dict.fromkeys(_clean_text(row.get(\"query\", \"\"), 180) for row in attempts if row.get(\"query\")))[:3]"` | — |
| [SRC-1AE03B9EC3-L002854](../../agents/web_agent.py#L2854) | 2854 | `"            errors = list(dict.fromkeys(redact(row.get(\"error\")) for row in attempts if row.get(\"error\")))[:3]"` | — |
| [SRC-1AE03B9EC3-L002855](../../agents/web_agent.py#L2855) | 2855 | `"            result_count = sum(max(0, int(row.get(\"result_count\", 0) or 0)) for row in attempts)"` | — |
| [SRC-1AE03B9EC3-L002856](../../agents/web_agent.py#L2856) | 2856 | `"            accepted_count = sum("` | — |
| [SRC-1AE03B9EC3-L002857](../../agents/web_agent.py#L2857) | 2857 | `"                max(0, int(row.get(\"accepted_count\", row.get(\"result_count\", 0)) or 0))"` | — |
| [SRC-1AE03B9EC3-L002858](../../agents/web_agent.py#L2858) | 2858 | `"                for row in attempts"` | — |
| [SRC-1AE03B9EC3-L002859](../../agents/web_agent.py#L2859) | 2859 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002860](../../agents/web_agent.py#L2860) | 2860 | `"            rejected_count = sum(max(0, int(row.get(\"rejected_count\", 0) or 0)) for row in attempts)"` | — |
| [SRC-1AE03B9EC3-L002861](../../agents/web_agent.py#L2861) | 2861 | `"            rejection_count_totals = {reason: 0 for reason in _PROVIDER_REJECTION_REASONS}"` | — |
| [SRC-1AE03B9EC3-L002862](../../agents/web_agent.py#L2862) | 2862 | `"            rejection_counts_seen = False"` | — |
| [SRC-1AE03B9EC3-L002863](../../agents/web_agent.py#L2863) | 2863 | `"            rejection_counts_complete = True"` | — |
| [SRC-1AE03B9EC3-L002864](../../agents/web_agent.py#L2864) | 2864 | `"            for row in attempts:"` | — |
| [SRC-1AE03B9EC3-L002865](../../agents/web_agent.py#L2865) | 2865 | `"                row_counts = row.get(\"rejection_counts\")"` | — |
| [SRC-1AE03B9EC3-L002866](../../agents/web_agent.py#L2866) | 2866 | `"                if not isinstance(row_counts, dict):"` | — |
| [SRC-1AE03B9EC3-L002867](../../agents/web_agent.py#L2867) | 2867 | `"                    # Legacy/incomplete records with actual rejections prevent claiming"` | — |
| [SRC-1AE03B9EC3-L002868](../../agents/web_agent.py#L2868) | 2868 | `"                    # that an aggregate breakdown covers every rejected candidate."` | — |
| [SRC-1AE03B9EC3-L002869](../../agents/web_agent.py#L2869) | 2869 | `"                    if max(0, int(row.get(\"rejected_count\", 0) or 0)) > 0:"` | — |
| [SRC-1AE03B9EC3-L002870](../../agents/web_agent.py#L2870) | 2870 | `"                        rejection_counts_complete = False"` | — |
| [SRC-1AE03B9EC3-L002871](../../agents/web_agent.py#L2871) | 2871 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002872](../../agents/web_agent.py#L2872) | 2872 | `"                rejection_counts_seen = True"` | — |
| [SRC-1AE03B9EC3-L002873](../../agents/web_agent.py#L2873) | 2873 | `"                for reason in _PROVIDER_REJECTION_REASONS:"` | — |
| [SRC-1AE03B9EC3-L002874](../../agents/web_agent.py#L2874) | 2874 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002875](../../agents/web_agent.py#L2875) | 2875 | `"                        rejection_count_totals[reason] += max(0, int(row_counts.get(reason, 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002876](../../agents/web_agent.py#L2876) | 2876 | `"                    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L002877](../../agents/web_agent.py#L2877) | 2877 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002878](../../agents/web_agent.py#L2878) | 2878 | `"            rejection_counts_observed = ("` | — |
| [SRC-1AE03B9EC3-L002879](../../agents/web_agent.py#L2879) | 2879 | `"                rejection_counts_seen"` | — |
| [SRC-1AE03B9EC3-L002880](../../agents/web_agent.py#L2880) | 2880 | `"                and rejection_counts_complete"` | — |
| [SRC-1AE03B9EC3-L002881](../../agents/web_agent.py#L2881) | 2881 | `"                and sum(rejection_count_totals.values()) == rejected_count"` | — |
| [SRC-1AE03B9EC3-L002882](../../agents/web_agent.py#L2882) | 2882 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002883](../../agents/web_agent.py#L2883) | 2883 | `"            candidate_rejection_observed = \"filtered_all\" in statuses or rejected_count > 0"` | — |
| [SRC-1AE03B9EC3-L002884](../../agents/web_agent.py#L2884) | 2884 | `"            connectors.append({"` | — |
| [SRC-1AE03B9EC3-L002885](../../agents/web_agent.py#L2885) | 2885 | `"                \"name\": name, \"in_codebase\": name in config or bool(attempts),"` | — |
| [SRC-1AE03B9EC3-L002886](../../agents/web_agent.py#L2886) | 2886 | `"                \"implementation_status\": implementation_status,"` | — |
| [SRC-1AE03B9EC3-L002887](../../agents/web_agent.py#L2887) | 2887 | `"                \"configured\": bool(ready), \"configuration_status\": config_status,"` | — |
| [SRC-1AE03B9EC3-L002888](../../agents/web_agent.py#L2888) | 2888 | `"                \"attempted\": attempted, \"available_for_this_request\": available,"` | — |
| [SRC-1AE03B9EC3-L002889](../../agents/web_agent.py#L2889) | 2889 | `"                \"verified_for_this_request\": verified, \"failure_observed\": failure_observed,"` | — |
| [SRC-1AE03B9EC3-L002890](../../agents/web_agent.py#L2890) | 2890 | `"                \"candidate_rejection_observed\": candidate_rejection_observed,"` | — |
| [SRC-1AE03B9EC3-L002891](../../agents/web_agent.py#L2891) | 2891 | `"                \"status\": status, \"observed_statuses\": list(dict.fromkeys(statuses))[:6],"` | — |
| [SRC-1AE03B9EC3-L002892](../../agents/web_agent.py#L2892) | 2892 | `"                \"result_count\": result_count, \"accepted_count\": accepted_count,"` | — |
| [SRC-1AE03B9EC3-L002893](../../agents/web_agent.py#L2893) | 2893 | `"                \"useful_result_count\": useful.get(name, 0),"` | — |
| [SRC-1AE03B9EC3-L002894](../../agents/web_agent.py#L2894) | 2894 | `"                \"rejected_count\": rejected_count,"` | — |
| [SRC-1AE03B9EC3-L002895](../../agents/web_agent.py#L2895) | 2895 | `"                \"rejection_counts_observed\": rejection_counts_observed,"` | — |
| [SRC-1AE03B9EC3-L002896](../../agents/web_agent.py#L2896) | 2896 | `"                \"rejection_counts\": rejection_count_totals if rejection_counts_observed else None,"` | — |
| [SRC-1AE03B9EC3-L002897](../../agents/web_agent.py#L2897) | 2897 | `"                \"queries\": queries, \"errors\": errors,"` | — |
| [SRC-1AE03B9EC3-L002898](../../agents/web_agent.py#L2898) | 2898 | `"            })"` | — |
| [SRC-1AE03B9EC3-L002899](../../agents/web_agent.py#L2899) | 2899 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L002900](../../agents/web_agent.py#L2900) | 2900 | `"            \"scope\": \"this_request_only\","` | — |
| [SRC-1AE03B9EC3-L002901](../../agents/web_agent.py#L2901) | 2901 | `"            \"semantics\": \"result_count is connector-reported rows; useful_result_count counts final fused source records attributed to a connector; neither proves factual accuracy or editorial independence.\","` | — |
| [SRC-1AE03B9EC3-L002902](../../agents/web_agent.py#L2902) | 2902 | `"            \"attempted_count\": sum(bool(item[\"attempted\"]) for item in connectors),"` | — |
| [SRC-1AE03B9EC3-L002903](../../agents/web_agent.py#L2903) | 2903 | `"            \"failed_count\": sum(item[\"status\"] in {\"failed\", \"error\", \"timeout\", \"http_error\", \"unauthorized\", \"rate_limited\"} for item in connectors),"` | — |
| [SRC-1AE03B9EC3-L002904](../../agents/web_agent.py#L2904) | 2904 | `"            \"connectors\": connectors[:24],"` | — |
| [SRC-1AE03B9EC3-L002905](../../agents/web_agent.py#L2905) | 2905 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002906](../../agents/web_agent.py#L2906) | 2906 | `""` | — |
| [SRC-1AE03B9EC3-L002907](../../agents/web_agent.py#L2907) | 2907 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L002908](../../agents/web_agent.py#L2908) | 2908 | `"    def _sanitize_history(history: Any) -> list[dict[str, str]]:"` | — |
| [SRC-1AE03B9EC3-L002909](../../agents/web_agent.py#L2909) | 2909 | `"        if not isinstance(history, list):"` | — |
| [SRC-1AE03B9EC3-L002910](../../agents/web_agent.py#L2910) | 2910 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L002911](../../agents/web_agent.py#L2911) | 2911 | `"        result: list[dict[str, str]] = []"` | — |
| [SRC-1AE03B9EC3-L002912](../../agents/web_agent.py#L2912) | 2912 | `"        for item in history[-MAX_HISTORY_ITEMS:]:"` | — |
| [SRC-1AE03B9EC3-L002913](../../agents/web_agent.py#L2913) | 2913 | `"            if not isinstance(item, dict) or item.get(\"role\") not in {\"user\", \"assistant\"}:"` | — |
| [SRC-1AE03B9EC3-L002914](../../agents/web_agent.py#L2914) | 2914 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002915](../../agents/web_agent.py#L2915) | 2915 | `"            text = _clean_text(item.get(\"content\"), MAX_HISTORY_CHARS)"` | — |
| [SRC-1AE03B9EC3-L002916](../../agents/web_agent.py#L2916) | 2916 | `"            if text:"` | — |
| [SRC-1AE03B9EC3-L002917](../../agents/web_agent.py#L2917) | 2917 | `"                result.append({\"role\": item[\"role\"], \"content\": text})"` | — |
| [SRC-1AE03B9EC3-L002918](../../agents/web_agent.py#L2918) | 2918 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L002919](../../agents/web_agent.py#L2919) | 2919 | `""` | — |
| [SRC-1AE03B9EC3-L002920](../../agents/web_agent.py#L2920) | 2920 | `"    def _record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L002921](../../agents/web_agent.py#L2921) | 2921 | `"        self,"` | — |
| [SRC-1AE03B9EC3-L002922](../../agents/web_agent.py#L2922) | 2922 | `"        requested_model: str,"` | — |
| [SRC-1AE03B9EC3-L002923](../../agents/web_agent.py#L2923) | 2923 | `"        attempted_model: str,"` | — |
| [SRC-1AE03B9EC3-L002924](../../agents/web_agent.py#L2924) | 2924 | `"        status: str,"` | — |
| [SRC-1AE03B9EC3-L002925](../../agents/web_agent.py#L2925) | 2925 | `"        finish_reason: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002926](../../agents/web_agent.py#L2926) | 2926 | `"        error_class: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002927](../../agents/web_agent.py#L2927) | 2927 | `"        request_started: bool = True,"` | — |
| [SRC-1AE03B9EC3-L002928](../../agents/web_agent.py#L2928) | 2928 | `"        remote_response_received: bool \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002929](../../agents/web_agent.py#L2929) | 2929 | `"    ) -> None:"` | — |
| [SRC-1AE03B9EC3-L002930](../../agents/web_agent.py#L2930) | 2930 | `"        \"\"\"Store bounded metadata for each model attempt; never retain prompts or output.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002931](../../agents/web_agent.py#L2931) | 2931 | `"        self._generation_attempt_sequence = getattr(self, \"_generation_attempt_sequence\", 0) + 1"` | — |
| [SRC-1AE03B9EC3-L002932](../../agents/web_agent.py#L2932) | 2932 | `"        record: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L002933](../../agents/web_agent.py#L2933) | 2933 | `"            \"attempt_number\": self._generation_attempt_sequence,"` | — |
| [SRC-1AE03B9EC3-L002934](../../agents/web_agent.py#L2934) | 2934 | `"            \"requested_model\": str(requested_model)[:160],"` | — |
| [SRC-1AE03B9EC3-L002935](../../agents/web_agent.py#L2935) | 2935 | `"            \"attempted_model\": str(attempted_model)[:160],"` | — |
| [SRC-1AE03B9EC3-L002936](../../agents/web_agent.py#L2936) | 2936 | `"            \"fallback_used\": str(attempted_model) != str(requested_model),"` | — |
| [SRC-1AE03B9EC3-L002937](../../agents/web_agent.py#L2937) | 2937 | `"            \"request_started\": bool(request_started),"` | — |
| [SRC-1AE03B9EC3-L002938](../../agents/web_agent.py#L2938) | 2938 | `"            \"status\": str(status)[:48],"` | — |
| [SRC-1AE03B9EC3-L002939](../../agents/web_agent.py#L2939) | 2939 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002940](../../agents/web_agent.py#L2940) | 2940 | `"        if remote_response_received is None and isinstance(finish_reason, str) and finish_reason.strip():"` | — |
| [SRC-1AE03B9EC3-L002941](../../agents/web_agent.py#L2941) | 2941 | `"            # A concrete finish_reason can only be observed after a provider response was received."` | — |
| [SRC-1AE03B9EC3-L002942](../../agents/web_agent.py#L2942) | 2942 | `"            remote_response_received = True"` | — |
| [SRC-1AE03B9EC3-L002943](../../agents/web_agent.py#L2943) | 2943 | `"        if remote_response_received is not None:"` | — |
| [SRC-1AE03B9EC3-L002944](../../agents/web_agent.py#L2944) | 2944 | `"            record[\"remote_response_received\"] = bool(remote_response_received)"` | — |
| [SRC-1AE03B9EC3-L002945](../../agents/web_agent.py#L2945) | 2945 | `"        if isinstance(finish_reason, str) and finish_reason.strip():"` | — |
| [SRC-1AE03B9EC3-L002946](../../agents/web_agent.py#L2946) | 2946 | `"            record[\"finish_reason\"] = finish_reason.strip()[:48]"` | — |
| [SRC-1AE03B9EC3-L002947](../../agents/web_agent.py#L2947) | 2947 | `"        if isinstance(error_class, str) and error_class:"` | — |
| [SRC-1AE03B9EC3-L002948](../../agents/web_agent.py#L2948) | 2948 | `"            record[\"error_class\"] = error_class[:80]"` | — |
| [SRC-1AE03B9EC3-L002949](../../agents/web_agent.py#L2949) | 2949 | `"        self.generation_diagnostics.append(record)"` | — |
| [SRC-1AE03B9EC3-L002950](../../agents/web_agent.py#L2950) | 2950 | `"        self.generation_diagnostics = self.generation_diagnostics[-12:]"` | — |
| [SRC-1AE03B9EC3-L002951](../../agents/web_agent.py#L2951) | 2951 | `""` | — |
| [SRC-1AE03B9EC3-L002952](../../agents/web_agent.py#L2952) | 2952 | `"    def _request_completion("` | — |
| [SRC-1AE03B9EC3-L002953](../../agents/web_agent.py#L2953) | 2953 | `"        self,"` | — |
| [SRC-1AE03B9EC3-L002954](../../agents/web_agent.py#L2954) | 2954 | `"        messages: list[dict[str, str]],"` | — |
| [SRC-1AE03B9EC3-L002955](../../agents/web_agent.py#L2955) | 2955 | `"        max_tokens: int = 1400,"` | — |
| [SRC-1AE03B9EC3-L002956](../../agents/web_agent.py#L2956) | 2956 | `"        temperature: float = 0.2,"` | — |
| [SRC-1AE03B9EC3-L002957](../../agents/web_agent.py#L2957) | 2957 | `"        timeout: int \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002958](../../agents/web_agent.py#L2958) | 2958 | `"        model: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002959](../../agents/web_agent.py#L2959) | 2959 | `"        enable_web_search: bool = False,"` | — |
| [SRC-1AE03B9EC3-L002960](../../agents/web_agent.py#L2960) | 2960 | `"    ) -> str:"` | — |
| [SRC-1AE03B9EC3-L002961](../../agents/web_agent.py#L2961) | 2961 | `"        \"\"\"Call an OpenAI-compatible API with bounded fallback and optional live server search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002962](../../agents/web_agent.py#L2962) | 2962 | `"        requested_model = (model or self.answer_model).strip()"` | — |
| [SRC-1AE03B9EC3-L002963](../../agents/web_agent.py#L2963) | 2963 | `"        if not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L002964](../../agents/web_agent.py#L2964) | 2964 | `"            self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L002965](../../agents/web_agent.py#L2965) | 2965 | `"                requested_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L002966](../../agents/web_agent.py#L2966) | 2966 | `"                attempted_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L002967](../../agents/web_agent.py#L2967) | 2967 | `"                status=\"not_configured\","` | — |
| [SRC-1AE03B9EC3-L002968](../../agents/web_agent.py#L2968) | 2968 | `"                error_class=\"MissingAPIKey\","` | — |
| [SRC-1AE03B9EC3-L002969](../../agents/web_agent.py#L2969) | 2969 | `"                request_started=False,"` | — |
| [SRC-1AE03B9EC3-L002970](../../agents/web_agent.py#L2970) | 2970 | `"                remote_response_received=False,"` | — |
| [SRC-1AE03B9EC3-L002971](../../agents/web_agent.py#L2971) | 2971 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002972](../../agents/web_agent.py#L2972) | 2972 | `"            raise RuntimeError(\"لم يتم ضبط مفتاح نموذج اللغة.\")"` | — |
| [SRC-1AE03B9EC3-L002973](../../agents/web_agent.py#L2973) | 2973 | `""` | — |
| [SRC-1AE03B9EC3-L002974](../../agents/web_agent.py#L2974) | 2974 | `"        model_candidates = [requested_model]"` | — |
| [SRC-1AE03B9EC3-L002975](../../agents/web_agent.py#L2975) | 2975 | `"        if self.fallback_model and self.fallback_model not in model_candidates:"` | — |
| [SRC-1AE03B9EC3-L002976](../../agents/web_agent.py#L2976) | 2976 | `"            model_candidates.append(self.fallback_model)"` | — |
| [SRC-1AE03B9EC3-L002977](../../agents/web_agent.py#L2977) | 2977 | `""` | — |
| [SRC-1AE03B9EC3-L002978](../../agents/web_agent.py#L2978) | 2978 | `"        last_error: RuntimeError \| None = None"` | — |
| [SRC-1AE03B9EC3-L002979](../../agents/web_agent.py#L2979) | 2979 | `"        for candidate_model in model_candidates:"` | — |
| [SRC-1AE03B9EC3-L002980](../../agents/web_agent.py#L2980) | 2980 | `"            budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L002981](../../agents/web_agent.py#L2981) | 2981 | `"            use_web_search = enable_web_search and self.openrouter_web_search_enabled"` | — |
| [SRC-1AE03B9EC3-L002982](../../agents/web_agent.py#L2982) | 2982 | `"            if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L002983](../../agents/web_agent.py#L2983) | 2983 | `"                try:"` | — |
| [SRC-1AE03B9EC3-L002984](../../agents/web_agent.py#L2984) | 2984 | `"                    budget.reserve(\"model_calls\")"` | — |
| [SRC-1AE03B9EC3-L002985](../../agents/web_agent.py#L2985) | 2985 | `"                    request_timeout = budget.timeout_for(timeout or self.timeout)"` | — |
| [SRC-1AE03B9EC3-L002986](../../agents/web_agent.py#L2986) | 2986 | `"                    if use_web_search and budget.remaining_units(\"tool_calls\") < 3:"` | — |
| [SRC-1AE03B9EC3-L002987](../../agents/web_agent.py#L2987) | 2987 | `"                        # The model may still answer, but the optional server-side search"` | — |
| [SRC-1AE03B9EC3-L002988](../../agents/web_agent.py#L2988) | 2988 | `"                        # tool is disabled when its separate budget is unavailable."` | — |
| [SRC-1AE03B9EC3-L002989](../../agents/web_agent.py#L2989) | 2989 | `"                        use_web_search = False"` | — |
| [SRC-1AE03B9EC3-L002990](../../agents/web_agent.py#L2990) | 2990 | `"                    elif use_web_search:"` | — |
| [SRC-1AE03B9EC3-L002991](../../agents/web_agent.py#L2991) | 2991 | `"                        # Reserve the maximum server-side tool calls offered by this request."` | — |
| [SRC-1AE03B9EC3-L002992](../../agents/web_agent.py#L2992) | 2992 | `"                        budget.reserve(\"tool_calls\", amount=3)"` | — |
| [SRC-1AE03B9EC3-L002993](../../agents/web_agent.py#L2993) | 2993 | `"                except RequestBudgetExceeded as exc:"` | — |
| [SRC-1AE03B9EC3-L002994](../../agents/web_agent.py#L2994) | 2994 | `"                    self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L002995](../../agents/web_agent.py#L2995) | 2995 | `"                        requested_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L002996](../../agents/web_agent.py#L2996) | 2996 | `"                        attempted_model=candidate_model,"` | — |
| [SRC-1AE03B9EC3-L002997](../../agents/web_agent.py#L2997) | 2997 | `"                        status=\"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002998](../../agents/web_agent.py#L2998) | 2998 | `"                        error_class=type(exc).__name__,"` | — |
| [SRC-1AE03B9EC3-L002999](../../agents/web_agent.py#L2999) | 2999 | `"                        request_started=False,"` | — |
| [SRC-1AE03B9EC3-L003000](../../agents/web_agent.py#L3000) | 3000 | `"                        remote_response_received=False,"` | — |
| [SRC-1AE03B9EC3-L003001](../../agents/web_agent.py#L3001) | 3001 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003002](../../agents/web_agent.py#L3002) | 3002 | `"                    raise"` | — |
| [SRC-1AE03B9EC3-L003003](../../agents/web_agent.py#L3003) | 3003 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L003004](../../agents/web_agent.py#L3004) | 3004 | `"                request_timeout = timeout or self.timeout"` | — |
| [SRC-1AE03B9EC3-L003005](../../agents/web_agent.py#L3005) | 3005 | `"            request_payload: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L003006](../../agents/web_agent.py#L3006) | 3006 | `"                \"model\": candidate_model,"` | — |
| [SRC-1AE03B9EC3-L003007](../../agents/web_agent.py#L3007) | 3007 | `"                \"messages\": messages,"` | — |
| [SRC-1AE03B9EC3-L003008](../../agents/web_agent.py#L3008) | 3008 | `"                \"temperature\": temperature,"` | — |
| [SRC-1AE03B9EC3-L003009](../../agents/web_agent.py#L3009) | 3009 | `"                \"max_tokens\": max(100, min(int(max_tokens), 3000)),"` | — |
| [SRC-1AE03B9EC3-L003010](../../agents/web_agent.py#L3010) | 3010 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003011](../../agents/web_agent.py#L3011) | 3011 | `"            if use_web_search:"` | — |
| [SRC-1AE03B9EC3-L003012](../../agents/web_agent.py#L3012) | 3012 | `"                # OpenRouter executes these searches server-side and returns URL citations."` | — |
| [SRC-1AE03B9EC3-L003013](../../agents/web_agent.py#L3013) | 3013 | `"                # This is opt-in because provider search incurs usage charges."` | — |
| [SRC-1AE03B9EC3-L003014](../../agents/web_agent.py#L3014) | 3014 | `"                request_payload[\"tools\"] = [{"` | — |
| [SRC-1AE03B9EC3-L003015](../../agents/web_agent.py#L3015) | 3015 | `"                    \"type\": \"openrouter:web_search\","` | — |
| [SRC-1AE03B9EC3-L003016](../../agents/web_agent.py#L3016) | 3016 | `"                    \"parameters\": {"` | — |
| [SRC-1AE03B9EC3-L003017](../../agents/web_agent.py#L3017) | 3017 | `"                        \"engine\": \"auto\","` | — |
| [SRC-1AE03B9EC3-L003018](../../agents/web_agent.py#L3018) | 3018 | `"                        \"max_results\": 5,"` | — |
| [SRC-1AE03B9EC3-L003019](../../agents/web_agent.py#L3019) | 3019 | `"                        \"max_total_results\": 12,"` | — |
| [SRC-1AE03B9EC3-L003020](../../agents/web_agent.py#L3020) | 3020 | `"                        \"max_uses\": 3,"` | — |
| [SRC-1AE03B9EC3-L003021](../../agents/web_agent.py#L3021) | 3021 | `"                        \"search_context_size\": \"medium\","` | — |
| [SRC-1AE03B9EC3-L003022](../../agents/web_agent.py#L3022) | 3022 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L003023](../../agents/web_agent.py#L3023) | 3023 | `"                }]"` | — |
| [SRC-1AE03B9EC3-L003024](../../agents/web_agent.py#L3024) | 3024 | `"                request_payload[\"max_tool_calls\"] = 5"` | — |
| [SRC-1AE03B9EC3-L003025](../../agents/web_agent.py#L3025) | 3025 | `"            payload = json.dumps(request_payload, ensure_ascii=False).encode(\"utf-8\")"` | — |
| [SRC-1AE03B9EC3-L003026](../../agents/web_agent.py#L3026) | 3026 | `"            request = urllib.request.Request("` | — |
| [SRC-1AE03B9EC3-L003027](../../agents/web_agent.py#L3027) | 3027 | `"                self.base_url + \"/chat/completions\","` | — |
| [SRC-1AE03B9EC3-L003028](../../agents/web_agent.py#L3028) | 3028 | `"                data=payload,"` | — |
| [SRC-1AE03B9EC3-L003029](../../agents/web_agent.py#L3029) | 3029 | `"                headers={"` | — |
| [SRC-1AE03B9EC3-L003030](../../agents/web_agent.py#L3030) | 3030 | `"                    \"Authorization\": \"Bearer \" + self.api_key,"` | — |
| [SRC-1AE03B9EC3-L003031](../../agents/web_agent.py#L3031) | 3031 | `"                    \"Content-Type\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L003032](../../agents/web_agent.py#L3032) | 3032 | `"                    \"HTTP-Referer\": \"https://github.com/mosabosama2030-oss/omarai\","` | — |
| [SRC-1AE03B9EC3-L003033](../../agents/web_agent.py#L3033) | 3033 | `"                    \"X-Title\": \"Omarai Web Agent\","` | — |
| [SRC-1AE03B9EC3-L003034](../../agents/web_agent.py#L3034) | 3034 | `"                },"` | — |
| [SRC-1AE03B9EC3-L003035](../../agents/web_agent.py#L3035) | 3035 | `"                method=\"POST\","` | — |
| [SRC-1AE03B9EC3-L003036](../../agents/web_agent.py#L3036) | 3036 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003037](../../agents/web_agent.py#L3037) | 3037 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L003038](../../agents/web_agent.py#L3038) | 3038 | `"                with urllib.request.urlopen(request, timeout=request_timeout) as response:"` | — |
| [SRC-1AE03B9EC3-L003039](../../agents/web_agent.py#L3039) | 3039 | `"                    data = json.loads(response.read(2_000_000).decode(\"utf-8\"))"` | — |
| [SRC-1AE03B9EC3-L003040](../../agents/web_agent.py#L3040) | 3040 | `"                choice = data[\"choices\"][0]"` | — |
| [SRC-1AE03B9EC3-L003041](../../agents/web_agent.py#L3041) | 3041 | `"                if not isinstance(choice, dict):"` | — |
| [SRC-1AE03B9EC3-L003042](../../agents/web_agent.py#L3042) | 3042 | `"                    raise TypeError(\"invalid completion choice\")"` | — |
| [SRC-1AE03B9EC3-L003043](../../agents/web_agent.py#L3043) | 3043 | `"                finish_reason = choice.get(\"finish_reason\")"` | — |
| [SRC-1AE03B9EC3-L003044](../../agents/web_agent.py#L3044) | 3044 | `"                normalized_finish_reason = ("` | — |
| [SRC-1AE03B9EC3-L003045](../../agents/web_agent.py#L3045) | 3045 | `"                    finish_reason.strip().lower()"` | — |
| [SRC-1AE03B9EC3-L003046](../../agents/web_agent.py#L3046) | 3046 | `"                    if isinstance(finish_reason, str)"` | — |
| [SRC-1AE03B9EC3-L003047](../../agents/web_agent.py#L3047) | 3047 | `"                    else \"\""` | — |
| [SRC-1AE03B9EC3-L003048](../../agents/web_agent.py#L3048) | 3048 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003049](../../agents/web_agent.py#L3049) | 3049 | `"                # This application consumes a final text completion from an"` | — |
| [SRC-1AE03B9EC3-L003050](../../agents/web_agent.py#L3050) | 3050 | `"                # OpenAI-compatible /chat/completions endpoint. Fail closed when the"` | — |
| [SRC-1AE03B9EC3-L003051](../../agents/web_agent.py#L3051) | 3051 | `"                # provider does not explicitly report the standardized \"stop\" reason."` | — |
| [SRC-1AE03B9EC3-L003052](../../agents/web_agent.py#L3052) | 3052 | `"                if normalized_finish_reason != \"stop\":"` | — |
| [SRC-1AE03B9EC3-L003053](../../agents/web_agent.py#L3053) | 3053 | `"                    if normalized_finish_reason in {\"length\", \"max_tokens\"}:"` | — |
| [SRC-1AE03B9EC3-L003054](../../agents/web_agent.py#L3054) | 3054 | `"                        diagnostic_status = \"truncated\""` | — |
| [SRC-1AE03B9EC3-L003055](../../agents/web_agent.py#L3055) | 3055 | `"                        last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L003056](../../agents/web_agent.py#L3056) | 3056 | `"                            \"أعاد نموذج اللغة إجابة مبتورة بسبب الوصول إلى حد الرموز؛ \""` | — |
| [SRC-1AE03B9EC3-L003057](../../agents/web_agent.py#L3057) | 3057 | `"                            \"لم تُقبل كإجابة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L003058](../../agents/web_agent.py#L3058) | 3058 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003059](../../agents/web_agent.py#L3059) | 3059 | `"                    elif not normalized_finish_reason:"` | — |
| [SRC-1AE03B9EC3-L003060](../../agents/web_agent.py#L3060) | 3060 | `"                        diagnostic_status = \"finish_reason_missing\""` | — |
| [SRC-1AE03B9EC3-L003061](../../agents/web_agent.py#L3061) | 3061 | `"                        last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L003062](../../agents/web_agent.py#L3062) | 3062 | `"                            \"لم تقدم خدمة النموذج سبب انتهاء واضحًا؛ لم تُقبل الإجابة \""` | — |
| [SRC-1AE03B9EC3-L003063](../../agents/web_agent.py#L3063) | 3063 | `"                            \"كإجابة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L003064](../../agents/web_agent.py#L3064) | 3064 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003065](../../agents/web_agent.py#L3065) | 3065 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L003066](../../agents/web_agent.py#L3066) | 3066 | `"                        diagnostic_status = \"finish_reason_not_accepted\""` | — |
| [SRC-1AE03B9EC3-L003067](../../agents/web_agent.py#L3067) | 3067 | `"                        last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L003068](../../agents/web_agent.py#L3068) | 3068 | `"                            \"لم تُكمل خدمة النموذج إجابة نصية نهائية مقبولة \""` | — |
| [SRC-1AE03B9EC3-L003069](../../agents/web_agent.py#L3069) | 3069 | `"                            \"(حالة الإنهاء: \" + normalized_finish_reason[:40] + \").\""` | — |
| [SRC-1AE03B9EC3-L003070](../../agents/web_agent.py#L3070) | 3070 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003071](../../agents/web_agent.py#L3071) | 3071 | `"                    self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L003072](../../agents/web_agent.py#L3072) | 3072 | `"                        requested_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L003073](../../agents/web_agent.py#L3073) | 3073 | `"                        attempted_model=candidate_model,"` | — |
| [SRC-1AE03B9EC3-L003074](../../agents/web_agent.py#L3074) | 3074 | `"                        status=diagnostic_status,"` | — |
| [SRC-1AE03B9EC3-L003075](../../agents/web_agent.py#L3075) | 3075 | `"                        finish_reason=normalized_finish_reason or None,"` | — |
| [SRC-1AE03B9EC3-L003076](../../agents/web_agent.py#L3076) | 3076 | `"                        request_started=True,"` | — |
| [SRC-1AE03B9EC3-L003077](../../agents/web_agent.py#L3077) | 3077 | `"                        remote_response_received=True,"` | — |
| [SRC-1AE03B9EC3-L003078](../../agents/web_agent.py#L3078) | 3078 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003079](../../agents/web_agent.py#L3079) | 3079 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L003080](../../agents/web_agent.py#L3080) | 3080 | `"                message = choice[\"message\"]"` | — |
| [SRC-1AE03B9EC3-L003081](../../agents/web_agent.py#L3081) | 3081 | `"                answer = message[\"content\"]"` | — |
| [SRC-1AE03B9EC3-L003082](../../agents/web_agent.py#L3082) | 3082 | `"                if use_web_search:"` | — |
| [SRC-1AE03B9EC3-L003083](../../agents/web_agent.py#L3083) | 3083 | `"                    for annotation in message.get(\"annotations\", []):"` | — |
| [SRC-1AE03B9EC3-L003084](../../agents/web_agent.py#L3084) | 3084 | `"                        if not isinstance(annotation, dict) or annotation.get(\"type\") != \"url_citation\":"` | — |
| [SRC-1AE03B9EC3-L003085](../../agents/web_agent.py#L3085) | 3085 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L003086](../../agents/web_agent.py#L3086) | 3086 | `"                        citation = annotation.get(\"url_citation\", annotation)"` | — |
| [SRC-1AE03B9EC3-L003087](../../agents/web_agent.py#L3087) | 3087 | `"                        if not isinstance(citation, dict):"` | — |
| [SRC-1AE03B9EC3-L003088](../../agents/web_agent.py#L3088) | 3088 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L003089](../../agents/web_agent.py#L3089) | 3089 | `"                        url = _public_http_url(citation.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L003090](../../agents/web_agent.py#L3090) | 3090 | `"                        if not url or any(item.get(\"url\") == url for item in self.server_search_sources):"` | — |
| [SRC-1AE03B9EC3-L003091](../../agents/web_agent.py#L3091) | 3091 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L003092](../../agents/web_agent.py#L3092) | 3092 | `"                        parsed_url = urllib.parse.urlparse(url)"` | — |
| [SRC-1AE03B9EC3-L003093](../../agents/web_agent.py#L3093) | 3093 | `"                        excerpt = _clean_text(citation.get(\"content\", \"\"), 1800)"` | — |
| [SRC-1AE03B9EC3-L003094](../../agents/web_agent.py#L3094) | 3094 | `"                        self.server_search_sources.append({"` | — |
| [SRC-1AE03B9EC3-L003095](../../agents/web_agent.py#L3095) | 3095 | `"                            \"title\": _clean_text(citation.get(\"title\", \"\"), 300) or parsed_url.netloc,"` | — |
| [SRC-1AE03B9EC3-L003096](../../agents/web_agent.py#L3096) | 3096 | `"                            \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L003097](../../agents/web_agent.py#L3097) | 3097 | `"                            \"snippet\": excerpt,"` | — |
| [SRC-1AE03B9EC3-L003098](../../agents/web_agent.py#L3098) | 3098 | `"                            \"page_text\": excerpt,"` | — |
| [SRC-1AE03B9EC3-L003099](../../agents/web_agent.py#L3099) | 3099 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L003100](../../agents/web_agent.py#L3100) | 3100 | `"                            \"provider\": \"openrouter_web_search\","` | — |
| [SRC-1AE03B9EC3-L003101](../../agents/web_agent.py#L3101) | 3101 | `"                            \"providers\": [\"openrouter_web_search\"],"` | — |
| [SRC-1AE03B9EC3-L003102](../../agents/web_agent.py#L3102) | 3102 | `"                            \"queries\": [],"` | — |
| [SRC-1AE03B9EC3-L003103](../../agents/web_agent.py#L3103) | 3103 | `"                            \"domain\": parsed_url.netloc.lower(),"` | — |
| [SRC-1AE03B9EC3-L003104](../../agents/web_agent.py#L3104) | 3104 | `"                            \"source_class\": \"general\","` | — |
| [SRC-1AE03B9EC3-L003105](../../agents/web_agent.py#L3105) | 3105 | `"                            \"platform\": \"web\","` | — |
| [SRC-1AE03B9EC3-L003106](../../agents/web_agent.py#L3106) | 3106 | `"                            \"published_at\": \"\","` | — |
| [SRC-1AE03B9EC3-L003107](../../agents/web_agent.py#L3107) | 3107 | `"                            \"rank_score\": 0.0,"` | — |
| [SRC-1AE03B9EC3-L003108](../../agents/web_agent.py#L3108) | 3108 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L003109](../../agents/web_agent.py#L3109) | 3109 | `"                if isinstance(answer, list):"` | — |
| [SRC-1AE03B9EC3-L003110](../../agents/web_agent.py#L3110) | 3110 | `"                    answer = \"\".join("` | — |
| [SRC-1AE03B9EC3-L003111](../../agents/web_agent.py#L3111) | 3111 | `"                        item.get(\"text\", \"\") for item in answer if isinstance(item, dict)"` | — |
| [SRC-1AE03B9EC3-L003112](../../agents/web_agent.py#L3112) | 3112 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003113](../../agents/web_agent.py#L3113) | 3113 | `"                if not isinstance(answer, str) or not answer.strip():"` | — |
| [SRC-1AE03B9EC3-L003114](../../agents/web_agent.py#L3114) | 3114 | `"                    raise ValueError(\"empty model response\")"` | — |
| [SRC-1AE03B9EC3-L003115](../../agents/web_agent.py#L3115) | 3115 | `"                self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L003116](../../agents/web_agent.py#L3116) | 3116 | `"                    requested_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L003117](../../agents/web_agent.py#L3117) | 3117 | `"                    attempted_model=candidate_model,"` | — |
| [SRC-1AE03B9EC3-L003118](../../agents/web_agent.py#L3118) | 3118 | `"                    status=\"accepted\","` | — |
| [SRC-1AE03B9EC3-L003119](../../agents/web_agent.py#L3119) | 3119 | `"                    finish_reason=normalized_finish_reason,"` | — |
| [SRC-1AE03B9EC3-L003120](../../agents/web_agent.py#L3120) | 3120 | `"                    request_started=True,"` | — |
| [SRC-1AE03B9EC3-L003121](../../agents/web_agent.py#L3121) | 3121 | `"                    remote_response_received=True,"` | — |
| [SRC-1AE03B9EC3-L003122](../../agents/web_agent.py#L3122) | 3122 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003123](../../agents/web_agent.py#L3123) | 3123 | `"                self.model_usage.append({"` | — |
| [SRC-1AE03B9EC3-L003124](../../agents/web_agent.py#L3124) | 3124 | `"                    \"requested_model\": requested_model,"` | — |
| [SRC-1AE03B9EC3-L003125](../../agents/web_agent.py#L3125) | 3125 | `"                    \"used_model\": candidate_model,"` | — |
| [SRC-1AE03B9EC3-L003126](../../agents/web_agent.py#L3126) | 3126 | `"                    \"fallback_used\": \"true\" if candidate_model != requested_model else \"false\","` | — |
| [SRC-1AE03B9EC3-L003127](../../agents/web_agent.py#L3127) | 3127 | `"                })"` | — |
| [SRC-1AE03B9EC3-L003128](../../agents/web_agent.py#L3128) | 3128 | `"                return answer.strip()"` | — |
| [SRC-1AE03B9EC3-L003129](../../agents/web_agent.py#L3129) | 3129 | `"            except urllib.error.HTTPError as exc:"` | — |
| [SRC-1AE03B9EC3-L003130](../../agents/web_agent.py#L3130) | 3130 | `"                # Never echo provider response bodies: they may contain private diagnostics."` | — |
| [SRC-1AE03B9EC3-L003131](../../agents/web_agent.py#L3131) | 3131 | `"                self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L003132](../../agents/web_agent.py#L3132) | 3132 | `"                    requested_model, candidate_model, \"provider_http_error\","` | — |
| [SRC-1AE03B9EC3-L003133](../../agents/web_agent.py#L3133) | 3133 | `"                    error_class=\"HTTPError\", request_started=True,"` | — |
| [SRC-1AE03B9EC3-L003134](../../agents/web_agent.py#L3134) | 3134 | `"                    remote_response_received=True,"` | — |
| [SRC-1AE03B9EC3-L003135](../../agents/web_agent.py#L3135) | 3135 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003136](../../agents/web_agent.py#L3136) | 3136 | `"                last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L003137](../../agents/web_agent.py#L3137) | 3137 | `"                    f\"خدمة نموذج اللغة رفضت الطلب (HTTP {exc.code}) على النموذج المحدد.\""` | — |
| [SRC-1AE03B9EC3-L003138](../../agents/web_agent.py#L3138) | 3138 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003139](../../agents/web_agent.py#L3139) | 3139 | `"            except (urllib.error.URLError, TimeoutError, OSError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003140](../../agents/web_agent.py#L3140) | 3140 | `"                self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L003141](../../agents/web_agent.py#L3141) | 3141 | `"                    requested_model, candidate_model, \"connection_error\","` | — |
| [SRC-1AE03B9EC3-L003142](../../agents/web_agent.py#L3142) | 3142 | `"                    error_class=type(exc).__name__, request_started=True,"` | — |
| [SRC-1AE03B9EC3-L003143](../../agents/web_agent.py#L3143) | 3143 | `"                    remote_response_received=None,"` | — |
| [SRC-1AE03B9EC3-L003144](../../agents/web_agent.py#L3144) | 3144 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003145](../../agents/web_agent.py#L3145) | 3145 | `"                last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L003146](../../agents/web_agent.py#L3146) | 3146 | `"                    \"تعذر الاتصال بخدمة نموذج اللغة؛ جرت محاولة استخدام النموذج الاحتياطي.\""` | — |
| [SRC-1AE03B9EC3-L003147](../../agents/web_agent.py#L3147) | 3147 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003148](../../agents/web_agent.py#L3148) | 3148 | `"            except (KeyError, IndexError, TypeError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003149](../../agents/web_agent.py#L3149) | 3149 | `"                self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L003150](../../agents/web_agent.py#L3150) | 3150 | `"                    requested_model, candidate_model, \"invalid_response\","` | — |
| [SRC-1AE03B9EC3-L003151](../../agents/web_agent.py#L3151) | 3151 | `"                    error_class=type(exc).__name__, request_started=True,"` | — |
| [SRC-1AE03B9EC3-L003152](../../agents/web_agent.py#L3152) | 3152 | `"                    remote_response_received=True,"` | — |
| [SRC-1AE03B9EC3-L003153](../../agents/web_agent.py#L3153) | 3153 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003154](../../agents/web_agent.py#L3154) | 3154 | `"                last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L003155](../../agents/web_agent.py#L3155) | 3155 | `"                    \"خدمة نموذج اللغة أعادت استجابة غير صالحة؛ جرت محاولة استخدام النموذج الاحتياطي.\""` | — |
| [SRC-1AE03B9EC3-L003156](../../agents/web_agent.py#L3156) | 3156 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003157](../../agents/web_agent.py#L3157) | 3157 | `""` | — |
| [SRC-1AE03B9EC3-L003158](../../agents/web_agent.py#L3158) | 3158 | `"        raise last_error or RuntimeError(\"تعذر توليد إجابة من النموذج اللغوي.\")"` | — |
| [SRC-1AE03B9EC3-L003159](../../agents/web_agent.py#L3159) | 3159 | `""` | — |
| [SRC-1AE03B9EC3-L003160](../../agents/web_agent.py#L3160) | 3160 | `"    def _resolve_dialogue_context("` | — |
| [SRC-1AE03B9EC3-L003161](../../agents/web_agent.py#L3161) | 3161 | `"        self, question: str, history: list[dict[str, str]]"` | — |
| [SRC-1AE03B9EC3-L003162](../../agents/web_agent.py#L3162) | 3162 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L003163](../../agents/web_agent.py#L3163) | 3163 | `"        \"\"\"Use the configured language model to resolve dialogue meaning, never to search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L003164](../../agents/web_agent.py#L3164) | 3164 | `"        fallback = fallback_dialogue_context(question, history)"` | — |
| [SRC-1AE03B9EC3-L003165](../../agents/web_agent.py#L3165) | 3165 | `"        if not self.api_key or not history:"` | — |
| [SRC-1AE03B9EC3-L003166](../../agents/web_agent.py#L3166) | 3166 | `"            return fallback"` | — |
| [SRC-1AE03B9EC3-L003167](../../agents/web_agent.py#L3167) | 3167 | `"        messages = ["` | — |
