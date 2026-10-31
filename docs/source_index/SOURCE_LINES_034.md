# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **034**
- سجلات الأسطر: **800**
- النطاق: SRC-63610B9E85-L000019 إلى SRC-D186ED3822-L000088
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-63610B9E85 — [tests/test_agentic_retrieval.py](../../tests/test_agentic_retrieval.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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

### FILE-6A7519AC10 — [tests/test_answer_quality_comparison.py](../../tests/test_answer_quality_comparison.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6A7519AC10-L000001](../../tests/test_answer_quality_comparison.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-6A7519AC10-L000002](../../tests/test_answer_quality_comparison.py#L2) | 2 | `""` | — |
| [SRC-6A7519AC10-L000003](../../tests/test_answer_quality_comparison.py#L3) | 3 | `"import importlib.util"` | — |
| [SRC-6A7519AC10-L000004](../../tests/test_answer_quality_comparison.py#L4) | 4 | `"import json"` | — |
| [SRC-6A7519AC10-L000005](../../tests/test_answer_quality_comparison.py#L5) | 5 | `"from pathlib import Path"` | — |
| [SRC-6A7519AC10-L000006](../../tests/test_answer_quality_comparison.py#L6) | 6 | `""` | — |
| [SRC-6A7519AC10-L000007](../../tests/test_answer_quality_comparison.py#L7) | 7 | `"import pytest"` | — |
| [SRC-6A7519AC10-L000008](../../tests/test_answer_quality_comparison.py#L8) | 8 | `""` | — |
| [SRC-6A7519AC10-L000009](../../tests/test_answer_quality_comparison.py#L9) | 9 | `"ROOT = Path(__file__).resolve().parents[1]"` | — |
| [SRC-6A7519AC10-L000010](../../tests/test_answer_quality_comparison.py#L10) | 10 | `"SCRIPT = ROOT / \"scripts\" / \"compare_answer_quality_runs.py\""` | — |
| [SRC-6A7519AC10-L000011](../../tests/test_answer_quality_comparison.py#L11) | 11 | `"CORPUS_PATH = ROOT / \"tests\" / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-6A7519AC10-L000012](../../tests/test_answer_quality_comparison.py#L12) | 12 | `""` | — |
| [SRC-6A7519AC10-L000013](../../tests/test_answer_quality_comparison.py#L13) | 13 | `""` | — |
| [SRC-6A7519AC10-L000014](../../tests/test_answer_quality_comparison.py#L14) | 14 | `"def load_module():"` | — |
| [SRC-6A7519AC10-L000015](../../tests/test_answer_quality_comparison.py#L15) | 15 | `"    spec = importlib.util.spec_from_file_location(\"answer_quality_run_comparison\", SCRIPT)"` | — |
| [SRC-6A7519AC10-L000016](../../tests/test_answer_quality_comparison.py#L16) | 16 | `"    assert spec and spec.loader"` | — |
| [SRC-6A7519AC10-L000017](../../tests/test_answer_quality_comparison.py#L17) | 17 | `"    module = importlib.util.module_from_spec(spec)"` | — |
| [SRC-6A7519AC10-L000018](../../tests/test_answer_quality_comparison.py#L18) | 18 | `"    spec.loader.exec_module(module)"` | — |
| [SRC-6A7519AC10-L000019](../../tests/test_answer_quality_comparison.py#L19) | 19 | `"    return module"` | — |
| [SRC-6A7519AC10-L000020](../../tests/test_answer_quality_comparison.py#L20) | 20 | `""` | — |
| [SRC-6A7519AC10-L000021](../../tests/test_answer_quality_comparison.py#L21) | 21 | `""` | — |
| [SRC-6A7519AC10-L000022](../../tests/test_answer_quality_comparison.py#L22) | 22 | `"def _run(*, build_sha: str, results: list[dict]) -> dict:"` | — |
| [SRC-6A7519AC10-L000023](../../tests/test_answer_quality_comparison.py#L23) | 23 | `"    corpus = json.loads(CORPUS_PATH.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-6A7519AC10-L000024](../../tests/test_answer_quality_comparison.py#L24) | 24 | `"    return {"` | — |
| [SRC-6A7519AC10-L000025](../../tests/test_answer_quality_comparison.py#L25) | 25 | `"        \"benchmark_id\": corpus[\"benchmark_id\"],"` | — |
| [SRC-6A7519AC10-L000026](../../tests/test_answer_quality_comparison.py#L26) | 26 | `"        \"benchmark_version\": corpus[\"version\"],"` | — |
| [SRC-6A7519AC10-L000027](../../tests/test_answer_quality_comparison.py#L27) | 27 | `"        \"build_sha\": build_sha,"` | — |
| [SRC-6A7519AC10-L000028](../../tests/test_answer_quality_comparison.py#L28) | 28 | `"        \"executed_at_utc\": \"2026-10-29T12:00:00+00:00\","` | — |
| [SRC-6A7519AC10-L000029](../../tests/test_answer_quality_comparison.py#L29) | 29 | `"        \"results\": results,"` | — |
| [SRC-6A7519AC10-L000030](../../tests/test_answer_quality_comparison.py#L30) | 30 | `"    }"` | — |
| [SRC-6A7519AC10-L000031](../../tests/test_answer_quality_comparison.py#L31) | 31 | `""` | — |
| [SRC-6A7519AC10-L000032](../../tests/test_answer_quality_comparison.py#L32) | 32 | `""` | — |
| [SRC-6A7519AC10-L000033](../../tests/test_answer_quality_comparison.py#L33) | 33 | `"def _row(case_id: str, *, latency: float, tool_status: str, cost: float \| None, request_cost: float \| None = None, expected_strategy: str = \"web_search\") -> dict:"` | — |
| [SRC-6A7519AC10-L000034](../../tests/test_answer_quality_comparison.py#L34) | 34 | `"    row = {"` | — |
| [SRC-6A7519AC10-L000035](../../tests/test_answer_quality_comparison.py#L35) | 35 | `"        \"case_id\": case_id,"` | — |
| [SRC-6A7519AC10-L000036](../../tests/test_answer_quality_comparison.py#L36) | 36 | `"        \"prompt\": \"Test question \" + case_id,"` | — |
| [SRC-6A7519AC10-L000037](../../tests/test_answer_quality_comparison.py#L37) | 37 | `"        \"expected_strategy\": expected_strategy,"` | — |
| [SRC-6A7519AC10-L000038](../../tests/test_answer_quality_comparison.py#L38) | 38 | `"        \"transport_ok\": True,"` | — |
| [SRC-6A7519AC10-L000039](../../tests/test_answer_quality_comparison.py#L39) | 39 | `"        \"elapsed_ms\": latency,"` | — |
| [SRC-6A7519AC10-L000040](../../tests/test_answer_quality_comparison.py#L40) | 40 | `"        \"tool_status\": tool_status,"` | — |
| [SRC-6A7519AC10-L000041](../../tests/test_answer_quality_comparison.py#L41) | 41 | `"        \"search_outcome\": \"attempted_with_usable_sources\" if tool_status == \"SUCCESS_WITH_USABLE_RESULTS\" else \"attempted_no_usable_sources\","` | — |
| [SRC-6A7519AC10-L000042](../../tests/test_answer_quality_comparison.py#L42) | 42 | `"        \"provider_reported_model_cost_status\": \"COMPLETE_FOR_RETURNED_MODEL_CALLS\" if cost is not None else \"PROVIDER_COST_NOT_REPORTED\","` | — |
| [SRC-6A7519AC10-L000043](../../tests/test_answer_quality_comparison.py#L43) | 43 | `"        \"request_cost_status\": \"RECONCILED_COMPLETE_REQUEST_COST\" if request_cost is not None else \"NOT_MEASURED_TOTAL_CONNECTOR_COSTS_NOT_EXPOSED\","` | — |
| [SRC-6A7519AC10-L000044](../../tests/test_answer_quality_comparison.py#L44) | 44 | `"        \"required_tool_matrix_complete\": True,"` | — |
| [SRC-6A7519AC10-L000045](../../tests/test_answer_quality_comparison.py#L45) | 45 | `"        \"required_tool_statuses\": ("` | — |
| [SRC-6A7519AC10-L000046](../../tests/test_answer_quality_comparison.py#L46) | 46 | `"            [{"` | — |
| [SRC-6A7519AC10-L000047](../../tests/test_answer_quality_comparison.py#L47) | 47 | `"                \"tool\": \"web_search\","` | — |
| [SRC-6A7519AC10-L000048](../../tests/test_answer_quality_comparison.py#L48) | 48 | `"                \"status\": \"completed_with_results\" if tool_status == \"SUCCESS_WITH_USABLE_RESULTS\" else \"completed_no_usable_results\","` | — |
| [SRC-6A7519AC10-L000049](../../tests/test_answer_quality_comparison.py#L49) | 49 | `"                \"successful_completion\": tool_status == \"SUCCESS_WITH_USABLE_RESULTS\","` | — |
| [SRC-6A7519AC10-L000050](../../tests/test_answer_quality_comparison.py#L50) | 50 | `"            }]"` | — |
| [SRC-6A7519AC10-L000051](../../tests/test_answer_quality_comparison.py#L51) | 51 | `"            if expected_strategy == \"web_search\""` | — |
| [SRC-6A7519AC10-L000052](../../tests/test_answer_quality_comparison.py#L52) | 52 | `"            else []"` | — |
| [SRC-6A7519AC10-L000053](../../tests/test_answer_quality_comparison.py#L53) | 53 | `"        ),"` | — |
| [SRC-6A7519AC10-L000054](../../tests/test_answer_quality_comparison.py#L54) | 54 | `"    }"` | — |
| [SRC-6A7519AC10-L000055](../../tests/test_answer_quality_comparison.py#L55) | 55 | `"    if cost is not None:"` | — |
| [SRC-6A7519AC10-L000056](../../tests/test_answer_quality_comparison.py#L56) | 56 | `"        row[\"provider_reported_model_cost_usd\"] = cost"` | — |
| [SRC-6A7519AC10-L000057](../../tests/test_answer_quality_comparison.py#L57) | 57 | `"    if request_cost is not None:"` | — |
| [SRC-6A7519AC10-L000058](../../tests/test_answer_quality_comparison.py#L58) | 58 | `"        row[\"request_cost_usd\"] = request_cost"` | — |
| [SRC-6A7519AC10-L000059](../../tests/test_answer_quality_comparison.py#L59) | 59 | `"    return row"` | — |
| [SRC-6A7519AC10-L000060](../../tests/test_answer_quality_comparison.py#L60) | 60 | `""` | — |
| [SRC-6A7519AC10-L000061](../../tests/test_answer_quality_comparison.py#L61) | 61 | `""` | — |
| [SRC-6A7519AC10-L000062](../../tests/test_answer_quality_comparison.py#L62) | 62 | `"def _reviews(*, correct: int, supported_citations: int) -> dict:"` | — |
| [SRC-6A7519AC10-L000063](../../tests/test_answer_quality_comparison.py#L63) | 63 | `"    corpus = json.loads(CORPUS_PATH.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-6A7519AC10-L000064](../../tests/test_answer_quality_comparison.py#L64) | 64 | `"    return {"` | — |
| [SRC-6A7519AC10-L000065](../../tests/test_answer_quality_comparison.py#L65) | 65 | `"        \"schema_version\": \"1.0\","` | — |
| [SRC-6A7519AC10-L000066](../../tests/test_answer_quality_comparison.py#L66) | 66 | `"        \"reviews\": ["` | — |
| [SRC-6A7519AC10-L000067](../../tests/test_answer_quality_comparison.py#L67) | 67 | `"            {"` | — |
| [SRC-6A7519AC10-L000068](../../tests/test_answer_quality_comparison.py#L68) | 68 | `"                \"case_id\": case[\"case_id\"],"` | — |
| [SRC-6A7519AC10-L000069](../../tests/test_answer_quality_comparison.py#L69) | 69 | `"                \"status\": \"REVIEWED\","` | — |
| [SRC-6A7519AC10-L000070](../../tests/test_answer_quality_comparison.py#L70) | 70 | `"                \"retrieval\": {"` | — |
| [SRC-6A7519AC10-L000071](../../tests/test_answer_quality_comparison.py#L71) | 71 | `"                    \"relevant_retrieved\": 2 if case[\"case_id\"] == \"AQ-007\" else 1,"` | — |
| [SRC-6A7519AC10-L000072](../../tests/test_answer_quality_comparison.py#L72) | 72 | `"                    \"retrieved_count\": 3,"` | — |
| [SRC-6A7519AC10-L000073](../../tests/test_answer_quality_comparison.py#L73) | 73 | `"                    \"relevant_available\": 3 if case[\"case_id\"] == \"AQ-007\" else 2,"` | — |
| [SRC-6A7519AC10-L000074](../../tests/test_answer_quality_comparison.py#L74) | 74 | `"                },"` | — |
| [SRC-6A7519AC10-L000075](../../tests/test_answer_quality_comparison.py#L75) | 75 | `"                \"faithfulness\": {\"supported_claims\": correct, \"reviewed_claims\": 3},"` | — |
| [SRC-6A7519AC10-L000076](../../tests/test_answer_quality_comparison.py#L76) | 76 | `"                \"correctness\": {\"correct_facts\": correct, \"reviewed_facts\": 3},"` | — |
| [SRC-6A7519AC10-L000077](../../tests/test_answer_quality_comparison.py#L77) | 77 | `"                \"citations\": {"` | — |
| [SRC-6A7519AC10-L000078](../../tests/test_answer_quality_comparison.py#L78) | 78 | `"                    \"supported_citations\": supported_citations,"` | — |
| [SRC-6A7519AC10-L000079](../../tests/test_answer_quality_comparison.py#L79) | 79 | `"                    \"reviewed_citations\": 2,"` | — |
| [SRC-6A7519AC10-L000080](../../tests/test_answer_quality_comparison.py#L80) | 80 | `"                },"` | — |
| [SRC-6A7519AC10-L000081](../../tests/test_answer_quality_comparison.py#L81) | 81 | `"                \"writing_quality\": 4,"` | — |
| [SRC-6A7519AC10-L000082](../../tests/test_answer_quality_comparison.py#L82) | 82 | `"            }"` | — |
| [SRC-6A7519AC10-L000083](../../tests/test_answer_quality_comparison.py#L83) | 83 | `"            for case in corpus[\"cases\"]"` | — |
| [SRC-6A7519AC10-L000084](../../tests/test_answer_quality_comparison.py#L84) | 84 | `"        ],"` | — |
| [SRC-6A7519AC10-L000085](../../tests/test_answer_quality_comparison.py#L85) | 85 | `"    }"` | — |
| [SRC-6A7519AC10-L000086](../../tests/test_answer_quality_comparison.py#L86) | 86 | `""` | — |
| [SRC-6A7519AC10-L000087](../../tests/test_answer_quality_comparison.py#L87) | 87 | `""` | — |
| [SRC-6A7519AC10-L000088](../../tests/test_answer_quality_comparison.py#L88) | 88 | `"def _full_run(*, build_sha: str, candidate: bool) -> dict:"` | — |
| [SRC-6A7519AC10-L000089](../../tests/test_answer_quality_comparison.py#L89) | 89 | `"    corpus = json.loads(CORPUS_PATH.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-6A7519AC10-L000090](../../tests/test_answer_quality_comparison.py#L90) | 90 | `"    rows = []"` | — |
| [SRC-6A7519AC10-L000091](../../tests/test_answer_quality_comparison.py#L91) | 91 | `"    for case in corpus[\"cases\"]:"` | — |
| [SRC-6A7519AC10-L000092](../../tests/test_answer_quality_comparison.py#L92) | 92 | `"        case_id = case[\"case_id\"]"` | — |
| [SRC-6A7519AC10-L000093](../../tests/test_answer_quality_comparison.py#L93) | 93 | `"        is_aq007 = case_id == \"AQ-007\""` | — |
| [SRC-6A7519AC10-L000094](../../tests/test_answer_quality_comparison.py#L94) | 94 | `"        is_aq008 = case_id == \"AQ-008\""` | — |
| [SRC-6A7519AC10-L000095](../../tests/test_answer_quality_comparison.py#L95) | 95 | `"        if candidate:"` | — |
| [SRC-6A7519AC10-L000096](../../tests/test_answer_quality_comparison.py#L96) | 96 | `"            latency = 80 if is_aq007 else 120 if is_aq008 else 100"` | — |
| [SRC-6A7519AC10-L000097](../../tests/test_answer_quality_comparison.py#L97) | 97 | `"            status = \"SUCCESS_WITH_USABLE_RESULTS\""` | — |
| [SRC-6A7519AC10-L000098](../../tests/test_answer_quality_comparison.py#L98) | 98 | `"            model_cost = 0.005 if is_aq007 else 0.002 if is_aq008 else None"` | — |
| [SRC-6A7519AC10-L000099](../../tests/test_answer_quality_comparison.py#L99) | 99 | `"            request_cost = 0.007 if is_aq007 else 0.009 if is_aq008 else 0.001"` | — |
| [SRC-6A7519AC10-L000100](../../tests/test_answer_quality_comparison.py#L100) | 100 | `"        else:"` | — |
| [SRC-6A7519AC10-L000101](../../tests/test_answer_quality_comparison.py#L101) | 101 | `"            latency = 100 if is_aq007 else 200 if is_aq008 else 150"` | — |
| [SRC-6A7519AC10-L000102](../../tests/test_answer_quality_comparison.py#L102) | 102 | `"            status = \"SUCCESS_WITH_USABLE_RESULTS\" if is_aq007 else \"ATTEMPTED_NO_USABLE_RESULTS\""` | — |
| [SRC-6A7519AC10-L000103](../../tests/test_answer_quality_comparison.py#L103) | 103 | `"            model_cost = 0.01 if is_aq007 else None"` | — |
| [SRC-6A7519AC10-L000104](../../tests/test_answer_quality_comparison.py#L104) | 104 | `"            request_cost = 0.012 if is_aq007 else 0.015 if is_aq008 else 0.001"` | — |
| [SRC-6A7519AC10-L000105](../../tests/test_answer_quality_comparison.py#L105) | 105 | `"        rows.append({"` | — |
| [SRC-6A7519AC10-L000106](../../tests/test_answer_quality_comparison.py#L106) | 106 | `"            **_row("` | — |
| [SRC-6A7519AC10-L000107](../../tests/test_answer_quality_comparison.py#L107) | 107 | `"                case_id, latency=latency, tool_status=status,"` | — |
| [SRC-6A7519AC10-L000108](../../tests/test_answer_quality_comparison.py#L108) | 108 | `"                cost=model_cost, request_cost=request_cost,"` | — |
| [SRC-6A7519AC10-L000109](../../tests/test_answer_quality_comparison.py#L109) | 109 | `"                expected_strategy=case[\"expected_strategy\"],"` | — |
| [SRC-6A7519AC10-L000110](../../tests/test_answer_quality_comparison.py#L110) | 110 | `"            ),"` | — |
| [SRC-6A7519AC10-L000111](../../tests/test_answer_quality_comparison.py#L111) | 111 | `"            \"prompt\": case[\"question\"],"` | — |
| [SRC-6A7519AC10-L000112](../../tests/test_answer_quality_comparison.py#L112) | 112 | `"        })"` | — |
| [SRC-6A7519AC10-L000113](../../tests/test_answer_quality_comparison.py#L113) | 113 | `"    return _run(build_sha=build_sha, results=rows)"` | — |
| [SRC-6A7519AC10-L000114](../../tests/test_answer_quality_comparison.py#L114) | 114 | `""` | — |
| [SRC-6A7519AC10-L000115](../../tests/test_answer_quality_comparison.py#L115) | 115 | `""` | — |
| [SRC-6A7519AC10-L000116](../../tests/test_answer_quality_comparison.py#L116) | 116 | `"def test_comparison_measures_latency_tools_cost_and_human_reviewed_quality():"` | — |
| [SRC-6A7519AC10-L000117](../../tests/test_answer_quality_comparison.py#L117) | 117 | `"    mod = load_module()"` | — |
| [SRC-6A7519AC10-L000118](../../tests/test_answer_quality_comparison.py#L118) | 118 | `"    baseline = _full_run(build_sha=\"a\" * 40, candidate=False)"` | — |
| [SRC-6A7519AC10-L000119](../../tests/test_answer_quality_comparison.py#L119) | 119 | `"    candidate = _full_run(build_sha=\"b\" * 40, candidate=True)"` | — |
| [SRC-6A7519AC10-L000120](../../tests/test_answer_quality_comparison.py#L120) | 120 | `"    corpus = mod.load_json_object(CORPUS_PATH)"` | — |
| [SRC-6A7519AC10-L000121](../../tests/test_answer_quality_comparison.py#L121) | 121 | `"    result = mod.compare_runs("` | — |
| [SRC-6A7519AC10-L000122](../../tests/test_answer_quality_comparison.py#L122) | 122 | `"        baseline,"` | — |
| [SRC-6A7519AC10-L000123](../../tests/test_answer_quality_comparison.py#L123) | 123 | `"        candidate,"` | — |
| [SRC-6A7519AC10-L000124](../../tests/test_answer_quality_comparison.py#L124) | 124 | `"        corpus=corpus,"` | — |
| [SRC-6A7519AC10-L000125](../../tests/test_answer_quality_comparison.py#L125) | 125 | `"        baseline_reviews=_reviews(correct=2, supported_citations=1),"` | — |
| [SRC-6A7519AC10-L000126](../../tests/test_answer_quality_comparison.py#L126) | 126 | `"        candidate_reviews=_reviews(correct=3, supported_citations=2),"` | — |
| [SRC-6A7519AC10-L000127](../../tests/test_answer_quality_comparison.py#L127) | 127 | `"    )"` | — |
| [SRC-6A7519AC10-L000128](../../tests/test_answer_quality_comparison.py#L128) | 128 | `"    assert result[\"acceptance_status\"] == \"COMPARABLE_WITH_REVIEWED_QUALITY_AND_BUILD_IDENTITIES\""` | — |
| [SRC-6A7519AC10-L000129](../../tests/test_answer_quality_comparison.py#L129) | 129 | `"    assert result[\"case_count\"] == 45"` | — |
| [SRC-6A7519AC10-L000130](../../tests/test_answer_quality_comparison.py#L130) | 130 | `"    assert result[\"baseline\"][\"metrics\"][\"latency_ms\"][\"p50\"] == 150"` | — |
| [SRC-6A7519AC10-L000131](../../tests/test_answer_quality_comparison.py#L131) | 131 | `"    assert result[\"candidate\"][\"metrics\"][\"latency_ms\"][\"p95\"] == 100"` | — |
| [SRC-6A7519AC10-L000132](../../tests/test_answer_quality_comparison.py#L132) | 132 | `"    assert result[\"candidate\"][\"metrics\"][\"latency_ms\"][\"max\"] == 120"` | — |
| [SRC-6A7519AC10-L000133](../../tests/test_answer_quality_comparison.py#L133) | 133 | `"    assert result[\"baseline\"][\"metrics\"][\"tool_usage\"][\"required_tool_matrix_coverage\"][\"score\"] == 1.0"` | — |
| [SRC-6A7519AC10-L000134](../../tests/test_answer_quality_comparison.py#L134) | 134 | `"    assert result[\"candidate\"][\"metrics\"][\"tool_usage\"][\"required_tool_matrix_coverage\"][\"score\"] == 1.0"` | — |
| [SRC-6A7519AC10-L000135](../../tests/test_answer_quality_comparison.py#L135) | 135 | `"    assert result[\"baseline\"][\"metrics\"][\"tool_usage\"][\"required_tool_observation_count\"] == 30"` | — |
| [SRC-6A7519AC10-L000136](../../tests/test_answer_quality_comparison.py#L136) | 136 | `"    assert result[\"runtime_deltas\"][\"usable_result_rate\"][\"baseline\"] == pytest.approx(0.0333)"` | — |
| [SRC-6A7519AC10-L000137](../../tests/test_answer_quality_comparison.py#L137) | 137 | `"    assert result[\"runtime_deltas\"][\"usable_result_rate\"][\"candidate\"] == 1.0"` | — |
| [SRC-6A7519AC10-L000138](../../tests/test_answer_quality_comparison.py#L138) | 138 | `"    assert result[\"runtime_deltas\"][\"required_tool_success_rate\"][\"baseline\"] == pytest.approx(0.0333)"` | — |
| [SRC-6A7519AC10-L000139](../../tests/test_answer_quality_comparison.py#L139) | 139 | `"    assert result[\"runtime_deltas\"][\"required_tool_success_rate\"][\"candidate\"] == 1.0"` | — |
| [SRC-6A7519AC10-L000140](../../tests/test_answer_quality_comparison.py#L140) | 140 | `"    assert result[\"runtime_deltas\"][\"required_tool_success_rate\"][\"delta\"] == pytest.approx(0.9667)"` | — |
| [SRC-6A7519AC10-L000141](../../tests/test_answer_quality_comparison.py#L141) | 141 | `"    assert result[\"runtime_deltas\"][\"provider_reported_model_cost_usd\"][\"delta\"] == -0.003"` | — |
| [SRC-6A7519AC10-L000142](../../tests/test_answer_quality_comparison.py#L142) | 142 | `"    assert result[\"baseline\"][\"metrics\"][\"provider_reported_model_cost\"][\"complete_request_cost_usd\"] == pytest.approx(0.070)"` | — |
| [SRC-6A7519AC10-L000143](../../tests/test_answer_quality_comparison.py#L143) | 143 | `"    assert result[\"runtime_deltas\"][\"complete_request_cost_usd\"][\"delta\"] == pytest.approx(-0.011)"` | — |
| [SRC-6A7519AC10-L000144](../../tests/test_answer_quality_comparison.py#L144) | 144 | `"    assert result[\"runtime_deltas\"][\"complete_request_cost_usd\"][\"status\"] == \"COMPARED\""` | — |
| [SRC-6A7519AC10-L000145](../../tests/test_answer_quality_comparison.py#L145) | 145 | `"    assert result[\"quality_comparison\"][\"metrics\"][\"factual_accuracy\"][\"baseline\"] == pytest.approx(2 / 3, abs=0.0001)"` | — |
| [SRC-6A7519AC10-L000146](../../tests/test_answer_quality_comparison.py#L146) | 146 | `"    assert result[\"quality_comparison\"][\"metrics\"][\"factual_accuracy\"][\"candidate\"] == 1.0"` | — |
| [SRC-6A7519AC10-L000147](../../tests/test_answer_quality_comparison.py#L147) | 147 | `"    assert result[\"quality_comparison\"][\"metrics\"][\"citation_support\"][\"delta\"] == 0.5"` | — |
| [SRC-6A7519AC10-L000148](../../tests/test_answer_quality_comparison.py#L148) | 148 | `""` | — |
| [SRC-6A7519AC10-L000149](../../tests/test_answer_quality_comparison.py#L149) | 149 | `""` | — |
| [SRC-6A7519AC10-L000150](../../tests/test_answer_quality_comparison.py#L150) | 150 | `"def test_missing_build_sha_and_review_data_cannot_claim_complete_acceptance():"` | — |
| [SRC-6A7519AC10-L000151](../../tests/test_answer_quality_comparison.py#L151) | 151 | `"    mod = load_module()"` | — |
| [SRC-6A7519AC10-L000152](../../tests/test_answer_quality_comparison.py#L152) | 152 | `"    baseline = _run(build_sha=\"unknown\", results=[_row(\"AQ-001\", latency=100, tool_status=\"SUCCESS_WITH_USABLE_RESULTS\", cost=None)])"` | — |
| [SRC-6A7519AC10-L000153](../../tests/test_answer_quality_comparison.py#L153) | 153 | `"    candidate = _run(build_sha=\"\", results=[_row(\"AQ-001\", latency=90, tool_status=\"SUCCESS_WITH_USABLE_RESULTS\", cost=None)])"` | — |
| [SRC-6A7519AC10-L000154](../../tests/test_answer_quality_comparison.py#L154) | 154 | `"    result = mod.compare_runs(baseline, candidate)"` | — |
| [SRC-6A7519AC10-L000155](../../tests/test_answer_quality_comparison.py#L155) | 155 | `"    assert result[\"acceptance_status\"] == \"INCOMPLETE\""` | — |
| [SRC-6A7519AC10-L000156](../../tests/test_answer_quality_comparison.py#L156) | 156 | `"    assert \"baseline_build_sha_missing_or_invalid\" in result[\"acceptance_blockers\"]"` | — |
| [SRC-6A7519AC10-L000157](../../tests/test_answer_quality_comparison.py#L157) | 157 | `"    assert \"candidate_build_sha_missing_or_invalid\" in result[\"acceptance_blockers\"]"` | — |
| [SRC-6A7519AC10-L000158](../../tests/test_answer_quality_comparison.py#L158) | 158 | `"    assert \"human_review_files_missing\" in result[\"acceptance_blockers\"]"` | — |
| [SRC-6A7519AC10-L000159](../../tests/test_answer_quality_comparison.py#L159) | 159 | `"    assert result[\"quality_comparison\"] is None"` | — |
| [SRC-6A7519AC10-L000160](../../tests/test_answer_quality_comparison.py#L160) | 160 | `"    assert result[\"baseline\"][\"metrics\"][\"provider_reported_model_cost\"][\"reported_sum_usd\"] is None"` | — |
| [SRC-6A7519AC10-L000161](../../tests/test_answer_quality_comparison.py#L161) | 161 | `"    assert result[\"runtime_deltas\"][\"provider_reported_model_cost_usd\"][\"status\"] == \"NOT_MEASURED\""` | — |
| [SRC-6A7519AC10-L000162](../../tests/test_answer_quality_comparison.py#L162) | 162 | `""` | — |
| [SRC-6A7519AC10-L000163](../../tests/test_answer_quality_comparison.py#L163) | 163 | `""` | — |
| [SRC-6A7519AC10-L000164](../../tests/test_answer_quality_comparison.py#L164) | 164 | `"def test_comparison_rejects_different_case_sets_and_questions():"` | — |
| [SRC-6A7519AC10-L000165](../../tests/test_answer_quality_comparison.py#L165) | 165 | `"    mod = load_module()"` | — |
| [SRC-6A7519AC10-L000166](../../tests/test_answer_quality_comparison.py#L166) | 166 | `"    baseline = _run(build_sha=\"a\" * 40, results=[_row(\"AQ-007\", latency=100, tool_status=\"SUCCESS_WITH_USABLE_RESULTS\", cost=None)])"` | — |
| [SRC-6A7519AC10-L000167](../../tests/test_answer_quality_comparison.py#L167) | 167 | `"    missing = _run(build_sha=\"b\" * 40, results=[_row(\"AQ-008\", latency=90, tool_status=\"SUCCESS_WITH_USABLE_RESULTS\", cost=None)])"` | — |
| [SRC-6A7519AC10-L000168](../../tests/test_answer_quality_comparison.py#L168) | 168 | `"    with pytest.raises(ValueError, match=\"incomparable case sets\"):"` | — |
| [SRC-6A7519AC10-L000169](../../tests/test_answer_quality_comparison.py#L169) | 169 | `"        mod.compare_runs(baseline, missing)"` | — |
| [SRC-6A7519AC10-L000170](../../tests/test_answer_quality_comparison.py#L170) | 170 | `"    changed_question = _run("` | — |
| [SRC-6A7519AC10-L000171](../../tests/test_answer_quality_comparison.py#L171) | 171 | `"        build_sha=\"b\" * 40,"` | — |
| [SRC-6A7519AC10-L000172](../../tests/test_answer_quality_comparison.py#L172) | 172 | `"        results=[{**_row(\"AQ-007\", latency=90, tool_status=\"SUCCESS_WITH_USABLE_RESULTS\", cost=None), \"prompt\": \"A different prompt\"}],"` | — |
| [SRC-6A7519AC10-L000173](../../tests/test_answer_quality_comparison.py#L173) | 173 | `"    )"` | — |
| [SRC-6A7519AC10-L000174](../../tests/test_answer_quality_comparison.py#L174) | 174 | `"    with pytest.raises(ValueError, match=\"incomparable question text\"):"` | — |
| [SRC-6A7519AC10-L000175](../../tests/test_answer_quality_comparison.py#L175) | 175 | `"        mod.compare_runs(baseline, changed_question)"` | — |
| [SRC-6A7519AC10-L000176](../../tests/test_answer_quality_comparison.py#L176) | 176 | `""` | — |
| [SRC-6A7519AC10-L000177](../../tests/test_answer_quality_comparison.py#L177) | 177 | `""` | — |
| [SRC-6A7519AC10-L000178](../../tests/test_answer_quality_comparison.py#L178) | 178 | `"def test_run_validation_rejects_duplicate_ids_and_invalid_latency():"` | — |
| [SRC-6A7519AC10-L000179](../../tests/test_answer_quality_comparison.py#L179) | 179 | `"    mod = load_module()"` | — |
| [SRC-6A7519AC10-L000180](../../tests/test_answer_quality_comparison.py#L180) | 180 | `"    run = _run("` | — |
| [SRC-6A7519AC10-L000181](../../tests/test_answer_quality_comparison.py#L181) | 181 | `"        build_sha=\"a\" * 40,"` | — |
| [SRC-6A7519AC10-L000182](../../tests/test_answer_quality_comparison.py#L182) | 182 | `"        results=["` | — |
| [SRC-6A7519AC10-L000183](../../tests/test_answer_quality_comparison.py#L183) | 183 | `"            _row(\"AQ-007\", latency=-1, tool_status=\"UNKNOWN\", cost=None),"` | — |
| [SRC-6A7519AC10-L000184](../../tests/test_answer_quality_comparison.py#L184) | 184 | `"            _row(\"AQ-007\", latency=10, tool_status=\"UNKNOWN\", cost=None),"` | — |
| [SRC-6A7519AC10-L000185](../../tests/test_answer_quality_comparison.py#L185) | 185 | `"        ],"` | — |
| [SRC-6A7519AC10-L000186](../../tests/test_answer_quality_comparison.py#L186) | 186 | `"    )"` | — |
| [SRC-6A7519AC10-L000187](../../tests/test_answer_quality_comparison.py#L187) | 187 | `"    errors = mod.validate_run(run, \"run\")"` | — |
| [SRC-6A7519AC10-L000188](../../tests/test_answer_quality_comparison.py#L188) | 188 | `"    assert any(\"duplicate case_id\" in error for error in errors)"` | — |
| [SRC-6A7519AC10-L000189](../../tests/test_answer_quality_comparison.py#L189) | 189 | `"    assert any(\"elapsed_ms must be finite and non-negative\" in error for error in errors)"` | — |
| [SRC-6A7519AC10-L000190](../../tests/test_answer_quality_comparison.py#L190) | 190 | `""` | — |
| [SRC-6A7519AC10-L000191](../../tests/test_answer_quality_comparison.py#L191) | 191 | `""` | — |
| [SRC-6A7519AC10-L000192](../../tests/test_answer_quality_comparison.py#L192) | 192 | `"def test_comparison_blocks_incomplete_required_tool_matrix_coverage():"` | — |
| [SRC-6A7519AC10-L000193](../../tests/test_answer_quality_comparison.py#L193) | 193 | `"    mod = load_module()"` | — |
| [SRC-6A7519AC10-L000194](../../tests/test_answer_quality_comparison.py#L194) | 194 | `"    baseline = _full_run(build_sha=\"a\" * 40, candidate=False)"` | — |
| [SRC-6A7519AC10-L000195](../../tests/test_answer_quality_comparison.py#L195) | 195 | `"    candidate = _full_run(build_sha=\"b\" * 40, candidate=True)"` | — |
| [SRC-6A7519AC10-L000196](../../tests/test_answer_quality_comparison.py#L196) | 196 | `"    baseline[\"results\"][0][\"required_tool_matrix_complete\"] = False"` | — |
| [SRC-6A7519AC10-L000197](../../tests/test_answer_quality_comparison.py#L197) | 197 | `"    result = mod.compare_runs("` | — |
| [SRC-6A7519AC10-L000198](../../tests/test_answer_quality_comparison.py#L198) | 198 | `"        baseline,"` | — |
| [SRC-6A7519AC10-L000199](../../tests/test_answer_quality_comparison.py#L199) | 199 | `"        candidate,"` | — |
| [SRC-6A7519AC10-L000200](../../tests/test_answer_quality_comparison.py#L200) | 200 | `"        corpus=mod.load_json_object(CORPUS_PATH),"` | — |
| [SRC-6A7519AC10-L000201](../../tests/test_answer_quality_comparison.py#L201) | 201 | `"        baseline_reviews=_reviews(correct=2, supported_citations=1),"` | — |
| [SRC-6A7519AC10-L000202](../../tests/test_answer_quality_comparison.py#L202) | 202 | `"        candidate_reviews=_reviews(correct=3, supported_citations=2),"` | — |
| [SRC-6A7519AC10-L000203](../../tests/test_answer_quality_comparison.py#L203) | 203 | `"    )"` | — |
| [SRC-6A7519AC10-L000204](../../tests/test_answer_quality_comparison.py#L204) | 204 | `"    assert result[\"acceptance_status\"] == \"INCOMPLETE\""` | — |
| [SRC-6A7519AC10-L000205](../../tests/test_answer_quality_comparison.py#L205) | 205 | `"    assert \"baseline_required_tool_matrix_incomplete\" in result[\"acceptance_blockers\"]"` | — |
| [SRC-6A7519AC10-L000206](../../tests/test_answer_quality_comparison.py#L206) | 206 | `"    assert result[\"baseline\"][\"metrics\"][\"tool_usage\"][\"required_tool_matrix_coverage\"][\"score\"] < 1.0"` | — |
| [SRC-6A7519AC10-L000207](../../tests/test_answer_quality_comparison.py#L207) | 207 | `""` | — |
| [SRC-6A7519AC10-L000208](../../tests/test_answer_quality_comparison.py#L208) | 208 | `""` | — |
| [SRC-6A7519AC10-L000209](../../tests/test_answer_quality_comparison.py#L209) | 209 | `"def test_comparison_blocks_partially_reconciled_request_costs():"` | — |
| [SRC-6A7519AC10-L000210](../../tests/test_answer_quality_comparison.py#L210) | 210 | `"    mod = load_module()"` | — |
| [SRC-6A7519AC10-L000211](../../tests/test_answer_quality_comparison.py#L211) | 211 | `"    baseline = _full_run(build_sha=\"a\" * 40, candidate=False)"` | — |
| [SRC-6A7519AC10-L000212](../../tests/test_answer_quality_comparison.py#L212) | 212 | `"    candidate = _full_run(build_sha=\"b\" * 40, candidate=True)"` | — |
| [SRC-6A7519AC10-L000213](../../tests/test_answer_quality_comparison.py#L213) | 213 | `"    baseline[\"results\"][0][\"request_cost_usd\"] = None"` | — |
| [SRC-6A7519AC10-L000214](../../tests/test_answer_quality_comparison.py#L214) | 214 | `"    baseline[\"results\"][0][\"request_cost_status\"] = \"PARTIAL_EXTERNAL_COST_RECONCILIATION\""` | — |
| [SRC-6A7519AC10-L000215](../../tests/test_answer_quality_comparison.py#L215) | 215 | `"    result = mod.compare_runs("` | — |
| [SRC-6A7519AC10-L000216](../../tests/test_answer_quality_comparison.py#L216) | 216 | `"        baseline,"` | — |
| [SRC-6A7519AC10-L000217](../../tests/test_answer_quality_comparison.py#L217) | 217 | `"        candidate,"` | — |
| [SRC-6A7519AC10-L000218](../../tests/test_answer_quality_comparison.py#L218) | 218 | `"        corpus=mod.load_json_object(CORPUS_PATH),"` | — |
| [SRC-6A7519AC10-L000219](../../tests/test_answer_quality_comparison.py#L219) | 219 | `"        baseline_reviews=_reviews(correct=2, supported_citations=1),"` | — |
| [SRC-6A7519AC10-L000220](../../tests/test_answer_quality_comparison.py#L220) | 220 | `"        candidate_reviews=_reviews(correct=3, supported_citations=2),"` | — |
| [SRC-6A7519AC10-L000221](../../tests/test_answer_quality_comparison.py#L221) | 221 | `"    )"` | — |
| [SRC-6A7519AC10-L000222](../../tests/test_answer_quality_comparison.py#L222) | 222 | `"    assert result[\"acceptance_status\"] == \"INCOMPLETE\""` | — |
| [SRC-6A7519AC10-L000223](../../tests/test_answer_quality_comparison.py#L223) | 223 | `"    assert \"baseline_complete_request_cost_missing_or_partial\" in result[\"acceptance_blockers\"]"` | — |
| [SRC-6A7519AC10-L000224](../../tests/test_answer_quality_comparison.py#L224) | 224 | `"    assert result[\"baseline\"][\"metrics\"][\"provider_reported_model_cost\"][\"complete_request_cost_usd\"] is None"` | — |
| [SRC-6A7519AC10-L000225](../../tests/test_answer_quality_comparison.py#L225) | 225 | `""` | — |
| [SRC-6A7519AC10-L000226](../../tests/test_answer_quality_comparison.py#L226) | 226 | `""` | — |
| [SRC-6A7519AC10-L000227](../../tests/test_answer_quality_comparison.py#L227) | 227 | `"def test_quality_comparison_rejects_incomplete_human_review_coverage():"` | — |
| [SRC-6A7519AC10-L000228](../../tests/test_answer_quality_comparison.py#L228) | 228 | `"    mod = load_module()"` | — |
| [SRC-6A7519AC10-L000229](../../tests/test_answer_quality_comparison.py#L229) | 229 | `"    corpus = mod.load_json_object(CORPUS_PATH)"` | — |
| [SRC-6A7519AC10-L000230](../../tests/test_answer_quality_comparison.py#L230) | 230 | `"    partial = {"` | — |
| [SRC-6A7519AC10-L000231](../../tests/test_answer_quality_comparison.py#L231) | 231 | `"        \"schema_version\": \"1.0\","` | — |
| [SRC-6A7519AC10-L000232](../../tests/test_answer_quality_comparison.py#L232) | 232 | `"        \"reviews\": [{"` | — |
| [SRC-6A7519AC10-L000233](../../tests/test_answer_quality_comparison.py#L233) | 233 | `"            \"case_id\": \"AQ-001\","` | — |
| [SRC-6A7519AC10-L000234](../../tests/test_answer_quality_comparison.py#L234) | 234 | `"            \"status\": \"REVIEWED\","` | — |
| [SRC-6A7519AC10-L000235](../../tests/test_answer_quality_comparison.py#L235) | 235 | `"            \"correctness\": {\"correct_facts\": 1, \"reviewed_facts\": 1},"` | — |
| [SRC-6A7519AC10-L000236](../../tests/test_answer_quality_comparison.py#L236) | 236 | `"        }],"` | — |
| [SRC-6A7519AC10-L000237](../../tests/test_answer_quality_comparison.py#L237) | 237 | `"    }"` | — |
| [SRC-6A7519AC10-L000238](../../tests/test_answer_quality_comparison.py#L238) | 238 | `"    full = _reviews(correct=1, supported_citations=1)"` | — |
| [SRC-6A7519AC10-L000239](../../tests/test_answer_quality_comparison.py#L239) | 239 | `"    with pytest.raises(ValueError, match=\"incomplete human review coverage\"):"` | — |
| [SRC-6A7519AC10-L000240](../../tests/test_answer_quality_comparison.py#L240) | 240 | `"        mod.review_comparison(partial, full, corpus)"` | — |
| [SRC-6A7519AC10-L000241](../../tests/test_answer_quality_comparison.py#L241) | 241 | `""` | — |
| [SRC-6A7519AC10-L000242](../../tests/test_answer_quality_comparison.py#L242) | 242 | `""` | — |
| [SRC-6A7519AC10-L000243](../../tests/test_answer_quality_comparison.py#L243) | 243 | `"def test_comparison_requires_nonempty_recorded_question_text():"` | — |
| [SRC-6A7519AC10-L000244](../../tests/test_answer_quality_comparison.py#L244) | 244 | `"    mod = load_module()"` | — |
| [SRC-6A7519AC10-L000245](../../tests/test_answer_quality_comparison.py#L245) | 245 | `"    baseline = _run(build_sha=\"a\" * 40, results=[{\"case_id\": \"AQ-001\", \"elapsed_ms\": 20}])"` | — |
| [SRC-6A7519AC10-L000246](../../tests/test_answer_quality_comparison.py#L246) | 246 | `"    candidate = _run(build_sha=\"b\" * 40, results=[{\"case_id\": \"AQ-001\", \"elapsed_ms\": 10}])"` | — |
| [SRC-6A7519AC10-L000247](../../tests/test_answer_quality_comparison.py#L247) | 247 | `"    errors = mod.validate_run(baseline, \"baseline\")"` | — |
| [SRC-6A7519AC10-L000248](../../tests/test_answer_quality_comparison.py#L248) | 248 | `"    assert any(\"prompt must be a non-empty string\" in error for error in errors)"` | — |
| [SRC-6A7519AC10-L000249](../../tests/test_answer_quality_comparison.py#L249) | 249 | `"    with pytest.raises(ValueError, match=\"prompt must be a non-empty string\"):"` | — |
| [SRC-6A7519AC10-L000250](../../tests/test_answer_quality_comparison.py#L250) | 250 | `"        mod.compare_runs(baseline, candidate)"` | — |
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

### FILE-2477C41448 — [tests/test_answer_quality_provider_usage.py](../../tests/test_answer_quality_provider_usage.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2477C41448-L000001](../../tests/test_answer_quality_provider_usage.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-2477C41448-L000002](../../tests/test_answer_quality_provider_usage.py#L2) | 2 | `""` | — |
| [SRC-2477C41448-L000003](../../tests/test_answer_quality_provider_usage.py#L3) | 3 | `"import json"` | — |
| [SRC-2477C41448-L000004](../../tests/test_answer_quality_provider_usage.py#L4) | 4 | `""` | — |
| [SRC-2477C41448-L000005](../../tests/test_answer_quality_provider_usage.py#L5) | 5 | `"from agents.web_agent import WebAgent, _normalized_provider_usage"` | — |
| [SRC-2477C41448-L000006](../../tests/test_answer_quality_provider_usage.py#L6) | 6 | `""` | — |
| [SRC-2477C41448-L000007](../../tests/test_answer_quality_provider_usage.py#L7) | 7 | `""` | — |
| [SRC-2477C41448-L000008](../../tests/test_answer_quality_provider_usage.py#L8) | 8 | `"def test_provider_usage_keeps_only_valid_numeric_fields_and_openrouter_usd_cost():"` | — |
| [SRC-2477C41448-L000009](../../tests/test_answer_quality_provider_usage.py#L9) | 9 | `"    usage = {"` | — |
| [SRC-2477C41448-L000010](../../tests/test_answer_quality_provider_usage.py#L10) | 10 | `"        \"prompt_tokens\": 18,"` | — |
| [SRC-2477C41448-L000011](../../tests/test_answer_quality_provider_usage.py#L11) | 11 | `"        \"completion_tokens\": 24,"` | — |
| [SRC-2477C41448-L000012](../../tests/test_answer_quality_provider_usage.py#L12) | 12 | `"        \"total_tokens\": 42,"` | — |
| [SRC-2477C41448-L000013](../../tests/test_answer_quality_provider_usage.py#L13) | 13 | `"        \"cost\": 0.00125,"` | — |
| [SRC-2477C41448-L000014](../../tests/test_answer_quality_provider_usage.py#L14) | 14 | `"        \"provider_private_payload\": \"must not be retained\","` | — |
| [SRC-2477C41448-L000015](../../tests/test_answer_quality_provider_usage.py#L15) | 15 | `"        \"prompt_tokens_text\": \"18\","` | — |
| [SRC-2477C41448-L000016](../../tests/test_answer_quality_provider_usage.py#L16) | 16 | `"    }"` | — |
| [SRC-2477C41448-L000017](../../tests/test_answer_quality_provider_usage.py#L17) | 17 | `"    normalized = _normalized_provider_usage("` | — |
| [SRC-2477C41448-L000018](../../tests/test_answer_quality_provider_usage.py#L18) | 18 | `"        usage, provider_base_url=\"https://openrouter.ai/api/v1\""` | — |
| [SRC-2477C41448-L000019](../../tests/test_answer_quality_provider_usage.py#L19) | 19 | `"    )"` | — |
| [SRC-2477C41448-L000020](../../tests/test_answer_quality_provider_usage.py#L20) | 20 | `"    assert normalized == {"` | — |
| [SRC-2477C41448-L000021](../../tests/test_answer_quality_provider_usage.py#L21) | 21 | `"        \"prompt_tokens\": 18,"` | — |
| [SRC-2477C41448-L000022](../../tests/test_answer_quality_provider_usage.py#L22) | 22 | `"        \"completion_tokens\": 24,"` | — |
| [SRC-2477C41448-L000023](../../tests/test_answer_quality_provider_usage.py#L23) | 23 | `"        \"total_tokens\": 42,"` | — |
| [SRC-2477C41448-L000024](../../tests/test_answer_quality_provider_usage.py#L24) | 24 | `"        \"cost_usd\": 0.00125,"` | — |
| [SRC-2477C41448-L000025](../../tests/test_answer_quality_provider_usage.py#L25) | 25 | `"    }"` | — |
| [SRC-2477C41448-L000026](../../tests/test_answer_quality_provider_usage.py#L26) | 26 | `""` | — |
| [SRC-2477C41448-L000027](../../tests/test_answer_quality_provider_usage.py#L27) | 27 | `""` | — |
| [SRC-2477C41448-L000028](../../tests/test_answer_quality_provider_usage.py#L28) | 28 | `"def test_generic_provider_cost_is_not_assumed_to_be_usd():"` | — |
| [SRC-2477C41448-L000029](../../tests/test_answer_quality_provider_usage.py#L29) | 29 | `"    normalized = _normalized_provider_usage("` | — |
| [SRC-2477C41448-L000030](../../tests/test_answer_quality_provider_usage.py#L30) | 30 | `"        {\"prompt_tokens\": 5, \"cost\": 0.05},"` | — |
| [SRC-2477C41448-L000031](../../tests/test_answer_quality_provider_usage.py#L31) | 31 | `"        provider_base_url=\"https://custom-provider.example/v1\","` | — |
| [SRC-2477C41448-L000032](../../tests/test_answer_quality_provider_usage.py#L32) | 32 | `"    )"` | — |
| [SRC-2477C41448-L000033](../../tests/test_answer_quality_provider_usage.py#L33) | 33 | `"    assert normalized == {\"prompt_tokens\": 5}"` | — |
| [SRC-2477C41448-L000034](../../tests/test_answer_quality_provider_usage.py#L34) | 34 | `""` | — |
| [SRC-2477C41448-L000035](../../tests/test_answer_quality_provider_usage.py#L35) | 35 | `""` | — |
| [SRC-2477C41448-L000036](../../tests/test_answer_quality_provider_usage.py#L36) | 36 | `"def test_nonfinite_or_negative_provider_cost_is_not_recorded():"` | — |
| [SRC-2477C41448-L000037](../../tests/test_answer_quality_provider_usage.py#L37) | 37 | `"    normalized = _normalized_provider_usage("` | — |
| [SRC-2477C41448-L000038](../../tests/test_answer_quality_provider_usage.py#L38) | 38 | `"        {\"prompt_tokens\": 2, \"cost\": float(\"nan\"), \"total_cost\": -1},"` | — |
| [SRC-2477C41448-L000039](../../tests/test_answer_quality_provider_usage.py#L39) | 39 | `"        provider_base_url=\"https://openrouter.ai/api/v1\","` | — |
| [SRC-2477C41448-L000040](../../tests/test_answer_quality_provider_usage.py#L40) | 40 | `"    )"` | — |
| [SRC-2477C41448-L000041](../../tests/test_answer_quality_provider_usage.py#L41) | 41 | `"    assert normalized == {\"prompt_tokens\": 2}"` | — |
| [SRC-2477C41448-L000042](../../tests/test_answer_quality_provider_usage.py#L42) | 42 | `""` | — |
| [SRC-2477C41448-L000043](../../tests/test_answer_quality_provider_usage.py#L43) | 43 | `""` | — |
| [SRC-2477C41448-L000044](../../tests/test_answer_quality_provider_usage.py#L44) | 44 | `"def test_completion_records_provider_usage_without_retaining_provider_body(monkeypatch):"` | — |
| [SRC-2477C41448-L000045](../../tests/test_answer_quality_provider_usage.py#L45) | 45 | `"    agent = WebAgent()"` | — |
| [SRC-2477C41448-L000046](../../tests/test_answer_quality_provider_usage.py#L46) | 46 | `"    agent.api_key = \"unit-test-key\""` | — |
| [SRC-2477C41448-L000047](../../tests/test_answer_quality_provider_usage.py#L47) | 47 | `"    agent.base_url = \"https://openrouter.ai/api/v1\""` | — |
| [SRC-2477C41448-L000048](../../tests/test_answer_quality_provider_usage.py#L48) | 48 | `"    agent.fallback_model = \"\""` | — |
| [SRC-2477C41448-L000049](../../tests/test_answer_quality_provider_usage.py#L49) | 49 | `""` | — |
| [SRC-2477C41448-L000050](../../tests/test_answer_quality_provider_usage.py#L50) | 50 | `"    class FakeResponse:"` | — |
| [SRC-2477C41448-L000051](../../tests/test_answer_quality_provider_usage.py#L51) | 51 | `"        status = 200"` | — |
| [SRC-2477C41448-L000052](../../tests/test_answer_quality_provider_usage.py#L52) | 52 | `""` | — |
| [SRC-2477C41448-L000053](../../tests/test_answer_quality_provider_usage.py#L53) | 53 | `"        def __enter__(self):"` | — |
| [SRC-2477C41448-L000054](../../tests/test_answer_quality_provider_usage.py#L54) | 54 | `"            return self"` | — |
| [SRC-2477C41448-L000055](../../tests/test_answer_quality_provider_usage.py#L55) | 55 | `""` | — |
| [SRC-2477C41448-L000056](../../tests/test_answer_quality_provider_usage.py#L56) | 56 | `"        def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-2477C41448-L000057](../../tests/test_answer_quality_provider_usage.py#L57) | 57 | `"            return False"` | — |
| [SRC-2477C41448-L000058](../../tests/test_answer_quality_provider_usage.py#L58) | 58 | `""` | — |
| [SRC-2477C41448-L000059](../../tests/test_answer_quality_provider_usage.py#L59) | 59 | `"        def read(self, limit):"` | — |
| [SRC-2477C41448-L000060](../../tests/test_answer_quality_provider_usage.py#L60) | 60 | `"            return json.dumps({"` | — |
| [SRC-2477C41448-L000061](../../tests/test_answer_quality_provider_usage.py#L61) | 61 | `"                \"choices\": [{"` | — |
| [SRC-2477C41448-L000062](../../tests/test_answer_quality_provider_usage.py#L62) | 62 | `"                    \"message\": {\"content\": \"إجابة اختبارية\"},"` | — |
| [SRC-2477C41448-L000063](../../tests/test_answer_quality_provider_usage.py#L63) | 63 | `"                    \"finish_reason\": \"stop\","` | — |
| [SRC-2477C41448-L000064](../../tests/test_answer_quality_provider_usage.py#L64) | 64 | `"                }],"` | — |
| [SRC-2477C41448-L000065](../../tests/test_answer_quality_provider_usage.py#L65) | 65 | `"                \"usage\": {"` | — |
| [SRC-2477C41448-L000066](../../tests/test_answer_quality_provider_usage.py#L66) | 66 | `"                    \"prompt_tokens\": 10,"` | — |
| [SRC-2477C41448-L000067](../../tests/test_answer_quality_provider_usage.py#L67) | 67 | `"                    \"completion_tokens\": 7,"` | — |
| [SRC-2477C41448-L000068](../../tests/test_answer_quality_provider_usage.py#L68) | 68 | `"                    \"total_tokens\": 17,"` | — |
| [SRC-2477C41448-L000069](../../tests/test_answer_quality_provider_usage.py#L69) | 69 | `"                    \"cost\": 0.0004,"` | — |
| [SRC-2477C41448-L000070](../../tests/test_answer_quality_provider_usage.py#L70) | 70 | `"                    \"debug_blob\": \"private-provider-details\","` | — |
| [SRC-2477C41448-L000071](../../tests/test_answer_quality_provider_usage.py#L71) | 71 | `"                },"` | — |
| [SRC-2477C41448-L000072](../../tests/test_answer_quality_provider_usage.py#L72) | 72 | `"            }).encode(\"utf-8\")"` | — |
| [SRC-2477C41448-L000073](../../tests/test_answer_quality_provider_usage.py#L73) | 73 | `""` | — |
| [SRC-2477C41448-L000074](../../tests/test_answer_quality_provider_usage.py#L74) | 74 | `"    monkeypatch.setattr(\"agents.web_agent._open_model_request\", lambda request, timeout: FakeResponse())"` | — |
| [SRC-2477C41448-L000075](../../tests/test_answer_quality_provider_usage.py#L75) | 75 | `"    answer = agent._request_completion("` | — |
| [SRC-2477C41448-L000076](../../tests/test_answer_quality_provider_usage.py#L76) | 76 | `"        [{\"role\": \"user\", \"content\": \"اختبر\"}],"` | — |
| [SRC-2477C41448-L000077](../../tests/test_answer_quality_provider_usage.py#L77) | 77 | `"        model=\"test/model\","` | — |
| [SRC-2477C41448-L000078](../../tests/test_answer_quality_provider_usage.py#L78) | 78 | `"    )"` | — |
| [SRC-2477C41448-L000079](../../tests/test_answer_quality_provider_usage.py#L79) | 79 | `"    assert answer == \"إجابة اختبارية\""` | — |
| [SRC-2477C41448-L000080](../../tests/test_answer_quality_provider_usage.py#L80) | 80 | `"    assert agent.model_usage[0][\"provider_usage\"] == {"` | — |
| [SRC-2477C41448-L000081](../../tests/test_answer_quality_provider_usage.py#L81) | 81 | `"        \"prompt_tokens\": 10,"` | — |
| [SRC-2477C41448-L000082](../../tests/test_answer_quality_provider_usage.py#L82) | 82 | `"        \"completion_tokens\": 7,"` | — |
| [SRC-2477C41448-L000083](../../tests/test_answer_quality_provider_usage.py#L83) | 83 | `"        \"total_tokens\": 17,"` | — |
| [SRC-2477C41448-L000084](../../tests/test_answer_quality_provider_usage.py#L84) | 84 | `"        \"cost_usd\": 0.0004,"` | — |
| [SRC-2477C41448-L000085](../../tests/test_answer_quality_provider_usage.py#L85) | 85 | `"    }"` | — |
| [SRC-2477C41448-L000086](../../tests/test_answer_quality_provider_usage.py#L86) | 86 | `"    assert \"debug_blob\" not in str(agent.model_usage)"` | — |
| [SRC-2477C41448-L000087](../../tests/test_answer_quality_provider_usage.py#L87) | 87 | `""` | — |
| [SRC-2477C41448-L000088](../../tests/test_answer_quality_provider_usage.py#L88) | 88 | `""` | — |
| [SRC-2477C41448-L000089](../../tests/test_answer_quality_provider_usage.py#L89) | 89 | `"def test_openrouter_cost_requires_real_hostname_boundary():"` | — |
| [SRC-2477C41448-L000090](../../tests/test_answer_quality_provider_usage.py#L90) | 90 | `"    normalized = _normalized_provider_usage("` | — |
| [SRC-2477C41448-L000091](../../tests/test_answer_quality_provider_usage.py#L91) | 91 | `"        {\"cost\": 0.05},"` | — |
| [SRC-2477C41448-L000092](../../tests/test_answer_quality_provider_usage.py#L92) | 92 | `"        provider_base_url=\"https://openrouter.ai.attacker.example/api/v1\","` | — |
| [SRC-2477C41448-L000093](../../tests/test_answer_quality_provider_usage.py#L93) | 93 | `"    )"` | — |
| [SRC-2477C41448-L000094](../../tests/test_answer_quality_provider_usage.py#L94) | 94 | `"    assert normalized is None"` | — |
| [SRC-2477C41448-L000095](../../tests/test_answer_quality_provider_usage.py#L95) | 95 | `""` | — |
| [SRC-2477C41448-L000096](../../tests/test_answer_quality_provider_usage.py#L96) | 96 | `"    normalized = _normalized_provider_usage("` | — |
| [SRC-2477C41448-L000097](../../tests/test_answer_quality_provider_usage.py#L97) | 97 | `"        {\"cost\": 0.05},"` | — |
| [SRC-2477C41448-L000098](../../tests/test_answer_quality_provider_usage.py#L98) | 98 | `"        provider_base_url=\"https://evilopenrouter.ai/api/v1\","` | — |
| [SRC-2477C41448-L000099](../../tests/test_answer_quality_provider_usage.py#L99) | 99 | `"    )"` | — |
| [SRC-2477C41448-L000100](../../tests/test_answer_quality_provider_usage.py#L100) | 100 | `"    assert normalized is None"` | — |
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
