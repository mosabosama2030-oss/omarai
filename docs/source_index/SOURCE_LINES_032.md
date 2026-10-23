# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **032**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L002008 إلى SRC-DE7EABE998-L000070
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L002008](../../tests/test_web_agent.py#L2008) | 2008 | `"    assert \"لم يمكن تحديد عدد المصادر القابلة للاستخدام\" in html"` | — |
| [SRC-F725E90B2A-L002009](../../tests/test_web_agent.py#L2009) | 2009 | `"    assert \"غير محدد\" in html"` | — |
| [SRC-F725E90B2A-L002010](../../tests/test_web_agent.py#L2010) | 2010 | `"    assert 'const score=(researchErrorOutcome\|\|lead)?null:Number(e.coverage_score\|\|0)' not in html"` | — |
| [SRC-F725E90B2A-L002011](../../tests/test_web_agent.py#L2011) | 2011 | `"    assert \"مؤشر تغطية البحث:\" not in html"` | — |
| [SRC-F725E90B2A-L002012](../../tests/test_web_agent.py#L2012) | 2012 | `"    assert '\"تغطية الأدلة: \"+scoreLabel' in html"` | — |
| [SRC-F725E90B2A-L002013](../../tests/test_web_agent.py#L2013) | 2013 | `"    assert \"يصف هذا الوصف اتساع الأدلة المتاحة ولا يمثل احتمال صحة الإجابة\" in html"` | — |
| [SRC-F725E90B2A-L002014](../../tests/test_web_agent.py#L2014) | 2014 | `"    assert \"تعذر تحديد تغطية البحث لأن مسار تجميع الأدلة لم يكتمل\" in html"` | — |
| [SRC-F725E90B2A-L002015](../../tests/test_web_agent.py#L2015) | 2015 | `""` | — |
| [SRC-F725E90B2A-L002016](../../tests/test_web_agent.py#L2016) | 2016 | `""` | — |
| [SRC-F725E90B2A-L002017](../../tests/test_web_agent.py#L2017) | 2017 | `"def test_generic_provider_failure_does_not_claim_search_attempt_as_confirmed(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002018](../../tests/test_web_agent.py#L2018) | 2018 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002019](../../tests/test_web_agent.py#L2019) | 2019 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002020](../../tests/test_web_agent.py#L2020) | 2020 | `"        \"queries\": [\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\"],"` | — |
| [SRC-F725E90B2A-L002021](../../tests/test_web_agent.py#L2021) | 2021 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002022](../../tests/test_web_agent.py#L2022) | 2022 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002023](../../tests/test_web_agent.py#L2023) | 2023 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L002024](../../tests/test_web_agent.py#L2024) | 2024 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002025](../../tests/test_web_agent.py#L2025) | 2025 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002026](../../tests/test_web_agent.py#L2026) | 2026 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002027](../../tests/test_web_agent.py#L2027) | 2027 | `"    }"` | — |
| [SRC-F725E90B2A-L002028](../../tests/test_web_agent.py#L2028) | 2028 | `""` | — |
| [SRC-F725E90B2A-L002029](../../tests/test_web_agent.py#L2029) | 2029 | `"    def fail_after_generic_provider_error(research_plan):"` | — |
| [SRC-F725E90B2A-L002030](../../tests/test_web_agent.py#L2030) | 2030 | `"        # A generic failed diagnostic does not prove whether the network request"` | — |
| [SRC-F725E90B2A-L002031](../../tests/test_web_agent.py#L2031) | 2031 | `"        # was actually sent; it must not be upgraded to a confirmed attempt."` | — |
| [SRC-F725E90B2A-L002032](../../tests/test_web_agent.py#L2032) | 2032 | `"        agent._record_provider_diagnostic("` | — |
| [SRC-F725E90B2A-L002033](../../tests/test_web_agent.py#L2033) | 2033 | `"            \"duckduckgo_html\","` | — |
| [SRC-F725E90B2A-L002034](../../tests/test_web_agent.py#L2034) | 2034 | `"            research_plan[\"queries\"][0],"` | — |
| [SRC-F725E90B2A-L002035](../../tests/test_web_agent.py#L2035) | 2035 | `"            \"failed\","` | — |
| [SRC-F725E90B2A-L002036](../../tests/test_web_agent.py#L2036) | 2036 | `"            error=\"simulated failure before request send\","` | — |
| [SRC-F725E90B2A-L002037](../../tests/test_web_agent.py#L2037) | 2037 | `"        )"` | — |
| [SRC-F725E90B2A-L002038](../../tests/test_web_agent.py#L2038) | 2038 | `"        raise RuntimeError(\"simulated research pipeline failure\")"` | — |
| [SRC-F725E90B2A-L002039](../../tests/test_web_agent.py#L2039) | 2039 | `""` | — |
| [SRC-F725E90B2A-L002040](../../tests/test_web_agent.py#L2040) | 2040 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002041](../../tests/test_web_agent.py#L2041) | 2041 | `"    monkeypatch.setattr(agent, \"_collect_research\", fail_after_generic_provider_error)"` | — |
| [SRC-F725E90B2A-L002042](../../tests/test_web_agent.py#L2042) | 2042 | `""` | — |
| [SRC-F725E90B2A-L002043](../../tests/test_web_agent.py#L2043) | 2043 | `"    result = agent.answer(\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\")"` | — |
| [SRC-F725E90B2A-L002044](../../tests/test_web_agent.py#L2044) | 2044 | `""` | — |
| [SRC-F725E90B2A-L002045](../../tests/test_web_agent.py#L2045) | 2045 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L002046](../../tests/test_web_agent.py#L2046) | 2046 | `"    assert result[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002047](../../tests/test_web_agent.py#L2047) | 2047 | `"    assert report[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002048](../../tests/test_web_agent.py#L2048) | 2048 | `"    assert report[\"search_outcome\"] == \"unknown_after_research_error\""` | — |
| [SRC-F725E90B2A-L002049](../../tests/test_web_agent.py#L2049) | 2049 | `"    assert report[\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002050](../../tests/test_web_agent.py#L2050) | 2050 | `"    assert report[\"unique_sources\"] is None"` | — |
| [SRC-F725E90B2A-L002051](../../tests/test_web_agent.py#L2051) | 2051 | `""` | — |
| [SRC-F725E90B2A-L002052](../../tests/test_web_agent.py#L2052) | 2052 | `""` | — |
| [SRC-F725E90B2A-L002053](../../tests/test_web_agent.py#L2053) | 2053 | `""` | — |
| [SRC-F725E90B2A-L002054](../../tests/test_web_agent.py#L2054) | 2054 | `"def test_diagnostics_tries_fallback_probe_when_first_probe_has_no_results(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002055](../../tests/test_web_agent.py#L2055) | 2055 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002056](../../tests/test_web_agent.py#L2056) | 2056 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L002057](../../tests/test_web_agent.py#L2057) | 2057 | `""` | — |
| [SRC-F725E90B2A-L002058](../../tests/test_web_agent.py#L2058) | 2058 | `"    def search(query):"` | — |
| [SRC-F725E90B2A-L002059](../../tests/test_web_agent.py#L2059) | 2059 | `"        calls.append(query)"` | — |
| [SRC-F725E90B2A-L002060](../../tests/test_web_agent.py#L2060) | 2060 | `"        if len(calls) == 1:"` | — |
| [SRC-F725E90B2A-L002061](../../tests/test_web_agent.py#L2061) | 2061 | `"            return []"` | — |
| [SRC-F725E90B2A-L002062](../../tests/test_web_agent.py#L2062) | 2062 | `"        return ["` | — |
| [SRC-F725E90B2A-L002063](../../tests/test_web_agent.py#L2063) | 2063 | `"            {"` | — |
| [SRC-F725E90B2A-L002064](../../tests/test_web_agent.py#L2064) | 2064 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-F725E90B2A-L002065](../../tests/test_web_agent.py#L2065) | 2065 | `"                \"title\": \"OpenAI official website\","` | — |
| [SRC-F725E90B2A-L002066](../../tests/test_web_agent.py#L2066) | 2066 | `"                \"url\": \"https://openai.com/\","` | — |
| [SRC-F725E90B2A-L002067](../../tests/test_web_agent.py#L2067) | 2067 | `"                \"snippet\": \"Official website and products\","` | — |
| [SRC-F725E90B2A-L002068](../../tests/test_web_agent.py#L2068) | 2068 | `"            }"` | — |
| [SRC-F725E90B2A-L002069](../../tests/test_web_agent.py#L2069) | 2069 | `"        ]"` | — |
| [SRC-F725E90B2A-L002070](../../tests/test_web_agent.py#L2070) | 2070 | `""` | — |
| [SRC-F725E90B2A-L002071](../../tests/test_web_agent.py#L2071) | 2071 | `"    monkeypatch.setattr(agent, \"_search_web\", search)"` | — |
| [SRC-F725E90B2A-L002072](../../tests/test_web_agent.py#L2072) | 2072 | `"    monkeypatch.setattr(agent, \"_request_completion\", lambda *args, **kwargs: \"OK\")"` | — |
| [SRC-F725E90B2A-L002073](../../tests/test_web_agent.py#L2073) | 2073 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002074](../../tests/test_web_agent.py#L2074) | 2074 | `""` | — |
| [SRC-F725E90B2A-L002075](../../tests/test_web_agent.py#L2075) | 2075 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L002076](../../tests/test_web_agent.py#L2076) | 2076 | `""` | — |
| [SRC-F725E90B2A-L002077](../../tests/test_web_agent.py#L2077) | 2077 | `"    assert len(calls) == 2"` | — |
| [SRC-F725E90B2A-L002078](../../tests/test_web_agent.py#L2078) | 2078 | `"    assert report[\"checks\"][\"web_search\"][\"status\"] == \"passed\""` | — |
| [SRC-F725E90B2A-L002079](../../tests/test_web_agent.py#L2079) | 2079 | `"    assert report[\"checks\"][\"web_search\"][\"probe_count\"] == 2"` | — |
| [SRC-F725E90B2A-L002080](../../tests/test_web_agent.py#L2080) | 2080 | `"    assert report[\"checks\"][\"web_search\"][\"result_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002081](../../tests/test_web_agent.py#L2081) | 2081 | `""` | — |
| [SRC-F725E90B2A-L002082](../../tests/test_web_agent.py#L2082) | 2082 | `""` | — |
| [SRC-F725E90B2A-L002083](../../tests/test_web_agent.py#L2083) | 2083 | `"def test_lead_discovery_is_distinct_from_listing_search():"` | — |
| [SRC-F725E90B2A-L002084](../../tests/test_web_agent.py#L2084) | 2084 | `"    assert WebAgent._is_lead_search(\"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية\")"` | — |
| [SRC-F725E90B2A-L002085](../../tests/test_web_agent.py#L2085) | 2085 | `"    assert WebAgent._is_lead_search(\"Find buyers looking to buy apartments\")"` | — |
| [SRC-F725E90B2A-L002086](../../tests/test_web_agent.py#L2086) | 2086 | `"    assert not WebAgent._is_lead_search(\"ابحث عن شقق للبيع في العاصمة الإدارية\")"` | — |
| [SRC-F725E90B2A-L002087](../../tests/test_web_agent.py#L2087) | 2087 | `"    assert not WebAgent._is_lead_search(\"Find apartments for sale\")"` | — |
| [SRC-F725E90B2A-L002088](../../tests/test_web_agent.py#L2088) | 2088 | `""` | — |
| [SRC-F725E90B2A-L002089](../../tests/test_web_agent.py#L2089) | 2089 | `""` | — |
| [SRC-F725E90B2A-L002090](../../tests/test_web_agent.py#L2090) | 2090 | `"def test_buyer_intent_evidence_requires_explicit_purchase_signal():"` | — |
| [SRC-F725E90B2A-L002091](../../tests/test_web_agent.py#L2091) | 2091 | `"    listing = {"` | — |
| [SRC-F725E90B2A-L002092](../../tests/test_web_agent.py#L2092) | 2092 | `"        \"title\": \"شقق للبيع في العاصمة الإدارية الجديدة\","` | — |
| [SRC-F725E90B2A-L002093](../../tests/test_web_agent.py#L2093) | 2093 | `"        \"snippet\": \"أفضل شقق للبيع بالتقسيط\","` | — |
| [SRC-F725E90B2A-L002094](../../tests/test_web_agent.py#L2094) | 2094 | `"        \"page_text\": \"إعلانات وحدات سكنية للبيع بمساحات مختلفة.\","` | — |
| [SRC-F725E90B2A-L002095](../../tests/test_web_agent.py#L2095) | 2095 | `"    }"` | — |
| [SRC-F725E90B2A-L002096](../../tests/test_web_agent.py#L2096) | 2096 | `"    buyer_post = {"` | — |
| [SRC-F725E90B2A-L002097](../../tests/test_web_agent.py#L2097) | 2097 | `"        \"title\": \"بدور على شقة تمليك في العاصمة الإدارية\","` | — |
| [SRC-F725E90B2A-L002098](../../tests/test_web_agent.py#L2098) | 2098 | `"        \"snippet\": \"مطلوب شقة تمليك في العاصمة الإدارية.\","` | — |
| [SRC-F725E90B2A-L002099](../../tests/test_web_agent.py#L2099) | 2099 | `"        \"page_text\": \"أنا بدور على شقة تمليك في العاصمة الإدارية وعايز أشتري خلال شهر.\","` | — |
| [SRC-F725E90B2A-L002100](../../tests/test_web_agent.py#L2100) | 2100 | `"    }"` | — |
| [SRC-F725E90B2A-L002101](../../tests/test_web_agent.py#L2101) | 2101 | `"    assert WebAgent._lead_intent_evidence(listing) is None"` | — |
| [SRC-F725E90B2A-L002102](../../tests/test_web_agent.py#L2102) | 2102 | `"    signal = WebAgent._lead_intent_evidence(buyer_post)"` | — |
| [SRC-F725E90B2A-L002103](../../tests/test_web_agent.py#L2103) | 2103 | `"    assert signal is not None"` | — |
| [SRC-F725E90B2A-L002104](../../tests/test_web_agent.py#L2104) | 2104 | `"    assert signal[\"basis\"] == \"page_text\""` | — |
| [SRC-F725E90B2A-L002105](../../tests/test_web_agent.py#L2105) | 2105 | `""` | — |
| [SRC-F725E90B2A-L002106](../../tests/test_web_agent.py#L2106) | 2106 | `""` | — |
| [SRC-F725E90B2A-L002107](../../tests/test_web_agent.py#L2107) | 2107 | `"def test_lead_generation_does_not_present_sale_listings_as_buyers(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002108](../../tests/test_web_agent.py#L2108) | 2108 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002109](../../tests/test_web_agent.py#L2109) | 2109 | `"    question = \"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\""` | — |
| [SRC-F725E90B2A-L002110](../../tests/test_web_agent.py#L2110) | 2110 | `"    source_a = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002111](../../tests/test_web_agent.py#L2111) | 2111 | `"    source_a.update({"` | — |
| [SRC-F725E90B2A-L002112](../../tests/test_web_agent.py#L2112) | 2112 | `"        \"title\": \"شقق للبيع في العاصمة الإدارية الجديدة\","` | — |
| [SRC-F725E90B2A-L002113](../../tests/test_web_agent.py#L2113) | 2113 | `"        \"snippet\": \"قارن أسعار الشقق والمساحات وخطط السداد.\","` | — |
| [SRC-F725E90B2A-L002114](../../tests/test_web_agent.py#L2114) | 2114 | `"        \"page_text\": \"إعلانات شقق للبيع من شركات تطوير عقاري.\","` | — |
| [SRC-F725E90B2A-L002115](../../tests/test_web_agent.py#L2115) | 2115 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002116](../../tests/test_web_agent.py#L2116) | 2116 | `"    })"` | — |
| [SRC-F725E90B2A-L002117](../../tests/test_web_agent.py#L2117) | 2117 | `"    source_b = sample_source(1)"` | — |
| [SRC-F725E90B2A-L002118](../../tests/test_web_agent.py#L2118) | 2118 | `"    source_b.update({"` | — |
| [SRC-F725E90B2A-L002119](../../tests/test_web_agent.py#L2119) | 2119 | `"        \"title\": \"مشروعات عقارية في العاصمة الإدارية\","` | — |
| [SRC-F725E90B2A-L002120](../../tests/test_web_agent.py#L2120) | 2120 | `"        \"snippet\": \"تعرف على الوحدات السكنية المتاحة للبيع.\","` | — |
| [SRC-F725E90B2A-L002121](../../tests/test_web_agent.py#L2121) | 2121 | `"        \"page_text\": \"معلومات عامة عن مشروعات وشقق للبيع.\","` | — |
| [SRC-F725E90B2A-L002122](../../tests/test_web_agent.py#L2122) | 2122 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002123](../../tests/test_web_agent.py#L2123) | 2123 | `"    })"` | — |
| [SRC-F725E90B2A-L002124](../../tests/test_web_agent.py#L2124) | 2124 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002125](../../tests/test_web_agent.py#L2125) | 2125 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002126](../../tests/test_web_agent.py#L2126) | 2126 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002127](../../tests/test_web_agent.py#L2127) | 2127 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002128](../../tests/test_web_agent.py#L2128) | 2128 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002129](../../tests/test_web_agent.py#L2129) | 2129 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002130](../../tests/test_web_agent.py#L2130) | 2130 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002131](../../tests/test_web_agent.py#L2131) | 2131 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002132](../../tests/test_web_agent.py#L2132) | 2132 | `"    }"` | — |
| [SRC-F725E90B2A-L002133](../../tests/test_web_agent.py#L2133) | 2133 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda q, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002134](../../tests/test_web_agent.py#L2134) | 2134 | `"    monkeypatch.setattr(agent, \"_collect_research\", lambda p: ("` | — |
| [SRC-F725E90B2A-L002135](../../tests/test_web_agent.py#L2135) | 2135 | `"        [source_a, source_b], [], {"` | — |
| [SRC-F725E90B2A-L002136](../../tests/test_web_agent.py#L2136) | 2136 | `"            \"queries_planned\": 1, \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L002137](../../tests/test_web_agent.py#L2137) | 2137 | `"            \"query_results\": [{\"query\": question, \"results\": 2}],"` | — |
| [SRC-F725E90B2A-L002138](../../tests/test_web_agent.py#L2138) | 2138 | `"            \"unique_sources\": 2, \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L002139](../../tests/test_web_agent.py#L2139) | 2139 | `"            \"providers_used\": [\"test_provider\"], \"provider_counts\": {\"test_provider\": 2},"` | — |
| [SRC-F725E90B2A-L002140](../../tests/test_web_agent.py#L2140) | 2140 | `"            \"platform_counts\": {\"web\": 2}, \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002141](../../tests/test_web_agent.py#L2141) | 2141 | `"            \"depth\": \"standard\", \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002142](../../tests/test_web_agent.py#L2142) | 2142 | `"        }"` | — |
| [SRC-F725E90B2A-L002143](../../tests/test_web_agent.py#L2143) | 2143 | `"    ))"` | — |
| [SRC-F725E90B2A-L002144](../../tests/test_web_agent.py#L2144) | 2144 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002145](../../tests/test_web_agent.py#L2145) | 2145 | `"        agent, \"_generate\","` | — |
| [SRC-F725E90B2A-L002146](../../tests/test_web_agent.py#L2146) | 2146 | `"        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError(\"must not synthesize false leads\")),"` | — |
| [SRC-F725E90B2A-L002147](../../tests/test_web_agent.py#L2147) | 2147 | `"    )"` | — |
| [SRC-F725E90B2A-L002148](../../tests/test_web_agent.py#L2148) | 2148 | `""` | — |
| [SRC-F725E90B2A-L002149](../../tests/test_web_agent.py#L2149) | 2149 | `"    result = agent.answer(question)"` | — |
| [SRC-F725E90B2A-L002150](../../tests/test_web_agent.py#L2150) | 2150 | `""` | — |
| [SRC-F725E90B2A-L002151](../../tests/test_web_agent.py#L2151) | 2151 | `"    assert result[\"intent_route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-F725E90B2A-L002152](../../tests/test_web_agent.py#L2152) | 2152 | `"    assert result[\"kind\"] == \"lead_discovery_no_qualified_candidates\""` | — |
| [SRC-F725E90B2A-L002153](../../tests/test_web_agent.py#L2153) | 2153 | `"    assert result[\"search_report\"][\"lead_generation\"][\"candidate_signal_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002154](../../tests/test_web_agent.py#L2154) | 2154 | `"    assert result[\"search_report\"][\"lead_generation\"][\"related_results_reviewed\"] == 2"` | — |
| [SRC-F725E90B2A-L002155](../../tests/test_web_agent.py#L2155) | 2155 | `"    assert \"لم أعتبر إعلانات البيع\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L002156](../../tests/test_web_agent.py#L2156) | 2156 | `"    assert all(s[\"lead_qualification\"] == \"related_result_not_lead\" for s in result[\"sources\"])"` | — |
| [SRC-F725E90B2A-L002157](../../tests/test_web_agent.py#L2157) | 2157 | `""` | — |
| [SRC-F725E90B2A-L002158](../../tests/test_web_agent.py#L2158) | 2158 | `""` | — |
| [SRC-F725E90B2A-L002159](../../tests/test_web_agent.py#L2159) | 2159 | `"def test_lead_generation_search_plan_includes_high_intent_queries(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002160](../../tests/test_web_agent.py#L2160) | 2160 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002161](../../tests/test_web_agent.py#L2161) | 2161 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002162](../../tests/test_web_agent.py#L2162) | 2162 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002163](../../tests/test_web_agent.py#L2163) | 2163 | `"        \"queries\": [\"generic apartment listings\"],"` | — |
| [SRC-F725E90B2A-L002164](../../tests/test_web_agent.py#L2164) | 2164 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002165](../../tests/test_web_agent.py#L2165) | 2165 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002166](../../tests/test_web_agent.py#L2166) | 2166 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002167](../../tests/test_web_agent.py#L2167) | 2167 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002168](../../tests/test_web_agent.py#L2168) | 2168 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002169](../../tests/test_web_agent.py#L2169) | 2169 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002170](../../tests/test_web_agent.py#L2170) | 2170 | `"    }"` | — |
| [SRC-F725E90B2A-L002171](../../tests/test_web_agent.py#L2171) | 2171 | `""` | — |
| [SRC-F725E90B2A-L002172](../../tests/test_web_agent.py#L2172) | 2172 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L002173](../../tests/test_web_agent.py#L2173) | 2173 | `"        seen.update(research_plan)"` | — |
| [SRC-F725E90B2A-L002174](../../tests/test_web_agent.py#L2174) | 2174 | `"        source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002175](../../tests/test_web_agent.py#L2175) | 2175 | `"        source.update({"` | — |
| [SRC-F725E90B2A-L002176](../../tests/test_web_agent.py#L2176) | 2176 | `"            \"title\": \"مطلوب شقة تمليك في العاصمة الإدارية\","` | — |
| [SRC-F725E90B2A-L002177](../../tests/test_web_agent.py#L2177) | 2177 | `"            \"snippet\": \"صاحب المنشور يبحث عن شقة للشراء\","` | — |
| [SRC-F725E90B2A-L002178](../../tests/test_web_agent.py#L2178) | 2178 | `"            \"page_text\": \"مطلوب شقة تمليك في العاصمة الإدارية، أريد الشراء.\","` | — |
| [SRC-F725E90B2A-L002179](../../tests/test_web_agent.py#L2179) | 2179 | `"            \"queries\": list(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002180](../../tests/test_web_agent.py#L2180) | 2180 | `"        })"` | — |
| [SRC-F725E90B2A-L002181](../../tests/test_web_agent.py#L2181) | 2181 | `"        return [source], [], {"` | — |
| [SRC-F725E90B2A-L002182](../../tests/test_web_agent.py#L2182) | 2182 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002183](../../tests/test_web_agent.py#L2183) | 2183 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002184](../../tests/test_web_agent.py#L2184) | 2184 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L002185](../../tests/test_web_agent.py#L2185) | 2185 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L002186](../../tests/test_web_agent.py#L2186) | 2186 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L002187](../../tests/test_web_agent.py#L2187) | 2187 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L002188](../../tests/test_web_agent.py#L2188) | 2188 | `"            \"provider_counts\": {\"test_provider\": 1},"` | — |
| [SRC-F725E90B2A-L002189](../../tests/test_web_agent.py#L2189) | 2189 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L002190](../../tests/test_web_agent.py#L2190) | 2190 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002191](../../tests/test_web_agent.py#L2191) | 2191 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002192](../../tests/test_web_agent.py#L2192) | 2192 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002193](../../tests/test_web_agent.py#L2193) | 2193 | `"        }"` | — |
| [SRC-F725E90B2A-L002194](../../tests/test_web_agent.py#L2194) | 2194 | `""` | — |
| [SRC-F725E90B2A-L002195](../../tests/test_web_agent.py#L2195) | 2195 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda q, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002196](../../tests/test_web_agent.py#L2196) | 2196 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L002197](../../tests/test_web_agent.py#L2197) | 2197 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"عُثر على إشارة علنية محتملة [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L002198](../../tests/test_web_agent.py#L2198) | 2198 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L002199](../../tests/test_web_agent.py#L2199) | 2199 | `""` | — |
| [SRC-F725E90B2A-L002200](../../tests/test_web_agent.py#L2200) | 2200 | `"    result = agent.answer(\"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\")"` | — |
| [SRC-F725E90B2A-L002201](../../tests/test_web_agent.py#L2201) | 2201 | `""` | — |
| [SRC-F725E90B2A-L002202](../../tests/test_web_agent.py#L2202) | 2202 | `"    assert result[\"intent_route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-F725E90B2A-L002203](../../tests/test_web_agent.py#L2203) | 2203 | `"    assert seen[\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L002204](../../tests/test_web_agent.py#L2204) | 2204 | `"    assert len(seen[\"queries\"]) >= 4"` | — |
| [SRC-F725E90B2A-L002205](../../tests/test_web_agent.py#L2205) | 2205 | `"    assert any('\"مطلوب شراء\"' in q or '\"مطلوب شقه تمليك\"' in q for q in seen[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002206](../../tests/test_web_agent.py#L2206) | 2206 | `"    assert result[\"search_report\"][\"lead_generation\"][\"candidate_signal_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002207](../../tests/test_web_agent.py#L2207) | 2207 | `"    assert result[\"sources\"][0][\"lead_qualification\"] == \"public_buyer_intent_signal\""` | — |
| [SRC-F725E90B2A-L002208](../../tests/test_web_agent.py#L2208) | 2208 | `""` | — |
| [SRC-F725E90B2A-L002209](../../tests/test_web_agent.py#L2209) | 2209 | `""` | — |
| [SRC-F725E90B2A-L002210](../../tests/test_web_agent.py#L2210) | 2210 | `"def test_deepseek_search_adapter_normalizes_results_without_exposing_api_key(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002211](../../tests/test_web_agent.py#L2211) | 2211 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002212](../../tests/test_web_agent.py#L2212) | 2212 | `""` | — |
| [SRC-F725E90B2A-L002213](../../tests/test_web_agent.py#L2213) | 2213 | `"    monkeypatch.setenv(\"DEEPSEEK_SEARCH_API_KEY\", \"test-secret-key-that-must-not-appear\")"` | — |
| [SRC-F725E90B2A-L002214](../../tests/test_web_agent.py#L2214) | 2214 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002215](../../tests/test_web_agent.py#L2215) | 2215 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002216](../../tests/test_web_agent.py#L2216) | 2216 | `""` | — |
| [SRC-F725E90B2A-L002217](../../tests/test_web_agent.py#L2217) | 2217 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L002218](../../tests/test_web_agent.py#L2218) | 2218 | `"        def raise_for_status(self):"` | — |
| [SRC-F725E90B2A-L002219](../../tests/test_web_agent.py#L2219) | 2219 | `"            return None"` | — |
| [SRC-F725E90B2A-L002220](../../tests/test_web_agent.py#L2220) | 2220 | `""` | — |
| [SRC-F725E90B2A-L002221](../../tests/test_web_agent.py#L2221) | 2221 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L002222](../../tests/test_web_agent.py#L2222) | 2222 | `"            return {"` | — |
| [SRC-F725E90B2A-L002223](../../tests/test_web_agent.py#L2223) | 2223 | `"                \"results\": [{"` | — |
| [SRC-F725E90B2A-L002224](../../tests/test_web_agent.py#L2224) | 2224 | `"                    \"title\": \"Buyer wanted\","` | — |
| [SRC-F725E90B2A-L002225](../../tests/test_web_agent.py#L2225) | 2225 | `"                    \"url\": \"https://example.com/buyer\","` | — |
| [SRC-F725E90B2A-L002226](../../tests/test_web_agent.py#L2226) | 2226 | `"                    \"snippet\": \"Looking to buy a flat.\","` | — |
| [SRC-F725E90B2A-L002227](../../tests/test_web_agent.py#L2227) | 2227 | `"                    \"summary\": \"Looking to buy a flat in the requested area.\","` | — |
| [SRC-F725E90B2A-L002228](../../tests/test_web_agent.py#L2228) | 2228 | `"                    \"date\": \"2026-10-16T12:00:00Z\","` | — |
| [SRC-F725E90B2A-L002229](../../tests/test_web_agent.py#L2229) | 2229 | `"                    \"site_name\": \"Example\","` | — |
| [SRC-F725E90B2A-L002230](../../tests/test_web_agent.py#L2230) | 2230 | `"                    \"rerank_score\": 2.2,"` | — |
| [SRC-F725E90B2A-L002231](../../tests/test_web_agent.py#L2231) | 2231 | `"                    \"authority\": 2,"` | — |
| [SRC-F725E90B2A-L002232](../../tests/test_web_agent.py#L2232) | 2232 | `"                }]"` | — |
| [SRC-F725E90B2A-L002233](../../tests/test_web_agent.py#L2233) | 2233 | `"            }"` | — |
| [SRC-F725E90B2A-L002234](../../tests/test_web_agent.py#L2234) | 2234 | `""` | — |
| [SRC-F725E90B2A-L002235](../../tests/test_web_agent.py#L2235) | 2235 | `"    def fake_post(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002236](../../tests/test_web_agent.py#L2236) | 2236 | `"        seen[\"url\"] = url"` | — |
| [SRC-F725E90B2A-L002237](../../tests/test_web_agent.py#L2237) | 2237 | `"        seen.update(kwargs)"` | — |
| [SRC-F725E90B2A-L002238](../../tests/test_web_agent.py#L2238) | 2238 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L002239](../../tests/test_web_agent.py#L2239) | 2239 | `""` | — |
| [SRC-F725E90B2A-L002240](../../tests/test_web_agent.py#L2240) | 2240 | `"    monkeypatch.setattr(httpx, \"post\", fake_post)"` | — |
| [SRC-F725E90B2A-L002241](../../tests/test_web_agent.py#L2241) | 2241 | `"    rows = agent._search_deepseek_api(\"buyers looking to buy a flat\")"` | — |
| [SRC-F725E90B2A-L002242](../../tests/test_web_agent.py#L2242) | 2242 | `""` | — |
| [SRC-F725E90B2A-L002243](../../tests/test_web_agent.py#L2243) | 2243 | `"    assert seen[\"url\"] == \"https://api.deepseek.com/v1/tools/search\""` | — |
| [SRC-F725E90B2A-L002244](../../tests/test_web_agent.py#L2244) | 2244 | `"    assert seen[\"headers\"][\"Authorization\"] == \"Bearer test-secret-key-that-must-not-appear\""` | — |
| [SRC-F725E90B2A-L002245](../../tests/test_web_agent.py#L2245) | 2245 | `"    assert seen[\"json\"][\"count\"] == 6"` | — |
| [SRC-F725E90B2A-L002246](../../tests/test_web_agent.py#L2246) | 2246 | `"    assert rows[0][\"provider\"] == \"deepseek_search_api\""` | — |
| [SRC-F725E90B2A-L002247](../../tests/test_web_agent.py#L2247) | 2247 | `"    assert rows[0][\"snippet\"] == \"Looking to buy a flat in the requested area.\""` | — |
| [SRC-F725E90B2A-L002248](../../tests/test_web_agent.py#L2248) | 2248 | `"    assert rows[0][\"provider_rerank_score\"] == 2.2"` | — |
| [SRC-F725E90B2A-L002249](../../tests/test_web_agent.py#L2249) | 2249 | `"    assert \"test-secret-key-that-must-not-appear\" not in str(rows)"` | — |
| [SRC-F725E90B2A-L002250](../../tests/test_web_agent.py#L2250) | 2250 | `""` | — |
| [SRC-F725E90B2A-L002251](../../tests/test_web_agent.py#L2251) | 2251 | `""` | — |
| [SRC-F725E90B2A-L002252](../../tests/test_web_agent.py#L2252) | 2252 | `""` | — |
| [SRC-F725E90B2A-L002253](../../tests/test_web_agent.py#L2253) | 2253 | `"def test_diagnostics_distinguishes_connector_response_without_matches_from_offline(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002254](../../tests/test_web_agent.py#L2254) | 2254 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002255](../../tests/test_web_agent.py#L2255) | 2255 | `"    monkeypatch.setattr(agent, \"_request_completion\", lambda *args, **kwargs: \"OK\")"` | — |
| [SRC-F725E90B2A-L002256](../../tests/test_web_agent.py#L2256) | 2256 | `""` | — |
| [SRC-F725E90B2A-L002257](../../tests/test_web_agent.py#L2257) | 2257 | `"    def completed_empty_search(query):"` | — |
| [SRC-F725E90B2A-L002258](../../tests/test_web_agent.py#L2258) | 2258 | `"        agent._record_provider_diagnostic("` | — |
| [SRC-F725E90B2A-L002259](../../tests/test_web_agent.py#L2259) | 2259 | `"            \"bing_rss\", query, \"no_results\", result_count=0,"` | — |
| [SRC-F725E90B2A-L002260](../../tests/test_web_agent.py#L2260) | 2260 | `"            error=\"connector completed but returned no parseable results\","` | — |
| [SRC-F725E90B2A-L002261](../../tests/test_web_agent.py#L2261) | 2261 | `"        )"` | — |
| [SRC-F725E90B2A-L002262](../../tests/test_web_agent.py#L2262) | 2262 | `"        raise RuntimeError(\"no usable search matches\")"` | — |
| [SRC-F725E90B2A-L002263](../../tests/test_web_agent.py#L2263) | 2263 | `""` | — |
| [SRC-F725E90B2A-L002264](../../tests/test_web_agent.py#L2264) | 2264 | `"    monkeypatch.setattr(agent, \"_search_web\", completed_empty_search)"` | — |
| [SRC-F725E90B2A-L002265](../../tests/test_web_agent.py#L2265) | 2265 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L002266](../../tests/test_web_agent.py#L2266) | 2266 | `""` | — |
| [SRC-F725E90B2A-L002267](../../tests/test_web_agent.py#L2267) | 2267 | `"    assert report[\"checks\"][\"web_search\"][\"status\"] == \"degraded\""` | — |
| [SRC-F725E90B2A-L002268](../../tests/test_web_agent.py#L2268) | 2268 | `"    assert report[\"checks\"][\"web_search\"][\"result_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002269](../../tests/test_web_agent.py#L2269) | 2269 | `"    assert report[\"checks\"][\"web_search\"][\"completed_connector_responses\"] >= 1"` | — |
| [SRC-F725E90B2A-L002270](../../tests/test_web_agent.py#L2270) | 2270 | `"    assert \"completed a request\" in report[\"checks\"][\"web_search\"][\"note\"]"` | — |
| [SRC-F725E90B2A-L002271](../../tests/test_web_agent.py#L2271) | 2271 | `""` | — |
| [SRC-F725E90B2A-L002272](../../tests/test_web_agent.py#L2272) | 2272 | `""` | — |
| [SRC-F725E90B2A-L002273](../../tests/test_web_agent.py#L2273) | 2273 | `"def test_deepseek_search_request_budget_defaults_to_one_and_is_bounded(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002274](../../tests/test_web_agent.py#L2274) | 2274 | `"    monkeypatch.setenv(\"DEEPSEEK_SEARCH_API_KEY\", \"test-secret-key\")"` | — |
| [SRC-F725E90B2A-L002275](../../tests/test_web_agent.py#L2275) | 2275 | `"    monkeypatch.delenv(\"OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET\", raising=False)"` | — |
| [SRC-F725E90B2A-L002276](../../tests/test_web_agent.py#L2276) | 2276 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002277](../../tests/test_web_agent.py#L2277) | 2277 | `"    assert agent._reserve_deepseek_search_request() is True"` | — |
| [SRC-F725E90B2A-L002278](../../tests/test_web_agent.py#L2278) | 2278 | `"    assert agent._reserve_deepseek_search_request() is False"` | — |
| [SRC-F725E90B2A-L002279](../../tests/test_web_agent.py#L2279) | 2279 | `""` | — |
| [SRC-F725E90B2A-L002280](../../tests/test_web_agent.py#L2280) | 2280 | `"    monkeypatch.setenv(\"OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET\", \"2\")"` | — |
| [SRC-F725E90B2A-L002281](../../tests/test_web_agent.py#L2281) | 2281 | `"    other_agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002282](../../tests/test_web_agent.py#L2282) | 2282 | `"    assert other_agent._reserve_deepseek_search_request() is True"` | — |
| [SRC-F725E90B2A-L002283](../../tests/test_web_agent.py#L2283) | 2283 | `"    assert other_agent._reserve_deepseek_search_request() is True"` | — |
| [SRC-F725E90B2A-L002284](../../tests/test_web_agent.py#L2284) | 2284 | `"    assert other_agent._reserve_deepseek_search_request() is False"` | — |
| [SRC-F725E90B2A-L002285](../../tests/test_web_agent.py#L2285) | 2285 | `""` | — |
| [SRC-F725E90B2A-L002286](../../tests/test_web_agent.py#L2286) | 2286 | `""` | — |
| [SRC-F725E90B2A-L002287](../../tests/test_web_agent.py#L2287) | 2287 | `""` | — |
| [SRC-F725E90B2A-L002288](../../tests/test_web_agent.py#L2288) | 2288 | `"def test_diagnostics_distinguishes_completed_search_without_matches_from_connection_failure(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002289](../../tests/test_web_agent.py#L2289) | 2289 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002290](../../tests/test_web_agent.py#L2290) | 2290 | `"    # A stale record from a prior search must not make a new diagnostics call pass."` | — |
| [SRC-F725E90B2A-L002291](../../tests/test_web_agent.py#L2291) | 2291 | `"    agent._record_provider_diagnostic(\"old_provider\", \"old query\", \"ok\", 1)"` | — |
| [SRC-F725E90B2A-L002292](../../tests/test_web_agent.py#L2292) | 2292 | `""` | — |
| [SRC-F725E90B2A-L002293](../../tests/test_web_agent.py#L2293) | 2293 | `"    def no_results(query):"` | — |
| [SRC-F725E90B2A-L002294](../../tests/test_web_agent.py#L2294) | 2294 | `"        agent._record_provider_diagnostic(\"duckduckgo_html\", query, \"no_results\")"` | — |
| [SRC-F725E90B2A-L002295](../../tests/test_web_agent.py#L2295) | 2295 | `"        raise RuntimeError(\"no parseable results\")"` | — |
| [SRC-F725E90B2A-L002296](../../tests/test_web_agent.py#L2296) | 2296 | `""` | — |
| [SRC-F725E90B2A-L002297](../../tests/test_web_agent.py#L2297) | 2297 | `"    monkeypatch.setattr(agent, \"_search_web\", no_results)"` | — |
| [SRC-F725E90B2A-L002298](../../tests/test_web_agent.py#L2298) | 2298 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L002299](../../tests/test_web_agent.py#L2299) | 2299 | `""` | — |
| [SRC-F725E90B2A-L002300](../../tests/test_web_agent.py#L2300) | 2300 | `"    check = report[\"checks\"][\"web_search\"]"` | — |
| [SRC-F725E90B2A-L002301](../../tests/test_web_agent.py#L2301) | 2301 | `"    assert check[\"status\"] == \"degraded\""` | — |
| [SRC-F725E90B2A-L002302](../../tests/test_web_agent.py#L2302) | 2302 | `"    assert check[\"result_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002303](../../tests/test_web_agent.py#L2303) | 2303 | `"    assert check[\"completed_connector_responses\"] >= 1"` | — |
| [SRC-F725E90B2A-L002304](../../tests/test_web_agent.py#L2304) | 2304 | `"    assert \"completed a request\" in check[\"note\"]"` | — |
| [SRC-F725E90B2A-L002305](../../tests/test_web_agent.py#L2305) | 2305 | `"    assert \"old_provider\" not in str(check)"` | — |
| [SRC-F725E90B2A-L002306](../../tests/test_web_agent.py#L2306) | 2306 | `""` | — |
| [SRC-F725E90B2A-L002307](../../tests/test_web_agent.py#L2307) | 2307 | `""` | — |
| [SRC-F725E90B2A-L002308](../../tests/test_web_agent.py#L2308) | 2308 | `"def test_buyer_intent_phrase_inside_negated_text_is_not_a_lead_signal():"` | — |
| [SRC-F725E90B2A-L002309](../../tests/test_web_agent.py#L2309) | 2309 | `"    source = {"` | — |
| [SRC-F725E90B2A-L002310](../../tests/test_web_agent.py#L2310) | 2310 | `"        \"title\": \"Buyer discussion\","` | — |
| [SRC-F725E90B2A-L002311](../../tests/test_web_agent.py#L2311) | 2311 | `"        \"snippet\": \"I am not looking to buy an apartment this year.\","` | — |
| [SRC-F725E90B2A-L002312](../../tests/test_web_agent.py#L2312) | 2312 | `"        \"page_text\": \"I am not looking to buy an apartment this year.\","` | — |
| [SRC-F725E90B2A-L002313](../../tests/test_web_agent.py#L2313) | 2313 | `"    }"` | — |
| [SRC-F725E90B2A-L002314](../../tests/test_web_agent.py#L2314) | 2314 | `"    assert WebAgent._lead_intent_evidence(source) is None"` | — |
| [SRC-F725E90B2A-L002315](../../tests/test_web_agent.py#L2315) | 2315 | `""` | — |
| [SRC-F725E90B2A-L002316](../../tests/test_web_agent.py#L2316) | 2316 | `""` | — |
| [SRC-F725E90B2A-L002317](../../tests/test_web_agent.py#L2317) | 2317 | `""` | — |
| [SRC-F725E90B2A-L002318](../../tests/test_web_agent.py#L2318) | 2318 | `"def test_lead_generation_preserves_unknown_state_when_research_throws(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002319](../../tests/test_web_agent.py#L2319) | 2319 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002320](../../tests/test_web_agent.py#L2320) | 2320 | `"    question = \"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\""` | — |
| [SRC-F725E90B2A-L002321](../../tests/test_web_agent.py#L2321) | 2321 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002322](../../tests/test_web_agent.py#L2322) | 2322 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002323](../../tests/test_web_agent.py#L2323) | 2323 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002324](../../tests/test_web_agent.py#L2324) | 2324 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002325](../../tests/test_web_agent.py#L2325) | 2325 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002326](../../tests/test_web_agent.py#L2326) | 2326 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002327](../../tests/test_web_agent.py#L2327) | 2327 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002328](../../tests/test_web_agent.py#L2328) | 2328 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002329](../../tests/test_web_agent.py#L2329) | 2329 | `"    }"` | — |
| [SRC-F725E90B2A-L002330](../../tests/test_web_agent.py#L2330) | 2330 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda q, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002331](../../tests/test_web_agent.py#L2331) | 2331 | `""` | — |
| [SRC-F725E90B2A-L002332](../../tests/test_web_agent.py#L2332) | 2332 | `"    def fail_research(research_plan):"` | — |
| [SRC-F725E90B2A-L002333](../../tests/test_web_agent.py#L2333) | 2333 | `"        raise RuntimeError(\"mocked interrupted research\")"` | — |
| [SRC-F725E90B2A-L002334](../../tests/test_web_agent.py#L2334) | 2334 | `""` | — |
| [SRC-F725E90B2A-L002335](../../tests/test_web_agent.py#L2335) | 2335 | `"    monkeypatch.setattr(agent, \"_collect_research\", fail_research)"` | — |
| [SRC-F725E90B2A-L002336](../../tests/test_web_agent.py#L2336) | 2336 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002337](../../tests/test_web_agent.py#L2337) | 2337 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002338](../../tests/test_web_agent.py#L2338) | 2338 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L002339](../../tests/test_web_agent.py#L2339) | 2339 | `"        lambda *args, **kwargs: (_ for _ in ()).throw("` | — |
| [SRC-F725E90B2A-L002340](../../tests/test_web_agent.py#L2340) | 2340 | `"            AssertionError(\"must not generate a lead from an incomplete search\")"` | — |
| [SRC-F725E90B2A-L002341](../../tests/test_web_agent.py#L2341) | 2341 | `"        ),"` | — |
| [SRC-F725E90B2A-L002342](../../tests/test_web_agent.py#L2342) | 2342 | `"    )"` | — |
| [SRC-F725E90B2A-L002343](../../tests/test_web_agent.py#L2343) | 2343 | `""` | — |
| [SRC-F725E90B2A-L002344](../../tests/test_web_agent.py#L2344) | 2344 | `"    result = agent.answer(question)"` | — |
| [SRC-F725E90B2A-L002345](../../tests/test_web_agent.py#L2345) | 2345 | `"    lead = result[\"search_report\"][\"lead_generation\"]"` | — |
| [SRC-F725E90B2A-L002346](../../tests/test_web_agent.py#L2346) | 2346 | `""` | — |
| [SRC-F725E90B2A-L002347](../../tests/test_web_agent.py#L2347) | 2347 | `"    assert lead[\"status\"] == \"research_incomplete\""` | — |
| [SRC-F725E90B2A-L002348](../../tests/test_web_agent.py#L2348) | 2348 | `"    assert lead[\"candidate_signal_count\"] is None"` | — |
| [SRC-F725E90B2A-L002349](../../tests/test_web_agent.py#L2349) | 2349 | `"    assert lead[\"related_results_reviewed\"] is None"` | — |
| [SRC-F725E90B2A-L002350](../../tests/test_web_agent.py#L2350) | 2350 | `"    assert result[\"search_report\"][\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002351](../../tests/test_web_agent.py#L2351) | 2351 | `"    assert result[\"search_report\"][\"evidence_signals\"] is None"` | — |
| [SRC-F725E90B2A-L002352](../../tests/test_web_agent.py#L2352) | 2352 | `"    assert \"لم أستطع تحديد\" in result[\"answer\"] or \"تعطل مسار البحث\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L002353](../../tests/test_web_agent.py#L2353) | 2353 | `""` | — |
| [SRC-F725E90B2A-L002354](../../tests/test_web_agent.py#L2354) | 2354 | `""` | — |
| [SRC-F725E90B2A-L002355](../../tests/test_web_agent.py#L2355) | 2355 | `""` | — |
| [SRC-F725E90B2A-L002356](../../tests/test_web_agent.py#L2356) | 2356 | `"def test_local_answer_exposes_request_budget_without_claiming_live_search():"` | — |
| [SRC-F725E90B2A-L002357](../../tests/test_web_agent.py#L2357) | 2357 | `"    result = WebAgent().answer(\"مرحبا\")"` | — |
| [SRC-F725E90B2A-L002358](../../tests/test_web_agent.py#L2358) | 2358 | `""` | — |
| [SRC-F725E90B2A-L002359](../../tests/test_web_agent.py#L2359) | 2359 | `"    budget = result[\"request_budget\"]"` | — |
| [SRC-F725E90B2A-L002360](../../tests/test_web_agent.py#L2360) | 2360 | `"    assert budget[\"policy\"] == \"cooperative_per_request_budget\""` | — |
| [SRC-F725E90B2A-L002361](../../tests/test_web_agent.py#L2361) | 2361 | `"    assert budget[\"counts\"][\"search_queries\"] == 0"` | — |
| [SRC-F725E90B2A-L002362](../../tests/test_web_agent.py#L2362) | 2362 | `"    assert budget[\"counts\"][\"model_calls\"] == 0"` | — |
| [SRC-F725E90B2A-L002363](../../tests/test_web_agent.py#L2363) | 2363 | `"    assert budget[\"hard_cancellation_guaranteed\"] is False"` | — |
| [SRC-F725E90B2A-L002364](../../tests/test_web_agent.py#L2364) | 2364 | `""` | — |
| [SRC-F725E90B2A-L002365](../../tests/test_web_agent.py#L2365) | 2365 | `""` | — |
| [SRC-F725E90B2A-L002366](../../tests/test_web_agent.py#L2366) | 2366 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L002367](../../tests/test_web_agent.py#L2367) | 2367 | `"    \"draft_answer\","` | — |
| [SRC-F725E90B2A-L002368](../../tests/test_web_agent.py#L2368) | 2368 | `"    ["` | — |
| [SRC-F725E90B2A-L002369](../../tests/test_web_agent.py#L2369) | 2369 | `"        \"وفق المقارنة، الخيار الأول أفضل من الثاني.\","` | — |
| [SRC-F725E90B2A-L002370](../../tests/test_web_agent.py#L2370) | 2370 | `"        \"وفق المقارنة، الخيار الأول أفضل من الثاني [المصدر 99].\","` | — |
| [SRC-F725E90B2A-L002371](../../tests/test_web_agent.py#L2371) | 2371 | `"    ],"` | — |
| [SRC-F725E90B2A-L002372](../../tests/test_web_agent.py#L2372) | 2372 | `")"` | — |
| [SRC-F725E90B2A-L002373](../../tests/test_web_agent.py#L2373) | 2373 | `"def test_reviewed_answer_without_valid_citations_cannot_be_rated_good("` | — |
| [SRC-F725E90B2A-L002374](../../tests/test_web_agent.py#L2374) | 2374 | `"    monkeypatch, draft_answer"` | — |
| [SRC-F725E90B2A-L002375](../../tests/test_web_agent.py#L2375) | 2375 | `"):"` | — |
| [SRC-F725E90B2A-L002376](../../tests/test_web_agent.py#L2376) | 2376 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002377](../../tests/test_web_agent.py#L2377) | 2377 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002378](../../tests/test_web_agent.py#L2378) | 2378 | `"    domains = [\"alpha.org\", \"beta.net\", \"gamma.io\", \"delta.dev\"]"` | — |
| [SRC-F725E90B2A-L002379](../../tests/test_web_agent.py#L2379) | 2379 | `"    providers = [\"duckduckgo_html\", \"bing_rss\", \"duckduckgo_html\", \"bing_rss\"]"` | — |
| [SRC-F725E90B2A-L002380](../../tests/test_web_agent.py#L2380) | 2380 | `"    sources = []"` | — |
| [SRC-F725E90B2A-L002381](../../tests/test_web_agent.py#L2381) | 2381 | `"    for index, (domain, provider) in enumerate(zip(domains, providers, strict=True)):"` | — |
| [SRC-F725E90B2A-L002382](../../tests/test_web_agent.py#L2382) | 2382 | `"        source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002383](../../tests/test_web_agent.py#L2383) | 2383 | `"        source.update("` | — |
| [SRC-F725E90B2A-L002384](../../tests/test_web_agent.py#L2384) | 2384 | `"            {"` | — |
| [SRC-F725E90B2A-L002385](../../tests/test_web_agent.py#L2385) | 2385 | `"                \"title\": f\"مصدر اختبار {index + 1}\","` | — |
| [SRC-F725E90B2A-L002386](../../tests/test_web_agent.py#L2386) | 2386 | `"                \"url\": f\"https://{domain}/research\","` | — |
| [SRC-F725E90B2A-L002387](../../tests/test_web_agent.py#L2387) | 2387 | `"                \"domain\": domain,"` | — |
| [SRC-F725E90B2A-L002388](../../tests/test_web_agent.py#L2388) | 2388 | `"                \"providers\": [provider],"` | — |
| [SRC-F725E90B2A-L002389](../../tests/test_web_agent.py#L2389) | 2389 | `"                \"queries\": [\"قارن بالتفصيل بين طرق إدارة الميزانية\"],"` | — |
| [SRC-F725E90B2A-L002390](../../tests/test_web_agent.py#L2390) | 2390 | `"                \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L002391](../../tests/test_web_agent.py#L2391) | 2391 | `"                \"page_text\": f\"نص مصدر الاختبار رقم {index + 1}.\","` | — |
| [SRC-F725E90B2A-L002392](../../tests/test_web_agent.py#L2392) | 2392 | `"            }"` | — |
| [SRC-F725E90B2A-L002393](../../tests/test_web_agent.py#L2393) | 2393 | `"        )"` | — |
| [SRC-F725E90B2A-L002394](../../tests/test_web_agent.py#L2394) | 2394 | `"        sources.append(source)"` | — |
| [SRC-F725E90B2A-L002395](../../tests/test_web_agent.py#L2395) | 2395 | `""` | — |
| [SRC-F725E90B2A-L002396](../../tests/test_web_agent.py#L2396) | 2396 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002397](../../tests/test_web_agent.py#L2397) | 2397 | `"        \"queries\": [\"قارن بالتفصيل بين طرق إدارة الميزانية\"],"` | — |
| [SRC-F725E90B2A-L002398](../../tests/test_web_agent.py#L2398) | 2398 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002399](../../tests/test_web_agent.py#L2399) | 2399 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002400](../../tests/test_web_agent.py#L2400) | 2400 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002401](../../tests/test_web_agent.py#L2401) | 2401 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002402](../../tests/test_web_agent.py#L2402) | 2402 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002403](../../tests/test_web_agent.py#L2403) | 2403 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002404](../../tests/test_web_agent.py#L2404) | 2404 | `"    }"` | — |
| [SRC-F725E90B2A-L002405](../../tests/test_web_agent.py#L2405) | 2405 | `"    report = {"` | — |
| [SRC-F725E90B2A-L002406](../../tests/test_web_agent.py#L2406) | 2406 | `"        \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L002407](../../tests/test_web_agent.py#L2407) | 2407 | `"        \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L002408](../../tests/test_web_agent.py#L2408) | 2408 | `"        \"query_results\": [{\"query\": plan[\"queries\"][0], \"results\": 4}],"` | — |
| [SRC-F725E90B2A-L002409](../../tests/test_web_agent.py#L2409) | 2409 | `"        \"unique_sources\": 4,"` | — |
| [SRC-F725E90B2A-L002410](../../tests/test_web_agent.py#L2410) | 2410 | `"        \"pages_fetched\": 4,"` | — |
| [SRC-F725E90B2A-L002411](../../tests/test_web_agent.py#L2411) | 2411 | `"        \"providers_used\": providers,"` | — |
| [SRC-F725E90B2A-L002412](../../tests/test_web_agent.py#L2412) | 2412 | `"        \"provider_counts\": {\"duckduckgo_html\": 2, \"bing_rss\": 2},"` | — |
| [SRC-F725E90B2A-L002413](../../tests/test_web_agent.py#L2413) | 2413 | `"        \"platform_counts\": {\"web\": 4},"` | — |
| [SRC-F725E90B2A-L002414](../../tests/test_web_agent.py#L2414) | 2414 | `"        \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002415](../../tests/test_web_agent.py#L2415) | 2415 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002416](../../tests/test_web_agent.py#L2416) | 2416 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002417](../../tests/test_web_agent.py#L2417) | 2417 | `"        \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L002418](../../tests/test_web_agent.py#L2418) | 2418 | `"    }"` | — |
| [SRC-F725E90B2A-L002419](../../tests/test_web_agent.py#L2419) | 2419 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002420](../../tests/test_web_agent.py#L2420) | 2420 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002421](../../tests/test_web_agent.py#L2421) | 2421 | `"        agent, \"_collect_research\", lambda research_plan: (sources, [], dict(report))"` | — |
| [SRC-F725E90B2A-L002422](../../tests/test_web_agent.py#L2422) | 2422 | `"    )"` | — |
| [SRC-F725E90B2A-L002423](../../tests/test_web_agent.py#L2423) | 2423 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L002424](../../tests/test_web_agent.py#L2424) | 2424 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: draft_answer)"` | — |
| [SRC-F725E90B2A-L002425](../../tests/test_web_agent.py#L2425) | 2425 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002426](../../tests/test_web_agent.py#L2426) | 2426 | `"        agent, \"_review_answer\", lambda question, answer, review_sources: answer"` | — |
| [SRC-F725E90B2A-L002427](../../tests/test_web_agent.py#L2427) | 2427 | `"    )"` | — |
| [SRC-F725E90B2A-L002428](../../tests/test_web_agent.py#L2428) | 2428 | `""` | — |
| [SRC-F725E90B2A-L002429](../../tests/test_web_agent.py#L2429) | 2429 | `"    result = agent.answer(plan[\"queries\"][0], mode=\"deep\")"` | — |
| [SRC-F725E90B2A-L002430](../../tests/test_web_agent.py#L2430) | 2430 | `""` | — |
| [SRC-F725E90B2A-L002431](../../tests/test_web_agent.py#L2431) | 2431 | `"    assert result[\"used_language_model\"] is True"` | — |
| [SRC-F725E90B2A-L002432](../../tests/test_web_agent.py#L2432) | 2432 | `"    assert result[\"search_report\"][\"second_pass_review\"] == \"model_claim_audit_completed\""` | — |
| [SRC-F725E90B2A-L002433](../../tests/test_web_agent.py#L2433) | 2433 | `"    assert result[\"citation_validation\"][\"valid_citation_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002434](../../tests/test_web_agent.py#L2434) | 2434 | `"    assert result[\"research_quality\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L002435](../../tests/test_web_agent.py#L2435) | 2435 | `"    assert result[\"search_report\"][\"research_quality\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L002436](../../tests/test_web_agent.py#L2436) | 2436 | `"    assert result[\"answer_evidence_status\"] == \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-F725E90B2A-L002437](../../tests/test_web_agent.py#L2437) | 2437 | `"    assert result[\"citation_validation\"][\"claim_support\"] == ("` | — |
| [SRC-F725E90B2A-L002438](../../tests/test_web_agent.py#L2438) | 2438 | `"        \"not_established_no_valid_source_citations\""` | — |
| [SRC-F725E90B2A-L002439](../../tests/test_web_agent.py#L2439) | 2439 | `"    )"` | — |
| [SRC-F725E90B2A-L002440](../../tests/test_web_agent.py#L2440) | 2440 | `"    assert any(\"لا تحتوي على إحالات صالحة\" in warning for warning in result[\"warnings\"])"` | — |
| [SRC-F725E90B2A-L002441](../../tests/test_web_agent.py#L2441) | 2441 | `""` | — |
| [SRC-F725E90B2A-L002442](../../tests/test_web_agent.py#L2442) | 2442 | `"# Network-boundary regression tests. These use mocked transports and never make"` | — |
| [SRC-F725E90B2A-L002443](../../tests/test_web_agent.py#L2443) | 2443 | `"# an outbound connection; they protect against SSRF and redirect/DNS-rebinding regressions."` | — |
| [SRC-F725E90B2A-L002444](../../tests/test_web_agent.py#L2444) | 2444 | `"def test_public_ip_literals_rejects_mixed_public_and_private_dns_answers(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002445](../../tests/test_web_agent.py#L2445) | 2445 | `"    import socket"` | — |
| [SRC-F725E90B2A-L002446](../../tests/test_web_agent.py#L2446) | 2446 | `""` | — |
| [SRC-F725E90B2A-L002447](../../tests/test_web_agent.py#L2447) | 2447 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L002448](../../tests/test_web_agent.py#L2448) | 2448 | `""` | — |
| [SRC-F725E90B2A-L002449](../../tests/test_web_agent.py#L2449) | 2449 | `"    answers = ["` | — |
| [SRC-F725E90B2A-L002450](../../tests/test_web_agent.py#L2450) | 2450 | `"        (socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, \"\", (\"93.184.216.34\", 80)),"` | — |
| [SRC-F725E90B2A-L002451](../../tests/test_web_agent.py#L2451) | 2451 | `"        (socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, \"\", (\"10.10.0.8\", 80)),"` | — |
| [SRC-F725E90B2A-L002452](../../tests/test_web_agent.py#L2452) | 2452 | `"    ]"` | — |
| [SRC-F725E90B2A-L002453](../../tests/test_web_agent.py#L2453) | 2453 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002454](../../tests/test_web_agent.py#L2454) | 2454 | `"        web_agent.socket,"` | — |
| [SRC-F725E90B2A-L002455](../../tests/test_web_agent.py#L2455) | 2455 | `"        \"getaddrinfo\","` | — |
| [SRC-F725E90B2A-L002456](../../tests/test_web_agent.py#L2456) | 2456 | `"        lambda host, port, type: answers,"` | — |
| [SRC-F725E90B2A-L002457](../../tests/test_web_agent.py#L2457) | 2457 | `"    )"` | — |
| [SRC-F725E90B2A-L002458](../../tests/test_web_agent.py#L2458) | 2458 | `""` | — |
| [SRC-F725E90B2A-L002459](../../tests/test_web_agent.py#L2459) | 2459 | `"    # One private DNS answer must fail closed, even when another answer is public."` | — |
| [SRC-F725E90B2A-L002460](../../tests/test_web_agent.py#L2460) | 2460 | `"    assert web_agent._public_ip_literals(\"mixed.example\") is None"` | — |
| [SRC-F725E90B2A-L002461](../../tests/test_web_agent.py#L2461) | 2461 | `""` | — |
| [SRC-F725E90B2A-L002462](../../tests/test_web_agent.py#L2462) | 2462 | `""` | — |
| [SRC-F725E90B2A-L002463](../../tests/test_web_agent.py#L2463) | 2463 | `"def test_pinned_connect_url_uses_checked_ip_without_losing_logical_path():"` | — |
| [SRC-F725E90B2A-L002464](../../tests/test_web_agent.py#L2464) | 2464 | `"    from agents.web_agent import _pinned_connect_url"` | — |
| [SRC-F725E90B2A-L002465](../../tests/test_web_agent.py#L2465) | 2465 | `""` | — |
| [SRC-F725E90B2A-L002466](../../tests/test_web_agent.py#L2466) | 2466 | `"    assert _pinned_connect_url("` | — |
| [SRC-F725E90B2A-L002467](../../tests/test_web_agent.py#L2467) | 2467 | `"        \"https://example.test:443/path?q=1\","` | — |
| [SRC-F725E90B2A-L002468](../../tests/test_web_agent.py#L2468) | 2468 | `"        \"93.184.216.34\","` | — |
| [SRC-F725E90B2A-L002469](../../tests/test_web_agent.py#L2469) | 2469 | `"    ) == \"https://93.184.216.34:443/path?q=1\""` | — |
| [SRC-F725E90B2A-L002470](../../tests/test_web_agent.py#L2470) | 2470 | `""` | — |
| [SRC-F725E90B2A-L002471](../../tests/test_web_agent.py#L2471) | 2471 | `""` | — |
| [SRC-F725E90B2A-L002472](../../tests/test_web_agent.py#L2472) | 2472 | `"def test_fetch_page_rejects_private_redirect_before_connecting(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002473](../../tests/test_web_agent.py#L2473) | 2473 | `"    from contextlib import contextmanager"` | — |
| [SRC-F725E90B2A-L002474](../../tests/test_web_agent.py#L2474) | 2474 | `""` | — |
| [SRC-F725E90B2A-L002475](../../tests/test_web_agent.py#L2475) | 2475 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002476](../../tests/test_web_agent.py#L2476) | 2476 | `""` | — |
| [SRC-F725E90B2A-L002477](../../tests/test_web_agent.py#L2477) | 2477 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L002478](../../tests/test_web_agent.py#L2478) | 2478 | `""` | — |
| [SRC-F725E90B2A-L002479](../../tests/test_web_agent.py#L2479) | 2479 | `"    resolved_hosts = []"` | — |
| [SRC-F725E90B2A-L002480](../../tests/test_web_agent.py#L2480) | 2480 | `"    requests = []"` | — |
| [SRC-F725E90B2A-L002481](../../tests/test_web_agent.py#L2481) | 2481 | `""` | — |
| [SRC-F725E90B2A-L002482](../../tests/test_web_agent.py#L2482) | 2482 | `"    def resolve_public_ip(host):"` | — |
| [SRC-F725E90B2A-L002483](../../tests/test_web_agent.py#L2483) | 2483 | `"        resolved_hosts.append(host)"` | — |
| [SRC-F725E90B2A-L002484](../../tests/test_web_agent.py#L2484) | 2484 | `"        return [\"93.184.216.34\"] if host == \"first.example\" else None"` | — |
| [SRC-F725E90B2A-L002485](../../tests/test_web_agent.py#L2485) | 2485 | `""` | — |
| [SRC-F725E90B2A-L002486](../../tests/test_web_agent.py#L2486) | 2486 | `"    monkeypatch.setattr(web_agent, \"_public_ip_literals\", resolve_public_ip)"` | — |
| [SRC-F725E90B2A-L002487](../../tests/test_web_agent.py#L2487) | 2487 | `""` | — |
| [SRC-F725E90B2A-L002488](../../tests/test_web_agent.py#L2488) | 2488 | `"    class RedirectResponse:"` | — |
| [SRC-F725E90B2A-L002489](../../tests/test_web_agent.py#L2489) | 2489 | `"        status_code = 302"` | — |
| [SRC-F725E90B2A-L002490](../../tests/test_web_agent.py#L2490) | 2490 | `""` | — |
| [SRC-F725E90B2A-L002491](../../tests/test_web_agent.py#L2491) | 2491 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L002492](../../tests/test_web_agent.py#L2492) | 2492 | `"            self.headers = {\"location\": \"http://127.0.0.1/admin\"}"` | — |
| [SRC-F725E90B2A-L002493](../../tests/test_web_agent.py#L2493) | 2493 | `""` | — |
| [SRC-F725E90B2A-L002494](../../tests/test_web_agent.py#L2494) | 2494 | `"    @contextmanager"` | — |
| [SRC-F725E90B2A-L002495](../../tests/test_web_agent.py#L2495) | 2495 | `"    def fake_stream(self, method, url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002496](../../tests/test_web_agent.py#L2496) | 2496 | `"        requests.append((method, str(url), kwargs))"` | — |
| [SRC-F725E90B2A-L002497](../../tests/test_web_agent.py#L2497) | 2497 | `"        yield RedirectResponse()"` | — |
| [SRC-F725E90B2A-L002498](../../tests/test_web_agent.py#L2498) | 2498 | `""` | — |
| [SRC-F725E90B2A-L002499](../../tests/test_web_agent.py#L2499) | 2499 | `"    class FakeClient:"` | — |
| [SRC-F725E90B2A-L002500](../../tests/test_web_agent.py#L2500) | 2500 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-F725E90B2A-L002501](../../tests/test_web_agent.py#L2501) | 2501 | `"            self.options = kwargs"` | — |
| [SRC-F725E90B2A-L002502](../../tests/test_web_agent.py#L2502) | 2502 | `""` | — |
| [SRC-F725E90B2A-L002503](../../tests/test_web_agent.py#L2503) | 2503 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L002504](../../tests/test_web_agent.py#L2504) | 2504 | `"            return self"` | — |
| [SRC-F725E90B2A-L002505](../../tests/test_web_agent.py#L2505) | 2505 | `""` | — |
| [SRC-F725E90B2A-L002506](../../tests/test_web_agent.py#L2506) | 2506 | `"        def __exit__(self, *_args):"` | — |
| [SRC-F725E90B2A-L002507](../../tests/test_web_agent.py#L2507) | 2507 | `"            return False"` | — |
| [SRC-F725E90B2A-L002508](../../tests/test_web_agent.py#L2508) | 2508 | `""` | — |
| [SRC-F725E90B2A-L002509](../../tests/test_web_agent.py#L2509) | 2509 | `"        stream = fake_stream"` | — |
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
