# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **023**
- سجلات الأسطر: **800**
- النطاق: SRC-1C77C97630-L000238 إلى SRC-DA61479D59-L000044
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-1C77C97630 — [tests/test_answer_validation.py](../../tests/test_answer_validation.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-3451CC474D-L000326](../../tests/test_api.py#L326) | 326 | `"def test_public_api_authentication_and_rate_limit_precede_json_parsing(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000327](../../tests/test_api.py#L327) | 327 | `"    \"\"\"Reject untrusted API calls before parsing bodies and throttle repeated failures.\"\"\""` | — |
| [SRC-3451CC474D-L000328](../../tests/test_api.py#L328) | 328 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000329](../../tests/test_api.py#L329) | 329 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"z\" * 48)"` | — |
| [SRC-3451CC474D-L000330](../../tests/test_api.py#L330) | 330 | `"    monkeypatch.setattr(Handler, \"RATE_LIMIT_REQUESTS\", 1)"` | — |
| [SRC-3451CC474D-L000331](../../tests/test_api.py#L331) | 331 | `"    with Handler._rate_lock:"` | — |
| [SRC-3451CC474D-L000332](../../tests/test_api.py#L332) | 332 | `"        Handler._request_times.clear()"` | — |
| [SRC-3451CC474D-L000333](../../tests/test_api.py#L333) | 333 | `"    request = Request("` | — |
| [SRC-3451CC474D-L000334](../../tests/test_api.py#L334) | 334 | `"        local_api + \"/api/agent\","` | — |
| [SRC-3451CC474D-L000335](../../tests/test_api.py#L335) | 335 | `"        data=b\"invalid-json-body\","` | — |
| [SRC-3451CC474D-L000336](../../tests/test_api.py#L336) | 336 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000337](../../tests/test_api.py#L337) | 337 | `"        headers={\"Content-Type\": \"application/json\"},"` | — |
| [SRC-3451CC474D-L000338](../../tests/test_api.py#L338) | 338 | `"    )"` | — |
| [SRC-3451CC474D-L000339](../../tests/test_api.py#L339) | 339 | `"    try:"` | — |
| [SRC-3451CC474D-L000340](../../tests/test_api.py#L340) | 340 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000341](../../tests/test_api.py#L341) | 341 | `"            first_status = response.status"` | — |
| [SRC-3451CC474D-L000342](../../tests/test_api.py#L342) | 342 | `"    except HTTPError as error:"` | — |
| [SRC-3451CC474D-L000343](../../tests/test_api.py#L343) | 343 | `"        first_status = error.code"` | — |
| [SRC-3451CC474D-L000344](../../tests/test_api.py#L344) | 344 | `"    assert first_status == 401"` | — |
| [SRC-3451CC474D-L000345](../../tests/test_api.py#L345) | 345 | `""` | — |
| [SRC-3451CC474D-L000346](../../tests/test_api.py#L346) | 346 | `"    try:"` | — |
| [SRC-3451CC474D-L000347](../../tests/test_api.py#L347) | 347 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000348](../../tests/test_api.py#L348) | 348 | `"            second_status = response.status"` | — |
| [SRC-3451CC474D-L000349](../../tests/test_api.py#L349) | 349 | `"    except HTTPError as error:"` | — |
| [SRC-3451CC474D-L000350](../../tests/test_api.py#L350) | 350 | `"        second_status = error.code"` | — |
| [SRC-3451CC474D-L000351](../../tests/test_api.py#L351) | 351 | `"    assert second_status == 429"` | — |
| [SRC-3451CC474D-L000352](../../tests/test_api.py#L352) | 352 | `""` | — |
| [SRC-3451CC474D-L000353](../../tests/test_api.py#L353) | 353 | `""` | — |
| [SRC-3451CC474D-L000354](../../tests/test_api.py#L354) | 354 | `"def test_hosted_api_requires_private_token_for_search_and_lead_data(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000355](../../tests/test_api.py#L355) | 355 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000356](../../tests/test_api.py#L356) | 356 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"x\" * 48)"` | — |
| [SRC-3451CC474D-L000357](../../tests/test_api.py#L357) | 357 | `""` | — |
| [SRC-3451CC474D-L000358](../../tests/test_api.py#L358) | 358 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000359](../../tests/test_api.py#L359) | 359 | `"        local_api, \"/api/analyze\", method=\"POST\", payload={\"text\": \"test\"}"` | — |
| [SRC-3451CC474D-L000360](../../tests/test_api.py#L360) | 360 | `"    )"` | — |
| [SRC-3451CC474D-L000361](../../tests/test_api.py#L361) | 361 | `"    assert status == 401"` | — |
| [SRC-3451CC474D-L000362](../../tests/test_api.py#L362) | 362 | `"    assert \"رمز الوصول\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000363](../../tests/test_api.py#L363) | 363 | `""` | — |
| [SRC-3451CC474D-L000364](../../tests/test_api.py#L364) | 364 | `"    status, error = request_json(local_api, \"/api/leads\")"` | — |
| [SRC-3451CC474D-L000365](../../tests/test_api.py#L365) | 365 | `"    assert status == 401"` | — |
| [SRC-3451CC474D-L000366](../../tests/test_api.py#L366) | 366 | `""` | — |
| [SRC-3451CC474D-L000367](../../tests/test_api.py#L367) | 367 | `"    headers = {\"Authorization\": \"Bearer \" + \"x\" * 48}"` | — |
| [SRC-3451CC474D-L000368](../../tests/test_api.py#L368) | 368 | `"    status, result = request_json("` | — |
| [SRC-3451CC474D-L000369](../../tests/test_api.py#L369) | 369 | `"        local_api, \"/api/analyze\", method=\"POST\", payload={\"text\": \"بدور على شقة\"}, headers=headers"` | — |
| [SRC-3451CC474D-L000370](../../tests/test_api.py#L370) | 370 | `"    )"` | — |
| [SRC-3451CC474D-L000371](../../tests/test_api.py#L371) | 371 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000372](../../tests/test_api.py#L372) | 372 | `"    assert \"score\" in result"` | — |
| [SRC-3451CC474D-L000373](../../tests/test_api.py#L373) | 373 | `""` | — |
| [SRC-3451CC474D-L000374](../../tests/test_api.py#L374) | 374 | `"    status, result = request_json(local_api, \"/api/leads\", headers=headers)"` | — |
| [SRC-3451CC474D-L000375](../../tests/test_api.py#L375) | 375 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000376](../../tests/test_api.py#L376) | 376 | `"    assert result[\"count\"] == 0"` | — |
| [SRC-3451CC474D-L000377](../../tests/test_api.py#L377) | 377 | `""` | — |
| [SRC-3451CC474D-L000378](../../tests/test_api.py#L378) | 378 | `""` | — |
| [SRC-3451CC474D-L000379](../../tests/test_api.py#L379) | 379 | `"def test_hosted_api_rate_limits_authenticated_requests(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000380](../../tests/test_api.py#L380) | 380 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000381](../../tests/test_api.py#L381) | 381 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"y\" * 48)"` | — |
| [SRC-3451CC474D-L000382](../../tests/test_api.py#L382) | 382 | `"    monkeypatch.setattr(Handler, \"RATE_LIMIT_REQUESTS\", 1)"` | — |
| [SRC-3451CC474D-L000383](../../tests/test_api.py#L383) | 383 | `"    with Handler._rate_lock:"` | — |
| [SRC-3451CC474D-L000384](../../tests/test_api.py#L384) | 384 | `"        Handler._request_times.clear()"` | — |
| [SRC-3451CC474D-L000385](../../tests/test_api.py#L385) | 385 | `"    headers = {\"Authorization\": \"Bearer \" + \"y\" * 48}"` | — |
| [SRC-3451CC474D-L000386](../../tests/test_api.py#L386) | 386 | `""` | — |
| [SRC-3451CC474D-L000387](../../tests/test_api.py#L387) | 387 | `"    status, _ = request_json("` | — |
| [SRC-3451CC474D-L000388](../../tests/test_api.py#L388) | 388 | `"        local_api, \"/api/analyze\", method=\"POST\", payload={\"text\": \"first\"}, headers=headers"` | — |
| [SRC-3451CC474D-L000389](../../tests/test_api.py#L389) | 389 | `"    )"` | — |
| [SRC-3451CC474D-L000390](../../tests/test_api.py#L390) | 390 | `"    assert status == 200"` | — |
| [SRC-3451CC474D-L000391](../../tests/test_api.py#L391) | 391 | `""` | — |
| [SRC-3451CC474D-L000392](../../tests/test_api.py#L392) | 392 | `"    status, error = request_json("` | — |
| [SRC-3451CC474D-L000393](../../tests/test_api.py#L393) | 393 | `"        local_api, \"/api/analyze\", method=\"POST\", payload={\"text\": \"second\"}, headers=headers"` | — |
| [SRC-3451CC474D-L000394](../../tests/test_api.py#L394) | 394 | `"    )"` | — |
| [SRC-3451CC474D-L000395](../../tests/test_api.py#L395) | 395 | `"    assert status == 429"` | — |
| [SRC-3451CC474D-L000396](../../tests/test_api.py#L396) | 396 | `"    assert \"حد الطلبات\" in error[\"error\"]"` | — |
| [SRC-3451CC474D-L000397](../../tests/test_api.py#L397) | 397 | `""` | — |
| [SRC-3451CC474D-L000398](../../tests/test_api.py#L398) | 398 | `""` | — |
| [SRC-3451CC474D-L000399](../../tests/test_api.py#L399) | 399 | `""` | — |
| [SRC-3451CC474D-L000400](../../tests/test_api.py#L400) | 400 | `"def test_public_binding_requires_explicit_deployment_flag_and_strong_token(monkeypatch):"` | — |
| [SRC-3451CC474D-L000401](../../tests/test_api.py#L401) | 401 | `"    from api.omarai import serve"` | — |
| [SRC-3451CC474D-L000402](../../tests/test_api.py#L402) | 402 | `""` | — |
| [SRC-3451CC474D-L000403](../../tests/test_api.py#L403) | 403 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000404](../../tests/test_api.py#L404) | 404 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000405](../../tests/test_api.py#L405) | 405 | `"    with pytest.raises(ValueError, match=\"Public binding requires\"):"` | — |
| [SRC-3451CC474D-L000406](../../tests/test_api.py#L406) | 406 | `"        serve(\"0.0.0.0\", 0)"` | — |
| [SRC-3451CC474D-L000407](../../tests/test_api.py#L407) | 407 | `""` | — |
| [SRC-3451CC474D-L000408](../../tests/test_api.py#L408) | 408 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000409](../../tests/test_api.py#L409) | 409 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", \"short\")"` | — |
| [SRC-3451CC474D-L000410](../../tests/test_api.py#L410) | 410 | `"    with pytest.raises(ValueError, match=\"at least 32 characters\"):"` | — |
| [SRC-3451CC474D-L000411](../../tests/test_api.py#L411) | 411 | `"        serve(\"0.0.0.0\", 0)"` | — |
| [SRC-3451CC474D-L000412](../../tests/test_api.py#L412) | 412 | `""` | — |
| [SRC-3451CC474D-L000413](../../tests/test_api.py#L413) | 413 | `"def test_rate_limiter_prunes_expired_client_buckets(monkeypatch):"` | — |
| [SRC-3451CC474D-L000414](../../tests/test_api.py#L414) | 414 | `"    \"\"\"Client IPs do not accumulate forever after their 60-second window expires.\"\"\""` | — |
| [SRC-3451CC474D-L000415](../../tests/test_api.py#L415) | 415 | `"    monkeypatch.delenv(\"OMARAI_TRUST_PROXY_HEADERS\", raising=False)"` | — |
| [SRC-3451CC474D-L000416](../../tests/test_api.py#L416) | 416 | `"    monkeypatch.setattr(Handler, \"_request_times\", defaultdict(deque))"` | — |
| [SRC-3451CC474D-L000417](../../tests/test_api.py#L417) | 417 | `"    monkeypatch.setattr(Handler, \"_rate_last_cleanup\", 0.0)"` | — |
| [SRC-3451CC474D-L000418](../../tests/test_api.py#L418) | 418 | `"    clock = {\"now\": 100.0}"` | — |
| [SRC-3451CC474D-L000419](../../tests/test_api.py#L419) | 419 | `"    monkeypatch.setattr(\"api.omarai.time.monotonic\", lambda: clock[\"now\"])"` | — |
| [SRC-3451CC474D-L000420](../../tests/test_api.py#L420) | 420 | `""` | — |
| [SRC-3451CC474D-L000421](../../tests/test_api.py#L421) | 421 | `"    class FakeHandler(Handler):"` | — |
| [SRC-3451CC474D-L000422](../../tests/test_api.py#L422) | 422 | `"        def __init__(self, ip):"` | — |
| [SRC-3451CC474D-L000423](../../tests/test_api.py#L423) | 423 | `"            self.headers = {}"` | — |
| [SRC-3451CC474D-L000424](../../tests/test_api.py#L424) | 424 | `"            self.client_address = (ip, 1234)"` | — |
| [SRC-3451CC474D-L000425](../../tests/test_api.py#L425) | 425 | `""` | — |
| [SRC-3451CC474D-L000426](../../tests/test_api.py#L426) | 426 | `"    first = FakeHandler(\"192.0.2.1\")"` | — |
| [SRC-3451CC474D-L000427](../../tests/test_api.py#L427) | 427 | `"    second = FakeHandler(\"192.0.2.2\")"` | — |
| [SRC-3451CC474D-L000428](../../tests/test_api.py#L428) | 428 | `"    assert first._rate_limit_ok() is True"` | — |
| [SRC-3451CC474D-L000429](../../tests/test_api.py#L429) | 429 | `"    assert \"192.0.2.1\" in Handler._request_times"` | — |
| [SRC-3451CC474D-L000430](../../tests/test_api.py#L430) | 430 | `""` | — |
| [SRC-3451CC474D-L000431](../../tests/test_api.py#L431) | 431 | `"    clock[\"now\"] = 161.0"` | — |
| [SRC-3451CC474D-L000432](../../tests/test_api.py#L432) | 432 | `"    assert second._rate_limit_ok() is True"` | — |
| [SRC-3451CC474D-L000433](../../tests/test_api.py#L433) | 433 | `"    assert \"192.0.2.1\" not in Handler._request_times"` | — |
| [SRC-3451CC474D-L000434](../../tests/test_api.py#L434) | 434 | `"    assert \"192.0.2.2\" in Handler._request_times"` | — |
| [SRC-3451CC474D-L000435](../../tests/test_api.py#L435) | 435 | `""` | — |
| [SRC-3451CC474D-L000436](../../tests/test_api.py#L436) | 436 | `""` | — |
| [SRC-3451CC474D-L000437](../../tests/test_api.py#L437) | 437 | `""` | — |
| [SRC-3451CC474D-L000438](../../tests/test_api.py#L438) | 438 | `"def test_agent_concurrency_cap_rejects_work_when_all_slots_are_busy(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000439](../../tests/test_api.py#L439) | 439 | `"    from api.omarai import WebAgent"` | — |
| [SRC-3451CC474D-L000440](../../tests/test_api.py#L440) | 440 | `""` | — |
| [SRC-3451CC474D-L000441](../../tests/test_api.py#L441) | 441 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000442](../../tests/test_api.py#L442) | 442 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000443](../../tests/test_api.py#L443) | 443 | `"    monkeypatch.setattr(Handler, \"_request_times\", defaultdict(deque))"` | — |
| [SRC-3451CC474D-L000444](../../tests/test_api.py#L444) | 444 | `"    monkeypatch.setattr(Handler, \"_rate_last_cleanup\", 0.0)"` | — |
| [SRC-3451CC474D-L000445](../../tests/test_api.py#L445) | 445 | `"    monkeypatch.setattr(Handler, \"_agent_semaphore\", threading.BoundedSemaphore(1))"` | — |
| [SRC-3451CC474D-L000446](../../tests/test_api.py#L446) | 446 | `""` | — |
| [SRC-3451CC474D-L000447](../../tests/test_api.py#L447) | 447 | `"    entered = threading.Event()"` | — |
| [SRC-3451CC474D-L000448](../../tests/test_api.py#L448) | 448 | `"    release = threading.Event()"` | — |
| [SRC-3451CC474D-L000449](../../tests/test_api.py#L449) | 449 | `"    first_result = {}"` | — |
| [SRC-3451CC474D-L000450](../../tests/test_api.py#L450) | 450 | `""` | — |
| [SRC-3451CC474D-L000451](../../tests/test_api.py#L451) | 451 | `"    def slow_answer(self, question, history=None, mode=\"auto\"):"` | — |
| [SRC-3451CC474D-L000452](../../tests/test_api.py#L452) | 452 | `"        entered.set()"` | — |
| [SRC-3451CC474D-L000453](../../tests/test_api.py#L453) | 453 | `"        assert release.wait(timeout=2), \"test did not release the held research slot\""` | — |
| [SRC-3451CC474D-L000454](../../tests/test_api.py#L454) | 454 | `"        return {"` | — |
| [SRC-3451CC474D-L000455](../../tests/test_api.py#L455) | 455 | `"            \"answer\": \"نتيجة اختبار محدودة\","` | — |
| [SRC-3451CC474D-L000456](../../tests/test_api.py#L456) | 456 | `"            \"question\": question,"` | — |
| [SRC-3451CC474D-L000457](../../tests/test_api.py#L457) | 457 | `"            \"search_query\": question,"` | — |
| [SRC-3451CC474D-L000458](../../tests/test_api.py#L458) | 458 | `"            \"search_queries\": [],"` | — |
| [SRC-3451CC474D-L000459](../../tests/test_api.py#L459) | 459 | `"            \"search_report\": {\"search_attempted\": False, \"search_outcome\": \"not_attempted\"},"` | — |
| [SRC-3451CC474D-L000460](../../tests/test_api.py#L460) | 460 | `"            \"sources\": [],"` | — |
| [SRC-3451CC474D-L000461](../../tests/test_api.py#L461) | 461 | `"            \"used_language_model\": False,"` | — |
| [SRC-3451CC474D-L000462](../../tests/test_api.py#L462) | 462 | `"            \"used_web_search\": False,"` | — |
| [SRC-3451CC474D-L000463](../../tests/test_api.py#L463) | 463 | `"            \"search_attempted\": False,"` | — |
| [SRC-3451CC474D-L000464](../../tests/test_api.py#L464) | 464 | `"            \"used_social_search\": False,"` | — |
| [SRC-3451CC474D-L000465](../../tests/test_api.py#L465) | 465 | `"            \"warnings\": [],"` | — |
| [SRC-3451CC474D-L000466](../../tests/test_api.py#L466) | 466 | `"            \"kind\": \"web_fallback\","` | — |
| [SRC-3451CC474D-L000467](../../tests/test_api.py#L467) | 467 | `"        }"` | — |
| [SRC-3451CC474D-L000468](../../tests/test_api.py#L468) | 468 | `""` | — |
| [SRC-3451CC474D-L000469](../../tests/test_api.py#L469) | 469 | `"    monkeypatch.setattr(WebAgent, \"answer\", slow_answer)"` | — |
| [SRC-3451CC474D-L000470](../../tests/test_api.py#L470) | 470 | `""` | — |
| [SRC-3451CC474D-L000471](../../tests/test_api.py#L471) | 471 | `"    def first_request():"` | — |
| [SRC-3451CC474D-L000472](../../tests/test_api.py#L472) | 472 | `"        first_result[\"response\"] = request_json("` | — |
| [SRC-3451CC474D-L000473](../../tests/test_api.py#L473) | 473 | `"            local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"السؤال الأول\"}"` | — |
| [SRC-3451CC474D-L000474](../../tests/test_api.py#L474) | 474 | `"        )"` | — |
| [SRC-3451CC474D-L000475](../../tests/test_api.py#L475) | 475 | `""` | — |
| [SRC-3451CC474D-L000476](../../tests/test_api.py#L476) | 476 | `"    worker = threading.Thread(target=first_request, daemon=True)"` | — |
| [SRC-3451CC474D-L000477](../../tests/test_api.py#L477) | 477 | `"    worker.start()"` | — |
| [SRC-3451CC474D-L000478](../../tests/test_api.py#L478) | 478 | `"    try:"` | — |
| [SRC-3451CC474D-L000479](../../tests/test_api.py#L479) | 479 | `"        assert entered.wait(timeout=1), \"first request did not acquire the research slot\""` | — |
| [SRC-3451CC474D-L000480](../../tests/test_api.py#L480) | 480 | `"        status, payload = request_json("` | — |
| [SRC-3451CC474D-L000481](../../tests/test_api.py#L481) | 481 | `"            local_api, \"/api/agent\", method=\"POST\", payload={\"question\": \"السؤال الثاني\"}"` | — |
| [SRC-3451CC474D-L000482](../../tests/test_api.py#L482) | 482 | `"        )"` | — |
| [SRC-3451CC474D-L000483](../../tests/test_api.py#L483) | 483 | `"        assert status == 503"` | — |
| [SRC-3451CC474D-L000484](../../tests/test_api.py#L484) | 484 | `"        assert payload[\"retry_after_seconds\"] == 5"` | — |
| [SRC-3451CC474D-L000485](../../tests/test_api.py#L485) | 485 | `"        assert \"مشغولة\" in payload[\"error\"]"` | — |
| [SRC-3451CC474D-L000486](../../tests/test_api.py#L486) | 486 | `"    finally:"` | — |
| [SRC-3451CC474D-L000487](../../tests/test_api.py#L487) | 487 | `"        release.set()"` | — |
| [SRC-3451CC474D-L000488](../../tests/test_api.py#L488) | 488 | `"        worker.join(timeout=3)"` | — |
| [SRC-3451CC474D-L000489](../../tests/test_api.py#L489) | 489 | `""` | — |
| [SRC-3451CC474D-L000490](../../tests/test_api.py#L490) | 490 | `"    assert not worker.is_alive()"` | — |
| [SRC-3451CC474D-L000491](../../tests/test_api.py#L491) | 491 | `"    assert first_result[\"response\"][0] == 200"` | — |
| [SRC-3451CC474D-L000492](../../tests/test_api.py#L492) | 492 | `""` | — |
| [SRC-3451CC474D-L000493](../../tests/test_api.py#L493) | 493 | `""` | — |
| [SRC-3451CC474D-L000494](../../tests/test_api.py#L494) | 494 | `"def test_agent_concurrency_limit_has_hard_bounds(monkeypatch):"` | — |
| [SRC-3451CC474D-L000495](../../tests/test_api.py#L495) | 495 | `"    from api.omarai import _configured_agent_concurrency_limit"` | — |
| [SRC-3451CC474D-L000496](../../tests/test_api.py#L496) | 496 | `""` | — |
| [SRC-3451CC474D-L000497](../../tests/test_api.py#L497) | 497 | `"    monkeypatch.setenv(\"OMARAI_MAX_CONCURRENT_AGENT_REQUESTS\", \"99\")"` | — |
| [SRC-3451CC474D-L000498](../../tests/test_api.py#L498) | 498 | `"    assert _configured_agent_concurrency_limit() == 8"` | — |
| [SRC-3451CC474D-L000499](../../tests/test_api.py#L499) | 499 | `"    monkeypatch.setenv(\"OMARAI_MAX_CONCURRENT_AGENT_REQUESTS\", \"invalid\")"` | — |
| [SRC-3451CC474D-L000500](../../tests/test_api.py#L500) | 500 | `"    assert _configured_agent_concurrency_limit() == 4"` | — |
| [SRC-3451CC474D-L000501](../../tests/test_api.py#L501) | 501 | `""` | — |
| [SRC-3451CC474D-L000502](../../tests/test_api.py#L502) | 502 | `""` | — |
| [SRC-3451CC474D-L000503](../../tests/test_api.py#L503) | 503 | `"def test_api_rejects_oversized_request_body(local_api):"` | — |
| [SRC-3451CC474D-L000504](../../tests/test_api.py#L504) | 504 | `"    status, payload = request_json("` | — |
| [SRC-3451CC474D-L000505](../../tests/test_api.py#L505) | 505 | `"        local_api,"` | — |
| [SRC-3451CC474D-L000506](../../tests/test_api.py#L506) | 506 | `"        \"/api/analyze\","` | — |
| [SRC-3451CC474D-L000507](../../tests/test_api.py#L507) | 507 | `"        method=\"POST\","` | — |
| [SRC-3451CC474D-L000508](../../tests/test_api.py#L508) | 508 | `"        payload={\"text\": \"x\" * 200_001},"` | — |
| [SRC-3451CC474D-L000509](../../tests/test_api.py#L509) | 509 | `"    )"` | — |
| [SRC-3451CC474D-L000510](../../tests/test_api.py#L510) | 510 | `""` | — |
| [SRC-3451CC474D-L000511](../../tests/test_api.py#L511) | 511 | `"    assert status == 413"` | — |
| [SRC-3451CC474D-L000512](../../tests/test_api.py#L512) | 512 | `"    assert payload[\"error\"] == \"request too large\""` | — |
| [SRC-3451CC474D-L000513](../../tests/test_api.py#L513) | 513 | `""` | — |
| [SRC-3451CC474D-L000514](../../tests/test_api.py#L514) | 514 | `""` | — |
| [SRC-3451CC474D-L000515](../../tests/test_api.py#L515) | 515 | `"def test_api_rejects_malformed_content_length(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000516](../../tests/test_api.py#L516) | 516 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000517](../../tests/test_api.py#L517) | 517 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000518](../../tests/test_api.py#L518) | 518 | `"    host_port = local_api.rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000519](../../tests/test_api.py#L519) | 519 | `"    with socket.create_connection((host_port[0].removeprefix(\"http://\"), int(host_port[1])), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000520](../../tests/test_api.py#L520) | 520 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000521](../../tests/test_api.py#L521) | 521 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000522](../../tests/test_api.py#L522) | 522 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000523](../../tests/test_api.py#L523) | 523 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000524](../../tests/test_api.py#L524) | 524 | `"            b\"Content-Length: invalid\\r\\n\""` | — |
| [SRC-3451CC474D-L000525](../../tests/test_api.py#L525) | 525 | `"            b\"Connection: close\\r\\n\\r\\n\""` | — |
| [SRC-3451CC474D-L000526](../../tests/test_api.py#L526) | 526 | `"        )"` | — |
| [SRC-3451CC474D-L000527](../../tests/test_api.py#L527) | 527 | `"        response = b\"\""` | — |
| [SRC-3451CC474D-L000528](../../tests/test_api.py#L528) | 528 | `"        while True:"` | — |
| [SRC-3451CC474D-L000529](../../tests/test_api.py#L529) | 529 | `"            chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000530](../../tests/test_api.py#L530) | 530 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000531](../../tests/test_api.py#L531) | 531 | `"                break"` | — |
| [SRC-3451CC474D-L000532](../../tests/test_api.py#L532) | 532 | `"            response += chunk"` | — |
| [SRC-3451CC474D-L000533](../../tests/test_api.py#L533) | 533 | `""` | — |
| [SRC-3451CC474D-L000534](../../tests/test_api.py#L534) | 534 | `"    assert response.startswith(b\"HTTP/1.0 400\")"` | — |
| [SRC-3451CC474D-L000535](../../tests/test_api.py#L535) | 535 | `"    assert b\"valid Content-Length is required\" in response"` | — |
| [SRC-3451CC474D-L000536](../../tests/test_api.py#L536) | 536 | `""` | — |
| [SRC-3451CC474D-L000537](../../tests/test_api.py#L537) | 537 | `""` | — |
| [SRC-3451CC474D-L000538](../../tests/test_api.py#L538) | 538 | `"def test_api_returns_408_when_request_body_read_times_out(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000539](../../tests/test_api.py#L539) | 539 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000540](../../tests/test_api.py#L540) | 540 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000541](../../tests/test_api.py#L541) | 541 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_BODY_READ_TIMEOUT_SECONDS\", 0.1)"` | — |
| [SRC-3451CC474D-L000542](../../tests/test_api.py#L542) | 542 | `"    host_port = local_api.rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000543](../../tests/test_api.py#L543) | 543 | `"    with socket.create_connection((host_port[0].removeprefix(\"http://\"), int(host_port[1])), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000544](../../tests/test_api.py#L544) | 544 | `"        client.settimeout(2)"` | — |
| [SRC-3451CC474D-L000545](../../tests/test_api.py#L545) | 545 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000546](../../tests/test_api.py#L546) | 546 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000547](../../tests/test_api.py#L547) | 547 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000548](../../tests/test_api.py#L548) | 548 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000549](../../tests/test_api.py#L549) | 549 | `"            b\"Content-Length: 40\\r\\n\""` | — |
| [SRC-3451CC474D-L000550](../../tests/test_api.py#L550) | 550 | `"            b\"Connection: close\\r\\n\\r\\n\""` | — |
| [SRC-3451CC474D-L000551](../../tests/test_api.py#L551) | 551 | `"            b\"{}\""` | — |
| [SRC-3451CC474D-L000552](../../tests/test_api.py#L552) | 552 | `"        )"` | — |
| [SRC-3451CC474D-L000553](../../tests/test_api.py#L553) | 553 | `"        response = b\"\""` | — |
| [SRC-3451CC474D-L000554](../../tests/test_api.py#L554) | 554 | `"        while True:"` | — |
| [SRC-3451CC474D-L000555](../../tests/test_api.py#L555) | 555 | `"            chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000556](../../tests/test_api.py#L556) | 556 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000557](../../tests/test_api.py#L557) | 557 | `"                break"` | — |
| [SRC-3451CC474D-L000558](../../tests/test_api.py#L558) | 558 | `"            response += chunk"` | — |
| [SRC-3451CC474D-L000559](../../tests/test_api.py#L559) | 559 | `""` | — |
| [SRC-3451CC474D-L000560](../../tests/test_api.py#L560) | 560 | `"    assert response.startswith(b\"HTTP/1.0 408\")"` | — |
| [SRC-3451CC474D-L000561](../../tests/test_api.py#L561) | 561 | `"    assert b\"request body read timed out\" in response"` | — |
| [SRC-3451CC474D-L000562](../../tests/test_api.py#L562) | 562 | `""` | — |
| [SRC-3451CC474D-L000563](../../tests/test_api.py#L563) | 563 | `""` | — |
| [SRC-3451CC474D-L000564](../../tests/test_api.py#L564) | 564 | `"def test_api_absolute_body_deadline_stops_slow_trickle(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000565](../../tests/test_api.py#L565) | 565 | `"    \"\"\"A client must not evade the total deadline by sending before each idle timeout.\"\"\""` | — |
| [SRC-3451CC474D-L000566](../../tests/test_api.py#L566) | 566 | `"    import time"` | — |
| [SRC-3451CC474D-L000567](../../tests/test_api.py#L567) | 567 | `""` | — |
| [SRC-3451CC474D-L000568](../../tests/test_api.py#L568) | 568 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000569](../../tests/test_api.py#L569) | 569 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000570](../../tests/test_api.py#L570) | 570 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_BODY_READ_TIMEOUT_SECONDS\", 0.45)"` | — |
| [SRC-3451CC474D-L000571](../../tests/test_api.py#L571) | 571 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_BODY_IDLE_TIMEOUT_SECONDS\", 0.20)"` | — |
| [SRC-3451CC474D-L000572](../../tests/test_api.py#L572) | 572 | `"    host, port = local_api.removeprefix(\"http://\").rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000573](../../tests/test_api.py#L573) | 573 | `""` | — |
| [SRC-3451CC474D-L000574](../../tests/test_api.py#L574) | 574 | `"    with socket.create_connection((host, int(port)), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000575](../../tests/test_api.py#L575) | 575 | `"        client.settimeout(2)"` | — |
| [SRC-3451CC474D-L000576](../../tests/test_api.py#L576) | 576 | `"        started = time.monotonic()"` | — |
| [SRC-3451CC474D-L000577](../../tests/test_api.py#L577) | 577 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000578](../../tests/test_api.py#L578) | 578 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000579](../../tests/test_api.py#L579) | 579 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000580](../../tests/test_api.py#L580) | 580 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000581](../../tests/test_api.py#L581) | 581 | `"            b\"Content-Length: 100\\r\\n\""` | — |
| [SRC-3451CC474D-L000582](../../tests/test_api.py#L582) | 582 | `"            b\"Connection: close\\r\\n\\r\\n\""` | — |
| [SRC-3451CC474D-L000583](../../tests/test_api.py#L583) | 583 | `"            b\"{\""` | — |
| [SRC-3451CC474D-L000584](../../tests/test_api.py#L584) | 584 | `"        )"` | — |
| [SRC-3451CC474D-L000585](../../tests/test_api.py#L585) | 585 | `"        # Each fragment arrives before the 0.20s idle timeout, but the complete"` | — |
| [SRC-3451CC474D-L000586](../../tests/test_api.py#L586) | 586 | `"        # request body never arrives before the 0.45s absolute deadline."` | — |
| [SRC-3451CC474D-L000587](../../tests/test_api.py#L587) | 587 | `"        for fragment in (b'\"', b\"text\", b'\"', b\":\"):"` | — |
| [SRC-3451CC474D-L000588](../../tests/test_api.py#L588) | 588 | `"            time.sleep(0.08)"` | — |
| [SRC-3451CC474D-L000589](../../tests/test_api.py#L589) | 589 | `"            try:"` | — |
| [SRC-3451CC474D-L000590](../../tests/test_api.py#L590) | 590 | `"                client.sendall(fragment)"` | — |
| [SRC-3451CC474D-L000591](../../tests/test_api.py#L591) | 591 | `"            except OSError:"` | — |
| [SRC-3451CC474D-L000592](../../tests/test_api.py#L592) | 592 | `"                break"` | — |
| [SRC-3451CC474D-L000593](../../tests/test_api.py#L593) | 593 | `""` | — |
| [SRC-3451CC474D-L000594](../../tests/test_api.py#L594) | 594 | `"        response = bytearray()"` | — |
| [SRC-3451CC474D-L000595](../../tests/test_api.py#L595) | 595 | `"        while True:"` | — |
| [SRC-3451CC474D-L000596](../../tests/test_api.py#L596) | 596 | `"            try:"` | — |
| [SRC-3451CC474D-L000597](../../tests/test_api.py#L597) | 597 | `"                chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000598](../../tests/test_api.py#L598) | 598 | `"            except TimeoutError:"` | — |
| [SRC-3451CC474D-L000599](../../tests/test_api.py#L599) | 599 | `"                break"` | — |
| [SRC-3451CC474D-L000600](../../tests/test_api.py#L600) | 600 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000601](../../tests/test_api.py#L601) | 601 | `"                break"` | — |
| [SRC-3451CC474D-L000602](../../tests/test_api.py#L602) | 602 | `"            response.extend(chunk)"` | — |
| [SRC-3451CC474D-L000603](../../tests/test_api.py#L603) | 603 | `""` | — |
| [SRC-3451CC474D-L000604](../../tests/test_api.py#L604) | 604 | `"    elapsed = time.monotonic() - started"` | — |
| [SRC-3451CC474D-L000605](../../tests/test_api.py#L605) | 605 | `"    assert response.startswith(b\"HTTP/1.0 408\")"` | — |
| [SRC-3451CC474D-L000606](../../tests/test_api.py#L606) | 606 | `"    assert b\"request body read timed out\" in response"` | — |
| [SRC-3451CC474D-L000607](../../tests/test_api.py#L607) | 607 | `"    assert elapsed < 1.5"` | — |
| [SRC-3451CC474D-L000608](../../tests/test_api.py#L608) | 608 | `""` | — |
| [SRC-3451CC474D-L000609](../../tests/test_api.py#L609) | 609 | `""` | — |
| [SRC-3451CC474D-L000610](../../tests/test_api.py#L610) | 610 | `""` | — |
| [SRC-3451CC474D-L000611](../../tests/test_api.py#L611) | 611 | `"def test_api_absolute_header_deadline_stops_slow_trickle(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000612](../../tests/test_api.py#L612) | 612 | `"    \"\"\"Header bytes arriving before idle timeout must not extend the total deadline.\"\"\""` | — |
| [SRC-3451CC474D-L000613](../../tests/test_api.py#L613) | 613 | `"    import time"` | — |
| [SRC-3451CC474D-L000614](../../tests/test_api.py#L614) | 614 | `""` | — |
| [SRC-3451CC474D-L000615](../../tests/test_api.py#L615) | 615 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000616](../../tests/test_api.py#L616) | 616 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000617](../../tests/test_api.py#L617) | 617 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_HEADER_READ_TIMEOUT_SECONDS\", 0.5)"` | — |
| [SRC-3451CC474D-L000618](../../tests/test_api.py#L618) | 618 | `"    monkeypatch.setattr(\"api.omarai.REQUEST_HEADER_IDLE_TIMEOUT_SECONDS\", 0.35)"` | — |
| [SRC-3451CC474D-L000619](../../tests/test_api.py#L619) | 619 | `"    host, port = local_api.removeprefix(\"http://\").rsplit(\":\", 1)"` | — |
| [SRC-3451CC474D-L000620](../../tests/test_api.py#L620) | 620 | `""` | — |
| [SRC-3451CC474D-L000621](../../tests/test_api.py#L621) | 621 | `"    with socket.create_connection((host, int(port)), timeout=2) as client:"` | — |
| [SRC-3451CC474D-L000622](../../tests/test_api.py#L622) | 622 | `"        client.settimeout(1.2)"` | — |
| [SRC-3451CC474D-L000623](../../tests/test_api.py#L623) | 623 | `"        started = time.monotonic()"` | — |
| [SRC-3451CC474D-L000624](../../tests/test_api.py#L624) | 624 | `"        client.sendall("` | — |
| [SRC-3451CC474D-L000625](../../tests/test_api.py#L625) | 625 | `"            b\"POST /api/analyze HTTP/1.1\\r\\n\""` | — |
| [SRC-3451CC474D-L000626](../../tests/test_api.py#L626) | 626 | `"            b\"Host: localhost\\r\\n\""` | — |
| [SRC-3451CC474D-L000627](../../tests/test_api.py#L627) | 627 | `"            b\"Content-Type: application/json\\r\\n\""` | — |
| [SRC-3451CC474D-L000628](../../tests/test_api.py#L628) | 628 | `"            b\"Content-Length: 40\\r\\n\""` | — |
| [SRC-3451CC474D-L000629](../../tests/test_api.py#L629) | 629 | `"            b\"X-Slow: \""` | — |
| [SRC-3451CC474D-L000630](../../tests/test_api.py#L630) | 630 | `"        )"` | — |
| [SRC-3451CC474D-L000631](../../tests/test_api.py#L631) | 631 | `"        # Each tiny fragment is sent well before the 0.35s idle timeout. No"` | — |
| [SRC-3451CC474D-L000632](../../tests/test_api.py#L632) | 632 | `"        # newline completes X-Slow, so only an absolute header deadline can stop it."` | — |
| [SRC-3451CC474D-L000633](../../tests/test_api.py#L633) | 633 | `"        for fragment in (b\"a\", b\"b\", b\"c\", b\"d\", b\"e\", b\"f\", b\"g\", b\"h\", b\"i\"):"` | — |
| [SRC-3451CC474D-L000634](../../tests/test_api.py#L634) | 634 | `"            time.sleep(0.12)"` | — |
| [SRC-3451CC474D-L000635](../../tests/test_api.py#L635) | 635 | `"            try:"` | — |
| [SRC-3451CC474D-L000636](../../tests/test_api.py#L636) | 636 | `"                client.sendall(fragment)"` | — |
| [SRC-3451CC474D-L000637](../../tests/test_api.py#L637) | 637 | `"            except OSError:"` | — |
| [SRC-3451CC474D-L000638](../../tests/test_api.py#L638) | 638 | `"                break"` | — |
| [SRC-3451CC474D-L000639](../../tests/test_api.py#L639) | 639 | `""` | — |
| [SRC-3451CC474D-L000640](../../tests/test_api.py#L640) | 640 | `"        response = bytearray()"` | — |
| [SRC-3451CC474D-L000641](../../tests/test_api.py#L641) | 641 | `"        while True:"` | — |
| [SRC-3451CC474D-L000642](../../tests/test_api.py#L642) | 642 | `"            try:"` | — |
| [SRC-3451CC474D-L000643](../../tests/test_api.py#L643) | 643 | `"                chunk = client.recv(4096)"` | — |
| [SRC-3451CC474D-L000644](../../tests/test_api.py#L644) | 644 | `"            except TimeoutError:"` | — |
| [SRC-3451CC474D-L000645](../../tests/test_api.py#L645) | 645 | `"                break"` | — |
| [SRC-3451CC474D-L000646](../../tests/test_api.py#L646) | 646 | `"            except OSError:"` | — |
| [SRC-3451CC474D-L000647](../../tests/test_api.py#L647) | 647 | `"                break"` | — |
| [SRC-3451CC474D-L000648](../../tests/test_api.py#L648) | 648 | `"            if not chunk:"` | — |
| [SRC-3451CC474D-L000649](../../tests/test_api.py#L649) | 649 | `"                break"` | — |
| [SRC-3451CC474D-L000650](../../tests/test_api.py#L650) | 650 | `"            response.extend(chunk)"` | — |
| [SRC-3451CC474D-L000651](../../tests/test_api.py#L651) | 651 | `"        elapsed = time.monotonic() - started"` | — |
| [SRC-3451CC474D-L000652](../../tests/test_api.py#L652) | 652 | `""` | — |
| [SRC-3451CC474D-L000653](../../tests/test_api.py#L653) | 653 | `"    assert elapsed < 0.8"` | — |
| [SRC-3451CC474D-L000654](../../tests/test_api.py#L654) | 654 | `"    # The timed-out request never reached application dispatch; the handler closes silently."` | — |
| [SRC-3451CC474D-L000655](../../tests/test_api.py#L655) | 655 | `"    assert response == b\"\""` | — |
| [SRC-3451CC474D-L000656](../../tests/test_api.py#L656) | 656 | `""` | — |
| [SRC-3451CC474D-L000657](../../tests/test_api.py#L657) | 657 | `"def test_public_preflight_does_not_trust_spoofed_forwarded_host(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000658](../../tests/test_api.py#L658) | 658 | `"    \"\"\"A client-controlled X-Forwarded-Host must not grant an origin CORS access.\"\"\""` | — |
| [SRC-3451CC474D-L000659](../../tests/test_api.py#L659) | 659 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000660](../../tests/test_api.py#L660) | 660 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000661](../../tests/test_api.py#L661) | 661 | `""` | — |
| [SRC-3451CC474D-L000662](../../tests/test_api.py#L662) | 662 | `"    request = Request("` | — |
| [SRC-3451CC474D-L000663](../../tests/test_api.py#L663) | 663 | `"        local_api + \"/api/agent\","` | — |
| [SRC-3451CC474D-L000664](../../tests/test_api.py#L664) | 664 | `"        method=\"OPTIONS\","` | — |
| [SRC-3451CC474D-L000665](../../tests/test_api.py#L665) | 665 | `"        headers={"` | — |
| [SRC-3451CC474D-L000666](../../tests/test_api.py#L666) | 666 | `"            \"Origin\": \"https://attacker.example\","` | — |
| [SRC-3451CC474D-L000667](../../tests/test_api.py#L667) | 667 | `"            \"X-Forwarded-Host\": \"attacker.example\","` | — |
| [SRC-3451CC474D-L000668](../../tests/test_api.py#L668) | 668 | `"            \"X-Forwarded-Proto\": \"https\","` | — |
| [SRC-3451CC474D-L000669](../../tests/test_api.py#L669) | 669 | `"            \"Access-Control-Request-Method\": \"POST\","` | — |
| [SRC-3451CC474D-L000670](../../tests/test_api.py#L670) | 670 | `"            \"Access-Control-Request-Headers\": \"authorization,content-type\","` | — |
| [SRC-3451CC474D-L000671](../../tests/test_api.py#L671) | 671 | `"        },"` | — |
| [SRC-3451CC474D-L000672](../../tests/test_api.py#L672) | 672 | `"    )"` | — |
| [SRC-3451CC474D-L000673](../../tests/test_api.py#L673) | 673 | `"    with pytest.raises(HTTPError) as error:"` | — |
| [SRC-3451CC474D-L000674](../../tests/test_api.py#L674) | 674 | `"        urlopen(request, timeout=3)"` | — |
| [SRC-3451CC474D-L000675](../../tests/test_api.py#L675) | 675 | `"    assert error.value.code == 403"` | — |
| [SRC-3451CC474D-L000676](../../tests/test_api.py#L676) | 676 | `""` | — |
| [SRC-3451CC474D-L000677](../../tests/test_api.py#L677) | 677 | `""` | — |
| [SRC-3451CC474D-L000678](../../tests/test_api.py#L678) | 678 | `"def test_public_origin_still_allows_the_requested_host(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000679](../../tests/test_api.py#L679) | 679 | `"    \"\"\"Same-service public UI remains compatible when the request Host is trusted.\"\"\""` | — |
| [SRC-3451CC474D-L000680](../../tests/test_api.py#L680) | 680 | `"    from types import SimpleNamespace"` | — |
| [SRC-3451CC474D-L000681](../../tests/test_api.py#L681) | 681 | `""` | — |
| [SRC-3451CC474D-L000682](../../tests/test_api.py#L682) | 682 | `"    from api.omarai import Handler"` | — |
| [SRC-3451CC474D-L000683](../../tests/test_api.py#L683) | 683 | `""` | — |
| [SRC-3451CC474D-L000684](../../tests/test_api.py#L684) | 684 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-3451CC474D-L000685](../../tests/test_api.py#L685) | 685 | `"    monkeypatch.delenv(\"OMARAI_ALLOWED_ORIGINS\", raising=False)"` | — |
| [SRC-3451CC474D-L000686](../../tests/test_api.py#L686) | 686 | `"    handler = SimpleNamespace("` | — |
| [SRC-3451CC474D-L000687](../../tests/test_api.py#L687) | 687 | `"        headers={"` | — |
| [SRC-3451CC474D-L000688](../../tests/test_api.py#L688) | 688 | `"            \"Host\": \"omarai.example\","` | — |
| [SRC-3451CC474D-L000689](../../tests/test_api.py#L689) | 689 | `"            \"X-Forwarded-Proto\": \"https\","` | — |
| [SRC-3451CC474D-L000690](../../tests/test_api.py#L690) | 690 | `"            \"X-Forwarded-Host\": \"attacker.example\","` | — |
| [SRC-3451CC474D-L000691](../../tests/test_api.py#L691) | 691 | `"        }"` | — |
| [SRC-3451CC474D-L000692](../../tests/test_api.py#L692) | 692 | `"    )"` | — |
| [SRC-3451CC474D-L000693](../../tests/test_api.py#L693) | 693 | `"    allowed = Handler._allowed_origins(handler)"` | — |
| [SRC-3451CC474D-L000694](../../tests/test_api.py#L694) | 694 | `"    assert \"https://omarai.example\" in allowed"` | — |
| [SRC-3451CC474D-L000695](../../tests/test_api.py#L695) | 695 | `"    assert \"https://attacker.example\" not in allowed"` | — |
| [SRC-3451CC474D-L000696](../../tests/test_api.py#L696) | 696 | `""` | — |
| [SRC-3451CC474D-L000697](../../tests/test_api.py#L697) | 697 | `""` | — |
| [SRC-3451CC474D-L000698](../../tests/test_api.py#L698) | 698 | `""` | — |
| [SRC-3451CC474D-L000699](../../tests/test_api.py#L699) | 699 | `"def test_security_headers_apply_to_json_and_html_responses(local_api, monkeypatch):"` | — |
| [SRC-3451CC474D-L000700](../../tests/test_api.py#L700) | 700 | `"    monkeypatch.delenv(\"OMARAI_PUBLIC_DEPLOYMENT\", raising=False)"` | — |
| [SRC-3451CC474D-L000701](../../tests/test_api.py#L701) | 701 | `"    monkeypatch.delenv(\"OMARAI_ACCESS_TOKEN\", raising=False)"` | — |
| [SRC-3451CC474D-L000702](../../tests/test_api.py#L702) | 702 | `"    for path in (\"/api/health\", \"/\"):"` | — |
| [SRC-3451CC474D-L000703](../../tests/test_api.py#L703) | 703 | `"        request = Request(local_api + path)"` | — |
| [SRC-3451CC474D-L000704](../../tests/test_api.py#L704) | 704 | `"        with urlopen(request, timeout=3) as response:"` | — |
| [SRC-3451CC474D-L000705](../../tests/test_api.py#L705) | 705 | `"            headers = {name.lower(): value for name, value in response.headers.items()}"` | — |
| [SRC-3451CC474D-L000706](../../tests/test_api.py#L706) | 706 | `"            assert headers[\"x-content-type-options\"] == \"nosniff\""` | — |
| [SRC-3451CC474D-L000707](../../tests/test_api.py#L707) | 707 | `"            assert headers[\"x-frame-options\"] == \"DENY\""` | — |
| [SRC-3451CC474D-L000708](../../tests/test_api.py#L708) | 708 | `"            assert headers[\"referrer-policy\"] == \"strict-origin-when-cross-origin\""` | — |
| [SRC-3451CC474D-L000709](../../tests/test_api.py#L709) | 709 | `"            assert \"default-src 'self'\" in headers[\"content-security-policy\"]"` | — |
| [SRC-3451CC474D-L000710](../../tests/test_api.py#L710) | 710 | `"            assert \"frame-ancestors 'none'\" in headers[\"content-security-policy\"]"` | — |
| [SRC-3451CC474D-L000711](../../tests/test_api.py#L711) | 711 | `"            assert headers[\"permissions-policy\"] == ("` | — |
| [SRC-3451CC474D-L000712](../../tests/test_api.py#L712) | 712 | `"                \"camera=(), microphone=(), geolocation=()\""` | — |
| [SRC-3451CC474D-L000713](../../tests/test_api.py#L713) | 713 | `"            )"` | — |
| [SRC-3451CC474D-L000714](../../tests/test_api.py#L714) | 714 | `""` | — |
| [SRC-3451CC474D-L000715](../../tests/test_api.py#L715) | 715 | `""` | — |
| [SRC-3451CC474D-L000716](../../tests/test_api.py#L716) | 716 | `"def test_health_exposes_only_validated_image_baked_sha(monkeypatch, tmp_path):"` | — |
| [SRC-3451CC474D-L000717](../../tests/test_api.py#L717) | 717 | `"    import api.omarai as api_module"` | — |
| [SRC-3451CC474D-L000718](../../tests/test_api.py#L718) | 718 | `""` | — |
| [SRC-3451CC474D-L000719](../../tests/test_api.py#L719) | 719 | `"    build_sha_file = tmp_path / \"BUILD_SHA\""` | — |
| [SRC-3451CC474D-L000720](../../tests/test_api.py#L720) | 720 | `"    monkeypatch.setattr(api_module, \"BUILD_SHA_FILE\", build_sha_file)"` | — |
| [SRC-3451CC474D-L000721](../../tests/test_api.py#L721) | 721 | `"    assert api_module._build_sha() == \"unknown\""` | — |
| [SRC-3451CC474D-L000722](../../tests/test_api.py#L722) | 722 | `"    build_sha_file.write_text(\"a\" * 40, encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000723](../../tests/test_api.py#L723) | 723 | `"    assert api_module._build_sha() == \"a\" * 40"` | — |
| [SRC-3451CC474D-L000724](../../tests/test_api.py#L724) | 724 | `"    build_sha_file.write_text(\"not-a-git-sha\", encoding=\"ascii\")"` | — |
| [SRC-3451CC474D-L000725](../../tests/test_api.py#L725) | 725 | `"    assert api_module._build_sha() == \"unknown\""` | — |
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
