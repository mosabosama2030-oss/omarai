# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **036**
- سجلات الأسطر: **800**
- النطاق: SRC-3451CC474D-L000543 إلى SRC-DA61479D59-L000181
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-3451CC474D — [tests/test_api.py](../../tests/test_api.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3451CC474D-L000543](../../tests/test_api.py#L543) | 543 | `"    first_result = {}"` | — |
| [SRC-3451CC474D-L000544](../../tests/test_api.py#L544) | 544 | `""` | — |
| [SRC-3451CC474D-L000545](../../tests/test_api.py#L545) | 545 | `"    def slow_answer(self, question, history=None, mode=\"auto\"):"` | — |
| [SRC-3451CC474D-L000546](../../tests/test_api.py#L546) | 546 | `"        entered.set()"` | — |
| [SRC-3451CC474D-L000547](../../tests/test_api.py#L547) | 547 | `"        assert release.wait(timeout=2), \"test did not release the held research slot\""` | — |
| [SRC-3451CC474D-L000548](../../tests/test_api.py#L548) | 548 | `"        return {"` | — |
| [SRC-3451CC474D-L000549](../../tests/test_api.py#L549) | 549 | `"            \"answer\": \"نتيجة اختبار محدودة\","` | — |
| [SRC-3451CC474D-L000550](../../tests/test_api.py#L550) | 550 | `"            \"question\": question,"` | — |
| [SRC-3451CC474D-L000551](../../tests/test_api.py#L551) | 551 | `"            \"search_query\": question,"` | — |
| [SRC-3451CC474D-L000552](../../tests/test_api.py#L552) | 552 | `"            \"search_queries\": [],"` | — |
| [SRC-3451CC474D-L000553](../../tests/test_api.py#L553) | 553 | `"            \"search_report\": {\"search_attempted\": False, \"search_outcome\": \"not_attempted\"},"` | — |
| [SRC-3451CC474D-L000554](../../tests/test_api.py#L554) | 554 | `"            \"sources\": [],"` | — |
| [SRC-3451CC474D-L000555](../../tests/test_api.py#L555) | 555 | `"            \"used_language_model\": False,"` | — |
| [SRC-3451CC474D-L000556](../../tests/test_api.py#L556) | 556 | `"            \"used_web_search\": False,"` | — |
| [SRC-3451CC474D-L000557](../../tests/test_api.py#L557) | 557 | `"            \"search_attempted\": False,"` | — |
| [SRC-3451CC474D-L000558](../../tests/test_api.py#L558) | 558 | `"            \"used_social_search\": False,"` | — |
| [SRC-3451CC474D-L000559](../../tests/test_api.py#L559) | 559 | `"            \"warnings\": [],"` | — |
| [SRC-3451CC474D-L000560](../../tests/test_api.py#L560) | 560 | `"            \"kind\": \"web_fallback\","` | — |
| [SRC-3451CC474D-L000561](../../tests/test_api.py#L561) | 561 | `"        }"` | — |
| [SRC-3451CC474D-L000562](../../tests/test_api.py#L562) | 562 | `""` | — |
| [SRC-3451CC474D-L000563](../../tests/test_api.py#L563) | 563 | `"    monkeypatch.setattr(WebAgent, \"answer\", slow_answer)"` | — |
| [SRC-3451CC474D-L000564](../../tests/test_api.py#L564) | 564 | `""` | — |
| [SRC-3451CC474D-L000565](../../tests/test_api.py#L565) | 565 | `"    def first_request():"` | — |
| [SRC-3451CC474D-L000566](../../tests/test_api.py#L566) | 566 | `"        first_result[\"response\"] = request_json("` | — |
| [SRC-3451CC474D-L000567](../../tests/test_api.py#L567) | 567 | `"            local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"السؤال الأول\"}"` | — |
| [SRC-3451CC474D-L000568](../../tests/test_api.py#L568) | 568 | `"        )"` | — |
| [SRC-3451CC474D-L000569](../../tests/test_api.py#L569) | 569 | `""` | — |
| [SRC-3451CC474D-L000570](../../tests/test_api.py#L570) | 570 | `"    worker = threading.Thread(target=first_request, daemon=True)"` | — |
| [SRC-3451CC474D-L000571](../../tests/test_api.py#L571) | 571 | `"    worker.start()"` | — |
| [SRC-3451CC474D-L000572](../../tests/test_api.py#L572) | 572 | `"    try:"` | — |
| [SRC-3451CC474D-L000573](../../tests/test_api.py#L573) | 573 | `"        assert entered.wait(timeout=1), \"first request did not acquire the research slot\""` | — |
| [SRC-3451CC474D-L000574](../../tests/test_api.py#L574) | 574 | `"        status, payload = request_json("` | — |
| [SRC-3451CC474D-L000575](../../tests/test_api.py#L575) | 575 | `"            local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"السؤال الثاني\"}"` | — |
| [SRC-3451CC474D-L000576](../../tests/test_api.py#L576) | 576 | `"        )"` | — |
| [SRC-3451CC474D-L000577](../../tests/test_api.py#L577) | 577 | `"        assert status == 503"` | — |
| [SRC-3451CC474D-L000578](../../tests/test_api.py#L578) | 578 | `"        assert payload[\"retry_after_seconds\"] == 5"` | — |
| [SRC-3451CC474D-L000579](../../tests/test_api.py#L579) | 579 | `"        assert \"مشغولة\" in payload[\"error\"]"` | — |
| [SRC-3451CC474D-L000580](../../tests/test_api.py#L580) | 580 | `"    finally:"` | — |
| [SRC-3451CC474D-L000581](../../tests/test_api.py#L581) | 581 | `"        release.set()"` | — |
| [SRC-3451CC474D-L000582](../../tests/test_api.py#L582) | 582 | `"        worker.join(timeout=3)"` | — |
| [SRC-3451CC474D-L000583](../../tests/test_api.py#L583) | 583 | `""` | — |
| [SRC-3451CC474D-L000584](../../tests/test_api.py#L584) | 584 | `"    assert not worker.is_alive()"` | — |
| [SRC-3451CC474D-L000585](../../tests/test_api.py#L585) | 585 | `"    assert first_result[\"response\"][0] == 200"` | — |
| [SRC-3451CC474D-L000586](../../tests/test_api.py#L586) | 586 | `""` | — |
| [SRC-3451CC474D-L000587](../../tests/test_api.py#L587) | 587 | `""` | — |
| [SRC-3451CC474D-L000588](../../tests/test_api.py#L588) | 588 | `"def test_agent_concurrency_limit_has_hard_bounds(monkeypatch):"` | — |
| [SRC-3451CC474D-L000589](../../tests/test_api.py#L589) | 589 | `"    from api.omarai import _configured_agent_concurrency_limit"` | — |
| [SRC-3451CC474D-L000590](../../tests/test_api.py#L590) | 590 | `""` | — |
| [SRC-3451CC474D-L000591](../../tests/test_api.py#L591) | 591 | `"    monkeypatch.setenv(\"OMARAI_MAX_CONCURRENT_AGENT_REQUESTS\", \"99\")"` | — |
| [SRC-3451CC474D-L000592](../../tests/test_api.py#L592) | 592 | `"    assert _configured_agent_concurrency_limit() == 8"` | — |
| [SRC-3451CC474D-L000593](../../tests/test_api.py#L593) | 593 | `"    monkeypatch.setenv(\"OMARAI_MAX_CONCURRENT_AGENT_REQUESTS\", \"invalid\")"` | — |
| [SRC-3451CC474D-L000594](../../tests/test_api.py#L594) | 594 | `"    assert _configured_agent_concurrency_limit() == 4"` | — |
| [SRC-3451CC474D-L000595](../../tests/test_api.py#L595) | 595 | `""` | — |
| [SRC-3451CC474D-L000596](../../tests/test_api.py#L596) | 596 | `""` | — |
| [SRC-3451CC474D-L000597](../../tests/test_api.py#L597) | 597 | `"def test_api_rejects_oversized_request_body(local_api):"` | — |
| [SRC-3451CC474D-L000598](../../tests/test_api.py#L598) | 598 | `"    status, payload = request_json("` | — |
| [SRC-3451CC474D-L000599](../../tests/test_api.py#L599) | 599 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000600](../../tests/test_api.py#L600) | 600 | `"        \"/api/analyze\","` | — |
| [SRC-3451CC474D-L000601](../../tests/test_api.py#L601) | 601 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000602](../../tests/test_api.py#L602) | 602 | `"        payload={\"text\": \"x\" * 200_001},"` | — |
| [SRC-3451CC474D-L000603](../../tests/test_api.py#L603) | 603 | `"    )"` | — |
| [SRC-3451CC474D-L000604](../../tests/test_api.py#L604) | 604 | `""` | — |
| [SRC-3451CC474D-L000605](../../tests/test_api.py#L605) | 605 | `"    assert status == 413"` | — |
| [SRC-3451CC474D-L000606](../../tests/test_api.py#L606) | 606 | `"    assert payload[\"error\"] == \"request too large\""` | — |
| [SRC-3451CC474D-L000607](../../tests/test_api.py#L607) | 607 | `""` | — |
| [SRC-3451CC474D-L000608](../../tests/test_api.py#L608) | 608 | `""` | — |
| [SRC-3451CC474D-L000609](../../tests/test_api.py#L609) | 609 | `"def test_api_rejects_malformed_content_length(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000610](../../tests/test_api.py#L610) | 610 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000611](../../tests/test_api.py#L611) | 611 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000612](../../tests/test_api.py#L612) | 612 | `"    host_port = local_api.rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000613](../../tests/test_api.py#L613) | 613 | `"    with socket.create_connection((host_port[0].removeprefix(\"http://\"), int(host_port[1])), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000614](../../tests/test_api.py#L614) | 614 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000615](../../tests/test_api.py#L615) | 615 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000616](../../tests/test_api.py#L616) | 616 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000617](../../tests/test_api.py#L617) | 617 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000618](../../tests/test_api.py#L618) | 618 | `"            b\"Content-Length: invalid\\r\\n\""` | — |
| [SRC-3451CC474D-L000619](../../tests/test_api.py#L619) | 619 | `"            b\"Connection: close\\r\\n\\r\\n\""` | — |
| [SRC-3451CC474D-L000620](../../tests/test_api.py#L620) | 620 | `"        )"` | — |
| [SRC-3451CC474D-L000621](../../tests/test_api.py#L621) | 621 | `"        response = b\"\""` | — |
| [SRC-3451CC474D-L000622](../../tests/test_api.py#L622) | 622 | `"        while True:"` | — |
| [SRC-3451CC474D-L000623](../../tests/test_api.py#L623) | 623 | `"            chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000624](../../tests/test_api.py#L624) | 624 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000625](../../tests/test_api.py#L625) | 625 | `"                break"` | — |
| [SRC-3451CC474D-L000626](../../tests/test_api.py#L626) | 626 | `"            response += chunk"` | — |
| [SRC-3451CC474D-L000627](../../tests/test_api.py#L627) | 627 | `""` | — |
| [SRC-3451CC474D-L000628](../../tests/test_api.py#L628) | 628 | `"    assert response.startswith(b\"HTTP/1.0 400\")"` | — |
| [SRC-3451CC474D-L000629](../../tests/test_api.py#L629) | 629 | `"    assert b\"valid Content-Length is required\" in response"` | — |
| [SRC-3451CC474D-L000630](../../tests/test_api.py#L630) | 630 | `""` | — |
| [SRC-3451CC474D-L000631](../../tests/test_api.py#L631) | 631 | `""` | — |
| [SRC-3451CC474D-L000632](../../tests/test_api.py#L632) | 632 | `"def test_api_returns_408_when_request_body_read_times_out(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000633](../../tests/test_api.py#L633) | 633 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000634](../../tests/test_api.py#L634) | 634 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000635](../../tests/test_api.py#L635) | 635 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_BODY_READ_TIMEOUT_SECONDS\", 0.1)"` | — |
| [SRC-3451CC474D-L000636](../../tests/test_api.py#L636) | 636 | `"    host_port = local_api.rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000637](../../tests/test_api.py#L637) | 637 | `"    with socket.create_connection((host_port[0].removeprefix(\"http://\"), int(host_port[1])), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000638](../../tests/test_api.py#L638) | 638 | `"        client.settimeout(2)"` | — |
| [SRC-3451CC474D-L000639](../../tests/test_api.py#L639) | 639 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000640](../../tests/test_api.py#L640) | 640 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000641](../../tests/test_api.py#L641) | 641 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000642](../../tests/test_api.py#L642) | 642 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000643](../../tests/test_api.py#L643) | 643 | `"            b\"Content-Length: 40\\r\\n\""` | — |
| [SRC-3451CC474D-L000644](../../tests/test_api.py#L644) | 644 | `"            b\"Connection: close\\r\\n\\r\\n\""` | — |
| [SRC-3451CC474D-L000645](../../tests/test_api.py#L645) | 645 | `"            b\"{}\""` | — |
| [SRC-3451CC474D-L000646](../../tests/test_api.py#L646) | 646 | `"        )"` | — |
| [SRC-3451CC474D-L000647](../../tests/test_api.py#L647) | 647 | `"        response = b\"\""` | — |
| [SRC-3451CC474D-L000648](../../tests/test_api.py#L648) | 648 | `"        while True:"` | — |
| [SRC-3451CC474D-L000649](../../tests/test_api.py#L649) | 649 | `"            chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000650](../../tests/test_api.py#L650) | 650 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000651](../../tests/test_api.py#L651) | 651 | `"                break"` | — |
| [SRC-3451CC474D-L000652](../../tests/test_api.py#L652) | 652 | `"            response += chunk"` | — |
| [SRC-3451CC474D-L000653](../../tests/test_api.py#L653) | 653 | `""` | — |
| [SRC-3451CC474D-L000654](../../tests/test_api.py#L654) | 654 | `"    assert response.startswith(b\"HTTP/1.0 408\")"` | — |
| [SRC-3451CC474D-L000655](../../tests/test_api.py#L655) | 655 | `"    assert b\"request body read timed out\" in response"` | — |
| [SRC-3451CC474D-L000656](../../tests/test_api.py#L656) | 656 | `""` | — |
| [SRC-3451CC474D-L000657](../../tests/test_api.py#L657) | 657 | `""` | — |
| [SRC-3451CC474D-L000658](../../tests/test_api.py#L658) | 658 | `"def test_api_absolute_body_deadline_stops_slow_trickle(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000659](../../tests/test_api.py#L659) | 659 | `"    \"\"\"A client must not evade the total deadline by sending before each idle timeout.\"\"\""` | — |
| [SRC-3451CC474D-L000660](../../tests/test_api.py#L660) | 660 | `"    import time"` | — |
| [SRC-3451CC474D-L000661](../../tests/test_api.py#L661) | 661 | `""` | — |
| [SRC-3451CC474D-L000662](../../tests/test_api.py#L662) | 662 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000663](../../tests/test_api.py#L663) | 663 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000664](../../tests/test_api.py#L664) | 664 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_BODY_READ_TIMEOUT_SECONDS\", 0.45)"` | — |
| [SRC-3451CC474D-L000665](../../tests/test_api.py#L665) | 665 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_BODY_IDLE_TIMEOUT_SECONDS\", 0.20)"` | — |
| [SRC-3451CC474D-L000666](../../tests/test_api.py#L666) | 666 | `"    host, port = local_api.removeprefix(\"http://\").rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000667](../../tests/test_api.py#L667) | 667 | `""` | — |
| [SRC-3451CC474D-L000668](../../tests/test_api.py#L668) | 668 | `"    with socket.create_connection((host, int(port)), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000669](../../tests/test_api.py#L669) | 669 | `"        client.settimeout(2)"` | — |
| [SRC-3451CC474D-L000670](../../tests/test_api.py#L670) | 670 | `"        started = time.monotonic()"` | — |
| [SRC-3451CC474D-L000671](../../tests/test_api.py#L671) | 671 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000672](../../tests/test_api.py#L672) | 672 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000673](../../tests/test_api.py#L673) | 673 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000674](../../tests/test_api.py#L674) | 674 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000675](../../tests/test_api.py#L675) | 675 | `"            b\"Content-Length: 100\\r\\n\""` | — |
| [SRC-3451CC474D-L000676](../../tests/test_api.py#L676) | 676 | `"            b\"Connection: close\\r\\n\\r\\n\""` | — |
| [SRC-3451CC474D-L000677](../../tests/test_api.py#L677) | 677 | `"            b\"{\""` | — |
| [SRC-3451CC474D-L000678](../../tests/test_api.py#L678) | 678 | `"        )"` | — |
| [SRC-3451CC474D-L000679](../../tests/test_api.py#L679) | 679 | `"        # Each fragment arrives before the 0.20s idle timeout, but the complete"` | — |
| [SRC-3451CC474D-L000680](../../tests/test_api.py#L680) | 680 | `"        # request body never arrives before the 0.45s absolute deadline."` | — |
| [SRC-3451CC474D-L000681](../../tests/test_api.py#L681) | 681 | `"        for fragment in (b'\"', b\"text\", b'\"', b\":\"):"` | — |
| [SRC-3451CC474D-L000682](../../tests/test_api.py#L682) | 682 | `"            time.sleep(0.08)"` | — |
| [SRC-3451CC474D-L000683](../../tests/test_api.py#L683) | 683 | `"            try:"` | — |
| [SRC-3451CC474D-L000684](../../tests/test_api.py#L684) | 684 | `"                client.sendall(fragment)"` | — |
| [SRC-3451CC474D-L000685](../../tests/test_api.py#L685) | 685 | `"            except OSError:"` | — |
| [SRC-3451CC474D-L000686](../../tests/test_api.py#L686) | 686 | `"                break"` | — |
| [SRC-3451CC474D-L000687](../../tests/test_api.py#L687) | 687 | `""` | — |
| [SRC-3451CC474D-L000688](../../tests/test_api.py#L688) | 688 | `"        response = bytearray()"` | — |
| [SRC-3451CC474D-L000689](../../tests/test_api.py#L689) | 689 | `"        while True:"` | — |
| [SRC-3451CC474D-L000690](../../tests/test_api.py#L690) | 690 | `"            try:"` | — |
| [SRC-3451CC474D-L000691](../../tests/test_api.py#L691) | 691 | `"                chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000692](../../tests/test_api.py#L692) | 692 | `"            except TimeoutError:"` | — |
| [SRC-3451CC474D-L000693](../../tests/test_api.py#L693) | 693 | `"                break"` | — |
| [SRC-3451CC474D-L000694](../../tests/test_api.py#L694) | 694 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000695](../../tests/test_api.py#L695) | 695 | `"                break"` | — |
| [SRC-3451CC474D-L000696](../../tests/test_api.py#L696) | 696 | `"            response.extend(chunk)"` | — |
| [SRC-3451CC474D-L000697](../../tests/test_api.py#L697) | 697 | `""` | — |
| [SRC-3451CC474D-L000698](../../tests/test_api.py#L698) | 698 | `"    elapsed = time.monotonic() - started"` | — |
| [SRC-3451CC474D-L000699](../../tests/test_api.py#L699) | 699 | `"    assert response.startswith(b\"HTTP/1.0 408\")"` | — |
| [SRC-3451CC474D-L000700](../../tests/test_api.py#L700) | 700 | `"    assert b\"request body read timed out\" in response"` | — |
| [SRC-3451CC474D-L000701](../../tests/test_api.py#L701) | 701 | `"    assert elapsed < 1.5"` | — |
| [SRC-3451CC474D-L000702](../../tests/test_api.py#L702) | 702 | `""` | — |
| [SRC-3451CC474D-L000703](../../tests/test_api.py#L703) | 703 | `""` | — |
| [SRC-3451CC474D-L000704](../../tests/test_api.py#L704) | 704 | `""` | — |
| [SRC-3451CC474D-L000705](../../tests/test_api.py#L705) | 705 | `"def test_api_absolute_header_deadline_stops_slow_trickle(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000706](../../tests/test_api.py#L706) | 706 | `"    \"\"\"Header bytes arriving before idle timeout must not extend the total deadline.\"\"\""` | — |
| [SRC-3451CC474D-L000707](../../tests/test_api.py#L707) | 707 | `"    import time"` | — |
| [SRC-3451CC474D-L000708](../../tests/test_api.py#L708) | 708 | `""` | — |
| [SRC-3451CC474D-L000709](../../tests/test_api.py#L709) | 709 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000710](../../tests/test_api.py#L710) | 710 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000711](../../tests/test_api.py#L711) | 711 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_HEADER_READ_TIMEOUT_SECONDS\", 0.5)"` | — |
| [SRC-3451CC474D-L000712](../../tests/test_api.py#L712) | 712 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_HEADER_IDLE_TIMEOUT_SECONDS\", 0.35)"` | — |
| [SRC-3451CC474D-L000713](../../tests/test_api.py#L713) | 713 | `"    host, port = local_api.removeprefix(\"http://\").rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000714](../../tests/test_api.py#L714) | 714 | `""` | — |
| [SRC-3451CC474D-L000715](../../tests/test_api.py#L715) | 715 | `"    with socket.create_connection((host, int(port)), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000716](../../tests/test_api.py#L716) | 716 | `"        client.settimeout(1.2)"` | — |
| [SRC-3451CC474D-L000717](../../tests/test_api.py#L717) | 717 | `"        started = time.monotonic()"` | — |
| [SRC-3451CC474D-L000718](../../tests/test_api.py#L718) | 718 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000719](../../tests/test_api.py#L719) | 719 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000720](../../tests/test_api.py#L720) | 720 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000721](../../tests/test_api.py#L721) | 721 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000722](../../tests/test_api.py#L722) | 722 | `"            b\"Content-Length: 40\\r\\n\""` | — |
| [SRC-3451CC474D-L000723](../../tests/test_api.py#L723) | 723 | `"            b\"X-Slow: \""` | — |
| [SRC-3451CC474D-L000724](../../tests/test_api.py#L724) | 724 | `"        )"` | — |
| [SRC-3451CC474D-L000725](../../tests/test_api.py#L725) | 725 | `"        # Each tiny fragment is sent well before the 0.35s idle timeout. No"` | — |
| [SRC-3451CC474D-L000726](../../tests/test_api.py#L726) | 726 | `"        # newline completes X-Slow, so only an absolute header deadline can stop it."` | — |
| [SRC-3451CC474D-L000727](../../tests/test_api.py#L727) | 727 | `"        for fragment in (b\"a\", b\"b\", b\"c\", b\"d\", b\"e\", b\"f\", b\"g\", b\"h\", b\"i\"):"` | — |
| [SRC-3451CC474D-L000728](../../tests/test_api.py#L728) | 728 | `"            time.sleep(0.12)"` | — |
| [SRC-3451CC474D-L000729](../../tests/test_api.py#L729) | 729 | `"            try:"` | — |
| [SRC-3451CC474D-L000730](../../tests/test_api.py#L730) | 730 | `"                client.sendall(fragment)"` | — |
| [SRC-3451CC474D-L000731](../../tests/test_api.py#L731) | 731 | `"            except OSError:"` | — |
| [SRC-3451CC474D-L000732](../../tests/test_api.py#L732) | 732 | `"                break"` | — |
| [SRC-3451CC474D-L000733](../../tests/test_api.py#L733) | 733 | `""` | — |
| [SRC-3451CC474D-L000734](../../tests/test_api.py#L734) | 734 | `"        response = bytearray()"` | — |
| [SRC-3451CC474D-L000735](../../tests/test_api.py#L735) | 735 | `"        while True:"` | — |
| [SRC-3451CC474D-L000736](../../tests/test_api.py#L736) | 736 | `"            try:"` | — |
| [SRC-3451CC474D-L000737](../../tests/test_api.py#L737) | 737 | `"                chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000738](../../tests/test_api.py#L738) | 738 | `"            except TimeoutError:"` | — |
| [SRC-3451CC474D-L000739](../../tests/test_api.py#L739) | 739 | `"                break"` | — |
| [SRC-3451CC474D-L000740](../../tests/test_api.py#L740) | 740 | `"            except OSError:"` | — |
| [SRC-3451CC474D-L000741](../../tests/test_api.py#L741) | 741 | `"                break"` | — |
| [SRC-3451CC474D-L000742](../../tests/test_api.py#L742) | 742 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000743](../../tests/test_api.py#L743) | 743 | `"                break"` | — |
| [SRC-3451CC474D-L000744](../../tests/test_api.py#L744) | 744 | `"            response.extend(chunk)"` | — |
| [SRC-3451CC474D-L000745](../../tests/test_api.py#L745) | 745 | `"        elapsed = time.monotonic() - started"` | — |
| [SRC-3451CC474D-L000746](../../tests/test_api.py#L746) | 746 | `""` | — |
| [SRC-3451CC474D-L000747](../../tests/test_api.py#L747) | 747 | `"    assert elapsed < 0.8"` | — |
| [SRC-3451CC474D-L000748](../../tests/test_api.py#L748) | 748 | `"    # The timed-out request never reached application dispatch; the handler closes silently."` | — |
| [SRC-3451CC474D-L000749](../../tests/test_api.py#L749) | 749 | `"    assert response == b\"\""` | — |
| [SRC-3451CC474D-L000750](../../tests/test_api.py#L750) | 750 | `""` | — |
| [SRC-3451CC474D-L000751](../../tests/test_api.py#L751) | 751 | `"def test_public_preflight_does_not_trust_spoofed_forwarded_host(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000752](../../tests/test_api.py#L752) | 752 | `"    \"\"\"A client-controlled X-Forwarded-Host must not grant an origin CORS access.\"\"\""` | — |
| [SRC-3451CC474D-L000753](../../tests/test_api.py#L753) | 753 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000754](../../tests/test_api.py#L754) | 754 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000755](../../tests/test_api.py#L755) | 755 | `""` | — |
| [SRC-3451CC474D-L000756](../../tests/test_api.py#L756) | 756 | `"    request = Request("` | — |
| [SRC-3451CC474D-L000757](../../tests/test_api.py#L757) | 757 | `"        local_api + \"/api/agent\","` | — |
| [SRC-3451CC474D-L000758](../../tests/test_api.py#L758) | 758 | `"        method=\"OPTIONS\","` | — |
| [SRC-3451CC474D-L000759](../../tests/test_api.py#L759) | 759 | `"        headers={"` | — |
| [SRC-3451CC474D-L000760](../../tests/test_api.py#L760) | 760 | `"            \"Origin\": \"https://attacker.example\","` | — |
| [SRC-3451CC474D-L000761](../../tests/test_api.py#L761) | 761 | `"            \"X-Forwarded-Host\": \"attacker.example\","` | — |
| [SRC-3451CC474D-L000762](../../tests/test_api.py#L762) | 762 | `"            \"X-Forwarded-Proto\": \"https\","` | — |
| [SRC-3451CC474D-L000763](../../tests/test_api.py#L763) | 763 | `"            \"Access-Control-Request-Method\": \"POST\","` | — |
| [SRC-3451CC474D-L000764](../../tests/test_api.py#L764) | 764 | `"            \"Access-Control-Request-Headers\": \"authorization,content-type\","` | — |
| [SRC-3451CC474D-L000765](../../tests/test_api.py#L765) | 765 | `"        },"` | — |
| [SRC-3451CC474D-L000766](../../tests/test_api.py#L766) | 766 | `"    )"` | — |
| [SRC-3451CC474D-L000767](../../tests/test_api.py#L767) | 767 | `"    with pytest.raises(HTTPError) as error:"` | — |
| [SRC-3451CC474D-L000768](../../tests/test_api.py#L768) | 768 | `"        urlopen(request, timeout=3)"` | — |
| [SRC-3451CC474D-L000769](../../tests/test_api.py#L769) | 769 | `"    assert error.value.code == 403"` | — |
| [SRC-3451CC474D-L000770](../../tests/test_api.py#L770) | 770 | `""` | — |
| [SRC-3451CC474D-L000771](../../tests/test_api.py#L771) | 771 | `""` | — |
| [SRC-3451CC474D-L000772](../../tests/test_api.py#L772) | 772 | `"def test_public_origin_still_allows_the_requested_host(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000773](../../tests/test_api.py#L773) | 773 | `"    \"\"\"Same-service public UI remains compatible when the request Host is trusted.\"\"\""` | — |
| [SRC-3451CC474D-L000774](../../tests/test_api.py#L774) | 774 | `"    from types import SimpleNamespace"` | — |
| [SRC-3451CC474D-L000775](../../tests/test_api.py#L775) | 775 | `""` | — |
| [SRC-3451CC474D-L000776](../../tests/test_api.py#L776) | 776 | `"    from api.omarai import Handler"` | — |
| [SRC-3451CC474D-L000777](../../tests/test_api.py#L777) | 777 | `""` | — |
| [SRC-3451CC474D-L000778](../../tests/test_api.py#L778) | 778 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000779](../../tests/test_api.py#L779) | 779 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000780](../../tests/test_api.py#L780) | 780 | `"    handler = SimpleNamespace("` | — |
| [SRC-3451CC474D-L000781](../../tests/test_api.py#L781) | 781 | `"        headers={"` | — |
| [SRC-3451CC474D-L000782](../../tests/test_api.py#L782) | 782 | `"            \"Host\": \"omarai.example\","` | — |
| [SRC-3451CC474D-L000783](../../tests/test_api.py#L783) | 783 | `"            \"X-Forwarded-Proto\": \"https\","` | — |
| [SRC-3451CC474D-L000784](../../tests/test_api.py#L784) | 784 | `"            \"X-Forwarded-Host\": \"attacker.example\","` | — |
| [SRC-3451CC474D-L000785](../../tests/test_api.py#L785) | 785 | `"        }"` | — |
| [SRC-3451CC474D-L000786](../../tests/test_api.py#L786) | 786 | `"    )"` | — |
| [SRC-3451CC474D-L000787](../../tests/test_api.py#L787) | 787 | `"    allowed = Handler._allowed_origins(handler)"` | — |
| [SRC-3451CC474D-L000788](../../tests/test_api.py#L788) | 788 | `"    assert \"https://omarai.example\" in allowed"` | — |
| [SRC-3451CC474D-L000789](../../tests/test_api.py#L789) | 789 | `"    assert \"https://attacker.example\" not in allowed"` | — |
| [SRC-3451CC474D-L000790](../../tests/test_api.py#L790) | 790 | `""` | — |
| [SRC-3451CC474D-L000791](../../tests/test_api.py#L791) | 791 | `""` | — |
| [SRC-3451CC474D-L000792](../../tests/test_api.py#L792) | 792 | `""` | — |
| [SRC-3451CC474D-L000793](../../tests/test_api.py#L793) | 793 | `"def test_security_headers_apply_to_json_and_html_responses(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000794](../../tests/test_api.py#L794) | 794 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000795](../../tests/test_api.py#L795) | 795 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000796](../../tests/test_api.py#L796) | 796 | `"    for path in (\"/api/health\", \"/\"):"` | — |
| [SRC-3451CC474D-L000797](../../tests/test_api.py#L797) | 797 | `"        request = Request(local_api + path)"` | — |
| [SRC-3451CC474D-L000798](../../tests/test_api.py#L798) | 798 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000799](../../tests/test_api.py#L799) | 799 | `"            headers = {name.lower(): value for name, value in response.headers.items()}"` | — |
| [SRC-3451CC474D-L000800](../../tests/test_api.py#L800) | 800 | `"            assert headers[\"x-content-type-options\"] == \"nosniff\""` | — |
| [SRC-3451CC474D-L000801](../../tests/test_api.py#L801) | 801 | `"            assert headers[\"x-frame-options\"] == \"DENY\""` | — |
| [SRC-3451CC474D-L000802](../../tests/test_api.py#L802) | 802 | `"            assert headers[\"referrer-policy\"] == \"strict-origin-when-cross-origin\""` | — |
| [SRC-3451CC474D-L000803](../../tests/test_api.py#L803) | 803 | `"            assert \"default-src 'self'\" in headers[\"content-security-policy\"]"` | — |
| [SRC-3451CC474D-L000804](../../tests/test_api.py#L804) | 804 | `"            policy = headers[\"content-security-policy\"]"` | — |
| [SRC-3451CC474D-L000805](../../tests/test_api.py#L805) | 805 | `"            assert \"frame-ancestors 'none'\" in policy"` | — |
| [SRC-3451CC474D-L000806](../../tests/test_api.py#L806) | 806 | `"            assert \"'unsafe-inline'\" not in policy"` | — |
| [SRC-3451CC474D-L000807](../../tests/test_api.py#L807) | 807 | `"            assert \"'sha256-\" in policy"` | — |
| [SRC-3451CC474D-L000808](../../tests/test_api.py#L808) | 808 | `"            assert headers[\"permissions-policy\"] == ("` | — |
| [SRC-3451CC474D-L000809](../../tests/test_api.py#L809) | 809 | `"                \"camera=(), microphone=(), geolocation=()\""` | — |
| [SRC-3451CC474D-L000810](../../tests/test_api.py#L810) | 810 | `"            )"` | — |
| [SRC-3451CC474D-L000811](../../tests/test_api.py#L811) | 811 | `""` | — |
| [SRC-3451CC474D-L000812](../../tests/test_api.py#L812) | 812 | `""` | — |
| [SRC-3451CC474D-L000813](../../tests/test_api.py#L813) | 813 | `"def test_health_exposes_only_validated_image_baked_sha(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L000814](../../tests/test_api.py#L814) | 814 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000815](../../tests/test_api.py#L815) | 815 | `""` | — |
| [SRC-3451CC474D-L000816](../../tests/test_api.py#L816) | 816 | `"    build_sha_file = tmp_path / \"BUILD_SHA\""` | — |
| [SRC-3451CC474D-L000817](../../tests/test_api.py#L817) | 817 | `"    monkeypatch.setattr(api_module, \"BUILD_SHA_FILE\", build_sha_file)"` | — |
| [SRC-3451CC474D-L000818](../../tests/test_api.py#L818) | 818 | `"    assert api_module._build_sha() == \"unknown\""` | — |
| [SRC-3451CC474D-L000819](../../tests/test_api.py#L819) | 819 | `"    build_sha_file.write_text(\"a\" * 40, encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000820](../../tests/test_api.py#L820) | 820 | `"    assert api_module._build_sha() == \"a\" * 40"` | — |
| [SRC-3451CC474D-L000821](../../tests/test_api.py#L821) | 821 | `"    build_sha_file.write_text(\"not-a-git-sha\", encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000822](../../tests/test_api.py#L822) | 822 | `"    assert api_module._build_sha() == \"unknown\""` | — |
| [SRC-3451CC474D-L000823](../../tests/test_api.py#L823) | 823 | `""` | — |
| [SRC-3451CC474D-L000824](../../tests/test_api.py#L824) | 824 | `""` | — |
| [SRC-3451CC474D-L000825](../../tests/test_api.py#L825) | 825 | `""` | — |
| [SRC-3451CC474D-L000826](../../tests/test_api.py#L826) | 826 | `"@pytest.mark.parametrize("` | — |
| [SRC-3451CC474D-L000827](../../tests/test_api.py#L827) | 827 | `"    (\"variable\", \"source\"),"` | — |
| [SRC-3451CC474D-L000828](../../tests/test_api.py#L828) | 828 | `"    ["` | — |
| [SRC-3451CC474D-L000829](../../tests/test_api.py#L829) | 829 | `"        (\"RAILWAY_GIT_COMMIT_SHA\", \"platform:railway\"),"` | — |
| [SRC-3451CC474D-L000830](../../tests/test_api.py#L830) | 830 | `"        (\"RENDER_GIT_COMMIT\", \"platform:render\"),"` | — |
| [SRC-3451CC474D-L000831](../../tests/test_api.py#L831) | 831 | `"    ],"` | — |
| [SRC-3451CC474D-L000832](../../tests/test_api.py#L832) | 832 | `")"` | — |
| [SRC-3451CC474D-L000833](../../tests/test_api.py#L833) | 833 | `"def test_build_identity_uses_validated_platform_commit_when_image_sha_is_unavailable("` | — |
| [SRC-3451CC474D-L000834](../../tests/test_api.py#L834) | 834 | `"    monkeypatch, tmp_path, variable, source"` | — |
| [SRC-3451CC474D-L000835](../../tests/test_api.py#L835) | 835 | `"):"` | — |
| [SRC-3451CC474D-L000836](../../tests/test_api.py#L836) | 836 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000837](../../tests/test_api.py#L837) | 837 | `""` | — |
| [SRC-3451CC474D-L000838](../../tests/test_api.py#L838) | 838 | `"    build_sha_file = tmp_path / \"BUILD_SHA\""` | — |
| [SRC-3451CC474D-L000839](../../tests/test_api.py#L839) | 839 | `"    monkeypatch.setattr(api_module, \"BUILD_SHA_FILE\", build_sha_file)"` | — |
| [SRC-3451CC474D-L000840](../../tests/test_api.py#L840) | 840 | `"    build_sha_file.write_text(\"unknown\", encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000841](../../tests/test_api.py#L841) | 841 | `"    for name, _label in api_module._PLATFORM_BUILD_SHA_ENVIRONMENTS:"` | — |
| [SRC-3451CC474D-L000842](../../tests/test_api.py#L842) | 842 | `"        monkeypatch.delenv(name, raising=False)"` | — |
| [SRC-3451CC474D-L000843](../../tests/test_api.py#L843) | 843 | `"    monkeypatch.setenv(variable, \"b\" * 40)"` | — |
| [SRC-3451CC474D-L000844](../../tests/test_api.py#L844) | 844 | `""` | — |
| [SRC-3451CC474D-L000845](../../tests/test_api.py#L845) | 845 | `"    assert api_module._build_identity() == (\"b\" * 40, source)"` | — |
| [SRC-3451CC474D-L000846](../../tests/test_api.py#L846) | 846 | `""` | — |
| [SRC-3451CC474D-L000847](../../tests/test_api.py#L847) | 847 | `""` | — |
| [SRC-3451CC474D-L000848](../../tests/test_api.py#L848) | 848 | `"def test_invalid_platform_commit_does_not_create_build_identity(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L000849](../../tests/test_api.py#L849) | 849 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000850](../../tests/test_api.py#L850) | 850 | `""` | — |
| [SRC-3451CC474D-L000851](../../tests/test_api.py#L851) | 851 | `"    monkeypatch.setattr(api_module, \"BUILD_SHA_FILE\", tmp_path / \"BUILD_SHA\")"` | — |
| [SRC-3451CC474D-L000852](../../tests/test_api.py#L852) | 852 | `"    api_module.BUILD_SHA_FILE.write_text(\"unknown\", encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000853](../../tests/test_api.py#L853) | 853 | `"    monkeypatch.setenv(\"RAILWAY_GIT_COMMIT_SHA\", \"not-a-sha\")"` | — |
| [SRC-3451CC474D-L000854](../../tests/test_api.py#L854) | 854 | `"    monkeypatch.setenv(\"RENDER_GIT_COMMIT\", \"also-not-a-sha\")"` | — |
| [SRC-3451CC474D-L000855](../../tests/test_api.py#L855) | 855 | `""` | — |
| [SRC-3451CC474D-L000856](../../tests/test_api.py#L856) | 856 | `"    assert api_module._build_identity() == (\"unknown\", \"unknown\")"` | — |
| [SRC-3451CC474D-L000857](../../tests/test_api.py#L857) | 857 | `""` | — |
| [SRC-3451CC474D-L000858](../../tests/test_api.py#L858) | 858 | `""` | — |
| [SRC-3451CC474D-L000859](../../tests/test_api.py#L859) | 859 | `""` | — |
| [SRC-3451CC474D-L000860](../../tests/test_api.py#L860) | 860 | `"def test_lead_store_uses_configured_database_path(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L000861](../../tests/test_api.py#L861) | 861 | `"    from api.omarai import _lead_store_from_environment"` | — |
| [SRC-3451CC474D-L000862](../../tests/test_api.py#L862) | 862 | `""` | — |
| [SRC-3451CC474D-L000863](../../tests/test_api.py#L863) | 863 | `"    database_path = tmp_path / \"persistent\" / \"omarai.sqlite3\""` | — |
| [SRC-3451CC474D-L000864](../../tests/test_api.py#L864) | 864 | `"    monkeypatch.setenv(\"OMARAI_DB_PATH\", str(database_path))"` | — |
| [SRC-3451CC474D-L000865](../../tests/test_api.py#L865) | 865 | `""` | — |
| [SRC-3451CC474D-L000866](../../tests/test_api.py#L866) | 866 | `"    store = _lead_store_from_environment()"` | — |
| [SRC-3451CC474D-L000867](../../tests/test_api.py#L867) | 867 | `""` | — |
| [SRC-3451CC474D-L000868](../../tests/test_api.py#L868) | 868 | `"    assert store.path == database_path"` | — |
| [SRC-3451CC474D-L000869](../../tests/test_api.py#L869) | 869 | `"    assert database_path.is_file()"` | — |
| [SRC-3451CC474D-L000870](../../tests/test_api.py#L870) | 870 | `""` | — |
| [SRC-3451CC474D-L000871](../../tests/test_api.py#L871) | 871 | `""` | — |
| [SRC-3451CC474D-L000872](../../tests/test_api.py#L872) | 872 | `""` | — |
| [SRC-3451CC474D-L000873](../../tests/test_api.py#L873) | 873 | `"def test_agent_concurrency_slot_released_after_operation_error(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000874](../../tests/test_api.py#L874) | 874 | `"    from api.omarai import WebAgent"` | — |
| [SRC-3451CC474D-L000875](../../tests/test_api.py#L875) | 875 | `""` | — |
| [SRC-3451CC474D-L000876](../../tests/test_api.py#L876) | 876 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000877](../../tests/test_api.py#L877) | 877 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000878](../../tests/test_api.py#L878) | 878 | `"    monkeypatch.setattr(Handler, \"_request_times\", defaultdict(deque))"` | — |
| [SRC-3451CC474D-L000879](../../tests/test_api.py#L879) | 879 | `"    monkeypatch.setattr(Handler, \"_rate_last_cleanup\", 0.0)"` | — |
| [SRC-3451CC474D-L000880](../../tests/test_api.py#L880) | 880 | `"    monkeypatch.setattr(Handler, \"_agent_semaphore\", threading.BoundedSemaphore(1))"` | — |
| [SRC-3451CC474D-L000881](../../tests/test_api.py#L881) | 881 | `"    state = {\"fail\": True}"` | — |
| [SRC-3451CC474D-L000882](../../tests/test_api.py#L882) | 882 | `""` | — |
| [SRC-3451CC474D-L000883](../../tests/test_api.py#L883) | 883 | `"    def answer_with_one_transient_failure(self, question, history=None, mode=\"auto\"):"` | — |
| [SRC-3451CC474D-L000884](../../tests/test_api.py#L884) | 884 | `"        if state[\"fail\"]:"` | — |
| [SRC-3451CC474D-L000885](../../tests/test_api.py#L885) | 885 | `"            raise RuntimeError(\"synthetic operation failure\")"` | — |
| [SRC-3451CC474D-L000886](../../tests/test_api.py#L886) | 886 | `"        return {"` | — |
| [SRC-3451CC474D-L000887](../../tests/test_api.py#L887) | 887 | `"            \"answer\": \"اختبار ناجح\","` | — |
| [SRC-3451CC474D-L000888](../../tests/test_api.py#L888) | 888 | `"            \"question\": question,"` | — |
| [SRC-3451CC474D-L000889](../../tests/test_api.py#L889) | 889 | `"            \"search_query\": question,"` | — |
| [SRC-3451CC474D-L000890](../../tests/test_api.py#L890) | 890 | `"            \"search_queries\": [],"` | — |
| [SRC-3451CC474D-L000891](../../tests/test_api.py#L891) | 891 | `"            \"search_report\": {"` | — |
| [SRC-3451CC474D-L000892](../../tests/test_api.py#L892) | 892 | `"                \"search_attempted\": False,"` | — |
| [SRC-3451CC474D-L000893](../../tests/test_api.py#L893) | 893 | `"                \"search_outcome\": \"not_attempted\","` | — |
| [SRC-3451CC474D-L000894](../../tests/test_api.py#L894) | 894 | `"            },"` | — |
| [SRC-3451CC474D-L000895](../../tests/test_api.py#L895) | 895 | `"            \"sources\": [],"` | — |
| [SRC-3451CC474D-L000896](../../tests/test_api.py#L896) | 896 | `"            \"used_language_model\": False,"` | — |
| [SRC-3451CC474D-L000897](../../tests/test_api.py#L897) | 897 | `"            \"used_web_search\": False,"` | — |
| [SRC-3451CC474D-L000898](../../tests/test_api.py#L898) | 898 | `"            \"search_attempted\": False,"` | — |
| [SRC-3451CC474D-L000899](../../tests/test_api.py#L899) | 899 | `"            \"used_social_search\": False,"` | — |
| [SRC-3451CC474D-L000900](../../tests/test_api.py#L900) | 900 | `"            \"warnings\": [],"` | — |
| [SRC-3451CC474D-L000901](../../tests/test_api.py#L901) | 901 | `"            \"kind\": \"web_fallback\","` | — |
| [SRC-3451CC474D-L000902](../../tests/test_api.py#L902) | 902 | `"        }"` | — |
| [SRC-3451CC474D-L000903](../../tests/test_api.py#L903) | 903 | `""` | — |
| [SRC-3451CC474D-L000904](../../tests/test_api.py#L904) | 904 | `"    monkeypatch.setattr(WebAgent, \"answer\", answer_with_one_transient_failure)"` | — |
| [SRC-3451CC474D-L000905](../../tests/test_api.py#L905) | 905 | `""` | — |
| [SRC-3451CC474D-L000906](../../tests/test_api.py#L906) | 906 | `"    status, payload = request_json("` | — |
| [SRC-3451CC474D-L000907](../../tests/test_api.py#L907) | 907 | `"        local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"الطلب الأول\"}"` | — |
| [SRC-3451CC474D-L000908](../../tests/test_api.py#L908) | 908 | `"    )"` | — |
| [SRC-3451CC474D-L000909](../../tests/test_api.py#L909) | 909 | `"    assert status == 500"` | — |
| [SRC-3451CC474D-L000910](../../tests/test_api.py#L910) | 910 | `"    assert payload[\"error\"] == \"internal server error\""` | — |
| [SRC-3451CC474D-L000911](../../tests/test_api.py#L911) | 911 | `""` | — |
| [SRC-3451CC474D-L000912](../../tests/test_api.py#L912) | 912 | `"    state[\"fail\"] = False"` | — |
| [SRC-3451CC474D-L000913](../../tests/test_api.py#L913) | 913 | `"    status, payload = request_json("` | — |
| [SRC-3451CC474D-L000914](../../tests/test_api.py#L914) | 914 | `"        local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"الطلب الثاني\"}"` | — |
| [SRC-3451CC474D-L000915](../../tests/test_api.py#L915) | 915 | `"    )"` | — |
| [SRC-3451CC474D-L000916](../../tests/test_api.py#L916) | 916 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000917](../../tests/test_api.py#L917) | 917 | `"    assert payload[\"answer\"] == \"اختبار ناجح\""` | — |
| [SRC-3451CC474D-L000918](../../tests/test_api.py#L918) | 918 | `""` | — |
| [SRC-3451CC474D-L000919](../../tests/test_api.py#L919) | 919 | `""` | — |
| [SRC-3451CC474D-L000920](../../tests/test_api.py#L920) | 920 | `"def test_csp_hashes_match_all_first_party_inline_content_and_attributes():"` | — |
| [SRC-3451CC474D-L000921](../../tests/test_api.py#L921) | 921 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000922](../../tests/test_api.py#L922) | 922 | `""` | — |
| [SRC-3451CC474D-L000923](../../tests/test_api.py#L923) | 923 | `"    policy = api_module._content_security_policy()"` | — |
| [SRC-3451CC474D-L000924](../../tests/test_api.py#L924) | 924 | `"    assert \"'unsafe-inline'\" not in policy"` | — |
| [SRC-3451CC474D-L000925](../../tests/test_api.py#L925) | 925 | `"    script_blocks = 0"` | — |
| [SRC-3451CC474D-L000926](../../tests/test_api.py#L926) | 926 | `"    style_blocks = 0"` | — |
| [SRC-3451CC474D-L000927](../../tests/test_api.py#L927) | 927 | `"    style_attributes = 0"` | — |
| [SRC-3451CC474D-L000928](../../tests/test_api.py#L928) | 928 | `"    for html_path in api_module.ROOT.glob(\"*.html\"):"` | — |
| [SRC-3451CC474D-L000929](../../tests/test_api.py#L929) | 929 | `"        document = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3451CC474D-L000930](../../tests/test_api.py#L930) | 930 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000931](../../tests/test_api.py#L931) | 931 | `"            r\"<script\\b(?P<attrs>[^>]*)>(?P<body>.*?)</script\\s*>\","` | — |
| [SRC-3451CC474D-L000932](../../tests/test_api.py#L932) | 932 | `"            document,"` | — |
| [SRC-3451CC474D-L000933](../../tests/test_api.py#L933) | 933 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L000934](../../tests/test_api.py#L934) | 934 | `"        ):"` | — |
| [SRC-3451CC474D-L000935](../../tests/test_api.py#L935) | 935 | `"            if re.search(r\"\\bsrc\\s*=\", match.group(\"attrs\"), re.IGNORECASE):"` | — |
| [SRC-3451CC474D-L000936](../../tests/test_api.py#L936) | 936 | `"                continue"` | — |
| [SRC-3451CC474D-L000937](../../tests/test_api.py#L937) | 937 | `"            script_blocks += 1"` | — |
| [SRC-3451CC474D-L000938](../../tests/test_api.py#L938) | 938 | `"            assert api_module._csp_hash_source(match.group(\"body\")) in policy"` | — |
| [SRC-3451CC474D-L000939](../../tests/test_api.py#L939) | 939 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000940](../../tests/test_api.py#L940) | 940 | `"            r\"<style\\b[^>]*>(?P<body>.*?)</style\\s*>\","` | — |
| [SRC-3451CC474D-L000941](../../tests/test_api.py#L941) | 941 | `"            document,"` | — |
| [SRC-3451CC474D-L000942](../../tests/test_api.py#L942) | 942 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L000943](../../tests/test_api.py#L943) | 943 | `"        ):"` | — |
| [SRC-3451CC474D-L000944](../../tests/test_api.py#L944) | 944 | `"            style_blocks += 1"` | — |
| [SRC-3451CC474D-L000945](../../tests/test_api.py#L945) | 945 | `"            assert api_module._csp_hash_source(match.group(\"body\")) in policy"` | — |
| [SRC-3451CC474D-L000946](../../tests/test_api.py#L946) | 946 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000947](../../tests/test_api.py#L947) | 947 | `"            r\"\"\"\\bstyle\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-3451CC474D-L000948](../../tests/test_api.py#L948) | 948 | `"            document,"` | — |
| [SRC-3451CC474D-L000949](../../tests/test_api.py#L949) | 949 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L000950](../../tests/test_api.py#L950) | 950 | `"        ):"` | — |
| [SRC-3451CC474D-L000951](../../tests/test_api.py#L951) | 951 | `"            style_attributes += 1"` | — |
| [SRC-3451CC474D-L000952](../../tests/test_api.py#L952) | 952 | `"            assert api_module._csp_hash_source(match.group(2).strip()) in policy"` | — |
| [SRC-3451CC474D-L000953](../../tests/test_api.py#L953) | 953 | `"    assert script_blocks >= 2"` | — |
| [SRC-3451CC474D-L000954](../../tests/test_api.py#L954) | 954 | `"    assert style_blocks >= 2"` | — |
| [SRC-3451CC474D-L000955](../../tests/test_api.py#L955) | 955 | `"    assert style_attributes >= 10"` | — |
| [SRC-3451CC474D-L000956](../../tests/test_api.py#L956) | 956 | `""` | — |
| [SRC-3451CC474D-L000957](../../tests/test_api.py#L957) | 957 | `""` | — |
| [SRC-3451CC474D-L000958](../../tests/test_api.py#L958) | 958 | `"def test_dashboard_uses_delegated_status_action_not_inline_onclick():"` | — |
| [SRC-3451CC474D-L000959](../../tests/test_api.py#L959) | 959 | `"    dashboard = (Path(__file__).resolve().parents[1] / \"web\" / \"dashboard.html\").read_text("` | — |
| [SRC-3451CC474D-L000960](../../tests/test_api.py#L960) | 960 | `"        encoding=\"utf-8\""` | — |
| [SRC-3451CC474D-L000961](../../tests/test_api.py#L961) | 961 | `"    )"` | — |
| [SRC-3451CC474D-L000962](../../tests/test_api.py#L962) | 962 | `"    assert 'data-action=\"save-status\"' in dashboard"` | — |
| [SRC-3451CC474D-L000963](../../tests/test_api.py#L963) | 963 | `"    assert 'onclick=\"saveStatus' not in dashboard"` | — |
| [SRC-3451CC474D-L000964](../../tests/test_api.py#L964) | 964 | `"    assert \"\"\"data-lead-id=\"'+esc(l.id)+'\">\"\"\" in dashboard"` | — |
## اختبارات

### FILE-6CBA87B20C — [tests/test_aspect_planning.py](../../tests/test_aspect_planning.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6CBA87B20C-L000001](../../tests/test_aspect_planning.py#L1) | 1 | `"\"\"\"Unit tests for aspect extraction and evidence ledger (no network).\"\"\""` | — |
| [SRC-6CBA87B20C-L000002](../../tests/test_aspect_planning.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-6CBA87B20C-L000003](../../tests/test_aspect_planning.py#L3) | 3 | `""` | — |
| [SRC-6CBA87B20C-L000004](../../tests/test_aspect_planning.py#L4) | 4 | `"from agents.aspect_planning import ("` | — |
| [SRC-6CBA87B20C-L000005](../../tests/test_aspect_planning.py#L5) | 5 | `"    arabic_aspect_diagnostics,"` | — |
| [SRC-6CBA87B20C-L000006](../../tests/test_aspect_planning.py#L6) | 6 | `"    build_aspect_queries,"` | — |
| [SRC-6CBA87B20C-L000007](../../tests/test_aspect_planning.py#L7) | 7 | `"    build_evidence_ledger,"` | — |
| [SRC-6CBA87B20C-L000008](../../tests/test_aspect_planning.py#L8) | 8 | `"    extract_aspects,"` | — |
| [SRC-6CBA87B20C-L000009](../../tests/test_aspect_planning.py#L9) | 9 | `"    repair_queries_for_missing_aspects,"` | — |
| [SRC-6CBA87B20C-L000010](../../tests/test_aspect_planning.py#L10) | 10 | `")"` | — |
| [SRC-6CBA87B20C-L000011](../../tests/test_aspect_planning.py#L11) | 11 | `""` | — |
| [SRC-6CBA87B20C-L000012](../../tests/test_aspect_planning.py#L12) | 12 | `""` | — |
| [SRC-6CBA87B20C-L000013](../../tests/test_aspect_planning.py#L13) | 13 | `"def test_extract_aspects_from_min_hayth():"` | — |
| [SRC-6CBA87B20C-L000014](../../tests/test_aspect_planning.py#L14) | 14 | `"    q = ("` | — |
| [SRC-6CBA87B20C-L000015](../../tests/test_aspect_planning.py#L15) | 15 | `"        \"حلل السيارات الكهربائية في مصر من حيث السعر، البطارية، والضمان. \""` | — |
| [SRC-6CBA87B20C-L000016](../../tests/test_aspect_planning.py#L16) | 16 | `"        \"اذكر مصادر موثوقة.\""` | — |
| [SRC-6CBA87B20C-L000017](../../tests/test_aspect_planning.py#L17) | 17 | `"    )"` | — |
| [SRC-6CBA87B20C-L000018](../../tests/test_aspect_planning.py#L18) | 18 | `"    aspects = extract_aspects(q)"` | — |
| [SRC-6CBA87B20C-L000019](../../tests/test_aspect_planning.py#L19) | 19 | `"    assert \"السعر\" in aspects or any(\"سعر\" in a for a in aspects)"` | — |
| [SRC-6CBA87B20C-L000020](../../tests/test_aspect_planning.py#L20) | 20 | `"    assert any(\"بطار\" in a for a in aspects)"` | — |
| [SRC-6CBA87B20C-L000021](../../tests/test_aspect_planning.py#L21) | 21 | `"    assert any(\"ضمان\" in a for a in aspects)"` | — |
| [SRC-6CBA87B20C-L000022](../../tests/test_aspect_planning.py#L22) | 22 | `"    assert len(aspects) >= 3"` | — |
| [SRC-6CBA87B20C-L000023](../../tests/test_aspect_planning.py#L23) | 23 | `""` | — |
| [SRC-6CBA87B20C-L000024](../../tests/test_aspect_planning.py#L24) | 24 | `""` | — |
| [SRC-6CBA87B20C-L000025](../../tests/test_aspect_planning.py#L25) | 25 | `"def test_extract_aspects_from_multi_question_marks():"` | — |
| [SRC-6CBA87B20C-L000026](../../tests/test_aspect_planning.py#L26) | 26 | `"    q = \"ما سعر الآيفون في مصر؟ وما مدة الضمان؟ وهل تتوفر صيانة محلية؟\""` | — |
| [SRC-6CBA87B20C-L000027](../../tests/test_aspect_planning.py#L27) | 27 | `"    aspects = extract_aspects(q)"` | — |
| [SRC-6CBA87B20C-L000028](../../tests/test_aspect_planning.py#L28) | 28 | `"    assert len(aspects) >= 2"` | — |
| [SRC-6CBA87B20C-L000029](../../tests/test_aspect_planning.py#L29) | 29 | `""` | — |
| [SRC-6CBA87B20C-L000030](../../tests/test_aspect_planning.py#L30) | 30 | `""` | — |
| [SRC-6CBA87B20C-L000031](../../tests/test_aspect_planning.py#L31) | 31 | `"def test_build_aspect_queries_prioritizes_topic():"` | — |
| [SRC-6CBA87B20C-L000032](../../tests/test_aspect_planning.py#L32) | 32 | `"    queries = build_aspect_queries("` | — |
| [SRC-6CBA87B20C-L000033](../../tests/test_aspect_planning.py#L33) | 33 | `"        \"السيارات الكهربائية في مصر\","` | — |
| [SRC-6CBA87B20C-L000034](../../tests/test_aspect_planning.py#L34) | 34 | `"        [\"السعر\", \"الضمان\"],"` | — |
| [SRC-6CBA87B20C-L000035](../../tests/test_aspect_planning.py#L35) | 35 | `"        limit=5,"` | — |
| [SRC-6CBA87B20C-L000036](../../tests/test_aspect_planning.py#L36) | 36 | `"    )"` | — |
| [SRC-6CBA87B20C-L000037](../../tests/test_aspect_planning.py#L37) | 37 | `"    assert queries[0] == \"السيارات الكهربائية في مصر\""` | — |
| [SRC-6CBA87B20C-L000038](../../tests/test_aspect_planning.py#L38) | 38 | `"    assert any(\"السعر\" in q for q in queries)"` | — |
| [SRC-6CBA87B20C-L000039](../../tests/test_aspect_planning.py#L39) | 39 | `"    assert any(\"الضمان\" in q for q in queries)"` | — |
| [SRC-6CBA87B20C-L000040](../../tests/test_aspect_planning.py#L40) | 40 | `"    assert len(queries) <= 5"` | — |
| [SRC-6CBA87B20C-L000041](../../tests/test_aspect_planning.py#L41) | 41 | `""` | — |
| [SRC-6CBA87B20C-L000042](../../tests/test_aspect_planning.py#L42) | 42 | `""` | — |
| [SRC-6CBA87B20C-L000043](../../tests/test_aspect_planning.py#L43) | 43 | `"def test_evidence_ledger_marks_missing_and_covered():"` | — |
| [SRC-6CBA87B20C-L000044](../../tests/test_aspect_planning.py#L44) | 44 | `"    aspects = [\"السعر\", \"الضمان\"]"` | — |
| [SRC-6CBA87B20C-L000045](../../tests/test_aspect_planning.py#L45) | 45 | `"    sources = ["` | — |
| [SRC-6CBA87B20C-L000046](../../tests/test_aspect_planning.py#L46) | 46 | `"        {"` | — |
| [SRC-6CBA87B20C-L000047](../../tests/test_aspect_planning.py#L47) | 47 | `"            \"title\": \"أسعار السيارات الكهربائية\","` | — |
| [SRC-6CBA87B20C-L000048](../../tests/test_aspect_planning.py#L48) | 48 | `"            \"url\": \"https://example.com/prices\","` | — |
| [SRC-6CBA87B20C-L000049](../../tests/test_aspect_planning.py#L49) | 49 | `"            \"snippet\": \"متوسط السعر في مصر لعام 2026\","` | — |
| [SRC-6CBA87B20C-L000050](../../tests/test_aspect_planning.py#L50) | 50 | `"            \"page_text\": \"\","` | — |
| [SRC-6CBA87B20C-L000051](../../tests/test_aspect_planning.py#L51) | 51 | `"            \"provider\": \"test\","` | — |
| [SRC-6CBA87B20C-L000052](../../tests/test_aspect_planning.py#L52) | 52 | `"        }"` | — |
| [SRC-6CBA87B20C-L000053](../../tests/test_aspect_planning.py#L53) | 53 | `"    ]"` | — |
| [SRC-6CBA87B20C-L000054](../../tests/test_aspect_planning.py#L54) | 54 | `"    ledger = build_evidence_ledger(aspects, sources)"` | — |
| [SRC-6CBA87B20C-L000055](../../tests/test_aspect_planning.py#L55) | 55 | `"    assert \"السعر\" in ledger[\"covered\"] or any("` | — |
| [SRC-6CBA87B20C-L000056](../../tests/test_aspect_planning.py#L56) | 56 | `"        \"سعر\" in c for c in ledger[\"covered\"]"` | — |
| [SRC-6CBA87B20C-L000057](../../tests/test_aspect_planning.py#L57) | 57 | `"    )"` | — |
| [SRC-6CBA87B20C-L000058](../../tests/test_aspect_planning.py#L58) | 58 | `"    assert \"الضمان\" in ledger[\"missing\"]"` | — |
| [SRC-6CBA87B20C-L000059](../../tests/test_aspect_planning.py#L59) | 59 | `"    assert 0 <= ledger[\"coverage_ratio\"] <= 1"` | — |
| [SRC-6CBA87B20C-L000060](../../tests/test_aspect_planning.py#L60) | 60 | `""` | — |
| [SRC-6CBA87B20C-L000061](../../tests/test_aspect_planning.py#L61) | 61 | `""` | — |
| [SRC-6CBA87B20C-L000062](../../tests/test_aspect_planning.py#L62) | 62 | `"def test_repair_queries_for_missing():"` | — |
| [SRC-6CBA87B20C-L000063](../../tests/test_aspect_planning.py#L63) | 63 | `"    qs = repair_queries_for_missing_aspects("` | — |
| [SRC-6CBA87B20C-L000064](../../tests/test_aspect_planning.py#L64) | 64 | `"        \"السيارات الكهربائية مصر\","` | — |
| [SRC-6CBA87B20C-L000065](../../tests/test_aspect_planning.py#L65) | 65 | `"        [\"الضمان\", \"الصيانة\"],"` | — |
| [SRC-6CBA87B20C-L000066](../../tests/test_aspect_planning.py#L66) | 66 | `"        limit=2,"` | — |
| [SRC-6CBA87B20C-L000067](../../tests/test_aspect_planning.py#L67) | 67 | `"    )"` | — |
| [SRC-6CBA87B20C-L000068](../../tests/test_aspect_planning.py#L68) | 68 | `"    assert len(qs) == 2"` | — |
| [SRC-6CBA87B20C-L000069](../../tests/test_aspect_planning.py#L69) | 69 | `"    assert all(\"السيارات\" in q for q in qs)"` | — |
| [SRC-6CBA87B20C-L000070](../../tests/test_aspect_planning.py#L70) | 70 | `""` | — |
| [SRC-6CBA87B20C-L000071](../../tests/test_aspect_planning.py#L71) | 71 | `""` | — |
| [SRC-6CBA87B20C-L000072](../../tests/test_aspect_planning.py#L72) | 72 | `"def test_arabic_diagnostics_not_truth_claim():"` | — |
| [SRC-6CBA87B20C-L000073](../../tests/test_aspect_planning.py#L73) | 73 | `"    ledger = {"` | — |
| [SRC-6CBA87B20C-L000074](../../tests/test_aspect_planning.py#L74) | 74 | `"        \"covered\": [\"السعر\"],"` | — |
| [SRC-6CBA87B20C-L000075](../../tests/test_aspect_planning.py#L75) | 75 | `"        \"missing\": [\"الضمان\"],"` | — |
| [SRC-6CBA87B20C-L000076](../../tests/test_aspect_planning.py#L76) | 76 | `"        \"coverage_ratio\": 0.5,"` | — |
| [SRC-6CBA87B20C-L000077](../../tests/test_aspect_planning.py#L77) | 77 | `"    }"` | — |
| [SRC-6CBA87B20C-L000078](../../tests/test_aspect_planning.py#L78) | 78 | `"    lines = arabic_aspect_diagnostics(ledger)"` | — |
| [SRC-6CBA87B20C-L000079](../../tests/test_aspect_planning.py#L79) | 79 | `"    assert any(\"ضمان\" in line for line in lines)"` | — |
| [SRC-6CBA87B20C-L000080](../../tests/test_aspect_planning.py#L80) | 80 | `"    assert any(\"لا يثبت\" in line for line in lines)"` | — |
| [SRC-6CBA87B20C-L000081](../../tests/test_aspect_planning.py#L81) | 81 | `""` | — |
| [SRC-6CBA87B20C-L000082](../../tests/test_aspect_planning.py#L82) | 82 | `""` | — |
| [SRC-6CBA87B20C-L000083](../../tests/test_aspect_planning.py#L83) | 83 | `"def test_extract_aspects_understands_compound_connectors_without_marker():"` | — |
| [SRC-6CBA87B20C-L000084](../../tests/test_aspect_planning.py#L84) | 84 | `"    question = ("` | — |
| [SRC-6CBA87B20C-L000085](../../tests/test_aspect_planning.py#L85) | 85 | `"        \"قارن بين الأنظمة: السعر والبطارية، بالإضافة إلى الضمان والصيانة \""` | — |
| [SRC-6CBA87B20C-L000086](../../tests/test_aspect_planning.py#L86) | 86 | `"        \"والخصوصية والاعتمادية والدعم والجودة\""` | — |
| [SRC-6CBA87B20C-L000087](../../tests/test_aspect_planning.py#L87) | 87 | `"    )"` | — |
| [SRC-6CBA87B20C-L000088](../../tests/test_aspect_planning.py#L88) | 88 | `"    aspects = extract_aspects(question)"` | — |
| [SRC-6CBA87B20C-L000089](../../tests/test_aspect_planning.py#L89) | 89 | `"    normalized = \" \".join(aspects)"` | — |
| [SRC-6CBA87B20C-L000090](../../tests/test_aspect_planning.py#L90) | 90 | `"    for expected in (\"السعر\", \"البطارية\", \"الضمان\", \"الصيانة\", \"الخصوصية\", \"الاعتمادية\", \"الدعم\", \"الجودة\"):"` | — |
| [SRC-6CBA87B20C-L000091](../../tests/test_aspect_planning.py#L91) | 91 | `"        assert expected in normalized"` | — |
| [SRC-6CBA87B20C-L000092](../../tests/test_aspect_planning.py#L92) | 92 | `"    assert len(aspects) <= 8"` | — |
| [SRC-6CBA87B20C-L000093](../../tests/test_aspect_planning.py#L93) | 93 | `""` | — |
| [SRC-6CBA87B20C-L000094](../../tests/test_aspect_planning.py#L94) | 94 | `""` | — |
| [SRC-6CBA87B20C-L000095](../../tests/test_aspect_planning.py#L95) | 95 | `"def test_extracts_joined_facets_without_formal_comparison_marker():"` | — |
| [SRC-6CBA87B20C-L000096](../../tests/test_aspect_planning.py#L96) | 96 | `"    aspects = extract_aspects(\"ما سعر الهاتف ومدة الضمان والصيانة؟\")"` | — |
| [SRC-6CBA87B20C-L000097](../../tests/test_aspect_planning.py#L97) | 97 | `"    joined = \" \".join(aspects)"` | — |
| [SRC-6CBA87B20C-L000098](../../tests/test_aspect_planning.py#L98) | 98 | `"    assert \"السعر\" in joined"` | — |
| [SRC-6CBA87B20C-L000099](../../tests/test_aspect_planning.py#L99) | 99 | `"    assert \"الضمان\" in joined"` | — |
| [SRC-6CBA87B20C-L000100](../../tests/test_aspect_planning.py#L100) | 100 | `"    assert \"الصيانة\" in joined"` | — |
| [SRC-6CBA87B20C-L000101](../../tests/test_aspect_planning.py#L101) | 101 | `""` | — |
| [SRC-6CBA87B20C-L000102](../../tests/test_aspect_planning.py#L102) | 102 | `""` | — |
| [SRC-6CBA87B20C-L000103](../../tests/test_aspect_planning.py#L103) | 103 | `"def test_extracts_general_factual_aspects_from_compound_arabic_question():"` | — |
| [SRC-6CBA87B20C-L000104](../../tests/test_aspect_planning.py#L104) | 104 | `"    question = \"اذكر عاصمة مصر وعدد سكان القاهرة، مع مصدر وتاريخ لكل معلومة\""` | — |
| [SRC-6CBA87B20C-L000105](../../tests/test_aspect_planning.py#L105) | 105 | `"    aspects = extract_aspects(question)"` | — |
| [SRC-6CBA87B20C-L000106](../../tests/test_aspect_planning.py#L106) | 106 | `"    joined = \" \".join(aspects)"` | — |
| [SRC-6CBA87B20C-L000107](../../tests/test_aspect_planning.py#L107) | 107 | `"    assert \"العاصمة\" in joined"` | — |
| [SRC-6CBA87B20C-L000108](../../tests/test_aspect_planning.py#L108) | 108 | `"    assert \"عدد السكان\" in joined"` | — |
| [SRC-6CBA87B20C-L000109](../../tests/test_aspect_planning.py#L109) | 109 | `"    assert len(aspects) <= 8"` | — |
| [SRC-6CBA87B20C-L000110](../../tests/test_aspect_planning.py#L110) | 110 | `""` | — |
| [SRC-6CBA87B20C-L000111](../../tests/test_aspect_planning.py#L111) | 111 | `""` | — |
| [SRC-6CBA87B20C-L000112](../../tests/test_aspect_planning.py#L112) | 112 | `"def test_builds_separate_queries_for_capital_and_population_aspects():"` | — |
| [SRC-6CBA87B20C-L000113](../../tests/test_aspect_planning.py#L113) | 113 | `"    question = \"اذكر عاصمة مصر وعدد سكان القاهرة\""` | — |
| [SRC-6CBA87B20C-L000114](../../tests/test_aspect_planning.py#L114) | 114 | `"    aspects = extract_aspects(question)"` | — |
| [SRC-6CBA87B20C-L000115](../../tests/test_aspect_planning.py#L115) | 115 | `"    queries = build_aspect_queries(\"مصر القاهرة\", aspects)"` | — |
| [SRC-6CBA87B20C-L000116](../../tests/test_aspect_planning.py#L116) | 116 | `"    assert any(\"العاصمة\" in query for query in queries)"` | — |
| [SRC-6CBA87B20C-L000117](../../tests/test_aspect_planning.py#L117) | 117 | `"    assert any(\"عدد السكان\" in query for query in queries)"` | — |
## اختبارات

### FILE-6B37B7D6D3 — [tests/test_claim_evidence_metadata.py](../../tests/test_claim_evidence_metadata.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6B37B7D6D3-L000001](../../tests/test_claim_evidence_metadata.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-6B37B7D6D3-L000002](../../tests/test_claim_evidence_metadata.py#L2) | 2 | `""` | — |
| [SRC-6B37B7D6D3-L000003](../../tests/test_claim_evidence_metadata.py#L3) | 3 | `"from agents.claim_evidence import audit_source_metadata, build_claim_evidence_ledger"` | — |
| [SRC-6B37B7D6D3-L000004](../../tests/test_claim_evidence_metadata.py#L4) | 4 | `""` | — |
| [SRC-6B37B7D6D3-L000005](../../tests/test_claim_evidence_metadata.py#L5) | 5 | `""` | — |
| [SRC-6B37B7D6D3-L000006](../../tests/test_claim_evidence_metadata.py#L6) | 6 | `"def test_source_metadata_accepts_complete_population_metadata_without_asserting_truth():"` | — |
| [SRC-6B37B7D6D3-L000007](../../tests/test_claim_evidence_metadata.py#L7) | 7 | `"    result = audit_source_metadata("` | — |
| [SRC-6B37B7D6D3-L000008](../../tests/test_claim_evidence_metadata.py#L8) | 8 | `"        {"` | — |
| [SRC-6B37B7D6D3-L000009](../../tests/test_claim_evidence_metadata.py#L9) | 9 | `"            \"url\": \"https://example.org/census\","` | — |
| [SRC-6B37B7D6D3-L000010](../../tests/test_claim_evidence_metadata.py#L10) | 10 | `"            \"title\": \"Population table\","` | — |
| [SRC-6B37B7D6D3-L000011](../../tests/test_claim_evidence_metadata.py#L11) | 11 | `"            \"publisher\": \"Example Statistics Office\","` | — |
| [SRC-6B37B7D6D3-L000012](../../tests/test_claim_evidence_metadata.py#L12) | 12 | `"            \"published_at\": \"2025-06-01\","` | — |
| [SRC-6B37B7D6D3-L000013](../../tests/test_claim_evidence_metadata.py#L13) | 13 | `"            \"data_reference_period\": \"2025 estimate\","` | — |
| [SRC-6B37B7D6D3-L000014](../../tests/test_claim_evidence_metadata.py#L14) | 14 | `"            \"geographic_scope\": \"Cairo Governorate administrative boundaries\","` | — |
| [SRC-6B37B7D6D3-L000015](../../tests/test_claim_evidence_metadata.py#L15) | 15 | `"            \"snippet\": \"Population estimate for the governorate.\","` | — |
| [SRC-6B37B7D6D3-L000016](../../tests/test_claim_evidence_metadata.py#L16) | 16 | `"        },"` | — |
| [SRC-6B37B7D6D3-L000017](../../tests/test_claim_evidence_metadata.py#L17) | 17 | `"        claim_text=\"عدد سكان محافظة القاهرة\","` | — |
| [SRC-6B37B7D6D3-L000018](../../tests/test_claim_evidence_metadata.py#L18) | 18 | `"    )"` | — |
| [SRC-6B37B7D6D3-L000019](../../tests/test_claim_evidence_metadata.py#L19) | 19 | `""` | — |
| [SRC-6B37B7D6D3-L000020](../../tests/test_claim_evidence_metadata.py#L20) | 20 | `"    assert result[\"status\"] == \"metadata_complete\""` | — |
| [SRC-6B37B7D6D3-L000021](../../tests/test_claim_evidence_metadata.py#L21) | 21 | `"    assert result[\"required_fields_missing\"] == []"` | — |
| [SRC-6B37B7D6D3-L000022](../../tests/test_claim_evidence_metadata.py#L22) | 22 | `"    assert result[\"claim_entailment\"] == \"not_checked\""` | — |
| [SRC-6B37B7D6D3-L000023](../../tests/test_claim_evidence_metadata.py#L23) | 23 | `"    assert result[\"fact_correctness\"] == \"not_checked\""` | — |
| [SRC-6B37B7D6D3-L000024](../../tests/test_claim_evidence_metadata.py#L24) | 24 | `"    assert result[\"semantic_verification\"] is False"` | — |
| [SRC-6B37B7D6D3-L000025](../../tests/test_claim_evidence_metadata.py#L25) | 25 | `""` | — |
| [SRC-6B37B7D6D3-L000026](../../tests/test_claim_evidence_metadata.py#L26) | 26 | `""` | — |
| [SRC-6B37B7D6D3-L000027](../../tests/test_claim_evidence_metadata.py#L27) | 27 | `"def test_source_metadata_flags_missing_publication_date_period_and_population_scope():"` | — |
| [SRC-6B37B7D6D3-L000028](../../tests/test_claim_evidence_metadata.py#L28) | 28 | `"    result = audit_source_metadata("` | — |
| [SRC-6B37B7D6D3-L000029](../../tests/test_claim_evidence_metadata.py#L29) | 29 | `"        {"` | — |
| [SRC-6B37B7D6D3-L000030](../../tests/test_claim_evidence_metadata.py#L30) | 30 | `"            \"url\": \"https://example.org/census\","` | — |
| [SRC-6B37B7D6D3-L000031](../../tests/test_claim_evidence_metadata.py#L31) | 31 | `"            \"title\": \"Population table\","` | — |
| [SRC-6B37B7D6D3-L000032](../../tests/test_claim_evidence_metadata.py#L32) | 32 | `"            \"publisher\": \"Example Statistics Office\","` | — |
| [SRC-6B37B7D6D3-L000033](../../tests/test_claim_evidence_metadata.py#L33) | 33 | `"            \"snippet\": \"Population estimate.\","` | — |
| [SRC-6B37B7D6D3-L000034](../../tests/test_claim_evidence_metadata.py#L34) | 34 | `"        },"` | — |
| [SRC-6B37B7D6D3-L000035](../../tests/test_claim_evidence_metadata.py#L35) | 35 | `"        claim_text=\"عدد سكان القاهرة الكبرى\","` | — |
| [SRC-6B37B7D6D3-L000036](../../tests/test_claim_evidence_metadata.py#L36) | 36 | `"    )"` | — |
| [SRC-6B37B7D6D3-L000037](../../tests/test_claim_evidence_metadata.py#L37) | 37 | `""` | — |
| [SRC-6B37B7D6D3-L000038](../../tests/test_claim_evidence_metadata.py#L38) | 38 | `"    assert result[\"status\"] == \"metadata_incomplete\""` | — |
| [SRC-6B37B7D6D3-L000039](../../tests/test_claim_evidence_metadata.py#L39) | 39 | `"    assert \"publication_date\" in result[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000040](../../tests/test_claim_evidence_metadata.py#L40) | 40 | `"    assert \"data_reference_period_for_population_claim\" in result[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000041](../../tests/test_claim_evidence_metadata.py#L41) | 41 | `"    assert \"geographic_scope_for_population_claim\" in result[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000042](../../tests/test_claim_evidence_metadata.py#L42) | 42 | `""` | — |
| [SRC-6B37B7D6D3-L000043](../../tests/test_claim_evidence_metadata.py#L43) | 43 | `""` | — |
| [SRC-6B37B7D6D3-L000044](../../tests/test_claim_evidence_metadata.py#L44) | 44 | `"def test_source_metadata_rejects_non_http_urls_and_urls_with_credentials():"` | — |
| [SRC-6B37B7D6D3-L000045](../../tests/test_claim_evidence_metadata.py#L45) | 45 | `"    for url in (\"javascript:alert(1)\", \"https://user:password@example.org/data\"):"` | — |
| [SRC-6B37B7D6D3-L000046](../../tests/test_claim_evidence_metadata.py#L46) | 46 | `"        result = audit_source_metadata("` | — |
| [SRC-6B37B7D6D3-L000047](../../tests/test_claim_evidence_metadata.py#L47) | 47 | `"            {"` | — |
| [SRC-6B37B7D6D3-L000048](../../tests/test_claim_evidence_metadata.py#L48) | 48 | `"                \"url\": url,"` | — |
| [SRC-6B37B7D6D3-L000049](../../tests/test_claim_evidence_metadata.py#L49) | 49 | `"                \"title\": \"Research report\","` | — |
| [SRC-6B37B7D6D3-L000050](../../tests/test_claim_evidence_metadata.py#L50) | 50 | `"                \"publisher\": \"Example Statistics Office\","` | — |
| [SRC-6B37B7D6D3-L000051](../../tests/test_claim_evidence_metadata.py#L51) | 51 | `"                \"published_at\": \"2025-06-01\","` | — |
| [SRC-6B37B7D6D3-L000052](../../tests/test_claim_evidence_metadata.py#L52) | 52 | `"                \"snippet\": \"A readable summary.\","` | — |
| [SRC-6B37B7D6D3-L000053](../../tests/test_claim_evidence_metadata.py#L53) | 53 | `"            },"` | — |
| [SRC-6B37B7D6D3-L000054](../../tests/test_claim_evidence_metadata.py#L54) | 54 | `"            claim_text=\"general research\","` | — |
| [SRC-6B37B7D6D3-L000055](../../tests/test_claim_evidence_metadata.py#L55) | 55 | `"        )"` | — |
| [SRC-6B37B7D6D3-L000056](../../tests/test_claim_evidence_metadata.py#L56) | 56 | `""` | — |
| [SRC-6B37B7D6D3-L000057](../../tests/test_claim_evidence_metadata.py#L57) | 57 | `"        assert result[\"valid_http_url\"] is False"` | — |
| [SRC-6B37B7D6D3-L000058](../../tests/test_claim_evidence_metadata.py#L58) | 58 | `"        assert \"valid_http_source_url\" in result[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000059](../../tests/test_claim_evidence_metadata.py#L59) | 59 | `""` | — |
| [SRC-6B37B7D6D3-L000060](../../tests/test_claim_evidence_metadata.py#L60) | 60 | `""` | — |
| [SRC-6B37B7D6D3-L000061](../../tests/test_claim_evidence_metadata.py#L61) | 61 | `"def test_claim_evidence_ledger_uses_question_context_for_population_metadata():"` | — |
| [SRC-6B37B7D6D3-L000062](../../tests/test_claim_evidence_metadata.py#L62) | 62 | `"    ledger = build_claim_evidence_ledger("` | — |
| [SRC-6B37B7D6D3-L000063](../../tests/test_claim_evidence_metadata.py#L63) | 63 | `"        \"The estimate is 9.7 million [source 1].\","` | — |
| [SRC-6B37B7D6D3-L000064](../../tests/test_claim_evidence_metadata.py#L64) | 64 | `"        ["` | — |
| [SRC-6B37B7D6D3-L000065](../../tests/test_claim_evidence_metadata.py#L65) | 65 | `"            {"` | — |
| [SRC-6B37B7D6D3-L000066](../../tests/test_claim_evidence_metadata.py#L66) | 66 | `"                \"url\": \"https://example.org/census\","` | — |
| [SRC-6B37B7D6D3-L000067](../../tests/test_claim_evidence_metadata.py#L67) | 67 | `"                \"title\": \"Population table\","` | — |
| [SRC-6B37B7D6D3-L000068](../../tests/test_claim_evidence_metadata.py#L68) | 68 | `"                \"publisher\": \"Example Statistics Office\","` | — |
| [SRC-6B37B7D6D3-L000069](../../tests/test_claim_evidence_metadata.py#L69) | 69 | `"                \"published_at\": \"2025-06-01\","` | — |
| [SRC-6B37B7D6D3-L000070](../../tests/test_claim_evidence_metadata.py#L70) | 70 | `"                \"snippet\": \"The estimate is 9.7 million.\","` | — |
| [SRC-6B37B7D6D3-L000071](../../tests/test_claim_evidence_metadata.py#L71) | 71 | `"            }"` | — |
| [SRC-6B37B7D6D3-L000072](../../tests/test_claim_evidence_metadata.py#L72) | 72 | `"        ],"` | — |
| [SRC-6B37B7D6D3-L000073](../../tests/test_claim_evidence_metadata.py#L73) | 73 | `"        question_context=\"How many people live in Cairo?\","` | — |
| [SRC-6B37B7D6D3-L000074](../../tests/test_claim_evidence_metadata.py#L74) | 74 | `"    )"` | — |
| [SRC-6B37B7D6D3-L000075](../../tests/test_claim_evidence_metadata.py#L75) | 75 | `""` | — |
| [SRC-6B37B7D6D3-L000076](../../tests/test_claim_evidence_metadata.py#L76) | 76 | `"    audit = ledger[\"segments\"][0][\"sources\"][0][\"metadata_audit\"]"` | — |
| [SRC-6B37B7D6D3-L000077](../../tests/test_claim_evidence_metadata.py#L77) | 77 | `"    assert audit[\"population_scope_required\"] is True"` | — |
| [SRC-6B37B7D6D3-L000078](../../tests/test_claim_evidence_metadata.py#L78) | 78 | `"    assert \"data_reference_period_for_population_claim\" in audit[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000079](../../tests/test_claim_evidence_metadata.py#L79) | 79 | `"    assert \"geographic_scope_for_population_claim\" in audit[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000080](../../tests/test_claim_evidence_metadata.py#L80) | 80 | `"    assert ledger[\"fact_correctness\"] == \"not_checked\""` | — |
## اختبارات

### FILE-DA61479D59 — [tests/test_connector_summary_counters.py](../../tests/test_connector_summary_counters.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-DA61479D59-L000001](../../tests/test_connector_summary_counters.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-DA61479D59-L000002](../../tests/test_connector_summary_counters.py#L2) | 2 | `""` | — |
| [SRC-DA61479D59-L000003](../../tests/test_connector_summary_counters.py#L3) | 3 | `"import json"` | — |
| [SRC-DA61479D59-L000004](../../tests/test_connector_summary_counters.py#L4) | 4 | `""` | — |
| [SRC-DA61479D59-L000005](../../tests/test_connector_summary_counters.py#L5) | 5 | `"from agents.web_agent import PageFetchResult, WebAgent"` | — |
| [SRC-DA61479D59-L000006](../../tests/test_connector_summary_counters.py#L6) | 6 | `""` | — |
| [SRC-DA61479D59-L000007](../../tests/test_connector_summary_counters.py#L7) | 7 | `""` | — |
| [SRC-DA61479D59-L000008](../../tests/test_connector_summary_counters.py#L8) | 8 | `"def test_connector_summary_reports_request_scope_worst_state_and_redacts_secrets(monkeypatch):"` | — |
| [SRC-DA61479D59-L000009](../../tests/test_connector_summary_counters.py#L9) | 9 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000010](../../tests/test_connector_summary_counters.py#L10) | 10 | `"    monkeypatch.delenv(\"BRAVE_SEARCH_API_KEY\", raising=False)"` | — |
| [SRC-DA61479D59-L000011](../../tests/test_connector_summary_counters.py#L11) | 11 | `"    diagnostics = ["` | — |
| [SRC-DA61479D59-L000012](../../tests/test_connector_summary_counters.py#L12) | 12 | `"        {"` | — |
| [SRC-DA61479D59-L000013](../../tests/test_connector_summary_counters.py#L13) | 13 | `"            \"provider\": \"duckduckgo_html\","` | — |
| [SRC-DA61479D59-L000014](../../tests/test_connector_summary_counters.py#L14) | 14 | `"            \"query\": \"renewable energy\","` | — |
| [SRC-DA61479D59-L000015](../../tests/test_connector_summary_counters.py#L15) | 15 | `"            \"status\": \"ok\","` | — |
| [SRC-DA61479D59-L000016](../../tests/test_connector_summary_counters.py#L16) | 16 | `"            \"result_count\": 3,"` | — |
| [SRC-DA61479D59-L000017](../../tests/test_connector_summary_counters.py#L17) | 17 | `"            \"rejected_count\": 1,"` | — |
| [SRC-DA61479D59-L000018](../../tests/test_connector_summary_counters.py#L18) | 18 | `"        },"` | — |
| [SRC-DA61479D59-L000019](../../tests/test_connector_summary_counters.py#L19) | 19 | `"        {"` | — |
| [SRC-DA61479D59-L000020](../../tests/test_connector_summary_counters.py#L20) | 20 | `"            \"provider\": \"duckduckgo_html\","` | — |
| [SRC-DA61479D59-L000021](../../tests/test_connector_summary_counters.py#L21) | 21 | `"            \"query\": \"renewable energy\","` | — |
| [SRC-DA61479D59-L000022](../../tests/test_connector_summary_counters.py#L22) | 22 | `"            \"status\": \"failed\","` | — |
| [SRC-DA61479D59-L000023](../../tests/test_connector_summary_counters.py#L23) | 23 | `"            \"result_count\": 0,"` | — |
| [SRC-DA61479D59-L000024](../../tests/test_connector_summary_counters.py#L24) | 24 | `"            \"rejected_count\": 0,"` | — |
| [SRC-DA61479D59-L000025](../../tests/test_connector_summary_counters.py#L25) | 25 | `"            \"error\": \"HTTP 500 token=secret-value\","` | — |
| [SRC-DA61479D59-L000026](../../tests/test_connector_summary_counters.py#L26) | 26 | `"        },"` | — |
| [SRC-DA61479D59-L000027](../../tests/test_connector_summary_counters.py#L27) | 27 | `"    ]"` | — |
| [SRC-DA61479D59-L000028](../../tests/test_connector_summary_counters.py#L28) | 28 | `"    sources = ["` | — |
| [SRC-DA61479D59-L000029](../../tests/test_connector_summary_counters.py#L29) | 29 | `"        {\"url\": \"https://example.com/a\", \"providers\": [\"duckduckgo_html\"]},"` | — |
| [SRC-DA61479D59-L000030](../../tests/test_connector_summary_counters.py#L30) | 30 | `"        {\"url\": \"https://example.org/b\", \"providers\": [\"bing_rss\"]},"` | — |
| [SRC-DA61479D59-L000031](../../tests/test_connector_summary_counters.py#L31) | 31 | `"    ]"` | — |
| [SRC-DA61479D59-L000032](../../tests/test_connector_summary_counters.py#L32) | 32 | `""` | — |
| [SRC-DA61479D59-L000033](../../tests/test_connector_summary_counters.py#L33) | 33 | `"    summary = agent._connector_status_summary(diagnostics, sources)"` | — |
| [SRC-DA61479D59-L000034](../../tests/test_connector_summary_counters.py#L34) | 34 | `""` | — |
| [SRC-DA61479D59-L000035](../../tests/test_connector_summary_counters.py#L35) | 35 | `"    duckduckgo = next(item for item in summary[\"connectors\"] if item[\"name\"] == \"duckduckgo_html\")"` | — |
| [SRC-DA61479D59-L000036](../../tests/test_connector_summary_counters.py#L36) | 36 | `"    brave = next(item for item in summary[\"connectors\"] if item[\"name\"] == \"brave_search_api\")"` | — |
| [SRC-DA61479D59-L000037](../../tests/test_connector_summary_counters.py#L37) | 37 | `"    assert summary[\"scope\"] == \"this_request_only\""` | — |
| [SRC-DA61479D59-L000038](../../tests/test_connector_summary_counters.py#L38) | 38 | `"    assert duckduckgo[\"attempted\"] is True"` | — |
| [SRC-DA61479D59-L000039](../../tests/test_connector_summary_counters.py#L39) | 39 | `"    assert duckduckgo[\"status\"] == \"failed\""` | — |
| [SRC-DA61479D59-L000040](../../tests/test_connector_summary_counters.py#L40) | 40 | `"    assert duckduckgo[\"observed_statuses\"] == [\"ok\", \"failed\"]"` | — |
| [SRC-DA61479D59-L000041](../../tests/test_connector_summary_counters.py#L41) | 41 | `"    assert duckduckgo[\"result_count\"] == 3"` | — |
| [SRC-DA61479D59-L000042](../../tests/test_connector_summary_counters.py#L42) | 42 | `"    assert duckduckgo[\"useful_result_count\"] == 1"` | — |
| [SRC-DA61479D59-L000043](../../tests/test_connector_summary_counters.py#L43) | 43 | `"    assert duckduckgo[\"rejected_count\"] == 1"` | — |
| [SRC-DA61479D59-L000044](../../tests/test_connector_summary_counters.py#L44) | 44 | `"    assert duckduckgo[\"implementation_status\"] == \"implemented_in_code\""` | — |
| [SRC-DA61479D59-L000045](../../tests/test_connector_summary_counters.py#L45) | 45 | `"    assert duckduckgo[\"available_for_this_request\"] is True"` | — |
| [SRC-DA61479D59-L000046](../../tests/test_connector_summary_counters.py#L46) | 46 | `"    assert duckduckgo[\"verified_for_this_request\"] is True"` | — |
| [SRC-DA61479D59-L000047](../../tests/test_connector_summary_counters.py#L47) | 47 | `"    assert duckduckgo[\"failure_observed\"] is True"` | — |
| [SRC-DA61479D59-L000048](../../tests/test_connector_summary_counters.py#L48) | 48 | `"    assert \"secret-value\" not in json.dumps(summary)"` | — |
| [SRC-DA61479D59-L000049](../../tests/test_connector_summary_counters.py#L49) | 49 | `"    assert brave[\"configured\"] is False"` | — |
| [SRC-DA61479D59-L000050](../../tests/test_connector_summary_counters.py#L50) | 50 | `"    assert brave[\"status\"] == \"not_configured\""` | — |
| [SRC-DA61479D59-L000051](../../tests/test_connector_summary_counters.py#L51) | 51 | `"    assert brave[\"available_for_this_request\"] is False"` | — |
| [SRC-DA61479D59-L000052](../../tests/test_connector_summary_counters.py#L52) | 52 | `"    assert brave[\"verified_for_this_request\"] is None"` | — |
| [SRC-DA61479D59-L000053](../../tests/test_connector_summary_counters.py#L53) | 53 | `""` | — |
| [SRC-DA61479D59-L000054](../../tests/test_connector_summary_counters.py#L54) | 54 | `""` | — |
| [SRC-DA61479D59-L000055](../../tests/test_connector_summary_counters.py#L55) | 55 | `"def test_collect_research_distinguishes_raw_rows_unique_urls_and_page_extraction(monkeypatch):"` | — |
| [SRC-DA61479D59-L000056](../../tests/test_connector_summary_counters.py#L56) | 56 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000057](../../tests/test_connector_summary_counters.py#L57) | 57 | `"    query = \"renewable energy storage\""` | — |
| [SRC-DA61479D59-L000058](../../tests/test_connector_summary_counters.py#L58) | 58 | `"    results = ["` | — |
| [SRC-DA61479D59-L000059](../../tests/test_connector_summary_counters.py#L59) | 59 | `"        {"` | — |
| [SRC-DA61479D59-L000060](../../tests/test_connector_summary_counters.py#L60) | 60 | `"            \"title\": \"Renewable energy storage report\","` | — |
| [SRC-DA61479D59-L000061](../../tests/test_connector_summary_counters.py#L61) | 61 | `"            \"url\": \"https://example.com/report\","` | — |
| [SRC-DA61479D59-L000062](../../tests/test_connector_summary_counters.py#L62) | 62 | `"            \"snippet\": \"Renewable energy storage data from the report\","` | — |
| [SRC-DA61479D59-L000063](../../tests/test_connector_summary_counters.py#L63) | 63 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000064](../../tests/test_connector_summary_counters.py#L64) | 64 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000065](../../tests/test_connector_summary_counters.py#L65) | 65 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000066](../../tests/test_connector_summary_counters.py#L66) | 66 | `"            \"provider_rank\": 1,"` | — |
| [SRC-DA61479D59-L000067](../../tests/test_connector_summary_counters.py#L67) | 67 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000068](../../tests/test_connector_summary_counters.py#L68) | 68 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000069](../../tests/test_connector_summary_counters.py#L69) | 69 | `"        },"` | — |
| [SRC-DA61479D59-L000070](../../tests/test_connector_summary_counters.py#L70) | 70 | `"        {"` | — |
| [SRC-DA61479D59-L000071](../../tests/test_connector_summary_counters.py#L71) | 71 | `"            \"title\": \"Renewable energy storage report (duplicate URL)\","` | — |
| [SRC-DA61479D59-L000072](../../tests/test_connector_summary_counters.py#L72) | 72 | `"            \"url\": \"https://example.com/report?utm_source=test\","` | — |
| [SRC-DA61479D59-L000073](../../tests/test_connector_summary_counters.py#L73) | 73 | `"            \"snippet\": \"Renewable energy storage data from a duplicate result\","` | — |
| [SRC-DA61479D59-L000074](../../tests/test_connector_summary_counters.py#L74) | 74 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000075](../../tests/test_connector_summary_counters.py#L75) | 75 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000076](../../tests/test_connector_summary_counters.py#L76) | 76 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000077](../../tests/test_connector_summary_counters.py#L77) | 77 | `"            \"provider_rank\": 2,"` | — |
| [SRC-DA61479D59-L000078](../../tests/test_connector_summary_counters.py#L78) | 78 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000079](../../tests/test_connector_summary_counters.py#L79) | 79 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000080](../../tests/test_connector_summary_counters.py#L80) | 80 | `"        },"` | — |
| [SRC-DA61479D59-L000081](../../tests/test_connector_summary_counters.py#L81) | 81 | `"        {"` | — |
| [SRC-DA61479D59-L000082](../../tests/test_connector_summary_counters.py#L82) | 82 | `"            \"title\": \"Renewable energy storage statistics\","` | — |
| [SRC-DA61479D59-L000083](../../tests/test_connector_summary_counters.py#L83) | 83 | `"            \"url\": \"https://example.org/statistics\","` | — |
| [SRC-DA61479D59-L000084](../../tests/test_connector_summary_counters.py#L84) | 84 | `"            \"snippet\": \"Renewable energy storage statistics\","` | — |
| [SRC-DA61479D59-L000085](../../tests/test_connector_summary_counters.py#L85) | 85 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000086](../../tests/test_connector_summary_counters.py#L86) | 86 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000087](../../tests/test_connector_summary_counters.py#L87) | 87 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000088](../../tests/test_connector_summary_counters.py#L88) | 88 | `"            \"provider_rank\": 3,"` | — |
| [SRC-DA61479D59-L000089](../../tests/test_connector_summary_counters.py#L89) | 89 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000090](../../tests/test_connector_summary_counters.py#L90) | 90 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000091](../../tests/test_connector_summary_counters.py#L91) | 91 | `"        },"` | — |
| [SRC-DA61479D59-L000092](../../tests/test_connector_summary_counters.py#L92) | 92 | `"    ]"` | — |
| [SRC-DA61479D59-L000093](../../tests/test_connector_summary_counters.py#L93) | 93 | `""` | — |
| [SRC-DA61479D59-L000094](../../tests/test_connector_summary_counters.py#L94) | 94 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda _query: results)"` | — |
| [SRC-DA61479D59-L000095](../../tests/test_connector_summary_counters.py#L95) | 95 | `"    def fetch(url: str):"` | — |
| [SRC-DA61479D59-L000096](../../tests/test_connector_summary_counters.py#L96) | 96 | `"        if \"example.com\" in url:"` | — |
| [SRC-DA61479D59-L000097](../../tests/test_connector_summary_counters.py#L97) | 97 | `"            return \"Report page\", \"Renewable energy storage page body with extracted text.\""` | — |
| [SRC-DA61479D59-L000098](../../tests/test_connector_summary_counters.py#L98) | 98 | `"        return \"\", \"\""` | — |
| [SRC-DA61479D59-L000099](../../tests/test_connector_summary_counters.py#L99) | 99 | `""` | — |
| [SRC-DA61479D59-L000100](../../tests/test_connector_summary_counters.py#L100) | 100 | `"    monkeypatch.setattr(agent, \"_fetch_page\", fetch)"` | — |
| [SRC-DA61479D59-L000101](../../tests/test_connector_summary_counters.py#L101) | 101 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-DA61479D59-L000102](../../tests/test_connector_summary_counters.py#L102) | 102 | `"        \"queries\": [query],"` | — |
| [SRC-DA61479D59-L000103](../../tests/test_connector_summary_counters.py#L103) | 103 | `"        \"direct_urls\": [],"` | — |
| [SRC-DA61479D59-L000104](../../tests/test_connector_summary_counters.py#L104) | 104 | `"        \"social_focus\": False,"` | — |
| [SRC-DA61479D59-L000105](../../tests/test_connector_summary_counters.py#L105) | 105 | `"        \"freshness\": \"any\","` | — |
| [SRC-DA61479D59-L000106](../../tests/test_connector_summary_counters.py#L106) | 106 | `"        \"depth\": \"standard\","` | — |
| [SRC-DA61479D59-L000107](../../tests/test_connector_summary_counters.py#L107) | 107 | `"        \"platforms\": [],"` | — |
| [SRC-DA61479D59-L000108](../../tests/test_connector_summary_counters.py#L108) | 108 | `"        \"planning_method\": \"unit_test\","` | — |
| [SRC-DA61479D59-L000109](../../tests/test_connector_summary_counters.py#L109) | 109 | `"    })"` | — |
| [SRC-DA61479D59-L000110](../../tests/test_connector_summary_counters.py#L110) | 110 | `""` | — |
| [SRC-DA61479D59-L000111](../../tests/test_connector_summary_counters.py#L111) | 111 | `"    assert warnings"` | — |
| [SRC-DA61479D59-L000112](../../tests/test_connector_summary_counters.py#L112) | 112 | `"    assert report[\"raw_results\"] == 3"` | — |
| [SRC-DA61479D59-L000113](../../tests/test_connector_summary_counters.py#L113) | 113 | `"    assert report[\"unique_urls\"] == 2"` | — |
| [SRC-DA61479D59-L000114](../../tests/test_connector_summary_counters.py#L114) | 114 | `"    assert report[\"unique_sources\"] == 2"` | — |
| [SRC-DA61479D59-L000115](../../tests/test_connector_summary_counters.py#L115) | 115 | `"    assert report[\"pages_fetch_attempted\"] == 2"` | — |
| [SRC-DA61479D59-L000116](../../tests/test_connector_summary_counters.py#L116) | 116 | `"    assert report[\"pages_content_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000117](../../tests/test_connector_summary_counters.py#L117) | 117 | `"    assert report[\"pages_extract_failed\"] == 1"` | — |
| [SRC-DA61479D59-L000118](../../tests/test_connector_summary_counters.py#L118) | 118 | `"    assert report[\"page_fetch_status_counts\"][\"content_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000119](../../tests/test_connector_summary_counters.py#L119) | 119 | `"    assert report[\"page_fetch_status_counts\"][\"no_text_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000120](../../tests/test_connector_summary_counters.py#L120) | 120 | `"    assert report[\"page_fetch_status_counts\"][\"fetch_failed\"] == 0"` | — |
| [SRC-DA61479D59-L000121](../../tests/test_connector_summary_counters.py#L121) | 121 | `"    assert report[\"page_fetch_status_counts\"][\"partial_extraction\"] == 0"` | — |
| [SRC-DA61479D59-L000122](../../tests/test_connector_summary_counters.py#L122) | 122 | `"    assert report[\"pages_partial_extracted\"] == 0"` | — |
| [SRC-DA61479D59-L000123](../../tests/test_connector_summary_counters.py#L123) | 123 | `"    assert sum(source[\"page_fetch_status\"] == \"content_extracted\" for source in sources) == 1"` | — |
| [SRC-DA61479D59-L000124](../../tests/test_connector_summary_counters.py#L124) | 124 | `"    assert sum(source[\"page_fetch_status\"] == \"no_text_extracted\" for source in sources) == 1"` | — |
| [SRC-DA61479D59-L000125](../../tests/test_connector_summary_counters.py#L125) | 125 | `"    assert report[\"connector_summary\"][\"scope\"] == \"this_request_only\""` | — |
| [SRC-DA61479D59-L000126](../../tests/test_connector_summary_counters.py#L126) | 126 | `""` | — |
| [SRC-DA61479D59-L000127](../../tests/test_connector_summary_counters.py#L127) | 127 | `""` | — |
| [SRC-DA61479D59-L000128](../../tests/test_connector_summary_counters.py#L128) | 128 | `"def test_connector_summary_does_not_claim_timeout_or_budget_exhaustion_was_a_confirmed_attempt(monkeypatch):"` | — |
| [SRC-DA61479D59-L000129](../../tests/test_connector_summary_counters.py#L129) | 129 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000130](../../tests/test_connector_summary_counters.py#L130) | 130 | `"    monkeypatch.setenv(\"TAVILY_API_KEY\", \"configured-test-key\")"` | — |
| [SRC-DA61479D59-L000131](../../tests/test_connector_summary_counters.py#L131) | 131 | `"    monkeypatch.setenv(\"DEEPSEEK_SEARCH_API_KEY\", \"configured-test-key\")"` | — |
| [SRC-DA61479D59-L000132](../../tests/test_connector_summary_counters.py#L132) | 132 | `"    timeout = agent._connector_status_summary("` | — |
| [SRC-DA61479D59-L000133](../../tests/test_connector_summary_counters.py#L133) | 133 | `"        [{\"provider\": \"tavily_search_api\", \"query\": \"query\", \"status\": \"timeout\", \"error\": \"request timed out\"}],"` | — |
| [SRC-DA61479D59-L000134](../../tests/test_connector_summary_counters.py#L134) | 134 | `"        [],"` | — |
| [SRC-DA61479D59-L000135](../../tests/test_connector_summary_counters.py#L135) | 135 | `"    )"` | — |
| [SRC-DA61479D59-L000136](../../tests/test_connector_summary_counters.py#L136) | 136 | `"    exhausted = agent._connector_status_summary("` | — |
| [SRC-DA61479D59-L000137](../../tests/test_connector_summary_counters.py#L137) | 137 | `"        [{\"provider\": \"deepseek_search_api\", \"query\": \"query\", \"status\": \"budget_exhausted\"}],"` | — |
| [SRC-DA61479D59-L000138](../../tests/test_connector_summary_counters.py#L138) | 138 | `"        [],"` | — |
| [SRC-DA61479D59-L000139](../../tests/test_connector_summary_counters.py#L139) | 139 | `"    )"` | — |
| [SRC-DA61479D59-L000140](../../tests/test_connector_summary_counters.py#L140) | 140 | `"    tavily = next(item for item in timeout[\"connectors\"] if item[\"name\"] == \"tavily_search_api\")"` | — |
| [SRC-DA61479D59-L000141](../../tests/test_connector_summary_counters.py#L141) | 141 | `"    deepseek = next(item for item in exhausted[\"connectors\"] if item[\"name\"] == \"deepseek_search_api\")"` | — |
| [SRC-DA61479D59-L000142](../../tests/test_connector_summary_counters.py#L142) | 142 | `"    assert tavily[\"configured\"] is True"` | — |
| [SRC-DA61479D59-L000143](../../tests/test_connector_summary_counters.py#L143) | 143 | `"    assert tavily[\"attempted\"] is None"` | — |
| [SRC-DA61479D59-L000144](../../tests/test_connector_summary_counters.py#L144) | 144 | `"    assert tavily[\"status\"] == \"timeout\""` | — |
| [SRC-DA61479D59-L000145](../../tests/test_connector_summary_counters.py#L145) | 145 | `"    assert tavily[\"available_for_this_request\"] is None"` | — |
| [SRC-DA61479D59-L000146](../../tests/test_connector_summary_counters.py#L146) | 146 | `"    assert tavily[\"verified_for_this_request\"] is None"` | — |
| [SRC-DA61479D59-L000147](../../tests/test_connector_summary_counters.py#L147) | 147 | `"    assert tavily[\"failure_observed\"] is True"` | — |
| [SRC-DA61479D59-L000148](../../tests/test_connector_summary_counters.py#L148) | 148 | `"    assert deepseek[\"configured\"] is True"` | — |
| [SRC-DA61479D59-L000149](../../tests/test_connector_summary_counters.py#L149) | 149 | `"    assert deepseek[\"attempted\"] is False"` | — |
| [SRC-DA61479D59-L000150](../../tests/test_connector_summary_counters.py#L150) | 150 | `"    assert deepseek[\"status\"] == \"budget_exhausted\""` | — |
| [SRC-DA61479D59-L000151](../../tests/test_connector_summary_counters.py#L151) | 151 | `"    assert deepseek[\"available_for_this_request\"] is False"` | — |
| [SRC-DA61479D59-L000152](../../tests/test_connector_summary_counters.py#L152) | 152 | `"    assert deepseek[\"verified_for_this_request\"] is None"` | — |
| [SRC-DA61479D59-L000153](../../tests/test_connector_summary_counters.py#L153) | 153 | `""` | — |
| [SRC-DA61479D59-L000154](../../tests/test_connector_summary_counters.py#L154) | 154 | `""` | — |
| [SRC-DA61479D59-L000155](../../tests/test_connector_summary_counters.py#L155) | 155 | `"def test_collect_research_preserves_partial_and_http_failure_page_statuses(monkeypatch):"` | — |
| [SRC-DA61479D59-L000156](../../tests/test_connector_summary_counters.py#L156) | 156 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000157](../../tests/test_connector_summary_counters.py#L157) | 157 | `"    query = \"renewable energy storage\""` | — |
| [SRC-DA61479D59-L000158](../../tests/test_connector_summary_counters.py#L158) | 158 | `"    results = ["` | — |
| [SRC-DA61479D59-L000159](../../tests/test_connector_summary_counters.py#L159) | 159 | `"        {"` | — |
| [SRC-DA61479D59-L000160](../../tests/test_connector_summary_counters.py#L160) | 160 | `"            \"title\": \"Renewable energy storage report\","` | — |
| [SRC-DA61479D59-L000161](../../tests/test_connector_summary_counters.py#L161) | 161 | `"            \"url\": \"https://example.com/report\","` | — |
| [SRC-DA61479D59-L000162](../../tests/test_connector_summary_counters.py#L162) | 162 | `"            \"snippet\": \"Renewable energy storage report\","` | — |
| [SRC-DA61479D59-L000163](../../tests/test_connector_summary_counters.py#L163) | 163 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000164](../../tests/test_connector_summary_counters.py#L164) | 164 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000165](../../tests/test_connector_summary_counters.py#L165) | 165 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000166](../../tests/test_connector_summary_counters.py#L166) | 166 | `"            \"provider_rank\": 1,"` | — |
| [SRC-DA61479D59-L000167](../../tests/test_connector_summary_counters.py#L167) | 167 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000168](../../tests/test_connector_summary_counters.py#L168) | 168 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000169](../../tests/test_connector_summary_counters.py#L169) | 169 | `"        },"` | — |
| [SRC-DA61479D59-L000170](../../tests/test_connector_summary_counters.py#L170) | 170 | `"        {"` | — |
| [SRC-DA61479D59-L000171](../../tests/test_connector_summary_counters.py#L171) | 171 | `"            \"title\": \"Renewable energy storage statistics\","` | — |
| [SRC-DA61479D59-L000172](../../tests/test_connector_summary_counters.py#L172) | 172 | `"            \"url\": \"https://example.org/statistics\","` | — |
| [SRC-DA61479D59-L000173](../../tests/test_connector_summary_counters.py#L173) | 173 | `"            \"snippet\": \"Renewable energy storage statistics\","` | — |
| [SRC-DA61479D59-L000174](../../tests/test_connector_summary_counters.py#L174) | 174 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000175](../../tests/test_connector_summary_counters.py#L175) | 175 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000176](../../tests/test_connector_summary_counters.py#L176) | 176 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000177](../../tests/test_connector_summary_counters.py#L177) | 177 | `"            \"provider_rank\": 2,"` | — |
| [SRC-DA61479D59-L000178](../../tests/test_connector_summary_counters.py#L178) | 178 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000179](../../tests/test_connector_summary_counters.py#L179) | 179 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000180](../../tests/test_connector_summary_counters.py#L180) | 180 | `"        },"` | — |
| [SRC-DA61479D59-L000181](../../tests/test_connector_summary_counters.py#L181) | 181 | `"    ]"` | — |
