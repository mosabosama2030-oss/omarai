# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **046**
- سجلات الأسطر: **800**
- النطاق: SRC-6BECF5AD00-L000018 إلى SRC-DA139AC9D0-L000063
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-6BECF5AD00 — [tests/test_connectors_mocked.py](../../tests/test_connectors_mocked.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-29A9CD43D1-L000040](../../tests/test_dialogue_context_pipeline.py#L40) | 40 | `"        \"providers_used\": [\"test_search\"],"` | — |
| [SRC-29A9CD43D1-L000041](../../tests/test_dialogue_context_pipeline.py#L41) | 41 | `"        \"provider_counts\": {\"test_search\": len(sources)},"` | — |
| [SRC-29A9CD43D1-L000042](../../tests/test_dialogue_context_pipeline.py#L42) | 42 | `"        \"platform_counts\": {\"web\": len(sources)},"` | — |
| [SRC-29A9CD43D1-L000043](../../tests/test_dialogue_context_pipeline.py#L43) | 43 | `"        \"social_direct_results\": 0,"` | — |
| [SRC-29A9CD43D1-L000044](../../tests/test_dialogue_context_pipeline.py#L44) | 44 | `"        \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-29A9CD43D1-L000045](../../tests/test_dialogue_context_pipeline.py#L45) | 45 | `"        \"planning_method\": plan.get(\"planning_method\", \"test\"),"` | — |
| [SRC-29A9CD43D1-L000046](../../tests/test_dialogue_context_pipeline.py#L46) | 46 | `"        \"evidence_signals\": evidence_signal_report(sources),"` | — |
| [SRC-29A9CD43D1-L000047](../../tests/test_dialogue_context_pipeline.py#L47) | 47 | `"    }"` | — |
| [SRC-29A9CD43D1-L000048](../../tests/test_dialogue_context_pipeline.py#L48) | 48 | `""` | — |
| [SRC-29A9CD43D1-L000049](../../tests/test_dialogue_context_pipeline.py#L49) | 49 | `""` | — |
| [SRC-29A9CD43D1-L000050](../../tests/test_dialogue_context_pipeline.py#L50) | 50 | `"def _semantic_context(*, needs_clarification: bool = False) -> dict[str, Any]:"` | — |
| [SRC-29A9CD43D1-L000051](../../tests/test_dialogue_context_pipeline.py#L51) | 51 | `"    return {"` | — |
| [SRC-29A9CD43D1-L000052](../../tests/test_dialogue_context_pipeline.py#L52) | 52 | `"        \"resolved_question\": ("` | — |
| [SRC-29A9CD43D1-L000053](../../tests/test_dialogue_context_pipeline.py#L53) | 53 | `"            \"هل الضمان الدولي لهاتف iPhone 17 سعة 256 جيجابايت الذي اشتريته \""` | — |
| [SRC-29A9CD43D1-L000054](../../tests/test_dialogue_context_pipeline.py#L54) | 54 | `"            \"في مصر يغطي الصيانة داخل مصر؟\""` | — |
| [SRC-29A9CD43D1-L000055](../../tests/test_dialogue_context_pipeline.py#L55) | 55 | `"        ),"` | — |
| [SRC-29A9CD43D1-L000056](../../tests/test_dialogue_context_pipeline.py#L56) | 56 | `"        \"intent\": \"current_information\","` | — |
| [SRC-29A9CD43D1-L000057](../../tests/test_dialogue_context_pipeline.py#L57) | 57 | `"        \"topic\": \"تغطية الضمان\","` | — |
| [SRC-29A9CD43D1-L000058](../../tests/test_dialogue_context_pipeline.py#L58) | 58 | `"        \"entities\": [\"iPhone 17\"],"` | — |
| [SRC-29A9CD43D1-L000059](../../tests/test_dialogue_context_pipeline.py#L59) | 59 | `"        \"slots\": {"` | — |
| [SRC-29A9CD43D1-L000060](../../tests/test_dialogue_context_pipeline.py#L60) | 60 | `"            \"product\": \"iPhone 17\","` | — |
| [SRC-29A9CD43D1-L000061](../../tests/test_dialogue_context_pipeline.py#L61) | 61 | `"            \"capacity\": \"256 جيجابايت\","` | — |
| [SRC-29A9CD43D1-L000062](../../tests/test_dialogue_context_pipeline.py#L62) | 62 | `"            \"country\": \"مصر\","` | — |
| [SRC-29A9CD43D1-L000063](../../tests/test_dialogue_context_pipeline.py#L63) | 63 | `"            \"aspect\": \"الضمان الدولي والصيانة داخل مصر\","` | — |
| [SRC-29A9CD43D1-L000064](../../tests/test_dialogue_context_pipeline.py#L64) | 64 | `"        },"` | — |
| [SRC-29A9CD43D1-L000065](../../tests/test_dialogue_context_pipeline.py#L65) | 65 | `"        \"changed_slots\": [\"aspect\"],"` | — |
| [SRC-29A9CD43D1-L000066](../../tests/test_dialogue_context_pipeline.py#L66) | 66 | `"        \"is_follow_up\": True,"` | — |
| [SRC-29A9CD43D1-L000067](../../tests/test_dialogue_context_pipeline.py#L67) | 67 | `"        \"topic_shift\": False,"` | — |
| [SRC-29A9CD43D1-L000068](../../tests/test_dialogue_context_pipeline.py#L68) | 68 | `"        \"needs_web\": True,"` | — |
| [SRC-29A9CD43D1-L000069](../../tests/test_dialogue_context_pipeline.py#L69) | 69 | `"        \"research_depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000070](../../tests/test_dialogue_context_pipeline.py#L70) | 70 | `"        \"needs_clarification\": needs_clarification,"` | — |
| [SRC-29A9CD43D1-L000071](../../tests/test_dialogue_context_pipeline.py#L71) | 71 | `"        \"clarification_question\": ("` | — |
| [SRC-29A9CD43D1-L000072](../../tests/test_dialogue_context_pipeline.py#L72) | 72 | `"            \"تقصد ضمان أي هاتف تحديدًا، أم تريد مقارنة ضمان الهاتفين؟\""` | — |
| [SRC-29A9CD43D1-L000073](../../tests/test_dialogue_context_pipeline.py#L73) | 73 | `"            if needs_clarification else \"\""` | — |
| [SRC-29A9CD43D1-L000074](../../tests/test_dialogue_context_pipeline.py#L74) | 74 | `"        ),"` | — |
| [SRC-29A9CD43D1-L000075](../../tests/test_dialogue_context_pipeline.py#L75) | 75 | `"        \"unresolved_references\": [\"الضمان\"] if needs_clarification else [],"` | — |
| [SRC-29A9CD43D1-L000076](../../tests/test_dialogue_context_pipeline.py#L76) | 76 | `"        \"resolution_basis\": \"history_inferred\","` | — |
| [SRC-29A9CD43D1-L000077](../../tests/test_dialogue_context_pipeline.py#L77) | 77 | `"        \"confidence_band\": \"medium\","` | — |
| [SRC-29A9CD43D1-L000078](../../tests/test_dialogue_context_pipeline.py#L78) | 78 | `"    }"` | — |
| [SRC-29A9CD43D1-L000079](../../tests/test_dialogue_context_pipeline.py#L79) | 79 | `""` | — |
| [SRC-29A9CD43D1-L000080](../../tests/test_dialogue_context_pipeline.py#L80) | 80 | `""` | — |
| [SRC-29A9CD43D1-L000081](../../tests/test_dialogue_context_pipeline.py#L81) | 81 | `"def test_semantic_context_probe_routes_natural_followup_to_search_and_answer("` | — |
| [SRC-29A9CD43D1-L000082](../../tests/test_dialogue_context_pipeline.py#L82) | 82 | `"    monkeypatch: pytest.MonkeyPatch,"` | — |
| [SRC-29A9CD43D1-L000083](../../tests/test_dialogue_context_pipeline.py#L83) | 83 | `") -> None:"` | — |
| [SRC-29A9CD43D1-L000084](../../tests/test_dialogue_context_pipeline.py#L84) | 84 | `"    agent = WebAgent()"` | — |
| [SRC-29A9CD43D1-L000085](../../tests/test_dialogue_context_pipeline.py#L85) | 85 | `"    agent.api_key = \"test-key\"  # All model responses are mocked; no provider call is made."` | — |
| [SRC-29A9CD43D1-L000086](../../tests/test_dialogue_context_pipeline.py#L86) | 86 | `"    history = ["` | — |
| [SRC-29A9CD43D1-L000087](../../tests/test_dialogue_context_pipeline.py#L87) | 87 | `"        {\"role\": \"user\", \"content\": \"اشتريت iPhone 17 النسخة الأساسية سعة 256 جيجابايت من مصر.\"},"` | — |
| [SRC-29A9CD43D1-L000088](../../tests/test_dialogue_context_pipeline.py#L88) | 88 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن نسخة iPhone 17 سعة 256 جيجابايت في مصر.\"},"` | — |
| [SRC-29A9CD43D1-L000089](../../tests/test_dialogue_context_pipeline.py#L89) | 89 | `"    ]"` | — |
| [SRC-29A9CD43D1-L000090](../../tests/test_dialogue_context_pipeline.py#L90) | 90 | `"    context = _semantic_context()"` | — |
| [SRC-29A9CD43D1-L000091](../../tests/test_dialogue_context_pipeline.py#L91) | 91 | `"    seen: dict[str, Any] = {\"model_prompts\": []}"` | — |
| [SRC-29A9CD43D1-L000092](../../tests/test_dialogue_context_pipeline.py#L92) | 92 | `""` | — |
| [SRC-29A9CD43D1-L000093](../../tests/test_dialogue_context_pipeline.py#L93) | 93 | `"    def mocked_completion(messages, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000094](../../tests/test_dialogue_context_pipeline.py#L94) | 94 | `"        system_prompt = messages[0][\"content\"]"` | — |
| [SRC-29A9CD43D1-L000095](../../tests/test_dialogue_context_pipeline.py#L95) | 95 | `"        seen[\"model_prompts\"].append(system_prompt)"` | — |
| [SRC-29A9CD43D1-L000096](../../tests/test_dialogue_context_pipeline.py#L96) | 96 | `"        if \"أنت محلل سياق حواري\" in system_prompt:"` | — |
| [SRC-29A9CD43D1-L000097](../../tests/test_dialogue_context_pipeline.py#L97) | 97 | `"            assert \"تعامل معها كتصحيح للكيان/قيمة القيد\" in system_prompt"` | — |
| [SRC-29A9CD43D1-L000098](../../tests/test_dialogue_context_pipeline.py#L98) | 98 | `"            assert \"سجّل اسم القيد المعدل في changed_slots\" in system_prompt"` | — |
| [SRC-29A9CD43D1-L000099](../../tests/test_dialogue_context_pipeline.py#L99) | 99 | `"            return json.dumps(context, ensure_ascii=False)"` | — |
| [SRC-29A9CD43D1-L000100](../../tests/test_dialogue_context_pipeline.py#L100) | 100 | `"        if \"أنت مخطط بحث ومحلل دلالي حواري\" in system_prompt:"` | — |
| [SRC-29A9CD43D1-L000101](../../tests/test_dialogue_context_pipeline.py#L101) | 101 | `"            return json.dumps("` | — |
| [SRC-29A9CD43D1-L000102](../../tests/test_dialogue_context_pipeline.py#L102) | 102 | `"                {"` | — |
| [SRC-29A9CD43D1-L000103](../../tests/test_dialogue_context_pipeline.py#L103) | 103 | `"                    \"queries\": ["` | — |
| [SRC-29A9CD43D1-L000104](../../tests/test_dialogue_context_pipeline.py#L104) | 104 | `"                        \"iPhone 17 256GB الضمان الدولي في مصر تغطية الصيانة warranty Egypt\""` | — |
| [SRC-29A9CD43D1-L000105](../../tests/test_dialogue_context_pipeline.py#L105) | 105 | `"                    ],"` | — |
| [SRC-29A9CD43D1-L000106](../../tests/test_dialogue_context_pipeline.py#L106) | 106 | `"                    \"direct_urls\": [],"` | — |
| [SRC-29A9CD43D1-L000107](../../tests/test_dialogue_context_pipeline.py#L107) | 107 | `"                    \"social_focus\": False,"` | — |
| [SRC-29A9CD43D1-L000108](../../tests/test_dialogue_context_pipeline.py#L108) | 108 | `"                    \"freshness\": \"current\","` | — |
| [SRC-29A9CD43D1-L000109](../../tests/test_dialogue_context_pipeline.py#L109) | 109 | `"                    \"depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000110](../../tests/test_dialogue_context_pipeline.py#L110) | 110 | `"                    \"platforms\": [],"` | — |
| [SRC-29A9CD43D1-L000111](../../tests/test_dialogue_context_pipeline.py#L111) | 111 | `"                    \"dialogue_context\": context,"` | — |
| [SRC-29A9CD43D1-L000112](../../tests/test_dialogue_context_pipeline.py#L112) | 112 | `"                },"` | — |
| [SRC-29A9CD43D1-L000113](../../tests/test_dialogue_context_pipeline.py#L113) | 113 | `"                ensure_ascii=False,"` | — |
| [SRC-29A9CD43D1-L000114](../../tests/test_dialogue_context_pipeline.py#L114) | 114 | `"            )"` | — |
| [SRC-29A9CD43D1-L000115](../../tests/test_dialogue_context_pipeline.py#L115) | 115 | `"        pytest.fail(\"Unexpected model prompt in mocked offline test\")"` | — |
| [SRC-29A9CD43D1-L000116](../../tests/test_dialogue_context_pipeline.py#L116) | 116 | `""` | — |
| [SRC-29A9CD43D1-L000117](../../tests/test_dialogue_context_pipeline.py#L117) | 117 | `"    monkeypatch.setattr(agent, \"_request_completion\", mocked_completion)"` | — |
| [SRC-29A9CD43D1-L000118](../../tests/test_dialogue_context_pipeline.py#L118) | 118 | `"    seen[\"generated_question\"] = None"` | — |
| [SRC-29A9CD43D1-L000119](../../tests/test_dialogue_context_pipeline.py#L119) | 119 | `"    seen[\"reviewed_question\"] = None"` | — |
| [SRC-29A9CD43D1-L000120](../../tests/test_dialogue_context_pipeline.py#L120) | 120 | `""` | — |
| [SRC-29A9CD43D1-L000121](../../tests/test_dialogue_context_pipeline.py#L121) | 121 | `"    def collect(plan):"` | — |
| [SRC-29A9CD43D1-L000122](../../tests/test_dialogue_context_pipeline.py#L122) | 122 | `"        seen[\"plan\"] = dict(plan)"` | — |
| [SRC-29A9CD43D1-L000123](../../tests/test_dialogue_context_pipeline.py#L123) | 123 | `"        sources = [_source(\"example.com\", plan[\"queries\"]), _source(\"example.net\", plan[\"queries\"])]"` | — |
| [SRC-29A9CD43D1-L000124](../../tests/test_dialogue_context_pipeline.py#L124) | 124 | `"        return sources, [], _report(plan, sources)"` | — |
| [SRC-29A9CD43D1-L000125](../../tests/test_dialogue_context_pipeline.py#L125) | 125 | `""` | — |
| [SRC-29A9CD43D1-L000126](../../tests/test_dialogue_context_pipeline.py#L126) | 126 | `"    def generate(resolved_question, *args, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000127](../../tests/test_dialogue_context_pipeline.py#L127) | 127 | `"        seen[\"generated_question\"] = resolved_question"` | — |
| [SRC-29A9CD43D1-L000128](../../tests/test_dialogue_context_pipeline.py#L128) | 128 | `"        return \"لم أؤكد شروط الضمان من النصوص المتاحة؛ راجع الشروط الرسمية [المصدر 1].\""` | — |
| [SRC-29A9CD43D1-L000129](../../tests/test_dialogue_context_pipeline.py#L129) | 129 | `""` | — |
| [SRC-29A9CD43D1-L000130](../../tests/test_dialogue_context_pipeline.py#L130) | 130 | `"    def review(resolved_question, answer, sources):"` | — |
| [SRC-29A9CD43D1-L000131](../../tests/test_dialogue_context_pipeline.py#L131) | 131 | `"        seen[\"reviewed_question\"] = resolved_question"` | — |
| [SRC-29A9CD43D1-L000132](../../tests/test_dialogue_context_pipeline.py#L132) | 132 | `"        return answer"` | — |
| [SRC-29A9CD43D1-L000133](../../tests/test_dialogue_context_pipeline.py#L133) | 133 | `""` | — |
| [SRC-29A9CD43D1-L000134](../../tests/test_dialogue_context_pipeline.py#L134) | 134 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-29A9CD43D1-L000135](../../tests/test_dialogue_context_pipeline.py#L135) | 135 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda _query, _source: True)"` | — |
| [SRC-29A9CD43D1-L000136](../../tests/test_dialogue_context_pipeline.py#L136) | 136 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-29A9CD43D1-L000137](../../tests/test_dialogue_context_pipeline.py#L137) | 137 | `"    monkeypatch.setattr(agent, \"_review_answer\", review)"` | — |
| [SRC-29A9CD43D1-L000138](../../tests/test_dialogue_context_pipeline.py#L138) | 138 | `"    monkeypatch.setattr(agent, \"_verify_semantic_claims\", lambda *args, **kwargs: {"` | — |
| [SRC-29A9CD43D1-L000139](../../tests/test_dialogue_context_pipeline.py#L139) | 139 | `"        \"status\": \"completed_all_claims_supported\","` | — |
| [SRC-29A9CD43D1-L000140](../../tests/test_dialogue_context_pipeline.py#L140) | 140 | `"        \"withhold_answer\": False,"` | — |
| [SRC-29A9CD43D1-L000141](../../tests/test_dialogue_context_pipeline.py#L141) | 141 | `"        \"semantic_verification\": \"model_assessed_source_support\","` | — |
| [SRC-29A9CD43D1-L000142](../../tests/test_dialogue_context_pipeline.py#L142) | 142 | `"        \"fact_correctness\": \"not_verified\","` | — |
| [SRC-29A9CD43D1-L000143](../../tests/test_dialogue_context_pipeline.py#L143) | 143 | `"    })"` | — |
| [SRC-29A9CD43D1-L000144](../../tests/test_dialogue_context_pipeline.py#L144) | 144 | `""` | — |
| [SRC-29A9CD43D1-L000145](../../tests/test_dialogue_context_pipeline.py#L145) | 145 | `"    question = \"وطب الضمان الدولي بيسري في مصر؟\""` | — |
| [SRC-29A9CD43D1-L000146](../../tests/test_dialogue_context_pipeline.py#L146) | 146 | `"    result = agent.answer(question, history=history)"` | — |
| [SRC-29A9CD43D1-L000147](../../tests/test_dialogue_context_pipeline.py#L147) | 147 | `""` | — |
| [SRC-29A9CD43D1-L000148](../../tests/test_dialogue_context_pipeline.py#L148) | 148 | `"    assert result[\"intent_route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-29A9CD43D1-L000149](../../tests/test_dialogue_context_pipeline.py#L149) | 149 | `"    assert result[\"question\"] == question  # Preserve the visible user utterance."` | — |
| [SRC-29A9CD43D1-L000150](../../tests/test_dialogue_context_pipeline.py#L150) | 150 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-29A9CD43D1-L000151](../../tests/test_dialogue_context_pipeline.py#L151) | 151 | `"    assert len(seen[\"model_prompts\"]) == 2  # one context pass + one search-plan pass"` | — |
| [SRC-29A9CD43D1-L000152](../../tests/test_dialogue_context_pipeline.py#L152) | 152 | `"    assert \"iPhone 17\" in seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000153](../../tests/test_dialogue_context_pipeline.py#L153) | 153 | `"    assert \"256 جيجابايت\" in seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000154](../../tests/test_dialogue_context_pipeline.py#L154) | 154 | `"    assert \"الضمان الدولي\" in seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000155](../../tests/test_dialogue_context_pipeline.py#L155) | 155 | `"    assert seen[\"reviewed_question\"] == seen[\"generated_question\"]"` | — |
| [SRC-29A9CD43D1-L000156](../../tests/test_dialogue_context_pipeline.py#L156) | 156 | `"    context_result = result[\"research_plan\"][\"dialogue_context\"]"` | — |
| [SRC-29A9CD43D1-L000157](../../tests/test_dialogue_context_pipeline.py#L157) | 157 | `"    assert context_result[\"method\"] == \"llm_semantic_context\""` | — |
| [SRC-29A9CD43D1-L000158](../../tests/test_dialogue_context_pipeline.py#L158) | 158 | `"    assert context_result[\"slots\"][\"country\"] == \"مصر\""` | — |
| [SRC-29A9CD43D1-L000159](../../tests/test_dialogue_context_pipeline.py#L159) | 159 | `"    assert context_result[\"changed_slots\"] == [\"aspect\"]"` | — |
| [SRC-29A9CD43D1-L000160](../../tests/test_dialogue_context_pipeline.py#L160) | 160 | `"    assert context_result[\"needs_web\"] is True"` | — |
| [SRC-29A9CD43D1-L000161](../../tests/test_dialogue_context_pipeline.py#L161) | 161 | `""` | — |
| [SRC-29A9CD43D1-L000162](../../tests/test_dialogue_context_pipeline.py#L162) | 162 | `""` | — |
| [SRC-29A9CD43D1-L000163](../../tests/test_dialogue_context_pipeline.py#L163) | 163 | `"def test_semantic_context_asks_before_search_when_two_referents_are_plausible("` | — |
| [SRC-29A9CD43D1-L000164](../../tests/test_dialogue_context_pipeline.py#L164) | 164 | `"    monkeypatch: pytest.MonkeyPatch,"` | — |
| [SRC-29A9CD43D1-L000165](../../tests/test_dialogue_context_pipeline.py#L165) | 165 | `") -> None:"` | — |
| [SRC-29A9CD43D1-L000166](../../tests/test_dialogue_context_pipeline.py#L166) | 166 | `"    agent = WebAgent()"` | — |
| [SRC-29A9CD43D1-L000167](../../tests/test_dialogue_context_pipeline.py#L167) | 167 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-29A9CD43D1-L000168](../../tests/test_dialogue_context_pipeline.py#L168) | 168 | `"    history = ["` | — |
| [SRC-29A9CD43D1-L000169](../../tests/test_dialogue_context_pipeline.py#L169) | 169 | `"        {\"role\": \"user\", \"content\": \"قارن بين iPhone 17 وSamsung S26\"},"` | — |
| [SRC-29A9CD43D1-L000170](../../tests/test_dialogue_context_pipeline.py#L170) | 170 | `"        {\"role\": \"assistant\", \"content\": \"ذكرت الهاتفين في المقارنة.\"},"` | — |
| [SRC-29A9CD43D1-L000171](../../tests/test_dialogue_context_pipeline.py#L171) | 171 | `"    ]"` | — |
| [SRC-29A9CD43D1-L000172](../../tests/test_dialogue_context_pipeline.py#L172) | 172 | `"    ambiguous = {"` | — |
| [SRC-29A9CD43D1-L000173](../../tests/test_dialogue_context_pipeline.py#L173) | 173 | `"        \"resolved_question\": \"What about the second one?\","` | — |
| [SRC-29A9CD43D1-L000174](../../tests/test_dialogue_context_pipeline.py#L174) | 174 | `"        \"intent\": \"compare\","` | — |
| [SRC-29A9CD43D1-L000175](../../tests/test_dialogue_context_pipeline.py#L175) | 175 | `"        \"topic\": \"اختيار الهاتف\","` | — |
| [SRC-29A9CD43D1-L000176](../../tests/test_dialogue_context_pipeline.py#L176) | 176 | `"        \"entities\": [\"iPhone 17\", \"Samsung S26\"],"` | — |
| [SRC-29A9CD43D1-L000177](../../tests/test_dialogue_context_pipeline.py#L177) | 177 | `"        \"slots\": {\"aspect\": \"الاختيار\"},"` | — |
| [SRC-29A9CD43D1-L000178](../../tests/test_dialogue_context_pipeline.py#L178) | 178 | `"        \"changed_slots\": [],"` | — |
| [SRC-29A9CD43D1-L000179](../../tests/test_dialogue_context_pipeline.py#L179) | 179 | `"        \"is_follow_up\": True,"` | — |
| [SRC-29A9CD43D1-L000180](../../tests/test_dialogue_context_pipeline.py#L180) | 180 | `"        \"topic_shift\": False,"` | — |
| [SRC-29A9CD43D1-L000181](../../tests/test_dialogue_context_pipeline.py#L181) | 181 | `"        \"needs_web\": False,"` | — |
| [SRC-29A9CD43D1-L000182](../../tests/test_dialogue_context_pipeline.py#L182) | 182 | `"        \"research_depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000183](../../tests/test_dialogue_context_pipeline.py#L183) | 183 | `"        \"needs_clarification\": True,"` | — |
| [SRC-29A9CD43D1-L000184](../../tests/test_dialogue_context_pipeline.py#L184) | 184 | `"        \"clarification_question\": \"تقصد أي هاتف تحديدًا: iPhone 17 أم Samsung S26؟\","` | — |
| [SRC-29A9CD43D1-L000185](../../tests/test_dialogue_context_pipeline.py#L185) | 185 | `"        \"unresolved_references\": [\"the second one\"],"` | — |
| [SRC-29A9CD43D1-L000186](../../tests/test_dialogue_context_pipeline.py#L186) | 186 | `"        \"resolution_basis\": \"insufficient_evidence\","` | — |
| [SRC-29A9CD43D1-L000187](../../tests/test_dialogue_context_pipeline.py#L187) | 187 | `"        \"confidence_band\": \"low\","` | — |
| [SRC-29A9CD43D1-L000188](../../tests/test_dialogue_context_pipeline.py#L188) | 188 | `"    }"` | — |
| [SRC-29A9CD43D1-L000189](../../tests/test_dialogue_context_pipeline.py#L189) | 189 | `""` | — |
| [SRC-29A9CD43D1-L000190](../../tests/test_dialogue_context_pipeline.py#L190) | 190 | `"    def mocked_completion(messages, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000191](../../tests/test_dialogue_context_pipeline.py#L191) | 191 | `"        assert \"أنت محلل سياق حواري\" in messages[0][\"content\"]"` | — |
| [SRC-29A9CD43D1-L000192](../../tests/test_dialogue_context_pipeline.py#L192) | 192 | `"        return json.dumps(ambiguous, ensure_ascii=False)"` | — |
| [SRC-29A9CD43D1-L000193](../../tests/test_dialogue_context_pipeline.py#L193) | 193 | `""` | — |
| [SRC-29A9CD43D1-L000194](../../tests/test_dialogue_context_pipeline.py#L194) | 194 | `"    def forbidden_search(*args, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000195](../../tests/test_dialogue_context_pipeline.py#L195) | 195 | `"        pytest.fail(\"An unresolved referent must not start web research.\")"` | — |
| [SRC-29A9CD43D1-L000196](../../tests/test_dialogue_context_pipeline.py#L196) | 196 | `""` | — |
| [SRC-29A9CD43D1-L000197](../../tests/test_dialogue_context_pipeline.py#L197) | 197 | `"    monkeypatch.setattr(agent, \"_request_completion\", mocked_completion)"` | — |
| [SRC-29A9CD43D1-L000198](../../tests/test_dialogue_context_pipeline.py#L198) | 198 | `"    monkeypatch.setattr(agent, \"_collect_research\", forbidden_search)"` | — |
| [SRC-29A9CD43D1-L000199](../../tests/test_dialogue_context_pipeline.py#L199) | 199 | `""` | — |
| [SRC-29A9CD43D1-L000200](../../tests/test_dialogue_context_pipeline.py#L200) | 200 | `"    result = agent.answer(\"What about the second one?\", history=history)"` | — |
| [SRC-29A9CD43D1-L000201](../../tests/test_dialogue_context_pipeline.py#L201) | 201 | `""` | — |
| [SRC-29A9CD43D1-L000202](../../tests/test_dialogue_context_pipeline.py#L202) | 202 | `"    assert result[\"kind\"] == \"clarification_needed\""` | — |
| [SRC-29A9CD43D1-L000203](../../tests/test_dialogue_context_pipeline.py#L203) | 203 | `"    assert result[\"intent_route\"] == \"CLARIFY\""` | — |
| [SRC-29A9CD43D1-L000204](../../tests/test_dialogue_context_pipeline.py#L204) | 204 | `"    assert \"iPhone 17\" in result[\"answer\"]"` | — |
| [SRC-29A9CD43D1-L000205](../../tests/test_dialogue_context_pipeline.py#L205) | 205 | `"    assert \"Samsung S26\" in result[\"answer\"]"` | — |
| [SRC-29A9CD43D1-L000206](../../tests/test_dialogue_context_pipeline.py#L206) | 206 | `"    assert result[\"dialogue_context\"][\"needs_clarification\"] is True"` | — |
| [SRC-29A9CD43D1-L000207](../../tests/test_dialogue_context_pipeline.py#L207) | 207 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-29A9CD43D1-L000208](../../tests/test_dialogue_context_pipeline.py#L208) | 208 | `""` | — |
| [SRC-29A9CD43D1-L000209](../../tests/test_dialogue_context_pipeline.py#L209) | 209 | `"def test_semantic_probe_catches_implicit_context_without_keyword_trigger("` | — |
| [SRC-29A9CD43D1-L000210](../../tests/test_dialogue_context_pipeline.py#L210) | 210 | `"    monkeypatch: pytest.MonkeyPatch,"` | — |
| [SRC-29A9CD43D1-L000211](../../tests/test_dialogue_context_pipeline.py#L211) | 211 | `") -> None:"` | — |
| [SRC-29A9CD43D1-L000212](../../tests/test_dialogue_context_pipeline.py#L212) | 212 | `"    agent = WebAgent()"` | — |
| [SRC-29A9CD43D1-L000213](../../tests/test_dialogue_context_pipeline.py#L213) | 213 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-29A9CD43D1-L000214](../../tests/test_dialogue_context_pipeline.py#L214) | 214 | `"    question = \"في وضعي، أبدأ بإيه؟\""` | — |
| [SRC-29A9CD43D1-L000215](../../tests/test_dialogue_context_pipeline.py#L215) | 215 | `"    history = ["` | — |
| [SRC-29A9CD43D1-L000216](../../tests/test_dialogue_context_pipeline.py#L216) | 216 | `"        {"` | — |
| [SRC-29A9CD43D1-L000217](../../tests/test_dialogue_context_pipeline.py#L217) | 217 | `"            \"role\": \"user\","` | — |
| [SRC-29A9CD43D1-L000218](../../tests/test_dialogue_context_pipeline.py#L218) | 218 | `"            \"content\": ("` | — |
| [SRC-29A9CD43D1-L000219](../../tests/test_dialogue_context_pipeline.py#L219) | 219 | `"                \"عندي امتحان كيمياء بكرة، وفاضلي ساعتين أراجع الاتزان الكيميائي \""` | — |
| [SRC-29A9CD43D1-L000220](../../tests/test_dialogue_context_pipeline.py#L220) | 220 | `"                \"ومش فاهمه كويس.\""` | — |
| [SRC-29A9CD43D1-L000221](../../tests/test_dialogue_context_pipeline.py#L221) | 221 | `"            ),"` | — |
| [SRC-29A9CD43D1-L000222](../../tests/test_dialogue_context_pipeline.py#L222) | 222 | `"        },"` | — |
| [SRC-29A9CD43D1-L000223](../../tests/test_dialogue_context_pipeline.py#L223) | 223 | `"        {"` | — |
| [SRC-29A9CD43D1-L000224](../../tests/test_dialogue_context_pipeline.py#L224) | 224 | `"            \"role\": \"assistant\","` | — |
| [SRC-29A9CD43D1-L000225](../../tests/test_dialogue_context_pipeline.py#L225) | 225 | `"            \"content\": \"نقدر نرتب الساعتين لمراجعة المفاهيم والتدريب على المسائل.\","` | — |
| [SRC-29A9CD43D1-L000226](../../tests/test_dialogue_context_pipeline.py#L226) | 226 | `"        },"` | — |
| [SRC-29A9CD43D1-L000227](../../tests/test_dialogue_context_pipeline.py#L227) | 227 | `"    ]"` | — |
| [SRC-29A9CD43D1-L000228](../../tests/test_dialogue_context_pipeline.py#L228) | 228 | `"    assert not might_be_context_dependent(question)"` | — |
| [SRC-29A9CD43D1-L000229](../../tests/test_dialogue_context_pipeline.py#L229) | 229 | `""` | — |
| [SRC-29A9CD43D1-L000230](../../tests/test_dialogue_context_pipeline.py#L230) | 230 | `"    semantic_context = {"` | — |
| [SRC-29A9CD43D1-L000231](../../tests/test_dialogue_context_pipeline.py#L231) | 231 | `"        \"resolved_question\": ("` | — |
| [SRC-29A9CD43D1-L000232](../../tests/test_dialogue_context_pipeline.py#L232) | 232 | `"            \"في ظل امتحان الكيمياء غدًا ووجود ساعتين لمراجعة الاتزان الكيميائي، \""` | — |
| [SRC-29A9CD43D1-L000233](../../tests/test_dialogue_context_pipeline.py#L233) | 233 | `"            \"بماذا أبدأ؟\""` | — |
| [SRC-29A9CD43D1-L000234](../../tests/test_dialogue_context_pipeline.py#L234) | 234 | `"        ),"` | — |
| [SRC-29A9CD43D1-L000235](../../tests/test_dialogue_context_pipeline.py#L235) | 235 | `"        \"intent\": \"how_to\","` | — |
| [SRC-29A9CD43D1-L000236](../../tests/test_dialogue_context_pipeline.py#L236) | 236 | `"        \"topic\": \"خطة مراجعة الاتزان الكيميائي\","` | — |
| [SRC-29A9CD43D1-L000237](../../tests/test_dialogue_context_pipeline.py#L237) | 237 | `"        \"entities\": [\"امتحان الكيمياء\", \"الاتزان الكيميائي\"],"` | — |
| [SRC-29A9CD43D1-L000238](../../tests/test_dialogue_context_pipeline.py#L238) | 238 | `"        \"slots\": {"` | — |
| [SRC-29A9CD43D1-L000239](../../tests/test_dialogue_context_pipeline.py#L239) | 239 | `"            \"goal\": \"مراجعة امتحان الكيمياء\","` | — |
| [SRC-29A9CD43D1-L000240](../../tests/test_dialogue_context_pipeline.py#L240) | 240 | `"            \"time_range\": \"ساعتان\","` | — |
| [SRC-29A9CD43D1-L000241](../../tests/test_dialogue_context_pipeline.py#L241) | 241 | `"            \"topic\": \"الاتزان الكيميائي\","` | — |
| [SRC-29A9CD43D1-L000242](../../tests/test_dialogue_context_pipeline.py#L242) | 242 | `"        },"` | — |
| [SRC-29A9CD43D1-L000243](../../tests/test_dialogue_context_pipeline.py#L243) | 243 | `"        \"changed_slots\": [\"goal\"],"` | — |
| [SRC-29A9CD43D1-L000244](../../tests/test_dialogue_context_pipeline.py#L244) | 244 | `"        \"is_follow_up\": True,"` | — |
| [SRC-29A9CD43D1-L000245](../../tests/test_dialogue_context_pipeline.py#L245) | 245 | `"        \"topic_shift\": False,"` | — |
| [SRC-29A9CD43D1-L000246](../../tests/test_dialogue_context_pipeline.py#L246) | 246 | `"        \"needs_web\": False,"` | — |
| [SRC-29A9CD43D1-L000247](../../tests/test_dialogue_context_pipeline.py#L247) | 247 | `"        \"research_depth\": \"standard\","` | — |
| [SRC-29A9CD43D1-L000248](../../tests/test_dialogue_context_pipeline.py#L248) | 248 | `"        \"needs_clarification\": False,"` | — |
| [SRC-29A9CD43D1-L000249](../../tests/test_dialogue_context_pipeline.py#L249) | 249 | `"        \"clarification_question\": \"\","` | — |
| [SRC-29A9CD43D1-L000250](../../tests/test_dialogue_context_pipeline.py#L250) | 250 | `"        \"unresolved_references\": [],"` | — |
| [SRC-29A9CD43D1-L000251](../../tests/test_dialogue_context_pipeline.py#L251) | 251 | `"        \"resolution_basis\": \"history_inferred\","` | — |
| [SRC-29A9CD43D1-L000252](../../tests/test_dialogue_context_pipeline.py#L252) | 252 | `"        \"confidence_band\": \"medium\","` | — |
| [SRC-29A9CD43D1-L000253](../../tests/test_dialogue_context_pipeline.py#L253) | 253 | `"    }"` | — |
| [SRC-29A9CD43D1-L000254](../../tests/test_dialogue_context_pipeline.py#L254) | 254 | `"    seen: dict[str, Any] = {\"context_calls\": 0}"` | — |
| [SRC-29A9CD43D1-L000255](../../tests/test_dialogue_context_pipeline.py#L255) | 255 | `""` | — |
| [SRC-29A9CD43D1-L000256](../../tests/test_dialogue_context_pipeline.py#L256) | 256 | `"    def mocked_completion(messages, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000257](../../tests/test_dialogue_context_pipeline.py#L257) | 257 | `"        assert \"أنت محلل سياق حواري\" in messages[0][\"content\"]"` | — |
| [SRC-29A9CD43D1-L000258](../../tests/test_dialogue_context_pipeline.py#L258) | 258 | `"        seen[\"context_calls\"] += 1"` | — |
| [SRC-29A9CD43D1-L000259](../../tests/test_dialogue_context_pipeline.py#L259) | 259 | `"        return json.dumps(semantic_context, ensure_ascii=False)"` | — |
| [SRC-29A9CD43D1-L000260](../../tests/test_dialogue_context_pipeline.py#L260) | 260 | `""` | — |
| [SRC-29A9CD43D1-L000261](../../tests/test_dialogue_context_pipeline.py#L261) | 261 | `"    def answer_without_search(resolved_question, prior_history):"` | — |
| [SRC-29A9CD43D1-L000262](../../tests/test_dialogue_context_pipeline.py#L262) | 262 | `"        seen[\"resolved_question\"] = resolved_question"` | — |
| [SRC-29A9CD43D1-L000263](../../tests/test_dialogue_context_pipeline.py#L263) | 263 | `"        return {"` | — |
| [SRC-29A9CD43D1-L000264](../../tests/test_dialogue_context_pipeline.py#L264) | 264 | `"            \"answer\": \"ابدأ بمراجعة أساسيات الاتزان ثم حل أمثلة قصيرة.\","` | — |
| [SRC-29A9CD43D1-L000265](../../tests/test_dialogue_context_pipeline.py#L265) | 265 | `"            \"question\": resolved_question,"` | — |
| [SRC-29A9CD43D1-L000266](../../tests/test_dialogue_context_pipeline.py#L266) | 266 | `"            \"search_query\": resolved_question,"` | — |
| [SRC-29A9CD43D1-L000267](../../tests/test_dialogue_context_pipeline.py#L267) | 267 | `"            \"search_queries\": [],"` | — |
| [SRC-29A9CD43D1-L000268](../../tests/test_dialogue_context_pipeline.py#L268) | 268 | `"            \"research_plan\": {"` | — |
| [SRC-29A9CD43D1-L000269](../../tests/test_dialogue_context_pipeline.py#L269) | 269 | `"                \"mode\": \"auto\","` | — |
| [SRC-29A9CD43D1-L000270](../../tests/test_dialogue_context_pipeline.py#L270) | 270 | `"                \"planning_method\": \"general_qa_without_web\","` | — |
| [SRC-29A9CD43D1-L000271](../../tests/test_dialogue_context_pipeline.py#L271) | 271 | `"                \"web_search_skipped\": True,"` | — |
| [SRC-29A9CD43D1-L000272](../../tests/test_dialogue_context_pipeline.py#L272) | 272 | `"            },"` | — |
| [SRC-29A9CD43D1-L000273](../../tests/test_dialogue_context_pipeline.py#L273) | 273 | `"            \"sources\": [],"` | — |
| [SRC-29A9CD43D1-L000274](../../tests/test_dialogue_context_pipeline.py#L274) | 274 | `"            \"used_language_model\": True,"` | — |
| [SRC-29A9CD43D1-L000275](../../tests/test_dialogue_context_pipeline.py#L275) | 275 | `"            \"used_web_search\": False,"` | — |
| [SRC-29A9CD43D1-L000276](../../tests/test_dialogue_context_pipeline.py#L276) | 276 | `"            \"search_attempted\": False,"` | — |
| [SRC-29A9CD43D1-L000277](../../tests/test_dialogue_context_pipeline.py#L277) | 277 | `"            \"used_social_search\": False,"` | — |
| [SRC-29A9CD43D1-L000278](../../tests/test_dialogue_context_pipeline.py#L278) | 278 | `"            \"warnings\": [],"` | — |
| [SRC-29A9CD43D1-L000279](../../tests/test_dialogue_context_pipeline.py#L279) | 279 | `"            \"kind\": \"general_answer\","` | — |
| [SRC-29A9CD43D1-L000280](../../tests/test_dialogue_context_pipeline.py#L280) | 280 | `"            \"research_quality\": \"not_applicable\","` | — |
| [SRC-29A9CD43D1-L000281](../../tests/test_dialogue_context_pipeline.py#L281) | 281 | `"            \"model_calls\": [],"` | — |
| [SRC-29A9CD43D1-L000282](../../tests/test_dialogue_context_pipeline.py#L282) | 282 | `"        }"` | — |
| [SRC-29A9CD43D1-L000283](../../tests/test_dialogue_context_pipeline.py#L283) | 283 | `""` | — |
| [SRC-29A9CD43D1-L000284](../../tests/test_dialogue_context_pipeline.py#L284) | 284 | `"    def forbidden_search(*args, **kwargs):"` | — |
| [SRC-29A9CD43D1-L000285](../../tests/test_dialogue_context_pipeline.py#L285) | 285 | `"        pytest.fail(\"This contextual study-plan question must not start web search.\")"` | — |
| [SRC-29A9CD43D1-L000286](../../tests/test_dialogue_context_pipeline.py#L286) | 286 | `""` | — |
| [SRC-29A9CD43D1-L000287](../../tests/test_dialogue_context_pipeline.py#L287) | 287 | `"    monkeypatch.setattr(agent, \"_request_completion\", mocked_completion)"` | — |
| [SRC-29A9CD43D1-L000288](../../tests/test_dialogue_context_pipeline.py#L288) | 288 | `"    monkeypatch.setattr(agent, \"_answer_without_search\", answer_without_search)"` | — |
| [SRC-29A9CD43D1-L000289](../../tests/test_dialogue_context_pipeline.py#L289) | 289 | `"    monkeypatch.setattr(agent, \"_collect_research\", forbidden_search)"` | — |
| [SRC-29A9CD43D1-L000290](../../tests/test_dialogue_context_pipeline.py#L290) | 290 | `""` | — |
| [SRC-29A9CD43D1-L000291](../../tests/test_dialogue_context_pipeline.py#L291) | 291 | `"    result = agent.answer(question, history=history)"` | — |
| [SRC-29A9CD43D1-L000292](../../tests/test_dialogue_context_pipeline.py#L292) | 292 | `""` | — |
| [SRC-29A9CD43D1-L000293](../../tests/test_dialogue_context_pipeline.py#L293) | 293 | `"    assert seen[\"context_calls\"] == 1"` | — |
| [SRC-29A9CD43D1-L000294](../../tests/test_dialogue_context_pipeline.py#L294) | 294 | `"    assert \"الكيمياء\" in seen[\"resolved_question\"]"` | — |
| [SRC-29A9CD43D1-L000295](../../tests/test_dialogue_context_pipeline.py#L295) | 295 | `"    assert \"ساعتين\" in seen[\"resolved_question\"]"` | — |
| [SRC-29A9CD43D1-L000296](../../tests/test_dialogue_context_pipeline.py#L296) | 296 | `"    assert \"الاتزان الكيميائي\" in seen[\"resolved_question\"]"` | — |
| [SRC-29A9CD43D1-L000297](../../tests/test_dialogue_context_pipeline.py#L297) | 297 | `"    assert result[\"question\"] == question"` | — |
| [SRC-29A9CD43D1-L000298](../../tests/test_dialogue_context_pipeline.py#L298) | 298 | `"    assert result[\"dialogue_context\"][\"is_follow_up\"] is True"` | — |
| [SRC-29A9CD43D1-L000299](../../tests/test_dialogue_context_pipeline.py#L299) | 299 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-29A9CD43D1-L000300](../../tests/test_dialogue_context_pipeline.py#L300) | 300 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-29A9CD43D1-L000301](../../tests/test_dialogue_context_pipeline.py#L301) | 301 | `""` | — |
## اختبارات

### FILE-DA139AC9D0 — [tests/test_dialogue_state.py](../../tests/test_dialogue_state.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-DA139AC9D0-L000001](../../tests/test_dialogue_state.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-DA139AC9D0-L000002](../../tests/test_dialogue_state.py#L2) | 2 | `""` | — |
| [SRC-DA139AC9D0-L000003](../../tests/test_dialogue_state.py#L3) | 3 | `"import pytest"` | — |
| [SRC-DA139AC9D0-L000004](../../tests/test_dialogue_state.py#L4) | 4 | `""` | — |
| [SRC-DA139AC9D0-L000005](../../tests/test_dialogue_state.py#L5) | 5 | `"from agents.dialogue_state import ("` | — |
| [SRC-DA139AC9D0-L000006](../../tests/test_dialogue_state.py#L6) | 6 | `"    fallback_dialogue_context,"` | — |
| [SRC-DA139AC9D0-L000007](../../tests/test_dialogue_state.py#L7) | 7 | `"    might_be_context_dependent,"` | — |
| [SRC-DA139AC9D0-L000008](../../tests/test_dialogue_state.py#L8) | 8 | `"    validate_dialogue_context,"` | — |
| [SRC-DA139AC9D0-L000009](../../tests/test_dialogue_state.py#L9) | 9 | `")"` | — |
| [SRC-DA139AC9D0-L000010](../../tests/test_dialogue_state.py#L10) | 10 | `""` | — |
| [SRC-DA139AC9D0-L000011](../../tests/test_dialogue_state.py#L11) | 11 | `""` | — |
| [SRC-DA139AC9D0-L000012](../../tests/test_dialogue_state.py#L12) | 12 | `"def test_deterministic_fallback_preserves_explicit_followup_topic() -> None:"` | — |
| [SRC-DA139AC9D0-L000013](../../tests/test_dialogue_state.py#L13) | 13 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000014](../../tests/test_dialogue_state.py#L14) | 14 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-DA139AC9D0-L000015](../../tests/test_dialogue_state.py#L15) | 15 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن هاتف iPhone 17 في السوق المصري.\"},"` | — |
| [SRC-DA139AC9D0-L000016](../../tests/test_dialogue_state.py#L16) | 16 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000017](../../tests/test_dialogue_state.py#L17) | 17 | `""` | — |
| [SRC-DA139AC9D0-L000018](../../tests/test_dialogue_state.py#L18) | 18 | `"    context = fallback_dialogue_context(\"كام سعرها؟\", history)"` | — |
| [SRC-DA139AC9D0-L000019](../../tests/test_dialogue_state.py#L19) | 19 | `""` | — |
| [SRC-DA139AC9D0-L000020](../../tests/test_dialogue_state.py#L20) | 20 | `"    assert context[\"method\"] == \"deterministic_followup_heuristic\""` | — |
| [SRC-DA139AC9D0-L000021](../../tests/test_dialogue_state.py#L21) | 21 | `"    assert context[\"is_follow_up\"] is True"` | — |
| [SRC-DA139AC9D0-L000022](../../tests/test_dialogue_state.py#L22) | 22 | `"    assert \"iPhone 17\" in context[\"resolved_question\"]"` | — |
| [SRC-DA139AC9D0-L000023](../../tests/test_dialogue_state.py#L23) | 23 | `"    assert \"كام سعرها\" in context[\"resolved_question\"]"` | — |
| [SRC-DA139AC9D0-L000024](../../tests/test_dialogue_state.py#L24) | 24 | `"    assert context[\"confidence_band\"] == \"unassessed\""` | — |
| [SRC-DA139AC9D0-L000025](../../tests/test_dialogue_state.py#L25) | 25 | `""` | — |
| [SRC-DA139AC9D0-L000026](../../tests/test_dialogue_state.py#L26) | 26 | `""` | — |
| [SRC-DA139AC9D0-L000027](../../tests/test_dialogue_state.py#L27) | 27 | `"def test_topic_shift_is_a_hard_boundary_against_stale_context() -> None:"` | — |
| [SRC-DA139AC9D0-L000028](../../tests/test_dialogue_state.py#L28) | 28 | `"    question = \"ازاي أنظف شاشة اللابتوب بأمان؟\""` | — |
| [SRC-DA139AC9D0-L000029](../../tests/test_dialogue_state.py#L29) | 29 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000030](../../tests/test_dialogue_state.py#L30) | 30 | `"        {\"role\": \"user\", \"content\": \"قارن iPhone 17 وSamsung S26\"},"` | — |
| [SRC-DA139AC9D0-L000031](../../tests/test_dialogue_state.py#L31) | 31 | `"        {\"role\": \"assistant\", \"content\": \"هذه مقارنة بين هاتفين.\"},"` | — |
| [SRC-DA139AC9D0-L000032](../../tests/test_dialogue_state.py#L32) | 32 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000033](../../tests/test_dialogue_state.py#L33) | 33 | `"    proposed = {"` | — |
| [SRC-DA139AC9D0-L000034](../../tests/test_dialogue_state.py#L34) | 34 | `"        \"resolved_question\": \"قارن iPhone 17 ثم ازاي أنظف شاشة اللابتوب بأمان\","` | — |
| [SRC-DA139AC9D0-L000035](../../tests/test_dialogue_state.py#L35) | 35 | `"        \"topic_shift\": True,"` | — |
| [SRC-DA139AC9D0-L000036](../../tests/test_dialogue_state.py#L36) | 36 | `"        \"is_follow_up\": True,"` | — |
| [SRC-DA139AC9D0-L000037](../../tests/test_dialogue_state.py#L37) | 37 | `"        \"intent\": \"how_to\","` | — |
| [SRC-DA139AC9D0-L000038](../../tests/test_dialogue_state.py#L38) | 38 | `"        \"needs_clarification\": False,"` | — |
| [SRC-DA139AC9D0-L000039](../../tests/test_dialogue_state.py#L39) | 39 | `"    }"` | — |
| [SRC-DA139AC9D0-L000040](../../tests/test_dialogue_state.py#L40) | 40 | `""` | — |
| [SRC-DA139AC9D0-L000041](../../tests/test_dialogue_state.py#L41) | 41 | `"    context = validate_dialogue_context(proposed, question, history)"` | — |
| [SRC-DA139AC9D0-L000042](../../tests/test_dialogue_state.py#L42) | 42 | `""` | — |
| [SRC-DA139AC9D0-L000043](../../tests/test_dialogue_state.py#L43) | 43 | `"    assert context[\"topic_shift\"] is True"` | — |
| [SRC-DA139AC9D0-L000044](../../tests/test_dialogue_state.py#L44) | 44 | `"    assert context[\"is_follow_up\"] is False"` | — |
| [SRC-DA139AC9D0-L000045](../../tests/test_dialogue_state.py#L45) | 45 | `"    assert context[\"resolved_question\"] == question"` | — |
| [SRC-DA139AC9D0-L000046](../../tests/test_dialogue_state.py#L46) | 46 | `"    assert context[\"resolution_basis\"] == \"current_message\""` | — |
| [SRC-DA139AC9D0-L000047](../../tests/test_dialogue_state.py#L47) | 47 | `"    assert context[\"topic\"] == \"\""` | — |
| [SRC-DA139AC9D0-L000048](../../tests/test_dialogue_state.py#L48) | 48 | `"    assert context[\"entities\"] == []"` | — |
| [SRC-DA139AC9D0-L000049](../../tests/test_dialogue_state.py#L49) | 49 | `"    assert context[\"slots\"] == {}"` | — |
| [SRC-DA139AC9D0-L000050](../../tests/test_dialogue_state.py#L50) | 50 | `"    assert context[\"changed_slots\"] == []"` | — |
| [SRC-DA139AC9D0-L000051](../../tests/test_dialogue_state.py#L51) | 51 | `""` | — |
| [SRC-DA139AC9D0-L000052](../../tests/test_dialogue_state.py#L52) | 52 | `""` | — |
| [SRC-DA139AC9D0-L000053](../../tests/test_dialogue_state.py#L53) | 53 | `"def test_standalone_question_cannot_inherit_old_topic_without_followup_signal() -> None:"` | — |
| [SRC-DA139AC9D0-L000054](../../tests/test_dialogue_state.py#L54) | 54 | `"    question = \"ازاي أنظف شاشة اللابتوب بأمان؟\""` | — |
| [SRC-DA139AC9D0-L000055](../../tests/test_dialogue_state.py#L55) | 55 | `"    history = ["` | — |
| [SRC-DA139AC9D0-L000056](../../tests/test_dialogue_state.py#L56) | 56 | `"        {\"role\": \"user\", \"content\": \"قارن iPhone 17 وSamsung S26 من حيث السعر\"},"` | — |
| [SRC-DA139AC9D0-L000057](../../tests/test_dialogue_state.py#L57) | 57 | `"        {\"role\": \"assistant\", \"content\": \"هذه مقارنة بين هاتفين.\"},"` | — |
| [SRC-DA139AC9D0-L000058](../../tests/test_dialogue_state.py#L58) | 58 | `"    ]"` | — |
| [SRC-DA139AC9D0-L000059](../../tests/test_dialogue_state.py#L59) | 59 | `"    proposed = {"` | — |
| [SRC-DA139AC9D0-L000060](../../tests/test_dialogue_state.py#L60) | 60 | `"        \"resolved_question\": \"قارن iPhone 17 ثم ازاي أنظف شاشة اللابتوب بأمان\","` | — |
| [SRC-DA139AC9D0-L000061](../../tests/test_dialogue_state.py#L61) | 61 | `"        \"topic\": \"مقارنة الهواتف\","` | — |
| [SRC-DA139AC9D0-L000062](../../tests/test_dialogue_state.py#L62) | 62 | `"        \"entities\": [\"iPhone 17\", \"Samsung S26\"],"` | — |
| [SRC-DA139AC9D0-L000063](../../tests/test_dialogue_state.py#L63) | 63 | `"        \"slots\": {\"product\": \"iPhone 17\", \"country\": \"مصر\"},"` | — |
