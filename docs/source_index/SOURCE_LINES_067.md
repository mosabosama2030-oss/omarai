# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **067**
- سجلات الأسطر: **800**
- النطاق: SRC-8C13B81AB4-L000019 إلى SRC-DE7EABE998-L000337
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-8C13B81AB4 — [tests/test_web_agent_nlu_integration.py](../../tests/test_web_agent_nlu_integration.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-8C13B81AB4-L000019](../../tests/test_web_agent_nlu_integration.py#L19) | 19 | `"        \"snippet\": \"Peer reviewed research on lithium battery degradation study.\","` | — |
| [SRC-8C13B81AB4-L000020](../../tests/test_web_agent_nlu_integration.py#L20) | 20 | `"        \"page_fetched\": False,"` | — |
| [SRC-8C13B81AB4-L000021](../../tests/test_web_agent_nlu_integration.py#L21) | 21 | `"        \"provider\": provider,"` | — |
| [SRC-8C13B81AB4-L000022](../../tests/test_web_agent_nlu_integration.py#L22) | 22 | `"        \"provider_rank\": 1,"` | — |
| [SRC-8C13B81AB4-L000023](../../tests/test_web_agent_nlu_integration.py#L23) | 23 | `"        \"search_query\": query,"` | — |
| [SRC-8C13B81AB4-L000024](../../tests/test_web_agent_nlu_integration.py#L24) | 24 | `"        \"published_at\": \"2025\","` | — |
| [SRC-8C13B81AB4-L000025](../../tests/test_web_agent_nlu_integration.py#L25) | 25 | `"        \"source_class\": \"academic\","` | — |
| [SRC-8C13B81AB4-L000026](../../tests/test_web_agent_nlu_integration.py#L26) | 26 | `"    }"` | — |
| [SRC-8C13B81AB4-L000027](../../tests/test_web_agent_nlu_integration.py#L27) | 27 | `""` | — |
| [SRC-8C13B81AB4-L000028](../../tests/test_web_agent_nlu_integration.py#L28) | 28 | `""` | — |
| [SRC-8C13B81AB4-L000029](../../tests/test_web_agent_nlu_integration.py#L29) | 29 | `"def test_sparse_academic_search_uses_budgeted_safe_connectors(monkeypatch) -> None:"` | — |
| [SRC-8C13B81AB4-L000030](../../tests/test_web_agent_nlu_integration.py#L30) | 30 | `"    agent = WebAgent()"` | — |
| [SRC-8C13B81AB4-L000031](../../tests/test_web_agent_nlu_integration.py#L31) | 31 | `"    agent._request_budget = None"` | — |
| [SRC-8C13B81AB4-L000032](../../tests/test_web_agent_nlu_integration.py#L32) | 32 | `"    for key in (\"DEEPSEEK_SEARCH_API_KEY\", \"BRAVE_SEARCH_API_KEY\", \"TAVILY_API_KEY\"):"` | — |
| [SRC-8C13B81AB4-L000033](../../tests/test_web_agent_nlu_integration.py#L33) | 33 | `"        monkeypatch.delenv(key, raising=False)"` | — |
| [SRC-8C13B81AB4-L000034](../../tests/test_web_agent_nlu_integration.py#L34) | 34 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _q: [])"` | — |
| [SRC-8C13B81AB4-L000035](../../tests/test_web_agent_nlu_integration.py#L35) | 35 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _q: [])"` | — |
| [SRC-8C13B81AB4-L000036](../../tests/test_web_agent_nlu_integration.py#L36) | 36 | `"    monkeypatch.setattr(web_module, \"_public_http_url\", lambda value: value)"` | — |
| [SRC-8C13B81AB4-L000037](../../tests/test_web_agent_nlu_integration.py#L37) | 37 | `"    monkeypatch.setattr(web_module, \"_blocked_source_url\", lambda _value: False)"` | — |
| [SRC-8C13B81AB4-L000038](../../tests/test_web_agent_nlu_integration.py#L38) | 38 | `"    monkeypatch.setattr(web_module, \"_relevance_ratio\", lambda _q, _text: 1.0)"` | — |
| [SRC-8C13B81AB4-L000039](../../tests/test_web_agent_nlu_integration.py#L39) | 39 | `"    funcs = {\"openalex\": \"search_openalex\", \"arxiv\": \"search_arxiv\", \"crossref\": \"search_crossref\"}"` | — |
| [SRC-8C13B81AB4-L000040](../../tests/test_web_agent_nlu_integration.py#L40) | 40 | `"    for provider, attr in funcs.items():"` | — |
| [SRC-8C13B81AB4-L000041](../../tests/test_web_agent_nlu_integration.py#L41) | 41 | `"        monkeypatch.setattr("` | — |
| [SRC-8C13B81AB4-L000042](../../tests/test_web_agent_nlu_integration.py#L42) | 42 | `"            web_module, attr,"` | — |
| [SRC-8C13B81AB4-L000043](../../tests/test_web_agent_nlu_integration.py#L43) | 43 | `"            lambda query, limit=3, p=provider: [_academic_result(p, query)],"` | — |
| [SRC-8C13B81AB4-L000044](../../tests/test_web_agent_nlu_integration.py#L44) | 44 | `"        )"` | — |
| [SRC-8C13B81AB4-L000045](../../tests/test_web_agent_nlu_integration.py#L45) | 45 | `"    results = agent._search_web(\"peer-reviewed research on lithium battery degradation\")"` | — |
| [SRC-8C13B81AB4-L000046](../../tests/test_web_agent_nlu_integration.py#L46) | 46 | `"    assert {\"openalex\", \"arxiv\", \"crossref\"} <= {row[\"provider\"] for row in results}"` | — |
| [SRC-8C13B81AB4-L000047](../../tests/test_web_agent_nlu_integration.py#L47) | 47 | `""` | — |
| [SRC-8C13B81AB4-L000048](../../tests/test_web_agent_nlu_integration.py#L48) | 48 | `""` | — |
| [SRC-8C13B81AB4-L000049](../../tests/test_web_agent_nlu_integration.py#L49) | 49 | `"def test_academic_connectors_are_not_called_for_ordinary_sparse_queries(monkeypatch) -> None:"` | — |
| [SRC-8C13B81AB4-L000050](../../tests/test_web_agent_nlu_integration.py#L50) | 50 | `"    agent = WebAgent()"` | — |
| [SRC-8C13B81AB4-L000051](../../tests/test_web_agent_nlu_integration.py#L51) | 51 | `"    agent._request_budget = None"` | — |
| [SRC-8C13B81AB4-L000052](../../tests/test_web_agent_nlu_integration.py#L52) | 52 | `"    for key in (\"DEEPSEEK_SEARCH_API_KEY\", \"BRAVE_SEARCH_API_KEY\", \"TAVILY_API_KEY\"):"` | — |
| [SRC-8C13B81AB4-L000053](../../tests/test_web_agent_nlu_integration.py#L53) | 53 | `"        monkeypatch.delenv(key, raising=False)"` | — |
| [SRC-8C13B81AB4-L000054](../../tests/test_web_agent_nlu_integration.py#L54) | 54 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _q: [{"` | — |
| [SRC-8C13B81AB4-L000055](../../tests/test_web_agent_nlu_integration.py#L55) | 55 | `"        \"title\": \"iPhone 17 price in Egypt\","` | — |
| [SRC-8C13B81AB4-L000056](../../tests/test_web_agent_nlu_integration.py#L56) | 56 | `"        \"url\": \"https://example.com/iphone-price\","` | — |
| [SRC-8C13B81AB4-L000057](../../tests/test_web_agent_nlu_integration.py#L57) | 57 | `"        \"snippet\": \"iPhone 17 price in Egypt.\","` | — |
| [SRC-8C13B81AB4-L000058](../../tests/test_web_agent_nlu_integration.py#L58) | 58 | `"        \"provider\": \"duckduckgo_html\","` | — |
| [SRC-8C13B81AB4-L000059](../../tests/test_web_agent_nlu_integration.py#L59) | 59 | `"        \"provider_rank\": 1,"` | — |
| [SRC-8C13B81AB4-L000060](../../tests/test_web_agent_nlu_integration.py#L60) | 60 | `"    }])"` | — |
| [SRC-8C13B81AB4-L000061](../../tests/test_web_agent_nlu_integration.py#L61) | 61 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _q: [])"` | — |
| [SRC-8C13B81AB4-L000062](../../tests/test_web_agent_nlu_integration.py#L62) | 62 | `"    monkeypatch.setattr(web_module, \"_public_http_url\", lambda value: value)"` | — |
| [SRC-8C13B81AB4-L000063](../../tests/test_web_agent_nlu_integration.py#L63) | 63 | `"    monkeypatch.setattr(web_module, \"_blocked_source_url\", lambda _value: False)"` | — |
| [SRC-8C13B81AB4-L000064](../../tests/test_web_agent_nlu_integration.py#L64) | 64 | `"    monkeypatch.setattr(web_module, \"_relevance_ratio\", lambda _q, _text: 1.0)"` | — |
| [SRC-8C13B81AB4-L000065](../../tests/test_web_agent_nlu_integration.py#L65) | 65 | `""` | — |
| [SRC-8C13B81AB4-L000066](../../tests/test_web_agent_nlu_integration.py#L66) | 66 | `"    def unexpected(*_args, **_kwargs):"` | — |
| [SRC-8C13B81AB4-L000067](../../tests/test_web_agent_nlu_integration.py#L67) | 67 | `"        pytest.fail(\"Academic connectors must not run for ordinary product-price queries.\")"` | — |
| [SRC-8C13B81AB4-L000068](../../tests/test_web_agent_nlu_integration.py#L68) | 68 | `""` | — |
| [SRC-8C13B81AB4-L000069](../../tests/test_web_agent_nlu_integration.py#L69) | 69 | `"    monkeypatch.setattr(web_module, \"search_openalex\", unexpected)"` | — |
| [SRC-8C13B81AB4-L000070](../../tests/test_web_agent_nlu_integration.py#L70) | 70 | `"    monkeypatch.setattr(web_module, \"search_arxiv\", unexpected)"` | — |
| [SRC-8C13B81AB4-L000071](../../tests/test_web_agent_nlu_integration.py#L71) | 71 | `"    monkeypatch.setattr(web_module, \"search_crossref\", unexpected)"` | — |
| [SRC-8C13B81AB4-L000072](../../tests/test_web_agent_nlu_integration.py#L72) | 72 | `"    results = agent._search_web(\"iPhone 17 price in Egypt\")"` | — |
| [SRC-8C13B81AB4-L000073](../../tests/test_web_agent_nlu_integration.py#L73) | 73 | `"    assert len(results) == 1"` | — |
| [SRC-8C13B81AB4-L000074](../../tests/test_web_agent_nlu_integration.py#L74) | 74 | `"    assert results[0][\"provider\"] == \"duckduckgo_html\""` | — |
| [SRC-8C13B81AB4-L000075](../../tests/test_web_agent_nlu_integration.py#L75) | 75 | `""` | — |
| [SRC-8C13B81AB4-L000076](../../tests/test_web_agent_nlu_integration.py#L76) | 76 | `""` | — |
| [SRC-8C13B81AB4-L000077](../../tests/test_web_agent_nlu_integration.py#L77) | 77 | `"def test_web_agent_extracts_joined_comparison_facets() -> None:"` | — |
| [SRC-8C13B81AB4-L000078](../../tests/test_web_agent_nlu_integration.py#L78) | 78 | `"    targets = WebAgent._question_coverage_targets("` | — |
| [SRC-8C13B81AB4-L000079](../../tests/test_web_agent_nlu_integration.py#L79) | 79 | `"        \"قارن بين الأنظمة: السعر والبطارية، بالإضافة إلى الضمان والصيانة \""` | — |
| [SRC-8C13B81AB4-L000080](../../tests/test_web_agent_nlu_integration.py#L80) | 80 | `"        \"والخصوصية والاعتمادية والدعم والجودة\""` | — |
| [SRC-8C13B81AB4-L000081](../../tests/test_web_agent_nlu_integration.py#L81) | 81 | `"    )"` | — |
| [SRC-8C13B81AB4-L000082](../../tests/test_web_agent_nlu_integration.py#L82) | 82 | `"    joined = \" \".join(targets)"` | — |
| [SRC-8C13B81AB4-L000083](../../tests/test_web_agent_nlu_integration.py#L83) | 83 | `"    for expected in (\"السعر\", \"البطارية\", \"الضمان\", \"الصيانة\", \"الخصوصية\", \"الاعتمادية\", \"الدعم\", \"الجودة\"):"` | — |
| [SRC-8C13B81AB4-L000084](../../tests/test_web_agent_nlu_integration.py#L84) | 84 | `"        assert expected in joined"` | — |
| [SRC-8C13B81AB4-L000085](../../tests/test_web_agent_nlu_integration.py#L85) | 85 | `""` | — |
| [SRC-8C13B81AB4-L000086](../../tests/test_web_agent_nlu_integration.py#L86) | 86 | `""` | — |
| [SRC-8C13B81AB4-L000087](../../tests/test_web_agent_nlu_integration.py#L87) | 87 | `"def test_incomplete_compound_evidence_withholds_final_answer() -> None:"` | — |
| [SRC-8C13B81AB4-L000088](../../tests/test_web_agent_nlu_integration.py#L88) | 88 | `"    from agents.web_agent import enforce_aspect_answer_completeness"` | — |
| [SRC-8C13B81AB4-L000089](../../tests/test_web_agent_nlu_integration.py#L89) | 89 | `""` | — |
| [SRC-8C13B81AB4-L000090](../../tests/test_web_agent_nlu_integration.py#L90) | 90 | `"    payload = {"` | — |
| [SRC-8C13B81AB4-L000091](../../tests/test_web_agent_nlu_integration.py#L91) | 91 | `"        \"answer\": \"PRIVATE DRAFT: claim complete details for price and warranty.\","` | — |
| [SRC-8C13B81AB4-L000092](../../tests/test_web_agent_nlu_integration.py#L92) | 92 | `"        \"sources\": ["` | — |
| [SRC-8C13B81AB4-L000093](../../tests/test_web_agent_nlu_integration.py#L93) | 93 | `"            {"` | — |
| [SRC-8C13B81AB4-L000094](../../tests/test_web_agent_nlu_integration.py#L94) | 94 | `"                \"title\": \"Price list\","` | — |
| [SRC-8C13B81AB4-L000095](../../tests/test_web_agent_nlu_integration.py#L95) | 95 | `"                \"url\": \"https://example.org/prices\","` | — |
| [SRC-8C13B81AB4-L000096](../../tests/test_web_agent_nlu_integration.py#L96) | 96 | `"                \"snippet\": \"price cost prices\","` | — |
| [SRC-8C13B81AB4-L000097](../../tests/test_web_agent_nlu_integration.py#L97) | 97 | `"                \"provider\": \"mock\","` | — |
| [SRC-8C13B81AB4-L000098](../../tests/test_web_agent_nlu_integration.py#L98) | 98 | `"            }"` | — |
| [SRC-8C13B81AB4-L000099](../../tests/test_web_agent_nlu_integration.py#L99) | 99 | `"        ],"` | — |
| [SRC-8C13B81AB4-L000100](../../tests/test_web_agent_nlu_integration.py#L100) | 100 | `"        \"search_report\": {"` | — |
| [SRC-8C13B81AB4-L000101](../../tests/test_web_agent_nlu_integration.py#L101) | 101 | `"            \"evidence_ledger\": {"` | — |
| [SRC-8C13B81AB4-L000102](../../tests/test_web_agent_nlu_integration.py#L102) | 102 | `"                \"aspects\": [\"price\", \"warranty\"],"` | — |
| [SRC-8C13B81AB4-L000103](../../tests/test_web_agent_nlu_integration.py#L103) | 103 | `"                \"covered\": [\"price\"],"` | — |
| [SRC-8C13B81AB4-L000104](../../tests/test_web_agent_nlu_integration.py#L104) | 104 | `"                \"missing\": [\"warranty\"],"` | — |
| [SRC-8C13B81AB4-L000105](../../tests/test_web_agent_nlu_integration.py#L105) | 105 | `"                \"coverage_ratio\": 0.5,"` | — |
| [SRC-8C13B81AB4-L000106](../../tests/test_web_agent_nlu_integration.py#L106) | 106 | `"            },"` | — |
| [SRC-8C13B81AB4-L000107](../../tests/test_web_agent_nlu_integration.py#L107) | 107 | `"            \"aspect_diagnostics_ar\": [],"` | — |
| [SRC-8C13B81AB4-L000108](../../tests/test_web_agent_nlu_integration.py#L108) | 108 | `"        },"` | — |
| [SRC-8C13B81AB4-L000109](../../tests/test_web_agent_nlu_integration.py#L109) | 109 | `"    }"` | — |
| [SRC-8C13B81AB4-L000110](../../tests/test_web_agent_nlu_integration.py#L110) | 110 | `"    result = enforce_aspect_answer_completeness(payload)"` | — |
| [SRC-8C13B81AB4-L000111](../../tests/test_web_agent_nlu_integration.py#L111) | 111 | `"    assert result[\"answer_was_withheld\"] is True"` | — |
| [SRC-8C13B81AB4-L000112](../../tests/test_web_agent_nlu_integration.py#L112) | 112 | `"    assert result[\"answer_completeness_status\"] == \"incomplete_evidence_withheld\""` | — |
| [SRC-8C13B81AB4-L000113](../../tests/test_web_agent_nlu_integration.py#L113) | 113 | `"    assert result[\"aspect_evidence_gaps\"] == [\"warranty\"]"` | — |
| [SRC-8C13B81AB4-L000114](../../tests/test_web_agent_nlu_integration.py#L114) | 114 | `"    assert \"PRIVATE DRAFT\" not in result[\"answer\"]"` | — |
| [SRC-8C13B81AB4-L000115](../../tests/test_web_agent_nlu_integration.py#L115) | 115 | `"    assert \"warranty\" in result[\"answer\"]"` | — |
| [SRC-8C13B81AB4-L000116](../../tests/test_web_agent_nlu_integration.py#L116) | 116 | `"    assert result[\"search_report\"][\"task_fulfillment_status\"] == \"possible_gap_detected\""` | — |
| [SRC-8C13B81AB4-L000117](../../tests/test_web_agent_nlu_integration.py#L117) | 117 | `"    assert result[\"final_answer_status\"] == \"incomplete_evidence_withheld\""` | — |
| [SRC-8C13B81AB4-L000118](../../tests/test_web_agent_nlu_integration.py#L118) | 118 | `""` | — |
| [SRC-8C13B81AB4-L000119](../../tests/test_web_agent_nlu_integration.py#L119) | 119 | `""` | — |
| [SRC-8C13B81AB4-L000120](../../tests/test_web_agent_nlu_integration.py#L120) | 120 | `"def test_no_lexical_gap_is_not_presented_as_semantic_proof() -> None:"` | — |
| [SRC-8C13B81AB4-L000121](../../tests/test_web_agent_nlu_integration.py#L121) | 121 | `"    from agents.web_agent import enforce_aspect_answer_completeness"` | — |
| [SRC-8C13B81AB4-L000122](../../tests/test_web_agent_nlu_integration.py#L122) | 122 | `""` | — |
| [SRC-8C13B81AB4-L000123](../../tests/test_web_agent_nlu_integration.py#L123) | 123 | `"    payload = {"` | — |
| [SRC-8C13B81AB4-L000124](../../tests/test_web_agent_nlu_integration.py#L124) | 124 | `"        \"answer\": \"Supported draft.\","` | — |
| [SRC-8C13B81AB4-L000125](../../tests/test_web_agent_nlu_integration.py#L125) | 125 | `"        \"sources\": ["` | — |
| [SRC-8C13B81AB4-L000126](../../tests/test_web_agent_nlu_integration.py#L126) | 126 | `"            {"` | — |
| [SRC-8C13B81AB4-L000127](../../tests/test_web_agent_nlu_integration.py#L127) | 127 | `"                \"title\": \"Price and warranty terms\","` | — |
| [SRC-8C13B81AB4-L000128](../../tests/test_web_agent_nlu_integration.py#L128) | 128 | `"                \"url\": \"https://example.org/terms\","` | — |
| [SRC-8C13B81AB4-L000129](../../tests/test_web_agent_nlu_integration.py#L129) | 129 | `"                \"snippet\": \"price cost warranty warranty coverage\","` | — |
| [SRC-8C13B81AB4-L000130](../../tests/test_web_agent_nlu_integration.py#L130) | 130 | `"                \"provider\": \"mock\","` | — |
| [SRC-8C13B81AB4-L000131](../../tests/test_web_agent_nlu_integration.py#L131) | 131 | `"            }"` | — |
| [SRC-8C13B81AB4-L000132](../../tests/test_web_agent_nlu_integration.py#L132) | 132 | `"        ],"` | — |
| [SRC-8C13B81AB4-L000133](../../tests/test_web_agent_nlu_integration.py#L133) | 133 | `"        \"search_report\": {"` | — |
| [SRC-8C13B81AB4-L000134](../../tests/test_web_agent_nlu_integration.py#L134) | 134 | `"            \"evidence_ledger\": {\"aspects\": [\"price\", \"warranty\"], \"missing\": []},"` | — |
| [SRC-8C13B81AB4-L000135](../../tests/test_web_agent_nlu_integration.py#L135) | 135 | `"            \"aspect_diagnostics_ar\": [],"` | — |
| [SRC-8C13B81AB4-L000136](../../tests/test_web_agent_nlu_integration.py#L136) | 136 | `"        },"` | — |
| [SRC-8C13B81AB4-L000137](../../tests/test_web_agent_nlu_integration.py#L137) | 137 | `"    }"` | — |
| [SRC-8C13B81AB4-L000138](../../tests/test_web_agent_nlu_integration.py#L138) | 138 | `"    result = enforce_aspect_answer_completeness(payload)"` | — |
| [SRC-8C13B81AB4-L000139](../../tests/test_web_agent_nlu_integration.py#L139) | 139 | `"    assert result[\"answer_was_withheld\"] is False"` | — |
| [SRC-8C13B81AB4-L000140](../../tests/test_web_agent_nlu_integration.py#L140) | 140 | `"    assert result[\"answer_completeness_status\"] == ("` | — |
| [SRC-8C13B81AB4-L000141](../../tests/test_web_agent_nlu_integration.py#L141) | 141 | `"        \"no_lexical_gaps_detected_semantic_completeness_not_proven\""` | — |
| [SRC-8C13B81AB4-L000142](../../tests/test_web_agent_nlu_integration.py#L142) | 142 | `"    )"` | — |
| [SRC-8C13B81AB4-L000143](../../tests/test_web_agent_nlu_integration.py#L143) | 143 | `"    assert result[\"aspect_coverage_is_not_truth_score\"] is True"` | — |
## اختبارات

### FILE-E3EEC2014A — [tests/test_workspace_discovery.py](../../tests/test_workspace_discovery.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E3EEC2014A-L000001](../../tests/test_workspace_discovery.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-E3EEC2014A-L000002](../../tests/test_workspace_discovery.py#L2) | 2 | `""` | — |
| [SRC-E3EEC2014A-L000003](../../tests/test_workspace_discovery.py#L3) | 3 | `"import pytest"` | — |
| [SRC-E3EEC2014A-L000004](../../tests/test_workspace_discovery.py#L4) | 4 | `""` | — |
| [SRC-E3EEC2014A-L000005](../../tests/test_workspace_discovery.py#L5) | 5 | `"from agents.omarai import LeadStore"` | — |
| [SRC-E3EEC2014A-L000006](../../tests/test_workspace_discovery.py#L6) | 6 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-E3EEC2014A-L000007](../../tests/test_workspace_discovery.py#L7) | 7 | `""` | — |
| [SRC-E3EEC2014A-L000008](../../tests/test_workspace_discovery.py#L8) | 8 | `""` | — |
| [SRC-E3EEC2014A-L000009](../../tests/test_workspace_discovery.py#L9) | 9 | `"def product_profile(name=\"لوحة إنذار الحريق\", aliases=None):"` | — |
| [SRC-E3EEC2014A-L000010](../../tests/test_workspace_discovery.py#L10) | 10 | `"    return {"` | — |
| [SRC-E3EEC2014A-L000011](../../tests/test_workspace_discovery.py#L11) | 11 | `"        \"product\": {"` | — |
| [SRC-E3EEC2014A-L000012](../../tests/test_workspace_discovery.py#L12) | 12 | `"            \"name\": name,"` | — |
| [SRC-E3EEC2014A-L000013](../../tests/test_workspace_discovery.py#L13) | 13 | `"            \"aliases\": aliases or [\"FACP\"],"` | — |
| [SRC-E3EEC2014A-L000014](../../tests/test_workspace_discovery.py#L14) | 14 | `"            \"category_path\": [\"السلامة\", \"إنذار الحريق\"],"` | — |
| [SRC-E3EEC2014A-L000015](../../tests/test_workspace_discovery.py#L15) | 15 | `"            \"use_cases\": [\"حماية المباني\"],"` | — |
| [SRC-E3EEC2014A-L000016](../../tests/test_workspace_discovery.py#L16) | 16 | `"            \"problems_solved\": [\"اكتشاف الحريق مبكرًا\"],"` | — |
| [SRC-E3EEC2014A-L000017](../../tests/test_workspace_discovery.py#L17) | 17 | `"            \"facts\": [],"` | — |
| [SRC-E3EEC2014A-L000018](../../tests/test_workspace_discovery.py#L18) | 18 | `"        },"` | — |
| [SRC-E3EEC2014A-L000019](../../tests/test_workspace_discovery.py#L19) | 19 | `"        \"market\": {"` | — |
| [SRC-E3EEC2014A-L000020](../../tests/test_workspace_discovery.py#L20) | 20 | `"            \"locations\": [\"القاهرة\", \"الجيزة\"],"` | — |
| [SRC-E3EEC2014A-L000021](../../tests/test_workspace_discovery.py#L21) | 21 | `"            \"industries\": [\"المقاولات\"],"` | — |
| [SRC-E3EEC2014A-L000022](../../tests/test_workspace_discovery.py#L22) | 22 | `"            \"customer_types\": [\"مقاولون\", \"ملاك مشروعات\"],"` | — |
| [SRC-E3EEC2014A-L000023](../../tests/test_workspace_discovery.py#L23) | 23 | `"            \"decision_roles\": [\"مدير مشتريات\"],"` | — |
| [SRC-E3EEC2014A-L000024](../../tests/test_workspace_discovery.py#L24) | 24 | `"            \"exclusions\": [],"` | — |
| [SRC-E3EEC2014A-L000025](../../tests/test_workspace_discovery.py#L25) | 25 | `"        },"` | — |
| [SRC-E3EEC2014A-L000026](../../tests/test_workspace_discovery.py#L26) | 26 | `"        \"locale\": \"ar\","` | — |
| [SRC-E3EEC2014A-L000027](../../tests/test_workspace_discovery.py#L27) | 27 | `"    }"` | — |
| [SRC-E3EEC2014A-L000028](../../tests/test_workspace_discovery.py#L28) | 28 | `""` | — |
| [SRC-E3EEC2014A-L000029](../../tests/test_workspace_discovery.py#L29) | 29 | `""` | — |
| [SRC-E3EEC2014A-L000030](../../tests/test_workspace_discovery.py#L30) | 30 | `"def discovery_run():"` | — |
| [SRC-E3EEC2014A-L000031](../../tests/test_workspace_discovery.py#L31) | 31 | `"    return {"` | — |
| [SRC-E3EEC2014A-L000032](../../tests/test_workspace_discovery.py#L32) | 32 | `"        \"answer\": \"عُثر على إشارة طلب واحدة.\","` | — |
| [SRC-E3EEC2014A-L000033](../../tests/test_workspace_discovery.py#L33) | 33 | `"        \"search_queries\": ['\"مطلوب شراء\" \"لوحة إنذار الحريق\"'],"` | — |
| [SRC-E3EEC2014A-L000034](../../tests/test_workspace_discovery.py#L34) | 34 | `"        \"search_report\": {"` | — |
| [SRC-E3EEC2014A-L000035](../../tests/test_workspace_discovery.py#L35) | 35 | `"            \"lead_generation\": {"` | — |
| [SRC-E3EEC2014A-L000036](../../tests/test_workspace_discovery.py#L36) | 36 | `"                \"status\": \"candidate_signals_found\","` | — |
| [SRC-E3EEC2014A-L000037](../../tests/test_workspace_discovery.py#L37) | 37 | `"                \"candidate_signal_count\": 1,"` | — |
| [SRC-E3EEC2014A-L000038](../../tests/test_workspace_discovery.py#L38) | 38 | `"                \"related_results_reviewed\": 2,"` | — |
| [SRC-E3EEC2014A-L000039](../../tests/test_workspace_discovery.py#L39) | 39 | `"                \"qualification_rule\": \"public_demand_signal_phrase_by_type\","` | — |
| [SRC-E3EEC2014A-L000040](../../tests/test_workspace_discovery.py#L40) | 40 | `"                \"identity_verified\": False,"` | — |
| [SRC-E3EEC2014A-L000041](../../tests/test_workspace_discovery.py#L41) | 41 | `"            },"` | — |
| [SRC-E3EEC2014A-L000042](../../tests/test_workspace_discovery.py#L42) | 42 | `"            \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-E3EEC2014A-L000043](../../tests/test_workspace_discovery.py#L43) | 43 | `"        },"` | — |
| [SRC-E3EEC2014A-L000044](../../tests/test_workspace_discovery.py#L44) | 44 | `"        \"sources\": ["` | — |
| [SRC-E3EEC2014A-L000045](../../tests/test_workspace_discovery.py#L45) | 45 | `"            {"` | — |
| [SRC-E3EEC2014A-L000046](../../tests/test_workspace_discovery.py#L46) | 46 | `"                \"title\": \"طلب توريد لوحة إنذار\","` | — |
| [SRC-E3EEC2014A-L000047](../../tests/test_workspace_discovery.py#L47) | 47 | `"                \"url\": \"https://example.org/public-request/1\","` | — |
| [SRC-E3EEC2014A-L000048](../../tests/test_workspace_discovery.py#L48) | 48 | `"                \"snippet\": \"نبحث عن مورد لتوريد لوحة إنذار حريق لمشروع في القاهرة.\","` | — |
| [SRC-E3EEC2014A-L000049](../../tests/test_workspace_discovery.py#L49) | 49 | `"                \"platform\": \"web\","` | — |
| [SRC-E3EEC2014A-L000050](../../tests/test_workspace_discovery.py#L50) | 50 | `"                \"published_at\": None,"` | — |
| [SRC-E3EEC2014A-L000051](../../tests/test_workspace_discovery.py#L51) | 51 | `"                \"page_fetched\": False,"` | — |
| [SRC-E3EEC2014A-L000052](../../tests/test_workspace_discovery.py#L52) | 52 | `"                \"lead_qualification\": \"public_demand_signal\","` | — |
| [SRC-E3EEC2014A-L000053](../../tests/test_workspace_discovery.py#L53) | 53 | `"                \"lead_intent_evidence\": {"` | — |
| [SRC-E3EEC2014A-L000054](../../tests/test_workspace_discovery.py#L54) | 54 | `"                    \"phrase\": \"نبحث عن مورد\","` | — |
| [SRC-E3EEC2014A-L000055](../../tests/test_workspace_discovery.py#L55) | 55 | `"                    \"basis\": \"snippet\","` | — |
| [SRC-E3EEC2014A-L000056](../../tests/test_workspace_discovery.py#L56) | 56 | `"                    \"signal_type\": \"request_for_quotation\","` | — |
| [SRC-E3EEC2014A-L000057](../../tests/test_workspace_discovery.py#L57) | 57 | `"                    \"product_fit\": \"unassessed\","` | — |
| [SRC-E3EEC2014A-L000058](../../tests/test_workspace_discovery.py#L58) | 58 | `"                },"` | — |
| [SRC-E3EEC2014A-L000059](../../tests/test_workspace_discovery.py#L59) | 59 | `"            },"` | — |
| [SRC-E3EEC2014A-L000060](../../tests/test_workspace_discovery.py#L60) | 60 | `"            {"` | — |
| [SRC-E3EEC2014A-L000061](../../tests/test_workspace_discovery.py#L61) | 61 | `"                \"title\": \"كتالوج لوحات إنذار\","` | — |
| [SRC-E3EEC2014A-L000062](../../tests/test_workspace_discovery.py#L62) | 62 | `"                \"url\": \"https://example.net/catalog\","` | — |
| [SRC-E3EEC2014A-L000063](../../tests/test_workspace_discovery.py#L63) | 63 | `"                \"snippet\": \"كتالوج تعريفي بلوحات إنذار الحريق.\","` | — |
| [SRC-E3EEC2014A-L000064](../../tests/test_workspace_discovery.py#L64) | 64 | `"                \"platform\": \"web\","` | — |
| [SRC-E3EEC2014A-L000065](../../tests/test_workspace_discovery.py#L65) | 65 | `"                \"published_at\": None,"` | — |
| [SRC-E3EEC2014A-L000066](../../tests/test_workspace_discovery.py#L66) | 66 | `"                \"page_fetched\": False,"` | — |
| [SRC-E3EEC2014A-L000067](../../tests/test_workspace_discovery.py#L67) | 67 | `"                \"lead_qualification\": \"related_result_not_lead\","` | — |
| [SRC-E3EEC2014A-L000068](../../tests/test_workspace_discovery.py#L68) | 68 | `"                \"lead_intent_evidence\": None,"` | — |
| [SRC-E3EEC2014A-L000069](../../tests/test_workspace_discovery.py#L69) | 69 | `"            },"` | — |
| [SRC-E3EEC2014A-L000070](../../tests/test_workspace_discovery.py#L70) | 70 | `"        ],"` | — |
| [SRC-E3EEC2014A-L000071](../../tests/test_workspace_discovery.py#L71) | 71 | `"    }"` | — |
| [SRC-E3EEC2014A-L000072](../../tests/test_workspace_discovery.py#L72) | 72 | `""` | — |
| [SRC-E3EEC2014A-L000073](../../tests/test_workspace_discovery.py#L73) | 73 | `""` | — |
| [SRC-E3EEC2014A-L000074](../../tests/test_workspace_discovery.py#L74) | 74 | `"def test_product_profiles_and_discovery_runs_are_tenant_scoped(tmp_path):"` | — |
| [SRC-E3EEC2014A-L000075](../../tests/test_workspace_discovery.py#L75) | 75 | `"    store = LeadStore(tmp_path / \"workspace-discovery.sqlite3\")"` | — |
| [SRC-E3EEC2014A-L000076](../../tests/test_workspace_discovery.py#L76) | 76 | `"    tenant_a = store.create_tenant(\"Workspace A\", \"workspace-a\")"` | — |
| [SRC-E3EEC2014A-L000077](../../tests/test_workspace_discovery.py#L77) | 77 | `"    tenant_b = store.create_tenant(\"Workspace B\", \"workspace-b\")"` | — |
| [SRC-E3EEC2014A-L000078](../../tests/test_workspace_discovery.py#L78) | 78 | `""` | — |
| [SRC-E3EEC2014A-L000079](../../tests/test_workspace_discovery.py#L79) | 79 | `"    saved_profile = store.save_product_profile(product_profile(), tenant_id=tenant_a)"` | — |
| [SRC-E3EEC2014A-L000080](../../tests/test_workspace_discovery.py#L80) | 80 | `"    saved_run = store.save_discovery_run("` | — |
| [SRC-E3EEC2014A-L000081](../../tests/test_workspace_discovery.py#L81) | 81 | `"        saved_profile[\"id\"], discovery_run(), tenant_id=tenant_a"` | — |
| [SRC-E3EEC2014A-L000082](../../tests/test_workspace_discovery.py#L82) | 82 | `"    )"` | — |
| [SRC-E3EEC2014A-L000083](../../tests/test_workspace_discovery.py#L83) | 83 | `""` | — |
| [SRC-E3EEC2014A-L000084](../../tests/test_workspace_discovery.py#L84) | 84 | `"    assert [item[\"id\"] for item in store.list_product_profiles(tenant_id=tenant_a)] == ["` | — |
| [SRC-E3EEC2014A-L000085](../../tests/test_workspace_discovery.py#L85) | 85 | `"        saved_profile[\"id\"]"` | — |
| [SRC-E3EEC2014A-L000086](../../tests/test_workspace_discovery.py#L86) | 86 | `"    ]"` | — |
| [SRC-E3EEC2014A-L000087](../../tests/test_workspace_discovery.py#L87) | 87 | `"    assert store.list_product_profiles(tenant_id=tenant_b) == []"` | — |
| [SRC-E3EEC2014A-L000088](../../tests/test_workspace_discovery.py#L88) | 88 | `"    assert store.get_product_profile(saved_profile[\"id\"], tenant_id=tenant_b) is None"` | — |
| [SRC-E3EEC2014A-L000089](../../tests/test_workspace_discovery.py#L89) | 89 | `"    assert store.get_discovery_run(saved_run[\"id\"], tenant_id=tenant_b) is None"` | — |
| [SRC-E3EEC2014A-L000090](../../tests/test_workspace_discovery.py#L90) | 90 | `"    assert store.list_discovery_runs(tenant_id=tenant_b) == []"` | — |
| [SRC-E3EEC2014A-L000091](../../tests/test_workspace_discovery.py#L91) | 91 | `""` | — |
| [SRC-E3EEC2014A-L000092](../../tests/test_workspace_discovery.py#L92) | 92 | `""` | — |
| [SRC-E3EEC2014A-L000093](../../tests/test_workspace_discovery.py#L93) | 93 | `"def test_duplicate_product_profile_name_updates_within_tenant(tmp_path):"` | — |
| [SRC-E3EEC2014A-L000094](../../tests/test_workspace_discovery.py#L94) | 94 | `"    store = LeadStore(tmp_path / \"workspace-profiles.sqlite3\")"` | — |
| [SRC-E3EEC2014A-L000095](../../tests/test_workspace_discovery.py#L95) | 95 | `"    tenant = store.create_tenant(\"Workspace\", \"workspace\")"` | — |
| [SRC-E3EEC2014A-L000096](../../tests/test_workspace_discovery.py#L96) | 96 | `"    first = store.save_product_profile(product_profile(), tenant_id=tenant)"` | — |
| [SRC-E3EEC2014A-L000097](../../tests/test_workspace_discovery.py#L97) | 97 | `"    updated = store.save_product_profile("` | — |
| [SRC-E3EEC2014A-L000098](../../tests/test_workspace_discovery.py#L98) | 98 | `"        product_profile(aliases=[\"FACP\", \"لوحة إنذار\"]), tenant_id=tenant"` | — |
| [SRC-E3EEC2014A-L000099](../../tests/test_workspace_discovery.py#L99) | 99 | `"    )"` | — |
| [SRC-E3EEC2014A-L000100](../../tests/test_workspace_discovery.py#L100) | 100 | `""` | — |
| [SRC-E3EEC2014A-L000101](../../tests/test_workspace_discovery.py#L101) | 101 | `"    assert updated[\"id\"] == first[\"id\"]"` | — |
| [SRC-E3EEC2014A-L000102](../../tests/test_workspace_discovery.py#L102) | 102 | `"    assert updated[\"profile\"][\"product\"][\"aliases\"] == [\"FACP\", \"لوحة إنذار\"]"` | — |
| [SRC-E3EEC2014A-L000103](../../tests/test_workspace_discovery.py#L103) | 103 | `"    assert len(store.list_product_profiles(tenant_id=tenant)) == 1"` | — |
| [SRC-E3EEC2014A-L000104](../../tests/test_workspace_discovery.py#L104) | 104 | `""` | — |
| [SRC-E3EEC2014A-L000105](../../tests/test_workspace_discovery.py#L105) | 105 | `""` | — |
| [SRC-E3EEC2014A-L000106](../../tests/test_workspace_discovery.py#L106) | 106 | `"def test_discovery_signal_save_uses_server_stored_qualification_and_evidence(tmp_path):"` | — |
| [SRC-E3EEC2014A-L000107](../../tests/test_workspace_discovery.py#L107) | 107 | `"    store = LeadStore(tmp_path / \"workspace-signals.sqlite3\")"` | — |
| [SRC-E3EEC2014A-L000108](../../tests/test_workspace_discovery.py#L108) | 108 | `"    tenant = store.create_tenant(\"Workspace\", \"workspace\")"` | — |
| [SRC-E3EEC2014A-L000109](../../tests/test_workspace_discovery.py#L109) | 109 | `"    profile = store.save_product_profile(product_profile(), tenant_id=tenant)"` | — |
| [SRC-E3EEC2014A-L000110](../../tests/test_workspace_discovery.py#L110) | 110 | `"    run = store.save_discovery_run(profile[\"id\"], discovery_run(), tenant_id=tenant)"` | — |
| [SRC-E3EEC2014A-L000111](../../tests/test_workspace_discovery.py#L111) | 111 | `""` | — |
| [SRC-E3EEC2014A-L000112](../../tests/test_workspace_discovery.py#L112) | 112 | `"    assert store.save_discovery_signal(run[\"id\"], 1, tenant_id=tenant) is None"` | — |
| [SRC-E3EEC2014A-L000113](../../tests/test_workspace_discovery.py#L113) | 113 | `""` | — |
| [SRC-E3EEC2014A-L000114](../../tests/test_workspace_discovery.py#L114) | 114 | `"    saved, created = store.save_discovery_signal(run[\"id\"], 0, tenant_id=tenant)"` | — |
| [SRC-E3EEC2014A-L000115](../../tests/test_workspace_discovery.py#L115) | 115 | `"    assert created is True"` | — |
| [SRC-E3EEC2014A-L000116](../../tests/test_workspace_discovery.py#L116) | 116 | `"    assert saved[\"source_url\"] == \"https://example.org/public-request/1\""` | — |
| [SRC-E3EEC2014A-L000117](../../tests/test_workspace_discovery.py#L117) | 117 | `"    assert \"نبحث عن مورد\" in saved[\"note\"]"` | — |
| [SRC-E3EEC2014A-L000118](../../tests/test_workspace_discovery.py#L118) | 118 | `"    assert \"request_for_quotation\" in saved[\"note\"]"` | — |
| [SRC-E3EEC2014A-L000119](../../tests/test_workspace_discovery.py#L119) | 119 | `"    assert store.save_discovery_signal(run[\"id\"], 0, tenant_id=tenant)[1] is False"` | — |
| [SRC-E3EEC2014A-L000120](../../tests/test_workspace_discovery.py#L120) | 120 | `""` | — |
| [SRC-E3EEC2014A-L000121](../../tests/test_workspace_discovery.py#L121) | 121 | `""` | — |
| [SRC-E3EEC2014A-L000122](../../tests/test_workspace_discovery.py#L122) | 122 | `"def test_discovery_signal_save_rejects_other_tenant_run(tmp_path):"` | — |
| [SRC-E3EEC2014A-L000123](../../tests/test_workspace_discovery.py#L123) | 123 | `"    store = LeadStore(tmp_path / \"workspace-run-isolation.sqlite3\")"` | — |
| [SRC-E3EEC2014A-L000124](../../tests/test_workspace_discovery.py#L124) | 124 | `"    tenant_a = store.create_tenant(\"Workspace A\", \"workspace-a\")"` | — |
| [SRC-E3EEC2014A-L000125](../../tests/test_workspace_discovery.py#L125) | 125 | `"    tenant_b = store.create_tenant(\"Workspace B\", \"workspace-b\")"` | — |
| [SRC-E3EEC2014A-L000126](../../tests/test_workspace_discovery.py#L126) | 126 | `"    profile = store.save_product_profile(product_profile(), tenant_id=tenant_a)"` | — |
| [SRC-E3EEC2014A-L000127](../../tests/test_workspace_discovery.py#L127) | 127 | `"    run = store.save_discovery_run(profile[\"id\"], discovery_run(), tenant_id=tenant_a)"` | — |
| [SRC-E3EEC2014A-L000128](../../tests/test_workspace_discovery.py#L128) | 128 | `""` | — |
| [SRC-E3EEC2014A-L000129](../../tests/test_workspace_discovery.py#L129) | 129 | `"    assert store.save_discovery_signal(run[\"id\"], 0, tenant_id=tenant_b) is None"` | — |
| [SRC-E3EEC2014A-L000130](../../tests/test_workspace_discovery.py#L130) | 130 | `""` | — |
| [SRC-E3EEC2014A-L000131](../../tests/test_workspace_discovery.py#L131) | 131 | `""` | — |
| [SRC-E3EEC2014A-L000132](../../tests/test_workspace_discovery.py#L132) | 132 | `"def test_web_agent_forwards_structured_buyer_queries(monkeypatch):"` | — |
| [SRC-E3EEC2014A-L000133](../../tests/test_workspace_discovery.py#L133) | 133 | `"    agent = WebAgent()"` | — |
| [SRC-E3EEC2014A-L000134](../../tests/test_workspace_discovery.py#L134) | 134 | `"    captured = {}"` | — |
| [SRC-E3EEC2014A-L000135](../../tests/test_workspace_discovery.py#L135) | 135 | `""` | — |
| [SRC-E3EEC2014A-L000136](../../tests/test_workspace_discovery.py#L136) | 136 | `"    def fake_answer_with_budget(question, history=None, mode=\"auto\", *, buyer_queries=None):"` | — |
| [SRC-E3EEC2014A-L000137](../../tests/test_workspace_discovery.py#L137) | 137 | `"        captured.update(question=question, history=history, mode=mode, buyer_queries=buyer_queries)"` | — |
| [SRC-E3EEC2014A-L000138](../../tests/test_workspace_discovery.py#L138) | 138 | `"        return {\"kind\": \"lead_discovery\", \"sources\": []}"` | — |
| [SRC-E3EEC2014A-L000139](../../tests/test_workspace_discovery.py#L139) | 139 | `""` | — |
| [SRC-E3EEC2014A-L000140](../../tests/test_workspace_discovery.py#L140) | 140 | `"    monkeypatch.setattr(agent, \"_answer_with_budget\", fake_answer_with_budget)"` | — |
| [SRC-E3EEC2014A-L000141](../../tests/test_workspace_discovery.py#L141) | 141 | `"    queries = ['\"مطلوب شراء\" \"لوحة إنذار الحريق\"', '\"عايز اشتري\" \"FACP\"']"` | — |
| [SRC-E3EEC2014A-L000142](../../tests/test_workspace_discovery.py#L142) | 142 | `""` | — |
| [SRC-E3EEC2014A-L000143](../../tests/test_workspace_discovery.py#L143) | 143 | `"    result = agent.answer("` | — |
| [SRC-E3EEC2014A-L000144](../../tests/test_workspace_discovery.py#L144) | 144 | `"        \"اكتشف طلب شراء معلن للمنتج في القاهرة\","` | — |
| [SRC-E3EEC2014A-L000145](../../tests/test_workspace_discovery.py#L145) | 145 | `"        buyer_queries=queries,"` | — |
| [SRC-E3EEC2014A-L000146](../../tests/test_workspace_discovery.py#L146) | 146 | `"    )"` | — |
| [SRC-E3EEC2014A-L000147](../../tests/test_workspace_discovery.py#L147) | 147 | `""` | — |
| [SRC-E3EEC2014A-L000148](../../tests/test_workspace_discovery.py#L148) | 148 | `"    assert result[\"kind\"] == \"lead_discovery\""` | — |
| [SRC-E3EEC2014A-L000149](../../tests/test_workspace_discovery.py#L149) | 149 | `"    assert captured[\"buyer_queries\"] == queries"` | — |
| [SRC-E3EEC2014A-L000150](../../tests/test_workspace_discovery.py#L150) | 150 | `""` | — |
| [SRC-E3EEC2014A-L000151](../../tests/test_workspace_discovery.py#L151) | 151 | `""` | — |
| [SRC-E3EEC2014A-L000152](../../tests/test_workspace_discovery.py#L152) | 152 | `"def test_web_agent_can_skip_optional_search_connectors_by_request(monkeypatch):"` | — |
| [SRC-E3EEC2014A-L000153](../../tests/test_workspace_discovery.py#L153) | 153 | `"    monkeypatch.setenv(\"DEEPSEEK_SEARCH_API_KEY\", \"test-deepseek\")"` | — |
| [SRC-E3EEC2014A-L000154](../../tests/test_workspace_discovery.py#L154) | 154 | `"    monkeypatch.setenv(\"BRAVE_SEARCH_API_KEY\", \"test-brave\")"` | — |
| [SRC-E3EEC2014A-L000155](../../tests/test_workspace_discovery.py#L155) | 155 | `"    monkeypatch.setenv(\"TAVILY_API_KEY\", \"test-tavily\")"` | — |
| [SRC-E3EEC2014A-L000156](../../tests/test_workspace_discovery.py#L156) | 156 | `"    agent = WebAgent()"` | — |
| [SRC-E3EEC2014A-L000157](../../tests/test_workspace_discovery.py#L157) | 157 | `"    agent.allow_optional_providers = False"` | — |
| [SRC-E3EEC2014A-L000158](../../tests/test_workspace_discovery.py#L158) | 158 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _query: [])"` | — |
| [SRC-E3EEC2014A-L000159](../../tests/test_workspace_discovery.py#L159) | 159 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _query: [])"` | — |
| [SRC-E3EEC2014A-L000160](../../tests/test_workspace_discovery.py#L160) | 160 | `""` | — |
| [SRC-E3EEC2014A-L000161](../../tests/test_workspace_discovery.py#L161) | 161 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-E3EEC2014A-L000162](../../tests/test_workspace_discovery.py#L162) | 162 | `"        agent._search_web(\"لوحة إنذار الحريق\")"` | — |
| [SRC-E3EEC2014A-L000163](../../tests/test_workspace_discovery.py#L163) | 163 | `""` | — |
| [SRC-E3EEC2014A-L000164](../../tests/test_workspace_discovery.py#L164) | 164 | `"    statuses = {item[\"provider\"]: item[\"status\"] for item in agent._provider_diagnostics}"` | — |
| [SRC-E3EEC2014A-L000165](../../tests/test_workspace_discovery.py#L165) | 165 | `"    assert statuses[\"deepseek_search_api\"] == \"disabled_by_request\""` | — |
| [SRC-E3EEC2014A-L000166](../../tests/test_workspace_discovery.py#L166) | 166 | `"    assert statuses[\"brave_search_api\"] == \"disabled_by_request\""` | — |
| [SRC-E3EEC2014A-L000167](../../tests/test_workspace_discovery.py#L167) | 167 | `"    assert statuses[\"tavily_search_api\"] == \"disabled_by_request\""` | — |
| [SRC-E3EEC2014A-L000168](../../tests/test_workspace_discovery.py#L168) | 168 | `""` | — |
| [SRC-E3EEC2014A-L000169](../../tests/test_workspace_discovery.py#L169) | 169 | `""` | — |
| [SRC-E3EEC2014A-L000170](../../tests/test_workspace_discovery.py#L170) | 170 | `"def test_discovery_without_optional_approval_skips_reddit_oauth_but_keeps_public_rss("` | — |
| [SRC-E3EEC2014A-L000171](../../tests/test_workspace_discovery.py#L171) | 171 | `"    monkeypatch,"` | — |
| [SRC-E3EEC2014A-L000172](../../tests/test_workspace_discovery.py#L172) | 172 | `"):"` | — |
| [SRC-E3EEC2014A-L000173](../../tests/test_workspace_discovery.py#L173) | 173 | `"    import agents.web_agent as web_agent_module"` | — |
| [SRC-E3EEC2014A-L000174](../../tests/test_workspace_discovery.py#L174) | 174 | `""` | — |
| [SRC-E3EEC2014A-L000175](../../tests/test_workspace_discovery.py#L175) | 175 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_ID\", \"configured-client-id\")"` | — |
| [SRC-E3EEC2014A-L000176](../../tests/test_workspace_discovery.py#L176) | 176 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_SECRET\", \"configured-client-secret\")"` | — |
| [SRC-E3EEC2014A-L000177](../../tests/test_workspace_discovery.py#L177) | 177 | `"    agent = WebAgent()"` | — |
| [SRC-E3EEC2014A-L000178](../../tests/test_workspace_discovery.py#L178) | 178 | `"    agent.allow_optional_providers = False"` | — |
| [SRC-E3EEC2014A-L000179](../../tests/test_workspace_discovery.py#L179) | 179 | `"    called_urls = []"` | — |
| [SRC-E3EEC2014A-L000180](../../tests/test_workspace_discovery.py#L180) | 180 | `""` | — |
| [SRC-E3EEC2014A-L000181](../../tests/test_workspace_discovery.py#L181) | 181 | `"    class FakeResponse:"` | — |
| [SRC-E3EEC2014A-L000182](../../tests/test_workspace_discovery.py#L182) | 182 | `"        status_code = 200"` | — |
| [SRC-E3EEC2014A-L000183](../../tests/test_workspace_discovery.py#L183) | 183 | `"        content = ("` | — |
| [SRC-E3EEC2014A-L000184](../../tests/test_workspace_discovery.py#L184) | 184 | `"            \"<rss><channel><item><title>طلب شراء لوحة إنذار</title>\""` | — |
| [SRC-E3EEC2014A-L000185](../../tests/test_workspace_discovery.py#L185) | 185 | `"            \"<link>https://www.reddit.com/r/example/comments/123/request</link>\""` | — |
| [SRC-E3EEC2014A-L000186](../../tests/test_workspace_discovery.py#L186) | 186 | `"            \"<description>نبحث عن مورد للوحة إنذار حريق.</description>\""` | — |
| [SRC-E3EEC2014A-L000187](../../tests/test_workspace_discovery.py#L187) | 187 | `"            \"<pubDate>Fri, 06 Nov 2026 08:00:00 GMT</pubDate>\""` | — |
| [SRC-E3EEC2014A-L000188](../../tests/test_workspace_discovery.py#L188) | 188 | `"            \"</item></channel></rss>\""` | — |
| [SRC-E3EEC2014A-L000189](../../tests/test_workspace_discovery.py#L189) | 189 | `"        ).encode()"` | — |
| [SRC-E3EEC2014A-L000190](../../tests/test_workspace_discovery.py#L190) | 190 | `""` | — |
| [SRC-E3EEC2014A-L000191](../../tests/test_workspace_discovery.py#L191) | 191 | `"    def fake_request(method, url, **kwargs):"` | — |
| [SRC-E3EEC2014A-L000192](../../tests/test_workspace_discovery.py#L192) | 192 | `"        called_urls.append(url)"` | — |
| [SRC-E3EEC2014A-L000193](../../tests/test_workspace_discovery.py#L193) | 193 | `"        if url != \"https://www.reddit.com/search.rss\":"` | — |
| [SRC-E3EEC2014A-L000194](../../tests/test_workspace_discovery.py#L194) | 194 | `"            raise AssertionError(\"quota-backed Reddit OAuth must stay disabled\")"` | — |
| [SRC-E3EEC2014A-L000195](../../tests/test_workspace_discovery.py#L195) | 195 | `"        return FakeResponse()"` | — |
| [SRC-E3EEC2014A-L000196](../../tests/test_workspace_discovery.py#L196) | 196 | `""` | — |
| [SRC-E3EEC2014A-L000197](../../tests/test_workspace_discovery.py#L197) | 197 | `"    monkeypatch.setattr(web_agent_module, \"_bounded_http_request\", fake_request)"` | — |
| [SRC-E3EEC2014A-L000198](../../tests/test_workspace_discovery.py#L198) | 198 | `"    results, _warnings = agent._search_social(\"لوحة إنذار حريق\", [\"reddit\"])"` | — |
| [SRC-E3EEC2014A-L000199](../../tests/test_workspace_discovery.py#L199) | 199 | `""` | — |
| [SRC-E3EEC2014A-L000200](../../tests/test_workspace_discovery.py#L200) | 200 | `"    assert called_urls == [\"https://www.reddit.com/search.rss\"]"` | — |
| [SRC-E3EEC2014A-L000201](../../tests/test_workspace_discovery.py#L201) | 201 | `"    assert results and results[0][\"provider\"] == \"reddit_public_rss\""` | — |
| [SRC-E3EEC2014A-L000202](../../tests/test_workspace_discovery.py#L202) | 202 | `""` | — |
| [SRC-E3EEC2014A-L000203](../../tests/test_workspace_discovery.py#L203) | 203 | `""` | — |
| [SRC-E3EEC2014A-L000204](../../tests/test_workspace_discovery.py#L204) | 204 | `"@pytest.mark.parametrize("` | — |
| [SRC-E3EEC2014A-L000205](../../tests/test_workspace_discovery.py#L205) | 205 | `"    \"url\","` | — |
| [SRC-E3EEC2014A-L000206](../../tests/test_workspace_discovery.py#L206) | 206 | `"    ["` | — |
| [SRC-E3EEC2014A-L000207](../../tests/test_workspace_discovery.py#L207) | 207 | `"        \"http://localhost/private\","` | — |
| [SRC-E3EEC2014A-L000208](../../tests/test_workspace_discovery.py#L208) | 208 | `"        \"http://service.localhost/private\","` | — |
| [SRC-E3EEC2014A-L000209](../../tests/test_workspace_discovery.py#L209) | 209 | `"        \"http://service.local/private\","` | — |
| [SRC-E3EEC2014A-L000210](../../tests/test_workspace_discovery.py#L210) | 210 | `"        \"http://127.0.0.1/private\","` | — |
| [SRC-E3EEC2014A-L000211](../../tests/test_workspace_discovery.py#L211) | 211 | `"        \"http://10.0.0.8/private\","` | — |
| [SRC-E3EEC2014A-L000212](../../tests/test_workspace_discovery.py#L212) | 212 | `"        \"http://192.168.1.2/private\","` | — |
| [SRC-E3EEC2014A-L000213](../../tests/test_workspace_discovery.py#L213) | 213 | `"        \"http://[::1]/private\","` | — |
| [SRC-E3EEC2014A-L000214](../../tests/test_workspace_discovery.py#L214) | 214 | `"        \"http://[fd00::1]/private\","` | — |
| [SRC-E3EEC2014A-L000215](../../tests/test_workspace_discovery.py#L215) | 215 | `"    ],"` | — |
| [SRC-E3EEC2014A-L000216](../../tests/test_workspace_discovery.py#L216) | 216 | `")"` | — |
| [SRC-E3EEC2014A-L000217](../../tests/test_workspace_discovery.py#L217) | 217 | `"def test_discovery_source_storage_rejects_non_public_hosts(url):"` | — |
| [SRC-E3EEC2014A-L000218](../../tests/test_workspace_discovery.py#L218) | 218 | `"    with pytest.raises(ValueError, match=\"not public\"):"` | — |
| [SRC-E3EEC2014A-L000219](../../tests/test_workspace_discovery.py#L219) | 219 | `"        LeadStore._safe_discovery_source("` | — |
| [SRC-E3EEC2014A-L000220](../../tests/test_workspace_discovery.py#L220) | 220 | `"            {"` | — |
| [SRC-E3EEC2014A-L000221](../../tests/test_workspace_discovery.py#L221) | 221 | `"                \"title\": \"Private target\","` | — |
| [SRC-E3EEC2014A-L000222](../../tests/test_workspace_discovery.py#L222) | 222 | `"                \"url\": url,"` | — |
| [SRC-E3EEC2014A-L000223](../../tests/test_workspace_discovery.py#L223) | 223 | `"                \"snippet\": \"not a public result\","` | — |
| [SRC-E3EEC2014A-L000224](../../tests/test_workspace_discovery.py#L224) | 224 | `"                \"lead_qualification\": \"related_result_not_lead\","` | — |
| [SRC-E3EEC2014A-L000225](../../tests/test_workspace_discovery.py#L225) | 225 | `"            }"` | — |
| [SRC-E3EEC2014A-L000226](../../tests/test_workspace_discovery.py#L226) | 226 | `"        )"` | — |
| [SRC-E3EEC2014A-L000227](../../tests/test_workspace_discovery.py#L227) | 227 | `""` | — |
| [SRC-E3EEC2014A-L000228](../../tests/test_workspace_discovery.py#L228) | 228 | `""` | — |
| [SRC-E3EEC2014A-L000229](../../tests/test_workspace_discovery.py#L229) | 229 | `"def test_discovery_source_storage_accepts_public_http_source():"` | — |
| [SRC-E3EEC2014A-L000230](../../tests/test_workspace_discovery.py#L230) | 230 | `"    source = LeadStore._safe_discovery_source("` | — |
| [SRC-E3EEC2014A-L000231](../../tests/test_workspace_discovery.py#L231) | 231 | `"        {"` | — |
| [SRC-E3EEC2014A-L000232](../../tests/test_workspace_discovery.py#L232) | 232 | `"            \"title\": \"Public result\","` | — |
| [SRC-E3EEC2014A-L000233](../../tests/test_workspace_discovery.py#L233) | 233 | `"            \"url\": \"https://example.org/request\","` | — |
| [SRC-E3EEC2014A-L000234](../../tests/test_workspace_discovery.py#L234) | 234 | `"            \"snippet\": \"public source\","` | — |
| [SRC-E3EEC2014A-L000235](../../tests/test_workspace_discovery.py#L235) | 235 | `"            \"lead_qualification\": \"related_result_not_lead\","` | — |
| [SRC-E3EEC2014A-L000236](../../tests/test_workspace_discovery.py#L236) | 236 | `"        }"` | — |
| [SRC-E3EEC2014A-L000237](../../tests/test_workspace_discovery.py#L237) | 237 | `"    )"` | — |
| [SRC-E3EEC2014A-L000238](../../tests/test_workspace_discovery.py#L238) | 238 | `"    assert source[\"url\"] == \"https://example.org/request\""` | — |
## اختبارات

### FILE-F7BF7F2B46 — [tests/test_workspace_ui_regressions.py](../../tests/test_workspace_ui_regressions.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F7BF7F2B46-L000001](../../tests/test_workspace_ui_regressions.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-F7BF7F2B46-L000002](../../tests/test_workspace_ui_regressions.py#L2) | 2 | `""` | — |
| [SRC-F7BF7F2B46-L000003](../../tests/test_workspace_ui_regressions.py#L3) | 3 | `"import re"` | — |
| [SRC-F7BF7F2B46-L000004](../../tests/test_workspace_ui_regressions.py#L4) | 4 | `"from pathlib import Path"` | — |
| [SRC-F7BF7F2B46-L000005](../../tests/test_workspace_ui_regressions.py#L5) | 5 | `""` | — |
| [SRC-F7BF7F2B46-L000006](../../tests/test_workspace_ui_regressions.py#L6) | 6 | `""` | — |
| [SRC-F7BF7F2B46-L000007](../../tests/test_workspace_ui_regressions.py#L7) | 7 | `"ROOT = Path(__file__).resolve().parents[1] / \"web\""` | — |
| [SRC-F7BF7F2B46-L000008](../../tests/test_workspace_ui_regressions.py#L8) | 8 | `""` | — |
| [SRC-F7BF7F2B46-L000009](../../tests/test_workspace_ui_regressions.py#L9) | 9 | `""` | — |
| [SRC-F7BF7F2B46-L000010](../../tests/test_workspace_ui_regressions.py#L10) | 10 | `"def inline_script(name: str) -> str:"` | — |
| [SRC-F7BF7F2B46-L000011](../../tests/test_workspace_ui_regressions.py#L11) | 11 | `"    html = (ROOT / name).read_text(encoding=\"utf-8\")"` | — |
| [SRC-F7BF7F2B46-L000012](../../tests/test_workspace_ui_regressions.py#L12) | 12 | `"    scripts = re.findall(r\"<script[^>]*>([\\s\\S]*?)</script\\s*>\", html, re.IGNORECASE)"` | — |
| [SRC-F7BF7F2B46-L000013](../../tests/test_workspace_ui_regressions.py#L13) | 13 | `"    assert scripts, f\"{name} must contain its application script\""` | — |
| [SRC-F7BF7F2B46-L000014](../../tests/test_workspace_ui_regressions.py#L14) | 14 | `"    return \"\\n\".join(scripts)"` | — |
| [SRC-F7BF7F2B46-L000015](../../tests/test_workspace_ui_regressions.py#L15) | 15 | `""` | — |
| [SRC-F7BF7F2B46-L000016](../../tests/test_workspace_ui_regressions.py#L16) | 16 | `""` | — |
| [SRC-F7BF7F2B46-L000017](../../tests/test_workspace_ui_regressions.py#L17) | 17 | `"def function_source(script: str, name: str) -> str:"` | — |
| [SRC-F7BF7F2B46-L000018](../../tests/test_workspace_ui_regressions.py#L18) | 18 | `"    match = re.search("` | — |
| [SRC-F7BF7F2B46-L000019](../../tests/test_workspace_ui_regressions.py#L19) | 19 | `"        rf\"(?:async\\s+)?function\\s+{re.escape(name)}\\s*\\([^)]*\\)\\s*\\{{\","` | — |
| [SRC-F7BF7F2B46-L000020](../../tests/test_workspace_ui_regressions.py#L20) | 20 | `"        script,"` | — |
| [SRC-F7BF7F2B46-L000021](../../tests/test_workspace_ui_regressions.py#L21) | 21 | `"    )"` | — |
| [SRC-F7BF7F2B46-L000022](../../tests/test_workspace_ui_regressions.py#L22) | 22 | `"    assert match, f\"function {name} must exist\""` | — |
| [SRC-F7BF7F2B46-L000023](../../tests/test_workspace_ui_regressions.py#L23) | 23 | `"    next_function = re.search("` | — |
| [SRC-F7BF7F2B46-L000024](../../tests/test_workspace_ui_regressions.py#L24) | 24 | `"        r\"\\n(?:async\\s+)?function\\s+[A-Za-z_$]\", script[match.end():]"` | — |
| [SRC-F7BF7F2B46-L000025](../../tests/test_workspace_ui_regressions.py#L25) | 25 | `"    )"` | — |
| [SRC-F7BF7F2B46-L000026](../../tests/test_workspace_ui_regressions.py#L26) | 26 | `"    end = match.end() + next_function.start() if next_function else len(script)"` | — |
| [SRC-F7BF7F2B46-L000027](../../tests/test_workspace_ui_regressions.py#L27) | 27 | `"    return script[match.start():end]"` | — |
| [SRC-F7BF7F2B46-L000028](../../tests/test_workspace_ui_regressions.py#L28) | 28 | `""` | — |
| [SRC-F7BF7F2B46-L000029](../../tests/test_workspace_ui_regressions.py#L29) | 29 | `""` | — |
| [SRC-F7BF7F2B46-L000030](../../tests/test_workspace_ui_regressions.py#L30) | 30 | `"def test_workspace_api_forwards_optional_abort_signal_to_fetch():"` | — |
| [SRC-F7BF7F2B46-L000031](../../tests/test_workspace_ui_regressions.py#L31) | 31 | `"    body = function_source(inline_script(\"workspace.html\"), \"api\")"` | — |
| [SRC-F7BF7F2B46-L000032](../../tests/test_workspace_ui_regressions.py#L32) | 32 | `"    assert re.search(r\"signal\\s*:\\s*opts\\.signal\", body)"` | — |
| [SRC-F7BF7F2B46-L000033](../../tests/test_workspace_ui_regressions.py#L33) | 33 | `""` | — |
| [SRC-F7BF7F2B46-L000034](../../tests/test_workspace_ui_regressions.py#L34) | 34 | `""` | — |
| [SRC-F7BF7F2B46-L000035](../../tests/test_workspace_ui_regressions.py#L35) | 35 | `"def test_workspace_chat_uses_bounded_abort_and_restores_chat_state():"` | — |
| [SRC-F7BF7F2B46-L000036](../../tests/test_workspace_ui_regressions.py#L36) | 36 | `"    body = function_source(inline_script(\"workspace.html\"), \"sendChat\")"` | — |
| [SRC-F7BF7F2B46-L000037](../../tests/test_workspace_ui_regressions.py#L37) | 37 | `"    assert \"new AbortController()\" in body"` | — |
| [SRC-F7BF7F2B46-L000038](../../tests/test_workspace_ui_regressions.py#L38) | 38 | `"    assert re.search(r\"signal\\s*:\\s*controller\\.signal\", body)"` | — |
| [SRC-F7BF7F2B46-L000039](../../tests/test_workspace_ui_regressions.py#L39) | 39 | `"    assert re.search(r\"window\\.setTimeout\\s*\\(.*controller\\.abort\", body, re.DOTALL)"` | — |
| [SRC-F7BF7F2B46-L000040](../../tests/test_workspace_ui_regressions.py#L40) | 40 | `"    assert \"window.clearTimeout(timeoutId)\" in body"` | — |
| [SRC-F7BF7F2B46-L000041](../../tests/test_workspace_ui_regressions.py#L41) | 41 | `"    assert \"انتهى وقت انتظار الواجهة بعد 135 ثانية\" in body"` | — |
| [SRC-F7BF7F2B46-L000042](../../tests/test_workspace_ui_regressions.py#L42) | 42 | `"    assert \"قد يواصل الخادم إنهاء العملية\" in body"` | — |
| [SRC-F7BF7F2B46-L000043](../../tests/test_workspace_ui_regressions.py#L43) | 43 | `"    assert \"if(chat.busy)return\" in body"` | — |
| [SRC-F7BF7F2B46-L000044](../../tests/test_workspace_ui_regressions.py#L44) | 44 | `"    assert \"chat.busy=false\" in body"` | — |
| [SRC-F7BF7F2B46-L000045](../../tests/test_workspace_ui_regressions.py#L45) | 45 | `""` | — |
| [SRC-F7BF7F2B46-L000046](../../tests/test_workspace_ui_regressions.py#L46) | 46 | `""` | — |
| [SRC-F7BF7F2B46-L000047](../../tests/test_workspace_ui_regressions.py#L47) | 47 | `"def test_legacy_agent_search_uses_bounded_abort_and_restores_controls():"` | — |
| [SRC-F7BF7F2B46-L000048](../../tests/test_workspace_ui_regressions.py#L48) | 48 | `"    body = function_source(inline_script(\"agent.html\"), \"ask\")"` | — |
| [SRC-F7BF7F2B46-L000049](../../tests/test_workspace_ui_regressions.py#L49) | 49 | `"    assert \"new AbortController()\" in body"` | — |
| [SRC-F7BF7F2B46-L000050](../../tests/test_workspace_ui_regressions.py#L50) | 50 | `"    assert re.search(r\"signal\\s*:\\s*controller\\.signal\", body)"` | — |
| [SRC-F7BF7F2B46-L000051](../../tests/test_workspace_ui_regressions.py#L51) | 51 | `"    assert re.search(r\"window\\.setTimeout\\s*\\(.*controller\\.abort\", body, re.DOTALL)"` | — |
| [SRC-F7BF7F2B46-L000052](../../tests/test_workspace_ui_regressions.py#L52) | 52 | `"    assert \"window.clearTimeout(timeoutId)\" in body"` | — |
| [SRC-F7BF7F2B46-L000053](../../tests/test_workspace_ui_regressions.py#L53) | 53 | `"    assert \"انتهى وقت انتظار الواجهة بعد 135 ثانية\" in body"` | — |
| [SRC-F7BF7F2B46-L000054](../../tests/test_workspace_ui_regressions.py#L54) | 54 | `"    assert \"قد يواصل الخادم إنهاء العملية\" in body"` | — |
| [SRC-F7BF7F2B46-L000055](../../tests/test_workspace_ui_regressions.py#L55) | 55 | `"    assert \"setBusy(false)\" in body"` | — |
| [SRC-F7BF7F2B46-L000056](../../tests/test_workspace_ui_regressions.py#L56) | 56 | `""` | — |
| [SRC-F7BF7F2B46-L000057](../../tests/test_workspace_ui_regressions.py#L57) | 57 | `""` | — |
| [SRC-F7BF7F2B46-L000058](../../tests/test_workspace_ui_regressions.py#L58) | 58 | `"def test_signal_inbox_refresh_surfaces_errors_and_restores_button():"` | — |
| [SRC-F7BF7F2B46-L000059](../../tests/test_workspace_ui_regressions.py#L59) | 59 | `"    body = function_source(inline_script(\"workspace.html\"), \"renderSignals\")"` | — |
| [SRC-F7BF7F2B46-L000060](../../tests/test_workspace_ui_regressions.py#L60) | 60 | `"    assert \"refresh.disabled=true\" in body"` | — |
| [SRC-F7BF7F2B46-L000061](../../tests/test_workspace_ui_regressions.py#L61) | 61 | `"    assert \"تعذر تحديث إشارات الطلب\" in body"` | — |
| [SRC-F7BF7F2B46-L000062](../../tests/test_workspace_ui_regressions.py#L62) | 62 | `"    assert \"البيانات المعروضة هي آخر نسخة تم تحميلها\" in body"` | — |
| [SRC-F7BF7F2B46-L000063](../../tests/test_workspace_ui_regressions.py#L63) | 63 | `"    assert \"catch(error)\" in body"` | — |
| [SRC-F7BF7F2B46-L000064](../../tests/test_workspace_ui_regressions.py#L64) | 64 | `"    assert \"refresh.disabled=false\" in body"` | — |
| [SRC-F7BF7F2B46-L000065](../../tests/test_workspace_ui_regressions.py#L65) | 65 | `""` | — |
| [SRC-F7BF7F2B46-L000066](../../tests/test_workspace_ui_regressions.py#L66) | 66 | `""` | — |
| [SRC-F7BF7F2B46-L000067](../../tests/test_workspace_ui_regressions.py#L67) | 67 | `"def test_manual_signal_save_distinguishes_saved_from_refresh_failure():"` | — |
| [SRC-F7BF7F2B46-L000068](../../tests/test_workspace_ui_regressions.py#L68) | 68 | `"    body = function_source(inline_script(\"workspace.html\"), \"createSignalForm\")"` | — |
| [SRC-F7BF7F2B46-L000069](../../tests/test_workspace_ui_regressions.py#L69) | 69 | `"    assert \"refreshWarning\" in body"` | — |
| [SRC-F7BF7F2B46-L000070](../../tests/test_workspace_ui_regressions.py#L70) | 70 | `"    assert \"تم حفظ الإشارة، لكن تعذر تحديث صندوق الإشارات\" in body"` | — |
| [SRC-F7BF7F2B46-L000071](../../tests/test_workspace_ui_regressions.py#L71) | 71 | `""` | — |
| [SRC-F7BF7F2B46-L000072](../../tests/test_workspace_ui_regressions.py#L72) | 72 | `""` | — |
| [SRC-F7BF7F2B46-L000073](../../tests/test_workspace_ui_regressions.py#L73) | 73 | `"def test_product_profile_save_distinguishes_saved_from_refresh_failure():"` | — |
| [SRC-F7BF7F2B46-L000074](../../tests/test_workspace_ui_regressions.py#L74) | 74 | `"    body = function_source(inline_script(\"workspace.html\"), \"renderProductProfile\")"` | — |
| [SRC-F7BF7F2B46-L000075](../../tests/test_workspace_ui_regressions.py#L75) | 75 | `"    assert \"refreshWarning\" in body"` | — |
| [SRC-F7BF7F2B46-L000076](../../tests/test_workspace_ui_regressions.py#L76) | 76 | `"    assert \"تم حفظ ملف المنتج والسوق، لكن تعذر تحديث قائمة الملفات المحفوظة\" in body"` | — |
| [SRC-F7BF7F2B46-L000077](../../tests/test_workspace_ui_regressions.py#L77) | 77 | `""` | — |
| [SRC-F7BF7F2B46-L000078](../../tests/test_workspace_ui_regressions.py#L78) | 78 | `""` | — |
| [SRC-F7BF7F2B46-L000079](../../tests/test_workspace_ui_regressions.py#L79) | 79 | `"def test_discovery_signal_save_distinguishes_saved_from_refresh_failure():"` | — |
| [SRC-F7BF7F2B46-L000080](../../tests/test_workspace_ui_regressions.py#L80) | 80 | `"    body = function_source(inline_script(\"workspace.html\"), \"renderDiscoveryRun\")"` | — |
| [SRC-F7BF7F2B46-L000081](../../tests/test_workspace_ui_regressions.py#L81) | 81 | `"    assert \"refreshWarning\" in body"` | — |
| [SRC-F7BF7F2B46-L000082](../../tests/test_workspace_ui_regressions.py#L82) | 82 | `"    assert \"تم حفظ الإشارة، لكن تعذر تحديث صندوق الإشارات\" in body"` | — |
| [SRC-F7BF7F2B46-L000083](../../tests/test_workspace_ui_regressions.py#L83) | 83 | `""` | — |
| [SRC-F7BF7F2B46-L000084](../../tests/test_workspace_ui_regressions.py#L84) | 84 | `""` | — |
| [SRC-F7BF7F2B46-L000085](../../tests/test_workspace_ui_regressions.py#L85) | 85 | `"def test_discovery_history_refresh_failure_keeps_the_saved_run_visible():"` | — |
| [SRC-F7BF7F2B46-L000086](../../tests/test_workspace_ui_regressions.py#L86) | 86 | `"    body = function_source(inline_script(\"workspace.html\"), \"renderDiscovery\")"` | — |
| [SRC-F7BF7F2B46-L000087](../../tests/test_workspace_ui_regressions.py#L87) | 87 | `"    assert \"state.activeDiscovery=savedRun\" in body"` | — |
| [SRC-F7BF7F2B46-L000088](../../tests/test_workspace_ui_regressions.py#L88) | 88 | `"    assert \"refreshWarning\" in body"` | — |
| [SRC-F7BF7F2B46-L000089](../../tests/test_workspace_ui_regressions.py#L89) | 89 | `"    assert \"تعذر تحديث سجل العمليات\" in body"` | — |
| [SRC-F7BF7F2B46-L000090](../../tests/test_workspace_ui_regressions.py#L90) | 90 | `""` | — |
| [SRC-F7BF7F2B46-L000091](../../tests/test_workspace_ui_regressions.py#L91) | 91 | `""` | — |
| [SRC-F7BF7F2B46-L000092](../../tests/test_workspace_ui_regressions.py#L92) | 92 | `"def test_workspace_chat_links_each_inline_citation_to_its_exact_source_index():"` | — |
| [SRC-F7BF7F2B46-L000093](../../tests/test_workspace_ui_regressions.py#L93) | 93 | `"    script = inline_script(\"workspace.html\")"` | — |
| [SRC-F7BF7F2B46-L000094](../../tests/test_workspace_ui_regressions.py#L94) | 94 | `"    renderer = function_source(script, \"appendCitedAnswer\")"` | — |
| [SRC-F7BF7F2B46-L000095](../../tests/test_workspace_ui_regressions.py#L95) | 95 | `"    message = function_source(script, \"chatMessageNode\")"` | — |
| [SRC-F7BF7F2B46-L000096](../../tests/test_workspace_ui_regressions.py#L96) | 96 | `"    assert \"sources[index-1]\" in renderer"` | — |
| [SRC-F7BF7F2B46-L000097](../../tests/test_workspace_ui_regressions.py#L97) | 97 | `"    assert \"safeHttp(source.url)\" in renderer"` | — |
| [SRC-F7BF7F2B46-L000098](../../tests/test_workspace_ui_regressions.py#L98) | 98 | `"    assert \"document.createTextNode\" in renderer"` | — |
| [SRC-F7BF7F2B46-L000099](../../tests/test_workspace_ui_regressions.py#L99) | 99 | `"    assert \"chat-citation\" in renderer"` | — |
| [SRC-F7BF7F2B46-L000100](../../tests/test_workspace_ui_regressions.py#L100) | 100 | `"    assert \"appendCitedAnswer\" in message"` | — |
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
| [SRC-DE7EABE998-L000045](../../web/agent.html#L45) | 45 | `"<a class=\"ghost\" href=\"/workspace\">مساحة عمل المبيعات ↗</a></header>"` | — |
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
| [SRC-DE7EABE998-L000073](../../web/agent.html#L73) | 73 | `"      <button id=\"saveAccessToken\" type=\"button\" class=\"ghost checkbutton\">تسجيل الدخول</button>"` | — |
| [SRC-DE7EABE998-L000074](../../web/agent.html#L74) | 74 | `"      <button id=\"logoutSession\" type=\"button\" class=\"ghost checkbutton\">تسجيل الخروج</button>"` | — |
| [SRC-DE7EABE998-L000075](../../web/agent.html#L75) | 75 | `"      <p id=\"authStatus\" style=\"font-size:10px;color:var(--muted);line-height:1.8;margin-top:7px\" aria-live=\"polite\">لا يُحفظ رمز الوصول في تخزين JavaScript؛ بعد الدخول يستخدم المتصفح ملف ارتباط HttpOnly محدود المدة.</p>"` | — |
| [SRC-DE7EABE998-L000076](../../web/agent.html#L76) | 76 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000077](../../web/agent.html#L77) | 77 | `"    <div class=\"sideblock\">"` | — |
| [SRC-DE7EABE998-L000078](../../web/agent.html#L78) | 78 | `"      <h3>حالة الاتصال الفعلية</h3>"` | — |
| [SRC-DE7EABE998-L000079](../../web/agent.html#L79) | 79 | `"      <p id=\"setupStatus\">جارٍ فحص إعدادات الخادم. إعداد المحرك لا يعني أن البحث الحي نجح بعد؛ استخدم الاختبار أدناه للتحقق من الاتصال الفعلي.</p>"` | — |
| [SRC-DE7EABE998-L000080](../../web/agent.html#L80) | 80 | `"      <label style=\"display:flex;gap:8px;align-items:flex-start;margin:11px 0;font-size:10px;color:#b9c9dc;line-height:1.7\"><input id=\"diagSocial\" type=\"checkbox\" style=\"margin-top:3px\"> اختبار المصادر الاجتماعية العامة والموصلات المهيأة أيضًا</label>"` | — |
| [SRC-DE7EABE998-L000081](../../web/agent.html#L81) | 81 | `"      <button id=\"runDiagnostics\" type=\"button\" class=\"primary checkbutton\">اختبار حي للإنترنت والنموذج</button>"` | — |
| [SRC-DE7EABE998-L000082](../../web/agent.html#L82) | 82 | `"      <p id=\"diagnosticsResult\" class=\"diag\" aria-live=\"polite\"></p>"` | — |
| [SRC-DE7EABE998-L000083](../../web/agent.html#L83) | 83 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000084](../../web/agent.html#L84) | 84 | `"    <div class=\"sideblock\">"` | — |
| [SRC-DE7EABE998-L000085](../../web/agent.html#L85) | 85 | `"      <h3>مصادر البحث</h3>"` | — |
| [SRC-DE7EABE998-L000086](../../web/agent.html#L86) | 86 | `"      <div class=\"sidefeature\"><div class=\"sideicon\">⌕</div><div><b>محركات الويب</b><span>DuckDuckGo وBing؛ ويمكن إضافة Brave وTavily بمفتاح API اختياري.</span></div></div>"` | — |
| [SRC-DE7EABE998-L000087](../../web/agent.html#L87) | 87 | `"      <div class=\"sidefeature\"><div class=\"sideicon\">▤</div><div><b>الأخبار والمصادر العامة</b><span>Google News عند طلب معلومات حديثة، وقراءة الصفحات التي تسمح بالوصول العام.</span></div></div>"` | — |
| [SRC-DE7EABE998-L000088](../../web/agent.html#L88) | 88 | `"      <div class=\"sidefeature\"><div class=\"sideicon\">◎</div><div><b>الشبكات الاجتماعية</b><span>مصادر عامة موصولة فعليًا أو نتائج مفهرسة؛ ليست تغطية كاملة لكل المنصات أو المنشورات.</span></div></div>"` | — |
| [SRC-DE7EABE998-L000089](../../web/agent.html#L89) | 89 | `"      <div id=\"providerSetup\"></div>"` | — |
| [SRC-DE7EABE998-L000090](../../web/agent.html#L90) | 90 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000091](../../web/agent.html#L91) | 91 | `"    <div class=\"sideblock\">"` | — |
| [SRC-DE7EABE998-L000092](../../web/agent.html#L92) | 92 | `"      <h3>كيف تقرأ النتيجة؟</h3>"` | — |
| [SRC-DE7EABE998-L000093](../../web/agent.html#L93) | 93 | `"      <p>تنوع النطاقات ومحركات البحث والصفحات المقروءة وتواريخ النشر إشارات إلى مدى تغطية البحث، لا دليلًا قاطعًا على صحة الادعاء. افتح المصادر المهمة، وانتبه إلى التضارب والمعلومات غير المؤرخة.</p>"` | — |
| [SRC-DE7EABE998-L000094](../../web/agent.html#L94) | 94 | `"    </div>"` | — |
| [SRC-DE7EABE998-L000095](../../web/agent.html#L95) | 95 | `"  </aside>"` | — |
| [SRC-DE7EABE998-L000096](../../web/agent.html#L96) | 96 | `"</main>"` | — |
| [SRC-DE7EABE998-L000097](../../web/agent.html#L97) | 97 | `"<footer class=\"foot\">Omarai · لا يتجاوز تسجيل الدخول أو الصفحات الخاصة أو الحواجز المدفوعة، ولا يرسل رسائل تلقائية. الإتاحة الفعلية تعتمد على اتصال الإنترنت، وحدود محركات البحث، ومفاتيح الخدمات الاختيارية.</footer>"` | — |
| [SRC-DE7EABE998-L000098](../../web/agent.html#L98) | 98 | `"</div>"` | — |
| [SRC-DE7EABE998-L000099](../../web/agent.html#L99) | 99 | `""` | — |
| [SRC-DE7EABE998-L000100](../../web/agent.html#L100) | 100 | `"<script>"` | — |
| [SRC-DE7EABE998-L000101](../../web/agent.html#L101) | 101 | `"const $=id=>document.getElementById(id);"` | — |
| [SRC-DE7EABE998-L000102](../../web/agent.html#L102) | 102 | `"function apiHeaders(){return {\"Content-Type\":\"application/json\"};}"` | — |
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
| [SRC-DE7EABE998-L000156](../../web/agent.html#L156) | 156 | `" if(s.lead_qualification===\"public_demand_signal\"\|\|s.lead_qualification===\"public_buyer_intent_signal\"){"` | — |
| [SRC-DE7EABE998-L000157](../../web/agent.html#L157) | 157 | `"  const demandType=s.lead_intent_evidence&&s.lead_intent_evidence.signal_type;"` | — |
| [SRC-DE7EABE998-L000158](../../web/agent.html#L158) | 158 | `"  const demandLabels={direct_purchase_request:\"طلب شراء مباشر\",request_for_quotation:\"طلب عرض سعر\",tender_or_procurement:\"مناقصة أو توريد\",stated_need:\"احتياج معلن\",indirect_indicator:\"مؤشر احتياج غير مباشر\"};"` | — |
| [SRC-DE7EABE998-L000159](../../web/agent.html#L159) | 159 | `"  const demandLabel=demandLabels[demandType]\|\|\"إشارة طلب غير مكتملة التصنيف\";"` | — |
| [SRC-DE7EABE998-L000160](../../web/agent.html#L160) | 160 | `"  tags.push('<span class=\"tag read\">'+escapeHtml(demandLabel)+' — ملاءمة المنتج والهوية تحتاج إلى تحقق</span>');"` | — |
| [SRC-DE7EABE998-L000161](../../web/agent.html#L161) | 161 | `" }"` | — |
| [SRC-DE7EABE998-L000162](../../web/agent.html#L162) | 162 | `" const heading=url?'<a href=\"'+escapeHtml(url)+'\" target=\"_blank\" rel=\"noopener noreferrer\">['+(index+1)+'] '+title+' ↗</a>':'<strong>['+(index+1)+'] '+title+'</strong><p class=\"warning\">لم يُعرض الرابط لأنه غير صالح.</p>';"` | — |
| [SRC-DE7EABE998-L000163](../../web/agent.html#L163) | 163 | `" return '<article class=\"source\">'+heading+'<p>'+escapeHtml(s.snippet\|\|\"لا يتوفر مقتطف نصي من هذه النتيجة.\")+'</p><div class=\"source-meta\">'+tags.join(\"\")+'</div></article>';"` | — |
| [SRC-DE7EABE998-L000164](../../web/agent.html#L164) | 164 | `"}"` | — |
| [SRC-DE7EABE998-L000165](../../web/agent.html#L165) | 165 | `"function renderReport(result){"` | — |
| [SRC-DE7EABE998-L000166](../../web/agent.html#L166) | 166 | `" const r=result&&result.search_report&&typeof result.search_report===\"object\"?result.search_report:{};"` | — |
| [SRC-DE7EABE998-L000167](../../web/agent.html#L167) | 167 | `" const completion=r.research_completion&&typeof r.research_completion===\"object\"?r.research_completion:"` | — |
| [SRC-DE7EABE998-L000168](../../web/agent.html#L168) | 168 | `"  (result&&result.research_completion&&typeof result.research_completion===\"object\"?result.research_completion:null);"` | — |
| [SRC-DE7EABE998-L000169](../../web/agent.html#L169) | 169 | `" const completionStatusLabels={"` | — |
| [SRC-DE7EABE998-L000170](../../web/agent.html#L170) | 170 | `"  execution_stopped_budget:\"توقفت العملية عند حد الميزانية\","` | — |
| [SRC-DE7EABE998-L000171](../../web/agent.html#L171) | 171 | `"  no_eligible_sources_after_filtering:\"لم يبقَ مصدر مقبول بعد التصفية\","` | — |
| [SRC-DE7EABE998-L000172](../../web/agent.html#L172) | 172 | `"  search_failed_or_incomplete:\"البحث فشل أو لم يكتمل\","` | — |
| [SRC-DE7EABE998-L000173](../../web/agent.html#L173) | 173 | `"  no_results_returned:\"اكتمل البحث دون نتائج\","` | — |
| [SRC-DE7EABE998-L000174](../../web/agent.html#L174) | 174 | `"  search_not_attempted:\"لم تُنفذ محاولة البحث\","` | — |
| [SRC-DE7EABE998-L000175](../../web/agent.html#L175) | 175 | `"  insufficient_evidence:\"الأدلة غير كافية\","` | — |
| [SRC-DE7EABE998-L000176](../../web/agent.html#L176) | 176 | `"  source_snippets_only_generation_not_completed:\"مقتطفات فقط؛ لم تكتمل صياغة الإجابة\","` | — |
| [SRC-DE7EABE998-L000177](../../web/agent.html#L177) | 177 | `"  evidence_collected_generation_not_completed:\"جُمعت أدلة؛ لم تكتمل صياغة الإجابة\","` | — |
| [SRC-DE7EABE998-L000178](../../web/agent.html#L178) | 178 | `"  answer_generation_or_review_failed:\"تعذر توليد الإجابة أو مراجعتها\","` | — |
| [SRC-DE7EABE998-L000179](../../web/agent.html#L179) | 179 | `"  partial_answer_evidence_gaps_detected:\"إجابة جزئية مع فجوات أدلة محتملة\","` | — |
| [SRC-DE7EABE998-L000180](../../web/agent.html#L180) | 180 | `"  answer_generated_citations_range_checked_semantic_support_unverified:\"وُلّدت الإجابة وفُحصت أرقام الإحالات فقط؛ دعم الادعاءات دلاليًا غير متحقق\","` | — |
| [SRC-DE7EABE998-L000181](../../web/agent.html#L181) | 181 | `"  answer_generated_without_valid_citation_markers:\"وُلّدت الإجابة دون علامات إحالة صالحة\""` | — |
| [SRC-DE7EABE998-L000182](../../web/agent.html#L182) | 182 | `" };"` | — |
| [SRC-DE7EABE998-L000183](../../web/agent.html#L183) | 183 | `" const completionPhaseLabels={"` | — |
| [SRC-DE7EABE998-L000184](../../web/agent.html#L184) | 184 | `"  planning:\"التخطيط\",search:\"البحث\",source_filtering:\"تصفية المصادر\","` | — |
| [SRC-DE7EABE998-L000185](../../web/agent.html#L185) | 185 | `"  page_reading:\"قراءة الصفحات\",answer_generation:\"توليد الإجابة\","` | — |
| [SRC-DE7EABE998-L000186](../../web/agent.html#L186) | 186 | `"  citation_validation:\"فحص الإحالات\",semantic_verification:\"التحقق الدلالي\""` | — |
| [SRC-DE7EABE998-L000187](../../web/agent.html#L187) | 187 | `" };"` | — |
| [SRC-DE7EABE998-L000188](../../web/agent.html#L188) | 188 | `" const completionStateLabels={"` | — |
| [SRC-DE7EABE998-L000189](../../web/agent.html#L189) | 189 | `"  completed:\"مكتمل\",unknown:\"غير معلوم\",not_attempted:\"لم يبدأ\","` | — |
| [SRC-DE7EABE998-L000190](../../web/agent.html#L190) | 190 | `"  failed_or_incomplete:\"فشل أو لم يكتمل\",results_received:\"استُلمت نتائج\","` | — |
| [SRC-DE7EABE998-L000191](../../web/agent.html#L191) | 191 | `"  completed_no_results:\"اكتمل دون نتائج\",attempted_no_usable_sources:\"محاولة دون مصادر صالحة\","` | — |
| [SRC-DE7EABE998-L000192](../../web/agent.html#L192) | 192 | `"  not_applicable_no_eligible_sources:\"لا توجد مصادر نهائية\",all_final_sources_read:\"قُرئت كل الصفحات النهائية\","` | — |
| [SRC-DE7EABE998-L000193](../../web/agent.html#L193) | 193 | `"  some_final_sources_read:\"قُرئ بعض الصفحات\",no_final_source_page_read:\"لم تُقرأ صفحات نهائية\","` | — |
| [SRC-DE7EABE998-L000194](../../web/agent.html#L194) | 194 | `"  not_attempted_or_withheld:\"لم تُولد الإجابة أو حُجبت\",answer_generated:\"وُلّدت الإجابة\","` | — |
| [SRC-DE7EABE998-L000195](../../web/agent.html#L195) | 195 | `"  not_completed:\"لم يكتمل\",failed_or_unavailable:\"فشل أو غير متاح\","` | — |
| [SRC-DE7EABE998-L000196](../../web/agent.html#L196) | 196 | `"  not_run:\"لم يُنفذ\",not_performed:\"لم يُنفذ\",sources_retained:\"احتُفظ بمصادر\","` | — |
| [SRC-DE7EABE998-L000197](../../web/agent.html#L197) | 197 | `"  rejected_all_candidates:\"رُفضت كل المرشحات\",no_eligible_sources:\"لا توجد مصادر مقبولة\","` | — |
| [SRC-DE7EABE998-L000198](../../web/agent.html#L198) | 198 | `"  index_range_check_passed:\"فُحص نطاق أرقام الإحالات فقط\","` | — |
| [SRC-DE7EABE998-L000199](../../web/agent.html#L199) | 199 | `"  invalid_index_references_removed:\"حُذفت إحالات خارج النطاق\","` | — |
| [SRC-DE7EABE998-L000200](../../web/agent.html#L200) | 200 | `"  no_citation_markers_present:\"لا توجد علامات إحالة\",diagnostics_not_computed:\"تعذر احتساب التشخيص\""` | — |
| [SRC-DE7EABE998-L000201](../../web/agent.html#L201) | 201 | `" };"` | — |
| [SRC-DE7EABE998-L000202](../../web/agent.html#L202) | 202 | `" const completionSummary=completion&&completion.status"` | — |
| [SRC-DE7EABE998-L000203](../../web/agent.html#L203) | 203 | `"  ?'<p class=\"'+([\"search_failed_or_incomplete\",\"execution_stopped_budget\",\"answer_generation_or_review_failed\",\"no_eligible_sources_after_filtering\",\"partial_answer_evidence_gaps_detected\"].includes(completion.status)?\"warning\":\"report-note\")+'\"><b>حالة إكمال البحث:</b> '+escapeHtml(completionStatusLabels[completion.status]\|\|completion.status)+'. هذه حالة تشغيلية وليست احتمالًا لصحة الإجابة.</p>'"` | — |
| [SRC-DE7EABE998-L000204](../../web/agent.html#L204) | 204 | `"  :\"\";"` | — |
| [SRC-DE7EABE998-L000205](../../web/agent.html#L205) | 205 | `" const completionPhaseRows=completion&&completion.phases&&typeof completion.phases===\"object\""` | — |
| [SRC-DE7EABE998-L000206](../../web/agent.html#L206) | 206 | `"  ?Object.entries(completion.phases).map(([phase,state])=>'<li>'+escapeHtml(completionPhaseLabels[phase]\|\|phase)+': '+escapeHtml(completionStateLabels[state]\|\|state\|\|\"غير محدد\")+'</li>').join(\"\")"` | — |
| [SRC-DE7EABE998-L000207](../../web/agent.html#L207) | 207 | `"  :\"\";"` | — |
| [SRC-DE7EABE998-L000208](../../web/agent.html#L208) | 208 | `" const completionCounters=completion&&completion.counters&&typeof completion.counters===\"object\"?completion.counters:{};"` | — |
| [SRC-DE7EABE998-L000209](../../web/agent.html#L209) | 209 | `" const completionCounterRows=["` | — |
| [SRC-DE7EABE998-L000210](../../web/agent.html#L210) | 210 | `"  [completionCounters.queries_planned,\"استعلامًا مخططًا\"],"` | — |
| [SRC-DE7EABE998-L000211](../../web/agent.html#L211) | 211 | `"  [completionCounters.queries_attempted,\"استعلامًا تمت محاولته\"],"` | — |
| [SRC-DE7EABE998-L000212](../../web/agent.html#L212) | 212 | `"  [completionCounters.per_query_result_count_sum,\"مجموع أعداد النتائج المسجلة لكل استعلام، قبل إزالة التكرار\"],"` | — |
| [SRC-DE7EABE998-L000213](../../web/agent.html#L213) | 213 | `"  [completionCounters.final_source_list_count,\"مصدرًا في القائمة النهائية\"],"` | — |
| [SRC-DE7EABE998-L000214](../../web/agent.html#L214) | 214 | `"  [completionCounters.unique_normalized_url_count,\"رابطًا فريدًا بعد التطبيع\"],"` | — |
| [SRC-DE7EABE998-L000215](../../web/agent.html#L215) | 215 | `"  [completionCounters.duplicate_normalized_url_count,\"رابطًا مكررًا وفق التطبيع\"],"` | — |
| [SRC-DE7EABE998-L000216](../../web/agent.html#L216) | 216 | `"  [completionCounters.distinct_registrable_domain_count,\"نطاقًا مسجلًا مختلفًا\"],"` | — |
| [SRC-DE7EABE998-L000217](../../web/agent.html#L217) | 217 | `"  [completionCounters.pages_fetched_flag_count,\"صفحة تحمل علامة جلب\"],"` | — |
| [SRC-DE7EABE998-L000218](../../web/agent.html#L218) | 218 | `"  [completionCounters.pages_read_with_text_count,\"صفحة توفر نصها المقروء\"],"` | — |
| [SRC-DE7EABE998-L000219](../../web/agent.html#L219) | 219 | `"  [completionCounters.snippet_only_source_count,\"مصدرًا بمقتطف دون صفحة مقروءة\"],"` | — |
| [SRC-DE7EABE998-L000220](../../web/agent.html#L220) | 220 | `"  [completionCounters.connector_success_count,\"استجابة موصل ناجحة/مكتملة\"],"` | — |
| [SRC-DE7EABE998-L000221](../../web/agent.html#L221) | 221 | `"  [completionCounters.connector_failure_count,\"حالة إخفاق موصل مسجلة\"],"` | — |
| [SRC-DE7EABE998-L000222](../../web/agent.html#L222) | 222 | `"  [completionCounters.guardrail_rejected_candidate_count,\"مرشحًا مرفوضًا بحواجز الأدلة\"]"` | — |
| [SRC-DE7EABE998-L000223](../../web/agent.html#L223) | 223 | `" ];"` | — |
| [SRC-DE7EABE998-L000224](../../web/agent.html#L224) | 224 | `" const completionCounterHtml=completionCounterRows.map(([value,label])=>'<div class=\"metric\"><strong>'+escapeHtml(value===null\|\|value===undefined?\"غير محدد\":value)+'</strong><span>'+escapeHtml(label)+'</span></div>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000225](../../web/agent.html#L225) | 225 | `" const consistency=completion&&completion.counter_consistency&&typeof completion.counter_consistency===\"object\"?completion.counter_consistency:null;"` | — |
| [SRC-DE7EABE998-L000226](../../web/agent.html#L226) | 226 | `" const consistencyLabels={matched:\"العدادات المتاحة متطابقة\",mismatch_detected:\"اختلاف بين بعض العدادات والقائمة النهائية\",not_computable:\"لا توجد عدادات كافية للمقارنة\"};"` | — |
| [SRC-DE7EABE998-L000227](../../web/agent.html#L227) | 227 | `" const consistencyHtml=consistency?'<p class=\"'+(consistency.status===\"mismatch_detected\"?\"warning\":\"report-note\")+'\">اتساق العدادات: '+escapeHtml(consistencyLabels[consistency.status]\|\|consistency.status\|\|\"غير محدد\")+(Array.isArray(consistency.issues)&&consistency.issues.length?' — '+consistency.issues.map(escapeHtml).join(\"، \"):\"\")+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000228](../../web/agent.html#L228) | 228 | `" const completionDetailsHtml=completion&&completion.status"` | — |
| [SRC-DE7EABE998-L000229](../../web/agent.html#L229) | 229 | `"  ?'<details class=\"details\"><summary>تفاصيل مراحل إكمال البحث والعدادات</summary>'+(completionPhaseRows?'<p class=\"report-note\">مراحل التنفيذ:</p><ul>'+completionPhaseRows+'</ul>':\"\")+'<div class=\"metrics\">'+completionCounterHtml+'</div>'+consistencyHtml+'<p class=\"warning\">التحقق الدلالي من أن كل ادعاء مسنود فعلًا بالمصدر لم يُنفذ في هذا التشخيص. صلاحية رقم الإحالة أو قراءة الصفحة لا تثبت صحة الادعاء.</p></details>'"` | — |
| [SRC-DE7EABE998-L000230](../../web/agent.html#L230) | 230 | `"  :\"\";"` | — |
| [SRC-DE7EABE998-L000231](../../web/agent.html#L231) | 231 | `" const e=r.evidence_signals&&typeof r.evidence_signals===\"object\"?r.evidence_signals:{};"` | — |
| [SRC-DE7EABE998-L000232](../../web/agent.html#L232) | 232 | `" const sources=Array.isArray(result.sources)?result.sources:[];"` | — |
| [SRC-DE7EABE998-L000233](../../web/agent.html#L233) | 233 | `" const researchErrorOutcome=[\"attempted_research_error\",\"unknown_after_research_error\"].includes(r.search_outcome);"` | — |
| [SRC-DE7EABE998-L000234](../../web/agent.html#L234) | 234 | `" const lead=r.lead_generation&&typeof r.lead_generation===\"object\"?r.lead_generation:null;"` | — |
| [SRC-DE7EABE998-L000235](../../web/agent.html#L235) | 235 | `" const leadResearchIncomplete=!!lead&&lead.status===\"research_incomplete\";"` | — |
| [SRC-DE7EABE998-L000236](../../web/agent.html#L236) | 236 | `" const leadSignalCount=lead&&lead.candidate_signal_count!==null&&lead.candidate_signal_count!==undefined&&Number.isFinite(Number(lead.candidate_signal_count))?Number(lead.candidate_signal_count):null;"` | — |
| [SRC-DE7EABE998-L000237](../../web/agent.html#L237) | 237 | `" const noQualifiedLeads=!!lead&&!leadResearchIncomplete&&leadSignalCount===0;"` | — |
| [SRC-DE7EABE998-L000238](../../web/agent.html#L238) | 238 | `" const scoreLabel=lead?(leadResearchIncomplete?\"تعذر حسم البحث عن العملاء\":noQualifiedLeads?\"لم يُثبت وجود عميل محتمل\":\"إشارات نية شراء مرشحة\"):(researchErrorOutcome?\"تعذر تحديد التغطية\":(e.coverage_level\|\|\"تغطية محدودة\"));"` | — |
| [SRC-DE7EABE998-L000239](../../web/agent.html#L239) | 239 | `" const metrics=lead?["` | — |
| [SRC-DE7EABE998-L000240](../../web/agent.html#L240) | 240 | `"  [leadSignalCount??\"غير محدد\",\"إشارة نصية مرشحة لنية شراء\"],"` | — |
| [SRC-DE7EABE998-L000241](../../web/agent.html#L241) | 241 | `"  [lead.related_results_reviewed??\"غير محدد\",\"نتيجة تمت مراجعتها\"],"` | — |
| [SRC-DE7EABE998-L000242](../../web/agent.html#L242) | 242 | `"  [r.pages_fetched??(leadResearchIncomplete?\"غير محدد\":0),\"صفحة قُرئت\"],"` | — |
| [SRC-DE7EABE998-L000243](../../web/agent.html#L243) | 243 | `"  [leadResearchIncomplete?\"غير محدد\":(e.providers_count??(Array.isArray(r.providers_used)?r.providers_used.length:0)),\"واجهة أسهمت بمصدر صالح\"]"` | — |
| [SRC-DE7EABE998-L000244](../../web/agent.html#L244) | 244 | `" ]:["` | — |
| [SRC-DE7EABE998-L000245](../../web/agent.html#L245) | 245 | `"  [researchErrorOutcome?(r.unique_sources??\"غير محدد\"):(r.unique_sources??sources.length),\"مصدرًا فريدًا\"],"` | — |
| [SRC-DE7EABE998-L000246](../../web/agent.html#L246) | 246 | `"  [researchErrorOutcome?\"غير محدد\":(e.unique_domains??\"—\"),\"نطاقًا مختلفًا\"],"` | — |
| [SRC-DE7EABE998-L000247](../../web/agent.html#L247) | 247 | `"  [researchErrorOutcome?(r.pages_fetched??\"غير محدد\"):(r.pages_fetched??e.pages_read??0),\"صفحة قُرئت\"],"` | — |
| [SRC-DE7EABE998-L000248](../../web/agent.html#L248) | 248 | `"  [researchErrorOutcome?\"غير محدد\":(e.providers_count??(Array.isArray(r.providers_used)?r.providers_used.length:0)),\"واجهة أسهمت بمصدر صالح\"]"` | — |
| [SRC-DE7EABE998-L000249](../../web/agent.html#L249) | 249 | `" ];"` | — |
| [SRC-DE7EABE998-L000250](../../web/agent.html#L250) | 250 | `" const metricHtml=metrics.map(([v,l])=>'<div class=\"metric\"><strong>'+escapeHtml(v)+'</strong><span>'+escapeHtml(l)+'</span></div>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000251](../../web/agent.html#L251) | 251 | `" const operationalMetrics=["` | — |
| [SRC-DE7EABE998-L000252](../../web/agent.html#L252) | 252 | `"  [r.provider_candidates_received??\"غير محدد\",\"مرشح أعاده محرك البحث قبل التصفية (قد يتكرر)\"],"` | — |
| [SRC-DE7EABE998-L000253](../../web/agent.html#L253) | 253 | `"  [r.provider_candidates_accepted??\"غير محدد\",\"مرشح اجتاز فحص الموصل قبل الدمج\"],"` | — |
| [SRC-DE7EABE998-L000254](../../web/agent.html#L254) | 254 | `"  [r.provider_candidates_rejected??\"غير محدد\",\"مرشح رُفض بفحص الرابط أو الصلة\"],"` | — |
| [SRC-DE7EABE998-L000255](../../web/agent.html#L255) | 255 | `"  [r.raw_results??\"غير محدد\",\"نتيجة جُمعت قبل دمج التكرارات\"],"` | — |
| [SRC-DE7EABE998-L000256](../../web/agent.html#L256) | 256 | `"  [r.unique_urls??r.unique_sources??sources.length,\"رابط فريد بعد الدمج\"],"` | — |
| [SRC-DE7EABE998-L000257](../../web/agent.html#L257) | 257 | `"  [r.pages_fetch_attempted??\"غير محدد\",\"محاولة جلب صفحة\"],"` | — |
| [SRC-DE7EABE998-L000258](../../web/agent.html#L258) | 258 | `"  [r.pages_content_extracted??r.pages_fetched??\"غير محدد\",\"صفحة استُخرج منها نص\"],"` | — |
| [SRC-DE7EABE998-L000259](../../web/agent.html#L259) | 259 | `"  [r.pages_partial_extracted??\"غير محدد\",\"صفحة استُخرج جزء من نصها\"],"` | — |
| [SRC-DE7EABE998-L000260](../../web/agent.html#L260) | 260 | `"  [r.pages_extract_failed??\"غير محدد\",\"صفحة فشل استخراج نصها\"]"` | — |
| [SRC-DE7EABE998-L000261](../../web/agent.html#L261) | 261 | `" ];"` | — |
| [SRC-DE7EABE998-L000262](../../web/agent.html#L262) | 262 | `" const operationalHtml='<div class=\"metrics\">'+operationalMetrics.map(([v,l])=>'<div class=\"metric\"><strong>'+escapeHtml(v)+'</strong><span>'+escapeHtml(l)+'</span></div>').join(\"\")+'</div>';"` | — |
| [SRC-DE7EABE998-L000263](../../web/agent.html#L263) | 263 | `" const connectors=r.connector_summary&&Array.isArray(r.connector_summary.connectors)?r.connector_summary.connectors:[];"` | — |
| [SRC-DE7EABE998-L000264](../../web/agent.html#L264) | 264 | `" const connectorDetails=connectors.length?'<details class=\"details\"><summary>تشخيص الموصلات في هذا الطلب ('+connectors.length+')</summary><div>'+connectors.map(c=>'<article class=\"source\"><strong>'+escapeHtml(c.name\|\|\"موصل\")+' · '+escapeHtml(c.status\|\|\"unknown\")+'</strong><p>الإعداد: '+escapeHtml(c.configuration_status\|\|\"unknown\")+' · تمت المحاولة: '+escapeHtml(c.attempted===true?\"نعم\":c.attempted===false?\"لا\":\"غير محسوم\")+' · متاح في هذا الطلب: '+escapeHtml(c.available_for_this_request===true?\"نعم\":c.available_for_this_request===false?\"لا\":\"غير محسوم\")+' · استجابة المعالجة مؤكدة: '+escapeHtml(c.verified_for_this_request===true?\"نعم\":c.verified_for_this_request===false?\"لا\":\"غير مختبر/غير محسوم\")+' · إخفاق ملاحظ: '+escapeHtml(c.failure_observed===true?\"نعم\":\"لا\")+' · مرشحون أوليون من الموصل: '+escapeHtml(c.result_count??\"غير محدد\")+' · اجتازوا فحص الموصل: '+escapeHtml(c.accepted_count??\"غير محدد\")+' · مصادر نهائية منسوبة إليه: '+escapeHtml(c.useful_result_count??\"غير محدد\")+' · مرفوض: '+escapeHtml(c.rejected_count??\"غير محدد\")+' · توزيع الرفض: '+escapeHtml(c.rejection_counts_observed===true&&c.rejection_counts?('مرشح مشوّه '+(c.rejection_counts.malformed_candidate??0)+'؛ رابط غير صالح/هدف غير آمن '+(c.rejection_counts.invalid_url_or_unsafe_target??0)+'؛ نطاق محظور '+(c.rejection_counts.blocked_domain??0)+'؛ صلة ضعيفة '+(c.rejection_counts.relevance_below_threshold??0)):'غير مسجل في هذه الجولة')+' · كل المرشحين رُفضوا: '+escapeHtml(c.candidate_rejection_observed===true?\"نعم\":c.candidate_rejection_observed===false?\"لا\":\"غير محسوم\")+'</p>'+((Array.isArray(c.queries)&&c.queries.length)?'<p>استعلامات: '+c.queries.map(escapeHtml).join(\" · \")+'</p>':\"\")+((Array.isArray(c.errors)&&c.errors.length)?'<p class=\"warning\">أخطاء: '+c.errors.map(escapeHtml).join(\" · \")+'</p>':\"\")+'</article>').join(\"\")+'</div></details>':\"\";"` | — |
| [SRC-DE7EABE998-L000265](../../web/agent.html#L265) | 265 | `" const integrity=r.answer_integrity&&typeof r.answer_integrity===\"object\"?r.answer_integrity:null;"` | — |
| [SRC-DE7EABE998-L000266](../../web/agent.html#L266) | 266 | `" const integrityNumbers=integrity&&Array.isArray(integrity.potentially_unsupported_numeric_literals)?integrity.potentially_unsupported_numeric_literals:[];"` | — |
| [SRC-DE7EABE998-L000267](../../web/agent.html#L267) | 267 | `" const integrityTargets=integrity&&Array.isArray(integrity.target_coverage)?integrity.target_coverage:[];"` | — |
| [SRC-DE7EABE998-L000268](../../web/agent.html#L268) | 268 | `" const requirementEvidence=integrity&&Array.isArray(integrity.requirement_evidence)?integrity.requirement_evidence:[];"` | — |
| [SRC-DE7EABE998-L000269](../../web/agent.html#L269) | 269 | `" const requirementEvidenceHtml=requirementEvidence.length?'<p class=\"report-note\">سجل الأدلة لكل محور — إشارات لفظية وربط استعلامات، وليست إثباتًا لصحة الادعاءات:</p><ul>'+requirementEvidence.map(item=>{const statusText=({candidate_evidence_found_not_verified:\"وُجد نص مرشح مطابق لفظيًا؛ لم تُتحقق دلالته.\",query_returned_candidates_no_lexical_signal:\"عاد الاستعلام بمصادر، لكن لم يظهر تطابق لفظي كافٍ داخل النص.\",no_candidate_evidence_found:\"لم تُسجل أدلة مرشحة لهذا المحور في النتائج المتاحة.\",query_result_linkage_unavailable:\"تعذر ربط النتائج بالاستعلام المخصص لهذا المحور.\",query_not_available:\"لا يوجد استعلام مخصص مسجل لهذا المحور.\"})[item.status]\|\|\"الحالة غير محسومة.\";const ids=Array.isArray(item.candidate_source_indexes)?item.candidate_source_indexes:[];const qids=Array.isArray(item.query_result_source_indexes)?item.query_result_source_indexes:[];return '<li><strong>'+escapeHtml(item.target\|\|\"محور\")+':</strong> '+escapeHtml(statusText)+(ids.length?' — مرشحو الدليل: '+ids.map(n=>\"المصدر \"+escapeHtml(n)).join(\"، \"):\"\")+(qids.length?' — نتائج الاستعلام: '+qids.map(n=>\"المصدر \"+escapeHtml(n)).join(\"، \"):\"\")+'</li>';}).join(\"\")+'</ul>':\"\";"` | — |
| [SRC-DE7EABE998-L000270](../../web/agent.html#L270) | 270 | `" const citationNumericSupport=integrity&&Array.isArray(integrity.citation_numeric_support)?integrity.citation_numeric_support:[];"` | — |
| [SRC-DE7EABE998-L000271](../../web/agent.html#L271) | 271 | `" const citedNumberIssues=citationNumericSupport.filter(item=>item&&Array.isArray(item.potentially_unsupported_numeric_literals)&&item.potentially_unsupported_numeric_literals.length);"` | — |
| [SRC-DE7EABE998-L000272](../../web/agent.html#L272) | 272 | `" const citedNumberHtml=citedNumberIssues.length?'<p class=\"warning\">وجد الفحص أرقامًا قد لا يسندها المصدر المحدد في الاستشهاد؛ راجع المقتطف أو نص الصفحة الأصلي.</p><ul>'+citedNumberIssues.map(item=>'<li>الجملة '+escapeHtml(item.sentence_number??\"غير محدد\")+' · الرقم: '+item.potentially_unsupported_numeric_literals.map(escapeHtml).join(\"، \")+' · الاستشهادات: '+(Array.isArray(item.cited_source_indexes)?item.cited_source_indexes.map(n=>'المصدر '+escapeHtml(n)).join(\"، \"):\"غير محددة\")+'</li>').join(\"\")+'</ul>':\"\";"` | — |
| [SRC-DE7EABE998-L000273](../../web/agent.html#L273) | 273 | `" const valueDiscrepancies=integrity&&Array.isArray(integrity.potential_value_discrepancies)?integrity.potential_value_discrepancies:[];"` | — |
| [SRC-DE7EABE998-L000274](../../web/agent.html#L274) | 274 | `" const valueDimensionLabels={price_or_cost:\"السعر/التكلفة\",area_or_size:\"المساحة/الحجم\",duration:\"المدة\",percentage_or_rate:\"النسبة\",date_or_year:\"التاريخ/السنة\"};"` | — |
| [SRC-DE7EABE998-L000275](../../web/agent.html#L275) | 275 | `" const valueDiscrepancyHtml=valueDiscrepancies.length?'<p class=\"warning\">رُصدت قيم مختلفة في مصادر متعددة. قد يكون الاختلاف بين منتجات أو فترات أو وحدات مختلفة؛ هذه ليست إثباتًا تلقائيًا لوجود تناقض.</p><ul>'+valueDiscrepancies.map(item=>'<li>'+escapeHtml(valueDimensionLabels[item.dimension]\|\|item.dimension\|\|\"قيمة\")+' — '+(Array.isArray(item.values)?item.values.map(value=>escapeHtml(value.value)+' ('+(Array.isArray(value.source_indexes)?value.source_indexes.map(n=>'المصدر '+escapeHtml(n)).join(\"، \"):\"مصدر غير محدد\")+')').join(' مقابل '):\"قِيَم تحتاج مراجعة\")+'</li>').join(\"\")+'</ul>':\"\";"` | — |
| [SRC-DE7EABE998-L000276](../../web/agent.html#L276) | 276 | `" const citationAlignment=integrity&&Array.isArray(integrity.citation_lexical_alignment)?integrity.citation_lexical_alignment:[];"` | — |
| [SRC-DE7EABE998-L000277](../../web/agent.html#L277) | 277 | `" const weakCitationAlignment=citationAlignment.filter(item=>item&&item.status===\"weak_lexical_overlap\");"` | — |
| [SRC-DE7EABE998-L000278](../../web/agent.html#L278) | 278 | `" const citationAlignmentHtml=citationAlignment.length?'<p class=\"report-note\">'+(weakCitationAlignment.length?'لم يظهر تطابق لفظي كافٍ في '+weakCitationAlignment.length+' جملة/جمل مستشهد بها؛ راجع الاستشهادات يدويًا.':'ظهرت إشارات تطابق لفظي لبعض الجمل المستشهد بها، لكنها لا تثبت أن المصدر يسند الادعاء.')+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000279](../../web/agent.html#L279) | 279 | `" const integrityScope=integrity?({contains_extracted_page_text_and_or_snippets:\"نص صفحات مستخرج مع مقتطفات بحث\",search_snippets_only:\"مقتطفات بحث فقط — لم يؤكد النظام قراءة نص الصفحات\",no_readable_source_text:\"لا يتوفر نص مصدر قابل للفحص\"}[integrity.source_evidence_scope]\|\|integrity.source_evidence_scope\|\|\"غير محدد\"):\"غير محدد\";"` | — |
| [SRC-DE7EABE998-L000280](../../web/agent.html#L280) | 280 | `" const integritySummary=integrity?'<p class=\"report-note\">عدادات الفحص اللفظي: '+escapeHtml(integrity.potentially_unsupported_numeric_count??0)+' رقم لم يظهر نصيًا في الأدلة؛ '+escapeHtml(integrity.potentially_unsupported_numeric_by_citation_count??0)+' رقم لا يسنده المصدر المشار إليه تحديدًا؛ '+escapeHtml(integrity.potential_value_discrepancy_count??0)+' اختلاف قيمة يحتاج مطابقة؛ '+escapeHtml(integrity.potentially_missing_target_count??0)+' محور محتمل النقص؛ '+escapeHtml(integrity.source_evidence_gap_count??0)+' محور بلا إشارة لفظية في المصادر.</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000281](../../web/agent.html#L281) | 281 | `" const taskFulfillmentStatus=r.task_fulfillment_status\|\|result.task_fulfillment_status\|\|\"not_machine_assessed_no_explicit_targets_detected\";"` | — |
| [SRC-DE7EABE998-L000282](../../web/agent.html#L282) | 282 | `" const taskFulfillmentText=({"` | — |
| [SRC-DE7EABE998-L000283](../../web/agent.html#L283) | 283 | `"  possible_gap_detected:\"قد تكون الإجابة أغفلت محورًا من السؤال؛ هذه إشارة لفظية تحتاج مراجعة وليست حكمًا نهائيًا.\","` | — |
| [SRC-DE7EABE998-L000284](../../web/agent.html#L284) | 284 | `"  lexical_signals_found_not_semantically_verified:\"ظهرت إشارات لفظية للمحاور المستخرجة، لكن هذا لا يثبت اكتمال المهمة.\","` | — |
| [SRC-DE7EABE998-L000285](../../web/agent.html#L285) | 285 | `"  candidate_evidence_gaps_or_linkage_unknown:\"لا توجد إشارات نصية كافية لبعض المحاور أو تعذر ربط نتائج البحث بها؛ راجع الاستعلامات والمصادر قبل اعتماد الإجابة.\","` | — |
| [SRC-DE7EABE998-L000286](../../web/agent.html#L286) | 286 | `"  not_assessed_insufficient_evidence:\"الأدلة غير كافية؛ لم يتم التحقق من اكتمال المهمة.\","` | — |
| [SRC-DE7EABE998-L000287](../../web/agent.html#L287) | 287 | `"  not_machine_assessed_no_explicit_targets_detected:\"لم تُستخرج محاور صريحة قابلة للفحص؛ اكتمال المهمة لم يُقيّم آليًا.\""` | — |
| [SRC-DE7EABE998-L000288](../../web/agent.html#L288) | 288 | `" })[taskFulfillmentStatus]\|\|\"حالة اكتمال المهمة غير محسومة آليًا.\";"` | — |
| [SRC-DE7EABE998-L000289](../../web/agent.html#L289) | 289 | `" const taskFulfillmentHtml='<p class=\"'+([\"possible_gap_detected\",\"candidate_evidence_gaps_or_linkage_unknown\"].includes(taskFulfillmentStatus)?\"warning\":\"report-note\")+'\">حالة تنفيذ المطلوب: '+escapeHtml(taskFulfillmentText)+'</p>';"` | — |
| [SRC-DE7EABE998-L000290](../../web/agent.html#L290) | 290 | `" const coverageRepairStatus=r.coverage_repair_status\|\|result.coverage_repair_status\|\|\"\";"` | — |
| [SRC-DE7EABE998-L000291](../../web/agent.html#L291) | 291 | `" const coverageRepairMessages={"` | — |
| [SRC-DE7EABE998-L000292](../../web/agent.html#L292) | 292 | `"  revised_and_reaudited:\"عُدّلت الإجابة بعد رصد محور محتمل النقص ثم خضعت لمراجعة أدلة ثانية؛ تظل المراجعة بمساعدة نموذج وليست تحققًا مستقلًا.\","` | — |
| [SRC-DE7EABE998-L000293](../../web/agent.html#L293) | 293 | `"  revised_and_reaudited_remaining_gaps:\"خضعت الإجابة المعدلة لمراجعة ثانية، لكن بقي محور محتمل النقص؛ لا تعتبر المهمة مكتملة قبل مراجعة الأدلة.\","` | — |
| [SRC-DE7EABE998-L000294](../../web/agent.html#L294) | 294 | `"  reaudit_budget_exhausted:\"انتهت ميزانية النماذج قبل إعادة تدقيق الإجابة المعدلة؛ عُرضت مقتطفات المصادر بدل اعتبار النص المعدل إجابة مكتملة.\","` | — |
| [SRC-DE7EABE998-L000295](../../web/agent.html#L295) | 295 | `"  reaudit_unavailable:\"تعذرت إعادة تدقيق الإجابة المعدلة؛ عُرضت مقتطفات المصادر بدل اعتبار النص المعدل إجابة مكتملة.\","` | — |
| [SRC-DE7EABE998-L000296](../../web/agent.html#L296) | 296 | `"  budget_exhausted:\"انتهت ميزانية النماذج قبل استكمال محور محتمل النقص.\","` | — |
| [SRC-DE7EABE998-L000297](../../web/agent.html#L297) | 297 | `"  unavailable:\"تعذرت محاولة إصلاح محور محتمل النقص.\","` | — |
| [SRC-DE7EABE998-L000298](../../web/agent.html#L298) | 298 | `"  no_change_gap_unresolved:\"لم تغيّر محاولة الإصلاح الإجابة؛ لا يزال احتمال نقص أحد المحاور قائمًا.\","` | — |
| [SRC-DE7EABE998-L000299](../../web/agent.html#L299) | 299 | `"  source_evidence_gap_unresolved:\"ذُكرت المحاور في الإجابة، لكن لم تظهر لها إشارات لفظية في المصادر؛ تظل غير محسومة.\""` | — |
| [SRC-DE7EABE998-L000300](../../web/agent.html#L300) | 300 | `" };"` | — |
| [SRC-DE7EABE998-L000301](../../web/agent.html#L301) | 301 | `" const coverageRepairHtml=coverageRepairMessages[coverageRepairStatus]?'<p class=\"warning\">حالة إصلاح التغطية: '+escapeHtml(coverageRepairMessages[coverageRepairStatus])+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000302](../../web/agent.html#L302) | 302 | `" const criterionGapResearch=r.criterion_gap_research\|\|(result.search_report&&result.search_report.criterion_gap_research)\|\|{};"` | — |
| [SRC-DE7EABE998-L000303](../../web/agent.html#L303) | 303 | `" const criterionGapResearchStatus=criterionGapResearch.status\|\|\"\";"` | — |
| [SRC-DE7EABE998-L000304](../../web/agent.html#L304) | 304 | `" const criterionGapResearchMessages={"` | — |
| [SRC-DE7EABE998-L000305](../../web/agent.html#L305) | 305 | `"  not_needed:\"لم يرصد الفحص فجوة مصدر تستدعي بحثًا إضافيًا.\","` | — |
| [SRC-DE7EABE998-L000306](../../web/agent.html#L306) | 306 | `"  evidence_added_and_answer_regenerated:\"أضاف البحث الإضافي نص مصدر جديدًا؛ ثم أُعيد توليد الإجابة ومراجعتها.\","` | — |
| [SRC-DE7EABE998-L000307](../../web/agent.html#L307) | 307 | `"  search_completed_no_new_criterion_evidence:\"أُجري بحث إضافي للمحاور الناقصة، لكنه لم يضف نص مصدر جديدًا يمكن تمييزه.\","` | — |
| [SRC-DE7EABE998-L000308](../../web/agent.html#L308) | 308 | `"  skipped_no_reserved_search_slot:\"لم يُخصّص استعلام إضافي لهذه المهمة؛ ظلت المحاور بلا إشارة مصدر غير محسومة.\","` | — |
| [SRC-DE7EABE998-L000309](../../web/agent.html#L309) | 309 | `"  skipped_search_budget_exhausted:\"انتهت ميزانية البحث قبل إعادة البحث عن المحاور الناقصة؛ لا تُعدّ التغطية مكتملة.\","` | — |
| [SRC-DE7EABE998-L000310](../../web/agent.html#L310) | 310 | `"  search_failed:\"تعذر إكمال البحث الإضافي عن الأدلة المفقودة.\","` | — |
| [SRC-DE7EABE998-L000311](../../web/agent.html#L311) | 311 | `"  skipped_no_request_budget:\"تعذر فحص ميزانية البحث؛ لم يُنفذ بحث إضافي.\","` | — |
| [SRC-DE7EABE998-L000312](../../web/agent.html#L312) | 312 | `"  skipped_query_not_distinct:\"لم يُنفذ بحث إضافي لأن الاستعلام المقترح لم يكن مختلفًا بما يكفي.\","` | — |
| [SRC-DE7EABE998-L000313](../../web/agent.html#L313) | 313 | `"  skipped_no_valid_query:\"لم يتوفر استعلام إضافي صالح للمحاور الناقصة.\","` | — |
| [SRC-DE7EABE998-L000314](../../web/agent.html#L314) | 314 | `"  evidence_added_but_regeneration_unavailable:\"وصل نص مصدر إضافي، لكن تعذرت إعادة توليد الإجابة ومراجعتها؛ يلزم التحقق من المحاور يدويًا.\""` | — |
| [SRC-DE7EABE998-L000315](../../web/agent.html#L315) | 315 | `" };"` | — |
| [SRC-DE7EABE998-L000316](../../web/agent.html#L316) | 316 | `" const criterionGapResearchHtml=criterionGapResearchMessages[criterionGapResearchStatus]?'<p class=\"'+(criterionGapResearchStatus===\"evidence_added_and_answer_regenerated\"?\"report-note\":\"warning\")+'\">بحث فجوة الأدلة: '+escapeHtml(criterionGapResearchMessages[criterionGapResearchStatus])+'</p>':\"\";"` | — |
| [SRC-DE7EABE998-L000317](../../web/agent.html#L317) | 317 | `" const claimLedger=r.claim_evidence_ledger&&typeof r.claim_evidence_ledger===\"object\"?r.claim_evidence_ledger:null;"` | — |
| [SRC-DE7EABE998-L000318](../../web/agent.html#L318) | 318 | `" const claimSegments=claimLedger&&Array.isArray(claimLedger.segments)?claimLedger.segments:[];"` | — |
| [SRC-DE7EABE998-L000319](../../web/agent.html#L319) | 319 | `" const claimSummary=claimLedger&&claimLedger.summary&&typeof claimLedger.summary===\"object\"?claimLedger.summary:{};"` | — |
| [SRC-DE7EABE998-L000320](../../web/agent.html#L320) | 320 | `" const claimEvidenceHtml=claimLedger?'<p class=\"report-note\">سجل تتبع الاستشهادات (لا يثبت صحة الادعاء): '+escapeHtml(claimSummary.segments_with_citations??0)+' مقطعًا يحمل استشهادًا، '+escapeHtml(claimSummary.segments_without_citation_markers??0)+' بلا علامة استشهاد، '+escapeHtml(claimSummary.out_of_range_reference_count??0)+' مرجعًا خارج نطاق المصادر، '+escapeHtml(claimSummary.cited_segments_with_readable_source_evidence??0)+' مقطعًا مستشهدًا به له نص دليل قابل للقراءة.</p>'+(claimSegments.length?'<details class=\"details\"><summary>عرض سجل المقاطع والاستشهادات المرتبطة</summary><ol>'+claimSegments.map(item=>'<li><p>'+escapeHtml(item.text\|\|\"\")+'</p><p class=\"report-note\">الحالة: '+escapeHtml(item.citation_status\|\|\"غير محدد\")+' · الفحص اللفظي: '+escapeHtml(item.lexical_audit_status\|\|\"غير منفذ\")+'</p>'+(Array.isArray(item.sources)&&item.sources.length?'<ul>'+item.sources.map(source=>'<li>المصدر '+escapeHtml(source.source_index)+' · '+escapeHtml(source.title\|\|\"دون عنوان\")+' · '+escapeHtml(source.evidence_basis\|\|\"غير معروف\")+(source.url?' · <a href=\"'+escapeHtml(source.url)+'\" target=\"_blank\" rel=\"noopener noreferrer\">فتح المصدر</a>':\"\")+'</li>').join(\"\")+'</ul>':\"\")+'</li>').join(\"\")+'</ol><p class=\"report-note\">السجل يربط علامات الاستشهاد بقائمة المصادر المتاحة فقط؛ لا يُجري تحققًا دلاليًا أو مستقلًا من الحقيقة.</p></details>':\"\"):\"\";"` | — |
| [SRC-DE7EABE998-L000321](../../web/agent.html#L321) | 321 | `" const integrityHtml=integrity?'<details class=\"details\"><summary>فحص لفظي أولي: اتساق الإجابة مع الأدلة — ليس تحققًا من الحقيقة</summary><p class=\"report-note\">لا يثبت هذا الفحص صحة الوقائع أو دلالة الاستشهاد. نطاق الأدلة النصية: '+escapeHtml(integrityScope)+'.</p>'+integritySummary+taskFulfillmentHtml+claimEvidenceHtml+coverageRepairHtml+requirementEvidenceHtml+criterionGapResearchHtml+'<p class=\"report-note\">'+(integrityNumbers.length?'أرقام أو تواريخ تحتاج مراجعة لأنها لم تظهر نصيًا في المواد المتاحة: '+integrityNumbers.map(escapeHtml).join(\"، \")+'.':'لم يرصد الفحص أرقامًا محددة غائبة عن النصوص التي جمعها. هذا لا يثبت أن كل رقم صحيح أو أن المصدر يدعم الادعاء المرتبط به.')+'</p>'+citedNumberHtml+valueDiscrepancyHtml+citationAlignmentHtml+(integrityTargets.length?'<p class=\"report-note\">إشارات التغطية اللفظية لمحاور السؤال:</p><ul>'+integrityTargets.map(t=>'<li>'+escapeHtml(t.target\|\|\"محور\")+' — '+escapeHtml(t.status===\"lexical_signal_found\"?\"وُجد تطابق لفظي في الإجابة؛ ليس إثباتًا لاكتمالها\":\"قد يكون هذا المحور ناقصًا؛ لم يظهر تطابق لفظي كافٍ في الإجابة\")+' · '+escapeHtml(t.source_evidence_status===\"source_lexical_signal_found\"?\"توجد إشارة لفظية في المصادر\":\"لا توجد إشارة لفظية في المصادر\")+(Array.isArray(t.source_evidence_checks)&&t.source_evidence_checks.length?' ('+t.source_evidence_checks.map(item=>'المصدر '+escapeHtml(item.source_index)).join('، ')+')':'')+'</li>').join(\"\")+'</ul>':\"\")+'<p class=\"report-note\">المنهج: فحص لفظي حتمي محدود. لا يتحقق من معنى الادعاء أو صلة الاستشهاد به أو استقلال المصادر؛ راجع الأدلة الأصلية قبل الاعتماد.</p></details>':\"\";"` | — |
| [SRC-DE7EABE998-L000322](../../web/agent.html#L322) | 322 | `" const providerCounts=r.provider_counts&&typeof r.provider_counts===\"object\"&&!Array.isArray(r.provider_counts)?r.provider_counts:{};"` | — |
| [SRC-DE7EABE998-L000323](../../web/agent.html#L323) | 323 | `" const providerHtml=Object.entries(providerCounts).map(([p,n])=>'<span class=\"provider\">'+escapeHtml(p)+' · '+escapeHtml(n)+'</span>').join(\"\");"` | — |
| [SRC-DE7EABE998-L000324](../../web/agent.html#L324) | 324 | `" const notes=Array.isArray(e.warnings)?e.warnings:[];"` | — |
| [SRC-DE7EABE998-L000325](../../web/agent.html#L325) | 325 | `" const queryList=Array.isArray(result.search_queries)?result.search_queries:[];"` | — |
| [SRC-DE7EABE998-L000326](../../web/agent.html#L326) | 326 | `" const details=queryList.length?'<details class=\"details\"><summary>زوايا البحث المستخدمة ('+queryList.length+')</summary><ol>'+queryList.map(q=>'<li>'+escapeHtml(q)+'</li>').join(\"\")+'</ol></details>':\"\";"` | — |
| [SRC-DE7EABE998-L000327](../../web/agent.html#L327) | 327 | `" const coverageText=lead"` | — |
| [SRC-DE7EABE998-L000328](../../web/agent.html#L328) | 328 | `"  ? (leadResearchIncomplete"` | — |
| [SRC-DE7EABE998-L000329](../../web/agent.html#L329) | 329 | `"     ? \"تعطل البحث أو لم يكتمل التقرير؛ الأعداد غير المتاحة ليست صفرًا، ولا يمكن استنتاج عدم وجود عملاء.\""` | — |
| [SRC-DE7EABE998-L000330](../../web/agent.html#L330) | 330 | `"     : noQualifiedLeads"` | — |
| [SRC-DE7EABE998-L000331](../../web/agent.html#L331) | 331 | `"      ? \"لم تثبت النتائج وجود أي عميل محتمل. عدد صفحات العقارات أو النطاقات ليس عدد المشترين.\""` | — |
| [SRC-DE7EABE998-L000332](../../web/agent.html#L332) | 332 | `"      : \"الإشارات العلنية لا تثبت هوية الشخص أو استمرار رغبته في الشراء؛ راجع نص المصدر وتاريخه يدويًا.\")"` | — |
| [SRC-DE7EABE998-L000333](../../web/agent.html#L333) | 333 | `"  : researchErrorOutcome"` | — |
| [SRC-DE7EABE998-L000334](../../web/agent.html#L334) | 334 | `"   ? \"تعذر تحديد تغطية البحث لأن مسار تجميع الأدلة لم يكتمل؛ الأرقام غير المتاحة ليست صفرًا.\""` | — |
| [SRC-DE7EABE998-L000335](../../web/agent.html#L335) | 335 | `"   : \"تغطية الأدلة: \"+scoreLabel+\" — يصف هذا الوصف اتساع الأدلة المتاحة ولا يمثل احتمال صحة الإجابة.\";"` | — |
| [SRC-DE7EABE998-L000336](../../web/agent.html#L336) | 336 | `" const usableSourceCount=researchErrorOutcome?null:(r.usable_sources_after_filtering??sources.length);"` | — |
| [SRC-DE7EABE998-L000337](../../web/agent.html#L337) | 337 | `" const attemptText=result&&result.search_attempted===true"` | — |
