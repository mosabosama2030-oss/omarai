# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **048**
- سجلات الأسطر: **800**
- النطاق: SRC-6BCB799CEC-L000234 إلى SRC-FA4E1423C3-L000373
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-6BCB799CEC — [tests/test_evidence_provenance.py](../../tests/test_evidence_provenance.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6BCB799CEC-L000234](../../tests/test_evidence_provenance.py#L234) | 234 | `""` | — |
| [SRC-6BCB799CEC-L000235](../../tests/test_evidence_provenance.py#L235) | 235 | `""` | — |
| [SRC-6BCB799CEC-L000236](../../tests/test_evidence_provenance.py#L236) | 236 | `"def test_private_redirect_target_is_rejected_before_a_second_connection(monkeypatch):"` | — |
| [SRC-6BCB799CEC-L000237](../../tests/test_evidence_provenance.py#L237) | 237 | `"    \"\"\"Every redirect is validated independently, even after a pinned public request.\"\"\""` | — |
| [SRC-6BCB799CEC-L000238](../../tests/test_evidence_provenance.py#L238) | 238 | `"    resolutions = []"` | — |
| [SRC-6BCB799CEC-L000239](../../tests/test_evidence_provenance.py#L239) | 239 | `"    connections = []"` | — |
| [SRC-6BCB799CEC-L000240](../../tests/test_evidence_provenance.py#L240) | 240 | `""` | — |
| [SRC-6BCB799CEC-L000241](../../tests/test_evidence_provenance.py#L241) | 241 | `"    def fake_getaddrinfo(host, port, *args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000242](../../tests/test_evidence_provenance.py#L242) | 242 | `"        resolutions.append(host)"` | — |
| [SRC-6BCB799CEC-L000243](../../tests/test_evidence_provenance.py#L243) | 243 | `"        assert host == \"example.com\""` | — |
| [SRC-6BCB799CEC-L000244](../../tests/test_evidence_provenance.py#L244) | 244 | `"        return _addrinfo(\"1.1.1.1\")"` | — |
| [SRC-6BCB799CEC-L000245](../../tests/test_evidence_provenance.py#L245) | 245 | `""` | — |
| [SRC-6BCB799CEC-L000246](../../tests/test_evidence_provenance.py#L246) | 246 | `"    class FakeResponse:"` | — |
| [SRC-6BCB799CEC-L000247](../../tests/test_evidence_provenance.py#L247) | 247 | `"        status_code = 302"` | — |
| [SRC-6BCB799CEC-L000248](../../tests/test_evidence_provenance.py#L248) | 248 | `""` | — |
| [SRC-6BCB799CEC-L000249](../../tests/test_evidence_provenance.py#L249) | 249 | `"        def __init__(self):"` | — |
| [SRC-6BCB799CEC-L000250](../../tests/test_evidence_provenance.py#L250) | 250 | `"            self.headers = {\"location\": \"http://127.0.0.1/latest/meta-data/\"}"` | — |
| [SRC-6BCB799CEC-L000251](../../tests/test_evidence_provenance.py#L251) | 251 | `""` | — |
| [SRC-6BCB799CEC-L000252](../../tests/test_evidence_provenance.py#L252) | 252 | `"        def __enter__(self):"` | — |
| [SRC-6BCB799CEC-L000253](../../tests/test_evidence_provenance.py#L253) | 253 | `"            return self"` | — |
| [SRC-6BCB799CEC-L000254](../../tests/test_evidence_provenance.py#L254) | 254 | `""` | — |
| [SRC-6BCB799CEC-L000255](../../tests/test_evidence_provenance.py#L255) | 255 | `"        def __exit__(self, *args):"` | — |
| [SRC-6BCB799CEC-L000256](../../tests/test_evidence_provenance.py#L256) | 256 | `"            return False"` | — |
| [SRC-6BCB799CEC-L000257](../../tests/test_evidence_provenance.py#L257) | 257 | `""` | — |
| [SRC-6BCB799CEC-L000258](../../tests/test_evidence_provenance.py#L258) | 258 | `"    class FakeClient:"` | — |
| [SRC-6BCB799CEC-L000259](../../tests/test_evidence_provenance.py#L259) | 259 | `"        def __init__(self, *args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000260](../../tests/test_evidence_provenance.py#L260) | 260 | `"            assert kwargs.get(\"trust_env\") is False"` | — |
| [SRC-6BCB799CEC-L000261](../../tests/test_evidence_provenance.py#L261) | 261 | `"            assert kwargs.get(\"follow_redirects\") is False"` | — |
| [SRC-6BCB799CEC-L000262](../../tests/test_evidence_provenance.py#L262) | 262 | `""` | — |
| [SRC-6BCB799CEC-L000263](../../tests/test_evidence_provenance.py#L263) | 263 | `"        def __enter__(self):"` | — |
| [SRC-6BCB799CEC-L000264](../../tests/test_evidence_provenance.py#L264) | 264 | `"            return self"` | — |
| [SRC-6BCB799CEC-L000265](../../tests/test_evidence_provenance.py#L265) | 265 | `""` | — |
| [SRC-6BCB799CEC-L000266](../../tests/test_evidence_provenance.py#L266) | 266 | `"        def __exit__(self, *args):"` | — |
| [SRC-6BCB799CEC-L000267](../../tests/test_evidence_provenance.py#L267) | 267 | `"            return False"` | — |
| [SRC-6BCB799CEC-L000268](../../tests/test_evidence_provenance.py#L268) | 268 | `""` | — |
| [SRC-6BCB799CEC-L000269](../../tests/test_evidence_provenance.py#L269) | 269 | `"        def stream(self, method, url, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000270](../../tests/test_evidence_provenance.py#L270) | 270 | `"            connections.append(url)"` | — |
| [SRC-6BCB799CEC-L000271](../../tests/test_evidence_provenance.py#L271) | 271 | `"            return FakeResponse()"` | — |
| [SRC-6BCB799CEC-L000272](../../tests/test_evidence_provenance.py#L272) | 272 | `""` | — |
| [SRC-6BCB799CEC-L000273](../../tests/test_evidence_provenance.py#L273) | 273 | `"    monkeypatch.setattr(socket, \"getaddrinfo\", fake_getaddrinfo)"` | — |
| [SRC-6BCB799CEC-L000274](../../tests/test_evidence_provenance.py#L274) | 274 | `"    monkeypatch.setattr(\"httpx.Client\", FakeClient)"` | — |
| [SRC-6BCB799CEC-L000275](../../tests/test_evidence_provenance.py#L275) | 275 | `"    assert WebAgent()._fetch_page(\"https://example.com/article\") == (\"\", \"\")"` | — |
| [SRC-6BCB799CEC-L000276](../../tests/test_evidence_provenance.py#L276) | 276 | `"    assert len(connections) == 1"` | — |
| [SRC-6BCB799CEC-L000277](../../tests/test_evidence_provenance.py#L277) | 277 | `"    assert connections[0].startswith(\"https://1.1.1.1/\")"` | — |
| [SRC-6BCB799CEC-L000278](../../tests/test_evidence_provenance.py#L278) | 278 | `"    assert resolutions == [\"example.com\"]"` | — |
| [SRC-6BCB799CEC-L000279](../../tests/test_evidence_provenance.py#L279) | 279 | `""` | — |
| [SRC-6BCB799CEC-L000280](../../tests/test_evidence_provenance.py#L280) | 280 | `""` | — |
| [SRC-6BCB799CEC-L000281](../../tests/test_evidence_provenance.py#L281) | 281 | `""` | — |
| [SRC-6BCB799CEC-L000282](../../tests/test_evidence_provenance.py#L282) | 282 | `"@pytest.mark.parametrize("` | — |
| [SRC-6BCB799CEC-L000283](../../tests/test_evidence_provenance.py#L283) | 283 | `"    \"address\","` | — |
| [SRC-6BCB799CEC-L000284](../../tests/test_evidence_provenance.py#L284) | 284 | `"    ["` | — |
| [SRC-6BCB799CEC-L000285](../../tests/test_evidence_provenance.py#L285) | 285 | `"        \"0.0.0.0\",          # unspecified IPv4"` | — |
| [SRC-6BCB799CEC-L000286](../../tests/test_evidence_provenance.py#L286) | 286 | `"        \"127.0.0.1\",        # loopback IPv4"` | — |
| [SRC-6BCB799CEC-L000287](../../tests/test_evidence_provenance.py#L287) | 287 | `"        \"10.0.0.1\",         # private IPv4"` | — |
| [SRC-6BCB799CEC-L000288](../../tests/test_evidence_provenance.py#L288) | 288 | `"        \"172.16.0.1\",       # private IPv4"` | — |
| [SRC-6BCB799CEC-L000289](../../tests/test_evidence_provenance.py#L289) | 289 | `"        \"192.168.1.1\",      # private IPv4"` | — |
| [SRC-6BCB799CEC-L000290](../../tests/test_evidence_provenance.py#L290) | 290 | `"        \"169.254.169.254\",  # link-local / common metadata endpoint"` | — |
| [SRC-6BCB799CEC-L000291](../../tests/test_evidence_provenance.py#L291) | 291 | `"        \"100.64.0.1\",       # shared address space"` | — |
| [SRC-6BCB799CEC-L000292](../../tests/test_evidence_provenance.py#L292) | 292 | `"        \"::\",                # unspecified IPv6"` | — |
| [SRC-6BCB799CEC-L000293](../../tests/test_evidence_provenance.py#L293) | 293 | `"        \"::1\",               # loopback IPv6"` | — |
| [SRC-6BCB799CEC-L000294](../../tests/test_evidence_provenance.py#L294) | 294 | `"        \"fc00::1\",           # unique-local IPv6"` | — |
| [SRC-6BCB799CEC-L000295](../../tests/test_evidence_provenance.py#L295) | 295 | `"        \"fe80::1\",           # link-local IPv6"` | — |
| [SRC-6BCB799CEC-L000296](../../tests/test_evidence_provenance.py#L296) | 296 | `"    ],"` | — |
| [SRC-6BCB799CEC-L000297](../../tests/test_evidence_provenance.py#L297) | 297 | `")"` | — |
| [SRC-6BCB799CEC-L000298](../../tests/test_evidence_provenance.py#L298) | 298 | `"def test_non_global_ipv4_and_ipv6_dns_answers_are_rejected(address, monkeypatch):"` | — |
| [SRC-6BCB799CEC-L000299](../../tests/test_evidence_provenance.py#L299) | 299 | `"    \"\"\"No DNS answer from a non-global range may pass the page-fetch gate.\"\"\""` | — |
| [SRC-6BCB799CEC-L000300](../../tests/test_evidence_provenance.py#L300) | 300 | `"    monkeypatch.setattr("` | — |
| [SRC-6BCB799CEC-L000301](../../tests/test_evidence_provenance.py#L301) | 301 | `"        socket,"` | — |
| [SRC-6BCB799CEC-L000302](../../tests/test_evidence_provenance.py#L302) | 302 | `"        \"getaddrinfo\","` | — |
| [SRC-6BCB799CEC-L000303](../../tests/test_evidence_provenance.py#L303) | 303 | `"        lambda host, port, *args, **kwargs: _addrinfo(address),"` | — |
| [SRC-6BCB799CEC-L000304](../../tests/test_evidence_provenance.py#L304) | 304 | `"    )"` | — |
| [SRC-6BCB799CEC-L000305](../../tests/test_evidence_provenance.py#L305) | 305 | `""` | — |
| [SRC-6BCB799CEC-L000306](../../tests/test_evidence_provenance.py#L306) | 306 | `"    assert _public_ip_literals(\"public.example\") is None"` | — |
## اختبارات

### FILE-8455F405B6 — [tests/test_evidence_signals.py](../../tests/test_evidence_signals.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-8455F405B6-L000001](../../tests/test_evidence_signals.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-8455F405B6-L000002](../../tests/test_evidence_signals.py#L2) | 2 | `""` | — |
| [SRC-8455F405B6-L000003](../../tests/test_evidence_signals.py#L3) | 3 | `"from datetime import UTC, datetime"` | — |
| [SRC-8455F405B6-L000004](../../tests/test_evidence_signals.py#L4) | 4 | `""` | — |
| [SRC-8455F405B6-L000005](../../tests/test_evidence_signals.py#L5) | 5 | `"from agents.research import _parse_publication_date, evidence_signal_report"` | — |
| [SRC-8455F405B6-L000006](../../tests/test_evidence_signals.py#L6) | 6 | `""` | — |
| [SRC-8455F405B6-L000007](../../tests/test_evidence_signals.py#L7) | 7 | `""` | — |
| [SRC-8455F405B6-L000008](../../tests/test_evidence_signals.py#L8) | 8 | `"def test_evidence_signal_report_uses_domain_provider_page_and_date_coverage():"` | — |
| [SRC-8455F405B6-L000009](../../tests/test_evidence_signals.py#L9) | 9 | `"    now = datetime(2026, 10, 12, 12, 0, tzinfo=UTC)"` | — |
| [SRC-8455F405B6-L000010](../../tests/test_evidence_signals.py#L10) | 10 | `"    sources = []"` | — |
| [SRC-8455F405B6-L000011](../../tests/test_evidence_signals.py#L11) | 11 | `"    domains = ["` | — |
| [SRC-8455F405B6-L000012](../../tests/test_evidence_signals.py#L12) | 12 | `"        \"agency.gov.eg\", \"university.edu.eg\", \"reuters.com\", \"apnews.com\","` | — |
| [SRC-8455F405B6-L000013](../../tests/test_evidence_signals.py#L13) | 13 | `"        \"example.org\", \"example.net\", \"bbc.com\", \"sample.com\","` | — |
| [SRC-8455F405B6-L000014](../../tests/test_evidence_signals.py#L14) | 14 | `"    ]"` | — |
| [SRC-8455F405B6-L000015](../../tests/test_evidence_signals.py#L15) | 15 | `"    classes = ["` | — |
| [SRC-8455F405B6-L000016](../../tests/test_evidence_signals.py#L16) | 16 | `"        \"government\", \"academic\", \"news\", \"news\","` | — |
| [SRC-8455F405B6-L000017](../../tests/test_evidence_signals.py#L17) | 17 | `"        \"general\", \"general\", \"news\", \"general\","` | — |
| [SRC-8455F405B6-L000018](../../tests/test_evidence_signals.py#L18) | 18 | `"    ]"` | — |
| [SRC-8455F405B6-L000019](../../tests/test_evidence_signals.py#L19) | 19 | `"    for index, (domain, source_class) in enumerate(zip(domains, classes)):"` | — |
| [SRC-8455F405B6-L000020](../../tests/test_evidence_signals.py#L20) | 20 | `"        sources.append({"` | — |
| [SRC-8455F405B6-L000021](../../tests/test_evidence_signals.py#L21) | 21 | `"            \"url\": f\"https://{domain}/article-{index}\","` | — |
| [SRC-8455F405B6-L000022](../../tests/test_evidence_signals.py#L22) | 22 | `"            \"domain\": domain,"` | — |
| [SRC-8455F405B6-L000023](../../tests/test_evidence_signals.py#L23) | 23 | `"            \"source_class\": source_class,"` | — |
| [SRC-8455F405B6-L000024](../../tests/test_evidence_signals.py#L24) | 24 | `"            \"providers\": [\"brave_search_api\"] if index % 2 else [\"bing_rss\"],"` | — |
| [SRC-8455F405B6-L000025](../../tests/test_evidence_signals.py#L25) | 25 | `"            \"page_fetched\": index < 3,"` | — |
| [SRC-8455F405B6-L000026](../../tests/test_evidence_signals.py#L26) | 26 | `"            \"published_at\": \"2026-10-10T09:00:00Z\" if index < 6 else \"\","` | — |
| [SRC-8455F405B6-L000027](../../tests/test_evidence_signals.py#L27) | 27 | `"        })"` | — |
| [SRC-8455F405B6-L000028](../../tests/test_evidence_signals.py#L28) | 28 | `""` | — |
| [SRC-8455F405B6-L000029](../../tests/test_evidence_signals.py#L29) | 29 | `"    report = evidence_signal_report(sources, freshness=\"current\", now=now)"` | — |
| [SRC-8455F405B6-L000030](../../tests/test_evidence_signals.py#L30) | 30 | `""` | — |
| [SRC-8455F405B6-L000031](../../tests/test_evidence_signals.py#L31) | 31 | `"    assert report[\"unique_sources\"] == 8"` | — |
| [SRC-8455F405B6-L000032](../../tests/test_evidence_signals.py#L32) | 32 | `"    assert report[\"unique_domains\"] == 8"` | — |
| [SRC-8455F405B6-L000033](../../tests/test_evidence_signals.py#L33) | 33 | `"    assert report[\"providers_count\"] == 2"` | — |
| [SRC-8455F405B6-L000034](../../tests/test_evidence_signals.py#L34) | 34 | `"    assert report[\"pages_read\"] == 3"` | — |
| [SRC-8455F405B6-L000035](../../tests/test_evidence_signals.py#L35) | 35 | `"    assert report[\"primary_sources\"] == 2"` | — |
| [SRC-8455F405B6-L000036](../../tests/test_evidence_signals.py#L36) | 36 | `"    assert report[\"dated_sources\"] == 6"` | — |
| [SRC-8455F405B6-L000037](../../tests/test_evidence_signals.py#L37) | 37 | `"    assert report[\"recent_sources\"] == 6"` | — |
| [SRC-8455F405B6-L000038](../../tests/test_evidence_signals.py#L38) | 38 | `"    assert report[\"coverage_level\"] == \"متعدد المصادر\""` | — |
| [SRC-8455F405B6-L000039](../../tests/test_evidence_signals.py#L39) | 39 | `"    assert \"ليس احتمال صحة الإجابة\" in report[\"score_meaning\"]"` | — |
| [SRC-8455F405B6-L000040](../../tests/test_evidence_signals.py#L40) | 40 | `""` | — |
| [SRC-8455F405B6-L000041](../../tests/test_evidence_signals.py#L41) | 41 | `""` | — |
| [SRC-8455F405B6-L000042](../../tests/test_evidence_signals.py#L42) | 42 | `"def test_evidence_signal_report_warns_when_no_sources_are_available():"` | — |
| [SRC-8455F405B6-L000043](../../tests/test_evidence_signals.py#L43) | 43 | `"    report = evidence_signal_report([], freshness=\"current\")"` | — |
| [SRC-8455F405B6-L000044](../../tests/test_evidence_signals.py#L44) | 44 | `"    assert report[\"coverage_level\"] == \"محدود\""` | — |
| [SRC-8455F405B6-L000045](../../tests/test_evidence_signals.py#L45) | 45 | `"    assert report[\"coverage_score\"] == 0"` | — |
| [SRC-8455F405B6-L000046](../../tests/test_evidence_signals.py#L46) | 46 | `"    assert any(\"لا توجد مصادر\" in warning for warning in report[\"warnings\"])"` | — |
| [SRC-8455F405B6-L000047](../../tests/test_evidence_signals.py#L47) | 47 | `"    assert any(\"حداثة النتائج غير مؤكدة\" in warning for warning in report[\"warnings\"])"` | — |
| [SRC-8455F405B6-L000048](../../tests/test_evidence_signals.py#L48) | 48 | `""` | — |
| [SRC-8455F405B6-L000049](../../tests/test_evidence_signals.py#L49) | 49 | `""` | — |
| [SRC-8455F405B6-L000050](../../tests/test_evidence_signals.py#L50) | 50 | `"def test_publication_date_parser_handles_iso_rfc822_and_relative_dates():"` | — |
| [SRC-8455F405B6-L000051](../../tests/test_evidence_signals.py#L51) | 51 | `"    now = datetime(2026, 10, 12, 12, 0, tzinfo=UTC)"` | — |
| [SRC-8455F405B6-L000052](../../tests/test_evidence_signals.py#L52) | 52 | `"    assert _parse_publication_date(\"2026-10-10T09:00:00Z\", now) == datetime("` | — |
| [SRC-8455F405B6-L000053](../../tests/test_evidence_signals.py#L53) | 53 | `"        2026, 10, 10, 9, 0, tzinfo=UTC"` | — |
| [SRC-8455F405B6-L000054](../../tests/test_evidence_signals.py#L54) | 54 | `"    )"` | — |
| [SRC-8455F405B6-L000055](../../tests/test_evidence_signals.py#L55) | 55 | `"    assert _parse_publication_date(\"2 days ago\", now) == datetime("` | — |
| [SRC-8455F405B6-L000056](../../tests/test_evidence_signals.py#L56) | 56 | `"        2026, 10, 10, 12, 0, tzinfo=UTC"` | — |
| [SRC-8455F405B6-L000057](../../tests/test_evidence_signals.py#L57) | 57 | `"    )"` | — |
| [SRC-8455F405B6-L000058](../../tests/test_evidence_signals.py#L58) | 58 | `"    assert _parse_publication_date(\"date not supplied\", now) is None"` | — |
## اختبارات

### FILE-1A17F27323 — [tests/test_firecrawl_connector.py](../../tests/test_firecrawl_connector.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1A17F27323-L000001](../../tests/test_firecrawl_connector.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-1A17F27323-L000002](../../tests/test_firecrawl_connector.py#L2) | 2 | `""` | — |
| [SRC-1A17F27323-L000003](../../tests/test_firecrawl_connector.py#L3) | 3 | `"import pytest"` | — |
| [SRC-1A17F27323-L000004](../../tests/test_firecrawl_connector.py#L4) | 4 | `""` | — |
| [SRC-1A17F27323-L000005](../../tests/test_firecrawl_connector.py#L5) | 5 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-1A17F27323-L000006](../../tests/test_firecrawl_connector.py#L6) | 6 | `""` | — |
| [SRC-1A17F27323-L000007](../../tests/test_firecrawl_connector.py#L7) | 7 | `""` | — |
| [SRC-1A17F27323-L000008](../../tests/test_firecrawl_connector.py#L8) | 8 | `"class FakeResponse:"` | — |
| [SRC-1A17F27323-L000009](../../tests/test_firecrawl_connector.py#L9) | 9 | `"    status_code = 200"` | — |
| [SRC-1A17F27323-L000010](../../tests/test_firecrawl_connector.py#L10) | 10 | `""` | — |
| [SRC-1A17F27323-L000011](../../tests/test_firecrawl_connector.py#L11) | 11 | `"    def __init__(self, payload):"` | — |
| [SRC-1A17F27323-L000012](../../tests/test_firecrawl_connector.py#L12) | 12 | `"        self._payload = payload"` | — |
| [SRC-1A17F27323-L000013](../../tests/test_firecrawl_connector.py#L13) | 13 | `""` | — |
| [SRC-1A17F27323-L000014](../../tests/test_firecrawl_connector.py#L14) | 14 | `"    def raise_for_status(self):"` | — |
| [SRC-1A17F27323-L000015](../../tests/test_firecrawl_connector.py#L15) | 15 | `"        return None"` | — |
| [SRC-1A17F27323-L000016](../../tests/test_firecrawl_connector.py#L16) | 16 | `""` | — |
| [SRC-1A17F27323-L000017](../../tests/test_firecrawl_connector.py#L17) | 17 | `"    def json(self):"` | — |
| [SRC-1A17F27323-L000018](../../tests/test_firecrawl_connector.py#L18) | 18 | `"        return self._payload"` | — |
| [SRC-1A17F27323-L000019](../../tests/test_firecrawl_connector.py#L19) | 19 | `""` | — |
| [SRC-1A17F27323-L000020](../../tests/test_firecrawl_connector.py#L20) | 20 | `""` | — |
| [SRC-1A17F27323-L000021](../../tests/test_firecrawl_connector.py#L21) | 21 | `"def test_firecrawl_search_normalizes_only_safe_described_web_results(monkeypatch):"` | — |
| [SRC-1A17F27323-L000022](../../tests/test_firecrawl_connector.py#L22) | 22 | `"    monkeypatch.setenv(\"FIRECRAWL_API_KEY\", \"test-firecrawl-secret\")"` | — |
| [SRC-1A17F27323-L000023](../../tests/test_firecrawl_connector.py#L23) | 23 | `"    monkeypatch.setenv(\"FIRECRAWL_SEARCH_ENABLED\", \"1\")"` | — |
| [SRC-1A17F27323-L000024](../../tests/test_firecrawl_connector.py#L24) | 24 | `"    captured = {}"` | — |
| [SRC-1A17F27323-L000025](../../tests/test_firecrawl_connector.py#L25) | 25 | `""` | — |
| [SRC-1A17F27323-L000026](../../tests/test_firecrawl_connector.py#L26) | 26 | `"    def fake_request(method, url, **kwargs):"` | — |
| [SRC-1A17F27323-L000027](../../tests/test_firecrawl_connector.py#L27) | 27 | `"        captured.update(method=method, url=url, kwargs=kwargs)"` | — |
| [SRC-1A17F27323-L000028](../../tests/test_firecrawl_connector.py#L28) | 28 | `"        return FakeResponse({"` | — |
| [SRC-1A17F27323-L000029](../../tests/test_firecrawl_connector.py#L29) | 29 | `"            \"success\": True,"` | — |
| [SRC-1A17F27323-L000030](../../tests/test_firecrawl_connector.py#L30) | 30 | `"            \"data\": {"` | — |
| [SRC-1A17F27323-L000031](../../tests/test_firecrawl_connector.py#L31) | 31 | `"                \"web\": ["` | — |
| [SRC-1A17F27323-L000032](../../tests/test_firecrawl_connector.py#L32) | 32 | `"                    {"` | — |
| [SRC-1A17F27323-L000033](../../tests/test_firecrawl_connector.py#L33) | 33 | `"                        \"title\": \"طلب شراء معدات\","` | — |
| [SRC-1A17F27323-L000034](../../tests/test_firecrawl_connector.py#L34) | 34 | `"                        \"url\": \"https://example.com/request\","` | — |
| [SRC-1A17F27323-L000035](../../tests/test_firecrawl_connector.py#L35) | 35 | `"                        \"description\": \"نبحث عن مورد لتوريد المعدات المطلوبة\","` | — |
| [SRC-1A17F27323-L000036](../../tests/test_firecrawl_connector.py#L36) | 36 | `"                    },"` | — |
| [SRC-1A17F27323-L000037](../../tests/test_firecrawl_connector.py#L37) | 37 | `"                    {"` | — |
| [SRC-1A17F27323-L000038](../../tests/test_firecrawl_connector.py#L38) | 38 | `"                        \"title\": \"وجهة محلية\","` | — |
| [SRC-1A17F27323-L000039](../../tests/test_firecrawl_connector.py#L39) | 39 | `"                        \"url\": \"http://127.0.0.1/internal\","` | — |
| [SRC-1A17F27323-L000040](../../tests/test_firecrawl_connector.py#L40) | 40 | `"                        \"description\": \"طلب شراء معدات\","` | — |
| [SRC-1A17F27323-L000041](../../tests/test_firecrawl_connector.py#L41) | 41 | `"                    },"` | — |
| [SRC-1A17F27323-L000042](../../tests/test_firecrawl_connector.py#L42) | 42 | `"                    {"` | — |
| [SRC-1A17F27323-L000043](../../tests/test_firecrawl_connector.py#L43) | 43 | `"                        \"title\": \"وصف فارغ\","` | — |
| [SRC-1A17F27323-L000044](../../tests/test_firecrawl_connector.py#L44) | 44 | `"                        \"url\": \"https://example.net/empty\","` | — |
| [SRC-1A17F27323-L000045](../../tests/test_firecrawl_connector.py#L45) | 45 | `"                        \"description\": \"\","` | — |
| [SRC-1A17F27323-L000046](../../tests/test_firecrawl_connector.py#L46) | 46 | `"                    },"` | — |
| [SRC-1A17F27323-L000047](../../tests/test_firecrawl_connector.py#L47) | 47 | `"                ]"` | — |
| [SRC-1A17F27323-L000048](../../tests/test_firecrawl_connector.py#L48) | 48 | `"            },"` | — |
| [SRC-1A17F27323-L000049](../../tests/test_firecrawl_connector.py#L49) | 49 | `"        })"` | — |
| [SRC-1A17F27323-L000050](../../tests/test_firecrawl_connector.py#L50) | 50 | `""` | — |
| [SRC-1A17F27323-L000051](../../tests/test_firecrawl_connector.py#L51) | 51 | `"    monkeypatch.setattr(\"agents.web_agent._bounded_http_request\", fake_request)"` | — |
| [SRC-1A17F27323-L000052](../../tests/test_firecrawl_connector.py#L52) | 52 | `"    result = WebAgent()._search_firecrawl(\"طلب شراء معدات في مصر\")"` | — |
| [SRC-1A17F27323-L000053](../../tests/test_firecrawl_connector.py#L53) | 53 | `""` | — |
| [SRC-1A17F27323-L000054](../../tests/test_firecrawl_connector.py#L54) | 54 | `"    assert len(result) == 1"` | — |
| [SRC-1A17F27323-L000055](../../tests/test_firecrawl_connector.py#L55) | 55 | `"    assert result[0][\"provider\"] == \"firecrawl_search_api\""` | — |
| [SRC-1A17F27323-L000056](../../tests/test_firecrawl_connector.py#L56) | 56 | `"    assert result[0][\"url\"] == \"https://example.com/request\""` | — |
| [SRC-1A17F27323-L000057](../../tests/test_firecrawl_connector.py#L57) | 57 | `"    assert result[0][\"snippet\"] == \"نبحث عن مورد لتوريد المعدات المطلوبة\""` | — |
| [SRC-1A17F27323-L000058](../../tests/test_firecrawl_connector.py#L58) | 58 | `"    assert captured[\"method\"] == \"POST\""` | — |
| [SRC-1A17F27323-L000059](../../tests/test_firecrawl_connector.py#L59) | 59 | `"    assert captured[\"url\"] == \"https://api.firecrawl.dev/v2/search\""` | — |
| [SRC-1A17F27323-L000060](../../tests/test_firecrawl_connector.py#L60) | 60 | `"    assert captured[\"kwargs\"][\"json\"][\"sources\"] == [\"web\"]"` | — |
| [SRC-1A17F27323-L000061](../../tests/test_firecrawl_connector.py#L61) | 61 | `"    assert captured[\"kwargs\"][\"json\"][\"limit\"] == 6"` | — |
| [SRC-1A17F27323-L000062](../../tests/test_firecrawl_connector.py#L62) | 62 | `"    assert captured[\"kwargs\"][\"json\"][\"country\"] == \"EG\""` | — |
| [SRC-1A17F27323-L000063](../../tests/test_firecrawl_connector.py#L63) | 63 | `"    assert captured[\"kwargs\"][\"headers\"][\"Authorization\"] == \"Bearer test-firecrawl-secret\""` | — |
| [SRC-1A17F27323-L000064](../../tests/test_firecrawl_connector.py#L64) | 64 | `"    assert captured[\"kwargs\"][\"follow_redirects\"] is False"` | — |
| [SRC-1A17F27323-L000065](../../tests/test_firecrawl_connector.py#L65) | 65 | `""` | — |
| [SRC-1A17F27323-L000066](../../tests/test_firecrawl_connector.py#L66) | 66 | `""` | — |
| [SRC-1A17F27323-L000067](../../tests/test_firecrawl_connector.py#L67) | 67 | `"def test_firecrawl_search_does_not_call_network_without_api_key(monkeypatch):"` | — |
| [SRC-1A17F27323-L000068](../../tests/test_firecrawl_connector.py#L68) | 68 | `"    monkeypatch.setenv(\"FIRECRAWL_SEARCH_ENABLED\", \"1\")"` | — |
| [SRC-1A17F27323-L000069](../../tests/test_firecrawl_connector.py#L69) | 69 | `"    monkeypatch.delenv(\"FIRECRAWL_API_KEY\", raising=False)"` | — |
| [SRC-1A17F27323-L000070](../../tests/test_firecrawl_connector.py#L70) | 70 | `""` | — |
| [SRC-1A17F27323-L000071](../../tests/test_firecrawl_connector.py#L71) | 71 | `"    def unexpected_request(*args, **kwargs):"` | — |
| [SRC-1A17F27323-L000072](../../tests/test_firecrawl_connector.py#L72) | 72 | `"        raise AssertionError(\"network must not be called without an API key\")"` | — |
| [SRC-1A17F27323-L000073](../../tests/test_firecrawl_connector.py#L73) | 73 | `""` | — |
| [SRC-1A17F27323-L000074](../../tests/test_firecrawl_connector.py#L74) | 74 | `"    monkeypatch.setattr(\"agents.web_agent._bounded_http_request\", unexpected_request)"` | — |
| [SRC-1A17F27323-L000075](../../tests/test_firecrawl_connector.py#L75) | 75 | `"    assert WebAgent()._search_firecrawl(\"query\") == []"` | — |
| [SRC-1A17F27323-L000076](../../tests/test_firecrawl_connector.py#L76) | 76 | `""` | — |
| [SRC-1A17F27323-L000077](../../tests/test_firecrawl_connector.py#L77) | 77 | `""` | — |
| [SRC-1A17F27323-L000078](../../tests/test_firecrawl_connector.py#L78) | 78 | `"def test_firecrawl_provider_is_disabled_by_default(monkeypatch):"` | — |
| [SRC-1A17F27323-L000079](../../tests/test_firecrawl_connector.py#L79) | 79 | `"    monkeypatch.delenv(\"FIRECRAWL_API_KEY\", raising=False)"` | — |
| [SRC-1A17F27323-L000080](../../tests/test_firecrawl_connector.py#L80) | 80 | `"    monkeypatch.delenv(\"FIRECRAWL_SEARCH_ENABLED\", raising=False)"` | — |
| [SRC-1A17F27323-L000081](../../tests/test_firecrawl_connector.py#L81) | 81 | `"    monkeypatch.delenv(\"OMARAI_FIRECRAWL_SEARCH_REQUEST_BUDGET\", raising=False)"` | — |
| [SRC-1A17F27323-L000082](../../tests/test_firecrawl_connector.py#L82) | 82 | `""` | — |
| [SRC-1A17F27323-L000083](../../tests/test_firecrawl_connector.py#L83) | 83 | `"    status = WebAgent.status()"` | — |
| [SRC-1A17F27323-L000084](../../tests/test_firecrawl_connector.py#L84) | 84 | `""` | — |
| [SRC-1A17F27323-L000085](../../tests/test_firecrawl_connector.py#L85) | 85 | `"    assert status[\"firecrawl_search_api_configured\"] is False"` | — |
| [SRC-1A17F27323-L000086](../../tests/test_firecrawl_connector.py#L86) | 86 | `"    assert status[\"firecrawl_search_enabled\"] is False"` | — |
| [SRC-1A17F27323-L000087](../../tests/test_firecrawl_connector.py#L87) | 87 | `"    assert status[\"firecrawl_search_request_budget\"] == 0"` | — |
| [SRC-1A17F27323-L000088](../../tests/test_firecrawl_connector.py#L88) | 88 | `""` | — |
| [SRC-1A17F27323-L000089](../../tests/test_firecrawl_connector.py#L89) | 89 | `""` | — |
| [SRC-1A17F27323-L000090](../../tests/test_firecrawl_connector.py#L90) | 90 | `"def test_firecrawl_request_budget_is_opt_in_and_hard_capped_to_one(monkeypatch):"` | — |
| [SRC-1A17F27323-L000091](../../tests/test_firecrawl_connector.py#L91) | 91 | `"    agent = WebAgent()"` | — |
| [SRC-1A17F27323-L000092](../../tests/test_firecrawl_connector.py#L92) | 92 | `"    monkeypatch.setenv(\"FIRECRAWL_API_KEY\", \"test-firecrawl-secret\")"` | — |
| [SRC-1A17F27323-L000093](../../tests/test_firecrawl_connector.py#L93) | 93 | `"    monkeypatch.setenv(\"FIRECRAWL_SEARCH_ENABLED\", \"1\")"` | — |
| [SRC-1A17F27323-L000094](../../tests/test_firecrawl_connector.py#L94) | 94 | `"    monkeypatch.setenv(\"OMARAI_FIRECRAWL_SEARCH_REQUEST_BUDGET\", \"3\")"` | — |
| [SRC-1A17F27323-L000095](../../tests/test_firecrawl_connector.py#L95) | 95 | `""` | — |
| [SRC-1A17F27323-L000096](../../tests/test_firecrawl_connector.py#L96) | 96 | `"    agent._reset_deepseek_search_budget()"` | — |
| [SRC-1A17F27323-L000097](../../tests/test_firecrawl_connector.py#L97) | 97 | `"    assert agent._reserve_firecrawl_search_request() is True"` | — |
| [SRC-1A17F27323-L000098](../../tests/test_firecrawl_connector.py#L98) | 98 | `"    assert agent._reserve_firecrawl_search_request() is False"` | — |
| [SRC-1A17F27323-L000099](../../tests/test_firecrawl_connector.py#L99) | 99 | `""` | — |
| [SRC-1A17F27323-L000100](../../tests/test_firecrawl_connector.py#L100) | 100 | `"    agent._reset_deepseek_search_budget()"` | — |
| [SRC-1A17F27323-L000101](../../tests/test_firecrawl_connector.py#L101) | 101 | `"    assert agent._reserve_firecrawl_search_request() is True"` | — |
| [SRC-1A17F27323-L000102](../../tests/test_firecrawl_connector.py#L102) | 102 | `""` | — |
| [SRC-1A17F27323-L000103](../../tests/test_firecrawl_connector.py#L103) | 103 | `""` | — |
| [SRC-1A17F27323-L000104](../../tests/test_firecrawl_connector.py#L104) | 104 | `"def test_firecrawl_request_budget_defaults_to_zero(monkeypatch):"` | — |
| [SRC-1A17F27323-L000105](../../tests/test_firecrawl_connector.py#L105) | 105 | `"    agent = WebAgent()"` | — |
| [SRC-1A17F27323-L000106](../../tests/test_firecrawl_connector.py#L106) | 106 | `"    monkeypatch.setenv(\"FIRECRAWL_API_KEY\", \"test-firecrawl-secret\")"` | — |
| [SRC-1A17F27323-L000107](../../tests/test_firecrawl_connector.py#L107) | 107 | `"    monkeypatch.setenv(\"FIRECRAWL_SEARCH_ENABLED\", \"1\")"` | — |
| [SRC-1A17F27323-L000108](../../tests/test_firecrawl_connector.py#L108) | 108 | `"    monkeypatch.delenv(\"OMARAI_FIRECRAWL_SEARCH_REQUEST_BUDGET\", raising=False)"` | — |
| [SRC-1A17F27323-L000109](../../tests/test_firecrawl_connector.py#L109) | 109 | `""` | — |
| [SRC-1A17F27323-L000110](../../tests/test_firecrawl_connector.py#L110) | 110 | `"    agent._reset_deepseek_search_budget()"` | — |
| [SRC-1A17F27323-L000111](../../tests/test_firecrawl_connector.py#L111) | 111 | `""` | — |
| [SRC-1A17F27323-L000112](../../tests/test_firecrawl_connector.py#L112) | 112 | `"    assert agent._reserve_firecrawl_search_request() is False"` | — |
| [SRC-1A17F27323-L000113](../../tests/test_firecrawl_connector.py#L113) | 113 | `""` | — |
| [SRC-1A17F27323-L000114](../../tests/test_firecrawl_connector.py#L114) | 114 | `""` | — |
| [SRC-1A17F27323-L000115](../../tests/test_firecrawl_connector.py#L115) | 115 | `"def test_firecrawl_is_blocked_when_optional_providers_are_disabled(monkeypatch):"` | — |
| [SRC-1A17F27323-L000116](../../tests/test_firecrawl_connector.py#L116) | 116 | `"    agent = WebAgent()"` | — |
| [SRC-1A17F27323-L000117](../../tests/test_firecrawl_connector.py#L117) | 117 | `"    agent.allow_optional_providers = False"` | — |
| [SRC-1A17F27323-L000118](../../tests/test_firecrawl_connector.py#L118) | 118 | `"    monkeypatch.setenv(\"FIRECRAWL_API_KEY\", \"test-firecrawl-secret\")"` | — |
| [SRC-1A17F27323-L000119](../../tests/test_firecrawl_connector.py#L119) | 119 | `"    monkeypatch.setenv(\"FIRECRAWL_SEARCH_ENABLED\", \"1\")"` | — |
| [SRC-1A17F27323-L000120](../../tests/test_firecrawl_connector.py#L120) | 120 | `"    monkeypatch.setenv(\"OMARAI_FIRECRAWL_SEARCH_REQUEST_BUDGET\", \"1\")"` | — |
| [SRC-1A17F27323-L000121](../../tests/test_firecrawl_connector.py#L121) | 121 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _query: [])"` | — |
| [SRC-1A17F27323-L000122](../../tests/test_firecrawl_connector.py#L122) | 122 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _query: [])"` | — |
| [SRC-1A17F27323-L000123](../../tests/test_firecrawl_connector.py#L123) | 123 | `""` | — |
| [SRC-1A17F27323-L000124](../../tests/test_firecrawl_connector.py#L124) | 124 | `"    def forbidden_firecrawl(_query):"` | — |
| [SRC-1A17F27323-L000125](../../tests/test_firecrawl_connector.py#L125) | 125 | `"        pytest.fail(\"per-request optional-provider denial must block Firecrawl\")"` | — |
| [SRC-1A17F27323-L000126](../../tests/test_firecrawl_connector.py#L126) | 126 | `""` | — |
| [SRC-1A17F27323-L000127](../../tests/test_firecrawl_connector.py#L127) | 127 | `"    monkeypatch.setattr(agent, \"_search_firecrawl\", forbidden_firecrawl)"` | — |
| [SRC-1A17F27323-L000128](../../tests/test_firecrawl_connector.py#L128) | 128 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-1A17F27323-L000129](../../tests/test_firecrawl_connector.py#L129) | 129 | `"        agent._search_web(\"Find industrial fire alarm suppliers in Egypt\")"` | — |
| [SRC-1A17F27323-L000130](../../tests/test_firecrawl_connector.py#L130) | 130 | `""` | — |
| [SRC-1A17F27323-L000131](../../tests/test_firecrawl_connector.py#L131) | 131 | `"    firecrawl_status = next("` | — |
| [SRC-1A17F27323-L000132](../../tests/test_firecrawl_connector.py#L132) | 132 | `"        item[\"status\"]"` | — |
| [SRC-1A17F27323-L000133](../../tests/test_firecrawl_connector.py#L133) | 133 | `"        for item in agent._provider_diagnostics"` | — |
| [SRC-1A17F27323-L000134](../../tests/test_firecrawl_connector.py#L134) | 134 | `"        if item[\"provider\"] == \"firecrawl_search_api\""` | — |
| [SRC-1A17F27323-L000135](../../tests/test_firecrawl_connector.py#L135) | 135 | `"    )"` | — |
| [SRC-1A17F27323-L000136](../../tests/test_firecrawl_connector.py#L136) | 136 | `"    assert firecrawl_status == \"disabled_by_request\""` | — |
| [SRC-1A17F27323-L000137](../../tests/test_firecrawl_connector.py#L137) | 137 | `""` | — |
| [SRC-1A17F27323-L000138](../../tests/test_firecrawl_connector.py#L138) | 138 | `""` | — |
| [SRC-1A17F27323-L000139](../../tests/test_firecrawl_connector.py#L139) | 139 | `"@pytest.mark.parametrize("` | — |
| [SRC-1A17F27323-L000140](../../tests/test_firecrawl_connector.py#L140) | 140 | `"    (\"query\", \"expected\"),"` | — |
| [SRC-1A17F27323-L000141](../../tests/test_firecrawl_connector.py#L141) | 141 | `"    ["` | — |
| [SRC-1A17F27323-L000142](../../tests/test_firecrawl_connector.py#L142) | 142 | `"        (\"Find buyers for industrial fire alarms in Egypt\", \"EG\"),"` | — |
| [SRC-1A17F27323-L000143](../../tests/test_firecrawl_connector.py#L143) | 143 | `"        (\"موردون لأنظمة الإنذار في السعودية\", \"SA\"),"` | — |
| [SRC-1A17F27323-L000144](../../tests/test_firecrawl_connector.py#L144) | 144 | `"        (\"Find fire alarm suppliers in Dubai UAE\", \"AE\"),"` | — |
| [SRC-1A17F27323-L000145](../../tests/test_firecrawl_connector.py#L145) | 145 | `"        (\"Find suppliers in the United Kingdom\", \"UK\"),"` | — |
| [SRC-1A17F27323-L000146](../../tests/test_firecrawl_connector.py#L146) | 146 | `"        (\"ابحث عن موردين لأنظمة الإنذار\", None),"` | — |
| [SRC-1A17F27323-L000147](../../tests/test_firecrawl_connector.py#L147) | 147 | `"        (\"Find suppliers for fire alarms\", None),"` | — |
| [SRC-1A17F27323-L000148](../../tests/test_firecrawl_connector.py#L148) | 148 | `"        (\"Find suppliers in the United States\", \"US\"),"` | — |
| [SRC-1A17F27323-L000149](../../tests/test_firecrawl_connector.py#L149) | 149 | `"        (\"Find suppliers in the U.S.A.\", \"US\"),"` | — |
| [SRC-1A17F27323-L000150](../../tests/test_firecrawl_connector.py#L150) | 150 | `"    ],"` | — |
| [SRC-1A17F27323-L000151](../../tests/test_firecrawl_connector.py#L151) | 151 | `")"` | — |
| [SRC-1A17F27323-L000152](../../tests/test_firecrawl_connector.py#L152) | 152 | `"def test_firecrawl_search_uses_explicit_query_geography(query, expected):"` | — |
| [SRC-1A17F27323-L000153](../../tests/test_firecrawl_connector.py#L153) | 153 | `"    assert WebAgent._firecrawl_search_country(query) == expected"` | — |
| [SRC-1A17F27323-L000154](../../tests/test_firecrawl_connector.py#L154) | 154 | `""` | — |
| [SRC-1A17F27323-L000155](../../tests/test_firecrawl_connector.py#L155) | 155 | `""` | — |
| [SRC-1A17F27323-L000156](../../tests/test_firecrawl_connector.py#L156) | 156 | `"@pytest.mark.parametrize("` | — |
| [SRC-1A17F27323-L000157](../../tests/test_firecrawl_connector.py#L157) | 157 | `"    (\"enabled\", \"api_key\", \"budget\", \"expected_status\"),"` | — |
| [SRC-1A17F27323-L000158](../../tests/test_firecrawl_connector.py#L158) | 158 | `"    ["` | — |
| [SRC-1A17F27323-L000159](../../tests/test_firecrawl_connector.py#L159) | 159 | `"        (\"0\", \"\", \"0\", \"disabled\"),"` | — |
| [SRC-1A17F27323-L000160](../../tests/test_firecrawl_connector.py#L160) | 160 | `"        (\"1\", \"\", \"1\", \"not_configured\"),"` | — |
| [SRC-1A17F27323-L000161](../../tests/test_firecrawl_connector.py#L161) | 161 | `"        (\"1\", \"test-firecrawl-secret\", \"0\", \"budget_exhausted\"),"` | — |
| [SRC-1A17F27323-L000162](../../tests/test_firecrawl_connector.py#L162) | 162 | `"        (\"1\", \"test-firecrawl-secret\", \"1\", \"configured\"),"` | — |
| [SRC-1A17F27323-L000163](../../tests/test_firecrawl_connector.py#L163) | 163 | `"    ],"` | — |
| [SRC-1A17F27323-L000164](../../tests/test_firecrawl_connector.py#L164) | 164 | `")"` | — |
| [SRC-1A17F27323-L000165](../../tests/test_firecrawl_connector.py#L165) | 165 | `"def test_firecrawl_capability_snapshot_reports_configuration_and_budget("` | — |
| [SRC-1A17F27323-L000166](../../tests/test_firecrawl_connector.py#L166) | 166 | `"    monkeypatch, enabled, api_key, budget, expected_status"` | — |
| [SRC-1A17F27323-L000167](../../tests/test_firecrawl_connector.py#L167) | 167 | `"):"` | — |
| [SRC-1A17F27323-L000168](../../tests/test_firecrawl_connector.py#L168) | 168 | `"    monkeypatch.setenv(\"FIRECRAWL_SEARCH_ENABLED\", enabled)"` | — |
| [SRC-1A17F27323-L000169](../../tests/test_firecrawl_connector.py#L169) | 169 | `"    monkeypatch.setenv(\"OMARAI_FIRECRAWL_SEARCH_REQUEST_BUDGET\", budget)"` | — |
| [SRC-1A17F27323-L000170](../../tests/test_firecrawl_connector.py#L170) | 170 | `"    if api_key:"` | — |
| [SRC-1A17F27323-L000171](../../tests/test_firecrawl_connector.py#L171) | 171 | `"        monkeypatch.setenv(\"FIRECRAWL_API_KEY\", api_key)"` | — |
| [SRC-1A17F27323-L000172](../../tests/test_firecrawl_connector.py#L172) | 172 | `"    else:"` | — |
| [SRC-1A17F27323-L000173](../../tests/test_firecrawl_connector.py#L173) | 173 | `"        monkeypatch.delenv(\"FIRECRAWL_API_KEY\", raising=False)"` | — |
| [SRC-1A17F27323-L000174](../../tests/test_firecrawl_connector.py#L174) | 174 | `""` | — |
| [SRC-1A17F27323-L000175](../../tests/test_firecrawl_connector.py#L175) | 175 | `"    snapshot = WebAgent()._capability_status_snapshot()"` | — |
| [SRC-1A17F27323-L000176](../../tests/test_firecrawl_connector.py#L176) | 176 | `"    firecrawl = next("` | — |
| [SRC-1A17F27323-L000177](../../tests/test_firecrawl_connector.py#L177) | 177 | `"        item for item in snapshot[\"web_search\"][\"providers\"]"` | — |
| [SRC-1A17F27323-L000178](../../tests/test_firecrawl_connector.py#L178) | 178 | `"        if item[\"name\"] == \"firecrawl_search_api\""` | — |
| [SRC-1A17F27323-L000179](../../tests/test_firecrawl_connector.py#L179) | 179 | `"    )"` | — |
| [SRC-1A17F27323-L000180](../../tests/test_firecrawl_connector.py#L180) | 180 | `""` | — |
| [SRC-1A17F27323-L000181](../../tests/test_firecrawl_connector.py#L181) | 181 | `"    assert firecrawl[\"implemented\"] is True"` | — |
| [SRC-1A17F27323-L000182](../../tests/test_firecrawl_connector.py#L182) | 182 | `"    assert firecrawl[\"configuration_status\"] == expected_status"` | — |
| [SRC-1A17F27323-L000183](../../tests/test_firecrawl_connector.py#L183) | 183 | `"    if expected_status == \"configured\":"` | — |
| [SRC-1A17F27323-L000184](../../tests/test_firecrawl_connector.py#L184) | 184 | `"        assert firecrawl[\"runtime_status\"] == \"not_tested_in_this_response\""` | — |
| [SRC-1A17F27323-L000185](../../tests/test_firecrawl_connector.py#L185) | 185 | `"    else:"` | — |
| [SRC-1A17F27323-L000186](../../tests/test_firecrawl_connector.py#L186) | 186 | `"        assert firecrawl[\"runtime_status\"] == expected_status"` | — |
| [SRC-1A17F27323-L000187](../../tests/test_firecrawl_connector.py#L187) | 187 | `""` | — |
| [SRC-1A17F27323-L000188](../../tests/test_firecrawl_connector.py#L188) | 188 | `""` | — |
| [SRC-1A17F27323-L000189](../../tests/test_firecrawl_connector.py#L189) | 189 | `"def test_firecrawl_search_does_not_call_network_when_disabled_even_with_key(monkeypatch):"` | — |
| [SRC-1A17F27323-L000190](../../tests/test_firecrawl_connector.py#L190) | 190 | `"    monkeypatch.setenv(\"FIRECRAWL_API_KEY\", \"test-firecrawl-secret\")"` | — |
| [SRC-1A17F27323-L000191](../../tests/test_firecrawl_connector.py#L191) | 191 | `"    monkeypatch.setenv(\"FIRECRAWL_SEARCH_ENABLED\", \"0\")"` | — |
| [SRC-1A17F27323-L000192](../../tests/test_firecrawl_connector.py#L192) | 192 | `""` | — |
| [SRC-1A17F27323-L000193](../../tests/test_firecrawl_connector.py#L193) | 193 | `"    def unexpected_request(*args, **kwargs):"` | — |
| [SRC-1A17F27323-L000194](../../tests/test_firecrawl_connector.py#L194) | 194 | `"        raise AssertionError(\"disabled Firecrawl connector must not call the network\")"` | — |
| [SRC-1A17F27323-L000195](../../tests/test_firecrawl_connector.py#L195) | 195 | `""` | — |
| [SRC-1A17F27323-L000196](../../tests/test_firecrawl_connector.py#L196) | 196 | `"    monkeypatch.setattr(\"agents.web_agent._bounded_http_request\", unexpected_request)"` | — |
| [SRC-1A17F27323-L000197](../../tests/test_firecrawl_connector.py#L197) | 197 | `"    assert WebAgent()._search_firecrawl(\"query\") == []"` | — |
| [SRC-1A17F27323-L000198](../../tests/test_firecrawl_connector.py#L198) | 198 | `""` | — |
| [SRC-1A17F27323-L000199](../../tests/test_firecrawl_connector.py#L199) | 199 | `""` | — |
| [SRC-1A17F27323-L000200](../../tests/test_firecrawl_connector.py#L200) | 200 | `"def test_firecrawl_status_handles_invalid_budget_without_crashing(monkeypatch):"` | — |
| [SRC-1A17F27323-L000201](../../tests/test_firecrawl_connector.py#L201) | 201 | `"    monkeypatch.setenv(\"FIRECRAWL_API_KEY\", \"test-firecrawl-secret\")"` | — |
| [SRC-1A17F27323-L000202](../../tests/test_firecrawl_connector.py#L202) | 202 | `"    monkeypatch.setenv(\"FIRECRAWL_SEARCH_ENABLED\", \"1\")"` | — |
| [SRC-1A17F27323-L000203](../../tests/test_firecrawl_connector.py#L203) | 203 | `"    monkeypatch.setenv(\"OMARAI_FIRECRAWL_SEARCH_REQUEST_BUDGET\", \"not-a-number\")"` | — |
| [SRC-1A17F27323-L000204](../../tests/test_firecrawl_connector.py#L204) | 204 | `""` | — |
| [SRC-1A17F27323-L000205](../../tests/test_firecrawl_connector.py#L205) | 205 | `"    status = WebAgent.status()"` | — |
| [SRC-1A17F27323-L000206](../../tests/test_firecrawl_connector.py#L206) | 206 | `""` | — |
| [SRC-1A17F27323-L000207](../../tests/test_firecrawl_connector.py#L207) | 207 | `"    assert status[\"firecrawl_search_api_configured\"] is True"` | — |
| [SRC-1A17F27323-L000208](../../tests/test_firecrawl_connector.py#L208) | 208 | `"    assert status[\"firecrawl_search_enabled\"] is True"` | — |
| [SRC-1A17F27323-L000209](../../tests/test_firecrawl_connector.py#L209) | 209 | `"    assert status[\"firecrawl_search_request_budget\"] == 0"` | — |
| [SRC-1A17F27323-L000210](../../tests/test_firecrawl_connector.py#L210) | 210 | `""` | — |
| [SRC-1A17F27323-L000211](../../tests/test_firecrawl_connector.py#L211) | 211 | `""` | — |
| [SRC-1A17F27323-L000212](../../tests/test_firecrawl_connector.py#L212) | 212 | `"@pytest.mark.parametrize("` | — |
| [SRC-1A17F27323-L000213](../../tests/test_firecrawl_connector.py#L213) | 213 | `"    \"query\","` | — |
| [SRC-1A17F27323-L000214](../../tests/test_firecrawl_connector.py#L214) | 214 | `"    ["` | — |
| [SRC-1A17F27323-L000215](../../tests/test_firecrawl_connector.py#L215) | 215 | `"        \"ابحث عن موردين لأنظمة إنذار الحريق\","` | — |
| [SRC-1A17F27323-L000216](../../tests/test_firecrawl_connector.py#L216) | 216 | `"        \"Find suppliers for industrial fire alarm systems\","` | — |
| [SRC-1A17F27323-L000217](../../tests/test_firecrawl_connector.py#L217) | 217 | `"    ],"` | — |
| [SRC-1A17F27323-L000218](../../tests/test_firecrawl_connector.py#L218) | 218 | `")"` | — |
| [SRC-1A17F27323-L000219](../../tests/test_firecrawl_connector.py#L219) | 219 | `"def test_firecrawl_search_skips_network_without_explicit_country(monkeypatch, query):"` | — |
| [SRC-1A17F27323-L000220](../../tests/test_firecrawl_connector.py#L220) | 220 | `"    monkeypatch.setenv(\"FIRECRAWL_API_KEY\", \"test-firecrawl-secret\")"` | — |
| [SRC-1A17F27323-L000221](../../tests/test_firecrawl_connector.py#L221) | 221 | `"    monkeypatch.setenv(\"FIRECRAWL_SEARCH_ENABLED\", \"1\")"` | — |
| [SRC-1A17F27323-L000222](../../tests/test_firecrawl_connector.py#L222) | 222 | `""` | — |
| [SRC-1A17F27323-L000223](../../tests/test_firecrawl_connector.py#L223) | 223 | `"    def unexpected_request(*args, **kwargs):"` | — |
| [SRC-1A17F27323-L000224](../../tests/test_firecrawl_connector.py#L224) | 224 | `"        pytest.fail(\"Firecrawl must not be called when its default country would bias results to US\")"` | — |
| [SRC-1A17F27323-L000225](../../tests/test_firecrawl_connector.py#L225) | 225 | `""` | — |
| [SRC-1A17F27323-L000226](../../tests/test_firecrawl_connector.py#L226) | 226 | `"    monkeypatch.setattr(\"agents.web_agent._bounded_http_request\", unexpected_request)"` | — |
| [SRC-1A17F27323-L000227](../../tests/test_firecrawl_connector.py#L227) | 227 | `""` | — |
| [SRC-1A17F27323-L000228](../../tests/test_firecrawl_connector.py#L228) | 228 | `"    assert WebAgent()._search_firecrawl(query) == []"` | — |
| [SRC-1A17F27323-L000229](../../tests/test_firecrawl_connector.py#L229) | 229 | `""` | — |
| [SRC-1A17F27323-L000230](../../tests/test_firecrawl_connector.py#L230) | 230 | `""` | — |
| [SRC-1A17F27323-L000231](../../tests/test_firecrawl_connector.py#L231) | 231 | `"def test_firecrawl_search_is_not_attempted_or_budgeted_without_explicit_country(monkeypatch):"` | — |
| [SRC-1A17F27323-L000232](../../tests/test_firecrawl_connector.py#L232) | 232 | `"    agent = WebAgent()"` | — |
| [SRC-1A17F27323-L000233](../../tests/test_firecrawl_connector.py#L233) | 233 | `"    agent.allow_optional_providers = True"` | — |
| [SRC-1A17F27323-L000234](../../tests/test_firecrawl_connector.py#L234) | 234 | `"    monkeypatch.setenv(\"FIRECRAWL_API_KEY\", \"test-firecrawl-secret\")"` | — |
| [SRC-1A17F27323-L000235](../../tests/test_firecrawl_connector.py#L235) | 235 | `"    monkeypatch.setenv(\"FIRECRAWL_SEARCH_ENABLED\", \"1\")"` | — |
| [SRC-1A17F27323-L000236](../../tests/test_firecrawl_connector.py#L236) | 236 | `"    monkeypatch.setenv(\"OMARAI_FIRECRAWL_SEARCH_REQUEST_BUDGET\", \"1\")"` | — |
| [SRC-1A17F27323-L000237](../../tests/test_firecrawl_connector.py#L237) | 237 | `"    monkeypatch.delenv(\"DEEPSEEK_SEARCH_API_KEY\", raising=False)"` | — |
| [SRC-1A17F27323-L000238](../../tests/test_firecrawl_connector.py#L238) | 238 | `"    monkeypatch.delenv(\"BRAVE_SEARCH_API_KEY\", raising=False)"` | — |
| [SRC-1A17F27323-L000239](../../tests/test_firecrawl_connector.py#L239) | 239 | `"    monkeypatch.delenv(\"TAVILY_API_KEY\", raising=False)"` | — |
| [SRC-1A17F27323-L000240](../../tests/test_firecrawl_connector.py#L240) | 240 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _query: [])"` | — |
| [SRC-1A17F27323-L000241](../../tests/test_firecrawl_connector.py#L241) | 241 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _query: [])"` | — |
| [SRC-1A17F27323-L000242](../../tests/test_firecrawl_connector.py#L242) | 242 | `"    monkeypatch.setattr("` | — |
| [SRC-1A17F27323-L000243](../../tests/test_firecrawl_connector.py#L243) | 243 | `"        \"agents.web_agent._bounded_http_request\","` | — |
| [SRC-1A17F27323-L000244](../../tests/test_firecrawl_connector.py#L244) | 244 | `"        lambda *args, **kwargs: pytest.fail(\"no provider request is expected for this unlocated query\"),"` | — |
| [SRC-1A17F27323-L000245](../../tests/test_firecrawl_connector.py#L245) | 245 | `"    )"` | — |
| [SRC-1A17F27323-L000246](../../tests/test_firecrawl_connector.py#L246) | 246 | `""` | — |
| [SRC-1A17F27323-L000247](../../tests/test_firecrawl_connector.py#L247) | 247 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-1A17F27323-L000248](../../tests/test_firecrawl_connector.py#L248) | 248 | `"        agent._search_web(\"Find suppliers for industrial fire alarm systems\")"` | — |
| [SRC-1A17F27323-L000249](../../tests/test_firecrawl_connector.py#L249) | 249 | `""` | — |
| [SRC-1A17F27323-L000250](../../tests/test_firecrawl_connector.py#L250) | 250 | `"    diagnostic = next("` | — |
| [SRC-1A17F27323-L000251](../../tests/test_firecrawl_connector.py#L251) | 251 | `"        item for item in agent._provider_diagnostics"` | — |
| [SRC-1A17F27323-L000252](../../tests/test_firecrawl_connector.py#L252) | 252 | `"        if item[\"provider\"] == \"firecrawl_search_api\""` | — |
| [SRC-1A17F27323-L000253](../../tests/test_firecrawl_connector.py#L253) | 253 | `"    )"` | — |
| [SRC-1A17F27323-L000254](../../tests/test_firecrawl_connector.py#L254) | 254 | `"    assert diagnostic[\"status\"] == \"not_attempted\""` | — |
| [SRC-1A17F27323-L000255](../../tests/test_firecrawl_connector.py#L255) | 255 | `"    assert agent._firecrawl_search_requests_reserved == 0"` | — |
| [SRC-1A17F27323-L000256](../../tests/test_firecrawl_connector.py#L256) | 256 | `""` | — |
| [SRC-1A17F27323-L000257](../../tests/test_firecrawl_connector.py#L257) | 257 | `""` | — |
| [SRC-1A17F27323-L000258](../../tests/test_firecrawl_connector.py#L258) | 258 | `"def test_firecrawl_search_skips_network_when_no_explicit_geography(monkeypatch):"` | — |
| [SRC-1A17F27323-L000259](../../tests/test_firecrawl_connector.py#L259) | 259 | `"    monkeypatch.setenv(\"FIRECRAWL_API_KEY\", \"test-firecrawl-secret\")"` | — |
| [SRC-1A17F27323-L000260](../../tests/test_firecrawl_connector.py#L260) | 260 | `"    monkeypatch.setenv(\"FIRECRAWL_SEARCH_ENABLED\", \"1\")"` | — |
| [SRC-1A17F27323-L000261](../../tests/test_firecrawl_connector.py#L261) | 261 | `"    monkeypatch.setenv(\"OMARAI_FIRECRAWL_SEARCH_REQUEST_BUDGET\", \"1\")"` | — |
| [SRC-1A17F27323-L000262](../../tests/test_firecrawl_connector.py#L262) | 262 | `""` | — |
| [SRC-1A17F27323-L000263](../../tests/test_firecrawl_connector.py#L263) | 263 | `"    def unexpected_request(*args, **kwargs):"` | — |
| [SRC-1A17F27323-L000264](../../tests/test_firecrawl_connector.py#L264) | 264 | `"        raise AssertionError("` | — |
| [SRC-1A17F27323-L000265](../../tests/test_firecrawl_connector.py#L265) | 265 | `"            \"Firecrawl defaults to US when geography is omitted; do not make an inferred-country request\""` | — |
| [SRC-1A17F27323-L000266](../../tests/test_firecrawl_connector.py#L266) | 266 | `"        )"` | — |
| [SRC-1A17F27323-L000267](../../tests/test_firecrawl_connector.py#L267) | 267 | `""` | — |
| [SRC-1A17F27323-L000268](../../tests/test_firecrawl_connector.py#L268) | 268 | `"    monkeypatch.setattr(\"agents.web_agent._bounded_http_request\", unexpected_request)"` | — |
| [SRC-1A17F27323-L000269](../../tests/test_firecrawl_connector.py#L269) | 269 | `"    assert WebAgent()._search_firecrawl(\"Find buyers for industrial fire alarms\") == []"` | — |
| [SRC-1A17F27323-L000270](../../tests/test_firecrawl_connector.py#L270) | 270 | `""` | — |
| [SRC-1A17F27323-L000271](../../tests/test_firecrawl_connector.py#L271) | 271 | `""` | — |
| [SRC-1A17F27323-L000272](../../tests/test_firecrawl_connector.py#L272) | 272 | `"def test_search_web_marks_firecrawl_not_attempted_without_explicit_geography(monkeypatch):"` | — |
| [SRC-1A17F27323-L000273](../../tests/test_firecrawl_connector.py#L273) | 273 | `"    agent = WebAgent()"` | — |
| [SRC-1A17F27323-L000274](../../tests/test_firecrawl_connector.py#L274) | 274 | `"    agent.allow_optional_providers = True"` | — |
| [SRC-1A17F27323-L000275](../../tests/test_firecrawl_connector.py#L275) | 275 | `"    monkeypatch.setenv(\"FIRECRAWL_API_KEY\", \"test-firecrawl-secret\")"` | — |
| [SRC-1A17F27323-L000276](../../tests/test_firecrawl_connector.py#L276) | 276 | `"    monkeypatch.setenv(\"FIRECRAWL_SEARCH_ENABLED\", \"1\")"` | — |
| [SRC-1A17F27323-L000277](../../tests/test_firecrawl_connector.py#L277) | 277 | `"    monkeypatch.setenv(\"OMARAI_FIRECRAWL_SEARCH_REQUEST_BUDGET\", \"1\")"` | — |
| [SRC-1A17F27323-L000278](../../tests/test_firecrawl_connector.py#L278) | 278 | `"    for env_name in (\"DEEPSEEK_SEARCH_API_KEY\", \"BRAVE_SEARCH_API_KEY\", \"TAVILY_API_KEY\"):"` | — |
| [SRC-1A17F27323-L000279](../../tests/test_firecrawl_connector.py#L279) | 279 | `"        monkeypatch.delenv(env_name, raising=False)"` | — |
| [SRC-1A17F27323-L000280](../../tests/test_firecrawl_connector.py#L280) | 280 | `"    monkeypatch.setattr(agent, \"_search_duckduckgo_html\", lambda _query: [])"` | — |
| [SRC-1A17F27323-L000281](../../tests/test_firecrawl_connector.py#L281) | 281 | `"    monkeypatch.setattr(agent, \"_search_bing_rss\", lambda _query: [])"` | — |
| [SRC-1A17F27323-L000282](../../tests/test_firecrawl_connector.py#L282) | 282 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda _query: [])"` | — |
| [SRC-1A17F27323-L000283](../../tests/test_firecrawl_connector.py#L283) | 283 | `""` | — |
| [SRC-1A17F27323-L000284](../../tests/test_firecrawl_connector.py#L284) | 284 | `"    def forbidden_firecrawl(_query):"` | — |
| [SRC-1A17F27323-L000285](../../tests/test_firecrawl_connector.py#L285) | 285 | `"        pytest.fail(\"Firecrawl must be skipped if country would be inferred as US\")"` | — |
| [SRC-1A17F27323-L000286](../../tests/test_firecrawl_connector.py#L286) | 286 | `""` | — |
| [SRC-1A17F27323-L000287](../../tests/test_firecrawl_connector.py#L287) | 287 | `"    monkeypatch.setattr(agent, \"_search_firecrawl\", forbidden_firecrawl)"` | — |
| [SRC-1A17F27323-L000288](../../tests/test_firecrawl_connector.py#L288) | 288 | `"    with pytest.raises(RuntimeError, match=\"لم تُرجع موصلات البحث\"):"` | — |
| [SRC-1A17F27323-L000289](../../tests/test_firecrawl_connector.py#L289) | 289 | `"        agent._search_web(\"Find buyers for industrial fire alarms\")"` | — |
| [SRC-1A17F27323-L000290](../../tests/test_firecrawl_connector.py#L290) | 290 | `""` | — |
| [SRC-1A17F27323-L000291](../../tests/test_firecrawl_connector.py#L291) | 291 | `"    diagnostic = next("` | — |
| [SRC-1A17F27323-L000292](../../tests/test_firecrawl_connector.py#L292) | 292 | `"        row for row in agent._provider_diagnostics"` | — |
| [SRC-1A17F27323-L000293](../../tests/test_firecrawl_connector.py#L293) | 293 | `"        if row.get(\"provider\") == \"firecrawl_search_api\""` | — |
| [SRC-1A17F27323-L000294](../../tests/test_firecrawl_connector.py#L294) | 294 | `"    )"` | — |
| [SRC-1A17F27323-L000295](../../tests/test_firecrawl_connector.py#L295) | 295 | `"    assert diagnostic[\"status\"] == \"not_attempted\""` | — |
| [SRC-1A17F27323-L000296](../../tests/test_firecrawl_connector.py#L296) | 296 | `"    assert \"explicit geography\" in diagnostic[\"error\"]"` | — |
## اختبارات

### FILE-FA4E1423C3 — [tests/test_generate_index.py](../../tests/test_generate_index.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-FA4E1423C3-L000001](../../tests/test_generate_index.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-FA4E1423C3-L000002](../../tests/test_generate_index.py#L2) | 2 | `""` | — |
| [SRC-FA4E1423C3-L000003](../../tests/test_generate_index.py#L3) | 3 | `"import importlib.util"` | — |
| [SRC-FA4E1423C3-L000004](../../tests/test_generate_index.py#L4) | 4 | `"from dataclasses import replace"` | — |
| [SRC-FA4E1423C3-L000005](../../tests/test_generate_index.py#L5) | 5 | `"import sys"` | — |
| [SRC-FA4E1423C3-L000006](../../tests/test_generate_index.py#L6) | 6 | `"from pathlib import Path"` | — |
| [SRC-FA4E1423C3-L000007](../../tests/test_generate_index.py#L7) | 7 | `""` | — |
| [SRC-FA4E1423C3-L000008](../../tests/test_generate_index.py#L8) | 8 | `"import pytest"` | — |
| [SRC-FA4E1423C3-L000009](../../tests/test_generate_index.py#L9) | 9 | `""` | — |
| [SRC-FA4E1423C3-L000010](../../tests/test_generate_index.py#L10) | 10 | `""` | — |
| [SRC-FA4E1423C3-L000011](../../tests/test_generate_index.py#L11) | 11 | `"INDEXER_PATH = Path(__file__).resolve().parents[1] / \"docs\" / \"generate_index.py\""` | — |
| [SRC-FA4E1423C3-L000012](../../tests/test_generate_index.py#L12) | 12 | `"INDEXER_SPEC = importlib.util.spec_from_file_location("` | — |
| [SRC-FA4E1423C3-L000013](../../tests/test_generate_index.py#L13) | 13 | `"    \"omarai_generate_index_for_tests\","` | — |
| [SRC-FA4E1423C3-L000014](../../tests/test_generate_index.py#L14) | 14 | `"    INDEXER_PATH,"` | — |
| [SRC-FA4E1423C3-L000015](../../tests/test_generate_index.py#L15) | 15 | `")"` | — |
| [SRC-FA4E1423C3-L000016](../../tests/test_generate_index.py#L16) | 16 | `"assert INDEXER_SPEC is not None"` | — |
| [SRC-FA4E1423C3-L000017](../../tests/test_generate_index.py#L17) | 17 | `"assert INDEXER_SPEC.loader is not None"` | — |
| [SRC-FA4E1423C3-L000018](../../tests/test_generate_index.py#L18) | 18 | `"INDEXER = importlib.util.module_from_spec(INDEXER_SPEC)"` | — |
| [SRC-FA4E1423C3-L000019](../../tests/test_generate_index.py#L19) | 19 | `"sys.modules[INDEXER_SPEC.name] = INDEXER"` | — |
| [SRC-FA4E1423C3-L000020](../../tests/test_generate_index.py#L20) | 20 | `"INDEXER_SPEC.loader.exec_module(INDEXER)"` | — |
| [SRC-FA4E1423C3-L000021](../../tests/test_generate_index.py#L21) | 21 | `""` | — |
| [SRC-FA4E1423C3-L000022](../../tests/test_generate_index.py#L22) | 22 | `""` | — |
| [SRC-FA4E1423C3-L000023](../../tests/test_generate_index.py#L23) | 23 | `"def test_indexes_functions_classes_methods_and_docstring_status(tmp_path: Path) -> None:"` | — |
| [SRC-FA4E1423C3-L000024](../../tests/test_generate_index.py#L24) | 24 | `"    \"\"\"The Python AST index includes qualified names and documentation state.\"\"\""` | — |
| [SRC-FA4E1423C3-L000025](../../tests/test_generate_index.py#L25) | 25 | `"    source_dir = tmp_path / \"src\""` | — |
| [SRC-FA4E1423C3-L000026](../../tests/test_generate_index.py#L26) | 26 | `"    source_dir.mkdir()"` | — |
| [SRC-FA4E1423C3-L000027](../../tests/test_generate_index.py#L27) | 27 | `"    (source_dir / \"sample.py\").write_text("` | — |
| [SRC-FA4E1423C3-L000028](../../tests/test_generate_index.py#L28) | 28 | `"        'class DocumentedClass:\\n'"` | — |
| [SRC-FA4E1423C3-L000029](../../tests/test_generate_index.py#L29) | 29 | `"        '    \"\"\"A documented class.\"\"\"\\n'"` | — |
| [SRC-FA4E1423C3-L000030](../../tests/test_generate_index.py#L30) | 30 | `"        '    def documented_method(self):\\n'"` | — |
| [SRC-FA4E1423C3-L000031](../../tests/test_generate_index.py#L31) | 31 | `"        '        \"\"\"Price \| unit.\"\"\"\\n'"` | — |
| [SRC-FA4E1423C3-L000032](../../tests/test_generate_index.py#L32) | 32 | `"        '        return None\\n\\n'"` | — |
| [SRC-FA4E1423C3-L000033](../../tests/test_generate_index.py#L33) | 33 | `"        'class UndocumentedClass:\\n'"` | — |
| [SRC-FA4E1423C3-L000034](../../tests/test_generate_index.py#L34) | 34 | `"        '    pass\\n\\n'"` | — |
| [SRC-FA4E1423C3-L000035](../../tests/test_generate_index.py#L35) | 35 | `"        'def documented_function():\\n'"` | — |
| [SRC-FA4E1423C3-L000036](../../tests/test_generate_index.py#L36) | 36 | `"        '    \"\"\"A documented function.\"\"\"\\n'"` | — |
| [SRC-FA4E1423C3-L000037](../../tests/test_generate_index.py#L37) | 37 | `"        '    return None\\n\\n'"` | — |
| [SRC-FA4E1423C3-L000038](../../tests/test_generate_index.py#L38) | 38 | `"        'def undocumented_function():\\n'"` | — |
| [SRC-FA4E1423C3-L000039](../../tests/test_generate_index.py#L39) | 39 | `"        '    return None\\n\\n'"` | — |
| [SRC-FA4E1423C3-L000040](../../tests/test_generate_index.py#L40) | 40 | `"        'async def async_function():\\n'"` | — |
| [SRC-FA4E1423C3-L000041](../../tests/test_generate_index.py#L41) | 41 | `"        '    \"\"\"An asynchronous function.\"\"\"\\n'"` | — |
| [SRC-FA4E1423C3-L000042](../../tests/test_generate_index.py#L42) | 42 | `"        '    return None\\n',"` | — |
| [SRC-FA4E1423C3-L000043](../../tests/test_generate_index.py#L43) | 43 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000044](../../tests/test_generate_index.py#L44) | 44 | `"    )"` | — |
| [SRC-FA4E1423C3-L000045](../../tests/test_generate_index.py#L45) | 45 | `""` | — |
| [SRC-FA4E1423C3-L000046](../../tests/test_generate_index.py#L46) | 46 | `"    symbols, files_scanned = INDEXER.scan_repository(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000047](../../tests/test_generate_index.py#L47) | 47 | `"    by_name = {symbol.name: symbol for symbol in symbols}"` | — |
| [SRC-FA4E1423C3-L000048](../../tests/test_generate_index.py#L48) | 48 | `"    markdown = INDEXER.render_markdown(symbols, files_scanned)"` | — |
| [SRC-FA4E1423C3-L000049](../../tests/test_generate_index.py#L49) | 49 | `""` | — |
| [SRC-FA4E1423C3-L000050](../../tests/test_generate_index.py#L50) | 50 | `"    assert files_scanned == 1"` | — |
| [SRC-FA4E1423C3-L000051](../../tests/test_generate_index.py#L51) | 51 | `"    assert by_name[\"DocumentedClass\"].documented is True"` | — |
| [SRC-FA4E1423C3-L000052](../../tests/test_generate_index.py#L52) | 52 | `"    assert by_name[\"DocumentedClass.documented_method\"].documented is True"` | — |
| [SRC-FA4E1423C3-L000053](../../tests/test_generate_index.py#L53) | 53 | `"    assert by_name[\"UndocumentedClass\"].documented is False"` | — |
| [SRC-FA4E1423C3-L000054](../../tests/test_generate_index.py#L54) | 54 | `"    assert by_name[\"documented_function\"].documented is True"` | — |
| [SRC-FA4E1423C3-L000055](../../tests/test_generate_index.py#L55) | 55 | `"    assert by_name[\"undocumented_function\"].documented is False"` | — |
| [SRC-FA4E1423C3-L000056](../../tests/test_generate_index.py#L56) | 56 | `"    assert by_name[\"async_function\"].kind == \"دالة غير متزامنة\""` | — |
| [SRC-FA4E1423C3-L000057](../../tests/test_generate_index.py#L57) | 57 | `"    assert \"Price \\\\\| unit.\" in markdown"` | — |
| [SRC-FA4E1423C3-L000058](../../tests/test_generate_index.py#L58) | 58 | `"    assert \"\| موثق \|\" in markdown"` | — |
| [SRC-FA4E1423C3-L000059](../../tests/test_generate_index.py#L59) | 59 | `"    assert \"\| ناقص \|\" in markdown"` | — |
| [SRC-FA4E1423C3-L000060](../../tests/test_generate_index.py#L60) | 60 | `""` | — |
| [SRC-FA4E1423C3-L000061](../../tests/test_generate_index.py#L61) | 61 | `""` | — |
| [SRC-FA4E1423C3-L000062](../../tests/test_generate_index.py#L62) | 62 | `"def test_indexes_module_and_class_assignments_but_not_function_locals("` | — |
| [SRC-FA4E1423C3-L000063](../../tests/test_generate_index.py#L63) | 63 | `"    tmp_path: Path,"` | — |
| [SRC-FA4E1423C3-L000064](../../tests/test_generate_index.py#L64) | 64 | `") -> None:"` | — |
| [SRC-FA4E1423C3-L000065](../../tests/test_generate_index.py#L65) | 65 | `"    \"\"\"Module/class attributes are searchable without flooding the index with locals.\"\"\""` | — |
| [SRC-FA4E1423C3-L000066](../../tests/test_generate_index.py#L66) | 66 | `"    (tmp_path / \"settings.py\").write_text("` | — |
| [SRC-FA4E1423C3-L000067](../../tests/test_generate_index.py#L67) | 67 | `"        'MODULE_SETTING = \"enabled\"\\n'"` | — |
| [SRC-FA4E1423C3-L000068](../../tests/test_generate_index.py#L68) | 68 | `"        'class Settings:\\n'"` | — |
| [SRC-FA4E1423C3-L000069](../../tests/test_generate_index.py#L69) | 69 | `"        '    CLASS_SETTING: str = \"strict\"\\n'"` | — |
| [SRC-FA4E1423C3-L000070](../../tests/test_generate_index.py#L70) | 70 | `"        '    def method(self):\\n'"` | — |
| [SRC-FA4E1423C3-L000071](../../tests/test_generate_index.py#L71) | 71 | `"        '        local_only = \"do not index\"\\n'"` | — |
| [SRC-FA4E1423C3-L000072](../../tests/test_generate_index.py#L72) | 72 | `"        '        return local_only\\n',"` | — |
| [SRC-FA4E1423C3-L000073](../../tests/test_generate_index.py#L73) | 73 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000074](../../tests/test_generate_index.py#L74) | 74 | `"    )"` | — |
| [SRC-FA4E1423C3-L000075](../../tests/test_generate_index.py#L75) | 75 | `""` | — |
| [SRC-FA4E1423C3-L000076](../../tests/test_generate_index.py#L76) | 76 | `"    symbols, _ = INDEXER.scan_repository(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000077](../../tests/test_generate_index.py#L77) | 77 | `"    by_name = {symbol.name: symbol for symbol in symbols}"` | — |
| [SRC-FA4E1423C3-L000078](../../tests/test_generate_index.py#L78) | 78 | `""` | — |
| [SRC-FA4E1423C3-L000079](../../tests/test_generate_index.py#L79) | 79 | `"    assert by_name[\"MODULE_SETTING\"].kind == \"متغير/ثابت Python\""` | — |
| [SRC-FA4E1423C3-L000080](../../tests/test_generate_index.py#L80) | 80 | `"    assert by_name[\"MODULE_SETTING\"].documented is None"` | — |
| [SRC-FA4E1423C3-L000081](../../tests/test_generate_index.py#L81) | 81 | `"    assert by_name[\"Settings.CLASS_SETTING\"].kind == \"متغير/ثابت Python\""` | — |
| [SRC-FA4E1423C3-L000082](../../tests/test_generate_index.py#L82) | 82 | `"    assert \"local_only\" not in by_name"` | — |
| [SRC-FA4E1423C3-L000083](../../tests/test_generate_index.py#L83) | 83 | `""` | — |
| [SRC-FA4E1423C3-L000084](../../tests/test_generate_index.py#L84) | 84 | `""` | — |
| [SRC-FA4E1423C3-L000085](../../tests/test_generate_index.py#L85) | 85 | `"def test_indexes_frontend_ids_javascript_symbols_css_and_documentation_headings("` | — |
| [SRC-FA4E1423C3-L000086](../../tests/test_generate_index.py#L86) | 86 | `"    tmp_path: Path,"` | — |
| [SRC-FA4E1423C3-L000087](../../tests/test_generate_index.py#L87) | 87 | `") -> None:"` | — |
| [SRC-FA4E1423C3-L000088](../../tests/test_generate_index.py#L88) | 88 | `"    \"\"\"Frontend declarations and Markdown headings remain navigable without language parsers.\"\"\""` | — |
| [SRC-FA4E1423C3-L000089](../../tests/test_generate_index.py#L89) | 89 | `"    web_dir = tmp_path / \"web\""` | — |
| [SRC-FA4E1423C3-L000090](../../tests/test_generate_index.py#L90) | 90 | `"    docs_dir = tmp_path / \"docs\""` | — |
| [SRC-FA4E1423C3-L000091](../../tests/test_generate_index.py#L91) | 91 | `"    web_dir.mkdir()"` | — |
| [SRC-FA4E1423C3-L000092](../../tests/test_generate_index.py#L92) | 92 | `"    docs_dir.mkdir()"` | — |
| [SRC-FA4E1423C3-L000093](../../tests/test_generate_index.py#L93) | 93 | `"    (web_dir / \"agent.html\").write_text("` | — |
| [SRC-FA4E1423C3-L000094](../../tests/test_generate_index.py#L94) | 94 | `"        '<div id=\"chat-panel\" name=\"question-box\" data-testid=\"send-button\"></div>\\n'"` | — |
| [SRC-FA4E1423C3-L000095](../../tests/test_generate_index.py#L95) | 95 | `"        \"<style>\\n\""` | — |
| [SRC-FA4E1423C3-L000096](../../tests/test_generate_index.py#L96) | 96 | `"        \".chat-panel { --accent-color: #fff; }\\n\""` | — |
| [SRC-FA4E1423C3-L000097](../../tests/test_generate_index.py#L97) | 97 | `"        \"#answer-panel { display: block; }\\n\""` | — |
| [SRC-FA4E1423C3-L000098](../../tests/test_generate_index.py#L98) | 98 | `"        \"</style>\\n\""` | — |
| [SRC-FA4E1423C3-L000099](../../tests/test_generate_index.py#L99) | 99 | `"        \"<script>\\n\""` | — |
| [SRC-FA4E1423C3-L000100](../../tests/test_generate_index.py#L100) | 100 | `"        \"function sendMessage() { return true; }\\n\""` | — |
| [SRC-FA4E1423C3-L000101](../../tests/test_generate_index.py#L101) | 101 | `"        \"class AgentCore {}\\n\""` | — |
| [SRC-FA4E1423C3-L000102](../../tests/test_generate_index.py#L102) | 102 | `"        \"const fetchAnswer = async (question) => question;\\n\""` | — |
| [SRC-FA4E1423C3-L000103](../../tests/test_generate_index.py#L103) | 103 | `"        \"const ACCESS_TOKEN = 'example';\\n\""` | — |
| [SRC-FA4E1423C3-L000104](../../tests/test_generate_index.py#L104) | 104 | `"        \"</script>\\n\","` | — |
| [SRC-FA4E1423C3-L000105](../../tests/test_generate_index.py#L105) | 105 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000106](../../tests/test_generate_index.py#L106) | 106 | `"    )"` | — |
| [SRC-FA4E1423C3-L000107](../../tests/test_generate_index.py#L107) | 107 | `"    (docs_dir / \"guide.md\").write_text("` | — |
| [SRC-FA4E1423C3-L000108](../../tests/test_generate_index.py#L108) | 108 | `"        \"# User Guide\\n## Troubleshooting\\n\","` | — |
| [SRC-FA4E1423C3-L000109](../../tests/test_generate_index.py#L109) | 109 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000110](../../tests/test_generate_index.py#L110) | 110 | `"    )"` | — |
| [SRC-FA4E1423C3-L000111](../../tests/test_generate_index.py#L111) | 111 | `"    (tmp_path / \"settings.yml\").write_text("` | — |
| [SRC-FA4E1423C3-L000112](../../tests/test_generate_index.py#L112) | 112 | `"        \"OMARAI_ENABLED: true\\nrequest-budget:\\n  max-calls: 3\\n\","` | — |
| [SRC-FA4E1423C3-L000113](../../tests/test_generate_index.py#L113) | 113 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000114](../../tests/test_generate_index.py#L114) | 114 | `"    )"` | — |
| [SRC-FA4E1423C3-L000115](../../tests/test_generate_index.py#L115) | 115 | `""` | — |
| [SRC-FA4E1423C3-L000116](../../tests/test_generate_index.py#L116) | 116 | `"    inventory = INDEXER.build_file_inventory(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000117](../../tests/test_generate_index.py#L117) | 117 | `"    symbols = INDEXER.scan_static_symbols(tmp_path, inventory)"` | — |
| [SRC-FA4E1423C3-L000118](../../tests/test_generate_index.py#L118) | 118 | `"    names_by_kind = {(symbol.kind, symbol.name) for symbol in symbols}"` | — |
| [SRC-FA4E1423C3-L000119](../../tests/test_generate_index.py#L119) | 119 | `""` | — |
| [SRC-FA4E1423C3-L000120](../../tests/test_generate_index.py#L120) | 120 | `"    assert (\"قيمة سمة HTML (id)\", \"chat-panel\") in names_by_kind"` | — |
| [SRC-FA4E1423C3-L000121](../../tests/test_generate_index.py#L121) | 121 | `"    assert (\"قيمة سمة HTML (name)\", \"question-box\") in names_by_kind"` | — |
| [SRC-FA4E1423C3-L000122](../../tests/test_generate_index.py#L122) | 122 | `"    assert (\"قيمة سمة HTML (data-testid)\", \"send-button\") in names_by_kind"` | — |
| [SRC-FA4E1423C3-L000123](../../tests/test_generate_index.py#L123) | 123 | `"    assert (\"دالة JavaScript/TypeScript\", \"sendMessage\") in names_by_kind"` | — |
| [SRC-FA4E1423C3-L000124](../../tests/test_generate_index.py#L124) | 124 | `"    assert (\"كلاس JavaScript/TypeScript\", \"AgentCore\") in names_by_kind"` | — |
| [SRC-FA4E1423C3-L000125](../../tests/test_generate_index.py#L125) | 125 | `"    assert (\"دالة JavaScript/TypeScript\", \"fetchAnswer\") in names_by_kind"` | — |
| [SRC-FA4E1423C3-L000126](../../tests/test_generate_index.py#L126) | 126 | `"    assert (\"متغير JavaScript/TypeScript\", \"ACCESS_TOKEN\") in names_by_kind"` | — |
| [SRC-FA4E1423C3-L000127](../../tests/test_generate_index.py#L127) | 127 | `"    assert (\"محدد class في CSS\", \"chat-panel\") in names_by_kind"` | — |
| [SRC-FA4E1423C3-L000128](../../tests/test_generate_index.py#L128) | 128 | `"    assert (\"محدد id في CSS\", \"answer-panel\") in names_by_kind"` | — |
| [SRC-FA4E1423C3-L000129](../../tests/test_generate_index.py#L129) | 129 | `"    assert (\"متغير CSS مخصص\", \"accent-color\") in names_by_kind"` | — |
| [SRC-FA4E1423C3-L000130](../../tests/test_generate_index.py#L130) | 130 | `"    assert (\"عنوان Markdown (H1)\", \"User Guide\") in names_by_kind"` | — |
| [SRC-FA4E1423C3-L000131](../../tests/test_generate_index.py#L131) | 131 | `"    assert (\"عنوان Markdown (H2)\", \"Troubleshooting\") in names_by_kind"` | — |
| [SRC-FA4E1423C3-L000132](../../tests/test_generate_index.py#L132) | 132 | `"    assert (\"مفتاح إعداد YAML\", \"OMARAI_ENABLED\") in names_by_kind"` | — |
| [SRC-FA4E1423C3-L000133](../../tests/test_generate_index.py#L133) | 133 | `"    assert (\"اسم ثابت/إعداد بصيغة UPPER_SNAKE_CASE\", \"OMARAI_ENABLED\") in names_by_kind"` | — |
| [SRC-FA4E1423C3-L000134](../../tests/test_generate_index.py#L134) | 134 | `""` | — |
| [SRC-FA4E1423C3-L000135](../../tests/test_generate_index.py#L135) | 135 | `""` | — |
| [SRC-FA4E1423C3-L000136](../../tests/test_generate_index.py#L136) | 136 | `"def test_repository_inventory_covers_files_and_excludes_private_runtime_paths("` | — |
| [SRC-FA4E1423C3-L000137](../../tests/test_generate_index.py#L137) | 137 | `"    tmp_path: Path,"` | — |
| [SRC-FA4E1423C3-L000138](../../tests/test_generate_index.py#L138) | 138 | `") -> None:"` | — |
| [SRC-FA4E1423C3-L000139](../../tests/test_generate_index.py#L139) | 139 | `"    \"\"\"The file inventory includes docs/config and excludes known local secret/runtime files.\"\"\""` | — |
| [SRC-FA4E1423C3-L000140](../../tests/test_generate_index.py#L140) | 140 | `"    (tmp_path / \"app.py\").write_text(\"VALUE = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000141](../../tests/test_generate_index.py#L141) | 141 | `"    docs_dir = tmp_path / \"docs\""` | — |
| [SRC-FA4E1423C3-L000142](../../tests/test_generate_index.py#L142) | 142 | `"    docs_dir.mkdir()"` | — |
| [SRC-FA4E1423C3-L000143](../../tests/test_generate_index.py#L143) | 143 | `"    (docs_dir / \"guide.md\").write_text(\"# Guide\\n\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000144](../../tests/test_generate_index.py#L144) | 144 | `"    (tmp_path / \".env\").write_text(\"OPENROUTER_API_KEY=private-value\\n\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000145](../../tests/test_generate_index.py#L145) | 145 | `"    (tmp_path / \".env.example\").write_text("` | — |
| [SRC-FA4E1423C3-L000146](../../tests/test_generate_index.py#L146) | 146 | `"        \"OPENROUTER_API_KEY=replace-me\\n\", encoding=\"utf-8\""` | — |
| [SRC-FA4E1423C3-L000147](../../tests/test_generate_index.py#L147) | 147 | `"    )"` | — |
| [SRC-FA4E1423C3-L000148](../../tests/test_generate_index.py#L148) | 148 | `"    (tmp_path / \"local.sqlite3\").write_bytes(b\"not a real database\")"` | — |
| [SRC-FA4E1423C3-L000149](../../tests/test_generate_index.py#L149) | 149 | `"    (tmp_path / \"logo.bin\").write_bytes(b\"\\x00\\x01\\x02\")"` | — |
| [SRC-FA4E1423C3-L000150](../../tests/test_generate_index.py#L150) | 150 | `""` | — |
| [SRC-FA4E1423C3-L000151](../../tests/test_generate_index.py#L151) | 151 | `"    inventory = INDEXER.build_file_inventory(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000152](../../tests/test_generate_index.py#L152) | 152 | `"    paths = {item.file for item in inventory}"` | — |
| [SRC-FA4E1423C3-L000153](../../tests/test_generate_index.py#L153) | 153 | `"    by_path = {item.file: item for item in inventory}"` | — |
| [SRC-FA4E1423C3-L000154](../../tests/test_generate_index.py#L154) | 154 | `""` | — |
| [SRC-FA4E1423C3-L000155](../../tests/test_generate_index.py#L155) | 155 | `"    assert \"app.py\" in paths"` | — |
| [SRC-FA4E1423C3-L000156](../../tests/test_generate_index.py#L156) | 156 | `"    assert \"docs/guide.md\" in paths"` | — |
| [SRC-FA4E1423C3-L000157](../../tests/test_generate_index.py#L157) | 157 | `"    assert \".env.example\" in paths"` | — |
| [SRC-FA4E1423C3-L000158](../../tests/test_generate_index.py#L158) | 158 | `"    assert \".env\" not in paths"` | — |
| [SRC-FA4E1423C3-L000159](../../tests/test_generate_index.py#L159) | 159 | `"    assert \"local.sqlite3\" not in paths"` | — |
| [SRC-FA4E1423C3-L000160](../../tests/test_generate_index.py#L160) | 160 | `"    assert \"logo.bin\" in paths"` | — |
| [SRC-FA4E1423C3-L000161](../../tests/test_generate_index.py#L161) | 161 | `"    assert by_path[\"logo.bin\"].line_count is None"` | — |
| [SRC-FA4E1423C3-L000162](../../tests/test_generate_index.py#L162) | 162 | `""` | — |
| [SRC-FA4E1423C3-L000163](../../tests/test_generate_index.py#L163) | 163 | `""` | — |
| [SRC-FA4E1423C3-L000164](../../tests/test_generate_index.py#L164) | 164 | `"def test_skips_virtual_environments_and_generated_dependency_directories("` | — |
| [SRC-FA4E1423C3-L000165](../../tests/test_generate_index.py#L165) | 165 | `"    tmp_path: Path,"` | — |
| [SRC-FA4E1423C3-L000166](../../tests/test_generate_index.py#L166) | 166 | `") -> None:"` | — |
| [SRC-FA4E1423C3-L000167](../../tests/test_generate_index.py#L167) | 167 | `"    \"\"\"The scan avoids vendored dependencies, build outputs, and virtual environments.\"\"\""` | — |
| [SRC-FA4E1423C3-L000168](../../tests/test_generate_index.py#L168) | 168 | `"    (tmp_path / \"app.py\").write_text("` | — |
| [SRC-FA4E1423C3-L000169](../../tests/test_generate_index.py#L169) | 169 | `"        'def application_entry():\\n    \"\"\"Main entry point.\"\"\"\\n',"` | — |
| [SRC-FA4E1423C3-L000170](../../tests/test_generate_index.py#L170) | 170 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000171](../../tests/test_generate_index.py#L171) | 171 | `"    )"` | — |
| [SRC-FA4E1423C3-L000172](../../tests/test_generate_index.py#L172) | 172 | `"    excluded_files = ("` | — |
| [SRC-FA4E1423C3-L000173](../../tests/test_generate_index.py#L173) | 173 | `"        tmp_path / \".venv\" / \"lib\" / \"hidden.py\","` | — |
| [SRC-FA4E1423C3-L000174](../../tests/test_generate_index.py#L174) | 174 | `"        tmp_path / \"node_modules\" / \"package\" / \"hidden.py\","` | — |
| [SRC-FA4E1423C3-L000175](../../tests/test_generate_index.py#L175) | 175 | `"        tmp_path / \"build\" / \"generated.py\","` | — |
| [SRC-FA4E1423C3-L000176](../../tests/test_generate_index.py#L176) | 176 | `"        tmp_path / \"omarai_agent.egg-info\" / \"PKG-INFO\","` | — |
| [SRC-FA4E1423C3-L000177](../../tests/test_generate_index.py#L177) | 177 | `"        tmp_path / \"package.dist-info\" / \"METADATA\","` | — |
| [SRC-FA4E1423C3-L000178](../../tests/test_generate_index.py#L178) | 178 | `"    )"` | — |
| [SRC-FA4E1423C3-L000179](../../tests/test_generate_index.py#L179) | 179 | `"    for path in excluded_files:"` | — |
| [SRC-FA4E1423C3-L000180](../../tests/test_generate_index.py#L180) | 180 | `"        path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-FA4E1423C3-L000181](../../tests/test_generate_index.py#L181) | 181 | `"        path.write_text(\"def should_not_be_indexed():\\n    pass\\n\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000182](../../tests/test_generate_index.py#L182) | 182 | `""` | — |
| [SRC-FA4E1423C3-L000183](../../tests/test_generate_index.py#L183) | 183 | `"    symbols, files_scanned = INDEXER.scan_repository(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000184](../../tests/test_generate_index.py#L184) | 184 | `""` | — |
| [SRC-FA4E1423C3-L000185](../../tests/test_generate_index.py#L185) | 185 | `"    assert files_scanned == 1"` | — |
| [SRC-FA4E1423C3-L000186](../../tests/test_generate_index.py#L186) | 186 | `"    assert [symbol.name for symbol in symbols] == [\"application_entry\"]"` | — |
| [SRC-FA4E1423C3-L000187](../../tests/test_generate_index.py#L187) | 187 | `"    inventory_paths = {item.file for item in INDEXER.build_file_inventory(tmp_path)}"` | — |
| [SRC-FA4E1423C3-L000188](../../tests/test_generate_index.py#L188) | 188 | `"    assert not any(\".egg-info/\" in path for path in inventory_paths)"` | — |
| [SRC-FA4E1423C3-L000189](../../tests/test_generate_index.py#L189) | 189 | `"    assert not any(\".dist-info/\" in path for path in inventory_paths)"` | — |
| [SRC-FA4E1423C3-L000190](../../tests/test_generate_index.py#L190) | 190 | `""` | — |
| [SRC-FA4E1423C3-L000191](../../tests/test_generate_index.py#L191) | 191 | `""` | — |
| [SRC-FA4E1423C3-L000192](../../tests/test_generate_index.py#L192) | 192 | `"def test_syntax_error_does_not_overwrite_the_previous_index("` | — |
| [SRC-FA4E1423C3-L000193](../../tests/test_generate_index.py#L193) | 193 | `"    tmp_path: Path,"` | — |
| [SRC-FA4E1423C3-L000194](../../tests/test_generate_index.py#L194) | 194 | `"    capsys,"` | — |
| [SRC-FA4E1423C3-L000195](../../tests/test_generate_index.py#L195) | 195 | `") -> None:"` | — |
| [SRC-FA4E1423C3-L000196](../../tests/test_generate_index.py#L196) | 196 | `"    \"\"\"A failed parse leaves the prior index intact rather than publishing partial data.\"\"\""` | — |
| [SRC-FA4E1423C3-L000197](../../tests/test_generate_index.py#L197) | 197 | `"    docs_dir = tmp_path / \"docs\""` | — |
| [SRC-FA4E1423C3-L000198](../../tests/test_generate_index.py#L198) | 198 | `"    docs_dir.mkdir()"` | — |
| [SRC-FA4E1423C3-L000199](../../tests/test_generate_index.py#L199) | 199 | `"    index_path = docs_dir / \"MASTER_INDEX.md\""` | — |
| [SRC-FA4E1423C3-L000200](../../tests/test_generate_index.py#L200) | 200 | `"    index_path.write_text(\"previous index must survive\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000201](../../tests/test_generate_index.py#L201) | 201 | `"    (tmp_path / \"broken.py\").write_text("` | — |
| [SRC-FA4E1423C3-L000202](../../tests/test_generate_index.py#L202) | 202 | `"        \"def incomplete(:\\n    pass\\n\","` | — |
| [SRC-FA4E1423C3-L000203](../../tests/test_generate_index.py#L203) | 203 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000204](../../tests/test_generate_index.py#L204) | 204 | `"    )"` | — |
| [SRC-FA4E1423C3-L000205](../../tests/test_generate_index.py#L205) | 205 | `""` | — |
| [SRC-FA4E1423C3-L000206](../../tests/test_generate_index.py#L206) | 206 | `"    result = INDEXER.main([\"--root\", str(tmp_path)])"` | — |
| [SRC-FA4E1423C3-L000207](../../tests/test_generate_index.py#L207) | 207 | `""` | — |
| [SRC-FA4E1423C3-L000208](../../tests/test_generate_index.py#L208) | 208 | `"    assert result == 1"` | — |
| [SRC-FA4E1423C3-L000209](../../tests/test_generate_index.py#L209) | 209 | `"    assert index_path.read_text(encoding=\"utf-8\") == \"previous index must survive\""` | — |
| [SRC-FA4E1423C3-L000210](../../tests/test_generate_index.py#L210) | 210 | `"    assert \"لم يُكتب MASTER_INDEX.md\" in capsys.readouterr().err"` | — |
| [SRC-FA4E1423C3-L000211](../../tests/test_generate_index.py#L211) | 211 | `""` | — |
| [SRC-FA4E1423C3-L000212](../../tests/test_generate_index.py#L212) | 212 | `""` | — |
| [SRC-FA4E1423C3-L000213](../../tests/test_generate_index.py#L213) | 213 | `"def test_repeated_generation_is_deterministic_and_does_not_rewrite_unchanged_index("` | — |
| [SRC-FA4E1423C3-L000214](../../tests/test_generate_index.py#L214) | 214 | `"    tmp_path: Path,"` | — |
| [SRC-FA4E1423C3-L000215](../../tests/test_generate_index.py#L215) | 215 | `") -> None:"` | — |
| [SRC-FA4E1423C3-L000216](../../tests/test_generate_index.py#L216) | 216 | `"    \"\"\"An unchanged scan produces identical Markdown and avoids an unnecessary write.\"\"\""` | — |
| [SRC-FA4E1423C3-L000217](../../tests/test_generate_index.py#L217) | 217 | `"    (tmp_path / \"app.py\").write_text("` | — |
| [SRC-FA4E1423C3-L000218](../../tests/test_generate_index.py#L218) | 218 | `"        'def entry():\\n    \"\"\"Entry point.\"\"\"\\n', encoding=\"utf-8\""` | — |
| [SRC-FA4E1423C3-L000219](../../tests/test_generate_index.py#L219) | 219 | `"    )"` | — |
| [SRC-FA4E1423C3-L000220](../../tests/test_generate_index.py#L220) | 220 | `"    first_symbols, first_count = INDEXER.scan_repository(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000221](../../tests/test_generate_index.py#L221) | 221 | `"    second_symbols, second_count = INDEXER.scan_repository(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000222](../../tests/test_generate_index.py#L222) | 222 | `"    first_inventory = INDEXER.build_file_inventory(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000223](../../tests/test_generate_index.py#L223) | 223 | `"    second_inventory = INDEXER.build_file_inventory(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000224](../../tests/test_generate_index.py#L224) | 224 | `"    first_static = INDEXER.scan_static_symbols(tmp_path, first_inventory)"` | — |
| [SRC-FA4E1423C3-L000225](../../tests/test_generate_index.py#L225) | 225 | `"    second_static = INDEXER.scan_static_symbols(tmp_path, second_inventory)"` | — |
| [SRC-FA4E1423C3-L000226](../../tests/test_generate_index.py#L226) | 226 | `"    first_markdown = INDEXER.render_markdown("` | — |
| [SRC-FA4E1423C3-L000227](../../tests/test_generate_index.py#L227) | 227 | `"        first_symbols, first_count, first_inventory, first_static"` | — |
| [SRC-FA4E1423C3-L000228](../../tests/test_generate_index.py#L228) | 228 | `"    )"` | — |
| [SRC-FA4E1423C3-L000229](../../tests/test_generate_index.py#L229) | 229 | `"    second_markdown = INDEXER.render_markdown("` | — |
| [SRC-FA4E1423C3-L000230](../../tests/test_generate_index.py#L230) | 230 | `"        second_symbols, second_count, second_inventory, second_static"` | — |
| [SRC-FA4E1423C3-L000231](../../tests/test_generate_index.py#L231) | 231 | `"    )"` | — |
| [SRC-FA4E1423C3-L000232](../../tests/test_generate_index.py#L232) | 232 | `"    output_path = tmp_path / \"docs\" / \"MASTER_INDEX.md\""` | — |
| [SRC-FA4E1423C3-L000233](../../tests/test_generate_index.py#L233) | 233 | `""` | — |
| [SRC-FA4E1423C3-L000234](../../tests/test_generate_index.py#L234) | 234 | `"    assert first_markdown == second_markdown"` | — |
| [SRC-FA4E1423C3-L000235](../../tests/test_generate_index.py#L235) | 235 | `"    assert INDEXER.write_if_changed(output_path, first_markdown) is True"` | — |
| [SRC-FA4E1423C3-L000236](../../tests/test_generate_index.py#L236) | 236 | `"    assert INDEXER.write_if_changed(output_path, second_markdown) is False"` | — |
| [SRC-FA4E1423C3-L000237](../../tests/test_generate_index.py#L237) | 237 | `""` | — |
| [SRC-FA4E1423C3-L000238](../../tests/test_generate_index.py#L238) | 238 | `""` | — |
| [SRC-FA4E1423C3-L000239](../../tests/test_generate_index.py#L239) | 239 | `"def test_check_mode_detects_stale_index_without_modifying_it(tmp_path: Path, capsys) -> None:"` | — |
| [SRC-FA4E1423C3-L000240](../../tests/test_generate_index.py#L240) | 240 | `"    \"\"\"Check mode fails on a stale index and leaves the existing file untouched.\"\"\""` | — |
| [SRC-FA4E1423C3-L000241](../../tests/test_generate_index.py#L241) | 241 | `"    (tmp_path / \"app.py\").write_text(\"VALUE = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000242](../../tests/test_generate_index.py#L242) | 242 | `"    docs_dir = tmp_path / \"docs\""` | — |
| [SRC-FA4E1423C3-L000243](../../tests/test_generate_index.py#L243) | 243 | `"    docs_dir.mkdir()"` | — |
| [SRC-FA4E1423C3-L000244](../../tests/test_generate_index.py#L244) | 244 | `"    index_path = docs_dir / \"MASTER_INDEX.md\""` | — |
| [SRC-FA4E1423C3-L000245](../../tests/test_generate_index.py#L245) | 245 | `"    index_path.write_text(\"stale\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000246](../../tests/test_generate_index.py#L246) | 246 | `""` | — |
| [SRC-FA4E1423C3-L000247](../../tests/test_generate_index.py#L247) | 247 | `"    assert INDEXER.main([\"--root\", str(tmp_path), \"--check\"]) == 1"` | — |
| [SRC-FA4E1423C3-L000248](../../tests/test_generate_index.py#L248) | 248 | `"    assert index_path.read_text(encoding=\"utf-8\") == \"stale\""` | — |
| [SRC-FA4E1423C3-L000249](../../tests/test_generate_index.py#L249) | 249 | `"    assert \"الفهرس قديم\" in capsys.readouterr().err"` | — |
| [SRC-FA4E1423C3-L000250](../../tests/test_generate_index.py#L250) | 250 | `""` | — |
| [SRC-FA4E1423C3-L000251](../../tests/test_generate_index.py#L251) | 251 | `"    assert INDEXER.main([\"--root\", str(tmp_path)]) == 0"` | — |
| [SRC-FA4E1423C3-L000252](../../tests/test_generate_index.py#L252) | 252 | `"    assert INDEXER.main([\"--root\", str(tmp_path), \"--check\"]) == 0"` | — |
| [SRC-FA4E1423C3-L000253](../../tests/test_generate_index.py#L253) | 253 | `""` | — |
| [SRC-FA4E1423C3-L000254](../../tests/test_generate_index.py#L254) | 254 | `""` | — |
| [SRC-FA4E1423C3-L000255](../../tests/test_generate_index.py#L255) | 255 | `"def test_indexes_every_eligible_text_line_with_file_and_line_ids(tmp_path: Path) -> None:"` | — |
| [SRC-FA4E1423C3-L000256](../../tests/test_generate_index.py#L256) | 256 | `"    \"\"\"All readable text lines, including blank lines and unfamiliar extensions, are searchable.\"\"\""` | — |
| [SRC-FA4E1423C3-L000257](../../tests/test_generate_index.py#L257) | 257 | `"    (tmp_path / \"app.py\").write_text("` | — |
| [SRC-FA4E1423C3-L000258](../../tests/test_generate_index.py#L258) | 258 | `"        'VALUE = 1\\n\\n'"` | — |
| [SRC-FA4E1423C3-L000259](../../tests/test_generate_index.py#L259) | 259 | `"        'def greet():\\n'"` | — |
| [SRC-FA4E1423C3-L000260](../../tests/test_generate_index.py#L260) | 260 | `"        '    return \"hello\"\\n',"` | — |
| [SRC-FA4E1423C3-L000261](../../tests/test_generate_index.py#L261) | 261 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000262](../../tests/test_generate_index.py#L262) | 262 | `"    )"` | — |
| [SRC-FA4E1423C3-L000263](../../tests/test_generate_index.py#L263) | 263 | `"    docs_dir = tmp_path / \"docs\""` | — |
| [SRC-FA4E1423C3-L000264](../../tests/test_generate_index.py#L264) | 264 | `"    docs_dir.mkdir()"` | — |
| [SRC-FA4E1423C3-L000265](../../tests/test_generate_index.py#L265) | 265 | `"    (docs_dir / \"guide.txt\").write_text("` | — |
| [SRC-FA4E1423C3-L000266](../../tests/test_generate_index.py#L266) | 266 | `"        \"First documented step.\\nSecond documented step.\\n\","` | — |
| [SRC-FA4E1423C3-L000267](../../tests/test_generate_index.py#L267) | 267 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000268](../../tests/test_generate_index.py#L268) | 268 | `"    )"` | — |
| [SRC-FA4E1423C3-L000269](../../tests/test_generate_index.py#L269) | 269 | `"    (tmp_path / \".env\").write_text(\"PRIVATE_TOKEN=do-not-index\\n\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000270](../../tests/test_generate_index.py#L270) | 270 | `"    (tmp_path / \"payload.bin\").write_bytes(b\"\\x00\\x01\\x02\")"` | — |
| [SRC-FA4E1423C3-L000271](../../tests/test_generate_index.py#L271) | 271 | `""` | — |
| [SRC-FA4E1423C3-L000272](../../tests/test_generate_index.py#L272) | 272 | `"    inventory = INDEXER.build_file_inventory(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000273](../../tests/test_generate_index.py#L273) | 273 | `"    source_lines = INDEXER.scan_source_lines(tmp_path, inventory)"` | — |
| [SRC-FA4E1423C3-L000274](../../tests/test_generate_index.py#L274) | 274 | `"    findings = INDEXER.scan_finding_annotations(source_lines)"` | — |
| [SRC-FA4E1423C3-L000275](../../tests/test_generate_index.py#L275) | 275 | `"    line_by_file_and_number = {(line.file, line.line): line for line in source_lines}"` | — |
| [SRC-FA4E1423C3-L000276](../../tests/test_generate_index.py#L276) | 276 | `"    pages, pages_by_file = INDEXER.render_source_line_pages(source_lines, inventory, findings)"` | — |
| [SRC-FA4E1423C3-L000277](../../tests/test_generate_index.py#L277) | 277 | `"    lines_markdown = INDEXER.render_source_lines_markdown("` | — |
| [SRC-FA4E1423C3-L000278](../../tests/test_generate_index.py#L278) | 278 | `"        source_lines, inventory, findings, pages_by_file, pages"` | — |
| [SRC-FA4E1423C3-L000279](../../tests/test_generate_index.py#L279) | 279 | `"    )"` | — |
| [SRC-FA4E1423C3-L000280](../../tests/test_generate_index.py#L280) | 280 | `"    all_page_content = \"\\n\".join(pages.values())"` | — |
| [SRC-FA4E1423C3-L000281](../../tests/test_generate_index.py#L281) | 281 | `""` | — |
| [SRC-FA4E1423C3-L000282](../../tests/test_generate_index.py#L282) | 282 | `"    assert (\"app.py\", 1) in line_by_file_and_number"` | — |
| [SRC-FA4E1423C3-L000283](../../tests/test_generate_index.py#L283) | 283 | `"    assert (\"app.py\", 2) in line_by_file_and_number"` | — |
| [SRC-FA4E1423C3-L000284](../../tests/test_generate_index.py#L284) | 284 | `"    assert line_by_file_and_number[(\"app.py\", 2)].content == \"\""` | — |
| [SRC-FA4E1423C3-L000285](../../tests/test_generate_index.py#L285) | 285 | `"    assert line_by_file_and_number[(\"app.py\", 4)].content == '    return \"hello\"'"` | — |
| [SRC-FA4E1423C3-L000286](../../tests/test_generate_index.py#L286) | 286 | `"    assert line_by_file_and_number[(\"docs/guide.txt\", 2)].content == \"Second documented step.\""` | — |
| [SRC-FA4E1423C3-L000287](../../tests/test_generate_index.py#L287) | 287 | `"    assert line_by_file_and_number[(\"app.py\", 1)].line_id.startswith(\"SRC-\")"` | — |
| [SRC-FA4E1423C3-L000288](../../tests/test_generate_index.py#L288) | 288 | `"    assert line_by_file_and_number[(\"app.py\", 1)].file_id.startswith(\"FILE-\")"` | — |
| [SRC-FA4E1423C3-L000289](../../tests/test_generate_index.py#L289) | 289 | `"    assert line_by_file_and_number[(\"app.py\", 1)].category == \"ملفات أخرى\""` | — |
| [SRC-FA4E1423C3-L000290](../../tests/test_generate_index.py#L290) | 290 | `"    assert \"PRIVATE_TOKEN\" not in lines_markdown"` | — |
| [SRC-FA4E1423C3-L000291](../../tests/test_generate_index.py#L291) | 291 | `"    assert \"payload.bin\" not in {line.file for line in source_lines}"` | — |
| [SRC-FA4E1423C3-L000292](../../tests/test_generate_index.py#L292) | 292 | `"    assert \"Second documented step.\" in all_page_content"` | — |
| [SRC-FA4E1423C3-L000293](../../tests/test_generate_index.py#L293) | 293 | `"    assert \"SRC-\" in all_page_content"` | — |
| [SRC-FA4E1423C3-L000294](../../tests/test_generate_index.py#L294) | 294 | `"    assert \"SOURCE_LINES_001\" in lines_markdown"` | — |
| [SRC-FA4E1423C3-L000295](../../tests/test_generate_index.py#L295) | 295 | `"    assert pages_by_file[\"app.py\"]"` | — |
| [SRC-FA4E1423C3-L000296](../../tests/test_generate_index.py#L296) | 296 | `""` | — |
| [SRC-FA4E1423C3-L000297](../../tests/test_generate_index.py#L297) | 297 | `""` | — |
| [SRC-FA4E1423C3-L000298](../../tests/test_generate_index.py#L298) | 298 | `"def test_explicit_review_markers_have_unique_codes_and_source_line_links("` | — |
| [SRC-FA4E1423C3-L000299](../../tests/test_generate_index.py#L299) | 299 | `"    tmp_path: Path,"` | — |
| [SRC-FA4E1423C3-L000300](../../tests/test_generate_index.py#L300) | 300 | `") -> None:"` | — |
| [SRC-FA4E1423C3-L000301](../../tests/test_generate_index.py#L301) | 301 | `"    \"\"\"TODO/FIXME/BUG-style annotations receive stable named IDs linked to their exact lines.\"\"\""` | — |
| [SRC-FA4E1423C3-L000302](../../tests/test_generate_index.py#L302) | 302 | `"    (tmp_path / \"module.py\").write_text("` | — |
| [SRC-FA4E1423C3-L000303](../../tests/test_generate_index.py#L303) | 303 | `"        \"# TODO: verify fallback\\n\""` | — |
| [SRC-FA4E1423C3-L000304](../../tests/test_generate_index.py#L304) | 304 | `"        \"value = 1  # FIXME: handle overflow\\n\""` | — |
| [SRC-FA4E1423C3-L000305](../../tests/test_generate_index.py#L305) | 305 | `"        \"# SECURITY: check token handling\\n\""` | — |
| [SRC-FA4E1423C3-L000306](../../tests/test_generate_index.py#L306) | 306 | `"        \"def ready():\\n\""` | — |
| [SRC-FA4E1423C3-L000307](../../tests/test_generate_index.py#L307) | 307 | `"        \"    return True\\n\","` | — |
| [SRC-FA4E1423C3-L000308](../../tests/test_generate_index.py#L308) | 308 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000309](../../tests/test_generate_index.py#L309) | 309 | `"    )"` | — |
| [SRC-FA4E1423C3-L000310](../../tests/test_generate_index.py#L310) | 310 | `""` | — |
| [SRC-FA4E1423C3-L000311](../../tests/test_generate_index.py#L311) | 311 | `"    inventory = INDEXER.build_file_inventory(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000312](../../tests/test_generate_index.py#L312) | 312 | `"    source_lines = INDEXER.scan_source_lines(tmp_path, inventory)"` | — |
| [SRC-FA4E1423C3-L000313](../../tests/test_generate_index.py#L313) | 313 | `"    findings = INDEXER.scan_finding_annotations(source_lines)"` | — |
| [SRC-FA4E1423C3-L000314](../../tests/test_generate_index.py#L314) | 314 | `""` | — |
| [SRC-FA4E1423C3-L000315](../../tests/test_generate_index.py#L315) | 315 | `"    assert [item.marker for item in findings] == [\"FIXME\", \"SECURITY\", \"TODO\"]"` | — |
| [SRC-FA4E1423C3-L000316](../../tests/test_generate_index.py#L316) | 316 | `"    assert len({item.finding_id for item in findings}) == 3"` | — |
| [SRC-FA4E1423C3-L000317](../../tests/test_generate_index.py#L317) | 317 | `"    for finding in findings:"` | — |
| [SRC-FA4E1423C3-L000318](../../tests/test_generate_index.py#L318) | 318 | `"        assert finding.finding_id.startswith(f\"FND-{finding.marker}-\")"` | — |
| [SRC-FA4E1423C3-L000319](../../tests/test_generate_index.py#L319) | 319 | `"        assert finding.line_id.startswith(\"SRC-\")"` | — |
| [SRC-FA4E1423C3-L000320](../../tests/test_generate_index.py#L320) | 320 | `"        assert finding.file == \"module.py\""` | — |
| [SRC-FA4E1423C3-L000321](../../tests/test_generate_index.py#L321) | 321 | `""` | — |
| [SRC-FA4E1423C3-L000322](../../tests/test_generate_index.py#L322) | 322 | `""` | — |
| [SRC-FA4E1423C3-L000323](../../tests/test_generate_index.py#L323) | 323 | `"def test_check_mode_validates_all_generated_indexes(tmp_path: Path, capsys) -> None:"` | — |
| [SRC-FA4E1423C3-L000324](../../tests/test_generate_index.py#L324) | 324 | `"    \"\"\"Check mode detects stale master, line, and coverage indexes.\"\"\""` | — |
| [SRC-FA4E1423C3-L000325](../../tests/test_generate_index.py#L325) | 325 | `""` | — |
| [SRC-FA4E1423C3-L000326](../../tests/test_generate_index.py#L326) | 326 | `"    (tmp_path / \"app.py\").write_text(\"VALUE = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000327](../../tests/test_generate_index.py#L327) | 327 | `""` | — |
| [SRC-FA4E1423C3-L000328](../../tests/test_generate_index.py#L328) | 328 | `"    assert INDEXER.main([\"--root\", str(tmp_path)]) == 0"` | — |
| [SRC-FA4E1423C3-L000329](../../tests/test_generate_index.py#L329) | 329 | `"    master_path = tmp_path / INDEXER.INDEX_RELATIVE_PATH"` | — |
| [SRC-FA4E1423C3-L000330](../../tests/test_generate_index.py#L330) | 330 | `"    line_index_path = tmp_path / INDEXER.SOURCE_LINES_INDEX_RELATIVE_PATH"` | — |
| [SRC-FA4E1423C3-L000331](../../tests/test_generate_index.py#L331) | 331 | `"    coverage_path = tmp_path / INDEXER.COVERAGE_AUDIT_RELATIVE_PATH"` | — |
| [SRC-FA4E1423C3-L000332](../../tests/test_generate_index.py#L332) | 332 | `"    assert master_path.exists()"` | — |
| [SRC-FA4E1423C3-L000333](../../tests/test_generate_index.py#L333) | 333 | `"    assert line_index_path.exists()"` | — |
| [SRC-FA4E1423C3-L000334](../../tests/test_generate_index.py#L334) | 334 | `"    assert coverage_path.exists()"` | — |
| [SRC-FA4E1423C3-L000335](../../tests/test_generate_index.py#L335) | 335 | `"    assert INDEXER.main([\"--root\", str(tmp_path), \"--check\"]) == 0"` | — |
| [SRC-FA4E1423C3-L000336](../../tests/test_generate_index.py#L336) | 336 | `""` | — |
| [SRC-FA4E1423C3-L000337](../../tests/test_generate_index.py#L337) | 337 | `"    original_line_index = line_index_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000338](../../tests/test_generate_index.py#L338) | 338 | `"    line_index_path.write_text(\"stale line index\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000339](../../tests/test_generate_index.py#L339) | 339 | `"    assert INDEXER.main([\"--root\", str(tmp_path), \"--check\"]) == 1"` | — |
| [SRC-FA4E1423C3-L000340](../../tests/test_generate_index.py#L340) | 340 | `"    assert line_index_path.read_text(encoding=\"utf-8\") == \"stale line index\""` | — |
| [SRC-FA4E1423C3-L000341](../../tests/test_generate_index.py#L341) | 341 | `"    assert \"فهرس الأسطر قديم\" in capsys.readouterr().err"` | — |
| [SRC-FA4E1423C3-L000342](../../tests/test_generate_index.py#L342) | 342 | `""` | — |
| [SRC-FA4E1423C3-L000343](../../tests/test_generate_index.py#L343) | 343 | `"    line_index_path.write_text(original_line_index, encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000344](../../tests/test_generate_index.py#L344) | 344 | `"    coverage_path.write_text(\"stale coverage audit\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000345](../../tests/test_generate_index.py#L345) | 345 | `"    assert INDEXER.main([\"--root\", str(tmp_path), \"--check\"]) == 1"` | — |
| [SRC-FA4E1423C3-L000346](../../tests/test_generate_index.py#L346) | 346 | `"    assert coverage_path.read_text(encoding=\"utf-8\") == \"stale coverage audit\""` | — |
| [SRC-FA4E1423C3-L000347](../../tests/test_generate_index.py#L347) | 347 | `"    assert \"فهرس تغطية الفهرسة قديم\" in capsys.readouterr().err"` | — |
| [SRC-FA4E1423C3-L000348](../../tests/test_generate_index.py#L348) | 348 | `""` | — |
| [SRC-FA4E1423C3-L000349](../../tests/test_generate_index.py#L349) | 349 | `""` | — |
| [SRC-FA4E1423C3-L000350](../../tests/test_generate_index.py#L350) | 350 | `""` | — |
| [SRC-FA4E1423C3-L000351](../../tests/test_generate_index.py#L351) | 351 | `"def test_source_line_coverage_validator_rejects_missing_or_duplicate_lines(tmp_path: Path) -> None:"` | — |
| [SRC-FA4E1423C3-L000352](../../tests/test_generate_index.py#L352) | 352 | `"    \"\"\"A gap or duplicate in line IDs prevents the generator from claiming full coverage.\"\"\""` | — |
| [SRC-FA4E1423C3-L000353](../../tests/test_generate_index.py#L353) | 353 | `"    source_file = tmp_path / \"src.py\""` | — |
| [SRC-FA4E1423C3-L000354](../../tests/test_generate_index.py#L354) | 354 | `"    source_file.write_text(\"FIRST = 1\\nSECOND = 2\\n\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000355](../../tests/test_generate_index.py#L355) | 355 | `"    inventory = INDEXER.build_file_inventory(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000356](../../tests/test_generate_index.py#L356) | 356 | `"    lines = INDEXER.scan_source_lines(tmp_path, inventory)"` | — |
| [SRC-FA4E1423C3-L000357](../../tests/test_generate_index.py#L357) | 357 | `""` | — |
| [SRC-FA4E1423C3-L000358](../../tests/test_generate_index.py#L358) | 358 | `"    INDEXER.validate_source_line_coverage(tmp_path, inventory, lines)"` | — |
| [SRC-FA4E1423C3-L000359](../../tests/test_generate_index.py#L359) | 359 | `"    with pytest.raises(INDEXER.IndexGenerationError, match=\"اكتمال فهرسة السطور\"):"` | — |
| [SRC-FA4E1423C3-L000360](../../tests/test_generate_index.py#L360) | 360 | `"        INDEXER.validate_source_line_coverage(tmp_path, inventory, lines[:-1])"` | — |
| [SRC-FA4E1423C3-L000361](../../tests/test_generate_index.py#L361) | 361 | `"    with pytest.raises(INDEXER.IndexGenerationError, match=\"معرّف SRC مكرر\"):"` | — |
| [SRC-FA4E1423C3-L000362](../../tests/test_generate_index.py#L362) | 362 | `"        INDEXER.validate_source_line_coverage(tmp_path, inventory, lines + [lines[0]])"` | — |
| [SRC-FA4E1423C3-L000363](../../tests/test_generate_index.py#L363) | 363 | `"    corrupted = [replace(lines[0], content=\"not the source\"), *lines[1:]]"` | — |
| [SRC-FA4E1423C3-L000364](../../tests/test_generate_index.py#L364) | 364 | `"    with pytest.raises(INDEXER.IndexGenerationError, match=\"نص السطر لا يطابق المصدر\"):"` | — |
| [SRC-FA4E1423C3-L000365](../../tests/test_generate_index.py#L365) | 365 | `"        INDEXER.validate_source_line_coverage(tmp_path, inventory, corrupted)"` | — |
| [SRC-FA4E1423C3-L000366](../../tests/test_generate_index.py#L366) | 366 | `""` | — |
| [SRC-FA4E1423C3-L000367](../../tests/test_generate_index.py#L367) | 367 | `""` | — |
| [SRC-FA4E1423C3-L000368](../../tests/test_generate_index.py#L368) | 368 | `"def test_coverage_audit_discloses_metadata_only_and_excluded_paths_without_secrets("` | — |
| [SRC-FA4E1423C3-L000369](../../tests/test_generate_index.py#L369) | 369 | `"    tmp_path: Path,"` | — |
| [SRC-FA4E1423C3-L000370](../../tests/test_generate_index.py#L370) | 370 | `") -> None:"` | — |
| [SRC-FA4E1423C3-L000371](../../tests/test_generate_index.py#L371) | 371 | `"    \"\"\"Coverage report states exact skipped-file reasons without exposing secret contents.\"\"\""` | — |
| [SRC-FA4E1423C3-L000372](../../tests/test_generate_index.py#L372) | 372 | `"    (tmp_path / \"source.py\").write_text(\"VALUE = 7\\n\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000373](../../tests/test_generate_index.py#L373) | 373 | `"    (tmp_path / \".env\").write_text(\"PRIVATE_API_TOKEN=never-print-this-secret\\n\", encoding=\"utf-8\")"` | — |
