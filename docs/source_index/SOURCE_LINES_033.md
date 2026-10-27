# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **033**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L001552 إلى SRC-F725E90B2A-L002351
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L001552](../../tests/test_web_agent.py#L1552) | 1552 | `"    results = agent._search_web(\"AI use cases for small businesses latest news\")"` | — |
| [SRC-F725E90B2A-L001553](../../tests/test_web_agent.py#L1553) | 1553 | `""` | — |
| [SRC-F725E90B2A-L001554](../../tests/test_web_agent.py#L1554) | 1554 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L001555](../../tests/test_web_agent.py#L1555) | 1555 | `"    assert results[0][\"title\"] == \"أكثر حالات استخدام الذكاء الاصطناعي قيمة للأعمال\""` | — |
| [SRC-F725E90B2A-L001556](../../tests/test_web_agent.py#L1556) | 1556 | `"    diagnostic = next("` | — |
| [SRC-F725E90B2A-L001557](../../tests/test_web_agent.py#L1557) | 1557 | `"        row for row in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L001558](../../tests/test_web_agent.py#L1558) | 1558 | `"        if row[\"provider\"] == \"google_news_rss\""` | — |
| [SRC-F725E90B2A-L001559](../../tests/test_web_agent.py#L1559) | 1559 | `"    )"` | — |
| [SRC-F725E90B2A-L001560](../../tests/test_web_agent.py#L1560) | 1560 | `"    assert diagnostic[\"status\"] == \"ok\""` | — |
| [SRC-F725E90B2A-L001561](../../tests/test_web_agent.py#L1561) | 1561 | `"    assert diagnostic[\"result_count\"] == 2"` | — |
| [SRC-F725E90B2A-L001562](../../tests/test_web_agent.py#L1562) | 1562 | `"    assert diagnostic[\"accepted_count\"] == 1"` | — |
| [SRC-F725E90B2A-L001563](../../tests/test_web_agent.py#L1563) | 1563 | `"    assert diagnostic[\"rejected_count\"] == 1"` | — |
| [SRC-F725E90B2A-L001564](../../tests/test_web_agent.py#L1564) | 1564 | `"    assert diagnostic[\"rejection_counts\"][\"relevance_below_threshold\"] == 1"` | — |
| [SRC-F725E90B2A-L001565](../../tests/test_web_agent.py#L1565) | 1565 | `""` | — |
| [SRC-F725E90B2A-L001566](../../tests/test_web_agent.py#L1566) | 1566 | `""` | — |
| [SRC-F725E90B2A-L001567](../../tests/test_web_agent.py#L1567) | 1567 | `"def test_google_news_preserves_publisher_identity(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001568](../../tests/test_web_agent.py#L1568) | 1568 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L001569](../../tests/test_web_agent.py#L1569) | 1569 | `""` | — |
| [SRC-F725E90B2A-L001570](../../tests/test_web_agent.py#L1570) | 1570 | `"    rss = \"\"\"<rss><channel><item>"` | — |
| [SRC-F725E90B2A-L001571](../../tests/test_web_agent.py#L1571) | 1571 | `"      <title>مصر الرقمية: تحديث جديد للخدمات</title>"` | — |
| [SRC-F725E90B2A-L001572](../../tests/test_web_agent.py#L1572) | 1572 | `"      <link>https://news.google.com/rss/articles/EXAMPLE123</link>"` | — |
| [SRC-F725E90B2A-L001573](../../tests/test_web_agent.py#L1573) | 1573 | `"      <description>معلومات عن بوابة مصر الرقمية والخدمات الإلكترونية.</description>"` | — |
| [SRC-F725E90B2A-L001574](../../tests/test_web_agent.py#L1574) | 1574 | `"      <source url=\"https://digital.gov.eg/\">بوابة مصر الرقمية</source>"` | — |
| [SRC-F725E90B2A-L001575](../../tests/test_web_agent.py#L1575) | 1575 | `"      <pubDate>Sat, 17 Oct 2026 10:00:00 GMT</pubDate>"` | — |
| [SRC-F725E90B2A-L001576](../../tests/test_web_agent.py#L1576) | 1576 | `"    </item></channel></rss>\"\"\""` | — |
| [SRC-F725E90B2A-L001577](../../tests/test_web_agent.py#L1577) | 1577 | `""` | — |
| [SRC-F725E90B2A-L001578](../../tests/test_web_agent.py#L1578) | 1578 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L001579](../../tests/test_web_agent.py#L1579) | 1579 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L001580](../../tests/test_web_agent.py#L1580) | 1580 | `"        content = rss.encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L001581](../../tests/test_web_agent.py#L1581) | 1581 | `""` | — |
| [SRC-F725E90B2A-L001582](../../tests/test_web_agent.py#L1582) | 1582 | `"    monkeypatch.setattr(httpx, \"get\", lambda *args, **kwargs: FakeResponse())"` | — |
| [SRC-F725E90B2A-L001583](../../tests/test_web_agent.py#L1583) | 1583 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001584](../../tests/test_web_agent.py#L1584) | 1584 | `"    results = agent._search_news(\"مصر الرقمية أحدث الأخبار\")"` | — |
| [SRC-F725E90B2A-L001585](../../tests/test_web_agent.py#L1585) | 1585 | `""` | — |
| [SRC-F725E90B2A-L001586](../../tests/test_web_agent.py#L1586) | 1586 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L001587](../../tests/test_web_agent.py#L1587) | 1587 | `"    assert results[0][\"url\"].startswith(\"https://news.google.com/\")"` | — |
| [SRC-F725E90B2A-L001588](../../tests/test_web_agent.py#L1588) | 1588 | `"    assert results[0][\"publisher_name\"] == \"بوابة مصر الرقمية\""` | — |
| [SRC-F725E90B2A-L001589](../../tests/test_web_agent.py#L1589) | 1589 | `"    assert results[0][\"publisher_url\"] == \"https://digital.gov.eg/\""` | — |
| [SRC-F725E90B2A-L001590](../../tests/test_web_agent.py#L1590) | 1590 | `"    assert results[0][\"publisher_domain\"] == \"digital.gov.eg\""` | — |
| [SRC-F725E90B2A-L001591](../../tests/test_web_agent.py#L1591) | 1591 | `""` | — |
| [SRC-F725E90B2A-L001592](../../tests/test_web_agent.py#L1592) | 1592 | `""` | — |
| [SRC-F725E90B2A-L001593](../../tests/test_web_agent.py#L1593) | 1593 | `"def test_relevance_matching_handles_arabic_names_with_english_results():"` | — |
| [SRC-F725E90B2A-L001594](../../tests/test_web_agent.py#L1594) | 1594 | `"    assert _relevance_ratio(\"ابحث عن ميكروسوفت\", \"Microsoft official company website\") >= 0.20"` | — |
| [SRC-F725E90B2A-L001595](../../tests/test_web_agent.py#L1595) | 1595 | `"    assert _relevance_ratio(\"موقع مصر الرقمية\", \"Egypt Digital portal for government services\") >= 0.20"` | — |
| [SRC-F725E90B2A-L001596](../../tests/test_web_agent.py#L1596) | 1596 | `"    assert _relevance_ratio(\"ابحث عن شقة للايجار\", \"Apartment listing available for rent\") >= 0.20"` | — |
| [SRC-F725E90B2A-L001597](../../tests/test_web_agent.py#L1597) | 1597 | `"    assert _relevance_ratio(\"مقارنة بين الشركات الناشئة\", \"Comparison of startup companies\") >= 0.20"` | — |
| [SRC-F725E90B2A-L001598](../../tests/test_web_agent.py#L1598) | 1598 | `""` | — |
| [SRC-F725E90B2A-L001599](../../tests/test_web_agent.py#L1599) | 1599 | `"def test_relevance_matching_handles_english_ai_use_cases_with_arabic_results():"` | — |
| [SRC-F725E90B2A-L001600](../../tests/test_web_agent.py#L1600) | 1600 | `"    assert _relevance_ratio("` | — |
| [SRC-F725E90B2A-L001601](../../tests/test_web_agent.py#L1601) | 1601 | `"        \"AI use cases for small businesses\","` | — |
| [SRC-F725E90B2A-L001602](../../tests/test_web_agent.py#L1602) | 1602 | `"        \"أكثر حالات استخدام الذكاء الاصطناعي قيمة للأعمال\","` | — |
| [SRC-F725E90B2A-L001603](../../tests/test_web_agent.py#L1603) | 1603 | `"    ) >= 0.20"` | — |
| [SRC-F725E90B2A-L001604](../../tests/test_web_agent.py#L1604) | 1604 | `"    assert _relevance_ratio("` | — |
| [SRC-F725E90B2A-L001605](../../tests/test_web_agent.py#L1605) | 1605 | `"        \"استخدامات الذكاء الاصطناعي في الشركات الصغيرة\","` | — |
| [SRC-F725E90B2A-L001606](../../tests/test_web_agent.py#L1606) | 1606 | `"        \"AI use cases for small businesses\","` | — |
| [SRC-F725E90B2A-L001607](../../tests/test_web_agent.py#L1607) | 1607 | `"    ) >= 0.20"` | — |
| [SRC-F725E90B2A-L001608](../../tests/test_web_agent.py#L1608) | 1608 | `""` | — |
| [SRC-F725E90B2A-L001609](../../tests/test_web_agent.py#L1609) | 1609 | `""` | — |
| [SRC-F725E90B2A-L001610](../../tests/test_web_agent.py#L1610) | 1610 | `"def test_routine_lookup_ignores_planner_overclassification(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001611](../../tests/test_web_agent.py#L1611) | 1611 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001612](../../tests/test_web_agent.py#L1612) | 1612 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L001613](../../tests/test_web_agent.py#L1613) | 1613 | `"    observed = {}"` | — |
| [SRC-F725E90B2A-L001614](../../tests/test_web_agent.py#L1614) | 1614 | `"    sources = []"` | — |
| [SRC-F725E90B2A-L001615](../../tests/test_web_agent.py#L1615) | 1615 | `"    for domain in (\"example.com\", \"example.net\"):"` | — |
| [SRC-F725E90B2A-L001616](../../tests/test_web_agent.py#L1616) | 1616 | `"        sources.append({"` | — |
| [SRC-F725E90B2A-L001617](../../tests/test_web_agent.py#L1617) | 1617 | `"            \"title\": \"موقع مصر الرقمية الرسمي والخدمات الحكومية\","` | — |
| [SRC-F725E90B2A-L001618](../../tests/test_web_agent.py#L1618) | 1618 | `"            \"url\": f\"https://{domain}/digital-egypt\","` | — |
| [SRC-F725E90B2A-L001619](../../tests/test_web_agent.py#L1619) | 1619 | `"            \"snippet\": \"معلومات عن موقع مصر الرقمية والخدمات الحكومية.\","` | — |
| [SRC-F725E90B2A-L001620](../../tests/test_web_agent.py#L1620) | 1620 | `"            \"page_text\": \"معلومات عن موقع مصر الرقمية والخدمات الحكومية.\","` | — |
| [SRC-F725E90B2A-L001621](../../tests/test_web_agent.py#L1621) | 1621 | `"            \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L001622](../../tests/test_web_agent.py#L1622) | 1622 | `"            \"providers\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001623](../../tests/test_web_agent.py#L1623) | 1623 | `"            \"queries\": [],"` | — |
| [SRC-F725E90B2A-L001624](../../tests/test_web_agent.py#L1624) | 1624 | `"            \"domain\": domain,"` | — |
| [SRC-F725E90B2A-L001625](../../tests/test_web_agent.py#L1625) | 1625 | `"            \"source_class\": \"general\","` | — |
| [SRC-F725E90B2A-L001626](../../tests/test_web_agent.py#L1626) | 1626 | `"            \"platform\": \"web\","` | — |
| [SRC-F725E90B2A-L001627](../../tests/test_web_agent.py#L1627) | 1627 | `"        })"` | — |
| [SRC-F725E90B2A-L001628](../../tests/test_web_agent.py#L1628) | 1628 | `""` | — |
| [SRC-F725E90B2A-L001629](../../tests/test_web_agent.py#L1629) | 1629 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001630](../../tests/test_web_agent.py#L1630) | 1630 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L001631](../../tests/test_web_agent.py#L1631) | 1631 | `"        lambda question, history: {"` | — |
| [SRC-F725E90B2A-L001632](../../tests/test_web_agent.py#L1632) | 1632 | `"            \"queries\": [f\"query {i}\" for i in range(8)],"` | — |
| [SRC-F725E90B2A-L001633](../../tests/test_web_agent.py#L1633) | 1633 | `"            \"direct_urls\": [], \"social_focus\": False, \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L001634](../../tests/test_web_agent.py#L1634) | 1634 | `"            \"depth\": \"deep\", \"platforms\": [], \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001635](../../tests/test_web_agent.py#L1635) | 1635 | `"        },"` | — |
| [SRC-F725E90B2A-L001636](../../tests/test_web_agent.py#L1636) | 1636 | `"    )"` | — |
| [SRC-F725E90B2A-L001637](../../tests/test_web_agent.py#L1637) | 1637 | `""` | — |
| [SRC-F725E90B2A-L001638](../../tests/test_web_agent.py#L1638) | 1638 | `"    def collect(plan):"` | — |
| [SRC-F725E90B2A-L001639](../../tests/test_web_agent.py#L1639) | 1639 | `"        observed[\"plan\"] = plan"` | — |
| [SRC-F725E90B2A-L001640](../../tests/test_web_agent.py#L1640) | 1640 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L001641](../../tests/test_web_agent.py#L1641) | 1641 | `"            \"queries_planned\": len(plan[\"queries\"]), \"queries_attempted\": len(plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L001642](../../tests/test_web_agent.py#L1642) | 1642 | `"            \"unique_sources\": 2, \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L001643](../../tests/test_web_agent.py#L1643) | 1643 | `"            \"providers_used\": [\"test_provider\"], \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-F725E90B2A-L001644](../../tests/test_web_agent.py#L1644) | 1644 | `"            \"social_direct_results\": 0, \"depth\": plan[\"depth\"], \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001645](../../tests/test_web_agent.py#L1645) | 1645 | `"        }"` | — |
| [SRC-F725E90B2A-L001646](../../tests/test_web_agent.py#L1646) | 1646 | `""` | — |
| [SRC-F725E90B2A-L001647](../../tests/test_web_agent.py#L1647) | 1647 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L001648](../../tests/test_web_agent.py#L1648) | 1648 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"النتيجة [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L001649](../../tests/test_web_agent.py#L1649) | 1649 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L001650](../../tests/test_web_agent.py#L1650) | 1650 | `""` | — |
| [SRC-F725E90B2A-L001651](../../tests/test_web_agent.py#L1651) | 1651 | `"    result = agent.answer(\"ابحث عن موقع مصر الرقمية\")"` | — |
| [SRC-F725E90B2A-L001652](../../tests/test_web_agent.py#L1652) | 1652 | `""` | — |
| [SRC-F725E90B2A-L001653](../../tests/test_web_agent.py#L1653) | 1653 | `"    assert result[\"kind\"] == \"web_research\""` | — |
| [SRC-F725E90B2A-L001654](../../tests/test_web_agent.py#L1654) | 1654 | `"    assert observed[\"plan\"][\"depth\"] == \"standard\""` | — |
| [SRC-F725E90B2A-L001655](../../tests/test_web_agent.py#L1655) | 1655 | `"    assert len(observed[\"plan\"][\"queries\"]) <= 3"` | — |
| [SRC-F725E90B2A-L001656](../../tests/test_web_agent.py#L1656) | 1656 | `"    assert observed[\"plan\"][\"queries\"][0] == \"موقع مصر الرقمية\""` | — |
| [SRC-F725E90B2A-L001657](../../tests/test_web_agent.py#L1657) | 1657 | `""` | — |
| [SRC-F725E90B2A-L001658](../../tests/test_web_agent.py#L1658) | 1658 | `""` | — |
| [SRC-F725E90B2A-L001659](../../tests/test_web_agent.py#L1659) | 1659 | `"def test_listing_discovery_detects_arabic_property_requests():"` | — |
| [SRC-F725E90B2A-L001660](../../tests/test_web_agent.py#L1660) | 1660 | `"    assert WebAgent._is_listing_discovery(\"ابحث عن شقة في التجمع الخامس، ممكن معاينة\")"` | — |
| [SRC-F725E90B2A-L001661](../../tests/test_web_agent.py#L1661) | 1661 | `"    assert WebAgent._is_listing_discovery(\"عايز شقق للايجار في القاهرة\")"` | — |
| [SRC-F725E90B2A-L001662](../../tests/test_web_agent.py#L1662) | 1662 | `"    assert not WebAgent._is_listing_discovery(\"اشرح الفرق بين الشقة والفيلا\")"` | — |
| [SRC-F725E90B2A-L001663](../../tests/test_web_agent.py#L1663) | 1663 | `""` | — |
| [SRC-F725E90B2A-L001664](../../tests/test_web_agent.py#L1664) | 1664 | `""` | — |
| [SRC-F725E90B2A-L001665](../../tests/test_web_agent.py#L1665) | 1665 | `"def test_single_property_listing_is_returned_with_safety_caveat(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001666](../../tests/test_web_agent.py#L1666) | 1666 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001667](../../tests/test_web_agent.py#L1667) | 1667 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L001668](../../tests/test_web_agent.py#L1668) | 1668 | `"    source = {"` | — |
| [SRC-F725E90B2A-L001669](../../tests/test_web_agent.py#L1669) | 1669 | `"        \"title\": \"شقة للبيع في التجمع الخامس\","` | — |
| [SRC-F725E90B2A-L001670](../../tests/test_web_agent.py#L1670) | 1670 | `"        \"url\": \"https://example.com/listing/123\","` | — |
| [SRC-F725E90B2A-L001671](../../tests/test_web_agent.py#L1671) | 1671 | `"        \"snippet\": \"شقة في التجمع الخامس، معاينة بالتنسيق مع المعلن.\","` | — |
| [SRC-F725E90B2A-L001672](../../tests/test_web_agent.py#L1672) | 1672 | `"        \"page_text\": \"شقة في التجمع الخامس، معاينة بالتنسيق مع المعلن.\","` | — |
| [SRC-F725E90B2A-L001673](../../tests/test_web_agent.py#L1673) | 1673 | `"        \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L001674](../../tests/test_web_agent.py#L1674) | 1674 | `"        \"providers\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001675](../../tests/test_web_agent.py#L1675) | 1675 | `"        \"queries\": [\"شقة في التجمع الخامس\"],"` | — |
| [SRC-F725E90B2A-L001676](../../tests/test_web_agent.py#L1676) | 1676 | `"        \"domain\": \"example.com\","` | — |
| [SRC-F725E90B2A-L001677](../../tests/test_web_agent.py#L1677) | 1677 | `"        \"source_class\": \"general\","` | — |
| [SRC-F725E90B2A-L001678](../../tests/test_web_agent.py#L1678) | 1678 | `"        \"platform\": \"web\","` | — |
| [SRC-F725E90B2A-L001679](../../tests/test_web_agent.py#L1679) | 1679 | `"    }"` | — |
| [SRC-F725E90B2A-L001680](../../tests/test_web_agent.py#L1680) | 1680 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001681](../../tests/test_web_agent.py#L1681) | 1681 | `"        agent, \"_plan_search\","` | — |
| [SRC-F725E90B2A-L001682](../../tests/test_web_agent.py#L1682) | 1682 | `"        lambda question, history: {"` | — |
| [SRC-F725E90B2A-L001683](../../tests/test_web_agent.py#L1683) | 1683 | `"            \"queries\": [question], \"direct_urls\": [], \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001684](../../tests/test_web_agent.py#L1684) | 1684 | `"            \"freshness\": \"any\", \"depth\": \"standard\", \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001685](../../tests/test_web_agent.py#L1685) | 1685 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001686](../../tests/test_web_agent.py#L1686) | 1686 | `"        },"` | — |
| [SRC-F725E90B2A-L001687](../../tests/test_web_agent.py#L1687) | 1687 | `"    )"` | — |
| [SRC-F725E90B2A-L001688](../../tests/test_web_agent.py#L1688) | 1688 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001689](../../tests/test_web_agent.py#L1689) | 1689 | `"        agent, \"_collect_research\","` | — |
| [SRC-F725E90B2A-L001690](../../tests/test_web_agent.py#L1690) | 1690 | `"        lambda plan: ([source], [], {"` | — |
| [SRC-F725E90B2A-L001691](../../tests/test_web_agent.py#L1691) | 1691 | `"            \"queries_planned\": 1, \"queries_attempted\": 1, \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L001692](../../tests/test_web_agent.py#L1692) | 1692 | `"            \"pages_fetched\": 1, \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001693](../../tests/test_web_agent.py#L1693) | 1693 | `"            \"platform_counts\": {\"web\": 1}, \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001694](../../tests/test_web_agent.py#L1694) | 1694 | `"            \"depth\": \"standard\", \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001695](../../tests/test_web_agent.py#L1695) | 1695 | `"        }),"` | — |
| [SRC-F725E90B2A-L001696](../../tests/test_web_agent.py#L1696) | 1696 | `"    )"` | — |
| [SRC-F725E90B2A-L001697](../../tests/test_web_agent.py#L1697) | 1697 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001698](../../tests/test_web_agent.py#L1698) | 1698 | `"        agent, \"_generate\","` | — |
| [SRC-F725E90B2A-L001699](../../tests/test_web_agent.py#L1699) | 1699 | `"        lambda *args, **kwargs: \"وجدت إعلانًا مرشحًا لشقة؛ تحقق من التفاصيل [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L001700](../../tests/test_web_agent.py#L1700) | 1700 | `"    )"` | — |
| [SRC-F725E90B2A-L001701](../../tests/test_web_agent.py#L1701) | 1701 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L001702](../../tests/test_web_agent.py#L1702) | 1702 | `""` | — |
| [SRC-F725E90B2A-L001703](../../tests/test_web_agent.py#L1703) | 1703 | `"    result = agent.answer(\"ابحث عن شقة في التجمع الخامس، ممكن معاينة\")"` | — |
| [SRC-F725E90B2A-L001704](../../tests/test_web_agent.py#L1704) | 1704 | `""` | — |
| [SRC-F725E90B2A-L001705](../../tests/test_web_agent.py#L1705) | 1705 | `"    assert result[\"kind\"] == \"web_research\""` | — |
| [SRC-F725E90B2A-L001706](../../tests/test_web_agent.py#L1706) | 1706 | `"    assert len(result[\"sources\"]) == 1"` | — |
| [SRC-F725E90B2A-L001707](../../tests/test_web_agent.py#L1707) | 1707 | `"    assert \"إعلانات/قوائم مرشحة فقط\" in \" \".join(result[\"warnings\"])"` | — |
| [SRC-F725E90B2A-L001708](../../tests/test_web_agent.py#L1708) | 1708 | `""` | — |
| [SRC-F725E90B2A-L001709](../../tests/test_web_agent.py#L1709) | 1709 | `""` | — |
| [SRC-F725E90B2A-L001710](../../tests/test_web_agent.py#L1710) | 1710 | `""` | — |
| [SRC-F725E90B2A-L001711](../../tests/test_web_agent.py#L1711) | 1711 | `"def test_normalized_source_url_key_ignores_tracking_parameters_and_fragment():"` | — |
| [SRC-F725E90B2A-L001712](../../tests/test_web_agent.py#L1712) | 1712 | `"    normalize = WebAgent._normalized_source_url_key"` | — |
| [SRC-F725E90B2A-L001713](../../tests/test_web_agent.py#L1713) | 1713 | `"    assert normalize(\"HTTPS://EXAMPLE.COM:443/article/?utm_source=newsletter#section\") == ("` | — |
| [SRC-F725E90B2A-L001714](../../tests/test_web_agent.py#L1714) | 1714 | `"        \"https://example.com/article\""` | — |
| [SRC-F725E90B2A-L001715](../../tests/test_web_agent.py#L1715) | 1715 | `"    )"` | — |
| [SRC-F725E90B2A-L001716](../../tests/test_web_agent.py#L1716) | 1716 | `"    assert normalize(\"https://example.com/article?fbclid=abc&x=1\") == ("` | — |
| [SRC-F725E90B2A-L001717](../../tests/test_web_agent.py#L1717) | 1717 | `"        \"https://example.com/article?x=1\""` | — |
| [SRC-F725E90B2A-L001718](../../tests/test_web_agent.py#L1718) | 1718 | `"    )"` | — |
| [SRC-F725E90B2A-L001719](../../tests/test_web_agent.py#L1719) | 1719 | `"    assert normalize(\"file:///etc/passwd\") == \"\""` | — |
| [SRC-F725E90B2A-L001720](../../tests/test_web_agent.py#L1720) | 1720 | `""` | — |
| [SRC-F725E90B2A-L001721](../../tests/test_web_agent.py#L1721) | 1721 | `""` | — |
| [SRC-F725E90B2A-L001722](../../tests/test_web_agent.py#L1722) | 1722 | `"def test_bounded_repair_deduplicates_same_page_even_with_tracking_url(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001723](../../tests/test_web_agent.py#L1723) | 1723 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001724](../../tests/test_web_agent.py#L1724) | 1724 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001725](../../tests/test_web_agent.py#L1725) | 1725 | `"        \"queries\": [\"معلومات عن شركة ألفا اليوم\"],"` | — |
| [SRC-F725E90B2A-L001726](../../tests/test_web_agent.py#L1726) | 1726 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L001727](../../tests/test_web_agent.py#L1727) | 1727 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001728](../../tests/test_web_agent.py#L1728) | 1728 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L001729](../../tests/test_web_agent.py#L1729) | 1729 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001730](../../tests/test_web_agent.py#L1730) | 1730 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001731](../../tests/test_web_agent.py#L1731) | 1731 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001732](../../tests/test_web_agent.py#L1732) | 1732 | `"    }"` | — |
| [SRC-F725E90B2A-L001733](../../tests/test_web_agent.py#L1733) | 1733 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L001734](../../tests/test_web_agent.py#L1734) | 1734 | `""` | — |
| [SRC-F725E90B2A-L001735](../../tests/test_web_agent.py#L1735) | 1735 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L001736](../../tests/test_web_agent.py#L1736) | 1736 | `"        calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L001737](../../tests/test_web_agent.py#L1737) | 1737 | `"        source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L001738](../../tests/test_web_agent.py#L1738) | 1738 | `"        if len(calls) > 1:"` | — |
| [SRC-F725E90B2A-L001739](../../tests/test_web_agent.py#L1739) | 1739 | `"            source[\"url\"] = \"https://EXAMPLE.com/research/?utm_source=test#details\""` | — |
| [SRC-F725E90B2A-L001740](../../tests/test_web_agent.py#L1740) | 1740 | `"            source[\"providers\"] = [\"second_provider\"]"` | — |
| [SRC-F725E90B2A-L001741](../../tests/test_web_agent.py#L1741) | 1741 | `"            source[\"page_fetched\"] = False"` | — |
| [SRC-F725E90B2A-L001742](../../tests/test_web_agent.py#L1742) | 1742 | `"        return [source], [], {"` | — |
| [SRC-F725E90B2A-L001743](../../tests/test_web_agent.py#L1743) | 1743 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L001744](../../tests/test_web_agent.py#L1744) | 1744 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001745](../../tests/test_web_agent.py#L1745) | 1745 | `"            \"query_results\": [{\"query\": research_plan[\"queries\"][0], \"results\": 1}],"` | — |
| [SRC-F725E90B2A-L001746](../../tests/test_web_agent.py#L1746) | 1746 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L001747](../../tests/test_web_agent.py#L1747) | 1747 | `"            \"pages_fetched\": 1 if len(calls) == 1 else 0,"` | — |
| [SRC-F725E90B2A-L001748](../../tests/test_web_agent.py#L1748) | 1748 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001749](../../tests/test_web_agent.py#L1749) | 1749 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L001750](../../tests/test_web_agent.py#L1750) | 1750 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001751](../../tests/test_web_agent.py#L1751) | 1751 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001752](../../tests/test_web_agent.py#L1752) | 1752 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001753](../../tests/test_web_agent.py#L1753) | 1753 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L001754](../../tests/test_web_agent.py#L1754) | 1754 | `"        }"` | — |
| [SRC-F725E90B2A-L001755](../../tests/test_web_agent.py#L1755) | 1755 | `""` | — |
| [SRC-F725E90B2A-L001756](../../tests/test_web_agent.py#L1756) | 1756 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001757](../../tests/test_web_agent.py#L1757) | 1757 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L001758](../../tests/test_web_agent.py#L1758) | 1758 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L001759](../../tests/test_web_agent.py#L1759) | 1759 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001760](../../tests/test_web_agent.py#L1760) | 1760 | `"        agent, \"_generate\","` | — |
| [SRC-F725E90B2A-L001761](../../tests/test_web_agent.py#L1761) | 1761 | `"        lambda *args, **kwargs: pytest.fail(\"Duplicate URL must not satisfy corroboration\"),"` | — |
| [SRC-F725E90B2A-L001762](../../tests/test_web_agent.py#L1762) | 1762 | `"    )"` | — |
| [SRC-F725E90B2A-L001763](../../tests/test_web_agent.py#L1763) | 1763 | `""` | — |
| [SRC-F725E90B2A-L001764](../../tests/test_web_agent.py#L1764) | 1764 | `"    result = agent.answer(\"ما آخر معلومات عن شركة ألفا اليوم؟\")"` | — |
| [SRC-F725E90B2A-L001765](../../tests/test_web_agent.py#L1765) | 1765 | `""` | — |
| [SRC-F725E90B2A-L001766](../../tests/test_web_agent.py#L1766) | 1766 | `"    assert len(calls) == 2"` | — |
| [SRC-F725E90B2A-L001767](../../tests/test_web_agent.py#L1767) | 1767 | `"    repair = result[\"search_report\"][\"evidence_repair\"]"` | — |
| [SRC-F725E90B2A-L001768](../../tests/test_web_agent.py#L1768) | 1768 | `"    assert repair[\"attempted\"] is True"` | — |
| [SRC-F725E90B2A-L001769](../../tests/test_web_agent.py#L1769) | 1769 | `"    assert repair[\"new_sources_added\"] == 0"` | — |
| [SRC-F725E90B2A-L001770](../../tests/test_web_agent.py#L1770) | 1770 | `"    assert repair[\"recovered\"] is False"` | — |
| [SRC-F725E90B2A-L001771](../../tests/test_web_agent.py#L1771) | 1771 | `"    assert result[\"search_report\"][\"independent_sources\"] == 1"` | — |
| [SRC-F725E90B2A-L001772](../../tests/test_web_agent.py#L1772) | 1772 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L001773](../../tests/test_web_agent.py#L1773) | 1773 | `""` | — |
| [SRC-F725E90B2A-L001774](../../tests/test_web_agent.py#L1774) | 1774 | `""` | — |
| [SRC-F725E90B2A-L001775](../../tests/test_web_agent.py#L1775) | 1775 | `"def test_social_focused_partial_evidence_does_not_trigger_general_repair(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001776](../../tests/test_web_agent.py#L1776) | 1776 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001777](../../tests/test_web_agent.py#L1777) | 1777 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001778](../../tests/test_web_agent.py#L1778) | 1778 | `"        \"queries\": [\"تجارب المستخدمين حول التقنية\"],"` | — |
| [SRC-F725E90B2A-L001779](../../tests/test_web_agent.py#L1779) | 1779 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L001780](../../tests/test_web_agent.py#L1780) | 1780 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001781](../../tests/test_web_agent.py#L1781) | 1781 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L001782](../../tests/test_web_agent.py#L1782) | 1782 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001783](../../tests/test_web_agent.py#L1783) | 1783 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001784](../../tests/test_web_agent.py#L1784) | 1784 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001785](../../tests/test_web_agent.py#L1785) | 1785 | `"    }"` | — |
| [SRC-F725E90B2A-L001786](../../tests/test_web_agent.py#L1786) | 1786 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L001787](../../tests/test_web_agent.py#L1787) | 1787 | `""` | — |
| [SRC-F725E90B2A-L001788](../../tests/test_web_agent.py#L1788) | 1788 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L001789](../../tests/test_web_agent.py#L1789) | 1789 | `"        calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L001790](../../tests/test_web_agent.py#L1790) | 1790 | `"        return [sample_source(0)], [], {"` | — |
| [SRC-F725E90B2A-L001791](../../tests/test_web_agent.py#L1791) | 1791 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L001792](../../tests/test_web_agent.py#L1792) | 1792 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001793](../../tests/test_web_agent.py#L1793) | 1793 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L001794](../../tests/test_web_agent.py#L1794) | 1794 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L001795](../../tests/test_web_agent.py#L1795) | 1795 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L001796](../../tests/test_web_agent.py#L1796) | 1796 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001797](../../tests/test_web_agent.py#L1797) | 1797 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L001798](../../tests/test_web_agent.py#L1798) | 1798 | `"            \"social_direct_results\": 1,"` | — |
| [SRC-F725E90B2A-L001799](../../tests/test_web_agent.py#L1799) | 1799 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001800](../../tests/test_web_agent.py#L1800) | 1800 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001801](../../tests/test_web_agent.py#L1801) | 1801 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L001802](../../tests/test_web_agent.py#L1802) | 1802 | `"        }"` | — |
| [SRC-F725E90B2A-L001803](../../tests/test_web_agent.py#L1803) | 1803 | `""` | — |
| [SRC-F725E90B2A-L001804](../../tests/test_web_agent.py#L1804) | 1804 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001805](../../tests/test_web_agent.py#L1805) | 1805 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L001806](../../tests/test_web_agent.py#L1806) | 1806 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L001807](../../tests/test_web_agent.py#L1807) | 1807 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"إشارات أولية فقط [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L001808](../../tests/test_web_agent.py#L1808) | 1808 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L001809](../../tests/test_web_agent.py#L1809) | 1809 | `""` | — |
| [SRC-F725E90B2A-L001810](../../tests/test_web_agent.py#L1810) | 1810 | `"    result = agent.answer(\"اجمع آراء الناس حول هذه التقنية\", mode=\"social\")"` | — |
| [SRC-F725E90B2A-L001811](../../tests/test_web_agent.py#L1811) | 1811 | `""` | — |
| [SRC-F725E90B2A-L001812](../../tests/test_web_agent.py#L1812) | 1812 | `"    assert len(calls) == 1"` | — |
| [SRC-F725E90B2A-L001813](../../tests/test_web_agent.py#L1813) | 1813 | `"    assert calls[0][\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L001814](../../tests/test_web_agent.py#L1814) | 1814 | `"    assert result[\"search_report\"][\"evidence_repair\"][\"attempted\"] is False"` | — |
| [SRC-F725E90B2A-L001815](../../tests/test_web_agent.py#L1815) | 1815 | `"    assert result[\"search_report\"][\"evidence_repair\"][\"reason\"] == \"task_specific_partial_evidence\""` | — |
| [SRC-F725E90B2A-L001816](../../tests/test_web_agent.py#L1816) | 1816 | `"    assert result[\"research_quality\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L001817](../../tests/test_web_agent.py#L1817) | 1817 | `""` | — |
| [SRC-F725E90B2A-L001818](../../tests/test_web_agent.py#L1818) | 1818 | `""` | — |
| [SRC-F725E90B2A-L001819](../../tests/test_web_agent.py#L1819) | 1819 | `""` | — |
| [SRC-F725E90B2A-L001820](../../tests/test_web_agent.py#L1820) | 1820 | `"def test_question_coverage_targets_extract_arabic_and_english_explicit_criteria():"` | — |
| [SRC-F725E90B2A-L001821](../../tests/test_web_agent.py#L1821) | 1821 | `"    arabic = WebAgent._question_coverage_targets("` | — |
| [SRC-F725E90B2A-L001822](../../tests/test_web_agent.py#L1822) | 1822 | `"        \"قارن بين خدمتين من حيث السعر، الخصوصية، الاعتمادية، وخيار التواصل مع الدعم، \""` | — |
| [SRC-F725E90B2A-L001823](../../tests/test_web_agent.py#L1823) | 1823 | `"        \"واذكر ما لا تستطيع التحقق منه.\""` | — |
| [SRC-F725E90B2A-L001824](../../tests/test_web_agent.py#L1824) | 1824 | `"    )"` | — |
| [SRC-F725E90B2A-L001825](../../tests/test_web_agent.py#L1825) | 1825 | `"    assert arabic == [\"السعر\", \"الخصوصية\", \"الاعتمادية\", \"خيار التواصل مع الدعم\"]"` | — |
| [SRC-F725E90B2A-L001826](../../tests/test_web_agent.py#L1826) | 1826 | `""` | — |
| [SRC-F725E90B2A-L001827](../../tests/test_web_agent.py#L1827) | 1827 | `"    english = WebAgent._question_coverage_targets("` | — |
| [SRC-F725E90B2A-L001828](../../tests/test_web_agent.py#L1828) | 1828 | `"        \"Compare two services in terms of price, privacy, reliability and customer support?\""` | — |
| [SRC-F725E90B2A-L001829](../../tests/test_web_agent.py#L1829) | 1829 | `"    )"` | — |
| [SRC-F725E90B2A-L001830](../../tests/test_web_agent.py#L1830) | 1830 | `"    assert english == [\"price\", \"privacy\", \"reliability\", \"customer support\"]"` | — |
| [SRC-F725E90B2A-L001831](../../tests/test_web_agent.py#L1831) | 1831 | `""` | — |
| [SRC-F725E90B2A-L001832](../../tests/test_web_agent.py#L1832) | 1832 | `"    english_with_period = WebAgent._question_coverage_targets("` | — |
| [SRC-F725E90B2A-L001833](../../tests/test_web_agent.py#L1833) | 1833 | `"        \"Compare two services in terms of price, privacy and reliability.\""` | — |
| [SRC-F725E90B2A-L001834](../../tests/test_web_agent.py#L1834) | 1834 | `"    )"` | — |
| [SRC-F725E90B2A-L001835](../../tests/test_web_agent.py#L1835) | 1835 | `"    assert english_with_period == [\"price\", \"privacy\", \"reliability\"]"` | — |
| [SRC-F725E90B2A-L001836](../../tests/test_web_agent.py#L1836) | 1836 | `""` | — |
| [SRC-F725E90B2A-L001837](../../tests/test_web_agent.py#L1837) | 1837 | `""` | — |
| [SRC-F725E90B2A-L001838](../../tests/test_web_agent.py#L1838) | 1838 | `"def test_question_coverage_targets_do_not_invent_parts_for_simple_question():"` | — |
| [SRC-F725E90B2A-L001839](../../tests/test_web_agent.py#L1839) | 1839 | `"    assert WebAgent._question_coverage_targets(\"ما الذي يقوله المصدر؟\") == []"` | — |
| [SRC-F725E90B2A-L001840](../../tests/test_web_agent.py#L1840) | 1840 | `""` | — |
| [SRC-F725E90B2A-L001841](../../tests/test_web_agent.py#L1841) | 1841 | `""` | — |
| [SRC-F725E90B2A-L001842](../../tests/test_web_agent.py#L1842) | 1842 | `"def test_generator_includes_extracted_targets_as_a_non_authoritative_checklist(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001843](../../tests/test_web_agent.py#L1843) | 1843 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001844](../../tests/test_web_agent.py#L1844) | 1844 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L001845](../../tests/test_web_agent.py#L1845) | 1845 | `""` | — |
| [SRC-F725E90B2A-L001846](../../tests/test_web_agent.py#L1846) | 1846 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L001847](../../tests/test_web_agent.py#L1847) | 1847 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L001848](../../tests/test_web_agent.py#L1848) | 1848 | `"        return \"مقارنة مختصرة.\""` | — |
| [SRC-F725E90B2A-L001849](../../tests/test_web_agent.py#L1849) | 1849 | `""` | — |
| [SRC-F725E90B2A-L001850](../../tests/test_web_agent.py#L1850) | 1850 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L001851](../../tests/test_web_agent.py#L1851) | 1851 | `"    result = agent._generate("` | — |
| [SRC-F725E90B2A-L001852](../../tests/test_web_agent.py#L1852) | 1852 | `"        question=\"قارن بين خدمتين من حيث السعر، الخصوصية والاعتمادية\","` | — |
| [SRC-F725E90B2A-L001853](../../tests/test_web_agent.py#L1853) | 1853 | `"        history=[],"` | — |
| [SRC-F725E90B2A-L001854](../../tests/test_web_agent.py#L1854) | 1854 | `"        sources=[sample_source(0), sample_source(1)],"` | — |
| [SRC-F725E90B2A-L001855](../../tests/test_web_agent.py#L1855) | 1855 | `"        search_warning=None,"` | — |
| [SRC-F725E90B2A-L001856](../../tests/test_web_agent.py#L1856) | 1856 | `"        research_plan={\"depth\": \"deep\", \"queries\": [\"مقارنة الخدمتين\"]},"` | — |
| [SRC-F725E90B2A-L001857](../../tests/test_web_agent.py#L1857) | 1857 | `"        search_report={},"` | — |
| [SRC-F725E90B2A-L001858](../../tests/test_web_agent.py#L1858) | 1858 | `"    )"` | — |
| [SRC-F725E90B2A-L001859](../../tests/test_web_agent.py#L1859) | 1859 | `""` | — |
| [SRC-F725E90B2A-L001860](../../tests/test_web_agent.py#L1860) | 1860 | `"    user_content = \"\\n\".join(m[\"content\"] for m in captured[\"messages\"] if m[\"role\"] == \"user\")"` | — |
| [SRC-F725E90B2A-L001861](../../tests/test_web_agent.py#L1861) | 1861 | `"    assert result == \"مقارنة مختصرة.\""` | — |
| [SRC-F725E90B2A-L001862](../../tests/test_web_agent.py#L1862) | 1862 | `"    assert \"قائمة محاور مستخرجة آليًا\" in user_content"` | — |
| [SRC-F725E90B2A-L001863](../../tests/test_web_agent.py#L1863) | 1863 | `"    for target in (\"السعر\", \"الخصوصية\", \"الاعتمادية\"):"` | — |
| [SRC-F725E90B2A-L001864](../../tests/test_web_agent.py#L1864) | 1864 | `"        assert target in user_content"` | — |
| [SRC-F725E90B2A-L001865](../../tests/test_web_agent.py#L1865) | 1865 | `""` | — |
| [SRC-F725E90B2A-L001866](../../tests/test_web_agent.py#L1866) | 1866 | `""` | — |
| [SRC-F725E90B2A-L001867](../../tests/test_web_agent.py#L1867) | 1867 | `"def test_reviewer_checks_coverage_targets_without_claiming_independent_verification(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001868](../../tests/test_web_agent.py#L1868) | 1868 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001869](../../tests/test_web_agent.py#L1869) | 1869 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L001870](../../tests/test_web_agent.py#L1870) | 1870 | `""` | — |
| [SRC-F725E90B2A-L001871](../../tests/test_web_agent.py#L1871) | 1871 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L001872](../../tests/test_web_agent.py#L1872) | 1872 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L001873](../../tests/test_web_agent.py#L1873) | 1873 | `"        return \"<<<OMARAI_FINAL_ANSWER>>>تمت مراجعة المسودة.<<<END_OMARAI_FINAL_ANSWER>>>\""` | — |
| [SRC-F725E90B2A-L001874](../../tests/test_web_agent.py#L1874) | 1874 | `""` | — |
| [SRC-F725E90B2A-L001875](../../tests/test_web_agent.py#L1875) | 1875 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L001876](../../tests/test_web_agent.py#L1876) | 1876 | `"    result = agent._review_answer("` | — |
| [SRC-F725E90B2A-L001877](../../tests/test_web_agent.py#L1877) | 1877 | `"        question=\"قارن بين خدمتين من حيث السعر، الخصوصية والاعتمادية\","` | — |
| [SRC-F725E90B2A-L001878](../../tests/test_web_agent.py#L1878) | 1878 | `"        answer=\"السعر مناسب [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L001879](../../tests/test_web_agent.py#L1879) | 1879 | `"        sources=[sample_source(0)],"` | — |
| [SRC-F725E90B2A-L001880](../../tests/test_web_agent.py#L1880) | 1880 | `"    )"` | — |
| [SRC-F725E90B2A-L001881](../../tests/test_web_agent.py#L1881) | 1881 | `"    system_content = \"\\n\".join(m[\"content\"] for m in captured[\"messages\"] if m[\"role\"] == \"system\")"` | — |
| [SRC-F725E90B2A-L001882](../../tests/test_web_agent.py#L1882) | 1882 | `"    user_content = \"\\n\".join(m[\"content\"] for m in captured[\"messages\"] if m[\"role\"] == \"user\")"` | — |
| [SRC-F725E90B2A-L001883](../../tests/test_web_agent.py#L1883) | 1883 | `"    assert result == \"تمت مراجعة المسودة.\""` | — |
| [SRC-F725E90B2A-L001884](../../tests/test_web_agent.py#L1884) | 1884 | `"    assert \"اكتمال الإجابة مقابل\" in system_content"` | — |
| [SRC-F725E90B2A-L001885](../../tests/test_web_agent.py#L1885) | 1885 | `"    assert \"الاعتمادية\" in user_content"` | — |
| [SRC-F725E90B2A-L001886](../../tests/test_web_agent.py#L1886) | 1886 | `"    assert \"قائمة محاور مستخرجة آليًا\" in user_content"` | — |
| [SRC-F725E90B2A-L001887](../../tests/test_web_agent.py#L1887) | 1887 | `""` | — |
| [SRC-F725E90B2A-L001888](../../tests/test_web_agent.py#L1888) | 1888 | `""` | — |
| [SRC-F725E90B2A-L001889](../../tests/test_web_agent.py#L1889) | 1889 | `"def test_search_attempt_is_reported_when_no_sources_survive(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001890](../../tests/test_web_agent.py#L1890) | 1890 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001891](../../tests/test_web_agent.py#L1891) | 1891 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L001892](../../tests/test_web_agent.py#L1892) | 1892 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001893](../../tests/test_web_agent.py#L1893) | 1893 | `"        \"queries\": [\"ما آخر تطورات الطاقة المتجددة اليوم؟\"],"` | — |
| [SRC-F725E90B2A-L001894](../../tests/test_web_agent.py#L1894) | 1894 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L001895](../../tests/test_web_agent.py#L1895) | 1895 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001896](../../tests/test_web_agent.py#L1896) | 1896 | `"        \"freshness\": \"today\","` | — |
| [SRC-F725E90B2A-L001897](../../tests/test_web_agent.py#L1897) | 1897 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L001898](../../tests/test_web_agent.py#L1898) | 1898 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001899](../../tests/test_web_agent.py#L1899) | 1899 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001900](../../tests/test_web_agent.py#L1900) | 1900 | `"    }"` | — |
| [SRC-F725E90B2A-L001901](../../tests/test_web_agent.py#L1901) | 1901 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L001902](../../tests/test_web_agent.py#L1902) | 1902 | `""` | — |
| [SRC-F725E90B2A-L001903](../../tests/test_web_agent.py#L1903) | 1903 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L001904](../../tests/test_web_agent.py#L1904) | 1904 | `"        calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L001905](../../tests/test_web_agent.py#L1905) | 1905 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L001906](../../tests/test_web_agent.py#L1906) | 1906 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L001907](../../tests/test_web_agent.py#L1907) | 1907 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001908](../../tests/test_web_agent.py#L1908) | 1908 | `"            \"query_results\": [{\"query\": research_plan[\"queries\"][0], \"results\": 0}],"` | — |
| [SRC-F725E90B2A-L001909](../../tests/test_web_agent.py#L1909) | 1909 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L001910](../../tests/test_web_agent.py#L1910) | 1910 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L001911](../../tests/test_web_agent.py#L1911) | 1911 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L001912](../../tests/test_web_agent.py#L1912) | 1912 | `"            \"provider_counts\": {},"` | — |
| [SRC-F725E90B2A-L001913](../../tests/test_web_agent.py#L1913) | 1913 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L001914](../../tests/test_web_agent.py#L1914) | 1914 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001915](../../tests/test_web_agent.py#L1915) | 1915 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L001916](../../tests/test_web_agent.py#L1916) | 1916 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001917](../../tests/test_web_agent.py#L1917) | 1917 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L001918](../../tests/test_web_agent.py#L1918) | 1918 | `"        }"` | — |
| [SRC-F725E90B2A-L001919](../../tests/test_web_agent.py#L1919) | 1919 | `""` | — |
| [SRC-F725E90B2A-L001920](../../tests/test_web_agent.py#L1920) | 1920 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001921](../../tests/test_web_agent.py#L1921) | 1921 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L001922](../../tests/test_web_agent.py#L1922) | 1922 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001923](../../tests/test_web_agent.py#L1923) | 1923 | `"        agent,"` | — |
| [SRC-F725E90B2A-L001924](../../tests/test_web_agent.py#L1924) | 1924 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L001925](../../tests/test_web_agent.py#L1925) | 1925 | `"        lambda *args, **kwargs: pytest.fail(\"The model must not answer without usable evidence\"),"` | — |
| [SRC-F725E90B2A-L001926](../../tests/test_web_agent.py#L1926) | 1926 | `"    )"` | — |
| [SRC-F725E90B2A-L001927](../../tests/test_web_agent.py#L1927) | 1927 | `""` | — |
| [SRC-F725E90B2A-L001928](../../tests/test_web_agent.py#L1928) | 1928 | `"    result = agent.answer(\"ما آخر تطورات الطاقة المتجددة اليوم؟\")"` | — |
| [SRC-F725E90B2A-L001929](../../tests/test_web_agent.py#L1929) | 1929 | `""` | — |
| [SRC-F725E90B2A-L001930](../../tests/test_web_agent.py#L1930) | 1930 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L001931](../../tests/test_web_agent.py#L1931) | 1931 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L001932](../../tests/test_web_agent.py#L1932) | 1932 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-F725E90B2A-L001933](../../tests/test_web_agent.py#L1933) | 1933 | `"    assert result[\"sources\"] == []"` | — |
| [SRC-F725E90B2A-L001934](../../tests/test_web_agent.py#L1934) | 1934 | `"    assert result[\"search_report\"][\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L001935](../../tests/test_web_agent.py#L1935) | 1935 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_no_usable_sources\""` | — |
| [SRC-F725E90B2A-L001936](../../tests/test_web_agent.py#L1936) | 1936 | `"    assert result[\"search_report\"][\"usable_sources_after_filtering\"] == 0"` | — |
| [SRC-F725E90B2A-L001937](../../tests/test_web_agent.py#L1937) | 1937 | `"    assert calls, \"Expected at least one attempted retrieval round\""` | — |
| [SRC-F725E90B2A-L001938](../../tests/test_web_agent.py#L1938) | 1938 | `""` | — |
| [SRC-F725E90B2A-L001939](../../tests/test_web_agent.py#L1939) | 1939 | `""` | — |
| [SRC-F725E90B2A-L001940](../../tests/test_web_agent.py#L1940) | 1940 | `"def test_success_report_counts_registrable_domains_not_sibling_subdomains(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001941](../../tests/test_web_agent.py#L1941) | 1941 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001942](../../tests/test_web_agent.py#L1942) | 1942 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L001943](../../tests/test_web_agent.py#L1943) | 1943 | `"    first = sample_source(0)"` | — |
| [SRC-F725E90B2A-L001944](../../tests/test_web_agent.py#L1944) | 1944 | `"    first[\"url\"] = \"https://news.example.com/research\""` | — |
| [SRC-F725E90B2A-L001945](../../tests/test_web_agent.py#L1945) | 1945 | `"    first[\"domain\"] = \"news.example.com\""` | — |
| [SRC-F725E90B2A-L001946](../../tests/test_web_agent.py#L1946) | 1946 | `"    second = sample_source(0)"` | — |
| [SRC-F725E90B2A-L001947](../../tests/test_web_agent.py#L1947) | 1947 | `"    second[\"url\"] = \"https://offers.example.com/research\""` | — |
| [SRC-F725E90B2A-L001948](../../tests/test_web_agent.py#L1948) | 1948 | `"    second[\"domain\"] = \"offers.example.com\""` | — |
| [SRC-F725E90B2A-L001949](../../tests/test_web_agent.py#L1949) | 1949 | `"    third = sample_source(1)"` | — |
| [SRC-F725E90B2A-L001950](../../tests/test_web_agent.py#L1950) | 1950 | `"    sources = [first, second, third]"` | — |
| [SRC-F725E90B2A-L001951](../../tests/test_web_agent.py#L1951) | 1951 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001952](../../tests/test_web_agent.py#L1952) | 1952 | `"        \"queries\": [\"قارن هذه التقنية\"],"` | — |
| [SRC-F725E90B2A-L001953](../../tests/test_web_agent.py#L1953) | 1953 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L001954](../../tests/test_web_agent.py#L1954) | 1954 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001955](../../tests/test_web_agent.py#L1955) | 1955 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L001956](../../tests/test_web_agent.py#L1956) | 1956 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L001957](../../tests/test_web_agent.py#L1957) | 1957 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001958](../../tests/test_web_agent.py#L1958) | 1958 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001959](../../tests/test_web_agent.py#L1959) | 1959 | `"    }"` | — |
| [SRC-F725E90B2A-L001960](../../tests/test_web_agent.py#L1960) | 1960 | `""` | — |
| [SRC-F725E90B2A-L001961](../../tests/test_web_agent.py#L1961) | 1961 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001962](../../tests/test_web_agent.py#L1962) | 1962 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001963](../../tests/test_web_agent.py#L1963) | 1963 | `"        agent,"` | — |
| [SRC-F725E90B2A-L001964](../../tests/test_web_agent.py#L1964) | 1964 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L001965](../../tests/test_web_agent.py#L1965) | 1965 | `"        lambda research_plan: ("` | — |
| [SRC-F725E90B2A-L001966](../../tests/test_web_agent.py#L1966) | 1966 | `"            sources,"` | — |
| [SRC-F725E90B2A-L001967](../../tests/test_web_agent.py#L1967) | 1967 | `"            [],"` | — |
| [SRC-F725E90B2A-L001968](../../tests/test_web_agent.py#L1968) | 1968 | `"            {"` | — |
| [SRC-F725E90B2A-L001969](../../tests/test_web_agent.py#L1969) | 1969 | `"                \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L001970](../../tests/test_web_agent.py#L1970) | 1970 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001971](../../tests/test_web_agent.py#L1971) | 1971 | `"                \"query_results\": [{\"query\": \"قارن هذه التقنية\", \"results\": 3}],"` | — |
| [SRC-F725E90B2A-L001972](../../tests/test_web_agent.py#L1972) | 1972 | `"                \"unique_sources\": 3,"` | — |
| [SRC-F725E90B2A-L001973](../../tests/test_web_agent.py#L1973) | 1973 | `"                \"pages_fetched\": 3,"` | — |
| [SRC-F725E90B2A-L001974](../../tests/test_web_agent.py#L1974) | 1974 | `"                \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001975](../../tests/test_web_agent.py#L1975) | 1975 | `"                \"provider_counts\": {\"test_provider\": 3},"` | — |
| [SRC-F725E90B2A-L001976](../../tests/test_web_agent.py#L1976) | 1976 | `"                \"platform_counts\": {\"web\": 3},"` | — |
| [SRC-F725E90B2A-L001977](../../tests/test_web_agent.py#L1977) | 1977 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001978](../../tests/test_web_agent.py#L1978) | 1978 | `"                \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L001979](../../tests/test_web_agent.py#L1979) | 1979 | `"                \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001980](../../tests/test_web_agent.py#L1980) | 1980 | `"                \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L001981](../../tests/test_web_agent.py#L1981) | 1981 | `"            },"` | — |
| [SRC-F725E90B2A-L001982](../../tests/test_web_agent.py#L1982) | 1982 | `"        ),"` | — |
| [SRC-F725E90B2A-L001983](../../tests/test_web_agent.py#L1983) | 1983 | `"    )"` | — |
| [SRC-F725E90B2A-L001984](../../tests/test_web_agent.py#L1984) | 1984 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L001985](../../tests/test_web_agent.py#L1985) | 1985 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"الإجابة [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L001986](../../tests/test_web_agent.py#L1986) | 1986 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L001987](../../tests/test_web_agent.py#L1987) | 1987 | `""` | — |
| [SRC-F725E90B2A-L001988](../../tests/test_web_agent.py#L1988) | 1988 | `"    result = agent.answer(\"قارن هذه التقنية\")"` | — |
| [SRC-F725E90B2A-L001989](../../tests/test_web_agent.py#L1989) | 1989 | `""` | — |
| [SRC-F725E90B2A-L001990](../../tests/test_web_agent.py#L1990) | 1990 | `"    assert result[\"kind\"] in {\"web_research\", \"web_fallback\"}"` | — |
| [SRC-F725E90B2A-L001991](../../tests/test_web_agent.py#L1991) | 1991 | `"    assert result[\"search_report\"][\"unique_sources\"] == 3"` | — |
| [SRC-F725E90B2A-L001992](../../tests/test_web_agent.py#L1992) | 1992 | `"    assert result[\"search_report\"][\"distinct_registrable_domains\"] == 2"` | — |
| [SRC-F725E90B2A-L001993](../../tests/test_web_agent.py#L1993) | 1993 | `"    assert result[\"search_report\"][\"independent_sources\"] == 2"` | — |
| [SRC-F725E90B2A-L001994](../../tests/test_web_agent.py#L1994) | 1994 | `"    assert result[\"search_report\"][\"editorial_independence_status\"] == \"not_assessed\""` | — |
| [SRC-F725E90B2A-L001995](../../tests/test_web_agent.py#L1995) | 1995 | `""` | — |
| [SRC-F725E90B2A-L001996](../../tests/test_web_agent.py#L1996) | 1996 | `""` | — |
| [SRC-F725E90B2A-L001997](../../tests/test_web_agent.py#L1997) | 1997 | `"def test_completion_rejects_content_filtered_primary_and_uses_fallback(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001998](../../tests/test_web_agent.py#L1998) | 1998 | `"    import json"` | — |
| [SRC-F725E90B2A-L001999](../../tests/test_web_agent.py#L1999) | 1999 | `""` | — |
| [SRC-F725E90B2A-L002000](../../tests/test_web_agent.py#L2000) | 2000 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002001](../../tests/test_web_agent.py#L2001) | 2001 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002002](../../tests/test_web_agent.py#L2002) | 2002 | `"    agent.fallback_model = \"fallback/model\""` | — |
| [SRC-F725E90B2A-L002003](../../tests/test_web_agent.py#L2003) | 2003 | `"    called = []"` | — |
| [SRC-F725E90B2A-L002004](../../tests/test_web_agent.py#L2004) | 2004 | `""` | — |
| [SRC-F725E90B2A-L002005](../../tests/test_web_agent.py#L2005) | 2005 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L002006](../../tests/test_web_agent.py#L2006) | 2006 | `"        def __init__(self, content, finish_reason):"` | — |
| [SRC-F725E90B2A-L002007](../../tests/test_web_agent.py#L2007) | 2007 | `"            self.body = json.dumps({"` | — |
| [SRC-F725E90B2A-L002008](../../tests/test_web_agent.py#L2008) | 2008 | `"                \"choices\": [{"` | — |
| [SRC-F725E90B2A-L002009](../../tests/test_web_agent.py#L2009) | 2009 | `"                    \"message\": {\"content\": content},"` | — |
| [SRC-F725E90B2A-L002010](../../tests/test_web_agent.py#L2010) | 2010 | `"                    \"finish_reason\": finish_reason,"` | — |
| [SRC-F725E90B2A-L002011](../../tests/test_web_agent.py#L2011) | 2011 | `"                }]"` | — |
| [SRC-F725E90B2A-L002012](../../tests/test_web_agent.py#L2012) | 2012 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002013](../../tests/test_web_agent.py#L2013) | 2013 | `""` | — |
| [SRC-F725E90B2A-L002014](../../tests/test_web_agent.py#L2014) | 2014 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L002015](../../tests/test_web_agent.py#L2015) | 2015 | `"            return self"` | — |
| [SRC-F725E90B2A-L002016](../../tests/test_web_agent.py#L2016) | 2016 | `""` | — |
| [SRC-F725E90B2A-L002017](../../tests/test_web_agent.py#L2017) | 2017 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L002018](../../tests/test_web_agent.py#L2018) | 2018 | `"            return False"` | — |
| [SRC-F725E90B2A-L002019](../../tests/test_web_agent.py#L2019) | 2019 | `""` | — |
| [SRC-F725E90B2A-L002020](../../tests/test_web_agent.py#L2020) | 2020 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L002021](../../tests/test_web_agent.py#L2021) | 2021 | `"            return self.body"` | — |
| [SRC-F725E90B2A-L002022](../../tests/test_web_agent.py#L2022) | 2022 | `""` | — |
| [SRC-F725E90B2A-L002023](../../tests/test_web_agent.py#L2023) | 2023 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L002024](../../tests/test_web_agent.py#L2024) | 2024 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-F725E90B2A-L002025](../../tests/test_web_agent.py#L2025) | 2025 | `"        called.append(model)"` | — |
| [SRC-F725E90B2A-L002026](../../tests/test_web_agent.py#L2026) | 2026 | `"        if model == \"filtered/primary\":"` | — |
| [SRC-F725E90B2A-L002027](../../tests/test_web_agent.py#L2027) | 2027 | `"            return FakeResponse(\"جزء جواب مفلتر لا ينبغي اعتباره مكتملا\", \"content_filter\")"` | — |
| [SRC-F725E90B2A-L002028](../../tests/test_web_agent.py#L2028) | 2028 | `"        return FakeResponse(\"إجابة الاحتياط المكتملة\", \"stop\")"` | — |
| [SRC-F725E90B2A-L002029](../../tests/test_web_agent.py#L2029) | 2029 | `""` | — |
| [SRC-F725E90B2A-L002030](../../tests/test_web_agent.py#L2030) | 2030 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L002031](../../tests/test_web_agent.py#L2031) | 2031 | `"    result = agent._request_completion("` | — |
| [SRC-F725E90B2A-L002032](../../tests/test_web_agent.py#L2032) | 2032 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-F725E90B2A-L002033](../../tests/test_web_agent.py#L2033) | 2033 | `"        model=\"filtered/primary\","` | — |
| [SRC-F725E90B2A-L002034](../../tests/test_web_agent.py#L2034) | 2034 | `"    )"` | — |
| [SRC-F725E90B2A-L002035](../../tests/test_web_agent.py#L2035) | 2035 | `""` | — |
| [SRC-F725E90B2A-L002036](../../tests/test_web_agent.py#L2036) | 2036 | `"    assert result == \"إجابة الاحتياط المكتملة\""` | — |
| [SRC-F725E90B2A-L002037](../../tests/test_web_agent.py#L2037) | 2037 | `"    assert called == [\"filtered/primary\", \"fallback/model\"]"` | — |
| [SRC-F725E90B2A-L002038](../../tests/test_web_agent.py#L2038) | 2038 | `"    assert \"جزء جواب مفلتر\" not in result"` | — |
| [SRC-F725E90B2A-L002039](../../tests/test_web_agent.py#L2039) | 2039 | `""` | — |
| [SRC-F725E90B2A-L002040](../../tests/test_web_agent.py#L2040) | 2040 | `""` | — |
| [SRC-F725E90B2A-L002041](../../tests/test_web_agent.py#L2041) | 2041 | `"def test_reviewer_rejects_duplicate_final_answer_delimiters(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002042](../../tests/test_web_agent.py#L2042) | 2042 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002043](../../tests/test_web_agent.py#L2043) | 2043 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002044](../../tests/test_web_agent.py#L2044) | 2044 | `"    source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002045](../../tests/test_web_agent.py#L2045) | 2045 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002046](../../tests/test_web_agent.py#L2046) | 2046 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002047](../../tests/test_web_agent.py#L2047) | 2047 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L002048](../../tests/test_web_agent.py#L2048) | 2048 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-F725E90B2A-L002049](../../tests/test_web_agent.py#L2049) | 2049 | `"            \"<<<OMARAI_FINAL_ANSWER>>>تقرير مراجعة داخلي \""` | — |
| [SRC-F725E90B2A-L002050](../../tests/test_web_agent.py#L2050) | 2050 | `"            \"<<<OMARAI_FINAL_ANSWER>>>نص مزعوم\""` | — |
| [SRC-F725E90B2A-L002051](../../tests/test_web_agent.py#L2051) | 2051 | `"            \"<<<END_OMARAI_FINAL_ANSWER>>><<<END_OMARAI_FINAL_ANSWER>>>\""` | — |
| [SRC-F725E90B2A-L002052](../../tests/test_web_agent.py#L2052) | 2052 | `"        ),"` | — |
| [SRC-F725E90B2A-L002053](../../tests/test_web_agent.py#L2053) | 2053 | `"    )"` | — |
| [SRC-F725E90B2A-L002054](../../tests/test_web_agent.py#L2054) | 2054 | `""` | — |
| [SRC-F725E90B2A-L002055](../../tests/test_web_agent.py#L2055) | 2055 | `"    with pytest.raises(RuntimeError, match=\"فصل الإجابة النهائية\"):"` | — |
| [SRC-F725E90B2A-L002056](../../tests/test_web_agent.py#L2056) | 2056 | `"        agent._review_answer(\"ما مضمون الصفحة؟\", \"مسودة\", [source])"` | — |
| [SRC-F725E90B2A-L002057](../../tests/test_web_agent.py#L2057) | 2057 | `""` | — |
| [SRC-F725E90B2A-L002058](../../tests/test_web_agent.py#L2058) | 2058 | `""` | — |
| [SRC-F725E90B2A-L002059](../../tests/test_web_agent.py#L2059) | 2059 | `"def test_frontend_review_status_matches_api_contract():"` | — |
| [SRC-F725E90B2A-L002060](../../tests/test_web_agent.py#L2060) | 2060 | `"    html = (Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002061](../../tests/test_web_agent.py#L2061) | 2061 | `"    assert 'r.second_pass_review===\"model_claim_audit_completed\"' in html"` | — |
| [SRC-F725E90B2A-L002062](../../tests/test_web_agent.py#L2062) | 2062 | `"    assert 'r.second_pass_review===\"model_claim_audit_unavailable\"' in html"` | — |
| [SRC-F725E90B2A-L002063](../../tests/test_web_agent.py#L2063) | 2063 | `"    assert 'r.second_pass_review===\"model_second_pass_completed\"' not in html"` | — |
| [SRC-F725E90B2A-L002064](../../tests/test_web_agent.py#L2064) | 2064 | `"    assert 'r.second_pass_review===\"model_second_pass_unavailable\"' not in html"` | — |
| [SRC-F725E90B2A-L002065](../../tests/test_web_agent.py#L2065) | 2065 | `""` | — |
| [SRC-F725E90B2A-L002066](../../tests/test_web_agent.py#L2066) | 2066 | `""` | — |
| [SRC-F725E90B2A-L002067](../../tests/test_web_agent.py#L2067) | 2067 | `""` | — |
| [SRC-F725E90B2A-L002068](../../tests/test_web_agent.py#L2068) | 2068 | `"def test_research_error_preserves_confirmed_search_attempt_without_fabricating_counts(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002069](../../tests/test_web_agent.py#L2069) | 2069 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002070](../../tests/test_web_agent.py#L2070) | 2070 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002071](../../tests/test_web_agent.py#L2071) | 2071 | `"        \"queries\": [\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\"],"` | — |
| [SRC-F725E90B2A-L002072](../../tests/test_web_agent.py#L2072) | 2072 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002073](../../tests/test_web_agent.py#L2073) | 2073 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002074](../../tests/test_web_agent.py#L2074) | 2074 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L002075](../../tests/test_web_agent.py#L2075) | 2075 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002076](../../tests/test_web_agent.py#L2076) | 2076 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002077](../../tests/test_web_agent.py#L2077) | 2077 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002078](../../tests/test_web_agent.py#L2078) | 2078 | `"    }"` | — |
| [SRC-F725E90B2A-L002079](../../tests/test_web_agent.py#L2079) | 2079 | `""` | — |
| [SRC-F725E90B2A-L002080](../../tests/test_web_agent.py#L2080) | 2080 | `"    def failed_after_provider_result(research_plan):"` | — |
| [SRC-F725E90B2A-L002081](../../tests/test_web_agent.py#L2081) | 2081 | `"        # A completed provider result-processing state confirms that a search"` | — |
| [SRC-F725E90B2A-L002082](../../tests/test_web_agent.py#L2082) | 2082 | `"        # connector returned; the collector then fails during downstream processing."` | — |
| [SRC-F725E90B2A-L002083](../../tests/test_web_agent.py#L2083) | 2083 | `"        agent._record_provider_diagnostic("` | — |
| [SRC-F725E90B2A-L002084](../../tests/test_web_agent.py#L2084) | 2084 | `"            \"duckduckgo_html\","` | — |
| [SRC-F725E90B2A-L002085](../../tests/test_web_agent.py#L2085) | 2085 | `"            research_plan[\"queries\"][0],"` | — |
| [SRC-F725E90B2A-L002086](../../tests/test_web_agent.py#L2086) | 2086 | `"            \"ok\","` | — |
| [SRC-F725E90B2A-L002087](../../tests/test_web_agent.py#L2087) | 2087 | `"            result_count=1,"` | — |
| [SRC-F725E90B2A-L002088](../../tests/test_web_agent.py#L2088) | 2088 | `"        )"` | — |
| [SRC-F725E90B2A-L002089](../../tests/test_web_agent.py#L2089) | 2089 | `"        raise RuntimeError(\"simulated post-search pipeline failure\")"` | — |
| [SRC-F725E90B2A-L002090](../../tests/test_web_agent.py#L2090) | 2090 | `""` | — |
| [SRC-F725E90B2A-L002091](../../tests/test_web_agent.py#L2091) | 2091 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002092](../../tests/test_web_agent.py#L2092) | 2092 | `"    monkeypatch.setattr(agent, \"_collect_research\", failed_after_provider_result)"` | — |
| [SRC-F725E90B2A-L002093](../../tests/test_web_agent.py#L2093) | 2093 | `""` | — |
| [SRC-F725E90B2A-L002094](../../tests/test_web_agent.py#L2094) | 2094 | `"    result = agent.answer(\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\")"` | — |
| [SRC-F725E90B2A-L002095](../../tests/test_web_agent.py#L2095) | 2095 | `""` | — |
| [SRC-F725E90B2A-L002096](../../tests/test_web_agent.py#L2096) | 2096 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L002097](../../tests/test_web_agent.py#L2097) | 2097 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L002098](../../tests/test_web_agent.py#L2098) | 2098 | `"    assert report[\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L002099](../../tests/test_web_agent.py#L2099) | 2099 | `"    assert report[\"search_outcome\"] == \"attempted_research_error\""` | — |
| [SRC-F725E90B2A-L002100](../../tests/test_web_agent.py#L2100) | 2100 | `"    assert report[\"queries_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002101](../../tests/test_web_agent.py#L2101) | 2101 | `"    assert report[\"queries_attempted_known\"] is False"` | — |
| [SRC-F725E90B2A-L002102](../../tests/test_web_agent.py#L2102) | 2102 | `"    assert report[\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002103](../../tests/test_web_agent.py#L2103) | 2103 | `"    assert report[\"unique_sources\"] is None"` | — |
| [SRC-F725E90B2A-L002104](../../tests/test_web_agent.py#L2104) | 2104 | `"    assert report[\"pages_fetched\"] is None"` | — |
| [SRC-F725E90B2A-L002105](../../tests/test_web_agent.py#L2105) | 2105 | `""` | — |
| [SRC-F725E90B2A-L002106](../../tests/test_web_agent.py#L2106) | 2106 | `""` | — |
| [SRC-F725E90B2A-L002107](../../tests/test_web_agent.py#L2107) | 2107 | `"def test_research_error_without_provider_diagnostics_is_reported_as_unknown(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002108](../../tests/test_web_agent.py#L2108) | 2108 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002109](../../tests/test_web_agent.py#L2109) | 2109 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002110](../../tests/test_web_agent.py#L2110) | 2110 | `"        \"queries\": [\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\"],"` | — |
| [SRC-F725E90B2A-L002111](../../tests/test_web_agent.py#L2111) | 2111 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002112](../../tests/test_web_agent.py#L2112) | 2112 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002113](../../tests/test_web_agent.py#L2113) | 2113 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L002114](../../tests/test_web_agent.py#L2114) | 2114 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002115](../../tests/test_web_agent.py#L2115) | 2115 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002116](../../tests/test_web_agent.py#L2116) | 2116 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002117](../../tests/test_web_agent.py#L2117) | 2117 | `"    }"` | — |
| [SRC-F725E90B2A-L002118](../../tests/test_web_agent.py#L2118) | 2118 | `""` | — |
| [SRC-F725E90B2A-L002119](../../tests/test_web_agent.py#L2119) | 2119 | `"    def fail_before_attempt(research_plan):"` | — |
| [SRC-F725E90B2A-L002120](../../tests/test_web_agent.py#L2120) | 2120 | `"        raise RuntimeError(\"simulated scheduler failure\")"` | — |
| [SRC-F725E90B2A-L002121](../../tests/test_web_agent.py#L2121) | 2121 | `""` | — |
| [SRC-F725E90B2A-L002122](../../tests/test_web_agent.py#L2122) | 2122 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002123](../../tests/test_web_agent.py#L2123) | 2123 | `"    monkeypatch.setattr(agent, \"_collect_research\", fail_before_attempt)"` | — |
| [SRC-F725E90B2A-L002124](../../tests/test_web_agent.py#L2124) | 2124 | `""` | — |
| [SRC-F725E90B2A-L002125](../../tests/test_web_agent.py#L2125) | 2125 | `"    result = agent.answer(\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\")"` | — |
| [SRC-F725E90B2A-L002126](../../tests/test_web_agent.py#L2126) | 2126 | `""` | — |
| [SRC-F725E90B2A-L002127](../../tests/test_web_agent.py#L2127) | 2127 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L002128](../../tests/test_web_agent.py#L2128) | 2128 | `"    assert result[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002129](../../tests/test_web_agent.py#L2129) | 2129 | `"    assert report[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002130](../../tests/test_web_agent.py#L2130) | 2130 | `"    assert report[\"search_outcome\"] == \"unknown_after_research_error\""` | — |
| [SRC-F725E90B2A-L002131](../../tests/test_web_agent.py#L2131) | 2131 | `"    assert report[\"queries_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002132](../../tests/test_web_agent.py#L2132) | 2132 | `"    assert report[\"queries_attempted_known\"] is False"` | — |
| [SRC-F725E90B2A-L002133](../../tests/test_web_agent.py#L2133) | 2133 | `"    assert report[\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002134](../../tests/test_web_agent.py#L2134) | 2134 | `""` | — |
| [SRC-F725E90B2A-L002135](../../tests/test_web_agent.py#L2135) | 2135 | `""` | — |
| [SRC-F725E90B2A-L002136](../../tests/test_web_agent.py#L2136) | 2136 | `"def test_general_answer_does_not_silently_slice_overlong_model_output(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002137](../../tests/test_web_agent.py#L2137) | 2137 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002138](../../tests/test_web_agent.py#L2138) | 2138 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002139](../../tests/test_web_agent.py#L2139) | 2139 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002140](../../tests/test_web_agent.py#L2140) | 2140 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002141](../../tests/test_web_agent.py#L2141) | 2141 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L002142](../../tests/test_web_agent.py#L2142) | 2142 | `"        lambda *args, **kwargs: \"ن\" * 24_001,"` | — |
| [SRC-F725E90B2A-L002143](../../tests/test_web_agent.py#L2143) | 2143 | `"    )"` | — |
| [SRC-F725E90B2A-L002144](../../tests/test_web_agent.py#L2144) | 2144 | `""` | — |
| [SRC-F725E90B2A-L002145](../../tests/test_web_agent.py#L2145) | 2145 | `"    result = agent._answer_without_search(\"اشرح مفهومًا عامًا\", [])"` | — |
| [SRC-F725E90B2A-L002146](../../tests/test_web_agent.py#L2146) | 2146 | `""` | — |
| [SRC-F725E90B2A-L002147](../../tests/test_web_agent.py#L2147) | 2147 | `"    assert result is None"` | — |
| [SRC-F725E90B2A-L002148](../../tests/test_web_agent.py#L2148) | 2148 | `""` | — |
| [SRC-F725E90B2A-L002149](../../tests/test_web_agent.py#L2149) | 2149 | `""` | — |
| [SRC-F725E90B2A-L002150](../../tests/test_web_agent.py#L2150) | 2150 | `"def test_frontend_discloses_unknown_counts_after_research_error():"` | — |
| [SRC-F725E90B2A-L002151](../../tests/test_web_agent.py#L2151) | 2151 | `"    html = (Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002152](../../tests/test_web_agent.py#L2152) | 2152 | `"    assert '[\"attempted_research_error\",\"unknown_after_research_error\"].includes(r.search_outcome)' in html"` | — |
| [SRC-F725E90B2A-L002153](../../tests/test_web_agent.py#L2153) | 2153 | `"    assert \"لم يمكن تحديد عدد المصادر القابلة للاستخدام\" in html"` | — |
| [SRC-F725E90B2A-L002154](../../tests/test_web_agent.py#L2154) | 2154 | `"    assert \"غير محدد\" in html"` | — |
| [SRC-F725E90B2A-L002155](../../tests/test_web_agent.py#L2155) | 2155 | `"    assert 'const score=(researchErrorOutcome\|\|lead)?null:Number(e.coverage_score\|\|0)' not in html"` | — |
| [SRC-F725E90B2A-L002156](../../tests/test_web_agent.py#L2156) | 2156 | `"    assert \"مؤشر تغطية البحث:\" not in html"` | — |
| [SRC-F725E90B2A-L002157](../../tests/test_web_agent.py#L2157) | 2157 | `"    assert '\"تغطية الأدلة: \"+scoreLabel' in html"` | — |
| [SRC-F725E90B2A-L002158](../../tests/test_web_agent.py#L2158) | 2158 | `"    assert \"يصف هذا الوصف اتساع الأدلة المتاحة ولا يمثل احتمال صحة الإجابة\" in html"` | — |
| [SRC-F725E90B2A-L002159](../../tests/test_web_agent.py#L2159) | 2159 | `"    assert \"تعذر تحديد تغطية البحث لأن مسار تجميع الأدلة لم يكتمل\" in html"` | — |
| [SRC-F725E90B2A-L002160](../../tests/test_web_agent.py#L2160) | 2160 | `""` | — |
| [SRC-F725E90B2A-L002161](../../tests/test_web_agent.py#L2161) | 2161 | `""` | — |
| [SRC-F725E90B2A-L002162](../../tests/test_web_agent.py#L2162) | 2162 | `"def test_generic_provider_failure_does_not_claim_search_attempt_as_confirmed(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002163](../../tests/test_web_agent.py#L2163) | 2163 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002164](../../tests/test_web_agent.py#L2164) | 2164 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002165](../../tests/test_web_agent.py#L2165) | 2165 | `"        \"queries\": [\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\"],"` | — |
| [SRC-F725E90B2A-L002166](../../tests/test_web_agent.py#L2166) | 2166 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002167](../../tests/test_web_agent.py#L2167) | 2167 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002168](../../tests/test_web_agent.py#L2168) | 2168 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L002169](../../tests/test_web_agent.py#L2169) | 2169 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002170](../../tests/test_web_agent.py#L2170) | 2170 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002171](../../tests/test_web_agent.py#L2171) | 2171 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002172](../../tests/test_web_agent.py#L2172) | 2172 | `"    }"` | — |
| [SRC-F725E90B2A-L002173](../../tests/test_web_agent.py#L2173) | 2173 | `""` | — |
| [SRC-F725E90B2A-L002174](../../tests/test_web_agent.py#L2174) | 2174 | `"    def fail_after_generic_provider_error(research_plan):"` | — |
| [SRC-F725E90B2A-L002175](../../tests/test_web_agent.py#L2175) | 2175 | `"        # A generic failed diagnostic does not prove whether the network request"` | — |
| [SRC-F725E90B2A-L002176](../../tests/test_web_agent.py#L2176) | 2176 | `"        # was actually sent; it must not be upgraded to a confirmed attempt."` | — |
| [SRC-F725E90B2A-L002177](../../tests/test_web_agent.py#L2177) | 2177 | `"        agent._record_provider_diagnostic("` | — |
| [SRC-F725E90B2A-L002178](../../tests/test_web_agent.py#L2178) | 2178 | `"            \"duckduckgo_html\","` | — |
| [SRC-F725E90B2A-L002179](../../tests/test_web_agent.py#L2179) | 2179 | `"            research_plan[\"queries\"][0],"` | — |
| [SRC-F725E90B2A-L002180](../../tests/test_web_agent.py#L2180) | 2180 | `"            \"failed\","` | — |
| [SRC-F725E90B2A-L002181](../../tests/test_web_agent.py#L2181) | 2181 | `"            error=\"simulated failure before request send\","` | — |
| [SRC-F725E90B2A-L002182](../../tests/test_web_agent.py#L2182) | 2182 | `"        )"` | — |
| [SRC-F725E90B2A-L002183](../../tests/test_web_agent.py#L2183) | 2183 | `"        raise RuntimeError(\"simulated research pipeline failure\")"` | — |
| [SRC-F725E90B2A-L002184](../../tests/test_web_agent.py#L2184) | 2184 | `""` | — |
| [SRC-F725E90B2A-L002185](../../tests/test_web_agent.py#L2185) | 2185 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002186](../../tests/test_web_agent.py#L2186) | 2186 | `"    monkeypatch.setattr(agent, \"_collect_research\", fail_after_generic_provider_error)"` | — |
| [SRC-F725E90B2A-L002187](../../tests/test_web_agent.py#L2187) | 2187 | `""` | — |
| [SRC-F725E90B2A-L002188](../../tests/test_web_agent.py#L2188) | 2188 | `"    result = agent.answer(\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\")"` | — |
| [SRC-F725E90B2A-L002189](../../tests/test_web_agent.py#L2189) | 2189 | `""` | — |
| [SRC-F725E90B2A-L002190](../../tests/test_web_agent.py#L2190) | 2190 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L002191](../../tests/test_web_agent.py#L2191) | 2191 | `"    assert result[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002192](../../tests/test_web_agent.py#L2192) | 2192 | `"    assert report[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002193](../../tests/test_web_agent.py#L2193) | 2193 | `"    assert report[\"search_outcome\"] == \"unknown_after_research_error\""` | — |
| [SRC-F725E90B2A-L002194](../../tests/test_web_agent.py#L2194) | 2194 | `"    assert report[\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002195](../../tests/test_web_agent.py#L2195) | 2195 | `"    assert report[\"unique_sources\"] is None"` | — |
| [SRC-F725E90B2A-L002196](../../tests/test_web_agent.py#L2196) | 2196 | `""` | — |
| [SRC-F725E90B2A-L002197](../../tests/test_web_agent.py#L2197) | 2197 | `""` | — |
| [SRC-F725E90B2A-L002198](../../tests/test_web_agent.py#L2198) | 2198 | `""` | — |
| [SRC-F725E90B2A-L002199](../../tests/test_web_agent.py#L2199) | 2199 | `"def test_diagnostics_tries_fallback_probe_when_first_probe_has_no_results(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002200](../../tests/test_web_agent.py#L2200) | 2200 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002201](../../tests/test_web_agent.py#L2201) | 2201 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L002202](../../tests/test_web_agent.py#L2202) | 2202 | `""` | — |
| [SRC-F725E90B2A-L002203](../../tests/test_web_agent.py#L2203) | 2203 | `"    def search(query):"` | — |
| [SRC-F725E90B2A-L002204](../../tests/test_web_agent.py#L2204) | 2204 | `"        calls.append(query)"` | — |
| [SRC-F725E90B2A-L002205](../../tests/test_web_agent.py#L2205) | 2205 | `"        if len(calls) == 1:"` | — |
| [SRC-F725E90B2A-L002206](../../tests/test_web_agent.py#L2206) | 2206 | `"            return []"` | — |
| [SRC-F725E90B2A-L002207](../../tests/test_web_agent.py#L2207) | 2207 | `"        return ["` | — |
| [SRC-F725E90B2A-L002208](../../tests/test_web_agent.py#L2208) | 2208 | `"            {"` | — |
| [SRC-F725E90B2A-L002209](../../tests/test_web_agent.py#L2209) | 2209 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-F725E90B2A-L002210](../../tests/test_web_agent.py#L2210) | 2210 | `"                \"title\": \"OpenAI official website\","` | — |
| [SRC-F725E90B2A-L002211](../../tests/test_web_agent.py#L2211) | 2211 | `"                \"url\": \"https://openai.com/\","` | — |
| [SRC-F725E90B2A-L002212](../../tests/test_web_agent.py#L2212) | 2212 | `"                \"snippet\": \"Official website and products\","` | — |
| [SRC-F725E90B2A-L002213](../../tests/test_web_agent.py#L2213) | 2213 | `"            }"` | — |
| [SRC-F725E90B2A-L002214](../../tests/test_web_agent.py#L2214) | 2214 | `"        ]"` | — |
| [SRC-F725E90B2A-L002215](../../tests/test_web_agent.py#L2215) | 2215 | `""` | — |
| [SRC-F725E90B2A-L002216](../../tests/test_web_agent.py#L2216) | 2216 | `"    monkeypatch.setattr(agent, \"_search_web\", search)"` | — |
| [SRC-F725E90B2A-L002217](../../tests/test_web_agent.py#L2217) | 2217 | `"    monkeypatch.setattr(agent, \"_request_completion\", lambda *args, **kwargs: \"OK\")"` | — |
| [SRC-F725E90B2A-L002218](../../tests/test_web_agent.py#L2218) | 2218 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002219](../../tests/test_web_agent.py#L2219) | 2219 | `""` | — |
| [SRC-F725E90B2A-L002220](../../tests/test_web_agent.py#L2220) | 2220 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L002221](../../tests/test_web_agent.py#L2221) | 2221 | `""` | — |
| [SRC-F725E90B2A-L002222](../../tests/test_web_agent.py#L2222) | 2222 | `"    assert len(calls) == 2"` | — |
| [SRC-F725E90B2A-L002223](../../tests/test_web_agent.py#L2223) | 2223 | `"    assert report[\"checks\"][\"web_search\"][\"status\"] == \"passed\""` | — |
| [SRC-F725E90B2A-L002224](../../tests/test_web_agent.py#L2224) | 2224 | `"    assert report[\"checks\"][\"web_search\"][\"probe_count\"] == 2"` | — |
| [SRC-F725E90B2A-L002225](../../tests/test_web_agent.py#L2225) | 2225 | `"    assert report[\"checks\"][\"web_search\"][\"result_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002226](../../tests/test_web_agent.py#L2226) | 2226 | `""` | — |
| [SRC-F725E90B2A-L002227](../../tests/test_web_agent.py#L2227) | 2227 | `""` | — |
| [SRC-F725E90B2A-L002228](../../tests/test_web_agent.py#L2228) | 2228 | `"def test_lead_discovery_is_distinct_from_listing_search():"` | — |
| [SRC-F725E90B2A-L002229](../../tests/test_web_agent.py#L2229) | 2229 | `"    assert WebAgent._is_lead_search(\"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية\")"` | — |
| [SRC-F725E90B2A-L002230](../../tests/test_web_agent.py#L2230) | 2230 | `"    assert WebAgent._is_lead_search(\"Find buyers looking to buy apartments\")"` | — |
| [SRC-F725E90B2A-L002231](../../tests/test_web_agent.py#L2231) | 2231 | `"    assert not WebAgent._is_lead_search(\"ابحث عن شقق للبيع في العاصمة الإدارية\")"` | — |
| [SRC-F725E90B2A-L002232](../../tests/test_web_agent.py#L2232) | 2232 | `"    assert not WebAgent._is_lead_search(\"Find apartments for sale\")"` | — |
| [SRC-F725E90B2A-L002233](../../tests/test_web_agent.py#L2233) | 2233 | `""` | — |
| [SRC-F725E90B2A-L002234](../../tests/test_web_agent.py#L2234) | 2234 | `""` | — |
| [SRC-F725E90B2A-L002235](../../tests/test_web_agent.py#L2235) | 2235 | `"def test_buyer_intent_evidence_requires_explicit_purchase_signal():"` | — |
| [SRC-F725E90B2A-L002236](../../tests/test_web_agent.py#L2236) | 2236 | `"    listing = {"` | — |
| [SRC-F725E90B2A-L002237](../../tests/test_web_agent.py#L2237) | 2237 | `"        \"title\": \"شقق للبيع في العاصمة الإدارية الجديدة\","` | — |
| [SRC-F725E90B2A-L002238](../../tests/test_web_agent.py#L2238) | 2238 | `"        \"snippet\": \"أفضل شقق للبيع بالتقسيط\","` | — |
| [SRC-F725E90B2A-L002239](../../tests/test_web_agent.py#L2239) | 2239 | `"        \"page_text\": \"إعلانات وحدات سكنية للبيع بمساحات مختلفة.\","` | — |
| [SRC-F725E90B2A-L002240](../../tests/test_web_agent.py#L2240) | 2240 | `"    }"` | — |
| [SRC-F725E90B2A-L002241](../../tests/test_web_agent.py#L2241) | 2241 | `"    buyer_post = {"` | — |
| [SRC-F725E90B2A-L002242](../../tests/test_web_agent.py#L2242) | 2242 | `"        \"title\": \"بدور على شقة تمليك في العاصمة الإدارية\","` | — |
| [SRC-F725E90B2A-L002243](../../tests/test_web_agent.py#L2243) | 2243 | `"        \"snippet\": \"مطلوب شقة تمليك في العاصمة الإدارية.\","` | — |
| [SRC-F725E90B2A-L002244](../../tests/test_web_agent.py#L2244) | 2244 | `"        \"page_text\": \"أنا بدور على شقة تمليك في العاصمة الإدارية وعايز أشتري خلال شهر.\","` | — |
| [SRC-F725E90B2A-L002245](../../tests/test_web_agent.py#L2245) | 2245 | `"    }"` | — |
| [SRC-F725E90B2A-L002246](../../tests/test_web_agent.py#L2246) | 2246 | `"    assert WebAgent._lead_intent_evidence(listing) is None"` | — |
| [SRC-F725E90B2A-L002247](../../tests/test_web_agent.py#L2247) | 2247 | `"    signal = WebAgent._lead_intent_evidence(buyer_post)"` | — |
| [SRC-F725E90B2A-L002248](../../tests/test_web_agent.py#L2248) | 2248 | `"    assert signal is not None"` | — |
| [SRC-F725E90B2A-L002249](../../tests/test_web_agent.py#L2249) | 2249 | `"    assert signal[\"basis\"] == \"page_text\""` | — |
| [SRC-F725E90B2A-L002250](../../tests/test_web_agent.py#L2250) | 2250 | `""` | — |
| [SRC-F725E90B2A-L002251](../../tests/test_web_agent.py#L2251) | 2251 | `""` | — |
| [SRC-F725E90B2A-L002252](../../tests/test_web_agent.py#L2252) | 2252 | `"def test_lead_generation_does_not_present_sale_listings_as_buyers(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002253](../../tests/test_web_agent.py#L2253) | 2253 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002254](../../tests/test_web_agent.py#L2254) | 2254 | `"    question = \"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\""` | — |
| [SRC-F725E90B2A-L002255](../../tests/test_web_agent.py#L2255) | 2255 | `"    source_a = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002256](../../tests/test_web_agent.py#L2256) | 2256 | `"    source_a.update({"` | — |
| [SRC-F725E90B2A-L002257](../../tests/test_web_agent.py#L2257) | 2257 | `"        \"title\": \"شقق للبيع في العاصمة الإدارية الجديدة\","` | — |
| [SRC-F725E90B2A-L002258](../../tests/test_web_agent.py#L2258) | 2258 | `"        \"snippet\": \"قارن أسعار الشقق والمساحات وخطط السداد.\","` | — |
| [SRC-F725E90B2A-L002259](../../tests/test_web_agent.py#L2259) | 2259 | `"        \"page_text\": \"إعلانات شقق للبيع من شركات تطوير عقاري.\","` | — |
| [SRC-F725E90B2A-L002260](../../tests/test_web_agent.py#L2260) | 2260 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002261](../../tests/test_web_agent.py#L2261) | 2261 | `"    })"` | — |
| [SRC-F725E90B2A-L002262](../../tests/test_web_agent.py#L2262) | 2262 | `"    source_b = sample_source(1)"` | — |
| [SRC-F725E90B2A-L002263](../../tests/test_web_agent.py#L2263) | 2263 | `"    source_b.update({"` | — |
| [SRC-F725E90B2A-L002264](../../tests/test_web_agent.py#L2264) | 2264 | `"        \"title\": \"مشروعات عقارية في العاصمة الإدارية\","` | — |
| [SRC-F725E90B2A-L002265](../../tests/test_web_agent.py#L2265) | 2265 | `"        \"snippet\": \"تعرف على الوحدات السكنية المتاحة للبيع.\","` | — |
| [SRC-F725E90B2A-L002266](../../tests/test_web_agent.py#L2266) | 2266 | `"        \"page_text\": \"معلومات عامة عن مشروعات وشقق للبيع.\","` | — |
| [SRC-F725E90B2A-L002267](../../tests/test_web_agent.py#L2267) | 2267 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002268](../../tests/test_web_agent.py#L2268) | 2268 | `"    })"` | — |
| [SRC-F725E90B2A-L002269](../../tests/test_web_agent.py#L2269) | 2269 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002270](../../tests/test_web_agent.py#L2270) | 2270 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002271](../../tests/test_web_agent.py#L2271) | 2271 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002272](../../tests/test_web_agent.py#L2272) | 2272 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002273](../../tests/test_web_agent.py#L2273) | 2273 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002274](../../tests/test_web_agent.py#L2274) | 2274 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002275](../../tests/test_web_agent.py#L2275) | 2275 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002276](../../tests/test_web_agent.py#L2276) | 2276 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002277](../../tests/test_web_agent.py#L2277) | 2277 | `"    }"` | — |
| [SRC-F725E90B2A-L002278](../../tests/test_web_agent.py#L2278) | 2278 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda q, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002279](../../tests/test_web_agent.py#L2279) | 2279 | `"    monkeypatch.setattr(agent, \"_collect_research\", lambda p: ("` | — |
| [SRC-F725E90B2A-L002280](../../tests/test_web_agent.py#L2280) | 2280 | `"        [source_a, source_b], [], {"` | — |
| [SRC-F725E90B2A-L002281](../../tests/test_web_agent.py#L2281) | 2281 | `"            \"queries_planned\": 1, \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L002282](../../tests/test_web_agent.py#L2282) | 2282 | `"            \"query_results\": [{\"query\": question, \"results\": 2}],"` | — |
| [SRC-F725E90B2A-L002283](../../tests/test_web_agent.py#L2283) | 2283 | `"            \"unique_sources\": 2, \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L002284](../../tests/test_web_agent.py#L2284) | 2284 | `"            \"providers_used\": [\"test_provider\"], \"provider_counts\": {\"test_provider\": 2},"` | — |
| [SRC-F725E90B2A-L002285](../../tests/test_web_agent.py#L2285) | 2285 | `"            \"platform_counts\": {\"web\": 2}, \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002286](../../tests/test_web_agent.py#L2286) | 2286 | `"            \"depth\": \"standard\", \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002287](../../tests/test_web_agent.py#L2287) | 2287 | `"        }"` | — |
| [SRC-F725E90B2A-L002288](../../tests/test_web_agent.py#L2288) | 2288 | `"    ))"` | — |
| [SRC-F725E90B2A-L002289](../../tests/test_web_agent.py#L2289) | 2289 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002290](../../tests/test_web_agent.py#L2290) | 2290 | `"        agent, \"_generate\","` | — |
| [SRC-F725E90B2A-L002291](../../tests/test_web_agent.py#L2291) | 2291 | `"        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError(\"must not synthesize false leads\")),"` | — |
| [SRC-F725E90B2A-L002292](../../tests/test_web_agent.py#L2292) | 2292 | `"    )"` | — |
| [SRC-F725E90B2A-L002293](../../tests/test_web_agent.py#L2293) | 2293 | `""` | — |
| [SRC-F725E90B2A-L002294](../../tests/test_web_agent.py#L2294) | 2294 | `"    result = agent.answer(question)"` | — |
| [SRC-F725E90B2A-L002295](../../tests/test_web_agent.py#L2295) | 2295 | `""` | — |
| [SRC-F725E90B2A-L002296](../../tests/test_web_agent.py#L2296) | 2296 | `"    assert result[\"intent_route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-F725E90B2A-L002297](../../tests/test_web_agent.py#L2297) | 2297 | `"    assert result[\"kind\"] == \"lead_discovery_no_qualified_candidates\""` | — |
| [SRC-F725E90B2A-L002298](../../tests/test_web_agent.py#L2298) | 2298 | `"    assert result[\"search_report\"][\"lead_generation\"][\"candidate_signal_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002299](../../tests/test_web_agent.py#L2299) | 2299 | `"    assert result[\"search_report\"][\"lead_generation\"][\"related_results_reviewed\"] == 2"` | — |
| [SRC-F725E90B2A-L002300](../../tests/test_web_agent.py#L2300) | 2300 | `"    assert \"لم أعتبر إعلانات البيع\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L002301](../../tests/test_web_agent.py#L2301) | 2301 | `"    assert all(s[\"lead_qualification\"] == \"related_result_not_lead\" for s in result[\"sources\"])"` | — |
| [SRC-F725E90B2A-L002302](../../tests/test_web_agent.py#L2302) | 2302 | `""` | — |
| [SRC-F725E90B2A-L002303](../../tests/test_web_agent.py#L2303) | 2303 | `""` | — |
| [SRC-F725E90B2A-L002304](../../tests/test_web_agent.py#L2304) | 2304 | `"def test_lead_generation_search_plan_includes_high_intent_queries(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002305](../../tests/test_web_agent.py#L2305) | 2305 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002306](../../tests/test_web_agent.py#L2306) | 2306 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002307](../../tests/test_web_agent.py#L2307) | 2307 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002308](../../tests/test_web_agent.py#L2308) | 2308 | `"        \"queries\": [\"generic apartment listings\"],"` | — |
| [SRC-F725E90B2A-L002309](../../tests/test_web_agent.py#L2309) | 2309 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002310](../../tests/test_web_agent.py#L2310) | 2310 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002311](../../tests/test_web_agent.py#L2311) | 2311 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002312](../../tests/test_web_agent.py#L2312) | 2312 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002313](../../tests/test_web_agent.py#L2313) | 2313 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002314](../../tests/test_web_agent.py#L2314) | 2314 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002315](../../tests/test_web_agent.py#L2315) | 2315 | `"    }"` | — |
| [SRC-F725E90B2A-L002316](../../tests/test_web_agent.py#L2316) | 2316 | `""` | — |
| [SRC-F725E90B2A-L002317](../../tests/test_web_agent.py#L2317) | 2317 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L002318](../../tests/test_web_agent.py#L2318) | 2318 | `"        seen.update(research_plan)"` | — |
| [SRC-F725E90B2A-L002319](../../tests/test_web_agent.py#L2319) | 2319 | `"        source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002320](../../tests/test_web_agent.py#L2320) | 2320 | `"        source.update({"` | — |
| [SRC-F725E90B2A-L002321](../../tests/test_web_agent.py#L2321) | 2321 | `"            \"title\": \"مطلوب شقة تمليك في العاصمة الإدارية\","` | — |
| [SRC-F725E90B2A-L002322](../../tests/test_web_agent.py#L2322) | 2322 | `"            \"snippet\": \"صاحب المنشور يبحث عن شقة للشراء\","` | — |
| [SRC-F725E90B2A-L002323](../../tests/test_web_agent.py#L2323) | 2323 | `"            \"page_text\": \"مطلوب شقة تمليك في العاصمة الإدارية، أريد الشراء.\","` | — |
| [SRC-F725E90B2A-L002324](../../tests/test_web_agent.py#L2324) | 2324 | `"            \"queries\": list(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002325](../../tests/test_web_agent.py#L2325) | 2325 | `"        })"` | — |
| [SRC-F725E90B2A-L002326](../../tests/test_web_agent.py#L2326) | 2326 | `"        return [source], [], {"` | — |
| [SRC-F725E90B2A-L002327](../../tests/test_web_agent.py#L2327) | 2327 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002328](../../tests/test_web_agent.py#L2328) | 2328 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002329](../../tests/test_web_agent.py#L2329) | 2329 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L002330](../../tests/test_web_agent.py#L2330) | 2330 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L002331](../../tests/test_web_agent.py#L2331) | 2331 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L002332](../../tests/test_web_agent.py#L2332) | 2332 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L002333](../../tests/test_web_agent.py#L2333) | 2333 | `"            \"provider_counts\": {\"test_provider\": 1},"` | — |
| [SRC-F725E90B2A-L002334](../../tests/test_web_agent.py#L2334) | 2334 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L002335](../../tests/test_web_agent.py#L2335) | 2335 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002336](../../tests/test_web_agent.py#L2336) | 2336 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002337](../../tests/test_web_agent.py#L2337) | 2337 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002338](../../tests/test_web_agent.py#L2338) | 2338 | `"        }"` | — |
| [SRC-F725E90B2A-L002339](../../tests/test_web_agent.py#L2339) | 2339 | `""` | — |
| [SRC-F725E90B2A-L002340](../../tests/test_web_agent.py#L2340) | 2340 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda q, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002341](../../tests/test_web_agent.py#L2341) | 2341 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L002342](../../tests/test_web_agent.py#L2342) | 2342 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"عُثر على إشارة علنية محتملة [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L002343](../../tests/test_web_agent.py#L2343) | 2343 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L002344](../../tests/test_web_agent.py#L2344) | 2344 | `""` | — |
| [SRC-F725E90B2A-L002345](../../tests/test_web_agent.py#L2345) | 2345 | `"    result = agent.answer(\"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\")"` | — |
| [SRC-F725E90B2A-L002346](../../tests/test_web_agent.py#L2346) | 2346 | `""` | — |
| [SRC-F725E90B2A-L002347](../../tests/test_web_agent.py#L2347) | 2347 | `"    assert result[\"intent_route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-F725E90B2A-L002348](../../tests/test_web_agent.py#L2348) | 2348 | `"    assert seen[\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L002349](../../tests/test_web_agent.py#L2349) | 2349 | `"    assert len(seen[\"queries\"]) >= 4"` | — |
| [SRC-F725E90B2A-L002350](../../tests/test_web_agent.py#L2350) | 2350 | `"    assert any('\"مطلوب شراء\"' in q or '\"مطلوب شقه تمليك\"' in q for q in seen[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002351](../../tests/test_web_agent.py#L2351) | 2351 | `"    assert result[\"search_report\"][\"lead_generation\"][\"candidate_signal_count\"] == 1"` | — |
