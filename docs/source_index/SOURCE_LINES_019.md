# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **019**
- سجلات الأسطر: **800**
- النطاق: SRC-CAC5F305FE-L000057 إلى SRC-3451CC474D-L000325
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-CAC5F305FE — [tests/test_agent_modes.py](../../tests/test_agent_modes.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-B3062EB677-L000113](../../tests/test_answer_quality_runner.py#L113) | 113 | `"    monkeypatch.setattr(mod, \"post_agent\", fake_post)"` | — |
| [SRC-B3062EB677-L000114](../../tests/test_answer_quality_runner.py#L114) | 114 | `"    out = tmp_path / \"results.json\""` | — |
| [SRC-B3062EB677-L000115](../../tests/test_answer_quality_runner.py#L115) | 115 | `"    rc = mod.main("` | — |
| [SRC-B3062EB677-L000116](../../tests/test_answer_quality_runner.py#L116) | 116 | `"        ["` | — |
| [SRC-B3062EB677-L000117](../../tests/test_answer_quality_runner.py#L117) | 117 | `"            \"--mode\","` | — |
| [SRC-B3062EB677-L000118](../../tests/test_answer_quality_runner.py#L118) | 118 | `"            \"live\","` | — |
| [SRC-B3062EB677-L000119](../../tests/test_answer_quality_runner.py#L119) | 119 | `"            \"--corpus\","` | — |
| [SRC-B3062EB677-L000120](../../tests/test_answer_quality_runner.py#L120) | 120 | `"            str(CORPUS),"` | — |
| [SRC-B3062EB677-L000121](../../tests/test_answer_quality_runner.py#L121) | 121 | `"            \"--case-id\","` | — |
| [SRC-B3062EB677-L000122](../../tests/test_answer_quality_runner.py#L122) | 122 | `"            \"AQ-001\","` | — |
| [SRC-B3062EB677-L000123](../../tests/test_answer_quality_runner.py#L123) | 123 | `"            \"--limit\","` | — |
| [SRC-B3062EB677-L000124](../../tests/test_answer_quality_runner.py#L124) | 124 | `"            \"1\","` | — |
| [SRC-B3062EB677-L000125](../../tests/test_answer_quality_runner.py#L125) | 125 | `"            \"--out\","` | — |
| [SRC-B3062EB677-L000126](../../tests/test_answer_quality_runner.py#L126) | 126 | `"            str(out),"` | — |
| [SRC-B3062EB677-L000127](../../tests/test_answer_quality_runner.py#L127) | 127 | `"        ]"` | — |
| [SRC-B3062EB677-L000128](../../tests/test_answer_quality_runner.py#L128) | 128 | `"    )"` | — |
| [SRC-B3062EB677-L000129](../../tests/test_answer_quality_runner.py#L129) | 129 | `"    assert rc == 0"` | — |
| [SRC-B3062EB677-L000130](../../tests/test_answer_quality_runner.py#L130) | 130 | `"    payload = json.loads(out.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-B3062EB677-L000131](../../tests/test_answer_quality_runner.py#L131) | 131 | `"    assert payload[\"results\"][0][\"status\"] == \"NOT_TESTED\""` | — |
| [SRC-B3062EB677-L000132](../../tests/test_answer_quality_runner.py#L132) | 132 | `"    assert payload[\"results\"][0][\"evidence_fixture_injected\"] is False"` | — |
| [SRC-B3062EB677-L000133](../../tests/test_answer_quality_runner.py#L133) | 133 | `"    assert payload[\"results\"][0][\"transport_ok\"] is True"` | — |
| [SRC-B3062EB677-L000134](../../tests/test_answer_quality_runner.py#L134) | 134 | `""` | — |
| [SRC-B3062EB677-L000135](../../tests/test_answer_quality_runner.py#L135) | 135 | `""` | — |
| [SRC-B3062EB677-L000136](../../tests/test_answer_quality_runner.py#L136) | 136 | `"def test_validate_base_url_rejects_non_loopback_http():"` | — |
| [SRC-B3062EB677-L000137](../../tests/test_answer_quality_runner.py#L137) | 137 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000138](../../tests/test_answer_quality_runner.py#L138) | 138 | `"    with pytest.raises(ValueError, match=\"Plain HTTP\"):"` | — |
| [SRC-B3062EB677-L000139](../../tests/test_answer_quality_runner.py#L139) | 139 | `"        mod.validate_base_url(\"http://research.example\")"` | — |
| [SRC-B3062EB677-L000140](../../tests/test_answer_quality_runner.py#L140) | 140 | `""` | — |
| [SRC-B3062EB677-L000141](../../tests/test_answer_quality_runner.py#L141) | 141 | `""` | — |
| [SRC-B3062EB677-L000142](../../tests/test_answer_quality_runner.py#L142) | 142 | `"@pytest.mark.parametrize("` | — |
| [SRC-B3062EB677-L000143](../../tests/test_answer_quality_runner.py#L143) | 143 | `"    \"url\","` | — |
| [SRC-B3062EB677-L000144](../../tests/test_answer_quality_runner.py#L144) | 144 | `"    ["` | — |
| [SRC-B3062EB677-L000145](../../tests/test_answer_quality_runner.py#L145) | 145 | `"        \"https://user:password@example.com\","` | — |
| [SRC-B3062EB677-L000146](../../tests/test_answer_quality_runner.py#L146) | 146 | `"        \"https://example.com/private/path\","` | — |
| [SRC-B3062EB677-L000147](../../tests/test_answer_quality_runner.py#L147) | 147 | `"        \"https://example.com/?token=oops\","` | — |
| [SRC-B3062EB677-L000148](../../tests/test_answer_quality_runner.py#L148) | 148 | `"        \"https://example.com/#fragment\","` | — |
| [SRC-B3062EB677-L000149](../../tests/test_answer_quality_runner.py#L149) | 149 | `"    ],"` | — |
| [SRC-B3062EB677-L000150](../../tests/test_answer_quality_runner.py#L150) | 150 | `")"` | — |
| [SRC-B3062EB677-L000151](../../tests/test_answer_quality_runner.py#L151) | 151 | `"def test_validate_base_url_rejects_ambiguous_or_credential_bearing_urls(url):"` | — |
| [SRC-B3062EB677-L000152](../../tests/test_answer_quality_runner.py#L152) | 152 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000153](../../tests/test_answer_quality_runner.py#L153) | 153 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-B3062EB677-L000154](../../tests/test_answer_quality_runner.py#L154) | 154 | `"        mod.validate_base_url(url)"` | — |
| [SRC-B3062EB677-L000155](../../tests/test_answer_quality_runner.py#L155) | 155 | `""` | — |
| [SRC-B3062EB677-L000156](../../tests/test_answer_quality_runner.py#L156) | 156 | `""` | — |
| [SRC-B3062EB677-L000157](../../tests/test_answer_quality_runner.py#L157) | 157 | `"def test_remote_bearer_token_requires_exact_allowlisted_https_origin(monkeypatch):"` | — |
| [SRC-B3062EB677-L000158](../../tests/test_answer_quality_runner.py#L158) | 158 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000159](../../tests/test_answer_quality_runner.py#L159) | 159 | `"    monkeypatch.delenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", raising=False)"` | — |
| [SRC-B3062EB677-L000160](../../tests/test_answer_quality_runner.py#L160) | 160 | `"    with pytest.raises(ValueError, match=\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\"):"` | — |
| [SRC-B3062EB677-L000161](../../tests/test_answer_quality_runner.py#L161) | 161 | `"        mod.validate_base_url(\"https://app.example\", token_present=True)"` | — |
| [SRC-B3062EB677-L000162](../../tests/test_answer_quality_runner.py#L162) | 162 | `""` | — |
| [SRC-B3062EB677-L000163](../../tests/test_answer_quality_runner.py#L163) | 163 | `"    monkeypatch.setenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", \"https://app.example\")"` | — |
| [SRC-B3062EB677-L000164](../../tests/test_answer_quality_runner.py#L164) | 164 | `"    assert mod.validate_base_url(\"https://app.example/\", token_present=True) == \"https://app.example\""` | — |
| [SRC-B3062EB677-L000165](../../tests/test_answer_quality_runner.py#L165) | 165 | `"    with pytest.raises(ValueError, match=\"does not match\"):"` | — |
| [SRC-B3062EB677-L000166](../../tests/test_answer_quality_runner.py#L166) | 166 | `"        mod.validate_base_url(\"https://other.example\", token_present=True)"` | — |
| [SRC-B3062EB677-L000167](../../tests/test_answer_quality_runner.py#L167) | 167 | `""` | — |
| [SRC-B3062EB677-L000168](../../tests/test_answer_quality_runner.py#L168) | 168 | `""` | — |
| [SRC-B3062EB677-L000169](../../tests/test_answer_quality_runner.py#L169) | 169 | `"def test_remote_token_origin_comparison_normalizes_default_https_port(monkeypatch):"` | — |
| [SRC-B3062EB677-L000170](../../tests/test_answer_quality_runner.py#L170) | 170 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000171](../../tests/test_answer_quality_runner.py#L171) | 171 | `"    monkeypatch.setenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", \"https://app.example\")"` | — |
| [SRC-B3062EB677-L000172](../../tests/test_answer_quality_runner.py#L172) | 172 | `"    assert ("` | — |
| [SRC-B3062EB677-L000173](../../tests/test_answer_quality_runner.py#L173) | 173 | `"        mod.validate_base_url(\"https://app.example:443\", token_present=True)"` | — |
| [SRC-B3062EB677-L000174](../../tests/test_answer_quality_runner.py#L174) | 174 | `"        == \"https://app.example\""` | — |
| [SRC-B3062EB677-L000175](../../tests/test_answer_quality_runner.py#L175) | 175 | `"    )"` | — |
| [SRC-B3062EB677-L000176](../../tests/test_answer_quality_runner.py#L176) | 176 | `""` | — |
| [SRC-B3062EB677-L000177](../../tests/test_answer_quality_runner.py#L177) | 177 | `""` | — |
| [SRC-B3062EB677-L000178](../../tests/test_answer_quality_runner.py#L178) | 178 | `"def test_redirect_handler_refuses_following_redirects():"` | — |
| [SRC-B3062EB677-L000179](../../tests/test_answer_quality_runner.py#L179) | 179 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000180](../../tests/test_answer_quality_runner.py#L180) | 180 | `"    handler = mod._NoRedirectHandler()"` | — |
| [SRC-B3062EB677-L000181](../../tests/test_answer_quality_runner.py#L181) | 181 | `"    assert handler.redirect_request("` | — |
| [SRC-B3062EB677-L000182](../../tests/test_answer_quality_runner.py#L182) | 182 | `"        req=None,"` | — |
| [SRC-B3062EB677-L000183](../../tests/test_answer_quality_runner.py#L183) | 183 | `"        fp=None,"` | — |
| [SRC-B3062EB677-L000184](../../tests/test_answer_quality_runner.py#L184) | 184 | `"        code=302,"` | — |
| [SRC-B3062EB677-L000185](../../tests/test_answer_quality_runner.py#L185) | 185 | `"        msg=\"Found\","` | — |
| [SRC-B3062EB677-L000186](../../tests/test_answer_quality_runner.py#L186) | 186 | `"        headers={},"` | — |
| [SRC-B3062EB677-L000187](../../tests/test_answer_quality_runner.py#L187) | 187 | `"        newurl=\"https://attacker.example/collect\","` | — |
| [SRC-B3062EB677-L000188](../../tests/test_answer_quality_runner.py#L188) | 188 | `"    ) is None"` | — |
| [SRC-B3062EB677-L000189](../../tests/test_answer_quality_runner.py#L189) | 189 | `""` | — |
| [SRC-B3062EB677-L000190](../../tests/test_answer_quality_runner.py#L190) | 190 | `""` | — |
| [SRC-B3062EB677-L000191](../../tests/test_answer_quality_runner.py#L191) | 191 | `"def test_live_rejects_unapproved_remote_url_before_network(monkeypatch, capsys):"` | — |
| [SRC-B3062EB677-L000192](../../tests/test_answer_quality_runner.py#L192) | 192 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000193](../../tests/test_answer_quality_runner.py#L193) | 193 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"a-test-token\")"` | — |
| [SRC-B3062EB677-L000194](../../tests/test_answer_quality_runner.py#L194) | 194 | `"    monkeypatch.delenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", raising=False)"` | — |
| [SRC-B3062EB677-L000195](../../tests/test_answer_quality_runner.py#L195) | 195 | `"    rc = mod.run_live("` | — |
| [SRC-B3062EB677-L000196](../../tests/test_answer_quality_runner.py#L196) | 196 | `"        CORPUS,"` | — |
| [SRC-B3062EB677-L000197](../../tests/test_answer_quality_runner.py#L197) | 197 | `"        \"https://not-allowlisted.example\","` | — |
| [SRC-B3062EB677-L000198](../../tests/test_answer_quality_runner.py#L198) | 198 | `"        \"AQ-001\","` | — |
| [SRC-B3062EB677-L000199](../../tests/test_answer_quality_runner.py#L199) | 199 | `"        1,"` | — |
| [SRC-B3062EB677-L000200](../../tests/test_answer_quality_runner.py#L200) | 200 | `"        1.0,"` | — |
| [SRC-B3062EB677-L000201](../../tests/test_answer_quality_runner.py#L201) | 201 | `"        0.0,"` | — |
| [SRC-B3062EB677-L000202](../../tests/test_answer_quality_runner.py#L202) | 202 | `"        None,"` | — |
| [SRC-B3062EB677-L000203](../../tests/test_answer_quality_runner.py#L203) | 203 | `"    )"` | — |
| [SRC-B3062EB677-L000204](../../tests/test_answer_quality_runner.py#L204) | 204 | `"    assert rc == 2"` | — |
| [SRC-B3062EB677-L000205](../../tests/test_answer_quality_runner.py#L205) | 205 | `"    assert \"Unsafe base URL\" in capsys.readouterr().err"` | — |
| [SRC-B3062EB677-L000206](../../tests/test_answer_quality_runner.py#L206) | 206 | `""` | — |
| [SRC-B3062EB677-L000207](../../tests/test_answer_quality_runner.py#L207) | 207 | `""` | — |
| [SRC-B3062EB677-L000208](../../tests/test_answer_quality_runner.py#L208) | 208 | `"def test_live_transport_error_still_not_pass(monkeypatch, tmp_path):"` | — |
| [SRC-B3062EB677-L000209](../../tests/test_answer_quality_runner.py#L209) | 209 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000210](../../tests/test_answer_quality_runner.py#L210) | 210 | `""` | — |
| [SRC-B3062EB677-L000211](../../tests/test_answer_quality_runner.py#L211) | 211 | `"    def fake_post(base_url, question, timeout, token):"` | — |
| [SRC-B3062EB677-L000212](../../tests/test_answer_quality_runner.py#L212) | 212 | `"        return 0, {\"error\": \"URLError\", \"detail\": \"connection refused\"}"` | — |
| [SRC-B3062EB677-L000213](../../tests/test_answer_quality_runner.py#L213) | 213 | `""` | — |
| [SRC-B3062EB677-L000214](../../tests/test_answer_quality_runner.py#L214) | 214 | `"    monkeypatch.setattr(mod, \"post_agent\", fake_post)"` | — |
| [SRC-B3062EB677-L000215](../../tests/test_answer_quality_runner.py#L215) | 215 | `"    out = tmp_path / \"results.json\""` | — |
| [SRC-B3062EB677-L000216](../../tests/test_answer_quality_runner.py#L216) | 216 | `"    rc = mod.main("` | — |
| [SRC-B3062EB677-L000217](../../tests/test_answer_quality_runner.py#L217) | 217 | `"        ["` | — |
| [SRC-B3062EB677-L000218](../../tests/test_answer_quality_runner.py#L218) | 218 | `"            \"--mode\","` | — |
| [SRC-B3062EB677-L000219](../../tests/test_answer_quality_runner.py#L219) | 219 | `"            \"live\","` | — |
| [SRC-B3062EB677-L000220](../../tests/test_answer_quality_runner.py#L220) | 220 | `"            \"--corpus\","` | — |
| [SRC-B3062EB677-L000221](../../tests/test_answer_quality_runner.py#L221) | 221 | `"            str(CORPUS),"` | — |
| [SRC-B3062EB677-L000222](../../tests/test_answer_quality_runner.py#L222) | 222 | `"            \"--case-id\","` | — |
| [SRC-B3062EB677-L000223](../../tests/test_answer_quality_runner.py#L223) | 223 | `"            \"AQ-001\","` | — |
| [SRC-B3062EB677-L000224](../../tests/test_answer_quality_runner.py#L224) | 224 | `"            \"--out\","` | — |
| [SRC-B3062EB677-L000225](../../tests/test_answer_quality_runner.py#L225) | 225 | `"            str(out),"` | — |
| [SRC-B3062EB677-L000226](../../tests/test_answer_quality_runner.py#L226) | 226 | `"        ]"` | — |
| [SRC-B3062EB677-L000227](../../tests/test_answer_quality_runner.py#L227) | 227 | `"    )"` | — |
| [SRC-B3062EB677-L000228](../../tests/test_answer_quality_runner.py#L228) | 228 | `"    assert rc == 0"` | — |
| [SRC-B3062EB677-L000229](../../tests/test_answer_quality_runner.py#L229) | 229 | `"    payload = json.loads(out.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-B3062EB677-L000230](../../tests/test_answer_quality_runner.py#L230) | 230 | `"    assert payload[\"results\"][0][\"status\"] == \"NOT_TESTED\""` | — |
| [SRC-B3062EB677-L000231](../../tests/test_answer_quality_runner.py#L231) | 231 | `"    assert payload[\"results\"][0][\"transport_ok\"] is False"` | — |
## اختبارات

### FILE-3451CC474D — [tests/test_api.py](../../tests/test_api.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3451CC474D-L000001](../../tests/test_api.py#L1) | 1 | `"\"\"\"HTTP integration tests for Omarai local API and assistant endpoints.\"\"\""` | — |
| [SRC-3451CC474D-L000002](../../tests/test_api.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-3451CC474D-L000003](../../tests/test_api.py#L3) | 3 | `""` | — |
| [SRC-3451CC474D-L000004](../../tests/test_api.py#L4) | 4 | `"import json"` | — |
| [SRC-3451CC474D-L000005](../../tests/test_api.py#L5) | 5 | `"import socket"` | — |
| [SRC-3451CC474D-L000006](../../tests/test_api.py#L6) | 6 | `"import threading"` | — |
| [SRC-3451CC474D-L000007](../../tests/test_api.py#L7) | 7 | `"from collections import defaultdict, deque"` | — |
| [SRC-3451CC474D-L000008](../../tests/test_api.py#L8) | 8 | `"from http.server import ThreadingHTTPServer"` | — |
| [SRC-3451CC474D-L000009](../../tests/test_api.py#L9) | 9 | `"from types import SimpleNamespace"` | — |
| [SRC-3451CC474D-L000010](../../tests/test_api.py#L10) | 10 | `"from urllib.error import HTTPError"` | — |
| [SRC-3451CC474D-L000011](../../tests/test_api.py#L11) | 11 | `"from urllib.request import Request, urlopen"` | — |
| [SRC-3451CC474D-L000012](../../tests/test_api.py#L12) | 12 | `""` | — |
| [SRC-3451CC474D-L000013](../../tests/test_api.py#L13) | 13 | `"import pytest"` | — |
| [SRC-3451CC474D-L000014](../../tests/test_api.py#L14) | 14 | `""` | — |
| [SRC-3451CC474D-L000015](../../tests/test_api.py#L15) | 15 | `"from agents.omarai import LeadStore"` | — |
| [SRC-3451CC474D-L000016](../../tests/test_api.py#L16) | 16 | `"from api.omarai import Handler"` | — |
| [SRC-3451CC474D-L000017](../../tests/test_api.py#L17) | 17 | `""` | — |
| [SRC-3451CC474D-L000018](../../tests/test_api.py#L18) | 18 | `""` | — |
| [SRC-3451CC474D-L000019](../../tests/test_api.py#L19) | 19 | `"@pytest.fixture"` | — |
| [SRC-3451CC474D-L000020](../../tests/test_api.py#L20) | 20 | `"def local_api(tmp_path):"` | — |
| [SRC-3451CC474D-L000021](../../tests/test_api.py#L21) | 21 | `"    \"\"\"Run the real handler on an ephemeral loopback port with an isolated database.\"\"\""` | — |
| [SRC-3451CC474D-L000022](../../tests/test_api.py#L22) | 22 | `"    previous_store = Handler.store"` | — |
| [SRC-3451CC474D-L000023](../../tests/test_api.py#L23) | 23 | `"    Handler.store = LeadStore(tmp_path / \"api-test.sqlite3\")"` | — |
| [SRC-3451CC474D-L000024](../../tests/test_api.py#L24) | 24 | `"    server = ThreadingHTTPServer((\"127.0.0.1\", 0), Handler)"` | — |
| [SRC-3451CC474D-L000025](../../tests/test_api.py#L25) | 25 | `"    thread = threading.Thread(target=server.serve_forever, daemon=True)"` | — |
| [SRC-3451CC474D-L000026](../../tests/test_api.py#L26) | 26 | `"    thread.start()"` | — |
| [SRC-3451CC474D-L000027](../../tests/test_api.py#L27) | 27 | `"    try:"` | — |
| [SRC-3451CC474D-L000028](../../tests/test_api.py#L28) | 28 | `"        yield f\"http://127.0.0.1:{server.server_port}\""` | — |
| [SRC-3451CC474D-L000029](../../tests/test_api.py#L29) | 29 | `"    finally:"` | — |
| [SRC-3451CC474D-L000030](../../tests/test_api.py#L30) | 30 | `"        server.shutdown()"` | — |
| [SRC-3451CC474D-L000031](../../tests/test_api.py#L31) | 31 | `"        server.server_close()"` | — |
| [SRC-3451CC474D-L000032](../../tests/test_api.py#L32) | 32 | `"        thread.join(timeout=3)"` | — |
| [SRC-3451CC474D-L000033](../../tests/test_api.py#L33) | 33 | `"        Handler.store = previous_store"` | — |
| [SRC-3451CC474D-L000034](../../tests/test_api.py#L34) | 34 | `""` | — |
| [SRC-3451CC474D-L000035](../../tests/test_api.py#L35) | 35 | `""` | — |
| [SRC-3451CC474D-L000036](../../tests/test_api.py#L36) | 36 | `"def request_json(base, path, method=\"GET\", payload=None, headers=None):"` | — |
| [SRC-3451CC474D-L000037](../../tests/test_api.py#L37) | 37 | `"    body = None if payload is None else json.dumps(payload, ensure_ascii=False).encode(\"utf-8\")"` | — |
| [SRC-3451CC474D-L000038](../../tests/test_api.py#L38) | 38 | `"    request_headers = dict(headers or {})"` | — |
| [SRC-3451CC474D-L000039](../../tests/test_api.py#L39) | 39 | `"    if body is not None and \"Content-Type\" not in request_headers:"` | — |
| [SRC-3451CC474D-L000040](../../tests/test_api.py#L40) | 40 | `"        request_headers[\"Content-Type\"] = \"application/json\""` | — |
| [SRC-3451CC474D-L000041](../../tests/test_api.py#L41) | 41 | `"    request = Request(base + path, data=body, method=method, headers=request_headers)"` | — |
| [SRC-3451CC474D-L000042](../../tests/test_api.py#L42) | 42 | `"    try:"` | — |
| [SRC-3451CC474D-L000043](../../tests/test_api.py#L43) | 43 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000044](../../tests/test_api.py#L44) | 44 | `"            return response.status, json.loads(response.read().decode(\"utf-8\"))"` | — |
| [SRC-3451CC474D-L000045](../../tests/test_api.py#L45) | 45 | `"    except HTTPError as error:"` | — |
| [SRC-3451CC474D-L000046](../../tests/test_api.py#L46) | 46 | `"        return error.code, json.loads(error.read().decode(\"utf-8\"))"` | — |
| [SRC-3451CC474D-L000047](../../tests/test_api.py#L47) | 47 | `""` | — |
| [SRC-3451CC474D-L000048](../../tests/test_api.py#L48) | 48 | `""` | — |
| [SRC-3451CC474D-L000049](../../tests/test_api.py#L49) | 49 | `"def test_api_health_analyze_save_duplicate_list_and_status(local_api):"` | — |
| [SRC-3451CC474D-L000050](../../tests/test_api.py#L50) | 50 | `"    status, health = request_json(local_api, \"/api/health\")"` | — |
| [SRC-3451CC474D-L000051](../../tests/test_api.py#L51) | 51 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000052](../../tests/test_api.py#L52) | 52 | `"    assert health[\"app\"] == \"Omarai\""` | — |
| [SRC-3451CC474D-L000053](../../tests/test_api.py#L53) | 53 | `"    assert health[\"mode\"] == \"web-research\""` | — |
| [SRC-3451CC474D-L000054](../../tests/test_api.py#L54) | 54 | `"    assert health[\"agent\"][\"verification_scope\"][\"live_network_checks_performed\"] is False"` | — |
| [SRC-3451CC474D-L000055](../../tests/test_api.py#L55) | 55 | `"    assert health[\"agent\"][\"verification_scope\"][\"live_diagnostics_endpoint\"] == \"POST /api/diagnostics\""` | — |
| [SRC-3451CC474D-L000056](../../tests/test_api.py#L56) | 56 | `""` | — |
| [SRC-3451CC474D-L000057](../../tests/test_api.py#L57) | 57 | `"    text = \"بدور على شقة في التجمع الخامس وممكن معاينة\""` | — |
| [SRC-3451CC474D-L000058](../../tests/test_api.py#L58) | 58 | `"    status, assessment = request_json("` | — |
| [SRC-3451CC474D-L000059](../../tests/test_api.py#L59) | 59 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000060](../../tests/test_api.py#L60) | 60 | `"        \"/api/analyze\","` | — |
| [SRC-3451CC474D-L000061](../../tests/test_api.py#L61) | 61 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000062](../../tests/test_api.py#L62) | 62 | `"        payload={\"text\": text, \"product_terms\": [\"شقة\"], \"location_terms\": [\"التجمع الخامس\"]},"` | — |
| [SRC-3451CC474D-L000063](../../tests/test_api.py#L63) | 63 | `"    )"` | — |
| [SRC-3451CC474D-L000064](../../tests/test_api.py#L64) | 64 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000065](../../tests/test_api.py#L65) | 65 | `"    assert assessment[\"label\"] == \"high_intent\""` | — |
| [SRC-3451CC474D-L000066](../../tests/test_api.py#L66) | 66 | `"    assert {item[\"category\"] for item in assessment[\"matched_signals\"]} >= {"` | — |
| [SRC-3451CC474D-L000067](../../tests/test_api.py#L67) | 67 | `"        \"high\", \"next_step\", \"product_context\", \"location_context\""` | — |
| [SRC-3451CC474D-L000068](../../tests/test_api.py#L68) | 68 | `"    }"` | — |
| [SRC-3451CC474D-L000069](../../tests/test_api.py#L69) | 69 | `""` | — |
| [SRC-3451CC474D-L000070](../../tests/test_api.py#L70) | 70 | `"    payload = {"` | — |
| [SRC-3451CC474D-L000071](../../tests/test_api.py#L71) | 71 | `"        \"text\": text,"` | — |
| [SRC-3451CC474D-L000072](../../tests/test_api.py#L72) | 72 | `"        \"source_url\": \"https://example.com/posts/123\","` | — |
| [SRC-3451CC474D-L000073](../../tests/test_api.py#L73) | 73 | `"        \"platform\": \"Public website\","` | — |
| [SRC-3451CC474D-L000074](../../tests/test_api.py#L74) | 74 | `"        \"product_terms\": [\"شقة\"],"` | — |
| [SRC-3451CC474D-L000075](../../tests/test_api.py#L75) | 75 | `"        \"location_terms\": [\"التجمع الخامس\"],"` | — |
| [SRC-3451CC474D-L000076](../../tests/test_api.py#L76) | 76 | `"    }"` | — |
| [SRC-3451CC474D-L000077](../../tests/test_api.py#L77) | 77 | `"    status, saved = request_json(local_api, \"/api/leads\", method=\"POST\", payload=payload)"` | — |
| [SRC-3451CC474D-L000078](../../tests/test_api.py#L78) | 78 | `"    assert status == 201"` | — |
| [SRC-3451CC474D-L000079](../../tests/test_api.py#L79) | 79 | `"    assert saved[\"created\"] is True"` | — |
| [SRC-3451CC474D-L000080](../../tests/test_api.py#L80) | 80 | `"    assert saved[\"lead\"][\"assessment\"][\"label\"] == \"high_intent\""` | — |
| [SRC-3451CC474D-L000081](../../tests/test_api.py#L81) | 81 | `"    assert \"product_context\" in {"` | — |
| [SRC-3451CC474D-L000082](../../tests/test_api.py#L82) | 82 | `"        item[\"category\"] for item in saved[\"lead\"][\"assessment\"][\"matched_signals\"]"` | — |
| [SRC-3451CC474D-L000083](../../tests/test_api.py#L83) | 83 | `"    }"` | — |
| [SRC-3451CC474D-L000084](../../tests/test_api.py#L84) | 84 | `"    status, duplicate = request_json(local_api, \"/api/leads\", method=\"POST\", payload=payload)"` | — |
| [SRC-3451CC474D-L000085](../../tests/test_api.py#L85) | 85 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000086](../../tests/test_api.py#L86) | 86 | `"    assert duplicate[\"created\"] is False"` | — |
| [SRC-3451CC474D-L000087](../../tests/test_api.py#L87) | 87 | `""` | — |
| [SRC-3451CC474D-L000088](../../tests/test_api.py#L88) | 88 | `"    status, listing = request_json(local_api, \"/api/leads?limit=25\")"` | — |
| [SRC-3451CC474D-L000089](../../tests/test_api.py#L89) | 89 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000090](../../tests/test_api.py#L90) | 90 | `"    assert listing[\"count\"] == 1"` | — |
| [SRC-3451CC474D-L000091](../../tests/test_api.py#L91) | 91 | `"    lead_id = listing[\"leads\"][0][\"id\"]"` | — |
| [SRC-3451CC474D-L000092](../../tests/test_api.py#L92) | 92 | `""` | — |
| [SRC-3451CC474D-L000093](../../tests/test_api.py#L93) | 93 | `"    status, changed = request_json("` | — |
| [SRC-3451CC474D-L000094](../../tests/test_api.py#L94) | 94 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000095](../../tests/test_api.py#L95) | 95 | `"        f\"/api/leads/{lead_id}/status\","` | — |
| [SRC-3451CC474D-L000096](../../tests/test_api.py#L96) | 96 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000097](../../tests/test_api.py#L97) | 97 | `"        payload={\"status\": \"qualified\"},"` | — |
| [SRC-3451CC474D-L000098](../../tests/test_api.py#L98) | 98 | `"    )"` | — |
| [SRC-3451CC474D-L000099](../../tests/test_api.py#L99) | 99 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000100](../../tests/test_api.py#L100) | 100 | `"    assert changed[\"lead\"][\"status\"] == \"qualified\""` | — |
| [SRC-3451CC474D-L000101](../../tests/test_api.py#L101) | 101 | `""` | — |
| [SRC-3451CC474D-L000102](../../tests/test_api.py#L102) | 102 | `"    status, stats = request_json("` | — |
| [SRC-3451CC474D-L000103](../../tests/test_api.py#L103) | 103 | `"        local_api, \"/api/ask\", method=\"POST\", payload={\"question\": \"كام عميل عندي؟\"}"` | — |
| [SRC-3451CC474D-L000104](../../tests/test_api.py#L104) | 104 | `"    )"` | — |
| [SRC-3451CC474D-L000105](../../tests/test_api.py#L105) | 105 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000106](../../tests/test_api.py#L106) | 106 | `"    assert stats[\"kind\"] == \"local_statistics\""` | — |
| [SRC-3451CC474D-L000107](../../tests/test_api.py#L107) | 107 | `"    assert \"1 إشارة\" in stats[\"answer\"]"` | — |
| [SRC-3451CC474D-L000108](../../tests/test_api.py#L108) | 108 | `""` | — |
| [SRC-3451CC474D-L000109](../../tests/test_api.py#L109) | 109 | `"    status, recommendation = request_json("` | — |
| [SRC-3451CC474D-L000110](../../tests/test_api.py#L110) | 110 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000111](../../tests/test_api.py#L111) | 111 | `"        \"/api/ask\","` | — |
| [SRC-3451CC474D-L000112](../../tests/test_api.py#L112) | 112 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000113](../../tests/test_api.py#L113) | 113 | `"        payload={\"question\": \"مين أفضل إشارة أراجعها؟\"},"` | — |
| [SRC-3451CC474D-L000114](../../tests/test_api.py#L114) | 114 | `"    )"` | — |
| [SRC-3451CC474D-L000115](../../tests/test_api.py#L115) | 115 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000116](../../tests/test_api.py#L116) | 116 | `"    assert recommendation[\"kind\"] == \"lead_recommendation\""` | — |
| [SRC-3451CC474D-L000117](../../tests/test_api.py#L117) | 117 | `"    assert payload[\"source_url\"] in recommendation[\"answer\"]"` | — |
| [SRC-3451CC474D-L000118](../../tests/test_api.py#L118) | 118 | `""` | — |
| [SRC-3451CC474D-L000119](../../tests/test_api.py#L119) | 119 | `""` | — |
| [SRC-3451CC474D-L000120](../../tests/test_api.py#L120) | 120 | `"def test_api_rejects_invalid_filters_and_request_shapes(local_api):"` | — |
| [SRC-3451CC474D-L000121](../../tests/test_api.py#L121) | 121 | `"    status, error = request_json(local_api, \"/api/leads?limit=not-a-number\")"` | — |
| [SRC-3451CC474D-L000122](../../tests/test_api.py#L122) | 122 | `"    assert status == 400"` | — |
| [SRC-3451CC474D-L000123](../../tests/test_api.py#L123) | 123 | `"    assert \"limit\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000124](../../tests/test_api.py#L124) | 124 | `""` | — |
| [SRC-3451CC474D-L000125](../../tests/test_api.py#L125) | 125 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000126](../../tests/test_api.py#L126) | 126 | `"        local_api, \"/api/analyze\", method=\"POST\", payload=[\"not\", \"an\", \"object\"]"` | — |
| [SRC-3451CC474D-L000127](../../tests/test_api.py#L127) | 127 | `"    )"` | — |
| [SRC-3451CC474D-L000128](../../tests/test_api.py#L128) | 128 | `"    assert status == 400"` | — |
| [SRC-3451CC474D-L000129](../../tests/test_api.py#L129) | 129 | `"    assert \"object\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000130](../../tests/test_api.py#L130) | 130 | `""` | — |
| [SRC-3451CC474D-L000131](../../tests/test_api.py#L131) | 131 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000132](../../tests/test_api.py#L132) | 132 | `"        local_api, \"/api/ask\", method=\"POST\", payload={\"question\": \"\"}"` | — |
| [SRC-3451CC474D-L000133](../../tests/test_api.py#L133) | 133 | `"    )"` | — |
| [SRC-3451CC474D-L000134](../../tests/test_api.py#L134) | 134 | `"    assert status == 400"` | — |
| [SRC-3451CC474D-L000135](../../tests/test_api.py#L135) | 135 | `"    assert \"question\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000136](../../tests/test_api.py#L136) | 136 | `""` | — |
| [SRC-3451CC474D-L000137](../../tests/test_api.py#L137) | 137 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000138](../../tests/test_api.py#L138) | 138 | `"        local_api, \"/api/leads\", method=\"POST\", payload={"` | — |
| [SRC-3451CC474D-L000139](../../tests/test_api.py#L139) | 139 | `"            \"text\": \"بدور على شقة\", \"source_url\": \"file:///private/data\", \"platform\": \"manual\""` | — |
| [SRC-3451CC474D-L000140](../../tests/test_api.py#L140) | 140 | `"        }"` | — |
| [SRC-3451CC474D-L000141](../../tests/test_api.py#L141) | 141 | `"    )"` | — |
| [SRC-3451CC474D-L000142](../../tests/test_api.py#L142) | 142 | `"    assert status == 400"` | — |
| [SRC-3451CC474D-L000143](../../tests/test_api.py#L143) | 143 | `"    assert \"absolute\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000144](../../tests/test_api.py#L144) | 144 | `""` | — |
| [SRC-3451CC474D-L000145](../../tests/test_api.py#L145) | 145 | `""` | — |
| [SRC-3451CC474D-L000146](../../tests/test_api.py#L146) | 146 | `"def test_api_blocks_non_json_and_cross_origin_posts(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000147](../../tests/test_api.py#L147) | 147 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000148](../../tests/test_api.py#L148) | 148 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000149](../../tests/test_api.py#L149) | 149 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000150](../../tests/test_api.py#L150) | 150 | `"        \"/api/ask\","` | — |
| [SRC-3451CC474D-L000151](../../tests/test_api.py#L151) | 151 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000152](../../tests/test_api.py#L152) | 152 | `"        payload={\"question\": \"كام عميل؟\"},"` | — |
| [SRC-3451CC474D-L000153](../../tests/test_api.py#L153) | 153 | `"        headers={\"Content-Type\": \"text/plain\"},"` | — |
| [SRC-3451CC474D-L000154](../../tests/test_api.py#L154) | 154 | `"    )"` | — |
| [SRC-3451CC474D-L000155](../../tests/test_api.py#L155) | 155 | `"    assert status == 415"` | — |
| [SRC-3451CC474D-L000156](../../tests/test_api.py#L156) | 156 | `"    assert \"Content-Type\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000157](../../tests/test_api.py#L157) | 157 | `""` | — |
| [SRC-3451CC474D-L000158](../../tests/test_api.py#L158) | 158 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000159](../../tests/test_api.py#L159) | 159 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000160](../../tests/test_api.py#L160) | 160 | `"        \"/api/ask\","` | — |
| [SRC-3451CC474D-L000161](../../tests/test_api.py#L161) | 161 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000162](../../tests/test_api.py#L162) | 162 | `"        payload={\"question\": \"كام عميل؟\"},"` | — |
| [SRC-3451CC474D-L000163](../../tests/test_api.py#L163) | 163 | `"        headers={\"Origin\": \"https://attacker.example\"},"` | — |
| [SRC-3451CC474D-L000164](../../tests/test_api.py#L164) | 164 | `"    )"` | — |
| [SRC-3451CC474D-L000165](../../tests/test_api.py#L165) | 165 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L000166](../../tests/test_api.py#L166) | 166 | `"    assert \"cross-origin\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000167](../../tests/test_api.py#L167) | 167 | `""` | — |
| [SRC-3451CC474D-L000168](../../tests/test_api.py#L168) | 168 | `""` | — |
| [SRC-3451CC474D-L000169](../../tests/test_api.py#L169) | 169 | `"def test_configured_frontend_origin_supports_preflight_and_post(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000170](../../tests/test_api.py#L170) | 170 | `"    origin = \"https://frontend.example\""` | — |
| [SRC-3451CC474D-L000171](../../tests/test_api.py#L171) | 171 | `"    monkeypatch.setenv(\"OMARAI_ALLOWED_ORIGINS\", origin)"` | — |
| [SRC-3451CC474D-L000172](../../tests/test_api.py#L172) | 172 | `""` | — |
| [SRC-3451CC474D-L000173](../../tests/test_api.py#L173) | 173 | `"    preflight = Request("` | — |
| [SRC-3451CC474D-L000174](../../tests/test_api.py#L174) | 174 | `"        local_api + \"/api/agent\","` | — |
| [SRC-3451CC474D-L000175](../../tests/test_api.py#L175) | 175 | `"        method=\"OPTIONS\","` | — |
| [SRC-3451CC474D-L000176](../../tests/test_api.py#L176) | 176 | `"        headers={"` | — |
| [SRC-3451CC474D-L000177](../../tests/test_api.py#L177) | 177 | `"            \"Origin\": origin,"` | — |
| [SRC-3451CC474D-L000178](../../tests/test_api.py#L178) | 178 | `"            \"Access-Control-Request-Method\": \"POST\","` | — |
| [SRC-3451CC474D-L000179](../../tests/test_api.py#L179) | 179 | `"            \"Access-Control-Request-Headers\": \"authorization,content-type\","` | — |
| [SRC-3451CC474D-L000180](../../tests/test_api.py#L180) | 180 | `"        },"` | — |
| [SRC-3451CC474D-L000181](../../tests/test_api.py#L181) | 181 | `"    )"` | — |
| [SRC-3451CC474D-L000182](../../tests/test_api.py#L182) | 182 | `"    with urlopen(preflight, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000183](../../tests/test_api.py#L183) | 183 | `"        assert response.status == 204"` | — |
| [SRC-3451CC474D-L000184](../../tests/test_api.py#L184) | 184 | `"        assert response.headers.get(\"Access-Control-Allow-Origin\") == origin"` | — |
| [SRC-3451CC474D-L000185](../../tests/test_api.py#L185) | 185 | `"        assert response.headers.get(\"Access-Control-Allow-Methods\") == \"GET, POST, OPTIONS\""` | — |
| [SRC-3451CC474D-L000186](../../tests/test_api.py#L186) | 186 | `"        assert response.headers.get(\"Access-Control-Allow-Headers\") == \"Authorization, Content-Type\""` | — |
| [SRC-3451CC474D-L000187](../../tests/test_api.py#L187) | 187 | `""` | — |
| [SRC-3451CC474D-L000188](../../tests/test_api.py#L188) | 188 | `"    body = json.dumps({\"question\": \"مين أفضل إشارة أراجعها؟\"}, ensure_ascii=False).encode(\"utf-8\")"` | — |
| [SRC-3451CC474D-L000189](../../tests/test_api.py#L189) | 189 | `"    post = Request("` | — |
| [SRC-3451CC474D-L000190](../../tests/test_api.py#L190) | 190 | `"        local_api + \"/api/ask\","` | — |
| [SRC-3451CC474D-L000191](../../tests/test_api.py#L191) | 191 | `"        data=body,"` | — |
| [SRC-3451CC474D-L000192](../../tests/test_api.py#L192) | 192 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000193](../../tests/test_api.py#L193) | 193 | `"        headers={\"Content-Type\": \"application/json\", \"Origin\": origin},"` | — |
| [SRC-3451CC474D-L000194](../../tests/test_api.py#L194) | 194 | `"    )"` | — |
| [SRC-3451CC474D-L000195](../../tests/test_api.py#L195) | 195 | `"    with urlopen(post, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000196](../../tests/test_api.py#L196) | 196 | `"        payload = json.loads(response.read().decode(\"utf-8\"))"` | — |
| [SRC-3451CC474D-L000197](../../tests/test_api.py#L197) | 197 | `"        assert response.status == 200"` | — |
| [SRC-3451CC474D-L000198](../../tests/test_api.py#L198) | 198 | `"        assert response.headers.get(\"Access-Control-Allow-Origin\") == origin"` | — |
| [SRC-3451CC474D-L000199](../../tests/test_api.py#L199) | 199 | `"        assert payload[\"kind\"] == \"no_data\""` | — |
| [SRC-3451CC474D-L000200](../../tests/test_api.py#L200) | 200 | `""` | — |
| [SRC-3451CC474D-L000201](../../tests/test_api.py#L201) | 201 | `""` | — |
| [SRC-3451CC474D-L000202](../../tests/test_api.py#L202) | 202 | `"def test_preflight_rejects_unconfigured_origin(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000203](../../tests/test_api.py#L203) | 203 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000204](../../tests/test_api.py#L204) | 204 | `"    preflight = Request("` | — |
| [SRC-3451CC474D-L000205](../../tests/test_api.py#L205) | 205 | `"        local_api + \"/api/agent\","` | — |
| [SRC-3451CC474D-L000206](../../tests/test_api.py#L206) | 206 | `"        method=\"OPTIONS\","` | — |
| [SRC-3451CC474D-L000207](../../tests/test_api.py#L207) | 207 | `"        headers={"` | — |
| [SRC-3451CC474D-L000208](../../tests/test_api.py#L208) | 208 | `"            \"Origin\": \"https://attacker.example\","` | — |
| [SRC-3451CC474D-L000209](../../tests/test_api.py#L209) | 209 | `"            \"Access-Control-Request-Method\": \"POST\","` | — |
| [SRC-3451CC474D-L000210](../../tests/test_api.py#L210) | 210 | `"        },"` | — |
| [SRC-3451CC474D-L000211](../../tests/test_api.py#L211) | 211 | `"    )"` | — |
| [SRC-3451CC474D-L000212](../../tests/test_api.py#L212) | 212 | `"    with pytest.raises(HTTPError) as error:"` | — |
| [SRC-3451CC474D-L000213](../../tests/test_api.py#L213) | 213 | `"        urlopen(preflight, timeout=3)"` | — |
| [SRC-3451CC474D-L000214](../../tests/test_api.py#L214) | 214 | `"    assert error.value.code == 403"` | — |
| [SRC-3451CC474D-L000215](../../tests/test_api.py#L215) | 215 | `""` | — |
| [SRC-3451CC474D-L000216](../../tests/test_api.py#L216) | 216 | `""` | — |
| [SRC-3451CC474D-L000217](../../tests/test_api.py#L217) | 217 | `"def test_ask_is_honest_when_database_is_empty(local_api):"` | — |
| [SRC-3451CC474D-L000218](../../tests/test_api.py#L218) | 218 | `"    status, answer = request_json("` | — |
| [SRC-3451CC474D-L000219](../../tests/test_api.py#L219) | 219 | `"        local_api, \"/api/ask\", method=\"POST\", payload={\"question\": \"مين أفضل إشارة أراجعها؟\"}"` | — |
| [SRC-3451CC474D-L000220](../../tests/test_api.py#L220) | 220 | `"    )"` | — |
| [SRC-3451CC474D-L000221](../../tests/test_api.py#L221) | 221 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000222](../../tests/test_api.py#L222) | 222 | `"    assert answer[\"kind\"] == \"no_data\""` | — |
| [SRC-3451CC474D-L000223](../../tests/test_api.py#L223) | 223 | `"    assert \"لا توجد إشارة\" in answer[\"answer\"]"` | — |
| [SRC-3451CC474D-L000224](../../tests/test_api.py#L224) | 224 | `""` | — |
| [SRC-3451CC474D-L000225](../../tests/test_api.py#L225) | 225 | `""` | — |
| [SRC-3451CC474D-L000226](../../tests/test_api.py#L226) | 226 | `""` | — |
| [SRC-3451CC474D-L000227](../../tests/test_api.py#L227) | 227 | `"def test_web_agent_endpoint_uses_agent_result(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000228](../../tests/test_api.py#L228) | 228 | `"    from api.omarai import WebAgent"` | — |
| [SRC-3451CC474D-L000229](../../tests/test_api.py#L229) | 229 | `""` | — |
| [SRC-3451CC474D-L000230](../../tests/test_api.py#L230) | 230 | `"    def fake_answer(self, question, history=None):"` | — |
| [SRC-3451CC474D-L000231](../../tests/test_api.py#L231) | 231 | `"        return {"` | — |
| [SRC-3451CC474D-L000232](../../tests/test_api.py#L232) | 232 | `"            \"answer\": \"إجابة اختبار [المصدر 1]\","` | — |
| [SRC-3451CC474D-L000233](../../tests/test_api.py#L233) | 233 | `"            \"question\": question,"` | — |
| [SRC-3451CC474D-L000234](../../tests/test_api.py#L234) | 234 | `"            \"search_query\": question,"` | — |
| [SRC-3451CC474D-L000235](../../tests/test_api.py#L235) | 235 | `"            \"sources\": [{\"title\": \"مصدر\", \"url\": \"https://example.com\", \"snippet\": \"نص\", \"page_fetched\": False}],"` | — |
| [SRC-3451CC474D-L000236](../../tests/test_api.py#L236) | 236 | `"            \"used_language_model\": True,"` | — |
| [SRC-3451CC474D-L000237](../../tests/test_api.py#L237) | 237 | `"            \"used_web_search\": True,"` | — |
| [SRC-3451CC474D-L000238](../../tests/test_api.py#L238) | 238 | `"            \"warnings\": [],"` | — |
| [SRC-3451CC474D-L000239](../../tests/test_api.py#L239) | 239 | `"            \"kind\": \"web_research\","` | — |
| [SRC-3451CC474D-L000240](../../tests/test_api.py#L240) | 240 | `"        }"` | — |
| [SRC-3451CC474D-L000241](../../tests/test_api.py#L241) | 241 | `""` | — |
| [SRC-3451CC474D-L000242](../../tests/test_api.py#L242) | 242 | `"    monkeypatch.setattr(WebAgent, \"answer\", fake_answer)"` | — |
| [SRC-3451CC474D-L000243](../../tests/test_api.py#L243) | 243 | `"    status, response = request_json("` | — |
| [SRC-3451CC474D-L000244](../../tests/test_api.py#L244) | 244 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000245](../../tests/test_api.py#L245) | 245 | `"        \"/api/agent\","` | — |
| [SRC-3451CC474D-L000246](../../tests/test_api.py#L246) | 246 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000247](../../tests/test_api.py#L247) | 247 | `"        payload={\"question\": \"ابحث عن موضوع\", \"history\": []},"` | — |
| [SRC-3451CC474D-L000248](../../tests/test_api.py#L248) | 248 | `"    )"` | — |
| [SRC-3451CC474D-L000249](../../tests/test_api.py#L249) | 249 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000250](../../tests/test_api.py#L250) | 250 | `"    assert response[\"kind\"] == \"web_research\""` | — |
| [SRC-3451CC474D-L000251](../../tests/test_api.py#L251) | 251 | `"    assert response[\"sources\"][0][\"url\"] == \"https://example.com\""` | — |
| [SRC-3451CC474D-L000252](../../tests/test_api.py#L252) | 252 | `""` | — |
| [SRC-3451CC474D-L000253](../../tests/test_api.py#L253) | 253 | `""` | — |
| [SRC-3451CC474D-L000254](../../tests/test_api.py#L254) | 254 | `""` | — |
| [SRC-3451CC474D-L000255](../../tests/test_api.py#L255) | 255 | `"def test_live_diagnostics_endpoint_returns_report_without_secrets(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000256](../../tests/test_api.py#L256) | 256 | `"    from api.omarai import WebAgent"` | — |
| [SRC-3451CC474D-L000257](../../tests/test_api.py#L257) | 257 | `""` | — |
| [SRC-3451CC474D-L000258](../../tests/test_api.py#L258) | 258 | `"    def fake_diagnostics(self, test_model=True, test_social=False):"` | — |
| [SRC-3451CC474D-L000259](../../tests/test_api.py#L259) | 259 | `"        return {"` | — |
| [SRC-3451CC474D-L000260](../../tests/test_api.py#L260) | 260 | `"            \"overall_status\": \"passed\","` | — |
| [SRC-3451CC474D-L000261](../../tests/test_api.py#L261) | 261 | `"            \"checks\": {"` | — |
| [SRC-3451CC474D-L000262](../../tests/test_api.py#L262) | 262 | `"                \"web_search\": {\"status\": \"passed\", \"result_count\": 4},"` | — |
| [SRC-3451CC474D-L000263](../../tests/test_api.py#L263) | 263 | `"                \"language_model\": {\"status\": \"passed\", \"response_received\": True},"` | — |
| [SRC-3451CC474D-L000264](../../tests/test_api.py#L264) | 264 | `"                \"social_search\": {\"status\": \"skipped\"},"` | — |
| [SRC-3451CC474D-L000265](../../tests/test_api.py#L265) | 265 | `"            },"` | — |
| [SRC-3451CC474D-L000266](../../tests/test_api.py#L266) | 266 | `"            \"model_usage\": [{"` | — |
| [SRC-3451CC474D-L000267](../../tests/test_api.py#L267) | 267 | `"                \"requested_model\": \"google/gemma-4-31b-it:free\","` | — |
| [SRC-3451CC474D-L000268](../../tests/test_api.py#L268) | 268 | `"                \"used_model\": \"google/gemma-4-31b-it:free\","` | — |
| [SRC-3451CC474D-L000269](../../tests/test_api.py#L269) | 269 | `"                \"fallback_used\": \"false\","` | — |
| [SRC-3451CC474D-L000270](../../tests/test_api.py#L270) | 270 | `"            }],"` | — |
| [SRC-3451CC474D-L000271](../../tests/test_api.py#L271) | 271 | `"        }"` | — |
| [SRC-3451CC474D-L000272](../../tests/test_api.py#L272) | 272 | `""` | — |
| [SRC-3451CC474D-L000273](../../tests/test_api.py#L273) | 273 | `"    monkeypatch.setattr(WebAgent, \"diagnostics\", fake_diagnostics)"` | — |
| [SRC-3451CC474D-L000274](../../tests/test_api.py#L274) | 274 | `"    status, report = request_json("` | — |
| [SRC-3451CC474D-L000275](../../tests/test_api.py#L275) | 275 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000276](../../tests/test_api.py#L276) | 276 | `"        \"/api/diagnostics\","` | — |
| [SRC-3451CC474D-L000277](../../tests/test_api.py#L277) | 277 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000278](../../tests/test_api.py#L278) | 278 | `"        payload={\"test_model\": True, \"test_social\": False},"` | — |
| [SRC-3451CC474D-L000279](../../tests/test_api.py#L279) | 279 | `"    )"` | — |
| [SRC-3451CC474D-L000280](../../tests/test_api.py#L280) | 280 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000281](../../tests/test_api.py#L281) | 281 | `"    assert report[\"overall_status\"] == \"passed\""` | — |
| [SRC-3451CC474D-L000282](../../tests/test_api.py#L282) | 282 | `"    assert report[\"checks\"][\"web_search\"][\"result_count\"] == 4"` | — |
| [SRC-3451CC474D-L000283](../../tests/test_api.py#L283) | 283 | `"    assert \"api_key\" not in report"` | — |
| [SRC-3451CC474D-L000284](../../tests/test_api.py#L284) | 284 | `"    assert \"secret\" not in str(report)"` | — |
| [SRC-3451CC474D-L000285](../../tests/test_api.py#L285) | 285 | `""` | — |
| [SRC-3451CC474D-L000286](../../tests/test_api.py#L286) | 286 | `""` | — |
| [SRC-3451CC474D-L000287](../../tests/test_api.py#L287) | 287 | `"def test_diagnostics_endpoint_requires_boolean_options(local_api):"` | — |
| [SRC-3451CC474D-L000288](../../tests/test_api.py#L288) | 288 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000289](../../tests/test_api.py#L289) | 289 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000290](../../tests/test_api.py#L290) | 290 | `"        \"/api/diagnostics\","` | — |
| [SRC-3451CC474D-L000291](../../tests/test_api.py#L291) | 291 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000292](../../tests/test_api.py#L292) | 292 | `"        payload={\"test_model\": \"yes\", \"test_social\": False},"` | — |
| [SRC-3451CC474D-L000293](../../tests/test_api.py#L293) | 293 | `"    )"` | — |
| [SRC-3451CC474D-L000294](../../tests/test_api.py#L294) | 294 | `"    assert status == 400"` | — |
| [SRC-3451CC474D-L000295](../../tests/test_api.py#L295) | 295 | `"    assert \"booleans\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000296](../../tests/test_api.py#L296) | 296 | `""` | — |
| [SRC-3451CC474D-L000297](../../tests/test_api.py#L297) | 297 | `""` | — |
| [SRC-3451CC474D-L000298](../../tests/test_api.py#L298) | 298 | `""` | — |
| [SRC-3451CC474D-L000299](../../tests/test_api.py#L299) | 299 | `"def test_rate_limit_ignores_spoofed_forwarded_for_by_default(monkeypatch):"` | — |
| [SRC-3451CC474D-L000300](../../tests/test_api.py#L300) | 300 | `"    monkeypatch.delenv(\"OMARAI_TRUST_PROXY_HEADERS\", raising=False)"` | — |
| [SRC-3451CC474D-L000301](../../tests/test_api.py#L301) | 301 | `"    handler = SimpleNamespace("` | — |
| [SRC-3451CC474D-L000302](../../tests/test_api.py#L302) | 302 | `"        headers={\"X-Forwarded-For\": \"198.51.100.77, 203.0.113.10\"},"` | — |
| [SRC-3451CC474D-L000303](../../tests/test_api.py#L303) | 303 | `"        client_address=(\"192.0.2.44\", 12345),"` | — |
| [SRC-3451CC474D-L000304](../../tests/test_api.py#L304) | 304 | `"    )"` | — |
| [SRC-3451CC474D-L000305](../../tests/test_api.py#L305) | 305 | `"    assert Handler._rate_limit_client_key(handler) == \"192.0.2.44\""` | — |
| [SRC-3451CC474D-L000306](../../tests/test_api.py#L306) | 306 | `""` | — |
| [SRC-3451CC474D-L000307](../../tests/test_api.py#L307) | 307 | `""` | — |
| [SRC-3451CC474D-L000308](../../tests/test_api.py#L308) | 308 | `"def test_rate_limit_uses_rightmost_valid_proxy_ip_only_when_enabled(monkeypatch):"` | — |
| [SRC-3451CC474D-L000309](../../tests/test_api.py#L309) | 309 | `"    monkeypatch.setenv(\"OMARAI_TRUST_PROXY_HEADERS\", \"1\")"` | — |
| [SRC-3451CC474D-L000310](../../tests/test_api.py#L310) | 310 | `"    handler = SimpleNamespace("` | — |
| [SRC-3451CC474D-L000311](../../tests/test_api.py#L311) | 311 | `"        headers={\"X-Forwarded-For\": \"198.51.100.77, 203.0.113.10\"},"` | — |
| [SRC-3451CC474D-L000312](../../tests/test_api.py#L312) | 312 | `"        client_address=(\"192.0.2.44\", 12345),"` | — |
| [SRC-3451CC474D-L000313](../../tests/test_api.py#L313) | 313 | `"    )"` | — |
| [SRC-3451CC474D-L000314](../../tests/test_api.py#L314) | 314 | `"    assert Handler._rate_limit_client_key(handler) == \"203.0.113.10\""` | — |
| [SRC-3451CC474D-L000315](../../tests/test_api.py#L315) | 315 | `""` | — |
| [SRC-3451CC474D-L000316](../../tests/test_api.py#L316) | 316 | `""` | — |
| [SRC-3451CC474D-L000317](../../tests/test_api.py#L317) | 317 | `"def test_rate_limit_proxy_header_invalid_value_falls_back_to_peer_ip(monkeypatch):"` | — |
| [SRC-3451CC474D-L000318](../../tests/test_api.py#L318) | 318 | `"    monkeypatch.setenv(\"OMARAI_TRUST_PROXY_HEADERS\", \"1\")"` | — |
| [SRC-3451CC474D-L000319](../../tests/test_api.py#L319) | 319 | `"    handler = SimpleNamespace("` | — |
| [SRC-3451CC474D-L000320](../../tests/test_api.py#L320) | 320 | `"        headers={\"X-Forwarded-For\": \"198.51.100.77, not-an-ip\"},"` | — |
| [SRC-3451CC474D-L000321](../../tests/test_api.py#L321) | 321 | `"        client_address=(\"192.0.2.44\", 12345),"` | — |
| [SRC-3451CC474D-L000322](../../tests/test_api.py#L322) | 322 | `"    )"` | — |
| [SRC-3451CC474D-L000323](../../tests/test_api.py#L323) | 323 | `"    assert Handler._rate_limit_client_key(handler) == \"192.0.2.44\""` | — |
| [SRC-3451CC474D-L000324](../../tests/test_api.py#L324) | 324 | `""` | — |
| [SRC-3451CC474D-L000325](../../tests/test_api.py#L325) | 325 | `""` | — |
