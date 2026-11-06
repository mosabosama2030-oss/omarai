# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **043**
- سجلات الأسطر: **800**
- النطاق: SRC-3451CC474D-L000509 إلى SRC-3451CC474D-L001308
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-3451CC474D — [tests/test_api.py](../../tests/test_api.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3451CC474D-L000509](../../tests/test_api.py#L509) | 509 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"x\" * 48)"` | — |
| [SRC-3451CC474D-L000510](../../tests/test_api.py#L510) | 510 | `""` | — |
| [SRC-3451CC474D-L000511](../../tests/test_api.py#L511) | 511 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000512](../../tests/test_api.py#L512) | 512 | `"        local_api, \"/api/analyze\", method=\"POST\", payload={\"text\": \"test\"}"` | — |
| [SRC-3451CC474D-L000513](../../tests/test_api.py#L513) | 513 | `"    )"` | — |
| [SRC-3451CC474D-L000514](../../tests/test_api.py#L514) | 514 | `"    assert status == 401"` | — |
| [SRC-3451CC474D-L000515](../../tests/test_api.py#L515) | 515 | `"    assert \"رمز الوصول\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000516](../../tests/test_api.py#L516) | 516 | `""` | — |
| [SRC-3451CC474D-L000517](../../tests/test_api.py#L517) | 517 | `"    status, error = request_json(local_api, \"/api/leads\")"` | — |
| [SRC-3451CC474D-L000518](../../tests/test_api.py#L518) | 518 | `"    assert status == 401"` | — |
| [SRC-3451CC474D-L000519](../../tests/test_api.py#L519) | 519 | `""` | — |
| [SRC-3451CC474D-L000520](../../tests/test_api.py#L520) | 520 | `"    headers = {\"Authorization\": \"Bearer \" + \"x\" * 48}"` | — |
| [SRC-3451CC474D-L000521](../../tests/test_api.py#L521) | 521 | `"    status, result = request_json("` | — |
| [SRC-3451CC474D-L000522](../../tests/test_api.py#L522) | 522 | `"        local_api, \"/api/analyze\", method=\"POST\", payload={\"text\": \"بدور على شقة\"}, headers=headers"` | — |
| [SRC-3451CC474D-L000523](../../tests/test_api.py#L523) | 523 | `"    )"` | — |
| [SRC-3451CC474D-L000524](../../tests/test_api.py#L524) | 524 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000525](../../tests/test_api.py#L525) | 525 | `"    assert \"score\" in result"` | — |
| [SRC-3451CC474D-L000526](../../tests/test_api.py#L526) | 526 | `""` | — |
| [SRC-3451CC474D-L000527](../../tests/test_api.py#L527) | 527 | `"    status, result = request_json(local_api, \"/api/leads\", headers=headers)"` | — |
| [SRC-3451CC474D-L000528](../../tests/test_api.py#L528) | 528 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000529](../../tests/test_api.py#L529) | 529 | `"    assert result[\"count\"] == 0"` | — |
| [SRC-3451CC474D-L000530](../../tests/test_api.py#L530) | 530 | `""` | — |
| [SRC-3451CC474D-L000531](../../tests/test_api.py#L531) | 531 | `""` | — |
| [SRC-3451CC474D-L000532](../../tests/test_api.py#L532) | 532 | `"def test_hosted_api_rate_limits_authenticated_requests(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000533](../../tests/test_api.py#L533) | 533 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000534](../../tests/test_api.py#L534) | 534 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"y\" * 48)"` | — |
| [SRC-3451CC474D-L000535](../../tests/test_api.py#L535) | 535 | `"    monkeypatch.setattr(Handler, \"RATE_LIMIT_REQUESTS\", 1)"` | — |
| [SRC-3451CC474D-L000536](../../tests/test_api.py#L536) | 536 | `"    with Handler._rate_lock:"` | — |
| [SRC-3451CC474D-L000537](../../tests/test_api.py#L537) | 537 | `"        Handler._request_times.clear()"` | — |
| [SRC-3451CC474D-L000538](../../tests/test_api.py#L538) | 538 | `"    headers = {\"Authorization\": \"Bearer \" + \"y\" * 48}"` | — |
| [SRC-3451CC474D-L000539](../../tests/test_api.py#L539) | 539 | `""` | — |
| [SRC-3451CC474D-L000540](../../tests/test_api.py#L540) | 540 | `"    status, _ = request_json("` | — |
| [SRC-3451CC474D-L000541](../../tests/test_api.py#L541) | 541 | `"        local_api, \"/api/analyze\", method=\"POST\", payload={\"text\": \"first\"}, headers=headers"` | — |
| [SRC-3451CC474D-L000542](../../tests/test_api.py#L542) | 542 | `"    )"` | — |
| [SRC-3451CC474D-L000543](../../tests/test_api.py#L543) | 543 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000544](../../tests/test_api.py#L544) | 544 | `""` | — |
| [SRC-3451CC474D-L000545](../../tests/test_api.py#L545) | 545 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000546](../../tests/test_api.py#L546) | 546 | `"        local_api, \"/api/analyze\", method=\"POST\", payload={\"text\": \"second\"}, headers=headers"` | — |
| [SRC-3451CC474D-L000547](../../tests/test_api.py#L547) | 547 | `"    )"` | — |
| [SRC-3451CC474D-L000548](../../tests/test_api.py#L548) | 548 | `"    assert status == 429"` | — |
| [SRC-3451CC474D-L000549](../../tests/test_api.py#L549) | 549 | `"    assert \"حد الطلبات\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000550](../../tests/test_api.py#L550) | 550 | `""` | — |
| [SRC-3451CC474D-L000551](../../tests/test_api.py#L551) | 551 | `""` | — |
| [SRC-3451CC474D-L000552](../../tests/test_api.py#L552) | 552 | `""` | — |
| [SRC-3451CC474D-L000553](../../tests/test_api.py#L553) | 553 | `"def test_public_binding_requires_explicit_deployment_flag_and_strong_token(monkeypatch):"` | — |
| [SRC-3451CC474D-L000554](../../tests/test_api.py#L554) | 554 | `"    from api.omarai import serve"` | — |
| [SRC-3451CC474D-L000555](../../tests/test_api.py#L555) | 555 | `""` | — |
| [SRC-3451CC474D-L000556](../../tests/test_api.py#L556) | 556 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000557](../../tests/test_api.py#L557) | 557 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000558](../../tests/test_api.py#L558) | 558 | `"    with pytest.raises(ValueError, match=\"Public binding requires\"):"` | — |
| [SRC-3451CC474D-L000559](../../tests/test_api.py#L559) | 559 | `"        serve(\"0.0.0.0\", 0)"` | — |
| [SRC-3451CC474D-L000560](../../tests/test_api.py#L560) | 560 | `""` | — |
| [SRC-3451CC474D-L000561](../../tests/test_api.py#L561) | 561 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000562](../../tests/test_api.py#L562) | 562 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"short\")"` | — |
| [SRC-3451CC474D-L000563](../../tests/test_api.py#L563) | 563 | `"    with pytest.raises(ValueError, match=\"at least 32 characters\"):"` | — |
| [SRC-3451CC474D-L000564](../../tests/test_api.py#L564) | 564 | `"        serve(\"0.0.0.0\", 0)"` | — |
| [SRC-3451CC474D-L000565](../../tests/test_api.py#L565) | 565 | `""` | — |
| [SRC-3451CC474D-L000566](../../tests/test_api.py#L566) | 566 | `"def test_rate_limiter_prunes_expired_client_buckets(monkeypatch):"` | — |
| [SRC-3451CC474D-L000567](../../tests/test_api.py#L567) | 567 | `"    \"\"\"Client IPs do not accumulate forever after their 60-second window expires.\"\"\""` | — |
| [SRC-3451CC474D-L000568](../../tests/test_api.py#L568) | 568 | `"    monkeypatch.delenv(\"OMARAI_TRUST_PROXY_HEADERS\", raising=False)"` | — |
| [SRC-3451CC474D-L000569](../../tests/test_api.py#L569) | 569 | `"    monkeypatch.setattr(Handler, \"_request_times\", defaultdict(deque))"` | — |
| [SRC-3451CC474D-L000570](../../tests/test_api.py#L570) | 570 | `"    monkeypatch.setattr(Handler, \"_rate_last_cleanup\", 0.0)"` | — |
| [SRC-3451CC474D-L000571](../../tests/test_api.py#L571) | 571 | `"    clock = {\"now\": 100.0}"` | — |
| [SRC-3451CC474D-L000572](../../tests/test_api.py#L572) | 572 | `"    monkeypatch.setattr(\"api.omarai.time.monotonic\", lambda: clock[\"now\"])"` | — |
| [SRC-3451CC474D-L000573](../../tests/test_api.py#L573) | 573 | `""` | — |
| [SRC-3451CC474D-L000574](../../tests/test_api.py#L574) | 574 | `"    class FakeHandler(Handler):"` | — |
| [SRC-3451CC474D-L000575](../../tests/test_api.py#L575) | 575 | `"        def __init__(self, ip):"` | — |
| [SRC-3451CC474D-L000576](../../tests/test_api.py#L576) | 576 | `"            self.headers = {}"` | — |
| [SRC-3451CC474D-L000577](../../tests/test_api.py#L577) | 577 | `"            self.client_address = (ip, 1234)"` | — |
| [SRC-3451CC474D-L000578](../../tests/test_api.py#L578) | 578 | `""` | — |
| [SRC-3451CC474D-L000579](../../tests/test_api.py#L579) | 579 | `"    first = FakeHandler(\"192.0.2.1\")"` | — |
| [SRC-3451CC474D-L000580](../../tests/test_api.py#L580) | 580 | `"    second = FakeHandler(\"192.0.2.2\")"` | — |
| [SRC-3451CC474D-L000581](../../tests/test_api.py#L581) | 581 | `"    assert first._rate_limit_ok() is True"` | — |
| [SRC-3451CC474D-L000582](../../tests/test_api.py#L582) | 582 | `"    assert \"192.0.2.1\" in Handler._request_times"` | — |
| [SRC-3451CC474D-L000583](../../tests/test_api.py#L583) | 583 | `""` | — |
| [SRC-3451CC474D-L000584](../../tests/test_api.py#L584) | 584 | `"    clock[\"now\"] = 161.0"` | — |
| [SRC-3451CC474D-L000585](../../tests/test_api.py#L585) | 585 | `"    assert second._rate_limit_ok() is True"` | — |
| [SRC-3451CC474D-L000586](../../tests/test_api.py#L586) | 586 | `"    assert \"192.0.2.1\" not in Handler._request_times"` | — |
| [SRC-3451CC474D-L000587](../../tests/test_api.py#L587) | 587 | `"    assert \"192.0.2.2\" in Handler._request_times"` | — |
| [SRC-3451CC474D-L000588](../../tests/test_api.py#L588) | 588 | `""` | — |
| [SRC-3451CC474D-L000589](../../tests/test_api.py#L589) | 589 | `""` | — |
| [SRC-3451CC474D-L000590](../../tests/test_api.py#L590) | 590 | `""` | — |
| [SRC-3451CC474D-L000591](../../tests/test_api.py#L591) | 591 | `"def test_agent_concurrency_cap_rejects_work_when_all_slots_are_busy(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000592](../../tests/test_api.py#L592) | 592 | `"    from api.omarai import WebAgent"` | — |
| [SRC-3451CC474D-L000593](../../tests/test_api.py#L593) | 593 | `""` | — |
| [SRC-3451CC474D-L000594](../../tests/test_api.py#L594) | 594 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000595](../../tests/test_api.py#L595) | 595 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000596](../../tests/test_api.py#L596) | 596 | `"    monkeypatch.setattr(Handler, \"_request_times\", defaultdict(deque))"` | — |
| [SRC-3451CC474D-L000597](../../tests/test_api.py#L597) | 597 | `"    monkeypatch.setattr(Handler, \"_rate_last_cleanup\", 0.0)"` | — |
| [SRC-3451CC474D-L000598](../../tests/test_api.py#L598) | 598 | `"    monkeypatch.setattr(Handler, \"_agent_semaphore\", threading.BoundedSemaphore(1))"` | — |
| [SRC-3451CC474D-L000599](../../tests/test_api.py#L599) | 599 | `""` | — |
| [SRC-3451CC474D-L000600](../../tests/test_api.py#L600) | 600 | `"    entered = threading.Event()"` | — |
| [SRC-3451CC474D-L000601](../../tests/test_api.py#L601) | 601 | `"    release = threading.Event()"` | — |
| [SRC-3451CC474D-L000602](../../tests/test_api.py#L602) | 602 | `"    first_result = {}"` | — |
| [SRC-3451CC474D-L000603](../../tests/test_api.py#L603) | 603 | `""` | — |
| [SRC-3451CC474D-L000604](../../tests/test_api.py#L604) | 604 | `"    def slow_answer(self, question, history=None, mode=\"auto\", *, budget_profile=\"default\"):"` | — |
| [SRC-3451CC474D-L000605](../../tests/test_api.py#L605) | 605 | `"        entered.set()"` | — |
| [SRC-3451CC474D-L000606](../../tests/test_api.py#L606) | 606 | `"        assert release.wait(timeout=2), \"test did not release the held research slot\""` | — |
| [SRC-3451CC474D-L000607](../../tests/test_api.py#L607) | 607 | `"        return {"` | — |
| [SRC-3451CC474D-L000608](../../tests/test_api.py#L608) | 608 | `"            \"answer\": \"نتيجة اختبار محدودة\","` | — |
| [SRC-3451CC474D-L000609](../../tests/test_api.py#L609) | 609 | `"            \"question\": question,"` | — |
| [SRC-3451CC474D-L000610](../../tests/test_api.py#L610) | 610 | `"            \"search_query\": question,"` | — |
| [SRC-3451CC474D-L000611](../../tests/test_api.py#L611) | 611 | `"            \"search_queries\": [],"` | — |
| [SRC-3451CC474D-L000612](../../tests/test_api.py#L612) | 612 | `"            \"search_report\": {\"search_attempted\": False, \"search_outcome\": \"not_attempted\"},"` | — |
| [SRC-3451CC474D-L000613](../../tests/test_api.py#L613) | 613 | `"            \"sources\": [],"` | — |
| [SRC-3451CC474D-L000614](../../tests/test_api.py#L614) | 614 | `"            \"used_language_model\": False,"` | — |
| [SRC-3451CC474D-L000615](../../tests/test_api.py#L615) | 615 | `"            \"used_web_search\": False,"` | — |
| [SRC-3451CC474D-L000616](../../tests/test_api.py#L616) | 616 | `"            \"search_attempted\": False,"` | — |
| [SRC-3451CC474D-L000617](../../tests/test_api.py#L617) | 617 | `"            \"used_social_search\": False,"` | — |
| [SRC-3451CC474D-L000618](../../tests/test_api.py#L618) | 618 | `"            \"warnings\": [],"` | — |
| [SRC-3451CC474D-L000619](../../tests/test_api.py#L619) | 619 | `"            \"kind\": \"web_fallback\","` | — |
| [SRC-3451CC474D-L000620](../../tests/test_api.py#L620) | 620 | `"        }"` | — |
| [SRC-3451CC474D-L000621](../../tests/test_api.py#L621) | 621 | `""` | — |
| [SRC-3451CC474D-L000622](../../tests/test_api.py#L622) | 622 | `"    monkeypatch.setattr(WebAgent, \"answer\", slow_answer)"` | — |
| [SRC-3451CC474D-L000623](../../tests/test_api.py#L623) | 623 | `""` | — |
| [SRC-3451CC474D-L000624](../../tests/test_api.py#L624) | 624 | `"    def first_request():"` | — |
| [SRC-3451CC474D-L000625](../../tests/test_api.py#L625) | 625 | `"        first_result[\"response\"] = request_json("` | — |
| [SRC-3451CC474D-L000626](../../tests/test_api.py#L626) | 626 | `"            local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"السؤال الأول\"}"` | — |
| [SRC-3451CC474D-L000627](../../tests/test_api.py#L627) | 627 | `"        )"` | — |
| [SRC-3451CC474D-L000628](../../tests/test_api.py#L628) | 628 | `""` | — |
| [SRC-3451CC474D-L000629](../../tests/test_api.py#L629) | 629 | `"    worker = threading.Thread(target=first_request, daemon=True)"` | — |
| [SRC-3451CC474D-L000630](../../tests/test_api.py#L630) | 630 | `"    worker.start()"` | — |
| [SRC-3451CC474D-L000631](../../tests/test_api.py#L631) | 631 | `"    try:"` | — |
| [SRC-3451CC474D-L000632](../../tests/test_api.py#L632) | 632 | `"        assert entered.wait(timeout=1), \"first request did not acquire the research slot\""` | — |
| [SRC-3451CC474D-L000633](../../tests/test_api.py#L633) | 633 | `"        status, payload = request_json("` | — |
| [SRC-3451CC474D-L000634](../../tests/test_api.py#L634) | 634 | `"            local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"السؤال الثاني\"}"` | — |
| [SRC-3451CC474D-L000635](../../tests/test_api.py#L635) | 635 | `"        )"` | — |
| [SRC-3451CC474D-L000636](../../tests/test_api.py#L636) | 636 | `"        assert status == 503"` | — |
| [SRC-3451CC474D-L000637](../../tests/test_api.py#L637) | 637 | `"        assert payload[\"retry_after_seconds\"] == 5"` | — |
| [SRC-3451CC474D-L000638](../../tests/test_api.py#L638) | 638 | `"        assert \"مشغولة\" in payload[\"error\"]"` | — |
| [SRC-3451CC474D-L000639](../../tests/test_api.py#L639) | 639 | `"    finally:"` | — |
| [SRC-3451CC474D-L000640](../../tests/test_api.py#L640) | 640 | `"        release.set()"` | — |
| [SRC-3451CC474D-L000641](../../tests/test_api.py#L641) | 641 | `"        worker.join(timeout=3)"` | — |
| [SRC-3451CC474D-L000642](../../tests/test_api.py#L642) | 642 | `""` | — |
| [SRC-3451CC474D-L000643](../../tests/test_api.py#L643) | 643 | `"    assert not worker.is_alive()"` | — |
| [SRC-3451CC474D-L000644](../../tests/test_api.py#L644) | 644 | `"    assert first_result[\"response\"][0] == 200"` | — |
| [SRC-3451CC474D-L000645](../../tests/test_api.py#L645) | 645 | `""` | — |
| [SRC-3451CC474D-L000646](../../tests/test_api.py#L646) | 646 | `""` | — |
| [SRC-3451CC474D-L000647](../../tests/test_api.py#L647) | 647 | `"def test_agent_concurrency_limit_has_hard_bounds(monkeypatch):"` | — |
| [SRC-3451CC474D-L000648](../../tests/test_api.py#L648) | 648 | `"    from api.omarai import _configured_agent_concurrency_limit"` | — |
| [SRC-3451CC474D-L000649](../../tests/test_api.py#L649) | 649 | `""` | — |
| [SRC-3451CC474D-L000650](../../tests/test_api.py#L650) | 650 | `"    monkeypatch.setenv(\"OMARAI_MAX_CONCURRENT_AGENT_REQUESTS\", \"99\")"` | — |
| [SRC-3451CC474D-L000651](../../tests/test_api.py#L651) | 651 | `"    assert _configured_agent_concurrency_limit() == 8"` | — |
| [SRC-3451CC474D-L000652](../../tests/test_api.py#L652) | 652 | `"    monkeypatch.setenv(\"OMARAI_MAX_CONCURRENT_AGENT_REQUESTS\", \"invalid\")"` | — |
| [SRC-3451CC474D-L000653](../../tests/test_api.py#L653) | 653 | `"    assert _configured_agent_concurrency_limit() == 4"` | — |
| [SRC-3451CC474D-L000654](../../tests/test_api.py#L654) | 654 | `""` | — |
| [SRC-3451CC474D-L000655](../../tests/test_api.py#L655) | 655 | `""` | — |
| [SRC-3451CC474D-L000656](../../tests/test_api.py#L656) | 656 | `"def test_api_rejects_oversized_request_body(local_api):"` | — |
| [SRC-3451CC474D-L000657](../../tests/test_api.py#L657) | 657 | `"    status, payload = request_json("` | — |
| [SRC-3451CC474D-L000658](../../tests/test_api.py#L658) | 658 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000659](../../tests/test_api.py#L659) | 659 | `"        \"/api/analyze\","` | — |
| [SRC-3451CC474D-L000660](../../tests/test_api.py#L660) | 660 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000661](../../tests/test_api.py#L661) | 661 | `"        payload={\"text\": \"x\" * 200_001},"` | — |
| [SRC-3451CC474D-L000662](../../tests/test_api.py#L662) | 662 | `"    )"` | — |
| [SRC-3451CC474D-L000663](../../tests/test_api.py#L663) | 663 | `""` | — |
| [SRC-3451CC474D-L000664](../../tests/test_api.py#L664) | 664 | `"    assert status == 413"` | — |
| [SRC-3451CC474D-L000665](../../tests/test_api.py#L665) | 665 | `"    assert payload[\"error\"] == \"request too large\""` | — |
| [SRC-3451CC474D-L000666](../../tests/test_api.py#L666) | 666 | `""` | — |
| [SRC-3451CC474D-L000667](../../tests/test_api.py#L667) | 667 | `""` | — |
| [SRC-3451CC474D-L000668](../../tests/test_api.py#L668) | 668 | `"def test_api_rejects_malformed_content_length(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000669](../../tests/test_api.py#L669) | 669 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000670](../../tests/test_api.py#L670) | 670 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000671](../../tests/test_api.py#L671) | 671 | `"    host_port = local_api.rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000672](../../tests/test_api.py#L672) | 672 | `"    with socket.create_connection((host_port[0].removeprefix(\"http://\"), int(host_port[1])), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000673](../../tests/test_api.py#L673) | 673 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000674](../../tests/test_api.py#L674) | 674 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000675](../../tests/test_api.py#L675) | 675 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000676](../../tests/test_api.py#L676) | 676 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000677](../../tests/test_api.py#L677) | 677 | `"            b\"Content-Length: invalid\\r\\n\""` | — |
| [SRC-3451CC474D-L000678](../../tests/test_api.py#L678) | 678 | `"            b\"Connection: close\\r\\n\\r\\n\""` | — |
| [SRC-3451CC474D-L000679](../../tests/test_api.py#L679) | 679 | `"        )"` | — |
| [SRC-3451CC474D-L000680](../../tests/test_api.py#L680) | 680 | `"        response = b\"\""` | — |
| [SRC-3451CC474D-L000681](../../tests/test_api.py#L681) | 681 | `"        while True:"` | — |
| [SRC-3451CC474D-L000682](../../tests/test_api.py#L682) | 682 | `"            chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000683](../../tests/test_api.py#L683) | 683 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000684](../../tests/test_api.py#L684) | 684 | `"                break"` | — |
| [SRC-3451CC474D-L000685](../../tests/test_api.py#L685) | 685 | `"            response += chunk"` | — |
| [SRC-3451CC474D-L000686](../../tests/test_api.py#L686) | 686 | `""` | — |
| [SRC-3451CC474D-L000687](../../tests/test_api.py#L687) | 687 | `"    assert response.startswith(b\"HTTP/1.0 400\")"` | — |
| [SRC-3451CC474D-L000688](../../tests/test_api.py#L688) | 688 | `"    assert b\"valid Content-Length is required\" in response"` | — |
| [SRC-3451CC474D-L000689](../../tests/test_api.py#L689) | 689 | `""` | — |
| [SRC-3451CC474D-L000690](../../tests/test_api.py#L690) | 690 | `""` | — |
| [SRC-3451CC474D-L000691](../../tests/test_api.py#L691) | 691 | `"def test_api_returns_408_when_request_body_read_times_out(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000692](../../tests/test_api.py#L692) | 692 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000693](../../tests/test_api.py#L693) | 693 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000694](../../tests/test_api.py#L694) | 694 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_BODY_READ_TIMEOUT_SECONDS\", 0.1)"` | — |
| [SRC-3451CC474D-L000695](../../tests/test_api.py#L695) | 695 | `"    host_port = local_api.rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000696](../../tests/test_api.py#L696) | 696 | `"    with socket.create_connection((host_port[0].removeprefix(\"http://\"), int(host_port[1])), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000697](../../tests/test_api.py#L697) | 697 | `"        client.settimeout(2)"` | — |
| [SRC-3451CC474D-L000698](../../tests/test_api.py#L698) | 698 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000699](../../tests/test_api.py#L699) | 699 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000700](../../tests/test_api.py#L700) | 700 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000701](../../tests/test_api.py#L701) | 701 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000702](../../tests/test_api.py#L702) | 702 | `"            b\"Content-Length: 40\\r\\n\""` | — |
| [SRC-3451CC474D-L000703](../../tests/test_api.py#L703) | 703 | `"            b\"Connection: close\\r\\n\\r\\n\""` | — |
| [SRC-3451CC474D-L000704](../../tests/test_api.py#L704) | 704 | `"            b\"{}\""` | — |
| [SRC-3451CC474D-L000705](../../tests/test_api.py#L705) | 705 | `"        )"` | — |
| [SRC-3451CC474D-L000706](../../tests/test_api.py#L706) | 706 | `"        response = b\"\""` | — |
| [SRC-3451CC474D-L000707](../../tests/test_api.py#L707) | 707 | `"        while True:"` | — |
| [SRC-3451CC474D-L000708](../../tests/test_api.py#L708) | 708 | `"            chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000709](../../tests/test_api.py#L709) | 709 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000710](../../tests/test_api.py#L710) | 710 | `"                break"` | — |
| [SRC-3451CC474D-L000711](../../tests/test_api.py#L711) | 711 | `"            response += chunk"` | — |
| [SRC-3451CC474D-L000712](../../tests/test_api.py#L712) | 712 | `""` | — |
| [SRC-3451CC474D-L000713](../../tests/test_api.py#L713) | 713 | `"    assert response.startswith(b\"HTTP/1.0 408\")"` | — |
| [SRC-3451CC474D-L000714](../../tests/test_api.py#L714) | 714 | `"    assert b\"request body read timed out\" in response"` | — |
| [SRC-3451CC474D-L000715](../../tests/test_api.py#L715) | 715 | `""` | — |
| [SRC-3451CC474D-L000716](../../tests/test_api.py#L716) | 716 | `""` | — |
| [SRC-3451CC474D-L000717](../../tests/test_api.py#L717) | 717 | `"def test_api_absolute_body_deadline_stops_slow_trickle(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000718](../../tests/test_api.py#L718) | 718 | `"    \"\"\"A client must not evade the total deadline by sending before each idle timeout.\"\"\""` | — |
| [SRC-3451CC474D-L000719](../../tests/test_api.py#L719) | 719 | `"    import time"` | — |
| [SRC-3451CC474D-L000720](../../tests/test_api.py#L720) | 720 | `""` | — |
| [SRC-3451CC474D-L000721](../../tests/test_api.py#L721) | 721 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000722](../../tests/test_api.py#L722) | 722 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000723](../../tests/test_api.py#L723) | 723 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_BODY_READ_TIMEOUT_SECONDS\", 0.45)"` | — |
| [SRC-3451CC474D-L000724](../../tests/test_api.py#L724) | 724 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_BODY_IDLE_TIMEOUT_SECONDS\", 0.20)"` | — |
| [SRC-3451CC474D-L000725](../../tests/test_api.py#L725) | 725 | `"    host, port = local_api.removeprefix(\"http://\").rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000726](../../tests/test_api.py#L726) | 726 | `""` | — |
| [SRC-3451CC474D-L000727](../../tests/test_api.py#L727) | 727 | `"    with socket.create_connection((host, int(port)), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000728](../../tests/test_api.py#L728) | 728 | `"        client.settimeout(2)"` | — |
| [SRC-3451CC474D-L000729](../../tests/test_api.py#L729) | 729 | `"        started = time.monotonic()"` | — |
| [SRC-3451CC474D-L000730](../../tests/test_api.py#L730) | 730 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000731](../../tests/test_api.py#L731) | 731 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000732](../../tests/test_api.py#L732) | 732 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000733](../../tests/test_api.py#L733) | 733 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000734](../../tests/test_api.py#L734) | 734 | `"            b\"Content-Length: 100\\r\\n\""` | — |
| [SRC-3451CC474D-L000735](../../tests/test_api.py#L735) | 735 | `"            b\"Connection: close\\r\\n\\r\\n\""` | — |
| [SRC-3451CC474D-L000736](../../tests/test_api.py#L736) | 736 | `"            b\"{\""` | — |
| [SRC-3451CC474D-L000737](../../tests/test_api.py#L737) | 737 | `"        )"` | — |
| [SRC-3451CC474D-L000738](../../tests/test_api.py#L738) | 738 | `"        # Each fragment arrives before the 0.20s idle timeout, but the complete"` | — |
| [SRC-3451CC474D-L000739](../../tests/test_api.py#L739) | 739 | `"        # request body never arrives before the 0.45s absolute deadline."` | — |
| [SRC-3451CC474D-L000740](../../tests/test_api.py#L740) | 740 | `"        for fragment in (b'\"', b\"text\", b'\"', b\":\"):"` | — |
| [SRC-3451CC474D-L000741](../../tests/test_api.py#L741) | 741 | `"            time.sleep(0.08)"` | — |
| [SRC-3451CC474D-L000742](../../tests/test_api.py#L742) | 742 | `"            try:"` | — |
| [SRC-3451CC474D-L000743](../../tests/test_api.py#L743) | 743 | `"                client.sendall(fragment)"` | — |
| [SRC-3451CC474D-L000744](../../tests/test_api.py#L744) | 744 | `"            except OSError:"` | — |
| [SRC-3451CC474D-L000745](../../tests/test_api.py#L745) | 745 | `"                break"` | — |
| [SRC-3451CC474D-L000746](../../tests/test_api.py#L746) | 746 | `""` | — |
| [SRC-3451CC474D-L000747](../../tests/test_api.py#L747) | 747 | `"        response = bytearray()"` | — |
| [SRC-3451CC474D-L000748](../../tests/test_api.py#L748) | 748 | `"        while True:"` | — |
| [SRC-3451CC474D-L000749](../../tests/test_api.py#L749) | 749 | `"            try:"` | — |
| [SRC-3451CC474D-L000750](../../tests/test_api.py#L750) | 750 | `"                chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000751](../../tests/test_api.py#L751) | 751 | `"            except TimeoutError:"` | — |
| [SRC-3451CC474D-L000752](../../tests/test_api.py#L752) | 752 | `"                break"` | — |
| [SRC-3451CC474D-L000753](../../tests/test_api.py#L753) | 753 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000754](../../tests/test_api.py#L754) | 754 | `"                break"` | — |
| [SRC-3451CC474D-L000755](../../tests/test_api.py#L755) | 755 | `"            response.extend(chunk)"` | — |
| [SRC-3451CC474D-L000756](../../tests/test_api.py#L756) | 756 | `""` | — |
| [SRC-3451CC474D-L000757](../../tests/test_api.py#L757) | 757 | `"    elapsed = time.monotonic() - started"` | — |
| [SRC-3451CC474D-L000758](../../tests/test_api.py#L758) | 758 | `"    assert response.startswith(b\"HTTP/1.0 408\")"` | — |
| [SRC-3451CC474D-L000759](../../tests/test_api.py#L759) | 759 | `"    assert b\"request body read timed out\" in response"` | — |
| [SRC-3451CC474D-L000760](../../tests/test_api.py#L760) | 760 | `"    assert elapsed < 1.5"` | — |
| [SRC-3451CC474D-L000761](../../tests/test_api.py#L761) | 761 | `""` | — |
| [SRC-3451CC474D-L000762](../../tests/test_api.py#L762) | 762 | `""` | — |
| [SRC-3451CC474D-L000763](../../tests/test_api.py#L763) | 763 | `""` | — |
| [SRC-3451CC474D-L000764](../../tests/test_api.py#L764) | 764 | `"def test_api_absolute_header_deadline_stops_slow_trickle(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000765](../../tests/test_api.py#L765) | 765 | `"    \"\"\"Header bytes arriving before idle timeout must not extend the total deadline.\"\"\""` | — |
| [SRC-3451CC474D-L000766](../../tests/test_api.py#L766) | 766 | `"    import time"` | — |
| [SRC-3451CC474D-L000767](../../tests/test_api.py#L767) | 767 | `""` | — |
| [SRC-3451CC474D-L000768](../../tests/test_api.py#L768) | 768 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000769](../../tests/test_api.py#L769) | 769 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000770](../../tests/test_api.py#L770) | 770 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_HEADER_READ_TIMEOUT_SECONDS\", 0.5)"` | — |
| [SRC-3451CC474D-L000771](../../tests/test_api.py#L771) | 771 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_HEADER_IDLE_TIMEOUT_SECONDS\", 0.35)"` | — |
| [SRC-3451CC474D-L000772](../../tests/test_api.py#L772) | 772 | `"    host, port = local_api.removeprefix(\"http://\").rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000773](../../tests/test_api.py#L773) | 773 | `""` | — |
| [SRC-3451CC474D-L000774](../../tests/test_api.py#L774) | 774 | `"    with socket.create_connection((host, int(port)), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000775](../../tests/test_api.py#L775) | 775 | `"        client.settimeout(1.2)"` | — |
| [SRC-3451CC474D-L000776](../../tests/test_api.py#L776) | 776 | `"        started = time.monotonic()"` | — |
| [SRC-3451CC474D-L000777](../../tests/test_api.py#L777) | 777 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000778](../../tests/test_api.py#L778) | 778 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000779](../../tests/test_api.py#L779) | 779 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000780](../../tests/test_api.py#L780) | 780 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000781](../../tests/test_api.py#L781) | 781 | `"            b\"Content-Length: 40\\r\\n\""` | — |
| [SRC-3451CC474D-L000782](../../tests/test_api.py#L782) | 782 | `"            b\"X-Slow: \""` | — |
| [SRC-3451CC474D-L000783](../../tests/test_api.py#L783) | 783 | `"        )"` | — |
| [SRC-3451CC474D-L000784](../../tests/test_api.py#L784) | 784 | `"        # Each tiny fragment is sent well before the 0.35s idle timeout. No"` | — |
| [SRC-3451CC474D-L000785](../../tests/test_api.py#L785) | 785 | `"        # newline completes X-Slow, so only an absolute header deadline can stop it."` | — |
| [SRC-3451CC474D-L000786](../../tests/test_api.py#L786) | 786 | `"        for fragment in (b\"a\", b\"b\", b\"c\", b\"d\", b\"e\", b\"f\", b\"g\", b\"h\", b\"i\"):"` | — |
| [SRC-3451CC474D-L000787](../../tests/test_api.py#L787) | 787 | `"            time.sleep(0.12)"` | — |
| [SRC-3451CC474D-L000788](../../tests/test_api.py#L788) | 788 | `"            try:"` | — |
| [SRC-3451CC474D-L000789](../../tests/test_api.py#L789) | 789 | `"                client.sendall(fragment)"` | — |
| [SRC-3451CC474D-L000790](../../tests/test_api.py#L790) | 790 | `"            except OSError:"` | — |
| [SRC-3451CC474D-L000791](../../tests/test_api.py#L791) | 791 | `"                break"` | — |
| [SRC-3451CC474D-L000792](../../tests/test_api.py#L792) | 792 | `""` | — |
| [SRC-3451CC474D-L000793](../../tests/test_api.py#L793) | 793 | `"        response = bytearray()"` | — |
| [SRC-3451CC474D-L000794](../../tests/test_api.py#L794) | 794 | `"        while True:"` | — |
| [SRC-3451CC474D-L000795](../../tests/test_api.py#L795) | 795 | `"            try:"` | — |
| [SRC-3451CC474D-L000796](../../tests/test_api.py#L796) | 796 | `"                chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000797](../../tests/test_api.py#L797) | 797 | `"            except TimeoutError:"` | — |
| [SRC-3451CC474D-L000798](../../tests/test_api.py#L798) | 798 | `"                break"` | — |
| [SRC-3451CC474D-L000799](../../tests/test_api.py#L799) | 799 | `"            except OSError:"` | — |
| [SRC-3451CC474D-L000800](../../tests/test_api.py#L800) | 800 | `"                break"` | — |
| [SRC-3451CC474D-L000801](../../tests/test_api.py#L801) | 801 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000802](../../tests/test_api.py#L802) | 802 | `"                break"` | — |
| [SRC-3451CC474D-L000803](../../tests/test_api.py#L803) | 803 | `"            response.extend(chunk)"` | — |
| [SRC-3451CC474D-L000804](../../tests/test_api.py#L804) | 804 | `"        elapsed = time.monotonic() - started"` | — |
| [SRC-3451CC474D-L000805](../../tests/test_api.py#L805) | 805 | `""` | — |
| [SRC-3451CC474D-L000806](../../tests/test_api.py#L806) | 806 | `"    assert elapsed < 0.8"` | — |
| [SRC-3451CC474D-L000807](../../tests/test_api.py#L807) | 807 | `"    # The timed-out request never reached application dispatch; the handler closes silently."` | — |
| [SRC-3451CC474D-L000808](../../tests/test_api.py#L808) | 808 | `"    assert response == b\"\""` | — |
| [SRC-3451CC474D-L000809](../../tests/test_api.py#L809) | 809 | `""` | — |
| [SRC-3451CC474D-L000810](../../tests/test_api.py#L810) | 810 | `"def test_public_preflight_does_not_trust_spoofed_forwarded_host(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000811](../../tests/test_api.py#L811) | 811 | `"    \"\"\"A client-controlled X-Forwarded-Host must not grant an origin CORS access.\"\"\""` | — |
| [SRC-3451CC474D-L000812](../../tests/test_api.py#L812) | 812 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000813](../../tests/test_api.py#L813) | 813 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000814](../../tests/test_api.py#L814) | 814 | `""` | — |
| [SRC-3451CC474D-L000815](../../tests/test_api.py#L815) | 815 | `"    request = Request("` | — |
| [SRC-3451CC474D-L000816](../../tests/test_api.py#L816) | 816 | `"        local_api + \"/api/agent\","` | — |
| [SRC-3451CC474D-L000817](../../tests/test_api.py#L817) | 817 | `"        method=\"OPTIONS\","` | — |
| [SRC-3451CC474D-L000818](../../tests/test_api.py#L818) | 818 | `"        headers={"` | — |
| [SRC-3451CC474D-L000819](../../tests/test_api.py#L819) | 819 | `"            \"Origin\": \"https://attacker.example\","` | — |
| [SRC-3451CC474D-L000820](../../tests/test_api.py#L820) | 820 | `"            \"X-Forwarded-Host\": \"attacker.example\","` | — |
| [SRC-3451CC474D-L000821](../../tests/test_api.py#L821) | 821 | `"            \"X-Forwarded-Proto\": \"https\","` | — |
| [SRC-3451CC474D-L000822](../../tests/test_api.py#L822) | 822 | `"            \"Access-Control-Request-Method\": \"POST\","` | — |
| [SRC-3451CC474D-L000823](../../tests/test_api.py#L823) | 823 | `"            \"Access-Control-Request-Headers\": \"authorization,content-type\","` | — |
| [SRC-3451CC474D-L000824](../../tests/test_api.py#L824) | 824 | `"        },"` | — |
| [SRC-3451CC474D-L000825](../../tests/test_api.py#L825) | 825 | `"    )"` | — |
| [SRC-3451CC474D-L000826](../../tests/test_api.py#L826) | 826 | `"    with pytest.raises(HTTPError) as error:"` | — |
| [SRC-3451CC474D-L000827](../../tests/test_api.py#L827) | 827 | `"        urlopen(request, timeout=3)"` | — |
| [SRC-3451CC474D-L000828](../../tests/test_api.py#L828) | 828 | `"    assert error.value.code == 403"` | — |
| [SRC-3451CC474D-L000829](../../tests/test_api.py#L829) | 829 | `""` | — |
| [SRC-3451CC474D-L000830](../../tests/test_api.py#L830) | 830 | `""` | — |
| [SRC-3451CC474D-L000831](../../tests/test_api.py#L831) | 831 | `"def test_public_origin_still_allows_the_requested_host(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000832](../../tests/test_api.py#L832) | 832 | `"    \"\"\"Same-service public UI remains compatible when the request Host is trusted.\"\"\""` | — |
| [SRC-3451CC474D-L000833](../../tests/test_api.py#L833) | 833 | `"    from types import SimpleNamespace"` | — |
| [SRC-3451CC474D-L000834](../../tests/test_api.py#L834) | 834 | `""` | — |
| [SRC-3451CC474D-L000835](../../tests/test_api.py#L835) | 835 | `"    from api.omarai import Handler"` | — |
| [SRC-3451CC474D-L000836](../../tests/test_api.py#L836) | 836 | `""` | — |
| [SRC-3451CC474D-L000837](../../tests/test_api.py#L837) | 837 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000838](../../tests/test_api.py#L838) | 838 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000839](../../tests/test_api.py#L839) | 839 | `"    handler = SimpleNamespace("` | — |
| [SRC-3451CC474D-L000840](../../tests/test_api.py#L840) | 840 | `"        headers={"` | — |
| [SRC-3451CC474D-L000841](../../tests/test_api.py#L841) | 841 | `"            \"Host\": \"omarai.example\","` | — |
| [SRC-3451CC474D-L000842](../../tests/test_api.py#L842) | 842 | `"            \"X-Forwarded-Proto\": \"https\","` | — |
| [SRC-3451CC474D-L000843](../../tests/test_api.py#L843) | 843 | `"            \"X-Forwarded-Host\": \"attacker.example\","` | — |
| [SRC-3451CC474D-L000844](../../tests/test_api.py#L844) | 844 | `"        }"` | — |
| [SRC-3451CC474D-L000845](../../tests/test_api.py#L845) | 845 | `"    )"` | — |
| [SRC-3451CC474D-L000846](../../tests/test_api.py#L846) | 846 | `"    allowed = Handler._allowed_origins(handler)"` | — |
| [SRC-3451CC474D-L000847](../../tests/test_api.py#L847) | 847 | `"    assert \"https://omarai.example\" in allowed"` | — |
| [SRC-3451CC474D-L000848](../../tests/test_api.py#L848) | 848 | `"    assert \"https://attacker.example\" not in allowed"` | — |
| [SRC-3451CC474D-L000849](../../tests/test_api.py#L849) | 849 | `""` | — |
| [SRC-3451CC474D-L000850](../../tests/test_api.py#L850) | 850 | `""` | — |
| [SRC-3451CC474D-L000851](../../tests/test_api.py#L851) | 851 | `""` | — |
| [SRC-3451CC474D-L000852](../../tests/test_api.py#L852) | 852 | `"def test_security_headers_apply_to_json_and_html_responses(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000853](../../tests/test_api.py#L853) | 853 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000854](../../tests/test_api.py#L854) | 854 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000855](../../tests/test_api.py#L855) | 855 | `"    for path in (\"/api/health\", \"/\"):"` | — |
| [SRC-3451CC474D-L000856](../../tests/test_api.py#L856) | 856 | `"        request = Request(local_api + path)"` | — |
| [SRC-3451CC474D-L000857](../../tests/test_api.py#L857) | 857 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000858](../../tests/test_api.py#L858) | 858 | `"            headers = {name.lower(): value for name, value in response.headers.items()}"` | — |
| [SRC-3451CC474D-L000859](../../tests/test_api.py#L859) | 859 | `"            assert headers[\"x-content-type-options\"] == \"nosniff\""` | — |
| [SRC-3451CC474D-L000860](../../tests/test_api.py#L860) | 860 | `"            assert headers[\"x-frame-options\"] == \"DENY\""` | — |
| [SRC-3451CC474D-L000861](../../tests/test_api.py#L861) | 861 | `"            assert headers[\"referrer-policy\"] == \"strict-origin-when-cross-origin\""` | — |
| [SRC-3451CC474D-L000862](../../tests/test_api.py#L862) | 862 | `"            assert \"default-src 'self'\" in headers[\"content-security-policy\"]"` | — |
| [SRC-3451CC474D-L000863](../../tests/test_api.py#L863) | 863 | `"            policy = headers[\"content-security-policy\"]"` | — |
| [SRC-3451CC474D-L000864](../../tests/test_api.py#L864) | 864 | `"            assert \"frame-ancestors 'none'\" in policy"` | — |
| [SRC-3451CC474D-L000865](../../tests/test_api.py#L865) | 865 | `"            assert \"'unsafe-inline'\" not in policy"` | — |
| [SRC-3451CC474D-L000866](../../tests/test_api.py#L866) | 866 | `"            assert \"'sha256-\" in policy"` | — |
| [SRC-3451CC474D-L000867](../../tests/test_api.py#L867) | 867 | `"            assert headers[\"permissions-policy\"] == ("` | — |
| [SRC-3451CC474D-L000868](../../tests/test_api.py#L868) | 868 | `"                \"camera=(), microphone=(), geolocation=()\""` | — |
| [SRC-3451CC474D-L000869](../../tests/test_api.py#L869) | 869 | `"            )"` | — |
| [SRC-3451CC474D-L000870](../../tests/test_api.py#L870) | 870 | `""` | — |
| [SRC-3451CC474D-L000871](../../tests/test_api.py#L871) | 871 | `""` | — |
| [SRC-3451CC474D-L000872](../../tests/test_api.py#L872) | 872 | `"def test_health_exposes_only_validated_image_baked_sha(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L000873](../../tests/test_api.py#L873) | 873 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000874](../../tests/test_api.py#L874) | 874 | `""` | — |
| [SRC-3451CC474D-L000875](../../tests/test_api.py#L875) | 875 | `"    build_sha_file = tmp_path / \"BUILD_SHA\""` | — |
| [SRC-3451CC474D-L000876](../../tests/test_api.py#L876) | 876 | `"    monkeypatch.setattr(api_module, \"BUILD_SHA_FILE\", build_sha_file)"` | — |
| [SRC-3451CC474D-L000877](../../tests/test_api.py#L877) | 877 | `"    assert api_module._build_sha() == \"unknown\""` | — |
| [SRC-3451CC474D-L000878](../../tests/test_api.py#L878) | 878 | `"    build_sha_file.write_text(\"a\" * 40, encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000879](../../tests/test_api.py#L879) | 879 | `"    assert api_module._build_sha() == \"a\" * 40"` | — |
| [SRC-3451CC474D-L000880](../../tests/test_api.py#L880) | 880 | `"    build_sha_file.write_text(\"not-a-git-sha\", encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000881](../../tests/test_api.py#L881) | 881 | `"    assert api_module._build_sha() == \"unknown\""` | — |
| [SRC-3451CC474D-L000882](../../tests/test_api.py#L882) | 882 | `""` | — |
| [SRC-3451CC474D-L000883](../../tests/test_api.py#L883) | 883 | `""` | — |
| [SRC-3451CC474D-L000884](../../tests/test_api.py#L884) | 884 | `""` | — |
| [SRC-3451CC474D-L000885](../../tests/test_api.py#L885) | 885 | `"@pytest.mark.parametrize("` | — |
| [SRC-3451CC474D-L000886](../../tests/test_api.py#L886) | 886 | `"    (\"variable\", \"source\"),"` | — |
| [SRC-3451CC474D-L000887](../../tests/test_api.py#L887) | 887 | `"    ["` | — |
| [SRC-3451CC474D-L000888](../../tests/test_api.py#L888) | 888 | `"        (\"RAILWAY_GIT_COMMIT_SHA\", \"platform:railway\"),"` | — |
| [SRC-3451CC474D-L000889](../../tests/test_api.py#L889) | 889 | `"        (\"RENDER_GIT_COMMIT\", \"platform:render\"),"` | — |
| [SRC-3451CC474D-L000890](../../tests/test_api.py#L890) | 890 | `"    ],"` | — |
| [SRC-3451CC474D-L000891](../../tests/test_api.py#L891) | 891 | `")"` | — |
| [SRC-3451CC474D-L000892](../../tests/test_api.py#L892) | 892 | `"def test_build_identity_uses_validated_platform_commit_when_image_sha_is_unavailable("` | — |
| [SRC-3451CC474D-L000893](../../tests/test_api.py#L893) | 893 | `"    monkeypatch, tmp_path, variable, source"` | — |
| [SRC-3451CC474D-L000894](../../tests/test_api.py#L894) | 894 | `"):"` | — |
| [SRC-3451CC474D-L000895](../../tests/test_api.py#L895) | 895 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000896](../../tests/test_api.py#L896) | 896 | `""` | — |
| [SRC-3451CC474D-L000897](../../tests/test_api.py#L897) | 897 | `"    build_sha_file = tmp_path / \"BUILD_SHA\""` | — |
| [SRC-3451CC474D-L000898](../../tests/test_api.py#L898) | 898 | `"    monkeypatch.setattr(api_module, \"BUILD_SHA_FILE\", build_sha_file)"` | — |
| [SRC-3451CC474D-L000899](../../tests/test_api.py#L899) | 899 | `"    build_sha_file.write_text(\"unknown\", encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000900](../../tests/test_api.py#L900) | 900 | `"    for name, _label in api_module._PLATFORM_BUILD_SHA_ENVIRONMENTS:"` | — |
| [SRC-3451CC474D-L000901](../../tests/test_api.py#L901) | 901 | `"        monkeypatch.delenv(name, raising=False)"` | — |
| [SRC-3451CC474D-L000902](../../tests/test_api.py#L902) | 902 | `"    monkeypatch.setenv(variable, \"b\" * 40)"` | — |
| [SRC-3451CC474D-L000903](../../tests/test_api.py#L903) | 903 | `""` | — |
| [SRC-3451CC474D-L000904](../../tests/test_api.py#L904) | 904 | `"    assert api_module._build_identity() == (\"b\" * 40, source)"` | — |
| [SRC-3451CC474D-L000905](../../tests/test_api.py#L905) | 905 | `""` | — |
| [SRC-3451CC474D-L000906](../../tests/test_api.py#L906) | 906 | `""` | — |
| [SRC-3451CC474D-L000907](../../tests/test_api.py#L907) | 907 | `"def test_invalid_platform_commit_does_not_create_build_identity(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L000908](../../tests/test_api.py#L908) | 908 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000909](../../tests/test_api.py#L909) | 909 | `""` | — |
| [SRC-3451CC474D-L000910](../../tests/test_api.py#L910) | 910 | `"    monkeypatch.setattr(api_module, \"BUILD_SHA_FILE\", tmp_path / \"BUILD_SHA\")"` | — |
| [SRC-3451CC474D-L000911](../../tests/test_api.py#L911) | 911 | `"    api_module.BUILD_SHA_FILE.write_text(\"unknown\", encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000912](../../tests/test_api.py#L912) | 912 | `"    monkeypatch.setenv(\"RAILWAY_GIT_COMMIT_SHA\", \"not-a-sha\")"` | — |
| [SRC-3451CC474D-L000913](../../tests/test_api.py#L913) | 913 | `"    monkeypatch.setenv(\"RENDER_GIT_COMMIT\", \"also-not-a-sha\")"` | — |
| [SRC-3451CC474D-L000914](../../tests/test_api.py#L914) | 914 | `""` | — |
| [SRC-3451CC474D-L000915](../../tests/test_api.py#L915) | 915 | `"    assert api_module._build_identity() == (\"unknown\", \"unknown\")"` | — |
| [SRC-3451CC474D-L000916](../../tests/test_api.py#L916) | 916 | `""` | — |
| [SRC-3451CC474D-L000917](../../tests/test_api.py#L917) | 917 | `""` | — |
| [SRC-3451CC474D-L000918](../../tests/test_api.py#L918) | 918 | `""` | — |
| [SRC-3451CC474D-L000919](../../tests/test_api.py#L919) | 919 | `"def test_lead_store_uses_configured_database_path(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L000920](../../tests/test_api.py#L920) | 920 | `"    from api.omarai import _lead_store_from_environment"` | — |
| [SRC-3451CC474D-L000921](../../tests/test_api.py#L921) | 921 | `""` | — |
| [SRC-3451CC474D-L000922](../../tests/test_api.py#L922) | 922 | `"    database_path = tmp_path / \"persistent\" / \"omarai.sqlite3\""` | — |
| [SRC-3451CC474D-L000923](../../tests/test_api.py#L923) | 923 | `"    monkeypatch.setenv(\"OMARAI_DB_PATH\", str(database_path))"` | — |
| [SRC-3451CC474D-L000924](../../tests/test_api.py#L924) | 924 | `""` | — |
| [SRC-3451CC474D-L000925](../../tests/test_api.py#L925) | 925 | `"    store = _lead_store_from_environment()"` | — |
| [SRC-3451CC474D-L000926](../../tests/test_api.py#L926) | 926 | `""` | — |
| [SRC-3451CC474D-L000927](../../tests/test_api.py#L927) | 927 | `"    assert store.path == database_path"` | — |
| [SRC-3451CC474D-L000928](../../tests/test_api.py#L928) | 928 | `"    assert database_path.is_file()"` | — |
| [SRC-3451CC474D-L000929](../../tests/test_api.py#L929) | 929 | `""` | — |
| [SRC-3451CC474D-L000930](../../tests/test_api.py#L930) | 930 | `""` | — |
| [SRC-3451CC474D-L000931](../../tests/test_api.py#L931) | 931 | `""` | — |
| [SRC-3451CC474D-L000932](../../tests/test_api.py#L932) | 932 | `"def test_agent_concurrency_slot_released_after_operation_error(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000933](../../tests/test_api.py#L933) | 933 | `"    from api.omarai import WebAgent"` | — |
| [SRC-3451CC474D-L000934](../../tests/test_api.py#L934) | 934 | `""` | — |
| [SRC-3451CC474D-L000935](../../tests/test_api.py#L935) | 935 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000936](../../tests/test_api.py#L936) | 936 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000937](../../tests/test_api.py#L937) | 937 | `"    monkeypatch.setattr(Handler, \"_request_times\", defaultdict(deque))"` | — |
| [SRC-3451CC474D-L000938](../../tests/test_api.py#L938) | 938 | `"    monkeypatch.setattr(Handler, \"_rate_last_cleanup\", 0.0)"` | — |
| [SRC-3451CC474D-L000939](../../tests/test_api.py#L939) | 939 | `"    monkeypatch.setattr(Handler, \"_agent_semaphore\", threading.BoundedSemaphore(1))"` | — |
| [SRC-3451CC474D-L000940](../../tests/test_api.py#L940) | 940 | `"    state = {\"fail\": True}"` | — |
| [SRC-3451CC474D-L000941](../../tests/test_api.py#L941) | 941 | `""` | — |
| [SRC-3451CC474D-L000942](../../tests/test_api.py#L942) | 942 | `"    def answer_with_one_transient_failure(self, question, history=None, mode=\"auto\", *, budget_profile=\"default\"):"` | — |
| [SRC-3451CC474D-L000943](../../tests/test_api.py#L943) | 943 | `"        if state[\"fail\"]:"` | — |
| [SRC-3451CC474D-L000944](../../tests/test_api.py#L944) | 944 | `"            raise RuntimeError(\"synthetic operation failure\")"` | — |
| [SRC-3451CC474D-L000945](../../tests/test_api.py#L945) | 945 | `"        return {"` | — |
| [SRC-3451CC474D-L000946](../../tests/test_api.py#L946) | 946 | `"            \"answer\": \"اختبار ناجح\","` | — |
| [SRC-3451CC474D-L000947](../../tests/test_api.py#L947) | 947 | `"            \"question\": question,"` | — |
| [SRC-3451CC474D-L000948](../../tests/test_api.py#L948) | 948 | `"            \"search_query\": question,"` | — |
| [SRC-3451CC474D-L000949](../../tests/test_api.py#L949) | 949 | `"            \"search_queries\": [],"` | — |
| [SRC-3451CC474D-L000950](../../tests/test_api.py#L950) | 950 | `"            \"search_report\": {"` | — |
| [SRC-3451CC474D-L000951](../../tests/test_api.py#L951) | 951 | `"                \"search_attempted\": False,"` | — |
| [SRC-3451CC474D-L000952](../../tests/test_api.py#L952) | 952 | `"                \"search_outcome\": \"not_attempted\","` | — |
| [SRC-3451CC474D-L000953](../../tests/test_api.py#L953) | 953 | `"            },"` | — |
| [SRC-3451CC474D-L000954](../../tests/test_api.py#L954) | 954 | `"            \"sources\": [],"` | — |
| [SRC-3451CC474D-L000955](../../tests/test_api.py#L955) | 955 | `"            \"used_language_model\": False,"` | — |
| [SRC-3451CC474D-L000956](../../tests/test_api.py#L956) | 956 | `"            \"used_web_search\": False,"` | — |
| [SRC-3451CC474D-L000957](../../tests/test_api.py#L957) | 957 | `"            \"search_attempted\": False,"` | — |
| [SRC-3451CC474D-L000958](../../tests/test_api.py#L958) | 958 | `"            \"used_social_search\": False,"` | — |
| [SRC-3451CC474D-L000959](../../tests/test_api.py#L959) | 959 | `"            \"warnings\": [],"` | — |
| [SRC-3451CC474D-L000960](../../tests/test_api.py#L960) | 960 | `"            \"kind\": \"web_fallback\","` | — |
| [SRC-3451CC474D-L000961](../../tests/test_api.py#L961) | 961 | `"        }"` | — |
| [SRC-3451CC474D-L000962](../../tests/test_api.py#L962) | 962 | `""` | — |
| [SRC-3451CC474D-L000963](../../tests/test_api.py#L963) | 963 | `"    monkeypatch.setattr(WebAgent, \"answer\", answer_with_one_transient_failure)"` | — |
| [SRC-3451CC474D-L000964](../../tests/test_api.py#L964) | 964 | `""` | — |
| [SRC-3451CC474D-L000965](../../tests/test_api.py#L965) | 965 | `"    status, payload = request_json("` | — |
| [SRC-3451CC474D-L000966](../../tests/test_api.py#L966) | 966 | `"        local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"الطلب الأول\"}"` | — |
| [SRC-3451CC474D-L000967](../../tests/test_api.py#L967) | 967 | `"    )"` | — |
| [SRC-3451CC474D-L000968](../../tests/test_api.py#L968) | 968 | `"    assert status == 500"` | — |
| [SRC-3451CC474D-L000969](../../tests/test_api.py#L969) | 969 | `"    assert payload[\"error\"] == \"internal server error\""` | — |
| [SRC-3451CC474D-L000970](../../tests/test_api.py#L970) | 970 | `""` | — |
| [SRC-3451CC474D-L000971](../../tests/test_api.py#L971) | 971 | `"    state[\"fail\"] = False"` | — |
| [SRC-3451CC474D-L000972](../../tests/test_api.py#L972) | 972 | `"    status, payload = request_json("` | — |
| [SRC-3451CC474D-L000973](../../tests/test_api.py#L973) | 973 | `"        local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"الطلب الثاني\"}"` | — |
| [SRC-3451CC474D-L000974](../../tests/test_api.py#L974) | 974 | `"    )"` | — |
| [SRC-3451CC474D-L000975](../../tests/test_api.py#L975) | 975 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000976](../../tests/test_api.py#L976) | 976 | `"    assert payload[\"answer\"] == \"اختبار ناجح\""` | — |
| [SRC-3451CC474D-L000977](../../tests/test_api.py#L977) | 977 | `""` | — |
| [SRC-3451CC474D-L000978](../../tests/test_api.py#L978) | 978 | `""` | — |
| [SRC-3451CC474D-L000979](../../tests/test_api.py#L979) | 979 | `"def test_csp_hashes_match_all_first_party_inline_content_and_attributes():"` | — |
| [SRC-3451CC474D-L000980](../../tests/test_api.py#L980) | 980 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000981](../../tests/test_api.py#L981) | 981 | `""` | — |
| [SRC-3451CC474D-L000982](../../tests/test_api.py#L982) | 982 | `"    policy = api_module._content_security_policy()"` | — |
| [SRC-3451CC474D-L000983](../../tests/test_api.py#L983) | 983 | `"    assert \"'unsafe-inline'\" not in policy"` | — |
| [SRC-3451CC474D-L000984](../../tests/test_api.py#L984) | 984 | `"    script_blocks = 0"` | — |
| [SRC-3451CC474D-L000985](../../tests/test_api.py#L985) | 985 | `"    style_blocks = 0"` | — |
| [SRC-3451CC474D-L000986](../../tests/test_api.py#L986) | 986 | `"    style_attributes = 0"` | — |
| [SRC-3451CC474D-L000987](../../tests/test_api.py#L987) | 987 | `"    for html_path in api_module.ROOT.glob(\"*.html\"):"` | — |
| [SRC-3451CC474D-L000988](../../tests/test_api.py#L988) | 988 | `"        document = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3451CC474D-L000989](../../tests/test_api.py#L989) | 989 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000990](../../tests/test_api.py#L990) | 990 | `"            r\"<script\\b(?P<attrs>[^>]*)>(?P<body>.*?)</script\\s*>\","` | — |
| [SRC-3451CC474D-L000991](../../tests/test_api.py#L991) | 991 | `"            document,"` | — |
| [SRC-3451CC474D-L000992](../../tests/test_api.py#L992) | 992 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L000993](../../tests/test_api.py#L993) | 993 | `"        ):"` | — |
| [SRC-3451CC474D-L000994](../../tests/test_api.py#L994) | 994 | `"            if re.search(r\"\\bsrc\\s*=\", match.group(\"attrs\"), re.IGNORECASE):"` | — |
| [SRC-3451CC474D-L000995](../../tests/test_api.py#L995) | 995 | `"                continue"` | — |
| [SRC-3451CC474D-L000996](../../tests/test_api.py#L996) | 996 | `"            script_blocks += 1"` | — |
| [SRC-3451CC474D-L000997](../../tests/test_api.py#L997) | 997 | `"            assert api_module._csp_hash_source(match.group(\"body\")) in policy"` | — |
| [SRC-3451CC474D-L000998](../../tests/test_api.py#L998) | 998 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000999](../../tests/test_api.py#L999) | 999 | `"            r\"<style\\b[^>]*>(?P<body>.*?)</style\\s*>\","` | — |
| [SRC-3451CC474D-L001000](../../tests/test_api.py#L1000) | 1000 | `"            document,"` | — |
| [SRC-3451CC474D-L001001](../../tests/test_api.py#L1001) | 1001 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L001002](../../tests/test_api.py#L1002) | 1002 | `"        ):"` | — |
| [SRC-3451CC474D-L001003](../../tests/test_api.py#L1003) | 1003 | `"            style_blocks += 1"` | — |
| [SRC-3451CC474D-L001004](../../tests/test_api.py#L1004) | 1004 | `"            assert api_module._csp_hash_source(match.group(\"body\")) in policy"` | — |
| [SRC-3451CC474D-L001005](../../tests/test_api.py#L1005) | 1005 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L001006](../../tests/test_api.py#L1006) | 1006 | `"            r\"\"\"\\bstyle\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-3451CC474D-L001007](../../tests/test_api.py#L1007) | 1007 | `"            document,"` | — |
| [SRC-3451CC474D-L001008](../../tests/test_api.py#L1008) | 1008 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L001009](../../tests/test_api.py#L1009) | 1009 | `"        ):"` | — |
| [SRC-3451CC474D-L001010](../../tests/test_api.py#L1010) | 1010 | `"            style_attributes += 1"` | — |
| [SRC-3451CC474D-L001011](../../tests/test_api.py#L1011) | 1011 | `"            assert api_module._csp_hash_source(match.group(2).strip()) in policy"` | — |
| [SRC-3451CC474D-L001012](../../tests/test_api.py#L1012) | 1012 | `"    assert script_blocks >= 2"` | — |
| [SRC-3451CC474D-L001013](../../tests/test_api.py#L1013) | 1013 | `"    assert style_blocks >= 2"` | — |
| [SRC-3451CC474D-L001014](../../tests/test_api.py#L1014) | 1014 | `"    assert style_attributes >= 10"` | — |
| [SRC-3451CC474D-L001015](../../tests/test_api.py#L1015) | 1015 | `""` | — |
| [SRC-3451CC474D-L001016](../../tests/test_api.py#L1016) | 1016 | `""` | — |
| [SRC-3451CC474D-L001017](../../tests/test_api.py#L1017) | 1017 | `"def test_dashboard_uses_delegated_status_action_not_inline_onclick():"` | — |
| [SRC-3451CC474D-L001018](../../tests/test_api.py#L1018) | 1018 | `"    dashboard = (Path(__file__).resolve().parents[1] / \"web\" / \"dashboard.html\").read_text("` | — |
| [SRC-3451CC474D-L001019](../../tests/test_api.py#L1019) | 1019 | `"        encoding=\"utf-8\""` | — |
| [SRC-3451CC474D-L001020](../../tests/test_api.py#L1020) | 1020 | `"    )"` | — |
| [SRC-3451CC474D-L001021](../../tests/test_api.py#L1021) | 1021 | `"    assert 'data-action=\"save-status\"' in dashboard"` | — |
| [SRC-3451CC474D-L001022](../../tests/test_api.py#L1022) | 1022 | `"    assert 'onclick=\"saveStatus' not in dashboard"` | — |
| [SRC-3451CC474D-L001023](../../tests/test_api.py#L1023) | 1023 | `"    assert \"\"\"data-lead-id=\"'+esc(l.id)+'\">\"\"\" in dashboard"` | — |
| [SRC-3451CC474D-L001024](../../tests/test_api.py#L1024) | 1024 | `""` | — |
| [SRC-3451CC474D-L001025](../../tests/test_api.py#L1025) | 1025 | `"def test_browser_session_uses_http_only_cookie_and_rejects_cross_site_posts(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L001026](../../tests/test_api.py#L1026) | 1026 | `"    from urllib.parse import urlsplit"` | — |
| [SRC-3451CC474D-L001027](../../tests/test_api.py#L1027) | 1027 | `""` | — |
| [SRC-3451CC474D-L001028](../../tests/test_api.py#L1028) | 1028 | `"    token = \"browser-session-test-token-1234567890\""` | — |
| [SRC-3451CC474D-L001029](../../tests/test_api.py#L1029) | 1029 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L001030](../../tests/test_api.py#L1030) | 1030 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", token)"` | — |
| [SRC-3451CC474D-L001031](../../tests/test_api.py#L1031) | 1031 | `"    origin = \"https://\" + urlsplit(local_api).netloc"` | — |
| [SRC-3451CC474D-L001032](../../tests/test_api.py#L1032) | 1032 | `""` | — |
| [SRC-3451CC474D-L001033](../../tests/test_api.py#L1033) | 1033 | `"    status, payload, headers = request_json_with_headers("` | — |
| [SRC-3451CC474D-L001034](../../tests/test_api.py#L1034) | 1034 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001035](../../tests/test_api.py#L1035) | 1035 | `"        \"/api/session\","` | — |
| [SRC-3451CC474D-L001036](../../tests/test_api.py#L1036) | 1036 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001037](../../tests/test_api.py#L1037) | 1037 | `"        payload={\"access_token\": token},"` | — |
| [SRC-3451CC474D-L001038](../../tests/test_api.py#L1038) | 1038 | `"        headers={\"Origin\": origin},"` | — |
| [SRC-3451CC474D-L001039](../../tests/test_api.py#L1039) | 1039 | `"    )"` | — |
| [SRC-3451CC474D-L001040](../../tests/test_api.py#L1040) | 1040 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001041](../../tests/test_api.py#L1041) | 1041 | `"    assert payload == {\"authenticated\": True, \"role\": \"owner\"}"` | — |
| [SRC-3451CC474D-L001042](../../tests/test_api.py#L1042) | 1042 | `"    assert token not in json.dumps(payload)"` | — |
| [SRC-3451CC474D-L001043](../../tests/test_api.py#L1043) | 1043 | `"    set_cookie = headers.get(\"Set-Cookie\", \"\")"` | — |
| [SRC-3451CC474D-L001044](../../tests/test_api.py#L1044) | 1044 | `"    assert set_cookie.startswith(\"__Host-omarai_session=\")"` | — |
| [SRC-3451CC474D-L001045](../../tests/test_api.py#L1045) | 1045 | `"    assert \"Path=/\" in set_cookie"` | — |
| [SRC-3451CC474D-L001046](../../tests/test_api.py#L1046) | 1046 | `"    assert \"Secure\" in set_cookie"` | — |
| [SRC-3451CC474D-L001047](../../tests/test_api.py#L1047) | 1047 | `"    assert \"HttpOnly\" in set_cookie"` | — |
| [SRC-3451CC474D-L001048](../../tests/test_api.py#L1048) | 1048 | `"    assert \"SameSite=Strict\" in set_cookie"` | — |
| [SRC-3451CC474D-L001049](../../tests/test_api.py#L1049) | 1049 | `"    assert \"Max-Age=28800\" in set_cookie"` | — |
| [SRC-3451CC474D-L001050](../../tests/test_api.py#L1050) | 1050 | `"    assert \"Domain=\" not in set_cookie"` | — |
| [SRC-3451CC474D-L001051](../../tests/test_api.py#L1051) | 1051 | `"    cookie = set_cookie.split(\";\", 1)[0]"` | — |
| [SRC-3451CC474D-L001052](../../tests/test_api.py#L1052) | 1052 | `"    assert token not in cookie"` | — |
| [SRC-3451CC474D-L001053](../../tests/test_api.py#L1053) | 1053 | `"    assert len(cookie.split(\"=\", 1)[1]) >= 32"` | — |
| [SRC-3451CC474D-L001054](../../tests/test_api.py#L1054) | 1054 | `""` | — |
| [SRC-3451CC474D-L001055](../../tests/test_api.py#L1055) | 1055 | `"    status, session = request_json("` | — |
| [SRC-3451CC474D-L001056](../../tests/test_api.py#L1056) | 1056 | `"        local_api, \"/api/session\", headers={\"Cookie\": cookie}"` | — |
| [SRC-3451CC474D-L001057](../../tests/test_api.py#L1057) | 1057 | `"    )"` | — |
| [SRC-3451CC474D-L001058](../../tests/test_api.py#L1058) | 1058 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001059](../../tests/test_api.py#L1059) | 1059 | `"    assert session == {\"authenticated\": True, \"role\": \"owner\"}"` | — |
| [SRC-3451CC474D-L001060](../../tests/test_api.py#L1060) | 1060 | `""` | — |
| [SRC-3451CC474D-L001061](../../tests/test_api.py#L1061) | 1061 | `"    status, listing = request_json("` | — |
| [SRC-3451CC474D-L001062](../../tests/test_api.py#L1062) | 1062 | `"        local_api, \"/api/leads\", headers={\"Cookie\": cookie}"` | — |
| [SRC-3451CC474D-L001063](../../tests/test_api.py#L1063) | 1063 | `"    )"` | — |
| [SRC-3451CC474D-L001064](../../tests/test_api.py#L1064) | 1064 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001065](../../tests/test_api.py#L1065) | 1065 | `"    assert listing[\"count\"] == 0"` | — |
| [SRC-3451CC474D-L001066](../../tests/test_api.py#L1066) | 1066 | `""` | — |
| [SRC-3451CC474D-L001067](../../tests/test_api.py#L1067) | 1067 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L001068](../../tests/test_api.py#L1068) | 1068 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001069](../../tests/test_api.py#L1069) | 1069 | `"        \"/api/ask\","` | — |
| [SRC-3451CC474D-L001070](../../tests/test_api.py#L1070) | 1070 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001071](../../tests/test_api.py#L1071) | 1071 | `"        payload={\"question\": \"كم عميل؟\"},"` | — |
| [SRC-3451CC474D-L001072](../../tests/test_api.py#L1072) | 1072 | `"        headers={\"Cookie\": cookie, \"Origin\": \"https://attacker.example\"},"` | — |
| [SRC-3451CC474D-L001073](../../tests/test_api.py#L1073) | 1073 | `"    )"` | — |
| [SRC-3451CC474D-L001074](../../tests/test_api.py#L1074) | 1074 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L001075](../../tests/test_api.py#L1075) | 1075 | `"    assert \"Origin\" in error[\"error\"] or \"cross-origin\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L001076](../../tests/test_api.py#L1076) | 1076 | `""` | — |
| [SRC-3451CC474D-L001077](../../tests/test_api.py#L1077) | 1077 | `"    status, logged_out, logout_headers = request_json_with_headers("` | — |
| [SRC-3451CC474D-L001078](../../tests/test_api.py#L1078) | 1078 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001079](../../tests/test_api.py#L1079) | 1079 | `"        \"/api/session/logout\","` | — |
| [SRC-3451CC474D-L001080](../../tests/test_api.py#L1080) | 1080 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001081](../../tests/test_api.py#L1081) | 1081 | `"        payload={},"` | — |
| [SRC-3451CC474D-L001082](../../tests/test_api.py#L1082) | 1082 | `"        headers={\"Cookie\": cookie, \"Origin\": origin},"` | — |
| [SRC-3451CC474D-L001083](../../tests/test_api.py#L1083) | 1083 | `"    )"` | — |
| [SRC-3451CC474D-L001084](../../tests/test_api.py#L1084) | 1084 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001085](../../tests/test_api.py#L1085) | 1085 | `"    assert logged_out[\"logged_out\"] is True"` | — |
| [SRC-3451CC474D-L001086](../../tests/test_api.py#L1086) | 1086 | `"    cleared_cookie = logout_headers.get(\"Set-Cookie\", \"\")"` | — |
| [SRC-3451CC474D-L001087](../../tests/test_api.py#L1087) | 1087 | `"    assert cleared_cookie.startswith(\"__Host-omarai_session=\")"` | — |
| [SRC-3451CC474D-L001088](../../tests/test_api.py#L1088) | 1088 | `"    assert \"Max-Age=0\" in cleared_cookie"` | — |
| [SRC-3451CC474D-L001089](../../tests/test_api.py#L1089) | 1089 | `""` | — |
| [SRC-3451CC474D-L001090](../../tests/test_api.py#L1090) | 1090 | `"    status, error = request_json(local_api, \"/api/leads\")"` | — |
| [SRC-3451CC474D-L001091](../../tests/test_api.py#L1091) | 1091 | `"    assert status == 401"` | — |
| [SRC-3451CC474D-L001092](../../tests/test_api.py#L1092) | 1092 | `""` | — |
| [SRC-3451CC474D-L001093](../../tests/test_api.py#L1093) | 1093 | `""` | — |
| [SRC-3451CC474D-L001094](../../tests/test_api.py#L1094) | 1094 | `"def test_browser_session_login_rejects_untrusted_origin(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L001095](../../tests/test_api.py#L1095) | 1095 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L001096](../../tests/test_api.py#L1096) | 1096 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"browser-session-test-token-1234567890\")"` | — |
| [SRC-3451CC474D-L001097](../../tests/test_api.py#L1097) | 1097 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L001098](../../tests/test_api.py#L1098) | 1098 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001099](../../tests/test_api.py#L1099) | 1099 | `"        \"/api/session\","` | — |
| [SRC-3451CC474D-L001100](../../tests/test_api.py#L1100) | 1100 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001101](../../tests/test_api.py#L1101) | 1101 | `"        payload={\"access_token\": \"browser-session-test-token-1234567890\"},"` | — |
| [SRC-3451CC474D-L001102](../../tests/test_api.py#L1102) | 1102 | `"        headers={\"Origin\": \"https://attacker.example\"},"` | — |
| [SRC-3451CC474D-L001103](../../tests/test_api.py#L1103) | 1103 | `"    )"` | — |
| [SRC-3451CC474D-L001104](../../tests/test_api.py#L1104) | 1104 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L001105](../../tests/test_api.py#L1105) | 1105 | `"    assert \"same-origin\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L001106](../../tests/test_api.py#L1106) | 1106 | `""` | — |
| [SRC-3451CC474D-L001107](../../tests/test_api.py#L1107) | 1107 | `""` | — |
| [SRC-3451CC474D-L001108](../../tests/test_api.py#L1108) | 1108 | `"def test_browser_session_does_not_accept_unsafe_cookie_token_format(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L001109](../../tests/test_api.py#L1109) | 1109 | `"    from urllib.parse import urlsplit"` | — |
| [SRC-3451CC474D-L001110](../../tests/test_api.py#L1110) | 1110 | `""` | — |
| [SRC-3451CC474D-L001111](../../tests/test_api.py#L1111) | 1111 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L001112](../../tests/test_api.py#L1112) | 1112 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"browser-session-test-token-1234567890\")"` | — |
| [SRC-3451CC474D-L001113](../../tests/test_api.py#L1113) | 1113 | `"    status, _error = request_json("` | — |
| [SRC-3451CC474D-L001114](../../tests/test_api.py#L1114) | 1114 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001115](../../tests/test_api.py#L1115) | 1115 | `"        \"/api/session\","` | — |
| [SRC-3451CC474D-L001116](../../tests/test_api.py#L1116) | 1116 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001117](../../tests/test_api.py#L1117) | 1117 | `"        payload={\"access_token\": \"unsafe;token\" + \"x\" * 40},"` | — |
| [SRC-3451CC474D-L001118](../../tests/test_api.py#L1118) | 1118 | `"        headers={\"Origin\": \"https://\" + urlsplit(local_api).netloc},"` | — |
| [SRC-3451CC474D-L001119](../../tests/test_api.py#L1119) | 1119 | `"    )"` | — |
| [SRC-3451CC474D-L001120](../../tests/test_api.py#L1120) | 1120 | `"    assert status == 401"` | — |
| [SRC-3451CC474D-L001121](../../tests/test_api.py#L1121) | 1121 | `""` | — |
| [SRC-3451CC474D-L001122](../../tests/test_api.py#L1122) | 1122 | `"def test_expired_browser_session_can_logout_and_clear_cookie(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L001123](../../tests/test_api.py#L1123) | 1123 | `"    from urllib.parse import urlsplit"` | — |
| [SRC-3451CC474D-L001124](../../tests/test_api.py#L1124) | 1124 | `"    from api.omarai import Handler"` | — |
| [SRC-3451CC474D-L001125](../../tests/test_api.py#L1125) | 1125 | `""` | — |
| [SRC-3451CC474D-L001126](../../tests/test_api.py#L1126) | 1126 | `"    token = \"expired-browser-session-token-123456\""` | — |
| [SRC-3451CC474D-L001127](../../tests/test_api.py#L1127) | 1127 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L001128](../../tests/test_api.py#L1128) | 1128 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", token)"` | — |
| [SRC-3451CC474D-L001129](../../tests/test_api.py#L1129) | 1129 | `"    origin = \"https://\" + urlsplit(local_api).netloc"` | — |
| [SRC-3451CC474D-L001130](../../tests/test_api.py#L1130) | 1130 | `""` | — |
| [SRC-3451CC474D-L001131](../../tests/test_api.py#L1131) | 1131 | `"    status, _payload, headers = request_json_with_headers("` | — |
| [SRC-3451CC474D-L001132](../../tests/test_api.py#L1132) | 1132 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001133](../../tests/test_api.py#L1133) | 1133 | `"        \"/api/session\","` | — |
| [SRC-3451CC474D-L001134](../../tests/test_api.py#L1134) | 1134 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001135](../../tests/test_api.py#L1135) | 1135 | `"        payload={\"access_token\": token},"` | — |
| [SRC-3451CC474D-L001136](../../tests/test_api.py#L1136) | 1136 | `"        headers={\"Origin\": origin},"` | — |
| [SRC-3451CC474D-L001137](../../tests/test_api.py#L1137) | 1137 | `"    )"` | — |
| [SRC-3451CC474D-L001138](../../tests/test_api.py#L1138) | 1138 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001139](../../tests/test_api.py#L1139) | 1139 | `"    cookie = headers.get(\"Set-Cookie\", \"\").split(\";\", 1)[0]"` | — |
| [SRC-3451CC474D-L001140](../../tests/test_api.py#L1140) | 1140 | `"    session_id = cookie.split(\"=\", 1)[1]"` | — |
| [SRC-3451CC474D-L001141](../../tests/test_api.py#L1141) | 1141 | `""` | — |
| [SRC-3451CC474D-L001142](../../tests/test_api.py#L1142) | 1142 | `"    with Handler.store.connect() as db:"` | — |
| [SRC-3451CC474D-L001143](../../tests/test_api.py#L1143) | 1143 | `"        db.execute("` | — |
| [SRC-3451CC474D-L001144](../../tests/test_api.py#L1144) | 1144 | `"            \"UPDATE web_sessions SET expires_at=? WHERE session_hash=?\","` | — |
| [SRC-3451CC474D-L001145](../../tests/test_api.py#L1145) | 1145 | `"            (\"2000-01-01T00:00:00Z\", Handler.store._token_hash(session_id)),"` | — |
| [SRC-3451CC474D-L001146](../../tests/test_api.py#L1146) | 1146 | `"        )"` | — |
| [SRC-3451CC474D-L001147](../../tests/test_api.py#L1147) | 1147 | `""` | — |
| [SRC-3451CC474D-L001148](../../tests/test_api.py#L1148) | 1148 | `"    status, payload, logout_headers = request_json_with_headers("` | — |
| [SRC-3451CC474D-L001149](../../tests/test_api.py#L1149) | 1149 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001150](../../tests/test_api.py#L1150) | 1150 | `"        \"/api/session/logout\","` | — |
| [SRC-3451CC474D-L001151](../../tests/test_api.py#L1151) | 1151 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001152](../../tests/test_api.py#L1152) | 1152 | `"        payload={},"` | — |
| [SRC-3451CC474D-L001153](../../tests/test_api.py#L1153) | 1153 | `"        headers={\"Cookie\": cookie, \"Origin\": origin},"` | — |
| [SRC-3451CC474D-L001154](../../tests/test_api.py#L1154) | 1154 | `"    )"` | — |
| [SRC-3451CC474D-L001155](../../tests/test_api.py#L1155) | 1155 | `""` | — |
| [SRC-3451CC474D-L001156](../../tests/test_api.py#L1156) | 1156 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L001157](../../tests/test_api.py#L1157) | 1157 | `"    assert payload == {\"logged_out\": True}"` | — |
| [SRC-3451CC474D-L001158](../../tests/test_api.py#L1158) | 1158 | `"    cleared_cookie = logout_headers.get(\"Set-Cookie\", \"\")"` | — |
| [SRC-3451CC474D-L001159](../../tests/test_api.py#L1159) | 1159 | `"    assert cleared_cookie.startswith(\"__Host-omarai_session=\")"` | — |
| [SRC-3451CC474D-L001160](../../tests/test_api.py#L1160) | 1160 | `"    assert \"Max-Age=0\" in cleared_cookie"` | — |
| [SRC-3451CC474D-L001161](../../tests/test_api.py#L1161) | 1161 | `""` | — |
| [SRC-3451CC474D-L001162](../../tests/test_api.py#L1162) | 1162 | `"    status, _error = request_json("` | — |
| [SRC-3451CC474D-L001163](../../tests/test_api.py#L1163) | 1163 | `"        local_api, \"/api/session\", headers={\"Cookie\": cookie}"` | — |
| [SRC-3451CC474D-L001164](../../tests/test_api.py#L1164) | 1164 | `"    )"` | — |
| [SRC-3451CC474D-L001165](../../tests/test_api.py#L1165) | 1165 | `"    assert status == 401"` | — |
| [SRC-3451CC474D-L001166](../../tests/test_api.py#L1166) | 1166 | `""` | — |
| [SRC-3451CC474D-L001167](../../tests/test_api.py#L1167) | 1167 | `"def test_browser_session_logout_rejects_untrusted_origin_even_without_valid_cookie("` | — |
| [SRC-3451CC474D-L001168](../../tests/test_api.py#L1168) | 1168 | `"    local_api, monkeypatch"` | — |
| [SRC-3451CC474D-L001169](../../tests/test_api.py#L1169) | 1169 | `"):"` | — |
| [SRC-3451CC474D-L001170](../../tests/test_api.py#L1170) | 1170 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L001171](../../tests/test_api.py#L1171) | 1171 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L001172](../../tests/test_api.py#L1172) | 1172 | `"        local_api,"` | — |
| [SRC-3451CC474D-L001173](../../tests/test_api.py#L1173) | 1173 | `"        \"/api/session/logout\","` | — |
| [SRC-3451CC474D-L001174](../../tests/test_api.py#L1174) | 1174 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L001175](../../tests/test_api.py#L1175) | 1175 | `"        payload={},"` | — |
| [SRC-3451CC474D-L001176](../../tests/test_api.py#L1176) | 1176 | `"        headers={\"Origin\": \"https://attacker.example\"},"` | — |
| [SRC-3451CC474D-L001177](../../tests/test_api.py#L1177) | 1177 | `"    )"` | — |
| [SRC-3451CC474D-L001178](../../tests/test_api.py#L1178) | 1178 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L001179](../../tests/test_api.py#L1179) | 1179 | `"    assert \"same-origin\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L001180](../../tests/test_api.py#L1180) | 1180 | `""` | — |
| [SRC-3451CC474D-L001181](../../tests/test_api.py#L1181) | 1181 | `"@pytest.mark.parametrize("` | — |
| [SRC-3451CC474D-L001182](../../tests/test_api.py#L1182) | 1182 | `"    (\"request_line\", \"framing_headers\", \"body\", \"error_marker\"),"` | — |
| [SRC-3451CC474D-L001183](../../tests/test_api.py#L1183) | 1183 | `"    ["` | — |
| [SRC-3451CC474D-L001184](../../tests/test_api.py#L1184) | 1184 | `"        ("` | — |
| [SRC-3451CC474D-L001185](../../tests/test_api.py#L1185) | 1185 | `"            \"POST /api/analyze HTTP/1.1\","` | — |
| [SRC-3451CC474D-L001186](../../tests/test_api.py#L1186) | 1186 | `"            b\"Transfer-Encoding: chunked\\r\\nContent-Length: 4\\r\\n\","` | — |
| [SRC-3451CC474D-L001187](../../tests/test_api.py#L1187) | 1187 | `"            b\"0\\r\\n\\r\\n\","` | — |
| [SRC-3451CC474D-L001188](../../tests/test_api.py#L1188) | 1188 | `"            b\"Transfer-Encoding\","` | — |
| [SRC-3451CC474D-L001189](../../tests/test_api.py#L1189) | 1189 | `"        ),"` | — |
| [SRC-3451CC474D-L001190](../../tests/test_api.py#L1190) | 1190 | `"        ("` | — |
| [SRC-3451CC474D-L001191](../../tests/test_api.py#L1191) | 1191 | `"            \"POST /api/analyze HTTP/1.1\","` | — |
| [SRC-3451CC474D-L001192](../../tests/test_api.py#L1192) | 1192 | `"            b\"Content-Length: 4\\r\\nContent-Length: 5\\r\\n\","` | — |
| [SRC-3451CC474D-L001193](../../tests/test_api.py#L1193) | 1193 | `"            b\"test\","` | — |
| [SRC-3451CC474D-L001194](../../tests/test_api.py#L1194) | 1194 | `"            b\"Content-Length\","` | — |
| [SRC-3451CC474D-L001195](../../tests/test_api.py#L1195) | 1195 | `"        ),"` | — |
| [SRC-3451CC474D-L001196](../../tests/test_api.py#L1196) | 1196 | `"        ("` | — |
| [SRC-3451CC474D-L001197](../../tests/test_api.py#L1197) | 1197 | `"            \"GET /api/health HTTP/1.1\","` | — |
| [SRC-3451CC474D-L001198](../../tests/test_api.py#L1198) | 1198 | `"            b\"Content-Length: 4\\r\\n\","` | — |
| [SRC-3451CC474D-L001199](../../tests/test_api.py#L1199) | 1199 | `"            b\"test\","` | — |
| [SRC-3451CC474D-L001200](../../tests/test_api.py#L1200) | 1200 | `"            b\"Content-Length\","` | — |
| [SRC-3451CC474D-L001201](../../tests/test_api.py#L1201) | 1201 | `"        ),"` | — |
| [SRC-3451CC474D-L001202](../../tests/test_api.py#L1202) | 1202 | `"    ],"` | — |
| [SRC-3451CC474D-L001203](../../tests/test_api.py#L1203) | 1203 | `")"` | — |
| [SRC-3451CC474D-L001204](../../tests/test_api.py#L1204) | 1204 | `"def test_api_rejects_ambiguous_or_unsupported_http_request_framing("` | — |
| [SRC-3451CC474D-L001205](../../tests/test_api.py#L1205) | 1205 | `"    local_api, request_line, framing_headers, body, error_marker"` | — |
| [SRC-3451CC474D-L001206](../../tests/test_api.py#L1206) | 1206 | `"):"` | — |
| [SRC-3451CC474D-L001207](../../tests/test_api.py#L1207) | 1207 | `"    host_port = local_api.rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L001208](../../tests/test_api.py#L1208) | 1208 | `"    with socket.create_connection("` | — |
| [SRC-3451CC474D-L001209](../../tests/test_api.py#L1209) | 1209 | `"        (host_port[0].removeprefix(\"http://\"), int(host_port[1])), timeout=2"` | — |
| [SRC-3451CC474D-L001210](../../tests/test_api.py#L1210) | 1210 | `"    ) as client:"` | — |
| [SRC-3451CC474D-L001211](../../tests/test_api.py#L1211) | 1211 | `"        client.settimeout(2)"` | — |
| [SRC-3451CC474D-L001212](../../tests/test_api.py#L1212) | 1212 | `"        request = ("` | — |
| [SRC-3451CC474D-L001213](../../tests/test_api.py#L1213) | 1213 | `"            request_line.encode(\"ascii\")"` | — |
| [SRC-3451CC474D-L001214](../../tests/test_api.py#L1214) | 1214 | `"            + b\"\\r\\nHost: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L001215](../../tests/test_api.py#L1215) | 1215 | `"            + b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L001216](../../tests/test_api.py#L1216) | 1216 | `"            + framing_headers"` | — |
| [SRC-3451CC474D-L001217](../../tests/test_api.py#L1217) | 1217 | `"            + b\"Connection: close\\r\\n\\r\\n\""` | — |
| [SRC-3451CC474D-L001218](../../tests/test_api.py#L1218) | 1218 | `"            + body"` | — |
| [SRC-3451CC474D-L001219](../../tests/test_api.py#L1219) | 1219 | `"        )"` | — |
| [SRC-3451CC474D-L001220](../../tests/test_api.py#L1220) | 1220 | `"        client.sendall(request)"` | — |
| [SRC-3451CC474D-L001221](../../tests/test_api.py#L1221) | 1221 | `"        response = b\"\""` | — |
| [SRC-3451CC474D-L001222](../../tests/test_api.py#L1222) | 1222 | `"        while True:"` | — |
| [SRC-3451CC474D-L001223](../../tests/test_api.py#L1223) | 1223 | `"            chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L001224](../../tests/test_api.py#L1224) | 1224 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L001225](../../tests/test_api.py#L1225) | 1225 | `"                break"` | — |
| [SRC-3451CC474D-L001226](../../tests/test_api.py#L1226) | 1226 | `"            response += chunk"` | — |
| [SRC-3451CC474D-L001227](../../tests/test_api.py#L1227) | 1227 | `""` | — |
| [SRC-3451CC474D-L001228](../../tests/test_api.py#L1228) | 1228 | `"    assert response.startswith(b\"HTTP/1.0 400\")"` | — |
| [SRC-3451CC474D-L001229](../../tests/test_api.py#L1229) | 1229 | `"    assert error_marker in response"` | — |
| [SRC-3451CC474D-L001230](../../tests/test_api.py#L1230) | 1230 | `"    assert b\"200 OK\" not in response"` | — |
| [SRC-3451CC474D-L001231](../../tests/test_api.py#L1231) | 1231 | `""` | — |
| [SRC-3451CC474D-L001232](../../tests/test_api.py#L1232) | 1232 | `"def test_api_closes_connection_when_declared_body_exceeds_limit(local_api):"` | — |
| [SRC-3451CC474D-L001233](../../tests/test_api.py#L1233) | 1233 | `"    host_port = local_api.rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L001234](../../tests/test_api.py#L1234) | 1234 | `"    with socket.create_connection("` | — |
| [SRC-3451CC474D-L001235](../../tests/test_api.py#L1235) | 1235 | `"        (host_port[0].removeprefix(\"http://\"), int(host_port[1])), timeout=2"` | — |
| [SRC-3451CC474D-L001236](../../tests/test_api.py#L1236) | 1236 | `"    ) as client:"` | — |
| [SRC-3451CC474D-L001237](../../tests/test_api.py#L1237) | 1237 | `"        client.settimeout(2)"` | — |
| [SRC-3451CC474D-L001238](../../tests/test_api.py#L1238) | 1238 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L001239](../../tests/test_api.py#L1239) | 1239 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L001240](../../tests/test_api.py#L1240) | 1240 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L001241](../../tests/test_api.py#L1241) | 1241 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L001242](../../tests/test_api.py#L1242) | 1242 | `"            b\"Content-Length: 200001\\r\\n\""` | — |
| [SRC-3451CC474D-L001243](../../tests/test_api.py#L1243) | 1243 | `"            b\"\\r\\n\""` | — |
| [SRC-3451CC474D-L001244](../../tests/test_api.py#L1244) | 1244 | `"        )"` | — |
| [SRC-3451CC474D-L001245](../../tests/test_api.py#L1245) | 1245 | `"        response = b\"\""` | — |
| [SRC-3451CC474D-L001246](../../tests/test_api.py#L1246) | 1246 | `"        while True:"` | — |
| [SRC-3451CC474D-L001247](../../tests/test_api.py#L1247) | 1247 | `"            chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L001248](../../tests/test_api.py#L1248) | 1248 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L001249](../../tests/test_api.py#L1249) | 1249 | `"                break"` | — |
| [SRC-3451CC474D-L001250](../../tests/test_api.py#L1250) | 1250 | `"            response += chunk"` | — |
| [SRC-3451CC474D-L001251](../../tests/test_api.py#L1251) | 1251 | `""` | — |
| [SRC-3451CC474D-L001252](../../tests/test_api.py#L1252) | 1252 | `"    assert response.startswith(b\"HTTP/1.0 413\")"` | — |
| [SRC-3451CC474D-L001253](../../tests/test_api.py#L1253) | 1253 | `"    assert b\"request too large\" in response"` | — |
| [SRC-3451CC474D-L001254](../../tests/test_api.py#L1254) | 1254 | `""` | — |
| [SRC-3451CC474D-L001255](../../tests/test_api.py#L1255) | 1255 | `""` | — |
| [SRC-3451CC474D-L001256](../../tests/test_api.py#L1256) | 1256 | `""` | — |
| [SRC-3451CC474D-L001257](../../tests/test_api.py#L1257) | 1257 | `"def test_workspace_route_serves_the_arabic_rtl_workspace_shell(local_api):"` | — |
| [SRC-3451CC474D-L001258](../../tests/test_api.py#L1258) | 1258 | `"    with urlopen(local_api + \"/workspace\", timeout=3) as response:"` | — |
| [SRC-3451CC474D-L001259](../../tests/test_api.py#L1259) | 1259 | `"        html = response.read().decode(\"utf-8\")"` | — |
| [SRC-3451CC474D-L001260](../../tests/test_api.py#L1260) | 1260 | `"        assert response.status == 200"` | — |
| [SRC-3451CC474D-L001261](../../tests/test_api.py#L1261) | 1261 | `"        assert response.headers.get_content_type() == \"text/html\""` | — |
| [SRC-3451CC474D-L001262](../../tests/test_api.py#L1262) | 1262 | `""` | — |
| [SRC-3451CC474D-L001263](../../tests/test_api.py#L1263) | 1263 | `"    assert '<html lang=\"ar\" dir=\"rtl\">' in html"` | — |
| [SRC-3451CC474D-L001264](../../tests/test_api.py#L1264) | 1264 | `"    assert 'api(\"/api/session\")' in html"` | — |
| [SRC-3451CC474D-L001265](../../tests/test_api.py#L1265) | 1265 | `"    assert 'api(\"/api/leads?limit=500\")' in html"` | — |
| [SRC-3451CC474D-L001266](../../tests/test_api.py#L1266) | 1266 | `"    assert \"localStorage\" not in html"` | — |
| [SRC-3451CC474D-L001267](../../tests/test_api.py#L1267) | 1267 | `"    assert \"sessionStorage\" not in html"` | — |
| [SRC-3451CC474D-L001268](../../tests/test_api.py#L1268) | 1268 | `""` | — |
| [SRC-3451CC474D-L001269](../../tests/test_api.py#L1269) | 1269 | `"def test_sales_workspace_is_default_home_and_preserves_agent_and_legacy_leads(local_api):"` | — |
| [SRC-3451CC474D-L001270](../../tests/test_api.py#L1270) | 1270 | `"    with urlopen(local_api + \"/\", timeout=3) as response:"` | — |
| [SRC-3451CC474D-L001271](../../tests/test_api.py#L1271) | 1271 | `"        home = response.read().decode(\"utf-8\")"` | — |
| [SRC-3451CC474D-L001272](../../tests/test_api.py#L1272) | 1272 | `"        assert response.status == 200"` | — |
| [SRC-3451CC474D-L001273](../../tests/test_api.py#L1273) | 1273 | `"        assert '<html lang=\"ar\" dir=\"rtl\">' in home"` | — |
| [SRC-3451CC474D-L001274](../../tests/test_api.py#L1274) | 1274 | `"        assert \"OMARAI SECURE WORKSPACE\" in home"` | — |
| [SRC-3451CC474D-L001275](../../tests/test_api.py#L1275) | 1275 | `""` | — |
| [SRC-3451CC474D-L001276](../../tests/test_api.py#L1276) | 1276 | `"    with urlopen(local_api + \"/workspace\", timeout=3) as response:"` | — |
| [SRC-3451CC474D-L001277](../../tests/test_api.py#L1277) | 1277 | `"        workspace = response.read().decode(\"utf-8\")"` | — |
| [SRC-3451CC474D-L001278](../../tests/test_api.py#L1278) | 1278 | `"        assert response.status == 200"` | — |
| [SRC-3451CC474D-L001279](../../tests/test_api.py#L1279) | 1279 | `"        assert workspace == home"` | — |
| [SRC-3451CC474D-L001280](../../tests/test_api.py#L1280) | 1280 | `""` | — |
| [SRC-3451CC474D-L001281](../../tests/test_api.py#L1281) | 1281 | `"    with urlopen(local_api + \"/agent\", timeout=3) as response:"` | — |
| [SRC-3451CC474D-L001282](../../tests/test_api.py#L1282) | 1282 | `"        agent = response.read().decode(\"utf-8\")"` | — |
| [SRC-3451CC474D-L001283](../../tests/test_api.py#L1283) | 1283 | `"        assert response.status == 200"` | — |
| [SRC-3451CC474D-L001284](../../tests/test_api.py#L1284) | 1284 | `"        assert agent != home"` | — |
| [SRC-3451CC474D-L001285](../../tests/test_api.py#L1285) | 1285 | `"        assert \"وكيل البحث الحي والتحليل متعدد المصادر\" in agent"` | — |
| [SRC-3451CC474D-L001286](../../tests/test_api.py#L1286) | 1286 | `""` | — |
| [SRC-3451CC474D-L001287](../../tests/test_api.py#L1287) | 1287 | `"    with urlopen(local_api + \"/leads\", timeout=3) as response:"` | — |
| [SRC-3451CC474D-L001288](../../tests/test_api.py#L1288) | 1288 | `"        leads = response.read().decode(\"utf-8\")"` | — |
| [SRC-3451CC474D-L001289](../../tests/test_api.py#L1289) | 1289 | `"        assert response.status == 200"` | — |
| [SRC-3451CC474D-L001290](../../tests/test_api.py#L1290) | 1290 | `"        assert \"مساعد اكتشاف العملاء\" in leads"` | — |
| [SRC-3451CC474D-L001291](../../tests/test_api.py#L1291) | 1291 | `""` | — |
| [SRC-3451CC474D-L001292](../../tests/test_api.py#L1292) | 1292 | `""` | — |
| [SRC-3451CC474D-L001293](../../tests/test_api.py#L1293) | 1293 | `"def test_product_profile_and_buyer_discovery_api_persist_evidence_and_save_only_qualified_sources("` | — |
| [SRC-3451CC474D-L001294](../../tests/test_api.py#L1294) | 1294 | `"    local_api, monkeypatch"` | — |
| [SRC-3451CC474D-L001295](../../tests/test_api.py#L1295) | 1295 | `"):"` | — |
| [SRC-3451CC474D-L001296](../../tests/test_api.py#L1296) | 1296 | `"    from api.omarai import WebAgent"` | — |
| [SRC-3451CC474D-L001297](../../tests/test_api.py#L1297) | 1297 | `""` | — |
| [SRC-3451CC474D-L001298](../../tests/test_api.py#L1298) | 1298 | `"    captured = {}"` | — |
| [SRC-3451CC474D-L001299](../../tests/test_api.py#L1299) | 1299 | `""` | — |
| [SRC-3451CC474D-L001300](../../tests/test_api.py#L1300) | 1300 | `"    def fake_answer("` | — |
| [SRC-3451CC474D-L001301](../../tests/test_api.py#L1301) | 1301 | `"        self, question, history=None, mode=\"auto\", *, budget_profile=\"default\", buyer_queries=None"` | — |
| [SRC-3451CC474D-L001302](../../tests/test_api.py#L1302) | 1302 | `"    ):"` | — |
| [SRC-3451CC474D-L001303](../../tests/test_api.py#L1303) | 1303 | `"        captured[\"question\"] = question"` | — |
| [SRC-3451CC474D-L001304](../../tests/test_api.py#L1304) | 1304 | `"        captured[\"buyer_queries\"] = buyer_queries"` | — |
| [SRC-3451CC474D-L001305](../../tests/test_api.py#L1305) | 1305 | `"        captured[\"allow_optional_providers\"] = self.allow_optional_providers"` | — |
| [SRC-3451CC474D-L001306](../../tests/test_api.py#L1306) | 1306 | `"        captured[\"openrouter_web_search_enabled\"] = self.openrouter_web_search_enabled"` | — |
| [SRC-3451CC474D-L001307](../../tests/test_api.py#L1307) | 1307 | `"        return {"` | — |
| [SRC-3451CC474D-L001308](../../tests/test_api.py#L1308) | 1308 | `"            \"answer\": \"عُثر على إشارة طلب واحدة.\","` | — |
