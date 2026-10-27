# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **007**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L002245 إلى SRC-1AE03B9EC3-L003044
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L002245](../../agents/web_agent.py#L2245) | 2245 | `"                    search_started_queries += 1"` | — |
| [SRC-1AE03B9EC3-L002246](../../agents/web_agent.py#L2246) | 2246 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002247](../../agents/web_agent.py#L2247) | 2247 | `"                        results = future.result()"` | — |
| [SRC-1AE03B9EC3-L002248](../../agents/web_agent.py#L2248) | 2248 | `"                    except (RequestBudgetExceeded, RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002249](../../agents/web_agent.py#L2249) | 2249 | `"                        warnings.append(f\"تعذر بحث الاستعلام «{query[:70]}»: {exc}\")"` | — |
| [SRC-1AE03B9EC3-L002250](../../agents/web_agent.py#L2250) | 2250 | `"                        query_counts.append({\"query\": query, \"results\": 0})"` | — |
| [SRC-1AE03B9EC3-L002251](../../agents/web_agent.py#L2251) | 2251 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002252](../../agents/web_agent.py#L2252) | 2252 | `"                    query_counts.append({\"query\": query, \"results\": len(results)})"` | — |
| [SRC-1AE03B9EC3-L002253](../../agents/web_agent.py#L2253) | 2253 | `"                    grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002254](../../agents/web_agent.py#L2254) | 2254 | `"                    for source in results:"` | — |
| [SRC-1AE03B9EC3-L002255](../../agents/web_agent.py#L2255) | 2255 | `"                        provider = str(source.get(\"provider\") or \"web_search\")"` | — |
| [SRC-1AE03B9EC3-L002256](../../agents/web_agent.py#L2256) | 2256 | `"                        grouped.setdefault(provider, []).append(source)"` | — |
| [SRC-1AE03B9EC3-L002257](../../agents/web_agent.py#L2257) | 2257 | `"                    for provider, items in grouped.items():"` | — |
| [SRC-1AE03B9EC3-L002258](../../agents/web_agent.py#L2258) | 2258 | `"                        items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002259](../../agents/web_agent.py#L2259) | 2259 | `"                        batches.append({\"query\": query, \"provider\": provider, \"results\": items})"` | — |
| [SRC-1AE03B9EC3-L002260](../../agents/web_agent.py#L2260) | 2260 | `""` | — |
| [SRC-1AE03B9EC3-L002261](../../agents/web_agent.py#L2261) | 2261 | `"        # Evidence-gap iteration: deep tasks get up to three targeted follow-up searches"` | — |
| [SRC-1AE03B9EC3-L002262](../../agents/web_agent.py#L2262) | 2262 | `"        # when initial coverage is thin. This uses observed source/domain/provider coverage,"` | — |
| [SRC-1AE03B9EC3-L002263](../../agents/web_agent.py#L2263) | 2263 | `"        # not the language model's subjective claim that it has enough evidence."` | — |
| [SRC-1AE03B9EC3-L002264](../../agents/web_agent.py#L2264) | 2264 | `"        preliminary = fuse_ranked_results(batches, limit=MAX_SEARCH_RESULTS)"` | — |
| [SRC-1AE03B9EC3-L002265](../../agents/web_agent.py#L2265) | 2265 | `"        preliminary_domains = {"` | — |
| [SRC-1AE03B9EC3-L002266](../../agents/web_agent.py#L2266) | 2266 | `"            registrable_domain(item.get(\"domain\") or urllib.parse.urlparse(item.get(\"url\", \"\")).hostname)"` | — |
| [SRC-1AE03B9EC3-L002267](../../agents/web_agent.py#L2267) | 2267 | `"            for item in preliminary"` | — |
| [SRC-1AE03B9EC3-L002268](../../agents/web_agent.py#L2268) | 2268 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002269](../../agents/web_agent.py#L2269) | 2269 | `"        preliminary_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L002270](../../agents/web_agent.py#L2270) | 2270 | `"        preliminary_providers = {"` | — |
| [SRC-1AE03B9EC3-L002271](../../agents/web_agent.py#L2271) | 2271 | `"            provider for item in preliminary for provider in item.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L002272](../../agents/web_agent.py#L2272) | 2272 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002273](../../agents/web_agent.py#L2273) | 2273 | `"        needs_expansion = ("` | — |
| [SRC-1AE03B9EC3-L002274](../../agents/web_agent.py#L2274) | 2274 | `"            plan.get(\"depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L002275](../../agents/web_agent.py#L2275) | 2275 | `"            and (len(preliminary) < 8 or len(preliminary_domains) < 5 or len(preliminary_providers) < 2)"` | — |
| [SRC-1AE03B9EC3-L002276](../../agents/web_agent.py#L2276) | 2276 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002277](../../agents/web_agent.py#L2277) | 2277 | `"        expansion_queries: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002278](../../agents/web_agent.py#L2278) | 2278 | `"        if needs_expansion and len(queries) < MAX_PLAN_QUERIES and queries:"` | — |
| [SRC-1AE03B9EC3-L002279](../../agents/web_agent.py#L2279) | 2279 | `"            base_query = (queries[0] if queries else \"\")"` | — |
| [SRC-1AE03B9EC3-L002280](../../agents/web_agent.py#L2280) | 2280 | `"            candidates = ["` | — |
| [SRC-1AE03B9EC3-L002281](../../agents/web_agent.py#L2281) | 2281 | `"                f\"{base_query} official sources data reports\","` | — |
| [SRC-1AE03B9EC3-L002282](../../agents/web_agent.py#L2282) | 2282 | `"                f\"{base_query} limitations risks criticism alternatives\","` | — |
| [SRC-1AE03B9EC3-L002283](../../agents/web_agent.py#L2283) | 2283 | `"                f\"{base_query} recent developments case studies analysis\","` | — |
| [SRC-1AE03B9EC3-L002284](../../agents/web_agent.py#L2284) | 2284 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L002285](../../agents/web_agent.py#L2285) | 2285 | `"            existing = {item.casefold() for item in queries}"` | — |
| [SRC-1AE03B9EC3-L002286](../../agents/web_agent.py#L2286) | 2286 | `"            expansion_queries = []"` | — |
| [SRC-1AE03B9EC3-L002287](../../agents/web_agent.py#L2287) | 2287 | `"            seen_expansions = set(existing)"` | — |
| [SRC-1AE03B9EC3-L002288](../../agents/web_agent.py#L2288) | 2288 | `"            for candidate in candidates:"` | — |
| [SRC-1AE03B9EC3-L002289](../../agents/web_agent.py#L2289) | 2289 | `"                compacted = compact_search_query(candidate)"` | — |
| [SRC-1AE03B9EC3-L002290](../../agents/web_agent.py#L2290) | 2290 | `"                key = compacted.casefold()"` | — |
| [SRC-1AE03B9EC3-L002291](../../agents/web_agent.py#L2291) | 2291 | `"                if compacted and key not in seen_expansions:"` | — |
| [SRC-1AE03B9EC3-L002292](../../agents/web_agent.py#L2292) | 2292 | `"                    expansion_queries.append(compacted)"` | — |
| [SRC-1AE03B9EC3-L002293](../../agents/web_agent.py#L2293) | 2293 | `"                    seen_expansions.add(key)"` | — |
| [SRC-1AE03B9EC3-L002294](../../agents/web_agent.py#L2294) | 2294 | `"                if len(expansion_queries) >= max(0, MAX_PLAN_QUERIES - len(queries)):"` | — |
| [SRC-1AE03B9EC3-L002295](../../agents/web_agent.py#L2295) | 2295 | `"                    break"` | — |
| [SRC-1AE03B9EC3-L002296](../../agents/web_agent.py#L2296) | 2296 | `"            if expansion_queries:"` | — |
| [SRC-1AE03B9EC3-L002297](../../agents/web_agent.py#L2297) | 2297 | `"                with ThreadPoolExecutor("` | — |
| [SRC-1AE03B9EC3-L002298](../../agents/web_agent.py#L2298) | 2298 | `"                    max_workers=min(MAX_RESEARCH_WORKERS, len(expansion_queries))"` | — |
| [SRC-1AE03B9EC3-L002299](../../agents/web_agent.py#L2299) | 2299 | `"                ) as pool:"` | — |
| [SRC-1AE03B9EC3-L002300](../../agents/web_agent.py#L2300) | 2300 | `"                    futures = {"` | — |
| [SRC-1AE03B9EC3-L002301](../../agents/web_agent.py#L2301) | 2301 | `"                        pool.submit(self._search_web, query): query"` | — |
| [SRC-1AE03B9EC3-L002302](../../agents/web_agent.py#L2302) | 2302 | `"                        for query in expansion_queries"` | — |
| [SRC-1AE03B9EC3-L002303](../../agents/web_agent.py#L2303) | 2303 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L002304](../../agents/web_agent.py#L2304) | 2304 | `"                    for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002305](../../agents/web_agent.py#L2305) | 2305 | `"                        query = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002306](../../agents/web_agent.py#L2306) | 2306 | `"                        search_started_queries += 1"` | — |
| [SRC-1AE03B9EC3-L002307](../../agents/web_agent.py#L2307) | 2307 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L002308](../../agents/web_agent.py#L2308) | 2308 | `"                            results = future.result()"` | — |
| [SRC-1AE03B9EC3-L002309](../../agents/web_agent.py#L2309) | 2309 | `"                        except (RequestBudgetExceeded, RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002310](../../agents/web_agent.py#L2310) | 2310 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002311](../../agents/web_agent.py#L2311) | 2311 | `"                                f\"تعذر بحث زاوية إضافية «{query[:70]}»: {exc}\""` | — |
| [SRC-1AE03B9EC3-L002312](../../agents/web_agent.py#L2312) | 2312 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002313](../../agents/web_agent.py#L2313) | 2313 | `"                            query_counts.append({\"query\": query, \"results\": 0})"` | — |
| [SRC-1AE03B9EC3-L002314](../../agents/web_agent.py#L2314) | 2314 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002315](../../agents/web_agent.py#L2315) | 2315 | `"                        query_counts.append({\"query\": query, \"results\": len(results)})"` | — |
| [SRC-1AE03B9EC3-L002316](../../agents/web_agent.py#L2316) | 2316 | `"                        grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002317](../../agents/web_agent.py#L2317) | 2317 | `"                        for source in results:"` | — |
| [SRC-1AE03B9EC3-L002318](../../agents/web_agent.py#L2318) | 2318 | `"                            grouped.setdefault("` | — |
| [SRC-1AE03B9EC3-L002319](../../agents/web_agent.py#L2319) | 2319 | `"                                str(source.get(\"provider\") or \"web_search\"), []"` | — |
| [SRC-1AE03B9EC3-L002320](../../agents/web_agent.py#L2320) | 2320 | `"                            ).append(source)"` | — |
| [SRC-1AE03B9EC3-L002321](../../agents/web_agent.py#L2321) | 2321 | `"                        for provider, items in grouped.items():"` | — |
| [SRC-1AE03B9EC3-L002322](../../agents/web_agent.py#L2322) | 2322 | `"                            items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002323](../../agents/web_agent.py#L2323) | 2323 | `"                            batches.append({"` | — |
| [SRC-1AE03B9EC3-L002324](../../agents/web_agent.py#L2324) | 2324 | `"                                \"query\": query, \"provider\": provider, \"results\": items"` | — |
| [SRC-1AE03B9EC3-L002325](../../agents/web_agent.py#L2325) | 2325 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L002326](../../agents/web_agent.py#L2326) | 2326 | `"                queries.extend(expansion_queries)"` | — |
| [SRC-1AE03B9EC3-L002327](../../agents/web_agent.py#L2327) | 2327 | `"                plan[\"queries\"] = list(queries)"` | — |
| [SRC-1AE03B9EC3-L002328](../../agents/web_agent.py#L2328) | 2328 | `""` | — |
| [SRC-1AE03B9EC3-L002329](../../agents/web_agent.py#L2329) | 2329 | `"        # Google News RSS is included concurrently by _search_web for freshness-bearing queries."` | — |
| [SRC-1AE03B9EC3-L002330](../../agents/web_agent.py#L2330) | 2330 | `""` | — |
| [SRC-1AE03B9EC3-L002331](../../agents/web_agent.py#L2331) | 2331 | `"        # A social-focused task uses public social endpoints in parallel with indexed"` | — |
| [SRC-1AE03B9EC3-L002332](../../agents/web_agent.py#L2332) | 2332 | `"        # public pages. No login, private profile, session cookie or anti-bot bypass."` | — |
| [SRC-1AE03B9EC3-L002333](../../agents/web_agent.py#L2333) | 2333 | `"        social_results: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002334](../../agents/web_agent.py#L2334) | 2334 | `"        if plan.get(\"social_focus\") and queries:"` | — |
| [SRC-1AE03B9EC3-L002335](../../agents/web_agent.py#L2335) | 2335 | `"            requested_platforms = plan.get(\"platforms\") or []"` | — |
| [SRC-1AE03B9EC3-L002336](../../agents/web_agent.py#L2336) | 2336 | `"            if requested_platforms:"` | — |
| [SRC-1AE03B9EC3-L002337](../../agents/web_agent.py#L2337) | 2337 | `"                platforms = list(dict.fromkeys(requested_platforms))"` | — |
| [SRC-1AE03B9EC3-L002338](../../agents/web_agent.py#L2338) | 2338 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002339](../../agents/web_agent.py#L2339) | 2339 | `"                # Broad social research: always try no-key public sources, and add"` | — |
| [SRC-1AE03B9EC3-L002340](../../agents/web_agent.py#L2340) | 2340 | `"                # official platform connectors only when they are configured."` | — |
| [SRC-1AE03B9EC3-L002341](../../agents/web_agent.py#L2341) | 2341 | `"                platforms = [\"reddit\", \"bluesky\"]"` | — |
| [SRC-1AE03B9EC3-L002342](../../agents/web_agent.py#L2342) | 2342 | `"                optional_connectors = {"` | — |
| [SRC-1AE03B9EC3-L002343](../../agents/web_agent.py#L2343) | 2343 | `"                    \"facebook\": bool("` | — |
| [SRC-1AE03B9EC3-L002344](../../agents/web_agent.py#L2344) | 2344 | `"                        os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002345](../../agents/web_agent.py#L2345) | 2345 | `"                        and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002346](../../agents/web_agent.py#L2346) | 2346 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L002347](../../agents/web_agent.py#L2347) | 2347 | `"                    \"instagram\": bool("` | — |
| [SRC-1AE03B9EC3-L002348](../../agents/web_agent.py#L2348) | 2348 | `"                        os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002349](../../agents/web_agent.py#L2349) | 2349 | `"                        and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002350](../../agents/web_agent.py#L2350) | 2350 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L002351](../../agents/web_agent.py#L2351) | 2351 | `"                    \"x\": bool(os.getenv(\"X_BEARER_TOKEN\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L002352](../../agents/web_agent.py#L2352) | 2352 | `"                    \"youtube\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L002353](../../agents/web_agent.py#L2353) | 2353 | `"                }"` | — |
| [SRC-1AE03B9EC3-L002354](../../agents/web_agent.py#L2354) | 2354 | `"                platforms.extend("` | — |
| [SRC-1AE03B9EC3-L002355](../../agents/web_agent.py#L2355) | 2355 | `"                    name for name, ready in optional_connectors.items()"` | — |
| [SRC-1AE03B9EC3-L002356](../../agents/web_agent.py#L2356) | 2356 | `"                    if ready and name not in platforms"` | — |
| [SRC-1AE03B9EC3-L002357](../../agents/web_agent.py#L2357) | 2357 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002358](../../agents/web_agent.py#L2358) | 2358 | `"            social_results, social_warnings = self._search_social((queries[0] if queries else \"\"), platforms)"` | — |
| [SRC-1AE03B9EC3-L002359](../../agents/web_agent.py#L2359) | 2359 | `"            warnings.extend(social_warnings)"` | — |
| [SRC-1AE03B9EC3-L002360](../../agents/web_agent.py#L2360) | 2360 | `"            social_groups: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002361](../../agents/web_agent.py#L2361) | 2361 | `"            for source in social_results:"` | — |
| [SRC-1AE03B9EC3-L002362](../../agents/web_agent.py#L2362) | 2362 | `"                social_groups.setdefault(str(source.get(\"provider\") or \"social\"), []).append(source)"` | — |
| [SRC-1AE03B9EC3-L002363](../../agents/web_agent.py#L2363) | 2363 | `"            for provider, items in social_groups.items():"` | — |
| [SRC-1AE03B9EC3-L002364](../../agents/web_agent.py#L2364) | 2364 | `"                items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002365](../../agents/web_agent.py#L2365) | 2365 | `"                batches.append({\"query\": (queries[0] if queries else \"\"), \"provider\": provider, \"results\": items})"` | — |
| [SRC-1AE03B9EC3-L002366](../../agents/web_agent.py#L2366) | 2366 | `""` | — |
| [SRC-1AE03B9EC3-L002367](../../agents/web_agent.py#L2367) | 2367 | `"        # Explicit URLs are first-class inputs: fetch the page the user actually asked about"` | — |
| [SRC-1AE03B9EC3-L002368](../../agents/web_agent.py#L2368) | 2368 | `"        # instead of relying on a search engine to rediscover it. URL and DNS checks still apply."` | — |
| [SRC-1AE03B9EC3-L002369](../../agents/web_agent.py#L2369) | 2369 | `"        direct_urls: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002370](../../agents/web_agent.py#L2370) | 2370 | `"        for value in plan.get(\"direct_urls\", [])[:5]:"` | — |
| [SRC-1AE03B9EC3-L002371](../../agents/web_agent.py#L2371) | 2371 | `"            safe_url = _public_http_url(value)"` | — |
| [SRC-1AE03B9EC3-L002372](../../agents/web_agent.py#L2372) | 2372 | `"            if safe_url and not _blocked_source_url(safe_url) and safe_url not in direct_urls:"` | — |
| [SRC-1AE03B9EC3-L002373](../../agents/web_agent.py#L2373) | 2373 | `"                direct_urls.append(safe_url)"` | — |
| [SRC-1AE03B9EC3-L002374](../../agents/web_agent.py#L2374) | 2374 | `"        for direct_url in direct_urls:"` | — |
| [SRC-1AE03B9EC3-L002375](../../agents/web_agent.py#L2375) | 2375 | `"            batches.append({"` | — |
| [SRC-1AE03B9EC3-L002376](../../agents/web_agent.py#L2376) | 2376 | `"                \"query\": (queries[0] if queries else \"\"),"` | — |
| [SRC-1AE03B9EC3-L002377](../../agents/web_agent.py#L2377) | 2377 | `"                \"provider\": \"user_supplied_url\","` | — |
| [SRC-1AE03B9EC3-L002378](../../agents/web_agent.py#L2378) | 2378 | `"                \"results\": [{"` | — |
| [SRC-1AE03B9EC3-L002379](../../agents/web_agent.py#L2379) | 2379 | `"                    \"title\": \"رابط قدمه المستخدم للتحليل\","` | — |
| [SRC-1AE03B9EC3-L002380](../../agents/web_agent.py#L2380) | 2380 | `"                    \"url\": direct_url,"` | — |
| [SRC-1AE03B9EC3-L002381](../../agents/web_agent.py#L2381) | 2381 | `"                    \"snippet\": \"\","` | — |
| [SRC-1AE03B9EC3-L002382](../../agents/web_agent.py#L2382) | 2382 | `"                    \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002383](../../agents/web_agent.py#L2383) | 2383 | `"                    \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002384](../../agents/web_agent.py#L2384) | 2384 | `"                    \"provider\": \"user_supplied_url\","` | — |
| [SRC-1AE03B9EC3-L002385](../../agents/web_agent.py#L2385) | 2385 | `"                    \"provider_rank\": 1,"` | — |
| [SRC-1AE03B9EC3-L002386](../../agents/web_agent.py#L2386) | 2386 | `"                    \"search_query\": (queries[0] if queries else \"\"),"` | — |
| [SRC-1AE03B9EC3-L002387](../../agents/web_agent.py#L2387) | 2387 | `"                    \"published_at\": \"\","` | — |
| [SRC-1AE03B9EC3-L002388](../../agents/web_agent.py#L2388) | 2388 | `"                }],"` | — |
| [SRC-1AE03B9EC3-L002389](../../agents/web_agent.py#L2389) | 2389 | `"            })"` | — |
| [SRC-1AE03B9EC3-L002390](../../agents/web_agent.py#L2390) | 2390 | `""` | — |
| [SRC-1AE03B9EC3-L002391](../../agents/web_agent.py#L2391) | 2391 | `"        raw_results_count = sum(len(batch.get(\"results\", [])) for batch in batches if isinstance(batch, dict) and isinstance(batch.get(\"results\", []), list))"` | — |
| [SRC-1AE03B9EC3-L002392](../../agents/web_agent.py#L2392) | 2392 | `"        sources = fuse_ranked_results(batches, limit=MAX_SEARCH_RESULTS)"` | — |
| [SRC-1AE03B9EC3-L002393](../../agents/web_agent.py#L2393) | 2393 | `""` | — |
| [SRC-1AE03B9EC3-L002394](../../agents/web_agent.py#L2394) | 2394 | `"        # Keep at least one returned source per explicit criterion query in the"` | — |
| [SRC-1AE03B9EC3-L002395](../../agents/web_agent.py#L2395) | 2395 | `"        # bounded source set sent to synthesis. Global fusion can otherwise crowd"` | — |
| [SRC-1AE03B9EC3-L002396](../../agents/web_agent.py#L2396) | 2396 | `"        # lower-ranked criterion results out before the model can inspect them."` | — |
| [SRC-1AE03B9EC3-L002397](../../agents/web_agent.py#L2397) | 2397 | `"        requirement_queries = plan.get(\"requirement_queries\", [])"` | — |
| [SRC-1AE03B9EC3-L002398](../../agents/web_agent.py#L2398) | 2398 | `"        if isinstance(requirement_queries, list) and requirement_queries:"` | — |
| [SRC-1AE03B9EC3-L002399](../../agents/web_agent.py#L2399) | 2399 | `"            globally_fused = sources"` | — |
| [SRC-1AE03B9EC3-L002400](../../agents/web_agent.py#L2400) | 2400 | `"            globally_fused_by_url = {"` | — |
| [SRC-1AE03B9EC3-L002401](../../agents/web_agent.py#L2401) | 2401 | `"                _normalized_source_url_key(item.get(\"url\", \"\")): item"` | — |
| [SRC-1AE03B9EC3-L002402](../../agents/web_agent.py#L2402) | 2402 | `"                for item in globally_fused"` | — |
| [SRC-1AE03B9EC3-L002403](../../agents/web_agent.py#L2403) | 2403 | `"                if _normalized_source_url_key(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002404](../../agents/web_agent.py#L2404) | 2404 | `"            }"` | — |
| [SRC-1AE03B9EC3-L002405](../../agents/web_agent.py#L2405) | 2405 | `"            pinned_by_url: dict[str, dict[str, Any]] = {}"` | — |
| [SRC-1AE03B9EC3-L002406](../../agents/web_agent.py#L2406) | 2406 | `"            pinned_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002407](../../agents/web_agent.py#L2407) | 2407 | `"            for requirement in requirement_queries[:MAX_PLAN_QUERIES]:"` | — |
| [SRC-1AE03B9EC3-L002408](../../agents/web_agent.py#L2408) | 2408 | `"                if not isinstance(requirement, dict):"` | — |
| [SRC-1AE03B9EC3-L002409](../../agents/web_agent.py#L2409) | 2409 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002410](../../agents/web_agent.py#L2410) | 2410 | `"                target_query = compact_search_query(str(requirement.get(\"query\") or \"\"))"` | — |
| [SRC-1AE03B9EC3-L002411](../../agents/web_agent.py#L2411) | 2411 | `"                if not target_query:"` | — |
| [SRC-1AE03B9EC3-L002412](../../agents/web_agent.py#L2412) | 2412 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002413](../../agents/web_agent.py#L2413) | 2413 | `"                query_key = re.sub(r\"\\s+\", \" \", target_query).strip().casefold()"` | — |
| [SRC-1AE03B9EC3-L002414](../../agents/web_agent.py#L2414) | 2414 | `"                criterion_batches = ["` | — |
| [SRC-1AE03B9EC3-L002415](../../agents/web_agent.py#L2415) | 2415 | `"                    batch for batch in batches"` | — |
| [SRC-1AE03B9EC3-L002416](../../agents/web_agent.py#L2416) | 2416 | `"                    if re.sub("` | — |
| [SRC-1AE03B9EC3-L002417](../../agents/web_agent.py#L2417) | 2417 | `"                        r\"\\s+\", \" \", str(batch.get(\"query\") or \"\")"` | — |
| [SRC-1AE03B9EC3-L002418](../../agents/web_agent.py#L2418) | 2418 | `"                    ).strip().casefold() == query_key"` | — |
| [SRC-1AE03B9EC3-L002419](../../agents/web_agent.py#L2419) | 2419 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L002420](../../agents/web_agent.py#L2420) | 2420 | `"                criterion_candidates = fuse_ranked_results("` | — |
| [SRC-1AE03B9EC3-L002421](../../agents/web_agent.py#L2421) | 2421 | `"                    criterion_batches, limit=MAX_SEARCH_RESULTS"` | — |
| [SRC-1AE03B9EC3-L002422](../../agents/web_agent.py#L2422) | 2422 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002423](../../agents/web_agent.py#L2423) | 2423 | `"                candidate = None"` | — |
| [SRC-1AE03B9EC3-L002424](../../agents/web_agent.py#L2424) | 2424 | `"                if criterion_candidates:"` | — |
| [SRC-1AE03B9EC3-L002425](../../agents/web_agent.py#L2425) | 2425 | `"                    criterion_ledger = build_requirement_evidence_ledger("` | — |
| [SRC-1AE03B9EC3-L002426](../../agents/web_agent.py#L2426) | 2426 | `"                        [str(requirement.get(\"target\") or \"\")],"` | — |
| [SRC-1AE03B9EC3-L002427](../../agents/web_agent.py#L2427) | 2427 | `"                        criterion_candidates,"` | — |
| [SRC-1AE03B9EC3-L002428](../../agents/web_agent.py#L2428) | 2428 | `"                        [requirement],"` | — |
| [SRC-1AE03B9EC3-L002429](../../agents/web_agent.py#L2429) | 2429 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002430](../../agents/web_agent.py#L2430) | 2430 | `"                    candidate_indexes = ("` | — |
| [SRC-1AE03B9EC3-L002431](../../agents/web_agent.py#L2431) | 2431 | `"                        criterion_ledger[0].get(\"candidate_source_indexes\", [])"` | — |
| [SRC-1AE03B9EC3-L002432](../../agents/web_agent.py#L2432) | 2432 | `"                        if criterion_ledger else []"` | — |
| [SRC-1AE03B9EC3-L002433](../../agents/web_agent.py#L2433) | 2433 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002434](../../agents/web_agent.py#L2434) | 2434 | `"                    if candidate_indexes:"` | — |
| [SRC-1AE03B9EC3-L002435](../../agents/web_agent.py#L2435) | 2435 | `"                        candidate = criterion_candidates[int(candidate_indexes[0]) - 1]"` | — |
| [SRC-1AE03B9EC3-L002436](../../agents/web_agent.py#L2436) | 2436 | `"                if candidate is None:"` | — |
| [SRC-1AE03B9EC3-L002437](../../agents/web_agent.py#L2437) | 2437 | `"                    candidate = next("` | — |
| [SRC-1AE03B9EC3-L002438](../../agents/web_agent.py#L2438) | 2438 | `"                        ("` | — |
| [SRC-1AE03B9EC3-L002439](../../agents/web_agent.py#L2439) | 2439 | `"                            item for item in globally_fused"` | — |
| [SRC-1AE03B9EC3-L002440](../../agents/web_agent.py#L2440) | 2440 | `"                            if query_key in {"` | — |
| [SRC-1AE03B9EC3-L002441](../../agents/web_agent.py#L2441) | 2441 | `"                                re.sub(r\"\\s+\", \" \", str(value)).strip().casefold()"` | — |
| [SRC-1AE03B9EC3-L002442](../../agents/web_agent.py#L2442) | 2442 | `"                                for value in item.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L002443](../../agents/web_agent.py#L2443) | 2443 | `"                            }"` | — |
| [SRC-1AE03B9EC3-L002444](../../agents/web_agent.py#L2444) | 2444 | `"                        ),"` | — |
| [SRC-1AE03B9EC3-L002445](../../agents/web_agent.py#L2445) | 2445 | `"                        criterion_candidates[0] if criterion_candidates else None,"` | — |
| [SRC-1AE03B9EC3-L002446](../../agents/web_agent.py#L2446) | 2446 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002447](../../agents/web_agent.py#L2447) | 2447 | `"                if not candidate:"` | — |
| [SRC-1AE03B9EC3-L002448](../../agents/web_agent.py#L2448) | 2448 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002449](../../agents/web_agent.py#L2449) | 2449 | `"                source_key = _normalized_source_url_key(candidate.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002450](../../agents/web_agent.py#L2450) | 2450 | `"                if not source_key:"` | — |
| [SRC-1AE03B9EC3-L002451](../../agents/web_agent.py#L2451) | 2451 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002452](../../agents/web_agent.py#L2452) | 2452 | `"                selected = ("` | — |
| [SRC-1AE03B9EC3-L002453](../../agents/web_agent.py#L2453) | 2453 | `"                    pinned_by_url.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L002454](../../agents/web_agent.py#L2454) | 2454 | `"                    or globally_fused_by_url.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L002455](../../agents/web_agent.py#L2455) | 2455 | `"                    or candidate"` | — |
| [SRC-1AE03B9EC3-L002456](../../agents/web_agent.py#L2456) | 2456 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002457](../../agents/web_agent.py#L2457) | 2457 | `"                if source_key not in pinned_by_url:"` | — |
| [SRC-1AE03B9EC3-L002458](../../agents/web_agent.py#L2458) | 2458 | `"                    pinned_by_url[source_key] = selected"` | — |
| [SRC-1AE03B9EC3-L002459](../../agents/web_agent.py#L2459) | 2459 | `"                    pinned_sources.append(selected)"` | — |
| [SRC-1AE03B9EC3-L002460](../../agents/web_agent.py#L2460) | 2460 | `"                selected_queries = selected.setdefault(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L002461](../../agents/web_agent.py#L2461) | 2461 | `"                if target_query not in selected_queries:"` | — |
| [SRC-1AE03B9EC3-L002462](../../agents/web_agent.py#L2462) | 2462 | `"                    selected_queries.append(target_query)"` | — |
| [SRC-1AE03B9EC3-L002463](../../agents/web_agent.py#L2463) | 2463 | `"            pinned_keys = set(pinned_by_url)"` | — |
| [SRC-1AE03B9EC3-L002464](../../agents/web_agent.py#L2464) | 2464 | `"            sources = ("` | — |
| [SRC-1AE03B9EC3-L002465](../../agents/web_agent.py#L2465) | 2465 | `"                pinned_sources"` | — |
| [SRC-1AE03B9EC3-L002466](../../agents/web_agent.py#L2466) | 2466 | `"                + ["` | — |
| [SRC-1AE03B9EC3-L002467](../../agents/web_agent.py#L2467) | 2467 | `"                    item for item in globally_fused"` | — |
| [SRC-1AE03B9EC3-L002468](../../agents/web_agent.py#L2468) | 2468 | `"                    if _normalized_source_url_key(item.get(\"url\", \"\")) not in pinned_keys"` | — |
| [SRC-1AE03B9EC3-L002469](../../agents/web_agent.py#L2469) | 2469 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L002470](../../agents/web_agent.py#L2470) | 2470 | `"            )[:MAX_SEARCH_RESULTS]"` | — |
| [SRC-1AE03B9EC3-L002471](../../agents/web_agent.py#L2471) | 2471 | `""` | — |
| [SRC-1AE03B9EC3-L002472](../../agents/web_agent.py#L2472) | 2472 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L002473](../../agents/web_agent.py#L2473) | 2473 | `"            source.setdefault(\"page_fetch_status\", \"not_attempted\")"` | — |
| [SRC-1AE03B9EC3-L002474](../../agents/web_agent.py#L2474) | 2474 | `"        # Fetch page text only for the best few public URLs; do it concurrently with strict bounds."` | — |
| [SRC-1AE03B9EC3-L002475](../../agents/web_agent.py#L2475) | 2475 | `"        fetch_targets = sources[:MAX_FETCHED_PAGES]"` | — |
| [SRC-1AE03B9EC3-L002476](../../agents/web_agent.py#L2476) | 2476 | `"        for source in fetch_targets:"` | — |
| [SRC-1AE03B9EC3-L002477](../../agents/web_agent.py#L2477) | 2477 | `"            source[\"page_fetch_status\"] = \"attempted\""` | — |
| [SRC-1AE03B9EC3-L002478](../../agents/web_agent.py#L2478) | 2478 | `"        fetched_count = 0"` | — |
| [SRC-1AE03B9EC3-L002479](../../agents/web_agent.py#L2479) | 2479 | `"        if fetch_targets:"` | — |
| [SRC-1AE03B9EC3-L002480](../../agents/web_agent.py#L2480) | 2480 | `"            with ThreadPoolExecutor(max_workers=min(4, len(fetch_targets))) as pool:"` | — |
| [SRC-1AE03B9EC3-L002481](../../agents/web_agent.py#L2481) | 2481 | `"                futures = {"` | — |
| [SRC-1AE03B9EC3-L002482](../../agents/web_agent.py#L2482) | 2482 | `"                    pool.submit(self._fetch_page, source[\"url\"]): source"` | — |
| [SRC-1AE03B9EC3-L002483](../../agents/web_agent.py#L2483) | 2483 | `"                    for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L002484](../../agents/web_agent.py#L2484) | 2484 | `"                }"` | — |
| [SRC-1AE03B9EC3-L002485](../../agents/web_agent.py#L2485) | 2485 | `"                for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002486](../../agents/web_agent.py#L2486) | 2486 | `"                    source = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002487](../../agents/web_agent.py#L2487) | 2487 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002488](../../agents/web_agent.py#L2488) | 2488 | `"                        fetch_result = future.result()"` | — |
| [SRC-1AE03B9EC3-L002489](../../agents/web_agent.py#L2489) | 2489 | `"                    except RequestBudgetExceeded as exc:"` | — |
| [SRC-1AE03B9EC3-L002490](../../agents/web_agent.py#L2490) | 2490 | `"                        source[\"page_fetch_status\"] = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L002491](../../agents/web_agent.py#L2491) | 2491 | `"                        source[\"page_fetch_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L002492](../../agents/web_agent.py#L2492) | 2492 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002493](../../agents/web_agent.py#L2493) | 2493 | `"                    except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002494](../../agents/web_agent.py#L2494) | 2494 | `"                        source[\"page_fetch_status\"] = \"fetch_failed\""` | — |
| [SRC-1AE03B9EC3-L002495](../../agents/web_agent.py#L2495) | 2495 | `"                        source[\"page_fetch_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L002496](../../agents/web_agent.py#L2496) | 2496 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002497](../../agents/web_agent.py#L2497) | 2497 | `"                    title, page_text = fetch_result"` | — |
| [SRC-1AE03B9EC3-L002498](../../agents/web_agent.py#L2498) | 2498 | `"                    observed_status = getattr(fetch_result, \"status\", None)"` | — |
| [SRC-1AE03B9EC3-L002499](../../agents/web_agent.py#L2499) | 2499 | `"                    error_class = getattr(fetch_result, \"error_class\", None)"` | — |
| [SRC-1AE03B9EC3-L002500](../../agents/web_agent.py#L2500) | 2500 | `"                    if title:"` | — |
| [SRC-1AE03B9EC3-L002501](../../agents/web_agent.py#L2501) | 2501 | `"                        source[\"title\"] = title"` | — |
| [SRC-1AE03B9EC3-L002502](../../agents/web_agent.py#L2502) | 2502 | `"                    if page_text and page_text.strip():"` | — |
| [SRC-1AE03B9EC3-L002503](../../agents/web_agent.py#L2503) | 2503 | `"                        source[\"page_text\"] = page_text"` | — |
| [SRC-1AE03B9EC3-L002504](../../agents/web_agent.py#L2504) | 2504 | `"                        source[\"snippet\"] = page_text[:1800]"` | — |
| [SRC-1AE03B9EC3-L002505](../../agents/web_agent.py#L2505) | 2505 | `"                        source[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L002506](../../agents/web_agent.py#L2506) | 2506 | `"                        source[\"page_fetch_status\"] = ("` | — |
| [SRC-1AE03B9EC3-L002507](../../agents/web_agent.py#L2507) | 2507 | `"                            observed_status"` | — |
| [SRC-1AE03B9EC3-L002508](../../agents/web_agent.py#L2508) | 2508 | `"                            if observed_status in {\"content_extracted\", \"partial_extraction\"}"` | — |
| [SRC-1AE03B9EC3-L002509](../../agents/web_agent.py#L2509) | 2509 | `"                            else \"partial_extraction\""` | — |
| [SRC-1AE03B9EC3-L002510](../../agents/web_agent.py#L2510) | 2510 | `"                            if len(page_text) >= MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L002511](../../agents/web_agent.py#L2511) | 2511 | `"                            else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L002512](../../agents/web_agent.py#L2512) | 2512 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002513](../../agents/web_agent.py#L2513) | 2513 | `"                        if error_class:"` | — |
| [SRC-1AE03B9EC3-L002514](../../agents/web_agent.py#L2514) | 2514 | `"                            source[\"page_fetch_error_class\"] = str(error_class)[:80]"` | — |
| [SRC-1AE03B9EC3-L002515](../../agents/web_agent.py#L2515) | 2515 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L002516](../../agents/web_agent.py#L2516) | 2516 | `"                            source.pop(\"page_fetch_error_class\", None)"` | — |
| [SRC-1AE03B9EC3-L002517](../../agents/web_agent.py#L2517) | 2517 | `"                        fetched_count += 1"` | — |
| [SRC-1AE03B9EC3-L002518](../../agents/web_agent.py#L2518) | 2518 | `"                        if source[\"page_fetch_status\"] == \"partial_extraction\":"` | — |
| [SRC-1AE03B9EC3-L002519](../../agents/web_agent.py#L2519) | 2519 | `"                            host = urllib.parse.urlparse(source.get(\"url\", \"\")).hostname or \"المصدر\""` | — |
| [SRC-1AE03B9EC3-L002520](../../agents/web_agent.py#L2520) | 2520 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002521](../../agents/web_agent.py#L2521) | 2521 | `"                                f\"استُخرج جزء من نص {host} فقط؛ قد تكون الصفحة أطول من الحد الآمن.\""` | — |
| [SRC-1AE03B9EC3-L002522](../../agents/web_agent.py#L2522) | 2522 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002523](../../agents/web_agent.py#L2523) | 2523 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L002524](../../agents/web_agent.py#L2524) | 2524 | `"                        source[\"page_fetched\"] = False"` | — |
| [SRC-1AE03B9EC3-L002525](../../agents/web_agent.py#L2525) | 2525 | `"                        if observed_status in {"` | — |
| [SRC-1AE03B9EC3-L002526](../../agents/web_agent.py#L2526) | 2526 | `"                            \"rejected_url\", \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L002527](../../agents/web_agent.py#L2527) | 2527 | `"                            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\", \"http_error\","` | — |
| [SRC-1AE03B9EC3-L002528](../../agents/web_agent.py#L2528) | 2528 | `"                            \"unsupported_content_type\", \"page_too_large\", \"network_error\","` | — |
| [SRC-1AE03B9EC3-L002529](../../agents/web_agent.py#L2529) | 2529 | `"                            \"empty_content\", \"no_text_extracted\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002530](../../agents/web_agent.py#L2530) | 2530 | `"                        }:"` | — |
| [SRC-1AE03B9EC3-L002531](../../agents/web_agent.py#L2531) | 2531 | `"                            source[\"page_fetch_status\"] = observed_status"` | — |
| [SRC-1AE03B9EC3-L002532](../../agents/web_agent.py#L2532) | 2532 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L002533](../../agents/web_agent.py#L2533) | 2533 | `"                            source[\"page_fetch_status\"] = \"no_text_extracted\""` | — |
| [SRC-1AE03B9EC3-L002534](../../agents/web_agent.py#L2534) | 2534 | `"                        if error_class:"` | — |
| [SRC-1AE03B9EC3-L002535](../../agents/web_agent.py#L2535) | 2535 | `"                            source[\"page_fetch_error_class\"] = str(error_class)[:80]"` | — |
| [SRC-1AE03B9EC3-L002536](../../agents/web_agent.py#L2536) | 2536 | `"                        host = urllib.parse.urlparse(source.get(\"url\", \"\")).hostname or \"المصدر\""` | — |
| [SRC-1AE03B9EC3-L002537](../../agents/web_agent.py#L2537) | 2537 | `"                        if source[\"page_fetch_status\"] in {\"no_text_extracted\", \"empty_content\"}:"` | — |
| [SRC-1AE03B9EC3-L002538](../../agents/web_agent.py#L2538) | 2538 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002539](../../agents/web_agent.py#L2539) | 2539 | `"                                f\"لم يمكن استخراج نص من {host}؛ جُلبت الصفحة أو جرت محاولة قراءتها لكن قد تكون ديناميكية أو محجوبة.\""` | — |
| [SRC-1AE03B9EC3-L002540](../../agents/web_agent.py#L2540) | 2540 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002541](../../agents/web_agent.py#L2541) | 2541 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L002542](../../agents/web_agent.py#L2542) | 2542 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002543](../../agents/web_agent.py#L2543) | 2543 | `"                                f\"تعذرت قراءة نص {host} بسبب حالة الجلب: {source['page_fetch_status']}.\""` | — |
| [SRC-1AE03B9EC3-L002544](../../agents/web_agent.py#L2544) | 2544 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002545](../../agents/web_agent.py#L2545) | 2545 | `""` | — |
| [SRC-1AE03B9EC3-L002546](../../agents/web_agent.py#L2546) | 2546 | `"        # Reorder on consensus first, and keep clear machine-readable provenance."` | — |
| [SRC-1AE03B9EC3-L002547](../../agents/web_agent.py#L2547) | 2547 | `"        sources.sort(key=lambda source: source.get(\"rank_score\", 0), reverse=True)"` | — |
| [SRC-1AE03B9EC3-L002548](../../agents/web_agent.py#L2548) | 2548 | `"        providers = sorted({"` | — |
| [SRC-1AE03B9EC3-L002549](../../agents/web_agent.py#L2549) | 2549 | `"            provider"` | — |
| [SRC-1AE03B9EC3-L002550](../../agents/web_agent.py#L2550) | 2550 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L002551](../../agents/web_agent.py#L2551) | 2551 | `"            for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L002552](../../agents/web_agent.py#L2552) | 2552 | `"        })"` | — |
| [SRC-1AE03B9EC3-L002553](../../agents/web_agent.py#L2553) | 2553 | `"        platform_counts: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L002554](../../agents/web_agent.py#L2554) | 2554 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L002555](../../agents/web_agent.py#L2555) | 2555 | `"            label = source.get(\"platform\", \"web\")"` | — |
| [SRC-1AE03B9EC3-L002556](../../agents/web_agent.py#L2556) | 2556 | `"            platform_counts[label] = platform_counts.get(label, 0) + 1"` | — |
| [SRC-1AE03B9EC3-L002557](../../agents/web_agent.py#L2557) | 2557 | `"        page_failure_statuses = {"` | — |
| [SRC-1AE03B9EC3-L002558](../../agents/web_agent.py#L2558) | 2558 | `"            \"fetch_failed\", \"no_text_extracted\", \"rejected_url\","` | — |
| [SRC-1AE03B9EC3-L002559](../../agents/web_agent.py#L2559) | 2559 | `"            \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L002560](../../agents/web_agent.py#L2560) | 2560 | `"            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\","` | — |
| [SRC-1AE03B9EC3-L002561](../../agents/web_agent.py#L2561) | 2561 | `"            \"http_error\", \"unsupported_content_type\", \"page_too_large\","` | — |
| [SRC-1AE03B9EC3-L002562](../../agents/web_agent.py#L2562) | 2562 | `"            \"network_error\", \"empty_content\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002563](../../agents/web_agent.py#L2563) | 2563 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002564](../../agents/web_agent.py#L2564) | 2564 | `"        page_status_values = ("` | — |
| [SRC-1AE03B9EC3-L002565](../../agents/web_agent.py#L2565) | 2565 | `"            \"not_attempted\", \"attempted\", \"content_extracted\", \"partial_extraction\","` | — |
| [SRC-1AE03B9EC3-L002566](../../agents/web_agent.py#L2566) | 2566 | `"            \"no_text_extracted\", \"fetch_failed\", \"rejected_url\","` | — |
| [SRC-1AE03B9EC3-L002567](../../agents/web_agent.py#L2567) | 2567 | `"            \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L002568](../../agents/web_agent.py#L2568) | 2568 | `"            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\","` | — |
| [SRC-1AE03B9EC3-L002569](../../agents/web_agent.py#L2569) | 2569 | `"            \"http_error\", \"unsupported_content_type\", \"page_too_large\","` | — |
| [SRC-1AE03B9EC3-L002570](../../agents/web_agent.py#L2570) | 2570 | `"            \"network_error\", \"empty_content\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002571](../../agents/web_agent.py#L2571) | 2571 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002572](../../agents/web_agent.py#L2572) | 2572 | `"        page_fetch_status_counts = {"` | — |
| [SRC-1AE03B9EC3-L002573](../../agents/web_agent.py#L2573) | 2573 | `"            status: sum(source.get(\"page_fetch_status\") == status for source in fetch_targets)"` | — |
| [SRC-1AE03B9EC3-L002574](../../agents/web_agent.py#L2574) | 2574 | `"            for status in page_status_values"` | — |
| [SRC-1AE03B9EC3-L002575](../../agents/web_agent.py#L2575) | 2575 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002576](../../agents/web_agent.py#L2576) | 2576 | `"        provider_diagnostics = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L002577](../../agents/web_agent.py#L2577) | 2577 | `"        provider_candidates_received = sum("` | — |
| [SRC-1AE03B9EC3-L002578](../../agents/web_agent.py#L2578) | 2578 | `"            max(0, int(row.get(\"result_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002579](../../agents/web_agent.py#L2579) | 2579 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L002580](../../agents/web_agent.py#L2580) | 2580 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002581](../../agents/web_agent.py#L2581) | 2581 | `"        provider_candidates_accepted = sum("` | — |
| [SRC-1AE03B9EC3-L002582](../../agents/web_agent.py#L2582) | 2582 | `"            max(0, int(row.get(\"accepted_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002583](../../agents/web_agent.py#L2583) | 2583 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L002584](../../agents/web_agent.py#L2584) | 2584 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002585](../../agents/web_agent.py#L2585) | 2585 | `"        provider_candidates_rejected = sum("` | — |
| [SRC-1AE03B9EC3-L002586](../../agents/web_agent.py#L2586) | 2586 | `"            max(0, int(row.get(\"rejected_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002587](../../agents/web_agent.py#L2587) | 2587 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L002588](../../agents/web_agent.py#L2588) | 2588 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002589](../../agents/web_agent.py#L2589) | 2589 | `"        report = {"` | — |
| [SRC-1AE03B9EC3-L002590](../../agents/web_agent.py#L2590) | 2590 | `"            \"raw_results\": raw_results_count,"` | — |
| [SRC-1AE03B9EC3-L002591](../../agents/web_agent.py#L2591) | 2591 | `"            \"provider_candidates_received\": provider_candidates_received,"` | — |
| [SRC-1AE03B9EC3-L002592](../../agents/web_agent.py#L2592) | 2592 | `"            \"provider_candidates_accepted\": provider_candidates_accepted,"` | — |
| [SRC-1AE03B9EC3-L002593](../../agents/web_agent.py#L2593) | 2593 | `"            \"provider_candidates_rejected\": provider_candidates_rejected,"` | — |
| [SRC-1AE03B9EC3-L002594](../../agents/web_agent.py#L2594) | 2594 | `"            \"unique_urls\": len({"` | — |
| [SRC-1AE03B9EC3-L002595](../../agents/web_agent.py#L2595) | 2595 | `"                self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L002596](../../agents/web_agent.py#L2596) | 2596 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L002597](../../agents/web_agent.py#L2597) | 2597 | `"                if self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L002598](../../agents/web_agent.py#L2598) | 2598 | `"            }),"` | — |
| [SRC-1AE03B9EC3-L002599](../../agents/web_agent.py#L2599) | 2599 | `"            \"pages_content_extracted\": fetched_count,"` | — |
| [SRC-1AE03B9EC3-L002600](../../agents/web_agent.py#L2600) | 2600 | `"            \"pages_partial_extracted\": sum("` | — |
| [SRC-1AE03B9EC3-L002601](../../agents/web_agent.py#L2601) | 2601 | `"                source.get(\"page_fetch_status\") == \"partial_extraction\""` | — |
| [SRC-1AE03B9EC3-L002602](../../agents/web_agent.py#L2602) | 2602 | `"                for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L002603](../../agents/web_agent.py#L2603) | 2603 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L002604](../../agents/web_agent.py#L2604) | 2604 | `"            \"pages_extract_failed\": sum("` | — |
| [SRC-1AE03B9EC3-L002605](../../agents/web_agent.py#L2605) | 2605 | `"                source.get(\"page_fetch_status\") in page_failure_statuses"` | — |
| [SRC-1AE03B9EC3-L002606](../../agents/web_agent.py#L2606) | 2606 | `"                for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L002607](../../agents/web_agent.py#L2607) | 2607 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L002608](../../agents/web_agent.py#L2608) | 2608 | `"            \"page_fetch_status_counts\": page_fetch_status_counts,"` | — |
| [SRC-1AE03B9EC3-L002609](../../agents/web_agent.py#L2609) | 2609 | `"            \"queries_planned\": len(queries),"` | — |
| [SRC-1AE03B9EC3-L002610](../../agents/web_agent.py#L2610) | 2610 | `"            \"queries_attempted\": search_started_queries,"` | — |
| [SRC-1AE03B9EC3-L002611](../../agents/web_agent.py#L2611) | 2611 | `"            \"query_results\": query_counts,"` | — |
| [SRC-1AE03B9EC3-L002612](../../agents/web_agent.py#L2612) | 2612 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L002613](../../agents/web_agent.py#L2613) | 2613 | `"            \"pages_fetched\": fetched_count,"` | — |
| [SRC-1AE03B9EC3-L002614](../../agents/web_agent.py#L2614) | 2614 | `"            \"providers_used\": providers,"` | — |
| [SRC-1AE03B9EC3-L002615](../../agents/web_agent.py#L2615) | 2615 | `"            \"provider_counts\": {"` | — |
| [SRC-1AE03B9EC3-L002616](../../agents/web_agent.py#L2616) | 2616 | `"                provider: sum(provider in source.get(\"providers\", []) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L002617](../../agents/web_agent.py#L2617) | 2617 | `"                for provider in providers"` | — |
| [SRC-1AE03B9EC3-L002618](../../agents/web_agent.py#L2618) | 2618 | `"            },"` | — |
| [SRC-1AE03B9EC3-L002619](../../agents/web_agent.py#L2619) | 2619 | `"            \"platform_counts\": platform_counts,"` | — |
| [SRC-1AE03B9EC3-L002620](../../agents/web_agent.py#L2620) | 2620 | `"            \"social_direct_results\": len(social_results),"` | — |
| [SRC-1AE03B9EC3-L002621](../../agents/web_agent.py#L2621) | 2621 | `"            \"expansion_queries\": expansion_queries,"` | — |
| [SRC-1AE03B9EC3-L002622](../../agents/web_agent.py#L2622) | 2622 | `"            \"evidence_signals\": evidence_signal_report(sources, plan.get(\"freshness\", \"any\")),"` | — |
| [SRC-1AE03B9EC3-L002623](../../agents/web_agent.py#L2623) | 2623 | `"            \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L002624](../../agents/web_agent.py#L2624) | 2624 | `"            \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L002625](../../agents/web_agent.py#L2625) | 2625 | `"            \"provider_diagnostics\": provider_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L002626](../../agents/web_agent.py#L2626) | 2626 | `"            \"connector_summary\": self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L002627](../../agents/web_agent.py#L2627) | 2627 | `"                provider_diagnostics, sources"` | — |
| [SRC-1AE03B9EC3-L002628](../../agents/web_agent.py#L2628) | 2628 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L002629](../../agents/web_agent.py#L2629) | 2629 | `"            \"pages_fetch_attempted\": len(fetch_targets),"` | — |
| [SRC-1AE03B9EC3-L002630](../../agents/web_agent.py#L2630) | 2630 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002631](../../agents/web_agent.py#L2631) | 2631 | `"        return sources, list(dict.fromkeys(warnings)), report"` | — |
| [SRC-1AE03B9EC3-L002632](../../agents/web_agent.py#L2632) | 2632 | `""` | — |
| [SRC-1AE03B9EC3-L002633](../../agents/web_agent.py#L2633) | 2633 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L002634](../../agents/web_agent.py#L2634) | 2634 | `"    def _history_search_query(question: str, history: list[dict[str, str]]) -> str:"` | — |
| [SRC-1AE03B9EC3-L002635](../../agents/web_agent.py#L2635) | 2635 | `"        \"\"\"Backward-compatible wrapper for the shared follow-up resolver.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002636](../../agents/web_agent.py#L2636) | 2636 | `"        return resolve_followup_query(question, history)"` | — |
| [SRC-1AE03B9EC3-L002637](../../agents/web_agent.py#L2637) | 2637 | `""` | — |
| [SRC-1AE03B9EC3-L002638](../../agents/web_agent.py#L2638) | 2638 | `"    def _connector_status_summary(self, diagnostics: list[dict[str, Any]] \| None,"` | — |
| [SRC-1AE03B9EC3-L002639](../../agents/web_agent.py#L2639) | 2639 | `"                                  sources: list[dict[str, Any]] \| None = None) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L002640](../../agents/web_agent.py#L2640) | 2640 | `"        \"\"\"Summarize this request's connector states without exposing credentials.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002641](../../agents/web_agent.py#L2641) | 2641 | `"        optional = {"` | — |
| [SRC-1AE03B9EC3-L002642](../../agents/web_agent.py#L2642) | 2642 | `"            \"deepseek_search_api\": (\"DEEPSEEK_SEARCH_API_KEY\",), \"brave_search_api\": (\"BRAVE_SEARCH_API_KEY\",),"` | — |
| [SRC-1AE03B9EC3-L002643](../../agents/web_agent.py#L2643) | 2643 | `"            \"tavily_search_api\": (\"TAVILY_API_KEY\",), \"reddit_oauth_api\": (\"REDDIT_CLIENT_ID\", \"REDDIT_CLIENT_SECRET\"),"` | — |
| [SRC-1AE03B9EC3-L002644](../../agents/web_agent.py#L2644) | 2644 | `"            \"facebook_pages_api\": (\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"FACEBOOK_PAGE_IDS\"),"` | — |
| [SRC-1AE03B9EC3-L002645](../../agents/web_agent.py#L2645) | 2645 | `"            \"instagram_graph_api\": (\"INSTAGRAM_USER_ID\", \"INSTAGRAM_ACCESS_TOKEN\"),"` | — |
| [SRC-1AE03B9EC3-L002646](../../agents/web_agent.py#L2646) | 2646 | `"            \"x_official_api\": (\"X_BEARER_TOKEN\",), \"youtube_data_api\": (\"YOUTUBE_API_KEY\",),"` | — |
| [SRC-1AE03B9EC3-L002647](../../agents/web_agent.py#L2647) | 2647 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002648](../../agents/web_agent.py#L2648) | 2648 | `"        config: dict[str, tuple[bool, str]] = {"` | — |
| [SRC-1AE03B9EC3-L002649](../../agents/web_agent.py#L2649) | 2649 | `"            \"duckduckgo_html\": (True, \"built_in_no_api_key\"), \"bing_rss\": (True, \"built_in_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L002650](../../agents/web_agent.py#L2650) | 2650 | `"            \"google_news_rss\": (True, \"built_in_conditional_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L002651](../../agents/web_agent.py#L2651) | 2651 | `"            \"reddit_public_rss\": (True, \"built_in_no_api_key\"), \"bluesky_public_search\": (True, \"built_in_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L002652](../../agents/web_agent.py#L2652) | 2652 | `"            \"openrouter_web_search\": (bool(self.openrouter_web_search_enabled),"` | — |
| [SRC-1AE03B9EC3-L002653](../../agents/web_agent.py#L2653) | 2653 | `"                \"enabled\" if self.openrouter_web_search_enabled else \"disabled\"),"` | — |
| [SRC-1AE03B9EC3-L002654](../../agents/web_agent.py#L2654) | 2654 | `"            \"user_supplied_url\": (True, \"request_driven\"),"` | — |
| [SRC-1AE03B9EC3-L002655](../../agents/web_agent.py#L2655) | 2655 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002656](../../agents/web_agent.py#L2656) | 2656 | `"        for name, keys in optional.items():"` | — |
| [SRC-1AE03B9EC3-L002657](../../agents/web_agent.py#L2657) | 2657 | `"            ready = all(bool(os.getenv(key, \"\").strip()) for key in keys)"` | — |
| [SRC-1AE03B9EC3-L002658](../../agents/web_agent.py#L2658) | 2658 | `"            config[name] = (ready, \"configured\" if ready else \"not_configured\")"` | — |
| [SRC-1AE03B9EC3-L002659](../../agents/web_agent.py#L2659) | 2659 | `"        grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002660](../../agents/web_agent.py#L2660) | 2660 | `"        for item in diagnostics or []:"` | — |
| [SRC-1AE03B9EC3-L002661](../../agents/web_agent.py#L2661) | 2661 | `"            if isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L002662](../../agents/web_agent.py#L2662) | 2662 | `"                name = _clean_text(item.get(\"provider\", \"unknown\"), 80) or \"unknown\""` | — |
| [SRC-1AE03B9EC3-L002663](../../agents/web_agent.py#L2663) | 2663 | `"                grouped.setdefault(name, []).append(item)"` | — |
| [SRC-1AE03B9EC3-L002664](../../agents/web_agent.py#L2664) | 2664 | `"        useful: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L002665](../../agents/web_agent.py#L2665) | 2665 | `"        for source in sources or []:"` | — |
| [SRC-1AE03B9EC3-L002666](../../agents/web_agent.py#L2666) | 2666 | `"            if not isinstance(source, dict):"` | — |
| [SRC-1AE03B9EC3-L002667](../../agents/web_agent.py#L2667) | 2667 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002668](../../agents/web_agent.py#L2668) | 2668 | `"            providers = source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L002669](../../agents/web_agent.py#L2669) | 2669 | `"            if isinstance(providers, str):"` | — |
| [SRC-1AE03B9EC3-L002670](../../agents/web_agent.py#L2670) | 2670 | `"                providers = [providers]"` | — |
| [SRC-1AE03B9EC3-L002671](../../agents/web_agent.py#L2671) | 2671 | `"            if not isinstance(providers, list):"` | — |
| [SRC-1AE03B9EC3-L002672](../../agents/web_agent.py#L2672) | 2672 | `"                providers = []"` | — |
| [SRC-1AE03B9EC3-L002673](../../agents/web_agent.py#L2673) | 2673 | `"            if isinstance(source.get(\"provider\"), str):"` | — |
| [SRC-1AE03B9EC3-L002674](../../agents/web_agent.py#L2674) | 2674 | `"                providers = providers + [source[\"provider\"]]"` | — |
| [SRC-1AE03B9EC3-L002675](../../agents/web_agent.py#L2675) | 2675 | `"            for name in {str(value) for value in providers if value}:"` | — |
| [SRC-1AE03B9EC3-L002676](../../agents/web_agent.py#L2676) | 2676 | `"                useful[name] = useful.get(name, 0) + 1"` | — |
| [SRC-1AE03B9EC3-L002677](../../agents/web_agent.py#L2677) | 2677 | `"        priority = {\"ok\": 0, \"no_results\": 1, \"filtered_all\": 2, \"not_attempted\": 3,"` | — |
| [SRC-1AE03B9EC3-L002678](../../agents/web_agent.py#L2678) | 2678 | `"                    \"disabled\": 4, \"not_configured\": 5, \"budget_exhausted\": 6,"` | — |
| [SRC-1AE03B9EC3-L002679](../../agents/web_agent.py#L2679) | 2679 | `"                    \"unknown\": 6, \"rate_limited\": 7, \"unauthorized\": 8, \"http_error\": 9,"` | — |
| [SRC-1AE03B9EC3-L002680](../../agents/web_agent.py#L2680) | 2680 | `"                    \"timeout\": 10, \"failed\": 11, \"error\": 11}"` | — |
| [SRC-1AE03B9EC3-L002681](../../agents/web_agent.py#L2681) | 2681 | `"        confirmed_attempt_statuses = _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES \| {"` | — |
| [SRC-1AE03B9EC3-L002682](../../agents/web_agent.py#L2682) | 2682 | `"            \"http_error\", \"unauthorized\", \"rate_limited\", \"invalid_response\""` | — |
| [SRC-1AE03B9EC3-L002683](../../agents/web_agent.py#L2683) | 2683 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002684](../../agents/web_agent.py#L2684) | 2684 | `"        uncertain_attempt_statuses = {\"timeout\", \"failed\", \"error\", \"unknown\", \"inconclusive\"}"` | — |
| [SRC-1AE03B9EC3-L002685](../../agents/web_agent.py#L2685) | 2685 | `""` | — |
| [SRC-1AE03B9EC3-L002686](../../agents/web_agent.py#L2686) | 2686 | `"        def redact(value: Any) -> str:"` | — |
| [SRC-1AE03B9EC3-L002687](../../agents/web_agent.py#L2687) | 2687 | `"            safe = _clean_text(str(value or \"\"), 180)"` | — |
| [SRC-1AE03B9EC3-L002688](../../agents/web_agent.py#L2688) | 2688 | `"            safe = re.sub(r\"(?i)(bearer\\s+)[A-Za-z0-9._~+/-]+=*\", r\"\\1[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L002689](../../agents/web_agent.py#L2689) | 2689 | `"            safe = re.sub(r\"(?i)\\b(api[_-]?key\|access[_-]?token\|refresh[_-]?token\|token\|secret\|password)\\s*[:=]\\s*[^\\s,;]+\", r\"\\1=[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L002690](../../agents/web_agent.py#L2690) | 2690 | `"            safe = re.sub(r\"(?i)([?&](?:api[_-]?key\|access[_-]?token\|token\|key)=)[^&\\s]+\", r\"\\1[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L002691](../../agents/web_agent.py#L2691) | 2691 | `"            return safe[:180]"` | — |
| [SRC-1AE03B9EC3-L002692](../../agents/web_agent.py#L2692) | 2692 | `""` | — |
| [SRC-1AE03B9EC3-L002693](../../agents/web_agent.py#L2693) | 2693 | `"        names = set(config) \| set(grouped) \| set(useful)"` | — |
| [SRC-1AE03B9EC3-L002694](../../agents/web_agent.py#L2694) | 2694 | `"        connectors = []"` | — |
| [SRC-1AE03B9EC3-L002695](../../agents/web_agent.py#L2695) | 2695 | `"        for name in sorted(names):"` | — |
| [SRC-1AE03B9EC3-L002696](../../agents/web_agent.py#L2696) | 2696 | `"            ready, config_status = config.get(name, (bool(grouped.get(name) or useful.get(name)), \"observed_in_code_path\"))"` | — |
| [SRC-1AE03B9EC3-L002697](../../agents/web_agent.py#L2697) | 2697 | `"            attempts = grouped.get(name, [])"` | — |
| [SRC-1AE03B9EC3-L002698](../../agents/web_agent.py#L2698) | 2698 | `"            statuses = [_clean_text(row.get(\"status\", \"unknown\"), 40).lower() or \"unknown\" for row in attempts]"` | — |
| [SRC-1AE03B9EC3-L002699](../../agents/web_agent.py#L2699) | 2699 | `"            status = max(statuses, key=lambda value: priority.get(value, 6)) if statuses else ("` | — |
| [SRC-1AE03B9EC3-L002700](../../agents/web_agent.py#L2700) | 2700 | `"                \"ok\" if useful.get(name, 0) else \"not_configured\" if not ready else \"not_attempted\")"` | — |
| [SRC-1AE03B9EC3-L002701](../../agents/web_agent.py#L2701) | 2701 | `"            if any(value in confirmed_attempt_statuses for value in statuses) or useful.get(name, 0):"` | — |
| [SRC-1AE03B9EC3-L002702](../../agents/web_agent.py#L2702) | 2702 | `"                attempted: bool \| None = True"` | — |
| [SRC-1AE03B9EC3-L002703](../../agents/web_agent.py#L2703) | 2703 | `"            elif any(value in uncertain_attempt_statuses for value in statuses):"` | — |
| [SRC-1AE03B9EC3-L002704](../../agents/web_agent.py#L2704) | 2704 | `"                attempted = None"` | — |
| [SRC-1AE03B9EC3-L002705](../../agents/web_agent.py#L2705) | 2705 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002706](../../agents/web_agent.py#L2706) | 2706 | `"                attempted = False"` | — |
| [SRC-1AE03B9EC3-L002707](../../agents/web_agent.py#L2707) | 2707 | `"            successful_statuses = set(statuses) & _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L002708](../../agents/web_agent.py#L2708) | 2708 | `"            error_response_statuses = set(statuses) & {\"http_error\", \"unauthorized\", \"rate_limited\"}"` | — |
| [SRC-1AE03B9EC3-L002709](../../agents/web_agent.py#L2709) | 2709 | `"            uncertain_failure_statuses = set(statuses) & {\"timeout\", \"failed\", \"error\", \"unknown\", \"inconclusive\"}"` | — |
| [SRC-1AE03B9EC3-L002710](../../agents/web_agent.py#L2710) | 2710 | `"            failure_observed = bool(error_response_statuses or uncertain_failure_statuses or \"budget_exhausted\" in statuses)"` | — |
| [SRC-1AE03B9EC3-L002711](../../agents/web_agent.py#L2711) | 2711 | `"            available: bool \| None = ("` | — |
| [SRC-1AE03B9EC3-L002712](../../agents/web_agent.py#L2712) | 2712 | `"                True if successful_statuses or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L002713](../../agents/web_agent.py#L2713) | 2713 | `"                else False if error_response_statuses or not ready or \"disabled\" in statuses or \"budget_exhausted\" in statuses"` | — |
| [SRC-1AE03B9EC3-L002714](../../agents/web_agent.py#L2714) | 2714 | `"                else None"` | — |
| [SRC-1AE03B9EC3-L002715](../../agents/web_agent.py#L2715) | 2715 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002716](../../agents/web_agent.py#L2716) | 2716 | `"            verified: bool \| None = ("` | — |
| [SRC-1AE03B9EC3-L002717](../../agents/web_agent.py#L2717) | 2717 | `"                True if successful_statuses or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L002718](../../agents/web_agent.py#L2718) | 2718 | `"                else False if error_response_statuses"` | — |
| [SRC-1AE03B9EC3-L002719](../../agents/web_agent.py#L2719) | 2719 | `"                else None"` | — |
| [SRC-1AE03B9EC3-L002720](../../agents/web_agent.py#L2720) | 2720 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002721](../../agents/web_agent.py#L2721) | 2721 | `"            implementation_status = ("` | — |
| [SRC-1AE03B9EC3-L002722](../../agents/web_agent.py#L2722) | 2722 | `"                \"implemented_in_code\" if name in config"` | — |
| [SRC-1AE03B9EC3-L002723](../../agents/web_agent.py#L2723) | 2723 | `"                else \"observed_runtime_path\" if attempts or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L002724](../../agents/web_agent.py#L2724) | 2724 | `"                else \"unknown\""` | — |
| [SRC-1AE03B9EC3-L002725](../../agents/web_agent.py#L2725) | 2725 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002726](../../agents/web_agent.py#L2726) | 2726 | `"            queries = list(dict.fromkeys(_clean_text(row.get(\"query\", \"\"), 180) for row in attempts if row.get(\"query\")))[:3]"` | — |
| [SRC-1AE03B9EC3-L002727](../../agents/web_agent.py#L2727) | 2727 | `"            errors = list(dict.fromkeys(redact(row.get(\"error\")) for row in attempts if row.get(\"error\")))[:3]"` | — |
| [SRC-1AE03B9EC3-L002728](../../agents/web_agent.py#L2728) | 2728 | `"            result_count = sum(max(0, int(row.get(\"result_count\", 0) or 0)) for row in attempts)"` | — |
| [SRC-1AE03B9EC3-L002729](../../agents/web_agent.py#L2729) | 2729 | `"            accepted_count = sum("` | — |
| [SRC-1AE03B9EC3-L002730](../../agents/web_agent.py#L2730) | 2730 | `"                max(0, int(row.get(\"accepted_count\", row.get(\"result_count\", 0)) or 0))"` | — |
| [SRC-1AE03B9EC3-L002731](../../agents/web_agent.py#L2731) | 2731 | `"                for row in attempts"` | — |
| [SRC-1AE03B9EC3-L002732](../../agents/web_agent.py#L2732) | 2732 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002733](../../agents/web_agent.py#L2733) | 2733 | `"            rejected_count = sum(max(0, int(row.get(\"rejected_count\", 0) or 0)) for row in attempts)"` | — |
| [SRC-1AE03B9EC3-L002734](../../agents/web_agent.py#L2734) | 2734 | `"            rejection_count_totals = {reason: 0 for reason in _PROVIDER_REJECTION_REASONS}"` | — |
| [SRC-1AE03B9EC3-L002735](../../agents/web_agent.py#L2735) | 2735 | `"            rejection_counts_seen = False"` | — |
| [SRC-1AE03B9EC3-L002736](../../agents/web_agent.py#L2736) | 2736 | `"            rejection_counts_complete = True"` | — |
| [SRC-1AE03B9EC3-L002737](../../agents/web_agent.py#L2737) | 2737 | `"            for row in attempts:"` | — |
| [SRC-1AE03B9EC3-L002738](../../agents/web_agent.py#L2738) | 2738 | `"                row_counts = row.get(\"rejection_counts\")"` | — |
| [SRC-1AE03B9EC3-L002739](../../agents/web_agent.py#L2739) | 2739 | `"                if not isinstance(row_counts, dict):"` | — |
| [SRC-1AE03B9EC3-L002740](../../agents/web_agent.py#L2740) | 2740 | `"                    # Legacy/incomplete records with actual rejections prevent claiming"` | — |
| [SRC-1AE03B9EC3-L002741](../../agents/web_agent.py#L2741) | 2741 | `"                    # that an aggregate breakdown covers every rejected candidate."` | — |
| [SRC-1AE03B9EC3-L002742](../../agents/web_agent.py#L2742) | 2742 | `"                    if max(0, int(row.get(\"rejected_count\", 0) or 0)) > 0:"` | — |
| [SRC-1AE03B9EC3-L002743](../../agents/web_agent.py#L2743) | 2743 | `"                        rejection_counts_complete = False"` | — |
| [SRC-1AE03B9EC3-L002744](../../agents/web_agent.py#L2744) | 2744 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002745](../../agents/web_agent.py#L2745) | 2745 | `"                rejection_counts_seen = True"` | — |
| [SRC-1AE03B9EC3-L002746](../../agents/web_agent.py#L2746) | 2746 | `"                for reason in _PROVIDER_REJECTION_REASONS:"` | — |
| [SRC-1AE03B9EC3-L002747](../../agents/web_agent.py#L2747) | 2747 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002748](../../agents/web_agent.py#L2748) | 2748 | `"                        rejection_count_totals[reason] += max(0, int(row_counts.get(reason, 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002749](../../agents/web_agent.py#L2749) | 2749 | `"                    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L002750](../../agents/web_agent.py#L2750) | 2750 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002751](../../agents/web_agent.py#L2751) | 2751 | `"            rejection_counts_observed = ("` | — |
| [SRC-1AE03B9EC3-L002752](../../agents/web_agent.py#L2752) | 2752 | `"                rejection_counts_seen"` | — |
| [SRC-1AE03B9EC3-L002753](../../agents/web_agent.py#L2753) | 2753 | `"                and rejection_counts_complete"` | — |
| [SRC-1AE03B9EC3-L002754](../../agents/web_agent.py#L2754) | 2754 | `"                and sum(rejection_count_totals.values()) == rejected_count"` | — |
| [SRC-1AE03B9EC3-L002755](../../agents/web_agent.py#L2755) | 2755 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002756](../../agents/web_agent.py#L2756) | 2756 | `"            candidate_rejection_observed = \"filtered_all\" in statuses or rejected_count > 0"` | — |
| [SRC-1AE03B9EC3-L002757](../../agents/web_agent.py#L2757) | 2757 | `"            connectors.append({"` | — |
| [SRC-1AE03B9EC3-L002758](../../agents/web_agent.py#L2758) | 2758 | `"                \"name\": name, \"in_codebase\": name in config or bool(attempts),"` | — |
| [SRC-1AE03B9EC3-L002759](../../agents/web_agent.py#L2759) | 2759 | `"                \"implementation_status\": implementation_status,"` | — |
| [SRC-1AE03B9EC3-L002760](../../agents/web_agent.py#L2760) | 2760 | `"                \"configured\": bool(ready), \"configuration_status\": config_status,"` | — |
| [SRC-1AE03B9EC3-L002761](../../agents/web_agent.py#L2761) | 2761 | `"                \"attempted\": attempted, \"available_for_this_request\": available,"` | — |
| [SRC-1AE03B9EC3-L002762](../../agents/web_agent.py#L2762) | 2762 | `"                \"verified_for_this_request\": verified, \"failure_observed\": failure_observed,"` | — |
| [SRC-1AE03B9EC3-L002763](../../agents/web_agent.py#L2763) | 2763 | `"                \"candidate_rejection_observed\": candidate_rejection_observed,"` | — |
| [SRC-1AE03B9EC3-L002764](../../agents/web_agent.py#L2764) | 2764 | `"                \"status\": status, \"observed_statuses\": list(dict.fromkeys(statuses))[:6],"` | — |
| [SRC-1AE03B9EC3-L002765](../../agents/web_agent.py#L2765) | 2765 | `"                \"result_count\": result_count, \"accepted_count\": accepted_count,"` | — |
| [SRC-1AE03B9EC3-L002766](../../agents/web_agent.py#L2766) | 2766 | `"                \"useful_result_count\": useful.get(name, 0),"` | — |
| [SRC-1AE03B9EC3-L002767](../../agents/web_agent.py#L2767) | 2767 | `"                \"rejected_count\": rejected_count,"` | — |
| [SRC-1AE03B9EC3-L002768](../../agents/web_agent.py#L2768) | 2768 | `"                \"rejection_counts_observed\": rejection_counts_observed,"` | — |
| [SRC-1AE03B9EC3-L002769](../../agents/web_agent.py#L2769) | 2769 | `"                \"rejection_counts\": rejection_count_totals if rejection_counts_observed else None,"` | — |
| [SRC-1AE03B9EC3-L002770](../../agents/web_agent.py#L2770) | 2770 | `"                \"queries\": queries, \"errors\": errors,"` | — |
| [SRC-1AE03B9EC3-L002771](../../agents/web_agent.py#L2771) | 2771 | `"            })"` | — |
| [SRC-1AE03B9EC3-L002772](../../agents/web_agent.py#L2772) | 2772 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L002773](../../agents/web_agent.py#L2773) | 2773 | `"            \"scope\": \"this_request_only\","` | — |
| [SRC-1AE03B9EC3-L002774](../../agents/web_agent.py#L2774) | 2774 | `"            \"semantics\": \"result_count is connector-reported rows; useful_result_count counts final fused source records attributed to a connector; neither proves factual accuracy or editorial independence.\","` | — |
| [SRC-1AE03B9EC3-L002775](../../agents/web_agent.py#L2775) | 2775 | `"            \"attempted_count\": sum(bool(item[\"attempted\"]) for item in connectors),"` | — |
| [SRC-1AE03B9EC3-L002776](../../agents/web_agent.py#L2776) | 2776 | `"            \"failed_count\": sum(item[\"status\"] in {\"failed\", \"error\", \"timeout\", \"http_error\", \"unauthorized\", \"rate_limited\"} for item in connectors),"` | — |
| [SRC-1AE03B9EC3-L002777](../../agents/web_agent.py#L2777) | 2777 | `"            \"connectors\": connectors[:24],"` | — |
| [SRC-1AE03B9EC3-L002778](../../agents/web_agent.py#L2778) | 2778 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002779](../../agents/web_agent.py#L2779) | 2779 | `""` | — |
| [SRC-1AE03B9EC3-L002780](../../agents/web_agent.py#L2780) | 2780 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L002781](../../agents/web_agent.py#L2781) | 2781 | `"    def _sanitize_history(history: Any) -> list[dict[str, str]]:"` | — |
| [SRC-1AE03B9EC3-L002782](../../agents/web_agent.py#L2782) | 2782 | `"        if not isinstance(history, list):"` | — |
| [SRC-1AE03B9EC3-L002783](../../agents/web_agent.py#L2783) | 2783 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L002784](../../agents/web_agent.py#L2784) | 2784 | `"        result: list[dict[str, str]] = []"` | — |
| [SRC-1AE03B9EC3-L002785](../../agents/web_agent.py#L2785) | 2785 | `"        for item in history[-MAX_HISTORY_ITEMS:]:"` | — |
| [SRC-1AE03B9EC3-L002786](../../agents/web_agent.py#L2786) | 2786 | `"            if not isinstance(item, dict) or item.get(\"role\") not in {\"user\", \"assistant\"}:"` | — |
| [SRC-1AE03B9EC3-L002787](../../agents/web_agent.py#L2787) | 2787 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002788](../../agents/web_agent.py#L2788) | 2788 | `"            text = _clean_text(item.get(\"content\"), MAX_HISTORY_CHARS)"` | — |
| [SRC-1AE03B9EC3-L002789](../../agents/web_agent.py#L2789) | 2789 | `"            if text:"` | — |
| [SRC-1AE03B9EC3-L002790](../../agents/web_agent.py#L2790) | 2790 | `"                result.append({\"role\": item[\"role\"], \"content\": text})"` | — |
| [SRC-1AE03B9EC3-L002791](../../agents/web_agent.py#L2791) | 2791 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L002792](../../agents/web_agent.py#L2792) | 2792 | `""` | — |
| [SRC-1AE03B9EC3-L002793](../../agents/web_agent.py#L2793) | 2793 | `"    def _record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L002794](../../agents/web_agent.py#L2794) | 2794 | `"        self,"` | — |
| [SRC-1AE03B9EC3-L002795](../../agents/web_agent.py#L2795) | 2795 | `"        requested_model: str,"` | — |
| [SRC-1AE03B9EC3-L002796](../../agents/web_agent.py#L2796) | 2796 | `"        attempted_model: str,"` | — |
| [SRC-1AE03B9EC3-L002797](../../agents/web_agent.py#L2797) | 2797 | `"        status: str,"` | — |
| [SRC-1AE03B9EC3-L002798](../../agents/web_agent.py#L2798) | 2798 | `"        finish_reason: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002799](../../agents/web_agent.py#L2799) | 2799 | `"        error_class: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002800](../../agents/web_agent.py#L2800) | 2800 | `"        request_started: bool = True,"` | — |
| [SRC-1AE03B9EC3-L002801](../../agents/web_agent.py#L2801) | 2801 | `"        remote_response_received: bool \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002802](../../agents/web_agent.py#L2802) | 2802 | `"    ) -> None:"` | — |
| [SRC-1AE03B9EC3-L002803](../../agents/web_agent.py#L2803) | 2803 | `"        \"\"\"Store bounded metadata for each model attempt; never retain prompts or output.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002804](../../agents/web_agent.py#L2804) | 2804 | `"        self._generation_attempt_sequence = getattr(self, \"_generation_attempt_sequence\", 0) + 1"` | — |
| [SRC-1AE03B9EC3-L002805](../../agents/web_agent.py#L2805) | 2805 | `"        record: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L002806](../../agents/web_agent.py#L2806) | 2806 | `"            \"attempt_number\": self._generation_attempt_sequence,"` | — |
| [SRC-1AE03B9EC3-L002807](../../agents/web_agent.py#L2807) | 2807 | `"            \"requested_model\": str(requested_model)[:160],"` | — |
| [SRC-1AE03B9EC3-L002808](../../agents/web_agent.py#L2808) | 2808 | `"            \"attempted_model\": str(attempted_model)[:160],"` | — |
| [SRC-1AE03B9EC3-L002809](../../agents/web_agent.py#L2809) | 2809 | `"            \"fallback_used\": str(attempted_model) != str(requested_model),"` | — |
| [SRC-1AE03B9EC3-L002810](../../agents/web_agent.py#L2810) | 2810 | `"            \"request_started\": bool(request_started),"` | — |
| [SRC-1AE03B9EC3-L002811](../../agents/web_agent.py#L2811) | 2811 | `"            \"status\": str(status)[:48],"` | — |
| [SRC-1AE03B9EC3-L002812](../../agents/web_agent.py#L2812) | 2812 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002813](../../agents/web_agent.py#L2813) | 2813 | `"        if remote_response_received is None and isinstance(finish_reason, str) and finish_reason.strip():"` | — |
| [SRC-1AE03B9EC3-L002814](../../agents/web_agent.py#L2814) | 2814 | `"            # A concrete finish_reason can only be observed after a provider response was received."` | — |
| [SRC-1AE03B9EC3-L002815](../../agents/web_agent.py#L2815) | 2815 | `"            remote_response_received = True"` | — |
| [SRC-1AE03B9EC3-L002816](../../agents/web_agent.py#L2816) | 2816 | `"        if remote_response_received is not None:"` | — |
| [SRC-1AE03B9EC3-L002817](../../agents/web_agent.py#L2817) | 2817 | `"            record[\"remote_response_received\"] = bool(remote_response_received)"` | — |
| [SRC-1AE03B9EC3-L002818](../../agents/web_agent.py#L2818) | 2818 | `"        if isinstance(finish_reason, str) and finish_reason.strip():"` | — |
| [SRC-1AE03B9EC3-L002819](../../agents/web_agent.py#L2819) | 2819 | `"            record[\"finish_reason\"] = finish_reason.strip()[:48]"` | — |
| [SRC-1AE03B9EC3-L002820](../../agents/web_agent.py#L2820) | 2820 | `"        if isinstance(error_class, str) and error_class:"` | — |
| [SRC-1AE03B9EC3-L002821](../../agents/web_agent.py#L2821) | 2821 | `"            record[\"error_class\"] = error_class[:80]"` | — |
| [SRC-1AE03B9EC3-L002822](../../agents/web_agent.py#L2822) | 2822 | `"        self.generation_diagnostics.append(record)"` | — |
| [SRC-1AE03B9EC3-L002823](../../agents/web_agent.py#L2823) | 2823 | `"        self.generation_diagnostics = self.generation_diagnostics[-12:]"` | — |
| [SRC-1AE03B9EC3-L002824](../../agents/web_agent.py#L2824) | 2824 | `""` | — |
| [SRC-1AE03B9EC3-L002825](../../agents/web_agent.py#L2825) | 2825 | `"    def _request_completion("` | — |
| [SRC-1AE03B9EC3-L002826](../../agents/web_agent.py#L2826) | 2826 | `"        self,"` | — |
| [SRC-1AE03B9EC3-L002827](../../agents/web_agent.py#L2827) | 2827 | `"        messages: list[dict[str, str]],"` | — |
| [SRC-1AE03B9EC3-L002828](../../agents/web_agent.py#L2828) | 2828 | `"        max_tokens: int = 1400,"` | — |
| [SRC-1AE03B9EC3-L002829](../../agents/web_agent.py#L2829) | 2829 | `"        temperature: float = 0.2,"` | — |
| [SRC-1AE03B9EC3-L002830](../../agents/web_agent.py#L2830) | 2830 | `"        timeout: int \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002831](../../agents/web_agent.py#L2831) | 2831 | `"        model: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002832](../../agents/web_agent.py#L2832) | 2832 | `"        enable_web_search: bool = False,"` | — |
| [SRC-1AE03B9EC3-L002833](../../agents/web_agent.py#L2833) | 2833 | `"    ) -> str:"` | — |
| [SRC-1AE03B9EC3-L002834](../../agents/web_agent.py#L2834) | 2834 | `"        \"\"\"Call an OpenAI-compatible API with bounded fallback and optional live server search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002835](../../agents/web_agent.py#L2835) | 2835 | `"        requested_model = (model or self.answer_model).strip()"` | — |
| [SRC-1AE03B9EC3-L002836](../../agents/web_agent.py#L2836) | 2836 | `"        if not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L002837](../../agents/web_agent.py#L2837) | 2837 | `"            self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L002838](../../agents/web_agent.py#L2838) | 2838 | `"                requested_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L002839](../../agents/web_agent.py#L2839) | 2839 | `"                attempted_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L002840](../../agents/web_agent.py#L2840) | 2840 | `"                status=\"not_configured\","` | — |
| [SRC-1AE03B9EC3-L002841](../../agents/web_agent.py#L2841) | 2841 | `"                error_class=\"MissingAPIKey\","` | — |
| [SRC-1AE03B9EC3-L002842](../../agents/web_agent.py#L2842) | 2842 | `"                request_started=False,"` | — |
| [SRC-1AE03B9EC3-L002843](../../agents/web_agent.py#L2843) | 2843 | `"                remote_response_received=False,"` | — |
| [SRC-1AE03B9EC3-L002844](../../agents/web_agent.py#L2844) | 2844 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002845](../../agents/web_agent.py#L2845) | 2845 | `"            raise RuntimeError(\"لم يتم ضبط مفتاح نموذج اللغة.\")"` | — |
| [SRC-1AE03B9EC3-L002846](../../agents/web_agent.py#L2846) | 2846 | `""` | — |
| [SRC-1AE03B9EC3-L002847](../../agents/web_agent.py#L2847) | 2847 | `"        model_candidates = [requested_model]"` | — |
| [SRC-1AE03B9EC3-L002848](../../agents/web_agent.py#L2848) | 2848 | `"        if self.fallback_model and self.fallback_model not in model_candidates:"` | — |
| [SRC-1AE03B9EC3-L002849](../../agents/web_agent.py#L2849) | 2849 | `"            model_candidates.append(self.fallback_model)"` | — |
| [SRC-1AE03B9EC3-L002850](../../agents/web_agent.py#L2850) | 2850 | `""` | — |
| [SRC-1AE03B9EC3-L002851](../../agents/web_agent.py#L2851) | 2851 | `"        last_error: RuntimeError \| None = None"` | — |
| [SRC-1AE03B9EC3-L002852](../../agents/web_agent.py#L2852) | 2852 | `"        for candidate_model in model_candidates:"` | — |
| [SRC-1AE03B9EC3-L002853](../../agents/web_agent.py#L2853) | 2853 | `"            budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L002854](../../agents/web_agent.py#L2854) | 2854 | `"            use_web_search = enable_web_search and self.openrouter_web_search_enabled"` | — |
| [SRC-1AE03B9EC3-L002855](../../agents/web_agent.py#L2855) | 2855 | `"            if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L002856](../../agents/web_agent.py#L2856) | 2856 | `"                try:"` | — |
| [SRC-1AE03B9EC3-L002857](../../agents/web_agent.py#L2857) | 2857 | `"                    budget.reserve(\"model_calls\")"` | — |
| [SRC-1AE03B9EC3-L002858](../../agents/web_agent.py#L2858) | 2858 | `"                    request_timeout = budget.timeout_for(timeout or self.timeout)"` | — |
| [SRC-1AE03B9EC3-L002859](../../agents/web_agent.py#L2859) | 2859 | `"                    if use_web_search and budget.remaining_units(\"tool_calls\") < 3:"` | — |
| [SRC-1AE03B9EC3-L002860](../../agents/web_agent.py#L2860) | 2860 | `"                        # The model may still answer, but the optional server-side search"` | — |
| [SRC-1AE03B9EC3-L002861](../../agents/web_agent.py#L2861) | 2861 | `"                        # tool is disabled when its separate budget is unavailable."` | — |
| [SRC-1AE03B9EC3-L002862](../../agents/web_agent.py#L2862) | 2862 | `"                        use_web_search = False"` | — |
| [SRC-1AE03B9EC3-L002863](../../agents/web_agent.py#L2863) | 2863 | `"                    elif use_web_search:"` | — |
| [SRC-1AE03B9EC3-L002864](../../agents/web_agent.py#L2864) | 2864 | `"                        # Reserve the maximum server-side tool calls offered by this request."` | — |
| [SRC-1AE03B9EC3-L002865](../../agents/web_agent.py#L2865) | 2865 | `"                        budget.reserve(\"tool_calls\", amount=3)"` | — |
| [SRC-1AE03B9EC3-L002866](../../agents/web_agent.py#L2866) | 2866 | `"                except RequestBudgetExceeded as exc:"` | — |
| [SRC-1AE03B9EC3-L002867](../../agents/web_agent.py#L2867) | 2867 | `"                    self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L002868](../../agents/web_agent.py#L2868) | 2868 | `"                        requested_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L002869](../../agents/web_agent.py#L2869) | 2869 | `"                        attempted_model=candidate_model,"` | — |
| [SRC-1AE03B9EC3-L002870](../../agents/web_agent.py#L2870) | 2870 | `"                        status=\"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002871](../../agents/web_agent.py#L2871) | 2871 | `"                        error_class=type(exc).__name__,"` | — |
| [SRC-1AE03B9EC3-L002872](../../agents/web_agent.py#L2872) | 2872 | `"                        request_started=False,"` | — |
| [SRC-1AE03B9EC3-L002873](../../agents/web_agent.py#L2873) | 2873 | `"                        remote_response_received=False,"` | — |
| [SRC-1AE03B9EC3-L002874](../../agents/web_agent.py#L2874) | 2874 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002875](../../agents/web_agent.py#L2875) | 2875 | `"                    raise"` | — |
| [SRC-1AE03B9EC3-L002876](../../agents/web_agent.py#L2876) | 2876 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002877](../../agents/web_agent.py#L2877) | 2877 | `"                request_timeout = timeout or self.timeout"` | — |
| [SRC-1AE03B9EC3-L002878](../../agents/web_agent.py#L2878) | 2878 | `"            request_payload: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L002879](../../agents/web_agent.py#L2879) | 2879 | `"                \"model\": candidate_model,"` | — |
| [SRC-1AE03B9EC3-L002880](../../agents/web_agent.py#L2880) | 2880 | `"                \"messages\": messages,"` | — |
| [SRC-1AE03B9EC3-L002881](../../agents/web_agent.py#L2881) | 2881 | `"                \"temperature\": temperature,"` | — |
| [SRC-1AE03B9EC3-L002882](../../agents/web_agent.py#L2882) | 2882 | `"                \"max_tokens\": max(100, min(int(max_tokens), 3000)),"` | — |
| [SRC-1AE03B9EC3-L002883](../../agents/web_agent.py#L2883) | 2883 | `"            }"` | — |
| [SRC-1AE03B9EC3-L002884](../../agents/web_agent.py#L2884) | 2884 | `"            if use_web_search:"` | — |
| [SRC-1AE03B9EC3-L002885](../../agents/web_agent.py#L2885) | 2885 | `"                # OpenRouter executes these searches server-side and returns URL citations."` | — |
| [SRC-1AE03B9EC3-L002886](../../agents/web_agent.py#L2886) | 2886 | `"                # This is opt-in because provider search incurs usage charges."` | — |
| [SRC-1AE03B9EC3-L002887](../../agents/web_agent.py#L2887) | 2887 | `"                request_payload[\"tools\"] = [{"` | — |
| [SRC-1AE03B9EC3-L002888](../../agents/web_agent.py#L2888) | 2888 | `"                    \"type\": \"openrouter:web_search\","` | — |
| [SRC-1AE03B9EC3-L002889](../../agents/web_agent.py#L2889) | 2889 | `"                    \"parameters\": {"` | — |
| [SRC-1AE03B9EC3-L002890](../../agents/web_agent.py#L2890) | 2890 | `"                        \"engine\": \"auto\","` | — |
| [SRC-1AE03B9EC3-L002891](../../agents/web_agent.py#L2891) | 2891 | `"                        \"max_results\": 5,"` | — |
| [SRC-1AE03B9EC3-L002892](../../agents/web_agent.py#L2892) | 2892 | `"                        \"max_total_results\": 12,"` | — |
| [SRC-1AE03B9EC3-L002893](../../agents/web_agent.py#L2893) | 2893 | `"                        \"max_uses\": 3,"` | — |
| [SRC-1AE03B9EC3-L002894](../../agents/web_agent.py#L2894) | 2894 | `"                        \"search_context_size\": \"medium\","` | — |
| [SRC-1AE03B9EC3-L002895](../../agents/web_agent.py#L2895) | 2895 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L002896](../../agents/web_agent.py#L2896) | 2896 | `"                }]"` | — |
| [SRC-1AE03B9EC3-L002897](../../agents/web_agent.py#L2897) | 2897 | `"                request_payload[\"max_tool_calls\"] = 5"` | — |
| [SRC-1AE03B9EC3-L002898](../../agents/web_agent.py#L2898) | 2898 | `"            payload = json.dumps(request_payload, ensure_ascii=False).encode(\"utf-8\")"` | — |
| [SRC-1AE03B9EC3-L002899](../../agents/web_agent.py#L2899) | 2899 | `"            request = urllib.request.Request("` | — |
| [SRC-1AE03B9EC3-L002900](../../agents/web_agent.py#L2900) | 2900 | `"                self.base_url + \"/chat/completions\","` | — |
| [SRC-1AE03B9EC3-L002901](../../agents/web_agent.py#L2901) | 2901 | `"                data=payload,"` | — |
| [SRC-1AE03B9EC3-L002902](../../agents/web_agent.py#L2902) | 2902 | `"                headers={"` | — |
| [SRC-1AE03B9EC3-L002903](../../agents/web_agent.py#L2903) | 2903 | `"                    \"Authorization\": \"Bearer \" + self.api_key,"` | — |
| [SRC-1AE03B9EC3-L002904](../../agents/web_agent.py#L2904) | 2904 | `"                    \"Content-Type\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L002905](../../agents/web_agent.py#L2905) | 2905 | `"                    \"HTTP-Referer\": \"https://github.com/mosabosama2030-oss/omarai\","` | — |
| [SRC-1AE03B9EC3-L002906](../../agents/web_agent.py#L2906) | 2906 | `"                    \"X-Title\": \"Omarai Web Agent\","` | — |
| [SRC-1AE03B9EC3-L002907](../../agents/web_agent.py#L2907) | 2907 | `"                },"` | — |
| [SRC-1AE03B9EC3-L002908](../../agents/web_agent.py#L2908) | 2908 | `"                method=\"POST\","` | — |
| [SRC-1AE03B9EC3-L002909](../../agents/web_agent.py#L2909) | 2909 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002910](../../agents/web_agent.py#L2910) | 2910 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002911](../../agents/web_agent.py#L2911) | 2911 | `"                with urllib.request.urlopen(request, timeout=request_timeout) as response:"` | — |
| [SRC-1AE03B9EC3-L002912](../../agents/web_agent.py#L2912) | 2912 | `"                    data = json.loads(response.read(2_000_000).decode(\"utf-8\"))"` | — |
| [SRC-1AE03B9EC3-L002913](../../agents/web_agent.py#L2913) | 2913 | `"                choice = data[\"choices\"][0]"` | — |
| [SRC-1AE03B9EC3-L002914](../../agents/web_agent.py#L2914) | 2914 | `"                if not isinstance(choice, dict):"` | — |
| [SRC-1AE03B9EC3-L002915](../../agents/web_agent.py#L2915) | 2915 | `"                    raise TypeError(\"invalid completion choice\")"` | — |
| [SRC-1AE03B9EC3-L002916](../../agents/web_agent.py#L2916) | 2916 | `"                finish_reason = choice.get(\"finish_reason\")"` | — |
| [SRC-1AE03B9EC3-L002917](../../agents/web_agent.py#L2917) | 2917 | `"                normalized_finish_reason = ("` | — |
| [SRC-1AE03B9EC3-L002918](../../agents/web_agent.py#L2918) | 2918 | `"                    finish_reason.strip().lower()"` | — |
| [SRC-1AE03B9EC3-L002919](../../agents/web_agent.py#L2919) | 2919 | `"                    if isinstance(finish_reason, str)"` | — |
| [SRC-1AE03B9EC3-L002920](../../agents/web_agent.py#L2920) | 2920 | `"                    else \"\""` | — |
| [SRC-1AE03B9EC3-L002921](../../agents/web_agent.py#L2921) | 2921 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002922](../../agents/web_agent.py#L2922) | 2922 | `"                # This application consumes a final text completion from an"` | — |
| [SRC-1AE03B9EC3-L002923](../../agents/web_agent.py#L2923) | 2923 | `"                # OpenAI-compatible /chat/completions endpoint. Fail closed when the"` | — |
| [SRC-1AE03B9EC3-L002924](../../agents/web_agent.py#L2924) | 2924 | `"                # provider does not explicitly report the standardized \"stop\" reason."` | — |
| [SRC-1AE03B9EC3-L002925](../../agents/web_agent.py#L2925) | 2925 | `"                if normalized_finish_reason != \"stop\":"` | — |
| [SRC-1AE03B9EC3-L002926](../../agents/web_agent.py#L2926) | 2926 | `"                    if normalized_finish_reason in {\"length\", \"max_tokens\"}:"` | — |
| [SRC-1AE03B9EC3-L002927](../../agents/web_agent.py#L2927) | 2927 | `"                        diagnostic_status = \"truncated\""` | — |
| [SRC-1AE03B9EC3-L002928](../../agents/web_agent.py#L2928) | 2928 | `"                        last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L002929](../../agents/web_agent.py#L2929) | 2929 | `"                            \"أعاد نموذج اللغة إجابة مبتورة بسبب الوصول إلى حد الرموز؛ \""` | — |
| [SRC-1AE03B9EC3-L002930](../../agents/web_agent.py#L2930) | 2930 | `"                            \"لم تُقبل كإجابة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L002931](../../agents/web_agent.py#L2931) | 2931 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002932](../../agents/web_agent.py#L2932) | 2932 | `"                    elif not normalized_finish_reason:"` | — |
| [SRC-1AE03B9EC3-L002933](../../agents/web_agent.py#L2933) | 2933 | `"                        diagnostic_status = \"finish_reason_missing\""` | — |
| [SRC-1AE03B9EC3-L002934](../../agents/web_agent.py#L2934) | 2934 | `"                        last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L002935](../../agents/web_agent.py#L2935) | 2935 | `"                            \"لم تقدم خدمة النموذج سبب انتهاء واضحًا؛ لم تُقبل الإجابة \""` | — |
| [SRC-1AE03B9EC3-L002936](../../agents/web_agent.py#L2936) | 2936 | `"                            \"كإجابة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L002937](../../agents/web_agent.py#L2937) | 2937 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002938](../../agents/web_agent.py#L2938) | 2938 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L002939](../../agents/web_agent.py#L2939) | 2939 | `"                        diagnostic_status = \"finish_reason_not_accepted\""` | — |
| [SRC-1AE03B9EC3-L002940](../../agents/web_agent.py#L2940) | 2940 | `"                        last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L002941](../../agents/web_agent.py#L2941) | 2941 | `"                            \"لم تُكمل خدمة النموذج إجابة نصية نهائية مقبولة \""` | — |
| [SRC-1AE03B9EC3-L002942](../../agents/web_agent.py#L2942) | 2942 | `"                            \"(حالة الإنهاء: \" + normalized_finish_reason[:40] + \").\""` | — |
| [SRC-1AE03B9EC3-L002943](../../agents/web_agent.py#L2943) | 2943 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002944](../../agents/web_agent.py#L2944) | 2944 | `"                    self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L002945](../../agents/web_agent.py#L2945) | 2945 | `"                        requested_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L002946](../../agents/web_agent.py#L2946) | 2946 | `"                        attempted_model=candidate_model,"` | — |
| [SRC-1AE03B9EC3-L002947](../../agents/web_agent.py#L2947) | 2947 | `"                        status=diagnostic_status,"` | — |
| [SRC-1AE03B9EC3-L002948](../../agents/web_agent.py#L2948) | 2948 | `"                        finish_reason=normalized_finish_reason or None,"` | — |
| [SRC-1AE03B9EC3-L002949](../../agents/web_agent.py#L2949) | 2949 | `"                        request_started=True,"` | — |
| [SRC-1AE03B9EC3-L002950](../../agents/web_agent.py#L2950) | 2950 | `"                        remote_response_received=True,"` | — |
| [SRC-1AE03B9EC3-L002951](../../agents/web_agent.py#L2951) | 2951 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002952](../../agents/web_agent.py#L2952) | 2952 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002953](../../agents/web_agent.py#L2953) | 2953 | `"                message = choice[\"message\"]"` | — |
| [SRC-1AE03B9EC3-L002954](../../agents/web_agent.py#L2954) | 2954 | `"                answer = message[\"content\"]"` | — |
| [SRC-1AE03B9EC3-L002955](../../agents/web_agent.py#L2955) | 2955 | `"                if use_web_search:"` | — |
| [SRC-1AE03B9EC3-L002956](../../agents/web_agent.py#L2956) | 2956 | `"                    for annotation in message.get(\"annotations\", []):"` | — |
| [SRC-1AE03B9EC3-L002957](../../agents/web_agent.py#L2957) | 2957 | `"                        if not isinstance(annotation, dict) or annotation.get(\"type\") != \"url_citation\":"` | — |
| [SRC-1AE03B9EC3-L002958](../../agents/web_agent.py#L2958) | 2958 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002959](../../agents/web_agent.py#L2959) | 2959 | `"                        citation = annotation.get(\"url_citation\", annotation)"` | — |
| [SRC-1AE03B9EC3-L002960](../../agents/web_agent.py#L2960) | 2960 | `"                        if not isinstance(citation, dict):"` | — |
| [SRC-1AE03B9EC3-L002961](../../agents/web_agent.py#L2961) | 2961 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002962](../../agents/web_agent.py#L2962) | 2962 | `"                        url = _public_http_url(citation.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002963](../../agents/web_agent.py#L2963) | 2963 | `"                        if not url or any(item.get(\"url\") == url for item in self.server_search_sources):"` | — |
| [SRC-1AE03B9EC3-L002964](../../agents/web_agent.py#L2964) | 2964 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002965](../../agents/web_agent.py#L2965) | 2965 | `"                        parsed_url = urllib.parse.urlparse(url)"` | — |
| [SRC-1AE03B9EC3-L002966](../../agents/web_agent.py#L2966) | 2966 | `"                        excerpt = _clean_text(citation.get(\"content\", \"\"), 1800)"` | — |
| [SRC-1AE03B9EC3-L002967](../../agents/web_agent.py#L2967) | 2967 | `"                        self.server_search_sources.append({"` | — |
| [SRC-1AE03B9EC3-L002968](../../agents/web_agent.py#L2968) | 2968 | `"                            \"title\": _clean_text(citation.get(\"title\", \"\"), 300) or parsed_url.netloc,"` | — |
| [SRC-1AE03B9EC3-L002969](../../agents/web_agent.py#L2969) | 2969 | `"                            \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L002970](../../agents/web_agent.py#L2970) | 2970 | `"                            \"snippet\": excerpt,"` | — |
| [SRC-1AE03B9EC3-L002971](../../agents/web_agent.py#L2971) | 2971 | `"                            \"page_text\": excerpt,"` | — |
| [SRC-1AE03B9EC3-L002972](../../agents/web_agent.py#L2972) | 2972 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002973](../../agents/web_agent.py#L2973) | 2973 | `"                            \"provider\": \"openrouter_web_search\","` | — |
| [SRC-1AE03B9EC3-L002974](../../agents/web_agent.py#L2974) | 2974 | `"                            \"providers\": [\"openrouter_web_search\"],"` | — |
| [SRC-1AE03B9EC3-L002975](../../agents/web_agent.py#L2975) | 2975 | `"                            \"queries\": [],"` | — |
| [SRC-1AE03B9EC3-L002976](../../agents/web_agent.py#L2976) | 2976 | `"                            \"domain\": parsed_url.netloc.lower(),"` | — |
| [SRC-1AE03B9EC3-L002977](../../agents/web_agent.py#L2977) | 2977 | `"                            \"source_class\": \"general\","` | — |
| [SRC-1AE03B9EC3-L002978](../../agents/web_agent.py#L2978) | 2978 | `"                            \"platform\": \"web\","` | — |
| [SRC-1AE03B9EC3-L002979](../../agents/web_agent.py#L2979) | 2979 | `"                            \"published_at\": \"\","` | — |
| [SRC-1AE03B9EC3-L002980](../../agents/web_agent.py#L2980) | 2980 | `"                            \"rank_score\": 0.0,"` | — |
| [SRC-1AE03B9EC3-L002981](../../agents/web_agent.py#L2981) | 2981 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L002982](../../agents/web_agent.py#L2982) | 2982 | `"                if isinstance(answer, list):"` | — |
| [SRC-1AE03B9EC3-L002983](../../agents/web_agent.py#L2983) | 2983 | `"                    answer = \"\".join("` | — |
| [SRC-1AE03B9EC3-L002984](../../agents/web_agent.py#L2984) | 2984 | `"                        item.get(\"text\", \"\") for item in answer if isinstance(item, dict)"` | — |
| [SRC-1AE03B9EC3-L002985](../../agents/web_agent.py#L2985) | 2985 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002986](../../agents/web_agent.py#L2986) | 2986 | `"                if not isinstance(answer, str) or not answer.strip():"` | — |
| [SRC-1AE03B9EC3-L002987](../../agents/web_agent.py#L2987) | 2987 | `"                    raise ValueError(\"empty model response\")"` | — |
| [SRC-1AE03B9EC3-L002988](../../agents/web_agent.py#L2988) | 2988 | `"                self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L002989](../../agents/web_agent.py#L2989) | 2989 | `"                    requested_model=requested_model,"` | — |
| [SRC-1AE03B9EC3-L002990](../../agents/web_agent.py#L2990) | 2990 | `"                    attempted_model=candidate_model,"` | — |
| [SRC-1AE03B9EC3-L002991](../../agents/web_agent.py#L2991) | 2991 | `"                    status=\"accepted\","` | — |
| [SRC-1AE03B9EC3-L002992](../../agents/web_agent.py#L2992) | 2992 | `"                    finish_reason=normalized_finish_reason,"` | — |
| [SRC-1AE03B9EC3-L002993](../../agents/web_agent.py#L2993) | 2993 | `"                    request_started=True,"` | — |
| [SRC-1AE03B9EC3-L002994](../../agents/web_agent.py#L2994) | 2994 | `"                    remote_response_received=True,"` | — |
| [SRC-1AE03B9EC3-L002995](../../agents/web_agent.py#L2995) | 2995 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002996](../../agents/web_agent.py#L2996) | 2996 | `"                self.model_usage.append({"` | — |
| [SRC-1AE03B9EC3-L002997](../../agents/web_agent.py#L2997) | 2997 | `"                    \"requested_model\": requested_model,"` | — |
| [SRC-1AE03B9EC3-L002998](../../agents/web_agent.py#L2998) | 2998 | `"                    \"used_model\": candidate_model,"` | — |
| [SRC-1AE03B9EC3-L002999](../../agents/web_agent.py#L2999) | 2999 | `"                    \"fallback_used\": \"true\" if candidate_model != requested_model else \"false\","` | — |
| [SRC-1AE03B9EC3-L003000](../../agents/web_agent.py#L3000) | 3000 | `"                })"` | — |
| [SRC-1AE03B9EC3-L003001](../../agents/web_agent.py#L3001) | 3001 | `"                return answer.strip()"` | — |
| [SRC-1AE03B9EC3-L003002](../../agents/web_agent.py#L3002) | 3002 | `"            except urllib.error.HTTPError as exc:"` | — |
| [SRC-1AE03B9EC3-L003003](../../agents/web_agent.py#L3003) | 3003 | `"                # Never echo provider response bodies: they may contain private diagnostics."` | — |
| [SRC-1AE03B9EC3-L003004](../../agents/web_agent.py#L3004) | 3004 | `"                self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L003005](../../agents/web_agent.py#L3005) | 3005 | `"                    requested_model, candidate_model, \"provider_http_error\","` | — |
| [SRC-1AE03B9EC3-L003006](../../agents/web_agent.py#L3006) | 3006 | `"                    error_class=\"HTTPError\", request_started=True,"` | — |
| [SRC-1AE03B9EC3-L003007](../../agents/web_agent.py#L3007) | 3007 | `"                    remote_response_received=True,"` | — |
| [SRC-1AE03B9EC3-L003008](../../agents/web_agent.py#L3008) | 3008 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003009](../../agents/web_agent.py#L3009) | 3009 | `"                last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L003010](../../agents/web_agent.py#L3010) | 3010 | `"                    f\"خدمة نموذج اللغة رفضت الطلب (HTTP {exc.code}) على النموذج المحدد.\""` | — |
| [SRC-1AE03B9EC3-L003011](../../agents/web_agent.py#L3011) | 3011 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003012](../../agents/web_agent.py#L3012) | 3012 | `"            except (urllib.error.URLError, TimeoutError, OSError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003013](../../agents/web_agent.py#L3013) | 3013 | `"                self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L003014](../../agents/web_agent.py#L3014) | 3014 | `"                    requested_model, candidate_model, \"connection_error\","` | — |
| [SRC-1AE03B9EC3-L003015](../../agents/web_agent.py#L3015) | 3015 | `"                    error_class=type(exc).__name__, request_started=True,"` | — |
| [SRC-1AE03B9EC3-L003016](../../agents/web_agent.py#L3016) | 3016 | `"                    remote_response_received=None,"` | — |
| [SRC-1AE03B9EC3-L003017](../../agents/web_agent.py#L3017) | 3017 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003018](../../agents/web_agent.py#L3018) | 3018 | `"                last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L003019](../../agents/web_agent.py#L3019) | 3019 | `"                    \"تعذر الاتصال بخدمة نموذج اللغة؛ جرت محاولة استخدام النموذج الاحتياطي.\""` | — |
| [SRC-1AE03B9EC3-L003020](../../agents/web_agent.py#L3020) | 3020 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003021](../../agents/web_agent.py#L3021) | 3021 | `"            except (KeyError, IndexError, TypeError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003022](../../agents/web_agent.py#L3022) | 3022 | `"                self._record_generation_diagnostic("` | — |
| [SRC-1AE03B9EC3-L003023](../../agents/web_agent.py#L3023) | 3023 | `"                    requested_model, candidate_model, \"invalid_response\","` | — |
| [SRC-1AE03B9EC3-L003024](../../agents/web_agent.py#L3024) | 3024 | `"                    error_class=type(exc).__name__, request_started=True,"` | — |
| [SRC-1AE03B9EC3-L003025](../../agents/web_agent.py#L3025) | 3025 | `"                    remote_response_received=True,"` | — |
| [SRC-1AE03B9EC3-L003026](../../agents/web_agent.py#L3026) | 3026 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003027](../../agents/web_agent.py#L3027) | 3027 | `"                last_error = RuntimeError("` | — |
| [SRC-1AE03B9EC3-L003028](../../agents/web_agent.py#L3028) | 3028 | `"                    \"خدمة نموذج اللغة أعادت استجابة غير صالحة؛ جرت محاولة استخدام النموذج الاحتياطي.\""` | — |
| [SRC-1AE03B9EC3-L003029](../../agents/web_agent.py#L3029) | 3029 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003030](../../agents/web_agent.py#L3030) | 3030 | `""` | — |
| [SRC-1AE03B9EC3-L003031](../../agents/web_agent.py#L3031) | 3031 | `"        raise last_error or RuntimeError(\"تعذر توليد إجابة من النموذج اللغوي.\")"` | — |
| [SRC-1AE03B9EC3-L003032](../../agents/web_agent.py#L3032) | 3032 | `""` | — |
| [SRC-1AE03B9EC3-L003033](../../agents/web_agent.py#L3033) | 3033 | `"    def _plan_search("` | — |
| [SRC-1AE03B9EC3-L003034](../../agents/web_agent.py#L3034) | 3034 | `"        self, question: str, history: list[dict[str, str]]"` | — |
| [SRC-1AE03B9EC3-L003035](../../agents/web_agent.py#L3035) | 3035 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L003036](../../agents/web_agent.py#L3036) | 3036 | `"        \"\"\"Ask the language model how to search, then validate its proposal deterministically.\"\"\""` | — |
| [SRC-1AE03B9EC3-L003037](../../agents/web_agent.py#L3037) | 3037 | `"        fallback = fallback_plan(question, history)"` | — |
| [SRC-1AE03B9EC3-L003038](../../agents/web_agent.py#L3038) | 3038 | `"        # Do not ask the planner to invent a generic query when there is no topic."` | — |
| [SRC-1AE03B9EC3-L003039](../../agents/web_agent.py#L3039) | 3039 | `"        # Explicit URLs remain usable through the direct-page-fetch path."` | — |
| [SRC-1AE03B9EC3-L003040](../../agents/web_agent.py#L3040) | 3040 | `"        if not fallback.get(\"queries\"):"` | — |
| [SRC-1AE03B9EC3-L003041](../../agents/web_agent.py#L3041) | 3041 | `"            return fallback"` | — |
| [SRC-1AE03B9EC3-L003042](../../agents/web_agent.py#L3042) | 3042 | `"        search_question = self._history_search_query(question, history)"` | — |
| [SRC-1AE03B9EC3-L003043](../../agents/web_agent.py#L3043) | 3043 | `"        if search_question != question:"` | — |
| [SRC-1AE03B9EC3-L003044](../../agents/web_agent.py#L3044) | 3044 | `"            compact_context_query = compact_search_query(search_question)"` | — |
