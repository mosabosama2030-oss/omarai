# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **047**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L002593 إلى SRC-F725E90B2A-L003392
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L002593](../../tests/test_web_agent.py#L2593) | 2593 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L002594](../../tests/test_web_agent.py#L2594) | 2594 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: draft_answer)"` | — |
| [SRC-F725E90B2A-L002595](../../tests/test_web_agent.py#L2595) | 2595 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002596](../../tests/test_web_agent.py#L2596) | 2596 | `"        agent, \"_review_answer\", lambda question, answer, review_sources: answer"` | — |
| [SRC-F725E90B2A-L002597](../../tests/test_web_agent.py#L2597) | 2597 | `"    )"` | — |
| [SRC-F725E90B2A-L002598](../../tests/test_web_agent.py#L2598) | 2598 | `""` | — |
| [SRC-F725E90B2A-L002599](../../tests/test_web_agent.py#L2599) | 2599 | `"    result = agent.answer(plan[\"queries\"][0], mode=\"deep\")"` | — |
| [SRC-F725E90B2A-L002600](../../tests/test_web_agent.py#L2600) | 2600 | `""` | — |
| [SRC-F725E90B2A-L002601](../../tests/test_web_agent.py#L2601) | 2601 | `"    assert result[\"used_language_model\"] is True"` | — |
| [SRC-F725E90B2A-L002602](../../tests/test_web_agent.py#L2602) | 2602 | `"    assert result[\"search_report\"][\"second_pass_review\"] == \"model_claim_audit_completed\""` | — |
| [SRC-F725E90B2A-L002603](../../tests/test_web_agent.py#L2603) | 2603 | `"    assert result[\"citation_validation\"][\"valid_citation_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002604](../../tests/test_web_agent.py#L2604) | 2604 | `"    assert result[\"research_quality\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L002605](../../tests/test_web_agent.py#L2605) | 2605 | `"    assert result[\"search_report\"][\"research_quality\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L002606](../../tests/test_web_agent.py#L2606) | 2606 | `"    assert result[\"answer_evidence_status\"] == \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-F725E90B2A-L002607](../../tests/test_web_agent.py#L2607) | 2607 | `"    assert result[\"citation_validation\"][\"claim_support\"] == ("` | — |
| [SRC-F725E90B2A-L002608](../../tests/test_web_agent.py#L2608) | 2608 | `"        \"not_established_no_valid_source_citations\""` | — |
| [SRC-F725E90B2A-L002609](../../tests/test_web_agent.py#L2609) | 2609 | `"    )"` | — |
| [SRC-F725E90B2A-L002610](../../tests/test_web_agent.py#L2610) | 2610 | `"    assert any(\"لا تحتوي على إحالات صالحة\" in warning for warning in result[\"warnings\"])"` | — |
| [SRC-F725E90B2A-L002611](../../tests/test_web_agent.py#L2611) | 2611 | `""` | — |
| [SRC-F725E90B2A-L002612](../../tests/test_web_agent.py#L2612) | 2612 | `"# Network-boundary regression tests. These use mocked transports and never make"` | — |
| [SRC-F725E90B2A-L002613](../../tests/test_web_agent.py#L2613) | 2613 | `"# an outbound connection; they protect against SSRF and redirect/DNS-rebinding regressions."` | — |
| [SRC-F725E90B2A-L002614](../../tests/test_web_agent.py#L2614) | 2614 | `"def test_public_ip_literals_rejects_mixed_public_and_private_dns_answers(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002615](../../tests/test_web_agent.py#L2615) | 2615 | `"    import socket"` | — |
| [SRC-F725E90B2A-L002616](../../tests/test_web_agent.py#L2616) | 2616 | `""` | — |
| [SRC-F725E90B2A-L002617](../../tests/test_web_agent.py#L2617) | 2617 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L002618](../../tests/test_web_agent.py#L2618) | 2618 | `""` | — |
| [SRC-F725E90B2A-L002619](../../tests/test_web_agent.py#L2619) | 2619 | `"    answers = ["` | — |
| [SRC-F725E90B2A-L002620](../../tests/test_web_agent.py#L2620) | 2620 | `"        (socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, \"\", (\"93.184.216.34\", 80)),"` | — |
| [SRC-F725E90B2A-L002621](../../tests/test_web_agent.py#L2621) | 2621 | `"        (socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, \"\", (\"10.10.0.8\", 80)),"` | — |
| [SRC-F725E90B2A-L002622](../../tests/test_web_agent.py#L2622) | 2622 | `"    ]"` | — |
| [SRC-F725E90B2A-L002623](../../tests/test_web_agent.py#L2623) | 2623 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002624](../../tests/test_web_agent.py#L2624) | 2624 | `"        web_agent.socket,"` | — |
| [SRC-F725E90B2A-L002625](../../tests/test_web_agent.py#L2625) | 2625 | `"        \"getaddrinfo\","` | — |
| [SRC-F725E90B2A-L002626](../../tests/test_web_agent.py#L2626) | 2626 | `"        lambda host, port, type: answers,"` | — |
| [SRC-F725E90B2A-L002627](../../tests/test_web_agent.py#L2627) | 2627 | `"    )"` | — |
| [SRC-F725E90B2A-L002628](../../tests/test_web_agent.py#L2628) | 2628 | `""` | — |
| [SRC-F725E90B2A-L002629](../../tests/test_web_agent.py#L2629) | 2629 | `"    # One private DNS answer must fail closed, even when another answer is public."` | — |
| [SRC-F725E90B2A-L002630](../../tests/test_web_agent.py#L2630) | 2630 | `"    assert web_agent._public_ip_literals(\"mixed.example\") is None"` | — |
| [SRC-F725E90B2A-L002631](../../tests/test_web_agent.py#L2631) | 2631 | `""` | — |
| [SRC-F725E90B2A-L002632](../../tests/test_web_agent.py#L2632) | 2632 | `""` | — |
| [SRC-F725E90B2A-L002633](../../tests/test_web_agent.py#L2633) | 2633 | `"def test_pinned_connect_url_uses_checked_ip_without_losing_logical_path():"` | — |
| [SRC-F725E90B2A-L002634](../../tests/test_web_agent.py#L2634) | 2634 | `"    from agents.web_agent import _pinned_connect_url"` | — |
| [SRC-F725E90B2A-L002635](../../tests/test_web_agent.py#L2635) | 2635 | `""` | — |
| [SRC-F725E90B2A-L002636](../../tests/test_web_agent.py#L2636) | 2636 | `"    assert _pinned_connect_url("` | — |
| [SRC-F725E90B2A-L002637](../../tests/test_web_agent.py#L2637) | 2637 | `"        \"https://example.test:443/path?q=1\","` | — |
| [SRC-F725E90B2A-L002638](../../tests/test_web_agent.py#L2638) | 2638 | `"        \"93.184.216.34\","` | — |
| [SRC-F725E90B2A-L002639](../../tests/test_web_agent.py#L2639) | 2639 | `"    ) == \"https://93.184.216.34:443/path?q=1\""` | — |
| [SRC-F725E90B2A-L002640](../../tests/test_web_agent.py#L2640) | 2640 | `""` | — |
| [SRC-F725E90B2A-L002641](../../tests/test_web_agent.py#L2641) | 2641 | `""` | — |
| [SRC-F725E90B2A-L002642](../../tests/test_web_agent.py#L2642) | 2642 | `"def test_fetch_page_rejects_private_redirect_before_connecting(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002643](../../tests/test_web_agent.py#L2643) | 2643 | `"    from contextlib import contextmanager"` | — |
| [SRC-F725E90B2A-L002644](../../tests/test_web_agent.py#L2644) | 2644 | `""` | — |
| [SRC-F725E90B2A-L002645](../../tests/test_web_agent.py#L2645) | 2645 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002646](../../tests/test_web_agent.py#L2646) | 2646 | `""` | — |
| [SRC-F725E90B2A-L002647](../../tests/test_web_agent.py#L2647) | 2647 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L002648](../../tests/test_web_agent.py#L2648) | 2648 | `""` | — |
| [SRC-F725E90B2A-L002649](../../tests/test_web_agent.py#L2649) | 2649 | `"    resolved_hosts = []"` | — |
| [SRC-F725E90B2A-L002650](../../tests/test_web_agent.py#L2650) | 2650 | `"    requests = []"` | — |
| [SRC-F725E90B2A-L002651](../../tests/test_web_agent.py#L2651) | 2651 | `""` | — |
| [SRC-F725E90B2A-L002652](../../tests/test_web_agent.py#L2652) | 2652 | `"    def resolve_public_ip(host):"` | — |
| [SRC-F725E90B2A-L002653](../../tests/test_web_agent.py#L2653) | 2653 | `"        resolved_hosts.append(host)"` | — |
| [SRC-F725E90B2A-L002654](../../tests/test_web_agent.py#L2654) | 2654 | `"        return [\"93.184.216.34\"] if host == \"first.example\" else None"` | — |
| [SRC-F725E90B2A-L002655](../../tests/test_web_agent.py#L2655) | 2655 | `""` | — |
| [SRC-F725E90B2A-L002656](../../tests/test_web_agent.py#L2656) | 2656 | `"    monkeypatch.setattr(web_agent, \"_public_ip_literals\", resolve_public_ip)"` | — |
| [SRC-F725E90B2A-L002657](../../tests/test_web_agent.py#L2657) | 2657 | `""` | — |
| [SRC-F725E90B2A-L002658](../../tests/test_web_agent.py#L2658) | 2658 | `"    class RedirectResponse:"` | — |
| [SRC-F725E90B2A-L002659](../../tests/test_web_agent.py#L2659) | 2659 | `"        status_code = 302"` | — |
| [SRC-F725E90B2A-L002660](../../tests/test_web_agent.py#L2660) | 2660 | `""` | — |
| [SRC-F725E90B2A-L002661](../../tests/test_web_agent.py#L2661) | 2661 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L002662](../../tests/test_web_agent.py#L2662) | 2662 | `"            self.headers = {\"location\": \"http://127.0.0.1/admin\"}"` | — |
| [SRC-F725E90B2A-L002663](../../tests/test_web_agent.py#L2663) | 2663 | `""` | — |
| [SRC-F725E90B2A-L002664](../../tests/test_web_agent.py#L2664) | 2664 | `"    @contextmanager"` | — |
| [SRC-F725E90B2A-L002665](../../tests/test_web_agent.py#L2665) | 2665 | `"    def fake_stream(self, method, url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002666](../../tests/test_web_agent.py#L2666) | 2666 | `"        requests.append((method, str(url), kwargs))"` | — |
| [SRC-F725E90B2A-L002667](../../tests/test_web_agent.py#L2667) | 2667 | `"        yield RedirectResponse()"` | — |
| [SRC-F725E90B2A-L002668](../../tests/test_web_agent.py#L2668) | 2668 | `""` | — |
| [SRC-F725E90B2A-L002669](../../tests/test_web_agent.py#L2669) | 2669 | `"    class FakeClient:"` | — |
| [SRC-F725E90B2A-L002670](../../tests/test_web_agent.py#L2670) | 2670 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-F725E90B2A-L002671](../../tests/test_web_agent.py#L2671) | 2671 | `"            self.options = kwargs"` | — |
| [SRC-F725E90B2A-L002672](../../tests/test_web_agent.py#L2672) | 2672 | `""` | — |
| [SRC-F725E90B2A-L002673](../../tests/test_web_agent.py#L2673) | 2673 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L002674](../../tests/test_web_agent.py#L2674) | 2674 | `"            return self"` | — |
| [SRC-F725E90B2A-L002675](../../tests/test_web_agent.py#L2675) | 2675 | `""` | — |
| [SRC-F725E90B2A-L002676](../../tests/test_web_agent.py#L2676) | 2676 | `"        def __exit__(self, *_args):"` | — |
| [SRC-F725E90B2A-L002677](../../tests/test_web_agent.py#L2677) | 2677 | `"            return False"` | — |
| [SRC-F725E90B2A-L002678](../../tests/test_web_agent.py#L2678) | 2678 | `""` | — |
| [SRC-F725E90B2A-L002679](../../tests/test_web_agent.py#L2679) | 2679 | `"        stream = fake_stream"` | — |
| [SRC-F725E90B2A-L002680](../../tests/test_web_agent.py#L2680) | 2680 | `""` | — |
| [SRC-F725E90B2A-L002681](../../tests/test_web_agent.py#L2681) | 2681 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-F725E90B2A-L002682](../../tests/test_web_agent.py#L2682) | 2682 | `""` | — |
| [SRC-F725E90B2A-L002683](../../tests/test_web_agent.py#L2683) | 2683 | `"    assert web_agent.WebAgent()._fetch_page(\"https://first.example/article\") == (\"\", \"\")"` | — |
| [SRC-F725E90B2A-L002684](../../tests/test_web_agent.py#L2684) | 2684 | `"    assert resolved_hosts == [\"first.example\"]"` | — |
| [SRC-F725E90B2A-L002685](../../tests/test_web_agent.py#L2685) | 2685 | `"    assert len(requests) == 1"` | — |
| [SRC-F725E90B2A-L002686](../../tests/test_web_agent.py#L2686) | 2686 | `"    assert requests[0][1] == \"https://93.184.216.34/article\""` | — |
| [SRC-F725E90B2A-L002687](../../tests/test_web_agent.py#L2687) | 2687 | `"    assert requests[0][2][\"headers\"][\"Host\"] == \"first.example\""` | — |
| [SRC-F725E90B2A-L002688](../../tests/test_web_agent.py#L2688) | 2688 | `"    assert requests[0][2][\"extensions\"][\"sni_hostname\"] == \"first.example\""` | — |
| [SRC-F725E90B2A-L002689](../../tests/test_web_agent.py#L2689) | 2689 | `""` | — |
| [SRC-F725E90B2A-L002690](../../tests/test_web_agent.py#L2690) | 2690 | `""` | — |
| [SRC-F725E90B2A-L002691](../../tests/test_web_agent.py#L2691) | 2691 | `"def test_fetch_page_revalidates_dns_for_each_redirect_destination(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002692](../../tests/test_web_agent.py#L2692) | 2692 | `"    from contextlib import contextmanager"` | — |
| [SRC-F725E90B2A-L002693](../../tests/test_web_agent.py#L2693) | 2693 | `""` | — |
| [SRC-F725E90B2A-L002694](../../tests/test_web_agent.py#L2694) | 2694 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002695](../../tests/test_web_agent.py#L2695) | 2695 | `""` | — |
| [SRC-F725E90B2A-L002696](../../tests/test_web_agent.py#L2696) | 2696 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L002697](../../tests/test_web_agent.py#L2697) | 2697 | `""` | — |
| [SRC-F725E90B2A-L002698](../../tests/test_web_agent.py#L2698) | 2698 | `"    resolved_hosts = []"` | — |
| [SRC-F725E90B2A-L002699](../../tests/test_web_agent.py#L2699) | 2699 | `"    requests = []"` | — |
| [SRC-F725E90B2A-L002700](../../tests/test_web_agent.py#L2700) | 2700 | `""` | — |
| [SRC-F725E90B2A-L002701](../../tests/test_web_agent.py#L2701) | 2701 | `"    def resolve_public_ip(host):"` | — |
| [SRC-F725E90B2A-L002702](../../tests/test_web_agent.py#L2702) | 2702 | `"        resolved_hosts.append(host)"` | — |
| [SRC-F725E90B2A-L002703](../../tests/test_web_agent.py#L2703) | 2703 | `"        if host == \"first.example\":"` | — |
| [SRC-F725E90B2A-L002704](../../tests/test_web_agent.py#L2704) | 2704 | `"            return [\"93.184.216.34\"]"` | — |
| [SRC-F725E90B2A-L002705](../../tests/test_web_agent.py#L2705) | 2705 | `"        # Model a redirect destination that resolves to no verified public IP."` | — |
| [SRC-F725E90B2A-L002706](../../tests/test_web_agent.py#L2706) | 2706 | `"        return None"` | — |
| [SRC-F725E90B2A-L002707](../../tests/test_web_agent.py#L2707) | 2707 | `""` | — |
| [SRC-F725E90B2A-L002708](../../tests/test_web_agent.py#L2708) | 2708 | `"    monkeypatch.setattr(web_agent, \"_public_ip_literals\", resolve_public_ip)"` | — |
| [SRC-F725E90B2A-L002709](../../tests/test_web_agent.py#L2709) | 2709 | `""` | — |
| [SRC-F725E90B2A-L002710](../../tests/test_web_agent.py#L2710) | 2710 | `"    class RedirectResponse:"` | — |
| [SRC-F725E90B2A-L002711](../../tests/test_web_agent.py#L2711) | 2711 | `"        status_code = 302"` | — |
| [SRC-F725E90B2A-L002712](../../tests/test_web_agent.py#L2712) | 2712 | `""` | — |
| [SRC-F725E90B2A-L002713](../../tests/test_web_agent.py#L2713) | 2713 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L002714](../../tests/test_web_agent.py#L2714) | 2714 | `"            self.headers = {\"location\": \"https://second.example/internal\"}"` | — |
| [SRC-F725E90B2A-L002715](../../tests/test_web_agent.py#L2715) | 2715 | `""` | — |
| [SRC-F725E90B2A-L002716](../../tests/test_web_agent.py#L2716) | 2716 | `"    @contextmanager"` | — |
| [SRC-F725E90B2A-L002717](../../tests/test_web_agent.py#L2717) | 2717 | `"    def fake_stream(self, method, url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002718](../../tests/test_web_agent.py#L2718) | 2718 | `"        requests.append((method, str(url), kwargs))"` | — |
| [SRC-F725E90B2A-L002719](../../tests/test_web_agent.py#L2719) | 2719 | `"        yield RedirectResponse()"` | — |
| [SRC-F725E90B2A-L002720](../../tests/test_web_agent.py#L2720) | 2720 | `""` | — |
| [SRC-F725E90B2A-L002721](../../tests/test_web_agent.py#L2721) | 2721 | `"    class FakeClient:"` | — |
| [SRC-F725E90B2A-L002722](../../tests/test_web_agent.py#L2722) | 2722 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-F725E90B2A-L002723](../../tests/test_web_agent.py#L2723) | 2723 | `"            self.options = kwargs"` | — |
| [SRC-F725E90B2A-L002724](../../tests/test_web_agent.py#L2724) | 2724 | `""` | — |
| [SRC-F725E90B2A-L002725](../../tests/test_web_agent.py#L2725) | 2725 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L002726](../../tests/test_web_agent.py#L2726) | 2726 | `"            return self"` | — |
| [SRC-F725E90B2A-L002727](../../tests/test_web_agent.py#L2727) | 2727 | `""` | — |
| [SRC-F725E90B2A-L002728](../../tests/test_web_agent.py#L2728) | 2728 | `"        def __exit__(self, *_args):"` | — |
| [SRC-F725E90B2A-L002729](../../tests/test_web_agent.py#L2729) | 2729 | `"            return False"` | — |
| [SRC-F725E90B2A-L002730](../../tests/test_web_agent.py#L2730) | 2730 | `""` | — |
| [SRC-F725E90B2A-L002731](../../tests/test_web_agent.py#L2731) | 2731 | `"        stream = fake_stream"` | — |
| [SRC-F725E90B2A-L002732](../../tests/test_web_agent.py#L2732) | 2732 | `""` | — |
| [SRC-F725E90B2A-L002733](../../tests/test_web_agent.py#L2733) | 2733 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-F725E90B2A-L002734](../../tests/test_web_agent.py#L2734) | 2734 | `""` | — |
| [SRC-F725E90B2A-L002735](../../tests/test_web_agent.py#L2735) | 2735 | `"    assert web_agent.WebAgent()._fetch_page(\"https://first.example/article\") == (\"\", \"\")"` | — |
| [SRC-F725E90B2A-L002736](../../tests/test_web_agent.py#L2736) | 2736 | `"    assert resolved_hosts == [\"first.example\", \"second.example\"]"` | — |
| [SRC-F725E90B2A-L002737](../../tests/test_web_agent.py#L2737) | 2737 | `"    # The second host is validated before any connection attempt to it."` | — |
| [SRC-F725E90B2A-L002738](../../tests/test_web_agent.py#L2738) | 2738 | `"    assert len(requests) == 1"` | — |
| [SRC-F725E90B2A-L002739](../../tests/test_web_agent.py#L2739) | 2739 | `""` | — |
| [SRC-F725E90B2A-L002740](../../tests/test_web_agent.py#L2740) | 2740 | `""` | — |
| [SRC-F725E90B2A-L002741](../../tests/test_web_agent.py#L2741) | 2741 | `""` | — |
| [SRC-F725E90B2A-L002742](../../tests/test_web_agent.py#L2742) | 2742 | `"def test_history_search_query_uses_shared_context_resolver():"` | — |
| [SRC-F725E90B2A-L002743](../../tests/test_web_agent.py#L2743) | 2743 | `"    history = ["` | — |
| [SRC-F725E90B2A-L002744](../../tests/test_web_agent.py#L2744) | 2744 | `"        {\"role\": \"user\", \"content\": \"سعر آيفون 16 في مصر\"},"` | — |
| [SRC-F725E90B2A-L002745](../../tests/test_web_agent.py#L2745) | 2745 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن السعر.\"},"` | — |
| [SRC-F725E90B2A-L002746](../../tests/test_web_agent.py#L2746) | 2746 | `"    ]"` | — |
| [SRC-F725E90B2A-L002747](../../tests/test_web_agent.py#L2747) | 2747 | `"    query = WebAgent._history_search_query(\"هل فيه ضمان؟\", history)"` | — |
| [SRC-F725E90B2A-L002748](../../tests/test_web_agent.py#L2748) | 2748 | `"    assert \"آيفون 16\" in query"` | — |
| [SRC-F725E90B2A-L002749](../../tests/test_web_agent.py#L2749) | 2749 | `"    assert \"ضمان\" in query"` | — |
| [SRC-F725E90B2A-L002750](../../tests/test_web_agent.py#L2750) | 2750 | `""` | — |
| [SRC-F725E90B2A-L002751](../../tests/test_web_agent.py#L2751) | 2751 | `""` | — |
| [SRC-F725E90B2A-L002752](../../tests/test_web_agent.py#L2752) | 2752 | `"def test_history_search_query_does_not_reuse_stale_topic_after_acknowledgment():"` | — |
| [SRC-F725E90B2A-L002753](../../tests/test_web_agent.py#L2753) | 2753 | `"    history = ["` | — |
| [SRC-F725E90B2A-L002754](../../tests/test_web_agent.py#L2754) | 2754 | `"        {\"role\": \"user\", \"content\": \"سعر آيفون 16 في مصر\"},"` | — |
| [SRC-F725E90B2A-L002755](../../tests/test_web_agent.py#L2755) | 2755 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن السعر.\"},"` | — |
| [SRC-F725E90B2A-L002756](../../tests/test_web_agent.py#L2756) | 2756 | `"        {\"role\": \"user\", \"content\": \"شكرا\"},"` | — |
| [SRC-F725E90B2A-L002757](../../tests/test_web_agent.py#L2757) | 2757 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-F725E90B2A-L002758](../../tests/test_web_agent.py#L2758) | 2758 | `"    ]"` | — |
| [SRC-F725E90B2A-L002759](../../tests/test_web_agent.py#L2759) | 2759 | `"    assert WebAgent._history_search_query(\"فين؟\", history) == \"فين؟\""` | — |
| [SRC-F725E90B2A-L002760](../../tests/test_web_agent.py#L2760) | 2760 | `""` | — |
| [SRC-F725E90B2A-L002761](../../tests/test_web_agent.py#L2761) | 2761 | `""` | — |
| [SRC-F725E90B2A-L002762](../../tests/test_web_agent.py#L2762) | 2762 | `"def test_frontend_exposes_structured_page_fetch_statuses():"` | — |
| [SRC-F725E90B2A-L002763](../../tests/test_web_agent.py#L2763) | 2763 | `"    html_path = Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\""` | — |
| [SRC-F725E90B2A-L002764](../../tests/test_web_agent.py#L2764) | 2764 | `"    html = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002765](../../tests/test_web_agent.py#L2765) | 2765 | `"    assert \"page_fetch_status\" in html"` | — |
| [SRC-F725E90B2A-L002766](../../tests/test_web_agent.py#L2766) | 2766 | `"    assert \"partial_extraction\" in html"` | — |
| [SRC-F725E90B2A-L002767](../../tests/test_web_agent.py#L2767) | 2767 | `"    assert \"لم يُستخرج نص؛ قد تكون الصفحة ديناميكية أو محجوبة\" in html"` | — |
| [SRC-F725E90B2A-L002768](../../tests/test_web_agent.py#L2768) | 2768 | `"    assert \"تشخيص الموصلات في هذا الطلب\" in html"` | — |
| [SRC-F725E90B2A-L002769](../../tests/test_web_agent.py#L2769) | 2769 | `"    assert \"حالة إكمال البحث\" in html"` | — |
| [SRC-F725E90B2A-L002770](../../tests/test_web_agent.py#L2770) | 2770 | `"    assert \"تفاصيل مراحل إكمال البحث والعدادات\" in html"` | — |
| [SRC-F725E90B2A-L002771](../../tests/test_web_agent.py#L2771) | 2771 | `"    assert \"pages_read_with_text_count\" in html"` | — |
| [SRC-F725E90B2A-L002772](../../tests/test_web_agent.py#L2772) | 2772 | `"    assert \"التحقق الدلالي من أن كل ادعاء مسنود فعلًا بالمصدر\" in html"` | — |
| [SRC-F725E90B2A-L002773](../../tests/test_web_agent.py#L2773) | 2773 | `""` | — |
| [SRC-F725E90B2A-L002774](../../tests/test_web_agent.py#L2774) | 2774 | `""` | — |
| [SRC-F725E90B2A-L002775](../../tests/test_web_agent.py#L2775) | 2775 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L002776](../../tests/test_web_agent.py#L2776) | 2776 | `"    \"method_name\","` | — |
| [SRC-F725E90B2A-L002777](../../tests/test_web_agent.py#L2777) | 2777 | `"    [\"_search_duckduckgo_html\", \"_search_bing_rss\", \"_search_news\"],"` | — |
| [SRC-F725E90B2A-L002778](../../tests/test_web_agent.py#L2778) | 2778 | `")"` | — |
| [SRC-F725E90B2A-L002779](../../tests/test_web_agent.py#L2779) | 2779 | `"def test_search_providers_do_not_follow_redirects_automatically("` | — |
| [SRC-F725E90B2A-L002780](../../tests/test_web_agent.py#L2780) | 2780 | `"    monkeypatch, method_name"` | — |
| [SRC-F725E90B2A-L002781](../../tests/test_web_agent.py#L2781) | 2781 | `"):"` | — |
| [SRC-F725E90B2A-L002782](../../tests/test_web_agent.py#L2782) | 2782 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002783](../../tests/test_web_agent.py#L2783) | 2783 | `""` | — |
| [SRC-F725E90B2A-L002784](../../tests/test_web_agent.py#L2784) | 2784 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002785](../../tests/test_web_agent.py#L2785) | 2785 | `"    observed = []"` | — |
| [SRC-F725E90B2A-L002786](../../tests/test_web_agent.py#L2786) | 2786 | `""` | — |
| [SRC-F725E90B2A-L002787](../../tests/test_web_agent.py#L2787) | 2787 | `"    class RedirectResponse:"` | — |
| [SRC-F725E90B2A-L002788](../../tests/test_web_agent.py#L2788) | 2788 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L002789](../../tests/test_web_agent.py#L2789) | 2789 | `"            self.status_code = 302"` | — |
| [SRC-F725E90B2A-L002790](../../tests/test_web_agent.py#L2790) | 2790 | `"            self.headers = {\"location\": \"http://127.0.0.1:8765/private\"}"` | — |
| [SRC-F725E90B2A-L002791](../../tests/test_web_agent.py#L2791) | 2791 | `"            self.text = \"redirect\""` | — |
| [SRC-F725E90B2A-L002792](../../tests/test_web_agent.py#L2792) | 2792 | `"            self.content = b\"redirect\""` | — |
| [SRC-F725E90B2A-L002793](../../tests/test_web_agent.py#L2793) | 2793 | `""` | — |
| [SRC-F725E90B2A-L002794](../../tests/test_web_agent.py#L2794) | 2794 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002795](../../tests/test_web_agent.py#L2795) | 2795 | `"        observed.append((url, kwargs.get(\"follow_redirects\")))"` | — |
| [SRC-F725E90B2A-L002796](../../tests/test_web_agent.py#L2796) | 2796 | `"        return RedirectResponse()"` | — |
| [SRC-F725E90B2A-L002797](../../tests/test_web_agent.py#L2797) | 2797 | `""` | — |
| [SRC-F725E90B2A-L002798](../../tests/test_web_agent.py#L2798) | 2798 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L002799](../../tests/test_web_agent.py#L2799) | 2799 | `"    method = getattr(agent, method_name)"` | — |
| [SRC-F725E90B2A-L002800](../../tests/test_web_agent.py#L2800) | 2800 | `"    with pytest.raises(RuntimeError, match=\"HTTP 302\"):"` | — |
| [SRC-F725E90B2A-L002801](../../tests/test_web_agent.py#L2801) | 2801 | `"        method(\"redirect regression test\")"` | — |
| [SRC-F725E90B2A-L002802](../../tests/test_web_agent.py#L2802) | 2802 | `""` | — |
| [SRC-F725E90B2A-L002803](../../tests/test_web_agent.py#L2803) | 2803 | `"    assert len(observed) == 1"` | — |
| [SRC-F725E90B2A-L002804](../../tests/test_web_agent.py#L2804) | 2804 | `"    assert observed[0][1] is False"` | — |
| [SRC-F725E90B2A-L002805](../../tests/test_web_agent.py#L2805) | 2805 | `""` | — |
| [SRC-F725E90B2A-L002806](../../tests/test_web_agent.py#L2806) | 2806 | `""` | — |
| [SRC-F725E90B2A-L002807](../../tests/test_web_agent.py#L2807) | 2807 | `""` | — |
| [SRC-F725E90B2A-L002808](../../tests/test_web_agent.py#L2808) | 2808 | `"@pytest.mark.parametrize(\"mode\", [\"deep\", \"latest\", \"social\"])"` | — |
| [SRC-F725E90B2A-L002809](../../tests/test_web_agent.py#L2809) | 2809 | `"def test_explicit_modes_survive_deterministic_planning(monkeypatch, mode):"` | — |
| [SRC-F725E90B2A-L002810](../../tests/test_web_agent.py#L2810) | 2810 | `"    \"\"\"A missing planner model must not erase a mode explicitly selected by the user.\"\"\""` | — |
| [SRC-F725E90B2A-L002811](../../tests/test_web_agent.py#L2811) | 2811 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002812](../../tests/test_web_agent.py#L2812) | 2812 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L002813](../../tests/test_web_agent.py#L2813) | 2813 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002814](../../tests/test_web_agent.py#L2814) | 2814 | `""` | — |
| [SRC-F725E90B2A-L002815](../../tests/test_web_agent.py#L2815) | 2815 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L002816](../../tests/test_web_agent.py#L2816) | 2816 | `"        seen[\"plan\"] = dict(research_plan)"` | — |
| [SRC-F725E90B2A-L002817](../../tests/test_web_agent.py#L2817) | 2817 | `"        sources = [sample_source(0), sample_source(1)]"` | — |
| [SRC-F725E90B2A-L002818](../../tests/test_web_agent.py#L2818) | 2818 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L002819](../../tests/test_web_agent.py#L2819) | 2819 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002820](../../tests/test_web_agent.py#L2820) | 2820 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002821](../../tests/test_web_agent.py#L2821) | 2821 | `"            \"query_results\": ["` | — |
| [SRC-F725E90B2A-L002822](../../tests/test_web_agent.py#L2822) | 2822 | `"                {\"query\": query, \"results\": 1}"` | — |
| [SRC-F725E90B2A-L002823](../../tests/test_web_agent.py#L2823) | 2823 | `"                for query in research_plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L002824](../../tests/test_web_agent.py#L2824) | 2824 | `"            ],"` | — |
| [SRC-F725E90B2A-L002825](../../tests/test_web_agent.py#L2825) | 2825 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-F725E90B2A-L002826](../../tests/test_web_agent.py#L2826) | 2826 | `"            \"pages_fetched\": len(sources),"` | — |
| [SRC-F725E90B2A-L002827](../../tests/test_web_agent.py#L2827) | 2827 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L002828](../../tests/test_web_agent.py#L2828) | 2828 | `"            \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-F725E90B2A-L002829](../../tests/test_web_agent.py#L2829) | 2829 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002830](../../tests/test_web_agent.py#L2830) | 2830 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L002831](../../tests/test_web_agent.py#L2831) | 2831 | `"            \"planning_method\": \"deterministic_fallback\","` | — |
| [SRC-F725E90B2A-L002832](../../tests/test_web_agent.py#L2832) | 2832 | `"        }"` | — |
| [SRC-F725E90B2A-L002833](../../tests/test_web_agent.py#L2833) | 2833 | `""` | — |
| [SRC-F725E90B2A-L002834](../../tests/test_web_agent.py#L2834) | 2834 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L002835](../../tests/test_web_agent.py#L2835) | 2835 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L002836](../../tests/test_web_agent.py#L2836) | 2836 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L002837](../../tests/test_web_agent.py#L2837) | 2837 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002838](../../tests/test_web_agent.py#L2838) | 2838 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002839](../../tests/test_web_agent.py#L2839) | 2839 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L002840](../../tests/test_web_agent.py#L2840) | 2840 | `"        lambda question, history, sources, search_warning, research_plan=None,"` | — |
| [SRC-F725E90B2A-L002841](../../tests/test_web_agent.py#L2841) | 2841 | `"               search_report=None: \"توجد نتائج أولية للمراجعة [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L002842](../../tests/test_web_agent.py#L2842) | 2842 | `"    )"` | — |
| [SRC-F725E90B2A-L002843](../../tests/test_web_agent.py#L2843) | 2843 | `""` | — |
| [SRC-F725E90B2A-L002844](../../tests/test_web_agent.py#L2844) | 2844 | `"    question = ("` | — |
| [SRC-F725E90B2A-L002845](../../tests/test_web_agent.py#L2845) | 2845 | `"        \"ابحث عن شقة في التجمع الخامس بسعر 5000000 جنيه\""` | — |
| [SRC-F725E90B2A-L002846](../../tests/test_web_agent.py#L2846) | 2846 | `"        if mode == \"deep\" else \"الطاقة المتجددة في مصر\""` | — |
| [SRC-F725E90B2A-L002847](../../tests/test_web_agent.py#L2847) | 2847 | `"    )"` | — |
| [SRC-F725E90B2A-L002848](../../tests/test_web_agent.py#L2848) | 2848 | `"    result = agent.answer(question, mode=mode)"` | — |
| [SRC-F725E90B2A-L002849](../../tests/test_web_agent.py#L2849) | 2849 | `"    plan = seen[\"plan\"]"` | — |
| [SRC-F725E90B2A-L002850](../../tests/test_web_agent.py#L2850) | 2850 | `""` | — |
| [SRC-F725E90B2A-L002851](../../tests/test_web_agent.py#L2851) | 2851 | `"    assert plan[\"mode\"] == mode"` | — |
| [SRC-F725E90B2A-L002852](../../tests/test_web_agent.py#L2852) | 2852 | `"    assert result[\"research_plan\"][\"mode\"] == mode"` | — |
| [SRC-F725E90B2A-L002853](../../tests/test_web_agent.py#L2853) | 2853 | `"    if mode == \"deep\":"` | — |
| [SRC-F725E90B2A-L002854](../../tests/test_web_agent.py#L2854) | 2854 | `"        assert plan[\"depth\"] == \"deep\""` | — |
| [SRC-F725E90B2A-L002855](../../tests/test_web_agent.py#L2855) | 2855 | `"        assert len(plan[\"queries\"]) >= 3"` | — |
| [SRC-F725E90B2A-L002856](../../tests/test_web_agent.py#L2856) | 2856 | `"        assert any(\"إعلانات عقارية\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002857](../../tests/test_web_agent.py#L2857) | 2857 | `"        assert any(\"متوسط أسعار السوق للمتر\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002858](../../tests/test_web_agent.py#L2858) | 2858 | `"    elif mode == \"latest\":"` | — |
| [SRC-F725E90B2A-L002859](../../tests/test_web_agent.py#L2859) | 2859 | `"        assert plan[\"freshness\"] == \"current\""` | — |
| [SRC-F725E90B2A-L002860](../../tests/test_web_agent.py#L2860) | 2860 | `"        assert any("` | — |
| [SRC-F725E90B2A-L002861](../../tests/test_web_agent.py#L2861) | 2861 | `"            \"latest\" in query.lower() or \"recent\" in query.lower()"` | — |
| [SRC-F725E90B2A-L002862](../../tests/test_web_agent.py#L2862) | 2862 | `"            for query in plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L002863](../../tests/test_web_agent.py#L2863) | 2863 | `"        )"` | — |
| [SRC-F725E90B2A-L002864](../../tests/test_web_agent.py#L2864) | 2864 | `"    else:"` | — |
| [SRC-F725E90B2A-L002865](../../tests/test_web_agent.py#L2865) | 2865 | `"        assert plan[\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L002866](../../tests/test_web_agent.py#L2866) | 2866 | `"        assert any(query.startswith(\"site:\") for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002867](../../tests/test_web_agent.py#L2867) | 2867 | `""` | — |
| [SRC-F725E90B2A-L002868](../../tests/test_web_agent.py#L2868) | 2868 | `""` | — |
| [SRC-F725E90B2A-L002869](../../tests/test_web_agent.py#L2869) | 2869 | `"def test_latest_mode_preserves_official_website_navigation_intent(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002870](../../tests/test_web_agent.py#L2870) | 2870 | `"    \"\"\"Latest mode must not replace an official-site lookup with generic news queries.\"\"\""` | — |
| [SRC-F725E90B2A-L002871](../../tests/test_web_agent.py#L2871) | 2871 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002872](../../tests/test_web_agent.py#L2872) | 2872 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L002873](../../tests/test_web_agent.py#L2873) | 2873 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002874](../../tests/test_web_agent.py#L2874) | 2874 | `""` | — |
| [SRC-F725E90B2A-L002875](../../tests/test_web_agent.py#L2875) | 2875 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L002876](../../tests/test_web_agent.py#L2876) | 2876 | `"        seen[\"plan\"] = dict(research_plan)"` | — |
| [SRC-F725E90B2A-L002877](../../tests/test_web_agent.py#L2877) | 2877 | `"        sources = [sample_source(0), sample_source(1)]"` | — |
| [SRC-F725E90B2A-L002878](../../tests/test_web_agent.py#L2878) | 2878 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L002879](../../tests/test_web_agent.py#L2879) | 2879 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002880](../../tests/test_web_agent.py#L2880) | 2880 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002881](../../tests/test_web_agent.py#L2881) | 2881 | `"            \"query_results\": ["` | — |
| [SRC-F725E90B2A-L002882](../../tests/test_web_agent.py#L2882) | 2882 | `"                {\"query\": query, \"results\": 1}"` | — |
| [SRC-F725E90B2A-L002883](../../tests/test_web_agent.py#L2883) | 2883 | `"                for query in research_plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L002884](../../tests/test_web_agent.py#L2884) | 2884 | `"            ],"` | — |
| [SRC-F725E90B2A-L002885](../../tests/test_web_agent.py#L2885) | 2885 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-F725E90B2A-L002886](../../tests/test_web_agent.py#L2886) | 2886 | `"            \"pages_fetched\": len(sources),"` | — |
| [SRC-F725E90B2A-L002887](../../tests/test_web_agent.py#L2887) | 2887 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L002888](../../tests/test_web_agent.py#L2888) | 2888 | `"            \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-F725E90B2A-L002889](../../tests/test_web_agent.py#L2889) | 2889 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002890](../../tests/test_web_agent.py#L2890) | 2890 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L002891](../../tests/test_web_agent.py#L2891) | 2891 | `"            \"planning_method\": \"deterministic_fallback\","` | — |
| [SRC-F725E90B2A-L002892](../../tests/test_web_agent.py#L2892) | 2892 | `"        }"` | — |
| [SRC-F725E90B2A-L002893](../../tests/test_web_agent.py#L2893) | 2893 | `""` | — |
| [SRC-F725E90B2A-L002894](../../tests/test_web_agent.py#L2894) | 2894 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L002895](../../tests/test_web_agent.py#L2895) | 2895 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L002896](../../tests/test_web_agent.py#L2896) | 2896 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L002897](../../tests/test_web_agent.py#L2897) | 2897 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002898](../../tests/test_web_agent.py#L2898) | 2898 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002899](../../tests/test_web_agent.py#L2899) | 2899 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L002900](../../tests/test_web_agent.py#L2900) | 2900 | `"        lambda question, history, sources, search_warning, research_plan=None,"` | — |
| [SRC-F725E90B2A-L002901](../../tests/test_web_agent.py#L2901) | 2901 | `"               search_report=None: \"وجدت مرشحًا للموقع الرسمي [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L002902](../../tests/test_web_agent.py#L2902) | 2902 | `"    )"` | — |
| [SRC-F725E90B2A-L002903](../../tests/test_web_agent.py#L2903) | 2903 | `""` | — |
| [SRC-F725E90B2A-L002904](../../tests/test_web_agent.py#L2904) | 2904 | `"    question = ("` | — |
| [SRC-F725E90B2A-L002905](../../tests/test_web_agent.py#L2905) | 2905 | `"        \"ابحث عن الموقع الرسمي لوزارة الاتصالات وتكنولوجيا المعلومات المصرية، \""` | — |
| [SRC-F725E90B2A-L002906](../../tests/test_web_agent.py#L2906) | 2906 | `"        \"واعرض رابط المصدر وتاريخ الصفحة إن توفر\""` | — |
| [SRC-F725E90B2A-L002907](../../tests/test_web_agent.py#L2907) | 2907 | `"    )"` | — |
| [SRC-F725E90B2A-L002908](../../tests/test_web_agent.py#L2908) | 2908 | `"    result = agent.answer(question, mode=\"latest\")"` | — |
| [SRC-F725E90B2A-L002909](../../tests/test_web_agent.py#L2909) | 2909 | `"    plan = seen[\"plan\"]"` | — |
| [SRC-F725E90B2A-L002910](../../tests/test_web_agent.py#L2910) | 2910 | `""` | — |
| [SRC-F725E90B2A-L002911](../../tests/test_web_agent.py#L2911) | 2911 | `"    assert plan[\"mode\"] == \"latest\""` | — |
| [SRC-F725E90B2A-L002912](../../tests/test_web_agent.py#L2912) | 2912 | `"    assert result[\"research_plan\"][\"mode\"] == \"latest\""` | — |
| [SRC-F725E90B2A-L002913](../../tests/test_web_agent.py#L2913) | 2913 | `"    assert any("` | — |
| [SRC-F725E90B2A-L002914](../../tests/test_web_agent.py#L2914) | 2914 | `"        \"الموقع الرسمي\" in query or \"official website\" in query.lower()"` | — |
| [SRC-F725E90B2A-L002915](../../tests/test_web_agent.py#L2915) | 2915 | `"        for query in plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L002916](../../tests/test_web_agent.py#L2916) | 2916 | `"    )"` | — |
| [SRC-F725E90B2A-L002917](../../tests/test_web_agent.py#L2917) | 2917 | `"    assert not any(\"latest news updates\" in query.lower() for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002918](../../tests/test_web_agent.py#L2918) | 2918 | `"    assert not any(\"recent official announcement\" in query.lower() for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002919](../../tests/test_web_agent.py#L2919) | 2919 | `""` | — |
| [SRC-F725E90B2A-L002920](../../tests/test_web_agent.py#L2920) | 2920 | `""` | — |
| [SRC-F725E90B2A-L002921](../../tests/test_web_agent.py#L2921) | 2921 | `"def test_web_answer_integrity_is_attached_without_live_network(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002922](../../tests/test_web_agent.py#L2922) | 2922 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002923](../../tests/test_web_agent.py#L2923) | 2923 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002924](../../tests/test_web_agent.py#L2924) | 2924 | `"        agent, \"_question_coverage_targets\", lambda question: [\"السعر\", \"المساحة\"]"` | — |
| [SRC-F725E90B2A-L002925](../../tests/test_web_agent.py#L2925) | 2925 | `"    )"` | — |
| [SRC-F725E90B2A-L002926](../../tests/test_web_agent.py#L2926) | 2926 | `"    monkeypatch.setattr(agent, \"_answer_with_budget\", lambda question, history, mode: {"` | — |
| [SRC-F725E90B2A-L002927](../../tests/test_web_agent.py#L2927) | 2927 | `"        \"kind\": \"web_research\","` | — |
| [SRC-F725E90B2A-L002928](../../tests/test_web_agent.py#L2928) | 2928 | `"        \"answer\": \"السعر 500 جنيه [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L002929](../../tests/test_web_agent.py#L2929) | 2929 | `"        \"sources\": [{"` | — |
| [SRC-F725E90B2A-L002930](../../tests/test_web_agent.py#L2930) | 2930 | `"            \"title\": \"تفاصيل العرض\","` | — |
| [SRC-F725E90B2A-L002931](../../tests/test_web_agent.py#L2931) | 2931 | `"            \"url\": \"https://example.com/offer\","` | — |
| [SRC-F725E90B2A-L002932](../../tests/test_web_agent.py#L2932) | 2932 | `"            \"snippet\": \"السعر 300 جنيه\","` | — |
| [SRC-F725E90B2A-L002933](../../tests/test_web_agent.py#L2933) | 2933 | `"            \"page_fetched\": False,"` | — |
| [SRC-F725E90B2A-L002934](../../tests/test_web_agent.py#L2934) | 2934 | `"        }],"` | — |
| [SRC-F725E90B2A-L002935](../../tests/test_web_agent.py#L2935) | 2935 | `"        \"research_quality\": \"partial\","` | — |
| [SRC-F725E90B2A-L002936](../../tests/test_web_agent.py#L2936) | 2936 | `"        \"search_report\": {},"` | — |
| [SRC-F725E90B2A-L002937](../../tests/test_web_agent.py#L2937) | 2937 | `"        \"answer_coverage\": {},"` | — |
| [SRC-F725E90B2A-L002938](../../tests/test_web_agent.py#L2938) | 2938 | `"        \"used_language_model\": True,"` | — |
| [SRC-F725E90B2A-L002939](../../tests/test_web_agent.py#L2939) | 2939 | `"        \"used_web_search\": True,"` | — |
| [SRC-F725E90B2A-L002940](../../tests/test_web_agent.py#L2940) | 2940 | `"        \"warnings\": [],"` | — |
| [SRC-F725E90B2A-L002941](../../tests/test_web_agent.py#L2941) | 2941 | `"    })"` | — |
| [SRC-F725E90B2A-L002942](../../tests/test_web_agent.py#L2942) | 2942 | `""` | — |
| [SRC-F725E90B2A-L002943](../../tests/test_web_agent.py#L2943) | 2943 | `"    result = agent.answer(\"قارن السعر والمساحة\", mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L002944](../../tests/test_web_agent.py#L2944) | 2944 | `""` | — |
| [SRC-F725E90B2A-L002945](../../tests/test_web_agent.py#L2945) | 2945 | `"    assert result[\"answer_integrity\"][\"semantic_verification\"] is False"` | — |
| [SRC-F725E90B2A-L002946](../../tests/test_web_agent.py#L2946) | 2946 | `"    assert result[\"answer_integrity\"][\"independent_fact_check\"] is False"` | — |
| [SRC-F725E90B2A-L002947](../../tests/test_web_agent.py#L2947) | 2947 | `"    assert result[\"answer_integrity\"][\"potentially_unsupported_numeric_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002948](../../tests/test_web_agent.py#L2948) | 2948 | `"    assert result[\"answer_integrity\"][\"potentially_unsupported_numeric_by_citation_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002949](../../tests/test_web_agent.py#L2949) | 2949 | `"    assert result[\"answer_integrity\"][\"potentially_missing_target_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002950](../../tests/test_web_agent.py#L2950) | 2950 | `"    assert result[\"task_fulfillment_status\"] == \"possible_gap_detected\""` | — |
| [SRC-F725E90B2A-L002951](../../tests/test_web_agent.py#L2951) | 2951 | `"    assert result[\"answer_coverage\"][\"lexical_screen_method\"] == ("` | — |
| [SRC-F725E90B2A-L002952](../../tests/test_web_agent.py#L2952) | 2952 | `"        \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-F725E90B2A-L002953](../../tests/test_web_agent.py#L2953) | 2953 | `"    )"` | — |
| [SRC-F725E90B2A-L002954](../../tests/test_web_agent.py#L2954) | 2954 | `""` | — |
| [SRC-F725E90B2A-L002955](../../tests/test_web_agent.py#L2955) | 2955 | `""` | — |
| [SRC-F725E90B2A-L002956](../../tests/test_web_agent.py#L2956) | 2956 | `"def test_frontend_labels_answer_integrity_screen_as_non_semantic():"` | — |
| [SRC-F725E90B2A-L002957](../../tests/test_web_agent.py#L2957) | 2957 | `"    html = ("` | — |
| [SRC-F725E90B2A-L002958](../../tests/test_web_agent.py#L2958) | 2958 | `"        Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\""` | — |
| [SRC-F725E90B2A-L002959](../../tests/test_web_agent.py#L2959) | 2959 | `"    ).read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002960](../../tests/test_web_agent.py#L2960) | 2960 | `"    assert \"فحص لفظي أولي:\" in html"` | — |
| [SRC-F725E90B2A-L002961](../../tests/test_web_agent.py#L2961) | 2961 | `"    assert \"لا يثبت هذا الفحص صحة الوقائع أو دلالة الاستشهاد\" in html"` | — |
| [SRC-F725E90B2A-L002962](../../tests/test_web_agent.py#L2962) | 2962 | `"    assert \"potentially_unsupported_numeric_by_citation_count\" in html"` | — |
| [SRC-F725E90B2A-L002963](../../tests/test_web_agent.py#L2963) | 2963 | `"    assert \"potential_value_discrepancy_count\" in html"` | — |
| [SRC-F725E90B2A-L002964](../../tests/test_web_agent.py#L2964) | 2964 | `""` | — |
| [SRC-F725E90B2A-L002965](../../tests/test_web_agent.py#L2965) | 2965 | `""` | — |
| [SRC-F725E90B2A-L002966](../../tests/test_web_agent.py#L2966) | 2966 | `"def test_search_web_keeps_arabic_topic_matches_in_english_indexed_results(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002967](../../tests/test_web_agent.py#L2967) | 2967 | `"    cases = ["` | — |
| [SRC-F725E90B2A-L002968](../../tests/test_web_agent.py#L2968) | 2968 | `"        ("` | — |
| [SRC-F725E90B2A-L002969](../../tests/test_web_agent.py#L2969) | 2969 | `"            \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\","` | — |
| [SRC-F725E90B2A-L002970](../../tests/test_web_agent.py#L2970) | 2970 | `"            \"Egypt's capital is Cairo\","` | — |
| [SRC-F725E90B2A-L002971](../../tests/test_web_agent.py#L2971) | 2971 | `"            \"The capital city of Egypt is Cairo.\","` | — |
| [SRC-F725E90B2A-L002972](../../tests/test_web_agent.py#L2972) | 2972 | `"        ),"` | — |
| [SRC-F725E90B2A-L002973](../../tests/test_web_agent.py#L2973) | 2973 | `"        ("` | — |
| [SRC-F725E90B2A-L002974](../../tests/test_web_agent.py#L2974) | 2974 | `"            \"حلل أهم التحديات التي تواجه السيارات الكهربائية في مصر، وقارن بين التكلفة والبنية التحتية والشحن. استخدم مصادر متعددة، وميز بين الحقائق والاستنتاجات، واذكر روابط المصادر.\","` | — |
| [SRC-F725E90B2A-L002975](../../tests/test_web_agent.py#L2975) | 2975 | `"            \"Electric vehicles in Egypt: charging infrastructure and costs\","` | — |
| [SRC-F725E90B2A-L002976](../../tests/test_web_agent.py#L2976) | 2976 | `"            \"Electric cars face high costs and limited charging infrastructure in Egypt.\","` | — |
| [SRC-F725E90B2A-L002977](../../tests/test_web_agent.py#L2977) | 2977 | `"        ),"` | — |
| [SRC-F725E90B2A-L002978](../../tests/test_web_agent.py#L2978) | 2978 | `"        ("` | — |
| [SRC-F725E90B2A-L002979](../../tests/test_web_agent.py#L2979) | 2979 | `"            \"ما أحدث التطورات في وكلاء الذكاء الاصطناعي خلال الأيام السبعة الماضية؟ اذكر تواريخ الأخبار وروابط المصادر، ولا تعرض معلومات قديمة باعتبارها جديدة.\","` | — |
| [SRC-F725E90B2A-L002980](../../tests/test_web_agent.py#L2980) | 2980 | `"            \"Recent developments in AI agents\","` | — |
| [SRC-F725E90B2A-L002981](../../tests/test_web_agent.py#L2981) | 2981 | `"            \"New AI agent tools and launches this week.\","` | — |
| [SRC-F725E90B2A-L002982](../../tests/test_web_agent.py#L2982) | 2982 | `"        ),"` | — |
| [SRC-F725E90B2A-L002983](../../tests/test_web_agent.py#L2983) | 2983 | `"        ("` | — |
| [SRC-F725E90B2A-L002984](../../tests/test_web_agent.py#L2984) | 2984 | `"            \"اجمع آراء وتجارب المستخدمين العامة حول السيارات الكهربائية في مصر. اعرض الآراء الإيجابية والسلبية، واذكر روابط المنشورات أو المصادر المتاحة.\","` | — |
| [SRC-F725E90B2A-L002985](../../tests/test_web_agent.py#L2985) | 2985 | `"            \"Reddit users share electric car experiences in Egypt\","` | — |
| [SRC-F725E90B2A-L002986](../../tests/test_web_agent.py#L2986) | 2986 | `"            \"Owners discuss electric vehicles, charging and daily use.\","` | — |
| [SRC-F725E90B2A-L002987](../../tests/test_web_agent.py#L2987) | 2987 | `"        ),"` | — |
| [SRC-F725E90B2A-L002988](../../tests/test_web_agent.py#L2988) | 2988 | `"    ]"` | — |
| [SRC-F725E90B2A-L002989](../../tests/test_web_agent.py#L2989) | 2989 | `"    for index, (query, title, snippet) in enumerate(cases):"` | — |
| [SRC-F725E90B2A-L002990](../../tests/test_web_agent.py#L2990) | 2990 | `"        agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002991](../../tests/test_web_agent.py#L2991) | 2991 | `"        row = {"` | — |
| [SRC-F725E90B2A-L002992](../../tests/test_web_agent.py#L2992) | 2992 | `"            \"title\": title,"` | — |
| [SRC-F725E90B2A-L002993](../../tests/test_web_agent.py#L2993) | 2993 | `"            \"url\": f\"https://example.com/case-{index}\","` | — |
| [SRC-F725E90B2A-L002994](../../tests/test_web_agent.py#L2994) | 2994 | `"            \"snippet\": snippet,"` | — |
| [SRC-F725E90B2A-L002995](../../tests/test_web_agent.py#L2995) | 2995 | `"            \"provider\": \"fake_provider\","` | — |
| [SRC-F725E90B2A-L002996](../../tests/test_web_agent.py#L2996) | 2996 | `"            \"provider_rank\": 1,"` | — |
| [SRC-F725E90B2A-L002997](../../tests/test_web_agent.py#L2997) | 2997 | `"            \"search_query\": query,"` | — |
| [SRC-F725E90B2A-L002998](../../tests/test_web_agent.py#L2998) | 2998 | `"        }"` | — |
| [SRC-F725E90B2A-L002999](../../tests/test_web_agent.py#L2999) | 2999 | `"        monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _q, row=row: [dict(row)])"` | — |
| [SRC-F725E90B2A-L003000](../../tests/test_web_agent.py#L3000) | 3000 | `"        monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _q, row=row: [dict(row)])"` | — |
| [SRC-F725E90B2A-L003001](../../tests/test_web_agent.py#L3001) | 3001 | `"        # Current-news questions normally add Google News RSS; keep this unit test deterministic."` | — |
| [SRC-F725E90B2A-L003002](../../tests/test_web_agent.py#L3002) | 3002 | `"        monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L003003](../../tests/test_web_agent.py#L3003) | 3003 | `"        results = agent._search_web(query)"` | — |
| [SRC-F725E90B2A-L003004](../../tests/test_web_agent.py#L3004) | 3004 | `"        assert results, f\"Search candidates were all filtered for case {index}\""` | — |
| [SRC-F725E90B2A-L003005](../../tests/test_web_agent.py#L3005) | 3005 | `"        diagnostic = next("` | — |
| [SRC-F725E90B2A-L003006](../../tests/test_web_agent.py#L3006) | 3006 | `"            item for item in agent._provider_diagnostics if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L003007](../../tests/test_web_agent.py#L3007) | 3007 | `"        )"` | — |
| [SRC-F725E90B2A-L003008](../../tests/test_web_agent.py#L3008) | 3008 | `"        assert diagnostic[\"accepted_count\"] == 1"` | — |
| [SRC-F725E90B2A-L003009](../../tests/test_web_agent.py#L3009) | 3009 | `"        assert diagnostic[\"result_count\"] == 1"` | — |
| [SRC-F725E90B2A-L003010](../../tests/test_web_agent.py#L3010) | 3010 | `""` | — |
| [SRC-F725E90B2A-L003011](../../tests/test_web_agent.py#L3011) | 3011 | `""` | — |
| [SRC-F725E90B2A-L003012](../../tests/test_web_agent.py#L3012) | 3012 | `"def test_search_web_classifies_http_challenge_and_rate_limit_as_provider_degradation(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003013](../../tests/test_web_agent.py#L3013) | 3013 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003014](../../tests/test_web_agent.py#L3014) | 3014 | `""` | — |
| [SRC-F725E90B2A-L003015](../../tests/test_web_agent.py#L3015) | 3015 | `"    def http_202(_query):"` | — |
| [SRC-F725E90B2A-L003016](../../tests/test_web_agent.py#L3016) | 3016 | `"        raise RuntimeError(\"HTTP 202\")"` | — |
| [SRC-F725E90B2A-L003017](../../tests/test_web_agent.py#L3017) | 3017 | `""` | — |
| [SRC-F725E90B2A-L003018](../../tests/test_web_agent.py#L3018) | 3018 | `"    def http_429(_query):"` | — |
| [SRC-F725E90B2A-L003019](../../tests/test_web_agent.py#L3019) | 3019 | `"        raise RuntimeError(\"HTTP 429\")"` | — |
| [SRC-F725E90B2A-L003020](../../tests/test_web_agent.py#L3020) | 3020 | `""` | — |
| [SRC-F725E90B2A-L003021](../../tests/test_web_agent.py#L3021) | 3021 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", http_202)"` | — |
| [SRC-F725E90B2A-L003022](../../tests/test_web_agent.py#L3022) | 3022 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", http_429)"` | — |
| [SRC-F725E90B2A-L003023](../../tests/test_web_agent.py#L3023) | 3023 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L003024](../../tests/test_web_agent.py#L3024) | 3024 | `"        agent._search_web(\"renewable energy storage policy\")"` | — |
| [SRC-F725E90B2A-L003025](../../tests/test_web_agent.py#L3025) | 3025 | `""` | — |
| [SRC-F725E90B2A-L003026](../../tests/test_web_agent.py#L3026) | 3026 | `"    statuses = {"` | — |
| [SRC-F725E90B2A-L003027](../../tests/test_web_agent.py#L3027) | 3027 | `"        item[\"provider\"]: item[\"status\"]"` | — |
| [SRC-F725E90B2A-L003028](../../tests/test_web_agent.py#L3028) | 3028 | `"        for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L003029](../../tests/test_web_agent.py#L3029) | 3029 | `"        if item[\"provider\"] in {\"duckduckgo_html\", \"bing_rss\"}"` | — |
| [SRC-F725E90B2A-L003030](../../tests/test_web_agent.py#L3030) | 3030 | `"    }"` | — |
| [SRC-F725E90B2A-L003031](../../tests/test_web_agent.py#L3031) | 3031 | `"    assert statuses[\"duckduckgo_html\"] == \"http_error\""` | — |
| [SRC-F725E90B2A-L003032](../../tests/test_web_agent.py#L3032) | 3032 | `"    assert statuses[\"bing_rss\"] == \"rate_limited\""` | — |
| [SRC-F725E90B2A-L003033](../../tests/test_web_agent.py#L3033) | 3033 | `""` | — |
| [SRC-F725E90B2A-L003034](../../tests/test_web_agent.py#L3034) | 3034 | `""` | — |
| [SRC-F725E90B2A-L003035](../../tests/test_web_agent.py#L3035) | 3035 | `"def test_search_web_records_distinct_candidate_rejection_reasons(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003036](../../tests/test_web_agent.py#L3036) | 3036 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003037](../../tests/test_web_agent.py#L3037) | 3037 | `"    query = \"renewable energy storage\""` | — |
| [SRC-F725E90B2A-L003038](../../tests/test_web_agent.py#L3038) | 3038 | `"    candidates = ["` | — |
| [SRC-F725E90B2A-L003039](../../tests/test_web_agent.py#L3039) | 3039 | `"        \"malformed candidate\","` | — |
| [SRC-F725E90B2A-L003040](../../tests/test_web_agent.py#L3040) | 3040 | `"        {"` | — |
| [SRC-F725E90B2A-L003041](../../tests/test_web_agent.py#L3041) | 3041 | `"            \"title\": \"Unsafe scheme\","` | — |
| [SRC-F725E90B2A-L003042](../../tests/test_web_agent.py#L3042) | 3042 | `"            \"url\": \"javascript:alert(1)\","` | — |
| [SRC-F725E90B2A-L003043](../../tests/test_web_agent.py#L3043) | 3043 | `"            \"snippet\": \"Renewable energy storage report\","` | — |
| [SRC-F725E90B2A-L003044](../../tests/test_web_agent.py#L3044) | 3044 | `"        },"` | — |
| [SRC-F725E90B2A-L003045](../../tests/test_web_agent.py#L3045) | 3045 | `"        {"` | — |
| [SRC-F725E90B2A-L003046](../../tests/test_web_agent.py#L3046) | 3046 | `"            \"title\": \"Translated mirror\","` | — |
| [SRC-F725E90B2A-L003047](../../tests/test_web_agent.py#L3047) | 3047 | `"            \"url\": \"https://translate.google.com/translate?u=https%3A%2F%2Fexample.com\","` | — |
| [SRC-F725E90B2A-L003048](../../tests/test_web_agent.py#L3048) | 3048 | `"            \"snippet\": \"Renewable energy storage\","` | — |
| [SRC-F725E90B2A-L003049](../../tests/test_web_agent.py#L3049) | 3049 | `"        },"` | — |
| [SRC-F725E90B2A-L003050](../../tests/test_web_agent.py#L3050) | 3050 | `"        {"` | — |
| [SRC-F725E90B2A-L003051](../../tests/test_web_agent.py#L3051) | 3051 | `"            \"title\": \"Gardening tips\","` | — |
| [SRC-F725E90B2A-L003052](../../tests/test_web_agent.py#L3052) | 3052 | `"            \"url\": \"https://example.com/gardening\","` | — |
| [SRC-F725E90B2A-L003053](../../tests/test_web_agent.py#L3053) | 3053 | `"            \"snippet\": \"Gardening flowers and house plants\","` | — |
| [SRC-F725E90B2A-L003054](../../tests/test_web_agent.py#L3054) | 3054 | `"        },"` | — |
| [SRC-F725E90B2A-L003055](../../tests/test_web_agent.py#L3055) | 3055 | `"    ]"` | — |
| [SRC-F725E90B2A-L003056](../../tests/test_web_agent.py#L3056) | 3056 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _q: [dict(x) if isinstance(x, dict) else x for x in candidates])"` | — |
| [SRC-F725E90B2A-L003057](../../tests/test_web_agent.py#L3057) | 3057 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _q: [dict(x) if isinstance(x, dict) else x for x in candidates])"` | — |
| [SRC-F725E90B2A-L003058](../../tests/test_web_agent.py#L3058) | 3058 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L003059](../../tests/test_web_agent.py#L3059) | 3059 | `""` | — |
| [SRC-F725E90B2A-L003060](../../tests/test_web_agent.py#L3060) | 3060 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L003061](../../tests/test_web_agent.py#L3061) | 3061 | `"        agent._search_web(query)"` | — |
| [SRC-F725E90B2A-L003062](../../tests/test_web_agent.py#L3062) | 3062 | `""` | — |
| [SRC-F725E90B2A-L003063](../../tests/test_web_agent.py#L3063) | 3063 | `"    diagnostic = next("` | — |
| [SRC-F725E90B2A-L003064](../../tests/test_web_agent.py#L3064) | 3064 | `"        item for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L003065](../../tests/test_web_agent.py#L3065) | 3065 | `"        if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L003066](../../tests/test_web_agent.py#L3066) | 3066 | `"    )"` | — |
| [SRC-F725E90B2A-L003067](../../tests/test_web_agent.py#L3067) | 3067 | `"    assert diagnostic[\"status\"] == \"filtered_all\""` | — |
| [SRC-F725E90B2A-L003068](../../tests/test_web_agent.py#L3068) | 3068 | `"    assert diagnostic[\"result_count\"] == 4"` | — |
| [SRC-F725E90B2A-L003069](../../tests/test_web_agent.py#L3069) | 3069 | `"    assert diagnostic[\"accepted_count\"] == 0"` | — |
| [SRC-F725E90B2A-L003070](../../tests/test_web_agent.py#L3070) | 3070 | `"    assert diagnostic[\"rejected_count\"] == 4"` | — |
| [SRC-F725E90B2A-L003071](../../tests/test_web_agent.py#L3071) | 3071 | `"    assert diagnostic[\"rejection_counts\"] == {"` | — |
| [SRC-F725E90B2A-L003072](../../tests/test_web_agent.py#L3072) | 3072 | `"        \"malformed_candidate\": 1,"` | — |
| [SRC-F725E90B2A-L003073](../../tests/test_web_agent.py#L3073) | 3073 | `"        \"invalid_url_or_unsafe_target\": 1,"` | — |
| [SRC-F725E90B2A-L003074](../../tests/test_web_agent.py#L3074) | 3074 | `"        \"blocked_domain\": 1,"` | — |
| [SRC-F725E90B2A-L003075](../../tests/test_web_agent.py#L3075) | 3075 | `"        \"relevance_below_threshold\": 1,"` | — |
| [SRC-F725E90B2A-L003076](../../tests/test_web_agent.py#L3076) | 3076 | `"    }"` | — |
| [SRC-F725E90B2A-L003077](../../tests/test_web_agent.py#L3077) | 3077 | `"    assert sum(diagnostic[\"rejection_counts\"].values()) == diagnostic[\"rejected_count\"]"` | — |
| [SRC-F725E90B2A-L003078](../../tests/test_web_agent.py#L3078) | 3078 | `""` | — |
| [SRC-F725E90B2A-L003079](../../tests/test_web_agent.py#L3079) | 3079 | `""` | — |
| [SRC-F725E90B2A-L003080](../../tests/test_web_agent.py#L3080) | 3080 | `"def test_search_web_classifies_http_302_as_degraded_without_following_provider_redirect(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003081](../../tests/test_web_agent.py#L3081) | 3081 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003082](../../tests/test_web_agent.py#L3082) | 3082 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L003083](../../tests/test_web_agent.py#L3083) | 3083 | `""` | — |
| [SRC-F725E90B2A-L003084](../../tests/test_web_agent.py#L3084) | 3084 | `"    def redirect_response(query):"` | — |
| [SRC-F725E90B2A-L003085](../../tests/test_web_agent.py#L3085) | 3085 | `"        calls.append((\"duckduckgo_html\", query))"` | — |
| [SRC-F725E90B2A-L003086](../../tests/test_web_agent.py#L3086) | 3086 | `"        raise RuntimeError(\"HTTP 302\")"` | — |
| [SRC-F725E90B2A-L003087](../../tests/test_web_agent.py#L3087) | 3087 | `""` | — |
| [SRC-F725E90B2A-L003088](../../tests/test_web_agent.py#L3088) | 3088 | `"    def no_results(query):"` | — |
| [SRC-F725E90B2A-L003089](../../tests/test_web_agent.py#L3089) | 3089 | `"        calls.append((\"bing_rss\", query))"` | — |
| [SRC-F725E90B2A-L003090](../../tests/test_web_agent.py#L3090) | 3090 | `"        return []"` | — |
| [SRC-F725E90B2A-L003091](../../tests/test_web_agent.py#L3091) | 3091 | `""` | — |
| [SRC-F725E90B2A-L003092](../../tests/test_web_agent.py#L3092) | 3092 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", redirect_response)"` | — |
| [SRC-F725E90B2A-L003093](../../tests/test_web_agent.py#L3093) | 3093 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", no_results)"` | — |
| [SRC-F725E90B2A-L003094](../../tests/test_web_agent.py#L3094) | 3094 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L003095](../../tests/test_web_agent.py#L3095) | 3095 | `""` | — |
| [SRC-F725E90B2A-L003096](../../tests/test_web_agent.py#L3096) | 3096 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L003097](../../tests/test_web_agent.py#L3097) | 3097 | `"        agent._search_web(\"renewable energy storage\")"` | — |
| [SRC-F725E90B2A-L003098](../../tests/test_web_agent.py#L3098) | 3098 | `""` | — |
| [SRC-F725E90B2A-L003099](../../tests/test_web_agent.py#L3099) | 3099 | `"    diagnostic = next("` | — |
| [SRC-F725E90B2A-L003100](../../tests/test_web_agent.py#L3100) | 3100 | `"        item for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L003101](../../tests/test_web_agent.py#L3101) | 3101 | `"        if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L003102](../../tests/test_web_agent.py#L3102) | 3102 | `"    )"` | — |
| [SRC-F725E90B2A-L003103](../../tests/test_web_agent.py#L3103) | 3103 | `"    assert diagnostic[\"status\"] == \"http_error\""` | — |
| [SRC-F725E90B2A-L003104](../../tests/test_web_agent.py#L3104) | 3104 | `"    assert diagnostic[\"error\"] == \"RuntimeError: HTTP 302\""` | — |
| [SRC-F725E90B2A-L003105](../../tests/test_web_agent.py#L3105) | 3105 | `"    assert sum(provider == \"duckduckgo_html\" for provider, _query in calls) == 1"` | — |
| [SRC-F725E90B2A-L003106](../../tests/test_web_agent.py#L3106) | 3106 | `""` | — |
| [SRC-F725E90B2A-L003107](../../tests/test_web_agent.py#L3107) | 3107 | `""` | — |
| [SRC-F725E90B2A-L003108](../../tests/test_web_agent.py#L3108) | 3108 | `"def test_relevance_filter_compacts_prompt_and_rejects_instruction_only_queries():"` | — |
| [SRC-F725E90B2A-L003109](../../tests/test_web_agent.py#L3109) | 3109 | `"    question = \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003110](../../tests/test_web_agent.py#L3110) | 3110 | `"    assert _relevance_ratio(question, \"عاصمة مصر القاهرة\") >= 0.20"` | — |
| [SRC-F725E90B2A-L003111](../../tests/test_web_agent.py#L3111) | 3111 | `"    assert _relevance_ratio("` | — |
| [SRC-F725E90B2A-L003112](../../tests/test_web_agent.py#L3112) | 3112 | `"        \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\","` | — |
| [SRC-F725E90B2A-L003113](../../tests/test_web_agent.py#L3113) | 3113 | `"        \"Football results and unrelated match reports\","` | — |
| [SRC-F725E90B2A-L003114](../../tests/test_web_agent.py#L3114) | 3114 | `"    ) == 0.0"` | — |
| [SRC-F725E90B2A-L003115](../../tests/test_web_agent.py#L3115) | 3115 | `""` | — |
| [SRC-F725E90B2A-L003116](../../tests/test_web_agent.py#L3116) | 3116 | `""` | — |
| [SRC-F725E90B2A-L003117](../../tests/test_web_agent.py#L3117) | 3117 | `"def test_relevance_query_tokens_reject_site_only_and_modifier_only_queries():"` | — |
| [SRC-F725E90B2A-L003118](../../tests/test_web_agent.py#L3118) | 3118 | `"    assert _relevance_query_tokens(\"site:reddit.com\") == set()"` | — |
| [SRC-F725E90B2A-L003119](../../tests/test_web_agent.py#L3119) | 3119 | `"    assert _relevance_query_tokens(\"risks limitations alternatives\") == set()"` | — |
| [SRC-F725E90B2A-L003120](../../tests/test_web_agent.py#L3120) | 3120 | `"    assert _relevance_query_tokens(\"السيارات الكهربائية المستعملة في مصر\")"` | — |
| [SRC-F725E90B2A-L003121](../../tests/test_web_agent.py#L3121) | 3121 | `""` | — |
| [SRC-F725E90B2A-L003122](../../tests/test_web_agent.py#L3122) | 3122 | `""` | — |
| [SRC-F725E90B2A-L003123](../../tests/test_web_agent.py#L3123) | 3123 | `"def test_search_web_compacts_request_before_provider_dispatch(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003124](../../tests/test_web_agent.py#L3124) | 3124 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003125](../../tests/test_web_agent.py#L3125) | 3125 | `"    seen = []"` | — |
| [SRC-F725E90B2A-L003126](../../tests/test_web_agent.py#L3126) | 3126 | `""` | — |
| [SRC-F725E90B2A-L003127](../../tests/test_web_agent.py#L3127) | 3127 | `"    def capture(query):"` | — |
| [SRC-F725E90B2A-L003128](../../tests/test_web_agent.py#L3128) | 3128 | `"        seen.append(query)"` | — |
| [SRC-F725E90B2A-L003129](../../tests/test_web_agent.py#L3129) | 3129 | `"        return []"` | — |
| [SRC-F725E90B2A-L003130](../../tests/test_web_agent.py#L3130) | 3130 | `""` | — |
| [SRC-F725E90B2A-L003131](../../tests/test_web_agent.py#L3131) | 3131 | `"    for env_name in ("` | — |
| [SRC-F725E90B2A-L003132](../../tests/test_web_agent.py#L3132) | 3132 | `"        \"DEEPSEEK_SEARCH_API_KEY\","` | — |
| [SRC-F725E90B2A-L003133](../../tests/test_web_agent.py#L3133) | 3133 | `"        \"BRAVE_SEARCH_API_KEY\","` | — |
| [SRC-F725E90B2A-L003134](../../tests/test_web_agent.py#L3134) | 3134 | `"        \"TAVILY_API_KEY\","` | — |
| [SRC-F725E90B2A-L003135](../../tests/test_web_agent.py#L3135) | 3135 | `"    ):"` | — |
| [SRC-F725E90B2A-L003136](../../tests/test_web_agent.py#L3136) | 3136 | `"        monkeypatch.delenv(env_name, raising=False)"` | — |
| [SRC-F725E90B2A-L003137](../../tests/test_web_agent.py#L3137) | 3137 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", capture)"` | — |
| [SRC-F725E90B2A-L003138](../../tests/test_web_agent.py#L3138) | 3138 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", capture)"` | — |
| [SRC-F725E90B2A-L003139](../../tests/test_web_agent.py#L3139) | 3139 | `""` | — |
| [SRC-F725E90B2A-L003140](../../tests/test_web_agent.py#L3140) | 3140 | `"    raw_question = ("` | — |
| [SRC-F725E90B2A-L003141](../../tests/test_web_agent.py#L3141) | 3141 | `"        \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003142](../../tests/test_web_agent.py#L3142) | 3142 | `"    )"` | — |
| [SRC-F725E90B2A-L003143](../../tests/test_web_agent.py#L3143) | 3143 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L003144](../../tests/test_web_agent.py#L3144) | 3144 | `"        agent._search_web(raw_question)"` | — |
| [SRC-F725E90B2A-L003145](../../tests/test_web_agent.py#L3145) | 3145 | `""` | — |
| [SRC-F725E90B2A-L003146](../../tests/test_web_agent.py#L3146) | 3146 | `"    expected = _normalize_search_query(compact_search_query(raw_question))"` | — |
| [SRC-F725E90B2A-L003147](../../tests/test_web_agent.py#L3147) | 3147 | `"    assert seen"` | — |
| [SRC-F725E90B2A-L003148](../../tests/test_web_agent.py#L3148) | 3148 | `"    assert set(seen) == {expected}"` | — |
| [SRC-F725E90B2A-L003149](../../tests/test_web_agent.py#L3149) | 3149 | `"    assert len(expected) <= 240"` | — |
| [SRC-F725E90B2A-L003150](../../tests/test_web_agent.py#L3150) | 3150 | `"    assert \"رابط مباشر\" not in \" \".join(seen)"` | — |
| [SRC-F725E90B2A-L003151](../../tests/test_web_agent.py#L3151) | 3151 | `""` | — |
| [SRC-F725E90B2A-L003152](../../tests/test_web_agent.py#L3152) | 3152 | `""` | — |
| [SRC-F725E90B2A-L003153](../../tests/test_web_agent.py#L3153) | 3153 | `"def test_search_web_does_not_dispatch_instruction_only_query(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003154](../../tests/test_web_agent.py#L3154) | 3154 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003155](../../tests/test_web_agent.py#L3155) | 3155 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003156](../../tests/test_web_agent.py#L3156) | 3156 | `"        agent, \"_search_duckduckgo_html\","` | — |
| [SRC-F725E90B2A-L003157](../../tests/test_web_agent.py#L3157) | 3157 | `"        lambda query: pytest.fail(f\"provider should not receive {query!r}\"),"` | — |
| [SRC-F725E90B2A-L003158](../../tests/test_web_agent.py#L3158) | 3158 | `"    )"` | — |
| [SRC-F725E90B2A-L003159](../../tests/test_web_agent.py#L3159) | 3159 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003160](../../tests/test_web_agent.py#L3160) | 3160 | `"        agent, \"_search_bing_rss\","` | — |
| [SRC-F725E90B2A-L003161](../../tests/test_web_agent.py#L3161) | 3161 | `"        lambda query: pytest.fail(f\"provider should not receive {query!r}\"),"` | — |
| [SRC-F725E90B2A-L003162](../../tests/test_web_agent.py#L3162) | 3162 | `"    )"` | — |
| [SRC-F725E90B2A-L003163](../../tests/test_web_agent.py#L3163) | 3163 | `"    results = agent._search_web(\"اذكر مصادر موثوقة، روابط مباشرة، باختصار\")"` | — |
| [SRC-F725E90B2A-L003164](../../tests/test_web_agent.py#L3164) | 3164 | `"    assert results == []"` | — |
| [SRC-F725E90B2A-L003165](../../tests/test_web_agent.py#L3165) | 3165 | `""` | — |
| [SRC-F725E90B2A-L003166](../../tests/test_web_agent.py#L3166) | 3166 | `""` | — |
| [SRC-F725E90B2A-L003167](../../tests/test_web_agent.py#L3167) | 3167 | `"def test_plan_search_does_not_call_planner_without_a_topic(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003168](../../tests/test_web_agent.py#L3168) | 3168 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003169](../../tests/test_web_agent.py#L3169) | 3169 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003170](../../tests/test_web_agent.py#L3170) | 3170 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003171](../../tests/test_web_agent.py#L3171) | 3171 | `"        agent, \"_request_completion\","` | — |
| [SRC-F725E90B2A-L003172](../../tests/test_web_agent.py#L3172) | 3172 | `"        lambda *args, **kwargs: pytest.fail(\"planner should not run without a topic\"),"` | — |
| [SRC-F725E90B2A-L003173](../../tests/test_web_agent.py#L3173) | 3173 | `"    )"` | — |
| [SRC-F725E90B2A-L003174](../../tests/test_web_agent.py#L3174) | 3174 | `"    plan = agent._plan_search("` | — |
| [SRC-F725E90B2A-L003175](../../tests/test_web_agent.py#L3175) | 3175 | `"        \"استخدم مصادر متعددة، واذكر روابط المصادر\","` | — |
| [SRC-F725E90B2A-L003176](../../tests/test_web_agent.py#L3176) | 3176 | `"        [],"` | — |
| [SRC-F725E90B2A-L003177](../../tests/test_web_agent.py#L3177) | 3177 | `"    )"` | — |
| [SRC-F725E90B2A-L003178](../../tests/test_web_agent.py#L3178) | 3178 | `"    assert plan[\"queries\"] == []"` | — |
| [SRC-F725E90B2A-L003179](../../tests/test_web_agent.py#L3179) | 3179 | `""` | — |
| [SRC-F725E90B2A-L003180](../../tests/test_web_agent.py#L3180) | 3180 | `""` | — |
| [SRC-F725E90B2A-L003181](../../tests/test_web_agent.py#L3181) | 3181 | `"def test_plan_search_compacts_followup_query_before_fallback(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003182](../../tests/test_web_agent.py#L3182) | 3182 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003183](../../tests/test_web_agent.py#L3183) | 3183 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L003184](../../tests/test_web_agent.py#L3184) | 3184 | `"    history = ["` | — |
| [SRC-F725E90B2A-L003185](../../tests/test_web_agent.py#L3185) | 3185 | `"        {"` | — |
| [SRC-F725E90B2A-L003186](../../tests/test_web_agent.py#L3186) | 3186 | `"            \"role\": \"user\","` | — |
| [SRC-F725E90B2A-L003187](../../tests/test_web_agent.py#L3187) | 3187 | `"            \"content\": ("` | — |
| [SRC-F725E90B2A-L003188](../../tests/test_web_agent.py#L3188) | 3188 | `"                \"قارن السيارات الكهربائية في مصر. استخدم مصادر متعددة، \""` | — |
| [SRC-F725E90B2A-L003189](../../tests/test_web_agent.py#L3189) | 3189 | `"                \"واذكر روابط المصادر وأجب بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003190](../../tests/test_web_agent.py#L3190) | 3190 | `"            ),"` | — |
| [SRC-F725E90B2A-L003191](../../tests/test_web_agent.py#L3191) | 3191 | `"        },"` | — |
| [SRC-F725E90B2A-L003192](../../tests/test_web_agent.py#L3192) | 3192 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن مقارنة موثقة.\"},"` | — |
| [SRC-F725E90B2A-L003193](../../tests/test_web_agent.py#L3193) | 3193 | `"    ]"` | — |
| [SRC-F725E90B2A-L003194](../../tests/test_web_agent.py#L3194) | 3194 | `"    plan = agent._plan_search(\"وطب الأسعار الحالية؟\", history)"` | — |
| [SRC-F725E90B2A-L003195](../../tests/test_web_agent.py#L3195) | 3195 | `""` | — |
| [SRC-F725E90B2A-L003196](../../tests/test_web_agent.py#L3196) | 3196 | `"    assert plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L003197](../../tests/test_web_agent.py#L3197) | 3197 | `"    assert all(len(query) <= 240 for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L003198](../../tests/test_web_agent.py#L3198) | 3198 | `"    assert any(\"السيارات الكهربائية\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L003199](../../tests/test_web_agent.py#L3199) | 3199 | `"    assert all("` | — |
| [SRC-F725E90B2A-L003200](../../tests/test_web_agent.py#L3200) | 3200 | `"        \"روابط المصادر\" not in query and \"أجب بإيجاز\" not in query"` | — |
| [SRC-F725E90B2A-L003201](../../tests/test_web_agent.py#L3201) | 3201 | `"        for query in plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L003202](../../tests/test_web_agent.py#L3202) | 3202 | `"    )"` | — |
| [SRC-F725E90B2A-L003203](../../tests/test_web_agent.py#L3203) | 3203 | `""` | — |
| [SRC-F725E90B2A-L003204](../../tests/test_web_agent.py#L3204) | 3204 | `""` | — |
| [SRC-F725E90B2A-L003205](../../tests/test_web_agent.py#L3205) | 3205 | `"@pytest.mark.parametrize(\"fallback_queries\", [[], None])"` | — |
| [SRC-F725E90B2A-L003206](../../tests/test_web_agent.py#L3206) | 3206 | `"def test_auto_mode_does_not_reinsert_raw_question_when_fallback_has_no_query("` | — |
| [SRC-F725E90B2A-L003207](../../tests/test_web_agent.py#L3207) | 3207 | `"    monkeypatch, fallback_queries"` | — |
| [SRC-F725E90B2A-L003208](../../tests/test_web_agent.py#L3208) | 3208 | `"):"` | — |
| [SRC-F725E90B2A-L003209](../../tests/test_web_agent.py#L3209) | 3209 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003210](../../tests/test_web_agent.py#L3210) | 3210 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003211](../../tests/test_web_agent.py#L3211) | 3211 | `"    question = ("` | — |
| [SRC-F725E90B2A-L003212](../../tests/test_web_agent.py#L3212) | 3212 | `"        \"ما عيوب السيارات الكهربائية المستعملة في مصر؟ \""` | — |
| [SRC-F725E90B2A-L003213](../../tests/test_web_agent.py#L3213) | 3213 | `"        \"اذكر مصادر موثوقة وروابط مباشرة وأجب بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003214](../../tests/test_web_agent.py#L3214) | 3214 | `"    )"` | — |
| [SRC-F725E90B2A-L003215](../../tests/test_web_agent.py#L3215) | 3215 | `"    observed_plans = []"` | — |
| [SRC-F725E90B2A-L003216](../../tests/test_web_agent.py#L3216) | 3216 | `""` | — |
| [SRC-F725E90B2A-L003217](../../tests/test_web_agent.py#L3217) | 3217 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003218](../../tests/test_web_agent.py#L3218) | 3218 | `"        \"agents.web_agent.route_intent\","` | — |
| [SRC-F725E90B2A-L003219](../../tests/test_web_agent.py#L3219) | 3219 | `"        lambda *args, **kwargs: {\"route\": \"WEB_SIMPLE\", \"reason\": \"test\"},"` | — |
| [SRC-F725E90B2A-L003220](../../tests/test_web_agent.py#L3220) | 3220 | `"    )"` | — |
| [SRC-F725E90B2A-L003221](../../tests/test_web_agent.py#L3221) | 3221 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003222](../../tests/test_web_agent.py#L3222) | 3222 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003223](../../tests/test_web_agent.py#L3223) | 3223 | `"        lambda _question, _history: {"` | — |
| [SRC-F725E90B2A-L003224](../../tests/test_web_agent.py#L3224) | 3224 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L003225](../../tests/test_web_agent.py#L3225) | 3225 | `"            \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003226](../../tests/test_web_agent.py#L3226) | 3226 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003227](../../tests/test_web_agent.py#L3227) | 3227 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003228](../../tests/test_web_agent.py#L3228) | 3228 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003229](../../tests/test_web_agent.py#L3229) | 3229 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003230](../../tests/test_web_agent.py#L3230) | 3230 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003231](../../tests/test_web_agent.py#L3231) | 3231 | `"        },"` | — |
| [SRC-F725E90B2A-L003232](../../tests/test_web_agent.py#L3232) | 3232 | `"    )"` | — |
| [SRC-F725E90B2A-L003233](../../tests/test_web_agent.py#L3233) | 3233 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003234](../../tests/test_web_agent.py#L3234) | 3234 | `"        \"agents.web_agent.fallback_plan\","` | — |
| [SRC-F725E90B2A-L003235](../../tests/test_web_agent.py#L3235) | 3235 | `"        lambda *args, **kwargs: {\"queries\": fallback_queries},"` | — |
| [SRC-F725E90B2A-L003236](../../tests/test_web_agent.py#L3236) | 3236 | `"    )"` | — |
| [SRC-F725E90B2A-L003237](../../tests/test_web_agent.py#L3237) | 3237 | `""` | — |
| [SRC-F725E90B2A-L003238](../../tests/test_web_agent.py#L3238) | 3238 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003239](../../tests/test_web_agent.py#L3239) | 3239 | `"        observed_plans.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003240](../../tests/test_web_agent.py#L3240) | 3240 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L003241](../../tests/test_web_agent.py#L3241) | 3241 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003242](../../tests/test_web_agent.py#L3242) | 3242 | `"            \"queries_attempted\": 0,"` | — |
| [SRC-F725E90B2A-L003243](../../tests/test_web_agent.py#L3243) | 3243 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003244](../../tests/test_web_agent.py#L3244) | 3244 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L003245](../../tests/test_web_agent.py#L3245) | 3245 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L003246](../../tests/test_web_agent.py#L3246) | 3246 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L003247](../../tests/test_web_agent.py#L3247) | 3247 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003248](../../tests/test_web_agent.py#L3248) | 3248 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003249](../../tests/test_web_agent.py#L3249) | 3249 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L003250](../../tests/test_web_agent.py#L3250) | 3250 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003251](../../tests/test_web_agent.py#L3251) | 3251 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003252](../../tests/test_web_agent.py#L3252) | 3252 | `"        }"` | — |
| [SRC-F725E90B2A-L003253](../../tests/test_web_agent.py#L3253) | 3253 | `""` | — |
| [SRC-F725E90B2A-L003254](../../tests/test_web_agent.py#L3254) | 3254 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003255](../../tests/test_web_agent.py#L3255) | 3255 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"لا تتوفر مصادر كافية.\")"` | — |
| [SRC-F725E90B2A-L003256](../../tests/test_web_agent.py#L3256) | 3256 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-F725E90B2A-L003257](../../tests/test_web_agent.py#L3257) | 3257 | `""` | — |
| [SRC-F725E90B2A-L003258](../../tests/test_web_agent.py#L3258) | 3258 | `"    agent.answer(question, mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L003259](../../tests/test_web_agent.py#L3259) | 3259 | `""` | — |
| [SRC-F725E90B2A-L003260](../../tests/test_web_agent.py#L3260) | 3260 | `"    assert observed_plans"` | — |
| [SRC-F725E90B2A-L003261](../../tests/test_web_agent.py#L3261) | 3261 | `"    assert question not in observed_plans[0][\"queries\"]"` | — |
| [SRC-F725E90B2A-L003262](../../tests/test_web_agent.py#L3262) | 3262 | `"    assert observed_plans[0][\"queries\"]"` | — |
| [SRC-F725E90B2A-L003263](../../tests/test_web_agent.py#L3263) | 3263 | `"    assert observed_plans[0][\"queries\"][0] == compact_search_query(question)"` | — |
| [SRC-F725E90B2A-L003264](../../tests/test_web_agent.py#L3264) | 3264 | `""` | — |
| [SRC-F725E90B2A-L003265](../../tests/test_web_agent.py#L3265) | 3265 | `""` | — |
| [SRC-F725E90B2A-L003266](../../tests/test_web_agent.py#L3266) | 3266 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L003267](../../tests/test_web_agent.py#L3267) | 3267 | `"    (\"question\", \"planned_query\"),"` | — |
| [SRC-F725E90B2A-L003268](../../tests/test_web_agent.py#L3268) | 3268 | `"    ["` | — |
| [SRC-F725E90B2A-L003269](../../tests/test_web_agent.py#L3269) | 3269 | `"        ("` | — |
| [SRC-F725E90B2A-L003270](../../tests/test_web_agent.py#L3270) | 3270 | `"            ("` | — |
| [SRC-F725E90B2A-L003271](../../tests/test_web_agent.py#L3271) | 3271 | `"                \"ما عيوب السيارات الكهربائية المستعملة في مصر؟ \""` | — |
| [SRC-F725E90B2A-L003272](../../tests/test_web_agent.py#L3272) | 3272 | `"                \"اذكر مصادر موثوقة وروابط مباشرة وأجب بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003273](../../tests/test_web_agent.py#L3273) | 3273 | `"            ),"` | — |
| [SRC-F725E90B2A-L003274](../../tests/test_web_agent.py#L3274) | 3274 | `"            None,"` | — |
| [SRC-F725E90B2A-L003275](../../tests/test_web_agent.py#L3275) | 3275 | `"        ),"` | — |
| [SRC-F725E90B2A-L003276](../../tests/test_web_agent.py#L3276) | 3276 | `"        ("` | — |
| [SRC-F725E90B2A-L003277](../../tests/test_web_agent.py#L3277) | 3277 | `"            \"كام سعرها؟ اذكر مصادر موثوقة وروابط مباشرة وأجب بإيجاز.\","` | — |
| [SRC-F725E90B2A-L003278](../../tests/test_web_agent.py#L3278) | 3278 | `"            \"أسعار السيارات الكهربائية المستعملة في مصر\","` | — |
| [SRC-F725E90B2A-L003279](../../tests/test_web_agent.py#L3279) | 3279 | `"        ),"` | — |
| [SRC-F725E90B2A-L003280](../../tests/test_web_agent.py#L3280) | 3280 | `"    ],"` | — |
| [SRC-F725E90B2A-L003281](../../tests/test_web_agent.py#L3281) | 3281 | `")"` | — |
| [SRC-F725E90B2A-L003282](../../tests/test_web_agent.py#L3282) | 3282 | `"def test_server_search_sources_use_compact_question_and_topic_plan("` | — |
| [SRC-F725E90B2A-L003283](../../tests/test_web_agent.py#L3283) | 3283 | `"    monkeypatch, question, planned_query"` | — |
| [SRC-F725E90B2A-L003284](../../tests/test_web_agent.py#L3284) | 3284 | `"):"` | — |
| [SRC-F725E90B2A-L003285](../../tests/test_web_agent.py#L3285) | 3285 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003286](../../tests/test_web_agent.py#L3286) | 3286 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003287](../../tests/test_web_agent.py#L3287) | 3287 | `"    topic_query = planned_query or compact_search_query(question)"` | — |
| [SRC-F725E90B2A-L003288](../../tests/test_web_agent.py#L3288) | 3288 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003289](../../tests/test_web_agent.py#L3289) | 3289 | `"        \"queries\": [topic_query],"` | — |
| [SRC-F725E90B2A-L003290](../../tests/test_web_agent.py#L3290) | 3290 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003291](../../tests/test_web_agent.py#L3291) | 3291 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003292](../../tests/test_web_agent.py#L3292) | 3292 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003293](../../tests/test_web_agent.py#L3293) | 3293 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003294](../../tests/test_web_agent.py#L3294) | 3294 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003295](../../tests/test_web_agent.py#L3295) | 3295 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003296](../../tests/test_web_agent.py#L3296) | 3296 | `"    }"` | — |
| [SRC-F725E90B2A-L003297](../../tests/test_web_agent.py#L3297) | 3297 | `"    source_queries = []"` | — |
| [SRC-F725E90B2A-L003298](../../tests/test_web_agent.py#L3298) | 3298 | `""` | — |
| [SRC-F725E90B2A-L003299](../../tests/test_web_agent.py#L3299) | 3299 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda _question, _history: dict(plan))"` | — |
| [SRC-F725E90B2A-L003300](../../tests/test_web_agent.py#L3300) | 3300 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003301](../../tests/test_web_agent.py#L3301) | 3301 | `"        agent, \"_collect_research\","` | — |
| [SRC-F725E90B2A-L003302](../../tests/test_web_agent.py#L3302) | 3302 | `"        lambda research_plan: ([sample_source(0), sample_source(1)], [], {"` | — |
| [SRC-F725E90B2A-L003303](../../tests/test_web_agent.py#L3303) | 3303 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L003304](../../tests/test_web_agent.py#L3304) | 3304 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003305](../../tests/test_web_agent.py#L3305) | 3305 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003306](../../tests/test_web_agent.py#L3306) | 3306 | `"            \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L003307](../../tests/test_web_agent.py#L3307) | 3307 | `"            \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L003308](../../tests/test_web_agent.py#L3308) | 3308 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003309](../../tests/test_web_agent.py#L3309) | 3309 | `"            \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-F725E90B2A-L003310](../../tests/test_web_agent.py#L3310) | 3310 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003311](../../tests/test_web_agent.py#L3311) | 3311 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003312](../../tests/test_web_agent.py#L3312) | 3312 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003313](../../tests/test_web_agent.py#L3313) | 3313 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003314](../../tests/test_web_agent.py#L3314) | 3314 | `"        }),"` | — |
| [SRC-F725E90B2A-L003315](../../tests/test_web_agent.py#L3315) | 3315 | `"    )"` | — |
| [SRC-F725E90B2A-L003316](../../tests/test_web_agent.py#L3316) | 3316 | `""` | — |
| [SRC-F725E90B2A-L003317](../../tests/test_web_agent.py#L3317) | 3317 | `"    def generate(*args, **kwargs):"` | — |
| [SRC-F725E90B2A-L003318](../../tests/test_web_agent.py#L3318) | 3318 | `"        agent.server_search_sources = [{"` | — |
| [SRC-F725E90B2A-L003319](../../tests/test_web_agent.py#L3319) | 3319 | `"            \"title\": \"تجارب السيارات الكهربائية المستعملة\","` | — |
| [SRC-F725E90B2A-L003320](../../tests/test_web_agent.py#L3320) | 3320 | `"            \"url\": \"https://example.org/ev-used-cars\","` | — |
| [SRC-F725E90B2A-L003321](../../tests/test_web_agent.py#L3321) | 3321 | `"            \"snippet\": \"تكلفة البطارية والمدى الفعلي للسيارات الكهربائية المستعملة في مصر\","` | — |
| [SRC-F725E90B2A-L003322](../../tests/test_web_agent.py#L3322) | 3322 | `"            \"page_text\": \"تكلفة البطارية والمدى الفعلي للسيارات الكهربائية المستعملة في مصر\","` | — |
| [SRC-F725E90B2A-L003323](../../tests/test_web_agent.py#L3323) | 3323 | `"            \"page_fetched\": False,"` | — |
| [SRC-F725E90B2A-L003324](../../tests/test_web_agent.py#L3324) | 3324 | `"            \"provider\": \"openrouter_web_search\","` | — |
| [SRC-F725E90B2A-L003325](../../tests/test_web_agent.py#L3325) | 3325 | `"            \"providers\": [\"openrouter_web_search\"],"` | — |
| [SRC-F725E90B2A-L003326](../../tests/test_web_agent.py#L3326) | 3326 | `"            \"queries\": [],"` | — |
| [SRC-F725E90B2A-L003327](../../tests/test_web_agent.py#L3327) | 3327 | `"            \"domain\": \"example.org\","` | — |
| [SRC-F725E90B2A-L003328](../../tests/test_web_agent.py#L3328) | 3328 | `"            \"source_class\": \"general\","` | — |
| [SRC-F725E90B2A-L003329](../../tests/test_web_agent.py#L3329) | 3329 | `"            \"platform\": \"web\","` | — |
| [SRC-F725E90B2A-L003330](../../tests/test_web_agent.py#L3330) | 3330 | `"            \"published_at\": \"\","` | — |
| [SRC-F725E90B2A-L003331](../../tests/test_web_agent.py#L3331) | 3331 | `"        }]"` | — |
| [SRC-F725E90B2A-L003332](../../tests/test_web_agent.py#L3332) | 3332 | `"        return \"إجابة مبدئية [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L003333](../../tests/test_web_agent.py#L3333) | 3333 | `""` | — |
| [SRC-F725E90B2A-L003334](../../tests/test_web_agent.py#L3334) | 3334 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-F725E90B2A-L003335](../../tests/test_web_agent.py#L3335) | 3335 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-F725E90B2A-L003336](../../tests/test_web_agent.py#L3336) | 3336 | `""` | — |
| [SRC-F725E90B2A-L003337](../../tests/test_web_agent.py#L3337) | 3337 | `"    def capture_relevance(query, text):"` | — |
| [SRC-F725E90B2A-L003338](../../tests/test_web_agent.py#L3338) | 3338 | `"        if \"تجارب السيارات الكهربائية المستعملة\" in text:"` | — |
| [SRC-F725E90B2A-L003339](../../tests/test_web_agent.py#L3339) | 3339 | `"            source_queries.append(query)"` | — |
| [SRC-F725E90B2A-L003340](../../tests/test_web_agent.py#L3340) | 3340 | `"            if planned_query and query != compact_search_query(topic_query):"` | — |
| [SRC-F725E90B2A-L003341](../../tests/test_web_agent.py#L3341) | 3341 | `"                return 0.0"` | — |
| [SRC-F725E90B2A-L003342](../../tests/test_web_agent.py#L3342) | 3342 | `"        return 0.25"` | — |
| [SRC-F725E90B2A-L003343](../../tests/test_web_agent.py#L3343) | 3343 | `""` | — |
| [SRC-F725E90B2A-L003344](../../tests/test_web_agent.py#L3344) | 3344 | `"    monkeypatch.setattr(\"agents.web_agent._relevance_ratio\", capture_relevance)"` | — |
| [SRC-F725E90B2A-L003345](../../tests/test_web_agent.py#L3345) | 3345 | `""` | — |
| [SRC-F725E90B2A-L003346](../../tests/test_web_agent.py#L3346) | 3346 | `"    agent.answer(question)"` | — |
| [SRC-F725E90B2A-L003347](../../tests/test_web_agent.py#L3347) | 3347 | `""` | — |
| [SRC-F725E90B2A-L003348](../../tests/test_web_agent.py#L3348) | 3348 | `"    expected_queries = list(dict.fromkeys("` | — |
| [SRC-F725E90B2A-L003349](../../tests/test_web_agent.py#L3349) | 3349 | `"        query for query in ("` | — |
| [SRC-F725E90B2A-L003350](../../tests/test_web_agent.py#L3350) | 3350 | `"            compact_search_query(question),"` | — |
| [SRC-F725E90B2A-L003351](../../tests/test_web_agent.py#L3351) | 3351 | `"            compact_search_query(topic_query),"` | — |
| [SRC-F725E90B2A-L003352](../../tests/test_web_agent.py#L3352) | 3352 | `"        ) if query"` | — |
| [SRC-F725E90B2A-L003353](../../tests/test_web_agent.py#L3353) | 3353 | `"    ))"` | — |
| [SRC-F725E90B2A-L003354](../../tests/test_web_agent.py#L3354) | 3354 | `"    assert source_queries == expected_queries"` | — |
| [SRC-F725E90B2A-L003355](../../tests/test_web_agent.py#L3355) | 3355 | `""` | — |
| [SRC-F725E90B2A-L003356](../../tests/test_web_agent.py#L3356) | 3356 | `""` | — |
| [SRC-F725E90B2A-L003357](../../tests/test_web_agent.py#L3357) | 3357 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L003358](../../tests/test_web_agent.py#L3358) | 3358 | `"    (\"mode\", \"planner_query\"),"` | — |
| [SRC-F725E90B2A-L003359](../../tests/test_web_agent.py#L3359) | 3359 | `"    ["` | — |
| [SRC-F725E90B2A-L003360](../../tests/test_web_agent.py#L3360) | 3360 | `"        (\"auto\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003361](../../tests/test_web_agent.py#L3361) | 3361 | `"        (\"auto\", \"site:reddit.com\"),"` | — |
| [SRC-F725E90B2A-L003362](../../tests/test_web_agent.py#L3362) | 3362 | `"        (\"latest\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003363](../../tests/test_web_agent.py#L3363) | 3363 | `"        (\"deep\", \"site:reddit.com\"),"` | — |
| [SRC-F725E90B2A-L003364](../../tests/test_web_agent.py#L3364) | 3364 | `"        (\"social\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003365](../../tests/test_web_agent.py#L3365) | 3365 | `"    ],"` | — |
| [SRC-F725E90B2A-L003366](../../tests/test_web_agent.py#L3366) | 3366 | `")"` | — |
| [SRC-F725E90B2A-L003367](../../tests/test_web_agent.py#L3367) | 3367 | `"def test_modes_do_not_create_generic_queries_without_topic("` | — |
| [SRC-F725E90B2A-L003368](../../tests/test_web_agent.py#L3368) | 3368 | `"    monkeypatch, mode, planner_query"` | — |
| [SRC-F725E90B2A-L003369](../../tests/test_web_agent.py#L3369) | 3369 | `"):"` | — |
| [SRC-F725E90B2A-L003370](../../tests/test_web_agent.py#L3370) | 3370 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003371](../../tests/test_web_agent.py#L3371) | 3371 | `"    instruction_only = \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\""` | — |
| [SRC-F725E90B2A-L003372](../../tests/test_web_agent.py#L3372) | 3372 | `"    direct_url = \"https://example.com/report\""` | — |
| [SRC-F725E90B2A-L003373](../../tests/test_web_agent.py#L3373) | 3373 | `"    observed_plans = []"` | — |
| [SRC-F725E90B2A-L003374](../../tests/test_web_agent.py#L3374) | 3374 | `""` | — |
| [SRC-F725E90B2A-L003375](../../tests/test_web_agent.py#L3375) | 3375 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003376](../../tests/test_web_agent.py#L3376) | 3376 | `"        \"agents.web_agent.route_intent\","` | — |
| [SRC-F725E90B2A-L003377](../../tests/test_web_agent.py#L3377) | 3377 | `"        lambda *args, **kwargs: {\"route\": \"WEB_DEEP\", \"reason\": \"test\"},"` | — |
| [SRC-F725E90B2A-L003378](../../tests/test_web_agent.py#L3378) | 3378 | `"    )"` | — |
| [SRC-F725E90B2A-L003379](../../tests/test_web_agent.py#L3379) | 3379 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003380](../../tests/test_web_agent.py#L3380) | 3380 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003381](../../tests/test_web_agent.py#L3381) | 3381 | `"        lambda _question, _history: {"` | — |
| [SRC-F725E90B2A-L003382](../../tests/test_web_agent.py#L3382) | 3382 | `"            \"queries\": [planner_query],"` | — |
| [SRC-F725E90B2A-L003383](../../tests/test_web_agent.py#L3383) | 3383 | `"            \"direct_urls\": [direct_url],"` | — |
| [SRC-F725E90B2A-L003384](../../tests/test_web_agent.py#L3384) | 3384 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003385](../../tests/test_web_agent.py#L3385) | 3385 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003386](../../tests/test_web_agent.py#L3386) | 3386 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L003387](../../tests/test_web_agent.py#L3387) | 3387 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003388](../../tests/test_web_agent.py#L3388) | 3388 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003389](../../tests/test_web_agent.py#L3389) | 3389 | `"        },"` | — |
| [SRC-F725E90B2A-L003390](../../tests/test_web_agent.py#L3390) | 3390 | `"    )"` | — |
| [SRC-F725E90B2A-L003391](../../tests/test_web_agent.py#L3391) | 3391 | `""` | — |
| [SRC-F725E90B2A-L003392](../../tests/test_web_agent.py#L3392) | 3392 | `"    def collect(research_plan):"` | — |
