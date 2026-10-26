# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **033**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L002510 إلى SRC-A16FA6D4B5-L000033
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L002510](../../tests/test_web_agent.py#L2510) | 2510 | `""` | — |
| [SRC-F725E90B2A-L002511](../../tests/test_web_agent.py#L2511) | 2511 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-F725E90B2A-L002512](../../tests/test_web_agent.py#L2512) | 2512 | `""` | — |
| [SRC-F725E90B2A-L002513](../../tests/test_web_agent.py#L2513) | 2513 | `"    assert web_agent.WebAgent()._fetch_page(\"https://first.example/article\") == (\"\", \"\")"` | — |
| [SRC-F725E90B2A-L002514](../../tests/test_web_agent.py#L2514) | 2514 | `"    assert resolved_hosts == [\"first.example\"]"` | — |
| [SRC-F725E90B2A-L002515](../../tests/test_web_agent.py#L2515) | 2515 | `"    assert len(requests) == 1"` | — |
| [SRC-F725E90B2A-L002516](../../tests/test_web_agent.py#L2516) | 2516 | `"    assert requests[0][1] == \"https://93.184.216.34/article\""` | — |
| [SRC-F725E90B2A-L002517](../../tests/test_web_agent.py#L2517) | 2517 | `"    assert requests[0][2][\"headers\"][\"Host\"] == \"first.example\""` | — |
| [SRC-F725E90B2A-L002518](../../tests/test_web_agent.py#L2518) | 2518 | `"    assert requests[0][2][\"extensions\"][\"sni_hostname\"] == \"first.example\""` | — |
| [SRC-F725E90B2A-L002519](../../tests/test_web_agent.py#L2519) | 2519 | `""` | — |
| [SRC-F725E90B2A-L002520](../../tests/test_web_agent.py#L2520) | 2520 | `""` | — |
| [SRC-F725E90B2A-L002521](../../tests/test_web_agent.py#L2521) | 2521 | `"def test_fetch_page_revalidates_dns_for_each_redirect_destination(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002522](../../tests/test_web_agent.py#L2522) | 2522 | `"    from contextlib import contextmanager"` | — |
| [SRC-F725E90B2A-L002523](../../tests/test_web_agent.py#L2523) | 2523 | `""` | — |
| [SRC-F725E90B2A-L002524](../../tests/test_web_agent.py#L2524) | 2524 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002525](../../tests/test_web_agent.py#L2525) | 2525 | `""` | — |
| [SRC-F725E90B2A-L002526](../../tests/test_web_agent.py#L2526) | 2526 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L002527](../../tests/test_web_agent.py#L2527) | 2527 | `""` | — |
| [SRC-F725E90B2A-L002528](../../tests/test_web_agent.py#L2528) | 2528 | `"    resolved_hosts = []"` | — |
| [SRC-F725E90B2A-L002529](../../tests/test_web_agent.py#L2529) | 2529 | `"    requests = []"` | — |
| [SRC-F725E90B2A-L002530](../../tests/test_web_agent.py#L2530) | 2530 | `""` | — |
| [SRC-F725E90B2A-L002531](../../tests/test_web_agent.py#L2531) | 2531 | `"    def resolve_public_ip(host):"` | — |
| [SRC-F725E90B2A-L002532](../../tests/test_web_agent.py#L2532) | 2532 | `"        resolved_hosts.append(host)"` | — |
| [SRC-F725E90B2A-L002533](../../tests/test_web_agent.py#L2533) | 2533 | `"        if host == \"first.example\":"` | — |
| [SRC-F725E90B2A-L002534](../../tests/test_web_agent.py#L2534) | 2534 | `"            return [\"93.184.216.34\"]"` | — |
| [SRC-F725E90B2A-L002535](../../tests/test_web_agent.py#L2535) | 2535 | `"        # Model a redirect destination that resolves to no verified public IP."` | — |
| [SRC-F725E90B2A-L002536](../../tests/test_web_agent.py#L2536) | 2536 | `"        return None"` | — |
| [SRC-F725E90B2A-L002537](../../tests/test_web_agent.py#L2537) | 2537 | `""` | — |
| [SRC-F725E90B2A-L002538](../../tests/test_web_agent.py#L2538) | 2538 | `"    monkeypatch.setattr(web_agent, \"_public_ip_literals\", resolve_public_ip)"` | — |
| [SRC-F725E90B2A-L002539](../../tests/test_web_agent.py#L2539) | 2539 | `""` | — |
| [SRC-F725E90B2A-L002540](../../tests/test_web_agent.py#L2540) | 2540 | `"    class RedirectResponse:"` | — |
| [SRC-F725E90B2A-L002541](../../tests/test_web_agent.py#L2541) | 2541 | `"        status_code = 302"` | — |
| [SRC-F725E90B2A-L002542](../../tests/test_web_agent.py#L2542) | 2542 | `""` | — |
| [SRC-F725E90B2A-L002543](../../tests/test_web_agent.py#L2543) | 2543 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L002544](../../tests/test_web_agent.py#L2544) | 2544 | `"            self.headers = {\"location\": \"https://second.example/internal\"}"` | — |
| [SRC-F725E90B2A-L002545](../../tests/test_web_agent.py#L2545) | 2545 | `""` | — |
| [SRC-F725E90B2A-L002546](../../tests/test_web_agent.py#L2546) | 2546 | `"    @contextmanager"` | — |
| [SRC-F725E90B2A-L002547](../../tests/test_web_agent.py#L2547) | 2547 | `"    def fake_stream(self, method, url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002548](../../tests/test_web_agent.py#L2548) | 2548 | `"        requests.append((method, str(url), kwargs))"` | — |
| [SRC-F725E90B2A-L002549](../../tests/test_web_agent.py#L2549) | 2549 | `"        yield RedirectResponse()"` | — |
| [SRC-F725E90B2A-L002550](../../tests/test_web_agent.py#L2550) | 2550 | `""` | — |
| [SRC-F725E90B2A-L002551](../../tests/test_web_agent.py#L2551) | 2551 | `"    class FakeClient:"` | — |
| [SRC-F725E90B2A-L002552](../../tests/test_web_agent.py#L2552) | 2552 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-F725E90B2A-L002553](../../tests/test_web_agent.py#L2553) | 2553 | `"            self.options = kwargs"` | — |
| [SRC-F725E90B2A-L002554](../../tests/test_web_agent.py#L2554) | 2554 | `""` | — |
| [SRC-F725E90B2A-L002555](../../tests/test_web_agent.py#L2555) | 2555 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L002556](../../tests/test_web_agent.py#L2556) | 2556 | `"            return self"` | — |
| [SRC-F725E90B2A-L002557](../../tests/test_web_agent.py#L2557) | 2557 | `""` | — |
| [SRC-F725E90B2A-L002558](../../tests/test_web_agent.py#L2558) | 2558 | `"        def __exit__(self, *_args):"` | — |
| [SRC-F725E90B2A-L002559](../../tests/test_web_agent.py#L2559) | 2559 | `"            return False"` | — |
| [SRC-F725E90B2A-L002560](../../tests/test_web_agent.py#L2560) | 2560 | `""` | — |
| [SRC-F725E90B2A-L002561](../../tests/test_web_agent.py#L2561) | 2561 | `"        stream = fake_stream"` | — |
| [SRC-F725E90B2A-L002562](../../tests/test_web_agent.py#L2562) | 2562 | `""` | — |
| [SRC-F725E90B2A-L002563](../../tests/test_web_agent.py#L2563) | 2563 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-F725E90B2A-L002564](../../tests/test_web_agent.py#L2564) | 2564 | `""` | — |
| [SRC-F725E90B2A-L002565](../../tests/test_web_agent.py#L2565) | 2565 | `"    assert web_agent.WebAgent()._fetch_page(\"https://first.example/article\") == (\"\", \"\")"` | — |
| [SRC-F725E90B2A-L002566](../../tests/test_web_agent.py#L2566) | 2566 | `"    assert resolved_hosts == [\"first.example\", \"second.example\"]"` | — |
| [SRC-F725E90B2A-L002567](../../tests/test_web_agent.py#L2567) | 2567 | `"    # The second host is validated before any connection attempt to it."` | — |
| [SRC-F725E90B2A-L002568](../../tests/test_web_agent.py#L2568) | 2568 | `"    assert len(requests) == 1"` | — |
| [SRC-F725E90B2A-L002569](../../tests/test_web_agent.py#L2569) | 2569 | `""` | — |
| [SRC-F725E90B2A-L002570](../../tests/test_web_agent.py#L2570) | 2570 | `""` | — |
| [SRC-F725E90B2A-L002571](../../tests/test_web_agent.py#L2571) | 2571 | `""` | — |
| [SRC-F725E90B2A-L002572](../../tests/test_web_agent.py#L2572) | 2572 | `"def test_history_search_query_uses_shared_context_resolver():"` | — |
| [SRC-F725E90B2A-L002573](../../tests/test_web_agent.py#L2573) | 2573 | `"    history = ["` | — |
| [SRC-F725E90B2A-L002574](../../tests/test_web_agent.py#L2574) | 2574 | `"        {\"role\": \"user\", \"content\": \"سعر آيفون 16 في مصر\"},"` | — |
| [SRC-F725E90B2A-L002575](../../tests/test_web_agent.py#L2575) | 2575 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن السعر.\"},"` | — |
| [SRC-F725E90B2A-L002576](../../tests/test_web_agent.py#L2576) | 2576 | `"    ]"` | — |
| [SRC-F725E90B2A-L002577](../../tests/test_web_agent.py#L2577) | 2577 | `"    query = WebAgent._history_search_query(\"هل فيه ضمان؟\", history)"` | — |
| [SRC-F725E90B2A-L002578](../../tests/test_web_agent.py#L2578) | 2578 | `"    assert \"آيفون 16\" in query"` | — |
| [SRC-F725E90B2A-L002579](../../tests/test_web_agent.py#L2579) | 2579 | `"    assert \"ضمان\" in query"` | — |
| [SRC-F725E90B2A-L002580](../../tests/test_web_agent.py#L2580) | 2580 | `""` | — |
| [SRC-F725E90B2A-L002581](../../tests/test_web_agent.py#L2581) | 2581 | `""` | — |
| [SRC-F725E90B2A-L002582](../../tests/test_web_agent.py#L2582) | 2582 | `"def test_history_search_query_does_not_reuse_stale_topic_after_acknowledgment():"` | — |
| [SRC-F725E90B2A-L002583](../../tests/test_web_agent.py#L2583) | 2583 | `"    history = ["` | — |
| [SRC-F725E90B2A-L002584](../../tests/test_web_agent.py#L2584) | 2584 | `"        {\"role\": \"user\", \"content\": \"سعر آيفون 16 في مصر\"},"` | — |
| [SRC-F725E90B2A-L002585](../../tests/test_web_agent.py#L2585) | 2585 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن السعر.\"},"` | — |
| [SRC-F725E90B2A-L002586](../../tests/test_web_agent.py#L2586) | 2586 | `"        {\"role\": \"user\", \"content\": \"شكرا\"},"` | — |
| [SRC-F725E90B2A-L002587](../../tests/test_web_agent.py#L2587) | 2587 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-F725E90B2A-L002588](../../tests/test_web_agent.py#L2588) | 2588 | `"    ]"` | — |
| [SRC-F725E90B2A-L002589](../../tests/test_web_agent.py#L2589) | 2589 | `"    assert WebAgent._history_search_query(\"فين؟\", history) == \"فين؟\""` | — |
| [SRC-F725E90B2A-L002590](../../tests/test_web_agent.py#L2590) | 2590 | `""` | — |
| [SRC-F725E90B2A-L002591](../../tests/test_web_agent.py#L2591) | 2591 | `""` | — |
| [SRC-F725E90B2A-L002592](../../tests/test_web_agent.py#L2592) | 2592 | `"def test_frontend_exposes_structured_page_fetch_statuses():"` | — |
| [SRC-F725E90B2A-L002593](../../tests/test_web_agent.py#L2593) | 2593 | `"    html_path = Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\""` | — |
| [SRC-F725E90B2A-L002594](../../tests/test_web_agent.py#L2594) | 2594 | `"    html = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002595](../../tests/test_web_agent.py#L2595) | 2595 | `"    assert \"page_fetch_status\" in html"` | — |
| [SRC-F725E90B2A-L002596](../../tests/test_web_agent.py#L2596) | 2596 | `"    assert \"partial_extraction\" in html"` | — |
| [SRC-F725E90B2A-L002597](../../tests/test_web_agent.py#L2597) | 2597 | `"    assert \"لم يُستخرج نص؛ قد تكون الصفحة ديناميكية أو محجوبة\" in html"` | — |
| [SRC-F725E90B2A-L002598](../../tests/test_web_agent.py#L2598) | 2598 | `"    assert \"تشخيص الموصلات في هذا الطلب\" in html"` | — |
| [SRC-F725E90B2A-L002599](../../tests/test_web_agent.py#L2599) | 2599 | `""` | — |
| [SRC-F725E90B2A-L002600](../../tests/test_web_agent.py#L2600) | 2600 | `""` | — |
| [SRC-F725E90B2A-L002601](../../tests/test_web_agent.py#L2601) | 2601 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L002602](../../tests/test_web_agent.py#L2602) | 2602 | `"    \"method_name\","` | — |
| [SRC-F725E90B2A-L002603](../../tests/test_web_agent.py#L2603) | 2603 | `"    [\"_search_duckduckgo_html\", \"_search_bing_rss\", \"_search_news\"],"` | — |
| [SRC-F725E90B2A-L002604](../../tests/test_web_agent.py#L2604) | 2604 | `")"` | — |
| [SRC-F725E90B2A-L002605](../../tests/test_web_agent.py#L2605) | 2605 | `"def test_search_providers_do_not_follow_redirects_automatically("` | — |
| [SRC-F725E90B2A-L002606](../../tests/test_web_agent.py#L2606) | 2606 | `"    monkeypatch, method_name"` | — |
| [SRC-F725E90B2A-L002607](../../tests/test_web_agent.py#L2607) | 2607 | `"):"` | — |
| [SRC-F725E90B2A-L002608](../../tests/test_web_agent.py#L2608) | 2608 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002609](../../tests/test_web_agent.py#L2609) | 2609 | `""` | — |
| [SRC-F725E90B2A-L002610](../../tests/test_web_agent.py#L2610) | 2610 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002611](../../tests/test_web_agent.py#L2611) | 2611 | `"    observed = []"` | — |
| [SRC-F725E90B2A-L002612](../../tests/test_web_agent.py#L2612) | 2612 | `""` | — |
| [SRC-F725E90B2A-L002613](../../tests/test_web_agent.py#L2613) | 2613 | `"    class RedirectResponse:"` | — |
| [SRC-F725E90B2A-L002614](../../tests/test_web_agent.py#L2614) | 2614 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L002615](../../tests/test_web_agent.py#L2615) | 2615 | `"            self.status_code = 302"` | — |
| [SRC-F725E90B2A-L002616](../../tests/test_web_agent.py#L2616) | 2616 | `"            self.headers = {\"location\": \"http://127.0.0.1:8765/private\"}"` | — |
| [SRC-F725E90B2A-L002617](../../tests/test_web_agent.py#L2617) | 2617 | `"            self.text = \"redirect\""` | — |
| [SRC-F725E90B2A-L002618](../../tests/test_web_agent.py#L2618) | 2618 | `"            self.content = b\"redirect\""` | — |
| [SRC-F725E90B2A-L002619](../../tests/test_web_agent.py#L2619) | 2619 | `""` | — |
| [SRC-F725E90B2A-L002620](../../tests/test_web_agent.py#L2620) | 2620 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002621](../../tests/test_web_agent.py#L2621) | 2621 | `"        observed.append((url, kwargs.get(\"follow_redirects\")))"` | — |
| [SRC-F725E90B2A-L002622](../../tests/test_web_agent.py#L2622) | 2622 | `"        return RedirectResponse()"` | — |
| [SRC-F725E90B2A-L002623](../../tests/test_web_agent.py#L2623) | 2623 | `""` | — |
| [SRC-F725E90B2A-L002624](../../tests/test_web_agent.py#L2624) | 2624 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L002625](../../tests/test_web_agent.py#L2625) | 2625 | `"    method = getattr(agent, method_name)"` | — |
| [SRC-F725E90B2A-L002626](../../tests/test_web_agent.py#L2626) | 2626 | `"    with pytest.raises(RuntimeError, match=\"HTTP 302\"):"` | — |
| [SRC-F725E90B2A-L002627](../../tests/test_web_agent.py#L2627) | 2627 | `"        method(\"redirect regression test\")"` | — |
| [SRC-F725E90B2A-L002628](../../tests/test_web_agent.py#L2628) | 2628 | `""` | — |
| [SRC-F725E90B2A-L002629](../../tests/test_web_agent.py#L2629) | 2629 | `"    assert len(observed) == 1"` | — |
| [SRC-F725E90B2A-L002630](../../tests/test_web_agent.py#L2630) | 2630 | `"    assert observed[0][1] is False"` | — |
| [SRC-F725E90B2A-L002631](../../tests/test_web_agent.py#L2631) | 2631 | `""` | — |
| [SRC-F725E90B2A-L002632](../../tests/test_web_agent.py#L2632) | 2632 | `""` | — |
| [SRC-F725E90B2A-L002633](../../tests/test_web_agent.py#L2633) | 2633 | `""` | — |
| [SRC-F725E90B2A-L002634](../../tests/test_web_agent.py#L2634) | 2634 | `"@pytest.mark.parametrize(\"mode\", [\"deep\", \"latest\", \"social\"])"` | — |
| [SRC-F725E90B2A-L002635](../../tests/test_web_agent.py#L2635) | 2635 | `"def test_explicit_modes_survive_deterministic_planning(monkeypatch, mode):"` | — |
| [SRC-F725E90B2A-L002636](../../tests/test_web_agent.py#L2636) | 2636 | `"    \"\"\"A missing planner model must not erase a mode explicitly selected by the user.\"\"\""` | — |
| [SRC-F725E90B2A-L002637](../../tests/test_web_agent.py#L2637) | 2637 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002638](../../tests/test_web_agent.py#L2638) | 2638 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L002639](../../tests/test_web_agent.py#L2639) | 2639 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002640](../../tests/test_web_agent.py#L2640) | 2640 | `""` | — |
| [SRC-F725E90B2A-L002641](../../tests/test_web_agent.py#L2641) | 2641 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L002642](../../tests/test_web_agent.py#L2642) | 2642 | `"        seen[\"plan\"] = dict(research_plan)"` | — |
| [SRC-F725E90B2A-L002643](../../tests/test_web_agent.py#L2643) | 2643 | `"        sources = [sample_source(0), sample_source(1)]"` | — |
| [SRC-F725E90B2A-L002644](../../tests/test_web_agent.py#L2644) | 2644 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L002645](../../tests/test_web_agent.py#L2645) | 2645 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002646](../../tests/test_web_agent.py#L2646) | 2646 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002647](../../tests/test_web_agent.py#L2647) | 2647 | `"            \"query_results\": ["` | — |
| [SRC-F725E90B2A-L002648](../../tests/test_web_agent.py#L2648) | 2648 | `"                {\"query\": query, \"results\": 1}"` | — |
| [SRC-F725E90B2A-L002649](../../tests/test_web_agent.py#L2649) | 2649 | `"                for query in research_plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L002650](../../tests/test_web_agent.py#L2650) | 2650 | `"            ],"` | — |
| [SRC-F725E90B2A-L002651](../../tests/test_web_agent.py#L2651) | 2651 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-F725E90B2A-L002652](../../tests/test_web_agent.py#L2652) | 2652 | `"            \"pages_fetched\": len(sources),"` | — |
| [SRC-F725E90B2A-L002653](../../tests/test_web_agent.py#L2653) | 2653 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L002654](../../tests/test_web_agent.py#L2654) | 2654 | `"            \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-F725E90B2A-L002655](../../tests/test_web_agent.py#L2655) | 2655 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002656](../../tests/test_web_agent.py#L2656) | 2656 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L002657](../../tests/test_web_agent.py#L2657) | 2657 | `"            \"planning_method\": \"deterministic_fallback\","` | — |
| [SRC-F725E90B2A-L002658](../../tests/test_web_agent.py#L2658) | 2658 | `"        }"` | — |
| [SRC-F725E90B2A-L002659](../../tests/test_web_agent.py#L2659) | 2659 | `""` | — |
| [SRC-F725E90B2A-L002660](../../tests/test_web_agent.py#L2660) | 2660 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L002661](../../tests/test_web_agent.py#L2661) | 2661 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L002662](../../tests/test_web_agent.py#L2662) | 2662 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L002663](../../tests/test_web_agent.py#L2663) | 2663 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002664](../../tests/test_web_agent.py#L2664) | 2664 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002665](../../tests/test_web_agent.py#L2665) | 2665 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L002666](../../tests/test_web_agent.py#L2666) | 2666 | `"        lambda question, history, sources, search_warning, research_plan=None,"` | — |
| [SRC-F725E90B2A-L002667](../../tests/test_web_agent.py#L2667) | 2667 | `"               search_report=None: \"توجد نتائج أولية للمراجعة [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L002668](../../tests/test_web_agent.py#L2668) | 2668 | `"    )"` | — |
| [SRC-F725E90B2A-L002669](../../tests/test_web_agent.py#L2669) | 2669 | `""` | — |
| [SRC-F725E90B2A-L002670](../../tests/test_web_agent.py#L2670) | 2670 | `"    question = ("` | — |
| [SRC-F725E90B2A-L002671](../../tests/test_web_agent.py#L2671) | 2671 | `"        \"ابحث عن شقة في التجمع الخامس بسعر 5000000 جنيه\""` | — |
| [SRC-F725E90B2A-L002672](../../tests/test_web_agent.py#L2672) | 2672 | `"        if mode == \"deep\" else \"الطاقة المتجددة في مصر\""` | — |
| [SRC-F725E90B2A-L002673](../../tests/test_web_agent.py#L2673) | 2673 | `"    )"` | — |
| [SRC-F725E90B2A-L002674](../../tests/test_web_agent.py#L2674) | 2674 | `"    result = agent.answer(question, mode=mode)"` | — |
| [SRC-F725E90B2A-L002675](../../tests/test_web_agent.py#L2675) | 2675 | `"    plan = seen[\"plan\"]"` | — |
| [SRC-F725E90B2A-L002676](../../tests/test_web_agent.py#L2676) | 2676 | `""` | — |
| [SRC-F725E90B2A-L002677](../../tests/test_web_agent.py#L2677) | 2677 | `"    assert plan[\"mode\"] == mode"` | — |
| [SRC-F725E90B2A-L002678](../../tests/test_web_agent.py#L2678) | 2678 | `"    assert result[\"research_plan\"][\"mode\"] == mode"` | — |
| [SRC-F725E90B2A-L002679](../../tests/test_web_agent.py#L2679) | 2679 | `"    if mode == \"deep\":"` | — |
| [SRC-F725E90B2A-L002680](../../tests/test_web_agent.py#L2680) | 2680 | `"        assert plan[\"depth\"] == \"deep\""` | — |
| [SRC-F725E90B2A-L002681](../../tests/test_web_agent.py#L2681) | 2681 | `"        assert len(plan[\"queries\"]) >= 3"` | — |
| [SRC-F725E90B2A-L002682](../../tests/test_web_agent.py#L2682) | 2682 | `"        assert any(\"إعلانات عقارية\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002683](../../tests/test_web_agent.py#L2683) | 2683 | `"        assert any(\"متوسط أسعار السوق للمتر\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002684](../../tests/test_web_agent.py#L2684) | 2684 | `"    elif mode == \"latest\":"` | — |
| [SRC-F725E90B2A-L002685](../../tests/test_web_agent.py#L2685) | 2685 | `"        assert plan[\"freshness\"] == \"current\""` | — |
| [SRC-F725E90B2A-L002686](../../tests/test_web_agent.py#L2686) | 2686 | `"        assert any("` | — |
| [SRC-F725E90B2A-L002687](../../tests/test_web_agent.py#L2687) | 2687 | `"            \"latest\" in query.lower() or \"recent\" in query.lower()"` | — |
| [SRC-F725E90B2A-L002688](../../tests/test_web_agent.py#L2688) | 2688 | `"            for query in plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L002689](../../tests/test_web_agent.py#L2689) | 2689 | `"        )"` | — |
| [SRC-F725E90B2A-L002690](../../tests/test_web_agent.py#L2690) | 2690 | `"    else:"` | — |
| [SRC-F725E90B2A-L002691](../../tests/test_web_agent.py#L2691) | 2691 | `"        assert plan[\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L002692](../../tests/test_web_agent.py#L2692) | 2692 | `"        assert any(query.startswith(\"site:\") for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002693](../../tests/test_web_agent.py#L2693) | 2693 | `""` | — |
| [SRC-F725E90B2A-L002694](../../tests/test_web_agent.py#L2694) | 2694 | `""` | — |
| [SRC-F725E90B2A-L002695](../../tests/test_web_agent.py#L2695) | 2695 | `"def test_web_answer_integrity_is_attached_without_live_network(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002696](../../tests/test_web_agent.py#L2696) | 2696 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002697](../../tests/test_web_agent.py#L2697) | 2697 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002698](../../tests/test_web_agent.py#L2698) | 2698 | `"        agent, \"_question_coverage_targets\", lambda question: [\"السعر\", \"المساحة\"]"` | — |
| [SRC-F725E90B2A-L002699](../../tests/test_web_agent.py#L2699) | 2699 | `"    )"` | — |
| [SRC-F725E90B2A-L002700](../../tests/test_web_agent.py#L2700) | 2700 | `"    monkeypatch.setattr(agent, \"_answer_with_budget\", lambda question, history, mode: {"` | — |
| [SRC-F725E90B2A-L002701](../../tests/test_web_agent.py#L2701) | 2701 | `"        \"kind\": \"web_research\","` | — |
| [SRC-F725E90B2A-L002702](../../tests/test_web_agent.py#L2702) | 2702 | `"        \"answer\": \"السعر 500 جنيه [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L002703](../../tests/test_web_agent.py#L2703) | 2703 | `"        \"sources\": [{"` | — |
| [SRC-F725E90B2A-L002704](../../tests/test_web_agent.py#L2704) | 2704 | `"            \"title\": \"تفاصيل العرض\","` | — |
| [SRC-F725E90B2A-L002705](../../tests/test_web_agent.py#L2705) | 2705 | `"            \"url\": \"https://example.com/offer\","` | — |
| [SRC-F725E90B2A-L002706](../../tests/test_web_agent.py#L2706) | 2706 | `"            \"snippet\": \"السعر 300 جنيه\","` | — |
| [SRC-F725E90B2A-L002707](../../tests/test_web_agent.py#L2707) | 2707 | `"            \"page_fetched\": False,"` | — |
| [SRC-F725E90B2A-L002708](../../tests/test_web_agent.py#L2708) | 2708 | `"        }],"` | — |
| [SRC-F725E90B2A-L002709](../../tests/test_web_agent.py#L2709) | 2709 | `"        \"research_quality\": \"partial\","` | — |
| [SRC-F725E90B2A-L002710](../../tests/test_web_agent.py#L2710) | 2710 | `"        \"search_report\": {},"` | — |
| [SRC-F725E90B2A-L002711](../../tests/test_web_agent.py#L2711) | 2711 | `"        \"answer_coverage\": {},"` | — |
| [SRC-F725E90B2A-L002712](../../tests/test_web_agent.py#L2712) | 2712 | `"        \"used_language_model\": True,"` | — |
| [SRC-F725E90B2A-L002713](../../tests/test_web_agent.py#L2713) | 2713 | `"        \"used_web_search\": True,"` | — |
| [SRC-F725E90B2A-L002714](../../tests/test_web_agent.py#L2714) | 2714 | `"        \"warnings\": [],"` | — |
| [SRC-F725E90B2A-L002715](../../tests/test_web_agent.py#L2715) | 2715 | `"    })"` | — |
| [SRC-F725E90B2A-L002716](../../tests/test_web_agent.py#L2716) | 2716 | `""` | — |
| [SRC-F725E90B2A-L002717](../../tests/test_web_agent.py#L2717) | 2717 | `"    result = agent.answer(\"قارن السعر والمساحة\", mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L002718](../../tests/test_web_agent.py#L2718) | 2718 | `""` | — |
| [SRC-F725E90B2A-L002719](../../tests/test_web_agent.py#L2719) | 2719 | `"    assert result[\"answer_integrity\"][\"semantic_verification\"] is False"` | — |
| [SRC-F725E90B2A-L002720](../../tests/test_web_agent.py#L2720) | 2720 | `"    assert result[\"answer_integrity\"][\"independent_fact_check\"] is False"` | — |
| [SRC-F725E90B2A-L002721](../../tests/test_web_agent.py#L2721) | 2721 | `"    assert result[\"answer_integrity\"][\"potentially_unsupported_numeric_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002722](../../tests/test_web_agent.py#L2722) | 2722 | `"    assert result[\"answer_integrity\"][\"potentially_unsupported_numeric_by_citation_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002723](../../tests/test_web_agent.py#L2723) | 2723 | `"    assert result[\"answer_integrity\"][\"potentially_missing_target_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002724](../../tests/test_web_agent.py#L2724) | 2724 | `"    assert result[\"task_fulfillment_status\"] == \"possible_gap_detected\""` | — |
| [SRC-F725E90B2A-L002725](../../tests/test_web_agent.py#L2725) | 2725 | `"    assert result[\"answer_coverage\"][\"lexical_screen_method\"] == ("` | — |
| [SRC-F725E90B2A-L002726](../../tests/test_web_agent.py#L2726) | 2726 | `"        \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-F725E90B2A-L002727](../../tests/test_web_agent.py#L2727) | 2727 | `"    )"` | — |
| [SRC-F725E90B2A-L002728](../../tests/test_web_agent.py#L2728) | 2728 | `""` | — |
| [SRC-F725E90B2A-L002729](../../tests/test_web_agent.py#L2729) | 2729 | `""` | — |
| [SRC-F725E90B2A-L002730](../../tests/test_web_agent.py#L2730) | 2730 | `"def test_frontend_labels_answer_integrity_screen_as_non_semantic():"` | — |
| [SRC-F725E90B2A-L002731](../../tests/test_web_agent.py#L2731) | 2731 | `"    html = ("` | — |
| [SRC-F725E90B2A-L002732](../../tests/test_web_agent.py#L2732) | 2732 | `"        Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\""` | — |
| [SRC-F725E90B2A-L002733](../../tests/test_web_agent.py#L2733) | 2733 | `"    ).read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002734](../../tests/test_web_agent.py#L2734) | 2734 | `"    assert \"فحص لفظي أولي:\" in html"` | — |
| [SRC-F725E90B2A-L002735](../../tests/test_web_agent.py#L2735) | 2735 | `"    assert \"لا يثبت هذا الفحص صحة الوقائع أو دلالة الاستشهاد\" in html"` | — |
| [SRC-F725E90B2A-L002736](../../tests/test_web_agent.py#L2736) | 2736 | `"    assert \"potentially_unsupported_numeric_by_citation_count\" in html"` | — |
| [SRC-F725E90B2A-L002737](../../tests/test_web_agent.py#L2737) | 2737 | `"    assert \"potential_value_discrepancy_count\" in html"` | — |
| [SRC-F725E90B2A-L002738](../../tests/test_web_agent.py#L2738) | 2738 | `""` | — |
| [SRC-F725E90B2A-L002739](../../tests/test_web_agent.py#L2739) | 2739 | `""` | — |
| [SRC-F725E90B2A-L002740](../../tests/test_web_agent.py#L2740) | 2740 | `"def test_search_web_keeps_arabic_topic_matches_in_english_indexed_results(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002741](../../tests/test_web_agent.py#L2741) | 2741 | `"    cases = ["` | — |
| [SRC-F725E90B2A-L002742](../../tests/test_web_agent.py#L2742) | 2742 | `"        ("` | — |
| [SRC-F725E90B2A-L002743](../../tests/test_web_agent.py#L2743) | 2743 | `"            \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\","` | — |
| [SRC-F725E90B2A-L002744](../../tests/test_web_agent.py#L2744) | 2744 | `"            \"Egypt's capital is Cairo\","` | — |
| [SRC-F725E90B2A-L002745](../../tests/test_web_agent.py#L2745) | 2745 | `"            \"The capital city of Egypt is Cairo.\","` | — |
| [SRC-F725E90B2A-L002746](../../tests/test_web_agent.py#L2746) | 2746 | `"        ),"` | — |
| [SRC-F725E90B2A-L002747](../../tests/test_web_agent.py#L2747) | 2747 | `"        ("` | — |
| [SRC-F725E90B2A-L002748](../../tests/test_web_agent.py#L2748) | 2748 | `"            \"حلل أهم التحديات التي تواجه السيارات الكهربائية في مصر، وقارن بين التكلفة والبنية التحتية والشحن. استخدم مصادر متعددة، وميز بين الحقائق والاستنتاجات، واذكر روابط المصادر.\","` | — |
| [SRC-F725E90B2A-L002749](../../tests/test_web_agent.py#L2749) | 2749 | `"            \"Electric vehicles in Egypt: charging infrastructure and costs\","` | — |
| [SRC-F725E90B2A-L002750](../../tests/test_web_agent.py#L2750) | 2750 | `"            \"Electric cars face high costs and limited charging infrastructure in Egypt.\","` | — |
| [SRC-F725E90B2A-L002751](../../tests/test_web_agent.py#L2751) | 2751 | `"        ),"` | — |
| [SRC-F725E90B2A-L002752](../../tests/test_web_agent.py#L2752) | 2752 | `"        ("` | — |
| [SRC-F725E90B2A-L002753](../../tests/test_web_agent.py#L2753) | 2753 | `"            \"ما أحدث التطورات في وكلاء الذكاء الاصطناعي خلال الأيام السبعة الماضية؟ اذكر تواريخ الأخبار وروابط المصادر، ولا تعرض معلومات قديمة باعتبارها جديدة.\","` | — |
| [SRC-F725E90B2A-L002754](../../tests/test_web_agent.py#L2754) | 2754 | `"            \"Recent developments in AI agents\","` | — |
| [SRC-F725E90B2A-L002755](../../tests/test_web_agent.py#L2755) | 2755 | `"            \"New AI agent tools and launches this week.\","` | — |
| [SRC-F725E90B2A-L002756](../../tests/test_web_agent.py#L2756) | 2756 | `"        ),"` | — |
| [SRC-F725E90B2A-L002757](../../tests/test_web_agent.py#L2757) | 2757 | `"        ("` | — |
| [SRC-F725E90B2A-L002758](../../tests/test_web_agent.py#L2758) | 2758 | `"            \"اجمع آراء وتجارب المستخدمين العامة حول السيارات الكهربائية في مصر. اعرض الآراء الإيجابية والسلبية، واذكر روابط المنشورات أو المصادر المتاحة.\","` | — |
| [SRC-F725E90B2A-L002759](../../tests/test_web_agent.py#L2759) | 2759 | `"            \"Reddit users share electric car experiences in Egypt\","` | — |
| [SRC-F725E90B2A-L002760](../../tests/test_web_agent.py#L2760) | 2760 | `"            \"Owners discuss electric vehicles, charging and daily use.\","` | — |
| [SRC-F725E90B2A-L002761](../../tests/test_web_agent.py#L2761) | 2761 | `"        ),"` | — |
| [SRC-F725E90B2A-L002762](../../tests/test_web_agent.py#L2762) | 2762 | `"    ]"` | — |
| [SRC-F725E90B2A-L002763](../../tests/test_web_agent.py#L2763) | 2763 | `"    for index, (query, title, snippet) in enumerate(cases):"` | — |
| [SRC-F725E90B2A-L002764](../../tests/test_web_agent.py#L2764) | 2764 | `"        agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002765](../../tests/test_web_agent.py#L2765) | 2765 | `"        row = {"` | — |
| [SRC-F725E90B2A-L002766](../../tests/test_web_agent.py#L2766) | 2766 | `"            \"title\": title,"` | — |
| [SRC-F725E90B2A-L002767](../../tests/test_web_agent.py#L2767) | 2767 | `"            \"url\": f\"https://example.com/case-{index}\","` | — |
| [SRC-F725E90B2A-L002768](../../tests/test_web_agent.py#L2768) | 2768 | `"            \"snippet\": snippet,"` | — |
| [SRC-F725E90B2A-L002769](../../tests/test_web_agent.py#L2769) | 2769 | `"            \"provider\": \"fake_provider\","` | — |
| [SRC-F725E90B2A-L002770](../../tests/test_web_agent.py#L2770) | 2770 | `"            \"provider_rank\": 1,"` | — |
| [SRC-F725E90B2A-L002771](../../tests/test_web_agent.py#L2771) | 2771 | `"            \"search_query\": query,"` | — |
| [SRC-F725E90B2A-L002772](../../tests/test_web_agent.py#L2772) | 2772 | `"        }"` | — |
| [SRC-F725E90B2A-L002773](../../tests/test_web_agent.py#L2773) | 2773 | `"        monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _q, row=row: [dict(row)])"` | — |
| [SRC-F725E90B2A-L002774](../../tests/test_web_agent.py#L2774) | 2774 | `"        monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _q, row=row: [dict(row)])"` | — |
| [SRC-F725E90B2A-L002775](../../tests/test_web_agent.py#L2775) | 2775 | `"        # Current-news questions normally add Google News RSS; keep this unit test deterministic."` | — |
| [SRC-F725E90B2A-L002776](../../tests/test_web_agent.py#L2776) | 2776 | `"        monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L002777](../../tests/test_web_agent.py#L2777) | 2777 | `"        results = agent._search_web(query)"` | — |
| [SRC-F725E90B2A-L002778](../../tests/test_web_agent.py#L2778) | 2778 | `"        assert results, f\"Search candidates were all filtered for case {index}\""` | — |
| [SRC-F725E90B2A-L002779](../../tests/test_web_agent.py#L2779) | 2779 | `"        diagnostic = next("` | — |
| [SRC-F725E90B2A-L002780](../../tests/test_web_agent.py#L2780) | 2780 | `"            item for item in agent._provider_diagnostics if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L002781](../../tests/test_web_agent.py#L2781) | 2781 | `"        )"` | — |
| [SRC-F725E90B2A-L002782](../../tests/test_web_agent.py#L2782) | 2782 | `"        assert diagnostic[\"accepted_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002783](../../tests/test_web_agent.py#L2783) | 2783 | `"        assert diagnostic[\"result_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002784](../../tests/test_web_agent.py#L2784) | 2784 | `""` | — |
| [SRC-F725E90B2A-L002785](../../tests/test_web_agent.py#L2785) | 2785 | `""` | — |
| [SRC-F725E90B2A-L002786](../../tests/test_web_agent.py#L2786) | 2786 | `"def test_search_web_classifies_http_challenge_and_rate_limit_as_provider_degradation(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002787](../../tests/test_web_agent.py#L2787) | 2787 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002788](../../tests/test_web_agent.py#L2788) | 2788 | `""` | — |
| [SRC-F725E90B2A-L002789](../../tests/test_web_agent.py#L2789) | 2789 | `"    def http_202(_query):"` | — |
| [SRC-F725E90B2A-L002790](../../tests/test_web_agent.py#L2790) | 2790 | `"        raise RuntimeError(\"HTTP 202\")"` | — |
| [SRC-F725E90B2A-L002791](../../tests/test_web_agent.py#L2791) | 2791 | `""` | — |
| [SRC-F725E90B2A-L002792](../../tests/test_web_agent.py#L2792) | 2792 | `"    def http_429(_query):"` | — |
| [SRC-F725E90B2A-L002793](../../tests/test_web_agent.py#L2793) | 2793 | `"        raise RuntimeError(\"HTTP 429\")"` | — |
| [SRC-F725E90B2A-L002794](../../tests/test_web_agent.py#L2794) | 2794 | `""` | — |
| [SRC-F725E90B2A-L002795](../../tests/test_web_agent.py#L2795) | 2795 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", http_202)"` | — |
| [SRC-F725E90B2A-L002796](../../tests/test_web_agent.py#L2796) | 2796 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", http_429)"` | — |
| [SRC-F725E90B2A-L002797](../../tests/test_web_agent.py#L2797) | 2797 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L002798](../../tests/test_web_agent.py#L2798) | 2798 | `"        agent._search_web(\"renewable energy storage policy\")"` | — |
| [SRC-F725E90B2A-L002799](../../tests/test_web_agent.py#L2799) | 2799 | `""` | — |
| [SRC-F725E90B2A-L002800](../../tests/test_web_agent.py#L2800) | 2800 | `"    statuses = {"` | — |
| [SRC-F725E90B2A-L002801](../../tests/test_web_agent.py#L2801) | 2801 | `"        item[\"provider\"]: item[\"status\"]"` | — |
| [SRC-F725E90B2A-L002802](../../tests/test_web_agent.py#L2802) | 2802 | `"        for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L002803](../../tests/test_web_agent.py#L2803) | 2803 | `"        if item[\"provider\"] in {\"duckduckgo_html\", \"bing_rss\"}"` | — |
| [SRC-F725E90B2A-L002804](../../tests/test_web_agent.py#L2804) | 2804 | `"    }"` | — |
| [SRC-F725E90B2A-L002805](../../tests/test_web_agent.py#L2805) | 2805 | `"    assert statuses[\"duckduckgo_html\"] == \"http_error\""` | — |
| [SRC-F725E90B2A-L002806](../../tests/test_web_agent.py#L2806) | 2806 | `"    assert statuses[\"bing_rss\"] == \"rate_limited\""` | — |
| [SRC-F725E90B2A-L002807](../../tests/test_web_agent.py#L2807) | 2807 | `""` | — |
| [SRC-F725E90B2A-L002808](../../tests/test_web_agent.py#L2808) | 2808 | `""` | — |
| [SRC-F725E90B2A-L002809](../../tests/test_web_agent.py#L2809) | 2809 | `"def test_search_web_records_distinct_candidate_rejection_reasons(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002810](../../tests/test_web_agent.py#L2810) | 2810 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002811](../../tests/test_web_agent.py#L2811) | 2811 | `"    query = \"renewable energy storage\""` | — |
| [SRC-F725E90B2A-L002812](../../tests/test_web_agent.py#L2812) | 2812 | `"    candidates = ["` | — |
| [SRC-F725E90B2A-L002813](../../tests/test_web_agent.py#L2813) | 2813 | `"        \"malformed candidate\","` | — |
| [SRC-F725E90B2A-L002814](../../tests/test_web_agent.py#L2814) | 2814 | `"        {"` | — |
| [SRC-F725E90B2A-L002815](../../tests/test_web_agent.py#L2815) | 2815 | `"            \"title\": \"Unsafe scheme\","` | — |
| [SRC-F725E90B2A-L002816](../../tests/test_web_agent.py#L2816) | 2816 | `"            \"url\": \"javascript:alert(1)\","` | — |
| [SRC-F725E90B2A-L002817](../../tests/test_web_agent.py#L2817) | 2817 | `"            \"snippet\": \"Renewable energy storage report\","` | — |
| [SRC-F725E90B2A-L002818](../../tests/test_web_agent.py#L2818) | 2818 | `"        },"` | — |
| [SRC-F725E90B2A-L002819](../../tests/test_web_agent.py#L2819) | 2819 | `"        {"` | — |
| [SRC-F725E90B2A-L002820](../../tests/test_web_agent.py#L2820) | 2820 | `"            \"title\": \"Translated mirror\","` | — |
| [SRC-F725E90B2A-L002821](../../tests/test_web_agent.py#L2821) | 2821 | `"            \"url\": \"https://translate.google.com/translate?u=https%3A%2F%2Fexample.com\","` | — |
| [SRC-F725E90B2A-L002822](../../tests/test_web_agent.py#L2822) | 2822 | `"            \"snippet\": \"Renewable energy storage\","` | — |
| [SRC-F725E90B2A-L002823](../../tests/test_web_agent.py#L2823) | 2823 | `"        },"` | — |
| [SRC-F725E90B2A-L002824](../../tests/test_web_agent.py#L2824) | 2824 | `"        {"` | — |
| [SRC-F725E90B2A-L002825](../../tests/test_web_agent.py#L2825) | 2825 | `"            \"title\": \"Gardening tips\","` | — |
| [SRC-F725E90B2A-L002826](../../tests/test_web_agent.py#L2826) | 2826 | `"            \"url\": \"https://example.com/gardening\","` | — |
| [SRC-F725E90B2A-L002827](../../tests/test_web_agent.py#L2827) | 2827 | `"            \"snippet\": \"Gardening flowers and house plants\","` | — |
| [SRC-F725E90B2A-L002828](../../tests/test_web_agent.py#L2828) | 2828 | `"        },"` | — |
| [SRC-F725E90B2A-L002829](../../tests/test_web_agent.py#L2829) | 2829 | `"    ]"` | — |
| [SRC-F725E90B2A-L002830](../../tests/test_web_agent.py#L2830) | 2830 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _q: [dict(x) if isinstance(x, dict) else x for x in candidates])"` | — |
| [SRC-F725E90B2A-L002831](../../tests/test_web_agent.py#L2831) | 2831 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _q: [dict(x) if isinstance(x, dict) else x for x in candidates])"` | — |
| [SRC-F725E90B2A-L002832](../../tests/test_web_agent.py#L2832) | 2832 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L002833](../../tests/test_web_agent.py#L2833) | 2833 | `""` | — |
| [SRC-F725E90B2A-L002834](../../tests/test_web_agent.py#L2834) | 2834 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L002835](../../tests/test_web_agent.py#L2835) | 2835 | `"        agent._search_web(query)"` | — |
| [SRC-F725E90B2A-L002836](../../tests/test_web_agent.py#L2836) | 2836 | `""` | — |
| [SRC-F725E90B2A-L002837](../../tests/test_web_agent.py#L2837) | 2837 | `"    diagnostic = next("` | — |
| [SRC-F725E90B2A-L002838](../../tests/test_web_agent.py#L2838) | 2838 | `"        item for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L002839](../../tests/test_web_agent.py#L2839) | 2839 | `"        if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L002840](../../tests/test_web_agent.py#L2840) | 2840 | `"    )"` | — |
| [SRC-F725E90B2A-L002841](../../tests/test_web_agent.py#L2841) | 2841 | `"    assert diagnostic[\"status\"] == \"filtered_all\""` | — |
| [SRC-F725E90B2A-L002842](../../tests/test_web_agent.py#L2842) | 2842 | `"    assert diagnostic[\"result_count\"] == 4"` | — |
| [SRC-F725E90B2A-L002843](../../tests/test_web_agent.py#L2843) | 2843 | `"    assert diagnostic[\"accepted_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002844](../../tests/test_web_agent.py#L2844) | 2844 | `"    assert diagnostic[\"rejected_count\"] == 4"` | — |
| [SRC-F725E90B2A-L002845](../../tests/test_web_agent.py#L2845) | 2845 | `"    assert diagnostic[\"rejection_counts\"] == {"` | — |
| [SRC-F725E90B2A-L002846](../../tests/test_web_agent.py#L2846) | 2846 | `"        \"malformed_candidate\": 1,"` | — |
| [SRC-F725E90B2A-L002847](../../tests/test_web_agent.py#L2847) | 2847 | `"        \"invalid_url_or_unsafe_target\": 1,"` | — |
| [SRC-F725E90B2A-L002848](../../tests/test_web_agent.py#L2848) | 2848 | `"        \"blocked_domain\": 1,"` | — |
| [SRC-F725E90B2A-L002849](../../tests/test_web_agent.py#L2849) | 2849 | `"        \"relevance_below_threshold\": 1,"` | — |
| [SRC-F725E90B2A-L002850](../../tests/test_web_agent.py#L2850) | 2850 | `"    }"` | — |
| [SRC-F725E90B2A-L002851](../../tests/test_web_agent.py#L2851) | 2851 | `"    assert sum(diagnostic[\"rejection_counts\"].values()) == diagnostic[\"rejected_count\"]"` | — |
| [SRC-F725E90B2A-L002852](../../tests/test_web_agent.py#L2852) | 2852 | `""` | — |
| [SRC-F725E90B2A-L002853](../../tests/test_web_agent.py#L2853) | 2853 | `""` | — |
| [SRC-F725E90B2A-L002854](../../tests/test_web_agent.py#L2854) | 2854 | `"def test_search_web_classifies_http_302_as_degraded_without_following_provider_redirect(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002855](../../tests/test_web_agent.py#L2855) | 2855 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002856](../../tests/test_web_agent.py#L2856) | 2856 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L002857](../../tests/test_web_agent.py#L2857) | 2857 | `""` | — |
| [SRC-F725E90B2A-L002858](../../tests/test_web_agent.py#L2858) | 2858 | `"    def redirect_response(query):"` | — |
| [SRC-F725E90B2A-L002859](../../tests/test_web_agent.py#L2859) | 2859 | `"        calls.append((\"duckduckgo_html\", query))"` | — |
| [SRC-F725E90B2A-L002860](../../tests/test_web_agent.py#L2860) | 2860 | `"        raise RuntimeError(\"HTTP 302\")"` | — |
| [SRC-F725E90B2A-L002861](../../tests/test_web_agent.py#L2861) | 2861 | `""` | — |
| [SRC-F725E90B2A-L002862](../../tests/test_web_agent.py#L2862) | 2862 | `"    def no_results(query):"` | — |
| [SRC-F725E90B2A-L002863](../../tests/test_web_agent.py#L2863) | 2863 | `"        calls.append((\"bing_rss\", query))"` | — |
| [SRC-F725E90B2A-L002864](../../tests/test_web_agent.py#L2864) | 2864 | `"        return []"` | — |
| [SRC-F725E90B2A-L002865](../../tests/test_web_agent.py#L2865) | 2865 | `""` | — |
| [SRC-F725E90B2A-L002866](../../tests/test_web_agent.py#L2866) | 2866 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", redirect_response)"` | — |
| [SRC-F725E90B2A-L002867](../../tests/test_web_agent.py#L2867) | 2867 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", no_results)"` | — |
| [SRC-F725E90B2A-L002868](../../tests/test_web_agent.py#L2868) | 2868 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L002869](../../tests/test_web_agent.py#L2869) | 2869 | `""` | — |
| [SRC-F725E90B2A-L002870](../../tests/test_web_agent.py#L2870) | 2870 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L002871](../../tests/test_web_agent.py#L2871) | 2871 | `"        agent._search_web(\"renewable energy storage\")"` | — |
| [SRC-F725E90B2A-L002872](../../tests/test_web_agent.py#L2872) | 2872 | `""` | — |
| [SRC-F725E90B2A-L002873](../../tests/test_web_agent.py#L2873) | 2873 | `"    diagnostic = next("` | — |
| [SRC-F725E90B2A-L002874](../../tests/test_web_agent.py#L2874) | 2874 | `"        item for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L002875](../../tests/test_web_agent.py#L2875) | 2875 | `"        if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L002876](../../tests/test_web_agent.py#L2876) | 2876 | `"    )"` | — |
| [SRC-F725E90B2A-L002877](../../tests/test_web_agent.py#L2877) | 2877 | `"    assert diagnostic[\"status\"] == \"http_error\""` | — |
| [SRC-F725E90B2A-L002878](../../tests/test_web_agent.py#L2878) | 2878 | `"    assert diagnostic[\"error\"] == \"RuntimeError: HTTP 302\""` | — |
| [SRC-F725E90B2A-L002879](../../tests/test_web_agent.py#L2879) | 2879 | `"    assert sum(provider == \"duckduckgo_html\" for provider, _query in calls) == 1"` | — |
## واجهة الويب

### FILE-DE7EABE998 — [web/agent.html](../../web/agent.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-DE7EABE998-L000001](../../web/agent.html#L1) | 1 | `"<!doctype html>"` | — |
| [SRC-DE7EABE998-L000002](../../web/agent.html#L2) | 2 | `"<html lang=\"ar\" dir=\"rtl\">"` | — |
| [SRC-DE7EABE998-L000003](../../web/agent.html#L3) | 3 | `"<head>"` | — |
| [SRC-DE7EABE998-L000004](../../web/agent.html#L4) | 4 | `"<meta charset=\"utf-8\">"` | — |
| [SRC-DE7EABE998-L000005](../../web/agent.html#L5) | 5 | `"<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">"` | — |
| [SRC-DE7EABE998-L000006](../../web/agent.html#L6) | 6 | `"<meta name=\"theme-color\" content=\"#0a1220\">"` | — |
| [SRC-DE7EABE998-L000007](../../web/agent.html#L7) | 7 | `"<title>Omarai \| وكيل البحث والتحليل</title>"` | — |
| [SRC-DE7EABE998-L000008](../../web/agent.html#L8) | 8 | `"<style>"` | — |
| [SRC-DE7EABE998-L000009](../../web/agent.html#L9) | 9 | `":root{color-scheme:dark;--bg:#0a1220;--panel:#101b2c;--panel2:#132238;--line:#263b55;--text:#f0f5fc;--muted:#9cabc0;--teal:#65e5d0;--blue:#9bbcff;--green:#84e0a9;--amber:#ffd28a;--red:#ff929e;--radius:20px}"` | — |
| [SRC-DE7EABE998-L000010](../../web/agent.html#L10) | 10 | `"*{box-sizing:border-box}"` | — |
| [SRC-DE7EABE998-L000011](../../web/agent.html#L11) | 11 | `"body{margin:0;background:radial-gradient(ellipse at 92% -10%,#173755 0,transparent 38%),radial-gradient(ellipse at 5% 40%,#10273a 0,transparent 32%),var(--bg);color:var(--text);font-family:system-ui,-apple-system,\"Segoe UI\",sans-serif;min-height:100vh}"` | — |
| [SRC-DE7EABE998-L000012](../../web/agent.html#L12) | 12 | `"button,input,textarea{font:inherit}button{cursor:pointer}button:focus-visible,textarea:focus-visible{outline:2px solid var(--teal);outline-offset:2px}"` | — |
| [SRC-DE7EABE998-L000013](../../web/agent.html#L13) | 13 | `".shell{max-width:1240px;margin:auto;padding:18px;min-height:100vh;display:flex;flex-direction:column}"` | — |
| [SRC-DE7EABE998-L000014](../../web/agent.html#L14) | 14 | `".topbar{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:7px 2px 18px;border-bottom:1px solid #26384b}"` | — |
| [SRC-DE7EABE998-L000015](../../web/agent.html#L15) | 15 | `".brand{display:flex;align-items:center;gap:11px;min-width:0}.logo{height:45px;width:45px;border-radius:15px;display:grid;place-items:center;color:#07131e;background:linear-gradient(135deg,#73f0d8,#9bbcff);font-weight:950;font-size:25px;box-shadow:0 8px 30px #67e8df22}"` | — |
| [SRC-DE7EABE998-L000016](../../web/agent.html#L16) | 16 | `".brand h1{font-size:21px;letter-spacing:.2px;margin:0}.brand p{margin:3px 0 0;color:var(--muted);font-size:11px}"` | — |
| [SRC-DE7EABE998-L000017](../../web/agent.html#L17) | 17 | `".top-actions{display:flex;align-items:center;gap:8px}.status{display:flex;gap:8px;align-items:center;padding:8px 11px;border:1px solid var(--line);border-radius:99px;color:var(--muted);font-size:11px}.dot{width:7px;height:7px;border-radius:50%;background:#8394aa;flex:none}.dot.ok{background:var(--green);box-shadow:0 0 11px #84e0a966}.dot.warn{background:var(--amber)}.dot.bad{background:var(--red)}"` | — |
| [SRC-DE7EABE998-L000018](../../web/agent.html#L18) | 18 | `".ghost,.primary{border:1px solid var(--line);border-radius:12px;padding:10px 13px;font-weight:750;font-size:12px}.ghost{color:#d9e6f8;background:#121f32}.ghost:hover{border-color:#50718e}.primary{color:#07131e;border:0;background:linear-gradient(110deg,var(--teal),#acc4ff)}.primary:disabled{opacity:.5;cursor:wait}"` | — |
| [SRC-DE7EABE998-L000019](../../web/agent.html#L19) | 19 | `".hero{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;padding:24px 3px 18px}.eyebrow{color:var(--teal);font-size:11px;font-weight:850;letter-spacing:.55px}.hero h2{font-size:clamp(26px,4vw,37px);line-height:1.35;margin:7px 0 9px;letter-spacing:-.6px}.hero h2 span{color:var(--teal)}.hero p{font-size:13px;line-height:1.9;color:var(--muted);margin:0;max-width:760px}.trust{width:230px;flex:none;border:1px solid #28524f;background:#0c2629;border-radius:16px;padding:13px 15px;color:#b5f7e8;font-size:11px;line-height:1.8}.trust b{display:block;color:#e4fffa;font-size:12px;margin-bottom:3px}"` | — |
| [SRC-DE7EABE998-L000020](../../web/agent.html#L20) | 20 | `".layout{display:grid;grid-template-columns:minmax(0,1fr) 286px;gap:15px;align-items:start;flex:1}"` | — |
| [SRC-DE7EABE998-L000021](../../web/agent.html#L21) | 21 | `".chatpanel,.sidepanel{border:1px solid var(--line);background:linear-gradient(150deg,#111e30f5,#0d1727f5);border-radius:var(--radius);overflow:hidden;box-shadow:0 24px 70px #0002}"` | — |
| [SRC-DE7EABE998-L000022](../../web/agent.html#L22) | 22 | `".chatpanel{display:flex;flex-direction:column;min-height:600px}.chathead{padding:15px 17px;border-bottom:1px solid #24384f;display:flex;align-items:center;justify-content:space-between;gap:12px}.chathead h3{font-size:14px;margin:0}.chathead p{font-size:11px;color:var(--muted);margin:4px 0 0}.live-tag{display:flex;align-items:center;gap:7px;color:#b9fff2;background:#102a2e;border:1px solid #245358;padding:7px 10px;border-radius:99px;font-size:10px;white-space:nowrap}"` | — |
| [SRC-DE7EABE998-L000023](../../web/agent.html#L23) | 23 | `".modebar{display:flex;align-items:center;gap:7px;flex-wrap:wrap;padding:12px 15px;border-bottom:1px solid #24384f;background:#0d1827}.mode-label{color:var(--muted);font-size:11px;margin-left:3px}.mode-btn{color:#c3d3e8;border:1px solid #2b4059;background:#101f32;border-radius:99px;padding:8px 11px;font-size:11px;font-weight:700;transition:.16s}.mode-btn:hover{border-color:#5b86a5}.mode-btn.active{color:#07131e;border-color:transparent;background:linear-gradient(110deg,var(--teal),#a8c1ff)}"` | — |
| [SRC-DE7EABE998-L000024](../../web/agent.html#L24) | 24 | `".messages{padding:18px;display:flex;flex-direction:column;gap:18px;min-height:360px;max-height:calc(100vh - 360px);overflow:auto;scroll-behavior:smooth}.welcome{margin:auto 0;text-align:center;padding:25px 10px}.welcome-icon{width:58px;height:58px;border-radius:19px;display:grid;place-items:center;margin:0 auto 14px;background:#142c3c;border:1px solid #2c5561;color:var(--teal);font-size:26px}.welcome h3{font-size:19px;margin:0 0 8px}.welcome p{font-size:12px;color:var(--muted);line-height:1.9;max-width:470px;margin:0 auto 19px}.suggestions{display:flex;flex-wrap:wrap;justify-content:center;gap:8px}.suggestions button{font-size:11px;line-height:1.65;color:#c4d6ec;border:1px solid #2b4059;background:#101f32;padding:10px 12px;border-radius:12px}.suggestions button:hover{color:white;border-color:var(--teal)}"` | — |
| [SRC-DE7EABE998-L000025](../../web/agent.html#L25) | 25 | `".message{display:flex;flex-direction:column;gap:8px;align-self:stretch;max-width:100%;min-width:0}.message.user{align-self:flex-end;max-width:88%;width:max-content}.who{font-size:10px;color:var(--muted);padding:0 3px;display:flex;align-items:center;gap:7px}.bubble{color:#e6eef9;background:#111f32;border:1px solid #2a405a;border-radius:15px 15px 15px 4px;padding:14px 16px;line-height:1.95;font-size:13px;overflow-wrap:anywhere}.user .bubble{background:#123039;border-color:#2b5759;border-radius:15px 15px 4px 15px;white-space:pre-wrap}.bubble h3{font-size:14px;color:#e8fffb;margin:15px 0 5px}.bubble h4{font-size:13px;color:#dce8fc;margin:12px 0 4px}.bubble strong{color:#f6fbff}.bubble ul{margin:6px 0;padding-inline-start:20px}.bubble li{margin:4px 0}.bubble a{color:#b4d4ff}"` | — |
| [SRC-DE7EABE998-L000026](../../web/agent.html#L26) | 26 | `".pending{display:flex;align-items:center;gap:10px;color:#b5c7dc}.spinner{width:17px;height:17px;border:2px solid #2c485a;border-top-color:var(--teal);border-radius:50%;animation:spin .85s linear infinite;flex:none}@keyframes spin{to{transform:rotate(360deg)}}"` | — |
| [SRC-DE7EABE998-L000027](../../web/agent.html#L27) | 27 | `".report{border:1px solid #30465f;background:#0b1726;border-radius:15px;padding:13px;margin-top:3px}.report-head{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:10px}.report-head b{font-size:12px}.coverage{border:1px solid #315950;background:#102926;border-radius:99px;padding:5px 9px;color:#b9ffeb;font-size:10px;font-weight:800;white-space:nowrap}"` | — |
| [SRC-DE7EABE998-L000028](../../web/agent.html#L28) | 28 | `".metrics{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}.metric{background:#111f31;border:1px solid #273c55;padding:10px;border-radius:12px;min-width:0}.metric strong{display:block;font-size:20px;line-height:1.35;color:var(--teal);font-weight:850}.metric span{display:block;font-size:10px;color:var(--muted);margin-top:3px;line-height:1.5}.report-note{font-size:11px;color:#b7c8dc;line-height:1.8;margin:10px 0 0}.providers{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}.provider{border:1px solid #2d425b;background:#102035;color:#c3d5ea;border-radius:99px;padding:5px 8px;font-size:9px}"` | — |
| [SRC-DE7EABE998-L000029](../../web/agent.html#L29) | 29 | `".details{margin-top:9px;border:1px solid #2b4059;background:#0d1929;border-radius:12px;padding:10px 12px;font-size:11px;color:#c6d5e7;line-height:1.8}.details summary{cursor:pointer;color:#b9f8eb;font-weight:700}.details ol{margin:8px 0 0;padding-inline-start:22px}.details li{overflow-wrap:anywhere;margin:4px 0}"` | — |
| [SRC-DE7EABE998-L000030](../../web/agent.html#L30) | 30 | `".warning{border:1px solid #6c5831;background:#292216;color:#ffdfa2;padding:11px 13px;border-radius:12px;font-size:11px;line-height:1.85}.sources{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:9px;margin-top:4px}.source{border:1px solid #293e56;background:#0b1726;border-radius:13px;padding:12px;min-width:0;display:flex;flex-direction:column;gap:6px}.source a{color:#c2d9ff;text-decoration:none;font-weight:800;font-size:11px;line-height:1.75;overflow-wrap:anywhere}.source a:hover{text-decoration:underline;color:white}.source p{color:#acbdd1;font-size:11px;line-height:1.8;margin:0;overflow-wrap:anywhere}.source-meta{display:flex;gap:5px;flex-wrap:wrap;margin-top:auto;padding-top:4px}.tag{border:1px solid #31435a;background:#132237;border-radius:99px;padding:4px 7px;color:#aabbd0;font-size:9px}.tag.read{border-color:#28574b;background:#102821;color:#9deac6}.tag.social{border-color:#594c37;color:#f0cc8f}.no-sources{font-size:11px;color:var(--muted);margin-top:6px}"` | — |
| [SRC-DE7EABE998-L000031](../../web/agent.html#L31) | 31 | `".composer{padding:14px;border-top:1px solid #24384f;background:#0b1523}.inputwrap{display:flex;align-items:flex-end;gap:9px;padding:8px;border:1px solid #314861;border-radius:16px;background:#07111e}.inputwrap:focus-within{border-color:var(--teal);box-shadow:0 0 0 3px #65e5d00e}.inputwrap textarea{flex:1;min-width:0;max-height:150px;min-height:48px;resize:vertical;color:var(--text);background:transparent;border:0;outline:0;padding:10px;font-size:13px;line-height:1.8}.inputwrap textarea::placeholder{color:#7186a0}.send{min-height:44px;min-width:82px}.hint{color:#7589a2;font-size:10px;line-height:1.8;margin:8px 5px 1px}"` | — |
| [SRC-DE7EABE998-L000032](../../web/agent.html#L32) | 32 | `".sidepanel{padding:16px}.sidepanel h3{font-size:13px;margin:0 0 12px}.sideblock{padding:13px 0;border-bottom:1px solid #24374d}.sideblock:first-child{padding-top:0}.sideblock:last-child{border-bottom:0;padding-bottom:0}.sideblock p{font-size:11px;color:var(--muted);line-height:1.9;margin:0}.sidefeature{display:flex;gap:9px;align-items:flex-start;margin:12px 0}.sideicon{flex:none;width:29px;height:29px;display:grid;place-items:center;background:#142b3c;border:1px solid #2a475d;border-radius:9px;color:var(--teal);font-size:13px}.sidefeature b{display:block;font-size:11px;margin:0 0 3px}.sidefeature span{display:block;color:var(--muted);font-size:10px;line-height:1.7}"` | — |
| [SRC-DE7EABE998-L000033](../../web/agent.html#L33) | 33 | `".checkbutton{width:100%;margin-top:10px}.diag{font-size:10px;line-height:1.8;color:#b7c9de;white-space:pre-wrap;overflow-wrap:anywhere;margin:10px 0 0}.config-label{display:inline-block;color:var(--teal);border:1px solid #27534f;background:#0e2827;border-radius:99px;padding:4px 8px;font-size:9px;margin-top:6px}.foot{text-align:center;font-size:10px;color:#71859c;line-height:1.8;padding:16px 4px}"` | — |
| [SRC-DE7EABE998-L000034](../../web/agent.html#L34) | 34 | `"@media(max-width:950px){.layout{grid-template-columns:minmax(0,1fr) 245px}.trust{width:200px}.metrics{grid-template-columns:repeat(2,minmax(0,1fr))}}"` | — |
| [SRC-DE7EABE998-L000035](../../web/agent.html#L35) | 35 | `"@media(max-width:740px){.shell{padding:10px}.layout{grid-template-columns:1fr}.sidepanel{order:2}.hero{align-items:stretch;flex-direction:column;padding:19px 3px 14px}.trust{width:auto}.hero h2{font-size:28px}.topbar{padding-bottom:13px}.brand h1{font-size:19px}.status{display:none}.chatpanel{min-height:70vh}.messages{max-height:unset;min-height:350px;padding:12px}.sidepanel{padding:14px}.sources{grid-template-columns:1fr}.message.user{max-width:94%}.chathead{padding:13px}.modebar{padding:10px;gap:6px}.mode-btn{padding:8px 10px}.composer{padding:10px}.inputwrap{gap:5px}.send{min-width:65px;padding:9px}.bubble{padding:12px;font-size:12px}}"` | — |
| [SRC-DE7EABE998-L000036](../../web/agent.html#L36) | 36 | `"@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;scroll-behavior:auto!important;transition:none!important}}"` | — |
| [SRC-DE7EABE998-L000037](../../web/agent.html#L37) | 37 | `".message-context{margin:0 0 9px;padding:8px 10px;border-inline-start:3px solid var(--teal);border-radius:8px;background:rgba(40,190,170,.07);color:var(--muted);font-size:11px;line-height:1.7;overflow-wrap:anywhere}.retry-row{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}.retry-button{border:1px solid #496780;border-radius:10px;background:#152c40;color:var(--text);font:inherit;font-size:12px;font-weight:700;padding:9px 12px;cursor:pointer}.retry-button:focus-visible{outline:2px solid var(--teal);outline-offset:2px}.retry-button:hover{border-color:var(--teal)}"` | — |
| [SRC-DE7EABE998-L000038](../../web/agent.html#L38) | 38 | `"</style>"` | — |
| [SRC-DE7EABE998-L000039](../../web/agent.html#L39) | 39 | `"</head>"` | — |
| [SRC-DE7EABE998-L000040](../../web/agent.html#L40) | 40 | `"<body>"` | — |
| [SRC-DE7EABE998-L000041](../../web/agent.html#L41) | 41 | `"<div class=\"shell\">"` | — |
| [SRC-DE7EABE998-L000042](../../web/agent.html#L42) | 42 | `"<header class=\"topbar\">"` | — |
| [SRC-DE7EABE998-L000043](../../web/agent.html#L43) | 43 | `"  <div class=\"brand\"><div class=\"logo\" aria-hidden=\"true\">O</div><div><h1>Omarai</h1><p>وكيل البحث الحي والتحليل متعدد المصادر</p></div></div>"` | — |
| [SRC-DE7EABE998-L000044](../../web/agent.html#L44) | 44 | `"  <div class=\"top-actions\"><div class=\"status\" id=\"status\" role=\"status\"><span class=\"dot\"></span><span>يفحص الإعداد...</span></div><button class=\"ghost\" id=\"clear\" type=\"button\">بحث جديد ↻</button></div>"` | — |
| [SRC-DE7EABE998-L000045](../../web/agent.html#L45) | 45 | `"</header>"` | — |
| [SRC-DE7EABE998-L000046](../../web/agent.html#L46) | 46 | `""` | — |
| [SRC-DE7EABE998-L000047](../../web/agent.html#L47) | 47 | `"<section class=\"hero\">"` | — |
| [SRC-DE7EABE998-L000048](../../web/agent.html#L48) | 48 | `"  <div><span class=\"eyebrow\">بحث حي · مصادر قابلة للمراجعة · تحليل واضح</span><h2>من السؤال إلى <span>صورة أوضح مدعومة بالأدلة</span></h2><p>اكتب سؤالك بطريقتك الطبيعية. يبحث Omarai عبر محركات ويب ومصادر عامة متاحة، يقرأ الصفحات التي تسمح بالوصول، ويقارن تنوع المصادر وحداثتها ونوعها قبل صياغة إجابة بروابط واضحة. لا يعتبر عدد النتائج وحده إثباتًا للحقيقة.</p></div>"` | — |
| [SRC-DE7EABE998-L000049](../../web/agent.html#L49) | 49 | `"  <div class=\"trust\"><b>◈ شفافية الأدلة أولًا</b>سترى عدد المصادر والنطاقات والصفحات المقروءة ومحركات البحث المستخدمة، مع التنبيه إلى الفجوات. مؤشرات التغطية تصف البحث ولا تمثل احتمال صحة المعلومة.</div>"` | — |
| [SRC-DE7EABE998-L000050](../../web/agent.html#L50) | 50 | `"</section>"` | — |
| [SRC-DE7EABE998-L000051](../../web/agent.html#L51) | 51 | `""` | — |
| [SRC-DE7EABE998-L000052](../../web/agent.html#L52) | 52 | `"<main class=\"layout\">"` | — |
| [SRC-DE7EABE998-L000053](../../web/agent.html#L53) | 53 | `"  <section class=\"chatpanel\" aria-label=\"واجهة البحث\">"` | — |
| [SRC-DE7EABE998-L000054](../../web/agent.html#L54) | 54 | `"    <div class=\"chathead\"><div><h3>مساحة البحث والتحليل</h3><p>تُرسل أسئلة البحث إلى محركات الإنترنت، وقد تُرسل مقتطفات المصادر إلى مزود نموذج اللغة المضبوط.</p></div><span class=\"live-tag\"><span class=\"dot\"></span> بحث ويب</span></div>"` | — |
| [SRC-DE7EABE998-L000055](../../web/agent.html#L55) | 55 | `"    <div class=\"modebar\" role=\"group\" aria-label=\"نمط البحث\">"` | — |
| [SRC-DE7EABE998-L000056](../../web/agent.html#L56) | 56 | `"      <span class=\"mode-label\">عمق البحث:</span>"` | — |
| [SRC-DE7EABE998-L000057](../../web/agent.html#L57) | 57 | `"      <button class=\"mode-btn\" data-mode=\"auto\" type=\"button\">تلقائي</button>"` | — |
| [SRC-DE7EABE998-L000058](../../web/agent.html#L58) | 58 | `"      <button class=\"mode-btn active\" data-mode=\"deep\" type=\"button\" aria-pressed=\"true\">بحث معمّق</button>"` | — |
| [SRC-DE7EABE998-L000059](../../web/agent.html#L59) | 59 | `"      <button class=\"mode-btn\" data-mode=\"latest\" type=\"button\">الأحدث الآن</button>"` | — |
| [SRC-DE7EABE998-L000060](../../web/agent.html#L60) | 60 | `"      <button class=\"mode-btn\" data-mode=\"social\" type=\"button\">آراء الناس</button>"` | — |
| [SRC-DE7EABE998-L000061](../../web/agent.html#L61) | 61 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000062](../../web/agent.html#L62) | 62 | `"    <div class=\"messages\" id=\"messages\" aria-live=\"polite\">"` | — |
| [SRC-DE7EABE998-L000063](../../web/agent.html#L63) | 63 | `"      <div class=\"welcome\" id=\"welcome\"><div class=\"welcome-icon\">⌕</div><h3>ما الذي تريد أن تبحث عنه؟</h3><p>ابدأ بسؤال أو مهمة بحث. اختر بحثًا معمقًا لتوسيع زوايا البحث، أو «الأحدث الآن» للمعلومات الزمنية، أو «آراء الناس» للمحتوى الاجتماعي العام المتاح.</p><div class=\"suggestions\"><button type=\"button\">حلّل أحدث تطورات وكلاء الذكاء الاصطناعي مع المصادر</button><button type=\"button\">قارن سوق العقارات في التجمع والعاصمة الإدارية بالأدلة</button><button type=\"button\">اجمع آراء وتجارب عامة حول منتج أو خدمة</button></div></div>"` | — |
| [SRC-DE7EABE998-L000064](../../web/agent.html#L64) | 64 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000065](../../web/agent.html#L65) | 65 | `"    <div class=\"composer\"><div class=\"inputwrap\"><textarea id=\"question\" rows=\"2\" maxlength=\"4000\" placeholder=\"اسأل باللهجة المصرية أو العربية الفصحى أو الإنجليزية…\"></textarea><button class=\"primary send\" id=\"send\" type=\"button\">ابحث ←</button></div><div class=\"hint\">Enter للإرسال · Shift + Enter لسطر جديد · لا تضع كلمات مرور أو مفاتيح API أو بيانات شخصية سرية داخل السؤال.</div></div>"` | — |
| [SRC-DE7EABE998-L000066](../../web/agent.html#L66) | 66 | `"  </section>"` | — |
| [SRC-DE7EABE998-L000067](../../web/agent.html#L67) | 67 | `""` | — |
| [SRC-DE7EABE998-L000068](../../web/agent.html#L68) | 68 | `"  <aside class=\"sidepanel\">"` | — |
| [SRC-DE7EABE998-L000069](../../web/agent.html#L69) | 69 | `"    <div class=\"sideblock\">"` | — |
| [SRC-DE7EABE998-L000070](../../web/agent.html#L70) | 70 | `"      <h3>الوصول الآمن إلى النسخة المستضافة</h3>"` | — |
| [SRC-DE7EABE998-L000071](../../web/agent.html#L71) | 71 | `"      <label for=\"accessToken\" style=\"display:block;font-size:11px;color:#b9c9dc;margin:9px 0\">رمز الوصول الخاص بالتطبيق</label>"` | — |
| [SRC-DE7EABE998-L000072](../../web/agent.html#L72) | 72 | `"      <input id=\"accessToken\" type=\"password\" autocomplete=\"off\" spellcheck=\"false\" placeholder=\"أدخل رمز الاستضافة الذي أنشأته\" style=\"width:100%;padding:11px;border:1px solid #314861;border-radius:11px;background:#07111e;color:var(--text);font-size:12px\">"` | — |
| [SRC-DE7EABE998-L000073](../../web/agent.html#L73) | 73 | `"      <button id=\"saveAccessToken\" type=\"button\" class=\"ghost checkbutton\">حفظ الرمز على هذا الجهاز</button>"` | — |
| [SRC-DE7EABE998-L000074](../../web/agent.html#L74) | 74 | `"      <p style=\"font-size:10px;color:var(--muted);line-height:1.8;margin-top:7px\">لا تضع مفتاح OpenRouter هنا. هذا رمز منفصل لحماية تطبيقك المستضاف، ويُحفظ محليًا في متصفحك فقط.</p>"` | — |
| [SRC-DE7EABE998-L000075](../../web/agent.html#L75) | 75 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000076](../../web/agent.html#L76) | 76 | `"    <div class=\"sideblock\">"` | — |
| [SRC-DE7EABE998-L000077](../../web/agent.html#L77) | 77 | `"      <h3>حالة الاتصال الفعلية</h3>"` | — |
| [SRC-DE7EABE998-L000078](../../web/agent.html#L78) | 78 | `"      <p id=\"setupStatus\">جارٍ فحص إعدادات الخادم. إعداد المحرك لا يعني أن البحث الحي نجح بعد؛ استخدم الاختبار أدناه للتحقق من الاتصال الفعلي.</p>"` | — |
| [SRC-DE7EABE998-L000079](../../web/agent.html#L79) | 79 | `"      <label style=\"display:flex;gap:8px;align-items:flex-start;margin:11px 0;font-size:10px;color:#b9c9dc;line-height:1.7\"><input id=\"diagSocial\" type=\"checkbox\" style=\"margin-top:3px\"> اختبار المصادر الاجتماعية العامة والموصلات المهيأة أيضًا</label>"` | — |
| [SRC-DE7EABE998-L000080](../../web/agent.html#L80) | 80 | `"      <button id=\"runDiagnostics\" type=\"button\" class=\"primary checkbutton\">اختبار حي للإنترنت والنموذج</button>"` | — |
| [SRC-DE7EABE998-L000081](../../web/agent.html#L81) | 81 | `"      <p id=\"diagnosticsResult\" class=\"diag\" aria-live=\"polite\"></p>"` | — |
| [SRC-DE7EABE998-L000082](../../web/agent.html#L82) | 82 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000083](../../web/agent.html#L83) | 83 | `"    <div class=\"sideblock\">"` | — |
| [SRC-DE7EABE998-L000084](../../web/agent.html#L84) | 84 | `"      <h3>مصادر البحث</h3>"` | — |
| [SRC-DE7EABE998-L000085](../../web/agent.html#L85) | 85 | `"      <div class=\"sidefeature\"><div class=\"sideicon\">⌕</div><div><b>محركات الويب</b><span>DuckDuckGo وBing؛ ويمكن إضافة Brave وTavily بمفتاح API اختياري.</span></div></div>"` | — |
| [SRC-DE7EABE998-L000086](../../web/agent.html#L86) | 86 | `"      <div class=\"sidefeature\"><div class=\"sideicon\">▤</div><div><b>الأخبار والمصادر العامة</b><span>Google News عند طلب معلومات حديثة، وقراءة الصفحات التي تسمح بالوصول العام.</span></div></div>"` | — |
| [SRC-DE7EABE998-L000087](../../web/agent.html#L87) | 87 | `"      <div class=\"sidefeature\"><div class=\"sideicon\">◎</div><div><b>الشبكات الاجتماعية</b><span>مصادر عامة موصولة فعليًا أو نتائج مفهرسة؛ ليست تغطية كاملة لكل المنصات أو المنشورات.</span></div></div>"` | — |
| [SRC-DE7EABE998-L000088](../../web/agent.html#L88) | 88 | `"      <div id=\"providerSetup\"></div>"` | — |
| [SRC-DE7EABE998-L000089](../../web/agent.html#L89) | 89 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000090](../../web/agent.html#L90) | 90 | `"    <div class=\"sideblock\">"` | — |
| [SRC-DE7EABE998-L000091](../../web/agent.html#L91) | 91 | `"      <h3>كيف تقرأ النتيجة؟</h3>"` | — |
| [SRC-DE7EABE998-L000092](../../web/agent.html#L92) | 92 | `"      <p>تنوع النطاقات ومحركات البحث والصفحات المقروءة وتواريخ النشر إشارات إلى مدى تغطية البحث، لا دليلًا قاطعًا على صحة الادعاء. افتح المصادر المهمة، وانتبه إلى التضارب والمعلومات غير المؤرخة.</p>"` | — |
| [SRC-DE7EABE998-L000093](../../web/agent.html#L93) | 93 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000094](../../web/agent.html#L94) | 94 | `"  </aside>"` | — |
| [SRC-DE7EABE998-L000095](../../web/agent.html#L95) | 95 | `"</main>"` | — |
| [SRC-DE7EABE998-L000096](../../web/agent.html#L96) | 96 | `"<footer class=\"foot\">Omarai · لا يتجاوز تسجيل الدخول أو الصفحات الخاصة أو الحواجز المدفوعة، ولا يرسل رسائل تلقائية. الإتاحة الفعلية تعتمد على اتصال الإنترنت، وحدود محركات البحث، ومفاتيح الخدمات الاختيارية.</footer>"` | — |
| [SRC-DE7EABE998-L000097](../../web/agent.html#L97) | 97 | `"</div>"` | — |
| [SRC-DE7EABE998-L000098](../../web/agent.html#L98) | 98 | `""` | — |
| [SRC-DE7EABE998-L000099](../../web/agent.html#L99) | 99 | `"<script>"` | — |
| [SRC-DE7EABE998-L000100](../../web/agent.html#L100) | 100 | `"const $=id=>document.getElementById(id);"` | — |
| [SRC-DE7EABE998-L000101](../../web/agent.html#L101) | 101 | `"const ACCESS_TOKEN_STORAGE_KEY=\"omarai_access_token\";"` | — |
| [SRC-DE7EABE998-L000102](../../web/agent.html#L102) | 102 | `"function apiHeaders(){const headers={\"Content-Type\":\"application/json\"};const token=($(\"accessToken\")?.value\|\|localStorage.getItem(ACCESS_TOKEN_STORAGE_KEY)\|\|\"\").trim();if(token)headers.Authorization=\"Bearer \"+token;return headers;}"` | — |
| [SRC-DE7EABE998-L000103](../../web/agent.html#L103) | 103 | `"const history=[];"` | — |
| [SRC-DE7EABE998-L000104](../../web/agent.html#L104) | 104 | `"let busy=false;"` | — |
| [SRC-DE7EABE998-L000105](../../web/agent.html#L105) | 105 | `"let activeMode=\"deep\";"` | — |
| [SRC-DE7EABE998-L000106](../../web/agent.html#L106) | 106 | `"const modeLabels={auto:\"تلقائي\",deep:\"بحث معمّق\",latest:\"الأحدث الآن\",social:\"آراء الناس\"};"` | — |
| [SRC-DE7EABE998-L000107](../../web/agent.html#L107) | 107 | `"function escapeHtml(s){return String(s??\"\").replace(/[&<>\"']/g,c=>({\"&\":\"&amp;\",\"<\":\"&lt;\",\">\":\"&gt;\",'\"':\"&quot;\",\"'\":\"&#39;\"}[c]));}"` | — |
| [SRC-DE7EABE998-L000108](../../web/agent.html#L108) | 108 | `"function answerMarkup(text){"` | — |
| [SRC-DE7EABE998-L000109](../../web/agent.html#L109) | 109 | `"  const escaped=escapeHtml(text);"` | — |
| [SRC-DE7EABE998-L000110](../../web/agent.html#L110) | 110 | `"  return escaped"` | — |
| [SRC-DE7EABE998-L000111](../../web/agent.html#L111) | 111 | `"   .replace(/^###\\s+(.+)$/gm,\"<h3>$1</h3>\")"` | — |
| [SRC-DE7EABE998-L000112](../../web/agent.html#L112) | 112 | `"   .replace(/^##\\s+(.+)$/gm,\"<h3>$1</h3>\")"` | — |
| [SRC-DE7EABE998-L000113](../../web/agent.html#L113) | 113 | `"   .replace(/^#\\s+(.+)$/gm,\"<h3>$1</h3>\")"` | — |
| [SRC-DE7EABE998-L000114](../../web/agent.html#L114) | 114 | `"   .replace(/^\\s*[-*]\\s+(.+)$/gm,\"• $1\")"` | — |
| [SRC-DE7EABE998-L000115](../../web/agent.html#L115) | 115 | `"   .replace(/\\*\\*(.+?)\\*\\*/g,\"<strong>$1</strong>\")"` | — |
| [SRC-DE7EABE998-L000116](../../web/agent.html#L116) | 116 | ``"   .replace(/`([^`]+)`/g,\"<code>$1</code>\")"`` | — |
| [SRC-DE7EABE998-L000117](../../web/agent.html#L117) | 117 | `"   .replace(/\\n/g,\"<br>\");"` | — |
| [SRC-DE7EABE998-L000118](../../web/agent.html#L118) | 118 | `"}"` | — |
| [SRC-DE7EABE998-L000119](../../web/agent.html#L119) | 119 | `"function setStatus(text,kind){$(\"status\").innerHTML='<span class=\"dot '+(kind\|\|\"\")+'\"></span><span>'+escapeHtml(text)+'</span>';}"` | — |
| [SRC-DE7EABE998-L000120](../../web/agent.html#L120) | 120 | `"function modeName(mode){return modeLabels[mode]\|\|modeLabels.auto;}"` | — |
| [SRC-DE7EABE998-L000121](../../web/agent.html#L121) | 121 | `"function safeSourceUrl(value){"` | — |
| [SRC-DE7EABE998-L000122](../../web/agent.html#L122) | 122 | `" try{"` | — |
| [SRC-DE7EABE998-L000123](../../web/agent.html#L123) | 123 | `"  const parsed=new URL(String(value??\"\"));"` | — |
| [SRC-DE7EABE998-L000124](../../web/agent.html#L124) | 124 | `"  if(![\"https:\",\"http:\"].includes(parsed.protocol)\|\|!parsed.hostname\|\|parsed.username\|\|parsed.password)return null;"` | — |
| [SRC-DE7EABE998-L000125](../../web/agent.html#L125) | 125 | `"  return parsed.href;"` | — |
| [SRC-DE7EABE998-L000126](../../web/agent.html#L126) | 126 | `" }catch(_error){return null;}"` | — |
| [SRC-DE7EABE998-L000127](../../web/agent.html#L127) | 127 | `"}"` | — |
| [SRC-DE7EABE998-L000128](../../web/agent.html#L128) | 128 | `"function renderSource(s,index){"` | — |
| [SRC-DE7EABE998-L000129](../../web/agent.html#L129) | 129 | `" if(!s\|\|typeof s!==\"object\")return \"\";"` | — |
| [SRC-DE7EABE998-L000130](../../web/agent.html#L130) | 130 | `" const url=safeSourceUrl(s.url);"` | — |
| [SRC-DE7EABE998-L000131](../../web/agent.html#L131) | 131 | `" const title=escapeHtml(s.title\|\|(\"نتيجة ويب \"+(index+1)));"` | — |
| [SRC-DE7EABE998-L000132](../../web/agent.html#L132) | 132 | `" const tags=[];"` | — |
| [SRC-DE7EABE998-L000133](../../web/agent.html#L133) | 133 | `" tags.push('<span class=\"tag\">'+escapeHtml(s.source_class\|\|\"مصدر عام\")+'</span>');"` | — |
| [SRC-DE7EABE998-L000134](../../web/agent.html#L134) | 134 | `" const fetchStatus=s.page_fetch_status\|\|(s.page_fetched?\"content_extracted\":\"not_attempted\");"` | — |
| [SRC-DE7EABE998-L000135](../../web/agent.html#L135) | 135 | `" if(fetchStatus===\"partial_extraction\")tags.push('<span class=\"tag read\">اُستخرج جزء من النص فقط</span>');"` | — |
| [SRC-DE7EABE998-L000136](../../web/agent.html#L136) | 136 | `" else if(fetchStatus===\"content_extracted\"\|\|s.page_fetched)tags.push('<span class=\"tag read\">قُرئت الصفحة واستُخرج نص</span>');"` | — |
| [SRC-DE7EABE998-L000137](../../web/agent.html#L137) | 137 | `" else if(fetchStatus===\"no_text_extracted\"\|\|fetchStatus===\"empty_content\")tags.push('<span class=\"tag\">لم يُستخرج نص؛ قد تكون الصفحة ديناميكية أو محجوبة</span>');"` | — |
| [SRC-DE7EABE998-L000138](../../web/agent.html#L138) | 138 | `" else if(fetchStatus===\"blocked_or_unresolved_host\"\|\|fetchStatus===\"blocked_connection_target\")tags.push('<span class=\"tag\">حُظر العنوان أو تعذّر التحقق الآمن منه</span>');"` | — |
| [SRC-DE7EABE998-L000139](../../web/agent.html#L139) | 139 | `" else if([\"redirect_failed\",\"redirect_rejected\",\"redirect_limit\"].includes(fetchStatus))tags.push('<span class=\"tag\">تعذّر اتباع تحويل الرابط بأمان</span>');"` | — |
| [SRC-DE7EABE998-L000140](../../web/agent.html#L140) | 140 | `" else if(fetchStatus===\"http_error\")tags.push('<span class=\"tag\">الموقع أعاد خطأ HTTP</span>');"` | — |
| [SRC-DE7EABE998-L000141](../../web/agent.html#L141) | 141 | `" else if(fetchStatus===\"unsupported_content_type\")tags.push('<span class=\"tag\">نوع محتوى الصفحة غير مدعوم</span>');"` | — |
| [SRC-DE7EABE998-L000142](../../web/agent.html#L142) | 142 | `" else if(fetchStatus===\"page_too_large\")tags.push('<span class=\"tag\">الصفحة تجاوزت حد الحجم الآمن</span>');"` | — |
| [SRC-DE7EABE998-L000143](../../web/agent.html#L143) | 143 | `" else if(fetchStatus===\"network_error\")tags.push('<span class=\"tag\">تعذّر الاتصال بالصفحة</span>');"` | — |
| [SRC-DE7EABE998-L000144](../../web/agent.html#L144) | 144 | `" else if(fetchStatus===\"budget_exhausted\")tags.push('<span class=\"tag\">توقفت القراءة بسبب حدود الموارد</span>');"` | — |
| [SRC-DE7EABE998-L000145](../../web/agent.html#L145) | 145 | `" else if(fetchStatus===\"rejected_url\")tags.push('<span class=\"tag\">رُفض الرابط لأسباب أمان</span>');"` | — |
| [SRC-DE7EABE998-L000146](../../web/agent.html#L146) | 146 | `" else if(fetchStatus===\"fetch_failed\")tags.push('<span class=\"tag\">تعذّر جلب الصفحة</span>');"` | — |
| [SRC-DE7EABE998-L000147](../../web/agent.html#L147) | 147 | `" else if(fetchStatus===\"attempted\")tags.push('<span class=\"tag\">محاولة جلب الصفحة</span>');"` | — |
| [SRC-DE7EABE998-L000148](../../web/agent.html#L148) | 148 | `" else tags.push('<span class=\"tag\">مقتطف بحث — لم تُحاول قراءة الصفحة</span>');"` | — |
| [SRC-DE7EABE998-L000149](../../web/agent.html#L149) | 149 | `" if(s.platform&&s.platform!==\"web\")tags.push('<span class=\"tag social\">'+escapeHtml(s.platform)+'</span>');"` | — |
| [SRC-DE7EABE998-L000150](../../web/agent.html#L150) | 150 | `" if(s.published_at)tags.push('<span class=\"tag\">تاريخ ظاهر: '+escapeHtml(s.published_at)+'</span>');"` | — |
| [SRC-DE7EABE998-L000151](../../web/agent.html#L151) | 151 | `" const providers=Array.isArray(s.providers)?s.providers.map(escapeHtml):[];"` | — |
| [SRC-DE7EABE998-L000152](../../web/agent.html#L152) | 152 | `" if(s.publisher_name)tags.push('<span class=\"tag\">الناشر: '+escapeHtml(s.publisher_name)+'</span>');"` | — |
| [SRC-DE7EABE998-L000153](../../web/agent.html#L153) | 153 | `" if(s.publisher_url&&safeSourceUrl(s.publisher_url))tags.push('<a class=\"tag\" href=\"'+escapeHtml(s.publisher_url)+'\" target=\"_blank\" rel=\"noopener noreferrer\">صفحة الناشر ↗</a>');"` | — |
| [SRC-DE7EABE998-L000154](../../web/agent.html#L154) | 154 | `" if(providers.length)tags.push('<span class=\"tag\">'+providers.join(\" · \")+'</span>');"` | — |
| [SRC-DE7EABE998-L000155](../../web/agent.html#L155) | 155 | `" if(s.lead_qualification===\"related_result_not_lead\")tags.push('<span class=\"tag social\">نتيجة مرتبطة وليست عميلًا محتملًا</span>');"` | — |
| [SRC-DE7EABE998-L000156](../../web/agent.html#L156) | 156 | `" if(s.lead_qualification===\"public_buyer_intent_signal\")tags.push('<span class=\"tag read\">إشارة علنية محتملة لنية شراء؛ الهوية غير متحققة</span>');"` | — |
| [SRC-DE7EABE998-L000157](../../web/agent.html#L157) | 157 | `" const heading=url?'<a href=\"'+escapeHtml(url)+'\" target=\"_blank\" rel=\"noopener noreferrer\">['+(index+1)+'] '+title+' ↗</a>':'<strong>['+(index+1)+'] '+title+'</strong><p class=\"warning\">لم يُعرض الرابط لأنه غير صالح.</p>';"` | — |
| [SRC-DE7EABE998-L000158](../../web/agent.html#L158) | 158 | `" return '<article class=\"source\">'+heading+'<p>'+escapeHtml(s.snippet\|\|\"لا يتوفر مقتطف نصي من هذه النتيجة.\")+'</p><div class=\"source-meta\">'+tags.join(\"\")+'</div></article>';"` | — |
| [SRC-DE7EABE998-L000159](../../web/agent.html#L159) | 159 | `"}"` | — |
| [SRC-DE7EABE998-L000160](../../web/agent.html#L160) | 160 | `"function renderReport(result){"` | — |
| [SRC-DE7EABE998-L000161](../../web/agent.html#L161) | 161 | `" const r=result&&result.search_report&&typeof result.search_report===\"object\"?result.search_report:{};"` | — |
| [SRC-DE7EABE998-L000162](../../web/agent.html#L162) | 162 | `" const e=r.evidence_signals&&typeof r.evidence_signals===\"object\"?r.evidence_signals:{};"` | — |
| [SRC-DE7EABE998-L000163](../../web/agent.html#L163) | 163 | `" const sources=Array.isArray(result.sources)?result.sources:[];"` | — |
| [SRC-DE7EABE998-L000164](../../web/agent.html#L164) | 164 | `" const researchErrorOutcome=[\"attempted_research_error\",\"unknown_after_research_error\"].includes(r.search_outcome);"` | — |
| [SRC-DE7EABE998-L000165](../../web/agent.html#L165) | 165 | `" const lead=r.lead_generation&&typeof r.lead_generation===\"object\"?r.lead_generation:null;"` | — |
| [SRC-DE7EABE998-L000166](../../web/agent.html#L166) | 166 | `" const leadResearchIncomplete=!!lead&&lead.status===\"research_incomplete\";"` | — |
| [SRC-DE7EABE998-L000167](../../web/agent.html#L167) | 167 | `" const leadSignalCount=lead&&lead.candidate_signal_count!==null&&lead.candidate_signal_count!==undefined&&Number.isFinite(Number(lead.candidate_signal_count))?Number(lead.candidate_signal_count):null;"` | — |
| [SRC-DE7EABE998-L000168](../../web/agent.html#L168) | 168 | `" const noQualifiedLeads=!!lead&&!leadResearchIncomplete&&leadSignalCount===0;"` | — |
| [SRC-DE7EABE998-L000169](../../web/agent.html#L169) | 169 | `" const scoreLabel=lead?(leadResearchIncomplete?\"تعذر حسم البحث عن العملاء\":noQualifiedLeads?\"لم يُثبت وجود عميل محتمل\":\"إشارات نية شراء مرشحة\"):(researchErrorOutcome?\"تعذر تحديد التغطية\":(e.coverage_level\|\|\"تغطية محدودة\"));"` | — |
| [SRC-DE7EABE998-L000170](../../web/agent.html#L170) | 170 | `" const metrics=lead?["` | — |
| [SRC-DE7EABE998-L000171](../../web/agent.html#L171) | 171 | `"  [leadSignalCount??\"غير محدد\",\"إشارة نصية مرشحة لنية شراء\"],"` | — |
| [SRC-DE7EABE998-L000172](../../web/agent.html#L172) | 172 | `"  [lead.related_results_reviewed??\"غير محدد\",\"نتيجة تمت مراجعتها\"],"` | — |
| [SRC-DE7EABE998-L000173](../../web/agent.html#L173) | 173 | `"  [r.pages_fetched??(leadResearchIncomplete?\"غير محدد\":0),\"صفحة قُرئت\"],"` | — |
| [SRC-DE7EABE998-L000174](../../web/agent.html#L174) | 174 | `"  [leadResearchIncomplete?\"غير محدد\":(e.providers_count??(Array.isArray(r.providers_used)?r.providers_used.length:0)),\"واجهة أسهمت بمصدر صالح\"]"` | — |
| [SRC-DE7EABE998-L000175](../../web/agent.html#L175) | 175 | `" ]:["` | — |
| [SRC-DE7EABE998-L000176](../../web/agent.html#L176) | 176 | `"  [researchErrorOutcome?(r.unique_sources??\"غير محدد\"):(r.unique_sources??sources.length),\"مصدرًا فريدًا\"],"` | — |
| [SRC-DE7EABE998-L000177](../../web/agent.html#L177) | 177 | `"  [researchErrorOutcome?\"غير محدد\":(e.unique_domains??\"—\"),\"نطاقًا مختلفًا\"],"` | — |
| [SRC-DE7EABE998-L000178](../../web/agent.html#L178) | 178 | `"  [researchErrorOutcome?(r.pages_fetched??\"غير محدد\"):(r.pages_fetched??e.pages_read??0),\"صفحة قُرئت\"],"` | — |
| [SRC-DE7EABE998-L000179](../../web/agent.html#L179) | 179 | `"  [researchErrorOutcome?\"غير محدد\":(e.providers_count??(Array.isArray(r.providers_used)?r.providers_used.length:0)),\"واجهة أسهمت بمصدر صالح\"]"` | — |
| [SRC-DE7EABE998-L000180](../../web/agent.html#L180) | 180 | `" ];"` | — |
| [SRC-DE7EABE998-L000181](../../web/agent.html#L181) | 181 | `" const metricHtml=metrics.map(([v,l])=>'<div class=\"metric\"><strong>'+escapeHtml(v)+'</strong><span>'+escapeHtml(l)+'</span></div>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000182](../../web/agent.html#L182) | 182 | `" const operationalMetrics=["` | — |
| [SRC-DE7EABE998-L000183](../../web/agent.html#L183) | 183 | `"  [r.provider_candidates_received??\"غير محدد\",\"مرشح أعاده محرك البحث قبل التصفية (قد يتكرر)\"],"` | — |
| [SRC-DE7EABE998-L000184](../../web/agent.html#L184) | 184 | `"  [r.provider_candidates_accepted??\"غير محدد\",\"مرشح اجتاز فحص الموصل قبل الدمج\"],"` | — |
| [SRC-DE7EABE998-L000185](../../web/agent.html#L185) | 185 | `"  [r.provider_candidates_rejected??\"غير محدد\",\"مرشح رُفض بفحص الرابط أو الصلة\"],"` | — |
| [SRC-DE7EABE998-L000186](../../web/agent.html#L186) | 186 | `"  [r.raw_results??\"غير محدد\",\"نتيجة جُمعت قبل دمج التكرارات\"],"` | — |
| [SRC-DE7EABE998-L000187](../../web/agent.html#L187) | 187 | `"  [r.unique_urls??r.unique_sources??sources.length,\"رابط فريد بعد الدمج\"],"` | — |
| [SRC-DE7EABE998-L000188](../../web/agent.html#L188) | 188 | `"  [r.pages_fetch_attempted??\"غير محدد\",\"محاولة جلب صفحة\"],"` | — |
| [SRC-DE7EABE998-L000189](../../web/agent.html#L189) | 189 | `"  [r.pages_content_extracted??r.pages_fetched??\"غير محدد\",\"صفحة استُخرج منها نص\"],"` | — |
| [SRC-DE7EABE998-L000190](../../web/agent.html#L190) | 190 | `"  [r.pages_partial_extracted??\"غير محدد\",\"صفحة استُخرج جزء من نصها\"],"` | — |
| [SRC-DE7EABE998-L000191](../../web/agent.html#L191) | 191 | `"  [r.pages_extract_failed??\"غير محدد\",\"صفحة فشل استخراج نصها\"]"` | — |
| [SRC-DE7EABE998-L000192](../../web/agent.html#L192) | 192 | `" ];"` | — |
| [SRC-DE7EABE998-L000193](../../web/agent.html#L193) | 193 | `" const operationalHtml='<div class=\"metrics\">'+operationalMetrics.map(([v,l])=>'<div class=\"metric\"><strong>'+escapeHtml(v)+'</strong><span>'+escapeHtml(l)+'</span></div>').join(\"\")+'</div>';"` | — |
| [SRC-DE7EABE998-L000194](../../web/agent.html#L194) | 194 | `" const connectors=r.connector_summary&&Array.isArray(r.connector_summary.connectors)?r.connector_summary.connectors:[];"` | — |
| [SRC-DE7EABE998-L000195](../../web/agent.html#L195) | 195 | `" const connectorDetails=connectors.length?'<details class=\"details\"><summary>تشخيص الموصلات في هذا الطلب ('+connectors.length+')</summary><div>'+connectors.map(c=>'<article class=\"source\"><strong>'+escapeHtml(c.name\|\|\"موصل\")+' · '+escapeHtml(c.status\|\|\"unknown\")+'</strong><p>الإعداد: '+escapeHtml(c.configuration_status\|\|\"unknown\")+' · تمت المحاولة: '+escapeHtml(c.attempted===true?\"نعم\":c.attempted===false?\"لا\":\"غير محسوم\")+' · متاح في هذا الطلب: '+escapeHtml(c.available_for_this_request===true?\"نعم\":c.available_for_this_request===false?\"لا\":\"غير محسوم\")+' · استجابة المعالجة مؤكدة: '+escapeHtml(c.verified_for_this_request===true?\"نعم\":c.verified_for_this_request===false?\"لا\":\"غير مختبر/غير محسوم\")+' · إخفاق ملاحظ: '+escapeHtml(c.failure_observed===true?\"نعم\":\"لا\")+' · مرشحون أوليون من الموصل: '+escapeHtml(c.result_count??\"غير محدد\")+' · اجتازوا فحص الموصل: '+escapeHtml(c.accepted_count??\"غير محدد\")+' · مصادر نهائية منسوبة إليه: '+escapeHtml(c.useful_result_count??\"غير محدد\")+' · مرفوض: '+escapeHtml(c.rejected_count??\"غير محدد\")+' · توزيع الرفض: '+escapeHtml(c.rejection_counts_observed===true&&c.rejection_counts?('مرشح مشوّه '+(c.rejection_counts.malformed_candidate??0)+'؛ رابط غير صالح/هدف غير آمن '+(c.rejection_counts.invalid_url_or_unsafe_target??0)+'؛ نطاق محظور '+(c.rejection_counts.blocked_domain??0)+'؛ صلة ضعيفة '+(c.rejection_counts.relevance_below_threshold??0)):'غير مسجل في هذه الجولة')+' · كل المرشحين رُفضوا: '+escapeHtml(c.candidate_rejection_observed===true?\"نعم\":c.candidate_rejection_observed===false?\"لا\":\"غير محسوم\")+'</p>'+((Array.isArray(c.queries)&&c.queries.length)?'<p>استعلامات: '+c.queries.map(escapeHtml).join(\" · \")+'</p>':\"\")+((Array.isArray(c.errors)&&c.errors.length)?'<p class=\"warning\">أخطاء: '+c.errors.map(escapeHtml).join(\" · \")+'</p>':\"\")+'</article>').join(\"\")+'</div></details>':\"\";"` | — |
| [SRC-DE7EABE998-L000196](../../web/agent.html#L196) | 196 | `" const integrity=r.answer_integrity&&typeof r.answer_integrity===\"object\"?r.answer_integrity:null;"` | — |
| [SRC-DE7EABE998-L000197](../../web/agent.html#L197) | 197 | `" const integrityNumbers=integrity&&Array.isArray(integrity.potentially_unsupported_numeric_literals)?integrity.potentially_unsupported_numeric_literals:[];"` | — |
| [SRC-DE7EABE998-L000198](../../web/agent.html#L198) | 198 | `" const integrityTargets=integrity&&Array.isArray(integrity.target_coverage)?integrity.target_coverage:[];"` | — |
| [SRC-DE7EABE998-L000199](../../web/agent.html#L199) | 199 | `" const citationNumericSupport=integrity&&Array.isArray(integrity.citation_numeric_support)?integrity.citation_numeric_support:[];"` | — |
| [SRC-DE7EABE998-L000200](../../web/agent.html#L200) | 200 | `" const citedNumberIssues=citationNumericSupport.filter(item=>item&&Array.isArray(item.potentially_unsupported_numeric_literals)&&item.potentially_unsupported_numeric_literals.length);"` | — |
| [SRC-DE7EABE998-L000201](../../web/agent.html#L201) | 201 | `" const citedNumberHtml=citedNumberIssues.length?'<p class=\"warning\">وجد الفحص أرقامًا قد لا يسندها المصدر المحدد في الاستشهاد؛ راجع المقتطف أو نص الصفحة الأصلي.</p><ul>'+citedNumberIssues.map(item=>'<li>الجملة '+escapeHtml(item.sentence_number??\"غير محدد\")+' · الرقم: '+item.potentially_unsupported_numeric_literals.map(escapeHtml).join(\"، \")+' · الاستشهادات: '+(Array.isArray(item.cited_source_indexes)?item.cited_source_indexes.map(n=>'المصدر '+escapeHtml(n)).join(\"، \"):\"غير محددة\")+'</li>').join(\"\")+'</ul>':\"\";"` | — |
| [SRC-DE7EABE998-L000202](../../web/agent.html#L202) | 202 | `" const valueDiscrepancies=integrity&&Array.isArray(integrity.potential_value_discrepancies)?integrity.potential_value_discrepancies:[];"` | — |
| [SRC-DE7EABE998-L000203](../../web/agent.html#L203) | 203 | `" const valueDimensionLabels={price_or_cost:\"السعر/التكلفة\",area_or_size:\"المساحة/الحجم\",duration:\"المدة\",percentage_or_rate:\"النسبة\",date_or_year:\"التاريخ/السنة\"};"` | — |
| [SRC-DE7EABE998-L000204](../../web/agent.html#L204) | 204 | `" const valueDiscrepancyHtml=valueDiscrepancies.length?'<p class=\"warning\">رُصدت قيم مختلفة في مصادر متعددة. قد يكون الاختلاف بين منتجات أو فترات أو وحدات مختلفة؛ هذه ليست إثباتًا تلقائيًا لوجود تناقض.</p><ul>'+valueDiscrepancies.map(item=>'<li>'+escapeHtml(valueDimensionLabels[item.dimension]\|\|item.dimension\|\|\"قيمة\")+' — '+(Array.isArray(item.values)?item.values.map(value=>escapeHtml(value.value)+' ('+(Array.isArray(value.source_indexes)?value.source_indexes.map(n=>'المصدر '+escapeHtml(n)).join(\"، \"):\"مصدر غير محدد\")+')').join(' مقابل '):\"قِيَم تحتاج مراجعة\")+'</li>').join(\"\")+'</ul>':\"\";"` | — |
| [SRC-DE7EABE998-L000205](../../web/agent.html#L205) | 205 | `" const citationAlignment=integrity&&Array.isArray(integrity.citation_lexical_alignment)?integrity.citation_lexical_alignment:[];"` | — |
| [SRC-DE7EABE998-L000206](../../web/agent.html#L206) | 206 | `" const weakCitationAlignment=citationAlignment.filter(item=>item&&item.status===\"weak_lexical_overlap\");"` | — |
| [SRC-DE7EABE998-L000207](../../web/agent.html#L207) | 207 | `" const citationAlignmentHtml=citationAlignment.length?'<p class=\"report-note\">'+(weakCitationAlignment.length?'لم يظهر تطابق لفظي كافٍ في '+weakCitationAlignment.length+' جملة/جمل مستشهد بها؛ راجع الاستشهادات يدويًا.':'ظهرت إشارات تطابق لفظي لبعض الجمل المستشهد بها، لكنها لا تثبت أن المصدر يسند الادعاء.')+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000208](../../web/agent.html#L208) | 208 | `" const integrityScope=integrity?({contains_extracted_page_text_and_or_snippets:\"نص صفحات مستخرج مع مقتطفات بحث\",search_snippets_only:\"مقتطفات بحث فقط — لم يؤكد النظام قراءة نص الصفحات\",no_readable_source_text:\"لا يتوفر نص مصدر قابل للفحص\"}[integrity.source_evidence_scope]\|\|integrity.source_evidence_scope\|\|\"غير محدد\"):\"غير محدد\";"` | — |
| [SRC-DE7EABE998-L000209](../../web/agent.html#L209) | 209 | `" const integritySummary=integrity?'<p class=\"report-note\">عدادات الفحص اللفظي: '+escapeHtml(integrity.potentially_unsupported_numeric_count??0)+' رقم لم يظهر نصيًا في الأدلة؛ '+escapeHtml(integrity.potentially_unsupported_numeric_by_citation_count??0)+' رقم لا يسنده المصدر المشار إليه تحديدًا؛ '+escapeHtml(integrity.potential_value_discrepancy_count??0)+' اختلاف قيمة يحتاج مطابقة؛ '+escapeHtml(integrity.potentially_missing_target_count??0)+' محور محتمل النقص.</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000210](../../web/agent.html#L210) | 210 | `" const taskFulfillmentStatus=r.task_fulfillment_status\|\|result.task_fulfillment_status\|\|\"not_machine_assessed_no_explicit_targets_detected\";"` | — |
| [SRC-DE7EABE998-L000211](../../web/agent.html#L211) | 211 | `" const taskFulfillmentText=({"` | — |
| [SRC-DE7EABE998-L000212](../../web/agent.html#L212) | 212 | `"  possible_gap_detected:\"قد تكون الإجابة أغفلت محورًا من السؤال؛ هذه إشارة لفظية تحتاج مراجعة وليست حكمًا نهائيًا.\","` | — |
| [SRC-DE7EABE998-L000213](../../web/agent.html#L213) | 213 | `"  lexical_signals_found_not_semantically_verified:\"ظهرت إشارات لفظية للمحاور المستخرجة، لكن هذا لا يثبت اكتمال المهمة.\","` | — |
| [SRC-DE7EABE998-L000214](../../web/agent.html#L214) | 214 | `"  not_assessed_insufficient_evidence:\"الأدلة غير كافية؛ لم يتم التحقق من اكتمال المهمة.\","` | — |
| [SRC-DE7EABE998-L000215](../../web/agent.html#L215) | 215 | `"  not_machine_assessed_no_explicit_targets_detected:\"لم تُستخرج محاور صريحة قابلة للفحص؛ اكتمال المهمة لم يُقيّم آليًا.\""` | — |
| [SRC-DE7EABE998-L000216](../../web/agent.html#L216) | 216 | `" })[taskFulfillmentStatus]\|\|\"حالة اكتمال المهمة غير محسومة آليًا.\";"` | — |
| [SRC-DE7EABE998-L000217](../../web/agent.html#L217) | 217 | `" const taskFulfillmentHtml='<p class=\"'+(taskFulfillmentStatus===\"possible_gap_detected\"?\"warning\":\"report-note\")+'\">حالة تنفيذ المطلوب: '+escapeHtml(taskFulfillmentText)+'</p>';"` | — |
| [SRC-DE7EABE998-L000218](../../web/agent.html#L218) | 218 | `" const coverageRepairStatus=r.coverage_repair_status\|\|result.coverage_repair_status\|\|\"\";"` | — |
| [SRC-DE7EABE998-L000219](../../web/agent.html#L219) | 219 | `" const coverageRepairMessages={"` | — |
| [SRC-DE7EABE998-L000220](../../web/agent.html#L220) | 220 | `"  revised_and_reaudited:\"عُدّلت الإجابة بعد رصد محور محتمل النقص ثم خضعت لمراجعة أدلة ثانية؛ تظل المراجعة بمساعدة نموذج وليست تحققًا مستقلًا.\","` | — |
| [SRC-DE7EABE998-L000221](../../web/agent.html#L221) | 221 | `"  reaudit_budget_exhausted:\"انتهت ميزانية النماذج قبل إعادة تدقيق الإجابة المعدلة؛ عُرضت مقتطفات المصادر بدل اعتبار النص المعدل إجابة مكتملة.\","` | — |
| [SRC-DE7EABE998-L000222](../../web/agent.html#L222) | 222 | `"  reaudit_unavailable:\"تعذرت إعادة تدقيق الإجابة المعدلة؛ عُرضت مقتطفات المصادر بدل اعتبار النص المعدل إجابة مكتملة.\","` | — |
| [SRC-DE7EABE998-L000223](../../web/agent.html#L223) | 223 | `"  budget_exhausted:\"انتهت ميزانية النماذج قبل استكمال محور محتمل النقص.\","` | — |
| [SRC-DE7EABE998-L000224](../../web/agent.html#L224) | 224 | `"  unavailable:\"تعذرت محاولة إصلاح محور محتمل النقص.\","` | — |
| [SRC-DE7EABE998-L000225](../../web/agent.html#L225) | 225 | `"  no_change_gap_unresolved:\"لم تغيّر محاولة الإصلاح الإجابة؛ لا يزال احتمال نقص أحد المحاور قائمًا.\""` | — |
| [SRC-DE7EABE998-L000226](../../web/agent.html#L226) | 226 | `" };"` | — |
| [SRC-DE7EABE998-L000227](../../web/agent.html#L227) | 227 | `" const coverageRepairHtml=coverageRepairMessages[coverageRepairStatus]?'<p class=\"warning\">حالة إصلاح التغطية: '+escapeHtml(coverageRepairMessages[coverageRepairStatus])+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000228](../../web/agent.html#L228) | 228 | `" const integrityHtml=integrity?'<details class=\"details\"><summary>فحص لفظي أولي: اتساق الإجابة مع الأدلة — ليس تحققًا من الحقيقة</summary><p class=\"report-note\">لا يثبت هذا الفحص صحة الوقائع أو دلالة الاستشهاد. نطاق الأدلة النصية: '+escapeHtml(integrityScope)+'.</p>'+integritySummary+taskFulfillmentHtml+coverageRepairHtml+'<p class=\"report-note\">'+(integrityNumbers.length?'أرقام أو تواريخ تحتاج مراجعة لأنها لم تظهر نصيًا في المواد المتاحة: '+integrityNumbers.map(escapeHtml).join(\"، \")+'.':'لم يرصد الفحص أرقامًا محددة غائبة عن النصوص التي جمعها. هذا لا يثبت أن كل رقم صحيح أو أن المصدر يدعم الادعاء المرتبط به.')+'</p>'+citedNumberHtml+valueDiscrepancyHtml+citationAlignmentHtml+(integrityTargets.length?'<p class=\"report-note\">إشارات التغطية اللفظية لمحاور السؤال:</p><ul>'+integrityTargets.map(t=>'<li>'+escapeHtml(t.target\|\|\"محور\")+' — '+escapeHtml(t.status===\"lexical_signal_found\"?\"وُجد تطابق لفظي؛ ليس إثباتًا لاكتمال الإجابة\":\"قد يكون هذا المحور ناقصًا؛ لم يظهر تطابق لفظي كافٍ\")+'</li>').join(\"\")+'</ul>':\"\")+'<p class=\"report-note\">المنهج: فحص لفظي حتمي محدود. لا يتحقق من معنى الادعاء أو صلة الاستشهاد به أو استقلال المصادر؛ راجع الأدلة الأصلية قبل الاعتماد.</p></details>':\"\";"` | — |
| [SRC-DE7EABE998-L000229](../../web/agent.html#L229) | 229 | `" const providerCounts=r.provider_counts&&typeof r.provider_counts===\"object\"&&!Array.isArray(r.provider_counts)?r.provider_counts:{};"` | — |
| [SRC-DE7EABE998-L000230](../../web/agent.html#L230) | 230 | `" const providerHtml=Object.entries(providerCounts).map(([p,n])=>'<span class=\"provider\">'+escapeHtml(p)+' · '+escapeHtml(n)+'</span>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000231](../../web/agent.html#L231) | 231 | `" const notes=Array.isArray(e.warnings)?e.warnings:[];"` | — |
| [SRC-DE7EABE998-L000232](../../web/agent.html#L232) | 232 | `" const queryList=Array.isArray(result.search_queries)?result.search_queries:[];"` | — |
| [SRC-DE7EABE998-L000233](../../web/agent.html#L233) | 233 | `" const details=queryList.length?'<details class=\"details\"><summary>زوايا البحث المستخدمة ('+queryList.length+')</summary><ol>'+queryList.map(q=>'<li>'+escapeHtml(q)+'</li>').join(\"\")+'</ol></details>':\"\";"` | — |
| [SRC-DE7EABE998-L000234](../../web/agent.html#L234) | 234 | `" const coverageText=lead"` | — |
| [SRC-DE7EABE998-L000235](../../web/agent.html#L235) | 235 | `"  ? (leadResearchIncomplete"` | — |
| [SRC-DE7EABE998-L000236](../../web/agent.html#L236) | 236 | `"     ? \"تعطل البحث أو لم يكتمل التقرير؛ الأعداد غير المتاحة ليست صفرًا، ولا يمكن استنتاج عدم وجود عملاء.\""` | — |
| [SRC-DE7EABE998-L000237](../../web/agent.html#L237) | 237 | `"     : noQualifiedLeads"` | — |
| [SRC-DE7EABE998-L000238](../../web/agent.html#L238) | 238 | `"      ? \"لم تثبت النتائج وجود أي عميل محتمل. عدد صفحات العقارات أو النطاقات ليس عدد المشترين.\""` | — |
| [SRC-DE7EABE998-L000239](../../web/agent.html#L239) | 239 | `"      : \"الإشارات العلنية لا تثبت هوية الشخص أو استمرار رغبته في الشراء؛ راجع نص المصدر وتاريخه يدويًا.\")"` | — |
| [SRC-DE7EABE998-L000240](../../web/agent.html#L240) | 240 | `"  : researchErrorOutcome"` | — |
| [SRC-DE7EABE998-L000241](../../web/agent.html#L241) | 241 | `"   ? \"تعذر تحديد تغطية البحث لأن مسار تجميع الأدلة لم يكتمل؛ الأرقام غير المتاحة ليست صفرًا.\""` | — |
| [SRC-DE7EABE998-L000242](../../web/agent.html#L242) | 242 | `"   : \"تغطية الأدلة: \"+scoreLabel+\" — يصف هذا الوصف اتساع الأدلة المتاحة ولا يمثل احتمال صحة الإجابة.\";"` | — |
| [SRC-DE7EABE998-L000243](../../web/agent.html#L243) | 243 | `" const usableSourceCount=researchErrorOutcome?null:(r.usable_sources_after_filtering??sources.length);"` | — |
| [SRC-DE7EABE998-L000244](../../web/agent.html#L244) | 244 | `" const attemptText=result&&result.search_attempted===true"` | — |
| [SRC-DE7EABE998-L000245](../../web/agent.html#L245) | 245 | `"  ? (r.search_outcome===\"attempted_research_error\""` | — |
| [SRC-DE7EABE998-L000246](../../web/agent.html#L246) | 246 | `"     ? \"بدأت محاولة البحث، لكن تعطل مسار تجميع الأدلة قبل اكتمال التقرير؛ لم يمكن تحديد عدد المصادر القابلة للاستخدام.\""` | — |
| [SRC-DE7EABE998-L000247](../../web/agent.html#L247) | 247 | `"     : \"تمت محاولة البحث في الويب. عدد المصادر القابلة للاستخدام بعد التصفية: \"+(usableSourceCount??\"غير محدد\")+\".\")"` | — |
| [SRC-DE7EABE998-L000248](../../web/agent.html#L248) | 248 | `"  : result&&result.search_attempted===false"` | — |
| [SRC-DE7EABE998-L000249](../../web/agent.html#L249) | 249 | `"   ? \"لم تُنفّذ محاولة بحث ويب في هذه الجولة.\""` | — |
| [SRC-DE7EABE998-L000250](../../web/agent.html#L250) | 250 | `"   : r.search_outcome===\"unknown_after_research_error\""` | — |
| [SRC-DE7EABE998-L000251](../../web/agent.html#L251) | 251 | `"    ? \"تعطل مسار البحث، ولم يمكن تأكيد ما إذا كانت محاولة البحث قد بدأت أو كم مصدرًا كان قابلًا للاستخدام.\""` | — |
| [SRC-DE7EABE998-L000252](../../web/agent.html#L252) | 252 | `"    : \"حالة محاولة البحث غير موضحة في الاستجابة.\";"` | — |
| [SRC-DE7EABE998-L000253](../../web/agent.html#L253) | 253 | `" const qualityText='تصنيف جودة البحث يصف تغطية العملية والأدلة المتاحة، ولا يمثل احتمال صحة الوقائع.';"` | — |
| [SRC-DE7EABE998-L000254](../../web/agent.html#L254) | 254 | `" const reviewText=r.claim_audit_semantics==='model_assisted_not_independent_fact_check'?'مراجعة الادعاءات تمت بمساعدة نموذج لغوي؛ وهي ليست تحققًا مستقلًا من صحة الحقائق.':'لم يثبت إجراء تحقق مستقل من صحة الحقائق.';"` | — |
| [SRC-DE7EABE998-L000255](../../web/agent.html#L255) | 255 | `" const diversityText='اختلاف النطاقات المسجلة لا يثبت الاستقلال التحريري؛ فقد تنقل المواقع عن مصدر أصلي واحد.';"` | — |
| [SRC-DE7EABE998-L000256](../../web/agent.html#L256) | 256 | `" const reportNotes=[coverageText,attemptText,qualityText,reviewText,diversityText,...notes].map(n=>'<p class=\"report-note\">'+escapeHtml(n)+'</p>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000257](../../web/agent.html#L257) | 257 | `" const review=r.second_pass_review===\"model_claim_audit_completed\"?\"مراجعة الادعاءات بمساعدة النموذج تمت (ليست تحققًا مستقلًا)\":r.second_pass_review===\"model_claim_audit_completed_before_coverage_repair\"?\"تمت مراجعة المسودة قبل تعديل التغطية؛ النسخة المعدلة لم تخضع لمراجعة ثانية\":r.second_pass_review===\"model_claim_audit_unavailable\"?\"تعذرت مراجعة الادعاءات بمساعدة النموذج\":\"\";"` | — |
| [SRC-DE7EABE998-L000258](../../web/agent.html#L258) | 258 | `" return '<div class=\"report-head\"><b>ملخص الأدلة وتغطية البحث</b><span class=\"coverage\">'+escapeHtml(scoreLabel)+'</span></div><div class=\"metrics\">'+metricHtml+'</div>'+operationalHtml+connectorDetails+integrityHtml+reportNotes+(providerHtml?'<div class=\"providers\">'+providerHtml+'</div>':\"\")+(review?'<p class=\"report-note\">'+escapeHtml(review)+'</p>':\"\")+details;"` | — |
| [SRC-DE7EABE998-L000259](../../web/agent.html#L259) | 259 | `"}"` | — |
| [SRC-DE7EABE998-L000260](../../web/agent.html#L260) | 260 | `"function addMessage(role,text,result,options={}){"` | — |
| [SRC-DE7EABE998-L000261](../../web/agent.html#L261) | 261 | `" const welcome=$(\"welcome\");if(welcome)welcome.remove();"` | — |
| [SRC-DE7EABE998-L000262](../../web/agent.html#L262) | 262 | `" const box=document.createElement(\"div\");box.className=\"message \"+(role===\"user\"?\"user\":\"assistant\");"` | — |
| [SRC-DE7EABE998-L000263](../../web/agent.html#L263) | 263 | `" const who=document.createElement(\"div\");who.className=\"who\";"` | — |
| [SRC-DE7EABE998-L000264](../../web/agent.html#L264) | 264 | `" who.textContent=role===\"user\"?\"أنت\":(result&&result.used_language_model?\"Omarai · بحث وتحليل توليدي\":\"Omarai · إجابة جزئية أو احتياطية\");"` | — |
| [SRC-DE7EABE998-L000265](../../web/agent.html#L265) | 265 | `" box.appendChild(who);"` | — |
| [SRC-DE7EABE998-L000266](../../web/agent.html#L266) | 266 | `" const linkedQuestion=(options&&options.question)\|\|(result&&result.question);"` | — |
| [SRC-DE7EABE998-L000267](../../web/agent.html#L267) | 267 | `" if(role===\"assistant\"&&linkedQuestion){"` | — |
| [SRC-DE7EABE998-L000268](../../web/agent.html#L268) | 268 | `"  const context=document.createElement(\"div\");context.className=\"message-context\";"` | — |
| [SRC-DE7EABE998-L000269](../../web/agent.html#L269) | 269 | `"  context.textContent=\"ردًا على السؤال: \"+linkedQuestion;box.appendChild(context);"` | — |
| [SRC-DE7EABE998-L000270](../../web/agent.html#L270) | 270 | `" }"` | — |
| [SRC-DE7EABE998-L000271](../../web/agent.html#L271) | 271 | `" const bubble=document.createElement(\"div\");bubble.className=\"bubble\";bubble.innerHTML=answerMarkup(text);box.appendChild(bubble);"` | — |
| [SRC-DE7EABE998-L000272](../../web/agent.html#L272) | 272 | `" if(result&&result.used_web_search!==true&&result.kind!==\"general_answer\"&&result.kind!==\"capability_answer\"){"` | — |
| [SRC-DE7EABE998-L000273](../../web/agent.html#L273) | 273 | `"  const notice=document.createElement(\"div\");notice.className=\"warning\";"` | — |
| [SRC-DE7EABE998-L000274](../../web/agent.html#L274) | 274 | `"  notice.textContent=result.search_attempted===true?\"نُفذت محاولة بحث، لكن لم يؤكد النظام توفر مصادر قابلة للاستخدام؛ تعامل مع الإجابة باعتبارها غير مكتملة حتى مراجعة المصادر.\":result.search_attempted===false?\"لم تُنفذ محاولة بحث ويب في هذه الجولة؛ لا تعتبر الإجابة نتيجة بحث حي.\":\"لم يؤكد النظام نجاح البحث الحي في هذه الجولة؛ تعامل مع الإجابة باعتبارها غير مكتملة حتى مراجعة المصادر.\";"` | — |
| [SRC-DE7EABE998-L000275](../../web/agent.html#L275) | 275 | `"  box.appendChild(notice);"` | — |
| [SRC-DE7EABE998-L000276](../../web/agent.html#L276) | 276 | `" }"` | — |
| [SRC-DE7EABE998-L000277](../../web/agent.html#L277) | 277 | `" if(result&&result.used_language_model!==true&&result.kind!==\"general_answer\"&&result.kind!==\"capability_answer\"){"` | — |
| [SRC-DE7EABE998-L000278](../../web/agent.html#L278) | 278 | `"  const notice=document.createElement(\"div\");notice.className=\"warning\";"` | — |
| [SRC-DE7EABE998-L000279](../../web/agent.html#L279) | 279 | `"  notice.textContent=\"لم تُستخدم استجابة مؤكدة من النموذج اللغوي؛ قد تكون الإجابة مقتطفات أو ردًا احتياطيًا وليست تحليلًا توليديًا كاملًا.\";"` | — |
| [SRC-DE7EABE998-L000280](../../web/agent.html#L280) | 280 | `"  box.appendChild(notice);"` | — |
| [SRC-DE7EABE998-L000281](../../web/agent.html#L281) | 281 | `" }"` | — |
| [SRC-DE7EABE998-L000282](../../web/agent.html#L282) | 282 | `" if(result&&result.search_report){"` | — |
| [SRC-DE7EABE998-L000283](../../web/agent.html#L283) | 283 | `"  const report=document.createElement(\"section\");report.className=\"report\";report.innerHTML=renderReport(result);box.appendChild(report);"` | — |
| [SRC-DE7EABE998-L000284](../../web/agent.html#L284) | 284 | `" }"` | — |
| [SRC-DE7EABE998-L000285](../../web/agent.html#L285) | 285 | `" if(result&&Array.isArray(result.warnings)&&result.warnings.length){"` | — |
| [SRC-DE7EABE998-L000286](../../web/agent.html#L286) | 286 | `"  const warning=document.createElement(\"div\");warning.className=\"warning\";"` | — |
| [SRC-DE7EABE998-L000287](../../web/agent.html#L287) | 287 | `"  warning.textContent=result.warnings.join(\" \");box.appendChild(warning);"` | — |
| [SRC-DE7EABE998-L000288](../../web/agent.html#L288) | 288 | `" }"` | — |
| [SRC-DE7EABE998-L000289](../../web/agent.html#L289) | 289 | `" const rawSources=result&&Array.isArray(result.sources)?result.sources:[];"` | — |
| [SRC-DE7EABE998-L000290](../../web/agent.html#L290) | 290 | `" const usableSources=rawSources.filter(s=>s&&typeof s===\"object\"&&safeSourceUrl(s.url));"` | — |
| [SRC-DE7EABE998-L000291](../../web/agent.html#L291) | 291 | `" if(usableSources.length){"` | — |
| [SRC-DE7EABE998-L000292](../../web/agent.html#L292) | 292 | `"  const sources=document.createElement(\"div\");sources.className=\"sources\";"` | — |
| [SRC-DE7EABE998-L000293](../../web/agent.html#L293) | 293 | `"  sources.innerHTML=usableSources.map((s,i)=>renderSource(s,i)).join(\"\");box.appendChild(sources);"` | — |
| [SRC-DE7EABE998-L000294](../../web/agent.html#L294) | 294 | `" }else if(role===\"assistant\"&&result&&result.kind!==\"general_answer\"&&result.kind!==\"capability_answer\"){"` | — |
| [SRC-DE7EABE998-L000295](../../web/agent.html#L295) | 295 | `"  const no=document.createElement(\"p\");no.className=\"no-sources\";"` | — |
| [SRC-DE7EABE998-L000296](../../web/agent.html#L296) | 296 | `"  no.textContent=\"لم يتم إرجاع مصدر صالح قابل للفتح في هذه الجولة. لا تعتبر الإجابة المدعومة بلا مصادر نتيجة بحث ناجحة.\";"` | — |
| [SRC-DE7EABE998-L000297](../../web/agent.html#L297) | 297 | `"  box.appendChild(no);"` | — |
| [SRC-DE7EABE998-L000298](../../web/agent.html#L298) | 298 | `" }"` | — |
| [SRC-DE7EABE998-L000299](../../web/agent.html#L299) | 299 | `" $(\"messages\").appendChild(box);box.scrollIntoView({behavior:\"smooth\",block:\"end\"});"` | — |
| [SRC-DE7EABE998-L000300](../../web/agent.html#L300) | 300 | `" return box;"` | — |
| [SRC-DE7EABE998-L000301](../../web/agent.html#L301) | 301 | `"}"` | — |
| [SRC-DE7EABE998-L000302](../../web/agent.html#L302) | 302 | `"function setBusy(on){busy=on;$(\"send\").disabled=on;$(\"send\").textContent=on?\"يبحث…\":\"ابحث ←\";$(\"question\").disabled=on;document.querySelectorAll(\".mode-btn\").forEach(b=>b.disabled=on);}"` | — |
| [SRC-DE7EABE998-L000303](../../web/agent.html#L303) | 303 | `"async function ask(value){"` | — |
| [SRC-DE7EABE998-L000304](../../web/agent.html#L304) | 304 | `" const q=(value??$(\"question\").value).trim();if(!q\|\|busy)return;"` | — |
| [SRC-DE7EABE998-L000305](../../web/agent.html#L305) | 305 | `" addMessage(\"user\",q);$(\"question\").value=\"\";setBusy(true);"` | — |
| [SRC-DE7EABE998-L000306](../../web/agent.html#L306) | 306 | `" setStatus(\"جارٍ تنفيذ البحث عن السؤال الحالي…\",\"warn\");"` | — |
| [SRC-DE7EABE998-L000307](../../web/agent.html#L307) | 307 | `" const pending=document.createElement(\"div\");pending.className=\"message assistant\";"` | — |
| [SRC-DE7EABE998-L000308](../../web/agent.html#L308) | 308 | `" pending.innerHTML='<div class=\"who\">Omarai · '+escapeHtml(modeName(activeMode))+'</div><div class=\"bubble\"><div class=\"pending\"><span class=\"spinner\"></span><span>يبحث الآن ويجمع المصادر. ستظهر نتيجة هذه الجولة مرتبطة بسؤالك أدناه.</span></div></div>';"` | — |
| [SRC-DE7EABE998-L000309](../../web/agent.html#L309) | 309 | `" $(\"messages\").appendChild(pending);pending.scrollIntoView({behavior:\"smooth\",block:\"end\"});"` | — |
| [SRC-DE7EABE998-L000310](../../web/agent.html#L310) | 310 | `" try{"` | — |
| [SRC-DE7EABE998-L000311](../../web/agent.html#L311) | 311 | `"  const response=await fetch(\"/api/agent\",{method:\"POST\",headers:apiHeaders(),body:JSON.stringify({question:q,history:history.slice(-8),mode:activeMode})});"` | — |
| [SRC-DE7EABE998-L000312](../../web/agent.html#L312) | 312 | `"  const data=await response.json().catch(()=>({}));"` | — |
| [SRC-DE7EABE998-L000313](../../web/agent.html#L313) | 313 | `"  pending.remove();"` | — |
| [SRC-DE7EABE998-L000314](../../web/agent.html#L314) | 314 | `"  if(!response.ok){"` | — |
| [SRC-DE7EABE998-L000315](../../web/agent.html#L315) | 315 | `"   if(response.status===401)throw Error(\"رمز الوصول غير صحيح أو غير محفوظ. راجع رمز التطبيق المستضاف.\");"` | — |
| [SRC-DE7EABE998-L000316](../../web/agent.html#L316) | 316 | `"   if(response.status===429)throw Error(\"تجاوز حد الطلبات المؤقت. انتظر قليلًا ثم أعد المحاولة.\");"` | — |
| [SRC-DE7EABE998-L000317](../../web/agent.html#L317) | 317 | `"   throw Error(data.error\|\|\"تعذر إكمال البحث. أعد المحاولة بعد التحقق من الاتصال.\");"` | — |
| [SRC-DE7EABE998-L000318](../../web/agent.html#L318) | 318 | `"  }"` | — |
| [SRC-DE7EABE998-L000319](../../web/agent.html#L319) | 319 | `"  addMessage(\"assistant\",data.answer\|\|\"لم يرجع الخادم نص إجابة.\",data);"` | — |
| [SRC-DE7EABE998-L000320](../../web/agent.html#L320) | 320 | `"  history.push({role:\"user\",content:q},{role:\"assistant\",content:String(data.answer\|\|\"\")});"` | — |
| [SRC-DE7EABE998-L000321](../../web/agent.html#L321) | 321 | `"  const sources=Array.isArray(data.sources)?data.sources.filter(s=>s&&safeSourceUrl(s.url)):[];"` | — |
| [SRC-DE7EABE998-L000322](../../web/agent.html#L322) | 322 | `"  if(data.kind===\"general_answer\"){"` | — |
| [SRC-DE7EABE998-L000323](../../web/agent.html#L323) | 323 | `"   setStatus(\"اكتملت إجابة المعرفة العامة دون بحث ويب\",\"ok\");"` | — |
| [SRC-DE7EABE998-L000324](../../web/agent.html#L324) | 324 | `"  }else if(data.kind===\"capability_answer\"){"` | — |
| [SRC-DE7EABE998-L000325](../../web/agent.html#L325) | 325 | `"   setStatus(\"إجابة عن قدرات Omarai وحدوده · لم يُجر بحث حي\",\"ok\");"` | — |
| [SRC-DE7EABE998-L000326](../../web/agent.html#L326) | 326 | `"  }else if(data.used_web_search===true&&data.used_language_model===true&&sources.length>0){"` | — |
| [SRC-DE7EABE998-L000327](../../web/agent.html#L327) | 327 | `"   setStatus(\"اكتمل البحث والتحليل · \"+sources.length+\" مصدرًا صالحًا\",\"ok\");"` | — |
| [SRC-DE7EABE998-L000328](../../web/agent.html#L328) | 328 | `"  }else if(data.used_web_search===true&&sources.length>0){"` | — |
| [SRC-DE7EABE998-L000329](../../web/agent.html#L329) | 329 | `"   setStatus(\"البحث أعاد مصادر، لكن التحليل غير مكتمل\",\"warn\");"` | — |
| [SRC-DE7EABE998-L000330](../../web/agent.html#L330) | 330 | `"  }else{"` | — |
| [SRC-DE7EABE998-L000331](../../web/agent.html#L331) | 331 | `"   setStatus(\"نتيجة جزئية: لا يوجد بحث حي مؤكد مع مصادر كافية\",\"bad\");"` | — |
| [SRC-DE7EABE998-L000332](../../web/agent.html#L332) | 332 | `"  }"` | — |
| [SRC-DE7EABE998-L000333](../../web/agent.html#L333) | 333 | `" }catch(error){"` | — |
| [SRC-DE7EABE998-L000334](../../web/agent.html#L334) | 334 | `"  pending.remove();"` | — |
| [SRC-DE7EABE998-L000335](../../web/agent.html#L335) | 335 | `"  const safeMessage=error&&error.message?error.message:\"تعذر إكمال الطلب.\";"` | — |
| [SRC-DE7EABE998-L000336](../../web/agent.html#L336) | 336 | `"  const box=addMessage(\"assistant\",safeMessage,null,{question:q});"` | — |
| [SRC-DE7EABE998-L000337](../../web/agent.html#L337) | 337 | `"  const actions=document.createElement(\"div\");actions.className=\"retry-row\";"` | — |
| [SRC-DE7EABE998-L000338](../../web/agent.html#L338) | 338 | `"  const retry=document.createElement(\"button\");retry.type=\"button\";retry.className=\"retry-button\";"` | — |
| [SRC-DE7EABE998-L000339](../../web/agent.html#L339) | 339 | `"  retry.textContent=\"إعادة محاولة هذا السؤال\";"` | — |
| [SRC-DE7EABE998-L000340](../../web/agent.html#L340) | 340 | `"  retry.addEventListener(\"click\",()=>ask(q));actions.appendChild(retry);box.appendChild(actions);"` | — |
| [SRC-DE7EABE998-L000341](../../web/agent.html#L341) | 341 | `"  setStatus(\"لم يكتمل الطلب؛ يمكنك إعادة محاولة السؤال نفسه\",\"bad\");"` | — |
| [SRC-DE7EABE998-L000342](../../web/agent.html#L342) | 342 | `" }finally{"` | — |
| [SRC-DE7EABE998-L000343](../../web/agent.html#L343) | 343 | `"  setBusy(false);$(\"question\").focus();"` | — |
| [SRC-DE7EABE998-L000344](../../web/agent.html#L344) | 344 | `" }"` | — |
| [SRC-DE7EABE998-L000345](../../web/agent.html#L345) | 345 | `"}"` | — |
| [SRC-DE7EABE998-L000346](../../web/agent.html#L346) | 346 | `"async function runDiagnostics(){"` | — |
| [SRC-DE7EABE998-L000347](../../web/agent.html#L347) | 347 | `" const button=$(\"runDiagnostics\"),output=$(\"diagnosticsResult\");if(button.disabled)return;"` | — |
| [SRC-DE7EABE998-L000348](../../web/agent.html#L348) | 348 | `" button.disabled=true;button.textContent=\"جارٍ الاختبار الحقيقي…\";output.textContent=\"يُرسل الآن طلب فعلي إلى محركات البحث، وقد يستغرق بضع ثوانٍ.\";"` | — |
| [SRC-DE7EABE998-L000349](../../web/agent.html#L349) | 349 | `" try{"` | — |
| [SRC-DE7EABE998-L000350](../../web/agent.html#L350) | 350 | `"  const response=await fetch(\"/api/diagnostics\",{method:\"POST\",headers:apiHeaders(),body:JSON.stringify({test_model:true,test_social:$(\"diagSocial\").checked})});"` | — |
| [SRC-DE7EABE998-L000351](../../web/agent.html#L351) | 351 | `"  const data=await response.json();if(!response.ok)throw Error(data.error\|\|\"فشل طلب الاختبار\");"` | — |
| [SRC-DE7EABE998-L000352](../../web/agent.html#L352) | 352 | `"  const labels={passed:\"نجح فعليًا\",degraded:\"جزئي أو بلا نتائج كافية\",failed:\"فشل\",skipped:\"لم يُختبر\",not_configured:\"غير مضبوط\"};"` | — |
| [SRC-DE7EABE998-L000353](../../web/agent.html#L353) | 353 | `"  const lines=[\"النتيجة: \"+(labels[data.overall_status]\|\|data.overall_status)];"` | — |
| [SRC-DE7EABE998-L000354](../../web/agent.html#L354) | 354 | `"  for(const [key,label] of [[\"web_search\",\"بحث الإنترنت\"],[\"language_model\",\"النموذج اللغوي\"],[\"social_search\",\"المصادر الاجتماعية\"]]){"` | — |
| [SRC-DE7EABE998-L000355](../../web/agent.html#L355) | 355 | `"   const item=(data.checks\|\|{})[key];if(!item)continue;"` | — |
| [SRC-DE7EABE998-L000356](../../web/agent.html#L356) | 356 | `"   lines.push(label+\": \"+(labels[item.status]\|\|item.status)+(item.result_count!==undefined?\" · \"+item.result_count+\" نتيجة\":\"\"));"` | — |
| [SRC-DE7EABE998-L000357](../../web/agent.html#L357) | 357 | `"   if(item.provider_counts&&Object.keys(item.provider_counts).length)lines.push(\"المصادر التي أعادت نتائج: \"+Object.entries(item.provider_counts).map(([p,n])=>p+\" (\"+n+\")\").join(\"، \"));"` | — |
| [SRC-DE7EABE998-L000358](../../web/agent.html#L358) | 358 | `"   if(item.note)lines.push(item.note);"` | — |
| [SRC-DE7EABE998-L000359](../../web/agent.html#L359) | 359 | `"   if(item.warnings&&item.warnings.length)lines.push(item.warnings.join(\"؛ \"));"` | — |
| [SRC-DE7EABE998-L000360](../../web/agent.html#L360) | 360 | `"  }"` | — |
| [SRC-DE7EABE998-L000361](../../web/agent.html#L361) | 361 | `"  if(data.model_usage&&data.model_usage.length)lines.push(\"النموذج المستخدم: \"+data.model_usage.map(x=>x.used_model).join(\"، \"));"` | — |
| [SRC-DE7EABE998-L000362](../../web/agent.html#L362) | 362 | `"  if(data.elapsed_ms!==undefined)lines.push(\"مدة الاختبار: \"+(data.elapsed_ms/1000).toFixed(1)+\" ثانية\");"` | — |
| [SRC-DE7EABE998-L000363](../../web/agent.html#L363) | 363 | `"  output.textContent=lines.join(\"\\n\");setStatus(data.overall_status===\"passed\"?\"نجح الاختبار الحي\":data.overall_status===\"failed\"?\"فشل الاختبار الحي\":\"نتيجة الاختبار جزئية\",data.overall_status===\"passed\"?\"ok\":data.overall_status===\"failed\"?\"bad\":\"warn\");"` | — |
| [SRC-DE7EABE998-L000364](../../web/agent.html#L364) | 364 | `" }catch(e){output.textContent=\"تعذّر الاختبار الحي: \"+(e&&e.message?e.message:\"خطأ غير معروف\");setStatus(\"فشل الاختبار الحي\",\"bad\");}"` | — |
| [SRC-DE7EABE998-L000365](../../web/agent.html#L365) | 365 | `" finally{button.disabled=false;button.textContent=\"إعادة الاختبار الحي\";}"` | — |
| [SRC-DE7EABE998-L000366](../../web/agent.html#L366) | 366 | `"}"` | — |
| [SRC-DE7EABE998-L000367](../../web/agent.html#L367) | 367 | `"async function checkHealth(){"` | — |
| [SRC-DE7EABE998-L000368](../../web/agent.html#L368) | 368 | `" try{"` | — |
| [SRC-DE7EABE998-L000369](../../web/agent.html#L369) | 369 | `"  const r=await fetch(\"/api/health\");const d=await r.json();const a=d.agent\|\|{};"` | — |
| [SRC-DE7EABE998-L000370](../../web/agent.html#L370) | 370 | `"  const configured=[];"` | — |
| [SRC-DE7EABE998-L000371](../../web/agent.html#L371) | 371 | `"  if(a.brave_search_api_configured)configured.push(\"Brave API\");"` | — |
| [SRC-DE7EABE998-L000372](../../web/agent.html#L372) | 372 | `"  if(a.tavily_search_api_configured)configured.push(\"Tavily API\");"` | — |
| [SRC-DE7EABE998-L000373](../../web/agent.html#L373) | 373 | `"  if(a.reddit_oauth_configured)configured.push(\"Reddit OAuth\");"` | — |
| [SRC-DE7EABE998-L000374](../../web/agent.html#L374) | 374 | `"  if(a.facebook_pages_api_configured)configured.push(\"Facebook Pages\");"` | — |
| [SRC-DE7EABE998-L000375](../../web/agent.html#L375) | 375 | `"  if(a.instagram_graph_api_configured)configured.push(\"Instagram Graph\");"` | — |
| [SRC-DE7EABE998-L000376](../../web/agent.html#L376) | 376 | `"  if(a.x_api_configured)configured.push(\"X API\");"` | — |
| [SRC-DE7EABE998-L000377](../../web/agent.html#L377) | 377 | `"  if(a.youtube_api_configured)configured.push(\"YouTube API\");"` | — |
| [SRC-DE7EABE998-L000378](../../web/agent.html#L378) | 378 | `"  const model=!!a.language_model_configured, search=!!a.web_search_ready;"` | — |
| [SRC-DE7EABE998-L000379](../../web/agent.html#L379) | 379 | `"  $(\"setupStatus\").textContent=(search?\"حزم البحث مثبتة. \":\"حزم البحث تحتاج تثبيتًا. \")+(model?\"مفتاح نموذج اللغة موجود في جلسة الخادم. \":\"النموذج التوليدي غير مضبوط بعد. \")+\"لم يتم تأكيد اتصال الإنترنت من هذه الشاشة وحدها؛ شغّل الاختبار الحي. لا تظهر هنا مفاتيح الخدمات أو قيمها.\";"` | — |
| [SRC-DE7EABE998-L000380](../../web/agent.html#L380) | 380 | `"  $(\"providerSetup\").innerHTML=configured.length?'<span class=\"config-label\">موصلات مفاتيحها مضبوطة: '+configured.map(escapeHtml).join(\" · \")+'</span>':'<p>لم تُضبط مفاتيح API البحثية الإضافية؛ يظل Omarai قادرًا على تجربة محركات البحث العامة المتاحة.</p>';"` | — |
| [SRC-DE7EABE998-L000381](../../web/agent.html#L381) | 381 | `"  setStatus(\"الإعداد ظاهر · يلزم اختبار حي\",\"warn\");"` | — |
| [SRC-DE7EABE998-L000382](../../web/agent.html#L382) | 382 | `" }catch(e){setStatus(\"تعذر فحص الإعداد\",\"bad\");$(\"setupStatus\").textContent=\"تعذر الاتصال بخادم Omarai المحلي. تأكد أن الخادم يعمل في Termux.\";}"` | — |
| [SRC-DE7EABE998-L000383](../../web/agent.html#L383) | 383 | `"}"` | — |
| [SRC-DE7EABE998-L000384](../../web/agent.html#L384) | 384 | `"document.querySelectorAll(\".mode-btn\").forEach(button=>button.addEventListener(\"click\",()=>{"` | — |
| [SRC-DE7EABE998-L000385](../../web/agent.html#L385) | 385 | `" activeMode=button.dataset.mode;"` | — |
| [SRC-DE7EABE998-L000386](../../web/agent.html#L386) | 386 | `" document.querySelectorAll(\".mode-btn\").forEach(other=>{const active=other===button;other.classList.toggle(\"active\",active);other.setAttribute(\"aria-pressed\",String(active));});"` | — |
| [SRC-DE7EABE998-L000387](../../web/agent.html#L387) | 387 | `"}));"` | — |
| [SRC-DE7EABE998-L000388](../../web/agent.html#L388) | 388 | `"$(\"send\").addEventListener(\"click\",()=>ask());"` | — |
| [SRC-DE7EABE998-L000389](../../web/agent.html#L389) | 389 | `"$(\"question\").addEventListener(\"keydown\",e=>{if(e.key===\"Enter\"&&!e.shiftKey){e.preventDefault();ask();}});"` | — |
| [SRC-DE7EABE998-L000390](../../web/agent.html#L390) | 390 | `"$(\"clear\").addEventListener(\"click\",()=>{history.length=0;$(\"messages\").innerHTML='<div class=\"welcome\" id=\"welcome\"><div class=\"welcome-icon\">⌕</div><h3>محادثة جديدة</h3><p>اكتب سؤالك واختر نمط البحث المناسب. المصادر والتغطية سيظهران أسفل الإجابة.</p></div>';$(\"question\").focus();});"` | — |
| [SRC-DE7EABE998-L000391](../../web/agent.html#L391) | 391 | `"document.querySelectorAll(\".suggestions button\").forEach(b=>b.addEventListener(\"click\",()=>ask(b.textContent)));"` | — |
| [SRC-DE7EABE998-L000392](../../web/agent.html#L392) | 392 | `"$(\"saveAccessToken\").addEventListener(\"click\",()=>{const token=$(\"accessToken\").value.trim();if(token)localStorage.setItem(ACCESS_TOKEN_STORAGE_KEY,token);else localStorage.removeItem(ACCESS_TOKEN_STORAGE_KEY);$(\"saveAccessToken\").textContent=token?\"تم حفظ الرمز على هذا الجهاز\":\"تم مسح الرمز المحفوظ\";});"` | — |
| [SRC-DE7EABE998-L000393](../../web/agent.html#L393) | 393 | `"$(\"accessToken\").value=localStorage.getItem(ACCESS_TOKEN_STORAGE_KEY)\|\|\"\";"` | — |
| [SRC-DE7EABE998-L000394](../../web/agent.html#L394) | 394 | `"$(\"runDiagnostics\").addEventListener(\"click\",runDiagnostics);checkHealth();"` | — |
| [SRC-DE7EABE998-L000395](../../web/agent.html#L395) | 395 | `"</script>"` | — |
| [SRC-DE7EABE998-L000396](../../web/agent.html#L396) | 396 | `"</body>"` | — |
| [SRC-DE7EABE998-L000397](../../web/agent.html#L397) | 397 | `"</html>"` | — |
## واجهة الويب

### FILE-A16FA6D4B5 — [web/dashboard.html](../../web/dashboard.html#L1)

- النوع: **HTML**
- نطاق الفهرسة: جرد الملف + معرفات HTML والرموز داخل script/style

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-A16FA6D4B5-L000001](../../web/dashboard.html#L1) | 1 | `"<!doctype html>"` | — |
| [SRC-A16FA6D4B5-L000002](../../web/dashboard.html#L2) | 2 | `"<html lang=\"ar\" dir=\"rtl\">"` | — |
| [SRC-A16FA6D4B5-L000003](../../web/dashboard.html#L3) | 3 | `"<head>"` | — |
| [SRC-A16FA6D4B5-L000004](../../web/dashboard.html#L4) | 4 | `"<meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"` | — |
| [SRC-A16FA6D4B5-L000005](../../web/dashboard.html#L5) | 5 | `"<meta name=\"theme-color\" content=\"#0b1020\"><title>Omarai \| مساعد اكتشاف العملاء</title>"` | — |
| [SRC-A16FA6D4B5-L000006](../../web/dashboard.html#L6) | 6 | `"<style>"` | — |
| [SRC-A16FA6D4B5-L000007](../../web/dashboard.html#L7) | 7 | `":root{color-scheme:dark;--bg:#080d19;--panel:#111a2d;--line:#263550;--muted:#98a9c5;--text:#edf4ff;--cyan:#57e5dc;--blue:#7b9cff;--green:#7be0a3;--amber:#ffca72;--red:#ff8494}"` | — |
| [SRC-A16FA6D4B5-L000008](../../web/dashboard.html#L8) | 8 | `"*{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at 80% 0%,#162b4b 0,transparent 38%),var(--bg);font-family:system-ui,-apple-system,\"Segoe UI\",sans-serif;color:var(--text);min-height:100vh}"` | — |
| [SRC-A16FA6D4B5-L000009](../../web/dashboard.html#L9) | 9 | `".wrap{max-width:1180px;margin:auto;padding:22px}.top{display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap;margin-bottom:22px}.brand{display:flex;align-items:center;gap:12px}.logo{width:48px;height:48px;border-radius:16px;background:linear-gradient(135deg,var(--cyan),var(--blue));color:#071020;display:grid;place-items:center;font-weight:900;font-size:22px;box-shadow:0 8px 28px #57e5dc30}.brand h1{margin:0;font-size:25px;letter-spacing:.2px}.brand p{margin:4px 0 0;color:var(--muted);font-size:13px}.badge{border:1px solid #2e5b62;background:#102a32;color:var(--cyan);padding:8px 12px;border-radius:99px;font-size:12px}"` | — |
| [SRC-A16FA6D4B5-L000010](../../web/dashboard.html#L10) | 10 | `".hero{display:grid;grid-template-columns:1.2fr .8fr;gap:16px;margin-bottom:16px}.card{background:linear-gradient(145deg,#131e33f2,#0d1526f2);border:1px solid var(--line);border-radius:22px;padding:20px;box-shadow:0 18px 40px #0002}.eyebrow{font-size:12px;color:var(--cyan);font-weight:700;letter-spacing:.4px}.card h2{font-size:21px;margin:8px 0}.muted{color:var(--muted);font-size:13px;line-height:1.8}.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:18px}.stat{padding:14px;border-radius:15px;background:#0a1222;border:1px solid #202f49}.stat strong{display:block;font-size:25px}.stat span{font-size:12px;color:var(--muted)}"` | — |
| [SRC-A16FA6D4B5-L000011](../../web/dashboard.html#L11) | 11 | `".layout{display:grid;grid-template-columns:1fr 1fr;gap:16px}.field{margin:13px 0}label{display:block;font-size:13px;color:#c7d4ea;margin-bottom:7px}input,textarea,select{width:100%;border:1px solid #30415e;background:#091222;color:var(--text);border-radius:12px;padding:12px;font:inherit;outline:none}input:focus,textarea:focus,select:focus{border-color:var(--cyan);box-shadow:0 0 0 3px #57e5dc15}textarea{min-height:132px;resize:vertical}button{border:0;border-radius:12px;padding:12px 16px;font:inherit;font-weight:750;cursor:pointer;transition:.15s}button:hover{transform:translateY(-1px)}.primary{background:linear-gradient(110deg,var(--cyan),#8cbdff);color:#071020}.secondary{background:#1c2a43;color:#dce8ff;border:1px solid #344664}.row{display:flex;gap:9px;flex-wrap:wrap}.result{display:none;margin-top:15px;padding:16px;border:1px solid #344664;border-radius:16px;background:#0a1324}.score{font-size:35px;font-weight:850}.pill{display:inline-block;border-radius:99px;padding:5px 10px;background:#18333b;color:var(--cyan);font-size:12px;margin:4px 0}.signal{padding:10px 0;border-bottom:1px solid #24324a;font-size:13px}.signal:last-child{border-bottom:0}.warning{font-size:12px;color:var(--amber);line-height:1.8;margin-top:12px}.leads{margin-top:16px}.lead{padding:14px;border:1px solid #263650;background:#0a1323;border-radius:15px;margin-top:10px}.leadhead{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap}.lead p{line-height:1.8;font-size:14px;white-space:pre-wrap;overflow-wrap:anywhere}.empty{text-align:center;padding:24px;color:var(--muted);border:1px dashed #33435c;border-radius:14px;margin-top:12px}.foot{text-align:center;color:#6f819e;font-size:11px;padding:24px 0 8px}"` | — |
| [SRC-A16FA6D4B5-L000012](../../web/dashboard.html#L12) | 12 | `"@media(max-width:800px){.hero,.layout{grid-template-columns:1fr}.wrap{padding:14px}.card{padding:16px}.brand h1{font-size:22px}.stats{gap:7px}.stat{padding:11px}.stat strong{font-size:21px}}"` | — |
| [SRC-A16FA6D4B5-L000013](../../web/dashboard.html#L13) | 13 | `"</style></head><body><div class=\"wrap\">"` | — |
| [SRC-A16FA6D4B5-L000014](../../web/dashboard.html#L14) | 14 | `"<header class=\"top\"><div class=\"brand\"><div class=\"logo\">O</div><div><h1>Omarai</h1><p>مساعد ذكي لتأهيل إشارات العملاء المحتملين</p></div></div><span class=\"badge\">● تشغيل محلي أو مستضاف حسب إعداد الخادم</span></header>"` | — |
| [SRC-A16FA6D4B5-L000015](../../web/dashboard.html#L15) | 15 | `"<section class=\"card\" style=\"margin-bottom:16px\">"` | — |
| [SRC-A16FA6D4B5-L000016](../../web/dashboard.html#L16) | 16 | `"  <div class=\"row\" style=\"align-items:end\">"` | — |
| [SRC-A16FA6D4B5-L000017](../../web/dashboard.html#L17) | 17 | `"    <div style=\"flex:1;min-width:220px\">"` | — |
| [SRC-A16FA6D4B5-L000018](../../web/dashboard.html#L18) | 18 | `"      <label for=\"accessToken\">رمز الوصول الخاص بالتطبيق (للاستضافة فقط)</label>"` | — |
| [SRC-A16FA6D4B5-L000019](../../web/dashboard.html#L19) | 19 | `"      <input id=\"accessToken\" type=\"password\" autocomplete=\"current-password\" placeholder=\"أدخل رمز الوصول الذي ضبطته في الاستضافة\">"` | — |
| [SRC-A16FA6D4B5-L000020](../../web/dashboard.html#L20) | 20 | `"    </div>"` | — |
| [SRC-A16FA6D4B5-L000021](../../web/dashboard.html#L21) | 21 | `"    <button class=\"secondary\" id=\"saveAccessToken\">حفظ الرمز على هذا الجهاز</button>"` | — |
| [SRC-A16FA6D4B5-L000022](../../web/dashboard.html#L22) | 22 | `"  </div>"` | — |
| [SRC-A16FA6D4B5-L000023](../../web/dashboard.html#L23) | 23 | `"  <p id=\"authMessage\" class=\"muted\" aria-live=\"polite\">يُستخدم الرمز للوصول إلى السجل الخاص. الرمز محفوظ في هذا المتصفح فقط ولا يُعرض في الصفحة.</p>"` | — |
| [SRC-A16FA6D4B5-L000024](../../web/dashboard.html#L24) | 24 | `"</section>"` | — |
| [SRC-A16FA6D4B5-L000025](../../web/dashboard.html#L25) | 25 | `"<section class=\"hero\"><div class=\"card\"><span class=\"eyebrow\">مساحة العمل · الإصدار الأول</span><h2>حوّل الإشارات إلى فرص منظمة</h2><p class=\"muted\">أدخل نصًا من مصدر مسموح، افهم مؤشرات الاهتمام وأسبابها، ثم احفظ الإشارة وتابعها بنفسك. لا يوجد تواصل تلقائي مع أي شخص.</p><div class=\"stats\"><div class=\"stat\"><strong id=\"total\">—</strong><span>إشارة محفوظة</span></div><div class=\"stat\"><strong id=\"qualified\">—</strong><span>مؤهلة يدويًا</span></div><div class=\"stat\"><strong id=\"review\">—</strong><span>تحتاج مراجعة</span></div></div></div><div class=\"card\"><span class=\"eyebrow\">كيف يعمل Omarai؟</span><h2>القرار لك دائمًا</h2><p class=\"muted\">١. تحليل محلي قابل للتفسير<br>٢. تسجيل رابط المصدر ووقت الرصد<br>٣. منع التكرار لنفس النص والمصدر<br>٤. متابعة بشرية للحالة والخطوة التالية</p><p class=\"warning\">تنبيه: الدرجة قواعد إرشادية وليست احتمالًا إحصائيًا للشراء أو ضمانًا لجودة العميل.</p></div></section>"` | — |
| [SRC-A16FA6D4B5-L000026](../../web/dashboard.html#L26) | 26 | `"<section class=\"layout\"><div class=\"card\"><span class=\"eyebrow\">١ / تحليل إشارة</span><h2>اكتشف نية الاهتمام</h2><div class=\"field\"><label for=\"text\">النص المراد تحليله</label><textarea id=\"text\" placeholder=\"مثال: بدور على شقة في التجمع الخامس وممكن معاينة...\"></textarea></div><div class=\"field\"><label for=\"product\">نوع المنتج (اختياري)</label><input id=\"product\" placeholder=\"شقة، عقار\"></div><div class=\"field\"><label for=\"location\">المنطقة (اختياري)</label><input id=\"location\" placeholder=\"التجمع الخامس، العاصمة الإدارية\"></div><button class=\"primary\" id=\"analyze\">حلّل الإشارة ←</button><div class=\"result\" id=\"result\"></div></div>"` | — |
| [SRC-A16FA6D4B5-L000027](../../web/dashboard.html#L27) | 27 | `"<div class=\"card\"><span class=\"eyebrow\">٢ / حفظ ومتابعة</span><h2>سجّل المصدر</h2><div class=\"field\"><label for=\"source\">رابط المنشور أو المصدر</label><input id=\"source\" type=\"url\" placeholder=\"https://...\"></div><div class=\"field\"><label for=\"platform\">المنصة أو المصدر</label><select id=\"platform\"><option value=\"manual\">إدخال يدوي</option><option>Facebook</option><option>Website</option><option>OLX</option><option>Other</option></select></div><div class=\"field\"><label for=\"note\">ملاحظاتك (اختياري)</label><input id=\"note\" placeholder=\"ميزانية معلنة، موعد متابعة...\"></div><button class=\"primary\" id=\"save\">احفظ الإشارة</button><p class=\"muted\">لا تحفظ بيانات شخصية غير لازمة. أدخل فقط ما يحق لك معالجته.</p><div id=\"message\" class=\"muted\" aria-live=\"polite\"></div></div></section>"` | — |
| [SRC-A16FA6D4B5-L000028](../../web/dashboard.html#L28) | 28 | `"<section class=\"card leads\"><div class=\"leadhead\"><div><span class=\"eyebrow\">٣ / قائمة الفرص</span><h2>الإشارات المحفوظة</h2></div><button class=\"secondary\" id=\"refresh\">تحديث القائمة ↻</button></div><div id=\"leadlist\"><div class=\"empty\">جارٍ تحميل البيانات...</div></div></section><section class=\"card\" style=\"margin-top:16px\"><span class=\"eyebrow\">٤ / المساعد المحلي</span><h2>اسأل Omarai</h2><p class=\"muted\">اسأل عن عدد الإشارات، أولوية المراجعة، تفسير الدرجة، أو اطلب مسودة تواصل. الإجابات مبنية على سجلك المحلي وقواعد واضحة؛ لا يوجد نموذج سحابي ولا يتم إرسال رسائل.</p><div id=\"askMessages\" style=\"display:flex;flex-direction:column;gap:10px;margin:12px 0;max-height:270px;overflow:auto\"><div class=\"lead\">جرّب: «كام عميل عندي؟» أو «مين أفضل إشارة أراجعها؟»</div></div><div class=\"row\"><input id=\"askInput\" maxlength=\"1000\" placeholder=\"اكتب سؤالك هنا...\" style=\"flex:1;min-width:180px\"><button class=\"primary\" id=\"askBtn\">اسأل ←</button></div></section><div class=\"foot\">Omarai · Local-first · تخزين البيانات يعتمد على الخادم المستخدم · لا زحف آلي ولا رسائل تلقائية</div></div>"` | — |
| [SRC-A16FA6D4B5-L000029](../../web/dashboard.html#L29) | 29 | `"<script>"` | — |
| [SRC-A16FA6D4B5-L000030](../../web/dashboard.html#L30) | 30 | `"const $=id=>document.getElementById(id);let lastAssessment=null;let lastAnalysisInput=null;"` | — |
| [SRC-A16FA6D4B5-L000031](../../web/dashboard.html#L31) | 31 | `"const ACCESS_TOKEN_STORAGE_KEY=\"omarai_access_token\";"` | — |
| [SRC-A16FA6D4B5-L000032](../../web/dashboard.html#L32) | 32 | `"const labels={high_intent:\"اهتمام قوي نسبيًا\",medium_intent:\"اهتمام متوسط\",early_research:\"استكشاف مبكر\",unclear:\"غير واضح\",not_buyer_signal:\"ليس إشارة شراء مباشرة\"};"` | — |
| [SRC-A16FA6D4B5-L000033](../../web/dashboard.html#L33) | 33 | `"const esc=s=>String(s??\"\").replace(/[&<>\"']/g,c=>({\"&\":\"&amp;\",\"<\":\"&lt;\",\">\":\"&gt;\",'\"':\"&quot;\",\"'\":\"&#39;\"}[c]));"` | — |
