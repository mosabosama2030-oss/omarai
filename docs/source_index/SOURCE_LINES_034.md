# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **034**
- سجلات الأسطر: **800**
- النطاق: SRC-B3062EB677-L000250 إلى SRC-3451CC474D-L000409
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-B3062EB677 — [tests/test_answer_quality_runner.py](../../tests/test_answer_quality_runner.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-B3062EB677-L000250](../../tests/test_answer_quality_runner.py#L250) | 250 | `"        {"` | — |
| [SRC-B3062EB677-L000251](../../tests/test_answer_quality_runner.py#L251) | 251 | `"            \"search_report\": {"` | — |
| [SRC-B3062EB677-L000252](../../tests/test_answer_quality_runner.py#L252) | 252 | `"                \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-B3062EB677-L000253](../../tests/test_answer_quality_runner.py#L253) | 253 | `"                \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-B3062EB677-L000254](../../tests/test_answer_quality_runner.py#L254) | 254 | `"                \"model_calls\": [{"` | — |
| [SRC-B3062EB677-L000255](../../tests/test_answer_quality_runner.py#L255) | 255 | `"                    \"requested_model\": \"test/model\","` | — |
| [SRC-B3062EB677-L000256](../../tests/test_answer_quality_runner.py#L256) | 256 | `"                    \"provider_usage\": {"` | — |
| [SRC-B3062EB677-L000257](../../tests/test_answer_quality_runner.py#L257) | 257 | `"                        \"prompt_tokens\": 10,"` | — |
| [SRC-B3062EB677-L000258](../../tests/test_answer_quality_runner.py#L258) | 258 | `"                        \"completion_tokens\": 20,"` | — |
| [SRC-B3062EB677-L000259](../../tests/test_answer_quality_runner.py#L259) | 259 | `"                        \"total_tokens\": 30,"` | — |
| [SRC-B3062EB677-L000260](../../tests/test_answer_quality_runner.py#L260) | 260 | `"                        \"cost_usd\": 0.0008,"` | — |
| [SRC-B3062EB677-L000261](../../tests/test_answer_quality_runner.py#L261) | 261 | `"                    },"` | — |
| [SRC-B3062EB677-L000262](../../tests/test_answer_quality_runner.py#L262) | 262 | `"                }],"` | — |
| [SRC-B3062EB677-L000263](../../tests/test_answer_quality_runner.py#L263) | 263 | `"            },"` | — |
| [SRC-B3062EB677-L000264](../../tests/test_answer_quality_runner.py#L264) | 264 | `"            \"model_calls\": [],"` | — |
| [SRC-B3062EB677-L000265](../../tests/test_answer_quality_runner.py#L265) | 265 | `"            \"sources\": [{\"url\": \"https://example.org\"}],"` | — |
| [SRC-B3062EB677-L000266](../../tests/test_answer_quality_runner.py#L266) | 266 | `"        },"` | — |
| [SRC-B3062EB677-L000267](../../tests/test_answer_quality_runner.py#L267) | 267 | `"        expected_strategy=\"web_search\","` | — |
| [SRC-B3062EB677-L000268](../../tests/test_answer_quality_runner.py#L268) | 268 | `"        transport_ok=True,"` | — |
| [SRC-B3062EB677-L000269](../../tests/test_answer_quality_runner.py#L269) | 269 | `"    )"` | — |
| [SRC-B3062EB677-L000270](../../tests/test_answer_quality_runner.py#L270) | 270 | `"    assert successful_search[\"tool_status\"] == \"SUCCESS_WITH_USABLE_RESULTS\""` | — |
| [SRC-B3062EB677-L000271](../../tests/test_answer_quality_runner.py#L271) | 271 | `"    assert successful_search[\"source_count\"] == 1"` | — |
| [SRC-B3062EB677-L000272](../../tests/test_answer_quality_runner.py#L272) | 272 | `"    assert successful_search[\"provider_reported_model_cost_usd\"] == 0.0008"` | — |
| [SRC-B3062EB677-L000273](../../tests/test_answer_quality_runner.py#L273) | 273 | `"    assert successful_search[\"provider_reported_model_cost_status\"] == \"COMPLETE_FOR_RETURNED_MODEL_CALLS\""` | — |
| [SRC-B3062EB677-L000274](../../tests/test_answer_quality_runner.py#L274) | 274 | `""` | — |
| [SRC-B3062EB677-L000275](../../tests/test_answer_quality_runner.py#L275) | 275 | `""` | — |
| [SRC-B3062EB677-L000276](../../tests/test_answer_quality_runner.py#L276) | 276 | `"def test_request_cost_ledger_accepts_explicit_full_request_usd_reconciliation(tmp_path):"` | — |
| [SRC-B3062EB677-L000277](../../tests/test_answer_quality_runner.py#L277) | 277 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000278](../../tests/test_answer_quality_runner.py#L278) | 278 | `"    ledger_path = tmp_path / \"cost-ledger.json\""` | — |
| [SRC-B3062EB677-L000279](../../tests/test_answer_quality_runner.py#L279) | 279 | `"    ledger_path.write_text("` | — |
| [SRC-B3062EB677-L000280](../../tests/test_answer_quality_runner.py#L280) | 280 | `"        json.dumps({"` | — |
| [SRC-B3062EB677-L000281](../../tests/test_answer_quality_runner.py#L281) | 281 | `"            \"schema_version\": \"1.0\","` | — |
| [SRC-B3062EB677-L000282](../../tests/test_answer_quality_runner.py#L282) | 282 | `"            \"currency\": \"USD\","` | — |
| [SRC-B3062EB677-L000283](../../tests/test_answer_quality_runner.py#L283) | 283 | `"            \"scope\": \"complete_request\","` | — |
| [SRC-B3062EB677-L000284](../../tests/test_answer_quality_runner.py#L284) | 284 | `"            \"source\": \"provider usage export reviewed by operator\","` | — |
| [SRC-B3062EB677-L000285](../../tests/test_answer_quality_runner.py#L285) | 285 | `"            \"costs\": [{\"case_id\": \"AQ-001\", \"cost_usd\": 0.0042}],"` | — |
| [SRC-B3062EB677-L000286](../../tests/test_answer_quality_runner.py#L286) | 286 | `"        }),"` | — |
| [SRC-B3062EB677-L000287](../../tests/test_answer_quality_runner.py#L287) | 287 | `"        encoding=\"utf-8\","` | — |
| [SRC-B3062EB677-L000288](../../tests/test_answer_quality_runner.py#L288) | 288 | `"    )"` | — |
| [SRC-B3062EB677-L000289](../../tests/test_answer_quality_runner.py#L289) | 289 | `"    costs, source = mod._load_request_cost_ledger(ledger_path, {\"AQ-001\", \"AQ-002\"})"` | — |
| [SRC-B3062EB677-L000290](../../tests/test_answer_quality_runner.py#L290) | 290 | `"    assert costs == {\"AQ-001\": 0.0042}"` | — |
| [SRC-B3062EB677-L000291](../../tests/test_answer_quality_runner.py#L291) | 291 | `"    assert source == \"provider usage export reviewed by operator\""` | — |
| [SRC-B3062EB677-L000292](../../tests/test_answer_quality_runner.py#L292) | 292 | `""` | — |
| [SRC-B3062EB677-L000293](../../tests/test_answer_quality_runner.py#L293) | 293 | `""` | — |
| [SRC-B3062EB677-L000294](../../tests/test_answer_quality_runner.py#L294) | 294 | `"@pytest.mark.parametrize("` | — |
| [SRC-B3062EB677-L000295](../../tests/test_answer_quality_runner.py#L295) | 295 | `"    \"ledger, allowed_ids, message\","` | — |
| [SRC-B3062EB677-L000296](../../tests/test_answer_quality_runner.py#L296) | 296 | `"    ["` | — |
| [SRC-B3062EB677-L000297](../../tests/test_answer_quality_runner.py#L297) | 297 | `"        ({\"currency\": \"EUR\", \"scope\": \"complete_request\", \"source\": \"invoice\", \"costs\": []}, {\"AQ-001\"}, \"currency=USD\"),"` | — |
| [SRC-B3062EB677-L000298](../../tests/test_answer_quality_runner.py#L298) | 298 | `"        ({\"currency\": \"USD\", \"scope\": \"model_only\", \"source\": \"invoice\", \"costs\": []}, {\"AQ-001\"}, \"scope=complete_request\"),"` | — |
| [SRC-B3062EB677-L000299](../../tests/test_answer_quality_runner.py#L299) | 299 | `"        ({\"currency\": \"USD\", \"scope\": \"complete_request\", \"source\": \"\", \"costs\": []}, {\"AQ-001\"}, \"non-empty source\"),"` | — |
| [SRC-B3062EB677-L000300](../../tests/test_answer_quality_runner.py#L300) | 300 | `"        ({\"currency\": \"USD\", \"scope\": \"complete_request\", \"source\": \"invoice\", \"costs\": [{\"case_id\": \"AQ-404\", \"cost_usd\": 0.0}]}, {\"AQ-001\"}, \"unknown case_id\"),"` | — |
| [SRC-B3062EB677-L000301](../../tests/test_answer_quality_runner.py#L301) | 301 | `"        ({\"currency\": \"USD\", \"scope\": \"complete_request\", \"source\": \"invoice\", \"costs\": [{\"case_id\": \"AQ-001\", \"cost_usd\": -0.1}]}, {\"AQ-001\"}, \"finite and non-negative\"),"` | — |
| [SRC-B3062EB677-L000302](../../tests/test_answer_quality_runner.py#L302) | 302 | `"    ],"` | — |
| [SRC-B3062EB677-L000303](../../tests/test_answer_quality_runner.py#L303) | 303 | `")"` | — |
| [SRC-B3062EB677-L000304](../../tests/test_answer_quality_runner.py#L304) | 304 | `"def test_request_cost_ledger_rejects_unverifiable_values(tmp_path, ledger, allowed_ids, message):"` | — |
| [SRC-B3062EB677-L000305](../../tests/test_answer_quality_runner.py#L305) | 305 | `"    mod = _load_runner()"` | — |
| [SRC-B3062EB677-L000306](../../tests/test_answer_quality_runner.py#L306) | 306 | `"    path = tmp_path / \"cost-ledger.json\""` | — |
| [SRC-B3062EB677-L000307](../../tests/test_answer_quality_runner.py#L307) | 307 | `"    path.write_text(json.dumps(ledger), encoding=\"utf-8\")"` | — |
| [SRC-B3062EB677-L000308](../../tests/test_answer_quality_runner.py#L308) | 308 | `"    with pytest.raises(ValueError, match=message):"` | — |
| [SRC-B3062EB677-L000309](../../tests/test_answer_quality_runner.py#L309) | 309 | `"        mod._load_request_cost_ledger(path, allowed_ids)"` | — |
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
| [SRC-1C77C97630-L000066](../../tests/test_answer_validation.py#L66) | 66 | `"def test_criterion_coverage_distinguishes_answer_mentions_from_source_evidence():"` | — |
| [SRC-1C77C97630-L000067](../../tests/test_answer_validation.py#L67) | 67 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000068](../../tests/test_answer_validation.py#L68) | 68 | `"        \"قارن من حيث السعر والمساحة\","` | — |
| [SRC-1C77C97630-L000069](../../tests/test_answer_validation.py#L69) | 69 | `"        \"السعر واضح، أما المساحة فلا تتوفر بيانات عنها.\","` | — |
| [SRC-1C77C97630-L000070](../../tests/test_answer_validation.py#L70) | 70 | `"        [{"` | — |
| [SRC-1C77C97630-L000071](../../tests/test_answer_validation.py#L71) | 71 | `"            \"title\": \"سعر الهاتف\","` | — |
| [SRC-1C77C97630-L000072](../../tests/test_answer_validation.py#L72) | 72 | `"            \"snippet\": \"سعر الهاتف 100 جنيه\","` | — |
| [SRC-1C77C97630-L000073](../../tests/test_answer_validation.py#L73) | 73 | `"            \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000074](../../tests/test_answer_validation.py#L74) | 74 | `"        }],"` | — |
| [SRC-1C77C97630-L000075](../../tests/test_answer_validation.py#L75) | 75 | `"        [\"السعر\", \"المساحة\"],"` | — |
| [SRC-1C77C97630-L000076](../../tests/test_answer_validation.py#L76) | 76 | `"    )"` | — |
| [SRC-1C77C97630-L000077](../../tests/test_answer_validation.py#L77) | 77 | `"    checks = {item[\"target\"]: item for item in result[\"target_coverage\"]}"` | — |
| [SRC-1C77C97630-L000078](../../tests/test_answer_validation.py#L78) | 78 | `""` | — |
| [SRC-1C77C97630-L000079](../../tests/test_answer_validation.py#L79) | 79 | `"    # Both dimensions are mentioned in the answer, but only price has a source signal."` | — |
| [SRC-1C77C97630-L000080](../../tests/test_answer_validation.py#L80) | 80 | `"    assert checks[\"السعر\"][\"status\"] == \"lexical_signal_found\""` | — |
| [SRC-1C77C97630-L000081](../../tests/test_answer_validation.py#L81) | 81 | `"    assert checks[\"السعر\"][\"source_evidence_status\"] == \"source_lexical_signal_found\""` | — |
| [SRC-1C77C97630-L000082](../../tests/test_answer_validation.py#L82) | 82 | `"    assert checks[\"المساحة\"][\"status\"] == \"lexical_signal_found\""` | — |
| [SRC-1C77C97630-L000083](../../tests/test_answer_validation.py#L83) | 83 | `"    assert checks[\"المساحة\"][\"source_evidence_status\"] == \"no_source_lexical_signal\""` | — |
| [SRC-1C77C97630-L000084](../../tests/test_answer_validation.py#L84) | 84 | `"    assert result[\"source_evidence_gap_count\"] == 1"` | — |
| [SRC-1C77C97630-L000085](../../tests/test_answer_validation.py#L85) | 85 | `"    assert result[\"source_evidence_assessment\"] == ("` | — |
| [SRC-1C77C97630-L000086](../../tests/test_answer_validation.py#L86) | 86 | `"        \"criterion_level_lexical_signals_not_claim_support_or_entailment\""` | — |
| [SRC-1C77C97630-L000087](../../tests/test_answer_validation.py#L87) | 87 | `"    )"` | — |
| [SRC-1C77C97630-L000088](../../tests/test_answer_validation.py#L88) | 88 | `"    assert result[\"independent_fact_check\"] is False"` | — |
| [SRC-1C77C97630-L000089](../../tests/test_answer_validation.py#L89) | 89 | `""` | — |
| [SRC-1C77C97630-L000090](../../tests/test_answer_validation.py#L90) | 90 | `""` | — |
| [SRC-1C77C97630-L000091](../../tests/test_answer_validation.py#L91) | 91 | `"def test_arabic_criterion_can_match_common_english_source_terms():"` | — |
| [SRC-1C77C97630-L000092](../../tests/test_answer_validation.py#L92) | 92 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000093](../../tests/test_answer_validation.py#L93) | 93 | `"        \"قارن من حيث السعر والمساحة\","` | — |
| [SRC-1C77C97630-L000094](../../tests/test_answer_validation.py#L94) | 94 | `"        \"السعر مذكور، لكن المساحة غير متاحة في الأدلة.\","` | — |
| [SRC-1C77C97630-L000095](../../tests/test_answer_validation.py#L95) | 95 | `"        [{"` | — |
| [SRC-1C77C97630-L000096](../../tests/test_answer_validation.py#L96) | 96 | `"            \"title\": \"Product listing\","` | — |
| [SRC-1C77C97630-L000097](../../tests/test_answer_validation.py#L97) | 97 | `"            \"snippet\": \"Price: 100 EGP. Size: 80 sqm.\","` | — |
| [SRC-1C77C97630-L000098](../../tests/test_answer_validation.py#L98) | 98 | `"            \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000099](../../tests/test_answer_validation.py#L99) | 99 | `"        }],"` | — |
| [SRC-1C77C97630-L000100](../../tests/test_answer_validation.py#L100) | 100 | `"        [\"السعر\", \"المساحة\"],"` | — |
| [SRC-1C77C97630-L000101](../../tests/test_answer_validation.py#L101) | 101 | `"    )"` | — |
| [SRC-1C77C97630-L000102](../../tests/test_answer_validation.py#L102) | 102 | `"    checks = {item[\"target\"]: item for item in result[\"target_coverage\"]}"` | — |
| [SRC-1C77C97630-L000103](../../tests/test_answer_validation.py#L103) | 103 | `"    assert checks[\"السعر\"][\"source_evidence_status\"] == \"source_lexical_signal_found\""` | — |
| [SRC-1C77C97630-L000104](../../tests/test_answer_validation.py#L104) | 104 | `"    assert checks[\"المساحة\"][\"source_evidence_status\"] == \"source_lexical_signal_found\""` | — |
| [SRC-1C77C97630-L000105](../../tests/test_answer_validation.py#L105) | 105 | `"    assert result[\"source_evidence_gap_count\"] == 0"` | — |
| [SRC-1C77C97630-L000106](../../tests/test_answer_validation.py#L106) | 106 | `"    # Cross-language lexical matching remains a retrieval hint, not entailment."` | — |
| [SRC-1C77C97630-L000107](../../tests/test_answer_validation.py#L107) | 107 | `"    assert result[\"semantic_verification\"] is False"` | — |
| [SRC-1C77C97630-L000108](../../tests/test_answer_validation.py#L108) | 108 | `"    assert result[\"independent_fact_check\"] is False"` | — |
| [SRC-1C77C97630-L000109](../../tests/test_answer_validation.py#L109) | 109 | `""` | — |
| [SRC-1C77C97630-L000110](../../tests/test_answer_validation.py#L110) | 110 | `""` | — |
| [SRC-1C77C97630-L000111](../../tests/test_answer_validation.py#L111) | 111 | `"def test_source_scope_does_not_confuse_snippet_with_fetched_page():"` | — |
| [SRC-1C77C97630-L000112](../../tests/test_answer_validation.py#L112) | 112 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000113](../../tests/test_answer_validation.py#L113) | 113 | `"        \"ما التفاصيل؟\","` | — |
| [SRC-1C77C97630-L000114](../../tests/test_answer_validation.py#L114) | 114 | `"        \"وجدت مقتطفًا.\","` | — |
| [SRC-1C77C97630-L000115](../../tests/test_answer_validation.py#L115) | 115 | `"        [{\"title\": \"نتيجة\", \"snippet\": \"مقتطف قصير\", \"page_fetched\": False}],"` | — |
| [SRC-1C77C97630-L000116](../../tests/test_answer_validation.py#L116) | 116 | `"    )"` | — |
| [SRC-1C77C97630-L000117](../../tests/test_answer_validation.py#L117) | 117 | `"    assert result[\"source_evidence_scope\"] == \"search_snippets_only\""` | — |
| [SRC-1C77C97630-L000118](../../tests/test_answer_validation.py#L118) | 118 | `"    assert result[\"pages_with_extracted_text\"] == 0"` | — |
| [SRC-1C77C97630-L000119](../../tests/test_answer_validation.py#L119) | 119 | `"    assert result[\"sources_with_snippets_only\"] == 1"` | — |
| [SRC-1C77C97630-L000120](../../tests/test_answer_validation.py#L120) | 120 | `""` | — |
| [SRC-1C77C97630-L000121](../../tests/test_answer_validation.py#L121) | 121 | `""` | — |
| [SRC-1C77C97630-L000122](../../tests/test_answer_validation.py#L122) | 122 | `"def test_review_prompt_explicitly_requires_number_and_conflict_audit(monkeypatch):"` | — |
| [SRC-1C77C97630-L000123](../../tests/test_answer_validation.py#L123) | 123 | `"    agent = WebAgent()"` | — |
| [SRC-1C77C97630-L000124](../../tests/test_answer_validation.py#L124) | 124 | `"    captured = {}"` | — |
| [SRC-1C77C97630-L000125](../../tests/test_answer_validation.py#L125) | 125 | `""` | — |
| [SRC-1C77C97630-L000126](../../tests/test_answer_validation.py#L126) | 126 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-1C77C97630-L000127](../../tests/test_answer_validation.py#L127) | 127 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-1C77C97630-L000128](../../tests/test_answer_validation.py#L128) | 128 | `"        return \"<<<OMARAI_FINAL_ANSWER>>>لا تكفي الأدلة.<<<END_OMARAI_FINAL_ANSWER>>>\""` | — |
| [SRC-1C77C97630-L000129](../../tests/test_answer_validation.py#L129) | 129 | `""` | — |
| [SRC-1C77C97630-L000130](../../tests/test_answer_validation.py#L130) | 130 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-1C77C97630-L000131](../../tests/test_answer_validation.py#L131) | 131 | `"    answer = agent._review_answer("` | — |
| [SRC-1C77C97630-L000132](../../tests/test_answer_validation.py#L132) | 132 | `"        \"قارن السعر والمدة\","` | — |
| [SRC-1C77C97630-L000133](../../tests/test_answer_validation.py#L133) | 133 | `"        \"السعر 100 جنيه [المصدر 1].\","` | — |
| [SRC-1C77C97630-L000134](../../tests/test_answer_validation.py#L134) | 134 | `"        [{"` | — |
| [SRC-1C77C97630-L000135](../../tests/test_answer_validation.py#L135) | 135 | `"            \"title\": \"مصدر\","` | — |
| [SRC-1C77C97630-L000136](../../tests/test_answer_validation.py#L136) | 136 | `"            \"url\": \"https://example.com/item\","` | — |
| [SRC-1C77C97630-L000137](../../tests/test_answer_validation.py#L137) | 137 | `"            \"page_text\": \"السعر 90 جنيه، والمدة 5 أيام.\","` | — |
| [SRC-1C77C97630-L000138](../../tests/test_answer_validation.py#L138) | 138 | `"            \"snippet\": \"السعر 90 جنيه\","` | — |
| [SRC-1C77C97630-L000139](../../tests/test_answer_validation.py#L139) | 139 | `"            \"page_fetched\": True,"` | — |
| [SRC-1C77C97630-L000140](../../tests/test_answer_validation.py#L140) | 140 | `"        }],"` | — |
| [SRC-1C77C97630-L000141](../../tests/test_answer_validation.py#L141) | 141 | `"    )"` | — |
| [SRC-1C77C97630-L000142](../../tests/test_answer_validation.py#L142) | 142 | `"    prompt = captured[\"messages\"][0][\"content\"]"` | — |
| [SRC-1C77C97630-L000143](../../tests/test_answer_validation.py#L143) | 143 | `"    assert answer == \"لا تكفي الأدلة.\""` | — |
| [SRC-1C77C97630-L000144](../../tests/test_answer_validation.py#L144) | 144 | `"    assert \"المبالغ والأسعار والنسب والتواريخ والمدد والقياسات\" in prompt"` | — |
| [SRC-1C77C97630-L000145](../../tests/test_answer_validation.py#L145) | 145 | `"    assert \"قيمًا متعارضة\" in prompt"` | — |
| [SRC-1C77C97630-L000146](../../tests/test_answer_validation.py#L146) | 146 | `""` | — |
| [SRC-1C77C97630-L000147](../../tests/test_answer_validation.py#L147) | 147 | `""` | — |
| [SRC-1C77C97630-L000148](../../tests/test_answer_validation.py#L148) | 148 | `"def test_citation_alignment_uses_fetched_page_text_and_flags_weak_overlap():"` | — |
| [SRC-1C77C97630-L000149](../../tests/test_answer_validation.py#L149) | 149 | `"    page_source = {"` | — |
| [SRC-1C77C97630-L000150](../../tests/test_answer_validation.py#L150) | 150 | `"        \"title\": \"Report\","` | — |
| [SRC-1C77C97630-L000151](../../tests/test_answer_validation.py#L151) | 151 | `"        \"snippet\": \"completely unrelated snippet about fruit\","` | — |
| [SRC-1C77C97630-L000152](../../tests/test_answer_validation.py#L152) | 152 | `"        \"page_text\": \"Renewable energy storage costs decreased during the reporting period.\","` | — |
| [SRC-1C77C97630-L000153](../../tests/test_answer_validation.py#L153) | 153 | `"        \"page_fetched\": True,"` | — |
| [SRC-1C77C97630-L000154](../../tests/test_answer_validation.py#L154) | 154 | `"        \"published_at\": \"\","` | — |
| [SRC-1C77C97630-L000155](../../tests/test_answer_validation.py#L155) | 155 | `"    }"` | — |
| [SRC-1C77C97630-L000156](../../tests/test_answer_validation.py#L156) | 156 | `"    good = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000157](../../tests/test_answer_validation.py#L157) | 157 | `"        \"What changed?\","` | — |
| [SRC-1C77C97630-L000158](../../tests/test_answer_validation.py#L158) | 158 | `"        \"Renewable energy storage costs decreased [source 1].\","` | — |
| [SRC-1C77C97630-L000159](../../tests/test_answer_validation.py#L159) | 159 | `"        [page_source],"` | — |
| [SRC-1C77C97630-L000160](../../tests/test_answer_validation.py#L160) | 160 | `"    )"` | — |
| [SRC-1C77C97630-L000161](../../tests/test_answer_validation.py#L161) | 161 | `"    assert good[\"citation_lexical_alignment_method\"] == \"content_word_overlap_heuristic_not_entailment\""` | — |
| [SRC-1C77C97630-L000162](../../tests/test_answer_validation.py#L162) | 162 | `"    assert good[\"citation_lexical_alignment\"][0][\"status\"] == \"lexical_overlap_signal_found\""` | — |
| [SRC-1C77C97630-L000163](../../tests/test_answer_validation.py#L163) | 163 | `"    assert good[\"citation_lexical_alignment\"][0][\"citations\"][0][\"evidence_basis\"] == \"extracted_page_text\""` | — |
| [SRC-1C77C97630-L000164](../../tests/test_answer_validation.py#L164) | 164 | `"    assert good[\"citation_entailment\"] == \"not_checked\""` | — |
| [SRC-1C77C97630-L000165](../../tests/test_answer_validation.py#L165) | 165 | `""` | — |
| [SRC-1C77C97630-L000166](../../tests/test_answer_validation.py#L166) | 166 | `"    weak = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000167](../../tests/test_answer_validation.py#L167) | 167 | `"        \"What happened?\","` | — |
| [SRC-1C77C97630-L000168](../../tests/test_answer_validation.py#L168) | 168 | `"        \"Mango harvest volume rose sharply [source 1].\","` | — |
| [SRC-1C77C97630-L000169](../../tests/test_answer_validation.py#L169) | 169 | `"        [page_source],"` | — |
| [SRC-1C77C97630-L000170](../../tests/test_answer_validation.py#L170) | 170 | `"    )"` | — |
| [SRC-1C77C97630-L000171](../../tests/test_answer_validation.py#L171) | 171 | `"    assert weak[\"citation_lexical_alignment\"][0][\"status\"] == \"weak_lexical_overlap\""` | — |
| [SRC-1C77C97630-L000172](../../tests/test_answer_validation.py#L172) | 172 | `"    assert weak[\"weak_citation_alignment_count\"] == 1"` | — |
| [SRC-1C77C97630-L000173](../../tests/test_answer_validation.py#L173) | 173 | `"    assert weak[\"independent_fact_check\"] is False"` | — |
| [SRC-1C77C97630-L000174](../../tests/test_answer_validation.py#L174) | 174 | `""` | — |
| [SRC-1C77C97630-L000175](../../tests/test_answer_validation.py#L175) | 175 | `""` | — |
| [SRC-1C77C97630-L000176](../../tests/test_answer_validation.py#L176) | 176 | `"def test_snippet_only_citation_alignment_is_labeled_as_snippet_evidence():"` | — |
| [SRC-1C77C97630-L000177](../../tests/test_answer_validation.py#L177) | 177 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000178](../../tests/test_answer_validation.py#L178) | 178 | `"        \"What was reported?\","` | — |
| [SRC-1C77C97630-L000179](../../tests/test_answer_validation.py#L179) | 179 | `"        \"The reported costs changed [المصدر 1].\","` | — |
| [SRC-1C77C97630-L000180](../../tests/test_answer_validation.py#L180) | 180 | `"        [{"` | — |
| [SRC-1C77C97630-L000181](../../tests/test_answer_validation.py#L181) | 181 | `"            \"title\": \"Costs report\","` | — |
| [SRC-1C77C97630-L000182](../../tests/test_answer_validation.py#L182) | 182 | `"            \"snippet\": \"Reported costs changed in the new report.\","` | — |
| [SRC-1C77C97630-L000183](../../tests/test_answer_validation.py#L183) | 183 | `"            \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000184](../../tests/test_answer_validation.py#L184) | 184 | `"        }],"` | — |
| [SRC-1C77C97630-L000185](../../tests/test_answer_validation.py#L185) | 185 | `"    )"` | — |
| [SRC-1C77C97630-L000186](../../tests/test_answer_validation.py#L186) | 186 | `"    assert result[\"citation_lexical_alignment\"][0][\"citations\"][0][\"evidence_basis\"] == \"search_snippet\""` | — |
| [SRC-1C77C97630-L000187](../../tests/test_answer_validation.py#L187) | 187 | `"    assert result[\"citation_entailment\"] == \"not_checked\""` | — |
| [SRC-1C77C97630-L000188](../../tests/test_answer_validation.py#L188) | 188 | `""` | — |
| [SRC-1C77C97630-L000189](../../tests/test_answer_validation.py#L189) | 189 | `""` | — |
| [SRC-1C77C97630-L000190](../../tests/test_answer_validation.py#L190) | 190 | `"def test_bounded_coverage_repair_parses_one_delimited_answer_and_supplies_evidence(monkeypatch):"` | — |
| [SRC-1C77C97630-L000191](../../tests/test_answer_validation.py#L191) | 191 | `"    agent = WebAgent()"` | — |
| [SRC-1C77C97630-L000192](../../tests/test_answer_validation.py#L192) | 192 | `"    captured = {}"` | — |
| [SRC-1C77C97630-L000193](../../tests/test_answer_validation.py#L193) | 193 | `""` | — |
| [SRC-1C77C97630-L000194](../../tests/test_answer_validation.py#L194) | 194 | `"    def fake_completion(messages, **kwargs):"` | — |
| [SRC-1C77C97630-L000195](../../tests/test_answer_validation.py#L195) | 195 | `"        captured[\"messages\"] = messages"` | — |
| [SRC-1C77C97630-L000196](../../tests/test_answer_validation.py#L196) | 196 | `"        return \"<<<OMARAI_COVERAGE_REPAIR>>>تم توضيح السعر والمساحة [المصدر 1].<<<END_OMARAI_COVERAGE_REPAIR>>>\""` | — |
| [SRC-1C77C97630-L000197](../../tests/test_answer_validation.py#L197) | 197 | `""` | — |
| [SRC-1C77C97630-L000198](../../tests/test_answer_validation.py#L198) | 198 | `"    monkeypatch.setattr(agent, \"_request_completion\", fake_completion)"` | — |
| [SRC-1C77C97630-L000199](../../tests/test_answer_validation.py#L199) | 199 | `"    repaired = agent._repair_answer_coverage("` | — |
| [SRC-1C77C97630-L000200](../../tests/test_answer_validation.py#L200) | 200 | `"        \"قارن السعر والمساحة\","` | — |
| [SRC-1C77C97630-L000201](../../tests/test_answer_validation.py#L201) | 201 | `"        \"الإجابة الأولية.\","` | — |
| [SRC-1C77C97630-L000202](../../tests/test_answer_validation.py#L202) | 202 | `"        [{"` | — |
| [SRC-1C77C97630-L000203](../../tests/test_answer_validation.py#L203) | 203 | `"            \"title\": \"إعلان\","` | — |
| [SRC-1C77C97630-L000204](../../tests/test_answer_validation.py#L204) | 204 | `"            \"url\": \"https://example.com/listing\","` | — |
| [SRC-1C77C97630-L000205](../../tests/test_answer_validation.py#L205) | 205 | `"            \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000206](../../tests/test_answer_validation.py#L206) | 206 | `"            \"snippet\": \"السعر مذكور والمساحة غير مذكورة\","` | — |
| [SRC-1C77C97630-L000207](../../tests/test_answer_validation.py#L207) | 207 | `"        }],"` | — |
| [SRC-1C77C97630-L000208](../../tests/test_answer_validation.py#L208) | 208 | `"        [\"المساحة\"],"` | — |
| [SRC-1C77C97630-L000209](../../tests/test_answer_validation.py#L209) | 209 | `"    )"` | — |
| [SRC-1C77C97630-L000210](../../tests/test_answer_validation.py#L210) | 210 | `"    assert repaired == \"تم توضيح السعر والمساحة [المصدر 1].\""` | — |
| [SRC-1C77C97630-L000211](../../tests/test_answer_validation.py#L211) | 211 | `"    assert \"المساحة\" in captured[\"messages\"][2][\"content\"]"` | — |
| [SRC-1C77C97630-L000212](../../tests/test_answer_validation.py#L212) | 212 | `"    assert \"السعر مذكور والمساحة غير مذكورة\" in captured[\"messages\"][4][\"content\"]"` | — |
| [SRC-1C77C97630-L000213](../../tests/test_answer_validation.py#L213) | 213 | `"    assert \"مقتطف بحث\" in captured[\"messages\"][4][\"content\"]"` | — |
| [SRC-1C77C97630-L000214](../../tests/test_answer_validation.py#L214) | 214 | `""` | — |
| [SRC-1C77C97630-L000215](../../tests/test_answer_validation.py#L215) | 215 | `""` | — |
| [SRC-1C77C97630-L000216](../../tests/test_answer_validation.py#L216) | 216 | `"def test_bounded_coverage_repair_rejects_missing_or_duplicate_markers(monkeypatch):"` | — |
| [SRC-1C77C97630-L000217](../../tests/test_answer_validation.py#L217) | 217 | `"    agent = WebAgent()"` | — |
| [SRC-1C77C97630-L000218](../../tests/test_answer_validation.py#L218) | 218 | `"    monkeypatch.setattr("` | — |
| [SRC-1C77C97630-L000219](../../tests/test_answer_validation.py#L219) | 219 | `"        agent,"` | — |
| [SRC-1C77C97630-L000220](../../tests/test_answer_validation.py#L220) | 220 | `"        \"_request_completion\","` | — |
| [SRC-1C77C97630-L000221](../../tests/test_answer_validation.py#L221) | 221 | `"        lambda *args, **kwargs: ("` | — |
| [SRC-1C77C97630-L000222](../../tests/test_answer_validation.py#L222) | 222 | `"            \"<<<OMARAI_COVERAGE_REPAIR>>>إجابة<<<END_OMARAI_COVERAGE_REPAIR>>>\""` | — |
| [SRC-1C77C97630-L000223](../../tests/test_answer_validation.py#L223) | 223 | `"            \"<<<END_OMARAI_COVERAGE_REPAIR>>>\""` | — |
| [SRC-1C77C97630-L000224](../../tests/test_answer_validation.py#L224) | 224 | `"        ),"` | — |
| [SRC-1C77C97630-L000225](../../tests/test_answer_validation.py#L225) | 225 | `"    )"` | — |
| [SRC-1C77C97630-L000226](../../tests/test_answer_validation.py#L226) | 226 | `"    with pytest.raises(RuntimeError, match=\"إصلاح تغطية آمن\"):"` | — |
| [SRC-1C77C97630-L000227](../../tests/test_answer_validation.py#L227) | 227 | `"        agent._repair_answer_coverage("` | — |
| [SRC-1C77C97630-L000228](../../tests/test_answer_validation.py#L228) | 228 | `"            \"قارن السعر\","` | — |
| [SRC-1C77C97630-L000229](../../tests/test_answer_validation.py#L229) | 229 | `"            \"مسودة\","` | — |
| [SRC-1C77C97630-L000230](../../tests/test_answer_validation.py#L230) | 230 | `"            [{\"title\": \"مصدر\", \"url\": \"https://example.com\", \"snippet\": \"السعر 100 جنيه\"}],"` | — |
| [SRC-1C77C97630-L000231](../../tests/test_answer_validation.py#L231) | 231 | `"            [\"السعر\"],"` | — |
| [SRC-1C77C97630-L000232](../../tests/test_answer_validation.py#L232) | 232 | `"        )"` | — |
| [SRC-1C77C97630-L000233](../../tests/test_answer_validation.py#L233) | 233 | `""` | — |
| [SRC-1C77C97630-L000234](../../tests/test_answer_validation.py#L234) | 234 | `""` | — |
| [SRC-1C77C97630-L000235](../../tests/test_answer_validation.py#L235) | 235 | `"def test_cited_number_must_appear_in_the_exact_cited_source_not_merely_some_source():"` | — |
| [SRC-1C77C97630-L000236](../../tests/test_answer_validation.py#L236) | 236 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000237](../../tests/test_answer_validation.py#L237) | 237 | `"        \"قارن أسعار المنتجين\","` | — |
| [SRC-1C77C97630-L000238](../../tests/test_answer_validation.py#L238) | 238 | `"        \"سعر المنتج الأول 500 جنيه [المصدر 1].\","` | — |
| [SRC-1C77C97630-L000239](../../tests/test_answer_validation.py#L239) | 239 | `"        ["` | — |
| [SRC-1C77C97630-L000240](../../tests/test_answer_validation.py#L240) | 240 | `"            {"` | — |
| [SRC-1C77C97630-L000241](../../tests/test_answer_validation.py#L241) | 241 | `"                \"title\": \"سعر المنتج الأول\","` | — |
| [SRC-1C77C97630-L000242](../../tests/test_answer_validation.py#L242) | 242 | `"                \"snippet\": \"سعر المنتج الأول 300 جنيه\","` | — |
| [SRC-1C77C97630-L000243](../../tests/test_answer_validation.py#L243) | 243 | `"                \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000244](../../tests/test_answer_validation.py#L244) | 244 | `"            },"` | — |
| [SRC-1C77C97630-L000245](../../tests/test_answer_validation.py#L245) | 245 | `"            {"` | — |
| [SRC-1C77C97630-L000246](../../tests/test_answer_validation.py#L246) | 246 | `"                \"title\": \"سعر المنتج الثاني\","` | — |
| [SRC-1C77C97630-L000247](../../tests/test_answer_validation.py#L247) | 247 | `"                \"snippet\": \"سعر المنتج الثاني 500 جنيه\","` | — |
| [SRC-1C77C97630-L000248](../../tests/test_answer_validation.py#L248) | 248 | `"                \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000249](../../tests/test_answer_validation.py#L249) | 249 | `"            },"` | — |
| [SRC-1C77C97630-L000250](../../tests/test_answer_validation.py#L250) | 250 | `"        ],"` | — |
| [SRC-1C77C97630-L000251](../../tests/test_answer_validation.py#L251) | 251 | `"    )"` | — |
| [SRC-1C77C97630-L000252](../../tests/test_answer_validation.py#L252) | 252 | `""` | — |
| [SRC-1C77C97630-L000253](../../tests/test_answer_validation.py#L253) | 253 | `"    assert result[\"potentially_unsupported_numeric_literals\"] == []"` | — |
| [SRC-1C77C97630-L000254](../../tests/test_answer_validation.py#L254) | 254 | `"    assert result[\"potentially_unsupported_numeric_by_citation_count\"] == 1"` | — |
| [SRC-1C77C97630-L000255](../../tests/test_answer_validation.py#L255) | 255 | `"    cited_check = result[\"citation_numeric_support\"][0]"` | — |
| [SRC-1C77C97630-L000256](../../tests/test_answer_validation.py#L256) | 256 | `"    assert cited_check[\"cited_source_indexes\"] == [1]"` | — |
| [SRC-1C77C97630-L000257](../../tests/test_answer_validation.py#L257) | 257 | `"    assert cited_check[\"potentially_unsupported_numeric_literals\"] == [\"500\"]"` | — |
| [SRC-1C77C97630-L000258](../../tests/test_answer_validation.py#L258) | 258 | `"    assert cited_check[\"status\"] == \"potentially_unsupported_numeric_literals_for_cited_sources\""` | — |
| [SRC-1C77C97630-L000259](../../tests/test_answer_validation.py#L259) | 259 | `""` | — |
| [SRC-1C77C97630-L000260](../../tests/test_answer_validation.py#L260) | 260 | `""` | — |
| [SRC-1C77C97630-L000261](../../tests/test_answer_validation.py#L261) | 261 | `"def test_different_price_values_are_flagged_for_review_not_called_contradictions():"` | — |
| [SRC-1C77C97630-L000262](../../tests/test_answer_validation.py#L262) | 262 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000263](../../tests/test_answer_validation.py#L263) | 263 | `"        \"قارن العروض\","` | — |
| [SRC-1C77C97630-L000264](../../tests/test_answer_validation.py#L264) | 264 | `"        \"العرض الأول أرخص من الثاني [المصدر 1] [المصدر 2].\","` | — |
| [SRC-1C77C97630-L000265](../../tests/test_answer_validation.py#L265) | 265 | `"        ["` | — |
| [SRC-1C77C97630-L000266](../../tests/test_answer_validation.py#L266) | 266 | `"            {"` | — |
| [SRC-1C77C97630-L000267](../../tests/test_answer_validation.py#L267) | 267 | `"                \"title\": \"شقة القاهرة\","` | — |
| [SRC-1C77C97630-L000268](../../tests/test_answer_validation.py#L268) | 268 | `"                \"snippet\": \"السعر 100000 جنيه\","` | — |
| [SRC-1C77C97630-L000269](../../tests/test_answer_validation.py#L269) | 269 | `"                \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000270](../../tests/test_answer_validation.py#L270) | 270 | `"            },"` | — |
| [SRC-1C77C97630-L000271](../../tests/test_answer_validation.py#L271) | 271 | `"            {"` | — |
| [SRC-1C77C97630-L000272](../../tests/test_answer_validation.py#L272) | 272 | `"                \"title\": \"شقة القاهرة\","` | — |
| [SRC-1C77C97630-L000273](../../tests/test_answer_validation.py#L273) | 273 | `"                \"snippet\": \"السعر 120000 جنيه\","` | — |
| [SRC-1C77C97630-L000274](../../tests/test_answer_validation.py#L274) | 274 | `"                \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000275](../../tests/test_answer_validation.py#L275) | 275 | `"            },"` | — |
| [SRC-1C77C97630-L000276](../../tests/test_answer_validation.py#L276) | 276 | `"        ],"` | — |
| [SRC-1C77C97630-L000277](../../tests/test_answer_validation.py#L277) | 277 | `"    )"` | — |
| [SRC-1C77C97630-L000278](../../tests/test_answer_validation.py#L278) | 278 | `""` | — |
| [SRC-1C77C97630-L000279](../../tests/test_answer_validation.py#L279) | 279 | `"    price = next("` | — |
| [SRC-1C77C97630-L000280](../../tests/test_answer_validation.py#L280) | 280 | `"        item for item in result[\"potential_value_discrepancies\"]"` | — |
| [SRC-1C77C97630-L000281](../../tests/test_answer_validation.py#L281) | 281 | `"        if item[\"dimension\"] == \"price_or_cost\""` | — |
| [SRC-1C77C97630-L000282](../../tests/test_answer_validation.py#L282) | 282 | `"    )"` | — |
| [SRC-1C77C97630-L000283](../../tests/test_answer_validation.py#L283) | 283 | `"    assert {item[\"value\"] for item in price[\"values\"]} == {\"100000\", \"120000\"}"` | — |
| [SRC-1C77C97630-L000284](../../tests/test_answer_validation.py#L284) | 284 | `"    assert price[\"status\"] == \"potential_variation_or_conflict_requires_entity_review\""` | — |
| [SRC-1C77C97630-L000285](../../tests/test_answer_validation.py#L285) | 285 | `"    assert \"contradiction\" not in price[\"status\"]"` | — |
| [SRC-1C77C97630-L000286](../../tests/test_answer_validation.py#L286) | 286 | `"    assert result[\"independent_fact_check\"] is False"` | — |
| [SRC-1C77C97630-L000287](../../tests/test_answer_validation.py#L287) | 287 | `""` | — |
| [SRC-1C77C97630-L000288](../../tests/test_answer_validation.py#L288) | 288 | `""` | — |
| [SRC-1C77C97630-L000289](../../tests/test_answer_validation.py#L289) | 289 | `"def test_date_in_answer_missing_from_its_cited_source_is_flagged():"` | — |
| [SRC-1C77C97630-L000290](../../tests/test_answer_validation.py#L290) | 290 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000291](../../tests/test_answer_validation.py#L291) | 291 | `"        \"ما تاريخ التقرير؟\","` | — |
| [SRC-1C77C97630-L000292](../../tests/test_answer_validation.py#L292) | 292 | `"        \"صدر التقرير في 2026 [المصدر 1].\","` | — |
| [SRC-1C77C97630-L000293](../../tests/test_answer_validation.py#L293) | 293 | `"        [{"` | — |
| [SRC-1C77C97630-L000294](../../tests/test_answer_validation.py#L294) | 294 | `"            \"title\": \"تقرير سابق\","` | — |
| [SRC-1C77C97630-L000295](../../tests/test_answer_validation.py#L295) | 295 | `"            \"snippet\": \"تقرير منشور في 2024.\","` | — |
| [SRC-1C77C97630-L000296](../../tests/test_answer_validation.py#L296) | 296 | `"            \"published_at\": \"2024\","` | — |
| [SRC-1C77C97630-L000297](../../tests/test_answer_validation.py#L297) | 297 | `"            \"page_fetched\": False,"` | — |
| [SRC-1C77C97630-L000298](../../tests/test_answer_validation.py#L298) | 298 | `"        }],"` | — |
| [SRC-1C77C97630-L000299](../../tests/test_answer_validation.py#L299) | 299 | `"    )"` | — |
| [SRC-1C77C97630-L000300](../../tests/test_answer_validation.py#L300) | 300 | `""` | — |
| [SRC-1C77C97630-L000301](../../tests/test_answer_validation.py#L301) | 301 | `"    numeric_check = result[\"citation_numeric_support\"][0]"` | — |
| [SRC-1C77C97630-L000302](../../tests/test_answer_validation.py#L302) | 302 | `"    assert numeric_check[\"potentially_unsupported_numeric_literals\"] == [\"2026\"]"` | — |
| [SRC-1C77C97630-L000303](../../tests/test_answer_validation.py#L303) | 303 | `"    assert numeric_check[\"status\"] == \"potentially_unsupported_numeric_literals_for_cited_sources\""` | — |
| [SRC-1C77C97630-L000304](../../tests/test_answer_validation.py#L304) | 304 | `""` | — |
| [SRC-1C77C97630-L000305](../../tests/test_answer_validation.py#L305) | 305 | `""` | — |
| [SRC-1C77C97630-L000306](../../tests/test_answer_validation.py#L306) | 306 | `"def test_frontend_surfaces_source_specific_number_and_possible_value_discrepancies():"` | — |
| [SRC-1C77C97630-L000307](../../tests/test_answer_validation.py#L307) | 307 | `"    html_path = Path(__file__).resolve().parents[1] / \"web\" / \"agent.html\""` | — |
| [SRC-1C77C97630-L000308](../../tests/test_answer_validation.py#L308) | 308 | `"    html = html_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-1C77C97630-L000309](../../tests/test_answer_validation.py#L309) | 309 | `""` | — |
| [SRC-1C77C97630-L000310](../../tests/test_answer_validation.py#L310) | 310 | `"    assert \"citation_numeric_support\" in html"` | — |
| [SRC-1C77C97630-L000311](../../tests/test_answer_validation.py#L311) | 311 | `"    assert \"potential_value_discrepancies\" in html"` | — |
| [SRC-1C77C97630-L000312](../../tests/test_answer_validation.py#L312) | 312 | `"    assert \"claim_evidence_ledger\" in html"` | — |
| [SRC-1C77C97630-L000313](../../tests/test_answer_validation.py#L313) | 313 | `"    assert \"سجل تتبع الاستشهادات\" in html"` | — |
| [SRC-1C77C97630-L000314](../../tests/test_answer_validation.py#L314) | 314 | `"    assert \"هذه ليست إثباتًا تلقائيًا لوجود تناقض\" in html"` | — |
| [SRC-1C77C97630-L000315](../../tests/test_answer_validation.py#L315) | 315 | `"    assert \"ليس تحققًا من الحقيقة\" in html"` | — |
| [SRC-1C77C97630-L000316](../../tests/test_answer_validation.py#L316) | 316 | `""` | — |
| [SRC-1C77C97630-L000317](../../tests/test_answer_validation.py#L317) | 317 | `""` | — |
| [SRC-1C77C97630-L000318](../../tests/test_answer_validation.py#L318) | 318 | `"def test_single_coincidental_token_does_not_count_as_citation_support():"` | — |
| [SRC-1C77C97630-L000319](../../tests/test_answer_validation.py#L319) | 319 | `"    result = audit_answer_integrity("` | — |
| [SRC-1C77C97630-L000320](../../tests/test_answer_validation.py#L320) | 320 | `"        \"What is the device quality?\","` | — |
| [SRC-1C77C97630-L000321](../../tests/test_answer_validation.py#L321) | 321 | `"        \"Apple is a premium and exceptionally reliable device [source 1].\","` | — |
| [SRC-1C77C97630-L000322](../../tests/test_answer_validation.py#L322) | 322 | `"        [{"` | — |
| [SRC-1C77C97630-L000323](../../tests/test_answer_validation.py#L323) | 323 | `"            \"title\": \"Apple catalog\","` | — |
| [SRC-1C77C97630-L000324](../../tests/test_answer_validation.py#L324) | 324 | `"            \"snippet\": \"Apple product listing\","` | — |
| [SRC-1C77C97630-L000325](../../tests/test_answer_validation.py#L325) | 325 | `"            \"page_text\": \"Apple products are listed with model identifiers and availability.\","` | — |
| [SRC-1C77C97630-L000326](../../tests/test_answer_validation.py#L326) | 326 | `"            \"page_fetched\": True,"` | — |
| [SRC-1C77C97630-L000327](../../tests/test_answer_validation.py#L327) | 327 | `"        }],"` | — |
| [SRC-1C77C97630-L000328](../../tests/test_answer_validation.py#L328) | 328 | `"    )"` | — |
| [SRC-1C77C97630-L000329](../../tests/test_answer_validation.py#L329) | 329 | `"    assert result[\"citation_lexical_alignment\"][0][\"status\"] == \"weak_lexical_overlap\""` | — |
| [SRC-1C77C97630-L000330](../../tests/test_answer_validation.py#L330) | 330 | `"    assert result[\"weak_citation_alignment_count\"] == 1"` | — |
| [SRC-1C77C97630-L000331](../../tests/test_answer_validation.py#L331) | 331 | `"    assert result[\"citation_entailment\"] == \"not_checked\""` | — |
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
| [SRC-3451CC474D-L000250](../../tests/test_api.py#L250) | 250 | `"    )"` | — |
| [SRC-3451CC474D-L000251](../../tests/test_api.py#L251) | 251 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000252](../../tests/test_api.py#L252) | 252 | `"    assert response[\"kind\"] == \"web_research\""` | — |
| [SRC-3451CC474D-L000253](../../tests/test_api.py#L253) | 253 | `"    assert response[\"sources\"][0][\"url\"] == \"https://example.com\""` | — |
| [SRC-3451CC474D-L000254](../../tests/test_api.py#L254) | 254 | `""` | — |
| [SRC-3451CC474D-L000255](../../tests/test_api.py#L255) | 255 | `""` | — |
| [SRC-3451CC474D-L000256](../../tests/test_api.py#L256) | 256 | `""` | — |
| [SRC-3451CC474D-L000257](../../tests/test_api.py#L257) | 257 | `"def test_live_diagnostics_endpoint_returns_report_without_secrets(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000258](../../tests/test_api.py#L258) | 258 | `"    from api.omarai import WebAgent"` | — |
| [SRC-3451CC474D-L000259](../../tests/test_api.py#L259) | 259 | `""` | — |
| [SRC-3451CC474D-L000260](../../tests/test_api.py#L260) | 260 | `"    def fake_diagnostics(self, test_model=True, test_social=False):"` | — |
| [SRC-3451CC474D-L000261](../../tests/test_api.py#L261) | 261 | `"        return {"` | — |
| [SRC-3451CC474D-L000262](../../tests/test_api.py#L262) | 262 | `"            \"overall_status\": \"passed\","` | — |
| [SRC-3451CC474D-L000263](../../tests/test_api.py#L263) | 263 | `"            \"checks\": {"` | — |
| [SRC-3451CC474D-L000264](../../tests/test_api.py#L264) | 264 | `"                \"web_search\": {\"status\": \"passed\", \"result_count\": 4},"` | — |
| [SRC-3451CC474D-L000265](../../tests/test_api.py#L265) | 265 | `"                \"language_model\": {\"status\": \"passed\", \"response_received\": True},"` | — |
| [SRC-3451CC474D-L000266](../../tests/test_api.py#L266) | 266 | `"                \"social_search\": {\"status\": \"skipped\"},"` | — |
| [SRC-3451CC474D-L000267](../../tests/test_api.py#L267) | 267 | `"            },"` | — |
| [SRC-3451CC474D-L000268](../../tests/test_api.py#L268) | 268 | `"            \"model_usage\": [{"` | — |
| [SRC-3451CC474D-L000269](../../tests/test_api.py#L269) | 269 | `"                \"requested_model\": \"google/gemma-4-31b-it:free\","` | — |
| [SRC-3451CC474D-L000270](../../tests/test_api.py#L270) | 270 | `"                \"used_model\": \"google/gemma-4-31b-it:free\","` | — |
| [SRC-3451CC474D-L000271](../../tests/test_api.py#L271) | 271 | `"                \"fallback_used\": \"false\","` | — |
| [SRC-3451CC474D-L000272](../../tests/test_api.py#L272) | 272 | `"            }],"` | — |
| [SRC-3451CC474D-L000273](../../tests/test_api.py#L273) | 273 | `"        }"` | — |
| [SRC-3451CC474D-L000274](../../tests/test_api.py#L274) | 274 | `""` | — |
| [SRC-3451CC474D-L000275](../../tests/test_api.py#L275) | 275 | `"    monkeypatch.setattr(WebAgent, \"diagnostics\", fake_diagnostics)"` | — |
| [SRC-3451CC474D-L000276](../../tests/test_api.py#L276) | 276 | `"    status, report = request_json("` | — |
| [SRC-3451CC474D-L000277](../../tests/test_api.py#L277) | 277 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000278](../../tests/test_api.py#L278) | 278 | `"        \"/api/diagnostics\","` | — |
| [SRC-3451CC474D-L000279](../../tests/test_api.py#L279) | 279 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000280](../../tests/test_api.py#L280) | 280 | `"        payload={\"test_model\": True, \"test_social\": False},"` | — |
| [SRC-3451CC474D-L000281](../../tests/test_api.py#L281) | 281 | `"    )"` | — |
| [SRC-3451CC474D-L000282](../../tests/test_api.py#L282) | 282 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000283](../../tests/test_api.py#L283) | 283 | `"    assert report[\"overall_status\"] == \"passed\""` | — |
| [SRC-3451CC474D-L000284](../../tests/test_api.py#L284) | 284 | `"    assert report[\"checks\"][\"web_search\"][\"result_count\"] == 4"` | — |
| [SRC-3451CC474D-L000285](../../tests/test_api.py#L285) | 285 | `"    assert \"api_key\" not in report"` | — |
| [SRC-3451CC474D-L000286](../../tests/test_api.py#L286) | 286 | `"    assert \"secret\" not in str(report)"` | — |
| [SRC-3451CC474D-L000287](../../tests/test_api.py#L287) | 287 | `""` | — |
| [SRC-3451CC474D-L000288](../../tests/test_api.py#L288) | 288 | `""` | — |
| [SRC-3451CC474D-L000289](../../tests/test_api.py#L289) | 289 | `"def test_diagnostics_endpoint_requires_boolean_options(local_api):"` | — |
| [SRC-3451CC474D-L000290](../../tests/test_api.py#L290) | 290 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000291](../../tests/test_api.py#L291) | 291 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000292](../../tests/test_api.py#L292) | 292 | `"        \"/api/diagnostics\","` | — |
| [SRC-3451CC474D-L000293](../../tests/test_api.py#L293) | 293 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000294](../../tests/test_api.py#L294) | 294 | `"        payload={\"test_model\": \"yes\", \"test_social\": False},"` | — |
| [SRC-3451CC474D-L000295](../../tests/test_api.py#L295) | 295 | `"    )"` | — |
| [SRC-3451CC474D-L000296](../../tests/test_api.py#L296) | 296 | `"    assert status == 400"` | — |
| [SRC-3451CC474D-L000297](../../tests/test_api.py#L297) | 297 | `"    assert \"booleans\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000298](../../tests/test_api.py#L298) | 298 | `""` | — |
| [SRC-3451CC474D-L000299](../../tests/test_api.py#L299) | 299 | `""` | — |
| [SRC-3451CC474D-L000300](../../tests/test_api.py#L300) | 300 | `""` | — |
| [SRC-3451CC474D-L000301](../../tests/test_api.py#L301) | 301 | `"def test_rate_limit_ignores_spoofed_forwarded_for_by_default(monkeypatch):"` | — |
| [SRC-3451CC474D-L000302](../../tests/test_api.py#L302) | 302 | `"    monkeypatch.delenv(\"OMARAI_TRUST_PROXY_HEADERS\", raising=False)"` | — |
| [SRC-3451CC474D-L000303](../../tests/test_api.py#L303) | 303 | `"    handler = SimpleNamespace("` | — |
| [SRC-3451CC474D-L000304](../../tests/test_api.py#L304) | 304 | `"        headers={\"X-Forwarded-For\": \"198.51.100.77, 203.0.113.10\"},"` | — |
| [SRC-3451CC474D-L000305](../../tests/test_api.py#L305) | 305 | `"        client_address=(\"192.0.2.44\", 12345),"` | — |
| [SRC-3451CC474D-L000306](../../tests/test_api.py#L306) | 306 | `"    )"` | — |
| [SRC-3451CC474D-L000307](../../tests/test_api.py#L307) | 307 | `"    assert Handler._rate_limit_client_key(handler) == \"192.0.2.44\""` | — |
| [SRC-3451CC474D-L000308](../../tests/test_api.py#L308) | 308 | `""` | — |
| [SRC-3451CC474D-L000309](../../tests/test_api.py#L309) | 309 | `""` | — |
| [SRC-3451CC474D-L000310](../../tests/test_api.py#L310) | 310 | `"def test_rate_limit_uses_rightmost_valid_proxy_ip_only_when_enabled(monkeypatch):"` | — |
| [SRC-3451CC474D-L000311](../../tests/test_api.py#L311) | 311 | `"    monkeypatch.setenv(\"OMARAI_TRUST_PROXY_HEADERS\", \"1\")"` | — |
| [SRC-3451CC474D-L000312](../../tests/test_api.py#L312) | 312 | `"    handler = SimpleNamespace("` | — |
| [SRC-3451CC474D-L000313](../../tests/test_api.py#L313) | 313 | `"        headers={\"X-Forwarded-For\": \"198.51.100.77, 203.0.113.10\"},"` | — |
| [SRC-3451CC474D-L000314](../../tests/test_api.py#L314) | 314 | `"        client_address=(\"192.0.2.44\", 12345),"` | — |
| [SRC-3451CC474D-L000315](../../tests/test_api.py#L315) | 315 | `"    )"` | — |
| [SRC-3451CC474D-L000316](../../tests/test_api.py#L316) | 316 | `"    assert Handler._rate_limit_client_key(handler) == \"203.0.113.10\""` | — |
| [SRC-3451CC474D-L000317](../../tests/test_api.py#L317) | 317 | `""` | — |
| [SRC-3451CC474D-L000318](../../tests/test_api.py#L318) | 318 | `""` | — |
| [SRC-3451CC474D-L000319](../../tests/test_api.py#L319) | 319 | `"def test_rate_limit_proxy_header_invalid_value_falls_back_to_peer_ip(monkeypatch):"` | — |
| [SRC-3451CC474D-L000320](../../tests/test_api.py#L320) | 320 | `"    monkeypatch.setenv(\"OMARAI_TRUST_PROXY_HEADERS\", \"1\")"` | — |
| [SRC-3451CC474D-L000321](../../tests/test_api.py#L321) | 321 | `"    handler = SimpleNamespace("` | — |
| [SRC-3451CC474D-L000322](../../tests/test_api.py#L322) | 322 | `"        headers={\"X-Forwarded-For\": \"198.51.100.77, not-an-ip\"},"` | — |
| [SRC-3451CC474D-L000323](../../tests/test_api.py#L323) | 323 | `"        client_address=(\"192.0.2.44\", 12345),"` | — |
| [SRC-3451CC474D-L000324](../../tests/test_api.py#L324) | 324 | `"    )"` | — |
| [SRC-3451CC474D-L000325](../../tests/test_api.py#L325) | 325 | `"    assert Handler._rate_limit_client_key(handler) == \"192.0.2.44\""` | — |
| [SRC-3451CC474D-L000326](../../tests/test_api.py#L326) | 326 | `""` | — |
| [SRC-3451CC474D-L000327](../../tests/test_api.py#L327) | 327 | `""` | — |
| [SRC-3451CC474D-L000328](../../tests/test_api.py#L328) | 328 | `"def test_public_api_authentication_and_rate_limit_precede_json_parsing(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000329](../../tests/test_api.py#L329) | 329 | `"    \"\"\"Reject untrusted API calls before parsing bodies and throttle repeated failures.\"\"\""` | — |
| [SRC-3451CC474D-L000330](../../tests/test_api.py#L330) | 330 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000331](../../tests/test_api.py#L331) | 331 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"z\" * 48)"` | — |
| [SRC-3451CC474D-L000332](../../tests/test_api.py#L332) | 332 | `"    monkeypatch.setattr(Handler, \"RATE_LIMIT_REQUESTS\", 1)"` | — |
| [SRC-3451CC474D-L000333](../../tests/test_api.py#L333) | 333 | `"    with Handler._rate_lock:"` | — |
| [SRC-3451CC474D-L000334](../../tests/test_api.py#L334) | 334 | `"        Handler._request_times.clear()"` | — |
| [SRC-3451CC474D-L000335](../../tests/test_api.py#L335) | 335 | `"    request = Request("` | — |
| [SRC-3451CC474D-L000336](../../tests/test_api.py#L336) | 336 | `"        local_api + \"/api/agent\","` | — |
| [SRC-3451CC474D-L000337](../../tests/test_api.py#L337) | 337 | `"        data=b\"invalid-json-body\","` | — |
| [SRC-3451CC474D-L000338](../../tests/test_api.py#L338) | 338 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000339](../../tests/test_api.py#L339) | 339 | `"        headers={\"Content-Type\": \"application/json\"},"` | — |
| [SRC-3451CC474D-L000340](../../tests/test_api.py#L340) | 340 | `"    )"` | — |
| [SRC-3451CC474D-L000341](../../tests/test_api.py#L341) | 341 | `"    try:"` | — |
| [SRC-3451CC474D-L000342](../../tests/test_api.py#L342) | 342 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000343](../../tests/test_api.py#L343) | 343 | `"            first_status = response.status"` | — |
| [SRC-3451CC474D-L000344](../../tests/test_api.py#L344) | 344 | `"    except HTTPError as error:"` | — |
| [SRC-3451CC474D-L000345](../../tests/test_api.py#L345) | 345 | `"        first_status = error.code"` | — |
| [SRC-3451CC474D-L000346](../../tests/test_api.py#L346) | 346 | `"    assert first_status == 401"` | — |
| [SRC-3451CC474D-L000347](../../tests/test_api.py#L347) | 347 | `""` | — |
| [SRC-3451CC474D-L000348](../../tests/test_api.py#L348) | 348 | `"    try:"` | — |
| [SRC-3451CC474D-L000349](../../tests/test_api.py#L349) | 349 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000350](../../tests/test_api.py#L350) | 350 | `"            second_status = response.status"` | — |
| [SRC-3451CC474D-L000351](../../tests/test_api.py#L351) | 351 | `"    except HTTPError as error:"` | — |
| [SRC-3451CC474D-L000352](../../tests/test_api.py#L352) | 352 | `"        second_status = error.code"` | — |
| [SRC-3451CC474D-L000353](../../tests/test_api.py#L353) | 353 | `"    assert second_status == 429"` | — |
| [SRC-3451CC474D-L000354](../../tests/test_api.py#L354) | 354 | `""` | — |
| [SRC-3451CC474D-L000355](../../tests/test_api.py#L355) | 355 | `""` | — |
| [SRC-3451CC474D-L000356](../../tests/test_api.py#L356) | 356 | `"def test_hosted_api_requires_private_token_for_search_and_lead_data(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000357](../../tests/test_api.py#L357) | 357 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000358](../../tests/test_api.py#L358) | 358 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"x\" * 48)"` | — |
| [SRC-3451CC474D-L000359](../../tests/test_api.py#L359) | 359 | `""` | — |
| [SRC-3451CC474D-L000360](../../tests/test_api.py#L360) | 360 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000361](../../tests/test_api.py#L361) | 361 | `"        local_api, \"/api/analyze\", method=\"POST\", payload={\"text\": \"test\"}"` | — |
| [SRC-3451CC474D-L000362](../../tests/test_api.py#L362) | 362 | `"    )"` | — |
| [SRC-3451CC474D-L000363](../../tests/test_api.py#L363) | 363 | `"    assert status == 401"` | — |
| [SRC-3451CC474D-L000364](../../tests/test_api.py#L364) | 364 | `"    assert \"رمز الوصول\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000365](../../tests/test_api.py#L365) | 365 | `""` | — |
| [SRC-3451CC474D-L000366](../../tests/test_api.py#L366) | 366 | `"    status, error = request_json(local_api, \"/api/leads\")"` | — |
| [SRC-3451CC474D-L000367](../../tests/test_api.py#L367) | 367 | `"    assert status == 401"` | — |
| [SRC-3451CC474D-L000368](../../tests/test_api.py#L368) | 368 | `""` | — |
| [SRC-3451CC474D-L000369](../../tests/test_api.py#L369) | 369 | `"    headers = {\"Authorization\": \"Bearer \" + \"x\" * 48}"` | — |
| [SRC-3451CC474D-L000370](../../tests/test_api.py#L370) | 370 | `"    status, result = request_json("` | — |
| [SRC-3451CC474D-L000371](../../tests/test_api.py#L371) | 371 | `"        local_api, \"/api/analyze\", method=\"POST\", payload={\"text\": \"بدور على شقة\"}, headers=headers"` | — |
| [SRC-3451CC474D-L000372](../../tests/test_api.py#L372) | 372 | `"    )"` | — |
| [SRC-3451CC474D-L000373](../../tests/test_api.py#L373) | 373 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000374](../../tests/test_api.py#L374) | 374 | `"    assert \"score\" in result"` | — |
| [SRC-3451CC474D-L000375](../../tests/test_api.py#L375) | 375 | `""` | — |
| [SRC-3451CC474D-L000376](../../tests/test_api.py#L376) | 376 | `"    status, result = request_json(local_api, \"/api/leads\", headers=headers)"` | — |
| [SRC-3451CC474D-L000377](../../tests/test_api.py#L377) | 377 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000378](../../tests/test_api.py#L378) | 378 | `"    assert result[\"count\"] == 0"` | — |
| [SRC-3451CC474D-L000379](../../tests/test_api.py#L379) | 379 | `""` | — |
| [SRC-3451CC474D-L000380](../../tests/test_api.py#L380) | 380 | `""` | — |
| [SRC-3451CC474D-L000381](../../tests/test_api.py#L381) | 381 | `"def test_hosted_api_rate_limits_authenticated_requests(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000382](../../tests/test_api.py#L382) | 382 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000383](../../tests/test_api.py#L383) | 383 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"y\" * 48)"` | — |
| [SRC-3451CC474D-L000384](../../tests/test_api.py#L384) | 384 | `"    monkeypatch.setattr(Handler, \"RATE_LIMIT_REQUESTS\", 1)"` | — |
| [SRC-3451CC474D-L000385](../../tests/test_api.py#L385) | 385 | `"    with Handler._rate_lock:"` | — |
| [SRC-3451CC474D-L000386](../../tests/test_api.py#L386) | 386 | `"        Handler._request_times.clear()"` | — |
| [SRC-3451CC474D-L000387](../../tests/test_api.py#L387) | 387 | `"    headers = {\"Authorization\": \"Bearer \" + \"y\" * 48}"` | — |
| [SRC-3451CC474D-L000388](../../tests/test_api.py#L388) | 388 | `""` | — |
| [SRC-3451CC474D-L000389](../../tests/test_api.py#L389) | 389 | `"    status, _ = request_json("` | — |
| [SRC-3451CC474D-L000390](../../tests/test_api.py#L390) | 390 | `"        local_api, \"/api/analyze\", method=\"POST\", payload={\"text\": \"first\"}, headers=headers"` | — |
| [SRC-3451CC474D-L000391](../../tests/test_api.py#L391) | 391 | `"    )"` | — |
| [SRC-3451CC474D-L000392](../../tests/test_api.py#L392) | 392 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000393](../../tests/test_api.py#L393) | 393 | `""` | — |
| [SRC-3451CC474D-L000394](../../tests/test_api.py#L394) | 394 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000395](../../tests/test_api.py#L395) | 395 | `"        local_api, \"/api/analyze\", method=\"POST\", payload={\"text\": \"second\"}, headers=headers"` | — |
| [SRC-3451CC474D-L000396](../../tests/test_api.py#L396) | 396 | `"    )"` | — |
| [SRC-3451CC474D-L000397](../../tests/test_api.py#L397) | 397 | `"    assert status == 429"` | — |
| [SRC-3451CC474D-L000398](../../tests/test_api.py#L398) | 398 | `"    assert \"حد الطلبات\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000399](../../tests/test_api.py#L399) | 399 | `""` | — |
| [SRC-3451CC474D-L000400](../../tests/test_api.py#L400) | 400 | `""` | — |
| [SRC-3451CC474D-L000401](../../tests/test_api.py#L401) | 401 | `""` | — |
| [SRC-3451CC474D-L000402](../../tests/test_api.py#L402) | 402 | `"def test_public_binding_requires_explicit_deployment_flag_and_strong_token(monkeypatch):"` | — |
| [SRC-3451CC474D-L000403](../../tests/test_api.py#L403) | 403 | `"    from api.omarai import serve"` | — |
| [SRC-3451CC474D-L000404](../../tests/test_api.py#L404) | 404 | `""` | — |
| [SRC-3451CC474D-L000405](../../tests/test_api.py#L405) | 405 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000406](../../tests/test_api.py#L406) | 406 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000407](../../tests/test_api.py#L407) | 407 | `"    with pytest.raises(ValueError, match=\"Public binding requires\"):"` | — |
| [SRC-3451CC474D-L000408](../../tests/test_api.py#L408) | 408 | `"        serve(\"0.0.0.0\", 0)"` | — |
| [SRC-3451CC474D-L000409](../../tests/test_api.py#L409) | 409 | `""` | — |
