# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **032**
- سجلات الأسطر: **800**
- النطاق: SRC-CAC5F305FE-L000032 إلى SRC-B3062EB677-L000263
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-CAC5F305FE — [tests/test_agent_modes.py](../../tests/test_agent_modes.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-CAC5F305FE-L000032](../../tests/test_agent_modes.py#L32) | 32 | `"        \"domain\": \"example.org\","` | — |
| [SRC-CAC5F305FE-L000033](../../tests/test_agent_modes.py#L33) | 33 | `"        \"source_class\": \"general\","` | — |
| [SRC-CAC5F305FE-L000034](../../tests/test_agent_modes.py#L34) | 34 | `"        \"platform\": \"web\","` | — |
| [SRC-CAC5F305FE-L000035](../../tests/test_agent_modes.py#L35) | 35 | `"        \"published_at\": \"2026-10-10\","` | — |
| [SRC-CAC5F305FE-L000036](../../tests/test_agent_modes.py#L36) | 36 | `"        \"rank_score\": 1.0,"` | — |
| [SRC-CAC5F305FE-L000037](../../tests/test_agent_modes.py#L37) | 37 | `"    }"` | — |
| [SRC-CAC5F305FE-L000038](../../tests/test_agent_modes.py#L38) | 38 | `""` | — |
| [SRC-CAC5F305FE-L000039](../../tests/test_agent_modes.py#L39) | 39 | `"    def collect(research_plan):"` | — |
| [SRC-CAC5F305FE-L000040](../../tests/test_agent_modes.py#L40) | 40 | `"        seen[\"plan\"] = dict(research_plan)"` | — |
| [SRC-CAC5F305FE-L000041](../../tests/test_agent_modes.py#L41) | 41 | `"        report = {"` | — |
| [SRC-CAC5F305FE-L000042](../../tests/test_agent_modes.py#L42) | 42 | `"            \"queries_planned\": len(research_plan[\"queries\"]),"` | — |
| [SRC-CAC5F305FE-L000043](../../tests/test_agent_modes.py#L43) | 43 | `"            \"queries_attempted\": len(research_plan[\"queries\"]),"` | — |
| [SRC-CAC5F305FE-L000044](../../tests/test_agent_modes.py#L44) | 44 | `"            \"query_results\": [],"` | — |
| [SRC-CAC5F305FE-L000045](../../tests/test_agent_modes.py#L45) | 45 | `"            \"unique_sources\": 1,"` | — |
| [SRC-CAC5F305FE-L000046](../../tests/test_agent_modes.py#L46) | 46 | `"            \"pages_fetched\": 1,"` | — |
| [SRC-CAC5F305FE-L000047](../../tests/test_agent_modes.py#L47) | 47 | `"            \"providers_used\": [\"test_search\"],"` | — |
| [SRC-CAC5F305FE-L000048](../../tests/test_agent_modes.py#L48) | 48 | `"            \"provider_counts\": {\"test_search\": 1},"` | — |
| [SRC-CAC5F305FE-L000049](../../tests/test_agent_modes.py#L49) | 49 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-CAC5F305FE-L000050](../../tests/test_agent_modes.py#L50) | 50 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-CAC5F305FE-L000051](../../tests/test_agent_modes.py#L51) | 51 | `"            \"depth\": research_plan[\"depth\"],"` | — |
| [SRC-CAC5F305FE-L000052](../../tests/test_agent_modes.py#L52) | 52 | `"            \"planning_method\": \"test\","` | — |
| [SRC-CAC5F305FE-L000053](../../tests/test_agent_modes.py#L53) | 53 | `"            \"evidence_signals\": evidence_signal_report([source]),"` | — |
| [SRC-CAC5F305FE-L000054](../../tests/test_agent_modes.py#L54) | 54 | `"        }"` | — |
| [SRC-CAC5F305FE-L000055](../../tests/test_agent_modes.py#L55) | 55 | `"        return [source], [], report"` | — |
| [SRC-CAC5F305FE-L000056](../../tests/test_agent_modes.py#L56) | 56 | `""` | — |
| [SRC-CAC5F305FE-L000057](../../tests/test_agent_modes.py#L57) | 57 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-CAC5F305FE-L000058](../../tests/test_agent_modes.py#L58) | 58 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-CAC5F305FE-L000059](../../tests/test_agent_modes.py#L59) | 59 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: \"الخلاصة [المصدر 1]\")"` | — |
| [SRC-CAC5F305FE-L000060](../../tests/test_agent_modes.py#L60) | 60 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-CAC5F305FE-L000061](../../tests/test_agent_modes.py#L61) | 61 | `""` | — |
| [SRC-CAC5F305FE-L000062](../../tests/test_agent_modes.py#L62) | 62 | `"    result = agent.answer(\"حلل الموضوع\", mode=\"deep\")"` | — |
| [SRC-CAC5F305FE-L000063](../../tests/test_agent_modes.py#L63) | 63 | `""` | — |
| [SRC-CAC5F305FE-L000064](../../tests/test_agent_modes.py#L64) | 64 | `"    assert seen[\"plan\"][\"depth\"] == \"deep\""` | — |
| [SRC-CAC5F305FE-L000065](../../tests/test_agent_modes.py#L65) | 65 | `"    assert len(seen[\"plan\"][\"queries\"]) > 1"` | — |
| [SRC-CAC5F305FE-L000066](../../tests/test_agent_modes.py#L66) | 66 | `"    assert result[\"research_plan\"][\"mode\"] == \"deep\""` | — |
| [SRC-CAC5F305FE-L000067](../../tests/test_agent_modes.py#L67) | 67 | `"    assert \"evidence_signals\" in result[\"search_report\"]"` | — |
| [SRC-CAC5F305FE-L000068](../../tests/test_agent_modes.py#L68) | 68 | `"    assert result[\"search_report\"][\"evidence_repair\"][\"attempted\"] is False"` | — |
| [SRC-CAC5F305FE-L000069](../../tests/test_agent_modes.py#L69) | 69 | `"    assert result[\"search_report\"][\"evidence_repair\"][\"reason\"] == \"deep_research_already_expanded\""` | — |
| [SRC-CAC5F305FE-L000070](../../tests/test_agent_modes.py#L70) | 70 | `"    assert result[\"search_report\"][\"evidence_signals\"][\"unique_domains\"] == 1"` | — |
## اختبارات

### FILE-63610B9E85 — [tests/test_agentic_retrieval.py](../../tests/test_agentic_retrieval.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-63610B9E85-L000001](../../tests/test_agentic_retrieval.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-63610B9E85-L000002](../../tests/test_agentic_retrieval.py#L2) | 2 | `""` | — |
| [SRC-63610B9E85-L000003](../../tests/test_agentic_retrieval.py#L3) | 3 | `"from agents.claim_evidence import build_claim_evidence_ledger"` | — |
| [SRC-63610B9E85-L000004](../../tests/test_agentic_retrieval.py#L4) | 4 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-63610B9E85-L000005](../../tests/test_agentic_retrieval.py#L5) | 5 | `""` | — |
| [SRC-63610B9E85-L000006](../../tests/test_agentic_retrieval.py#L6) | 6 | `""` | — |
| [SRC-63610B9E85-L000007](../../tests/test_agentic_retrieval.py#L7) | 7 | `"def test_claim_ledger_maps_citations_to_exact_sources() -> None:"` | — |
| [SRC-63610B9E85-L000008](../../tests/test_agentic_retrieval.py#L8) | 8 | `"    sources = ["` | — |
| [SRC-63610B9E85-L000009](../../tests/test_agentic_retrieval.py#L9) | 9 | `"        {\"title\": \"Price source\", \"url\": \"https://example.com/price\","` | — |
| [SRC-63610B9E85-L000010](../../tests/test_agentic_retrieval.py#L10) | 10 | `"         \"snippet\": \"Solar battery price is 100 EGP.\", \"provider\": \"fixture\"},"` | — |
| [SRC-63610B9E85-L000011](../../tests/test_agentic_retrieval.py#L11) | 11 | `"        {\"title\": \"Warranty source\", \"url\": \"https://example.org/warranty\","` | — |
| [SRC-63610B9E85-L000012](../../tests/test_agentic_retrieval.py#L12) | 12 | `"         \"page_text\": \"Warranty terms are listed here.\", \"page_fetched\": True,"` | — |
| [SRC-63610B9E85-L000013](../../tests/test_agentic_retrieval.py#L13) | 13 | `"         \"provider\": \"fixture\"},"` | — |
| [SRC-63610B9E85-L000014](../../tests/test_agentic_retrieval.py#L14) | 14 | `"    ]"` | — |
| [SRC-63610B9E85-L000015](../../tests/test_agentic_retrieval.py#L15) | 15 | `"    result = build_claim_evidence_ledger("` | — |
| [SRC-63610B9E85-L000016](../../tests/test_agentic_retrieval.py#L16) | 16 | `"        \"The price is 100 EGP [source 1]. Warranty terms are shown [المصدر 2].\","` | — |
| [SRC-63610B9E85-L000017](../../tests/test_agentic_retrieval.py#L17) | 17 | `"        sources,"` | — |
| [SRC-63610B9E85-L000018](../../tests/test_agentic_retrieval.py#L18) | 18 | `"        {\"citation_lexical_alignment\": ["` | — |
| [SRC-63610B9E85-L000019](../../tests/test_agentic_retrieval.py#L19) | 19 | `"            {\"sentence_number\": 1, \"status\": \"lexical_overlap_signal_found\"},"` | — |
| [SRC-63610B9E85-L000020](../../tests/test_agentic_retrieval.py#L20) | 20 | `"            {\"sentence_number\": 2, \"status\": \"weak_lexical_overlap\"},"` | — |
| [SRC-63610B9E85-L000021](../../tests/test_agentic_retrieval.py#L21) | 21 | `"        ]},"` | — |
| [SRC-63610B9E85-L000022](../../tests/test_agentic_retrieval.py#L22) | 22 | `"    )"` | — |
| [SRC-63610B9E85-L000023](../../tests/test_agentic_retrieval.py#L23) | 23 | `"    assert result[\"semantic_verification\"] is False"` | — |
| [SRC-63610B9E85-L000024](../../tests/test_agentic_retrieval.py#L24) | 24 | `"    assert result[\"claim_entailment\"] == \"not_checked\""` | — |
| [SRC-63610B9E85-L000025](../../tests/test_agentic_retrieval.py#L25) | 25 | `"    assert result[\"summary\"][\"segment_candidate_count\"] == 2"` | — |
| [SRC-63610B9E85-L000026](../../tests/test_agentic_retrieval.py#L26) | 26 | `"    assert result[\"summary\"][\"valid_source_reference_count\"] == 2"` | — |
| [SRC-63610B9E85-L000027](../../tests/test_agentic_retrieval.py#L27) | 27 | `"    assert result[\"segments\"][0][\"sources\"][0][\"url\"] == \"https://example.com/price\""` | — |
| [SRC-63610B9E85-L000028](../../tests/test_agentic_retrieval.py#L28) | 28 | `"    assert result[\"segments\"][1][\"sources\"][0][\"evidence_basis\"] == \"extracted_page_text\""` | — |
| [SRC-63610B9E85-L000029](../../tests/test_agentic_retrieval.py#L29) | 29 | `"    assert result[\"segments\"][0][\"lexical_audit_status\"] == \"lexical_overlap_signal_found\""` | — |
| [SRC-63610B9E85-L000030](../../tests/test_agentic_retrieval.py#L30) | 30 | `""` | — |
| [SRC-63610B9E85-L000031](../../tests/test_agentic_retrieval.py#L31) | 31 | `""` | — |
| [SRC-63610B9E85-L000032](../../tests/test_agentic_retrieval.py#L32) | 32 | `"def test_claim_ledger_marks_uncited_and_out_of_range_references() -> None:"` | — |
| [SRC-63610B9E85-L000033](../../tests/test_agentic_retrieval.py#L33) | 33 | `"    result = build_claim_evidence_ledger("` | — |
| [SRC-63610B9E85-L000034](../../tests/test_agentic_retrieval.py#L34) | 34 | `"        \"Uncited sentence. Bad reference [المصدر 2]. Valid [source 1].\","` | — |
| [SRC-63610B9E85-L000035](../../tests/test_agentic_retrieval.py#L35) | 35 | `"        [{\"title\": \"Source\", \"url\": \"https://example.com\", \"snippet\": \"text\"}],"` | — |
| [SRC-63610B9E85-L000036](../../tests/test_agentic_retrieval.py#L36) | 36 | `"    )"` | — |
| [SRC-63610B9E85-L000037](../../tests/test_agentic_retrieval.py#L37) | 37 | `"    assert result[\"summary\"][\"segments_without_citation_markers\"] == 1"` | — |
| [SRC-63610B9E85-L000038](../../tests/test_agentic_retrieval.py#L38) | 38 | `"    assert result[\"summary\"][\"out_of_range_reference_count\"] == 1"` | — |
| [SRC-63610B9E85-L000039](../../tests/test_agentic_retrieval.py#L39) | 39 | `"    assert result[\"segments\"][0][\"citation_status\"] == \"no_citation_marker\""` | — |
| [SRC-63610B9E85-L000040](../../tests/test_agentic_retrieval.py#L40) | 40 | `"    assert result[\"segments\"][1][\"citation_status\"] == \"citation_index_out_of_range\""` | — |
| [SRC-63610B9E85-L000041](../../tests/test_agentic_retrieval.py#L41) | 41 | `"    assert result[\"segments\"][2][\"citation_status\"] == \"cited_source_attached\""` | — |
| [SRC-63610B9E85-L000042](../../tests/test_agentic_retrieval.py#L42) | 42 | `""` | — |
| [SRC-63610B9E85-L000043](../../tests/test_agentic_retrieval.py#L43) | 43 | `""` | — |
| [SRC-63610B9E85-L000044](../../tests/test_agentic_retrieval.py#L44) | 44 | `"def test_claim_ledger_does_not_equate_valid_index_with_verification() -> None:"` | — |
| [SRC-63610B9E85-L000045](../../tests/test_agentic_retrieval.py#L45) | 45 | `"    result = build_claim_evidence_ledger("` | — |
| [SRC-63610B9E85-L000046](../../tests/test_agentic_retrieval.py#L46) | 46 | `"        \"Claim with a marker [المصدر 1].\","` | — |
| [SRC-63610B9E85-L000047](../../tests/test_agentic_retrieval.py#L47) | 47 | `"        [{\"title\": \"Only a title\", \"url\": \"https://example.com\"}],"` | — |
| [SRC-63610B9E85-L000048](../../tests/test_agentic_retrieval.py#L48) | 48 | `"    )"` | — |
| [SRC-63610B9E85-L000049](../../tests/test_agentic_retrieval.py#L49) | 49 | `"    assert result[\"segments\"][0][\"citation_status\"] == \"valid_index_without_readable_evidence\""` | — |
| [SRC-63610B9E85-L000050](../../tests/test_agentic_retrieval.py#L50) | 50 | `"    assert result[\"segments\"][0][\"sources\"][0][\"evidence_basis\"] == \"title_only\""` | — |
| [SRC-63610B9E85-L000051](../../tests/test_agentic_retrieval.py#L51) | 51 | `"    # A title is metadata, not a source passage available for evidence review."` | — |
| [SRC-63610B9E85-L000052](../../tests/test_agentic_retrieval.py#L52) | 52 | `"    assert result[\"segments\"][0][\"sources\"][0][\"reference_status\"] == \"valid_index_without_readable_evidence\""` | — |
| [SRC-63610B9E85-L000053](../../tests/test_agentic_retrieval.py#L53) | 53 | `"    assert result[\"summary\"][\"cited_segments_with_readable_source_evidence\"] == 0"` | — |
| [SRC-63610B9E85-L000054](../../tests/test_agentic_retrieval.py#L54) | 54 | `"    assert result[\"fact_correctness\"] == \"not_checked\""` | — |
| [SRC-63610B9E85-L000055](../../tests/test_agentic_retrieval.py#L55) | 55 | `"    assert any(\"do not prove\" in item for item in result[\"limitations\"])"` | — |
| [SRC-63610B9E85-L000056](../../tests/test_agentic_retrieval.py#L56) | 56 | `""` | — |
| [SRC-63610B9E85-L000057](../../tests/test_agentic_retrieval.py#L57) | 57 | `""` | — |
| [SRC-63610B9E85-L000058](../../tests/test_agentic_retrieval.py#L58) | 58 | `"def test_collect_research_retries_missing_aspect_within_query_limit(monkeypatch) -> None:"` | — |
| [SRC-63610B9E85-L000059](../../tests/test_agentic_retrieval.py#L59) | 59 | `"    agent = WebAgent()"` | — |
| [SRC-63610B9E85-L000060](../../tests/test_agentic_retrieval.py#L60) | 60 | `"    agent._request_budget = None"` | — |
| [SRC-63610B9E85-L000061](../../tests/test_agentic_retrieval.py#L61) | 61 | `"    queries: list[str] = []"` | — |
| [SRC-63610B9E85-L000062](../../tests/test_agentic_retrieval.py#L62) | 62 | `""` | — |
| [SRC-63610B9E85-L000063](../../tests/test_agentic_retrieval.py#L63) | 63 | `"    def fake_search(query: str):"` | — |
| [SRC-63610B9E85-L000064](../../tests/test_agentic_retrieval.py#L64) | 64 | `"        queries.append(query)"` | — |
| [SRC-63610B9E85-L000065](../../tests/test_agentic_retrieval.py#L65) | 65 | `"        if \"warranty\" in query.casefold():"` | — |
| [SRC-63610B9E85-L000066](../../tests/test_agentic_retrieval.py#L66) | 66 | `"            return [{"` | — |
| [SRC-63610B9E85-L000067](../../tests/test_agentic_retrieval.py#L67) | 67 | `"                \"title\": \"Solar battery warranty terms\","` | — |
| [SRC-63610B9E85-L000068](../../tests/test_agentic_retrieval.py#L68) | 68 | `"                \"url\": \"https://example.org/warranty\","` | — |
| [SRC-63610B9E85-L000069](../../tests/test_agentic_retrieval.py#L69) | 69 | `"                \"snippet\": \"Solar battery warranty terms and coverage.\","` | — |
| [SRC-63610B9E85-L000070](../../tests/test_agentic_retrieval.py#L70) | 70 | `"                \"provider\": \"fixture_search\","` | — |
| [SRC-63610B9E85-L000071](../../tests/test_agentic_retrieval.py#L71) | 71 | `"                \"provider_rank\": 1,"` | — |
| [SRC-63610B9E85-L000072](../../tests/test_agentic_retrieval.py#L72) | 72 | `"            }]"` | — |
| [SRC-63610B9E85-L000073](../../tests/test_agentic_retrieval.py#L73) | 73 | `"        return [{"` | — |
| [SRC-63610B9E85-L000074](../../tests/test_agentic_retrieval.py#L74) | 74 | `"            \"title\": \"Solar battery price details\","` | — |
| [SRC-63610B9E85-L000075](../../tests/test_agentic_retrieval.py#L75) | 75 | `"            \"url\": \"https://example.com/price\","` | — |
| [SRC-63610B9E85-L000076](../../tests/test_agentic_retrieval.py#L76) | 76 | `"            \"snippet\": \"Solar battery price: 100 EGP.\","` | — |
| [SRC-63610B9E85-L000077](../../tests/test_agentic_retrieval.py#L77) | 77 | `"            \"provider\": \"fixture_search\","` | — |
| [SRC-63610B9E85-L000078](../../tests/test_agentic_retrieval.py#L78) | 78 | `"            \"provider_rank\": 1,"` | — |
| [SRC-63610B9E85-L000079](../../tests/test_agentic_retrieval.py#L79) | 79 | `"        }]"` | — |
| [SRC-63610B9E85-L000080](../../tests/test_agentic_retrieval.py#L80) | 80 | `""` | — |
| [SRC-63610B9E85-L000081](../../tests/test_agentic_retrieval.py#L81) | 81 | `"    monkeypatch.setattr(agent, \"_search_web\", fake_search)"` | — |
| [SRC-63610B9E85-L000082](../../tests/test_agentic_retrieval.py#L82) | 82 | `"    monkeypatch.setattr("` | — |
| [SRC-63610B9E85-L000083](../../tests/test_agentic_retrieval.py#L83) | 83 | `"        agent, \"_fetch_page\","` | — |
| [SRC-63610B9E85-L000084](../../tests/test_agentic_retrieval.py#L84) | 84 | `"        lambda _url: (\"Fixture page\", \"Solar battery price and warranty evidence text.\"),"` | — |
| [SRC-63610B9E85-L000085](../../tests/test_agentic_retrieval.py#L85) | 85 | `"    )"` | — |
| [SRC-63610B9E85-L000086](../../tests/test_agentic_retrieval.py#L86) | 86 | `"    sources, _warnings, report = agent._collect_research({"` | — |
| [SRC-63610B9E85-L000087](../../tests/test_agentic_retrieval.py#L87) | 87 | `"        \"query_limit\": 3,"` | — |
| [SRC-63610B9E85-L000088](../../tests/test_agentic_retrieval.py#L88) | 88 | `"        \"queries\": [\"solar battery\", \"solar battery price\", \"solar battery warranty\"],"` | — |
| [SRC-63610B9E85-L000089](../../tests/test_agentic_retrieval.py#L89) | 89 | `"        \"coverage_targets\": [\"price\", \"warranty\"],"` | — |
| [SRC-63610B9E85-L000090](../../tests/test_agentic_retrieval.py#L90) | 90 | `"        \"depth\": \"standard\","` | — |
| [SRC-63610B9E85-L000091](../../tests/test_agentic_retrieval.py#L91) | 91 | `"        \"social_focus\": False,"` | — |
| [SRC-63610B9E85-L000092](../../tests/test_agentic_retrieval.py#L92) | 92 | `"        \"platforms\": [],"` | — |
| [SRC-63610B9E85-L000093](../../tests/test_agentic_retrieval.py#L93) | 93 | `"        \"direct_urls\": [],"` | — |
| [SRC-63610B9E85-L000094](../../tests/test_agentic_retrieval.py#L94) | 94 | `"    })"` | — |
| [SRC-63610B9E85-L000095](../../tests/test_agentic_retrieval.py#L95) | 95 | `"    assert len(queries) <= 3"` | — |
| [SRC-63610B9E85-L000096](../../tests/test_agentic_retrieval.py#L96) | 96 | `"    assert any(\"warranty\" in query.casefold() for query in queries)"` | — |
| [SRC-63610B9E85-L000097](../../tests/test_agentic_retrieval.py#L97) | 97 | `"    assert report[\"queries_attempted\"] == len(queries)"` | — |
| [SRC-63610B9E85-L000098](../../tests/test_agentic_retrieval.py#L98) | 98 | `"    assert any(\"warranty\" in str(source.get(\"url\", \"\")).casefold() for source in sources)"` | — |
| [SRC-63610B9E85-L000099](../../tests/test_agentic_retrieval.py#L99) | 99 | `""` | — |
| [SRC-63610B9E85-L000100](../../tests/test_agentic_retrieval.py#L100) | 100 | `""` | — |
| [SRC-63610B9E85-L000101](../../tests/test_agentic_retrieval.py#L101) | 101 | `""` | — |
| [SRC-63610B9E85-L000102](../../tests/test_agentic_retrieval.py#L102) | 102 | `"def test_generation_prompt_includes_grounded_writing_examples(monkeypatch) -> None:"` | — |
| [SRC-63610B9E85-L000103](../../tests/test_agentic_retrieval.py#L103) | 103 | `"    agent = WebAgent()"` | — |
| [SRC-63610B9E85-L000104](../../tests/test_agentic_retrieval.py#L104) | 104 | `"    captured: dict[str, object] = {}"` | — |
| [SRC-63610B9E85-L000105](../../tests/test_agentic_retrieval.py#L105) | 105 | `""` | — |
| [SRC-63610B9E85-L000106](../../tests/test_agentic_retrieval.py#L106) | 106 | `"    def fake_completion(messages, **_kwargs):"` | — |
| [SRC-63610B9E85-L000107](../../tests/test_agentic_retrieval.py#L107) | 107 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-63610B9E85-L000108](../../tests/test_agentic_retrieval.py#L108) | 108 | `"        return \"إجابة تجريبية.\""` | — |
| [SRC-63610B9E85-L000109](../../tests/test_agentic_retrieval.py#L109) | 109 | `""` | — |
| [SRC-63610B9E85-L000110](../../tests/test_agentic_retrieval.py#L110) | 110 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-63610B9E85-L000111](../../tests/test_agentic_retrieval.py#L111) | 111 | `"    answer = agent._generate("` | — |
| [SRC-63610B9E85-L000112](../../tests/test_agentic_retrieval.py#L112) | 112 | `"        question=\"اشرح لي معنى مفهوم بسيط.\","` | — |
| [SRC-63610B9E85-L000113](../../tests/test_agentic_retrieval.py#L113) | 113 | `"        history=[],"` | — |
| [SRC-63610B9E85-L000114](../../tests/test_agentic_retrieval.py#L114) | 114 | `"        sources=[],"` | — |
| [SRC-63610B9E85-L000115](../../tests/test_agentic_retrieval.py#L115) | 115 | `"        search_warning=None,"` | — |
| [SRC-63610B9E85-L000116](../../tests/test_agentic_retrieval.py#L116) | 116 | `"        research_plan={\"depth\": \"standard\"},"` | — |
| [SRC-63610B9E85-L000117](../../tests/test_agentic_retrieval.py#L117) | 117 | `"        search_report={},"` | — |
| [SRC-63610B9E85-L000118](../../tests/test_agentic_retrieval.py#L118) | 118 | `"    )"` | — |
| [SRC-63610B9E85-L000119](../../tests/test_agentic_retrieval.py#L119) | 119 | `""` | — |
| [SRC-63610B9E85-L000120](../../tests/test_agentic_retrieval.py#L120) | 120 | `"    assert answer == \"إجابة تجريبية.\""` | — |
| [SRC-63610B9E85-L000121](../../tests/test_agentic_retrieval.py#L121) | 121 | `"    messages = captured[\"messages\"]"` | — |
| [SRC-63610B9E85-L000122](../../tests/test_agentic_retrieval.py#L122) | 122 | `"    assert isinstance(messages, list)"` | — |
| [SRC-63610B9E85-L000123](../../tests/test_agentic_retrieval.py#L123) | 123 | `"    combined = \"\\n\".join("` | — |
| [SRC-63610B9E85-L000124](../../tests/test_agentic_retrieval.py#L124) | 124 | `"        str(message.get(\"content\") or \"\")"` | — |
| [SRC-63610B9E85-L000125](../../tests/test_agentic_retrieval.py#L125) | 125 | `"        for message in messages"` | — |
| [SRC-63610B9E85-L000126](../../tests/test_agentic_retrieval.py#L126) | 126 | `"        if isinstance(message, dict)"` | — |
| [SRC-63610B9E85-L000127](../../tests/test_agentic_retrieval.py#L127) | 127 | `"    )"` | — |
| [SRC-63610B9E85-L000128](../../tests/test_agentic_retrieval.py#L128) | 128 | `"    assert \"مثال أسلوبي توضيحي فقط\" in combined"` | — |
| [SRC-63610B9E85-L000129](../../tests/test_agentic_retrieval.py#L129) | 129 | `"    assert \"لا تعمم هذا على منتجات أخرى\" in combined"` | — |
| [SRC-63610B9E85-L000130](../../tests/test_agentic_retrieval.py#L130) | 130 | `"    assert \"لا أستطيع تأكيده من هذه النتائج\" in combined"` | — |
## اختبارات

### FILE-4CCB1F172B — [tests/test_answer_quality_corpus.py](../../tests/test_answer_quality_corpus.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-4CCB1F172B-L000001](../../tests/test_answer_quality_corpus.py#L1) | 1 | `"\"\"\"Structural validation for the offline answer-quality adversarial corpus."` | — |
| [SRC-4CCB1F172B-L000002](../../tests/test_answer_quality_corpus.py#L2) | 2 | `""` | — |
| [SRC-4CCB1F172B-L000003](../../tests/test_answer_quality_corpus.py#L3) | 3 | `"This module does NOT execute Omarai against the cases and does NOT claim that"` | — |
| [SRC-4CCB1F172B-L000004](../../tests/test_answer_quality_corpus.py#L4) | 4 | `"any reasoning case passed. It only verifies that the benchmark file is complete,"` | — |
| [SRC-4CCB1F172B-L000005](../../tests/test_answer_quality_corpus.py#L5) | 5 | `"internally consistent, and ready for human or fixture-assisted review."` | — |
| [SRC-4CCB1F172B-L000006](../../tests/test_answer_quality_corpus.py#L6) | 6 | `"\"\"\""` | — |
| [SRC-4CCB1F172B-L000007](../../tests/test_answer_quality_corpus.py#L7) | 7 | `"from __future__ import annotations"` | — |
| [SRC-4CCB1F172B-L000008](../../tests/test_answer_quality_corpus.py#L8) | 8 | `""` | — |
| [SRC-4CCB1F172B-L000009](../../tests/test_answer_quality_corpus.py#L9) | 9 | `"import json"` | — |
| [SRC-4CCB1F172B-L000010](../../tests/test_answer_quality_corpus.py#L10) | 10 | `"import re"` | — |
| [SRC-4CCB1F172B-L000011](../../tests/test_answer_quality_corpus.py#L11) | 11 | `"from collections import Counter"` | — |
| [SRC-4CCB1F172B-L000012](../../tests/test_answer_quality_corpus.py#L12) | 12 | `"from pathlib import Path"` | — |
| [SRC-4CCB1F172B-L000013](../../tests/test_answer_quality_corpus.py#L13) | 13 | `""` | — |
| [SRC-4CCB1F172B-L000014](../../tests/test_answer_quality_corpus.py#L14) | 14 | `"CORPUS_PATH = Path(__file__).resolve().parent / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-4CCB1F172B-L000015](../../tests/test_answer_quality_corpus.py#L15) | 15 | `"DOCS_PATH = Path(__file__).resolve().parents[1] / \"docs\" / \"ANSWER_QUALITY_BENCHMARK_AR.md\""` | — |
| [SRC-4CCB1F172B-L000016](../../tests/test_answer_quality_corpus.py#L16) | 16 | `""` | — |
| [SRC-4CCB1F172B-L000017](../../tests/test_answer_quality_corpus.py#L17) | 17 | `"REQUIRED_CASE_FIELDS = {"` | — |
| [SRC-4CCB1F172B-L000018](../../tests/test_answer_quality_corpus.py#L18) | 18 | `"    \"case_id\","` | — |
| [SRC-4CCB1F172B-L000019](../../tests/test_answer_quality_corpus.py#L19) | 19 | `"    \"category\","` | — |
| [SRC-4CCB1F172B-L000020](../../tests/test_answer_quality_corpus.py#L20) | 20 | `"    \"language\","` | — |
| [SRC-4CCB1F172B-L000021](../../tests/test_answer_quality_corpus.py#L21) | 21 | `"    \"question\","` | — |
| [SRC-4CCB1F172B-L000022](../../tests/test_answer_quality_corpus.py#L22) | 22 | `"    \"expected_strategy\","` | — |
| [SRC-4CCB1F172B-L000023](../../tests/test_answer_quality_corpus.py#L23) | 23 | `"    \"required_behaviors\","` | — |
| [SRC-4CCB1F172B-L000024](../../tests/test_answer_quality_corpus.py#L24) | 24 | `"    \"forbidden_behaviors\","` | — |
| [SRC-4CCB1F172B-L000025](../../tests/test_answer_quality_corpus.py#L25) | 25 | `"    \"evidence_fixture\","` | — |
| [SRC-4CCB1F172B-L000026](../../tests/test_answer_quality_corpus.py#L26) | 26 | `"    \"failure_conditions\","` | — |
| [SRC-4CCB1F172B-L000027](../../tests/test_answer_quality_corpus.py#L27) | 27 | `"    \"evaluation_mode\","` | — |
| [SRC-4CCB1F172B-L000028](../../tests/test_answer_quality_corpus.py#L28) | 28 | `"}"` | — |
| [SRC-4CCB1F172B-L000029](../../tests/test_answer_quality_corpus.py#L29) | 29 | `""` | — |
| [SRC-4CCB1F172B-L000030](../../tests/test_answer_quality_corpus.py#L30) | 30 | `"ALLOWED_STRATEGIES = {\"local\", \"model_no_search\", \"web_search\", \"clarify\"}"` | — |
| [SRC-4CCB1F172B-L000031](../../tests/test_answer_quality_corpus.py#L31) | 31 | `"ALLOWED_EVAL_MODES = {\"deterministic_structure\", \"fixture_assisted\", \"human_judgment\"}"` | — |
| [SRC-4CCB1F172B-L000032](../../tests/test_answer_quality_corpus.py#L32) | 32 | `""` | — |
| [SRC-4CCB1F172B-L000033](../../tests/test_answer_quality_corpus.py#L33) | 33 | `"REQUIRED_THEME_CATEGORIES = {"` | — |
| [SRC-4CCB1F172B-L000034](../../tests/test_answer_quality_corpus.py#L34) | 34 | `"    \"simple_conversational\","` | — |
| [SRC-4CCB1F172B-L000035](../../tests/test_answer_quality_corpus.py#L35) | 35 | `"    \"general_knowledge\","` | — |
| [SRC-4CCB1F172B-L000036](../../tests/test_answer_quality_corpus.py#L36) | 36 | `"    \"omarai_capabilities\","` | — |
| [SRC-4CCB1F172B-L000037](../../tests/test_answer_quality_corpus.py#L37) | 37 | `"    \"current_information\","` | — |
| [SRC-4CCB1F172B-L000038](../../tests/test_answer_quality_corpus.py#L38) | 38 | `"    \"multi_subquestions\","` | — |
| [SRC-4CCB1F172B-L000039](../../tests/test_answer_quality_corpus.py#L39) | 39 | `"    \"ambiguous_clarify\","` | — |
| [SRC-4CCB1F172B-L000040](../../tests/test_answer_quality_corpus.py#L40) | 40 | `"    \"spelling_variation\","` | — |
| [SRC-4CCB1F172B-L000041](../../tests/test_answer_quality_corpus.py#L41) | 41 | `"    \"irrelevant_results\","` | — |
| [SRC-4CCB1F172B-L000042](../../tests/test_answer_quality_corpus.py#L42) | 42 | `"    \"empty_or_failed_search\","` | — |
| [SRC-4CCB1F172B-L000043](../../tests/test_answer_quality_corpus.py#L43) | 43 | `"    \"conflicting_sources\","` | — |
| [SRC-4CCB1F172B-L000044](../../tests/test_answer_quality_corpus.py#L44) | 44 | `"    \"stale_sources_for_current\","` | — |
| [SRC-4CCB1F172B-L000045](../../tests/test_answer_quality_corpus.py#L45) | 45 | `"    \"false_corroboration\","` | — |
| [SRC-4CCB1F172B-L000046](../../tests/test_answer_quality_corpus.py#L46) | 46 | `"    \"unsupported_claim\","` | — |
| [SRC-4CCB1F172B-L000047](../../tests/test_answer_quality_corpus.py#L47) | 47 | `"    \"invalid_links\","` | — |
| [SRC-4CCB1F172B-L000048](../../tests/test_answer_quality_corpus.py#L48) | 48 | `"    \"prompt_injection_in_content\","` | — |
| [SRC-4CCB1F172B-L000049](../../tests/test_answer_quality_corpus.py#L49) | 49 | `"    \"secret_exfiltration_attempt\","` | — |
| [SRC-4CCB1F172B-L000050](../../tests/test_answer_quality_corpus.py#L50) | 50 | `"    \"missing_model_credentials\","` | — |
| [SRC-4CCB1F172B-L000051](../../tests/test_answer_quality_corpus.py#L51) | 51 | `"    \"overconfidence_insufficient_evidence\","` | — |
| [SRC-4CCB1F172B-L000052](../../tests/test_answer_quality_corpus.py#L52) | 52 | `"    \"incomplete_answer\","` | — |
| [SRC-4CCB1F172B-L000053](../../tests/test_answer_quality_corpus.py#L53) | 53 | `"    \"lead_not_verified\","` | — |
| [SRC-4CCB1F172B-L000054](../../tests/test_answer_quality_corpus.py#L54) | 54 | `"}"` | — |
| [SRC-4CCB1F172B-L000055](../../tests/test_answer_quality_corpus.py#L55) | 55 | `""` | — |
| [SRC-4CCB1F172B-L000056](../../tests/test_answer_quality_corpus.py#L56) | 56 | `"DOC_EXAMPLE_CATEGORY_EXPECTATIONS = {"` | — |
| [SRC-4CCB1F172B-L000057](../../tests/test_answer_quality_corpus.py#L57) | 57 | `"    \"AQ-024\": \"prompt_injection_in_content\","` | — |
| [SRC-4CCB1F172B-L000058](../../tests/test_answer_quality_corpus.py#L58) | 58 | `"    \"AQ-030\": \"prompt_injection_in_content\","` | — |
| [SRC-4CCB1F172B-L000059](../../tests/test_answer_quality_corpus.py#L59) | 59 | `"    \"AQ-025\": \"secret_exfiltration_attempt\","` | — |
| [SRC-4CCB1F172B-L000060](../../tests/test_answer_quality_corpus.py#L60) | 60 | `"    \"AQ-031\": \"secret_exfiltration_attempt\","` | — |
| [SRC-4CCB1F172B-L000061](../../tests/test_answer_quality_corpus.py#L61) | 61 | `"    \"AQ-023\": \"invalid_links\","` | — |
| [SRC-4CCB1F172B-L000062](../../tests/test_answer_quality_corpus.py#L62) | 62 | `"    \"AQ-029\": \"lead_not_verified\","` | — |
| [SRC-4CCB1F172B-L000063](../../tests/test_answer_quality_corpus.py#L63) | 63 | `"    \"AQ-032\": \"lead_not_verified\","` | — |
| [SRC-4CCB1F172B-L000064](../../tests/test_answer_quality_corpus.py#L64) | 64 | `"    \"AQ-033\": \"lead_not_verified\","` | — |
| [SRC-4CCB1F172B-L000065](../../tests/test_answer_quality_corpus.py#L65) | 65 | `"    \"AQ-045\": \"lead_not_verified\","` | — |
| [SRC-4CCB1F172B-L000066](../../tests/test_answer_quality_corpus.py#L66) | 66 | `"    \"AQ-018\": \"conflicting_sources\","` | — |
| [SRC-4CCB1F172B-L000067](../../tests/test_answer_quality_corpus.py#L67) | 67 | `"    \"AQ-019\": \"conflicting_sources\","` | — |
| [SRC-4CCB1F172B-L000068](../../tests/test_answer_quality_corpus.py#L68) | 68 | `"    \"AQ-020\": \"stale_sources_for_current\","` | — |
| [SRC-4CCB1F172B-L000069](../../tests/test_answer_quality_corpus.py#L69) | 69 | `"    \"AQ-034\": \"stale_sources_for_current\","` | — |
| [SRC-4CCB1F172B-L000070](../../tests/test_answer_quality_corpus.py#L70) | 70 | `"    \"AQ-042\": \"stale_sources_for_current\","` | — |
| [SRC-4CCB1F172B-L000071](../../tests/test_answer_quality_corpus.py#L71) | 71 | `"    \"AQ-021\": \"false_corroboration\","` | — |
| [SRC-4CCB1F172B-L000072](../../tests/test_answer_quality_corpus.py#L72) | 72 | `"    \"AQ-035\": \"false_corroboration\","` | — |
| [SRC-4CCB1F172B-L000073](../../tests/test_answer_quality_corpus.py#L73) | 73 | `"}"` | — |
| [SRC-4CCB1F172B-L000074](../../tests/test_answer_quality_corpus.py#L74) | 74 | `""` | — |
| [SRC-4CCB1F172B-L000075](../../tests/test_answer_quality_corpus.py#L75) | 75 | `"CASE_ID_RE = re.compile(r\"^AQ-\\d{3}$\")"` | — |
| [SRC-4CCB1F172B-L000076](../../tests/test_answer_quality_corpus.py#L76) | 76 | `""` | — |
| [SRC-4CCB1F172B-L000077](../../tests/test_answer_quality_corpus.py#L77) | 77 | `""` | — |
| [SRC-4CCB1F172B-L000078](../../tests/test_answer_quality_corpus.py#L78) | 78 | `"def _load_corpus() -> dict:"` | — |
| [SRC-4CCB1F172B-L000079](../../tests/test_answer_quality_corpus.py#L79) | 79 | `"    assert CORPUS_PATH.is_file(), f\"Missing corpus file: {CORPUS_PATH}\""` | — |
| [SRC-4CCB1F172B-L000080](../../tests/test_answer_quality_corpus.py#L80) | 80 | `"    data = json.loads(CORPUS_PATH.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-4CCB1F172B-L000081](../../tests/test_answer_quality_corpus.py#L81) | 81 | `"    assert isinstance(data, dict), \"Corpus root must be an object\""` | — |
| [SRC-4CCB1F172B-L000082](../../tests/test_answer_quality_corpus.py#L82) | 82 | `"    assert \"parts\" not in data or not data.get(\"parts\"), ("` | — |
| [SRC-4CCB1F172B-L000083](../../tests/test_answer_quality_corpus.py#L83) | 83 | `"        \"Authoritative corpus must be a single merged cases[] file, not incomplete shards\""` | — |
| [SRC-4CCB1F172B-L000084](../../tests/test_answer_quality_corpus.py#L84) | 84 | `"    )"` | — |
| [SRC-4CCB1F172B-L000085](../../tests/test_answer_quality_corpus.py#L85) | 85 | `"    return data"` | — |
| [SRC-4CCB1F172B-L000086](../../tests/test_answer_quality_corpus.py#L86) | 86 | `""` | — |
| [SRC-4CCB1F172B-L000087](../../tests/test_answer_quality_corpus.py#L87) | 87 | `""` | — |
| [SRC-4CCB1F172B-L000088](../../tests/test_answer_quality_corpus.py#L88) | 88 | `"def test_corpus_file_loads_as_utf8_json():"` | — |
| [SRC-4CCB1F172B-L000089](../../tests/test_answer_quality_corpus.py#L89) | 89 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000090](../../tests/test_answer_quality_corpus.py#L90) | 90 | `"    assert data.get(\"benchmark_id\") == \"OMARAI-REDTEAM-001\""` | — |
| [SRC-4CCB1F172B-L000091](../../tests/test_answer_quality_corpus.py#L91) | 91 | `"    assert isinstance(data.get(\"cases\"), list)"` | — |
| [SRC-4CCB1F172B-L000092](../../tests/test_answer_quality_corpus.py#L92) | 92 | `"    assert data[\"case_count\"] == len(data[\"cases\"])"` | — |
| [SRC-4CCB1F172B-L000093](../../tests/test_answer_quality_corpus.py#L93) | 93 | `""` | — |
| [SRC-4CCB1F172B-L000094](../../tests/test_answer_quality_corpus.py#L94) | 94 | `""` | — |
| [SRC-4CCB1F172B-L000095](../../tests/test_answer_quality_corpus.py#L95) | 95 | `"def test_minimum_case_count():"` | — |
| [SRC-4CCB1F172B-L000096](../../tests/test_answer_quality_corpus.py#L96) | 96 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000097](../../tests/test_answer_quality_corpus.py#L97) | 97 | `"    assert len(data[\"cases\"]) >= 40, f\"Need at least 40 cases, found {len(data['cases'])}\""` | — |
| [SRC-4CCB1F172B-L000098](../../tests/test_answer_quality_corpus.py#L98) | 98 | `"    assert data[\"case_count\"] == 45"` | — |
| [SRC-4CCB1F172B-L000099](../../tests/test_answer_quality_corpus.py#L99) | 99 | `""` | — |
| [SRC-4CCB1F172B-L000100](../../tests/test_answer_quality_corpus.py#L100) | 100 | `""` | — |
| [SRC-4CCB1F172B-L000101](../../tests/test_answer_quality_corpus.py#L101) | 101 | `"def test_case_ids_unique_and_shaped():"` | — |
| [SRC-4CCB1F172B-L000102](../../tests/test_answer_quality_corpus.py#L102) | 102 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000103](../../tests/test_answer_quality_corpus.py#L103) | 103 | `"    ids = [c[\"case_id\"] for c in data[\"cases\"]]"` | — |
| [SRC-4CCB1F172B-L000104](../../tests/test_answer_quality_corpus.py#L104) | 104 | `"    assert len(ids) == len(set(ids)), \"Duplicate case_id values found\""` | — |
| [SRC-4CCB1F172B-L000105](../../tests/test_answer_quality_corpus.py#L105) | 105 | `"    for case_id in ids:"` | — |
| [SRC-4CCB1F172B-L000106](../../tests/test_answer_quality_corpus.py#L106) | 106 | `"        assert CASE_ID_RE.match(case_id), f\"Bad case_id shape: {case_id}\""` | — |
| [SRC-4CCB1F172B-L000107](../../tests/test_answer_quality_corpus.py#L107) | 107 | `"    assert set(ids) == {f\"AQ-{i:03d}\" for i in range(1, 46)}"` | — |
| [SRC-4CCB1F172B-L000108](../../tests/test_answer_quality_corpus.py#L108) | 108 | `""` | — |
| [SRC-4CCB1F172B-L000109](../../tests/test_answer_quality_corpus.py#L109) | 109 | `""` | — |
| [SRC-4CCB1F172B-L000110](../../tests/test_answer_quality_corpus.py#L110) | 110 | `"def test_required_fields_and_types():"` | — |
| [SRC-4CCB1F172B-L000111](../../tests/test_answer_quality_corpus.py#L111) | 111 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000112](../../tests/test_answer_quality_corpus.py#L112) | 112 | `"    for case in data[\"cases\"]:"` | — |
| [SRC-4CCB1F172B-L000113](../../tests/test_answer_quality_corpus.py#L113) | 113 | `"        missing = REQUIRED_CASE_FIELDS - set(case)"` | — |
| [SRC-4CCB1F172B-L000114](../../tests/test_answer_quality_corpus.py#L114) | 114 | `"        assert not missing, f\"{case.get('case_id')}: missing {missing}\""` | — |
| [SRC-4CCB1F172B-L000115](../../tests/test_answer_quality_corpus.py#L115) | 115 | `"        assert isinstance(case[\"case_id\"], str) and case[\"case_id\"].strip()"` | — |
| [SRC-4CCB1F172B-L000116](../../tests/test_answer_quality_corpus.py#L116) | 116 | `"        assert isinstance(case[\"category\"], str) and case[\"category\"].strip()"` | — |
| [SRC-4CCB1F172B-L000117](../../tests/test_answer_quality_corpus.py#L117) | 117 | `"        assert isinstance(case[\"language\"], str) and case[\"language\"].strip()"` | — |
| [SRC-4CCB1F172B-L000118](../../tests/test_answer_quality_corpus.py#L118) | 118 | `"        assert isinstance(case[\"question\"], str) and len(case[\"question\"].strip()) >= 2"` | — |
| [SRC-4CCB1F172B-L000119](../../tests/test_answer_quality_corpus.py#L119) | 119 | `"        assert case[\"expected_strategy\"] in ALLOWED_STRATEGIES"` | — |
| [SRC-4CCB1F172B-L000120](../../tests/test_answer_quality_corpus.py#L120) | 120 | `"        assert case[\"evaluation_mode\"] in ALLOWED_EVAL_MODES"` | — |
| [SRC-4CCB1F172B-L000121](../../tests/test_answer_quality_corpus.py#L121) | 121 | `"        assert isinstance(case[\"required_behaviors\"], list) and case[\"required_behaviors\"]"` | — |
| [SRC-4CCB1F172B-L000122](../../tests/test_answer_quality_corpus.py#L122) | 122 | `"        assert isinstance(case[\"forbidden_behaviors\"], list) and case[\"forbidden_behaviors\"]"` | — |
| [SRC-4CCB1F172B-L000123](../../tests/test_answer_quality_corpus.py#L123) | 123 | `"        assert isinstance(case[\"failure_conditions\"], list) and case[\"failure_conditions\"]"` | — |
| [SRC-4CCB1F172B-L000124](../../tests/test_answer_quality_corpus.py#L124) | 124 | `"        assert isinstance(case[\"evidence_fixture\"], dict)"` | — |
| [SRC-4CCB1F172B-L000125](../../tests/test_answer_quality_corpus.py#L125) | 125 | `"        for item in ("` | — |
| [SRC-4CCB1F172B-L000126](../../tests/test_answer_quality_corpus.py#L126) | 126 | `"            case[\"required_behaviors\"]"` | — |
| [SRC-4CCB1F172B-L000127](../../tests/test_answer_quality_corpus.py#L127) | 127 | `"            + case[\"forbidden_behaviors\"]"` | — |
| [SRC-4CCB1F172B-L000128](../../tests/test_answer_quality_corpus.py#L128) | 128 | `"            + case[\"failure_conditions\"]"` | — |
| [SRC-4CCB1F172B-L000129](../../tests/test_answer_quality_corpus.py#L129) | 129 | `"        ):"` | — |
| [SRC-4CCB1F172B-L000130](../../tests/test_answer_quality_corpus.py#L130) | 130 | `"            assert isinstance(item, str) and item.strip(), ("` | — |
| [SRC-4CCB1F172B-L000131](../../tests/test_answer_quality_corpus.py#L131) | 131 | `"                f\"{case['case_id']}: empty behavior/condition\""` | — |
| [SRC-4CCB1F172B-L000132](../../tests/test_answer_quality_corpus.py#L132) | 132 | `"            )"` | — |
| [SRC-4CCB1F172B-L000133](../../tests/test_answer_quality_corpus.py#L133) | 133 | `""` | — |
| [SRC-4CCB1F172B-L000134](../../tests/test_answer_quality_corpus.py#L134) | 134 | `""` | — |
| [SRC-4CCB1F172B-L000135](../../tests/test_answer_quality_corpus.py#L135) | 135 | `"def test_required_theme_categories_represented():"` | — |
| [SRC-4CCB1F172B-L000136](../../tests/test_answer_quality_corpus.py#L136) | 136 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000137](../../tests/test_answer_quality_corpus.py#L137) | 137 | `"    present = {c[\"category\"] for c in data[\"cases\"]}"` | — |
| [SRC-4CCB1F172B-L000138](../../tests/test_answer_quality_corpus.py#L138) | 138 | `"    missing = REQUIRED_THEME_CATEGORIES - present"` | — |
| [SRC-4CCB1F172B-L000139](../../tests/test_answer_quality_corpus.py#L139) | 139 | `"    assert not missing, f\"Missing required categories: {sorted(missing)}\""` | — |
| [SRC-4CCB1F172B-L000140](../../tests/test_answer_quality_corpus.py#L140) | 140 | `""` | — |
| [SRC-4CCB1F172B-L000141](../../tests/test_answer_quality_corpus.py#L141) | 141 | `""` | — |
| [SRC-4CCB1F172B-L000142](../../tests/test_answer_quality_corpus.py#L142) | 142 | `"def test_no_empty_or_exact_duplicate_questions():"` | — |
| [SRC-4CCB1F172B-L000143](../../tests/test_answer_quality_corpus.py#L143) | 143 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000144](../../tests/test_answer_quality_corpus.py#L144) | 144 | `"    normalized = []"` | — |
| [SRC-4CCB1F172B-L000145](../../tests/test_answer_quality_corpus.py#L145) | 145 | `"    for case in data[\"cases\"]:"` | — |
| [SRC-4CCB1F172B-L000146](../../tests/test_answer_quality_corpus.py#L146) | 146 | `"        q = \" \".join(case[\"question\"].casefold().split())"` | — |
| [SRC-4CCB1F172B-L000147](../../tests/test_answer_quality_corpus.py#L147) | 147 | `"        assert len(q) >= 3, f\"{case['case_id']}: question too short\""` | — |
| [SRC-4CCB1F172B-L000148](../../tests/test_answer_quality_corpus.py#L148) | 148 | `"        normalized.append((case[\"case_id\"], q))"` | — |
| [SRC-4CCB1F172B-L000149](../../tests/test_answer_quality_corpus.py#L149) | 149 | `"    counts = Counter(q for _, q in normalized)"` | — |
| [SRC-4CCB1F172B-L000150](../../tests/test_answer_quality_corpus.py#L150) | 150 | `"    dupes = [q for q, n in counts.items() if n > 1]"` | — |
| [SRC-4CCB1F172B-L000151](../../tests/test_answer_quality_corpus.py#L151) | 151 | `"    assert not dupes, f\"Duplicate questions: {dupes}\""` | — |
| [SRC-4CCB1F172B-L000152](../../tests/test_answer_quality_corpus.py#L152) | 152 | `""` | — |
| [SRC-4CCB1F172B-L000153](../../tests/test_answer_quality_corpus.py#L153) | 153 | `""` | — |
| [SRC-4CCB1F172B-L000154](../../tests/test_answer_quality_corpus.py#L154) | 154 | `"def test_research_cases_declare_fixture_or_controlled_env():"` | — |
| [SRC-4CCB1F172B-L000155](../../tests/test_answer_quality_corpus.py#L155) | 155 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000156](../../tests/test_answer_quality_corpus.py#L156) | 156 | `"    for case in data[\"cases\"]:"` | — |
| [SRC-4CCB1F172B-L000157](../../tests/test_answer_quality_corpus.py#L157) | 157 | `"        if case[\"expected_strategy\"] != \"web_search\":"` | — |
| [SRC-4CCB1F172B-L000158](../../tests/test_answer_quality_corpus.py#L158) | 158 | `"            continue"` | — |
| [SRC-4CCB1F172B-L000159](../../tests/test_answer_quality_corpus.py#L159) | 159 | `"        fixture = case[\"evidence_fixture\"]"` | — |
| [SRC-4CCB1F172B-L000160](../../tests/test_answer_quality_corpus.py#L160) | 160 | `"        assert fixture.get(\"type\") in {"` | — |
| [SRC-4CCB1F172B-L000161](../../tests/test_answer_quality_corpus.py#L161) | 161 | `"            \"controlled_search\","` | — |
| [SRC-4CCB1F172B-L000162](../../tests/test_answer_quality_corpus.py#L162) | 162 | `"            \"controlled_page\","` | — |
| [SRC-4CCB1F172B-L000163](../../tests/test_answer_quality_corpus.py#L163) | 163 | `"            \"controlled_fetch_failure\","` | — |
| [SRC-4CCB1F172B-L000164](../../tests/test_answer_quality_corpus.py#L164) | 164 | `"            \"ssrf_blocked\","` | — |
| [SRC-4CCB1F172B-L000165](../../tests/test_answer_quality_corpus.py#L165) | 165 | `"            \"env\","` | — |
| [SRC-4CCB1F172B-L000166](../../tests/test_answer_quality_corpus.py#L166) | 166 | `"            \"none\","` | — |
| [SRC-4CCB1F172B-L000167](../../tests/test_answer_quality_corpus.py#L167) | 167 | `"        } or \"notes\" in fixture, ("` | — |
| [SRC-4CCB1F172B-L000168](../../tests/test_answer_quality_corpus.py#L168) | 168 | `"            f\"{case['case_id']}: research case needs a clear evidence fixture\""` | — |
| [SRC-4CCB1F172B-L000169](../../tests/test_answer_quality_corpus.py#L169) | 169 | `"        )"` | — |
| [SRC-4CCB1F172B-L000170](../../tests/test_answer_quality_corpus.py#L170) | 170 | `""` | — |
| [SRC-4CCB1F172B-L000171](../../tests/test_answer_quality_corpus.py#L171) | 171 | `""` | — |
| [SRC-4CCB1F172B-L000172](../../tests/test_answer_quality_corpus.py#L172) | 172 | `"def test_safety_categories_include_injection_and_secrets():"` | — |
| [SRC-4CCB1F172B-L000173](../../tests/test_answer_quality_corpus.py#L173) | 173 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000174](../../tests/test_answer_quality_corpus.py#L174) | 174 | `"    cats = {c[\"category\"] for c in data[\"cases\"]}"` | — |
| [SRC-4CCB1F172B-L000175](../../tests/test_answer_quality_corpus.py#L175) | 175 | `"    assert \"prompt_injection_in_content\" in cats"` | — |
| [SRC-4CCB1F172B-L000176](../../tests/test_answer_quality_corpus.py#L176) | 176 | `"    assert \"secret_exfiltration_attempt\" in cats"` | — |
| [SRC-4CCB1F172B-L000177](../../tests/test_answer_quality_corpus.py#L177) | 177 | `"    secret_failures = ["` | — |
| [SRC-4CCB1F172B-L000178](../../tests/test_answer_quality_corpus.py#L178) | 178 | `"        c"` | — |
| [SRC-4CCB1F172B-L000179](../../tests/test_answer_quality_corpus.py#L179) | 179 | `"        for c in data[\"cases\"]"` | — |
| [SRC-4CCB1F172B-L000180](../../tests/test_answer_quality_corpus.py#L180) | 180 | `"        if any("` | — |
| [SRC-4CCB1F172B-L000181](../../tests/test_answer_quality_corpus.py#L181) | 181 | `"            \"token\" in f.casefold() or \"secret\" in f.casefold() or \"key\" in f.casefold()"` | — |
| [SRC-4CCB1F172B-L000182](../../tests/test_answer_quality_corpus.py#L182) | 182 | `"            for f in c[\"failure_conditions\"]"` | — |
| [SRC-4CCB1F172B-L000183](../../tests/test_answer_quality_corpus.py#L183) | 183 | `"        )"` | — |
| [SRC-4CCB1F172B-L000184](../../tests/test_answer_quality_corpus.py#L184) | 184 | `"    ]"` | — |
| [SRC-4CCB1F172B-L000185](../../tests/test_answer_quality_corpus.py#L185) | 185 | `"    assert secret_failures, \"Expected at least one case with secret-related failure conditions\""` | — |
| [SRC-4CCB1F172B-L000186](../../tests/test_answer_quality_corpus.py#L186) | 186 | `""` | — |
| [SRC-4CCB1F172B-L000187](../../tests/test_answer_quality_corpus.py#L187) | 187 | `""` | — |
| [SRC-4CCB1F172B-L000188](../../tests/test_answer_quality_corpus.py#L188) | 188 | `"def test_corpus_does_not_claim_live_execution_results():"` | — |
| [SRC-4CCB1F172B-L000189](../../tests/test_answer_quality_corpus.py#L189) | 189 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000190](../../tests/test_answer_quality_corpus.py#L190) | 190 | `"    for case in data[\"cases\"]:"` | — |
| [SRC-4CCB1F172B-L000191](../../tests/test_answer_quality_corpus.py#L191) | 191 | `"        assert \"observed_result\" not in case"` | — |
| [SRC-4CCB1F172B-L000192](../../tests/test_answer_quality_corpus.py#L192) | 192 | `"        assert \"score\" not in case"` | — |
| [SRC-4CCB1F172B-L000193](../../tests/test_answer_quality_corpus.py#L193) | 193 | `"        assert case.get(\"status\") not in {\"PASS\", \"FAIL\"}"` | — |
| [SRC-4CCB1F172B-L000194](../../tests/test_answer_quality_corpus.py#L194) | 194 | `""` | — |
| [SRC-4CCB1F172B-L000195](../../tests/test_answer_quality_corpus.py#L195) | 195 | `""` | — |
| [SRC-4CCB1F172B-L000196](../../tests/test_answer_quality_corpus.py#L196) | 196 | `"def test_languages_include_arabic_english_and_mixed():"` | — |
| [SRC-4CCB1F172B-L000197](../../tests/test_answer_quality_corpus.py#L197) | 197 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000198](../../tests/test_answer_quality_corpus.py#L198) | 198 | `"    langs = {c[\"language\"] for c in data[\"cases\"]}"` | — |
| [SRC-4CCB1F172B-L000199](../../tests/test_answer_quality_corpus.py#L199) | 199 | `"    assert any(x.startswith(\"ar\") for x in langs)"` | — |
| [SRC-4CCB1F172B-L000200](../../tests/test_answer_quality_corpus.py#L200) | 200 | `"    assert \"en\" in langs"` | — |
| [SRC-4CCB1F172B-L000201](../../tests/test_answer_quality_corpus.py#L201) | 201 | `"    assert \"mixed\" in langs"` | — |
| [SRC-4CCB1F172B-L000202](../../tests/test_answer_quality_corpus.py#L202) | 202 | `"    assert \"ar-EG\" in langs"` | — |
| [SRC-4CCB1F172B-L000203](../../tests/test_answer_quality_corpus.py#L203) | 203 | `"    assert \"ar-MSA\" in langs"` | — |
| [SRC-4CCB1F172B-L000204](../../tests/test_answer_quality_corpus.py#L204) | 204 | `""` | — |
| [SRC-4CCB1F172B-L000205](../../tests/test_answer_quality_corpus.py#L205) | 205 | `""` | — |
| [SRC-4CCB1F172B-L000206](../../tests/test_answer_quality_corpus.py#L206) | 206 | `"def test_documented_high_risk_examples_match_json_categories():"` | — |
| [SRC-4CCB1F172B-L000207](../../tests/test_answer_quality_corpus.py#L207) | 207 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000208](../../tests/test_answer_quality_corpus.py#L208) | 208 | `"    by_id = {c[\"case_id\"]: c for c in data[\"cases\"]}"` | — |
| [SRC-4CCB1F172B-L000209](../../tests/test_answer_quality_corpus.py#L209) | 209 | `"    for case_id, expected_cat in DOC_EXAMPLE_CATEGORY_EXPECTATIONS.items():"` | — |
| [SRC-4CCB1F172B-L000210](../../tests/test_answer_quality_corpus.py#L210) | 210 | `"        assert case_id in by_id, f\"Doc example {case_id} missing from corpus\""` | — |
| [SRC-4CCB1F172B-L000211](../../tests/test_answer_quality_corpus.py#L211) | 211 | `"        actual = by_id[case_id][\"category\"]"` | — |
| [SRC-4CCB1F172B-L000212](../../tests/test_answer_quality_corpus.py#L212) | 212 | `"        assert actual == expected_cat, ("` | — |
| [SRC-4CCB1F172B-L000213](../../tests/test_answer_quality_corpus.py#L213) | 213 | `"            f\"Doc/example mismatch: {case_id} is category={actual!r}, \""` | — |
| [SRC-4CCB1F172B-L000214](../../tests/test_answer_quality_corpus.py#L214) | 214 | `"            f\"expected {expected_cat!r}\""` | — |
| [SRC-4CCB1F172B-L000215](../../tests/test_answer_quality_corpus.py#L215) | 215 | `"        )"` | — |
| [SRC-4CCB1F172B-L000216](../../tests/test_answer_quality_corpus.py#L216) | 216 | `""` | — |
| [SRC-4CCB1F172B-L000217](../../tests/test_answer_quality_corpus.py#L217) | 217 | `""` | — |
| [SRC-4CCB1F172B-L000218](../../tests/test_answer_quality_corpus.py#L218) | 218 | `"def test_docs_mention_corrected_high_risk_ids():"` | — |
| [SRC-4CCB1F172B-L000219](../../tests/test_answer_quality_corpus.py#L219) | 219 | `"    assert DOCS_PATH.is_file()"` | — |
| [SRC-4CCB1F172B-L000220](../../tests/test_answer_quality_corpus.py#L220) | 220 | `"    text = DOCS_PATH.read_text(encoding=\"utf-8\")"` | — |
| [SRC-4CCB1F172B-L000221](../../tests/test_answer_quality_corpus.py#L221) | 221 | `"    for case_id in (\"AQ-024\", \"AQ-030\", \"AQ-025\", \"AQ-031\", \"AQ-023\", \"AQ-018\", \"AQ-021\"):"` | — |
| [SRC-4CCB1F172B-L000222](../../tests/test_answer_quality_corpus.py#L222) | 222 | `"        assert case_id in text, f\"Docs missing corrected example {case_id}\""` | — |
| [SRC-4CCB1F172B-L000223](../../tests/test_answer_quality_corpus.py#L223) | 223 | `""` | — |
| [SRC-4CCB1F172B-L000224](../../tests/test_answer_quality_corpus.py#L224) | 224 | `""` | — |
| [SRC-4CCB1F172B-L000225](../../tests/test_answer_quality_corpus.py#L225) | 225 | `"def test_no_placeholder_corpus_content():"` | — |
| [SRC-4CCB1F172B-L000226](../../tests/test_answer_quality_corpus.py#L226) | 226 | `"    raw = CORPUS_PATH.read_text(encoding=\"utf-8\")"` | — |
| [SRC-4CCB1F172B-L000227](../../tests/test_answer_quality_corpus.py#L227) | 227 | `"    assert \"PLACEHOLDER\" not in raw"` | — |
| [SRC-4CCB1F172B-L000228](../../tests/test_answer_quality_corpus.py#L228) | 228 | `"    assert \"SEE_LOCAL_FILE\" not in raw"` | — |
| [SRC-4CCB1F172B-L000229](../../tests/test_answer_quality_corpus.py#L229) | 229 | `"    data = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000230](../../tests/test_answer_quality_corpus.py#L230) | 230 | `"    assert len(data[\"cases\"]) == data[\"case_count\"] == 45"` | — |
| [SRC-4CCB1F172B-L000231](../../tests/test_answer_quality_corpus.py#L231) | 231 | `""` | — |
| [SRC-4CCB1F172B-L000232](../../tests/test_answer_quality_corpus.py#L232) | 232 | `""` | — |
| [SRC-4CCB1F172B-L000233](../../tests/test_answer_quality_corpus.py#L233) | 233 | `"def test_human_review_template_matches_corpus_and_contains_no_scores():"` | — |
| [SRC-4CCB1F172B-L000234](../../tests/test_answer_quality_corpus.py#L234) | 234 | `"    template_path = CORPUS_PATH.parent / \"answer_quality_reviews_template.json\""` | — |
| [SRC-4CCB1F172B-L000235](../../tests/test_answer_quality_corpus.py#L235) | 235 | `"    assert template_path.is_file(), f\"Missing review template: {template_path}\""` | — |
| [SRC-4CCB1F172B-L000236](../../tests/test_answer_quality_corpus.py#L236) | 236 | `"    template = json.loads(template_path.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-4CCB1F172B-L000237](../../tests/test_answer_quality_corpus.py#L237) | 237 | `"    corpus = _load_corpus()"` | — |
| [SRC-4CCB1F172B-L000238](../../tests/test_answer_quality_corpus.py#L238) | 238 | `"    assert template.get(\"template_only\") is True"` | — |
| [SRC-4CCB1F172B-L000239](../../tests/test_answer_quality_corpus.py#L239) | 239 | `"    assert template.get(\"benchmark_id\") == corpus[\"benchmark_id\"]"` | — |
| [SRC-4CCB1F172B-L000240](../../tests/test_answer_quality_corpus.py#L240) | 240 | `"    assert template.get(\"benchmark_version\") == corpus[\"version\"]"` | — |
| [SRC-4CCB1F172B-L000241](../../tests/test_answer_quality_corpus.py#L241) | 241 | `"    case_ids = {case[\"case_id\"] for case in corpus[\"cases\"]}"` | — |
| [SRC-4CCB1F172B-L000242](../../tests/test_answer_quality_corpus.py#L242) | 242 | `"    reviews = template.get(\"reviews\")"` | — |
| [SRC-4CCB1F172B-L000243](../../tests/test_answer_quality_corpus.py#L243) | 243 | `"    assert isinstance(reviews, list)"` | — |
| [SRC-4CCB1F172B-L000244](../../tests/test_answer_quality_corpus.py#L244) | 244 | `"    assert {item.get(\"case_id\") for item in reviews} == case_ids"` | — |
| [SRC-4CCB1F172B-L000245](../../tests/test_answer_quality_corpus.py#L245) | 245 | `"    for item in reviews:"` | — |
| [SRC-4CCB1F172B-L000246](../../tests/test_answer_quality_corpus.py#L246) | 246 | `"        assert item[\"status\"] == \"NOT_TESTED\""` | — |
| [SRC-4CCB1F172B-L000247](../../tests/test_answer_quality_corpus.py#L247) | 247 | `"        assert \"correctness\" not in item"` | — |
| [SRC-4CCB1F172B-L000248](../../tests/test_answer_quality_corpus.py#L248) | 248 | `"        assert \"citations\" not in item"` | — |
| [SRC-4CCB1F172B-L000249](../../tests/test_answer_quality_corpus.py#L249) | 249 | `"        assert \"retrieval\" not in item"` | — |
| [SRC-4CCB1F172B-L000250](../../tests/test_answer_quality_corpus.py#L250) | 250 | `"        assert \"writing_quality\" not in item"` | — |
## اختبارات

### FILE-D186ED3822 — [tests/test_answer_quality_review_scorecard.py](../../tests/test_answer_quality_review_scorecard.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-D186ED3822-L000001](../../tests/test_answer_quality_review_scorecard.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-D186ED3822-L000002](../../tests/test_answer_quality_review_scorecard.py#L2) | 2 | `""` | — |
| [SRC-D186ED3822-L000003](../../tests/test_answer_quality_review_scorecard.py#L3) | 3 | `"import importlib.util"` | — |
| [SRC-D186ED3822-L000004](../../tests/test_answer_quality_review_scorecard.py#L4) | 4 | `"from pathlib import Path"` | — |
| [SRC-D186ED3822-L000005](../../tests/test_answer_quality_review_scorecard.py#L5) | 5 | `""` | — |
| [SRC-D186ED3822-L000006](../../tests/test_answer_quality_review_scorecard.py#L6) | 6 | `"import pytest"` | — |
| [SRC-D186ED3822-L000007](../../tests/test_answer_quality_review_scorecard.py#L7) | 7 | `""` | — |
| [SRC-D186ED3822-L000008](../../tests/test_answer_quality_review_scorecard.py#L8) | 8 | `"ROOT = Path(__file__).resolve().parents[1]"` | — |
| [SRC-D186ED3822-L000009](../../tests/test_answer_quality_review_scorecard.py#L9) | 9 | `"SCRIPT = ROOT / \"scripts\" / \"score_answer_quality_reviews.py\""` | — |
| [SRC-D186ED3822-L000010](../../tests/test_answer_quality_review_scorecard.py#L10) | 10 | `"CORPUS_PATH = ROOT / \"tests\" / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-D186ED3822-L000011](../../tests/test_answer_quality_review_scorecard.py#L11) | 11 | `""` | — |
| [SRC-D186ED3822-L000012](../../tests/test_answer_quality_review_scorecard.py#L12) | 12 | `""` | — |
| [SRC-D186ED3822-L000013](../../tests/test_answer_quality_review_scorecard.py#L13) | 13 | `"def load_module():"` | — |
| [SRC-D186ED3822-L000014](../../tests/test_answer_quality_review_scorecard.py#L14) | 14 | `"    spec = importlib.util.spec_from_file_location(\"answer_quality_review_scorecard\", SCRIPT)"` | — |
| [SRC-D186ED3822-L000015](../../tests/test_answer_quality_review_scorecard.py#L15) | 15 | `"    assert spec and spec.loader"` | — |
| [SRC-D186ED3822-L000016](../../tests/test_answer_quality_review_scorecard.py#L16) | 16 | `"    module = importlib.util.module_from_spec(spec)"` | — |
| [SRC-D186ED3822-L000017](../../tests/test_answer_quality_review_scorecard.py#L17) | 17 | `"    spec.loader.exec_module(module)"` | — |
| [SRC-D186ED3822-L000018](../../tests/test_answer_quality_review_scorecard.py#L18) | 18 | `"    return module"` | — |
| [SRC-D186ED3822-L000019](../../tests/test_answer_quality_review_scorecard.py#L19) | 19 | `""` | — |
| [SRC-D186ED3822-L000020](../../tests/test_answer_quality_review_scorecard.py#L20) | 20 | `""` | — |
| [SRC-D186ED3822-L000021](../../tests/test_answer_quality_review_scorecard.py#L21) | 21 | `"def corpus():"` | — |
| [SRC-D186ED3822-L000022](../../tests/test_answer_quality_review_scorecard.py#L22) | 22 | `"    return load_module().load_json_object(CORPUS_PATH)"` | — |
| [SRC-D186ED3822-L000023](../../tests/test_answer_quality_review_scorecard.py#L23) | 23 | `""` | — |
| [SRC-D186ED3822-L000024](../../tests/test_answer_quality_review_scorecard.py#L24) | 24 | `""` | — |
| [SRC-D186ED3822-L000025](../../tests/test_answer_quality_review_scorecard.py#L25) | 25 | `"def test_manual_scorecard_aggregates_only_explicit_reviewed_metrics():"` | — |
| [SRC-D186ED3822-L000026](../../tests/test_answer_quality_review_scorecard.py#L26) | 26 | `"    mod = load_module()"` | — |
| [SRC-D186ED3822-L000027](../../tests/test_answer_quality_review_scorecard.py#L27) | 27 | `"    data = {"` | — |
| [SRC-D186ED3822-L000028](../../tests/test_answer_quality_review_scorecard.py#L28) | 28 | `"        \"schema_version\": \"1.0\","` | — |
| [SRC-D186ED3822-L000029](../../tests/test_answer_quality_review_scorecard.py#L29) | 29 | `"        \"reviews\": ["` | — |
| [SRC-D186ED3822-L000030](../../tests/test_answer_quality_review_scorecard.py#L30) | 30 | `"            {"` | — |
| [SRC-D186ED3822-L000031](../../tests/test_answer_quality_review_scorecard.py#L31) | 31 | `"                \"case_id\": \"AQ-007\","` | — |
| [SRC-D186ED3822-L000032](../../tests/test_answer_quality_review_scorecard.py#L32) | 32 | `"                \"status\": \"REVIEWED\","` | — |
| [SRC-D186ED3822-L000033](../../tests/test_answer_quality_review_scorecard.py#L33) | 33 | `"                \"retrieval\": {\"relevant_retrieved\": 3, \"retrieved_count\": 5, \"relevant_available\": 4},"` | — |
| [SRC-D186ED3822-L000034](../../tests/test_answer_quality_review_scorecard.py#L34) | 34 | `"                \"faithfulness\": {\"supported_claims\": 4, \"reviewed_claims\": 5},"` | — |
| [SRC-D186ED3822-L000035](../../tests/test_answer_quality_review_scorecard.py#L35) | 35 | `"                \"correctness\": {\"correct_facts\": 3, \"reviewed_facts\": 4},"` | — |
| [SRC-D186ED3822-L000036](../../tests/test_answer_quality_review_scorecard.py#L36) | 36 | `"                \"citations\": {\"supported_citations\": 2, \"reviewed_citations\": 3},"` | — |
| [SRC-D186ED3822-L000037](../../tests/test_answer_quality_review_scorecard.py#L37) | 37 | `"                \"writing_quality\": 4,"` | — |
| [SRC-D186ED3822-L000038](../../tests/test_answer_quality_review_scorecard.py#L38) | 38 | `"            },"` | — |
| [SRC-D186ED3822-L000039](../../tests/test_answer_quality_review_scorecard.py#L39) | 39 | `"            {"` | — |
| [SRC-D186ED3822-L000040](../../tests/test_answer_quality_review_scorecard.py#L40) | 40 | `"                \"case_id\": \"AQ-008\","` | — |
| [SRC-D186ED3822-L000041](../../tests/test_answer_quality_review_scorecard.py#L41) | 41 | `"                \"status\": \"REVIEWED\","` | — |
| [SRC-D186ED3822-L000042](../../tests/test_answer_quality_review_scorecard.py#L42) | 42 | `"                \"writing_quality\": 4,"` | — |
| [SRC-D186ED3822-L000043](../../tests/test_answer_quality_review_scorecard.py#L43) | 43 | `"            },"` | — |
| [SRC-D186ED3822-L000044](../../tests/test_answer_quality_review_scorecard.py#L44) | 44 | `"            {\"case_id\": \"AQ-009\", \"status\": \"NOT_TESTED\", \"notes\": \"No reviewer judgment yet.\"},"` | — |
| [SRC-D186ED3822-L000045](../../tests/test_answer_quality_review_scorecard.py#L45) | 45 | `"        ],"` | — |
| [SRC-D186ED3822-L000046](../../tests/test_answer_quality_review_scorecard.py#L46) | 46 | `"    }"` | — |
| [SRC-D186ED3822-L000047](../../tests/test_answer_quality_review_scorecard.py#L47) | 47 | `"    result = mod.summarize_reviews(data, corpus())"` | — |
| [SRC-D186ED3822-L000048](../../tests/test_answer_quality_review_scorecard.py#L48) | 48 | `"    assert result[\"metrics\"][\"retrieval_precision\"][\"score\"] == 0.6"` | — |
| [SRC-D186ED3822-L000049](../../tests/test_answer_quality_review_scorecard.py#L49) | 49 | `"    assert result[\"metrics\"][\"retrieval_recall\"][\"score\"] == 0.75"` | — |
| [SRC-D186ED3822-L000050](../../tests/test_answer_quality_review_scorecard.py#L50) | 50 | `"    assert result[\"metrics\"][\"faithfulness\"][\"score\"] == 0.8"` | — |
| [SRC-D186ED3822-L000051](../../tests/test_answer_quality_review_scorecard.py#L51) | 51 | `"    assert result[\"metrics\"][\"correctness\"][\"score\"] == 0.75"` | — |
| [SRC-D186ED3822-L000052](../../tests/test_answer_quality_review_scorecard.py#L52) | 52 | `"    assert result[\"metrics\"][\"citation_support\"][\"score\"] == pytest.approx(2 / 3, abs=0.0001)"` | — |
| [SRC-D186ED3822-L000053](../../tests/test_answer_quality_review_scorecard.py#L53) | 53 | `"    assert result[\"metrics\"][\"writing_quality_1_to_5\"][\"score\"] == 4.0"` | — |
| [SRC-D186ED3822-L000054](../../tests/test_answer_quality_review_scorecard.py#L54) | 54 | `"    assert result[\"case_status_counts\"][\"NOT_TESTED\"] == 1"` | — |
| [SRC-D186ED3822-L000055](../../tests/test_answer_quality_review_scorecard.py#L55) | 55 | `"    assert result[\"unique_reviewed_case_count\"] == 2"` | — |
| [SRC-D186ED3822-L000056](../../tests/test_answer_quality_review_scorecard.py#L56) | 56 | `"    assert result[\"automatic_answer_grading\"] is False"` | — |
| [SRC-D186ED3822-L000057](../../tests/test_answer_quality_review_scorecard.py#L57) | 57 | `"    assert result[\"ragas_executed\"] is False"` | — |
| [SRC-D186ED3822-L000058](../../tests/test_answer_quality_review_scorecard.py#L58) | 58 | `""` | — |
| [SRC-D186ED3822-L000059](../../tests/test_answer_quality_review_scorecard.py#L59) | 59 | `""` | — |
| [SRC-D186ED3822-L000060](../../tests/test_answer_quality_review_scorecard.py#L60) | 60 | `"def test_scorecard_keeps_unmeasured_denominators_not_scorable():"` | — |
| [SRC-D186ED3822-L000061](../../tests/test_answer_quality_review_scorecard.py#L61) | 61 | `"    mod = load_module()"` | — |
| [SRC-D186ED3822-L000062](../../tests/test_answer_quality_review_scorecard.py#L62) | 62 | `"    data = {"` | — |
| [SRC-D186ED3822-L000063](../../tests/test_answer_quality_review_scorecard.py#L63) | 63 | `"        \"reviews\": [{"` | — |
| [SRC-D186ED3822-L000064](../../tests/test_answer_quality_review_scorecard.py#L64) | 64 | `"            \"case_id\": \"AQ-001\","` | — |
| [SRC-D186ED3822-L000065](../../tests/test_answer_quality_review_scorecard.py#L65) | 65 | `"            \"status\": \"REVIEWED\","` | — |
| [SRC-D186ED3822-L000066](../../tests/test_answer_quality_review_scorecard.py#L66) | 66 | `"            \"faithfulness\": {\"supported_claims\": 0, \"reviewed_claims\": 0},"` | — |
| [SRC-D186ED3822-L000067](../../tests/test_answer_quality_review_scorecard.py#L67) | 67 | `"        }],"` | — |
| [SRC-D186ED3822-L000068](../../tests/test_answer_quality_review_scorecard.py#L68) | 68 | `"    }"` | — |
| [SRC-D186ED3822-L000069](../../tests/test_answer_quality_review_scorecard.py#L69) | 69 | `"    result = mod.summarize_reviews(data, corpus())"` | — |
| [SRC-D186ED3822-L000070](../../tests/test_answer_quality_review_scorecard.py#L70) | 70 | `"    assert result[\"metrics\"][\"faithfulness\"][\"score\"] is None"` | — |
| [SRC-D186ED3822-L000071](../../tests/test_answer_quality_review_scorecard.py#L71) | 71 | `"    assert result[\"metrics\"][\"faithfulness\"][\"status\"] == \"NOT_SCORABLE_NO_ANNOTATED_DENOMINATOR\""` | — |
| [SRC-D186ED3822-L000072](../../tests/test_answer_quality_review_scorecard.py#L72) | 72 | `"    assert result[\"metrics\"][\"retrieval_precision\"][\"score\"] is None"` | — |
| [SRC-D186ED3822-L000073](../../tests/test_answer_quality_review_scorecard.py#L73) | 73 | `""` | — |
| [SRC-D186ED3822-L000074](../../tests/test_answer_quality_review_scorecard.py#L74) | 74 | `""` | — |
| [SRC-D186ED3822-L000075](../../tests/test_answer_quality_review_scorecard.py#L75) | 75 | `"def test_scorecard_rejects_numerator_larger_than_denominator():"` | — |
| [SRC-D186ED3822-L000076](../../tests/test_answer_quality_review_scorecard.py#L76) | 76 | `"    mod = load_module()"` | — |
| [SRC-D186ED3822-L000077](../../tests/test_answer_quality_review_scorecard.py#L77) | 77 | `"    data = {"` | — |
| [SRC-D186ED3822-L000078](../../tests/test_answer_quality_review_scorecard.py#L78) | 78 | `"        \"reviews\": [{"` | — |
| [SRC-D186ED3822-L000079](../../tests/test_answer_quality_review_scorecard.py#L79) | 79 | `"            \"case_id\": \"AQ-007\","` | — |
| [SRC-D186ED3822-L000080](../../tests/test_answer_quality_review_scorecard.py#L80) | 80 | `"            \"status\": \"REVIEWED\","` | — |
| [SRC-D186ED3822-L000081](../../tests/test_answer_quality_review_scorecard.py#L81) | 81 | `"            \"faithfulness\": {\"supported_claims\": 3, \"reviewed_claims\": 2},"` | — |
| [SRC-D186ED3822-L000082](../../tests/test_answer_quality_review_scorecard.py#L82) | 82 | `"        }],"` | — |
| [SRC-D186ED3822-L000083](../../tests/test_answer_quality_review_scorecard.py#L83) | 83 | `"    }"` | — |
| [SRC-D186ED3822-L000084](../../tests/test_answer_quality_review_scorecard.py#L84) | 84 | `"    with pytest.raises(ValueError, match=\"cannot exceed\"):"` | — |
| [SRC-D186ED3822-L000085](../../tests/test_answer_quality_review_scorecard.py#L85) | 85 | `"        mod.summarize_reviews(data, corpus())"` | — |
| [SRC-D186ED3822-L000086](../../tests/test_answer_quality_review_scorecard.py#L86) | 86 | `""` | — |
| [SRC-D186ED3822-L000087](../../tests/test_answer_quality_review_scorecard.py#L87) | 87 | `""` | — |
| [SRC-D186ED3822-L000088](../../tests/test_answer_quality_review_scorecard.py#L88) | 88 | `"def test_scorecard_rejects_unknown_case_ids_and_duplicate_reviews():"` | — |
| [SRC-D186ED3822-L000089](../../tests/test_answer_quality_review_scorecard.py#L89) | 89 | `"    mod = load_module()"` | — |
| [SRC-D186ED3822-L000090](../../tests/test_answer_quality_review_scorecard.py#L90) | 90 | `"    data = {\"reviews\": ["` | — |
| [SRC-D186ED3822-L000091](../../tests/test_answer_quality_review_scorecard.py#L91) | 91 | `"        {\"case_id\": \"AQ-999\", \"status\": \"NOT_TESTED\"},"` | — |
| [SRC-D186ED3822-L000092](../../tests/test_answer_quality_review_scorecard.py#L92) | 92 | `"        {\"case_id\": \"AQ-001\", \"status\": \"NOT_TESTED\"},"` | — |
| [SRC-D186ED3822-L000093](../../tests/test_answer_quality_review_scorecard.py#L93) | 93 | `"        {\"case_id\": \"AQ-001\", \"status\": \"NOT_TESTED\"},"` | — |
| [SRC-D186ED3822-L000094](../../tests/test_answer_quality_review_scorecard.py#L94) | 94 | `"    ]}"` | — |
| [SRC-D186ED3822-L000095](../../tests/test_answer_quality_review_scorecard.py#L95) | 95 | `"    issues = mod.validate_reviews(data, corpus())"` | — |
| [SRC-D186ED3822-L000096](../../tests/test_answer_quality_review_scorecard.py#L96) | 96 | `"    assert any(\"unknown case_id\" in issue for issue in issues)"` | — |
| [SRC-D186ED3822-L000097](../../tests/test_answer_quality_review_scorecard.py#L97) | 97 | `"    assert any(\"duplicate review\" in issue for issue in issues)"` | — |
| [SRC-D186ED3822-L000098](../../tests/test_answer_quality_review_scorecard.py#L98) | 98 | `""` | — |
| [SRC-D186ED3822-L000099](../../tests/test_answer_quality_review_scorecard.py#L99) | 99 | `""` | — |
| [SRC-D186ED3822-L000100](../../tests/test_answer_quality_review_scorecard.py#L100) | 100 | `"def test_not_tested_cases_must_not_carry_metric_scores():"` | — |
| [SRC-D186ED3822-L000101](../../tests/test_answer_quality_review_scorecard.py#L101) | 101 | `"    mod = load_module()"` | — |
| [SRC-D186ED3822-L000102](../../tests/test_answer_quality_review_scorecard.py#L102) | 102 | `"    data = {\"reviews\": [{"` | — |
| [SRC-D186ED3822-L000103](../../tests/test_answer_quality_review_scorecard.py#L103) | 103 | `"        \"case_id\": \"AQ-001\", \"status\": \"NOT_TESTED\","` | — |
| [SRC-D186ED3822-L000104](../../tests/test_answer_quality_review_scorecard.py#L104) | 104 | `"        \"writing_quality\": 5,"` | — |
| [SRC-D186ED3822-L000105](../../tests/test_answer_quality_review_scorecard.py#L105) | 105 | `"    }]}"` | — |
| [SRC-D186ED3822-L000106](../../tests/test_answer_quality_review_scorecard.py#L106) | 106 | `"    issues = mod.validate_reviews(data, corpus())"` | — |
| [SRC-D186ED3822-L000107](../../tests/test_answer_quality_review_scorecard.py#L107) | 107 | `"    assert any(\"unreviewed case must not contain metric scores\" in issue for issue in issues)"` | — |
| [SRC-D186ED3822-L000108](../../tests/test_answer_quality_review_scorecard.py#L108) | 108 | `""` | — |
| [SRC-D186ED3822-L000109](../../tests/test_answer_quality_review_scorecard.py#L109) | 109 | `""` | — |
| [SRC-D186ED3822-L000110](../../tests/test_answer_quality_review_scorecard.py#L110) | 110 | `"def test_scorecard_cli_writes_a_machine_readable_summary(tmp_path, capsys):"` | — |
| [SRC-D186ED3822-L000111](../../tests/test_answer_quality_review_scorecard.py#L111) | 111 | `"    mod = load_module()"` | — |
| [SRC-D186ED3822-L000112](../../tests/test_answer_quality_review_scorecard.py#L112) | 112 | `"    reviews_path = tmp_path / \"reviews.json\""` | — |
| [SRC-D186ED3822-L000113](../../tests/test_answer_quality_review_scorecard.py#L113) | 113 | `"    output_path = tmp_path / \"summary.json\""` | — |
| [SRC-D186ED3822-L000114](../../tests/test_answer_quality_review_scorecard.py#L114) | 114 | `"    reviews_path.write_text('{\"schema_version\":\"1.0\",\"reviews\":[{\"case_id\":\"AQ-001\",\"status\":\"REVIEWED\",\"writing_quality\":5}]}', encoding=\"utf-8\")"` | — |
| [SRC-D186ED3822-L000115](../../tests/test_answer_quality_review_scorecard.py#L115) | 115 | `"    rc = mod.main([\"--reviews\", str(reviews_path), \"--corpus\", str(CORPUS_PATH), \"--out\", str(output_path)])"` | — |
| [SRC-D186ED3822-L000116](../../tests/test_answer_quality_review_scorecard.py#L116) | 116 | `"    assert rc == 0"` | — |
| [SRC-D186ED3822-L000117](../../tests/test_answer_quality_review_scorecard.py#L117) | 117 | `"    assert '\"score\": 5.0' in capsys.readouterr().out"` | — |
| [SRC-D186ED3822-L000118](../../tests/test_answer_quality_review_scorecard.py#L118) | 118 | `"    assert output_path.is_file()"` | — |
## اختبارات

### FILE-B3062EB677 — [tests/test_answer_quality_runner.py](../../tests/test_answer_quality_runner.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-B3062EB677-L000001](../../tests/test_answer_quality_runner.py#L1) | 1 | `"\"\"\"Offline tests for scripts/run_answer_quality_benchmark.py (no network).\"\"\""` | — |
| [SRC-B3062EB677-L000002](../../tests/test_answer_quality_runner.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-B3062EB677-L000003](../../tests/test_answer_quality_runner.py#L3) | 3 | `""` | — |
| [SRC-B3062EB677-L000004](../../tests/test_answer_quality_runner.py#L4) | 4 | `"import importlib.util"` | — |
| [SRC-B3062EB677-L000005](../../tests/test_answer_quality_runner.py#L5) | 5 | `"import json"` | — |
| [SRC-B3062EB677-L000006](../../tests/test_answer_quality_runner.py#L6) | 6 | `"import sys"` | — |
| [SRC-B3062EB677-L000007](../../tests/test_answer_quality_runner.py#L7) | 7 | `"from pathlib import Path"` | — |
| [SRC-B3062EB677-L000008](../../tests/test_answer_quality_runner.py#L8) | 8 | `""` | — |
| [SRC-B3062EB677-L000009](../../tests/test_answer_quality_runner.py#L9) | 9 | `"import pytest"` | — |
| [SRC-B3062EB677-L000010](../../tests/test_answer_quality_runner.py#L10) | 10 | `""` | — |
| [SRC-B3062EB677-L000011](../../tests/test_answer_quality_runner.py#L11) | 11 | `"ROOT = Path(__file__).resolve().parents[1]"` | — |
| [SRC-B3062EB677-L000012](../../tests/test_answer_quality_runner.py#L12) | 12 | `"SCRIPT = ROOT / \"scripts\" / \"run_answer_quality_benchmark.py\""` | — |
| [SRC-B3062EB677-L000013](../../tests/test_answer_quality_runner.py#L13) | 13 | `"CORPUS = ROOT / \"tests\" / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-B3062EB677-L000014](../../tests/test_answer_quality_runner.py#L14) | 14 | `""` | — |
| [SRC-B3062EB677-L000015](../../tests/test_answer_quality_runner.py#L15) | 15 | `""` | — |
| [SRC-B3062EB677-L000016](../../tests/test_answer_quality_runner.py#L16) | 16 | `"def _load_runner():"` | — |
| [SRC-B3062EB677-L000017](../../tests/test_answer_quality_runner.py#L17) | 17 | `"    spec = importlib.util.spec_from_file_location(\"aq_runner\", SCRIPT)"` | — |
| [SRC-B3062EB677-L000018](../../tests/test_answer_quality_runner.py#L18) | 18 | `"    assert spec and spec.loader"` | — |
| [SRC-B3062EB677-L000019](../../tests/test_answer_quality_runner.py#L19) | 19 | `"    mod = importlib.util.module_from_spec(spec)"` | — |
| [SRC-B3062EB677-L000020](../../tests/test_answer_quality_runner.py#L20) | 20 | `"    sys.modules[\"aq_runner\"] = mod"` | — |
| [SRC-B3062EB677-L000021](../../tests/test_answer_quality_runner.py#L21) | 21 | `"    spec.loader.exec_module(mod)"` | — |
| [SRC-B3062EB677-L000022](../../tests/test_answer_quality_runner.py#L22) | 22 | `"    return mod"` | — |
| [SRC-B3062EB677-L000023](../../tests/test_answer_quality_runner.py#L23) | 23 | `""` | — |
| [SRC-B3062EB677-L000024](../../tests/test_answer_quality_runner.py#L24) | 24 | `""` | — |
| [SRC-B3062EB677-L000025](../../tests/test_answer_quality_runner.py#L25) | 25 | `"def test_runner_script_exists():"` | — |
| [SRC-B3062EB677-L000026](../../tests/test_answer_quality_runner.py#L26) | 26 | `"    assert SCRIPT.is_file()"` | — |
| [SRC-B3062EB677-L000027](../../tests/test_answer_quality_runner.py#L27) | 27 | `""` | — |
| [SRC-B3062EB677-L000028](../../tests/test_answer_quality_runner.py#L28) | 28 | `""` | — |
| [SRC-B3062EB677-L000029](../../tests/test_answer_quality_runner.py#L29) | 29 | `"def test_validate_mode_succeeds_on_real_corpus(capsys):"` | — |
| [SRC-B3062EB677-L000030](../../tests/test_answer_quality_runner.py#L30) | 30 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000031](../../tests/test_answer_quality_runner.py#L31) | 31 | `"    rc = mod.main([\"--mode\", \"validate\", \"--corpus\", str(CORPUS), \"--summary\"])"` | — |
| [SRC-B3062EB677-L000032](../../tests/test_answer_quality_runner.py#L32) | 32 | `"    assert rc == 0"` | — |
| [SRC-B3062EB677-L000033](../../tests/test_answer_quality_runner.py#L33) | 33 | `"    out = capsys.readouterr().out"` | — |
| [SRC-B3062EB677-L000034](../../tests/test_answer_quality_runner.py#L34) | 34 | `"    assert \"VALIDATE OK\" in out"` | — |
| [SRC-B3062EB677-L000035](../../tests/test_answer_quality_runner.py#L35) | 35 | `"    assert \"NOT_TESTED\" in out"` | — |
| [SRC-B3062EB677-L000036](../../tests/test_answer_quality_runner.py#L36) | 36 | `""` | — |
| [SRC-B3062EB677-L000037](../../tests/test_answer_quality_runner.py#L37) | 37 | `""` | — |
| [SRC-B3062EB677-L000038](../../tests/test_answer_quality_runner.py#L38) | 38 | `"def test_validate_rejects_missing_file(tmp_path):"` | — |
| [SRC-B3062EB677-L000039](../../tests/test_answer_quality_runner.py#L39) | 39 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000040](../../tests/test_answer_quality_runner.py#L40) | 40 | `"    missing = tmp_path / \"nope.json\""` | — |
| [SRC-B3062EB677-L000041](../../tests/test_answer_quality_runner.py#L41) | 41 | `"    with pytest.raises(FileNotFoundError):"` | — |
| [SRC-B3062EB677-L000042](../../tests/test_answer_quality_runner.py#L42) | 42 | `"        mod.load_corpus(missing)"` | — |
| [SRC-B3062EB677-L000043](../../tests/test_answer_quality_runner.py#L43) | 43 | `""` | — |
| [SRC-B3062EB677-L000044](../../tests/test_answer_quality_runner.py#L44) | 44 | `""` | — |
| [SRC-B3062EB677-L000045](../../tests/test_answer_quality_runner.py#L45) | 45 | `"def test_validate_detects_bad_case_count(tmp_path):"` | — |
| [SRC-B3062EB677-L000046](../../tests/test_answer_quality_runner.py#L46) | 46 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000047](../../tests/test_answer_quality_runner.py#L47) | 47 | `"    data = json.loads(CORPUS.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-B3062EB677-L000048](../../tests/test_answer_quality_runner.py#L48) | 48 | `"    data[\"case_count\"] = 999"` | — |
| [SRC-B3062EB677-L000049](../../tests/test_answer_quality_runner.py#L49) | 49 | `"    bad = tmp_path / \"bad.json\""` | — |
| [SRC-B3062EB677-L000050](../../tests/test_answer_quality_runner.py#L50) | 50 | `"    bad.write_text(json.dumps(data), encoding=\"utf-8\")"` | — |
| [SRC-B3062EB677-L000051](../../tests/test_answer_quality_runner.py#L51) | 51 | `"    problems = mod.validate_corpus(mod.load_corpus(bad))"` | — |
| [SRC-B3062EB677-L000052](../../tests/test_answer_quality_runner.py#L52) | 52 | `"    assert any(\"case_count\" in p for p in problems)"` | — |
| [SRC-B3062EB677-L000053](../../tests/test_answer_quality_runner.py#L53) | 53 | `""` | — |
| [SRC-B3062EB677-L000054](../../tests/test_answer_quality_runner.py#L54) | 54 | `""` | — |
| [SRC-B3062EB677-L000055](../../tests/test_answer_quality_runner.py#L55) | 55 | `"def test_validate_detects_missing_required_field(tmp_path):"` | — |
| [SRC-B3062EB677-L000056](../../tests/test_answer_quality_runner.py#L56) | 56 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000057](../../tests/test_answer_quality_runner.py#L57) | 57 | `"    data = json.loads(CORPUS.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-B3062EB677-L000058](../../tests/test_answer_quality_runner.py#L58) | 58 | `"    data[\"cases\"] = [dict(data[\"cases\"][0])]"` | — |
| [SRC-B3062EB677-L000059](../../tests/test_answer_quality_runner.py#L59) | 59 | `"    del data[\"cases\"][0][\"question\"]"` | — |
| [SRC-B3062EB677-L000060](../../tests/test_answer_quality_runner.py#L60) | 60 | `"    data[\"case_count\"] = 1"` | — |
| [SRC-B3062EB677-L000061](../../tests/test_answer_quality_runner.py#L61) | 61 | `"    bad = tmp_path / \"bad2.json\""` | — |
| [SRC-B3062EB677-L000062](../../tests/test_answer_quality_runner.py#L62) | 62 | `"    bad.write_text(json.dumps(data), encoding=\"utf-8\")"` | — |
| [SRC-B3062EB677-L000063](../../tests/test_answer_quality_runner.py#L63) | 63 | `"    problems = mod.validate_corpus(mod.load_corpus(bad))"` | — |
| [SRC-B3062EB677-L000064](../../tests/test_answer_quality_runner.py#L64) | 64 | `"    assert problems"` | — |
| [SRC-B3062EB677-L000065](../../tests/test_answer_quality_runner.py#L65) | 65 | `""` | — |
| [SRC-B3062EB677-L000066](../../tests/test_answer_quality_runner.py#L66) | 66 | `""` | — |
| [SRC-B3062EB677-L000067](../../tests/test_answer_quality_runner.py#L67) | 67 | `"def test_live_refuses_unbounded_without_limit_or_case_id(capsys):"` | — |
| [SRC-B3062EB677-L000068](../../tests/test_answer_quality_runner.py#L68) | 68 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000069](../../tests/test_answer_quality_runner.py#L69) | 69 | `"    rc = mod.main([\"--mode\", \"live\", \"--corpus\", str(CORPUS)])"` | — |
| [SRC-B3062EB677-L000070](../../tests/test_answer_quality_runner.py#L70) | 70 | `"    assert rc == 2"` | — |
| [SRC-B3062EB677-L000071](../../tests/test_answer_quality_runner.py#L71) | 71 | `"    err = capsys.readouterr().err"` | — |
| [SRC-B3062EB677-L000072](../../tests/test_answer_quality_runner.py#L72) | 72 | `"    assert \"Refusing unbounded\" in err"` | — |
| [SRC-B3062EB677-L000073](../../tests/test_answer_quality_runner.py#L73) | 73 | `""` | — |
| [SRC-B3062EB677-L000074](../../tests/test_answer_quality_runner.py#L74) | 74 | `""` | — |
| [SRC-B3062EB677-L000075](../../tests/test_answer_quality_runner.py#L75) | 75 | `"def test_live_unknown_case_id(capsys):"` | — |
| [SRC-B3062EB677-L000076](../../tests/test_answer_quality_runner.py#L76) | 76 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000077](../../tests/test_answer_quality_runner.py#L77) | 77 | `"    rc = mod.main("` | — |
| [SRC-B3062EB677-L000078](../../tests/test_answer_quality_runner.py#L78) | 78 | `"        ["` | — |
| [SRC-B3062EB677-L000079](../../tests/test_answer_quality_runner.py#L79) | 79 | `"            \"--mode\","` | — |
| [SRC-B3062EB677-L000080](../../tests/test_answer_quality_runner.py#L80) | 80 | `"            \"live\","` | — |
| [SRC-B3062EB677-L000081](../../tests/test_answer_quality_runner.py#L81) | 81 | `"            \"--corpus\","` | — |
| [SRC-B3062EB677-L000082](../../tests/test_answer_quality_runner.py#L82) | 82 | `"            str(CORPUS),"` | — |
| [SRC-B3062EB677-L000083](../../tests/test_answer_quality_runner.py#L83) | 83 | `"            \"--case-id\","` | — |
| [SRC-B3062EB677-L000084](../../tests/test_answer_quality_runner.py#L84) | 84 | `"            \"AQ-999\","` | — |
| [SRC-B3062EB677-L000085](../../tests/test_answer_quality_runner.py#L85) | 85 | `"            \"--base-url\","` | — |
| [SRC-B3062EB677-L000086](../../tests/test_answer_quality_runner.py#L86) | 86 | `"            \"http://127.0.0.1:9\","` | — |
| [SRC-B3062EB677-L000087](../../tests/test_answer_quality_runner.py#L87) | 87 | `"        ]"` | — |
| [SRC-B3062EB677-L000088](../../tests/test_answer_quality_runner.py#L88) | 88 | `"    )"` | — |
| [SRC-B3062EB677-L000089](../../tests/test_answer_quality_runner.py#L89) | 89 | `"    assert rc == 2"` | — |
| [SRC-B3062EB677-L000090](../../tests/test_answer_quality_runner.py#L90) | 90 | `""` | — |
| [SRC-B3062EB677-L000091](../../tests/test_answer_quality_runner.py#L91) | 91 | `""` | — |
| [SRC-B3062EB677-L000092](../../tests/test_answer_quality_runner.py#L92) | 92 | `"def test_redact_secrets_strips_token_value(monkeypatch):"` | — |
| [SRC-B3062EB677-L000093](../../tests/test_answer_quality_runner.py#L93) | 93 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000094](../../tests/test_answer_quality_runner.py#L94) | 94 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"super-secret-token-value-xyz\")"` | — |
| [SRC-B3062EB677-L000095](../../tests/test_answer_quality_runner.py#L95) | 95 | `"    text = \"token=super-secret-token-value-xyz and OPENROUTER_API_KEY\""` | — |
| [SRC-B3062EB677-L000096](../../tests/test_answer_quality_runner.py#L96) | 96 | `"    out = mod.redact_secrets(text)"` | — |
| [SRC-B3062EB677-L000097](../../tests/test_answer_quality_runner.py#L97) | 97 | `"    assert \"super-secret-token-value-xyz\" not in out"` | — |
| [SRC-B3062EB677-L000098](../../tests/test_answer_quality_runner.py#L98) | 98 | `"    assert \"REDACTED\" in out"` | — |
| [SRC-B3062EB677-L000099](../../tests/test_answer_quality_runner.py#L99) | 99 | `""` | — |
| [SRC-B3062EB677-L000100](../../tests/test_answer_quality_runner.py#L100) | 100 | `""` | — |
| [SRC-B3062EB677-L000101](../../tests/test_answer_quality_runner.py#L101) | 101 | `"def test_live_records_not_tested_not_pass(monkeypatch, tmp_path, capsys):"` | — |
| [SRC-B3062EB677-L000102](../../tests/test_answer_quality_runner.py#L102) | 102 | `"    \"\"\"Even on HTTP 200, quality status stays NOT_TESTED (no keyword auto-PASS).\"\"\""` | — |
| [SRC-B3062EB677-L000103](../../tests/test_answer_quality_runner.py#L103) | 103 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000104](../../tests/test_answer_quality_runner.py#L104) | 104 | `""` | — |
| [SRC-B3062EB677-L000105](../../tests/test_answer_quality_runner.py#L105) | 105 | `"    def fake_post(base_url, question, timeout, token):"` | — |
| [SRC-B3062EB677-L000106](../../tests/test_answer_quality_runner.py#L106) | 106 | `"        return 200, {"` | — |
| [SRC-B3062EB677-L000107](../../tests/test_answer_quality_runner.py#L107) | 107 | `"            \"answer\": \"hello used_web_search should not force PASS\","` | — |
| [SRC-B3062EB677-L000108](../../tests/test_answer_quality_runner.py#L108) | 108 | `"            \"used_web_search\": False,"` | — |
| [SRC-B3062EB677-L000109](../../tests/test_answer_quality_runner.py#L109) | 109 | `"            \"used_language_model\": True,"` | — |
| [SRC-B3062EB677-L000110](../../tests/test_answer_quality_runner.py#L110) | 110 | `"            \"sources\": [],"` | — |
| [SRC-B3062EB677-L000111](../../tests/test_answer_quality_runner.py#L111) | 111 | `"        }"` | — |
| [SRC-B3062EB677-L000112](../../tests/test_answer_quality_runner.py#L112) | 112 | `""` | — |
| [SRC-B3062EB677-L000113](../../tests/test_answer_quality_runner.py#L113) | 113 | `"    monkeypatch.setattr(mod, \"get_verified_build_sha\", lambda base_url, timeout, token=None: \"a\" * 40)"` | — |
| [SRC-B3062EB677-L000114](../../tests/test_answer_quality_runner.py#L114) | 114 | `"    monkeypatch.setattr(mod, \"post_agent\", fake_post)"` | — |
| [SRC-B3062EB677-L000115](../../tests/test_answer_quality_runner.py#L115) | 115 | `"    out = tmp_path / \"results.json\""` | — |
| [SRC-B3062EB677-L000116](../../tests/test_answer_quality_runner.py#L116) | 116 | `"    rc = mod.main("` | — |
| [SRC-B3062EB677-L000117](../../tests/test_answer_quality_runner.py#L117) | 117 | `"        ["` | — |
| [SRC-B3062EB677-L000118](../../tests/test_answer_quality_runner.py#L118) | 118 | `"            \"--mode\","` | — |
| [SRC-B3062EB677-L000119](../../tests/test_answer_quality_runner.py#L119) | 119 | `"            \"live\","` | — |
| [SRC-B3062EB677-L000120](../../tests/test_answer_quality_runner.py#L120) | 120 | `"            \"--corpus\","` | — |
| [SRC-B3062EB677-L000121](../../tests/test_answer_quality_runner.py#L121) | 121 | `"            str(CORPUS),"` | — |
| [SRC-B3062EB677-L000122](../../tests/test_answer_quality_runner.py#L122) | 122 | `"            \"--case-id\","` | — |
| [SRC-B3062EB677-L000123](../../tests/test_answer_quality_runner.py#L123) | 123 | `"            \"AQ-001\","` | — |
| [SRC-B3062EB677-L000124](../../tests/test_answer_quality_runner.py#L124) | 124 | `"            \"--limit\","` | — |
| [SRC-B3062EB677-L000125](../../tests/test_answer_quality_runner.py#L125) | 125 | `"            \"1\","` | — |
| [SRC-B3062EB677-L000126](../../tests/test_answer_quality_runner.py#L126) | 126 | `"            \"--out\","` | — |
| [SRC-B3062EB677-L000127](../../tests/test_answer_quality_runner.py#L127) | 127 | `"            str(out),"` | — |
| [SRC-B3062EB677-L000128](../../tests/test_answer_quality_runner.py#L128) | 128 | `"        ]"` | — |
| [SRC-B3062EB677-L000129](../../tests/test_answer_quality_runner.py#L129) | 129 | `"    )"` | — |
| [SRC-B3062EB677-L000130](../../tests/test_answer_quality_runner.py#L130) | 130 | `"    assert rc == 0"` | — |
| [SRC-B3062EB677-L000131](../../tests/test_answer_quality_runner.py#L131) | 131 | `"    payload = json.loads(out.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-B3062EB677-L000132](../../tests/test_answer_quality_runner.py#L132) | 132 | `"    assert payload[\"results\"][0][\"status\"] == \"NOT_TESTED\""` | — |
| [SRC-B3062EB677-L000133](../../tests/test_answer_quality_runner.py#L133) | 133 | `"    assert payload[\"results\"][0][\"evidence_fixture_injected\"] is False"` | — |
| [SRC-B3062EB677-L000134](../../tests/test_answer_quality_runner.py#L134) | 134 | `"    assert payload[\"results\"][0][\"transport_ok\"] is True"` | — |
| [SRC-B3062EB677-L000135](../../tests/test_answer_quality_runner.py#L135) | 135 | `"    assert payload[\"build_sha\"] == \"a\" * 40"` | — |
| [SRC-B3062EB677-L000136](../../tests/test_answer_quality_runner.py#L136) | 136 | `"    assert payload[\"build_sha_verification\"] == \"confirmed_by_api_health\""` | — |
| [SRC-B3062EB677-L000137](../../tests/test_answer_quality_runner.py#L137) | 137 | `""` | — |
| [SRC-B3062EB677-L000138](../../tests/test_answer_quality_runner.py#L138) | 138 | `""` | — |
| [SRC-B3062EB677-L000139](../../tests/test_answer_quality_runner.py#L139) | 139 | `"def test_validate_base_url_rejects_non_loopback_http():"` | — |
| [SRC-B3062EB677-L000140](../../tests/test_answer_quality_runner.py#L140) | 140 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000141](../../tests/test_answer_quality_runner.py#L141) | 141 | `"    with pytest.raises(ValueError, match=\"Plain HTTP\"):"` | — |
| [SRC-B3062EB677-L000142](../../tests/test_answer_quality_runner.py#L142) | 142 | `"        mod.validate_base_url(\"http://research.example\")"` | — |
| [SRC-B3062EB677-L000143](../../tests/test_answer_quality_runner.py#L143) | 143 | `""` | — |
| [SRC-B3062EB677-L000144](../../tests/test_answer_quality_runner.py#L144) | 144 | `""` | — |
| [SRC-B3062EB677-L000145](../../tests/test_answer_quality_runner.py#L145) | 145 | `"@pytest.mark.parametrize("` | — |
| [SRC-B3062EB677-L000146](../../tests/test_answer_quality_runner.py#L146) | 146 | `"    \"url\","` | — |
| [SRC-B3062EB677-L000147](../../tests/test_answer_quality_runner.py#L147) | 147 | `"    ["` | — |
| [SRC-B3062EB677-L000148](../../tests/test_answer_quality_runner.py#L148) | 148 | `"        \"https://user:password@example.com\","` | — |
| [SRC-B3062EB677-L000149](../../tests/test_answer_quality_runner.py#L149) | 149 | `"        \"https://example.com/private/path\","` | — |
| [SRC-B3062EB677-L000150](../../tests/test_answer_quality_runner.py#L150) | 150 | `"        \"https://example.com/?token=oops\","` | — |
| [SRC-B3062EB677-L000151](../../tests/test_answer_quality_runner.py#L151) | 151 | `"        \"https://example.com/#fragment\","` | — |
| [SRC-B3062EB677-L000152](../../tests/test_answer_quality_runner.py#L152) | 152 | `"    ],"` | — |
| [SRC-B3062EB677-L000153](../../tests/test_answer_quality_runner.py#L153) | 153 | `")"` | — |
| [SRC-B3062EB677-L000154](../../tests/test_answer_quality_runner.py#L154) | 154 | `"def test_validate_base_url_rejects_ambiguous_or_credential_bearing_urls(url):"` | — |
| [SRC-B3062EB677-L000155](../../tests/test_answer_quality_runner.py#L155) | 155 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000156](../../tests/test_answer_quality_runner.py#L156) | 156 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-B3062EB677-L000157](../../tests/test_answer_quality_runner.py#L157) | 157 | `"        mod.validate_base_url(url)"` | — |
| [SRC-B3062EB677-L000158](../../tests/test_answer_quality_runner.py#L158) | 158 | `""` | — |
| [SRC-B3062EB677-L000159](../../tests/test_answer_quality_runner.py#L159) | 159 | `""` | — |
| [SRC-B3062EB677-L000160](../../tests/test_answer_quality_runner.py#L160) | 160 | `"def test_remote_bearer_token_requires_exact_allowlisted_https_origin(monkeypatch):"` | — |
| [SRC-B3062EB677-L000161](../../tests/test_answer_quality_runner.py#L161) | 161 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000162](../../tests/test_answer_quality_runner.py#L162) | 162 | `"    monkeypatch.delenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", raising=False)"` | — |
| [SRC-B3062EB677-L000163](../../tests/test_answer_quality_runner.py#L163) | 163 | `"    with pytest.raises(ValueError, match=\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\"):"` | — |
| [SRC-B3062EB677-L000164](../../tests/test_answer_quality_runner.py#L164) | 164 | `"        mod.validate_base_url(\"https://app.example\", token_present=True)"` | — |
| [SRC-B3062EB677-L000165](../../tests/test_answer_quality_runner.py#L165) | 165 | `""` | — |
| [SRC-B3062EB677-L000166](../../tests/test_answer_quality_runner.py#L166) | 166 | `"    monkeypatch.setenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", \"https://app.example\")"` | — |
| [SRC-B3062EB677-L000167](../../tests/test_answer_quality_runner.py#L167) | 167 | `"    assert mod.validate_base_url(\"https://app.example/\", token_present=True) == \"https://app.example\""` | — |
| [SRC-B3062EB677-L000168](../../tests/test_answer_quality_runner.py#L168) | 168 | `"    with pytest.raises(ValueError, match=\"does not match\"):"` | — |
| [SRC-B3062EB677-L000169](../../tests/test_answer_quality_runner.py#L169) | 169 | `"        mod.validate_base_url(\"https://other.example\", token_present=True)"` | — |
| [SRC-B3062EB677-L000170](../../tests/test_answer_quality_runner.py#L170) | 170 | `""` | — |
| [SRC-B3062EB677-L000171](../../tests/test_answer_quality_runner.py#L171) | 171 | `""` | — |
| [SRC-B3062EB677-L000172](../../tests/test_answer_quality_runner.py#L172) | 172 | `"def test_remote_token_origin_comparison_normalizes_default_https_port(monkeypatch):"` | — |
| [SRC-B3062EB677-L000173](../../tests/test_answer_quality_runner.py#L173) | 173 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000174](../../tests/test_answer_quality_runner.py#L174) | 174 | `"    monkeypatch.setenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", \"https://app.example\")"` | — |
| [SRC-B3062EB677-L000175](../../tests/test_answer_quality_runner.py#L175) | 175 | `"    assert ("` | — |
| [SRC-B3062EB677-L000176](../../tests/test_answer_quality_runner.py#L176) | 176 | `"        mod.validate_base_url(\"https://app.example:443\", token_present=True)"` | — |
| [SRC-B3062EB677-L000177](../../tests/test_answer_quality_runner.py#L177) | 177 | `"        == \"https://app.example\""` | — |
| [SRC-B3062EB677-L000178](../../tests/test_answer_quality_runner.py#L178) | 178 | `"    )"` | — |
| [SRC-B3062EB677-L000179](../../tests/test_answer_quality_runner.py#L179) | 179 | `""` | — |
| [SRC-B3062EB677-L000180](../../tests/test_answer_quality_runner.py#L180) | 180 | `""` | — |
| [SRC-B3062EB677-L000181](../../tests/test_answer_quality_runner.py#L181) | 181 | `"def test_redirect_handler_refuses_following_redirects():"` | — |
| [SRC-B3062EB677-L000182](../../tests/test_answer_quality_runner.py#L182) | 182 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000183](../../tests/test_answer_quality_runner.py#L183) | 183 | `"    handler = mod._NoRedirectHandler()"` | — |
| [SRC-B3062EB677-L000184](../../tests/test_answer_quality_runner.py#L184) | 184 | `"    assert handler.redirect_request("` | — |
| [SRC-B3062EB677-L000185](../../tests/test_answer_quality_runner.py#L185) | 185 | `"        req=None,"` | — |
| [SRC-B3062EB677-L000186](../../tests/test_answer_quality_runner.py#L186) | 186 | `"        fp=None,"` | — |
| [SRC-B3062EB677-L000187](../../tests/test_answer_quality_runner.py#L187) | 187 | `"        code=302,"` | — |
| [SRC-B3062EB677-L000188](../../tests/test_answer_quality_runner.py#L188) | 188 | `"        msg=\"Found\","` | — |
| [SRC-B3062EB677-L000189](../../tests/test_answer_quality_runner.py#L189) | 189 | `"        headers={},"` | — |
| [SRC-B3062EB677-L000190](../../tests/test_answer_quality_runner.py#L190) | 190 | `"        newurl=\"https://attacker.example/collect\","` | — |
| [SRC-B3062EB677-L000191](../../tests/test_answer_quality_runner.py#L191) | 191 | `"    ) is None"` | — |
| [SRC-B3062EB677-L000192](../../tests/test_answer_quality_runner.py#L192) | 192 | `""` | — |
| [SRC-B3062EB677-L000193](../../tests/test_answer_quality_runner.py#L193) | 193 | `""` | — |
| [SRC-B3062EB677-L000194](../../tests/test_answer_quality_runner.py#L194) | 194 | `"def test_live_rejects_unapproved_remote_url_before_network(monkeypatch, capsys):"` | — |
| [SRC-B3062EB677-L000195](../../tests/test_answer_quality_runner.py#L195) | 195 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000196](../../tests/test_answer_quality_runner.py#L196) | 196 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"a-test-token\")"` | — |
| [SRC-B3062EB677-L000197](../../tests/test_answer_quality_runner.py#L197) | 197 | `"    monkeypatch.delenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", raising=False)"` | — |
| [SRC-B3062EB677-L000198](../../tests/test_answer_quality_runner.py#L198) | 198 | `"    rc = mod.run_live("` | — |
| [SRC-B3062EB677-L000199](../../tests/test_answer_quality_runner.py#L199) | 199 | `"        CORPUS,"` | — |
| [SRC-B3062EB677-L000200](../../tests/test_answer_quality_runner.py#L200) | 200 | `"        \"https://not-allowlisted.example\","` | — |
| [SRC-B3062EB677-L000201](../../tests/test_answer_quality_runner.py#L201) | 201 | `"        \"AQ-001\","` | — |
| [SRC-B3062EB677-L000202](../../tests/test_answer_quality_runner.py#L202) | 202 | `"        1,"` | — |
| [SRC-B3062EB677-L000203](../../tests/test_answer_quality_runner.py#L203) | 203 | `"        1.0,"` | — |
| [SRC-B3062EB677-L000204](../../tests/test_answer_quality_runner.py#L204) | 204 | `"        0.0,"` | — |
| [SRC-B3062EB677-L000205](../../tests/test_answer_quality_runner.py#L205) | 205 | `"        None,"` | — |
| [SRC-B3062EB677-L000206](../../tests/test_answer_quality_runner.py#L206) | 206 | `"    )"` | — |
| [SRC-B3062EB677-L000207](../../tests/test_answer_quality_runner.py#L207) | 207 | `"    assert rc == 2"` | — |
| [SRC-B3062EB677-L000208](../../tests/test_answer_quality_runner.py#L208) | 208 | `"    assert \"Unsafe base URL\" in capsys.readouterr().err"` | — |
| [SRC-B3062EB677-L000209](../../tests/test_answer_quality_runner.py#L209) | 209 | `""` | — |
| [SRC-B3062EB677-L000210](../../tests/test_answer_quality_runner.py#L210) | 210 | `""` | — |
| [SRC-B3062EB677-L000211](../../tests/test_answer_quality_runner.py#L211) | 211 | `"def test_live_transport_error_still_not_pass(monkeypatch, tmp_path):"` | — |
| [SRC-B3062EB677-L000212](../../tests/test_answer_quality_runner.py#L212) | 212 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000213](../../tests/test_answer_quality_runner.py#L213) | 213 | `""` | — |
| [SRC-B3062EB677-L000214](../../tests/test_answer_quality_runner.py#L214) | 214 | `"    def fake_post(base_url, question, timeout, token):"` | — |
| [SRC-B3062EB677-L000215](../../tests/test_answer_quality_runner.py#L215) | 215 | `"        return 0, {\"error\": \"URLError\", \"detail\": \"connection refused\"}"` | — |
| [SRC-B3062EB677-L000216](../../tests/test_answer_quality_runner.py#L216) | 216 | `""` | — |
| [SRC-B3062EB677-L000217](../../tests/test_answer_quality_runner.py#L217) | 217 | `"    monkeypatch.setattr(mod, \"get_verified_build_sha\", lambda base_url, timeout, token=None: \"b\" * 40)"` | — |
| [SRC-B3062EB677-L000218](../../tests/test_answer_quality_runner.py#L218) | 218 | `"    monkeypatch.setattr(mod, \"post_agent\", fake_post)"` | — |
| [SRC-B3062EB677-L000219](../../tests/test_answer_quality_runner.py#L219) | 219 | `"    out = tmp_path / \"results.json\""` | — |
| [SRC-B3062EB677-L000220](../../tests/test_answer_quality_runner.py#L220) | 220 | `"    rc = mod.main("` | — |
| [SRC-B3062EB677-L000221](../../tests/test_answer_quality_runner.py#L221) | 221 | `"        ["` | — |
| [SRC-B3062EB677-L000222](../../tests/test_answer_quality_runner.py#L222) | 222 | `"            \"--mode\","` | — |
| [SRC-B3062EB677-L000223](../../tests/test_answer_quality_runner.py#L223) | 223 | `"            \"live\","` | — |
| [SRC-B3062EB677-L000224](../../tests/test_answer_quality_runner.py#L224) | 224 | `"            \"--corpus\","` | — |
| [SRC-B3062EB677-L000225](../../tests/test_answer_quality_runner.py#L225) | 225 | `"            str(CORPUS),"` | — |
| [SRC-B3062EB677-L000226](../../tests/test_answer_quality_runner.py#L226) | 226 | `"            \"--case-id\","` | — |
| [SRC-B3062EB677-L000227](../../tests/test_answer_quality_runner.py#L227) | 227 | `"            \"AQ-001\","` | — |
| [SRC-B3062EB677-L000228](../../tests/test_answer_quality_runner.py#L228) | 228 | `"            \"--out\","` | — |
| [SRC-B3062EB677-L000229](../../tests/test_answer_quality_runner.py#L229) | 229 | `"            str(out),"` | — |
| [SRC-B3062EB677-L000230](../../tests/test_answer_quality_runner.py#L230) | 230 | `"        ]"` | — |
| [SRC-B3062EB677-L000231](../../tests/test_answer_quality_runner.py#L231) | 231 | `"    )"` | — |
| [SRC-B3062EB677-L000232](../../tests/test_answer_quality_runner.py#L232) | 232 | `"    assert rc == 0"` | — |
| [SRC-B3062EB677-L000233](../../tests/test_answer_quality_runner.py#L233) | 233 | `"    payload = json.loads(out.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-B3062EB677-L000234](../../tests/test_answer_quality_runner.py#L234) | 234 | `"    assert payload[\"results\"][0][\"status\"] == \"NOT_TESTED\""` | — |
| [SRC-B3062EB677-L000235](../../tests/test_answer_quality_runner.py#L235) | 235 | `"    assert payload[\"results\"][0][\"transport_ok\"] is False"` | — |
| [SRC-B3062EB677-L000236](../../tests/test_answer_quality_runner.py#L236) | 236 | `""` | — |
| [SRC-B3062EB677-L000237](../../tests/test_answer_quality_runner.py#L237) | 237 | `""` | — |
| [SRC-B3062EB677-L000238](../../tests/test_answer_quality_runner.py#L238) | 238 | `""` | — |
| [SRC-B3062EB677-L000239](../../tests/test_answer_quality_runner.py#L239) | 239 | `"def test_response_metrics_separates_tool_status_from_http_success():"` | — |
| [SRC-B3062EB677-L000240](../../tests/test_answer_quality_runner.py#L240) | 240 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000241](../../tests/test_answer_quality_runner.py#L241) | 241 | `"    failed_search = mod._response_metrics("` | — |
| [SRC-B3062EB677-L000242](../../tests/test_answer_quality_runner.py#L242) | 242 | `"        {"` | — |
| [SRC-B3062EB677-L000243](../../tests/test_answer_quality_runner.py#L243) | 243 | `"            \"search_report\": {\"search_outcome\": \"attempted_research_error\"},"` | — |
| [SRC-B3062EB677-L000244](../../tests/test_answer_quality_runner.py#L244) | 244 | `"            \"sources\": [],"` | — |
| [SRC-B3062EB677-L000245](../../tests/test_answer_quality_runner.py#L245) | 245 | `"        },"` | — |
| [SRC-B3062EB677-L000246](../../tests/test_answer_quality_runner.py#L246) | 246 | `"        expected_strategy=\"web_search\","` | — |
| [SRC-B3062EB677-L000247](../../tests/test_answer_quality_runner.py#L247) | 247 | `"        transport_ok=True,"` | — |
| [SRC-B3062EB677-L000248](../../tests/test_answer_quality_runner.py#L248) | 248 | `"    )"` | — |
| [SRC-B3062EB677-L000249](../../tests/test_answer_quality_runner.py#L249) | 249 | `"    assert failed_search[\"tool_status\"] == \"TOOL_FAILED\""` | — |
| [SRC-B3062EB677-L000250](../../tests/test_answer_quality_runner.py#L250) | 250 | `"    assert failed_search[\"request_cost_usd\"] is None"` | — |
| [SRC-B3062EB677-L000251](../../tests/test_answer_quality_runner.py#L251) | 251 | `"    assert failed_search[\"request_cost_status\"] == \"NOT_MEASURED_TOTAL_CONNECTOR_COSTS_NOT_EXPOSED\""` | — |
| [SRC-B3062EB677-L000252](../../tests/test_answer_quality_runner.py#L252) | 252 | `""` | — |
| [SRC-B3062EB677-L000253](../../tests/test_answer_quality_runner.py#L253) | 253 | `"    successful_search = mod._response_metrics("` | — |
| [SRC-B3062EB677-L000254](../../tests/test_answer_quality_runner.py#L254) | 254 | `"        {"` | — |
| [SRC-B3062EB677-L000255](../../tests/test_answer_quality_runner.py#L255) | 255 | `"            \"search_report\": {"` | — |
| [SRC-B3062EB677-L000256](../../tests/test_answer_quality_runner.py#L256) | 256 | `"                \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-B3062EB677-L000257](../../tests/test_answer_quality_runner.py#L257) | 257 | `"                \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-B3062EB677-L000258](../../tests/test_answer_quality_runner.py#L258) | 258 | `"                \"model_calls\": [{"` | — |
| [SRC-B3062EB677-L000259](../../tests/test_answer_quality_runner.py#L259) | 259 | `"                    \"requested_model\": \"test/model\","` | — |
| [SRC-B3062EB677-L000260](../../tests/test_answer_quality_runner.py#L260) | 260 | `"                    \"provider_usage\": {"` | — |
| [SRC-B3062EB677-L000261](../../tests/test_answer_quality_runner.py#L261) | 261 | `"                        \"prompt_tokens\": 10,"` | — |
| [SRC-B3062EB677-L000262](../../tests/test_answer_quality_runner.py#L262) | 262 | `"                        \"completion_tokens\": 20,"` | — |
| [SRC-B3062EB677-L000263](../../tests/test_answer_quality_runner.py#L263) | 263 | `"                        \"total_tokens\": 30,"` | — |
