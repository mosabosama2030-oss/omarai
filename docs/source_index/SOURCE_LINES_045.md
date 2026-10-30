# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **045**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L000424 إلى SRC-F725E90B2A-L001223
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L000424](../../tests/test_web_agent.py#L424) | 424 | `"        \"max_citable_source_index\": 1,"` | — |
| [SRC-F725E90B2A-L000425](../../tests/test_web_agent.py#L425) | 425 | `"        \"claim_support\": \"model_review_not_independent_fact_check\","` | — |
| [SRC-F725E90B2A-L000426](../../tests/test_web_agent.py#L426) | 426 | `"    }"` | — |
| [SRC-F725E90B2A-L000427](../../tests/test_web_agent.py#L427) | 427 | `""` | — |
| [SRC-F725E90B2A-L000428](../../tests/test_web_agent.py#L428) | 428 | `""` | — |
| [SRC-F725E90B2A-L000429](../../tests/test_web_agent.py#L429) | 429 | `"def test_citation_metadata_reports_invalid_reference_repair():"` | — |
| [SRC-F725E90B2A-L000430](../../tests/test_web_agent.py#L430) | 430 | `"    cleaned, warnings = WebAgent._remove_invalid_citations("` | — |
| [SRC-F725E90B2A-L000431](../../tests/test_web_agent.py#L431) | 431 | `"        \"صحيح [المصدر 1] وخاطئ [المصدر 9].\", 1"` | — |
| [SRC-F725E90B2A-L000432](../../tests/test_web_agent.py#L432) | 432 | `"    )"` | — |
| [SRC-F725E90B2A-L000433](../../tests/test_web_agent.py#L433) | 433 | `"    metadata = WebAgent._citation_validation_metadata("` | — |
| [SRC-F725E90B2A-L000434](../../tests/test_web_agent.py#L434) | 434 | `"        cleaned, 1, warnings, \"not_run\""` | — |
| [SRC-F725E90B2A-L000435](../../tests/test_web_agent.py#L435) | 435 | `"    )"` | — |
| [SRC-F725E90B2A-L000436](../../tests/test_web_agent.py#L436) | 436 | `"    assert metadata[\"status\"] == \"invalid_index_references_removed\""` | — |
| [SRC-F725E90B2A-L000437](../../tests/test_web_agent.py#L437) | 437 | `"    assert metadata[\"valid_citation_count\"] == 1"` | — |
| [SRC-F725E90B2A-L000438](../../tests/test_web_agent.py#L438) | 438 | `"    assert metadata[\"invalid_references_removed\"] == 1"` | — |
| [SRC-F725E90B2A-L000439](../../tests/test_web_agent.py#L439) | 439 | `"    assert metadata[\"claim_support\"] == \"not_verified\""` | — |
| [SRC-F725E90B2A-L000440](../../tests/test_web_agent.py#L440) | 440 | `""` | — |
| [SRC-F725E90B2A-L000441](../../tests/test_web_agent.py#L441) | 441 | `""` | — |
| [SRC-F725E90B2A-L000442](../../tests/test_web_agent.py#L442) | 442 | `"def test_citation_metadata_reports_absent_markers_and_empty_source_range():"` | — |
| [SRC-F725E90B2A-L000443](../../tests/test_web_agent.py#L443) | 443 | `"    metadata = WebAgent._citation_validation_metadata("` | — |
| [SRC-F725E90B2A-L000444](../../tests/test_web_agent.py#L444) | 444 | `"        \"لا توجد إحالات للمصادر.\", 0, [], \"not_run\""` | — |
| [SRC-F725E90B2A-L000445](../../tests/test_web_agent.py#L445) | 445 | `"    )"` | — |
| [SRC-F725E90B2A-L000446](../../tests/test_web_agent.py#L446) | 446 | `"    assert metadata[\"status\"] == \"no_citation_markers_present\""` | — |
| [SRC-F725E90B2A-L000447](../../tests/test_web_agent.py#L447) | 447 | `"    assert metadata[\"valid_citation_count\"] == 0"` | — |
| [SRC-F725E90B2A-L000448](../../tests/test_web_agent.py#L448) | 448 | `"    assert metadata[\"max_citable_source_index\"] == 0"` | — |
| [SRC-F725E90B2A-L000449](../../tests/test_web_agent.py#L449) | 449 | `""` | — |
| [SRC-F725E90B2A-L000450](../../tests/test_web_agent.py#L450) | 450 | `""` | — |
| [SRC-F725E90B2A-L000451](../../tests/test_web_agent.py#L451) | 451 | `"def test_user_supplied_url_is_prioritized_and_page_content_is_extracted(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000452](../../tests/test_web_agent.py#L452) | 452 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000453](../../tests/test_web_agent.py#L453) | 453 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: [])"` | — |
| [SRC-F725E90B2A-L000454](../../tests/test_web_agent.py#L454) | 454 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000455](../../tests/test_web_agent.py#L455) | 455 | `"        agent,"` | — |
| [SRC-F725E90B2A-L000456](../../tests/test_web_agent.py#L456) | 456 | `"        \"_fetch_page\","` | — |
| [SRC-F725E90B2A-L000457](../../tests/test_web_agent.py#L457) | 457 | `"        lambda url: (\"User page title\", \"Full public page text supplied for analysis\"),"` | — |
| [SRC-F725E90B2A-L000458](../../tests/test_web_agent.py#L458) | 458 | `"    )"` | — |
| [SRC-F725E90B2A-L000459](../../tests/test_web_agent.py#L459) | 459 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-F725E90B2A-L000460](../../tests/test_web_agent.py#L460) | 460 | `"        \"queries\": [\"لخص هذه الصفحة\"],"` | — |
| [SRC-F725E90B2A-L000461](../../tests/test_web_agent.py#L461) | 461 | `"        \"direct_urls\": [\"https://example.com/article\"],"` | — |
| [SRC-F725E90B2A-L000462](../../tests/test_web_agent.py#L462) | 462 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L000463](../../tests/test_web_agent.py#L463) | 463 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L000464](../../tests/test_web_agent.py#L464) | 464 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000465](../../tests/test_web_agent.py#L465) | 465 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000466](../../tests/test_web_agent.py#L466) | 466 | `"    })"` | — |
| [SRC-F725E90B2A-L000467](../../tests/test_web_agent.py#L467) | 467 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000468](../../tests/test_web_agent.py#L468) | 468 | `"    assert len(sources) == 1"` | — |
| [SRC-F725E90B2A-L000469](../../tests/test_web_agent.py#L469) | 469 | `"    assert sources[0][\"url\"] == \"https://example.com/article\""` | — |
| [SRC-F725E90B2A-L000470](../../tests/test_web_agent.py#L470) | 470 | `"    assert sources[0][\"title\"] == \"User page title\""` | — |
| [SRC-F725E90B2A-L000471](../../tests/test_web_agent.py#L471) | 471 | `"    assert sources[0][\"page_fetched\"] is True"` | — |
| [SRC-F725E90B2A-L000472](../../tests/test_web_agent.py#L472) | 472 | `"    assert \"user_supplied_url\" in report[\"providers_used\"]"` | — |
| [SRC-F725E90B2A-L000473](../../tests/test_web_agent.py#L473) | 473 | `""` | — |
| [SRC-F725E90B2A-L000474](../../tests/test_web_agent.py#L474) | 474 | `""` | — |
| [SRC-F725E90B2A-L000475](../../tests/test_web_agent.py#L475) | 475 | `""` | — |
| [SRC-F725E90B2A-L000476](../../tests/test_web_agent.py#L476) | 476 | `"def test_official_x_search_is_used_only_with_explicit_bearer_token(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000477](../../tests/test_web_agent.py#L477) | 477 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000478](../../tests/test_web_agent.py#L478) | 478 | `""` | — |
| [SRC-F725E90B2A-L000479](../../tests/test_web_agent.py#L479) | 479 | `"    monkeypatch.setenv(\"X_BEARER_TOKEN\", \"test-token\")"` | — |
| [SRC-F725E90B2A-L000480](../../tests/test_web_agent.py#L480) | 480 | `""` | — |
| [SRC-F725E90B2A-L000481](../../tests/test_web_agent.py#L481) | 481 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000482](../../tests/test_web_agent.py#L482) | 482 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000483](../../tests/test_web_agent.py#L483) | 483 | `""` | — |
| [SRC-F725E90B2A-L000484](../../tests/test_web_agent.py#L484) | 484 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000485](../../tests/test_web_agent.py#L485) | 485 | `"            return {"` | — |
| [SRC-F725E90B2A-L000486](../../tests/test_web_agent.py#L486) | 486 | `"                \"data\": [{"` | — |
| [SRC-F725E90B2A-L000487](../../tests/test_web_agent.py#L487) | 487 | `"                    \"id\": \"1840000000000000000\","` | — |
| [SRC-F725E90B2A-L000488](../../tests/test_web_agent.py#L488) | 488 | `"                    \"text\": \"تجربة علنية لاستهلاك سيارة كهربائية\","` | — |
| [SRC-F725E90B2A-L000489](../../tests/test_web_agent.py#L489) | 489 | `"                    \"created_at\": \"2026-10-12T10:00:00Z\","` | — |
| [SRC-F725E90B2A-L000490](../../tests/test_web_agent.py#L490) | 490 | `"                    \"author_id\": \"u1\","` | — |
| [SRC-F725E90B2A-L000491](../../tests/test_web_agent.py#L491) | 491 | `"                }],"` | — |
| [SRC-F725E90B2A-L000492](../../tests/test_web_agent.py#L492) | 492 | `"                \"includes\": {"` | — |
| [SRC-F725E90B2A-L000493](../../tests/test_web_agent.py#L493) | 493 | `"                    \"users\": [{\"id\": \"u1\", \"username\": \"driver\", \"name\": \"Driver\"}]"` | — |
| [SRC-F725E90B2A-L000494](../../tests/test_web_agent.py#L494) | 494 | `"                },"` | — |
| [SRC-F725E90B2A-L000495](../../tests/test_web_agent.py#L495) | 495 | `"            }"` | — |
| [SRC-F725E90B2A-L000496](../../tests/test_web_agent.py#L496) | 496 | `""` | — |
| [SRC-F725E90B2A-L000497](../../tests/test_web_agent.py#L497) | 497 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000498](../../tests/test_web_agent.py#L498) | 498 | `""` | — |
| [SRC-F725E90B2A-L000499](../../tests/test_web_agent.py#L499) | 499 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000500](../../tests/test_web_agent.py#L500) | 500 | `"        calls.append((url, kwargs))"` | — |
| [SRC-F725E90B2A-L000501](../../tests/test_web_agent.py#L501) | 501 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L000502](../../tests/test_web_agent.py#L502) | 502 | `""` | — |
| [SRC-F725E90B2A-L000503](../../tests/test_web_agent.py#L503) | 503 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000504](../../tests/test_web_agent.py#L504) | 504 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000505](../../tests/test_web_agent.py#L505) | 505 | `"        \"سيارة كهربائية\", [\"x\"]"` | — |
| [SRC-F725E90B2A-L000506](../../tests/test_web_agent.py#L506) | 506 | `"    )"` | — |
| [SRC-F725E90B2A-L000507](../../tests/test_web_agent.py#L507) | 507 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000508](../../tests/test_web_agent.py#L508) | 508 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L000509](../../tests/test_web_agent.py#L509) | 509 | `"    assert results[0][\"provider\"] == \"x_official_api\""` | — |
| [SRC-F725E90B2A-L000510](../../tests/test_web_agent.py#L510) | 510 | `"    assert results[0][\"url\"] == \"https://x.com/driver/status/1840000000000000000\""` | — |
| [SRC-F725E90B2A-L000511](../../tests/test_web_agent.py#L511) | 511 | `"    assert calls[0][1][\"headers\"][\"Authorization\"] == \"Bearer test-token\""` | — |
| [SRC-F725E90B2A-L000512](../../tests/test_web_agent.py#L512) | 512 | `""` | — |
| [SRC-F725E90B2A-L000513](../../tests/test_web_agent.py#L513) | 513 | `""` | — |
| [SRC-F725E90B2A-L000514](../../tests/test_web_agent.py#L514) | 514 | `""` | — |
| [SRC-F725E90B2A-L000515](../../tests/test_web_agent.py#L515) | 515 | `"def test_instagram_graph_api_returns_only_public_hashtag_media(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000516](../../tests/test_web_agent.py#L516) | 516 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000517](../../tests/test_web_agent.py#L517) | 517 | `""` | — |
| [SRC-F725E90B2A-L000518](../../tests/test_web_agent.py#L518) | 518 | `"    monkeypatch.setenv(\"INSTAGRAM_USER_ID\", \"ig-user-123\")"` | — |
| [SRC-F725E90B2A-L000519](../../tests/test_web_agent.py#L519) | 519 | `"    monkeypatch.setenv(\"INSTAGRAM_ACCESS_TOKEN\", \"test-ig-token\")"` | — |
| [SRC-F725E90B2A-L000520](../../tests/test_web_agent.py#L520) | 520 | `"    monkeypatch.setenv(\"META_GRAPH_VERSION\", \"v25.0\")"` | — |
| [SRC-F725E90B2A-L000521](../../tests/test_web_agent.py#L521) | 521 | `""` | — |
| [SRC-F725E90B2A-L000522](../../tests/test_web_agent.py#L522) | 522 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000523](../../tests/test_web_agent.py#L523) | 523 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000524](../../tests/test_web_agent.py#L524) | 524 | `""` | — |
| [SRC-F725E90B2A-L000525](../../tests/test_web_agent.py#L525) | 525 | `"        def __init__(self, payload):"` | — |
| [SRC-F725E90B2A-L000526](../../tests/test_web_agent.py#L526) | 526 | `"            self.payload = payload"` | — |
| [SRC-F725E90B2A-L000527](../../tests/test_web_agent.py#L527) | 527 | `""` | — |
| [SRC-F725E90B2A-L000528](../../tests/test_web_agent.py#L528) | 528 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000529](../../tests/test_web_agent.py#L529) | 529 | `"            return self.payload"` | — |
| [SRC-F725E90B2A-L000530](../../tests/test_web_agent.py#L530) | 530 | `""` | — |
| [SRC-F725E90B2A-L000531](../../tests/test_web_agent.py#L531) | 531 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000532](../../tests/test_web_agent.py#L532) | 532 | `""` | — |
| [SRC-F725E90B2A-L000533](../../tests/test_web_agent.py#L533) | 533 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000534](../../tests/test_web_agent.py#L534) | 534 | `"        calls.append((url, kwargs))"` | — |
| [SRC-F725E90B2A-L000535](../../tests/test_web_agent.py#L535) | 535 | `"        if url.endswith(\"/ig_hashtag_search\"):"` | — |
| [SRC-F725E90B2A-L000536](../../tests/test_web_agent.py#L536) | 536 | `"            return FakeResponse({\"data\": [{\"id\": \"tag-7\", \"name\": \"cars\"}]})"` | — |
| [SRC-F725E90B2A-L000537](../../tests/test_web_agent.py#L537) | 537 | `"        if url.endswith(\"/tag-7/recent_media\"):"` | — |
| [SRC-F725E90B2A-L000538](../../tests/test_web_agent.py#L538) | 538 | `"            return FakeResponse({\"data\": [{"` | — |
| [SRC-F725E90B2A-L000539](../../tests/test_web_agent.py#L539) | 539 | `"                \"permalink\": \"https://www.instagram.com/p/ABC123/\","` | — |
| [SRC-F725E90B2A-L000540](../../tests/test_web_agent.py#L540) | 540 | `"                \"caption\": \"Owner shared an electric car review\","` | — |
| [SRC-F725E90B2A-L000541](../../tests/test_web_agent.py#L541) | 541 | `"                \"media_type\": \"IMAGE\","` | — |
| [SRC-F725E90B2A-L000542](../../tests/test_web_agent.py#L542) | 542 | `"                \"timestamp\": \"2026-10-12T10:00:00+0000\","` | — |
| [SRC-F725E90B2A-L000543](../../tests/test_web_agent.py#L543) | 543 | `"                \"like_count\": 17,"` | — |
| [SRC-F725E90B2A-L000544](../../tests/test_web_agent.py#L544) | 544 | `"                \"comments_count\": 4,"` | — |
| [SRC-F725E90B2A-L000545](../../tests/test_web_agent.py#L545) | 545 | `"            }]})"` | — |
| [SRC-F725E90B2A-L000546](../../tests/test_web_agent.py#L546) | 546 | `"        raise AssertionError(f\"Unexpected URL {url}\")"` | — |
| [SRC-F725E90B2A-L000547](../../tests/test_web_agent.py#L547) | 547 | `""` | — |
| [SRC-F725E90B2A-L000548](../../tests/test_web_agent.py#L548) | 548 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000549](../../tests/test_web_agent.py#L549) | 549 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000550](../../tests/test_web_agent.py#L550) | 550 | `"        \"Instagram #cars\", [\"instagram\"]"` | — |
| [SRC-F725E90B2A-L000551](../../tests/test_web_agent.py#L551) | 551 | `"    )"` | — |
| [SRC-F725E90B2A-L000552](../../tests/test_web_agent.py#L552) | 552 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000553](../../tests/test_web_agent.py#L553) | 553 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L000554](../../tests/test_web_agent.py#L554) | 554 | `"    assert results[0][\"provider\"] == \"instagram_graph_api\""` | — |
| [SRC-F725E90B2A-L000555](../../tests/test_web_agent.py#L555) | 555 | `"    assert results[0][\"url\"] == \"https://www.instagram.com/p/ABC123/\""` | — |
| [SRC-F725E90B2A-L000556](../../tests/test_web_agent.py#L556) | 556 | `"    assert \"likes=17\" in results[0][\"snippet\"]"` | — |
| [SRC-F725E90B2A-L000557](../../tests/test_web_agent.py#L557) | 557 | `"    assert calls[0][1][\"params\"][\"q\"] == \"cars\""` | — |
| [SRC-F725E90B2A-L000558](../../tests/test_web_agent.py#L558) | 558 | `"    assert calls[0][1][\"params\"][\"access_token\"] == \"test-ig-token\""` | — |
| [SRC-F725E90B2A-L000559](../../tests/test_web_agent.py#L559) | 559 | `"    assert \"test-ig-token\" not in str(results)"` | — |
| [SRC-F725E90B2A-L000560](../../tests/test_web_agent.py#L560) | 560 | `""` | — |
| [SRC-F725E90B2A-L000561](../../tests/test_web_agent.py#L561) | 561 | `""` | — |
| [SRC-F725E90B2A-L000562](../../tests/test_web_agent.py#L562) | 562 | `"def test_instagram_api_not_configured_uses_honest_fallback_warning(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000563](../../tests/test_web_agent.py#L563) | 563 | `"    monkeypatch.delenv(\"INSTAGRAM_USER_ID\", raising=False)"` | — |
| [SRC-F725E90B2A-L000564](../../tests/test_web_agent.py#L564) | 564 | `"    monkeypatch.delenv(\"INSTAGRAM_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-F725E90B2A-L000565](../../tests/test_web_agent.py#L565) | 565 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000566](../../tests/test_web_agent.py#L566) | 566 | `"        \"تجارب عامة على Instagram\", [\"instagram\"]"` | — |
| [SRC-F725E90B2A-L000567](../../tests/test_web_agent.py#L567) | 567 | `"    )"` | — |
| [SRC-F725E90B2A-L000568](../../tests/test_web_agent.py#L568) | 568 | `"    assert results == []"` | — |
| [SRC-F725E90B2A-L000569](../../tests/test_web_agent.py#L569) | 569 | `"    assert any(\"indexed public Instagram\" in warning for warning in warnings)"` | — |
| [SRC-F725E90B2A-L000570](../../tests/test_web_agent.py#L570) | 570 | `""` | — |
| [SRC-F725E90B2A-L000571](../../tests/test_web_agent.py#L571) | 571 | `""` | — |
| [SRC-F725E90B2A-L000572](../../tests/test_web_agent.py#L572) | 572 | `"def test_facebook_pages_api_reads_only_operator_configured_pages(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000573](../../tests/test_web_agent.py#L573) | 573 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000574](../../tests/test_web_agent.py#L574) | 574 | `""` | — |
| [SRC-F725E90B2A-L000575](../../tests/test_web_agent.py#L575) | 575 | `"    monkeypatch.setenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"test-page-token\")"` | — |
| [SRC-F725E90B2A-L000576](../../tests/test_web_agent.py#L576) | 576 | `"    monkeypatch.setenv(\"FACEBOOK_PAGE_IDS\", \"page-1,page-2\")"` | — |
| [SRC-F725E90B2A-L000577](../../tests/test_web_agent.py#L577) | 577 | `""` | — |
| [SRC-F725E90B2A-L000578](../../tests/test_web_agent.py#L578) | 578 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000579](../../tests/test_web_agent.py#L579) | 579 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000580](../../tests/test_web_agent.py#L580) | 580 | `""` | — |
| [SRC-F725E90B2A-L000581](../../tests/test_web_agent.py#L581) | 581 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000582](../../tests/test_web_agent.py#L582) | 582 | `"            return {\"data\": [{"` | — |
| [SRC-F725E90B2A-L000583](../../tests/test_web_agent.py#L583) | 583 | `"                \"message\": \"Electric car owners looking for charging advice\","` | — |
| [SRC-F725E90B2A-L000584](../../tests/test_web_agent.py#L584) | 584 | `"                \"permalink_url\": \"https://www.facebook.com/example/posts/123\","` | — |
| [SRC-F725E90B2A-L000585](../../tests/test_web_agent.py#L585) | 585 | `"                \"created_time\": \"2026-10-12T12:00:00+0000\","` | — |
| [SRC-F725E90B2A-L000586](../../tests/test_web_agent.py#L586) | 586 | `"                \"comments\": {\"data\": ["` | — |
| [SRC-F725E90B2A-L000587](../../tests/test_web_agent.py#L587) | 587 | `"                    {\"message\": \"What is the current price?\", \"like_count\": 3}"` | — |
| [SRC-F725E90B2A-L000588](../../tests/test_web_agent.py#L588) | 588 | `"                ]},"` | — |
| [SRC-F725E90B2A-L000589](../../tests/test_web_agent.py#L589) | 589 | `"            }]}"` | — |
| [SRC-F725E90B2A-L000590](../../tests/test_web_agent.py#L590) | 590 | `""` | — |
| [SRC-F725E90B2A-L000591](../../tests/test_web_agent.py#L591) | 591 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000592](../../tests/test_web_agent.py#L592) | 592 | `""` | — |
| [SRC-F725E90B2A-L000593](../../tests/test_web_agent.py#L593) | 593 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000594](../../tests/test_web_agent.py#L594) | 594 | `"        calls.append((url, kwargs))"` | — |
| [SRC-F725E90B2A-L000595](../../tests/test_web_agent.py#L595) | 595 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L000596](../../tests/test_web_agent.py#L596) | 596 | `""` | — |
| [SRC-F725E90B2A-L000597](../../tests/test_web_agent.py#L597) | 597 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000598](../../tests/test_web_agent.py#L598) | 598 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000599](../../tests/test_web_agent.py#L599) | 599 | `"        \"electric car\", [\"facebook\"]"` | — |
| [SRC-F725E90B2A-L000600](../../tests/test_web_agent.py#L600) | 600 | `"    )"` | — |
| [SRC-F725E90B2A-L000601](../../tests/test_web_agent.py#L601) | 601 | `"    assert len(results) == 2  # one matching post for each explicitly configured page"` | — |
| [SRC-F725E90B2A-L000602](../../tests/test_web_agent.py#L602) | 602 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000603](../../tests/test_web_agent.py#L603) | 603 | `"    assert all(item[\"provider\"] == \"facebook_pages_api\" for item in results)"` | — |
| [SRC-F725E90B2A-L000604](../../tests/test_web_agent.py#L604) | 604 | `"    assert all(\"Electric car owners\" in item[\"snippet\"] for item in results)"` | — |
| [SRC-F725E90B2A-L000605](../../tests/test_web_agent.py#L605) | 605 | `"    assert len(calls) == 2"` | — |
| [SRC-F725E90B2A-L000606](../../tests/test_web_agent.py#L606) | 606 | `"    assert all(\"Bearer test-page-token\" == call[1][\"headers\"][\"Authorization\"] for call in calls)"` | — |
| [SRC-F725E90B2A-L000607](../../tests/test_web_agent.py#L607) | 607 | `""` | — |
| [SRC-F725E90B2A-L000608](../../tests/test_web_agent.py#L608) | 608 | `""` | — |
| [SRC-F725E90B2A-L000609](../../tests/test_web_agent.py#L609) | 609 | `"def test_reddit_oauth_api_is_preferred_when_credentials_are_configured(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000610](../../tests/test_web_agent.py#L610) | 610 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000611](../../tests/test_web_agent.py#L611) | 611 | `""` | — |
| [SRC-F725E90B2A-L000612](../../tests/test_web_agent.py#L612) | 612 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_ID\", \"client-test\")"` | — |
| [SRC-F725E90B2A-L000613](../../tests/test_web_agent.py#L613) | 613 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_SECRET\", \"secret-test\")"` | — |
| [SRC-F725E90B2A-L000614](../../tests/test_web_agent.py#L614) | 614 | `"    monkeypatch.setenv(\"REDDIT_USER_AGENT\", \"test:omarai:0.1\")"` | — |
| [SRC-F725E90B2A-L000615](../../tests/test_web_agent.py#L615) | 615 | `""` | — |
| [SRC-F725E90B2A-L000616](../../tests/test_web_agent.py#L616) | 616 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000617](../../tests/test_web_agent.py#L617) | 617 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000618](../../tests/test_web_agent.py#L618) | 618 | `""` | — |
| [SRC-F725E90B2A-L000619](../../tests/test_web_agent.py#L619) | 619 | `"        def __init__(self, payload):"` | — |
| [SRC-F725E90B2A-L000620](../../tests/test_web_agent.py#L620) | 620 | `"            self.payload = payload"` | — |
| [SRC-F725E90B2A-L000621](../../tests/test_web_agent.py#L621) | 621 | `""` | — |
| [SRC-F725E90B2A-L000622](../../tests/test_web_agent.py#L622) | 622 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000623](../../tests/test_web_agent.py#L623) | 623 | `"            return self.payload"` | — |
| [SRC-F725E90B2A-L000624](../../tests/test_web_agent.py#L624) | 624 | `""` | — |
| [SRC-F725E90B2A-L000625](../../tests/test_web_agent.py#L625) | 625 | `"        @property"` | — |
| [SRC-F725E90B2A-L000626](../../tests/test_web_agent.py#L626) | 626 | `"        def content(self):"` | — |
| [SRC-F725E90B2A-L000627](../../tests/test_web_agent.py#L627) | 627 | `"            import json"` | — |
| [SRC-F725E90B2A-L000628](../../tests/test_web_agent.py#L628) | 628 | `"            return json.dumps(self.payload).encode()"` | — |
| [SRC-F725E90B2A-L000629](../../tests/test_web_agent.py#L629) | 629 | `""` | — |
| [SRC-F725E90B2A-L000630](../../tests/test_web_agent.py#L630) | 630 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000631](../../tests/test_web_agent.py#L631) | 631 | `""` | — |
| [SRC-F725E90B2A-L000632](../../tests/test_web_agent.py#L632) | 632 | `"    def fake_post(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000633](../../tests/test_web_agent.py#L633) | 633 | `"        calls.append((\"POST\", url, kwargs))"` | — |
| [SRC-F725E90B2A-L000634](../../tests/test_web_agent.py#L634) | 634 | `"        return FakeResponse({\"access_token\": \"test-reddit-access-token\"})"` | — |
| [SRC-F725E90B2A-L000635](../../tests/test_web_agent.py#L635) | 635 | `""` | — |
| [SRC-F725E90B2A-L000636](../../tests/test_web_agent.py#L636) | 636 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000637](../../tests/test_web_agent.py#L637) | 637 | `"        calls.append((\"GET\", url, kwargs))"` | — |
| [SRC-F725E90B2A-L000638](../../tests/test_web_agent.py#L638) | 638 | `"        return FakeResponse({\"data\": {\"children\": [{"` | — |
| [SRC-F725E90B2A-L000639](../../tests/test_web_agent.py#L639) | 639 | `"            \"data\": {"` | — |
| [SRC-F725E90B2A-L000640](../../tests/test_web_agent.py#L640) | 640 | `"                \"title\": \"Electric vehicle owner discussion\","` | — |
| [SRC-F725E90B2A-L000641](../../tests/test_web_agent.py#L641) | 641 | `"                \"permalink\": \"/r/cars/comments/example/post/\","` | — |
| [SRC-F725E90B2A-L000642](../../tests/test_web_agent.py#L642) | 642 | `"                \"selftext\": \"Owners discuss battery range.\","` | — |
| [SRC-F725E90B2A-L000643](../../tests/test_web_agent.py#L643) | 643 | `"                \"created_utc\": 1791800000,"` | — |
| [SRC-F725E90B2A-L000644](../../tests/test_web_agent.py#L644) | 644 | `"                \"score\": 25,"` | — |
| [SRC-F725E90B2A-L000645](../../tests/test_web_agent.py#L645) | 645 | `"                \"num_comments\": 8,"` | — |
| [SRC-F725E90B2A-L000646](../../tests/test_web_agent.py#L646) | 646 | `"            }"` | — |
| [SRC-F725E90B2A-L000647](../../tests/test_web_agent.py#L647) | 647 | `"        }]}})"` | — |
| [SRC-F725E90B2A-L000648](../../tests/test_web_agent.py#L648) | 648 | `""` | — |
| [SRC-F725E90B2A-L000649](../../tests/test_web_agent.py#L649) | 649 | `"    monkeypatch.setattr(httpx, \"post\", fake_post)"` | — |
| [SRC-F725E90B2A-L000650](../../tests/test_web_agent.py#L650) | 650 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000651](../../tests/test_web_agent.py#L651) | 651 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000652](../../tests/test_web_agent.py#L652) | 652 | `"        \"electric vehicles\", [\"reddit\"]"` | — |
| [SRC-F725E90B2A-L000653](../../tests/test_web_agent.py#L653) | 653 | `"    )"` | — |
| [SRC-F725E90B2A-L000654](../../tests/test_web_agent.py#L654) | 654 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L000655](../../tests/test_web_agent.py#L655) | 655 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000656](../../tests/test_web_agent.py#L656) | 656 | `"    assert results[0][\"provider\"] == \"reddit_oauth_api\""` | — |
| [SRC-F725E90B2A-L000657](../../tests/test_web_agent.py#L657) | 657 | `"    assert results[0][\"url\"] == \"https://www.reddit.com/r/cars/comments/example/post/\""` | — |
| [SRC-F725E90B2A-L000658](../../tests/test_web_agent.py#L658) | 658 | `"    assert \"score=25\" in results[0][\"snippet\"]"` | — |
| [SRC-F725E90B2A-L000659](../../tests/test_web_agent.py#L659) | 659 | `"    assert len([call for call in calls if call[0] == \"POST\"]) == 1"` | — |
| [SRC-F725E90B2A-L000660](../../tests/test_web_agent.py#L660) | 660 | `"    assert any(\"oauth.reddit.com/search\" in call[1] for call in calls if call[0] == \"GET\")"` | — |
| [SRC-F725E90B2A-L000661](../../tests/test_web_agent.py#L661) | 661 | `"    assert \"test-reddit-access-token\" not in str(results)"` | — |
| [SRC-F725E90B2A-L000662](../../tests/test_web_agent.py#L662) | 662 | `""` | — |
| [SRC-F725E90B2A-L000663](../../tests/test_web_agent.py#L663) | 663 | `""` | — |
| [SRC-F725E90B2A-L000664](../../tests/test_web_agent.py#L664) | 664 | `""` | — |
| [SRC-F725E90B2A-L000665](../../tests/test_web_agent.py#L665) | 665 | `"def test_role_models_are_explicit_and_have_a_fallback(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000666](../../tests/test_web_agent.py#L666) | 666 | `"    for name in ("` | — |
| [SRC-F725E90B2A-L000667](../../tests/test_web_agent.py#L667) | 667 | `"        \"OMARAI_LLM_MODEL\","` | — |
| [SRC-F725E90B2A-L000668](../../tests/test_web_agent.py#L668) | 668 | `"        \"OMARAI_PLANNER_MODEL\","` | — |
| [SRC-F725E90B2A-L000669](../../tests/test_web_agent.py#L669) | 669 | `"        \"OMARAI_ANSWER_MODEL\","` | — |
| [SRC-F725E90B2A-L000670](../../tests/test_web_agent.py#L670) | 670 | `"        \"OMARAI_REVIEW_MODEL\","` | — |
| [SRC-F725E90B2A-L000671](../../tests/test_web_agent.py#L671) | 671 | `"        \"OMARAI_LLM_FALLBACK_MODEL\","` | — |
| [SRC-F725E90B2A-L000672](../../tests/test_web_agent.py#L672) | 672 | `"    ):"` | — |
| [SRC-F725E90B2A-L000673](../../tests/test_web_agent.py#L673) | 673 | `"        monkeypatch.delenv(name, raising=False)"` | — |
| [SRC-F725E90B2A-L000674](../../tests/test_web_agent.py#L674) | 674 | `""` | — |
| [SRC-F725E90B2A-L000675](../../tests/test_web_agent.py#L675) | 675 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000676](../../tests/test_web_agent.py#L676) | 676 | `"    assert agent.planner_model == \"nvidia/nemotron-3-ultra-550b-a55b:free\""` | — |
| [SRC-F725E90B2A-L000677](../../tests/test_web_agent.py#L677) | 677 | `"    assert agent.answer_model == \"google/gemma-4-31b-it:free\""` | — |
| [SRC-F725E90B2A-L000678](../../tests/test_web_agent.py#L678) | 678 | `"    assert agent.review_model == agent.answer_model"` | — |
| [SRC-F725E90B2A-L000679](../../tests/test_web_agent.py#L679) | 679 | `"    assert agent.fallback_model == \"openrouter/free\""` | — |
| [SRC-F725E90B2A-L000680](../../tests/test_web_agent.py#L680) | 680 | `""` | — |
| [SRC-F725E90B2A-L000681](../../tests/test_web_agent.py#L681) | 681 | `""` | — |
| [SRC-F725E90B2A-L000682](../../tests/test_web_agent.py#L682) | 682 | `"def test_global_model_override_is_preserved_for_existing_users(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000683](../../tests/test_web_agent.py#L683) | 683 | `"    monkeypatch.setenv(\"OMARAI_LLM_MODEL\", \"example/custom-model\")"` | — |
| [SRC-F725E90B2A-L000684](../../tests/test_web_agent.py#L684) | 684 | `"    monkeypatch.delenv(\"OMARAI_PLANNER_MODEL\", raising=False)"` | — |
| [SRC-F725E90B2A-L000685](../../tests/test_web_agent.py#L685) | 685 | `"    monkeypatch.delenv(\"OMARAI_ANSWER_MODEL\", raising=False)"` | — |
| [SRC-F725E90B2A-L000686](../../tests/test_web_agent.py#L686) | 686 | `"    monkeypatch.delenv(\"OMARAI_REVIEW_MODEL\", raising=False)"` | — |
| [SRC-F725E90B2A-L000687](../../tests/test_web_agent.py#L687) | 687 | `""` | — |
| [SRC-F725E90B2A-L000688](../../tests/test_web_agent.py#L688) | 688 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000689](../../tests/test_web_agent.py#L689) | 689 | `"    assert agent.planner_model == \"example/custom-model\""` | — |
| [SRC-F725E90B2A-L000690](../../tests/test_web_agent.py#L690) | 690 | `"    assert agent.answer_model == \"example/custom-model\""` | — |
| [SRC-F725E90B2A-L000691](../../tests/test_web_agent.py#L691) | 691 | `"    assert agent.review_model == \"example/custom-model\""` | — |
| [SRC-F725E90B2A-L000692](../../tests/test_web_agent.py#L692) | 692 | `""` | — |
| [SRC-F725E90B2A-L000693](../../tests/test_web_agent.py#L693) | 693 | `""` | — |
| [SRC-F725E90B2A-L000694](../../tests/test_web_agent.py#L694) | 694 | `"def test_completion_uses_fallback_model_after_primary_http_error(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000695](../../tests/test_web_agent.py#L695) | 695 | `"    import io"` | — |
| [SRC-F725E90B2A-L000696](../../tests/test_web_agent.py#L696) | 696 | `"    import json"` | — |
| [SRC-F725E90B2A-L000697](../../tests/test_web_agent.py#L697) | 697 | `"    import urllib.error"` | — |
| [SRC-F725E90B2A-L000698](../../tests/test_web_agent.py#L698) | 698 | `""` | — |
| [SRC-F725E90B2A-L000699](../../tests/test_web_agent.py#L699) | 699 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000700](../../tests/test_web_agent.py#L700) | 700 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000701](../../tests/test_web_agent.py#L701) | 701 | `"    agent.fallback_model = \"openrouter/free\""` | — |
| [SRC-F725E90B2A-L000702](../../tests/test_web_agent.py#L702) | 702 | `"    called = []"` | — |
| [SRC-F725E90B2A-L000703](../../tests/test_web_agent.py#L703) | 703 | `""` | — |
| [SRC-F725E90B2A-L000704](../../tests/test_web_agent.py#L704) | 704 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000705](../../tests/test_web_agent.py#L705) | 705 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L000706](../../tests/test_web_agent.py#L706) | 706 | `"            return self"` | — |
| [SRC-F725E90B2A-L000707](../../tests/test_web_agent.py#L707) | 707 | `""` | — |
| [SRC-F725E90B2A-L000708](../../tests/test_web_agent.py#L708) | 708 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L000709](../../tests/test_web_agent.py#L709) | 709 | `"            return False"` | — |
| [SRC-F725E90B2A-L000710](../../tests/test_web_agent.py#L710) | 710 | `""` | — |
| [SRC-F725E90B2A-L000711](../../tests/test_web_agent.py#L711) | 711 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L000712](../../tests/test_web_agent.py#L712) | 712 | `"            return json.dumps({"` | — |
| [SRC-F725E90B2A-L000713](../../tests/test_web_agent.py#L713) | 713 | `"                \"choices\": [{"` | — |
| [SRC-F725E90B2A-L000714](../../tests/test_web_agent.py#L714) | 714 | `"                    \"message\": {\"content\": \"إجابة من النموذج الاحتياطي\"},"` | — |
| [SRC-F725E90B2A-L000715](../../tests/test_web_agent.py#L715) | 715 | `"                    \"finish_reason\": \"stop\","` | — |
| [SRC-F725E90B2A-L000716](../../tests/test_web_agent.py#L716) | 716 | `"                }]"` | — |
| [SRC-F725E90B2A-L000717](../../tests/test_web_agent.py#L717) | 717 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000718](../../tests/test_web_agent.py#L718) | 718 | `""` | — |
| [SRC-F725E90B2A-L000719](../../tests/test_web_agent.py#L719) | 719 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L000720](../../tests/test_web_agent.py#L720) | 720 | `"        payload = json.loads(request.data.decode(\"utf-8\"))"` | — |
| [SRC-F725E90B2A-L000721](../../tests/test_web_agent.py#L721) | 721 | `"        called.append(payload[\"model\"])"` | — |
| [SRC-F725E90B2A-L000722](../../tests/test_web_agent.py#L722) | 722 | `"        if payload[\"model\"] == \"broken/primary\":"` | — |
| [SRC-F725E90B2A-L000723](../../tests/test_web_agent.py#L723) | 723 | `"            raise urllib.error.HTTPError("` | — |
| [SRC-F725E90B2A-L000724](../../tests/test_web_agent.py#L724) | 724 | `"                request.full_url,"` | — |
| [SRC-F725E90B2A-L000725](../../tests/test_web_agent.py#L725) | 725 | `"                503,"` | — |
| [SRC-F725E90B2A-L000726](../../tests/test_web_agent.py#L726) | 726 | `"                \"service unavailable\","` | — |
| [SRC-F725E90B2A-L000727](../../tests/test_web_agent.py#L727) | 727 | `"                hdrs=None,"` | — |
| [SRC-F725E90B2A-L000728](../../tests/test_web_agent.py#L728) | 728 | `"                fp=io.BytesIO(b\"private provider diagnostics\"),"` | — |
| [SRC-F725E90B2A-L000729](../../tests/test_web_agent.py#L729) | 729 | `"            )"` | — |
| [SRC-F725E90B2A-L000730](../../tests/test_web_agent.py#L730) | 730 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L000731](../../tests/test_web_agent.py#L731) | 731 | `""` | — |
| [SRC-F725E90B2A-L000732](../../tests/test_web_agent.py#L732) | 732 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L000733](../../tests/test_web_agent.py#L733) | 733 | `"    result = agent._request_completion("` | — |
| [SRC-F725E90B2A-L000734](../../tests/test_web_agent.py#L734) | 734 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-F725E90B2A-L000735](../../tests/test_web_agent.py#L735) | 735 | `"        model=\"broken/primary\","` | — |
| [SRC-F725E90B2A-L000736](../../tests/test_web_agent.py#L736) | 736 | `"    )"` | — |
| [SRC-F725E90B2A-L000737](../../tests/test_web_agent.py#L737) | 737 | `""` | — |
| [SRC-F725E90B2A-L000738](../../tests/test_web_agent.py#L738) | 738 | `"    assert result == \"إجابة من النموذج الاحتياطي\""` | — |
| [SRC-F725E90B2A-L000739](../../tests/test_web_agent.py#L739) | 739 | `"    assert called == [\"broken/primary\", \"openrouter/free\"]"` | — |
| [SRC-F725E90B2A-L000740](../../tests/test_web_agent.py#L740) | 740 | `"    assert agent.model_usage == [{"` | — |
| [SRC-F725E90B2A-L000741](../../tests/test_web_agent.py#L741) | 741 | `"        \"requested_model\": \"broken/primary\","` | — |
| [SRC-F725E90B2A-L000742](../../tests/test_web_agent.py#L742) | 742 | `"        \"used_model\": \"openrouter/free\","` | — |
| [SRC-F725E90B2A-L000743](../../tests/test_web_agent.py#L743) | 743 | `"        \"fallback_used\": \"true\","` | — |
| [SRC-F725E90B2A-L000744](../../tests/test_web_agent.py#L744) | 744 | `"    }]"` | — |
| [SRC-F725E90B2A-L000745](../../tests/test_web_agent.py#L745) | 745 | `""` | — |
| [SRC-F725E90B2A-L000746](../../tests/test_web_agent.py#L746) | 746 | `""` | — |
| [SRC-F725E90B2A-L000747](../../tests/test_web_agent.py#L747) | 747 | `""` | — |
| [SRC-F725E90B2A-L000748](../../tests/test_web_agent.py#L748) | 748 | `""` | — |
| [SRC-F725E90B2A-L000749](../../tests/test_web_agent.py#L749) | 749 | `"def test_generator_rejects_silent_character_limit_truncation(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000750](../../tests/test_web_agent.py#L750) | 750 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000751](../../tests/test_web_agent.py#L751) | 751 | `"    monkeypatch.setattr(agent, \"_request_completion\", lambda *args, **kwargs: \"ن\" * 24_001)"` | — |
| [SRC-F725E90B2A-L000752](../../tests/test_web_agent.py#L752) | 752 | `""` | — |
| [SRC-F725E90B2A-L000753](../../tests/test_web_agent.py#L753) | 753 | `"    with pytest.raises(RuntimeError, match=\"تجاوزت حد طول النص\"):"` | — |
| [SRC-F725E90B2A-L000754](../../tests/test_web_agent.py#L754) | 754 | `"        agent._generate("` | — |
| [SRC-F725E90B2A-L000755](../../tests/test_web_agent.py#L755) | 755 | `"            question=\"لخص هذا المصدر\","` | — |
| [SRC-F725E90B2A-L000756](../../tests/test_web_agent.py#L756) | 756 | `"            history=[],"` | — |
| [SRC-F725E90B2A-L000757](../../tests/test_web_agent.py#L757) | 757 | `"            sources=[sample_source(0), sample_source(1)],"` | — |
| [SRC-F725E90B2A-L000758](../../tests/test_web_agent.py#L758) | 758 | `"            search_warning=None,"` | — |
| [SRC-F725E90B2A-L000759](../../tests/test_web_agent.py#L759) | 759 | `"            research_plan={\"depth\": \"standard\", \"queries\": [\"لخص هذا المصدر\"]},"` | — |
| [SRC-F725E90B2A-L000760](../../tests/test_web_agent.py#L760) | 760 | `"            search_report={},"` | — |
| [SRC-F725E90B2A-L000761](../../tests/test_web_agent.py#L761) | 761 | `"        )"` | — |
| [SRC-F725E90B2A-L000762](../../tests/test_web_agent.py#L762) | 762 | `""` | — |
| [SRC-F725E90B2A-L000763](../../tests/test_web_agent.py#L763) | 763 | `""` | — |
| [SRC-F725E90B2A-L000764](../../tests/test_web_agent.py#L764) | 764 | `"def test_completion_discards_truncated_primary_and_uses_complete_fallback(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000765](../../tests/test_web_agent.py#L765) | 765 | `"    import json"` | — |
| [SRC-F725E90B2A-L000766](../../tests/test_web_agent.py#L766) | 766 | `""` | — |
| [SRC-F725E90B2A-L000767](../../tests/test_web_agent.py#L767) | 767 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000768](../../tests/test_web_agent.py#L768) | 768 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000769](../../tests/test_web_agent.py#L769) | 769 | `"    agent.fallback_model = \"openrouter/free\""` | — |
| [SRC-F725E90B2A-L000770](../../tests/test_web_agent.py#L770) | 770 | `"    called = []"` | — |
| [SRC-F725E90B2A-L000771](../../tests/test_web_agent.py#L771) | 771 | `""` | — |
| [SRC-F725E90B2A-L000772](../../tests/test_web_agent.py#L772) | 772 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000773](../../tests/test_web_agent.py#L773) | 773 | `"        def __init__(self, content, finish_reason):"` | — |
| [SRC-F725E90B2A-L000774](../../tests/test_web_agent.py#L774) | 774 | `"            self.body = json.dumps({"` | — |
| [SRC-F725E90B2A-L000775](../../tests/test_web_agent.py#L775) | 775 | `"                \"choices\": [{"` | — |
| [SRC-F725E90B2A-L000776](../../tests/test_web_agent.py#L776) | 776 | `"                    \"message\": {\"content\": content},"` | — |
| [SRC-F725E90B2A-L000777](../../tests/test_web_agent.py#L777) | 777 | `"                    \"finish_reason\": finish_reason,"` | — |
| [SRC-F725E90B2A-L000778](../../tests/test_web_agent.py#L778) | 778 | `"                }]"` | — |
| [SRC-F725E90B2A-L000779](../../tests/test_web_agent.py#L779) | 779 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000780](../../tests/test_web_agent.py#L780) | 780 | `""` | — |
| [SRC-F725E90B2A-L000781](../../tests/test_web_agent.py#L781) | 781 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L000782](../../tests/test_web_agent.py#L782) | 782 | `"            return self"` | — |
| [SRC-F725E90B2A-L000783](../../tests/test_web_agent.py#L783) | 783 | `""` | — |
| [SRC-F725E90B2A-L000784](../../tests/test_web_agent.py#L784) | 784 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L000785](../../tests/test_web_agent.py#L785) | 785 | `"            return False"` | — |
| [SRC-F725E90B2A-L000786](../../tests/test_web_agent.py#L786) | 786 | `""` | — |
| [SRC-F725E90B2A-L000787](../../tests/test_web_agent.py#L787) | 787 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L000788](../../tests/test_web_agent.py#L788) | 788 | `"            return self.body"` | — |
| [SRC-F725E90B2A-L000789](../../tests/test_web_agent.py#L789) | 789 | `""` | — |
| [SRC-F725E90B2A-L000790](../../tests/test_web_agent.py#L790) | 790 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L000791](../../tests/test_web_agent.py#L791) | 791 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-F725E90B2A-L000792](../../tests/test_web_agent.py#L792) | 792 | `"        called.append(model)"` | — |
| [SRC-F725E90B2A-L000793](../../tests/test_web_agent.py#L793) | 793 | `"        if model == \"broken/primary\":"` | — |
| [SRC-F725E90B2A-L000794](../../tests/test_web_agent.py#L794) | 794 | `"            return FakeResponse(\"جزء مبتور لا يجوز عرضه\", \"length\")"` | — |
| [SRC-F725E90B2A-L000795](../../tests/test_web_agent.py#L795) | 795 | `"        return FakeResponse(\"إجابة مكتملة\", \"stop\")"` | — |
| [SRC-F725E90B2A-L000796](../../tests/test_web_agent.py#L796) | 796 | `""` | — |
| [SRC-F725E90B2A-L000797](../../tests/test_web_agent.py#L797) | 797 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L000798](../../tests/test_web_agent.py#L798) | 798 | `"    result = agent._request_completion("` | — |
| [SRC-F725E90B2A-L000799](../../tests/test_web_agent.py#L799) | 799 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-F725E90B2A-L000800](../../tests/test_web_agent.py#L800) | 800 | `"        model=\"broken/primary\","` | — |
| [SRC-F725E90B2A-L000801](../../tests/test_web_agent.py#L801) | 801 | `"    )"` | — |
| [SRC-F725E90B2A-L000802](../../tests/test_web_agent.py#L802) | 802 | `""` | — |
| [SRC-F725E90B2A-L000803](../../tests/test_web_agent.py#L803) | 803 | `"    assert result == \"إجابة مكتملة\""` | — |
| [SRC-F725E90B2A-L000804](../../tests/test_web_agent.py#L804) | 804 | `"    assert called == [\"broken/primary\", \"openrouter/free\"]"` | — |
| [SRC-F725E90B2A-L000805](../../tests/test_web_agent.py#L805) | 805 | `"    assert \"جزء مبتور لا يجوز عرضه\" not in result"` | — |
| [SRC-F725E90B2A-L000806](../../tests/test_web_agent.py#L806) | 806 | `"    assert agent.model_usage == [{"` | — |
| [SRC-F725E90B2A-L000807](../../tests/test_web_agent.py#L807) | 807 | `"        \"requested_model\": \"broken/primary\","` | — |
| [SRC-F725E90B2A-L000808](../../tests/test_web_agent.py#L808) | 808 | `"        \"used_model\": \"openrouter/free\","` | — |
| [SRC-F725E90B2A-L000809](../../tests/test_web_agent.py#L809) | 809 | `"        \"fallback_used\": \"true\","` | — |
| [SRC-F725E90B2A-L000810](../../tests/test_web_agent.py#L810) | 810 | `"    }]"` | — |
| [SRC-F725E90B2A-L000811](../../tests/test_web_agent.py#L811) | 811 | `""` | — |
| [SRC-F725E90B2A-L000812](../../tests/test_web_agent.py#L812) | 812 | `""` | — |
| [SRC-F725E90B2A-L000813](../../tests/test_web_agent.py#L813) | 813 | `"def test_completion_rejects_response_when_all_models_are_truncated(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000814](../../tests/test_web_agent.py#L814) | 814 | `"    import json"` | — |
| [SRC-F725E90B2A-L000815](../../tests/test_web_agent.py#L815) | 815 | `""` | — |
| [SRC-F725E90B2A-L000816](../../tests/test_web_agent.py#L816) | 816 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000817](../../tests/test_web_agent.py#L817) | 817 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000818](../../tests/test_web_agent.py#L818) | 818 | `"    agent.fallback_model = \"fallback/model\""` | — |
| [SRC-F725E90B2A-L000819](../../tests/test_web_agent.py#L819) | 819 | `"    called = []"` | — |
| [SRC-F725E90B2A-L000820](../../tests/test_web_agent.py#L820) | 820 | `""` | — |
| [SRC-F725E90B2A-L000821](../../tests/test_web_agent.py#L821) | 821 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000822](../../tests/test_web_agent.py#L822) | 822 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L000823](../../tests/test_web_agent.py#L823) | 823 | `"            return self"` | — |
| [SRC-F725E90B2A-L000824](../../tests/test_web_agent.py#L824) | 824 | `""` | — |
| [SRC-F725E90B2A-L000825](../../tests/test_web_agent.py#L825) | 825 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L000826](../../tests/test_web_agent.py#L826) | 826 | `"            return False"` | — |
| [SRC-F725E90B2A-L000827](../../tests/test_web_agent.py#L827) | 827 | `""` | — |
| [SRC-F725E90B2A-L000828](../../tests/test_web_agent.py#L828) | 828 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L000829](../../tests/test_web_agent.py#L829) | 829 | `"            return json.dumps({"` | — |
| [SRC-F725E90B2A-L000830](../../tests/test_web_agent.py#L830) | 830 | `"                \"choices\": [{"` | — |
| [SRC-F725E90B2A-L000831](../../tests/test_web_agent.py#L831) | 831 | `"                    \"message\": {\"content\": \"نص مبتور\"},"` | — |
| [SRC-F725E90B2A-L000832](../../tests/test_web_agent.py#L832) | 832 | `"                    \"finish_reason\": \"length\","` | — |
| [SRC-F725E90B2A-L000833](../../tests/test_web_agent.py#L833) | 833 | `"                }]"` | — |
| [SRC-F725E90B2A-L000834](../../tests/test_web_agent.py#L834) | 834 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000835](../../tests/test_web_agent.py#L835) | 835 | `""` | — |
| [SRC-F725E90B2A-L000836](../../tests/test_web_agent.py#L836) | 836 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L000837](../../tests/test_web_agent.py#L837) | 837 | `"        called.append(json.loads(request.data.decode(\"utf-8\"))[\"model\"])"` | — |
| [SRC-F725E90B2A-L000838](../../tests/test_web_agent.py#L838) | 838 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L000839](../../tests/test_web_agent.py#L839) | 839 | `""` | — |
| [SRC-F725E90B2A-L000840](../../tests/test_web_agent.py#L840) | 840 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L000841](../../tests/test_web_agent.py#L841) | 841 | `"    with pytest.raises(RuntimeError, match=\"مبتورة\"):"` | — |
| [SRC-F725E90B2A-L000842](../../tests/test_web_agent.py#L842) | 842 | `"        agent._request_completion("` | — |
| [SRC-F725E90B2A-L000843](../../tests/test_web_agent.py#L843) | 843 | `"            [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-F725E90B2A-L000844](../../tests/test_web_agent.py#L844) | 844 | `"            model=\"broken/primary\","` | — |
| [SRC-F725E90B2A-L000845](../../tests/test_web_agent.py#L845) | 845 | `"        )"` | — |
| [SRC-F725E90B2A-L000846](../../tests/test_web_agent.py#L846) | 846 | `""` | — |
| [SRC-F725E90B2A-L000847](../../tests/test_web_agent.py#L847) | 847 | `"    assert called == [\"broken/primary\", \"fallback/model\"]"` | — |
| [SRC-F725E90B2A-L000848](../../tests/test_web_agent.py#L848) | 848 | `"    assert agent.model_usage == []"` | — |
| [SRC-F725E90B2A-L000849](../../tests/test_web_agent.py#L849) | 849 | `""` | — |
| [SRC-F725E90B2A-L000850](../../tests/test_web_agent.py#L850) | 850 | `""` | — |
| [SRC-F725E90B2A-L000851](../../tests/test_web_agent.py#L851) | 851 | `"def test_completion_falls_back_for_malformed_choice(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000852](../../tests/test_web_agent.py#L852) | 852 | `"    import json"` | — |
| [SRC-F725E90B2A-L000853](../../tests/test_web_agent.py#L853) | 853 | `""` | — |
| [SRC-F725E90B2A-L000854](../../tests/test_web_agent.py#L854) | 854 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000855](../../tests/test_web_agent.py#L855) | 855 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000856](../../tests/test_web_agent.py#L856) | 856 | `"    agent.fallback_model = \"fallback/model\""` | — |
| [SRC-F725E90B2A-L000857](../../tests/test_web_agent.py#L857) | 857 | `"    called = []"` | — |
| [SRC-F725E90B2A-L000858](../../tests/test_web_agent.py#L858) | 858 | `""` | — |
| [SRC-F725E90B2A-L000859](../../tests/test_web_agent.py#L859) | 859 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000860](../../tests/test_web_agent.py#L860) | 860 | `"        def __init__(self, body):"` | — |
| [SRC-F725E90B2A-L000861](../../tests/test_web_agent.py#L861) | 861 | `"            self.body = body"` | — |
| [SRC-F725E90B2A-L000862](../../tests/test_web_agent.py#L862) | 862 | `""` | — |
| [SRC-F725E90B2A-L000863](../../tests/test_web_agent.py#L863) | 863 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L000864](../../tests/test_web_agent.py#L864) | 864 | `"            return self"` | — |
| [SRC-F725E90B2A-L000865](../../tests/test_web_agent.py#L865) | 865 | `""` | — |
| [SRC-F725E90B2A-L000866](../../tests/test_web_agent.py#L866) | 866 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L000867](../../tests/test_web_agent.py#L867) | 867 | `"            return False"` | — |
| [SRC-F725E90B2A-L000868](../../tests/test_web_agent.py#L868) | 868 | `""` | — |
| [SRC-F725E90B2A-L000869](../../tests/test_web_agent.py#L869) | 869 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L000870](../../tests/test_web_agent.py#L870) | 870 | `"            return self.body"` | — |
| [SRC-F725E90B2A-L000871](../../tests/test_web_agent.py#L871) | 871 | `""` | — |
| [SRC-F725E90B2A-L000872](../../tests/test_web_agent.py#L872) | 872 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L000873](../../tests/test_web_agent.py#L873) | 873 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-F725E90B2A-L000874](../../tests/test_web_agent.py#L874) | 874 | `"        called.append(model)"` | — |
| [SRC-F725E90B2A-L000875](../../tests/test_web_agent.py#L875) | 875 | `"        choices = ("` | — |
| [SRC-F725E90B2A-L000876](../../tests/test_web_agent.py#L876) | 876 | `"            [\"malformed choice\"]"` | — |
| [SRC-F725E90B2A-L000877](../../tests/test_web_agent.py#L877) | 877 | `"            if model == \"broken/primary\""` | — |
| [SRC-F725E90B2A-L000878](../../tests/test_web_agent.py#L878) | 878 | `"            else [{\"message\": {\"content\": \"fallback answer\"}, \"finish_reason\": \"stop\"}]"` | — |
| [SRC-F725E90B2A-L000879](../../tests/test_web_agent.py#L879) | 879 | `"        )"` | — |
| [SRC-F725E90B2A-L000880](../../tests/test_web_agent.py#L880) | 880 | `"        return FakeResponse(json.dumps({\"choices\": choices}).encode(\"utf-8\"))"` | — |
| [SRC-F725E90B2A-L000881](../../tests/test_web_agent.py#L881) | 881 | `""` | — |
| [SRC-F725E90B2A-L000882](../../tests/test_web_agent.py#L882) | 882 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L000883](../../tests/test_web_agent.py#L883) | 883 | `"    result = agent._request_completion("` | — |
| [SRC-F725E90B2A-L000884](../../tests/test_web_agent.py#L884) | 884 | `"        [{\"role\": \"user\", \"content\": \"test\"}],"` | — |
| [SRC-F725E90B2A-L000885](../../tests/test_web_agent.py#L885) | 885 | `"        model=\"broken/primary\","` | — |
| [SRC-F725E90B2A-L000886](../../tests/test_web_agent.py#L886) | 886 | `"    )"` | — |
| [SRC-F725E90B2A-L000887](../../tests/test_web_agent.py#L887) | 887 | `""` | — |
| [SRC-F725E90B2A-L000888](../../tests/test_web_agent.py#L888) | 888 | `"    assert result == \"fallback answer\""` | — |
| [SRC-F725E90B2A-L000889](../../tests/test_web_agent.py#L889) | 889 | `"    assert called == [\"broken/primary\", \"fallback/model\"]"` | — |
| [SRC-F725E90B2A-L000890](../../tests/test_web_agent.py#L890) | 890 | `""` | — |
| [SRC-F725E90B2A-L000891](../../tests/test_web_agent.py#L891) | 891 | `""` | — |
| [SRC-F725E90B2A-L000892](../../tests/test_web_agent.py#L892) | 892 | `"def test_health_status_reports_models_without_credentials(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000893](../../tests/test_web_agent.py#L893) | 893 | `"    monkeypatch.delenv(\"OPENROUTER_API_KEY\", raising=False)"` | — |
| [SRC-F725E90B2A-L000894](../../tests/test_web_agent.py#L894) | 894 | `"    monkeypatch.delenv(\"OMARAI_LLM_API_KEY\", raising=False)"` | — |
| [SRC-F725E90B2A-L000895](../../tests/test_web_agent.py#L895) | 895 | `"    status = WebAgent.status()"` | — |
| [SRC-F725E90B2A-L000896](../../tests/test_web_agent.py#L896) | 896 | `"    assert status[\"planner_model\"] == \"nvidia/nemotron-3-ultra-550b-a55b:free\""` | — |
| [SRC-F725E90B2A-L000897](../../tests/test_web_agent.py#L897) | 897 | `"    assert status[\"answer_model\"] == \"google/gemma-4-31b-it:free\""` | — |
| [SRC-F725E90B2A-L000898](../../tests/test_web_agent.py#L898) | 898 | `"    assert status[\"fallback_model\"] == \"openrouter/free\""` | — |
| [SRC-F725E90B2A-L000899](../../tests/test_web_agent.py#L899) | 899 | `"    assert status[\"language_model_configured\"] is False"` | — |
| [SRC-F725E90B2A-L000900](../../tests/test_web_agent.py#L900) | 900 | `"    assert status[\"verification_scope\"][\"kind\"] == \"configuration_snapshot\""` | — |
| [SRC-F725E90B2A-L000901](../../tests/test_web_agent.py#L901) | 901 | `"    assert status[\"verification_scope\"][\"live_network_checks_performed\"] is False"` | — |
| [SRC-F725E90B2A-L000902](../../tests/test_web_agent.py#L902) | 902 | `"    assert status[\"verification_scope\"][\"language_model_configured_means\"] == ("` | — |
| [SRC-F725E90B2A-L000903](../../tests/test_web_agent.py#L903) | 903 | `"        \"credential_present_not_successful_completion\""` | — |
| [SRC-F725E90B2A-L000904](../../tests/test_web_agent.py#L904) | 904 | `"    )"` | — |
| [SRC-F725E90B2A-L000905](../../tests/test_web_agent.py#L905) | 905 | `"    assert status[\"verification_scope\"][\"live_diagnostics_endpoint\"] == \"POST /api/diagnostics\""` | — |
| [SRC-F725E90B2A-L000906](../../tests/test_web_agent.py#L906) | 906 | `"    assert \"api_key\" not in status"` | — |
| [SRC-F725E90B2A-L000907](../../tests/test_web_agent.py#L907) | 907 | `""` | — |
| [SRC-F725E90B2A-L000908](../../tests/test_web_agent.py#L908) | 908 | `""` | — |
| [SRC-F725E90B2A-L000909](../../tests/test_web_agent.py#L909) | 909 | `""` | — |
| [SRC-F725E90B2A-L000910](../../tests/test_web_agent.py#L910) | 910 | `"def test_health_status_exposes_external_model_privacy_notice_without_secrets(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000911](../../tests/test_web_agent.py#L911) | 911 | `"    monkeypatch.delenv(\"OPENROUTER_API_KEY\", raising=False)"` | — |
| [SRC-F725E90B2A-L000912](../../tests/test_web_agent.py#L912) | 912 | `"    monkeypatch.delenv(\"OMARAI_LLM_API_KEY\", raising=False)"` | — |
| [SRC-F725E90B2A-L000913](../../tests/test_web_agent.py#L913) | 913 | `"    status = WebAgent.status()"` | — |
| [SRC-F725E90B2A-L000914](../../tests/test_web_agent.py#L914) | 914 | `"    notice = status[\"external_model_privacy_notice\"]"` | — |
| [SRC-F725E90B2A-L000915](../../tests/test_web_agent.py#L915) | 915 | `"    assert \"external model provider\" in notice"` | — |
| [SRC-F725E90B2A-L000916](../../tests/test_web_agent.py#L916) | 916 | `"    assert \"personal/confidential customer data\" in notice"` | — |
| [SRC-F725E90B2A-L000917](../../tests/test_web_agent.py#L917) | 917 | `"    assert \"api_key\" not in status"` | — |
| [SRC-F725E90B2A-L000918](../../tests/test_web_agent.py#L918) | 918 | `"    assert \"OPENROUTER_API_KEY\" not in str(status)"` | — |
| [SRC-F725E90B2A-L000919](../../tests/test_web_agent.py#L919) | 919 | `""` | — |
| [SRC-F725E90B2A-L000920](../../tests/test_web_agent.py#L920) | 920 | `""` | — |
| [SRC-F725E90B2A-L000921](../../tests/test_web_agent.py#L921) | 921 | `""` | — |
| [SRC-F725E90B2A-L000922](../../tests/test_web_agent.py#L922) | 922 | `"def test_diagnostics_runs_real_search_and_can_skip_paid_or_rate_limited_model_calls(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000923](../../tests/test_web_agent.py#L923) | 923 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000924](../../tests/test_web_agent.py#L924) | 924 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: ["` | — |
| [SRC-F725E90B2A-L000925](../../tests/test_web_agent.py#L925) | 925 | `"        {\"provider\": \"duckduckgo_html\", \"url\": \"https://example.com/a\"},"` | — |
| [SRC-F725E90B2A-L000926](../../tests/test_web_agent.py#L926) | 926 | `"        {\"provider\": \"bing_rss\", \"url\": \"https://example.com/b\"},"` | — |
| [SRC-F725E90B2A-L000927](../../tests/test_web_agent.py#L927) | 927 | `"    ])"` | — |
| [SRC-F725E90B2A-L000928](../../tests/test_web_agent.py#L928) | 928 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000929](../../tests/test_web_agent.py#L929) | 929 | `"        agent,"` | — |
| [SRC-F725E90B2A-L000930](../../tests/test_web_agent.py#L930) | 930 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L000931](../../tests/test_web_agent.py#L931) | 931 | `"        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError(\"model should be skipped\")),"` | — |
| [SRC-F725E90B2A-L000932](../../tests/test_web_agent.py#L932) | 932 | `"    )"` | — |
| [SRC-F725E90B2A-L000933](../../tests/test_web_agent.py#L933) | 933 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L000934](../../tests/test_web_agent.py#L934) | 934 | `"    assert report[\"checks\"][\"web_search\"][\"status\"] == \"passed\""` | — |
| [SRC-F725E90B2A-L000935](../../tests/test_web_agent.py#L935) | 935 | `"    assert report[\"checks\"][\"web_search\"][\"provider_counts\"] == {"` | — |
| [SRC-F725E90B2A-L000936](../../tests/test_web_agent.py#L936) | 936 | `"        \"duckduckgo_html\": 1, \"bing_rss\": 1"` | — |
| [SRC-F725E90B2A-L000937](../../tests/test_web_agent.py#L937) | 937 | `"    }"` | — |
| [SRC-F725E90B2A-L000938](../../tests/test_web_agent.py#L938) | 938 | `"    assert report[\"checks\"][\"language_model\"][\"status\"] == \"skipped\""` | — |
| [SRC-F725E90B2A-L000939](../../tests/test_web_agent.py#L939) | 939 | `"    assert report[\"checks\"][\"social_search\"][\"status\"] == \"skipped\""` | — |
| [SRC-F725E90B2A-L000940](../../tests/test_web_agent.py#L940) | 940 | `"    assert report[\"elapsed_ms\"] >= 0"` | — |
| [SRC-F725E90B2A-L000941](../../tests/test_web_agent.py#L941) | 941 | `"    assert \"api_key\" not in str(report)"` | — |
| [SRC-F725E90B2A-L000942](../../tests/test_web_agent.py#L942) | 942 | `""` | — |
| [SRC-F725E90B2A-L000943](../../tests/test_web_agent.py#L943) | 943 | `""` | — |
| [SRC-F725E90B2A-L000944](../../tests/test_web_agent.py#L944) | 944 | `"def test_diagnostics_calls_a_model_only_when_explicitly_requested(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000945](../../tests/test_web_agent.py#L945) | 945 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000946](../../tests/test_web_agent.py#L946) | 946 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000947](../../tests/test_web_agent.py#L947) | 947 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: ["` | — |
| [SRC-F725E90B2A-L000948](../../tests/test_web_agent.py#L948) | 948 | `"        {\"provider\": \"duckduckgo_html\", \"url\": \"https://example.com/a\"}"` | — |
| [SRC-F725E90B2A-L000949](../../tests/test_web_agent.py#L949) | 949 | `"    ])"` | — |
| [SRC-F725E90B2A-L000950](../../tests/test_web_agent.py#L950) | 950 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000951](../../tests/test_web_agent.py#L951) | 951 | `""` | — |
| [SRC-F725E90B2A-L000952](../../tests/test_web_agent.py#L952) | 952 | `"    def completion(*args, **kwargs):"` | — |
| [SRC-F725E90B2A-L000953](../../tests/test_web_agent.py#L953) | 953 | `"        calls.append(kwargs.get(\"model\"))"` | — |
| [SRC-F725E90B2A-L000954](../../tests/test_web_agent.py#L954) | 954 | `"        agent.model_usage.append({"` | — |
| [SRC-F725E90B2A-L000955](../../tests/test_web_agent.py#L955) | 955 | `"            \"requested_model\": kwargs.get(\"model\", \"\"),"` | — |
| [SRC-F725E90B2A-L000956](../../tests/test_web_agent.py#L956) | 956 | `"            \"used_model\": kwargs.get(\"model\", \"\"),"` | — |
| [SRC-F725E90B2A-L000957](../../tests/test_web_agent.py#L957) | 957 | `"            \"fallback_used\": \"false\","` | — |
| [SRC-F725E90B2A-L000958](../../tests/test_web_agent.py#L958) | 958 | `"        })"` | — |
| [SRC-F725E90B2A-L000959](../../tests/test_web_agent.py#L959) | 959 | `"        return \"OK\""` | — |
| [SRC-F725E90B2A-L000960](../../tests/test_web_agent.py#L960) | 960 | `""` | — |
| [SRC-F725E90B2A-L000961](../../tests/test_web_agent.py#L961) | 961 | `"    monkeypatch.setattr(agent, \"_request_completion\", completion)"` | — |
| [SRC-F725E90B2A-L000962](../../tests/test_web_agent.py#L962) | 962 | `"    report = agent.diagnostics(test_model=True, test_social=False)"` | — |
| [SRC-F725E90B2A-L000963](../../tests/test_web_agent.py#L963) | 963 | `"    assert report[\"checks\"][\"language_model\"][\"status\"] == \"passed\""` | — |
| [SRC-F725E90B2A-L000964](../../tests/test_web_agent.py#L964) | 964 | `"    assert calls == [agent.answer_model]"` | — |
| [SRC-F725E90B2A-L000965](../../tests/test_web_agent.py#L965) | 965 | `"    assert len(report[\"model_usage\"]) == 1"` | — |
| [SRC-F725E90B2A-L000966](../../tests/test_web_agent.py#L966) | 966 | `""` | — |
| [SRC-F725E90B2A-L000967](../../tests/test_web_agent.py#L967) | 967 | `""` | — |
| [SRC-F725E90B2A-L000968](../../tests/test_web_agent.py#L968) | 968 | `""` | — |
| [SRC-F725E90B2A-L000969](../../tests/test_web_agent.py#L969) | 969 | `""` | — |
| [SRC-F725E90B2A-L000970](../../tests/test_web_agent.py#L970) | 970 | `"def test_diagnostics_reports_degraded_when_search_has_no_results_and_model_is_unconfigured(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000971](../../tests/test_web_agent.py#L971) | 971 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000972](../../tests/test_web_agent.py#L972) | 972 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L000973](../../tests/test_web_agent.py#L973) | 973 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: [])"` | — |
| [SRC-F725E90B2A-L000974](../../tests/test_web_agent.py#L974) | 974 | `""` | — |
| [SRC-F725E90B2A-L000975](../../tests/test_web_agent.py#L975) | 975 | `"    report = agent.diagnostics(test_model=True, test_social=False)"` | — |
| [SRC-F725E90B2A-L000976](../../tests/test_web_agent.py#L976) | 976 | `""` | — |
| [SRC-F725E90B2A-L000977](../../tests/test_web_agent.py#L977) | 977 | `"    assert report[\"checks\"][\"web_search\"][\"status\"] == \"degraded\""` | — |
| [SRC-F725E90B2A-L000978](../../tests/test_web_agent.py#L978) | 978 | `"    assert report[\"checks\"][\"language_model\"][\"status\"] == \"not_configured\""` | — |
| [SRC-F725E90B2A-L000979](../../tests/test_web_agent.py#L979) | 979 | `"    assert report[\"checks\"][\"social_search\"][\"status\"] == \"skipped\""` | — |
| [SRC-F725E90B2A-L000980](../../tests/test_web_agent.py#L980) | 980 | `"    assert report[\"overall_status\"] == \"degraded\""` | — |
| [SRC-F725E90B2A-L000981](../../tests/test_web_agent.py#L981) | 981 | `""` | — |
| [SRC-F725E90B2A-L000982](../../tests/test_web_agent.py#L982) | 982 | `""` | — |
| [SRC-F725E90B2A-L000983](../../tests/test_web_agent.py#L983) | 983 | `"def test_diagnostics_does_not_report_full_success_when_model_probe_fails(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000984](../../tests/test_web_agent.py#L984) | 984 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000985](../../tests/test_web_agent.py#L985) | 985 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000986](../../tests/test_web_agent.py#L986) | 986 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: ["` | — |
| [SRC-F725E90B2A-L000987](../../tests/test_web_agent.py#L987) | 987 | `"        {\"provider\": \"duckduckgo_html\", \"url\": \"https://example.com/a\"}"` | — |
| [SRC-F725E90B2A-L000988](../../tests/test_web_agent.py#L988) | 988 | `"    ])"` | — |
| [SRC-F725E90B2A-L000989](../../tests/test_web_agent.py#L989) | 989 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000990](../../tests/test_web_agent.py#L990) | 990 | `"        agent,"` | — |
| [SRC-F725E90B2A-L000991](../../tests/test_web_agent.py#L991) | 991 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L000992](../../tests/test_web_agent.py#L992) | 992 | `"        lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError(\"provider unavailable\")),"` | — |
| [SRC-F725E90B2A-L000993](../../tests/test_web_agent.py#L993) | 993 | `"    )"` | — |
| [SRC-F725E90B2A-L000994](../../tests/test_web_agent.py#L994) | 994 | `""` | — |
| [SRC-F725E90B2A-L000995](../../tests/test_web_agent.py#L995) | 995 | `"    report = agent.diagnostics(test_model=True, test_social=False)"` | — |
| [SRC-F725E90B2A-L000996](../../tests/test_web_agent.py#L996) | 996 | `""` | — |
| [SRC-F725E90B2A-L000997](../../tests/test_web_agent.py#L997) | 997 | `"    assert report[\"checks\"][\"web_search\"][\"status\"] == \"passed\""` | — |
| [SRC-F725E90B2A-L000998](../../tests/test_web_agent.py#L998) | 998 | `"    assert report[\"checks\"][\"language_model\"][\"status\"] == \"failed\""` | — |
| [SRC-F725E90B2A-L000999](../../tests/test_web_agent.py#L999) | 999 | `"    assert report[\"overall_status\"] == \"degraded\""` | — |
| [SRC-F725E90B2A-L001000](../../tests/test_web_agent.py#L1000) | 1000 | `"    assert \"test-key\" not in str(report)"` | — |
| [SRC-F725E90B2A-L001001](../../tests/test_web_agent.py#L1001) | 1001 | `""` | — |
| [SRC-F725E90B2A-L001002](../../tests/test_web_agent.py#L1002) | 1002 | `""` | — |
| [SRC-F725E90B2A-L001003](../../tests/test_web_agent.py#L1003) | 1003 | `"def test_openrouter_live_web_search_tool_is_opt_in_and_returns_citations(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001004](../../tests/test_web_agent.py#L1004) | 1004 | `"    import json"` | — |
| [SRC-F725E90B2A-L001005](../../tests/test_web_agent.py#L1005) | 1005 | `""` | — |
| [SRC-F725E90B2A-L001006](../../tests/test_web_agent.py#L1006) | 1006 | `"    monkeypatch.setenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"1\")"` | — |
| [SRC-F725E90B2A-L001007](../../tests/test_web_agent.py#L1007) | 1007 | `"    monkeypatch.setenv(\"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\")"` | — |
| [SRC-F725E90B2A-L001008](../../tests/test_web_agent.py#L1008) | 1008 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001009](../../tests/test_web_agent.py#L1009) | 1009 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L001010](../../tests/test_web_agent.py#L1010) | 1010 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L001011](../../tests/test_web_agent.py#L1011) | 1011 | `""` | — |
| [SRC-F725E90B2A-L001012](../../tests/test_web_agent.py#L1012) | 1012 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L001013](../../tests/test_web_agent.py#L1013) | 1013 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L001014](../../tests/test_web_agent.py#L1014) | 1014 | `"            return self"` | — |
| [SRC-F725E90B2A-L001015](../../tests/test_web_agent.py#L1015) | 1015 | `""` | — |
| [SRC-F725E90B2A-L001016](../../tests/test_web_agent.py#L1016) | 1016 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L001017](../../tests/test_web_agent.py#L1017) | 1017 | `"            return False"` | — |
| [SRC-F725E90B2A-L001018](../../tests/test_web_agent.py#L1018) | 1018 | `""` | — |
| [SRC-F725E90B2A-L001019](../../tests/test_web_agent.py#L1019) | 1019 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L001020](../../tests/test_web_agent.py#L1020) | 1020 | `"            return json.dumps({"` | — |
| [SRC-F725E90B2A-L001021](../../tests/test_web_agent.py#L1021) | 1021 | `"                \"choices\": [{"` | — |
| [SRC-F725E90B2A-L001022](../../tests/test_web_agent.py#L1022) | 1022 | `"                    \"message\": {"` | — |
| [SRC-F725E90B2A-L001023](../../tests/test_web_agent.py#L1023) | 1023 | `"                        \"content\": \"تحليل مستند إلى بحث حي.\","` | — |
| [SRC-F725E90B2A-L001024](../../tests/test_web_agent.py#L1024) | 1024 | `"                        \"annotations\": [{"` | — |
| [SRC-F725E90B2A-L001025](../../tests/test_web_agent.py#L1025) | 1025 | `"                            \"type\": \"url_citation\","` | — |
| [SRC-F725E90B2A-L001026](../../tests/test_web_agent.py#L1026) | 1026 | `"                            \"url_citation\": {"` | — |
| [SRC-F725E90B2A-L001027](../../tests/test_web_agent.py#L1027) | 1027 | `"                                \"url\": \"https://example.org/current-report\","` | — |
| [SRC-F725E90B2A-L001028](../../tests/test_web_agent.py#L1028) | 1028 | `"                                \"title\": \"Current public report\","` | — |
| [SRC-F725E90B2A-L001029](../../tests/test_web_agent.py#L1029) | 1029 | `"                                \"content\": \"An excerpt returned by the live search service.\","` | — |
| [SRC-F725E90B2A-L001030](../../tests/test_web_agent.py#L1030) | 1030 | `"                            },"` | — |
| [SRC-F725E90B2A-L001031](../../tests/test_web_agent.py#L1031) | 1031 | `"                        }],"` | — |
| [SRC-F725E90B2A-L001032](../../tests/test_web_agent.py#L1032) | 1032 | `"                    },"` | — |
| [SRC-F725E90B2A-L001033](../../tests/test_web_agent.py#L1033) | 1033 | `"                    \"finish_reason\": \"stop\","` | — |
| [SRC-F725E90B2A-L001034](../../tests/test_web_agent.py#L1034) | 1034 | `"                }]"` | — |
| [SRC-F725E90B2A-L001035](../../tests/test_web_agent.py#L1035) | 1035 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L001036](../../tests/test_web_agent.py#L1036) | 1036 | `""` | — |
| [SRC-F725E90B2A-L001037](../../tests/test_web_agent.py#L1037) | 1037 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L001038](../../tests/test_web_agent.py#L1038) | 1038 | `"        seen[\"payload\"] = json.loads(request.data.decode(\"utf-8\"))"` | — |
| [SRC-F725E90B2A-L001039](../../tests/test_web_agent.py#L1039) | 1039 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L001040](../../tests/test_web_agent.py#L1040) | 1040 | `""` | — |
| [SRC-F725E90B2A-L001041](../../tests/test_web_agent.py#L1041) | 1041 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L001042](../../tests/test_web_agent.py#L1042) | 1042 | `"    result = agent._request_completion("` | — |
| [SRC-F725E90B2A-L001043](../../tests/test_web_agent.py#L1043) | 1043 | `"        [{\"role\": \"user\", \"content\": \"ابحث عن أحدث تقرير\"}],"` | — |
| [SRC-F725E90B2A-L001044](../../tests/test_web_agent.py#L1044) | 1044 | `"        model=\"example/model\","` | — |
| [SRC-F725E90B2A-L001045](../../tests/test_web_agent.py#L1045) | 1045 | `"        enable_web_search=True,"` | — |
| [SRC-F725E90B2A-L001046](../../tests/test_web_agent.py#L1046) | 1046 | `"    )"` | — |
| [SRC-F725E90B2A-L001047](../../tests/test_web_agent.py#L1047) | 1047 | `""` | — |
| [SRC-F725E90B2A-L001048](../../tests/test_web_agent.py#L1048) | 1048 | `"    assert result == \"تحليل مستند إلى بحث حي.\""` | — |
| [SRC-F725E90B2A-L001049](../../tests/test_web_agent.py#L1049) | 1049 | `"    assert seen[\"payload\"][\"tools\"][0][\"type\"] == \"openrouter:web_search\""` | — |
| [SRC-F725E90B2A-L001050](../../tests/test_web_agent.py#L1050) | 1050 | `"    assert seen[\"payload\"][\"tools\"][0][\"parameters\"][\"max_uses\"] == 3"` | — |
| [SRC-F725E90B2A-L001051](../../tests/test_web_agent.py#L1051) | 1051 | `"    assert seen[\"payload\"][\"max_tool_calls\"] == 5"` | — |
| [SRC-F725E90B2A-L001052](../../tests/test_web_agent.py#L1052) | 1052 | `"    assert agent.server_search_sources[0][\"url\"] == \"https://example.org/current-report\""` | — |
| [SRC-F725E90B2A-L001053](../../tests/test_web_agent.py#L1053) | 1053 | `"    assert agent.server_search_sources[0][\"provider\"] == \"openrouter_web_search\""` | — |
| [SRC-F725E90B2A-L001054](../../tests/test_web_agent.py#L1054) | 1054 | `"    assert \"test-key\" not in str(agent.server_search_sources)"` | — |
| [SRC-F725E90B2A-L001055](../../tests/test_web_agent.py#L1055) | 1055 | `""` | — |
| [SRC-F725E90B2A-L001056](../../tests/test_web_agent.py#L1056) | 1056 | `""` | — |
| [SRC-F725E90B2A-L001057](../../tests/test_web_agent.py#L1057) | 1057 | `"def test_openrouter_live_web_search_remains_disabled_without_explicit_opt_in(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001058](../../tests/test_web_agent.py#L1058) | 1058 | `"    monkeypatch.delenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", raising=False)"` | — |
| [SRC-F725E90B2A-L001059](../../tests/test_web_agent.py#L1059) | 1059 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001060](../../tests/test_web_agent.py#L1060) | 1060 | `"    assert agent.openrouter_web_search_enabled is False"` | — |
| [SRC-F725E90B2A-L001061](../../tests/test_web_agent.py#L1061) | 1061 | `""` | — |
| [SRC-F725E90B2A-L001062](../../tests/test_web_agent.py#L1062) | 1062 | `""` | — |
| [SRC-F725E90B2A-L001063](../../tests/test_web_agent.py#L1063) | 1063 | `""` | — |
| [SRC-F725E90B2A-L001064](../../tests/test_web_agent.py#L1064) | 1064 | `"def test_arabic_query_normalization_removes_diacritics_and_unifies_hamza():"` | — |
| [SRC-F725E90B2A-L001065](../../tests/test_web_agent.py#L1065) | 1065 | `"    normalized = _normalize_search_query(\"إِنَّ أَسْعَارَ أُسْتُرَالِيَا\")"` | — |
| [SRC-F725E90B2A-L001066](../../tests/test_web_agent.py#L1066) | 1066 | `"    assert \"إ\" not in normalized"` | — |
| [SRC-F725E90B2A-L001067](../../tests/test_web_agent.py#L1067) | 1067 | `"    assert \"أ\" not in normalized"` | — |
| [SRC-F725E90B2A-L001068](../../tests/test_web_agent.py#L1068) | 1068 | `"    assert \"ا\" in normalized"` | — |
| [SRC-F725E90B2A-L001069](../../tests/test_web_agent.py#L1069) | 1069 | `"    assert normalized == \"ان اسعار استراليا\""` | — |
| [SRC-F725E90B2A-L001070](../../tests/test_web_agent.py#L1070) | 1070 | `""` | — |
| [SRC-F725E90B2A-L001071](../../tests/test_web_agent.py#L1071) | 1071 | `""` | — |
| [SRC-F725E90B2A-L001072](../../tests/test_web_agent.py#L1072) | 1072 | `"def test_relevance_filter_rejects_translation_and_sports_noise():"` | — |
| [SRC-F725E90B2A-L001073](../../tests/test_web_agent.py#L1073) | 1073 | `"    query = \"قارن Railway و Render لاستضافة Python\""` | — |
| [SRC-F725E90B2A-L001074](../../tests/test_web_agent.py#L1074) | 1074 | `"    assert _relevance_ratio(query, \"Google Translate: error in translation\") < 0.20"` | — |
| [SRC-F725E90B2A-L001075](../../tests/test_web_agent.py#L1075) | 1075 | `"    assert _relevance_ratio("` | — |
| [SRC-F725E90B2A-L001076](../../tests/test_web_agent.py#L1076) | 1076 | `"        \"أول شركة ناشئة في صعيد مصر عام 2019\","` | — |
| [SRC-F725E90B2A-L001077](../../tests/test_web_agent.py#L1077) | 1077 | `"        \"نتائج مباراة كرة القدم وأهداف الدوري المصري اليوم\","` | — |
| [SRC-F725E90B2A-L001078](../../tests/test_web_agent.py#L1078) | 1078 | `"    ) < 0.20"` | — |
| [SRC-F725E90B2A-L001079](../../tests/test_web_agent.py#L1079) | 1079 | `"    assert _relevance_ratio("` | — |
| [SRC-F725E90B2A-L001080](../../tests/test_web_agent.py#L1080) | 1080 | `"        query, \"Railway vs Render for Python app hosting comparison\""` | — |
| [SRC-F725E90B2A-L001081](../../tests/test_web_agent.py#L1081) | 1081 | `"    ) >= 0.20"` | — |
| [SRC-F725E90B2A-L001082](../../tests/test_web_agent.py#L1082) | 1082 | `""` | — |
| [SRC-F725E90B2A-L001083](../../tests/test_web_agent.py#L1083) | 1083 | `""` | — |
| [SRC-F725E90B2A-L001084](../../tests/test_web_agent.py#L1084) | 1084 | `"def test_search_provider_failure_isolated_and_logged(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001085](../../tests/test_web_agent.py#L1085) | 1085 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001086](../../tests/test_web_agent.py#L1086) | 1086 | `""` | — |
| [SRC-F725E90B2A-L001087](../../tests/test_web_agent.py#L1087) | 1087 | `"    def broken(_query):"` | — |
| [SRC-F725E90B2A-L001088](../../tests/test_web_agent.py#L1088) | 1088 | `"        raise RuntimeError(\"upstream HTTP 503\")"` | — |
| [SRC-F725E90B2A-L001089](../../tests/test_web_agent.py#L1089) | 1089 | `""` | — |
| [SRC-F725E90B2A-L001090](../../tests/test_web_agent.py#L1090) | 1090 | `"    def working(_query):"` | — |
| [SRC-F725E90B2A-L001091](../../tests/test_web_agent.py#L1091) | 1091 | `"        return [{"` | — |
| [SRC-F725E90B2A-L001092](../../tests/test_web_agent.py#L1092) | 1092 | `"            \"title\": \"Railway and Render Python hosting\","` | — |
| [SRC-F725E90B2A-L001093](../../tests/test_web_agent.py#L1093) | 1093 | `"            \"url\": \"https://example.net/hosting\","` | — |
| [SRC-F725E90B2A-L001094](../../tests/test_web_agent.py#L1094) | 1094 | `"            \"snippet\": \"Comparison of Railway and Render for Python hosting\","` | — |
| [SRC-F725E90B2A-L001095](../../tests/test_web_agent.py#L1095) | 1095 | `"            \"provider\": \"bing_rss\","` | — |
| [SRC-F725E90B2A-L001096](../../tests/test_web_agent.py#L1096) | 1096 | `"            \"provider_rank\": 1,"` | — |
| [SRC-F725E90B2A-L001097](../../tests/test_web_agent.py#L1097) | 1097 | `"        }]"` | — |
| [SRC-F725E90B2A-L001098](../../tests/test_web_agent.py#L1098) | 1098 | `""` | — |
| [SRC-F725E90B2A-L001099](../../tests/test_web_agent.py#L1099) | 1099 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", broken)"` | — |
| [SRC-F725E90B2A-L001100](../../tests/test_web_agent.py#L1100) | 1100 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", working)"` | — |
| [SRC-F725E90B2A-L001101](../../tests/test_web_agent.py#L1101) | 1101 | `"    results = agent._search_web(\"قارن Railway و Render لاستضافة Python\")"` | — |
| [SRC-F725E90B2A-L001102](../../tests/test_web_agent.py#L1102) | 1102 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L001103](../../tests/test_web_agent.py#L1103) | 1103 | `"    diagnostics = agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L001104](../../tests/test_web_agent.py#L1104) | 1104 | `"    assert any("` | — |
| [SRC-F725E90B2A-L001105](../../tests/test_web_agent.py#L1105) | 1105 | `"        row[\"provider\"] == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L001106](../../tests/test_web_agent.py#L1106) | 1106 | `"        and row[\"status\"] == \"http_error\""` | — |
| [SRC-F725E90B2A-L001107](../../tests/test_web_agent.py#L1107) | 1107 | `"        and \"HTTP 503\" in row.get(\"error\", \"\")"` | — |
| [SRC-F725E90B2A-L001108](../../tests/test_web_agent.py#L1108) | 1108 | `"        for row in diagnostics"` | — |
| [SRC-F725E90B2A-L001109](../../tests/test_web_agent.py#L1109) | 1109 | `"    )"` | — |
| [SRC-F725E90B2A-L001110](../../tests/test_web_agent.py#L1110) | 1110 | `"    assert any("` | — |
| [SRC-F725E90B2A-L001111](../../tests/test_web_agent.py#L1111) | 1111 | `"        row[\"provider\"] == \"bing_rss\" and row[\"status\"] == \"ok\""` | — |
| [SRC-F725E90B2A-L001112](../../tests/test_web_agent.py#L1112) | 1112 | `"        for row in diagnostics"` | — |
| [SRC-F725E90B2A-L001113](../../tests/test_web_agent.py#L1113) | 1113 | `"    )"` | — |
| [SRC-F725E90B2A-L001114](../../tests/test_web_agent.py#L1114) | 1114 | `""` | — |
| [SRC-F725E90B2A-L001115](../../tests/test_web_agent.py#L1115) | 1115 | `""` | — |
| [SRC-F725E90B2A-L001116](../../tests/test_web_agent.py#L1116) | 1116 | `"def test_single_user_supplied_page_can_be_summarized_without_claiming_corroboration(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001117](../../tests/test_web_agent.py#L1117) | 1117 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001118](../../tests/test_web_agent.py#L1118) | 1118 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L001119](../../tests/test_web_agent.py#L1119) | 1119 | `"    source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L001120](../../tests/test_web_agent.py#L1120) | 1120 | `"    source[\"providers\"] = [\"user_supplied_url\"]"` | — |
| [SRC-F725E90B2A-L001121](../../tests/test_web_agent.py#L1121) | 1121 | `"    source[\"page_fetched\"] = True"` | — |
| [SRC-F725E90B2A-L001122](../../tests/test_web_agent.py#L1122) | 1122 | `"    source[\"page_text\"] = \"النص الكامل المستخرج من الصفحة التي قدمها المستخدم.\""` | — |
| [SRC-F725E90B2A-L001123](../../tests/test_web_agent.py#L1123) | 1123 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001124](../../tests/test_web_agent.py#L1124) | 1124 | `"        \"queries\": [\"لخص الصفحة\"],"` | — |
| [SRC-F725E90B2A-L001125](../../tests/test_web_agent.py#L1125) | 1125 | `"        \"direct_urls\": [\"https://example.com/research\"],"` | — |
| [SRC-F725E90B2A-L001126](../../tests/test_web_agent.py#L1126) | 1126 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001127](../../tests/test_web_agent.py#L1127) | 1127 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L001128](../../tests/test_web_agent.py#L1128) | 1128 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001129](../../tests/test_web_agent.py#L1129) | 1129 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001130](../../tests/test_web_agent.py#L1130) | 1130 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001131](../../tests/test_web_agent.py#L1131) | 1131 | `"    }"` | — |
| [SRC-F725E90B2A-L001132](../../tests/test_web_agent.py#L1132) | 1132 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001133](../../tests/test_web_agent.py#L1133) | 1133 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001134](../../tests/test_web_agent.py#L1134) | 1134 | `"        agent,"` | — |
| [SRC-F725E90B2A-L001135](../../tests/test_web_agent.py#L1135) | 1135 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L001136](../../tests/test_web_agent.py#L1136) | 1136 | `"        lambda research_plan: ("` | — |
| [SRC-F725E90B2A-L001137](../../tests/test_web_agent.py#L1137) | 1137 | `"            [source], [], {"` | — |
| [SRC-F725E90B2A-L001138](../../tests/test_web_agent.py#L1138) | 1138 | `"                \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L001139](../../tests/test_web_agent.py#L1139) | 1139 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001140](../../tests/test_web_agent.py#L1140) | 1140 | `"                \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L001141](../../tests/test_web_agent.py#L1141) | 1141 | `"                \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L001142](../../tests/test_web_agent.py#L1142) | 1142 | `"                \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L001143](../../tests/test_web_agent.py#L1143) | 1143 | `"                \"providers_used\": [\"user_supplied_url\"],"` | — |
| [SRC-F725E90B2A-L001144](../../tests/test_web_agent.py#L1144) | 1144 | `"                \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L001145](../../tests/test_web_agent.py#L1145) | 1145 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001146](../../tests/test_web_agent.py#L1146) | 1146 | `"                \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001147](../../tests/test_web_agent.py#L1147) | 1147 | `"                \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001148](../../tests/test_web_agent.py#L1148) | 1148 | `"            },"` | — |
| [SRC-F725E90B2A-L001149](../../tests/test_web_agent.py#L1149) | 1149 | `"        ),"` | — |
| [SRC-F725E90B2A-L001150](../../tests/test_web_agent.py#L1150) | 1150 | `"    )"` | — |
| [SRC-F725E90B2A-L001151](../../tests/test_web_agent.py#L1151) | 1151 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"ملخص محتوى الصفحة [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L001152](../../tests/test_web_agent.py#L1152) | 1152 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L001153](../../tests/test_web_agent.py#L1153) | 1153 | `""` | — |
| [SRC-F725E90B2A-L001154](../../tests/test_web_agent.py#L1154) | 1154 | `"    result = agent.answer(\"لخص الصفحة https://example.com/research\")"` | — |
| [SRC-F725E90B2A-L001155](../../tests/test_web_agent.py#L1155) | 1155 | `""` | — |
| [SRC-F725E90B2A-L001156](../../tests/test_web_agent.py#L1156) | 1156 | `"    assert result[\"kind\"] != \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L001157](../../tests/test_web_agent.py#L1157) | 1157 | `"    assert result[\"answer\"] == \"ملخص محتوى الصفحة [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L001158](../../tests/test_web_agent.py#L1158) | 1158 | `"    assert result[\"search_report\"][\"independent_sources\"] == 1"` | — |
| [SRC-F725E90B2A-L001159](../../tests/test_web_agent.py#L1159) | 1159 | `"    assert result[\"research_quality\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L001160](../../tests/test_web_agent.py#L1160) | 1160 | `"    assert any(\"لم يتم تأكيد محتواه\" in warning for warning in result[\"warnings\"])"` | — |
| [SRC-F725E90B2A-L001161](../../tests/test_web_agent.py#L1161) | 1161 | `""` | — |
| [SRC-F725E90B2A-L001162](../../tests/test_web_agent.py#L1162) | 1162 | `""` | — |
| [SRC-F725E90B2A-L001163](../../tests/test_web_agent.py#L1163) | 1163 | `""` | — |
| [SRC-F725E90B2A-L001164](../../tests/test_web_agent.py#L1164) | 1164 | `"def test_answer_hides_unwrapped_internal_review_report(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001165](../../tests/test_web_agent.py#L1165) | 1165 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001166](../../tests/test_web_agent.py#L1166) | 1166 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L001167](../../tests/test_web_agent.py#L1167) | 1167 | `"    sources = [sample_source(0), sample_source(1)]"` | — |
| [SRC-F725E90B2A-L001168](../../tests/test_web_agent.py#L1168) | 1168 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001169](../../tests/test_web_agent.py#L1169) | 1169 | `"        \"queries\": [\"قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية\"],"` | — |
| [SRC-F725E90B2A-L001170](../../tests/test_web_agent.py#L1170) | 1170 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L001171](../../tests/test_web_agent.py#L1171) | 1171 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001172](../../tests/test_web_agent.py#L1172) | 1172 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L001173](../../tests/test_web_agent.py#L1173) | 1173 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L001174](../../tests/test_web_agent.py#L1174) | 1174 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001175](../../tests/test_web_agent.py#L1175) | 1175 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001176](../../tests/test_web_agent.py#L1176) | 1176 | `"    }"` | — |
| [SRC-F725E90B2A-L001177](../../tests/test_web_agent.py#L1177) | 1177 | `""` | — |
| [SRC-F725E90B2A-L001178](../../tests/test_web_agent.py#L1178) | 1178 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L001179](../../tests/test_web_agent.py#L1179) | 1179 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L001180](../../tests/test_web_agent.py#L1180) | 1180 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L001181](../../tests/test_web_agent.py#L1181) | 1181 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L001182](../../tests/test_web_agent.py#L1182) | 1182 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L001183](../../tests/test_web_agent.py#L1183) | 1183 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-F725E90B2A-L001184](../../tests/test_web_agent.py#L1184) | 1184 | `"            \"pages_fetched\": len(sources),"` | — |
| [SRC-F725E90B2A-L001185](../../tests/test_web_agent.py#L1185) | 1185 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001186](../../tests/test_web_agent.py#L1186) | 1186 | `"            \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-F725E90B2A-L001187](../../tests/test_web_agent.py#L1187) | 1187 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001188](../../tests/test_web_agent.py#L1188) | 1188 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L001189](../../tests/test_web_agent.py#L1189) | 1189 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001190](../../tests/test_web_agent.py#L1190) | 1190 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L001191](../../tests/test_web_agent.py#L1191) | 1191 | `"        }"` | — |
| [SRC-F725E90B2A-L001192](../../tests/test_web_agent.py#L1192) | 1192 | `""` | — |
| [SRC-F725E90B2A-L001193](../../tests/test_web_agent.py#L1193) | 1193 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001194](../../tests/test_web_agent.py#L1194) | 1194 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L001195](../../tests/test_web_agent.py#L1195) | 1195 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L001196](../../tests/test_web_agent.py#L1196) | 1196 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001197](../../tests/test_web_agent.py#L1197) | 1197 | `"        agent, \"_generate\", lambda *args, **kwargs: \"إجابة مبدئية [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L001198](../../tests/test_web_agent.py#L1198) | 1198 | `"    )"` | — |
| [SRC-F725E90B2A-L001199](../../tests/test_web_agent.py#L1199) | 1199 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001200](../../tests/test_web_agent.py#L1200) | 1200 | `"        agent,"` | — |
| [SRC-F725E90B2A-L001201](../../tests/test_web_agent.py#L1201) | 1201 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L001202](../../tests/test_web_agent.py#L1202) | 1202 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-F725E90B2A-L001203](../../tests/test_web_agent.py#L1203) | 1203 | `"            \"Audit Report: ملاحظة داخلية سرية\\\\n\""` | — |
| [SRC-F725E90B2A-L001204](../../tests/test_web_agent.py#L1204) | 1204 | `"            \"Final answer: إجابة نهائية مزعومة\""` | — |
| [SRC-F725E90B2A-L001205](../../tests/test_web_agent.py#L1205) | 1205 | `"        ),"` | — |
| [SRC-F725E90B2A-L001206](../../tests/test_web_agent.py#L1206) | 1206 | `"    )"` | — |
| [SRC-F725E90B2A-L001207](../../tests/test_web_agent.py#L1207) | 1207 | `""` | — |
| [SRC-F725E90B2A-L001208](../../tests/test_web_agent.py#L1208) | 1208 | `"    result = agent.answer(\"قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية\")"` | — |
| [SRC-F725E90B2A-L001209](../../tests/test_web_agent.py#L1209) | 1209 | `""` | — |
| [SRC-F725E90B2A-L001210](../../tests/test_web_agent.py#L1210) | 1210 | `"    assert result[\"search_report\"][\"second_pass_review\"] == \"model_claim_audit_unavailable\""` | — |
| [SRC-F725E90B2A-L001211](../../tests/test_web_agent.py#L1211) | 1211 | `"    assert result[\"final_answer_status\"] == \"review_failed_with_source_fallback\""` | — |
| [SRC-F725E90B2A-L001212](../../tests/test_web_agent.py#L1212) | 1212 | `"    assert \"Audit Report\" not in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L001213](../../tests/test_web_agent.py#L1213) | 1213 | `"    assert \"ملاحظة داخلية سرية\" not in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L001214](../../tests/test_web_agent.py#L1214) | 1214 | `"    assert \"إجابة نهائية مزعومة\" not in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L001215](../../tests/test_web_agent.py#L1215) | 1215 | `""` | — |
| [SRC-F725E90B2A-L001216](../../tests/test_web_agent.py#L1216) | 1216 | `""` | — |
| [SRC-F725E90B2A-L001217](../../tests/test_web_agent.py#L1217) | 1217 | `"def test_sibling_subdomains_do_not_satisfy_independent_evidence_gate(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001218](../../tests/test_web_agent.py#L1218) | 1218 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001219](../../tests/test_web_agent.py#L1219) | 1219 | `"    first = sample_source(0)"` | — |
| [SRC-F725E90B2A-L001220](../../tests/test_web_agent.py#L1220) | 1220 | `"    first[\"url\"] = \"https://news.example.com/research\""` | — |
| [SRC-F725E90B2A-L001221](../../tests/test_web_agent.py#L1221) | 1221 | `"    first[\"domain\"] = \"news.example.com\""` | — |
| [SRC-F725E90B2A-L001222](../../tests/test_web_agent.py#L1222) | 1222 | `"    second = sample_source(1)"` | — |
| [SRC-F725E90B2A-L001223](../../tests/test_web_agent.py#L1223) | 1223 | `"    second[\"url\"] = \"https://offers.example.com/research\""` | — |
