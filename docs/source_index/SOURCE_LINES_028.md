# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **028**
- سجلات الأسطر: **800**
- النطاق: SRC-62DC597310-L000015 إلى SRC-2614DCB6FB-L000077
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-62DC597310 — [tests/test_live_search_connectors.py](../../tests/test_live_search_connectors.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-62DC597310-L000015](../../tests/test_live_search_connectors.py#L15) | 15 | `""` | — |
| [SRC-62DC597310-L000016](../../tests/test_live_search_connectors.py#L16) | 16 | `"    def json(self):"` | — |
| [SRC-62DC597310-L000017](../../tests/test_live_search_connectors.py#L17) | 17 | `"        return self.payload"` | — |
| [SRC-62DC597310-L000018](../../tests/test_live_search_connectors.py#L18) | 18 | `""` | — |
| [SRC-62DC597310-L000019](../../tests/test_live_search_connectors.py#L19) | 19 | `""` | — |
| [SRC-62DC597310-L000020](../../tests/test_live_search_connectors.py#L20) | 20 | `"def test_brave_search_adapter_normalizes_real_api_response(monkeypatch):"` | — |
| [SRC-62DC597310-L000021](../../tests/test_live_search_connectors.py#L21) | 21 | `"    monkeypatch.setenv(\"BRAVE_SEARCH_API_KEY\", \"unit-test-secret\")"` | — |
| [SRC-62DC597310-L000022](../../tests/test_live_search_connectors.py#L22) | 22 | `"    requested = {}"` | — |
| [SRC-62DC597310-L000023](../../tests/test_live_search_connectors.py#L23) | 23 | `""` | — |
| [SRC-62DC597310-L000024](../../tests/test_live_search_connectors.py#L24) | 24 | `"    def fake_get(url, **kwargs):"` | — |
| [SRC-62DC597310-L000025](../../tests/test_live_search_connectors.py#L25) | 25 | `"        requested[\"url\"] = url"` | — |
| [SRC-62DC597310-L000026](../../tests/test_live_search_connectors.py#L26) | 26 | `"        requested.update(kwargs)"` | — |
| [SRC-62DC597310-L000027](../../tests/test_live_search_connectors.py#L27) | 27 | `"        return FakeResponse({"` | — |
| [SRC-62DC597310-L000028](../../tests/test_live_search_connectors.py#L28) | 28 | `"            \"web\": {"` | — |
| [SRC-62DC597310-L000029](../../tests/test_live_search_connectors.py#L29) | 29 | `"                \"results\": [{"` | — |
| [SRC-62DC597310-L000030](../../tests/test_live_search_connectors.py#L30) | 30 | `"                    \"title\": \"Current research\","` | — |
| [SRC-62DC597310-L000031](../../tests/test_live_search_connectors.py#L31) | 31 | `"                    \"url\": \"https://example.org/research\","` | — |
| [SRC-62DC597310-L000032](../../tests/test_live_search_connectors.py#L32) | 32 | `"                    \"description\": \"A substantive search result.\","` | — |
| [SRC-62DC597310-L000033](../../tests/test_live_search_connectors.py#L33) | 33 | `"                    \"page_age\": \"October 10, 2026\","` | — |
| [SRC-62DC597310-L000034](../../tests/test_live_search_connectors.py#L34) | 34 | `"                }]"` | — |
| [SRC-62DC597310-L000035](../../tests/test_live_search_connectors.py#L35) | 35 | `"            }"` | — |
| [SRC-62DC597310-L000036](../../tests/test_live_search_connectors.py#L36) | 36 | `"        })"` | — |
| [SRC-62DC597310-L000037](../../tests/test_live_search_connectors.py#L37) | 37 | `""` | — |
| [SRC-62DC597310-L000038](../../tests/test_live_search_connectors.py#L38) | 38 | `"    monkeypatch.setattr(httpx, \"get\", fake_get)"` | — |
| [SRC-62DC597310-L000039](../../tests/test_live_search_connectors.py#L39) | 39 | `"    rows = WebAgent()._search_brave(\"بحث حديث\")"` | — |
| [SRC-62DC597310-L000040](../../tests/test_live_search_connectors.py#L40) | 40 | `"    assert requested[\"url\"] == \"https://api.search.brave.com/res/v1/web/search\""` | — |
| [SRC-62DC597310-L000041](../../tests/test_live_search_connectors.py#L41) | 41 | `"    assert requested[\"headers\"][\"X-Subscription-Token\"] == \"unit-test-secret\""` | — |
| [SRC-62DC597310-L000042](../../tests/test_live_search_connectors.py#L42) | 42 | `"    assert requested[\"params\"][\"country\"] == \"EG\""` | — |
| [SRC-62DC597310-L000043](../../tests/test_live_search_connectors.py#L43) | 43 | `"    assert rows[0][\"provider\"] == \"brave_search_api\""` | — |
| [SRC-62DC597310-L000044](../../tests/test_live_search_connectors.py#L44) | 44 | `"    assert rows[0][\"published_at\"] == \"October 10, 2026\""` | — |
| [SRC-62DC597310-L000045](../../tests/test_live_search_connectors.py#L45) | 45 | `"    assert \"unit-test-secret\" not in str(rows)"` | — |
| [SRC-62DC597310-L000046](../../tests/test_live_search_connectors.py#L46) | 46 | `""` | — |
| [SRC-62DC597310-L000047](../../tests/test_live_search_connectors.py#L47) | 47 | `""` | — |
| [SRC-62DC597310-L000048](../../tests/test_live_search_connectors.py#L48) | 48 | `"def test_tavily_search_adapter_normalizes_live_search_results(monkeypatch):"` | — |
| [SRC-62DC597310-L000049](../../tests/test_live_search_connectors.py#L49) | 49 | `"    monkeypatch.setenv(\"TAVILY_API_KEY\", \"unit-test-tavily-secret\")"` | — |
| [SRC-62DC597310-L000050](../../tests/test_live_search_connectors.py#L50) | 50 | `"    requested = {}"` | — |
| [SRC-62DC597310-L000051](../../tests/test_live_search_connectors.py#L51) | 51 | `""` | — |
| [SRC-62DC597310-L000052](../../tests/test_live_search_connectors.py#L52) | 52 | `"    def fake_post(url, **kwargs):"` | — |
| [SRC-62DC597310-L000053](../../tests/test_live_search_connectors.py#L53) | 53 | `"        requested[\"url\"] = url"` | — |
| [SRC-62DC597310-L000054](../../tests/test_live_search_connectors.py#L54) | 54 | `"        requested.update(kwargs)"` | — |
| [SRC-62DC597310-L000055](../../tests/test_live_search_connectors.py#L55) | 55 | `"        return FakeResponse({"` | — |
| [SRC-62DC597310-L000056](../../tests/test_live_search_connectors.py#L56) | 56 | `"            \"results\": [{"` | — |
| [SRC-62DC597310-L000057](../../tests/test_live_search_connectors.py#L57) | 57 | `"                \"title\": \"Official report\","` | — |
| [SRC-62DC597310-L000058](../../tests/test_live_search_connectors.py#L58) | 58 | `"                \"url\": \"https://example.org/report\","` | — |
| [SRC-62DC597310-L000059](../../tests/test_live_search_connectors.py#L59) | 59 | `"                \"content\": \"A source excerpt from the search response.\","` | — |
| [SRC-62DC597310-L000060](../../tests/test_live_search_connectors.py#L60) | 60 | `"                \"published_date\": \"2026-10-11\","` | — |
| [SRC-62DC597310-L000061](../../tests/test_live_search_connectors.py#L61) | 61 | `"            }]"` | — |
| [SRC-62DC597310-L000062](../../tests/test_live_search_connectors.py#L62) | 62 | `"        })"` | — |
| [SRC-62DC597310-L000063](../../tests/test_live_search_connectors.py#L63) | 63 | `""` | — |
| [SRC-62DC597310-L000064](../../tests/test_live_search_connectors.py#L64) | 64 | `"    monkeypatch.setattr(httpx, \"post\", fake_post)"` | — |
| [SRC-62DC597310-L000065](../../tests/test_live_search_connectors.py#L65) | 65 | `"    rows = WebAgent()._search_tavily(\"official sources report\")"` | — |
| [SRC-62DC597310-L000066](../../tests/test_live_search_connectors.py#L66) | 66 | `"    assert requested[\"url\"] == \"https://api.tavily.com/search\""` | — |
| [SRC-62DC597310-L000067](../../tests/test_live_search_connectors.py#L67) | 67 | `"    assert requested[\"json\"][\"api_key\"] == \"unit-test-tavily-secret\""` | — |
| [SRC-62DC597310-L000068](../../tests/test_live_search_connectors.py#L68) | 68 | `"    assert requested[\"json\"][\"include_answer\"] is False"` | — |
| [SRC-62DC597310-L000069](../../tests/test_live_search_connectors.py#L69) | 69 | `"    assert rows[0][\"provider\"] == \"tavily_search_api\""` | — |
| [SRC-62DC597310-L000070](../../tests/test_live_search_connectors.py#L70) | 70 | `"    assert rows[0][\"snippet\"].startswith(\"A source excerpt\")"` | — |
| [SRC-62DC597310-L000071](../../tests/test_live_search_connectors.py#L71) | 71 | `"    assert \"unit-test-tavily-secret\" not in str(rows)"` | — |
| [SRC-62DC597310-L000072](../../tests/test_live_search_connectors.py#L72) | 72 | `""` | — |
| [SRC-62DC597310-L000073](../../tests/test_live_search_connectors.py#L73) | 73 | `""` | — |
| [SRC-62DC597310-L000074](../../tests/test_live_search_connectors.py#L74) | 74 | `"def test_search_api_setup_status_reports_only_presence_not_secret_values(monkeypatch):"` | — |
| [SRC-62DC597310-L000075](../../tests/test_live_search_connectors.py#L75) | 75 | `"    monkeypatch.setenv(\"BRAVE_SEARCH_API_KEY\", \"brave-secret\")"` | — |
| [SRC-62DC597310-L000076](../../tests/test_live_search_connectors.py#L76) | 76 | `"    monkeypatch.setenv(\"TAVILY_API_KEY\", \"tavily-secret\")"` | — |
| [SRC-62DC597310-L000077](../../tests/test_live_search_connectors.py#L77) | 77 | `"    status = WebAgent.status()"` | — |
| [SRC-62DC597310-L000078](../../tests/test_live_search_connectors.py#L78) | 78 | `"    assert status[\"brave_search_api_configured\"] is True"` | — |
| [SRC-62DC597310-L000079](../../tests/test_live_search_connectors.py#L79) | 79 | `"    assert status[\"tavily_search_api_configured\"] is True"` | — |
| [SRC-62DC597310-L000080](../../tests/test_live_search_connectors.py#L80) | 80 | `"    assert \"brave-secret\" not in str(status)"` | — |
| [SRC-62DC597310-L000081](../../tests/test_live_search_connectors.py#L81) | 81 | `"    assert \"tavily-secret\" not in str(status)"` | — |
## اختبارات

### FILE-44CDA52D01 — [tests/test_omarai.py](../../tests/test_omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-44CDA52D01-L000001](../../tests/test_omarai.py#L1) | 1 | `"import csv"` | — |
| [SRC-44CDA52D01-L000002](../../tests/test_omarai.py#L2) | 2 | `""` | — |
| [SRC-44CDA52D01-L000003](../../tests/test_omarai.py#L3) | 3 | `"import pytest"` | — |
| [SRC-44CDA52D01-L000004](../../tests/test_omarai.py#L4) | 4 | `""` | — |
| [SRC-44CDA52D01-L000005](../../tests/test_omarai.py#L5) | 5 | `"from agents.omarai import LeadStore, analyze, normalize"` | — |
| [SRC-44CDA52D01-L000006](../../tests/test_omarai.py#L6) | 6 | `""` | — |
| [SRC-44CDA52D01-L000007](../../tests/test_omarai.py#L7) | 7 | `""` | — |
| [SRC-44CDA52D01-L000008](../../tests/test_omarai.py#L8) | 8 | `"def test_arabic_normalization():"` | — |
| [SRC-44CDA52D01-L000009](../../tests/test_omarai.py#L9) | 9 | `"    assert normalize(\"إيجارٌ ـ شقة\") == normalize(\"ايجار شقة\")"` | — |
| [SRC-44CDA52D01-L000010](../../tests/test_omarai.py#L10) | 10 | `""` | — |
| [SRC-44CDA52D01-L000011](../../tests/test_omarai.py#L11) | 11 | `"def test_high_intent_with_next_step():"` | — |
| [SRC-44CDA52D01-L000012](../../tests/test_omarai.py#L12) | 12 | `"    result=analyze(\"بدور على شقة وممكن معاينة\")"` | — |
| [SRC-44CDA52D01-L000013](../../tests/test_omarai.py#L13) | 13 | `"    assert result[\"label\"]==\"high_intent\""` | — |
| [SRC-44CDA52D01-L000014](../../tests/test_omarai.py#L14) | 14 | `"    assert result[\"score\"]>=55"` | — |
| [SRC-44CDA52D01-L000015](../../tests/test_omarai.py#L15) | 15 | `""` | — |
| [SRC-44CDA52D01-L000016](../../tests/test_omarai.py#L16) | 16 | `"def test_non_buyer_override():"` | — |
| [SRC-44CDA52D01-L000017](../../tests/test_omarai.py#L17) | 17 | `"    result=analyze(\"مش عايز اشتري، عايز ابيع شقة\")"` | — |
| [SRC-44CDA52D01-L000018](../../tests/test_omarai.py#L18) | 18 | `"    assert result[\"label\"]==\"not_buyer_signal\""` | — |
| [SRC-44CDA52D01-L000019](../../tests/test_omarai.py#L19) | 19 | `"    assert result[\"score\"]==0"` | — |
| [SRC-44CDA52D01-L000020](../../tests/test_omarai.py#L20) | 20 | `""` | — |
| [SRC-44CDA52D01-L000021](../../tests/test_omarai.py#L21) | 21 | `"def test_empty_text_rejected():"` | — |
| [SRC-44CDA52D01-L000022](../../tests/test_omarai.py#L22) | 22 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000023](../../tests/test_omarai.py#L23) | 23 | `"        analyze(\" \")"` | — |
| [SRC-44CDA52D01-L000024](../../tests/test_omarai.py#L24) | 24 | `""` | — |
| [SRC-44CDA52D01-L000025](../../tests/test_omarai.py#L25) | 25 | `"def test_url_required_and_validated(tmp_path):"` | — |
| [SRC-44CDA52D01-L000026](../../tests/test_omarai.py#L26) | 26 | `"    store=LeadStore(tmp_path/\"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000027](../../tests/test_omarai.py#L27) | 27 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000028](../../tests/test_omarai.py#L28) | 28 | `"        store.add(\"بدور على شقة\",\"\",\"manual\")"` | — |
| [SRC-44CDA52D01-L000029](../../tests/test_omarai.py#L29) | 29 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000030](../../tests/test_omarai.py#L30) | 30 | `"        store.add(\"بدور على شقة\",\"file:///tmp/private\",\"manual\")"` | — |
| [SRC-44CDA52D01-L000031](../../tests/test_omarai.py#L31) | 31 | `""` | — |
| [SRC-44CDA52D01-L000032](../../tests/test_omarai.py#L32) | 32 | `"def test_duplicate_is_idempotent(tmp_path):"` | — |
| [SRC-44CDA52D01-L000033](../../tests/test_omarai.py#L33) | 33 | `"    store=LeadStore(tmp_path/\"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000034](../../tests/test_omarai.py#L34) | 34 | `"    one,created1=store.add(\"بدور على شقة\",\"https://example.com/post/1\",\"facebook\")"` | — |
| [SRC-44CDA52D01-L000035](../../tests/test_omarai.py#L35) | 35 | `"    two,created2=store.add(\"بدور على شقة\",\"https://example.com/post/1\",\"facebook\")"` | — |
| [SRC-44CDA52D01-L000036](../../tests/test_omarai.py#L36) | 36 | `"    assert created1 is True and created2 is False"` | — |
| [SRC-44CDA52D01-L000037](../../tests/test_omarai.py#L37) | 37 | `"    assert one[\"id\"]==two[\"id\"]"` | — |
| [SRC-44CDA52D01-L000038](../../tests/test_omarai.py#L38) | 38 | `"    assert len(store.list())==1"` | — |
| [SRC-44CDA52D01-L000039](../../tests/test_omarai.py#L39) | 39 | `""` | — |
| [SRC-44CDA52D01-L000040](../../tests/test_omarai.py#L40) | 40 | `"def test_status_updates_are_explicit(tmp_path):"` | — |
| [SRC-44CDA52D01-L000041](../../tests/test_omarai.py#L41) | 41 | `"    store=LeadStore(tmp_path/\"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000042](../../tests/test_omarai.py#L42) | 42 | `"    lead,_=store.add(\"بدور على شقة\",\"https://example.com/p\",\"manual\")"` | — |
| [SRC-44CDA52D01-L000043](../../tests/test_omarai.py#L43) | 43 | `"    updated=store.update_status(lead[\"id\"],\"qualified\")"` | — |
| [SRC-44CDA52D01-L000044](../../tests/test_omarai.py#L44) | 44 | `"    assert updated[\"status\"]==\"qualified\""` | — |
| [SRC-44CDA52D01-L000045](../../tests/test_omarai.py#L45) | 45 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000046](../../tests/test_omarai.py#L46) | 46 | `"        store.update_status(lead[\"id\"],\"magic\")"` | — |
| [SRC-44CDA52D01-L000047](../../tests/test_omarai.py#L47) | 47 | `""` | — |
| [SRC-44CDA52D01-L000048](../../tests/test_omarai.py#L48) | 48 | `"def test_csv_requires_columns(tmp_path):"` | — |
| [SRC-44CDA52D01-L000049](../../tests/test_omarai.py#L49) | 49 | `"    bad=tmp_path/\"bad.csv\""` | — |
| [SRC-44CDA52D01-L000050](../../tests/test_omarai.py#L50) | 50 | `"    bad.write_text(\"foo,bar\\na,b\\n\",encoding=\"utf-8\")"` | — |
| [SRC-44CDA52D01-L000051](../../tests/test_omarai.py#L51) | 51 | `"    store=LeadStore(tmp_path/\"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000052](../../tests/test_omarai.py#L52) | 52 | `"    with pytest.raises(ValueError):"` | — |
| [SRC-44CDA52D01-L000053](../../tests/test_omarai.py#L53) | 53 | `"        store.import_csv(bad)"` | — |
| [SRC-44CDA52D01-L000054](../../tests/test_omarai.py#L54) | 54 | `""` | — |
| [SRC-44CDA52D01-L000055](../../tests/test_omarai.py#L55) | 55 | `"def test_csv_export_neutralizes_spreadsheet_formula_injection(tmp_path):"` | — |
| [SRC-44CDA52D01-L000056](../../tests/test_omarai.py#L56) | 56 | `"    store = LeadStore(tmp_path / \"db.sqlite3\")"` | — |
| [SRC-44CDA52D01-L000057](../../tests/test_omarai.py#L57) | 57 | `"    store.add("` | — |
| [SRC-44CDA52D01-L000058](../../tests/test_omarai.py#L58) | 58 | `"        '=HYPERLINK(\"https://evil.example\",\"click\")',"` | — |
| [SRC-44CDA52D01-L000059](../../tests/test_omarai.py#L59) | 59 | `"        \"https://example.com/post/1\","` | — |
| [SRC-44CDA52D01-L000060](../../tests/test_omarai.py#L60) | 60 | `"        platform=\"manual\","` | — |
| [SRC-44CDA52D01-L000061](../../tests/test_omarai.py#L61) | 61 | `"        note=\"  +SUM(1,1)\","` | — |
| [SRC-44CDA52D01-L000062](../../tests/test_omarai.py#L62) | 62 | `"    )"` | — |
| [SRC-44CDA52D01-L000063](../../tests/test_omarai.py#L63) | 63 | `"    store.add("` | — |
| [SRC-44CDA52D01-L000064](../../tests/test_omarai.py#L64) | 64 | `"        \"\\u00a0\\ufeff=1+1\","` | — |
| [SRC-44CDA52D01-L000065](../../tests/test_omarai.py#L65) | 65 | `"        \"https://example.com/post/2\","` | — |
| [SRC-44CDA52D01-L000066](../../tests/test_omarai.py#L66) | 66 | `"        platform=\"manual\","` | — |
| [SRC-44CDA52D01-L000067](../../tests/test_omarai.py#L67) | 67 | `"        note=\"\\u00a0\\ufeff=SUM(1,1)\","` | — |
| [SRC-44CDA52D01-L000068](../../tests/test_omarai.py#L68) | 68 | `"    )"` | — |
| [SRC-44CDA52D01-L000069](../../tests/test_omarai.py#L69) | 69 | `"    destination = tmp_path / \"export.csv\""` | — |
| [SRC-44CDA52D01-L000070](../../tests/test_omarai.py#L70) | 70 | `"    assert store.export_csv(destination) == 2"` | — |
| [SRC-44CDA52D01-L000071](../../tests/test_omarai.py#L71) | 71 | `"    raw_csv = destination.read_text(encoding=\"utf-8-sig\")"` | — |
| [SRC-44CDA52D01-L000072](../../tests/test_omarai.py#L72) | 72 | `"    assert '\"\\t=HYPERLINK(' in raw_csv"` | — |
| [SRC-44CDA52D01-L000073](../../tests/test_omarai.py#L73) | 73 | `"    assert '\"\\t  +SUM' in raw_csv"` | — |
| [SRC-44CDA52D01-L000074](../../tests/test_omarai.py#L74) | 74 | `""` | — |
| [SRC-44CDA52D01-L000075](../../tests/test_omarai.py#L75) | 75 | `"    with destination.open(newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-44CDA52D01-L000076](../../tests/test_omarai.py#L76) | 76 | `"        rows = list(csv.DictReader(stream))"` | — |
| [SRC-44CDA52D01-L000077](../../tests/test_omarai.py#L77) | 77 | `""` | — |
| [SRC-44CDA52D01-L000078](../../tests/test_omarai.py#L78) | 78 | `"    row1 = next(row for row in rows if row[\"source_url\"] == \"https://example.com/post/1\")"` | — |
| [SRC-44CDA52D01-L000079](../../tests/test_omarai.py#L79) | 79 | `"    row2 = next(row for row in rows if row[\"source_url\"] == \"https://example.com/post/2\")"` | — |
| [SRC-44CDA52D01-L000080](../../tests/test_omarai.py#L80) | 80 | `"    assert row1[\"text\"].startswith(\"\\t=\")"` | — |
| [SRC-44CDA52D01-L000081](../../tests/test_omarai.py#L81) | 81 | `"    assert row1[\"note\"].startswith(\"\\t  +\")"` | — |
| [SRC-44CDA52D01-L000082](../../tests/test_omarai.py#L82) | 82 | `"    assert row2[\"text\"].startswith(\"\\t\\ufeff=\")"` | — |
| [SRC-44CDA52D01-L000083](../../tests/test_omarai.py#L83) | 83 | `"    assert row2[\"note\"].startswith(\"\\t\\u00a0\\ufeff=\")"` | — |
| [SRC-44CDA52D01-L000084](../../tests/test_omarai.py#L84) | 84 | `""` | — |
## اختبارات

### FILE-B106ADC5EF — [tests/test_proxy_origin.py](../../tests/test_proxy_origin.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-B106ADC5EF-L000001](../../tests/test_proxy_origin.py#L1) | 1 | `"\"\"\"Regression tests for the proxy-aware Origin check. OMARAI-PROXY-ORIGIN-PATCH\"\"\""` | — |
| [SRC-B106ADC5EF-L000002](../../tests/test_proxy_origin.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-B106ADC5EF-L000003](../../tests/test_proxy_origin.py#L3) | 3 | `"import http.client"` | — |
| [SRC-B106ADC5EF-L000004](../../tests/test_proxy_origin.py#L4) | 4 | `"import threading"` | — |
| [SRC-B106ADC5EF-L000005](../../tests/test_proxy_origin.py#L5) | 5 | `"from http.server import ThreadingHTTPServer"` | — |
| [SRC-B106ADC5EF-L000006](../../tests/test_proxy_origin.py#L6) | 6 | `"import pytest"` | — |
| [SRC-B106ADC5EF-L000007](../../tests/test_proxy_origin.py#L7) | 7 | `"from agents.omarai import LeadStore"` | — |
| [SRC-B106ADC5EF-L000008](../../tests/test_proxy_origin.py#L8) | 8 | `"from api.omarai import Handler"` | — |
| [SRC-B106ADC5EF-L000009](../../tests/test_proxy_origin.py#L9) | 9 | `""` | — |
| [SRC-B106ADC5EF-L000010](../../tests/test_proxy_origin.py#L10) | 10 | `"TOKEN = \"t\" * 40"` | — |
| [SRC-B106ADC5EF-L000011](../../tests/test_proxy_origin.py#L11) | 11 | `"PUBLIC_NAME = \"app-1234.hosting.example\""` | — |
| [SRC-B106ADC5EF-L000012](../../tests/test_proxy_origin.py#L12) | 12 | `""` | — |
| [SRC-B106ADC5EF-L000013](../../tests/test_proxy_origin.py#L13) | 13 | `"@pytest.fixture"` | — |
| [SRC-B106ADC5EF-L000014](../../tests/test_proxy_origin.py#L14) | 14 | `"def port(tmp_path, monkeypatch):"` | — |
| [SRC-B106ADC5EF-L000015](../../tests/test_proxy_origin.py#L15) | 15 | `"    monkeypatch.setenv(\"OMARAI_PUBLIC_DEPLOYMENT\", \"1\")"` | — |
| [SRC-B106ADC5EF-L000016](../../tests/test_proxy_origin.py#L16) | 16 | `"    monkeypatch.setenv(\"OMARAI_ACCESS_TOKEN\", TOKEN)"` | — |
| [SRC-B106ADC5EF-L000017](../../tests/test_proxy_origin.py#L17) | 17 | `"    # The public host is explicitly configured; do not infer it from a client header."` | — |
| [SRC-B106ADC5EF-L000018](../../tests/test_proxy_origin.py#L18) | 18 | `"    monkeypatch.setenv(\"OMARAI_ALLOWED_ORIGINS\", \"https://\" + PUBLIC_NAME)"` | — |
| [SRC-B106ADC5EF-L000019](../../tests/test_proxy_origin.py#L19) | 19 | `"    monkeypatch.setattr(Handler, \"store\", LeadStore(tmp_path / \"origin-test.sqlite3\"))"` | — |
| [SRC-B106ADC5EF-L000020](../../tests/test_proxy_origin.py#L20) | 20 | `"    monkeypatch.setattr(Handler, \"RATE_LIMIT_REQUESTS\", 10_000)"` | — |
| [SRC-B106ADC5EF-L000021](../../tests/test_proxy_origin.py#L21) | 21 | `"    server = ThreadingHTTPServer((\"127.0.0.1\", 0), Handler)"` | — |
| [SRC-B106ADC5EF-L000022](../../tests/test_proxy_origin.py#L22) | 22 | `"    thread = threading.Thread(target=server.serve_forever, daemon=True)"` | — |
| [SRC-B106ADC5EF-L000023](../../tests/test_proxy_origin.py#L23) | 23 | `"    thread.start()"` | — |
| [SRC-B106ADC5EF-L000024](../../tests/test_proxy_origin.py#L24) | 24 | `"    try:"` | — |
| [SRC-B106ADC5EF-L000025](../../tests/test_proxy_origin.py#L25) | 25 | `"        yield server.server_port"` | — |
| [SRC-B106ADC5EF-L000026](../../tests/test_proxy_origin.py#L26) | 26 | `"    finally:"` | — |
| [SRC-B106ADC5EF-L000027](../../tests/test_proxy_origin.py#L27) | 27 | `"        server.shutdown()"` | — |
| [SRC-B106ADC5EF-L000028](../../tests/test_proxy_origin.py#L28) | 28 | `"        server.server_close()"` | — |
| [SRC-B106ADC5EF-L000029](../../tests/test_proxy_origin.py#L29) | 29 | `"        thread.join(timeout=3)"` | — |
| [SRC-B106ADC5EF-L000030](../../tests/test_proxy_origin.py#L30) | 30 | `""` | — |
| [SRC-B106ADC5EF-L000031](../../tests/test_proxy_origin.py#L31) | 31 | `"def call(port, method, extra):"` | — |
| [SRC-B106ADC5EF-L000032](../../tests/test_proxy_origin.py#L32) | 32 | `"    body = b'{\"question\": \"x\"}' if method == \"POST\" else b\"\""` | — |
| [SRC-B106ADC5EF-L000033](../../tests/test_proxy_origin.py#L33) | 33 | `"    headers = {\"Content-Type\": \"application/json\", \"Authorization\": \"Bearer \" + TOKEN, **extra}"` | — |
| [SRC-B106ADC5EF-L000034](../../tests/test_proxy_origin.py#L34) | 34 | `"    connection = http.client.HTTPConnection(\"127.0.0.1\", port, timeout=5)"` | — |
| [SRC-B106ADC5EF-L000035](../../tests/test_proxy_origin.py#L35) | 35 | `"    connection.putrequest(method, \"/api/ask\", skip_host=True)"` | — |
| [SRC-B106ADC5EF-L000036](../../tests/test_proxy_origin.py#L36) | 36 | `"    for name, value in headers.items():"` | — |
| [SRC-B106ADC5EF-L000037](../../tests/test_proxy_origin.py#L37) | 37 | `"        connection.putheader(name, value)"` | — |
| [SRC-B106ADC5EF-L000038](../../tests/test_proxy_origin.py#L38) | 38 | `"    connection.putheader(\"Content-Length\", str(len(body)))"` | — |
| [SRC-B106ADC5EF-L000039](../../tests/test_proxy_origin.py#L39) | 39 | `"    connection.endheaders()"` | — |
| [SRC-B106ADC5EF-L000040](../../tests/test_proxy_origin.py#L40) | 40 | `"    if body:"` | — |
| [SRC-B106ADC5EF-L000041](../../tests/test_proxy_origin.py#L41) | 41 | `"        connection.send(body)"` | — |
| [SRC-B106ADC5EF-L000042](../../tests/test_proxy_origin.py#L42) | 42 | `"    response = connection.getresponse()"` | — |
| [SRC-B106ADC5EF-L000043](../../tests/test_proxy_origin.py#L43) | 43 | `"    response.read()"` | — |
| [SRC-B106ADC5EF-L000044](../../tests/test_proxy_origin.py#L44) | 44 | `"    connection.close()"` | — |
| [SRC-B106ADC5EF-L000045](../../tests/test_proxy_origin.py#L45) | 45 | `"    return response.status"` | — |
| [SRC-B106ADC5EF-L000046](../../tests/test_proxy_origin.py#L46) | 46 | `""` | — |
| [SRC-B106ADC5EF-L000047](../../tests/test_proxy_origin.py#L47) | 47 | `"ALLOWED_SHAPES = {"` | — |
| [SRC-B106ADC5EF-L000048](../../tests/test_proxy_origin.py#L48) | 48 | `"    \"proxy keeps Host, forwards https\": {\"Host\": PUBLIC_NAME, \"X-Forwarded-Proto\": \"https\"},"` | — |
| [SRC-B106ADC5EF-L000049](../../tests/test_proxy_origin.py#L49) | 49 | `"    \"proxy keeps Host, sends no proto header\": {\"Host\": PUBLIC_NAME},"` | — |
| [SRC-B106ADC5EF-L000050](../../tests/test_proxy_origin.py#L50) | 50 | `"    \"proxy forwards plain http\": {\"Host\": PUBLIC_NAME, \"X-Forwarded-Proto\": \"http\"},"` | — |
| [SRC-B106ADC5EF-L000051](../../tests/test_proxy_origin.py#L51) | 51 | `"    \"proxy rewrites Host, public name in X-Forwarded-Host\": {"` | — |
| [SRC-B106ADC5EF-L000052](../../tests/test_proxy_origin.py#L52) | 52 | `"        \"Host\": \"127.0.0.1:8000\", \"X-Forwarded-Host\": PUBLIC_NAME, \"X-Forwarded-Proto\": \"http\"},"` | — |
| [SRC-B106ADC5EF-L000053](../../tests/test_proxy_origin.py#L53) | 53 | `"}"` | — |
| [SRC-B106ADC5EF-L000054](../../tests/test_proxy_origin.py#L54) | 54 | `""` | — |
| [SRC-B106ADC5EF-L000055](../../tests/test_proxy_origin.py#L55) | 55 | `"@pytest.mark.parametrize(\"shape\", ALLOWED_SHAPES)"` | — |
| [SRC-B106ADC5EF-L000056](../../tests/test_proxy_origin.py#L56) | 56 | `"def test_own_origin_is_accepted_behind_a_proxy(port, shape):"` | — |
| [SRC-B106ADC5EF-L000057](../../tests/test_proxy_origin.py#L57) | 57 | `"    headers = {**ALLOWED_SHAPES[shape], \"Origin\": \"https://\" + PUBLIC_NAME}"` | — |
| [SRC-B106ADC5EF-L000058](../../tests/test_proxy_origin.py#L58) | 58 | `"    assert call(port, \"POST\", headers) == 200"` | — |
| [SRC-B106ADC5EF-L000059](../../tests/test_proxy_origin.py#L59) | 59 | `"    assert call(port, \"OPTIONS\", {k: v for k, v in headers.items() if k != \"Authorization\"}) == 204"` | — |
| [SRC-B106ADC5EF-L000060](../../tests/test_proxy_origin.py#L60) | 60 | `""` | — |
| [SRC-B106ADC5EF-L000061](../../tests/test_proxy_origin.py#L61) | 61 | `"@pytest.mark.parametrize(\"shape\", ALLOWED_SHAPES)"` | — |
| [SRC-B106ADC5EF-L000062](../../tests/test_proxy_origin.py#L62) | 62 | `"def test_a_foreign_site_is_still_refused(port, shape):"` | — |
| [SRC-B106ADC5EF-L000063](../../tests/test_proxy_origin.py#L63) | 63 | `"    headers = {**ALLOWED_SHAPES[shape], \"Origin\": \"https://evil.example\"}"` | — |
| [SRC-B106ADC5EF-L000064](../../tests/test_proxy_origin.py#L64) | 64 | `"    assert call(port, \"POST\", headers) == 403"` | — |
| [SRC-B106ADC5EF-L000065](../../tests/test_proxy_origin.py#L65) | 65 | `"    assert call(port, \"OPTIONS\", headers) == 403"` | — |
| [SRC-B106ADC5EF-L000066](../../tests/test_proxy_origin.py#L66) | 66 | `""` | — |
| [SRC-B106ADC5EF-L000067](../../tests/test_proxy_origin.py#L67) | 67 | `"def test_configured_origin_still_works_without_any_proxy_headers(port, monkeypatch):"` | — |
| [SRC-B106ADC5EF-L000068](../../tests/test_proxy_origin.py#L68) | 68 | `"    monkeypatch.setenv(\"OMARAI_ALLOWED_ORIGINS\", \"https://frontend.example\")"` | — |
| [SRC-B106ADC5EF-L000069](../../tests/test_proxy_origin.py#L69) | 69 | `"    headers = {\"Host\": \"127.0.0.1:8000\", \"Origin\": \"https://frontend.example\"}"` | — |
| [SRC-B106ADC5EF-L000070](../../tests/test_proxy_origin.py#L70) | 70 | `"    assert call(port, \"POST\", headers) == 200"` | — |
| [SRC-B106ADC5EF-L000071](../../tests/test_proxy_origin.py#L71) | 71 | `""` | — |
| [SRC-B106ADC5EF-L000072](../../tests/test_proxy_origin.py#L72) | 72 | `"def test_spoofed_forwarded_host_cannot_add_an_unapproved_origin(port):"` | — |
| [SRC-B106ADC5EF-L000073](../../tests/test_proxy_origin.py#L73) | 73 | `"    \"\"\"A client-supplied X-Forwarded-Host must not expand the CORS allowlist.\"\"\""` | — |
| [SRC-B106ADC5EF-L000074](../../tests/test_proxy_origin.py#L74) | 74 | `"    headers = {"` | — |
| [SRC-B106ADC5EF-L000075](../../tests/test_proxy_origin.py#L75) | 75 | `"        \"Host\": \"127.0.0.1:8000\","` | — |
| [SRC-B106ADC5EF-L000076](../../tests/test_proxy_origin.py#L76) | 76 | `"        \"X-Forwarded-Host\": \"evil.example\","` | — |
| [SRC-B106ADC5EF-L000077](../../tests/test_proxy_origin.py#L77) | 77 | `"        \"X-Forwarded-Proto\": \"https\","` | — |
| [SRC-B106ADC5EF-L000078](../../tests/test_proxy_origin.py#L78) | 78 | `"        \"Origin\": \"https://evil.example\","` | — |
| [SRC-B106ADC5EF-L000079](../../tests/test_proxy_origin.py#L79) | 79 | `"    }"` | — |
| [SRC-B106ADC5EF-L000080](../../tests/test_proxy_origin.py#L80) | 80 | `"    assert call(port, \"POST\", headers) == 403"` | — |
| [SRC-B106ADC5EF-L000081](../../tests/test_proxy_origin.py#L81) | 81 | `"    assert call("` | — |
| [SRC-B106ADC5EF-L000082](../../tests/test_proxy_origin.py#L82) | 82 | `"        port,"` | — |
| [SRC-B106ADC5EF-L000083](../../tests/test_proxy_origin.py#L83) | 83 | `"        \"OPTIONS\","` | — |
| [SRC-B106ADC5EF-L000084](../../tests/test_proxy_origin.py#L84) | 84 | `"        {key: value for key, value in headers.items() if key != \"Authorization\"},"` | — |
| [SRC-B106ADC5EF-L000085](../../tests/test_proxy_origin.py#L85) | 85 | `"    ) == 403"` | — |
| [SRC-B106ADC5EF-L000086](../../tests/test_proxy_origin.py#L86) | 86 | `""` | — |
## اختبارات

### FILE-C353AAAC10 — [tests/test_request_budget.py](../../tests/test_request_budget.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C353AAAC10-L000001](../../tests/test_request_budget.py#L1) | 1 | `"\"\"\"Unit tests for Omarai's per-request resource budget.\"\"\""` | — |
| [SRC-C353AAAC10-L000002](../../tests/test_request_budget.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-C353AAAC10-L000003](../../tests/test_request_budget.py#L3) | 3 | `""` | — |
| [SRC-C353AAAC10-L000004](../../tests/test_request_budget.py#L4) | 4 | `"import pytest"` | — |
| [SRC-C353AAAC10-L000005](../../tests/test_request_budget.py#L5) | 5 | `""` | — |
| [SRC-C353AAAC10-L000006](../../tests/test_request_budget.py#L6) | 6 | `"from agents.request_budget import RequestBudget, RequestBudgetExceeded"` | — |
| [SRC-C353AAAC10-L000007](../../tests/test_request_budget.py#L7) | 7 | `""` | — |
| [SRC-C353AAAC10-L000008](../../tests/test_request_budget.py#L8) | 8 | `""` | — |
| [SRC-C353AAAC10-L000009](../../tests/test_request_budget.py#L9) | 9 | `"class FakeClock:"` | — |
| [SRC-C353AAAC10-L000010](../../tests/test_request_budget.py#L10) | 10 | `"    def __init__(self, value: float = 100.0) -> None:"` | — |
| [SRC-C353AAAC10-L000011](../../tests/test_request_budget.py#L11) | 11 | `"        self.value = value"` | — |
| [SRC-C353AAAC10-L000012](../../tests/test_request_budget.py#L12) | 12 | `""` | — |
| [SRC-C353AAAC10-L000013](../../tests/test_request_budget.py#L13) | 13 | `"    def __call__(self) -> float:"` | — |
| [SRC-C353AAAC10-L000014](../../tests/test_request_budget.py#L14) | 14 | `"        return self.value"` | — |
| [SRC-C353AAAC10-L000015](../../tests/test_request_budget.py#L15) | 15 | `""` | — |
| [SRC-C353AAAC10-L000016](../../tests/test_request_budget.py#L16) | 16 | `""` | — |
| [SRC-C353AAAC10-L000017](../../tests/test_request_budget.py#L17) | 17 | `"def test_resource_reservations_are_bounded_and_thread_safe_in_snapshot():"` | — |
| [SRC-C353AAAC10-L000018](../../tests/test_request_budget.py#L18) | 18 | `"    clock = FakeClock()"` | — |
| [SRC-C353AAAC10-L000019](../../tests/test_request_budget.py#L19) | 19 | `"    budget = RequestBudget("` | — |
| [SRC-C353AAAC10-L000020](../../tests/test_request_budget.py#L20) | 20 | `"        timeout_seconds=10,"` | — |
| [SRC-C353AAAC10-L000021](../../tests/test_request_budget.py#L21) | 21 | `"        limits={\"search_calls\": 1},"` | — |
| [SRC-C353AAAC10-L000022](../../tests/test_request_budget.py#L22) | 22 | `"        clock=clock,"` | — |
| [SRC-C353AAAC10-L000023](../../tests/test_request_budget.py#L23) | 23 | `"    )"` | — |
| [SRC-C353AAAC10-L000024](../../tests/test_request_budget.py#L24) | 24 | `""` | — |
| [SRC-C353AAAC10-L000025](../../tests/test_request_budget.py#L25) | 25 | `"    budget.reserve(\"search_calls\")"` | — |
| [SRC-C353AAAC10-L000026](../../tests/test_request_budget.py#L26) | 26 | `"    with pytest.raises(RequestBudgetExceeded, match=\"search_calls\"):"` | — |
| [SRC-C353AAAC10-L000027](../../tests/test_request_budget.py#L27) | 27 | `"        budget.reserve(\"search_calls\")"` | — |
| [SRC-C353AAAC10-L000028](../../tests/test_request_budget.py#L28) | 28 | `""` | — |
| [SRC-C353AAAC10-L000029](../../tests/test_request_budget.py#L29) | 29 | `"    snapshot = budget.snapshot()"` | — |
| [SRC-C353AAAC10-L000030](../../tests/test_request_budget.py#L30) | 30 | `"    assert snapshot[\"counts\"][\"search_calls\"] == 1"` | — |
| [SRC-C353AAAC10-L000031](../../tests/test_request_budget.py#L31) | 31 | `"    assert snapshot[\"limits\"][\"search_calls\"] == 1"` | — |
| [SRC-C353AAAC10-L000032](../../tests/test_request_budget.py#L32) | 32 | `"    assert snapshot[\"deadline_exceeded\"] is False"` | — |
| [SRC-C353AAAC10-L000033](../../tests/test_request_budget.py#L33) | 33 | `""` | — |
| [SRC-C353AAAC10-L000034](../../tests/test_request_budget.py#L34) | 34 | `""` | — |
| [SRC-C353AAAC10-L000035](../../tests/test_request_budget.py#L35) | 35 | `"def test_deadline_blocks_new_work_and_caps_outbound_timeout():"` | — |
| [SRC-C353AAAC10-L000036](../../tests/test_request_budget.py#L36) | 36 | `"    clock = FakeClock()"` | — |
| [SRC-C353AAAC10-L000037](../../tests/test_request_budget.py#L37) | 37 | `"    budget = RequestBudget(timeout_seconds=10, clock=clock)"` | — |
| [SRC-C353AAAC10-L000038](../../tests/test_request_budget.py#L38) | 38 | `""` | — |
| [SRC-C353AAAC10-L000039](../../tests/test_request_budget.py#L39) | 39 | `"    clock.value += 7"` | — |
| [SRC-C353AAAC10-L000040](../../tests/test_request_budget.py#L40) | 40 | `"    assert budget.timeout_for(30) == pytest.approx(3)"` | — |
| [SRC-C353AAAC10-L000041](../../tests/test_request_budget.py#L41) | 41 | `"    assert budget.timeout_for(1) == pytest.approx(1)"` | — |
| [SRC-C353AAAC10-L000042](../../tests/test_request_budget.py#L42) | 42 | `""` | — |
| [SRC-C353AAAC10-L000043](../../tests/test_request_budget.py#L43) | 43 | `"    clock.value += 4"` | — |
| [SRC-C353AAAC10-L000044](../../tests/test_request_budget.py#L44) | 44 | `"    assert budget.remaining_seconds() == 0"` | — |
| [SRC-C353AAAC10-L000045](../../tests/test_request_budget.py#L45) | 45 | `"    with pytest.raises(RequestBudgetExceeded, match=\"وقت الطلب\"):"` | — |
| [SRC-C353AAAC10-L000046](../../tests/test_request_budget.py#L46) | 46 | `"        budget.reserve(\"model_calls\")"` | — |
| [SRC-C353AAAC10-L000047](../../tests/test_request_budget.py#L47) | 47 | `"    with pytest.raises(RequestBudgetExceeded, match=\"وقت الطلب\"):"` | — |
| [SRC-C353AAAC10-L000048](../../tests/test_request_budget.py#L48) | 48 | `"        budget.timeout_for(3)"` | — |
| [SRC-C353AAAC10-L000049](../../tests/test_request_budget.py#L49) | 49 | `""` | — |
| [SRC-C353AAAC10-L000050](../../tests/test_request_budget.py#L50) | 50 | `""` | — |
| [SRC-C353AAAC10-L000051](../../tests/test_request_budget.py#L51) | 51 | `"def test_environment_overrides_are_clamped(monkeypatch):"` | — |
| [SRC-C353AAAC10-L000052](../../tests/test_request_budget.py#L52) | 52 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_BUDGET_SECONDS\", \"999\")"` | — |
| [SRC-C353AAAC10-L000053](../../tests/test_request_budget.py#L53) | 53 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_SEARCH_CALLS\", \"999\")"` | — |
| [SRC-C353AAAC10-L000054](../../tests/test_request_budget.py#L54) | 54 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_MODEL_CALLS\", \"-1\")"` | — |
| [SRC-C353AAAC10-L000055](../../tests/test_request_budget.py#L55) | 55 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_TOOL_CALLS\", \"-1\")"` | — |
| [SRC-C353AAAC10-L000056](../../tests/test_request_budget.py#L56) | 56 | `""` | — |
| [SRC-C353AAAC10-L000057](../../tests/test_request_budget.py#L57) | 57 | `"    snapshot = RequestBudget.from_environment().snapshot()"` | — |
| [SRC-C353AAAC10-L000058](../../tests/test_request_budget.py#L58) | 58 | `""` | — |
| [SRC-C353AAAC10-L000059](../../tests/test_request_budget.py#L59) | 59 | `"    assert snapshot[\"timeout_seconds\"] == 120"` | — |
| [SRC-C353AAAC10-L000060](../../tests/test_request_budget.py#L60) | 60 | `"    assert snapshot[\"limits\"][\"search_calls\"] == 40"` | — |
| [SRC-C353AAAC10-L000061](../../tests/test_request_budget.py#L61) | 61 | `"    assert snapshot[\"limits\"][\"model_calls\"] == 1"` | — |
| [SRC-C353AAAC10-L000062](../../tests/test_request_budget.py#L62) | 62 | `"    assert snapshot[\"limits\"][\"tool_calls\"] == 0"` | — |
| [SRC-C353AAAC10-L000063](../../tests/test_request_budget.py#L63) | 63 | `""` | — |
| [SRC-C353AAAC10-L000064](../../tests/test_request_budget.py#L64) | 64 | `""` | — |
| [SRC-C353AAAC10-L000065](../../tests/test_request_budget.py#L65) | 65 | `"def test_web_agent_reserves_search_model_and_page_work_before_io(monkeypatch):"` | — |
| [SRC-C353AAAC10-L000066](../../tests/test_request_budget.py#L66) | 66 | `"    from agents.web_agent import WebAgent"` | — |
| [SRC-C353AAAC10-L000067](../../tests/test_request_budget.py#L67) | 67 | `""` | — |
| [SRC-C353AAAC10-L000068](../../tests/test_request_budget.py#L68) | 68 | `"    agent = WebAgent()"` | — |
| [SRC-C353AAAC10-L000069](../../tests/test_request_budget.py#L69) | 69 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-C353AAAC10-L000070](../../tests/test_request_budget.py#L70) | 70 | `""` | — |
| [SRC-C353AAAC10-L000071](../../tests/test_request_budget.py#L71) | 71 | `"    agent._request_budget = RequestBudget(limits={\"search_queries\": 0})"` | — |
| [SRC-C353AAAC10-L000072](../../tests/test_request_budget.py#L72) | 72 | `"    with pytest.raises(RequestBudgetExceeded, match=\"search_queries\"):"` | — |
| [SRC-C353AAAC10-L000073](../../tests/test_request_budget.py#L73) | 73 | `"        agent._search_web(\"budget test\")"` | — |
| [SRC-C353AAAC10-L000074](../../tests/test_request_budget.py#L74) | 74 | `""` | — |
| [SRC-C353AAAC10-L000075](../../tests/test_request_budget.py#L75) | 75 | `"    agent._request_budget = RequestBudget(limits={\"model_calls\": 0})"` | — |
| [SRC-C353AAAC10-L000076](../../tests/test_request_budget.py#L76) | 76 | `"    monkeypatch.setattr("` | — |
| [SRC-C353AAAC10-L000077](../../tests/test_request_budget.py#L77) | 77 | `"        \"agents.web_agent.urllib.request.urlopen\","` | — |
| [SRC-C353AAAC10-L000078](../../tests/test_request_budget.py#L78) | 78 | `"        lambda *args, **kwargs: pytest.fail(\"model HTTP request must not start\"),"` | — |
| [SRC-C353AAAC10-L000079](../../tests/test_request_budget.py#L79) | 79 | `"    )"` | — |
| [SRC-C353AAAC10-L000080](../../tests/test_request_budget.py#L80) | 80 | `"    with pytest.raises(RequestBudgetExceeded, match=\"model_calls\"):"` | — |
| [SRC-C353AAAC10-L000081](../../tests/test_request_budget.py#L81) | 81 | `"        agent._request_completion([{\"role\": \"user\", \"content\": \"test\"}])"` | — |
| [SRC-C353AAAC10-L000082](../../tests/test_request_budget.py#L82) | 82 | `""` | — |
| [SRC-C353AAAC10-L000083](../../tests/test_request_budget.py#L83) | 83 | `"    agent._request_budget = RequestBudget(limits={\"page_fetches\": 0})"` | — |
| [SRC-C353AAAC10-L000084](../../tests/test_request_budget.py#L84) | 84 | `"    with pytest.raises(RequestBudgetExceeded, match=\"page_fetches\"):"` | — |
| [SRC-C353AAAC10-L000085](../../tests/test_request_budget.py#L85) | 85 | `"        agent._fetch_page(\"https://example.com/\")"` | — |
| [SRC-C353AAAC10-L000086](../../tests/test_request_budget.py#L86) | 86 | `""` | — |
| [SRC-C353AAAC10-L000087](../../tests/test_request_budget.py#L87) | 87 | `""` | — |
| [SRC-C353AAAC10-L000088](../../tests/test_request_budget.py#L88) | 88 | `"def test_social_provider_reserves_budget_before_network_io(monkeypatch):"` | — |
| [SRC-C353AAAC10-L000089](../../tests/test_request_budget.py#L89) | 89 | `"    from agents.web_agent import WebAgent"` | — |
| [SRC-C353AAAC10-L000090](../../tests/test_request_budget.py#L90) | 90 | `""` | — |
| [SRC-C353AAAC10-L000091](../../tests/test_request_budget.py#L91) | 91 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_ID\", \"test-client\")"` | — |
| [SRC-C353AAAC10-L000092](../../tests/test_request_budget.py#L92) | 92 | `"    monkeypatch.setenv(\"REDDIT_CLIENT_SECRET\", \"test-secret\")"` | — |
| [SRC-C353AAAC10-L000093](../../tests/test_request_budget.py#L93) | 93 | `"    agent = WebAgent()"` | — |
| [SRC-C353AAAC10-L000094](../../tests/test_request_budget.py#L94) | 94 | `"    agent._request_budget = RequestBudget(limits={\"search_calls\": 0})"` | — |
| [SRC-C353AAAC10-L000095](../../tests/test_request_budget.py#L95) | 95 | `""` | — |
| [SRC-C353AAAC10-L000096](../../tests/test_request_budget.py#L96) | 96 | `"    monkeypatch.setattr("` | — |
| [SRC-C353AAAC10-L000097](../../tests/test_request_budget.py#L97) | 97 | `"        \"httpx.post\","` | — |
| [SRC-C353AAAC10-L000098](../../tests/test_request_budget.py#L98) | 98 | `"        lambda *args, **kwargs: pytest.fail(\"social HTTP request must not start\"),"` | — |
| [SRC-C353AAAC10-L000099](../../tests/test_request_budget.py#L99) | 99 | `"    )"` | — |
| [SRC-C353AAAC10-L000100](../../tests/test_request_budget.py#L100) | 100 | `"    with pytest.raises(RequestBudgetExceeded, match=\"search_calls\"):"` | — |
| [SRC-C353AAAC10-L000101](../../tests/test_request_budget.py#L101) | 101 | `"        agent._search_social(\"budget test\", [\"reddit\"])"` | — |
| [SRC-C353AAAC10-L000102](../../tests/test_request_budget.py#L102) | 102 | `""` | — |
| [SRC-C353AAAC10-L000103](../../tests/test_request_budget.py#L103) | 103 | `""` | — |
| [SRC-C353AAAC10-L000104](../../tests/test_request_budget.py#L104) | 104 | `"@pytest.mark.parametrize("` | — |
| [SRC-C353AAAC10-L000105](../../tests/test_request_budget.py#L105) | 105 | `"    (\"resource\", \"limit\"),"` | — |
| [SRC-C353AAAC10-L000106](../../tests/test_request_budget.py#L106) | 106 | `"    ["` | — |
| [SRC-C353AAAC10-L000107](../../tests/test_request_budget.py#L107) | 107 | `"        (\"search_queries\", 8),"` | — |
| [SRC-C353AAAC10-L000108](../../tests/test_request_budget.py#L108) | 108 | `"        (\"search_calls\", 32),"` | — |
| [SRC-C353AAAC10-L000109](../../tests/test_request_budget.py#L109) | 109 | `"        (\"model_calls\", 8),"` | — |
| [SRC-C353AAAC10-L000110](../../tests/test_request_budget.py#L110) | 110 | `"        (\"page_fetches\", 8),"` | — |
| [SRC-C353AAAC10-L000111](../../tests/test_request_budget.py#L111) | 111 | `"        (\"tool_calls\", 3),"` | — |
| [SRC-C353AAAC10-L000112](../../tests/test_request_budget.py#L112) | 112 | `"    ],"` | — |
| [SRC-C353AAAC10-L000113](../../tests/test_request_budget.py#L113) | 113 | `")"` | — |
| [SRC-C353AAAC10-L000114](../../tests/test_request_budget.py#L114) | 114 | `"def test_each_resource_counter_stops_at_its_limit(resource, limit):"` | — |
| [SRC-C353AAAC10-L000115](../../tests/test_request_budget.py#L115) | 115 | `"    budget = RequestBudget(timeout_seconds=10, limits={resource: limit})"` | — |
| [SRC-C353AAAC10-L000116](../../tests/test_request_budget.py#L116) | 116 | `""` | — |
| [SRC-C353AAAC10-L000117](../../tests/test_request_budget.py#L117) | 117 | `"    for expected_count in range(1, limit + 1):"` | — |
| [SRC-C353AAAC10-L000118](../../tests/test_request_budget.py#L118) | 118 | `"        budget.reserve(resource)"` | — |
| [SRC-C353AAAC10-L000119](../../tests/test_request_budget.py#L119) | 119 | `"        snapshot = budget.snapshot()"` | — |
| [SRC-C353AAAC10-L000120](../../tests/test_request_budget.py#L120) | 120 | `"        assert snapshot[\"counts\"][resource] == expected_count"` | — |
| [SRC-C353AAAC10-L000121](../../tests/test_request_budget.py#L121) | 121 | `"        assert snapshot[\"counts\"][resource] <= snapshot[\"limits\"][resource]"` | — |
| [SRC-C353AAAC10-L000122](../../tests/test_request_budget.py#L122) | 122 | `""` | — |
| [SRC-C353AAAC10-L000123](../../tests/test_request_budget.py#L123) | 123 | `"    with pytest.raises(RequestBudgetExceeded, match=resource):"` | — |
| [SRC-C353AAAC10-L000124](../../tests/test_request_budget.py#L124) | 124 | `"        budget.reserve(resource)"` | — |
| [SRC-C353AAAC10-L000125](../../tests/test_request_budget.py#L125) | 125 | `""` | — |
| [SRC-C353AAAC10-L000126](../../tests/test_request_budget.py#L126) | 126 | `"    snapshot = budget.snapshot()"` | — |
| [SRC-C353AAAC10-L000127](../../tests/test_request_budget.py#L127) | 127 | `"    assert snapshot[\"counts\"][resource] == limit"` | — |
| [SRC-C353AAAC10-L000128](../../tests/test_request_budget.py#L128) | 128 | `"    assert resource in snapshot[\"exhausted_reasons\"]"` | — |
| [SRC-C353AAAC10-L000129](../../tests/test_request_budget.py#L129) | 129 | `""` | — |
| [SRC-C353AAAC10-L000130](../../tests/test_request_budget.py#L130) | 130 | `""` | — |
| [SRC-C353AAAC10-L000131](../../tests/test_request_budget.py#L131) | 131 | `"@pytest.mark.parametrize("` | — |
| [SRC-C353AAAC10-L000132](../../tests/test_request_budget.py#L132) | 132 | `"    \"resource\","` | — |
| [SRC-C353AAAC10-L000133](../../tests/test_request_budget.py#L133) | 133 | `"    [\"search_queries\", \"search_calls\", \"model_calls\", \"page_fetches\", \"tool_calls\"],"` | — |
| [SRC-C353AAAC10-L000134](../../tests/test_request_budget.py#L134) | 134 | `")"` | — |
| [SRC-C353AAAC10-L000135](../../tests/test_request_budget.py#L135) | 135 | `"def test_disabled_resource_never_starts_work(resource):"` | — |
| [SRC-C353AAAC10-L000136](../../tests/test_request_budget.py#L136) | 136 | `"    budget = RequestBudget(timeout_seconds=10, limits={resource: 0})"` | — |
| [SRC-C353AAAC10-L000137](../../tests/test_request_budget.py#L137) | 137 | `""` | — |
| [SRC-C353AAAC10-L000138](../../tests/test_request_budget.py#L138) | 138 | `"    assert budget.remaining_units(resource) == 0"` | — |
| [SRC-C353AAAC10-L000139](../../tests/test_request_budget.py#L139) | 139 | `"    with pytest.raises(RequestBudgetExceeded, match=resource):"` | — |
| [SRC-C353AAAC10-L000140](../../tests/test_request_budget.py#L140) | 140 | `"        budget.reserve(resource)"` | — |
| [SRC-C353AAAC10-L000141](../../tests/test_request_budget.py#L141) | 141 | `""` | — |
| [SRC-C353AAAC10-L000142](../../tests/test_request_budget.py#L142) | 142 | `"    snapshot = budget.snapshot()"` | — |
| [SRC-C353AAAC10-L000143](../../tests/test_request_budget.py#L143) | 143 | `"    assert snapshot[\"counts\"][resource] == 0"` | — |
| [SRC-C353AAAC10-L000144](../../tests/test_request_budget.py#L144) | 144 | `"    assert snapshot[\"limits\"][resource] == 0"` | — |
| [SRC-C353AAAC10-L000145](../../tests/test_request_budget.py#L145) | 145 | `"    assert resource in snapshot[\"disabled_resources\"]"` | — |
| [SRC-C353AAAC10-L000146](../../tests/test_request_budget.py#L146) | 146 | `"    assert resource in snapshot[\"exhausted_reasons\"]"` | — |
## اختبارات

### FILE-6BF96689A8 — [tests/test_research.py](../../tests/test_research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6BF96689A8-L000001](../../tests/test_research.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-6BF96689A8-L000002](../../tests/test_research.py#L2) | 2 | `""` | — |
| [SRC-6BF96689A8-L000003](../../tests/test_research.py#L3) | 3 | `"from agents.research import ("` | — |
| [SRC-6BF96689A8-L000004](../../tests/test_research.py#L4) | 4 | `"    evidence_signal_report,"` | — |
| [SRC-6BF96689A8-L000005](../../tests/test_research.py#L5) | 5 | `"    fallback_plan,"` | — |
| [SRC-6BF96689A8-L000006](../../tests/test_research.py#L6) | 6 | `"    fuse_ranked_results,"` | — |
| [SRC-6BF96689A8-L000007](../../tests/test_research.py#L7) | 7 | `"    registrable_domain,"` | — |
| [SRC-6BF96689A8-L000008](../../tests/test_research.py#L8) | 8 | `"    validate_plan,"` | — |
| [SRC-6BF96689A8-L000009](../../tests/test_research.py#L9) | 9 | `")"` | — |
| [SRC-6BF96689A8-L000010](../../tests/test_research.py#L10) | 10 | `""` | — |
| [SRC-6BF96689A8-L000011](../../tests/test_research.py#L11) | 11 | `""` | — |
| [SRC-6BF96689A8-L000012](../../tests/test_research.py#L12) | 12 | `"def test_social_question_gets_platform_targeted_queries():"` | — |
| [SRC-6BF96689A8-L000013](../../tests/test_research.py#L13) | 13 | `"    plan = fallback_plan(\"ابحث في Reddit عن تجارب العملاء مع السيارات الكهربائية\")"` | — |
| [SRC-6BF96689A8-L000014](../../tests/test_research.py#L14) | 14 | `"    assert plan[\"social_focus\"] is True"` | — |
| [SRC-6BF96689A8-L000015](../../tests/test_research.py#L15) | 15 | `"    assert \"reddit\" in plan[\"platforms\"]"` | — |
| [SRC-6BF96689A8-L000016](../../tests/test_research.py#L16) | 16 | `"    assert any(\"site:reddit.com\" in query for query in plan[\"queries\"])"` | — |
| [SRC-6BF96689A8-L000017](../../tests/test_research.py#L17) | 17 | `"    assert len(plan[\"queries\"]) <= 8"` | — |
| [SRC-6BF96689A8-L000018](../../tests/test_research.py#L18) | 18 | `""` | — |
| [SRC-6BF96689A8-L000019](../../tests/test_research.py#L19) | 19 | `""` | — |
| [SRC-6BF96689A8-L000020](../../tests/test_research.py#L20) | 20 | `"def test_follow_up_query_keeps_prior_topic():"` | — |
| [SRC-6BF96689A8-L000021](../../tests/test_research.py#L21) | 21 | `"    history = [{\"role\": \"user\", \"content\": \"قارن سوق السيارات الكهربائية في مصر\"}]"` | — |
| [SRC-6BF96689A8-L000022](../../tests/test_research.py#L22) | 22 | `"    plan = fallback_plan(\"وطب الأسعار الحالية؟\", history)"` | — |
| [SRC-6BF96689A8-L000023](../../tests/test_research.py#L23) | 23 | `"    assert \"السيارات الكهربائية\" in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000024](../../tests/test_research.py#L24) | 24 | `"    assert plan[\"freshness\"] == \"current\""` | — |
| [SRC-6BF96689A8-L000025](../../tests/test_research.py#L25) | 25 | `""` | — |
| [SRC-6BF96689A8-L000026](../../tests/test_research.py#L26) | 26 | `""` | — |
| [SRC-6BF96689A8-L000027](../../tests/test_research.py#L27) | 27 | `"def test_plan_validation_caps_queries_and_rejects_non_string_values():"` | — |
| [SRC-6BF96689A8-L000028](../../tests/test_research.py#L28) | 28 | `"    candidate = {"` | — |
| [SRC-6BF96689A8-L000029](../../tests/test_research.py#L29) | 29 | `"        \"queries\": [\"بحث أ\", \"بحث ب\", None, \"بحث ج\", \"بحث د\", \"بحث هـ\", \"بحث سادس\", \"بحث سابع\", \"بحث ثامن\", \"بحث تاسع\"],"` | — |
| [SRC-6BF96689A8-L000030](../../tests/test_research.py#L30) | 30 | `"        \"social_focus\": True,"` | — |
| [SRC-6BF96689A8-L000031](../../tests/test_research.py#L31) | 31 | `"        \"freshness\": \"current\","` | — |
| [SRC-6BF96689A8-L000032](../../tests/test_research.py#L32) | 32 | `"        \"depth\": \"deep\","` | — |
| [SRC-6BF96689A8-L000033](../../tests/test_research.py#L33) | 33 | `"        \"platforms\": [\"reddit\", \"unknown\"],"` | — |
| [SRC-6BF96689A8-L000034](../../tests/test_research.py#L34) | 34 | `"    }"` | — |
| [SRC-6BF96689A8-L000035](../../tests/test_research.py#L35) | 35 | `"    plan = validate_plan(candidate, \"بحث عن منشورات\")"` | — |
| [SRC-6BF96689A8-L000036](../../tests/test_research.py#L36) | 36 | `"    assert len(plan[\"queries\"]) <= 8"` | — |
| [SRC-6BF96689A8-L000037](../../tests/test_research.py#L37) | 37 | `"    assert \"unknown\" not in plan[\"platforms\"]"` | — |
| [SRC-6BF96689A8-L000038](../../tests/test_research.py#L38) | 38 | `"    assert plan[\"social_focus\"] is True"` | — |
| [SRC-6BF96689A8-L000039](../../tests/test_research.py#L39) | 39 | `"    assert plan[\"freshness\"] == \"current\""` | — |
| [SRC-6BF96689A8-L000040](../../tests/test_research.py#L40) | 40 | `""` | — |
| [SRC-6BF96689A8-L000041](../../tests/test_research.py#L41) | 41 | `""` | — |
| [SRC-6BF96689A8-L000042](../../tests/test_research.py#L42) | 42 | `"def test_rank_fusion_promotes_cross_provider_consensus_and_deduplicates():"` | — |
| [SRC-6BF96689A8-L000043](../../tests/test_research.py#L43) | 43 | `"    batches = ["` | — |
| [SRC-6BF96689A8-L000044](../../tests/test_research.py#L44) | 44 | `"        {"` | — |
| [SRC-6BF96689A8-L000045](../../tests/test_research.py#L45) | 45 | `"            \"query\": \"cars Egypt\","` | — |
| [SRC-6BF96689A8-L000046](../../tests/test_research.py#L46) | 46 | `"            \"provider\": \"ddg\","` | — |
| [SRC-6BF96689A8-L000047](../../tests/test_research.py#L47) | 47 | `"            \"results\": ["` | — |
| [SRC-6BF96689A8-L000048](../../tests/test_research.py#L48) | 48 | `"                {\"title\": \"A\", \"url\": \"https://www.example.com/a?utm_source=x\", \"snippet\": \"A\"},"` | — |
| [SRC-6BF96689A8-L000049](../../tests/test_research.py#L49) | 49 | `"                {\"title\": \"B\", \"url\": \"https://example.com/b\", \"snippet\": \"B\"},"` | — |
| [SRC-6BF96689A8-L000050](../../tests/test_research.py#L50) | 50 | `"            ],"` | — |
| [SRC-6BF96689A8-L000051](../../tests/test_research.py#L51) | 51 | `"        },"` | — |
| [SRC-6BF96689A8-L000052](../../tests/test_research.py#L52) | 52 | `"        {"` | — |
| [SRC-6BF96689A8-L000053](../../tests/test_research.py#L53) | 53 | `"            \"query\": \"electric vehicles Egypt\","` | — |
| [SRC-6BF96689A8-L000054](../../tests/test_research.py#L54) | 54 | `"            \"provider\": \"bing\","` | — |
| [SRC-6BF96689A8-L000055](../../tests/test_research.py#L55) | 55 | `"            \"results\": ["` | — |
| [SRC-6BF96689A8-L000056](../../tests/test_research.py#L56) | 56 | `"                {\"title\": \"A better title\", \"url\": \"https://example.com/a\", \"snippet\": \"Longer evidence snippet\"},"` | — |
| [SRC-6BF96689A8-L000057](../../tests/test_research.py#L57) | 57 | `"                {\"title\": \"C\", \"url\": \"https://example.com/c\", \"snippet\": \"C\"},"` | — |
| [SRC-6BF96689A8-L000058](../../tests/test_research.py#L58) | 58 | `"            ],"` | — |
| [SRC-6BF96689A8-L000059](../../tests/test_research.py#L59) | 59 | `"        },"` | — |
| [SRC-6BF96689A8-L000060](../../tests/test_research.py#L60) | 60 | `"    ]"` | — |
| [SRC-6BF96689A8-L000061](../../tests/test_research.py#L61) | 61 | `"    ranked = fuse_ranked_results(batches)"` | — |
| [SRC-6BF96689A8-L000062](../../tests/test_research.py#L62) | 62 | `"    urls = [source[\"url\"] for source in ranked]"` | — |
| [SRC-6BF96689A8-L000063](../../tests/test_research.py#L63) | 63 | `"    assert len(urls) == 3"` | — |
| [SRC-6BF96689A8-L000064](../../tests/test_research.py#L64) | 64 | `"    source_a = next(source for source in ranked if \"example.com/a\" in source[\"url\"])"` | — |
| [SRC-6BF96689A8-L000065](../../tests/test_research.py#L65) | 65 | `"    assert len(source_a[\"providers\"]) == 2"` | — |
| [SRC-6BF96689A8-L000066](../../tests/test_research.py#L66) | 66 | `"    assert len(source_a[\"queries\"]) == 2"` | — |
| [SRC-6BF96689A8-L000067](../../tests/test_research.py#L67) | 67 | `"    assert source_a[\"rank_score\"] > next("` | — |
| [SRC-6BF96689A8-L000068](../../tests/test_research.py#L68) | 68 | `"        source[\"rank_score\"] for source in ranked if \"example.com/c\" in source[\"url\"]"` | — |
| [SRC-6BF96689A8-L000069](../../tests/test_research.py#L69) | 69 | `"    )"` | — |
| [SRC-6BF96689A8-L000070](../../tests/test_research.py#L70) | 70 | `""` | — |
| [SRC-6BF96689A8-L000071](../../tests/test_research.py#L71) | 71 | `""` | — |
| [SRC-6BF96689A8-L000072](../../tests/test_research.py#L72) | 72 | `"def test_source_classification_distinguishes_social_and_government():"` | — |
| [SRC-6BF96689A8-L000073](../../tests/test_research.py#L73) | 73 | `"    from agents.research import classify_source"` | — |
| [SRC-6BF96689A8-L000074](../../tests/test_research.py#L74) | 74 | `""` | — |
| [SRC-6BF96689A8-L000075](../../tests/test_research.py#L75) | 75 | `"    assert classify_source(\"https://www.reddit.com/r/example/comments/1\")[\"platform\"] == \"reddit\""` | — |
| [SRC-6BF96689A8-L000076](../../tests/test_research.py#L76) | 76 | `"    assert classify_source(\"https://example.gov.eg/page\")[\"source_class\"] == \"government\""` | — |
| [SRC-6BF96689A8-L000077](../../tests/test_research.py#L77) | 77 | `""` | — |
| [SRC-6BF96689A8-L000078](../../tests/test_research.py#L78) | 78 | `""` | — |
| [SRC-6BF96689A8-L000079](../../tests/test_research.py#L79) | 79 | `"def test_explicit_page_urls_are_extracted_and_not_left_in_search_terms():"` | — |
| [SRC-6BF96689A8-L000080](../../tests/test_research.py#L80) | 80 | `"    from agents.research import extract_urls"` | — |
| [SRC-6BF96689A8-L000081](../../tests/test_research.py#L81) | 81 | `""` | — |
| [SRC-6BF96689A8-L000082](../../tests/test_research.py#L82) | 82 | `"    question = \"حلل هذه الصفحة بالتفصيل https://example.com/a?utm_source=chat#section.\""` | — |
| [SRC-6BF96689A8-L000083](../../tests/test_research.py#L83) | 83 | `"    plan = fallback_plan(question)"` | — |
| [SRC-6BF96689A8-L000084](../../tests/test_research.py#L84) | 84 | `"    assert extract_urls(question) == [\"https://example.com/a?utm_source=chat#section\"]"` | — |
| [SRC-6BF96689A8-L000085](../../tests/test_research.py#L85) | 85 | `"    assert plan[\"direct_urls\"] == [\"https://example.com/a?utm_source=chat#section\"]"` | — |
| [SRC-6BF96689A8-L000086](../../tests/test_research.py#L86) | 86 | `"    assert \"https://\" not in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000087](../../tests/test_research.py#L87) | 87 | `""` | — |
| [SRC-6BF96689A8-L000088](../../tests/test_research.py#L88) | 88 | `"def test_registrable_domain_groups_subdomains_and_respects_public_suffixes():"` | — |
| [SRC-6BF96689A8-L000089](../../tests/test_research.py#L89) | 89 | `"    assert registrable_domain(\"news.example.com\") == \"example.com\""` | — |
| [SRC-6BF96689A8-L000090](../../tests/test_research.py#L90) | 90 | `"    assert registrable_domain(\"offers.example.com\") == \"example.com\""` | — |
| [SRC-6BF96689A8-L000091](../../tests/test_research.py#L91) | 91 | `"    assert registrable_domain(\"news.example.co.uk\") == \"example.co.uk\""` | — |
| [SRC-6BF96689A8-L000092](../../tests/test_research.py#L92) | 92 | `"    assert registrable_domain(\"other.co.uk\") == \"other.co.uk\""` | — |
| [SRC-6BF96689A8-L000093](../../tests/test_research.py#L93) | 93 | `"    assert registrable_domain(\"alice.github.io\") == \"alice.github.io\""` | — |
| [SRC-6BF96689A8-L000094](../../tests/test_research.py#L94) | 94 | `"    assert registrable_domain(\"https://www.example.com/path\") == \"example.com\""` | — |
| [SRC-6BF96689A8-L000095](../../tests/test_research.py#L95) | 95 | `""` | — |
| [SRC-6BF96689A8-L000096](../../tests/test_research.py#L96) | 96 | `""` | — |
| [SRC-6BF96689A8-L000097](../../tests/test_research.py#L97) | 97 | `"def test_evidence_coverage_does_not_count_sibling_subdomains_as_independent():"` | — |
| [SRC-6BF96689A8-L000098](../../tests/test_research.py#L98) | 98 | `"    report = evidence_signal_report(["` | — |
| [SRC-6BF96689A8-L000099](../../tests/test_research.py#L99) | 99 | `"        {"` | — |
| [SRC-6BF96689A8-L000100](../../tests/test_research.py#L100) | 100 | `"            \"url\": \"https://news.example.com/story\","` | — |
| [SRC-6BF96689A8-L000101](../../tests/test_research.py#L101) | 101 | `"            \"domain\": \"news.example.com\","` | — |
| [SRC-6BF96689A8-L000102](../../tests/test_research.py#L102) | 102 | `"            \"providers\": [\"search_a\"],"` | — |
| [SRC-6BF96689A8-L000103](../../tests/test_research.py#L103) | 103 | `"        },"` | — |
| [SRC-6BF96689A8-L000104](../../tests/test_research.py#L104) | 104 | `"        {"` | — |
| [SRC-6BF96689A8-L000105](../../tests/test_research.py#L105) | 105 | `"            \"url\": \"https://offers.example.com/second-story\","` | — |
| [SRC-6BF96689A8-L000106](../../tests/test_research.py#L106) | 106 | `"            \"domain\": \"offers.example.com\","` | — |
| [SRC-6BF96689A8-L000107](../../tests/test_research.py#L107) | 107 | `"            \"providers\": [\"search_b\"],"` | — |
| [SRC-6BF96689A8-L000108](../../tests/test_research.py#L108) | 108 | `"        },"` | — |
| [SRC-6BF96689A8-L000109](../../tests/test_research.py#L109) | 109 | `"    ])"` | — |
| [SRC-6BF96689A8-L000110](../../tests/test_research.py#L110) | 110 | `"    assert report[\"unique_domains\"] == 1"` | — |
| [SRC-6BF96689A8-L000111](../../tests/test_research.py#L111) | 111 | `"    assert report[\"coverage_level\"] == \"محدود\""` | — |
| [SRC-6BF96689A8-L000112](../../tests/test_research.py#L112) | 112 | `""` | — |
| [SRC-6BF96689A8-L000113](../../tests/test_research.py#L113) | 113 | `""` | — |
| [SRC-6BF96689A8-L000114](../../tests/test_research.py#L114) | 114 | `""` | — |
| [SRC-6BF96689A8-L000115](../../tests/test_research.py#L115) | 115 | `"def test_standard_fallback_plan_does_not_add_deep_research_query():"` | — |
| [SRC-6BF96689A8-L000116](../../tests/test_research.py#L116) | 116 | `"    plan = fallback_plan(\"اشرح طريقة عمل المحرك الكهربائي\")"` | — |
| [SRC-6BF96689A8-L000117](../../tests/test_research.py#L117) | 117 | `"    assert plan[\"depth\"] == \"standard\""` | — |
| [SRC-6BF96689A8-L000118](../../tests/test_research.py#L118) | 118 | `"    assert not any(\"مصادر موثوقة تقارير إحصاءات\" in query for query in plan[\"queries\"])"` | — |
| [SRC-6BF96689A8-L000119](../../tests/test_research.py#L119) | 119 | `""` | — |
| [SRC-6BF96689A8-L000120](../../tests/test_research.py#L120) | 120 | `""` | — |
| [SRC-6BF96689A8-L000121](../../tests/test_research.py#L121) | 121 | `"def test_deep_fallback_plan_adds_deep_research_query_for_explicit_comparison():"` | — |
| [SRC-6BF96689A8-L000122](../../tests/test_research.py#L122) | 122 | `"    plan = fallback_plan(\"قارن مميزات وعيوب المحرك الكهربائي\")"` | — |
| [SRC-6BF96689A8-L000123](../../tests/test_research.py#L123) | 123 | `"    assert plan[\"depth\"] == \"deep\""` | — |
| [SRC-6BF96689A8-L000124](../../tests/test_research.py#L124) | 124 | `"    assert any(\"مصادر موثوقة تقارير إحصاءات\" in query for query in plan[\"queries\"])"` | — |
| [SRC-6BF96689A8-L000125](../../tests/test_research.py#L125) | 125 | `""` | — |
| [SRC-6BF96689A8-L000126](../../tests/test_research.py#L126) | 126 | `""` | — |
| [SRC-6BF96689A8-L000127](../../tests/test_research.py#L127) | 127 | `"def test_fallback_plan_expands_warranty_followup_with_previous_topic():"` | — |
| [SRC-6BF96689A8-L000128](../../tests/test_research.py#L128) | 128 | `"    history = ["` | — |
| [SRC-6BF96689A8-L000129](../../tests/test_research.py#L129) | 129 | `"        {\"role\": \"user\", \"content\": \"سعر آيفون 16 في مصر\"},"` | — |
| [SRC-6BF96689A8-L000130](../../tests/test_research.py#L130) | 130 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن معلومات حديثة.\"},"` | — |
| [SRC-6BF96689A8-L000131](../../tests/test_research.py#L131) | 131 | `"    ]"` | — |
| [SRC-6BF96689A8-L000132](../../tests/test_research.py#L132) | 132 | `"    plan = fallback_plan(\"هل فيه ضمان؟\", history)"` | — |
| [SRC-6BF96689A8-L000133](../../tests/test_research.py#L133) | 133 | `"    assert \"آيفون 16\" in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000134](../../tests/test_research.py#L134) | 134 | `"    assert \"ضمان\" in plan[\"queries\"][0]"` | — |
| [SRC-6BF96689A8-L000135](../../tests/test_research.py#L135) | 135 | `""` | — |
| [SRC-6BF96689A8-L000136](../../tests/test_research.py#L136) | 136 | `""` | — |
| [SRC-6BF96689A8-L000137](../../tests/test_research.py#L137) | 137 | `"def test_fallback_plan_does_not_reuse_topic_after_acknowledgment():"` | — |
| [SRC-6BF96689A8-L000138](../../tests/test_research.py#L138) | 138 | `"    history = ["` | — |
| [SRC-6BF96689A8-L000139](../../tests/test_research.py#L139) | 139 | `"        {\"role\": \"user\", \"content\": \"سعر آيفون 16 في مصر\"},"` | — |
| [SRC-6BF96689A8-L000140](../../tests/test_research.py#L140) | 140 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن معلومات حديثة.\"},"` | — |
| [SRC-6BF96689A8-L000141](../../tests/test_research.py#L141) | 141 | `"        {\"role\": \"user\", \"content\": \"شكرًا\"},"` | — |
| [SRC-6BF96689A8-L000142](../../tests/test_research.py#L142) | 142 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-6BF96689A8-L000143](../../tests/test_research.py#L143) | 143 | `"    ]"` | — |
| [SRC-6BF96689A8-L000144](../../tests/test_research.py#L144) | 144 | `"    plan = fallback_plan(\"فين؟\", history)"` | — |
| [SRC-6BF96689A8-L000145](../../tests/test_research.py#L145) | 145 | `"    assert \"آيفون 16\" not in plan[\"queries\"][0]"` | — |
## اختبارات

### FILE-01E35ABC46 — [tests/test_research_guardrails.py](../../tests/test_research_guardrails.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-01E35ABC46-L000001](../../tests/test_research_guardrails.py#L1) | 1 | `"\"\"\"Regression and adversarial tests for depth, freshness, relevance, evidence.\"\"\""` | — |
| [SRC-01E35ABC46-L000002](../../tests/test_research_guardrails.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-01E35ABC46-L000003](../../tests/test_research_guardrails.py#L3) | 3 | `""` | — |
| [SRC-01E35ABC46-L000004](../../tests/test_research_guardrails.py#L4) | 4 | `"from agents.research import ("` | — |
| [SRC-01E35ABC46-L000005](../../tests/test_research_guardrails.py#L5) | 5 | `"    decide_evidence_status,"` | — |
| [SRC-01E35ABC46-L000006](../../tests/test_research_guardrails.py#L6) | 6 | `"    detect_depth,"` | — |
| [SRC-01E35ABC46-L000007](../../tests/test_research_guardrails.py#L7) | 7 | `"    detect_freshness,"` | — |
| [SRC-01E35ABC46-L000008](../../tests/test_research_guardrails.py#L8) | 8 | `"    filter_relevant_sources,"` | — |
| [SRC-01E35ABC46-L000009](../../tests/test_research_guardrails.py#L9) | 9 | `"    source_relevance_score,"` | — |
| [SRC-01E35ABC46-L000010](../../tests/test_research_guardrails.py#L10) | 10 | `")"` | — |
| [SRC-01E35ABC46-L000011](../../tests/test_research_guardrails.py#L11) | 11 | `""` | — |
| [SRC-01E35ABC46-L000012](../../tests/test_research_guardrails.py#L12) | 12 | `""` | — |
| [SRC-01E35ABC46-L000013](../../tests/test_research_guardrails.py#L13) | 13 | `"# --- detect_depth -----------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000014](../../tests/test_research_guardrails.py#L14) | 14 | `""` | — |
| [SRC-01E35ABC46-L000015](../../tests/test_research_guardrails.py#L15) | 15 | `"def test_depth_deep_english_phrases():"` | — |
| [SRC-01E35ABC46-L000016](../../tests/test_research_guardrails.py#L16) | 16 | `"    assert detect_depth(\"Please do a deep research on climate policy\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000017](../../tests/test_research_guardrails.py#L17) | 17 | `"    assert detect_depth(\"in-depth comparison of EV batteries\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000018](../../tests/test_research_guardrails.py#L18) | 18 | `"    assert detect_depth(\"comprehensive analysis of market risks\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000019](../../tests/test_research_guardrails.py#L19) | 19 | `""` | — |
| [SRC-01E35ABC46-L000020](../../tests/test_research_guardrails.py#L20) | 20 | `""` | — |
| [SRC-01E35ABC46-L000021](../../tests/test_research_guardrails.py#L21) | 21 | `"def test_depth_deep_arabic_phrases():"` | — |
| [SRC-01E35ABC46-L000022](../../tests/test_research_guardrails.py#L22) | 22 | `"    assert detect_depth(\"أريد بحث عميق عن الذكاء الاصطناعي\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000023](../../tests/test_research_guardrails.py#L23) | 23 | `"    assert detect_depth(\"قارن بين السيارات الكهربائية والبنزين\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000024](../../tests/test_research_guardrails.py#L24) | 24 | `"    assert detect_depth(\"بحث شامل بالتفصيل عن الذهب\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000025](../../tests/test_research_guardrails.py#L25) | 25 | `""` | — |
| [SRC-01E35ABC46-L000026](../../tests/test_research_guardrails.py#L26) | 26 | `""` | — |
| [SRC-01E35ABC46-L000027](../../tests/test_research_guardrails.py#L27) | 27 | `"def test_depth_standard_ordinary_questions():"` | — |
| [SRC-01E35ABC46-L000028](../../tests/test_research_guardrails.py#L28) | 28 | `"    assert detect_depth(\"what is the capital of France\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000029](../../tests/test_research_guardrails.py#L29) | 29 | `"    assert detect_depth(\"ما عاصمة مصر\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000030](../../tests/test_research_guardrails.py#L30) | 30 | `"    assert detect_depth(\"I know about electric cars\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000031](../../tests/test_research_guardrails.py#L31) | 31 | `"    assert detect_depth(\"hello\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000032](../../tests/test_research_guardrails.py#L32) | 32 | `"    assert detect_depth(\"\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000033](../../tests/test_research_guardrails.py#L33) | 33 | `""` | — |
| [SRC-01E35ABC46-L000034](../../tests/test_research_guardrails.py#L34) | 34 | `""` | — |
| [SRC-01E35ABC46-L000035](../../tests/test_research_guardrails.py#L35) | 35 | `"def test_depth_does_not_trigger_on_partial_words():"` | — |
| [SRC-01E35ABC46-L000036](../../tests/test_research_guardrails.py#L36) | 36 | `"    # \"sources\" is a deep term; ensure isolated ordinary use still works via whole-word"` | — |
| [SRC-01E35ABC46-L000037](../../tests/test_research_guardrails.py#L37) | 37 | `"    assert detect_depth(\"the river sources of the Nile\") in {\"deep\", \"standard\"}  # may match"` | — |
| [SRC-01E35ABC46-L000038](../../tests/test_research_guardrails.py#L38) | 38 | `"    assert detect_depth(\"tell me a joke\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000039](../../tests/test_research_guardrails.py#L39) | 39 | `""` | — |
| [SRC-01E35ABC46-L000040](../../tests/test_research_guardrails.py#L40) | 40 | `""` | — |
| [SRC-01E35ABC46-L000041](../../tests/test_research_guardrails.py#L41) | 41 | `"# --- detect_freshness -------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000042](../../tests/test_research_guardrails.py#L42) | 42 | `""` | — |
| [SRC-01E35ABC46-L000043](../../tests/test_research_guardrails.py#L43) | 43 | `"def test_freshness_positive_english():"` | — |
| [SRC-01E35ABC46-L000044](../../tests/test_research_guardrails.py#L44) | 44 | `"    assert detect_freshness(\"what is happening now\") is True"` | — |
| [SRC-01E35ABC46-L000045](../../tests/test_research_guardrails.py#L45) | 45 | `"    assert detect_freshness(\"latest news about Egypt\") is True"` | — |
| [SRC-01E35ABC46-L000046](../../tests/test_research_guardrails.py#L46) | 46 | `"    assert detect_freshness(\"price today of gold\") is True"` | — |
| [SRC-01E35ABC46-L000047](../../tests/test_research_guardrails.py#L47) | 47 | `"    assert detect_freshness(\"breaking news\") is True"` | — |
| [SRC-01E35ABC46-L000048](../../tests/test_research_guardrails.py#L48) | 48 | `""` | — |
| [SRC-01E35ABC46-L000049](../../tests/test_research_guardrails.py#L49) | 49 | `""` | — |
| [SRC-01E35ABC46-L000050](../../tests/test_research_guardrails.py#L50) | 50 | `"def test_freshness_positive_arabic():"` | — |
| [SRC-01E35ABC46-L000051](../../tests/test_research_guardrails.py#L51) | 51 | `"    assert detect_freshness(\"ما هي آخر الأخبار عن الذهب\") is True"` | — |
| [SRC-01E35ABC46-L000052](../../tests/test_research_guardrails.py#L52) | 52 | `"    assert detect_freshness(\"سعر اليوم للدولار\") is True"` | — |
| [SRC-01E35ABC46-L000053](../../tests/test_research_guardrails.py#L53) | 53 | `"    assert detect_freshness(\"مستجدات السوق حاليا\") is True"` | — |
| [SRC-01E35ABC46-L000054](../../tests/test_research_guardrails.py#L54) | 54 | `""` | — |
| [SRC-01E35ABC46-L000055](../../tests/test_research_guardrails.py#L55) | 55 | `""` | — |
| [SRC-01E35ABC46-L000056](../../tests/test_research_guardrails.py#L56) | 56 | `"def test_freshness_negative_know_and_snowden():"` | — |
| [SRC-01E35ABC46-L000057](../../tests/test_research_guardrails.py#L57) | 57 | `"    assert detect_freshness(\"I know about cars\") is False"` | — |
| [SRC-01E35ABC46-L000058](../../tests/test_research_guardrails.py#L58) | 58 | `"    assert detect_freshness(\"Snowden revelations summary\") is False"` | — |
| [SRC-01E35ABC46-L000059](../../tests/test_research_guardrails.py#L59) | 59 | `"    assert detect_freshness(\"knowledge graph basics\") is False"` | — |
| [SRC-01E35ABC46-L000060](../../tests/test_research_guardrails.py#L60) | 60 | `"    assert detect_freshness(\"ما عاصمة فرنسا\") is False"` | — |
| [SRC-01E35ABC46-L000061](../../tests/test_research_guardrails.py#L61) | 61 | `""` | — |
| [SRC-01E35ABC46-L000062](../../tests/test_research_guardrails.py#L62) | 62 | `""` | — |
| [SRC-01E35ABC46-L000063](../../tests/test_research_guardrails.py#L63) | 63 | `"# --- relevance gate ---------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000064](../../tests/test_research_guardrails.py#L64) | 64 | `""` | — |
| [SRC-01E35ABC46-L000065](../../tests/test_research_guardrails.py#L65) | 65 | `"def test_relevance_keeps_matching_source():"` | — |
| [SRC-01E35ABC46-L000066](../../tests/test_research_guardrails.py#L66) | 66 | `"    src = {"` | — |
| [SRC-01E35ABC46-L000067](../../tests/test_research_guardrails.py#L67) | 67 | `"        \"title\": \"أسعار السيارات الكهربائية في مصر 2026\","` | — |
| [SRC-01E35ABC46-L000068](../../tests/test_research_guardrails.py#L68) | 68 | `"        \"url\": \"https://example.com/ev-egypt\","` | — |
| [SRC-01E35ABC46-L000069](../../tests/test_research_guardrails.py#L69) | 69 | `"        \"snippet\": \"ارتفعت حصة السيارات الكهربائية في السوق المصري هذا العام.\","` | — |
| [SRC-01E35ABC46-L000070](../../tests/test_research_guardrails.py#L70) | 70 | `"        \"domain\": \"example.com\","` | — |
| [SRC-01E35ABC46-L000071](../../tests/test_research_guardrails.py#L71) | 71 | `"        \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000072](../../tests/test_research_guardrails.py#L72) | 72 | `"        \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000073](../../tests/test_research_guardrails.py#L73) | 73 | `"    }"` | — |
| [SRC-01E35ABC46-L000074](../../tests/test_research_guardrails.py#L74) | 74 | `"    rel = source_relevance_score(src, \"أسعار السيارات الكهربائية في مصر\")"` | — |
| [SRC-01E35ABC46-L000075](../../tests/test_research_guardrails.py#L75) | 75 | `"    assert rel[\"accepted\"] is True"` | — |
| [SRC-01E35ABC46-L000076](../../tests/test_research_guardrails.py#L76) | 76 | `"    assert rel[\"score\"] >= 18"` | — |
| [SRC-01E35ABC46-L000077](../../tests/test_research_guardrails.py#L77) | 77 | `""` | — |
| [SRC-01E35ABC46-L000078](../../tests/test_research_guardrails.py#L78) | 78 | `"    # English-English match"` | — |
| [SRC-01E35ABC46-L000079](../../tests/test_research_guardrails.py#L79) | 79 | `"    src_en = {"` | — |
| [SRC-01E35ABC46-L000080](../../tests/test_research_guardrails.py#L80) | 80 | `"        \"title\": \"Electric vehicles in Egypt 2026\","` | — |
| [SRC-01E35ABC46-L000081](../../tests/test_research_guardrails.py#L81) | 81 | `"        \"url\": \"https://example.com/ev-egypt-en\","` | — |
| [SRC-01E35ABC46-L000082](../../tests/test_research_guardrails.py#L82) | 82 | `"        \"snippet\": \"Market share of electric cars in Egypt rose this year.\","` | — |
| [SRC-01E35ABC46-L000083](../../tests/test_research_guardrails.py#L83) | 83 | `"        \"domain\": \"example.com\","` | — |
| [SRC-01E35ABC46-L000084](../../tests/test_research_guardrails.py#L84) | 84 | `"        \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000085](../../tests/test_research_guardrails.py#L85) | 85 | `"        \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000086](../../tests/test_research_guardrails.py#L86) | 86 | `"    }"` | — |
| [SRC-01E35ABC46-L000087](../../tests/test_research_guardrails.py#L87) | 87 | `"    rel_en = source_relevance_score(src_en, \"electric vehicles Egypt market share\")"` | — |
| [SRC-01E35ABC46-L000088](../../tests/test_research_guardrails.py#L88) | 88 | `"    assert rel_en[\"accepted\"] is True"` | — |
| [SRC-01E35ABC46-L000089](../../tests/test_research_guardrails.py#L89) | 89 | `""` | — |
| [SRC-01E35ABC46-L000090](../../tests/test_research_guardrails.py#L90) | 90 | `""` | — |
| [SRC-01E35ABC46-L000091](../../tests/test_research_guardrails.py#L91) | 91 | `"def test_relevance_rejects_unrelated():"` | — |
| [SRC-01E35ABC46-L000092](../../tests/test_research_guardrails.py#L92) | 92 | `"    src = {"` | — |
| [SRC-01E35ABC46-L000093](../../tests/test_research_guardrails.py#L93) | 93 | `"        \"title\": \"Best pasta recipes\","` | — |
| [SRC-01E35ABC46-L000094](../../tests/test_research_guardrails.py#L94) | 94 | `"        \"url\": \"https://cooking.example/pasta\","` | — |
| [SRC-01E35ABC46-L000095](../../tests/test_research_guardrails.py#L95) | 95 | `"        \"snippet\": \"How to make carbonara at home with eggs and cheese.\","` | — |
| [SRC-01E35ABC46-L000096](../../tests/test_research_guardrails.py#L96) | 96 | `"        \"domain\": \"cooking.example\","` | — |
| [SRC-01E35ABC46-L000097](../../tests/test_research_guardrails.py#L97) | 97 | `"        \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000098](../../tests/test_research_guardrails.py#L98) | 98 | `"        \"providers\": [\"bing\"],"` | — |
| [SRC-01E35ABC46-L000099](../../tests/test_research_guardrails.py#L99) | 99 | `"    }"` | — |
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
