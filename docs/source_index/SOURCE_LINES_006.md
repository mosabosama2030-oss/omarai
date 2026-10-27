# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **006**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L001445 إلى SRC-1AE03B9EC3-L002244
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L001445](../../agents/web_agent.py#L1445) | 1445 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001446](../../agents/web_agent.py#L1446) | 1446 | `"            url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001447](../../agents/web_agent.py#L1447) | 1447 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001448](../../agents/web_agent.py#L1448) | 1448 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001449](../../agents/web_agent.py#L1449) | 1449 | `"            snippets = item.get(\"extra_snippets\", [])"` | — |
| [SRC-1AE03B9EC3-L001450](../../agents/web_agent.py#L1450) | 1450 | `"            extra = \" \".join(x for x in snippets if isinstance(x, str)) if isinstance(snippets, list) else \"\""` | — |
| [SRC-1AE03B9EC3-L001451](../../agents/web_agent.py#L1451) | 1451 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001452](../../agents/web_agent.py#L1452) | 1452 | `"                \"title\": _clean_text(item.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001453](../../agents/web_agent.py#L1453) | 1453 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001454](../../agents/web_agent.py#L1454) | 1454 | `"                \"snippet\": _clean_text(item.get(\"description\", \"\") + \" \" + extra, 1600),"` | — |
| [SRC-1AE03B9EC3-L001455](../../agents/web_agent.py#L1455) | 1455 | `"                \"provider\": \"brave_search_api\","` | — |
| [SRC-1AE03B9EC3-L001456](../../agents/web_agent.py#L1456) | 1456 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001457](../../agents/web_agent.py#L1457) | 1457 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001458](../../agents/web_agent.py#L1458) | 1458 | `"                \"published_at\": _clean_text(item.get(\"page_age\", \"\") or item.get(\"published_at\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001459](../../agents/web_agent.py#L1459) | 1459 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001460](../../agents/web_agent.py#L1460) | 1460 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001461](../../agents/web_agent.py#L1461) | 1461 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001462](../../agents/web_agent.py#L1462) | 1462 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001463](../../agents/web_agent.py#L1463) | 1463 | `""` | — |
| [SRC-1AE03B9EC3-L001464](../../agents/web_agent.py#L1464) | 1464 | `"    def _search_tavily(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001465](../../agents/web_agent.py#L1465) | 1465 | `"        \"\"\"Use Tavily's official search API for structured, extractable live web results.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001466](../../agents/web_agent.py#L1466) | 1466 | `"        api_key = os.getenv(\"TAVILY_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001467](../../agents/web_agent.py#L1467) | 1467 | `"        if not api_key:"` | — |
| [SRC-1AE03B9EC3-L001468](../../agents/web_agent.py#L1468) | 1468 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001469](../../agents/web_agent.py#L1469) | 1469 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001470](../../agents/web_agent.py#L1470) | 1470 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L001471](../../agents/web_agent.py#L1471) | 1471 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L001472](../../agents/web_agent.py#L1472) | 1472 | `"            raise AgentDependencyError(\"حزمة httpx غير مثبتة.\") from exc"` | — |
| [SRC-1AE03B9EC3-L001473](../../agents/web_agent.py#L1473) | 1473 | `"        from agents.research import detect_depth, detect_freshness"` | — |
| [SRC-1AE03B9EC3-L001474](../../agents/web_agent.py#L1474) | 1474 | `""` | — |
| [SRC-1AE03B9EC3-L001475](../../agents/web_agent.py#L1475) | 1475 | `"        response = httpx.post("` | — |
| [SRC-1AE03B9EC3-L001476](../../agents/web_agent.py#L1476) | 1476 | `"            \"https://api.tavily.com/search\","` | — |
| [SRC-1AE03B9EC3-L001477](../../agents/web_agent.py#L1477) | 1477 | `"            json={"` | — |
| [SRC-1AE03B9EC3-L001478](../../agents/web_agent.py#L1478) | 1478 | `"                \"api_key\": api_key,"` | — |
| [SRC-1AE03B9EC3-L001479](../../agents/web_agent.py#L1479) | 1479 | `"                \"query\": query[:500],"` | — |
| [SRC-1AE03B9EC3-L001480](../../agents/web_agent.py#L1480) | 1480 | `"                \"search_depth\": \"advanced\" if detect_depth(query) == \"deep\" else \"basic\","` | — |
| [SRC-1AE03B9EC3-L001481](../../agents/web_agent.py#L1481) | 1481 | `"                \"topic\": \"news\" if detect_freshness(query) else \"general\","` | — |
| [SRC-1AE03B9EC3-L001482](../../agents/web_agent.py#L1482) | 1482 | `"                \"max_results\": MAX_PROVIDER_RESULTS,"` | — |
| [SRC-1AE03B9EC3-L001483](../../agents/web_agent.py#L1483) | 1483 | `"                \"include_answer\": False,"` | — |
| [SRC-1AE03B9EC3-L001484](../../agents/web_agent.py#L1484) | 1484 | `"                \"include_raw_content\": False,"` | — |
| [SRC-1AE03B9EC3-L001485](../../agents/web_agent.py#L1485) | 1485 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001486](../../agents/web_agent.py#L1486) | 1486 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001487](../../agents/web_agent.py#L1487) | 1487 | `"                \"Accept\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001488](../../agents/web_agent.py#L1488) | 1488 | `"                \"Content-Type\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001489](../../agents/web_agent.py#L1489) | 1489 | `"                \"User-Agent\": \"OmaraiResearchAgent/1.0\","` | — |
| [SRC-1AE03B9EC3-L001490](../../agents/web_agent.py#L1490) | 1490 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001491](../../agents/web_agent.py#L1491) | 1491 | `"            timeout=self._effective_timeout(8.5),"` | — |
| [SRC-1AE03B9EC3-L001492](../../agents/web_agent.py#L1492) | 1492 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001493](../../agents/web_agent.py#L1493) | 1493 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001494](../../agents/web_agent.py#L1494) | 1494 | `"        response.raise_for_status()"` | — |
| [SRC-1AE03B9EC3-L001495](../../agents/web_agent.py#L1495) | 1495 | `"        payload = response.json()"` | — |
| [SRC-1AE03B9EC3-L001496](../../agents/web_agent.py#L1496) | 1496 | `"        search_results = payload.get(\"results\", [])"` | — |
| [SRC-1AE03B9EC3-L001497](../../agents/web_agent.py#L1497) | 1497 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001498](../../agents/web_agent.py#L1498) | 1498 | `"        for item in search_results if isinstance(search_results, list) else []:"` | — |
| [SRC-1AE03B9EC3-L001499](../../agents/web_agent.py#L1499) | 1499 | `"            if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L001500](../../agents/web_agent.py#L1500) | 1500 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001501](../../agents/web_agent.py#L1501) | 1501 | `"            url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001502](../../agents/web_agent.py#L1502) | 1502 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001503](../../agents/web_agent.py#L1503) | 1503 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001504](../../agents/web_agent.py#L1504) | 1504 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001505](../../agents/web_agent.py#L1505) | 1505 | `"                \"title\": _clean_text(item.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001506](../../agents/web_agent.py#L1506) | 1506 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001507](../../agents/web_agent.py#L1507) | 1507 | `"                \"snippet\": _clean_text(item.get(\"content\", \"\"), 1600),"` | — |
| [SRC-1AE03B9EC3-L001508](../../agents/web_agent.py#L1508) | 1508 | `"                \"provider\": \"tavily_search_api\","` | — |
| [SRC-1AE03B9EC3-L001509](../../agents/web_agent.py#L1509) | 1509 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001510](../../agents/web_agent.py#L1510) | 1510 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001511](../../agents/web_agent.py#L1511) | 1511 | `"                \"published_at\": _clean_text(item.get(\"published_date\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001512](../../agents/web_agent.py#L1512) | 1512 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001513](../../agents/web_agent.py#L1513) | 1513 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001514](../../agents/web_agent.py#L1514) | 1514 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001515](../../agents/web_agent.py#L1515) | 1515 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001516](../../agents/web_agent.py#L1516) | 1516 | `""` | — |
| [SRC-1AE03B9EC3-L001517](../../agents/web_agent.py#L1517) | 1517 | `"    def _search_news(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001518](../../agents/web_agent.py#L1518) | 1518 | `"        \"\"\"Read the public Google News RSS search feed for freshness-sensitive queries.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001519](../../agents/web_agent.py#L1519) | 1519 | `"        import xml.etree.ElementTree as ET"` | — |
| [SRC-1AE03B9EC3-L001520](../../agents/web_agent.py#L1520) | 1520 | `""` | — |
| [SRC-1AE03B9EC3-L001521](../../agents/web_agent.py#L1521) | 1521 | `"        import httpx"` | — |
| [SRC-1AE03B9EC3-L001522](../../agents/web_agent.py#L1522) | 1522 | `""` | — |
| [SRC-1AE03B9EC3-L001523](../../agents/web_agent.py#L1523) | 1523 | `"        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001524](../../agents/web_agent.py#L1524) | 1524 | `"            \"https://news.google.com/rss/search\","` | — |
| [SRC-1AE03B9EC3-L001525](../../agents/web_agent.py#L1525) | 1525 | `"            params={\"q\": query, \"hl\": \"ar\", \"gl\": \"EG\", \"ceid\": \"EG:ar\"},"` | — |
| [SRC-1AE03B9EC3-L001526](../../agents/web_agent.py#L1526) | 1526 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001527](../../agents/web_agent.py#L1527) | 1527 | `"                \"User-Agent\": \"OmaraiResearchBot/1.2\","` | — |
| [SRC-1AE03B9EC3-L001528](../../agents/web_agent.py#L1528) | 1528 | `"                \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001529](../../agents/web_agent.py#L1529) | 1529 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001530](../../agents/web_agent.py#L1530) | 1530 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001531](../../agents/web_agent.py#L1531) | 1531 | `"            # Refuse automatic redirects from public search endpoints; never fetch an"` | — |
| [SRC-1AE03B9EC3-L001532](../../agents/web_agent.py#L1532) | 1532 | `"            # unchecked redirect target as part of a provider search request."` | — |
| [SRC-1AE03B9EC3-L001533](../../agents/web_agent.py#L1533) | 1533 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001534](../../agents/web_agent.py#L1534) | 1534 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001535](../../agents/web_agent.py#L1535) | 1535 | `"        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001536](../../agents/web_agent.py#L1536) | 1536 | `"            raise RuntimeError(f\"HTTP {response.status_code}\")"` | — |
| [SRC-1AE03B9EC3-L001537](../../agents/web_agent.py#L1537) | 1537 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001538](../../agents/web_agent.py#L1538) | 1538 | `"            root = ET.fromstring(response.content)"` | — |
| [SRC-1AE03B9EC3-L001539](../../agents/web_agent.py#L1539) | 1539 | `"        except ET.ParseError as exc:"` | — |
| [SRC-1AE03B9EC3-L001540](../../agents/web_agent.py#L1540) | 1540 | `"            raise RuntimeError(\"invalid RSS XML\") from exc"` | — |
| [SRC-1AE03B9EC3-L001541](../../agents/web_agent.py#L1541) | 1541 | `"        results: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001542](../../agents/web_agent.py#L1542) | 1542 | `"        for item in root.iter():"` | — |
| [SRC-1AE03B9EC3-L001543](../../agents/web_agent.py#L1543) | 1543 | `"            if item.tag.rsplit(\"}\", 1)[-1] != \"item\":"` | — |
| [SRC-1AE03B9EC3-L001544](../../agents/web_agent.py#L1544) | 1544 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001545](../../agents/web_agent.py#L1545) | 1545 | `"            fields = {"` | — |
| [SRC-1AE03B9EC3-L001546](../../agents/web_agent.py#L1546) | 1546 | `"                child.tag.rsplit(\"}\", 1)[-1]: (child.text or \"\")"` | — |
| [SRC-1AE03B9EC3-L001547](../../agents/web_agent.py#L1547) | 1547 | `"                for child in item"` | — |
| [SRC-1AE03B9EC3-L001548](../../agents/web_agent.py#L1548) | 1548 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001549](../../agents/web_agent.py#L1549) | 1549 | `"            url = _public_http_url(fields.get(\"link\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001550](../../agents/web_agent.py#L1550) | 1550 | `"            if not url or _blocked_source_url(url):"` | — |
| [SRC-1AE03B9EC3-L001551](../../agents/web_agent.py#L1551) | 1551 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001552](../../agents/web_agent.py#L1552) | 1552 | `"            # Keep every parseable, safe candidate here. _search_web applies the"` | — |
| [SRC-1AE03B9EC3-L001553](../../agents/web_agent.py#L1553) | 1553 | `"            # shared relevance filter and records accepted/rejected counters."` | — |
| [SRC-1AE03B9EC3-L001554](../../agents/web_agent.py#L1554) | 1554 | `"            # Filtering again in this adapter mislabels a valid feed as no results."` | — |
| [SRC-1AE03B9EC3-L001555](../../agents/web_agent.py#L1555) | 1555 | `"            source_node = next("` | — |
| [SRC-1AE03B9EC3-L001556](../../agents/web_agent.py#L1556) | 1556 | `"                (child for child in item if child.tag.rsplit(\"}\", 1)[-1] == \"source\"),"` | — |
| [SRC-1AE03B9EC3-L001557](../../agents/web_agent.py#L1557) | 1557 | `"                None,"` | — |
| [SRC-1AE03B9EC3-L001558](../../agents/web_agent.py#L1558) | 1558 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001559](../../agents/web_agent.py#L1559) | 1559 | `"            publisher_url = _public_http_url("` | — |
| [SRC-1AE03B9EC3-L001560](../../agents/web_agent.py#L1560) | 1560 | `"                source_node.attrib.get(\"url\", \"\") if source_node is not None else \"\""` | — |
| [SRC-1AE03B9EC3-L001561](../../agents/web_agent.py#L1561) | 1561 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001562](../../agents/web_agent.py#L1562) | 1562 | `"            publisher_name = _clean_text("` | — |
| [SRC-1AE03B9EC3-L001563](../../agents/web_agent.py#L1563) | 1563 | `"                source_node.text if source_node is not None else \"\", 200"` | — |
| [SRC-1AE03B9EC3-L001564](../../agents/web_agent.py#L1564) | 1564 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001565](../../agents/web_agent.py#L1565) | 1565 | `"            publisher_domain = ("` | — |
| [SRC-1AE03B9EC3-L001566](../../agents/web_agent.py#L1566) | 1566 | `"                (urllib.parse.urlparse(publisher_url).hostname or \"\").lower()"` | — |
| [SRC-1AE03B9EC3-L001567](../../agents/web_agent.py#L1567) | 1567 | `"                if publisher_url else \"\""` | — |
| [SRC-1AE03B9EC3-L001568](../../agents/web_agent.py#L1568) | 1568 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001569](../../agents/web_agent.py#L1569) | 1569 | `"            results.append({"` | — |
| [SRC-1AE03B9EC3-L001570](../../agents/web_agent.py#L1570) | 1570 | `"                \"title\": _clean_text(fields.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001571](../../agents/web_agent.py#L1571) | 1571 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001572](../../agents/web_agent.py#L1572) | 1572 | `"                \"snippet\": _clean_text(fields.get(\"description\", \"\"), 1200),"` | — |
| [SRC-1AE03B9EC3-L001573](../../agents/web_agent.py#L1573) | 1573 | `"                \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001574](../../agents/web_agent.py#L1574) | 1574 | `"                \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001575](../../agents/web_agent.py#L1575) | 1575 | `"                \"provider\": \"google_news_rss\","` | — |
| [SRC-1AE03B9EC3-L001576](../../agents/web_agent.py#L1576) | 1576 | `"                \"provider_rank\": len(results) + 1,"` | — |
| [SRC-1AE03B9EC3-L001577](../../agents/web_agent.py#L1577) | 1577 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001578](../../agents/web_agent.py#L1578) | 1578 | `"                \"published_at\": _clean_text(fields.get(\"pubDate\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001579](../../agents/web_agent.py#L1579) | 1579 | `"                \"publisher_name\": publisher_name,"` | — |
| [SRC-1AE03B9EC3-L001580](../../agents/web_agent.py#L1580) | 1580 | `"                \"publisher_url\": publisher_url or \"\","` | — |
| [SRC-1AE03B9EC3-L001581](../../agents/web_agent.py#L1581) | 1581 | `"                \"publisher_domain\": publisher_domain,"` | — |
| [SRC-1AE03B9EC3-L001582](../../agents/web_agent.py#L1582) | 1582 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001583](../../agents/web_agent.py#L1583) | 1583 | `"            if len(results) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001584](../../agents/web_agent.py#L1584) | 1584 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001585](../../agents/web_agent.py#L1585) | 1585 | `"        return results"` | — |
| [SRC-1AE03B9EC3-L001586](../../agents/web_agent.py#L1586) | 1586 | `""` | — |
| [SRC-1AE03B9EC3-L001587](../../agents/web_agent.py#L1587) | 1587 | `"    def _search_social("` | — |
| [SRC-1AE03B9EC3-L001588](../../agents/web_agent.py#L1588) | 1588 | `"        self, query: str, platforms: list[str]"` | — |
| [SRC-1AE03B9EC3-L001589](../../agents/web_agent.py#L1589) | 1589 | `"    ) -> tuple[list[dict[str, Any]], list[str]]:"` | — |
| [SRC-1AE03B9EC3-L001590](../../agents/web_agent.py#L1590) | 1590 | `"        \"\"\"Search public social content through exposed public endpoints only.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001591](../../agents/web_agent.py#L1591) | 1591 | `"        query = compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L001592](../../agents/web_agent.py#L1592) | 1592 | `"        if not query:"` | — |
| [SRC-1AE03B9EC3-L001593](../../agents/web_agent.py#L1593) | 1593 | `"            return [], [\"لم يبدأ البحث الاجتماعي لعدم وجود كلمات موضوعية قابلة للبحث.\"]"` | — |
| [SRC-1AE03B9EC3-L001594](../../agents/web_agent.py#L1594) | 1594 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001595](../../agents/web_agent.py#L1595) | 1595 | `"            import xml.etree.ElementTree as ET"` | — |
| [SRC-1AE03B9EC3-L001596](../../agents/web_agent.py#L1596) | 1596 | `""` | — |
| [SRC-1AE03B9EC3-L001597](../../agents/web_agent.py#L1597) | 1597 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L001598](../../agents/web_agent.py#L1598) | 1598 | `"            from bs4 import BeautifulSoup"` | — |
| [SRC-1AE03B9EC3-L001599](../../agents/web_agent.py#L1599) | 1599 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L001600](../../agents/web_agent.py#L1600) | 1600 | `"            raise AgentDependencyError("` | — |
| [SRC-1AE03B9EC3-L001601](../../agents/web_agent.py#L1601) | 1601 | `"                \"حزم البحث الاجتماعي غير مثبتة. نفّذ: python -m pip install -e .\""` | — |
| [SRC-1AE03B9EC3-L001602](../../agents/web_agent.py#L1602) | 1602 | `"            ) from exc"` | — |
| [SRC-1AE03B9EC3-L001603](../../agents/web_agent.py#L1603) | 1603 | `""` | — |
| [SRC-1AE03B9EC3-L001604](../../agents/web_agent.py#L1604) | 1604 | `"        results: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001605](../../agents/web_agent.py#L1605) | 1605 | `"        warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L001606](../../agents/web_agent.py#L1606) | 1606 | `"        headers = {"` | — |
| [SRC-1AE03B9EC3-L001607](../../agents/web_agent.py#L1607) | 1607 | `"            \"User-Agent\": \"OmaraiResearchBot/1.0 (public-content search; no login)\","` | — |
| [SRC-1AE03B9EC3-L001608](../../agents/web_agent.py#L1608) | 1608 | `"            \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001609](../../agents/web_agent.py#L1609) | 1609 | `"        }"` | — |
| [SRC-1AE03B9EC3-L001610](../../agents/web_agent.py#L1610) | 1610 | `""` | — |
| [SRC-1AE03B9EC3-L001611](../../agents/web_agent.py#L1611) | 1611 | `"        reddit_client_id = os.getenv(\"REDDIT_CLIENT_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001612](../../agents/web_agent.py#L1612) | 1612 | `"        reddit_client_secret = os.getenv(\"REDDIT_CLIENT_SECRET\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001613](../../agents/web_agent.py#L1613) | 1613 | `"        reddit_user_agent = os.getenv("` | — |
| [SRC-1AE03B9EC3-L001614](../../agents/web_agent.py#L1614) | 1614 | `"            \"REDDIT_USER_AGENT\","` | — |
| [SRC-1AE03B9EC3-L001615](../../agents/web_agent.py#L1615) | 1615 | `"            \"web:omarai-research-agent:v0.3 (public-content research)\","` | — |
| [SRC-1AE03B9EC3-L001616](../../agents/web_agent.py#L1616) | 1616 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L001617](../../agents/web_agent.py#L1617) | 1617 | `"        if \"reddit\" in platforms and reddit_client_id and reddit_client_secret:"` | — |
| [SRC-1AE03B9EC3-L001618](../../agents/web_agent.py#L1618) | 1618 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001619](../../agents/web_agent.py#L1619) | 1619 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001620](../../agents/web_agent.py#L1620) | 1620 | `"                token_response = httpx.post("` | — |
| [SRC-1AE03B9EC3-L001621](../../agents/web_agent.py#L1621) | 1621 | `"                    \"https://www.reddit.com/api/v1/access_token\","` | — |
| [SRC-1AE03B9EC3-L001622](../../agents/web_agent.py#L1622) | 1622 | `"                    data={\"grant_type\": \"client_credentials\"},"` | — |
| [SRC-1AE03B9EC3-L001623](../../agents/web_agent.py#L1623) | 1623 | `"                    auth=(reddit_client_id, reddit_client_secret),"` | — |
| [SRC-1AE03B9EC3-L001624](../../agents/web_agent.py#L1624) | 1624 | `"                    headers={\"User-Agent\": reddit_user_agent},"` | — |
| [SRC-1AE03B9EC3-L001625](../../agents/web_agent.py#L1625) | 1625 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001626](../../agents/web_agent.py#L1626) | 1626 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001627](../../agents/web_agent.py#L1627) | 1627 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001628](../../agents/web_agent.py#L1628) | 1628 | `"                if token_response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001629](../../agents/web_agent.py#L1629) | 1629 | `"                    access_token = token_response.json().get(\"access_token\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001630](../../agents/web_agent.py#L1630) | 1630 | `"                    if access_token:"` | — |
| [SRC-1AE03B9EC3-L001631](../../agents/web_agent.py#L1631) | 1631 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001632](../../agents/web_agent.py#L1632) | 1632 | `"                        search_response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001633](../../agents/web_agent.py#L1633) | 1633 | `"                            \"https://oauth.reddit.com/search\","` | — |
| [SRC-1AE03B9EC3-L001634](../../agents/web_agent.py#L1634) | 1634 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L001635](../../agents/web_agent.py#L1635) | 1635 | `"                                \"q\": query,"` | — |
| [SRC-1AE03B9EC3-L001636](../../agents/web_agent.py#L1636) | 1636 | `"                                \"sort\": \"relevance\","` | — |
| [SRC-1AE03B9EC3-L001637](../../agents/web_agent.py#L1637) | 1637 | `"                                \"t\": \"all\","` | — |
| [SRC-1AE03B9EC3-L001638](../../agents/web_agent.py#L1638) | 1638 | `"                                \"limit\": 10,"` | — |
| [SRC-1AE03B9EC3-L001639](../../agents/web_agent.py#L1639) | 1639 | `"                                \"type\": \"link\","` | — |
| [SRC-1AE03B9EC3-L001640](../../agents/web_agent.py#L1640) | 1640 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L001641](../../agents/web_agent.py#L1641) | 1641 | `"                            headers={"` | — |
| [SRC-1AE03B9EC3-L001642](../../agents/web_agent.py#L1642) | 1642 | `"                                **headers,"` | — |
| [SRC-1AE03B9EC3-L001643](../../agents/web_agent.py#L1643) | 1643 | `"                                \"User-Agent\": reddit_user_agent,"` | — |
| [SRC-1AE03B9EC3-L001644](../../agents/web_agent.py#L1644) | 1644 | `"                                \"Authorization\": \"Bearer \" + access_token,"` | — |
| [SRC-1AE03B9EC3-L001645](../../agents/web_agent.py#L1645) | 1645 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L001646](../../agents/web_agent.py#L1646) | 1646 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001647](../../agents/web_agent.py#L1647) | 1647 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001648](../../agents/web_agent.py#L1648) | 1648 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L001649](../../agents/web_agent.py#L1649) | 1649 | `"                        if search_response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001650](../../agents/web_agent.py#L1650) | 1650 | `"                            children = search_response.json().get(\"data\", {}).get(\"children\", [])"` | — |
| [SRC-1AE03B9EC3-L001651](../../agents/web_agent.py#L1651) | 1651 | `"                            rank = 0"` | — |
| [SRC-1AE03B9EC3-L001652](../../agents/web_agent.py#L1652) | 1652 | `"                            for child in children:"` | — |
| [SRC-1AE03B9EC3-L001653](../../agents/web_agent.py#L1653) | 1653 | `"                                post = child.get(\"data\", {}) if isinstance(child, dict) else {}"` | — |
| [SRC-1AE03B9EC3-L001654](../../agents/web_agent.py#L1654) | 1654 | `"                                permalink = str(post.get(\"permalink\") or \"\")"` | — |
| [SRC-1AE03B9EC3-L001655](../../agents/web_agent.py#L1655) | 1655 | `"                                url = _public_http_url("` | — |
| [SRC-1AE03B9EC3-L001656](../../agents/web_agent.py#L1656) | 1656 | `"                                    permalink if permalink.startswith(\"http\")"` | — |
| [SRC-1AE03B9EC3-L001657](../../agents/web_agent.py#L1657) | 1657 | `"                                    else \"https://www.reddit.com\" + permalink"` | — |
| [SRC-1AE03B9EC3-L001658](../../agents/web_agent.py#L1658) | 1658 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L001659](../../agents/web_agent.py#L1659) | 1659 | `"                                if not url:"` | — |
| [SRC-1AE03B9EC3-L001660](../../agents/web_agent.py#L1660) | 1660 | `"                                    continue"` | — |
| [SRC-1AE03B9EC3-L001661](../../agents/web_agent.py#L1661) | 1661 | `"                                rank += 1"` | — |
| [SRC-1AE03B9EC3-L001662](../../agents/web_agent.py#L1662) | 1662 | `"                                snippet = _clean_text(post.get(\"selftext\") or \"\", 1000)"` | — |
| [SRC-1AE03B9EC3-L001663](../../agents/web_agent.py#L1663) | 1663 | `"                                metrics = []"` | — |
| [SRC-1AE03B9EC3-L001664](../../agents/web_agent.py#L1664) | 1664 | `"                                if post.get(\"score\") is not None:"` | — |
| [SRC-1AE03B9EC3-L001665](../../agents/web_agent.py#L1665) | 1665 | `"                                    metrics.append(\"score=\" + str(post[\"score\"]))"` | — |
| [SRC-1AE03B9EC3-L001666](../../agents/web_agent.py#L1666) | 1666 | `"                                if post.get(\"num_comments\") is not None:"` | — |
| [SRC-1AE03B9EC3-L001667](../../agents/web_agent.py#L1667) | 1667 | `"                                    metrics.append(\"comments=\" + str(post[\"num_comments\"]))"` | — |
| [SRC-1AE03B9EC3-L001668](../../agents/web_agent.py#L1668) | 1668 | `"                                if metrics:"` | — |
| [SRC-1AE03B9EC3-L001669](../../agents/web_agent.py#L1669) | 1669 | `"                                    snippet = (snippet + \" \| \" if snippet else \"\") + \", \".join(metrics)"` | — |
| [SRC-1AE03B9EC3-L001670](../../agents/web_agent.py#L1670) | 1670 | `"                                results.append({"` | — |
| [SRC-1AE03B9EC3-L001671](../../agents/web_agent.py#L1671) | 1671 | `"                                    \"title\": _clean_text(post.get(\"title\") or \"Reddit post\", 300),"` | — |
| [SRC-1AE03B9EC3-L001672](../../agents/web_agent.py#L1672) | 1672 | `"                                    \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001673](../../agents/web_agent.py#L1673) | 1673 | `"                                    \"snippet\": snippet,"` | — |
| [SRC-1AE03B9EC3-L001674](../../agents/web_agent.py#L1674) | 1674 | `"                                    \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001675](../../agents/web_agent.py#L1675) | 1675 | `"                                    \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001676](../../agents/web_agent.py#L1676) | 1676 | `"                                    \"provider\": \"reddit_oauth_api\","` | — |
| [SRC-1AE03B9EC3-L001677](../../agents/web_agent.py#L1677) | 1677 | `"                                    \"provider_rank\": rank,"` | — |
| [SRC-1AE03B9EC3-L001678](../../agents/web_agent.py#L1678) | 1678 | `"                                    \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001679](../../agents/web_agent.py#L1679) | 1679 | `"                                    \"published_at\": _clean_text(str(post.get(\"created_utc\") or \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001680](../../agents/web_agent.py#L1680) | 1680 | `"                                })"` | — |
| [SRC-1AE03B9EC3-L001681](../../agents/web_agent.py#L1681) | 1681 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L001682](../../agents/web_agent.py#L1682) | 1682 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L001683](../../agents/web_agent.py#L1683) | 1683 | `"                                f\"Reddit OAuth search unavailable (HTTP {search_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L001684](../../agents/web_agent.py#L1684) | 1684 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L001685](../../agents/web_agent.py#L1685) | 1685 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L001686](../../agents/web_agent.py#L1686) | 1686 | `"                        warnings.append(\"Reddit OAuth did not return an access token.\")"` | — |
| [SRC-1AE03B9EC3-L001687](../../agents/web_agent.py#L1687) | 1687 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001688](../../agents/web_agent.py#L1688) | 1688 | `"                    warnings.append("` | — |
| [SRC-1AE03B9EC3-L001689](../../agents/web_agent.py#L1689) | 1689 | `"                        f\"Reddit OAuth authentication unavailable (HTTP {token_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L001690](../../agents/web_agent.py#L1690) | 1690 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L001691](../../agents/web_agent.py#L1691) | 1691 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L001692](../../agents/web_agent.py#L1692) | 1692 | `"                warnings.append(\"Reddit OAuth search failed for this request.\")"` | — |
| [SRC-1AE03B9EC3-L001693](../../agents/web_agent.py#L1693) | 1693 | `""` | — |
| [SRC-1AE03B9EC3-L001694](../../agents/web_agent.py#L1694) | 1694 | `"        if \"reddit\" in platforms and not any("` | — |
| [SRC-1AE03B9EC3-L001695](../../agents/web_agent.py#L1695) | 1695 | `"            row.get(\"provider\") == \"reddit_oauth_api\" for row in results"` | — |
| [SRC-1AE03B9EC3-L001696](../../agents/web_agent.py#L1696) | 1696 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L001697](../../agents/web_agent.py#L1697) | 1697 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001698](../../agents/web_agent.py#L1698) | 1698 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001699](../../agents/web_agent.py#L1699) | 1699 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001700](../../agents/web_agent.py#L1700) | 1700 | `"                    \"https://www.reddit.com/search.rss\","` | — |
| [SRC-1AE03B9EC3-L001701](../../agents/web_agent.py#L1701) | 1701 | `"                    params={\"q\": query, \"sort\": \"relevance\", \"t\": \"all\", \"limit\": \"8\"},"` | — |
| [SRC-1AE03B9EC3-L001702](../../agents/web_agent.py#L1702) | 1702 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L001703](../../agents/web_agent.py#L1703) | 1703 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001704](../../agents/web_agent.py#L1704) | 1704 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001705](../../agents/web_agent.py#L1705) | 1705 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001706](../../agents/web_agent.py#L1706) | 1706 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001707](../../agents/web_agent.py#L1707) | 1707 | `"                    root = ET.fromstring(response.content)"` | — |
| [SRC-1AE03B9EC3-L001708](../../agents/web_agent.py#L1708) | 1708 | `"                    for item in root.iter():"` | — |
| [SRC-1AE03B9EC3-L001709](../../agents/web_agent.py#L1709) | 1709 | `"                        if item.tag.rsplit(\"}\", 1)[-1] != \"item\":"` | — |
| [SRC-1AE03B9EC3-L001710](../../agents/web_agent.py#L1710) | 1710 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001711](../../agents/web_agent.py#L1711) | 1711 | `"                        fields = {"` | — |
| [SRC-1AE03B9EC3-L001712](../../agents/web_agent.py#L1712) | 1712 | `"                            child.tag.rsplit(\"}\", 1)[-1]: (child.text or \"\")"` | — |
| [SRC-1AE03B9EC3-L001713](../../agents/web_agent.py#L1713) | 1713 | `"                            for child in item"` | — |
| [SRC-1AE03B9EC3-L001714](../../agents/web_agent.py#L1714) | 1714 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L001715](../../agents/web_agent.py#L1715) | 1715 | `"                        url = _public_http_url(fields.get(\"link\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001716](../../agents/web_agent.py#L1716) | 1716 | `"                        if not url or \"reddit.com/\" not in url:"` | — |
| [SRC-1AE03B9EC3-L001717](../../agents/web_agent.py#L1717) | 1717 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001718](../../agents/web_agent.py#L1718) | 1718 | `"                        description = BeautifulSoup("` | — |
| [SRC-1AE03B9EC3-L001719](../../agents/web_agent.py#L1719) | 1719 | `"                            fields.get(\"description\", \"\"), \"html.parser\""` | — |
| [SRC-1AE03B9EC3-L001720](../../agents/web_agent.py#L1720) | 1720 | `"                        ).get_text(\" \", strip=True)"` | — |
| [SRC-1AE03B9EC3-L001721](../../agents/web_agent.py#L1721) | 1721 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L001722](../../agents/web_agent.py#L1722) | 1722 | `"                            \"title\": _clean_text(fields.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001723](../../agents/web_agent.py#L1723) | 1723 | `"                            \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001724](../../agents/web_agent.py#L1724) | 1724 | `"                            \"snippet\": _clean_text(description, 1200),"` | — |
| [SRC-1AE03B9EC3-L001725](../../agents/web_agent.py#L1725) | 1725 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001726](../../agents/web_agent.py#L1726) | 1726 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001727](../../agents/web_agent.py#L1727) | 1727 | `"                            \"provider\": \"reddit_public_rss\","` | — |
| [SRC-1AE03B9EC3-L001728](../../agents/web_agent.py#L1728) | 1728 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L001729](../../agents/web_agent.py#L1729) | 1729 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L001730](../../agents/web_agent.py#L1730) | 1730 | `"                                if row.get(\"provider\") == \"reddit_public_rss\""` | — |
| [SRC-1AE03B9EC3-L001731](../../agents/web_agent.py#L1731) | 1731 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L001732](../../agents/web_agent.py#L1732) | 1732 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001733](../../agents/web_agent.py#L1733) | 1733 | `"                            \"published_at\": _clean_text(fields.get(\"pubDate\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001734](../../agents/web_agent.py#L1734) | 1734 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L001735](../../agents/web_agent.py#L1735) | 1735 | `"                        if sum(row.get(\"provider\") == \"reddit_public_rss\" for row in results) >= 8:"` | — |
| [SRC-1AE03B9EC3-L001736](../../agents/web_agent.py#L1736) | 1736 | `"                            break"` | — |
| [SRC-1AE03B9EC3-L001737](../../agents/web_agent.py#L1737) | 1737 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001738](../../agents/web_agent.py#L1738) | 1738 | `"                    warnings.append(f\"Reddit public RSS unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L001739](../../agents/web_agent.py#L1739) | 1739 | `"            except (httpx.HTTPError, OSError, ValueError, ET.ParseError):"` | — |
| [SRC-1AE03B9EC3-L001740](../../agents/web_agent.py#L1740) | 1740 | `"                warnings.append(\"Reddit public RSS unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L001741](../../agents/web_agent.py#L1741) | 1741 | `""` | — |
| [SRC-1AE03B9EC3-L001742](../../agents/web_agent.py#L1742) | 1742 | `"        if \"bluesky\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L001743](../../agents/web_agent.py#L1743) | 1743 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001744](../../agents/web_agent.py#L1744) | 1744 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001745](../../agents/web_agent.py#L1745) | 1745 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001746](../../agents/web_agent.py#L1746) | 1746 | `"                    \"https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts\","` | — |
| [SRC-1AE03B9EC3-L001747](../../agents/web_agent.py#L1747) | 1747 | `"                    params={\"q\": query, \"limit\": 10},"` | — |
| [SRC-1AE03B9EC3-L001748](../../agents/web_agent.py#L1748) | 1748 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L001749](../../agents/web_agent.py#L1749) | 1749 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001750](../../agents/web_agent.py#L1750) | 1750 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001751](../../agents/web_agent.py#L1751) | 1751 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001752](../../agents/web_agent.py#L1752) | 1752 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001753](../../agents/web_agent.py#L1753) | 1753 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L001754](../../agents/web_agent.py#L1754) | 1754 | `"                    for item in data.get(\"posts\", []):"` | — |
| [SRC-1AE03B9EC3-L001755](../../agents/web_agent.py#L1755) | 1755 | `"                        post = item.get(\"post\", {})"` | — |
| [SRC-1AE03B9EC3-L001756](../../agents/web_agent.py#L1756) | 1756 | `"                        record = post.get(\"record\", {})"` | — |
| [SRC-1AE03B9EC3-L001757](../../agents/web_agent.py#L1757) | 1757 | `"                        author = post.get(\"author\", {})"` | — |
| [SRC-1AE03B9EC3-L001758](../../agents/web_agent.py#L1758) | 1758 | `"                        uri = post.get(\"uri\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001759](../../agents/web_agent.py#L1759) | 1759 | `"                        rkey = uri.rsplit(\"/\", 1)[-1]"` | — |
| [SRC-1AE03B9EC3-L001760](../../agents/web_agent.py#L1760) | 1760 | `"                        handle = author.get(\"handle\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001761](../../agents/web_agent.py#L1761) | 1761 | `"                        if not handle or not rkey:"` | — |
| [SRC-1AE03B9EC3-L001762](../../agents/web_agent.py#L1762) | 1762 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001763](../../agents/web_agent.py#L1763) | 1763 | `"                        url = f\"https://bsky.app/profile/{handle}/post/{rkey}\""` | — |
| [SRC-1AE03B9EC3-L001764](../../agents/web_agent.py#L1764) | 1764 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L001765](../../agents/web_agent.py#L1765) | 1765 | `"                            \"title\": _clean_text(author.get(\"displayName\") or handle, 300),"` | — |
| [SRC-1AE03B9EC3-L001766](../../agents/web_agent.py#L1766) | 1766 | `"                            \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001767](../../agents/web_agent.py#L1767) | 1767 | `"                            \"snippet\": _clean_text(record.get(\"text\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L001768](../../agents/web_agent.py#L1768) | 1768 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001769](../../agents/web_agent.py#L1769) | 1769 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001770](../../agents/web_agent.py#L1770) | 1770 | `"                            \"provider\": \"bluesky_public_search\","` | — |
| [SRC-1AE03B9EC3-L001771](../../agents/web_agent.py#L1771) | 1771 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L001772](../../agents/web_agent.py#L1772) | 1772 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L001773](../../agents/web_agent.py#L1773) | 1773 | `"                                if row.get(\"provider\") == \"bluesky_public_search\""` | — |
| [SRC-1AE03B9EC3-L001774](../../agents/web_agent.py#L1774) | 1774 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L001775](../../agents/web_agent.py#L1775) | 1775 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001776](../../agents/web_agent.py#L1776) | 1776 | `"                            \"published_at\": _clean_text(post.get(\"indexedAt\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L001777](../../agents/web_agent.py#L1777) | 1777 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L001778](../../agents/web_agent.py#L1778) | 1778 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001779](../../agents/web_agent.py#L1779) | 1779 | `"                    warnings.append(f\"Bluesky public search unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L001780](../../agents/web_agent.py#L1780) | 1780 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L001781](../../agents/web_agent.py#L1781) | 1781 | `"                warnings.append(\"Bluesky public search unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L001782](../../agents/web_agent.py#L1782) | 1782 | `""` | — |
| [SRC-1AE03B9EC3-L001783](../../agents/web_agent.py#L1783) | 1783 | `"        if \"facebook\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L001784](../../agents/web_agent.py#L1784) | 1784 | `"            fb_token = os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001785](../../agents/web_agent.py#L1785) | 1785 | `"            page_ids = ["` | — |
| [SRC-1AE03B9EC3-L001786](../../agents/web_agent.py#L1786) | 1786 | `"                value.strip()"` | — |
| [SRC-1AE03B9EC3-L001787](../../agents/web_agent.py#L1787) | 1787 | `"                for value in os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").split(\",\")"` | — |
| [SRC-1AE03B9EC3-L001788](../../agents/web_agent.py#L1788) | 1788 | `"                if value.strip()"` | — |
| [SRC-1AE03B9EC3-L001789](../../agents/web_agent.py#L1789) | 1789 | `"            ][:5]"` | — |
| [SRC-1AE03B9EC3-L001790](../../agents/web_agent.py#L1790) | 1790 | `"            graph_version = os.getenv(\"META_GRAPH_VERSION\", \"v25.0\").strip()"` | — |
| [SRC-1AE03B9EC3-L001791](../../agents/web_agent.py#L1791) | 1791 | `"            if fb_token and page_ids:"` | — |
| [SRC-1AE03B9EC3-L001792](../../agents/web_agent.py#L1792) | 1792 | `"                # Scope direct reading to page IDs supplied by the operator and the"` | — |
| [SRC-1AE03B9EC3-L001793](../../agents/web_agent.py#L1793) | 1793 | `"                # permissions granted to this token. This is not global Facebook search."` | — |
| [SRC-1AE03B9EC3-L001794](../../agents/web_agent.py#L1794) | 1794 | `"                query_terms = {"` | — |
| [SRC-1AE03B9EC3-L001795](../../agents/web_agent.py#L1795) | 1795 | `"                    word.casefold()"` | — |
| [SRC-1AE03B9EC3-L001796](../../agents/web_agent.py#L1796) | 1796 | `"                    for word in re.findall(r\"[\\w\\u0600-\\u06FF]+\", query, flags=re.UNICODE)"` | — |
| [SRC-1AE03B9EC3-L001797](../../agents/web_agent.py#L1797) | 1797 | `"                    if len(word) >= 3"` | — |
| [SRC-1AE03B9EC3-L001798](../../agents/web_agent.py#L1798) | 1798 | `"                }"` | — |
| [SRC-1AE03B9EC3-L001799](../../agents/web_agent.py#L1799) | 1799 | `"                for page_id in page_ids:"` | — |
| [SRC-1AE03B9EC3-L001800](../../agents/web_agent.py#L1800) | 1800 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L001801](../../agents/web_agent.py#L1801) | 1801 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001802](../../agents/web_agent.py#L1802) | 1802 | `"                        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001803](../../agents/web_agent.py#L1803) | 1803 | `"                            f\"https://graph.facebook.com/{graph_version}/{page_id}/posts\","` | — |
| [SRC-1AE03B9EC3-L001804](../../agents/web_agent.py#L1804) | 1804 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L001805](../../agents/web_agent.py#L1805) | 1805 | `"                                \"fields\": ("` | — |
| [SRC-1AE03B9EC3-L001806](../../agents/web_agent.py#L1806) | 1806 | `"                                    \"message,permalink_url,created_time,\""` | — |
| [SRC-1AE03B9EC3-L001807](../../agents/web_agent.py#L1807) | 1807 | `"                                    \"comments.limit(10){message,created_time,like_count}\""` | — |
| [SRC-1AE03B9EC3-L001808](../../agents/web_agent.py#L1808) | 1808 | `"                                ),"` | — |
| [SRC-1AE03B9EC3-L001809](../../agents/web_agent.py#L1809) | 1809 | `"                                \"limit\": 10,"` | — |
| [SRC-1AE03B9EC3-L001810](../../agents/web_agent.py#L1810) | 1810 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L001811](../../agents/web_agent.py#L1811) | 1811 | `"                            headers={"` | — |
| [SRC-1AE03B9EC3-L001812](../../agents/web_agent.py#L1812) | 1812 | `"                                **headers,"` | — |
| [SRC-1AE03B9EC3-L001813](../../agents/web_agent.py#L1813) | 1813 | `"                                \"Authorization\": \"Bearer \" + fb_token,"` | — |
| [SRC-1AE03B9EC3-L001814](../../agents/web_agent.py#L1814) | 1814 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L001815](../../agents/web_agent.py#L1815) | 1815 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001816](../../agents/web_agent.py#L1816) | 1816 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001817](../../agents/web_agent.py#L1817) | 1817 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L001818](../../agents/web_agent.py#L1818) | 1818 | `"                        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001819](../../agents/web_agent.py#L1819) | 1819 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L001820](../../agents/web_agent.py#L1820) | 1820 | `"                                \"Facebook Pages API unavailable for one configured page \""` | — |
| [SRC-1AE03B9EC3-L001821](../../agents/web_agent.py#L1821) | 1821 | `"                                f\"(HTTP {response.status_code}); verify page ownership, token and permissions.\""` | — |
| [SRC-1AE03B9EC3-L001822](../../agents/web_agent.py#L1822) | 1822 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L001823](../../agents/web_agent.py#L1823) | 1823 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001824](../../agents/web_agent.py#L1824) | 1824 | `"                        posts = response.json().get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L001825](../../agents/web_agent.py#L1825) | 1825 | `"                        rank = 0"` | — |
| [SRC-1AE03B9EC3-L001826](../../agents/web_agent.py#L1826) | 1826 | `"                        for post in posts:"` | — |
| [SRC-1AE03B9EC3-L001827](../../agents/web_agent.py#L1827) | 1827 | `"                            message = _clean_text(post.get(\"message\") or \"\", 1400)"` | — |
| [SRC-1AE03B9EC3-L001828](../../agents/web_agent.py#L1828) | 1828 | `"                            comments = post.get(\"comments\", {}).get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L001829](../../agents/web_agent.py#L1829) | 1829 | `"                            comment_text = ["` | — |
| [SRC-1AE03B9EC3-L001830](../../agents/web_agent.py#L1830) | 1830 | `"                                _clean_text(item.get(\"message\") or \"\", 500)"` | — |
| [SRC-1AE03B9EC3-L001831](../../agents/web_agent.py#L1831) | 1831 | `"                                for item in comments"` | — |
| [SRC-1AE03B9EC3-L001832](../../agents/web_agent.py#L1832) | 1832 | `"                                if isinstance(item, dict) and item.get(\"message\")"` | — |
| [SRC-1AE03B9EC3-L001833](../../agents/web_agent.py#L1833) | 1833 | `"                            ]"` | — |
| [SRC-1AE03B9EC3-L001834](../../agents/web_agent.py#L1834) | 1834 | `"                            searchable = (message + \" \" + \" \".join(comment_text)).casefold()"` | — |
| [SRC-1AE03B9EC3-L001835](../../agents/web_agent.py#L1835) | 1835 | `"                            matched = sum(term in searchable for term in query_terms)"` | — |
| [SRC-1AE03B9EC3-L001836](../../agents/web_agent.py#L1836) | 1836 | `"                            if query_terms and matched == 0:"` | — |
| [SRC-1AE03B9EC3-L001837](../../agents/web_agent.py#L1837) | 1837 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L001838](../../agents/web_agent.py#L1838) | 1838 | `"                            permalink = _public_http_url(post.get(\"permalink_url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001839](../../agents/web_agent.py#L1839) | 1839 | `"                            if not permalink:"` | — |
| [SRC-1AE03B9EC3-L001840](../../agents/web_agent.py#L1840) | 1840 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L001841](../../agents/web_agent.py#L1841) | 1841 | `"                            rank += 1"` | — |
| [SRC-1AE03B9EC3-L001842](../../agents/web_agent.py#L1842) | 1842 | `"                            excerpt = message"` | — |
| [SRC-1AE03B9EC3-L001843](../../agents/web_agent.py#L1843) | 1843 | `"                            if comment_text:"` | — |
| [SRC-1AE03B9EC3-L001844](../../agents/web_agent.py#L1844) | 1844 | `"                                excerpt = ("` | — |
| [SRC-1AE03B9EC3-L001845](../../agents/web_agent.py#L1845) | 1845 | `"                                    excerpt + \"\\n\\nتعليقات عامة على المنشور:\\n\""` | — |
| [SRC-1AE03B9EC3-L001846](../../agents/web_agent.py#L1846) | 1846 | `"                                    if excerpt else \"تعليقات عامة على المنشور:\\n\""` | — |
| [SRC-1AE03B9EC3-L001847](../../agents/web_agent.py#L1847) | 1847 | `"                                ) + \"\\n— \".join(comment_text)"` | — |
| [SRC-1AE03B9EC3-L001848](../../agents/web_agent.py#L1848) | 1848 | `"                            results.append({"` | — |
| [SRC-1AE03B9EC3-L001849](../../agents/web_agent.py#L1849) | 1849 | `"                                \"title\": _clean_text(message or \"Facebook public Page post\", 300),"` | — |
| [SRC-1AE03B9EC3-L001850](../../agents/web_agent.py#L1850) | 1850 | `"                                \"url\": permalink,"` | — |
| [SRC-1AE03B9EC3-L001851](../../agents/web_agent.py#L1851) | 1851 | `"                                \"snippet\": _clean_text(excerpt, 1800),"` | — |
| [SRC-1AE03B9EC3-L001852](../../agents/web_agent.py#L1852) | 1852 | `"                                \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001853](../../agents/web_agent.py#L1853) | 1853 | `"                                \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001854](../../agents/web_agent.py#L1854) | 1854 | `"                                \"provider\": \"facebook_pages_api\","` | — |
| [SRC-1AE03B9EC3-L001855](../../agents/web_agent.py#L1855) | 1855 | `"                                \"provider_rank\": rank,"` | — |
| [SRC-1AE03B9EC3-L001856](../../agents/web_agent.py#L1856) | 1856 | `"                                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001857](../../agents/web_agent.py#L1857) | 1857 | `"                                \"published_at\": _clean_text(post.get(\"created_time\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L001858](../../agents/web_agent.py#L1858) | 1858 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L001859](../../agents/web_agent.py#L1859) | 1859 | `"                            if rank >= 10:"` | — |
| [SRC-1AE03B9EC3-L001860](../../agents/web_agent.py#L1860) | 1860 | `"                                break"` | — |
| [SRC-1AE03B9EC3-L001861](../../agents/web_agent.py#L1861) | 1861 | `"                    except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L001862](../../agents/web_agent.py#L1862) | 1862 | `"                        warnings.append(\"Facebook Pages API failed for one configured page.\")"` | — |
| [SRC-1AE03B9EC3-L001863](../../agents/web_agent.py#L1863) | 1863 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L001864](../../agents/web_agent.py#L1864) | 1864 | `"                warnings.append("` | — |
| [SRC-1AE03B9EC3-L001865](../../agents/web_agent.py#L1865) | 1865 | `"                    \"Facebook direct API is not configured for specific pages; indexed public Facebook pages are still searched.\""` | — |
| [SRC-1AE03B9EC3-L001866](../../agents/web_agent.py#L1866) | 1866 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001867](../../agents/web_agent.py#L1867) | 1867 | `""` | — |
| [SRC-1AE03B9EC3-L001868](../../agents/web_agent.py#L1868) | 1868 | `"        if \"instagram\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L001869](../../agents/web_agent.py#L1869) | 1869 | `"            ig_user_id = os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001870](../../agents/web_agent.py#L1870) | 1870 | `"            ig_token = os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001871](../../agents/web_agent.py#L1871) | 1871 | `"            graph_version = os.getenv(\"META_GRAPH_VERSION\", \"v25.0\").strip()"` | — |
| [SRC-1AE03B9EC3-L001872](../../agents/web_agent.py#L1872) | 1872 | `"            if ig_user_id and ig_token:"` | — |
| [SRC-1AE03B9EC3-L001873](../../agents/web_agent.py#L1873) | 1873 | `"                # The official Hashtag Search API returns public hashtag media only."` | — |
| [SRC-1AE03B9EC3-L001874](../../agents/web_agent.py#L1874) | 1874 | `"                # It does not search every Instagram post or bypass private accounts."` | — |
| [SRC-1AE03B9EC3-L001875](../../agents/web_agent.py#L1875) | 1875 | `"                hashtags = re.findall(r\"#([\\w\\u0600-\\u06FF]+)\", query, flags=re.UNICODE)"` | — |
| [SRC-1AE03B9EC3-L001876](../../agents/web_agent.py#L1876) | 1876 | `"                if not hashtags:"` | — |
| [SRC-1AE03B9EC3-L001877](../../agents/web_agent.py#L1877) | 1877 | `"                    words = re.findall(r\"[\\w\\u0600-\\u06FF]+\", query, flags=re.UNICODE)"` | — |
| [SRC-1AE03B9EC3-L001878](../../agents/web_agent.py#L1878) | 1878 | `"                    stopwords = {"` | — |
| [SRC-1AE03B9EC3-L001879](../../agents/web_agent.py#L1879) | 1879 | `"                        \"ابحث\", \"بحث\", \"عن\", \"في\", \"على\", \"من\", \"مع\", \"تجارب\","` | — |
| [SRC-1AE03B9EC3-L001880](../../agents/web_agent.py#L1880) | 1880 | `"                        \"الناس\", \"العملاء\", \"منشورات\", \"تعليقات\", \"مواقع\", \"التواصل\","` | — |
| [SRC-1AE03B9EC3-L001881](../../agents/web_agent.py#L1881) | 1881 | `"                        \"الاجتماعي\", \"public\", \"search\", \"social\", \"media\", \"posts\","` | — |
| [SRC-1AE03B9EC3-L001882](../../agents/web_agent.py#L1882) | 1882 | `"                        \"find\", \"about\", \"with\", \"the\", \"and\", \"for\","` | — |
| [SRC-1AE03B9EC3-L001883](../../agents/web_agent.py#L1883) | 1883 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L001884](../../agents/web_agent.py#L1884) | 1884 | `"                    useful = ["` | — |
| [SRC-1AE03B9EC3-L001885](../../agents/web_agent.py#L1885) | 1885 | `"                        word for word in words"` | — |
| [SRC-1AE03B9EC3-L001886](../../agents/web_agent.py#L1886) | 1886 | `"                        if len(word) >= 3 and word.casefold() not in stopwords"` | — |
| [SRC-1AE03B9EC3-L001887](../../agents/web_agent.py#L1887) | 1887 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L001888](../../agents/web_agent.py#L1888) | 1888 | `"                    if useful:"` | — |
| [SRC-1AE03B9EC3-L001889](../../agents/web_agent.py#L1889) | 1889 | `"                        hashtags = [\"_\".join(useful[:3])]"` | — |
| [SRC-1AE03B9EC3-L001890](../../agents/web_agent.py#L1890) | 1890 | `"                # Meta limits unique hashtag searches over a rolling week; keep this"` | — |
| [SRC-1AE03B9EC3-L001891](../../agents/web_agent.py#L1891) | 1891 | `"                # connector conservative and use no more than two tags per user request."` | — |
| [SRC-1AE03B9EC3-L001892](../../agents/web_agent.py#L1892) | 1892 | `"                for hashtag in list(dict.fromkeys(hashtags))[:1]:"` | — |
| [SRC-1AE03B9EC3-L001893](../../agents/web_agent.py#L1893) | 1893 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L001894](../../agents/web_agent.py#L1894) | 1894 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001895](../../agents/web_agent.py#L1895) | 1895 | `"                        search_response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001896](../../agents/web_agent.py#L1896) | 1896 | `"                            f\"https://graph.facebook.com/{graph_version}/ig_hashtag_search\","` | — |
| [SRC-1AE03B9EC3-L001897](../../agents/web_agent.py#L1897) | 1897 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L001898](../../agents/web_agent.py#L1898) | 1898 | `"                                \"user_id\": ig_user_id,"` | — |
| [SRC-1AE03B9EC3-L001899](../../agents/web_agent.py#L1899) | 1899 | `"                                \"q\": hashtag,"` | — |
| [SRC-1AE03B9EC3-L001900](../../agents/web_agent.py#L1900) | 1900 | `"                                \"fields\": \"id,name\","` | — |
| [SRC-1AE03B9EC3-L001901](../../agents/web_agent.py#L1901) | 1901 | `"                                \"access_token\": ig_token,"` | — |
| [SRC-1AE03B9EC3-L001902](../../agents/web_agent.py#L1902) | 1902 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L001903](../../agents/web_agent.py#L1903) | 1903 | `"                            headers=headers,"` | — |
| [SRC-1AE03B9EC3-L001904](../../agents/web_agent.py#L1904) | 1904 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001905](../../agents/web_agent.py#L1905) | 1905 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001906](../../agents/web_agent.py#L1906) | 1906 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L001907](../../agents/web_agent.py#L1907) | 1907 | `"                        if search_response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001908](../../agents/web_agent.py#L1908) | 1908 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L001909](../../agents/web_agent.py#L1909) | 1909 | `"                                \"Instagram Graph API hashtag search unavailable \""` | — |
| [SRC-1AE03B9EC3-L001910](../../agents/web_agent.py#L1910) | 1910 | `"                                f\"(HTTP {search_response.status_code}); check permissions and access.\""` | — |
| [SRC-1AE03B9EC3-L001911](../../agents/web_agent.py#L1911) | 1911 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L001912](../../agents/web_agent.py#L1912) | 1912 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001913](../../agents/web_agent.py#L1913) | 1913 | `"                        tag_data = search_response.json().get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L001914](../../agents/web_agent.py#L1914) | 1914 | `"                        if not tag_data:"` | — |
| [SRC-1AE03B9EC3-L001915](../../agents/web_agent.py#L1915) | 1915 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001916](../../agents/web_agent.py#L1916) | 1916 | `"                        hashtag_id = tag_data[0].get(\"id\")"` | — |
| [SRC-1AE03B9EC3-L001917](../../agents/web_agent.py#L1917) | 1917 | `"                        if not hashtag_id:"` | — |
| [SRC-1AE03B9EC3-L001918](../../agents/web_agent.py#L1918) | 1918 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001919](../../agents/web_agent.py#L1919) | 1919 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001920](../../agents/web_agent.py#L1920) | 1920 | `"                        media_response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001921](../../agents/web_agent.py#L1921) | 1921 | `"                            f\"https://graph.facebook.com/{graph_version}/{hashtag_id}/recent_media\","` | — |
| [SRC-1AE03B9EC3-L001922](../../agents/web_agent.py#L1922) | 1922 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L001923](../../agents/web_agent.py#L1923) | 1923 | `"                                \"user_id\": ig_user_id,"` | — |
| [SRC-1AE03B9EC3-L001924](../../agents/web_agent.py#L1924) | 1924 | `"                                \"fields\": \"id,caption,media_type,permalink,timestamp,like_count,comments_count\","` | — |
| [SRC-1AE03B9EC3-L001925](../../agents/web_agent.py#L1925) | 1925 | `"                                \"limit\": 20,"` | — |
| [SRC-1AE03B9EC3-L001926](../../agents/web_agent.py#L1926) | 1926 | `"                                \"access_token\": ig_token,"` | — |
| [SRC-1AE03B9EC3-L001927](../../agents/web_agent.py#L1927) | 1927 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L001928](../../agents/web_agent.py#L1928) | 1928 | `"                            headers=headers,"` | — |
| [SRC-1AE03B9EC3-L001929](../../agents/web_agent.py#L1929) | 1929 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001930](../../agents/web_agent.py#L1930) | 1930 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001931](../../agents/web_agent.py#L1931) | 1931 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L001932](../../agents/web_agent.py#L1932) | 1932 | `"                        if media_response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001933](../../agents/web_agent.py#L1933) | 1933 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L001934](../../agents/web_agent.py#L1934) | 1934 | `"                                \"Instagram public hashtag media unavailable \""` | — |
| [SRC-1AE03B9EC3-L001935](../../agents/web_agent.py#L1935) | 1935 | `"                                f\"(HTTP {media_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L001936](../../agents/web_agent.py#L1936) | 1936 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L001937](../../agents/web_agent.py#L1937) | 1937 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001938](../../agents/web_agent.py#L1938) | 1938 | `"                        items = media_response.json().get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L001939](../../agents/web_agent.py#L1939) | 1939 | `"                        for item in items:"` | — |
| [SRC-1AE03B9EC3-L001940](../../agents/web_agent.py#L1940) | 1940 | `"                            url = _public_http_url(item.get(\"permalink\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001941](../../agents/web_agent.py#L1941) | 1941 | `"                            if not url:"` | — |
| [SRC-1AE03B9EC3-L001942](../../agents/web_agent.py#L1942) | 1942 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L001943](../../agents/web_agent.py#L1943) | 1943 | `"                            metrics = []"` | — |
| [SRC-1AE03B9EC3-L001944](../../agents/web_agent.py#L1944) | 1944 | `"                            if item.get(\"like_count\") is not None:"` | — |
| [SRC-1AE03B9EC3-L001945](../../agents/web_agent.py#L1945) | 1945 | `"                                metrics.append(\"likes=\" + str(item[\"like_count\"]))"` | — |
| [SRC-1AE03B9EC3-L001946](../../agents/web_agent.py#L1946) | 1946 | `"                            if item.get(\"comments_count\") is not None:"` | — |
| [SRC-1AE03B9EC3-L001947](../../agents/web_agent.py#L1947) | 1947 | `"                                metrics.append(\"comments=\" + str(item[\"comments_count\"]))"` | — |
| [SRC-1AE03B9EC3-L001948](../../agents/web_agent.py#L1948) | 1948 | `"                            caption = _clean_text(item.get(\"caption\") or \"\", 1200)"` | — |
| [SRC-1AE03B9EC3-L001949](../../agents/web_agent.py#L1949) | 1949 | `"                            if metrics:"` | — |
| [SRC-1AE03B9EC3-L001950](../../agents/web_agent.py#L1950) | 1950 | `"                                caption = (caption + \" \| \" if caption else \"\") + \", \".join(metrics)"` | — |
| [SRC-1AE03B9EC3-L001951](../../agents/web_agent.py#L1951) | 1951 | `"                            results.append({"` | — |
| [SRC-1AE03B9EC3-L001952](../../agents/web_agent.py#L1952) | 1952 | `"                                \"title\": \"Instagram public hashtag: #\" + hashtag,"` | — |
| [SRC-1AE03B9EC3-L001953](../../agents/web_agent.py#L1953) | 1953 | `"                                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001954](../../agents/web_agent.py#L1954) | 1954 | `"                                \"snippet\": caption,"` | — |
| [SRC-1AE03B9EC3-L001955](../../agents/web_agent.py#L1955) | 1955 | `"                                \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001956](../../agents/web_agent.py#L1956) | 1956 | `"                                \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001957](../../agents/web_agent.py#L1957) | 1957 | `"                                \"provider\": \"instagram_graph_api\","` | — |
| [SRC-1AE03B9EC3-L001958](../../agents/web_agent.py#L1958) | 1958 | `"                                \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L001959](../../agents/web_agent.py#L1959) | 1959 | `"                                    row for row in results"` | — |
| [SRC-1AE03B9EC3-L001960](../../agents/web_agent.py#L1960) | 1960 | `"                                    if row.get(\"provider\") == \"instagram_graph_api\""` | — |
| [SRC-1AE03B9EC3-L001961](../../agents/web_agent.py#L1961) | 1961 | `"                                ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L001962](../../agents/web_agent.py#L1962) | 1962 | `"                                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001963](../../agents/web_agent.py#L1963) | 1963 | `"                                \"published_at\": _clean_text(item.get(\"timestamp\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L001964](../../agents/web_agent.py#L1964) | 1964 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L001965](../../agents/web_agent.py#L1965) | 1965 | `"                    except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L001966](../../agents/web_agent.py#L1966) | 1966 | `"                        warnings.append(\"Instagram Graph API search failed for a requested hashtag.\")"` | — |
| [SRC-1AE03B9EC3-L001967](../../agents/web_agent.py#L1967) | 1967 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L001968](../../agents/web_agent.py#L1968) | 1968 | `"                warnings.append("` | — |
| [SRC-1AE03B9EC3-L001969](../../agents/web_agent.py#L1969) | 1969 | `"                    \"Instagram direct API is not configured; indexed public Instagram pages are still searched.\""` | — |
| [SRC-1AE03B9EC3-L001970](../../agents/web_agent.py#L1970) | 1970 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001971](../../agents/web_agent.py#L1971) | 1971 | `""` | — |
| [SRC-1AE03B9EC3-L001972](../../agents/web_agent.py#L1972) | 1972 | `"        if \"x\" in platforms and os.getenv(\"X_BEARER_TOKEN\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001973](../../agents/web_agent.py#L1973) | 1973 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001974](../../agents/web_agent.py#L1974) | 1974 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001975](../../agents/web_agent.py#L1975) | 1975 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001976](../../agents/web_agent.py#L1976) | 1976 | `"                    \"https://api.x.com/2/tweets/search/recent\","` | — |
| [SRC-1AE03B9EC3-L001977](../../agents/web_agent.py#L1977) | 1977 | `"                    params={"` | — |
| [SRC-1AE03B9EC3-L001978](../../agents/web_agent.py#L1978) | 1978 | `"                        \"query\": query + \" -is:retweet\","` | — |
| [SRC-1AE03B9EC3-L001979](../../agents/web_agent.py#L1979) | 1979 | `"                        \"max_results\": 10,"` | — |
| [SRC-1AE03B9EC3-L001980](../../agents/web_agent.py#L1980) | 1980 | `"                        \"tweet.fields\": \"created_at,lang,public_metrics,author_id\","` | — |
| [SRC-1AE03B9EC3-L001981](../../agents/web_agent.py#L1981) | 1981 | `"                        \"expansions\": \"author_id\","` | — |
| [SRC-1AE03B9EC3-L001982](../../agents/web_agent.py#L1982) | 1982 | `"                        \"user.fields\": \"name,username\","` | — |
| [SRC-1AE03B9EC3-L001983](../../agents/web_agent.py#L1983) | 1983 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L001984](../../agents/web_agent.py#L1984) | 1984 | `"                    headers={"` | — |
| [SRC-1AE03B9EC3-L001985](../../agents/web_agent.py#L1985) | 1985 | `"                        **headers,"` | — |
| [SRC-1AE03B9EC3-L001986](../../agents/web_agent.py#L1986) | 1986 | `"                        \"Authorization\": \"Bearer \" + os.getenv(\"X_BEARER_TOKEN\", \"\").strip(),"` | — |
| [SRC-1AE03B9EC3-L001987](../../agents/web_agent.py#L1987) | 1987 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L001988](../../agents/web_agent.py#L1988) | 1988 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001989](../../agents/web_agent.py#L1989) | 1989 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001990](../../agents/web_agent.py#L1990) | 1990 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001991](../../agents/web_agent.py#L1991) | 1991 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001992](../../agents/web_agent.py#L1992) | 1992 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L001993](../../agents/web_agent.py#L1993) | 1993 | `"                    authors = {"` | — |
| [SRC-1AE03B9EC3-L001994](../../agents/web_agent.py#L1994) | 1994 | `"                        user.get(\"id\"): user"` | — |
| [SRC-1AE03B9EC3-L001995](../../agents/web_agent.py#L1995) | 1995 | `"                        for user in data.get(\"includes\", {}).get(\"users\", [])"` | — |
| [SRC-1AE03B9EC3-L001996](../../agents/web_agent.py#L1996) | 1996 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L001997](../../agents/web_agent.py#L1997) | 1997 | `"                    for item in data.get(\"data\", []):"` | — |
| [SRC-1AE03B9EC3-L001998](../../agents/web_agent.py#L1998) | 1998 | `"                        author = authors.get(item.get(\"author_id\"), {})"` | — |
| [SRC-1AE03B9EC3-L001999](../../agents/web_agent.py#L1999) | 1999 | `"                        username = author.get(\"username\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002000](../../agents/web_agent.py#L2000) | 2000 | `"                        post_id = item.get(\"id\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002001](../../agents/web_agent.py#L2001) | 2001 | `"                        if not username or not post_id:"` | — |
| [SRC-1AE03B9EC3-L002002](../../agents/web_agent.py#L2002) | 2002 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002003](../../agents/web_agent.py#L2003) | 2003 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L002004](../../agents/web_agent.py#L2004) | 2004 | `"                            \"title\": _clean_text(author.get(\"name\") or username, 300),"` | — |
| [SRC-1AE03B9EC3-L002005](../../agents/web_agent.py#L2005) | 2005 | `"                            \"url\": f\"https://x.com/{username}/status/{post_id}\","` | — |
| [SRC-1AE03B9EC3-L002006](../../agents/web_agent.py#L2006) | 2006 | `"                            \"snippet\": _clean_text(item.get(\"text\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L002007](../../agents/web_agent.py#L2007) | 2007 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002008](../../agents/web_agent.py#L2008) | 2008 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002009](../../agents/web_agent.py#L2009) | 2009 | `"                            \"provider\": \"x_official_api\","` | — |
| [SRC-1AE03B9EC3-L002010](../../agents/web_agent.py#L2010) | 2010 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002011](../../agents/web_agent.py#L2011) | 2011 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L002012](../../agents/web_agent.py#L2012) | 2012 | `"                                if row.get(\"provider\") == \"x_official_api\""` | — |
| [SRC-1AE03B9EC3-L002013](../../agents/web_agent.py#L2013) | 2013 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002014](../../agents/web_agent.py#L2014) | 2014 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002015](../../agents/web_agent.py#L2015) | 2015 | `"                            \"published_at\": _clean_text(item.get(\"created_at\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002016](../../agents/web_agent.py#L2016) | 2016 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L002017](../../agents/web_agent.py#L2017) | 2017 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002018](../../agents/web_agent.py#L2018) | 2018 | `"                    warnings.append(f\"X API unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L002019](../../agents/web_agent.py#L2019) | 2019 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002020](../../agents/web_agent.py#L2020) | 2020 | `"                warnings.append(\"X API unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L002021](../../agents/web_agent.py#L2021) | 2021 | `"        elif \"x\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002022](../../agents/web_agent.py#L2022) | 2022 | `"            warnings.append(\"X direct API is not configured; indexed public X pages are still searched.\")"` | — |
| [SRC-1AE03B9EC3-L002023](../../agents/web_agent.py#L2023) | 2023 | `""` | — |
| [SRC-1AE03B9EC3-L002024](../../agents/web_agent.py#L2024) | 2024 | `"        if \"youtube\" in platforms and os.getenv(\"YOUTUBE_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L002025](../../agents/web_agent.py#L2025) | 2025 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002026](../../agents/web_agent.py#L2026) | 2026 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L002027](../../agents/web_agent.py#L2027) | 2027 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L002028](../../agents/web_agent.py#L2028) | 2028 | `"                    \"https://www.googleapis.com/youtube/v3/search\","` | — |
| [SRC-1AE03B9EC3-L002029](../../agents/web_agent.py#L2029) | 2029 | `"                    params={"` | — |
| [SRC-1AE03B9EC3-L002030](../../agents/web_agent.py#L2030) | 2030 | `"                        \"part\": \"snippet\","` | — |
| [SRC-1AE03B9EC3-L002031](../../agents/web_agent.py#L2031) | 2031 | `"                        \"q\": query,"` | — |
| [SRC-1AE03B9EC3-L002032](../../agents/web_agent.py#L2032) | 2032 | `"                        \"type\": \"video\","` | — |
| [SRC-1AE03B9EC3-L002033](../../agents/web_agent.py#L2033) | 2033 | `"                        \"maxResults\": 8,"` | — |
| [SRC-1AE03B9EC3-L002034](../../agents/web_agent.py#L2034) | 2034 | `"                        \"key\": os.getenv(\"YOUTUBE_API_KEY\", \"\").strip(),"` | — |
| [SRC-1AE03B9EC3-L002035](../../agents/web_agent.py#L2035) | 2035 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L002036](../../agents/web_agent.py#L2036) | 2036 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002037](../../agents/web_agent.py#L2037) | 2037 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L002038](../../agents/web_agent.py#L2038) | 2038 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002039](../../agents/web_agent.py#L2039) | 2039 | `"                )"` | — |
| [SRC-1AE03B9EC3-L002040](../../agents/web_agent.py#L2040) | 2040 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L002041](../../agents/web_agent.py#L2041) | 2041 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L002042](../../agents/web_agent.py#L2042) | 2042 | `"                    for item in data.get(\"items\", []):"` | — |
| [SRC-1AE03B9EC3-L002043](../../agents/web_agent.py#L2043) | 2043 | `"                        video_id = item.get(\"id\", {}).get(\"videoId\")"` | — |
| [SRC-1AE03B9EC3-L002044](../../agents/web_agent.py#L2044) | 2044 | `"                        snippet = item.get(\"snippet\", {})"` | — |
| [SRC-1AE03B9EC3-L002045](../../agents/web_agent.py#L2045) | 2045 | `"                        if not video_id:"` | — |
| [SRC-1AE03B9EC3-L002046](../../agents/web_agent.py#L2046) | 2046 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002047](../../agents/web_agent.py#L2047) | 2047 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L002048](../../agents/web_agent.py#L2048) | 2048 | `"                            \"title\": _clean_text(snippet.get(\"title\") or \"\", 300),"` | — |
| [SRC-1AE03B9EC3-L002049](../../agents/web_agent.py#L2049) | 2049 | `"                            \"url\": f\"https://www.youtube.com/watch?v={video_id}\","` | — |
| [SRC-1AE03B9EC3-L002050](../../agents/web_agent.py#L2050) | 2050 | `"                            \"snippet\": _clean_text(snippet.get(\"description\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L002051](../../agents/web_agent.py#L2051) | 2051 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L002052](../../agents/web_agent.py#L2052) | 2052 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L002053](../../agents/web_agent.py#L2053) | 2053 | `"                            \"provider\": \"youtube_data_api\","` | — |
| [SRC-1AE03B9EC3-L002054](../../agents/web_agent.py#L2054) | 2054 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L002055](../../agents/web_agent.py#L2055) | 2055 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L002056](../../agents/web_agent.py#L2056) | 2056 | `"                                if row.get(\"provider\") == \"youtube_data_api\""` | — |
| [SRC-1AE03B9EC3-L002057](../../agents/web_agent.py#L2057) | 2057 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L002058](../../agents/web_agent.py#L2058) | 2058 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002059](../../agents/web_agent.py#L2059) | 2059 | `"                            \"published_at\": _clean_text(snippet.get(\"publishedAt\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L002060](../../agents/web_agent.py#L2060) | 2060 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L002061](../../agents/web_agent.py#L2061) | 2061 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002062](../../agents/web_agent.py#L2062) | 2062 | `"                    warnings.append(f\"YouTube Data API unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L002063](../../agents/web_agent.py#L2063) | 2063 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L002064](../../agents/web_agent.py#L2064) | 2064 | `"                warnings.append(\"YouTube Data API unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L002065](../../agents/web_agent.py#L2065) | 2065 | `"        elif \"youtube\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L002066](../../agents/web_agent.py#L2066) | 2066 | `"            warnings.append(\"YouTube direct API is not configured; indexed public YouTube pages are still searched.\")"` | — |
| [SRC-1AE03B9EC3-L002067](../../agents/web_agent.py#L2067) | 2067 | `""` | — |
| [SRC-1AE03B9EC3-L002068](../../agents/web_agent.py#L2068) | 2068 | `"        return results, warnings"` | — |
| [SRC-1AE03B9EC3-L002069](../../agents/web_agent.py#L2069) | 2069 | `""` | — |
| [SRC-1AE03B9EC3-L002070](../../agents/web_agent.py#L2070) | 2070 | `"    def _fetch_page(self, url: str) -> tuple[str, str]:"` | — |
| [SRC-1AE03B9EC3-L002071](../../agents/web_agent.py#L2071) | 2071 | `"        \"\"\"Fetch a public page with bounded redirects and an inspectable extraction outcome.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002072](../../agents/web_agent.py#L2072) | 2072 | `"        def result("` | — |
| [SRC-1AE03B9EC3-L002073](../../agents/web_agent.py#L2073) | 2073 | `"            title: str = \"\","` | — |
| [SRC-1AE03B9EC3-L002074](../../agents/web_agent.py#L2074) | 2074 | `"            page_text: str = \"\","` | — |
| [SRC-1AE03B9EC3-L002075](../../agents/web_agent.py#L2075) | 2075 | `"            status: str = \"unknown\","` | — |
| [SRC-1AE03B9EC3-L002076](../../agents/web_agent.py#L2076) | 2076 | `"            error_class: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L002077](../../agents/web_agent.py#L2077) | 2077 | `"        ) -> PageFetchResult:"` | — |
| [SRC-1AE03B9EC3-L002078](../../agents/web_agent.py#L2078) | 2078 | `"            return PageFetchResult(title, page_text, status, error_class)"` | — |
| [SRC-1AE03B9EC3-L002079](../../agents/web_agent.py#L2079) | 2079 | `""` | — |
| [SRC-1AE03B9EC3-L002080](../../agents/web_agent.py#L2080) | 2080 | `"        current_url = _public_http_url(url)"` | — |
| [SRC-1AE03B9EC3-L002081](../../agents/web_agent.py#L2081) | 2081 | `"        if not current_url:"` | — |
| [SRC-1AE03B9EC3-L002082](../../agents/web_agent.py#L2082) | 2082 | `"            return result(status=\"rejected_url\", error_class=\"PublicUrlRejected\")"` | — |
| [SRC-1AE03B9EC3-L002083](../../agents/web_agent.py#L2083) | 2083 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L002084](../../agents/web_agent.py#L2084) | 2084 | `"        if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L002085](../../agents/web_agent.py#L2085) | 2085 | `"            budget.reserve(\"page_fetches\")"` | — |
| [SRC-1AE03B9EC3-L002086](../../agents/web_agent.py#L2086) | 2086 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002087](../../agents/web_agent.py#L2087) | 2087 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L002088](../../agents/web_agent.py#L2088) | 2088 | `"            from bs4 import BeautifulSoup"` | — |
| [SRC-1AE03B9EC3-L002089](../../agents/web_agent.py#L2089) | 2089 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L002090](../../agents/web_agent.py#L2090) | 2090 | `"            raise AgentDependencyError("` | — |
| [SRC-1AE03B9EC3-L002091](../../agents/web_agent.py#L2091) | 2091 | `"                \"حزم استخراج الصفحات غير مثبتة. نفّذ: python -m pip install -e .\""` | — |
| [SRC-1AE03B9EC3-L002092](../../agents/web_agent.py#L2092) | 2092 | `"            ) from exc"` | — |
| [SRC-1AE03B9EC3-L002093](../../agents/web_agent.py#L2093) | 2093 | `""` | — |
| [SRC-1AE03B9EC3-L002094](../../agents/web_agent.py#L2094) | 2094 | `"        headers = {"` | — |
| [SRC-1AE03B9EC3-L002095](../../agents/web_agent.py#L2095) | 2095 | `"            \"User-Agent\": \"OmaraiResearchBot/1.1 (public page research; no login)\","` | — |
| [SRC-1AE03B9EC3-L002096](../../agents/web_agent.py#L2096) | 2096 | `"            \"Accept\": \"text/html,application/xhtml+xml,text/plain;q=0.8\","` | — |
| [SRC-1AE03B9EC3-L002097](../../agents/web_agent.py#L2097) | 2097 | `"        }"` | — |
| [SRC-1AE03B9EC3-L002098](../../agents/web_agent.py#L2098) | 2098 | `"        media_type = \"\""` | — |
| [SRC-1AE03B9EC3-L002099](../../agents/web_agent.py#L2099) | 2099 | `"        html = \"\""` | — |
| [SRC-1AE03B9EC3-L002100](../../agents/web_agent.py#L2100) | 2100 | `"        bytes_truncated = False"` | — |
| [SRC-1AE03B9EC3-L002101](../../agents/web_agent.py#L2101) | 2101 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002102](../../agents/web_agent.py#L2102) | 2102 | `"            with httpx.Client("` | — |
| [SRC-1AE03B9EC3-L002103](../../agents/web_agent.py#L2103) | 2103 | `"                timeout=self._effective_timeout(8.0),"` | — |
| [SRC-1AE03B9EC3-L002104](../../agents/web_agent.py#L2104) | 2104 | `"                follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002105](../../agents/web_agent.py#L2105) | 2105 | `"                headers=headers,"` | — |
| [SRC-1AE03B9EC3-L002106](../../agents/web_agent.py#L2106) | 2106 | `"                verify=True,"` | — |
| [SRC-1AE03B9EC3-L002107](../../agents/web_agent.py#L2107) | 2107 | `"                trust_env=False,"` | — |
| [SRC-1AE03B9EC3-L002108](../../agents/web_agent.py#L2108) | 2108 | `"            ) as client:"` | — |
| [SRC-1AE03B9EC3-L002109](../../agents/web_agent.py#L2109) | 2109 | `"                for redirect_number in range(4):"` | — |
| [SRC-1AE03B9EC3-L002110](../../agents/web_agent.py#L2110) | 2110 | `"                    parsed = urllib.parse.urlparse(current_url)"` | — |
| [SRC-1AE03B9EC3-L002111](../../agents/web_agent.py#L2111) | 2111 | `"                    host = parsed.hostname or \"\""` | — |
| [SRC-1AE03B9EC3-L002112](../../agents/web_agent.py#L2112) | 2112 | `"                    # Resolve and pin a public IP. Do not let the HTTP client resolve"` | — |
| [SRC-1AE03B9EC3-L002113](../../agents/web_agent.py#L2113) | 2113 | `"                    # the original hostname a second time."` | — |
| [SRC-1AE03B9EC3-L002114](../../agents/web_agent.py#L2114) | 2114 | `"                    public_ips = _public_ip_literals(host)"` | — |
| [SRC-1AE03B9EC3-L002115](../../agents/web_agent.py#L2115) | 2115 | `"                    if not public_ips:"` | — |
| [SRC-1AE03B9EC3-L002116](../../agents/web_agent.py#L2116) | 2116 | `"                        return result(status=\"blocked_or_unresolved_host\", error_class=\"HostResolutionOrSSRFCheck\")"` | — |
| [SRC-1AE03B9EC3-L002117](../../agents/web_agent.py#L2117) | 2117 | `"                    connect_url = _pinned_connect_url(current_url, public_ips[0])"` | — |
| [SRC-1AE03B9EC3-L002118](../../agents/web_agent.py#L2118) | 2118 | `"                    if not connect_url:"` | — |
| [SRC-1AE03B9EC3-L002119](../../agents/web_agent.py#L2119) | 2119 | `"                        return result(status=\"blocked_connection_target\", error_class=\"PinnedTargetRejected\")"` | — |
| [SRC-1AE03B9EC3-L002120](../../agents/web_agent.py#L2120) | 2120 | `"                    request_headers = {\"Host\": host}"` | — |
| [SRC-1AE03B9EC3-L002121](../../agents/web_agent.py#L2121) | 2121 | `"                    extensions = {\"sni_hostname\": host} if parsed.scheme == \"https\" else {}"` | — |
| [SRC-1AE03B9EC3-L002122](../../agents/web_agent.py#L2122) | 2122 | `"                    with client.stream("` | — |
| [SRC-1AE03B9EC3-L002123](../../agents/web_agent.py#L2123) | 2123 | `"                        \"GET\","` | — |
| [SRC-1AE03B9EC3-L002124](../../agents/web_agent.py#L2124) | 2124 | `"                        connect_url,"` | — |
| [SRC-1AE03B9EC3-L002125](../../agents/web_agent.py#L2125) | 2125 | `"                        headers=request_headers,"` | — |
| [SRC-1AE03B9EC3-L002126](../../agents/web_agent.py#L2126) | 2126 | `"                        extensions=extensions,"` | — |
| [SRC-1AE03B9EC3-L002127](../../agents/web_agent.py#L2127) | 2127 | `"                    ) as response:"` | — |
| [SRC-1AE03B9EC3-L002128](../../agents/web_agent.py#L2128) | 2128 | `"                        if response.status_code in {301, 302, 303, 307, 308}:"` | — |
| [SRC-1AE03B9EC3-L002129](../../agents/web_agent.py#L2129) | 2129 | `"                            location = response.headers.get(\"location\", \"\")"` | — |
| [SRC-1AE03B9EC3-L002130](../../agents/web_agent.py#L2130) | 2130 | `"                            if not location or redirect_number >= 3:"` | — |
| [SRC-1AE03B9EC3-L002131](../../agents/web_agent.py#L2131) | 2131 | `"                                return result(status=\"redirect_failed\", error_class=\"RedirectLimitOrMissingLocation\")"` | — |
| [SRC-1AE03B9EC3-L002132](../../agents/web_agent.py#L2132) | 2132 | `"                            target = _public_http_url("` | — |
| [SRC-1AE03B9EC3-L002133](../../agents/web_agent.py#L2133) | 2133 | `"                                urllib.parse.urljoin(current_url, location)"` | — |
| [SRC-1AE03B9EC3-L002134](../../agents/web_agent.py#L2134) | 2134 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L002135](../../agents/web_agent.py#L2135) | 2135 | `"                            if not target:"` | — |
| [SRC-1AE03B9EC3-L002136](../../agents/web_agent.py#L2136) | 2136 | `"                                return result(status=\"redirect_rejected\", error_class=\"RedirectTargetRejected\")"` | — |
| [SRC-1AE03B9EC3-L002137](../../agents/web_agent.py#L2137) | 2137 | `"                            current_url = target"` | — |
| [SRC-1AE03B9EC3-L002138](../../agents/web_agent.py#L2138) | 2138 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L002139](../../agents/web_agent.py#L2139) | 2139 | `"                        if response.status_code < 200 or response.status_code >= 300:"` | — |
| [SRC-1AE03B9EC3-L002140](../../agents/web_agent.py#L2140) | 2140 | `"                            return result(status=\"http_error\", error_class=\"HTTPStatus\")"` | — |
| [SRC-1AE03B9EC3-L002141](../../agents/web_agent.py#L2141) | 2141 | `"                        media_type = response.headers.get("` | — |
| [SRC-1AE03B9EC3-L002142](../../agents/web_agent.py#L2142) | 2142 | `"                            \"content-type\", \"\""` | — |
| [SRC-1AE03B9EC3-L002143](../../agents/web_agent.py#L2143) | 2143 | `"                        ).split(\";\")[0].lower()"` | — |
| [SRC-1AE03B9EC3-L002144](../../agents/web_agent.py#L2144) | 2144 | `"                        if media_type not in {"` | — |
| [SRC-1AE03B9EC3-L002145](../../agents/web_agent.py#L2145) | 2145 | `"                            \"text/html\", \"application/xhtml+xml\", \"text/plain\""` | — |
| [SRC-1AE03B9EC3-L002146](../../agents/web_agent.py#L2146) | 2146 | `"                        }:"` | — |
| [SRC-1AE03B9EC3-L002147](../../agents/web_agent.py#L2147) | 2147 | `"                            return result(status=\"unsupported_content_type\", error_class=\"UnsupportedContentType\")"` | — |
| [SRC-1AE03B9EC3-L002148](../../agents/web_agent.py#L2148) | 2148 | `"                        content_length = response.headers.get(\"content-length\")"` | — |
| [SRC-1AE03B9EC3-L002149](../../agents/web_agent.py#L2149) | 2149 | `"                        if content_length:"` | — |
| [SRC-1AE03B9EC3-L002150](../../agents/web_agent.py#L2150) | 2150 | `"                            try:"` | — |
| [SRC-1AE03B9EC3-L002151](../../agents/web_agent.py#L2151) | 2151 | `"                                if int(content_length) > MAX_PAGE_BYTES:"` | — |
| [SRC-1AE03B9EC3-L002152](../../agents/web_agent.py#L2152) | 2152 | `"                                    return result(status=\"page_too_large\", error_class=\"ContentLengthLimit\")"` | — |
| [SRC-1AE03B9EC3-L002153](../../agents/web_agent.py#L2153) | 2153 | `"                            except ValueError:"` | — |
| [SRC-1AE03B9EC3-L002154](../../agents/web_agent.py#L2154) | 2154 | `"                                pass"` | — |
| [SRC-1AE03B9EC3-L002155](../../agents/web_agent.py#L2155) | 2155 | `"                        chunks: list[bytes] = []"` | — |
| [SRC-1AE03B9EC3-L002156](../../agents/web_agent.py#L2156) | 2156 | `"                        count = 0"` | — |
| [SRC-1AE03B9EC3-L002157](../../agents/web_agent.py#L2157) | 2157 | `"                        for chunk in response.iter_bytes():"` | — |
| [SRC-1AE03B9EC3-L002158](../../agents/web_agent.py#L2158) | 2158 | `"                            count += len(chunk)"` | — |
| [SRC-1AE03B9EC3-L002159](../../agents/web_agent.py#L2159) | 2159 | `"                            if count > MAX_PAGE_BYTES:"` | — |
| [SRC-1AE03B9EC3-L002160](../../agents/web_agent.py#L2160) | 2160 | `"                                remaining = max(0, MAX_PAGE_BYTES - (count - len(chunk)))"` | — |
| [SRC-1AE03B9EC3-L002161](../../agents/web_agent.py#L2161) | 2161 | `"                                if remaining:"` | — |
| [SRC-1AE03B9EC3-L002162](../../agents/web_agent.py#L2162) | 2162 | `"                                    chunks.append(chunk[:remaining])"` | — |
| [SRC-1AE03B9EC3-L002163](../../agents/web_agent.py#L2163) | 2163 | `"                                bytes_truncated = True"` | — |
| [SRC-1AE03B9EC3-L002164](../../agents/web_agent.py#L2164) | 2164 | `"                                break"` | — |
| [SRC-1AE03B9EC3-L002165](../../agents/web_agent.py#L2165) | 2165 | `"                            chunks.append(chunk)"` | — |
| [SRC-1AE03B9EC3-L002166](../../agents/web_agent.py#L2166) | 2166 | `"                        raw = b\"\".join(chunks)"` | — |
| [SRC-1AE03B9EC3-L002167](../../agents/web_agent.py#L2167) | 2167 | `"                        encoding = response.encoding or \"utf-8\""` | — |
| [SRC-1AE03B9EC3-L002168](../../agents/web_agent.py#L2168) | 2168 | `"                        html = raw.decode(encoding, errors=\"replace\")"` | — |
| [SRC-1AE03B9EC3-L002169](../../agents/web_agent.py#L2169) | 2169 | `"                        break"` | — |
| [SRC-1AE03B9EC3-L002170](../../agents/web_agent.py#L2170) | 2170 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L002171](../../agents/web_agent.py#L2171) | 2171 | `"                    return result(status=\"redirect_limit\", error_class=\"RedirectLimit\")"` | — |
| [SRC-1AE03B9EC3-L002172](../../agents/web_agent.py#L2172) | 2172 | `"        except (OSError, ValueError, httpx.HTTPError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002173](../../agents/web_agent.py#L2173) | 2173 | `"            return result(status=\"network_error\", error_class=type(exc).__name__)"` | — |
| [SRC-1AE03B9EC3-L002174](../../agents/web_agent.py#L2174) | 2174 | `""` | — |
| [SRC-1AE03B9EC3-L002175](../../agents/web_agent.py#L2175) | 2175 | `"        if media_type == \"text/plain\":"` | — |
| [SRC-1AE03B9EC3-L002176](../../agents/web_agent.py#L2176) | 2176 | `"            bounded_text = _clean_text(html, MAX_PAGE_TEXT_CHARS + 1)"` | — |
| [SRC-1AE03B9EC3-L002177](../../agents/web_agent.py#L2177) | 2177 | `"            text_truncated = len(bounded_text) > MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L002178](../../agents/web_agent.py#L2178) | 2178 | `"            page_text = _clean_text(bounded_text, MAX_PAGE_TEXT_CHARS)"` | — |
| [SRC-1AE03B9EC3-L002179](../../agents/web_agent.py#L2179) | 2179 | `"            status = ("` | — |
| [SRC-1AE03B9EC3-L002180](../../agents/web_agent.py#L2180) | 2180 | `"                \"empty_content\" if not page_text"` | — |
| [SRC-1AE03B9EC3-L002181](../../agents/web_agent.py#L2181) | 2181 | `"                else \"partial_extraction\" if bytes_truncated or text_truncated"` | — |
| [SRC-1AE03B9EC3-L002182](../../agents/web_agent.py#L2182) | 2182 | `"                else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L002183](../../agents/web_agent.py#L2183) | 2183 | `"            )"` | — |
| [SRC-1AE03B9EC3-L002184](../../agents/web_agent.py#L2184) | 2184 | `"            return result(\"\", page_text, status)"` | — |
| [SRC-1AE03B9EC3-L002185](../../agents/web_agent.py#L2185) | 2185 | `""` | — |
| [SRC-1AE03B9EC3-L002186](../../agents/web_agent.py#L2186) | 2186 | `"        soup = BeautifulSoup(html, \"html.parser\")"` | — |
| [SRC-1AE03B9EC3-L002187](../../agents/web_agent.py#L2187) | 2187 | `"        title = _clean_text(soup.title.get_text(\" \", strip=True), 300) if soup.title else \"\""` | — |
| [SRC-1AE03B9EC3-L002188](../../agents/web_agent.py#L2188) | 2188 | `"        for element in soup(["` | — |
| [SRC-1AE03B9EC3-L002189](../../agents/web_agent.py#L2189) | 2189 | `"            \"script\", \"style\", \"nav\", \"footer\", \"header\", \"noscript\","` | — |
| [SRC-1AE03B9EC3-L002190](../../agents/web_agent.py#L2190) | 2190 | `"            \"svg\", \"form\", \"iframe\", \"template\""` | — |
| [SRC-1AE03B9EC3-L002191](../../agents/web_agent.py#L2191) | 2191 | `"        ]):"` | — |
| [SRC-1AE03B9EC3-L002192](../../agents/web_agent.py#L2192) | 2192 | `"            element.decompose()"` | — |
| [SRC-1AE03B9EC3-L002193](../../agents/web_agent.py#L2193) | 2193 | `"        main = soup.find(\"main\") or soup.find(\"article\") or soup.body or soup"` | — |
| [SRC-1AE03B9EC3-L002194](../../agents/web_agent.py#L2194) | 2194 | `"        bounded_text = _clean_text(main.get_text(\" \", strip=True), MAX_PAGE_TEXT_CHARS + 1)"` | — |
| [SRC-1AE03B9EC3-L002195](../../agents/web_agent.py#L2195) | 2195 | `"        text_truncated = len(bounded_text) > MAX_PAGE_TEXT_CHARS"` | — |
| [SRC-1AE03B9EC3-L002196](../../agents/web_agent.py#L2196) | 2196 | `"        page_text = _clean_text(bounded_text, MAX_PAGE_TEXT_CHARS)"` | — |
| [SRC-1AE03B9EC3-L002197](../../agents/web_agent.py#L2197) | 2197 | `"        status = ("` | — |
| [SRC-1AE03B9EC3-L002198](../../agents/web_agent.py#L2198) | 2198 | `"            \"no_text_extracted\" if not page_text"` | — |
| [SRC-1AE03B9EC3-L002199](../../agents/web_agent.py#L2199) | 2199 | `"            else \"partial_extraction\" if bytes_truncated or text_truncated"` | — |
| [SRC-1AE03B9EC3-L002200](../../agents/web_agent.py#L2200) | 2200 | `"            else \"content_extracted\""` | — |
| [SRC-1AE03B9EC3-L002201](../../agents/web_agent.py#L2201) | 2201 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002202](../../agents/web_agent.py#L2202) | 2202 | `"        return result(title, page_text, status)"` | — |
| [SRC-1AE03B9EC3-L002203](../../agents/web_agent.py#L2203) | 2203 | `""` | — |
| [SRC-1AE03B9EC3-L002204](../../agents/web_agent.py#L2204) | 2204 | `"    def _collect_sources(self, query: str) -> tuple[list[dict[str, Any]], str \| None]:"` | — |
| [SRC-1AE03B9EC3-L002205](../../agents/web_agent.py#L2205) | 2205 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002206](../../agents/web_agent.py#L2206) | 2206 | `"            sources = self._search_web(query)"` | — |
| [SRC-1AE03B9EC3-L002207](../../agents/web_agent.py#L2207) | 2207 | `"        except (RuntimeError, AgentDependencyError) as exc:"` | — |
| [SRC-1AE03B9EC3-L002208](../../agents/web_agent.py#L2208) | 2208 | `"            return [], str(exc)"` | — |
| [SRC-1AE03B9EC3-L002209](../../agents/web_agent.py#L2209) | 2209 | `"        for source in sources[:MAX_FETCHED_PAGES]:"` | — |
| [SRC-1AE03B9EC3-L002210](../../agents/web_agent.py#L2210) | 2210 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L002211](../../agents/web_agent.py#L2211) | 2211 | `"                title, page_text = self._fetch_page(source[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L002212](../../agents/web_agent.py#L2212) | 2212 | `"            except (AgentDependencyError, RuntimeError):"` | — |
| [SRC-1AE03B9EC3-L002213](../../agents/web_agent.py#L2213) | 2213 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002214](../../agents/web_agent.py#L2214) | 2214 | `"            if title:"` | — |
| [SRC-1AE03B9EC3-L002215](../../agents/web_agent.py#L2215) | 2215 | `"                source[\"title\"] = title"` | — |
| [SRC-1AE03B9EC3-L002216](../../agents/web_agent.py#L2216) | 2216 | `"            if page_text:"` | — |
| [SRC-1AE03B9EC3-L002217](../../agents/web_agent.py#L2217) | 2217 | `"                source[\"page_text\"] = page_text"` | — |
| [SRC-1AE03B9EC3-L002218](../../agents/web_agent.py#L2218) | 2218 | `"                source[\"page_fetched\"] = True"` | — |
| [SRC-1AE03B9EC3-L002219](../../agents/web_agent.py#L2219) | 2219 | `"                # Prefer extracted text over a thin search snippet."` | — |
| [SRC-1AE03B9EC3-L002220](../../agents/web_agent.py#L2220) | 2220 | `"                source[\"snippet\"] = page_text[:1800]"` | — |
| [SRC-1AE03B9EC3-L002221](../../agents/web_agent.py#L2221) | 2221 | `"        return sources, None"` | — |
| [SRC-1AE03B9EC3-L002222](../../agents/web_agent.py#L2222) | 2222 | `""` | — |
| [SRC-1AE03B9EC3-L002223](../../agents/web_agent.py#L2223) | 2223 | `"    def _collect_research("` | — |
| [SRC-1AE03B9EC3-L002224](../../agents/web_agent.py#L2224) | 2224 | `"        self, plan: dict[str, Any]"` | — |
| [SRC-1AE03B9EC3-L002225](../../agents/web_agent.py#L2225) | 2225 | `"    ) -> tuple[list[dict[str, Any]], list[str], dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L002226](../../agents/web_agent.py#L2226) | 2226 | `"        \"\"\"Run independent query searches concurrently, fuse evidence, then fetch top pages.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002227](../../agents/web_agent.py#L2227) | 2227 | `"        queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L002228](../../agents/web_agent.py#L2228) | 2228 | `"            compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L002229](../../agents/web_agent.py#L2229) | 2229 | `"            for query in plan.get(\"queries\", [])[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L002230](../../agents/web_agent.py#L2230) | 2230 | `"            if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L002231](../../agents/web_agent.py#L2231) | 2231 | `"        ))"` | — |
| [SRC-1AE03B9EC3-L002232](../../agents/web_agent.py#L2232) | 2232 | `"        queries = [query for query in queries if query]"` | — |
| [SRC-1AE03B9EC3-L002233](../../agents/web_agent.py#L2233) | 2233 | `"        warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L002234](../../agents/web_agent.py#L2234) | 2234 | `"        if not queries and not plan.get(\"direct_urls\"):"` | — |
| [SRC-1AE03B9EC3-L002235](../../agents/web_agent.py#L2235) | 2235 | `"            warnings.append(\"لم يُنشأ استعلام موضوعي قابل للبحث؛ لم تُستدعَ محركات البحث.\")"` | — |
| [SRC-1AE03B9EC3-L002236](../../agents/web_agent.py#L2236) | 2236 | `"        batches: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002237](../../agents/web_agent.py#L2237) | 2237 | `"        query_counts: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002238](../../agents/web_agent.py#L2238) | 2238 | `"        search_started_queries = 0"` | — |
| [SRC-1AE03B9EC3-L002239](../../agents/web_agent.py#L2239) | 2239 | `""` | — |
| [SRC-1AE03B9EC3-L002240](../../agents/web_agent.py#L2240) | 2240 | `"        if queries:"` | — |
| [SRC-1AE03B9EC3-L002241](../../agents/web_agent.py#L2241) | 2241 | `"            with ThreadPoolExecutor(max_workers=min(MAX_RESEARCH_WORKERS, len(queries))) as pool:"` | — |
| [SRC-1AE03B9EC3-L002242](../../agents/web_agent.py#L2242) | 2242 | `"                futures = {pool.submit(self._search_web, query): query for query in queries}"` | — |
| [SRC-1AE03B9EC3-L002243](../../agents/web_agent.py#L2243) | 2243 | `"                for future in as_completed(futures):"` | — |
| [SRC-1AE03B9EC3-L002244](../../agents/web_agent.py#L2244) | 2244 | `"                    query = futures[future]"` | — |
