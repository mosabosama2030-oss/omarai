# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **012**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L002289 إلى SRC-1AE03B9EC3-L003088
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L002289](../../agents/web_agent.py#L2289) | 2289 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002290](../../agents/web_agent.py#L2290) | 2290 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L002291](../../agents/web_agent.py#L2291) | 2291 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L002292](../../agents/web_agent.py#L2292) | 2292 | `"                    authors = {"` | — |
| [SRC-1AE03B9EC3-L002293](../../agents/web_agent.py#L2293) | 2293 | `"                        user.get(\"id\"): user"` | — |
| [SRC-1AE03B9EC3-L002294](../../agents/web_agent.py#L2294) | 2294 | `"                        for user in data.get(\"includes\", {}).get(\"users\", [])"` | — |
| [SRC-1AE03B9EC3-L002295](../../agents/web_agent.py#L2295) | 2295 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L002296](../../agents/web_agent.py#L2296) | 2296 | `"                    for item in data.get(\"data\", []):"` | — |
| [SRC-1AE03B9EC3-L002297](../../agents/web_agent.py#L2297) | 2297 | `"                        author = authors.get(item.get(\"author_id\"), {})"` | — |
| [SRC-1AE03B9EC3-L002298](../../agents/web_agent.py#L2298) | 2298 | `"                        username = author.get(\"username\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002299](../../agents/web_agent.py#L2299) | 2299 | `"                        post_id = item.get(\"id\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002300](../../agents/web_agent.py#L2300) | 2300 | `"                        if not username or not post_id:"` | — |
| [SRC-1AE03B9EC3-L002301](../../agents/web_agent.py#L2301) | 2301 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002302](../../agents/web_agent.py#L2302) | 2302 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L002303](../../agents/web_agent.py#L2303) | 2303 | `"                            \"title\": _clean_text(author.get(\"name\") or username, 300),"` | — |
| [SRC-1AE03B9EC3-L002304](../../agents/web_agent.py#L2304) | 2304 | `"                            \"url\": f\"https://x.com/{username}/status/{post_id}\","` | — |
| [SRC-1AE03B9EC3-L002305](../../agents/web_agent.py#L2305) | 2305 | `"                            \"snippet\": _clean_text(item.get(\"text\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L002306](../../agents/web_agent.py#L2306) | 2306 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002307](../../agents/web_agent.py#L2307) | 2307 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002308](../../agents/web_agent.py#L2308) | 2308 | `"                            \"provider\": \"x_official_api\","` | — |
| [SRC-1AE03B9EC3-L002309](../../agents/web_agent.py#L2309) | 2309 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002310](../../agents/web_agent.py#L2310) | 2310 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L002311](../../agents/web_agent.py#L2311) | 2311 | `"                                if row.get(\"provider\") == \"x_official_api\""` | — |
| [SRC-1AE03B9EC3-L002312](../../agents/web_agent.py#L2312) | 2312 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002313](../../agents/web_agent.py#L2313) | 2313 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002314](../../agents/web_agent.py#L2314) | 2314 | `"                            \"published_at\": _clean_text(item.get(\"created_at\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002315](../../agents/web_agent.py#L2315) | 2315 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L002316](../../agents/web_agent.py#L2316) | 2316 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002317](../../agents/web_agent.py#L2317) | 2317 | `"                    warnings.append(f\"X API unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L002318](../../agents/web_agent.py#L2318) | 2318 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002319](../../agents/web_agent.py#L2319) | 2319 | `"                warnings.append(\"X API unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L002320](../../agents/web_agent.py#L2320) | 2320 | `"        elif \"x\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002321](../../agents/web_agent.py#L2321) | 2321 | `"            warnings.append(\"X direct API is not configured; indexed public X pages are still searched.\")"` | — |
| [SRC-1AE03B9EC3-L002322](../../agents/web_agent.py#L2322) | 2322 | `""` | — |
| [SRC-1AE03B9EC3-L002323](../../agents/web_agent.py#L2323) | 2323 | `"        if \"youtube\" in platforms and os.getenv(\"YOUTUBE_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L002324](../../agents/web_agent.py#L2324) | 2324 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002325](../../agents/web_agent.py#L2325) | 2325 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002326](../../agents/web_agent.py#L2326) | 2326 | `"                response = _bounded_http_request(\"GET\", "` | — |
| [SRC-1AE03B9EC3-L002327](../../agents/web_agent.py#L2327) | 2327 | `"                    \"https://www.googleapis.com/youtube/v3/search\","` | — |
| [SRC-1AE03B9EC3-L002328](../../agents/web_agent.py#L2328) | 2328 | `"                    params={"` | — |
| [SRC-1AE03B9EC3-L002329](../../agents/web_agent.py#L2329) | 2329 | `"                        \"part\": \"snippet\","` | — |
| [SRC-1AE03B9EC3-L002330](../../agents/web_agent.py#L2330) | 2330 | `"                        \"q\": query,"` | — |
| [SRC-1AE03B9EC3-L002331](../../agents/web_agent.py#L2331) | 2331 | `"                        \"type\": \"video\","` | — |
| [SRC-1AE03B9EC3-L002332](../../agents/web_agent.py#L2332) | 2332 | `"                        \"maxResults\": 8,"` | — |
| [SRC-1AE03B9EC3-L002333](../../agents/web_agent.py#L2333) | 2333 | `"                        \"key\": os.getenv(\"YOUTUBE_API_KEY\", \"\").strip(),"` | — |
| [SRC-1AE03B9EC3-L002334](../../agents/web_agent.py#L2334) | 2334 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L002335](../../agents/web_agent.py#L2335) | 2335 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002336](../../agents/web_agent.py#L2336) | 2336 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002337](../../agents/web_agent.py#L2337) | 2337 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002338](../../agents/web_agent.py#L2338) | 2338 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002339](../../agents/web_agent.py#L2339) | 2339 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L002340](../../agents/web_agent.py#L2340) | 2340 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L002341](../../agents/web_agent.py#L2341) | 2341 | `"                    for item in data.get(\"items\", []):"` | — |
| [SRC-1AE03B9EC3-L002342](../../agents/web_agent.py#L2342) | 2342 | `"                        video_id = item.get(\"id\", {}).get(\"videoId\")"` | — |
| [SRC-1AE03B9EC3-L002343](../../agents/web_agent.py#L2343) | 2343 | `"                        snippet = item.get(\"snippet\", {})"` | — |
| [SRC-1AE03B9EC3-L002344](../../agents/web_agent.py#L2344) | 2344 | `"                        if not video_id:"` | — |
| [SRC-1AE03B9EC3-L002345](../../agents/web_agent.py#L2345) | 2345 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002346](../../agents/web_agent.py#L2346) | 2346 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L002347](../../agents/web_agent.py#L2347) | 2347 | `"                            \"title\": _clean_text(snippet.get(\"title\") or \"\", 300),"` | — |
| [SRC-1AE03B9EC3-L002348](../../agents/web_agent.py#L2348) | 2348 | `"                            \"url\": f\"https://www.youtube.com/watch?v={video_id}\","` | — |
| [SRC-1AE03B9EC3-L002349](../../agents/web_agent.py#L2349) | 2349 | `"                            \"snippet\": _clean_text(snippet.get(\"description\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L002350](../../agents/web_agent.py#L2350) | 2350 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002351](../../agents/web_agent.py#L2351) | 2351 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002352](../../agents/web_agent.py#L2352) | 2352 | `"                            \"provider\": \"youtube_data_api\","` | — |
| [SRC-1AE03B9EC3-L002353](../../agents/web_agent.py#L2353) | 2353 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002354](../../agents/web_agent.py#L2354) | 2354 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L002355](../../agents/web_agent.py#L2355) | 2355 | `"                                if row.get(\"provider\") == \"youtube_data_api\""` | — |
| [SRC-1AE03B9EC3-L002356](../../agents/web_agent.py#L2356) | 2356 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002357](../../agents/web_agent.py#L2357) | 2357 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002358](../../agents/web_agent.py#L2358) | 2358 | `"                            \"published_at\": _clean_text(snippet.get(\"publishedAt\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002359](../../agents/web_agent.py#L2359) | 2359 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L002360](../../agents/web_agent.py#L2360) | 2360 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002361](../../agents/web_agent.py#L2361) | 2361 | `"                    warnings.append(f\"YouTube Data API unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L002362](../../agents/web_agent.py#L2362) | 2362 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002363](../../agents/web_agent.py#L2363) | 2363 | `"                warnings.append(\"YouTube Data API unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L002364](../../agents/web_agent.py#L2364) | 2364 | `"        elif \"youtube\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002365](../../agents/web_agent.py#L2365) | 2365 | `"            warnings.append(\"YouTube direct API is not configured; indexed public YouTube pages are still searched.\")"` | — |
| [SRC-1AE03B9EC3-L002366](../../agents/web_agent.py#L2366) | 2366 | `""` | — |
| [SRC-1AE03B9EC3-L002367](../../agents/web_agent.py#L2367) | 2367 | `"        return results, warnings"` | — |
| [SRC-1AE03B9EC3-L002368](../../agents/web_agent.py#L2368) | 2368 | `""` | — |
| [SRC-1AE03B9EC3-L002369](../../agents/web_agent.py#L2369) | 2369 | `"    def _fetch_page(self, url: str) -> tuple[str, str]:"` | — |
| [SRC-1AE03B9EC3-L002370](../../agents/web_agent.py#L2370) | 2370 | `"        \"\"\"Fetch a public page with bounded redirects and an inspectable extraction outcome.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002371](../../agents/web_agent.py#L2371) | 2371 | `"        def result("` | — |
| [SRC-1AE03B9EC3-L002372](../../agents/web_agent.py#L2372) | 2372 | `"            title: str = \"\","` | — |
| [SRC-1AE03B9EC3-L002373](../../agents/web_agent.py#L2373) | 2373 | `"            page_text: str = \"\","` | — |
| [SRC-1AE03B9EC3-L002374](../../agents/web_agent.py#L2374) | 2374 | `"            status: str = \"unknown\","` | — |
| [SRC-1AE03B9EC3-L002375](../../agents/web_agent.py#L2375) | 2375 | `"            error_class: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002376](../../agents/web_agent.py#L2376) | 2376 | `"        ) -> PageFetchResult:"` | — |
| [SRC-1AE03B9EC3-L002377](../../agents/web_agent.py#L2377) | 2377 | `"            return PageFetchResult(title, page_text, status, error_class)"` | — |
| [SRC-1AE03B9EC3-L002378](../../agents/web_agent.py#L2378) | 2378 | `""` | — |
| [SRC-1AE03B9EC3-L002379](../../agents/web_agent.py#L2379) | 2379 | `"        current_url = _public_http_url(url)"` | — |
| [SRC-1AE03B9EC3-L002380](../../agents/web_agent.py#L2380) | 2380 | `"        if not current_url:"` | — |
| [SRC-1AE03B9EC3-L002381](../../agents/web_agent.py#L2381) | 2381 | `"            return result(status=\"rejected_url\", error_class=\"PublicUrlRejected\")"` | — |
| [SRC-1AE03B9EC3-L002382](../../agents/web_agent.py#L2382) | 2382 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L002383](../../agents/web_agent.py#L2383) | 2383 | `"        if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L002384](../../agents/web_agent.py#L2384) | 2384 | `"            budget.reserve(\"page_fetches\")"` | — |
| [SRC-1AE03B9EC3-L002385](../../agents/web_agent.py#L2385) | 2385 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002386](../../agents/web_agent.py#L2386) | 2386 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L002387](../../agents/web_agent.py#L2387) | 2387 | `"            from bs4 import BeautifulSoup"` | — |
| [SRC-1AE03B9EC3-L002388](../../agents/web_agent.py#L2388) | 2388 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L002389](../../agents/web_agent.py#L2389) | 2389 | `"            raise AgentDependencyError("` | — |
| [SRC-1AE03B9EC3-L002390](../../agents/web_agent.py#L2390) | 2390 | `"                \"حزم استخراج الصفحات غير مثبتة. نفّذ: python -m pip install -e .\""` | — |
| [SRC-1AE03B9EC3-L002391](../../agents/web_agent.py#L2391) | 2391 | `"            ) from exc"` | — |
| [SRC-1AE03B9EC3-L002392](../../agents/web_agent.py#L2392) | 2392 | `""` | — |
| [SRC-1AE03B9EC3-L002393](../../agents/web_agent.py#L2393) | 2393 | `"        headers = {"` | — |
| [SRC-1AE03B9EC3-L002394](../../agents/web_agent.py#L2394) | 2394 | `"            \"User-Agent\": \"OmaraiResearchBot/1.1 (public page research; no login)\","` | — |
| [SRC-1AE03B9EC3-L002395](../../agents/web_agent.py#L2395) | 2395 | `"            \"Accept\": \"text/html,application/xhtml+xml,text/plain;q=0.8\","` | — |
| [SRC-1AE03B9EC3-L002396](../../agents/web_agent.py#L2396) | 2396 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002397](../../agents/web_agent.py#L2397) | 2397 | `"        media_type = \"\""` | — |
| [SRC-1AE03B9EC3-L002398](../../agents/web_agent.py#L2398) | 2398 | `"        html = \"\""` | — |
| [SRC-1AE03B9EC3-L002399](../../agents/web_agent.py#L2399) | 2399 | `"        bytes_truncated = False"` | — |
| [SRC-1AE03B9EC3-L002400](../../agents/web_agent.py#L2400) | 2400 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002401](../../agents/web_agent.py#L2401) | 2401 | `"            with httpx.Client("` | — |
| [SRC-1AE03B9EC3-L002402](../../agents/web_agent.py#L2402) | 2402 | `"                timeout=self._effective_timeout(8.0),"` | — |
| [SRC-1AE03B9EC3-L002403](../../agents/web_agent.py#L2403) | 2403 | `"                follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002404](../../agents/web_agent.py#L2404) | 2404 | `"                headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002405](../../agents/web_agent.py#L2405) | 2405 | `"                verify=True,"` | — |
| [SRC-1AE03B9EC3-L002406](../../agents/web_agent.py#L2406) | 2406 | `"                trust_env=False,"` | — |
| [SRC-1AE03B9EC3-L002407](../../agents/web_agent.py#L2407) | 2407 | `"            ) as client:"` | — |
| [SRC-1AE03B9EC3-L002408](../../agents/web_agent.py#L2408) | 2408 | `"                for redirect_number in range(4):"` | — |
| [SRC-1AE03B9EC3-L002409](../../agents/web_agent.py#L2409) | 2409 | `"                    parsed = urllib.parse.urlparse(current_url)"` | — |
| [SRC-1AE03B9EC3-L002410](../../agents/web_agent.py#L2410) | 2410 | `"                    host = parsed.hostname or \"\""` | — |
| [SRC-1AE03B9EC3-L002411](../../agents/web_agent.py#L2411) | 2411 | `"                    # Resolve and pin a public IP. Do not let the HTTP client resolve"` | — |
| [SRC-1AE03B9EC3-L002412](../../agents/web_agent.py#L2412) | 2412 | `"                    # the original hostname a second time."` | — |
| [SRC-1AE03B9EC3-L002413](../../agents/web_agent.py#L2413) | 2413 | `"                    public_ips = _public_ip_literals(host)"` | — |
| [SRC-1AE03B9EC3-L002414](../../agents/web_agent.py#L2414) | 2414 | `"                    if not public_ips:"` | — |
| [SRC-1AE03B9EC3-L002415](../../agents/web_agent.py#L2415) | 2415 | `"                        return result(status=\"blocked_or_unresolved_host\", error_class=\"HostResolutionOrSSRFCheck\")"` | — |
| [SRC-1AE03B9EC3-L002416](../../agents/web_agent.py#L2416) | 2416 | `"                    connect_url = _pinned_connect_url(current_url, public_ips[0])"` | — |
| [SRC-1AE03B9EC3-L002417](../../agents/web_agent.py#L2417) | 2417 | `"                    if not connect_url:"` | — |
| [SRC-1AE03B9EC3-L002418](../../agents/web_agent.py#L2418) | 2418 | `"                        return result(status=\"blocked_connection_target\", error_class=\"PinnedTargetRejected\")"` | — |
| [SRC-1AE03B9EC3-L002419](../../agents/web_agent.py#L2419) | 2419 | `"                    request_headers = {\"Host\": host}"` | — |
| [SRC-1AE03B9EC3-L002420](../../agents/web_agent.py#L2420) | 2420 | `"                    extensions = {\"sni_hostname\": host} if parsed.scheme == \"https\" else {}"` | — |
| [SRC-1AE03B9EC3-L002421](../../agents/web_agent.py#L2421) | 2421 | `"                    with client.stream("` | — |
| [SRC-1AE03B9EC3-L002422](../../agents/web_agent.py#L2422) | 2422 | `"                        \"GET\","` | — |
| [SRC-1AE03B9EC3-L002423](../../agents/web_agent.py#L2423) | 2423 | `"                        connect_url,"` | — |
| [SRC-1AE03B9EC3-L002424](../../agents/web_agent.py#L2424) | 2424 | `"                        headers=request_headers,"` | — |
| [SRC-1AE03B9EC3-L002425](../../agents/web_agent.py#L2425) | 2425 | `"                        extensions=extensions,"` | — |
| [SRC-1AE03B9EC3-L002426](../../agents/web_agent.py#L2426) | 2426 | `"                    ) as response:"` | — |
| [SRC-1AE03B9EC3-L002427](../../agents/web_agent.py#L2427) | 2427 | `"                        if response.status_code in {301, 302, 303, 307, 308}:"` | — |
| [SRC-1AE03B9EC3-L002428](../../agents/web_agent.py#L2428) | 2428 | `"                            location = response.headers.get(\"location\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002429](../../agents/web_agent.py#L2429) | 2429 | `"                            if not location or redirect_number >= 3:"` | — |
| [SRC-1AE03B9EC3-L002430](../../agents/web_agent.py#L2430) | 2430 | `"                                return result(status=\"redirect_failed\", error_class=\"RedirectLimitOrMissingLocation\")"` | — |
| [SRC-1AE03B9EC3-L002431](../../agents/web_agent.py#L2431) | 2431 | `"                            target = _public_http_url("` | — |
| [SRC-1AE03B9EC3-L002432](../../agents/web_agent.py#L2432) | 2432 | `"                                urllib.parse.urljoin(current_url, location)"` | — |
| [SRC-1AE03B9EC3-L002433](../../agents/web_agent.py#L2433) | 2433 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002434](../../agents/web_agent.py#L2434) | 2434 | `"                            if not target:"` | — |
| [SRC-1AE03B9EC3-L002435](../../agents/web_agent.py#L2435) | 2435 | `"                                return result(status=\"redirect_rejected\", error_class=\"RedirectTargetRejected\")"` | — |
| [SRC-1AE03B9EC3-L002436](../../agents/web_agent.py#L2436) | 2436 | `"                            current_url = target"` | — |
| [SRC-1AE03B9EC3-L002437](../../agents/web_agent.py#L2437) | 2437 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002438](../../agents/web_agent.py#L2438) | 2438 | `"                        if response.status_code < 200 or response.status_code >= 300:"` | — |
| [SRC-1AE03B9EC3-L002439](../../agents/web_agent.py#L2439) | 2439 | `"                            return result(status=\"http_error\", error_class=\"HTTPStatus\")"` | — |
| [SRC-1AE03B9EC3-L002440](../../agents/web_agent.py#L2440) | 2440 | `"                        media_type = response.headers.get("` | — |
| [SRC-1AE03B9EC3-L002441](../../agents/web_agent.py#L2441) | 2441 | `"                            \"content-type\", \"\""` | — |
| [SRC-1AE03B9EC3-L002442](../../agents/web_agent.py#L2442) | 2442 | `"                        ).split(\";\")[0].lower()"` | — |
| [SRC-1AE03B9EC3-L002443](../../agents/web_agent.py#L2443) | 2443 | `"                        if media_type not in {"` | — |
| [SRC-1AE03B9EC3-L002444](../../agents/web_agent.py#L2444) | 2444 | `"                            \"text/html\", \"application/xhtml+xml\", \"text/plain\""` | — |
| [SRC-1AE03B9EC3-L002445](../../agents/web_agent.py#L2445) | 2445 | `"                        }:"` | — |
| [SRC-1AE03B9EC3-L002446](../../agents/web_agent.py#L2446) | 2446 | `"                            return result(status=\"unsupported_content_type\", error_class=\"UnsupportedContentType\")"` | — |
| [SRC-1AE03B9EC3-L002447](../../agents/web_agent.py#L2447) | 2447 | `"                        content_length = response.headers.get(\"content-length\")"` | — |
| [SRC-1AE03B9EC3-L002448](../../agents/web_agent.py#L2448) | 2448 | `"                        if content_length:"` | — |
| [SRC-1AE03B9EC3-L002449](../../agents/web_agent.py#L2449) | 2449 | `"                            try:"` | — |
| [SRC-1AE03B9EC3-L002450](../../agents/web_agent.py#L2450) | 2450 | `"                                if int(content_length) > MAX_PAGE_BYTES:"` | — |
| [SRC-1AE03B9EC3-L002451](../../agents/web_agent.py#L2451) | 2451 | `"                                    return result(status=\"page_too_large\", error_class=\"ContentLengthLimit\")"` | — |
| [SRC-1AE03B9EC3-L002452](../../agents/web_agent.py#L2452) | 2452 | `"                            except ValueError:"` | — |
| [SRC-1AE03B9EC3-L002453](../../agents/web_agent.py#L2453) | 2453 | `"                                pass"` | — |
| [SRC-1AE03B9EC3-L002454](../../agents/web_agent.py#L2454) | 2454 | `"                        chunks: list[bytes] = []"` | — |
| [SRC-1AE03B9EC3-L002455](../../agents/web_agent.py#L2455) | 2455 | `"                        count = 0"` | — |
| [SRC-1AE03B9EC3-L002456](../../agents/web_agent.py#L2456) | 2456 | `"                        for chunk in response.iter_bytes():"` | — |
| [SRC-1AE03B9EC3-L002457](../../agents/web_agent.py#L2457) | 2457 | `"                            count += len(chunk)"` | — |
| [SRC-1AE03B9EC3-L002458](../../agents/web_agent.py#L2458) | 2458 | `"                            if count > MAX_PAGE_BYTES:"` | — |
| [SRC-1AE03B9EC3-L002459](../../agents/web_agent.py#L2459) | 2459 | `"                                remaining = max(0, MAX_PAGE_BYTES - (count - len(chunk)))"` | — |
| [SRC-1AE03B9EC3-L002460](../../agents/web_agent.py#L2460) | 2460 | `"                                if remaining:"` | — |
| [SRC-1AE03B9EC3-L002461](../../agents/web_agent.py#L2461) | 2461 | `"                                    chunks.append(chunk[:remaining])"` | — |
| [SRC-1AE03B9EC3-L002462](../../agents/web_agent.py#L2462) | 2462 | `"                                bytes_truncated = True"` | — |
| [SRC-1AE03B9EC3-L002463](../../agents/web_agent.py#L2463) | 2463 | `"                                break"` | — |
| [SRC-1AE03B9EC3-L002464](../../agents/web_agent.py#L2464) | 2464 | `"                            chunks.append(chunk)"` | — |
| [SRC-1AE03B9EC3-L002465](../../agents/web_agent.py#L2465) | 2465 | `"                        raw = b\"\".join(chunks)"` | — |
| [SRC-1AE03B9EC3-L002466](../../agents/web_agent.py#L2466) | 2466 | `"                        encoding = response.encoding or \"utf-8\""` | — |
| [SRC-1AE03B9EC3-L002467](../../agents/web_agent.py#L2467) | 2467 | `"                        html = raw.decode(encoding, errors=\"replace\")"` | — |
| [SRC-1AE03B9EC3-L002468](../../agents/web_agent.py#L2468) | 2468 | `"                        break"` | — |
| [SRC-1AE03B9EC3-L002469](../../agents/web_agent.py#L2469) | 2469 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002470](../../agents/web_agent.py#L2470) | 2470 | `"                    return result(status=\"redirect_limit\", error_class=\"RedirectLimit\")"` | — |
| [SRC-1AE03B9EC3-L002471](../../agents/web_agent.py#L2471) | 2471 | `"        except (OSError, ValueError, httpx.HTTPError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002472](../../agents/web_agent.py#L2472) | 2472 | `"            return result(status=\"network_error\", error_class=type(exc).__name__)"` | — |
| [SRC-1AE03B9EC3-L002473](../../agents/web_agent.py#L2473) | 2473 | `""` | — |
| [SRC-1AE03B9EC3-L002474](../../agents/web_agent.py#L2474) | 2474 | `"        if media_type == \"text/plain\":"` | — |
| [SRC-1AE03B9EC3-L002475](../../agents/web_agent.py#L2475) | 2475 | `"            bounded_text = _clean_text(html, MAX_PAGE_TEXT_CHARS + 1)"` | — |
| [SRC-1AE03B9EC3-L002476](../../agents/web_agent.py#L2476) | 2476 | `"            text_truncated = len(bounded_text) > MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L002477](../../agents/web_agent.py#L2477) | 2477 | `"            page_text = _clean_text(bounded_text, MAX_PAGE_TEXT_CHARS)"` | — |
| [SRC-1AE03B9EC3-L002478](../../agents/web_agent.py#L2478) | 2478 | `"            status = ("` | — |
| [SRC-1AE03B9EC3-L002479](../../agents/web_agent.py#L2479) | 2479 | `"                \"empty_content\" if not page_text"` | — |
| [SRC-1AE03B9EC3-L002480](../../agents/web_agent.py#L2480) | 2480 | `"                else \"partial_extraction\" if bytes_truncated or text_truncated"` | — |
| [SRC-1AE03B9EC3-L002481](../../agents/web_agent.py#L2481) | 2481 | `"                else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L002482](../../agents/web_agent.py#L2482) | 2482 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002483](../../agents/web_agent.py#L2483) | 2483 | `"            return result(\"\", page_text, status)"` | — |
| [SRC-1AE03B9EC3-L002484](../../agents/web_agent.py#L2484) | 2484 | `""` | — |
| [SRC-1AE03B9EC3-L002485](../../agents/web_agent.py#L2485) | 2485 | `"        soup = BeautifulSoup(html, \"html.parser\")"` | — |
| [SRC-1AE03B9EC3-L002486](../../agents/web_agent.py#L2486) | 2486 | `"        title = _clean_text(soup.title.get_text(\" \", strip=True), 300) if soup.title else \"\""` | — |
| [SRC-1AE03B9EC3-L002487](../../agents/web_agent.py#L2487) | 2487 | `"        for element in soup(["` | — |
| [SRC-1AE03B9EC3-L002488](../../agents/web_agent.py#L2488) | 2488 | `"            \"script\", \"style\", \"nav\", \"footer\", \"header\", \"noscript\","` | — |
| [SRC-1AE03B9EC3-L002489](../../agents/web_agent.py#L2489) | 2489 | `"            \"svg\", \"form\", \"iframe\", \"template\""` | — |
| [SRC-1AE03B9EC3-L002490](../../agents/web_agent.py#L2490) | 2490 | `"        ]):"` | — |
| [SRC-1AE03B9EC3-L002491](../../agents/web_agent.py#L2491) | 2491 | `"            element.decompose()"` | — |
| [SRC-1AE03B9EC3-L002492](../../agents/web_agent.py#L2492) | 2492 | `"        main = soup.find(\"main\") or soup.find(\"article\") or soup.body or soup"` | — |
| [SRC-1AE03B9EC3-L002493](../../agents/web_agent.py#L2493) | 2493 | `"        bounded_text = _clean_text(main.get_text(\" \", strip=True), MAX_PAGE_TEXT_CHARS + 1)"` | — |
| [SRC-1AE03B9EC3-L002494](../../agents/web_agent.py#L2494) | 2494 | `"        text_truncated = len(bounded_text) > MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L002495](../../agents/web_agent.py#L2495) | 2495 | `"        page_text = _clean_text(bounded_text, MAX_PAGE_TEXT_CHARS)"` | — |
| [SRC-1AE03B9EC3-L002496](../../agents/web_agent.py#L2496) | 2496 | `"        status = ("` | — |
| [SRC-1AE03B9EC3-L002497](../../agents/web_agent.py#L2497) | 2497 | `"            \"no_text_extracted\" if not page_text"` | — |
| [SRC-1AE03B9EC3-L002498](../../agents/web_agent.py#L2498) | 2498 | `"            else \"partial_extraction\" if bytes_truncated or text_truncated"` | — |
| [SRC-1AE03B9EC3-L002499](../../agents/web_agent.py#L2499) | 2499 | `"            else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L002500](../../agents/web_agent.py#L2500) | 2500 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002501](../../agents/web_agent.py#L2501) | 2501 | `"        return result(title, page_text, status)"` | — |
| [SRC-1AE03B9EC3-L002502](../../agents/web_agent.py#L2502) | 2502 | `""` | — |
| [SRC-1AE03B9EC3-L002503](../../agents/web_agent.py#L2503) | 2503 | `"    def _collect_sources(self, query: str) -> tuple[list[dict[str, Any]], str \| None]:"` | — |
| [SRC-1AE03B9EC3-L002504](../../agents/web_agent.py#L2504) | 2504 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002505](../../agents/web_agent.py#L2505) | 2505 | `"            sources = self._search_web(query)"` | — |
| [SRC-1AE03B9EC3-L002506](../../agents/web_agent.py#L2506) | 2506 | `"        except (RuntimeError, AgentDependencyError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002507](../../agents/web_agent.py#L2507) | 2507 | `"            return [], str(exc)"` | — |
| [SRC-1AE03B9EC3-L002508](../../agents/web_agent.py#L2508) | 2508 | `"        for source in sources[:MAX_FETCHED_PAGES]:"` | — |
| [SRC-1AE03B9EC3-L002509](../../agents/web_agent.py#L2509) | 2509 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002510](../../agents/web_agent.py#L2510) | 2510 | `"                title, page_text = self._fetch_page(source[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L002511](../../agents/web_agent.py#L2511) | 2511 | `"            except (AgentDependencyError, RuntimeError):"` | — |
| [SRC-1AE03B9EC3-L002512](../../agents/web_agent.py#L2512) | 2512 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002513](../../agents/web_agent.py#L2513) | 2513 | `"            if title:"` | — |
| [SRC-1AE03B9EC3-L002514](../../agents/web_agent.py#L2514) | 2514 | `"                source[\"title\"] = title"` | — |
| [SRC-1AE03B9EC3-L002515](../../agents/web_agent.py#L2515) | 2515 | `"            if page_text:"` | — |
| [SRC-1AE03B9EC3-L002516](../../agents/web_agent.py#L2516) | 2516 | `"                source[\"page_text\"] = page_text"` | — |
| [SRC-1AE03B9EC3-L002517](../../agents/web_agent.py#L2517) | 2517 | `"                source[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L002518](../../agents/web_agent.py#L2518) | 2518 | `"                # Prefer extracted text over a thin search snippet."` | — |
| [SRC-1AE03B9EC3-L002519](../../agents/web_agent.py#L2519) | 2519 | `"                source[\"snippet\"] = page_text[:1800]"` | — |
| [SRC-1AE03B9EC3-L002520](../../agents/web_agent.py#L2520) | 2520 | `"        return sources, None"` | — |
| [SRC-1AE03B9EC3-L002521](../../agents/web_agent.py#L2521) | 2521 | `""` | — |
| [SRC-1AE03B9EC3-L002522](../../agents/web_agent.py#L2522) | 2522 | `"    def _collect_research("` | — |
| [SRC-1AE03B9EC3-L002523](../../agents/web_agent.py#L2523) | 2523 | `"        self, plan: dict[str, Any]"` | — |
| [SRC-1AE03B9EC3-L002524](../../agents/web_agent.py#L2524) | 2524 | `"    ) -> tuple[list[dict[str, Any]], list[str], dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L002525](../../agents/web_agent.py#L2525) | 2525 | `"        \"\"\"Run independent query searches concurrently, fuse evidence, then fetch top pages.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002526](../../agents/web_agent.py#L2526) | 2526 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002527](../../agents/web_agent.py#L2527) | 2527 | `"            query_limit = int(plan.get(\"query_limit\", MAX_PLAN_QUERIES))"` | — |
| [SRC-1AE03B9EC3-L002528](../../agents/web_agent.py#L2528) | 2528 | `"        except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L002529](../../agents/web_agent.py#L2529) | 2529 | `"            query_limit = MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L002530](../../agents/web_agent.py#L2530) | 2530 | `"        query_limit = max(1, min(query_limit, MAX_PLAN_QUERIES))"` | — |
| [SRC-1AE03B9EC3-L002531](../../agents/web_agent.py#L2531) | 2531 | `"        raw_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L002532](../../agents/web_agent.py#L2532) | 2532 | `"            compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L002533](../../agents/web_agent.py#L2533) | 2533 | `"            for query in plan.get(\"queries\", [])[:query_limit]"` | — |
| [SRC-1AE03B9EC3-L002534](../../agents/web_agent.py#L2534) | 2534 | `"            if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L002535](../../agents/web_agent.py#L2535) | 2535 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L002536](../../agents/web_agent.py#L2536) | 2536 | `"        raw_queries = [query for query in raw_queries if query]"` | — |
| [SRC-1AE03B9EC3-L002537](../../agents/web_agent.py#L2537) | 2537 | `"        target_aspects = ["` | — |
| [SRC-1AE03B9EC3-L002538](../../agents/web_agent.py#L2538) | 2538 | `"            str(target).strip()[:120]"` | — |
| [SRC-1AE03B9EC3-L002539](../../agents/web_agent.py#L2539) | 2539 | `"            for target in (plan.get(\"coverage_targets\") or [])[:8]"` | — |
| [SRC-1AE03B9EC3-L002540](../../agents/web_agent.py#L2540) | 2540 | `"            if isinstance(target, str) and target.strip()"` | — |
| [SRC-1AE03B9EC3-L002541](../../agents/web_agent.py#L2541) | 2541 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L002542](../../agents/web_agent.py#L2542) | 2542 | `"        # Reserve part of the existing query ceiling for evidence-gap repair."` | — |
| [SRC-1AE03B9EC3-L002543](../../agents/web_agent.py#L2543) | 2543 | `"        # This is a bounded retrieval loop, not an unbounded agent loop."` | — |
| [SRC-1AE03B9EC3-L002544](../../agents/web_agent.py#L2544) | 2544 | `"        repair_slot_limit = ("` | — |
| [SRC-1AE03B9EC3-L002545](../../agents/web_agent.py#L2545) | 2545 | `"            min(3, len(target_aspects), max(0, query_limit - 1))"` | — |
| [SRC-1AE03B9EC3-L002546](../../agents/web_agent.py#L2546) | 2546 | `"            if target_aspects else 0"` | — |
| [SRC-1AE03B9EC3-L002547](../../agents/web_agent.py#L2547) | 2547 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002548](../../agents/web_agent.py#L2548) | 2548 | `"        initial_query_limit = max(1, query_limit - repair_slot_limit)"` | — |
| [SRC-1AE03B9EC3-L002549](../../agents/web_agent.py#L2549) | 2549 | `"        queries = raw_queries[:initial_query_limit]"` | — |
| [SRC-1AE03B9EC3-L002550](../../agents/web_agent.py#L2550) | 2550 | `"        warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002551](../../agents/web_agent.py#L2551) | 2551 | `"        if not queries and not plan.get(\"direct_urls\"):"` | — |
| [SRC-1AE03B9EC3-L002552](../../agents/web_agent.py#L2552) | 2552 | `"            warnings.append(\"لم يُنشأ استعلام موضوعي قابل للبحث؛ لم تُستدعَ محركات البحث.\")"` | — |
| [SRC-1AE03B9EC3-L002553](../../agents/web_agent.py#L2553) | 2553 | `"        batches: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002554](../../agents/web_agent.py#L2554) | 2554 | `"        query_counts: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002555](../../agents/web_agent.py#L2555) | 2555 | `"        search_started_queries = 0"` | — |
| [SRC-1AE03B9EC3-L002556](../../agents/web_agent.py#L2556) | 2556 | `""` | — |
| [SRC-1AE03B9EC3-L002557](../../agents/web_agent.py#L2557) | 2557 | `"        if queries:"` | — |
| [SRC-1AE03B9EC3-L002558](../../agents/web_agent.py#L2558) | 2558 | `"            with ThreadPoolExecutor(max_workers=min(MAX_RESEARCH_WORKERS, len(queries))) as pool:"` | — |
| [SRC-1AE03B9EC3-L002559](../../agents/web_agent.py#L2559) | 2559 | `"                futures = {pool.submit(self._search_web, query): query for query in queries}"` | — |
| [SRC-1AE03B9EC3-L002560](../../agents/web_agent.py#L2560) | 2560 | `"                for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002561](../../agents/web_agent.py#L2561) | 2561 | `"                    query = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002562](../../agents/web_agent.py#L2562) | 2562 | `"                    search_started_queries += 1"` | — |
| [SRC-1AE03B9EC3-L002563](../../agents/web_agent.py#L2563) | 2563 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002564](../../agents/web_agent.py#L2564) | 2564 | `"                        results = future.result()"` | — |
| [SRC-1AE03B9EC3-L002565](../../agents/web_agent.py#L2565) | 2565 | `"                    except (RequestBudgetExceeded, RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002566](../../agents/web_agent.py#L2566) | 2566 | `"                        warnings.append(f\"تعذر بحث الاستعلام «{query[:70]}»: {exc}\")"` | — |
| [SRC-1AE03B9EC3-L002567](../../agents/web_agent.py#L2567) | 2567 | `"                        query_counts.append({\"query\": query, \"results\": 0})"` | — |
| [SRC-1AE03B9EC3-L002568](../../agents/web_agent.py#L2568) | 2568 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002569](../../agents/web_agent.py#L2569) | 2569 | `"                    query_counts.append({\"query\": query, \"results\": len(results)})"` | — |
| [SRC-1AE03B9EC3-L002570](../../agents/web_agent.py#L2570) | 2570 | `"                    grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002571](../../agents/web_agent.py#L2571) | 2571 | `"                    for source in results:"` | — |
| [SRC-1AE03B9EC3-L002572](../../agents/web_agent.py#L2572) | 2572 | `"                        provider = str(source.get(\"provider\") or \"web_search\")"` | — |
| [SRC-1AE03B9EC3-L002573](../../agents/web_agent.py#L2573) | 2573 | `"                        grouped.setdefault(provider, []).append(source)"` | — |
| [SRC-1AE03B9EC3-L002574](../../agents/web_agent.py#L2574) | 2574 | `"                    for provider, items in grouped.items():"` | — |
| [SRC-1AE03B9EC3-L002575](../../agents/web_agent.py#L2575) | 2575 | `"                        items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002576](../../agents/web_agent.py#L2576) | 2576 | `"                        batches.append({\"query\": query, \"provider\": provider, \"results\": items})"` | — |
| [SRC-1AE03B9EC3-L002577](../../agents/web_agent.py#L2577) | 2577 | `""` | — |
| [SRC-1AE03B9EC3-L002578](../../agents/web_agent.py#L2578) | 2578 | `"        # Evidence-gap iteration: deep tasks get up to three targeted follow-up searches"` | — |
| [SRC-1AE03B9EC3-L002579](../../agents/web_agent.py#L2579) | 2579 | `"        # when initial coverage is thin. This uses observed source/domain/provider coverage,"` | — |
| [SRC-1AE03B9EC3-L002580](../../agents/web_agent.py#L2580) | 2580 | `"        # not the language model's subjective claim that it has enough evidence."` | — |
| [SRC-1AE03B9EC3-L002581](../../agents/web_agent.py#L2581) | 2581 | `"        preliminary = fuse_ranked_results(batches, limit=MAX_SEARCH_RESULTS)"` | — |
| [SRC-1AE03B9EC3-L002582](../../agents/web_agent.py#L2582) | 2582 | `"        preliminary_domains = {"` | — |
| [SRC-1AE03B9EC3-L002583](../../agents/web_agent.py#L2583) | 2583 | `"            registrable_domain(item.get(\"domain\") or urllib.parse.urlparse(item.get(\"url\", \"\")).hostname)"` | — |
| [SRC-1AE03B9EC3-L002584](../../agents/web_agent.py#L2584) | 2584 | `"            for item in preliminary"` | — |
| [SRC-1AE03B9EC3-L002585](../../agents/web_agent.py#L2585) | 2585 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002586](../../agents/web_agent.py#L2586) | 2586 | `"        preliminary_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L002587](../../agents/web_agent.py#L2587) | 2587 | `"        preliminary_providers = {"` | — |
| [SRC-1AE03B9EC3-L002588](../../agents/web_agent.py#L2588) | 2588 | `"            provider for item in preliminary for provider in item.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L002589](../../agents/web_agent.py#L2589) | 2589 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002590](../../agents/web_agent.py#L2590) | 2590 | `"        needs_expansion = ("` | — |
| [SRC-1AE03B9EC3-L002591](../../agents/web_agent.py#L2591) | 2591 | `"            plan.get(\"depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L002592](../../agents/web_agent.py#L2592) | 2592 | `"            and (len(preliminary) < 8 or len(preliminary_domains) < 5 or len(preliminary_providers) < 2)"` | — |
| [SRC-1AE03B9EC3-L002593](../../agents/web_agent.py#L2593) | 2593 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002594](../../agents/web_agent.py#L2594) | 2594 | `"        preliminary_ledger = build_evidence_ledger(target_aspects, preliminary)"` | — |
| [SRC-1AE03B9EC3-L002595](../../agents/web_agent.py#L2595) | 2595 | `"        missing_aspects = list(preliminary_ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L002596](../../agents/web_agent.py#L2596) | 2596 | `"        expansion_queries: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002597](../../agents/web_agent.py#L2597) | 2597 | `"        # Do not issue generic repairs when a standard task already has per-requirement queries."` | — |
| [SRC-1AE03B9EC3-L002598](../../agents/web_agent.py#L2598) | 2598 | `"        # Legacy plans without those query records still need the bounded missing-aspect fallback;"` | — |
| [SRC-1AE03B9EC3-L002599](../../agents/web_agent.py#L2599) | 2599 | `"        # deep research may expand further even after targeted queries."` | — |
| [SRC-1AE03B9EC3-L002600](../../agents/web_agent.py#L2600) | 2600 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L002601](../../agents/web_agent.py#L2601) | 2601 | `"            (missing_aspects or needs_expansion)"` | — |
| [SRC-1AE03B9EC3-L002602](../../agents/web_agent.py#L2602) | 2602 | `"            and len(queries) < query_limit"` | — |
| [SRC-1AE03B9EC3-L002603](../../agents/web_agent.py#L2603) | 2603 | `"            and queries"` | — |
| [SRC-1AE03B9EC3-L002604](../../agents/web_agent.py#L2604) | 2604 | `"            and ("` | — |
| [SRC-1AE03B9EC3-L002605](../../agents/web_agent.py#L2605) | 2605 | `"                not plan.get(\"requirement_queries\")"` | — |
| [SRC-1AE03B9EC3-L002606](../../agents/web_agent.py#L2606) | 2606 | `"                or plan.get(\"depth\") == \"deep\""` | — |
| [SRC-1AE03B9EC3-L002607](../../agents/web_agent.py#L2607) | 2607 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002608](../../agents/web_agent.py#L2608) | 2608 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L002609](../../agents/web_agent.py#L2609) | 2609 | `"            base_query = (queries[0] if queries else \"\")"` | — |
| [SRC-1AE03B9EC3-L002610](../../agents/web_agent.py#L2610) | 2610 | `"            remaining_slots = max(0, query_limit - len(queries))"` | — |
| [SRC-1AE03B9EC3-L002611](../../agents/web_agent.py#L2611) | 2611 | `"            aspect_queries = repair_queries_for_missing_aspects("` | — |
| [SRC-1AE03B9EC3-L002612](../../agents/web_agent.py#L2612) | 2612 | `"                base_query,"` | — |
| [SRC-1AE03B9EC3-L002613](../../agents/web_agent.py#L2613) | 2613 | `"                missing_aspects,"` | — |
| [SRC-1AE03B9EC3-L002614](../../agents/web_agent.py#L2614) | 2614 | `"                limit=min(repair_slot_limit, remaining_slots),"` | — |
| [SRC-1AE03B9EC3-L002615](../../agents/web_agent.py#L2615) | 2615 | `"                compact_fn=compact_search_query,"` | — |
| [SRC-1AE03B9EC3-L002616](../../agents/web_agent.py#L2616) | 2616 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002617](../../agents/web_agent.py#L2617) | 2617 | `"            candidates = list(aspect_queries)"` | — |
| [SRC-1AE03B9EC3-L002618](../../agents/web_agent.py#L2618) | 2618 | `"            if needs_expansion:"` | — |
| [SRC-1AE03B9EC3-L002619](../../agents/web_agent.py#L2619) | 2619 | `"                candidates.extend(["` | — |
| [SRC-1AE03B9EC3-L002620](../../agents/web_agent.py#L2620) | 2620 | `"                    f\"{base_query} official sources data reports\","` | — |
| [SRC-1AE03B9EC3-L002621](../../agents/web_agent.py#L2621) | 2621 | `"                    f\"{base_query} limitations risks criticism alternatives\","` | — |
| [SRC-1AE03B9EC3-L002622](../../agents/web_agent.py#L2622) | 2622 | `"                    f\"{base_query} recent developments case studies analysis\","` | — |
| [SRC-1AE03B9EC3-L002623](../../agents/web_agent.py#L2623) | 2623 | `"                ])"` | — |
| [SRC-1AE03B9EC3-L002624](../../agents/web_agent.py#L2624) | 2624 | `"            existing = {item.casefold() for item in queries}"` | — |
| [SRC-1AE03B9EC3-L002625](../../agents/web_agent.py#L2625) | 2625 | `"            expansion_queries = []"` | — |
| [SRC-1AE03B9EC3-L002626](../../agents/web_agent.py#L2626) | 2626 | `"            seen_expansions = set(existing)"` | — |
| [SRC-1AE03B9EC3-L002627](../../agents/web_agent.py#L2627) | 2627 | `"            for candidate in candidates:"` | — |
| [SRC-1AE03B9EC3-L002628](../../agents/web_agent.py#L2628) | 2628 | `"                compacted = compact_search_query(candidate)"` | — |
| [SRC-1AE03B9EC3-L002629](../../agents/web_agent.py#L2629) | 2629 | `"                key = compacted.casefold()"` | — |
| [SRC-1AE03B9EC3-L002630](../../agents/web_agent.py#L2630) | 2630 | `"                if compacted and key not in seen_expansions:"` | — |
| [SRC-1AE03B9EC3-L002631](../../agents/web_agent.py#L2631) | 2631 | `"                    expansion_queries.append(compacted)"` | — |
| [SRC-1AE03B9EC3-L002632](../../agents/web_agent.py#L2632) | 2632 | `"                    seen_expansions.add(key)"` | — |
| [SRC-1AE03B9EC3-L002633](../../agents/web_agent.py#L2633) | 2633 | `"                if len(expansion_queries) >= remaining_slots:"` | — |
| [SRC-1AE03B9EC3-L002634](../../agents/web_agent.py#L2634) | 2634 | `"                    break"` | — |
| [SRC-1AE03B9EC3-L002635](../../agents/web_agent.py#L2635) | 2635 | `"            if expansion_queries:"` | — |
| [SRC-1AE03B9EC3-L002636](../../agents/web_agent.py#L2636) | 2636 | `"                with ThreadPoolExecutor("` | — |
| [SRC-1AE03B9EC3-L002637](../../agents/web_agent.py#L2637) | 2637 | `"                    max_workers=min(MAX_RESEARCH_WORKERS, len(expansion_queries))"` | — |
| [SRC-1AE03B9EC3-L002638](../../agents/web_agent.py#L2638) | 2638 | `"                ) as pool:"` | — |
| [SRC-1AE03B9EC3-L002639](../../agents/web_agent.py#L2639) | 2639 | `"                    futures = {"` | — |
| [SRC-1AE03B9EC3-L002640](../../agents/web_agent.py#L2640) | 2640 | `"                        pool.submit(self._search_web, query): query"` | — |
| [SRC-1AE03B9EC3-L002641](../../agents/web_agent.py#L2641) | 2641 | `"                        for query in expansion_queries"` | — |
| [SRC-1AE03B9EC3-L002642](../../agents/web_agent.py#L2642) | 2642 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L002643](../../agents/web_agent.py#L2643) | 2643 | `"                    for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002644](../../agents/web_agent.py#L2644) | 2644 | `"                        query = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002645](../../agents/web_agent.py#L2645) | 2645 | `"                        search_started_queries += 1"` | — |
| [SRC-1AE03B9EC3-L002646](../../agents/web_agent.py#L2646) | 2646 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L002647](../../agents/web_agent.py#L2647) | 2647 | `"                            results = future.result()"` | — |
| [SRC-1AE03B9EC3-L002648](../../agents/web_agent.py#L2648) | 2648 | `"                        except (RequestBudgetExceeded, RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002649](../../agents/web_agent.py#L2649) | 2649 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002650](../../agents/web_agent.py#L2650) | 2650 | `"                                f\"تعذر بحث زاوية إضافية «{query[:70]}»: {exc}\""` | — |
| [SRC-1AE03B9EC3-L002651](../../agents/web_agent.py#L2651) | 2651 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002652](../../agents/web_agent.py#L2652) | 2652 | `"                            query_counts.append({\"query\": query, \"results\": 0})"` | — |
| [SRC-1AE03B9EC3-L002653](../../agents/web_agent.py#L2653) | 2653 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002654](../../agents/web_agent.py#L2654) | 2654 | `"                        query_counts.append({\"query\": query, \"results\": len(results)})"` | — |
| [SRC-1AE03B9EC3-L002655](../../agents/web_agent.py#L2655) | 2655 | `"                        grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002656](../../agents/web_agent.py#L2656) | 2656 | `"                        for source in results:"` | — |
| [SRC-1AE03B9EC3-L002657](../../agents/web_agent.py#L2657) | 2657 | `"                            grouped.setdefault("` | — |
| [SRC-1AE03B9EC3-L002658](../../agents/web_agent.py#L2658) | 2658 | `"                                str(source.get(\"provider\") or \"web_search\"), []"` | — |
| [SRC-1AE03B9EC3-L002659](../../agents/web_agent.py#L2659) | 2659 | `"                            ).append(source)"` | — |
| [SRC-1AE03B9EC3-L002660](../../agents/web_agent.py#L2660) | 2660 | `"                        for provider, items in grouped.items():"` | — |
| [SRC-1AE03B9EC3-L002661](../../agents/web_agent.py#L2661) | 2661 | `"                            items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002662](../../agents/web_agent.py#L2662) | 2662 | `"                            batches.append({"` | — |
| [SRC-1AE03B9EC3-L002663](../../agents/web_agent.py#L2663) | 2663 | `"                                \"query\": query, \"provider\": provider, \"results\": items"` | — |
| [SRC-1AE03B9EC3-L002664](../../agents/web_agent.py#L2664) | 2664 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L002665](../../agents/web_agent.py#L2665) | 2665 | `"                queries.extend(expansion_queries)"` | — |
| [SRC-1AE03B9EC3-L002666](../../agents/web_agent.py#L2666) | 2666 | `"        # Report queries actually selected, not planned queries skipped to reserve repair capacity."` | — |
| [SRC-1AE03B9EC3-L002667](../../agents/web_agent.py#L2667) | 2667 | `"        plan[\"queries\"] = list(dict.fromkeys(queries))"` | — |
| [SRC-1AE03B9EC3-L002668](../../agents/web_agent.py#L2668) | 2668 | `""` | — |
| [SRC-1AE03B9EC3-L002669](../../agents/web_agent.py#L2669) | 2669 | `"        # Google News RSS is included concurrently by _search_web for freshness-bearing queries."` | — |
| [SRC-1AE03B9EC3-L002670](../../agents/web_agent.py#L2670) | 2670 | `""` | — |
| [SRC-1AE03B9EC3-L002671](../../agents/web_agent.py#L2671) | 2671 | `"        # A social-focused task uses public social endpoints in parallel with indexed"` | — |
| [SRC-1AE03B9EC3-L002672](../../agents/web_agent.py#L2672) | 2672 | `"        # public pages. No login, private profile, session cookie or anti-bot bypass."` | — |
| [SRC-1AE03B9EC3-L002673](../../agents/web_agent.py#L2673) | 2673 | `"        social_results: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002674](../../agents/web_agent.py#L2674) | 2674 | `"        if plan.get(\"social_focus\") and queries:"` | — |
| [SRC-1AE03B9EC3-L002675](../../agents/web_agent.py#L2675) | 2675 | `"            requested_platforms = plan.get(\"platforms\") or []"` | — |
| [SRC-1AE03B9EC3-L002676](../../agents/web_agent.py#L2676) | 2676 | `"            if requested_platforms:"` | — |
| [SRC-1AE03B9EC3-L002677](../../agents/web_agent.py#L2677) | 2677 | `"                platforms = list(dict.fromkeys(requested_platforms))"` | — |
| [SRC-1AE03B9EC3-L002678](../../agents/web_agent.py#L2678) | 2678 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L002679](../../agents/web_agent.py#L2679) | 2679 | `"                # Broad social research: always try no-key public sources, and add"` | — |
| [SRC-1AE03B9EC3-L002680](../../agents/web_agent.py#L2680) | 2680 | `"                # official platform connectors only when they are configured."` | — |
| [SRC-1AE03B9EC3-L002681](../../agents/web_agent.py#L2681) | 2681 | `"                platforms = [\"reddit\", \"bluesky\"]"` | — |
| [SRC-1AE03B9EC3-L002682](../../agents/web_agent.py#L2682) | 2682 | `"                optional_connectors = {"` | — |
| [SRC-1AE03B9EC3-L002683](../../agents/web_agent.py#L2683) | 2683 | `"                    \"facebook\": bool("` | — |
| [SRC-1AE03B9EC3-L002684](../../agents/web_agent.py#L2684) | 2684 | `"                        os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002685](../../agents/web_agent.py#L2685) | 2685 | `"                        and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002686](../../agents/web_agent.py#L2686) | 2686 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L002687](../../agents/web_agent.py#L2687) | 2687 | `"                    \"instagram\": bool("` | — |
| [SRC-1AE03B9EC3-L002688](../../agents/web_agent.py#L2688) | 2688 | `"                        os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002689](../../agents/web_agent.py#L2689) | 2689 | `"                        and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002690](../../agents/web_agent.py#L2690) | 2690 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L002691](../../agents/web_agent.py#L2691) | 2691 | `"                    \"x\": bool(os.getenv(\"X_BEARER_TOKEN\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L002692](../../agents/web_agent.py#L2692) | 2692 | `"                    \"youtube\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L002693](../../agents/web_agent.py#L2693) | 2693 | `"                }"` | — |
| [SRC-1AE03B9EC3-L002694](../../agents/web_agent.py#L2694) | 2694 | `"                platforms.extend("` | — |
| [SRC-1AE03B9EC3-L002695](../../agents/web_agent.py#L2695) | 2695 | `"                    name for name, ready in optional_connectors.items()"` | — |
| [SRC-1AE03B9EC3-L002696](../../agents/web_agent.py#L2696) | 2696 | `"                    if ready and name not in platforms"` | — |
| [SRC-1AE03B9EC3-L002697](../../agents/web_agent.py#L2697) | 2697 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002698](../../agents/web_agent.py#L2698) | 2698 | `"            social_results, social_warnings = self._search_social((queries[0] if queries else \"\"), platforms)"` | — |
| [SRC-1AE03B9EC3-L002699](../../agents/web_agent.py#L2699) | 2699 | `"            warnings.extend(social_warnings)"` | — |
| [SRC-1AE03B9EC3-L002700](../../agents/web_agent.py#L2700) | 2700 | `"            social_groups: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L002701](../../agents/web_agent.py#L2701) | 2701 | `"            for source in social_results:"` | — |
| [SRC-1AE03B9EC3-L002702](../../agents/web_agent.py#L2702) | 2702 | `"                social_groups.setdefault(str(source.get(\"provider\") or \"social\"), []).append(source)"` | — |
| [SRC-1AE03B9EC3-L002703](../../agents/web_agent.py#L2703) | 2703 | `"            for provider, items in social_groups.items():"` | — |
| [SRC-1AE03B9EC3-L002704](../../agents/web_agent.py#L2704) | 2704 | `"                items.sort(key=lambda item: int(item.get(\"provider_rank\", 999)))"` | — |
| [SRC-1AE03B9EC3-L002705](../../agents/web_agent.py#L2705) | 2705 | `"                batches.append({\"query\": (queries[0] if queries else \"\"), \"provider\": provider, \"results\": items})"` | — |
| [SRC-1AE03B9EC3-L002706](../../agents/web_agent.py#L2706) | 2706 | `""` | — |
| [SRC-1AE03B9EC3-L002707](../../agents/web_agent.py#L2707) | 2707 | `"        # Explicit URLs are first-class inputs: fetch the page the user actually asked about"` | — |
| [SRC-1AE03B9EC3-L002708](../../agents/web_agent.py#L2708) | 2708 | `"        # instead of relying on a search engine to rediscover it. URL and DNS checks still apply."` | — |
| [SRC-1AE03B9EC3-L002709](../../agents/web_agent.py#L2709) | 2709 | `"        direct_urls: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002710](../../agents/web_agent.py#L2710) | 2710 | `"        for value in plan.get(\"direct_urls\", [])[:5]:"` | — |
| [SRC-1AE03B9EC3-L002711](../../agents/web_agent.py#L2711) | 2711 | `"            safe_url = _public_http_url(value)"` | — |
| [SRC-1AE03B9EC3-L002712](../../agents/web_agent.py#L2712) | 2712 | `"            if safe_url and not _blocked_source_url(safe_url) and safe_url not in direct_urls:"` | — |
| [SRC-1AE03B9EC3-L002713](../../agents/web_agent.py#L2713) | 2713 | `"                direct_urls.append(safe_url)"` | — |
| [SRC-1AE03B9EC3-L002714](../../agents/web_agent.py#L2714) | 2714 | `"        for direct_url in direct_urls:"` | — |
| [SRC-1AE03B9EC3-L002715](../../agents/web_agent.py#L2715) | 2715 | `"            batches.append({"` | — |
| [SRC-1AE03B9EC3-L002716](../../agents/web_agent.py#L2716) | 2716 | `"                \"query\": (queries[0] if queries else \"\"),"` | — |
| [SRC-1AE03B9EC3-L002717](../../agents/web_agent.py#L2717) | 2717 | `"                \"provider\": \"user_supplied_url\","` | — |
| [SRC-1AE03B9EC3-L002718](../../agents/web_agent.py#L2718) | 2718 | `"                \"results\": [{"` | — |
| [SRC-1AE03B9EC3-L002719](../../agents/web_agent.py#L2719) | 2719 | `"                    \"title\": \"رابط قدمه المستخدم للتحليل\","` | — |
| [SRC-1AE03B9EC3-L002720](../../agents/web_agent.py#L2720) | 2720 | `"                    \"url\": direct_url,"` | — |
| [SRC-1AE03B9EC3-L002721](../../agents/web_agent.py#L2721) | 2721 | `"                    \"snippet\": \"\","` | — |
| [SRC-1AE03B9EC3-L002722](../../agents/web_agent.py#L2722) | 2722 | `"                    \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002723](../../agents/web_agent.py#L2723) | 2723 | `"                    \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002724](../../agents/web_agent.py#L2724) | 2724 | `"                    \"provider\": \"user_supplied_url\","` | — |
| [SRC-1AE03B9EC3-L002725](../../agents/web_agent.py#L2725) | 2725 | `"                    \"provider_rank\": 1,"` | — |
| [SRC-1AE03B9EC3-L002726](../../agents/web_agent.py#L2726) | 2726 | `"                    \"search_query\": (queries[0] if queries else \"\"),"` | — |
| [SRC-1AE03B9EC3-L002727](../../agents/web_agent.py#L2727) | 2727 | `"                    \"published_at\": \"\","` | — |
| [SRC-1AE03B9EC3-L002728](../../agents/web_agent.py#L2728) | 2728 | `"                }],"` | — |
| [SRC-1AE03B9EC3-L002729](../../agents/web_agent.py#L2729) | 2729 | `"            })"` | — |
| [SRC-1AE03B9EC3-L002730](../../agents/web_agent.py#L2730) | 2730 | `""` | — |
| [SRC-1AE03B9EC3-L002731](../../agents/web_agent.py#L2731) | 2731 | `"        raw_results_count = sum(len(batch.get(\"results\", [])) for batch in batches if isinstance(batch, dict) and isinstance(batch.get(\"results\", []), list))"` | — |
| [SRC-1AE03B9EC3-L002732](../../agents/web_agent.py#L2732) | 2732 | `"        sources = fuse_ranked_results(batches, limit=MAX_SEARCH_RESULTS)"` | — |
| [SRC-1AE03B9EC3-L002733](../../agents/web_agent.py#L2733) | 2733 | `""` | — |
| [SRC-1AE03B9EC3-L002734](../../agents/web_agent.py#L2734) | 2734 | `"        # Keep at least one returned source per explicit criterion query in the"` | — |
| [SRC-1AE03B9EC3-L002735](../../agents/web_agent.py#L2735) | 2735 | `"        # bounded source set sent to synthesis. Global fusion can otherwise crowd"` | — |
| [SRC-1AE03B9EC3-L002736](../../agents/web_agent.py#L2736) | 2736 | `"        # lower-ranked criterion results out before the model can inspect them."` | — |
| [SRC-1AE03B9EC3-L002737](../../agents/web_agent.py#L2737) | 2737 | `"        requirement_queries = plan.get(\"requirement_queries\", [])"` | — |
| [SRC-1AE03B9EC3-L002738](../../agents/web_agent.py#L2738) | 2738 | `"        if isinstance(requirement_queries, list) and requirement_queries:"` | — |
| [SRC-1AE03B9EC3-L002739](../../agents/web_agent.py#L2739) | 2739 | `"            globally_fused = sources"` | — |
| [SRC-1AE03B9EC3-L002740](../../agents/web_agent.py#L2740) | 2740 | `"            globally_fused_by_url = {"` | — |
| [SRC-1AE03B9EC3-L002741](../../agents/web_agent.py#L2741) | 2741 | `"                self._normalized_source_url_key(item.get(\"url\", \"\")): item"` | — |
| [SRC-1AE03B9EC3-L002742](../../agents/web_agent.py#L2742) | 2742 | `"                for item in globally_fused"` | — |
| [SRC-1AE03B9EC3-L002743](../../agents/web_agent.py#L2743) | 2743 | `"                if self._normalized_source_url_key(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002744](../../agents/web_agent.py#L2744) | 2744 | `"            }"` | — |
| [SRC-1AE03B9EC3-L002745](../../agents/web_agent.py#L2745) | 2745 | `"            pinned_by_url: dict[str, dict[str, Any]] = {}"` | — |
| [SRC-1AE03B9EC3-L002746](../../agents/web_agent.py#L2746) | 2746 | `"            pinned_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002747](../../agents/web_agent.py#L2747) | 2747 | `"            for requirement in requirement_queries[:MAX_PLAN_QUERIES]:"` | — |
| [SRC-1AE03B9EC3-L002748](../../agents/web_agent.py#L2748) | 2748 | `"                if not isinstance(requirement, dict):"` | — |
| [SRC-1AE03B9EC3-L002749](../../agents/web_agent.py#L2749) | 2749 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002750](../../agents/web_agent.py#L2750) | 2750 | `"                target_query = compact_search_query(str(requirement.get(\"query\") or \"\"))"` | — |
| [SRC-1AE03B9EC3-L002751](../../agents/web_agent.py#L2751) | 2751 | `"                if not target_query:"` | — |
| [SRC-1AE03B9EC3-L002752](../../agents/web_agent.py#L2752) | 2752 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002753](../../agents/web_agent.py#L2753) | 2753 | `"                query_key = re.sub(r\"\\s+\", \" \", target_query).strip().casefold()"` | — |
| [SRC-1AE03B9EC3-L002754](../../agents/web_agent.py#L2754) | 2754 | `"                criterion_batches = ["` | — |
| [SRC-1AE03B9EC3-L002755](../../agents/web_agent.py#L2755) | 2755 | `"                    batch for batch in batches"` | — |
| [SRC-1AE03B9EC3-L002756](../../agents/web_agent.py#L2756) | 2756 | `"                    if re.sub("` | — |
| [SRC-1AE03B9EC3-L002757](../../agents/web_agent.py#L2757) | 2757 | `"                        r\"\\s+\", \" \", str(batch.get(\"query\") or \"\")"` | — |
| [SRC-1AE03B9EC3-L002758](../../agents/web_agent.py#L2758) | 2758 | `"                    ).strip().casefold() == query_key"` | — |
| [SRC-1AE03B9EC3-L002759](../../agents/web_agent.py#L2759) | 2759 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L002760](../../agents/web_agent.py#L2760) | 2760 | `"                criterion_candidates = fuse_ranked_results("` | — |
| [SRC-1AE03B9EC3-L002761](../../agents/web_agent.py#L2761) | 2761 | `"                    criterion_batches, limit=MAX_SEARCH_RESULTS"` | — |
| [SRC-1AE03B9EC3-L002762](../../agents/web_agent.py#L2762) | 2762 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002763](../../agents/web_agent.py#L2763) | 2763 | `"                candidate = None"` | — |
| [SRC-1AE03B9EC3-L002764](../../agents/web_agent.py#L2764) | 2764 | `"                if criterion_candidates:"` | — |
| [SRC-1AE03B9EC3-L002765](../../agents/web_agent.py#L2765) | 2765 | `"                    criterion_ledger = build_requirement_evidence_ledger("` | — |
| [SRC-1AE03B9EC3-L002766](../../agents/web_agent.py#L2766) | 2766 | `"                        [str(requirement.get(\"target\") or \"\")],"` | — |
| [SRC-1AE03B9EC3-L002767](../../agents/web_agent.py#L2767) | 2767 | `"                        criterion_candidates,"` | — |
| [SRC-1AE03B9EC3-L002768](../../agents/web_agent.py#L2768) | 2768 | `"                        [requirement],"` | — |
| [SRC-1AE03B9EC3-L002769](../../agents/web_agent.py#L2769) | 2769 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002770](../../agents/web_agent.py#L2770) | 2770 | `"                    candidate_indexes = ("` | — |
| [SRC-1AE03B9EC3-L002771](../../agents/web_agent.py#L2771) | 2771 | `"                        criterion_ledger[0].get(\"candidate_source_indexes\", [])"` | — |
| [SRC-1AE03B9EC3-L002772](../../agents/web_agent.py#L2772) | 2772 | `"                        if criterion_ledger else []"` | — |
| [SRC-1AE03B9EC3-L002773](../../agents/web_agent.py#L2773) | 2773 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002774](../../agents/web_agent.py#L2774) | 2774 | `"                    if candidate_indexes:"` | — |
| [SRC-1AE03B9EC3-L002775](../../agents/web_agent.py#L2775) | 2775 | `"                        candidate = criterion_candidates[int(candidate_indexes[0]) - 1]"` | — |
| [SRC-1AE03B9EC3-L002776](../../agents/web_agent.py#L2776) | 2776 | `"                if candidate is None:"` | — |
| [SRC-1AE03B9EC3-L002777](../../agents/web_agent.py#L2777) | 2777 | `"                    candidate = next("` | — |
| [SRC-1AE03B9EC3-L002778](../../agents/web_agent.py#L2778) | 2778 | `"                        ("` | — |
| [SRC-1AE03B9EC3-L002779](../../agents/web_agent.py#L2779) | 2779 | `"                            item for item in globally_fused"` | — |
| [SRC-1AE03B9EC3-L002780](../../agents/web_agent.py#L2780) | 2780 | `"                            if query_key in {"` | — |
| [SRC-1AE03B9EC3-L002781](../../agents/web_agent.py#L2781) | 2781 | `"                                re.sub(r\"\\s+\", \" \", str(value)).strip().casefold()"` | — |
| [SRC-1AE03B9EC3-L002782](../../agents/web_agent.py#L2782) | 2782 | `"                                for value in item.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L002783](../../agents/web_agent.py#L2783) | 2783 | `"                            }"` | — |
| [SRC-1AE03B9EC3-L002784](../../agents/web_agent.py#L2784) | 2784 | `"                        ),"` | — |
| [SRC-1AE03B9EC3-L002785](../../agents/web_agent.py#L2785) | 2785 | `"                        criterion_candidates[0] if criterion_candidates else None,"` | — |
| [SRC-1AE03B9EC3-L002786](../../agents/web_agent.py#L2786) | 2786 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002787](../../agents/web_agent.py#L2787) | 2787 | `"                if not candidate:"` | — |
| [SRC-1AE03B9EC3-L002788](../../agents/web_agent.py#L2788) | 2788 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002789](../../agents/web_agent.py#L2789) | 2789 | `"                source_key = self._normalized_source_url_key(candidate.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002790](../../agents/web_agent.py#L2790) | 2790 | `"                if not source_key:"` | — |
| [SRC-1AE03B9EC3-L002791](../../agents/web_agent.py#L2791) | 2791 | `"                    continue"` | — |
| [SRC-1AE03B9EC3-L002792](../../agents/web_agent.py#L2792) | 2792 | `"                selected = ("` | — |
| [SRC-1AE03B9EC3-L002793](../../agents/web_agent.py#L2793) | 2793 | `"                    pinned_by_url.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L002794](../../agents/web_agent.py#L2794) | 2794 | `"                    or globally_fused_by_url.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L002795](../../agents/web_agent.py#L2795) | 2795 | `"                    or candidate"` | — |
| [SRC-1AE03B9EC3-L002796](../../agents/web_agent.py#L2796) | 2796 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002797](../../agents/web_agent.py#L2797) | 2797 | `"                if source_key not in pinned_by_url:"` | — |
| [SRC-1AE03B9EC3-L002798](../../agents/web_agent.py#L2798) | 2798 | `"                    pinned_by_url[source_key] = selected"` | — |
| [SRC-1AE03B9EC3-L002799](../../agents/web_agent.py#L2799) | 2799 | `"                    pinned_sources.append(selected)"` | — |
| [SRC-1AE03B9EC3-L002800](../../agents/web_agent.py#L2800) | 2800 | `"                selected_queries = selected.setdefault(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L002801](../../agents/web_agent.py#L2801) | 2801 | `"                if target_query not in selected_queries:"` | — |
| [SRC-1AE03B9EC3-L002802](../../agents/web_agent.py#L2802) | 2802 | `"                    selected_queries.append(target_query)"` | — |
| [SRC-1AE03B9EC3-L002803](../../agents/web_agent.py#L2803) | 2803 | `"            pinned_keys = set(pinned_by_url)"` | — |
| [SRC-1AE03B9EC3-L002804](../../agents/web_agent.py#L2804) | 2804 | `"            sources = ("` | — |
| [SRC-1AE03B9EC3-L002805](../../agents/web_agent.py#L2805) | 2805 | `"                pinned_sources"` | — |
| [SRC-1AE03B9EC3-L002806](../../agents/web_agent.py#L2806) | 2806 | `"                + ["` | — |
| [SRC-1AE03B9EC3-L002807](../../agents/web_agent.py#L2807) | 2807 | `"                    item for item in globally_fused"` | — |
| [SRC-1AE03B9EC3-L002808](../../agents/web_agent.py#L2808) | 2808 | `"                    if self._normalized_source_url_key(item.get(\"url\", \"\")) not in pinned_keys"` | — |
| [SRC-1AE03B9EC3-L002809](../../agents/web_agent.py#L2809) | 2809 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L002810](../../agents/web_agent.py#L2810) | 2810 | `"            )[:MAX_SEARCH_RESULTS]"` | — |
| [SRC-1AE03B9EC3-L002811](../../agents/web_agent.py#L2811) | 2811 | `""` | — |
| [SRC-1AE03B9EC3-L002812](../../agents/web_agent.py#L2812) | 2812 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L002813](../../agents/web_agent.py#L2813) | 2813 | `"            source.setdefault(\"page_fetch_status\", \"not_attempted\")"` | — |
| [SRC-1AE03B9EC3-L002814](../../agents/web_agent.py#L2814) | 2814 | `"        # Fetch page text only for the best few public URLs; do it concurrently with strict bounds."` | — |
| [SRC-1AE03B9EC3-L002815](../../agents/web_agent.py#L2815) | 2815 | `"        fetch_targets = sources[:MAX_FETCHED_PAGES]"` | — |
| [SRC-1AE03B9EC3-L002816](../../agents/web_agent.py#L2816) | 2816 | `"        for source in fetch_targets:"` | — |
| [SRC-1AE03B9EC3-L002817](../../agents/web_agent.py#L2817) | 2817 | `"            source[\"page_fetch_status\"] = \"attempted\""` | — |
| [SRC-1AE03B9EC3-L002818](../../agents/web_agent.py#L2818) | 2818 | `"        fetched_count = 0"` | — |
| [SRC-1AE03B9EC3-L002819](../../agents/web_agent.py#L2819) | 2819 | `"        if fetch_targets:"` | — |
| [SRC-1AE03B9EC3-L002820](../../agents/web_agent.py#L2820) | 2820 | `"            with ThreadPoolExecutor(max_workers=min(4, len(fetch_targets))) as pool:"` | — |
| [SRC-1AE03B9EC3-L002821](../../agents/web_agent.py#L2821) | 2821 | `"                futures = {"` | — |
| [SRC-1AE03B9EC3-L002822](../../agents/web_agent.py#L2822) | 2822 | `"                    pool.submit(self._fetch_page, source[\"url\"]): source"` | — |
| [SRC-1AE03B9EC3-L002823](../../agents/web_agent.py#L2823) | 2823 | `"                    for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L002824](../../agents/web_agent.py#L2824) | 2824 | `"                }"` | — |
| [SRC-1AE03B9EC3-L002825](../../agents/web_agent.py#L2825) | 2825 | `"                for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002826](../../agents/web_agent.py#L2826) | 2826 | `"                    source = futures[future]"` | — |
| [SRC-1AE03B9EC3-L002827](../../agents/web_agent.py#L2827) | 2827 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L002828](../../agents/web_agent.py#L2828) | 2828 | `"                        fetch_result = future.result()"` | — |
| [SRC-1AE03B9EC3-L002829](../../agents/web_agent.py#L2829) | 2829 | `"                    except RequestBudgetExceeded as exc:"` | — |
| [SRC-1AE03B9EC3-L002830](../../agents/web_agent.py#L2830) | 2830 | `"                        source[\"page_fetch_status\"] = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L002831](../../agents/web_agent.py#L2831) | 2831 | `"                        source[\"page_fetch_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L002832](../../agents/web_agent.py#L2832) | 2832 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002833](../../agents/web_agent.py#L2833) | 2833 | `"                    except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002834](../../agents/web_agent.py#L2834) | 2834 | `"                        source[\"page_fetch_status\"] = \"fetch_failed\""` | — |
| [SRC-1AE03B9EC3-L002835](../../agents/web_agent.py#L2835) | 2835 | `"                        source[\"page_fetch_error_class\"] = type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L002836](../../agents/web_agent.py#L2836) | 2836 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L002837](../../agents/web_agent.py#L2837) | 2837 | `"                    title, page_text = fetch_result"` | — |
| [SRC-1AE03B9EC3-L002838](../../agents/web_agent.py#L2838) | 2838 | `"                    observed_status = getattr(fetch_result, \"status\", None)"` | — |
| [SRC-1AE03B9EC3-L002839](../../agents/web_agent.py#L2839) | 2839 | `"                    error_class = getattr(fetch_result, \"error_class\", None)"` | — |
| [SRC-1AE03B9EC3-L002840](../../agents/web_agent.py#L2840) | 2840 | `"                    if title:"` | — |
| [SRC-1AE03B9EC3-L002841](../../agents/web_agent.py#L2841) | 2841 | `"                        source[\"title\"] = title"` | — |
| [SRC-1AE03B9EC3-L002842](../../agents/web_agent.py#L2842) | 2842 | `"                    if page_text and page_text.strip():"` | — |
| [SRC-1AE03B9EC3-L002843](../../agents/web_agent.py#L2843) | 2843 | `"                        source[\"page_text\"] = page_text"` | — |
| [SRC-1AE03B9EC3-L002844](../../agents/web_agent.py#L2844) | 2844 | `"                        source[\"snippet\"] = page_text[:1800]"` | — |
| [SRC-1AE03B9EC3-L002845](../../agents/web_agent.py#L2845) | 2845 | `"                        source[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L002846](../../agents/web_agent.py#L2846) | 2846 | `"                        source[\"page_fetch_status\"] = ("` | — |
| [SRC-1AE03B9EC3-L002847](../../agents/web_agent.py#L2847) | 2847 | `"                            observed_status"` | — |
| [SRC-1AE03B9EC3-L002848](../../agents/web_agent.py#L2848) | 2848 | `"                            if observed_status in {\"content_extracted\", \"partial_extraction\"}"` | — |
| [SRC-1AE03B9EC3-L002849](../../agents/web_agent.py#L2849) | 2849 | `"                            else \"partial_extraction\""` | — |
| [SRC-1AE03B9EC3-L002850](../../agents/web_agent.py#L2850) | 2850 | `"                            if len(page_text) >= MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L002851](../../agents/web_agent.py#L2851) | 2851 | `"                            else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L002852](../../agents/web_agent.py#L2852) | 2852 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L002853](../../agents/web_agent.py#L2853) | 2853 | `"                        if error_class:"` | — |
| [SRC-1AE03B9EC3-L002854](../../agents/web_agent.py#L2854) | 2854 | `"                            source[\"page_fetch_error_class\"] = str(error_class)[:80]"` | — |
| [SRC-1AE03B9EC3-L002855](../../agents/web_agent.py#L2855) | 2855 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L002856](../../agents/web_agent.py#L2856) | 2856 | `"                            source.pop(\"page_fetch_error_class\", None)"` | — |
| [SRC-1AE03B9EC3-L002857](../../agents/web_agent.py#L2857) | 2857 | `"                        fetched_count += 1"` | — |
| [SRC-1AE03B9EC3-L002858](../../agents/web_agent.py#L2858) | 2858 | `"                        if source[\"page_fetch_status\"] == \"partial_extraction\":"` | — |
| [SRC-1AE03B9EC3-L002859](../../agents/web_agent.py#L2859) | 2859 | `"                            host = urllib.parse.urlparse(source.get(\"url\", \"\")).hostname or \"المصدر\""` | — |
| [SRC-1AE03B9EC3-L002860](../../agents/web_agent.py#L2860) | 2860 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002861](../../agents/web_agent.py#L2861) | 2861 | `"                                f\"استُخرج جزء من نص {host} فقط؛ قد تكون الصفحة أطول من الحد الآمن.\""` | — |
| [SRC-1AE03B9EC3-L002862](../../agents/web_agent.py#L2862) | 2862 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002863](../../agents/web_agent.py#L2863) | 2863 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L002864](../../agents/web_agent.py#L2864) | 2864 | `"                        source[\"page_fetched\"] = False"` | — |
| [SRC-1AE03B9EC3-L002865](../../agents/web_agent.py#L2865) | 2865 | `"                        if observed_status in {"` | — |
| [SRC-1AE03B9EC3-L002866](../../agents/web_agent.py#L2866) | 2866 | `"                            \"rejected_url\", \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L002867](../../agents/web_agent.py#L2867) | 2867 | `"                            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\", \"http_error\","` | — |
| [SRC-1AE03B9EC3-L002868](../../agents/web_agent.py#L2868) | 2868 | `"                            \"unsupported_content_type\", \"page_too_large\", \"network_error\","` | — |
| [SRC-1AE03B9EC3-L002869](../../agents/web_agent.py#L2869) | 2869 | `"                            \"empty_content\", \"no_text_extracted\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002870](../../agents/web_agent.py#L2870) | 2870 | `"                        }:"` | — |
| [SRC-1AE03B9EC3-L002871](../../agents/web_agent.py#L2871) | 2871 | `"                            source[\"page_fetch_status\"] = observed_status"` | — |
| [SRC-1AE03B9EC3-L002872](../../agents/web_agent.py#L2872) | 2872 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L002873](../../agents/web_agent.py#L2873) | 2873 | `"                            source[\"page_fetch_status\"] = \"no_text_extracted\""` | — |
| [SRC-1AE03B9EC3-L002874](../../agents/web_agent.py#L2874) | 2874 | `"                        if error_class:"` | — |
| [SRC-1AE03B9EC3-L002875](../../agents/web_agent.py#L2875) | 2875 | `"                            source[\"page_fetch_error_class\"] = str(error_class)[:80]"` | — |
| [SRC-1AE03B9EC3-L002876](../../agents/web_agent.py#L2876) | 2876 | `"                        host = urllib.parse.urlparse(source.get(\"url\", \"\")).hostname or \"المصدر\""` | — |
| [SRC-1AE03B9EC3-L002877](../../agents/web_agent.py#L2877) | 2877 | `"                        if source[\"page_fetch_status\"] in {\"no_text_extracted\", \"empty_content\"}:"` | — |
| [SRC-1AE03B9EC3-L002878](../../agents/web_agent.py#L2878) | 2878 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002879](../../agents/web_agent.py#L2879) | 2879 | `"                                f\"لم يمكن استخراج نص من {host}؛ جُلبت الصفحة أو جرت محاولة قراءتها لكن قد تكون ديناميكية أو محجوبة.\""` | — |
| [SRC-1AE03B9EC3-L002880](../../agents/web_agent.py#L2880) | 2880 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002881](../../agents/web_agent.py#L2881) | 2881 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L002882](../../agents/web_agent.py#L2882) | 2882 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L002883](../../agents/web_agent.py#L2883) | 2883 | `"                                f\"تعذرت قراءة نص {host} بسبب حالة الجلب: {source['page_fetch_status']}.\""` | — |
| [SRC-1AE03B9EC3-L002884](../../agents/web_agent.py#L2884) | 2884 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002885](../../agents/web_agent.py#L2885) | 2885 | `""` | — |
| [SRC-1AE03B9EC3-L002886](../../agents/web_agent.py#L2886) | 2886 | `"        # Reorder on consensus first, and keep clear machine-readable provenance."` | — |
| [SRC-1AE03B9EC3-L002887](../../agents/web_agent.py#L2887) | 2887 | `"        sources.sort(key=lambda source: source.get(\"rank_score\", 0), reverse=True)"` | — |
| [SRC-1AE03B9EC3-L002888](../../agents/web_agent.py#L2888) | 2888 | `"        providers = sorted({"` | — |
| [SRC-1AE03B9EC3-L002889](../../agents/web_agent.py#L2889) | 2889 | `"            provider"` | — |
| [SRC-1AE03B9EC3-L002890](../../agents/web_agent.py#L2890) | 2890 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L002891](../../agents/web_agent.py#L2891) | 2891 | `"            for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L002892](../../agents/web_agent.py#L2892) | 2892 | `"        })"` | — |
| [SRC-1AE03B9EC3-L002893](../../agents/web_agent.py#L2893) | 2893 | `"        platform_counts: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L002894](../../agents/web_agent.py#L2894) | 2894 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L002895](../../agents/web_agent.py#L2895) | 2895 | `"            label = source.get(\"platform\", \"web\")"` | — |
| [SRC-1AE03B9EC3-L002896](../../agents/web_agent.py#L2896) | 2896 | `"            platform_counts[label] = platform_counts.get(label, 0) + 1"` | — |
| [SRC-1AE03B9EC3-L002897](../../agents/web_agent.py#L2897) | 2897 | `"        page_failure_statuses = {"` | — |
| [SRC-1AE03B9EC3-L002898](../../agents/web_agent.py#L2898) | 2898 | `"            \"fetch_failed\", \"no_text_extracted\", \"rejected_url\","` | — |
| [SRC-1AE03B9EC3-L002899](../../agents/web_agent.py#L2899) | 2899 | `"            \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L002900](../../agents/web_agent.py#L2900) | 2900 | `"            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\","` | — |
| [SRC-1AE03B9EC3-L002901](../../agents/web_agent.py#L2901) | 2901 | `"            \"http_error\", \"unsupported_content_type\", \"page_too_large\","` | — |
| [SRC-1AE03B9EC3-L002902](../../agents/web_agent.py#L2902) | 2902 | `"            \"network_error\", \"empty_content\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002903](../../agents/web_agent.py#L2903) | 2903 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002904](../../agents/web_agent.py#L2904) | 2904 | `"        page_status_values = ("` | — |
| [SRC-1AE03B9EC3-L002905](../../agents/web_agent.py#L2905) | 2905 | `"            \"not_attempted\", \"attempted\", \"content_extracted\", \"partial_extraction\","` | — |
| [SRC-1AE03B9EC3-L002906](../../agents/web_agent.py#L2906) | 2906 | `"            \"no_text_extracted\", \"fetch_failed\", \"rejected_url\","` | — |
| [SRC-1AE03B9EC3-L002907](../../agents/web_agent.py#L2907) | 2907 | `"            \"blocked_or_unresolved_host\", \"blocked_connection_target\","` | — |
| [SRC-1AE03B9EC3-L002908](../../agents/web_agent.py#L2908) | 2908 | `"            \"redirect_failed\", \"redirect_rejected\", \"redirect_limit\","` | — |
| [SRC-1AE03B9EC3-L002909](../../agents/web_agent.py#L2909) | 2909 | `"            \"http_error\", \"unsupported_content_type\", \"page_too_large\","` | — |
| [SRC-1AE03B9EC3-L002910](../../agents/web_agent.py#L2910) | 2910 | `"            \"network_error\", \"empty_content\", \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L002911](../../agents/web_agent.py#L2911) | 2911 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002912](../../agents/web_agent.py#L2912) | 2912 | `"        page_fetch_status_counts = {"` | — |
| [SRC-1AE03B9EC3-L002913](../../agents/web_agent.py#L2913) | 2913 | `"            status: sum(source.get(\"page_fetch_status\") == status for source in fetch_targets)"` | — |
| [SRC-1AE03B9EC3-L002914](../../agents/web_agent.py#L2914) | 2914 | `"            for status in page_status_values"` | — |
| [SRC-1AE03B9EC3-L002915](../../agents/web_agent.py#L2915) | 2915 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002916](../../agents/web_agent.py#L2916) | 2916 | `"        provider_diagnostics = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L002917](../../agents/web_agent.py#L2917) | 2917 | `"        provider_candidates_received = sum("` | — |
| [SRC-1AE03B9EC3-L002918](../../agents/web_agent.py#L2918) | 2918 | `"            max(0, int(row.get(\"result_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002919](../../agents/web_agent.py#L2919) | 2919 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L002920](../../agents/web_agent.py#L2920) | 2920 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002921](../../agents/web_agent.py#L2921) | 2921 | `"        provider_candidates_accepted = sum("` | — |
| [SRC-1AE03B9EC3-L002922](../../agents/web_agent.py#L2922) | 2922 | `"            max(0, int(row.get(\"accepted_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002923](../../agents/web_agent.py#L2923) | 2923 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L002924](../../agents/web_agent.py#L2924) | 2924 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002925](../../agents/web_agent.py#L2925) | 2925 | `"        provider_candidates_rejected = sum("` | — |
| [SRC-1AE03B9EC3-L002926](../../agents/web_agent.py#L2926) | 2926 | `"            max(0, int(row.get(\"rejected_count\", 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L002927](../../agents/web_agent.py#L2927) | 2927 | `"            for row in provider_diagnostics if isinstance(row, dict)"` | — |
| [SRC-1AE03B9EC3-L002928](../../agents/web_agent.py#L2928) | 2928 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002929](../../agents/web_agent.py#L2929) | 2929 | `"        report = {"` | — |
| [SRC-1AE03B9EC3-L002930](../../agents/web_agent.py#L2930) | 2930 | `"            \"raw_results\": raw_results_count,"` | — |
| [SRC-1AE03B9EC3-L002931](../../agents/web_agent.py#L2931) | 2931 | `"            \"provider_candidates_received\": provider_candidates_received,"` | — |
| [SRC-1AE03B9EC3-L002932](../../agents/web_agent.py#L2932) | 2932 | `"            \"provider_candidates_accepted\": provider_candidates_accepted,"` | — |
| [SRC-1AE03B9EC3-L002933](../../agents/web_agent.py#L2933) | 2933 | `"            \"provider_candidates_rejected\": provider_candidates_rejected,"` | — |
| [SRC-1AE03B9EC3-L002934](../../agents/web_agent.py#L2934) | 2934 | `"            \"unique_urls\": len({"` | — |
| [SRC-1AE03B9EC3-L002935](../../agents/web_agent.py#L2935) | 2935 | `"                self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L002936](../../agents/web_agent.py#L2936) | 2936 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L002937](../../agents/web_agent.py#L2937) | 2937 | `"                if self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L002938](../../agents/web_agent.py#L2938) | 2938 | `"            }),"` | — |
| [SRC-1AE03B9EC3-L002939](../../agents/web_agent.py#L2939) | 2939 | `"            \"pages_content_extracted\": fetched_count,"` | — |
| [SRC-1AE03B9EC3-L002940](../../agents/web_agent.py#L2940) | 2940 | `"            \"pages_partial_extracted\": sum("` | — |
| [SRC-1AE03B9EC3-L002941](../../agents/web_agent.py#L2941) | 2941 | `"                source.get(\"page_fetch_status\") == \"partial_extraction\""` | — |
| [SRC-1AE03B9EC3-L002942](../../agents/web_agent.py#L2942) | 2942 | `"                for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L002943](../../agents/web_agent.py#L2943) | 2943 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L002944](../../agents/web_agent.py#L2944) | 2944 | `"            \"pages_extract_failed\": sum("` | — |
| [SRC-1AE03B9EC3-L002945](../../agents/web_agent.py#L2945) | 2945 | `"                source.get(\"page_fetch_status\") in page_failure_statuses"` | — |
| [SRC-1AE03B9EC3-L002946](../../agents/web_agent.py#L2946) | 2946 | `"                for source in fetch_targets"` | — |
| [SRC-1AE03B9EC3-L002947](../../agents/web_agent.py#L2947) | 2947 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L002948](../../agents/web_agent.py#L2948) | 2948 | `"            \"page_fetch_status_counts\": page_fetch_status_counts,"` | — |
| [SRC-1AE03B9EC3-L002949](../../agents/web_agent.py#L2949) | 2949 | `"            \"queries_planned\": len(queries),"` | — |
| [SRC-1AE03B9EC3-L002950](../../agents/web_agent.py#L2950) | 2950 | `"            \"queries_attempted\": search_started_queries,"` | — |
| [SRC-1AE03B9EC3-L002951](../../agents/web_agent.py#L2951) | 2951 | `"            \"query_results\": query_counts,"` | — |
| [SRC-1AE03B9EC3-L002952](../../agents/web_agent.py#L2952) | 2952 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L002953](../../agents/web_agent.py#L2953) | 2953 | `"            \"pages_fetched\": fetched_count,"` | — |
| [SRC-1AE03B9EC3-L002954](../../agents/web_agent.py#L2954) | 2954 | `"            \"providers_used\": providers,"` | — |
| [SRC-1AE03B9EC3-L002955](../../agents/web_agent.py#L2955) | 2955 | `"            \"provider_counts\": {"` | — |
| [SRC-1AE03B9EC3-L002956](../../agents/web_agent.py#L2956) | 2956 | `"                provider: sum(provider in source.get(\"providers\", []) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L002957](../../agents/web_agent.py#L2957) | 2957 | `"                for provider in providers"` | — |
| [SRC-1AE03B9EC3-L002958](../../agents/web_agent.py#L2958) | 2958 | `"            },"` | — |
| [SRC-1AE03B9EC3-L002959](../../agents/web_agent.py#L2959) | 2959 | `"            \"platform_counts\": platform_counts,"` | — |
| [SRC-1AE03B9EC3-L002960](../../agents/web_agent.py#L2960) | 2960 | `"            \"social_direct_results\": len(social_results),"` | — |
| [SRC-1AE03B9EC3-L002961](../../agents/web_agent.py#L2961) | 2961 | `"            \"expansion_queries\": expansion_queries,"` | — |
| [SRC-1AE03B9EC3-L002962](../../agents/web_agent.py#L2962) | 2962 | `"            \"evidence_signals\": evidence_signal_report(sources, plan.get(\"freshness\", \"any\")),"` | — |
| [SRC-1AE03B9EC3-L002963](../../agents/web_agent.py#L2963) | 2963 | `"            \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L002964](../../agents/web_agent.py#L2964) | 2964 | `"            \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L002965](../../agents/web_agent.py#L2965) | 2965 | `"            \"dialogue_context\": plan.get(\"dialogue_context\", {}),"` | — |
| [SRC-1AE03B9EC3-L002966](../../agents/web_agent.py#L2966) | 2966 | `"            \"provider_diagnostics\": provider_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L002967](../../agents/web_agent.py#L2967) | 2967 | `"            \"connector_summary\": self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L002968](../../agents/web_agent.py#L2968) | 2968 | `"                provider_diagnostics, sources"` | — |
| [SRC-1AE03B9EC3-L002969](../../agents/web_agent.py#L2969) | 2969 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L002970](../../agents/web_agent.py#L2970) | 2970 | `"            \"pages_fetch_attempted\": len(fetch_targets),"` | — |
| [SRC-1AE03B9EC3-L002971](../../agents/web_agent.py#L2971) | 2971 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002972](../../agents/web_agent.py#L2972) | 2972 | `"        coverage_targets = plan.get(\"coverage_targets\") or []"` | — |
| [SRC-1AE03B9EC3-L002973](../../agents/web_agent.py#L2973) | 2973 | `"        if isinstance(coverage_targets, list) and coverage_targets:"` | — |
| [SRC-1AE03B9EC3-L002974](../../agents/web_agent.py#L2974) | 2974 | `"            safe_targets = ["` | — |
| [SRC-1AE03B9EC3-L002975](../../agents/web_agent.py#L2975) | 2975 | `"                target[:120]"` | — |
| [SRC-1AE03B9EC3-L002976](../../agents/web_agent.py#L2976) | 2976 | `"                for target in coverage_targets"` | — |
| [SRC-1AE03B9EC3-L002977](../../agents/web_agent.py#L2977) | 2977 | `"                if isinstance(target, str) and target.strip()"` | — |
| [SRC-1AE03B9EC3-L002978](../../agents/web_agent.py#L2978) | 2978 | `"            ][:8]"` | — |
| [SRC-1AE03B9EC3-L002979](../../agents/web_agent.py#L2979) | 2979 | `"            ledger = build_evidence_ledger(safe_targets, sources)"` | — |
| [SRC-1AE03B9EC3-L002980](../../agents/web_agent.py#L2980) | 2980 | `"            report[\"aspects\"] = safe_targets"` | — |
| [SRC-1AE03B9EC3-L002981](../../agents/web_agent.py#L2981) | 2981 | `"            report[\"evidence_ledger\"] = ledger"` | — |
| [SRC-1AE03B9EC3-L002982](../../agents/web_agent.py#L2982) | 2982 | `"            report[\"aspect_diagnostics_ar\"] = arabic_aspect_diagnostics(ledger)"` | — |
| [SRC-1AE03B9EC3-L002983](../../agents/web_agent.py#L2983) | 2983 | `"            report[\"aspect_evidence_gaps\"] = list(ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L002984](../../agents/web_agent.py#L2984) | 2984 | `"            report[\"aspect_coverage_lexical_ratio\"] = ledger.get(\"coverage_ratio\")"` | — |
| [SRC-1AE03B9EC3-L002985](../../agents/web_agent.py#L2985) | 2985 | `"            report[\"aspect_coverage_is_not_truth_score\"] = True"` | — |
| [SRC-1AE03B9EC3-L002986](../../agents/web_agent.py#L2986) | 2986 | `""` | — |
| [SRC-1AE03B9EC3-L002987](../../agents/web_agent.py#L2987) | 2987 | `"        return sources, list(dict.fromkeys(warnings)), report"` | — |
| [SRC-1AE03B9EC3-L002988](../../agents/web_agent.py#L2988) | 2988 | `""` | — |
| [SRC-1AE03B9EC3-L002989](../../agents/web_agent.py#L2989) | 2989 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L002990](../../agents/web_agent.py#L2990) | 2990 | `"    def _history_search_query(question: str, history: list[dict[str, str]]) -> str:"` | — |
| [SRC-1AE03B9EC3-L002991](../../agents/web_agent.py#L2991) | 2991 | `"        \"\"\"Backward-compatible wrapper for the shared follow-up resolver.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002992](../../agents/web_agent.py#L2992) | 2992 | `"        return resolve_followup_query(question, history)"` | — |
| [SRC-1AE03B9EC3-L002993](../../agents/web_agent.py#L2993) | 2993 | `""` | — |
| [SRC-1AE03B9EC3-L002994](../../agents/web_agent.py#L2994) | 2994 | `"    def _connector_status_summary(self, diagnostics: list[dict[str, Any]] \| None,"` | — |
| [SRC-1AE03B9EC3-L002995](../../agents/web_agent.py#L2995) | 2995 | `"                                  sources: list[dict[str, Any]] \| None = None) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L002996](../../agents/web_agent.py#L2996) | 2996 | `"        \"\"\"Summarize this request's connector states without exposing credentials.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002997](../../agents/web_agent.py#L2997) | 2997 | `"        optional = {"` | — |
| [SRC-1AE03B9EC3-L002998](../../agents/web_agent.py#L2998) | 2998 | `"            \"deepseek_search_api\": (\"DEEPSEEK_SEARCH_API_KEY\",), \"brave_search_api\": (\"BRAVE_SEARCH_API_KEY\",),"` | — |
| [SRC-1AE03B9EC3-L002999](../../agents/web_agent.py#L2999) | 2999 | `"            \"tavily_search_api\": (\"TAVILY_API_KEY\",), \"reddit_oauth_api\": (\"REDDIT_CLIENT_ID\", \"REDDIT_CLIENT_SECRET\"),"` | — |
| [SRC-1AE03B9EC3-L003000](../../agents/web_agent.py#L3000) | 3000 | `"            \"facebook_pages_api\": (\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"FACEBOOK_PAGE_IDS\"),"` | — |
| [SRC-1AE03B9EC3-L003001](../../agents/web_agent.py#L3001) | 3001 | `"            \"instagram_graph_api\": (\"INSTAGRAM_USER_ID\", \"INSTAGRAM_ACCESS_TOKEN\"),"` | — |
| [SRC-1AE03B9EC3-L003002](../../agents/web_agent.py#L3002) | 3002 | `"            \"x_official_api\": (\"X_BEARER_TOKEN\",), \"youtube_data_api\": (\"YOUTUBE_API_KEY\",),"` | — |
| [SRC-1AE03B9EC3-L003003](../../agents/web_agent.py#L3003) | 3003 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003004](../../agents/web_agent.py#L3004) | 3004 | `"        config: dict[str, tuple[bool, str]] = {"` | — |
| [SRC-1AE03B9EC3-L003005](../../agents/web_agent.py#L3005) | 3005 | `"            \"duckduckgo_html\": (True, \"built_in_no_api_key\"), \"bing_rss\": (True, \"built_in_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L003006](../../agents/web_agent.py#L3006) | 3006 | `"            \"google_news_rss\": (True, \"built_in_conditional_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L003007](../../agents/web_agent.py#L3007) | 3007 | `"            \"openalex\": (True, \"built_in_free_academic\"),"` | — |
| [SRC-1AE03B9EC3-L003008](../../agents/web_agent.py#L3008) | 3008 | `"            \"arxiv\": (True, \"built_in_free_academic\"),"` | — |
| [SRC-1AE03B9EC3-L003009](../../agents/web_agent.py#L3009) | 3009 | `"            \"crossref\": (True, \"built_in_free_academic\"),"` | — |
| [SRC-1AE03B9EC3-L003010](../../agents/web_agent.py#L3010) | 3010 | `"            \"reddit_public_rss\": (True, \"built_in_no_api_key\"), \"bluesky_public_search\": (True, \"built_in_no_api_key\"),"` | — |
| [SRC-1AE03B9EC3-L003011](../../agents/web_agent.py#L3011) | 3011 | `"            \"openrouter_web_search\": (bool(self.openrouter_web_search_enabled),"` | — |
| [SRC-1AE03B9EC3-L003012](../../agents/web_agent.py#L3012) | 3012 | `"                \"enabled\" if self.openrouter_web_search_enabled else \"disabled\"),"` | — |
| [SRC-1AE03B9EC3-L003013](../../agents/web_agent.py#L3013) | 3013 | `"            \"user_supplied_url\": (True, \"request_driven\"),"` | — |
| [SRC-1AE03B9EC3-L003014](../../agents/web_agent.py#L3014) | 3014 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003015](../../agents/web_agent.py#L3015) | 3015 | `"        for name, keys in optional.items():"` | — |
| [SRC-1AE03B9EC3-L003016](../../agents/web_agent.py#L3016) | 3016 | `"            ready = all(bool(os.getenv(key, \"\").strip()) for key in keys)"` | — |
| [SRC-1AE03B9EC3-L003017](../../agents/web_agent.py#L3017) | 3017 | `"            config[name] = (ready, \"configured\" if ready else \"not_configured\")"` | — |
| [SRC-1AE03B9EC3-L003018](../../agents/web_agent.py#L3018) | 3018 | `"        grouped: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-1AE03B9EC3-L003019](../../agents/web_agent.py#L3019) | 3019 | `"        for item in diagnostics or []:"` | — |
| [SRC-1AE03B9EC3-L003020](../../agents/web_agent.py#L3020) | 3020 | `"            if isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L003021](../../agents/web_agent.py#L3021) | 3021 | `"                name = _clean_text(item.get(\"provider\", \"unknown\"), 80) or \"unknown\""` | — |
| [SRC-1AE03B9EC3-L003022](../../agents/web_agent.py#L3022) | 3022 | `"                grouped.setdefault(name, []).append(item)"` | — |
| [SRC-1AE03B9EC3-L003023](../../agents/web_agent.py#L3023) | 3023 | `"        useful: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L003024](../../agents/web_agent.py#L3024) | 3024 | `"        for source in sources or []:"` | — |
| [SRC-1AE03B9EC3-L003025](../../agents/web_agent.py#L3025) | 3025 | `"            if not isinstance(source, dict):"` | — |
| [SRC-1AE03B9EC3-L003026](../../agents/web_agent.py#L3026) | 3026 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L003027](../../agents/web_agent.py#L3027) | 3027 | `"            providers = source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L003028](../../agents/web_agent.py#L3028) | 3028 | `"            if isinstance(providers, str):"` | — |
| [SRC-1AE03B9EC3-L003029](../../agents/web_agent.py#L3029) | 3029 | `"                providers = [providers]"` | — |
| [SRC-1AE03B9EC3-L003030](../../agents/web_agent.py#L3030) | 3030 | `"            if not isinstance(providers, list):"` | — |
| [SRC-1AE03B9EC3-L003031](../../agents/web_agent.py#L3031) | 3031 | `"                providers = []"` | — |
| [SRC-1AE03B9EC3-L003032](../../agents/web_agent.py#L3032) | 3032 | `"            if isinstance(source.get(\"provider\"), str):"` | — |
| [SRC-1AE03B9EC3-L003033](../../agents/web_agent.py#L3033) | 3033 | `"                providers = providers + [source[\"provider\"]]"` | — |
| [SRC-1AE03B9EC3-L003034](../../agents/web_agent.py#L3034) | 3034 | `"            for name in {str(value) for value in providers if value}:"` | — |
| [SRC-1AE03B9EC3-L003035](../../agents/web_agent.py#L3035) | 3035 | `"                useful[name] = useful.get(name, 0) + 1"` | — |
| [SRC-1AE03B9EC3-L003036](../../agents/web_agent.py#L3036) | 3036 | `"        priority = {\"ok\": 0, \"no_results\": 1, \"filtered_all\": 2, \"not_attempted\": 3,"` | — |
| [SRC-1AE03B9EC3-L003037](../../agents/web_agent.py#L3037) | 3037 | `"                    \"disabled\": 4, \"not_configured\": 5, \"budget_exhausted\": 6,"` | — |
| [SRC-1AE03B9EC3-L003038](../../agents/web_agent.py#L3038) | 3038 | `"                    \"unknown\": 6, \"rate_limited\": 7, \"unauthorized\": 8, \"http_error\": 9,"` | — |
| [SRC-1AE03B9EC3-L003039](../../agents/web_agent.py#L3039) | 3039 | `"                    \"timeout\": 10, \"failed\": 11, \"error\": 11}"` | — |
| [SRC-1AE03B9EC3-L003040](../../agents/web_agent.py#L3040) | 3040 | `"        confirmed_attempt_statuses = _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES \| {"` | — |
| [SRC-1AE03B9EC3-L003041](../../agents/web_agent.py#L3041) | 3041 | `"            \"http_error\", \"unauthorized\", \"rate_limited\", \"invalid_response\""` | — |
| [SRC-1AE03B9EC3-L003042](../../agents/web_agent.py#L3042) | 3042 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003043](../../agents/web_agent.py#L3043) | 3043 | `"        uncertain_attempt_statuses = {\"timeout\", \"failed\", \"error\", \"unknown\", \"inconclusive\"}"` | — |
| [SRC-1AE03B9EC3-L003044](../../agents/web_agent.py#L3044) | 3044 | `""` | — |
| [SRC-1AE03B9EC3-L003045](../../agents/web_agent.py#L3045) | 3045 | `"        def redact(value: Any) -> str:"` | — |
| [SRC-1AE03B9EC3-L003046](../../agents/web_agent.py#L3046) | 3046 | `"            safe = _clean_text(str(value or \"\"), 180)"` | — |
| [SRC-1AE03B9EC3-L003047](../../agents/web_agent.py#L3047) | 3047 | `"            safe = re.sub(r\"(?i)(bearer\\s+)[A-Za-z0-9._~+/-]+=*\", r\"\\1[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L003048](../../agents/web_agent.py#L3048) | 3048 | `"            safe = re.sub(r\"(?i)\\b(api[_-]?key\|access[_-]?token\|refresh[_-]?token\|token\|secret\|password)\\s*[:=]\\s*[^\\s,;]+\", r\"\\1=[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L003049](../../agents/web_agent.py#L3049) | 3049 | `"            safe = re.sub(r\"(?i)([?&](?:api[_-]?key\|access[_-]?token\|token\|key)=)[^&\\s]+\", r\"\\1[REDACTED]\", safe)"` | — |
| [SRC-1AE03B9EC3-L003050](../../agents/web_agent.py#L3050) | 3050 | `"            return safe[:180]"` | — |
| [SRC-1AE03B9EC3-L003051](../../agents/web_agent.py#L3051) | 3051 | `""` | — |
| [SRC-1AE03B9EC3-L003052](../../agents/web_agent.py#L3052) | 3052 | `"        names = set(config) \| set(grouped) \| set(useful)"` | — |
| [SRC-1AE03B9EC3-L003053](../../agents/web_agent.py#L3053) | 3053 | `"        connectors = []"` | — |
| [SRC-1AE03B9EC3-L003054](../../agents/web_agent.py#L3054) | 3054 | `"        for name in sorted(names):"` | — |
| [SRC-1AE03B9EC3-L003055](../../agents/web_agent.py#L3055) | 3055 | `"            ready, config_status = config.get(name, (bool(grouped.get(name) or useful.get(name)), \"observed_in_code_path\"))"` | — |
| [SRC-1AE03B9EC3-L003056](../../agents/web_agent.py#L3056) | 3056 | `"            attempts = grouped.get(name, [])"` | — |
| [SRC-1AE03B9EC3-L003057](../../agents/web_agent.py#L3057) | 3057 | `"            statuses = [_clean_text(row.get(\"status\", \"unknown\"), 40).lower() or \"unknown\" for row in attempts]"` | — |
| [SRC-1AE03B9EC3-L003058](../../agents/web_agent.py#L3058) | 3058 | `"            status = max(statuses, key=lambda value: priority.get(value, 6)) if statuses else ("` | — |
| [SRC-1AE03B9EC3-L003059](../../agents/web_agent.py#L3059) | 3059 | `"                \"ok\" if useful.get(name, 0) else \"not_configured\" if not ready else \"not_attempted\")"` | — |
| [SRC-1AE03B9EC3-L003060](../../agents/web_agent.py#L3060) | 3060 | `"            if any(value in confirmed_attempt_statuses for value in statuses) or useful.get(name, 0):"` | — |
| [SRC-1AE03B9EC3-L003061](../../agents/web_agent.py#L3061) | 3061 | `"                attempted: bool \| None = True"` | — |
| [SRC-1AE03B9EC3-L003062](../../agents/web_agent.py#L3062) | 3062 | `"            elif any(value in uncertain_attempt_statuses for value in statuses):"` | — |
| [SRC-1AE03B9EC3-L003063](../../agents/web_agent.py#L3063) | 3063 | `"                attempted = None"` | — |
| [SRC-1AE03B9EC3-L003064](../../agents/web_agent.py#L3064) | 3064 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L003065](../../agents/web_agent.py#L3065) | 3065 | `"                attempted = False"` | — |
| [SRC-1AE03B9EC3-L003066](../../agents/web_agent.py#L3066) | 3066 | `"            successful_statuses = set(statuses) & _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L003067](../../agents/web_agent.py#L3067) | 3067 | `"            error_response_statuses = set(statuses) & {\"http_error\", \"unauthorized\", \"rate_limited\"}"` | — |
| [SRC-1AE03B9EC3-L003068](../../agents/web_agent.py#L3068) | 3068 | `"            uncertain_failure_statuses = set(statuses) & {\"timeout\", \"failed\", \"error\", \"unknown\", \"inconclusive\"}"` | — |
| [SRC-1AE03B9EC3-L003069](../../agents/web_agent.py#L3069) | 3069 | `"            failure_observed = bool(error_response_statuses or uncertain_failure_statuses or \"budget_exhausted\" in statuses)"` | — |
| [SRC-1AE03B9EC3-L003070](../../agents/web_agent.py#L3070) | 3070 | `"            available: bool \| None = ("` | — |
| [SRC-1AE03B9EC3-L003071](../../agents/web_agent.py#L3071) | 3071 | `"                True if successful_statuses or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L003072](../../agents/web_agent.py#L3072) | 3072 | `"                else False if error_response_statuses or not ready or \"disabled\" in statuses or \"budget_exhausted\" in statuses"` | — |
| [SRC-1AE03B9EC3-L003073](../../agents/web_agent.py#L3073) | 3073 | `"                else None"` | — |
| [SRC-1AE03B9EC3-L003074](../../agents/web_agent.py#L3074) | 3074 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003075](../../agents/web_agent.py#L3075) | 3075 | `"            verified: bool \| None = ("` | — |
| [SRC-1AE03B9EC3-L003076](../../agents/web_agent.py#L3076) | 3076 | `"                True if successful_statuses or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L003077](../../agents/web_agent.py#L3077) | 3077 | `"                else False if error_response_statuses"` | — |
| [SRC-1AE03B9EC3-L003078](../../agents/web_agent.py#L3078) | 3078 | `"                else None"` | — |
| [SRC-1AE03B9EC3-L003079](../../agents/web_agent.py#L3079) | 3079 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003080](../../agents/web_agent.py#L3080) | 3080 | `"            implementation_status = ("` | — |
| [SRC-1AE03B9EC3-L003081](../../agents/web_agent.py#L3081) | 3081 | `"                \"implemented_in_code\" if name in config"` | — |
| [SRC-1AE03B9EC3-L003082](../../agents/web_agent.py#L3082) | 3082 | `"                else \"observed_runtime_path\" if attempts or useful.get(name, 0)"` | — |
| [SRC-1AE03B9EC3-L003083](../../agents/web_agent.py#L3083) | 3083 | `"                else \"unknown\""` | — |
| [SRC-1AE03B9EC3-L003084](../../agents/web_agent.py#L3084) | 3084 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003085](../../agents/web_agent.py#L3085) | 3085 | `"            queries = list(dict.fromkeys(_clean_text(row.get(\"query\", \"\"), 180) for row in attempts if row.get(\"query\")))[:3]"` | — |
| [SRC-1AE03B9EC3-L003086](../../agents/web_agent.py#L3086) | 3086 | `"            errors = list(dict.fromkeys(redact(row.get(\"error\")) for row in attempts if row.get(\"error\")))[:3]"` | — |
| [SRC-1AE03B9EC3-L003087](../../agents/web_agent.py#L3087) | 3087 | `"            result_count = sum(max(0, int(row.get(\"result_count\", 0) or 0)) for row in attempts)"` | — |
| [SRC-1AE03B9EC3-L003088](../../agents/web_agent.py#L3088) | 3088 | `"            accepted_count = sum("` | — |
