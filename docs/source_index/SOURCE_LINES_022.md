# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **022**
- سجلات الأسطر: **800**
- النطاق: SRC-3451CC474D-L000240 إلى SRC-6BCB799CEC-L000295
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-3451CC474D — [tests/test_api.py](../../tests/test_api.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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

### FILE-3D0A619359 — [tests/test_dashboard_security.py](../../tests/test_dashboard_security.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3D0A619359-L000001](../../tests/test_dashboard_security.py#L1) | 1 | `"\"\"\"Static regression checks for sensitive lead-dashboard browser behavior.\"\"\""` | — |
| [SRC-3D0A619359-L000002](../../tests/test_dashboard_security.py#L2) | 2 | `"from pathlib import Path"` | — |
| [SRC-3D0A619359-L000003](../../tests/test_dashboard_security.py#L3) | 3 | `""` | — |
| [SRC-3D0A619359-L000004](../../tests/test_dashboard_security.py#L4) | 4 | `"DASHBOARD = Path(__file__).resolve().parents[1] / \"web\" / \"dashboard.html\""` | — |
| [SRC-3D0A619359-L000005](../../tests/test_dashboard_security.py#L5) | 5 | `""` | — |
| [SRC-3D0A619359-L000006](../../tests/test_dashboard_security.py#L6) | 6 | `""` | — |
| [SRC-3D0A619359-L000007](../../tests/test_dashboard_security.py#L7) | 7 | `"def test_hosted_lead_dashboard_can_send_the_private_access_token():"` | — |
| [SRC-3D0A619359-L000008](../../tests/test_dashboard_security.py#L8) | 8 | `"    html = DASHBOARD.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000009](../../tests/test_dashboard_security.py#L9) | 9 | `"    assert 'const ACCESS_TOKEN_STORAGE_KEY=\"omarai_access_token\"' in html"` | — |
| [SRC-3D0A619359-L000010](../../tests/test_dashboard_security.py#L10) | 10 | `"    assert 'headers.Authorization=\"Bearer \"+token' in html"` | — |
| [SRC-3D0A619359-L000011](../../tests/test_dashboard_security.py#L11) | 11 | `"    assert '$(\"saveAccessToken\").onclick' in html"` | — |
| [SRC-3D0A619359-L000012](../../tests/test_dashboard_security.py#L12) | 12 | `""` | — |
| [SRC-3D0A619359-L000013](../../tests/test_dashboard_security.py#L13) | 13 | `""` | — |
| [SRC-3D0A619359-L000014](../../tests/test_dashboard_security.py#L14) | 14 | `"def test_saved_lead_source_links_reject_non_http_schemes():"` | — |
| [SRC-3D0A619359-L000015](../../tests/test_dashboard_security.py#L15) | 15 | `"    html = DASHBOARD.read_text(encoding=\"utf-8\")"` | — |
| [SRC-3D0A619359-L000016](../../tests/test_dashboard_security.py#L16) | 16 | `"    assert \"function safeSourceUrl(value)\" in html"` | — |
| [SRC-3D0A619359-L000017](../../tests/test_dashboard_security.py#L17) | 17 | `"    assert '[\"http:\",\"https:\"]' in html"` | — |
| [SRC-3D0A619359-L000018](../../tests/test_dashboard_security.py#L18) | 18 | `"    assert \"const sourceUrl=safeSourceUrl(l.source_url)\" in html"` | — |
| [SRC-3D0A619359-L000019](../../tests/test_dashboard_security.py#L19) | 19 | `"    assert \"const sourceLink=sourceUrl?\" in html"` | — |
## اختبارات

### FILE-6BCB799CEC — [tests/test_evidence_provenance.py](../../tests/test_evidence_provenance.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6BCB799CEC-L000001](../../tests/test_evidence_provenance.py#L1) | 1 | `"\"\"\"Regression tests for evidence provenance and pinned public-page retrieval.\"\"\""` | — |
| [SRC-6BCB799CEC-L000002](../../tests/test_evidence_provenance.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-6BCB799CEC-L000003](../../tests/test_evidence_provenance.py#L3) | 3 | `""` | — |
| [SRC-6BCB799CEC-L000004](../../tests/test_evidence_provenance.py#L4) | 4 | `"import socket"` | — |
| [SRC-6BCB799CEC-L000005](../../tests/test_evidence_provenance.py#L5) | 5 | `""` | — |
| [SRC-6BCB799CEC-L000006](../../tests/test_evidence_provenance.py#L6) | 6 | `"import pytest"` | — |
| [SRC-6BCB799CEC-L000007](../../tests/test_evidence_provenance.py#L7) | 7 | `""` | — |
| [SRC-6BCB799CEC-L000008](../../tests/test_evidence_provenance.py#L8) | 8 | `"from agents.web_agent import WebAgent, _public_ip_literals"` | — |
| [SRC-6BCB799CEC-L000009](../../tests/test_evidence_provenance.py#L9) | 9 | `""` | — |
| [SRC-6BCB799CEC-L000010](../../tests/test_evidence_provenance.py#L10) | 10 | `""` | — |
| [SRC-6BCB799CEC-L000011](../../tests/test_evidence_provenance.py#L11) | 11 | `"def _addrinfo(ip: str):"` | — |
| [SRC-6BCB799CEC-L000012](../../tests/test_evidence_provenance.py#L12) | 12 | `"    family = socket.AF_INET6 if \":\" in ip else socket.AF_INET"` | — |
| [SRC-6BCB799CEC-L000013](../../tests/test_evidence_provenance.py#L13) | 13 | `"    return [(family, socket.SOCK_STREAM, 6, \"\", (ip, 0))]"` | — |
| [SRC-6BCB799CEC-L000014](../../tests/test_evidence_provenance.py#L14) | 14 | `""` | — |
| [SRC-6BCB799CEC-L000015](../../tests/test_evidence_provenance.py#L15) | 15 | `""` | — |
| [SRC-6BCB799CEC-L000016](../../tests/test_evidence_provenance.py#L16) | 16 | `"def test_failed_page_read_is_not_reported_as_fetched(monkeypatch):"` | — |
| [SRC-6BCB799CEC-L000017](../../tests/test_evidence_provenance.py#L17) | 17 | `"    \"\"\"An empty extraction must not set page_fetched through the real collector.\"\"\""` | — |
| [SRC-6BCB799CEC-L000018](../../tests/test_evidence_provenance.py#L18) | 18 | `"    agent = WebAgent()"` | — |
| [SRC-6BCB799CEC-L000019](../../tests/test_evidence_provenance.py#L19) | 19 | `""` | — |
| [SRC-6BCB799CEC-L000020](../../tests/test_evidence_provenance.py#L20) | 20 | `"    def search(query):"` | — |
| [SRC-6BCB799CEC-L000021](../../tests/test_evidence_provenance.py#L21) | 21 | `"        return [{"` | — |
| [SRC-6BCB799CEC-L000022](../../tests/test_evidence_provenance.py#L22) | 22 | `"            \"title\": \"عنوان فقط\","` | — |
| [SRC-6BCB799CEC-L000023](../../tests/test_evidence_provenance.py#L23) | 23 | `"            \"url\": \"https://example.com/unread\","` | — |
| [SRC-6BCB799CEC-L000024](../../tests/test_evidence_provenance.py#L24) | 24 | `"            \"snippet\": \"مقتطف محرك بحث\","` | — |
| [SRC-6BCB799CEC-L000025](../../tests/test_evidence_provenance.py#L25) | 25 | `"            \"provider\": \"duckduckgo_html\","` | — |
| [SRC-6BCB799CEC-L000026](../../tests/test_evidence_provenance.py#L26) | 26 | `"            \"provider_rank\": 1,"` | — |
| [SRC-6BCB799CEC-L000027](../../tests/test_evidence_provenance.py#L27) | 27 | `"            \"search_query\": query,"` | — |
| [SRC-6BCB799CEC-L000028](../../tests/test_evidence_provenance.py#L28) | 28 | `"            \"published_at\": \"\","` | — |
| [SRC-6BCB799CEC-L000029](../../tests/test_evidence_provenance.py#L29) | 29 | `"        }]"` | — |
| [SRC-6BCB799CEC-L000030](../../tests/test_evidence_provenance.py#L30) | 30 | `""` | — |
| [SRC-6BCB799CEC-L000031](../../tests/test_evidence_provenance.py#L31) | 31 | `"    monkeypatch.setattr(agent, \"_search_web\", search)"` | — |
| [SRC-6BCB799CEC-L000032](../../tests/test_evidence_provenance.py#L32) | 32 | `"    monkeypatch.setattr(agent, \"_search_news\", lambda query: [])"` | — |
| [SRC-6BCB799CEC-L000033](../../tests/test_evidence_provenance.py#L33) | 33 | `"    monkeypatch.setattr(agent, \"_search_social\", lambda query, platforms: ([], []))"` | — |
| [SRC-6BCB799CEC-L000034](../../tests/test_evidence_provenance.py#L34) | 34 | `"    monkeypatch.setattr(agent, \"_fetch_page\", lambda url: (\"\", \"\"))"` | — |
| [SRC-6BCB799CEC-L000035](../../tests/test_evidence_provenance.py#L35) | 35 | `""` | — |
| [SRC-6BCB799CEC-L000036](../../tests/test_evidence_provenance.py#L36) | 36 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-6BCB799CEC-L000037](../../tests/test_evidence_provenance.py#L37) | 37 | `"        \"queries\": [\"سؤال دون قراءة صفحة\"],"` | — |
| [SRC-6BCB799CEC-L000038](../../tests/test_evidence_provenance.py#L38) | 38 | `"        \"direct_urls\": [],"` | — |
| [SRC-6BCB799CEC-L000039](../../tests/test_evidence_provenance.py#L39) | 39 | `"        \"social_focus\": False,"` | — |
| [SRC-6BCB799CEC-L000040](../../tests/test_evidence_provenance.py#L40) | 40 | `"        \"freshness\": \"any\","` | — |
| [SRC-6BCB799CEC-L000041](../../tests/test_evidence_provenance.py#L41) | 41 | `"        \"depth\": \"standard\","` | — |
| [SRC-6BCB799CEC-L000042](../../tests/test_evidence_provenance.py#L42) | 42 | `"        \"platforms\": [],"` | — |
| [SRC-6BCB799CEC-L000043](../../tests/test_evidence_provenance.py#L43) | 43 | `"        \"planning_method\": \"test\","` | — |
| [SRC-6BCB799CEC-L000044](../../tests/test_evidence_provenance.py#L44) | 44 | `"    })"` | — |
| [SRC-6BCB799CEC-L000045](../../tests/test_evidence_provenance.py#L45) | 45 | `""` | — |
| [SRC-6BCB799CEC-L000046](../../tests/test_evidence_provenance.py#L46) | 46 | `"    assert any(\"لم يمكن استخراج نص\" in warning for warning in warnings)"` | — |
| [SRC-6BCB799CEC-L000047](../../tests/test_evidence_provenance.py#L47) | 47 | `"    assert len(sources) == 1"` | — |
| [SRC-6BCB799CEC-L000048](../../tests/test_evidence_provenance.py#L48) | 48 | `"    assert sources[0][\"url\"] == \"https://example.com/unread\""` | — |
| [SRC-6BCB799CEC-L000049](../../tests/test_evidence_provenance.py#L49) | 49 | `"    assert sources[0].get(\"page_fetched\") is not True"` | — |
| [SRC-6BCB799CEC-L000050](../../tests/test_evidence_provenance.py#L50) | 50 | `"    assert report[\"pages_fetched\"] == 0"` | — |
| [SRC-6BCB799CEC-L000051](../../tests/test_evidence_provenance.py#L51) | 51 | `"    assert report[\"queries_attempted\"] == 1"` | — |
| [SRC-6BCB799CEC-L000052](../../tests/test_evidence_provenance.py#L52) | 52 | `"    assert report[\"unique_sources\"] == 1"` | — |
| [SRC-6BCB799CEC-L000053](../../tests/test_evidence_provenance.py#L53) | 53 | `""` | — |
| [SRC-6BCB799CEC-L000054](../../tests/test_evidence_provenance.py#L54) | 54 | `""` | — |
| [SRC-6BCB799CEC-L000055](../../tests/test_evidence_provenance.py#L55) | 55 | `"def test_openrouter_citations_stay_unread_in_public_answer(monkeypatch):"` | — |
| [SRC-6BCB799CEC-L000056](../../tests/test_evidence_provenance.py#L56) | 56 | `"    \"\"\"Server-side citations must not be misreported as direct source-page reads.\"\"\""` | — |
| [SRC-6BCB799CEC-L000057](../../tests/test_evidence_provenance.py#L57) | 57 | `"    agent = WebAgent()"` | — |
| [SRC-6BCB799CEC-L000058](../../tests/test_evidence_provenance.py#L58) | 58 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-6BCB799CEC-L000059](../../tests/test_evidence_provenance.py#L59) | 59 | `"    question = \"ما آخر المعلومات؟\""` | — |
| [SRC-6BCB799CEC-L000060](../../tests/test_evidence_provenance.py#L60) | 60 | `""` | — |
| [SRC-6BCB799CEC-L000061](../../tests/test_evidence_provenance.py#L61) | 61 | `"    def collect(plan):"` | — |
| [SRC-6BCB799CEC-L000062](../../tests/test_evidence_provenance.py#L62) | 62 | `"        sources = ["` | — |
| [SRC-6BCB799CEC-L000063](../../tests/test_evidence_provenance.py#L63) | 63 | `"            {"` | — |
| [SRC-6BCB799CEC-L000064](../../tests/test_evidence_provenance.py#L64) | 64 | `"                \"title\": \"آخر المعلومات عن التقنية\","` | — |
| [SRC-6BCB799CEC-L000065](../../tests/test_evidence_provenance.py#L65) | 65 | `"                \"url\": \"https://alpha.example.com/report\","` | — |
| [SRC-6BCB799CEC-L000066](../../tests/test_evidence_provenance.py#L66) | 66 | `"                \"snippet\": \"معلومات حديثة عن الموضوع\","` | — |
| [SRC-6BCB799CEC-L000067](../../tests/test_evidence_provenance.py#L67) | 67 | `"                \"page_text\": \"\","` | — |
| [SRC-6BCB799CEC-L000068](../../tests/test_evidence_provenance.py#L68) | 68 | `"                \"page_fetched\": False,"` | — |
| [SRC-6BCB799CEC-L000069](../../tests/test_evidence_provenance.py#L69) | 69 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-6BCB799CEC-L000070](../../tests/test_evidence_provenance.py#L70) | 70 | `"                \"providers\": [\"bing_rss\"],"` | — |
| [SRC-6BCB799CEC-L000071](../../tests/test_evidence_provenance.py#L71) | 71 | `"                \"queries\": [question],"` | — |
| [SRC-6BCB799CEC-L000072](../../tests/test_evidence_provenance.py#L72) | 72 | `"                \"domain\": \"alpha.example.com\","` | — |
| [SRC-6BCB799CEC-L000073](../../tests/test_evidence_provenance.py#L73) | 73 | `"                \"source_class\": \"general\","` | — |
| [SRC-6BCB799CEC-L000074](../../tests/test_evidence_provenance.py#L74) | 74 | `"                \"platform\": \"web\","` | — |
| [SRC-6BCB799CEC-L000075](../../tests/test_evidence_provenance.py#L75) | 75 | `"                \"published_at\": \"\","` | — |
| [SRC-6BCB799CEC-L000076](../../tests/test_evidence_provenance.py#L76) | 76 | `"                \"rank_score\": 0.8,"` | — |
| [SRC-6BCB799CEC-L000077](../../tests/test_evidence_provenance.py#L77) | 77 | `"            },"` | — |
| [SRC-6BCB799CEC-L000078](../../tests/test_evidence_provenance.py#L78) | 78 | `"            {"` | — |
| [SRC-6BCB799CEC-L000079](../../tests/test_evidence_provenance.py#L79) | 79 | `"                \"title\": \"آخر المعلومات من مصدر مستقل\","` | — |
| [SRC-6BCB799CEC-L000080](../../tests/test_evidence_provenance.py#L80) | 80 | `"                \"url\": \"https://beta.example.org/report\","` | — |
| [SRC-6BCB799CEC-L000081](../../tests/test_evidence_provenance.py#L81) | 81 | `"                \"snippet\": \"معلومات موثقة عن الموضوع\","` | — |
| [SRC-6BCB799CEC-L000082](../../tests/test_evidence_provenance.py#L82) | 82 | `"                \"page_text\": \"\","` | — |
| [SRC-6BCB799CEC-L000083](../../tests/test_evidence_provenance.py#L83) | 83 | `"                \"page_fetched\": False,"` | — |
| [SRC-6BCB799CEC-L000084](../../tests/test_evidence_provenance.py#L84) | 84 | `"                \"provider\": \"duckduckgo_html\","` | — |
| [SRC-6BCB799CEC-L000085](../../tests/test_evidence_provenance.py#L85) | 85 | `"                \"providers\": [\"duckduckgo_html\"],"` | — |
| [SRC-6BCB799CEC-L000086](../../tests/test_evidence_provenance.py#L86) | 86 | `"                \"queries\": [question],"` | — |
| [SRC-6BCB799CEC-L000087](../../tests/test_evidence_provenance.py#L87) | 87 | `"                \"domain\": \"beta.example.org\","` | — |
| [SRC-6BCB799CEC-L000088](../../tests/test_evidence_provenance.py#L88) | 88 | `"                \"source_class\": \"general\","` | — |
| [SRC-6BCB799CEC-L000089](../../tests/test_evidence_provenance.py#L89) | 89 | `"                \"platform\": \"web\","` | — |
| [SRC-6BCB799CEC-L000090](../../tests/test_evidence_provenance.py#L90) | 90 | `"                \"published_at\": \"\","` | — |
| [SRC-6BCB799CEC-L000091](../../tests/test_evidence_provenance.py#L91) | 91 | `"                \"rank_score\": 0.7,"` | — |
| [SRC-6BCB799CEC-L000092](../../tests/test_evidence_provenance.py#L92) | 92 | `"            },"` | — |
| [SRC-6BCB799CEC-L000093](../../tests/test_evidence_provenance.py#L93) | 93 | `"        ]"` | — |
| [SRC-6BCB799CEC-L000094](../../tests/test_evidence_provenance.py#L94) | 94 | `"        return sources, [], {"` | — |
| [SRC-6BCB799CEC-L000095](../../tests/test_evidence_provenance.py#L95) | 95 | `"            \"queries_planned\": 1,"` | — |
| [SRC-6BCB799CEC-L000096](../../tests/test_evidence_provenance.py#L96) | 96 | `"            \"queries_attempted\": 1,"` | — |
| [SRC-6BCB799CEC-L000097](../../tests/test_evidence_provenance.py#L97) | 97 | `"            \"query_results\": [{\"query\": question, \"results\": 2}],"` | — |
| [SRC-6BCB799CEC-L000098](../../tests/test_evidence_provenance.py#L98) | 98 | `"            \"unique_sources\": 2,"` | — |
| [SRC-6BCB799CEC-L000099](../../tests/test_evidence_provenance.py#L99) | 99 | `"            \"pages_fetched\": 0,"` | — |
| [SRC-6BCB799CEC-L000100](../../tests/test_evidence_provenance.py#L100) | 100 | `"            \"providers_used\": [\"bing_rss\", \"duckduckgo_html\"],"` | — |
| [SRC-6BCB799CEC-L000101](../../tests/test_evidence_provenance.py#L101) | 101 | `"            \"provider_counts\": {\"bing_rss\": 1, \"duckduckgo_html\": 1},"` | — |
| [SRC-6BCB799CEC-L000102](../../tests/test_evidence_provenance.py#L102) | 102 | `"            \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-6BCB799CEC-L000103](../../tests/test_evidence_provenance.py#L103) | 103 | `"            \"social_direct_results\": 0,"` | — |
| [SRC-6BCB799CEC-L000104](../../tests/test_evidence_provenance.py#L104) | 104 | `"            \"expansion_queries\": [],"` | — |
| [SRC-6BCB799CEC-L000105](../../tests/test_evidence_provenance.py#L105) | 105 | `"            \"evidence_signals\": {},"` | — |
| [SRC-6BCB799CEC-L000106](../../tests/test_evidence_provenance.py#L106) | 106 | `"            \"depth\": \"standard\","` | — |
| [SRC-6BCB799CEC-L000107](../../tests/test_evidence_provenance.py#L107) | 107 | `"            \"planning_method\": \"test\","` | — |
| [SRC-6BCB799CEC-L000108](../../tests/test_evidence_provenance.py#L108) | 108 | `"        }"` | — |
| [SRC-6BCB799CEC-L000109](../../tests/test_evidence_provenance.py#L109) | 109 | `""` | — |
| [SRC-6BCB799CEC-L000110](../../tests/test_evidence_provenance.py#L110) | 110 | `"    def generate(*args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000111](../../tests/test_evidence_provenance.py#L111) | 111 | `"        agent.server_search_sources.append({"` | — |
| [SRC-6BCB799CEC-L000112](../../tests/test_evidence_provenance.py#L112) | 112 | `"            \"title\": \"آخر المعلومات - نتيجة بحث مباشر\","` | — |
| [SRC-6BCB799CEC-L000113](../../tests/test_evidence_provenance.py#L113) | 113 | `"            \"url\": \"https://research.example.net/live-result\","` | — |
| [SRC-6BCB799CEC-L000114](../../tests/test_evidence_provenance.py#L114) | 114 | `"            \"snippet\": \"معلومات حديثة إضافية عن الموضوع\","` | — |
| [SRC-6BCB799CEC-L000115](../../tests/test_evidence_provenance.py#L115) | 115 | `"            \"page_text\": \"مقتطف أعاده مزود البحث\","` | — |
| [SRC-6BCB799CEC-L000116](../../tests/test_evidence_provenance.py#L116) | 116 | `"            \"page_fetched\": False,"` | — |
| [SRC-6BCB799CEC-L000117](../../tests/test_evidence_provenance.py#L117) | 117 | `"            \"provider\": \"openrouter_web_search\","` | — |
| [SRC-6BCB799CEC-L000118](../../tests/test_evidence_provenance.py#L118) | 118 | `"            \"providers\": [\"openrouter_web_search\"],"` | — |
| [SRC-6BCB799CEC-L000119](../../tests/test_evidence_provenance.py#L119) | 119 | `"            \"queries\": [question],"` | — |
| [SRC-6BCB799CEC-L000120](../../tests/test_evidence_provenance.py#L120) | 120 | `"            \"domain\": \"research.example.net\","` | — |
| [SRC-6BCB799CEC-L000121](../../tests/test_evidence_provenance.py#L121) | 121 | `"            \"source_class\": \"general\","` | — |
| [SRC-6BCB799CEC-L000122](../../tests/test_evidence_provenance.py#L122) | 122 | `"            \"platform\": \"web\","` | — |
| [SRC-6BCB799CEC-L000123](../../tests/test_evidence_provenance.py#L123) | 123 | `"            \"published_at\": \"\","` | — |
| [SRC-6BCB799CEC-L000124](../../tests/test_evidence_provenance.py#L124) | 124 | `"            \"rank_score\": 0.0,"` | — |
| [SRC-6BCB799CEC-L000125](../../tests/test_evidence_provenance.py#L125) | 125 | `"        })"` | — |
| [SRC-6BCB799CEC-L000126](../../tests/test_evidence_provenance.py#L126) | 126 | `"        return \"الخلاصة من المصدرين [المصدر 1] [المصدر 2].\""` | — |
| [SRC-6BCB799CEC-L000127](../../tests/test_evidence_provenance.py#L127) | 127 | `""` | — |
| [SRC-6BCB799CEC-L000128](../../tests/test_evidence_provenance.py#L128) | 128 | `"    monkeypatch.setattr(agent, \"_plan_search\", lambda question, history: {"` | — |
| [SRC-6BCB799CEC-L000129](../../tests/test_evidence_provenance.py#L129) | 129 | `"        \"queries\": [question],"` | — |
| [SRC-6BCB799CEC-L000130](../../tests/test_evidence_provenance.py#L130) | 130 | `"        \"direct_urls\": [],"` | — |
| [SRC-6BCB799CEC-L000131](../../tests/test_evidence_provenance.py#L131) | 131 | `"        \"social_focus\": False,"` | — |
| [SRC-6BCB799CEC-L000132](../../tests/test_evidence_provenance.py#L132) | 132 | `"        \"freshness\": \"any\","` | — |
| [SRC-6BCB799CEC-L000133](../../tests/test_evidence_provenance.py#L133) | 133 | `"        \"depth\": \"standard\","` | — |
| [SRC-6BCB799CEC-L000134](../../tests/test_evidence_provenance.py#L134) | 134 | `"        \"platforms\": [],"` | — |
| [SRC-6BCB799CEC-L000135](../../tests/test_evidence_provenance.py#L135) | 135 | `"        \"planning_method\": \"test\","` | — |
| [SRC-6BCB799CEC-L000136](../../tests/test_evidence_provenance.py#L136) | 136 | `"    })"` | — |
| [SRC-6BCB799CEC-L000137](../../tests/test_evidence_provenance.py#L137) | 137 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect)"` | — |
| [SRC-6BCB799CEC-L000138](../../tests/test_evidence_provenance.py#L138) | 138 | `"    monkeypatch.setattr(agent, \"_generate\", generate)"` | — |
| [SRC-6BCB799CEC-L000139](../../tests/test_evidence_provenance.py#L139) | 139 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-6BCB799CEC-L000140](../../tests/test_evidence_provenance.py#L140) | 140 | `""` | — |
| [SRC-6BCB799CEC-L000141](../../tests/test_evidence_provenance.py#L141) | 141 | `"    result = agent.answer(question, history=[], mode=\"auto\")"` | — |
| [SRC-6BCB799CEC-L000142](../../tests/test_evidence_provenance.py#L142) | 142 | `"    cited = next(source for source in result[\"sources\"] if source[\"url\"] == \"https://research.example.net/live-result\")"` | — |
| [SRC-6BCB799CEC-L000143](../../tests/test_evidence_provenance.py#L143) | 143 | `"    assert cited[\"page_fetched\"] is False"` | — |
| [SRC-6BCB799CEC-L000144](../../tests/test_evidence_provenance.py#L144) | 144 | `"    assert \"openrouter_web_search\" in cited[\"providers\"]"` | — |
| [SRC-6BCB799CEC-L000145](../../tests/test_evidence_provenance.py#L145) | 145 | `"    assert result[\"search_report\"][\"pages_fetched\"] == 0"` | — |
| [SRC-6BCB799CEC-L000146](../../tests/test_evidence_provenance.py#L146) | 146 | `"    assert result[\"search_report\"][\"openrouter_web_search_results\"] == 1"` | — |
| [SRC-6BCB799CEC-L000147](../../tests/test_evidence_provenance.py#L147) | 147 | `""` | — |
| [SRC-6BCB799CEC-L000148](../../tests/test_evidence_provenance.py#L148) | 148 | `"def test_private_resolution_blocks_page_fetch(monkeypatch):"` | — |
| [SRC-6BCB799CEC-L000149](../../tests/test_evidence_provenance.py#L149) | 149 | `"    called = {\"stream\": 0}"` | — |
| [SRC-6BCB799CEC-L000150](../../tests/test_evidence_provenance.py#L150) | 150 | `""` | — |
| [SRC-6BCB799CEC-L000151](../../tests/test_evidence_provenance.py#L151) | 151 | `"    def fake_getaddrinfo(host, port, *args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000152](../../tests/test_evidence_provenance.py#L152) | 152 | `"        return _addrinfo(\"127.0.0.1\")"` | — |
| [SRC-6BCB799CEC-L000153](../../tests/test_evidence_provenance.py#L153) | 153 | `""` | — |
| [SRC-6BCB799CEC-L000154](../../tests/test_evidence_provenance.py#L154) | 154 | `"    class FakeClient:"` | — |
| [SRC-6BCB799CEC-L000155](../../tests/test_evidence_provenance.py#L155) | 155 | `"        def __init__(self, *args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000156](../../tests/test_evidence_provenance.py#L156) | 156 | `"            pass"` | — |
| [SRC-6BCB799CEC-L000157](../../tests/test_evidence_provenance.py#L157) | 157 | `""` | — |
| [SRC-6BCB799CEC-L000158](../../tests/test_evidence_provenance.py#L158) | 158 | `"        def __enter__(self):"` | — |
| [SRC-6BCB799CEC-L000159](../../tests/test_evidence_provenance.py#L159) | 159 | `"            return self"` | — |
| [SRC-6BCB799CEC-L000160](../../tests/test_evidence_provenance.py#L160) | 160 | `""` | — |
| [SRC-6BCB799CEC-L000161](../../tests/test_evidence_provenance.py#L161) | 161 | `"        def __exit__(self, *args):"` | — |
| [SRC-6BCB799CEC-L000162](../../tests/test_evidence_provenance.py#L162) | 162 | `"            return False"` | — |
| [SRC-6BCB799CEC-L000163](../../tests/test_evidence_provenance.py#L163) | 163 | `""` | — |
| [SRC-6BCB799CEC-L000164](../../tests/test_evidence_provenance.py#L164) | 164 | `"        def stream(self, *args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000165](../../tests/test_evidence_provenance.py#L165) | 165 | `"            called[\"stream\"] += 1"` | — |
| [SRC-6BCB799CEC-L000166](../../tests/test_evidence_provenance.py#L166) | 166 | `"            raise AssertionError(\"private destinations must not be connected\")"` | — |
| [SRC-6BCB799CEC-L000167](../../tests/test_evidence_provenance.py#L167) | 167 | `""` | — |
| [SRC-6BCB799CEC-L000168](../../tests/test_evidence_provenance.py#L168) | 168 | `"    monkeypatch.setattr(socket, \"getaddrinfo\", fake_getaddrinfo)"` | — |
| [SRC-6BCB799CEC-L000169](../../tests/test_evidence_provenance.py#L169) | 169 | `"    monkeypatch.setattr(\"httpx.Client\", FakeClient)"` | — |
| [SRC-6BCB799CEC-L000170](../../tests/test_evidence_provenance.py#L170) | 170 | `"    assert _public_ip_literals(\"example.com\") is None"` | — |
| [SRC-6BCB799CEC-L000171](../../tests/test_evidence_provenance.py#L171) | 171 | `"    assert WebAgent()._fetch_page(\"https://example.com/secret\") == (\"\", \"\")"` | — |
| [SRC-6BCB799CEC-L000172](../../tests/test_evidence_provenance.py#L172) | 172 | `"    assert called[\"stream\"] == 0"` | — |
| [SRC-6BCB799CEC-L000173](../../tests/test_evidence_provenance.py#L173) | 173 | `""` | — |
| [SRC-6BCB799CEC-L000174](../../tests/test_evidence_provenance.py#L174) | 174 | `""` | — |
| [SRC-6BCB799CEC-L000175](../../tests/test_evidence_provenance.py#L175) | 175 | `"def test_page_fetch_connects_to_the_validated_public_ip(monkeypatch):"` | — |
| [SRC-6BCB799CEC-L000176](../../tests/test_evidence_provenance.py#L176) | 176 | `"    seen = {}"` | — |
| [SRC-6BCB799CEC-L000177](../../tests/test_evidence_provenance.py#L177) | 177 | `""` | — |
| [SRC-6BCB799CEC-L000178](../../tests/test_evidence_provenance.py#L178) | 178 | `"    def fake_getaddrinfo(host, port, *args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000179](../../tests/test_evidence_provenance.py#L179) | 179 | `"        assert host == \"example.com\""` | — |
| [SRC-6BCB799CEC-L000180](../../tests/test_evidence_provenance.py#L180) | 180 | `"        return _addrinfo(\"1.1.1.1\")"` | — |
| [SRC-6BCB799CEC-L000181](../../tests/test_evidence_provenance.py#L181) | 181 | `""` | — |
| [SRC-6BCB799CEC-L000182](../../tests/test_evidence_provenance.py#L182) | 182 | `"    class FakeResponse:"` | — |
| [SRC-6BCB799CEC-L000183](../../tests/test_evidence_provenance.py#L183) | 183 | `"        status_code = 200"` | — |
| [SRC-6BCB799CEC-L000184](../../tests/test_evidence_provenance.py#L184) | 184 | `"        encoding = \"utf-8\""` | — |
| [SRC-6BCB799CEC-L000185](../../tests/test_evidence_provenance.py#L185) | 185 | `""` | — |
| [SRC-6BCB799CEC-L000186](../../tests/test_evidence_provenance.py#L186) | 186 | `"        def __init__(self):"` | — |
| [SRC-6BCB799CEC-L000187](../../tests/test_evidence_provenance.py#L187) | 187 | `"            self.headers = {\"content-type\": \"text/plain; charset=utf-8\"}"` | — |
| [SRC-6BCB799CEC-L000188](../../tests/test_evidence_provenance.py#L188) | 188 | `""` | — |
| [SRC-6BCB799CEC-L000189](../../tests/test_evidence_provenance.py#L189) | 189 | `"        def iter_bytes(self):"` | — |
| [SRC-6BCB799CEC-L000190](../../tests/test_evidence_provenance.py#L190) | 190 | `"            yield \"نص عام\".encode()"` | — |
| [SRC-6BCB799CEC-L000191](../../tests/test_evidence_provenance.py#L191) | 191 | `""` | — |
| [SRC-6BCB799CEC-L000192](../../tests/test_evidence_provenance.py#L192) | 192 | `"        def __enter__(self):"` | — |
| [SRC-6BCB799CEC-L000193](../../tests/test_evidence_provenance.py#L193) | 193 | `"            return self"` | — |
| [SRC-6BCB799CEC-L000194](../../tests/test_evidence_provenance.py#L194) | 194 | `""` | — |
| [SRC-6BCB799CEC-L000195](../../tests/test_evidence_provenance.py#L195) | 195 | `"        def __exit__(self, *args):"` | — |
| [SRC-6BCB799CEC-L000196](../../tests/test_evidence_provenance.py#L196) | 196 | `"            return False"` | — |
| [SRC-6BCB799CEC-L000197](../../tests/test_evidence_provenance.py#L197) | 197 | `""` | — |
| [SRC-6BCB799CEC-L000198](../../tests/test_evidence_provenance.py#L198) | 198 | `"    class FakeClient:"` | — |
| [SRC-6BCB799CEC-L000199](../../tests/test_evidence_provenance.py#L199) | 199 | `"        def __init__(self, *args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000200](../../tests/test_evidence_provenance.py#L200) | 200 | `"            assert kwargs.get(\"verify\") is True"` | — |
| [SRC-6BCB799CEC-L000201](../../tests/test_evidence_provenance.py#L201) | 201 | `"            assert kwargs.get(\"follow_redirects\") is False"` | — |
| [SRC-6BCB799CEC-L000202](../../tests/test_evidence_provenance.py#L202) | 202 | `"            # Do not allow HTTP_PROXY/HTTPS_PROXY to bypass the pinned IP."` | — |
| [SRC-6BCB799CEC-L000203](../../tests/test_evidence_provenance.py#L203) | 203 | `"            assert kwargs.get(\"trust_env\") is False"` | — |
| [SRC-6BCB799CEC-L000204](../../tests/test_evidence_provenance.py#L204) | 204 | `""` | — |
| [SRC-6BCB799CEC-L000205](../../tests/test_evidence_provenance.py#L205) | 205 | `"        def __enter__(self):"` | — |
| [SRC-6BCB799CEC-L000206](../../tests/test_evidence_provenance.py#L206) | 206 | `"            return self"` | — |
| [SRC-6BCB799CEC-L000207](../../tests/test_evidence_provenance.py#L207) | 207 | `""` | — |
| [SRC-6BCB799CEC-L000208](../../tests/test_evidence_provenance.py#L208) | 208 | `"        def __exit__(self, *args):"` | — |
| [SRC-6BCB799CEC-L000209](../../tests/test_evidence_provenance.py#L209) | 209 | `"            return False"` | — |
| [SRC-6BCB799CEC-L000210](../../tests/test_evidence_provenance.py#L210) | 210 | `""` | — |
| [SRC-6BCB799CEC-L000211](../../tests/test_evidence_provenance.py#L211) | 211 | `"        def stream(self, method, url, headers=None, extensions=None):"` | — |
| [SRC-6BCB799CEC-L000212](../../tests/test_evidence_provenance.py#L212) | 212 | `"            seen[\"method\"] = method"` | — |
| [SRC-6BCB799CEC-L000213](../../tests/test_evidence_provenance.py#L213) | 213 | `"            seen[\"url\"] = url"` | — |
| [SRC-6BCB799CEC-L000214](../../tests/test_evidence_provenance.py#L214) | 214 | `"            seen[\"headers\"] = headers"` | — |
| [SRC-6BCB799CEC-L000215](../../tests/test_evidence_provenance.py#L215) | 215 | `"            seen[\"extensions\"] = extensions"` | — |
| [SRC-6BCB799CEC-L000216](../../tests/test_evidence_provenance.py#L216) | 216 | `"            return FakeResponse()"` | — |
| [SRC-6BCB799CEC-L000217](../../tests/test_evidence_provenance.py#L217) | 217 | `""` | — |
| [SRC-6BCB799CEC-L000218](../../tests/test_evidence_provenance.py#L218) | 218 | `"    monkeypatch.setattr(socket, \"getaddrinfo\", fake_getaddrinfo)"` | — |
| [SRC-6BCB799CEC-L000219](../../tests/test_evidence_provenance.py#L219) | 219 | `"    monkeypatch.setattr(\"httpx.Client\", FakeClient)"` | — |
| [SRC-6BCB799CEC-L000220](../../tests/test_evidence_provenance.py#L220) | 220 | `"    title, text = WebAgent()._fetch_page(\"https://example.com/article\")"` | — |
| [SRC-6BCB799CEC-L000221](../../tests/test_evidence_provenance.py#L221) | 221 | `"    assert title == \"\""` | — |
| [SRC-6BCB799CEC-L000222](../../tests/test_evidence_provenance.py#L222) | 222 | `"    assert \"نص عام\" in text"` | — |
| [SRC-6BCB799CEC-L000223](../../tests/test_evidence_provenance.py#L223) | 223 | `"    assert seen[\"url\"].startswith(\"https://1.1.1.1/\")"` | — |
| [SRC-6BCB799CEC-L000224](../../tests/test_evidence_provenance.py#L224) | 224 | `"    assert seen[\"headers\"][\"Host\"] == \"example.com\""` | — |
| [SRC-6BCB799CEC-L000225](../../tests/test_evidence_provenance.py#L225) | 225 | `"    assert seen[\"extensions\"][\"sni_hostname\"] == \"example.com\""` | — |
| [SRC-6BCB799CEC-L000226](../../tests/test_evidence_provenance.py#L226) | 226 | `""` | — |
| [SRC-6BCB799CEC-L000227](../../tests/test_evidence_provenance.py#L227) | 227 | `"def test_mixed_public_and_private_dns_answers_block_page_fetch(monkeypatch):"` | — |
| [SRC-6BCB799CEC-L000228](../../tests/test_evidence_provenance.py#L228) | 228 | `"    \"\"\"A hostname is rejected when even one DNS answer is non-global.\"\"\""` | — |
| [SRC-6BCB799CEC-L000229](../../tests/test_evidence_provenance.py#L229) | 229 | `"    def fake_getaddrinfo(host, port, *args, **kwargs):"` | — |
| [SRC-6BCB799CEC-L000230](../../tests/test_evidence_provenance.py#L230) | 230 | `"        return _addrinfo(\"1.1.1.1\") + _addrinfo(\"127.0.0.1\")"` | — |
| [SRC-6BCB799CEC-L000231](../../tests/test_evidence_provenance.py#L231) | 231 | `""` | — |
| [SRC-6BCB799CEC-L000232](../../tests/test_evidence_provenance.py#L232) | 232 | `"    monkeypatch.setattr(socket, \"getaddrinfo\", fake_getaddrinfo)"` | — |
| [SRC-6BCB799CEC-L000233](../../tests/test_evidence_provenance.py#L233) | 233 | `"    assert _public_ip_literals(\"example.com\") is None"` | — |
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
