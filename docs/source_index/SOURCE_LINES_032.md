# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **032**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L000484 إلى SRC-F725E90B2A-L001283
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L000484](../../tests/test_web_agent.py#L484) | 484 | `""` | — |
| [SRC-F725E90B2A-L000485](../../tests/test_web_agent.py#L485) | 485 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000486](../../tests/test_web_agent.py#L486) | 486 | `"        calls.append((url, kwargs))"` | — |
| [SRC-F725E90B2A-L000487](../../tests/test_web_agent.py#L487) | 487 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L000488](../../tests/test_web_agent.py#L488) | 488 | `""` | — |
| [SRC-F725E90B2A-L000489](../../tests/test_web_agent.py#L489) | 489 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000490](../../tests/test_web_agent.py#L490) | 490 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000491](../../tests/test_web_agent.py#L491) | 491 | `"        \"سيارة كهربائية\", [\"x\"]"` | — |
| [SRC-F725E90B2A-L000492](../../tests/test_web_agent.py#L492) | 492 | `"    )"` | — |
| [SRC-F725E90B2A-L000493](../../tests/test_web_agent.py#L493) | 493 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000494](../../tests/test_web_agent.py#L494) | 494 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L000495](../../tests/test_web_agent.py#L495) | 495 | `"    assert results[0][\"provider\"] == \"x_official_api\""` | — |
| [SRC-F725E90B2A-L000496](../../tests/test_web_agent.py#L496) | 496 | `"    assert results[0][\"url\"] == \"https://x.com/driver/status/1840000000000000000\""` | — |
| [SRC-F725E90B2A-L000497](../../tests/test_web_agent.py#L497) | 497 | `"    assert calls[0][1][\"headers\"][\"Authorization\"] == \"Bearer test-token\""` | — |
| [SRC-F725E90B2A-L000498](../../tests/test_web_agent.py#L498) | 498 | `""` | — |
| [SRC-F725E90B2A-L000499](../../tests/test_web_agent.py#L499) | 499 | `""` | — |
| [SRC-F725E90B2A-L000500](../../tests/test_web_agent.py#L500) | 500 | `""` | — |
| [SRC-F725E90B2A-L000501](../../tests/test_web_agent.py#L501) | 501 | `"def test_instagram_graph_api_returns_only_public_hashtag_media(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000502](../../tests/test_web_agent.py#L502) | 502 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000503](../../tests/test_web_agent.py#L503) | 503 | `""` | — |
| [SRC-F725E90B2A-L000504](../../tests/test_web_agent.py#L504) | 504 | `"    monkeypatch.setenv(\"INSTAGRAM_USER_ID\", \"ig-user-123\")"` | — |
| [SRC-F725E90B2A-L000505](../../tests/test_web_agent.py#L505) | 505 | `"    monkeypatch.setenv(\"INSTAGRAM_ACCESS_TOKEN\", \"test-ig-token\")"` | — |
| [SRC-F725E90B2A-L000506](../../tests/test_web_agent.py#L506) | 506 | `"    monkeypatch.setenv(\"META_GRAPH_VERSION\", \"v25.0\")"` | — |
| [SRC-F725E90B2A-L000507](../../tests/test_web_agent.py#L507) | 507 | `""` | — |
| [SRC-F725E90B2A-L000508](../../tests/test_web_agent.py#L508) | 508 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000509](../../tests/test_web_agent.py#L509) | 509 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000510](../../tests/test_web_agent.py#L510) | 510 | `""` | — |
| [SRC-F725E90B2A-L000511](../../tests/test_web_agent.py#L511) | 511 | `"        def __init__(self, payload):"` | — |
| [SRC-F725E90B2A-L000512](../../tests/test_web_agent.py#L512) | 512 | `"            self.payload = payload"` | — |
| [SRC-F725E90B2A-L000513](../../tests/test_web_agent.py#L513) | 513 | `""` | — |
| [SRC-F725E90B2A-L000514](../../tests/test_web_agent.py#L514) | 514 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000515](../../tests/test_web_agent.py#L515) | 515 | `"            return self.payload"` | — |
| [SRC-F725E90B2A-L000516](../../tests/test_web_agent.py#L516) | 516 | `""` | — |
| [SRC-F725E90B2A-L000517](../../tests/test_web_agent.py#L517) | 517 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000518](../../tests/test_web_agent.py#L518) | 518 | `""` | — |
| [SRC-F725E90B2A-L000519](../../tests/test_web_agent.py#L519) | 519 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000520](../../tests/test_web_agent.py#L520) | 520 | `"        calls.append((url, kwargs))"` | — |
| [SRC-F725E90B2A-L000521](../../tests/test_web_agent.py#L521) | 521 | `"        if url.endswith(\"/ig_hashtag_search\"):"` | — |
| [SRC-F725E90B2A-L000522](../../tests/test_web_agent.py#L522) | 522 | `"            return FakeResponse({\"data\": [{\"id\": \"tag-7\", \"name\": \"cars\"}]})"` | — |
| [SRC-F725E90B2A-L000523](../../tests/test_web_agent.py#L523) | 523 | `"        if url.endswith(\"/tag-7/recent_media\"):"` | — |
| [SRC-F725E90B2A-L000524](../../tests/test_web_agent.py#L524) | 524 | `"            return FakeResponse({\"data\": [{"` | — |
| [SRC-F725E90B2A-L000525](../../tests/test_web_agent.py#L525) | 525 | `"                \"permalink\": \"https://www.instagram.com/p/ABC123/\","` | — |
| [SRC-F725E90B2A-L000526](../../tests/test_web_agent.py#L526) | 526 | `"                \"caption\": \"Owner shared an electric car review\","` | — |
| [SRC-F725E90B2A-L000527](../../tests/test_web_agent.py#L527) | 527 | `"                \"media_type\": \"IMAGE\","` | — |
| [SRC-F725E90B2A-L000528](../../tests/test_web_agent.py#L528) | 528 | `"                \"timestamp\": \"2026-10-12T10:00:00+0000\","` | — |
| [SRC-F725E90B2A-L000529](../../tests/test_web_agent.py#L529) | 529 | `"                \"like_count\": 17,"` | — |
| [SRC-F725E90B2A-L000530](../../tests/test_web_agent.py#L530) | 530 | `"                \"comments_count\": 4,"` | — |
| [SRC-F725E90B2A-L000531](../../tests/test_web_agent.py#L531) | 531 | `"            }]})"` | — |
| [SRC-F725E90B2A-L000532](../../tests/test_web_agent.py#L532) | 532 | `"        raise AssertionError(f\"Unexpected URL {url}\")"` | — |
| [SRC-F725E90B2A-L000533](../../tests/test_web_agent.py#L533) | 533 | `""` | — |
| [SRC-F725E90B2A-L000534](../../tests/test_web_agent.py#L534) | 534 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000535](../../tests/test_web_agent.py#L535) | 535 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000536](../../tests/test_web_agent.py#L536) | 536 | `"        \"Instagram #cars\", [\"instagram\"]"` | — |
| [SRC-F725E90B2A-L000537](../../tests/test_web_agent.py#L537) | 537 | `"    )"` | — |
| [SRC-F725E90B2A-L000538](../../tests/test_web_agent.py#L538) | 538 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000539](../../tests/test_web_agent.py#L539) | 539 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L000540](../../tests/test_web_agent.py#L540) | 540 | `"    assert results[0][\"provider\"] == \"instagram_graph_api\""` | — |
| [SRC-F725E90B2A-L000541](../../tests/test_web_agent.py#L541) | 541 | `"    assert results[0][\"url\"] == \"https://www.instagram.com/p/ABC123/\""` | — |
| [SRC-F725E90B2A-L000542](../../tests/test_web_agent.py#L542) | 542 | `"    assert \"likes=17\" in results[0][\"snippet\"]"` | — |
| [SRC-F725E90B2A-L000543](../../tests/test_web_agent.py#L543) | 543 | `"    assert calls[0][1][\"params\"][\"q\"] == \"cars\""` | — |
| [SRC-F725E90B2A-L000544](../../tests/test_web_agent.py#L544) | 544 | `"    assert calls[0][1][\"params\"][\"access_token\"] == \"test-ig-token\""` | — |
| [SRC-F725E90B2A-L000545](../../tests/test_web_agent.py#L545) | 545 | `"    assert \"test-ig-token\" not in str(results)"` | — |
| [SRC-F725E90B2A-L000546](../../tests/test_web_agent.py#L546) | 546 | `""` | — |
| [SRC-F725E90B2A-L000547](../../tests/test_web_agent.py#L547) | 547 | `""` | — |
| [SRC-F725E90B2A-L000548](../../tests/test_web_agent.py#L548) | 548 | `"def test_instagram_api_not_configured_uses_honest_fallback_warning(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000549](../../tests/test_web_agent.py#L549) | 549 | `"    monkeypatch.delenv(\"INSTAGRAM_USER_ID\", raising=False)"` | — |
| [SRC-F725E90B2A-L000550](../../tests/test_web_agent.py#L550) | 550 | `"    monkeypatch.delenv(\"INSTAGRAM_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-F725E90B2A-L000551](../../tests/test_web_agent.py#L551) | 551 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000552](../../tests/test_web_agent.py#L552) | 552 | `"        \"تجارب عامة على Instagram\", [\"instagram\"]"` | — |
| [SRC-F725E90B2A-L000553](../../tests/test_web_agent.py#L553) | 553 | `"    )"` | — |
| [SRC-F725E90B2A-L000554](../../tests/test_web_agent.py#L554) | 554 | `"    assert results == []"` | — |
| [SRC-F725E90B2A-L000555](../../tests/test_web_agent.py#L555) | 555 | `"    assert any(\"indexed public Instagram\" in warning for warning in warnings)"` | — |
| [SRC-F725E90B2A-L000556](../../tests/test_web_agent.py#L556) | 556 | `""` | — |
| [SRC-F725E90B2A-L000557](../../tests/test_web_agent.py#L557) | 557 | `""` | — |
| [SRC-F725E90B2A-L000558](../../tests/test_web_agent.py#L558) | 558 | `"def test_facebook_pages_api_reads_only_operator_configured_pages(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000559](../../tests/test_web_agent.py#L559) | 559 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000560](../../tests/test_web_agent.py#L560) | 560 | `""` | — |
| [SRC-F725E90B2A-L000561](../../tests/test_web_agent.py#L561) | 561 | `"    monkeypatch.setenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"test-page-token\")"` | — |
| [SRC-F725E90B2A-L000562](../../tests/test_web_agent.py#L562) | 562 | `"    monkeypatch.setenv(\"FACEBOOK_PAGE_IDS\", \"page-1,page-2\")"` | — |
| [SRC-F725E90B2A-L000563](../../tests/test_web_agent.py#L563) | 563 | `""` | — |
| [SRC-F725E90B2A-L000564](../../tests/test_web_agent.py#L564) | 564 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000565](../../tests/test_web_agent.py#L565) | 565 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000566](../../tests/test_web_agent.py#L566) | 566 | `""` | — |
| [SRC-F725E90B2A-L000567](../../tests/test_web_agent.py#L567) | 567 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000568](../../tests/test_web_agent.py#L568) | 568 | `"            return {\"data\": [{"` | — |
| [SRC-F725E90B2A-L000569](../../tests/test_web_agent.py#L569) | 569 | `"                \"message\": \"Electric car owners looking for charging advice\","` | — |
| [SRC-F725E90B2A-L000570](../../tests/test_web_agent.py#L570) | 570 | `"                \"permalink_url\": \"https://www.facebook.com/example/posts/123\","` | — |
| [SRC-F725E90B2A-L000571](../../tests/test_web_agent.py#L571) | 571 | `"                \"created_time\": \"2026-10-12T12:00:00+0000\","` | — |
| [SRC-F725E90B2A-L000572](../../tests/test_web_agent.py#L572) | 572 | `"                \"comments\": {\"data\": ["` | — |
| [SRC-F725E90B2A-L000573](../../tests/test_web_agent.py#L573) | 573 | `"                    {\"message\": \"What is the current price?\", \"like_count\": 3}"` | — |
| [SRC-F725E90B2A-L000574](../../tests/test_web_agent.py#L574) | 574 | `"                ]},"` | — |
| [SRC-F725E90B2A-L000575](../../tests/test_web_agent.py#L575) | 575 | `"            }]}"` | — |
| [SRC-F725E90B2A-L000576](../../tests/test_web_agent.py#L576) | 576 | `""` | — |
| [SRC-F725E90B2A-L000577](../../tests/test_web_agent.py#L577) | 577 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000578](../../tests/test_web_agent.py#L578) | 578 | `""` | — |
| [SRC-F725E90B2A-L000579](../../tests/test_web_agent.py#L579) | 579 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000580](../../tests/test_web_agent.py#L580) | 580 | `"        calls.append((url, kwargs))"` | — |
| [SRC-F725E90B2A-L000581](../../tests/test_web_agent.py#L581) | 581 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L000582](../../tests/test_web_agent.py#L582) | 582 | `""` | — |
| [SRC-F725E90B2A-L000583](../../tests/test_web_agent.py#L583) | 583 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000584](../../tests/test_web_agent.py#L584) | 584 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000585](../../tests/test_web_agent.py#L585) | 585 | `"        \"electric car\", [\"facebook\"]"` | — |
| [SRC-F725E90B2A-L000586](../../tests/test_web_agent.py#L586) | 586 | `"    )"` | — |
| [SRC-F725E90B2A-L000587](../../tests/test_web_agent.py#L587) | 587 | `"    assert len(results) == 2  # one matching post for each explicitly configured page"` | — |
| [SRC-F725E90B2A-L000588](../../tests/test_web_agent.py#L588) | 588 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000589](../../tests/test_web_agent.py#L589) | 589 | `"    assert all(item[\"provider\"] == \"facebook_pages_api\" for item in results)"` | — |
| [SRC-F725E90B2A-L000590](../../tests/test_web_agent.py#L590) | 590 | `"    assert all(\"Electric car owners\" in item[\"snippet\"] for item in results)"` | — |
| [SRC-F725E90B2A-L000591](../../tests/test_web_agent.py#L591) | 591 | `"    assert len(calls) == 2"` | — |
| [SRC-F725E90B2A-L000592](../../tests/test_web_agent.py#L592) | 592 | `"    assert all(\"Bearer test-page-token\" == call[1][\"headers\"][\"Authorization\"] for call in calls)"` | — |
| [SRC-F725E90B2A-L000593](../../tests/test_web_agent.py#L593) | 593 | `""` | — |
| [SRC-F725E90B2A-L000594](../../tests/test_web_agent.py#L594) | 594 | `""` | — |
| [SRC-F725E90B2A-L000595](../../tests/test_web_agent.py#L595) | 595 | `"def test_reddit_oauth_api_is_preferred_when_credentials_are_configured(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000596](../../tests/test_web_agent.py#L596) | 596 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000597](../../tests/test_web_agent.py#L597) | 597 | `""` | — |
| [SRC-F725E90B2A-L000598](../../tests/test_web_agent.py#L598) | 598 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_ID\", \"client-test\")"` | — |
| [SRC-F725E90B2A-L000599](../../tests/test_web_agent.py#L599) | 599 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_SECRET\", \"secret-test\")"` | — |
| [SRC-F725E90B2A-L000600](../../tests/test_web_agent.py#L600) | 600 | `"    monkeypatch.setenv(\"REDDIT_USER_AGENT\", \"test:omarai:0.1\")"` | — |
| [SRC-F725E90B2A-L000601](../../tests/test_web_agent.py#L601) | 601 | `""` | — |
| [SRC-F725E90B2A-L000602](../../tests/test_web_agent.py#L602) | 602 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000603](../../tests/test_web_agent.py#L603) | 603 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000604](../../tests/test_web_agent.py#L604) | 604 | `""` | — |
| [SRC-F725E90B2A-L000605](../../tests/test_web_agent.py#L605) | 605 | `"        def __init__(self, payload):"` | — |
| [SRC-F725E90B2A-L000606](../../tests/test_web_agent.py#L606) | 606 | `"            self.payload = payload"` | — |
| [SRC-F725E90B2A-L000607](../../tests/test_web_agent.py#L607) | 607 | `""` | — |
| [SRC-F725E90B2A-L000608](../../tests/test_web_agent.py#L608) | 608 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000609](../../tests/test_web_agent.py#L609) | 609 | `"            return self.payload"` | — |
| [SRC-F725E90B2A-L000610](../../tests/test_web_agent.py#L610) | 610 | `""` | — |
| [SRC-F725E90B2A-L000611](../../tests/test_web_agent.py#L611) | 611 | `"        @property"` | — |
| [SRC-F725E90B2A-L000612](../../tests/test_web_agent.py#L612) | 612 | `"        def content(self):"` | — |
| [SRC-F725E90B2A-L000613](../../tests/test_web_agent.py#L613) | 613 | `"            import json"` | — |
| [SRC-F725E90B2A-L000614](../../tests/test_web_agent.py#L614) | 614 | `"            return json.dumps(self.payload).encode()"` | — |
| [SRC-F725E90B2A-L000615](../../tests/test_web_agent.py#L615) | 615 | `""` | — |
| [SRC-F725E90B2A-L000616](../../tests/test_web_agent.py#L616) | 616 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000617](../../tests/test_web_agent.py#L617) | 617 | `""` | — |
| [SRC-F725E90B2A-L000618](../../tests/test_web_agent.py#L618) | 618 | `"    def fake_post(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000619](../../tests/test_web_agent.py#L619) | 619 | `"        calls.append((\"POST\", url, kwargs))"` | — |
| [SRC-F725E90B2A-L000620](../../tests/test_web_agent.py#L620) | 620 | `"        return FakeResponse({\"access_token\": \"test-reddit-access-token\"})"` | — |
| [SRC-F725E90B2A-L000621](../../tests/test_web_agent.py#L621) | 621 | `""` | — |
| [SRC-F725E90B2A-L000622](../../tests/test_web_agent.py#L622) | 622 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000623](../../tests/test_web_agent.py#L623) | 623 | `"        calls.append((\"GET\", url, kwargs))"` | — |
| [SRC-F725E90B2A-L000624](../../tests/test_web_agent.py#L624) | 624 | `"        return FakeResponse({\"data\": {\"children\": [{"` | — |
| [SRC-F725E90B2A-L000625](../../tests/test_web_agent.py#L625) | 625 | `"            \"data\": {"` | — |
| [SRC-F725E90B2A-L000626](../../tests/test_web_agent.py#L626) | 626 | `"                \"title\": \"Electric vehicle owner discussion\","` | — |
| [SRC-F725E90B2A-L000627](../../tests/test_web_agent.py#L627) | 627 | `"                \"permalink\": \"/r/cars/comments/example/post/\","` | — |
| [SRC-F725E90B2A-L000628](../../tests/test_web_agent.py#L628) | 628 | `"                \"selftext\": \"Owners discuss battery range.\","` | — |
| [SRC-F725E90B2A-L000629](../../tests/test_web_agent.py#L629) | 629 | `"                \"created_utc\": 1791800000,"` | — |
| [SRC-F725E90B2A-L000630](../../tests/test_web_agent.py#L630) | 630 | `"                \"score\": 25,"` | — |
| [SRC-F725E90B2A-L000631](../../tests/test_web_agent.py#L631) | 631 | `"                \"num_comments\": 8,"` | — |
| [SRC-F725E90B2A-L000632](../../tests/test_web_agent.py#L632) | 632 | `"            }"` | — |
| [SRC-F725E90B2A-L000633](../../tests/test_web_agent.py#L633) | 633 | `"        }]}})"` | — |
| [SRC-F725E90B2A-L000634](../../tests/test_web_agent.py#L634) | 634 | `""` | — |
| [SRC-F725E90B2A-L000635](../../tests/test_web_agent.py#L635) | 635 | `"    monkeypatch.setattr(httpx, \"post\", fake_post)"` | — |
| [SRC-F725E90B2A-L000636](../../tests/test_web_agent.py#L636) | 636 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000637](../../tests/test_web_agent.py#L637) | 637 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000638](../../tests/test_web_agent.py#L638) | 638 | `"        \"electric vehicles\", [\"reddit\"]"` | — |
| [SRC-F725E90B2A-L000639](../../tests/test_web_agent.py#L639) | 639 | `"    )"` | — |
| [SRC-F725E90B2A-L000640](../../tests/test_web_agent.py#L640) | 640 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L000641](../../tests/test_web_agent.py#L641) | 641 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000642](../../tests/test_web_agent.py#L642) | 642 | `"    assert results[0][\"provider\"] == \"reddit_oauth_api\""` | — |
| [SRC-F725E90B2A-L000643](../../tests/test_web_agent.py#L643) | 643 | `"    assert results[0][\"url\"] == \"https://www.reddit.com/r/cars/comments/example/post/\""` | — |
| [SRC-F725E90B2A-L000644](../../tests/test_web_agent.py#L644) | 644 | `"    assert \"score=25\" in results[0][\"snippet\"]"` | — |
| [SRC-F725E90B2A-L000645](../../tests/test_web_agent.py#L645) | 645 | `"    assert len([call for call in calls if call[0] == \"POST\"]) == 1"` | — |
| [SRC-F725E90B2A-L000646](../../tests/test_web_agent.py#L646) | 646 | `"    assert any(\"oauth.reddit.com/search\" in call[1] for call in calls if call[0] == \"GET\")"` | — |
| [SRC-F725E90B2A-L000647](../../tests/test_web_agent.py#L647) | 647 | `"    assert \"test-reddit-access-token\" not in str(results)"` | — |
| [SRC-F725E90B2A-L000648](../../tests/test_web_agent.py#L648) | 648 | `""` | — |
| [SRC-F725E90B2A-L000649](../../tests/test_web_agent.py#L649) | 649 | `""` | — |
| [SRC-F725E90B2A-L000650](../../tests/test_web_agent.py#L650) | 650 | `""` | — |
| [SRC-F725E90B2A-L000651](../../tests/test_web_agent.py#L651) | 651 | `"def test_role_models_are_explicit_and_have_a_fallback(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000652](../../tests/test_web_agent.py#L652) | 652 | `"    for name in ("` | — |
| [SRC-F725E90B2A-L000653](../../tests/test_web_agent.py#L653) | 653 | `"        \"OMARAI_LLM_MODEL\","` | — |
| [SRC-F725E90B2A-L000654](../../tests/test_web_agent.py#L654) | 654 | `"        \"OMARAI_PLANNER_MODEL\","` | — |
| [SRC-F725E90B2A-L000655](../../tests/test_web_agent.py#L655) | 655 | `"        \"OMARAI_ANSWER_MODEL\","` | — |
| [SRC-F725E90B2A-L000656](../../tests/test_web_agent.py#L656) | 656 | `"        \"OMARAI_REVIEW_MODEL\","` | — |
| [SRC-F725E90B2A-L000657](../../tests/test_web_agent.py#L657) | 657 | `"        \"OMARAI_LLM_FALLBACK_MODEL\","` | — |
| [SRC-F725E90B2A-L000658](../../tests/test_web_agent.py#L658) | 658 | `"    ):"` | — |
| [SRC-F725E90B2A-L000659](../../tests/test_web_agent.py#L659) | 659 | `"        monkeypatch.delenv(name, raising=False)"` | — |
| [SRC-F725E90B2A-L000660](../../tests/test_web_agent.py#L660) | 660 | `""` | — |
| [SRC-F725E90B2A-L000661](../../tests/test_web_agent.py#L661) | 661 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000662](../../tests/test_web_agent.py#L662) | 662 | `"    assert agent.planner_model == \"nvidia/nemotron-3-ultra-550b-a55b:free\""` | — |
| [SRC-F725E90B2A-L000663](../../tests/test_web_agent.py#L663) | 663 | `"    assert agent.answer_model == \"google/gemma-4-31b-it:free\""` | — |
| [SRC-F725E90B2A-L000664](../../tests/test_web_agent.py#L664) | 664 | `"    assert agent.review_model == agent.answer_model"` | — |
| [SRC-F725E90B2A-L000665](../../tests/test_web_agent.py#L665) | 665 | `"    assert agent.fallback_model == \"openrouter/free\""` | — |
| [SRC-F725E90B2A-L000666](../../tests/test_web_agent.py#L666) | 666 | `""` | — |
| [SRC-F725E90B2A-L000667](../../tests/test_web_agent.py#L667) | 667 | `""` | — |
| [SRC-F725E90B2A-L000668](../../tests/test_web_agent.py#L668) | 668 | `"def test_global_model_override_is_preserved_for_existing_users(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000669](../../tests/test_web_agent.py#L669) | 669 | `"    monkeypatch.setenv(\"OMARAI_LLM_MODEL\", \"example/custom-model\")"` | — |
| [SRC-F725E90B2A-L000670](../../tests/test_web_agent.py#L670) | 670 | `"    monkeypatch.delenv(\"OMARAI_PLANNER_MODEL\", raising=False)"` | — |
| [SRC-F725E90B2A-L000671](../../tests/test_web_agent.py#L671) | 671 | `"    monkeypatch.delenv(\"OMARAI_ANSWER_MODEL\", raising=False)"` | — |
| [SRC-F725E90B2A-L000672](../../tests/test_web_agent.py#L672) | 672 | `"    monkeypatch.delenv(\"OMARAI_REVIEW_MODEL\", raising=False)"` | — |
| [SRC-F725E90B2A-L000673](../../tests/test_web_agent.py#L673) | 673 | `""` | — |
| [SRC-F725E90B2A-L000674](../../tests/test_web_agent.py#L674) | 674 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000675](../../tests/test_web_agent.py#L675) | 675 | `"    assert agent.planner_model == \"example/custom-model\""` | — |
| [SRC-F725E90B2A-L000676](../../tests/test_web_agent.py#L676) | 676 | `"    assert agent.answer_model == \"example/custom-model\""` | — |
| [SRC-F725E90B2A-L000677](../../tests/test_web_agent.py#L677) | 677 | `"    assert agent.review_model == \"example/custom-model\""` | — |
| [SRC-F725E90B2A-L000678](../../tests/test_web_agent.py#L678) | 678 | `""` | — |
| [SRC-F725E90B2A-L000679](../../tests/test_web_agent.py#L679) | 679 | `""` | — |
| [SRC-F725E90B2A-L000680](../../tests/test_web_agent.py#L680) | 680 | `"def test_completion_uses_fallback_model_after_primary_http_error(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000681](../../tests/test_web_agent.py#L681) | 681 | `"    import io"` | — |
| [SRC-F725E90B2A-L000682](../../tests/test_web_agent.py#L682) | 682 | `"    import json"` | — |
| [SRC-F725E90B2A-L000683](../../tests/test_web_agent.py#L683) | 683 | `"    import urllib.error"` | — |
| [SRC-F725E90B2A-L000684](../../tests/test_web_agent.py#L684) | 684 | `""` | — |
| [SRC-F725E90B2A-L000685](../../tests/test_web_agent.py#L685) | 685 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000686](../../tests/test_web_agent.py#L686) | 686 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000687](../../tests/test_web_agent.py#L687) | 687 | `"    agent.fallback_model = \"openrouter/free\""` | — |
| [SRC-F725E90B2A-L000688](../../tests/test_web_agent.py#L688) | 688 | `"    called = []"` | — |
| [SRC-F725E90B2A-L000689](../../tests/test_web_agent.py#L689) | 689 | `""` | — |
| [SRC-F725E90B2A-L000690](../../tests/test_web_agent.py#L690) | 690 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000691](../../tests/test_web_agent.py#L691) | 691 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L000692](../../tests/test_web_agent.py#L692) | 692 | `"            return self"` | — |
| [SRC-F725E90B2A-L000693](../../tests/test_web_agent.py#L693) | 693 | `""` | — |
| [SRC-F725E90B2A-L000694](../../tests/test_web_agent.py#L694) | 694 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L000695](../../tests/test_web_agent.py#L695) | 695 | `"            return False"` | — |
| [SRC-F725E90B2A-L000696](../../tests/test_web_agent.py#L696) | 696 | `""` | — |
| [SRC-F725E90B2A-L000697](../../tests/test_web_agent.py#L697) | 697 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L000698](../../tests/test_web_agent.py#L698) | 698 | `"            return json.dumps({"` | — |
| [SRC-F725E90B2A-L000699](../../tests/test_web_agent.py#L699) | 699 | `"                \"choices\": [{"` | — |
| [SRC-F725E90B2A-L000700](../../tests/test_web_agent.py#L700) | 700 | `"                    \"message\": {\"content\": \"إجابة من النموذج الاحتياطي\"},"` | — |
| [SRC-F725E90B2A-L000701](../../tests/test_web_agent.py#L701) | 701 | `"                    \"finish_reason\": \"stop\","` | — |
| [SRC-F725E90B2A-L000702](../../tests/test_web_agent.py#L702) | 702 | `"                }]"` | — |
| [SRC-F725E90B2A-L000703](../../tests/test_web_agent.py#L703) | 703 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000704](../../tests/test_web_agent.py#L704) | 704 | `""` | — |
| [SRC-F725E90B2A-L000705](../../tests/test_web_agent.py#L705) | 705 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L000706](../../tests/test_web_agent.py#L706) | 706 | `"        payload = json.loads(request.data.decode(\"utf-8\"))"` | — |
| [SRC-F725E90B2A-L000707](../../tests/test_web_agent.py#L707) | 707 | `"        called.append(payload[\"model\"])"` | — |
| [SRC-F725E90B2A-L000708](../../tests/test_web_agent.py#L708) | 708 | `"        if payload[\"model\"] == \"broken/primary\":"` | — |
| [SRC-F725E90B2A-L000709](../../tests/test_web_agent.py#L709) | 709 | `"            raise urllib.error.HTTPError("` | — |
| [SRC-F725E90B2A-L000710](../../tests/test_web_agent.py#L710) | 710 | `"                request.full_url,"` | — |
| [SRC-F725E90B2A-L000711](../../tests/test_web_agent.py#L711) | 711 | `"                503,"` | — |
| [SRC-F725E90B2A-L000712](../../tests/test_web_agent.py#L712) | 712 | `"                \"service unavailable\","` | — |
| [SRC-F725E90B2A-L000713](../../tests/test_web_agent.py#L713) | 713 | `"                hdrs=None,"` | — |
| [SRC-F725E90B2A-L000714](../../tests/test_web_agent.py#L714) | 714 | `"                fp=io.BytesIO(b\"private provider diagnostics\"),"` | — |
| [SRC-F725E90B2A-L000715](../../tests/test_web_agent.py#L715) | 715 | `"            )"` | — |
| [SRC-F725E90B2A-L000716](../../tests/test_web_agent.py#L716) | 716 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L000717](../../tests/test_web_agent.py#L717) | 717 | `""` | — |
| [SRC-F725E90B2A-L000718](../../tests/test_web_agent.py#L718) | 718 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L000719](../../tests/test_web_agent.py#L719) | 719 | `"    result = agent._request_completion("` | — |
| [SRC-F725E90B2A-L000720](../../tests/test_web_agent.py#L720) | 720 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-F725E90B2A-L000721](../../tests/test_web_agent.py#L721) | 721 | `"        model=\"broken/primary\","` | — |
| [SRC-F725E90B2A-L000722](../../tests/test_web_agent.py#L722) | 722 | `"    )"` | — |
| [SRC-F725E90B2A-L000723](../../tests/test_web_agent.py#L723) | 723 | `""` | — |
| [SRC-F725E90B2A-L000724](../../tests/test_web_agent.py#L724) | 724 | `"    assert result == \"إجابة من النموذج الاحتياطي\""` | — |
| [SRC-F725E90B2A-L000725](../../tests/test_web_agent.py#L725) | 725 | `"    assert called == [\"broken/primary\", \"openrouter/free\"]"` | — |
| [SRC-F725E90B2A-L000726](../../tests/test_web_agent.py#L726) | 726 | `"    assert agent.model_usage == [{"` | — |
| [SRC-F725E90B2A-L000727](../../tests/test_web_agent.py#L727) | 727 | `"        \"requested_model\": \"broken/primary\","` | — |
| [SRC-F725E90B2A-L000728](../../tests/test_web_agent.py#L728) | 728 | `"        \"used_model\": \"openrouter/free\","` | — |
| [SRC-F725E90B2A-L000729](../../tests/test_web_agent.py#L729) | 729 | `"        \"fallback_used\": \"true\","` | — |
| [SRC-F725E90B2A-L000730](../../tests/test_web_agent.py#L730) | 730 | `"    }]"` | — |
| [SRC-F725E90B2A-L000731](../../tests/test_web_agent.py#L731) | 731 | `""` | — |
| [SRC-F725E90B2A-L000732](../../tests/test_web_agent.py#L732) | 732 | `""` | — |
| [SRC-F725E90B2A-L000733](../../tests/test_web_agent.py#L733) | 733 | `""` | — |
| [SRC-F725E90B2A-L000734](../../tests/test_web_agent.py#L734) | 734 | `""` | — |
| [SRC-F725E90B2A-L000735](../../tests/test_web_agent.py#L735) | 735 | `"def test_generator_rejects_silent_character_limit_truncation(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000736](../../tests/test_web_agent.py#L736) | 736 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000737](../../tests/test_web_agent.py#L737) | 737 | `"    monkeypatch.setattr(agent, \"_request_completion\", lambda *args, **kwargs: \"ن\" * 24_001)"` | — |
| [SRC-F725E90B2A-L000738](../../tests/test_web_agent.py#L738) | 738 | `""` | — |
| [SRC-F725E90B2A-L000739](../../tests/test_web_agent.py#L739) | 739 | `"    with pytest.raises(RuntimeError, match=\"تجاوزت حد طول النص\"):"` | — |
| [SRC-F725E90B2A-L000740](../../tests/test_web_agent.py#L740) | 740 | `"        agent._generate("` | — |
| [SRC-F725E90B2A-L000741](../../tests/test_web_agent.py#L741) | 741 | `"            question=\"لخص هذا المصدر\","` | — |
| [SRC-F725E90B2A-L000742](../../tests/test_web_agent.py#L742) | 742 | `"            history=[],"` | — |
| [SRC-F725E90B2A-L000743](../../tests/test_web_agent.py#L743) | 743 | `"            sources=[sample_source(0), sample_source(1)],"` | — |
| [SRC-F725E90B2A-L000744](../../tests/test_web_agent.py#L744) | 744 | `"            search_warning=None,"` | — |
| [SRC-F725E90B2A-L000745](../../tests/test_web_agent.py#L745) | 745 | `"            research_plan={\"depth\": \"standard\", \"queries\": [\"لخص هذا المصدر\"]},"` | — |
| [SRC-F725E90B2A-L000746](../../tests/test_web_agent.py#L746) | 746 | `"            search_report={},"` | — |
| [SRC-F725E90B2A-L000747](../../tests/test_web_agent.py#L747) | 747 | `"        )"` | — |
| [SRC-F725E90B2A-L000748](../../tests/test_web_agent.py#L748) | 748 | `""` | — |
| [SRC-F725E90B2A-L000749](../../tests/test_web_agent.py#L749) | 749 | `""` | — |
| [SRC-F725E90B2A-L000750](../../tests/test_web_agent.py#L750) | 750 | `"def test_completion_discards_truncated_primary_and_uses_complete_fallback(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000751](../../tests/test_web_agent.py#L751) | 751 | `"    import json"` | — |
| [SRC-F725E90B2A-L000752](../../tests/test_web_agent.py#L752) | 752 | `""` | — |
| [SRC-F725E90B2A-L000753](../../tests/test_web_agent.py#L753) | 753 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000754](../../tests/test_web_agent.py#L754) | 754 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000755](../../tests/test_web_agent.py#L755) | 755 | `"    agent.fallback_model = \"openrouter/free\""` | — |
| [SRC-F725E90B2A-L000756](../../tests/test_web_agent.py#L756) | 756 | `"    called = []"` | — |
| [SRC-F725E90B2A-L000757](../../tests/test_web_agent.py#L757) | 757 | `""` | — |
| [SRC-F725E90B2A-L000758](../../tests/test_web_agent.py#L758) | 758 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000759](../../tests/test_web_agent.py#L759) | 759 | `"        def __init__(self, content, finish_reason):"` | — |
| [SRC-F725E90B2A-L000760](../../tests/test_web_agent.py#L760) | 760 | `"            self.body = json.dumps({"` | — |
| [SRC-F725E90B2A-L000761](../../tests/test_web_agent.py#L761) | 761 | `"                \"choices\": [{"` | — |
| [SRC-F725E90B2A-L000762](../../tests/test_web_agent.py#L762) | 762 | `"                    \"message\": {\"content\": content},"` | — |
| [SRC-F725E90B2A-L000763](../../tests/test_web_agent.py#L763) | 763 | `"                    \"finish_reason\": finish_reason,"` | — |
| [SRC-F725E90B2A-L000764](../../tests/test_web_agent.py#L764) | 764 | `"                }]"` | — |
| [SRC-F725E90B2A-L000765](../../tests/test_web_agent.py#L765) | 765 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000766](../../tests/test_web_agent.py#L766) | 766 | `""` | — |
| [SRC-F725E90B2A-L000767](../../tests/test_web_agent.py#L767) | 767 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L000768](../../tests/test_web_agent.py#L768) | 768 | `"            return self"` | — |
| [SRC-F725E90B2A-L000769](../../tests/test_web_agent.py#L769) | 769 | `""` | — |
| [SRC-F725E90B2A-L000770](../../tests/test_web_agent.py#L770) | 770 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L000771](../../tests/test_web_agent.py#L771) | 771 | `"            return False"` | — |
| [SRC-F725E90B2A-L000772](../../tests/test_web_agent.py#L772) | 772 | `""` | — |
| [SRC-F725E90B2A-L000773](../../tests/test_web_agent.py#L773) | 773 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L000774](../../tests/test_web_agent.py#L774) | 774 | `"            return self.body"` | — |
| [SRC-F725E90B2A-L000775](../../tests/test_web_agent.py#L775) | 775 | `""` | — |
| [SRC-F725E90B2A-L000776](../../tests/test_web_agent.py#L776) | 776 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L000777](../../tests/test_web_agent.py#L777) | 777 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-F725E90B2A-L000778](../../tests/test_web_agent.py#L778) | 778 | `"        called.append(model)"` | — |
| [SRC-F725E90B2A-L000779](../../tests/test_web_agent.py#L779) | 779 | `"        if model == \"broken/primary\":"` | — |
| [SRC-F725E90B2A-L000780](../../tests/test_web_agent.py#L780) | 780 | `"            return FakeResponse(\"جزء مبتور لا يجوز عرضه\", \"length\")"` | — |
| [SRC-F725E90B2A-L000781](../../tests/test_web_agent.py#L781) | 781 | `"        return FakeResponse(\"إجابة مكتملة\", \"stop\")"` | — |
| [SRC-F725E90B2A-L000782](../../tests/test_web_agent.py#L782) | 782 | `""` | — |
| [SRC-F725E90B2A-L000783](../../tests/test_web_agent.py#L783) | 783 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L000784](../../tests/test_web_agent.py#L784) | 784 | `"    result = agent._request_completion("` | — |
| [SRC-F725E90B2A-L000785](../../tests/test_web_agent.py#L785) | 785 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-F725E90B2A-L000786](../../tests/test_web_agent.py#L786) | 786 | `"        model=\"broken/primary\","` | — |
| [SRC-F725E90B2A-L000787](../../tests/test_web_agent.py#L787) | 787 | `"    )"` | — |
| [SRC-F725E90B2A-L000788](../../tests/test_web_agent.py#L788) | 788 | `""` | — |
| [SRC-F725E90B2A-L000789](../../tests/test_web_agent.py#L789) | 789 | `"    assert result == \"إجابة مكتملة\""` | — |
| [SRC-F725E90B2A-L000790](../../tests/test_web_agent.py#L790) | 790 | `"    assert called == [\"broken/primary\", \"openrouter/free\"]"` | — |
| [SRC-F725E90B2A-L000791](../../tests/test_web_agent.py#L791) | 791 | `"    assert \"جزء مبتور لا يجوز عرضه\" not in result"` | — |
| [SRC-F725E90B2A-L000792](../../tests/test_web_agent.py#L792) | 792 | `"    assert agent.model_usage == [{"` | — |
| [SRC-F725E90B2A-L000793](../../tests/test_web_agent.py#L793) | 793 | `"        \"requested_model\": \"broken/primary\","` | — |
| [SRC-F725E90B2A-L000794](../../tests/test_web_agent.py#L794) | 794 | `"        \"used_model\": \"openrouter/free\","` | — |
| [SRC-F725E90B2A-L000795](../../tests/test_web_agent.py#L795) | 795 | `"        \"fallback_used\": \"true\","` | — |
| [SRC-F725E90B2A-L000796](../../tests/test_web_agent.py#L796) | 796 | `"    }]"` | — |
| [SRC-F725E90B2A-L000797](../../tests/test_web_agent.py#L797) | 797 | `""` | — |
| [SRC-F725E90B2A-L000798](../../tests/test_web_agent.py#L798) | 798 | `""` | — |
| [SRC-F725E90B2A-L000799](../../tests/test_web_agent.py#L799) | 799 | `"def test_completion_rejects_response_when_all_models_are_truncated(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000800](../../tests/test_web_agent.py#L800) | 800 | `"    import json"` | — |
| [SRC-F725E90B2A-L000801](../../tests/test_web_agent.py#L801) | 801 | `""` | — |
| [SRC-F725E90B2A-L000802](../../tests/test_web_agent.py#L802) | 802 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000803](../../tests/test_web_agent.py#L803) | 803 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000804](../../tests/test_web_agent.py#L804) | 804 | `"    agent.fallback_model = \"fallback/model\""` | — |
| [SRC-F725E90B2A-L000805](../../tests/test_web_agent.py#L805) | 805 | `"    called = []"` | — |
| [SRC-F725E90B2A-L000806](../../tests/test_web_agent.py#L806) | 806 | `""` | — |
| [SRC-F725E90B2A-L000807](../../tests/test_web_agent.py#L807) | 807 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000808](../../tests/test_web_agent.py#L808) | 808 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L000809](../../tests/test_web_agent.py#L809) | 809 | `"            return self"` | — |
| [SRC-F725E90B2A-L000810](../../tests/test_web_agent.py#L810) | 810 | `""` | — |
| [SRC-F725E90B2A-L000811](../../tests/test_web_agent.py#L811) | 811 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L000812](../../tests/test_web_agent.py#L812) | 812 | `"            return False"` | — |
| [SRC-F725E90B2A-L000813](../../tests/test_web_agent.py#L813) | 813 | `""` | — |
| [SRC-F725E90B2A-L000814](../../tests/test_web_agent.py#L814) | 814 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L000815](../../tests/test_web_agent.py#L815) | 815 | `"            return json.dumps({"` | — |
| [SRC-F725E90B2A-L000816](../../tests/test_web_agent.py#L816) | 816 | `"                \"choices\": [{"` | — |
| [SRC-F725E90B2A-L000817](../../tests/test_web_agent.py#L817) | 817 | `"                    \"message\": {\"content\": \"نص مبتور\"},"` | — |
| [SRC-F725E90B2A-L000818](../../tests/test_web_agent.py#L818) | 818 | `"                    \"finish_reason\": \"length\","` | — |
| [SRC-F725E90B2A-L000819](../../tests/test_web_agent.py#L819) | 819 | `"                }]"` | — |
| [SRC-F725E90B2A-L000820](../../tests/test_web_agent.py#L820) | 820 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000821](../../tests/test_web_agent.py#L821) | 821 | `""` | — |
| [SRC-F725E90B2A-L000822](../../tests/test_web_agent.py#L822) | 822 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L000823](../../tests/test_web_agent.py#L823) | 823 | `"        called.append(json.loads(request.data.decode(\"utf-8\"))[\"model\"])"` | — |
| [SRC-F725E90B2A-L000824](../../tests/test_web_agent.py#L824) | 824 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L000825](../../tests/test_web_agent.py#L825) | 825 | `""` | — |
| [SRC-F725E90B2A-L000826](../../tests/test_web_agent.py#L826) | 826 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L000827](../../tests/test_web_agent.py#L827) | 827 | `"    with pytest.raises(RuntimeError, match=\"مبتورة\"):"` | — |
| [SRC-F725E90B2A-L000828](../../tests/test_web_agent.py#L828) | 828 | `"        agent._request_completion("` | — |
| [SRC-F725E90B2A-L000829](../../tests/test_web_agent.py#L829) | 829 | `"            [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-F725E90B2A-L000830](../../tests/test_web_agent.py#L830) | 830 | `"            model=\"broken/primary\","` | — |
| [SRC-F725E90B2A-L000831](../../tests/test_web_agent.py#L831) | 831 | `"        )"` | — |
| [SRC-F725E90B2A-L000832](../../tests/test_web_agent.py#L832) | 832 | `""` | — |
| [SRC-F725E90B2A-L000833](../../tests/test_web_agent.py#L833) | 833 | `"    assert called == [\"broken/primary\", \"fallback/model\"]"` | — |
| [SRC-F725E90B2A-L000834](../../tests/test_web_agent.py#L834) | 834 | `"    assert agent.model_usage == []"` | — |
| [SRC-F725E90B2A-L000835](../../tests/test_web_agent.py#L835) | 835 | `""` | — |
| [SRC-F725E90B2A-L000836](../../tests/test_web_agent.py#L836) | 836 | `""` | — |
| [SRC-F725E90B2A-L000837](../../tests/test_web_agent.py#L837) | 837 | `"def test_completion_falls_back_for_malformed_choice(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000838](../../tests/test_web_agent.py#L838) | 838 | `"    import json"` | — |
| [SRC-F725E90B2A-L000839](../../tests/test_web_agent.py#L839) | 839 | `""` | — |
| [SRC-F725E90B2A-L000840](../../tests/test_web_agent.py#L840) | 840 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000841](../../tests/test_web_agent.py#L841) | 841 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000842](../../tests/test_web_agent.py#L842) | 842 | `"    agent.fallback_model = \"fallback/model\""` | — |
| [SRC-F725E90B2A-L000843](../../tests/test_web_agent.py#L843) | 843 | `"    called = []"` | — |
| [SRC-F725E90B2A-L000844](../../tests/test_web_agent.py#L844) | 844 | `""` | — |
| [SRC-F725E90B2A-L000845](../../tests/test_web_agent.py#L845) | 845 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000846](../../tests/test_web_agent.py#L846) | 846 | `"        def __init__(self, body):"` | — |
| [SRC-F725E90B2A-L000847](../../tests/test_web_agent.py#L847) | 847 | `"            self.body = body"` | — |
| [SRC-F725E90B2A-L000848](../../tests/test_web_agent.py#L848) | 848 | `""` | — |
| [SRC-F725E90B2A-L000849](../../tests/test_web_agent.py#L849) | 849 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L000850](../../tests/test_web_agent.py#L850) | 850 | `"            return self"` | — |
| [SRC-F725E90B2A-L000851](../../tests/test_web_agent.py#L851) | 851 | `""` | — |
| [SRC-F725E90B2A-L000852](../../tests/test_web_agent.py#L852) | 852 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L000853](../../tests/test_web_agent.py#L853) | 853 | `"            return False"` | — |
| [SRC-F725E90B2A-L000854](../../tests/test_web_agent.py#L854) | 854 | `""` | — |
| [SRC-F725E90B2A-L000855](../../tests/test_web_agent.py#L855) | 855 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L000856](../../tests/test_web_agent.py#L856) | 856 | `"            return self.body"` | — |
| [SRC-F725E90B2A-L000857](../../tests/test_web_agent.py#L857) | 857 | `""` | — |
| [SRC-F725E90B2A-L000858](../../tests/test_web_agent.py#L858) | 858 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L000859](../../tests/test_web_agent.py#L859) | 859 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-F725E90B2A-L000860](../../tests/test_web_agent.py#L860) | 860 | `"        called.append(model)"` | — |
| [SRC-F725E90B2A-L000861](../../tests/test_web_agent.py#L861) | 861 | `"        choices = ("` | — |
| [SRC-F725E90B2A-L000862](../../tests/test_web_agent.py#L862) | 862 | `"            [\"malformed choice\"]"` | — |
| [SRC-F725E90B2A-L000863](../../tests/test_web_agent.py#L863) | 863 | `"            if model == \"broken/primary\""` | — |
| [SRC-F725E90B2A-L000864](../../tests/test_web_agent.py#L864) | 864 | `"            else [{\"message\": {\"content\": \"fallback answer\"}, \"finish_reason\": \"stop\"}]"` | — |
| [SRC-F725E90B2A-L000865](../../tests/test_web_agent.py#L865) | 865 | `"        )"` | — |
| [SRC-F725E90B2A-L000866](../../tests/test_web_agent.py#L866) | 866 | `"        return FakeResponse(json.dumps({\"choices\": choices}).encode(\"utf-8\"))"` | — |
| [SRC-F725E90B2A-L000867](../../tests/test_web_agent.py#L867) | 867 | `""` | — |
| [SRC-F725E90B2A-L000868](../../tests/test_web_agent.py#L868) | 868 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L000869](../../tests/test_web_agent.py#L869) | 869 | `"    result = agent._request_completion("` | — |
| [SRC-F725E90B2A-L000870](../../tests/test_web_agent.py#L870) | 870 | `"        [{\"role\": \"user\", \"content\": \"test\"}],"` | — |
| [SRC-F725E90B2A-L000871](../../tests/test_web_agent.py#L871) | 871 | `"        model=\"broken/primary\","` | — |
| [SRC-F725E90B2A-L000872](../../tests/test_web_agent.py#L872) | 872 | `"    )"` | — |
| [SRC-F725E90B2A-L000873](../../tests/test_web_agent.py#L873) | 873 | `""` | — |
| [SRC-F725E90B2A-L000874](../../tests/test_web_agent.py#L874) | 874 | `"    assert result == \"fallback answer\""` | — |
| [SRC-F725E90B2A-L000875](../../tests/test_web_agent.py#L875) | 875 | `"    assert called == [\"broken/primary\", \"fallback/model\"]"` | — |
| [SRC-F725E90B2A-L000876](../../tests/test_web_agent.py#L876) | 876 | `""` | — |
| [SRC-F725E90B2A-L000877](../../tests/test_web_agent.py#L877) | 877 | `""` | — |
| [SRC-F725E90B2A-L000878](../../tests/test_web_agent.py#L878) | 878 | `"def test_health_status_reports_models_without_credentials(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000879](../../tests/test_web_agent.py#L879) | 879 | `"    monkeypatch.delenv(\"OPENROUTER_API_KEY\", raising=False)"` | — |
| [SRC-F725E90B2A-L000880](../../tests/test_web_agent.py#L880) | 880 | `"    monkeypatch.delenv(\"OMARAI_LLM_API_KEY\", raising=False)"` | — |
| [SRC-F725E90B2A-L000881](../../tests/test_web_agent.py#L881) | 881 | `"    status = WebAgent.status()"` | — |
| [SRC-F725E90B2A-L000882](../../tests/test_web_agent.py#L882) | 882 | `"    assert status[\"planner_model\"] == \"nvidia/nemotron-3-ultra-550b-a55b:free\""` | — |
| [SRC-F725E90B2A-L000883](../../tests/test_web_agent.py#L883) | 883 | `"    assert status[\"answer_model\"] == \"google/gemma-4-31b-it:free\""` | — |
| [SRC-F725E90B2A-L000884](../../tests/test_web_agent.py#L884) | 884 | `"    assert status[\"fallback_model\"] == \"openrouter/free\""` | — |
| [SRC-F725E90B2A-L000885](../../tests/test_web_agent.py#L885) | 885 | `"    assert status[\"language_model_configured\"] is False"` | — |
| [SRC-F725E90B2A-L000886](../../tests/test_web_agent.py#L886) | 886 | `"    assert status[\"verification_scope\"][\"kind\"] == \"configuration_snapshot\""` | — |
| [SRC-F725E90B2A-L000887](../../tests/test_web_agent.py#L887) | 887 | `"    assert status[\"verification_scope\"][\"live_network_checks_performed\"] is False"` | — |
| [SRC-F725E90B2A-L000888](../../tests/test_web_agent.py#L888) | 888 | `"    assert status[\"verification_scope\"][\"language_model_configured_means\"] == ("` | — |
| [SRC-F725E90B2A-L000889](../../tests/test_web_agent.py#L889) | 889 | `"        \"credential_present_not_successful_completion\""` | — |
| [SRC-F725E90B2A-L000890](../../tests/test_web_agent.py#L890) | 890 | `"    )"` | — |
| [SRC-F725E90B2A-L000891](../../tests/test_web_agent.py#L891) | 891 | `"    assert status[\"verification_scope\"][\"live_diagnostics_endpoint\"] == \"POST /api/diagnostics\""` | — |
| [SRC-F725E90B2A-L000892](../../tests/test_web_agent.py#L892) | 892 | `"    assert \"api_key\" not in status"` | — |
| [SRC-F725E90B2A-L000893](../../tests/test_web_agent.py#L893) | 893 | `""` | — |
| [SRC-F725E90B2A-L000894](../../tests/test_web_agent.py#L894) | 894 | `""` | — |
| [SRC-F725E90B2A-L000895](../../tests/test_web_agent.py#L895) | 895 | `""` | — |
| [SRC-F725E90B2A-L000896](../../tests/test_web_agent.py#L896) | 896 | `"def test_health_status_exposes_external_model_privacy_notice_without_secrets(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000897](../../tests/test_web_agent.py#L897) | 897 | `"    monkeypatch.delenv(\"OPENROUTER_API_KEY\", raising=False)"` | — |
| [SRC-F725E90B2A-L000898](../../tests/test_web_agent.py#L898) | 898 | `"    monkeypatch.delenv(\"OMARAI_LLM_API_KEY\", raising=False)"` | — |
| [SRC-F725E90B2A-L000899](../../tests/test_web_agent.py#L899) | 899 | `"    status = WebAgent.status()"` | — |
| [SRC-F725E90B2A-L000900](../../tests/test_web_agent.py#L900) | 900 | `"    notice = status[\"external_model_privacy_notice\"]"` | — |
| [SRC-F725E90B2A-L000901](../../tests/test_web_agent.py#L901) | 901 | `"    assert \"external model provider\" in notice"` | — |
| [SRC-F725E90B2A-L000902](../../tests/test_web_agent.py#L902) | 902 | `"    assert \"personal/confidential customer data\" in notice"` | — |
| [SRC-F725E90B2A-L000903](../../tests/test_web_agent.py#L903) | 903 | `"    assert \"api_key\" not in status"` | — |
| [SRC-F725E90B2A-L000904](../../tests/test_web_agent.py#L904) | 904 | `"    assert \"OPENROUTER_API_KEY\" not in str(status)"` | — |
| [SRC-F725E90B2A-L000905](../../tests/test_web_agent.py#L905) | 905 | `""` | — |
| [SRC-F725E90B2A-L000906](../../tests/test_web_agent.py#L906) | 906 | `""` | — |
| [SRC-F725E90B2A-L000907](../../tests/test_web_agent.py#L907) | 907 | `""` | — |
| [SRC-F725E90B2A-L000908](../../tests/test_web_agent.py#L908) | 908 | `"def test_diagnostics_runs_real_search_and_can_skip_paid_or_rate_limited_model_calls(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000909](../../tests/test_web_agent.py#L909) | 909 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000910](../../tests/test_web_agent.py#L910) | 910 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: ["` | — |
| [SRC-F725E90B2A-L000911](../../tests/test_web_agent.py#L911) | 911 | `"        {\"provider\": \"duckduckgo_html\", \"url\": \"https://example.com/a\"},"` | — |
| [SRC-F725E90B2A-L000912](../../tests/test_web_agent.py#L912) | 912 | `"        {\"provider\": \"bing_rss\", \"url\": \"https://example.com/b\"},"` | — |
| [SRC-F725E90B2A-L000913](../../tests/test_web_agent.py#L913) | 913 | `"    ])"` | — |
| [SRC-F725E90B2A-L000914](../../tests/test_web_agent.py#L914) | 914 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000915](../../tests/test_web_agent.py#L915) | 915 | `"        agent,"` | — |
| [SRC-F725E90B2A-L000916](../../tests/test_web_agent.py#L916) | 916 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L000917](../../tests/test_web_agent.py#L917) | 917 | `"        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError(\"model should be skipped\")),"` | — |
| [SRC-F725E90B2A-L000918](../../tests/test_web_agent.py#L918) | 918 | `"    )"` | — |
| [SRC-F725E90B2A-L000919](../../tests/test_web_agent.py#L919) | 919 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L000920](../../tests/test_web_agent.py#L920) | 920 | `"    assert report[\"checks\"][\"web_search\"][\"status\"] == \"passed\""` | — |
| [SRC-F725E90B2A-L000921](../../tests/test_web_agent.py#L921) | 921 | `"    assert report[\"checks\"][\"web_search\"][\"provider_counts\"] == {"` | — |
| [SRC-F725E90B2A-L000922](../../tests/test_web_agent.py#L922) | 922 | `"        \"duckduckgo_html\": 1, \"bing_rss\": 1"` | — |
| [SRC-F725E90B2A-L000923](../../tests/test_web_agent.py#L923) | 923 | `"    }"` | — |
| [SRC-F725E90B2A-L000924](../../tests/test_web_agent.py#L924) | 924 | `"    assert report[\"checks\"][\"language_model\"][\"status\"] == \"skipped\""` | — |
| [SRC-F725E90B2A-L000925](../../tests/test_web_agent.py#L925) | 925 | `"    assert report[\"checks\"][\"social_search\"][\"status\"] == \"skipped\""` | — |
| [SRC-F725E90B2A-L000926](../../tests/test_web_agent.py#L926) | 926 | `"    assert report[\"elapsed_ms\"] >= 0"` | — |
| [SRC-F725E90B2A-L000927](../../tests/test_web_agent.py#L927) | 927 | `"    assert \"api_key\" not in str(report)"` | — |
| [SRC-F725E90B2A-L000928](../../tests/test_web_agent.py#L928) | 928 | `""` | — |
| [SRC-F725E90B2A-L000929](../../tests/test_web_agent.py#L929) | 929 | `""` | — |
| [SRC-F725E90B2A-L000930](../../tests/test_web_agent.py#L930) | 930 | `"def test_diagnostics_calls_a_model_only_when_explicitly_requested(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000931](../../tests/test_web_agent.py#L931) | 931 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000932](../../tests/test_web_agent.py#L932) | 932 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000933](../../tests/test_web_agent.py#L933) | 933 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: ["` | — |
| [SRC-F725E90B2A-L000934](../../tests/test_web_agent.py#L934) | 934 | `"        {\"provider\": \"duckduckgo_html\", \"url\": \"https://example.com/a\"}"` | — |
| [SRC-F725E90B2A-L000935](../../tests/test_web_agent.py#L935) | 935 | `"    ])"` | — |
| [SRC-F725E90B2A-L000936](../../tests/test_web_agent.py#L936) | 936 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000937](../../tests/test_web_agent.py#L937) | 937 | `""` | — |
| [SRC-F725E90B2A-L000938](../../tests/test_web_agent.py#L938) | 938 | `"    def completion(*args, **kwargs):"` | — |
| [SRC-F725E90B2A-L000939](../../tests/test_web_agent.py#L939) | 939 | `"        calls.append(kwargs.get(\"model\"))"` | — |
| [SRC-F725E90B2A-L000940](../../tests/test_web_agent.py#L940) | 940 | `"        agent.model_usage.append({"` | — |
| [SRC-F725E90B2A-L000941](../../tests/test_web_agent.py#L941) | 941 | `"            \"requested_model\": kwargs.get(\"model\", \"\"),"` | — |
| [SRC-F725E90B2A-L000942](../../tests/test_web_agent.py#L942) | 942 | `"            \"used_model\": kwargs.get(\"model\", \"\"),"` | — |
| [SRC-F725E90B2A-L000943](../../tests/test_web_agent.py#L943) | 943 | `"            \"fallback_used\": \"false\","` | — |
| [SRC-F725E90B2A-L000944](../../tests/test_web_agent.py#L944) | 944 | `"        })"` | — |
| [SRC-F725E90B2A-L000945](../../tests/test_web_agent.py#L945) | 945 | `"        return \"OK\""` | — |
| [SRC-F725E90B2A-L000946](../../tests/test_web_agent.py#L946) | 946 | `""` | — |
| [SRC-F725E90B2A-L000947](../../tests/test_web_agent.py#L947) | 947 | `"    monkeypatch.setattr(agent, \"_request_completion\", completion)"` | — |
| [SRC-F725E90B2A-L000948](../../tests/test_web_agent.py#L948) | 948 | `"    report = agent.diagnostics(test_model=True, test_social=False)"` | — |
| [SRC-F725E90B2A-L000949](../../tests/test_web_agent.py#L949) | 949 | `"    assert report[\"checks\"][\"language_model\"][\"status\"] == \"passed\""` | — |
| [SRC-F725E90B2A-L000950](../../tests/test_web_agent.py#L950) | 950 | `"    assert calls == [agent.answer_model]"` | — |
| [SRC-F725E90B2A-L000951](../../tests/test_web_agent.py#L951) | 951 | `"    assert len(report[\"model_usage\"]) == 1"` | — |
| [SRC-F725E90B2A-L000952](../../tests/test_web_agent.py#L952) | 952 | `""` | — |
| [SRC-F725E90B2A-L000953](../../tests/test_web_agent.py#L953) | 953 | `""` | — |
| [SRC-F725E90B2A-L000954](../../tests/test_web_agent.py#L954) | 954 | `""` | — |
| [SRC-F725E90B2A-L000955](../../tests/test_web_agent.py#L955) | 955 | `""` | — |
| [SRC-F725E90B2A-L000956](../../tests/test_web_agent.py#L956) | 956 | `"def test_diagnostics_reports_degraded_when_search_has_no_results_and_model_is_unconfigured(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000957](../../tests/test_web_agent.py#L957) | 957 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000958](../../tests/test_web_agent.py#L958) | 958 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L000959](../../tests/test_web_agent.py#L959) | 959 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: [])"` | — |
| [SRC-F725E90B2A-L000960](../../tests/test_web_agent.py#L960) | 960 | `""` | — |
| [SRC-F725E90B2A-L000961](../../tests/test_web_agent.py#L961) | 961 | `"    report = agent.diagnostics(test_model=True, test_social=False)"` | — |
| [SRC-F725E90B2A-L000962](../../tests/test_web_agent.py#L962) | 962 | `""` | — |
| [SRC-F725E90B2A-L000963](../../tests/test_web_agent.py#L963) | 963 | `"    assert report[\"checks\"][\"web_search\"][\"status\"] == \"degraded\""` | — |
| [SRC-F725E90B2A-L000964](../../tests/test_web_agent.py#L964) | 964 | `"    assert report[\"checks\"][\"language_model\"][\"status\"] == \"not_configured\""` | — |
| [SRC-F725E90B2A-L000965](../../tests/test_web_agent.py#L965) | 965 | `"    assert report[\"checks\"][\"social_search\"][\"status\"] == \"skipped\""` | — |
| [SRC-F725E90B2A-L000966](../../tests/test_web_agent.py#L966) | 966 | `"    assert report[\"overall_status\"] == \"degraded\""` | — |
| [SRC-F725E90B2A-L000967](../../tests/test_web_agent.py#L967) | 967 | `""` | — |
| [SRC-F725E90B2A-L000968](../../tests/test_web_agent.py#L968) | 968 | `""` | — |
| [SRC-F725E90B2A-L000969](../../tests/test_web_agent.py#L969) | 969 | `"def test_diagnostics_does_not_report_full_success_when_model_probe_fails(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000970](../../tests/test_web_agent.py#L970) | 970 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000971](../../tests/test_web_agent.py#L971) | 971 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000972](../../tests/test_web_agent.py#L972) | 972 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: ["` | — |
| [SRC-F725E90B2A-L000973](../../tests/test_web_agent.py#L973) | 973 | `"        {\"provider\": \"duckduckgo_html\", \"url\": \"https://example.com/a\"}"` | — |
| [SRC-F725E90B2A-L000974](../../tests/test_web_agent.py#L974) | 974 | `"    ])"` | — |
| [SRC-F725E90B2A-L000975](../../tests/test_web_agent.py#L975) | 975 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000976](../../tests/test_web_agent.py#L976) | 976 | `"        agent,"` | — |
| [SRC-F725E90B2A-L000977](../../tests/test_web_agent.py#L977) | 977 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L000978](../../tests/test_web_agent.py#L978) | 978 | `"        lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError(\"provider unavailable\")),"` | — |
| [SRC-F725E90B2A-L000979](../../tests/test_web_agent.py#L979) | 979 | `"    )"` | — |
| [SRC-F725E90B2A-L000980](../../tests/test_web_agent.py#L980) | 980 | `""` | — |
| [SRC-F725E90B2A-L000981](../../tests/test_web_agent.py#L981) | 981 | `"    report = agent.diagnostics(test_model=True, test_social=False)"` | — |
| [SRC-F725E90B2A-L000982](../../tests/test_web_agent.py#L982) | 982 | `""` | — |
| [SRC-F725E90B2A-L000983](../../tests/test_web_agent.py#L983) | 983 | `"    assert report[\"checks\"][\"web_search\"][\"status\"] == \"passed\""` | — |
| [SRC-F725E90B2A-L000984](../../tests/test_web_agent.py#L984) | 984 | `"    assert report[\"checks\"][\"language_model\"][\"status\"] == \"failed\""` | — |
| [SRC-F725E90B2A-L000985](../../tests/test_web_agent.py#L985) | 985 | `"    assert report[\"overall_status\"] == \"degraded\""` | — |
| [SRC-F725E90B2A-L000986](../../tests/test_web_agent.py#L986) | 986 | `"    assert \"test-key\" not in str(report)"` | — |
| [SRC-F725E90B2A-L000987](../../tests/test_web_agent.py#L987) | 987 | `""` | — |
| [SRC-F725E90B2A-L000988](../../tests/test_web_agent.py#L988) | 988 | `""` | — |
| [SRC-F725E90B2A-L000989](../../tests/test_web_agent.py#L989) | 989 | `"def test_openrouter_live_web_search_tool_is_opt_in_and_returns_citations(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000990](../../tests/test_web_agent.py#L990) | 990 | `"    import json"` | — |
| [SRC-F725E90B2A-L000991](../../tests/test_web_agent.py#L991) | 991 | `""` | — |
| [SRC-F725E90B2A-L000992](../../tests/test_web_agent.py#L992) | 992 | `"    monkeypatch.setenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"1\")"` | — |
| [SRC-F725E90B2A-L000993](../../tests/test_web_agent.py#L993) | 993 | `"    monkeypatch.setenv(\"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\")"` | — |
| [SRC-F725E90B2A-L000994](../../tests/test_web_agent.py#L994) | 994 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000995](../../tests/test_web_agent.py#L995) | 995 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000996](../../tests/test_web_agent.py#L996) | 996 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L000997](../../tests/test_web_agent.py#L997) | 997 | `""` | — |
| [SRC-F725E90B2A-L000998](../../tests/test_web_agent.py#L998) | 998 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000999](../../tests/test_web_agent.py#L999) | 999 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L001000](../../tests/test_web_agent.py#L1000) | 1000 | `"            return self"` | — |
| [SRC-F725E90B2A-L001001](../../tests/test_web_agent.py#L1001) | 1001 | `""` | — |
| [SRC-F725E90B2A-L001002](../../tests/test_web_agent.py#L1002) | 1002 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L001003](../../tests/test_web_agent.py#L1003) | 1003 | `"            return False"` | — |
| [SRC-F725E90B2A-L001004](../../tests/test_web_agent.py#L1004) | 1004 | `""` | — |
| [SRC-F725E90B2A-L001005](../../tests/test_web_agent.py#L1005) | 1005 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L001006](../../tests/test_web_agent.py#L1006) | 1006 | `"            return json.dumps({"` | — |
| [SRC-F725E90B2A-L001007](../../tests/test_web_agent.py#L1007) | 1007 | `"                \"choices\": [{"` | — |
| [SRC-F725E90B2A-L001008](../../tests/test_web_agent.py#L1008) | 1008 | `"                    \"message\": {"` | — |
| [SRC-F725E90B2A-L001009](../../tests/test_web_agent.py#L1009) | 1009 | `"                        \"content\": \"تحليل مستند إلى بحث حي.\","` | — |
| [SRC-F725E90B2A-L001010](../../tests/test_web_agent.py#L1010) | 1010 | `"                        \"annotations\": [{"` | — |
| [SRC-F725E90B2A-L001011](../../tests/test_web_agent.py#L1011) | 1011 | `"                            \"type\": \"url_citation\","` | — |
| [SRC-F725E90B2A-L001012](../../tests/test_web_agent.py#L1012) | 1012 | `"                            \"url_citation\": {"` | — |
| [SRC-F725E90B2A-L001013](../../tests/test_web_agent.py#L1013) | 1013 | `"                                \"url\": \"https://example.org/current-report\","` | — |
| [SRC-F725E90B2A-L001014](../../tests/test_web_agent.py#L1014) | 1014 | `"                                \"title\": \"Current public report\","` | — |
| [SRC-F725E90B2A-L001015](../../tests/test_web_agent.py#L1015) | 1015 | `"                                \"content\": \"An excerpt returned by the live search service.\","` | — |
| [SRC-F725E90B2A-L001016](../../tests/test_web_agent.py#L1016) | 1016 | `"                            },"` | — |
| [SRC-F725E90B2A-L001017](../../tests/test_web_agent.py#L1017) | 1017 | `"                        }],"` | — |
| [SRC-F725E90B2A-L001018](../../tests/test_web_agent.py#L1018) | 1018 | `"                    },"` | — |
| [SRC-F725E90B2A-L001019](../../tests/test_web_agent.py#L1019) | 1019 | `"                    \"finish_reason\": \"stop\","` | — |
| [SRC-F725E90B2A-L001020](../../tests/test_web_agent.py#L1020) | 1020 | `"                }]"` | — |
| [SRC-F725E90B2A-L001021](../../tests/test_web_agent.py#L1021) | 1021 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L001022](../../tests/test_web_agent.py#L1022) | 1022 | `""` | — |
| [SRC-F725E90B2A-L001023](../../tests/test_web_agent.py#L1023) | 1023 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L001024](../../tests/test_web_agent.py#L1024) | 1024 | `"        seen[\"payload\"] = json.loads(request.data.decode(\"utf-8\"))"` | — |
| [SRC-F725E90B2A-L001025](../../tests/test_web_agent.py#L1025) | 1025 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L001026](../../tests/test_web_agent.py#L1026) | 1026 | `""` | — |
| [SRC-F725E90B2A-L001027](../../tests/test_web_agent.py#L1027) | 1027 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L001028](../../tests/test_web_agent.py#L1028) | 1028 | `"    result = agent._request_completion("` | — |
| [SRC-F725E90B2A-L001029](../../tests/test_web_agent.py#L1029) | 1029 | `"        [{\"role\": \"user\", \"content\": \"ابحث عن أحدث تقرير\"}],"` | — |
| [SRC-F725E90B2A-L001030](../../tests/test_web_agent.py#L1030) | 1030 | `"        model=\"example/model\","` | — |
| [SRC-F725E90B2A-L001031](../../tests/test_web_agent.py#L1031) | 1031 | `"        enable_web_search=True,"` | — |
| [SRC-F725E90B2A-L001032](../../tests/test_web_agent.py#L1032) | 1032 | `"    )"` | — |
| [SRC-F725E90B2A-L001033](../../tests/test_web_agent.py#L1033) | 1033 | `""` | — |
| [SRC-F725E90B2A-L001034](../../tests/test_web_agent.py#L1034) | 1034 | `"    assert result == \"تحليل مستند إلى بحث حي.\""` | — |
| [SRC-F725E90B2A-L001035](../../tests/test_web_agent.py#L1035) | 1035 | `"    assert seen[\"payload\"][\"tools\"][0][\"type\"] == \"openrouter:web_search\""` | — |
| [SRC-F725E90B2A-L001036](../../tests/test_web_agent.py#L1036) | 1036 | `"    assert seen[\"payload\"][\"tools\"][0][\"parameters\"][\"max_uses\"] == 3"` | — |
| [SRC-F725E90B2A-L001037](../../tests/test_web_agent.py#L1037) | 1037 | `"    assert seen[\"payload\"][\"max_tool_calls\"] == 5"` | — |
| [SRC-F725E90B2A-L001038](../../tests/test_web_agent.py#L1038) | 1038 | `"    assert agent.server_search_sources[0][\"url\"] == \"https://example.org/current-report\""` | — |
| [SRC-F725E90B2A-L001039](../../tests/test_web_agent.py#L1039) | 1039 | `"    assert agent.server_search_sources[0][\"provider\"] == \"openrouter_web_search\""` | — |
| [SRC-F725E90B2A-L001040](../../tests/test_web_agent.py#L1040) | 1040 | `"    assert \"test-key\" not in str(agent.server_search_sources)"` | — |
| [SRC-F725E90B2A-L001041](../../tests/test_web_agent.py#L1041) | 1041 | `""` | — |
| [SRC-F725E90B2A-L001042](../../tests/test_web_agent.py#L1042) | 1042 | `""` | — |
| [SRC-F725E90B2A-L001043](../../tests/test_web_agent.py#L1043) | 1043 | `"def test_openrouter_live_web_search_remains_disabled_without_explicit_opt_in(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001044](../../tests/test_web_agent.py#L1044) | 1044 | `"    monkeypatch.delenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", raising=False)"` | — |
| [SRC-F725E90B2A-L001045](../../tests/test_web_agent.py#L1045) | 1045 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001046](../../tests/test_web_agent.py#L1046) | 1046 | `"    assert agent.openrouter_web_search_enabled is False"` | — |
| [SRC-F725E90B2A-L001047](../../tests/test_web_agent.py#L1047) | 1047 | `""` | — |
| [SRC-F725E90B2A-L001048](../../tests/test_web_agent.py#L1048) | 1048 | `""` | — |
| [SRC-F725E90B2A-L001049](../../tests/test_web_agent.py#L1049) | 1049 | `""` | — |
| [SRC-F725E90B2A-L001050](../../tests/test_web_agent.py#L1050) | 1050 | `"def test_arabic_query_normalization_removes_diacritics_and_unifies_hamza():"` | — |
| [SRC-F725E90B2A-L001051](../../tests/test_web_agent.py#L1051) | 1051 | `"    normalized = _normalize_search_query(\"إِنَّ أَسْعَارَ أُسْتُرَالِيَا\")"` | — |
| [SRC-F725E90B2A-L001052](../../tests/test_web_agent.py#L1052) | 1052 | `"    assert \"إ\" not in normalized"` | — |
| [SRC-F725E90B2A-L001053](../../tests/test_web_agent.py#L1053) | 1053 | `"    assert \"أ\" not in normalized"` | — |
| [SRC-F725E90B2A-L001054](../../tests/test_web_agent.py#L1054) | 1054 | `"    assert \"ا\" in normalized"` | — |
| [SRC-F725E90B2A-L001055](../../tests/test_web_agent.py#L1055) | 1055 | `"    assert normalized == \"ان اسعار استراليا\""` | — |
| [SRC-F725E90B2A-L001056](../../tests/test_web_agent.py#L1056) | 1056 | `""` | — |
| [SRC-F725E90B2A-L001057](../../tests/test_web_agent.py#L1057) | 1057 | `""` | — |
| [SRC-F725E90B2A-L001058](../../tests/test_web_agent.py#L1058) | 1058 | `"def test_relevance_filter_rejects_translation_and_sports_noise():"` | — |
| [SRC-F725E90B2A-L001059](../../tests/test_web_agent.py#L1059) | 1059 | `"    query = \"قارن Railway و Render لاستضافة Python\""` | — |
| [SRC-F725E90B2A-L001060](../../tests/test_web_agent.py#L1060) | 1060 | `"    assert _relevance_ratio(query, \"Google Translate: error in translation\") < 0.20"` | — |
| [SRC-F725E90B2A-L001061](../../tests/test_web_agent.py#L1061) | 1061 | `"    assert _relevance_ratio("` | — |
| [SRC-F725E90B2A-L001062](../../tests/test_web_agent.py#L1062) | 1062 | `"        \"أول شركة ناشئة في صعيد مصر عام 2019\","` | — |
| [SRC-F725E90B2A-L001063](../../tests/test_web_agent.py#L1063) | 1063 | `"        \"نتائج مباراة كرة القدم وأهداف الدوري المصري اليوم\","` | — |
| [SRC-F725E90B2A-L001064](../../tests/test_web_agent.py#L1064) | 1064 | `"    ) < 0.20"` | — |
| [SRC-F725E90B2A-L001065](../../tests/test_web_agent.py#L1065) | 1065 | `"    assert _relevance_ratio("` | — |
| [SRC-F725E90B2A-L001066](../../tests/test_web_agent.py#L1066) | 1066 | `"        query, \"Railway vs Render for Python app hosting comparison\""` | — |
| [SRC-F725E90B2A-L001067](../../tests/test_web_agent.py#L1067) | 1067 | `"    ) >= 0.20"` | — |
| [SRC-F725E90B2A-L001068](../../tests/test_web_agent.py#L1068) | 1068 | `""` | — |
| [SRC-F725E90B2A-L001069](../../tests/test_web_agent.py#L1069) | 1069 | `""` | — |
| [SRC-F725E90B2A-L001070](../../tests/test_web_agent.py#L1070) | 1070 | `"def test_search_provider_failure_isolated_and_logged(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001071](../../tests/test_web_agent.py#L1071) | 1071 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001072](../../tests/test_web_agent.py#L1072) | 1072 | `""` | — |
| [SRC-F725E90B2A-L001073](../../tests/test_web_agent.py#L1073) | 1073 | `"    def broken(_query):"` | — |
| [SRC-F725E90B2A-L001074](../../tests/test_web_agent.py#L1074) | 1074 | `"        raise RuntimeError(\"upstream HTTP 503\")"` | — |
| [SRC-F725E90B2A-L001075](../../tests/test_web_agent.py#L1075) | 1075 | `""` | — |
| [SRC-F725E90B2A-L001076](../../tests/test_web_agent.py#L1076) | 1076 | `"    def working(_query):"` | — |
| [SRC-F725E90B2A-L001077](../../tests/test_web_agent.py#L1077) | 1077 | `"        return [{"` | — |
| [SRC-F725E90B2A-L001078](../../tests/test_web_agent.py#L1078) | 1078 | `"            \"title\": \"Railway and Render Python hosting\","` | — |
| [SRC-F725E90B2A-L001079](../../tests/test_web_agent.py#L1079) | 1079 | `"            \"url\": \"https://example.net/hosting\","` | — |
| [SRC-F725E90B2A-L001080](../../tests/test_web_agent.py#L1080) | 1080 | `"            \"snippet\": \"Comparison of Railway and Render for Python hosting\","` | — |
| [SRC-F725E90B2A-L001081](../../tests/test_web_agent.py#L1081) | 1081 | `"            \"provider\": \"bing_rss\","` | — |
| [SRC-F725E90B2A-L001082](../../tests/test_web_agent.py#L1082) | 1082 | `"            \"provider_rank\": 1,"` | — |
| [SRC-F725E90B2A-L001083](../../tests/test_web_agent.py#L1083) | 1083 | `"        }]"` | — |
| [SRC-F725E90B2A-L001084](../../tests/test_web_agent.py#L1084) | 1084 | `""` | — |
| [SRC-F725E90B2A-L001085](../../tests/test_web_agent.py#L1085) | 1085 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", broken)"` | — |
| [SRC-F725E90B2A-L001086](../../tests/test_web_agent.py#L1086) | 1086 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", working)"` | — |
| [SRC-F725E90B2A-L001087](../../tests/test_web_agent.py#L1087) | 1087 | `"    results = agent._search_web(\"قارن Railway و Render لاستضافة Python\")"` | — |
| [SRC-F725E90B2A-L001088](../../tests/test_web_agent.py#L1088) | 1088 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L001089](../../tests/test_web_agent.py#L1089) | 1089 | `"    diagnostics = agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L001090](../../tests/test_web_agent.py#L1090) | 1090 | `"    assert any("` | — |
| [SRC-F725E90B2A-L001091](../../tests/test_web_agent.py#L1091) | 1091 | `"        row[\"provider\"] == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L001092](../../tests/test_web_agent.py#L1092) | 1092 | `"        and row[\"status\"] == \"http_error\""` | — |
| [SRC-F725E90B2A-L001093](../../tests/test_web_agent.py#L1093) | 1093 | `"        and \"HTTP 503\" in row.get(\"error\", \"\")"` | — |
| [SRC-F725E90B2A-L001094](../../tests/test_web_agent.py#L1094) | 1094 | `"        for row in diagnostics"` | — |
| [SRC-F725E90B2A-L001095](../../tests/test_web_agent.py#L1095) | 1095 | `"    )"` | — |
| [SRC-F725E90B2A-L001096](../../tests/test_web_agent.py#L1096) | 1096 | `"    assert any("` | — |
| [SRC-F725E90B2A-L001097](../../tests/test_web_agent.py#L1097) | 1097 | `"        row[\"provider\"] == \"bing_rss\" and row[\"status\"] == \"ok\""` | — |
| [SRC-F725E90B2A-L001098](../../tests/test_web_agent.py#L1098) | 1098 | `"        for row in diagnostics"` | — |
| [SRC-F725E90B2A-L001099](../../tests/test_web_agent.py#L1099) | 1099 | `"    )"` | — |
| [SRC-F725E90B2A-L001100](../../tests/test_web_agent.py#L1100) | 1100 | `""` | — |
| [SRC-F725E90B2A-L001101](../../tests/test_web_agent.py#L1101) | 1101 | `""` | — |
| [SRC-F725E90B2A-L001102](../../tests/test_web_agent.py#L1102) | 1102 | `"def test_single_user_supplied_page_can_be_summarized_without_claiming_corroboration(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001103](../../tests/test_web_agent.py#L1103) | 1103 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001104](../../tests/test_web_agent.py#L1104) | 1104 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L001105](../../tests/test_web_agent.py#L1105) | 1105 | `"    source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L001106](../../tests/test_web_agent.py#L1106) | 1106 | `"    source[\"providers\"] = [\"user_supplied_url\"]"` | — |
| [SRC-F725E90B2A-L001107](../../tests/test_web_agent.py#L1107) | 1107 | `"    source[\"page_fetched\"] = True"` | — |
| [SRC-F725E90B2A-L001108](../../tests/test_web_agent.py#L1108) | 1108 | `"    source[\"page_text\"] = \"النص الكامل المستخرج من الصفحة التي قدمها المستخدم.\""` | — |
| [SRC-F725E90B2A-L001109](../../tests/test_web_agent.py#L1109) | 1109 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001110](../../tests/test_web_agent.py#L1110) | 1110 | `"        \"queries\": [\"لخص الصفحة\"],"` | — |
| [SRC-F725E90B2A-L001111](../../tests/test_web_agent.py#L1111) | 1111 | `"        \"direct_urls\": [\"https://example.com/research\"],"` | — |
| [SRC-F725E90B2A-L001112](../../tests/test_web_agent.py#L1112) | 1112 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001113](../../tests/test_web_agent.py#L1113) | 1113 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L001114](../../tests/test_web_agent.py#L1114) | 1114 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001115](../../tests/test_web_agent.py#L1115) | 1115 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001116](../../tests/test_web_agent.py#L1116) | 1116 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001117](../../tests/test_web_agent.py#L1117) | 1117 | `"    }"` | — |
| [SRC-F725E90B2A-L001118](../../tests/test_web_agent.py#L1118) | 1118 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001119](../../tests/test_web_agent.py#L1119) | 1119 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001120](../../tests/test_web_agent.py#L1120) | 1120 | `"        agent,"` | — |
| [SRC-F725E90B2A-L001121](../../tests/test_web_agent.py#L1121) | 1121 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L001122](../../tests/test_web_agent.py#L1122) | 1122 | `"        lambda research_plan: ("` | — |
| [SRC-F725E90B2A-L001123](../../tests/test_web_agent.py#L1123) | 1123 | `"            [source], [], {"` | — |
| [SRC-F725E90B2A-L001124](../../tests/test_web_agent.py#L1124) | 1124 | `"                \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L001125](../../tests/test_web_agent.py#L1125) | 1125 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001126](../../tests/test_web_agent.py#L1126) | 1126 | `"                \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L001127](../../tests/test_web_agent.py#L1127) | 1127 | `"                \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L001128](../../tests/test_web_agent.py#L1128) | 1128 | `"                \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L001129](../../tests/test_web_agent.py#L1129) | 1129 | `"                \"providers_used\": [\"user_supplied_url\"],"` | — |
| [SRC-F725E90B2A-L001130](../../tests/test_web_agent.py#L1130) | 1130 | `"                \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L001131](../../tests/test_web_agent.py#L1131) | 1131 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001132](../../tests/test_web_agent.py#L1132) | 1132 | `"                \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001133](../../tests/test_web_agent.py#L1133) | 1133 | `"                \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001134](../../tests/test_web_agent.py#L1134) | 1134 | `"            },"` | — |
| [SRC-F725E90B2A-L001135](../../tests/test_web_agent.py#L1135) | 1135 | `"        ),"` | — |
| [SRC-F725E90B2A-L001136](../../tests/test_web_agent.py#L1136) | 1136 | `"    )"` | — |
| [SRC-F725E90B2A-L001137](../../tests/test_web_agent.py#L1137) | 1137 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"ملخص محتوى الصفحة [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L001138](../../tests/test_web_agent.py#L1138) | 1138 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L001139](../../tests/test_web_agent.py#L1139) | 1139 | `""` | — |
| [SRC-F725E90B2A-L001140](../../tests/test_web_agent.py#L1140) | 1140 | `"    result = agent.answer(\"لخص الصفحة https://example.com/research\")"` | — |
| [SRC-F725E90B2A-L001141](../../tests/test_web_agent.py#L1141) | 1141 | `""` | — |
| [SRC-F725E90B2A-L001142](../../tests/test_web_agent.py#L1142) | 1142 | `"    assert result[\"kind\"] != \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L001143](../../tests/test_web_agent.py#L1143) | 1143 | `"    assert result[\"answer\"] == \"ملخص محتوى الصفحة [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L001144](../../tests/test_web_agent.py#L1144) | 1144 | `"    assert result[\"search_report\"][\"independent_sources\"] == 1"` | — |
| [SRC-F725E90B2A-L001145](../../tests/test_web_agent.py#L1145) | 1145 | `"    assert result[\"research_quality\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L001146](../../tests/test_web_agent.py#L1146) | 1146 | `"    assert any(\"لم يتم تأكيد محتواه\" in warning for warning in result[\"warnings\"])"` | — |
| [SRC-F725E90B2A-L001147](../../tests/test_web_agent.py#L1147) | 1147 | `""` | — |
| [SRC-F725E90B2A-L001148](../../tests/test_web_agent.py#L1148) | 1148 | `""` | — |
| [SRC-F725E90B2A-L001149](../../tests/test_web_agent.py#L1149) | 1149 | `""` | — |
| [SRC-F725E90B2A-L001150](../../tests/test_web_agent.py#L1150) | 1150 | `"def test_answer_hides_unwrapped_internal_review_report(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001151](../../tests/test_web_agent.py#L1151) | 1151 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001152](../../tests/test_web_agent.py#L1152) | 1152 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L001153](../../tests/test_web_agent.py#L1153) | 1153 | `"    sources = [sample_source(0), sample_source(1)]"` | — |
| [SRC-F725E90B2A-L001154](../../tests/test_web_agent.py#L1154) | 1154 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001155](../../tests/test_web_agent.py#L1155) | 1155 | `"        \"queries\": [\"قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية\"],"` | — |
| [SRC-F725E90B2A-L001156](../../tests/test_web_agent.py#L1156) | 1156 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L001157](../../tests/test_web_agent.py#L1157) | 1157 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001158](../../tests/test_web_agent.py#L1158) | 1158 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L001159](../../tests/test_web_agent.py#L1159) | 1159 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L001160](../../tests/test_web_agent.py#L1160) | 1160 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001161](../../tests/test_web_agent.py#L1161) | 1161 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001162](../../tests/test_web_agent.py#L1162) | 1162 | `"    }"` | — |
| [SRC-F725E90B2A-L001163](../../tests/test_web_agent.py#L1163) | 1163 | `""` | — |
| [SRC-F725E90B2A-L001164](../../tests/test_web_agent.py#L1164) | 1164 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L001165](../../tests/test_web_agent.py#L1165) | 1165 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L001166](../../tests/test_web_agent.py#L1166) | 1166 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L001167](../../tests/test_web_agent.py#L1167) | 1167 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L001168](../../tests/test_web_agent.py#L1168) | 1168 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L001169](../../tests/test_web_agent.py#L1169) | 1169 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-F725E90B2A-L001170](../../tests/test_web_agent.py#L1170) | 1170 | `"            \"pages_fetched\": len(sources),"` | — |
| [SRC-F725E90B2A-L001171](../../tests/test_web_agent.py#L1171) | 1171 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001172](../../tests/test_web_agent.py#L1172) | 1172 | `"            \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-F725E90B2A-L001173](../../tests/test_web_agent.py#L1173) | 1173 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001174](../../tests/test_web_agent.py#L1174) | 1174 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L001175](../../tests/test_web_agent.py#L1175) | 1175 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001176](../../tests/test_web_agent.py#L1176) | 1176 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L001177](../../tests/test_web_agent.py#L1177) | 1177 | `"        }"` | — |
| [SRC-F725E90B2A-L001178](../../tests/test_web_agent.py#L1178) | 1178 | `""` | — |
| [SRC-F725E90B2A-L001179](../../tests/test_web_agent.py#L1179) | 1179 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001180](../../tests/test_web_agent.py#L1180) | 1180 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L001181](../../tests/test_web_agent.py#L1181) | 1181 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L001182](../../tests/test_web_agent.py#L1182) | 1182 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001183](../../tests/test_web_agent.py#L1183) | 1183 | `"        agent, \"_generate\", lambda *args, **kwargs: \"إجابة مبدئية [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L001184](../../tests/test_web_agent.py#L1184) | 1184 | `"    )"` | — |
| [SRC-F725E90B2A-L001185](../../tests/test_web_agent.py#L1185) | 1185 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001186](../../tests/test_web_agent.py#L1186) | 1186 | `"        agent,"` | — |
| [SRC-F725E90B2A-L001187](../../tests/test_web_agent.py#L1187) | 1187 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L001188](../../tests/test_web_agent.py#L1188) | 1188 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-F725E90B2A-L001189](../../tests/test_web_agent.py#L1189) | 1189 | `"            \"Audit Report: ملاحظة داخلية سرية\\\\n\""` | — |
| [SRC-F725E90B2A-L001190](../../tests/test_web_agent.py#L1190) | 1190 | `"            \"Final answer: إجابة نهائية مزعومة\""` | — |
| [SRC-F725E90B2A-L001191](../../tests/test_web_agent.py#L1191) | 1191 | `"        ),"` | — |
| [SRC-F725E90B2A-L001192](../../tests/test_web_agent.py#L1192) | 1192 | `"    )"` | — |
| [SRC-F725E90B2A-L001193](../../tests/test_web_agent.py#L1193) | 1193 | `""` | — |
| [SRC-F725E90B2A-L001194](../../tests/test_web_agent.py#L1194) | 1194 | `"    result = agent.answer(\"قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية\")"` | — |
| [SRC-F725E90B2A-L001195](../../tests/test_web_agent.py#L1195) | 1195 | `""` | — |
| [SRC-F725E90B2A-L001196](../../tests/test_web_agent.py#L1196) | 1196 | `"    assert result[\"search_report\"][\"second_pass_review\"] == \"model_claim_audit_unavailable\""` | — |
| [SRC-F725E90B2A-L001197](../../tests/test_web_agent.py#L1197) | 1197 | `"    assert result[\"final_answer_status\"] == \"review_failed_with_source_fallback\""` | — |
| [SRC-F725E90B2A-L001198](../../tests/test_web_agent.py#L1198) | 1198 | `"    assert \"Audit Report\" not in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L001199](../../tests/test_web_agent.py#L1199) | 1199 | `"    assert \"ملاحظة داخلية سرية\" not in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L001200](../../tests/test_web_agent.py#L1200) | 1200 | `"    assert \"إجابة نهائية مزعومة\" not in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L001201](../../tests/test_web_agent.py#L1201) | 1201 | `""` | — |
| [SRC-F725E90B2A-L001202](../../tests/test_web_agent.py#L1202) | 1202 | `""` | — |
| [SRC-F725E90B2A-L001203](../../tests/test_web_agent.py#L1203) | 1203 | `"def test_sibling_subdomains_do_not_satisfy_independent_evidence_gate(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001204](../../tests/test_web_agent.py#L1204) | 1204 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001205](../../tests/test_web_agent.py#L1205) | 1205 | `"    first = sample_source(0)"` | — |
| [SRC-F725E90B2A-L001206](../../tests/test_web_agent.py#L1206) | 1206 | `"    first[\"url\"] = \"https://news.example.com/research\""` | — |
| [SRC-F725E90B2A-L001207](../../tests/test_web_agent.py#L1207) | 1207 | `"    first[\"domain\"] = \"news.example.com\""` | — |
| [SRC-F725E90B2A-L001208](../../tests/test_web_agent.py#L1208) | 1208 | `"    second = sample_source(1)"` | — |
| [SRC-F725E90B2A-L001209](../../tests/test_web_agent.py#L1209) | 1209 | `"    second[\"url\"] = \"https://offers.example.com/research\""` | — |
| [SRC-F725E90B2A-L001210](../../tests/test_web_agent.py#L1210) | 1210 | `"    second[\"domain\"] = \"offers.example.com\""` | — |
| [SRC-F725E90B2A-L001211](../../tests/test_web_agent.py#L1211) | 1211 | `""` | — |
| [SRC-F725E90B2A-L001212](../../tests/test_web_agent.py#L1212) | 1212 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001213](../../tests/test_web_agent.py#L1213) | 1213 | `"        agent,"` | — |
| [SRC-F725E90B2A-L001214](../../tests/test_web_agent.py#L1214) | 1214 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L001215](../../tests/test_web_agent.py#L1215) | 1215 | `"        lambda plan: ("` | — |
| [SRC-F725E90B2A-L001216](../../tests/test_web_agent.py#L1216) | 1216 | `"            [first, second],"` | — |
| [SRC-F725E90B2A-L001217](../../tests/test_web_agent.py#L1217) | 1217 | `"            [],"` | — |
| [SRC-F725E90B2A-L001218](../../tests/test_web_agent.py#L1218) | 1218 | `"            {"` | — |
| [SRC-F725E90B2A-L001219](../../tests/test_web_agent.py#L1219) | 1219 | `"                \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L001220](../../tests/test_web_agent.py#L1220) | 1220 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001221](../../tests/test_web_agent.py#L1221) | 1221 | `"                \"query_results\": [{\"query\": \"قارن هذه التقنية\", \"results\": 2}],"` | — |
| [SRC-F725E90B2A-L001222](../../tests/test_web_agent.py#L1222) | 1222 | `"                \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L001223](../../tests/test_web_agent.py#L1223) | 1223 | `"                \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L001224](../../tests/test_web_agent.py#L1224) | 1224 | `"                \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001225](../../tests/test_web_agent.py#L1225) | 1225 | `"                \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-F725E90B2A-L001226](../../tests/test_web_agent.py#L1226) | 1226 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001227](../../tests/test_web_agent.py#L1227) | 1227 | `"                \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001228](../../tests/test_web_agent.py#L1228) | 1228 | `"                \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001229](../../tests/test_web_agent.py#L1229) | 1229 | `"            },"` | — |
| [SRC-F725E90B2A-L001230](../../tests/test_web_agent.py#L1230) | 1230 | `"        ),"` | — |
| [SRC-F725E90B2A-L001231](../../tests/test_web_agent.py#L1231) | 1231 | `"    )"` | — |
| [SRC-F725E90B2A-L001232](../../tests/test_web_agent.py#L1232) | 1232 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001233](../../tests/test_web_agent.py#L1233) | 1233 | `"        agent, \"_generate\","` | — |
| [SRC-F725E90B2A-L001234](../../tests/test_web_agent.py#L1234) | 1234 | `"        lambda *args, **kwargs: pytest.fail("` | — |
| [SRC-F725E90B2A-L001235](../../tests/test_web_agent.py#L1235) | 1235 | `"            \"LLM must not answer when both sources belong to one registrable domain\""` | — |
| [SRC-F725E90B2A-L001236](../../tests/test_web_agent.py#L1236) | 1236 | `"        ),"` | — |
| [SRC-F725E90B2A-L001237](../../tests/test_web_agent.py#L1237) | 1237 | `"    )"` | — |
| [SRC-F725E90B2A-L001238](../../tests/test_web_agent.py#L1238) | 1238 | `""` | — |
| [SRC-F725E90B2A-L001239](../../tests/test_web_agent.py#L1239) | 1239 | `"    result = agent.answer(\"قارن هذه التقنية\")"` | — |
| [SRC-F725E90B2A-L001240](../../tests/test_web_agent.py#L1240) | 1240 | `""` | — |
| [SRC-F725E90B2A-L001241](../../tests/test_web_agent.py#L1241) | 1241 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L001242](../../tests/test_web_agent.py#L1242) | 1242 | `"    assert result[\"search_report\"][\"independent_sources\"] == 1"` | — |
| [SRC-F725E90B2A-L001243](../../tests/test_web_agent.py#L1243) | 1243 | `"    assert result[\"search_report\"][\"unique_sources\"] == 2"` | — |
| [SRC-F725E90B2A-L001244](../../tests/test_web_agent.py#L1244) | 1244 | `""` | — |
| [SRC-F725E90B2A-L001245](../../tests/test_web_agent.py#L1245) | 1245 | `""` | — |
| [SRC-F725E90B2A-L001246](../../tests/test_web_agent.py#L1246) | 1246 | `"def test_bounded_evidence_repair_recovers_with_one_relevant_independent_source(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001247](../../tests/test_web_agent.py#L1247) | 1247 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001248](../../tests/test_web_agent.py#L1248) | 1248 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L001249](../../tests/test_web_agent.py#L1249) | 1249 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001250](../../tests/test_web_agent.py#L1250) | 1250 | `"        \"queries\": [\"شركة ألفا التقنية معلومات\"],"` | — |
| [SRC-F725E90B2A-L001251](../../tests/test_web_agent.py#L1251) | 1251 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L001252](../../tests/test_web_agent.py#L1252) | 1252 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001253](../../tests/test_web_agent.py#L1253) | 1253 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L001254](../../tests/test_web_agent.py#L1254) | 1254 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001255](../../tests/test_web_agent.py#L1255) | 1255 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001256](../../tests/test_web_agent.py#L1256) | 1256 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001257](../../tests/test_web_agent.py#L1257) | 1257 | `"    }"` | — |
| [SRC-F725E90B2A-L001258](../../tests/test_web_agent.py#L1258) | 1258 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L001259](../../tests/test_web_agent.py#L1259) | 1259 | `"    matched_queries = []"` | — |
| [SRC-F725E90B2A-L001260](../../tests/test_web_agent.py#L1260) | 1260 | `"    question = ("` | — |
| [SRC-F725E90B2A-L001261](../../tests/test_web_agent.py#L1261) | 1261 | `"        \"ما أحدث معلومات شركة ألفا التقنية اليوم؟ \""` | — |
| [SRC-F725E90B2A-L001262](../../tests/test_web_agent.py#L1262) | 1262 | `"        \"اذكر مصادر موثوقة، وروابط مباشرة، وأجب بإيجاز.\""` | — |
| [SRC-F725E90B2A-L001263](../../tests/test_web_agent.py#L1263) | 1263 | `"    )"` | — |
| [SRC-F725E90B2A-L001264](../../tests/test_web_agent.py#L1264) | 1264 | `""` | — |
| [SRC-F725E90B2A-L001265](../../tests/test_web_agent.py#L1265) | 1265 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L001266](../../tests/test_web_agent.py#L1266) | 1266 | `"        calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L001267](../../tests/test_web_agent.py#L1267) | 1267 | `"        sources = [sample_source(0)] if len(calls) == 1 else [sample_source(1)]"` | — |
| [SRC-F725E90B2A-L001268](../../tests/test_web_agent.py#L1268) | 1268 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L001269](../../tests/test_web_agent.py#L1269) | 1269 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L001270](../../tests/test_web_agent.py#L1270) | 1270 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001271](../../tests/test_web_agent.py#L1271) | 1271 | `"            \"query_results\": [{\"query\": research_plan[\"queries\"][0], \"results\": len(sources)}],"` | — |
| [SRC-F725E90B2A-L001272](../../tests/test_web_agent.py#L1272) | 1272 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-F725E90B2A-L001273](../../tests/test_web_agent.py#L1273) | 1273 | `"            \"pages_fetched\": len(sources),"` | — |
| [SRC-F725E90B2A-L001274](../../tests/test_web_agent.py#L1274) | 1274 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001275](../../tests/test_web_agent.py#L1275) | 1275 | `"            \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-F725E90B2A-L001276](../../tests/test_web_agent.py#L1276) | 1276 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001277](../../tests/test_web_agent.py#L1277) | 1277 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L001278](../../tests/test_web_agent.py#L1278) | 1278 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001279](../../tests/test_web_agent.py#L1279) | 1279 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L001280](../../tests/test_web_agent.py#L1280) | 1280 | `"        }"` | — |
| [SRC-F725E90B2A-L001281](../../tests/test_web_agent.py#L1281) | 1281 | `""` | — |
| [SRC-F725E90B2A-L001282](../../tests/test_web_agent.py#L1282) | 1282 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001283](../../tests/test_web_agent.py#L1283) | 1283 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
