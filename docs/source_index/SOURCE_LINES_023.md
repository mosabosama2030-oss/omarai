# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **023**
- سجلات الأسطر: **800**
- النطاق: SRC-4CCB1F172B-L000195 إلى SRC-3451CC474D-L000249
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-4CCB1F172B — [tests/test_answer_quality_corpus.py](../../tests/test_answer_quality_corpus.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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

### FILE-1C77C97630 — [tests/test_answer_validation.py](../../tests/test_answer_validation.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1C77C97630-L000001](../../tests/test_answer_validation.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-1C77C97630-L000002](../../tests/test_answer_validation.py#L2) | 2 | `""` | — |
| [SRC-1C77C97630-L000003](../../tests/test_answer_validation.py#L3) | 3 | `"from pathlib import Path"` | — |
| [SRC-1C77C97630-L000004](../../tests/test_answer_validation.py#L4) | 4 | `""` | — |
| [SRC-1C77C97630-L000005](../../tests/test_answer_validation.py#L5) | 5 | `"import pytest"` | — |
| [SRC-1C77C97630-L000006](../../tests/test_answer_validation.py#L6) | 6 | `""` | — |
| [SRC-1C77C97630-L000007](../../tests/test_answer_validation.py#L7) | 7 | `"from agents.answer_validation import audit_answer_integrity"` | — |
| [SRC-1C77C97630-L000008](../../tests/test_answer_validation.py#L8) | 8 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-1C77C97630-L000009](../../tests/test_answer_validation.py#L9) | 9 | `""` | — |
| [SRC-1C77C97630-L000010](../../tests/test_answer_validation.py#L10) | 10 | `""` | — |
| [SRC-1C77C97630-L000011](../../tests/test_answer_validation.py#L11) | 11 | `"def test_numeric_screen_accepts_arabic_digits_and_thousands_formatting():"` | — |
| [SRC-1C77C97630-L000012](../../tests/test_answer_validation.py#L12) | 12 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000013](../../tests/test_answer_validation.py#L13) | 13 | `"        \"ما السعر المذكور في 2025؟\","` | — |
| [SRC-1C77C97630-L000014](../../tests/test_answer_validation.py#L14) | 14 | `"        \"السعر ١٠٠٬٠٠٠ جنيه في 2025 [المصدر 1].\","` | — |
| [SRC-1C77C97630-L000015](../../tests/test_answer_validation.py#L15) | 15 | `"        [{"` | — |
| [SRC-1C77C97630-L000016](../../tests/test_answer_validation.py#L16) | 16 | `"            \"title\": \"تفاصيل السعر\","` | — |
| [SRC-1C77C97630-L000017](../../tests/test_answer_validation.py#L17) | 17 | `"            \"snippet\": \"السعر 100,000 جنيه\","` | — |
| [SRC-1C77C97630-L000018](../../tests/test_answer_validation.py#L18) | 18 | `"            \"page_text\": \"السعر 100,000 جنيه\","` | — |
| [SRC-1C77C97630-L000019](../../tests/test_answer_validation.py#L19) | 19 | `"            \"page_fetched\": True,"` | — |
| [SRC-1C77C97630-L000020](../../tests/test_answer_validation.py#L20) | 20 | `"            \"published_at\": \"\","` | — |
| [SRC-1C77C97630-L000021](../../tests/test_answer_validation.py#L21) | 21 | `"        }],"` | — |
| [SRC-1C77C97630-L000022](../../tests/test_answer_validation.py#L22) | 22 | `"        [\"السعر\"],"` | — |
| [SRC-1C77C97630-L000023](../../tests/test_answer_validation.py#L23) | 23 | `"    )"` | — |
| [SRC-1C77C97630-L000024](../../tests/test_answer_validation.py#L24) | 24 | `"    assert result[\"numeric_check_status\"] == \"all_checked_numeric_literals_appear_in_source_text\""` | — |
| [SRC-1C77C97630-L000025](../../tests/test_answer_validation.py#L25) | 25 | `"    assert result[\"potentially_unsupported_numeric_literals\"] == []"` | — |
| [SRC-1C77C97630-L000026](../../tests/test_answer_validation.py#L26) | 26 | `"    assert result[\"source_evidence_scope\"] == \"contains_extracted_page_text_and_or_snippets\""` | — |
| [SRC-1C77C97630-L000027](../../tests/test_answer_validation.py#L27) | 27 | `"    assert result[\"citation_marker_count\"] == 1"` | — |
| [SRC-1C77C97630-L000028](../../tests/test_answer_validation.py#L28) | 28 | `"    assert result[\"semantic_verification\"] is False"` | — |
| [SRC-1C77C97630-L000029](../../tests/test_answer_validation.py#L29) | 29 | `""` | — |
| [SRC-1C77C97630-L000030](../../tests/test_answer_validation.py#L30) | 30 | `""` | — |
| [SRC-1C77C97630-L000031](../../tests/test_answer_validation.py#L31) | 31 | `"def test_numeric_screen_flags_number_absent_from_available_evidence():"` | — |
| [SRC-1C77C97630-L000032](../../tests/test_answer_validation.py#L32) | 32 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000033](../../tests/test_answer_validation.py#L33) | 33 | `"        \"ما السعر؟\","` | — |
| [SRC-1C77C97630-L000034](../../tests/test_answer_validation.py#L34) | 34 | `"        \"السعر 500 جنيه [المصدر 1].\","` | — |
| [SRC-1C77C97630-L000035](../../tests/test_answer_validation.py#L35) | 35 | `"        [{"` | — |
| [SRC-1C77C97630-L000036](../../tests/test_answer_validation.py#L36) | 36 | `"            \"title\": \"تفاصيل السعر\","` | — |
| [SRC-1C77C97630-L000037](../../tests/test_answer_validation.py#L37) | 37 | `"            \"snippet\": \"السعر 300 جنيه\","` | — |
| [SRC-1C77C97630-L000038](../../tests/test_answer_validation.py#L38) | 38 | `"            \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000039](../../tests/test_answer_validation.py#L39) | 39 | `"            \"published_at\": \"\","` | — |
| [SRC-1C77C97630-L000040](../../tests/test_answer_validation.py#L40) | 40 | `"        }],"` | — |
| [SRC-1C77C97630-L000041](../../tests/test_answer_validation.py#L41) | 41 | `"    )"` | — |
| [SRC-1C77C97630-L000042](../../tests/test_answer_validation.py#L42) | 42 | `"    assert result[\"numeric_check_status\"] == \"potentially_unsupported_numeric_literals\""` | — |
| [SRC-1C77C97630-L000043](../../tests/test_answer_validation.py#L43) | 43 | `"    assert \"500\" in result[\"potentially_unsupported_numeric_literals\"]"` | — |
| [SRC-1C77C97630-L000044](../../tests/test_answer_validation.py#L44) | 44 | `"    assert result[\"citation_entailment\"] == \"not_checked\""` | — |
| [SRC-1C77C97630-L000045](../../tests/test_answer_validation.py#L45) | 45 | `""` | — |
| [SRC-1C77C97630-L000046](../../tests/test_answer_validation.py#L46) | 46 | `""` | — |
| [SRC-1C77C97630-L000047](../../tests/test_answer_validation.py#L47) | 47 | `"def test_task_coverage_screen_flags_a_potentially_missing_target_without_claiming_failure():"` | — |
| [SRC-1C77C97630-L000048](../../tests/test_answer_validation.py#L48) | 48 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000049](../../tests/test_answer_validation.py#L49) | 49 | `"        \"قارن من حيث السعر والمساحة\","` | — |
| [SRC-1C77C97630-L000050](../../tests/test_answer_validation.py#L50) | 50 | `"        \"من حيث السعر، الخيار الأول أقل تكلفة.\","` | — |
| [SRC-1C77C97630-L000051](../../tests/test_answer_validation.py#L51) | 51 | `"        [{"` | — |
| [SRC-1C77C97630-L000052](../../tests/test_answer_validation.py#L52) | 52 | `"            \"title\": \"إعلان\","` | — |
| [SRC-1C77C97630-L000053](../../tests/test_answer_validation.py#L53) | 53 | `"            \"snippet\": \"السعر والمساحة غير موضحين\","` | — |
| [SRC-1C77C97630-L000054](../../tests/test_answer_validation.py#L54) | 54 | `"            \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000055](../../tests/test_answer_validation.py#L55) | 55 | `"        }],"` | — |
| [SRC-1C77C97630-L000056](../../tests/test_answer_validation.py#L56) | 56 | `"        [\"السعر\", \"المساحة\"],"` | — |
| [SRC-1C77C97630-L000057](../../tests/test_answer_validation.py#L57) | 57 | `"    )"` | — |
| [SRC-1C77C97630-L000058](../../tests/test_answer_validation.py#L58) | 58 | `"    checks = {item[\"target\"]: item for item in result[\"target_coverage\"]}"` | — |
| [SRC-1C77C97630-L000059](../../tests/test_answer_validation.py#L59) | 59 | `"    assert checks[\"السعر\"][\"status\"] == \"lexical_signal_found\""` | — |
| [SRC-1C77C97630-L000060](../../tests/test_answer_validation.py#L60) | 60 | `"    assert checks[\"المساحة\"][\"status\"] == \"possibly_missing\""` | — |
| [SRC-1C77C97630-L000061](../../tests/test_answer_validation.py#L61) | 61 | `"    assert result[\"potentially_missing_target_count\"] == 1"` | — |
| [SRC-1C77C97630-L000062](../../tests/test_answer_validation.py#L62) | 62 | `"    assert result[\"method\"] == \"deterministic_lexical_screen_only\""` | — |
| [SRC-1C77C97630-L000063](../../tests/test_answer_validation.py#L63) | 63 | `"    assert result[\"independent_fact_check\"] is False"` | — |
| [SRC-1C77C97630-L000064](../../tests/test_answer_validation.py#L64) | 64 | `""` | — |
| [SRC-1C77C97630-L000065](../../tests/test_answer_validation.py#L65) | 65 | `""` | — |
| [SRC-1C77C97630-L000066](../../tests/test_answer_validation.py#L66) | 66 | `"def test_source_scope_does_not_confuse_snippet_with_fetched_page():"` | — |
| [SRC-1C77C97630-L000067](../../tests/test_answer_validation.py#L67) | 67 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000068](../../tests/test_answer_validation.py#L68) | 68 | `"        \"ما التفاصيل؟\","` | — |
| [SRC-1C77C97630-L000069](../../tests/test_answer_validation.py#L69) | 69 | `"        \"وجدت مقتطفًا.\","` | — |
| [SRC-1C77C97630-L000070](../../tests/test_answer_validation.py#L70) | 70 | `"        [{\"title\": \"نتيجة\", \"snippet\": \"مقتطف قصير\", \"page_fetched\": False}],"` | — |
| [SRC-1C77C97630-L000071](../../tests/test_answer_validation.py#L71) | 71 | `"    )"` | — |
| [SRC-1C77C97630-L000072](../../tests/test_answer_validation.py#L72) | 72 | `"    assert result[\"source_evidence_scope\"] == \"search_snippets_only\""` | — |
| [SRC-1C77C97630-L000073](../../tests/test_answer_validation.py#L73) | 73 | `"    assert result[\"pages_with_extracted_text\"] == 0"` | — |
| [SRC-1C77C97630-L000074](../../tests/test_answer_validation.py#L74) | 74 | `"    assert result[\"sources_with_snippets_only\"] == 1"` | — |
| [SRC-1C77C97630-L000075](../../tests/test_answer_validation.py#L75) | 75 | `""` | — |
| [SRC-1C77C97630-L000076](../../tests/test_answer_validation.py#L76) | 76 | `""` | — |
| [SRC-1C77C97630-L000077](../../tests/test_answer_validation.py#L77) | 77 | `"def test_review_prompt_explicitly_requires_number_and_conflict_audit(monkeypatch):"` | — |
| [SRC-1C77C97630-L000078](../../tests/test_answer_validation.py#L78) | 78 | `"    agent = WebAgent()"` | — |
| [SRC-1C77C97630-L000079](../../tests/test_answer_validation.py#L79) | 79 | `"    captured = {}"` | — |
| [SRC-1C77C97630-L000080](../../tests/test_answer_validation.py#L80) | 80 | `""` | — |
| [SRC-1C77C97630-L000081](../../tests/test_answer_validation.py#L81) | 81 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-1C77C97630-L000082](../../tests/test_answer_validation.py#L82) | 82 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-1C77C97630-L000083](../../tests/test_answer_validation.py#L83) | 83 | `"        return \"<<<OMARAI_FINAL_ANSWER>>>لا تكفي الأدلة.<<<END_OMARAI_FINAL_ANSWER>>>\""` | — |
| [SRC-1C77C97630-L000084](../../tests/test_answer_validation.py#L84) | 84 | `""` | — |
| [SRC-1C77C97630-L000085](../../tests/test_answer_validation.py#L85) | 85 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-1C77C97630-L000086](../../tests/test_answer_validation.py#L86) | 86 | `"    answer = agent._review_answer("` | — |
| [SRC-1C77C97630-L000087](../../tests/test_answer_validation.py#L87) | 87 | `"        \"قارن السعر والمدة\","` | — |
| [SRC-1C77C97630-L000088](../../tests/test_answer_validation.py#L88) | 88 | `"        \"السعر 100 جنيه [المصدر 1].\","` | — |
| [SRC-1C77C97630-L000089](../../tests/test_answer_validation.py#L89) | 89 | `"        [{"` | — |
| [SRC-1C77C97630-L000090](../../tests/test_answer_validation.py#L90) | 90 | `"            \"title\": \"مصدر\","` | — |
| [SRC-1C77C97630-L000091](../../tests/test_answer_validation.py#L91) | 91 | `"            \"url\": \"https://example.com/item\","` | — |
| [SRC-1C77C97630-L000092](../../tests/test_answer_validation.py#L92) | 92 | `"            \"page_text\": \"السعر 90 جنيه، والمدة 5 أيام.\","` | — |
| [SRC-1C77C97630-L000093](../../tests/test_answer_validation.py#L93) | 93 | `"            \"snippet\": \"السعر 90 جنيه\","` | — |
| [SRC-1C77C97630-L000094](../../tests/test_answer_validation.py#L94) | 94 | `"            \"page_fetched\": True,"` | — |
| [SRC-1C77C97630-L000095](../../tests/test_answer_validation.py#L95) | 95 | `"        }],"` | — |
| [SRC-1C77C97630-L000096](../../tests/test_answer_validation.py#L96) | 96 | `"    )"` | — |
| [SRC-1C77C97630-L000097](../../tests/test_answer_validation.py#L97) | 97 | `"    prompt = captured[\"messages\"][0][\"content\"]"` | — |
| [SRC-1C77C97630-L000098](../../tests/test_answer_validation.py#L98) | 98 | `"    assert answer == \"لا تكفي الأدلة.\""` | — |
| [SRC-1C77C97630-L000099](../../tests/test_answer_validation.py#L99) | 99 | `"    assert \"المبالغ والأسعار والنسب والتواريخ والمدد والقياسات\" in prompt"` | — |
| [SRC-1C77C97630-L000100](../../tests/test_answer_validation.py#L100) | 100 | `"    assert \"قيمًا متعارضة\" in prompt"` | — |
| [SRC-1C77C97630-L000101](../../tests/test_answer_validation.py#L101) | 101 | `""` | — |
| [SRC-1C77C97630-L000102](../../tests/test_answer_validation.py#L102) | 102 | `""` | — |
| [SRC-1C77C97630-L000103](../../tests/test_answer_validation.py#L103) | 103 | `"def test_citation_alignment_uses_fetched_page_text_and_flags_weak_overlap():"` | — |
| [SRC-1C77C97630-L000104](../../tests/test_answer_validation.py#L104) | 104 | `"    page_source = {"` | — |
| [SRC-1C77C97630-L000105](../../tests/test_answer_validation.py#L105) | 105 | `"        \"title\": \"Report\","` | — |
| [SRC-1C77C97630-L000106](../../tests/test_answer_validation.py#L106) | 106 | `"        \"snippet\": \"completely unrelated snippet about fruit\","` | — |
| [SRC-1C77C97630-L000107](../../tests/test_answer_validation.py#L107) | 107 | `"        \"page_text\": \"Renewable energy storage costs decreased during the reporting period.\","` | — |
| [SRC-1C77C97630-L000108](../../tests/test_answer_validation.py#L108) | 108 | `"        \"page_fetched\": True,"` | — |
| [SRC-1C77C97630-L000109](../../tests/test_answer_validation.py#L109) | 109 | `"        \"published_at\": \"\","` | — |
| [SRC-1C77C97630-L000110](../../tests/test_answer_validation.py#L110) | 110 | `"    }"` | — |
| [SRC-1C77C97630-L000111](../../tests/test_answer_validation.py#L111) | 111 | `"    good = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000112](../../tests/test_answer_validation.py#L112) | 112 | `"        \"What changed?\","` | — |
| [SRC-1C77C97630-L000113](../../tests/test_answer_validation.py#L113) | 113 | `"        \"Renewable energy storage costs decreased [source 1].\","` | — |
| [SRC-1C77C97630-L000114](../../tests/test_answer_validation.py#L114) | 114 | `"        [page_source],"` | — |
| [SRC-1C77C97630-L000115](../../tests/test_answer_validation.py#L115) | 115 | `"    )"` | — |
| [SRC-1C77C97630-L000116](../../tests/test_answer_validation.py#L116) | 116 | `"    assert good[\"citation_lexical_alignment_method\"] == \"content_word_overlap_heuristic_not_entailment\""` | — |
| [SRC-1C77C97630-L000117](../../tests/test_answer_validation.py#L117) | 117 | `"    assert good[\"citation_lexical_alignment\"][0][\"status\"] == \"lexical_overlap_signal_found\""` | — |
| [SRC-1C77C97630-L000118](../../tests/test_answer_validation.py#L118) | 118 | `"    assert good[\"citation_lexical_alignment\"][0][\"citations\"][0][\"evidence_basis\"] == \"extracted_page_text\""` | — |
| [SRC-1C77C97630-L000119](../../tests/test_answer_validation.py#L119) | 119 | `"    assert good[\"citation_entailment\"] == \"not_checked\""` | — |
| [SRC-1C77C97630-L000120](../../tests/test_answer_validation.py#L120) | 120 | `""` | — |
| [SRC-1C77C97630-L000121](../../tests/test_answer_validation.py#L121) | 121 | `"    weak = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000122](../../tests/test_answer_validation.py#L122) | 122 | `"        \"What happened?\","` | — |
| [SRC-1C77C97630-L000123](../../tests/test_answer_validation.py#L123) | 123 | `"        \"Mango harvest volume rose sharply [source 1].\","` | — |
| [SRC-1C77C97630-L000124](../../tests/test_answer_validation.py#L124) | 124 | `"        [page_source],"` | — |
| [SRC-1C77C97630-L000125](../../tests/test_answer_validation.py#L125) | 125 | `"    )"` | — |
| [SRC-1C77C97630-L000126](../../tests/test_answer_validation.py#L126) | 126 | `"    assert weak[\"citation_lexical_alignment\"][0][\"status\"] == \"weak_lexical_overlap\""` | — |
| [SRC-1C77C97630-L000127](../../tests/test_answer_validation.py#L127) | 127 | `"    assert weak[\"weak_citation_alignment_count\"] == 1"` | — |
| [SRC-1C77C97630-L000128](../../tests/test_answer_validation.py#L128) | 128 | `"    assert weak[\"independent_fact_check\"] is False"` | — |
| [SRC-1C77C97630-L000129](../../tests/test_answer_validation.py#L129) | 129 | `""` | — |
| [SRC-1C77C97630-L000130](../../tests/test_answer_validation.py#L130) | 130 | `""` | — |
| [SRC-1C77C97630-L000131](../../tests/test_answer_validation.py#L131) | 131 | `"def test_snippet_only_citation_alignment_is_labeled_as_snippet_evidence():"` | — |
| [SRC-1C77C97630-L000132](../../tests/test_answer_validation.py#L132) | 132 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000133](../../tests/test_answer_validation.py#L133) | 133 | `"        \"What was reported?\","` | — |
| [SRC-1C77C97630-L000134](../../tests/test_answer_validation.py#L134) | 134 | `"        \"The reported costs changed [المصدر 1].\","` | — |
| [SRC-1C77C97630-L000135](../../tests/test_answer_validation.py#L135) | 135 | `"        [{"` | — |
| [SRC-1C77C97630-L000136](../../tests/test_answer_validation.py#L136) | 136 | `"            \"title\": \"Costs report\","` | — |
| [SRC-1C77C97630-L000137](../../tests/test_answer_validation.py#L137) | 137 | `"            \"snippet\": \"Reported costs changed in the new report.\","` | — |
| [SRC-1C77C97630-L000138](../../tests/test_answer_validation.py#L138) | 138 | `"            \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000139](../../tests/test_answer_validation.py#L139) | 139 | `"        }],"` | — |
| [SRC-1C77C97630-L000140](../../tests/test_answer_validation.py#L140) | 140 | `"    )"` | — |
| [SRC-1C77C97630-L000141](../../tests/test_answer_validation.py#L141) | 141 | `"    assert result[\"citation_lexical_alignment\"][0][\"citations\"][0][\"evidence_basis\"] == \"search_snippet\""` | — |
| [SRC-1C77C97630-L000142](../../tests/test_answer_validation.py#L142) | 142 | `"    assert result[\"citation_entailment\"] == \"not_checked\""` | — |
| [SRC-1C77C97630-L000143](../../tests/test_answer_validation.py#L143) | 143 | `""` | — |
| [SRC-1C77C97630-L000144](../../tests/test_answer_validation.py#L144) | 144 | `""` | — |
| [SRC-1C77C97630-L000145](../../tests/test_answer_validation.py#L145) | 145 | `"def test_bounded_coverage_repair_parses_one_delimited_answer_and_supplies_evidence(monkeypatch):"` | — |
| [SRC-1C77C97630-L000146](../../tests/test_answer_validation.py#L146) | 146 | `"    agent = WebAgent()"` | — |
| [SRC-1C77C97630-L000147](../../tests/test_answer_validation.py#L147) | 147 | `"    captured = {}"` | — |
| [SRC-1C77C97630-L000148](../../tests/test_answer_validation.py#L148) | 148 | `""` | — |
| [SRC-1C77C97630-L000149](../../tests/test_answer_validation.py#L149) | 149 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-1C77C97630-L000150](../../tests/test_answer_validation.py#L150) | 150 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-1C77C97630-L000151](../../tests/test_answer_validation.py#L151) | 151 | `"        return \"<<<OMARAI_COVERAGE_REPAIR>>>تم توضيح السعر والمساحة [المصدر 1].<<<END_OMARAI_COVERAGE_REPAIR>>>\""` | — |
| [SRC-1C77C97630-L000152](../../tests/test_answer_validation.py#L152) | 152 | `""` | — |
| [SRC-1C77C97630-L000153](../../tests/test_answer_validation.py#L153) | 153 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-1C77C97630-L000154](../../tests/test_answer_validation.py#L154) | 154 | `"    repaired = agent._repair_answer_coverage("` | — |
| [SRC-1C77C97630-L000155](../../tests/test_answer_validation.py#L155) | 155 | `"        \"قارن السعر والمساحة\","` | — |
| [SRC-1C77C97630-L000156](../../tests/test_answer_validation.py#L156) | 156 | `"        \"الإجابة الأولية.\","` | — |
| [SRC-1C77C97630-L000157](../../tests/test_answer_validation.py#L157) | 157 | `"        [{"` | — |
| [SRC-1C77C97630-L000158](../../tests/test_answer_validation.py#L158) | 158 | `"            \"title\": \"إعلان\","` | — |
| [SRC-1C77C97630-L000159](../../tests/test_answer_validation.py#L159) | 159 | `"            \"url\": \"https://example.com/listing\","` | — |
| [SRC-1C77C97630-L000160](../../tests/test_answer_validation.py#L160) | 160 | `"            \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000161](../../tests/test_answer_validation.py#L161) | 161 | `"            \"snippet\": \"السعر مذكور والمساحة غير مذكورة\","` | — |
| [SRC-1C77C97630-L000162](../../tests/test_answer_validation.py#L162) | 162 | `"        }],"` | — |
| [SRC-1C77C97630-L000163](../../tests/test_answer_validation.py#L163) | 163 | `"        [\"المساحة\"],"` | — |
| [SRC-1C77C97630-L000164](../../tests/test_answer_validation.py#L164) | 164 | `"    )"` | — |
| [SRC-1C77C97630-L000165](../../tests/test_answer_validation.py#L165) | 165 | `"    assert repaired == \"تم توضيح السعر والمساحة [المصدر 1].\""` | — |
| [SRC-1C77C97630-L000166](../../tests/test_answer_validation.py#L166) | 166 | `"    assert \"المساحة\" in captured[\"messages\"][2][\"content\"]"` | — |
| [SRC-1C77C97630-L000167](../../tests/test_answer_validation.py#L167) | 167 | `"    assert \"السعر مذكور والمساحة غير مذكورة\" in captured[\"messages\"][4][\"content\"]"` | — |
| [SRC-1C77C97630-L000168](../../tests/test_answer_validation.py#L168) | 168 | `"    assert \"مقتطف بحث\" in captured[\"messages\"][4][\"content\"]"` | — |
| [SRC-1C77C97630-L000169](../../tests/test_answer_validation.py#L169) | 169 | `""` | — |
| [SRC-1C77C97630-L000170](../../tests/test_answer_validation.py#L170) | 170 | `""` | — |
| [SRC-1C77C97630-L000171](../../tests/test_answer_validation.py#L171) | 171 | `"def test_bounded_coverage_repair_rejects_missing_or_duplicate_markers(monkeypatch):"` | — |
| [SRC-1C77C97630-L000172](../../tests/test_answer_validation.py#L172) | 172 | `"    agent = WebAgent()"` | — |
| [SRC-1C77C97630-L000173](../../tests/test_answer_validation.py#L173) | 173 | `"    monkeypatch.setattr("` | — |
| [SRC-1C77C97630-L000174](../../tests/test_answer_validation.py#L174) | 174 | `"        agent,"` | — |
| [SRC-1C77C97630-L000175](../../tests/test_answer_validation.py#L175) | 175 | `"        \"_request_completion\","` | — |
| [SRC-1C77C97630-L000176](../../tests/test_answer_validation.py#L176) | 176 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-1C77C97630-L000177](../../tests/test_answer_validation.py#L177) | 177 | `"            \"<<<OMARAI_COVERAGE_REPAIR>>>إجابة<<<END_OMARAI_COVERAGE_REPAIR>>>\""` | — |
| [SRC-1C77C97630-L000178](../../tests/test_answer_validation.py#L178) | 178 | `"            \"<<<END_OMARAI_COVERAGE_REPAIR>>>\""` | — |
| [SRC-1C77C97630-L000179](../../tests/test_answer_validation.py#L179) | 179 | `"        ),"` | — |
| [SRC-1C77C97630-L000180](../../tests/test_answer_validation.py#L180) | 180 | `"    )"` | — |
| [SRC-1C77C97630-L000181](../../tests/test_answer_validation.py#L181) | 181 | `"    with pytest.raises(RuntimeError, match=\"إصلاح تغطية آمن\"):"` | — |
| [SRC-1C77C97630-L000182](../../tests/test_answer_validation.py#L182) | 182 | `"        agent._repair_answer_coverage("` | — |
| [SRC-1C77C97630-L000183](../../tests/test_answer_validation.py#L183) | 183 | `"            \"قارن السعر\","` | — |
| [SRC-1C77C97630-L000184](../../tests/test_answer_validation.py#L184) | 184 | `"            \"مسودة\","` | — |
| [SRC-1C77C97630-L000185](../../tests/test_answer_validation.py#L185) | 185 | `"            [{\"title\": \"مصدر\", \"url\": \"https://example.com\", \"snippet\": \"السعر 100 جنيه\"}],"` | — |
| [SRC-1C77C97630-L000186](../../tests/test_answer_validation.py#L186) | 186 | `"            [\"السعر\"],"` | — |
| [SRC-1C77C97630-L000187](../../tests/test_answer_validation.py#L187) | 187 | `"        )"` | — |
| [SRC-1C77C97630-L000188](../../tests/test_answer_validation.py#L188) | 188 | `""` | — |
| [SRC-1C77C97630-L000189](../../tests/test_answer_validation.py#L189) | 189 | `""` | — |
| [SRC-1C77C97630-L000190](../../tests/test_answer_validation.py#L190) | 190 | `"def test_cited_number_must_appear_in_the_exact_cited_source_not_merely_some_source():"` | — |
| [SRC-1C77C97630-L000191](../../tests/test_answer_validation.py#L191) | 191 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000192](../../tests/test_answer_validation.py#L192) | 192 | `"        \"قارن أسعار المنتجين\","` | — |
| [SRC-1C77C97630-L000193](../../tests/test_answer_validation.py#L193) | 193 | `"        \"سعر المنتج الأول 500 جنيه [المصدر 1].\","` | — |
| [SRC-1C77C97630-L000194](../../tests/test_answer_validation.py#L194) | 194 | `"        ["` | — |
| [SRC-1C77C97630-L000195](../../tests/test_answer_validation.py#L195) | 195 | `"            {"` | — |
| [SRC-1C77C97630-L000196](../../tests/test_answer_validation.py#L196) | 196 | `"                \"title\": \"سعر المنتج الأول\","` | — |
| [SRC-1C77C97630-L000197](../../tests/test_answer_validation.py#L197) | 197 | `"                \"snippet\": \"سعر المنتج الأول 300 جنيه\","` | — |
| [SRC-1C77C97630-L000198](../../tests/test_answer_validation.py#L198) | 198 | `"                \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000199](../../tests/test_answer_validation.py#L199) | 199 | `"            },"` | — |
| [SRC-1C77C97630-L000200](../../tests/test_answer_validation.py#L200) | 200 | `"            {"` | — |
| [SRC-1C77C97630-L000201](../../tests/test_answer_validation.py#L201) | 201 | `"                \"title\": \"سعر المنتج الثاني\","` | — |
| [SRC-1C77C97630-L000202](../../tests/test_answer_validation.py#L202) | 202 | `"                \"snippet\": \"سعر المنتج الثاني 500 جنيه\","` | — |
| [SRC-1C77C97630-L000203](../../tests/test_answer_validation.py#L203) | 203 | `"                \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000204](../../tests/test_answer_validation.py#L204) | 204 | `"            },"` | — |
| [SRC-1C77C97630-L000205](../../tests/test_answer_validation.py#L205) | 205 | `"        ],"` | — |
| [SRC-1C77C97630-L000206](../../tests/test_answer_validation.py#L206) | 206 | `"    )"` | — |
| [SRC-1C77C97630-L000207](../../tests/test_answer_validation.py#L207) | 207 | `""` | — |
| [SRC-1C77C97630-L000208](../../tests/test_answer_validation.py#L208) | 208 | `"    assert result[\"potentially_unsupported_numeric_literals\"] == []"` | — |
| [SRC-1C77C97630-L000209](../../tests/test_answer_validation.py#L209) | 209 | `"    assert result[\"potentially_unsupported_numeric_by_citation_count\"] == 1"` | — |
| [SRC-1C77C97630-L000210](../../tests/test_answer_validation.py#L210) | 210 | `"    cited_check = result[\"citation_numeric_support\"][0]"` | — |
| [SRC-1C77C97630-L000211](../../tests/test_answer_validation.py#L211) | 211 | `"    assert cited_check[\"cited_source_indexes\"] == [1]"` | — |
| [SRC-1C77C97630-L000212](../../tests/test_answer_validation.py#L212) | 212 | `"    assert cited_check[\"potentially_unsupported_numeric_literals\"] == [\"500\"]"` | — |
| [SRC-1C77C97630-L000213](../../tests/test_answer_validation.py#L213) | 213 | `"    assert cited_check[\"status\"] == \"potentially_unsupported_numeric_literals_for_cited_sources\""` | — |
| [SRC-1C77C97630-L000214](../../tests/test_answer_validation.py#L214) | 214 | `""` | — |
| [SRC-1C77C97630-L000215](../../tests/test_answer_validation.py#L215) | 215 | `""` | — |
| [SRC-1C77C97630-L000216](../../tests/test_answer_validation.py#L216) | 216 | `"def test_different_price_values_are_flagged_for_review_not_called_contradictions():"` | — |
| [SRC-1C77C97630-L000217](../../tests/test_answer_validation.py#L217) | 217 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000218](../../tests/test_answer_validation.py#L218) | 218 | `"        \"قارن العروض\","` | — |
| [SRC-1C77C97630-L000219](../../tests/test_answer_validation.py#L219) | 219 | `"        \"العرض الأول أرخص من الثاني [المصدر 1] [المصدر 2].\","` | — |
| [SRC-1C77C97630-L000220](../../tests/test_answer_validation.py#L220) | 220 | `"        ["` | — |
| [SRC-1C77C97630-L000221](../../tests/test_answer_validation.py#L221) | 221 | `"            {"` | — |
| [SRC-1C77C97630-L000222](../../tests/test_answer_validation.py#L222) | 222 | `"                \"title\": \"شقة القاهرة\","` | — |
| [SRC-1C77C97630-L000223](../../tests/test_answer_validation.py#L223) | 223 | `"                \"snippet\": \"السعر 100000 جنيه\","` | — |
| [SRC-1C77C97630-L000224](../../tests/test_answer_validation.py#L224) | 224 | `"                \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000225](../../tests/test_answer_validation.py#L225) | 225 | `"            },"` | — |
| [SRC-1C77C97630-L000226](../../tests/test_answer_validation.py#L226) | 226 | `"            {"` | — |
| [SRC-1C77C97630-L000227](../../tests/test_answer_validation.py#L227) | 227 | `"                \"title\": \"شقة القاهرة\","` | — |
| [SRC-1C77C97630-L000228](../../tests/test_answer_validation.py#L228) | 228 | `"                \"snippet\": \"السعر 120000 جنيه\","` | — |
| [SRC-1C77C97630-L000229](../../tests/test_answer_validation.py#L229) | 229 | `"                \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000230](../../tests/test_answer_validation.py#L230) | 230 | `"            },"` | — |
| [SRC-1C77C97630-L000231](../../tests/test_answer_validation.py#L231) | 231 | `"        ],"` | — |
| [SRC-1C77C97630-L000232](../../tests/test_answer_validation.py#L232) | 232 | `"    )"` | — |
| [SRC-1C77C97630-L000233](../../tests/test_answer_validation.py#L233) | 233 | `""` | — |
| [SRC-1C77C97630-L000234](../../tests/test_answer_validation.py#L234) | 234 | `"    price = next("` | — |
| [SRC-1C77C97630-L000235](../../tests/test_answer_validation.py#L235) | 235 | `"        item for item in result[\"potential_value_discrepancies\"]"` | — |
| [SRC-1C77C97630-L000236](../../tests/test_answer_validation.py#L236) | 236 | `"        if item[\"dimension\"] == \"price_or_cost\""` | — |
| [SRC-1C77C97630-L000237](../../tests/test_answer_validation.py#L237) | 237 | `"    )"` | — |
| [SRC-1C77C97630-L000238](../../tests/test_answer_validation.py#L238) | 238 | `"    assert {item[\"value\"] for item in price[\"values\"]} == {\"100000\", \"120000\"}"` | — |
| [SRC-1C77C97630-L000239](../../tests/test_answer_validation.py#L239) | 239 | `"    assert price[\"status\"] == \"potential_variation_or_conflict_requires_entity_review\""` | — |
| [SRC-1C77C97630-L000240](../../tests/test_answer_validation.py#L240) | 240 | `"    assert \"contradiction\" not in price[\"status\"]"` | — |
| [SRC-1C77C97630-L000241](../../tests/test_answer_validation.py#L241) | 241 | `"    assert result[\"independent_fact_check\"] is False"` | — |
| [SRC-1C77C97630-L000242](../../tests/test_answer_validation.py#L242) | 242 | `""` | — |
| [SRC-1C77C97630-L000243](../../tests/test_answer_validation.py#L243) | 243 | `""` | — |
| [SRC-1C77C97630-L000244](../../tests/test_answer_validation.py#L244) | 244 | `"def test_date_in_answer_missing_from_its_cited_source_is_flagged():"` | — |
| [SRC-1C77C97630-L000245](../../tests/test_answer_validation.py#L245) | 245 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000246](../../tests/test_answer_validation.py#L246) | 246 | `"        \"ما تاريخ التقرير؟\","` | — |
| [SRC-1C77C97630-L000247](../../tests/test_answer_validation.py#L247) | 247 | `"        \"صدر التقرير في 2026 [المصدر 1].\","` | — |
| [SRC-1C77C97630-L000248](../../tests/test_answer_validation.py#L248) | 248 | `"        [{"` | — |
| [SRC-1C77C97630-L000249](../../tests/test_answer_validation.py#L249) | 249 | `"            \"title\": \"تقرير سابق\","` | — |
| [SRC-1C77C97630-L000250](../../tests/test_answer_validation.py#L250) | 250 | `"            \"snippet\": \"تقرير منشور في 2024.\","` | — |
| [SRC-1C77C97630-L000251](../../tests/test_answer_validation.py#L251) | 251 | `"            \"published_at\": \"2024\","` | — |
| [SRC-1C77C97630-L000252](../../tests/test_answer_validation.py#L252) | 252 | `"            \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000253](../../tests/test_answer_validation.py#L253) | 253 | `"        }],"` | — |
| [SRC-1C77C97630-L000254](../../tests/test_answer_validation.py#L254) | 254 | `"    )"` | — |
| [SRC-1C77C97630-L000255](../../tests/test_answer_validation.py#L255) | 255 | `""` | — |
| [SRC-1C77C97630-L000256](../../tests/test_answer_validation.py#L256) | 256 | `"    numeric_check = result[\"citation_numeric_support\"][0]"` | — |
| [SRC-1C77C97630-L000257](../../tests/test_answer_validation.py#L257) | 257 | `"    assert numeric_check[\"potentially_unsupported_numeric_literals\"] == [\"2026\"]"` | — |
| [SRC-1C77C97630-L000258](../../tests/test_answer_validation.py#L258) | 258 | `"    assert numeric_check[\"status\"] == \"potentially_unsupported_numeric_literals_for_cited_sources\""` | — |
| [SRC-1C77C97630-L000259](../../tests/test_answer_validation.py#L259) | 259 | `""` | — |
| [SRC-1C77C97630-L000260](../../tests/test_answer_validation.py#L260) | 260 | `""` | — |
| [SRC-1C77C97630-L000261](../../tests/test_answer_validation.py#L261) | 261 | `"def test_frontend_surfaces_source_specific_number_and_possible_value_discrepancies():"` | — |
| [SRC-1C77C97630-L000262](../../tests/test_answer_validation.py#L262) | 262 | `"    html_path = Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\""` | — |
| [SRC-1C77C97630-L000263](../../tests/test_answer_validation.py#L263) | 263 | `"    html = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-1C77C97630-L000264](../../tests/test_answer_validation.py#L264) | 264 | `""` | — |
| [SRC-1C77C97630-L000265](../../tests/test_answer_validation.py#L265) | 265 | `"    assert \"citation_numeric_support\" in html"` | — |
| [SRC-1C77C97630-L000266](../../tests/test_answer_validation.py#L266) | 266 | `"    assert \"potential_value_discrepancies\" in html"` | — |
| [SRC-1C77C97630-L000267](../../tests/test_answer_validation.py#L267) | 267 | `"    assert \"هذه ليست إثباتًا تلقائيًا لوجود تناقض\" in html"` | — |
| [SRC-1C77C97630-L000268](../../tests/test_answer_validation.py#L268) | 268 | `"    assert \"ليس تحققًا من الحقيقة\" in html"` | — |
| [SRC-1C77C97630-L000269](../../tests/test_answer_validation.py#L269) | 269 | `""` | — |
| [SRC-1C77C97630-L000270](../../tests/test_answer_validation.py#L270) | 270 | `""` | — |
| [SRC-1C77C97630-L000271](../../tests/test_answer_validation.py#L271) | 271 | `"def test_single_coincidental_token_does_not_count_as_citation_support():"` | — |
| [SRC-1C77C97630-L000272](../../tests/test_answer_validation.py#L272) | 272 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000273](../../tests/test_answer_validation.py#L273) | 273 | `"        \"What is the device quality?\","` | — |
| [SRC-1C77C97630-L000274](../../tests/test_answer_validation.py#L274) | 274 | `"        \"Apple is a premium and exceptionally reliable device [source 1].\","` | — |
| [SRC-1C77C97630-L000275](../../tests/test_answer_validation.py#L275) | 275 | `"        [{"` | — |
| [SRC-1C77C97630-L000276](../../tests/test_answer_validation.py#L276) | 276 | `"            \"title\": \"Apple catalog\","` | — |
| [SRC-1C77C97630-L000277](../../tests/test_answer_validation.py#L277) | 277 | `"            \"snippet\": \"Apple product listing\","` | — |
| [SRC-1C77C97630-L000278](../../tests/test_answer_validation.py#L278) | 278 | `"            \"page_text\": \"Apple products are listed with model identifiers and availability.\","` | — |
| [SRC-1C77C97630-L000279](../../tests/test_answer_validation.py#L279) | 279 | `"            \"page_fetched\": True,"` | — |
| [SRC-1C77C97630-L000280](../../tests/test_answer_validation.py#L280) | 280 | `"        }],"` | — |
| [SRC-1C77C97630-L000281](../../tests/test_answer_validation.py#L281) | 281 | `"    )"` | — |
| [SRC-1C77C97630-L000282](../../tests/test_answer_validation.py#L282) | 282 | `"    assert result[\"citation_lexical_alignment\"][0][\"status\"] == \"weak_lexical_overlap\""` | — |
| [SRC-1C77C97630-L000283](../../tests/test_answer_validation.py#L283) | 283 | `"    assert result[\"weak_citation_alignment_count\"] == 1"` | — |
| [SRC-1C77C97630-L000284](../../tests/test_answer_validation.py#L284) | 284 | `"    assert result[\"citation_entailment\"] == \"not_checked\""` | — |
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
| [SRC-3451CC474D-L000005](../../tests/test_api.py#L5) | 5 | `"import re"` | — |
| [SRC-3451CC474D-L000006](../../tests/test_api.py#L6) | 6 | `"import socket"` | — |
| [SRC-3451CC474D-L000007](../../tests/test_api.py#L7) | 7 | `"import threading"` | — |
| [SRC-3451CC474D-L000008](../../tests/test_api.py#L8) | 8 | `"from collections import defaultdict, deque"` | — |
| [SRC-3451CC474D-L000009](../../tests/test_api.py#L9) | 9 | `"from http.server import ThreadingHTTPServer"` | — |
| [SRC-3451CC474D-L000010](../../tests/test_api.py#L10) | 10 | `"from pathlib import Path"` | — |
| [SRC-3451CC474D-L000011](../../tests/test_api.py#L11) | 11 | `"from types import SimpleNamespace"` | — |
| [SRC-3451CC474D-L000012](../../tests/test_api.py#L12) | 12 | `"from urllib.error import HTTPError"` | — |
| [SRC-3451CC474D-L000013](../../tests/test_api.py#L13) | 13 | `"from urllib.request import Request, urlopen"` | — |
| [SRC-3451CC474D-L000014](../../tests/test_api.py#L14) | 14 | `""` | — |
| [SRC-3451CC474D-L000015](../../tests/test_api.py#L15) | 15 | `"import pytest"` | — |
| [SRC-3451CC474D-L000016](../../tests/test_api.py#L16) | 16 | `""` | — |
| [SRC-3451CC474D-L000017](../../tests/test_api.py#L17) | 17 | `"from agents.omarai import LeadStore"` | — |
| [SRC-3451CC474D-L000018](../../tests/test_api.py#L18) | 18 | `"from api.omarai import Handler"` | — |
| [SRC-3451CC474D-L000019](../../tests/test_api.py#L19) | 19 | `""` | — |
| [SRC-3451CC474D-L000020](../../tests/test_api.py#L20) | 20 | `""` | — |
| [SRC-3451CC474D-L000021](../../tests/test_api.py#L21) | 21 | `"@pytest.fixture"` | — |
| [SRC-3451CC474D-L000022](../../tests/test_api.py#L22) | 22 | `"def local_api(tmp_path):"` | — |
| [SRC-3451CC474D-L000023](../../tests/test_api.py#L23) | 23 | `"    \"\"\"Run the real handler on an ephemeral loopback port with an isolated database.\"\"\""` | — |
| [SRC-3451CC474D-L000024](../../tests/test_api.py#L24) | 24 | `"    previous_store = Handler.store"` | — |
| [SRC-3451CC474D-L000025](../../tests/test_api.py#L25) | 25 | `"    Handler.store = LeadStore(tmp_path / \"api-test.sqlite3\")"` | — |
| [SRC-3451CC474D-L000026](../../tests/test_api.py#L26) | 26 | `"    server = ThreadingHTTPServer((\"127.0.0.1\", 0), Handler)"` | — |
| [SRC-3451CC474D-L000027](../../tests/test_api.py#L27) | 27 | `"    thread = threading.Thread(target=server.serve_forever, daemon=True)"` | — |
| [SRC-3451CC474D-L000028](../../tests/test_api.py#L28) | 28 | `"    thread.start()"` | — |
| [SRC-3451CC474D-L000029](../../tests/test_api.py#L29) | 29 | `"    try:"` | — |
| [SRC-3451CC474D-L000030](../../tests/test_api.py#L30) | 30 | `"        yield f\"http://127.0.0.1:{server.server_port}\""` | — |
| [SRC-3451CC474D-L000031](../../tests/test_api.py#L31) | 31 | `"    finally:"` | — |
| [SRC-3451CC474D-L000032](../../tests/test_api.py#L32) | 32 | `"        server.shutdown()"` | — |
| [SRC-3451CC474D-L000033](../../tests/test_api.py#L33) | 33 | `"        server.server_close()"` | — |
| [SRC-3451CC474D-L000034](../../tests/test_api.py#L34) | 34 | `"        thread.join(timeout=3)"` | — |
| [SRC-3451CC474D-L000035](../../tests/test_api.py#L35) | 35 | `"        Handler.store = previous_store"` | — |
| [SRC-3451CC474D-L000036](../../tests/test_api.py#L36) | 36 | `""` | — |
| [SRC-3451CC474D-L000037](../../tests/test_api.py#L37) | 37 | `""` | — |
| [SRC-3451CC474D-L000038](../../tests/test_api.py#L38) | 38 | `"def request_json(base, path, method=\"GET\", payload=None, headers=None):"` | — |
| [SRC-3451CC474D-L000039](../../tests/test_api.py#L39) | 39 | `"    body = None if payload is None else json.dumps(payload, ensure_ascii=False).encode(\"utf-8\")"` | — |
| [SRC-3451CC474D-L000040](../../tests/test_api.py#L40) | 40 | `"    request_headers = dict(headers or {})"` | — |
| [SRC-3451CC474D-L000041](../../tests/test_api.py#L41) | 41 | `"    if body is not None and \"Content-Type\" not in request_headers:"` | — |
| [SRC-3451CC474D-L000042](../../tests/test_api.py#L42) | 42 | `"        request_headers[\"Content-Type\"] = \"application/json\""` | — |
| [SRC-3451CC474D-L000043](../../tests/test_api.py#L43) | 43 | `"    request = Request(base + path, data=body, method=method, headers=request_headers)"` | — |
| [SRC-3451CC474D-L000044](../../tests/test_api.py#L44) | 44 | `"    try:"` | — |
| [SRC-3451CC474D-L000045](../../tests/test_api.py#L45) | 45 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000046](../../tests/test_api.py#L46) | 46 | `"            return response.status, json.loads(response.read().decode(\"utf-8\"))"` | — |
| [SRC-3451CC474D-L000047](../../tests/test_api.py#L47) | 47 | `"    except HTTPError as error:"` | — |
| [SRC-3451CC474D-L000048](../../tests/test_api.py#L48) | 48 | `"        return error.code, json.loads(error.read().decode(\"utf-8\"))"` | — |
| [SRC-3451CC474D-L000049](../../tests/test_api.py#L49) | 49 | `""` | — |
| [SRC-3451CC474D-L000050](../../tests/test_api.py#L50) | 50 | `""` | — |
| [SRC-3451CC474D-L000051](../../tests/test_api.py#L51) | 51 | `"def test_api_health_analyze_save_duplicate_list_and_status(local_api):"` | — |
| [SRC-3451CC474D-L000052](../../tests/test_api.py#L52) | 52 | `"    status, health = request_json(local_api, \"/api/health\")"` | — |
| [SRC-3451CC474D-L000053](../../tests/test_api.py#L53) | 53 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000054](../../tests/test_api.py#L54) | 54 | `"    assert health[\"app\"] == \"Omarai\""` | — |
| [SRC-3451CC474D-L000055](../../tests/test_api.py#L55) | 55 | `"    assert health[\"mode\"] == \"web-research\""` | — |
| [SRC-3451CC474D-L000056](../../tests/test_api.py#L56) | 56 | `"    assert health[\"agent\"][\"verification_scope\"][\"live_network_checks_performed\"] is False"` | — |
| [SRC-3451CC474D-L000057](../../tests/test_api.py#L57) | 57 | `"    assert health[\"agent\"][\"verification_scope\"][\"live_diagnostics_endpoint\"] == \"POST /api/diagnostics\""` | — |
| [SRC-3451CC474D-L000058](../../tests/test_api.py#L58) | 58 | `""` | — |
| [SRC-3451CC474D-L000059](../../tests/test_api.py#L59) | 59 | `"    text = \"بدور على شقة في التجمع الخامس وممكن معاينة\""` | — |
| [SRC-3451CC474D-L000060](../../tests/test_api.py#L60) | 60 | `"    status, assessment = request_json("` | — |
| [SRC-3451CC474D-L000061](../../tests/test_api.py#L61) | 61 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000062](../../tests/test_api.py#L62) | 62 | `"        \"/api/analyze\","` | — |
| [SRC-3451CC474D-L000063](../../tests/test_api.py#L63) | 63 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000064](../../tests/test_api.py#L64) | 64 | `"        payload={\"text\": text, \"product_terms\": [\"شقة\"], \"location_terms\": [\"التجمع الخامس\"]},"` | — |
| [SRC-3451CC474D-L000065](../../tests/test_api.py#L65) | 65 | `"    )"` | — |
| [SRC-3451CC474D-L000066](../../tests/test_api.py#L66) | 66 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000067](../../tests/test_api.py#L67) | 67 | `"    assert assessment[\"label\"] == \"high_intent\""` | — |
| [SRC-3451CC474D-L000068](../../tests/test_api.py#L68) | 68 | `"    assert {item[\"category\"] for item in assessment[\"matched_signals\"]} >= {"` | — |
| [SRC-3451CC474D-L000069](../../tests/test_api.py#L69) | 69 | `"        \"high\", \"next_step\", \"product_context\", \"location_context\""` | — |
| [SRC-3451CC474D-L000070](../../tests/test_api.py#L70) | 70 | `"    }"` | — |
| [SRC-3451CC474D-L000071](../../tests/test_api.py#L71) | 71 | `""` | — |
| [SRC-3451CC474D-L000072](../../tests/test_api.py#L72) | 72 | `"    payload = {"` | — |
| [SRC-3451CC474D-L000073](../../tests/test_api.py#L73) | 73 | `"        \"text\": text,"` | — |
| [SRC-3451CC474D-L000074](../../tests/test_api.py#L74) | 74 | `"        \"source_url\": \"https://example.com/posts/123\","` | — |
| [SRC-3451CC474D-L000075](../../tests/test_api.py#L75) | 75 | `"        \"platform\": \"Public website\","` | — |
| [SRC-3451CC474D-L000076](../../tests/test_api.py#L76) | 76 | `"        \"product_terms\": [\"شقة\"],"` | — |
| [SRC-3451CC474D-L000077](../../tests/test_api.py#L77) | 77 | `"        \"location_terms\": [\"التجمع الخامس\"],"` | — |
| [SRC-3451CC474D-L000078](../../tests/test_api.py#L78) | 78 | `"    }"` | — |
| [SRC-3451CC474D-L000079](../../tests/test_api.py#L79) | 79 | `"    status, saved = request_json(local_api, \"/api/leads\", method=\"POST\", payload=payload)"` | — |
| [SRC-3451CC474D-L000080](../../tests/test_api.py#L80) | 80 | `"    assert status == 201"` | — |
| [SRC-3451CC474D-L000081](../../tests/test_api.py#L81) | 81 | `"    assert saved[\"created\"] is True"` | — |
| [SRC-3451CC474D-L000082](../../tests/test_api.py#L82) | 82 | `"    assert saved[\"lead\"][\"assessment\"][\"label\"] == \"high_intent\""` | — |
| [SRC-3451CC474D-L000083](../../tests/test_api.py#L83) | 83 | `"    assert \"product_context\" in {"` | — |
| [SRC-3451CC474D-L000084](../../tests/test_api.py#L84) | 84 | `"        item[\"category\"] for item in saved[\"lead\"][\"assessment\"][\"matched_signals\"]"` | — |
| [SRC-3451CC474D-L000085](../../tests/test_api.py#L85) | 85 | `"    }"` | — |
| [SRC-3451CC474D-L000086](../../tests/test_api.py#L86) | 86 | `"    status, duplicate = request_json(local_api, \"/api/leads\", method=\"POST\", payload=payload)"` | — |
| [SRC-3451CC474D-L000087](../../tests/test_api.py#L87) | 87 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000088](../../tests/test_api.py#L88) | 88 | `"    assert duplicate[\"created\"] is False"` | — |
| [SRC-3451CC474D-L000089](../../tests/test_api.py#L89) | 89 | `""` | — |
| [SRC-3451CC474D-L000090](../../tests/test_api.py#L90) | 90 | `"    status, listing = request_json(local_api, \"/api/leads?limit=25\")"` | — |
| [SRC-3451CC474D-L000091](../../tests/test_api.py#L91) | 91 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000092](../../tests/test_api.py#L92) | 92 | `"    assert listing[\"count\"] == 1"` | — |
| [SRC-3451CC474D-L000093](../../tests/test_api.py#L93) | 93 | `"    lead_id = listing[\"leads\"][0][\"id\"]"` | — |
| [SRC-3451CC474D-L000094](../../tests/test_api.py#L94) | 94 | `""` | — |
| [SRC-3451CC474D-L000095](../../tests/test_api.py#L95) | 95 | `"    status, changed = request_json("` | — |
| [SRC-3451CC474D-L000096](../../tests/test_api.py#L96) | 96 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000097](../../tests/test_api.py#L97) | 97 | `"        f\"/api/leads/{lead_id}/status\","` | — |
| [SRC-3451CC474D-L000098](../../tests/test_api.py#L98) | 98 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000099](../../tests/test_api.py#L99) | 99 | `"        payload={\"status\": \"qualified\"},"` | — |
| [SRC-3451CC474D-L000100](../../tests/test_api.py#L100) | 100 | `"    )"` | — |
| [SRC-3451CC474D-L000101](../../tests/test_api.py#L101) | 101 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000102](../../tests/test_api.py#L102) | 102 | `"    assert changed[\"lead\"][\"status\"] == \"qualified\""` | — |
| [SRC-3451CC474D-L000103](../../tests/test_api.py#L103) | 103 | `""` | — |
| [SRC-3451CC474D-L000104](../../tests/test_api.py#L104) | 104 | `"    status, stats = request_json("` | — |
| [SRC-3451CC474D-L000105](../../tests/test_api.py#L105) | 105 | `"        local_api, \"/api/ask\", method=\"POST\", payload={\"question\": \"كام عميل عندي؟\"}"` | — |
| [SRC-3451CC474D-L000106](../../tests/test_api.py#L106) | 106 | `"    )"` | — |
| [SRC-3451CC474D-L000107](../../tests/test_api.py#L107) | 107 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000108](../../tests/test_api.py#L108) | 108 | `"    assert stats[\"kind\"] == \"local_statistics\""` | — |
| [SRC-3451CC474D-L000109](../../tests/test_api.py#L109) | 109 | `"    assert \"1 إشارة\" in stats[\"answer\"]"` | — |
| [SRC-3451CC474D-L000110](../../tests/test_api.py#L110) | 110 | `""` | — |
| [SRC-3451CC474D-L000111](../../tests/test_api.py#L111) | 111 | `"    status, recommendation = request_json("` | — |
| [SRC-3451CC474D-L000112](../../tests/test_api.py#L112) | 112 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000113](../../tests/test_api.py#L113) | 113 | `"        \"/api/ask\","` | — |
| [SRC-3451CC474D-L000114](../../tests/test_api.py#L114) | 114 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000115](../../tests/test_api.py#L115) | 115 | `"        payload={\"question\": \"مين أفضل إشارة أراجعها؟\"},"` | — |
| [SRC-3451CC474D-L000116](../../tests/test_api.py#L116) | 116 | `"    )"` | — |
| [SRC-3451CC474D-L000117](../../tests/test_api.py#L117) | 117 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000118](../../tests/test_api.py#L118) | 118 | `"    assert recommendation[\"kind\"] == \"lead_recommendation\""` | — |
| [SRC-3451CC474D-L000119](../../tests/test_api.py#L119) | 119 | `"    assert payload[\"source_url\"] in recommendation[\"answer\"]"` | — |
| [SRC-3451CC474D-L000120](../../tests/test_api.py#L120) | 120 | `""` | — |
| [SRC-3451CC474D-L000121](../../tests/test_api.py#L121) | 121 | `""` | — |
| [SRC-3451CC474D-L000122](../../tests/test_api.py#L122) | 122 | `"def test_api_rejects_invalid_filters_and_request_shapes(local_api):"` | — |
| [SRC-3451CC474D-L000123](../../tests/test_api.py#L123) | 123 | `"    status, error = request_json(local_api, \"/api/leads?limit=not-a-number\")"` | — |
| [SRC-3451CC474D-L000124](../../tests/test_api.py#L124) | 124 | `"    assert status == 400"` | — |
| [SRC-3451CC474D-L000125](../../tests/test_api.py#L125) | 125 | `"    assert \"limit\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000126](../../tests/test_api.py#L126) | 126 | `""` | — |
| [SRC-3451CC474D-L000127](../../tests/test_api.py#L127) | 127 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000128](../../tests/test_api.py#L128) | 128 | `"        local_api, \"/api/analyze\", method=\"POST\", payload=[\"not\", \"an\", \"object\"]"` | — |
| [SRC-3451CC474D-L000129](../../tests/test_api.py#L129) | 129 | `"    )"` | — |
| [SRC-3451CC474D-L000130](../../tests/test_api.py#L130) | 130 | `"    assert status == 400"` | — |
| [SRC-3451CC474D-L000131](../../tests/test_api.py#L131) | 131 | `"    assert \"object\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000132](../../tests/test_api.py#L132) | 132 | `""` | — |
| [SRC-3451CC474D-L000133](../../tests/test_api.py#L133) | 133 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000134](../../tests/test_api.py#L134) | 134 | `"        local_api, \"/api/ask\", method=\"POST\", payload={\"question\": \"\"}"` | — |
| [SRC-3451CC474D-L000135](../../tests/test_api.py#L135) | 135 | `"    )"` | — |
| [SRC-3451CC474D-L000136](../../tests/test_api.py#L136) | 136 | `"    assert status == 400"` | — |
| [SRC-3451CC474D-L000137](../../tests/test_api.py#L137) | 137 | `"    assert \"question\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000138](../../tests/test_api.py#L138) | 138 | `""` | — |
| [SRC-3451CC474D-L000139](../../tests/test_api.py#L139) | 139 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000140](../../tests/test_api.py#L140) | 140 | `"        local_api, \"/api/leads\", method=\"POST\", payload={"` | — |
| [SRC-3451CC474D-L000141](../../tests/test_api.py#L141) | 141 | `"            \"text\": \"بدور على شقة\", \"source_url\": \"file:///private/data\", \"platform\": \"manual\""` | — |
| [SRC-3451CC474D-L000142](../../tests/test_api.py#L142) | 142 | `"        }"` | — |
| [SRC-3451CC474D-L000143](../../tests/test_api.py#L143) | 143 | `"    )"` | — |
| [SRC-3451CC474D-L000144](../../tests/test_api.py#L144) | 144 | `"    assert status == 400"` | — |
| [SRC-3451CC474D-L000145](../../tests/test_api.py#L145) | 145 | `"    assert \"absolute\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000146](../../tests/test_api.py#L146) | 146 | `""` | — |
| [SRC-3451CC474D-L000147](../../tests/test_api.py#L147) | 147 | `""` | — |
| [SRC-3451CC474D-L000148](../../tests/test_api.py#L148) | 148 | `"def test_api_blocks_non_json_and_cross_origin_posts(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000149](../../tests/test_api.py#L149) | 149 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000150](../../tests/test_api.py#L150) | 150 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000151](../../tests/test_api.py#L151) | 151 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000152](../../tests/test_api.py#L152) | 152 | `"        \"/api/ask\","` | — |
| [SRC-3451CC474D-L000153](../../tests/test_api.py#L153) | 153 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000154](../../tests/test_api.py#L154) | 154 | `"        payload={\"question\": \"كام عميل؟\"},"` | — |
| [SRC-3451CC474D-L000155](../../tests/test_api.py#L155) | 155 | `"        headers={\"Content-Type\": \"text/plain\"},"` | — |
| [SRC-3451CC474D-L000156](../../tests/test_api.py#L156) | 156 | `"    )"` | — |
| [SRC-3451CC474D-L000157](../../tests/test_api.py#L157) | 157 | `"    assert status == 415"` | — |
| [SRC-3451CC474D-L000158](../../tests/test_api.py#L158) | 158 | `"    assert \"Content-Type\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000159](../../tests/test_api.py#L159) | 159 | `""` | — |
| [SRC-3451CC474D-L000160](../../tests/test_api.py#L160) | 160 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000161](../../tests/test_api.py#L161) | 161 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000162](../../tests/test_api.py#L162) | 162 | `"        \"/api/ask\","` | — |
| [SRC-3451CC474D-L000163](../../tests/test_api.py#L163) | 163 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000164](../../tests/test_api.py#L164) | 164 | `"        payload={\"question\": \"كام عميل؟\"},"` | — |
| [SRC-3451CC474D-L000165](../../tests/test_api.py#L165) | 165 | `"        headers={\"Origin\": \"https://attacker.example\"},"` | — |
| [SRC-3451CC474D-L000166](../../tests/test_api.py#L166) | 166 | `"    )"` | — |
| [SRC-3451CC474D-L000167](../../tests/test_api.py#L167) | 167 | `"    assert status == 403"` | — |
| [SRC-3451CC474D-L000168](../../tests/test_api.py#L168) | 168 | `"    assert \"cross-origin\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000169](../../tests/test_api.py#L169) | 169 | `""` | — |
| [SRC-3451CC474D-L000170](../../tests/test_api.py#L170) | 170 | `""` | — |
| [SRC-3451CC474D-L000171](../../tests/test_api.py#L171) | 171 | `"def test_configured_frontend_origin_supports_preflight_and_post(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000172](../../tests/test_api.py#L172) | 172 | `"    origin = \"https://frontend.example\""` | — |
| [SRC-3451CC474D-L000173](../../tests/test_api.py#L173) | 173 | `"    monkeypatch.setenv(\"OMARAI_ALLOWED_ORIGINS\", origin)"` | — |
| [SRC-3451CC474D-L000174](../../tests/test_api.py#L174) | 174 | `""` | — |
| [SRC-3451CC474D-L000175](../../tests/test_api.py#L175) | 175 | `"    preflight = Request("` | — |
| [SRC-3451CC474D-L000176](../../tests/test_api.py#L176) | 176 | `"        local_api + \"/api/agent\","` | — |
| [SRC-3451CC474D-L000177](../../tests/test_api.py#L177) | 177 | `"        method=\"OPTIONS\","` | — |
| [SRC-3451CC474D-L000178](../../tests/test_api.py#L178) | 178 | `"        headers={"` | — |
| [SRC-3451CC474D-L000179](../../tests/test_api.py#L179) | 179 | `"            \"Origin\": origin,"` | — |
| [SRC-3451CC474D-L000180](../../tests/test_api.py#L180) | 180 | `"            \"Access-Control-Request-Method\": \"POST\","` | — |
| [SRC-3451CC474D-L000181](../../tests/test_api.py#L181) | 181 | `"            \"Access-Control-Request-Headers\": \"authorization,content-type\","` | — |
| [SRC-3451CC474D-L000182](../../tests/test_api.py#L182) | 182 | `"        },"` | — |
| [SRC-3451CC474D-L000183](../../tests/test_api.py#L183) | 183 | `"    )"` | — |
| [SRC-3451CC474D-L000184](../../tests/test_api.py#L184) | 184 | `"    with urlopen(preflight, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000185](../../tests/test_api.py#L185) | 185 | `"        assert response.status == 204"` | — |
| [SRC-3451CC474D-L000186](../../tests/test_api.py#L186) | 186 | `"        assert response.headers.get(\"Access-Control-Allow-Origin\") == origin"` | — |
| [SRC-3451CC474D-L000187](../../tests/test_api.py#L187) | 187 | `"        assert response.headers.get(\"Access-Control-Allow-Methods\") == \"GET, POST, OPTIONS\""` | — |
| [SRC-3451CC474D-L000188](../../tests/test_api.py#L188) | 188 | `"        assert response.headers.get(\"Access-Control-Allow-Headers\") == \"Authorization, Content-Type\""` | — |
| [SRC-3451CC474D-L000189](../../tests/test_api.py#L189) | 189 | `""` | — |
| [SRC-3451CC474D-L000190](../../tests/test_api.py#L190) | 190 | `"    body = json.dumps({\"question\": \"مين أفضل إشارة أراجعها؟\"}, ensure_ascii=False).encode(\"utf-8\")"` | — |
| [SRC-3451CC474D-L000191](../../tests/test_api.py#L191) | 191 | `"    post = Request("` | — |
| [SRC-3451CC474D-L000192](../../tests/test_api.py#L192) | 192 | `"        local_api + \"/api/ask\","` | — |
| [SRC-3451CC474D-L000193](../../tests/test_api.py#L193) | 193 | `"        data=body,"` | — |
| [SRC-3451CC474D-L000194](../../tests/test_api.py#L194) | 194 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000195](../../tests/test_api.py#L195) | 195 | `"        headers={\"Content-Type\": \"application/json\", \"Origin\": origin},"` | — |
| [SRC-3451CC474D-L000196](../../tests/test_api.py#L196) | 196 | `"    )"` | — |
| [SRC-3451CC474D-L000197](../../tests/test_api.py#L197) | 197 | `"    with urlopen(post, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000198](../../tests/test_api.py#L198) | 198 | `"        payload = json.loads(response.read().decode(\"utf-8\"))"` | — |
| [SRC-3451CC474D-L000199](../../tests/test_api.py#L199) | 199 | `"        assert response.status == 200"` | — |
| [SRC-3451CC474D-L000200](../../tests/test_api.py#L200) | 200 | `"        assert response.headers.get(\"Access-Control-Allow-Origin\") == origin"` | — |
| [SRC-3451CC474D-L000201](../../tests/test_api.py#L201) | 201 | `"        assert payload[\"kind\"] == \"no_data\""` | — |
| [SRC-3451CC474D-L000202](../../tests/test_api.py#L202) | 202 | `""` | — |
| [SRC-3451CC474D-L000203](../../tests/test_api.py#L203) | 203 | `""` | — |
| [SRC-3451CC474D-L000204](../../tests/test_api.py#L204) | 204 | `"def test_preflight_rejects_unconfigured_origin(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000205](../../tests/test_api.py#L205) | 205 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000206](../../tests/test_api.py#L206) | 206 | `"    preflight = Request("` | — |
| [SRC-3451CC474D-L000207](../../tests/test_api.py#L207) | 207 | `"        local_api + \"/api/agent\","` | — |
| [SRC-3451CC474D-L000208](../../tests/test_api.py#L208) | 208 | `"        method=\"OPTIONS\","` | — |
| [SRC-3451CC474D-L000209](../../tests/test_api.py#L209) | 209 | `"        headers={"` | — |
| [SRC-3451CC474D-L000210](../../tests/test_api.py#L210) | 210 | `"            \"Origin\": \"https://attacker.example\","` | — |
| [SRC-3451CC474D-L000211](../../tests/test_api.py#L211) | 211 | `"            \"Access-Control-Request-Method\": \"POST\","` | — |
| [SRC-3451CC474D-L000212](../../tests/test_api.py#L212) | 212 | `"        },"` | — |
| [SRC-3451CC474D-L000213](../../tests/test_api.py#L213) | 213 | `"    )"` | — |
| [SRC-3451CC474D-L000214](../../tests/test_api.py#L214) | 214 | `"    with pytest.raises(HTTPError) as error:"` | — |
| [SRC-3451CC474D-L000215](../../tests/test_api.py#L215) | 215 | `"        urlopen(preflight, timeout=3)"` | — |
| [SRC-3451CC474D-L000216](../../tests/test_api.py#L216) | 216 | `"    assert error.value.code == 403"` | — |
| [SRC-3451CC474D-L000217](../../tests/test_api.py#L217) | 217 | `""` | — |
| [SRC-3451CC474D-L000218](../../tests/test_api.py#L218) | 218 | `""` | — |
| [SRC-3451CC474D-L000219](../../tests/test_api.py#L219) | 219 | `"def test_ask_is_honest_when_database_is_empty(local_api):"` | — |
| [SRC-3451CC474D-L000220](../../tests/test_api.py#L220) | 220 | `"    status, answer = request_json("` | — |
| [SRC-3451CC474D-L000221](../../tests/test_api.py#L221) | 221 | `"        local_api, \"/api/ask\", method=\"POST\", payload={\"question\": \"مين أفضل إشارة أراجعها؟\"}"` | — |
| [SRC-3451CC474D-L000222](../../tests/test_api.py#L222) | 222 | `"    )"` | — |
| [SRC-3451CC474D-L000223](../../tests/test_api.py#L223) | 223 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000224](../../tests/test_api.py#L224) | 224 | `"    assert answer[\"kind\"] == \"no_data\""` | — |
| [SRC-3451CC474D-L000225](../../tests/test_api.py#L225) | 225 | `"    assert \"لا توجد إشارة\" in answer[\"answer\"]"` | — |
| [SRC-3451CC474D-L000226](../../tests/test_api.py#L226) | 226 | `""` | — |
| [SRC-3451CC474D-L000227](../../tests/test_api.py#L227) | 227 | `""` | — |
| [SRC-3451CC474D-L000228](../../tests/test_api.py#L228) | 228 | `""` | — |
| [SRC-3451CC474D-L000229](../../tests/test_api.py#L229) | 229 | `"def test_web_agent_endpoint_uses_agent_result(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000230](../../tests/test_api.py#L230) | 230 | `"    from api.omarai import WebAgent"` | — |
| [SRC-3451CC474D-L000231](../../tests/test_api.py#L231) | 231 | `""` | — |
| [SRC-3451CC474D-L000232](../../tests/test_api.py#L232) | 232 | `"    def fake_answer(self, question, history=None):"` | — |
| [SRC-3451CC474D-L000233](../../tests/test_api.py#L233) | 233 | `"        return {"` | — |
| [SRC-3451CC474D-L000234](../../tests/test_api.py#L234) | 234 | `"            \"answer\": \"إجابة اختبار [المصدر 1]\","` | — |
| [SRC-3451CC474D-L000235](../../tests/test_api.py#L235) | 235 | `"            \"question\": question,"` | — |
| [SRC-3451CC474D-L000236](../../tests/test_api.py#L236) | 236 | `"            \"search_query\": question,"` | — |
| [SRC-3451CC474D-L000237](../../tests/test_api.py#L237) | 237 | `"            \"sources\": [{\"title\": \"مصدر\", \"url\": \"https://example.com\", \"snippet\": \"نص\", \"page_fetched\": False}],"` | — |
| [SRC-3451CC474D-L000238](../../tests/test_api.py#L238) | 238 | `"            \"used_language_model\": True,"` | — |
| [SRC-3451CC474D-L000239](../../tests/test_api.py#L239) | 239 | `"            \"used_web_search\": True,"` | — |
| [SRC-3451CC474D-L000240](../../tests/test_api.py#L240) | 240 | `"            \"warnings\": [],"` | — |
| [SRC-3451CC474D-L000241](../../tests/test_api.py#L241) | 241 | `"            \"kind\": \"web_research\","` | — |
| [SRC-3451CC474D-L000242](../../tests/test_api.py#L242) | 242 | `"        }"` | — |
| [SRC-3451CC474D-L000243](../../tests/test_api.py#L243) | 243 | `""` | — |
| [SRC-3451CC474D-L000244](../../tests/test_api.py#L244) | 244 | `"    monkeypatch.setattr(WebAgent, \"answer\", fake_answer)"` | — |
| [SRC-3451CC474D-L000245](../../tests/test_api.py#L245) | 245 | `"    status, response = request_json("` | — |
| [SRC-3451CC474D-L000246](../../tests/test_api.py#L246) | 246 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000247](../../tests/test_api.py#L247) | 247 | `"        \"/api/agent\","` | — |
| [SRC-3451CC474D-L000248](../../tests/test_api.py#L248) | 248 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000249](../../tests/test_api.py#L249) | 249 | `"        payload={\"question\": \"ابحث عن موضوع\", \"history\": []},"` | — |
