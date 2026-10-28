# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **039**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L001723 إلى SRC-F725E90B2A-L002522
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L001723](../../tests/test_web_agent.py#L1723) | 1723 | `"    assert normalize(\"file:///etc/passwd\") == \"\""` | — |
| [SRC-F725E90B2A-L001724](../../tests/test_web_agent.py#L1724) | 1724 | `""` | — |
| [SRC-F725E90B2A-L001725](../../tests/test_web_agent.py#L1725) | 1725 | `""` | — |
| [SRC-F725E90B2A-L001726](../../tests/test_web_agent.py#L1726) | 1726 | `"def test_bounded_repair_deduplicates_same_page_even_with_tracking_url(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001727](../../tests/test_web_agent.py#L1727) | 1727 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001728](../../tests/test_web_agent.py#L1728) | 1728 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001729](../../tests/test_web_agent.py#L1729) | 1729 | `"        \"queries\": [\"معلومات عن شركة ألفا اليوم\"],"` | — |
| [SRC-F725E90B2A-L001730](../../tests/test_web_agent.py#L1730) | 1730 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L001731](../../tests/test_web_agent.py#L1731) | 1731 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001732](../../tests/test_web_agent.py#L1732) | 1732 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L001733](../../tests/test_web_agent.py#L1733) | 1733 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001734](../../tests/test_web_agent.py#L1734) | 1734 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001735](../../tests/test_web_agent.py#L1735) | 1735 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001736](../../tests/test_web_agent.py#L1736) | 1736 | `"    }"` | — |
| [SRC-F725E90B2A-L001737](../../tests/test_web_agent.py#L1737) | 1737 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L001738](../../tests/test_web_agent.py#L1738) | 1738 | `""` | — |
| [SRC-F725E90B2A-L001739](../../tests/test_web_agent.py#L1739) | 1739 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L001740](../../tests/test_web_agent.py#L1740) | 1740 | `"        calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L001741](../../tests/test_web_agent.py#L1741) | 1741 | `"        source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L001742](../../tests/test_web_agent.py#L1742) | 1742 | `"        if len(calls) > 1:"` | — |
| [SRC-F725E90B2A-L001743](../../tests/test_web_agent.py#L1743) | 1743 | `"            source[\"url\"] = \"https://EXAMPLE.com/research/?utm_source=test#details\""` | — |
| [SRC-F725E90B2A-L001744](../../tests/test_web_agent.py#L1744) | 1744 | `"            source[\"providers\"] = [\"second_provider\"]"` | — |
| [SRC-F725E90B2A-L001745](../../tests/test_web_agent.py#L1745) | 1745 | `"            source[\"page_fetched\"] = False"` | — |
| [SRC-F725E90B2A-L001746](../../tests/test_web_agent.py#L1746) | 1746 | `"        return [source], [], {"` | — |
| [SRC-F725E90B2A-L001747](../../tests/test_web_agent.py#L1747) | 1747 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L001748](../../tests/test_web_agent.py#L1748) | 1748 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001749](../../tests/test_web_agent.py#L1749) | 1749 | `"            \"query_results\": [{\"query\": research_plan[\"queries\"][0], \"results\": 1}],"` | — |
| [SRC-F725E90B2A-L001750](../../tests/test_web_agent.py#L1750) | 1750 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L001751](../../tests/test_web_agent.py#L1751) | 1751 | `"            \"pages_fetched\": 1 if len(calls) == 1 else 0,"` | — |
| [SRC-F725E90B2A-L001752](../../tests/test_web_agent.py#L1752) | 1752 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001753](../../tests/test_web_agent.py#L1753) | 1753 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L001754](../../tests/test_web_agent.py#L1754) | 1754 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001755](../../tests/test_web_agent.py#L1755) | 1755 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001756](../../tests/test_web_agent.py#L1756) | 1756 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001757](../../tests/test_web_agent.py#L1757) | 1757 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L001758](../../tests/test_web_agent.py#L1758) | 1758 | `"        }"` | — |
| [SRC-F725E90B2A-L001759](../../tests/test_web_agent.py#L1759) | 1759 | `""` | — |
| [SRC-F725E90B2A-L001760](../../tests/test_web_agent.py#L1760) | 1760 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001761](../../tests/test_web_agent.py#L1761) | 1761 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L001762](../../tests/test_web_agent.py#L1762) | 1762 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L001763](../../tests/test_web_agent.py#L1763) | 1763 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001764](../../tests/test_web_agent.py#L1764) | 1764 | `"        agent, \"_generate\","` | — |
| [SRC-F725E90B2A-L001765](../../tests/test_web_agent.py#L1765) | 1765 | `"        lambda *args, **kwargs: pytest.fail(\"Duplicate URL must not satisfy corroboration\"),"` | — |
| [SRC-F725E90B2A-L001766](../../tests/test_web_agent.py#L1766) | 1766 | `"    )"` | — |
| [SRC-F725E90B2A-L001767](../../tests/test_web_agent.py#L1767) | 1767 | `""` | — |
| [SRC-F725E90B2A-L001768](../../tests/test_web_agent.py#L1768) | 1768 | `"    result = agent.answer(\"ما آخر معلومات عن شركة ألفا اليوم؟\")"` | — |
| [SRC-F725E90B2A-L001769](../../tests/test_web_agent.py#L1769) | 1769 | `""` | — |
| [SRC-F725E90B2A-L001770](../../tests/test_web_agent.py#L1770) | 1770 | `"    assert len(calls) == 2"` | — |
| [SRC-F725E90B2A-L001771](../../tests/test_web_agent.py#L1771) | 1771 | `"    repair = result[\"search_report\"][\"evidence_repair\"]"` | — |
| [SRC-F725E90B2A-L001772](../../tests/test_web_agent.py#L1772) | 1772 | `"    assert repair[\"attempted\"] is True"` | — |
| [SRC-F725E90B2A-L001773](../../tests/test_web_agent.py#L1773) | 1773 | `"    assert repair[\"new_sources_added\"] == 0"` | — |
| [SRC-F725E90B2A-L001774](../../tests/test_web_agent.py#L1774) | 1774 | `"    assert repair[\"recovered\"] is False"` | — |
| [SRC-F725E90B2A-L001775](../../tests/test_web_agent.py#L1775) | 1775 | `"    assert result[\"search_report\"][\"independent_sources\"] == 0"` | — |
| [SRC-F725E90B2A-L001776](../../tests/test_web_agent.py#L1776) | 1776 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L001777](../../tests/test_web_agent.py#L1777) | 1777 | `"    assert result[\"search_report\"][\"source_guardrails\"][\"final\"][\"current_evidence_status\"] == \"no_current_eligible_evidence\""` | — |
| [SRC-F725E90B2A-L001778](../../tests/test_web_agent.py#L1778) | 1778 | `""` | — |
| [SRC-F725E90B2A-L001779](../../tests/test_web_agent.py#L1779) | 1779 | `""` | — |
| [SRC-F725E90B2A-L001780](../../tests/test_web_agent.py#L1780) | 1780 | `"def test_social_focused_partial_evidence_does_not_trigger_general_repair(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001781](../../tests/test_web_agent.py#L1781) | 1781 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001782](../../tests/test_web_agent.py#L1782) | 1782 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001783](../../tests/test_web_agent.py#L1783) | 1783 | `"        \"queries\": [\"تجارب المستخدمين حول التقنية\"],"` | — |
| [SRC-F725E90B2A-L001784](../../tests/test_web_agent.py#L1784) | 1784 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L001785](../../tests/test_web_agent.py#L1785) | 1785 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001786](../../tests/test_web_agent.py#L1786) | 1786 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L001787](../../tests/test_web_agent.py#L1787) | 1787 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001788](../../tests/test_web_agent.py#L1788) | 1788 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001789](../../tests/test_web_agent.py#L1789) | 1789 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001790](../../tests/test_web_agent.py#L1790) | 1790 | `"    }"` | — |
| [SRC-F725E90B2A-L001791](../../tests/test_web_agent.py#L1791) | 1791 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L001792](../../tests/test_web_agent.py#L1792) | 1792 | `""` | — |
| [SRC-F725E90B2A-L001793](../../tests/test_web_agent.py#L1793) | 1793 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L001794](../../tests/test_web_agent.py#L1794) | 1794 | `"        calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L001795](../../tests/test_web_agent.py#L1795) | 1795 | `"        social_source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L001796](../../tests/test_web_agent.py#L1796) | 1796 | `"        social_source.update({"` | — |
| [SRC-F725E90B2A-L001797](../../tests/test_web_agent.py#L1797) | 1797 | `"            \"url\": \"https://www.reddit.com/r/example/comments/test\","` | — |
| [SRC-F725E90B2A-L001798](../../tests/test_web_agent.py#L1798) | 1798 | `"            \"domain\": \"reddit.com\","` | — |
| [SRC-F725E90B2A-L001799](../../tests/test_web_agent.py#L1799) | 1799 | `"            \"platform\": \"reddit\","` | — |
| [SRC-F725E90B2A-L001800](../../tests/test_web_agent.py#L1800) | 1800 | `"            \"source_class\": \"social\","` | — |
| [SRC-F725E90B2A-L001801](../../tests/test_web_agent.py#L1801) | 1801 | `"        })"` | — |
| [SRC-F725E90B2A-L001802](../../tests/test_web_agent.py#L1802) | 1802 | `"        return [social_source], [], {"` | — |
| [SRC-F725E90B2A-L001803](../../tests/test_web_agent.py#L1803) | 1803 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L001804](../../tests/test_web_agent.py#L1804) | 1804 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001805](../../tests/test_web_agent.py#L1805) | 1805 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L001806](../../tests/test_web_agent.py#L1806) | 1806 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L001807](../../tests/test_web_agent.py#L1807) | 1807 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L001808](../../tests/test_web_agent.py#L1808) | 1808 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001809](../../tests/test_web_agent.py#L1809) | 1809 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L001810](../../tests/test_web_agent.py#L1810) | 1810 | `"            \"social_direct_results\": 1,"` | — |
| [SRC-F725E90B2A-L001811](../../tests/test_web_agent.py#L1811) | 1811 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L001812](../../tests/test_web_agent.py#L1812) | 1812 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001813](../../tests/test_web_agent.py#L1813) | 1813 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L001814](../../tests/test_web_agent.py#L1814) | 1814 | `"        }"` | — |
| [SRC-F725E90B2A-L001815](../../tests/test_web_agent.py#L1815) | 1815 | `""` | — |
| [SRC-F725E90B2A-L001816](../../tests/test_web_agent.py#L1816) | 1816 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001817](../../tests/test_web_agent.py#L1817) | 1817 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L001818](../../tests/test_web_agent.py#L1818) | 1818 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L001819](../../tests/test_web_agent.py#L1819) | 1819 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"إشارات أولية فقط [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L001820](../../tests/test_web_agent.py#L1820) | 1820 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L001821](../../tests/test_web_agent.py#L1821) | 1821 | `""` | — |
| [SRC-F725E90B2A-L001822](../../tests/test_web_agent.py#L1822) | 1822 | `"    result = agent.answer(\"اجمع آراء الناس حول هذه التقنية\", mode=\"social\")"` | — |
| [SRC-F725E90B2A-L001823](../../tests/test_web_agent.py#L1823) | 1823 | `""` | — |
| [SRC-F725E90B2A-L001824](../../tests/test_web_agent.py#L1824) | 1824 | `"    assert len(calls) == 1"` | — |
| [SRC-F725E90B2A-L001825](../../tests/test_web_agent.py#L1825) | 1825 | `"    assert calls[0][\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L001826](../../tests/test_web_agent.py#L1826) | 1826 | `"    assert result[\"search_report\"][\"evidence_repair\"][\"attempted\"] is False"` | — |
| [SRC-F725E90B2A-L001827](../../tests/test_web_agent.py#L1827) | 1827 | `"    assert result[\"search_report\"][\"evidence_repair\"][\"reason\"] == \"task_specific_partial_evidence\""` | — |
| [SRC-F725E90B2A-L001828](../../tests/test_web_agent.py#L1828) | 1828 | `"    assert result[\"research_quality\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L001829](../../tests/test_web_agent.py#L1829) | 1829 | `""` | — |
| [SRC-F725E90B2A-L001830](../../tests/test_web_agent.py#L1830) | 1830 | `""` | — |
| [SRC-F725E90B2A-L001831](../../tests/test_web_agent.py#L1831) | 1831 | `""` | — |
| [SRC-F725E90B2A-L001832](../../tests/test_web_agent.py#L1832) | 1832 | `"def test_question_coverage_targets_extract_arabic_and_english_explicit_criteria():"` | — |
| [SRC-F725E90B2A-L001833](../../tests/test_web_agent.py#L1833) | 1833 | `"    arabic = WebAgent._question_coverage_targets("` | — |
| [SRC-F725E90B2A-L001834](../../tests/test_web_agent.py#L1834) | 1834 | `"        \"قارن بين خدمتين من حيث السعر، الخصوصية، الاعتمادية، وخيار التواصل مع الدعم، \""` | — |
| [SRC-F725E90B2A-L001835](../../tests/test_web_agent.py#L1835) | 1835 | `"        \"واذكر ما لا تستطيع التحقق منه.\""` | — |
| [SRC-F725E90B2A-L001836](../../tests/test_web_agent.py#L1836) | 1836 | `"    )"` | — |
| [SRC-F725E90B2A-L001837](../../tests/test_web_agent.py#L1837) | 1837 | `"    assert arabic == [\"السعر\", \"الخصوصية\", \"الاعتمادية\", \"خيار التواصل مع الدعم\"]"` | — |
| [SRC-F725E90B2A-L001838](../../tests/test_web_agent.py#L1838) | 1838 | `""` | — |
| [SRC-F725E90B2A-L001839](../../tests/test_web_agent.py#L1839) | 1839 | `"    english = WebAgent._question_coverage_targets("` | — |
| [SRC-F725E90B2A-L001840](../../tests/test_web_agent.py#L1840) | 1840 | `"        \"Compare two services in terms of price, privacy, reliability and customer support?\""` | — |
| [SRC-F725E90B2A-L001841](../../tests/test_web_agent.py#L1841) | 1841 | `"    )"` | — |
| [SRC-F725E90B2A-L001842](../../tests/test_web_agent.py#L1842) | 1842 | `"    assert english == [\"price\", \"privacy\", \"reliability\", \"customer support\"]"` | — |
| [SRC-F725E90B2A-L001843](../../tests/test_web_agent.py#L1843) | 1843 | `""` | — |
| [SRC-F725E90B2A-L001844](../../tests/test_web_agent.py#L1844) | 1844 | `"    english_with_period = WebAgent._question_coverage_targets("` | — |
| [SRC-F725E90B2A-L001845](../../tests/test_web_agent.py#L1845) | 1845 | `"        \"Compare two services in terms of price, privacy and reliability.\""` | — |
| [SRC-F725E90B2A-L001846](../../tests/test_web_agent.py#L1846) | 1846 | `"    )"` | — |
| [SRC-F725E90B2A-L001847](../../tests/test_web_agent.py#L1847) | 1847 | `"    assert english_with_period == [\"price\", \"privacy\", \"reliability\"]"` | — |
| [SRC-F725E90B2A-L001848](../../tests/test_web_agent.py#L1848) | 1848 | `""` | — |
| [SRC-F725E90B2A-L001849](../../tests/test_web_agent.py#L1849) | 1849 | `""` | — |
| [SRC-F725E90B2A-L001850](../../tests/test_web_agent.py#L1850) | 1850 | `"def test_question_coverage_targets_do_not_invent_parts_for_simple_question():"` | — |
| [SRC-F725E90B2A-L001851](../../tests/test_web_agent.py#L1851) | 1851 | `"    assert WebAgent._question_coverage_targets(\"ما الذي يقوله المصدر؟\") == []"` | — |
| [SRC-F725E90B2A-L001852](../../tests/test_web_agent.py#L1852) | 1852 | `""` | — |
| [SRC-F725E90B2A-L001853](../../tests/test_web_agent.py#L1853) | 1853 | `""` | — |
| [SRC-F725E90B2A-L001854](../../tests/test_web_agent.py#L1854) | 1854 | `"def test_generator_includes_extracted_targets_as_a_non_authoritative_checklist(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001855](../../tests/test_web_agent.py#L1855) | 1855 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001856](../../tests/test_web_agent.py#L1856) | 1856 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L001857](../../tests/test_web_agent.py#L1857) | 1857 | `""` | — |
| [SRC-F725E90B2A-L001858](../../tests/test_web_agent.py#L1858) | 1858 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L001859](../../tests/test_web_agent.py#L1859) | 1859 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L001860](../../tests/test_web_agent.py#L1860) | 1860 | `"        return \"مقارنة مختصرة.\""` | — |
| [SRC-F725E90B2A-L001861](../../tests/test_web_agent.py#L1861) | 1861 | `""` | — |
| [SRC-F725E90B2A-L001862](../../tests/test_web_agent.py#L1862) | 1862 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L001863](../../tests/test_web_agent.py#L1863) | 1863 | `"    result = agent._generate("` | — |
| [SRC-F725E90B2A-L001864](../../tests/test_web_agent.py#L1864) | 1864 | `"        question=\"قارن بين خدمتين من حيث السعر، الخصوصية والاعتمادية\","` | — |
| [SRC-F725E90B2A-L001865](../../tests/test_web_agent.py#L1865) | 1865 | `"        history=[],"` | — |
| [SRC-F725E90B2A-L001866](../../tests/test_web_agent.py#L1866) | 1866 | `"        sources=[sample_source(0), sample_source(1)],"` | — |
| [SRC-F725E90B2A-L001867](../../tests/test_web_agent.py#L1867) | 1867 | `"        search_warning=None,"` | — |
| [SRC-F725E90B2A-L001868](../../tests/test_web_agent.py#L1868) | 1868 | `"        research_plan={\"depth\": \"deep\", \"queries\": [\"مقارنة الخدمتين\"]},"` | — |
| [SRC-F725E90B2A-L001869](../../tests/test_web_agent.py#L1869) | 1869 | `"        search_report={},"` | — |
| [SRC-F725E90B2A-L001870](../../tests/test_web_agent.py#L1870) | 1870 | `"    )"` | — |
| [SRC-F725E90B2A-L001871](../../tests/test_web_agent.py#L1871) | 1871 | `""` | — |
| [SRC-F725E90B2A-L001872](../../tests/test_web_agent.py#L1872) | 1872 | `"    user_content = \"\\n\".join(m[\"content\"] for m in captured[\"messages\"] if m[\"role\"] == \"user\")"` | — |
| [SRC-F725E90B2A-L001873](../../tests/test_web_agent.py#L1873) | 1873 | `"    assert result == \"مقارنة مختصرة.\""` | — |
| [SRC-F725E90B2A-L001874](../../tests/test_web_agent.py#L1874) | 1874 | `"    assert \"قائمة محاور مستخرجة آليًا\" in user_content"` | — |
| [SRC-F725E90B2A-L001875](../../tests/test_web_agent.py#L1875) | 1875 | `"    for target in (\"السعر\", \"الخصوصية\", \"الاعتمادية\"):"` | — |
| [SRC-F725E90B2A-L001876](../../tests/test_web_agent.py#L1876) | 1876 | `"        assert target in user_content"` | — |
| [SRC-F725E90B2A-L001877](../../tests/test_web_agent.py#L1877) | 1877 | `""` | — |
| [SRC-F725E90B2A-L001878](../../tests/test_web_agent.py#L1878) | 1878 | `""` | — |
| [SRC-F725E90B2A-L001879](../../tests/test_web_agent.py#L1879) | 1879 | `"def test_reviewer_checks_coverage_targets_without_claiming_independent_verification(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001880](../../tests/test_web_agent.py#L1880) | 1880 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001881](../../tests/test_web_agent.py#L1881) | 1881 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L001882](../../tests/test_web_agent.py#L1882) | 1882 | `""` | — |
| [SRC-F725E90B2A-L001883](../../tests/test_web_agent.py#L1883) | 1883 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L001884](../../tests/test_web_agent.py#L1884) | 1884 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L001885](../../tests/test_web_agent.py#L1885) | 1885 | `"        return \"<<<OMARAI_FINAL_ANSWER>>>تمت مراجعة المسودة.<<<END_OMARAI_FINAL_ANSWER>>>\""` | — |
| [SRC-F725E90B2A-L001886](../../tests/test_web_agent.py#L1886) | 1886 | `""` | — |
| [SRC-F725E90B2A-L001887](../../tests/test_web_agent.py#L1887) | 1887 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L001888](../../tests/test_web_agent.py#L1888) | 1888 | `"    result = agent._review_answer("` | — |
| [SRC-F725E90B2A-L001889](../../tests/test_web_agent.py#L1889) | 1889 | `"        question=\"قارن بين خدمتين من حيث السعر، الخصوصية والاعتمادية\","` | — |
| [SRC-F725E90B2A-L001890](../../tests/test_web_agent.py#L1890) | 1890 | `"        answer=\"السعر مناسب [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L001891](../../tests/test_web_agent.py#L1891) | 1891 | `"        sources=[sample_source(0)],"` | — |
| [SRC-F725E90B2A-L001892](../../tests/test_web_agent.py#L1892) | 1892 | `"    )"` | — |
| [SRC-F725E90B2A-L001893](../../tests/test_web_agent.py#L1893) | 1893 | `"    system_content = \"\\n\".join(m[\"content\"] for m in captured[\"messages\"] if m[\"role\"] == \"system\")"` | — |
| [SRC-F725E90B2A-L001894](../../tests/test_web_agent.py#L1894) | 1894 | `"    user_content = \"\\n\".join(m[\"content\"] for m in captured[\"messages\"] if m[\"role\"] == \"user\")"` | — |
| [SRC-F725E90B2A-L001895](../../tests/test_web_agent.py#L1895) | 1895 | `"    assert result == \"تمت مراجعة المسودة.\""` | — |
| [SRC-F725E90B2A-L001896](../../tests/test_web_agent.py#L1896) | 1896 | `"    assert \"اكتمال الإجابة مقابل\" in system_content"` | — |
| [SRC-F725E90B2A-L001897](../../tests/test_web_agent.py#L1897) | 1897 | `"    assert \"الاعتمادية\" in user_content"` | — |
| [SRC-F725E90B2A-L001898](../../tests/test_web_agent.py#L1898) | 1898 | `"    assert \"قائمة محاور مستخرجة آليًا\" in user_content"` | — |
| [SRC-F725E90B2A-L001899](../../tests/test_web_agent.py#L1899) | 1899 | `""` | — |
| [SRC-F725E90B2A-L001900](../../tests/test_web_agent.py#L1900) | 1900 | `""` | — |
| [SRC-F725E90B2A-L001901](../../tests/test_web_agent.py#L1901) | 1901 | `"def test_search_attempt_is_reported_when_no_sources_survive(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001902](../../tests/test_web_agent.py#L1902) | 1902 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001903](../../tests/test_web_agent.py#L1903) | 1903 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L001904](../../tests/test_web_agent.py#L1904) | 1904 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001905](../../tests/test_web_agent.py#L1905) | 1905 | `"        \"queries\": [\"ما آخر تطورات الطاقة المتجددة اليوم؟\"],"` | — |
| [SRC-F725E90B2A-L001906](../../tests/test_web_agent.py#L1906) | 1906 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L001907](../../tests/test_web_agent.py#L1907) | 1907 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001908](../../tests/test_web_agent.py#L1908) | 1908 | `"        \"freshness\": \"today\","` | — |
| [SRC-F725E90B2A-L001909](../../tests/test_web_agent.py#L1909) | 1909 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L001910](../../tests/test_web_agent.py#L1910) | 1910 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001911](../../tests/test_web_agent.py#L1911) | 1911 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001912](../../tests/test_web_agent.py#L1912) | 1912 | `"    }"` | — |
| [SRC-F725E90B2A-L001913](../../tests/test_web_agent.py#L1913) | 1913 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L001914](../../tests/test_web_agent.py#L1914) | 1914 | `""` | — |
| [SRC-F725E90B2A-L001915](../../tests/test_web_agent.py#L1915) | 1915 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L001916](../../tests/test_web_agent.py#L1916) | 1916 | `"        calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L001917](../../tests/test_web_agent.py#L1917) | 1917 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L001918](../../tests/test_web_agent.py#L1918) | 1918 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L001919](../../tests/test_web_agent.py#L1919) | 1919 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001920](../../tests/test_web_agent.py#L1920) | 1920 | `"            \"query_results\": [{\"query\": research_plan[\"queries\"][0], \"results\": 0}],"` | — |
| [SRC-F725E90B2A-L001921](../../tests/test_web_agent.py#L1921) | 1921 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L001922](../../tests/test_web_agent.py#L1922) | 1922 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L001923](../../tests/test_web_agent.py#L1923) | 1923 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L001924](../../tests/test_web_agent.py#L1924) | 1924 | `"            \"provider_counts\": {},"` | — |
| [SRC-F725E90B2A-L001925](../../tests/test_web_agent.py#L1925) | 1925 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L001926](../../tests/test_web_agent.py#L1926) | 1926 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001927](../../tests/test_web_agent.py#L1927) | 1927 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L001928](../../tests/test_web_agent.py#L1928) | 1928 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001929](../../tests/test_web_agent.py#L1929) | 1929 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L001930](../../tests/test_web_agent.py#L1930) | 1930 | `"        }"` | — |
| [SRC-F725E90B2A-L001931](../../tests/test_web_agent.py#L1931) | 1931 | `""` | — |
| [SRC-F725E90B2A-L001932](../../tests/test_web_agent.py#L1932) | 1932 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001933](../../tests/test_web_agent.py#L1933) | 1933 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L001934](../../tests/test_web_agent.py#L1934) | 1934 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001935](../../tests/test_web_agent.py#L1935) | 1935 | `"        agent,"` | — |
| [SRC-F725E90B2A-L001936](../../tests/test_web_agent.py#L1936) | 1936 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L001937](../../tests/test_web_agent.py#L1937) | 1937 | `"        lambda *args, **kwargs: pytest.fail(\"The model must not answer without usable evidence\"),"` | — |
| [SRC-F725E90B2A-L001938](../../tests/test_web_agent.py#L1938) | 1938 | `"    )"` | — |
| [SRC-F725E90B2A-L001939](../../tests/test_web_agent.py#L1939) | 1939 | `""` | — |
| [SRC-F725E90B2A-L001940](../../tests/test_web_agent.py#L1940) | 1940 | `"    result = agent.answer(\"ما آخر تطورات الطاقة المتجددة اليوم؟\")"` | — |
| [SRC-F725E90B2A-L001941](../../tests/test_web_agent.py#L1941) | 1941 | `""` | — |
| [SRC-F725E90B2A-L001942](../../tests/test_web_agent.py#L1942) | 1942 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L001943](../../tests/test_web_agent.py#L1943) | 1943 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L001944](../../tests/test_web_agent.py#L1944) | 1944 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-F725E90B2A-L001945](../../tests/test_web_agent.py#L1945) | 1945 | `"    assert result[\"sources\"] == []"` | — |
| [SRC-F725E90B2A-L001946](../../tests/test_web_agent.py#L1946) | 1946 | `"    assert result[\"search_report\"][\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L001947](../../tests/test_web_agent.py#L1947) | 1947 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_no_usable_sources\""` | — |
| [SRC-F725E90B2A-L001948](../../tests/test_web_agent.py#L1948) | 1948 | `"    assert result[\"search_report\"][\"usable_sources_after_filtering\"] == 0"` | — |
| [SRC-F725E90B2A-L001949](../../tests/test_web_agent.py#L1949) | 1949 | `"    assert calls, \"Expected at least one attempted retrieval round\""` | — |
| [SRC-F725E90B2A-L001950](../../tests/test_web_agent.py#L1950) | 1950 | `""` | — |
| [SRC-F725E90B2A-L001951](../../tests/test_web_agent.py#L1951) | 1951 | `""` | — |
| [SRC-F725E90B2A-L001952](../../tests/test_web_agent.py#L1952) | 1952 | `"def test_success_report_counts_registrable_domains_not_sibling_subdomains(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001953](../../tests/test_web_agent.py#L1953) | 1953 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001954](../../tests/test_web_agent.py#L1954) | 1954 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L001955](../../tests/test_web_agent.py#L1955) | 1955 | `"    first = sample_source(0)"` | — |
| [SRC-F725E90B2A-L001956](../../tests/test_web_agent.py#L1956) | 1956 | `"    first[\"url\"] = \"https://news.example.com/research\""` | — |
| [SRC-F725E90B2A-L001957](../../tests/test_web_agent.py#L1957) | 1957 | `"    first[\"domain\"] = \"news.example.com\""` | — |
| [SRC-F725E90B2A-L001958](../../tests/test_web_agent.py#L1958) | 1958 | `"    second = sample_source(0)"` | — |
| [SRC-F725E90B2A-L001959](../../tests/test_web_agent.py#L1959) | 1959 | `"    second[\"url\"] = \"https://offers.example.com/research\""` | — |
| [SRC-F725E90B2A-L001960](../../tests/test_web_agent.py#L1960) | 1960 | `"    second[\"domain\"] = \"offers.example.com\""` | — |
| [SRC-F725E90B2A-L001961](../../tests/test_web_agent.py#L1961) | 1961 | `"    third = sample_source(1)"` | — |
| [SRC-F725E90B2A-L001962](../../tests/test_web_agent.py#L1962) | 1962 | `"    sources = [first, second, third]"` | — |
| [SRC-F725E90B2A-L001963](../../tests/test_web_agent.py#L1963) | 1963 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001964](../../tests/test_web_agent.py#L1964) | 1964 | `"        \"queries\": [\"قارن هذه التقنية\"],"` | — |
| [SRC-F725E90B2A-L001965](../../tests/test_web_agent.py#L1965) | 1965 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L001966](../../tests/test_web_agent.py#L1966) | 1966 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001967](../../tests/test_web_agent.py#L1967) | 1967 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L001968](../../tests/test_web_agent.py#L1968) | 1968 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L001969](../../tests/test_web_agent.py#L1969) | 1969 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001970](../../tests/test_web_agent.py#L1970) | 1970 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001971](../../tests/test_web_agent.py#L1971) | 1971 | `"    }"` | — |
| [SRC-F725E90B2A-L001972](../../tests/test_web_agent.py#L1972) | 1972 | `""` | — |
| [SRC-F725E90B2A-L001973](../../tests/test_web_agent.py#L1973) | 1973 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001974](../../tests/test_web_agent.py#L1974) | 1974 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001975](../../tests/test_web_agent.py#L1975) | 1975 | `"        agent,"` | — |
| [SRC-F725E90B2A-L001976](../../tests/test_web_agent.py#L1976) | 1976 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L001977](../../tests/test_web_agent.py#L1977) | 1977 | `"        lambda research_plan: ("` | — |
| [SRC-F725E90B2A-L001978](../../tests/test_web_agent.py#L1978) | 1978 | `"            sources,"` | — |
| [SRC-F725E90B2A-L001979](../../tests/test_web_agent.py#L1979) | 1979 | `"            [],"` | — |
| [SRC-F725E90B2A-L001980](../../tests/test_web_agent.py#L1980) | 1980 | `"            {"` | — |
| [SRC-F725E90B2A-L001981](../../tests/test_web_agent.py#L1981) | 1981 | `"                \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L001982](../../tests/test_web_agent.py#L1982) | 1982 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001983](../../tests/test_web_agent.py#L1983) | 1983 | `"                \"query_results\": [{\"query\": \"قارن هذه التقنية\", \"results\": 3}],"` | — |
| [SRC-F725E90B2A-L001984](../../tests/test_web_agent.py#L1984) | 1984 | `"                \"unique_sources\": 3,"` | — |
| [SRC-F725E90B2A-L001985](../../tests/test_web_agent.py#L1985) | 1985 | `"                \"pages_fetched\": 3,"` | — |
| [SRC-F725E90B2A-L001986](../../tests/test_web_agent.py#L1986) | 1986 | `"                \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L001987](../../tests/test_web_agent.py#L1987) | 1987 | `"                \"provider_counts\": {\"test_provider\": 3},"` | — |
| [SRC-F725E90B2A-L001988](../../tests/test_web_agent.py#L1988) | 1988 | `"                \"platform_counts\": {\"web\": 3},"` | — |
| [SRC-F725E90B2A-L001989](../../tests/test_web_agent.py#L1989) | 1989 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001990](../../tests/test_web_agent.py#L1990) | 1990 | `"                \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L001991](../../tests/test_web_agent.py#L1991) | 1991 | `"                \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001992](../../tests/test_web_agent.py#L1992) | 1992 | `"                \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L001993](../../tests/test_web_agent.py#L1993) | 1993 | `"            },"` | — |
| [SRC-F725E90B2A-L001994](../../tests/test_web_agent.py#L1994) | 1994 | `"        ),"` | — |
| [SRC-F725E90B2A-L001995](../../tests/test_web_agent.py#L1995) | 1995 | `"    )"` | — |
| [SRC-F725E90B2A-L001996](../../tests/test_web_agent.py#L1996) | 1996 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L001997](../../tests/test_web_agent.py#L1997) | 1997 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"الإجابة [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L001998](../../tests/test_web_agent.py#L1998) | 1998 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L001999](../../tests/test_web_agent.py#L1999) | 1999 | `""` | — |
| [SRC-F725E90B2A-L002000](../../tests/test_web_agent.py#L2000) | 2000 | `"    result = agent.answer(\"قارن هذه التقنية\")"` | — |
| [SRC-F725E90B2A-L002001](../../tests/test_web_agent.py#L2001) | 2001 | `""` | — |
| [SRC-F725E90B2A-L002002](../../tests/test_web_agent.py#L2002) | 2002 | `"    assert result[\"kind\"] in {\"web_research\", \"web_fallback\"}"` | — |
| [SRC-F725E90B2A-L002003](../../tests/test_web_agent.py#L2003) | 2003 | `"    assert result[\"search_report\"][\"unique_sources\"] == 3"` | — |
| [SRC-F725E90B2A-L002004](../../tests/test_web_agent.py#L2004) | 2004 | `"    assert result[\"search_report\"][\"distinct_registrable_domains\"] == 2"` | — |
| [SRC-F725E90B2A-L002005](../../tests/test_web_agent.py#L2005) | 2005 | `"    assert result[\"search_report\"][\"independent_sources\"] == 2"` | — |
| [SRC-F725E90B2A-L002006](../../tests/test_web_agent.py#L2006) | 2006 | `"    assert result[\"search_report\"][\"editorial_independence_status\"] == \"not_assessed\""` | — |
| [SRC-F725E90B2A-L002007](../../tests/test_web_agent.py#L2007) | 2007 | `""` | — |
| [SRC-F725E90B2A-L002008](../../tests/test_web_agent.py#L2008) | 2008 | `""` | — |
| [SRC-F725E90B2A-L002009](../../tests/test_web_agent.py#L2009) | 2009 | `"def test_completion_rejects_content_filtered_primary_and_uses_fallback(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002010](../../tests/test_web_agent.py#L2010) | 2010 | `"    import json"` | — |
| [SRC-F725E90B2A-L002011](../../tests/test_web_agent.py#L2011) | 2011 | `""` | — |
| [SRC-F725E90B2A-L002012](../../tests/test_web_agent.py#L2012) | 2012 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002013](../../tests/test_web_agent.py#L2013) | 2013 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002014](../../tests/test_web_agent.py#L2014) | 2014 | `"    agent.fallback_model = \"fallback/model\""` | — |
| [SRC-F725E90B2A-L002015](../../tests/test_web_agent.py#L2015) | 2015 | `"    called = []"` | — |
| [SRC-F725E90B2A-L002016](../../tests/test_web_agent.py#L2016) | 2016 | `""` | — |
| [SRC-F725E90B2A-L002017](../../tests/test_web_agent.py#L2017) | 2017 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L002018](../../tests/test_web_agent.py#L2018) | 2018 | `"        def __init__(self, content, finish_reason):"` | — |
| [SRC-F725E90B2A-L002019](../../tests/test_web_agent.py#L2019) | 2019 | `"            self.body = json.dumps({"` | — |
| [SRC-F725E90B2A-L002020](../../tests/test_web_agent.py#L2020) | 2020 | `"                \"choices\": [{"` | — |
| [SRC-F725E90B2A-L002021](../../tests/test_web_agent.py#L2021) | 2021 | `"                    \"message\": {\"content\": content},"` | — |
| [SRC-F725E90B2A-L002022](../../tests/test_web_agent.py#L2022) | 2022 | `"                    \"finish_reason\": finish_reason,"` | — |
| [SRC-F725E90B2A-L002023](../../tests/test_web_agent.py#L2023) | 2023 | `"                }]"` | — |
| [SRC-F725E90B2A-L002024](../../tests/test_web_agent.py#L2024) | 2024 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002025](../../tests/test_web_agent.py#L2025) | 2025 | `""` | — |
| [SRC-F725E90B2A-L002026](../../tests/test_web_agent.py#L2026) | 2026 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L002027](../../tests/test_web_agent.py#L2027) | 2027 | `"            return self"` | — |
| [SRC-F725E90B2A-L002028](../../tests/test_web_agent.py#L2028) | 2028 | `""` | — |
| [SRC-F725E90B2A-L002029](../../tests/test_web_agent.py#L2029) | 2029 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L002030](../../tests/test_web_agent.py#L2030) | 2030 | `"            return False"` | — |
| [SRC-F725E90B2A-L002031](../../tests/test_web_agent.py#L2031) | 2031 | `""` | — |
| [SRC-F725E90B2A-L002032](../../tests/test_web_agent.py#L2032) | 2032 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L002033](../../tests/test_web_agent.py#L2033) | 2033 | `"            return self.body"` | — |
| [SRC-F725E90B2A-L002034](../../tests/test_web_agent.py#L2034) | 2034 | `""` | — |
| [SRC-F725E90B2A-L002035](../../tests/test_web_agent.py#L2035) | 2035 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L002036](../../tests/test_web_agent.py#L2036) | 2036 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-F725E90B2A-L002037](../../tests/test_web_agent.py#L2037) | 2037 | `"        called.append(model)"` | — |
| [SRC-F725E90B2A-L002038](../../tests/test_web_agent.py#L2038) | 2038 | `"        if model == \"filtered/primary\":"` | — |
| [SRC-F725E90B2A-L002039](../../tests/test_web_agent.py#L2039) | 2039 | `"            return FakeResponse(\"جزء جواب مفلتر لا ينبغي اعتباره مكتملا\", \"content_filter\")"` | — |
| [SRC-F725E90B2A-L002040](../../tests/test_web_agent.py#L2040) | 2040 | `"        return FakeResponse(\"إجابة الاحتياط المكتملة\", \"stop\")"` | — |
| [SRC-F725E90B2A-L002041](../../tests/test_web_agent.py#L2041) | 2041 | `""` | — |
| [SRC-F725E90B2A-L002042](../../tests/test_web_agent.py#L2042) | 2042 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L002043](../../tests/test_web_agent.py#L2043) | 2043 | `"    result = agent._request_completion("` | — |
| [SRC-F725E90B2A-L002044](../../tests/test_web_agent.py#L2044) | 2044 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-F725E90B2A-L002045](../../tests/test_web_agent.py#L2045) | 2045 | `"        model=\"filtered/primary\","` | — |
| [SRC-F725E90B2A-L002046](../../tests/test_web_agent.py#L2046) | 2046 | `"    )"` | — |
| [SRC-F725E90B2A-L002047](../../tests/test_web_agent.py#L2047) | 2047 | `""` | — |
| [SRC-F725E90B2A-L002048](../../tests/test_web_agent.py#L2048) | 2048 | `"    assert result == \"إجابة الاحتياط المكتملة\""` | — |
| [SRC-F725E90B2A-L002049](../../tests/test_web_agent.py#L2049) | 2049 | `"    assert called == [\"filtered/primary\", \"fallback/model\"]"` | — |
| [SRC-F725E90B2A-L002050](../../tests/test_web_agent.py#L2050) | 2050 | `"    assert \"جزء جواب مفلتر\" not in result"` | — |
| [SRC-F725E90B2A-L002051](../../tests/test_web_agent.py#L2051) | 2051 | `""` | — |
| [SRC-F725E90B2A-L002052](../../tests/test_web_agent.py#L2052) | 2052 | `""` | — |
| [SRC-F725E90B2A-L002053](../../tests/test_web_agent.py#L2053) | 2053 | `"def test_reviewer_rejects_duplicate_final_answer_delimiters(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002054](../../tests/test_web_agent.py#L2054) | 2054 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002055](../../tests/test_web_agent.py#L2055) | 2055 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002056](../../tests/test_web_agent.py#L2056) | 2056 | `"    source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002057](../../tests/test_web_agent.py#L2057) | 2057 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002058](../../tests/test_web_agent.py#L2058) | 2058 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002059](../../tests/test_web_agent.py#L2059) | 2059 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L002060](../../tests/test_web_agent.py#L2060) | 2060 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-F725E90B2A-L002061](../../tests/test_web_agent.py#L2061) | 2061 | `"            \"<<<OMARAI_FINAL_ANSWER>>>تقرير مراجعة داخلي \""` | — |
| [SRC-F725E90B2A-L002062](../../tests/test_web_agent.py#L2062) | 2062 | `"            \"<<<OMARAI_FINAL_ANSWER>>>نص مزعوم\""` | — |
| [SRC-F725E90B2A-L002063](../../tests/test_web_agent.py#L2063) | 2063 | `"            \"<<<END_OMARAI_FINAL_ANSWER>>><<<END_OMARAI_FINAL_ANSWER>>>\""` | — |
| [SRC-F725E90B2A-L002064](../../tests/test_web_agent.py#L2064) | 2064 | `"        ),"` | — |
| [SRC-F725E90B2A-L002065](../../tests/test_web_agent.py#L2065) | 2065 | `"    )"` | — |
| [SRC-F725E90B2A-L002066](../../tests/test_web_agent.py#L2066) | 2066 | `""` | — |
| [SRC-F725E90B2A-L002067](../../tests/test_web_agent.py#L2067) | 2067 | `"    with pytest.raises(RuntimeError, match=\"فصل الإجابة النهائية\"):"` | — |
| [SRC-F725E90B2A-L002068](../../tests/test_web_agent.py#L2068) | 2068 | `"        agent._review_answer(\"ما مضمون الصفحة؟\", \"مسودة\", [source])"` | — |
| [SRC-F725E90B2A-L002069](../../tests/test_web_agent.py#L2069) | 2069 | `""` | — |
| [SRC-F725E90B2A-L002070](../../tests/test_web_agent.py#L2070) | 2070 | `""` | — |
| [SRC-F725E90B2A-L002071](../../tests/test_web_agent.py#L2071) | 2071 | `"def test_frontend_review_status_matches_api_contract():"` | — |
| [SRC-F725E90B2A-L002072](../../tests/test_web_agent.py#L2072) | 2072 | `"    html = (Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002073](../../tests/test_web_agent.py#L2073) | 2073 | `"    assert 'r.second_pass_review===\"model_claim_audit_completed\"' in html"` | — |
| [SRC-F725E90B2A-L002074](../../tests/test_web_agent.py#L2074) | 2074 | `"    assert 'r.second_pass_review===\"model_claim_audit_unavailable\"' in html"` | — |
| [SRC-F725E90B2A-L002075](../../tests/test_web_agent.py#L2075) | 2075 | `"    assert 'r.second_pass_review===\"model_second_pass_completed\"' not in html"` | — |
| [SRC-F725E90B2A-L002076](../../tests/test_web_agent.py#L2076) | 2076 | `"    assert 'r.second_pass_review===\"model_second_pass_unavailable\"' not in html"` | — |
| [SRC-F725E90B2A-L002077](../../tests/test_web_agent.py#L2077) | 2077 | `""` | — |
| [SRC-F725E90B2A-L002078](../../tests/test_web_agent.py#L2078) | 2078 | `""` | — |
| [SRC-F725E90B2A-L002079](../../tests/test_web_agent.py#L2079) | 2079 | `""` | — |
| [SRC-F725E90B2A-L002080](../../tests/test_web_agent.py#L2080) | 2080 | `"def test_research_error_preserves_confirmed_search_attempt_without_fabricating_counts(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002081](../../tests/test_web_agent.py#L2081) | 2081 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002082](../../tests/test_web_agent.py#L2082) | 2082 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002083](../../tests/test_web_agent.py#L2083) | 2083 | `"        \"queries\": [\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\"],"` | — |
| [SRC-F725E90B2A-L002084](../../tests/test_web_agent.py#L2084) | 2084 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002085](../../tests/test_web_agent.py#L2085) | 2085 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002086](../../tests/test_web_agent.py#L2086) | 2086 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L002087](../../tests/test_web_agent.py#L2087) | 2087 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002088](../../tests/test_web_agent.py#L2088) | 2088 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002089](../../tests/test_web_agent.py#L2089) | 2089 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002090](../../tests/test_web_agent.py#L2090) | 2090 | `"    }"` | — |
| [SRC-F725E90B2A-L002091](../../tests/test_web_agent.py#L2091) | 2091 | `""` | — |
| [SRC-F725E90B2A-L002092](../../tests/test_web_agent.py#L2092) | 2092 | `"    def failed_after_provider_result(research_plan):"` | — |
| [SRC-F725E90B2A-L002093](../../tests/test_web_agent.py#L2093) | 2093 | `"        # A completed provider result-processing state confirms that a search"` | — |
| [SRC-F725E90B2A-L002094](../../tests/test_web_agent.py#L2094) | 2094 | `"        # connector returned; the collector then fails during downstream processing."` | — |
| [SRC-F725E90B2A-L002095](../../tests/test_web_agent.py#L2095) | 2095 | `"        agent._record_provider_diagnostic("` | — |
| [SRC-F725E90B2A-L002096](../../tests/test_web_agent.py#L2096) | 2096 | `"            \"duckduckgo_html\","` | — |
| [SRC-F725E90B2A-L002097](../../tests/test_web_agent.py#L2097) | 2097 | `"            research_plan[\"queries\"][0],"` | — |
| [SRC-F725E90B2A-L002098](../../tests/test_web_agent.py#L2098) | 2098 | `"            \"ok\","` | — |
| [SRC-F725E90B2A-L002099](../../tests/test_web_agent.py#L2099) | 2099 | `"            result_count=1,"` | — |
| [SRC-F725E90B2A-L002100](../../tests/test_web_agent.py#L2100) | 2100 | `"        )"` | — |
| [SRC-F725E90B2A-L002101](../../tests/test_web_agent.py#L2101) | 2101 | `"        raise RuntimeError(\"simulated post-search pipeline failure\")"` | — |
| [SRC-F725E90B2A-L002102](../../tests/test_web_agent.py#L2102) | 2102 | `""` | — |
| [SRC-F725E90B2A-L002103](../../tests/test_web_agent.py#L2103) | 2103 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002104](../../tests/test_web_agent.py#L2104) | 2104 | `"    monkeypatch.setattr(agent, \"_collect_research\", failed_after_provider_result)"` | — |
| [SRC-F725E90B2A-L002105](../../tests/test_web_agent.py#L2105) | 2105 | `""` | — |
| [SRC-F725E90B2A-L002106](../../tests/test_web_agent.py#L2106) | 2106 | `"    result = agent.answer(\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\")"` | — |
| [SRC-F725E90B2A-L002107](../../tests/test_web_agent.py#L2107) | 2107 | `""` | — |
| [SRC-F725E90B2A-L002108](../../tests/test_web_agent.py#L2108) | 2108 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L002109](../../tests/test_web_agent.py#L2109) | 2109 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L002110](../../tests/test_web_agent.py#L2110) | 2110 | `"    assert report[\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L002111](../../tests/test_web_agent.py#L2111) | 2111 | `"    assert report[\"search_outcome\"] == \"attempted_research_error\""` | — |
| [SRC-F725E90B2A-L002112](../../tests/test_web_agent.py#L2112) | 2112 | `"    assert report[\"queries_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002113](../../tests/test_web_agent.py#L2113) | 2113 | `"    assert report[\"queries_attempted_known\"] is False"` | — |
| [SRC-F725E90B2A-L002114](../../tests/test_web_agent.py#L2114) | 2114 | `"    assert report[\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002115](../../tests/test_web_agent.py#L2115) | 2115 | `"    assert report[\"unique_sources\"] is None"` | — |
| [SRC-F725E90B2A-L002116](../../tests/test_web_agent.py#L2116) | 2116 | `"    assert report[\"pages_fetched\"] is None"` | — |
| [SRC-F725E90B2A-L002117](../../tests/test_web_agent.py#L2117) | 2117 | `""` | — |
| [SRC-F725E90B2A-L002118](../../tests/test_web_agent.py#L2118) | 2118 | `""` | — |
| [SRC-F725E90B2A-L002119](../../tests/test_web_agent.py#L2119) | 2119 | `"def test_research_error_without_provider_diagnostics_is_reported_as_unknown(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002120](../../tests/test_web_agent.py#L2120) | 2120 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002121](../../tests/test_web_agent.py#L2121) | 2121 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002122](../../tests/test_web_agent.py#L2122) | 2122 | `"        \"queries\": [\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\"],"` | — |
| [SRC-F725E90B2A-L002123](../../tests/test_web_agent.py#L2123) | 2123 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002124](../../tests/test_web_agent.py#L2124) | 2124 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002125](../../tests/test_web_agent.py#L2125) | 2125 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L002126](../../tests/test_web_agent.py#L2126) | 2126 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002127](../../tests/test_web_agent.py#L2127) | 2127 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002128](../../tests/test_web_agent.py#L2128) | 2128 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002129](../../tests/test_web_agent.py#L2129) | 2129 | `"    }"` | — |
| [SRC-F725E90B2A-L002130](../../tests/test_web_agent.py#L2130) | 2130 | `""` | — |
| [SRC-F725E90B2A-L002131](../../tests/test_web_agent.py#L2131) | 2131 | `"    def fail_before_attempt(research_plan):"` | — |
| [SRC-F725E90B2A-L002132](../../tests/test_web_agent.py#L2132) | 2132 | `"        raise RuntimeError(\"simulated scheduler failure\")"` | — |
| [SRC-F725E90B2A-L002133](../../tests/test_web_agent.py#L2133) | 2133 | `""` | — |
| [SRC-F725E90B2A-L002134](../../tests/test_web_agent.py#L2134) | 2134 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002135](../../tests/test_web_agent.py#L2135) | 2135 | `"    monkeypatch.setattr(agent, \"_collect_research\", fail_before_attempt)"` | — |
| [SRC-F725E90B2A-L002136](../../tests/test_web_agent.py#L2136) | 2136 | `""` | — |
| [SRC-F725E90B2A-L002137](../../tests/test_web_agent.py#L2137) | 2137 | `"    result = agent.answer(\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\")"` | — |
| [SRC-F725E90B2A-L002138](../../tests/test_web_agent.py#L2138) | 2138 | `""` | — |
| [SRC-F725E90B2A-L002139](../../tests/test_web_agent.py#L2139) | 2139 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L002140](../../tests/test_web_agent.py#L2140) | 2140 | `"    assert result[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002141](../../tests/test_web_agent.py#L2141) | 2141 | `"    assert report[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002142](../../tests/test_web_agent.py#L2142) | 2142 | `"    assert report[\"search_outcome\"] == \"unknown_after_research_error\""` | — |
| [SRC-F725E90B2A-L002143](../../tests/test_web_agent.py#L2143) | 2143 | `"    assert report[\"queries_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002144](../../tests/test_web_agent.py#L2144) | 2144 | `"    assert report[\"queries_attempted_known\"] is False"` | — |
| [SRC-F725E90B2A-L002145](../../tests/test_web_agent.py#L2145) | 2145 | `"    assert report[\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002146](../../tests/test_web_agent.py#L2146) | 2146 | `""` | — |
| [SRC-F725E90B2A-L002147](../../tests/test_web_agent.py#L2147) | 2147 | `""` | — |
| [SRC-F725E90B2A-L002148](../../tests/test_web_agent.py#L2148) | 2148 | `"def test_general_answer_does_not_silently_slice_overlong_model_output(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002149](../../tests/test_web_agent.py#L2149) | 2149 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002150](../../tests/test_web_agent.py#L2150) | 2150 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002151](../../tests/test_web_agent.py#L2151) | 2151 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002152](../../tests/test_web_agent.py#L2152) | 2152 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002153](../../tests/test_web_agent.py#L2153) | 2153 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L002154](../../tests/test_web_agent.py#L2154) | 2154 | `"        lambda *args, **kwargs: \"ن\" * 24_001,"` | — |
| [SRC-F725E90B2A-L002155](../../tests/test_web_agent.py#L2155) | 2155 | `"    )"` | — |
| [SRC-F725E90B2A-L002156](../../tests/test_web_agent.py#L2156) | 2156 | `""` | — |
| [SRC-F725E90B2A-L002157](../../tests/test_web_agent.py#L2157) | 2157 | `"    result = agent._answer_without_search(\"اشرح مفهومًا عامًا\", [])"` | — |
| [SRC-F725E90B2A-L002158](../../tests/test_web_agent.py#L2158) | 2158 | `""` | — |
| [SRC-F725E90B2A-L002159](../../tests/test_web_agent.py#L2159) | 2159 | `"    assert result is None"` | — |
| [SRC-F725E90B2A-L002160](../../tests/test_web_agent.py#L2160) | 2160 | `""` | — |
| [SRC-F725E90B2A-L002161](../../tests/test_web_agent.py#L2161) | 2161 | `""` | — |
| [SRC-F725E90B2A-L002162](../../tests/test_web_agent.py#L2162) | 2162 | `"def test_frontend_discloses_unknown_counts_after_research_error():"` | — |
| [SRC-F725E90B2A-L002163](../../tests/test_web_agent.py#L2163) | 2163 | `"    html = (Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002164](../../tests/test_web_agent.py#L2164) | 2164 | `"    assert '[\"attempted_research_error\",\"unknown_after_research_error\"].includes(r.search_outcome)' in html"` | — |
| [SRC-F725E90B2A-L002165](../../tests/test_web_agent.py#L2165) | 2165 | `"    assert \"لم يمكن تحديد عدد المصادر القابلة للاستخدام\" in html"` | — |
| [SRC-F725E90B2A-L002166](../../tests/test_web_agent.py#L2166) | 2166 | `"    assert \"غير محدد\" in html"` | — |
| [SRC-F725E90B2A-L002167](../../tests/test_web_agent.py#L2167) | 2167 | `"    assert 'const score=(researchErrorOutcome\|\|lead)?null:Number(e.coverage_score\|\|0)' not in html"` | — |
| [SRC-F725E90B2A-L002168](../../tests/test_web_agent.py#L2168) | 2168 | `"    assert \"مؤشر تغطية البحث:\" not in html"` | — |
| [SRC-F725E90B2A-L002169](../../tests/test_web_agent.py#L2169) | 2169 | `"    assert '\"تغطية الأدلة: \"+scoreLabel' in html"` | — |
| [SRC-F725E90B2A-L002170](../../tests/test_web_agent.py#L2170) | 2170 | `"    assert \"يصف هذا الوصف اتساع الأدلة المتاحة ولا يمثل احتمال صحة الإجابة\" in html"` | — |
| [SRC-F725E90B2A-L002171](../../tests/test_web_agent.py#L2171) | 2171 | `"    assert \"تعذر تحديد تغطية البحث لأن مسار تجميع الأدلة لم يكتمل\" in html"` | — |
| [SRC-F725E90B2A-L002172](../../tests/test_web_agent.py#L2172) | 2172 | `""` | — |
| [SRC-F725E90B2A-L002173](../../tests/test_web_agent.py#L2173) | 2173 | `""` | — |
| [SRC-F725E90B2A-L002174](../../tests/test_web_agent.py#L2174) | 2174 | `"def test_generic_provider_failure_does_not_claim_search_attempt_as_confirmed(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002175](../../tests/test_web_agent.py#L2175) | 2175 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002176](../../tests/test_web_agent.py#L2176) | 2176 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002177](../../tests/test_web_agent.py#L2177) | 2177 | `"        \"queries\": [\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\"],"` | — |
| [SRC-F725E90B2A-L002178](../../tests/test_web_agent.py#L2178) | 2178 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002179](../../tests/test_web_agent.py#L2179) | 2179 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002180](../../tests/test_web_agent.py#L2180) | 2180 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L002181](../../tests/test_web_agent.py#L2181) | 2181 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002182](../../tests/test_web_agent.py#L2182) | 2182 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002183](../../tests/test_web_agent.py#L2183) | 2183 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002184](../../tests/test_web_agent.py#L2184) | 2184 | `"    }"` | — |
| [SRC-F725E90B2A-L002185](../../tests/test_web_agent.py#L2185) | 2185 | `""` | — |
| [SRC-F725E90B2A-L002186](../../tests/test_web_agent.py#L2186) | 2186 | `"    def fail_after_generic_provider_error(research_plan):"` | — |
| [SRC-F725E90B2A-L002187](../../tests/test_web_agent.py#L2187) | 2187 | `"        # A generic failed diagnostic does not prove whether the network request"` | — |
| [SRC-F725E90B2A-L002188](../../tests/test_web_agent.py#L2188) | 2188 | `"        # was actually sent; it must not be upgraded to a confirmed attempt."` | — |
| [SRC-F725E90B2A-L002189](../../tests/test_web_agent.py#L2189) | 2189 | `"        agent._record_provider_diagnostic("` | — |
| [SRC-F725E90B2A-L002190](../../tests/test_web_agent.py#L2190) | 2190 | `"            \"duckduckgo_html\","` | — |
| [SRC-F725E90B2A-L002191](../../tests/test_web_agent.py#L2191) | 2191 | `"            research_plan[\"queries\"][0],"` | — |
| [SRC-F725E90B2A-L002192](../../tests/test_web_agent.py#L2192) | 2192 | `"            \"failed\","` | — |
| [SRC-F725E90B2A-L002193](../../tests/test_web_agent.py#L2193) | 2193 | `"            error=\"simulated failure before request send\","` | — |
| [SRC-F725E90B2A-L002194](../../tests/test_web_agent.py#L2194) | 2194 | `"        )"` | — |
| [SRC-F725E90B2A-L002195](../../tests/test_web_agent.py#L2195) | 2195 | `"        raise RuntimeError(\"simulated research pipeline failure\")"` | — |
| [SRC-F725E90B2A-L002196](../../tests/test_web_agent.py#L2196) | 2196 | `""` | — |
| [SRC-F725E90B2A-L002197](../../tests/test_web_agent.py#L2197) | 2197 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002198](../../tests/test_web_agent.py#L2198) | 2198 | `"    monkeypatch.setattr(agent, \"_collect_research\", fail_after_generic_provider_error)"` | — |
| [SRC-F725E90B2A-L002199](../../tests/test_web_agent.py#L2199) | 2199 | `""` | — |
| [SRC-F725E90B2A-L002200](../../tests/test_web_agent.py#L2200) | 2200 | `"    result = agent.answer(\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\")"` | — |
| [SRC-F725E90B2A-L002201](../../tests/test_web_agent.py#L2201) | 2201 | `""` | — |
| [SRC-F725E90B2A-L002202](../../tests/test_web_agent.py#L2202) | 2202 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L002203](../../tests/test_web_agent.py#L2203) | 2203 | `"    assert result[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002204](../../tests/test_web_agent.py#L2204) | 2204 | `"    assert report[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002205](../../tests/test_web_agent.py#L2205) | 2205 | `"    assert report[\"search_outcome\"] == \"unknown_after_research_error\""` | — |
| [SRC-F725E90B2A-L002206](../../tests/test_web_agent.py#L2206) | 2206 | `"    assert report[\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002207](../../tests/test_web_agent.py#L2207) | 2207 | `"    assert report[\"unique_sources\"] is None"` | — |
| [SRC-F725E90B2A-L002208](../../tests/test_web_agent.py#L2208) | 2208 | `""` | — |
| [SRC-F725E90B2A-L002209](../../tests/test_web_agent.py#L2209) | 2209 | `""` | — |
| [SRC-F725E90B2A-L002210](../../tests/test_web_agent.py#L2210) | 2210 | `""` | — |
| [SRC-F725E90B2A-L002211](../../tests/test_web_agent.py#L2211) | 2211 | `"def test_diagnostics_tries_fallback_probe_when_first_probe_has_no_results(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002212](../../tests/test_web_agent.py#L2212) | 2212 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002213](../../tests/test_web_agent.py#L2213) | 2213 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L002214](../../tests/test_web_agent.py#L2214) | 2214 | `""` | — |
| [SRC-F725E90B2A-L002215](../../tests/test_web_agent.py#L2215) | 2215 | `"    def search(query):"` | — |
| [SRC-F725E90B2A-L002216](../../tests/test_web_agent.py#L2216) | 2216 | `"        calls.append(query)"` | — |
| [SRC-F725E90B2A-L002217](../../tests/test_web_agent.py#L2217) | 2217 | `"        if len(calls) == 1:"` | — |
| [SRC-F725E90B2A-L002218](../../tests/test_web_agent.py#L2218) | 2218 | `"            return []"` | — |
| [SRC-F725E90B2A-L002219](../../tests/test_web_agent.py#L2219) | 2219 | `"        return ["` | — |
| [SRC-F725E90B2A-L002220](../../tests/test_web_agent.py#L2220) | 2220 | `"            {"` | — |
| [SRC-F725E90B2A-L002221](../../tests/test_web_agent.py#L2221) | 2221 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-F725E90B2A-L002222](../../tests/test_web_agent.py#L2222) | 2222 | `"                \"title\": \"OpenAI official website\","` | — |
| [SRC-F725E90B2A-L002223](../../tests/test_web_agent.py#L2223) | 2223 | `"                \"url\": \"https://openai.com/\","` | — |
| [SRC-F725E90B2A-L002224](../../tests/test_web_agent.py#L2224) | 2224 | `"                \"snippet\": \"Official website and products\","` | — |
| [SRC-F725E90B2A-L002225](../../tests/test_web_agent.py#L2225) | 2225 | `"            }"` | — |
| [SRC-F725E90B2A-L002226](../../tests/test_web_agent.py#L2226) | 2226 | `"        ]"` | — |
| [SRC-F725E90B2A-L002227](../../tests/test_web_agent.py#L2227) | 2227 | `""` | — |
| [SRC-F725E90B2A-L002228](../../tests/test_web_agent.py#L2228) | 2228 | `"    monkeypatch.setattr(agent, \"_search_web\", search)"` | — |
| [SRC-F725E90B2A-L002229](../../tests/test_web_agent.py#L2229) | 2229 | `"    monkeypatch.setattr(agent, \"_request_completion\", lambda *args, **kwargs: \"OK\")"` | — |
| [SRC-F725E90B2A-L002230](../../tests/test_web_agent.py#L2230) | 2230 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002231](../../tests/test_web_agent.py#L2231) | 2231 | `""` | — |
| [SRC-F725E90B2A-L002232](../../tests/test_web_agent.py#L2232) | 2232 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L002233](../../tests/test_web_agent.py#L2233) | 2233 | `""` | — |
| [SRC-F725E90B2A-L002234](../../tests/test_web_agent.py#L2234) | 2234 | `"    assert len(calls) == 2"` | — |
| [SRC-F725E90B2A-L002235](../../tests/test_web_agent.py#L2235) | 2235 | `"    assert report[\"checks\"][\"web_search\"][\"status\"] == \"passed\""` | — |
| [SRC-F725E90B2A-L002236](../../tests/test_web_agent.py#L2236) | 2236 | `"    assert report[\"checks\"][\"web_search\"][\"probe_count\"] == 2"` | — |
| [SRC-F725E90B2A-L002237](../../tests/test_web_agent.py#L2237) | 2237 | `"    assert report[\"checks\"][\"web_search\"][\"result_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002238](../../tests/test_web_agent.py#L2238) | 2238 | `""` | — |
| [SRC-F725E90B2A-L002239](../../tests/test_web_agent.py#L2239) | 2239 | `""` | — |
| [SRC-F725E90B2A-L002240](../../tests/test_web_agent.py#L2240) | 2240 | `"def test_lead_discovery_is_distinct_from_listing_search():"` | — |
| [SRC-F725E90B2A-L002241](../../tests/test_web_agent.py#L2241) | 2241 | `"    assert WebAgent._is_lead_search(\"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية\")"` | — |
| [SRC-F725E90B2A-L002242](../../tests/test_web_agent.py#L2242) | 2242 | `"    assert WebAgent._is_lead_search(\"Find buyers looking to buy apartments\")"` | — |
| [SRC-F725E90B2A-L002243](../../tests/test_web_agent.py#L2243) | 2243 | `"    assert not WebAgent._is_lead_search(\"ابحث عن شقق للبيع في العاصمة الإدارية\")"` | — |
| [SRC-F725E90B2A-L002244](../../tests/test_web_agent.py#L2244) | 2244 | `"    assert not WebAgent._is_lead_search(\"Find apartments for sale\")"` | — |
| [SRC-F725E90B2A-L002245](../../tests/test_web_agent.py#L2245) | 2245 | `""` | — |
| [SRC-F725E90B2A-L002246](../../tests/test_web_agent.py#L2246) | 2246 | `""` | — |
| [SRC-F725E90B2A-L002247](../../tests/test_web_agent.py#L2247) | 2247 | `"def test_buyer_intent_evidence_requires_explicit_purchase_signal():"` | — |
| [SRC-F725E90B2A-L002248](../../tests/test_web_agent.py#L2248) | 2248 | `"    listing = {"` | — |
| [SRC-F725E90B2A-L002249](../../tests/test_web_agent.py#L2249) | 2249 | `"        \"title\": \"شقق للبيع في العاصمة الإدارية الجديدة\","` | — |
| [SRC-F725E90B2A-L002250](../../tests/test_web_agent.py#L2250) | 2250 | `"        \"snippet\": \"أفضل شقق للبيع بالتقسيط\","` | — |
| [SRC-F725E90B2A-L002251](../../tests/test_web_agent.py#L2251) | 2251 | `"        \"page_text\": \"إعلانات وحدات سكنية للبيع بمساحات مختلفة.\","` | — |
| [SRC-F725E90B2A-L002252](../../tests/test_web_agent.py#L2252) | 2252 | `"    }"` | — |
| [SRC-F725E90B2A-L002253](../../tests/test_web_agent.py#L2253) | 2253 | `"    buyer_post = {"` | — |
| [SRC-F725E90B2A-L002254](../../tests/test_web_agent.py#L2254) | 2254 | `"        \"title\": \"بدور على شقة تمليك في العاصمة الإدارية\","` | — |
| [SRC-F725E90B2A-L002255](../../tests/test_web_agent.py#L2255) | 2255 | `"        \"snippet\": \"مطلوب شقة تمليك في العاصمة الإدارية.\","` | — |
| [SRC-F725E90B2A-L002256](../../tests/test_web_agent.py#L2256) | 2256 | `"        \"page_text\": \"أنا بدور على شقة تمليك في العاصمة الإدارية وعايز أشتري خلال شهر.\","` | — |
| [SRC-F725E90B2A-L002257](../../tests/test_web_agent.py#L2257) | 2257 | `"    }"` | — |
| [SRC-F725E90B2A-L002258](../../tests/test_web_agent.py#L2258) | 2258 | `"    assert WebAgent._lead_intent_evidence(listing) is None"` | — |
| [SRC-F725E90B2A-L002259](../../tests/test_web_agent.py#L2259) | 2259 | `"    signal = WebAgent._lead_intent_evidence(buyer_post)"` | — |
| [SRC-F725E90B2A-L002260](../../tests/test_web_agent.py#L2260) | 2260 | `"    assert signal is not None"` | — |
| [SRC-F725E90B2A-L002261](../../tests/test_web_agent.py#L2261) | 2261 | `"    assert signal[\"basis\"] == \"page_text\""` | — |
| [SRC-F725E90B2A-L002262](../../tests/test_web_agent.py#L2262) | 2262 | `""` | — |
| [SRC-F725E90B2A-L002263](../../tests/test_web_agent.py#L2263) | 2263 | `""` | — |
| [SRC-F725E90B2A-L002264](../../tests/test_web_agent.py#L2264) | 2264 | `"def test_lead_generation_does_not_present_sale_listings_as_buyers(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002265](../../tests/test_web_agent.py#L2265) | 2265 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002266](../../tests/test_web_agent.py#L2266) | 2266 | `"    question = \"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\""` | — |
| [SRC-F725E90B2A-L002267](../../tests/test_web_agent.py#L2267) | 2267 | `"    source_a = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002268](../../tests/test_web_agent.py#L2268) | 2268 | `"    source_a.update({"` | — |
| [SRC-F725E90B2A-L002269](../../tests/test_web_agent.py#L2269) | 2269 | `"        \"title\": \"شقق للبيع في العاصمة الإدارية الجديدة\","` | — |
| [SRC-F725E90B2A-L002270](../../tests/test_web_agent.py#L2270) | 2270 | `"        \"snippet\": \"قارن أسعار الشقق والمساحات وخطط السداد.\","` | — |
| [SRC-F725E90B2A-L002271](../../tests/test_web_agent.py#L2271) | 2271 | `"        \"page_text\": \"إعلانات شقق للبيع من شركات تطوير عقاري.\","` | — |
| [SRC-F725E90B2A-L002272](../../tests/test_web_agent.py#L2272) | 2272 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002273](../../tests/test_web_agent.py#L2273) | 2273 | `"    })"` | — |
| [SRC-F725E90B2A-L002274](../../tests/test_web_agent.py#L2274) | 2274 | `"    source_b = sample_source(1)"` | — |
| [SRC-F725E90B2A-L002275](../../tests/test_web_agent.py#L2275) | 2275 | `"    source_b.update({"` | — |
| [SRC-F725E90B2A-L002276](../../tests/test_web_agent.py#L2276) | 2276 | `"        \"title\": \"مشروعات عقارية في العاصمة الإدارية\","` | — |
| [SRC-F725E90B2A-L002277](../../tests/test_web_agent.py#L2277) | 2277 | `"        \"snippet\": \"تعرف على الوحدات السكنية المتاحة للبيع.\","` | — |
| [SRC-F725E90B2A-L002278](../../tests/test_web_agent.py#L2278) | 2278 | `"        \"page_text\": \"معلومات عامة عن مشروعات وشقق للبيع.\","` | — |
| [SRC-F725E90B2A-L002279](../../tests/test_web_agent.py#L2279) | 2279 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002280](../../tests/test_web_agent.py#L2280) | 2280 | `"    })"` | — |
| [SRC-F725E90B2A-L002281](../../tests/test_web_agent.py#L2281) | 2281 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002282](../../tests/test_web_agent.py#L2282) | 2282 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002283](../../tests/test_web_agent.py#L2283) | 2283 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002284](../../tests/test_web_agent.py#L2284) | 2284 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002285](../../tests/test_web_agent.py#L2285) | 2285 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002286](../../tests/test_web_agent.py#L2286) | 2286 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002287](../../tests/test_web_agent.py#L2287) | 2287 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002288](../../tests/test_web_agent.py#L2288) | 2288 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002289](../../tests/test_web_agent.py#L2289) | 2289 | `"    }"` | — |
| [SRC-F725E90B2A-L002290](../../tests/test_web_agent.py#L2290) | 2290 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda q, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002291](../../tests/test_web_agent.py#L2291) | 2291 | `"    monkeypatch.setattr(agent, \"_collect_research\", lambda p: ("` | — |
| [SRC-F725E90B2A-L002292](../../tests/test_web_agent.py#L2292) | 2292 | `"        [source_a, source_b], [], {"` | — |
| [SRC-F725E90B2A-L002293](../../tests/test_web_agent.py#L2293) | 2293 | `"            \"queries_planned\": 1, \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L002294](../../tests/test_web_agent.py#L2294) | 2294 | `"            \"query_results\": [{\"query\": question, \"results\": 2}],"` | — |
| [SRC-F725E90B2A-L002295](../../tests/test_web_agent.py#L2295) | 2295 | `"            \"unique_sources\": 2, \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L002296](../../tests/test_web_agent.py#L2296) | 2296 | `"            \"providers_used\": [\"test_provider\"], \"provider_counts\": {\"test_provider\": 2},"` | — |
| [SRC-F725E90B2A-L002297](../../tests/test_web_agent.py#L2297) | 2297 | `"            \"platform_counts\": {\"web\": 2}, \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002298](../../tests/test_web_agent.py#L2298) | 2298 | `"            \"depth\": \"standard\", \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002299](../../tests/test_web_agent.py#L2299) | 2299 | `"        }"` | — |
| [SRC-F725E90B2A-L002300](../../tests/test_web_agent.py#L2300) | 2300 | `"    ))"` | — |
| [SRC-F725E90B2A-L002301](../../tests/test_web_agent.py#L2301) | 2301 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002302](../../tests/test_web_agent.py#L2302) | 2302 | `"        agent, \"_generate\","` | — |
| [SRC-F725E90B2A-L002303](../../tests/test_web_agent.py#L2303) | 2303 | `"        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError(\"must not synthesize false leads\")),"` | — |
| [SRC-F725E90B2A-L002304](../../tests/test_web_agent.py#L2304) | 2304 | `"    )"` | — |
| [SRC-F725E90B2A-L002305](../../tests/test_web_agent.py#L2305) | 2305 | `""` | — |
| [SRC-F725E90B2A-L002306](../../tests/test_web_agent.py#L2306) | 2306 | `"    result = agent.answer(question)"` | — |
| [SRC-F725E90B2A-L002307](../../tests/test_web_agent.py#L2307) | 2307 | `""` | — |
| [SRC-F725E90B2A-L002308](../../tests/test_web_agent.py#L2308) | 2308 | `"    assert result[\"intent_route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-F725E90B2A-L002309](../../tests/test_web_agent.py#L2309) | 2309 | `"    assert result[\"kind\"] == \"lead_discovery_no_qualified_candidates\""` | — |
| [SRC-F725E90B2A-L002310](../../tests/test_web_agent.py#L2310) | 2310 | `"    assert result[\"search_report\"][\"lead_generation\"][\"candidate_signal_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002311](../../tests/test_web_agent.py#L2311) | 2311 | `"    assert result[\"search_report\"][\"lead_generation\"][\"related_results_reviewed\"] == 2"` | — |
| [SRC-F725E90B2A-L002312](../../tests/test_web_agent.py#L2312) | 2312 | `"    assert \"لم أعتبر إعلانات البيع\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L002313](../../tests/test_web_agent.py#L2313) | 2313 | `"    assert all(s[\"lead_qualification\"] == \"related_result_not_lead\" for s in result[\"sources\"])"` | — |
| [SRC-F725E90B2A-L002314](../../tests/test_web_agent.py#L2314) | 2314 | `""` | — |
| [SRC-F725E90B2A-L002315](../../tests/test_web_agent.py#L2315) | 2315 | `""` | — |
| [SRC-F725E90B2A-L002316](../../tests/test_web_agent.py#L2316) | 2316 | `"def test_lead_generation_search_plan_includes_high_intent_queries(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002317](../../tests/test_web_agent.py#L2317) | 2317 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002318](../../tests/test_web_agent.py#L2318) | 2318 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002319](../../tests/test_web_agent.py#L2319) | 2319 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002320](../../tests/test_web_agent.py#L2320) | 2320 | `"        \"queries\": [\"generic apartment listings\"],"` | — |
| [SRC-F725E90B2A-L002321](../../tests/test_web_agent.py#L2321) | 2321 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002322](../../tests/test_web_agent.py#L2322) | 2322 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002323](../../tests/test_web_agent.py#L2323) | 2323 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002324](../../tests/test_web_agent.py#L2324) | 2324 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002325](../../tests/test_web_agent.py#L2325) | 2325 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002326](../../tests/test_web_agent.py#L2326) | 2326 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002327](../../tests/test_web_agent.py#L2327) | 2327 | `"    }"` | — |
| [SRC-F725E90B2A-L002328](../../tests/test_web_agent.py#L2328) | 2328 | `""` | — |
| [SRC-F725E90B2A-L002329](../../tests/test_web_agent.py#L2329) | 2329 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L002330](../../tests/test_web_agent.py#L2330) | 2330 | `"        seen.update(research_plan)"` | — |
| [SRC-F725E90B2A-L002331](../../tests/test_web_agent.py#L2331) | 2331 | `"        source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002332](../../tests/test_web_agent.py#L2332) | 2332 | `"        source.update({"` | — |
| [SRC-F725E90B2A-L002333](../../tests/test_web_agent.py#L2333) | 2333 | `"            \"title\": \"مطلوب شقة تمليك في العاصمة الإدارية\","` | — |
| [SRC-F725E90B2A-L002334](../../tests/test_web_agent.py#L2334) | 2334 | `"            \"snippet\": \"صاحب المنشور يبحث عن شقة للشراء\","` | — |
| [SRC-F725E90B2A-L002335](../../tests/test_web_agent.py#L2335) | 2335 | `"            \"page_text\": \"مطلوب شقة تمليك في العاصمة الإدارية، أريد الشراء.\","` | — |
| [SRC-F725E90B2A-L002336](../../tests/test_web_agent.py#L2336) | 2336 | `"            \"queries\": list(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002337](../../tests/test_web_agent.py#L2337) | 2337 | `"        })"` | — |
| [SRC-F725E90B2A-L002338](../../tests/test_web_agent.py#L2338) | 2338 | `"        return [source], [], {"` | — |
| [SRC-F725E90B2A-L002339](../../tests/test_web_agent.py#L2339) | 2339 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002340](../../tests/test_web_agent.py#L2340) | 2340 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002341](../../tests/test_web_agent.py#L2341) | 2341 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L002342](../../tests/test_web_agent.py#L2342) | 2342 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L002343](../../tests/test_web_agent.py#L2343) | 2343 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L002344](../../tests/test_web_agent.py#L2344) | 2344 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L002345](../../tests/test_web_agent.py#L2345) | 2345 | `"            \"provider_counts\": {\"test_provider\": 1},"` | — |
| [SRC-F725E90B2A-L002346](../../tests/test_web_agent.py#L2346) | 2346 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L002347](../../tests/test_web_agent.py#L2347) | 2347 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002348](../../tests/test_web_agent.py#L2348) | 2348 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002349](../../tests/test_web_agent.py#L2349) | 2349 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002350](../../tests/test_web_agent.py#L2350) | 2350 | `"        }"` | — |
| [SRC-F725E90B2A-L002351](../../tests/test_web_agent.py#L2351) | 2351 | `""` | — |
| [SRC-F725E90B2A-L002352](../../tests/test_web_agent.py#L2352) | 2352 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda q, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002353](../../tests/test_web_agent.py#L2353) | 2353 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L002354](../../tests/test_web_agent.py#L2354) | 2354 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"عُثر على إشارة علنية محتملة [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L002355](../../tests/test_web_agent.py#L2355) | 2355 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L002356](../../tests/test_web_agent.py#L2356) | 2356 | `""` | — |
| [SRC-F725E90B2A-L002357](../../tests/test_web_agent.py#L2357) | 2357 | `"    result = agent.answer(\"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\")"` | — |
| [SRC-F725E90B2A-L002358](../../tests/test_web_agent.py#L2358) | 2358 | `""` | — |
| [SRC-F725E90B2A-L002359](../../tests/test_web_agent.py#L2359) | 2359 | `"    assert result[\"intent_route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-F725E90B2A-L002360](../../tests/test_web_agent.py#L2360) | 2360 | `"    assert seen[\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L002361](../../tests/test_web_agent.py#L2361) | 2361 | `"    assert len(seen[\"queries\"]) >= 4"` | — |
| [SRC-F725E90B2A-L002362](../../tests/test_web_agent.py#L2362) | 2362 | `"    assert any('\"مطلوب شراء\"' in q or '\"مطلوب شقه تمليك\"' in q for q in seen[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002363](../../tests/test_web_agent.py#L2363) | 2363 | `"    assert result[\"search_report\"][\"lead_generation\"][\"candidate_signal_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002364](../../tests/test_web_agent.py#L2364) | 2364 | `"    assert result[\"sources\"][0][\"lead_qualification\"] == \"public_buyer_intent_signal\""` | — |
| [SRC-F725E90B2A-L002365](../../tests/test_web_agent.py#L2365) | 2365 | `""` | — |
| [SRC-F725E90B2A-L002366](../../tests/test_web_agent.py#L2366) | 2366 | `""` | — |
| [SRC-F725E90B2A-L002367](../../tests/test_web_agent.py#L2367) | 2367 | `"def test_deepseek_search_adapter_normalizes_results_without_exposing_api_key(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002368](../../tests/test_web_agent.py#L2368) | 2368 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002369](../../tests/test_web_agent.py#L2369) | 2369 | `""` | — |
| [SRC-F725E90B2A-L002370](../../tests/test_web_agent.py#L2370) | 2370 | `"    monkeypatch.setenv(\"DEEPSEEK_SEARCH_API_KEY\", \"test-secret-key-that-must-not-appear\")"` | — |
| [SRC-F725E90B2A-L002371](../../tests/test_web_agent.py#L2371) | 2371 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002372](../../tests/test_web_agent.py#L2372) | 2372 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002373](../../tests/test_web_agent.py#L2373) | 2373 | `""` | — |
| [SRC-F725E90B2A-L002374](../../tests/test_web_agent.py#L2374) | 2374 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L002375](../../tests/test_web_agent.py#L2375) | 2375 | `"        def raise_for_status(self):"` | — |
| [SRC-F725E90B2A-L002376](../../tests/test_web_agent.py#L2376) | 2376 | `"            return None"` | — |
| [SRC-F725E90B2A-L002377](../../tests/test_web_agent.py#L2377) | 2377 | `""` | — |
| [SRC-F725E90B2A-L002378](../../tests/test_web_agent.py#L2378) | 2378 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L002379](../../tests/test_web_agent.py#L2379) | 2379 | `"            return {"` | — |
| [SRC-F725E90B2A-L002380](../../tests/test_web_agent.py#L2380) | 2380 | `"                \"results\": [{"` | — |
| [SRC-F725E90B2A-L002381](../../tests/test_web_agent.py#L2381) | 2381 | `"                    \"title\": \"Buyer wanted\","` | — |
| [SRC-F725E90B2A-L002382](../../tests/test_web_agent.py#L2382) | 2382 | `"                    \"url\": \"https://example.com/buyer\","` | — |
| [SRC-F725E90B2A-L002383](../../tests/test_web_agent.py#L2383) | 2383 | `"                    \"snippet\": \"Looking to buy a flat.\","` | — |
| [SRC-F725E90B2A-L002384](../../tests/test_web_agent.py#L2384) | 2384 | `"                    \"summary\": \"Looking to buy a flat in the requested area.\","` | — |
| [SRC-F725E90B2A-L002385](../../tests/test_web_agent.py#L2385) | 2385 | `"                    \"date\": \"2026-10-16T12:00:00Z\","` | — |
| [SRC-F725E90B2A-L002386](../../tests/test_web_agent.py#L2386) | 2386 | `"                    \"site_name\": \"Example\","` | — |
| [SRC-F725E90B2A-L002387](../../tests/test_web_agent.py#L2387) | 2387 | `"                    \"rerank_score\": 2.2,"` | — |
| [SRC-F725E90B2A-L002388](../../tests/test_web_agent.py#L2388) | 2388 | `"                    \"authority\": 2,"` | — |
| [SRC-F725E90B2A-L002389](../../tests/test_web_agent.py#L2389) | 2389 | `"                }]"` | — |
| [SRC-F725E90B2A-L002390](../../tests/test_web_agent.py#L2390) | 2390 | `"            }"` | — |
| [SRC-F725E90B2A-L002391](../../tests/test_web_agent.py#L2391) | 2391 | `""` | — |
| [SRC-F725E90B2A-L002392](../../tests/test_web_agent.py#L2392) | 2392 | `"    def fake_post(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002393](../../tests/test_web_agent.py#L2393) | 2393 | `"        seen[\"url\"] = url"` | — |
| [SRC-F725E90B2A-L002394](../../tests/test_web_agent.py#L2394) | 2394 | `"        seen.update(kwargs)"` | — |
| [SRC-F725E90B2A-L002395](../../tests/test_web_agent.py#L2395) | 2395 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L002396](../../tests/test_web_agent.py#L2396) | 2396 | `""` | — |
| [SRC-F725E90B2A-L002397](../../tests/test_web_agent.py#L2397) | 2397 | `"    monkeypatch.setattr(httpx, \"post\", fake_post)"` | — |
| [SRC-F725E90B2A-L002398](../../tests/test_web_agent.py#L2398) | 2398 | `"    rows = agent._search_deepseek_api(\"buyers looking to buy a flat\")"` | — |
| [SRC-F725E90B2A-L002399](../../tests/test_web_agent.py#L2399) | 2399 | `""` | — |
| [SRC-F725E90B2A-L002400](../../tests/test_web_agent.py#L2400) | 2400 | `"    assert seen[\"url\"] == \"https://api.deepseek.com/v1/tools/search\""` | — |
| [SRC-F725E90B2A-L002401](../../tests/test_web_agent.py#L2401) | 2401 | `"    assert seen[\"headers\"][\"Authorization\"] == \"Bearer test-secret-key-that-must-not-appear\""` | — |
| [SRC-F725E90B2A-L002402](../../tests/test_web_agent.py#L2402) | 2402 | `"    assert seen[\"json\"][\"count\"] == 6"` | — |
| [SRC-F725E90B2A-L002403](../../tests/test_web_agent.py#L2403) | 2403 | `"    assert rows[0][\"provider\"] == \"deepseek_search_api\""` | — |
| [SRC-F725E90B2A-L002404](../../tests/test_web_agent.py#L2404) | 2404 | `"    assert rows[0][\"snippet\"] == \"Looking to buy a flat in the requested area.\""` | — |
| [SRC-F725E90B2A-L002405](../../tests/test_web_agent.py#L2405) | 2405 | `"    assert rows[0][\"provider_rerank_score\"] == 2.2"` | — |
| [SRC-F725E90B2A-L002406](../../tests/test_web_agent.py#L2406) | 2406 | `"    assert \"test-secret-key-that-must-not-appear\" not in str(rows)"` | — |
| [SRC-F725E90B2A-L002407](../../tests/test_web_agent.py#L2407) | 2407 | `""` | — |
| [SRC-F725E90B2A-L002408](../../tests/test_web_agent.py#L2408) | 2408 | `""` | — |
| [SRC-F725E90B2A-L002409](../../tests/test_web_agent.py#L2409) | 2409 | `""` | — |
| [SRC-F725E90B2A-L002410](../../tests/test_web_agent.py#L2410) | 2410 | `"def test_diagnostics_distinguishes_connector_response_without_matches_from_offline(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002411](../../tests/test_web_agent.py#L2411) | 2411 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002412](../../tests/test_web_agent.py#L2412) | 2412 | `"    monkeypatch.setattr(agent, \"_request_completion\", lambda *args, **kwargs: \"OK\")"` | — |
| [SRC-F725E90B2A-L002413](../../tests/test_web_agent.py#L2413) | 2413 | `""` | — |
| [SRC-F725E90B2A-L002414](../../tests/test_web_agent.py#L2414) | 2414 | `"    def completed_empty_search(query):"` | — |
| [SRC-F725E90B2A-L002415](../../tests/test_web_agent.py#L2415) | 2415 | `"        agent._record_provider_diagnostic("` | — |
| [SRC-F725E90B2A-L002416](../../tests/test_web_agent.py#L2416) | 2416 | `"            \"bing_rss\", query, \"no_results\", result_count=0,"` | — |
| [SRC-F725E90B2A-L002417](../../tests/test_web_agent.py#L2417) | 2417 | `"            error=\"connector completed but returned no parseable results\","` | — |
| [SRC-F725E90B2A-L002418](../../tests/test_web_agent.py#L2418) | 2418 | `"        )"` | — |
| [SRC-F725E90B2A-L002419](../../tests/test_web_agent.py#L2419) | 2419 | `"        raise RuntimeError(\"no usable search matches\")"` | — |
| [SRC-F725E90B2A-L002420](../../tests/test_web_agent.py#L2420) | 2420 | `""` | — |
| [SRC-F725E90B2A-L002421](../../tests/test_web_agent.py#L2421) | 2421 | `"    monkeypatch.setattr(agent, \"_search_web\", completed_empty_search)"` | — |
| [SRC-F725E90B2A-L002422](../../tests/test_web_agent.py#L2422) | 2422 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L002423](../../tests/test_web_agent.py#L2423) | 2423 | `""` | — |
| [SRC-F725E90B2A-L002424](../../tests/test_web_agent.py#L2424) | 2424 | `"    assert report[\"checks\"][\"web_search\"][\"status\"] == \"degraded\""` | — |
| [SRC-F725E90B2A-L002425](../../tests/test_web_agent.py#L2425) | 2425 | `"    assert report[\"checks\"][\"web_search\"][\"result_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002426](../../tests/test_web_agent.py#L2426) | 2426 | `"    assert report[\"checks\"][\"web_search\"][\"completed_connector_responses\"] >= 1"` | — |
| [SRC-F725E90B2A-L002427](../../tests/test_web_agent.py#L2427) | 2427 | `"    assert \"completed a request\" in report[\"checks\"][\"web_search\"][\"note\"]"` | — |
| [SRC-F725E90B2A-L002428](../../tests/test_web_agent.py#L2428) | 2428 | `""` | — |
| [SRC-F725E90B2A-L002429](../../tests/test_web_agent.py#L2429) | 2429 | `""` | — |
| [SRC-F725E90B2A-L002430](../../tests/test_web_agent.py#L2430) | 2430 | `"def test_deepseek_search_request_budget_defaults_to_one_and_is_bounded(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002431](../../tests/test_web_agent.py#L2431) | 2431 | `"    monkeypatch.setenv(\"DEEPSEEK_SEARCH_API_KEY\", \"test-secret-key\")"` | — |
| [SRC-F725E90B2A-L002432](../../tests/test_web_agent.py#L2432) | 2432 | `"    monkeypatch.delenv(\"OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET\", raising=False)"` | — |
| [SRC-F725E90B2A-L002433](../../tests/test_web_agent.py#L2433) | 2433 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002434](../../tests/test_web_agent.py#L2434) | 2434 | `"    assert agent._reserve_deepseek_search_request() is True"` | — |
| [SRC-F725E90B2A-L002435](../../tests/test_web_agent.py#L2435) | 2435 | `"    assert agent._reserve_deepseek_search_request() is False"` | — |
| [SRC-F725E90B2A-L002436](../../tests/test_web_agent.py#L2436) | 2436 | `""` | — |
| [SRC-F725E90B2A-L002437](../../tests/test_web_agent.py#L2437) | 2437 | `"    monkeypatch.setenv(\"OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET\", \"2\")"` | — |
| [SRC-F725E90B2A-L002438](../../tests/test_web_agent.py#L2438) | 2438 | `"    other_agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002439](../../tests/test_web_agent.py#L2439) | 2439 | `"    assert other_agent._reserve_deepseek_search_request() is True"` | — |
| [SRC-F725E90B2A-L002440](../../tests/test_web_agent.py#L2440) | 2440 | `"    assert other_agent._reserve_deepseek_search_request() is True"` | — |
| [SRC-F725E90B2A-L002441](../../tests/test_web_agent.py#L2441) | 2441 | `"    assert other_agent._reserve_deepseek_search_request() is False"` | — |
| [SRC-F725E90B2A-L002442](../../tests/test_web_agent.py#L2442) | 2442 | `""` | — |
| [SRC-F725E90B2A-L002443](../../tests/test_web_agent.py#L2443) | 2443 | `""` | — |
| [SRC-F725E90B2A-L002444](../../tests/test_web_agent.py#L2444) | 2444 | `""` | — |
| [SRC-F725E90B2A-L002445](../../tests/test_web_agent.py#L2445) | 2445 | `"def test_diagnostics_distinguishes_completed_search_without_matches_from_connection_failure(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002446](../../tests/test_web_agent.py#L2446) | 2446 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002447](../../tests/test_web_agent.py#L2447) | 2447 | `"    # A stale record from a prior search must not make a new diagnostics call pass."` | — |
| [SRC-F725E90B2A-L002448](../../tests/test_web_agent.py#L2448) | 2448 | `"    agent._record_provider_diagnostic(\"old_provider\", \"old query\", \"ok\", 1)"` | — |
| [SRC-F725E90B2A-L002449](../../tests/test_web_agent.py#L2449) | 2449 | `""` | — |
| [SRC-F725E90B2A-L002450](../../tests/test_web_agent.py#L2450) | 2450 | `"    def no_results(query):"` | — |
| [SRC-F725E90B2A-L002451](../../tests/test_web_agent.py#L2451) | 2451 | `"        agent._record_provider_diagnostic(\"duckduckgo_html\", query, \"no_results\")"` | — |
| [SRC-F725E90B2A-L002452](../../tests/test_web_agent.py#L2452) | 2452 | `"        raise RuntimeError(\"no parseable results\")"` | — |
| [SRC-F725E90B2A-L002453](../../tests/test_web_agent.py#L2453) | 2453 | `""` | — |
| [SRC-F725E90B2A-L002454](../../tests/test_web_agent.py#L2454) | 2454 | `"    monkeypatch.setattr(agent, \"_search_web\", no_results)"` | — |
| [SRC-F725E90B2A-L002455](../../tests/test_web_agent.py#L2455) | 2455 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L002456](../../tests/test_web_agent.py#L2456) | 2456 | `""` | — |
| [SRC-F725E90B2A-L002457](../../tests/test_web_agent.py#L2457) | 2457 | `"    check = report[\"checks\"][\"web_search\"]"` | — |
| [SRC-F725E90B2A-L002458](../../tests/test_web_agent.py#L2458) | 2458 | `"    assert check[\"status\"] == \"degraded\""` | — |
| [SRC-F725E90B2A-L002459](../../tests/test_web_agent.py#L2459) | 2459 | `"    assert check[\"result_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002460](../../tests/test_web_agent.py#L2460) | 2460 | `"    assert check[\"completed_connector_responses\"] >= 1"` | — |
| [SRC-F725E90B2A-L002461](../../tests/test_web_agent.py#L2461) | 2461 | `"    assert \"completed a request\" in check[\"note\"]"` | — |
| [SRC-F725E90B2A-L002462](../../tests/test_web_agent.py#L2462) | 2462 | `"    assert \"old_provider\" not in str(check)"` | — |
| [SRC-F725E90B2A-L002463](../../tests/test_web_agent.py#L2463) | 2463 | `""` | — |
| [SRC-F725E90B2A-L002464](../../tests/test_web_agent.py#L2464) | 2464 | `""` | — |
| [SRC-F725E90B2A-L002465](../../tests/test_web_agent.py#L2465) | 2465 | `"def test_buyer_intent_phrase_inside_negated_text_is_not_a_lead_signal():"` | — |
| [SRC-F725E90B2A-L002466](../../tests/test_web_agent.py#L2466) | 2466 | `"    source = {"` | — |
| [SRC-F725E90B2A-L002467](../../tests/test_web_agent.py#L2467) | 2467 | `"        \"title\": \"Buyer discussion\","` | — |
| [SRC-F725E90B2A-L002468](../../tests/test_web_agent.py#L2468) | 2468 | `"        \"snippet\": \"I am not looking to buy an apartment this year.\","` | — |
| [SRC-F725E90B2A-L002469](../../tests/test_web_agent.py#L2469) | 2469 | `"        \"page_text\": \"I am not looking to buy an apartment this year.\","` | — |
| [SRC-F725E90B2A-L002470](../../tests/test_web_agent.py#L2470) | 2470 | `"    }"` | — |
| [SRC-F725E90B2A-L002471](../../tests/test_web_agent.py#L2471) | 2471 | `"    assert WebAgent._lead_intent_evidence(source) is None"` | — |
| [SRC-F725E90B2A-L002472](../../tests/test_web_agent.py#L2472) | 2472 | `""` | — |
| [SRC-F725E90B2A-L002473](../../tests/test_web_agent.py#L2473) | 2473 | `""` | — |
| [SRC-F725E90B2A-L002474](../../tests/test_web_agent.py#L2474) | 2474 | `""` | — |
| [SRC-F725E90B2A-L002475](../../tests/test_web_agent.py#L2475) | 2475 | `"def test_lead_generation_preserves_unknown_state_when_research_throws(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002476](../../tests/test_web_agent.py#L2476) | 2476 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002477](../../tests/test_web_agent.py#L2477) | 2477 | `"    question = \"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\""` | — |
| [SRC-F725E90B2A-L002478](../../tests/test_web_agent.py#L2478) | 2478 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002479](../../tests/test_web_agent.py#L2479) | 2479 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002480](../../tests/test_web_agent.py#L2480) | 2480 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002481](../../tests/test_web_agent.py#L2481) | 2481 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002482](../../tests/test_web_agent.py#L2482) | 2482 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002483](../../tests/test_web_agent.py#L2483) | 2483 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002484](../../tests/test_web_agent.py#L2484) | 2484 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002485](../../tests/test_web_agent.py#L2485) | 2485 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002486](../../tests/test_web_agent.py#L2486) | 2486 | `"    }"` | — |
| [SRC-F725E90B2A-L002487](../../tests/test_web_agent.py#L2487) | 2487 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda q, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002488](../../tests/test_web_agent.py#L2488) | 2488 | `""` | — |
| [SRC-F725E90B2A-L002489](../../tests/test_web_agent.py#L2489) | 2489 | `"    def fail_research(research_plan):"` | — |
| [SRC-F725E90B2A-L002490](../../tests/test_web_agent.py#L2490) | 2490 | `"        raise RuntimeError(\"mocked interrupted research\")"` | — |
| [SRC-F725E90B2A-L002491](../../tests/test_web_agent.py#L2491) | 2491 | `""` | — |
| [SRC-F725E90B2A-L002492](../../tests/test_web_agent.py#L2492) | 2492 | `"    monkeypatch.setattr(agent, \"_collect_research\", fail_research)"` | — |
| [SRC-F725E90B2A-L002493](../../tests/test_web_agent.py#L2493) | 2493 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002494](../../tests/test_web_agent.py#L2494) | 2494 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002495](../../tests/test_web_agent.py#L2495) | 2495 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L002496](../../tests/test_web_agent.py#L2496) | 2496 | `"        lambda *args, **kwargs: (_ for _ in ()).throw("` | — |
| [SRC-F725E90B2A-L002497](../../tests/test_web_agent.py#L2497) | 2497 | `"            AssertionError(\"must not generate a lead from an incomplete search\")"` | — |
| [SRC-F725E90B2A-L002498](../../tests/test_web_agent.py#L2498) | 2498 | `"        ),"` | — |
| [SRC-F725E90B2A-L002499](../../tests/test_web_agent.py#L2499) | 2499 | `"    )"` | — |
| [SRC-F725E90B2A-L002500](../../tests/test_web_agent.py#L2500) | 2500 | `""` | — |
| [SRC-F725E90B2A-L002501](../../tests/test_web_agent.py#L2501) | 2501 | `"    result = agent.answer(question)"` | — |
| [SRC-F725E90B2A-L002502](../../tests/test_web_agent.py#L2502) | 2502 | `"    lead = result[\"search_report\"][\"lead_generation\"]"` | — |
| [SRC-F725E90B2A-L002503](../../tests/test_web_agent.py#L2503) | 2503 | `""` | — |
| [SRC-F725E90B2A-L002504](../../tests/test_web_agent.py#L2504) | 2504 | `"    assert lead[\"status\"] == \"research_incomplete\""` | — |
| [SRC-F725E90B2A-L002505](../../tests/test_web_agent.py#L2505) | 2505 | `"    assert lead[\"candidate_signal_count\"] is None"` | — |
| [SRC-F725E90B2A-L002506](../../tests/test_web_agent.py#L2506) | 2506 | `"    assert lead[\"related_results_reviewed\"] is None"` | — |
| [SRC-F725E90B2A-L002507](../../tests/test_web_agent.py#L2507) | 2507 | `"    assert result[\"search_report\"][\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002508](../../tests/test_web_agent.py#L2508) | 2508 | `"    assert result[\"search_report\"][\"evidence_signals\"] is None"` | — |
| [SRC-F725E90B2A-L002509](../../tests/test_web_agent.py#L2509) | 2509 | `"    assert \"لم أستطع تحديد\" in result[\"answer\"] or \"تعطل مسار البحث\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L002510](../../tests/test_web_agent.py#L2510) | 2510 | `""` | — |
| [SRC-F725E90B2A-L002511](../../tests/test_web_agent.py#L2511) | 2511 | `""` | — |
| [SRC-F725E90B2A-L002512](../../tests/test_web_agent.py#L2512) | 2512 | `""` | — |
| [SRC-F725E90B2A-L002513](../../tests/test_web_agent.py#L2513) | 2513 | `"def test_local_answer_exposes_request_budget_without_claiming_live_search():"` | — |
| [SRC-F725E90B2A-L002514](../../tests/test_web_agent.py#L2514) | 2514 | `"    result = WebAgent().answer(\"مرحبا\")"` | — |
| [SRC-F725E90B2A-L002515](../../tests/test_web_agent.py#L2515) | 2515 | `""` | — |
| [SRC-F725E90B2A-L002516](../../tests/test_web_agent.py#L2516) | 2516 | `"    budget = result[\"request_budget\"]"` | — |
| [SRC-F725E90B2A-L002517](../../tests/test_web_agent.py#L2517) | 2517 | `"    assert budget[\"policy\"] == \"cooperative_per_request_budget\""` | — |
| [SRC-F725E90B2A-L002518](../../tests/test_web_agent.py#L2518) | 2518 | `"    assert budget[\"counts\"][\"search_queries\"] == 0"` | — |
| [SRC-F725E90B2A-L002519](../../tests/test_web_agent.py#L2519) | 2519 | `"    assert budget[\"counts\"][\"model_calls\"] == 0"` | — |
| [SRC-F725E90B2A-L002520](../../tests/test_web_agent.py#L2520) | 2520 | `"    assert budget[\"hard_cancellation_guaranteed\"] is False"` | — |
| [SRC-F725E90B2A-L002521](../../tests/test_web_agent.py#L2521) | 2521 | `""` | — |
| [SRC-F725E90B2A-L002522](../../tests/test_web_agent.py#L2522) | 2522 | `""` | — |
