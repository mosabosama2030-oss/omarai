# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **060**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L001926 إلى SRC-F725E90B2A-L002725
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L001926](../../tests/test_web_agent.py#L1926) | 1926 | `""` | — |
| [SRC-F725E90B2A-L001927](../../tests/test_web_agent.py#L1927) | 1927 | `""` | — |
| [SRC-F725E90B2A-L001928](../../tests/test_web_agent.py#L1928) | 1928 | `"def test_reviewer_checks_coverage_targets_without_claiming_independent_verification(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001929](../../tests/test_web_agent.py#L1929) | 1929 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001930](../../tests/test_web_agent.py#L1930) | 1930 | `"    captured = {}"` | — |
| [SRC-F725E90B2A-L001931](../../tests/test_web_agent.py#L1931) | 1931 | `""` | — |
| [SRC-F725E90B2A-L001932](../../tests/test_web_agent.py#L1932) | 1932 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-F725E90B2A-L001933](../../tests/test_web_agent.py#L1933) | 1933 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-F725E90B2A-L001934](../../tests/test_web_agent.py#L1934) | 1934 | `"        return \"<<<OMARAI_FINAL_ANSWER>>>تمت مراجعة المسودة.<<<END_OMARAI_FINAL_ANSWER>>>\""` | — |
| [SRC-F725E90B2A-L001935](../../tests/test_web_agent.py#L1935) | 1935 | `""` | — |
| [SRC-F725E90B2A-L001936](../../tests/test_web_agent.py#L1936) | 1936 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-F725E90B2A-L001937](../../tests/test_web_agent.py#L1937) | 1937 | `"    result = agent._review_answer("` | — |
| [SRC-F725E90B2A-L001938](../../tests/test_web_agent.py#L1938) | 1938 | `"        question=\"قارن بين خدمتين من حيث السعر، الخصوصية والاعتمادية\","` | — |
| [SRC-F725E90B2A-L001939](../../tests/test_web_agent.py#L1939) | 1939 | `"        answer=\"السعر مناسب [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L001940](../../tests/test_web_agent.py#L1940) | 1940 | `"        sources=[sample_source(0)],"` | — |
| [SRC-F725E90B2A-L001941](../../tests/test_web_agent.py#L1941) | 1941 | `"    )"` | — |
| [SRC-F725E90B2A-L001942](../../tests/test_web_agent.py#L1942) | 1942 | `"    system_content = \"\\n\".join(m[\"content\"] for m in captured[\"messages\"] if m[\"role\"] == \"system\")"` | — |
| [SRC-F725E90B2A-L001943](../../tests/test_web_agent.py#L1943) | 1943 | `"    user_content = \"\\n\".join(m[\"content\"] for m in captured[\"messages\"] if m[\"role\"] == \"user\")"` | — |
| [SRC-F725E90B2A-L001944](../../tests/test_web_agent.py#L1944) | 1944 | `"    assert result == \"تمت مراجعة المسودة.\""` | — |
| [SRC-F725E90B2A-L001945](../../tests/test_web_agent.py#L1945) | 1945 | `"    assert \"اكتمال الإجابة مقابل\" in system_content"` | — |
| [SRC-F725E90B2A-L001946](../../tests/test_web_agent.py#L1946) | 1946 | `"    assert \"الاعتمادية\" in user_content"` | — |
| [SRC-F725E90B2A-L001947](../../tests/test_web_agent.py#L1947) | 1947 | `"    assert \"قائمة محاور مستخرجة آليًا\" in user_content"` | — |
| [SRC-F725E90B2A-L001948](../../tests/test_web_agent.py#L1948) | 1948 | `""` | — |
| [SRC-F725E90B2A-L001949](../../tests/test_web_agent.py#L1949) | 1949 | `""` | — |
| [SRC-F725E90B2A-L001950](../../tests/test_web_agent.py#L1950) | 1950 | `"def test_search_attempt_is_reported_when_no_sources_survive(monkeypatch):"` | — |
| [SRC-F725E90B2A-L001951](../../tests/test_web_agent.py#L1951) | 1951 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L001952](../../tests/test_web_agent.py#L1952) | 1952 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L001953](../../tests/test_web_agent.py#L1953) | 1953 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L001954](../../tests/test_web_agent.py#L1954) | 1954 | `"        \"queries\": [\"ما آخر تطورات الطاقة المتجددة اليوم؟\"],"` | — |
| [SRC-F725E90B2A-L001955](../../tests/test_web_agent.py#L1955) | 1955 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L001956](../../tests/test_web_agent.py#L1956) | 1956 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L001957](../../tests/test_web_agent.py#L1957) | 1957 | `"        \"freshness\": \"today\","` | — |
| [SRC-F725E90B2A-L001958](../../tests/test_web_agent.py#L1958) | 1958 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L001959](../../tests/test_web_agent.py#L1959) | 1959 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L001960](../../tests/test_web_agent.py#L1960) | 1960 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001961](../../tests/test_web_agent.py#L1961) | 1961 | `"    }"` | — |
| [SRC-F725E90B2A-L001962](../../tests/test_web_agent.py#L1962) | 1962 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L001963](../../tests/test_web_agent.py#L1963) | 1963 | `""` | — |
| [SRC-F725E90B2A-L001964](../../tests/test_web_agent.py#L1964) | 1964 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L001965](../../tests/test_web_agent.py#L1965) | 1965 | `"        calls.append(dict(research_plan))"` | — |
| [SRC-F725E90B2A-L001966](../../tests/test_web_agent.py#L1966) | 1966 | `"        return [], [], {"` | — |
| [SRC-F725E90B2A-L001967](../../tests/test_web_agent.py#L1967) | 1967 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L001968](../../tests/test_web_agent.py#L1968) | 1968 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L001969](../../tests/test_web_agent.py#L1969) | 1969 | `"            \"query_results\": [{\"query\": research_plan[\"queries\"][0], \"results\": 0}],"` | — |
| [SRC-F725E90B2A-L001970](../../tests/test_web_agent.py#L1970) | 1970 | `"            \"unique_sources\": 0,"` | — |
| [SRC-F725E90B2A-L001971](../../tests/test_web_agent.py#L1971) | 1971 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-F725E90B2A-L001972](../../tests/test_web_agent.py#L1972) | 1972 | `"            \"providers_used\": [],"` | — |
| [SRC-F725E90B2A-L001973](../../tests/test_web_agent.py#L1973) | 1973 | `"            \"provider_counts\": {},"` | — |
| [SRC-F725E90B2A-L001974](../../tests/test_web_agent.py#L1974) | 1974 | `"            \"platform_counts\": {},"` | — |
| [SRC-F725E90B2A-L001975](../../tests/test_web_agent.py#L1975) | 1975 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L001976](../../tests/test_web_agent.py#L1976) | 1976 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L001977](../../tests/test_web_agent.py#L1977) | 1977 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L001978](../../tests/test_web_agent.py#L1978) | 1978 | `"            \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L001979](../../tests/test_web_agent.py#L1979) | 1979 | `"        }"` | — |
| [SRC-F725E90B2A-L001980](../../tests/test_web_agent.py#L1980) | 1980 | `""` | — |
| [SRC-F725E90B2A-L001981](../../tests/test_web_agent.py#L1981) | 1981 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L001982](../../tests/test_web_agent.py#L1982) | 1982 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L001983](../../tests/test_web_agent.py#L1983) | 1983 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L001984](../../tests/test_web_agent.py#L1984) | 1984 | `"        agent,"` | — |
| [SRC-F725E90B2A-L001985](../../tests/test_web_agent.py#L1985) | 1985 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L001986](../../tests/test_web_agent.py#L1986) | 1986 | `"        lambda *args, **kwargs: pytest.fail(\"The model must not answer without usable evidence\"),"` | — |
| [SRC-F725E90B2A-L001987](../../tests/test_web_agent.py#L1987) | 1987 | `"    )"` | — |
| [SRC-F725E90B2A-L001988](../../tests/test_web_agent.py#L1988) | 1988 | `""` | — |
| [SRC-F725E90B2A-L001989](../../tests/test_web_agent.py#L1989) | 1989 | `"    result = agent.answer(\"ما آخر تطورات الطاقة المتجددة اليوم؟\")"` | — |
| [SRC-F725E90B2A-L001990](../../tests/test_web_agent.py#L1990) | 1990 | `""` | — |
| [SRC-F725E90B2A-L001991](../../tests/test_web_agent.py#L1991) | 1991 | `"    assert result[\"kind\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L001992](../../tests/test_web_agent.py#L1992) | 1992 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L001993](../../tests/test_web_agent.py#L1993) | 1993 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-F725E90B2A-L001994](../../tests/test_web_agent.py#L1994) | 1994 | `"    assert result[\"sources\"] == []"` | — |
| [SRC-F725E90B2A-L001995](../../tests/test_web_agent.py#L1995) | 1995 | `"    assert result[\"search_report\"][\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L001996](../../tests/test_web_agent.py#L1996) | 1996 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_no_usable_sources\""` | — |
| [SRC-F725E90B2A-L001997](../../tests/test_web_agent.py#L1997) | 1997 | `"    assert result[\"search_report\"][\"usable_sources_after_filtering\"] == 0"` | — |
| [SRC-F725E90B2A-L001998](../../tests/test_web_agent.py#L1998) | 1998 | `"    assert result[\"search_report\"][\"insufficient_evidence\"] is True"` | — |
| [SRC-F725E90B2A-L001999](../../tests/test_web_agent.py#L1999) | 1999 | `"    assert result[\"search_report\"][\"pipeline_completion_status\"] == \"insufficient_evidence\""` | — |
| [SRC-F725E90B2A-L002000](../../tests/test_web_agent.py#L2000) | 2000 | `"    assert result[\"task_understanding\"][\"tool_execution\"][\"accepted_source_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002001](../../tests/test_web_agent.py#L2001) | 2001 | `"    assert calls, \"Expected at least one attempted retrieval round\""` | — |
| [SRC-F725E90B2A-L002002](../../tests/test_web_agent.py#L2002) | 2002 | `""` | — |
| [SRC-F725E90B2A-L002003](../../tests/test_web_agent.py#L2003) | 2003 | `""` | — |
| [SRC-F725E90B2A-L002004](../../tests/test_web_agent.py#L2004) | 2004 | `"def test_success_report_counts_registrable_domains_not_sibling_subdomains(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002005](../../tests/test_web_agent.py#L2005) | 2005 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002006](../../tests/test_web_agent.py#L2006) | 2006 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002007](../../tests/test_web_agent.py#L2007) | 2007 | `"    first = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002008](../../tests/test_web_agent.py#L2008) | 2008 | `"    first[\"url\"] = \"https://news.example.com/research\""` | — |
| [SRC-F725E90B2A-L002009](../../tests/test_web_agent.py#L2009) | 2009 | `"    first[\"domain\"] = \"news.example.com\""` | — |
| [SRC-F725E90B2A-L002010](../../tests/test_web_agent.py#L2010) | 2010 | `"    second = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002011](../../tests/test_web_agent.py#L2011) | 2011 | `"    second[\"url\"] = \"https://offers.example.com/research\""` | — |
| [SRC-F725E90B2A-L002012](../../tests/test_web_agent.py#L2012) | 2012 | `"    second[\"domain\"] = \"offers.example.com\""` | — |
| [SRC-F725E90B2A-L002013](../../tests/test_web_agent.py#L2013) | 2013 | `"    third = sample_source(1)"` | — |
| [SRC-F725E90B2A-L002014](../../tests/test_web_agent.py#L2014) | 2014 | `"    sources = [first, second, third]"` | — |
| [SRC-F725E90B2A-L002015](../../tests/test_web_agent.py#L2015) | 2015 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002016](../../tests/test_web_agent.py#L2016) | 2016 | `"        \"queries\": [\"قارن هذه التقنية\"],"` | — |
| [SRC-F725E90B2A-L002017](../../tests/test_web_agent.py#L2017) | 2017 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002018](../../tests/test_web_agent.py#L2018) | 2018 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002019](../../tests/test_web_agent.py#L2019) | 2019 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002020](../../tests/test_web_agent.py#L2020) | 2020 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002021](../../tests/test_web_agent.py#L2021) | 2021 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002022](../../tests/test_web_agent.py#L2022) | 2022 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002023](../../tests/test_web_agent.py#L2023) | 2023 | `"    }"` | — |
| [SRC-F725E90B2A-L002024](../../tests/test_web_agent.py#L2024) | 2024 | `""` | — |
| [SRC-F725E90B2A-L002025](../../tests/test_web_agent.py#L2025) | 2025 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002026](../../tests/test_web_agent.py#L2026) | 2026 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002027](../../tests/test_web_agent.py#L2027) | 2027 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002028](../../tests/test_web_agent.py#L2028) | 2028 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L002029](../../tests/test_web_agent.py#L2029) | 2029 | `"        lambda research_plan: ("` | — |
| [SRC-F725E90B2A-L002030](../../tests/test_web_agent.py#L2030) | 2030 | `"            sources,"` | — |
| [SRC-F725E90B2A-L002031](../../tests/test_web_agent.py#L2031) | 2031 | `"            [],"` | — |
| [SRC-F725E90B2A-L002032](../../tests/test_web_agent.py#L2032) | 2032 | `"            {"` | — |
| [SRC-F725E90B2A-L002033](../../tests/test_web_agent.py#L2033) | 2033 | `"                \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L002034](../../tests/test_web_agent.py#L2034) | 2034 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L002035](../../tests/test_web_agent.py#L2035) | 2035 | `"                \"query_results\": [{\"query\": \"قارن هذه التقنية\", \"results\": 3}],"` | — |
| [SRC-F725E90B2A-L002036](../../tests/test_web_agent.py#L2036) | 2036 | `"                \"unique_sources\": 3,"` | — |
| [SRC-F725E90B2A-L002037](../../tests/test_web_agent.py#L2037) | 2037 | `"                \"pages_fetched\": 3,"` | — |
| [SRC-F725E90B2A-L002038](../../tests/test_web_agent.py#L2038) | 2038 | `"                \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L002039](../../tests/test_web_agent.py#L2039) | 2039 | `"                \"provider_counts\": {\"test_provider\": 3},"` | — |
| [SRC-F725E90B2A-L002040](../../tests/test_web_agent.py#L2040) | 2040 | `"                \"platform_counts\": {\"web\": 3},"` | — |
| [SRC-F725E90B2A-L002041](../../tests/test_web_agent.py#L2041) | 2041 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002042](../../tests/test_web_agent.py#L2042) | 2042 | `"                \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002043](../../tests/test_web_agent.py#L2043) | 2043 | `"                \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002044](../../tests/test_web_agent.py#L2044) | 2044 | `"                \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L002045](../../tests/test_web_agent.py#L2045) | 2045 | `"            },"` | — |
| [SRC-F725E90B2A-L002046](../../tests/test_web_agent.py#L2046) | 2046 | `"        ),"` | — |
| [SRC-F725E90B2A-L002047](../../tests/test_web_agent.py#L2047) | 2047 | `"    )"` | — |
| [SRC-F725E90B2A-L002048](../../tests/test_web_agent.py#L2048) | 2048 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L002049](../../tests/test_web_agent.py#L2049) | 2049 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"الإجابة [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L002050](../../tests/test_web_agent.py#L2050) | 2050 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L002051](../../tests/test_web_agent.py#L2051) | 2051 | `""` | — |
| [SRC-F725E90B2A-L002052](../../tests/test_web_agent.py#L2052) | 2052 | `"    result = agent.answer(\"قارن هذه التقنية\")"` | — |
| [SRC-F725E90B2A-L002053](../../tests/test_web_agent.py#L2053) | 2053 | `""` | — |
| [SRC-F725E90B2A-L002054](../../tests/test_web_agent.py#L2054) | 2054 | `"    assert result[\"kind\"] in {\"web_research\", \"web_fallback\"}"` | — |
| [SRC-F725E90B2A-L002055](../../tests/test_web_agent.py#L2055) | 2055 | `"    assert result[\"search_report\"][\"unique_sources\"] == 3"` | — |
| [SRC-F725E90B2A-L002056](../../tests/test_web_agent.py#L2056) | 2056 | `"    assert result[\"search_report\"][\"distinct_registrable_domains\"] == 2"` | — |
| [SRC-F725E90B2A-L002057](../../tests/test_web_agent.py#L2057) | 2057 | `"    assert result[\"search_report\"][\"independent_sources\"] == 2"` | — |
| [SRC-F725E90B2A-L002058](../../tests/test_web_agent.py#L2058) | 2058 | `"    assert result[\"search_report\"][\"editorial_independence_status\"] == \"not_assessed\""` | — |
| [SRC-F725E90B2A-L002059](../../tests/test_web_agent.py#L2059) | 2059 | `""` | — |
| [SRC-F725E90B2A-L002060](../../tests/test_web_agent.py#L2060) | 2060 | `""` | — |
| [SRC-F725E90B2A-L002061](../../tests/test_web_agent.py#L2061) | 2061 | `"def test_completion_rejects_content_filtered_primary_and_uses_fallback(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002062](../../tests/test_web_agent.py#L2062) | 2062 | `"    import json"` | — |
| [SRC-F725E90B2A-L002063](../../tests/test_web_agent.py#L2063) | 2063 | `""` | — |
| [SRC-F725E90B2A-L002064](../../tests/test_web_agent.py#L2064) | 2064 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002065](../../tests/test_web_agent.py#L2065) | 2065 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002066](../../tests/test_web_agent.py#L2066) | 2066 | `"    agent.fallback_model = \"fallback/model\""` | — |
| [SRC-F725E90B2A-L002067](../../tests/test_web_agent.py#L2067) | 2067 | `"    called = []"` | — |
| [SRC-F725E90B2A-L002068](../../tests/test_web_agent.py#L2068) | 2068 | `""` | — |
| [SRC-F725E90B2A-L002069](../../tests/test_web_agent.py#L2069) | 2069 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L002070](../../tests/test_web_agent.py#L2070) | 2070 | `"        def __init__(self, content, finish_reason):"` | — |
| [SRC-F725E90B2A-L002071](../../tests/test_web_agent.py#L2071) | 2071 | `"            self.body = json.dumps({"` | — |
| [SRC-F725E90B2A-L002072](../../tests/test_web_agent.py#L2072) | 2072 | `"                \"choices\": [{"` | — |
| [SRC-F725E90B2A-L002073](../../tests/test_web_agent.py#L2073) | 2073 | `"                    \"message\": {\"content\": content},"` | — |
| [SRC-F725E90B2A-L002074](../../tests/test_web_agent.py#L2074) | 2074 | `"                    \"finish_reason\": finish_reason,"` | — |
| [SRC-F725E90B2A-L002075](../../tests/test_web_agent.py#L2075) | 2075 | `"                }]"` | — |
| [SRC-F725E90B2A-L002076](../../tests/test_web_agent.py#L2076) | 2076 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002077](../../tests/test_web_agent.py#L2077) | 2077 | `""` | — |
| [SRC-F725E90B2A-L002078](../../tests/test_web_agent.py#L2078) | 2078 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L002079](../../tests/test_web_agent.py#L2079) | 2079 | `"            return self"` | — |
| [SRC-F725E90B2A-L002080](../../tests/test_web_agent.py#L2080) | 2080 | `""` | — |
| [SRC-F725E90B2A-L002081](../../tests/test_web_agent.py#L2081) | 2081 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-F725E90B2A-L002082](../../tests/test_web_agent.py#L2082) | 2082 | `"            return False"` | — |
| [SRC-F725E90B2A-L002083](../../tests/test_web_agent.py#L2083) | 2083 | `""` | — |
| [SRC-F725E90B2A-L002084](../../tests/test_web_agent.py#L2084) | 2084 | `"        def read(self, limit):"` | — |
| [SRC-F725E90B2A-L002085](../../tests/test_web_agent.py#L2085) | 2085 | `"            return self.body"` | — |
| [SRC-F725E90B2A-L002086](../../tests/test_web_agent.py#L2086) | 2086 | `""` | — |
| [SRC-F725E90B2A-L002087](../../tests/test_web_agent.py#L2087) | 2087 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-F725E90B2A-L002088](../../tests/test_web_agent.py#L2088) | 2088 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-F725E90B2A-L002089](../../tests/test_web_agent.py#L2089) | 2089 | `"        called.append(model)"` | — |
| [SRC-F725E90B2A-L002090](../../tests/test_web_agent.py#L2090) | 2090 | `"        if model == \"filtered/primary\":"` | — |
| [SRC-F725E90B2A-L002091](../../tests/test_web_agent.py#L2091) | 2091 | `"            return FakeResponse(\"جزء جواب مفلتر لا ينبغي اعتباره مكتملا\", \"content_filter\")"` | — |
| [SRC-F725E90B2A-L002092](../../tests/test_web_agent.py#L2092) | 2092 | `"        return FakeResponse(\"إجابة الاحتياط المكتملة\", \"stop\")"` | — |
| [SRC-F725E90B2A-L002093](../../tests/test_web_agent.py#L2093) | 2093 | `""` | — |
| [SRC-F725E90B2A-L002094](../../tests/test_web_agent.py#L2094) | 2094 | `"    monkeypatch.setattr(\"agents.web_agent._open_model_request\", fake_urlopen)"` | — |
| [SRC-F725E90B2A-L002095](../../tests/test_web_agent.py#L2095) | 2095 | `"    result = agent._request_completion("` | — |
| [SRC-F725E90B2A-L002096](../../tests/test_web_agent.py#L2096) | 2096 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-F725E90B2A-L002097](../../tests/test_web_agent.py#L2097) | 2097 | `"        model=\"filtered/primary\","` | — |
| [SRC-F725E90B2A-L002098](../../tests/test_web_agent.py#L2098) | 2098 | `"    )"` | — |
| [SRC-F725E90B2A-L002099](../../tests/test_web_agent.py#L2099) | 2099 | `""` | — |
| [SRC-F725E90B2A-L002100](../../tests/test_web_agent.py#L2100) | 2100 | `"    assert result == \"إجابة الاحتياط المكتملة\""` | — |
| [SRC-F725E90B2A-L002101](../../tests/test_web_agent.py#L2101) | 2101 | `"    assert called == [\"filtered/primary\", \"fallback/model\"]"` | — |
| [SRC-F725E90B2A-L002102](../../tests/test_web_agent.py#L2102) | 2102 | `"    assert \"جزء جواب مفلتر\" not in result"` | — |
| [SRC-F725E90B2A-L002103](../../tests/test_web_agent.py#L2103) | 2103 | `""` | — |
| [SRC-F725E90B2A-L002104](../../tests/test_web_agent.py#L2104) | 2104 | `""` | — |
| [SRC-F725E90B2A-L002105](../../tests/test_web_agent.py#L2105) | 2105 | `"def test_reviewer_rejects_duplicate_final_answer_delimiters(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002106](../../tests/test_web_agent.py#L2106) | 2106 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002107](../../tests/test_web_agent.py#L2107) | 2107 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002108](../../tests/test_web_agent.py#L2108) | 2108 | `"    source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002109](../../tests/test_web_agent.py#L2109) | 2109 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002110](../../tests/test_web_agent.py#L2110) | 2110 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002111](../../tests/test_web_agent.py#L2111) | 2111 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L002112](../../tests/test_web_agent.py#L2112) | 2112 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-F725E90B2A-L002113](../../tests/test_web_agent.py#L2113) | 2113 | `"            \"<<<OMARAI_FINAL_ANSWER>>>تقرير مراجعة داخلي \""` | — |
| [SRC-F725E90B2A-L002114](../../tests/test_web_agent.py#L2114) | 2114 | `"            \"<<<OMARAI_FINAL_ANSWER>>>نص مزعوم\""` | — |
| [SRC-F725E90B2A-L002115](../../tests/test_web_agent.py#L2115) | 2115 | `"            \"<<<END_OMARAI_FINAL_ANSWER>>><<<END_OMARAI_FINAL_ANSWER>>>\""` | — |
| [SRC-F725E90B2A-L002116](../../tests/test_web_agent.py#L2116) | 2116 | `"        ),"` | — |
| [SRC-F725E90B2A-L002117](../../tests/test_web_agent.py#L2117) | 2117 | `"    )"` | — |
| [SRC-F725E90B2A-L002118](../../tests/test_web_agent.py#L2118) | 2118 | `""` | — |
| [SRC-F725E90B2A-L002119](../../tests/test_web_agent.py#L2119) | 2119 | `"    with pytest.raises(RuntimeError, match=\"فصل الإجابة النهائية\"):"` | — |
| [SRC-F725E90B2A-L002120](../../tests/test_web_agent.py#L2120) | 2120 | `"        agent._review_answer(\"ما مضمون الصفحة؟\", \"مسودة\", [source])"` | — |
| [SRC-F725E90B2A-L002121](../../tests/test_web_agent.py#L2121) | 2121 | `""` | — |
| [SRC-F725E90B2A-L002122](../../tests/test_web_agent.py#L2122) | 2122 | `""` | — |
| [SRC-F725E90B2A-L002123](../../tests/test_web_agent.py#L2123) | 2123 | `"def test_frontend_review_status_matches_api_contract():"` | — |
| [SRC-F725E90B2A-L002124](../../tests/test_web_agent.py#L2124) | 2124 | `"    html = (Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002125](../../tests/test_web_agent.py#L2125) | 2125 | `"    assert 'r.second_pass_review===\"model_claim_audit_completed\"' in html"` | — |
| [SRC-F725E90B2A-L002126](../../tests/test_web_agent.py#L2126) | 2126 | `"    assert 'r.second_pass_review===\"model_claim_audit_unavailable\"' in html"` | — |
| [SRC-F725E90B2A-L002127](../../tests/test_web_agent.py#L2127) | 2127 | `"    assert 'r.second_pass_review===\"model_second_pass_completed\"' not in html"` | — |
| [SRC-F725E90B2A-L002128](../../tests/test_web_agent.py#L2128) | 2128 | `"    assert 'r.second_pass_review===\"model_second_pass_unavailable\"' not in html"` | — |
| [SRC-F725E90B2A-L002129](../../tests/test_web_agent.py#L2129) | 2129 | `""` | — |
| [SRC-F725E90B2A-L002130](../../tests/test_web_agent.py#L2130) | 2130 | `""` | — |
| [SRC-F725E90B2A-L002131](../../tests/test_web_agent.py#L2131) | 2131 | `""` | — |
| [SRC-F725E90B2A-L002132](../../tests/test_web_agent.py#L2132) | 2132 | `"def test_research_error_preserves_confirmed_search_attempt_without_fabricating_counts(monkeypatch):"` | — |
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
| [SRC-F725E90B2A-L002144](../../tests/test_web_agent.py#L2144) | 2144 | `"    def failed_after_provider_result(research_plan):"` | — |
| [SRC-F725E90B2A-L002145](../../tests/test_web_agent.py#L2145) | 2145 | `"        # A completed provider result-processing state confirms that a search"` | — |
| [SRC-F725E90B2A-L002146](../../tests/test_web_agent.py#L2146) | 2146 | `"        # connector returned; the collector then fails during downstream processing."` | — |
| [SRC-F725E90B2A-L002147](../../tests/test_web_agent.py#L2147) | 2147 | `"        agent._record_provider_diagnostic("` | — |
| [SRC-F725E90B2A-L002148](../../tests/test_web_agent.py#L2148) | 2148 | `"            \"duckduckgo_html\","` | — |
| [SRC-F725E90B2A-L002149](../../tests/test_web_agent.py#L2149) | 2149 | `"            research_plan[\"queries\"][0],"` | — |
| [SRC-F725E90B2A-L002150](../../tests/test_web_agent.py#L2150) | 2150 | `"            \"ok\","` | — |
| [SRC-F725E90B2A-L002151](../../tests/test_web_agent.py#L2151) | 2151 | `"            result_count=1,"` | — |
| [SRC-F725E90B2A-L002152](../../tests/test_web_agent.py#L2152) | 2152 | `"        )"` | — |
| [SRC-F725E90B2A-L002153](../../tests/test_web_agent.py#L2153) | 2153 | `"        raise RuntimeError(\"simulated post-search pipeline failure\")"` | — |
| [SRC-F725E90B2A-L002154](../../tests/test_web_agent.py#L2154) | 2154 | `""` | — |
| [SRC-F725E90B2A-L002155](../../tests/test_web_agent.py#L2155) | 2155 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002156](../../tests/test_web_agent.py#L2156) | 2156 | `"    monkeypatch.setattr(agent, \"_collect_research\", failed_after_provider_result)"` | — |
| [SRC-F725E90B2A-L002157](../../tests/test_web_agent.py#L2157) | 2157 | `""` | — |
| [SRC-F725E90B2A-L002158](../../tests/test_web_agent.py#L2158) | 2158 | `"    result = agent.answer(\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\")"` | — |
| [SRC-F725E90B2A-L002159](../../tests/test_web_agent.py#L2159) | 2159 | `""` | — |
| [SRC-F725E90B2A-L002160](../../tests/test_web_agent.py#L2160) | 2160 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L002161](../../tests/test_web_agent.py#L2161) | 2161 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L002162](../../tests/test_web_agent.py#L2162) | 2162 | `"    assert report[\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L002163](../../tests/test_web_agent.py#L2163) | 2163 | `"    assert report[\"search_outcome\"] == \"attempted_research_error\""` | — |
| [SRC-F725E90B2A-L002164](../../tests/test_web_agent.py#L2164) | 2164 | `"    assert report[\"queries_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002165](../../tests/test_web_agent.py#L2165) | 2165 | `"    assert report[\"queries_attempted_known\"] is False"` | — |
| [SRC-F725E90B2A-L002166](../../tests/test_web_agent.py#L2166) | 2166 | `"    assert report[\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002167](../../tests/test_web_agent.py#L2167) | 2167 | `"    assert report[\"unique_sources\"] is None"` | — |
| [SRC-F725E90B2A-L002168](../../tests/test_web_agent.py#L2168) | 2168 | `"    assert report[\"pages_fetched\"] is None"` | — |
| [SRC-F725E90B2A-L002169](../../tests/test_web_agent.py#L2169) | 2169 | `""` | — |
| [SRC-F725E90B2A-L002170](../../tests/test_web_agent.py#L2170) | 2170 | `""` | — |
| [SRC-F725E90B2A-L002171](../../tests/test_web_agent.py#L2171) | 2171 | `"def test_research_error_without_provider_diagnostics_is_reported_as_unknown(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002172](../../tests/test_web_agent.py#L2172) | 2172 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002173](../../tests/test_web_agent.py#L2173) | 2173 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002174](../../tests/test_web_agent.py#L2174) | 2174 | `"        \"queries\": [\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\"],"` | — |
| [SRC-F725E90B2A-L002175](../../tests/test_web_agent.py#L2175) | 2175 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002176](../../tests/test_web_agent.py#L2176) | 2176 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002177](../../tests/test_web_agent.py#L2177) | 2177 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L002178](../../tests/test_web_agent.py#L2178) | 2178 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002179](../../tests/test_web_agent.py#L2179) | 2179 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002180](../../tests/test_web_agent.py#L2180) | 2180 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002181](../../tests/test_web_agent.py#L2181) | 2181 | `"    }"` | — |
| [SRC-F725E90B2A-L002182](../../tests/test_web_agent.py#L2182) | 2182 | `""` | — |
| [SRC-F725E90B2A-L002183](../../tests/test_web_agent.py#L2183) | 2183 | `"    def fail_before_attempt(research_plan):"` | — |
| [SRC-F725E90B2A-L002184](../../tests/test_web_agent.py#L2184) | 2184 | `"        raise RuntimeError(\"simulated scheduler failure\")"` | — |
| [SRC-F725E90B2A-L002185](../../tests/test_web_agent.py#L2185) | 2185 | `""` | — |
| [SRC-F725E90B2A-L002186](../../tests/test_web_agent.py#L2186) | 2186 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002187](../../tests/test_web_agent.py#L2187) | 2187 | `"    monkeypatch.setattr(agent, \"_collect_research\", fail_before_attempt)"` | — |
| [SRC-F725E90B2A-L002188](../../tests/test_web_agent.py#L2188) | 2188 | `""` | — |
| [SRC-F725E90B2A-L002189](../../tests/test_web_agent.py#L2189) | 2189 | `"    result = agent.answer(\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\")"` | — |
| [SRC-F725E90B2A-L002190](../../tests/test_web_agent.py#L2190) | 2190 | `""` | — |
| [SRC-F725E90B2A-L002191](../../tests/test_web_agent.py#L2191) | 2191 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L002192](../../tests/test_web_agent.py#L2192) | 2192 | `"    assert result[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002193](../../tests/test_web_agent.py#L2193) | 2193 | `"    assert report[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002194](../../tests/test_web_agent.py#L2194) | 2194 | `"    assert report[\"search_outcome\"] == \"unknown_after_research_error\""` | — |
| [SRC-F725E90B2A-L002195](../../tests/test_web_agent.py#L2195) | 2195 | `"    assert report[\"queries_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002196](../../tests/test_web_agent.py#L2196) | 2196 | `"    assert report[\"queries_attempted_known\"] is False"` | — |
| [SRC-F725E90B2A-L002197](../../tests/test_web_agent.py#L2197) | 2197 | `"    assert report[\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002198](../../tests/test_web_agent.py#L2198) | 2198 | `""` | — |
| [SRC-F725E90B2A-L002199](../../tests/test_web_agent.py#L2199) | 2199 | `""` | — |
| [SRC-F725E90B2A-L002200](../../tests/test_web_agent.py#L2200) | 2200 | `"def test_general_answer_does_not_silently_slice_overlong_model_output(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002201](../../tests/test_web_agent.py#L2201) | 2201 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002202](../../tests/test_web_agent.py#L2202) | 2202 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002203](../../tests/test_web_agent.py#L2203) | 2203 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002204](../../tests/test_web_agent.py#L2204) | 2204 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002205](../../tests/test_web_agent.py#L2205) | 2205 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L002206](../../tests/test_web_agent.py#L2206) | 2206 | `"        lambda *args, **kwargs: \"ن\" * 24_001,"` | — |
| [SRC-F725E90B2A-L002207](../../tests/test_web_agent.py#L2207) | 2207 | `"    )"` | — |
| [SRC-F725E90B2A-L002208](../../tests/test_web_agent.py#L2208) | 2208 | `""` | — |
| [SRC-F725E90B2A-L002209](../../tests/test_web_agent.py#L2209) | 2209 | `"    result = agent._answer_without_search(\"اشرح مفهومًا عامًا\", [])"` | — |
| [SRC-F725E90B2A-L002210](../../tests/test_web_agent.py#L2210) | 2210 | `""` | — |
| [SRC-F725E90B2A-L002211](../../tests/test_web_agent.py#L2211) | 2211 | `"    assert result is None"` | — |
| [SRC-F725E90B2A-L002212](../../tests/test_web_agent.py#L2212) | 2212 | `""` | — |
| [SRC-F725E90B2A-L002213](../../tests/test_web_agent.py#L2213) | 2213 | `""` | — |
| [SRC-F725E90B2A-L002214](../../tests/test_web_agent.py#L2214) | 2214 | `"def test_frontend_discloses_unknown_counts_after_research_error():"` | — |
| [SRC-F725E90B2A-L002215](../../tests/test_web_agent.py#L2215) | 2215 | `"    html = (Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002216](../../tests/test_web_agent.py#L2216) | 2216 | `"    assert '[\"attempted_research_error\",\"unknown_after_research_error\"].includes(r.search_outcome)' in html"` | — |
| [SRC-F725E90B2A-L002217](../../tests/test_web_agent.py#L2217) | 2217 | `"    assert \"لم يمكن تحديد عدد المصادر القابلة للاستخدام\" in html"` | — |
| [SRC-F725E90B2A-L002218](../../tests/test_web_agent.py#L2218) | 2218 | `"    assert \"غير محدد\" in html"` | — |
| [SRC-F725E90B2A-L002219](../../tests/test_web_agent.py#L2219) | 2219 | `"    assert 'const score=(researchErrorOutcome\|\|lead)?null:Number(e.coverage_score\|\|0)' not in html"` | — |
| [SRC-F725E90B2A-L002220](../../tests/test_web_agent.py#L2220) | 2220 | `"    assert \"مؤشر تغطية البحث:\" not in html"` | — |
| [SRC-F725E90B2A-L002221](../../tests/test_web_agent.py#L2221) | 2221 | `"    assert '\"تغطية الأدلة: \"+scoreLabel' in html"` | — |
| [SRC-F725E90B2A-L002222](../../tests/test_web_agent.py#L2222) | 2222 | `"    assert \"يصف هذا الوصف اتساع الأدلة المتاحة ولا يمثل احتمال صحة الإجابة\" in html"` | — |
| [SRC-F725E90B2A-L002223](../../tests/test_web_agent.py#L2223) | 2223 | `"    assert \"تعذر تحديد تغطية البحث لأن مسار تجميع الأدلة لم يكتمل\" in html"` | — |
| [SRC-F725E90B2A-L002224](../../tests/test_web_agent.py#L2224) | 2224 | `""` | — |
| [SRC-F725E90B2A-L002225](../../tests/test_web_agent.py#L2225) | 2225 | `""` | — |
| [SRC-F725E90B2A-L002226](../../tests/test_web_agent.py#L2226) | 2226 | `"def test_generic_provider_failure_does_not_claim_search_attempt_as_confirmed(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002227](../../tests/test_web_agent.py#L2227) | 2227 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002228](../../tests/test_web_agent.py#L2228) | 2228 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002229](../../tests/test_web_agent.py#L2229) | 2229 | `"        \"queries\": [\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\"],"` | — |
| [SRC-F725E90B2A-L002230](../../tests/test_web_agent.py#L2230) | 2230 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002231](../../tests/test_web_agent.py#L2231) | 2231 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002232](../../tests/test_web_agent.py#L2232) | 2232 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L002233](../../tests/test_web_agent.py#L2233) | 2233 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002234](../../tests/test_web_agent.py#L2234) | 2234 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002235](../../tests/test_web_agent.py#L2235) | 2235 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002236](../../tests/test_web_agent.py#L2236) | 2236 | `"    }"` | — |
| [SRC-F725E90B2A-L002237](../../tests/test_web_agent.py#L2237) | 2237 | `""` | — |
| [SRC-F725E90B2A-L002238](../../tests/test_web_agent.py#L2238) | 2238 | `"    def fail_after_generic_provider_error(research_plan):"` | — |
| [SRC-F725E90B2A-L002239](../../tests/test_web_agent.py#L2239) | 2239 | `"        # A generic failed diagnostic does not prove whether the network request"` | — |
| [SRC-F725E90B2A-L002240](../../tests/test_web_agent.py#L2240) | 2240 | `"        # was actually sent; it must not be upgraded to a confirmed attempt."` | — |
| [SRC-F725E90B2A-L002241](../../tests/test_web_agent.py#L2241) | 2241 | `"        agent._record_provider_diagnostic("` | — |
| [SRC-F725E90B2A-L002242](../../tests/test_web_agent.py#L2242) | 2242 | `"            \"duckduckgo_html\","` | — |
| [SRC-F725E90B2A-L002243](../../tests/test_web_agent.py#L2243) | 2243 | `"            research_plan[\"queries\"][0],"` | — |
| [SRC-F725E90B2A-L002244](../../tests/test_web_agent.py#L2244) | 2244 | `"            \"failed\","` | — |
| [SRC-F725E90B2A-L002245](../../tests/test_web_agent.py#L2245) | 2245 | `"            error=\"simulated failure before request send\","` | — |
| [SRC-F725E90B2A-L002246](../../tests/test_web_agent.py#L2246) | 2246 | `"        )"` | — |
| [SRC-F725E90B2A-L002247](../../tests/test_web_agent.py#L2247) | 2247 | `"        raise RuntimeError(\"simulated research pipeline failure\")"` | — |
| [SRC-F725E90B2A-L002248](../../tests/test_web_agent.py#L2248) | 2248 | `""` | — |
| [SRC-F725E90B2A-L002249](../../tests/test_web_agent.py#L2249) | 2249 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002250](../../tests/test_web_agent.py#L2250) | 2250 | `"    monkeypatch.setattr(agent, \"_collect_research\", fail_after_generic_provider_error)"` | — |
| [SRC-F725E90B2A-L002251](../../tests/test_web_agent.py#L2251) | 2251 | `""` | — |
| [SRC-F725E90B2A-L002252](../../tests/test_web_agent.py#L2252) | 2252 | `"    result = agent.answer(\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\")"` | — |
| [SRC-F725E90B2A-L002253](../../tests/test_web_agent.py#L2253) | 2253 | `""` | — |
| [SRC-F725E90B2A-L002254](../../tests/test_web_agent.py#L2254) | 2254 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L002255](../../tests/test_web_agent.py#L2255) | 2255 | `"    assert result[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002256](../../tests/test_web_agent.py#L2256) | 2256 | `"    assert report[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002257](../../tests/test_web_agent.py#L2257) | 2257 | `"    assert report[\"search_outcome\"] == \"unknown_after_research_error\""` | — |
| [SRC-F725E90B2A-L002258](../../tests/test_web_agent.py#L2258) | 2258 | `"    assert report[\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002259](../../tests/test_web_agent.py#L2259) | 2259 | `"    assert report[\"unique_sources\"] is None"` | — |
| [SRC-F725E90B2A-L002260](../../tests/test_web_agent.py#L2260) | 2260 | `""` | — |
| [SRC-F725E90B2A-L002261](../../tests/test_web_agent.py#L2261) | 2261 | `""` | — |
| [SRC-F725E90B2A-L002262](../../tests/test_web_agent.py#L2262) | 2262 | `""` | — |
| [SRC-F725E90B2A-L002263](../../tests/test_web_agent.py#L2263) | 2263 | `"def test_diagnostics_tries_fallback_probe_when_first_probe_has_no_results(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002264](../../tests/test_web_agent.py#L2264) | 2264 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002265](../../tests/test_web_agent.py#L2265) | 2265 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L002266](../../tests/test_web_agent.py#L2266) | 2266 | `""` | — |
| [SRC-F725E90B2A-L002267](../../tests/test_web_agent.py#L2267) | 2267 | `"    def search(query):"` | — |
| [SRC-F725E90B2A-L002268](../../tests/test_web_agent.py#L2268) | 2268 | `"        calls.append(query)"` | — |
| [SRC-F725E90B2A-L002269](../../tests/test_web_agent.py#L2269) | 2269 | `"        if len(calls) == 1:"` | — |
| [SRC-F725E90B2A-L002270](../../tests/test_web_agent.py#L2270) | 2270 | `"            return []"` | — |
| [SRC-F725E90B2A-L002271](../../tests/test_web_agent.py#L2271) | 2271 | `"        return ["` | — |
| [SRC-F725E90B2A-L002272](../../tests/test_web_agent.py#L2272) | 2272 | `"            {"` | — |
| [SRC-F725E90B2A-L002273](../../tests/test_web_agent.py#L2273) | 2273 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-F725E90B2A-L002274](../../tests/test_web_agent.py#L2274) | 2274 | `"                \"title\": \"OpenAI official website\","` | — |
| [SRC-F725E90B2A-L002275](../../tests/test_web_agent.py#L2275) | 2275 | `"                \"url\": \"https://openai.com/\","` | — |
| [SRC-F725E90B2A-L002276](../../tests/test_web_agent.py#L2276) | 2276 | `"                \"snippet\": \"Official website and products\","` | — |
| [SRC-F725E90B2A-L002277](../../tests/test_web_agent.py#L2277) | 2277 | `"            }"` | — |
| [SRC-F725E90B2A-L002278](../../tests/test_web_agent.py#L2278) | 2278 | `"        ]"` | — |
| [SRC-F725E90B2A-L002279](../../tests/test_web_agent.py#L2279) | 2279 | `""` | — |
| [SRC-F725E90B2A-L002280](../../tests/test_web_agent.py#L2280) | 2280 | `"    monkeypatch.setattr(agent, \"_search_web\", search)"` | — |
| [SRC-F725E90B2A-L002281](../../tests/test_web_agent.py#L2281) | 2281 | `"    monkeypatch.setattr(agent, \"_request_completion\", lambda *args, **kwargs: \"OK\")"` | — |
| [SRC-F725E90B2A-L002282](../../tests/test_web_agent.py#L2282) | 2282 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002283](../../tests/test_web_agent.py#L2283) | 2283 | `""` | — |
| [SRC-F725E90B2A-L002284](../../tests/test_web_agent.py#L2284) | 2284 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L002285](../../tests/test_web_agent.py#L2285) | 2285 | `""` | — |
| [SRC-F725E90B2A-L002286](../../tests/test_web_agent.py#L2286) | 2286 | `"    assert len(calls) == 2"` | — |
| [SRC-F725E90B2A-L002287](../../tests/test_web_agent.py#L2287) | 2287 | `"    assert report[\"checks\"][\"web_search\"][\"status\"] == \"passed\""` | — |
| [SRC-F725E90B2A-L002288](../../tests/test_web_agent.py#L2288) | 2288 | `"    assert report[\"checks\"][\"web_search\"][\"probe_count\"] == 2"` | — |
| [SRC-F725E90B2A-L002289](../../tests/test_web_agent.py#L2289) | 2289 | `"    assert report[\"checks\"][\"web_search\"][\"result_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002290](../../tests/test_web_agent.py#L2290) | 2290 | `""` | — |
| [SRC-F725E90B2A-L002291](../../tests/test_web_agent.py#L2291) | 2291 | `""` | — |
| [SRC-F725E90B2A-L002292](../../tests/test_web_agent.py#L2292) | 2292 | `"def test_lead_discovery_is_distinct_from_listing_search():"` | — |
| [SRC-F725E90B2A-L002293](../../tests/test_web_agent.py#L2293) | 2293 | `"    assert WebAgent._is_lead_search(\"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية\")"` | — |
| [SRC-F725E90B2A-L002294](../../tests/test_web_agent.py#L2294) | 2294 | `"    assert WebAgent._is_lead_search(\"Find buyers looking to buy apartments\")"` | — |
| [SRC-F725E90B2A-L002295](../../tests/test_web_agent.py#L2295) | 2295 | `"    assert not WebAgent._is_lead_search(\"ابحث عن شقق للبيع في العاصمة الإدارية\")"` | — |
| [SRC-F725E90B2A-L002296](../../tests/test_web_agent.py#L2296) | 2296 | `"    assert not WebAgent._is_lead_search(\"Find apartments for sale\")"` | — |
| [SRC-F725E90B2A-L002297](../../tests/test_web_agent.py#L2297) | 2297 | `""` | — |
| [SRC-F725E90B2A-L002298](../../tests/test_web_agent.py#L2298) | 2298 | `""` | — |
| [SRC-F725E90B2A-L002299](../../tests/test_web_agent.py#L2299) | 2299 | `"def test_lead_queries_are_product_anchored_and_sector_neutral():"` | — |
| [SRC-F725E90B2A-L002300](../../tests/test_web_agent.py#L2300) | 2300 | `"    vehicle_queries = WebAgent._lead_generation_queries("` | — |
| [SRC-F725E90B2A-L002301](../../tests/test_web_agent.py#L2301) | 2301 | `"        \"ابحث عن عميل يريد شراء سيارة كهربائية في القاهرة\""` | — |
| [SRC-F725E90B2A-L002302](../../tests/test_web_agent.py#L2302) | 2302 | `"    )"` | — |
| [SRC-F725E90B2A-L002303](../../tests/test_web_agent.py#L2303) | 2303 | `"    industrial_queries = WebAgent._lead_generation_queries("` | — |
| [SRC-F725E90B2A-L002304](../../tests/test_web_agent.py#L2304) | 2304 | `"        \"ابحث عن عميل يريد شراء نظام إنذار حريق صناعي\""` | — |
| [SRC-F725E90B2A-L002305](../../tests/test_web_agent.py#L2305) | 2305 | `"    )"` | — |
| [SRC-F725E90B2A-L002306](../../tests/test_web_agent.py#L2306) | 2306 | `"    assert vehicle_queries and industrial_queries"` | — |
| [SRC-F725E90B2A-L002307](../../tests/test_web_agent.py#L2307) | 2307 | `"    assert all(\"شقه\" not in query and \"تمليك\" not in query for query in vehicle_queries)"` | — |
| [SRC-F725E90B2A-L002308](../../tests/test_web_agent.py#L2308) | 2308 | `"    assert all(\"شقه\" not in query and \"تمليك\" not in query for query in industrial_queries)"` | — |
| [SRC-F725E90B2A-L002309](../../tests/test_web_agent.py#L2309) | 2309 | `"    assert any(\"سياره كهرباييه\" in query for query in vehicle_queries)"` | — |
| [SRC-F725E90B2A-L002310](../../tests/test_web_agent.py#L2310) | 2310 | `"    assert any(\"نظام انذار حريق صناعي\" in query for query in industrial_queries)"` | — |
| [SRC-F725E90B2A-L002311](../../tests/test_web_agent.py#L2311) | 2311 | `""` | — |
| [SRC-F725E90B2A-L002312](../../tests/test_web_agent.py#L2312) | 2312 | `""` | — |
| [SRC-F725E90B2A-L002313](../../tests/test_web_agent.py#L2313) | 2313 | `"def test_buyer_intent_evidence_supports_non_property_purchase_requests():"` | — |
| [SRC-F725E90B2A-L002314](../../tests/test_web_agent.py#L2314) | 2314 | `"    source = {"` | — |
| [SRC-F725E90B2A-L002315](../../tests/test_web_agent.py#L2315) | 2315 | `"        \"title\": \"طلب شراء نظام إنذار حريق\","` | — |
| [SRC-F725E90B2A-L002316](../../tests/test_web_agent.py#L2316) | 2316 | `"        \"snippet\": \"الجهة تبحث عن مورد لنظام إنذار حريق صناعي.\","` | — |
| [SRC-F725E90B2A-L002317](../../tests/test_web_agent.py#L2317) | 2317 | `"        \"page_text\": \"نرغب في شراء نظام إنذار حريق للمصنع خلال هذا الربع.\","` | — |
| [SRC-F725E90B2A-L002318](../../tests/test_web_agent.py#L2318) | 2318 | `"    }"` | — |
| [SRC-F725E90B2A-L002319](../../tests/test_web_agent.py#L2319) | 2319 | `"    signal = WebAgent._lead_intent_evidence(source)"` | — |
| [SRC-F725E90B2A-L002320](../../tests/test_web_agent.py#L2320) | 2320 | `"    assert signal is not None"` | — |
| [SRC-F725E90B2A-L002321](../../tests/test_web_agent.py#L2321) | 2321 | `"    assert signal[\"signal_type\"] == \"direct_purchase_request\""` | — |
| [SRC-F725E90B2A-L002322](../../tests/test_web_agent.py#L2322) | 2322 | `"    assert signal[\"product_fit\"] == \"unassessed\""` | — |
| [SRC-F725E90B2A-L002323](../../tests/test_web_agent.py#L2323) | 2323 | `"    assert signal[\"basis\"] == \"page_text\""` | — |
| [SRC-F725E90B2A-L002324](../../tests/test_web_agent.py#L2324) | 2324 | `""` | — |
| [SRC-F725E90B2A-L002325](../../tests/test_web_agent.py#L2325) | 2325 | `""` | — |
| [SRC-F725E90B2A-L002326](../../tests/test_web_agent.py#L2326) | 2326 | `"def test_buyer_intent_evidence_distinguishes_rfq_from_direct_purchase():"` | — |
| [SRC-F725E90B2A-L002327](../../tests/test_web_agent.py#L2327) | 2327 | `"    source = {"` | — |
| [SRC-F725E90B2A-L002328](../../tests/test_web_agent.py#L2328) | 2328 | `"        \"title\": \"طلب عرض سعر لتوريد معدات\","` | — |
| [SRC-F725E90B2A-L002329](../../tests/test_web_agent.py#L2329) | 2329 | `"        \"snippet\": \"نرجو تقديم عرض سعر للمواصفات المرفقة.\","` | — |
| [SRC-F725E90B2A-L002330](../../tests/test_web_agent.py#L2330) | 2330 | `"        \"page_text\": \"طلب عرض سعر لتوريد معدات للمشروع.\","` | — |
| [SRC-F725E90B2A-L002331](../../tests/test_web_agent.py#L2331) | 2331 | `"    }"` | — |
| [SRC-F725E90B2A-L002332](../../tests/test_web_agent.py#L2332) | 2332 | `"    signal = WebAgent._lead_intent_evidence(source)"` | — |
| [SRC-F725E90B2A-L002333](../../tests/test_web_agent.py#L2333) | 2333 | `"    assert signal is not None"` | — |
| [SRC-F725E90B2A-L002334](../../tests/test_web_agent.py#L2334) | 2334 | `"    assert signal[\"signal_type\"] == \"request_for_quotation\""` | — |
| [SRC-F725E90B2A-L002335](../../tests/test_web_agent.py#L2335) | 2335 | `"    assert signal[\"product_fit\"] == \"unassessed\""` | — |
| [SRC-F725E90B2A-L002336](../../tests/test_web_agent.py#L2336) | 2336 | `""` | — |
| [SRC-F725E90B2A-L002337](../../tests/test_web_agent.py#L2337) | 2337 | `""` | — |
| [SRC-F725E90B2A-L002338](../../tests/test_web_agent.py#L2338) | 2338 | `"def test_buyer_intent_evidence_distinguishes_stated_need_from_purchase():"` | — |
| [SRC-F725E90B2A-L002339](../../tests/test_web_agent.py#L2339) | 2339 | `"    source = {"` | — |
| [SRC-F725E90B2A-L002340](../../tests/test_web_agent.py#L2340) | 2340 | `"        \"title\": \"بدور على مورد صيانة\","` | — |
| [SRC-F725E90B2A-L002341](../../tests/test_web_agent.py#L2341) | 2341 | `"        \"snippet\": \"نحتاج إلى مورد صيانة موثوق.\","` | — |
| [SRC-F725E90B2A-L002342](../../tests/test_web_agent.py#L2342) | 2342 | `"        \"page_text\": \"نبحث عن مورد صيانة للمصنع.\","` | — |
| [SRC-F725E90B2A-L002343](../../tests/test_web_agent.py#L2343) | 2343 | `"    }"` | — |
| [SRC-F725E90B2A-L002344](../../tests/test_web_agent.py#L2344) | 2344 | `"    signal = WebAgent._lead_intent_evidence(source)"` | — |
| [SRC-F725E90B2A-L002345](../../tests/test_web_agent.py#L2345) | 2345 | `"    assert signal is not None"` | — |
| [SRC-F725E90B2A-L002346](../../tests/test_web_agent.py#L2346) | 2346 | `"    assert signal[\"signal_type\"] == \"stated_need\""` | — |
| [SRC-F725E90B2A-L002347](../../tests/test_web_agent.py#L2347) | 2347 | `"    assert signal[\"product_fit\"] == \"unassessed\""` | — |
| [SRC-F725E90B2A-L002348](../../tests/test_web_agent.py#L2348) | 2348 | `""` | — |
| [SRC-F725E90B2A-L002349](../../tests/test_web_agent.py#L2349) | 2349 | `""` | — |
| [SRC-F725E90B2A-L002350](../../tests/test_web_agent.py#L2350) | 2350 | `"def test_seller_looking_for_a_buyer_is_not_a_buyer_demand_signal():"` | — |
| [SRC-F725E90B2A-L002351](../../tests/test_web_agent.py#L2351) | 2351 | `"    seller = {"` | — |
| [SRC-F725E90B2A-L002352](../../tests/test_web_agent.py#L2352) | 2352 | `"        \"title\": \"نبحث عن مشتري لسيارة مستعملة\","` | — |
| [SRC-F725E90B2A-L002353](../../tests/test_web_agent.py#L2353) | 2353 | `"        \"snippet\": \"مطلوب مشتري جاد للتواصل مع المالك.\","` | — |
| [SRC-F725E90B2A-L002354](../../tests/test_web_agent.py#L2354) | 2354 | `"        \"page_text\": \"نبحث عن مشتري لسيارة مستعملة بحالة جيدة.\","` | — |
| [SRC-F725E90B2A-L002355](../../tests/test_web_agent.py#L2355) | 2355 | `"    }"` | — |
| [SRC-F725E90B2A-L002356](../../tests/test_web_agent.py#L2356) | 2356 | `"    english_seller = {"` | — |
| [SRC-F725E90B2A-L002357](../../tests/test_web_agent.py#L2357) | 2357 | `"        \"title\": \"Looking for a buyer for our used equipment\","` | — |
| [SRC-F725E90B2A-L002358](../../tests/test_web_agent.py#L2358) | 2358 | `"        \"snippet\": \"Buyer wanted; seller will contact interested parties.\","` | — |
| [SRC-F725E90B2A-L002359](../../tests/test_web_agent.py#L2359) | 2359 | `"        \"page_text\": \"We are looking for a buyer for our used equipment.\","` | — |
| [SRC-F725E90B2A-L002360](../../tests/test_web_agent.py#L2360) | 2360 | `"    }"` | — |
| [SRC-F725E90B2A-L002361](../../tests/test_web_agent.py#L2361) | 2361 | `"    assert WebAgent._lead_intent_evidence(seller) is None"` | — |
| [SRC-F725E90B2A-L002362](../../tests/test_web_agent.py#L2362) | 2362 | `"    assert WebAgent._lead_intent_evidence(english_seller) is None"` | — |
| [SRC-F725E90B2A-L002363](../../tests/test_web_agent.py#L2363) | 2363 | `""` | — |
| [SRC-F725E90B2A-L002364](../../tests/test_web_agent.py#L2364) | 2364 | `""` | — |
| [SRC-F725E90B2A-L002365](../../tests/test_web_agent.py#L2365) | 2365 | `"def test_vehicle_request_rejects_property_buyer_signal():"` | — |
| [SRC-F725E90B2A-L002366](../../tests/test_web_agent.py#L2366) | 2366 | `"    source = {"` | — |
| [SRC-F725E90B2A-L002367](../../tests/test_web_agent.py#L2367) | 2367 | `"        \"title\": \"Looking to buy an apartment\","` | — |
| [SRC-F725E90B2A-L002368](../../tests/test_web_agent.py#L2368) | 2368 | `"        \"snippet\": \"Looking to buy an apartment in Cairo.\","` | — |
| [SRC-F725E90B2A-L002369](../../tests/test_web_agent.py#L2369) | 2369 | `"        \"page_text\": \"I want to buy an apartment this year.\","` | — |
| [SRC-F725E90B2A-L002370](../../tests/test_web_agent.py#L2370) | 2370 | `"    }"` | — |
| [SRC-F725E90B2A-L002371](../../tests/test_web_agent.py#L2371) | 2371 | `"    assert WebAgent._lead_intent_evidence(source, \"ابحث عن مشترين لسيارة كهربائية\") is None"` | — |
| [SRC-F725E90B2A-L002372](../../tests/test_web_agent.py#L2372) | 2372 | `""` | — |
| [SRC-F725E90B2A-L002373](../../tests/test_web_agent.py#L2373) | 2373 | `""` | — |
| [SRC-F725E90B2A-L002374](../../tests/test_web_agent.py#L2374) | 2374 | `"def test_property_request_rejects_vehicle_buyer_signal():"` | — |
| [SRC-F725E90B2A-L002375](../../tests/test_web_agent.py#L2375) | 2375 | `"    source = {"` | — |
| [SRC-F725E90B2A-L002376](../../tests/test_web_agent.py#L2376) | 2376 | `"        \"title\": \"Looking to buy a used car\","` | — |
| [SRC-F725E90B2A-L002377](../../tests/test_web_agent.py#L2377) | 2377 | `"        \"snippet\": \"Looking to buy a used car in Cairo.\","` | — |
| [SRC-F725E90B2A-L002378](../../tests/test_web_agent.py#L2378) | 2378 | `"        \"page_text\": \"I want to buy a used car this year.\","` | — |
| [SRC-F725E90B2A-L002379](../../tests/test_web_agent.py#L2379) | 2379 | `"    }"` | — |
| [SRC-F725E90B2A-L002380](../../tests/test_web_agent.py#L2380) | 2380 | `"    assert WebAgent._lead_intent_evidence(source, \"ابحث عن مشترين لشقة في القاهرة\") is None"` | — |
| [SRC-F725E90B2A-L002381](../../tests/test_web_agent.py#L2381) | 2381 | `""` | — |
| [SRC-F725E90B2A-L002382](../../tests/test_web_agent.py#L2382) | 2382 | `""` | — |
| [SRC-F725E90B2A-L002383](../../tests/test_web_agent.py#L2383) | 2383 | `"def test_arabic_typo_repair_keeps_product_topic_not_instruction_text():"` | — |
| [SRC-F725E90B2A-L002384](../../tests/test_web_agent.py#L2384) | 2384 | `"    queries = WebAgent._lead_generation_queries("` | — |
| [SRC-F725E90B2A-L002385](../../tests/test_web_agent.py#L2385) | 2385 | `"        \"ابحث عن ١٠ عملاش يريدون شرا شقة في التجمع الخامس\""` | — |
| [SRC-F725E90B2A-L002386](../../tests/test_web_agent.py#L2386) | 2386 | `"    )"` | — |
| [SRC-F725E90B2A-L002387](../../tests/test_web_agent.py#L2387) | 2387 | `"    assert queries"` | — |
| [SRC-F725E90B2A-L002388](../../tests/test_web_agent.py#L2388) | 2388 | `"    assert any(\"شقه في التجمع الخامس\" in query for query in queries)"` | — |
| [SRC-F725E90B2A-L002389](../../tests/test_web_agent.py#L2389) | 2389 | `"    assert all(\"عملاش\" not in query for query in queries)"` | — |
| [SRC-F725E90B2A-L002390](../../tests/test_web_agent.py#L2390) | 2390 | `""` | — |
| [SRC-F725E90B2A-L002391](../../tests/test_web_agent.py#L2391) | 2391 | `""` | — |
| [SRC-F725E90B2A-L002392](../../tests/test_web_agent.py#L2392) | 2392 | `"def test_lead_fallback_only_shows_sources_with_qualified_public_demand():"` | — |
| [SRC-F725E90B2A-L002393](../../tests/test_web_agent.py#L2393) | 2393 | `"    qualified = {"` | — |
| [SRC-F725E90B2A-L002394](../../tests/test_web_agent.py#L2394) | 2394 | `"        \"lead_qualification\": \"public_demand_signal\","` | — |
| [SRC-F725E90B2A-L002395](../../tests/test_web_agent.py#L2395) | 2395 | `"        \"lead_intent_evidence\": {\"phrase\": \"طلب عرض سعر\", \"signal_type\": \"request_for_quotation\"},"` | — |
| [SRC-F725E90B2A-L002396](../../tests/test_web_agent.py#L2396) | 2396 | `"        \"title\": \"طلب عرض سعر لتوريد معدات\","` | — |
| [SRC-F725E90B2A-L002397](../../tests/test_web_agent.py#L2397) | 2397 | `"        \"snippet\": \"طلب عرض سعر لمشروع صناعي\","` | — |
| [SRC-F725E90B2A-L002398](../../tests/test_web_agent.py#L2398) | 2398 | `"        \"url\": \"https://example.org/rfq\","` | — |
| [SRC-F725E90B2A-L002399](../../tests/test_web_agent.py#L2399) | 2399 | `"    }"` | — |
| [SRC-F725E90B2A-L002400](../../tests/test_web_agent.py#L2400) | 2400 | `"    related = {"` | — |
| [SRC-F725E90B2A-L002401](../../tests/test_web_agent.py#L2401) | 2401 | `"        \"lead_qualification\": \"related_result_not_lead\","` | — |
| [SRC-F725E90B2A-L002402](../../tests/test_web_agent.py#L2402) | 2402 | `"        \"title\": \"معدات للبيع\","` | — |
| [SRC-F725E90B2A-L002403](../../tests/test_web_agent.py#L2403) | 2403 | `"        \"snippet\": \"قائمة بيع عامة\","` | — |
| [SRC-F725E90B2A-L002404](../../tests/test_web_agent.py#L2404) | 2404 | `"        \"url\": \"https://example.org/listing\","` | — |
| [SRC-F725E90B2A-L002405](../../tests/test_web_agent.py#L2405) | 2405 | `"    }"` | — |
| [SRC-F725E90B2A-L002406](../../tests/test_web_agent.py#L2406) | 2406 | `"    answer = _fallback_lead_answer([qualified, related])"` | — |
| [SRC-F725E90B2A-L002407](../../tests/test_web_agent.py#L2407) | 2407 | `"    assert \"https://example.org/rfq\" in answer"` | — |
| [SRC-F725E90B2A-L002408](../../tests/test_web_agent.py#L2408) | 2408 | `"    assert \"https://example.org/listing\" not in answer"` | — |
| [SRC-F725E90B2A-L002409](../../tests/test_web_agent.py#L2409) | 2409 | `"    assert \"ملاءمة المنتج\" in answer"` | — |
| [SRC-F725E90B2A-L002410](../../tests/test_web_agent.py#L2410) | 2410 | `""` | — |
| [SRC-F725E90B2A-L002411](../../tests/test_web_agent.py#L2411) | 2411 | `""` | — |
| [SRC-F725E90B2A-L002412](../../tests/test_web_agent.py#L2412) | 2412 | `"def test_buyer_intent_evidence_requires_explicit_purchase_signal():"` | — |
| [SRC-F725E90B2A-L002413](../../tests/test_web_agent.py#L2413) | 2413 | `"    listing = {"` | — |
| [SRC-F725E90B2A-L002414](../../tests/test_web_agent.py#L2414) | 2414 | `"        \"title\": \"شقق للبيع في العاصمة الإدارية الجديدة\","` | — |
| [SRC-F725E90B2A-L002415](../../tests/test_web_agent.py#L2415) | 2415 | `"        \"snippet\": \"أفضل شقق للبيع بالتقسيط\","` | — |
| [SRC-F725E90B2A-L002416](../../tests/test_web_agent.py#L2416) | 2416 | `"        \"page_text\": \"إعلانات وحدات سكنية للبيع بمساحات مختلفة.\","` | — |
| [SRC-F725E90B2A-L002417](../../tests/test_web_agent.py#L2417) | 2417 | `"    }"` | — |
| [SRC-F725E90B2A-L002418](../../tests/test_web_agent.py#L2418) | 2418 | `"    buyer_post = {"` | — |
| [SRC-F725E90B2A-L002419](../../tests/test_web_agent.py#L2419) | 2419 | `"        \"title\": \"بدور على شقة تمليك في العاصمة الإدارية\","` | — |
| [SRC-F725E90B2A-L002420](../../tests/test_web_agent.py#L2420) | 2420 | `"        \"snippet\": \"مطلوب شقة تمليك في العاصمة الإدارية.\","` | — |
| [SRC-F725E90B2A-L002421](../../tests/test_web_agent.py#L2421) | 2421 | `"        \"page_text\": \"أنا بدور على شقة تمليك في العاصمة الإدارية وعايز أشتري خلال شهر.\","` | — |
| [SRC-F725E90B2A-L002422](../../tests/test_web_agent.py#L2422) | 2422 | `"    }"` | — |
| [SRC-F725E90B2A-L002423](../../tests/test_web_agent.py#L2423) | 2423 | `"    assert WebAgent._lead_intent_evidence(listing) is None"` | — |
| [SRC-F725E90B2A-L002424](../../tests/test_web_agent.py#L2424) | 2424 | `"    signal = WebAgent._lead_intent_evidence(buyer_post)"` | — |
| [SRC-F725E90B2A-L002425](../../tests/test_web_agent.py#L2425) | 2425 | `"    assert signal is not None"` | — |
| [SRC-F725E90B2A-L002426](../../tests/test_web_agent.py#L2426) | 2426 | `"    assert signal[\"basis\"] == \"page_text\""` | — |
| [SRC-F725E90B2A-L002427](../../tests/test_web_agent.py#L2427) | 2427 | `""` | — |
| [SRC-F725E90B2A-L002428](../../tests/test_web_agent.py#L2428) | 2428 | `""` | — |
| [SRC-F725E90B2A-L002429](../../tests/test_web_agent.py#L2429) | 2429 | `"def test_lead_generation_does_not_present_sale_listings_as_buyers(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002430](../../tests/test_web_agent.py#L2430) | 2430 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002431](../../tests/test_web_agent.py#L2431) | 2431 | `"    question = \"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\""` | — |
| [SRC-F725E90B2A-L002432](../../tests/test_web_agent.py#L2432) | 2432 | `"    source_a = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002433](../../tests/test_web_agent.py#L2433) | 2433 | `"    source_a.update({"` | — |
| [SRC-F725E90B2A-L002434](../../tests/test_web_agent.py#L2434) | 2434 | `"        \"title\": \"شقق للبيع في العاصمة الإدارية الجديدة\","` | — |
| [SRC-F725E90B2A-L002435](../../tests/test_web_agent.py#L2435) | 2435 | `"        \"snippet\": \"قارن أسعار الشقق والمساحات وخطط السداد.\","` | — |
| [SRC-F725E90B2A-L002436](../../tests/test_web_agent.py#L2436) | 2436 | `"        \"page_text\": \"إعلانات شقق للبيع من شركات تطوير عقاري.\","` | — |
| [SRC-F725E90B2A-L002437](../../tests/test_web_agent.py#L2437) | 2437 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002438](../../tests/test_web_agent.py#L2438) | 2438 | `"    })"` | — |
| [SRC-F725E90B2A-L002439](../../tests/test_web_agent.py#L2439) | 2439 | `"    source_b = sample_source(1)"` | — |
| [SRC-F725E90B2A-L002440](../../tests/test_web_agent.py#L2440) | 2440 | `"    source_b.update({"` | — |
| [SRC-F725E90B2A-L002441](../../tests/test_web_agent.py#L2441) | 2441 | `"        \"title\": \"مشروعات عقارية في العاصمة الإدارية\","` | — |
| [SRC-F725E90B2A-L002442](../../tests/test_web_agent.py#L2442) | 2442 | `"        \"snippet\": \"تعرف على الوحدات السكنية المتاحة للبيع.\","` | — |
| [SRC-F725E90B2A-L002443](../../tests/test_web_agent.py#L2443) | 2443 | `"        \"page_text\": \"معلومات عامة عن مشروعات وشقق للبيع.\","` | — |
| [SRC-F725E90B2A-L002444](../../tests/test_web_agent.py#L2444) | 2444 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002445](../../tests/test_web_agent.py#L2445) | 2445 | `"    })"` | — |
| [SRC-F725E90B2A-L002446](../../tests/test_web_agent.py#L2446) | 2446 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002447](../../tests/test_web_agent.py#L2447) | 2447 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002448](../../tests/test_web_agent.py#L2448) | 2448 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002449](../../tests/test_web_agent.py#L2449) | 2449 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002450](../../tests/test_web_agent.py#L2450) | 2450 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002451](../../tests/test_web_agent.py#L2451) | 2451 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002452](../../tests/test_web_agent.py#L2452) | 2452 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002453](../../tests/test_web_agent.py#L2453) | 2453 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002454](../../tests/test_web_agent.py#L2454) | 2454 | `"    }"` | — |
| [SRC-F725E90B2A-L002455](../../tests/test_web_agent.py#L2455) | 2455 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda q, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002456](../../tests/test_web_agent.py#L2456) | 2456 | `"    monkeypatch.setattr(agent, \"_collect_research\", lambda p: ("` | — |
| [SRC-F725E90B2A-L002457](../../tests/test_web_agent.py#L2457) | 2457 | `"        [source_a, source_b], [], {"` | — |
| [SRC-F725E90B2A-L002458](../../tests/test_web_agent.py#L2458) | 2458 | `"            \"queries_planned\": 1, \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L002459](../../tests/test_web_agent.py#L2459) | 2459 | `"            \"query_results\": [{\"query\": question, \"results\": 2}],"` | — |
| [SRC-F725E90B2A-L002460](../../tests/test_web_agent.py#L2460) | 2460 | `"            \"unique_sources\": 2, \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L002461](../../tests/test_web_agent.py#L2461) | 2461 | `"            \"providers_used\": [\"test_provider\"], \"provider_counts\": {\"test_provider\": 2},"` | — |
| [SRC-F725E90B2A-L002462](../../tests/test_web_agent.py#L2462) | 2462 | `"            \"platform_counts\": {\"web\": 2}, \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002463](../../tests/test_web_agent.py#L2463) | 2463 | `"            \"depth\": \"standard\", \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002464](../../tests/test_web_agent.py#L2464) | 2464 | `"        }"` | — |
| [SRC-F725E90B2A-L002465](../../tests/test_web_agent.py#L2465) | 2465 | `"    ))"` | — |
| [SRC-F725E90B2A-L002466](../../tests/test_web_agent.py#L2466) | 2466 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002467](../../tests/test_web_agent.py#L2467) | 2467 | `"        agent, \"_generate\","` | — |
| [SRC-F725E90B2A-L002468](../../tests/test_web_agent.py#L2468) | 2468 | `"        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError(\"must not synthesize false leads\")),"` | — |
| [SRC-F725E90B2A-L002469](../../tests/test_web_agent.py#L2469) | 2469 | `"    )"` | — |
| [SRC-F725E90B2A-L002470](../../tests/test_web_agent.py#L2470) | 2470 | `""` | — |
| [SRC-F725E90B2A-L002471](../../tests/test_web_agent.py#L2471) | 2471 | `"    result = agent.answer(question)"` | — |
| [SRC-F725E90B2A-L002472](../../tests/test_web_agent.py#L2472) | 2472 | `""` | — |
| [SRC-F725E90B2A-L002473](../../tests/test_web_agent.py#L2473) | 2473 | `"    assert result[\"intent_route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-F725E90B2A-L002474](../../tests/test_web_agent.py#L2474) | 2474 | `"    assert result[\"kind\"] == \"lead_discovery_no_qualified_candidates\""` | — |
| [SRC-F725E90B2A-L002475](../../tests/test_web_agent.py#L2475) | 2475 | `"    assert result[\"search_report\"][\"lead_generation\"][\"candidate_signal_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002476](../../tests/test_web_agent.py#L2476) | 2476 | `"    assert result[\"search_report\"][\"lead_generation\"][\"related_results_reviewed\"] == 2"` | — |
| [SRC-F725E90B2A-L002477](../../tests/test_web_agent.py#L2477) | 2477 | `"    assert \"لم أعتبر إعلانات البيع\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L002478](../../tests/test_web_agent.py#L2478) | 2478 | `"    assert all(s[\"lead_qualification\"] == \"related_result_not_lead\" for s in result[\"sources\"])"` | — |
| [SRC-F725E90B2A-L002479](../../tests/test_web_agent.py#L2479) | 2479 | `""` | — |
| [SRC-F725E90B2A-L002480](../../tests/test_web_agent.py#L2480) | 2480 | `""` | — |
| [SRC-F725E90B2A-L002481](../../tests/test_web_agent.py#L2481) | 2481 | `"def test_lead_generation_search_plan_includes_high_intent_queries(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002482](../../tests/test_web_agent.py#L2482) | 2482 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002483](../../tests/test_web_agent.py#L2483) | 2483 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002484](../../tests/test_web_agent.py#L2484) | 2484 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002485](../../tests/test_web_agent.py#L2485) | 2485 | `"        \"queries\": [\"generic apartment listings\"],"` | — |
| [SRC-F725E90B2A-L002486](../../tests/test_web_agent.py#L2486) | 2486 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002487](../../tests/test_web_agent.py#L2487) | 2487 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002488](../../tests/test_web_agent.py#L2488) | 2488 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002489](../../tests/test_web_agent.py#L2489) | 2489 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002490](../../tests/test_web_agent.py#L2490) | 2490 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002491](../../tests/test_web_agent.py#L2491) | 2491 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002492](../../tests/test_web_agent.py#L2492) | 2492 | `"    }"` | — |
| [SRC-F725E90B2A-L002493](../../tests/test_web_agent.py#L2493) | 2493 | `""` | — |
| [SRC-F725E90B2A-L002494](../../tests/test_web_agent.py#L2494) | 2494 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L002495](../../tests/test_web_agent.py#L2495) | 2495 | `"        seen.update(research_plan)"` | — |
| [SRC-F725E90B2A-L002496](../../tests/test_web_agent.py#L2496) | 2496 | `"        source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002497](../../tests/test_web_agent.py#L2497) | 2497 | `"        source.update({"` | — |
| [SRC-F725E90B2A-L002498](../../tests/test_web_agent.py#L2498) | 2498 | `"            \"title\": \"مطلوب شقة تمليك في العاصمة الإدارية\","` | — |
| [SRC-F725E90B2A-L002499](../../tests/test_web_agent.py#L2499) | 2499 | `"            \"snippet\": \"صاحب المنشور يبحث عن شقة للشراء\","` | — |
| [SRC-F725E90B2A-L002500](../../tests/test_web_agent.py#L2500) | 2500 | `"            \"page_text\": \"مطلوب شقة تمليك في العاصمة الإدارية، أريد الشراء.\","` | — |
| [SRC-F725E90B2A-L002501](../../tests/test_web_agent.py#L2501) | 2501 | `"            \"queries\": list(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002502](../../tests/test_web_agent.py#L2502) | 2502 | `"        })"` | — |
| [SRC-F725E90B2A-L002503](../../tests/test_web_agent.py#L2503) | 2503 | `"        return [source], [], {"` | — |
| [SRC-F725E90B2A-L002504](../../tests/test_web_agent.py#L2504) | 2504 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002505](../../tests/test_web_agent.py#L2505) | 2505 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002506](../../tests/test_web_agent.py#L2506) | 2506 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L002507](../../tests/test_web_agent.py#L2507) | 2507 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L002508](../../tests/test_web_agent.py#L2508) | 2508 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L002509](../../tests/test_web_agent.py#L2509) | 2509 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L002510](../../tests/test_web_agent.py#L2510) | 2510 | `"            \"provider_counts\": {\"test_provider\": 1},"` | — |
| [SRC-F725E90B2A-L002511](../../tests/test_web_agent.py#L2511) | 2511 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L002512](../../tests/test_web_agent.py#L2512) | 2512 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002513](../../tests/test_web_agent.py#L2513) | 2513 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002514](../../tests/test_web_agent.py#L2514) | 2514 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002515](../../tests/test_web_agent.py#L2515) | 2515 | `"        }"` | — |
| [SRC-F725E90B2A-L002516](../../tests/test_web_agent.py#L2516) | 2516 | `""` | — |
| [SRC-F725E90B2A-L002517](../../tests/test_web_agent.py#L2517) | 2517 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda q, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002518](../../tests/test_web_agent.py#L2518) | 2518 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L002519](../../tests/test_web_agent.py#L2519) | 2519 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"عُثر على إشارة علنية محتملة [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L002520](../../tests/test_web_agent.py#L2520) | 2520 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L002521](../../tests/test_web_agent.py#L2521) | 2521 | `""` | — |
| [SRC-F725E90B2A-L002522](../../tests/test_web_agent.py#L2522) | 2522 | `"    result = agent.answer(\"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\")"` | — |
| [SRC-F725E90B2A-L002523](../../tests/test_web_agent.py#L2523) | 2523 | `""` | — |
| [SRC-F725E90B2A-L002524](../../tests/test_web_agent.py#L2524) | 2524 | `"    assert result[\"intent_route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-F725E90B2A-L002525](../../tests/test_web_agent.py#L2525) | 2525 | `"    assert seen[\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L002526](../../tests/test_web_agent.py#L2526) | 2526 | `"    assert len(seen[\"queries\"]) >= 4"` | — |
| [SRC-F725E90B2A-L002527](../../tests/test_web_agent.py#L2527) | 2527 | `"    assert any('\"مطلوب شراء\"' in q or '\"مطلوب شقه تمليك\"' in q for q in seen[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002528](../../tests/test_web_agent.py#L2528) | 2528 | `"    assert result[\"search_report\"][\"lead_generation\"][\"candidate_signal_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002529](../../tests/test_web_agent.py#L2529) | 2529 | `"    assert result[\"sources\"][0][\"lead_qualification\"] == \"public_demand_signal\""` | — |
| [SRC-F725E90B2A-L002530](../../tests/test_web_agent.py#L2530) | 2530 | `""` | — |
| [SRC-F725E90B2A-L002531](../../tests/test_web_agent.py#L2531) | 2531 | `""` | — |
| [SRC-F725E90B2A-L002532](../../tests/test_web_agent.py#L2532) | 2532 | `"def test_deepseek_search_adapter_normalizes_results_without_exposing_api_key(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002533](../../tests/test_web_agent.py#L2533) | 2533 | `""` | — |
| [SRC-F725E90B2A-L002534](../../tests/test_web_agent.py#L2534) | 2534 | `"    monkeypatch.setenv(\"DEEPSEEK_SEARCH_API_KEY\", \"test-secret-key-that-must-not-appear\")"` | — |
| [SRC-F725E90B2A-L002535](../../tests/test_web_agent.py#L2535) | 2535 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002536](../../tests/test_web_agent.py#L2536) | 2536 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002537](../../tests/test_web_agent.py#L2537) | 2537 | `""` | — |
| [SRC-F725E90B2A-L002538](../../tests/test_web_agent.py#L2538) | 2538 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L002539](../../tests/test_web_agent.py#L2539) | 2539 | `"        def raise_for_status(self):"` | — |
| [SRC-F725E90B2A-L002540](../../tests/test_web_agent.py#L2540) | 2540 | `"            return None"` | — |
| [SRC-F725E90B2A-L002541](../../tests/test_web_agent.py#L2541) | 2541 | `""` | — |
| [SRC-F725E90B2A-L002542](../../tests/test_web_agent.py#L2542) | 2542 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L002543](../../tests/test_web_agent.py#L2543) | 2543 | `"            return {"` | — |
| [SRC-F725E90B2A-L002544](../../tests/test_web_agent.py#L2544) | 2544 | `"                \"results\": [{"` | — |
| [SRC-F725E90B2A-L002545](../../tests/test_web_agent.py#L2545) | 2545 | `"                    \"title\": \"Buyer wanted\","` | — |
| [SRC-F725E90B2A-L002546](../../tests/test_web_agent.py#L2546) | 2546 | `"                    \"url\": \"https://example.com/buyer\","` | — |
| [SRC-F725E90B2A-L002547](../../tests/test_web_agent.py#L2547) | 2547 | `"                    \"snippet\": \"Looking to buy a flat.\","` | — |
| [SRC-F725E90B2A-L002548](../../tests/test_web_agent.py#L2548) | 2548 | `"                    \"summary\": \"Looking to buy a flat in the requested area.\","` | — |
| [SRC-F725E90B2A-L002549](../../tests/test_web_agent.py#L2549) | 2549 | `"                    \"date\": \"2026-10-16T12:00:00Z\","` | — |
| [SRC-F725E90B2A-L002550](../../tests/test_web_agent.py#L2550) | 2550 | `"                    \"site_name\": \"Example\","` | — |
| [SRC-F725E90B2A-L002551](../../tests/test_web_agent.py#L2551) | 2551 | `"                    \"rerank_score\": 2.2,"` | — |
| [SRC-F725E90B2A-L002552](../../tests/test_web_agent.py#L2552) | 2552 | `"                    \"authority\": 2,"` | — |
| [SRC-F725E90B2A-L002553](../../tests/test_web_agent.py#L2553) | 2553 | `"                }]"` | — |
| [SRC-F725E90B2A-L002554](../../tests/test_web_agent.py#L2554) | 2554 | `"            }"` | — |
| [SRC-F725E90B2A-L002555](../../tests/test_web_agent.py#L2555) | 2555 | `""` | — |
| [SRC-F725E90B2A-L002556](../../tests/test_web_agent.py#L2556) | 2556 | `"    def fake_post(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002557](../../tests/test_web_agent.py#L2557) | 2557 | `"        seen[\"url\"] = url"` | — |
| [SRC-F725E90B2A-L002558](../../tests/test_web_agent.py#L2558) | 2558 | `"        seen.update(kwargs)"` | — |
| [SRC-F725E90B2A-L002559](../../tests/test_web_agent.py#L2559) | 2559 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L002560](../../tests/test_web_agent.py#L2560) | 2560 | `""` | — |
| [SRC-F725E90B2A-L002561](../../tests/test_web_agent.py#L2561) | 2561 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002562](../../tests/test_web_agent.py#L2562) | 2562 | `"        \"agents.web_agent._bounded_http_request\","` | — |
| [SRC-F725E90B2A-L002563](../../tests/test_web_agent.py#L2563) | 2563 | `"        lambda method, url, **kwargs: fake_post(url, **kwargs),"` | — |
| [SRC-F725E90B2A-L002564](../../tests/test_web_agent.py#L2564) | 2564 | `"    )"` | — |
| [SRC-F725E90B2A-L002565](../../tests/test_web_agent.py#L2565) | 2565 | `"    rows = agent._search_deepseek_api(\"buyers looking to buy a flat\")"` | — |
| [SRC-F725E90B2A-L002566](../../tests/test_web_agent.py#L2566) | 2566 | `""` | — |
| [SRC-F725E90B2A-L002567](../../tests/test_web_agent.py#L2567) | 2567 | `"    assert seen[\"url\"] == \"https://api.deepseek.com/v1/tools/search\""` | — |
| [SRC-F725E90B2A-L002568](../../tests/test_web_agent.py#L2568) | 2568 | `"    assert seen[\"headers\"][\"Authorization\"] == \"Bearer test-secret-key-that-must-not-appear\""` | — |
| [SRC-F725E90B2A-L002569](../../tests/test_web_agent.py#L2569) | 2569 | `"    assert seen[\"json\"][\"count\"] == 6"` | — |
| [SRC-F725E90B2A-L002570](../../tests/test_web_agent.py#L2570) | 2570 | `"    assert rows[0][\"provider\"] == \"deepseek_search_api\""` | — |
| [SRC-F725E90B2A-L002571](../../tests/test_web_agent.py#L2571) | 2571 | `"    assert rows[0][\"snippet\"] == \"Looking to buy a flat in the requested area.\""` | — |
| [SRC-F725E90B2A-L002572](../../tests/test_web_agent.py#L2572) | 2572 | `"    assert rows[0][\"provider_rerank_score\"] == 2.2"` | — |
| [SRC-F725E90B2A-L002573](../../tests/test_web_agent.py#L2573) | 2573 | `"    assert \"test-secret-key-that-must-not-appear\" not in str(rows)"` | — |
| [SRC-F725E90B2A-L002574](../../tests/test_web_agent.py#L2574) | 2574 | `""` | — |
| [SRC-F725E90B2A-L002575](../../tests/test_web_agent.py#L2575) | 2575 | `""` | — |
| [SRC-F725E90B2A-L002576](../../tests/test_web_agent.py#L2576) | 2576 | `""` | — |
| [SRC-F725E90B2A-L002577](../../tests/test_web_agent.py#L2577) | 2577 | `"def test_diagnostics_distinguishes_connector_response_without_matches_from_offline(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002578](../../tests/test_web_agent.py#L2578) | 2578 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002579](../../tests/test_web_agent.py#L2579) | 2579 | `"    monkeypatch.setattr(agent, \"_request_completion\", lambda *args, **kwargs: \"OK\")"` | — |
| [SRC-F725E90B2A-L002580](../../tests/test_web_agent.py#L2580) | 2580 | `""` | — |
| [SRC-F725E90B2A-L002581](../../tests/test_web_agent.py#L2581) | 2581 | `"    def completed_empty_search(query):"` | — |
| [SRC-F725E90B2A-L002582](../../tests/test_web_agent.py#L2582) | 2582 | `"        agent._record_provider_diagnostic("` | — |
| [SRC-F725E90B2A-L002583](../../tests/test_web_agent.py#L2583) | 2583 | `"            \"bing_rss\", query, \"no_results\", result_count=0,"` | — |
| [SRC-F725E90B2A-L002584](../../tests/test_web_agent.py#L2584) | 2584 | `"            error=\"connector completed but returned no parseable results\","` | — |
| [SRC-F725E90B2A-L002585](../../tests/test_web_agent.py#L2585) | 2585 | `"        )"` | — |
| [SRC-F725E90B2A-L002586](../../tests/test_web_agent.py#L2586) | 2586 | `"        raise RuntimeError(\"no usable search matches\")"` | — |
| [SRC-F725E90B2A-L002587](../../tests/test_web_agent.py#L2587) | 2587 | `""` | — |
| [SRC-F725E90B2A-L002588](../../tests/test_web_agent.py#L2588) | 2588 | `"    monkeypatch.setattr(agent, \"_search_web\", completed_empty_search)"` | — |
| [SRC-F725E90B2A-L002589](../../tests/test_web_agent.py#L2589) | 2589 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L002590](../../tests/test_web_agent.py#L2590) | 2590 | `""` | — |
| [SRC-F725E90B2A-L002591](../../tests/test_web_agent.py#L2591) | 2591 | `"    assert report[\"checks\"][\"web_search\"][\"status\"] == \"degraded\""` | — |
| [SRC-F725E90B2A-L002592](../../tests/test_web_agent.py#L2592) | 2592 | `"    assert report[\"checks\"][\"web_search\"][\"result_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002593](../../tests/test_web_agent.py#L2593) | 2593 | `"    assert report[\"checks\"][\"web_search\"][\"completed_connector_responses\"] >= 1"` | — |
| [SRC-F725E90B2A-L002594](../../tests/test_web_agent.py#L2594) | 2594 | `"    assert \"completed a request\" in report[\"checks\"][\"web_search\"][\"note\"]"` | — |
| [SRC-F725E90B2A-L002595](../../tests/test_web_agent.py#L2595) | 2595 | `""` | — |
| [SRC-F725E90B2A-L002596](../../tests/test_web_agent.py#L2596) | 2596 | `""` | — |
| [SRC-F725E90B2A-L002597](../../tests/test_web_agent.py#L2597) | 2597 | `"def test_deepseek_search_request_budget_defaults_to_one_and_is_bounded(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002598](../../tests/test_web_agent.py#L2598) | 2598 | `"    monkeypatch.setenv(\"DEEPSEEK_SEARCH_API_KEY\", \"test-secret-key\")"` | — |
| [SRC-F725E90B2A-L002599](../../tests/test_web_agent.py#L2599) | 2599 | `"    monkeypatch.delenv(\"OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET\", raising=False)"` | — |
| [SRC-F725E90B2A-L002600](../../tests/test_web_agent.py#L2600) | 2600 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002601](../../tests/test_web_agent.py#L2601) | 2601 | `"    assert agent._reserve_deepseek_search_request() is True"` | — |
| [SRC-F725E90B2A-L002602](../../tests/test_web_agent.py#L2602) | 2602 | `"    assert agent._reserve_deepseek_search_request() is False"` | — |
| [SRC-F725E90B2A-L002603](../../tests/test_web_agent.py#L2603) | 2603 | `""` | — |
| [SRC-F725E90B2A-L002604](../../tests/test_web_agent.py#L2604) | 2604 | `"    monkeypatch.setenv(\"OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET\", \"2\")"` | — |
| [SRC-F725E90B2A-L002605](../../tests/test_web_agent.py#L2605) | 2605 | `"    other_agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002606](../../tests/test_web_agent.py#L2606) | 2606 | `"    assert other_agent._reserve_deepseek_search_request() is True"` | — |
| [SRC-F725E90B2A-L002607](../../tests/test_web_agent.py#L2607) | 2607 | `"    assert other_agent._reserve_deepseek_search_request() is True"` | — |
| [SRC-F725E90B2A-L002608](../../tests/test_web_agent.py#L2608) | 2608 | `"    assert other_agent._reserve_deepseek_search_request() is False"` | — |
| [SRC-F725E90B2A-L002609](../../tests/test_web_agent.py#L2609) | 2609 | `""` | — |
| [SRC-F725E90B2A-L002610](../../tests/test_web_agent.py#L2610) | 2610 | `""` | — |
| [SRC-F725E90B2A-L002611](../../tests/test_web_agent.py#L2611) | 2611 | `""` | — |
| [SRC-F725E90B2A-L002612](../../tests/test_web_agent.py#L2612) | 2612 | `"def test_diagnostics_distinguishes_completed_search_without_matches_from_connection_failure(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002613](../../tests/test_web_agent.py#L2613) | 2613 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002614](../../tests/test_web_agent.py#L2614) | 2614 | `"    # A stale record from a prior search must not make a new diagnostics call pass."` | — |
| [SRC-F725E90B2A-L002615](../../tests/test_web_agent.py#L2615) | 2615 | `"    agent._record_provider_diagnostic(\"old_provider\", \"old query\", \"ok\", 1)"` | — |
| [SRC-F725E90B2A-L002616](../../tests/test_web_agent.py#L2616) | 2616 | `""` | — |
| [SRC-F725E90B2A-L002617](../../tests/test_web_agent.py#L2617) | 2617 | `"    def no_results(query):"` | — |
| [SRC-F725E90B2A-L002618](../../tests/test_web_agent.py#L2618) | 2618 | `"        agent._record_provider_diagnostic(\"duckduckgo_html\", query, \"no_results\")"` | — |
| [SRC-F725E90B2A-L002619](../../tests/test_web_agent.py#L2619) | 2619 | `"        raise RuntimeError(\"no parseable results\")"` | — |
| [SRC-F725E90B2A-L002620](../../tests/test_web_agent.py#L2620) | 2620 | `""` | — |
| [SRC-F725E90B2A-L002621](../../tests/test_web_agent.py#L2621) | 2621 | `"    monkeypatch.setattr(agent, \"_search_web\", no_results)"` | — |
| [SRC-F725E90B2A-L002622](../../tests/test_web_agent.py#L2622) | 2622 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L002623](../../tests/test_web_agent.py#L2623) | 2623 | `""` | — |
| [SRC-F725E90B2A-L002624](../../tests/test_web_agent.py#L2624) | 2624 | `"    check = report[\"checks\"][\"web_search\"]"` | — |
| [SRC-F725E90B2A-L002625](../../tests/test_web_agent.py#L2625) | 2625 | `"    assert check[\"status\"] == \"degraded\""` | — |
| [SRC-F725E90B2A-L002626](../../tests/test_web_agent.py#L2626) | 2626 | `"    assert check[\"result_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002627](../../tests/test_web_agent.py#L2627) | 2627 | `"    assert check[\"completed_connector_responses\"] >= 1"` | — |
| [SRC-F725E90B2A-L002628](../../tests/test_web_agent.py#L2628) | 2628 | `"    assert \"completed a request\" in check[\"note\"]"` | — |
| [SRC-F725E90B2A-L002629](../../tests/test_web_agent.py#L2629) | 2629 | `"    assert \"old_provider\" not in str(check)"` | — |
| [SRC-F725E90B2A-L002630](../../tests/test_web_agent.py#L2630) | 2630 | `""` | — |
| [SRC-F725E90B2A-L002631](../../tests/test_web_agent.py#L2631) | 2631 | `""` | — |
| [SRC-F725E90B2A-L002632](../../tests/test_web_agent.py#L2632) | 2632 | `"def test_buyer_intent_phrase_inside_negated_text_is_not_a_lead_signal():"` | — |
| [SRC-F725E90B2A-L002633](../../tests/test_web_agent.py#L2633) | 2633 | `"    source = {"` | — |
| [SRC-F725E90B2A-L002634](../../tests/test_web_agent.py#L2634) | 2634 | `"        \"title\": \"Buyer discussion\","` | — |
| [SRC-F725E90B2A-L002635](../../tests/test_web_agent.py#L2635) | 2635 | `"        \"snippet\": \"I am not looking to buy an apartment this year.\","` | — |
| [SRC-F725E90B2A-L002636](../../tests/test_web_agent.py#L2636) | 2636 | `"        \"page_text\": \"I am not looking to buy an apartment this year.\","` | — |
| [SRC-F725E90B2A-L002637](../../tests/test_web_agent.py#L2637) | 2637 | `"    }"` | — |
| [SRC-F725E90B2A-L002638](../../tests/test_web_agent.py#L2638) | 2638 | `"    assert WebAgent._lead_intent_evidence(source) is None"` | — |
| [SRC-F725E90B2A-L002639](../../tests/test_web_agent.py#L2639) | 2639 | `""` | — |
| [SRC-F725E90B2A-L002640](../../tests/test_web_agent.py#L2640) | 2640 | `""` | — |
| [SRC-F725E90B2A-L002641](../../tests/test_web_agent.py#L2641) | 2641 | `""` | — |
| [SRC-F725E90B2A-L002642](../../tests/test_web_agent.py#L2642) | 2642 | `"def test_lead_generation_preserves_unknown_state_when_research_throws(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002643](../../tests/test_web_agent.py#L2643) | 2643 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002644](../../tests/test_web_agent.py#L2644) | 2644 | `"    question = \"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\""` | — |
| [SRC-F725E90B2A-L002645](../../tests/test_web_agent.py#L2645) | 2645 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002646](../../tests/test_web_agent.py#L2646) | 2646 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002647](../../tests/test_web_agent.py#L2647) | 2647 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002648](../../tests/test_web_agent.py#L2648) | 2648 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002649](../../tests/test_web_agent.py#L2649) | 2649 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002650](../../tests/test_web_agent.py#L2650) | 2650 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002651](../../tests/test_web_agent.py#L2651) | 2651 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002652](../../tests/test_web_agent.py#L2652) | 2652 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002653](../../tests/test_web_agent.py#L2653) | 2653 | `"    }"` | — |
| [SRC-F725E90B2A-L002654](../../tests/test_web_agent.py#L2654) | 2654 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda q, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002655](../../tests/test_web_agent.py#L2655) | 2655 | `""` | — |
| [SRC-F725E90B2A-L002656](../../tests/test_web_agent.py#L2656) | 2656 | `"    def fail_research(research_plan):"` | — |
| [SRC-F725E90B2A-L002657](../../tests/test_web_agent.py#L2657) | 2657 | `"        raise RuntimeError(\"mocked interrupted research\")"` | — |
| [SRC-F725E90B2A-L002658](../../tests/test_web_agent.py#L2658) | 2658 | `""` | — |
| [SRC-F725E90B2A-L002659](../../tests/test_web_agent.py#L2659) | 2659 | `"    monkeypatch.setattr(agent, \"_collect_research\", fail_research)"` | — |
| [SRC-F725E90B2A-L002660](../../tests/test_web_agent.py#L2660) | 2660 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002661](../../tests/test_web_agent.py#L2661) | 2661 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002662](../../tests/test_web_agent.py#L2662) | 2662 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L002663](../../tests/test_web_agent.py#L2663) | 2663 | `"        lambda *args, **kwargs: (_ for _ in ()).throw("` | — |
| [SRC-F725E90B2A-L002664](../../tests/test_web_agent.py#L2664) | 2664 | `"            AssertionError(\"must not generate a lead from an incomplete search\")"` | — |
| [SRC-F725E90B2A-L002665](../../tests/test_web_agent.py#L2665) | 2665 | `"        ),"` | — |
| [SRC-F725E90B2A-L002666](../../tests/test_web_agent.py#L2666) | 2666 | `"    )"` | — |
| [SRC-F725E90B2A-L002667](../../tests/test_web_agent.py#L2667) | 2667 | `""` | — |
| [SRC-F725E90B2A-L002668](../../tests/test_web_agent.py#L2668) | 2668 | `"    result = agent.answer(question)"` | — |
| [SRC-F725E90B2A-L002669](../../tests/test_web_agent.py#L2669) | 2669 | `"    lead = result[\"search_report\"][\"lead_generation\"]"` | — |
| [SRC-F725E90B2A-L002670](../../tests/test_web_agent.py#L2670) | 2670 | `""` | — |
| [SRC-F725E90B2A-L002671](../../tests/test_web_agent.py#L2671) | 2671 | `"    assert lead[\"status\"] == \"research_incomplete\""` | — |
| [SRC-F725E90B2A-L002672](../../tests/test_web_agent.py#L2672) | 2672 | `"    assert lead[\"candidate_signal_count\"] is None"` | — |
| [SRC-F725E90B2A-L002673](../../tests/test_web_agent.py#L2673) | 2673 | `"    assert lead[\"related_results_reviewed\"] is None"` | — |
| [SRC-F725E90B2A-L002674](../../tests/test_web_agent.py#L2674) | 2674 | `"    assert result[\"search_report\"][\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002675](../../tests/test_web_agent.py#L2675) | 2675 | `"    assert result[\"search_report\"][\"evidence_signals\"] is None"` | — |
| [SRC-F725E90B2A-L002676](../../tests/test_web_agent.py#L2676) | 2676 | `"    assert \"لم أستطع تحديد\" in result[\"answer\"] or \"تعطل مسار البحث\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L002677](../../tests/test_web_agent.py#L2677) | 2677 | `""` | — |
| [SRC-F725E90B2A-L002678](../../tests/test_web_agent.py#L2678) | 2678 | `""` | — |
| [SRC-F725E90B2A-L002679](../../tests/test_web_agent.py#L2679) | 2679 | `""` | — |
| [SRC-F725E90B2A-L002680](../../tests/test_web_agent.py#L2680) | 2680 | `"def test_local_answer_exposes_request_budget_without_claiming_live_search():"` | — |
| [SRC-F725E90B2A-L002681](../../tests/test_web_agent.py#L2681) | 2681 | `"    result = WebAgent().answer(\"مرحبا\")"` | — |
| [SRC-F725E90B2A-L002682](../../tests/test_web_agent.py#L2682) | 2682 | `""` | — |
| [SRC-F725E90B2A-L002683](../../tests/test_web_agent.py#L2683) | 2683 | `"    budget = result[\"request_budget\"]"` | — |
| [SRC-F725E90B2A-L002684](../../tests/test_web_agent.py#L2684) | 2684 | `"    assert budget[\"policy\"] == \"cooperative_per_request_budget\""` | — |
| [SRC-F725E90B2A-L002685](../../tests/test_web_agent.py#L2685) | 2685 | `"    assert budget[\"counts\"][\"search_queries\"] == 0"` | — |
| [SRC-F725E90B2A-L002686](../../tests/test_web_agent.py#L2686) | 2686 | `"    assert budget[\"counts\"][\"model_calls\"] == 0"` | — |
| [SRC-F725E90B2A-L002687](../../tests/test_web_agent.py#L2687) | 2687 | `"    assert budget[\"hard_cancellation_guaranteed\"] is False"` | — |
| [SRC-F725E90B2A-L002688](../../tests/test_web_agent.py#L2688) | 2688 | `""` | — |
| [SRC-F725E90B2A-L002689](../../tests/test_web_agent.py#L2689) | 2689 | `""` | — |
| [SRC-F725E90B2A-L002690](../../tests/test_web_agent.py#L2690) | 2690 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L002691](../../tests/test_web_agent.py#L2691) | 2691 | `"    \"draft_answer\","` | — |
| [SRC-F725E90B2A-L002692](../../tests/test_web_agent.py#L2692) | 2692 | `"    ["` | — |
| [SRC-F725E90B2A-L002693](../../tests/test_web_agent.py#L2693) | 2693 | `"        \"وفق المقارنة، الخيار الأول أفضل من الثاني.\","` | — |
| [SRC-F725E90B2A-L002694](../../tests/test_web_agent.py#L2694) | 2694 | `"        \"وفق المقارنة، الخيار الأول أفضل من الثاني [المصدر 99].\","` | — |
| [SRC-F725E90B2A-L002695](../../tests/test_web_agent.py#L2695) | 2695 | `"    ],"` | — |
| [SRC-F725E90B2A-L002696](../../tests/test_web_agent.py#L2696) | 2696 | `")"` | — |
| [SRC-F725E90B2A-L002697](../../tests/test_web_agent.py#L2697) | 2697 | `"def test_reviewed_answer_without_valid_citations_cannot_be_rated_good("` | — |
| [SRC-F725E90B2A-L002698](../../tests/test_web_agent.py#L2698) | 2698 | `"    monkeypatch, draft_answer"` | — |
| [SRC-F725E90B2A-L002699](../../tests/test_web_agent.py#L2699) | 2699 | `"):"` | — |
| [SRC-F725E90B2A-L002700](../../tests/test_web_agent.py#L2700) | 2700 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002701](../../tests/test_web_agent.py#L2701) | 2701 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002702](../../tests/test_web_agent.py#L2702) | 2702 | `"    domains = [\"alpha.org\", \"beta.net\", \"gamma.io\", \"delta.dev\"]"` | — |
| [SRC-F725E90B2A-L002703](../../tests/test_web_agent.py#L2703) | 2703 | `"    providers = [\"duckduckgo_html\", \"bing_rss\", \"duckduckgo_html\", \"bing_rss\"]"` | — |
| [SRC-F725E90B2A-L002704](../../tests/test_web_agent.py#L2704) | 2704 | `"    sources = []"` | — |
| [SRC-F725E90B2A-L002705](../../tests/test_web_agent.py#L2705) | 2705 | `"    for index, (domain, provider) in enumerate(zip(domains, providers, strict=True)):"` | — |
| [SRC-F725E90B2A-L002706](../../tests/test_web_agent.py#L2706) | 2706 | `"        source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002707](../../tests/test_web_agent.py#L2707) | 2707 | `"        source.update("` | — |
| [SRC-F725E90B2A-L002708](../../tests/test_web_agent.py#L2708) | 2708 | `"            {"` | — |
| [SRC-F725E90B2A-L002709](../../tests/test_web_agent.py#L2709) | 2709 | `"                \"title\": f\"مصدر اختبار {index + 1}\","` | — |
| [SRC-F725E90B2A-L002710](../../tests/test_web_agent.py#L2710) | 2710 | `"                \"url\": f\"https://{domain}/research\","` | — |
| [SRC-F725E90B2A-L002711](../../tests/test_web_agent.py#L2711) | 2711 | `"                \"domain\": domain,"` | — |
| [SRC-F725E90B2A-L002712](../../tests/test_web_agent.py#L2712) | 2712 | `"                \"providers\": [provider],"` | — |
| [SRC-F725E90B2A-L002713](../../tests/test_web_agent.py#L2713) | 2713 | `"                \"queries\": [\"قارن بالتفصيل بين طرق إدارة الميزانية\"],"` | — |
| [SRC-F725E90B2A-L002714](../../tests/test_web_agent.py#L2714) | 2714 | `"                \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L002715](../../tests/test_web_agent.py#L2715) | 2715 | `"                \"page_text\": f\"نص مصدر الاختبار رقم {index + 1}.\","` | — |
| [SRC-F725E90B2A-L002716](../../tests/test_web_agent.py#L2716) | 2716 | `"            }"` | — |
| [SRC-F725E90B2A-L002717](../../tests/test_web_agent.py#L2717) | 2717 | `"        )"` | — |
| [SRC-F725E90B2A-L002718](../../tests/test_web_agent.py#L2718) | 2718 | `"        sources.append(source)"` | — |
| [SRC-F725E90B2A-L002719](../../tests/test_web_agent.py#L2719) | 2719 | `""` | — |
| [SRC-F725E90B2A-L002720](../../tests/test_web_agent.py#L2720) | 2720 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002721](../../tests/test_web_agent.py#L2721) | 2721 | `"        \"queries\": [\"قارن بالتفصيل بين طرق إدارة الميزانية\"],"` | — |
| [SRC-F725E90B2A-L002722](../../tests/test_web_agent.py#L2722) | 2722 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002723](../../tests/test_web_agent.py#L2723) | 2723 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002724](../../tests/test_web_agent.py#L2724) | 2724 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002725](../../tests/test_web_agent.py#L2725) | 2725 | `"        \"depth\": \"deep\","` | — |
