# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **049**
- سجلات الأسطر: **800**
- النطاق: SRC-AAA21D04E8-L000301 إلى SRC-1BB2FDD5B7-L000067
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-AAA21D04E8 — [tests/test_generation_capabilities.py](../../tests/test_generation_capabilities.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-AAA21D04E8-L000301](../../tests/test_generation_capabilities.py#L301) | 301 | `"        calls.append(model)"` | — |
| [SRC-AAA21D04E8-L000302](../../tests/test_generation_capabilities.py#L302) | 302 | `"        if model == \"primary/model\":"` | — |
| [SRC-AAA21D04E8-L000303](../../tests/test_generation_capabilities.py#L303) | 303 | `"            raise HTTPError(request.full_url, 429, \"Too Many Requests\", None, None)"` | — |
| [SRC-AAA21D04E8-L000304](../../tests/test_generation_capabilities.py#L304) | 304 | `"        return FakeResponse(\"إجابة مكتملة من النموذج الاحتياطي\", \"stop\")"` | — |
| [SRC-AAA21D04E8-L000305](../../tests/test_generation_capabilities.py#L305) | 305 | `""` | — |
| [SRC-AAA21D04E8-L000306](../../tests/test_generation_capabilities.py#L306) | 306 | `"    monkeypatch.setattr(\"agents.web_agent._open_model_request\", fake_urlopen)"` | — |
| [SRC-AAA21D04E8-L000307](../../tests/test_generation_capabilities.py#L307) | 307 | `"    answer = agent._request_completion("` | — |
| [SRC-AAA21D04E8-L000308](../../tests/test_generation_capabilities.py#L308) | 308 | `"        [{\"role\": \"user\", \"content\": \"اختبار\"}], model=\"primary/model\""` | — |
| [SRC-AAA21D04E8-L000309](../../tests/test_generation_capabilities.py#L309) | 309 | `"    )"` | — |
| [SRC-AAA21D04E8-L000310](../../tests/test_generation_capabilities.py#L310) | 310 | `""` | — |
| [SRC-AAA21D04E8-L000311](../../tests/test_generation_capabilities.py#L311) | 311 | `"    assert answer == \"إجابة مكتملة من النموذج الاحتياطي\""` | — |
| [SRC-AAA21D04E8-L000312](../../tests/test_generation_capabilities.py#L312) | 312 | `"    assert calls == [\"primary/model\", \"backup/model\"]"` | — |
| [SRC-AAA21D04E8-L000313](../../tests/test_generation_capabilities.py#L313) | 313 | `"    assert agent.generation_diagnostics[0][\"status\"] == \"rate_limited\""` | — |
| [SRC-AAA21D04E8-L000314](../../tests/test_generation_capabilities.py#L314) | 314 | `"    assert agent.generation_diagnostics[0][\"http_status_code\"] == 429"` | — |
| [SRC-AAA21D04E8-L000315](../../tests/test_generation_capabilities.py#L315) | 315 | `"    assert agent.generation_diagnostics[0][\"fallback_used\"] is False"` | — |
| [SRC-AAA21D04E8-L000316](../../tests/test_generation_capabilities.py#L316) | 316 | `"    assert agent.generation_diagnostics[1][\"status\"] == \"accepted\""` | — |
| [SRC-AAA21D04E8-L000317](../../tests/test_generation_capabilities.py#L317) | 317 | `"    assert agent.generation_diagnostics[1][\"fallback_used\"] is True"` | — |
| [SRC-AAA21D04E8-L000318](../../tests/test_generation_capabilities.py#L318) | 318 | `""` | — |
| [SRC-AAA21D04E8-L000319](../../tests/test_generation_capabilities.py#L319) | 319 | `""` | — |
| [SRC-AAA21D04E8-L000320](../../tests/test_generation_capabilities.py#L320) | 320 | `"def test_model_http_429_from_all_models_is_bounded_and_redacted(monkeypatch):"` | — |
| [SRC-AAA21D04E8-L000321](../../tests/test_generation_capabilities.py#L321) | 321 | `"    from urllib.error import HTTPError"` | — |
| [SRC-AAA21D04E8-L000322](../../tests/test_generation_capabilities.py#L322) | 322 | `""` | — |
| [SRC-AAA21D04E8-L000323](../../tests/test_generation_capabilities.py#L323) | 323 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000324](../../tests/test_generation_capabilities.py#L324) | 324 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-AAA21D04E8-L000325](../../tests/test_generation_capabilities.py#L325) | 325 | `"    agent.fallback_model = \"backup/model\""` | — |
| [SRC-AAA21D04E8-L000326](../../tests/test_generation_capabilities.py#L326) | 326 | `"    calls: list[str] = []"` | — |
| [SRC-AAA21D04E8-L000327](../../tests/test_generation_capabilities.py#L327) | 327 | `""` | — |
| [SRC-AAA21D04E8-L000328](../../tests/test_generation_capabilities.py#L328) | 328 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-AAA21D04E8-L000329](../../tests/test_generation_capabilities.py#L329) | 329 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-AAA21D04E8-L000330](../../tests/test_generation_capabilities.py#L330) | 330 | `"        calls.append(model)"` | — |
| [SRC-AAA21D04E8-L000331](../../tests/test_generation_capabilities.py#L331) | 331 | `"        raise HTTPError(request.full_url, 429, \"private provider detail\", None, None)"` | — |
| [SRC-AAA21D04E8-L000332](../../tests/test_generation_capabilities.py#L332) | 332 | `""` | — |
| [SRC-AAA21D04E8-L000333](../../tests/test_generation_capabilities.py#L333) | 333 | `"    monkeypatch.setattr(\"agents.web_agent._open_model_request\", fake_urlopen)"` | — |
| [SRC-AAA21D04E8-L000334](../../tests/test_generation_capabilities.py#L334) | 334 | `"    with pytest.raises(RuntimeError, match=\"HTTP 429\"):"` | — |
| [SRC-AAA21D04E8-L000335](../../tests/test_generation_capabilities.py#L335) | 335 | `"        agent._request_completion("` | — |
| [SRC-AAA21D04E8-L000336](../../tests/test_generation_capabilities.py#L336) | 336 | `"            [{\"role\": \"user\", \"content\": \"اختبار\"}], model=\"primary/model\""` | — |
| [SRC-AAA21D04E8-L000337](../../tests/test_generation_capabilities.py#L337) | 337 | `"        )"` | — |
| [SRC-AAA21D04E8-L000338](../../tests/test_generation_capabilities.py#L338) | 338 | `""` | — |
| [SRC-AAA21D04E8-L000339](../../tests/test_generation_capabilities.py#L339) | 339 | `"    assert calls == [\"primary/model\", \"backup/model\"]"` | — |
| [SRC-AAA21D04E8-L000340](../../tests/test_generation_capabilities.py#L340) | 340 | `"    assert [row[\"status\"] for row in agent.generation_diagnostics] == ["` | — |
| [SRC-AAA21D04E8-L000341](../../tests/test_generation_capabilities.py#L341) | 341 | `"        \"rate_limited\", \"rate_limited\""` | — |
| [SRC-AAA21D04E8-L000342](../../tests/test_generation_capabilities.py#L342) | 342 | `"    ]"` | — |
| [SRC-AAA21D04E8-L000343](../../tests/test_generation_capabilities.py#L343) | 343 | `"    assert [row[\"http_status_code\"] for row in agent.generation_diagnostics] == [429, 429]"` | — |
| [SRC-AAA21D04E8-L000344](../../tests/test_generation_capabilities.py#L344) | 344 | `"    assert \"private provider detail\" not in repr(agent.generation_diagnostics)"` | — |
| [SRC-AAA21D04E8-L000345](../../tests/test_generation_capabilities.py#L345) | 345 | `""` | — |
| [SRC-AAA21D04E8-L000346](../../tests/test_generation_capabilities.py#L346) | 346 | `""` | — |
| [SRC-AAA21D04E8-L000347](../../tests/test_generation_capabilities.py#L347) | 347 | `"@pytest.mark.parametrize(\"status_code\", [401, 403])"` | — |
| [SRC-AAA21D04E8-L000348](../../tests/test_generation_capabilities.py#L348) | 348 | `"def test_model_auth_http_errors_are_classified_and_fallback_is_bounded("` | — |
| [SRC-AAA21D04E8-L000349](../../tests/test_generation_capabilities.py#L349) | 349 | `"    monkeypatch, status_code"` | — |
| [SRC-AAA21D04E8-L000350](../../tests/test_generation_capabilities.py#L350) | 350 | `"):"` | — |
| [SRC-AAA21D04E8-L000351](../../tests/test_generation_capabilities.py#L351) | 351 | `"    from urllib.error import HTTPError"` | — |
| [SRC-AAA21D04E8-L000352](../../tests/test_generation_capabilities.py#L352) | 352 | `""` | — |
| [SRC-AAA21D04E8-L000353](../../tests/test_generation_capabilities.py#L353) | 353 | `"    agent = WebAgent()"` | — |
| [SRC-AAA21D04E8-L000354](../../tests/test_generation_capabilities.py#L354) | 354 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-AAA21D04E8-L000355](../../tests/test_generation_capabilities.py#L355) | 355 | `"    agent.fallback_model = \"backup/model\""` | — |
| [SRC-AAA21D04E8-L000356](../../tests/test_generation_capabilities.py#L356) | 356 | `"    calls: list[str] = []"` | — |
| [SRC-AAA21D04E8-L000357](../../tests/test_generation_capabilities.py#L357) | 357 | `""` | — |
| [SRC-AAA21D04E8-L000358](../../tests/test_generation_capabilities.py#L358) | 358 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-AAA21D04E8-L000359](../../tests/test_generation_capabilities.py#L359) | 359 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-AAA21D04E8-L000360](../../tests/test_generation_capabilities.py#L360) | 360 | `"        calls.append(model)"` | — |
| [SRC-AAA21D04E8-L000361](../../tests/test_generation_capabilities.py#L361) | 361 | `"        raise HTTPError(request.full_url, status_code, \"private auth detail\", None, None)"` | — |
| [SRC-AAA21D04E8-L000362](../../tests/test_generation_capabilities.py#L362) | 362 | `""` | — |
| [SRC-AAA21D04E8-L000363](../../tests/test_generation_capabilities.py#L363) | 363 | `"    monkeypatch.setattr(\"agents.web_agent._open_model_request\", fake_urlopen)"` | — |
| [SRC-AAA21D04E8-L000364](../../tests/test_generation_capabilities.py#L364) | 364 | `"    with pytest.raises(RuntimeError, match=f\"HTTP {status_code}\"):"` | — |
| [SRC-AAA21D04E8-L000365](../../tests/test_generation_capabilities.py#L365) | 365 | `"        agent._request_completion("` | — |
| [SRC-AAA21D04E8-L000366](../../tests/test_generation_capabilities.py#L366) | 366 | `"            [{\"role\": \"user\", \"content\": \"اختبار\"}], model=\"primary/model\""` | — |
| [SRC-AAA21D04E8-L000367](../../tests/test_generation_capabilities.py#L367) | 367 | `"        )"` | — |
| [SRC-AAA21D04E8-L000368](../../tests/test_generation_capabilities.py#L368) | 368 | `""` | — |
| [SRC-AAA21D04E8-L000369](../../tests/test_generation_capabilities.py#L369) | 369 | `"    assert calls == [\"primary/model\", \"backup/model\"]"` | — |
| [SRC-AAA21D04E8-L000370](../../tests/test_generation_capabilities.py#L370) | 370 | `"    assert [row[\"status\"] for row in agent.generation_diagnostics] == ["` | — |
| [SRC-AAA21D04E8-L000371](../../tests/test_generation_capabilities.py#L371) | 371 | `"        \"unauthorized\", \"unauthorized\""` | — |
| [SRC-AAA21D04E8-L000372](../../tests/test_generation_capabilities.py#L372) | 372 | `"    ]"` | — |
| [SRC-AAA21D04E8-L000373](../../tests/test_generation_capabilities.py#L373) | 373 | `"    assert [row[\"http_status_code\"] for row in agent.generation_diagnostics] == ["` | — |
| [SRC-AAA21D04E8-L000374](../../tests/test_generation_capabilities.py#L374) | 374 | `"        status_code, status_code"` | — |
| [SRC-AAA21D04E8-L000375](../../tests/test_generation_capabilities.py#L375) | 375 | `"    ]"` | — |
| [SRC-AAA21D04E8-L000376](../../tests/test_generation_capabilities.py#L376) | 376 | `"    assert \"private auth detail\" not in repr(agent.generation_diagnostics)"` | — |
| [SRC-AAA21D04E8-L000377](../../tests/test_generation_capabilities.py#L377) | 377 | `""` | — |
## اختبارات

### FILE-1A176AD4F0 — [tests/test_hosted_smoke.py](../../tests/test_hosted_smoke.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1A176AD4F0-L000001](../../tests/test_hosted_smoke.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-1A176AD4F0-L000002](../../tests/test_hosted_smoke.py#L2) | 2 | `""` | — |
| [SRC-1A176AD4F0-L000003](../../tests/test_hosted_smoke.py#L3) | 3 | `"import json"` | — |
| [SRC-1A176AD4F0-L000004](../../tests/test_hosted_smoke.py#L4) | 4 | `"import threading"` | — |
| [SRC-1A176AD4F0-L000005](../../tests/test_hosted_smoke.py#L5) | 5 | `"from pathlib import Path"` | — |
| [SRC-1A176AD4F0-L000006](../../tests/test_hosted_smoke.py#L6) | 6 | `"from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer"` | — |
| [SRC-1A176AD4F0-L000007](../../tests/test_hosted_smoke.py#L7) | 7 | `"from urllib.parse import urlsplit"` | — |
| [SRC-1A176AD4F0-L000008](../../tests/test_hosted_smoke.py#L8) | 8 | `""` | — |
| [SRC-1A176AD4F0-L000009](../../tests/test_hosted_smoke.py#L9) | 9 | `"import pytest"` | — |
| [SRC-1A176AD4F0-L000010](../../tests/test_hosted_smoke.py#L10) | 10 | `""` | — |
| [SRC-1A176AD4F0-L000011](../../tests/test_hosted_smoke.py#L11) | 11 | `"from scripts import hosted_smoke_test"` | — |
| [SRC-1A176AD4F0-L000012](../../tests/test_hosted_smoke.py#L12) | 12 | `"from scripts.hosted_smoke_test import SmokeError, normalize_origin, run_smoke"` | — |
| [SRC-1A176AD4F0-L000013](../../tests/test_hosted_smoke.py#L13) | 13 | `""` | — |
| [SRC-1A176AD4F0-L000014](../../tests/test_hosted_smoke.py#L14) | 14 | `"TOKEN = \"local-test-token-long-enough-for-the-32-character-rule\""` | — |
| [SRC-1A176AD4F0-L000015](../../tests/test_hosted_smoke.py#L15) | 15 | `""` | — |
| [SRC-1A176AD4F0-L000016](../../tests/test_hosted_smoke.py#L16) | 16 | `""` | — |
| [SRC-1A176AD4F0-L000017](../../tests/test_hosted_smoke.py#L17) | 17 | `"class Handler(BaseHTTPRequestHandler):"` | — |
| [SRC-1A176AD4F0-L000018](../../tests/test_hosted_smoke.py#L18) | 18 | `"    def log_message(self, format: str, *args: object) -> None:"` | — |
| [SRC-1A176AD4F0-L000019](../../tests/test_hosted_smoke.py#L19) | 19 | `"        return"` | — |
| [SRC-1A176AD4F0-L000020](../../tests/test_hosted_smoke.py#L20) | 20 | `""` | — |
| [SRC-1A176AD4F0-L000021](../../tests/test_hosted_smoke.py#L21) | 21 | `"    def respond(self, status: int, payload: dict[str, object]) -> None:"` | — |
| [SRC-1A176AD4F0-L000022](../../tests/test_hosted_smoke.py#L22) | 22 | `"        body = json.dumps(payload).encode()"` | — |
| [SRC-1A176AD4F0-L000023](../../tests/test_hosted_smoke.py#L23) | 23 | `"        self.send_response(status)"` | — |
| [SRC-1A176AD4F0-L000024](../../tests/test_hosted_smoke.py#L24) | 24 | `"        self.send_header(\"Content-Type\", \"application/json\")"` | — |
| [SRC-1A176AD4F0-L000025](../../tests/test_hosted_smoke.py#L25) | 25 | `"        self.send_header(\"Content-Length\", str(len(body)))"` | — |
| [SRC-1A176AD4F0-L000026](../../tests/test_hosted_smoke.py#L26) | 26 | `"        self.end_headers()"` | — |
| [SRC-1A176AD4F0-L000027](../../tests/test_hosted_smoke.py#L27) | 27 | `"        self.wfile.write(body)"` | — |
| [SRC-1A176AD4F0-L000028](../../tests/test_hosted_smoke.py#L28) | 28 | `""` | — |
| [SRC-1A176AD4F0-L000029](../../tests/test_hosted_smoke.py#L29) | 29 | `"    def do_GET(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000030](../../tests/test_hosted_smoke.py#L30) | 30 | `"        if self.path == \"/\":"` | — |
| [SRC-1A176AD4F0-L000031](../../tests/test_hosted_smoke.py#L31) | 31 | `"            self.respond(200, {\"page\": \"dashboard\"})"` | — |
| [SRC-1A176AD4F0-L000032](../../tests/test_hosted_smoke.py#L32) | 32 | `"        elif self.path == \"/api/health\":"` | — |
| [SRC-1A176AD4F0-L000033](../../tests/test_hosted_smoke.py#L33) | 33 | `"            self.respond(200, {\"ok\": True, \"app\": \"Omarai\", \"agent\": {}})"` | — |
| [SRC-1A176AD4F0-L000034](../../tests/test_hosted_smoke.py#L34) | 34 | `"        else:"` | — |
| [SRC-1A176AD4F0-L000035](../../tests/test_hosted_smoke.py#L35) | 35 | `"            self.respond(404, {\"error\": \"not found\"})"` | — |
| [SRC-1A176AD4F0-L000036](../../tests/test_hosted_smoke.py#L36) | 36 | `""` | — |
| [SRC-1A176AD4F0-L000037](../../tests/test_hosted_smoke.py#L37) | 37 | `"    def do_POST(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000038](../../tests/test_hosted_smoke.py#L38) | 38 | `"        if self.headers.get(\"Authorization\") != f\"Bearer {TOKEN}\":"` | — |
| [SRC-1A176AD4F0-L000039](../../tests/test_hosted_smoke.py#L39) | 39 | `"            self.respond(401, {\"error\": \"unauthorized\"})"` | — |
| [SRC-1A176AD4F0-L000040](../../tests/test_hosted_smoke.py#L40) | 40 | `"            return"` | — |
| [SRC-1A176AD4F0-L000041](../../tests/test_hosted_smoke.py#L41) | 41 | `"        length = int(self.headers.get(\"Content-Length\", \"0\"))"` | — |
| [SRC-1A176AD4F0-L000042](../../tests/test_hosted_smoke.py#L42) | 42 | `"        self.rfile.read(length)"` | — |
| [SRC-1A176AD4F0-L000043](../../tests/test_hosted_smoke.py#L43) | 43 | `"        if self.path == \"/api/diagnostics\":"` | — |
| [SRC-1A176AD4F0-L000044](../../tests/test_hosted_smoke.py#L44) | 44 | `"            self.respond(200, {"` | — |
| [SRC-1A176AD4F0-L000045](../../tests/test_hosted_smoke.py#L45) | 45 | `"                \"overall_status\": \"passed\","` | — |
| [SRC-1A176AD4F0-L000046](../../tests/test_hosted_smoke.py#L46) | 46 | `"                \"checks\": {"` | — |
| [SRC-1A176AD4F0-L000047](../../tests/test_hosted_smoke.py#L47) | 47 | `"                    \"web_search\": {"` | — |
| [SRC-1A176AD4F0-L000048](../../tests/test_hosted_smoke.py#L48) | 48 | `"                        \"status\": \"passed\", \"result_count\": 2,"` | — |
| [SRC-1A176AD4F0-L000049](../../tests/test_hosted_smoke.py#L49) | 49 | `"                        \"provider_counts\": {\"bing_rss\": 1, \"duckduckgo_html\": 1},"` | — |
| [SRC-1A176AD4F0-L000050](../../tests/test_hosted_smoke.py#L50) | 50 | `"                    },"` | — |
| [SRC-1A176AD4F0-L000051](../../tests/test_hosted_smoke.py#L51) | 51 | `"                    \"language_model\": {\"status\": \"passed\", \"response_received\": True},"` | — |
| [SRC-1A176AD4F0-L000052](../../tests/test_hosted_smoke.py#L52) | 52 | `"                    \"social_search\": {\"status\": \"skipped\"},"` | — |
| [SRC-1A176AD4F0-L000053](../../tests/test_hosted_smoke.py#L53) | 53 | `"                },"` | — |
| [SRC-1A176AD4F0-L000054](../../tests/test_hosted_smoke.py#L54) | 54 | `"            })"` | — |
| [SRC-1A176AD4F0-L000055](../../tests/test_hosted_smoke.py#L55) | 55 | `"        elif self.path == \"/api/agent\":"` | — |
| [SRC-1A176AD4F0-L000056](../../tests/test_hosted_smoke.py#L56) | 56 | `"            self.respond(200, {"` | — |
| [SRC-1A176AD4F0-L000057](../../tests/test_hosted_smoke.py#L57) | 57 | `"                \"answer\": \"القاهرة هي عاصمة مصر. [المصدر 1]\","` | — |
| [SRC-1A176AD4F0-L000058](../../tests/test_hosted_smoke.py#L58) | 58 | `"                \"used_web_search\": True,"` | — |
| [SRC-1A176AD4F0-L000059](../../tests/test_hosted_smoke.py#L59) | 59 | `"                \"used_language_model\": True,"` | — |
| [SRC-1A176AD4F0-L000060](../../tests/test_hosted_smoke.py#L60) | 60 | `"                \"sources\": [{\"title\": \"مصدر اختبار\", \"url\": \"https://example.com/source\"}],"` | — |
| [SRC-1A176AD4F0-L000061](../../tests/test_hosted_smoke.py#L61) | 61 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1A176AD4F0-L000062](../../tests/test_hosted_smoke.py#L62) | 62 | `"                \"request_budget\": {\"profile\": \"hosted_smoke\", \"timeout_seconds\": 75, \"budget_exhausted\": False, \"deadline_exceeded\": False, \"limits\": {\"search_queries\": 3, \"search_calls\": 12, \"model_calls\": 6, \"page_fetches\": 4, \"tool_calls\": 0}, \"counts\": {\"search_queries\": 2, \"search_calls\": 4, \"model_calls\": 4, \"page_fetches\": 1, \"tool_calls\": 0}},"` | — |
| [SRC-1A176AD4F0-L000063](../../tests/test_hosted_smoke.py#L63) | 63 | `"                \"search_report\": {"` | — |
| [SRC-1A176AD4F0-L000064](../../tests/test_hosted_smoke.py#L64) | 64 | `"                    \"providers_used\": [\"bing_rss\"], \"pages_fetched\": 1,"` | — |
| [SRC-1A176AD4F0-L000065](../../tests/test_hosted_smoke.py#L65) | 65 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1A176AD4F0-L000066](../../tests/test_hosted_smoke.py#L66) | 66 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_all_claims_supported\"},"` | — |
| [SRC-1A176AD4F0-L000067](../../tests/test_hosted_smoke.py#L67) | 67 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1A176AD4F0-L000068](../../tests/test_hosted_smoke.py#L68) | 68 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1A176AD4F0-L000069](../../tests/test_hosted_smoke.py#L69) | 69 | `"                },"` | — |
| [SRC-1A176AD4F0-L000070](../../tests/test_hosted_smoke.py#L70) | 70 | `"            })"` | — |
| [SRC-1A176AD4F0-L000071](../../tests/test_hosted_smoke.py#L71) | 71 | `"        else:"` | — |
| [SRC-1A176AD4F0-L000072](../../tests/test_hosted_smoke.py#L72) | 72 | `"            self.respond(404, {\"error\": \"not found\"})"` | — |
| [SRC-1A176AD4F0-L000073](../../tests/test_hosted_smoke.py#L73) | 73 | `""` | — |
| [SRC-1A176AD4F0-L000074](../../tests/test_hosted_smoke.py#L74) | 74 | `""` | — |
| [SRC-1A176AD4F0-L000075](../../tests/test_hosted_smoke.py#L75) | 75 | `"@pytest.fixture"` | — |
| [SRC-1A176AD4F0-L000076](../../tests/test_hosted_smoke.py#L76) | 76 | `"def hosted_server():"` | — |
| [SRC-1A176AD4F0-L000077](../../tests/test_hosted_smoke.py#L77) | 77 | `"    server = ThreadingHTTPServer((\"127.0.0.1\", 0), Handler)"` | — |
| [SRC-1A176AD4F0-L000078](../../tests/test_hosted_smoke.py#L78) | 78 | `"    thread = threading.Thread(target=server.serve_forever, daemon=True)"` | — |
| [SRC-1A176AD4F0-L000079](../../tests/test_hosted_smoke.py#L79) | 79 | `"    thread.start()"` | — |
| [SRC-1A176AD4F0-L000080](../../tests/test_hosted_smoke.py#L80) | 80 | `"    try:"` | — |
| [SRC-1A176AD4F0-L000081](../../tests/test_hosted_smoke.py#L81) | 81 | `"        yield f\"http://127.0.0.1:{server.server_port}\""` | — |
| [SRC-1A176AD4F0-L000082](../../tests/test_hosted_smoke.py#L82) | 82 | `"    finally:"` | — |
| [SRC-1A176AD4F0-L000083](../../tests/test_hosted_smoke.py#L83) | 83 | `"        server.shutdown()"` | — |
| [SRC-1A176AD4F0-L000084](../../tests/test_hosted_smoke.py#L84) | 84 | `"        server.server_close()"` | — |
| [SRC-1A176AD4F0-L000085](../../tests/test_hosted_smoke.py#L85) | 85 | `"        thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000086](../../tests/test_hosted_smoke.py#L86) | 86 | `""` | — |
| [SRC-1A176AD4F0-L000087](../../tests/test_hosted_smoke.py#L87) | 87 | `""` | — |
| [SRC-1A176AD4F0-L000088](../../tests/test_hosted_smoke.py#L88) | 88 | `"def test_normalize_origin_requires_https_and_rejects_credentials_or_paths():"` | — |
| [SRC-1A176AD4F0-L000089](../../tests/test_hosted_smoke.py#L89) | 89 | `"    assert normalize_origin(\"https://example.com/\") == \"https://example.com\""` | — |
| [SRC-1A176AD4F0-L000090](../../tests/test_hosted_smoke.py#L90) | 90 | `"    for invalid in ("` | — |
| [SRC-1A176AD4F0-L000091](../../tests/test_hosted_smoke.py#L91) | 91 | `"        \"http://example.com\","` | — |
| [SRC-1A176AD4F0-L000092](../../tests/test_hosted_smoke.py#L92) | 92 | `"        \"https://user:password@example.com\","` | — |
| [SRC-1A176AD4F0-L000093](../../tests/test_hosted_smoke.py#L93) | 93 | `"        \"https://example.com/path\","` | — |
| [SRC-1A176AD4F0-L000094](../../tests/test_hosted_smoke.py#L94) | 94 | `"        \"https://example.com/?token=secret\","` | — |
| [SRC-1A176AD4F0-L000095](../../tests/test_hosted_smoke.py#L95) | 95 | `"    ):"` | — |
| [SRC-1A176AD4F0-L000096](../../tests/test_hosted_smoke.py#L96) | 96 | `"        with pytest.raises(SmokeError):"` | — |
| [SRC-1A176AD4F0-L000097](../../tests/test_hosted_smoke.py#L97) | 97 | `"            normalize_origin(invalid)"` | — |
| [SRC-1A176AD4F0-L000098](../../tests/test_hosted_smoke.py#L98) | 98 | `""` | — |
| [SRC-1A176AD4F0-L000099](../../tests/test_hosted_smoke.py#L99) | 99 | `""` | — |
| [SRC-1A176AD4F0-L000100](../../tests/test_hosted_smoke.py#L100) | 100 | `"def test_normalize_origin_allows_plain_http_only_for_local_test():"` | — |
| [SRC-1A176AD4F0-L000101](../../tests/test_hosted_smoke.py#L101) | 101 | `"    assert normalize_origin(\"http://127.0.0.1:8765\", allow_http=True) == ("` | — |
| [SRC-1A176AD4F0-L000102](../../tests/test_hosted_smoke.py#L102) | 102 | `"        \"http://127.0.0.1:8765\""` | — |
| [SRC-1A176AD4F0-L000103](../../tests/test_hosted_smoke.py#L103) | 103 | `"    )"` | — |
| [SRC-1A176AD4F0-L000104](../../tests/test_hosted_smoke.py#L104) | 104 | `"    with pytest.raises(SmokeError):"` | — |
| [SRC-1A176AD4F0-L000105](../../tests/test_hosted_smoke.py#L105) | 105 | `"        normalize_origin(\"http://example.com\", allow_http=True)"` | — |
| [SRC-1A176AD4F0-L000106](../../tests/test_hosted_smoke.py#L106) | 106 | `""` | — |
| [SRC-1A176AD4F0-L000107](../../tests/test_hosted_smoke.py#L107) | 107 | `""` | — |
| [SRC-1A176AD4F0-L000108](../../tests/test_hosted_smoke.py#L108) | 108 | `"def test_smoke_checks_health_auth_and_single_agent_search(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000109](../../tests/test_hosted_smoke.py#L109) | 109 | `"    result = run_smoke("` | — |
| [SRC-1A176AD4F0-L000110](../../tests/test_hosted_smoke.py#L110) | 110 | `"        hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5"` | — |
| [SRC-1A176AD4F0-L000111](../../tests/test_hosted_smoke.py#L111) | 111 | `"    )"` | — |
| [SRC-1A176AD4F0-L000112](../../tests/test_hosted_smoke.py#L112) | 112 | `"    assert result[\"result\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000113](../../tests/test_hosted_smoke.py#L113) | 113 | `"    assert result[\"checks\"][\"health\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000114](../../tests/test_hosted_smoke.py#L114) | 114 | `"    assert result[\"checks\"][\"authentication\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000115](../../tests/test_hosted_smoke.py#L115) | 115 | `"    assert result[\"checks\"][\"search\"][\"providers_reported\"] == [\"bing_rss\"]"` | — |
| [SRC-1A176AD4F0-L000116](../../tests/test_hosted_smoke.py#L116) | 116 | `"    assert result[\"checks\"][\"agent_request\"][\"source_count\"] == 1"` | — |
| [SRC-1A176AD4F0-L000117](../../tests/test_hosted_smoke.py#L117) | 117 | `"    assert result[\"checks\"][\"agent_request\"][\"pipeline_completion_status\"] == \"completed\""` | — |
| [SRC-1A176AD4F0-L000118](../../tests/test_hosted_smoke.py#L118) | 118 | `""` | — |
| [SRC-1A176AD4F0-L000119](../../tests/test_hosted_smoke.py#L119) | 119 | `""` | — |
| [SRC-1A176AD4F0-L000120](../../tests/test_hosted_smoke.py#L120) | 120 | `"def test_smoke_never_forwards_bearer_to_cross_origin_redirect():"` | — |
| [SRC-1A176AD4F0-L000121](../../tests/test_hosted_smoke.py#L121) | 121 | `"    received_authorizations = []"` | — |
| [SRC-1A176AD4F0-L000122](../../tests/test_hosted_smoke.py#L122) | 122 | `""` | — |
| [SRC-1A176AD4F0-L000123](../../tests/test_hosted_smoke.py#L123) | 123 | `"    class RedirectHandler(BaseHTTPRequestHandler):"` | — |
| [SRC-1A176AD4F0-L000124](../../tests/test_hosted_smoke.py#L124) | 124 | `"        def log_message(self, format: str, *args: object) -> None:"` | — |
| [SRC-1A176AD4F0-L000125](../../tests/test_hosted_smoke.py#L125) | 125 | `"            return"` | — |
| [SRC-1A176AD4F0-L000126](../../tests/test_hosted_smoke.py#L126) | 126 | `""` | — |
| [SRC-1A176AD4F0-L000127](../../tests/test_hosted_smoke.py#L127) | 127 | `"        def do_GET(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000128](../../tests/test_hosted_smoke.py#L128) | 128 | `"            self.send_response(302)"` | — |
| [SRC-1A176AD4F0-L000129](../../tests/test_hosted_smoke.py#L129) | 129 | `"            self.send_header(\"Location\", self.server.redirect_destination)"` | — |
| [SRC-1A176AD4F0-L000130](../../tests/test_hosted_smoke.py#L130) | 130 | `"            self.send_header(\"Content-Length\", \"0\")"` | — |
| [SRC-1A176AD4F0-L000131](../../tests/test_hosted_smoke.py#L131) | 131 | `"            self.end_headers()"` | — |
| [SRC-1A176AD4F0-L000132](../../tests/test_hosted_smoke.py#L132) | 132 | `""` | — |
| [SRC-1A176AD4F0-L000133](../../tests/test_hosted_smoke.py#L133) | 133 | `"    class DestinationHandler(BaseHTTPRequestHandler):"` | — |
| [SRC-1A176AD4F0-L000134](../../tests/test_hosted_smoke.py#L134) | 134 | `"        def log_message(self, format: str, *args: object) -> None:"` | — |
| [SRC-1A176AD4F0-L000135](../../tests/test_hosted_smoke.py#L135) | 135 | `"            return"` | — |
| [SRC-1A176AD4F0-L000136](../../tests/test_hosted_smoke.py#L136) | 136 | `""` | — |
| [SRC-1A176AD4F0-L000137](../../tests/test_hosted_smoke.py#L137) | 137 | `"        def do_GET(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000138](../../tests/test_hosted_smoke.py#L138) | 138 | `"            received_authorizations.append(self.headers.get(\"Authorization\"))"` | — |
| [SRC-1A176AD4F0-L000139](../../tests/test_hosted_smoke.py#L139) | 139 | `"            self.send_response(200)"` | — |
| [SRC-1A176AD4F0-L000140](../../tests/test_hosted_smoke.py#L140) | 140 | `"            self.send_header(\"Content-Length\", \"0\")"` | — |
| [SRC-1A176AD4F0-L000141](../../tests/test_hosted_smoke.py#L141) | 141 | `"            self.end_headers()"` | — |
| [SRC-1A176AD4F0-L000142](../../tests/test_hosted_smoke.py#L142) | 142 | `""` | — |
| [SRC-1A176AD4F0-L000143](../../tests/test_hosted_smoke.py#L143) | 143 | `"    destination = ThreadingHTTPServer((\"127.0.0.1\", 0), DestinationHandler)"` | — |
| [SRC-1A176AD4F0-L000144](../../tests/test_hosted_smoke.py#L144) | 144 | `"    source = ThreadingHTTPServer((\"127.0.0.1\", 0), RedirectHandler)"` | — |
| [SRC-1A176AD4F0-L000145](../../tests/test_hosted_smoke.py#L145) | 145 | `"    destination_thread = threading.Thread(target=destination.serve_forever, daemon=True)"` | — |
| [SRC-1A176AD4F0-L000146](../../tests/test_hosted_smoke.py#L146) | 146 | `"    source_thread = threading.Thread(target=source.serve_forever, daemon=True)"` | — |
| [SRC-1A176AD4F0-L000147](../../tests/test_hosted_smoke.py#L147) | 147 | `"    source.redirect_destination = ("` | — |
| [SRC-1A176AD4F0-L000148](../../tests/test_hosted_smoke.py#L148) | 148 | `"        f\"http://127.0.0.1:{destination.server_port}/capture\""` | — |
| [SRC-1A176AD4F0-L000149](../../tests/test_hosted_smoke.py#L149) | 149 | `"    )"` | — |
| [SRC-1A176AD4F0-L000150](../../tests/test_hosted_smoke.py#L150) | 150 | `"    destination_thread.start()"` | — |
| [SRC-1A176AD4F0-L000151](../../tests/test_hosted_smoke.py#L151) | 151 | `"    source_thread.start()"` | — |
| [SRC-1A176AD4F0-L000152](../../tests/test_hosted_smoke.py#L152) | 152 | `"    try:"` | — |
| [SRC-1A176AD4F0-L000153](../../tests/test_hosted_smoke.py#L153) | 153 | `"        status, payload = hosted_smoke_test.request_json("` | — |
| [SRC-1A176AD4F0-L000154](../../tests/test_hosted_smoke.py#L154) | 154 | `"            f\"http://127.0.0.1:{source.server_port}/redirect\","` | — |
| [SRC-1A176AD4F0-L000155](../../tests/test_hosted_smoke.py#L155) | 155 | `"            token=TOKEN,"` | — |
| [SRC-1A176AD4F0-L000156](../../tests/test_hosted_smoke.py#L156) | 156 | `"            timeout=3,"` | — |
| [SRC-1A176AD4F0-L000157](../../tests/test_hosted_smoke.py#L157) | 157 | `"        )"` | — |
| [SRC-1A176AD4F0-L000158](../../tests/test_hosted_smoke.py#L158) | 158 | `"        assert status == 302"` | — |
| [SRC-1A176AD4F0-L000159](../../tests/test_hosted_smoke.py#L159) | 159 | `"        assert payload is None"` | — |
| [SRC-1A176AD4F0-L000160](../../tests/test_hosted_smoke.py#L160) | 160 | `"        assert received_authorizations == []"` | — |
| [SRC-1A176AD4F0-L000161](../../tests/test_hosted_smoke.py#L161) | 161 | `"    finally:"` | — |
| [SRC-1A176AD4F0-L000162](../../tests/test_hosted_smoke.py#L162) | 162 | `"        source.shutdown()"` | — |
| [SRC-1A176AD4F0-L000163](../../tests/test_hosted_smoke.py#L163) | 163 | `"        destination.shutdown()"` | — |
| [SRC-1A176AD4F0-L000164](../../tests/test_hosted_smoke.py#L164) | 164 | `"        source.server_close()"` | — |
| [SRC-1A176AD4F0-L000165](../../tests/test_hosted_smoke.py#L165) | 165 | `"        destination.server_close()"` | — |
| [SRC-1A176AD4F0-L000166](../../tests/test_hosted_smoke.py#L166) | 166 | `"        source_thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000167](../../tests/test_hosted_smoke.py#L167) | 167 | `"        destination_thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000168](../../tests/test_hosted_smoke.py#L168) | 168 | `""` | — |
| [SRC-1A176AD4F0-L000169](../../tests/test_hosted_smoke.py#L169) | 169 | `""` | — |
| [SRC-1A176AD4F0-L000170](../../tests/test_hosted_smoke.py#L170) | 170 | `"def test_smoke_refuses_missing_or_short_access_token(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000171](../../tests/test_hosted_smoke.py#L171) | 171 | `"    with pytest.raises(SmokeError, match=\"OMARAI_ACCESS_TOKEN\"):"` | — |
| [SRC-1A176AD4F0-L000172](../../tests/test_hosted_smoke.py#L172) | 172 | `"        run_smoke(hosted_server, \"\", allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000173](../../tests/test_hosted_smoke.py#L173) | 173 | `""` | — |
| [SRC-1A176AD4F0-L000174](../../tests/test_hosted_smoke.py#L174) | 174 | `""` | — |
| [SRC-1A176AD4F0-L000175](../../tests/test_hosted_smoke.py#L175) | 175 | `"def test_smoke_fails_when_agent_returns_no_live_source(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000176](../../tests/test_hosted_smoke.py#L176) | 176 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000177](../../tests/test_hosted_smoke.py#L177) | 177 | `""` | — |
| [SRC-1A176AD4F0-L000178](../../tests/test_hosted_smoke.py#L178) | 178 | `"    def without_sources(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000179](../../tests/test_hosted_smoke.py#L179) | 179 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000180](../../tests/test_hosted_smoke.py#L180) | 180 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000181](../../tests/test_hosted_smoke.py#L181) | 181 | `"                \"answer\": \"إجابة بلا مصادر\", \"used_web_search\": False,"` | — |
| [SRC-1A176AD4F0-L000182](../../tests/test_hosted_smoke.py#L182) | 182 | `"                \"used_language_model\": True, \"sources\": [],"` | — |
| [SRC-1A176AD4F0-L000183](../../tests/test_hosted_smoke.py#L183) | 183 | `"            }"` | — |
| [SRC-1A176AD4F0-L000184](../../tests/test_hosted_smoke.py#L184) | 184 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000185](../../tests/test_hosted_smoke.py#L185) | 185 | `""` | — |
| [SRC-1A176AD4F0-L000186](../../tests/test_hosted_smoke.py#L186) | 186 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", without_sources)"` | — |
| [SRC-1A176AD4F0-L000187](../../tests/test_hosted_smoke.py#L187) | 187 | `"    with pytest.raises(SmokeError, match=\"usable source URLs\") as failure:"` | — |
| [SRC-1A176AD4F0-L000188](../../tests/test_hosted_smoke.py#L188) | 188 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000189](../../tests/test_hosted_smoke.py#L189) | 189 | `"    assert failure.value.report[\"transcript\"][0][\"question\"] == ("` | — |
| [SRC-1A176AD4F0-L000190](../../tests/test_hosted_smoke.py#L190) | 190 | `"        hosted_smoke_test.LIVE_TEST_QUESTION"` | — |
| [SRC-1A176AD4F0-L000191](../../tests/test_hosted_smoke.py#L191) | 191 | `"    )"` | — |
| [SRC-1A176AD4F0-L000192](../../tests/test_hosted_smoke.py#L192) | 192 | `"    assert failure.value.report[\"transcript\"][0][\"answer\"] == \"إجابة بلا مصادر\""` | — |
| [SRC-1A176AD4F0-L000193](../../tests/test_hosted_smoke.py#L193) | 193 | `""` | — |
| [SRC-1A176AD4F0-L000194](../../tests/test_hosted_smoke.py#L194) | 194 | `""` | — |
| [SRC-1A176AD4F0-L000195](../../tests/test_hosted_smoke.py#L195) | 195 | `"def test_smoke_rejects_invalid_expected_source_sha(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000196](../../tests/test_hosted_smoke.py#L196) | 196 | `"    with pytest.raises(SmokeError, match=\"40-character Git SHA\"):"` | — |
| [SRC-1A176AD4F0-L000197](../../tests/test_hosted_smoke.py#L197) | 197 | `"        run_smoke("` | — |
| [SRC-1A176AD4F0-L000198](../../tests/test_hosted_smoke.py#L198) | 198 | `"            hosted_server, TOKEN, allow_http=True, timeout=5, expected_sha=\"main\""` | — |
| [SRC-1A176AD4F0-L000199](../../tests/test_hosted_smoke.py#L199) | 199 | `"        )"` | — |
| [SRC-1A176AD4F0-L000200](../../tests/test_hosted_smoke.py#L200) | 200 | `""` | — |
| [SRC-1A176AD4F0-L000201](../../tests/test_hosted_smoke.py#L201) | 201 | `""` | — |
| [SRC-1A176AD4F0-L000202](../../tests/test_hosted_smoke.py#L202) | 202 | `"def test_smoke_rejects_deployed_build_sha_mismatch(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000203](../../tests/test_hosted_smoke.py#L203) | 203 | `"    with pytest.raises(SmokeError, match=\"does not match the expected Git commit\"):"` | — |
| [SRC-1A176AD4F0-L000204](../../tests/test_hosted_smoke.py#L204) | 204 | `"        run_smoke("` | — |
| [SRC-1A176AD4F0-L000205](../../tests/test_hosted_smoke.py#L205) | 205 | `"            hosted_server,"` | — |
| [SRC-1A176AD4F0-L000206](../../tests/test_hosted_smoke.py#L206) | 206 | `"            TOKEN,"` | — |
| [SRC-1A176AD4F0-L000207](../../tests/test_hosted_smoke.py#L207) | 207 | `"            allow_http=True,"` | — |
| [SRC-1A176AD4F0-L000208](../../tests/test_hosted_smoke.py#L208) | 208 | `"            allow_provider_usage=True,"` | — |
| [SRC-1A176AD4F0-L000209](../../tests/test_hosted_smoke.py#L209) | 209 | `"            timeout=5,"` | — |
| [SRC-1A176AD4F0-L000210](../../tests/test_hosted_smoke.py#L210) | 210 | `"            expected_sha=\"a\" * 40,"` | — |
| [SRC-1A176AD4F0-L000211](../../tests/test_hosted_smoke.py#L211) | 211 | `"        )"` | — |
| [SRC-1A176AD4F0-L000212](../../tests/test_hosted_smoke.py#L212) | 212 | `""` | — |
| [SRC-1A176AD4F0-L000213](../../tests/test_hosted_smoke.py#L213) | 213 | `""` | — |
| [SRC-1A176AD4F0-L000214](../../tests/test_hosted_smoke.py#L214) | 214 | `""` | — |
| [SRC-1A176AD4F0-L000215](../../tests/test_hosted_smoke.py#L215) | 215 | `"def test_http_403_report_contains_only_safe_response_metadata():"` | — |
| [SRC-1A176AD4F0-L000216](../../tests/test_hosted_smoke.py#L216) | 216 | `"    class ForbiddenHandler(BaseHTTPRequestHandler):"` | — |
| [SRC-1A176AD4F0-L000217](../../tests/test_hosted_smoke.py#L217) | 217 | `"        def log_message(self, format: str, *args: object) -> None:"` | — |
| [SRC-1A176AD4F0-L000218](../../tests/test_hosted_smoke.py#L218) | 218 | `"            return"` | — |
| [SRC-1A176AD4F0-L000219](../../tests/test_hosted_smoke.py#L219) | 219 | `""` | — |
| [SRC-1A176AD4F0-L000220](../../tests/test_hosted_smoke.py#L220) | 220 | `"        def do_GET(self) -> None:"` | — |
| [SRC-1A176AD4F0-L000221](../../tests/test_hosted_smoke.py#L221) | 221 | `"            body = b\"<html>blocked</html>\""` | — |
| [SRC-1A176AD4F0-L000222](../../tests/test_hosted_smoke.py#L222) | 222 | `"            self.send_response(403)"` | — |
| [SRC-1A176AD4F0-L000223](../../tests/test_hosted_smoke.py#L223) | 223 | `"            self.send_header(\"Content-Type\", \"text/html\")"` | — |
| [SRC-1A176AD4F0-L000224](../../tests/test_hosted_smoke.py#L224) | 224 | `"            self.send_header(\"X-Request-ID\", \"request-123\")"` | — |
| [SRC-1A176AD4F0-L000225](../../tests/test_hosted_smoke.py#L225) | 225 | `"            self.send_header(\"CF-Ray\", \"ray-456\")"` | — |
| [SRC-1A176AD4F0-L000226](../../tests/test_hosted_smoke.py#L226) | 226 | `"            self.send_header(\"Content-Length\", str(len(body)))"` | — |
| [SRC-1A176AD4F0-L000227](../../tests/test_hosted_smoke.py#L227) | 227 | `"            self.end_headers()"` | — |
| [SRC-1A176AD4F0-L000228](../../tests/test_hosted_smoke.py#L228) | 228 | `"            self.wfile.write(body)"` | — |
| [SRC-1A176AD4F0-L000229](../../tests/test_hosted_smoke.py#L229) | 229 | `""` | — |
| [SRC-1A176AD4F0-L000230](../../tests/test_hosted_smoke.py#L230) | 230 | `"    server = ThreadingHTTPServer((\"127.0.0.1\", 0), ForbiddenHandler)"` | — |
| [SRC-1A176AD4F0-L000231](../../tests/test_hosted_smoke.py#L231) | 231 | `"    thread = threading.Thread(target=server.serve_forever, daemon=True)"` | — |
| [SRC-1A176AD4F0-L000232](../../tests/test_hosted_smoke.py#L232) | 232 | `"    thread.start()"` | — |
| [SRC-1A176AD4F0-L000233](../../tests/test_hosted_smoke.py#L233) | 233 | `"    try:"` | — |
| [SRC-1A176AD4F0-L000234](../../tests/test_hosted_smoke.py#L234) | 234 | `"        status, payload = hosted_smoke_test.request_json("` | — |
| [SRC-1A176AD4F0-L000235](../../tests/test_hosted_smoke.py#L235) | 235 | `"            f\"http://127.0.0.1:{server.server_port}/api/health\","` | — |
| [SRC-1A176AD4F0-L000236](../../tests/test_hosted_smoke.py#L236) | 236 | `"            token=TOKEN,"` | — |
| [SRC-1A176AD4F0-L000237](../../tests/test_hosted_smoke.py#L237) | 237 | `"            timeout=3,"` | — |
| [SRC-1A176AD4F0-L000238](../../tests/test_hosted_smoke.py#L238) | 238 | `"        )"` | — |
| [SRC-1A176AD4F0-L000239](../../tests/test_hosted_smoke.py#L239) | 239 | `"        assert status == 403"` | — |
| [SRC-1A176AD4F0-L000240](../../tests/test_hosted_smoke.py#L240) | 240 | `"        assert payload[\"_smoke_http\"][\"status\"] == 403"` | — |
| [SRC-1A176AD4F0-L000241](../../tests/test_hosted_smoke.py#L241) | 241 | `"        assert payload[\"_smoke_http\"][\"request_id\"] == \"request-123\""` | — |
| [SRC-1A176AD4F0-L000242](../../tests/test_hosted_smoke.py#L242) | 242 | `"        assert payload[\"_smoke_http\"][\"cf_ray\"] == \"ray-456\""` | — |
| [SRC-1A176AD4F0-L000243](../../tests/test_hosted_smoke.py#L243) | 243 | `"        assert payload[\"_smoke_http\"][\"body_bytes_sampled\"] == len(b\"<html>blocked</html>\")"` | — |
| [SRC-1A176AD4F0-L000244](../../tests/test_hosted_smoke.py#L244) | 244 | `"        assert \"body_sha256\" in payload[\"_smoke_http\"]"` | — |
| [SRC-1A176AD4F0-L000245](../../tests/test_hosted_smoke.py#L245) | 245 | `"        assert \"blocked\" not in str(payload)"` | — |
| [SRC-1A176AD4F0-L000246](../../tests/test_hosted_smoke.py#L246) | 246 | `"        assert TOKEN not in str(payload)"` | — |
| [SRC-1A176AD4F0-L000247](../../tests/test_hosted_smoke.py#L247) | 247 | `"    finally:"` | — |
| [SRC-1A176AD4F0-L000248](../../tests/test_hosted_smoke.py#L248) | 248 | `"        server.shutdown()"` | — |
| [SRC-1A176AD4F0-L000249](../../tests/test_hosted_smoke.py#L249) | 249 | `"        server.server_close()"` | — |
| [SRC-1A176AD4F0-L000250](../../tests/test_hosted_smoke.py#L250) | 250 | `"        thread.join(timeout=2)"` | — |
| [SRC-1A176AD4F0-L000251](../../tests/test_hosted_smoke.py#L251) | 251 | `""` | — |
| [SRC-1A176AD4F0-L000252](../../tests/test_hosted_smoke.py#L252) | 252 | `""` | — |
| [SRC-1A176AD4F0-L000253](../../tests/test_hosted_smoke.py#L253) | 253 | `""` | — |
| [SRC-1A176AD4F0-L000254](../../tests/test_hosted_smoke.py#L254) | 254 | `"def test_health_403_metadata_is_preserved_in_failure_report(monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000255](../../tests/test_hosted_smoke.py#L255) | 255 | `"    metadata = {"` | — |
| [SRC-1A176AD4F0-L000256](../../tests/test_hosted_smoke.py#L256) | 256 | `"        \"status\": 403,"` | — |
| [SRC-1A176AD4F0-L000257](../../tests/test_hosted_smoke.py#L257) | 257 | `"        \"content_type\": \"text/html\","` | — |
| [SRC-1A176AD4F0-L000258](../../tests/test_hosted_smoke.py#L258) | 258 | `"        \"server\": \"edge-gateway\","` | — |
| [SRC-1A176AD4F0-L000259](../../tests/test_hosted_smoke.py#L259) | 259 | `"        \"request_id\": \"request-403\","` | — |
| [SRC-1A176AD4F0-L000260](../../tests/test_hosted_smoke.py#L260) | 260 | `"        \"correlation_id\": \"\","` | — |
| [SRC-1A176AD4F0-L000261](../../tests/test_hosted_smoke.py#L261) | 261 | `"        \"cf_ray\": \"ray-403\","` | — |
| [SRC-1A176AD4F0-L000262](../../tests/test_hosted_smoke.py#L262) | 262 | `"        \"via\": \"\","` | — |
| [SRC-1A176AD4F0-L000263](../../tests/test_hosted_smoke.py#L263) | 263 | `"        \"body_bytes_sampled\": 19,"` | — |
| [SRC-1A176AD4F0-L000264](../../tests/test_hosted_smoke.py#L264) | 264 | `"        \"body_sha256\": \"a\" * 64,"` | — |
| [SRC-1A176AD4F0-L000265](../../tests/test_hosted_smoke.py#L265) | 265 | `"    }"` | — |
| [SRC-1A176AD4F0-L000266](../../tests/test_hosted_smoke.py#L266) | 266 | `""` | — |
| [SRC-1A176AD4F0-L000267](../../tests/test_hosted_smoke.py#L267) | 267 | `"    def forbidden_health(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000268](../../tests/test_hosted_smoke.py#L268) | 268 | `"        return 403, {\"_smoke_http\": metadata}"` | — |
| [SRC-1A176AD4F0-L000269](../../tests/test_hosted_smoke.py#L269) | 269 | `""` | — |
| [SRC-1A176AD4F0-L000270](../../tests/test_hosted_smoke.py#L270) | 270 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", forbidden_health)"` | — |
| [SRC-1A176AD4F0-L000271](../../tests/test_hosted_smoke.py#L271) | 271 | `"    with pytest.raises(SmokeError, match=\"Health check failed\") as failure:"` | — |
| [SRC-1A176AD4F0-L000272](../../tests/test_hosted_smoke.py#L272) | 272 | `"        run_smoke(\"https://omarai.example.test\", TOKEN, allow_provider_usage=False)"` | — |
| [SRC-1A176AD4F0-L000273](../../tests/test_hosted_smoke.py#L273) | 273 | `"    assert failure.value.report[\"http_response\"] == metadata"` | — |
| [SRC-1A176AD4F0-L000274](../../tests/test_hosted_smoke.py#L274) | 274 | `"    assert \"blocked\" not in str(failure.value.report)"` | — |
| [SRC-1A176AD4F0-L000275](../../tests/test_hosted_smoke.py#L275) | 275 | `""` | — |
| [SRC-1A176AD4F0-L000276](../../tests/test_hosted_smoke.py#L276) | 276 | `""` | — |
| [SRC-1A176AD4F0-L000277](../../tests/test_hosted_smoke.py#L277) | 277 | `""` | — |
| [SRC-1A176AD4F0-L000278](../../tests/test_hosted_smoke.py#L278) | 278 | `"def test_hosted_preflight_allows_remote_no_token_and_still_checks_auth_rejection(monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000279](../../tests/test_hosted_smoke.py#L279) | 279 | `"    calls = []"` | — |
| [SRC-1A176AD4F0-L000280](../../tests/test_hosted_smoke.py#L280) | 280 | `""` | — |
| [SRC-1A176AD4F0-L000281](../../tests/test_hosted_smoke.py#L281) | 281 | `"    def fake_request(url: str, *, token=\"\", payload=None, timeout=90):"` | — |
| [SRC-1A176AD4F0-L000282](../../tests/test_hosted_smoke.py#L282) | 282 | `"        path = urlsplit(url).path"` | — |
| [SRC-1A176AD4F0-L000283](../../tests/test_hosted_smoke.py#L283) | 283 | `"        calls.append((path, token, payload))"` | — |
| [SRC-1A176AD4F0-L000284](../../tests/test_hosted_smoke.py#L284) | 284 | `"        if path == \"/\":"` | — |
| [SRC-1A176AD4F0-L000285](../../tests/test_hosted_smoke.py#L285) | 285 | `"            return 200, None"` | — |
| [SRC-1A176AD4F0-L000286](../../tests/test_hosted_smoke.py#L286) | 286 | `"        if path == \"/api/health\":"` | — |
| [SRC-1A176AD4F0-L000287](../../tests/test_hosted_smoke.py#L287) | 287 | `"            return 200, {\"ok\": True, \"build\": {\"sha\": \"a\" * 40}}"` | — |
| [SRC-1A176AD4F0-L000288](../../tests/test_hosted_smoke.py#L288) | 288 | `"        if path == \"/api/agent\" and not token:"` | — |
| [SRC-1A176AD4F0-L000289](../../tests/test_hosted_smoke.py#L289) | 289 | `"            assert payload == {\"question\": \"\"}"` | — |
| [SRC-1A176AD4F0-L000290](../../tests/test_hosted_smoke.py#L290) | 290 | `"            return 401, None"` | — |
| [SRC-1A176AD4F0-L000291](../../tests/test_hosted_smoke.py#L291) | 291 | `"        raise AssertionError(\"preflight must not call authenticated agent/search/model paths\")"` | — |
| [SRC-1A176AD4F0-L000292](../../tests/test_hosted_smoke.py#L292) | 292 | `""` | — |
| [SRC-1A176AD4F0-L000293](../../tests/test_hosted_smoke.py#L293) | 293 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", fake_request)"` | — |
| [SRC-1A176AD4F0-L000294](../../tests/test_hosted_smoke.py#L294) | 294 | `"    result = run_smoke("` | — |
| [SRC-1A176AD4F0-L000295](../../tests/test_hosted_smoke.py#L295) | 295 | `"        \"https://omarai.example.test\","` | — |
| [SRC-1A176AD4F0-L000296](../../tests/test_hosted_smoke.py#L296) | 296 | `"        \"\","` | — |
| [SRC-1A176AD4F0-L000297](../../tests/test_hosted_smoke.py#L297) | 297 | `"        preflight_only=True,"` | — |
| [SRC-1A176AD4F0-L000298](../../tests/test_hosted_smoke.py#L298) | 298 | `"        allow_provider_usage=False,"` | — |
| [SRC-1A176AD4F0-L000299](../../tests/test_hosted_smoke.py#L299) | 299 | `"    )"` | — |
| [SRC-1A176AD4F0-L000300](../../tests/test_hosted_smoke.py#L300) | 300 | `"    assert result[\"result\"] == \"preflight_passed\""` | — |
| [SRC-1A176AD4F0-L000301](../../tests/test_hosted_smoke.py#L301) | 301 | `"    assert result[\"auth_mode\"] == \"preflight_no_token\""` | — |
| [SRC-1A176AD4F0-L000302](../../tests/test_hosted_smoke.py#L302) | 302 | `"    assert result[\"checks\"][\"authentication\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000303](../../tests/test_hosted_smoke.py#L303) | 303 | `"    assert result[\"checks\"][\"homepage\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000304](../../tests/test_hosted_smoke.py#L304) | 304 | `"    assert result[\"endpoint_diagnostics\"][\"homepage\"][\"http_status\"] == 200"` | — |
| [SRC-1A176AD4F0-L000305](../../tests/test_hosted_smoke.py#L305) | 305 | `"    assert result[\"endpoint_diagnostics\"][\"health\"][\"http_status\"] == 200"` | — |
| [SRC-1A176AD4F0-L000306](../../tests/test_hosted_smoke.py#L306) | 306 | `"    assert result[\"endpoint_diagnostics\"][\"unauthenticated_agent\"][\"http_status\"] == 401"` | — |
| [SRC-1A176AD4F0-L000307](../../tests/test_hosted_smoke.py#L307) | 307 | `"    assert calls == [(\"/\", \"\", None), (\"/api/health\", \"\", None), (\"/api/agent\", \"\", {\"question\": \"\"})]"` | — |
| [SRC-1A176AD4F0-L000308](../../tests/test_hosted_smoke.py#L308) | 308 | `""` | — |
| [SRC-1A176AD4F0-L000309](../../tests/test_hosted_smoke.py#L309) | 309 | `""` | — |
| [SRC-1A176AD4F0-L000310](../../tests/test_hosted_smoke.py#L310) | 310 | `""` | — |
| [SRC-1A176AD4F0-L000311](../../tests/test_hosted_smoke.py#L311) | 311 | `""` | — |
| [SRC-1A176AD4F0-L000312](../../tests/test_hosted_smoke.py#L312) | 312 | `"def test_preflight_fails_closed_if_unauthenticated_agent_probe_reaches_validation(monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000313](../../tests/test_hosted_smoke.py#L313) | 313 | `"    calls = []"` | — |
| [SRC-1A176AD4F0-L000314](../../tests/test_hosted_smoke.py#L314) | 314 | `""` | — |
| [SRC-1A176AD4F0-L000315](../../tests/test_hosted_smoke.py#L315) | 315 | `"    def auth_bypass(url: str, *, token=\"\", payload=None, timeout=90):"` | — |
| [SRC-1A176AD4F0-L000316](../../tests/test_hosted_smoke.py#L316) | 316 | `"        path = urlsplit(url).path"` | — |
| [SRC-1A176AD4F0-L000317](../../tests/test_hosted_smoke.py#L317) | 317 | `"        calls.append((path, token, payload))"` | — |
| [SRC-1A176AD4F0-L000318](../../tests/test_hosted_smoke.py#L318) | 318 | `"        if path == \"/\":"` | — |
| [SRC-1A176AD4F0-L000319](../../tests/test_hosted_smoke.py#L319) | 319 | `"            return 200, None"` | — |
| [SRC-1A176AD4F0-L000320](../../tests/test_hosted_smoke.py#L320) | 320 | `"        if path == \"/api/health\":"` | — |
| [SRC-1A176AD4F0-L000321](../../tests/test_hosted_smoke.py#L321) | 321 | `"            return 200, {\"ok\": True}"` | — |
| [SRC-1A176AD4F0-L000322](../../tests/test_hosted_smoke.py#L322) | 322 | `"        if path == \"/api/agent\" and not token:"` | — |
| [SRC-1A176AD4F0-L000323](../../tests/test_hosted_smoke.py#L323) | 323 | `"            assert payload == {\"question\": \"\"}"` | — |
| [SRC-1A176AD4F0-L000324](../../tests/test_hosted_smoke.py#L324) | 324 | `"            # The API reached question validation, so its auth gate did not reject first."` | — |
| [SRC-1A176AD4F0-L000325](../../tests/test_hosted_smoke.py#L325) | 325 | `"            return 400, {\"error\": \"question must be a non-empty string\"}"` | — |
| [SRC-1A176AD4F0-L000326](../../tests/test_hosted_smoke.py#L326) | 326 | `"        raise AssertionError(\"no authenticated agent request is allowed in preflight\")"` | — |
| [SRC-1A176AD4F0-L000327](../../tests/test_hosted_smoke.py#L327) | 327 | `""` | — |
| [SRC-1A176AD4F0-L000328](../../tests/test_hosted_smoke.py#L328) | 328 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", auth_bypass)"` | — |
| [SRC-1A176AD4F0-L000329](../../tests/test_hosted_smoke.py#L329) | 329 | `"    with pytest.raises(SmokeError, match=\"per-endpoint HTTP diagnostics\") as failure:"` | — |
| [SRC-1A176AD4F0-L000330](../../tests/test_hosted_smoke.py#L330) | 330 | `"        run_smoke(\"https://omarai.example.test\", \"\", preflight_only=True)"` | — |
| [SRC-1A176AD4F0-L000331](../../tests/test_hosted_smoke.py#L331) | 331 | `"    assert calls == [(\"/\", \"\", None), (\"/api/health\", \"\", None), (\"/api/agent\", \"\", {\"question\": \"\"})]"` | — |
| [SRC-1A176AD4F0-L000332](../../tests/test_hosted_smoke.py#L332) | 332 | `"    assert failure.value.report[\"endpoint_diagnostics\"][\"unauthenticated_agent\"][\"http_status\"] == 400"` | — |
| [SRC-1A176AD4F0-L000333](../../tests/test_hosted_smoke.py#L333) | 333 | `""` | — |
| [SRC-1A176AD4F0-L000334](../../tests/test_hosted_smoke.py#L334) | 334 | `""` | — |
| [SRC-1A176AD4F0-L000335](../../tests/test_hosted_smoke.py#L335) | 335 | `""` | — |
| [SRC-1A176AD4F0-L000336](../../tests/test_hosted_smoke.py#L336) | 336 | `""` | — |
| [SRC-1A176AD4F0-L000337](../../tests/test_hosted_smoke.py#L337) | 337 | `"def test_no_cost_preflight_rejects_a_mismatched_expected_build_sha(monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000338](../../tests/test_hosted_smoke.py#L338) | 338 | `"    def request_with_wrong_sha(url: str, *, token=\"\", payload=None, timeout=90):"` | — |
| [SRC-1A176AD4F0-L000339](../../tests/test_hosted_smoke.py#L339) | 339 | `"        path = urlsplit(url).path"` | — |
| [SRC-1A176AD4F0-L000340](../../tests/test_hosted_smoke.py#L340) | 340 | `"        if path == \"/\":"` | — |
| [SRC-1A176AD4F0-L000341](../../tests/test_hosted_smoke.py#L341) | 341 | `"            return 200, None"` | — |
| [SRC-1A176AD4F0-L000342](../../tests/test_hosted_smoke.py#L342) | 342 | `"        if path == \"/api/health\":"` | — |
| [SRC-1A176AD4F0-L000343](../../tests/test_hosted_smoke.py#L343) | 343 | `"            return 200, {\"ok\": True, \"build\": {\"sha\": \"b\" * 40}}"` | — |
| [SRC-1A176AD4F0-L000344](../../tests/test_hosted_smoke.py#L344) | 344 | `"        if path == \"/api/agent\":"` | — |
| [SRC-1A176AD4F0-L000345](../../tests/test_hosted_smoke.py#L345) | 345 | `"            assert payload == {\"question\": \"\"}"` | — |
| [SRC-1A176AD4F0-L000346](../../tests/test_hosted_smoke.py#L346) | 346 | `"            return 401, None"` | — |
| [SRC-1A176AD4F0-L000347](../../tests/test_hosted_smoke.py#L347) | 347 | `"        raise AssertionError(path)"` | — |
| [SRC-1A176AD4F0-L000348](../../tests/test_hosted_smoke.py#L348) | 348 | `""` | — |
| [SRC-1A176AD4F0-L000349](../../tests/test_hosted_smoke.py#L349) | 349 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", request_with_wrong_sha)"` | — |
| [SRC-1A176AD4F0-L000350](../../tests/test_hosted_smoke.py#L350) | 350 | `"    with pytest.raises(SmokeError, match=\"per-endpoint HTTP diagnostics\") as failure:"` | — |
| [SRC-1A176AD4F0-L000351](../../tests/test_hosted_smoke.py#L351) | 351 | `"        run_smoke("` | — |
| [SRC-1A176AD4F0-L000352](../../tests/test_hosted_smoke.py#L352) | 352 | `"            \"https://omarai.example.test\", \"\","` | — |
| [SRC-1A176AD4F0-L000353](../../tests/test_hosted_smoke.py#L353) | 353 | `"            expected_sha=\"a\" * 40, preflight_only=True,"` | — |
| [SRC-1A176AD4F0-L000354](../../tests/test_hosted_smoke.py#L354) | 354 | `"        )"` | — |
| [SRC-1A176AD4F0-L000355](../../tests/test_hosted_smoke.py#L355) | 355 | `"    assert failure.value.report[\"checks\"][\"build_identity\"][\"status\"] == \"failed\""` | — |
| [SRC-1A176AD4F0-L000356](../../tests/test_hosted_smoke.py#L356) | 356 | `""` | — |
| [SRC-1A176AD4F0-L000357](../../tests/test_hosted_smoke.py#L357) | 357 | `""` | — |
| [SRC-1A176AD4F0-L000358](../../tests/test_hosted_smoke.py#L358) | 358 | `"def test_no_cost_preflight_collects_all_endpoint_failures_without_request_bodies(monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000359](../../tests/test_hosted_smoke.py#L359) | 359 | `"    calls = []"` | — |
| [SRC-1A176AD4F0-L000360](../../tests/test_hosted_smoke.py#L360) | 360 | `"    body_digest = \"b\" * 64"` | — |
| [SRC-1A176AD4F0-L000361](../../tests/test_hosted_smoke.py#L361) | 361 | `"    metadata = {"` | — |
| [SRC-1A176AD4F0-L000362](../../tests/test_hosted_smoke.py#L362) | 362 | `"        \"status\": 403,"` | — |
| [SRC-1A176AD4F0-L000363](../../tests/test_hosted_smoke.py#L363) | 363 | `"        \"content_type\": \"application/json\","` | — |
| [SRC-1A176AD4F0-L000364](../../tests/test_hosted_smoke.py#L364) | 364 | `"        \"server\": \"cloudflare\","` | — |
| [SRC-1A176AD4F0-L000365](../../tests/test_hosted_smoke.py#L365) | 365 | `"        \"request_id\": \"\","` | — |
| [SRC-1A176AD4F0-L000366](../../tests/test_hosted_smoke.py#L366) | 366 | `"        \"correlation_id\": \"\","` | — |
| [SRC-1A176AD4F0-L000367](../../tests/test_hosted_smoke.py#L367) | 367 | `"        \"cf_ray\": \"ray-example-403\","` | — |
| [SRC-1A176AD4F0-L000368](../../tests/test_hosted_smoke.py#L368) | 368 | `"        \"via\": \"\","` | — |
| [SRC-1A176AD4F0-L000369](../../tests/test_hosted_smoke.py#L369) | 369 | `"        \"body_bytes_sampled\": 128,"` | — |
| [SRC-1A176AD4F0-L000370](../../tests/test_hosted_smoke.py#L370) | 370 | `"        \"body_sha256\": body_digest,"` | — |
| [SRC-1A176AD4F0-L000371](../../tests/test_hosted_smoke.py#L371) | 371 | `"    }"` | — |
| [SRC-1A176AD4F0-L000372](../../tests/test_hosted_smoke.py#L372) | 372 | `""` | — |
| [SRC-1A176AD4F0-L000373](../../tests/test_hosted_smoke.py#L373) | 373 | `"    def blocked_request(url: str, *, token=\"\", payload=None, timeout=90):"` | — |
| [SRC-1A176AD4F0-L000374](../../tests/test_hosted_smoke.py#L374) | 374 | `"        path = urlsplit(url).path"` | — |
| [SRC-1A176AD4F0-L000375](../../tests/test_hosted_smoke.py#L375) | 375 | `"        calls.append((path, token, payload))"` | — |
| [SRC-1A176AD4F0-L000376](../../tests/test_hosted_smoke.py#L376) | 376 | `"        if path in {\"/\", \"/api/health\"}:"` | — |
| [SRC-1A176AD4F0-L000377](../../tests/test_hosted_smoke.py#L377) | 377 | `"            return 403, {\"_smoke_http\": metadata}"` | — |
| [SRC-1A176AD4F0-L000378](../../tests/test_hosted_smoke.py#L378) | 378 | `"        if path == \"/api/agent\":"` | — |
| [SRC-1A176AD4F0-L000379](../../tests/test_hosted_smoke.py#L379) | 379 | `"            assert payload == {\"question\": \"\"}"` | — |
| [SRC-1A176AD4F0-L000380](../../tests/test_hosted_smoke.py#L380) | 380 | `"            return 403, {\"_smoke_http\": {**metadata, \"cf_ray\": \"ray-example-agent\"}}"` | — |
| [SRC-1A176AD4F0-L000381](../../tests/test_hosted_smoke.py#L381) | 381 | `"        raise AssertionError(f\"unexpected preflight request: {path}\")"` | — |
| [SRC-1A176AD4F0-L000382](../../tests/test_hosted_smoke.py#L382) | 382 | `""` | — |
| [SRC-1A176AD4F0-L000383](../../tests/test_hosted_smoke.py#L383) | 383 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", blocked_request)"` | — |
| [SRC-1A176AD4F0-L000384](../../tests/test_hosted_smoke.py#L384) | 384 | `"    with pytest.raises(SmokeError, match=\"per-endpoint HTTP diagnostics\") as failure:"` | — |
| [SRC-1A176AD4F0-L000385](../../tests/test_hosted_smoke.py#L385) | 385 | `"        run_smoke(\"https://omarai.example.test\", \"\", preflight_only=True)"` | — |
| [SRC-1A176AD4F0-L000386](../../tests/test_hosted_smoke.py#L386) | 386 | `""` | — |
| [SRC-1A176AD4F0-L000387](../../tests/test_hosted_smoke.py#L387) | 387 | `"    report = failure.value.report"` | — |
| [SRC-1A176AD4F0-L000388](../../tests/test_hosted_smoke.py#L388) | 388 | `"    assert calls == ["` | — |
| [SRC-1A176AD4F0-L000389](../../tests/test_hosted_smoke.py#L389) | 389 | `"        (\"/\", \"\", None),"` | — |
| [SRC-1A176AD4F0-L000390](../../tests/test_hosted_smoke.py#L390) | 390 | `"        (\"/api/health\", \"\", None),"` | — |
| [SRC-1A176AD4F0-L000391](../../tests/test_hosted_smoke.py#L391) | 391 | `"        (\"/api/agent\", \"\", {\"question\": \"\"}),"` | — |
| [SRC-1A176AD4F0-L000392](../../tests/test_hosted_smoke.py#L392) | 392 | `"    ]"` | — |
| [SRC-1A176AD4F0-L000393](../../tests/test_hosted_smoke.py#L393) | 393 | `"    assert set(report[\"http_responses\"]) == {"` | — |
| [SRC-1A176AD4F0-L000394](../../tests/test_hosted_smoke.py#L394) | 394 | `"        \"homepage\", \"health\", \"unauthenticated_agent\""` | — |
| [SRC-1A176AD4F0-L000395](../../tests/test_hosted_smoke.py#L395) | 395 | `"    }"` | — |
| [SRC-1A176AD4F0-L000396](../../tests/test_hosted_smoke.py#L396) | 396 | `"    assert report[\"endpoint_diagnostics\"][\"homepage\"][\"http_status\"] == 403"` | — |
| [SRC-1A176AD4F0-L000397](../../tests/test_hosted_smoke.py#L397) | 397 | `"    assert report[\"endpoint_diagnostics\"][\"health\"][\"http_status\"] == 403"` | — |
| [SRC-1A176AD4F0-L000398](../../tests/test_hosted_smoke.py#L398) | 398 | `"    assert report[\"endpoint_diagnostics\"][\"unauthenticated_agent\"][\"http_status\"] == 403"` | — |
| [SRC-1A176AD4F0-L000399](../../tests/test_hosted_smoke.py#L399) | 399 | `"    assert report[\"http_responses\"][\"health\"][\"cf_ray\"] == \"ray-example-403\""` | — |
| [SRC-1A176AD4F0-L000400](../../tests/test_hosted_smoke.py#L400) | 400 | `"    assert \"body_sha256\" in report[\"http_responses\"][\"health\"]"` | — |
| [SRC-1A176AD4F0-L000401](../../tests/test_hosted_smoke.py#L401) | 401 | `"    assert \"blocked\" not in str(report)"` | — |
| [SRC-1A176AD4F0-L000402](../../tests/test_hosted_smoke.py#L402) | 402 | `"    assert \"b\" * 128 not in str(report)"` | — |
| [SRC-1A176AD4F0-L000403](../../tests/test_hosted_smoke.py#L403) | 403 | `"    assert TOKEN not in str(report)"` | — |
| [SRC-1A176AD4F0-L000404](../../tests/test_hosted_smoke.py#L404) | 404 | `""` | — |
| [SRC-1A176AD4F0-L000405](../../tests/test_hosted_smoke.py#L405) | 405 | `""` | — |
| [SRC-1A176AD4F0-L000406](../../tests/test_hosted_smoke.py#L406) | 406 | `"def test_no_cost_preflight_keeps_probing_when_only_health_route_is_blocked(monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000407](../../tests/test_hosted_smoke.py#L407) | 407 | `"    calls = []"` | — |
| [SRC-1A176AD4F0-L000408](../../tests/test_hosted_smoke.py#L408) | 408 | `""` | — |
| [SRC-1A176AD4F0-L000409](../../tests/test_hosted_smoke.py#L409) | 409 | `"    def request_with_health_block(url: str, *, token=\"\", payload=None, timeout=90):"` | — |
| [SRC-1A176AD4F0-L000410](../../tests/test_hosted_smoke.py#L410) | 410 | `"        path = urlsplit(url).path"` | — |
| [SRC-1A176AD4F0-L000411](../../tests/test_hosted_smoke.py#L411) | 411 | `"        calls.append(path)"` | — |
| [SRC-1A176AD4F0-L000412](../../tests/test_hosted_smoke.py#L412) | 412 | `"        if path == \"/\":"` | — |
| [SRC-1A176AD4F0-L000413](../../tests/test_hosted_smoke.py#L413) | 413 | `"            return 200, None"` | — |
| [SRC-1A176AD4F0-L000414](../../tests/test_hosted_smoke.py#L414) | 414 | `"        if path == \"/api/health\":"` | — |
| [SRC-1A176AD4F0-L000415](../../tests/test_hosted_smoke.py#L415) | 415 | `"            return 403, {\"_smoke_http\": {\"status\": 403, \"cf_ray\": \"health-ray\"}}"` | — |
| [SRC-1A176AD4F0-L000416](../../tests/test_hosted_smoke.py#L416) | 416 | `"        if path == \"/api/agent\":"` | — |
| [SRC-1A176AD4F0-L000417](../../tests/test_hosted_smoke.py#L417) | 417 | `"            return 401, None"` | — |
| [SRC-1A176AD4F0-L000418](../../tests/test_hosted_smoke.py#L418) | 418 | `"        raise AssertionError(path)"` | — |
| [SRC-1A176AD4F0-L000419](../../tests/test_hosted_smoke.py#L419) | 419 | `""` | — |
| [SRC-1A176AD4F0-L000420](../../tests/test_hosted_smoke.py#L420) | 420 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", request_with_health_block)"` | — |
| [SRC-1A176AD4F0-L000421](../../tests/test_hosted_smoke.py#L421) | 421 | `"    with pytest.raises(SmokeError) as failure:"` | — |
| [SRC-1A176AD4F0-L000422](../../tests/test_hosted_smoke.py#L422) | 422 | `"        run_smoke(\"https://omarai.example.test\", \"\", preflight_only=True)"` | — |
| [SRC-1A176AD4F0-L000423](../../tests/test_hosted_smoke.py#L423) | 423 | `""` | — |
| [SRC-1A176AD4F0-L000424](../../tests/test_hosted_smoke.py#L424) | 424 | `"    assert calls == [\"/\", \"/api/health\", \"/api/agent\"]"` | — |
| [SRC-1A176AD4F0-L000425](../../tests/test_hosted_smoke.py#L425) | 425 | `"    diagnostics = failure.value.report[\"endpoint_diagnostics\"]"` | — |
| [SRC-1A176AD4F0-L000426](../../tests/test_hosted_smoke.py#L426) | 426 | `"    assert diagnostics[\"homepage\"][\"status\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000427](../../tests/test_hosted_smoke.py#L427) | 427 | `"    assert diagnostics[\"health\"][\"status\"] == \"failed\""` | — |
| [SRC-1A176AD4F0-L000428](../../tests/test_hosted_smoke.py#L428) | 428 | `"    assert diagnostics[\"unauthenticated_agent\"][\"status\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000429](../../tests/test_hosted_smoke.py#L429) | 429 | `""` | — |
| [SRC-1A176AD4F0-L000430](../../tests/test_hosted_smoke.py#L430) | 430 | `""` | — |
| [SRC-1A176AD4F0-L000431](../../tests/test_hosted_smoke.py#L431) | 431 | `""` | — |
| [SRC-1A176AD4F0-L000432](../../tests/test_hosted_smoke.py#L432) | 432 | `""` | — |
| [SRC-1A176AD4F0-L000433](../../tests/test_hosted_smoke.py#L433) | 433 | `"def test_smoke_preflight_runs_without_provider_usage_or_model_calls(hosted_server):"` | — |
| [SRC-1A176AD4F0-L000434](../../tests/test_hosted_smoke.py#L434) | 434 | `"    result = run_smoke("` | — |
| [SRC-1A176AD4F0-L000435](../../tests/test_hosted_smoke.py#L435) | 435 | `"        hosted_server, TOKEN, allow_http=True, preflight_only=True, allow_provider_usage=False, timeout=5"` | — |
| [SRC-1A176AD4F0-L000436](../../tests/test_hosted_smoke.py#L436) | 436 | `"    )"` | — |
| [SRC-1A176AD4F0-L000437](../../tests/test_hosted_smoke.py#L437) | 437 | `"    assert result[\"result\"] == \"preflight_passed\""` | — |
| [SRC-1A176AD4F0-L000438](../../tests/test_hosted_smoke.py#L438) | 438 | `"    assert result[\"checks\"][\"health\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000439](../../tests/test_hosted_smoke.py#L439) | 439 | `"    assert result[\"checks\"][\"authentication\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000440](../../tests/test_hosted_smoke.py#L440) | 440 | `"    assert result[\"checks\"][\"provider_usage\"][\"status\"] == \"skipped_not_approved\""` | — |
| [SRC-1A176AD4F0-L000441](../../tests/test_hosted_smoke.py#L441) | 441 | `"    assert result[\"transcript\"] == []"` | — |
| [SRC-1A176AD4F0-L000442](../../tests/test_hosted_smoke.py#L442) | 442 | `""` | — |
| [SRC-1A176AD4F0-L000443](../../tests/test_hosted_smoke.py#L443) | 443 | `""` | — |
| [SRC-1A176AD4F0-L000444](../../tests/test_hosted_smoke.py#L444) | 444 | `"def test_smoke_requires_provider_approval_after_no_cost_preflight(monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000445](../../tests/test_hosted_smoke.py#L445) | 445 | `"    calls = []"` | — |
| [SRC-1A176AD4F0-L000446](../../tests/test_hosted_smoke.py#L446) | 446 | `""` | — |
| [SRC-1A176AD4F0-L000447](../../tests/test_hosted_smoke.py#L447) | 447 | `"    def fake_request(url, *, token=\"\", payload=None, timeout=90):"` | — |
| [SRC-1A176AD4F0-L000448](../../tests/test_hosted_smoke.py#L448) | 448 | `"        calls.append((urlsplit(url).path, token, payload))"` | — |
| [SRC-1A176AD4F0-L000449](../../tests/test_hosted_smoke.py#L449) | 449 | `"        if url.endswith(\"/api/health\"):"` | — |
| [SRC-1A176AD4F0-L000450](../../tests/test_hosted_smoke.py#L450) | 450 | `"            return 200, {\"ok\": True}"` | — |
| [SRC-1A176AD4F0-L000451](../../tests/test_hosted_smoke.py#L451) | 451 | `"        if url.endswith(\"/api/agent\") and not token:"` | — |
| [SRC-1A176AD4F0-L000452](../../tests/test_hosted_smoke.py#L452) | 452 | `"            assert payload == {\"question\": \"\"}"` | — |
| [SRC-1A176AD4F0-L000453](../../tests/test_hosted_smoke.py#L453) | 453 | `"            return 401, None"` | — |
| [SRC-1A176AD4F0-L000454](../../tests/test_hosted_smoke.py#L454) | 454 | `"        raise AssertionError(\"provider-dependent request must not run without approval\")"` | — |
| [SRC-1A176AD4F0-L000455](../../tests/test_hosted_smoke.py#L455) | 455 | `""` | — |
| [SRC-1A176AD4F0-L000456](../../tests/test_hosted_smoke.py#L456) | 456 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", fake_request)"` | — |
| [SRC-1A176AD4F0-L000457](../../tests/test_hosted_smoke.py#L457) | 457 | `"    with pytest.raises(SmokeError, match=\"explicit human approval\") as failure:"` | — |
| [SRC-1A176AD4F0-L000458](../../tests/test_hosted_smoke.py#L458) | 458 | `"        run_smoke(\"https://omarai.example.test\", TOKEN, allow_provider_usage=False)"` | — |
| [SRC-1A176AD4F0-L000459](../../tests/test_hosted_smoke.py#L459) | 459 | `"    assert calls == [(\"/api/health\", \"\", None), (\"/api/agent\", \"\", {\"question\": \"\"})]"` | — |
| [SRC-1A176AD4F0-L000460](../../tests/test_hosted_smoke.py#L460) | 460 | `"    assert failure.value.report[\"checks\"][\"authentication\"] == \"passed\""` | — |
| [SRC-1A176AD4F0-L000461](../../tests/test_hosted_smoke.py#L461) | 461 | `"    assert failure.value.report[\"checks\"][\"provider_usage\"][\"status\"] == \"blocked_not_approved\""` | — |
| [SRC-1A176AD4F0-L000462](../../tests/test_hosted_smoke.py#L462) | 462 | `""` | — |
| [SRC-1A176AD4F0-L000463](../../tests/test_hosted_smoke.py#L463) | 463 | `""` | — |
| [SRC-1A176AD4F0-L000464](../../tests/test_hosted_smoke.py#L464) | 464 | `"def test_smoke_rejects_empty_agent_answer(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000465](../../tests/test_hosted_smoke.py#L465) | 465 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000466](../../tests/test_hosted_smoke.py#L466) | 466 | `""` | — |
| [SRC-1A176AD4F0-L000467](../../tests/test_hosted_smoke.py#L467) | 467 | `"    def empty_answer(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000468](../../tests/test_hosted_smoke.py#L468) | 468 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000469](../../tests/test_hosted_smoke.py#L469) | 469 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000470](../../tests/test_hosted_smoke.py#L470) | 470 | `"                \"answer\": \"  \", \"used_web_search\": True, \"used_language_model\": True,"` | — |
| [SRC-1A176AD4F0-L000471](../../tests/test_hosted_smoke.py#L471) | 471 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1A176AD4F0-L000472](../../tests/test_hosted_smoke.py#L472) | 472 | `"                \"sources\": [{\"url\": \"https://example.com/source\"}],"` | — |
| [SRC-1A176AD4F0-L000473](../../tests/test_hosted_smoke.py#L473) | 473 | `"                \"search_report\": {"` | — |
| [SRC-1A176AD4F0-L000474](../../tests/test_hosted_smoke.py#L474) | 474 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1A176AD4F0-L000475](../../tests/test_hosted_smoke.py#L475) | 475 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_all_claims_supported\"},"` | — |
| [SRC-1A176AD4F0-L000476](../../tests/test_hosted_smoke.py#L476) | 476 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1A176AD4F0-L000477](../../tests/test_hosted_smoke.py#L477) | 477 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1A176AD4F0-L000478](../../tests/test_hosted_smoke.py#L478) | 478 | `"                },"` | — |
| [SRC-1A176AD4F0-L000479](../../tests/test_hosted_smoke.py#L479) | 479 | `"            }"` | — |
| [SRC-1A176AD4F0-L000480](../../tests/test_hosted_smoke.py#L480) | 480 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000481](../../tests/test_hosted_smoke.py#L481) | 481 | `""` | — |
| [SRC-1A176AD4F0-L000482](../../tests/test_hosted_smoke.py#L482) | 482 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", empty_answer)"` | — |
| [SRC-1A176AD4F0-L000483](../../tests/test_hosted_smoke.py#L483) | 483 | `"    with pytest.raises(SmokeError, match=\"empty or whitespace-only answer\"):"` | — |
| [SRC-1A176AD4F0-L000484](../../tests/test_hosted_smoke.py#L484) | 484 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000485](../../tests/test_hosted_smoke.py#L485) | 485 | `""` | — |
| [SRC-1A176AD4F0-L000486](../../tests/test_hosted_smoke.py#L486) | 486 | `""` | — |
| [SRC-1A176AD4F0-L000487](../../tests/test_hosted_smoke.py#L487) | 487 | `""` | — |
| [SRC-1A176AD4F0-L000488](../../tests/test_hosted_smoke.py#L488) | 488 | `"def test_smoke_rejects_non_string_agent_answer(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000489](../../tests/test_hosted_smoke.py#L489) | 489 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000490](../../tests/test_hosted_smoke.py#L490) | 490 | `""` | — |
| [SRC-1A176AD4F0-L000491](../../tests/test_hosted_smoke.py#L491) | 491 | `"    def non_string_answer(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000492](../../tests/test_hosted_smoke.py#L492) | 492 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000493](../../tests/test_hosted_smoke.py#L493) | 493 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000494](../../tests/test_hosted_smoke.py#L494) | 494 | `"                \"answer\": None, \"used_web_search\": True, \"used_language_model\": True,"` | — |
| [SRC-1A176AD4F0-L000495](../../tests/test_hosted_smoke.py#L495) | 495 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1A176AD4F0-L000496](../../tests/test_hosted_smoke.py#L496) | 496 | `"                \"sources\": [{\"url\": \"https://example.com/source\"}],"` | — |
| [SRC-1A176AD4F0-L000497](../../tests/test_hosted_smoke.py#L497) | 497 | `"                \"search_report\": {"` | — |
| [SRC-1A176AD4F0-L000498](../../tests/test_hosted_smoke.py#L498) | 498 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1A176AD4F0-L000499](../../tests/test_hosted_smoke.py#L499) | 499 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_all_claims_supported\"},"` | — |
| [SRC-1A176AD4F0-L000500](../../tests/test_hosted_smoke.py#L500) | 500 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1A176AD4F0-L000501](../../tests/test_hosted_smoke.py#L501) | 501 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1A176AD4F0-L000502](../../tests/test_hosted_smoke.py#L502) | 502 | `"                },"` | — |
| [SRC-1A176AD4F0-L000503](../../tests/test_hosted_smoke.py#L503) | 503 | `"            }"` | — |
| [SRC-1A176AD4F0-L000504](../../tests/test_hosted_smoke.py#L504) | 504 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000505](../../tests/test_hosted_smoke.py#L505) | 505 | `""` | — |
| [SRC-1A176AD4F0-L000506](../../tests/test_hosted_smoke.py#L506) | 506 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", non_string_answer)"` | — |
| [SRC-1A176AD4F0-L000507](../../tests/test_hosted_smoke.py#L507) | 507 | `"    with pytest.raises(SmokeError, match=\"empty or whitespace-only answer\"):"` | — |
| [SRC-1A176AD4F0-L000508](../../tests/test_hosted_smoke.py#L508) | 508 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000509](../../tests/test_hosted_smoke.py#L509) | 509 | `""` | — |
| [SRC-1A176AD4F0-L000510](../../tests/test_hosted_smoke.py#L510) | 510 | `""` | — |
| [SRC-1A176AD4F0-L000511](../../tests/test_hosted_smoke.py#L511) | 511 | `"def test_smoke_rejects_partial_pipeline_even_with_sources(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000512](../../tests/test_hosted_smoke.py#L512) | 512 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000513](../../tests/test_hosted_smoke.py#L513) | 513 | `""` | — |
| [SRC-1A176AD4F0-L000514](../../tests/test_hosted_smoke.py#L514) | 514 | `"    def partial_pipeline(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000515](../../tests/test_hosted_smoke.py#L515) | 515 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000516](../../tests/test_hosted_smoke.py#L516) | 516 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000517](../../tests/test_hosted_smoke.py#L517) | 517 | `"                \"answer\": \"إجابة جزئية [المصدر 1]\", \"used_web_search\": True,"` | — |
| [SRC-1A176AD4F0-L000518](../../tests/test_hosted_smoke.py#L518) | 518 | `"                \"used_language_model\": True,"` | — |
| [SRC-1A176AD4F0-L000519](../../tests/test_hosted_smoke.py#L519) | 519 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1A176AD4F0-L000520](../../tests/test_hosted_smoke.py#L520) | 520 | `"                \"sources\": [{\"url\": \"https://example.com/source\"}],"` | — |
| [SRC-1A176AD4F0-L000521](../../tests/test_hosted_smoke.py#L521) | 521 | `"                \"request_budget\": {\"profile\": \"hosted_smoke\", \"timeout_seconds\": 75, \"budget_exhausted\": False, \"deadline_exceeded\": False, \"limits\": {\"search_queries\": 3, \"search_calls\": 12, \"model_calls\": 6, \"page_fetches\": 4, \"tool_calls\": 0}, \"counts\": {\"search_queries\": 2, \"search_calls\": 4, \"model_calls\": 4, \"page_fetches\": 1, \"tool_calls\": 0}},"` | — |
| [SRC-1A176AD4F0-L000522](../../tests/test_hosted_smoke.py#L522) | 522 | `"                \"search_report\": {"` | — |
| [SRC-1A176AD4F0-L000523](../../tests/test_hosted_smoke.py#L523) | 523 | `"                    \"pipeline_completion_status\": \"partial\","` | — |
| [SRC-1A176AD4F0-L000524](../../tests/test_hosted_smoke.py#L524) | 524 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_all_claims_supported\"},"` | — |
| [SRC-1A176AD4F0-L000525](../../tests/test_hosted_smoke.py#L525) | 525 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1A176AD4F0-L000526](../../tests/test_hosted_smoke.py#L526) | 526 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1A176AD4F0-L000527](../../tests/test_hosted_smoke.py#L527) | 527 | `"                },"` | — |
| [SRC-1A176AD4F0-L000528](../../tests/test_hosted_smoke.py#L528) | 528 | `"            }"` | — |
| [SRC-1A176AD4F0-L000529](../../tests/test_hosted_smoke.py#L529) | 529 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000530](../../tests/test_hosted_smoke.py#L530) | 530 | `""` | — |
| [SRC-1A176AD4F0-L000531](../../tests/test_hosted_smoke.py#L531) | 531 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", partial_pipeline)"` | — |
| [SRC-1A176AD4F0-L000532](../../tests/test_hosted_smoke.py#L532) | 532 | `"    with pytest.raises(SmokeError, match=\"pipeline did not complete\"):"` | — |
| [SRC-1A176AD4F0-L000533](../../tests/test_hosted_smoke.py#L533) | 533 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000534](../../tests/test_hosted_smoke.py#L534) | 534 | `""` | — |
| [SRC-1A176AD4F0-L000535](../../tests/test_hosted_smoke.py#L535) | 535 | `""` | — |
| [SRC-1A176AD4F0-L000536](../../tests/test_hosted_smoke.py#L536) | 536 | `"def test_smoke_rejects_unvalidated_answer_evidence(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000537](../../tests/test_hosted_smoke.py#L537) | 537 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000538](../../tests/test_hosted_smoke.py#L538) | 538 | `""` | — |
| [SRC-1A176AD4F0-L000539](../../tests/test_hosted_smoke.py#L539) | 539 | `"    def invalid_evidence(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000540](../../tests/test_hosted_smoke.py#L540) | 540 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000541](../../tests/test_hosted_smoke.py#L541) | 541 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000542](../../tests/test_hosted_smoke.py#L542) | 542 | `"                \"answer\": \"إجابة بلا إحالات صالحة\", \"used_web_search\": True,"` | — |
| [SRC-1A176AD4F0-L000543](../../tests/test_hosted_smoke.py#L543) | 543 | `"                \"used_language_model\": True, \"answer_evidence_status\": \"not_assessed\","` | — |
| [SRC-1A176AD4F0-L000544](../../tests/test_hosted_smoke.py#L544) | 544 | `"                \"sources\": [{\"url\": \"https://example.com/source\"}],"` | — |
| [SRC-1A176AD4F0-L000545](../../tests/test_hosted_smoke.py#L545) | 545 | `"                \"request_budget\": {\"profile\": \"hosted_smoke\", \"timeout_seconds\": 75, \"budget_exhausted\": False, \"deadline_exceeded\": False, \"limits\": {\"search_queries\": 3, \"search_calls\": 12, \"model_calls\": 6, \"page_fetches\": 4, \"tool_calls\": 0}, \"counts\": {\"search_queries\": 2, \"search_calls\": 4, \"model_calls\": 4, \"page_fetches\": 1, \"tool_calls\": 0}},"` | — |
| [SRC-1A176AD4F0-L000546](../../tests/test_hosted_smoke.py#L546) | 546 | `"                \"search_report\": {"` | — |
| [SRC-1A176AD4F0-L000547](../../tests/test_hosted_smoke.py#L547) | 547 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1A176AD4F0-L000548](../../tests/test_hosted_smoke.py#L548) | 548 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_all_claims_supported\"},"` | — |
| [SRC-1A176AD4F0-L000549](../../tests/test_hosted_smoke.py#L549) | 549 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1A176AD4F0-L000550](../../tests/test_hosted_smoke.py#L550) | 550 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1A176AD4F0-L000551](../../tests/test_hosted_smoke.py#L551) | 551 | `"                },"` | — |
| [SRC-1A176AD4F0-L000552](../../tests/test_hosted_smoke.py#L552) | 552 | `"            }"` | — |
| [SRC-1A176AD4F0-L000553](../../tests/test_hosted_smoke.py#L553) | 553 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000554](../../tests/test_hosted_smoke.py#L554) | 554 | `""` | — |
| [SRC-1A176AD4F0-L000555](../../tests/test_hosted_smoke.py#L555) | 555 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", invalid_evidence)"` | — |
| [SRC-1A176AD4F0-L000556](../../tests/test_hosted_smoke.py#L556) | 556 | `"    with pytest.raises(SmokeError, match=\"evidence status\"):"` | — |
| [SRC-1A176AD4F0-L000557](../../tests/test_hosted_smoke.py#L557) | 557 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000558](../../tests/test_hosted_smoke.py#L558) | 558 | `""` | — |
| [SRC-1A176AD4F0-L000559](../../tests/test_hosted_smoke.py#L559) | 559 | `""` | — |
| [SRC-1A176AD4F0-L000560](../../tests/test_hosted_smoke.py#L560) | 560 | `""` | — |
| [SRC-1A176AD4F0-L000561](../../tests/test_hosted_smoke.py#L561) | 561 | `""` | — |
| [SRC-1A176AD4F0-L000562](../../tests/test_hosted_smoke.py#L562) | 562 | `"def test_smoke_rejects_missing_or_exceeded_server_budget_profile(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000563](../../tests/test_hosted_smoke.py#L563) | 563 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000564](../../tests/test_hosted_smoke.py#L564) | 564 | `""` | — |
| [SRC-1A176AD4F0-L000565](../../tests/test_hosted_smoke.py#L565) | 565 | `"    def unbounded_budget(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000566](../../tests/test_hosted_smoke.py#L566) | 566 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000567](../../tests/test_hosted_smoke.py#L567) | 567 | `"            status, payload = original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000568](../../tests/test_hosted_smoke.py#L568) | 568 | `"            payload[\"request_budget\"] = {"` | — |
| [SRC-1A176AD4F0-L000569](../../tests/test_hosted_smoke.py#L569) | 569 | `"                \"profile\": \"default\","` | — |
| [SRC-1A176AD4F0-L000570](../../tests/test_hosted_smoke.py#L570) | 570 | `"                \"budget_exhausted\": False,"` | — |
| [SRC-1A176AD4F0-L000571](../../tests/test_hosted_smoke.py#L571) | 571 | `"                \"deadline_exceeded\": False,"` | — |
| [SRC-1A176AD4F0-L000572](../../tests/test_hosted_smoke.py#L572) | 572 | `"                \"limits\": {\"search_queries\": 8, \"search_calls\": 32, \"model_calls\": 8, \"page_fetches\": 8, \"tool_calls\": 3},"` | — |
| [SRC-1A176AD4F0-L000573](../../tests/test_hosted_smoke.py#L573) | 573 | `"                \"counts\": {\"search_queries\": 1, \"search_calls\": 2, \"model_calls\": 2, \"page_fetches\": 1, \"tool_calls\": 0},"` | — |
| [SRC-1A176AD4F0-L000574](../../tests/test_hosted_smoke.py#L574) | 574 | `"            }"` | — |
| [SRC-1A176AD4F0-L000575](../../tests/test_hosted_smoke.py#L575) | 575 | `"            return status, payload"` | — |
| [SRC-1A176AD4F0-L000576](../../tests/test_hosted_smoke.py#L576) | 576 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000577](../../tests/test_hosted_smoke.py#L577) | 577 | `""` | — |
| [SRC-1A176AD4F0-L000578](../../tests/test_hosted_smoke.py#L578) | 578 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", unbounded_budget)"` | — |
| [SRC-1A176AD4F0-L000579](../../tests/test_hosted_smoke.py#L579) | 579 | `"    with pytest.raises(SmokeError, match=\"hosted_smoke request budget\"):"` | — |
| [SRC-1A176AD4F0-L000580](../../tests/test_hosted_smoke.py#L580) | 580 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000581](../../tests/test_hosted_smoke.py#L581) | 581 | `""` | — |
| [SRC-1A176AD4F0-L000582](../../tests/test_hosted_smoke.py#L582) | 582 | `""` | — |
| [SRC-1A176AD4F0-L000583](../../tests/test_hosted_smoke.py#L583) | 583 | `""` | — |
| [SRC-1A176AD4F0-L000584](../../tests/test_hosted_smoke.py#L584) | 584 | `"def test_smoke_rejects_pipeline_complete_without_semantic_claim_support(hosted_server, monkeypatch):"` | — |
| [SRC-1A176AD4F0-L000585](../../tests/test_hosted_smoke.py#L585) | 585 | `"    original = hosted_smoke_test.request_json"` | — |
| [SRC-1A176AD4F0-L000586](../../tests/test_hosted_smoke.py#L586) | 586 | `""` | — |
| [SRC-1A176AD4F0-L000587](../../tests/test_hosted_smoke.py#L587) | 587 | `"    def unverified_claims(url: str, **kwargs):"` | — |
| [SRC-1A176AD4F0-L000588](../../tests/test_hosted_smoke.py#L588) | 588 | `"        if urlsplit(url).path == \"/api/agent\" and kwargs.get(\"token\") == TOKEN:"` | — |
| [SRC-1A176AD4F0-L000589](../../tests/test_hosted_smoke.py#L589) | 589 | `"            return 200, {"` | — |
| [SRC-1A176AD4F0-L000590](../../tests/test_hosted_smoke.py#L590) | 590 | `"                \"answer\": \"ادعاء غير متحقق [المصدر 1]\", \"used_web_search\": True,"` | — |
| [SRC-1A176AD4F0-L000591](../../tests/test_hosted_smoke.py#L591) | 591 | `"                \"used_language_model\": True,"` | — |
| [SRC-1A176AD4F0-L000592](../../tests/test_hosted_smoke.py#L592) | 592 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1A176AD4F0-L000593](../../tests/test_hosted_smoke.py#L593) | 593 | `"                \"sources\": [{\"url\": \"https://example.com/source\"}],"` | — |
| [SRC-1A176AD4F0-L000594](../../tests/test_hosted_smoke.py#L594) | 594 | `"                \"request_budget\": {\"profile\": \"hosted_smoke\", \"timeout_seconds\": 75, \"budget_exhausted\": False, \"deadline_exceeded\": False, \"limits\": {\"search_queries\": 3, \"search_calls\": 12, \"model_calls\": 6, \"page_fetches\": 4, \"tool_calls\": 0}, \"counts\": {\"search_queries\": 2, \"search_calls\": 4, \"model_calls\": 4, \"page_fetches\": 1, \"tool_calls\": 0}},"` | — |
| [SRC-1A176AD4F0-L000595](../../tests/test_hosted_smoke.py#L595) | 595 | `"                \"search_report\": {"` | — |
| [SRC-1A176AD4F0-L000596](../../tests/test_hosted_smoke.py#L596) | 596 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1A176AD4F0-L000597](../../tests/test_hosted_smoke.py#L597) | 597 | `"                    \"semantic_claim_verification\": {\"status\": \"not_performed\"},"` | — |
| [SRC-1A176AD4F0-L000598](../../tests/test_hosted_smoke.py#L598) | 598 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1A176AD4F0-L000599](../../tests/test_hosted_smoke.py#L599) | 599 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1A176AD4F0-L000600](../../tests/test_hosted_smoke.py#L600) | 600 | `"                },"` | — |
| [SRC-1A176AD4F0-L000601](../../tests/test_hosted_smoke.py#L601) | 601 | `"            }"` | — |
| [SRC-1A176AD4F0-L000602](../../tests/test_hosted_smoke.py#L602) | 602 | `"        return original(url, **kwargs)"` | — |
| [SRC-1A176AD4F0-L000603](../../tests/test_hosted_smoke.py#L603) | 603 | `""` | — |
| [SRC-1A176AD4F0-L000604](../../tests/test_hosted_smoke.py#L604) | 604 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", unverified_claims)"` | — |
| [SRC-1A176AD4F0-L000605](../../tests/test_hosted_smoke.py#L605) | 605 | `"    with pytest.raises(SmokeError, match=\"semantic claim-support review\"):"` | — |
| [SRC-1A176AD4F0-L000606](../../tests/test_hosted_smoke.py#L606) | 606 | `"        run_smoke(hosted_server, TOKEN, allow_http=True, allow_provider_usage=True, timeout=5)"` | — |
| [SRC-1A176AD4F0-L000607](../../tests/test_hosted_smoke.py#L607) | 607 | `""` | — |
| [SRC-1A176AD4F0-L000608](../../tests/test_hosted_smoke.py#L608) | 608 | `""` | — |
| [SRC-1A176AD4F0-L000609](../../tests/test_hosted_smoke.py#L609) | 609 | `"def test_hosted_smoke_workflow_scopes_secrets_to_the_execution_step():"` | — |
| [SRC-1A176AD4F0-L000610](../../tests/test_hosted_smoke.py#L610) | 610 | `"    workflow = Path(\".github/workflows/hosted-smoke.yml\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-1A176AD4F0-L000611](../../tests/test_hosted_smoke.py#L611) | 611 | `"    job = workflow.split(\"jobs:\", 1)[1].split(\"steps:\", 1)[0]"` | — |
| [SRC-1A176AD4F0-L000612](../../tests/test_hosted_smoke.py#L612) | 612 | `"    assert \"OMARAI_ACCESS_TOKEN\" not in job"` | — |
| [SRC-1A176AD4F0-L000613](../../tests/test_hosted_smoke.py#L613) | 613 | `"    assert \"OMARAI_BASE_URL\" not in job"` | — |
| [SRC-1A176AD4F0-L000614](../../tests/test_hosted_smoke.py#L614) | 614 | `"    assert \"OMARAI_ACCESS_TOKEN:\" in workflow"` | — |
| [SRC-1A176AD4F0-L000615](../../tests/test_hosted_smoke.py#L615) | 615 | `"    assert \"OMARAI_BASE_URL:\" in workflow"` | — |
| [SRC-1A176AD4F0-L000616](../../tests/test_hosted_smoke.py#L616) | 616 | `"    preflight_step = workflow.split(\"- name: Run no-cost hosted preflight\", 1)[1].split("` | — |
| [SRC-1A176AD4F0-L000617](../../tests/test_hosted_smoke.py#L617) | 617 | `"        \"- name: Run live hosted acceptance\", 1"` | — |
| [SRC-1A176AD4F0-L000618](../../tests/test_hosted_smoke.py#L618) | 618 | `"    )[0]"` | — |
| [SRC-1A176AD4F0-L000619](../../tests/test_hosted_smoke.py#L619) | 619 | `"    live_step = workflow.split(\"- name: Run live hosted acceptance\", 1)[1].split("` | — |
| [SRC-1A176AD4F0-L000620](../../tests/test_hosted_smoke.py#L620) | 620 | `"        \"- name: Upload hosted question-and-answer transcript\", 1"` | — |
| [SRC-1A176AD4F0-L000621](../../tests/test_hosted_smoke.py#L621) | 621 | `"    )[0]"` | — |
| [SRC-1A176AD4F0-L000622](../../tests/test_hosted_smoke.py#L622) | 622 | `"    assert \"OMARAI_ACCESS_TOKEN\" not in preflight_step"` | — |
| [SRC-1A176AD4F0-L000623](../../tests/test_hosted_smoke.py#L623) | 623 | `"    assert \"OMARAI_ACCESS_TOKEN:\" in live_step"` | — |
| [SRC-1A176AD4F0-L000624](../../tests/test_hosted_smoke.py#L624) | 624 | `"    assert \"preflight-only\" in workflow"` | — |
| [SRC-1A176AD4F0-L000625](../../tests/test_hosted_smoke.py#L625) | 625 | `"    assert \"default: false\" in workflow"` | — |
| [SRC-1A176AD4F0-L000626](../../tests/test_hosted_smoke.py#L626) | 626 | `""` | — |
| [SRC-1A176AD4F0-L000627](../../tests/test_hosted_smoke.py#L627) | 627 | `""` | — |
| [SRC-1A176AD4F0-L000628](../../tests/test_hosted_smoke.py#L628) | 628 | `"def test_hosted_smoke_workflow_is_manual_and_cost_gated():"` | — |
| [SRC-1A176AD4F0-L000629](../../tests/test_hosted_smoke.py#L629) | 629 | `"    workflow = Path(\".github/workflows/hosted-smoke.yml\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-1A176AD4F0-L000630](../../tests/test_hosted_smoke.py#L630) | 630 | `"    assert \"schedule:\" not in workflow"` | — |
| [SRC-1A176AD4F0-L000631](../../tests/test_hosted_smoke.py#L631) | 631 | `"    assert \"allow_provider_usage:\" in workflow"` | — |
| [SRC-1A176AD4F0-L000632](../../tests/test_hosted_smoke.py#L632) | 632 | `"    assert \"default: false\" in workflow"` | — |
| [SRC-1A176AD4F0-L000633](../../tests/test_hosted_smoke.py#L633) | 633 | `"    assert \"--allow-provider-usage\" in workflow"` | — |
| [SRC-1A176AD4F0-L000634](../../tests/test_hosted_smoke.py#L634) | 634 | `""` | — |
| [SRC-1A176AD4F0-L000635](../../tests/test_hosted_smoke.py#L635) | 635 | `""` | — |
| [SRC-1A176AD4F0-L000636](../../tests/test_hosted_smoke.py#L636) | 636 | `"def test_hosted_smoke_budget_caps_match_server_enforced_profile():"` | — |
| [SRC-1A176AD4F0-L000637](../../tests/test_hosted_smoke.py#L637) | 637 | `"    from agents.request_budget import HOSTED_SMOKE_BUDGET_LIMITS"` | — |
| [SRC-1A176AD4F0-L000638](../../tests/test_hosted_smoke.py#L638) | 638 | `""` | — |
| [SRC-1A176AD4F0-L000639](../../tests/test_hosted_smoke.py#L639) | 639 | `"    assert hosted_smoke_test.HOSTED_SMOKE_BUDGET_MAX == HOSTED_SMOKE_BUDGET_LIMITS"` | — |
| [SRC-1A176AD4F0-L000640](../../tests/test_hosted_smoke.py#L640) | 640 | `""` | — |
| [SRC-1A176AD4F0-L000641](../../tests/test_hosted_smoke.py#L641) | 641 | `""` | — |
| [SRC-1A176AD4F0-L000642](../../tests/test_hosted_smoke.py#L642) | 642 | `"def test_hosted_smoke_requires_successful_no_cost_preflight_before_live_usage():"` | — |
| [SRC-1A176AD4F0-L000643](../../tests/test_hosted_smoke.py#L643) | 643 | `"    workflow = Path(\".github/workflows/hosted-smoke.yml\").read_text(encoding=\"utf-8\")"` | — |
| [SRC-1A176AD4F0-L000644](../../tests/test_hosted_smoke.py#L644) | 644 | `"    preflight_step = workflow.split(\"- name: Run no-cost hosted preflight\", 1)[1].split("` | — |
| [SRC-1A176AD4F0-L000645](../../tests/test_hosted_smoke.py#L645) | 645 | `"        \"- name: Run live hosted acceptance\", 1"` | — |
| [SRC-1A176AD4F0-L000646](../../tests/test_hosted_smoke.py#L646) | 646 | `"    )[0]"` | — |
| [SRC-1A176AD4F0-L000647](../../tests/test_hosted_smoke.py#L647) | 647 | `"    live_step = workflow.split(\"- name: Run live hosted acceptance\", 1)[1].split("` | — |
| [SRC-1A176AD4F0-L000648](../../tests/test_hosted_smoke.py#L648) | 648 | `"        \"- name: Upload hosted question-and-answer transcript\", 1"` | — |
| [SRC-1A176AD4F0-L000649](../../tests/test_hosted_smoke.py#L649) | 649 | `"    )[0]"` | — |
| [SRC-1A176AD4F0-L000650](../../tests/test_hosted_smoke.py#L650) | 650 | `""` | — |
| [SRC-1A176AD4F0-L000651](../../tests/test_hosted_smoke.py#L651) | 651 | `"    assert \"id: preflight\" in preflight_step"` | — |
| [SRC-1A176AD4F0-L000652](../../tests/test_hosted_smoke.py#L652) | 652 | `"    assert \"if:\" not in preflight_step"` | — |
| [SRC-1A176AD4F0-L000653](../../tests/test_hosted_smoke.py#L653) | 653 | `"    assert '--expected-sha \"$(git rev-parse HEAD)\"' in preflight_step"` | — |
| [SRC-1A176AD4F0-L000654](../../tests/test_hosted_smoke.py#L654) | 654 | `"    assert \"steps.preflight.outcome == 'success'\" in live_step"` | — |
| [SRC-1A176AD4F0-L000655](../../tests/test_hosted_smoke.py#L655) | 655 | `"    assert \"allow_provider_usage == true\" in live_step"` | — |
| [SRC-1A176AD4F0-L000656](../../tests/test_hosted_smoke.py#L656) | 656 | `"    assert \"OMARAI_ACCESS_TOKEN\" not in preflight_step"` | — |
## اختبارات

### FILE-1BB2FDD5B7 — [tests/test_hosted_smoke_transcript.py](../../tests/test_hosted_smoke_transcript.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1BB2FDD5B7-L000001](../../tests/test_hosted_smoke_transcript.py#L1) | 1 | `"\"\"\"Tests for the hosted acceptance transcript contract.\"\"\""` | — |
| [SRC-1BB2FDD5B7-L000002](../../tests/test_hosted_smoke_transcript.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-1BB2FDD5B7-L000003](../../tests/test_hosted_smoke_transcript.py#L3) | 3 | `""` | — |
| [SRC-1BB2FDD5B7-L000004](../../tests/test_hosted_smoke_transcript.py#L4) | 4 | `"from scripts import hosted_smoke_test"` | — |
| [SRC-1BB2FDD5B7-L000005](../../tests/test_hosted_smoke_transcript.py#L5) | 5 | `""` | — |
| [SRC-1BB2FDD5B7-L000006](../../tests/test_hosted_smoke_transcript.py#L6) | 6 | `""` | — |
| [SRC-1BB2FDD5B7-L000007](../../tests/test_hosted_smoke_transcript.py#L7) | 7 | `"def test_hosted_smoke_returns_exact_question_answer_and_sources(monkeypatch):"` | — |
| [SRC-1BB2FDD5B7-L000008](../../tests/test_hosted_smoke_transcript.py#L8) | 8 | `"    calls = []"` | — |
| [SRC-1BB2FDD5B7-L000009](../../tests/test_hosted_smoke_transcript.py#L9) | 9 | `""` | — |
| [SRC-1BB2FDD5B7-L000010](../../tests/test_hosted_smoke_transcript.py#L10) | 10 | `"    def fake_request_json(url, *, token=\"\", payload=None, timeout=90):"` | — |
| [SRC-1BB2FDD5B7-L000011](../../tests/test_hosted_smoke_transcript.py#L11) | 11 | `"        calls.append((url, token, payload))"` | — |
| [SRC-1BB2FDD5B7-L000012](../../tests/test_hosted_smoke_transcript.py#L12) | 12 | `"        if url.endswith(\"/api/health\"):"` | — |
| [SRC-1BB2FDD5B7-L000013](../../tests/test_hosted_smoke_transcript.py#L13) | 13 | `"            return 200, {\"ok\": True, \"build\": {\"sha\": \"a\" * 40}}"` | — |
| [SRC-1BB2FDD5B7-L000014](../../tests/test_hosted_smoke_transcript.py#L14) | 14 | `"        if url.endswith(\"/api/agent\") and not token:"` | — |
| [SRC-1BB2FDD5B7-L000015](../../tests/test_hosted_smoke_transcript.py#L15) | 15 | `"            return 401, None"` | — |
| [SRC-1BB2FDD5B7-L000016](../../tests/test_hosted_smoke_transcript.py#L16) | 16 | `"        if url.endswith(\"/api/diagnostics\"):"` | — |
| [SRC-1BB2FDD5B7-L000017](../../tests/test_hosted_smoke_transcript.py#L17) | 17 | `"            return 200, {"` | — |
| [SRC-1BB2FDD5B7-L000018](../../tests/test_hosted_smoke_transcript.py#L18) | 18 | `"                \"checks\": {"` | — |
| [SRC-1BB2FDD5B7-L000019](../../tests/test_hosted_smoke_transcript.py#L19) | 19 | `"                    \"web_search\": {"` | — |
| [SRC-1BB2FDD5B7-L000020](../../tests/test_hosted_smoke_transcript.py#L20) | 20 | `"                        \"status\": \"passed\","` | — |
| [SRC-1BB2FDD5B7-L000021](../../tests/test_hosted_smoke_transcript.py#L21) | 21 | `"                        \"result_count\": 2,"` | — |
| [SRC-1BB2FDD5B7-L000022](../../tests/test_hosted_smoke_transcript.py#L22) | 22 | `"                        \"provider_counts\": {\"bing_rss\": 2},"` | — |
| [SRC-1BB2FDD5B7-L000023](../../tests/test_hosted_smoke_transcript.py#L23) | 23 | `"                    },"` | — |
| [SRC-1BB2FDD5B7-L000024](../../tests/test_hosted_smoke_transcript.py#L24) | 24 | `"                    \"language_model\": {\"status\": \"passed\"},"` | — |
| [SRC-1BB2FDD5B7-L000025](../../tests/test_hosted_smoke_transcript.py#L25) | 25 | `"                },"` | — |
| [SRC-1BB2FDD5B7-L000026](../../tests/test_hosted_smoke_transcript.py#L26) | 26 | `"                \"provider_diagnostics\": ["` | — |
| [SRC-1BB2FDD5B7-L000027](../../tests/test_hosted_smoke_transcript.py#L27) | 27 | `"                    {\"provider\": \"bing_rss\", \"status\": \"ok\", \"accepted_count\": 2}"` | — |
| [SRC-1BB2FDD5B7-L000028](../../tests/test_hosted_smoke_transcript.py#L28) | 28 | `"                ],"` | — |
| [SRC-1BB2FDD5B7-L000029](../../tests/test_hosted_smoke_transcript.py#L29) | 29 | `"                \"configuration\": {"` | — |
| [SRC-1BB2FDD5B7-L000030](../../tests/test_hosted_smoke_transcript.py#L30) | 30 | `"                    \"brave_search_api_configured\": False,"` | — |
| [SRC-1BB2FDD5B7-L000031](../../tests/test_hosted_smoke_transcript.py#L31) | 31 | `"                    \"tavily_search_api_configured\": False,"` | — |
| [SRC-1BB2FDD5B7-L000032](../../tests/test_hosted_smoke_transcript.py#L32) | 32 | `"                    \"deepseek_search_api_configured\": False,"` | — |
| [SRC-1BB2FDD5B7-L000033](../../tests/test_hosted_smoke_transcript.py#L33) | 33 | `"                },"` | — |
| [SRC-1BB2FDD5B7-L000034](../../tests/test_hosted_smoke_transcript.py#L34) | 34 | `"                \"warnings\": [],"` | — |
| [SRC-1BB2FDD5B7-L000035](../../tests/test_hosted_smoke_transcript.py#L35) | 35 | `"            }"` | — |
| [SRC-1BB2FDD5B7-L000036](../../tests/test_hosted_smoke_transcript.py#L36) | 36 | `"        if url.endswith(\"/api/agent\") and token:"` | — |
| [SRC-1BB2FDD5B7-L000037](../../tests/test_hosted_smoke_transcript.py#L37) | 37 | `"            return 200, {"` | — |
| [SRC-1BB2FDD5B7-L000038](../../tests/test_hosted_smoke_transcript.py#L38) | 38 | `"                \"answer\": \"وجدت إشارة منشورة تطلب عرض سعر لنظام إنذار الحريق.\","` | — |
| [SRC-1BB2FDD5B7-L000039](../../tests/test_hosted_smoke_transcript.py#L39) | 39 | `"                \"used_web_search\": True,"` | — |
| [SRC-1BB2FDD5B7-L000040](../../tests/test_hosted_smoke_transcript.py#L40) | 40 | `"                \"used_language_model\": True,"` | — |
| [SRC-1BB2FDD5B7-L000041](../../tests/test_hosted_smoke_transcript.py#L41) | 41 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1BB2FDD5B7-L000042](../../tests/test_hosted_smoke_transcript.py#L42) | 42 | `"                \"sources\": ["` | — |
| [SRC-1BB2FDD5B7-L000043](../../tests/test_hosted_smoke_transcript.py#L43) | 43 | `"                    {"` | — |
| [SRC-1BB2FDD5B7-L000044](../../tests/test_hosted_smoke_transcript.py#L44) | 44 | `"                        \"title\": \"Fire alarm tender notice\","` | — |
| [SRC-1BB2FDD5B7-L000045](../../tests/test_hosted_smoke_transcript.py#L45) | 45 | `"                        \"url\": \"https://example.test/fire-alarm-tender\","` | — |
| [SRC-1BB2FDD5B7-L000046](../../tests/test_hosted_smoke_transcript.py#L46) | 46 | `"                        \"provider\": \"bing_rss\","` | — |
| [SRC-1BB2FDD5B7-L000047](../../tests/test_hosted_smoke_transcript.py#L47) | 47 | `"                        \"snippet\": \"طلب عرض سعر لنظام إنذار الحريق.\","` | — |
| [SRC-1BB2FDD5B7-L000048](../../tests/test_hosted_smoke_transcript.py#L48) | 48 | `"                        \"published_at\": \"\","` | — |
| [SRC-1BB2FDD5B7-L000049](../../tests/test_hosted_smoke_transcript.py#L49) | 49 | `"                    }"` | — |
| [SRC-1BB2FDD5B7-L000050](../../tests/test_hosted_smoke_transcript.py#L50) | 50 | `"                ],"` | — |
| [SRC-1BB2FDD5B7-L000051](../../tests/test_hosted_smoke_transcript.py#L51) | 51 | `"                \"request_budget\": {\"profile\": \"hosted_smoke\", \"timeout_seconds\": 75, \"budget_exhausted\": False, \"deadline_exceeded\": False, \"limits\": {\"search_queries\": 3, \"search_calls\": 12, \"model_calls\": 6, \"page_fetches\": 4, \"tool_calls\": 0}, \"counts\": {\"search_queries\": 2, \"search_calls\": 4, \"model_calls\": 4, \"page_fetches\": 1, \"tool_calls\": 0}},"` | — |
| [SRC-1BB2FDD5B7-L000052](../../tests/test_hosted_smoke_transcript.py#L52) | 52 | `"                \"search_report\": {"` | — |
| [SRC-1BB2FDD5B7-L000053](../../tests/test_hosted_smoke_transcript.py#L53) | 53 | `"                    \"pages_fetched\": 1,"` | — |
| [SRC-1BB2FDD5B7-L000054](../../tests/test_hosted_smoke_transcript.py#L54) | 54 | `"                    \"providers_used\": [\"bing_rss\"],"` | — |
| [SRC-1BB2FDD5B7-L000055](../../tests/test_hosted_smoke_transcript.py#L55) | 55 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1BB2FDD5B7-L000056](../../tests/test_hosted_smoke_transcript.py#L56) | 56 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_all_claims_supported\"},"` | — |
| [SRC-1BB2FDD5B7-L000057](../../tests/test_hosted_smoke_transcript.py#L57) | 57 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1BB2FDD5B7-L000058](../../tests/test_hosted_smoke_transcript.py#L58) | 58 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1BB2FDD5B7-L000059](../../tests/test_hosted_smoke_transcript.py#L59) | 59 | `"                },"` | — |
| [SRC-1BB2FDD5B7-L000060](../../tests/test_hosted_smoke_transcript.py#L60) | 60 | `"            }"` | — |
| [SRC-1BB2FDD5B7-L000061](../../tests/test_hosted_smoke_transcript.py#L61) | 61 | `"        raise AssertionError(f\"unexpected request: {url}\")"` | — |
| [SRC-1BB2FDD5B7-L000062](../../tests/test_hosted_smoke_transcript.py#L62) | 62 | `""` | — |
| [SRC-1BB2FDD5B7-L000063](../../tests/test_hosted_smoke_transcript.py#L63) | 63 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", fake_request_json)"` | — |
| [SRC-1BB2FDD5B7-L000064](../../tests/test_hosted_smoke_transcript.py#L64) | 64 | `"    report = hosted_smoke_test.run_smoke("` | — |
| [SRC-1BB2FDD5B7-L000065](../../tests/test_hosted_smoke_transcript.py#L65) | 65 | `"        \"https://omarai.example\", \"T\" * 40, expected_sha=\"a\" * 40,"` | — |
| [SRC-1BB2FDD5B7-L000066](../../tests/test_hosted_smoke_transcript.py#L66) | 66 | `"        allow_provider_usage=True,"` | — |
| [SRC-1BB2FDD5B7-L000067](../../tests/test_hosted_smoke_transcript.py#L67) | 67 | `"    )"` | — |
