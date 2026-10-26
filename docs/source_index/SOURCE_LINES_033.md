# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **033**
- سجلات الأسطر: **800**
- النطاق: SRC-F725E90B2A-L002023 إلى SRC-F725E90B2A-L002822
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L002023](../../tests/test_web_agent.py#L2023) | 2023 | `"    assert \"غير محدد\" in html"` | — |
| [SRC-F725E90B2A-L002024](../../tests/test_web_agent.py#L2024) | 2024 | `"    assert 'const score=(researchErrorOutcome\|\|lead)?null:Number(e.coverage_score\|\|0)' not in html"` | — |
| [SRC-F725E90B2A-L002025](../../tests/test_web_agent.py#L2025) | 2025 | `"    assert \"مؤشر تغطية البحث:\" not in html"` | — |
| [SRC-F725E90B2A-L002026](../../tests/test_web_agent.py#L2026) | 2026 | `"    assert '\"تغطية الأدلة: \"+scoreLabel' in html"` | — |
| [SRC-F725E90B2A-L002027](../../tests/test_web_agent.py#L2027) | 2027 | `"    assert \"يصف هذا الوصف اتساع الأدلة المتاحة ولا يمثل احتمال صحة الإجابة\" in html"` | — |
| [SRC-F725E90B2A-L002028](../../tests/test_web_agent.py#L2028) | 2028 | `"    assert \"تعذر تحديد تغطية البحث لأن مسار تجميع الأدلة لم يكتمل\" in html"` | — |
| [SRC-F725E90B2A-L002029](../../tests/test_web_agent.py#L2029) | 2029 | `""` | — |
| [SRC-F725E90B2A-L002030](../../tests/test_web_agent.py#L2030) | 2030 | `""` | — |
| [SRC-F725E90B2A-L002031](../../tests/test_web_agent.py#L2031) | 2031 | `"def test_generic_provider_failure_does_not_claim_search_attempt_as_confirmed(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002032](../../tests/test_web_agent.py#L2032) | 2032 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002033](../../tests/test_web_agent.py#L2033) | 2033 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002034](../../tests/test_web_agent.py#L2034) | 2034 | `"        \"queries\": [\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\"],"` | — |
| [SRC-F725E90B2A-L002035](../../tests/test_web_agent.py#L2035) | 2035 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002036](../../tests/test_web_agent.py#L2036) | 2036 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002037](../../tests/test_web_agent.py#L2037) | 2037 | `"        \"freshness\": \"current\","` | — |
| [SRC-F725E90B2A-L002038](../../tests/test_web_agent.py#L2038) | 2038 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002039](../../tests/test_web_agent.py#L2039) | 2039 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002040](../../tests/test_web_agent.py#L2040) | 2040 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002041](../../tests/test_web_agent.py#L2041) | 2041 | `"    }"` | — |
| [SRC-F725E90B2A-L002042](../../tests/test_web_agent.py#L2042) | 2042 | `""` | — |
| [SRC-F725E90B2A-L002043](../../tests/test_web_agent.py#L2043) | 2043 | `"    def fail_after_generic_provider_error(research_plan):"` | — |
| [SRC-F725E90B2A-L002044](../../tests/test_web_agent.py#L2044) | 2044 | `"        # A generic failed diagnostic does not prove whether the network request"` | — |
| [SRC-F725E90B2A-L002045](../../tests/test_web_agent.py#L2045) | 2045 | `"        # was actually sent; it must not be upgraded to a confirmed attempt."` | — |
| [SRC-F725E90B2A-L002046](../../tests/test_web_agent.py#L2046) | 2046 | `"        agent._record_provider_diagnostic("` | — |
| [SRC-F725E90B2A-L002047](../../tests/test_web_agent.py#L2047) | 2047 | `"            \"duckduckgo_html\","` | — |
| [SRC-F725E90B2A-L002048](../../tests/test_web_agent.py#L2048) | 2048 | `"            research_plan[\"queries\"][0],"` | — |
| [SRC-F725E90B2A-L002049](../../tests/test_web_agent.py#L2049) | 2049 | `"            \"failed\","` | — |
| [SRC-F725E90B2A-L002050](../../tests/test_web_agent.py#L2050) | 2050 | `"            error=\"simulated failure before request send\","` | — |
| [SRC-F725E90B2A-L002051](../../tests/test_web_agent.py#L2051) | 2051 | `"        )"` | — |
| [SRC-F725E90B2A-L002052](../../tests/test_web_agent.py#L2052) | 2052 | `"        raise RuntimeError(\"simulated research pipeline failure\")"` | — |
| [SRC-F725E90B2A-L002053](../../tests/test_web_agent.py#L2053) | 2053 | `""` | — |
| [SRC-F725E90B2A-L002054](../../tests/test_web_agent.py#L2054) | 2054 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002055](../../tests/test_web_agent.py#L2055) | 2055 | `"    monkeypatch.setattr(agent, \"_collect_research\", fail_after_generic_provider_error)"` | — |
| [SRC-F725E90B2A-L002056](../../tests/test_web_agent.py#L2056) | 2056 | `""` | — |
| [SRC-F725E90B2A-L002057](../../tests/test_web_agent.py#L2057) | 2057 | `"    result = agent.answer(\"ابحث عن أحدث أخبار الطاقة المتجددة اليوم\")"` | — |
| [SRC-F725E90B2A-L002058](../../tests/test_web_agent.py#L2058) | 2058 | `""` | — |
| [SRC-F725E90B2A-L002059](../../tests/test_web_agent.py#L2059) | 2059 | `"    report = result[\"search_report\"]"` | — |
| [SRC-F725E90B2A-L002060](../../tests/test_web_agent.py#L2060) | 2060 | `"    assert result[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002061](../../tests/test_web_agent.py#L2061) | 2061 | `"    assert report[\"search_attempted\"] is None"` | — |
| [SRC-F725E90B2A-L002062](../../tests/test_web_agent.py#L2062) | 2062 | `"    assert report[\"search_outcome\"] == \"unknown_after_research_error\""` | — |
| [SRC-F725E90B2A-L002063](../../tests/test_web_agent.py#L2063) | 2063 | `"    assert report[\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002064](../../tests/test_web_agent.py#L2064) | 2064 | `"    assert report[\"unique_sources\"] is None"` | — |
| [SRC-F725E90B2A-L002065](../../tests/test_web_agent.py#L2065) | 2065 | `""` | — |
| [SRC-F725E90B2A-L002066](../../tests/test_web_agent.py#L2066) | 2066 | `""` | — |
| [SRC-F725E90B2A-L002067](../../tests/test_web_agent.py#L2067) | 2067 | `""` | — |
| [SRC-F725E90B2A-L002068](../../tests/test_web_agent.py#L2068) | 2068 | `"def test_diagnostics_tries_fallback_probe_when_first_probe_has_no_results(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002069](../../tests/test_web_agent.py#L2069) | 2069 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002070](../../tests/test_web_agent.py#L2070) | 2070 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L002071](../../tests/test_web_agent.py#L2071) | 2071 | `""` | — |
| [SRC-F725E90B2A-L002072](../../tests/test_web_agent.py#L2072) | 2072 | `"    def search(query):"` | — |
| [SRC-F725E90B2A-L002073](../../tests/test_web_agent.py#L2073) | 2073 | `"        calls.append(query)"` | — |
| [SRC-F725E90B2A-L002074](../../tests/test_web_agent.py#L2074) | 2074 | `"        if len(calls) == 1:"` | — |
| [SRC-F725E90B2A-L002075](../../tests/test_web_agent.py#L2075) | 2075 | `"            return []"` | — |
| [SRC-F725E90B2A-L002076](../../tests/test_web_agent.py#L2076) | 2076 | `"        return ["` | — |
| [SRC-F725E90B2A-L002077](../../tests/test_web_agent.py#L2077) | 2077 | `"            {"` | — |
| [SRC-F725E90B2A-L002078](../../tests/test_web_agent.py#L2078) | 2078 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-F725E90B2A-L002079](../../tests/test_web_agent.py#L2079) | 2079 | `"                \"title\": \"OpenAI official website\","` | — |
| [SRC-F725E90B2A-L002080](../../tests/test_web_agent.py#L2080) | 2080 | `"                \"url\": \"https://openai.com/\","` | — |
| [SRC-F725E90B2A-L002081](../../tests/test_web_agent.py#L2081) | 2081 | `"                \"snippet\": \"Official website and products\","` | — |
| [SRC-F725E90B2A-L002082](../../tests/test_web_agent.py#L2082) | 2082 | `"            }"` | — |
| [SRC-F725E90B2A-L002083](../../tests/test_web_agent.py#L2083) | 2083 | `"        ]"` | — |
| [SRC-F725E90B2A-L002084](../../tests/test_web_agent.py#L2084) | 2084 | `""` | — |
| [SRC-F725E90B2A-L002085](../../tests/test_web_agent.py#L2085) | 2085 | `"    monkeypatch.setattr(agent, \"_search_web\", search)"` | — |
| [SRC-F725E90B2A-L002086](../../tests/test_web_agent.py#L2086) | 2086 | `"    monkeypatch.setattr(agent, \"_request_completion\", lambda *args, **kwargs: \"OK\")"` | — |
| [SRC-F725E90B2A-L002087](../../tests/test_web_agent.py#L2087) | 2087 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002088](../../tests/test_web_agent.py#L2088) | 2088 | `""` | — |
| [SRC-F725E90B2A-L002089](../../tests/test_web_agent.py#L2089) | 2089 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L002090](../../tests/test_web_agent.py#L2090) | 2090 | `""` | — |
| [SRC-F725E90B2A-L002091](../../tests/test_web_agent.py#L2091) | 2091 | `"    assert len(calls) == 2"` | — |
| [SRC-F725E90B2A-L002092](../../tests/test_web_agent.py#L2092) | 2092 | `"    assert report[\"checks\"][\"web_search\"][\"status\"] == \"passed\""` | — |
| [SRC-F725E90B2A-L002093](../../tests/test_web_agent.py#L2093) | 2093 | `"    assert report[\"checks\"][\"web_search\"][\"probe_count\"] == 2"` | — |
| [SRC-F725E90B2A-L002094](../../tests/test_web_agent.py#L2094) | 2094 | `"    assert report[\"checks\"][\"web_search\"][\"result_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002095](../../tests/test_web_agent.py#L2095) | 2095 | `""` | — |
| [SRC-F725E90B2A-L002096](../../tests/test_web_agent.py#L2096) | 2096 | `""` | — |
| [SRC-F725E90B2A-L002097](../../tests/test_web_agent.py#L2097) | 2097 | `"def test_lead_discovery_is_distinct_from_listing_search():"` | — |
| [SRC-F725E90B2A-L002098](../../tests/test_web_agent.py#L2098) | 2098 | `"    assert WebAgent._is_lead_search(\"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية\")"` | — |
| [SRC-F725E90B2A-L002099](../../tests/test_web_agent.py#L2099) | 2099 | `"    assert WebAgent._is_lead_search(\"Find buyers looking to buy apartments\")"` | — |
| [SRC-F725E90B2A-L002100](../../tests/test_web_agent.py#L2100) | 2100 | `"    assert not WebAgent._is_lead_search(\"ابحث عن شقق للبيع في العاصمة الإدارية\")"` | — |
| [SRC-F725E90B2A-L002101](../../tests/test_web_agent.py#L2101) | 2101 | `"    assert not WebAgent._is_lead_search(\"Find apartments for sale\")"` | — |
| [SRC-F725E90B2A-L002102](../../tests/test_web_agent.py#L2102) | 2102 | `""` | — |
| [SRC-F725E90B2A-L002103](../../tests/test_web_agent.py#L2103) | 2103 | `""` | — |
| [SRC-F725E90B2A-L002104](../../tests/test_web_agent.py#L2104) | 2104 | `"def test_buyer_intent_evidence_requires_explicit_purchase_signal():"` | — |
| [SRC-F725E90B2A-L002105](../../tests/test_web_agent.py#L2105) | 2105 | `"    listing = {"` | — |
| [SRC-F725E90B2A-L002106](../../tests/test_web_agent.py#L2106) | 2106 | `"        \"title\": \"شقق للبيع في العاصمة الإدارية الجديدة\","` | — |
| [SRC-F725E90B2A-L002107](../../tests/test_web_agent.py#L2107) | 2107 | `"        \"snippet\": \"أفضل شقق للبيع بالتقسيط\","` | — |
| [SRC-F725E90B2A-L002108](../../tests/test_web_agent.py#L2108) | 2108 | `"        \"page_text\": \"إعلانات وحدات سكنية للبيع بمساحات مختلفة.\","` | — |
| [SRC-F725E90B2A-L002109](../../tests/test_web_agent.py#L2109) | 2109 | `"    }"` | — |
| [SRC-F725E90B2A-L002110](../../tests/test_web_agent.py#L2110) | 2110 | `"    buyer_post = {"` | — |
| [SRC-F725E90B2A-L002111](../../tests/test_web_agent.py#L2111) | 2111 | `"        \"title\": \"بدور على شقة تمليك في العاصمة الإدارية\","` | — |
| [SRC-F725E90B2A-L002112](../../tests/test_web_agent.py#L2112) | 2112 | `"        \"snippet\": \"مطلوب شقة تمليك في العاصمة الإدارية.\","` | — |
| [SRC-F725E90B2A-L002113](../../tests/test_web_agent.py#L2113) | 2113 | `"        \"page_text\": \"أنا بدور على شقة تمليك في العاصمة الإدارية وعايز أشتري خلال شهر.\","` | — |
| [SRC-F725E90B2A-L002114](../../tests/test_web_agent.py#L2114) | 2114 | `"    }"` | — |
| [SRC-F725E90B2A-L002115](../../tests/test_web_agent.py#L2115) | 2115 | `"    assert WebAgent._lead_intent_evidence(listing) is None"` | — |
| [SRC-F725E90B2A-L002116](../../tests/test_web_agent.py#L2116) | 2116 | `"    signal = WebAgent._lead_intent_evidence(buyer_post)"` | — |
| [SRC-F725E90B2A-L002117](../../tests/test_web_agent.py#L2117) | 2117 | `"    assert signal is not None"` | — |
| [SRC-F725E90B2A-L002118](../../tests/test_web_agent.py#L2118) | 2118 | `"    assert signal[\"basis\"] == \"page_text\""` | — |
| [SRC-F725E90B2A-L002119](../../tests/test_web_agent.py#L2119) | 2119 | `""` | — |
| [SRC-F725E90B2A-L002120](../../tests/test_web_agent.py#L2120) | 2120 | `""` | — |
| [SRC-F725E90B2A-L002121](../../tests/test_web_agent.py#L2121) | 2121 | `"def test_lead_generation_does_not_present_sale_listings_as_buyers(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002122](../../tests/test_web_agent.py#L2122) | 2122 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002123](../../tests/test_web_agent.py#L2123) | 2123 | `"    question = \"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\""` | — |
| [SRC-F725E90B2A-L002124](../../tests/test_web_agent.py#L2124) | 2124 | `"    source_a = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002125](../../tests/test_web_agent.py#L2125) | 2125 | `"    source_a.update({"` | — |
| [SRC-F725E90B2A-L002126](../../tests/test_web_agent.py#L2126) | 2126 | `"        \"title\": \"شقق للبيع في العاصمة الإدارية الجديدة\","` | — |
| [SRC-F725E90B2A-L002127](../../tests/test_web_agent.py#L2127) | 2127 | `"        \"snippet\": \"قارن أسعار الشقق والمساحات وخطط السداد.\","` | — |
| [SRC-F725E90B2A-L002128](../../tests/test_web_agent.py#L2128) | 2128 | `"        \"page_text\": \"إعلانات شقق للبيع من شركات تطوير عقاري.\","` | — |
| [SRC-F725E90B2A-L002129](../../tests/test_web_agent.py#L2129) | 2129 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002130](../../tests/test_web_agent.py#L2130) | 2130 | `"    })"` | — |
| [SRC-F725E90B2A-L002131](../../tests/test_web_agent.py#L2131) | 2131 | `"    source_b = sample_source(1)"` | — |
| [SRC-F725E90B2A-L002132](../../tests/test_web_agent.py#L2132) | 2132 | `"    source_b.update({"` | — |
| [SRC-F725E90B2A-L002133](../../tests/test_web_agent.py#L2133) | 2133 | `"        \"title\": \"مشروعات عقارية في العاصمة الإدارية\","` | — |
| [SRC-F725E90B2A-L002134](../../tests/test_web_agent.py#L2134) | 2134 | `"        \"snippet\": \"تعرف على الوحدات السكنية المتاحة للبيع.\","` | — |
| [SRC-F725E90B2A-L002135](../../tests/test_web_agent.py#L2135) | 2135 | `"        \"page_text\": \"معلومات عامة عن مشروعات وشقق للبيع.\","` | — |
| [SRC-F725E90B2A-L002136](../../tests/test_web_agent.py#L2136) | 2136 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002137](../../tests/test_web_agent.py#L2137) | 2137 | `"    })"` | — |
| [SRC-F725E90B2A-L002138](../../tests/test_web_agent.py#L2138) | 2138 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002139](../../tests/test_web_agent.py#L2139) | 2139 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002140](../../tests/test_web_agent.py#L2140) | 2140 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002141](../../tests/test_web_agent.py#L2141) | 2141 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002142](../../tests/test_web_agent.py#L2142) | 2142 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002143](../../tests/test_web_agent.py#L2143) | 2143 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002144](../../tests/test_web_agent.py#L2144) | 2144 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002145](../../tests/test_web_agent.py#L2145) | 2145 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002146](../../tests/test_web_agent.py#L2146) | 2146 | `"    }"` | — |
| [SRC-F725E90B2A-L002147](../../tests/test_web_agent.py#L2147) | 2147 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda q, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002148](../../tests/test_web_agent.py#L2148) | 2148 | `"    monkeypatch.setattr(agent, \"_collect_research\", lambda p: ("` | — |
| [SRC-F725E90B2A-L002149](../../tests/test_web_agent.py#L2149) | 2149 | `"        [source_a, source_b], [], {"` | — |
| [SRC-F725E90B2A-L002150](../../tests/test_web_agent.py#L2150) | 2150 | `"            \"queries_planned\": 1, \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L002151](../../tests/test_web_agent.py#L2151) | 2151 | `"            \"query_results\": [{\"query\": question, \"results\": 2}],"` | — |
| [SRC-F725E90B2A-L002152](../../tests/test_web_agent.py#L2152) | 2152 | `"            \"unique_sources\": 2, \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L002153](../../tests/test_web_agent.py#L2153) | 2153 | `"            \"providers_used\": [\"test_provider\"], \"provider_counts\": {\"test_provider\": 2},"` | — |
| [SRC-F725E90B2A-L002154](../../tests/test_web_agent.py#L2154) | 2154 | `"            \"platform_counts\": {\"web\": 2}, \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002155](../../tests/test_web_agent.py#L2155) | 2155 | `"            \"depth\": \"standard\", \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002156](../../tests/test_web_agent.py#L2156) | 2156 | `"        }"` | — |
| [SRC-F725E90B2A-L002157](../../tests/test_web_agent.py#L2157) | 2157 | `"    ))"` | — |
| [SRC-F725E90B2A-L002158](../../tests/test_web_agent.py#L2158) | 2158 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002159](../../tests/test_web_agent.py#L2159) | 2159 | `"        agent, \"_generate\","` | — |
| [SRC-F725E90B2A-L002160](../../tests/test_web_agent.py#L2160) | 2160 | `"        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError(\"must not synthesize false leads\")),"` | — |
| [SRC-F725E90B2A-L002161](../../tests/test_web_agent.py#L2161) | 2161 | `"    )"` | — |
| [SRC-F725E90B2A-L002162](../../tests/test_web_agent.py#L2162) | 2162 | `""` | — |
| [SRC-F725E90B2A-L002163](../../tests/test_web_agent.py#L2163) | 2163 | `"    result = agent.answer(question)"` | — |
| [SRC-F725E90B2A-L002164](../../tests/test_web_agent.py#L2164) | 2164 | `""` | — |
| [SRC-F725E90B2A-L002165](../../tests/test_web_agent.py#L2165) | 2165 | `"    assert result[\"intent_route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-F725E90B2A-L002166](../../tests/test_web_agent.py#L2166) | 2166 | `"    assert result[\"kind\"] == \"lead_discovery_no_qualified_candidates\""` | — |
| [SRC-F725E90B2A-L002167](../../tests/test_web_agent.py#L2167) | 2167 | `"    assert result[\"search_report\"][\"lead_generation\"][\"candidate_signal_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002168](../../tests/test_web_agent.py#L2168) | 2168 | `"    assert result[\"search_report\"][\"lead_generation\"][\"related_results_reviewed\"] == 2"` | — |
| [SRC-F725E90B2A-L002169](../../tests/test_web_agent.py#L2169) | 2169 | `"    assert \"لم أعتبر إعلانات البيع\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L002170](../../tests/test_web_agent.py#L2170) | 2170 | `"    assert all(s[\"lead_qualification\"] == \"related_result_not_lead\" for s in result[\"sources\"])"` | — |
| [SRC-F725E90B2A-L002171](../../tests/test_web_agent.py#L2171) | 2171 | `""` | — |
| [SRC-F725E90B2A-L002172](../../tests/test_web_agent.py#L2172) | 2172 | `""` | — |
| [SRC-F725E90B2A-L002173](../../tests/test_web_agent.py#L2173) | 2173 | `"def test_lead_generation_search_plan_includes_high_intent_queries(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002174](../../tests/test_web_agent.py#L2174) | 2174 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002175](../../tests/test_web_agent.py#L2175) | 2175 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002176](../../tests/test_web_agent.py#L2176) | 2176 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002177](../../tests/test_web_agent.py#L2177) | 2177 | `"        \"queries\": [\"generic apartment listings\"],"` | — |
| [SRC-F725E90B2A-L002178](../../tests/test_web_agent.py#L2178) | 2178 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002179](../../tests/test_web_agent.py#L2179) | 2179 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002180](../../tests/test_web_agent.py#L2180) | 2180 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002181](../../tests/test_web_agent.py#L2181) | 2181 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002182](../../tests/test_web_agent.py#L2182) | 2182 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002183](../../tests/test_web_agent.py#L2183) | 2183 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002184](../../tests/test_web_agent.py#L2184) | 2184 | `"    }"` | — |
| [SRC-F725E90B2A-L002185](../../tests/test_web_agent.py#L2185) | 2185 | `""` | — |
| [SRC-F725E90B2A-L002186](../../tests/test_web_agent.py#L2186) | 2186 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L002187](../../tests/test_web_agent.py#L2187) | 2187 | `"        seen.update(research_plan)"` | — |
| [SRC-F725E90B2A-L002188](../../tests/test_web_agent.py#L2188) | 2188 | `"        source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002189](../../tests/test_web_agent.py#L2189) | 2189 | `"        source.update({"` | — |
| [SRC-F725E90B2A-L002190](../../tests/test_web_agent.py#L2190) | 2190 | `"            \"title\": \"مطلوب شقة تمليك في العاصمة الإدارية\","` | — |
| [SRC-F725E90B2A-L002191](../../tests/test_web_agent.py#L2191) | 2191 | `"            \"snippet\": \"صاحب المنشور يبحث عن شقة للشراء\","` | — |
| [SRC-F725E90B2A-L002192](../../tests/test_web_agent.py#L2192) | 2192 | `"            \"page_text\": \"مطلوب شقة تمليك في العاصمة الإدارية، أريد الشراء.\","` | — |
| [SRC-F725E90B2A-L002193](../../tests/test_web_agent.py#L2193) | 2193 | `"            \"queries\": list(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002194](../../tests/test_web_agent.py#L2194) | 2194 | `"        })"` | — |
| [SRC-F725E90B2A-L002195](../../tests/test_web_agent.py#L2195) | 2195 | `"        return [source], [], {"` | — |
| [SRC-F725E90B2A-L002196](../../tests/test_web_agent.py#L2196) | 2196 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002197](../../tests/test_web_agent.py#L2197) | 2197 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002198](../../tests/test_web_agent.py#L2198) | 2198 | `"            \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L002199](../../tests/test_web_agent.py#L2199) | 2199 | `"            \"unique_sources\": 1,"` | — |
| [SRC-F725E90B2A-L002200](../../tests/test_web_agent.py#L2200) | 2200 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-F725E90B2A-L002201](../../tests/test_web_agent.py#L2201) | 2201 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L002202](../../tests/test_web_agent.py#L2202) | 2202 | `"            \"provider_counts\": {\"test_provider\": 1},"` | — |
| [SRC-F725E90B2A-L002203](../../tests/test_web_agent.py#L2203) | 2203 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L002204](../../tests/test_web_agent.py#L2204) | 2204 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002205](../../tests/test_web_agent.py#L2205) | 2205 | `"            \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002206](../../tests/test_web_agent.py#L2206) | 2206 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002207](../../tests/test_web_agent.py#L2207) | 2207 | `"        }"` | — |
| [SRC-F725E90B2A-L002208](../../tests/test_web_agent.py#L2208) | 2208 | `""` | — |
| [SRC-F725E90B2A-L002209](../../tests/test_web_agent.py#L2209) | 2209 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda q, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002210](../../tests/test_web_agent.py#L2210) | 2210 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L002211](../../tests/test_web_agent.py#L2211) | 2211 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"عُثر على إشارة علنية محتملة [المصدر 1].\")"` | — |
| [SRC-F725E90B2A-L002212](../../tests/test_web_agent.py#L2212) | 2212 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L002213](../../tests/test_web_agent.py#L2213) | 2213 | `""` | — |
| [SRC-F725E90B2A-L002214](../../tests/test_web_agent.py#L2214) | 2214 | `"    result = agent.answer(\"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\")"` | — |
| [SRC-F725E90B2A-L002215](../../tests/test_web_agent.py#L2215) | 2215 | `""` | — |
| [SRC-F725E90B2A-L002216](../../tests/test_web_agent.py#L2216) | 2216 | `"    assert result[\"intent_route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-F725E90B2A-L002217](../../tests/test_web_agent.py#L2217) | 2217 | `"    assert seen[\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L002218](../../tests/test_web_agent.py#L2218) | 2218 | `"    assert len(seen[\"queries\"]) >= 4"` | — |
| [SRC-F725E90B2A-L002219](../../tests/test_web_agent.py#L2219) | 2219 | `"    assert any('\"مطلوب شراء\"' in q or '\"مطلوب شقه تمليك\"' in q for q in seen[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002220](../../tests/test_web_agent.py#L2220) | 2220 | `"    assert result[\"search_report\"][\"lead_generation\"][\"candidate_signal_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002221](../../tests/test_web_agent.py#L2221) | 2221 | `"    assert result[\"sources\"][0][\"lead_qualification\"] == \"public_buyer_intent_signal\""` | — |
| [SRC-F725E90B2A-L002222](../../tests/test_web_agent.py#L2222) | 2222 | `""` | — |
| [SRC-F725E90B2A-L002223](../../tests/test_web_agent.py#L2223) | 2223 | `""` | — |
| [SRC-F725E90B2A-L002224](../../tests/test_web_agent.py#L2224) | 2224 | `"def test_deepseek_search_adapter_normalizes_results_without_exposing_api_key(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002225](../../tests/test_web_agent.py#L2225) | 2225 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002226](../../tests/test_web_agent.py#L2226) | 2226 | `""` | — |
| [SRC-F725E90B2A-L002227](../../tests/test_web_agent.py#L2227) | 2227 | `"    monkeypatch.setenv(\"DEEPSEEK_SEARCH_API_KEY\", \"test-secret-key-that-must-not-appear\")"` | — |
| [SRC-F725E90B2A-L002228](../../tests/test_web_agent.py#L2228) | 2228 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002229](../../tests/test_web_agent.py#L2229) | 2229 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002230](../../tests/test_web_agent.py#L2230) | 2230 | `""` | — |
| [SRC-F725E90B2A-L002231](../../tests/test_web_agent.py#L2231) | 2231 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L002232](../../tests/test_web_agent.py#L2232) | 2232 | `"        def raise_for_status(self):"` | — |
| [SRC-F725E90B2A-L002233](../../tests/test_web_agent.py#L2233) | 2233 | `"            return None"` | — |
| [SRC-F725E90B2A-L002234](../../tests/test_web_agent.py#L2234) | 2234 | `""` | — |
| [SRC-F725E90B2A-L002235](../../tests/test_web_agent.py#L2235) | 2235 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L002236](../../tests/test_web_agent.py#L2236) | 2236 | `"            return {"` | — |
| [SRC-F725E90B2A-L002237](../../tests/test_web_agent.py#L2237) | 2237 | `"                \"results\": [{"` | — |
| [SRC-F725E90B2A-L002238](../../tests/test_web_agent.py#L2238) | 2238 | `"                    \"title\": \"Buyer wanted\","` | — |
| [SRC-F725E90B2A-L002239](../../tests/test_web_agent.py#L2239) | 2239 | `"                    \"url\": \"https://example.com/buyer\","` | — |
| [SRC-F725E90B2A-L002240](../../tests/test_web_agent.py#L2240) | 2240 | `"                    \"snippet\": \"Looking to buy a flat.\","` | — |
| [SRC-F725E90B2A-L002241](../../tests/test_web_agent.py#L2241) | 2241 | `"                    \"summary\": \"Looking to buy a flat in the requested area.\","` | — |
| [SRC-F725E90B2A-L002242](../../tests/test_web_agent.py#L2242) | 2242 | `"                    \"date\": \"2026-10-16T12:00:00Z\","` | — |
| [SRC-F725E90B2A-L002243](../../tests/test_web_agent.py#L2243) | 2243 | `"                    \"site_name\": \"Example\","` | — |
| [SRC-F725E90B2A-L002244](../../tests/test_web_agent.py#L2244) | 2244 | `"                    \"rerank_score\": 2.2,"` | — |
| [SRC-F725E90B2A-L002245](../../tests/test_web_agent.py#L2245) | 2245 | `"                    \"authority\": 2,"` | — |
| [SRC-F725E90B2A-L002246](../../tests/test_web_agent.py#L2246) | 2246 | `"                }]"` | — |
| [SRC-F725E90B2A-L002247](../../tests/test_web_agent.py#L2247) | 2247 | `"            }"` | — |
| [SRC-F725E90B2A-L002248](../../tests/test_web_agent.py#L2248) | 2248 | `""` | — |
| [SRC-F725E90B2A-L002249](../../tests/test_web_agent.py#L2249) | 2249 | `"    def fake_post(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002250](../../tests/test_web_agent.py#L2250) | 2250 | `"        seen[\"url\"] = url"` | — |
| [SRC-F725E90B2A-L002251](../../tests/test_web_agent.py#L2251) | 2251 | `"        seen.update(kwargs)"` | — |
| [SRC-F725E90B2A-L002252](../../tests/test_web_agent.py#L2252) | 2252 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L002253](../../tests/test_web_agent.py#L2253) | 2253 | `""` | — |
| [SRC-F725E90B2A-L002254](../../tests/test_web_agent.py#L2254) | 2254 | `"    monkeypatch.setattr(httpx, \"post\", fake_post)"` | — |
| [SRC-F725E90B2A-L002255](../../tests/test_web_agent.py#L2255) | 2255 | `"    rows = agent._search_deepseek_api(\"buyers looking to buy a flat\")"` | — |
| [SRC-F725E90B2A-L002256](../../tests/test_web_agent.py#L2256) | 2256 | `""` | — |
| [SRC-F725E90B2A-L002257](../../tests/test_web_agent.py#L2257) | 2257 | `"    assert seen[\"url\"] == \"https://api.deepseek.com/v1/tools/search\""` | — |
| [SRC-F725E90B2A-L002258](../../tests/test_web_agent.py#L2258) | 2258 | `"    assert seen[\"headers\"][\"Authorization\"] == \"Bearer test-secret-key-that-must-not-appear\""` | — |
| [SRC-F725E90B2A-L002259](../../tests/test_web_agent.py#L2259) | 2259 | `"    assert seen[\"json\"][\"count\"] == 6"` | — |
| [SRC-F725E90B2A-L002260](../../tests/test_web_agent.py#L2260) | 2260 | `"    assert rows[0][\"provider\"] == \"deepseek_search_api\""` | — |
| [SRC-F725E90B2A-L002261](../../tests/test_web_agent.py#L2261) | 2261 | `"    assert rows[0][\"snippet\"] == \"Looking to buy a flat in the requested area.\""` | — |
| [SRC-F725E90B2A-L002262](../../tests/test_web_agent.py#L2262) | 2262 | `"    assert rows[0][\"provider_rerank_score\"] == 2.2"` | — |
| [SRC-F725E90B2A-L002263](../../tests/test_web_agent.py#L2263) | 2263 | `"    assert \"test-secret-key-that-must-not-appear\" not in str(rows)"` | — |
| [SRC-F725E90B2A-L002264](../../tests/test_web_agent.py#L2264) | 2264 | `""` | — |
| [SRC-F725E90B2A-L002265](../../tests/test_web_agent.py#L2265) | 2265 | `""` | — |
| [SRC-F725E90B2A-L002266](../../tests/test_web_agent.py#L2266) | 2266 | `""` | — |
| [SRC-F725E90B2A-L002267](../../tests/test_web_agent.py#L2267) | 2267 | `"def test_diagnostics_distinguishes_connector_response_without_matches_from_offline(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002268](../../tests/test_web_agent.py#L2268) | 2268 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002269](../../tests/test_web_agent.py#L2269) | 2269 | `"    monkeypatch.setattr(agent, \"_request_completion\", lambda *args, **kwargs: \"OK\")"` | — |
| [SRC-F725E90B2A-L002270](../../tests/test_web_agent.py#L2270) | 2270 | `""` | — |
| [SRC-F725E90B2A-L002271](../../tests/test_web_agent.py#L2271) | 2271 | `"    def completed_empty_search(query):"` | — |
| [SRC-F725E90B2A-L002272](../../tests/test_web_agent.py#L2272) | 2272 | `"        agent._record_provider_diagnostic("` | — |
| [SRC-F725E90B2A-L002273](../../tests/test_web_agent.py#L2273) | 2273 | `"            \"bing_rss\", query, \"no_results\", result_count=0,"` | — |
| [SRC-F725E90B2A-L002274](../../tests/test_web_agent.py#L2274) | 2274 | `"            error=\"connector completed but returned no parseable results\","` | — |
| [SRC-F725E90B2A-L002275](../../tests/test_web_agent.py#L2275) | 2275 | `"        )"` | — |
| [SRC-F725E90B2A-L002276](../../tests/test_web_agent.py#L2276) | 2276 | `"        raise RuntimeError(\"no usable search matches\")"` | — |
| [SRC-F725E90B2A-L002277](../../tests/test_web_agent.py#L2277) | 2277 | `""` | — |
| [SRC-F725E90B2A-L002278](../../tests/test_web_agent.py#L2278) | 2278 | `"    monkeypatch.setattr(agent, \"_search_web\", completed_empty_search)"` | — |
| [SRC-F725E90B2A-L002279](../../tests/test_web_agent.py#L2279) | 2279 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L002280](../../tests/test_web_agent.py#L2280) | 2280 | `""` | — |
| [SRC-F725E90B2A-L002281](../../tests/test_web_agent.py#L2281) | 2281 | `"    assert report[\"checks\"][\"web_search\"][\"status\"] == \"degraded\""` | — |
| [SRC-F725E90B2A-L002282](../../tests/test_web_agent.py#L2282) | 2282 | `"    assert report[\"checks\"][\"web_search\"][\"result_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002283](../../tests/test_web_agent.py#L2283) | 2283 | `"    assert report[\"checks\"][\"web_search\"][\"completed_connector_responses\"] >= 1"` | — |
| [SRC-F725E90B2A-L002284](../../tests/test_web_agent.py#L2284) | 2284 | `"    assert \"completed a request\" in report[\"checks\"][\"web_search\"][\"note\"]"` | — |
| [SRC-F725E90B2A-L002285](../../tests/test_web_agent.py#L2285) | 2285 | `""` | — |
| [SRC-F725E90B2A-L002286](../../tests/test_web_agent.py#L2286) | 2286 | `""` | — |
| [SRC-F725E90B2A-L002287](../../tests/test_web_agent.py#L2287) | 2287 | `"def test_deepseek_search_request_budget_defaults_to_one_and_is_bounded(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002288](../../tests/test_web_agent.py#L2288) | 2288 | `"    monkeypatch.setenv(\"DEEPSEEK_SEARCH_API_KEY\", \"test-secret-key\")"` | — |
| [SRC-F725E90B2A-L002289](../../tests/test_web_agent.py#L2289) | 2289 | `"    monkeypatch.delenv(\"OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET\", raising=False)"` | — |
| [SRC-F725E90B2A-L002290](../../tests/test_web_agent.py#L2290) | 2290 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002291](../../tests/test_web_agent.py#L2291) | 2291 | `"    assert agent._reserve_deepseek_search_request() is True"` | — |
| [SRC-F725E90B2A-L002292](../../tests/test_web_agent.py#L2292) | 2292 | `"    assert agent._reserve_deepseek_search_request() is False"` | — |
| [SRC-F725E90B2A-L002293](../../tests/test_web_agent.py#L2293) | 2293 | `""` | — |
| [SRC-F725E90B2A-L002294](../../tests/test_web_agent.py#L2294) | 2294 | `"    monkeypatch.setenv(\"OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET\", \"2\")"` | — |
| [SRC-F725E90B2A-L002295](../../tests/test_web_agent.py#L2295) | 2295 | `"    other_agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002296](../../tests/test_web_agent.py#L2296) | 2296 | `"    assert other_agent._reserve_deepseek_search_request() is True"` | — |
| [SRC-F725E90B2A-L002297](../../tests/test_web_agent.py#L2297) | 2297 | `"    assert other_agent._reserve_deepseek_search_request() is True"` | — |
| [SRC-F725E90B2A-L002298](../../tests/test_web_agent.py#L2298) | 2298 | `"    assert other_agent._reserve_deepseek_search_request() is False"` | — |
| [SRC-F725E90B2A-L002299](../../tests/test_web_agent.py#L2299) | 2299 | `""` | — |
| [SRC-F725E90B2A-L002300](../../tests/test_web_agent.py#L2300) | 2300 | `""` | — |
| [SRC-F725E90B2A-L002301](../../tests/test_web_agent.py#L2301) | 2301 | `""` | — |
| [SRC-F725E90B2A-L002302](../../tests/test_web_agent.py#L2302) | 2302 | `"def test_diagnostics_distinguishes_completed_search_without_matches_from_connection_failure(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002303](../../tests/test_web_agent.py#L2303) | 2303 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002304](../../tests/test_web_agent.py#L2304) | 2304 | `"    # A stale record from a prior search must not make a new diagnostics call pass."` | — |
| [SRC-F725E90B2A-L002305](../../tests/test_web_agent.py#L2305) | 2305 | `"    agent._record_provider_diagnostic(\"old_provider\", \"old query\", \"ok\", 1)"` | — |
| [SRC-F725E90B2A-L002306](../../tests/test_web_agent.py#L2306) | 2306 | `""` | — |
| [SRC-F725E90B2A-L002307](../../tests/test_web_agent.py#L2307) | 2307 | `"    def no_results(query):"` | — |
| [SRC-F725E90B2A-L002308](../../tests/test_web_agent.py#L2308) | 2308 | `"        agent._record_provider_diagnostic(\"duckduckgo_html\", query, \"no_results\")"` | — |
| [SRC-F725E90B2A-L002309](../../tests/test_web_agent.py#L2309) | 2309 | `"        raise RuntimeError(\"no parseable results\")"` | — |
| [SRC-F725E90B2A-L002310](../../tests/test_web_agent.py#L2310) | 2310 | `""` | — |
| [SRC-F725E90B2A-L002311](../../tests/test_web_agent.py#L2311) | 2311 | `"    monkeypatch.setattr(agent, \"_search_web\", no_results)"` | — |
| [SRC-F725E90B2A-L002312](../../tests/test_web_agent.py#L2312) | 2312 | `"    report = agent.diagnostics(test_model=False, test_social=False)"` | — |
| [SRC-F725E90B2A-L002313](../../tests/test_web_agent.py#L2313) | 2313 | `""` | — |
| [SRC-F725E90B2A-L002314](../../tests/test_web_agent.py#L2314) | 2314 | `"    check = report[\"checks\"][\"web_search\"]"` | — |
| [SRC-F725E90B2A-L002315](../../tests/test_web_agent.py#L2315) | 2315 | `"    assert check[\"status\"] == \"degraded\""` | — |
| [SRC-F725E90B2A-L002316](../../tests/test_web_agent.py#L2316) | 2316 | `"    assert check[\"result_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002317](../../tests/test_web_agent.py#L2317) | 2317 | `"    assert check[\"completed_connector_responses\"] >= 1"` | — |
| [SRC-F725E90B2A-L002318](../../tests/test_web_agent.py#L2318) | 2318 | `"    assert \"completed a request\" in check[\"note\"]"` | — |
| [SRC-F725E90B2A-L002319](../../tests/test_web_agent.py#L2319) | 2319 | `"    assert \"old_provider\" not in str(check)"` | — |
| [SRC-F725E90B2A-L002320](../../tests/test_web_agent.py#L2320) | 2320 | `""` | — |
| [SRC-F725E90B2A-L002321](../../tests/test_web_agent.py#L2321) | 2321 | `""` | — |
| [SRC-F725E90B2A-L002322](../../tests/test_web_agent.py#L2322) | 2322 | `"def test_buyer_intent_phrase_inside_negated_text_is_not_a_lead_signal():"` | — |
| [SRC-F725E90B2A-L002323](../../tests/test_web_agent.py#L2323) | 2323 | `"    source = {"` | — |
| [SRC-F725E90B2A-L002324](../../tests/test_web_agent.py#L2324) | 2324 | `"        \"title\": \"Buyer discussion\","` | — |
| [SRC-F725E90B2A-L002325](../../tests/test_web_agent.py#L2325) | 2325 | `"        \"snippet\": \"I am not looking to buy an apartment this year.\","` | — |
| [SRC-F725E90B2A-L002326](../../tests/test_web_agent.py#L2326) | 2326 | `"        \"page_text\": \"I am not looking to buy an apartment this year.\","` | — |
| [SRC-F725E90B2A-L002327](../../tests/test_web_agent.py#L2327) | 2327 | `"    }"` | — |
| [SRC-F725E90B2A-L002328](../../tests/test_web_agent.py#L2328) | 2328 | `"    assert WebAgent._lead_intent_evidence(source) is None"` | — |
| [SRC-F725E90B2A-L002329](../../tests/test_web_agent.py#L2329) | 2329 | `""` | — |
| [SRC-F725E90B2A-L002330](../../tests/test_web_agent.py#L2330) | 2330 | `""` | — |
| [SRC-F725E90B2A-L002331](../../tests/test_web_agent.py#L2331) | 2331 | `""` | — |
| [SRC-F725E90B2A-L002332](../../tests/test_web_agent.py#L2332) | 2332 | `"def test_lead_generation_preserves_unknown_state_when_research_throws(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002333](../../tests/test_web_agent.py#L2333) | 2333 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002334](../../tests/test_web_agent.py#L2334) | 2334 | `"    question = \"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\""` | — |
| [SRC-F725E90B2A-L002335](../../tests/test_web_agent.py#L2335) | 2335 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002336](../../tests/test_web_agent.py#L2336) | 2336 | `"        \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L002337](../../tests/test_web_agent.py#L2337) | 2337 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002338](../../tests/test_web_agent.py#L2338) | 2338 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002339](../../tests/test_web_agent.py#L2339) | 2339 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002340](../../tests/test_web_agent.py#L2340) | 2340 | `"        \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L002341](../../tests/test_web_agent.py#L2341) | 2341 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002342](../../tests/test_web_agent.py#L2342) | 2342 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002343](../../tests/test_web_agent.py#L2343) | 2343 | `"    }"` | — |
| [SRC-F725E90B2A-L002344](../../tests/test_web_agent.py#L2344) | 2344 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda q, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002345](../../tests/test_web_agent.py#L2345) | 2345 | `""` | — |
| [SRC-F725E90B2A-L002346](../../tests/test_web_agent.py#L2346) | 2346 | `"    def fail_research(research_plan):"` | — |
| [SRC-F725E90B2A-L002347](../../tests/test_web_agent.py#L2347) | 2347 | `"        raise RuntimeError(\"mocked interrupted research\")"` | — |
| [SRC-F725E90B2A-L002348](../../tests/test_web_agent.py#L2348) | 2348 | `""` | — |
| [SRC-F725E90B2A-L002349](../../tests/test_web_agent.py#L2349) | 2349 | `"    monkeypatch.setattr(agent, \"_collect_research\", fail_research)"` | — |
| [SRC-F725E90B2A-L002350](../../tests/test_web_agent.py#L2350) | 2350 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002351](../../tests/test_web_agent.py#L2351) | 2351 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002352](../../tests/test_web_agent.py#L2352) | 2352 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L002353](../../tests/test_web_agent.py#L2353) | 2353 | `"        lambda *args, **kwargs: (_ for _ in ()).throw("` | — |
| [SRC-F725E90B2A-L002354](../../tests/test_web_agent.py#L2354) | 2354 | `"            AssertionError(\"must not generate a lead from an incomplete search\")"` | — |
| [SRC-F725E90B2A-L002355](../../tests/test_web_agent.py#L2355) | 2355 | `"        ),"` | — |
| [SRC-F725E90B2A-L002356](../../tests/test_web_agent.py#L2356) | 2356 | `"    )"` | — |
| [SRC-F725E90B2A-L002357](../../tests/test_web_agent.py#L2357) | 2357 | `""` | — |
| [SRC-F725E90B2A-L002358](../../tests/test_web_agent.py#L2358) | 2358 | `"    result = agent.answer(question)"` | — |
| [SRC-F725E90B2A-L002359](../../tests/test_web_agent.py#L2359) | 2359 | `"    lead = result[\"search_report\"][\"lead_generation\"]"` | — |
| [SRC-F725E90B2A-L002360](../../tests/test_web_agent.py#L2360) | 2360 | `""` | — |
| [SRC-F725E90B2A-L002361](../../tests/test_web_agent.py#L2361) | 2361 | `"    assert lead[\"status\"] == \"research_incomplete\""` | — |
| [SRC-F725E90B2A-L002362](../../tests/test_web_agent.py#L2362) | 2362 | `"    assert lead[\"candidate_signal_count\"] is None"` | — |
| [SRC-F725E90B2A-L002363](../../tests/test_web_agent.py#L2363) | 2363 | `"    assert lead[\"related_results_reviewed\"] is None"` | — |
| [SRC-F725E90B2A-L002364](../../tests/test_web_agent.py#L2364) | 2364 | `"    assert result[\"search_report\"][\"usable_sources_after_filtering\"] is None"` | — |
| [SRC-F725E90B2A-L002365](../../tests/test_web_agent.py#L2365) | 2365 | `"    assert result[\"search_report\"][\"evidence_signals\"] is None"` | — |
| [SRC-F725E90B2A-L002366](../../tests/test_web_agent.py#L2366) | 2366 | `"    assert \"لم أستطع تحديد\" in result[\"answer\"] or \"تعطل مسار البحث\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L002367](../../tests/test_web_agent.py#L2367) | 2367 | `""` | — |
| [SRC-F725E90B2A-L002368](../../tests/test_web_agent.py#L2368) | 2368 | `""` | — |
| [SRC-F725E90B2A-L002369](../../tests/test_web_agent.py#L2369) | 2369 | `""` | — |
| [SRC-F725E90B2A-L002370](../../tests/test_web_agent.py#L2370) | 2370 | `"def test_local_answer_exposes_request_budget_without_claiming_live_search():"` | — |
| [SRC-F725E90B2A-L002371](../../tests/test_web_agent.py#L2371) | 2371 | `"    result = WebAgent().answer(\"مرحبا\")"` | — |
| [SRC-F725E90B2A-L002372](../../tests/test_web_agent.py#L2372) | 2372 | `""` | — |
| [SRC-F725E90B2A-L002373](../../tests/test_web_agent.py#L2373) | 2373 | `"    budget = result[\"request_budget\"]"` | — |
| [SRC-F725E90B2A-L002374](../../tests/test_web_agent.py#L2374) | 2374 | `"    assert budget[\"policy\"] == \"cooperative_per_request_budget\""` | — |
| [SRC-F725E90B2A-L002375](../../tests/test_web_agent.py#L2375) | 2375 | `"    assert budget[\"counts\"][\"search_queries\"] == 0"` | — |
| [SRC-F725E90B2A-L002376](../../tests/test_web_agent.py#L2376) | 2376 | `"    assert budget[\"counts\"][\"model_calls\"] == 0"` | — |
| [SRC-F725E90B2A-L002377](../../tests/test_web_agent.py#L2377) | 2377 | `"    assert budget[\"hard_cancellation_guaranteed\"] is False"` | — |
| [SRC-F725E90B2A-L002378](../../tests/test_web_agent.py#L2378) | 2378 | `""` | — |
| [SRC-F725E90B2A-L002379](../../tests/test_web_agent.py#L2379) | 2379 | `""` | — |
| [SRC-F725E90B2A-L002380](../../tests/test_web_agent.py#L2380) | 2380 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L002381](../../tests/test_web_agent.py#L2381) | 2381 | `"    \"draft_answer\","` | — |
| [SRC-F725E90B2A-L002382](../../tests/test_web_agent.py#L2382) | 2382 | `"    ["` | — |
| [SRC-F725E90B2A-L002383](../../tests/test_web_agent.py#L2383) | 2383 | `"        \"وفق المقارنة، الخيار الأول أفضل من الثاني.\","` | — |
| [SRC-F725E90B2A-L002384](../../tests/test_web_agent.py#L2384) | 2384 | `"        \"وفق المقارنة، الخيار الأول أفضل من الثاني [المصدر 99].\","` | — |
| [SRC-F725E90B2A-L002385](../../tests/test_web_agent.py#L2385) | 2385 | `"    ],"` | — |
| [SRC-F725E90B2A-L002386](../../tests/test_web_agent.py#L2386) | 2386 | `")"` | — |
| [SRC-F725E90B2A-L002387](../../tests/test_web_agent.py#L2387) | 2387 | `"def test_reviewed_answer_without_valid_citations_cannot_be_rated_good("` | — |
| [SRC-F725E90B2A-L002388](../../tests/test_web_agent.py#L2388) | 2388 | `"    monkeypatch, draft_answer"` | — |
| [SRC-F725E90B2A-L002389](../../tests/test_web_agent.py#L2389) | 2389 | `"):"` | — |
| [SRC-F725E90B2A-L002390](../../tests/test_web_agent.py#L2390) | 2390 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002391](../../tests/test_web_agent.py#L2391) | 2391 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L002392](../../tests/test_web_agent.py#L2392) | 2392 | `"    domains = [\"alpha.org\", \"beta.net\", \"gamma.io\", \"delta.dev\"]"` | — |
| [SRC-F725E90B2A-L002393](../../tests/test_web_agent.py#L2393) | 2393 | `"    providers = [\"duckduckgo_html\", \"bing_rss\", \"duckduckgo_html\", \"bing_rss\"]"` | — |
| [SRC-F725E90B2A-L002394](../../tests/test_web_agent.py#L2394) | 2394 | `"    sources = []"` | — |
| [SRC-F725E90B2A-L002395](../../tests/test_web_agent.py#L2395) | 2395 | `"    for index, (domain, provider) in enumerate(zip(domains, providers, strict=True)):"` | — |
| [SRC-F725E90B2A-L002396](../../tests/test_web_agent.py#L2396) | 2396 | `"        source = sample_source(0)"` | — |
| [SRC-F725E90B2A-L002397](../../tests/test_web_agent.py#L2397) | 2397 | `"        source.update("` | — |
| [SRC-F725E90B2A-L002398](../../tests/test_web_agent.py#L2398) | 2398 | `"            {"` | — |
| [SRC-F725E90B2A-L002399](../../tests/test_web_agent.py#L2399) | 2399 | `"                \"title\": f\"مصدر اختبار {index + 1}\","` | — |
| [SRC-F725E90B2A-L002400](../../tests/test_web_agent.py#L2400) | 2400 | `"                \"url\": f\"https://{domain}/research\","` | — |
| [SRC-F725E90B2A-L002401](../../tests/test_web_agent.py#L2401) | 2401 | `"                \"domain\": domain,"` | — |
| [SRC-F725E90B2A-L002402](../../tests/test_web_agent.py#L2402) | 2402 | `"                \"providers\": [provider],"` | — |
| [SRC-F725E90B2A-L002403](../../tests/test_web_agent.py#L2403) | 2403 | `"                \"queries\": [\"قارن بالتفصيل بين طرق إدارة الميزانية\"],"` | — |
| [SRC-F725E90B2A-L002404](../../tests/test_web_agent.py#L2404) | 2404 | `"                \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L002405](../../tests/test_web_agent.py#L2405) | 2405 | `"                \"page_text\": f\"نص مصدر الاختبار رقم {index + 1}.\","` | — |
| [SRC-F725E90B2A-L002406](../../tests/test_web_agent.py#L2406) | 2406 | `"            }"` | — |
| [SRC-F725E90B2A-L002407](../../tests/test_web_agent.py#L2407) | 2407 | `"        )"` | — |
| [SRC-F725E90B2A-L002408](../../tests/test_web_agent.py#L2408) | 2408 | `"        sources.append(source)"` | — |
| [SRC-F725E90B2A-L002409](../../tests/test_web_agent.py#L2409) | 2409 | `""` | — |
| [SRC-F725E90B2A-L002410](../../tests/test_web_agent.py#L2410) | 2410 | `"    plan = {"` | — |
| [SRC-F725E90B2A-L002411](../../tests/test_web_agent.py#L2411) | 2411 | `"        \"queries\": [\"قارن بالتفصيل بين طرق إدارة الميزانية\"],"` | — |
| [SRC-F725E90B2A-L002412](../../tests/test_web_agent.py#L2412) | 2412 | `"        \"direct_urls\": [],"` | — |
| [SRC-F725E90B2A-L002413](../../tests/test_web_agent.py#L2413) | 2413 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L002414](../../tests/test_web_agent.py#L2414) | 2414 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L002415](../../tests/test_web_agent.py#L2415) | 2415 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002416](../../tests/test_web_agent.py#L2416) | 2416 | `"        \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L002417](../../tests/test_web_agent.py#L2417) | 2417 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002418](../../tests/test_web_agent.py#L2418) | 2418 | `"    }"` | — |
| [SRC-F725E90B2A-L002419](../../tests/test_web_agent.py#L2419) | 2419 | `"    report = {"` | — |
| [SRC-F725E90B2A-L002420](../../tests/test_web_agent.py#L2420) | 2420 | `"        \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L002421](../../tests/test_web_agent.py#L2421) | 2421 | `"        \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L002422](../../tests/test_web_agent.py#L2422) | 2422 | `"        \"query_results\": [{\"query\": plan[\"queries\"][0], \"results\": 4}],"` | — |
| [SRC-F725E90B2A-L002423](../../tests/test_web_agent.py#L2423) | 2423 | `"        \"unique_sources\": 4,"` | — |
| [SRC-F725E90B2A-L002424](../../tests/test_web_agent.py#L2424) | 2424 | `"        \"pages_fetched\": 4,"` | — |
| [SRC-F725E90B2A-L002425](../../tests/test_web_agent.py#L2425) | 2425 | `"        \"providers_used\": providers,"` | — |
| [SRC-F725E90B2A-L002426](../../tests/test_web_agent.py#L2426) | 2426 | `"        \"provider_counts\": {\"duckduckgo_html\": 2, \"bing_rss\": 2},"` | — |
| [SRC-F725E90B2A-L002427](../../tests/test_web_agent.py#L2427) | 2427 | `"        \"platform_counts\": {\"web\": 4},"` | — |
| [SRC-F725E90B2A-L002428](../../tests/test_web_agent.py#L2428) | 2428 | `"        \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002429](../../tests/test_web_agent.py#L2429) | 2429 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L002430](../../tests/test_web_agent.py#L2430) | 2430 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L002431](../../tests/test_web_agent.py#L2431) | 2431 | `"        \"evidence_signals\": {},"` | — |
| [SRC-F725E90B2A-L002432](../../tests/test_web_agent.py#L2432) | 2432 | `"    }"` | — |
| [SRC-F725E90B2A-L002433](../../tests/test_web_agent.py#L2433) | 2433 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: dict(plan))"` | — |
| [SRC-F725E90B2A-L002434](../../tests/test_web_agent.py#L2434) | 2434 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002435](../../tests/test_web_agent.py#L2435) | 2435 | `"        agent, \"_collect_research\", lambda research_plan: (sources, [], dict(report))"` | — |
| [SRC-F725E90B2A-L002436](../../tests/test_web_agent.py#L2436) | 2436 | `"    )"` | — |
| [SRC-F725E90B2A-L002437](../../tests/test_web_agent.py#L2437) | 2437 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L002438](../../tests/test_web_agent.py#L2438) | 2438 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: draft_answer)"` | — |
| [SRC-F725E90B2A-L002439](../../tests/test_web_agent.py#L2439) | 2439 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002440](../../tests/test_web_agent.py#L2440) | 2440 | `"        agent, \"_review_answer\", lambda question, answer, review_sources: answer"` | — |
| [SRC-F725E90B2A-L002441](../../tests/test_web_agent.py#L2441) | 2441 | `"    )"` | — |
| [SRC-F725E90B2A-L002442](../../tests/test_web_agent.py#L2442) | 2442 | `""` | — |
| [SRC-F725E90B2A-L002443](../../tests/test_web_agent.py#L2443) | 2443 | `"    result = agent.answer(plan[\"queries\"][0], mode=\"deep\")"` | — |
| [SRC-F725E90B2A-L002444](../../tests/test_web_agent.py#L2444) | 2444 | `""` | — |
| [SRC-F725E90B2A-L002445](../../tests/test_web_agent.py#L2445) | 2445 | `"    assert result[\"used_language_model\"] is True"` | — |
| [SRC-F725E90B2A-L002446](../../tests/test_web_agent.py#L2446) | 2446 | `"    assert result[\"search_report\"][\"second_pass_review\"] == \"model_claim_audit_completed\""` | — |
| [SRC-F725E90B2A-L002447](../../tests/test_web_agent.py#L2447) | 2447 | `"    assert result[\"citation_validation\"][\"valid_citation_count\"] == 0"` | — |
| [SRC-F725E90B2A-L002448](../../tests/test_web_agent.py#L2448) | 2448 | `"    assert result[\"research_quality\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L002449](../../tests/test_web_agent.py#L2449) | 2449 | `"    assert result[\"search_report\"][\"research_quality\"] == \"partial\""` | — |
| [SRC-F725E90B2A-L002450](../../tests/test_web_agent.py#L2450) | 2450 | `"    assert result[\"answer_evidence_status\"] == \"reviewed_answer_has_no_valid_citations\""` | — |
| [SRC-F725E90B2A-L002451](../../tests/test_web_agent.py#L2451) | 2451 | `"    assert result[\"citation_validation\"][\"claim_support\"] == ("` | — |
| [SRC-F725E90B2A-L002452](../../tests/test_web_agent.py#L2452) | 2452 | `"        \"not_established_no_valid_source_citations\""` | — |
| [SRC-F725E90B2A-L002453](../../tests/test_web_agent.py#L2453) | 2453 | `"    )"` | — |
| [SRC-F725E90B2A-L002454](../../tests/test_web_agent.py#L2454) | 2454 | `"    assert any(\"لا تحتوي على إحالات صالحة\" in warning for warning in result[\"warnings\"])"` | — |
| [SRC-F725E90B2A-L002455](../../tests/test_web_agent.py#L2455) | 2455 | `""` | — |
| [SRC-F725E90B2A-L002456](../../tests/test_web_agent.py#L2456) | 2456 | `"# Network-boundary regression tests. These use mocked transports and never make"` | — |
| [SRC-F725E90B2A-L002457](../../tests/test_web_agent.py#L2457) | 2457 | `"# an outbound connection; they protect against SSRF and redirect/DNS-rebinding regressions."` | — |
| [SRC-F725E90B2A-L002458](../../tests/test_web_agent.py#L2458) | 2458 | `"def test_public_ip_literals_rejects_mixed_public_and_private_dns_answers(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002459](../../tests/test_web_agent.py#L2459) | 2459 | `"    import socket"` | — |
| [SRC-F725E90B2A-L002460](../../tests/test_web_agent.py#L2460) | 2460 | `""` | — |
| [SRC-F725E90B2A-L002461](../../tests/test_web_agent.py#L2461) | 2461 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L002462](../../tests/test_web_agent.py#L2462) | 2462 | `""` | — |
| [SRC-F725E90B2A-L002463](../../tests/test_web_agent.py#L2463) | 2463 | `"    answers = ["` | — |
| [SRC-F725E90B2A-L002464](../../tests/test_web_agent.py#L2464) | 2464 | `"        (socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, \"\", (\"93.184.216.34\", 80)),"` | — |
| [SRC-F725E90B2A-L002465](../../tests/test_web_agent.py#L2465) | 2465 | `"        (socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, \"\", (\"10.10.0.8\", 80)),"` | — |
| [SRC-F725E90B2A-L002466](../../tests/test_web_agent.py#L2466) | 2466 | `"    ]"` | — |
| [SRC-F725E90B2A-L002467](../../tests/test_web_agent.py#L2467) | 2467 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002468](../../tests/test_web_agent.py#L2468) | 2468 | `"        web_agent.socket,"` | — |
| [SRC-F725E90B2A-L002469](../../tests/test_web_agent.py#L2469) | 2469 | `"        \"getaddrinfo\","` | — |
| [SRC-F725E90B2A-L002470](../../tests/test_web_agent.py#L2470) | 2470 | `"        lambda host, port, type: answers,"` | — |
| [SRC-F725E90B2A-L002471](../../tests/test_web_agent.py#L2471) | 2471 | `"    )"` | — |
| [SRC-F725E90B2A-L002472](../../tests/test_web_agent.py#L2472) | 2472 | `""` | — |
| [SRC-F725E90B2A-L002473](../../tests/test_web_agent.py#L2473) | 2473 | `"    # One private DNS answer must fail closed, even when another answer is public."` | — |
| [SRC-F725E90B2A-L002474](../../tests/test_web_agent.py#L2474) | 2474 | `"    assert web_agent._public_ip_literals(\"mixed.example\") is None"` | — |
| [SRC-F725E90B2A-L002475](../../tests/test_web_agent.py#L2475) | 2475 | `""` | — |
| [SRC-F725E90B2A-L002476](../../tests/test_web_agent.py#L2476) | 2476 | `""` | — |
| [SRC-F725E90B2A-L002477](../../tests/test_web_agent.py#L2477) | 2477 | `"def test_pinned_connect_url_uses_checked_ip_without_losing_logical_path():"` | — |
| [SRC-F725E90B2A-L002478](../../tests/test_web_agent.py#L2478) | 2478 | `"    from agents.web_agent import _pinned_connect_url"` | — |
| [SRC-F725E90B2A-L002479](../../tests/test_web_agent.py#L2479) | 2479 | `""` | — |
| [SRC-F725E90B2A-L002480](../../tests/test_web_agent.py#L2480) | 2480 | `"    assert _pinned_connect_url("` | — |
| [SRC-F725E90B2A-L002481](../../tests/test_web_agent.py#L2481) | 2481 | `"        \"https://example.test:443/path?q=1\","` | — |
| [SRC-F725E90B2A-L002482](../../tests/test_web_agent.py#L2482) | 2482 | `"        \"93.184.216.34\","` | — |
| [SRC-F725E90B2A-L002483](../../tests/test_web_agent.py#L2483) | 2483 | `"    ) == \"https://93.184.216.34:443/path?q=1\""` | — |
| [SRC-F725E90B2A-L002484](../../tests/test_web_agent.py#L2484) | 2484 | `""` | — |
| [SRC-F725E90B2A-L002485](../../tests/test_web_agent.py#L2485) | 2485 | `""` | — |
| [SRC-F725E90B2A-L002486](../../tests/test_web_agent.py#L2486) | 2486 | `"def test_fetch_page_rejects_private_redirect_before_connecting(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002487](../../tests/test_web_agent.py#L2487) | 2487 | `"    from contextlib import contextmanager"` | — |
| [SRC-F725E90B2A-L002488](../../tests/test_web_agent.py#L2488) | 2488 | `""` | — |
| [SRC-F725E90B2A-L002489](../../tests/test_web_agent.py#L2489) | 2489 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002490](../../tests/test_web_agent.py#L2490) | 2490 | `""` | — |
| [SRC-F725E90B2A-L002491](../../tests/test_web_agent.py#L2491) | 2491 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L002492](../../tests/test_web_agent.py#L2492) | 2492 | `""` | — |
| [SRC-F725E90B2A-L002493](../../tests/test_web_agent.py#L2493) | 2493 | `"    resolved_hosts = []"` | — |
| [SRC-F725E90B2A-L002494](../../tests/test_web_agent.py#L2494) | 2494 | `"    requests = []"` | — |
| [SRC-F725E90B2A-L002495](../../tests/test_web_agent.py#L2495) | 2495 | `""` | — |
| [SRC-F725E90B2A-L002496](../../tests/test_web_agent.py#L2496) | 2496 | `"    def resolve_public_ip(host):"` | — |
| [SRC-F725E90B2A-L002497](../../tests/test_web_agent.py#L2497) | 2497 | `"        resolved_hosts.append(host)"` | — |
| [SRC-F725E90B2A-L002498](../../tests/test_web_agent.py#L2498) | 2498 | `"        return [\"93.184.216.34\"] if host == \"first.example\" else None"` | — |
| [SRC-F725E90B2A-L002499](../../tests/test_web_agent.py#L2499) | 2499 | `""` | — |
| [SRC-F725E90B2A-L002500](../../tests/test_web_agent.py#L2500) | 2500 | `"    monkeypatch.setattr(web_agent, \"_public_ip_literals\", resolve_public_ip)"` | — |
| [SRC-F725E90B2A-L002501](../../tests/test_web_agent.py#L2501) | 2501 | `""` | — |
| [SRC-F725E90B2A-L002502](../../tests/test_web_agent.py#L2502) | 2502 | `"    class RedirectResponse:"` | — |
| [SRC-F725E90B2A-L002503](../../tests/test_web_agent.py#L2503) | 2503 | `"        status_code = 302"` | — |
| [SRC-F725E90B2A-L002504](../../tests/test_web_agent.py#L2504) | 2504 | `""` | — |
| [SRC-F725E90B2A-L002505](../../tests/test_web_agent.py#L2505) | 2505 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L002506](../../tests/test_web_agent.py#L2506) | 2506 | `"            self.headers = {\"location\": \"http://127.0.0.1/admin\"}"` | — |
| [SRC-F725E90B2A-L002507](../../tests/test_web_agent.py#L2507) | 2507 | `""` | — |
| [SRC-F725E90B2A-L002508](../../tests/test_web_agent.py#L2508) | 2508 | `"    @contextmanager"` | — |
| [SRC-F725E90B2A-L002509](../../tests/test_web_agent.py#L2509) | 2509 | `"    def fake_stream(self, method, url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002510](../../tests/test_web_agent.py#L2510) | 2510 | `"        requests.append((method, str(url), kwargs))"` | — |
| [SRC-F725E90B2A-L002511](../../tests/test_web_agent.py#L2511) | 2511 | `"        yield RedirectResponse()"` | — |
| [SRC-F725E90B2A-L002512](../../tests/test_web_agent.py#L2512) | 2512 | `""` | — |
| [SRC-F725E90B2A-L002513](../../tests/test_web_agent.py#L2513) | 2513 | `"    class FakeClient:"` | — |
| [SRC-F725E90B2A-L002514](../../tests/test_web_agent.py#L2514) | 2514 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-F725E90B2A-L002515](../../tests/test_web_agent.py#L2515) | 2515 | `"            self.options = kwargs"` | — |
| [SRC-F725E90B2A-L002516](../../tests/test_web_agent.py#L2516) | 2516 | `""` | — |
| [SRC-F725E90B2A-L002517](../../tests/test_web_agent.py#L2517) | 2517 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L002518](../../tests/test_web_agent.py#L2518) | 2518 | `"            return self"` | — |
| [SRC-F725E90B2A-L002519](../../tests/test_web_agent.py#L2519) | 2519 | `""` | — |
| [SRC-F725E90B2A-L002520](../../tests/test_web_agent.py#L2520) | 2520 | `"        def __exit__(self, *_args):"` | — |
| [SRC-F725E90B2A-L002521](../../tests/test_web_agent.py#L2521) | 2521 | `"            return False"` | — |
| [SRC-F725E90B2A-L002522](../../tests/test_web_agent.py#L2522) | 2522 | `""` | — |
| [SRC-F725E90B2A-L002523](../../tests/test_web_agent.py#L2523) | 2523 | `"        stream = fake_stream"` | — |
| [SRC-F725E90B2A-L002524](../../tests/test_web_agent.py#L2524) | 2524 | `""` | — |
| [SRC-F725E90B2A-L002525](../../tests/test_web_agent.py#L2525) | 2525 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-F725E90B2A-L002526](../../tests/test_web_agent.py#L2526) | 2526 | `""` | — |
| [SRC-F725E90B2A-L002527](../../tests/test_web_agent.py#L2527) | 2527 | `"    assert web_agent.WebAgent()._fetch_page(\"https://first.example/article\") == (\"\", \"\")"` | — |
| [SRC-F725E90B2A-L002528](../../tests/test_web_agent.py#L2528) | 2528 | `"    assert resolved_hosts == [\"first.example\"]"` | — |
| [SRC-F725E90B2A-L002529](../../tests/test_web_agent.py#L2529) | 2529 | `"    assert len(requests) == 1"` | — |
| [SRC-F725E90B2A-L002530](../../tests/test_web_agent.py#L2530) | 2530 | `"    assert requests[0][1] == \"https://93.184.216.34/article\""` | — |
| [SRC-F725E90B2A-L002531](../../tests/test_web_agent.py#L2531) | 2531 | `"    assert requests[0][2][\"headers\"][\"Host\"] == \"first.example\""` | — |
| [SRC-F725E90B2A-L002532](../../tests/test_web_agent.py#L2532) | 2532 | `"    assert requests[0][2][\"extensions\"][\"sni_hostname\"] == \"first.example\""` | — |
| [SRC-F725E90B2A-L002533](../../tests/test_web_agent.py#L2533) | 2533 | `""` | — |
| [SRC-F725E90B2A-L002534](../../tests/test_web_agent.py#L2534) | 2534 | `""` | — |
| [SRC-F725E90B2A-L002535](../../tests/test_web_agent.py#L2535) | 2535 | `"def test_fetch_page_revalidates_dns_for_each_redirect_destination(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002536](../../tests/test_web_agent.py#L2536) | 2536 | `"    from contextlib import contextmanager"` | — |
| [SRC-F725E90B2A-L002537](../../tests/test_web_agent.py#L2537) | 2537 | `""` | — |
| [SRC-F725E90B2A-L002538](../../tests/test_web_agent.py#L2538) | 2538 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002539](../../tests/test_web_agent.py#L2539) | 2539 | `""` | — |
| [SRC-F725E90B2A-L002540](../../tests/test_web_agent.py#L2540) | 2540 | `"    from agents import web_agent"` | — |
| [SRC-F725E90B2A-L002541](../../tests/test_web_agent.py#L2541) | 2541 | `""` | — |
| [SRC-F725E90B2A-L002542](../../tests/test_web_agent.py#L2542) | 2542 | `"    resolved_hosts = []"` | — |
| [SRC-F725E90B2A-L002543](../../tests/test_web_agent.py#L2543) | 2543 | `"    requests = []"` | — |
| [SRC-F725E90B2A-L002544](../../tests/test_web_agent.py#L2544) | 2544 | `""` | — |
| [SRC-F725E90B2A-L002545](../../tests/test_web_agent.py#L2545) | 2545 | `"    def resolve_public_ip(host):"` | — |
| [SRC-F725E90B2A-L002546](../../tests/test_web_agent.py#L2546) | 2546 | `"        resolved_hosts.append(host)"` | — |
| [SRC-F725E90B2A-L002547](../../tests/test_web_agent.py#L2547) | 2547 | `"        if host == \"first.example\":"` | — |
| [SRC-F725E90B2A-L002548](../../tests/test_web_agent.py#L2548) | 2548 | `"            return [\"93.184.216.34\"]"` | — |
| [SRC-F725E90B2A-L002549](../../tests/test_web_agent.py#L2549) | 2549 | `"        # Model a redirect destination that resolves to no verified public IP."` | — |
| [SRC-F725E90B2A-L002550](../../tests/test_web_agent.py#L2550) | 2550 | `"        return None"` | — |
| [SRC-F725E90B2A-L002551](../../tests/test_web_agent.py#L2551) | 2551 | `""` | — |
| [SRC-F725E90B2A-L002552](../../tests/test_web_agent.py#L2552) | 2552 | `"    monkeypatch.setattr(web_agent, \"_public_ip_literals\", resolve_public_ip)"` | — |
| [SRC-F725E90B2A-L002553](../../tests/test_web_agent.py#L2553) | 2553 | `""` | — |
| [SRC-F725E90B2A-L002554](../../tests/test_web_agent.py#L2554) | 2554 | `"    class RedirectResponse:"` | — |
| [SRC-F725E90B2A-L002555](../../tests/test_web_agent.py#L2555) | 2555 | `"        status_code = 302"` | — |
| [SRC-F725E90B2A-L002556](../../tests/test_web_agent.py#L2556) | 2556 | `""` | — |
| [SRC-F725E90B2A-L002557](../../tests/test_web_agent.py#L2557) | 2557 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L002558](../../tests/test_web_agent.py#L2558) | 2558 | `"            self.headers = {\"location\": \"https://second.example/internal\"}"` | — |
| [SRC-F725E90B2A-L002559](../../tests/test_web_agent.py#L2559) | 2559 | `""` | — |
| [SRC-F725E90B2A-L002560](../../tests/test_web_agent.py#L2560) | 2560 | `"    @contextmanager"` | — |
| [SRC-F725E90B2A-L002561](../../tests/test_web_agent.py#L2561) | 2561 | `"    def fake_stream(self, method, url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002562](../../tests/test_web_agent.py#L2562) | 2562 | `"        requests.append((method, str(url), kwargs))"` | — |
| [SRC-F725E90B2A-L002563](../../tests/test_web_agent.py#L2563) | 2563 | `"        yield RedirectResponse()"` | — |
| [SRC-F725E90B2A-L002564](../../tests/test_web_agent.py#L2564) | 2564 | `""` | — |
| [SRC-F725E90B2A-L002565](../../tests/test_web_agent.py#L2565) | 2565 | `"    class FakeClient:"` | — |
| [SRC-F725E90B2A-L002566](../../tests/test_web_agent.py#L2566) | 2566 | `"        def __init__(self, **kwargs):"` | — |
| [SRC-F725E90B2A-L002567](../../tests/test_web_agent.py#L2567) | 2567 | `"            self.options = kwargs"` | — |
| [SRC-F725E90B2A-L002568](../../tests/test_web_agent.py#L2568) | 2568 | `""` | — |
| [SRC-F725E90B2A-L002569](../../tests/test_web_agent.py#L2569) | 2569 | `"        def __enter__(self):"` | — |
| [SRC-F725E90B2A-L002570](../../tests/test_web_agent.py#L2570) | 2570 | `"            return self"` | — |
| [SRC-F725E90B2A-L002571](../../tests/test_web_agent.py#L2571) | 2571 | `""` | — |
| [SRC-F725E90B2A-L002572](../../tests/test_web_agent.py#L2572) | 2572 | `"        def __exit__(self, *_args):"` | — |
| [SRC-F725E90B2A-L002573](../../tests/test_web_agent.py#L2573) | 2573 | `"            return False"` | — |
| [SRC-F725E90B2A-L002574](../../tests/test_web_agent.py#L2574) | 2574 | `""` | — |
| [SRC-F725E90B2A-L002575](../../tests/test_web_agent.py#L2575) | 2575 | `"        stream = fake_stream"` | — |
| [SRC-F725E90B2A-L002576](../../tests/test_web_agent.py#L2576) | 2576 | `""` | — |
| [SRC-F725E90B2A-L002577](../../tests/test_web_agent.py#L2577) | 2577 | `"    monkeypatch.setattr(httpx, \"Client\", FakeClient)"` | — |
| [SRC-F725E90B2A-L002578](../../tests/test_web_agent.py#L2578) | 2578 | `""` | — |
| [SRC-F725E90B2A-L002579](../../tests/test_web_agent.py#L2579) | 2579 | `"    assert web_agent.WebAgent()._fetch_page(\"https://first.example/article\") == (\"\", \"\")"` | — |
| [SRC-F725E90B2A-L002580](../../tests/test_web_agent.py#L2580) | 2580 | `"    assert resolved_hosts == [\"first.example\", \"second.example\"]"` | — |
| [SRC-F725E90B2A-L002581](../../tests/test_web_agent.py#L2581) | 2581 | `"    # The second host is validated before any connection attempt to it."` | — |
| [SRC-F725E90B2A-L002582](../../tests/test_web_agent.py#L2582) | 2582 | `"    assert len(requests) == 1"` | — |
| [SRC-F725E90B2A-L002583](../../tests/test_web_agent.py#L2583) | 2583 | `""` | — |
| [SRC-F725E90B2A-L002584](../../tests/test_web_agent.py#L2584) | 2584 | `""` | — |
| [SRC-F725E90B2A-L002585](../../tests/test_web_agent.py#L2585) | 2585 | `""` | — |
| [SRC-F725E90B2A-L002586](../../tests/test_web_agent.py#L2586) | 2586 | `"def test_history_search_query_uses_shared_context_resolver():"` | — |
| [SRC-F725E90B2A-L002587](../../tests/test_web_agent.py#L2587) | 2587 | `"    history = ["` | — |
| [SRC-F725E90B2A-L002588](../../tests/test_web_agent.py#L2588) | 2588 | `"        {\"role\": \"user\", \"content\": \"سعر آيفون 16 في مصر\"},"` | — |
| [SRC-F725E90B2A-L002589](../../tests/test_web_agent.py#L2589) | 2589 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن السعر.\"},"` | — |
| [SRC-F725E90B2A-L002590](../../tests/test_web_agent.py#L2590) | 2590 | `"    ]"` | — |
| [SRC-F725E90B2A-L002591](../../tests/test_web_agent.py#L2591) | 2591 | `"    query = WebAgent._history_search_query(\"هل فيه ضمان؟\", history)"` | — |
| [SRC-F725E90B2A-L002592](../../tests/test_web_agent.py#L2592) | 2592 | `"    assert \"آيفون 16\" in query"` | — |
| [SRC-F725E90B2A-L002593](../../tests/test_web_agent.py#L2593) | 2593 | `"    assert \"ضمان\" in query"` | — |
| [SRC-F725E90B2A-L002594](../../tests/test_web_agent.py#L2594) | 2594 | `""` | — |
| [SRC-F725E90B2A-L002595](../../tests/test_web_agent.py#L2595) | 2595 | `""` | — |
| [SRC-F725E90B2A-L002596](../../tests/test_web_agent.py#L2596) | 2596 | `"def test_history_search_query_does_not_reuse_stale_topic_after_acknowledgment():"` | — |
| [SRC-F725E90B2A-L002597](../../tests/test_web_agent.py#L2597) | 2597 | `"    history = ["` | — |
| [SRC-F725E90B2A-L002598](../../tests/test_web_agent.py#L2598) | 2598 | `"        {\"role\": \"user\", \"content\": \"سعر آيفون 16 في مصر\"},"` | — |
| [SRC-F725E90B2A-L002599](../../tests/test_web_agent.py#L2599) | 2599 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن السعر.\"},"` | — |
| [SRC-F725E90B2A-L002600](../../tests/test_web_agent.py#L2600) | 2600 | `"        {\"role\": \"user\", \"content\": \"شكرا\"},"` | — |
| [SRC-F725E90B2A-L002601](../../tests/test_web_agent.py#L2601) | 2601 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-F725E90B2A-L002602](../../tests/test_web_agent.py#L2602) | 2602 | `"    ]"` | — |
| [SRC-F725E90B2A-L002603](../../tests/test_web_agent.py#L2603) | 2603 | `"    assert WebAgent._history_search_query(\"فين؟\", history) == \"فين؟\""` | — |
| [SRC-F725E90B2A-L002604](../../tests/test_web_agent.py#L2604) | 2604 | `""` | — |
| [SRC-F725E90B2A-L002605](../../tests/test_web_agent.py#L2605) | 2605 | `""` | — |
| [SRC-F725E90B2A-L002606](../../tests/test_web_agent.py#L2606) | 2606 | `"def test_frontend_exposes_structured_page_fetch_statuses():"` | — |
| [SRC-F725E90B2A-L002607](../../tests/test_web_agent.py#L2607) | 2607 | `"    html_path = Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\""` | — |
| [SRC-F725E90B2A-L002608](../../tests/test_web_agent.py#L2608) | 2608 | `"    html = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002609](../../tests/test_web_agent.py#L2609) | 2609 | `"    assert \"page_fetch_status\" in html"` | — |
| [SRC-F725E90B2A-L002610](../../tests/test_web_agent.py#L2610) | 2610 | `"    assert \"partial_extraction\" in html"` | — |
| [SRC-F725E90B2A-L002611](../../tests/test_web_agent.py#L2611) | 2611 | `"    assert \"لم يُستخرج نص؛ قد تكون الصفحة ديناميكية أو محجوبة\" in html"` | — |
| [SRC-F725E90B2A-L002612](../../tests/test_web_agent.py#L2612) | 2612 | `"    assert \"تشخيص الموصلات في هذا الطلب\" in html"` | — |
| [SRC-F725E90B2A-L002613](../../tests/test_web_agent.py#L2613) | 2613 | `""` | — |
| [SRC-F725E90B2A-L002614](../../tests/test_web_agent.py#L2614) | 2614 | `""` | — |
| [SRC-F725E90B2A-L002615](../../tests/test_web_agent.py#L2615) | 2615 | `"@pytest.mark.parametrize("` | — |
| [SRC-F725E90B2A-L002616](../../tests/test_web_agent.py#L2616) | 2616 | `"    \"method_name\","` | — |
| [SRC-F725E90B2A-L002617](../../tests/test_web_agent.py#L2617) | 2617 | `"    [\"_search_duckduckgo_html\", \"_search_bing_rss\", \"_search_news\"],"` | — |
| [SRC-F725E90B2A-L002618](../../tests/test_web_agent.py#L2618) | 2618 | `")"` | — |
| [SRC-F725E90B2A-L002619](../../tests/test_web_agent.py#L2619) | 2619 | `"def test_search_providers_do_not_follow_redirects_automatically("` | — |
| [SRC-F725E90B2A-L002620](../../tests/test_web_agent.py#L2620) | 2620 | `"    monkeypatch, method_name"` | — |
| [SRC-F725E90B2A-L002621](../../tests/test_web_agent.py#L2621) | 2621 | `"):"` | — |
| [SRC-F725E90B2A-L002622](../../tests/test_web_agent.py#L2622) | 2622 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L002623](../../tests/test_web_agent.py#L2623) | 2623 | `""` | — |
| [SRC-F725E90B2A-L002624](../../tests/test_web_agent.py#L2624) | 2624 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002625](../../tests/test_web_agent.py#L2625) | 2625 | `"    observed = []"` | — |
| [SRC-F725E90B2A-L002626](../../tests/test_web_agent.py#L2626) | 2626 | `""` | — |
| [SRC-F725E90B2A-L002627](../../tests/test_web_agent.py#L2627) | 2627 | `"    class RedirectResponse:"` | — |
| [SRC-F725E90B2A-L002628](../../tests/test_web_agent.py#L2628) | 2628 | `"        def __init__(self):"` | — |
| [SRC-F725E90B2A-L002629](../../tests/test_web_agent.py#L2629) | 2629 | `"            self.status_code = 302"` | — |
| [SRC-F725E90B2A-L002630](../../tests/test_web_agent.py#L2630) | 2630 | `"            self.headers = {\"location\": \"http://127.0.0.1:8765/private\"}"` | — |
| [SRC-F725E90B2A-L002631](../../tests/test_web_agent.py#L2631) | 2631 | `"            self.text = \"redirect\""` | — |
| [SRC-F725E90B2A-L002632](../../tests/test_web_agent.py#L2632) | 2632 | `"            self.content = b\"redirect\""` | — |
| [SRC-F725E90B2A-L002633](../../tests/test_web_agent.py#L2633) | 2633 | `""` | — |
| [SRC-F725E90B2A-L002634](../../tests/test_web_agent.py#L2634) | 2634 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L002635](../../tests/test_web_agent.py#L2635) | 2635 | `"        observed.append((url, kwargs.get(\"follow_redirects\")))"` | — |
| [SRC-F725E90B2A-L002636](../../tests/test_web_agent.py#L2636) | 2636 | `"        return RedirectResponse()"` | — |
| [SRC-F725E90B2A-L002637](../../tests/test_web_agent.py#L2637) | 2637 | `""` | — |
| [SRC-F725E90B2A-L002638](../../tests/test_web_agent.py#L2638) | 2638 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L002639](../../tests/test_web_agent.py#L2639) | 2639 | `"    method = getattr(agent, method_name)"` | — |
| [SRC-F725E90B2A-L002640](../../tests/test_web_agent.py#L2640) | 2640 | `"    with pytest.raises(RuntimeError, match=\"HTTP 302\"):"` | — |
| [SRC-F725E90B2A-L002641](../../tests/test_web_agent.py#L2641) | 2641 | `"        method(\"redirect regression test\")"` | — |
| [SRC-F725E90B2A-L002642](../../tests/test_web_agent.py#L2642) | 2642 | `""` | — |
| [SRC-F725E90B2A-L002643](../../tests/test_web_agent.py#L2643) | 2643 | `"    assert len(observed) == 1"` | — |
| [SRC-F725E90B2A-L002644](../../tests/test_web_agent.py#L2644) | 2644 | `"    assert observed[0][1] is False"` | — |
| [SRC-F725E90B2A-L002645](../../tests/test_web_agent.py#L2645) | 2645 | `""` | — |
| [SRC-F725E90B2A-L002646](../../tests/test_web_agent.py#L2646) | 2646 | `""` | — |
| [SRC-F725E90B2A-L002647](../../tests/test_web_agent.py#L2647) | 2647 | `""` | — |
| [SRC-F725E90B2A-L002648](../../tests/test_web_agent.py#L2648) | 2648 | `"@pytest.mark.parametrize(\"mode\", [\"deep\", \"latest\", \"social\"])"` | — |
| [SRC-F725E90B2A-L002649](../../tests/test_web_agent.py#L2649) | 2649 | `"def test_explicit_modes_survive_deterministic_planning(monkeypatch, mode):"` | — |
| [SRC-F725E90B2A-L002650](../../tests/test_web_agent.py#L2650) | 2650 | `"    \"\"\"A missing planner model must not erase a mode explicitly selected by the user.\"\"\""` | — |
| [SRC-F725E90B2A-L002651](../../tests/test_web_agent.py#L2651) | 2651 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002652](../../tests/test_web_agent.py#L2652) | 2652 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L002653](../../tests/test_web_agent.py#L2653) | 2653 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L002654](../../tests/test_web_agent.py#L2654) | 2654 | `""` | — |
| [SRC-F725E90B2A-L002655](../../tests/test_web_agent.py#L2655) | 2655 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L002656](../../tests/test_web_agent.py#L2656) | 2656 | `"        seen[\"plan\"] = dict(research_plan)"` | — |
| [SRC-F725E90B2A-L002657](../../tests/test_web_agent.py#L2657) | 2657 | `"        sources = [sample_source(0), sample_source(1)]"` | — |
| [SRC-F725E90B2A-L002658](../../tests/test_web_agent.py#L2658) | 2658 | `"        return sources, [], {"` | — |
| [SRC-F725E90B2A-L002659](../../tests/test_web_agent.py#L2659) | 2659 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002660](../../tests/test_web_agent.py#L2660) | 2660 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-F725E90B2A-L002661](../../tests/test_web_agent.py#L2661) | 2661 | `"            \"query_results\": ["` | — |
| [SRC-F725E90B2A-L002662](../../tests/test_web_agent.py#L2662) | 2662 | `"                {\"query\": query, \"results\": 1}"` | — |
| [SRC-F725E90B2A-L002663](../../tests/test_web_agent.py#L2663) | 2663 | `"                for query in research_plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L002664](../../tests/test_web_agent.py#L2664) | 2664 | `"            ],"` | — |
| [SRC-F725E90B2A-L002665](../../tests/test_web_agent.py#L2665) | 2665 | `"            \"unique_sources\": len(sources),"` | — |
| [SRC-F725E90B2A-L002666](../../tests/test_web_agent.py#L2666) | 2666 | `"            \"pages_fetched\": len(sources),"` | — |
| [SRC-F725E90B2A-L002667](../../tests/test_web_agent.py#L2667) | 2667 | `"            \"providers_used\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L002668](../../tests/test_web_agent.py#L2668) | 2668 | `"            \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-F725E90B2A-L002669](../../tests/test_web_agent.py#L2669) | 2669 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L002670](../../tests/test_web_agent.py#L2670) | 2670 | `"            \"depth\": research_plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-F725E90B2A-L002671](../../tests/test_web_agent.py#L2671) | 2671 | `"            \"planning_method\": \"deterministic_fallback\","` | — |
| [SRC-F725E90B2A-L002672](../../tests/test_web_agent.py#L2672) | 2672 | `"        }"` | — |
| [SRC-F725E90B2A-L002673](../../tests/test_web_agent.py#L2673) | 2673 | `""` | — |
| [SRC-F725E90B2A-L002674](../../tests/test_web_agent.py#L2674) | 2674 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L002675](../../tests/test_web_agent.py#L2675) | 2675 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, source: True)"` | — |
| [SRC-F725E90B2A-L002676](../../tests/test_web_agent.py#L2676) | 2676 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L002677](../../tests/test_web_agent.py#L2677) | 2677 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002678](../../tests/test_web_agent.py#L2678) | 2678 | `"        agent,"` | — |
| [SRC-F725E90B2A-L002679](../../tests/test_web_agent.py#L2679) | 2679 | `"        \"_generate\","` | — |
| [SRC-F725E90B2A-L002680](../../tests/test_web_agent.py#L2680) | 2680 | `"        lambda question, history, sources, search_warning, research_plan=None,"` | — |
| [SRC-F725E90B2A-L002681](../../tests/test_web_agent.py#L2681) | 2681 | `"               search_report=None: \"توجد نتائج أولية للمراجعة [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L002682](../../tests/test_web_agent.py#L2682) | 2682 | `"    )"` | — |
| [SRC-F725E90B2A-L002683](../../tests/test_web_agent.py#L2683) | 2683 | `""` | — |
| [SRC-F725E90B2A-L002684](../../tests/test_web_agent.py#L2684) | 2684 | `"    question = ("` | — |
| [SRC-F725E90B2A-L002685](../../tests/test_web_agent.py#L2685) | 2685 | `"        \"ابحث عن شقة في التجمع الخامس بسعر 5000000 جنيه\""` | — |
| [SRC-F725E90B2A-L002686](../../tests/test_web_agent.py#L2686) | 2686 | `"        if mode == \"deep\" else \"الطاقة المتجددة في مصر\""` | — |
| [SRC-F725E90B2A-L002687](../../tests/test_web_agent.py#L2687) | 2687 | `"    )"` | — |
| [SRC-F725E90B2A-L002688](../../tests/test_web_agent.py#L2688) | 2688 | `"    result = agent.answer(question, mode=mode)"` | — |
| [SRC-F725E90B2A-L002689](../../tests/test_web_agent.py#L2689) | 2689 | `"    plan = seen[\"plan\"]"` | — |
| [SRC-F725E90B2A-L002690](../../tests/test_web_agent.py#L2690) | 2690 | `""` | — |
| [SRC-F725E90B2A-L002691](../../tests/test_web_agent.py#L2691) | 2691 | `"    assert plan[\"mode\"] == mode"` | — |
| [SRC-F725E90B2A-L002692](../../tests/test_web_agent.py#L2692) | 2692 | `"    assert result[\"research_plan\"][\"mode\"] == mode"` | — |
| [SRC-F725E90B2A-L002693](../../tests/test_web_agent.py#L2693) | 2693 | `"    if mode == \"deep\":"` | — |
| [SRC-F725E90B2A-L002694](../../tests/test_web_agent.py#L2694) | 2694 | `"        assert plan[\"depth\"] == \"deep\""` | — |
| [SRC-F725E90B2A-L002695](../../tests/test_web_agent.py#L2695) | 2695 | `"        assert len(plan[\"queries\"]) >= 3"` | — |
| [SRC-F725E90B2A-L002696](../../tests/test_web_agent.py#L2696) | 2696 | `"        assert any(\"إعلانات عقارية\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002697](../../tests/test_web_agent.py#L2697) | 2697 | `"        assert any(\"متوسط أسعار السوق للمتر\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002698](../../tests/test_web_agent.py#L2698) | 2698 | `"    elif mode == \"latest\":"` | — |
| [SRC-F725E90B2A-L002699](../../tests/test_web_agent.py#L2699) | 2699 | `"        assert plan[\"freshness\"] == \"current\""` | — |
| [SRC-F725E90B2A-L002700](../../tests/test_web_agent.py#L2700) | 2700 | `"        assert any("` | — |
| [SRC-F725E90B2A-L002701](../../tests/test_web_agent.py#L2701) | 2701 | `"            \"latest\" in query.lower() or \"recent\" in query.lower()"` | — |
| [SRC-F725E90B2A-L002702](../../tests/test_web_agent.py#L2702) | 2702 | `"            for query in plan[\"queries\"]"` | — |
| [SRC-F725E90B2A-L002703](../../tests/test_web_agent.py#L2703) | 2703 | `"        )"` | — |
| [SRC-F725E90B2A-L002704](../../tests/test_web_agent.py#L2704) | 2704 | `"    else:"` | — |
| [SRC-F725E90B2A-L002705](../../tests/test_web_agent.py#L2705) | 2705 | `"        assert plan[\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L002706](../../tests/test_web_agent.py#L2706) | 2706 | `"        assert any(query.startswith(\"site:\") for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L002707](../../tests/test_web_agent.py#L2707) | 2707 | `""` | — |
| [SRC-F725E90B2A-L002708](../../tests/test_web_agent.py#L2708) | 2708 | `""` | — |
| [SRC-F725E90B2A-L002709](../../tests/test_web_agent.py#L2709) | 2709 | `"def test_web_answer_integrity_is_attached_without_live_network(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002710](../../tests/test_web_agent.py#L2710) | 2710 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002711](../../tests/test_web_agent.py#L2711) | 2711 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L002712](../../tests/test_web_agent.py#L2712) | 2712 | `"        agent, \"_question_coverage_targets\", lambda question: [\"السعر\", \"المساحة\"]"` | — |
| [SRC-F725E90B2A-L002713](../../tests/test_web_agent.py#L2713) | 2713 | `"    )"` | — |
| [SRC-F725E90B2A-L002714](../../tests/test_web_agent.py#L2714) | 2714 | `"    monkeypatch.setattr(agent, \"_answer_with_budget\", lambda question, history, mode: {"` | — |
| [SRC-F725E90B2A-L002715](../../tests/test_web_agent.py#L2715) | 2715 | `"        \"kind\": \"web_research\","` | — |
| [SRC-F725E90B2A-L002716](../../tests/test_web_agent.py#L2716) | 2716 | `"        \"answer\": \"السعر 500 جنيه [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L002717](../../tests/test_web_agent.py#L2717) | 2717 | `"        \"sources\": [{"` | — |
| [SRC-F725E90B2A-L002718](../../tests/test_web_agent.py#L2718) | 2718 | `"            \"title\": \"تفاصيل العرض\","` | — |
| [SRC-F725E90B2A-L002719](../../tests/test_web_agent.py#L2719) | 2719 | `"            \"url\": \"https://example.com/offer\","` | — |
| [SRC-F725E90B2A-L002720](../../tests/test_web_agent.py#L2720) | 2720 | `"            \"snippet\": \"السعر 300 جنيه\","` | — |
| [SRC-F725E90B2A-L002721](../../tests/test_web_agent.py#L2721) | 2721 | `"            \"page_fetched\": False,"` | — |
| [SRC-F725E90B2A-L002722](../../tests/test_web_agent.py#L2722) | 2722 | `"        }],"` | — |
| [SRC-F725E90B2A-L002723](../../tests/test_web_agent.py#L2723) | 2723 | `"        \"research_quality\": \"partial\","` | — |
| [SRC-F725E90B2A-L002724](../../tests/test_web_agent.py#L2724) | 2724 | `"        \"search_report\": {},"` | — |
| [SRC-F725E90B2A-L002725](../../tests/test_web_agent.py#L2725) | 2725 | `"        \"answer_coverage\": {},"` | — |
| [SRC-F725E90B2A-L002726](../../tests/test_web_agent.py#L2726) | 2726 | `"        \"used_language_model\": True,"` | — |
| [SRC-F725E90B2A-L002727](../../tests/test_web_agent.py#L2727) | 2727 | `"        \"used_web_search\": True,"` | — |
| [SRC-F725E90B2A-L002728](../../tests/test_web_agent.py#L2728) | 2728 | `"        \"warnings\": [],"` | — |
| [SRC-F725E90B2A-L002729](../../tests/test_web_agent.py#L2729) | 2729 | `"    })"` | — |
| [SRC-F725E90B2A-L002730](../../tests/test_web_agent.py#L2730) | 2730 | `""` | — |
| [SRC-F725E90B2A-L002731](../../tests/test_web_agent.py#L2731) | 2731 | `"    result = agent.answer(\"قارن السعر والمساحة\", mode=\"auto\")"` | — |
| [SRC-F725E90B2A-L002732](../../tests/test_web_agent.py#L2732) | 2732 | `""` | — |
| [SRC-F725E90B2A-L002733](../../tests/test_web_agent.py#L2733) | 2733 | `"    assert result[\"answer_integrity\"][\"semantic_verification\"] is False"` | — |
| [SRC-F725E90B2A-L002734](../../tests/test_web_agent.py#L2734) | 2734 | `"    assert result[\"answer_integrity\"][\"independent_fact_check\"] is False"` | — |
| [SRC-F725E90B2A-L002735](../../tests/test_web_agent.py#L2735) | 2735 | `"    assert result[\"answer_integrity\"][\"potentially_unsupported_numeric_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002736](../../tests/test_web_agent.py#L2736) | 2736 | `"    assert result[\"answer_integrity\"][\"potentially_unsupported_numeric_by_citation_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002737](../../tests/test_web_agent.py#L2737) | 2737 | `"    assert result[\"answer_integrity\"][\"potentially_missing_target_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002738](../../tests/test_web_agent.py#L2738) | 2738 | `"    assert result[\"task_fulfillment_status\"] == \"possible_gap_detected\""` | — |
| [SRC-F725E90B2A-L002739](../../tests/test_web_agent.py#L2739) | 2739 | `"    assert result[\"answer_coverage\"][\"lexical_screen_method\"] == ("` | — |
| [SRC-F725E90B2A-L002740](../../tests/test_web_agent.py#L2740) | 2740 | `"        \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-F725E90B2A-L002741](../../tests/test_web_agent.py#L2741) | 2741 | `"    )"` | — |
| [SRC-F725E90B2A-L002742](../../tests/test_web_agent.py#L2742) | 2742 | `""` | — |
| [SRC-F725E90B2A-L002743](../../tests/test_web_agent.py#L2743) | 2743 | `""` | — |
| [SRC-F725E90B2A-L002744](../../tests/test_web_agent.py#L2744) | 2744 | `"def test_frontend_labels_answer_integrity_screen_as_non_semantic():"` | — |
| [SRC-F725E90B2A-L002745](../../tests/test_web_agent.py#L2745) | 2745 | `"    html = ("` | — |
| [SRC-F725E90B2A-L002746](../../tests/test_web_agent.py#L2746) | 2746 | `"        Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\""` | — |
| [SRC-F725E90B2A-L002747](../../tests/test_web_agent.py#L2747) | 2747 | `"    ).read_text(encoding=\"utf-8\")"` | — |
| [SRC-F725E90B2A-L002748](../../tests/test_web_agent.py#L2748) | 2748 | `"    assert \"فحص لفظي أولي:\" in html"` | — |
| [SRC-F725E90B2A-L002749](../../tests/test_web_agent.py#L2749) | 2749 | `"    assert \"لا يثبت هذا الفحص صحة الوقائع أو دلالة الاستشهاد\" in html"` | — |
| [SRC-F725E90B2A-L002750](../../tests/test_web_agent.py#L2750) | 2750 | `"    assert \"potentially_unsupported_numeric_by_citation_count\" in html"` | — |
| [SRC-F725E90B2A-L002751](../../tests/test_web_agent.py#L2751) | 2751 | `"    assert \"potential_value_discrepancy_count\" in html"` | — |
| [SRC-F725E90B2A-L002752](../../tests/test_web_agent.py#L2752) | 2752 | `""` | — |
| [SRC-F725E90B2A-L002753](../../tests/test_web_agent.py#L2753) | 2753 | `""` | — |
| [SRC-F725E90B2A-L002754](../../tests/test_web_agent.py#L2754) | 2754 | `"def test_search_web_keeps_arabic_topic_matches_in_english_indexed_results(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002755](../../tests/test_web_agent.py#L2755) | 2755 | `"    cases = ["` | — |
| [SRC-F725E90B2A-L002756](../../tests/test_web_agent.py#L2756) | 2756 | `"        ("` | — |
| [SRC-F725E90B2A-L002757](../../tests/test_web_agent.py#L2757) | 2757 | `"            \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\","` | — |
| [SRC-F725E90B2A-L002758](../../tests/test_web_agent.py#L2758) | 2758 | `"            \"Egypt's capital is Cairo\","` | — |
| [SRC-F725E90B2A-L002759](../../tests/test_web_agent.py#L2759) | 2759 | `"            \"The capital city of Egypt is Cairo.\","` | — |
| [SRC-F725E90B2A-L002760](../../tests/test_web_agent.py#L2760) | 2760 | `"        ),"` | — |
| [SRC-F725E90B2A-L002761](../../tests/test_web_agent.py#L2761) | 2761 | `"        ("` | — |
| [SRC-F725E90B2A-L002762](../../tests/test_web_agent.py#L2762) | 2762 | `"            \"حلل أهم التحديات التي تواجه السيارات الكهربائية في مصر، وقارن بين التكلفة والبنية التحتية والشحن. استخدم مصادر متعددة، وميز بين الحقائق والاستنتاجات، واذكر روابط المصادر.\","` | — |
| [SRC-F725E90B2A-L002763](../../tests/test_web_agent.py#L2763) | 2763 | `"            \"Electric vehicles in Egypt: charging infrastructure and costs\","` | — |
| [SRC-F725E90B2A-L002764](../../tests/test_web_agent.py#L2764) | 2764 | `"            \"Electric cars face high costs and limited charging infrastructure in Egypt.\","` | — |
| [SRC-F725E90B2A-L002765](../../tests/test_web_agent.py#L2765) | 2765 | `"        ),"` | — |
| [SRC-F725E90B2A-L002766](../../tests/test_web_agent.py#L2766) | 2766 | `"        ("` | — |
| [SRC-F725E90B2A-L002767](../../tests/test_web_agent.py#L2767) | 2767 | `"            \"ما أحدث التطورات في وكلاء الذكاء الاصطناعي خلال الأيام السبعة الماضية؟ اذكر تواريخ الأخبار وروابط المصادر، ولا تعرض معلومات قديمة باعتبارها جديدة.\","` | — |
| [SRC-F725E90B2A-L002768](../../tests/test_web_agent.py#L2768) | 2768 | `"            \"Recent developments in AI agents\","` | — |
| [SRC-F725E90B2A-L002769](../../tests/test_web_agent.py#L2769) | 2769 | `"            \"New AI agent tools and launches this week.\","` | — |
| [SRC-F725E90B2A-L002770](../../tests/test_web_agent.py#L2770) | 2770 | `"        ),"` | — |
| [SRC-F725E90B2A-L002771](../../tests/test_web_agent.py#L2771) | 2771 | `"        ("` | — |
| [SRC-F725E90B2A-L002772](../../tests/test_web_agent.py#L2772) | 2772 | `"            \"اجمع آراء وتجارب المستخدمين العامة حول السيارات الكهربائية في مصر. اعرض الآراء الإيجابية والسلبية، واذكر روابط المنشورات أو المصادر المتاحة.\","` | — |
| [SRC-F725E90B2A-L002773](../../tests/test_web_agent.py#L2773) | 2773 | `"            \"Reddit users share electric car experiences in Egypt\","` | — |
| [SRC-F725E90B2A-L002774](../../tests/test_web_agent.py#L2774) | 2774 | `"            \"Owners discuss electric vehicles, charging and daily use.\","` | — |
| [SRC-F725E90B2A-L002775](../../tests/test_web_agent.py#L2775) | 2775 | `"        ),"` | — |
| [SRC-F725E90B2A-L002776](../../tests/test_web_agent.py#L2776) | 2776 | `"    ]"` | — |
| [SRC-F725E90B2A-L002777](../../tests/test_web_agent.py#L2777) | 2777 | `"    for index, (query, title, snippet) in enumerate(cases):"` | — |
| [SRC-F725E90B2A-L002778](../../tests/test_web_agent.py#L2778) | 2778 | `"        agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002779](../../tests/test_web_agent.py#L2779) | 2779 | `"        row = {"` | — |
| [SRC-F725E90B2A-L002780](../../tests/test_web_agent.py#L2780) | 2780 | `"            \"title\": title,"` | — |
| [SRC-F725E90B2A-L002781](../../tests/test_web_agent.py#L2781) | 2781 | `"            \"url\": f\"https://example.com/case-{index}\","` | — |
| [SRC-F725E90B2A-L002782](../../tests/test_web_agent.py#L2782) | 2782 | `"            \"snippet\": snippet,"` | — |
| [SRC-F725E90B2A-L002783](../../tests/test_web_agent.py#L2783) | 2783 | `"            \"provider\": \"fake_provider\","` | — |
| [SRC-F725E90B2A-L002784](../../tests/test_web_agent.py#L2784) | 2784 | `"            \"provider_rank\": 1,"` | — |
| [SRC-F725E90B2A-L002785](../../tests/test_web_agent.py#L2785) | 2785 | `"            \"search_query\": query,"` | — |
| [SRC-F725E90B2A-L002786](../../tests/test_web_agent.py#L2786) | 2786 | `"        }"` | — |
| [SRC-F725E90B2A-L002787](../../tests/test_web_agent.py#L2787) | 2787 | `"        monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _q, row=row: [dict(row)])"` | — |
| [SRC-F725E90B2A-L002788](../../tests/test_web_agent.py#L2788) | 2788 | `"        monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _q, row=row: [dict(row)])"` | — |
| [SRC-F725E90B2A-L002789](../../tests/test_web_agent.py#L2789) | 2789 | `"        # Current-news questions normally add Google News RSS; keep this unit test deterministic."` | — |
| [SRC-F725E90B2A-L002790](../../tests/test_web_agent.py#L2790) | 2790 | `"        monkeypatch.setattr(agent, \"_search_news\", lambda _q: [])"` | — |
| [SRC-F725E90B2A-L002791](../../tests/test_web_agent.py#L2791) | 2791 | `"        results = agent._search_web(query)"` | — |
| [SRC-F725E90B2A-L002792](../../tests/test_web_agent.py#L2792) | 2792 | `"        assert results, f\"Search candidates were all filtered for case {index}\""` | — |
| [SRC-F725E90B2A-L002793](../../tests/test_web_agent.py#L2793) | 2793 | `"        diagnostic = next("` | — |
| [SRC-F725E90B2A-L002794](../../tests/test_web_agent.py#L2794) | 2794 | `"            item for item in agent._provider_diagnostics if item.get(\"provider\") == \"duckduckgo_html\""` | — |
| [SRC-F725E90B2A-L002795](../../tests/test_web_agent.py#L2795) | 2795 | `"        )"` | — |
| [SRC-F725E90B2A-L002796](../../tests/test_web_agent.py#L2796) | 2796 | `"        assert diagnostic[\"accepted_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002797](../../tests/test_web_agent.py#L2797) | 2797 | `"        assert diagnostic[\"result_count\"] == 1"` | — |
| [SRC-F725E90B2A-L002798](../../tests/test_web_agent.py#L2798) | 2798 | `""` | — |
| [SRC-F725E90B2A-L002799](../../tests/test_web_agent.py#L2799) | 2799 | `""` | — |
| [SRC-F725E90B2A-L002800](../../tests/test_web_agent.py#L2800) | 2800 | `"def test_search_web_classifies_http_challenge_and_rate_limit_as_provider_degradation(monkeypatch):"` | — |
| [SRC-F725E90B2A-L002801](../../tests/test_web_agent.py#L2801) | 2801 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L002802](../../tests/test_web_agent.py#L2802) | 2802 | `""` | — |
| [SRC-F725E90B2A-L002803](../../tests/test_web_agent.py#L2803) | 2803 | `"    def http_202(_query):"` | — |
| [SRC-F725E90B2A-L002804](../../tests/test_web_agent.py#L2804) | 2804 | `"        raise RuntimeError(\"HTTP 202\")"` | — |
| [SRC-F725E90B2A-L002805](../../tests/test_web_agent.py#L2805) | 2805 | `""` | — |
| [SRC-F725E90B2A-L002806](../../tests/test_web_agent.py#L2806) | 2806 | `"    def http_429(_query):"` | — |
| [SRC-F725E90B2A-L002807](../../tests/test_web_agent.py#L2807) | 2807 | `"        raise RuntimeError(\"HTTP 429\")"` | — |
| [SRC-F725E90B2A-L002808](../../tests/test_web_agent.py#L2808) | 2808 | `""` | — |
| [SRC-F725E90B2A-L002809](../../tests/test_web_agent.py#L2809) | 2809 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", http_202)"` | — |
| [SRC-F725E90B2A-L002810](../../tests/test_web_agent.py#L2810) | 2810 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", http_429)"` | — |
| [SRC-F725E90B2A-L002811](../../tests/test_web_agent.py#L2811) | 2811 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-F725E90B2A-L002812](../../tests/test_web_agent.py#L2812) | 2812 | `"        agent._search_web(\"renewable energy storage policy\")"` | — |
| [SRC-F725E90B2A-L002813](../../tests/test_web_agent.py#L2813) | 2813 | `""` | — |
| [SRC-F725E90B2A-L002814](../../tests/test_web_agent.py#L2814) | 2814 | `"    statuses = {"` | — |
| [SRC-F725E90B2A-L002815](../../tests/test_web_agent.py#L2815) | 2815 | `"        item[\"provider\"]: item[\"status\"]"` | — |
| [SRC-F725E90B2A-L002816](../../tests/test_web_agent.py#L2816) | 2816 | `"        for item in agent._provider_diagnostics"` | — |
| [SRC-F725E90B2A-L002817](../../tests/test_web_agent.py#L2817) | 2817 | `"        if item[\"provider\"] in {\"duckduckgo_html\", \"bing_rss\"}"` | — |
| [SRC-F725E90B2A-L002818](../../tests/test_web_agent.py#L2818) | 2818 | `"    }"` | — |
| [SRC-F725E90B2A-L002819](../../tests/test_web_agent.py#L2819) | 2819 | `"    assert statuses[\"duckduckgo_html\"] == \"http_error\""` | — |
| [SRC-F725E90B2A-L002820](../../tests/test_web_agent.py#L2820) | 2820 | `"    assert statuses[\"bing_rss\"] == \"rate_limited\""` | — |
| [SRC-F725E90B2A-L002821](../../tests/test_web_agent.py#L2821) | 2821 | `""` | — |
| [SRC-F725E90B2A-L002822](../../tests/test_web_agent.py#L2822) | 2822 | `""` | — |
