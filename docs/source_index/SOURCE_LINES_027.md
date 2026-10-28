# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **027**
- سجلات الأسطر: **800**
- النطاق: SRC-3451CC474D-L000566 إلى SRC-29A9CD43D1-L000170
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-3451CC474D — [tests/test_api.py](../../tests/test_api.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3451CC474D-L000566](../../tests/test_api.py#L566) | 566 | `"def test_api_absolute_body_deadline_stops_slow_trickle(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000567](../../tests/test_api.py#L567) | 567 | `"    \"\"\"A client must not evade the total deadline by sending before each idle timeout.\"\"\""` | — |
| [SRC-3451CC474D-L000568](../../tests/test_api.py#L568) | 568 | `"    import time"` | — |
| [SRC-3451CC474D-L000569](../../tests/test_api.py#L569) | 569 | `""` | — |
| [SRC-3451CC474D-L000570](../../tests/test_api.py#L570) | 570 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000571](../../tests/test_api.py#L571) | 571 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000572](../../tests/test_api.py#L572) | 572 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_BODY_READ_TIMEOUT_SECONDS\", 0.45)"` | — |
| [SRC-3451CC474D-L000573](../../tests/test_api.py#L573) | 573 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_BODY_IDLE_TIMEOUT_SECONDS\", 0.20)"` | — |
| [SRC-3451CC474D-L000574](../../tests/test_api.py#L574) | 574 | `"    host, port = local_api.removeprefix(\"http://\").rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000575](../../tests/test_api.py#L575) | 575 | `""` | — |
| [SRC-3451CC474D-L000576](../../tests/test_api.py#L576) | 576 | `"    with socket.create_connection((host, int(port)), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000577](../../tests/test_api.py#L577) | 577 | `"        client.settimeout(2)"` | — |
| [SRC-3451CC474D-L000578](../../tests/test_api.py#L578) | 578 | `"        started = time.monotonic()"` | — |
| [SRC-3451CC474D-L000579](../../tests/test_api.py#L579) | 579 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000580](../../tests/test_api.py#L580) | 580 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000581](../../tests/test_api.py#L581) | 581 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000582](../../tests/test_api.py#L582) | 582 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000583](../../tests/test_api.py#L583) | 583 | `"            b\"Content-Length: 100\\r\\n\""` | — |
| [SRC-3451CC474D-L000584](../../tests/test_api.py#L584) | 584 | `"            b\"Connection: close\\r\\n\\r\\n\""` | — |
| [SRC-3451CC474D-L000585](../../tests/test_api.py#L585) | 585 | `"            b\"{\""` | — |
| [SRC-3451CC474D-L000586](../../tests/test_api.py#L586) | 586 | `"        )"` | — |
| [SRC-3451CC474D-L000587](../../tests/test_api.py#L587) | 587 | `"        # Each fragment arrives before the 0.20s idle timeout, but the complete"` | — |
| [SRC-3451CC474D-L000588](../../tests/test_api.py#L588) | 588 | `"        # request body never arrives before the 0.45s absolute deadline."` | — |
| [SRC-3451CC474D-L000589](../../tests/test_api.py#L589) | 589 | `"        for fragment in (b'\"', b\"text\", b'\"', b\":\"):"` | — |
| [SRC-3451CC474D-L000590](../../tests/test_api.py#L590) | 590 | `"            time.sleep(0.08)"` | — |
| [SRC-3451CC474D-L000591](../../tests/test_api.py#L591) | 591 | `"            try:"` | — |
| [SRC-3451CC474D-L000592](../../tests/test_api.py#L592) | 592 | `"                client.sendall(fragment)"` | — |
| [SRC-3451CC474D-L000593](../../tests/test_api.py#L593) | 593 | `"            except OSError:"` | — |
| [SRC-3451CC474D-L000594](../../tests/test_api.py#L594) | 594 | `"                break"` | — |
| [SRC-3451CC474D-L000595](../../tests/test_api.py#L595) | 595 | `""` | — |
| [SRC-3451CC474D-L000596](../../tests/test_api.py#L596) | 596 | `"        response = bytearray()"` | — |
| [SRC-3451CC474D-L000597](../../tests/test_api.py#L597) | 597 | `"        while True:"` | — |
| [SRC-3451CC474D-L000598](../../tests/test_api.py#L598) | 598 | `"            try:"` | — |
| [SRC-3451CC474D-L000599](../../tests/test_api.py#L599) | 599 | `"                chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000600](../../tests/test_api.py#L600) | 600 | `"            except TimeoutError:"` | — |
| [SRC-3451CC474D-L000601](../../tests/test_api.py#L601) | 601 | `"                break"` | — |
| [SRC-3451CC474D-L000602](../../tests/test_api.py#L602) | 602 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000603](../../tests/test_api.py#L603) | 603 | `"                break"` | — |
| [SRC-3451CC474D-L000604](../../tests/test_api.py#L604) | 604 | `"            response.extend(chunk)"` | — |
| [SRC-3451CC474D-L000605](../../tests/test_api.py#L605) | 605 | `""` | — |
| [SRC-3451CC474D-L000606](../../tests/test_api.py#L606) | 606 | `"    elapsed = time.monotonic() - started"` | — |
| [SRC-3451CC474D-L000607](../../tests/test_api.py#L607) | 607 | `"    assert response.startswith(b\"HTTP/1.0 408\")"` | — |
| [SRC-3451CC474D-L000608](../../tests/test_api.py#L608) | 608 | `"    assert b\"request body read timed out\" in response"` | — |
| [SRC-3451CC474D-L000609](../../tests/test_api.py#L609) | 609 | `"    assert elapsed < 1.5"` | — |
| [SRC-3451CC474D-L000610](../../tests/test_api.py#L610) | 610 | `""` | — |
| [SRC-3451CC474D-L000611](../../tests/test_api.py#L611) | 611 | `""` | — |
| [SRC-3451CC474D-L000612](../../tests/test_api.py#L612) | 612 | `""` | — |
| [SRC-3451CC474D-L000613](../../tests/test_api.py#L613) | 613 | `"def test_api_absolute_header_deadline_stops_slow_trickle(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000614](../../tests/test_api.py#L614) | 614 | `"    \"\"\"Header bytes arriving before idle timeout must not extend the total deadline.\"\"\""` | — |
| [SRC-3451CC474D-L000615](../../tests/test_api.py#L615) | 615 | `"    import time"` | — |
| [SRC-3451CC474D-L000616](../../tests/test_api.py#L616) | 616 | `""` | — |
| [SRC-3451CC474D-L000617](../../tests/test_api.py#L617) | 617 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000618](../../tests/test_api.py#L618) | 618 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000619](../../tests/test_api.py#L619) | 619 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_HEADER_READ_TIMEOUT_SECONDS\", 0.5)"` | — |
| [SRC-3451CC474D-L000620](../../tests/test_api.py#L620) | 620 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_HEADER_IDLE_TIMEOUT_SECONDS\", 0.35)"` | — |
| [SRC-3451CC474D-L000621](../../tests/test_api.py#L621) | 621 | `"    host, port = local_api.removeprefix(\"http://\").rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000622](../../tests/test_api.py#L622) | 622 | `""` | — |
| [SRC-3451CC474D-L000623](../../tests/test_api.py#L623) | 623 | `"    with socket.create_connection((host, int(port)), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000624](../../tests/test_api.py#L624) | 624 | `"        client.settimeout(1.2)"` | — |
| [SRC-3451CC474D-L000625](../../tests/test_api.py#L625) | 625 | `"        started = time.monotonic()"` | — |
| [SRC-3451CC474D-L000626](../../tests/test_api.py#L626) | 626 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000627](../../tests/test_api.py#L627) | 627 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000628](../../tests/test_api.py#L628) | 628 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000629](../../tests/test_api.py#L629) | 629 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000630](../../tests/test_api.py#L630) | 630 | `"            b\"Content-Length: 40\\r\\n\""` | — |
| [SRC-3451CC474D-L000631](../../tests/test_api.py#L631) | 631 | `"            b\"X-Slow: \""` | — |
| [SRC-3451CC474D-L000632](../../tests/test_api.py#L632) | 632 | `"        )"` | — |
| [SRC-3451CC474D-L000633](../../tests/test_api.py#L633) | 633 | `"        # Each tiny fragment is sent well before the 0.35s idle timeout. No"` | — |
| [SRC-3451CC474D-L000634](../../tests/test_api.py#L634) | 634 | `"        # newline completes X-Slow, so only an absolute header deadline can stop it."` | — |
| [SRC-3451CC474D-L000635](../../tests/test_api.py#L635) | 635 | `"        for fragment in (b\"a\", b\"b\", b\"c\", b\"d\", b\"e\", b\"f\", b\"g\", b\"h\", b\"i\"):"` | — |
| [SRC-3451CC474D-L000636](../../tests/test_api.py#L636) | 636 | `"            time.sleep(0.12)"` | — |
| [SRC-3451CC474D-L000637](../../tests/test_api.py#L637) | 637 | `"            try:"` | — |
| [SRC-3451CC474D-L000638](../../tests/test_api.py#L638) | 638 | `"                client.sendall(fragment)"` | — |
| [SRC-3451CC474D-L000639](../../tests/test_api.py#L639) | 639 | `"            except OSError:"` | — |
| [SRC-3451CC474D-L000640](../../tests/test_api.py#L640) | 640 | `"                break"` | — |
| [SRC-3451CC474D-L000641](../../tests/test_api.py#L641) | 641 | `""` | — |
| [SRC-3451CC474D-L000642](../../tests/test_api.py#L642) | 642 | `"        response = bytearray()"` | — |
| [SRC-3451CC474D-L000643](../../tests/test_api.py#L643) | 643 | `"        while True:"` | — |
| [SRC-3451CC474D-L000644](../../tests/test_api.py#L644) | 644 | `"            try:"` | — |
| [SRC-3451CC474D-L000645](../../tests/test_api.py#L645) | 645 | `"                chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000646](../../tests/test_api.py#L646) | 646 | `"            except TimeoutError:"` | — |
| [SRC-3451CC474D-L000647](../../tests/test_api.py#L647) | 647 | `"                break"` | — |
| [SRC-3451CC474D-L000648](../../tests/test_api.py#L648) | 648 | `"            except OSError:"` | — |
| [SRC-3451CC474D-L000649](../../tests/test_api.py#L649) | 649 | `"                break"` | — |
| [SRC-3451CC474D-L000650](../../tests/test_api.py#L650) | 650 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000651](../../tests/test_api.py#L651) | 651 | `"                break"` | — |
| [SRC-3451CC474D-L000652](../../tests/test_api.py#L652) | 652 | `"            response.extend(chunk)"` | — |
| [SRC-3451CC474D-L000653](../../tests/test_api.py#L653) | 653 | `"        elapsed = time.monotonic() - started"` | — |
| [SRC-3451CC474D-L000654](../../tests/test_api.py#L654) | 654 | `""` | — |
| [SRC-3451CC474D-L000655](../../tests/test_api.py#L655) | 655 | `"    assert elapsed < 0.8"` | — |
| [SRC-3451CC474D-L000656](../../tests/test_api.py#L656) | 656 | `"    # The timed-out request never reached application dispatch; the handler closes silently."` | — |
| [SRC-3451CC474D-L000657](../../tests/test_api.py#L657) | 657 | `"    assert response == b\"\""` | — |
| [SRC-3451CC474D-L000658](../../tests/test_api.py#L658) | 658 | `""` | — |
| [SRC-3451CC474D-L000659](../../tests/test_api.py#L659) | 659 | `"def test_public_preflight_does_not_trust_spoofed_forwarded_host(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000660](../../tests/test_api.py#L660) | 660 | `"    \"\"\"A client-controlled X-Forwarded-Host must not grant an origin CORS access.\"\"\""` | — |
| [SRC-3451CC474D-L000661](../../tests/test_api.py#L661) | 661 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000662](../../tests/test_api.py#L662) | 662 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000663](../../tests/test_api.py#L663) | 663 | `""` | — |
| [SRC-3451CC474D-L000664](../../tests/test_api.py#L664) | 664 | `"    request = Request("` | — |
| [SRC-3451CC474D-L000665](../../tests/test_api.py#L665) | 665 | `"        local_api + \"/api/agent\","` | — |
| [SRC-3451CC474D-L000666](../../tests/test_api.py#L666) | 666 | `"        method=\"OPTIONS\","` | — |
| [SRC-3451CC474D-L000667](../../tests/test_api.py#L667) | 667 | `"        headers={"` | — |
| [SRC-3451CC474D-L000668](../../tests/test_api.py#L668) | 668 | `"            \"Origin\": \"https://attacker.example\","` | — |
| [SRC-3451CC474D-L000669](../../tests/test_api.py#L669) | 669 | `"            \"X-Forwarded-Host\": \"attacker.example\","` | — |
| [SRC-3451CC474D-L000670](../../tests/test_api.py#L670) | 670 | `"            \"X-Forwarded-Proto\": \"https\","` | — |
| [SRC-3451CC474D-L000671](../../tests/test_api.py#L671) | 671 | `"            \"Access-Control-Request-Method\": \"POST\","` | — |
| [SRC-3451CC474D-L000672](../../tests/test_api.py#L672) | 672 | `"            \"Access-Control-Request-Headers\": \"authorization,content-type\","` | — |
| [SRC-3451CC474D-L000673](../../tests/test_api.py#L673) | 673 | `"        },"` | — |
| [SRC-3451CC474D-L000674](../../tests/test_api.py#L674) | 674 | `"    )"` | — |
| [SRC-3451CC474D-L000675](../../tests/test_api.py#L675) | 675 | `"    with pytest.raises(HTTPError) as error:"` | — |
| [SRC-3451CC474D-L000676](../../tests/test_api.py#L676) | 676 | `"        urlopen(request, timeout=3)"` | — |
| [SRC-3451CC474D-L000677](../../tests/test_api.py#L677) | 677 | `"    assert error.value.code == 403"` | — |
| [SRC-3451CC474D-L000678](../../tests/test_api.py#L678) | 678 | `""` | — |
| [SRC-3451CC474D-L000679](../../tests/test_api.py#L679) | 679 | `""` | — |
| [SRC-3451CC474D-L000680](../../tests/test_api.py#L680) | 680 | `"def test_public_origin_still_allows_the_requested_host(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000681](../../tests/test_api.py#L681) | 681 | `"    \"\"\"Same-service public UI remains compatible when the request Host is trusted.\"\"\""` | — |
| [SRC-3451CC474D-L000682](../../tests/test_api.py#L682) | 682 | `"    from types import SimpleNamespace"` | — |
| [SRC-3451CC474D-L000683](../../tests/test_api.py#L683) | 683 | `""` | — |
| [SRC-3451CC474D-L000684](../../tests/test_api.py#L684) | 684 | `"    from api.omarai import Handler"` | — |
| [SRC-3451CC474D-L000685](../../tests/test_api.py#L685) | 685 | `""` | — |
| [SRC-3451CC474D-L000686](../../tests/test_api.py#L686) | 686 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000687](../../tests/test_api.py#L687) | 687 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000688](../../tests/test_api.py#L688) | 688 | `"    handler = SimpleNamespace("` | — |
| [SRC-3451CC474D-L000689](../../tests/test_api.py#L689) | 689 | `"        headers={"` | — |
| [SRC-3451CC474D-L000690](../../tests/test_api.py#L690) | 690 | `"            \"Host\": \"omarai.example\","` | — |
| [SRC-3451CC474D-L000691](../../tests/test_api.py#L691) | 691 | `"            \"X-Forwarded-Proto\": \"https\","` | — |
| [SRC-3451CC474D-L000692](../../tests/test_api.py#L692) | 692 | `"            \"X-Forwarded-Host\": \"attacker.example\","` | — |
| [SRC-3451CC474D-L000693](../../tests/test_api.py#L693) | 693 | `"        }"` | — |
| [SRC-3451CC474D-L000694](../../tests/test_api.py#L694) | 694 | `"    )"` | — |
| [SRC-3451CC474D-L000695](../../tests/test_api.py#L695) | 695 | `"    allowed = Handler._allowed_origins(handler)"` | — |
| [SRC-3451CC474D-L000696](../../tests/test_api.py#L696) | 696 | `"    assert \"https://omarai.example\" in allowed"` | — |
| [SRC-3451CC474D-L000697](../../tests/test_api.py#L697) | 697 | `"    assert \"https://attacker.example\" not in allowed"` | — |
| [SRC-3451CC474D-L000698](../../tests/test_api.py#L698) | 698 | `""` | — |
| [SRC-3451CC474D-L000699](../../tests/test_api.py#L699) | 699 | `""` | — |
| [SRC-3451CC474D-L000700](../../tests/test_api.py#L700) | 700 | `""` | — |
| [SRC-3451CC474D-L000701](../../tests/test_api.py#L701) | 701 | `"def test_security_headers_apply_to_json_and_html_responses(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000702](../../tests/test_api.py#L702) | 702 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000703](../../tests/test_api.py#L703) | 703 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000704](../../tests/test_api.py#L704) | 704 | `"    for path in (\"/api/health\", \"/\"):"` | — |
| [SRC-3451CC474D-L000705](../../tests/test_api.py#L705) | 705 | `"        request = Request(local_api + path)"` | — |
| [SRC-3451CC474D-L000706](../../tests/test_api.py#L706) | 706 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000707](../../tests/test_api.py#L707) | 707 | `"            headers = {name.lower(): value for name, value in response.headers.items()}"` | — |
| [SRC-3451CC474D-L000708](../../tests/test_api.py#L708) | 708 | `"            assert headers[\"x-content-type-options\"] == \"nosniff\""` | — |
| [SRC-3451CC474D-L000709](../../tests/test_api.py#L709) | 709 | `"            assert headers[\"x-frame-options\"] == \"DENY\""` | — |
| [SRC-3451CC474D-L000710](../../tests/test_api.py#L710) | 710 | `"            assert headers[\"referrer-policy\"] == \"strict-origin-when-cross-origin\""` | — |
| [SRC-3451CC474D-L000711](../../tests/test_api.py#L711) | 711 | `"            assert \"default-src 'self'\" in headers[\"content-security-policy\"]"` | — |
| [SRC-3451CC474D-L000712](../../tests/test_api.py#L712) | 712 | `"            policy = headers[\"content-security-policy\"]"` | — |
| [SRC-3451CC474D-L000713](../../tests/test_api.py#L713) | 713 | `"            assert \"frame-ancestors 'none'\" in policy"` | — |
| [SRC-3451CC474D-L000714](../../tests/test_api.py#L714) | 714 | `"            assert \"'unsafe-inline'\" not in policy"` | — |
| [SRC-3451CC474D-L000715](../../tests/test_api.py#L715) | 715 | `"            assert \"'sha256-\" in policy"` | — |
| [SRC-3451CC474D-L000716](../../tests/test_api.py#L716) | 716 | `"            assert headers[\"permissions-policy\"] == ("` | — |
| [SRC-3451CC474D-L000717](../../tests/test_api.py#L717) | 717 | `"                \"camera=(), microphone=(), geolocation=()\""` | — |
| [SRC-3451CC474D-L000718](../../tests/test_api.py#L718) | 718 | `"            )"` | — |
| [SRC-3451CC474D-L000719](../../tests/test_api.py#L719) | 719 | `""` | — |
| [SRC-3451CC474D-L000720](../../tests/test_api.py#L720) | 720 | `""` | — |
| [SRC-3451CC474D-L000721](../../tests/test_api.py#L721) | 721 | `"def test_health_exposes_only_validated_image_baked_sha(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L000722](../../tests/test_api.py#L722) | 722 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000723](../../tests/test_api.py#L723) | 723 | `""` | — |
| [SRC-3451CC474D-L000724](../../tests/test_api.py#L724) | 724 | `"    build_sha_file = tmp_path / \"BUILD_SHA\""` | — |
| [SRC-3451CC474D-L000725](../../tests/test_api.py#L725) | 725 | `"    monkeypatch.setattr(api_module, \"BUILD_SHA_FILE\", build_sha_file)"` | — |
| [SRC-3451CC474D-L000726](../../tests/test_api.py#L726) | 726 | `"    assert api_module._build_sha() == \"unknown\""` | — |
| [SRC-3451CC474D-L000727](../../tests/test_api.py#L727) | 727 | `"    build_sha_file.write_text(\"a\" * 40, encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000728](../../tests/test_api.py#L728) | 728 | `"    assert api_module._build_sha() == \"a\" * 40"` | — |
| [SRC-3451CC474D-L000729](../../tests/test_api.py#L729) | 729 | `"    build_sha_file.write_text(\"not-a-git-sha\", encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000730](../../tests/test_api.py#L730) | 730 | `"    assert api_module._build_sha() == \"unknown\""` | — |
| [SRC-3451CC474D-L000731](../../tests/test_api.py#L731) | 731 | `""` | — |
| [SRC-3451CC474D-L000732](../../tests/test_api.py#L732) | 732 | `""` | — |
| [SRC-3451CC474D-L000733](../../tests/test_api.py#L733) | 733 | `""` | — |
| [SRC-3451CC474D-L000734](../../tests/test_api.py#L734) | 734 | `"@pytest.mark.parametrize("` | — |
| [SRC-3451CC474D-L000735](../../tests/test_api.py#L735) | 735 | `"    (\"variable\", \"source\"),"` | — |
| [SRC-3451CC474D-L000736](../../tests/test_api.py#L736) | 736 | `"    ["` | — |
| [SRC-3451CC474D-L000737](../../tests/test_api.py#L737) | 737 | `"        (\"RAILWAY_GIT_COMMIT_SHA\", \"platform:railway\"),"` | — |
| [SRC-3451CC474D-L000738](../../tests/test_api.py#L738) | 738 | `"        (\"RENDER_GIT_COMMIT\", \"platform:render\"),"` | — |
| [SRC-3451CC474D-L000739](../../tests/test_api.py#L739) | 739 | `"    ],"` | — |
| [SRC-3451CC474D-L000740](../../tests/test_api.py#L740) | 740 | `")"` | — |
| [SRC-3451CC474D-L000741](../../tests/test_api.py#L741) | 741 | `"def test_build_identity_uses_validated_platform_commit_when_image_sha_is_unavailable("` | — |
| [SRC-3451CC474D-L000742](../../tests/test_api.py#L742) | 742 | `"    monkeypatch, tmp_path, variable, source"` | — |
| [SRC-3451CC474D-L000743](../../tests/test_api.py#L743) | 743 | `"):"` | — |
| [SRC-3451CC474D-L000744](../../tests/test_api.py#L744) | 744 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000745](../../tests/test_api.py#L745) | 745 | `""` | — |
| [SRC-3451CC474D-L000746](../../tests/test_api.py#L746) | 746 | `"    build_sha_file = tmp_path / \"BUILD_SHA\""` | — |
| [SRC-3451CC474D-L000747](../../tests/test_api.py#L747) | 747 | `"    monkeypatch.setattr(api_module, \"BUILD_SHA_FILE\", build_sha_file)"` | — |
| [SRC-3451CC474D-L000748](../../tests/test_api.py#L748) | 748 | `"    build_sha_file.write_text(\"unknown\", encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000749](../../tests/test_api.py#L749) | 749 | `"    for name, _label in api_module._PLATFORM_BUILD_SHA_ENVIRONMENTS:"` | — |
| [SRC-3451CC474D-L000750](../../tests/test_api.py#L750) | 750 | `"        monkeypatch.delenv(name, raising=False)"` | — |
| [SRC-3451CC474D-L000751](../../tests/test_api.py#L751) | 751 | `"    monkeypatch.setenv(variable, \"b\" * 40)"` | — |
| [SRC-3451CC474D-L000752](../../tests/test_api.py#L752) | 752 | `""` | — |
| [SRC-3451CC474D-L000753](../../tests/test_api.py#L753) | 753 | `"    assert api_module._build_identity() == (\"b\" * 40, source)"` | — |
| [SRC-3451CC474D-L000754](../../tests/test_api.py#L754) | 754 | `""` | — |
| [SRC-3451CC474D-L000755](../../tests/test_api.py#L755) | 755 | `""` | — |
| [SRC-3451CC474D-L000756](../../tests/test_api.py#L756) | 756 | `"def test_invalid_platform_commit_does_not_create_build_identity(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L000757](../../tests/test_api.py#L757) | 757 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000758](../../tests/test_api.py#L758) | 758 | `""` | — |
| [SRC-3451CC474D-L000759](../../tests/test_api.py#L759) | 759 | `"    monkeypatch.setattr(api_module, \"BUILD_SHA_FILE\", tmp_path / \"BUILD_SHA\")"` | — |
| [SRC-3451CC474D-L000760](../../tests/test_api.py#L760) | 760 | `"    api_module.BUILD_SHA_FILE.write_text(\"unknown\", encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000761](../../tests/test_api.py#L761) | 761 | `"    monkeypatch.setenv(\"RAILWAY_GIT_COMMIT_SHA\", \"not-a-sha\")"` | — |
| [SRC-3451CC474D-L000762](../../tests/test_api.py#L762) | 762 | `"    monkeypatch.setenv(\"RENDER_GIT_COMMIT\", \"also-not-a-sha\")"` | — |
| [SRC-3451CC474D-L000763](../../tests/test_api.py#L763) | 763 | `""` | — |
| [SRC-3451CC474D-L000764](../../tests/test_api.py#L764) | 764 | `"    assert api_module._build_identity() == (\"unknown\", \"unknown\")"` | — |
| [SRC-3451CC474D-L000765](../../tests/test_api.py#L765) | 765 | `""` | — |
| [SRC-3451CC474D-L000766](../../tests/test_api.py#L766) | 766 | `""` | — |
| [SRC-3451CC474D-L000767](../../tests/test_api.py#L767) | 767 | `""` | — |
| [SRC-3451CC474D-L000768](../../tests/test_api.py#L768) | 768 | `"def test_lead_store_uses_configured_database_path(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L000769](../../tests/test_api.py#L769) | 769 | `"    from api.omarai import _lead_store_from_environment"` | — |
| [SRC-3451CC474D-L000770](../../tests/test_api.py#L770) | 770 | `""` | — |
| [SRC-3451CC474D-L000771](../../tests/test_api.py#L771) | 771 | `"    database_path = tmp_path / \"persistent\" / \"omarai.sqlite3\""` | — |
| [SRC-3451CC474D-L000772](../../tests/test_api.py#L772) | 772 | `"    monkeypatch.setenv(\"OMARAI_DB_PATH\", str(database_path))"` | — |
| [SRC-3451CC474D-L000773](../../tests/test_api.py#L773) | 773 | `""` | — |
| [SRC-3451CC474D-L000774](../../tests/test_api.py#L774) | 774 | `"    store = _lead_store_from_environment()"` | — |
| [SRC-3451CC474D-L000775](../../tests/test_api.py#L775) | 775 | `""` | — |
| [SRC-3451CC474D-L000776](../../tests/test_api.py#L776) | 776 | `"    assert store.path == database_path"` | — |
| [SRC-3451CC474D-L000777](../../tests/test_api.py#L777) | 777 | `"    assert database_path.is_file()"` | — |
| [SRC-3451CC474D-L000778](../../tests/test_api.py#L778) | 778 | `""` | — |
| [SRC-3451CC474D-L000779](../../tests/test_api.py#L779) | 779 | `""` | — |
| [SRC-3451CC474D-L000780](../../tests/test_api.py#L780) | 780 | `""` | — |
| [SRC-3451CC474D-L000781](../../tests/test_api.py#L781) | 781 | `"def test_agent_concurrency_slot_released_after_operation_error(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000782](../../tests/test_api.py#L782) | 782 | `"    from api.omarai import WebAgent"` | — |
| [SRC-3451CC474D-L000783](../../tests/test_api.py#L783) | 783 | `""` | — |
| [SRC-3451CC474D-L000784](../../tests/test_api.py#L784) | 784 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000785](../../tests/test_api.py#L785) | 785 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000786](../../tests/test_api.py#L786) | 786 | `"    monkeypatch.setattr(Handler, \"_request_times\", defaultdict(deque))"` | — |
| [SRC-3451CC474D-L000787](../../tests/test_api.py#L787) | 787 | `"    monkeypatch.setattr(Handler, \"_rate_last_cleanup\", 0.0)"` | — |
| [SRC-3451CC474D-L000788](../../tests/test_api.py#L788) | 788 | `"    monkeypatch.setattr(Handler, \"_agent_semaphore\", threading.BoundedSemaphore(1))"` | — |
| [SRC-3451CC474D-L000789](../../tests/test_api.py#L789) | 789 | `"    state = {\"fail\": True}"` | — |
| [SRC-3451CC474D-L000790](../../tests/test_api.py#L790) | 790 | `""` | — |
| [SRC-3451CC474D-L000791](../../tests/test_api.py#L791) | 791 | `"    def answer_with_one_transient_failure(self, question, history=None, mode=\"auto\"):"` | — |
| [SRC-3451CC474D-L000792](../../tests/test_api.py#L792) | 792 | `"        if state[\"fail\"]:"` | — |
| [SRC-3451CC474D-L000793](../../tests/test_api.py#L793) | 793 | `"            raise RuntimeError(\"synthetic operation failure\")"` | — |
| [SRC-3451CC474D-L000794](../../tests/test_api.py#L794) | 794 | `"        return {"` | — |
| [SRC-3451CC474D-L000795](../../tests/test_api.py#L795) | 795 | `"            \"answer\": \"اختبار ناجح\","` | — |
| [SRC-3451CC474D-L000796](../../tests/test_api.py#L796) | 796 | `"            \"question\": question,"` | — |
| [SRC-3451CC474D-L000797](../../tests/test_api.py#L797) | 797 | `"            \"search_query\": question,"` | — |
| [SRC-3451CC474D-L000798](../../tests/test_api.py#L798) | 798 | `"            \"search_queries\": [],"` | — |
| [SRC-3451CC474D-L000799](../../tests/test_api.py#L799) | 799 | `"            \"search_report\": {"` | — |
| [SRC-3451CC474D-L000800](../../tests/test_api.py#L800) | 800 | `"                \"search_attempted\": False,"` | — |
| [SRC-3451CC474D-L000801](../../tests/test_api.py#L801) | 801 | `"                \"search_outcome\": \"not_attempted\","` | — |
| [SRC-3451CC474D-L000802](../../tests/test_api.py#L802) | 802 | `"            },"` | — |
| [SRC-3451CC474D-L000803](../../tests/test_api.py#L803) | 803 | `"            \"sources\": [],"` | — |
| [SRC-3451CC474D-L000804](../../tests/test_api.py#L804) | 804 | `"            \"used_language_model\": False,"` | — |
| [SRC-3451CC474D-L000805](../../tests/test_api.py#L805) | 805 | `"            \"used_web_search\": False,"` | — |
| [SRC-3451CC474D-L000806](../../tests/test_api.py#L806) | 806 | `"            \"search_attempted\": False,"` | — |
| [SRC-3451CC474D-L000807](../../tests/test_api.py#L807) | 807 | `"            \"used_social_search\": False,"` | — |
| [SRC-3451CC474D-L000808](../../tests/test_api.py#L808) | 808 | `"            \"warnings\": [],"` | — |
| [SRC-3451CC474D-L000809](../../tests/test_api.py#L809) | 809 | `"            \"kind\": \"web_fallback\","` | — |
| [SRC-3451CC474D-L000810](../../tests/test_api.py#L810) | 810 | `"        }"` | — |
| [SRC-3451CC474D-L000811](../../tests/test_api.py#L811) | 811 | `""` | — |
| [SRC-3451CC474D-L000812](../../tests/test_api.py#L812) | 812 | `"    monkeypatch.setattr(WebAgent, \"answer\", answer_with_one_transient_failure)"` | — |
| [SRC-3451CC474D-L000813](../../tests/test_api.py#L813) | 813 | `""` | — |
| [SRC-3451CC474D-L000814](../../tests/test_api.py#L814) | 814 | `"    status, payload = request_json("` | — |
| [SRC-3451CC474D-L000815](../../tests/test_api.py#L815) | 815 | `"        local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"الطلب الأول\"}"` | — |
| [SRC-3451CC474D-L000816](../../tests/test_api.py#L816) | 816 | `"    )"` | — |
| [SRC-3451CC474D-L000817](../../tests/test_api.py#L817) | 817 | `"    assert status == 500"` | — |
| [SRC-3451CC474D-L000818](../../tests/test_api.py#L818) | 818 | `"    assert payload[\"error\"] == \"internal server error\""` | — |
| [SRC-3451CC474D-L000819](../../tests/test_api.py#L819) | 819 | `""` | — |
| [SRC-3451CC474D-L000820](../../tests/test_api.py#L820) | 820 | `"    state[\"fail\"] = False"` | — |
| [SRC-3451CC474D-L000821](../../tests/test_api.py#L821) | 821 | `"    status, payload = request_json("` | — |
| [SRC-3451CC474D-L000822](../../tests/test_api.py#L822) | 822 | `"        local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"الطلب الثاني\"}"` | — |
| [SRC-3451CC474D-L000823](../../tests/test_api.py#L823) | 823 | `"    )"` | — |
| [SRC-3451CC474D-L000824](../../tests/test_api.py#L824) | 824 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000825](../../tests/test_api.py#L825) | 825 | `"    assert payload[\"answer\"] == \"اختبار ناجح\""` | — |
| [SRC-3451CC474D-L000826](../../tests/test_api.py#L826) | 826 | `""` | — |
| [SRC-3451CC474D-L000827](../../tests/test_api.py#L827) | 827 | `""` | — |
| [SRC-3451CC474D-L000828](../../tests/test_api.py#L828) | 828 | `"def test_csp_hashes_match_all_first_party_inline_content_and_attributes():"` | — |
| [SRC-3451CC474D-L000829](../../tests/test_api.py#L829) | 829 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000830](../../tests/test_api.py#L830) | 830 | `""` | — |
| [SRC-3451CC474D-L000831](../../tests/test_api.py#L831) | 831 | `"    policy = api_module._content_security_policy()"` | — |
| [SRC-3451CC474D-L000832](../../tests/test_api.py#L832) | 832 | `"    assert \"'unsafe-inline'\" not in policy"` | — |
| [SRC-3451CC474D-L000833](../../tests/test_api.py#L833) | 833 | `"    script_blocks = 0"` | — |
| [SRC-3451CC474D-L000834](../../tests/test_api.py#L834) | 834 | `"    style_blocks = 0"` | — |
| [SRC-3451CC474D-L000835](../../tests/test_api.py#L835) | 835 | `"    style_attributes = 0"` | — |
| [SRC-3451CC474D-L000836](../../tests/test_api.py#L836) | 836 | `"    for html_path in api_module.ROOT.glob(\"*.html\"):"` | — |
| [SRC-3451CC474D-L000837](../../tests/test_api.py#L837) | 837 | `"        document = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3451CC474D-L000838](../../tests/test_api.py#L838) | 838 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000839](../../tests/test_api.py#L839) | 839 | `"            r\"<script\\b(?P<attrs>[^>]*)>(?P<body>.*?)</script\\s*>\","` | — |
| [SRC-3451CC474D-L000840](../../tests/test_api.py#L840) | 840 | `"            document,"` | — |
| [SRC-3451CC474D-L000841](../../tests/test_api.py#L841) | 841 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L000842](../../tests/test_api.py#L842) | 842 | `"        ):"` | — |
| [SRC-3451CC474D-L000843](../../tests/test_api.py#L843) | 843 | `"            if re.search(r\"\\bsrc\\s*=\", match.group(\"attrs\"), re.IGNORECASE):"` | — |
| [SRC-3451CC474D-L000844](../../tests/test_api.py#L844) | 844 | `"                continue"` | — |
| [SRC-3451CC474D-L000845](../../tests/test_api.py#L845) | 845 | `"            script_blocks += 1"` | — |
| [SRC-3451CC474D-L000846](../../tests/test_api.py#L846) | 846 | `"            assert api_module._csp_hash_source(match.group(\"body\")) in policy"` | — |
| [SRC-3451CC474D-L000847](../../tests/test_api.py#L847) | 847 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000848](../../tests/test_api.py#L848) | 848 | `"            r\"<style\\b[^>]*>(?P<body>.*?)</style\\s*>\","` | — |
| [SRC-3451CC474D-L000849](../../tests/test_api.py#L849) | 849 | `"            document,"` | — |
| [SRC-3451CC474D-L000850](../../tests/test_api.py#L850) | 850 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L000851](../../tests/test_api.py#L851) | 851 | `"        ):"` | — |
| [SRC-3451CC474D-L000852](../../tests/test_api.py#L852) | 852 | `"            style_blocks += 1"` | — |
| [SRC-3451CC474D-L000853](../../tests/test_api.py#L853) | 853 | `"            assert api_module._csp_hash_source(match.group(\"body\")) in policy"` | — |
| [SRC-3451CC474D-L000854](../../tests/test_api.py#L854) | 854 | `"        for match in re.finditer("` | — |
| [SRC-3451CC474D-L000855](../../tests/test_api.py#L855) | 855 | `"            r\"\"\"\\bstyle\\s*=\\s*([\"'])(.*?)\\1\"\"\","` | — |
| [SRC-3451CC474D-L000856](../../tests/test_api.py#L856) | 856 | `"            document,"` | — |
| [SRC-3451CC474D-L000857](../../tests/test_api.py#L857) | 857 | `"            re.IGNORECASE \| re.DOTALL,"` | — |
| [SRC-3451CC474D-L000858](../../tests/test_api.py#L858) | 858 | `"        ):"` | — |
| [SRC-3451CC474D-L000859](../../tests/test_api.py#L859) | 859 | `"            style_attributes += 1"` | — |
| [SRC-3451CC474D-L000860](../../tests/test_api.py#L860) | 860 | `"            assert api_module._csp_hash_source(match.group(2).strip()) in policy"` | — |
| [SRC-3451CC474D-L000861](../../tests/test_api.py#L861) | 861 | `"    assert script_blocks >= 2"` | — |
| [SRC-3451CC474D-L000862](../../tests/test_api.py#L862) | 862 | `"    assert style_blocks >= 2"` | — |
| [SRC-3451CC474D-L000863](../../tests/test_api.py#L863) | 863 | `"    assert style_attributes >= 10"` | — |
| [SRC-3451CC474D-L000864](../../tests/test_api.py#L864) | 864 | `""` | — |
| [SRC-3451CC474D-L000865](../../tests/test_api.py#L865) | 865 | `""` | — |
| [SRC-3451CC474D-L000866](../../tests/test_api.py#L866) | 866 | `"def test_dashboard_uses_delegated_status_action_not_inline_onclick():"` | — |
| [SRC-3451CC474D-L000867](../../tests/test_api.py#L867) | 867 | `"    dashboard = (Path(__file__).resolve().parents[1] / \"web\" / \"dashboard.html\").read_text("` | — |
| [SRC-3451CC474D-L000868](../../tests/test_api.py#L868) | 868 | `"        encoding=\"utf-8\""` | — |
| [SRC-3451CC474D-L000869](../../tests/test_api.py#L869) | 869 | `"    )"` | — |
| [SRC-3451CC474D-L000870](../../tests/test_api.py#L870) | 870 | `"    assert 'data-action=\"save-status\"' in dashboard"` | — |
| [SRC-3451CC474D-L000871](../../tests/test_api.py#L871) | 871 | `"    assert 'onclick=\"saveStatus' not in dashboard"` | — |
| [SRC-3451CC474D-L000872](../../tests/test_api.py#L872) | 872 | `"    assert \"\"\"data-lead-id=\"'+esc(l.id)+'\">\"\"\" in dashboard"` | — |
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
| [SRC-DA61479D59-L000182](../../tests/test_connector_summary_counters.py#L182) | 182 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda _query: results)"` | — |
| [SRC-DA61479D59-L000183](../../tests/test_connector_summary_counters.py#L183) | 183 | `""` | — |
| [SRC-DA61479D59-L000184](../../tests/test_connector_summary_counters.py#L184) | 184 | `"    def fetch(url: str):"` | — |
| [SRC-DA61479D59-L000185](../../tests/test_connector_summary_counters.py#L185) | 185 | `"        if \"example.com\" in url:"` | — |
| [SRC-DA61479D59-L000186](../../tests/test_connector_summary_counters.py#L186) | 186 | `"            return PageFetchResult("` | — |
| [SRC-DA61479D59-L000187](../../tests/test_connector_summary_counters.py#L187) | 187 | `"                \"Report page\","` | — |
| [SRC-DA61479D59-L000188](../../tests/test_connector_summary_counters.py#L188) | 188 | `"                \"Renewable energy storage body, with an explicit note that extraction was capped.\","` | — |
| [SRC-DA61479D59-L000189](../../tests/test_connector_summary_counters.py#L189) | 189 | `"                \"partial_extraction\","` | — |
| [SRC-DA61479D59-L000190](../../tests/test_connector_summary_counters.py#L190) | 190 | `"            )"` | — |
| [SRC-DA61479D59-L000191](../../tests/test_connector_summary_counters.py#L191) | 191 | `"        return PageFetchResult(\"\", \"\", \"http_error\", \"HTTPStatus\")"` | — |
| [SRC-DA61479D59-L000192](../../tests/test_connector_summary_counters.py#L192) | 192 | `""` | — |
| [SRC-DA61479D59-L000193](../../tests/test_connector_summary_counters.py#L193) | 193 | `"    monkeypatch.setattr(agent, \"_fetch_page\", fetch)"` | — |
| [SRC-DA61479D59-L000194](../../tests/test_connector_summary_counters.py#L194) | 194 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-DA61479D59-L000195](../../tests/test_connector_summary_counters.py#L195) | 195 | `"        \"queries\": [query],"` | — |
| [SRC-DA61479D59-L000196](../../tests/test_connector_summary_counters.py#L196) | 196 | `"        \"direct_urls\": [],"` | — |
| [SRC-DA61479D59-L000197](../../tests/test_connector_summary_counters.py#L197) | 197 | `"        \"social_focus\": False,"` | — |
| [SRC-DA61479D59-L000198](../../tests/test_connector_summary_counters.py#L198) | 198 | `"        \"freshness\": \"any\","` | — |
| [SRC-DA61479D59-L000199](../../tests/test_connector_summary_counters.py#L199) | 199 | `"        \"depth\": \"standard\","` | — |
| [SRC-DA61479D59-L000200](../../tests/test_connector_summary_counters.py#L200) | 200 | `"        \"platforms\": [],"` | — |
| [SRC-DA61479D59-L000201](../../tests/test_connector_summary_counters.py#L201) | 201 | `"        \"planning_method\": \"unit_test\","` | — |
| [SRC-DA61479D59-L000202](../../tests/test_connector_summary_counters.py#L202) | 202 | `"    })"` | — |
| [SRC-DA61479D59-L000203](../../tests/test_connector_summary_counters.py#L203) | 203 | `""` | — |
| [SRC-DA61479D59-L000204](../../tests/test_connector_summary_counters.py#L204) | 204 | `"    assert warnings"` | — |
| [SRC-DA61479D59-L000205](../../tests/test_connector_summary_counters.py#L205) | 205 | `"    assert report[\"pages_fetch_attempted\"] == 2"` | — |
| [SRC-DA61479D59-L000206](../../tests/test_connector_summary_counters.py#L206) | 206 | `"    assert report[\"pages_content_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000207](../../tests/test_connector_summary_counters.py#L207) | 207 | `"    assert report[\"pages_partial_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000208](../../tests/test_connector_summary_counters.py#L208) | 208 | `"    assert report[\"pages_extract_failed\"] == 1"` | — |
| [SRC-DA61479D59-L000209](../../tests/test_connector_summary_counters.py#L209) | 209 | `"    assert report[\"page_fetch_status_counts\"][\"partial_extraction\"] == 1"` | — |
| [SRC-DA61479D59-L000210](../../tests/test_connector_summary_counters.py#L210) | 210 | `"    assert report[\"page_fetch_status_counts\"][\"http_error\"] == 1"` | — |
| [SRC-DA61479D59-L000211](../../tests/test_connector_summary_counters.py#L211) | 211 | `"    assert sum(item[\"page_fetch_status\"] == \"partial_extraction\" for item in sources) == 1"` | — |
| [SRC-DA61479D59-L000212](../../tests/test_connector_summary_counters.py#L212) | 212 | `"    assert sum(item[\"page_fetch_status\"] == \"http_error\" for item in sources) == 1"` | — |
| [SRC-DA61479D59-L000213](../../tests/test_connector_summary_counters.py#L213) | 213 | `"    assert any(\"HTTPStatus\" in str(item.get(\"page_fetch_error_class\")) for item in sources)"` | — |
| [SRC-DA61479D59-L000214](../../tests/test_connector_summary_counters.py#L214) | 214 | `""` | — |
| [SRC-DA61479D59-L000215](../../tests/test_connector_summary_counters.py#L215) | 215 | `""` | — |
| [SRC-DA61479D59-L000216](../../tests/test_connector_summary_counters.py#L216) | 216 | `"def test_raw_provider_diagnostics_redact_credentials_from_queries_and_errors():"` | — |
| [SRC-DA61479D59-L000217](../../tests/test_connector_summary_counters.py#L217) | 217 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000218](../../tests/test_connector_summary_counters.py#L218) | 218 | `"    agent._record_provider_diagnostic("` | — |
| [SRC-DA61479D59-L000219](../../tests/test_connector_summary_counters.py#L219) | 219 | `"        provider=\"test_provider\","` | — |
| [SRC-DA61479D59-L000220](../../tests/test_connector_summary_counters.py#L220) | 220 | `"        query=\"research API_KEY=query-secret\","` | — |
| [SRC-DA61479D59-L000221](../../tests/test_connector_summary_counters.py#L221) | 221 | `"        status=\"failed\","` | — |
| [SRC-DA61479D59-L000222](../../tests/test_connector_summary_counters.py#L222) | 222 | `"        error=("` | — |
| [SRC-DA61479D59-L000223](../../tests/test_connector_summary_counters.py#L223) | 223 | `"            \"Authorization: Bearer bearer-secret access_token=access-secret; \""` | — |
| [SRC-DA61479D59-L000224](../../tests/test_connector_summary_counters.py#L224) | 224 | `"            \"URL https://example.test/search?token=url-secret\""` | — |
| [SRC-DA61479D59-L000225](../../tests/test_connector_summary_counters.py#L225) | 225 | `"        ),"` | — |
| [SRC-DA61479D59-L000226](../../tests/test_connector_summary_counters.py#L226) | 226 | `"    )"` | — |
| [SRC-DA61479D59-L000227](../../tests/test_connector_summary_counters.py#L227) | 227 | `""` | — |
| [SRC-DA61479D59-L000228](../../tests/test_connector_summary_counters.py#L228) | 228 | `"    diagnostic_json = json.dumps(agent._provider_diagnostics, ensure_ascii=False)"` | — |
| [SRC-DA61479D59-L000229](../../tests/test_connector_summary_counters.py#L229) | 229 | `"    for secret in (\"query-secret\", \"bearer-secret\", \"access-secret\", \"url-secret\"):"` | — |
| [SRC-DA61479D59-L000230](../../tests/test_connector_summary_counters.py#L230) | 230 | `"        assert secret not in diagnostic_json"` | — |
| [SRC-DA61479D59-L000231](../../tests/test_connector_summary_counters.py#L231) | 231 | `"    assert \"[REDACTED]\" in diagnostic_json"` | — |
| [SRC-DA61479D59-L000232](../../tests/test_connector_summary_counters.py#L232) | 232 | `""` | — |
| [SRC-DA61479D59-L000233](../../tests/test_connector_summary_counters.py#L233) | 233 | `""` | — |
| [SRC-DA61479D59-L000234](../../tests/test_connector_summary_counters.py#L234) | 234 | `"def test_connector_summary_separates_raw_candidates_from_filtered_results():"` | — |
| [SRC-DA61479D59-L000235](../../tests/test_connector_summary_counters.py#L235) | 235 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000236](../../tests/test_connector_summary_counters.py#L236) | 236 | `"    summary = agent._connector_status_summary("` | — |
| [SRC-DA61479D59-L000237](../../tests/test_connector_summary_counters.py#L237) | 237 | `"        [{"` | — |
| [SRC-DA61479D59-L000238](../../tests/test_connector_summary_counters.py#L238) | 238 | `"            \"provider\": \"bing_rss\","` | — |
| [SRC-DA61479D59-L000239](../../tests/test_connector_summary_counters.py#L239) | 239 | `"            \"query\": \"Arabic question with source instructions\","` | — |
| [SRC-DA61479D59-L000240](../../tests/test_connector_summary_counters.py#L240) | 240 | `"            \"status\": \"filtered_all\","` | — |
| [SRC-DA61479D59-L000241](../../tests/test_connector_summary_counters.py#L241) | 241 | `"            \"result_count\": 6,"` | — |
| [SRC-DA61479D59-L000242](../../tests/test_connector_summary_counters.py#L242) | 242 | `"            \"accepted_count\": 0,"` | — |
| [SRC-DA61479D59-L000243](../../tests/test_connector_summary_counters.py#L243) | 243 | `"            \"rejected_count\": 6,"` | — |
| [SRC-DA61479D59-L000244](../../tests/test_connector_summary_counters.py#L244) | 244 | `"            \"rejection_counts\": {"` | — |
| [SRC-DA61479D59-L000245](../../tests/test_connector_summary_counters.py#L245) | 245 | `"                \"malformed_candidate\": 0,"` | — |
| [SRC-DA61479D59-L000246](../../tests/test_connector_summary_counters.py#L246) | 246 | `"                \"invalid_url_or_unsafe_target\": 2,"` | — |
| [SRC-DA61479D59-L000247](../../tests/test_connector_summary_counters.py#L247) | 247 | `"                \"blocked_domain\": 1,"` | — |
| [SRC-DA61479D59-L000248](../../tests/test_connector_summary_counters.py#L248) | 248 | `"                \"relevance_below_threshold\": 3,"` | — |
| [SRC-DA61479D59-L000249](../../tests/test_connector_summary_counters.py#L249) | 249 | `"            },"` | — |
| [SRC-DA61479D59-L000250](../../tests/test_connector_summary_counters.py#L250) | 250 | `"            \"error\": \"all candidates rejected; invalid_url_or_unsafe_target=2, blocked_domain=1, relevance_below_threshold=3\","` | — |
| [SRC-DA61479D59-L000251](../../tests/test_connector_summary_counters.py#L251) | 251 | `"        }],"` | — |
| [SRC-DA61479D59-L000252](../../tests/test_connector_summary_counters.py#L252) | 252 | `"        [],"` | — |
| [SRC-DA61479D59-L000253](../../tests/test_connector_summary_counters.py#L253) | 253 | `"    )"` | — |
| [SRC-DA61479D59-L000254](../../tests/test_connector_summary_counters.py#L254) | 254 | `"    bing = next(item for item in summary[\"connectors\"] if item[\"name\"] == \"bing_rss\")"` | — |
| [SRC-DA61479D59-L000255](../../tests/test_connector_summary_counters.py#L255) | 255 | `"    assert bing[\"attempted\"] is True"` | — |
| [SRC-DA61479D59-L000256](../../tests/test_connector_summary_counters.py#L256) | 256 | `"    assert bing[\"result_count\"] == 6"` | — |
| [SRC-DA61479D59-L000257](../../tests/test_connector_summary_counters.py#L257) | 257 | `"    assert bing[\"accepted_count\"] == 0"` | — |
| [SRC-DA61479D59-L000258](../../tests/test_connector_summary_counters.py#L258) | 258 | `"    assert bing[\"rejected_count\"] == 6"` | — |
| [SRC-DA61479D59-L000259](../../tests/test_connector_summary_counters.py#L259) | 259 | `"    assert bing[\"rejection_counts_observed\"] is True"` | — |
| [SRC-DA61479D59-L000260](../../tests/test_connector_summary_counters.py#L260) | 260 | `"    assert bing[\"rejection_counts\"] == {"` | — |
| [SRC-DA61479D59-L000261](../../tests/test_connector_summary_counters.py#L261) | 261 | `"        \"malformed_candidate\": 0,"` | — |
| [SRC-DA61479D59-L000262](../../tests/test_connector_summary_counters.py#L262) | 262 | `"        \"invalid_url_or_unsafe_target\": 2,"` | — |
| [SRC-DA61479D59-L000263](../../tests/test_connector_summary_counters.py#L263) | 263 | `"        \"blocked_domain\": 1,"` | — |
| [SRC-DA61479D59-L000264](../../tests/test_connector_summary_counters.py#L264) | 264 | `"        \"relevance_below_threshold\": 3,"` | — |
| [SRC-DA61479D59-L000265](../../tests/test_connector_summary_counters.py#L265) | 265 | `"    }"` | — |
| [SRC-DA61479D59-L000266](../../tests/test_connector_summary_counters.py#L266) | 266 | `"    assert sum(bing[\"rejection_counts\"].values()) == bing[\"rejected_count\"]"` | — |
| [SRC-DA61479D59-L000267](../../tests/test_connector_summary_counters.py#L267) | 267 | `"    assert bing[\"candidate_rejection_observed\"] is True"` | — |
| [SRC-DA61479D59-L000268](../../tests/test_connector_summary_counters.py#L268) | 268 | `"    assert bing[\"available_for_this_request\"] is True"` | — |
| [SRC-DA61479D59-L000269](../../tests/test_connector_summary_counters.py#L269) | 269 | `"    assert bing[\"verified_for_this_request\"] is True"` | — |
| [SRC-DA61479D59-L000270](../../tests/test_connector_summary_counters.py#L270) | 270 | `""` | — |
| [SRC-DA61479D59-L000271](../../tests/test_connector_summary_counters.py#L271) | 271 | `""` | — |
| [SRC-DA61479D59-L000272](../../tests/test_connector_summary_counters.py#L272) | 272 | `"def test_connector_summary_does_not_present_partial_legacy_rejection_counts_as_complete():"` | — |
| [SRC-DA61479D59-L000273](../../tests/test_connector_summary_counters.py#L273) | 273 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000274](../../tests/test_connector_summary_counters.py#L274) | 274 | `"    summary = agent._connector_status_summary("` | — |
| [SRC-DA61479D59-L000275](../../tests/test_connector_summary_counters.py#L275) | 275 | `"        ["` | — |
| [SRC-DA61479D59-L000276](../../tests/test_connector_summary_counters.py#L276) | 276 | `"            {"` | — |
| [SRC-DA61479D59-L000277](../../tests/test_connector_summary_counters.py#L277) | 277 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-DA61479D59-L000278](../../tests/test_connector_summary_counters.py#L278) | 278 | `"                \"query\": \"first query\","` | — |
| [SRC-DA61479D59-L000279](../../tests/test_connector_summary_counters.py#L279) | 279 | `"                \"status\": \"filtered_all\","` | — |
| [SRC-DA61479D59-L000280](../../tests/test_connector_summary_counters.py#L280) | 280 | `"                \"result_count\": 3,"` | — |
| [SRC-DA61479D59-L000281](../../tests/test_connector_summary_counters.py#L281) | 281 | `"                \"accepted_count\": 0,"` | — |
| [SRC-DA61479D59-L000282](../../tests/test_connector_summary_counters.py#L282) | 282 | `"                \"rejected_count\": 3,"` | — |
| [SRC-DA61479D59-L000283](../../tests/test_connector_summary_counters.py#L283) | 283 | `"            },"` | — |
| [SRC-DA61479D59-L000284](../../tests/test_connector_summary_counters.py#L284) | 284 | `"            {"` | — |
| [SRC-DA61479D59-L000285](../../tests/test_connector_summary_counters.py#L285) | 285 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-DA61479D59-L000286](../../tests/test_connector_summary_counters.py#L286) | 286 | `"                \"query\": \"second query\","` | — |
| [SRC-DA61479D59-L000287](../../tests/test_connector_summary_counters.py#L287) | 287 | `"                \"status\": \"filtered_all\","` | — |
| [SRC-DA61479D59-L000288](../../tests/test_connector_summary_counters.py#L288) | 288 | `"                \"result_count\": 2,"` | — |
| [SRC-DA61479D59-L000289](../../tests/test_connector_summary_counters.py#L289) | 289 | `"                \"accepted_count\": 0,"` | — |
| [SRC-DA61479D59-L000290](../../tests/test_connector_summary_counters.py#L290) | 290 | `"                \"rejected_count\": 2,"` | — |
| [SRC-DA61479D59-L000291](../../tests/test_connector_summary_counters.py#L291) | 291 | `"                \"rejection_counts\": {"` | — |
| [SRC-DA61479D59-L000292](../../tests/test_connector_summary_counters.py#L292) | 292 | `"                    \"malformed_candidate\": 0,"` | — |
| [SRC-DA61479D59-L000293](../../tests/test_connector_summary_counters.py#L293) | 293 | `"                    \"invalid_url_or_unsafe_target\": 0,"` | — |
| [SRC-DA61479D59-L000294](../../tests/test_connector_summary_counters.py#L294) | 294 | `"                    \"blocked_domain\": 0,"` | — |
| [SRC-DA61479D59-L000295](../../tests/test_connector_summary_counters.py#L295) | 295 | `"                    \"relevance_below_threshold\": 2,"` | — |
| [SRC-DA61479D59-L000296](../../tests/test_connector_summary_counters.py#L296) | 296 | `"                },"` | — |
| [SRC-DA61479D59-L000297](../../tests/test_connector_summary_counters.py#L297) | 297 | `"            },"` | — |
| [SRC-DA61479D59-L000298](../../tests/test_connector_summary_counters.py#L298) | 298 | `"        ],"` | — |
| [SRC-DA61479D59-L000299](../../tests/test_connector_summary_counters.py#L299) | 299 | `"        [],"` | — |
| [SRC-DA61479D59-L000300](../../tests/test_connector_summary_counters.py#L300) | 300 | `"    )"` | — |
| [SRC-DA61479D59-L000301](../../tests/test_connector_summary_counters.py#L301) | 301 | `"    bing = next(item for item in summary[\"connectors\"] if item[\"name\"] == \"bing_rss\")"` | — |
| [SRC-DA61479D59-L000302](../../tests/test_connector_summary_counters.py#L302) | 302 | `"    assert bing[\"rejected_count\"] == 5"` | — |
| [SRC-DA61479D59-L000303](../../tests/test_connector_summary_counters.py#L303) | 303 | `"    assert bing[\"rejection_counts_observed\"] is False"` | — |
| [SRC-DA61479D59-L000304](../../tests/test_connector_summary_counters.py#L304) | 304 | `"    assert bing[\"rejection_counts\"] is None"` | — |
## اختبارات

### FILE-3D0A619359 — [tests/test_dashboard_security.py](../../tests/test_dashboard_security.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3D0A619359-L000001](../../tests/test_dashboard_security.py#L1) | 1 | `"\"\"\"Static regression checks for sensitive lead-dashboard browser behavior.\"\"\""` | — |
| [SRC-3D0A619359-L000002](../../tests/test_dashboard_security.py#L2) | 2 | `"from pathlib import Path"` | — |
| [SRC-3D0A619359-L000003](../../tests/test_dashboard_security.py#L3) | 3 | `""` | — |
| [SRC-3D0A619359-L000004](../../tests/test_dashboard_security.py#L4) | 4 | `"DASHBOARD = Path(__file__).resolve().parents[1] / \"web\" / \"dashboard.html\""` | — |
| [SRC-3D0A619359-L000005](../../tests/test_dashboard_security.py#L5) | 5 | `""` | — |
| [SRC-3D0A619359-L000006](../../tests/test_dashboard_security.py#L6) | 6 | `""` | — |
| [SRC-3D0A619359-L000007](../../tests/test_dashboard_security.py#L7) | 7 | `"def test_hosted_lead_dashboard_can_send_the_private_access_token():"` | — |
| [SRC-3D0A619359-L000008](../../tests/test_dashboard_security.py#L8) | 8 | `"    html = DASHBOARD.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000009](../../tests/test_dashboard_security.py#L9) | 9 | `"    assert 'const ACCESS_TOKEN_STORAGE_KEY=\"omarai_access_token\"' in html"` | — |
| [SRC-3D0A619359-L000010](../../tests/test_dashboard_security.py#L10) | 10 | `"    assert 'headers.Authorization=\"Bearer \"+token' in html"` | — |
| [SRC-3D0A619359-L000011](../../tests/test_dashboard_security.py#L11) | 11 | `"    assert '$(\"saveAccessToken\").onclick' in html"` | — |
| [SRC-3D0A619359-L000012](../../tests/test_dashboard_security.py#L12) | 12 | `""` | — |
| [SRC-3D0A619359-L000013](../../tests/test_dashboard_security.py#L13) | 13 | `""` | — |
| [SRC-3D0A619359-L000014](../../tests/test_dashboard_security.py#L14) | 14 | `"def test_saved_lead_source_links_reject_non_http_schemes():"` | — |
| [SRC-3D0A619359-L000015](../../tests/test_dashboard_security.py#L15) | 15 | `"    html = DASHBOARD.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000016](../../tests/test_dashboard_security.py#L16) | 16 | `"    assert \"function safeSourceUrl(value)\" in html"` | — |
| [SRC-3D0A619359-L000017](../../tests/test_dashboard_security.py#L17) | 17 | `"    assert '[\"http:\",\"https:\"]' in html"` | — |
| [SRC-3D0A619359-L000018](../../tests/test_dashboard_security.py#L18) | 18 | `"    assert \"const sourceUrl=safeSourceUrl(l.source_url)\" in html"` | — |
| [SRC-3D0A619359-L000019](../../tests/test_dashboard_security.py#L19) | 19 | `"    assert \"const sourceLink=sourceUrl?\" in html"` | — |
## اختبارات

### FILE-29A9CD43D1 — [tests/test_dialogue_context_pipeline.py](../../tests/test_dialogue_context_pipeline.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-29A9CD43D1-L000001](../../tests/test_dialogue_context_pipeline.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-29A9CD43D1-L000002](../../tests/test_dialogue_context_pipeline.py#L2) | 2 | `""` | — |
| [SRC-29A9CD43D1-L000003](../../tests/test_dialogue_context_pipeline.py#L3) | 3 | `"import json"` | — |
| [SRC-29A9CD43D1-L000004](../../tests/test_dialogue_context_pipeline.py#L4) | 4 | `"from typing import Any"` | — |
| [SRC-29A9CD43D1-L000005](../../tests/test_dialogue_context_pipeline.py#L5) | 5 | `""` | — |
| [SRC-29A9CD43D1-L000006](../../tests/test_dialogue_context_pipeline.py#L6) | 6 | `"import pytest"` | — |
| [SRC-29A9CD43D1-L000007](../../tests/test_dialogue_context_pipeline.py#L7) | 7 | `""` | — |
| [SRC-29A9CD43D1-L000008](../../tests/test_dialogue_context_pipeline.py#L8) | 8 | `"from agents.research import evidence_signal_report"` | — |
| [SRC-29A9CD43D1-L000009](../../tests/test_dialogue_context_pipeline.py#L9) | 9 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-29A9CD43D1-L000010](../../tests/test_dialogue_context_pipeline.py#L10) | 10 | `""` | — |
| [SRC-29A9CD43D1-L000011](../../tests/test_dialogue_context_pipeline.py#L11) | 11 | `""` | — |
| [SRC-29A9CD43D1-L000012](../../tests/test_dialogue_context_pipeline.py#L12) | 12 | `"def _source(domain: str, queries: list[str]) -> dict[str, Any]:"` | — |
| [SRC-29A9CD43D1-L000013](../../tests/test_dialogue_context_pipeline.py#L13) | 13 | `"    return {"` | — |
| [SRC-29A9CD43D1-L000014](../../tests/test_dialogue_context_pipeline.py#L14) | 14 | `"        \"title\": \"iPhone 17 256GB international warranty coverage in Egypt\","` | — |
| [SRC-29A9CD43D1-L000015](../../tests/test_dialogue_context_pipeline.py#L15) | 15 | `"        \"url\": f\"https://{domain}/iphone-warranty\","` | — |
| [SRC-29A9CD43D1-L000016](../../tests/test_dialogue_context_pipeline.py#L16) | 16 | `"        \"snippet\": \"Warranty coverage and service policy for iPhone 17 in Egypt.\","` | — |
| [SRC-29A9CD43D1-L000017](../../tests/test_dialogue_context_pipeline.py#L17) | 17 | `"        \"page_text\": \"Warranty coverage and service policy for iPhone 17 in Egypt.\","` | — |
| [SRC-29A9CD43D1-L000018](../../tests/test_dialogue_context_pipeline.py#L18) | 18 | `"        \"page_fetched\": True,"` | — |
| [SRC-29A9CD43D1-L000019](../../tests/test_dialogue_context_pipeline.py#L19) | 19 | `"        \"providers\": [\"test_search\"],"` | — |
| [SRC-29A9CD43D1-L000020](../../tests/test_dialogue_context_pipeline.py#L20) | 20 | `"        \"queries\": list(queries),"` | — |
| [SRC-29A9CD43D1-L000021](../../tests/test_dialogue_context_pipeline.py#L21) | 21 | `"        \"domain\": domain,"` | — |
| [SRC-29A9CD43D1-L000022](../../tests/test_dialogue_context_pipeline.py#L22) | 22 | `"        \"source_class\": \"general\","` | — |
| [SRC-29A9CD43D1-L000023](../../tests/test_dialogue_context_pipeline.py#L23) | 23 | `"        \"platform\": \"web\","` | — |
| [SRC-29A9CD43D1-L000024](../../tests/test_dialogue_context_pipeline.py#L24) | 24 | `"        \"published_at\": \"\","` | — |
| [SRC-29A9CD43D1-L000025](../../tests/test_dialogue_context_pipeline.py#L25) | 25 | `"        \"rank_score\": 1.0,"` | — |
| [SRC-29A9CD43D1-L000026](../../tests/test_dialogue_context_pipeline.py#L26) | 26 | `"    }"` | — |
| [SRC-29A9CD43D1-L000027](../../tests/test_dialogue_context_pipeline.py#L27) | 27 | `""` | — |
| [SRC-29A9CD43D1-L000028](../../tests/test_dialogue_context_pipeline.py#L28) | 28 | `""` | — |
| [SRC-29A9CD43D1-L000029](../../tests/test_dialogue_context_pipeline.py#L29) | 29 | `"def _report(plan: dict[str, Any], sources: list[dict[str, Any]]) -> dict[str, Any]:"` | — |
| [SRC-29A9CD43D1-L000030](../../tests/test_dialogue_context_pipeline.py#L30) | 30 | `"    return {"` | — |
| [SRC-29A9CD43D1-L000031](../../tests/test_dialogue_context_pipeline.py#L31) | 31 | `"        \"queries_planned\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-29A9CD43D1-L000032](../../tests/test_dialogue_context_pipeline.py#L32) | 32 | `"        \"queries_attempted\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-29A9CD43D1-L000033](../../tests/test_dialogue_context_pipeline.py#L33) | 33 | `"        \"queries_attempted_known\": True,"` | — |
| [SRC-29A9CD43D1-L000034](../../tests/test_dialogue_context_pipeline.py#L34) | 34 | `"        \"search_attempted\": True,"` | — |
| [SRC-29A9CD43D1-L000035](../../tests/test_dialogue_context_pipeline.py#L35) | 35 | `"        \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-29A9CD43D1-L000036](../../tests/test_dialogue_context_pipeline.py#L36) | 36 | `"        \"query_results\": [],"` | — |
| [SRC-29A9CD43D1-L000037](../../tests/test_dialogue_context_pipeline.py#L37) | 37 | `"        \"unique_sources\": len(sources),"` | — |
| [SRC-29A9CD43D1-L000038](../../tests/test_dialogue_context_pipeline.py#L38) | 38 | `"        \"pages_fetched\": len(sources),"` | — |
| [SRC-29A9CD43D1-L000039](../../tests/test_dialogue_context_pipeline.py#L39) | 39 | `"        \"providers_used\": [\"test_search\"],"` | — |
| [SRC-29A9CD43D1-L000040](../../tests/test_dialogue_context_pipeline.py#L40) | 40 | `"        \"provider_counts\": {\"test_search\": len(sources)},"` | — |
| [SRC-29A9CD43D1-L000041](../../tests/test_dialogue_context_pipeline.py#L41) | 41 | `"        \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-29A9CD43D1-L000042](../../tests/test_dialogue_context_pipeline.py#L42) | 42 | `"        \"social_direct_results\": 0,"` | — |
| [SRC-29A9CD43D1-L000043](../../tests/test_dialogue_context_pipeline.py#L43) | 43 | `"        \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-29A9CD43D1-L000044](../../tests/test_dialogue_context_pipeline.py#L44) | 44 | `"        \"planning_method\": plan.get(\"planning_method\", \"test\"),"` | — |
| [SRC-29A9CD43D1-L000045](../../tests/test_dialogue_context_pipeline.py#L45) | 45 | `"        \"evidence_signals\": evidence_signal_report(sources),"` | — |
| [SRC-29A9CD43D1-L000046](../../tests/test_dialogue_context_pipeline.py#L46) | 46 | `"    }"` | — |
| [SRC-29A9CD43D1-L000047](../../tests/test_dialogue_context_pipeline.py#L47) | 47 | `""` | — |
| [SRC-29A9CD43D1-L000048](../../tests/test_dialogue_context_pipeline.py#L48) | 48 | `""` | — |
| [SRC-29A9CD43D1-L000049](../../tests/test_dialogue_context_pipeline.py#L49) | 49 | `"def _semantic_context(*, needs_clarification: bool = False) -> dict[str, Any]:"` | — |
| [SRC-29A9CD43D1-L000050](../../tests/test_dialogue_context_pipeline.py#L50) | 50 | `"    return {"` | — |
| [SRC-29A9CD43D1-L000051](../../tests/test_dialogue_context_pipeline.py#L51) | 51 | `"        \"resolved_question\": ("` | — |
| [SRC-29A9CD43D1-L000052](../../tests/test_dialogue_context_pipeline.py#L52) | 52 | `"            \"هل الضمان الدولي لهاتف iPhone 17 سعة 256 جيجابايت الذي اشتريته \""` | — |
| [SRC-29A9CD43D1-L000053](../../tests/test_dialogue_context_pipeline.py#L53) | 53 | `"            \"في مصر يغطي الصيانة داخل مصر؟\""` | — |
| [SRC-29A9CD43D1-L000054](../../tests/test_dialogue_context_pipeline.py#L54) | 54 | `"        ),"` | — |
| [SRC-29A9CD43D1-L000055](../../tests/test_dialogue_context_pipeline.py#L55) | 55 | `"        \"intent\": \"current_information\","` | — |
| [SRC-29A9CD43D1-L000056](../../tests/test_dialogue_context_pipeline.py#L56) | 56 | `"        \"topic\": \"تغطية الضمان\","` | — |
| [SRC-29A9CD43D1-L000057](../../tests/test_dialogue_context_pipeline.py#L57) | 57 | `"        \"entities\": [\"iPhone 17\"],"` | — |
| [SRC-29A9CD43D1-L000058](../../tests/test_dialogue_context_pipeline.py#L58) | 58 | `"        \"slots\": {"` | — |
| [SRC-29A9CD43D1-L000059](../../tests/test_dialogue_context_pipeline.py#L59) | 59 | `"            \"product\": \"iPhone 17\","` | — |
| [SRC-29A9CD43D1-L000060](../../tests/test_dialogue_context_pipeline.py#L60) | 60 | `"            \"capacity\": \"256 جيجابايت\","` | — |
| [SRC-29A9CD43D1-L000061](../../tests/test_dialogue_context_pipeline.py#L61) | 61 | `"            \"country\": \"مصر\","` | — |
| [SRC-29A9CD43D1-L000062](../../tests/test_dialogue_context_pipeline.py#L62) | 62 | `"            \"aspect\": \"الضمان الدولي والصيانة داخل مصر\","` | — |
| [SRC-29A9CD43D1-L000063](../../tests/test_dialogue_context_pipeline.py#L63) | 63 | `"        },"` | — |
| [SRC-29A9CD43D1-L000064](../../tests/test_dialogue_context_pipeline.py#L64) | 64 | `"        \"changed_slots\": [\"aspect\"],"` | — |
| [SRC-29A9CD43D1-L000065](../../tests/test_dialogue_context_pipeline.py#L65) | 65 | `"        \"is_follow_up\": True,"` | — |
| [SRC-29A9CD43D1-L000066](../../tests/test_dialogue_context_pipeline.py#L66) | 66 | `"        \"topic_shift\": False,"` | — |
| [SRC-29A9CD43D1-L000067](../../tests/test_dialogue_context_pipeline.py#L67) | 67 | `"        \"needs_web\": True,"` | — |
| [SRC-29A9CD43D1-L000068](../../tests/test_dialogue_context_pipeline.py#L68) | 68 | `"        \"research_depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000069](../../tests/test_dialogue_context_pipeline.py#L69) | 69 | `"        \"needs_clarification\": needs_clarification,"` | — |
| [SRC-29A9CD43D1-L000070](../../tests/test_dialogue_context_pipeline.py#L70) | 70 | `"        \"clarification_question\": ("` | — |
| [SRC-29A9CD43D1-L000071](../../tests/test_dialogue_context_pipeline.py#L71) | 71 | `"            \"تقصد ضمان أي هاتف تحديدًا، أم تريد مقارنة ضمان الهاتفين؟\""` | — |
| [SRC-29A9CD43D1-L000072](../../tests/test_dialogue_context_pipeline.py#L72) | 72 | `"            if needs_clarification else \"\""` | — |
| [SRC-29A9CD43D1-L000073](../../tests/test_dialogue_context_pipeline.py#L73) | 73 | `"        ),"` | — |
| [SRC-29A9CD43D1-L000074](../../tests/test_dialogue_context_pipeline.py#L74) | 74 | `"        \"unresolved_references\": [\"الضمان\"] if needs_clarification else [],"` | — |
| [SRC-29A9CD43D1-L000075](../../tests/test_dialogue_context_pipeline.py#L75) | 75 | `"        \"resolution_basis\": \"history_inferred\","` | — |
| [SRC-29A9CD43D1-L000076](../../tests/test_dialogue_context_pipeline.py#L76) | 76 | `"        \"confidence_band\": \"medium\","` | — |
| [SRC-29A9CD43D1-L000077](../../tests/test_dialogue_context_pipeline.py#L77) | 77 | `"    }"` | — |
| [SRC-29A9CD43D1-L000078](../../tests/test_dialogue_context_pipeline.py#L78) | 78 | `""` | — |
| [SRC-29A9CD43D1-L000079](../../tests/test_dialogue_context_pipeline.py#L79) | 79 | `""` | — |
| [SRC-29A9CD43D1-L000080](../../tests/test_dialogue_context_pipeline.py#L80) | 80 | `"def test_semantic_context_probe_routes_natural_followup_to_search_and_answer("` | — |
| [SRC-29A9CD43D1-L000081](../../tests/test_dialogue_context_pipeline.py#L81) | 81 | `"    monkeypatch: pytest.MonkeyPatch,"` | — |
| [SRC-29A9CD43D1-L000082](../../tests/test_dialogue_context_pipeline.py#L82) | 82 | `") -> None:"` | — |
| [SRC-29A9CD43D1-L000083](../../tests/test_dialogue_context_pipeline.py#L83) | 83 | `"    agent = WebAgent()"` | — |
| [SRC-29A9CD43D1-L000084](../../tests/test_dialogue_context_pipeline.py#L84) | 84 | `"    agent.api_key = \"test-key\"  # All model responses are mocked; no provider call is made."` | — |
| [SRC-29A9CD43D1-L000085](../../tests/test_dialogue_context_pipeline.py#L85) | 85 | `"    history = ["` | — |
| [SRC-29A9CD43D1-L000086](../../tests/test_dialogue_context_pipeline.py#L86) | 86 | `"        {\"role\": \"user\", \"content\": \"اشتريت iPhone 17 النسخة الأساسية سعة 256 جيجابايت من مصر.\"},"` | — |
| [SRC-29A9CD43D1-L000087](../../tests/test_dialogue_context_pipeline.py#L87) | 87 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن نسخة iPhone 17 سعة 256 جيجابايت في مصر.\"},"` | — |
| [SRC-29A9CD43D1-L000088](../../tests/test_dialogue_context_pipeline.py#L88) | 88 | `"    ]"` | — |
| [SRC-29A9CD43D1-L000089](../../tests/test_dialogue_context_pipeline.py#L89) | 89 | `"    context = _semantic_context()"` | — |
| [SRC-29A9CD43D1-L000090](../../tests/test_dialogue_context_pipeline.py#L90) | 90 | `"    seen: dict[str, Any] = {\"model_prompts\": []}"` | — |
| [SRC-29A9CD43D1-L000091](../../tests/test_dialogue_context_pipeline.py#L91) | 91 | `""` | — |
| [SRC-29A9CD43D1-L000092](../../tests/test_dialogue_context_pipeline.py#L92) | 92 | `"    def mocked_completion(messages, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000093](../../tests/test_dialogue_context_pipeline.py#L93) | 93 | `"        system_prompt = messages[0][\"content\"]"` | — |
| [SRC-29A9CD43D1-L000094](../../tests/test_dialogue_context_pipeline.py#L94) | 94 | `"        seen[\"model_prompts\"].append(system_prompt)"` | — |
| [SRC-29A9CD43D1-L000095](../../tests/test_dialogue_context_pipeline.py#L95) | 95 | `"        if \"أنت محلل سياق حواري\" in system_prompt:"` | — |
| [SRC-29A9CD43D1-L000096](../../tests/test_dialogue_context_pipeline.py#L96) | 96 | `"            return json.dumps(context, ensure_ascii=False)"` | — |
| [SRC-29A9CD43D1-L000097](../../tests/test_dialogue_context_pipeline.py#L97) | 97 | `"        if \"أنت مخطط بحث ومحلل دلالي حواري\" in system_prompt:"` | — |
| [SRC-29A9CD43D1-L000098](../../tests/test_dialogue_context_pipeline.py#L98) | 98 | `"            return json.dumps("` | — |
| [SRC-29A9CD43D1-L000099](../../tests/test_dialogue_context_pipeline.py#L99) | 99 | `"                {"` | — |
| [SRC-29A9CD43D1-L000100](../../tests/test_dialogue_context_pipeline.py#L100) | 100 | `"                    \"queries\": ["` | — |
| [SRC-29A9CD43D1-L000101](../../tests/test_dialogue_context_pipeline.py#L101) | 101 | `"                        \"iPhone 17 256GB الضمان الدولي في مصر تغطية الصيانة warranty Egypt\""` | — |
| [SRC-29A9CD43D1-L000102](../../tests/test_dialogue_context_pipeline.py#L102) | 102 | `"                    ],"` | — |
| [SRC-29A9CD43D1-L000103](../../tests/test_dialogue_context_pipeline.py#L103) | 103 | `"                    \"direct_urls\": [],"` | — |
| [SRC-29A9CD43D1-L000104](../../tests/test_dialogue_context_pipeline.py#L104) | 104 | `"                    \"social_focus\": False,"` | — |
| [SRC-29A9CD43D1-L000105](../../tests/test_dialogue_context_pipeline.py#L105) | 105 | `"                    \"freshness\": \"current\","` | — |
| [SRC-29A9CD43D1-L000106](../../tests/test_dialogue_context_pipeline.py#L106) | 106 | `"                    \"depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000107](../../tests/test_dialogue_context_pipeline.py#L107) | 107 | `"                    \"platforms\": [],"` | — |
| [SRC-29A9CD43D1-L000108](../../tests/test_dialogue_context_pipeline.py#L108) | 108 | `"                    \"dialogue_context\": context,"` | — |
| [SRC-29A9CD43D1-L000109](../../tests/test_dialogue_context_pipeline.py#L109) | 109 | `"                },"` | — |
| [SRC-29A9CD43D1-L000110](../../tests/test_dialogue_context_pipeline.py#L110) | 110 | `"                ensure_ascii=False,"` | — |
| [SRC-29A9CD43D1-L000111](../../tests/test_dialogue_context_pipeline.py#L111) | 111 | `"            )"` | — |
| [SRC-29A9CD43D1-L000112](../../tests/test_dialogue_context_pipeline.py#L112) | 112 | `"        pytest.fail(\"Unexpected model prompt in mocked offline test\")"` | — |
| [SRC-29A9CD43D1-L000113](../../tests/test_dialogue_context_pipeline.py#L113) | 113 | `""` | — |
| [SRC-29A9CD43D1-L000114](../../tests/test_dialogue_context_pipeline.py#L114) | 114 | `"    monkeypatch.setattr(agent, \"_request_completion\", mocked_completion)"` | — |
| [SRC-29A9CD43D1-L000115](../../tests/test_dialogue_context_pipeline.py#L115) | 115 | `"    seen[\"generated_question\"] = None"` | — |
| [SRC-29A9CD43D1-L000116](../../tests/test_dialogue_context_pipeline.py#L116) | 116 | `"    seen[\"reviewed_question\"] = None"` | — |
| [SRC-29A9CD43D1-L000117](../../tests/test_dialogue_context_pipeline.py#L117) | 117 | `""` | — |
| [SRC-29A9CD43D1-L000118](../../tests/test_dialogue_context_pipeline.py#L118) | 118 | `"    def collect(plan):"` | — |
| [SRC-29A9CD43D1-L000119](../../tests/test_dialogue_context_pipeline.py#L119) | 119 | `"        seen[\"plan\"] = dict(plan)"` | — |
| [SRC-29A9CD43D1-L000120](../../tests/test_dialogue_context_pipeline.py#L120) | 120 | `"        sources = [_source(\"example.com\", plan[\"queries\"]), _source(\"example.net\", plan[\"queries\"])]"` | — |
| [SRC-29A9CD43D1-L000121](../../tests/test_dialogue_context_pipeline.py#L121) | 121 | `"        return sources, [], _report(plan, sources)"` | — |
| [SRC-29A9CD43D1-L000122](../../tests/test_dialogue_context_pipeline.py#L122) | 122 | `""` | — |
| [SRC-29A9CD43D1-L000123](../../tests/test_dialogue_context_pipeline.py#L123) | 123 | `"    def generate(resolved_question, *args, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000124](../../tests/test_dialogue_context_pipeline.py#L124) | 124 | `"        seen[\"generated_question\"] = resolved_question"` | — |
| [SRC-29A9CD43D1-L000125](../../tests/test_dialogue_context_pipeline.py#L125) | 125 | `"        return \"لم أؤكد شروط الضمان من النصوص المتاحة؛ راجع الشروط الرسمية [المصدر 1].\""` | — |
| [SRC-29A9CD43D1-L000126](../../tests/test_dialogue_context_pipeline.py#L126) | 126 | `""` | — |
| [SRC-29A9CD43D1-L000127](../../tests/test_dialogue_context_pipeline.py#L127) | 127 | `"    def review(resolved_question, answer, sources):"` | — |
| [SRC-29A9CD43D1-L000128](../../tests/test_dialogue_context_pipeline.py#L128) | 128 | `"        seen[\"reviewed_question\"] = resolved_question"` | — |
| [SRC-29A9CD43D1-L000129](../../tests/test_dialogue_context_pipeline.py#L129) | 129 | `"        return answer"` | — |
| [SRC-29A9CD43D1-L000130](../../tests/test_dialogue_context_pipeline.py#L130) | 130 | `""` | — |
| [SRC-29A9CD43D1-L000131](../../tests/test_dialogue_context_pipeline.py#L131) | 131 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-29A9CD43D1-L000132](../../tests/test_dialogue_context_pipeline.py#L132) | 132 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda _query, _source: True)"` | — |
| [SRC-29A9CD43D1-L000133](../../tests/test_dialogue_context_pipeline.py#L133) | 133 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-29A9CD43D1-L000134](../../tests/test_dialogue_context_pipeline.py#L134) | 134 | `"    monkeypatch.setattr(agent, \"_review_answer\", review)"` | — |
| [SRC-29A9CD43D1-L000135](../../tests/test_dialogue_context_pipeline.py#L135) | 135 | `""` | — |
| [SRC-29A9CD43D1-L000136](../../tests/test_dialogue_context_pipeline.py#L136) | 136 | `"    question = \"وطب الضمان الدولي بيسري في مصر؟\""` | — |
| [SRC-29A9CD43D1-L000137](../../tests/test_dialogue_context_pipeline.py#L137) | 137 | `"    result = agent.answer(question, history=history)"` | — |
| [SRC-29A9CD43D1-L000138](../../tests/test_dialogue_context_pipeline.py#L138) | 138 | `""` | — |
| [SRC-29A9CD43D1-L000139](../../tests/test_dialogue_context_pipeline.py#L139) | 139 | `"    assert result[\"intent_route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-29A9CD43D1-L000140](../../tests/test_dialogue_context_pipeline.py#L140) | 140 | `"    assert result[\"question\"] == question  # Preserve the visible user utterance."` | — |
| [SRC-29A9CD43D1-L000141](../../tests/test_dialogue_context_pipeline.py#L141) | 141 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-29A9CD43D1-L000142](../../tests/test_dialogue_context_pipeline.py#L142) | 142 | `"    assert len(seen[\"model_prompts\"]) == 2  # one context pass + one search-plan pass"` | — |
| [SRC-29A9CD43D1-L000143](../../tests/test_dialogue_context_pipeline.py#L143) | 143 | `"    assert \"iPhone 17\" in seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000144](../../tests/test_dialogue_context_pipeline.py#L144) | 144 | `"    assert \"256 جيجابايت\" in seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000145](../../tests/test_dialogue_context_pipeline.py#L145) | 145 | `"    assert \"الضمان الدولي\" in seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000146](../../tests/test_dialogue_context_pipeline.py#L146) | 146 | `"    assert seen[\"reviewed_question\"] == seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000147](../../tests/test_dialogue_context_pipeline.py#L147) | 147 | `"    context_result = result[\"research_plan\"][\"dialogue_context\"]"` | — |
| [SRC-29A9CD43D1-L000148](../../tests/test_dialogue_context_pipeline.py#L148) | 148 | `"    assert context_result[\"method\"] == \"llm_semantic_context\""` | — |
| [SRC-29A9CD43D1-L000149](../../tests/test_dialogue_context_pipeline.py#L149) | 149 | `"    assert context_result[\"slots\"][\"country\"] == \"مصر\""` | — |
| [SRC-29A9CD43D1-L000150](../../tests/test_dialogue_context_pipeline.py#L150) | 150 | `"    assert context_result[\"changed_slots\"] == [\"aspect\"]"` | — |
| [SRC-29A9CD43D1-L000151](../../tests/test_dialogue_context_pipeline.py#L151) | 151 | `"    assert context_result[\"needs_web\"] is True"` | — |
| [SRC-29A9CD43D1-L000152](../../tests/test_dialogue_context_pipeline.py#L152) | 152 | `""` | — |
| [SRC-29A9CD43D1-L000153](../../tests/test_dialogue_context_pipeline.py#L153) | 153 | `""` | — |
| [SRC-29A9CD43D1-L000154](../../tests/test_dialogue_context_pipeline.py#L154) | 154 | `"def test_semantic_context_asks_before_search_when_two_referents_are_plausible("` | — |
| [SRC-29A9CD43D1-L000155](../../tests/test_dialogue_context_pipeline.py#L155) | 155 | `"    monkeypatch: pytest.MonkeyPatch,"` | — |
| [SRC-29A9CD43D1-L000156](../../tests/test_dialogue_context_pipeline.py#L156) | 156 | `") -> None:"` | — |
| [SRC-29A9CD43D1-L000157](../../tests/test_dialogue_context_pipeline.py#L157) | 157 | `"    agent = WebAgent()"` | — |
| [SRC-29A9CD43D1-L000158](../../tests/test_dialogue_context_pipeline.py#L158) | 158 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-29A9CD43D1-L000159](../../tests/test_dialogue_context_pipeline.py#L159) | 159 | `"    history = ["` | — |
| [SRC-29A9CD43D1-L000160](../../tests/test_dialogue_context_pipeline.py#L160) | 160 | `"        {\"role\": \"user\", \"content\": \"قارن بين iPhone 17 وSamsung S26\"},"` | — |
| [SRC-29A9CD43D1-L000161](../../tests/test_dialogue_context_pipeline.py#L161) | 161 | `"        {\"role\": \"assistant\", \"content\": \"ذكرت الهاتفين في المقارنة.\"},"` | — |
| [SRC-29A9CD43D1-L000162](../../tests/test_dialogue_context_pipeline.py#L162) | 162 | `"    ]"` | — |
| [SRC-29A9CD43D1-L000163](../../tests/test_dialogue_context_pipeline.py#L163) | 163 | `"    ambiguous = {"` | — |
| [SRC-29A9CD43D1-L000164](../../tests/test_dialogue_context_pipeline.py#L164) | 164 | `"        \"resolved_question\": \"What about the second one?\","` | — |
| [SRC-29A9CD43D1-L000165](../../tests/test_dialogue_context_pipeline.py#L165) | 165 | `"        \"intent\": \"compare\","` | — |
| [SRC-29A9CD43D1-L000166](../../tests/test_dialogue_context_pipeline.py#L166) | 166 | `"        \"topic\": \"اختيار الهاتف\","` | — |
| [SRC-29A9CD43D1-L000167](../../tests/test_dialogue_context_pipeline.py#L167) | 167 | `"        \"entities\": [\"iPhone 17\", \"Samsung S26\"],"` | — |
| [SRC-29A9CD43D1-L000168](../../tests/test_dialogue_context_pipeline.py#L168) | 168 | `"        \"slots\": {\"aspect\": \"الاختيار\"},"` | — |
| [SRC-29A9CD43D1-L000169](../../tests/test_dialogue_context_pipeline.py#L169) | 169 | `"        \"changed_slots\": [],"` | — |
| [SRC-29A9CD43D1-L000170](../../tests/test_dialogue_context_pipeline.py#L170) | 170 | `"        \"is_follow_up\": True,"` | — |
