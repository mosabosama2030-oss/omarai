# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **048**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L002643 إلى SRC-F725E90B2A-L003442
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L002643](../../tests/test_web_agent.py#L2643) | 2643 | `"        \"https://example.test:443/path?q=1\","` | — |
| [SRC-F725E90B2A-L002644](../../tests/test_web_agent.py#L2644) | 2644 | `"        \"93.184.216.34\","` | — |
| [SRC-F725E90B2A-L002645](../../tests/test_web_agent.py#L2645) | 2645 | `"    ) == \"https://93.184.216.34:443/path?q=1\""` | — |
| [SRC-F725E90B2A-L002646](../../tests/test_web_agent.py#L2646) | 2646 | `""` | — |
| [SRC-F725E90B2A-L002647](../../tests/test_web_agent.py#L2647) | 2647 | `""` | — |
| [SRC-F725E90B2A-L002648](../../tests/test_web_agent.py#L2648) | 2648 | `"def test_fetch_page_rejects_private_redirect_before_connecting(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002649](../../tests/test_web_agent.py#L2649) | 2649 | `"    from contextlib import contextmanager"` | — |
| [SRC-F725E90B2A-L002650](../../tests/test_web_agent.py#L2650) | 2650 | `""` | — |
| [SRC-F725E90B2A-L002651](../../tests/test_web_agent.py#L2651) | 2651 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002652](../../tests/test_web_agent.py#L2652) | 2652 | `""` | — |
| [SRC-F725E90B2A-L002653](../../tests/test_web_agent.py#L2653) | 2653 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L002654](../../tests/test_web_agent.py#L2654) | 2654 | `""` | — |
| [SRC-F725E90B2A-L002655](../../tests/test_web_agent.py#L2655) | 2655 | `"    resolved_hosts = []"` | — |
| [SRC-F725E90B2A-L002656](../../tests/test_web_agent.py#L2656) | 2656 | `"    requests = []"` | — |
| [SRC-F725E90B2A-L002657](../../tests/test_web_agent.py#L2657) | 2657 | `""` | — |
| [SRC-F725E90B2A-L002658](../../tests/test_web_agent.py#L2658) | 2658 | `"    def resolve_public_ip(host):"` | — |
| [SRC-F725E90B2A-L002659](../../tests/test_web_agent.py#L2659) | 2659 | `"        resolved_hosts.append(host)"` | — |
| [SRC-F725E90B2A-L002660](../../tests/test_web_agent.py#L2660) | 2660 | `"        return [\"93.184.216.34\"] if host == \"first.example\" else None"` | — |
| [SRC-F725E90B2A-L002661](../../tests/test_web_agent.py#L2661) | 2661 | `""` | — |
| [SRC-F725E90B2A-L002662](../../tests/test_web_agent.py#L2662) | 2662 | `"    monkeypatch.setattr(web_agent, \"_public_ip_literals\", resolve_public_ip)"` | — |
| [SRC-F725E90B2A-L002663](../../tests/test_web_agent.py#L2663) | 2663 | `""` | — |
| [SRC-F725E90B2A-L002664](../../tests/test_web_agent.py#L2664) | 2664 | `"    class RedirectResponse:"` | — |
| [SRC-F725E90B2A-L002665](../../tests/test_web_agent.py#L2665) | 2665 | `"        status_code = 302"` | — |
| [SRC-F725E90B2A-L002666](../../tests/test_web_agent.py#L2666) | 2666 | `""` | — |
| [SRC-F725E90B2A-L002667](../../tests/test_web_agent.py#L2667) | 2667 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L002668](../../tests/test_web_agent.py#L2668) | 2668 | `"            self.headers = {\"location\": \"http://127.0.0.1/admin\"}"` | — |
| [SRC-F725E90B2A-L002669](../../tests/test_web_agent.py#L2669) | 2669 | `""` | — |
| [SRC-F725E90B2A-L002670](../../tests/test_web_agent.py#L2670) | 2670 | `"    @contextmanager"` | — |
| [SRC-F725E90B2A-L002671](../../tests/test_web_agent.py#L2671) | 2671 | `"    def fake_stream(self, method, url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002672](../../tests/test_web_agent.py#L2672) | 2672 | `"        requests.append((method, str(url), kwargs))"` | — |
| [SRC-F725E90B2A-L002673](../../tests/test_web_agent.py#L2673) | 2673 | `"        yield RedirectResponse()"` | — |
| [SRC-F725E90B2A-L002674](../../tests/test_web_agent.py#L2674) | 2674 | `""` | — |
| [SRC-F725E90B2A-L002675](../../tests/test_web_agent.py#L2675) | 2675 | `"    class FakeClient:"` | — |
| [SRC-F725E90B2A-L002676](../../tests/test_web_agent.py#L2676) | 2676 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-F725E90B2A-L002677](../../tests/test_web_agent.py#L2677) | 2677 | `"            self.options = kwargs"` | — |
| [SRC-F725E90B2A-L002678](../../tests/test_web_agent.py#L2678) | 2678 | `""` | — |
| [SRC-F725E90B2A-L002679](../../tests/test_web_agent.py#L2679) | 2679 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L002680](../../tests/test_web_agent.py#L2680) | 2680 | `"            return self"` | — |
| [SRC-F725E90B2A-L002681](../../tests/test_web_agent.py#L2681) | 2681 | `""` | — |
| [SRC-F725E90B2A-L002682](../../tests/test_web_agent.py#L2682) | 2682 | `"        def __exit__(self, *_args):"` | — |
| [SRC-F725E90B2A-L002683](../../tests/test_web_agent.py#L2683) | 2683 | `"            return False"` | — |
| [SRC-F725E90B2A-L002684](../../tests/test_web_agent.py#L2684) | 2684 | `""` | — |
| [SRC-F725E90B2A-L002685](../../tests/test_web_agent.py#L2685) | 2685 | `"        stream = fake_stream"` | — |
| [SRC-F725E90B2A-L002686](../../tests/test_web_agent.py#L2686) | 2686 | `""` | — |
| [SRC-F725E90B2A-L002687](../../tests/test_web_agent.py#L2687) | 2687 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-F725E90B2A-L002688](../../tests/test_web_agent.py#L2688) | 2688 | `""` | — |
| [SRC-F725E90B2A-L002689](../../tests/test_web_agent.py#L2689) | 2689 | `"    assert web_agent.WebAgent()._fetch_page(\"https://first.example/article\") == (\"\", \"\")"` | — |
| [SRC-F725E90B2A-L002690](../../tests/test_web_agent.py#L2690) | 2690 | `"    assert resolved_hosts == [\"first.example\"]"` | — |
| [SRC-F725E90B2A-L002691](../../tests/test_web_agent.py#L2691) | 2691 | `"    assert len(requests) == 1"` | — |
| [SRC-F725E90B2A-L002692](../../tests/test_web_agent.py#L2692) | 2692 | `"    assert requests[0][1] == \"https://93.184.216.34/article\""` | — |
| [SRC-F725E90B2A-L002693](../../tests/test_web_agent.py#L2693) | 2693 | `"    assert requests[0][2][\"headers\"][\"Host\"] == \"first.example\""` | — |
| [SRC-F725E90B2A-L002694](../../tests/test_web_agent.py#L2694) | 2694 | `"    assert requests[0][2][\"extensions\"][\"sni_hostname\"] == \"first.example\""` | — |
| [SRC-F725E90B2A-L002695](../../tests/test_web_agent.py#L2695) | 2695 | `""` | — |
| [SRC-F725E90B2A-L002696](../../tests/test_web_agent.py#L2696) | 2696 | `""` | — |
| [SRC-F725E90B2A-L002697](../../tests/test_web_agent.py#L2697) | 2697 | `"def test_fetch_page_revalidates_dns_for_each_redirect_destination(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002698](../../tests/test_web_agent.py#L2698) | 2698 | `"    from contextlib import contextmanager"` | — |
| [SRC-F725E90B2A-L002699](../../tests/test_web_agent.py#L2699) | 2699 | `""` | — |
| [SRC-F725E90B2A-L002700](../../tests/test_web_agent.py#L2700) | 2700 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002701](../../tests/test_web_agent.py#L2701) | 2701 | `""` | — |
| [SRC-F725E90B2A-L002702](../../tests/test_web_agent.py#L2702) | 2702 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L002703](../../tests/test_web_agent.py#L2703) | 2703 | `""` | — |
| [SRC-F725E90B2A-L002704](../../tests/test_web_agent.py#L2704) | 2704 | `"    resolved_hosts = []"` | — |
| [SRC-F725E90B2A-L002705](../../tests/test_web_agent.py#L2705) | 2705 | `"    requests = []"` | — |
| [SRC-F725E90B2A-L002706](../../tests/test_web_agent.py#L2706) | 2706 | `""` | — |
| [SRC-F725E90B2A-L002707](../../tests/test_web_agent.py#L2707) | 2707 | `"    def resolve_public_ip(host):"` | — |
| [SRC-F725E90B2A-L002708](../../tests/test_web_agent.py#L2708) | 2708 | `"        resolved_hosts.append(host)"` | — |
| [SRC-F725E90B2A-L002709](../../tests/test_web_agent.py#L2709) | 2709 | `"        if host == \"first.example\":"` | — |
| [SRC-F725E90B2A-L002710](../../tests/test_web_agent.py#L2710) | 2710 | `"            return [\"93.184.216.34\"]"` | — |
| [SRC-F725E90B2A-L002711](../../tests/test_web_agent.py#L2711) | 2711 | `"        # Model a redirect destination that resolves to no verified public IP."` | — |
| [SRC-F725E90B2A-L002712](../../tests/test_web_agent.py#L2712) | 2712 | `"        return None"` | — |
| [SRC-F725E90B2A-L002713](../../tests/test_web_agent.py#L2713) | 2713 | `""` | — |
| [SRC-F725E90B2A-L002714](../../tests/test_web_agent.py#L2714) | 2714 | `"    monkeypatch.setattr(web_agent, \"_public_ip_literals\", resolve_public_ip)"` | — |
| [SRC-F725E90B2A-L002715](../../tests/test_web_agent.py#L2715) | 2715 | `""` | — |
| [SRC-F725E90B2A-L002716](../../tests/test_web_agent.py#L2716) | 2716 | `"    class RedirectResponse:"` | — |
| [SRC-F725E90B2A-L002717](../../tests/test_web_agent.py#L2717) | 2717 | `"        status_code = 302"` | — |
| [SRC-F725E90B2A-L002718](../../tests/test_web_agent.py#L2718) | 2718 | `""` | — |
| [SRC-F725E90B2A-L002719](../../tests/test_web_agent.py#L2719) | 2719 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L002720](../../tests/test_web_agent.py#L2720) | 2720 | `"            self.headers = {\"location\": \"https://second.example/internal\"}"` | — |
| [SRC-F725E90B2A-L002721](../../tests/test_web_agent.py#L2721) | 2721 | `""` | — |
| [SRC-F725E90B2A-L002722](../../tests/test_web_agent.py#L2722) | 2722 | `"    @contextmanager"` | — |
| [SRC-F725E90B2A-L002723](../../tests/test_web_agent.py#L2723) | 2723 | `"    def fake_stream(self, method, url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002724](../../tests/test_web_agent.py#L2724) | 2724 | `"        requests.append((method, str(url), kwargs))"` | — |
| [SRC-F725E90B2A-L002725](../../tests/test_web_agent.py#L2725) | 2725 | `"        yield RedirectResponse()"` | — |
| [SRC-F725E90B2A-L002726](../../tests/test_web_agent.py#L2726) | 2726 | `""` | — |
| [SRC-F725E90B2A-L002727](../../tests/test_web_agent.py#L2727) | 2727 | `"    class FakeClient:"` | — |
| [SRC-F725E90B2A-L002728](../../tests/test_web_agent.py#L2728) | 2728 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-F725E90B2A-L002729](../../tests/test_web_agent.py#L2729) | 2729 | `"            self.options = kwargs"` | — |
| [SRC-F725E90B2A-L002730](../../tests/test_web_agent.py#L2730) | 2730 | `""` | — |
| [SRC-F725E90B2A-L002731](../../tests/test_web_agent.py#L2731) | 2731 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L002732](../../tests/test_web_agent.py#L2732) | 2732 | `"            return self"` | — |
| [SRC-F725E90B2A-L002733](../../tests/test_web_agent.py#L2733) | 2733 | `""` | — |
| [SRC-F725E90B2A-L002734](../../tests/test_web_agent.py#L2734) | 2734 | `"        def __exit__(self, *_args):"` | — |
| [SRC-F725E90B2A-L002735](../../tests/test_web_agent.py#L2735) | 2735 | `"            return False"` | — |
| [SRC-F725E90B2A-L002736](../../tests/test_web_agent.py#L2736) | 2736 | `""` | — |
| [SRC-F725E90B2A-L002737](../../tests/test_web_agent.py#L2737) | 2737 | `"        stream = fake_stream"` | — |
| [SRC-F725E90B2A-L002738](../../tests/test_web_agent.py#L2738) | 2738 | `""` | — |
| [SRC-F725E90B2A-L002739](../../tests/test_web_agent.py#L2739) | 2739 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-F725E90B2A-L002740](../../tests/test_web_agent.py#L2740) | 2740 | `""` | — |
| [SRC-F725E90B2A-L002741](../../tests/test_web_agent.py#L2741) | 2741 | `"    assert web_agent.WebAgent()._fetch_page(\"https://first.example/article\") == (\"\", \"\")"` | — |
| [SRC-F725E90B2A-L002742](../../tests/test_web_agent.py#L2742) | 2742 | `"    assert resolved_hosts == [\"first.example\", \"second.example\"]"` | — |
| [SRC-F725E90B2A-L002743](../../tests/test_web_agent.py#L2743) | 2743 | `"    # The second host is validated before any connection attempt to it."` | — |
| [SRC-F725E90B2A-L002744](../../tests/test_web_agent.py#L2744) | 2744 | `"    assert len(requests) == 1"` | — |
| [SRC-F725E90B2A-L002745](../../tests/test_web_agent.py#L2745) | 2745 | `""` | — |
| [SRC-F725E90B2A-L002746](../../tests/test_web_agent.py#L2746) | 2746 | `""` | — |
| [SRC-F725E90B2A-L002747](../../tests/test_web_agent.py#L2747) | 2747 | `""` | — |
| [SRC-F725E90B2A-L002748](../../tests/test_web_agent.py#L2748) | 2748 | `"def test_history_search_query_uses_shared_context_resolver():"` | — |
| [SRC-F725E90B2A-L002749](../../tests/test_web_agent.py#L2749) | 2749 | `"    history = ["` | — |
| [SRC-F725E90B2A-L002750](../../tests/test_web_agent.py#L2750) | 2750 | `"        {\"role\": \"user\", \"content\": \"سعر آيفون 16 في مصر\"},"` | — |
| [SRC-F725E90B2A-L002751](../../tests/test_web_agent.py#L2751) | 2751 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن السعر.\"},"` | — |
| [SRC-F725E90B2A-L002752](../../tests/test_web_agent.py#L2752) | 2752 | `"    ]"` | — |
| [SRC-F725E90B2A-L002753](../../tests/test_web_agent.py#L2753) | 2753 | `"    query = WebAgent._history_search_query(\"هل فيه ضمان؟\", history)"` | — |
| [SRC-F725E90B2A-L002754](../../tests/test_web_agent.py#L2754) | 2754 | `"    assert \"آيفون 16\" in query"` | — |
| [SRC-F725E90B2A-L002755](../../tests/test_web_agent.py#L2755) | 2755 | `"    assert \"ضمان\" in query"` | — |
| [SRC-F725E90B2A-L002756](../../tests/test_web_agent.py#L2756) | 2756 | `""` | — |
| [SRC-F725E90B2A-L002757](../../tests/test_web_agent.py#L2757) | 2757 | `""` | — |
| [SRC-F725E90B2A-L002758](../../tests/test_web_agent.py#L2758) | 2758 | `"def test_history_search_query_does_not_reuse_stale_topic_after_acknowledgment():"` | — |
| [SRC-F725E90B2A-L002759](../../tests/test_web_agent.py#L2759) | 2759 | `"    history = ["` | — |
| [SRC-F725E90B2A-L002760](../../tests/test_web_agent.py#L2760) | 2760 | `"        {\"role\": \"user\", \"content\": \"سعر آيفون 16 في مصر\"},"` | — |
| [SRC-F725E90B2A-L002761](../../tests/test_web_agent.py#L2761) | 2761 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن السعر.\"},"` | — |
| [SRC-F725E90B2A-L002762](../../tests/test_web_agent.py#L2762) | 2762 | `"        {\"role\": \"user\", \"content\": \"شكرا\"},"` | — |
| [SRC-F725E90B2A-L002763](../../tests/test_web_agent.py#L2763) | 2763 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-F725E90B2A-L002764](../../tests/test_web_agent.py#L2764) | 2764 | `"    ]"` | — |
| [SRC-F725E90B2A-L002765](../../tests/test_web_agent.py#L2765) | 2765 | `"    assert WebAgent._history_search_query(\"فين؟\", history) == \"فين؟\""` | — |
| [SRC-F725E90B2A-L002766](../../tests/test_web_agent.py#L2766) | 2766 | `""` | — |
| [SRC-F725E90B2A-L002767](../../tests/test_web_agent.py#L2767) | 2767 | `""` | — |
| [SRC-F725E90B2A-L002768](../../tests/test_web_agent.py#L2768) | 2768 | `"def test_frontend_exposes_structured_page_fetch_statuses():"` | — |
| [SRC-F725E90B2A-L002769](../../tests/test_web_agent.py#L2769) | 2769 | `"    html_path = Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\""` | — |
| [SRC-F725E90B2A-L002770](../../tests/test_web_agent.py#L2770) | 2770 | `"    html = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002771](../../tests/test_web_agent.py#L2771) | 2771 | `"    assert \"page_fetch_status\" in html"` | — |
| [SRC-F725E90B2A-L002772](../../tests/test_web_agent.py#L2772) | 2772 | `"    assert \"partial_extraction\" in html"` | — |
| [SRC-F725E90B2A-L002773](../../tests/test_web_agent.py#L2773) | 2773 | `"    assert \"لم يُستخرج نص؛ قد تكون الصفحة ديناميكية أو محجوبة\" in html"` | — |
| [SRC-F725E90B2A-L002774](../../tests/test_web_agent.py#L2774) | 2774 | `"    assert \"تشخيص الموصلات في هذا الطلب\" in html"` | — |
| [SRC-F725E90B2A-L002775](../../tests/test_web_agent.py#L2775) | 2775 | `"    assert \"حالة إكمال البحث\" in html"` | — |
| [SRC-F725E90B2A-L002776](../../tests/test_web_agent.py#L2776) | 2776 | `"    assert \"تفاصيل مراحل إكمال البحث والعدادات\" in html"` | — |
| [SRC-F725E90B2A-L002777](../../tests/test_web_agent.py#L2777) | 2777 | `"    assert \"pages_read_with_text_count\" in html"` | — |
| [SRC-F725E90B2A-L002778](../../tests/test_web_agent.py#L2778) | 2778 | `"    assert \"التحقق الدلالي من أن كل ادعاء مسنود فعلًا بالمصدر\" in html"` | — |
| [SRC-F725E90B2A-L002779](../../tests/test_web_agent.py#L2779) | 2779 | `""` | — |
| [SRC-F725E90B2A-L002780](../../tests/test_web_agent.py#L2780) | 2780 | `""` | — |
| [SRC-F725E90B2A-L002781](../../tests/test_web_agent.py#L2781) | 2781 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L002782](../../tests/test_web_agent.py#L2782) | 2782 | `"    \"method_name\","` | — |
| [SRC-F725E90B2A-L002783](../../tests/test_web_agent.py#L2783) | 2783 | `"    [\"_search_duckduckgo_html\", \"_search_bing_rss\", \"_search_news\"],"` | — |
| [SRC-F725E90B2A-L002784](../../tests/test_web_agent.py#L2784) | 2784 | `")"` | — |
| [SRC-F725E90B2A-L002785](../../tests/test_web_agent.py#L2785) | 2785 | `"def test_search_providers_do_not_follow_redirects_automatically("` | — |
| [SRC-F725E90B2A-L002786](../../tests/test_web_agent.py#L2786) | 2786 | `"    monkeypatch, method_name"` | — |
| [SRC-F725E90B2A-L002787](../../tests/test_web_agent.py#L2787) | 2787 | `"):"` | — |
| [SRC-F725E90B2A-L002788](../../tests/test_web_agent.py#L2788) | 2788 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002789](../../tests/test_web_agent.py#L2789) | 2789 | `""` | — |
| [SRC-F725E90B2A-L002790](../../tests/test_web_agent.py#L2790) | 2790 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002791](../../tests/test_web_agent.py#L2791) | 2791 | `"    observed = []"` | — |
| [SRC-F725E90B2A-L002792](../../tests/test_web_agent.py#L2792) | 2792 | `""` | — |
| [SRC-F725E90B2A-L002793](../../tests/test_web_agent.py#L2793) | 2793 | `"    class RedirectResponse:"` | — |
| [SRC-F725E90B2A-L002794](../../tests/test_web_agent.py#L2794) | 2794 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L002795](../../tests/test_web_agent.py#L2795) | 2795 | `"            self.status_code = 302"` | — |
| [SRC-F725E90B2A-L002796](../../tests/test_web_agent.py#L2796) | 2796 | `"            self.headers = {\"location\": \"http://127.0.0.1:8765/private\"}"` | — |
| [SRC-F725E90B2A-L002797](../../tests/test_web_agent.py#L2797) | 2797 | `"            self.text = \"redirect\""` | — |
| [SRC-F725E90B2A-L002798](../../tests/test_web_agent.py#L2798) | 2798 | `"            self.content = b\"redirect\""` | — |
| [SRC-F725E90B2A-L002799](../../tests/test_web_agent.py#L2799) | 2799 | `""` | — |
| [SRC-F725E90B2A-L002800](../../tests/test_web_agent.py#L2800) | 2800 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002801](../../tests/test_web_agent.py#L2801) | 2801 | `"        observed.append((url, kwargs.get(\"follow_redirects\")))"` | — |
| [SRC-F725E90B2A-L002802](../../tests/test_web_agent.py#L2802) | 2802 | `"        return RedirectResponse()"` | — |
| [SRC-F725E90B2A-L002803](../../tests/test_web_agent.py#L2803) | 2803 | `""` | — |
| [SRC-F725E90B2A-L002804](../../tests/test_web_agent.py#L2804) | 2804 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L002805](../../tests/test_web_agent.py#L2805) | 2805 | `"    method = getattr(agent, method_name)"` | — |
| [SRC-F725E90B2A-L002806](../../tests/test_web_agent.py#L2806) | 2806 | `"    with pytest.raises(RuntimeError, match=\"HTTP 302\"):"` | — |
| [SRC-F725E90B2A-L002807](../../tests/test_web_agent.py#L2807) | 2807 | `"        method(\"redirect regression test\")"` | — |
| [SRC-F725E90B2A-L002808](../../tests/test_web_agent.py#L2808) | 2808 | `""` | — |
| [SRC-F725E90B2A-L002809](../../tests/test_web_agent.py#L2809) | 2809 | `"    assert len(observed) == 1"` | — |
| [SRC-F725E90B2A-L002810](../../tests/test_web_agent.py#L2810) | 2810 | `"    assert observed[0][1] is False"` | — |
| [SRC-F725E90B2A-L002811](../../tests/test_web_agent.py#L2811) | 2811 | `""` | — |
| [SRC-F725E90B2A-L002812](../../tests/test_web_agent.py#L2812) | 2812 | `""` | — |
| [SRC-F725E90B2A-L002813](../../tests/test_web_agent.py#L2813) | 2813 | `""` | — |
| [SRC-F725E90B2A-L002814](../../tests/test_web_agent.py#L2814) | 2814 | `"@pytest.mark.parametrize(\"mode\", [\"deep\", \"latest\", \"social\"])"` | — |
| [SRC-F725E90B2A-L002815](../../tests/test_web_agent.py#L2815) | 2815 | `"def test_explicit_modes_survive_deterministic_planning(monkeypatch, mode):"` | — |
| [SRC-F725E90B2A-L002816](../../tests/test_web_agent.py#L2816) | 2816 | `"    \"\"\"A missing planner model must not erase a mode explicitly selected by the user.\"\"\""` | — |
| [SRC-F725E90B2A-L002817](../../tests/test_web_agent.py#L2817) | 2817 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002818](../../tests/test_web_agent.py#L2818) | 2818 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L002819](../../tests/test_web_agent.py#L2819) | 2819 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002820](../../tests/test_web_agent.py#L2820) | 2820 | `""` | — |
| [SRC-F725E90B2A-L002821](../../tests/test_web_agent.py#L2821) | 2821 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L002822](../../tests/test_web_agent.py#L2822) | 2822 | `"        seen[\"plan\"] = dict(research_plan)"` | — |
| [SRC-F725E90B2A-L002823](../../tests/test_web_agent.py#L2823) | 2823 | `"        sources = [sample_source(0), sample_source(1)]"` | — |
| [SRC-F725E90B2A-L002824](../../tests/test_web_agent.py#L2824) | 2824 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L002825](../../tests/test_web_agent.py#L2825) | 2825 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002826](../../tests/test_web_agent.py#L2826) | 2826 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002827](../../tests/test_web_agent.py#L2827) | 2827 | `"            \"query_results\": ["` | — |
| [SRC-F725E90B2A-L002828](../../tests/test_web_agent.py#L2828) | 2828 | `"                {\"query\": query, \"results\": 1}"` | — |
| [SRC-F725E90B2A-L002829](../../tests/test_web_agent.py#L2829) | 2829 | `"                for query in research_plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L002830](../../tests/test_web_agent.py#L2830) | 2830 | `"            ],"` | — |
| [SRC-F725E90B2A-L002831](../../tests/test_web_agent.py#L2831) | 2831 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-F725E90B2A-L002832](../../tests/test_web_agent.py#L2832) | 2832 | `"            \"pages_fetched\": len(sources),"` | — |
| [SRC-F725E90B2A-L002833](../../tests/test_web_agent.py#L2833) | 2833 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L002834](../../tests/test_web_agent.py#L2834) | 2834 | `"            \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-F725E90B2A-L002835](../../tests/test_web_agent.py#L2835) | 2835 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002836](../../tests/test_web_agent.py#L2836) | 2836 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L002837](../../tests/test_web_agent.py#L2837) | 2837 | `"            \"planning_method\": \"deterministic_fallback\","` | — |
| [SRC-F725E90B2A-L002838](../../tests/test_web_agent.py#L2838) | 2838 | `"        }"` | — |
| [SRC-F725E90B2A-L002839](../../tests/test_web_agent.py#L2839) | 2839 | `""` | — |
| [SRC-F725E90B2A-L002840](../../tests/test_web_agent.py#L2840) | 2840 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L002841](../../tests/test_web_agent.py#L2841) | 2841 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L002842](../../tests/test_web_agent.py#L2842) | 2842 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L002843](../../tests/test_web_agent.py#L2843) | 2843 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002844](../../tests/test_web_agent.py#L2844) | 2844 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002845](../../tests/test_web_agent.py#L2845) | 2845 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L002846](../../tests/test_web_agent.py#L2846) | 2846 | `"        lambda question, history, sources, search_warning, research_plan=None,"` | — |
| [SRC-F725E90B2A-L002847](../../tests/test_web_agent.py#L2847) | 2847 | `"               search_report=None: \"توجد نتائج أولية للمراجعة [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L002848](../../tests/test_web_agent.py#L2848) | 2848 | `"    )"` | — |
| [SRC-F725E90B2A-L002849](../../tests/test_web_agent.py#L2849) | 2849 | `""` | — |
| [SRC-F725E90B2A-L002850](../../tests/test_web_agent.py#L2850) | 2850 | `"    question = ("` | — |
| [SRC-F725E90B2A-L002851](../../tests/test_web_agent.py#L2851) | 2851 | `"        \"ابحث عن شقة في التجمع الخامس بسعر 5000000 جنيه\""` | — |
| [SRC-F725E90B2A-L002852](../../tests/test_web_agent.py#L2852) | 2852 | `"        if mode == \"deep\" else \"الطاقة المتجددة في مصر\""` | — |
| [SRC-F725E90B2A-L002853](../../tests/test_web_agent.py#L2853) | 2853 | `"    )"` | — |
| [SRC-F725E90B2A-L002854](../../tests/test_web_agent.py#L2854) | 2854 | `"    result = agent.answer(question, mode=mode)"` | — |
| [SRC-F725E90B2A-L002855](../../tests/test_web_agent.py#L2855) | 2855 | `"    plan = seen[\"plan\"]"` | — |
| [SRC-F725E90B2A-L002856](../../tests/test_web_agent.py#L2856) | 2856 | `""` | — |
| [SRC-F725E90B2A-L002857](../../tests/test_web_agent.py#L2857) | 2857 | `"    assert plan[\"mode\"] == mode"` | — |
| [SRC-F725E90B2A-L002858](../../tests/test_web_agent.py#L2858) | 2858 | `"    assert result[\"research_plan\"][\"mode\"] == mode"` | — |
| [SRC-F725E90B2A-L002859](../../tests/test_web_agent.py#L2859) | 2859 | `"    if mode == \"deep\":"` | — |
| [SRC-F725E90B2A-L002860](../../tests/test_web_agent.py#L2860) | 2860 | `"        assert plan[\"depth\"] == \"deep\""` | — |
| [SRC-F725E90B2A-L002861](../../tests/test_web_agent.py#L2861) | 2861 | `"        assert len(plan[\"queries\"]) >= 3"` | — |
| [SRC-F725E90B2A-L002862](../../tests/test_web_agent.py#L2862) | 2862 | `"        assert any(\"إعلانات عقارية\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002863](../../tests/test_web_agent.py#L2863) | 2863 | `"        assert any(\"متوسط أسعار السوق للمتر\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002864](../../tests/test_web_agent.py#L2864) | 2864 | `"    elif mode == \"latest\":"` | — |
| [SRC-F725E90B2A-L002865](../../tests/test_web_agent.py#L2865) | 2865 | `"        assert plan[\"freshness\"] == \"current\""` | — |
| [SRC-F725E90B2A-L002866](../../tests/test_web_agent.py#L2866) | 2866 | `"        assert any("` | — |
| [SRC-F725E90B2A-L002867](../../tests/test_web_agent.py#L2867) | 2867 | `"            \"latest\" in query.lower() or \"recent\" in query.lower()"` | — |
| [SRC-F725E90B2A-L002868](../../tests/test_web_agent.py#L2868) | 2868 | `"            for query in plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L002869](../../tests/test_web_agent.py#L2869) | 2869 | `"        )"` | — |
| [SRC-F725E90B2A-L002870](../../tests/test_web_agent.py#L2870) | 2870 | `"    else:"` | — |
| [SRC-F725E90B2A-L002871](../../tests/test_web_agent.py#L2871) | 2871 | `"        assert plan[\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L002872](../../tests/test_web_agent.py#L2872) | 2872 | `"        assert any(query.startswith(\"site:\") for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002873](../../tests/test_web_agent.py#L2873) | 2873 | `""` | — |
| [SRC-F725E90B2A-L002874](../../tests/test_web_agent.py#L2874) | 2874 | `""` | — |
| [SRC-F725E90B2A-L002875](../../tests/test_web_agent.py#L2875) | 2875 | `"def test_latest_mode_preserves_official_website_navigation_intent(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002876](../../tests/test_web_agent.py#L2876) | 2876 | `"    \"\"\"Latest mode must not replace an official-site lookup with generic news queries.\"\"\""` | — |
| [SRC-F725E90B2A-L002877](../../tests/test_web_agent.py#L2877) | 2877 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002878](../../tests/test_web_agent.py#L2878) | 2878 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L002879](../../tests/test_web_agent.py#L2879) | 2879 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002880](../../tests/test_web_agent.py#L2880) | 2880 | `""` | — |
| [SRC-F725E90B2A-L002881](../../tests/test_web_agent.py#L2881) | 2881 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L002882](../../tests/test_web_agent.py#L2882) | 2882 | `"        seen[\"plan\"] = dict(research_plan)"` | — |
| [SRC-F725E90B2A-L002883](../../tests/test_web_agent.py#L2883) | 2883 | `"        sources = [sample_source(0), sample_source(1)]"` | — |
| [SRC-F725E90B2A-L002884](../../tests/test_web_agent.py#L2884) | 2884 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L002885](../../tests/test_web_agent.py#L2885) | 2885 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002886](../../tests/test_web_agent.py#L2886) | 2886 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002887](../../tests/test_web_agent.py#L2887) | 2887 | `"            \"query_results\": ["` | — |
| [SRC-F725E90B2A-L002888](../../tests/test_web_agent.py#L2888) | 2888 | `"                {\"query\": query, \"results\": 1}"` | — |
| [SRC-F725E90B2A-L002889](../../tests/test_web_agent.py#L2889) | 2889 | `"                for query in research_plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L002890](../../tests/test_web_agent.py#L2890) | 2890 | `"            ],"` | — |
| [SRC-F725E90B2A-L002891](../../tests/test_web_agent.py#L2891) | 2891 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-F725E90B2A-L002892](../../tests/test_web_agent.py#L2892) | 2892 | `"            \"pages_fetched\": len(sources),"` | — |
| [SRC-F725E90B2A-L002893](../../tests/test_web_agent.py#L2893) | 2893 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L002894](../../tests/test_web_agent.py#L2894) | 2894 | `"            \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-F725E90B2A-L002895](../../tests/test_web_agent.py#L2895) | 2895 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002896](../../tests/test_web_agent.py#L2896) | 2896 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L002897](../../tests/test_web_agent.py#L2897) | 2897 | `"            \"planning_method\": \"deterministic_fallback\","` | — |
| [SRC-F725E90B2A-L002898](../../tests/test_web_agent.py#L2898) | 2898 | `"        }"` | — |
| [SRC-F725E90B2A-L002899](../../tests/test_web_agent.py#L2899) | 2899 | `""` | — |
| [SRC-F725E90B2A-L002900](../../tests/test_web_agent.py#L2900) | 2900 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L002901](../../tests/test_web_agent.py#L2901) | 2901 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L002902](../../tests/test_web_agent.py#L2902) | 2902 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L002903](../../tests/test_web_agent.py#L2903) | 2903 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002904](../../tests/test_web_agent.py#L2904) | 2904 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002905](../../tests/test_web_agent.py#L2905) | 2905 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L002906](../../tests/test_web_agent.py#L2906) | 2906 | `"        lambda question, history, sources, search_warning, research_plan=None,"` | — |
| [SRC-F725E90B2A-L002907](../../tests/test_web_agent.py#L2907) | 2907 | `"               search_report=None: \"وجدت مرشحًا للموقع الرسمي [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L002908](../../tests/test_web_agent.py#L2908) | 2908 | `"    )"` | — |
| [SRC-F725E90B2A-L002909](../../tests/test_web_agent.py#L2909) | 2909 | `""` | — |
| [SRC-F725E90B2A-L002910](../../tests/test_web_agent.py#L2910) | 2910 | `"    question = ("` | — |
| [SRC-F725E90B2A-L002911](../../tests/test_web_agent.py#L2911) | 2911 | `"        \"ابحث عن الموقع الرسمي لوزارة الاتصالات وتكنولوجيا المعلومات المصرية، \""` | — |
| [SRC-F725E90B2A-L002912](../../tests/test_web_agent.py#L2912) | 2912 | `"        \"واعرض رابط المصدر وتاريخ الصفحة إن توفر\""` | — |
| [SRC-F725E90B2A-L002913](../../tests/test_web_agent.py#L2913) | 2913 | `"    )"` | — |
| [SRC-F725E90B2A-L002914](../../tests/test_web_agent.py#L2914) | 2914 | `"    result = agent.answer(question, mode=\"latest\")"` | — |
| [SRC-F725E90B2A-L002915](../../tests/test_web_agent.py#L2915) | 2915 | `"    plan = seen[\"plan\"]"` | — |
| [SRC-F725E90B2A-L002916](../../tests/test_web_agent.py#L2916) | 2916 | `""` | — |
| [SRC-F725E90B2A-L002917](../../tests/test_web_agent.py#L2917) | 2917 | `"    assert plan[\"mode\"] == \"latest\""` | — |
| [SRC-F725E90B2A-L002918](../../tests/test_web_agent.py#L2918) | 2918 | `"    assert result[\"research_plan\"][\"mode\"] == \"latest\""` | — |
| [SRC-F725E90B2A-L002919](../../tests/test_web_agent.py#L2919) | 2919 | `"    assert any("` | — |
| [SRC-F725E90B2A-L002920](../../tests/test_web_agent.py#L2920) | 2920 | `"        \"الموقع الرسمي\" in query or \"official website\" in query.lower()"` | — |
| [SRC-F725E90B2A-L002921](../../tests/test_web_agent.py#L2921) | 2921 | `"        for query in plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L002922](../../tests/test_web_agent.py#L2922) | 2922 | `"    )"` | — |
| [SRC-F725E90B2A-L002923](../../tests/test_web_agent.py#L2923) | 2923 | `"    assert not any(\"latest news updates\" in query.lower() for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002924](../../tests/test_web_agent.py#L2924) | 2924 | `"    assert not any(\"recent official announcement\" in query.lower() for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002925](../../tests/test_web_agent.py#L2925) | 2925 | `""` | — |
| [SRC-F725E90B2A-L002926](../../tests/test_web_agent.py#L2926) | 2926 | `""` | — |
| [SRC-F725E90B2A-L002927](../../tests/test_web_agent.py#L2927) | 2927 | `"def test_web_answer_integrity_is_attached_without_live_network(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002928](../../tests/test_web_agent.py#L2928) | 2928 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002929](../../tests/test_web_agent.py#L2929) | 2929 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002930](../../tests/test_web_agent.py#L2930) | 2930 | `"        agent, \"_question_coverage_targets\", lambda question: [\"السعر\", \"المساحة\"]"` | — |
| [SRC-F725E90B2A-L002931](../../tests/test_web_agent.py#L2931) | 2931 | `"    )"` | — |
| [SRC-F725E90B2A-L002932](../../tests/test_web_agent.py#L2932) | 2932 | `"    monkeypatch.setattr(agent, \"_answer_with_budget\", lambda question, history, mode: {"` | — |
| [SRC-F725E90B2A-L002933](../../tests/test_web_agent.py#L2933) | 2933 | `"        \"kind\": \"web_research\","` | — |
| [SRC-F725E90B2A-L002934](../../tests/test_web_agent.py#L2934) | 2934 | `"        \"answer\": \"السعر 500 جنيه [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L002935](../../tests/test_web_agent.py#L2935) | 2935 | `"        \"sources\": [{"` | — |
| [SRC-F725E90B2A-L002936](../../tests/test_web_agent.py#L2936) | 2936 | `"            \"title\": \"تفاصيل العرض\","` | — |
| [SRC-F725E90B2A-L002937](../../tests/test_web_agent.py#L2937) | 2937 | `"            \"url\": \"https://example.com/offer\","` | — |
| [SRC-F725E90B2A-L002938](../../tests/test_web_agent.py#L2938) | 2938 | `"            \"snippet\": \"السعر 300 جنيه\","` | — |
| [SRC-F725E90B2A-L002939](../../tests/test_web_agent.py#L2939) | 2939 | `"            \"page_fetched\": False,"` | — |
| [SRC-F725E90B2A-L002940](../../tests/test_web_agent.py#L2940) | 2940 | `"        }],"` | — |
| [SRC-F725E90B2A-L002941](../../tests/test_web_agent.py#L2941) | 2941 | `"        \"research_quality\": \"partial\","` | — |
| [SRC-F725E90B2A-L002942](../../tests/test_web_agent.py#L2942) | 2942 | `"        \"search_report\": {\"pipeline_completion_status\": \"completed\"},"` | — |
| [SRC-F725E90B2A-L002943](../../tests/test_web_agent.py#L2943) | 2943 | `"        \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-F725E90B2A-L002944](../../tests/test_web_agent.py#L2944) | 2944 | `"        \"citation_validation\": {"` | — |
| [SRC-F725E90B2A-L002945](../../tests/test_web_agent.py#L2945) | 2945 | `"            \"status\": \"index_range_check_passed\","` | — |
| [SRC-F725E90B2A-L002946](../../tests/test_web_agent.py#L2946) | 2946 | `"            \"valid_citation_count\": 1,"` | — |
| [SRC-F725E90B2A-L002947](../../tests/test_web_agent.py#L2947) | 2947 | `"        },"` | — |
| [SRC-F725E90B2A-L002948](../../tests/test_web_agent.py#L2948) | 2948 | `"        \"final_answer_status\": \"model_answer_generated\","` | — |
| [SRC-F725E90B2A-L002949](../../tests/test_web_agent.py#L2949) | 2949 | `"        \"answer_coverage\": {},"` | — |
| [SRC-F725E90B2A-L002950](../../tests/test_web_agent.py#L2950) | 2950 | `"        \"used_language_model\": True,"` | — |
| [SRC-F725E90B2A-L002951](../../tests/test_web_agent.py#L2951) | 2951 | `"        \"used_web_search\": True,"` | — |
| [SRC-F725E90B2A-L002952](../../tests/test_web_agent.py#L2952) | 2952 | `"        \"warnings\": [],"` | — |
| [SRC-F725E90B2A-L002953](../../tests/test_web_agent.py#L2953) | 2953 | `"    })"` | — |
| [SRC-F725E90B2A-L002954](../../tests/test_web_agent.py#L2954) | 2954 | `""` | — |
| [SRC-F725E90B2A-L002955](../../tests/test_web_agent.py#L2955) | 2955 | `"    result = agent.answer(\"قارن السعر والمساحة\", mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L002956](../../tests/test_web_agent.py#L2956) | 2956 | `""` | — |
| [SRC-F725E90B2A-L002957](../../tests/test_web_agent.py#L2957) | 2957 | `"    assert result[\"answer_integrity\"][\"semantic_verification\"] is False"` | — |
| [SRC-F725E90B2A-L002958](../../tests/test_web_agent.py#L2958) | 2958 | `"    assert result[\"answer_integrity\"][\"independent_fact_check\"] is False"` | — |
| [SRC-F725E90B2A-L002959](../../tests/test_web_agent.py#L2959) | 2959 | `"    assert result[\"answer_integrity\"][\"potentially_unsupported_numeric_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002960](../../tests/test_web_agent.py#L2960) | 2960 | `"    assert result[\"answer_integrity\"][\"potentially_unsupported_numeric_by_citation_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002961](../../tests/test_web_agent.py#L2961) | 2961 | `"    assert result[\"answer_integrity\"][\"potentially_missing_target_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002962](../../tests/test_web_agent.py#L2962) | 2962 | `"    assert result[\"task_fulfillment_status\"] == \"possible_gap_detected\""` | — |
| [SRC-F725E90B2A-L002963](../../tests/test_web_agent.py#L2963) | 2963 | `"    assert result[\"research_completion\"][\"status\"] == \"partial_answer_evidence_gaps_detected\""` | — |
| [SRC-F725E90B2A-L002964](../../tests/test_web_agent.py#L2964) | 2964 | `"    assert result[\"pipeline_completion_status\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L002965](../../tests/test_web_agent.py#L2965) | 2965 | `"    assert result[\"search_report\"][\"pipeline_completion_status\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L002966](../../tests/test_web_agent.py#L2966) | 2966 | `"    assert result[\"answer_coverage\"][\"lexical_screen_method\"] == ("` | — |
| [SRC-F725E90B2A-L002967](../../tests/test_web_agent.py#L2967) | 2967 | `"        \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-F725E90B2A-L002968](../../tests/test_web_agent.py#L2968) | 2968 | `"    )"` | — |
| [SRC-F725E90B2A-L002969](../../tests/test_web_agent.py#L2969) | 2969 | `""` | — |
| [SRC-F725E90B2A-L002970](../../tests/test_web_agent.py#L2970) | 2970 | `""` | — |
| [SRC-F725E90B2A-L002971](../../tests/test_web_agent.py#L2971) | 2971 | `"def test_frontend_labels_answer_integrity_screen_as_non_semantic():"` | — |
| [SRC-F725E90B2A-L002972](../../tests/test_web_agent.py#L2972) | 2972 | `"    html = ("` | — |
| [SRC-F725E90B2A-L002973](../../tests/test_web_agent.py#L2973) | 2973 | `"        Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\""` | — |
| [SRC-F725E90B2A-L002974](../../tests/test_web_agent.py#L2974) | 2974 | `"    ).read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002975](../../tests/test_web_agent.py#L2975) | 2975 | `"    assert \"فحص لفظي أولي:\" in html"` | — |
| [SRC-F725E90B2A-L002976](../../tests/test_web_agent.py#L2976) | 2976 | `"    assert \"لا يثبت هذا الفحص صحة الوقائع أو دلالة الاستشهاد\" in html"` | — |
| [SRC-F725E90B2A-L002977](../../tests/test_web_agent.py#L2977) | 2977 | `"    assert \"potentially_unsupported_numeric_by_citation_count\" in html"` | — |
| [SRC-F725E90B2A-L002978](../../tests/test_web_agent.py#L2978) | 2978 | `"    assert \"potential_value_discrepancy_count\" in html"` | — |
| [SRC-F725E90B2A-L002979](../../tests/test_web_agent.py#L2979) | 2979 | `""` | — |
| [SRC-F725E90B2A-L002980](../../tests/test_web_agent.py#L2980) | 2980 | `""` | — |
| [SRC-F725E90B2A-L002981](../../tests/test_web_agent.py#L2981) | 2981 | `"def test_search_web_keeps_arabic_topic_matches_in_english_indexed_results(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002982](../../tests/test_web_agent.py#L2982) | 2982 | `"    cases = ["` | — |
| [SRC-F725E90B2A-L002983](../../tests/test_web_agent.py#L2983) | 2983 | `"        ("` | — |
| [SRC-F725E90B2A-L002984](../../tests/test_web_agent.py#L2984) | 2984 | `"            \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\","` | — |
| [SRC-F725E90B2A-L002985](../../tests/test_web_agent.py#L2985) | 2985 | `"            \"Egypt's capital is Cairo\","` | — |
| [SRC-F725E90B2A-L002986](../../tests/test_web_agent.py#L2986) | 2986 | `"            \"The capital city of Egypt is Cairo.\","` | — |
| [SRC-F725E90B2A-L002987](../../tests/test_web_agent.py#L2987) | 2987 | `"        ),"` | — |
| [SRC-F725E90B2A-L002988](../../tests/test_web_agent.py#L2988) | 2988 | `"        ("` | — |
| [SRC-F725E90B2A-L002989](../../tests/test_web_agent.py#L2989) | 2989 | `"            \"حلل أهم التحديات التي تواجه السيارات الكهربائية في مصر، وقارن بين التكلفة والبنية التحتية والشحن. استخدم مصادر متعددة، وميز بين الحقائق والاستنتاجات، واذكر روابط المصادر.\","` | — |
| [SRC-F725E90B2A-L002990](../../tests/test_web_agent.py#L2990) | 2990 | `"            \"Electric vehicles in Egypt: charging infrastructure and costs\","` | — |
| [SRC-F725E90B2A-L002991](../../tests/test_web_agent.py#L2991) | 2991 | `"            \"Electric cars face high costs and limited charging infrastructure in Egypt.\","` | — |
| [SRC-F725E90B2A-L002992](../../tests/test_web_agent.py#L2992) | 2992 | `"        ),"` | — |
| [SRC-F725E90B2A-L002993](../../tests/test_web_agent.py#L2993) | 2993 | `"        ("` | — |
| [SRC-F725E90B2A-L002994](../../tests/test_web_agent.py#L2994) | 2994 | `"            \"ما أحدث التطورات في وكلاء الذكاء الاصطناعي خلال الأيام السبعة الماضية؟ اذكر تواريخ الأخبار وروابط المصادر، ولا تعرض معلومات قديمة باعتبارها جديدة.\","` | — |
| [SRC-F725E90B2A-L002995](../../tests/test_web_agent.py#L2995) | 2995 | `"            \"Recent developments in AI agents\","` | — |
| [SRC-F725E90B2A-L002996](../../tests/test_web_agent.py#L2996) | 2996 | `"            \"New AI agent tools and launches this week.\","` | — |
| [SRC-F725E90B2A-L002997](../../tests/test_web_agent.py#L2997) | 2997 | `"        ),"` | — |
| [SRC-F725E90B2A-L002998](../../tests/test_web_agent.py#L2998) | 2998 | `"        ("` | — |
| [SRC-F725E90B2A-L002999](../../tests/test_web_agent.py#L2999) | 2999 | `"            \"اجمع آراء وتجارب المستخدمين العامة حول السيارات الكهربائية في مصر. اعرض الآراء الإيجابية والسلبية، واذكر روابط المنشورات أو المصادر المتاحة.\","` | — |
| [SRC-F725E90B2A-L003000](../../tests/test_web_agent.py#L3000) | 3000 | `"            \"Reddit users share electric car experiences in Egypt\","` | — |
| [SRC-F725E90B2A-L003001](../../tests/test_web_agent.py#L3001) | 3001 | `"            \"Owners discuss electric vehicles, charging and daily use.\","` | — |
| [SRC-F725E90B2A-L003002](../../tests/test_web_agent.py#L3002) | 3002 | `"        ),"` | — |
| [SRC-F725E90B2A-L003003](../../tests/test_web_agent.py#L3003) | 3003 | `"    ]"` | — |
| [SRC-F725E90B2A-L003004](../../tests/test_web_agent.py#L3004) | 3004 | `"    for index, (query, title, snippet) in enumerate(cases):"` | — |
| [SRC-F725E90B2A-L003005](../../tests/test_web_agent.py#L3005) | 3005 | `"        agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003006](../../tests/test_web_agent.py#L3006) | 3006 | `"        row = {"` | — |
| [SRC-F725E90B2A-L003007](../../tests/test_web_agent.py#L3007) | 3007 | `"            \"title\": title,"` | — |
| [SRC-F725E90B2A-L003008](../../tests/test_web_agent.py#L3008) | 3008 | `"            \"url\": f\"https://example.com/case-{index}\","` | — |
| [SRC-F725E90B2A-L003009](../../tests/test_web_agent.py#L3009) | 3009 | `"            \"snippet\": snippet,"` | — |
| [SRC-F725E90B2A-L003010](../../tests/test_web_agent.py#L3010) | 3010 | `"            \"provider\": \"fake_provider\","` | — |
| [SRC-F725E90B2A-L003011](../../tests/test_web_agent.py#L3011) | 3011 | `"            \"provider_rank\": 1,"` | — |
| [SRC-F725E90B2A-L003012](../../tests/test_web_agent.py#L3012) | 3012 | `"            \"search_query\": query,"` | — |
| [SRC-F725E90B2A-L003013](../../tests/test_web_agent.py#L3013) | 3013 | `"        }"` | — |
| [SRC-F725E90B2A-L003014](../../tests/test_web_agent.py#L3014) | 3014 | `"        monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _q, row=row: [dict(row)])"` | — |
| [SRC-F725E90B2A-L003015](../../tests/test_web_agent.py#L3015) | 3015 | `"        monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _q, row=row: [dict(row)])"` | — |
| [SRC-F725E90B2A-L003016](../../tests/test_web_agent.py#L3016) | 3016 | `"        # Current-news questions normally add Google News RSS; keep this unit test deterministic."` | — |
| [SRC-F725E90B2A-L003017](../../tests/test_web_agent.py#L3017) | 3017 | `"        monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L003018](../../tests/test_web_agent.py#L3018) | 3018 | `"        results = agent._search_web(query)"` | — |
| [SRC-F725E90B2A-L003019](../../tests/test_web_agent.py#L3019) | 3019 | `"        assert results, f\"Search candidates were all filtered for case {index}\""` | — |
| [SRC-F725E90B2A-L003020](../../tests/test_web_agent.py#L3020) | 3020 | `"        diagnostic = next("` | — |
| [SRC-F725E90B2A-L003021](../../tests/test_web_agent.py#L3021) | 3021 | `"            item for item in agent._provider_diagnostics if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L003022](../../tests/test_web_agent.py#L3022) | 3022 | `"        )"` | — |
| [SRC-F725E90B2A-L003023](../../tests/test_web_agent.py#L3023) | 3023 | `"        assert diagnostic[\"accepted_count\"] == 1"` | — |
| [SRC-F725E90B2A-L003024](../../tests/test_web_agent.py#L3024) | 3024 | `"        assert diagnostic[\"result_count\"] == 1"` | — |
| [SRC-F725E90B2A-L003025](../../tests/test_web_agent.py#L3025) | 3025 | `""` | — |
| [SRC-F725E90B2A-L003026](../../tests/test_web_agent.py#L3026) | 3026 | `""` | — |
| [SRC-F725E90B2A-L003027](../../tests/test_web_agent.py#L3027) | 3027 | `"def test_search_web_classifies_http_challenge_and_rate_limit_as_provider_degradation(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003028](../../tests/test_web_agent.py#L3028) | 3028 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003029](../../tests/test_web_agent.py#L3029) | 3029 | `""` | — |
| [SRC-F725E90B2A-L003030](../../tests/test_web_agent.py#L3030) | 3030 | `"    def http_202(_query):"` | — |
| [SRC-F725E90B2A-L003031](../../tests/test_web_agent.py#L3031) | 3031 | `"        raise RuntimeError(\"HTTP 202\")"` | — |
| [SRC-F725E90B2A-L003032](../../tests/test_web_agent.py#L3032) | 3032 | `""` | — |
| [SRC-F725E90B2A-L003033](../../tests/test_web_agent.py#L3033) | 3033 | `"    def http_429(_query):"` | — |
| [SRC-F725E90B2A-L003034](../../tests/test_web_agent.py#L3034) | 3034 | `"        raise RuntimeError(\"HTTP 429\")"` | — |
| [SRC-F725E90B2A-L003035](../../tests/test_web_agent.py#L3035) | 3035 | `""` | — |
| [SRC-F725E90B2A-L003036](../../tests/test_web_agent.py#L3036) | 3036 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", http_202)"` | — |
| [SRC-F725E90B2A-L003037](../../tests/test_web_agent.py#L3037) | 3037 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", http_429)"` | — |
| [SRC-F725E90B2A-L003038](../../tests/test_web_agent.py#L3038) | 3038 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L003039](../../tests/test_web_agent.py#L3039) | 3039 | `"        agent._search_web(\"renewable energy storage policy\")"` | — |
| [SRC-F725E90B2A-L003040](../../tests/test_web_agent.py#L3040) | 3040 | `""` | — |
| [SRC-F725E90B2A-L003041](../../tests/test_web_agent.py#L3041) | 3041 | `"    statuses = {"` | — |
| [SRC-F725E90B2A-L003042](../../tests/test_web_agent.py#L3042) | 3042 | `"        item[\"provider\"]: item[\"status\"]"` | — |
| [SRC-F725E90B2A-L003043](../../tests/test_web_agent.py#L3043) | 3043 | `"        for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L003044](../../tests/test_web_agent.py#L3044) | 3044 | `"        if item[\"provider\"] in {\"duckduckgo_html\", \"bing_rss\"}"` | — |
| [SRC-F725E90B2A-L003045](../../tests/test_web_agent.py#L3045) | 3045 | `"    }"` | — |
| [SRC-F725E90B2A-L003046](../../tests/test_web_agent.py#L3046) | 3046 | `"    assert statuses[\"duckduckgo_html\"] == \"http_error\""` | — |
| [SRC-F725E90B2A-L003047](../../tests/test_web_agent.py#L3047) | 3047 | `"    assert statuses[\"bing_rss\"] == \"rate_limited\""` | — |
| [SRC-F725E90B2A-L003048](../../tests/test_web_agent.py#L3048) | 3048 | `""` | — |
| [SRC-F725E90B2A-L003049](../../tests/test_web_agent.py#L3049) | 3049 | `""` | — |
| [SRC-F725E90B2A-L003050](../../tests/test_web_agent.py#L3050) | 3050 | `"def test_search_web_records_distinct_candidate_rejection_reasons(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003051](../../tests/test_web_agent.py#L3051) | 3051 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003052](../../tests/test_web_agent.py#L3052) | 3052 | `"    query = \"renewable energy storage\""` | — |
| [SRC-F725E90B2A-L003053](../../tests/test_web_agent.py#L3053) | 3053 | `"    candidates = ["` | — |
| [SRC-F725E90B2A-L003054](../../tests/test_web_agent.py#L3054) | 3054 | `"        \"malformed candidate\","` | — |
| [SRC-F725E90B2A-L003055](../../tests/test_web_agent.py#L3055) | 3055 | `"        {"` | — |
| [SRC-F725E90B2A-L003056](../../tests/test_web_agent.py#L3056) | 3056 | `"            \"title\": \"Unsafe scheme\","` | — |
| [SRC-F725E90B2A-L003057](../../tests/test_web_agent.py#L3057) | 3057 | `"            \"url\": \"javascript:alert(1)\","` | — |
| [SRC-F725E90B2A-L003058](../../tests/test_web_agent.py#L3058) | 3058 | `"            \"snippet\": \"Renewable energy storage report\","` | — |
| [SRC-F725E90B2A-L003059](../../tests/test_web_agent.py#L3059) | 3059 | `"        },"` | — |
| [SRC-F725E90B2A-L003060](../../tests/test_web_agent.py#L3060) | 3060 | `"        {"` | — |
| [SRC-F725E90B2A-L003061](../../tests/test_web_agent.py#L3061) | 3061 | `"            \"title\": \"Translated mirror\","` | — |
| [SRC-F725E90B2A-L003062](../../tests/test_web_agent.py#L3062) | 3062 | `"            \"url\": \"https://translate.google.com/translate?u=https%3A%2F%2Fexample.com\","` | — |
| [SRC-F725E90B2A-L003063](../../tests/test_web_agent.py#L3063) | 3063 | `"            \"snippet\": \"Renewable energy storage\","` | — |
| [SRC-F725E90B2A-L003064](../../tests/test_web_agent.py#L3064) | 3064 | `"        },"` | — |
| [SRC-F725E90B2A-L003065](../../tests/test_web_agent.py#L3065) | 3065 | `"        {"` | — |
| [SRC-F725E90B2A-L003066](../../tests/test_web_agent.py#L3066) | 3066 | `"            \"title\": \"Gardening tips\","` | — |
| [SRC-F725E90B2A-L003067](../../tests/test_web_agent.py#L3067) | 3067 | `"            \"url\": \"https://example.com/gardening\","` | — |
| [SRC-F725E90B2A-L003068](../../tests/test_web_agent.py#L3068) | 3068 | `"            \"snippet\": \"Gardening flowers and house plants\","` | — |
| [SRC-F725E90B2A-L003069](../../tests/test_web_agent.py#L3069) | 3069 | `"        },"` | — |
| [SRC-F725E90B2A-L003070](../../tests/test_web_agent.py#L3070) | 3070 | `"    ]"` | — |
| [SRC-F725E90B2A-L003071](../../tests/test_web_agent.py#L3071) | 3071 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _q: [dict(x) if isinstance(x, dict) else x for x in candidates])"` | — |
| [SRC-F725E90B2A-L003072](../../tests/test_web_agent.py#L3072) | 3072 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _q: [dict(x) if isinstance(x, dict) else x for x in candidates])"` | — |
| [SRC-F725E90B2A-L003073](../../tests/test_web_agent.py#L3073) | 3073 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L003074](../../tests/test_web_agent.py#L3074) | 3074 | `""` | — |
| [SRC-F725E90B2A-L003075](../../tests/test_web_agent.py#L3075) | 3075 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L003076](../../tests/test_web_agent.py#L3076) | 3076 | `"        agent._search_web(query)"` | — |
| [SRC-F725E90B2A-L003077](../../tests/test_web_agent.py#L3077) | 3077 | `""` | — |
| [SRC-F725E90B2A-L003078](../../tests/test_web_agent.py#L3078) | 3078 | `"    diagnostic = next("` | — |
| [SRC-F725E90B2A-L003079](../../tests/test_web_agent.py#L3079) | 3079 | `"        item for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L003080](../../tests/test_web_agent.py#L3080) | 3080 | `"        if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L003081](../../tests/test_web_agent.py#L3081) | 3081 | `"    )"` | — |
| [SRC-F725E90B2A-L003082](../../tests/test_web_agent.py#L3082) | 3082 | `"    assert diagnostic[\"status\"] == \"filtered_all\""` | — |
| [SRC-F725E90B2A-L003083](../../tests/test_web_agent.py#L3083) | 3083 | `"    assert diagnostic[\"result_count\"] == 4"` | — |
| [SRC-F725E90B2A-L003084](../../tests/test_web_agent.py#L3084) | 3084 | `"    assert diagnostic[\"accepted_count\"] == 0"` | — |
| [SRC-F725E90B2A-L003085](../../tests/test_web_agent.py#L3085) | 3085 | `"    assert diagnostic[\"rejected_count\"] == 4"` | — |
| [SRC-F725E90B2A-L003086](../../tests/test_web_agent.py#L3086) | 3086 | `"    assert diagnostic[\"rejection_counts\"] == {"` | — |
| [SRC-F725E90B2A-L003087](../../tests/test_web_agent.py#L3087) | 3087 | `"        \"malformed_candidate\": 1,"` | — |
| [SRC-F725E90B2A-L003088](../../tests/test_web_agent.py#L3088) | 3088 | `"        \"invalid_url_or_unsafe_target\": 1,"` | — |
| [SRC-F725E90B2A-L003089](../../tests/test_web_agent.py#L3089) | 3089 | `"        \"blocked_domain\": 1,"` | — |
| [SRC-F725E90B2A-L003090](../../tests/test_web_agent.py#L3090) | 3090 | `"        \"relevance_below_threshold\": 1,"` | — |
| [SRC-F725E90B2A-L003091](../../tests/test_web_agent.py#L3091) | 3091 | `"    }"` | — |
| [SRC-F725E90B2A-L003092](../../tests/test_web_agent.py#L3092) | 3092 | `"    assert sum(diagnostic[\"rejection_counts\"].values()) == diagnostic[\"rejected_count\"]"` | — |
| [SRC-F725E90B2A-L003093](../../tests/test_web_agent.py#L3093) | 3093 | `""` | — |
| [SRC-F725E90B2A-L003094](../../tests/test_web_agent.py#L3094) | 3094 | `""` | — |
| [SRC-F725E90B2A-L003095](../../tests/test_web_agent.py#L3095) | 3095 | `"def test_search_web_classifies_http_302_as_degraded_without_following_provider_redirect(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003096](../../tests/test_web_agent.py#L3096) | 3096 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003097](../../tests/test_web_agent.py#L3097) | 3097 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L003098](../../tests/test_web_agent.py#L3098) | 3098 | `""` | — |
| [SRC-F725E90B2A-L003099](../../tests/test_web_agent.py#L3099) | 3099 | `"    def redirect_response(query):"` | — |
| [SRC-F725E90B2A-L003100](../../tests/test_web_agent.py#L3100) | 3100 | `"        calls.append((\"duckduckgo_html\", query))"` | — |
| [SRC-F725E90B2A-L003101](../../tests/test_web_agent.py#L3101) | 3101 | `"        raise RuntimeError(\"HTTP 302\")"` | — |
| [SRC-F725E90B2A-L003102](../../tests/test_web_agent.py#L3102) | 3102 | `""` | — |
| [SRC-F725E90B2A-L003103](../../tests/test_web_agent.py#L3103) | 3103 | `"    def no_results(query):"` | — |
| [SRC-F725E90B2A-L003104](../../tests/test_web_agent.py#L3104) | 3104 | `"        calls.append((\"bing_rss\", query))"` | — |
| [SRC-F725E90B2A-L003105](../../tests/test_web_agent.py#L3105) | 3105 | `"        return []"` | — |
| [SRC-F725E90B2A-L003106](../../tests/test_web_agent.py#L3106) | 3106 | `""` | — |
| [SRC-F725E90B2A-L003107](../../tests/test_web_agent.py#L3107) | 3107 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", redirect_response)"` | — |
| [SRC-F725E90B2A-L003108](../../tests/test_web_agent.py#L3108) | 3108 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", no_results)"` | — |
| [SRC-F725E90B2A-L003109](../../tests/test_web_agent.py#L3109) | 3109 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L003110](../../tests/test_web_agent.py#L3110) | 3110 | `""` | — |
| [SRC-F725E90B2A-L003111](../../tests/test_web_agent.py#L3111) | 3111 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L003112](../../tests/test_web_agent.py#L3112) | 3112 | `"        agent._search_web(\"renewable energy storage\")"` | — |
| [SRC-F725E90B2A-L003113](../../tests/test_web_agent.py#L3113) | 3113 | `""` | — |
| [SRC-F725E90B2A-L003114](../../tests/test_web_agent.py#L3114) | 3114 | `"    diagnostic = next("` | — |
| [SRC-F725E90B2A-L003115](../../tests/test_web_agent.py#L3115) | 3115 | `"        item for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L003116](../../tests/test_web_agent.py#L3116) | 3116 | `"        if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L003117](../../tests/test_web_agent.py#L3117) | 3117 | `"    )"` | — |
| [SRC-F725E90B2A-L003118](../../tests/test_web_agent.py#L3118) | 3118 | `"    assert diagnostic[\"status\"] == \"http_error\""` | — |
| [SRC-F725E90B2A-L003119](../../tests/test_web_agent.py#L3119) | 3119 | `"    assert diagnostic[\"error\"] == \"RuntimeError: HTTP 302\""` | — |
| [SRC-F725E90B2A-L003120](../../tests/test_web_agent.py#L3120) | 3120 | `"    assert sum(provider == \"duckduckgo_html\" for provider, _query in calls) == 1"` | — |
| [SRC-F725E90B2A-L003121](../../tests/test_web_agent.py#L3121) | 3121 | `""` | — |
| [SRC-F725E90B2A-L003122](../../tests/test_web_agent.py#L3122) | 3122 | `""` | — |
| [SRC-F725E90B2A-L003123](../../tests/test_web_agent.py#L3123) | 3123 | `"def test_relevance_filter_compacts_prompt_and_rejects_instruction_only_queries():"` | — |
| [SRC-F725E90B2A-L003124](../../tests/test_web_agent.py#L3124) | 3124 | `"    question = \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003125](../../tests/test_web_agent.py#L3125) | 3125 | `"    assert _relevance_ratio(question, \"عاصمة مصر القاهرة\") >= 0.20"` | — |
| [SRC-F725E90B2A-L003126](../../tests/test_web_agent.py#L3126) | 3126 | `"    assert _relevance_ratio("` | — |
| [SRC-F725E90B2A-L003127](../../tests/test_web_agent.py#L3127) | 3127 | `"        \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\","` | — |
| [SRC-F725E90B2A-L003128](../../tests/test_web_agent.py#L3128) | 3128 | `"        \"Football results and unrelated match reports\","` | — |
| [SRC-F725E90B2A-L003129](../../tests/test_web_agent.py#L3129) | 3129 | `"    ) == 0.0"` | — |
| [SRC-F725E90B2A-L003130](../../tests/test_web_agent.py#L3130) | 3130 | `""` | — |
| [SRC-F725E90B2A-L003131](../../tests/test_web_agent.py#L3131) | 3131 | `""` | — |
| [SRC-F725E90B2A-L003132](../../tests/test_web_agent.py#L3132) | 3132 | `"def test_relevance_query_tokens_reject_site_only_and_modifier_only_queries():"` | — |
| [SRC-F725E90B2A-L003133](../../tests/test_web_agent.py#L3133) | 3133 | `"    assert _relevance_query_tokens(\"site:reddit.com\") == set()"` | — |
| [SRC-F725E90B2A-L003134](../../tests/test_web_agent.py#L3134) | 3134 | `"    assert _relevance_query_tokens(\"risks limitations alternatives\") == set()"` | — |
| [SRC-F725E90B2A-L003135](../../tests/test_web_agent.py#L3135) | 3135 | `"    assert _relevance_query_tokens(\"السيارات الكهربائية المستعملة في مصر\")"` | — |
| [SRC-F725E90B2A-L003136](../../tests/test_web_agent.py#L3136) | 3136 | `""` | — |
| [SRC-F725E90B2A-L003137](../../tests/test_web_agent.py#L3137) | 3137 | `""` | — |
| [SRC-F725E90B2A-L003138](../../tests/test_web_agent.py#L3138) | 3138 | `"def test_search_web_compacts_request_before_provider_dispatch(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003139](../../tests/test_web_agent.py#L3139) | 3139 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003140](../../tests/test_web_agent.py#L3140) | 3140 | `"    seen = []"` | — |
| [SRC-F725E90B2A-L003141](../../tests/test_web_agent.py#L3141) | 3141 | `""` | — |
| [SRC-F725E90B2A-L003142](../../tests/test_web_agent.py#L3142) | 3142 | `"    def capture(query):"` | — |
| [SRC-F725E90B2A-L003143](../../tests/test_web_agent.py#L3143) | 3143 | `"        seen.append(query)"` | — |
| [SRC-F725E90B2A-L003144](../../tests/test_web_agent.py#L3144) | 3144 | `"        return []"` | — |
| [SRC-F725E90B2A-L003145](../../tests/test_web_agent.py#L3145) | 3145 | `""` | — |
| [SRC-F725E90B2A-L003146](../../tests/test_web_agent.py#L3146) | 3146 | `"    for env_name in ("` | — |
| [SRC-F725E90B2A-L003147](../../tests/test_web_agent.py#L3147) | 3147 | `"        \"DEEPSEEK_SEARCH_API_KEY\","` | — |
| [SRC-F725E90B2A-L003148](../../tests/test_web_agent.py#L3148) | 3148 | `"        \"BRAVE_SEARCH_API_KEY\","` | — |
| [SRC-F725E90B2A-L003149](../../tests/test_web_agent.py#L3149) | 3149 | `"        \"TAVILY_API_KEY\","` | — |
| [SRC-F725E90B2A-L003150](../../tests/test_web_agent.py#L3150) | 3150 | `"    ):"` | — |
| [SRC-F725E90B2A-L003151](../../tests/test_web_agent.py#L3151) | 3151 | `"        monkeypatch.delenv(env_name, raising=False)"` | — |
| [SRC-F725E90B2A-L003152](../../tests/test_web_agent.py#L3152) | 3152 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", capture)"` | — |
| [SRC-F725E90B2A-L003153](../../tests/test_web_agent.py#L3153) | 3153 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", capture)"` | — |
| [SRC-F725E90B2A-L003154](../../tests/test_web_agent.py#L3154) | 3154 | `""` | — |
| [SRC-F725E90B2A-L003155](../../tests/test_web_agent.py#L3155) | 3155 | `"    raw_question = ("` | — |
| [SRC-F725E90B2A-L003156](../../tests/test_web_agent.py#L3156) | 3156 | `"        \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003157](../../tests/test_web_agent.py#L3157) | 3157 | `"    )"` | — |
| [SRC-F725E90B2A-L003158](../../tests/test_web_agent.py#L3158) | 3158 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L003159](../../tests/test_web_agent.py#L3159) | 3159 | `"        agent._search_web(raw_question)"` | — |
| [SRC-F725E90B2A-L003160](../../tests/test_web_agent.py#L3160) | 3160 | `""` | — |
| [SRC-F725E90B2A-L003161](../../tests/test_web_agent.py#L3161) | 3161 | `"    expected = _normalize_search_query(compact_search_query(raw_question))"` | — |
| [SRC-F725E90B2A-L003162](../../tests/test_web_agent.py#L3162) | 3162 | `"    assert seen"` | — |
| [SRC-F725E90B2A-L003163](../../tests/test_web_agent.py#L3163) | 3163 | `"    assert set(seen) == {expected}"` | — |
| [SRC-F725E90B2A-L003164](../../tests/test_web_agent.py#L3164) | 3164 | `"    assert len(expected) <= 240"` | — |
| [SRC-F725E90B2A-L003165](../../tests/test_web_agent.py#L3165) | 3165 | `"    assert \"رابط مباشر\" not in \" \".join(seen)"` | — |
| [SRC-F725E90B2A-L003166](../../tests/test_web_agent.py#L3166) | 3166 | `""` | — |
| [SRC-F725E90B2A-L003167](../../tests/test_web_agent.py#L3167) | 3167 | `""` | — |
| [SRC-F725E90B2A-L003168](../../tests/test_web_agent.py#L3168) | 3168 | `"def test_search_web_does_not_dispatch_instruction_only_query(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003169](../../tests/test_web_agent.py#L3169) | 3169 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003170](../../tests/test_web_agent.py#L3170) | 3170 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003171](../../tests/test_web_agent.py#L3171) | 3171 | `"        agent, \"_search_duckduckgo_html\","` | — |
| [SRC-F725E90B2A-L003172](../../tests/test_web_agent.py#L3172) | 3172 | `"        lambda query: pytest.fail(f\"provider should not receive {query!r}\"),"` | — |
| [SRC-F725E90B2A-L003173](../../tests/test_web_agent.py#L3173) | 3173 | `"    )"` | — |
| [SRC-F725E90B2A-L003174](../../tests/test_web_agent.py#L3174) | 3174 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003175](../../tests/test_web_agent.py#L3175) | 3175 | `"        agent, \"_search_bing_rss\","` | — |
| [SRC-F725E90B2A-L003176](../../tests/test_web_agent.py#L3176) | 3176 | `"        lambda query: pytest.fail(f\"provider should not receive {query!r}\"),"` | — |
| [SRC-F725E90B2A-L003177](../../tests/test_web_agent.py#L3177) | 3177 | `"    )"` | — |
| [SRC-F725E90B2A-L003178](../../tests/test_web_agent.py#L3178) | 3178 | `"    results = agent._search_web(\"اذكر مصادر موثوقة، روابط مباشرة، باختصار\")"` | — |
| [SRC-F725E90B2A-L003179](../../tests/test_web_agent.py#L3179) | 3179 | `"    assert results == []"` | — |
| [SRC-F725E90B2A-L003180](../../tests/test_web_agent.py#L3180) | 3180 | `""` | — |
| [SRC-F725E90B2A-L003181](../../tests/test_web_agent.py#L3181) | 3181 | `""` | — |
| [SRC-F725E90B2A-L003182](../../tests/test_web_agent.py#L3182) | 3182 | `"def test_plan_search_does_not_call_planner_without_a_topic(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003183](../../tests/test_web_agent.py#L3183) | 3183 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003184](../../tests/test_web_agent.py#L3184) | 3184 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003185](../../tests/test_web_agent.py#L3185) | 3185 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003186](../../tests/test_web_agent.py#L3186) | 3186 | `"        agent, \"_request_completion\","` | — |
| [SRC-F725E90B2A-L003187](../../tests/test_web_agent.py#L3187) | 3187 | `"        lambda *args, **kwargs: pytest.fail(\"planner should not run without a topic\"),"` | — |
| [SRC-F725E90B2A-L003188](../../tests/test_web_agent.py#L3188) | 3188 | `"    )"` | — |
| [SRC-F725E90B2A-L003189](../../tests/test_web_agent.py#L3189) | 3189 | `"    plan = agent._plan_search("` | — |
| [SRC-F725E90B2A-L003190](../../tests/test_web_agent.py#L3190) | 3190 | `"        \"استخدم مصادر متعددة، واذكر روابط المصادر\","` | — |
| [SRC-F725E90B2A-L003191](../../tests/test_web_agent.py#L3191) | 3191 | `"        [],"` | — |
| [SRC-F725E90B2A-L003192](../../tests/test_web_agent.py#L3192) | 3192 | `"    )"` | — |
| [SRC-F725E90B2A-L003193](../../tests/test_web_agent.py#L3193) | 3193 | `"    assert plan[\"queries\"] == []"` | — |
| [SRC-F725E90B2A-L003194](../../tests/test_web_agent.py#L3194) | 3194 | `""` | — |
| [SRC-F725E90B2A-L003195](../../tests/test_web_agent.py#L3195) | 3195 | `""` | — |
| [SRC-F725E90B2A-L003196](../../tests/test_web_agent.py#L3196) | 3196 | `"def test_plan_search_compacts_followup_query_before_fallback(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003197](../../tests/test_web_agent.py#L3197) | 3197 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003198](../../tests/test_web_agent.py#L3198) | 3198 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L003199](../../tests/test_web_agent.py#L3199) | 3199 | `"    history = ["` | — |
| [SRC-F725E90B2A-L003200](../../tests/test_web_agent.py#L3200) | 3200 | `"        {"` | — |
| [SRC-F725E90B2A-L003201](../../tests/test_web_agent.py#L3201) | 3201 | `"            \"role\": \"user\","` | — |
| [SRC-F725E90B2A-L003202](../../tests/test_web_agent.py#L3202) | 3202 | `"            \"content\": ("` | — |
| [SRC-F725E90B2A-L003203](../../tests/test_web_agent.py#L3203) | 3203 | `"                \"قارن السيارات الكهربائية في مصر. استخدم مصادر متعددة، \""` | — |
| [SRC-F725E90B2A-L003204](../../tests/test_web_agent.py#L3204) | 3204 | `"                \"واذكر روابط المصادر وأجب بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003205](../../tests/test_web_agent.py#L3205) | 3205 | `"            ),"` | — |
| [SRC-F725E90B2A-L003206](../../tests/test_web_agent.py#L3206) | 3206 | `"        },"` | — |
| [SRC-F725E90B2A-L003207](../../tests/test_web_agent.py#L3207) | 3207 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن مقارنة موثقة.\"},"` | — |
| [SRC-F725E90B2A-L003208](../../tests/test_web_agent.py#L3208) | 3208 | `"    ]"` | — |
| [SRC-F725E90B2A-L003209](../../tests/test_web_agent.py#L3209) | 3209 | `"    plan = agent._plan_search(\"وطب الأسعار الحالية؟\", history)"` | — |
| [SRC-F725E90B2A-L003210](../../tests/test_web_agent.py#L3210) | 3210 | `""` | — |
| [SRC-F725E90B2A-L003211](../../tests/test_web_agent.py#L3211) | 3211 | `"    assert plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L003212](../../tests/test_web_agent.py#L3212) | 3212 | `"    assert all(len(query) <= 240 for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L003213](../../tests/test_web_agent.py#L3213) | 3213 | `"    assert any(\"السيارات الكهربائية\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L003214](../../tests/test_web_agent.py#L3214) | 3214 | `"    assert all("` | — |
| [SRC-F725E90B2A-L003215](../../tests/test_web_agent.py#L3215) | 3215 | `"        \"روابط المصادر\" not in query and \"أجب بإيجاز\" not in query"` | — |
| [SRC-F725E90B2A-L003216](../../tests/test_web_agent.py#L3216) | 3216 | `"        for query in plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L003217](../../tests/test_web_agent.py#L3217) | 3217 | `"    )"` | — |
| [SRC-F725E90B2A-L003218](../../tests/test_web_agent.py#L3218) | 3218 | `""` | — |
| [SRC-F725E90B2A-L003219](../../tests/test_web_agent.py#L3219) | 3219 | `""` | — |
| [SRC-F725E90B2A-L003220](../../tests/test_web_agent.py#L3220) | 3220 | `"@pytest.mark.parametrize(\"fallback_queries\", [[], None])"` | — |
| [SRC-F725E90B2A-L003221](../../tests/test_web_agent.py#L3221) | 3221 | `"def test_auto_mode_does_not_reinsert_raw_question_when_fallback_has_no_query("` | — |
| [SRC-F725E90B2A-L003222](../../tests/test_web_agent.py#L3222) | 3222 | `"    monkeypatch, fallback_queries"` | — |
| [SRC-F725E90B2A-L003223](../../tests/test_web_agent.py#L3223) | 3223 | `"):"` | — |
| [SRC-F725E90B2A-L003224](../../tests/test_web_agent.py#L3224) | 3224 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003225](../../tests/test_web_agent.py#L3225) | 3225 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003226](../../tests/test_web_agent.py#L3226) | 3226 | `"    question = ("` | — |
| [SRC-F725E90B2A-L003227](../../tests/test_web_agent.py#L3227) | 3227 | `"        \"ما عيوب السيارات الكهربائية المستعملة في مصر؟ \""` | — |
| [SRC-F725E90B2A-L003228](../../tests/test_web_agent.py#L3228) | 3228 | `"        \"اذكر مصادر موثوقة وروابط مباشرة وأجب بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003229](../../tests/test_web_agent.py#L3229) | 3229 | `"    )"` | — |
| [SRC-F725E90B2A-L003230](../../tests/test_web_agent.py#L3230) | 3230 | `"    observed_plans = []"` | — |
| [SRC-F725E90B2A-L003231](../../tests/test_web_agent.py#L3231) | 3231 | `""` | — |
| [SRC-F725E90B2A-L003232](../../tests/test_web_agent.py#L3232) | 3232 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003233](../../tests/test_web_agent.py#L3233) | 3233 | `"        \"agents.web_agent.route_intent\","` | — |
| [SRC-F725E90B2A-L003234](../../tests/test_web_agent.py#L3234) | 3234 | `"        lambda *args, **kwargs: {\"route\": \"WEB_SIMPLE\", \"reason\": \"test\"},"` | — |
| [SRC-F725E90B2A-L003235](../../tests/test_web_agent.py#L3235) | 3235 | `"    )"` | — |
| [SRC-F725E90B2A-L003236](../../tests/test_web_agent.py#L3236) | 3236 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003237](../../tests/test_web_agent.py#L3237) | 3237 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003238](../../tests/test_web_agent.py#L3238) | 3238 | `"        lambda _question, _history: {"` | — |
| [SRC-F725E90B2A-L003239](../../tests/test_web_agent.py#L3239) | 3239 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L003240](../../tests/test_web_agent.py#L3240) | 3240 | `"            \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003241](../../tests/test_web_agent.py#L3241) | 3241 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003242](../../tests/test_web_agent.py#L3242) | 3242 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003243](../../tests/test_web_agent.py#L3243) | 3243 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003244](../../tests/test_web_agent.py#L3244) | 3244 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003245](../../tests/test_web_agent.py#L3245) | 3245 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003246](../../tests/test_web_agent.py#L3246) | 3246 | `"        },"` | — |
| [SRC-F725E90B2A-L003247](../../tests/test_web_agent.py#L3247) | 3247 | `"    )"` | — |
| [SRC-F725E90B2A-L003248](../../tests/test_web_agent.py#L3248) | 3248 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003249](../../tests/test_web_agent.py#L3249) | 3249 | `"        \"agents.web_agent.fallback_plan\","` | — |
| [SRC-F725E90B2A-L003250](../../tests/test_web_agent.py#L3250) | 3250 | `"        lambda *args, **kwargs: {\"queries\": fallback_queries},"` | — |
| [SRC-F725E90B2A-L003251](../../tests/test_web_agent.py#L3251) | 3251 | `"    )"` | — |
| [SRC-F725E90B2A-L003252](../../tests/test_web_agent.py#L3252) | 3252 | `""` | — |
| [SRC-F725E90B2A-L003253](../../tests/test_web_agent.py#L3253) | 3253 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003254](../../tests/test_web_agent.py#L3254) | 3254 | `"        observed_plans.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003255](../../tests/test_web_agent.py#L3255) | 3255 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L003256](../../tests/test_web_agent.py#L3256) | 3256 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003257](../../tests/test_web_agent.py#L3257) | 3257 | `"            \"queries_attempted\": 0,"` | — |
| [SRC-F725E90B2A-L003258](../../tests/test_web_agent.py#L3258) | 3258 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003259](../../tests/test_web_agent.py#L3259) | 3259 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L003260](../../tests/test_web_agent.py#L3260) | 3260 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L003261](../../tests/test_web_agent.py#L3261) | 3261 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L003262](../../tests/test_web_agent.py#L3262) | 3262 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003263](../../tests/test_web_agent.py#L3263) | 3263 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003264](../../tests/test_web_agent.py#L3264) | 3264 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L003265](../../tests/test_web_agent.py#L3265) | 3265 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003266](../../tests/test_web_agent.py#L3266) | 3266 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003267](../../tests/test_web_agent.py#L3267) | 3267 | `"        }"` | — |
| [SRC-F725E90B2A-L003268](../../tests/test_web_agent.py#L3268) | 3268 | `""` | — |
| [SRC-F725E90B2A-L003269](../../tests/test_web_agent.py#L3269) | 3269 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003270](../../tests/test_web_agent.py#L3270) | 3270 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"لا تتوفر مصادر كافية.\")"` | — |
| [SRC-F725E90B2A-L003271](../../tests/test_web_agent.py#L3271) | 3271 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-F725E90B2A-L003272](../../tests/test_web_agent.py#L3272) | 3272 | `""` | — |
| [SRC-F725E90B2A-L003273](../../tests/test_web_agent.py#L3273) | 3273 | `"    agent.answer(question, mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L003274](../../tests/test_web_agent.py#L3274) | 3274 | `""` | — |
| [SRC-F725E90B2A-L003275](../../tests/test_web_agent.py#L3275) | 3275 | `"    assert observed_plans"` | — |
| [SRC-F725E90B2A-L003276](../../tests/test_web_agent.py#L3276) | 3276 | `"    assert question not in observed_plans[0][\"queries\"]"` | — |
| [SRC-F725E90B2A-L003277](../../tests/test_web_agent.py#L3277) | 3277 | `"    assert observed_plans[0][\"queries\"]"` | — |
| [SRC-F725E90B2A-L003278](../../tests/test_web_agent.py#L3278) | 3278 | `"    assert observed_plans[0][\"queries\"][0] == compact_search_query(question)"` | — |
| [SRC-F725E90B2A-L003279](../../tests/test_web_agent.py#L3279) | 3279 | `""` | — |
| [SRC-F725E90B2A-L003280](../../tests/test_web_agent.py#L3280) | 3280 | `""` | — |
| [SRC-F725E90B2A-L003281](../../tests/test_web_agent.py#L3281) | 3281 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L003282](../../tests/test_web_agent.py#L3282) | 3282 | `"    (\"question\", \"planned_query\"),"` | — |
| [SRC-F725E90B2A-L003283](../../tests/test_web_agent.py#L3283) | 3283 | `"    ["` | — |
| [SRC-F725E90B2A-L003284](../../tests/test_web_agent.py#L3284) | 3284 | `"        ("` | — |
| [SRC-F725E90B2A-L003285](../../tests/test_web_agent.py#L3285) | 3285 | `"            ("` | — |
| [SRC-F725E90B2A-L003286](../../tests/test_web_agent.py#L3286) | 3286 | `"                \"ما عيوب السيارات الكهربائية المستعملة في مصر؟ \""` | — |
| [SRC-F725E90B2A-L003287](../../tests/test_web_agent.py#L3287) | 3287 | `"                \"اذكر مصادر موثوقة وروابط مباشرة وأجب بإيجاز.\""` | — |
| [SRC-F725E90B2A-L003288](../../tests/test_web_agent.py#L3288) | 3288 | `"            ),"` | — |
| [SRC-F725E90B2A-L003289](../../tests/test_web_agent.py#L3289) | 3289 | `"            None,"` | — |
| [SRC-F725E90B2A-L003290](../../tests/test_web_agent.py#L3290) | 3290 | `"        ),"` | — |
| [SRC-F725E90B2A-L003291](../../tests/test_web_agent.py#L3291) | 3291 | `"        ("` | — |
| [SRC-F725E90B2A-L003292](../../tests/test_web_agent.py#L3292) | 3292 | `"            \"كام سعرها؟ اذكر مصادر موثوقة وروابط مباشرة وأجب بإيجاز.\","` | — |
| [SRC-F725E90B2A-L003293](../../tests/test_web_agent.py#L3293) | 3293 | `"            \"أسعار السيارات الكهربائية المستعملة في مصر\","` | — |
| [SRC-F725E90B2A-L003294](../../tests/test_web_agent.py#L3294) | 3294 | `"        ),"` | — |
| [SRC-F725E90B2A-L003295](../../tests/test_web_agent.py#L3295) | 3295 | `"    ],"` | — |
| [SRC-F725E90B2A-L003296](../../tests/test_web_agent.py#L3296) | 3296 | `")"` | — |
| [SRC-F725E90B2A-L003297](../../tests/test_web_agent.py#L3297) | 3297 | `"def test_server_search_sources_use_compact_question_and_topic_plan("` | — |
| [SRC-F725E90B2A-L003298](../../tests/test_web_agent.py#L3298) | 3298 | `"    monkeypatch, question, planned_query"` | — |
| [SRC-F725E90B2A-L003299](../../tests/test_web_agent.py#L3299) | 3299 | `"):"` | — |
| [SRC-F725E90B2A-L003300](../../tests/test_web_agent.py#L3300) | 3300 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003301](../../tests/test_web_agent.py#L3301) | 3301 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003302](../../tests/test_web_agent.py#L3302) | 3302 | `"    topic_query = planned_query or compact_search_query(question)"` | — |
| [SRC-F725E90B2A-L003303](../../tests/test_web_agent.py#L3303) | 3303 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L003304](../../tests/test_web_agent.py#L3304) | 3304 | `"        \"queries\": [topic_query],"` | — |
| [SRC-F725E90B2A-L003305](../../tests/test_web_agent.py#L3305) | 3305 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L003306](../../tests/test_web_agent.py#L3306) | 3306 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003307](../../tests/test_web_agent.py#L3307) | 3307 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003308](../../tests/test_web_agent.py#L3308) | 3308 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003309](../../tests/test_web_agent.py#L3309) | 3309 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003310](../../tests/test_web_agent.py#L3310) | 3310 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003311](../../tests/test_web_agent.py#L3311) | 3311 | `"    }"` | — |
| [SRC-F725E90B2A-L003312](../../tests/test_web_agent.py#L3312) | 3312 | `"    source_queries = []"` | — |
| [SRC-F725E90B2A-L003313](../../tests/test_web_agent.py#L3313) | 3313 | `""` | — |
| [SRC-F725E90B2A-L003314](../../tests/test_web_agent.py#L3314) | 3314 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda _question, _history: dict(plan))"` | — |
| [SRC-F725E90B2A-L003315](../../tests/test_web_agent.py#L3315) | 3315 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003316](../../tests/test_web_agent.py#L3316) | 3316 | `"        agent, \"_collect_research\","` | — |
| [SRC-F725E90B2A-L003317](../../tests/test_web_agent.py#L3317) | 3317 | `"        lambda research_plan: ([sample_source(0), sample_source(1)], [], {"` | — |
| [SRC-F725E90B2A-L003318](../../tests/test_web_agent.py#L3318) | 3318 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L003319](../../tests/test_web_agent.py#L3319) | 3319 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L003320](../../tests/test_web_agent.py#L3320) | 3320 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003321](../../tests/test_web_agent.py#L3321) | 3321 | `"            \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L003322](../../tests/test_web_agent.py#L3322) | 3322 | `"            \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L003323](../../tests/test_web_agent.py#L3323) | 3323 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L003324](../../tests/test_web_agent.py#L3324) | 3324 | `"            \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-F725E90B2A-L003325](../../tests/test_web_agent.py#L3325) | 3325 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003326](../../tests/test_web_agent.py#L3326) | 3326 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L003327](../../tests/test_web_agent.py#L3327) | 3327 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003328](../../tests/test_web_agent.py#L3328) | 3328 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003329](../../tests/test_web_agent.py#L3329) | 3329 | `"        }),"` | — |
| [SRC-F725E90B2A-L003330](../../tests/test_web_agent.py#L3330) | 3330 | `"    )"` | — |
| [SRC-F725E90B2A-L003331](../../tests/test_web_agent.py#L3331) | 3331 | `""` | — |
| [SRC-F725E90B2A-L003332](../../tests/test_web_agent.py#L3332) | 3332 | `"    def generate(*args, **kwargs):"` | — |
| [SRC-F725E90B2A-L003333](../../tests/test_web_agent.py#L3333) | 3333 | `"        agent.server_search_sources = [{"` | — |
| [SRC-F725E90B2A-L003334](../../tests/test_web_agent.py#L3334) | 3334 | `"            \"title\": \"تجارب السيارات الكهربائية المستعملة\","` | — |
| [SRC-F725E90B2A-L003335](../../tests/test_web_agent.py#L3335) | 3335 | `"            \"url\": \"https://example.org/ev-used-cars\","` | — |
| [SRC-F725E90B2A-L003336](../../tests/test_web_agent.py#L3336) | 3336 | `"            \"snippet\": \"تكلفة البطارية والمدى الفعلي للسيارات الكهربائية المستعملة في مصر\","` | — |
| [SRC-F725E90B2A-L003337](../../tests/test_web_agent.py#L3337) | 3337 | `"            \"page_text\": \"تكلفة البطارية والمدى الفعلي للسيارات الكهربائية المستعملة في مصر\","` | — |
| [SRC-F725E90B2A-L003338](../../tests/test_web_agent.py#L3338) | 3338 | `"            \"page_fetched\": False,"` | — |
| [SRC-F725E90B2A-L003339](../../tests/test_web_agent.py#L3339) | 3339 | `"            \"provider\": \"openrouter_web_search\","` | — |
| [SRC-F725E90B2A-L003340](../../tests/test_web_agent.py#L3340) | 3340 | `"            \"providers\": [\"openrouter_web_search\"],"` | — |
| [SRC-F725E90B2A-L003341](../../tests/test_web_agent.py#L3341) | 3341 | `"            \"queries\": [],"` | — |
| [SRC-F725E90B2A-L003342](../../tests/test_web_agent.py#L3342) | 3342 | `"            \"domain\": \"example.org\","` | — |
| [SRC-F725E90B2A-L003343](../../tests/test_web_agent.py#L3343) | 3343 | `"            \"source_class\": \"general\","` | — |
| [SRC-F725E90B2A-L003344](../../tests/test_web_agent.py#L3344) | 3344 | `"            \"platform\": \"web\","` | — |
| [SRC-F725E90B2A-L003345](../../tests/test_web_agent.py#L3345) | 3345 | `"            \"published_at\": \"\","` | — |
| [SRC-F725E90B2A-L003346](../../tests/test_web_agent.py#L3346) | 3346 | `"        }]"` | — |
| [SRC-F725E90B2A-L003347](../../tests/test_web_agent.py#L3347) | 3347 | `"        return \"إجابة مبدئية [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L003348](../../tests/test_web_agent.py#L3348) | 3348 | `""` | — |
| [SRC-F725E90B2A-L003349](../../tests/test_web_agent.py#L3349) | 3349 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-F725E90B2A-L003350](../../tests/test_web_agent.py#L3350) | 3350 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda _question, answer, _sources: answer)"` | — |
| [SRC-F725E90B2A-L003351](../../tests/test_web_agent.py#L3351) | 3351 | `""` | — |
| [SRC-F725E90B2A-L003352](../../tests/test_web_agent.py#L3352) | 3352 | `"    def capture_relevance(query, text):"` | — |
| [SRC-F725E90B2A-L003353](../../tests/test_web_agent.py#L3353) | 3353 | `"        if \"تجارب السيارات الكهربائية المستعملة\" in text:"` | — |
| [SRC-F725E90B2A-L003354](../../tests/test_web_agent.py#L3354) | 3354 | `"            source_queries.append(query)"` | — |
| [SRC-F725E90B2A-L003355](../../tests/test_web_agent.py#L3355) | 3355 | `"            if planned_query and query != compact_search_query(topic_query):"` | — |
| [SRC-F725E90B2A-L003356](../../tests/test_web_agent.py#L3356) | 3356 | `"                return 0.0"` | — |
| [SRC-F725E90B2A-L003357](../../tests/test_web_agent.py#L3357) | 3357 | `"        return 0.25"` | — |
| [SRC-F725E90B2A-L003358](../../tests/test_web_agent.py#L3358) | 3358 | `""` | — |
| [SRC-F725E90B2A-L003359](../../tests/test_web_agent.py#L3359) | 3359 | `"    monkeypatch.setattr(\"agents.web_agent._relevance_ratio\", capture_relevance)"` | — |
| [SRC-F725E90B2A-L003360](../../tests/test_web_agent.py#L3360) | 3360 | `""` | — |
| [SRC-F725E90B2A-L003361](../../tests/test_web_agent.py#L3361) | 3361 | `"    agent.answer(question)"` | — |
| [SRC-F725E90B2A-L003362](../../tests/test_web_agent.py#L3362) | 3362 | `""` | — |
| [SRC-F725E90B2A-L003363](../../tests/test_web_agent.py#L3363) | 3363 | `"    expected_queries = list(dict.fromkeys("` | — |
| [SRC-F725E90B2A-L003364](../../tests/test_web_agent.py#L3364) | 3364 | `"        query for query in ("` | — |
| [SRC-F725E90B2A-L003365](../../tests/test_web_agent.py#L3365) | 3365 | `"            compact_search_query(question),"` | — |
| [SRC-F725E90B2A-L003366](../../tests/test_web_agent.py#L3366) | 3366 | `"            compact_search_query(topic_query),"` | — |
| [SRC-F725E90B2A-L003367](../../tests/test_web_agent.py#L3367) | 3367 | `"        ) if query"` | — |
| [SRC-F725E90B2A-L003368](../../tests/test_web_agent.py#L3368) | 3368 | `"    ))"` | — |
| [SRC-F725E90B2A-L003369](../../tests/test_web_agent.py#L3369) | 3369 | `"    assert source_queries == expected_queries"` | — |
| [SRC-F725E90B2A-L003370](../../tests/test_web_agent.py#L3370) | 3370 | `""` | — |
| [SRC-F725E90B2A-L003371](../../tests/test_web_agent.py#L3371) | 3371 | `""` | — |
| [SRC-F725E90B2A-L003372](../../tests/test_web_agent.py#L3372) | 3372 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L003373](../../tests/test_web_agent.py#L3373) | 3373 | `"    (\"mode\", \"planner_query\"),"` | — |
| [SRC-F725E90B2A-L003374](../../tests/test_web_agent.py#L3374) | 3374 | `"    ["` | — |
| [SRC-F725E90B2A-L003375](../../tests/test_web_agent.py#L3375) | 3375 | `"        (\"auto\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003376](../../tests/test_web_agent.py#L3376) | 3376 | `"        (\"auto\", \"site:reddit.com\"),"` | — |
| [SRC-F725E90B2A-L003377](../../tests/test_web_agent.py#L3377) | 3377 | `"        (\"latest\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003378](../../tests/test_web_agent.py#L3378) | 3378 | `"        (\"deep\", \"site:reddit.com\"),"` | — |
| [SRC-F725E90B2A-L003379](../../tests/test_web_agent.py#L3379) | 3379 | `"        (\"social\", \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"),"` | — |
| [SRC-F725E90B2A-L003380](../../tests/test_web_agent.py#L3380) | 3380 | `"    ],"` | — |
| [SRC-F725E90B2A-L003381](../../tests/test_web_agent.py#L3381) | 3381 | `")"` | — |
| [SRC-F725E90B2A-L003382](../../tests/test_web_agent.py#L3382) | 3382 | `"def test_modes_do_not_create_generic_queries_without_topic("` | — |
| [SRC-F725E90B2A-L003383](../../tests/test_web_agent.py#L3383) | 3383 | `"    monkeypatch, mode, planner_query"` | — |
| [SRC-F725E90B2A-L003384](../../tests/test_web_agent.py#L3384) | 3384 | `"):"` | — |
| [SRC-F725E90B2A-L003385](../../tests/test_web_agent.py#L3385) | 3385 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003386](../../tests/test_web_agent.py#L3386) | 3386 | `"    instruction_only = \"اذكر مصادر موثوقة، روابط مباشرة، باختصار\""` | — |
| [SRC-F725E90B2A-L003387](../../tests/test_web_agent.py#L3387) | 3387 | `"    direct_url = \"https://example.com/report\""` | — |
| [SRC-F725E90B2A-L003388](../../tests/test_web_agent.py#L3388) | 3388 | `"    observed_plans = []"` | — |
| [SRC-F725E90B2A-L003389](../../tests/test_web_agent.py#L3389) | 3389 | `""` | — |
| [SRC-F725E90B2A-L003390](../../tests/test_web_agent.py#L3390) | 3390 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003391](../../tests/test_web_agent.py#L3391) | 3391 | `"        \"agents.web_agent.route_intent\","` | — |
| [SRC-F725E90B2A-L003392](../../tests/test_web_agent.py#L3392) | 3392 | `"        lambda *args, **kwargs: {\"route\": \"WEB_DEEP\", \"reason\": \"test\"},"` | — |
| [SRC-F725E90B2A-L003393](../../tests/test_web_agent.py#L3393) | 3393 | `"    )"` | — |
| [SRC-F725E90B2A-L003394](../../tests/test_web_agent.py#L3394) | 3394 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003395](../../tests/test_web_agent.py#L3395) | 3395 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L003396](../../tests/test_web_agent.py#L3396) | 3396 | `"        lambda _question, _history: {"` | — |
| [SRC-F725E90B2A-L003397](../../tests/test_web_agent.py#L3397) | 3397 | `"            \"queries\": [planner_query],"` | — |
| [SRC-F725E90B2A-L003398](../../tests/test_web_agent.py#L3398) | 3398 | `"            \"direct_urls\": [direct_url],"` | — |
| [SRC-F725E90B2A-L003399](../../tests/test_web_agent.py#L3399) | 3399 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L003400](../../tests/test_web_agent.py#L3400) | 3400 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L003401](../../tests/test_web_agent.py#L3401) | 3401 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L003402](../../tests/test_web_agent.py#L3402) | 3402 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L003403](../../tests/test_web_agent.py#L3403) | 3403 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003404](../../tests/test_web_agent.py#L3404) | 3404 | `"        },"` | — |
| [SRC-F725E90B2A-L003405](../../tests/test_web_agent.py#L3405) | 3405 | `"    )"` | — |
| [SRC-F725E90B2A-L003406](../../tests/test_web_agent.py#L3406) | 3406 | `""` | — |
| [SRC-F725E90B2A-L003407](../../tests/test_web_agent.py#L3407) | 3407 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L003408](../../tests/test_web_agent.py#L3408) | 3408 | `"        observed_plans.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L003409](../../tests/test_web_agent.py#L3409) | 3409 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L003410](../../tests/test_web_agent.py#L3410) | 3410 | `"            \"queries_planned\": len(research_plan.get(\"queries\", [])),"` | — |
| [SRC-F725E90B2A-L003411](../../tests/test_web_agent.py#L3411) | 3411 | `"            \"queries_attempted\": 0,"` | — |
| [SRC-F725E90B2A-L003412](../../tests/test_web_agent.py#L3412) | 3412 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L003413](../../tests/test_web_agent.py#L3413) | 3413 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L003414](../../tests/test_web_agent.py#L3414) | 3414 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L003415](../../tests/test_web_agent.py#L3415) | 3415 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L003416](../../tests/test_web_agent.py#L3416) | 3416 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L003417](../../tests/test_web_agent.py#L3417) | 3417 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L003418](../../tests/test_web_agent.py#L3418) | 3418 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L003419](../../tests/test_web_agent.py#L3419) | 3419 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L003420](../../tests/test_web_agent.py#L3420) | 3420 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L003421](../../tests/test_web_agent.py#L3421) | 3421 | `"        }"` | — |
| [SRC-F725E90B2A-L003422](../../tests/test_web_agent.py#L3422) | 3422 | `""` | — |
| [SRC-F725E90B2A-L003423](../../tests/test_web_agent.py#L3423) | 3423 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L003424](../../tests/test_web_agent.py#L3424) | 3424 | `""` | — |
| [SRC-F725E90B2A-L003425](../../tests/test_web_agent.py#L3425) | 3425 | `"    agent.answer(instruction_only, mode=mode)"` | — |
| [SRC-F725E90B2A-L003426](../../tests/test_web_agent.py#L3426) | 3426 | `""` | — |
| [SRC-F725E90B2A-L003427](../../tests/test_web_agent.py#L3427) | 3427 | `"    assert observed_plans"` | — |
| [SRC-F725E90B2A-L003428](../../tests/test_web_agent.py#L3428) | 3428 | `"    assert observed_plans[0][\"queries\"] == []"` | — |
| [SRC-F725E90B2A-L003429](../../tests/test_web_agent.py#L3429) | 3429 | `"    assert observed_plans[0][\"direct_urls\"] == [direct_url]"` | — |
| [SRC-F725E90B2A-L003430](../../tests/test_web_agent.py#L3430) | 3430 | `""` | — |
| [SRC-F725E90B2A-L003431](../../tests/test_web_agent.py#L3431) | 3431 | `""` | — |
| [SRC-F725E90B2A-L003432](../../tests/test_web_agent.py#L3432) | 3432 | `"def test_auto_navigation_strips_arabic_search_verb_without_regex_regression(monkeypatch):"` | — |
| [SRC-F725E90B2A-L003433](../../tests/test_web_agent.py#L3433) | 3433 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L003434](../../tests/test_web_agent.py#L3434) | 3434 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L003435](../../tests/test_web_agent.py#L3435) | 3435 | `"    question = \"ابحث عن الموقع الرسمي لشركة النور\""` | — |
| [SRC-F725E90B2A-L003436](../../tests/test_web_agent.py#L3436) | 3436 | `"    observed_plans = []"` | — |
| [SRC-F725E90B2A-L003437](../../tests/test_web_agent.py#L3437) | 3437 | `""` | — |
| [SRC-F725E90B2A-L003438](../../tests/test_web_agent.py#L3438) | 3438 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L003439](../../tests/test_web_agent.py#L3439) | 3439 | `"        \"agents.web_agent.route_intent\","` | — |
| [SRC-F725E90B2A-L003440](../../tests/test_web_agent.py#L3440) | 3440 | `"        lambda *args, **kwargs: {\"route\": \"WEB_SIMPLE\", \"reason\": \"test\"},"` | — |
| [SRC-F725E90B2A-L003441](../../tests/test_web_agent.py#L3441) | 3441 | `"    )"` | — |
| [SRC-F725E90B2A-L003442](../../tests/test_web_agent.py#L3442) | 3442 | `"    monkeypatch.setattr("` | — |
