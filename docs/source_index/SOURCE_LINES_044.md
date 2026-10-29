# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **044**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L001448 إلى SRC-F725E90B2A-L002247
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L001448](../../tests/test_web_agent.py#L1448) | 1448 | `"def test_general_question_uses_model_without_needlessly_searching(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001449](../../tests/test_web_agent.py#L1449) | 1449 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001450](../../tests/test_web_agent.py#L1450) | 1450 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L001451](../../tests/test_web_agent.py#L1451) | 1451 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L001452](../../tests/test_web_agent.py#L1452) | 1452 | `""` | — |
| [SRC-F725E90B2A-L001453](../../tests/test_web_agent.py#L1453) | 1453 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L001454](../../tests/test_web_agent.py#L1454) | 1454 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L001455](../../tests/test_web_agent.py#L1455) | 1455 | `"        captured[\"kwargs\"] = kwargs"` | — |
| [SRC-F725E90B2A-L001456](../../tests/test_web_agent.py#L1456) | 1456 | `"        return \"مصر دولة في شمال شرق أفريقيا، وعاصمتها القاهرة.\""` | — |
| [SRC-F725E90B2A-L001457](../../tests/test_web_agent.py#L1457) | 1457 | `""` | — |
| [SRC-F725E90B2A-L001458](../../tests/test_web_agent.py#L1458) | 1458 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L001459](../../tests/test_web_agent.py#L1459) | 1459 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001460](../../tests/test_web_agent.py#L1460) | 1460 | `"        agent, \"_collect_research\","` | — |
| [SRC-F725E90B2A-L001461](../../tests/test_web_agent.py#L1461) | 1461 | `"        lambda plan: pytest.fail(\"A stable general question should not start web research\"),"` | — |
| [SRC-F725E90B2A-L001462](../../tests/test_web_agent.py#L1462) | 1462 | `"    )"` | — |
| [SRC-F725E90B2A-L001463](../../tests/test_web_agent.py#L1463) | 1463 | `""` | — |
| [SRC-F725E90B2A-L001464](../../tests/test_web_agent.py#L1464) | 1464 | `"    result = agent.answer(\"ما هي جمهورية مصر العربية؟\")"` | — |
| [SRC-F725E90B2A-L001465](../../tests/test_web_agent.py#L1465) | 1465 | `""` | — |
| [SRC-F725E90B2A-L001466](../../tests/test_web_agent.py#L1466) | 1466 | `"    assert result[\"kind\"] == \"general_answer\""` | — |
| [SRC-F725E90B2A-L001467](../../tests/test_web_agent.py#L1467) | 1467 | `"    assert result[\"used_language_model\"] is True"` | — |
| [SRC-F725E90B2A-L001468](../../tests/test_web_agent.py#L1468) | 1468 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-F725E90B2A-L001469](../../tests/test_web_agent.py#L1469) | 1469 | `"    assert result[\"sources\"] == []"` | — |
| [SRC-F725E90B2A-L001470](../../tests/test_web_agent.py#L1470) | 1470 | `"    assert \"عاصمتها القاهرة\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L001471](../../tests/test_web_agent.py#L1471) | 1471 | `"    assert captured[\"kwargs\"][\"enable_web_search\"] is False"` | — |
| [SRC-F725E90B2A-L001472](../../tests/test_web_agent.py#L1472) | 1472 | `""` | — |
| [SRC-F725E90B2A-L001473](../../tests/test_web_agent.py#L1473) | 1473 | `""` | — |
| [SRC-F725E90B2A-L001474](../../tests/test_web_agent.py#L1474) | 1474 | `"def test_omarai_capability_question_is_answered_without_network(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001475](../../tests/test_web_agent.py#L1475) | 1475 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001476](../../tests/test_web_agent.py#L1476) | 1476 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L001477](../../tests/test_web_agent.py#L1477) | 1477 | `""` | — |
| [SRC-F725E90B2A-L001478](../../tests/test_web_agent.py#L1478) | 1478 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001479](../../tests/test_web_agent.py#L1479) | 1479 | `"        agent, \"_collect_research\","` | — |
| [SRC-F725E90B2A-L001480](../../tests/test_web_agent.py#L1480) | 1480 | `"        lambda plan: pytest.fail(\"Self-description must not call external search\"),"` | — |
| [SRC-F725E90B2A-L001481](../../tests/test_web_agent.py#L1481) | 1481 | `"    )"` | — |
| [SRC-F725E90B2A-L001482](../../tests/test_web_agent.py#L1482) | 1482 | `""` | — |
| [SRC-F725E90B2A-L001483](../../tests/test_web_agent.py#L1483) | 1483 | `"    result = agent.answer(\"كيف تبحث أنت في الإنترنت؟\")"` | — |
| [SRC-F725E90B2A-L001484](../../tests/test_web_agent.py#L1484) | 1484 | `""` | — |
| [SRC-F725E90B2A-L001485](../../tests/test_web_agent.py#L1485) | 1485 | `"    assert result[\"kind\"] == \"capability_answer\""` | — |
| [SRC-F725E90B2A-L001486](../../tests/test_web_agent.py#L1486) | 1486 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-F725E90B2A-L001487](../../tests/test_web_agent.py#L1487) | 1487 | `"    assert \"DuckDuckGo HTML\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L001488](../../tests/test_web_agent.py#L1488) | 1488 | `"    assert \"ليست إثباتًا\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L001489](../../tests/test_web_agent.py#L1489) | 1489 | `""` | — |
| [SRC-F725E90B2A-L001490](../../tests/test_web_agent.py#L1490) | 1490 | `""` | — |
| [SRC-F725E90B2A-L001491](../../tests/test_web_agent.py#L1491) | 1491 | `"def test_link_lookup_can_return_one_clearly_labelled_candidate(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001492](../../tests/test_web_agent.py#L1492) | 1492 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001493](../../tests/test_web_agent.py#L1493) | 1493 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L001494](../../tests/test_web_agent.py#L1494) | 1494 | `"    source = {"` | — |
| [SRC-F725E90B2A-L001495](../../tests/test_web_agent.py#L1495) | 1495 | `"        \"title\": \"موقع مصر الرقمية والخدمات الحكومية\","` | — |
| [SRC-F725E90B2A-L001496](../../tests/test_web_agent.py#L1496) | 1496 | `"        \"url\": \"https://digital.gov.eg/\","` | — |
| [SRC-F725E90B2A-L001497](../../tests/test_web_agent.py#L1497) | 1497 | `"        \"snippet\": \"بوابة مصر الرقمية للخدمات الحكومية الإلكترونية.\","` | — |
| [SRC-F725E90B2A-L001498](../../tests/test_web_agent.py#L1498) | 1498 | `"        \"page_text\": \"بوابة مصر الرقمية للخدمات الحكومية الإلكترونية.\","` | — |
| [SRC-F725E90B2A-L001499](../../tests/test_web_agent.py#L1499) | 1499 | `"        \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L001500](../../tests/test_web_agent.py#L1500) | 1500 | `"        \"providers\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001501](../../tests/test_web_agent.py#L1501) | 1501 | `"        \"queries\": [\"ابحث عن موقع مصر الرقمية\"],"` | — |
| [SRC-F725E90B2A-L001502](../../tests/test_web_agent.py#L1502) | 1502 | `"        \"domain\": \"digital.gov.eg\","` | — |
| [SRC-F725E90B2A-L001503](../../tests/test_web_agent.py#L1503) | 1503 | `"        \"source_class\": \"government\","` | — |
| [SRC-F725E90B2A-L001504](../../tests/test_web_agent.py#L1504) | 1504 | `"        \"platform\": \"web\","` | — |
| [SRC-F725E90B2A-L001505](../../tests/test_web_agent.py#L1505) | 1505 | `"    }"` | — |
| [SRC-F725E90B2A-L001506](../../tests/test_web_agent.py#L1506) | 1506 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001507](../../tests/test_web_agent.py#L1507) | 1507 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L001508](../../tests/test_web_agent.py#L1508) | 1508 | `"        lambda question, history: {"` | — |
| [SRC-F725E90B2A-L001509](../../tests/test_web_agent.py#L1509) | 1509 | `"            \"queries\": [question], \"direct_urls\": [], \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001510](../../tests/test_web_agent.py#L1510) | 1510 | `"            \"freshness\": \"any\", \"depth\": \"standard\", \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001511](../../tests/test_web_agent.py#L1511) | 1511 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001512](../../tests/test_web_agent.py#L1512) | 1512 | `"        },"` | — |
| [SRC-F725E90B2A-L001513](../../tests/test_web_agent.py#L1513) | 1513 | `"    )"` | — |
| [SRC-F725E90B2A-L001514](../../tests/test_web_agent.py#L1514) | 1514 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001515](../../tests/test_web_agent.py#L1515) | 1515 | `"        agent, \"_collect_research\","` | — |
| [SRC-F725E90B2A-L001516](../../tests/test_web_agent.py#L1516) | 1516 | `"        lambda plan: ([source], [], {"` | — |
| [SRC-F725E90B2A-L001517](../../tests/test_web_agent.py#L1517) | 1517 | `"            \"queries_planned\": 1, \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001518](../../tests/test_web_agent.py#L1518) | 1518 | `"            \"unique_sources\": 1, \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L001519](../../tests/test_web_agent.py#L1519) | 1519 | `"            \"providers_used\": [\"test_provider\"], \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L001520](../../tests/test_web_agent.py#L1520) | 1520 | `"            \"social_direct_results\": 0, \"depth\": \"standard\", \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001521](../../tests/test_web_agent.py#L1521) | 1521 | `"        }),"` | — |
| [SRC-F725E90B2A-L001522](../../tests/test_web_agent.py#L1522) | 1522 | `"    )"` | — |
| [SRC-F725E90B2A-L001523](../../tests/test_web_agent.py#L1523) | 1523 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001524](../../tests/test_web_agent.py#L1524) | 1524 | `"        agent, \"_generate\","` | — |
| [SRC-F725E90B2A-L001525](../../tests/test_web_agent.py#L1525) | 1525 | `"        lambda *args, **kwargs: \"وجدت نتيجة مرشحة لبوابة مصر الرقمية [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L001526](../../tests/test_web_agent.py#L1526) | 1526 | `"    )"` | — |
| [SRC-F725E90B2A-L001527](../../tests/test_web_agent.py#L1527) | 1527 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L001528](../../tests/test_web_agent.py#L1528) | 1528 | `""` | — |
| [SRC-F725E90B2A-L001529](../../tests/test_web_agent.py#L1529) | 1529 | `"    result = agent.answer(\"ابحث عن موقع مصر الرقمية\")"` | — |
| [SRC-F725E90B2A-L001530](../../tests/test_web_agent.py#L1530) | 1530 | `""` | — |
| [SRC-F725E90B2A-L001531](../../tests/test_web_agent.py#L1531) | 1531 | `"    assert result[\"kind\"] == \"web_research\""` | — |
| [SRC-F725E90B2A-L001532](../../tests/test_web_agent.py#L1532) | 1532 | `"    assert len(result[\"sources\"]) == 1"` | — |
| [SRC-F725E90B2A-L001533](../../tests/test_web_agent.py#L1533) | 1533 | `"    assert result[\"sources\"][0][\"url\"] == \"https://digital.gov.eg/\""` | — |
| [SRC-F725E90B2A-L001534](../../tests/test_web_agent.py#L1534) | 1534 | `"    assert any(\"نتيجة مرشحة\" in warning for warning in result[\"warnings\"])"` | — |
| [SRC-F725E90B2A-L001535](../../tests/test_web_agent.py#L1535) | 1535 | `""` | — |
| [SRC-F725E90B2A-L001536](../../tests/test_web_agent.py#L1536) | 1536 | `""` | — |
| [SRC-F725E90B2A-L001537](../../tests/test_web_agent.py#L1537) | 1537 | `"def test_google_news_uses_shared_relevance_filter_and_reports_rejections(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001538](../../tests/test_web_agent.py#L1538) | 1538 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L001539](../../tests/test_web_agent.py#L1539) | 1539 | `""` | — |
| [SRC-F725E90B2A-L001540](../../tests/test_web_agent.py#L1540) | 1540 | `"    rss = \"\"\"<rss><channel>"` | — |
| [SRC-F725E90B2A-L001541](../../tests/test_web_agent.py#L1541) | 1541 | `"    <item>"` | — |
| [SRC-F725E90B2A-L001542](../../tests/test_web_agent.py#L1542) | 1542 | `"      <title>أكثر حالات استخدام الذكاء الاصطناعي قيمة للأعمال</title>"` | — |
| [SRC-F725E90B2A-L001543](../../tests/test_web_agent.py#L1543) | 1543 | `"      <link>https://news.google.com/rss/articles/relevant</link>"` | — |
| [SRC-F725E90B2A-L001544](../../tests/test_web_agent.py#L1544) | 1544 | `"      <description>أمثلة على استخدام الذكاء الاصطناعي في الأعمال</description>"` | — |
| [SRC-F725E90B2A-L001545](../../tests/test_web_agent.py#L1545) | 1545 | `"      <source url=\"https://www.ibm.com/\">IBM</source>"` | — |
| [SRC-F725E90B2A-L001546](../../tests/test_web_agent.py#L1546) | 1546 | `"      <pubDate>Tue, 27 Oct 2026 10:00:00 GMT</pubDate>"` | — |
| [SRC-F725E90B2A-L001547](../../tests/test_web_agent.py#L1547) | 1547 | `"    </item>"` | — |
| [SRC-F725E90B2A-L001548](../../tests/test_web_agent.py#L1548) | 1548 | `"    <item>"` | — |
| [SRC-F725E90B2A-L001549](../../tests/test_web_agent.py#L1549) | 1549 | `"      <title>نتائج بطولة كرة القدم اليوم</title>"` | — |
| [SRC-F725E90B2A-L001550](../../tests/test_web_agent.py#L1550) | 1550 | `"      <link>https://news.google.com/rss/articles/irrelevant</link>"` | — |
| [SRC-F725E90B2A-L001551](../../tests/test_web_agent.py#L1551) | 1551 | `"      <description>تقرير عن الدوري ونتائج المباراة</description>"` | — |
| [SRC-F725E90B2A-L001552](../../tests/test_web_agent.py#L1552) | 1552 | `"      <source url=\"https://example.org/\">Example News</source>"` | — |
| [SRC-F725E90B2A-L001553](../../tests/test_web_agent.py#L1553) | 1553 | `"      <pubDate>Tue, 27 Oct 2026 09:00:00 GMT</pubDate>"` | — |
| [SRC-F725E90B2A-L001554](../../tests/test_web_agent.py#L1554) | 1554 | `"    </item>"` | — |
| [SRC-F725E90B2A-L001555](../../tests/test_web_agent.py#L1555) | 1555 | `"    </channel></rss>\"\"\""` | — |
| [SRC-F725E90B2A-L001556](../../tests/test_web_agent.py#L1556) | 1556 | `""` | — |
| [SRC-F725E90B2A-L001557](../../tests/test_web_agent.py#L1557) | 1557 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L001558](../../tests/test_web_agent.py#L1558) | 1558 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L001559](../../tests/test_web_agent.py#L1559) | 1559 | `"        content = rss.encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L001560](../../tests/test_web_agent.py#L1560) | 1560 | `""` | — |
| [SRC-F725E90B2A-L001561](../../tests/test_web_agent.py#L1561) | 1561 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001562](../../tests/test_web_agent.py#L1562) | 1562 | `"    monkeypatch.setattr(httpx, \"get\", lambda *args, **kwargs: FakeResponse())"` | — |
| [SRC-F725E90B2A-L001563](../../tests/test_web_agent.py#L1563) | 1563 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _query: [])"` | — |
| [SRC-F725E90B2A-L001564](../../tests/test_web_agent.py#L1564) | 1564 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _query: [])"` | — |
| [SRC-F725E90B2A-L001565](../../tests/test_web_agent.py#L1565) | 1565 | `""` | — |
| [SRC-F725E90B2A-L001566](../../tests/test_web_agent.py#L1566) | 1566 | `"    results = agent._search_web(\"AI use cases for small businesses latest news\")"` | — |
| [SRC-F725E90B2A-L001567](../../tests/test_web_agent.py#L1567) | 1567 | `""` | — |
| [SRC-F725E90B2A-L001568](../../tests/test_web_agent.py#L1568) | 1568 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L001569](../../tests/test_web_agent.py#L1569) | 1569 | `"    assert results[0][\"title\"] == \"أكثر حالات استخدام الذكاء الاصطناعي قيمة للأعمال\""` | — |
| [SRC-F725E90B2A-L001570](../../tests/test_web_agent.py#L1570) | 1570 | `"    diagnostic = next("` | — |
| [SRC-F725E90B2A-L001571](../../tests/test_web_agent.py#L1571) | 1571 | `"        row for row in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L001572](../../tests/test_web_agent.py#L1572) | 1572 | `"        if row[\"provider\"] == \"google_news_rss\""` | — |
| [SRC-F725E90B2A-L001573](../../tests/test_web_agent.py#L1573) | 1573 | `"    )"` | — |
| [SRC-F725E90B2A-L001574](../../tests/test_web_agent.py#L1574) | 1574 | `"    assert diagnostic[\"status\"] == \"ok\""` | — |
| [SRC-F725E90B2A-L001575](../../tests/test_web_agent.py#L1575) | 1575 | `"    assert diagnostic[\"result_count\"] == 2"` | — |
| [SRC-F725E90B2A-L001576](../../tests/test_web_agent.py#L1576) | 1576 | `"    assert diagnostic[\"accepted_count\"] == 1"` | — |
| [SRC-F725E90B2A-L001577](../../tests/test_web_agent.py#L1577) | 1577 | `"    assert diagnostic[\"rejected_count\"] == 1"` | — |
| [SRC-F725E90B2A-L001578](../../tests/test_web_agent.py#L1578) | 1578 | `"    assert diagnostic[\"rejection_counts\"][\"relevance_below_threshold\"] == 1"` | — |
| [SRC-F725E90B2A-L001579](../../tests/test_web_agent.py#L1579) | 1579 | `""` | — |
| [SRC-F725E90B2A-L001580](../../tests/test_web_agent.py#L1580) | 1580 | `""` | — |
| [SRC-F725E90B2A-L001581](../../tests/test_web_agent.py#L1581) | 1581 | `"def test_google_news_preserves_publisher_identity(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001582](../../tests/test_web_agent.py#L1582) | 1582 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L001583](../../tests/test_web_agent.py#L1583) | 1583 | `""` | — |
| [SRC-F725E90B2A-L001584](../../tests/test_web_agent.py#L1584) | 1584 | `"    rss = \"\"\"<rss><channel><item>"` | — |
| [SRC-F725E90B2A-L001585](../../tests/test_web_agent.py#L1585) | 1585 | `"      <title>مصر الرقمية: تحديث جديد للخدمات</title>"` | — |
| [SRC-F725E90B2A-L001586](../../tests/test_web_agent.py#L1586) | 1586 | `"      <link>https://news.google.com/rss/articles/EXAMPLE123</link>"` | — |
| [SRC-F725E90B2A-L001587](../../tests/test_web_agent.py#L1587) | 1587 | `"      <description>معلومات عن بوابة مصر الرقمية والخدمات الإلكترونية.</description>"` | — |
| [SRC-F725E90B2A-L001588](../../tests/test_web_agent.py#L1588) | 1588 | `"      <source url=\"https://digital.gov.eg/\">بوابة مصر الرقمية</source>"` | — |
| [SRC-F725E90B2A-L001589](../../tests/test_web_agent.py#L1589) | 1589 | `"      <pubDate>Sat, 17 Oct 2026 10:00:00 GMT</pubDate>"` | — |
| [SRC-F725E90B2A-L001590](../../tests/test_web_agent.py#L1590) | 1590 | `"    </item></channel></rss>\"\"\""` | — |
| [SRC-F725E90B2A-L001591](../../tests/test_web_agent.py#L1591) | 1591 | `""` | — |
| [SRC-F725E90B2A-L001592](../../tests/test_web_agent.py#L1592) | 1592 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L001593](../../tests/test_web_agent.py#L1593) | 1593 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L001594](../../tests/test_web_agent.py#L1594) | 1594 | `"        content = rss.encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L001595](../../tests/test_web_agent.py#L1595) | 1595 | `""` | — |
| [SRC-F725E90B2A-L001596](../../tests/test_web_agent.py#L1596) | 1596 | `"    monkeypatch.setattr(httpx, \"get\", lambda *args, **kwargs: FakeResponse())"` | — |
| [SRC-F725E90B2A-L001597](../../tests/test_web_agent.py#L1597) | 1597 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001598](../../tests/test_web_agent.py#L1598) | 1598 | `"    results = agent._search_news(\"مصر الرقمية أحدث الأخبار\")"` | — |
| [SRC-F725E90B2A-L001599](../../tests/test_web_agent.py#L1599) | 1599 | `""` | — |
| [SRC-F725E90B2A-L001600](../../tests/test_web_agent.py#L1600) | 1600 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L001601](../../tests/test_web_agent.py#L1601) | 1601 | `"    assert results[0][\"url\"].startswith(\"https://news.google.com/\")"` | — |
| [SRC-F725E90B2A-L001602](../../tests/test_web_agent.py#L1602) | 1602 | `"    assert results[0][\"publisher_name\"] == \"بوابة مصر الرقمية\""` | — |
| [SRC-F725E90B2A-L001603](../../tests/test_web_agent.py#L1603) | 1603 | `"    assert results[0][\"publisher_url\"] == \"https://digital.gov.eg/\""` | — |
| [SRC-F725E90B2A-L001604](../../tests/test_web_agent.py#L1604) | 1604 | `"    assert results[0][\"publisher_domain\"] == \"digital.gov.eg\""` | — |
| [SRC-F725E90B2A-L001605](../../tests/test_web_agent.py#L1605) | 1605 | `""` | — |
| [SRC-F725E90B2A-L001606](../../tests/test_web_agent.py#L1606) | 1606 | `""` | — |
| [SRC-F725E90B2A-L001607](../../tests/test_web_agent.py#L1607) | 1607 | `"def test_relevance_matching_handles_arabic_names_with_english_results():"` | — |
| [SRC-F725E90B2A-L001608](../../tests/test_web_agent.py#L1608) | 1608 | `"    assert _relevance_ratio(\"ابحث عن ميكروسوفت\", \"Microsoft official company website\") >= 0.20"` | — |
| [SRC-F725E90B2A-L001609](../../tests/test_web_agent.py#L1609) | 1609 | `"    assert _relevance_ratio(\"موقع مصر الرقمية\", \"Egypt Digital portal for government services\") >= 0.20"` | — |
| [SRC-F725E90B2A-L001610](../../tests/test_web_agent.py#L1610) | 1610 | `"    assert _relevance_ratio(\"ابحث عن شقة للايجار\", \"Apartment listing available for rent\") >= 0.20"` | — |
| [SRC-F725E90B2A-L001611](../../tests/test_web_agent.py#L1611) | 1611 | `"    assert _relevance_ratio(\"مقارنة بين الشركات الناشئة\", \"Comparison of startup companies\") >= 0.20"` | — |
| [SRC-F725E90B2A-L001612](../../tests/test_web_agent.py#L1612) | 1612 | `""` | — |
| [SRC-F725E90B2A-L001613](../../tests/test_web_agent.py#L1613) | 1613 | `"def test_relevance_matching_handles_english_ai_use_cases_with_arabic_results():"` | — |
| [SRC-F725E90B2A-L001614](../../tests/test_web_agent.py#L1614) | 1614 | `"    assert _relevance_ratio("` | — |
| [SRC-F725E90B2A-L001615](../../tests/test_web_agent.py#L1615) | 1615 | `"        \"AI use cases for small businesses\","` | — |
| [SRC-F725E90B2A-L001616](../../tests/test_web_agent.py#L1616) | 1616 | `"        \"أكثر حالات استخدام الذكاء الاصطناعي قيمة للأعمال\","` | — |
| [SRC-F725E90B2A-L001617](../../tests/test_web_agent.py#L1617) | 1617 | `"    ) >= 0.20"` | — |
| [SRC-F725E90B2A-L001618](../../tests/test_web_agent.py#L1618) | 1618 | `"    assert _relevance_ratio("` | — |
| [SRC-F725E90B2A-L001619](../../tests/test_web_agent.py#L1619) | 1619 | `"        \"استخدامات الذكاء الاصطناعي في الشركات الصغيرة\","` | — |
| [SRC-F725E90B2A-L001620](../../tests/test_web_agent.py#L1620) | 1620 | `"        \"AI use cases for small businesses\","` | — |
| [SRC-F725E90B2A-L001621](../../tests/test_web_agent.py#L1621) | 1621 | `"    ) >= 0.20"` | — |
| [SRC-F725E90B2A-L001622](../../tests/test_web_agent.py#L1622) | 1622 | `""` | — |
| [SRC-F725E90B2A-L001623](../../tests/test_web_agent.py#L1623) | 1623 | `""` | — |
| [SRC-F725E90B2A-L001624](../../tests/test_web_agent.py#L1624) | 1624 | `"def test_routine_lookup_ignores_planner_overclassification(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001625](../../tests/test_web_agent.py#L1625) | 1625 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001626](../../tests/test_web_agent.py#L1626) | 1626 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L001627](../../tests/test_web_agent.py#L1627) | 1627 | `"    observed = {}"` | — |
| [SRC-F725E90B2A-L001628](../../tests/test_web_agent.py#L1628) | 1628 | `"    sources = []"` | — |
| [SRC-F725E90B2A-L001629](../../tests/test_web_agent.py#L1629) | 1629 | `"    for domain in (\"example.com\", \"example.net\"):"` | — |
| [SRC-F725E90B2A-L001630](../../tests/test_web_agent.py#L1630) | 1630 | `"        sources.append({"` | — |
| [SRC-F725E90B2A-L001631](../../tests/test_web_agent.py#L1631) | 1631 | `"            \"title\": \"موقع مصر الرقمية الرسمي والخدمات الحكومية\","` | — |
| [SRC-F725E90B2A-L001632](../../tests/test_web_agent.py#L1632) | 1632 | `"            \"url\": f\"https://{domain}/digital-egypt\","` | — |
| [SRC-F725E90B2A-L001633](../../tests/test_web_agent.py#L1633) | 1633 | `"            \"snippet\": \"معلومات عن موقع مصر الرقمية والخدمات الحكومية.\","` | — |
| [SRC-F725E90B2A-L001634](../../tests/test_web_agent.py#L1634) | 1634 | `"            \"page_text\": \"معلومات عن موقع مصر الرقمية والخدمات الحكومية.\","` | — |
| [SRC-F725E90B2A-L001635](../../tests/test_web_agent.py#L1635) | 1635 | `"            \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L001636](../../tests/test_web_agent.py#L1636) | 1636 | `"            \"providers\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001637](../../tests/test_web_agent.py#L1637) | 1637 | `"            \"queries\": [],"` | — |
| [SRC-F725E90B2A-L001638](../../tests/test_web_agent.py#L1638) | 1638 | `"            \"domain\": domain,"` | — |
| [SRC-F725E90B2A-L001639](../../tests/test_web_agent.py#L1639) | 1639 | `"            \"source_class\": \"general\","` | — |
| [SRC-F725E90B2A-L001640](../../tests/test_web_agent.py#L1640) | 1640 | `"            \"platform\": \"web\","` | — |
| [SRC-F725E90B2A-L001641](../../tests/test_web_agent.py#L1641) | 1641 | `"        })"` | — |
| [SRC-F725E90B2A-L001642](../../tests/test_web_agent.py#L1642) | 1642 | `""` | — |
| [SRC-F725E90B2A-L001643](../../tests/test_web_agent.py#L1643) | 1643 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001644](../../tests/test_web_agent.py#L1644) | 1644 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L001645](../../tests/test_web_agent.py#L1645) | 1645 | `"        lambda question, history: {"` | — |
| [SRC-F725E90B2A-L001646](../../tests/test_web_agent.py#L1646) | 1646 | `"            \"queries\": [f\"query {i}\" for i in range(8)],"` | — |
| [SRC-F725E90B2A-L001647](../../tests/test_web_agent.py#L1647) | 1647 | `"            \"direct_urls\": [], \"social_focus\": False, \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L001648](../../tests/test_web_agent.py#L1648) | 1648 | `"            \"depth\": \"deep\", \"platforms\": [], \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001649](../../tests/test_web_agent.py#L1649) | 1649 | `"        },"` | — |
| [SRC-F725E90B2A-L001650](../../tests/test_web_agent.py#L1650) | 1650 | `"    )"` | — |
| [SRC-F725E90B2A-L001651](../../tests/test_web_agent.py#L1651) | 1651 | `""` | — |
| [SRC-F725E90B2A-L001652](../../tests/test_web_agent.py#L1652) | 1652 | `"    def collect(plan):"` | — |
| [SRC-F725E90B2A-L001653](../../tests/test_web_agent.py#L1653) | 1653 | `"        observed[\"plan\"] = plan"` | — |
| [SRC-F725E90B2A-L001654](../../tests/test_web_agent.py#L1654) | 1654 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L001655](../../tests/test_web_agent.py#L1655) | 1655 | `"            \"queries_planned\": len(plan[\"queries\"]), \"queries_attempted\": len(plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L001656](../../tests/test_web_agent.py#L1656) | 1656 | `"            \"unique_sources\": 2, \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L001657](../../tests/test_web_agent.py#L1657) | 1657 | `"            \"providers_used\": [\"test_provider\"], \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-F725E90B2A-L001658](../../tests/test_web_agent.py#L1658) | 1658 | `"            \"social_direct_results\": 0, \"depth\": plan[\"depth\"], \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001659](../../tests/test_web_agent.py#L1659) | 1659 | `"        }"` | — |
| [SRC-F725E90B2A-L001660](../../tests/test_web_agent.py#L1660) | 1660 | `""` | — |
| [SRC-F725E90B2A-L001661](../../tests/test_web_agent.py#L1661) | 1661 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L001662](../../tests/test_web_agent.py#L1662) | 1662 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"النتيجة [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L001663](../../tests/test_web_agent.py#L1663) | 1663 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L001664](../../tests/test_web_agent.py#L1664) | 1664 | `""` | — |
| [SRC-F725E90B2A-L001665](../../tests/test_web_agent.py#L1665) | 1665 | `"    result = agent.answer(\"ابحث عن موقع مصر الرقمية\")"` | — |
| [SRC-F725E90B2A-L001666](../../tests/test_web_agent.py#L1666) | 1666 | `""` | — |
| [SRC-F725E90B2A-L001667](../../tests/test_web_agent.py#L1667) | 1667 | `"    assert result[\"kind\"] == \"web_research\""` | — |
| [SRC-F725E90B2A-L001668](../../tests/test_web_agent.py#L1668) | 1668 | `"    assert observed[\"plan\"][\"depth\"] == \"standard\""` | — |
| [SRC-F725E90B2A-L001669](../../tests/test_web_agent.py#L1669) | 1669 | `"    assert len(observed[\"plan\"][\"queries\"]) <= 3"` | — |
| [SRC-F725E90B2A-L001670](../../tests/test_web_agent.py#L1670) | 1670 | `"    assert observed[\"plan\"][\"queries\"][0] == \"موقع مصر الرقمية\""` | — |
| [SRC-F725E90B2A-L001671](../../tests/test_web_agent.py#L1671) | 1671 | `""` | — |
| [SRC-F725E90B2A-L001672](../../tests/test_web_agent.py#L1672) | 1672 | `""` | — |
| [SRC-F725E90B2A-L001673](../../tests/test_web_agent.py#L1673) | 1673 | `"def test_listing_discovery_detects_arabic_property_requests():"` | — |
| [SRC-F725E90B2A-L001674](../../tests/test_web_agent.py#L1674) | 1674 | `"    assert WebAgent._is_listing_discovery(\"ابحث عن شقة في التجمع الخامس، ممكن معاينة\")"` | — |
| [SRC-F725E90B2A-L001675](../../tests/test_web_agent.py#L1675) | 1675 | `"    assert WebAgent._is_listing_discovery(\"عايز شقق للايجار في القاهرة\")"` | — |
| [SRC-F725E90B2A-L001676](../../tests/test_web_agent.py#L1676) | 1676 | `"    assert not WebAgent._is_listing_discovery(\"اشرح الفرق بين الشقة والفيلا\")"` | — |
| [SRC-F725E90B2A-L001677](../../tests/test_web_agent.py#L1677) | 1677 | `""` | — |
| [SRC-F725E90B2A-L001678](../../tests/test_web_agent.py#L1678) | 1678 | `""` | — |
| [SRC-F725E90B2A-L001679](../../tests/test_web_agent.py#L1679) | 1679 | `"def test_single_property_listing_is_returned_with_safety_caveat(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001680](../../tests/test_web_agent.py#L1680) | 1680 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001681](../../tests/test_web_agent.py#L1681) | 1681 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L001682](../../tests/test_web_agent.py#L1682) | 1682 | `"    source = {"` | — |
| [SRC-F725E90B2A-L001683](../../tests/test_web_agent.py#L1683) | 1683 | `"        \"title\": \"شقة للبيع في التجمع الخامس\","` | — |
| [SRC-F725E90B2A-L001684](../../tests/test_web_agent.py#L1684) | 1684 | `"        \"url\": \"https://example.com/listing/123\","` | — |
| [SRC-F725E90B2A-L001685](../../tests/test_web_agent.py#L1685) | 1685 | `"        \"snippet\": \"شقة في التجمع الخامس، معاينة بالتنسيق مع المعلن.\","` | — |
| [SRC-F725E90B2A-L001686](../../tests/test_web_agent.py#L1686) | 1686 | `"        \"page_text\": \"شقة في التجمع الخامس، معاينة بالتنسيق مع المعلن.\","` | — |
| [SRC-F725E90B2A-L001687](../../tests/test_web_agent.py#L1687) | 1687 | `"        \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L001688](../../tests/test_web_agent.py#L1688) | 1688 | `"        \"providers\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001689](../../tests/test_web_agent.py#L1689) | 1689 | `"        \"queries\": [\"شقة في التجمع الخامس\"],"` | — |
| [SRC-F725E90B2A-L001690](../../tests/test_web_agent.py#L1690) | 1690 | `"        \"domain\": \"example.com\","` | — |
| [SRC-F725E90B2A-L001691](../../tests/test_web_agent.py#L1691) | 1691 | `"        \"source_class\": \"general\","` | — |
| [SRC-F725E90B2A-L001692](../../tests/test_web_agent.py#L1692) | 1692 | `"        \"platform\": \"web\","` | — |
| [SRC-F725E90B2A-L001693](../../tests/test_web_agent.py#L1693) | 1693 | `"    }"` | — |
| [SRC-F725E90B2A-L001694](../../tests/test_web_agent.py#L1694) | 1694 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001695](../../tests/test_web_agent.py#L1695) | 1695 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L001696](../../tests/test_web_agent.py#L1696) | 1696 | `"        lambda question, history: {"` | — |
| [SRC-F725E90B2A-L001697](../../tests/test_web_agent.py#L1697) | 1697 | `"            \"queries\": [question], \"direct_urls\": [], \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001698](../../tests/test_web_agent.py#L1698) | 1698 | `"            \"freshness\": \"any\", \"depth\": \"standard\", \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001699](../../tests/test_web_agent.py#L1699) | 1699 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001700](../../tests/test_web_agent.py#L1700) | 1700 | `"        },"` | — |
| [SRC-F725E90B2A-L001701](../../tests/test_web_agent.py#L1701) | 1701 | `"    )"` | — |
| [SRC-F725E90B2A-L001702](../../tests/test_web_agent.py#L1702) | 1702 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001703](../../tests/test_web_agent.py#L1703) | 1703 | `"        agent, \"_collect_research\","` | — |
| [SRC-F725E90B2A-L001704](../../tests/test_web_agent.py#L1704) | 1704 | `"        lambda plan: ([source], [], {"` | — |
| [SRC-F725E90B2A-L001705](../../tests/test_web_agent.py#L1705) | 1705 | `"            \"queries_planned\": 1, \"queries_attempted\": 1, \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L001706](../../tests/test_web_agent.py#L1706) | 1706 | `"            \"pages_fetched\": 1, \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001707](../../tests/test_web_agent.py#L1707) | 1707 | `"            \"platform_counts\": {\"web\": 1}, \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001708](../../tests/test_web_agent.py#L1708) | 1708 | `"            \"depth\": \"standard\", \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001709](../../tests/test_web_agent.py#L1709) | 1709 | `"        }),"` | — |
| [SRC-F725E90B2A-L001710](../../tests/test_web_agent.py#L1710) | 1710 | `"    )"` | — |
| [SRC-F725E90B2A-L001711](../../tests/test_web_agent.py#L1711) | 1711 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001712](../../tests/test_web_agent.py#L1712) | 1712 | `"        agent, \"_generate\","` | — |
| [SRC-F725E90B2A-L001713](../../tests/test_web_agent.py#L1713) | 1713 | `"        lambda *args, **kwargs: \"وجدت إعلانًا مرشحًا لشقة؛ تحقق من التفاصيل [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L001714](../../tests/test_web_agent.py#L1714) | 1714 | `"    )"` | — |
| [SRC-F725E90B2A-L001715](../../tests/test_web_agent.py#L1715) | 1715 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L001716](../../tests/test_web_agent.py#L1716) | 1716 | `""` | — |
| [SRC-F725E90B2A-L001717](../../tests/test_web_agent.py#L1717) | 1717 | `"    result = agent.answer(\"ابحث عن شقة في التجمع الخامس، ممكن معاينة\")"` | — |
| [SRC-F725E90B2A-L001718](../../tests/test_web_agent.py#L1718) | 1718 | `""` | — |
| [SRC-F725E90B2A-L001719](../../tests/test_web_agent.py#L1719) | 1719 | `"    assert result[\"kind\"] == \"web_research\""` | — |
| [SRC-F725E90B2A-L001720](../../tests/test_web_agent.py#L1720) | 1720 | `"    assert len(result[\"sources\"]) == 1"` | — |
| [SRC-F725E90B2A-L001721](../../tests/test_web_agent.py#L1721) | 1721 | `"    assert \"إعلانات/قوائم مرشحة فقط\" in \" \".join(result[\"warnings\"])"` | — |
| [SRC-F725E90B2A-L001722](../../tests/test_web_agent.py#L1722) | 1722 | `""` | — |
| [SRC-F725E90B2A-L001723](../../tests/test_web_agent.py#L1723) | 1723 | `""` | — |
| [SRC-F725E90B2A-L001724](../../tests/test_web_agent.py#L1724) | 1724 | `""` | — |
| [SRC-F725E90B2A-L001725](../../tests/test_web_agent.py#L1725) | 1725 | `"def test_normalized_source_url_key_ignores_tracking_parameters_and_fragment():"` | — |
| [SRC-F725E90B2A-L001726](../../tests/test_web_agent.py#L1726) | 1726 | `"    normalize = WebAgent._normalized_source_url_key"` | — |
| [SRC-F725E90B2A-L001727](../../tests/test_web_agent.py#L1727) | 1727 | `"    assert normalize(\"HTTPS://EXAMPLE.COM:443/article/?utm_source=newsletter#section\") == ("` | — |
| [SRC-F725E90B2A-L001728](../../tests/test_web_agent.py#L1728) | 1728 | `"        \"https://example.com/article\""` | — |
| [SRC-F725E90B2A-L001729](../../tests/test_web_agent.py#L1729) | 1729 | `"    )"` | — |
| [SRC-F725E90B2A-L001730](../../tests/test_web_agent.py#L1730) | 1730 | `"    assert normalize(\"https://example.com/article?fbclid=abc&x=1\") == ("` | — |
| [SRC-F725E90B2A-L001731](../../tests/test_web_agent.py#L1731) | 1731 | `"        \"https://example.com/article?x=1\""` | — |
| [SRC-F725E90B2A-L001732](../../tests/test_web_agent.py#L1732) | 1732 | `"    )"` | — |
| [SRC-F725E90B2A-L001733](../../tests/test_web_agent.py#L1733) | 1733 | `"    assert normalize(\"file:///etc/passwd\") == \"\""` | — |
| [SRC-F725E90B2A-L001734](../../tests/test_web_agent.py#L1734) | 1734 | `""` | — |
| [SRC-F725E90B2A-L001735](../../tests/test_web_agent.py#L1735) | 1735 | `""` | — |
| [SRC-F725E90B2A-L001736](../../tests/test_web_agent.py#L1736) | 1736 | `"def test_bounded_repair_deduplicates_same_page_even_with_tracking_url(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001737](../../tests/test_web_agent.py#L1737) | 1737 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001738](../../tests/test_web_agent.py#L1738) | 1738 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001739](../../tests/test_web_agent.py#L1739) | 1739 | `"        \"queries\": [\"معلومات عن شركة ألفا اليوم\"],"` | — |
| [SRC-F725E90B2A-L001740](../../tests/test_web_agent.py#L1740) | 1740 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L001741](../../tests/test_web_agent.py#L1741) | 1741 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001742](../../tests/test_web_agent.py#L1742) | 1742 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L001743](../../tests/test_web_agent.py#L1743) | 1743 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001744](../../tests/test_web_agent.py#L1744) | 1744 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001745](../../tests/test_web_agent.py#L1745) | 1745 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001746](../../tests/test_web_agent.py#L1746) | 1746 | `"    }"` | — |
| [SRC-F725E90B2A-L001747](../../tests/test_web_agent.py#L1747) | 1747 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L001748](../../tests/test_web_agent.py#L1748) | 1748 | `""` | — |
| [SRC-F725E90B2A-L001749](../../tests/test_web_agent.py#L1749) | 1749 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L001750](../../tests/test_web_agent.py#L1750) | 1750 | `"        calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L001751](../../tests/test_web_agent.py#L1751) | 1751 | `"        source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L001752](../../tests/test_web_agent.py#L1752) | 1752 | `"        if len(calls) > 1:"` | — |
| [SRC-F725E90B2A-L001753](../../tests/test_web_agent.py#L1753) | 1753 | `"            source[\"url\"] = \"https://EXAMPLE.com/research/?utm_source=test#details\""` | — |
| [SRC-F725E90B2A-L001754](../../tests/test_web_agent.py#L1754) | 1754 | `"            source[\"providers\"] = [\"second_provider\"]"` | — |
| [SRC-F725E90B2A-L001755](../../tests/test_web_agent.py#L1755) | 1755 | `"            source[\"page_fetched\"] = False"` | — |
| [SRC-F725E90B2A-L001756](../../tests/test_web_agent.py#L1756) | 1756 | `"        return [source], [], {"` | — |
| [SRC-F725E90B2A-L001757](../../tests/test_web_agent.py#L1757) | 1757 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L001758](../../tests/test_web_agent.py#L1758) | 1758 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001759](../../tests/test_web_agent.py#L1759) | 1759 | `"            \"query_results\": [{\"query\": research_plan[\"queries\"][0], \"results\": 1}],"` | — |
| [SRC-F725E90B2A-L001760](../../tests/test_web_agent.py#L1760) | 1760 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L001761](../../tests/test_web_agent.py#L1761) | 1761 | `"            \"pages_fetched\": 1 if len(calls) == 1 else 0,"` | — |
| [SRC-F725E90B2A-L001762](../../tests/test_web_agent.py#L1762) | 1762 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001763](../../tests/test_web_agent.py#L1763) | 1763 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L001764](../../tests/test_web_agent.py#L1764) | 1764 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001765](../../tests/test_web_agent.py#L1765) | 1765 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001766](../../tests/test_web_agent.py#L1766) | 1766 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001767](../../tests/test_web_agent.py#L1767) | 1767 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L001768](../../tests/test_web_agent.py#L1768) | 1768 | `"        }"` | — |
| [SRC-F725E90B2A-L001769](../../tests/test_web_agent.py#L1769) | 1769 | `""` | — |
| [SRC-F725E90B2A-L001770](../../tests/test_web_agent.py#L1770) | 1770 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001771](../../tests/test_web_agent.py#L1771) | 1771 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L001772](../../tests/test_web_agent.py#L1772) | 1772 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L001773](../../tests/test_web_agent.py#L1773) | 1773 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001774](../../tests/test_web_agent.py#L1774) | 1774 | `"        agent, \"_generate\","` | — |
| [SRC-F725E90B2A-L001775](../../tests/test_web_agent.py#L1775) | 1775 | `"        lambda *args, **kwargs: pytest.fail(\"Duplicate URL must not satisfy corroboration\"),"` | — |
| [SRC-F725E90B2A-L001776](../../tests/test_web_agent.py#L1776) | 1776 | `"    )"` | — |
| [SRC-F725E90B2A-L001777](../../tests/test_web_agent.py#L1777) | 1777 | `""` | — |
| [SRC-F725E90B2A-L001778](../../tests/test_web_agent.py#L1778) | 1778 | `"    result = agent.answer(\"ما آخر معلومات عن شركة ألفا اليوم؟\")"` | — |
| [SRC-F725E90B2A-L001779](../../tests/test_web_agent.py#L1779) | 1779 | `""` | — |
| [SRC-F725E90B2A-L001780](../../tests/test_web_agent.py#L1780) | 1780 | `"    assert len(calls) == 2"` | — |
| [SRC-F725E90B2A-L001781](../../tests/test_web_agent.py#L1781) | 1781 | `"    repair = result[\"search_report\"][\"evidence_repair\"]"` | — |
| [SRC-F725E90B2A-L001782](../../tests/test_web_agent.py#L1782) | 1782 | `"    assert repair[\"attempted\"] is True"` | — |
| [SRC-F725E90B2A-L001783](../../tests/test_web_agent.py#L1783) | 1783 | `"    assert repair[\"new_sources_added\"] == 0"` | — |
| [SRC-F725E90B2A-L001784](../../tests/test_web_agent.py#L1784) | 1784 | `"    assert repair[\"recovered\"] is False"` | — |
| [SRC-F725E90B2A-L001785](../../tests/test_web_agent.py#L1785) | 1785 | `"    assert result[\"search_report\"][\"independent_sources\"] == 0"` | — |
| [SRC-F725E90B2A-L001786](../../tests/test_web_agent.py#L1786) | 1786 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L001787](../../tests/test_web_agent.py#L1787) | 1787 | `"    assert result[\"search_report\"][\"source_guardrails\"][\"final\"][\"current_evidence_status\"] == \"no_current_eligible_evidence\""` | — |
| [SRC-F725E90B2A-L001788](../../tests/test_web_agent.py#L1788) | 1788 | `""` | — |
| [SRC-F725E90B2A-L001789](../../tests/test_web_agent.py#L1789) | 1789 | `""` | — |
| [SRC-F725E90B2A-L001790](../../tests/test_web_agent.py#L1790) | 1790 | `"def test_social_focused_partial_evidence_does_not_trigger_general_repair(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001791](../../tests/test_web_agent.py#L1791) | 1791 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001792](../../tests/test_web_agent.py#L1792) | 1792 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001793](../../tests/test_web_agent.py#L1793) | 1793 | `"        \"queries\": [\"تجارب المستخدمين حول التقنية\"],"` | — |
| [SRC-F725E90B2A-L001794](../../tests/test_web_agent.py#L1794) | 1794 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L001795](../../tests/test_web_agent.py#L1795) | 1795 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001796](../../tests/test_web_agent.py#L1796) | 1796 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L001797](../../tests/test_web_agent.py#L1797) | 1797 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001798](../../tests/test_web_agent.py#L1798) | 1798 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001799](../../tests/test_web_agent.py#L1799) | 1799 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001800](../../tests/test_web_agent.py#L1800) | 1800 | `"    }"` | — |
| [SRC-F725E90B2A-L001801](../../tests/test_web_agent.py#L1801) | 1801 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L001802](../../tests/test_web_agent.py#L1802) | 1802 | `""` | — |
| [SRC-F725E90B2A-L001803](../../tests/test_web_agent.py#L1803) | 1803 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L001804](../../tests/test_web_agent.py#L1804) | 1804 | `"        calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L001805](../../tests/test_web_agent.py#L1805) | 1805 | `"        social_source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L001806](../../tests/test_web_agent.py#L1806) | 1806 | `"        social_source.update({"` | — |
| [SRC-F725E90B2A-L001807](../../tests/test_web_agent.py#L1807) | 1807 | `"            \"url\": \"https://www.reddit.com/r/example/comments/test\","` | — |
| [SRC-F725E90B2A-L001808](../../tests/test_web_agent.py#L1808) | 1808 | `"            \"domain\": \"reddit.com\","` | — |
| [SRC-F725E90B2A-L001809](../../tests/test_web_agent.py#L1809) | 1809 | `"            \"platform\": \"reddit\","` | — |
| [SRC-F725E90B2A-L001810](../../tests/test_web_agent.py#L1810) | 1810 | `"            \"source_class\": \"social\","` | — |
| [SRC-F725E90B2A-L001811](../../tests/test_web_agent.py#L1811) | 1811 | `"        })"` | — |
| [SRC-F725E90B2A-L001812](../../tests/test_web_agent.py#L1812) | 1812 | `"        return [social_source], [], {"` | — |
| [SRC-F725E90B2A-L001813](../../tests/test_web_agent.py#L1813) | 1813 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L001814](../../tests/test_web_agent.py#L1814) | 1814 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001815](../../tests/test_web_agent.py#L1815) | 1815 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L001816](../../tests/test_web_agent.py#L1816) | 1816 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L001817](../../tests/test_web_agent.py#L1817) | 1817 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L001818](../../tests/test_web_agent.py#L1818) | 1818 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001819](../../tests/test_web_agent.py#L1819) | 1819 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L001820](../../tests/test_web_agent.py#L1820) | 1820 | `"            \"social_direct_results\": 1,"` | — |
| [SRC-F725E90B2A-L001821](../../tests/test_web_agent.py#L1821) | 1821 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001822](../../tests/test_web_agent.py#L1822) | 1822 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001823](../../tests/test_web_agent.py#L1823) | 1823 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L001824](../../tests/test_web_agent.py#L1824) | 1824 | `"        }"` | — |
| [SRC-F725E90B2A-L001825](../../tests/test_web_agent.py#L1825) | 1825 | `""` | — |
| [SRC-F725E90B2A-L001826](../../tests/test_web_agent.py#L1826) | 1826 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001827](../../tests/test_web_agent.py#L1827) | 1827 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L001828](../../tests/test_web_agent.py#L1828) | 1828 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L001829](../../tests/test_web_agent.py#L1829) | 1829 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"إشارات أولية فقط [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L001830](../../tests/test_web_agent.py#L1830) | 1830 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L001831](../../tests/test_web_agent.py#L1831) | 1831 | `""` | — |
| [SRC-F725E90B2A-L001832](../../tests/test_web_agent.py#L1832) | 1832 | `"    result = agent.answer(\"اجمع آراء الناس حول هذه التقنية\", mode=\"social\")"` | — |
| [SRC-F725E90B2A-L001833](../../tests/test_web_agent.py#L1833) | 1833 | `""` | — |
| [SRC-F725E90B2A-L001834](../../tests/test_web_agent.py#L1834) | 1834 | `"    assert len(calls) == 1"` | — |
| [SRC-F725E90B2A-L001835](../../tests/test_web_agent.py#L1835) | 1835 | `"    assert calls[0][\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L001836](../../tests/test_web_agent.py#L1836) | 1836 | `"    assert result[\"search_report\"][\"evidence_repair\"][\"attempted\"] is False"` | — |
| [SRC-F725E90B2A-L001837](../../tests/test_web_agent.py#L1837) | 1837 | `"    assert result[\"search_report\"][\"evidence_repair\"][\"reason\"] == \"task_specific_partial_evidence\""` | — |
| [SRC-F725E90B2A-L001838](../../tests/test_web_agent.py#L1838) | 1838 | `"    assert result[\"research_quality\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L001839](../../tests/test_web_agent.py#L1839) | 1839 | `""` | — |
| [SRC-F725E90B2A-L001840](../../tests/test_web_agent.py#L1840) | 1840 | `""` | — |
| [SRC-F725E90B2A-L001841](../../tests/test_web_agent.py#L1841) | 1841 | `""` | — |
| [SRC-F725E90B2A-L001842](../../tests/test_web_agent.py#L1842) | 1842 | `"def test_question_coverage_targets_extract_arabic_and_english_explicit_criteria():"` | — |
| [SRC-F725E90B2A-L001843](../../tests/test_web_agent.py#L1843) | 1843 | `"    arabic = WebAgent._question_coverage_targets("` | — |
| [SRC-F725E90B2A-L001844](../../tests/test_web_agent.py#L1844) | 1844 | `"        \"قارن بين خدمتين من حيث السعر، الخصوصية، الاعتمادية، وخيار التواصل مع الدعم، \""` | — |
| [SRC-F725E90B2A-L001845](../../tests/test_web_agent.py#L1845) | 1845 | `"        \"واذكر ما لا تستطيع التحقق منه.\""` | — |
| [SRC-F725E90B2A-L001846](../../tests/test_web_agent.py#L1846) | 1846 | `"    )"` | — |
| [SRC-F725E90B2A-L001847](../../tests/test_web_agent.py#L1847) | 1847 | `"    assert arabic == [\"السعر\", \"الخصوصية\", \"الاعتمادية\", \"خيار التواصل مع الدعم\"]"` | — |
| [SRC-F725E90B2A-L001848](../../tests/test_web_agent.py#L1848) | 1848 | `""` | — |
| [SRC-F725E90B2A-L001849](../../tests/test_web_agent.py#L1849) | 1849 | `"    english = WebAgent._question_coverage_targets("` | — |
| [SRC-F725E90B2A-L001850](../../tests/test_web_agent.py#L1850) | 1850 | `"        \"Compare two services in terms of price, privacy, reliability and customer support?\""` | — |
| [SRC-F725E90B2A-L001851](../../tests/test_web_agent.py#L1851) | 1851 | `"    )"` | — |
| [SRC-F725E90B2A-L001852](../../tests/test_web_agent.py#L1852) | 1852 | `"    assert english == [\"price\", \"privacy\", \"reliability\", \"customer support\"]"` | — |
| [SRC-F725E90B2A-L001853](../../tests/test_web_agent.py#L1853) | 1853 | `""` | — |
| [SRC-F725E90B2A-L001854](../../tests/test_web_agent.py#L1854) | 1854 | `"    english_with_period = WebAgent._question_coverage_targets("` | — |
| [SRC-F725E90B2A-L001855](../../tests/test_web_agent.py#L1855) | 1855 | `"        \"Compare two services in terms of price, privacy and reliability.\""` | — |
| [SRC-F725E90B2A-L001856](../../tests/test_web_agent.py#L1856) | 1856 | `"    )"` | — |
| [SRC-F725E90B2A-L001857](../../tests/test_web_agent.py#L1857) | 1857 | `"    assert english_with_period == [\"price\", \"privacy\", \"reliability\"]"` | — |
| [SRC-F725E90B2A-L001858](../../tests/test_web_agent.py#L1858) | 1858 | `""` | — |
| [SRC-F725E90B2A-L001859](../../tests/test_web_agent.py#L1859) | 1859 | `""` | — |
| [SRC-F725E90B2A-L001860](../../tests/test_web_agent.py#L1860) | 1860 | `"def test_question_coverage_targets_do_not_invent_parts_for_simple_question():"` | — |
| [SRC-F725E90B2A-L001861](../../tests/test_web_agent.py#L1861) | 1861 | `"    assert WebAgent._question_coverage_targets(\"ما الذي يقوله المصدر؟\") == []"` | — |
| [SRC-F725E90B2A-L001862](../../tests/test_web_agent.py#L1862) | 1862 | `""` | — |
| [SRC-F725E90B2A-L001863](../../tests/test_web_agent.py#L1863) | 1863 | `""` | — |
| [SRC-F725E90B2A-L001864](../../tests/test_web_agent.py#L1864) | 1864 | `"def test_generator_includes_extracted_targets_as_a_non_authoritative_checklist(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001865](../../tests/test_web_agent.py#L1865) | 1865 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001866](../../tests/test_web_agent.py#L1866) | 1866 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L001867](../../tests/test_web_agent.py#L1867) | 1867 | `""` | — |
| [SRC-F725E90B2A-L001868](../../tests/test_web_agent.py#L1868) | 1868 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L001869](../../tests/test_web_agent.py#L1869) | 1869 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L001870](../../tests/test_web_agent.py#L1870) | 1870 | `"        return \"مقارنة مختصرة.\""` | — |
| [SRC-F725E90B2A-L001871](../../tests/test_web_agent.py#L1871) | 1871 | `""` | — |
| [SRC-F725E90B2A-L001872](../../tests/test_web_agent.py#L1872) | 1872 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L001873](../../tests/test_web_agent.py#L1873) | 1873 | `"    result = agent._generate("` | — |
| [SRC-F725E90B2A-L001874](../../tests/test_web_agent.py#L1874) | 1874 | `"        question=\"قارن بين خدمتين من حيث السعر، الخصوصية والاعتمادية\","` | — |
| [SRC-F725E90B2A-L001875](../../tests/test_web_agent.py#L1875) | 1875 | `"        history=[],"` | — |
| [SRC-F725E90B2A-L001876](../../tests/test_web_agent.py#L1876) | 1876 | `"        sources=[sample_source(0), sample_source(1)],"` | — |
| [SRC-F725E90B2A-L001877](../../tests/test_web_agent.py#L1877) | 1877 | `"        search_warning=None,"` | — |
| [SRC-F725E90B2A-L001878](../../tests/test_web_agent.py#L1878) | 1878 | `"        research_plan={\"depth\": \"deep\", \"queries\": [\"مقارنة الخدمتين\"]},"` | — |
| [SRC-F725E90B2A-L001879](../../tests/test_web_agent.py#L1879) | 1879 | `"        search_report={},"` | — |
| [SRC-F725E90B2A-L001880](../../tests/test_web_agent.py#L1880) | 1880 | `"    )"` | — |
| [SRC-F725E90B2A-L001881](../../tests/test_web_agent.py#L1881) | 1881 | `""` | — |
| [SRC-F725E90B2A-L001882](../../tests/test_web_agent.py#L1882) | 1882 | `"    user_content = \"\\n\".join(m[\"content\"] for m in captured[\"messages\"] if m[\"role\"] == \"user\")"` | — |
| [SRC-F725E90B2A-L001883](../../tests/test_web_agent.py#L1883) | 1883 | `"    assert result == \"مقارنة مختصرة.\""` | — |
| [SRC-F725E90B2A-L001884](../../tests/test_web_agent.py#L1884) | 1884 | `"    assert \"قائمة محاور مستخرجة آليًا\" in user_content"` | — |
| [SRC-F725E90B2A-L001885](../../tests/test_web_agent.py#L1885) | 1885 | `"    for target in (\"السعر\", \"الخصوصية\", \"الاعتمادية\"):"` | — |
| [SRC-F725E90B2A-L001886](../../tests/test_web_agent.py#L1886) | 1886 | `"        assert target in user_content"` | — |
| [SRC-F725E90B2A-L001887](../../tests/test_web_agent.py#L1887) | 1887 | `""` | — |
| [SRC-F725E90B2A-L001888](../../tests/test_web_agent.py#L1888) | 1888 | `""` | — |
| [SRC-F725E90B2A-L001889](../../tests/test_web_agent.py#L1889) | 1889 | `"def test_reviewer_checks_coverage_targets_without_claiming_independent_verification(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001890](../../tests/test_web_agent.py#L1890) | 1890 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001891](../../tests/test_web_agent.py#L1891) | 1891 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L001892](../../tests/test_web_agent.py#L1892) | 1892 | `""` | — |
| [SRC-F725E90B2A-L001893](../../tests/test_web_agent.py#L1893) | 1893 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L001894](../../tests/test_web_agent.py#L1894) | 1894 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L001895](../../tests/test_web_agent.py#L1895) | 1895 | `"        return \"<<<OMARAI_FINAL_ANSWER>>>تمت مراجعة المسودة.<<<END_OMARAI_FINAL_ANSWER>>>\""` | — |
| [SRC-F725E90B2A-L001896](../../tests/test_web_agent.py#L1896) | 1896 | `""` | — |
| [SRC-F725E90B2A-L001897](../../tests/test_web_agent.py#L1897) | 1897 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L001898](../../tests/test_web_agent.py#L1898) | 1898 | `"    result = agent._review_answer("` | — |
| [SRC-F725E90B2A-L001899](../../tests/test_web_agent.py#L1899) | 1899 | `"        question=\"قارن بين خدمتين من حيث السعر، الخصوصية والاعتمادية\","` | — |
| [SRC-F725E90B2A-L001900](../../tests/test_web_agent.py#L1900) | 1900 | `"        answer=\"السعر مناسب [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L001901](../../tests/test_web_agent.py#L1901) | 1901 | `"        sources=[sample_source(0)],"` | — |
| [SRC-F725E90B2A-L001902](../../tests/test_web_agent.py#L1902) | 1902 | `"    )"` | — |
| [SRC-F725E90B2A-L001903](../../tests/test_web_agent.py#L1903) | 1903 | `"    system_content = \"\\n\".join(m[\"content\"] for m in captured[\"messages\"] if m[\"role\"] == \"system\")"` | — |
| [SRC-F725E90B2A-L001904](../../tests/test_web_agent.py#L1904) | 1904 | `"    user_content = \"\\n\".join(m[\"content\"] for m in captured[\"messages\"] if m[\"role\"] == \"user\")"` | — |
| [SRC-F725E90B2A-L001905](../../tests/test_web_agent.py#L1905) | 1905 | `"    assert result == \"تمت مراجعة المسودة.\""` | — |
| [SRC-F725E90B2A-L001906](../../tests/test_web_agent.py#L1906) | 1906 | `"    assert \"اكتمال الإجابة مقابل\" in system_content"` | — |
| [SRC-F725E90B2A-L001907](../../tests/test_web_agent.py#L1907) | 1907 | `"    assert \"الاعتمادية\" in user_content"` | — |
| [SRC-F725E90B2A-L001908](../../tests/test_web_agent.py#L1908) | 1908 | `"    assert \"قائمة محاور مستخرجة آليًا\" in user_content"` | — |
| [SRC-F725E90B2A-L001909](../../tests/test_web_agent.py#L1909) | 1909 | `""` | — |
| [SRC-F725E90B2A-L001910](../../tests/test_web_agent.py#L1910) | 1910 | `""` | — |
| [SRC-F725E90B2A-L001911](../../tests/test_web_agent.py#L1911) | 1911 | `"def test_search_attempt_is_reported_when_no_sources_survive(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001912](../../tests/test_web_agent.py#L1912) | 1912 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001913](../../tests/test_web_agent.py#L1913) | 1913 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L001914](../../tests/test_web_agent.py#L1914) | 1914 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001915](../../tests/test_web_agent.py#L1915) | 1915 | `"        \"queries\": [\"ما آخر تطورات الطاقة المتجددة اليوم؟\"],"` | — |
| [SRC-F725E90B2A-L001916](../../tests/test_web_agent.py#L1916) | 1916 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L001917](../../tests/test_web_agent.py#L1917) | 1917 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001918](../../tests/test_web_agent.py#L1918) | 1918 | `"        \"freshness\": \"today\","` | — |
| [SRC-F725E90B2A-L001919](../../tests/test_web_agent.py#L1919) | 1919 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L001920](../../tests/test_web_agent.py#L1920) | 1920 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001921](../../tests/test_web_agent.py#L1921) | 1921 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001922](../../tests/test_web_agent.py#L1922) | 1922 | `"    }"` | — |
| [SRC-F725E90B2A-L001923](../../tests/test_web_agent.py#L1923) | 1923 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L001924](../../tests/test_web_agent.py#L1924) | 1924 | `""` | — |
| [SRC-F725E90B2A-L001925](../../tests/test_web_agent.py#L1925) | 1925 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L001926](../../tests/test_web_agent.py#L1926) | 1926 | `"        calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L001927](../../tests/test_web_agent.py#L1927) | 1927 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L001928](../../tests/test_web_agent.py#L1928) | 1928 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L001929](../../tests/test_web_agent.py#L1929) | 1929 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001930](../../tests/test_web_agent.py#L1930) | 1930 | `"            \"query_results\": [{\"query\": research_plan[\"queries\"][0], \"results\": 0}],"` | — |
| [SRC-F725E90B2A-L001931](../../tests/test_web_agent.py#L1931) | 1931 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L001932](../../tests/test_web_agent.py#L1932) | 1932 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L001933](../../tests/test_web_agent.py#L1933) | 1933 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L001934](../../tests/test_web_agent.py#L1934) | 1934 | `"            \"provider_counts\": {},"` | — |
| [SRC-F725E90B2A-L001935](../../tests/test_web_agent.py#L1935) | 1935 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L001936](../../tests/test_web_agent.py#L1936) | 1936 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001937](../../tests/test_web_agent.py#L1937) | 1937 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L001938](../../tests/test_web_agent.py#L1938) | 1938 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001939](../../tests/test_web_agent.py#L1939) | 1939 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L001940](../../tests/test_web_agent.py#L1940) | 1940 | `"        }"` | — |
| [SRC-F725E90B2A-L001941](../../tests/test_web_agent.py#L1941) | 1941 | `""` | — |
| [SRC-F725E90B2A-L001942](../../tests/test_web_agent.py#L1942) | 1942 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001943](../../tests/test_web_agent.py#L1943) | 1943 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L001944](../../tests/test_web_agent.py#L1944) | 1944 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001945](../../tests/test_web_agent.py#L1945) | 1945 | `"        agent,"` | — |
| [SRC-F725E90B2A-L001946](../../tests/test_web_agent.py#L1946) | 1946 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L001947](../../tests/test_web_agent.py#L1947) | 1947 | `"        lambda *args, **kwargs: pytest.fail(\"The model must not answer without usable evidence\"),"` | — |
| [SRC-F725E90B2A-L001948](../../tests/test_web_agent.py#L1948) | 1948 | `"    )"` | — |
| [SRC-F725E90B2A-L001949](../../tests/test_web_agent.py#L1949) | 1949 | `""` | — |
| [SRC-F725E90B2A-L001950](../../tests/test_web_agent.py#L1950) | 1950 | `"    result = agent.answer(\"ما آخر تطورات الطاقة المتجددة اليوم؟\")"` | — |
| [SRC-F725E90B2A-L001951](../../tests/test_web_agent.py#L1951) | 1951 | `""` | — |
| [SRC-F725E90B2A-L001952](../../tests/test_web_agent.py#L1952) | 1952 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L001953](../../tests/test_web_agent.py#L1953) | 1953 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L001954](../../tests/test_web_agent.py#L1954) | 1954 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-F725E90B2A-L001955](../../tests/test_web_agent.py#L1955) | 1955 | `"    assert result[\"sources\"] == []"` | — |
| [SRC-F725E90B2A-L001956](../../tests/test_web_agent.py#L1956) | 1956 | `"    assert result[\"search_report\"][\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L001957](../../tests/test_web_agent.py#L1957) | 1957 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_no_usable_sources\""` | — |
| [SRC-F725E90B2A-L001958](../../tests/test_web_agent.py#L1958) | 1958 | `"    assert result[\"search_report\"][\"usable_sources_after_filtering\"] == 0"` | — |
| [SRC-F725E90B2A-L001959](../../tests/test_web_agent.py#L1959) | 1959 | `"    assert result[\"search_report\"][\"insufficient_evidence\"] is True"` | — |
| [SRC-F725E90B2A-L001960](../../tests/test_web_agent.py#L1960) | 1960 | `"    assert result[\"search_report\"][\"pipeline_completion_status\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L001961](../../tests/test_web_agent.py#L1961) | 1961 | `"    assert result[\"task_understanding\"][\"tool_execution\"][\"accepted_source_count\"] == 0"` | — |
| [SRC-F725E90B2A-L001962](../../tests/test_web_agent.py#L1962) | 1962 | `"    assert calls, \"Expected at least one attempted retrieval round\""` | — |
| [SRC-F725E90B2A-L001963](../../tests/test_web_agent.py#L1963) | 1963 | `""` | — |
| [SRC-F725E90B2A-L001964](../../tests/test_web_agent.py#L1964) | 1964 | `""` | — |
| [SRC-F725E90B2A-L001965](../../tests/test_web_agent.py#L1965) | 1965 | `"def test_success_report_counts_registrable_domains_not_sibling_subdomains(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001966](../../tests/test_web_agent.py#L1966) | 1966 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001967](../../tests/test_web_agent.py#L1967) | 1967 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L001968](../../tests/test_web_agent.py#L1968) | 1968 | `"    first = sample_source(0)"` | — |
| [SRC-F725E90B2A-L001969](../../tests/test_web_agent.py#L1969) | 1969 | `"    first[\"url\"] = \"https://news.example.com/research\""` | — |
| [SRC-F725E90B2A-L001970](../../tests/test_web_agent.py#L1970) | 1970 | `"    first[\"domain\"] = \"news.example.com\""` | — |
| [SRC-F725E90B2A-L001971](../../tests/test_web_agent.py#L1971) | 1971 | `"    second = sample_source(0)"` | — |
| [SRC-F725E90B2A-L001972](../../tests/test_web_agent.py#L1972) | 1972 | `"    second[\"url\"] = \"https://offers.example.com/research\""` | — |
| [SRC-F725E90B2A-L001973](../../tests/test_web_agent.py#L1973) | 1973 | `"    second[\"domain\"] = \"offers.example.com\""` | — |
| [SRC-F725E90B2A-L001974](../../tests/test_web_agent.py#L1974) | 1974 | `"    third = sample_source(1)"` | — |
| [SRC-F725E90B2A-L001975](../../tests/test_web_agent.py#L1975) | 1975 | `"    sources = [first, second, third]"` | — |
| [SRC-F725E90B2A-L001976](../../tests/test_web_agent.py#L1976) | 1976 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001977](../../tests/test_web_agent.py#L1977) | 1977 | `"        \"queries\": [\"قارن هذه التقنية\"],"` | — |
| [SRC-F725E90B2A-L001978](../../tests/test_web_agent.py#L1978) | 1978 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L001979](../../tests/test_web_agent.py#L1979) | 1979 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001980](../../tests/test_web_agent.py#L1980) | 1980 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L001981](../../tests/test_web_agent.py#L1981) | 1981 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L001982](../../tests/test_web_agent.py#L1982) | 1982 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001983](../../tests/test_web_agent.py#L1983) | 1983 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001984](../../tests/test_web_agent.py#L1984) | 1984 | `"    }"` | — |
| [SRC-F725E90B2A-L001985](../../tests/test_web_agent.py#L1985) | 1985 | `""` | — |
| [SRC-F725E90B2A-L001986](../../tests/test_web_agent.py#L1986) | 1986 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001987](../../tests/test_web_agent.py#L1987) | 1987 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001988](../../tests/test_web_agent.py#L1988) | 1988 | `"        agent,"` | — |
| [SRC-F725E90B2A-L001989](../../tests/test_web_agent.py#L1989) | 1989 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L001990](../../tests/test_web_agent.py#L1990) | 1990 | `"        lambda research_plan: ("` | — |
| [SRC-F725E90B2A-L001991](../../tests/test_web_agent.py#L1991) | 1991 | `"            sources,"` | — |
| [SRC-F725E90B2A-L001992](../../tests/test_web_agent.py#L1992) | 1992 | `"            [],"` | — |
| [SRC-F725E90B2A-L001993](../../tests/test_web_agent.py#L1993) | 1993 | `"            {"` | — |
| [SRC-F725E90B2A-L001994](../../tests/test_web_agent.py#L1994) | 1994 | `"                \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L001995](../../tests/test_web_agent.py#L1995) | 1995 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001996](../../tests/test_web_agent.py#L1996) | 1996 | `"                \"query_results\": [{\"query\": \"قارن هذه التقنية\", \"results\": 3}],"` | — |
| [SRC-F725E90B2A-L001997](../../tests/test_web_agent.py#L1997) | 1997 | `"                \"unique_sources\": 3,"` | — |
| [SRC-F725E90B2A-L001998](../../tests/test_web_agent.py#L1998) | 1998 | `"                \"pages_fetched\": 3,"` | — |
| [SRC-F725E90B2A-L001999](../../tests/test_web_agent.py#L1999) | 1999 | `"                \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L002000](../../tests/test_web_agent.py#L2000) | 2000 | `"                \"provider_counts\": {\"test_provider\": 3},"` | — |
| [SRC-F725E90B2A-L002001](../../tests/test_web_agent.py#L2001) | 2001 | `"                \"platform_counts\": {\"web\": 3},"` | — |
| [SRC-F725E90B2A-L002002](../../tests/test_web_agent.py#L2002) | 2002 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002003](../../tests/test_web_agent.py#L2003) | 2003 | `"                \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002004](../../tests/test_web_agent.py#L2004) | 2004 | `"                \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002005](../../tests/test_web_agent.py#L2005) | 2005 | `"                \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L002006](../../tests/test_web_agent.py#L2006) | 2006 | `"            },"` | — |
| [SRC-F725E90B2A-L002007](../../tests/test_web_agent.py#L2007) | 2007 | `"        ),"` | — |
| [SRC-F725E90B2A-L002008](../../tests/test_web_agent.py#L2008) | 2008 | `"    )"` | — |
| [SRC-F725E90B2A-L002009](../../tests/test_web_agent.py#L2009) | 2009 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L002010](../../tests/test_web_agent.py#L2010) | 2010 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"الإجابة [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L002011](../../tests/test_web_agent.py#L2011) | 2011 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L002012](../../tests/test_web_agent.py#L2012) | 2012 | `""` | — |
| [SRC-F725E90B2A-L002013](../../tests/test_web_agent.py#L2013) | 2013 | `"    result = agent.answer(\"قارن هذه التقنية\")"` | — |
| [SRC-F725E90B2A-L002014](../../tests/test_web_agent.py#L2014) | 2014 | `""` | — |
| [SRC-F725E90B2A-L002015](../../tests/test_web_agent.py#L2015) | 2015 | `"    assert result[\"kind\"] in {\"web_research\", \"web_fallback\"}"` | — |
| [SRC-F725E90B2A-L002016](../../tests/test_web_agent.py#L2016) | 2016 | `"    assert result[\"search_report\"][\"unique_sources\"] == 3"` | — |
| [SRC-F725E90B2A-L002017](../../tests/test_web_agent.py#L2017) | 2017 | `"    assert result[\"search_report\"][\"distinct_registrable_domains\"] == 2"` | — |
| [SRC-F725E90B2A-L002018](../../tests/test_web_agent.py#L2018) | 2018 | `"    assert result[\"search_report\"][\"independent_sources\"] == 2"` | — |
| [SRC-F725E90B2A-L002019](../../tests/test_web_agent.py#L2019) | 2019 | `"    assert result[\"search_report\"][\"editorial_independence_status\"] == \"not_assessed\""` | — |
| [SRC-F725E90B2A-L002020](../../tests/test_web_agent.py#L2020) | 2020 | `""` | — |
| [SRC-F725E90B2A-L002021](../../tests/test_web_agent.py#L2021) | 2021 | `""` | — |
| [SRC-F725E90B2A-L002022](../../tests/test_web_agent.py#L2022) | 2022 | `"def test_completion_rejects_content_filtered_primary_and_uses_fallback(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002023](../../tests/test_web_agent.py#L2023) | 2023 | `"    import json"` | — |
| [SRC-F725E90B2A-L002024](../../tests/test_web_agent.py#L2024) | 2024 | `""` | — |
| [SRC-F725E90B2A-L002025](../../tests/test_web_agent.py#L2025) | 2025 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002026](../../tests/test_web_agent.py#L2026) | 2026 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002027](../../tests/test_web_agent.py#L2027) | 2027 | `"    agent.fallback_model = \"fallback/model\""` | — |
| [SRC-F725E90B2A-L002028](../../tests/test_web_agent.py#L2028) | 2028 | `"    called = []"` | — |
| [SRC-F725E90B2A-L002029](../../tests/test_web_agent.py#L2029) | 2029 | `""` | — |
| [SRC-F725E90B2A-L002030](../../tests/test_web_agent.py#L2030) | 2030 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L002031](../../tests/test_web_agent.py#L2031) | 2031 | `"        def __init__(self, content, finish_reason):"` | — |
| [SRC-F725E90B2A-L002032](../../tests/test_web_agent.py#L2032) | 2032 | `"            self.body = json.dumps({"` | — |
| [SRC-F725E90B2A-L002033](../../tests/test_web_agent.py#L2033) | 2033 | `"                \"choices\": [{"` | — |
| [SRC-F725E90B2A-L002034](../../tests/test_web_agent.py#L2034) | 2034 | `"                    \"message\": {\"content\": content},"` | — |
| [SRC-F725E90B2A-L002035](../../tests/test_web_agent.py#L2035) | 2035 | `"                    \"finish_reason\": finish_reason,"` | — |
| [SRC-F725E90B2A-L002036](../../tests/test_web_agent.py#L2036) | 2036 | `"                }]"` | — |
| [SRC-F725E90B2A-L002037](../../tests/test_web_agent.py#L2037) | 2037 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002038](../../tests/test_web_agent.py#L2038) | 2038 | `""` | — |
| [SRC-F725E90B2A-L002039](../../tests/test_web_agent.py#L2039) | 2039 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L002040](../../tests/test_web_agent.py#L2040) | 2040 | `"            return self"` | — |
| [SRC-F725E90B2A-L002041](../../tests/test_web_agent.py#L2041) | 2041 | `""` | — |
| [SRC-F725E90B2A-L002042](../../tests/test_web_agent.py#L2042) | 2042 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L002043](../../tests/test_web_agent.py#L2043) | 2043 | `"            return False"` | — |
| [SRC-F725E90B2A-L002044](../../tests/test_web_agent.py#L2044) | 2044 | `""` | — |
| [SRC-F725E90B2A-L002045](../../tests/test_web_agent.py#L2045) | 2045 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L002046](../../tests/test_web_agent.py#L2046) | 2046 | `"            return self.body"` | — |
| [SRC-F725E90B2A-L002047](../../tests/test_web_agent.py#L2047) | 2047 | `""` | — |
| [SRC-F725E90B2A-L002048](../../tests/test_web_agent.py#L2048) | 2048 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L002049](../../tests/test_web_agent.py#L2049) | 2049 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-F725E90B2A-L002050](../../tests/test_web_agent.py#L2050) | 2050 | `"        called.append(model)"` | — |
| [SRC-F725E90B2A-L002051](../../tests/test_web_agent.py#L2051) | 2051 | `"        if model == \"filtered/primary\":"` | — |
| [SRC-F725E90B2A-L002052](../../tests/test_web_agent.py#L2052) | 2052 | `"            return FakeResponse(\"جزء جواب مفلتر لا ينبغي اعتباره مكتملا\", \"content_filter\")"` | — |
| [SRC-F725E90B2A-L002053](../../tests/test_web_agent.py#L2053) | 2053 | `"        return FakeResponse(\"إجابة الاحتياط المكتملة\", \"stop\")"` | — |
| [SRC-F725E90B2A-L002054](../../tests/test_web_agent.py#L2054) | 2054 | `""` | — |
| [SRC-F725E90B2A-L002055](../../tests/test_web_agent.py#L2055) | 2055 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L002056](../../tests/test_web_agent.py#L2056) | 2056 | `"    result = agent._request_completion("` | — |
| [SRC-F725E90B2A-L002057](../../tests/test_web_agent.py#L2057) | 2057 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-F725E90B2A-L002058](../../tests/test_web_agent.py#L2058) | 2058 | `"        model=\"filtered/primary\","` | — |
| [SRC-F725E90B2A-L002059](../../tests/test_web_agent.py#L2059) | 2059 | `"    )"` | — |
| [SRC-F725E90B2A-L002060](../../tests/test_web_agent.py#L2060) | 2060 | `""` | — |
| [SRC-F725E90B2A-L002061](../../tests/test_web_agent.py#L2061) | 2061 | `"    assert result == \"إجابة الاحتياط المكتملة\""` | — |
| [SRC-F725E90B2A-L002062](../../tests/test_web_agent.py#L2062) | 2062 | `"    assert called == [\"filtered/primary\", \"fallback/model\"]"` | — |
| [SRC-F725E90B2A-L002063](../../tests/test_web_agent.py#L2063) | 2063 | `"    assert \"جزء جواب مفلتر\" not in result"` | — |
| [SRC-F725E90B2A-L002064](../../tests/test_web_agent.py#L2064) | 2064 | `""` | — |
| [SRC-F725E90B2A-L002065](../../tests/test_web_agent.py#L2065) | 2065 | `""` | — |
| [SRC-F725E90B2A-L002066](../../tests/test_web_agent.py#L2066) | 2066 | `"def test_reviewer_rejects_duplicate_final_answer_delimiters(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002067](../../tests/test_web_agent.py#L2067) | 2067 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002068](../../tests/test_web_agent.py#L2068) | 2068 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002069](../../tests/test_web_agent.py#L2069) | 2069 | `"    source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002070](../../tests/test_web_agent.py#L2070) | 2070 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002071](../../tests/test_web_agent.py#L2071) | 2071 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002072](../../tests/test_web_agent.py#L2072) | 2072 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L002073](../../tests/test_web_agent.py#L2073) | 2073 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-F725E90B2A-L002074](../../tests/test_web_agent.py#L2074) | 2074 | `"            \"<<<OMARAI_FINAL_ANSWER>>>تقرير مراجعة داخلي \""` | — |
| [SRC-F725E90B2A-L002075](../../tests/test_web_agent.py#L2075) | 2075 | `"            \"<<<OMARAI_FINAL_ANSWER>>>نص مزعوم\""` | — |
| [SRC-F725E90B2A-L002076](../../tests/test_web_agent.py#L2076) | 2076 | `"            \"<<<END_OMARAI_FINAL_ANSWER>>><<<END_OMARAI_FINAL_ANSWER>>>\""` | — |
| [SRC-F725E90B2A-L002077](../../tests/test_web_agent.py#L2077) | 2077 | `"        ),"` | — |
| [SRC-F725E90B2A-L002078](../../tests/test_web_agent.py#L2078) | 2078 | `"    )"` | — |
| [SRC-F725E90B2A-L002079](../../tests/test_web_agent.py#L2079) | 2079 | `""` | — |
| [SRC-F725E90B2A-L002080](../../tests/test_web_agent.py#L2080) | 2080 | `"    with pytest.raises(RuntimeError, match=\"فصل الإجابة النهائية\"):"` | — |
| [SRC-F725E90B2A-L002081](../../tests/test_web_agent.py#L2081) | 2081 | `"        agent._review_answer(\"ما مضمون الصفحة؟\", \"مسودة\", [source])"` | — |
| [SRC-F725E90B2A-L002082](../../tests/test_web_agent.py#L2082) | 2082 | `""` | — |
| [SRC-F725E90B2A-L002083](../../tests/test_web_agent.py#L2083) | 2083 | `""` | — |
| [SRC-F725E90B2A-L002084](../../tests/test_web_agent.py#L2084) | 2084 | `"def test_frontend_review_status_matches_api_contract():"` | — |
| [SRC-F725E90B2A-L002085](../../tests/test_web_agent.py#L2085) | 2085 | `"    html = (Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002086](../../tests/test_web_agent.py#L2086) | 2086 | `"    assert 'r.second_pass_review===\"model_claim_audit_completed\"' in html"` | — |
| [SRC-F725E90B2A-L002087](../../tests/test_web_agent.py#L2087) | 2087 | `"    assert 'r.second_pass_review===\"model_claim_audit_unavailable\"' in html"` | — |
| [SRC-F725E90B2A-L002088](../../tests/test_web_agent.py#L2088) | 2088 | `"    assert 'r.second_pass_review===\"model_second_pass_completed\"' not in html"` | — |
| [SRC-F725E90B2A-L002089](../../tests/test_web_agent.py#L2089) | 2089 | `"    assert 'r.second_pass_review===\"model_second_pass_unavailable\"' not in html"` | — |
| [SRC-F725E90B2A-L002090](../../tests/test_web_agent.py#L2090) | 2090 | `""` | — |
| [SRC-F725E90B2A-L002091](../../tests/test_web_agent.py#L2091) | 2091 | `""` | — |
| [SRC-F725E90B2A-L002092](../../tests/test_web_agent.py#L2092) | 2092 | `""` | — |
| [SRC-F725E90B2A-L002093](../../tests/test_web_agent.py#L2093) | 2093 | `"def test_research_error_preserves_confirmed_search_attempt_without_fabricating_counts(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002094](../../tests/test_web_agent.py#L2094) | 2094 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002095](../../tests/test_web_agent.py#L2095) | 2095 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002096](../../tests/test_web_agent.py#L2096) | 2096 | `"        \"queries\": [\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\"],"` | — |
| [SRC-F725E90B2A-L002097](../../tests/test_web_agent.py#L2097) | 2097 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002098](../../tests/test_web_agent.py#L2098) | 2098 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002099](../../tests/test_web_agent.py#L2099) | 2099 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L002100](../../tests/test_web_agent.py#L2100) | 2100 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002101](../../tests/test_web_agent.py#L2101) | 2101 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002102](../../tests/test_web_agent.py#L2102) | 2102 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002103](../../tests/test_web_agent.py#L2103) | 2103 | `"    }"` | — |
| [SRC-F725E90B2A-L002104](../../tests/test_web_agent.py#L2104) | 2104 | `""` | — |
| [SRC-F725E90B2A-L002105](../../tests/test_web_agent.py#L2105) | 2105 | `"    def failed_after_provider_result(research_plan):"` | — |
| [SRC-F725E90B2A-L002106](../../tests/test_web_agent.py#L2106) | 2106 | `"        # A completed provider result-processing state confirms that a search"` | — |
| [SRC-F725E90B2A-L002107](../../tests/test_web_agent.py#L2107) | 2107 | `"        # connector returned; the collector then fails during downstream processing."` | — |
| [SRC-F725E90B2A-L002108](../../tests/test_web_agent.py#L2108) | 2108 | `"        agent._record_provider_diagnostic("` | — |
| [SRC-F725E90B2A-L002109](../../tests/test_web_agent.py#L2109) | 2109 | `"            \"duckduckgo_html\","` | — |
| [SRC-F725E90B2A-L002110](../../tests/test_web_agent.py#L2110) | 2110 | `"            research_plan[\"queries\"][0],"` | — |
| [SRC-F725E90B2A-L002111](../../tests/test_web_agent.py#L2111) | 2111 | `"            \"ok\","` | — |
| [SRC-F725E90B2A-L002112](../../tests/test_web_agent.py#L2112) | 2112 | `"            result_count=1,"` | — |
| [SRC-F725E90B2A-L002113](../../tests/test_web_agent.py#L2113) | 2113 | `"        )"` | — |
| [SRC-F725E90B2A-L002114](../../tests/test_web_agent.py#L2114) | 2114 | `"        raise RuntimeError(\"simulated post-search pipeline failure\")"` | — |
| [SRC-F725E90B2A-L002115](../../tests/test_web_agent.py#L2115) | 2115 | `""` | — |
| [SRC-F725E90B2A-L002116](../../tests/test_web_agent.py#L2116) | 2116 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002117](../../tests/test_web_agent.py#L2117) | 2117 | `"    monkeypatch.setattr(agent, \"_collect_research\", failed_after_provider_result)"` | — |
| [SRC-F725E90B2A-L002118](../../tests/test_web_agent.py#L2118) | 2118 | `""` | — |
| [SRC-F725E90B2A-L002119](../../tests/test_web_agent.py#L2119) | 2119 | `"    result = agent.answer(\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\")"` | — |
| [SRC-F725E90B2A-L002120](../../tests/test_web_agent.py#L2120) | 2120 | `""` | — |
| [SRC-F725E90B2A-L002121](../../tests/test_web_agent.py#L2121) | 2121 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L002122](../../tests/test_web_agent.py#L2122) | 2122 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L002123](../../tests/test_web_agent.py#L2123) | 2123 | `"    assert report[\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L002124](../../tests/test_web_agent.py#L2124) | 2124 | `"    assert report[\"search_outcome\"] == \"attempted_research_error\""` | — |
| [SRC-F725E90B2A-L002125](../../tests/test_web_agent.py#L2125) | 2125 | `"    assert report[\"queries_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002126](../../tests/test_web_agent.py#L2126) | 2126 | `"    assert report[\"queries_attempted_known\"] is False"` | — |
| [SRC-F725E90B2A-L002127](../../tests/test_web_agent.py#L2127) | 2127 | `"    assert report[\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002128](../../tests/test_web_agent.py#L2128) | 2128 | `"    assert report[\"unique_sources\"] is None"` | — |
| [SRC-F725E90B2A-L002129](../../tests/test_web_agent.py#L2129) | 2129 | `"    assert report[\"pages_fetched\"] is None"` | — |
| [SRC-F725E90B2A-L002130](../../tests/test_web_agent.py#L2130) | 2130 | `""` | — |
| [SRC-F725E90B2A-L002131](../../tests/test_web_agent.py#L2131) | 2131 | `""` | — |
| [SRC-F725E90B2A-L002132](../../tests/test_web_agent.py#L2132) | 2132 | `"def test_research_error_without_provider_diagnostics_is_reported_as_unknown(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002133](../../tests/test_web_agent.py#L2133) | 2133 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002134](../../tests/test_web_agent.py#L2134) | 2134 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002135](../../tests/test_web_agent.py#L2135) | 2135 | `"        \"queries\": [\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\"],"` | — |
| [SRC-F725E90B2A-L002136](../../tests/test_web_agent.py#L2136) | 2136 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002137](../../tests/test_web_agent.py#L2137) | 2137 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002138](../../tests/test_web_agent.py#L2138) | 2138 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L002139](../../tests/test_web_agent.py#L2139) | 2139 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002140](../../tests/test_web_agent.py#L2140) | 2140 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002141](../../tests/test_web_agent.py#L2141) | 2141 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002142](../../tests/test_web_agent.py#L2142) | 2142 | `"    }"` | — |
| [SRC-F725E90B2A-L002143](../../tests/test_web_agent.py#L2143) | 2143 | `""` | — |
| [SRC-F725E90B2A-L002144](../../tests/test_web_agent.py#L2144) | 2144 | `"    def fail_before_attempt(research_plan):"` | — |
| [SRC-F725E90B2A-L002145](../../tests/test_web_agent.py#L2145) | 2145 | `"        raise RuntimeError(\"simulated scheduler failure\")"` | — |
| [SRC-F725E90B2A-L002146](../../tests/test_web_agent.py#L2146) | 2146 | `""` | — |
| [SRC-F725E90B2A-L002147](../../tests/test_web_agent.py#L2147) | 2147 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002148](../../tests/test_web_agent.py#L2148) | 2148 | `"    monkeypatch.setattr(agent, \"_collect_research\", fail_before_attempt)"` | — |
| [SRC-F725E90B2A-L002149](../../tests/test_web_agent.py#L2149) | 2149 | `""` | — |
| [SRC-F725E90B2A-L002150](../../tests/test_web_agent.py#L2150) | 2150 | `"    result = agent.answer(\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\")"` | — |
| [SRC-F725E90B2A-L002151](../../tests/test_web_agent.py#L2151) | 2151 | `""` | — |
| [SRC-F725E90B2A-L002152](../../tests/test_web_agent.py#L2152) | 2152 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L002153](../../tests/test_web_agent.py#L2153) | 2153 | `"    assert result[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002154](../../tests/test_web_agent.py#L2154) | 2154 | `"    assert report[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002155](../../tests/test_web_agent.py#L2155) | 2155 | `"    assert report[\"search_outcome\"] == \"unknown_after_research_error\""` | — |
| [SRC-F725E90B2A-L002156](../../tests/test_web_agent.py#L2156) | 2156 | `"    assert report[\"queries_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002157](../../tests/test_web_agent.py#L2157) | 2157 | `"    assert report[\"queries_attempted_known\"] is False"` | — |
| [SRC-F725E90B2A-L002158](../../tests/test_web_agent.py#L2158) | 2158 | `"    assert report[\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002159](../../tests/test_web_agent.py#L2159) | 2159 | `""` | — |
| [SRC-F725E90B2A-L002160](../../tests/test_web_agent.py#L2160) | 2160 | `""` | — |
| [SRC-F725E90B2A-L002161](../../tests/test_web_agent.py#L2161) | 2161 | `"def test_general_answer_does_not_silently_slice_overlong_model_output(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002162](../../tests/test_web_agent.py#L2162) | 2162 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002163](../../tests/test_web_agent.py#L2163) | 2163 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002164](../../tests/test_web_agent.py#L2164) | 2164 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002165](../../tests/test_web_agent.py#L2165) | 2165 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002166](../../tests/test_web_agent.py#L2166) | 2166 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L002167](../../tests/test_web_agent.py#L2167) | 2167 | `"        lambda *args, **kwargs: \"ن\" * 24_001,"` | — |
| [SRC-F725E90B2A-L002168](../../tests/test_web_agent.py#L2168) | 2168 | `"    )"` | — |
| [SRC-F725E90B2A-L002169](../../tests/test_web_agent.py#L2169) | 2169 | `""` | — |
| [SRC-F725E90B2A-L002170](../../tests/test_web_agent.py#L2170) | 2170 | `"    result = agent._answer_without_search(\"اشرح مفهومًا عامًا\", [])"` | — |
| [SRC-F725E90B2A-L002171](../../tests/test_web_agent.py#L2171) | 2171 | `""` | — |
| [SRC-F725E90B2A-L002172](../../tests/test_web_agent.py#L2172) | 2172 | `"    assert result is None"` | — |
| [SRC-F725E90B2A-L002173](../../tests/test_web_agent.py#L2173) | 2173 | `""` | — |
| [SRC-F725E90B2A-L002174](../../tests/test_web_agent.py#L2174) | 2174 | `""` | — |
| [SRC-F725E90B2A-L002175](../../tests/test_web_agent.py#L2175) | 2175 | `"def test_frontend_discloses_unknown_counts_after_research_error():"` | — |
| [SRC-F725E90B2A-L002176](../../tests/test_web_agent.py#L2176) | 2176 | `"    html = (Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002177](../../tests/test_web_agent.py#L2177) | 2177 | `"    assert '[\"attempted_research_error\",\"unknown_after_research_error\"].includes(r.search_outcome)' in html"` | — |
| [SRC-F725E90B2A-L002178](../../tests/test_web_agent.py#L2178) | 2178 | `"    assert \"لم يمكن تحديد عدد المصادر القابلة للاستخدام\" in html"` | — |
| [SRC-F725E90B2A-L002179](../../tests/test_web_agent.py#L2179) | 2179 | `"    assert \"غير محدد\" in html"` | — |
| [SRC-F725E90B2A-L002180](../../tests/test_web_agent.py#L2180) | 2180 | `"    assert 'const score=(researchErrorOutcome\|\|lead)?null:Number(e.coverage_score\|\|0)' not in html"` | — |
| [SRC-F725E90B2A-L002181](../../tests/test_web_agent.py#L2181) | 2181 | `"    assert \"مؤشر تغطية البحث:\" not in html"` | — |
| [SRC-F725E90B2A-L002182](../../tests/test_web_agent.py#L2182) | 2182 | `"    assert '\"تغطية الأدلة: \"+scoreLabel' in html"` | — |
| [SRC-F725E90B2A-L002183](../../tests/test_web_agent.py#L2183) | 2183 | `"    assert \"يصف هذا الوصف اتساع الأدلة المتاحة ولا يمثل احتمال صحة الإجابة\" in html"` | — |
| [SRC-F725E90B2A-L002184](../../tests/test_web_agent.py#L2184) | 2184 | `"    assert \"تعذر تحديد تغطية البحث لأن مسار تجميع الأدلة لم يكتمل\" in html"` | — |
| [SRC-F725E90B2A-L002185](../../tests/test_web_agent.py#L2185) | 2185 | `""` | — |
| [SRC-F725E90B2A-L002186](../../tests/test_web_agent.py#L2186) | 2186 | `""` | — |
| [SRC-F725E90B2A-L002187](../../tests/test_web_agent.py#L2187) | 2187 | `"def test_generic_provider_failure_does_not_claim_search_attempt_as_confirmed(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002188](../../tests/test_web_agent.py#L2188) | 2188 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002189](../../tests/test_web_agent.py#L2189) | 2189 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002190](../../tests/test_web_agent.py#L2190) | 2190 | `"        \"queries\": [\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\"],"` | — |
| [SRC-F725E90B2A-L002191](../../tests/test_web_agent.py#L2191) | 2191 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002192](../../tests/test_web_agent.py#L2192) | 2192 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002193](../../tests/test_web_agent.py#L2193) | 2193 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L002194](../../tests/test_web_agent.py#L2194) | 2194 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002195](../../tests/test_web_agent.py#L2195) | 2195 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002196](../../tests/test_web_agent.py#L2196) | 2196 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002197](../../tests/test_web_agent.py#L2197) | 2197 | `"    }"` | — |
| [SRC-F725E90B2A-L002198](../../tests/test_web_agent.py#L2198) | 2198 | `""` | — |
| [SRC-F725E90B2A-L002199](../../tests/test_web_agent.py#L2199) | 2199 | `"    def fail_after_generic_provider_error(research_plan):"` | — |
| [SRC-F725E90B2A-L002200](../../tests/test_web_agent.py#L2200) | 2200 | `"        # A generic failed diagnostic does not prove whether the network request"` | — |
| [SRC-F725E90B2A-L002201](../../tests/test_web_agent.py#L2201) | 2201 | `"        # was actually sent; it must not be upgraded to a confirmed attempt."` | — |
| [SRC-F725E90B2A-L002202](../../tests/test_web_agent.py#L2202) | 2202 | `"        agent._record_provider_diagnostic("` | — |
| [SRC-F725E90B2A-L002203](../../tests/test_web_agent.py#L2203) | 2203 | `"            \"duckduckgo_html\","` | — |
| [SRC-F725E90B2A-L002204](../../tests/test_web_agent.py#L2204) | 2204 | `"            research_plan[\"queries\"][0],"` | — |
| [SRC-F725E90B2A-L002205](../../tests/test_web_agent.py#L2205) | 2205 | `"            \"failed\","` | — |
| [SRC-F725E90B2A-L002206](../../tests/test_web_agent.py#L2206) | 2206 | `"            error=\"simulated failure before request send\","` | — |
| [SRC-F725E90B2A-L002207](../../tests/test_web_agent.py#L2207) | 2207 | `"        )"` | — |
| [SRC-F725E90B2A-L002208](../../tests/test_web_agent.py#L2208) | 2208 | `"        raise RuntimeError(\"simulated research pipeline failure\")"` | — |
| [SRC-F725E90B2A-L002209](../../tests/test_web_agent.py#L2209) | 2209 | `""` | — |
| [SRC-F725E90B2A-L002210](../../tests/test_web_agent.py#L2210) | 2210 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002211](../../tests/test_web_agent.py#L2211) | 2211 | `"    monkeypatch.setattr(agent, \"_collect_research\", fail_after_generic_provider_error)"` | — |
| [SRC-F725E90B2A-L002212](../../tests/test_web_agent.py#L2212) | 2212 | `""` | — |
| [SRC-F725E90B2A-L002213](../../tests/test_web_agent.py#L2213) | 2213 | `"    result = agent.answer(\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\")"` | — |
| [SRC-F725E90B2A-L002214](../../tests/test_web_agent.py#L2214) | 2214 | `""` | — |
| [SRC-F725E90B2A-L002215](../../tests/test_web_agent.py#L2215) | 2215 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L002216](../../tests/test_web_agent.py#L2216) | 2216 | `"    assert result[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002217](../../tests/test_web_agent.py#L2217) | 2217 | `"    assert report[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002218](../../tests/test_web_agent.py#L2218) | 2218 | `"    assert report[\"search_outcome\"] == \"unknown_after_research_error\""` | — |
| [SRC-F725E90B2A-L002219](../../tests/test_web_agent.py#L2219) | 2219 | `"    assert report[\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002220](../../tests/test_web_agent.py#L2220) | 2220 | `"    assert report[\"unique_sources\"] is None"` | — |
| [SRC-F725E90B2A-L002221](../../tests/test_web_agent.py#L2221) | 2221 | `""` | — |
| [SRC-F725E90B2A-L002222](../../tests/test_web_agent.py#L2222) | 2222 | `""` | — |
| [SRC-F725E90B2A-L002223](../../tests/test_web_agent.py#L2223) | 2223 | `""` | — |
| [SRC-F725E90B2A-L002224](../../tests/test_web_agent.py#L2224) | 2224 | `"def test_diagnostics_tries_fallback_probe_when_first_probe_has_no_results(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002225](../../tests/test_web_agent.py#L2225) | 2225 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002226](../../tests/test_web_agent.py#L2226) | 2226 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L002227](../../tests/test_web_agent.py#L2227) | 2227 | `""` | — |
| [SRC-F725E90B2A-L002228](../../tests/test_web_agent.py#L2228) | 2228 | `"    def search(query):"` | — |
| [SRC-F725E90B2A-L002229](../../tests/test_web_agent.py#L2229) | 2229 | `"        calls.append(query)"` | — |
| [SRC-F725E90B2A-L002230](../../tests/test_web_agent.py#L2230) | 2230 | `"        if len(calls) == 1:"` | — |
| [SRC-F725E90B2A-L002231](../../tests/test_web_agent.py#L2231) | 2231 | `"            return []"` | — |
| [SRC-F725E90B2A-L002232](../../tests/test_web_agent.py#L2232) | 2232 | `"        return ["` | — |
| [SRC-F725E90B2A-L002233](../../tests/test_web_agent.py#L2233) | 2233 | `"            {"` | — |
| [SRC-F725E90B2A-L002234](../../tests/test_web_agent.py#L2234) | 2234 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-F725E90B2A-L002235](../../tests/test_web_agent.py#L2235) | 2235 | `"                \"title\": \"OpenAI official website\","` | — |
| [SRC-F725E90B2A-L002236](../../tests/test_web_agent.py#L2236) | 2236 | `"                \"url\": \"https://openai.com/\","` | — |
| [SRC-F725E90B2A-L002237](../../tests/test_web_agent.py#L2237) | 2237 | `"                \"snippet\": \"Official website and products\","` | — |
| [SRC-F725E90B2A-L002238](../../tests/test_web_agent.py#L2238) | 2238 | `"            }"` | — |
| [SRC-F725E90B2A-L002239](../../tests/test_web_agent.py#L2239) | 2239 | `"        ]"` | — |
| [SRC-F725E90B2A-L002240](../../tests/test_web_agent.py#L2240) | 2240 | `""` | — |
| [SRC-F725E90B2A-L002241](../../tests/test_web_agent.py#L2241) | 2241 | `"    monkeypatch.setattr(agent, \"_search_web\", search)"` | — |
| [SRC-F725E90B2A-L002242](../../tests/test_web_agent.py#L2242) | 2242 | `"    monkeypatch.setattr(agent, \"_request_completion\", lambda *args, **kwargs: \"OK\")"` | — |
| [SRC-F725E90B2A-L002243](../../tests/test_web_agent.py#L2243) | 2243 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002244](../../tests/test_web_agent.py#L2244) | 2244 | `""` | — |
| [SRC-F725E90B2A-L002245](../../tests/test_web_agent.py#L2245) | 2245 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L002246](../../tests/test_web_agent.py#L2246) | 2246 | `""` | — |
| [SRC-F725E90B2A-L002247](../../tests/test_web_agent.py#L2247) | 2247 | `"    assert len(calls) == 2"` | — |
