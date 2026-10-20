# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **004**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L000345 إلى SRC-1AE03B9EC3-L001144
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L000345](../../agents/web_agent.py#L345) | 345 | `"            os.getenv(\"OMARAI_LLM_FALLBACK_MODEL\", \"\").strip() or \"openrouter/free\""` | — |
| [SRC-1AE03B9EC3-L000346](../../agents/web_agent.py#L346) | 346 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000347](../../agents/web_agent.py#L347) | 347 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L000348](../../agents/web_agent.py#L348) | 348 | `"            \"web_search_ready\": search_ready,"` | — |
| [SRC-1AE03B9EC3-L000349](../../agents/web_agent.py#L349) | 349 | `"            \"language_model_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000350](../../agents/web_agent.py#L350) | 350 | `"                os.getenv(\"OMARAI_LLM_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000351](../../agents/web_agent.py#L351) | 351 | `"                or os.getenv(\"OPENROUTER_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000352](../../agents/web_agent.py#L352) | 352 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000353](../../agents/web_agent.py#L353) | 353 | `"            \"language_model_provider\": os.getenv("` | — |
| [SRC-1AE03B9EC3-L000354](../../agents/web_agent.py#L354) | 354 | `"                \"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\""` | — |
| [SRC-1AE03B9EC3-L000355](../../agents/web_agent.py#L355) | 355 | `"            ).strip().rstrip(\"/\"),"` | — |
| [SRC-1AE03B9EC3-L000356](../../agents/web_agent.py#L356) | 356 | `"            \"default_model\": answer_model,"` | — |
| [SRC-1AE03B9EC3-L000357](../../agents/web_agent.py#L357) | 357 | `"            \"planner_model\": planner_model,"` | — |
| [SRC-1AE03B9EC3-L000358](../../agents/web_agent.py#L358) | 358 | `"            \"answer_model\": answer_model,"` | — |
| [SRC-1AE03B9EC3-L000359](../../agents/web_agent.py#L359) | 359 | `"            \"review_model\": review_model,"` | — |
| [SRC-1AE03B9EC3-L000360](../../agents/web_agent.py#L360) | 360 | `"            \"fallback_model\": fallback_model,"` | — |
| [SRC-1AE03B9EC3-L000361](../../agents/web_agent.py#L361) | 361 | `"            \"model_selection_mode\": \"role_specific_with_fallback\","` | — |
| [SRC-1AE03B9EC3-L000362](../../agents/web_agent.py#L362) | 362 | `"            \"external_model_privacy_notice\": ("` | — |
| [SRC-1AE03B9EC3-L000363](../../agents/web_agent.py#L363) | 363 | `"                \"Prompts and selected page excerpts are sent to the configured external model provider. \""` | — |
| [SRC-1AE03B9EC3-L000364](../../agents/web_agent.py#L364) | 364 | `"                \"Do not submit secrets or personal/confidential customer data. The default free NVIDIA \""` | — |
| [SRC-1AE03B9EC3-L000365](../../agents/web_agent.py#L365) | 365 | `"                \"Nemotron endpoint states that sessions may be logged for security and product improvement.\""` | — |
| [SRC-1AE03B9EC3-L000366](../../agents/web_agent.py#L366) | 366 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000367](../../agents/web_agent.py#L367) | 367 | `"            \"search_providers\": ["` | — |
| [SRC-1AE03B9EC3-L000368](../../agents/web_agent.py#L368) | 368 | `"                \"DuckDuckGo HTML\","` | — |
| [SRC-1AE03B9EC3-L000369](../../agents/web_agent.py#L369) | 369 | `"                \"Bing RSS\","` | — |
| [SRC-1AE03B9EC3-L000370](../../agents/web_agent.py#L370) | 370 | `"                \"Google News RSS for fresh queries\","` | — |
| [SRC-1AE03B9EC3-L000371](../../agents/web_agent.py#L371) | 371 | `"                \"DeepSeek Search API when DEEPSEEK_SEARCH_API_KEY is configured (optional; may incur charges)\","` | — |
| [SRC-1AE03B9EC3-L000372](../../agents/web_agent.py#L372) | 372 | `"                \"OpenRouter server-side live web search when OMARAI_OPENROUTER_WEB_SEARCH=1\","` | — |
| [SRC-1AE03B9EC3-L000373](../../agents/web_agent.py#L373) | 373 | `"                \"Brave Search API when BRAVE_SEARCH_API_KEY is configured\","` | — |
| [SRC-1AE03B9EC3-L000374](../../agents/web_agent.py#L374) | 374 | `"                \"Tavily Search API when TAVILY_API_KEY is configured\","` | — |
| [SRC-1AE03B9EC3-L000375](../../agents/web_agent.py#L375) | 375 | `"            ],"` | — |
| [SRC-1AE03B9EC3-L000376](../../agents/web_agent.py#L376) | 376 | `"            \"brave_search_api_configured\": bool(os.getenv(\"BRAVE_SEARCH_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000377](../../agents/web_agent.py#L377) | 377 | `"            \"deepseek_search_api_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000378](../../agents/web_agent.py#L378) | 378 | `"                os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000379](../../agents/web_agent.py#L379) | 379 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000380](../../agents/web_agent.py#L380) | 380 | `"            \"tavily_search_api_configured\": bool(os.getenv(\"TAVILY_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000381](../../agents/web_agent.py#L381) | 381 | `"            \"openrouter_web_search_enabled\": ("` | — |
| [SRC-1AE03B9EC3-L000382](../../agents/web_agent.py#L382) | 382 | `"                os.getenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"\").strip() == \"1\""` | — |
| [SRC-1AE03B9EC3-L000383](../../agents/web_agent.py#L383) | 383 | `"                and \"openrouter.ai\" in os.getenv("` | — |
| [SRC-1AE03B9EC3-L000384](../../agents/web_agent.py#L384) | 384 | `"                    \"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\""` | — |
| [SRC-1AE03B9EC3-L000385](../../agents/web_agent.py#L385) | 385 | `"                ).lower()"` | — |
| [SRC-1AE03B9EC3-L000386](../../agents/web_agent.py#L386) | 386 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000387](../../agents/web_agent.py#L387) | 387 | `"            \"public_social_sources\": ["` | — |
| [SRC-1AE03B9EC3-L000388](../../agents/web_agent.py#L388) | 388 | `"                \"Reddit public RSS and optional authorized Reddit OAuth search\","` | — |
| [SRC-1AE03B9EC3-L000389](../../agents/web_agent.py#L389) | 389 | `"                \"Bluesky public search\","` | — |
| [SRC-1AE03B9EC3-L000390](../../agents/web_agent.py#L390) | 390 | `"                \"indexed public pages from Facebook, Instagram, X, TikTok, LinkedIn, Threads and YouTube\","` | — |
| [SRC-1AE03B9EC3-L000391](../../agents/web_agent.py#L391) | 391 | `"                \"official Instagram public hashtag media when an authorized Graph API token is configured\","` | — |
| [SRC-1AE03B9EC3-L000392](../../agents/web_agent.py#L392) | 392 | `"                \"configured Facebook Pages when a valid authorized page token is configured\","` | — |
| [SRC-1AE03B9EC3-L000393](../../agents/web_agent.py#L393) | 393 | `"                \"official X recent-post API when X_BEARER_TOKEN is configured\","` | — |
| [SRC-1AE03B9EC3-L000394](../../agents/web_agent.py#L394) | 394 | `"            ],"` | — |
| [SRC-1AE03B9EC3-L000395](../../agents/web_agent.py#L395) | 395 | `"            \"reddit_oauth_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000396](../../agents/web_agent.py#L396) | 396 | `"                os.getenv(\"REDDIT_CLIENT_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000397](../../agents/web_agent.py#L397) | 397 | `"                and os.getenv(\"REDDIT_CLIENT_SECRET\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000398](../../agents/web_agent.py#L398) | 398 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000399](../../agents/web_agent.py#L399) | 399 | `"            \"facebook_pages_api_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000400](../../agents/web_agent.py#L400) | 400 | `"                os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000401](../../agents/web_agent.py#L401) | 401 | `"                and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000402](../../agents/web_agent.py#L402) | 402 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000403](../../agents/web_agent.py#L403) | 403 | `"            \"x_api_configured\": bool(os.getenv(\"X_BEARER_TOKEN\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000404](../../agents/web_agent.py#L404) | 404 | `"            \"instagram_graph_api_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000405](../../agents/web_agent.py#L405) | 405 | `"                os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000406](../../agents/web_agent.py#L406) | 406 | `"                and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000407](../../agents/web_agent.py#L407) | 407 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000408](../../agents/web_agent.py#L408) | 408 | `"            \"meta_graph_version\": os.getenv(\"META_GRAPH_VERSION\", \"v25.0\").strip(),"` | — |
| [SRC-1AE03B9EC3-L000409](../../agents/web_agent.py#L409) | 409 | `"            \"youtube_api_configured\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000410](../../agents/web_agent.py#L410) | 410 | `"            \"youtube_direct_api\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000411](../../agents/web_agent.py#L411) | 411 | `"            \"verification_scope\": {"` | — |
| [SRC-1AE03B9EC3-L000412](../../agents/web_agent.py#L412) | 412 | `"                \"kind\": \"configuration_snapshot\","` | — |
| [SRC-1AE03B9EC3-L000413](../../agents/web_agent.py#L413) | 413 | `"                \"live_network_checks_performed\": False,"` | — |
| [SRC-1AE03B9EC3-L000414](../../agents/web_agent.py#L414) | 414 | `"                \"web_search_ready_means\": \"dependencies_importable_not_provider_connectivity\","` | — |
| [SRC-1AE03B9EC3-L000415](../../agents/web_agent.py#L415) | 415 | `"                \"language_model_configured_means\": \"credential_present_not_successful_completion\","` | — |
| [SRC-1AE03B9EC3-L000416](../../agents/web_agent.py#L416) | 416 | `"                \"search_providers_means\": \"supported_or_conditionally_configured_not_live_verified\","` | — |
| [SRC-1AE03B9EC3-L000417](../../agents/web_agent.py#L417) | 417 | `"                \"direct_social_api_flags_mean\": \"credentials_present_not_permissions_or_connectivity_verified\","` | — |
| [SRC-1AE03B9EC3-L000418](../../agents/web_agent.py#L418) | 418 | `"                \"live_diagnostics_endpoint\": \"POST /api/diagnostics\","` | — |
| [SRC-1AE03B9EC3-L000419](../../agents/web_agent.py#L419) | 419 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000420](../../agents/web_agent.py#L420) | 420 | `"        }"` | — |
| [SRC-1AE03B9EC3-L000421](../../agents/web_agent.py#L421) | 421 | `""` | — |
| [SRC-1AE03B9EC3-L000422](../../agents/web_agent.py#L422) | 422 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000423](../../agents/web_agent.py#L423) | 423 | `"    def _unwrap_search_url(value: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000424](../../agents/web_agent.py#L424) | 424 | `"        if value.startswith(\"//\"):"` | — |
| [SRC-1AE03B9EC3-L000425](../../agents/web_agent.py#L425) | 425 | `"            value = \"https:\" + value"` | — |
| [SRC-1AE03B9EC3-L000426](../../agents/web_agent.py#L426) | 426 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000427](../../agents/web_agent.py#L427) | 427 | `"            parsed = urllib.parse.urlparse(value)"` | — |
| [SRC-1AE03B9EC3-L000428](../../agents/web_agent.py#L428) | 428 | `"            host = (parsed.hostname or \"\").lower()"` | — |
| [SRC-1AE03B9EC3-L000429](../../agents/web_agent.py#L429) | 429 | `"            if host.endswith(\"duckduckgo.com\") and parsed.path.startswith(\"/l/\"):"` | — |
| [SRC-1AE03B9EC3-L000430](../../agents/web_agent.py#L430) | 430 | `"                target = urllib.parse.parse_qs(parsed.query).get(\"uddg\", [\"\"])[0]"` | — |
| [SRC-1AE03B9EC3-L000431](../../agents/web_agent.py#L431) | 431 | `"                return urllib.parse.unquote(target) if target else \"\""` | — |
| [SRC-1AE03B9EC3-L000432](../../agents/web_agent.py#L432) | 432 | `"        except (ValueError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L000433](../../agents/web_agent.py#L433) | 433 | `"            return \"\""` | — |
| [SRC-1AE03B9EC3-L000434](../../agents/web_agent.py#L434) | 434 | `"        return value"` | — |
| [SRC-1AE03B9EC3-L000435](../../agents/web_agent.py#L435) | 435 | `""` | — |
| [SRC-1AE03B9EC3-L000436](../../agents/web_agent.py#L436) | 436 | `"    def _record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L000437](../../agents/web_agent.py#L437) | 437 | `"        self, provider: str, query: str, status: str, result_count: int = 0,"` | — |
| [SRC-1AE03B9EC3-L000438](../../agents/web_agent.py#L438) | 438 | `"        rejected_count: int = 0, error: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L000439](../../agents/web_agent.py#L439) | 439 | `"    ) -> None:"` | — |
| [SRC-1AE03B9EC3-L000440](../../agents/web_agent.py#L440) | 440 | `"        record = {"` | — |
| [SRC-1AE03B9EC3-L000441](../../agents/web_agent.py#L441) | 441 | `"            \"provider\": provider,"` | — |
| [SRC-1AE03B9EC3-L000442](../../agents/web_agent.py#L442) | 442 | `"            \"query\": _clean_text(query, 220),"` | — |
| [SRC-1AE03B9EC3-L000443](../../agents/web_agent.py#L443) | 443 | `"            \"status\": status,"` | — |
| [SRC-1AE03B9EC3-L000444](../../agents/web_agent.py#L444) | 444 | `"            \"result_count\": int(result_count),"` | — |
| [SRC-1AE03B9EC3-L000445](../../agents/web_agent.py#L445) | 445 | `"            \"rejected_count\": int(rejected_count),"` | — |
| [SRC-1AE03B9EC3-L000446](../../agents/web_agent.py#L446) | 446 | `"        }"` | — |
| [SRC-1AE03B9EC3-L000447](../../agents/web_agent.py#L447) | 447 | `"        if error:"` | — |
| [SRC-1AE03B9EC3-L000448](../../agents/web_agent.py#L448) | 448 | `"            record[\"error\"] = _clean_text(error, 180)"` | — |
| [SRC-1AE03B9EC3-L000449](../../agents/web_agent.py#L449) | 449 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L000450](../../agents/web_agent.py#L450) | 450 | `"            self._provider_diagnostics.append(record)"` | — |
| [SRC-1AE03B9EC3-L000451](../../agents/web_agent.py#L451) | 451 | `"            # Bound memory when the instance serves many user requests."` | — |
| [SRC-1AE03B9EC3-L000452](../../agents/web_agent.py#L452) | 452 | `"            self._provider_diagnostics = self._provider_diagnostics[-160:]"` | — |
| [SRC-1AE03B9EC3-L000453](../../agents/web_agent.py#L453) | 453 | `""` | — |
| [SRC-1AE03B9EC3-L000454](../../agents/web_agent.py#L454) | 454 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000455](../../agents/web_agent.py#L455) | 455 | `"    def _source_matches_query(query: str, source: dict[str, Any]) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000456](../../agents/web_agent.py#L456) | 456 | `"        if \"user_supplied_url\" in source.get(\"providers\", []):"` | — |
| [SRC-1AE03B9EC3-L000457](../../agents/web_agent.py#L457) | 457 | `"            return True"` | — |
| [SRC-1AE03B9EC3-L000458](../../agents/web_agent.py#L458) | 458 | `"        evidence = \" \".join("` | — |
| [SRC-1AE03B9EC3-L000459](../../agents/web_agent.py#L459) | 459 | `"            str(source.get(key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L000460](../../agents/web_agent.py#L460) | 460 | `"            for key in (\"title\", \"snippet\", \"page_text\")"` | — |
| [SRC-1AE03B9EC3-L000461](../../agents/web_agent.py#L461) | 461 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000462](../../agents/web_agent.py#L462) | 462 | `"        return _relevance_ratio(query, evidence) >= 0.20"` | — |
| [SRC-1AE03B9EC3-L000463](../../agents/web_agent.py#L463) | 463 | `""` | — |
| [SRC-1AE03B9EC3-L000464](../../agents/web_agent.py#L464) | 464 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000465](../../agents/web_agent.py#L465) | 465 | `"    def _normalized_source_url_key(value: Any) -> str:"` | — |
| [SRC-1AE03B9EC3-L000466](../../agents/web_agent.py#L466) | 466 | `"        \"\"\"Normalize a public HTTP(S) URL for duplicate detection across search rounds.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000467](../../agents/web_agent.py#L467) | 467 | `"        if not isinstance(value, str) or not value.strip():"` | — |
| [SRC-1AE03B9EC3-L000468](../../agents/web_agent.py#L468) | 468 | `"            return \"\""` | — |
| [SRC-1AE03B9EC3-L000469](../../agents/web_agent.py#L469) | 469 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000470](../../agents/web_agent.py#L470) | 470 | `"            parsed = urllib.parse.urlsplit(value.strip())"` | — |
| [SRC-1AE03B9EC3-L000471](../../agents/web_agent.py#L471) | 471 | `"            scheme = parsed.scheme.lower()"` | — |
| [SRC-1AE03B9EC3-L000472](../../agents/web_agent.py#L472) | 472 | `"            if scheme not in {\"http\", \"https\"} or not parsed.hostname:"` | — |
| [SRC-1AE03B9EC3-L000473](../../agents/web_agent.py#L473) | 473 | `"                return \"\""` | — |
| [SRC-1AE03B9EC3-L000474](../../agents/web_agent.py#L474) | 474 | `"            host = parsed.hostname.lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L000475](../../agents/web_agent.py#L475) | 475 | `"            port = parsed.port"` | — |
| [SRC-1AE03B9EC3-L000476](../../agents/web_agent.py#L476) | 476 | `"            if (scheme == \"https\" and port == 443) or (scheme == \"http\" and port == 80):"` | — |
| [SRC-1AE03B9EC3-L000477](../../agents/web_agent.py#L477) | 477 | `"                port = None"` | — |
| [SRC-1AE03B9EC3-L000478](../../agents/web_agent.py#L478) | 478 | `"            host_for_url = f\"[{host}]\" if \":\" in host else host"` | — |
| [SRC-1AE03B9EC3-L000479](../../agents/web_agent.py#L479) | 479 | `"            netloc = host_for_url + (f\":{port}\" if port is not None else \"\")"` | — |
| [SRC-1AE03B9EC3-L000480](../../agents/web_agent.py#L480) | 480 | `"            path = parsed.path.rstrip(\"/\") or \"/\""` | — |
| [SRC-1AE03B9EC3-L000481](../../agents/web_agent.py#L481) | 481 | `"            tracking_keys = {\"fbclid\", \"gclid\", \"ref\", \"source\"}"` | — |
| [SRC-1AE03B9EC3-L000482](../../agents/web_agent.py#L482) | 482 | `"            query_items = ["` | — |
| [SRC-1AE03B9EC3-L000483](../../agents/web_agent.py#L483) | 483 | `"                (key, item)"` | — |
| [SRC-1AE03B9EC3-L000484](../../agents/web_agent.py#L484) | 484 | `"                for key, item in urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)"` | — |
| [SRC-1AE03B9EC3-L000485](../../agents/web_agent.py#L485) | 485 | `"                if not key.lower().startswith(\"utm_\") and key.lower() not in tracking_keys"` | — |
| [SRC-1AE03B9EC3-L000486](../../agents/web_agent.py#L486) | 486 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L000487](../../agents/web_agent.py#L487) | 487 | `"            query = urllib.parse.urlencode(query_items, doseq=True)"` | — |
| [SRC-1AE03B9EC3-L000488](../../agents/web_agent.py#L488) | 488 | `"            return urllib.parse.urlunsplit((scheme, netloc, path, query, \"\"))"` | — |
| [SRC-1AE03B9EC3-L000489](../../agents/web_agent.py#L489) | 489 | `"        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L000490](../../agents/web_agent.py#L490) | 490 | `"            return \"\""` | — |
| [SRC-1AE03B9EC3-L000491](../../agents/web_agent.py#L491) | 491 | `""` | — |
| [SRC-1AE03B9EC3-L000492](../../agents/web_agent.py#L492) | 492 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000493](../../agents/web_agent.py#L493) | 493 | `"    def _question_coverage_targets(question: str) -> list[str]:"` | — |
| [SRC-1AE03B9EC3-L000494](../../agents/web_agent.py#L494) | 494 | `"        \"\"\"Extract explicit multi-part answer requirements conservatively; this is not semantic grading.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000495](../../agents/web_agent.py#L495) | 495 | `"        if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-1AE03B9EC3-L000496](../../agents/web_agent.py#L496) | 496 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L000497](../../agents/web_agent.py#L497) | 497 | `"        text = question.strip()[:MAX_QUESTION_CHARS]"` | — |
| [SRC-1AE03B9EC3-L000498](../../agents/web_agent.py#L498) | 498 | `"        marker = re.compile("` | — |
| [SRC-1AE03B9EC3-L000499](../../agents/web_agent.py#L499) | 499 | `"            r\"(?:من\\s+حيث\|من\\s+ناحية\|من\\s+الناحية\|فيما\\s+يتعلق\\s+ب\|فيما\\s+يخص\|\""` | — |
| [SRC-1AE03B9EC3-L000500](../../agents/web_agent.py#L500) | 500 | `"            r\"من\\s+منظور\|in\\s+terms\\s+of\|with\\s+respect\\s+to\|\""` | — |
| [SRC-1AE03B9EC3-L000501](../../agents/web_agent.py#L501) | 501 | `"            r\"from\\s+the\\s+perspective\\s+of\|based\\s+on\\s+the\\s+following\\s+criteria)\""` | — |
| [SRC-1AE03B9EC3-L000502](../../agents/web_agent.py#L502) | 502 | `"            r\"\\s*(.+?)(?=[؟?!.؛;\\n]\|$)\","` | — |
| [SRC-1AE03B9EC3-L000503](../../agents/web_agent.py#L503) | 503 | `"            flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L000504](../../agents/web_agent.py#L504) | 504 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000505](../../agents/web_agent.py#L505) | 505 | `"        match = marker.search(text)"` | — |
| [SRC-1AE03B9EC3-L000506](../../agents/web_agent.py#L506) | 506 | `"        if match:"` | — |
| [SRC-1AE03B9EC3-L000507](../../agents/web_agent.py#L507) | 507 | `"            raw = match.group(1)"` | — |
| [SRC-1AE03B9EC3-L000508](../../agents/web_agent.py#L508) | 508 | `"            # Keep explicit criteria separate from trailing meta-requests such as"` | — |
| [SRC-1AE03B9EC3-L000509](../../agents/web_agent.py#L509) | 509 | `"            # \"explain what cannot be verified\" rather than turning them into a criterion."` | — |
| [SRC-1AE03B9EC3-L000510](../../agents/web_agent.py#L510) | 510 | `"            raw = re.split("` | — |
| [SRC-1AE03B9EC3-L000511](../../agents/web_agent.py#L511) | 511 | `"                r\"(?:،\|,\|؛\|;)\\s*(?:و?اذكر\|و?وضح\|بيّن\|اشرح\|and\\s+(?:explain\|note\|discuss))\\b\","` | — |
| [SRC-1AE03B9EC3-L000512](../../agents/web_agent.py#L512) | 512 | `"                raw,"` | — |
| [SRC-1AE03B9EC3-L000513](../../agents/web_agent.py#L513) | 513 | `"                maxsplit=1,"` | — |
| [SRC-1AE03B9EC3-L000514](../../agents/web_agent.py#L514) | 514 | `"                flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L000515](../../agents/web_agent.py#L515) | 515 | `"            )[0]"` | — |
| [SRC-1AE03B9EC3-L000516](../../agents/web_agent.py#L516) | 516 | `"            pieces = re.split("` | — |
| [SRC-1AE03B9EC3-L000517](../../agents/web_agent.py#L517) | 517 | `"                r\"\\s*(?:،\|,\|؛\|;\|/)\\s*\|\""` | — |
| [SRC-1AE03B9EC3-L000518](../../agents/web_agent.py#L518) | 518 | `"                r\"\\s+\\band\\b\\s+\|\\s+\\bas well as\\b\\s+\|\""` | — |
| [SRC-1AE03B9EC3-L000519](../../agents/web_agent.py#L519) | 519 | `"                r\"\\s+و(?=ال\|[ء-ي])\","` | — |
| [SRC-1AE03B9EC3-L000520](../../agents/web_agent.py#L520) | 520 | `"                raw,"` | — |
| [SRC-1AE03B9EC3-L000521](../../agents/web_agent.py#L521) | 521 | `"                flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L000522](../../agents/web_agent.py#L522) | 522 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000523](../../agents/web_agent.py#L523) | 523 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L000524](../../agents/web_agent.py#L524) | 524 | `"            # If the user explicitly asks separate questions, preserve each clause."` | — |
| [SRC-1AE03B9EC3-L000525](../../agents/web_agent.py#L525) | 525 | `"            question_parts = ["` | — |
| [SRC-1AE03B9EC3-L000526](../../agents/web_agent.py#L526) | 526 | `"                part.strip(\" \\t\\r\\n-•\")"` | — |
| [SRC-1AE03B9EC3-L000527](../../agents/web_agent.py#L527) | 527 | `"                for part in re.split(r\"[؟?]+\", text)"` | — |
| [SRC-1AE03B9EC3-L000528](../../agents/web_agent.py#L528) | 528 | `"                if len(part.strip(\" \\t\\r\\n-•\")) >= 4"` | — |
| [SRC-1AE03B9EC3-L000529](../../agents/web_agent.py#L529) | 529 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L000530](../../agents/web_agent.py#L530) | 530 | `"            pieces = question_parts if len(question_parts) > 1 else []"` | — |
| [SRC-1AE03B9EC3-L000531](../../agents/web_agent.py#L531) | 531 | `""` | — |
| [SRC-1AE03B9EC3-L000532](../../agents/web_agent.py#L532) | 532 | `"        targets: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L000533](../../agents/web_agent.py#L533) | 533 | `"        seen: set[str] = set()"` | — |
| [SRC-1AE03B9EC3-L000534](../../agents/web_agent.py#L534) | 534 | `"        for piece in pieces:"` | — |
| [SRC-1AE03B9EC3-L000535](../../agents/web_agent.py#L535) | 535 | `"            target = re.sub(r\"^[\\s:،,؛;/.!?\\-–—]+\|[\\s:،,؛;/.!?\\-–—]+$\", \"\", piece).strip()"` | — |
| [SRC-1AE03B9EC3-L000536](../../agents/web_agent.py#L536) | 536 | `"            target = re.sub(r\"^(?:و\\s*)\", \"\", target).strip()"` | — |
| [SRC-1AE03B9EC3-L000537](../../agents/web_agent.py#L537) | 537 | `"            if len(target) < 2:"` | — |
| [SRC-1AE03B9EC3-L000538](../../agents/web_agent.py#L538) | 538 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L000539](../../agents/web_agent.py#L539) | 539 | `"            if len(target) > 120:"` | — |
| [SRC-1AE03B9EC3-L000540](../../agents/web_agent.py#L540) | 540 | `"                target = target[:120].rsplit(\" \", 1)[0].strip()"` | — |
| [SRC-1AE03B9EC3-L000541](../../agents/web_agent.py#L541) | 541 | `"            key = _normalize_search_query(target).casefold()"` | — |
| [SRC-1AE03B9EC3-L000542](../../agents/web_agent.py#L542) | 542 | `"            if key and key not in seen:"` | — |
| [SRC-1AE03B9EC3-L000543](../../agents/web_agent.py#L543) | 543 | `"                seen.add(key)"` | — |
| [SRC-1AE03B9EC3-L000544](../../agents/web_agent.py#L544) | 544 | `"                targets.append(target)"` | — |
| [SRC-1AE03B9EC3-L000545](../../agents/web_agent.py#L545) | 545 | `"            if len(targets) >= 8:"` | — |
| [SRC-1AE03B9EC3-L000546](../../agents/web_agent.py#L546) | 546 | `"                break"` | — |
| [SRC-1AE03B9EC3-L000547](../../agents/web_agent.py#L547) | 547 | `"        return targets"` | — |
| [SRC-1AE03B9EC3-L000548](../../agents/web_agent.py#L548) | 548 | `""` | — |
| [SRC-1AE03B9EC3-L000549](../../agents/web_agent.py#L549) | 549 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000550](../../agents/web_agent.py#L550) | 550 | `"    def _is_current_search_status_question(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000551](../../agents/web_agent.py#L551) | 551 | `"        \"\"\"Recognize a question about whether this answer already used web search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000552](../../agents/web_agent.py#L552) | 552 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000553](../../agents/web_agent.py#L553) | 553 | `"        asks_if_searched = any("` | — |
| [SRC-1AE03B9EC3-L000554](../../agents/web_agent.py#L554) | 554 | `"            term in value"` | — |
| [SRC-1AE03B9EC3-L000555](../../agents/web_agent.py#L555) | 555 | `"            for term in (\"بحثت\", \"اجريت بحث\", \"قمت بالبحث\", \"عملت بحث\", \"did you search\", \"did you browse\")"` | — |
| [SRC-1AE03B9EC3-L000556](../../agents/web_agent.py#L556) | 556 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000557](../../agents/web_agent.py#L557) | 557 | `"        references_web = any("` | — |
| [SRC-1AE03B9EC3-L000558](../../agents/web_agent.py#L558) | 558 | `"            term in value for term in (\"انترنت\", \"النت\", \"الويب\", \"ويب\", \"the web\", \"online\")"` | — |
| [SRC-1AE03B9EC3-L000559](../../agents/web_agent.py#L559) | 559 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000560](../../agents/web_agent.py#L560) | 560 | `"        references_current_answer = any("` | — |
| [SRC-1AE03B9EC3-L000561](../../agents/web_agent.py#L561) | 561 | `"            term in value"` | — |
| [SRC-1AE03B9EC3-L000562](../../agents/web_agent.py#L562) | 562 | `"            for term in ("` | — |
| [SRC-1AE03B9EC3-L000563](../../agents/web_agent.py#L563) | 563 | `"                \"اجاب\", \"الرد الحالي\", \"هذا السؤال\", \"هذه الاجابه\","` | — |
| [SRC-1AE03B9EC3-L000564](../../agents/web_agent.py#L564) | 564 | `"                \"this answer\", \"this response\","` | — |
| [SRC-1AE03B9EC3-L000565](../../agents/web_agent.py#L565) | 565 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000566](../../agents/web_agent.py#L566) | 566 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000567](../../agents/web_agent.py#L567) | 567 | `"        return asks_if_searched and references_web and references_current_answer"` | — |
| [SRC-1AE03B9EC3-L000568](../../agents/web_agent.py#L568) | 568 | `""` | — |
| [SRC-1AE03B9EC3-L000569](../../agents/web_agent.py#L569) | 569 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000570](../../agents/web_agent.py#L570) | 570 | `"    def _is_self_question(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000571](../../agents/web_agent.py#L571) | 571 | `"        \"\"\"Recognize questions about Omarai itself so they do not need web search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000572](../../agents/web_agent.py#L572) | 572 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000573](../../agents/web_agent.py#L573) | 573 | `"        capability_phrases = ("` | — |
| [SRC-1AE03B9EC3-L000574](../../agents/web_agent.py#L574) | 574 | `"            \"كيف تستطيع مساعدتي\", \"ازاي تقدر تساعدني\", \"ازاي ممكن تساعدني\","` | — |
| [SRC-1AE03B9EC3-L000575](../../agents/web_agent.py#L575) | 575 | `"            \"ماذا تستطيع ان تفعل\", \"ما الذي تستطيع فعله\", \"ايه اللي تقدر تعمله\","` | — |
| [SRC-1AE03B9EC3-L000576](../../agents/web_agent.py#L576) | 576 | `"            \"what can you do\", \"how can you help me\","` | — |
| [SRC-1AE03B9EC3-L000577](../../agents/web_agent.py#L577) | 577 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000578](../../agents/web_agent.py#L578) | 578 | `"        search_phrases = ("` | — |
| [SRC-1AE03B9EC3-L000579](../../agents/web_agent.py#L579) | 579 | `"            \"كيف تبحث انت\", \"ازاي بتبحث\", \"كيف يعمل البحث عندك\","` | — |
| [SRC-1AE03B9EC3-L000580](../../agents/web_agent.py#L580) | 580 | `"            \"ما المواقع التي تستخدمها\", \"ما محركات البحث التي تستخدمها\","` | — |
| [SRC-1AE03B9EC3-L000581](../../agents/web_agent.py#L581) | 581 | `"            \"ما المواقع التي قدرت\", \"كيف تبحث على الانترنت\","` | — |
| [SRC-1AE03B9EC3-L000582](../../agents/web_agent.py#L582) | 582 | `"            \"هل تستطيع البحث\", \"هل يمكنك البحث\", \"هل تقدر تبحث\","` | — |
| [SRC-1AE03B9EC3-L000583](../../agents/web_agent.py#L583) | 583 | `"            \"هل تستطيع الوصول\", \"هل يمكنك الوصول\","` | — |
| [SRC-1AE03B9EC3-L000584](../../agents/web_agent.py#L584) | 584 | `"            \"هل عندك اتصال بالانترنت\", \"هل عندك اتصال بالانترنيت\","` | — |
| [SRC-1AE03B9EC3-L000585](../../agents/web_agent.py#L585) | 585 | `"            \"هل عندك انترنت\","` | — |
| [SRC-1AE03B9EC3-L000586](../../agents/web_agent.py#L586) | 586 | `"            \"هل بحثت في الانترنت للاجابه الحاليه\","` | — |
| [SRC-1AE03B9EC3-L000587](../../agents/web_agent.py#L587) | 587 | `"            \"هل بحثت علي الانترنت للاجابه الحاليه\","` | — |
| [SRC-1AE03B9EC3-L000588](../../agents/web_agent.py#L588) | 588 | `"            \"هل بحثت في الانترنت لهذا السؤال\","` | — |
| [SRC-1AE03B9EC3-L000589](../../agents/web_agent.py#L589) | 589 | `"            \"هل بحثت في النت للرد ده\","` | — |
| [SRC-1AE03B9EC3-L000590](../../agents/web_agent.py#L590) | 590 | `"            \"did you search the web for this answer\","` | — |
| [SRC-1AE03B9EC3-L000591](../../agents/web_agent.py#L591) | 591 | `"            \"did you browse for this response\","` | — |
| [SRC-1AE03B9EC3-L000592](../../agents/web_agent.py#L592) | 592 | `"            \"how do you search\", \"which search engines\", \"what sites do you use\","` | — |
| [SRC-1AE03B9EC3-L000593](../../agents/web_agent.py#L593) | 593 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000594](../../agents/web_agent.py#L594) | 594 | `"        return ("` | — |
| [SRC-1AE03B9EC3-L000595](../../agents/web_agent.py#L595) | 595 | `"            any(phrase in value for phrase in capability_phrases + search_phrases)"` | — |
| [SRC-1AE03B9EC3-L000596](../../agents/web_agent.py#L596) | 596 | `"            or WebAgent._is_current_search_status_question(question)"` | — |
| [SRC-1AE03B9EC3-L000597](../../agents/web_agent.py#L597) | 597 | `"            or ("` | — |
| [SRC-1AE03B9EC3-L000598](../../agents/web_agent.py#L598) | 598 | `"                \"omarai\" in value"` | — |
| [SRC-1AE03B9EC3-L000599](../../agents/web_agent.py#L599) | 599 | `"                and any(token in value for token in (\"بحث\", \"موقع\", \"تستطيع\", \"تقدر\", \"تعمل\"))"` | — |
| [SRC-1AE03B9EC3-L000600](../../agents/web_agent.py#L600) | 600 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000601](../../agents/web_agent.py#L601) | 601 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000602](../../agents/web_agent.py#L602) | 602 | `""` | — |
| [SRC-1AE03B9EC3-L000603](../../agents/web_agent.py#L603) | 603 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000604](../../agents/web_agent.py#L604) | 604 | `"    def _is_navigation_request(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000605](../../agents/web_agent.py#L605) | 605 | `"        \"\"\"A link-finding task can be useful with one clearly labelled candidate result.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000606](../../agents/web_agent.py#L606) | 606 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000607](../../agents/web_agent.py#L607) | 607 | `"        terms = ("` | — |
| [SRC-1AE03B9EC3-L000608](../../agents/web_agent.py#L608) | 608 | `"            \"موقع\", \"رابط\", \"لينك\", \"الموقع الرسمي\", \"الصفحة الرسمية\","` | — |
| [SRC-1AE03B9EC3-L000609](../../agents/web_agent.py#L609) | 609 | `"            \"official website\", \"website\", \"homepage\", \"link to\","` | — |
| [SRC-1AE03B9EC3-L000610](../../agents/web_agent.py#L610) | 610 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000611](../../agents/web_agent.py#L611) | 611 | `"        return any(term in value for term in terms)"` | — |
| [SRC-1AE03B9EC3-L000612](../../agents/web_agent.py#L612) | 612 | `""` | — |
| [SRC-1AE03B9EC3-L000613](../../agents/web_agent.py#L613) | 613 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000614](../../agents/web_agent.py#L614) | 614 | `"    def _is_lead_search(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000615](../../agents/web_agent.py#L615) | 615 | `"        \"\"\"Keep lead discovery distinct from listing searches and generic explanations.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000616](../../agents/web_agent.py#L616) | 616 | `"        return route_intent(question).get(\"route\") == \"LEAD_GENERATION\""` | — |
| [SRC-1AE03B9EC3-L000617](../../agents/web_agent.py#L617) | 617 | `""` | — |
| [SRC-1AE03B9EC3-L000618](../../agents/web_agent.py#L618) | 618 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000619](../../agents/web_agent.py#L619) | 619 | `"    def _lead_intent_evidence(source: dict[str, Any]) -> dict[str, str] \| None:"` | — |
| [SRC-1AE03B9EC3-L000620](../../agents/web_agent.py#L620) | 620 | `"        \"\"\"Return a narrow, inspectable public buyer-intent phrase signal, if present.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000621](../../agents/web_agent.py#L621) | 621 | `"        phrases = ("` | — |
| [SRC-1AE03B9EC3-L000622](../../agents/web_agent.py#L622) | 622 | `"            \"مطلوب شقه تمليك\", \"مطلوب شقه للشراء\", \"مطلوب شراء شقه\","` | — |
| [SRC-1AE03B9EC3-L000623](../../agents/web_agent.py#L623) | 623 | `"            \"مطلوب عقار للشراء\", \"مطلوب فيلا للشراء\","` | — |
| [SRC-1AE03B9EC3-L000624](../../agents/web_agent.py#L624) | 624 | `"            \"بدور على شقه تمليك\", \"بدور على شقه للشراء\","` | — |
| [SRC-1AE03B9EC3-L000625](../../agents/web_agent.py#L625) | 625 | `"            \"ابحث عن شقه للشراء\", \"عايز اشتري شقه\", \"عاوز اشتري شقه\","` | — |
| [SRC-1AE03B9EC3-L000626](../../agents/web_agent.py#L626) | 626 | `"            \"عايز اشتري عقار\", \"عاوز اشتري عقار\", \"اريد شراء شقه\","` | — |
| [SRC-1AE03B9EC3-L000627](../../agents/web_agent.py#L627) | 627 | `"            \"ارغب في شراء شقه\", \"اريد شراء عقار\", \"ارغب في شراء عقار\","` | — |
| [SRC-1AE03B9EC3-L000628](../../agents/web_agent.py#L628) | 628 | `"            \"looking to buy\", \"looking to purchase\", \"want to buy\","` | — |
| [SRC-1AE03B9EC3-L000629](../../agents/web_agent.py#L629) | 629 | `"            \"wants to buy\", \"want to purchase\", \"wants to purchase\","` | — |
| [SRC-1AE03B9EC3-L000630](../../agents/web_agent.py#L630) | 630 | `"            \"seeking to buy\", \"seeking to purchase\", \"interested in buying\","` | — |
| [SRC-1AE03B9EC3-L000631](../../agents/web_agent.py#L631) | 631 | `"            \"interested in purchasing\", \"buyer looking to buy\","` | — |
| [SRC-1AE03B9EC3-L000632](../../agents/web_agent.py#L632) | 632 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000633](../../agents/web_agent.py#L633) | 633 | `"        for field, basis in ((\"page_text\", \"page_text\"), (\"title\", \"title\"), (\"snippet\", \"search_snippet\")):"` | — |
| [SRC-1AE03B9EC3-L000634](../../agents/web_agent.py#L634) | 634 | `"            raw = source.get(field)"` | — |
| [SRC-1AE03B9EC3-L000635](../../agents/web_agent.py#L635) | 635 | `"            if not isinstance(raw, str) or not raw.strip():"` | — |
| [SRC-1AE03B9EC3-L000636](../../agents/web_agent.py#L636) | 636 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L000637](../../agents/web_agent.py#L637) | 637 | `"            normalized = _normalize_search_query(raw).casefold()"` | — |
| [SRC-1AE03B9EC3-L000638](../../agents/web_agent.py#L638) | 638 | `"            negations = ("` | — |
| [SRC-1AE03B9EC3-L000639](../../agents/web_agent.py#L639) | 639 | `"                \"not looking to buy\", \"not interested in buying\","` | — |
| [SRC-1AE03B9EC3-L000640](../../agents/web_agent.py#L640) | 640 | `"                \"not interested in purchasing\", \"no longer looking to buy\","` | — |
| [SRC-1AE03B9EC3-L000641](../../agents/web_agent.py#L641) | 641 | `"                \"مش بدور على\", \"مش عايز اشتري\", \"مش عاوز اشتري\","` | — |
| [SRC-1AE03B9EC3-L000642](../../agents/web_agent.py#L642) | 642 | `"                \"لا اريد شراء\", \"لا ارغب في شراء\", \"مش محتاج اشتري\","` | — |
| [SRC-1AE03B9EC3-L000643](../../agents/web_agent.py#L643) | 643 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000644](../../agents/web_agent.py#L644) | 644 | `"            if any(_normalize_search_query(term).casefold() in normalized for term in negations):"` | — |
| [SRC-1AE03B9EC3-L000645](../../agents/web_agent.py#L645) | 645 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L000646](../../agents/web_agent.py#L646) | 646 | `"            for phrase in phrases:"` | — |
| [SRC-1AE03B9EC3-L000647](../../agents/web_agent.py#L647) | 647 | `"                needle = _normalize_search_query(phrase).casefold()"` | — |
| [SRC-1AE03B9EC3-L000648](../../agents/web_agent.py#L648) | 648 | `"                if needle and needle in normalized:"` | — |
| [SRC-1AE03B9EC3-L000649](../../agents/web_agent.py#L649) | 649 | `"                    return {\"phrase\": phrase, \"basis\": basis}"` | — |
| [SRC-1AE03B9EC3-L000650](../../agents/web_agent.py#L650) | 650 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000651](../../agents/web_agent.py#L651) | 651 | `""` | — |
| [SRC-1AE03B9EC3-L000652](../../agents/web_agent.py#L652) | 652 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000653](../../agents/web_agent.py#L653) | 653 | `"    def _lead_generation_queries("` | — |
| [SRC-1AE03B9EC3-L000654](../../agents/web_agent.py#L654) | 654 | `"        question: str, existing_queries: list[str] \| None = None"` | — |
| [SRC-1AE03B9EC3-L000655](../../agents/web_agent.py#L655) | 655 | `"    ) -> list[str]:"` | — |
| [SRC-1AE03B9EC3-L000656](../../agents/web_agent.py#L656) | 656 | `"        \"\"\"Create high-intent buyer-search variants without changing the product/location.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000657](../../agents/web_agent.py#L657) | 657 | `"        subject = _normalize_search_query(question).strip()"` | — |
| [SRC-1AE03B9EC3-L000658](../../agents/web_agent.py#L658) | 658 | `"        subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L000659](../../agents/web_agent.py#L659) | 659 | `"            r\"^(?:(?:من فضلك\|لو سمحت)\\s*)?(?:ابحث\|بحث\|دور\|دورلي\|اعثر)\\s+\""` | — |
| [SRC-1AE03B9EC3-L000660](../../agents/web_agent.py#L660) | 660 | `"            r\"(?:عن\|على)\\s+(?:عميل(?:\\s+محتمل)?\|عملاء(?:\\s+محتملين)?\|\""` | — |
| [SRC-1AE03B9EC3-L000661](../../agents/web_agent.py#L661) | 661 | `"            r\"مشتري(?:ن)?\|مشترين)\\s*(?:(?:الذي\|اللي\|الذين)\\s*)?\""` | — |
| [SRC-1AE03B9EC3-L000662](../../agents/web_agent.py#L662) | 662 | `"            r\"(?:(?:يريد\|عايز\|عاوز)\\s*(?:ان\\s*)?(?:يشتري\|شراء))?\\s*\","` | — |
| [SRC-1AE03B9EC3-L000663](../../agents/web_agent.py#L663) | 663 | `"            \"\", subject, flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L000664](../../agents/web_agent.py#L664) | 664 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000665](../../agents/web_agent.py#L665) | 665 | `"        subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L000666](../../agents/web_agent.py#L666) | 666 | `"            r\"^(?:please\\s+)?(?:find\|search for\|look for)\\s+(?:(?:a\|an)\\s+)?\""` | — |
| [SRC-1AE03B9EC3-L000667](../../agents/web_agent.py#L667) | 667 | `"            r\"(?:(?:potential\\s+)?(?:customer\|buyer\|prospect\|lead)s?)\\s*\""` | — |
| [SRC-1AE03B9EC3-L000668](../../agents/web_agent.py#L668) | 668 | `"            r\"(?:(?:who\|that)\\s*)?(?:(?:wants?\|looking to\|seeking to)\\s+\""` | — |
| [SRC-1AE03B9EC3-L000669](../../agents/web_agent.py#L669) | 669 | `"            r\"(?:buy\|purchase)\\s*)?\","` | — |
| [SRC-1AE03B9EC3-L000670](../../agents/web_agent.py#L670) | 670 | `"            \"\", subject, flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L000671](../../agents/web_agent.py#L671) | 671 | `"        ).strip(\" \\t:;,.-\")"` | — |
| [SRC-1AE03B9EC3-L000672](../../agents/web_agent.py#L672) | 672 | `"        if len(_search_tokens(subject)) < 2:"` | — |
| [SRC-1AE03B9EC3-L000673](../../agents/web_agent.py#L673) | 673 | `"            subject = _normalize_search_query(question).strip()"` | — |
| [SRC-1AE03B9EC3-L000674](../../agents/web_agent.py#L674) | 674 | `"        arabic = bool(re.search(r\"[\\u0600-\\u06FF]\", question))"` | — |
| [SRC-1AE03B9EC3-L000675](../../agents/web_agent.py#L675) | 675 | `"        if arabic:"` | — |
| [SRC-1AE03B9EC3-L000676](../../agents/web_agent.py#L676) | 676 | `"            targeted = ["` | — |
| [SRC-1AE03B9EC3-L000677](../../agents/web_agent.py#L677) | 677 | `"                f'\"مطلوب شراء\" {subject}',"` | — |
| [SRC-1AE03B9EC3-L000678](../../agents/web_agent.py#L678) | 678 | `"                f'\"مطلوب شقه تمليك\" {subject}',"` | — |
| [SRC-1AE03B9EC3-L000679](../../agents/web_agent.py#L679) | 679 | `"                f'\"بدور على\" {subject} تمليك',"` | — |
| [SRC-1AE03B9EC3-L000680](../../agents/web_agent.py#L680) | 680 | `"                f'\"عايز اشتري\" {subject}',"` | — |
| [SRC-1AE03B9EC3-L000681](../../agents/web_agent.py#L681) | 681 | `"                f'site:facebook.com/groups \"{subject}\" (\"مطلوب\" OR \"تمليك\")',"` | — |
| [SRC-1AE03B9EC3-L000682](../../agents/web_agent.py#L682) | 682 | `"                f'site:linkedin.com/posts \"{subject}\" (\"looking to buy\" OR \"purchase\")',"` | — |
| [SRC-1AE03B9EC3-L000683](../../agents/web_agent.py#L683) | 683 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L000684](../../agents/web_agent.py#L684) | 684 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L000685](../../agents/web_agent.py#L685) | 685 | `"            targeted = ["` | — |
| [SRC-1AE03B9EC3-L000686](../../agents/web_agent.py#L686) | 686 | `"                f'\"looking to buy\" {subject}',"` | — |
| [SRC-1AE03B9EC3-L000687](../../agents/web_agent.py#L687) | 687 | `"                f'\"want to purchase\" {subject}',"` | — |
| [SRC-1AE03B9EC3-L000688](../../agents/web_agent.py#L688) | 688 | `"                f'site:linkedin.com/posts \"{subject}\" (\"looking to buy\" OR \"purchase\")',"` | — |
| [SRC-1AE03B9EC3-L000689](../../agents/web_agent.py#L689) | 689 | `"                f'site:facebook.com/groups \"{subject}\" (\"looking for\" OR \"want to buy\")',"` | — |
| [SRC-1AE03B9EC3-L000690](../../agents/web_agent.py#L690) | 690 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L000691](../../agents/web_agent.py#L691) | 691 | `"        candidates = targeted + [_normalize_search_query(q) for q in (existing_queries or [])]"` | — |
| [SRC-1AE03B9EC3-L000692](../../agents/web_agent.py#L692) | 692 | `"        return list(dict.fromkeys(q[:500] for q in candidates if q and q.strip()))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L000693](../../agents/web_agent.py#L693) | 693 | `""` | — |
| [SRC-1AE03B9EC3-L000694](../../agents/web_agent.py#L694) | 694 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000695](../../agents/web_agent.py#L695) | 695 | `"    def _is_listing_discovery(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000696](../../agents/web_agent.py#L696) | 696 | `"        \"\"\"Recognize property/job/product discovery where candidates are useful with caveats.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000697](../../agents/web_agent.py#L697) | 697 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000698](../../agents/web_agent.py#L698) | 698 | `"        entities = ("` | — |
| [SRC-1AE03B9EC3-L000699](../../agents/web_agent.py#L699) | 699 | `"            \"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"فيلا\", \"فلل\", \"وحده سكنيه\","` | — |
| [SRC-1AE03B9EC3-L000700](../../agents/web_agent.py#L700) | 700 | `"            \"وحدات سكنيه\", \"apartment\", \"apartments\", \"flat\", \"property listing\","` | — |
| [SRC-1AE03B9EC3-L000701](../../agents/web_agent.py#L701) | 701 | `"            \"real estate\", \"house\", \"villa\", \"job opening\", \"وظيفه\", \"وظائف\","` | — |
| [SRC-1AE03B9EC3-L000702](../../agents/web_agent.py#L702) | 702 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000703](../../agents/web_agent.py#L703) | 703 | `"        actions = ("` | — |
| [SRC-1AE03B9EC3-L000704](../../agents/web_agent.py#L704) | 704 | `"            \"ابحث\", \"دور\", \"هات\", \"عايز\", \"عاوز\", \"محتاج\", \"بدور\", \"للبيع\","` | — |
| [SRC-1AE03B9EC3-L000705](../../agents/web_agent.py#L705) | 705 | `"            \"للايجار\", \"ايجار\", \"معاينه\", \"اعلان\", \"اعلانات\", \"find\", \"search\","` | — |
| [SRC-1AE03B9EC3-L000706](../../agents/web_agent.py#L706) | 706 | `"            \"looking for\", \"for sale\", \"for rent\","` | — |
| [SRC-1AE03B9EC3-L000707](../../agents/web_agent.py#L707) | 707 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000708](../../agents/web_agent.py#L708) | 708 | `"        normalized_entities = (_normalize_search_query(term).casefold() for term in entities)"` | — |
| [SRC-1AE03B9EC3-L000709](../../agents/web_agent.py#L709) | 709 | `"        normalized_actions = (_normalize_search_query(term).casefold() for term in actions)"` | — |
| [SRC-1AE03B9EC3-L000710](../../agents/web_agent.py#L710) | 710 | `"        return any(term in value for term in normalized_entities) and any("` | — |
| [SRC-1AE03B9EC3-L000711](../../agents/web_agent.py#L711) | 711 | `"            term in value for term in normalized_actions"` | — |
| [SRC-1AE03B9EC3-L000712](../../agents/web_agent.py#L712) | 712 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000713](../../agents/web_agent.py#L713) | 713 | `""` | — |
| [SRC-1AE03B9EC3-L000714](../../agents/web_agent.py#L714) | 714 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000715](../../agents/web_agent.py#L715) | 715 | `"    def _requires_web_research(question: str, mode: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000716](../../agents/web_agent.py#L716) | 716 | `"        \"\"\"Use the web only when the user requests it or the answer depends on live data.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000717](../../agents/web_agent.py#L717) | 717 | `"        # A question about whether the current answer already searched is a"` | — |
| [SRC-1AE03B9EC3-L000718](../../agents/web_agent.py#L718) | 718 | `"        # status query, not a request to launch fresh research in any UI mode."` | — |
| [SRC-1AE03B9EC3-L000719](../../agents/web_agent.py#L719) | 719 | `"        if WebAgent._is_current_search_status_question(question):"` | — |
| [SRC-1AE03B9EC3-L000720](../../agents/web_agent.py#L720) | 720 | `"            return False"` | — |
| [SRC-1AE03B9EC3-L000721](../../agents/web_agent.py#L721) | 721 | `"        if mode != \"auto\":"` | — |
| [SRC-1AE03B9EC3-L000722](../../agents/web_agent.py#L722) | 722 | `"            return True"` | — |
| [SRC-1AE03B9EC3-L000723](../../agents/web_agent.py#L723) | 723 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000724](../../agents/web_agent.py#L724) | 724 | `"        dynamic_terms = ("` | — |
| [SRC-1AE03B9EC3-L000725](../../agents/web_agent.py#L725) | 725 | `"            \"ابحث\", \"بحث عن\", \"دور على\", \"دورلي\", \"هات رابط\", \"هاتلي\","` | — |
| [SRC-1AE03B9EC3-L000726](../../agents/web_agent.py#L726) | 726 | `"            \"جيبلي\", \"اعثر على\", \"موقع\", \"رابط\", \"لينك\", \"اخبار\", \"اخر\","` | — |
| [SRC-1AE03B9EC3-L000727](../../agents/web_agent.py#L727) | 727 | `"            \"احدث\", \"اليوم\", \"دلوقتي\", \"حاليا\", \"سعر\", \"اسعار\", \"للبيع\","` | — |
| [SRC-1AE03B9EC3-L000728](../../agents/web_agent.py#L728) | 728 | `"            \"للايجار\", \"ايجار\", \"معاينه\", \"عميل محتمل\", \"عملاء محتملين\","` | — |
| [SRC-1AE03B9EC3-L000729](../../agents/web_agent.py#L729) | 729 | `"            \"وظائف\", \"وظيفه\", \"حجز\", \"موعد\", \"الطقس\", \"سهم\", \"سعر الصرف\","` | — |
| [SRC-1AE03B9EC3-L000730](../../agents/web_agent.py#L730) | 730 | `"            \"search\", \"find\", \"look up\", \"latest\", \"today\", \"current\","` | — |
| [SRC-1AE03B9EC3-L000731](../../agents/web_agent.py#L731) | 731 | `"            \"news\", \"price\", \"for sale\", \"for rent\", \"real estate\", \"job opening\","` | — |
| [SRC-1AE03B9EC3-L000732](../../agents/web_agent.py#L732) | 732 | `"            \"appointment\", \"reservation\", \"weather\", \"stock price\", \"exchange rate\","` | — |
| [SRC-1AE03B9EC3-L000733](../../agents/web_agent.py#L733) | 733 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000734](../../agents/web_agent.py#L734) | 734 | `"        return any(term in value for term in dynamic_terms) or bool("` | — |
| [SRC-1AE03B9EC3-L000735](../../agents/web_agent.py#L735) | 735 | `"            re.search(r\"https?://\", question, flags=re.IGNORECASE)"` | — |
| [SRC-1AE03B9EC3-L000736](../../agents/web_agent.py#L736) | 736 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000737](../../agents/web_agent.py#L737) | 737 | `""` | — |
| [SRC-1AE03B9EC3-L000738](../../agents/web_agent.py#L738) | 738 | `"    def _local_answer_result(self, question: str, answer: str, kind: str) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L000739](../../agents/web_agent.py#L739) | 739 | `"        \"\"\"Build a consistently shaped answer for non-research conversational requests.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000740](../../agents/web_agent.py#L740) | 740 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L000741](../../agents/web_agent.py#L741) | 741 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L000742](../../agents/web_agent.py#L742) | 742 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L000743](../../agents/web_agent.py#L743) | 743 | `"            \"search_query\": question,"` | — |
| [SRC-1AE03B9EC3-L000744](../../agents/web_agent.py#L744) | 744 | `"            \"search_queries\": [],"` | — |
| [SRC-1AE03B9EC3-L000745](../../agents/web_agent.py#L745) | 745 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L000746](../../agents/web_agent.py#L746) | 746 | `"                \"mode\": \"auto\","` | — |
| [SRC-1AE03B9EC3-L000747](../../agents/web_agent.py#L747) | 747 | `"                \"planning_method\": \"local_capability_router\","` | — |
| [SRC-1AE03B9EC3-L000748](../../agents/web_agent.py#L748) | 748 | `"                \"web_search_skipped\": True,"` | — |
| [SRC-1AE03B9EC3-L000749](../../agents/web_agent.py#L749) | 749 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000750](../../agents/web_agent.py#L750) | 750 | `"            \"sources\": [],"` | — |
| [SRC-1AE03B9EC3-L000751](../../agents/web_agent.py#L751) | 751 | `"            \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L000752](../../agents/web_agent.py#L752) | 752 | `"            \"used_web_search\": False,"` | — |
| [SRC-1AE03B9EC3-L000753](../../agents/web_agent.py#L753) | 753 | `"            \"search_attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L000754](../../agents/web_agent.py#L754) | 754 | `"            \"used_social_search\": False,"` | — |
| [SRC-1AE03B9EC3-L000755](../../agents/web_agent.py#L755) | 755 | `"            \"warnings\": [],"` | — |
| [SRC-1AE03B9EC3-L000756](../../agents/web_agent.py#L756) | 756 | `"            \"kind\": kind,"` | — |
| [SRC-1AE03B9EC3-L000757](../../agents/web_agent.py#L757) | 757 | `"            \"research_quality\": \"not_applicable\","` | — |
| [SRC-1AE03B9EC3-L000758](../../agents/web_agent.py#L758) | 758 | `"        }"` | — |
| [SRC-1AE03B9EC3-L000759](../../agents/web_agent.py#L759) | 759 | `""` | — |
| [SRC-1AE03B9EC3-L000760](../../agents/web_agent.py#L760) | 760 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000761](../../agents/web_agent.py#L761) | 761 | `"    def _local_conversation_reply(question: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000762](../../agents/web_agent.py#L762) | 762 | `"        \"\"\"Return a short greeting/acknowledgment without a model or web request.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000763](../../agents/web_agent.py#L763) | 763 | `"        value = _normalize_search_query(question).casefold().strip(\" \\t\\r\\n؟?!.,،؛;\")"` | — |
| [SRC-1AE03B9EC3-L000764](../../agents/web_agent.py#L764) | 764 | `"        if \"السلام عليكم\" in value:"` | — |
| [SRC-1AE03B9EC3-L000765](../../agents/web_agent.py#L765) | 765 | `"            return \"وعليكم السلام ورحمة الله وبركاته. أنا معاك؛ أقدر أساعدك في إيه؟\""` | — |
| [SRC-1AE03B9EC3-L000766](../../agents/web_agent.py#L766) | 766 | `"        if any(term in value for term in (\"شكرا\", \"متشكر\", \"متشكره\", \"العفو\")):"` | — |
| [SRC-1AE03B9EC3-L000767](../../agents/web_agent.py#L767) | 767 | `"            return \"العفو، تحت أمرك.\""` | — |
| [SRC-1AE03B9EC3-L000768](../../agents/web_agent.py#L768) | 768 | `"        if re.search(r\"[a-z]\", value):"` | — |
| [SRC-1AE03B9EC3-L000769](../../agents/web_agent.py#L769) | 769 | `"            if any(term in value for term in (\"thanks\", \"thank you\", \"got it\")):"` | — |
| [SRC-1AE03B9EC3-L000770](../../agents/web_agent.py#L770) | 770 | `"                return \"You're welcome—glad it helped.\""` | — |
| [SRC-1AE03B9EC3-L000771](../../agents/web_agent.py#L771) | 771 | `"            return \"Hi! I'm here and ready to help. What would you like to work on?\""` | — |
| [SRC-1AE03B9EC3-L000772](../../agents/web_agent.py#L772) | 772 | `"        return \"أهلًا! أنا معاك. أقدر أساعدك في إيه؟\""` | — |
| [SRC-1AE03B9EC3-L000773](../../agents/web_agent.py#L773) | 773 | `""` | — |
| [SRC-1AE03B9EC3-L000774](../../agents/web_agent.py#L774) | 774 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000775](../../agents/web_agent.py#L775) | 775 | `"    def _annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L000776](../../agents/web_agent.py#L776) | 776 | `"        result: dict[str, Any], route: str, reason: str, mode: str = \"auto\""` | — |
| [SRC-1AE03B9EC3-L000777](../../agents/web_agent.py#L777) | 777 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L000778](../../agents/web_agent.py#L778) | 778 | `"        \"\"\"Attach route diagnostics to both response and research-plan metadata.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000779](../../agents/web_agent.py#L779) | 779 | `"        result[\"intent_route\"] = route"` | — |
| [SRC-1AE03B9EC3-L000780](../../agents/web_agent.py#L780) | 780 | `"        result[\"intent_route_reason\"] = reason"` | — |
| [SRC-1AE03B9EC3-L000781](../../agents/web_agent.py#L781) | 781 | `"        plan = result.get(\"research_plan\")"` | — |
| [SRC-1AE03B9EC3-L000782](../../agents/web_agent.py#L782) | 782 | `"        if not isinstance(plan, dict):"` | — |
| [SRC-1AE03B9EC3-L000783](../../agents/web_agent.py#L783) | 783 | `"            plan = {}"` | — |
| [SRC-1AE03B9EC3-L000784](../../agents/web_agent.py#L784) | 784 | `"            result[\"research_plan\"] = plan"` | — |
| [SRC-1AE03B9EC3-L000785](../../agents/web_agent.py#L785) | 785 | `"        plan[\"intent_route\"] = route"` | — |
| [SRC-1AE03B9EC3-L000786](../../agents/web_agent.py#L786) | 786 | `"        plan[\"intent_route_reason\"] = reason"` | — |
| [SRC-1AE03B9EC3-L000787](../../agents/web_agent.py#L787) | 787 | `"        plan[\"mode\"] = mode"` | — |
| [SRC-1AE03B9EC3-L000788](../../agents/web_agent.py#L788) | 788 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L000789](../../agents/web_agent.py#L789) | 789 | `""` | — |
| [SRC-1AE03B9EC3-L000790](../../agents/web_agent.py#L790) | 790 | `"    def _clarification_result("` | — |
| [SRC-1AE03B9EC3-L000791](../../agents/web_agent.py#L791) | 791 | `"        self, question: str, mode: str, decision: dict[str, Any]"` | — |
| [SRC-1AE03B9EC3-L000792](../../agents/web_agent.py#L792) | 792 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L000793](../../agents/web_agent.py#L793) | 793 | `"        \"\"\"Ask for a missing referent without calling the model or search providers.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000794](../../agents/web_agent.py#L794) | 794 | `"        if re.search(r\"[a-z]\", question.casefold()):"` | — |
| [SRC-1AE03B9EC3-L000795](../../agents/web_agent.py#L795) | 795 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L000796](../../agents/web_agent.py#L796) | 796 | `"                \"What are you referring to? Please name the item or share its link, \""` | — |
| [SRC-1AE03B9EC3-L000797](../../agents/web_agent.py#L797) | 797 | `"                \"and I'll continue without guessing.\""` | — |
| [SRC-1AE03B9EC3-L000798](../../agents/web_agent.py#L798) | 798 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000799](../../agents/web_agent.py#L799) | 799 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L000800](../../agents/web_agent.py#L800) | 800 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L000801](../../agents/web_agent.py#L801) | 801 | `"                \"تقصد إيه تحديدًا؟ اكتب اسم الشيء أو المنتج المقصود، أو ابعت الرابط، \""` | — |
| [SRC-1AE03B9EC3-L000802](../../agents/web_agent.py#L802) | 802 | `"                \"وأكمل معاك من غير ما أخمّن.\""` | — |
| [SRC-1AE03B9EC3-L000803](../../agents/web_agent.py#L803) | 803 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000804](../../agents/web_agent.py#L804) | 804 | `"        result = self._local_answer_result(question, answer, \"clarification_needed\")"` | — |
| [SRC-1AE03B9EC3-L000805](../../agents/web_agent.py#L805) | 805 | `"        return self._annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L000806](../../agents/web_agent.py#L806) | 806 | `"            result, \"CLARIFY\", str(decision.get(\"reason\", \"missing_referent\")), mode"` | — |
| [SRC-1AE03B9EC3-L000807](../../agents/web_agent.py#L807) | 807 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000808](../../agents/web_agent.py#L808) | 808 | `""` | — |
| [SRC-1AE03B9EC3-L000809](../../agents/web_agent.py#L809) | 809 | `"    def _capability_status_snapshot(self) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L000810](../../agents/web_agent.py#L810) | 810 | `"        \"\"\"Describe configured capabilities without claiming a live health check.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000811](../../agents/web_agent.py#L811) | 811 | `"        status = self.status()"` | — |
| [SRC-1AE03B9EC3-L000812](../../agents/web_agent.py#L812) | 812 | `"        not_tested = \"not_tested_in_this_response\""` | — |
| [SRC-1AE03B9EC3-L000813](../../agents/web_agent.py#L813) | 813 | `"        providers = ["` | — |
| [SRC-1AE03B9EC3-L000814](../../agents/web_agent.py#L814) | 814 | `"            {"` | — |
| [SRC-1AE03B9EC3-L000815](../../agents/web_agent.py#L815) | 815 | `"                \"name\": \"duckduckgo_html\","` | — |
| [SRC-1AE03B9EC3-L000816](../../agents/web_agent.py#L816) | 816 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L000817](../../agents/web_agent.py#L817) | 817 | `"                \"configuration_status\": \"built_in_no_api_key\","` | — |
| [SRC-1AE03B9EC3-L000818](../../agents/web_agent.py#L818) | 818 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L000819](../../agents/web_agent.py#L819) | 819 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000820](../../agents/web_agent.py#L820) | 820 | `"            {"` | — |
| [SRC-1AE03B9EC3-L000821](../../agents/web_agent.py#L821) | 821 | `"                \"name\": \"bing_rss\","` | — |
| [SRC-1AE03B9EC3-L000822](../../agents/web_agent.py#L822) | 822 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L000823](../../agents/web_agent.py#L823) | 823 | `"                \"configuration_status\": \"built_in_no_api_key\","` | — |
| [SRC-1AE03B9EC3-L000824](../../agents/web_agent.py#L824) | 824 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L000825](../../agents/web_agent.py#L825) | 825 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000826](../../agents/web_agent.py#L826) | 826 | `"            {"` | — |
| [SRC-1AE03B9EC3-L000827](../../agents/web_agent.py#L827) | 827 | `"                \"name\": \"google_news_rss\","` | — |
| [SRC-1AE03B9EC3-L000828](../../agents/web_agent.py#L828) | 828 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L000829](../../agents/web_agent.py#L829) | 829 | `"                \"configuration_status\": \"conditional_no_api_key\","` | — |
| [SRC-1AE03B9EC3-L000830](../../agents/web_agent.py#L830) | 830 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L000831](../../agents/web_agent.py#L831) | 831 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000832](../../agents/web_agent.py#L832) | 832 | `"            {"` | — |
| [SRC-1AE03B9EC3-L000833](../../agents/web_agent.py#L833) | 833 | `"                \"name\": \"deepseek_search_api\","` | — |
| [SRC-1AE03B9EC3-L000834](../../agents/web_agent.py#L834) | 834 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L000835](../../agents/web_agent.py#L835) | 835 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L000836](../../agents/web_agent.py#L836) | 836 | `"                    \"configured\" if status.get(\"deepseek_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L000837](../../agents/web_agent.py#L837) | 837 | `"                    else \"not_configured\""` | — |
| [SRC-1AE03B9EC3-L000838](../../agents/web_agent.py#L838) | 838 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L000839](../../agents/web_agent.py#L839) | 839 | `"                \"runtime_status\": not_tested if status.get(\"deepseek_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L000840](../../agents/web_agent.py#L840) | 840 | `"                else \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L000841](../../agents/web_agent.py#L841) | 841 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000842](../../agents/web_agent.py#L842) | 842 | `"            {"` | — |
| [SRC-1AE03B9EC3-L000843](../../agents/web_agent.py#L843) | 843 | `"                \"name\": \"brave_search_api\","` | — |
| [SRC-1AE03B9EC3-L000844](../../agents/web_agent.py#L844) | 844 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L000845](../../agents/web_agent.py#L845) | 845 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L000846](../../agents/web_agent.py#L846) | 846 | `"                    \"configured\" if status.get(\"brave_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L000847](../../agents/web_agent.py#L847) | 847 | `"                    else \"not_configured\""` | — |
| [SRC-1AE03B9EC3-L000848](../../agents/web_agent.py#L848) | 848 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L000849](../../agents/web_agent.py#L849) | 849 | `"                \"runtime_status\": not_tested if status.get(\"brave_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L000850](../../agents/web_agent.py#L850) | 850 | `"                else \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L000851](../../agents/web_agent.py#L851) | 851 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000852](../../agents/web_agent.py#L852) | 852 | `"            {"` | — |
| [SRC-1AE03B9EC3-L000853](../../agents/web_agent.py#L853) | 853 | `"                \"name\": \"tavily_search_api\","` | — |
| [SRC-1AE03B9EC3-L000854](../../agents/web_agent.py#L854) | 854 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L000855](../../agents/web_agent.py#L855) | 855 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L000856](../../agents/web_agent.py#L856) | 856 | `"                    \"configured\" if status.get(\"tavily_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L000857](../../agents/web_agent.py#L857) | 857 | `"                    else \"not_configured\""` | — |
| [SRC-1AE03B9EC3-L000858](../../agents/web_agent.py#L858) | 858 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L000859](../../agents/web_agent.py#L859) | 859 | `"                \"runtime_status\": not_tested if status.get(\"tavily_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L000860](../../agents/web_agent.py#L860) | 860 | `"                else \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L000861](../../agents/web_agent.py#L861) | 861 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000862](../../agents/web_agent.py#L862) | 862 | `"            {"` | — |
| [SRC-1AE03B9EC3-L000863](../../agents/web_agent.py#L863) | 863 | `"                \"name\": \"openrouter_web_search\","` | — |
| [SRC-1AE03B9EC3-L000864](../../agents/web_agent.py#L864) | 864 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L000865](../../agents/web_agent.py#L865) | 865 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L000866](../../agents/web_agent.py#L866) | 866 | `"                    \"enabled\" if status.get(\"openrouter_web_search_enabled\")"` | — |
| [SRC-1AE03B9EC3-L000867](../../agents/web_agent.py#L867) | 867 | `"                    else \"disabled\""` | — |
| [SRC-1AE03B9EC3-L000868](../../agents/web_agent.py#L868) | 868 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L000869](../../agents/web_agent.py#L869) | 869 | `"                \"runtime_status\": not_tested if status.get(\"openrouter_web_search_enabled\")"` | — |
| [SRC-1AE03B9EC3-L000870](../../agents/web_agent.py#L870) | 870 | `"                else \"disabled\","` | — |
| [SRC-1AE03B9EC3-L000871](../../agents/web_agent.py#L871) | 871 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000872](../../agents/web_agent.py#L872) | 872 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L000873](../../agents/web_agent.py#L873) | 873 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L000874](../../agents/web_agent.py#L874) | 874 | `"            \"web_search\": {"` | — |
| [SRC-1AE03B9EC3-L000875](../../agents/web_agent.py#L875) | 875 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L000876](../../agents/web_agent.py#L876) | 876 | `"                \"local_dependencies_ready\": bool(status.get(\"web_search_ready\")),"` | — |
| [SRC-1AE03B9EC3-L000877](../../agents/web_agent.py#L877) | 877 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L000878](../../agents/web_agent.py#L878) | 878 | `"                \"providers\": providers,"` | — |
| [SRC-1AE03B9EC3-L000879](../../agents/web_agent.py#L879) | 879 | `"                \"semantics\": ("` | — |
| [SRC-1AE03B9EC3-L000880](../../agents/web_agent.py#L880) | 880 | `"                    \"Configuration and installed dependencies do not prove that a live \""` | — |
| [SRC-1AE03B9EC3-L000881](../../agents/web_agent.py#L881) | 881 | `"                    \"network request will succeed.\""` | — |
| [SRC-1AE03B9EC3-L000882](../../agents/web_agent.py#L882) | 882 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L000883](../../agents/web_agent.py#L883) | 883 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000884](../../agents/web_agent.py#L884) | 884 | `"            \"language_model\": {"` | — |
| [SRC-1AE03B9EC3-L000885](../../agents/web_agent.py#L885) | 885 | `"                \"configured\": bool(status.get(\"language_model_configured\")),"` | — |
| [SRC-1AE03B9EC3-L000886](../../agents/web_agent.py#L886) | 886 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L000887](../../agents/web_agent.py#L887) | 887 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000888](../../agents/web_agent.py#L888) | 888 | `"        }"` | — |
| [SRC-1AE03B9EC3-L000889](../../agents/web_agent.py#L889) | 889 | `""` | — |
| [SRC-1AE03B9EC3-L000890](../../agents/web_agent.py#L890) | 890 | `"    def _self_description_answer(self, question: str) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L000891](../../agents/web_agent.py#L891) | 891 | `"        \"\"\"Answer self/capability questions without inventing a live health result.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000892](../../agents/web_agent.py#L892) | 892 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000893](../../agents/web_agent.py#L893) | 893 | `"        current_search_question = self._is_current_search_status_question(question)"` | — |
| [SRC-1AE03B9EC3-L000894](../../agents/web_agent.py#L894) | 894 | `""` | — |
| [SRC-1AE03B9EC3-L000895](../../agents/web_agent.py#L895) | 895 | `"        if current_search_question:"` | — |
| [SRC-1AE03B9EC3-L000896](../../agents/web_agent.py#L896) | 896 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L000897](../../agents/web_agent.py#L897) | 897 | `"                \"لا، لم أنفّذ بحثًا حيًا للإجابة عن هذا السؤال تحديدًا؛ هذا السؤال عن \""` | — |
| [SRC-1AE03B9EC3-L000898](../../agents/web_agent.py#L898) | 898 | `"                \"طريقة عملي، ولذلك لم أبدأ بحث ويب في هذه الجولة. هذا لا يعني أن البحث \""` | — |
| [SRC-1AE03B9EC3-L000899](../../agents/web_agent.py#L899) | 899 | `"                \"غير متاح؛ عند تنفيذ طلب يحتاج إلى معلومات حديثة سأوضح هل جرت محاولة البحث، \""` | — |
| [SRC-1AE03B9EC3-L000900](../../agents/web_agent.py#L900) | 900 | `"                \"وما النتائج التي عادت، وما إذا اكتملت الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L000901](../../agents/web_agent.py#L901) | 901 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000902](../../agents/web_agent.py#L902) | 902 | `"            result = self._local_answer_result(question, answer, \"capability_answer\")"` | — |
| [SRC-1AE03B9EC3-L000903](../../agents/web_agent.py#L903) | 903 | `"            result[\"request_execution_status\"] = {"` | — |
| [SRC-1AE03B9EC3-L000904](../../agents/web_agent.py#L904) | 904 | `"                \"search_attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L000905](../../agents/web_agent.py#L905) | 905 | `"                \"search_outcome\": \"not_attempted\","` | — |
| [SRC-1AE03B9EC3-L000906](../../agents/web_agent.py#L906) | 906 | `"                \"semantics\": \"status_of_this_request_only\","` | — |
| [SRC-1AE03B9EC3-L000907](../../agents/web_agent.py#L907) | 907 | `"            }"` | — |
| [SRC-1AE03B9EC3-L000908](../../agents/web_agent.py#L908) | 908 | `"            result[\"capability_status\"] = self._capability_status_snapshot()"` | — |
| [SRC-1AE03B9EC3-L000909](../../agents/web_agent.py#L909) | 909 | `"            return result"` | — |
| [SRC-1AE03B9EC3-L000910](../../agents/web_agent.py#L910) | 910 | `""` | — |
| [SRC-1AE03B9EC3-L000911](../../agents/web_agent.py#L911) | 911 | `"        capability_phrases = ("` | — |
| [SRC-1AE03B9EC3-L000912](../../agents/web_agent.py#L912) | 912 | `"            \"كيف تستطيع مساعدتي\", \"ازاي تقدر تساعدني\", \"ازاي ممكن تساعدني\","` | — |
| [SRC-1AE03B9EC3-L000913](../../agents/web_agent.py#L913) | 913 | `"            \"ماذا تستطيع ان تفعل\", \"ما الذي تستطيع فعله\", \"ايه اللي تقدر تعمله\","` | — |
| [SRC-1AE03B9EC3-L000914](../../agents/web_agent.py#L914) | 914 | `"            \"what can you do\", \"how can you help me\","` | — |
| [SRC-1AE03B9EC3-L000915](../../agents/web_agent.py#L915) | 915 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000916](../../agents/web_agent.py#L916) | 916 | `"        if any(term in value for term in capability_phrases):"` | — |
| [SRC-1AE03B9EC3-L000917](../../agents/web_agent.py#L917) | 917 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L000918](../../agents/web_agent.py#L918) | 918 | `"                \"أقدر أساعدك في شرح الأسئلة ووضع خطط عملية، كما يتضمن Omarai مسارًا \""` | — |
| [SRC-1AE03B9EC3-L000919](../../agents/web_agent.py#L919) | 919 | `"                \"للبحث في الويب عند الحاجة إلى معلومات حديثة أو روابط أو مقارنة خيارات. \""` | — |
| [SRC-1AE03B9EC3-L000920](../../agents/web_agent.py#L920) | 920 | `"                \"سأوضح في كل مهمة ما إذا نُفذ البحث فعلًا وما المصادر التي أمكن جمعها، \""` | — |
| [SRC-1AE03B9EC3-L000921](../../agents/web_agent.py#L921) | 921 | `"                \"وما الذي لم يمكن التحقق منه. قد تعمل بعض الموصلات الاختيارية فقط عند \""` | — |
| [SRC-1AE03B9EC3-L000922](../../agents/web_agent.py#L922) | 922 | `"                \"ضبط إعداداتها، ولا أضمن الوصول إلى كل موقع أو إلى المجموعات والمنشورات \""` | — |
| [SRC-1AE03B9EC3-L000923](../../agents/web_agent.py#L923) | 923 | `"                \"الخاصة. لم أجرِ اختبار اتصال حي في هذه الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L000924](../../agents/web_agent.py#L924) | 924 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000925](../../agents/web_agent.py#L925) | 925 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L000926](../../agents/web_agent.py#L926) | 926 | `"            status = self.status()"` | — |
| [SRC-1AE03B9EC3-L000927](../../agents/web_agent.py#L927) | 927 | `"            providers = [\"DuckDuckGo HTML\", \"Bing RSS\"]"` | — |
| [SRC-1AE03B9EC3-L000928](../../agents/web_agent.py#L928) | 928 | `"            providers.append(\"Google News RSS عند ملاءمة السؤال أو الحاجة إلى معلومات حديثة\")"` | — |
| [SRC-1AE03B9EC3-L000929](../../agents/web_agent.py#L929) | 929 | `"            if status.get(\"deepseek_search_api_configured\"):"` | — |
| [SRC-1AE03B9EC3-L000930](../../agents/web_agent.py#L930) | 930 | `"                providers.append("` | — |
| [SRC-1AE03B9EC3-L000931](../../agents/web_agent.py#L931) | 931 | `"                    \"DeepSeek Search API (مفتاحه مضبوط، لكنه غير مختبر في هذه الإجابة \""` | — |
| [SRC-1AE03B9EC3-L000932](../../agents/web_agent.py#L932) | 932 | `"                    \"وقد يستهلك استخدامًا مدفوعًا)\""` | — |
| [SRC-1AE03B9EC3-L000933](../../agents/web_agent.py#L933) | 933 | `"                )"` | — |
| [SRC-1AE03B9EC3-L000934](../../agents/web_agent.py#L934) | 934 | `"            if status.get(\"brave_search_api_configured\"):"` | — |
| [SRC-1AE03B9EC3-L000935](../../agents/web_agent.py#L935) | 935 | `"                providers.append(\"Brave Search API (الإعداد موجود، وليس دليلًا على نجاح الاتصال)\")"` | — |
| [SRC-1AE03B9EC3-L000936](../../agents/web_agent.py#L936) | 936 | `"            if status.get(\"tavily_search_api_configured\"):"` | — |
| [SRC-1AE03B9EC3-L000937](../../agents/web_agent.py#L937) | 937 | `"                providers.append(\"Tavily Search API (الإعداد موجود، وليس دليلًا على نجاح الاتصال)\")"` | — |
| [SRC-1AE03B9EC3-L000938](../../agents/web_agent.py#L938) | 938 | `"            if status.get(\"openrouter_web_search_enabled\"):"` | — |
| [SRC-1AE03B9EC3-L000939](../../agents/web_agent.py#L939) | 939 | `"                providers.append(\"بحث OpenRouter المباشر (مفعّل بالإعداد، وقد يستهلك رصيدًا)\")"` | — |
| [SRC-1AE03B9EC3-L000940](../../agents/web_agent.py#L940) | 940 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L000941](../../agents/web_agent.py#L941) | 941 | `"                \"بحسب الكود الحالي، يتضمن Omarai مسار بحث ويب يستخدم: \""` | — |
| [SRC-1AE03B9EC3-L000942](../../agents/web_agent.py#L942) | 942 | `"                + \"، \".join(providers)"` | — |
| [SRC-1AE03B9EC3-L000943](../../agents/web_agent.py#L943) | 943 | `"                + \". هذه قائمة بالموصلات المضمّنة أو المهيأة، وليست إثباتًا بأنها نجحت \""` | — |
| [SRC-1AE03B9EC3-L000944](../../agents/web_agent.py#L944) | 944 | `"                \"في هذه اللحظة. لم أنفّذ اختبار اتصال حي في هذه الإجابة، لذلك لا أستطيع \""` | — |
| [SRC-1AE03B9EC3-L000945](../../agents/web_agent.py#L945) | 945 | `"                \"تأكيد توافر الشبكة الآن. عند طلب بحث فعلي، ينبغي أن يوضح التقرير ما إذا \""` | — |
| [SRC-1AE03B9EC3-L000946](../../agents/web_agent.py#L946) | 946 | `"                \"بدأت المحاولة، وما الموصلات التي أعادت نتائج، وما الصفحات التي أمكن قراءة \""` | — |
| [SRC-1AE03B9EC3-L000947](../../agents/web_agent.py#L947) | 947 | `"                \"محتواها. لا يوجد وصول مضمون إلى كل الإنترنت أو إلى المحتوى الخاص.\""` | — |
| [SRC-1AE03B9EC3-L000948](../../agents/web_agent.py#L948) | 948 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000949](../../agents/web_agent.py#L949) | 949 | `"        result = self._local_answer_result(question, answer, \"capability_answer\")"` | — |
| [SRC-1AE03B9EC3-L000950](../../agents/web_agent.py#L950) | 950 | `"        result[\"capability_status\"] = self._capability_status_snapshot()"` | — |
| [SRC-1AE03B9EC3-L000951](../../agents/web_agent.py#L951) | 951 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L000952](../../agents/web_agent.py#L952) | 952 | `""` | — |
| [SRC-1AE03B9EC3-L000953](../../agents/web_agent.py#L953) | 953 | `"    def _answer_without_search("` | — |
| [SRC-1AE03B9EC3-L000954](../../agents/web_agent.py#L954) | 954 | `"        self, question: str, history: list[dict[str, str]]"` | — |
| [SRC-1AE03B9EC3-L000955](../../agents/web_agent.py#L955) | 955 | `"    ) -> dict[str, Any] \| None:"` | — |
| [SRC-1AE03B9EC3-L000956](../../agents/web_agent.py#L956) | 956 | `"        \"\"\"Answer stable informational questions with the configured LLM, without fake citations.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000957](../../agents/web_agent.py#L957) | 957 | `"        if not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L000958](../../agents/web_agent.py#L958) | 958 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000959](../../agents/web_agent.py#L959) | 959 | `"        messages: list[dict[str, str]] = ["` | — |
| [SRC-1AE03B9EC3-L000960](../../agents/web_agent.py#L960) | 960 | `"            {"` | — |
| [SRC-1AE03B9EC3-L000961](../../agents/web_agent.py#L961) | 961 | `"                \"role\": \"system\","` | — |
| [SRC-1AE03B9EC3-L000962](../../agents/web_agent.py#L962) | 962 | `"                \"content\": ("` | — |
| [SRC-1AE03B9EC3-L000963](../../agents/web_agent.py#L963) | 963 | `"                    \"أنت Omarai، مساعد عربي عملي. أجب مباشرة وباللغة التي استخدمها الشخص، \""` | — |
| [SRC-1AE03B9EC3-L000964](../../agents/web_agent.py#L964) | 964 | `"                    \"وافهم المقصود حتى لو كان باللهجة المصرية أو به أخطاء كتابية. هذا المسار \""` | — |
| [SRC-1AE03B9EC3-L000965](../../agents/web_agent.py#L965) | 965 | `"                    \"للشرح والمعرفة العامة والأسئلة الحوارية غير المعتمدة على معلومات لحظية. \""` | — |
| [SRC-1AE03B9EC3-L000966](../../agents/web_agent.py#L966) | 966 | `"                    \"لا تستخدم أدوات الويب ولا تقل إنك بحثت أو تحققت من مصدر. لا تختلق أرقامًا \""` | — |
| [SRC-1AE03B9EC3-L000967](../../agents/web_agent.py#L967) | 967 | `"                    \"أو اقتباسات أو روابط. إذا كان جزء من السؤال يتطلب بيانات حديثة أو تحققًا \""` | — |
| [SRC-1AE03B9EC3-L000968](../../agents/web_agent.py#L968) | 968 | `"                    \"خارجيًا، صرّح بذلك بدل الجزم. وضّح عدم اليقين بإيجاز، وأعط إجابة مفيدة \""` | — |
| [SRC-1AE03B9EC3-L000969](../../agents/web_agent.py#L969) | 969 | `"                    \"من غير إطالة أو سلسلة تفكير داخلية.\""` | — |
| [SRC-1AE03B9EC3-L000970](../../agents/web_agent.py#L970) | 970 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L000971](../../agents/web_agent.py#L971) | 971 | `"            }"` | — |
| [SRC-1AE03B9EC3-L000972](../../agents/web_agent.py#L972) | 972 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L000973](../../agents/web_agent.py#L973) | 973 | `"        messages.extend(history[-MAX_HISTORY_ITEMS:])"` | — |
| [SRC-1AE03B9EC3-L000974](../../agents/web_agent.py#L974) | 974 | `"        messages.append({\"role\": \"user\", \"content\": question})"` | — |
| [SRC-1AE03B9EC3-L000975](../../agents/web_agent.py#L975) | 975 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000976](../../agents/web_agent.py#L976) | 976 | `"            answer = self._request_completion("` | — |
| [SRC-1AE03B9EC3-L000977](../../agents/web_agent.py#L977) | 977 | `"                messages,"` | — |
| [SRC-1AE03B9EC3-L000978](../../agents/web_agent.py#L978) | 978 | `"                max_tokens=1500,"` | — |
| [SRC-1AE03B9EC3-L000979](../../agents/web_agent.py#L979) | 979 | `"                temperature=0.2,"` | — |
| [SRC-1AE03B9EC3-L000980](../../agents/web_agent.py#L980) | 980 | `"                timeout=self._effective_timeout(min(self.timeout, 28)),"` | — |
| [SRC-1AE03B9EC3-L000981](../../agents/web_agent.py#L981) | 981 | `"                model=self.answer_model,"` | — |
| [SRC-1AE03B9EC3-L000982](../../agents/web_agent.py#L982) | 982 | `"                enable_web_search=False,"` | — |
| [SRC-1AE03B9EC3-L000983](../../agents/web_agent.py#L983) | 983 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000984](../../agents/web_agent.py#L984) | 984 | `"        except (RuntimeError, AgentDependencyError):"` | — |
| [SRC-1AE03B9EC3-L000985](../../agents/web_agent.py#L985) | 985 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000986](../../agents/web_agent.py#L986) | 986 | `"        # Never turn an overlong completion into a seemingly complete answer by slicing it."` | — |
| [SRC-1AE03B9EC3-L000987](../../agents/web_agent.py#L987) | 987 | `"        if len(answer) > 24_000:"` | — |
| [SRC-1AE03B9EC3-L000988](../../agents/web_agent.py#L988) | 988 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000989](../../agents/web_agent.py#L989) | 989 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L000990](../../agents/web_agent.py#L990) | 990 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L000991](../../agents/web_agent.py#L991) | 991 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L000992](../../agents/web_agent.py#L992) | 992 | `"            \"search_query\": question,"` | — |
| [SRC-1AE03B9EC3-L000993](../../agents/web_agent.py#L993) | 993 | `"            \"search_queries\": [],"` | — |
| [SRC-1AE03B9EC3-L000994](../../agents/web_agent.py#L994) | 994 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L000995](../../agents/web_agent.py#L995) | 995 | `"                \"mode\": \"auto\","` | — |
| [SRC-1AE03B9EC3-L000996](../../agents/web_agent.py#L996) | 996 | `"                \"planning_method\": \"general_qa_without_web\","` | — |
| [SRC-1AE03B9EC3-L000997](../../agents/web_agent.py#L997) | 997 | `"                \"web_search_skipped\": True,"` | — |
| [SRC-1AE03B9EC3-L000998](../../agents/web_agent.py#L998) | 998 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000999](../../agents/web_agent.py#L999) | 999 | `"            \"sources\": [],"` | — |
| [SRC-1AE03B9EC3-L001000](../../agents/web_agent.py#L1000) | 1000 | `"            \"used_language_model\": True,"` | — |
| [SRC-1AE03B9EC3-L001001](../../agents/web_agent.py#L1001) | 1001 | `"            \"used_web_search\": False,"` | — |
| [SRC-1AE03B9EC3-L001002](../../agents/web_agent.py#L1002) | 1002 | `"            \"search_attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L001003](../../agents/web_agent.py#L1003) | 1003 | `"            \"used_social_search\": False,"` | — |
| [SRC-1AE03B9EC3-L001004](../../agents/web_agent.py#L1004) | 1004 | `"            \"warnings\": [],"` | — |
| [SRC-1AE03B9EC3-L001005](../../agents/web_agent.py#L1005) | 1005 | `"            \"kind\": \"general_answer\","` | — |
| [SRC-1AE03B9EC3-L001006](../../agents/web_agent.py#L1006) | 1006 | `"            \"research_quality\": \"not_applicable\","` | — |
| [SRC-1AE03B9EC3-L001007](../../agents/web_agent.py#L1007) | 1007 | `"            \"model_calls\": list(self.model_usage),"` | — |
| [SRC-1AE03B9EC3-L001008](../../agents/web_agent.py#L1008) | 1008 | `"        }"` | — |
| [SRC-1AE03B9EC3-L001009](../../agents/web_agent.py#L1009) | 1009 | `""` | — |
| [SRC-1AE03B9EC3-L001010](../../agents/web_agent.py#L1010) | 1010 | `"    def _search_duckduckgo_html(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001011](../../agents/web_agent.py#L1011) | 1011 | `"        import httpx"` | — |
| [SRC-1AE03B9EC3-L001012](../../agents/web_agent.py#L1012) | 1012 | `"        from bs4 import BeautifulSoup"` | — |
| [SRC-1AE03B9EC3-L001013](../../agents/web_agent.py#L1013) | 1013 | `""` | — |
| [SRC-1AE03B9EC3-L001014](../../agents/web_agent.py#L1014) | 1014 | `"        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001015](../../agents/web_agent.py#L1015) | 1015 | `"            \"https://html.duckduckgo.com/html/\","` | — |
| [SRC-1AE03B9EC3-L001016](../../agents/web_agent.py#L1016) | 1016 | `"            params={\"q\": query},"` | — |
| [SRC-1AE03B9EC3-L001017](../../agents/web_agent.py#L1017) | 1017 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001018](../../agents/web_agent.py#L1018) | 1018 | `"                \"User-Agent\": ("` | — |
| [SRC-1AE03B9EC3-L001019](../../agents/web_agent.py#L1019) | 1019 | `"                    \"Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 \""` | — |
| [SRC-1AE03B9EC3-L001020](../../agents/web_agent.py#L1020) | 1020 | `"                    \"(KHTML, like Gecko) Chrome/124.0 Mobile Safari/537.36\""` | — |
| [SRC-1AE03B9EC3-L001021](../../agents/web_agent.py#L1021) | 1021 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001022](../../agents/web_agent.py#L1022) | 1022 | `"                \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001023](../../agents/web_agent.py#L1023) | 1023 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001024](../../agents/web_agent.py#L1024) | 1024 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001025](../../agents/web_agent.py#L1025) | 1025 | `"            follow_redirects=True,"` | — |
| [SRC-1AE03B9EC3-L001026](../../agents/web_agent.py#L1026) | 1026 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001027](../../agents/web_agent.py#L1027) | 1027 | `"        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001028](../../agents/web_agent.py#L1028) | 1028 | `"            raise RuntimeError(f\"HTTP {response.status_code}\")"` | — |
| [SRC-1AE03B9EC3-L001029](../../agents/web_agent.py#L1029) | 1029 | `"        soup = BeautifulSoup(response.text, \"html.parser\")"` | — |
| [SRC-1AE03B9EC3-L001030](../../agents/web_agent.py#L1030) | 1030 | `"        if soup.select_one(\"form#challenge-form, #challenge-form, .anomaly-modal\"):"` | — |
| [SRC-1AE03B9EC3-L001031](../../agents/web_agent.py#L1031) | 1031 | `"            raise RuntimeError(\"anti-bot challenge returned\")"` | — |
| [SRC-1AE03B9EC3-L001032](../../agents/web_agent.py#L1032) | 1032 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001033](../../agents/web_agent.py#L1033) | 1033 | `"        for card in soup.select(\"div.result\"):"` | — |
| [SRC-1AE03B9EC3-L001034](../../agents/web_agent.py#L1034) | 1034 | `"            link = card.select_one(\"a.result__a\")"` | — |
| [SRC-1AE03B9EC3-L001035](../../agents/web_agent.py#L1035) | 1035 | `"            if not link:"` | — |
| [SRC-1AE03B9EC3-L001036](../../agents/web_agent.py#L1036) | 1036 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001037](../../agents/web_agent.py#L1037) | 1037 | `"            url = _public_http_url(self._unwrap_search_url(str(link.get(\"href\", \"\"))))"` | — |
| [SRC-1AE03B9EC3-L001038](../../agents/web_agent.py#L1038) | 1038 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001039](../../agents/web_agent.py#L1039) | 1039 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001040](../../agents/web_agent.py#L1040) | 1040 | `"            snippet_node = card.select_one(\".result__snippet\")"` | — |
| [SRC-1AE03B9EC3-L001041](../../agents/web_agent.py#L1041) | 1041 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001042](../../agents/web_agent.py#L1042) | 1042 | `"                \"title\": _clean_text(link.get_text(\" \", strip=True), 300),"` | — |
| [SRC-1AE03B9EC3-L001043](../../agents/web_agent.py#L1043) | 1043 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001044](../../agents/web_agent.py#L1044) | 1044 | `"                \"snippet\": _clean_text("` | — |
| [SRC-1AE03B9EC3-L001045](../../agents/web_agent.py#L1045) | 1045 | `"                    snippet_node.get_text(\" \", strip=True) if snippet_node else \"\", 1200"` | — |
| [SRC-1AE03B9EC3-L001046](../../agents/web_agent.py#L1046) | 1046 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001047](../../agents/web_agent.py#L1047) | 1047 | `"                \"provider\": \"duckduckgo_html\","` | — |
| [SRC-1AE03B9EC3-L001048](../../agents/web_agent.py#L1048) | 1048 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001049](../../agents/web_agent.py#L1049) | 1049 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001050](../../agents/web_agent.py#L1050) | 1050 | `"                \"published_at\": \"\","` | — |
| [SRC-1AE03B9EC3-L001051](../../agents/web_agent.py#L1051) | 1051 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001052](../../agents/web_agent.py#L1052) | 1052 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001053](../../agents/web_agent.py#L1053) | 1053 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001054](../../agents/web_agent.py#L1054) | 1054 | `"        if not rows and (\"captcha\" in response.text.casefold() or \"anomaly\" in response.text.casefold()):"` | — |
| [SRC-1AE03B9EC3-L001055](../../agents/web_agent.py#L1055) | 1055 | `"            raise RuntimeError(\"anti-bot challenge returned no result cards\")"` | — |
| [SRC-1AE03B9EC3-L001056](../../agents/web_agent.py#L1056) | 1056 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001057](../../agents/web_agent.py#L1057) | 1057 | `""` | — |
| [SRC-1AE03B9EC3-L001058](../../agents/web_agent.py#L1058) | 1058 | `"    def _search_bing_rss(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001059](../../agents/web_agent.py#L1059) | 1059 | `"        import xml.etree.ElementTree as ET"` | — |
| [SRC-1AE03B9EC3-L001060](../../agents/web_agent.py#L1060) | 1060 | `""` | — |
| [SRC-1AE03B9EC3-L001061](../../agents/web_agent.py#L1061) | 1061 | `"        import httpx"` | — |
| [SRC-1AE03B9EC3-L001062](../../agents/web_agent.py#L1062) | 1062 | `""` | — |
| [SRC-1AE03B9EC3-L001063](../../agents/web_agent.py#L1063) | 1063 | `"        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001064](../../agents/web_agent.py#L1064) | 1064 | `"            \"https://www.bing.com/search\","` | — |
| [SRC-1AE03B9EC3-L001065](../../agents/web_agent.py#L1065) | 1065 | `"            params={\"format\": \"rss\", \"q\": query},"` | — |
| [SRC-1AE03B9EC3-L001066](../../agents/web_agent.py#L1066) | 1066 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001067](../../agents/web_agent.py#L1067) | 1067 | `"                \"User-Agent\": ("` | — |
| [SRC-1AE03B9EC3-L001068](../../agents/web_agent.py#L1068) | 1068 | `"                    \"Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 \""` | — |
| [SRC-1AE03B9EC3-L001069](../../agents/web_agent.py#L1069) | 1069 | `"                    \"(KHTML, like Gecko) Chrome/124.0 Mobile Safari/537.36\""` | — |
| [SRC-1AE03B9EC3-L001070](../../agents/web_agent.py#L1070) | 1070 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001071](../../agents/web_agent.py#L1071) | 1071 | `"                \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001072](../../agents/web_agent.py#L1072) | 1072 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001073](../../agents/web_agent.py#L1073) | 1073 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001074](../../agents/web_agent.py#L1074) | 1074 | `"            follow_redirects=True,"` | — |
| [SRC-1AE03B9EC3-L001075](../../agents/web_agent.py#L1075) | 1075 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001076](../../agents/web_agent.py#L1076) | 1076 | `"        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001077](../../agents/web_agent.py#L1077) | 1077 | `"            raise RuntimeError(f\"HTTP {response.status_code}\")"` | — |
| [SRC-1AE03B9EC3-L001078](../../agents/web_agent.py#L1078) | 1078 | `"        root = ET.fromstring(response.content)"` | — |
| [SRC-1AE03B9EC3-L001079](../../agents/web_agent.py#L1079) | 1079 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001080](../../agents/web_agent.py#L1080) | 1080 | `"        for item in root.iter():"` | — |
| [SRC-1AE03B9EC3-L001081](../../agents/web_agent.py#L1081) | 1081 | `"            if item.tag.rsplit(\"}\", 1)[-1] != \"item\":"` | — |
| [SRC-1AE03B9EC3-L001082](../../agents/web_agent.py#L1082) | 1082 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001083](../../agents/web_agent.py#L1083) | 1083 | `"            fields = {"` | — |
| [SRC-1AE03B9EC3-L001084](../../agents/web_agent.py#L1084) | 1084 | `"                child.tag.rsplit(\"}\", 1)[-1]: (child.text or \"\")"` | — |
| [SRC-1AE03B9EC3-L001085](../../agents/web_agent.py#L1085) | 1085 | `"                for child in item"` | — |
| [SRC-1AE03B9EC3-L001086](../../agents/web_agent.py#L1086) | 1086 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001087](../../agents/web_agent.py#L1087) | 1087 | `"            url = _public_http_url(fields.get(\"link\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001088](../../agents/web_agent.py#L1088) | 1088 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001089](../../agents/web_agent.py#L1089) | 1089 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001090](../../agents/web_agent.py#L1090) | 1090 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001091](../../agents/web_agent.py#L1091) | 1091 | `"                \"title\": _clean_text(fields.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001092](../../agents/web_agent.py#L1092) | 1092 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001093](../../agents/web_agent.py#L1093) | 1093 | `"                \"snippet\": _clean_text(fields.get(\"description\", \"\"), 1200),"` | — |
| [SRC-1AE03B9EC3-L001094](../../agents/web_agent.py#L1094) | 1094 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-1AE03B9EC3-L001095](../../agents/web_agent.py#L1095) | 1095 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001096](../../agents/web_agent.py#L1096) | 1096 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001097](../../agents/web_agent.py#L1097) | 1097 | `"                \"published_at\": _clean_text(fields.get(\"pubDate\", \"\"), 80),"` | — |
| [SRC-1AE03B9EC3-L001098](../../agents/web_agent.py#L1098) | 1098 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001099](../../agents/web_agent.py#L1099) | 1099 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001100](../../agents/web_agent.py#L1100) | 1100 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001101](../../agents/web_agent.py#L1101) | 1101 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001102](../../agents/web_agent.py#L1102) | 1102 | `""` | — |
| [SRC-1AE03B9EC3-L001103](../../agents/web_agent.py#L1103) | 1103 | `"    def _search_deepseek_api(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001104](../../agents/web_agent.py#L1104) | 1104 | `"        \"\"\"Use DeepSeek's optional Search API as a comparison provider, never by default.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001105](../../agents/web_agent.py#L1105) | 1105 | `"        api_key = os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001106](../../agents/web_agent.py#L1106) | 1106 | `"        if not api_key:"` | — |
| [SRC-1AE03B9EC3-L001107](../../agents/web_agent.py#L1107) | 1107 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001108](../../agents/web_agent.py#L1108) | 1108 | `"        import httpx"` | — |
| [SRC-1AE03B9EC3-L001109](../../agents/web_agent.py#L1109) | 1109 | `""` | — |
| [SRC-1AE03B9EC3-L001110](../../agents/web_agent.py#L1110) | 1110 | `"        response = httpx.post("` | — |
| [SRC-1AE03B9EC3-L001111](../../agents/web_agent.py#L1111) | 1111 | `"            \"https://api.deepseek.com/v1/tools/search\","` | — |
| [SRC-1AE03B9EC3-L001112](../../agents/web_agent.py#L1112) | 1112 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001113](../../agents/web_agent.py#L1113) | 1113 | `"                \"Authorization\": \"Bearer \" + api_key,"` | — |
| [SRC-1AE03B9EC3-L001114](../../agents/web_agent.py#L1114) | 1114 | `"                \"Content-Type\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001115](../../agents/web_agent.py#L1115) | 1115 | `"                \"Accept\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001116](../../agents/web_agent.py#L1116) | 1116 | `"                \"User-Agent\": \"OmaraiResearchAgent/1.0\","` | — |
| [SRC-1AE03B9EC3-L001117](../../agents/web_agent.py#L1117) | 1117 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001118](../../agents/web_agent.py#L1118) | 1118 | `"            json={"` | — |
| [SRC-1AE03B9EC3-L001119](../../agents/web_agent.py#L1119) | 1119 | `"                \"query\": _normalize_search_query(query)[:128] or \"public web search\","` | — |
| [SRC-1AE03B9EC3-L001120](../../agents/web_agent.py#L1120) | 1120 | `"                \"count\": min(MAX_PROVIDER_RESULTS, 10),"` | — |
| [SRC-1AE03B9EC3-L001121](../../agents/web_agent.py#L1121) | 1121 | `"                \"need_content\": False,"` | — |
| [SRC-1AE03B9EC3-L001122](../../agents/web_agent.py#L1122) | 1122 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001123](../../agents/web_agent.py#L1123) | 1123 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001124](../../agents/web_agent.py#L1124) | 1124 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001125](../../agents/web_agent.py#L1125) | 1125 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001126](../../agents/web_agent.py#L1126) | 1126 | `"        response.raise_for_status()"` | — |
| [SRC-1AE03B9EC3-L001127](../../agents/web_agent.py#L1127) | 1127 | `"        payload = response.json()"` | — |
| [SRC-1AE03B9EC3-L001128](../../agents/web_agent.py#L1128) | 1128 | `"        results = payload.get(\"results\", []) if isinstance(payload, dict) else []"` | — |
| [SRC-1AE03B9EC3-L001129](../../agents/web_agent.py#L1129) | 1129 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001130](../../agents/web_agent.py#L1130) | 1130 | `"        for item in results if isinstance(results, list) else []:"` | — |
| [SRC-1AE03B9EC3-L001131](../../agents/web_agent.py#L1131) | 1131 | `"            if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L001132](../../agents/web_agent.py#L1132) | 1132 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001133](../../agents/web_agent.py#L1133) | 1133 | `"            url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001134](../../agents/web_agent.py#L1134) | 1134 | `"            if not url or _blocked_source_url(url):"` | — |
| [SRC-1AE03B9EC3-L001135](../../agents/web_agent.py#L1135) | 1135 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001136](../../agents/web_agent.py#L1136) | 1136 | `"            title = _clean_text(item.get(\"title\", \"\"), 300)"` | — |
| [SRC-1AE03B9EC3-L001137](../../agents/web_agent.py#L1137) | 1137 | `"            summary = item.get(\"summary\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001138](../../agents/web_agent.py#L1138) | 1138 | `"            snippet = item.get(\"snippet\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001139](../../agents/web_agent.py#L1139) | 1139 | `"            if isinstance(summary, str) and summary.strip():"` | — |
| [SRC-1AE03B9EC3-L001140](../../agents/web_agent.py#L1140) | 1140 | `"                snippet = summary"` | — |
| [SRC-1AE03B9EC3-L001141](../../agents/web_agent.py#L1141) | 1141 | `"            if not title or not isinstance(snippet, str) or not snippet.strip():"` | — |
| [SRC-1AE03B9EC3-L001142](../../agents/web_agent.py#L1142) | 1142 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001143](../../agents/web_agent.py#L1143) | 1143 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001144](../../agents/web_agent.py#L1144) | 1144 | `"                \"title\": title,"` | — |
