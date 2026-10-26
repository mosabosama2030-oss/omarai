# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **030**
- سجلات الأسطر: **800**
- النطاق: SRC-01E35ABC46-L000100 إلى SRC-F725E90B2A-L000466
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-01E35ABC46 — [tests/test_research_guardrails.py](../../tests/test_research_guardrails.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-01E35ABC46-L000100](../../tests/test_research_guardrails.py#L100) | 100 | `"    rel = source_relevance_score(src, \"أسعار السيارات الكهربائية في مصر\")"` | — |
| [SRC-01E35ABC46-L000101](../../tests/test_research_guardrails.py#L101) | 101 | `"    assert rel[\"accepted\"] is False"` | — |
| [SRC-01E35ABC46-L000102](../../tests/test_research_guardrails.py#L102) | 102 | `""` | — |
| [SRC-01E35ABC46-L000103](../../tests/test_research_guardrails.py#L103) | 103 | `""` | — |
| [SRC-01E35ABC46-L000104](../../tests/test_research_guardrails.py#L104) | 104 | `"def test_relevance_keeps_official_despite_wording():"` | — |
| [SRC-01E35ABC46-L000105](../../tests/test_research_guardrails.py#L105) | 105 | `"    src = {"` | — |
| [SRC-01E35ABC46-L000106](../../tests/test_research_guardrails.py#L106) | 106 | `"        \"title\": \"Official statistical bulletin Q1\","` | — |
| [SRC-01E35ABC46-L000107](../../tests/test_research_guardrails.py#L107) | 107 | `"        \"url\": \"https://www.capmas.gov.eg/bulletin\","` | — |
| [SRC-01E35ABC46-L000108](../../tests/test_research_guardrails.py#L108) | 108 | `"        \"snippet\": \"National statistics release.\","` | — |
| [SRC-01E35ABC46-L000109](../../tests/test_research_guardrails.py#L109) | 109 | `"        \"domain\": \"capmas.gov.eg\","` | — |
| [SRC-01E35ABC46-L000110](../../tests/test_research_guardrails.py#L110) | 110 | `"        \"source_class\": \"government\","` | — |
| [SRC-01E35ABC46-L000111](../../tests/test_research_guardrails.py#L111) | 111 | `"        \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000112](../../tests/test_research_guardrails.py#L112) | 112 | `"    }"` | — |
| [SRC-01E35ABC46-L000113](../../tests/test_research_guardrails.py#L113) | 113 | `"    rel = source_relevance_score(src, \"أسعار السيارات الكهربائية في مصر\")"` | — |
| [SRC-01E35ABC46-L000114](../../tests/test_research_guardrails.py#L114) | 114 | `"    assert rel[\"accepted\"] is True"` | — |
| [SRC-01E35ABC46-L000115](../../tests/test_research_guardrails.py#L115) | 115 | `"    assert rel[\"reason\"] in {\"accepted\", \"kept_official_despite_low_overlap\"}"` | — |
| [SRC-01E35ABC46-L000116](../../tests/test_research_guardrails.py#L116) | 116 | `""` | — |
| [SRC-01E35ABC46-L000117](../../tests/test_research_guardrails.py#L117) | 117 | `""` | — |
| [SRC-01E35ABC46-L000118](../../tests/test_research_guardrails.py#L118) | 118 | `"def test_filter_deduplicates():"` | — |
| [SRC-01E35ABC46-L000119](../../tests/test_research_guardrails.py#L119) | 119 | `"    sources = ["` | — |
| [SRC-01E35ABC46-L000120](../../tests/test_research_guardrails.py#L120) | 120 | `"        {"` | — |
| [SRC-01E35ABC46-L000121](../../tests/test_research_guardrails.py#L121) | 121 | `"            \"title\": \"Same Article Title\","` | — |
| [SRC-01E35ABC46-L000122](../../tests/test_research_guardrails.py#L122) | 122 | `"            \"url\": \"https://a.example/1\","` | — |
| [SRC-01E35ABC46-L000123](../../tests/test_research_guardrails.py#L123) | 123 | `"            \"snippet\": \"electric vehicles Egypt market\","` | — |
| [SRC-01E35ABC46-L000124](../../tests/test_research_guardrails.py#L124) | 124 | `"            \"domain\": \"a.example\","` | — |
| [SRC-01E35ABC46-L000125](../../tests/test_research_guardrails.py#L125) | 125 | `"            \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000126](../../tests/test_research_guardrails.py#L126) | 126 | `"            \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000127](../../tests/test_research_guardrails.py#L127) | 127 | `"        },"` | — |
| [SRC-01E35ABC46-L000128](../../tests/test_research_guardrails.py#L128) | 128 | `"        {"` | — |
| [SRC-01E35ABC46-L000129](../../tests/test_research_guardrails.py#L129) | 129 | `"            \"title\": \"Same Article Title\","` | — |
| [SRC-01E35ABC46-L000130](../../tests/test_research_guardrails.py#L130) | 130 | `"            \"url\": \"https://a.example/1?utm=x\","` | — |
| [SRC-01E35ABC46-L000131](../../tests/test_research_guardrails.py#L131) | 131 | `"            \"snippet\": \"electric vehicles Egypt market again\","` | — |
| [SRC-01E35ABC46-L000132](../../tests/test_research_guardrails.py#L132) | 132 | `"            \"domain\": \"a.example\","` | — |
| [SRC-01E35ABC46-L000133](../../tests/test_research_guardrails.py#L133) | 133 | `"            \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000134](../../tests/test_research_guardrails.py#L134) | 134 | `"            \"providers\": [\"bing\"],"` | — |
| [SRC-01E35ABC46-L000135](../../tests/test_research_guardrails.py#L135) | 135 | `"        },"` | — |
| [SRC-01E35ABC46-L000136](../../tests/test_research_guardrails.py#L136) | 136 | `"    ]"` | — |
| [SRC-01E35ABC46-L000137](../../tests/test_research_guardrails.py#L137) | 137 | `"    kept, diag = filter_relevant_sources("` | — |
| [SRC-01E35ABC46-L000138](../../tests/test_research_guardrails.py#L138) | 138 | `"        sources, \"electric vehicles Egypt\", [\"electric vehicles Egypt\"]"` | — |
| [SRC-01E35ABC46-L000139](../../tests/test_research_guardrails.py#L139) | 139 | `"    )"` | — |
| [SRC-01E35ABC46-L000140](../../tests/test_research_guardrails.py#L140) | 140 | `"    assert len(kept) == 1"` | — |
| [SRC-01E35ABC46-L000141](../../tests/test_research_guardrails.py#L141) | 141 | `"    assert any(d[\"reason\"] == \"duplicate_title_domain\" for d in diag)"` | — |
| [SRC-01E35ABC46-L000142](../../tests/test_research_guardrails.py#L142) | 142 | `""` | — |
| [SRC-01E35ABC46-L000143](../../tests/test_research_guardrails.py#L143) | 143 | `""` | — |
| [SRC-01E35ABC46-L000144](../../tests/test_research_guardrails.py#L144) | 144 | `"def test_filter_empty_and_failed_extract():"` | — |
| [SRC-01E35ABC46-L000145](../../tests/test_research_guardrails.py#L145) | 145 | `"    kept, diag = filter_relevant_sources([], \"anything\")"` | — |
| [SRC-01E35ABC46-L000146](../../tests/test_research_guardrails.py#L146) | 146 | `"    assert kept == []"` | — |
| [SRC-01E35ABC46-L000147](../../tests/test_research_guardrails.py#L147) | 147 | `"    assert diag == []"` | — |
| [SRC-01E35ABC46-L000148](../../tests/test_research_guardrails.py#L148) | 148 | `"    src = {"` | — |
| [SRC-01E35ABC46-L000149](../../tests/test_research_guardrails.py#L149) | 149 | `"        \"title\": \"\","` | — |
| [SRC-01E35ABC46-L000150](../../tests/test_research_guardrails.py#L150) | 150 | `"        \"url\": \"https://example.com/x\","` | — |
| [SRC-01E35ABC46-L000151](../../tests/test_research_guardrails.py#L151) | 151 | `"        \"snippet\": \"\","` | — |
| [SRC-01E35ABC46-L000152](../../tests/test_research_guardrails.py#L152) | 152 | `"        \"page_text\": \"\","` | — |
| [SRC-01E35ABC46-L000153](../../tests/test_research_guardrails.py#L153) | 153 | `"        \"domain\": \"example.com\","` | — |
| [SRC-01E35ABC46-L000154](../../tests/test_research_guardrails.py#L154) | 154 | `"        \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000155](../../tests/test_research_guardrails.py#L155) | 155 | `"        \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000156](../../tests/test_research_guardrails.py#L156) | 156 | `"    }"` | — |
| [SRC-01E35ABC46-L000157](../../tests/test_research_guardrails.py#L157) | 157 | `"    _kept2, diag2 = filter_relevant_sources([src], \"unrelated pasta recipes\")"` | — |
| [SRC-01E35ABC46-L000158](../../tests/test_research_guardrails.py#L158) | 158 | `"    # May reject for low overlap"` | — |
| [SRC-01E35ABC46-L000159](../../tests/test_research_guardrails.py#L159) | 159 | `"    assert isinstance(diag2, list)"` | — |
| [SRC-01E35ABC46-L000160](../../tests/test_research_guardrails.py#L160) | 160 | `""` | — |
| [SRC-01E35ABC46-L000161](../../tests/test_research_guardrails.py#L161) | 161 | `""` | — |
| [SRC-01E35ABC46-L000162](../../tests/test_research_guardrails.py#L162) | 162 | `"# --- evidence status --------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000163](../../tests/test_research_guardrails.py#L163) | 163 | `""` | — |
| [SRC-01E35ABC46-L000164](../../tests/test_research_guardrails.py#L164) | 164 | `"def test_evidence_adequate():"` | — |
| [SRC-01E35ABC46-L000165](../../tests/test_research_guardrails.py#L165) | 165 | `"    sources = ["` | — |
| [SRC-01E35ABC46-L000166](../../tests/test_research_guardrails.py#L166) | 166 | `"        {\"url\": f\"https://a{i}.example/p\", \"domain\": f\"a{i}.example\","` | — |
| [SRC-01E35ABC46-L000167](../../tests/test_research_guardrails.py#L167) | 167 | `"         \"snippet\": \"content\", \"page_fetched\": True, \"source_class\": \"general\"}"` | — |
| [SRC-01E35ABC46-L000168](../../tests/test_research_guardrails.py#L168) | 168 | `"        for i in range(4)"` | — |
| [SRC-01E35ABC46-L000169](../../tests/test_research_guardrails.py#L169) | 169 | `"    ]"` | — |
| [SRC-01E35ABC46-L000170](../../tests/test_research_guardrails.py#L170) | 170 | `"    sources[0][\"source_class\"] = \"government\""` | — |
| [SRC-01E35ABC46-L000171](../../tests/test_research_guardrails.py#L171) | 171 | `"    decision = decide_evidence_status(sources, pages_read=2)"` | — |
| [SRC-01E35ABC46-L000172](../../tests/test_research_guardrails.py#L172) | 172 | `"    assert decision[\"evidence_status\"] == \"adequate\""` | — |
| [SRC-01E35ABC46-L000173](../../tests/test_research_guardrails.py#L173) | 173 | `"    assert decision[\"should_abstain\"] is False"` | — |
| [SRC-01E35ABC46-L000174](../../tests/test_research_guardrails.py#L174) | 174 | `""` | — |
| [SRC-01E35ABC46-L000175](../../tests/test_research_guardrails.py#L175) | 175 | `""` | — |
| [SRC-01E35ABC46-L000176](../../tests/test_research_guardrails.py#L176) | 176 | `"def test_evidence_insufficient_empty():"` | — |
| [SRC-01E35ABC46-L000177](../../tests/test_research_guardrails.py#L177) | 177 | `"    decision = decide_evidence_status([], search_attempted=True)"` | — |
| [SRC-01E35ABC46-L000178](../../tests/test_research_guardrails.py#L178) | 178 | `"    assert decision[\"evidence_status\"] == \"insufficient\""` | — |
| [SRC-01E35ABC46-L000179](../../tests/test_research_guardrails.py#L179) | 179 | `"    assert decision[\"should_abstain\"] is True"` | — |
| [SRC-01E35ABC46-L000180](../../tests/test_research_guardrails.py#L180) | 180 | `""` | — |
| [SRC-01E35ABC46-L000181](../../tests/test_research_guardrails.py#L181) | 181 | `""` | — |
| [SRC-01E35ABC46-L000182](../../tests/test_research_guardrails.py#L182) | 182 | `"def test_evidence_failed_provider():"` | — |
| [SRC-01E35ABC46-L000183](../../tests/test_research_guardrails.py#L183) | 183 | `"    decision = decide_evidence_status([], provider_failures=2, search_attempted=True)"` | — |
| [SRC-01E35ABC46-L000184](../../tests/test_research_guardrails.py#L184) | 184 | `"    assert decision[\"evidence_status\"] == \"failed\""` | — |
| [SRC-01E35ABC46-L000185](../../tests/test_research_guardrails.py#L185) | 185 | `"    assert decision[\"should_abstain\"] is True"` | — |
| [SRC-01E35ABC46-L000186](../../tests/test_research_guardrails.py#L186) | 186 | `""` | — |
| [SRC-01E35ABC46-L000187](../../tests/test_research_guardrails.py#L187) | 187 | `""` | — |
| [SRC-01E35ABC46-L000188](../../tests/test_research_guardrails.py#L188) | 188 | `"def test_evidence_partial_single_source():"` | — |
| [SRC-01E35ABC46-L000189](../../tests/test_research_guardrails.py#L189) | 189 | `"    sources = ["` | — |
| [SRC-01E35ABC46-L000190](../../tests/test_research_guardrails.py#L190) | 190 | `"        {\"url\": \"https://a.example/p\", \"domain\": \"a.example\","` | — |
| [SRC-01E35ABC46-L000191](../../tests/test_research_guardrails.py#L191) | 191 | `"         \"snippet\": \"some text\", \"page_fetched\": True, \"source_class\": \"general\"}"` | — |
| [SRC-01E35ABC46-L000192](../../tests/test_research_guardrails.py#L192) | 192 | `"    ]"` | — |
| [SRC-01E35ABC46-L000193](../../tests/test_research_guardrails.py#L193) | 193 | `"    decision = decide_evidence_status(sources, pages_read=1)"` | — |
| [SRC-01E35ABC46-L000194](../../tests/test_research_guardrails.py#L194) | 194 | `"    assert decision[\"evidence_status\"] == \"partial\""` | — |
| [SRC-01E35ABC46-L000195](../../tests/test_research_guardrails.py#L195) | 195 | `"    assert decision[\"should_abstain\"] is False"` | — |
## اختبارات

### FILE-2614DCB6FB — [tests/test_search_code.py](../../tests/test_search_code.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2614DCB6FB-L000001](../../tests/test_search_code.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-2614DCB6FB-L000002](../../tests/test_search_code.py#L2) | 2 | `""` | — |
| [SRC-2614DCB6FB-L000003](../../tests/test_search_code.py#L3) | 3 | `"import importlib.util"` | — |
| [SRC-2614DCB6FB-L000004](../../tests/test_search_code.py#L4) | 4 | `"import re"` | — |
| [SRC-2614DCB6FB-L000005](../../tests/test_search_code.py#L5) | 5 | `"import sys"` | — |
| [SRC-2614DCB6FB-L000006](../../tests/test_search_code.py#L6) | 6 | `"from pathlib import Path"` | — |
| [SRC-2614DCB6FB-L000007](../../tests/test_search_code.py#L7) | 7 | `""` | — |
| [SRC-2614DCB6FB-L000008](../../tests/test_search_code.py#L8) | 8 | `"SEARCH_PATH = Path(__file__).resolve().parents[1] / \"docs\" / \"search_code.py\""` | — |
| [SRC-2614DCB6FB-L000009](../../tests/test_search_code.py#L9) | 9 | `"SEARCH_SPEC = importlib.util.spec_from_file_location(\"omarai_search_code_for_tests\", SEARCH_PATH)"` | — |
| [SRC-2614DCB6FB-L000010](../../tests/test_search_code.py#L10) | 10 | `"assert SEARCH_SPEC is not None"` | — |
| [SRC-2614DCB6FB-L000011](../../tests/test_search_code.py#L11) | 11 | `"assert SEARCH_SPEC.loader is not None"` | — |
| [SRC-2614DCB6FB-L000012](../../tests/test_search_code.py#L12) | 12 | `"SEARCH = importlib.util.module_from_spec(SEARCH_SPEC)"` | — |
| [SRC-2614DCB6FB-L000013](../../tests/test_search_code.py#L13) | 13 | `"sys.modules[SEARCH_SPEC.name] = SEARCH"` | — |
| [SRC-2614DCB6FB-L000014](../../tests/test_search_code.py#L14) | 14 | `"SEARCH_SPEC.loader.exec_module(SEARCH)"` | — |
| [SRC-2614DCB6FB-L000015](../../tests/test_search_code.py#L15) | 15 | `""` | — |
| [SRC-2614DCB6FB-L000016](../../tests/test_search_code.py#L16) | 16 | `""` | — |
| [SRC-2614DCB6FB-L000017](../../tests/test_search_code.py#L17) | 17 | `"def test_search_returns_stable_file_line_and_source_link(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000018](../../tests/test_search_code.py#L18) | 18 | `"    \"\"\"Text search returns the exact file and 1-based line without network access.\"\"\""` | — |
| [SRC-2614DCB6FB-L000019](../../tests/test_search_code.py#L19) | 19 | `"    source = tmp_path / \"app.py\""` | — |
| [SRC-2614DCB6FB-L000020](../../tests/test_search_code.py#L20) | 20 | `"    source.write_text(\"first = 1\\nneedle = 2\\nlast = 3\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000021](../../tests/test_search_code.py#L21) | 21 | `""` | — |
| [SRC-2614DCB6FB-L000022](../../tests/test_search_code.py#L22) | 22 | `"    hits = SEARCH.search_repository(tmp_path, \"needle\")"` | — |
| [SRC-2614DCB6FB-L000023](../../tests/test_search_code.py#L23) | 23 | `""` | — |
| [SRC-2614DCB6FB-L000024](../../tests/test_search_code.py#L24) | 24 | `"    assert len(hits) == 1"` | — |
| [SRC-2614DCB6FB-L000025](../../tests/test_search_code.py#L25) | 25 | `"    assert hits[0].file == \"app.py\""` | — |
| [SRC-2614DCB6FB-L000026](../../tests/test_search_code.py#L26) | 26 | `"    assert hits[0].line == 2"` | — |
| [SRC-2614DCB6FB-L000027](../../tests/test_search_code.py#L27) | 27 | `"    assert \"needle = 2\" in hits[0].text"` | — |
| [SRC-2614DCB6FB-L000028](../../tests/test_search_code.py#L28) | 28 | `"    assert hits[0].link.endswith(\"/app.py#L2\")"` | — |
| [SRC-2614DCB6FB-L000029](../../tests/test_search_code.py#L29) | 29 | `""` | — |
| [SRC-2614DCB6FB-L000030](../../tests/test_search_code.py#L30) | 30 | `""` | — |
| [SRC-2614DCB6FB-L000031](../../tests/test_search_code.py#L31) | 31 | `"def test_search_supports_multiline_context_and_regex(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000032](../../tests/test_search_code.py#L32) | 32 | `"    \"\"\"The context argument returns the requested number of adjacent lines.\"\"\""` | — |
| [SRC-2614DCB6FB-L000033](../../tests/test_search_code.py#L33) | 33 | `"    source = tmp_path / \"app.py\""` | — |
| [SRC-2614DCB6FB-L000034](../../tests/test_search_code.py#L34) | 34 | `"    source.write_text(\"before one\\nbefore two\\nVALUE_42 = 7\\nafter one\\nafter two\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000035](../../tests/test_search_code.py#L35) | 35 | `""` | — |
| [SRC-2614DCB6FB-L000036](../../tests/test_search_code.py#L36) | 36 | `"    hits = SEARCH.search_repository("` | — |
| [SRC-2614DCB6FB-L000037](../../tests/test_search_code.py#L37) | 37 | `"        tmp_path, r\"VALUE_\\d+\", use_regex=True, context=2"` | — |
| [SRC-2614DCB6FB-L000038](../../tests/test_search_code.py#L38) | 38 | `"    )"` | — |
| [SRC-2614DCB6FB-L000039](../../tests/test_search_code.py#L39) | 39 | `""` | — |
| [SRC-2614DCB6FB-L000040](../../tests/test_search_code.py#L40) | 40 | `"    assert len(hits) == 1"` | — |
| [SRC-2614DCB6FB-L000041](../../tests/test_search_code.py#L41) | 41 | `"    assert hits[0].context_before.splitlines() == [\"before one\", \"before two\"]"` | — |
| [SRC-2614DCB6FB-L000042](../../tests/test_search_code.py#L42) | 42 | `"    assert hits[0].context_after.splitlines() == [\"after one\", \"after two\"]"` | — |
| [SRC-2614DCB6FB-L000043](../../tests/test_search_code.py#L43) | 43 | `""` | — |
| [SRC-2614DCB6FB-L000044](../../tests/test_search_code.py#L44) | 44 | `""` | — |
| [SRC-2614DCB6FB-L000045](../../tests/test_search_code.py#L45) | 45 | `"def test_search_excludes_common_secret_files_and_runtime_directories(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000046](../../tests/test_search_code.py#L46) | 46 | `"    \"\"\"Local searches skip common secret paths and binary/runtime data.\"\"\""` | — |
| [SRC-2614DCB6FB-L000047](../../tests/test_search_code.py#L47) | 47 | `"    (tmp_path / \"app.py\").write_text(\"safe_value = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000048](../../tests/test_search_code.py#L48) | 48 | `"    (tmp_path / \".env\").write_text(\"TOKEN=private-value\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000049](../../tests/test_search_code.py#L49) | 49 | `"    (tmp_path / \"credentials.json\").write_text('{\"token\":\"private-value\"}\\n', encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000050](../../tests/test_search_code.py#L50) | 50 | `"    aws_dir = tmp_path / \".aws\""` | — |
| [SRC-2614DCB6FB-L000051](../../tests/test_search_code.py#L51) | 51 | `"    aws_dir.mkdir()"` | — |
| [SRC-2614DCB6FB-L000052](../../tests/test_search_code.py#L52) | 52 | `"    (aws_dir / \"credentials\").write_text(\"token=private-value\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000053](../../tests/test_search_code.py#L53) | 53 | `"    data_dir = tmp_path / \"data\""` | — |
| [SRC-2614DCB6FB-L000054](../../tests/test_search_code.py#L54) | 54 | `"    data_dir.mkdir()"` | — |
| [SRC-2614DCB6FB-L000055](../../tests/test_search_code.py#L55) | 55 | `"    (data_dir / \"records.sqlite3\").write_bytes(b\"database-token\")"` | — |
| [SRC-2614DCB6FB-L000056](../../tests/test_search_code.py#L56) | 56 | `"    (tmp_path / \"credentials.example\").write_text(\"TOKEN=replace-me\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000057](../../tests/test_search_code.py#L57) | 57 | `""` | — |
| [SRC-2614DCB6FB-L000058](../../tests/test_search_code.py#L58) | 58 | `"    hits = SEARCH.search_repository(tmp_path, \"private-value\")"` | — |
| [SRC-2614DCB6FB-L000059](../../tests/test_search_code.py#L59) | 59 | `"    safe_example = SEARCH.search_repository(tmp_path, \"replace-me\")"` | — |
| [SRC-2614DCB6FB-L000060](../../tests/test_search_code.py#L60) | 60 | `""` | — |
| [SRC-2614DCB6FB-L000061](../../tests/test_search_code.py#L61) | 61 | `"    assert hits == []"` | — |
| [SRC-2614DCB6FB-L000062](../../tests/test_search_code.py#L62) | 62 | `"    assert len(safe_example) == 1"` | — |
| [SRC-2614DCB6FB-L000063](../../tests/test_search_code.py#L63) | 63 | `"    assert safe_example[0].file == \"credentials.example\""` | — |
| [SRC-2614DCB6FB-L000064](../../tests/test_search_code.py#L64) | 64 | `""` | — |
| [SRC-2614DCB6FB-L000065](../../tests/test_search_code.py#L65) | 65 | `""` | — |
| [SRC-2614DCB6FB-L000066](../../tests/test_search_code.py#L66) | 66 | `"def test_search_validates_query_limits_and_reports_invalid_regex(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000067](../../tests/test_search_code.py#L67) | 67 | `"    \"\"\"Invalid search controls fail clearly instead of silently returning confusing results.\"\"\""` | — |
| [SRC-2614DCB6FB-L000068](../../tests/test_search_code.py#L68) | 68 | `"    try:"` | — |
| [SRC-2614DCB6FB-L000069](../../tests/test_search_code.py#L69) | 69 | `"        SEARCH.search_repository(tmp_path, \"\")"` | — |
| [SRC-2614DCB6FB-L000070](../../tests/test_search_code.py#L70) | 70 | `"    except ValueError as exc:"` | — |
| [SRC-2614DCB6FB-L000071](../../tests/test_search_code.py#L71) | 71 | `"        assert \"فارغ\" in str(exc)"` | — |
| [SRC-2614DCB6FB-L000072](../../tests/test_search_code.py#L72) | 72 | `"    else:"` | — |
| [SRC-2614DCB6FB-L000073](../../tests/test_search_code.py#L73) | 73 | `"        raise AssertionError(\"An empty search query should be rejected.\")"` | — |
| [SRC-2614DCB6FB-L000074](../../tests/test_search_code.py#L74) | 74 | `""` | — |
| [SRC-2614DCB6FB-L000075](../../tests/test_search_code.py#L75) | 75 | `"    for kwargs in ({\"max_results\": 0}, {\"context\": -1}):"` | — |
| [SRC-2614DCB6FB-L000076](../../tests/test_search_code.py#L76) | 76 | `"        try:"` | — |
| [SRC-2614DCB6FB-L000077](../../tests/test_search_code.py#L77) | 77 | `"            SEARCH.search_repository(tmp_path, \"needle\", **kwargs)"` | — |
| [SRC-2614DCB6FB-L000078](../../tests/test_search_code.py#L78) | 78 | `"        except ValueError:"` | — |
| [SRC-2614DCB6FB-L000079](../../tests/test_search_code.py#L79) | 79 | `"            continue"` | — |
| [SRC-2614DCB6FB-L000080](../../tests/test_search_code.py#L80) | 80 | `"        raise AssertionError(f\"Invalid search limits should be rejected: {kwargs}\")"` | — |
| [SRC-2614DCB6FB-L000081](../../tests/test_search_code.py#L81) | 81 | `""` | — |
| [SRC-2614DCB6FB-L000082](../../tests/test_search_code.py#L82) | 82 | `"    try:"` | — |
| [SRC-2614DCB6FB-L000083](../../tests/test_search_code.py#L83) | 83 | `"        SEARCH.search_repository(tmp_path, \"(\", use_regex=True)"` | — |
| [SRC-2614DCB6FB-L000084](../../tests/test_search_code.py#L84) | 84 | `"    except re.error:"` | — |
| [SRC-2614DCB6FB-L000085](../../tests/test_search_code.py#L85) | 85 | `"        pass"` | — |
| [SRC-2614DCB6FB-L000086](../../tests/test_search_code.py#L86) | 86 | `"    else:"` | — |
| [SRC-2614DCB6FB-L000087](../../tests/test_search_code.py#L87) | 87 | `"        raise AssertionError(\"An invalid regular expression should be rejected.\")"` | — |
| [SRC-2614DCB6FB-L000088](../../tests/test_search_code.py#L88) | 88 | `""` | — |
| [SRC-2614DCB6FB-L000089](../../tests/test_search_code.py#L89) | 89 | `"def test_search_links_use_the_requested_revision_not_main(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000090](../../tests/test_search_code.py#L90) | 90 | `"    source = tmp_path / \"app.py\""` | — |
| [SRC-2614DCB6FB-L000091](../../tests/test_search_code.py#L91) | 91 | `"    source.write_text(\"needle = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000092](../../tests/test_search_code.py#L92) | 92 | `""` | — |
| [SRC-2614DCB6FB-L000093](../../tests/test_search_code.py#L93) | 93 | `"    hits = SEARCH.search_repository("` | — |
| [SRC-2614DCB6FB-L000094](../../tests/test_search_code.py#L94) | 94 | `"        tmp_path, \"needle\", repository_ref=\"fix/review-branch\""` | — |
| [SRC-2614DCB6FB-L000095](../../tests/test_search_code.py#L95) | 95 | `"    )"` | — |
| [SRC-2614DCB6FB-L000096](../../tests/test_search_code.py#L96) | 96 | `""` | — |
| [SRC-2614DCB6FB-L000097](../../tests/test_search_code.py#L97) | 97 | `"    assert len(hits) == 1"` | — |
| [SRC-2614DCB6FB-L000098](../../tests/test_search_code.py#L98) | 98 | `"    assert hits[0].link == ("` | — |
| [SRC-2614DCB6FB-L000099](../../tests/test_search_code.py#L99) | 99 | `"        \"https://github.com/mosabosama2030-oss/omarai/\""` | — |
| [SRC-2614DCB6FB-L000100](../../tests/test_search_code.py#L100) | 100 | `"        \"blob/fix/review-branch/app.py#L1\""` | — |
| [SRC-2614DCB6FB-L000101](../../tests/test_search_code.py#L101) | 101 | `"    )"` | — |
| [SRC-2614DCB6FB-L000102](../../tests/test_search_code.py#L102) | 102 | `""` | — |
| [SRC-2614DCB6FB-L000103](../../tests/test_search_code.py#L103) | 103 | `""` | — |
| [SRC-2614DCB6FB-L000104](../../tests/test_search_code.py#L104) | 104 | `"def test_default_repository_ref_prefers_explicit_environment_override("` | — |
| [SRC-2614DCB6FB-L000105](../../tests/test_search_code.py#L105) | 105 | `"    monkeypatch, tmp_path: Path"` | — |
| [SRC-2614DCB6FB-L000106](../../tests/test_search_code.py#L106) | 106 | `") -> None:"` | — |
| [SRC-2614DCB6FB-L000107](../../tests/test_search_code.py#L107) | 107 | `"    monkeypatch.setenv(\"OMARAI_GITHUB_REF\", \"feature/current-review\")"` | — |
| [SRC-2614DCB6FB-L000108](../../tests/test_search_code.py#L108) | 108 | `"    monkeypatch.setenv(\"GITHUB_SHA\", \"a\" * 40)"` | — |
| [SRC-2614DCB6FB-L000109](../../tests/test_search_code.py#L109) | 109 | `""` | — |
| [SRC-2614DCB6FB-L000110](../../tests/test_search_code.py#L110) | 110 | `"    assert SEARCH.default_repository_ref(tmp_path) == \"feature/current-review\""` | — |
| [SRC-2614DCB6FB-L000111](../../tests/test_search_code.py#L111) | 111 | `""` | — |
| [SRC-2614DCB6FB-L000112](../../tests/test_search_code.py#L112) | 112 | `""` | — |
| [SRC-2614DCB6FB-L000113](../../tests/test_search_code.py#L113) | 113 | `"def test_default_repository_ref_uses_valid_ci_sha("` | — |
| [SRC-2614DCB6FB-L000114](../../tests/test_search_code.py#L114) | 114 | `"    monkeypatch, tmp_path: Path"` | — |
| [SRC-2614DCB6FB-L000115](../../tests/test_search_code.py#L115) | 115 | `") -> None:"` | — |
| [SRC-2614DCB6FB-L000116](../../tests/test_search_code.py#L116) | 116 | `"    monkeypatch.delenv(\"OMARAI_GITHUB_REF\", raising=False)"` | — |
| [SRC-2614DCB6FB-L000117](../../tests/test_search_code.py#L117) | 117 | `"    monkeypatch.setenv(\"GITHUB_SHA\", \"B\" * 40)"` | — |
| [SRC-2614DCB6FB-L000118](../../tests/test_search_code.py#L118) | 118 | `""` | — |
| [SRC-2614DCB6FB-L000119](../../tests/test_search_code.py#L119) | 119 | `"    assert SEARCH.default_repository_ref(tmp_path) == \"b\" * 40"` | — |
| [SRC-2614DCB6FB-L000120](../../tests/test_search_code.py#L120) | 120 | `""` | — |
| [SRC-2614DCB6FB-L000121](../../tests/test_search_code.py#L121) | 121 | `"def test_cli_uses_explicit_ref_for_source_links(tmp_path: Path, capsys) -> None:"` | — |
| [SRC-2614DCB6FB-L000122](../../tests/test_search_code.py#L122) | 122 | `"    source = tmp_path / \"app.py\""` | — |
| [SRC-2614DCB6FB-L000123](../../tests/test_search_code.py#L123) | 123 | `"    source.write_text(\"needle = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000124](../../tests/test_search_code.py#L124) | 124 | `""` | — |
| [SRC-2614DCB6FB-L000125](../../tests/test_search_code.py#L125) | 125 | `"    exit_code = SEARCH.main(["` | — |
| [SRC-2614DCB6FB-L000126](../../tests/test_search_code.py#L126) | 126 | `"        \"needle\", \"--root\", str(tmp_path), \"--ref\", \"fix/cli-review\""` | — |
| [SRC-2614DCB6FB-L000127](../../tests/test_search_code.py#L127) | 127 | `"    ])"` | — |
| [SRC-2614DCB6FB-L000128](../../tests/test_search_code.py#L128) | 128 | `""` | — |
| [SRC-2614DCB6FB-L000129](../../tests/test_search_code.py#L129) | 129 | `"    output = capsys.readouterr().out"` | — |
| [SRC-2614DCB6FB-L000130](../../tests/test_search_code.py#L130) | 130 | `"    assert exit_code == 0"` | — |
| [SRC-2614DCB6FB-L000131](../../tests/test_search_code.py#L131) | 131 | `"    assert \"blob/fix/cli-review/app.py#L1\" in output"` | — |
| [SRC-2614DCB6FB-L000132](../../tests/test_search_code.py#L132) | 132 | `"    assert \"blob/main/app.py#L1\" not in output"` | — |
| [SRC-2614DCB6FB-L000133](../../tests/test_search_code.py#L133) | 133 | `""` | — |
## اختبارات

### FILE-1C0D3D1206 — [tests/test_sqlite_backup_restore.py](../../tests/test_sqlite_backup_restore.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1C0D3D1206-L000001](../../tests/test_sqlite_backup_restore.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-1C0D3D1206-L000002](../../tests/test_sqlite_backup_restore.py#L2) | 2 | `""` | — |
| [SRC-1C0D3D1206-L000003](../../tests/test_sqlite_backup_restore.py#L3) | 3 | `"import sqlite3"` | — |
| [SRC-1C0D3D1206-L000004](../../tests/test_sqlite_backup_restore.py#L4) | 4 | `""` | — |
| [SRC-1C0D3D1206-L000005](../../tests/test_sqlite_backup_restore.py#L5) | 5 | `"import pytest"` | — |
| [SRC-1C0D3D1206-L000006](../../tests/test_sqlite_backup_restore.py#L6) | 6 | `""` | — |
| [SRC-1C0D3D1206-L000007](../../tests/test_sqlite_backup_restore.py#L7) | 7 | `"from agents.omarai import LeadStore"` | — |
| [SRC-1C0D3D1206-L000008](../../tests/test_sqlite_backup_restore.py#L8) | 8 | `"from scripts.sqlite_backup_restore import BackupError, backup_database, restore_database"` | — |
| [SRC-1C0D3D1206-L000009](../../tests/test_sqlite_backup_restore.py#L9) | 9 | `""` | — |
| [SRC-1C0D3D1206-L000010](../../tests/test_sqlite_backup_restore.py#L10) | 10 | `""` | — |
| [SRC-1C0D3D1206-L000011](../../tests/test_sqlite_backup_restore.py#L11) | 11 | `"def test_backup_and_restore_preserve_omarai_leads(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000012](../../tests/test_sqlite_backup_restore.py#L12) | 12 | `"    source_path = tmp_path / \"live.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000013](../../tests/test_sqlite_backup_restore.py#L13) | 13 | `"    source = LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000014](../../tests/test_sqlite_backup_restore.py#L14) | 14 | `"    first, created_first = source.add("` | — |
| [SRC-1C0D3D1206-L000015](../../tests/test_sqlite_backup_restore.py#L15) | 15 | `"        \"بدور على شقة في التجمع وممكن معاينة\","` | — |
| [SRC-1C0D3D1206-L000016](../../tests/test_sqlite_backup_restore.py#L16) | 16 | `"        \"https://example.com/posts/1\","` | — |
| [SRC-1C0D3D1206-L000017](../../tests/test_sqlite_backup_restore.py#L17) | 17 | `"        platform=\"manual\","` | — |
| [SRC-1C0D3D1206-L000018](../../tests/test_sqlite_backup_restore.py#L18) | 18 | `"        note=\"سجل اختبار أول\","` | — |
| [SRC-1C0D3D1206-L000019](../../tests/test_sqlite_backup_restore.py#L19) | 19 | `"    )"` | — |
| [SRC-1C0D3D1206-L000020](../../tests/test_sqlite_backup_restore.py#L20) | 20 | `"    second, created_second = source.add("` | — |
| [SRC-1C0D3D1206-L000021](../../tests/test_sqlite_backup_restore.py#L21) | 21 | `"        \"محتاج شقة للإيجار الشهر القادم\","` | — |
| [SRC-1C0D3D1206-L000022](../../tests/test_sqlite_backup_restore.py#L22) | 22 | `"        \"https://example.com/posts/2\","` | — |
| [SRC-1C0D3D1206-L000023](../../tests/test_sqlite_backup_restore.py#L23) | 23 | `"        platform=\"manual\","` | — |
| [SRC-1C0D3D1206-L000024](../../tests/test_sqlite_backup_restore.py#L24) | 24 | `"        note=\"سجل اختبار ثان\","` | — |
| [SRC-1C0D3D1206-L000025](../../tests/test_sqlite_backup_restore.py#L25) | 25 | `"    )"` | — |
| [SRC-1C0D3D1206-L000026](../../tests/test_sqlite_backup_restore.py#L26) | 26 | `"    assert created_first and created_second"` | — |
| [SRC-1C0D3D1206-L000027](../../tests/test_sqlite_backup_restore.py#L27) | 27 | `"    source.update_status(first[\"id\"], \"qualified\")"` | — |
| [SRC-1C0D3D1206-L000028](../../tests/test_sqlite_backup_restore.py#L28) | 28 | `""` | — |
| [SRC-1C0D3D1206-L000029](../../tests/test_sqlite_backup_restore.py#L29) | 29 | `"    snapshot_path = tmp_path / \"backups\" / \"snapshot.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000030](../../tests/test_sqlite_backup_restore.py#L30) | 30 | `"    backup_report = backup_database(source_path, snapshot_path)"` | — |
| [SRC-1C0D3D1206-L000031](../../tests/test_sqlite_backup_restore.py#L31) | 31 | `"    assert backup_report[\"result\"] == \"passed\""` | — |
| [SRC-1C0D3D1206-L000032](../../tests/test_sqlite_backup_restore.py#L32) | 32 | `"    assert backup_report[\"integrity_check\"] == \"ok\""` | — |
| [SRC-1C0D3D1206-L000033](../../tests/test_sqlite_backup_restore.py#L33) | 33 | `"    assert backup_report[\"lead_count\"] == 2"` | — |
| [SRC-1C0D3D1206-L000034](../../tests/test_sqlite_backup_restore.py#L34) | 34 | `"    assert backup_report[\"overwrite\"] is False"` | — |
| [SRC-1C0D3D1206-L000035](../../tests/test_sqlite_backup_restore.py#L35) | 35 | `""` | — |
| [SRC-1C0D3D1206-L000036](../../tests/test_sqlite_backup_restore.py#L36) | 36 | `"    restored_path = tmp_path / \"restored\" / \"restored.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000037](../../tests/test_sqlite_backup_restore.py#L37) | 37 | `"    restore_report = restore_database(snapshot_path, restored_path)"` | — |
| [SRC-1C0D3D1206-L000038](../../tests/test_sqlite_backup_restore.py#L38) | 38 | `"    assert restore_report[\"result\"] == \"passed\""` | — |
| [SRC-1C0D3D1206-L000039](../../tests/test_sqlite_backup_restore.py#L39) | 39 | `"    assert restore_report[\"integrity_check\"] == \"ok\""` | — |
| [SRC-1C0D3D1206-L000040](../../tests/test_sqlite_backup_restore.py#L40) | 40 | `"    assert restore_report[\"lead_count\"] == 2"` | — |
| [SRC-1C0D3D1206-L000041](../../tests/test_sqlite_backup_restore.py#L41) | 41 | `""` | — |
| [SRC-1C0D3D1206-L000042](../../tests/test_sqlite_backup_restore.py#L42) | 42 | `"    restored = LeadStore(restored_path)"` | — |
| [SRC-1C0D3D1206-L000043](../../tests/test_sqlite_backup_restore.py#L43) | 43 | `"    original_rows = {row[\"id\"]: row for row in source.list(limit=500)}"` | — |
| [SRC-1C0D3D1206-L000044](../../tests/test_sqlite_backup_restore.py#L44) | 44 | `"    restored_rows = {row[\"id\"]: row for row in restored.list(limit=500)}"` | — |
| [SRC-1C0D3D1206-L000045](../../tests/test_sqlite_backup_restore.py#L45) | 45 | `"    assert restored_rows == original_rows"` | — |
| [SRC-1C0D3D1206-L000046](../../tests/test_sqlite_backup_restore.py#L46) | 46 | `"    assert restored_rows[first[\"id\"]][\"status\"] == \"qualified\""` | — |
| [SRC-1C0D3D1206-L000047](../../tests/test_sqlite_backup_restore.py#L47) | 47 | `"    assert second[\"id\"] in restored_rows"` | — |
| [SRC-1C0D3D1206-L000048](../../tests/test_sqlite_backup_restore.py#L48) | 48 | `""` | — |
| [SRC-1C0D3D1206-L000049](../../tests/test_sqlite_backup_restore.py#L49) | 49 | `""` | — |
| [SRC-1C0D3D1206-L000050](../../tests/test_sqlite_backup_restore.py#L50) | 50 | `"def test_backup_never_overwrites_an_existing_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000051](../../tests/test_sqlite_backup_restore.py#L51) | 51 | `"    source_path = tmp_path / \"source.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000052](../../tests/test_sqlite_backup_restore.py#L52) | 52 | `"    LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000053](../../tests/test_sqlite_backup_restore.py#L53) | 53 | `"    destination = tmp_path / \"keep-me.txt\""` | — |
| [SRC-1C0D3D1206-L000054](../../tests/test_sqlite_backup_restore.py#L54) | 54 | `"    destination.write_text(\"do not overwrite\", encoding=\"utf-8\")"` | — |
| [SRC-1C0D3D1206-L000055](../../tests/test_sqlite_backup_restore.py#L55) | 55 | `""` | — |
| [SRC-1C0D3D1206-L000056](../../tests/test_sqlite_backup_restore.py#L56) | 56 | `"    with pytest.raises(FileExistsError):"` | — |
| [SRC-1C0D3D1206-L000057](../../tests/test_sqlite_backup_restore.py#L57) | 57 | `"        backup_database(source_path, destination)"` | — |
| [SRC-1C0D3D1206-L000058](../../tests/test_sqlite_backup_restore.py#L58) | 58 | `""` | — |
| [SRC-1C0D3D1206-L000059](../../tests/test_sqlite_backup_restore.py#L59) | 59 | `"    assert destination.read_text(encoding=\"utf-8\") == \"do not overwrite\""` | — |
| [SRC-1C0D3D1206-L000060](../../tests/test_sqlite_backup_restore.py#L60) | 60 | `""` | — |
| [SRC-1C0D3D1206-L000061](../../tests/test_sqlite_backup_restore.py#L61) | 61 | `""` | — |
| [SRC-1C0D3D1206-L000062](../../tests/test_sqlite_backup_restore.py#L62) | 62 | `"def test_backup_rejects_non_omarai_sqlite_database_without_leaving_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000063](../../tests/test_sqlite_backup_restore.py#L63) | 63 | `"    source_path = tmp_path / \"unrelated.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000064](../../tests/test_sqlite_backup_restore.py#L64) | 64 | `"    with sqlite3.connect(source_path) as db:"` | — |
| [SRC-1C0D3D1206-L000065](../../tests/test_sqlite_backup_restore.py#L65) | 65 | `"        db.execute(\"CREATE TABLE unrelated (value TEXT)\")"` | — |
| [SRC-1C0D3D1206-L000066](../../tests/test_sqlite_backup_restore.py#L66) | 66 | `""` | — |
| [SRC-1C0D3D1206-L000067](../../tests/test_sqlite_backup_restore.py#L67) | 67 | `"    destination = tmp_path / \"should-not-exist.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000068](../../tests/test_sqlite_backup_restore.py#L68) | 68 | `"    with pytest.raises(BackupError, match=\"not an Omarai leads database\"):"` | — |
| [SRC-1C0D3D1206-L000069](../../tests/test_sqlite_backup_restore.py#L69) | 69 | `"        backup_database(source_path, destination)"` | — |
| [SRC-1C0D3D1206-L000070](../../tests/test_sqlite_backup_restore.py#L70) | 70 | `""` | — |
| [SRC-1C0D3D1206-L000071](../../tests/test_sqlite_backup_restore.py#L71) | 71 | `"    assert not destination.exists()"` | — |
| [SRC-1C0D3D1206-L000072](../../tests/test_sqlite_backup_restore.py#L72) | 72 | `""` | — |
| [SRC-1C0D3D1206-L000073](../../tests/test_sqlite_backup_restore.py#L73) | 73 | `""` | — |
| [SRC-1C0D3D1206-L000074](../../tests/test_sqlite_backup_restore.py#L74) | 74 | `"def test_backup_rejects_same_source_and_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000075](../../tests/test_sqlite_backup_restore.py#L75) | 75 | `"    source_path = tmp_path / \"source.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000076](../../tests/test_sqlite_backup_restore.py#L76) | 76 | `"    LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000077](../../tests/test_sqlite_backup_restore.py#L77) | 77 | `""` | — |
| [SRC-1C0D3D1206-L000078](../../tests/test_sqlite_backup_restore.py#L78) | 78 | `"    with pytest.raises(BackupError, match=\"different paths\"):"` | — |
| [SRC-1C0D3D1206-L000079](../../tests/test_sqlite_backup_restore.py#L79) | 79 | `"        backup_database(source_path, source_path)"` | — |
| [SRC-1C0D3D1206-L000080](../../tests/test_sqlite_backup_restore.py#L80) | 80 | `""` | — |
| [SRC-1C0D3D1206-L000081](../../tests/test_sqlite_backup_restore.py#L81) | 81 | `""` | — |
| [SRC-1C0D3D1206-L000082](../../tests/test_sqlite_backup_restore.py#L82) | 82 | `"def test_restore_rejects_corrupt_backup_without_overwriting_source(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000083](../../tests/test_sqlite_backup_restore.py#L83) | 83 | `"    backup_path = tmp_path / \"corrupt.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000084](../../tests/test_sqlite_backup_restore.py#L84) | 84 | `"    backup_path.write_bytes(b\"not a sqlite database\")"` | — |
| [SRC-1C0D3D1206-L000085](../../tests/test_sqlite_backup_restore.py#L85) | 85 | `"    destination = tmp_path / \"restore.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000086](../../tests/test_sqlite_backup_restore.py#L86) | 86 | `""` | — |
| [SRC-1C0D3D1206-L000087](../../tests/test_sqlite_backup_restore.py#L87) | 87 | `"    with pytest.raises(BackupError):"` | — |
| [SRC-1C0D3D1206-L000088](../../tests/test_sqlite_backup_restore.py#L88) | 88 | `"        restore_database(backup_path, destination)"` | — |
| [SRC-1C0D3D1206-L000089](../../tests/test_sqlite_backup_restore.py#L89) | 89 | `""` | — |
| [SRC-1C0D3D1206-L000090](../../tests/test_sqlite_backup_restore.py#L90) | 90 | `"    assert backup_path.read_bytes() == b\"not a sqlite database\""` | — |
| [SRC-1C0D3D1206-L000091](../../tests/test_sqlite_backup_restore.py#L91) | 91 | `"    assert not destination.exists()"` | — |
| [SRC-1C0D3D1206-L000092](../../tests/test_sqlite_backup_restore.py#L92) | 92 | `""` | — |
| [SRC-1C0D3D1206-L000093](../../tests/test_sqlite_backup_restore.py#L93) | 93 | `"def test_backup_rejects_dangling_symlink_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000094](../../tests/test_sqlite_backup_restore.py#L94) | 94 | `"    source_path = tmp_path / \"source.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000095](../../tests/test_sqlite_backup_restore.py#L95) | 95 | `"    LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000096](../../tests/test_sqlite_backup_restore.py#L96) | 96 | `"    target_path = tmp_path / \"target.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000097](../../tests/test_sqlite_backup_restore.py#L97) | 97 | `"    destination_link = tmp_path / \"backup-link.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000098](../../tests/test_sqlite_backup_restore.py#L98) | 98 | `"    destination_link.symlink_to(target_path)"` | — |
| [SRC-1C0D3D1206-L000099](../../tests/test_sqlite_backup_restore.py#L99) | 99 | `""` | — |
| [SRC-1C0D3D1206-L000100](../../tests/test_sqlite_backup_restore.py#L100) | 100 | `"    with pytest.raises(FileExistsError):"` | — |
| [SRC-1C0D3D1206-L000101](../../tests/test_sqlite_backup_restore.py#L101) | 101 | `"        backup_database(source_path, destination_link)"` | — |
| [SRC-1C0D3D1206-L000102](../../tests/test_sqlite_backup_restore.py#L102) | 102 | `""` | — |
| [SRC-1C0D3D1206-L000103](../../tests/test_sqlite_backup_restore.py#L103) | 103 | `"    assert destination_link.is_symlink()"` | — |
| [SRC-1C0D3D1206-L000104](../../tests/test_sqlite_backup_restore.py#L104) | 104 | `"    assert not target_path.exists()"` | — |
| [SRC-1C0D3D1206-L000105](../../tests/test_sqlite_backup_restore.py#L105) | 105 | `""` | — |
## اختبارات

### FILE-F725E90B2A — [tests/test_web_agent.py](../../tests/test_web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-F725E90B2A-L000001](../../tests/test_web_agent.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-F725E90B2A-L000002](../../tests/test_web_agent.py#L2) | 2 | `""` | — |
| [SRC-F725E90B2A-L000003](../../tests/test_web_agent.py#L3) | 3 | `"from pathlib import Path"` | — |
| [SRC-F725E90B2A-L000004](../../tests/test_web_agent.py#L4) | 4 | `""` | — |
| [SRC-F725E90B2A-L000005](../../tests/test_web_agent.py#L5) | 5 | `"import pytest"` | — |
| [SRC-F725E90B2A-L000006](../../tests/test_web_agent.py#L6) | 6 | `""` | — |
| [SRC-F725E90B2A-L000007](../../tests/test_web_agent.py#L7) | 7 | `"from agents.research import compact_search_query"` | — |
| [SRC-F725E90B2A-L000008](../../tests/test_web_agent.py#L8) | 8 | `"from agents.web_agent import ("` | — |
| [SRC-F725E90B2A-L000009](../../tests/test_web_agent.py#L9) | 9 | `"    WebAgent,"` | — |
| [SRC-F725E90B2A-L000010](../../tests/test_web_agent.py#L10) | 10 | `"    _normalize_search_query,"` | — |
| [SRC-F725E90B2A-L000011](../../tests/test_web_agent.py#L11) | 11 | `"    _public_http_url,"` | — |
| [SRC-F725E90B2A-L000012](../../tests/test_web_agent.py#L12) | 12 | `"    _relevance_ratio,"` | — |
| [SRC-F725E90B2A-L000013](../../tests/test_web_agent.py#L13) | 13 | `")"` | — |
| [SRC-F725E90B2A-L000014](../../tests/test_web_agent.py#L14) | 14 | `""` | — |
| [SRC-F725E90B2A-L000015](../../tests/test_web_agent.py#L15) | 15 | `""` | — |
| [SRC-F725E90B2A-L000016](../../tests/test_web_agent.py#L16) | 16 | `"def sample_source(index=0):"` | — |
| [SRC-F725E90B2A-L000017](../../tests/test_web_agent.py#L17) | 17 | `"    domain = \"example.com\" if index == 0 else \"example.net\""` | — |
| [SRC-F725E90B2A-L000018](../../tests/test_web_agent.py#L18) | 18 | `"    return {"` | — |
| [SRC-F725E90B2A-L000019](../../tests/test_web_agent.py#L19) | 19 | `"        \"title\": \"مقالة عن التقنية\","` | — |
| [SRC-F725E90B2A-L000020](../../tests/test_web_agent.py#L20) | 20 | `"        \"url\": f\"https://{domain}/research\","` | — |
| [SRC-F725E90B2A-L000021](../../tests/test_web_agent.py#L21) | 21 | `"        \"snippet\": \"يشرح هذا المصدر التقنية وسبب المقارنة.\","` | — |
| [SRC-F725E90B2A-L000022](../../tests/test_web_agent.py#L22) | 22 | `"        \"page_text\": \"نص مستخرج من الصفحة يشرح التقنية وأسباب المقارنة.\","` | — |
| [SRC-F725E90B2A-L000023](../../tests/test_web_agent.py#L23) | 23 | `"        \"page_fetched\": True,"` | — |
| [SRC-F725E90B2A-L000024](../../tests/test_web_agent.py#L24) | 24 | `"        \"providers\": [\"test_provider\"],"` | — |
| [SRC-F725E90B2A-L000025](../../tests/test_web_agent.py#L25) | 25 | `"        \"queries\": [\"قارن هذه التقنية\"],"` | — |
| [SRC-F725E90B2A-L000026](../../tests/test_web_agent.py#L26) | 26 | `"        \"domain\": domain,"` | — |
| [SRC-F725E90B2A-L000027](../../tests/test_web_agent.py#L27) | 27 | `"        \"source_class\": \"general\","` | — |
| [SRC-F725E90B2A-L000028](../../tests/test_web_agent.py#L28) | 28 | `"        \"platform\": \"web\","` | — |
| [SRC-F725E90B2A-L000029](../../tests/test_web_agent.py#L29) | 29 | `"    }"` | — |
| [SRC-F725E90B2A-L000030](../../tests/test_web_agent.py#L30) | 30 | `""` | — |
| [SRC-F725E90B2A-L000031](../../tests/test_web_agent.py#L31) | 31 | `""` | — |
| [SRC-F725E90B2A-L000032](../../tests/test_web_agent.py#L32) | 32 | `"def test_agent_synthesizes_with_sources_without_live_network(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000033](../../tests/test_web_agent.py#L33) | 33 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000034](../../tests/test_web_agent.py#L34) | 34 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000035](../../tests/test_web_agent.py#L35) | 35 | `"    seen = {}"` | — |
| [SRC-F725E90B2A-L000036](../../tests/test_web_agent.py#L36) | 36 | `""` | — |
| [SRC-F725E90B2A-L000037](../../tests/test_web_agent.py#L37) | 37 | `"    def plan(question, history):"` | — |
| [SRC-F725E90B2A-L000038](../../tests/test_web_agent.py#L38) | 38 | `"        return {"` | — |
| [SRC-F725E90B2A-L000039](../../tests/test_web_agent.py#L39) | 39 | `"            \"queries\": [question],"` | — |
| [SRC-F725E90B2A-L000040](../../tests/test_web_agent.py#L40) | 40 | `"            \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L000041](../../tests/test_web_agent.py#L41) | 41 | `"            \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L000042](../../tests/test_web_agent.py#L42) | 42 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000043](../../tests/test_web_agent.py#L43) | 43 | `"            \"platforms\": [],"` | — |
| [SRC-F725E90B2A-L000044](../../tests/test_web_agent.py#L44) | 44 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000045](../../tests/test_web_agent.py#L45) | 45 | `"        }"` | — |
| [SRC-F725E90B2A-L000046](../../tests/test_web_agent.py#L46) | 46 | `""` | — |
| [SRC-F725E90B2A-L000047](../../tests/test_web_agent.py#L47) | 47 | `"    def collect(research_plan):"` | — |
| [SRC-F725E90B2A-L000048](../../tests/test_web_agent.py#L48) | 48 | `"        seen[\"plan\"] = research_plan"` | — |
| [SRC-F725E90B2A-L000049](../../tests/test_web_agent.py#L49) | 49 | `"        return [sample_source(0), sample_source(1)], [], {"` | — |
| [SRC-F725E90B2A-L000050](../../tests/test_web_agent.py#L50) | 50 | `"            \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L000051](../../tests/test_web_agent.py#L51) | 51 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L000052](../../tests/test_web_agent.py#L52) | 52 | `"            \"query_results\": [{\"query\": research_plan[\"queries\"][0], \"results\": 1}],"` | — |
| [SRC-F725E90B2A-L000053](../../tests/test_web_agent.py#L53) | 53 | `"            \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L000054](../../tests/test_web_agent.py#L54) | 54 | `"            \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L000055](../../tests/test_web_agent.py#L55) | 55 | `"            \"providers_used\": [\"test\"],"` | — |
| [SRC-F725E90B2A-L000056](../../tests/test_web_agent.py#L56) | 56 | `"            \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L000057](../../tests/test_web_agent.py#L57) | 57 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L000058](../../tests/test_web_agent.py#L58) | 58 | `"            \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000059](../../tests/test_web_agent.py#L59) | 59 | `"            \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000060](../../tests/test_web_agent.py#L60) | 60 | `"        }"` | — |
| [SRC-F725E90B2A-L000061](../../tests/test_web_agent.py#L61) | 61 | `""` | — |
| [SRC-F725E90B2A-L000062](../../tests/test_web_agent.py#L62) | 62 | `"    def generate(question, history, sources, search_warning, research_plan=None, search_report=None):"` | — |
| [SRC-F725E90B2A-L000063](../../tests/test_web_agent.py#L63) | 63 | `"        seen[\"question\"] = question"` | — |
| [SRC-F725E90B2A-L000064](../../tests/test_web_agent.py#L64) | 64 | `"        seen[\"history\"] = history"` | — |
| [SRC-F725E90B2A-L000065](../../tests/test_web_agent.py#L65) | 65 | `"        seen[\"sources\"] = sources"` | — |
| [SRC-F725E90B2A-L000066](../../tests/test_web_agent.py#L66) | 66 | `"        seen[\"report\"] = search_report"` | — |
| [SRC-F725E90B2A-L000067](../../tests/test_web_agent.py#L67) | 67 | `"        return \"الإجابة: التقنية مناسبة للأسباب التالية [المصدر 1].\""` | — |
| [SRC-F725E90B2A-L000068](../../tests/test_web_agent.py#L68) | 68 | `""` | — |
| [SRC-F725E90B2A-L000069](../../tests/test_web_agent.py#L69) | 69 | `"    monkeypatch.setattr(agent, \"_plan_search\", plan)"` | — |
| [SRC-F725E90B2A-L000070](../../tests/test_web_agent.py#L70) | 70 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-F725E90B2A-L000071](../../tests/test_web_agent.py#L71) | 71 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-F725E90B2A-L000072](../../tests/test_web_agent.py#L72) | 72 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-F725E90B2A-L000073](../../tests/test_web_agent.py#L73) | 73 | `"    result = agent.answer("` | — |
| [SRC-F725E90B2A-L000074](../../tests/test_web_agent.py#L74) | 74 | `"        \"قارن هذه التقنية\","` | — |
| [SRC-F725E90B2A-L000075](../../tests/test_web_agent.py#L75) | 75 | `"        history=[{\"role\": \"user\", \"content\": \"ما هي التقنية؟\"}],"` | — |
| [SRC-F725E90B2A-L000076](../../tests/test_web_agent.py#L76) | 76 | `"    )"` | — |
| [SRC-F725E90B2A-L000077](../../tests/test_web_agent.py#L77) | 77 | `""` | — |
| [SRC-F725E90B2A-L000078](../../tests/test_web_agent.py#L78) | 78 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-F725E90B2A-L000079](../../tests/test_web_agent.py#L79) | 79 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L000080](../../tests/test_web_agent.py#L80) | 80 | `"    assert result[\"search_report\"][\"search_attempted\"] is True"` | — |
| [SRC-F725E90B2A-L000081](../../tests/test_web_agent.py#L81) | 81 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_with_usable_sources\""` | — |
| [SRC-F725E90B2A-L000082](../../tests/test_web_agent.py#L82) | 82 | `"    assert result[\"search_report\"][\"research_quality_semantics\"] == ("` | — |
| [SRC-F725E90B2A-L000083](../../tests/test_web_agent.py#L83) | 83 | `"        \"process_coverage_not_factual_probability\""` | — |
| [SRC-F725E90B2A-L000084](../../tests/test_web_agent.py#L84) | 84 | `"    )"` | — |
| [SRC-F725E90B2A-L000085](../../tests/test_web_agent.py#L85) | 85 | `"    assert result[\"search_report\"][\"claim_audit_semantics\"] == ("` | — |
| [SRC-F725E90B2A-L000086](../../tests/test_web_agent.py#L86) | 86 | `"        \"model_assisted_not_independent_fact_check\""` | — |
| [SRC-F725E90B2A-L000087](../../tests/test_web_agent.py#L87) | 87 | `"    )"` | — |
| [SRC-F725E90B2A-L000088](../../tests/test_web_agent.py#L88) | 88 | `"    assert result[\"search_report\"][\"distinct_registrable_domains\"] == 2"` | — |
| [SRC-F725E90B2A-L000089](../../tests/test_web_agent.py#L89) | 89 | `"    assert result[\"search_report\"][\"editorial_independence_status\"] == \"not_assessed\""` | — |
| [SRC-F725E90B2A-L000090](../../tests/test_web_agent.py#L90) | 90 | `"    assert result[\"search_report\"][\"independent_sources_field_semantics\"] == ("` | — |
| [SRC-F725E90B2A-L000091](../../tests/test_web_agent.py#L91) | 91 | `"        \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-F725E90B2A-L000092](../../tests/test_web_agent.py#L92) | 92 | `"    )"` | — |
| [SRC-F725E90B2A-L000093](../../tests/test_web_agent.py#L93) | 93 | `"    assert any(\"تعدد النطاقات المسجلة لا يثبت الاستقلال التحريري\" in warning"` | — |
| [SRC-F725E90B2A-L000094](../../tests/test_web_agent.py#L94) | 94 | `"               for warning in result[\"warnings\"])"` | — |
| [SRC-F725E90B2A-L000095](../../tests/test_web_agent.py#L95) | 95 | `"    assert result[\"used_language_model\"] is True"` | — |
| [SRC-F725E90B2A-L000096](../../tests/test_web_agent.py#L96) | 96 | `"    assert result[\"sources\"][0][\"url\"] == \"https://example.com/research\""` | — |
| [SRC-F725E90B2A-L000097](../../tests/test_web_agent.py#L97) | 97 | `"    assert \"[المصدر 1]\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L000098](../../tests/test_web_agent.py#L98) | 98 | `"    assert seen[\"question\"] == \"قارن هذه التقنية\""` | — |
| [SRC-F725E90B2A-L000099](../../tests/test_web_agent.py#L99) | 99 | `"    assert seen[\"history\"] == [{\"role\": \"user\", \"content\": \"ما هي التقنية؟\"}]"` | — |
| [SRC-F725E90B2A-L000100](../../tests/test_web_agent.py#L100) | 100 | `""` | — |
| [SRC-F725E90B2A-L000101](../../tests/test_web_agent.py#L101) | 101 | `""` | — |
| [SRC-F725E90B2A-L000102](../../tests/test_web_agent.py#L102) | 102 | `"def test_agent_returns_search_snippets_if_model_not_configured(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000103](../../tests/test_web_agent.py#L103) | 103 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000104](../../tests/test_web_agent.py#L104) | 104 | `"    agent.api_key = \"\""` | — |
| [SRC-F725E90B2A-L000105](../../tests/test_web_agent.py#L105) | 105 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000106](../../tests/test_web_agent.py#L106) | 106 | `"        agent,"` | — |
| [SRC-F725E90B2A-L000107](../../tests/test_web_agent.py#L107) | 107 | `"        \"_collect_research\","` | — |
| [SRC-F725E90B2A-L000108](../../tests/test_web_agent.py#L108) | 108 | `"        lambda plan: ("` | — |
| [SRC-F725E90B2A-L000109](../../tests/test_web_agent.py#L109) | 109 | `"            [sample_source(0), sample_source(1)],"` | — |
| [SRC-F725E90B2A-L000110](../../tests/test_web_agent.py#L110) | 110 | `"            [],"` | — |
| [SRC-F725E90B2A-L000111](../../tests/test_web_agent.py#L111) | 111 | `"            {"` | — |
| [SRC-F725E90B2A-L000112](../../tests/test_web_agent.py#L112) | 112 | `"                \"queries_planned\": 1,"` | — |
| [SRC-F725E90B2A-L000113](../../tests/test_web_agent.py#L113) | 113 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-F725E90B2A-L000114](../../tests/test_web_agent.py#L114) | 114 | `"                \"query_results\": [],"` | — |
| [SRC-F725E90B2A-L000115](../../tests/test_web_agent.py#L115) | 115 | `"                \"unique_sources\": 2,"` | — |
| [SRC-F725E90B2A-L000116](../../tests/test_web_agent.py#L116) | 116 | `"                \"pages_fetched\": 2,"` | — |
| [SRC-F725E90B2A-L000117](../../tests/test_web_agent.py#L117) | 117 | `"                \"providers_used\": [\"test\"],"` | — |
| [SRC-F725E90B2A-L000118](../../tests/test_web_agent.py#L118) | 118 | `"                \"platform_counts\": {\"web\": 1},"` | — |
| [SRC-F725E90B2A-L000119](../../tests/test_web_agent.py#L119) | 119 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-F725E90B2A-L000120](../../tests/test_web_agent.py#L120) | 120 | `"                \"depth\": \"standard\","` | — |
| [SRC-F725E90B2A-L000121](../../tests/test_web_agent.py#L121) | 121 | `"                \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000122](../../tests/test_web_agent.py#L122) | 122 | `"            },"` | — |
| [SRC-F725E90B2A-L000123](../../tests/test_web_agent.py#L123) | 123 | `"        ),"` | — |
| [SRC-F725E90B2A-L000124](../../tests/test_web_agent.py#L124) | 124 | `"    )"` | — |
| [SRC-F725E90B2A-L000125](../../tests/test_web_agent.py#L125) | 125 | `""` | — |
| [SRC-F725E90B2A-L000126](../../tests/test_web_agent.py#L126) | 126 | `"    result = agent.answer(\"ما الذي يقوله المصدر؟\")"` | — |
| [SRC-F725E90B2A-L000127](../../tests/test_web_agent.py#L127) | 127 | `""` | — |
| [SRC-F725E90B2A-L000128](../../tests/test_web_agent.py#L128) | 128 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-F725E90B2A-L000129](../../tests/test_web_agent.py#L129) | 129 | `"    assert result[\"used_language_model\"] is False"` | — |
| [SRC-F725E90B2A-L000130](../../tests/test_web_agent.py#L130) | 130 | `"    assert \"OPENROUTER_API_KEY\" in result[\"answer\"]"` | — |
| [SRC-F725E90B2A-L000131](../../tests/test_web_agent.py#L131) | 131 | `"    assert result[\"sources\"][0][\"page_fetched\"] is True"` | — |
| [SRC-F725E90B2A-L000132](../../tests/test_web_agent.py#L132) | 132 | `""` | — |
| [SRC-F725E90B2A-L000133](../../tests/test_web_agent.py#L133) | 133 | `""` | — |
| [SRC-F725E90B2A-L000134](../../tests/test_web_agent.py#L134) | 134 | `"def test_agent_rejects_empty_or_oversized_question():"` | — |
| [SRC-F725E90B2A-L000135](../../tests/test_web_agent.py#L135) | 135 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000136](../../tests/test_web_agent.py#L136) | 136 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-F725E90B2A-L000137](../../tests/test_web_agent.py#L137) | 137 | `"        agent.answer(\"   \")"` | — |
| [SRC-F725E90B2A-L000138](../../tests/test_web_agent.py#L138) | 138 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-F725E90B2A-L000139](../../tests/test_web_agent.py#L139) | 139 | `"        agent.answer(\"س\" * 4001)"` | — |
| [SRC-F725E90B2A-L000140](../../tests/test_web_agent.py#L140) | 140 | `""` | — |
| [SRC-F725E90B2A-L000141](../../tests/test_web_agent.py#L141) | 141 | `""` | — |
| [SRC-F725E90B2A-L000142](../../tests/test_web_agent.py#L142) | 142 | `"def test_history_search_query_expands_short_follow_up():"` | — |
| [SRC-F725E90B2A-L000143](../../tests/test_web_agent.py#L143) | 143 | `"    history = [{\"role\": \"user\", \"content\": \"قارن أسعار السيارات الكهربائية في مصر\"}]"` | — |
| [SRC-F725E90B2A-L000144](../../tests/test_web_agent.py#L144) | 144 | `"    query = WebAgent._history_search_query(\"والسعر؟\", history)"` | — |
| [SRC-F725E90B2A-L000145](../../tests/test_web_agent.py#L145) | 145 | `"    assert \"السيارات الكهربائية\" in query"` | — |
| [SRC-F725E90B2A-L000146](../../tests/test_web_agent.py#L146) | 146 | `"    assert \"والسعر؟\" in query"` | — |
| [SRC-F725E90B2A-L000147](../../tests/test_web_agent.py#L147) | 147 | `""` | — |
| [SRC-F725E90B2A-L000148](../../tests/test_web_agent.py#L148) | 148 | `""` | — |
| [SRC-F725E90B2A-L000149](../../tests/test_web_agent.py#L149) | 149 | `"def test_public_url_filter_rejects_local_and_credential_urls():"` | — |
| [SRC-F725E90B2A-L000150](../../tests/test_web_agent.py#L150) | 150 | `"    assert _public_http_url(\"http://127.0.0.1/admin\") is None"` | — |
| [SRC-F725E90B2A-L000151](../../tests/test_web_agent.py#L151) | 151 | `"    assert _public_http_url(\"http://localhost:8000/\") is None"` | — |
| [SRC-F725E90B2A-L000152](../../tests/test_web_agent.py#L152) | 152 | `"    assert _public_http_url(\"https://user:pass@example.com/private\") is None"` | — |
| [SRC-F725E90B2A-L000153](../../tests/test_web_agent.py#L153) | 153 | `"    assert _public_http_url(\"file:///etc/passwd\") is None"` | — |
| [SRC-F725E90B2A-L000154](../../tests/test_web_agent.py#L154) | 154 | `""` | — |
| [SRC-F725E90B2A-L000155](../../tests/test_web_agent.py#L155) | 155 | `""` | — |
| [SRC-F725E90B2A-L000156](../../tests/test_web_agent.py#L156) | 156 | `"def test_public_url_filter_accepts_basic_https_url():"` | — |
| [SRC-F725E90B2A-L000157](../../tests/test_web_agent.py#L157) | 157 | `"    assert _public_http_url(\"https://example.com/path#section\") == \"https://example.com/path\""` | — |
| [SRC-F725E90B2A-L000158](../../tests/test_web_agent.py#L158) | 158 | `""` | — |
| [SRC-F725E90B2A-L000159](../../tests/test_web_agent.py#L159) | 159 | `""` | — |
| [SRC-F725E90B2A-L000160](../../tests/test_web_agent.py#L160) | 160 | `"def test_search_web_parses_duckduckgo_and_bing_without_ddgs(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000161](../../tests/test_web_agent.py#L161) | 161 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000162](../../tests/test_web_agent.py#L162) | 162 | `""` | — |
| [SRC-F725E90B2A-L000163](../../tests/test_web_agent.py#L163) | 163 | `"    html = \"\"\""` | — |
| [SRC-F725E90B2A-L000164](../../tests/test_web_agent.py#L164) | 164 | `"    <html><body>"` | — |
| [SRC-F725E90B2A-L000165](../../tests/test_web_agent.py#L165) | 165 | `"      <div class=\"result\">"` | — |
| [SRC-F725E90B2A-L000166](../../tests/test_web_agent.py#L166) | 166 | `"        <a class=\"result__a\" href=\"https://example.com/first\">صفحة أولى</a>"` | — |
| [SRC-F725E90B2A-L000167](../../tests/test_web_agent.py#L167) | 167 | `"        <a class=\"result__snippet\">سؤال بحث تجريبي مقتطف أول</a>"` | — |
| [SRC-F725E90B2A-L000168](../../tests/test_web_agent.py#L168) | 168 | `"      </div>"` | — |
| [SRC-F725E90B2A-L000169](../../tests/test_web_agent.py#L169) | 169 | `"    </body></html>"` | — |
| [SRC-F725E90B2A-L000170](../../tests/test_web_agent.py#L170) | 170 | `"    \"\"\""` | — |
| [SRC-F725E90B2A-L000171](../../tests/test_web_agent.py#L171) | 171 | `"    rss = \"\"\""` | — |
| [SRC-F725E90B2A-L000172](../../tests/test_web_agent.py#L172) | 172 | `"    <rss><channel><item>"` | — |
| [SRC-F725E90B2A-L000173](../../tests/test_web_agent.py#L173) | 173 | `"      <title>صفحة ثانية</title>"` | — |
| [SRC-F725E90B2A-L000174](../../tests/test_web_agent.py#L174) | 174 | `"      <link>https://example.net/second</link>"` | — |
| [SRC-F725E90B2A-L000175](../../tests/test_web_agent.py#L175) | 175 | `"      <description>سؤال بحث تجريبي مقتطف ثاني</description>"` | — |
| [SRC-F725E90B2A-L000176](../../tests/test_web_agent.py#L176) | 176 | `"    </item></channel></rss>"` | — |
| [SRC-F725E90B2A-L000177](../../tests/test_web_agent.py#L177) | 177 | `"    \"\"\""` | — |
| [SRC-F725E90B2A-L000178](../../tests/test_web_agent.py#L178) | 178 | `""` | — |
| [SRC-F725E90B2A-L000179](../../tests/test_web_agent.py#L179) | 179 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000180](../../tests/test_web_agent.py#L180) | 180 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000181](../../tests/test_web_agent.py#L181) | 181 | `""` | — |
| [SRC-F725E90B2A-L000182](../../tests/test_web_agent.py#L182) | 182 | `"        def __init__(self, text):"` | — |
| [SRC-F725E90B2A-L000183](../../tests/test_web_agent.py#L183) | 183 | `"            self.text = text"` | — |
| [SRC-F725E90B2A-L000184](../../tests/test_web_agent.py#L184) | 184 | `"            self.content = text.encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000185](../../tests/test_web_agent.py#L185) | 185 | `""` | — |
| [SRC-F725E90B2A-L000186](../../tests/test_web_agent.py#L186) | 186 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000187](../../tests/test_web_agent.py#L187) | 187 | `""` | — |
| [SRC-F725E90B2A-L000188](../../tests/test_web_agent.py#L188) | 188 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000189](../../tests/test_web_agent.py#L189) | 189 | `"        calls.append(url)"` | — |
| [SRC-F725E90B2A-L000190](../../tests/test_web_agent.py#L190) | 190 | `"        return FakeResponse(html if \"duckduckgo.com\" in url else rss)"` | — |
| [SRC-F725E90B2A-L000191](../../tests/test_web_agent.py#L191) | 191 | `""` | — |
| [SRC-F725E90B2A-L000192](../../tests/test_web_agent.py#L192) | 192 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000193](../../tests/test_web_agent.py#L193) | 193 | `"    results = WebAgent()._search_web(\"سؤال بحث تجريبي\")"` | — |
| [SRC-F725E90B2A-L000194](../../tests/test_web_agent.py#L194) | 194 | `""` | — |
| [SRC-F725E90B2A-L000195](../../tests/test_web_agent.py#L195) | 195 | `"    assert len(results) == 2"` | — |
| [SRC-F725E90B2A-L000196](../../tests/test_web_agent.py#L196) | 196 | `"    assert results[0][\"title\"] == \"صفحة أولى\""` | — |
| [SRC-F725E90B2A-L000197](../../tests/test_web_agent.py#L197) | 197 | `"    assert results[0][\"url\"] == \"https://example.com/first\""` | — |
| [SRC-F725E90B2A-L000198](../../tests/test_web_agent.py#L198) | 198 | `"    assert results[1][\"title\"] == \"صفحة ثانية\""` | — |
| [SRC-F725E90B2A-L000199](../../tests/test_web_agent.py#L199) | 199 | `"    assert results[1][\"url\"] == \"https://example.net/second\""` | — |
| [SRC-F725E90B2A-L000200](../../tests/test_web_agent.py#L200) | 200 | `"    assert len(calls) == 2"` | — |
| [SRC-F725E90B2A-L000201](../../tests/test_web_agent.py#L201) | 201 | `""` | — |
| [SRC-F725E90B2A-L000202](../../tests/test_web_agent.py#L202) | 202 | `""` | — |
| [SRC-F725E90B2A-L000203](../../tests/test_web_agent.py#L203) | 203 | `""` | — |
| [SRC-F725E90B2A-L000204](../../tests/test_web_agent.py#L204) | 204 | `"def test_model_planner_preserves_social_intent_and_adds_targeted_query(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000205](../../tests/test_web_agent.py#L205) | 205 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000206](../../tests/test_web_agent.py#L206) | 206 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-F725E90B2A-L000207](../../tests/test_web_agent.py#L207) | 207 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000208](../../tests/test_web_agent.py#L208) | 208 | `"        agent,"` | — |
| [SRC-F725E90B2A-L000209](../../tests/test_web_agent.py#L209) | 209 | `"        \"_request_completion\","` | — |
| [SRC-F725E90B2A-L000210](../../tests/test_web_agent.py#L210) | 210 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-F725E90B2A-L000211](../../tests/test_web_agent.py#L211) | 211 | `"            '{\"queries\":[\"مراجعات السيارات الكهربائية\"],\"social_focus\":true,'"` | — |
| [SRC-F725E90B2A-L000212](../../tests/test_web_agent.py#L212) | 212 | `"            '\"freshness\":\"any\",\"depth\":\"deep\",\"platforms\":[\"reddit\"]}'"` | — |
| [SRC-F725E90B2A-L000213](../../tests/test_web_agent.py#L213) | 213 | `"        ),"` | — |
| [SRC-F725E90B2A-L000214](../../tests/test_web_agent.py#L214) | 214 | `"    )"` | — |
| [SRC-F725E90B2A-L000215](../../tests/test_web_agent.py#L215) | 215 | `"    plan = agent._plan_search("` | — |
| [SRC-F725E90B2A-L000216](../../tests/test_web_agent.py#L216) | 216 | `"        \"ابحث في Reddit عن تجارب العملاء مع السيارات الكهربائية\","` | — |
| [SRC-F725E90B2A-L000217](../../tests/test_web_agent.py#L217) | 217 | `"        [],"` | — |
| [SRC-F725E90B2A-L000218](../../tests/test_web_agent.py#L218) | 218 | `"    )"` | — |
| [SRC-F725E90B2A-L000219](../../tests/test_web_agent.py#L219) | 219 | `"    assert plan[\"planning_method\"] == \"language_model\""` | — |
| [SRC-F725E90B2A-L000220](../../tests/test_web_agent.py#L220) | 220 | `"    assert plan[\"social_focus\"] is True"` | — |
| [SRC-F725E90B2A-L000221](../../tests/test_web_agent.py#L221) | 221 | `"    assert \"reddit\" in plan[\"platforms\"]"` | — |
| [SRC-F725E90B2A-L000222](../../tests/test_web_agent.py#L222) | 222 | `"    assert any(\"site:reddit.com\" in query for query in plan[\"queries\"])"` | — |
| [SRC-F725E90B2A-L000223](../../tests/test_web_agent.py#L223) | 223 | `""` | — |
| [SRC-F725E90B2A-L000224](../../tests/test_web_agent.py#L224) | 224 | `""` | — |
| [SRC-F725E90B2A-L000225](../../tests/test_web_agent.py#L225) | 225 | `"def test_direct_social_search_reads_public_reddit_and_bluesky_results(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000226](../../tests/test_web_agent.py#L226) | 226 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000227](../../tests/test_web_agent.py#L227) | 227 | `""` | — |
| [SRC-F725E90B2A-L000228](../../tests/test_web_agent.py#L228) | 228 | `"    reddit_xml = \"\"\"<rss><channel><item>"` | — |
| [SRC-F725E90B2A-L000229](../../tests/test_web_agent.py#L229) | 229 | `"      <title>تجربة سيارة كهربائية</title>"` | — |
| [SRC-F725E90B2A-L000230](../../tests/test_web_agent.py#L230) | 230 | `"      <link>https://www.reddit.com/r/cars/comments/abc123/test/</link>"` | — |
| [SRC-F725E90B2A-L000231](../../tests/test_web_agent.py#L231) | 231 | `"      <description>استهلاك البطارية في الحر</description>"` | — |
| [SRC-F725E90B2A-L000232](../../tests/test_web_agent.py#L232) | 232 | `"      <pubDate>Mon, 12 Oct 2026 10:00:00 GMT</pubDate>"` | — |
| [SRC-F725E90B2A-L000233](../../tests/test_web_agent.py#L233) | 233 | `"    </item></channel></rss>\"\"\""` | — |
| [SRC-F725E90B2A-L000234](../../tests/test_web_agent.py#L234) | 234 | `""` | — |
| [SRC-F725E90B2A-L000235](../../tests/test_web_agent.py#L235) | 235 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000236](../../tests/test_web_agent.py#L236) | 236 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000237](../../tests/test_web_agent.py#L237) | 237 | `""` | — |
| [SRC-F725E90B2A-L000238](../../tests/test_web_agent.py#L238) | 238 | `"        def __init__(self, text=\"\", data=None):"` | — |
| [SRC-F725E90B2A-L000239](../../tests/test_web_agent.py#L239) | 239 | `"            self.text = text"` | — |
| [SRC-F725E90B2A-L000240](../../tests/test_web_agent.py#L240) | 240 | `"            self.content = text.encode(\"utf-8\")"` | — |
| [SRC-F725E90B2A-L000241](../../tests/test_web_agent.py#L241) | 241 | `"            self._data = data or {}"` | — |
| [SRC-F725E90B2A-L000242](../../tests/test_web_agent.py#L242) | 242 | `""` | — |
| [SRC-F725E90B2A-L000243](../../tests/test_web_agent.py#L243) | 243 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000244](../../tests/test_web_agent.py#L244) | 244 | `"            return self._data"` | — |
| [SRC-F725E90B2A-L000245](../../tests/test_web_agent.py#L245) | 245 | `""` | — |
| [SRC-F725E90B2A-L000246](../../tests/test_web_agent.py#L246) | 246 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000247](../../tests/test_web_agent.py#L247) | 247 | `"        if \"reddit.com\" in url:"` | — |
| [SRC-F725E90B2A-L000248](../../tests/test_web_agent.py#L248) | 248 | `"            return FakeResponse(reddit_xml)"` | — |
| [SRC-F725E90B2A-L000249](../../tests/test_web_agent.py#L249) | 249 | `"        if \"bsky.app\" in url or \"public.api.bsky.app\" in url:"` | — |
| [SRC-F725E90B2A-L000250](../../tests/test_web_agent.py#L250) | 250 | `"            return FakeResponse(data={"` | — |
| [SRC-F725E90B2A-L000251](../../tests/test_web_agent.py#L251) | 251 | `"                \"posts\": [{"` | — |
| [SRC-F725E90B2A-L000252](../../tests/test_web_agent.py#L252) | 252 | `"                    \"post\": {"` | — |
| [SRC-F725E90B2A-L000253](../../tests/test_web_agent.py#L253) | 253 | `"                        \"uri\": \"at://did:plc:example/app.bsky.feed.post/rkey123\","` | — |
| [SRC-F725E90B2A-L000254](../../tests/test_web_agent.py#L254) | 254 | `"                        \"indexedAt\": \"2026-10-12T10:00:00Z\","` | — |
| [SRC-F725E90B2A-L000255](../../tests/test_web_agent.py#L255) | 255 | `"                        \"record\": {\"text\": \"استخدمت السيارة شهرًا\"},"` | — |
| [SRC-F725E90B2A-L000256](../../tests/test_web_agent.py#L256) | 256 | `"                        \"author\": {\"handle\": \"driver.bsky.social\", \"displayName\": \"Driver\"},"` | — |
| [SRC-F725E90B2A-L000257](../../tests/test_web_agent.py#L257) | 257 | `"                    }"` | — |
| [SRC-F725E90B2A-L000258](../../tests/test_web_agent.py#L258) | 258 | `"                }]"` | — |
| [SRC-F725E90B2A-L000259](../../tests/test_web_agent.py#L259) | 259 | `"            })"` | — |
| [SRC-F725E90B2A-L000260](../../tests/test_web_agent.py#L260) | 260 | `"        raise AssertionError(f\"Unexpected URL: {url}\")"` | — |
| [SRC-F725E90B2A-L000261](../../tests/test_web_agent.py#L261) | 261 | `""` | — |
| [SRC-F725E90B2A-L000262](../../tests/test_web_agent.py#L262) | 262 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000263](../../tests/test_web_agent.py#L263) | 263 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000264](../../tests/test_web_agent.py#L264) | 264 | `"        \"سيارة كهربائية\", [\"reddit\", \"bluesky\"]"` | — |
| [SRC-F725E90B2A-L000265](../../tests/test_web_agent.py#L265) | 265 | `"    )"` | — |
| [SRC-F725E90B2A-L000266](../../tests/test_web_agent.py#L266) | 266 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000267](../../tests/test_web_agent.py#L267) | 267 | `"    assert any(item[\"provider\"] == \"reddit_public_rss\" for item in results)"` | — |
| [SRC-F725E90B2A-L000268](../../tests/test_web_agent.py#L268) | 268 | `"    bsky = next(item for item in results if item[\"provider\"] == \"bluesky_public_search\")"` | — |
| [SRC-F725E90B2A-L000269](../../tests/test_web_agent.py#L269) | 269 | `"    assert bsky[\"url\"] == \"https://bsky.app/profile/driver.bsky.social/post/rkey123\""` | — |
| [SRC-F725E90B2A-L000270](../../tests/test_web_agent.py#L270) | 270 | `"    assert bsky[\"snippet\"] == \"استخدمت السيارة شهرًا\""` | — |
| [SRC-F725E90B2A-L000271](../../tests/test_web_agent.py#L271) | 271 | `""` | — |
| [SRC-F725E90B2A-L000272](../../tests/test_web_agent.py#L272) | 272 | `""` | — |
| [SRC-F725E90B2A-L000273](../../tests/test_web_agent.py#L273) | 273 | `"def test_research_collection_fuses_multiple_queries_and_reports_provenance(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000274](../../tests/test_web_agent.py#L274) | 274 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000275](../../tests/test_web_agent.py#L275) | 275 | `""` | — |
| [SRC-F725E90B2A-L000276](../../tests/test_web_agent.py#L276) | 276 | `"    def search(query):"` | — |
| [SRC-F725E90B2A-L000277](../../tests/test_web_agent.py#L277) | 277 | `"        if query == \"query one\":"` | — |
| [SRC-F725E90B2A-L000278](../../tests/test_web_agent.py#L278) | 278 | `"            return ["` | — |
| [SRC-F725E90B2A-L000279](../../tests/test_web_agent.py#L279) | 279 | `"                {\"title\": \"Shared\", \"url\": \"https://example.com/shared\", \"snippet\": \"Some evidence\", \"provider\": \"ddg\", \"provider_rank\": 1},"` | — |
| [SRC-F725E90B2A-L000280](../../tests/test_web_agent.py#L280) | 280 | `"                {\"title\": \"Unique A\", \"url\": \"https://example.com/a\", \"snippet\": \"Evidence A\", \"provider\": \"ddg\", \"provider_rank\": 2},"` | — |
| [SRC-F725E90B2A-L000281](../../tests/test_web_agent.py#L281) | 281 | `"            ]"` | — |
| [SRC-F725E90B2A-L000282](../../tests/test_web_agent.py#L282) | 282 | `"        return ["` | — |
| [SRC-F725E90B2A-L000283](../../tests/test_web_agent.py#L283) | 283 | `"            {\"title\": \"Shared item\", \"url\": \"https://example.com/shared\", \"snippet\": \"More evidence about this result\", \"provider\": \"bing\", \"provider_rank\": 1},"` | — |
| [SRC-F725E90B2A-L000284](../../tests/test_web_agent.py#L284) | 284 | `"            {\"title\": \"Unique B\", \"url\": \"https://example.com/b\", \"snippet\": \"Evidence B\", \"provider\": \"bing\", \"provider_rank\": 2},"` | — |
| [SRC-F725E90B2A-L000285](../../tests/test_web_agent.py#L285) | 285 | `"        ]"` | — |
| [SRC-F725E90B2A-L000286](../../tests/test_web_agent.py#L286) | 286 | `""` | — |
| [SRC-F725E90B2A-L000287](../../tests/test_web_agent.py#L287) | 287 | `"    monkeypatch.setattr(agent, \"_search_web\", search)"` | — |
| [SRC-F725E90B2A-L000288](../../tests/test_web_agent.py#L288) | 288 | `"    monkeypatch.setattr(agent, \"_fetch_page\", lambda url: (\"Read title\", \"Extracted public page text\"))"` | — |
| [SRC-F725E90B2A-L000289](../../tests/test_web_agent.py#L289) | 289 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-F725E90B2A-L000290](../../tests/test_web_agent.py#L290) | 290 | `"        \"queries\": [\"query one\", \"query two\"],"` | — |
| [SRC-F725E90B2A-L000291](../../tests/test_web_agent.py#L291) | 291 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L000292](../../tests/test_web_agent.py#L292) | 292 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L000293](../../tests/test_web_agent.py#L293) | 293 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000294](../../tests/test_web_agent.py#L294) | 294 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000295](../../tests/test_web_agent.py#L295) | 295 | `"    })"` | — |
| [SRC-F725E90B2A-L000296](../../tests/test_web_agent.py#L296) | 296 | `"    shared = next(item for item in sources if \"shared\" in item[\"url\"])"` | — |
| [SRC-F725E90B2A-L000297](../../tests/test_web_agent.py#L297) | 297 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000298](../../tests/test_web_agent.py#L298) | 298 | `"    assert len(sources) == 3"` | — |
| [SRC-F725E90B2A-L000299](../../tests/test_web_agent.py#L299) | 299 | `"    assert set(shared[\"providers\"]) == {\"ddg\", \"bing\"}"` | — |
| [SRC-F725E90B2A-L000300](../../tests/test_web_agent.py#L300) | 300 | `"    assert {\"query one\", \"query two\"}.issubset(set(shared[\"queries\"]))"` | — |
| [SRC-F725E90B2A-L000301](../../tests/test_web_agent.py#L301) | 301 | `"    assert len(shared[\"queries\"]) >= 2"` | — |
| [SRC-F725E90B2A-L000302](../../tests/test_web_agent.py#L302) | 302 | `"    assert report[\"queries_planned\"] >= 2"` | — |
| [SRC-F725E90B2A-L000303](../../tests/test_web_agent.py#L303) | 303 | `"    assert report[\"queries_attempted\"] >= 2"` | — |
| [SRC-F725E90B2A-L000304](../../tests/test_web_agent.py#L304) | 304 | `"    assert report[\"expansion_queries\"]"` | — |
| [SRC-F725E90B2A-L000305](../../tests/test_web_agent.py#L305) | 305 | `"    assert report[\"pages_fetched\"] == 3"` | — |
| [SRC-F725E90B2A-L000306](../../tests/test_web_agent.py#L306) | 306 | `"    assert \"ddg\" in report[\"providers_used\"]"` | — |
| [SRC-F725E90B2A-L000307](../../tests/test_web_agent.py#L307) | 307 | `"    assert \"bing\" in report[\"providers_used\"]"` | — |
| [SRC-F725E90B2A-L000308](../../tests/test_web_agent.py#L308) | 308 | `""` | — |
| [SRC-F725E90B2A-L000309](../../tests/test_web_agent.py#L309) | 309 | `""` | — |
| [SRC-F725E90B2A-L000310](../../tests/test_web_agent.py#L310) | 310 | `""` | — |
| [SRC-F725E90B2A-L000311](../../tests/test_web_agent.py#L311) | 311 | `"def test_invalid_citations_are_removed_and_valid_ones_preserved():"` | — |
| [SRC-F725E90B2A-L000312](../../tests/test_web_agent.py#L312) | 312 | `"    answer, warnings = WebAgent._remove_invalid_citations("` | — |
| [SRC-F725E90B2A-L000313](../../tests/test_web_agent.py#L313) | 313 | `"        \"النتيجة [المصدر 1] وادعاء آخر [المصدر 11].\", 1"` | — |
| [SRC-F725E90B2A-L000314](../../tests/test_web_agent.py#L314) | 314 | `"    )"` | — |
| [SRC-F725E90B2A-L000315](../../tests/test_web_agent.py#L315) | 315 | `"    assert \"[المصدر 1]\" in answer"` | — |
| [SRC-F725E90B2A-L000316](../../tests/test_web_agent.py#L316) | 316 | `"    assert \"[المصدر 11]\" not in answer"` | — |
| [SRC-F725E90B2A-L000317](../../tests/test_web_agent.py#L317) | 317 | `"    assert len(warnings) == 1"` | — |
| [SRC-F725E90B2A-L000318](../../tests/test_web_agent.py#L318) | 318 | `""` | — |
| [SRC-F725E90B2A-L000319](../../tests/test_web_agent.py#L319) | 319 | `""` | — |
| [SRC-F725E90B2A-L000320](../../tests/test_web_agent.py#L320) | 320 | `"def test_citation_metadata_limits_claim_to_index_range_validation():"` | — |
| [SRC-F725E90B2A-L000321](../../tests/test_web_agent.py#L321) | 321 | `"    metadata = WebAgent._citation_validation_metadata("` | — |
| [SRC-F725E90B2A-L000322](../../tests/test_web_agent.py#L322) | 322 | `"        \"النتيجة المدعومة مبدئيًا [المصدر 1].\","` | — |
| [SRC-F725E90B2A-L000323](../../tests/test_web_agent.py#L323) | 323 | `"        1,"` | — |
| [SRC-F725E90B2A-L000324](../../tests/test_web_agent.py#L324) | 324 | `"        [],"` | — |
| [SRC-F725E90B2A-L000325](../../tests/test_web_agent.py#L325) | 325 | `"        \"model_claim_audit_completed\","` | — |
| [SRC-F725E90B2A-L000326](../../tests/test_web_agent.py#L326) | 326 | `"    )"` | — |
| [SRC-F725E90B2A-L000327](../../tests/test_web_agent.py#L327) | 327 | `"    assert metadata == {"` | — |
| [SRC-F725E90B2A-L000328](../../tests/test_web_agent.py#L328) | 328 | `"        \"method\": \"numeric_source_index_range_only\","` | — |
| [SRC-F725E90B2A-L000329](../../tests/test_web_agent.py#L329) | 329 | `"        \"status\": \"index_range_check_passed\","` | — |
| [SRC-F725E90B2A-L000330](../../tests/test_web_agent.py#L330) | 330 | `"        \"valid_citation_count\": 1,"` | — |
| [SRC-F725E90B2A-L000331](../../tests/test_web_agent.py#L331) | 331 | `"        \"invalid_references_removed\": 0,"` | — |
| [SRC-F725E90B2A-L000332](../../tests/test_web_agent.py#L332) | 332 | `"        \"max_citable_source_index\": 1,"` | — |
| [SRC-F725E90B2A-L000333](../../tests/test_web_agent.py#L333) | 333 | `"        \"claim_support\": \"model_review_not_independent_fact_check\","` | — |
| [SRC-F725E90B2A-L000334](../../tests/test_web_agent.py#L334) | 334 | `"    }"` | — |
| [SRC-F725E90B2A-L000335](../../tests/test_web_agent.py#L335) | 335 | `""` | — |
| [SRC-F725E90B2A-L000336](../../tests/test_web_agent.py#L336) | 336 | `""` | — |
| [SRC-F725E90B2A-L000337](../../tests/test_web_agent.py#L337) | 337 | `"def test_citation_metadata_reports_invalid_reference_repair():"` | — |
| [SRC-F725E90B2A-L000338](../../tests/test_web_agent.py#L338) | 338 | `"    cleaned, warnings = WebAgent._remove_invalid_citations("` | — |
| [SRC-F725E90B2A-L000339](../../tests/test_web_agent.py#L339) | 339 | `"        \"صحيح [المصدر 1] وخاطئ [المصدر 9].\", 1"` | — |
| [SRC-F725E90B2A-L000340](../../tests/test_web_agent.py#L340) | 340 | `"    )"` | — |
| [SRC-F725E90B2A-L000341](../../tests/test_web_agent.py#L341) | 341 | `"    metadata = WebAgent._citation_validation_metadata("` | — |
| [SRC-F725E90B2A-L000342](../../tests/test_web_agent.py#L342) | 342 | `"        cleaned, 1, warnings, \"not_run\""` | — |
| [SRC-F725E90B2A-L000343](../../tests/test_web_agent.py#L343) | 343 | `"    )"` | — |
| [SRC-F725E90B2A-L000344](../../tests/test_web_agent.py#L344) | 344 | `"    assert metadata[\"status\"] == \"invalid_index_references_removed\""` | — |
| [SRC-F725E90B2A-L000345](../../tests/test_web_agent.py#L345) | 345 | `"    assert metadata[\"valid_citation_count\"] == 1"` | — |
| [SRC-F725E90B2A-L000346](../../tests/test_web_agent.py#L346) | 346 | `"    assert metadata[\"invalid_references_removed\"] == 1"` | — |
| [SRC-F725E90B2A-L000347](../../tests/test_web_agent.py#L347) | 347 | `"    assert metadata[\"claim_support\"] == \"not_verified\""` | — |
| [SRC-F725E90B2A-L000348](../../tests/test_web_agent.py#L348) | 348 | `""` | — |
| [SRC-F725E90B2A-L000349](../../tests/test_web_agent.py#L349) | 349 | `""` | — |
| [SRC-F725E90B2A-L000350](../../tests/test_web_agent.py#L350) | 350 | `"def test_citation_metadata_reports_absent_markers_and_empty_source_range():"` | — |
| [SRC-F725E90B2A-L000351](../../tests/test_web_agent.py#L351) | 351 | `"    metadata = WebAgent._citation_validation_metadata("` | — |
| [SRC-F725E90B2A-L000352](../../tests/test_web_agent.py#L352) | 352 | `"        \"لا توجد إحالات للمصادر.\", 0, [], \"not_run\""` | — |
| [SRC-F725E90B2A-L000353](../../tests/test_web_agent.py#L353) | 353 | `"    )"` | — |
| [SRC-F725E90B2A-L000354](../../tests/test_web_agent.py#L354) | 354 | `"    assert metadata[\"status\"] == \"no_citation_markers_present\""` | — |
| [SRC-F725E90B2A-L000355](../../tests/test_web_agent.py#L355) | 355 | `"    assert metadata[\"valid_citation_count\"] == 0"` | — |
| [SRC-F725E90B2A-L000356](../../tests/test_web_agent.py#L356) | 356 | `"    assert metadata[\"max_citable_source_index\"] == 0"` | — |
| [SRC-F725E90B2A-L000357](../../tests/test_web_agent.py#L357) | 357 | `""` | — |
| [SRC-F725E90B2A-L000358](../../tests/test_web_agent.py#L358) | 358 | `""` | — |
| [SRC-F725E90B2A-L000359](../../tests/test_web_agent.py#L359) | 359 | `"def test_user_supplied_url_is_prioritized_and_page_content_is_extracted(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000360](../../tests/test_web_agent.py#L360) | 360 | `"    agent = WebAgent()"` | — |
| [SRC-F725E90B2A-L000361](../../tests/test_web_agent.py#L361) | 361 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: [])"` | — |
| [SRC-F725E90B2A-L000362](../../tests/test_web_agent.py#L362) | 362 | `"    monkeypatch.setattr("` | — |
| [SRC-F725E90B2A-L000363](../../tests/test_web_agent.py#L363) | 363 | `"        agent,"` | — |
| [SRC-F725E90B2A-L000364](../../tests/test_web_agent.py#L364) | 364 | `"        \"_fetch_page\","` | — |
| [SRC-F725E90B2A-L000365](../../tests/test_web_agent.py#L365) | 365 | `"        lambda url: (\"User page title\", \"Full public page text supplied for analysis\"),"` | — |
| [SRC-F725E90B2A-L000366](../../tests/test_web_agent.py#L366) | 366 | `"    )"` | — |
| [SRC-F725E90B2A-L000367](../../tests/test_web_agent.py#L367) | 367 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-F725E90B2A-L000368](../../tests/test_web_agent.py#L368) | 368 | `"        \"queries\": [\"لخص هذه الصفحة\"],"` | — |
| [SRC-F725E90B2A-L000369](../../tests/test_web_agent.py#L369) | 369 | `"        \"direct_urls\": [\"https://example.com/article\"],"` | — |
| [SRC-F725E90B2A-L000370](../../tests/test_web_agent.py#L370) | 370 | `"        \"social_focus\": False,"` | — |
| [SRC-F725E90B2A-L000371](../../tests/test_web_agent.py#L371) | 371 | `"        \"freshness\": \"any\","` | — |
| [SRC-F725E90B2A-L000372](../../tests/test_web_agent.py#L372) | 372 | `"        \"depth\": \"deep\","` | — |
| [SRC-F725E90B2A-L000373](../../tests/test_web_agent.py#L373) | 373 | `"        \"planning_method\": \"test\","` | — |
| [SRC-F725E90B2A-L000374](../../tests/test_web_agent.py#L374) | 374 | `"    })"` | — |
| [SRC-F725E90B2A-L000375](../../tests/test_web_agent.py#L375) | 375 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000376](../../tests/test_web_agent.py#L376) | 376 | `"    assert len(sources) == 1"` | — |
| [SRC-F725E90B2A-L000377](../../tests/test_web_agent.py#L377) | 377 | `"    assert sources[0][\"url\"] == \"https://example.com/article\""` | — |
| [SRC-F725E90B2A-L000378](../../tests/test_web_agent.py#L378) | 378 | `"    assert sources[0][\"title\"] == \"User page title\""` | — |
| [SRC-F725E90B2A-L000379](../../tests/test_web_agent.py#L379) | 379 | `"    assert sources[0][\"page_fetched\"] is True"` | — |
| [SRC-F725E90B2A-L000380](../../tests/test_web_agent.py#L380) | 380 | `"    assert \"user_supplied_url\" in report[\"providers_used\"]"` | — |
| [SRC-F725E90B2A-L000381](../../tests/test_web_agent.py#L381) | 381 | `""` | — |
| [SRC-F725E90B2A-L000382](../../tests/test_web_agent.py#L382) | 382 | `""` | — |
| [SRC-F725E90B2A-L000383](../../tests/test_web_agent.py#L383) | 383 | `""` | — |
| [SRC-F725E90B2A-L000384](../../tests/test_web_agent.py#L384) | 384 | `"def test_official_x_search_is_used_only_with_explicit_bearer_token(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000385](../../tests/test_web_agent.py#L385) | 385 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000386](../../tests/test_web_agent.py#L386) | 386 | `""` | — |
| [SRC-F725E90B2A-L000387](../../tests/test_web_agent.py#L387) | 387 | `"    monkeypatch.setenv(\"X_BEARER_TOKEN\", \"test-token\")"` | — |
| [SRC-F725E90B2A-L000388](../../tests/test_web_agent.py#L388) | 388 | `""` | — |
| [SRC-F725E90B2A-L000389](../../tests/test_web_agent.py#L389) | 389 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000390](../../tests/test_web_agent.py#L390) | 390 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000391](../../tests/test_web_agent.py#L391) | 391 | `""` | — |
| [SRC-F725E90B2A-L000392](../../tests/test_web_agent.py#L392) | 392 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000393](../../tests/test_web_agent.py#L393) | 393 | `"            return {"` | — |
| [SRC-F725E90B2A-L000394](../../tests/test_web_agent.py#L394) | 394 | `"                \"data\": [{"` | — |
| [SRC-F725E90B2A-L000395](../../tests/test_web_agent.py#L395) | 395 | `"                    \"id\": \"1840000000000000000\","` | — |
| [SRC-F725E90B2A-L000396](../../tests/test_web_agent.py#L396) | 396 | `"                    \"text\": \"تجربة علنية لاستهلاك سيارة كهربائية\","` | — |
| [SRC-F725E90B2A-L000397](../../tests/test_web_agent.py#L397) | 397 | `"                    \"created_at\": \"2026-10-12T10:00:00Z\","` | — |
| [SRC-F725E90B2A-L000398](../../tests/test_web_agent.py#L398) | 398 | `"                    \"author_id\": \"u1\","` | — |
| [SRC-F725E90B2A-L000399](../../tests/test_web_agent.py#L399) | 399 | `"                }],"` | — |
| [SRC-F725E90B2A-L000400](../../tests/test_web_agent.py#L400) | 400 | `"                \"includes\": {"` | — |
| [SRC-F725E90B2A-L000401](../../tests/test_web_agent.py#L401) | 401 | `"                    \"users\": [{\"id\": \"u1\", \"username\": \"driver\", \"name\": \"Driver\"}]"` | — |
| [SRC-F725E90B2A-L000402](../../tests/test_web_agent.py#L402) | 402 | `"                },"` | — |
| [SRC-F725E90B2A-L000403](../../tests/test_web_agent.py#L403) | 403 | `"            }"` | — |
| [SRC-F725E90B2A-L000404](../../tests/test_web_agent.py#L404) | 404 | `""` | — |
| [SRC-F725E90B2A-L000405](../../tests/test_web_agent.py#L405) | 405 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000406](../../tests/test_web_agent.py#L406) | 406 | `""` | — |
| [SRC-F725E90B2A-L000407](../../tests/test_web_agent.py#L407) | 407 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000408](../../tests/test_web_agent.py#L408) | 408 | `"        calls.append((url, kwargs))"` | — |
| [SRC-F725E90B2A-L000409](../../tests/test_web_agent.py#L409) | 409 | `"        return FakeResponse()"` | — |
| [SRC-F725E90B2A-L000410](../../tests/test_web_agent.py#L410) | 410 | `""` | — |
| [SRC-F725E90B2A-L000411](../../tests/test_web_agent.py#L411) | 411 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000412](../../tests/test_web_agent.py#L412) | 412 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000413](../../tests/test_web_agent.py#L413) | 413 | `"        \"سيارة كهربائية\", [\"x\"]"` | — |
| [SRC-F725E90B2A-L000414](../../tests/test_web_agent.py#L414) | 414 | `"    )"` | — |
| [SRC-F725E90B2A-L000415](../../tests/test_web_agent.py#L415) | 415 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000416](../../tests/test_web_agent.py#L416) | 416 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L000417](../../tests/test_web_agent.py#L417) | 417 | `"    assert results[0][\"provider\"] == \"x_official_api\""` | — |
| [SRC-F725E90B2A-L000418](../../tests/test_web_agent.py#L418) | 418 | `"    assert results[0][\"url\"] == \"https://x.com/driver/status/1840000000000000000\""` | — |
| [SRC-F725E90B2A-L000419](../../tests/test_web_agent.py#L419) | 419 | `"    assert calls[0][1][\"headers\"][\"Authorization\"] == \"Bearer test-token\""` | — |
| [SRC-F725E90B2A-L000420](../../tests/test_web_agent.py#L420) | 420 | `""` | — |
| [SRC-F725E90B2A-L000421](../../tests/test_web_agent.py#L421) | 421 | `""` | — |
| [SRC-F725E90B2A-L000422](../../tests/test_web_agent.py#L422) | 422 | `""` | — |
| [SRC-F725E90B2A-L000423](../../tests/test_web_agent.py#L423) | 423 | `"def test_instagram_graph_api_returns_only_public_hashtag_media(monkeypatch):"` | — |
| [SRC-F725E90B2A-L000424](../../tests/test_web_agent.py#L424) | 424 | `"    import httpx"` | — |
| [SRC-F725E90B2A-L000425](../../tests/test_web_agent.py#L425) | 425 | `""` | — |
| [SRC-F725E90B2A-L000426](../../tests/test_web_agent.py#L426) | 426 | `"    monkeypatch.setenv(\"INSTAGRAM_USER_ID\", \"ig-user-123\")"` | — |
| [SRC-F725E90B2A-L000427](../../tests/test_web_agent.py#L427) | 427 | `"    monkeypatch.setenv(\"INSTAGRAM_ACCESS_TOKEN\", \"test-ig-token\")"` | — |
| [SRC-F725E90B2A-L000428](../../tests/test_web_agent.py#L428) | 428 | `"    monkeypatch.setenv(\"META_GRAPH_VERSION\", \"v25.0\")"` | — |
| [SRC-F725E90B2A-L000429](../../tests/test_web_agent.py#L429) | 429 | `""` | — |
| [SRC-F725E90B2A-L000430](../../tests/test_web_agent.py#L430) | 430 | `"    class FakeResponse:"` | — |
| [SRC-F725E90B2A-L000431](../../tests/test_web_agent.py#L431) | 431 | `"        status_code = 200"` | — |
| [SRC-F725E90B2A-L000432](../../tests/test_web_agent.py#L432) | 432 | `""` | — |
| [SRC-F725E90B2A-L000433](../../tests/test_web_agent.py#L433) | 433 | `"        def __init__(self, payload):"` | — |
| [SRC-F725E90B2A-L000434](../../tests/test_web_agent.py#L434) | 434 | `"            self.payload = payload"` | — |
| [SRC-F725E90B2A-L000435](../../tests/test_web_agent.py#L435) | 435 | `""` | — |
| [SRC-F725E90B2A-L000436](../../tests/test_web_agent.py#L436) | 436 | `"        def json(self):"` | — |
| [SRC-F725E90B2A-L000437](../../tests/test_web_agent.py#L437) | 437 | `"            return self.payload"` | — |
| [SRC-F725E90B2A-L000438](../../tests/test_web_agent.py#L438) | 438 | `""` | — |
| [SRC-F725E90B2A-L000439](../../tests/test_web_agent.py#L439) | 439 | `"    calls = []"` | — |
| [SRC-F725E90B2A-L000440](../../tests/test_web_agent.py#L440) | 440 | `""` | — |
| [SRC-F725E90B2A-L000441](../../tests/test_web_agent.py#L441) | 441 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-F725E90B2A-L000442](../../tests/test_web_agent.py#L442) | 442 | `"        calls.append((url, kwargs))"` | — |
| [SRC-F725E90B2A-L000443](../../tests/test_web_agent.py#L443) | 443 | `"        if url.endswith(\"/ig_hashtag_search\"):"` | — |
| [SRC-F725E90B2A-L000444](../../tests/test_web_agent.py#L444) | 444 | `"            return FakeResponse({\"data\": [{\"id\": \"tag-7\", \"name\": \"cars\"}]})"` | — |
| [SRC-F725E90B2A-L000445](../../tests/test_web_agent.py#L445) | 445 | `"        if url.endswith(\"/tag-7/recent_media\"):"` | — |
| [SRC-F725E90B2A-L000446](../../tests/test_web_agent.py#L446) | 446 | `"            return FakeResponse({\"data\": [{"` | — |
| [SRC-F725E90B2A-L000447](../../tests/test_web_agent.py#L447) | 447 | `"                \"permalink\": \"https://www.instagram.com/p/ABC123/\","` | — |
| [SRC-F725E90B2A-L000448](../../tests/test_web_agent.py#L448) | 448 | `"                \"caption\": \"Owner shared an electric car review\","` | — |
| [SRC-F725E90B2A-L000449](../../tests/test_web_agent.py#L449) | 449 | `"                \"media_type\": \"IMAGE\","` | — |
| [SRC-F725E90B2A-L000450](../../tests/test_web_agent.py#L450) | 450 | `"                \"timestamp\": \"2026-10-12T10:00:00+0000\","` | — |
| [SRC-F725E90B2A-L000451](../../tests/test_web_agent.py#L451) | 451 | `"                \"like_count\": 17,"` | — |
| [SRC-F725E90B2A-L000452](../../tests/test_web_agent.py#L452) | 452 | `"                \"comments_count\": 4,"` | — |
| [SRC-F725E90B2A-L000453](../../tests/test_web_agent.py#L453) | 453 | `"            }]})"` | — |
| [SRC-F725E90B2A-L000454](../../tests/test_web_agent.py#L454) | 454 | `"        raise AssertionError(f\"Unexpected URL {url}\")"` | — |
| [SRC-F725E90B2A-L000455](../../tests/test_web_agent.py#L455) | 455 | `""` | — |
| [SRC-F725E90B2A-L000456](../../tests/test_web_agent.py#L456) | 456 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-F725E90B2A-L000457](../../tests/test_web_agent.py#L457) | 457 | `"    results, warnings = WebAgent()._search_social("` | — |
| [SRC-F725E90B2A-L000458](../../tests/test_web_agent.py#L458) | 458 | `"        \"Instagram #cars\", [\"instagram\"]"` | — |
| [SRC-F725E90B2A-L000459](../../tests/test_web_agent.py#L459) | 459 | `"    )"` | — |
| [SRC-F725E90B2A-L000460](../../tests/test_web_agent.py#L460) | 460 | `"    assert warnings == []"` | — |
| [SRC-F725E90B2A-L000461](../../tests/test_web_agent.py#L461) | 461 | `"    assert len(results) == 1"` | — |
| [SRC-F725E90B2A-L000462](../../tests/test_web_agent.py#L462) | 462 | `"    assert results[0][\"provider\"] == \"instagram_graph_api\""` | — |
| [SRC-F725E90B2A-L000463](../../tests/test_web_agent.py#L463) | 463 | `"    assert results[0][\"url\"] == \"https://www.instagram.com/p/ABC123/\""` | — |
| [SRC-F725E90B2A-L000464](../../tests/test_web_agent.py#L464) | 464 | `"    assert \"likes=17\" in results[0][\"snippet\"]"` | — |
| [SRC-F725E90B2A-L000465](../../tests/test_web_agent.py#L465) | 465 | `"    assert calls[0][1][\"params\"][\"q\"] == \"cars\""` | — |
| [SRC-F725E90B2A-L000466](../../tests/test_web_agent.py#L466) | 466 | `"    assert calls[0][1][\"params\"][\"access_token\"] == \"test-ig-token\""` | — |
