# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **046**
- سجلات الأسطر: **800**
- النطاق: SRC-6B37B7D6D3-L000077 إلى SRC-29A9CD43D1-L000039
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-6B37B7D6D3 — [tests/test_claim_evidence_metadata.py](../../tests/test_claim_evidence_metadata.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6B37B7D6D3-L000077](../../tests/test_claim_evidence_metadata.py#L77) | 77 | `"    assert audit[\"population_scope_required\"] is True"` | — |
| [SRC-6B37B7D6D3-L000078](../../tests/test_claim_evidence_metadata.py#L78) | 78 | `"    assert \"data_reference_period_for_population_claim\" in audit[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000079](../../tests/test_claim_evidence_metadata.py#L79) | 79 | `"    assert \"geographic_scope_for_population_claim\" in audit[\"required_fields_missing\"]"` | — |
| [SRC-6B37B7D6D3-L000080](../../tests/test_claim_evidence_metadata.py#L80) | 80 | `"    assert ledger[\"fact_correctness\"] == \"not_checked\""` | — |
## اختبارات

### FILE-DA61479D59 — [tests/test_connector_summary_counters.py](../../tests/test_connector_summary_counters.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-DA61479D59-L000001](../../tests/test_connector_summary_counters.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-DA61479D59-L000002](../../tests/test_connector_summary_counters.py#L2) | 2 | `""` | — |
| [SRC-DA61479D59-L000003](../../tests/test_connector_summary_counters.py#L3) | 3 | `"import json"` | — |
| [SRC-DA61479D59-L000004](../../tests/test_connector_summary_counters.py#L4) | 4 | `""` | — |
| [SRC-DA61479D59-L000005](../../tests/test_connector_summary_counters.py#L5) | 5 | `"from agents.web_agent import PageFetchResult, WebAgent"` | — |
| [SRC-DA61479D59-L000006](../../tests/test_connector_summary_counters.py#L6) | 6 | `""` | — |
| [SRC-DA61479D59-L000007](../../tests/test_connector_summary_counters.py#L7) | 7 | `""` | — |
| [SRC-DA61479D59-L000008](../../tests/test_connector_summary_counters.py#L8) | 8 | `"def test_connector_summary_reports_request_scope_worst_state_and_redacts_secrets(monkeypatch):"` | — |
| [SRC-DA61479D59-L000009](../../tests/test_connector_summary_counters.py#L9) | 9 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000010](../../tests/test_connector_summary_counters.py#L10) | 10 | `"    monkeypatch.delenv(\"BRAVE_SEARCH_API_KEY\", raising=False)"` | — |
| [SRC-DA61479D59-L000011](../../tests/test_connector_summary_counters.py#L11) | 11 | `"    diagnostics = ["` | — |
| [SRC-DA61479D59-L000012](../../tests/test_connector_summary_counters.py#L12) | 12 | `"        {"` | — |
| [SRC-DA61479D59-L000013](../../tests/test_connector_summary_counters.py#L13) | 13 | `"            \"provider\": \"duckduckgo_html\","` | — |
| [SRC-DA61479D59-L000014](../../tests/test_connector_summary_counters.py#L14) | 14 | `"            \"query\": \"renewable energy\","` | — |
| [SRC-DA61479D59-L000015](../../tests/test_connector_summary_counters.py#L15) | 15 | `"            \"status\": \"ok\","` | — |
| [SRC-DA61479D59-L000016](../../tests/test_connector_summary_counters.py#L16) | 16 | `"            \"result_count\": 3,"` | — |
| [SRC-DA61479D59-L000017](../../tests/test_connector_summary_counters.py#L17) | 17 | `"            \"rejected_count\": 1,"` | — |
| [SRC-DA61479D59-L000018](../../tests/test_connector_summary_counters.py#L18) | 18 | `"        },"` | — |
| [SRC-DA61479D59-L000019](../../tests/test_connector_summary_counters.py#L19) | 19 | `"        {"` | — |
| [SRC-DA61479D59-L000020](../../tests/test_connector_summary_counters.py#L20) | 20 | `"            \"provider\": \"duckduckgo_html\","` | — |
| [SRC-DA61479D59-L000021](../../tests/test_connector_summary_counters.py#L21) | 21 | `"            \"query\": \"renewable energy\","` | — |
| [SRC-DA61479D59-L000022](../../tests/test_connector_summary_counters.py#L22) | 22 | `"            \"status\": \"failed\","` | — |
| [SRC-DA61479D59-L000023](../../tests/test_connector_summary_counters.py#L23) | 23 | `"            \"result_count\": 0,"` | — |
| [SRC-DA61479D59-L000024](../../tests/test_connector_summary_counters.py#L24) | 24 | `"            \"rejected_count\": 0,"` | — |
| [SRC-DA61479D59-L000025](../../tests/test_connector_summary_counters.py#L25) | 25 | `"            \"error\": \"HTTP 500 token=secret-value\","` | — |
| [SRC-DA61479D59-L000026](../../tests/test_connector_summary_counters.py#L26) | 26 | `"        },"` | — |
| [SRC-DA61479D59-L000027](../../tests/test_connector_summary_counters.py#L27) | 27 | `"    ]"` | — |
| [SRC-DA61479D59-L000028](../../tests/test_connector_summary_counters.py#L28) | 28 | `"    sources = ["` | — |
| [SRC-DA61479D59-L000029](../../tests/test_connector_summary_counters.py#L29) | 29 | `"        {\"url\": \"https://example.com/a\", \"providers\": [\"duckduckgo_html\"]},"` | — |
| [SRC-DA61479D59-L000030](../../tests/test_connector_summary_counters.py#L30) | 30 | `"        {\"url\": \"https://example.org/b\", \"providers\": [\"bing_rss\"]},"` | — |
| [SRC-DA61479D59-L000031](../../tests/test_connector_summary_counters.py#L31) | 31 | `"    ]"` | — |
| [SRC-DA61479D59-L000032](../../tests/test_connector_summary_counters.py#L32) | 32 | `""` | — |
| [SRC-DA61479D59-L000033](../../tests/test_connector_summary_counters.py#L33) | 33 | `"    summary = agent._connector_status_summary(diagnostics, sources)"` | — |
| [SRC-DA61479D59-L000034](../../tests/test_connector_summary_counters.py#L34) | 34 | `""` | — |
| [SRC-DA61479D59-L000035](../../tests/test_connector_summary_counters.py#L35) | 35 | `"    duckduckgo = next(item for item in summary[\"connectors\"] if item[\"name\"] == \"duckduckgo_html\")"` | — |
| [SRC-DA61479D59-L000036](../../tests/test_connector_summary_counters.py#L36) | 36 | `"    brave = next(item for item in summary[\"connectors\"] if item[\"name\"] == \"brave_search_api\")"` | — |
| [SRC-DA61479D59-L000037](../../tests/test_connector_summary_counters.py#L37) | 37 | `"    assert summary[\"scope\"] == \"this_request_only\""` | — |
| [SRC-DA61479D59-L000038](../../tests/test_connector_summary_counters.py#L38) | 38 | `"    assert duckduckgo[\"attempted\"] is True"` | — |
| [SRC-DA61479D59-L000039](../../tests/test_connector_summary_counters.py#L39) | 39 | `"    assert duckduckgo[\"status\"] == \"failed\""` | — |
| [SRC-DA61479D59-L000040](../../tests/test_connector_summary_counters.py#L40) | 40 | `"    assert duckduckgo[\"observed_statuses\"] == [\"ok\", \"failed\"]"` | — |
| [SRC-DA61479D59-L000041](../../tests/test_connector_summary_counters.py#L41) | 41 | `"    assert duckduckgo[\"result_count\"] == 3"` | — |
| [SRC-DA61479D59-L000042](../../tests/test_connector_summary_counters.py#L42) | 42 | `"    assert duckduckgo[\"useful_result_count\"] == 1"` | — |
| [SRC-DA61479D59-L000043](../../tests/test_connector_summary_counters.py#L43) | 43 | `"    assert duckduckgo[\"rejected_count\"] == 1"` | — |
| [SRC-DA61479D59-L000044](../../tests/test_connector_summary_counters.py#L44) | 44 | `"    assert duckduckgo[\"implementation_status\"] == \"implemented_in_code\""` | — |
| [SRC-DA61479D59-L000045](../../tests/test_connector_summary_counters.py#L45) | 45 | `"    assert duckduckgo[\"available_for_this_request\"] is True"` | — |
| [SRC-DA61479D59-L000046](../../tests/test_connector_summary_counters.py#L46) | 46 | `"    assert duckduckgo[\"verified_for_this_request\"] is True"` | — |
| [SRC-DA61479D59-L000047](../../tests/test_connector_summary_counters.py#L47) | 47 | `"    assert duckduckgo[\"failure_observed\"] is True"` | — |
| [SRC-DA61479D59-L000048](../../tests/test_connector_summary_counters.py#L48) | 48 | `"    assert \"secret-value\" not in json.dumps(summary)"` | — |
| [SRC-DA61479D59-L000049](../../tests/test_connector_summary_counters.py#L49) | 49 | `"    assert brave[\"configured\"] is False"` | — |
| [SRC-DA61479D59-L000050](../../tests/test_connector_summary_counters.py#L50) | 50 | `"    assert brave[\"status\"] == \"not_configured\""` | — |
| [SRC-DA61479D59-L000051](../../tests/test_connector_summary_counters.py#L51) | 51 | `"    assert brave[\"available_for_this_request\"] is False"` | — |
| [SRC-DA61479D59-L000052](../../tests/test_connector_summary_counters.py#L52) | 52 | `"    assert brave[\"verified_for_this_request\"] is None"` | — |
| [SRC-DA61479D59-L000053](../../tests/test_connector_summary_counters.py#L53) | 53 | `""` | — |
| [SRC-DA61479D59-L000054](../../tests/test_connector_summary_counters.py#L54) | 54 | `""` | — |
| [SRC-DA61479D59-L000055](../../tests/test_connector_summary_counters.py#L55) | 55 | `"def test_collect_research_distinguishes_raw_rows_unique_urls_and_page_extraction(monkeypatch):"` | — |
| [SRC-DA61479D59-L000056](../../tests/test_connector_summary_counters.py#L56) | 56 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000057](../../tests/test_connector_summary_counters.py#L57) | 57 | `"    query = \"renewable energy storage\""` | — |
| [SRC-DA61479D59-L000058](../../tests/test_connector_summary_counters.py#L58) | 58 | `"    results = ["` | — |
| [SRC-DA61479D59-L000059](../../tests/test_connector_summary_counters.py#L59) | 59 | `"        {"` | — |
| [SRC-DA61479D59-L000060](../../tests/test_connector_summary_counters.py#L60) | 60 | `"            \"title\": \"Renewable energy storage report\","` | — |
| [SRC-DA61479D59-L000061](../../tests/test_connector_summary_counters.py#L61) | 61 | `"            \"url\": \"https://example.com/report\","` | — |
| [SRC-DA61479D59-L000062](../../tests/test_connector_summary_counters.py#L62) | 62 | `"            \"snippet\": \"Renewable energy storage data from the report\","` | — |
| [SRC-DA61479D59-L000063](../../tests/test_connector_summary_counters.py#L63) | 63 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000064](../../tests/test_connector_summary_counters.py#L64) | 64 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000065](../../tests/test_connector_summary_counters.py#L65) | 65 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000066](../../tests/test_connector_summary_counters.py#L66) | 66 | `"            \"provider_rank\": 1,"` | — |
| [SRC-DA61479D59-L000067](../../tests/test_connector_summary_counters.py#L67) | 67 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000068](../../tests/test_connector_summary_counters.py#L68) | 68 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000069](../../tests/test_connector_summary_counters.py#L69) | 69 | `"        },"` | — |
| [SRC-DA61479D59-L000070](../../tests/test_connector_summary_counters.py#L70) | 70 | `"        {"` | — |
| [SRC-DA61479D59-L000071](../../tests/test_connector_summary_counters.py#L71) | 71 | `"            \"title\": \"Renewable energy storage report (duplicate URL)\","` | — |
| [SRC-DA61479D59-L000072](../../tests/test_connector_summary_counters.py#L72) | 72 | `"            \"url\": \"https://example.com/report?utm_source=test\","` | — |
| [SRC-DA61479D59-L000073](../../tests/test_connector_summary_counters.py#L73) | 73 | `"            \"snippet\": \"Renewable energy storage data from a duplicate result\","` | — |
| [SRC-DA61479D59-L000074](../../tests/test_connector_summary_counters.py#L74) | 74 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000075](../../tests/test_connector_summary_counters.py#L75) | 75 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000076](../../tests/test_connector_summary_counters.py#L76) | 76 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000077](../../tests/test_connector_summary_counters.py#L77) | 77 | `"            \"provider_rank\": 2,"` | — |
| [SRC-DA61479D59-L000078](../../tests/test_connector_summary_counters.py#L78) | 78 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000079](../../tests/test_connector_summary_counters.py#L79) | 79 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000080](../../tests/test_connector_summary_counters.py#L80) | 80 | `"        },"` | — |
| [SRC-DA61479D59-L000081](../../tests/test_connector_summary_counters.py#L81) | 81 | `"        {"` | — |
| [SRC-DA61479D59-L000082](../../tests/test_connector_summary_counters.py#L82) | 82 | `"            \"title\": \"Renewable energy storage statistics\","` | — |
| [SRC-DA61479D59-L000083](../../tests/test_connector_summary_counters.py#L83) | 83 | `"            \"url\": \"https://example.org/statistics\","` | — |
| [SRC-DA61479D59-L000084](../../tests/test_connector_summary_counters.py#L84) | 84 | `"            \"snippet\": \"Renewable energy storage statistics\","` | — |
| [SRC-DA61479D59-L000085](../../tests/test_connector_summary_counters.py#L85) | 85 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000086](../../tests/test_connector_summary_counters.py#L86) | 86 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000087](../../tests/test_connector_summary_counters.py#L87) | 87 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000088](../../tests/test_connector_summary_counters.py#L88) | 88 | `"            \"provider_rank\": 3,"` | — |
| [SRC-DA61479D59-L000089](../../tests/test_connector_summary_counters.py#L89) | 89 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000090](../../tests/test_connector_summary_counters.py#L90) | 90 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000091](../../tests/test_connector_summary_counters.py#L91) | 91 | `"        },"` | — |
| [SRC-DA61479D59-L000092](../../tests/test_connector_summary_counters.py#L92) | 92 | `"    ]"` | — |
| [SRC-DA61479D59-L000093](../../tests/test_connector_summary_counters.py#L93) | 93 | `""` | — |
| [SRC-DA61479D59-L000094](../../tests/test_connector_summary_counters.py#L94) | 94 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda _query: results)"` | — |
| [SRC-DA61479D59-L000095](../../tests/test_connector_summary_counters.py#L95) | 95 | `"    def fetch(url: str):"` | — |
| [SRC-DA61479D59-L000096](../../tests/test_connector_summary_counters.py#L96) | 96 | `"        if \"example.com\" in url:"` | — |
| [SRC-DA61479D59-L000097](../../tests/test_connector_summary_counters.py#L97) | 97 | `"            return \"Report page\", \"Renewable energy storage page body with extracted text.\""` | — |
| [SRC-DA61479D59-L000098](../../tests/test_connector_summary_counters.py#L98) | 98 | `"        return \"\", \"\""` | — |
| [SRC-DA61479D59-L000099](../../tests/test_connector_summary_counters.py#L99) | 99 | `""` | — |
| [SRC-DA61479D59-L000100](../../tests/test_connector_summary_counters.py#L100) | 100 | `"    monkeypatch.setattr(agent, \"_fetch_page\", fetch)"` | — |
| [SRC-DA61479D59-L000101](../../tests/test_connector_summary_counters.py#L101) | 101 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-DA61479D59-L000102](../../tests/test_connector_summary_counters.py#L102) | 102 | `"        \"queries\": [query],"` | — |
| [SRC-DA61479D59-L000103](../../tests/test_connector_summary_counters.py#L103) | 103 | `"        \"direct_urls\": [],"` | — |
| [SRC-DA61479D59-L000104](../../tests/test_connector_summary_counters.py#L104) | 104 | `"        \"social_focus\": False,"` | — |
| [SRC-DA61479D59-L000105](../../tests/test_connector_summary_counters.py#L105) | 105 | `"        \"freshness\": \"any\","` | — |
| [SRC-DA61479D59-L000106](../../tests/test_connector_summary_counters.py#L106) | 106 | `"        \"depth\": \"standard\","` | — |
| [SRC-DA61479D59-L000107](../../tests/test_connector_summary_counters.py#L107) | 107 | `"        \"platforms\": [],"` | — |
| [SRC-DA61479D59-L000108](../../tests/test_connector_summary_counters.py#L108) | 108 | `"        \"planning_method\": \"unit_test\","` | — |
| [SRC-DA61479D59-L000109](../../tests/test_connector_summary_counters.py#L109) | 109 | `"    })"` | — |
| [SRC-DA61479D59-L000110](../../tests/test_connector_summary_counters.py#L110) | 110 | `""` | — |
| [SRC-DA61479D59-L000111](../../tests/test_connector_summary_counters.py#L111) | 111 | `"    assert warnings"` | — |
| [SRC-DA61479D59-L000112](../../tests/test_connector_summary_counters.py#L112) | 112 | `"    assert report[\"raw_results\"] == 3"` | — |
| [SRC-DA61479D59-L000113](../../tests/test_connector_summary_counters.py#L113) | 113 | `"    assert report[\"unique_urls\"] == 2"` | — |
| [SRC-DA61479D59-L000114](../../tests/test_connector_summary_counters.py#L114) | 114 | `"    assert report[\"unique_sources\"] == 2"` | — |
| [SRC-DA61479D59-L000115](../../tests/test_connector_summary_counters.py#L115) | 115 | `"    assert report[\"pages_fetch_attempted\"] == 2"` | — |
| [SRC-DA61479D59-L000116](../../tests/test_connector_summary_counters.py#L116) | 116 | `"    assert report[\"pages_content_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000117](../../tests/test_connector_summary_counters.py#L117) | 117 | `"    assert report[\"pages_extract_failed\"] == 1"` | — |
| [SRC-DA61479D59-L000118](../../tests/test_connector_summary_counters.py#L118) | 118 | `"    assert report[\"page_fetch_status_counts\"][\"content_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000119](../../tests/test_connector_summary_counters.py#L119) | 119 | `"    assert report[\"page_fetch_status_counts\"][\"no_text_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000120](../../tests/test_connector_summary_counters.py#L120) | 120 | `"    assert report[\"page_fetch_status_counts\"][\"fetch_failed\"] == 0"` | — |
| [SRC-DA61479D59-L000121](../../tests/test_connector_summary_counters.py#L121) | 121 | `"    assert report[\"page_fetch_status_counts\"][\"partial_extraction\"] == 0"` | — |
| [SRC-DA61479D59-L000122](../../tests/test_connector_summary_counters.py#L122) | 122 | `"    assert report[\"pages_partial_extracted\"] == 0"` | — |
| [SRC-DA61479D59-L000123](../../tests/test_connector_summary_counters.py#L123) | 123 | `"    assert sum(source[\"page_fetch_status\"] == \"content_extracted\" for source in sources) == 1"` | — |
| [SRC-DA61479D59-L000124](../../tests/test_connector_summary_counters.py#L124) | 124 | `"    assert sum(source[\"page_fetch_status\"] == \"no_text_extracted\" for source in sources) == 1"` | — |
| [SRC-DA61479D59-L000125](../../tests/test_connector_summary_counters.py#L125) | 125 | `"    assert report[\"connector_summary\"][\"scope\"] == \"this_request_only\""` | — |
| [SRC-DA61479D59-L000126](../../tests/test_connector_summary_counters.py#L126) | 126 | `""` | — |
| [SRC-DA61479D59-L000127](../../tests/test_connector_summary_counters.py#L127) | 127 | `""` | — |
| [SRC-DA61479D59-L000128](../../tests/test_connector_summary_counters.py#L128) | 128 | `"def test_connector_summary_does_not_claim_timeout_or_budget_exhaustion_was_a_confirmed_attempt(monkeypatch):"` | — |
| [SRC-DA61479D59-L000129](../../tests/test_connector_summary_counters.py#L129) | 129 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000130](../../tests/test_connector_summary_counters.py#L130) | 130 | `"    monkeypatch.setenv(\"TAVILY_API_KEY\", \"configured-test-key\")"` | — |
| [SRC-DA61479D59-L000131](../../tests/test_connector_summary_counters.py#L131) | 131 | `"    monkeypatch.setenv(\"DEEPSEEK_SEARCH_API_KEY\", \"configured-test-key\")"` | — |
| [SRC-DA61479D59-L000132](../../tests/test_connector_summary_counters.py#L132) | 132 | `"    timeout = agent._connector_status_summary("` | — |
| [SRC-DA61479D59-L000133](../../tests/test_connector_summary_counters.py#L133) | 133 | `"        [{\"provider\": \"tavily_search_api\", \"query\": \"query\", \"status\": \"timeout\", \"error\": \"request timed out\"}],"` | — |
| [SRC-DA61479D59-L000134](../../tests/test_connector_summary_counters.py#L134) | 134 | `"        [],"` | — |
| [SRC-DA61479D59-L000135](../../tests/test_connector_summary_counters.py#L135) | 135 | `"    )"` | — |
| [SRC-DA61479D59-L000136](../../tests/test_connector_summary_counters.py#L136) | 136 | `"    exhausted = agent._connector_status_summary("` | — |
| [SRC-DA61479D59-L000137](../../tests/test_connector_summary_counters.py#L137) | 137 | `"        [{\"provider\": \"deepseek_search_api\", \"query\": \"query\", \"status\": \"budget_exhausted\"}],"` | — |
| [SRC-DA61479D59-L000138](../../tests/test_connector_summary_counters.py#L138) | 138 | `"        [],"` | — |
| [SRC-DA61479D59-L000139](../../tests/test_connector_summary_counters.py#L139) | 139 | `"    )"` | — |
| [SRC-DA61479D59-L000140](../../tests/test_connector_summary_counters.py#L140) | 140 | `"    tavily = next(item for item in timeout[\"connectors\"] if item[\"name\"] == \"tavily_search_api\")"` | — |
| [SRC-DA61479D59-L000141](../../tests/test_connector_summary_counters.py#L141) | 141 | `"    deepseek = next(item for item in exhausted[\"connectors\"] if item[\"name\"] == \"deepseek_search_api\")"` | — |
| [SRC-DA61479D59-L000142](../../tests/test_connector_summary_counters.py#L142) | 142 | `"    assert tavily[\"configured\"] is True"` | — |
| [SRC-DA61479D59-L000143](../../tests/test_connector_summary_counters.py#L143) | 143 | `"    assert tavily[\"attempted\"] is None"` | — |
| [SRC-DA61479D59-L000144](../../tests/test_connector_summary_counters.py#L144) | 144 | `"    assert tavily[\"status\"] == \"timeout\""` | — |
| [SRC-DA61479D59-L000145](../../tests/test_connector_summary_counters.py#L145) | 145 | `"    assert tavily[\"available_for_this_request\"] is None"` | — |
| [SRC-DA61479D59-L000146](../../tests/test_connector_summary_counters.py#L146) | 146 | `"    assert tavily[\"verified_for_this_request\"] is None"` | — |
| [SRC-DA61479D59-L000147](../../tests/test_connector_summary_counters.py#L147) | 147 | `"    assert tavily[\"failure_observed\"] is True"` | — |
| [SRC-DA61479D59-L000148](../../tests/test_connector_summary_counters.py#L148) | 148 | `"    assert deepseek[\"configured\"] is True"` | — |
| [SRC-DA61479D59-L000149](../../tests/test_connector_summary_counters.py#L149) | 149 | `"    assert deepseek[\"attempted\"] is False"` | — |
| [SRC-DA61479D59-L000150](../../tests/test_connector_summary_counters.py#L150) | 150 | `"    assert deepseek[\"status\"] == \"budget_exhausted\""` | — |
| [SRC-DA61479D59-L000151](../../tests/test_connector_summary_counters.py#L151) | 151 | `"    assert deepseek[\"available_for_this_request\"] is False"` | — |
| [SRC-DA61479D59-L000152](../../tests/test_connector_summary_counters.py#L152) | 152 | `"    assert deepseek[\"verified_for_this_request\"] is None"` | — |
| [SRC-DA61479D59-L000153](../../tests/test_connector_summary_counters.py#L153) | 153 | `""` | — |
| [SRC-DA61479D59-L000154](../../tests/test_connector_summary_counters.py#L154) | 154 | `""` | — |
| [SRC-DA61479D59-L000155](../../tests/test_connector_summary_counters.py#L155) | 155 | `"def test_collect_research_preserves_partial_and_http_failure_page_statuses(monkeypatch):"` | — |
| [SRC-DA61479D59-L000156](../../tests/test_connector_summary_counters.py#L156) | 156 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000157](../../tests/test_connector_summary_counters.py#L157) | 157 | `"    query = \"renewable energy storage\""` | — |
| [SRC-DA61479D59-L000158](../../tests/test_connector_summary_counters.py#L158) | 158 | `"    results = ["` | — |
| [SRC-DA61479D59-L000159](../../tests/test_connector_summary_counters.py#L159) | 159 | `"        {"` | — |
| [SRC-DA61479D59-L000160](../../tests/test_connector_summary_counters.py#L160) | 160 | `"            \"title\": \"Renewable energy storage report\","` | — |
| [SRC-DA61479D59-L000161](../../tests/test_connector_summary_counters.py#L161) | 161 | `"            \"url\": \"https://example.com/report\","` | — |
| [SRC-DA61479D59-L000162](../../tests/test_connector_summary_counters.py#L162) | 162 | `"            \"snippet\": \"Renewable energy storage report\","` | — |
| [SRC-DA61479D59-L000163](../../tests/test_connector_summary_counters.py#L163) | 163 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000164](../../tests/test_connector_summary_counters.py#L164) | 164 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000165](../../tests/test_connector_summary_counters.py#L165) | 165 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000166](../../tests/test_connector_summary_counters.py#L166) | 166 | `"            \"provider_rank\": 1,"` | — |
| [SRC-DA61479D59-L000167](../../tests/test_connector_summary_counters.py#L167) | 167 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000168](../../tests/test_connector_summary_counters.py#L168) | 168 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000169](../../tests/test_connector_summary_counters.py#L169) | 169 | `"        },"` | — |
| [SRC-DA61479D59-L000170](../../tests/test_connector_summary_counters.py#L170) | 170 | `"        {"` | — |
| [SRC-DA61479D59-L000171](../../tests/test_connector_summary_counters.py#L171) | 171 | `"            \"title\": \"Renewable energy storage statistics\","` | — |
| [SRC-DA61479D59-L000172](../../tests/test_connector_summary_counters.py#L172) | 172 | `"            \"url\": \"https://example.org/statistics\","` | — |
| [SRC-DA61479D59-L000173](../../tests/test_connector_summary_counters.py#L173) | 173 | `"            \"snippet\": \"Renewable energy storage statistics\","` | — |
| [SRC-DA61479D59-L000174](../../tests/test_connector_summary_counters.py#L174) | 174 | `"            \"page_text\": \"\","` | — |
| [SRC-DA61479D59-L000175](../../tests/test_connector_summary_counters.py#L175) | 175 | `"            \"page_fetched\": False,"` | — |
| [SRC-DA61479D59-L000176](../../tests/test_connector_summary_counters.py#L176) | 176 | `"            \"provider\": \"test_search\","` | — |
| [SRC-DA61479D59-L000177](../../tests/test_connector_summary_counters.py#L177) | 177 | `"            \"provider_rank\": 2,"` | — |
| [SRC-DA61479D59-L000178](../../tests/test_connector_summary_counters.py#L178) | 178 | `"            \"search_query\": query,"` | — |
| [SRC-DA61479D59-L000179](../../tests/test_connector_summary_counters.py#L179) | 179 | `"            \"published_at\": \"\","` | — |
| [SRC-DA61479D59-L000180](../../tests/test_connector_summary_counters.py#L180) | 180 | `"        },"` | — |
| [SRC-DA61479D59-L000181](../../tests/test_connector_summary_counters.py#L181) | 181 | `"    ]"` | — |
| [SRC-DA61479D59-L000182](../../tests/test_connector_summary_counters.py#L182) | 182 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda _query: results)"` | — |
| [SRC-DA61479D59-L000183](../../tests/test_connector_summary_counters.py#L183) | 183 | `""` | — |
| [SRC-DA61479D59-L000184](../../tests/test_connector_summary_counters.py#L184) | 184 | `"    def fetch(url: str):"` | — |
| [SRC-DA61479D59-L000185](../../tests/test_connector_summary_counters.py#L185) | 185 | `"        if \"example.com\" in url:"` | — |
| [SRC-DA61479D59-L000186](../../tests/test_connector_summary_counters.py#L186) | 186 | `"            return PageFetchResult("` | — |
| [SRC-DA61479D59-L000187](../../tests/test_connector_summary_counters.py#L187) | 187 | `"                \"Report page\","` | — |
| [SRC-DA61479D59-L000188](../../tests/test_connector_summary_counters.py#L188) | 188 | `"                \"Renewable energy storage body, with an explicit note that extraction was capped.\","` | — |
| [SRC-DA61479D59-L000189](../../tests/test_connector_summary_counters.py#L189) | 189 | `"                \"partial_extraction\","` | — |
| [SRC-DA61479D59-L000190](../../tests/test_connector_summary_counters.py#L190) | 190 | `"            )"` | — |
| [SRC-DA61479D59-L000191](../../tests/test_connector_summary_counters.py#L191) | 191 | `"        return PageFetchResult(\"\", \"\", \"http_error\", \"HTTPStatus\")"` | — |
| [SRC-DA61479D59-L000192](../../tests/test_connector_summary_counters.py#L192) | 192 | `""` | — |
| [SRC-DA61479D59-L000193](../../tests/test_connector_summary_counters.py#L193) | 193 | `"    monkeypatch.setattr(agent, \"_fetch_page\", fetch)"` | — |
| [SRC-DA61479D59-L000194](../../tests/test_connector_summary_counters.py#L194) | 194 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-DA61479D59-L000195](../../tests/test_connector_summary_counters.py#L195) | 195 | `"        \"queries\": [query],"` | — |
| [SRC-DA61479D59-L000196](../../tests/test_connector_summary_counters.py#L196) | 196 | `"        \"direct_urls\": [],"` | — |
| [SRC-DA61479D59-L000197](../../tests/test_connector_summary_counters.py#L197) | 197 | `"        \"social_focus\": False,"` | — |
| [SRC-DA61479D59-L000198](../../tests/test_connector_summary_counters.py#L198) | 198 | `"        \"freshness\": \"any\","` | — |
| [SRC-DA61479D59-L000199](../../tests/test_connector_summary_counters.py#L199) | 199 | `"        \"depth\": \"standard\","` | — |
| [SRC-DA61479D59-L000200](../../tests/test_connector_summary_counters.py#L200) | 200 | `"        \"platforms\": [],"` | — |
| [SRC-DA61479D59-L000201](../../tests/test_connector_summary_counters.py#L201) | 201 | `"        \"planning_method\": \"unit_test\","` | — |
| [SRC-DA61479D59-L000202](../../tests/test_connector_summary_counters.py#L202) | 202 | `"    })"` | — |
| [SRC-DA61479D59-L000203](../../tests/test_connector_summary_counters.py#L203) | 203 | `""` | — |
| [SRC-DA61479D59-L000204](../../tests/test_connector_summary_counters.py#L204) | 204 | `"    assert warnings"` | — |
| [SRC-DA61479D59-L000205](../../tests/test_connector_summary_counters.py#L205) | 205 | `"    assert report[\"pages_fetch_attempted\"] == 2"` | — |
| [SRC-DA61479D59-L000206](../../tests/test_connector_summary_counters.py#L206) | 206 | `"    assert report[\"pages_content_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000207](../../tests/test_connector_summary_counters.py#L207) | 207 | `"    assert report[\"pages_partial_extracted\"] == 1"` | — |
| [SRC-DA61479D59-L000208](../../tests/test_connector_summary_counters.py#L208) | 208 | `"    assert report[\"pages_extract_failed\"] == 1"` | — |
| [SRC-DA61479D59-L000209](../../tests/test_connector_summary_counters.py#L209) | 209 | `"    assert report[\"page_fetch_status_counts\"][\"partial_extraction\"] == 1"` | — |
| [SRC-DA61479D59-L000210](../../tests/test_connector_summary_counters.py#L210) | 210 | `"    assert report[\"page_fetch_status_counts\"][\"http_error\"] == 1"` | — |
| [SRC-DA61479D59-L000211](../../tests/test_connector_summary_counters.py#L211) | 211 | `"    assert sum(item[\"page_fetch_status\"] == \"partial_extraction\" for item in sources) == 1"` | — |
| [SRC-DA61479D59-L000212](../../tests/test_connector_summary_counters.py#L212) | 212 | `"    assert sum(item[\"page_fetch_status\"] == \"http_error\" for item in sources) == 1"` | — |
| [SRC-DA61479D59-L000213](../../tests/test_connector_summary_counters.py#L213) | 213 | `"    assert any(\"HTTPStatus\" in str(item.get(\"page_fetch_error_class\")) for item in sources)"` | — |
| [SRC-DA61479D59-L000214](../../tests/test_connector_summary_counters.py#L214) | 214 | `""` | — |
| [SRC-DA61479D59-L000215](../../tests/test_connector_summary_counters.py#L215) | 215 | `""` | — |
| [SRC-DA61479D59-L000216](../../tests/test_connector_summary_counters.py#L216) | 216 | `"def test_raw_provider_diagnostics_redact_credentials_from_queries_and_errors():"` | — |
| [SRC-DA61479D59-L000217](../../tests/test_connector_summary_counters.py#L217) | 217 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000218](../../tests/test_connector_summary_counters.py#L218) | 218 | `"    agent._record_provider_diagnostic("` | — |
| [SRC-DA61479D59-L000219](../../tests/test_connector_summary_counters.py#L219) | 219 | `"        provider=\"test_provider\","` | — |
| [SRC-DA61479D59-L000220](../../tests/test_connector_summary_counters.py#L220) | 220 | `"        query=\"research API_KEY=query-secret\","` | — |
| [SRC-DA61479D59-L000221](../../tests/test_connector_summary_counters.py#L221) | 221 | `"        status=\"failed\","` | — |
| [SRC-DA61479D59-L000222](../../tests/test_connector_summary_counters.py#L222) | 222 | `"        error=("` | — |
| [SRC-DA61479D59-L000223](../../tests/test_connector_summary_counters.py#L223) | 223 | `"            \"Authorization: Bearer bearer-secret access_token=access-secret; \""` | — |
| [SRC-DA61479D59-L000224](../../tests/test_connector_summary_counters.py#L224) | 224 | `"            \"URL https://example.test/search?token=url-secret\""` | — |
| [SRC-DA61479D59-L000225](../../tests/test_connector_summary_counters.py#L225) | 225 | `"        ),"` | — |
| [SRC-DA61479D59-L000226](../../tests/test_connector_summary_counters.py#L226) | 226 | `"    )"` | — |
| [SRC-DA61479D59-L000227](../../tests/test_connector_summary_counters.py#L227) | 227 | `""` | — |
| [SRC-DA61479D59-L000228](../../tests/test_connector_summary_counters.py#L228) | 228 | `"    diagnostic_json = json.dumps(agent._provider_diagnostics, ensure_ascii=False)"` | — |
| [SRC-DA61479D59-L000229](../../tests/test_connector_summary_counters.py#L229) | 229 | `"    for secret in (\"query-secret\", \"bearer-secret\", \"access-secret\", \"url-secret\"):"` | — |
| [SRC-DA61479D59-L000230](../../tests/test_connector_summary_counters.py#L230) | 230 | `"        assert secret not in diagnostic_json"` | — |
| [SRC-DA61479D59-L000231](../../tests/test_connector_summary_counters.py#L231) | 231 | `"    assert \"[REDACTED]\" in diagnostic_json"` | — |
| [SRC-DA61479D59-L000232](../../tests/test_connector_summary_counters.py#L232) | 232 | `""` | — |
| [SRC-DA61479D59-L000233](../../tests/test_connector_summary_counters.py#L233) | 233 | `""` | — |
| [SRC-DA61479D59-L000234](../../tests/test_connector_summary_counters.py#L234) | 234 | `"def test_connector_summary_separates_raw_candidates_from_filtered_results():"` | — |
| [SRC-DA61479D59-L000235](../../tests/test_connector_summary_counters.py#L235) | 235 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000236](../../tests/test_connector_summary_counters.py#L236) | 236 | `"    summary = agent._connector_status_summary("` | — |
| [SRC-DA61479D59-L000237](../../tests/test_connector_summary_counters.py#L237) | 237 | `"        [{"` | — |
| [SRC-DA61479D59-L000238](../../tests/test_connector_summary_counters.py#L238) | 238 | `"            \"provider\": \"bing_rss\","` | — |
| [SRC-DA61479D59-L000239](../../tests/test_connector_summary_counters.py#L239) | 239 | `"            \"query\": \"Arabic question with source instructions\","` | — |
| [SRC-DA61479D59-L000240](../../tests/test_connector_summary_counters.py#L240) | 240 | `"            \"status\": \"filtered_all\","` | — |
| [SRC-DA61479D59-L000241](../../tests/test_connector_summary_counters.py#L241) | 241 | `"            \"result_count\": 6,"` | — |
| [SRC-DA61479D59-L000242](../../tests/test_connector_summary_counters.py#L242) | 242 | `"            \"accepted_count\": 0,"` | — |
| [SRC-DA61479D59-L000243](../../tests/test_connector_summary_counters.py#L243) | 243 | `"            \"rejected_count\": 6,"` | — |
| [SRC-DA61479D59-L000244](../../tests/test_connector_summary_counters.py#L244) | 244 | `"            \"rejection_counts\": {"` | — |
| [SRC-DA61479D59-L000245](../../tests/test_connector_summary_counters.py#L245) | 245 | `"                \"malformed_candidate\": 0,"` | — |
| [SRC-DA61479D59-L000246](../../tests/test_connector_summary_counters.py#L246) | 246 | `"                \"invalid_url_or_unsafe_target\": 2,"` | — |
| [SRC-DA61479D59-L000247](../../tests/test_connector_summary_counters.py#L247) | 247 | `"                \"blocked_domain\": 1,"` | — |
| [SRC-DA61479D59-L000248](../../tests/test_connector_summary_counters.py#L248) | 248 | `"                \"relevance_below_threshold\": 3,"` | — |
| [SRC-DA61479D59-L000249](../../tests/test_connector_summary_counters.py#L249) | 249 | `"            },"` | — |
| [SRC-DA61479D59-L000250](../../tests/test_connector_summary_counters.py#L250) | 250 | `"            \"error\": \"all candidates rejected; invalid_url_or_unsafe_target=2, blocked_domain=1, relevance_below_threshold=3\","` | — |
| [SRC-DA61479D59-L000251](../../tests/test_connector_summary_counters.py#L251) | 251 | `"        }],"` | — |
| [SRC-DA61479D59-L000252](../../tests/test_connector_summary_counters.py#L252) | 252 | `"        [],"` | — |
| [SRC-DA61479D59-L000253](../../tests/test_connector_summary_counters.py#L253) | 253 | `"    )"` | — |
| [SRC-DA61479D59-L000254](../../tests/test_connector_summary_counters.py#L254) | 254 | `"    bing = next(item for item in summary[\"connectors\"] if item[\"name\"] == \"bing_rss\")"` | — |
| [SRC-DA61479D59-L000255](../../tests/test_connector_summary_counters.py#L255) | 255 | `"    assert bing[\"attempted\"] is True"` | — |
| [SRC-DA61479D59-L000256](../../tests/test_connector_summary_counters.py#L256) | 256 | `"    assert bing[\"result_count\"] == 6"` | — |
| [SRC-DA61479D59-L000257](../../tests/test_connector_summary_counters.py#L257) | 257 | `"    assert bing[\"accepted_count\"] == 0"` | — |
| [SRC-DA61479D59-L000258](../../tests/test_connector_summary_counters.py#L258) | 258 | `"    assert bing[\"rejected_count\"] == 6"` | — |
| [SRC-DA61479D59-L000259](../../tests/test_connector_summary_counters.py#L259) | 259 | `"    assert bing[\"rejection_counts_observed\"] is True"` | — |
| [SRC-DA61479D59-L000260](../../tests/test_connector_summary_counters.py#L260) | 260 | `"    assert bing[\"rejection_counts\"] == {"` | — |
| [SRC-DA61479D59-L000261](../../tests/test_connector_summary_counters.py#L261) | 261 | `"        \"malformed_candidate\": 0,"` | — |
| [SRC-DA61479D59-L000262](../../tests/test_connector_summary_counters.py#L262) | 262 | `"        \"invalid_url_or_unsafe_target\": 2,"` | — |
| [SRC-DA61479D59-L000263](../../tests/test_connector_summary_counters.py#L263) | 263 | `"        \"blocked_domain\": 1,"` | — |
| [SRC-DA61479D59-L000264](../../tests/test_connector_summary_counters.py#L264) | 264 | `"        \"relevance_below_threshold\": 3,"` | — |
| [SRC-DA61479D59-L000265](../../tests/test_connector_summary_counters.py#L265) | 265 | `"    }"` | — |
| [SRC-DA61479D59-L000266](../../tests/test_connector_summary_counters.py#L266) | 266 | `"    assert sum(bing[\"rejection_counts\"].values()) == bing[\"rejected_count\"]"` | — |
| [SRC-DA61479D59-L000267](../../tests/test_connector_summary_counters.py#L267) | 267 | `"    assert bing[\"candidate_rejection_observed\"] is True"` | — |
| [SRC-DA61479D59-L000268](../../tests/test_connector_summary_counters.py#L268) | 268 | `"    assert bing[\"available_for_this_request\"] is True"` | — |
| [SRC-DA61479D59-L000269](../../tests/test_connector_summary_counters.py#L269) | 269 | `"    assert bing[\"verified_for_this_request\"] is True"` | — |
| [SRC-DA61479D59-L000270](../../tests/test_connector_summary_counters.py#L270) | 270 | `""` | — |
| [SRC-DA61479D59-L000271](../../tests/test_connector_summary_counters.py#L271) | 271 | `""` | — |
| [SRC-DA61479D59-L000272](../../tests/test_connector_summary_counters.py#L272) | 272 | `"def test_connector_summary_does_not_present_partial_legacy_rejection_counts_as_complete():"` | — |
| [SRC-DA61479D59-L000273](../../tests/test_connector_summary_counters.py#L273) | 273 | `"    agent = WebAgent()"` | — |
| [SRC-DA61479D59-L000274](../../tests/test_connector_summary_counters.py#L274) | 274 | `"    summary = agent._connector_status_summary("` | — |
| [SRC-DA61479D59-L000275](../../tests/test_connector_summary_counters.py#L275) | 275 | `"        ["` | — |
| [SRC-DA61479D59-L000276](../../tests/test_connector_summary_counters.py#L276) | 276 | `"            {"` | — |
| [SRC-DA61479D59-L000277](../../tests/test_connector_summary_counters.py#L277) | 277 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-DA61479D59-L000278](../../tests/test_connector_summary_counters.py#L278) | 278 | `"                \"query\": \"first query\","` | — |
| [SRC-DA61479D59-L000279](../../tests/test_connector_summary_counters.py#L279) | 279 | `"                \"status\": \"filtered_all\","` | — |
| [SRC-DA61479D59-L000280](../../tests/test_connector_summary_counters.py#L280) | 280 | `"                \"result_count\": 3,"` | — |
| [SRC-DA61479D59-L000281](../../tests/test_connector_summary_counters.py#L281) | 281 | `"                \"accepted_count\": 0,"` | — |
| [SRC-DA61479D59-L000282](../../tests/test_connector_summary_counters.py#L282) | 282 | `"                \"rejected_count\": 3,"` | — |
| [SRC-DA61479D59-L000283](../../tests/test_connector_summary_counters.py#L283) | 283 | `"            },"` | — |
| [SRC-DA61479D59-L000284](../../tests/test_connector_summary_counters.py#L284) | 284 | `"            {"` | — |
| [SRC-DA61479D59-L000285](../../tests/test_connector_summary_counters.py#L285) | 285 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-DA61479D59-L000286](../../tests/test_connector_summary_counters.py#L286) | 286 | `"                \"query\": \"second query\","` | — |
| [SRC-DA61479D59-L000287](../../tests/test_connector_summary_counters.py#L287) | 287 | `"                \"status\": \"filtered_all\","` | — |
| [SRC-DA61479D59-L000288](../../tests/test_connector_summary_counters.py#L288) | 288 | `"                \"result_count\": 2,"` | — |
| [SRC-DA61479D59-L000289](../../tests/test_connector_summary_counters.py#L289) | 289 | `"                \"accepted_count\": 0,"` | — |
| [SRC-DA61479D59-L000290](../../tests/test_connector_summary_counters.py#L290) | 290 | `"                \"rejected_count\": 2,"` | — |
| [SRC-DA61479D59-L000291](../../tests/test_connector_summary_counters.py#L291) | 291 | `"                \"rejection_counts\": {"` | — |
| [SRC-DA61479D59-L000292](../../tests/test_connector_summary_counters.py#L292) | 292 | `"                    \"malformed_candidate\": 0,"` | — |
| [SRC-DA61479D59-L000293](../../tests/test_connector_summary_counters.py#L293) | 293 | `"                    \"invalid_url_or_unsafe_target\": 0,"` | — |
| [SRC-DA61479D59-L000294](../../tests/test_connector_summary_counters.py#L294) | 294 | `"                    \"blocked_domain\": 0,"` | — |
| [SRC-DA61479D59-L000295](../../tests/test_connector_summary_counters.py#L295) | 295 | `"                    \"relevance_below_threshold\": 2,"` | — |
| [SRC-DA61479D59-L000296](../../tests/test_connector_summary_counters.py#L296) | 296 | `"                },"` | — |
| [SRC-DA61479D59-L000297](../../tests/test_connector_summary_counters.py#L297) | 297 | `"            },"` | — |
| [SRC-DA61479D59-L000298](../../tests/test_connector_summary_counters.py#L298) | 298 | `"        ],"` | — |
| [SRC-DA61479D59-L000299](../../tests/test_connector_summary_counters.py#L299) | 299 | `"        [],"` | — |
| [SRC-DA61479D59-L000300](../../tests/test_connector_summary_counters.py#L300) | 300 | `"    )"` | — |
| [SRC-DA61479D59-L000301](../../tests/test_connector_summary_counters.py#L301) | 301 | `"    bing = next(item for item in summary[\"connectors\"] if item[\"name\"] == \"bing_rss\")"` | — |
| [SRC-DA61479D59-L000302](../../tests/test_connector_summary_counters.py#L302) | 302 | `"    assert bing[\"rejected_count\"] == 5"` | — |
| [SRC-DA61479D59-L000303](../../tests/test_connector_summary_counters.py#L303) | 303 | `"    assert bing[\"rejection_counts_observed\"] is False"` | — |
| [SRC-DA61479D59-L000304](../../tests/test_connector_summary_counters.py#L304) | 304 | `"    assert bing[\"rejection_counts\"] is None"` | — |
## اختبارات

### FILE-6BECF5AD00 — [tests/test_connectors_mocked.py](../../tests/test_connectors_mocked.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6BECF5AD00-L000001](../../tests/test_connectors_mocked.py#L1) | 1 | `"\"\"\"Connector unit tests with mocked HTTP (no live network required).\"\"\""` | — |
| [SRC-6BECF5AD00-L000002](../../tests/test_connectors_mocked.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-6BECF5AD00-L000003](../../tests/test_connectors_mocked.py#L3) | 3 | `""` | — |
| [SRC-6BECF5AD00-L000004](../../tests/test_connectors_mocked.py#L4) | 4 | `""` | — |
| [SRC-6BECF5AD00-L000005](../../tests/test_connectors_mocked.py#L5) | 5 | `"import urllib.parse"` | — |
| [SRC-6BECF5AD00-L000006](../../tests/test_connectors_mocked.py#L6) | 6 | `""` | — |
| [SRC-6BECF5AD00-L000007](../../tests/test_connectors_mocked.py#L7) | 7 | `"import agents.search_connectors as sc"` | — |
| [SRC-6BECF5AD00-L000008](../../tests/test_connectors_mocked.py#L8) | 8 | `""` | — |
| [SRC-6BECF5AD00-L000009](../../tests/test_connectors_mocked.py#L9) | 9 | `""` | — |
| [SRC-6BECF5AD00-L000010](../../tests/test_connectors_mocked.py#L10) | 10 | `"def test_openalex_parses_mocked_payload(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000011](../../tests/test_connectors_mocked.py#L11) | 11 | `"    payload = {"` | — |
| [SRC-6BECF5AD00-L000012](../../tests/test_connectors_mocked.py#L12) | 12 | `"        \"results\": ["` | — |
| [SRC-6BECF5AD00-L000013](../../tests/test_connectors_mocked.py#L13) | 13 | `"            {"` | — |
| [SRC-6BECF5AD00-L000014](../../tests/test_connectors_mocked.py#L14) | 14 | `"                \"display_name\": \"Electric Vehicles in Egypt\","` | — |
| [SRC-6BECF5AD00-L000015](../../tests/test_connectors_mocked.py#L15) | 15 | `"                \"id\": \"https://openalex.org/W123\","` | — |
| [SRC-6BECF5AD00-L000016](../../tests/test_connectors_mocked.py#L16) | 16 | `"                \"primary_location\": {\"landing_page_url\": \"https://example.org/paper\"},"` | — |
| [SRC-6BECF5AD00-L000017](../../tests/test_connectors_mocked.py#L17) | 17 | `"                \"concepts\": [{\"display_name\": \"Battery\"}],"` | — |
| [SRC-6BECF5AD00-L000018](../../tests/test_connectors_mocked.py#L18) | 18 | `"                \"publication_date\": \"2024-01-01\","` | — |
| [SRC-6BECF5AD00-L000019](../../tests/test_connectors_mocked.py#L19) | 19 | `"            }"` | — |
| [SRC-6BECF5AD00-L000020](../../tests/test_connectors_mocked.py#L20) | 20 | `"        ]"` | — |
| [SRC-6BECF5AD00-L000021](../../tests/test_connectors_mocked.py#L21) | 21 | `"    }"` | — |
| [SRC-6BECF5AD00-L000022](../../tests/test_connectors_mocked.py#L22) | 22 | `""` | — |
| [SRC-6BECF5AD00-L000023](../../tests/test_connectors_mocked.py#L23) | 23 | `"    def fake_json(url, headers=None, timeout=12):"` | — |
| [SRC-6BECF5AD00-L000024](../../tests/test_connectors_mocked.py#L24) | 24 | `"        return payload"` | — |
| [SRC-6BECF5AD00-L000025](../../tests/test_connectors_mocked.py#L25) | 25 | `""` | — |
| [SRC-6BECF5AD00-L000026](../../tests/test_connectors_mocked.py#L26) | 26 | `"    monkeypatch.setattr(sc, \"_http_get_json\", fake_json)"` | — |
| [SRC-6BECF5AD00-L000027](../../tests/test_connectors_mocked.py#L27) | 27 | `"    rows = sc.search_openalex(\"electric vehicles Egypt\", limit=3)"` | — |
| [SRC-6BECF5AD00-L000028](../../tests/test_connectors_mocked.py#L28) | 28 | `"    assert len(rows) == 1"` | — |
| [SRC-6BECF5AD00-L000029](../../tests/test_connectors_mocked.py#L29) | 29 | `"    assert rows[0][\"provider\"] == \"openalex\""` | — |
| [SRC-6BECF5AD00-L000030](../../tests/test_connectors_mocked.py#L30) | 30 | `"    assert rows[0][\"url\"] == \"https://example.org/paper\""` | — |
| [SRC-6BECF5AD00-L000031](../../tests/test_connectors_mocked.py#L31) | 31 | `"    assert rows[0][\"page_fetched\"] is False"` | — |
| [SRC-6BECF5AD00-L000032](../../tests/test_connectors_mocked.py#L32) | 32 | `""` | — |
| [SRC-6BECF5AD00-L000033](../../tests/test_connectors_mocked.py#L33) | 33 | `""` | — |
| [SRC-6BECF5AD00-L000034](../../tests/test_connectors_mocked.py#L34) | 34 | `"def test_arxiv_parses_atom(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000035](../../tests/test_connectors_mocked.py#L35) | 35 | `"    xml = \"\"\""` | — |
| [SRC-6BECF5AD00-L000036](../../tests/test_connectors_mocked.py#L36) | 36 | `"    <feed>"` | — |
| [SRC-6BECF5AD00-L000037](../../tests/test_connectors_mocked.py#L37) | 37 | `"      <entry>"` | — |
| [SRC-6BECF5AD00-L000038](../../tests/test_connectors_mocked.py#L38) | 38 | `"        <title>Study of EV Batteries</title>"` | — |
| [SRC-6BECF5AD00-L000039](../../tests/test_connectors_mocked.py#L39) | 39 | `"        <id>http://arxiv.org/abs/2401.00001</id>"` | — |
| [SRC-6BECF5AD00-L000040](../../tests/test_connectors_mocked.py#L40) | 40 | `"        <summary>Battery degradation analysis.</summary>"` | — |
| [SRC-6BECF5AD00-L000041](../../tests/test_connectors_mocked.py#L41) | 41 | `"        <published>2024-01-02T00:00:00Z</published>"` | — |
| [SRC-6BECF5AD00-L000042](../../tests/test_connectors_mocked.py#L42) | 42 | `"      </entry>"` | — |
| [SRC-6BECF5AD00-L000043](../../tests/test_connectors_mocked.py#L43) | 43 | `"    </feed>"` | — |
| [SRC-6BECF5AD00-L000044](../../tests/test_connectors_mocked.py#L44) | 44 | `"    \"\"\""` | — |
| [SRC-6BECF5AD00-L000045](../../tests/test_connectors_mocked.py#L45) | 45 | `""` | — |
| [SRC-6BECF5AD00-L000046](../../tests/test_connectors_mocked.py#L46) | 46 | `"    monkeypatch.setattr(sc, \"_http_get_text\", lambda url, timeout=12: xml)"` | — |
| [SRC-6BECF5AD00-L000047](../../tests/test_connectors_mocked.py#L47) | 47 | `"    rows = sc.search_arxiv(\"battery\", limit=2)"` | — |
| [SRC-6BECF5AD00-L000048](../../tests/test_connectors_mocked.py#L48) | 48 | `"    assert len(rows) == 1"` | — |
| [SRC-6BECF5AD00-L000049](../../tests/test_connectors_mocked.py#L49) | 49 | `"    assert rows[0][\"provider\"] == \"arxiv\""` | — |
| [SRC-6BECF5AD00-L000050](../../tests/test_connectors_mocked.py#L50) | 50 | `"    assert \"arxiv.org\" in rows[0][\"url\"]"` | — |
| [SRC-6BECF5AD00-L000051](../../tests/test_connectors_mocked.py#L51) | 51 | `""` | — |
| [SRC-6BECF5AD00-L000052](../../tests/test_connectors_mocked.py#L52) | 52 | `""` | — |
| [SRC-6BECF5AD00-L000053](../../tests/test_connectors_mocked.py#L53) | 53 | `"def test_connector_failure_returns_empty(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000054](../../tests/test_connectors_mocked.py#L54) | 54 | `"    def boom(*args, **kwargs):"` | — |
| [SRC-6BECF5AD00-L000055](../../tests/test_connectors_mocked.py#L55) | 55 | `"        raise sc.urllib.error.URLError(\"down\")"` | — |
| [SRC-6BECF5AD00-L000056](../../tests/test_connectors_mocked.py#L56) | 56 | `""` | — |
| [SRC-6BECF5AD00-L000057](../../tests/test_connectors_mocked.py#L57) | 57 | `"    monkeypatch.setattr(sc, \"_http_get_json\", boom)"` | — |
| [SRC-6BECF5AD00-L000058](../../tests/test_connectors_mocked.py#L58) | 58 | `"    assert sc.run_connector(\"openalex\", \"query\") == []"` | — |
| [SRC-6BECF5AD00-L000059](../../tests/test_connectors_mocked.py#L59) | 59 | `""` | — |
| [SRC-6BECF5AD00-L000060](../../tests/test_connectors_mocked.py#L60) | 60 | `""` | — |
| [SRC-6BECF5AD00-L000061](../../tests/test_connectors_mocked.py#L61) | 61 | `"def test_run_free_academic_dedupe_path(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000062](../../tests/test_connectors_mocked.py#L62) | 62 | `"    def fake_run(name, query, limit=4):"` | — |
| [SRC-6BECF5AD00-L000063](../../tests/test_connectors_mocked.py#L63) | 63 | `"        return ["` | — |
| [SRC-6BECF5AD00-L000064](../../tests/test_connectors_mocked.py#L64) | 64 | `"            {"` | — |
| [SRC-6BECF5AD00-L000065](../../tests/test_connectors_mocked.py#L65) | 65 | `"                \"title\": f\"{name}-title\","` | — |
| [SRC-6BECF5AD00-L000066](../../tests/test_connectors_mocked.py#L66) | 66 | `"                \"url\": f\"https://example.com/{name}\","` | — |
| [SRC-6BECF5AD00-L000067](../../tests/test_connectors_mocked.py#L67) | 67 | `"                \"snippet\": \"x\","` | — |
| [SRC-6BECF5AD00-L000068](../../tests/test_connectors_mocked.py#L68) | 68 | `"                \"page_fetched\": False,"` | — |
| [SRC-6BECF5AD00-L000069](../../tests/test_connectors_mocked.py#L69) | 69 | `"                \"provider\": name,"` | — |
| [SRC-6BECF5AD00-L000070](../../tests/test_connectors_mocked.py#L70) | 70 | `"                \"provider_rank\": 1,"` | — |
| [SRC-6BECF5AD00-L000071](../../tests/test_connectors_mocked.py#L71) | 71 | `"                \"search_query\": query,"` | — |
| [SRC-6BECF5AD00-L000072](../../tests/test_connectors_mocked.py#L72) | 72 | `"                \"published_at\": \"\","` | — |
| [SRC-6BECF5AD00-L000073](../../tests/test_connectors_mocked.py#L73) | 73 | `"                \"source_class\": \"academic\","` | — |
| [SRC-6BECF5AD00-L000074](../../tests/test_connectors_mocked.py#L74) | 74 | `"            }"` | — |
| [SRC-6BECF5AD00-L000075](../../tests/test_connectors_mocked.py#L75) | 75 | `"        ]"` | — |
| [SRC-6BECF5AD00-L000076](../../tests/test_connectors_mocked.py#L76) | 76 | `""` | — |
| [SRC-6BECF5AD00-L000077](../../tests/test_connectors_mocked.py#L77) | 77 | `"    monkeypatch.setattr(sc, \"run_connector\", fake_run)"` | — |
| [SRC-6BECF5AD00-L000078](../../tests/test_connectors_mocked.py#L78) | 78 | `"    rows = sc.run_free_academic_connectors(\"ev egypt\", limit_per=1)"` | — |
| [SRC-6BECF5AD00-L000079](../../tests/test_connectors_mocked.py#L79) | 79 | `"    assert len(rows) == 3"` | — |
| [SRC-6BECF5AD00-L000080](../../tests/test_connectors_mocked.py#L80) | 80 | `"    providers = {r[\"provider\"] for r in rows}"` | — |
| [SRC-6BECF5AD00-L000081](../../tests/test_connectors_mocked.py#L81) | 81 | `"    assert providers == {\"openalex\", \"arxiv\", \"crossref\"}"` | — |
| [SRC-6BECF5AD00-L000082](../../tests/test_connectors_mocked.py#L82) | 82 | `""` | — |
| [SRC-6BECF5AD00-L000083](../../tests/test_connectors_mocked.py#L83) | 83 | `""` | — |
| [SRC-6BECF5AD00-L000084](../../tests/test_connectors_mocked.py#L84) | 84 | `"def test_openalex_uses_api_key_and_ignores_retired_mailto(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000085](../../tests/test_connectors_mocked.py#L85) | 85 | `"    captured = {}"` | — |
| [SRC-6BECF5AD00-L000086](../../tests/test_connectors_mocked.py#L86) | 86 | `"    monkeypatch.setenv(\"OPENALEX_API_KEY\", \"test-openalex-key\")"` | — |
| [SRC-6BECF5AD00-L000087](../../tests/test_connectors_mocked.py#L87) | 87 | `"    monkeypatch.setenv(\"OPENALEX_MAILTO\", \"legacy@example.invalid\")"` | — |
| [SRC-6BECF5AD00-L000088](../../tests/test_connectors_mocked.py#L88) | 88 | `""` | — |
| [SRC-6BECF5AD00-L000089](../../tests/test_connectors_mocked.py#L89) | 89 | `"    def fake_json(url, headers=None, timeout=12):"` | — |
| [SRC-6BECF5AD00-L000090](../../tests/test_connectors_mocked.py#L90) | 90 | `"        captured[\"url\"] = url"` | — |
| [SRC-6BECF5AD00-L000091](../../tests/test_connectors_mocked.py#L91) | 91 | `"        captured[\"headers\"] = headers or {}"` | — |
| [SRC-6BECF5AD00-L000092](../../tests/test_connectors_mocked.py#L92) | 92 | `"        return {\"results\": []}"` | — |
| [SRC-6BECF5AD00-L000093](../../tests/test_connectors_mocked.py#L93) | 93 | `""` | — |
| [SRC-6BECF5AD00-L000094](../../tests/test_connectors_mocked.py#L94) | 94 | `"    monkeypatch.setattr(sc, \"_http_get_json\", fake_json)"` | — |
| [SRC-6BECF5AD00-L000095](../../tests/test_connectors_mocked.py#L95) | 95 | `"    assert sc.search_openalex(\"solar cells\", limit=3) == []"` | — |
| [SRC-6BECF5AD00-L000096](../../tests/test_connectors_mocked.py#L96) | 96 | `""` | — |
| [SRC-6BECF5AD00-L000097](../../tests/test_connectors_mocked.py#L97) | 97 | `"    params = urllib.parse.parse_qs(urllib.parse.urlsplit(captured[\"url\"]).query)"` | — |
| [SRC-6BECF5AD00-L000098](../../tests/test_connectors_mocked.py#L98) | 98 | `"    assert params[\"search\"] == [\"solar cells\"]"` | — |
| [SRC-6BECF5AD00-L000099](../../tests/test_connectors_mocked.py#L99) | 99 | `"    assert params[\"per_page\"] == [\"3\"]"` | — |
| [SRC-6BECF5AD00-L000100](../../tests/test_connectors_mocked.py#L100) | 100 | `"    assert captured[\"headers\"][\"Authorization\"] == \"Bearer test-openalex-key\""` | — |
| [SRC-6BECF5AD00-L000101](../../tests/test_connectors_mocked.py#L101) | 101 | `"    assert \"test-openalex-key\" not in captured[\"url\"]"` | — |
| [SRC-6BECF5AD00-L000102](../../tests/test_connectors_mocked.py#L102) | 102 | `"    assert \"mailto\" not in params"` | — |
| [SRC-6BECF5AD00-L000103](../../tests/test_connectors_mocked.py#L103) | 103 | `""` | — |
| [SRC-6BECF5AD00-L000104](../../tests/test_connectors_mocked.py#L104) | 104 | `""` | — |
| [SRC-6BECF5AD00-L000105](../../tests/test_connectors_mocked.py#L105) | 105 | `"def test_openalex_remains_available_without_api_key_or_retired_mailto(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000106](../../tests/test_connectors_mocked.py#L106) | 106 | `"    captured = {}"` | — |
| [SRC-6BECF5AD00-L000107](../../tests/test_connectors_mocked.py#L107) | 107 | `"    monkeypatch.delenv(\"OPENALEX_API_KEY\", raising=False)"` | — |
| [SRC-6BECF5AD00-L000108](../../tests/test_connectors_mocked.py#L108) | 108 | `"    monkeypatch.setenv(\"OPENALEX_MAILTO\", \"legacy@example.invalid\")"` | — |
| [SRC-6BECF5AD00-L000109](../../tests/test_connectors_mocked.py#L109) | 109 | `""` | — |
| [SRC-6BECF5AD00-L000110](../../tests/test_connectors_mocked.py#L110) | 110 | `"    def fake_json(url, headers=None, timeout=12):"` | — |
| [SRC-6BECF5AD00-L000111](../../tests/test_connectors_mocked.py#L111) | 111 | `"        captured[\"url\"] = url"` | — |
| [SRC-6BECF5AD00-L000112](../../tests/test_connectors_mocked.py#L112) | 112 | `"        captured[\"headers\"] = headers or {}"` | — |
| [SRC-6BECF5AD00-L000113](../../tests/test_connectors_mocked.py#L113) | 113 | `"        return {\"results\": []}"` | — |
| [SRC-6BECF5AD00-L000114](../../tests/test_connectors_mocked.py#L114) | 114 | `""` | — |
| [SRC-6BECF5AD00-L000115](../../tests/test_connectors_mocked.py#L115) | 115 | `"    monkeypatch.setattr(sc, \"_http_get_json\", fake_json)"` | — |
| [SRC-6BECF5AD00-L000116](../../tests/test_connectors_mocked.py#L116) | 116 | `"    assert sc.search_openalex(\"solar cells\") == []"` | — |
| [SRC-6BECF5AD00-L000117](../../tests/test_connectors_mocked.py#L117) | 117 | `""` | — |
| [SRC-6BECF5AD00-L000118](../../tests/test_connectors_mocked.py#L118) | 118 | `"    params = urllib.parse.parse_qs(urllib.parse.urlsplit(captured[\"url\"]).query)"` | — |
| [SRC-6BECF5AD00-L000119](../../tests/test_connectors_mocked.py#L119) | 119 | `"    assert \"mailto\" not in params"` | — |
| [SRC-6BECF5AD00-L000120](../../tests/test_connectors_mocked.py#L120) | 120 | `"    assert \"Authorization\" not in captured[\"headers\"]"` | — |
| [SRC-6BECF5AD00-L000121](../../tests/test_connectors_mocked.py#L121) | 121 | `""` | — |
| [SRC-6BECF5AD00-L000122](../../tests/test_connectors_mocked.py#L122) | 122 | `""` | — |
| [SRC-6BECF5AD00-L000123](../../tests/test_connectors_mocked.py#L123) | 123 | `"def test_crossref_does_not_send_a_placeholder_contact_email(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000124](../../tests/test_connectors_mocked.py#L124) | 124 | `"    captured = {}"` | — |
| [SRC-6BECF5AD00-L000125](../../tests/test_connectors_mocked.py#L125) | 125 | `"    monkeypatch.delenv(\"CROSSREF_MAILTO\", raising=False)"` | — |
| [SRC-6BECF5AD00-L000126](../../tests/test_connectors_mocked.py#L126) | 126 | `""` | — |
| [SRC-6BECF5AD00-L000127](../../tests/test_connectors_mocked.py#L127) | 127 | `"    def fake_json(url, headers=None, timeout=12):"` | — |
| [SRC-6BECF5AD00-L000128](../../tests/test_connectors_mocked.py#L128) | 128 | `"        captured[\"url\"] = url"` | — |
| [SRC-6BECF5AD00-L000129](../../tests/test_connectors_mocked.py#L129) | 129 | `"        captured[\"headers\"] = headers or {}"` | — |
| [SRC-6BECF5AD00-L000130](../../tests/test_connectors_mocked.py#L130) | 130 | `"        return {\"message\": {\"items\": []}}"` | — |
| [SRC-6BECF5AD00-L000131](../../tests/test_connectors_mocked.py#L131) | 131 | `""` | — |
| [SRC-6BECF5AD00-L000132](../../tests/test_connectors_mocked.py#L132) | 132 | `"    monkeypatch.setattr(sc, \"_http_get_json\", fake_json)"` | — |
| [SRC-6BECF5AD00-L000133](../../tests/test_connectors_mocked.py#L133) | 133 | `"    assert sc.search_crossref(\"solar cells\") == []"` | — |
| [SRC-6BECF5AD00-L000134](../../tests/test_connectors_mocked.py#L134) | 134 | `""` | — |
| [SRC-6BECF5AD00-L000135](../../tests/test_connectors_mocked.py#L135) | 135 | `"    params = urllib.parse.parse_qs(urllib.parse.urlsplit(captured[\"url\"]).query)"` | — |
| [SRC-6BECF5AD00-L000136](../../tests/test_connectors_mocked.py#L136) | 136 | `"    assert \"mailto\" not in params"` | — |
| [SRC-6BECF5AD00-L000137](../../tests/test_connectors_mocked.py#L137) | 137 | `"    assert captured[\"headers\"][\"User-Agent\"] == \"OmaraiResearchBot/1.0\""` | — |
| [SRC-6BECF5AD00-L000138](../../tests/test_connectors_mocked.py#L138) | 138 | `"    assert \"ops@example.com\" not in str(captured)"` | — |
| [SRC-6BECF5AD00-L000139](../../tests/test_connectors_mocked.py#L139) | 139 | `""` | — |
| [SRC-6BECF5AD00-L000140](../../tests/test_connectors_mocked.py#L140) | 140 | `""` | — |
| [SRC-6BECF5AD00-L000141](../../tests/test_connectors_mocked.py#L141) | 141 | `"def test_crossref_uses_an_explicit_contact_email_for_polite_pool(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000142](../../tests/test_connectors_mocked.py#L142) | 142 | `"    captured = {}"` | — |
| [SRC-6BECF5AD00-L000143](../../tests/test_connectors_mocked.py#L143) | 143 | `"    monkeypatch.setenv(\"CROSSREF_MAILTO\", \"research@example.org\")"` | — |
| [SRC-6BECF5AD00-L000144](../../tests/test_connectors_mocked.py#L144) | 144 | `""` | — |
| [SRC-6BECF5AD00-L000145](../../tests/test_connectors_mocked.py#L145) | 145 | `"    def fake_json(url, headers=None, timeout=12):"` | — |
| [SRC-6BECF5AD00-L000146](../../tests/test_connectors_mocked.py#L146) | 146 | `"        captured[\"url\"] = url"` | — |
| [SRC-6BECF5AD00-L000147](../../tests/test_connectors_mocked.py#L147) | 147 | `"        return {\"message\": {\"items\": []}}"` | — |
| [SRC-6BECF5AD00-L000148](../../tests/test_connectors_mocked.py#L148) | 148 | `""` | — |
| [SRC-6BECF5AD00-L000149](../../tests/test_connectors_mocked.py#L149) | 149 | `"    monkeypatch.setattr(sc, \"_http_get_json\", fake_json)"` | — |
| [SRC-6BECF5AD00-L000150](../../tests/test_connectors_mocked.py#L150) | 150 | `"    assert sc.search_crossref(\"solar cells\") == []"` | — |
| [SRC-6BECF5AD00-L000151](../../tests/test_connectors_mocked.py#L151) | 151 | `""` | — |
| [SRC-6BECF5AD00-L000152](../../tests/test_connectors_mocked.py#L152) | 152 | `"    params = urllib.parse.parse_qs(urllib.parse.urlsplit(captured[\"url\"]).query)"` | — |
| [SRC-6BECF5AD00-L000153](../../tests/test_connectors_mocked.py#L153) | 153 | `"    assert params[\"mailto\"] == [\"research@example.org\"]"` | — |
| [SRC-6BECF5AD00-L000154](../../tests/test_connectors_mocked.py#L154) | 154 | `""` | — |
| [SRC-6BECF5AD00-L000155](../../tests/test_connectors_mocked.py#L155) | 155 | `""` | — |
| [SRC-6BECF5AD00-L000156](../../tests/test_connectors_mocked.py#L156) | 156 | `"def test_arxiv_parser_handles_namespaced_atom_and_decodes_xml_entities(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000157](../../tests/test_connectors_mocked.py#L157) | 157 | `"    xml = \"\"\"<?xml version=\"1.0\" encoding=\"UTF-8\"?>"` | — |
| [SRC-6BECF5AD00-L000158](../../tests/test_connectors_mocked.py#L158) | 158 | `"    <atom:feed xmlns:atom=\"http://www.w3.org/2005/Atom\">"` | — |
| [SRC-6BECF5AD00-L000159](../../tests/test_connectors_mocked.py#L159) | 159 | `"      <atom:entry>"` | — |
| [SRC-6BECF5AD00-L000160](../../tests/test_connectors_mocked.py#L160) | 160 | `"        <atom:title>Research &amp; development</atom:title>"` | — |
| [SRC-6BECF5AD00-L000161](../../tests/test_connectors_mocked.py#L161) | 161 | `"        <atom:id>https://arxiv.org/abs/2611.00001</atom:id>"` | — |
| [SRC-6BECF5AD00-L000162](../../tests/test_connectors_mocked.py#L162) | 162 | `"        <atom:summary>Safe &lt;design&gt; &amp; robust.</atom:summary>"` | — |
| [SRC-6BECF5AD00-L000163](../../tests/test_connectors_mocked.py#L163) | 163 | `"        <atom:published>2026-11-08T00:00:00Z</atom:published>"` | — |
| [SRC-6BECF5AD00-L000164](../../tests/test_connectors_mocked.py#L164) | 164 | `"      </atom:entry>"` | — |
| [SRC-6BECF5AD00-L000165](../../tests/test_connectors_mocked.py#L165) | 165 | `"    </atom:feed>"` | — |
| [SRC-6BECF5AD00-L000166](../../tests/test_connectors_mocked.py#L166) | 166 | `"    \"\"\""` | — |
| [SRC-6BECF5AD00-L000167](../../tests/test_connectors_mocked.py#L167) | 167 | `""` | — |
| [SRC-6BECF5AD00-L000168](../../tests/test_connectors_mocked.py#L168) | 168 | `"    monkeypatch.setattr(sc, \"_http_get_text\", lambda _url, timeout=12: xml)"` | — |
| [SRC-6BECF5AD00-L000169](../../tests/test_connectors_mocked.py#L169) | 169 | `"    rows = sc.search_arxiv(\"research design\", limit=2)"` | — |
| [SRC-6BECF5AD00-L000170](../../tests/test_connectors_mocked.py#L170) | 170 | `""` | — |
| [SRC-6BECF5AD00-L000171](../../tests/test_connectors_mocked.py#L171) | 171 | `"    assert len(rows) == 1"` | — |
| [SRC-6BECF5AD00-L000172](../../tests/test_connectors_mocked.py#L172) | 172 | `"    assert rows[0][\"title\"] == \"Research & development\""` | — |
| [SRC-6BECF5AD00-L000173](../../tests/test_connectors_mocked.py#L173) | 173 | `"    assert rows[0][\"snippet\"] == \"Safe <design> & robust.\""` | — |
| [SRC-6BECF5AD00-L000174](../../tests/test_connectors_mocked.py#L174) | 174 | `"    assert rows[0][\"published_at\"] == \"2026-11-08T00:00:00Z\""` | — |
| [SRC-6BECF5AD00-L000175](../../tests/test_connectors_mocked.py#L175) | 175 | `"    assert rows[0][\"url\"] == \"https://arxiv.org/abs/2611.00001\""` | — |
| [SRC-6BECF5AD00-L000176](../../tests/test_connectors_mocked.py#L176) | 176 | `""` | — |
| [SRC-6BECF5AD00-L000177](../../tests/test_connectors_mocked.py#L177) | 177 | `""` | — |
| [SRC-6BECF5AD00-L000178](../../tests/test_connectors_mocked.py#L178) | 178 | `"def test_arxiv_connector_contains_malformed_xml_failure(monkeypatch):"` | — |
| [SRC-6BECF5AD00-L000179](../../tests/test_connectors_mocked.py#L179) | 179 | `"    monkeypatch.setattr("` | — |
| [SRC-6BECF5AD00-L000180](../../tests/test_connectors_mocked.py#L180) | 180 | `"        sc,"` | — |
| [SRC-6BECF5AD00-L000181](../../tests/test_connectors_mocked.py#L181) | 181 | `"        \"_http_get_text\","` | — |
| [SRC-6BECF5AD00-L000182](../../tests/test_connectors_mocked.py#L182) | 182 | `"        lambda _url, timeout=12: \"<atom:feed><atom:entry>\","` | — |
| [SRC-6BECF5AD00-L000183](../../tests/test_connectors_mocked.py#L183) | 183 | `"    )"` | — |
| [SRC-6BECF5AD00-L000184](../../tests/test_connectors_mocked.py#L184) | 184 | `""` | — |
| [SRC-6BECF5AD00-L000185](../../tests/test_connectors_mocked.py#L185) | 185 | `"    assert sc.run_connector(\"arxiv\", \"research query\") == []"` | — |
## اختبارات

### FILE-3D0A619359 — [tests/test_dashboard_security.py](../../tests/test_dashboard_security.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3D0A619359-L000001](../../tests/test_dashboard_security.py#L1) | 1 | `"\"\"\"Static regression checks for sensitive lead-dashboard browser behavior.\"\"\""` | — |
| [SRC-3D0A619359-L000002](../../tests/test_dashboard_security.py#L2) | 2 | `"import json"` | — |
| [SRC-3D0A619359-L000003](../../tests/test_dashboard_security.py#L3) | 3 | `"import re"` | — |
| [SRC-3D0A619359-L000004](../../tests/test_dashboard_security.py#L4) | 4 | `"from pathlib import Path"` | — |
| [SRC-3D0A619359-L000005](../../tests/test_dashboard_security.py#L5) | 5 | `""` | — |
| [SRC-3D0A619359-L000006](../../tests/test_dashboard_security.py#L6) | 6 | `"from agents.omarai import LeadStore"` | — |
| [SRC-3D0A619359-L000007](../../tests/test_dashboard_security.py#L7) | 7 | `""` | — |
| [SRC-3D0A619359-L000008](../../tests/test_dashboard_security.py#L8) | 8 | `"DASHBOARD = Path(__file__).resolve().parents[1] / \"web\" / \"dashboard.html\""` | — |
| [SRC-3D0A619359-L000009](../../tests/test_dashboard_security.py#L9) | 9 | `""` | — |
| [SRC-3D0A619359-L000010](../../tests/test_dashboard_security.py#L10) | 10 | `""` | — |
| [SRC-3D0A619359-L000011](../../tests/test_dashboard_security.py#L11) | 11 | `"def test_hosted_lead_dashboard_exchanges_access_token_for_http_only_session():"` | — |
| [SRC-3D0A619359-L000012](../../tests/test_dashboard_security.py#L12) | 12 | `"    html = DASHBOARD.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000013](../../tests/test_dashboard_security.py#L13) | 13 | `"    assert 'fetch(\"/api/session\"' in html"` | — |
| [SRC-3D0A619359-L000014](../../tests/test_dashboard_security.py#L14) | 14 | `"    assert 'JSON.stringify({access_token:token})' in html"` | — |
| [SRC-3D0A619359-L000015](../../tests/test_dashboard_security.py#L15) | 15 | `"    assert 'credentials:\"same-origin\"' in html"` | — |
| [SRC-3D0A619359-L000016](../../tests/test_dashboard_security.py#L16) | 16 | `"    assert 'headers.Authorization=\"Bearer \"+token' not in html"` | — |
| [SRC-3D0A619359-L000017](../../tests/test_dashboard_security.py#L17) | 17 | `"    assert 'localStorage' not in html"` | — |
| [SRC-3D0A619359-L000018](../../tests/test_dashboard_security.py#L18) | 18 | `"    assert 'sessionStorage' not in html"` | — |
| [SRC-3D0A619359-L000019](../../tests/test_dashboard_security.py#L19) | 19 | `"    assert '$(\"saveAccessToken\").onclick' in html"` | — |
| [SRC-3D0A619359-L000020](../../tests/test_dashboard_security.py#L20) | 20 | `""` | — |
| [SRC-3D0A619359-L000021](../../tests/test_dashboard_security.py#L21) | 21 | `"def test_saved_lead_source_links_reject_non_http_schemes():"` | — |
| [SRC-3D0A619359-L000022](../../tests/test_dashboard_security.py#L22) | 22 | `"    html = DASHBOARD.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000023](../../tests/test_dashboard_security.py#L23) | 23 | `"    assert \"function safeSourceUrl(value)\" in html"` | — |
| [SRC-3D0A619359-L000024](../../tests/test_dashboard_security.py#L24) | 24 | `"    assert '[\"http:\",\"https:\"]' in html"` | — |
| [SRC-3D0A619359-L000025](../../tests/test_dashboard_security.py#L25) | 25 | `"    assert \"const sourceUrl=safeSourceUrl(l.source_url)\" in html"` | — |
| [SRC-3D0A619359-L000026](../../tests/test_dashboard_security.py#L26) | 26 | `"    assert \"const sourceLink=sourceUrl?\" in html"` | — |
| [SRC-3D0A619359-L000027](../../tests/test_dashboard_security.py#L27) | 27 | `""` | — |
| [SRC-3D0A619359-L000028](../../tests/test_dashboard_security.py#L28) | 28 | `"def test_lead_status_handler_accepts_sha256_hex_lead_ids():"` | — |
| [SRC-3D0A619359-L000029](../../tests/test_dashboard_security.py#L29) | 29 | `"    html = DASHBOARD.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000030](../../tests/test_dashboard_security.py#L30) | 30 | `"    assert 'if(!/^[a-f0-9]{24}$/.test(id\|\|\"\"))return;' in html"` | — |
| [SRC-3D0A619359-L000031](../../tests/test_dashboard_security.py#L31) | 31 | `"    assert 'data-lead-id=\"' in html"` | — |
| [SRC-3D0A619359-L000032](../../tests/test_dashboard_security.py#L32) | 32 | `""` | — |
| [SRC-3D0A619359-L000033](../../tests/test_dashboard_security.py#L33) | 33 | `"def test_browser_pages_never_store_access_tokens_in_web_storage():"` | — |
| [SRC-3D0A619359-L000034](../../tests/test_dashboard_security.py#L34) | 34 | `"    root = Path(__file__).resolve().parents[1] / \"web\""` | — |
| [SRC-3D0A619359-L000035](../../tests/test_dashboard_security.py#L35) | 35 | `"    for name in (\"agent.html\", \"dashboard.html\"):"` | — |
| [SRC-3D0A619359-L000036](../../tests/test_dashboard_security.py#L36) | 36 | `"        html = (root / name).read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000037](../../tests/test_dashboard_security.py#L37) | 37 | `"        assert \"localStorage\" not in html"` | — |
| [SRC-3D0A619359-L000038](../../tests/test_dashboard_security.py#L38) | 38 | `"        assert \"sessionStorage\" not in html"` | — |
| [SRC-3D0A619359-L000039](../../tests/test_dashboard_security.py#L39) | 39 | `"        assert \"/api/session\" in html"` | — |
| [SRC-3D0A619359-L000040](../../tests/test_dashboard_security.py#L40) | 40 | `"        assert \"credentials:\\\"same-origin\\\"\" in html"` | — |
| [SRC-3D0A619359-L000041](../../tests/test_dashboard_security.py#L41) | 41 | `""` | — |
| [SRC-3D0A619359-L000042](../../tests/test_dashboard_security.py#L42) | 42 | `""` | — |
| [SRC-3D0A619359-L000043](../../tests/test_dashboard_security.py#L43) | 43 | `""` | — |
| [SRC-3D0A619359-L000044](../../tests/test_dashboard_security.py#L44) | 44 | `"def test_sales_workspace_uses_http_only_session_and_never_persists_access_token():"` | — |
| [SRC-3D0A619359-L000045](../../tests/test_dashboard_security.py#L45) | 45 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000046](../../tests/test_dashboard_security.py#L46) | 46 | `"    html = workspace.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000047](../../tests/test_dashboard_security.py#L47) | 47 | `""` | — |
| [SRC-3D0A619359-L000048](../../tests/test_dashboard_security.py#L48) | 48 | `"    assert 'api(\"/api/session\")' in html"` | — |
| [SRC-3D0A619359-L000049](../../tests/test_dashboard_security.py#L49) | 49 | `"    assert 'credentials:\"same-origin\"' in html"` | — |
| [SRC-3D0A619359-L000050](../../tests/test_dashboard_security.py#L50) | 50 | `"    assert 'JSON.stringify({access_token:token})' not in html"` | — |
| [SRC-3D0A619359-L000051](../../tests/test_dashboard_security.py#L51) | 51 | `"    assert \"localStorage\" not in html"` | — |
| [SRC-3D0A619359-L000052](../../tests/test_dashboard_security.py#L52) | 52 | `"    assert \"sessionStorage\" not in html"` | — |
| [SRC-3D0A619359-L000053](../../tests/test_dashboard_security.py#L53) | 53 | `"    assert 'api(\"/api/leads?limit=500\")' in html"` | — |
| [SRC-3D0A619359-L000054](../../tests/test_dashboard_security.py#L54) | 54 | `"    assert 'api(\"/api/health\")' in html"` | — |
| [SRC-3D0A619359-L000055](../../tests/test_dashboard_security.py#L55) | 55 | `"    assert 'state.activeView===\"system\"' in html"` | — |
| [SRC-3D0A619359-L000056](../../tests/test_dashboard_security.py#L56) | 56 | `"    assert 'if(canWrite())panel.append(createSignalForm())' in html"` | — |
| [SRC-3D0A619359-L000057](../../tests/test_dashboard_security.py#L57) | 57 | `"    assert 'if(canWrite())' in html"` | — |
| [SRC-3D0A619359-L000058](../../tests/test_dashboard_security.py#L58) | 58 | `""` | — |
| [SRC-3D0A619359-L000059](../../tests/test_dashboard_security.py#L59) | 59 | `""` | — |
| [SRC-3D0A619359-L000060](../../tests/test_dashboard_security.py#L60) | 60 | `"def test_workspace_uses_approved_neon_command_theme_and_responsive_accessibility():"` | — |
| [SRC-3D0A619359-L000061](../../tests/test_dashboard_security.py#L61) | 61 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000062](../../tests/test_dashboard_security.py#L62) | 62 | `"    html = workspace.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000063](../../tests/test_dashboard_security.py#L63) | 63 | `""` | — |
| [SRC-3D0A619359-L000064](../../tests/test_dashboard_security.py#L64) | 64 | `"    assert \"Approved direction: Neon Command\" in html"` | — |
| [SRC-3D0A619359-L000065](../../tests/test_dashboard_security.py#L65) | 65 | `"    assert \"--bg:#070d16\" in html"` | — |
| [SRC-3D0A619359-L000066](../../tests/test_dashboard_security.py#L66) | 66 | `"    assert \"rgba(74,216,255,.17)\" in html"` | — |
| [SRC-3D0A619359-L000067](../../tests/test_dashboard_security.py#L67) | 67 | `"    assert \"@media(max-width:1100px)\" in html"` | — |
| [SRC-3D0A619359-L000068](../../tests/test_dashboard_security.py#L68) | 68 | `"    assert \"@media(max-width:760px)\" in html"` | — |
| [SRC-3D0A619359-L000069](../../tests/test_dashboard_security.py#L69) | 69 | `"    assert \"@media(max-width:420px)\" in html"` | — |
| [SRC-3D0A619359-L000070](../../tests/test_dashboard_security.py#L70) | 70 | `"    assert \"prefers-reduced-motion:reduce\" in html"` | — |
| [SRC-3D0A619359-L000071](../../tests/test_dashboard_security.py#L71) | 71 | `"    assert \"forced-colors:active\" in html"` | — |
| [SRC-3D0A619359-L000072](../../tests/test_dashboard_security.py#L72) | 72 | `"    assert \"min-height:42px\" in html"` | — |
| [SRC-3D0A619359-L000073](../../tests/test_dashboard_security.py#L73) | 73 | `"    assert 'href=\"/agent\">وكيل البحث</a>' in html"` | — |
| [SRC-3D0A619359-L000074](../../tests/test_dashboard_security.py#L74) | 74 | `""` | — |
| [SRC-3D0A619359-L000075](../../tests/test_dashboard_security.py#L75) | 75 | `"def test_workspace_write_controls_match_supported_membership_roles():"` | — |
| [SRC-3D0A619359-L000076](../../tests/test_dashboard_security.py#L76) | 76 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000077](../../tests/test_dashboard_security.py#L77) | 77 | `"    html = workspace.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000078](../../tests/test_dashboard_security.py#L78) | 78 | `""` | — |
| [SRC-3D0A619359-L000079](../../tests/test_dashboard_security.py#L79) | 79 | `"    match = re.search(r\"const WRITE_ROLES = (\\[[^\\]]*\\]);\", html)"` | — |
| [SRC-3D0A619359-L000080](../../tests/test_dashboard_security.py#L80) | 80 | `"    assert match is not None"` | — |
| [SRC-3D0A619359-L000081](../../tests/test_dashboard_security.py#L81) | 81 | `"    assert set(json.loads(match.group(1))) == set(LeadStore.ALLOWED_ROLES - {\"viewer\"})"` | — |
| [SRC-3D0A619359-L000082](../../tests/test_dashboard_security.py#L82) | 82 | `""` | — |
| [SRC-3D0A619359-L000083](../../tests/test_dashboard_security.py#L83) | 83 | `"def test_workspace_does_not_clear_local_session_state_when_server_logout_fails():"` | — |
| [SRC-3D0A619359-L000084](../../tests/test_dashboard_security.py#L84) | 84 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000085](../../tests/test_dashboard_security.py#L85) | 85 | `"    html = workspace.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000086](../../tests/test_dashboard_security.py#L86) | 86 | `"    start = html.index('$(\"logoutButton\").addEventListener(\"click\"')"` | — |
| [SRC-3D0A619359-L000087](../../tests/test_dashboard_security.py#L87) | 87 | `"    end = html.index('$(\"addSignalTop\").addEventListener', start)"` | — |
| [SRC-3D0A619359-L000088](../../tests/test_dashboard_security.py#L88) | 88 | `"    handler = html[start:end]"` | — |
| [SRC-3D0A619359-L000089](../../tests/test_dashboard_security.py#L89) | 89 | `""` | — |
| [SRC-3D0A619359-L000090](../../tests/test_dashboard_security.py#L90) | 90 | `"    assert \"catch(e)\" in handler"` | — |
| [SRC-3D0A619359-L000091](../../tests/test_dashboard_security.py#L91) | 91 | `"    assert \"alert(\" in handler"` | — |
| [SRC-3D0A619359-L000092](../../tests/test_dashboard_security.py#L92) | 92 | `"    assert \"catch(_e){}\" not in handler"` | — |
| [SRC-3D0A619359-L000093](../../tests/test_dashboard_security.py#L93) | 93 | `"    assert handler.index(\"await api(\\\"/api/session/logout\\\"\") < handler.index(\"state.role=null\")"` | — |
| [SRC-3D0A619359-L000094](../../tests/test_dashboard_security.py#L94) | 94 | `"    assert \"return\" in handler.split(\"catch(e)\", 1)[1].split(\"state.role=null\", 1)[0]"` | — |
| [SRC-3D0A619359-L000095](../../tests/test_dashboard_security.py#L95) | 95 | `""` | — |
| [SRC-3D0A619359-L000096](../../tests/test_dashboard_security.py#L96) | 96 | `"def test_workspace_navigation_exposes_six_core_destinations_and_secondary_system_status():"` | — |
| [SRC-3D0A619359-L000097](../../tests/test_dashboard_security.py#L97) | 97 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000098](../../tests/test_dashboard_security.py#L98) | 98 | `"    html = workspace.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000099](../../tests/test_dashboard_security.py#L99) | 99 | `"    match = re.search(r\"const menu=\\[(.*?)\\n\\];\", html, re.DOTALL)"` | — |
| [SRC-3D0A619359-L000100](../../tests/test_dashboard_security.py#L100) | 100 | `"    assert match is not None"` | — |
| [SRC-3D0A619359-L000101](../../tests/test_dashboard_security.py#L101) | 101 | `"    entries = re.findall("` | — |
| [SRC-3D0A619359-L000102](../../tests/test_dashboard_security.py#L102) | 102 | `"        r'\\{id:\"([^\"]+)\",label:\"([^\"]+)\",icon:\"[^\"]+\",enabled:(true\|false)\\}',"` | — |
| [SRC-3D0A619359-L000103](../../tests/test_dashboard_security.py#L103) | 103 | `"        match.group(1),"` | — |
| [SRC-3D0A619359-L000104](../../tests/test_dashboard_security.py#L104) | 104 | `"    )"` | — |
| [SRC-3D0A619359-L000105](../../tests/test_dashboard_security.py#L105) | 105 | `"    assert [entry[0] for entry in entries] == ["` | — |
| [SRC-3D0A619359-L000106](../../tests/test_dashboard_security.py#L106) | 106 | `"        \"overview\", \"offer\", \"campaign\", \"signals\", \"pipeline\", \"indicators\""` | — |
| [SRC-3D0A619359-L000107](../../tests/test_dashboard_security.py#L107) | 107 | `"    ]"` | — |
| [SRC-3D0A619359-L000108](../../tests/test_dashboard_security.py#L108) | 108 | `"    assert all(enabled == \"true\" for _, _, enabled in entries)"` | — |
| [SRC-3D0A619359-L000109](../../tests/test_dashboard_security.py#L109) | 109 | `"    assert 'id=\"systemNav\"' in html"` | — |
| [SRC-3D0A619359-L000110](../../tests/test_dashboard_security.py#L110) | 110 | `"    assert '$(\"systemNav\").addEventListener(\"click\",()=>navigate(\"system\"))' in html"` | — |
| [SRC-3D0A619359-L000111](../../tests/test_dashboard_security.py#L111) | 111 | `""` | — |
| [SRC-3D0A619359-L000112](../../tests/test_dashboard_security.py#L112) | 112 | `""` | — |
| [SRC-3D0A619359-L000113](../../tests/test_dashboard_security.py#L113) | 113 | `"def test_workspace_overview_uses_three_factual_kpis_and_simple_start_actions():"` | — |
| [SRC-3D0A619359-L000114](../../tests/test_dashboard_security.py#L114) | 114 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000115](../../tests/test_dashboard_security.py#L115) | 115 | `"    html = workspace.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000116](../../tests/test_dashboard_security.py#L116) | 116 | `"    overview = html.split(\"function renderOverview(){\", 1)[1].split(\"\\nfunction emptyState\", 1)[0]"` | — |
| [SRC-3D0A619359-L000117](../../tests/test_dashboard_security.py#L117) | 117 | `"    assert 'buildStat(\"إجمالي الإشارات\"' in overview"` | — |
| [SRC-3D0A619359-L000118](../../tests/test_dashboard_security.py#L118) | 118 | `"    assert 'buildStat(\"تحتاج مراجعة\"' in overview"` | — |
| [SRC-3D0A619359-L000119](../../tests/test_dashboard_security.py#L119) | 119 | `"    assert 'buildStat(\"مؤهلة أو قيد المتابعة\"' in overview"` | — |
| [SRC-3D0A619359-L000120](../../tests/test_dashboard_security.py#L120) | 120 | `"    assert \"قوية نسبيًا بالقواعد\" not in overview"` | — |
| [SRC-3D0A619359-L000121](../../tests/test_dashboard_security.py#L121) | 121 | `"    assert 'action(\"١. إعداد ملف المنتج\"' in overview"` | — |
| [SRC-3D0A619359-L000122](../../tests/test_dashboard_security.py#L122) | 122 | `"    assert 'action(\"٢. إنشاء حملة اكتشاف\"' in overview"` | — |
| [SRC-3D0A619359-L000123](../../tests/test_dashboard_security.py#L123) | 123 | `""` | — |
| [SRC-3D0A619359-L000124](../../tests/test_dashboard_security.py#L124) | 124 | `""` | — |
| [SRC-3D0A619359-L000125](../../tests/test_dashboard_security.py#L125) | 125 | `"def test_workspace_indicators_are_derived_from_loaded_server_data_not_mock_metrics():"` | — |
| [SRC-3D0A619359-L000126](../../tests/test_dashboard_security.py#L126) | 126 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000127](../../tests/test_dashboard_security.py#L127) | 127 | `"    html = workspace.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000128](../../tests/test_dashboard_security.py#L128) | 128 | `"    indicators = html.split(\"function renderIndicators(){\", 1)[1].split(\"\\nfunction renderPlaceholder\", 1)[0]"` | — |
| [SRC-3D0A619359-L000129](../../tests/test_dashboard_security.py#L129) | 129 | `"    assert \"state.leads.length\" in indicators"` | — |
| [SRC-3D0A619359-L000130](../../tests/test_dashboard_security.py#L130) | 130 | `"    assert \"state.discoveryRuns.length\" in indicators"` | — |
| [SRC-3D0A619359-L000131](../../tests/test_dashboard_security.py#L131) | 131 | `"    assert 'countByStatus(id)' in indicators"` | — |
| [SRC-3D0A619359-L000132](../../tests/test_dashboard_security.py#L132) | 132 | `"    assert \"safeHttp(x.source_url)\" in indicators"` | — |
| [SRC-3D0A619359-L000133](../../tests/test_dashboard_security.py#L133) | 133 | `"    assert \"78%\" not in indicators"` | — |
| [SRC-3D0A619359-L000134](../../tests/test_dashboard_security.py#L134) | 134 | `"    assert \"12%\" not in indicators"` | — |
| [SRC-3D0A619359-L000135](../../tests/test_dashboard_security.py#L135) | 135 | `"    assert \"احتمال شراء\" in indicators"` | — |
| [SRC-3D0A619359-L000136](../../tests/test_dashboard_security.py#L136) | 136 | `""` | — |
| [SRC-3D0A619359-L000137](../../tests/test_dashboard_security.py#L137) | 137 | `""` | — |
| [SRC-3D0A619359-L000138](../../tests/test_dashboard_security.py#L138) | 138 | `"def test_workspace_indicators_include_responsive_glass_layout_and_semantic_status_colors():"` | — |
| [SRC-3D0A619359-L000139](../../tests/test_dashboard_security.py#L139) | 139 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000140](../../tests/test_dashboard_security.py#L140) | 140 | `"    html = workspace.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000141](../../tests/test_dashboard_security.py#L141) | 141 | `"    assert \".indicator-hero\" in html"` | — |
| [SRC-3D0A619359-L000142](../../tests/test_dashboard_security.py#L142) | 142 | `"    assert \".indicator-ring\" in html"` | — |
| [SRC-3D0A619359-L000143](../../tests/test_dashboard_security.py#L143) | 143 | `"    assert \".indicator-fill.green\" in html"` | — |
| [SRC-3D0A619359-L000144](../../tests/test_dashboard_security.py#L144) | 144 | `"    assert \".indicator-fill.red\" in html"` | — |
| [SRC-3D0A619359-L000145](../../tests/test_dashboard_security.py#L145) | 145 | `"    assert \"@media(max-width:760px)\" in html"` | — |
| [SRC-3D0A619359-L000146](../../tests/test_dashboard_security.py#L146) | 146 | `"    assert \"@media(max-width:520px)\" in html"` | — |
| [SRC-3D0A619359-L000147](../../tests/test_dashboard_security.py#L147) | 147 | `"    # The indicator is created dynamically; assert the runtime DOM attributes are assigned."` | — |
| [SRC-3D0A619359-L000148](../../tests/test_dashboard_security.py#L148) | 148 | `"    assert 'ring.setAttribute(\"role\",\"img\")' in html"` | — |
| [SRC-3D0A619359-L000149](../../tests/test_dashboard_security.py#L149) | 149 | `"    assert 'ring.setAttribute(\"aria-label\",' in html"` | — |
| [SRC-3D0A619359-L000150](../../tests/test_dashboard_security.py#L150) | 150 | `""` | — |
| [SRC-3D0A619359-L000151](../../tests/test_dashboard_security.py#L151) | 151 | `""` | — |
| [SRC-3D0A619359-L000152](../../tests/test_dashboard_security.py#L152) | 152 | `"def test_workspace_uses_safe_http_source_urls_and_text_only_dom_rendering():"` | — |
| [SRC-3D0A619359-L000153](../../tests/test_dashboard_security.py#L153) | 153 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000154](../../tests/test_dashboard_security.py#L154) | 154 | `"    html = workspace.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000155](../../tests/test_dashboard_security.py#L155) | 155 | `""` | — |
| [SRC-3D0A619359-L000156](../../tests/test_dashboard_security.py#L156) | 156 | `"    assert \"function safeHttp(value)\" in html"` | — |
| [SRC-3D0A619359-L000157](../../tests/test_dashboard_security.py#L157) | 157 | `"    assert 'u.protocol!==\"http:\"&&u.protocol!==\"https:\"' in html"` | — |
| [SRC-3D0A619359-L000158](../../tests/test_dashboard_security.py#L158) | 158 | `"    assert \"u.username\|\|u.password\" in html"` | — |
| [SRC-3D0A619359-L000159](../../tests/test_dashboard_security.py#L159) | 159 | `"    assert \"node.textContent=String(text)\" in html"` | — |
| [SRC-3D0A619359-L000160](../../tests/test_dashboard_security.py#L160) | 160 | `"    assert \"innerHTML\" not in html"` | — |
| [SRC-3D0A619359-L000161](../../tests/test_dashboard_security.py#L161) | 161 | `""` | — |
| [SRC-3D0A619359-L000162](../../tests/test_dashboard_security.py#L162) | 162 | `""` | — |
| [SRC-3D0A619359-L000163](../../tests/test_dashboard_security.py#L163) | 163 | `"def test_workspace_product_profile_and_discovery_screens_are_connected_to_protected_apis():"` | — |
| [SRC-3D0A619359-L000164](../../tests/test_dashboard_security.py#L164) | 164 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000165](../../tests/test_dashboard_security.py#L165) | 165 | `"    html = workspace.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000166](../../tests/test_dashboard_security.py#L166) | 166 | `"    match = re.search(r\"const menu=\\[(.*?)\\n\\];\", html, re.DOTALL)"` | — |
| [SRC-3D0A619359-L000167](../../tests/test_dashboard_security.py#L167) | 167 | `"    assert match is not None"` | — |
| [SRC-3D0A619359-L000168](../../tests/test_dashboard_security.py#L168) | 168 | `"    entries = re.findall("` | — |
| [SRC-3D0A619359-L000169](../../tests/test_dashboard_security.py#L169) | 169 | `"        r'\\{id:\"([^\"]+)\",label:\"([^\"]+)\",icon:\"[^\"]+\",enabled:(true\|false)\\}',"` | — |
| [SRC-3D0A619359-L000170](../../tests/test_dashboard_security.py#L170) | 170 | `"        match.group(1),"` | — |
| [SRC-3D0A619359-L000171](../../tests/test_dashboard_security.py#L171) | 171 | `"    )"` | — |
| [SRC-3D0A619359-L000172](../../tests/test_dashboard_security.py#L172) | 172 | `"    roles = {entry_id: enabled == \"true\" for entry_id, _label, enabled in entries}"` | — |
| [SRC-3D0A619359-L000173](../../tests/test_dashboard_security.py#L173) | 173 | `"    assert roles[\"offer\"] is True"` | — |
| [SRC-3D0A619359-L000174](../../tests/test_dashboard_security.py#L174) | 174 | `"    assert roles[\"campaign\"] is True"` | — |
| [SRC-3D0A619359-L000175](../../tests/test_dashboard_security.py#L175) | 175 | `"    assert 'api(\"/api/product-profiles\")' in html"` | — |
| [SRC-3D0A619359-L000176](../../tests/test_dashboard_security.py#L176) | 176 | `"    assert 'api(\"/api/product-profiles\",{method:\"POST\",body:payload})' in html"` | — |
| [SRC-3D0A619359-L000177](../../tests/test_dashboard_security.py#L177) | 177 | `"    assert 'api(\"/api/discoveries\",{method:\"POST\"' in html"` | — |
| [SRC-3D0A619359-L000178](../../tests/test_dashboard_security.py#L178) | 178 | `"    assert 'api(\"/api/discoveries/\"+encodeURIComponent(run.id)+\"/signals/\"+index+\"/save\"' in html"` | — |
| [SRC-3D0A619359-L000179](../../tests/test_dashboard_security.py#L179) | 179 | `"    assert 'optional.checked=false' in html"` | — |
| [SRC-3D0A619359-L000180](../../tests/test_dashboard_security.py#L180) | 180 | `"    assert 'optional.disabled=state.role!==\"owner\"' in html"` | — |
| [SRC-3D0A619359-L000181](../../tests/test_dashboard_security.py#L181) | 181 | `"    assert 'window.location.href=\"/agent\"' in html"` | — |
| [SRC-3D0A619359-L000182](../../tests/test_dashboard_security.py#L182) | 182 | `"    assert \"innerHTML\" not in html"` | — |
| [SRC-3D0A619359-L000183](../../tests/test_dashboard_security.py#L183) | 183 | `"    assert \"Promise.allSettled\" in html"` | — |
| [SRC-3D0A619359-L000184](../../tests/test_dashboard_security.py#L184) | 184 | `"    assert \"تعذر تحميل بعض البيانات\" in html"` | — |
| [SRC-3D0A619359-L000185](../../tests/test_dashboard_security.py#L185) | 185 | `"    assert \"النموذج اللغوي المهيأ حاليًا في Omarai\" in html"` | — |
| [SRC-3D0A619359-L000186](../../tests/test_dashboard_security.py#L186) | 186 | `"    assert \"قد يستهلك حصة أو تكلفة\" in html"` | — |
| [SRC-3D0A619359-L000187](../../tests/test_dashboard_security.py#L187) | 187 | `""` | — |
| [SRC-3D0A619359-L000188](../../tests/test_dashboard_security.py#L188) | 188 | `""` | — |
| [SRC-3D0A619359-L000189](../../tests/test_dashboard_security.py#L189) | 189 | `"def test_workspace_discovery_failure_is_retryable_and_preserves_previous_results():"` | — |
| [SRC-3D0A619359-L000190](../../tests/test_dashboard_security.py#L190) | 190 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000191](../../tests/test_dashboard_security.py#L191) | 191 | `"    html = workspace.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000192](../../tests/test_dashboard_security.py#L192) | 192 | `"    discovery = html.split(\"function renderDiscovery(){\", 1)[1].split("` | — |
| [SRC-3D0A619359-L000193](../../tests/test_dashboard_security.py#L193) | 193 | `"        \"\\nfunction renderCurrent(\", 1"` | — |
| [SRC-3D0A619359-L000194](../../tests/test_dashboard_security.py#L194) | 194 | `"    )[0]"` | — |
| [SRC-3D0A619359-L000195](../../tests/test_dashboard_security.py#L195) | 195 | `""` | — |
| [SRC-3D0A619359-L000196](../../tests/test_dashboard_security.py#L196) | 196 | `"    assert 'status.setAttribute(\"role\",\"status\")' in discovery"` | — |
| [SRC-3D0A619359-L000197](../../tests/test_dashboard_security.py#L197) | 197 | `"    assert 'status.setAttribute(\"aria-live\",\"polite\")' in discovery"` | — |
| [SRC-3D0A619359-L000198](../../tests/test_dashboard_security.py#L198) | 198 | `"    assert 'status.textContent=\"تعذر تشغيل الاكتشاف: \"' in discovery"` | — |
| [SRC-3D0A619359-L000199](../../tests/test_dashboard_security.py#L199) | 199 | `"    assert \"لم تُحذف النتائج السابقة.\" in discovery"` | — |
| [SRC-3D0A619359-L000200](../../tests/test_dashboard_security.py#L200) | 200 | `"    assert 'run.removeAttribute(\"aria-busy\")' in discovery"` | — |
| [SRC-3D0A619359-L000201](../../tests/test_dashboard_security.py#L201) | 201 | `"    assert \"finally{\" in discovery"` | — |
| [SRC-3D0A619359-L000202](../../tests/test_dashboard_security.py#L202) | 202 | `""` | — |
| [SRC-3D0A619359-L000203](../../tests/test_dashboard_security.py#L203) | 203 | `""` | — |
| [SRC-3D0A619359-L000204](../../tests/test_dashboard_security.py#L204) | 204 | `"def test_workspace_discovery_result_survives_history_refresh_failure():"` | — |
| [SRC-3D0A619359-L000205](../../tests/test_dashboard_security.py#L205) | 205 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000206](../../tests/test_dashboard_security.py#L206) | 206 | `"    html = workspace.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000207](../../tests/test_dashboard_security.py#L207) | 207 | `"    discovery = html.split(\"function renderDiscovery(){\", 1)[1].split("` | — |
| [SRC-3D0A619359-L000208](../../tests/test_dashboard_security.py#L208) | 208 | `"        \"\\nfunction renderCurrent(\", 1"` | — |
| [SRC-3D0A619359-L000209](../../tests/test_dashboard_security.py#L209) | 209 | `"    )[0]"` | — |
| [SRC-3D0A619359-L000210](../../tests/test_dashboard_security.py#L210) | 210 | `""` | — |
| [SRC-3D0A619359-L000211](../../tests/test_dashboard_security.py#L211) | 211 | `"    assert 'const savedRun=await api(\"/api/discoveries\"' in discovery"` | — |
| [SRC-3D0A619359-L000212](../../tests/test_dashboard_security.py#L212) | 212 | `"    assert \"state.activeDiscovery=savedRun\" in discovery"` | — |
| [SRC-3D0A619359-L000213](../../tests/test_dashboard_security.py#L213) | 213 | `"    assert \"try{await loadDiscoveryRuns()}catch(refreshError)\" in discovery"` | — |
| [SRC-3D0A619359-L000214](../../tests/test_dashboard_security.py#L214) | 214 | `"    assert \"حُفظت نتيجة البحث، لكن تعذر تحديث سجل العمليات\" in discovery"` | — |
| [SRC-3D0A619359-L000215](../../tests/test_dashboard_security.py#L215) | 215 | `""` | — |
| [SRC-3D0A619359-L000216](../../tests/test_dashboard_security.py#L216) | 216 | `""` | — |
| [SRC-3D0A619359-L000217](../../tests/test_dashboard_security.py#L217) | 217 | `"def test_workspace_exposes_ai_chat_as_secondary_entry_using_agent_api_safely():"` | — |
| [SRC-3D0A619359-L000218](../../tests/test_dashboard_security.py#L218) | 218 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000219](../../tests/test_dashboard_security.py#L219) | 219 | `"    html = workspace.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000220](../../tests/test_dashboard_security.py#L220) | 220 | `"    chat = html.split(\"function chatMessageNode(\", 1)[1].split(\"function renderCurrent(){\", 1)[0]"` | — |
| [SRC-3D0A619359-L000221](../../tests/test_dashboard_security.py#L221) | 221 | `""` | — |
| [SRC-3D0A619359-L000222](../../tests/test_dashboard_security.py#L222) | 222 | `"    assert 'id=\"chatNav\"' in html"` | — |
| [SRC-3D0A619359-L000223](../../tests/test_dashboard_security.py#L223) | 223 | `"    assert '$(\"chatNav\").addEventListener(\"click\",()=>navigate(\"chat\"))' in html"` | — |
| [SRC-3D0A619359-L000224](../../tests/test_dashboard_security.py#L224) | 224 | `"    assert 'state.activeView===\"chat\"' in html"` | — |
| [SRC-3D0A619359-L000225](../../tests/test_dashboard_security.py#L225) | 225 | `"    assert 'api(\"/api/agent\"' in chat"` | — |
| [SRC-3D0A619359-L000226](../../tests/test_dashboard_security.py#L226) | 226 | `"    assert \"history:chat.history.slice(-8)\" in chat"` | — |
| [SRC-3D0A619359-L000227](../../tests/test_dashboard_security.py#L227) | 227 | `"    # Untrusted model/source text must only be rendered with textContent-based helpers."` | — |
| [SRC-3D0A619359-L000228](../../tests/test_dashboard_security.py#L228) | 228 | `"    assert \"innerHTML\" not in chat"` | — |
| [SRC-3D0A619359-L000229](../../tests/test_dashboard_security.py#L229) | 229 | `"    assert \"safeHttp(src.url)\" in chat"` | — |
| [SRC-3D0A619359-L000230](../../tests/test_dashboard_security.py#L230) | 230 | `"    assert \"a.rel=\\\"noopener noreferrer\\\"\" in chat"` | — |
| [SRC-3D0A619359-L000231](../../tests/test_dashboard_security.py#L231) | 231 | `""` | — |
| [SRC-3D0A619359-L000232](../../tests/test_dashboard_security.py#L232) | 232 | `""` | — |
| [SRC-3D0A619359-L000233](../../tests/test_dashboard_security.py#L233) | 233 | `"def test_workspace_clears_chat_at_auth_boundaries_and_ignores_stale_responses():"` | — |
| [SRC-3D0A619359-L000234](../../tests/test_dashboard_security.py#L234) | 234 | `"    workspace = Path(__file__).resolve().parents[1] / \"web\" / \"workspace.html\""` | — |
| [SRC-3D0A619359-L000235](../../tests/test_dashboard_security.py#L235) | 235 | `"    script = workspace.read_text(encoding=\"utf-8\").split(\"<script>\", 1)[1].split(\"</script>\", 1)[0]"` | — |
| [SRC-3D0A619359-L000236](../../tests/test_dashboard_security.py#L236) | 236 | `"    auth = script.split(\"function showAuth(\", 1)[1].split(\"function hideAuth(\", 1)[0]"` | — |
| [SRC-3D0A619359-L000237](../../tests/test_dashboard_security.py#L237) | 237 | `"    chat = script.split(\"async function sendChat(\", 1)[1].split(\"function renderCurrent(\", 1)[0]"` | — |
| [SRC-3D0A619359-L000238](../../tests/test_dashboard_security.py#L238) | 238 | `""` | — |
| [SRC-3D0A619359-L000239](../../tests/test_dashboard_security.py#L239) | 239 | `"    assert \"function clearWorkspaceSession()\" in script"` | — |
| [SRC-3D0A619359-L000240](../../tests/test_dashboard_security.py#L240) | 240 | `"    assert \"clearWorkspaceSession()\" in auth"` | — |
| [SRC-3D0A619359-L000241](../../tests/test_dashboard_security.py#L241) | 241 | `"    assert \"state.authSessionVersion=(state.authSessionVersion\|\|0)+1\" in script"` | — |
| [SRC-3D0A619359-L000242](../../tests/test_dashboard_security.py#L242) | 242 | `"    for field in ("` | — |
| [SRC-3D0A619359-L000243](../../tests/test_dashboard_security.py#L243) | 243 | `"        \"state.role=null\","` | — |
| [SRC-3D0A619359-L000244](../../tests/test_dashboard_security.py#L244) | 244 | `"        \"state.leads=[]\","` | — |
| [SRC-3D0A619359-L000245](../../tests/test_dashboard_security.py#L245) | 245 | `"        \"state.profiles=[]\","` | — |
| [SRC-3D0A619359-L000246](../../tests/test_dashboard_security.py#L246) | 246 | `"        \"state.discoveryRuns=[]\","` | — |
| [SRC-3D0A619359-L000247](../../tests/test_dashboard_security.py#L247) | 247 | `"        \"state.loadWarnings=[]\","` | — |
| [SRC-3D0A619359-L000248](../../tests/test_dashboard_security.py#L248) | 248 | `"        \"state.activeDiscovery=null\","` | — |
| [SRC-3D0A619359-L000249](../../tests/test_dashboard_security.py#L249) | 249 | `"        \"state.activeProfileId=null\","` | — |
| [SRC-3D0A619359-L000250](../../tests/test_dashboard_security.py#L250) | 250 | `"        \"state.analysis=null\","` | — |
| [SRC-3D0A619359-L000251](../../tests/test_dashboard_security.py#L251) | 251 | `"    ):"` | — |
| [SRC-3D0A619359-L000252](../../tests/test_dashboard_security.py#L252) | 252 | `"        assert field in script"` | — |
| [SRC-3D0A619359-L000253](../../tests/test_dashboard_security.py#L253) | 253 | `"    assert 'replaceChildren(emptyState(\"مساحة العمل مقفلة\"' in script"` | — |
| [SRC-3D0A619359-L000254](../../tests/test_dashboard_security.py#L254) | 254 | `"    assert \"function clearChatSession()\" in script"` | — |
| [SRC-3D0A619359-L000255](../../tests/test_dashboard_security.py#L255) | 255 | `"    assert \"clearChatSession()\" in script"` | — |
| [SRC-3D0A619359-L000256](../../tests/test_dashboard_security.py#L256) | 256 | `"    assert \"chat.messages=[]\" in script"` | — |
| [SRC-3D0A619359-L000257](../../tests/test_dashboard_security.py#L257) | 257 | `"    assert \"chat.history=[]\" in script"` | — |
| [SRC-3D0A619359-L000258](../../tests/test_dashboard_security.py#L258) | 258 | `"    assert 'chat.mode=\"deep\"' in script"` | — |
| [SRC-3D0A619359-L000259](../../tests/test_dashboard_security.py#L259) | 259 | `"    assert \"chat.sessionVersion=(chat.sessionVersion\|\|0)+1\" in script"` | — |
| [SRC-3D0A619359-L000260](../../tests/test_dashboard_security.py#L260) | 260 | `"    assert \"function advanceWorkspaceSessionVersion()\" in script"` | — |
| [SRC-3D0A619359-L000261](../../tests/test_dashboard_security.py#L261) | 261 | `"    login = script.split('$(\"loginForm\").addEventListener(\"submit\"', 1)[1].split('$(\"logoutButton\").addEventListener', 1)[0]"` | — |
| [SRC-3D0A619359-L000262](../../tests/test_dashboard_security.py#L262) | 262 | `"    assert \"advanceWorkspaceSessionVersion()\" in login"` | — |
| [SRC-3D0A619359-L000263](../../tests/test_dashboard_security.py#L263) | 263 | `"    api = script.split(\"async function api(\", 1)[1].split(\"function clearChatSession(\", 1)[0]"` | — |
| [SRC-3D0A619359-L000264](../../tests/test_dashboard_security.py#L264) | 264 | `"    assert \"const requestSessionVersion=state.authSessionVersion\" in api"` | — |
| [SRC-3D0A619359-L000265](../../tests/test_dashboard_security.py#L265) | 265 | `"    assert \"if(state.authSessionVersion!==requestSessionVersion)\" in api"` | — |
| [SRC-3D0A619359-L000266](../../tests/test_dashboard_security.py#L266) | 266 | `"    assert \"const requestSessionVersion=chat.sessionVersion\" in chat"` | — |
| [SRC-3D0A619359-L000267](../../tests/test_dashboard_security.py#L267) | 267 | `"    assert \"if(state.chat.sessionVersion!==requestSessionVersion)return;\" in chat"` | — |
| [SRC-3D0A619359-L000268](../../tests/test_dashboard_security.py#L268) | 268 | `"    assert \"if(state.chat.sessionVersion===requestSessionVersion)\" in chat"` | — |
## اختبارات

### FILE-29A9CD43D1 — [tests/test_dialogue_context_pipeline.py](../../tests/test_dialogue_context_pipeline.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-29A9CD43D1-L000001](../../tests/test_dialogue_context_pipeline.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-29A9CD43D1-L000002](../../tests/test_dialogue_context_pipeline.py#L2) | 2 | `""` | — |
| [SRC-29A9CD43D1-L000003](../../tests/test_dialogue_context_pipeline.py#L3) | 3 | `"import json"` | — |
| [SRC-29A9CD43D1-L000004](../../tests/test_dialogue_context_pipeline.py#L4) | 4 | `"from typing import Any"` | — |
| [SRC-29A9CD43D1-L000005](../../tests/test_dialogue_context_pipeline.py#L5) | 5 | `""` | — |
| [SRC-29A9CD43D1-L000006](../../tests/test_dialogue_context_pipeline.py#L6) | 6 | `"import pytest"` | — |
| [SRC-29A9CD43D1-L000007](../../tests/test_dialogue_context_pipeline.py#L7) | 7 | `""` | — |
| [SRC-29A9CD43D1-L000008](../../tests/test_dialogue_context_pipeline.py#L8) | 8 | `"from agents.research import evidence_signal_report"` | — |
| [SRC-29A9CD43D1-L000009](../../tests/test_dialogue_context_pipeline.py#L9) | 9 | `"from agents.dialogue_state import might_be_context_dependent"` | — |
| [SRC-29A9CD43D1-L000010](../../tests/test_dialogue_context_pipeline.py#L10) | 10 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-29A9CD43D1-L000011](../../tests/test_dialogue_context_pipeline.py#L11) | 11 | `""` | — |
| [SRC-29A9CD43D1-L000012](../../tests/test_dialogue_context_pipeline.py#L12) | 12 | `""` | — |
| [SRC-29A9CD43D1-L000013](../../tests/test_dialogue_context_pipeline.py#L13) | 13 | `"def _source(domain: str, queries: list[str]) -> dict[str, Any]:"` | — |
| [SRC-29A9CD43D1-L000014](../../tests/test_dialogue_context_pipeline.py#L14) | 14 | `"    return {"` | — |
| [SRC-29A9CD43D1-L000015](../../tests/test_dialogue_context_pipeline.py#L15) | 15 | `"        \"title\": \"iPhone 17 256GB international warranty coverage in Egypt\","` | — |
| [SRC-29A9CD43D1-L000016](../../tests/test_dialogue_context_pipeline.py#L16) | 16 | `"        \"url\": f\"https://{domain}/iphone-warranty\","` | — |
| [SRC-29A9CD43D1-L000017](../../tests/test_dialogue_context_pipeline.py#L17) | 17 | `"        \"snippet\": \"Warranty coverage and service policy for iPhone 17 in Egypt.\","` | — |
| [SRC-29A9CD43D1-L000018](../../tests/test_dialogue_context_pipeline.py#L18) | 18 | `"        \"page_text\": \"Warranty coverage and service policy for iPhone 17 in Egypt.\","` | — |
| [SRC-29A9CD43D1-L000019](../../tests/test_dialogue_context_pipeline.py#L19) | 19 | `"        \"page_fetched\": True,"` | — |
| [SRC-29A9CD43D1-L000020](../../tests/test_dialogue_context_pipeline.py#L20) | 20 | `"        \"providers\": [\"test_search\"],"` | — |
| [SRC-29A9CD43D1-L000021](../../tests/test_dialogue_context_pipeline.py#L21) | 21 | `"        \"queries\": list(queries),"` | — |
| [SRC-29A9CD43D1-L000022](../../tests/test_dialogue_context_pipeline.py#L22) | 22 | `"        \"domain\": domain,"` | — |
| [SRC-29A9CD43D1-L000023](../../tests/test_dialogue_context_pipeline.py#L23) | 23 | `"        \"source_class\": \"general\","` | — |
| [SRC-29A9CD43D1-L000024](../../tests/test_dialogue_context_pipeline.py#L24) | 24 | `"        \"platform\": \"web\","` | — |
| [SRC-29A9CD43D1-L000025](../../tests/test_dialogue_context_pipeline.py#L25) | 25 | `"        \"published_at\": \"\","` | — |
| [SRC-29A9CD43D1-L000026](../../tests/test_dialogue_context_pipeline.py#L26) | 26 | `"        \"rank_score\": 1.0,"` | — |
| [SRC-29A9CD43D1-L000027](../../tests/test_dialogue_context_pipeline.py#L27) | 27 | `"    }"` | — |
| [SRC-29A9CD43D1-L000028](../../tests/test_dialogue_context_pipeline.py#L28) | 28 | `""` | — |
| [SRC-29A9CD43D1-L000029](../../tests/test_dialogue_context_pipeline.py#L29) | 29 | `""` | — |
| [SRC-29A9CD43D1-L000030](../../tests/test_dialogue_context_pipeline.py#L30) | 30 | `"def _report(plan: dict[str, Any], sources: list[dict[str, Any]]) -> dict[str, Any]:"` | — |
| [SRC-29A9CD43D1-L000031](../../tests/test_dialogue_context_pipeline.py#L31) | 31 | `"    return {"` | — |
| [SRC-29A9CD43D1-L000032](../../tests/test_dialogue_context_pipeline.py#L32) | 32 | `"        \"queries_planned\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-29A9CD43D1-L000033](../../tests/test_dialogue_context_pipeline.py#L33) | 33 | `"        \"queries_attempted\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-29A9CD43D1-L000034](../../tests/test_dialogue_context_pipeline.py#L34) | 34 | `"        \"queries_attempted_known\": True,"` | — |
| [SRC-29A9CD43D1-L000035](../../tests/test_dialogue_context_pipeline.py#L35) | 35 | `"        \"search_attempted\": True,"` | — |
| [SRC-29A9CD43D1-L000036](../../tests/test_dialogue_context_pipeline.py#L36) | 36 | `"        \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-29A9CD43D1-L000037](../../tests/test_dialogue_context_pipeline.py#L37) | 37 | `"        \"query_results\": [],"` | — |
| [SRC-29A9CD43D1-L000038](../../tests/test_dialogue_context_pipeline.py#L38) | 38 | `"        \"unique_sources\": len(sources),"` | — |
| [SRC-29A9CD43D1-L000039](../../tests/test_dialogue_context_pipeline.py#L39) | 39 | `"        \"pages_fetched\": len(sources),"` | — |
