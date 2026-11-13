# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **052**
- سجلات الأسطر: **800**
- النطاق: SRC-1A176AD4F0-L000282 إلى SRC-EA6EC52573-L000303
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-1A176AD4F0 — [tests/test_hosted_smoke.py](../../tests/test_hosted_smoke.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-1BB2FDD5B7-L000068](../../tests/test_hosted_smoke_transcript.py#L68) | 68 | `""` | — |
| [SRC-1BB2FDD5B7-L000069](../../tests/test_hosted_smoke_transcript.py#L69) | 69 | `"    transcript = report[\"transcript\"][0]"` | — |
| [SRC-1BB2FDD5B7-L000070](../../tests/test_hosted_smoke_transcript.py#L70) | 70 | `"    assert transcript[\"question\"] == hosted_smoke_test.LIVE_TEST_QUESTION"` | — |
| [SRC-1BB2FDD5B7-L000071](../../tests/test_hosted_smoke_transcript.py#L71) | 71 | `"    assert transcript[\"answer\"] == \"وجدت إشارة منشورة تطلب عرض سعر لنظام إنذار الحريق.\""` | — |
| [SRC-1BB2FDD5B7-L000072](../../tests/test_hosted_smoke_transcript.py#L72) | 72 | `"    assert transcript[\"sources\"][0][\"url\"] == \"https://example.test/fire-alarm-tender\""` | — |
| [SRC-1BB2FDD5B7-L000073](../../tests/test_hosted_smoke_transcript.py#L73) | 73 | `"    assert transcript[\"pipeline_completion_status\"] == \"completed\""` | — |
| [SRC-1BB2FDD5B7-L000074](../../tests/test_hosted_smoke_transcript.py#L74) | 74 | `"    assert transcript[\"request_budget\"][\"profile\"] == \"hosted_smoke\""` | — |
| [SRC-1BB2FDD5B7-L000075](../../tests/test_hosted_smoke_transcript.py#L75) | 75 | `"    assert report[\"checks\"][\"request_budget\"][\"limits\"][\"search_calls\"] <= 12"` | — |
| [SRC-1BB2FDD5B7-L000076](../../tests/test_hosted_smoke_transcript.py#L76) | 76 | `"    assert report[\"checks\"][\"search\"][\"providers_reported\"] == [\"bing_rss\"]"` | — |
| [SRC-1BB2FDD5B7-L000077](../../tests/test_hosted_smoke_transcript.py#L77) | 77 | `"    assert all(\"T\" * 40 not in str(item) for item in report.values())"` | — |
| [SRC-1BB2FDD5B7-L000078](../../tests/test_hosted_smoke_transcript.py#L78) | 78 | `"    assert len(calls) == 3"` | — |
| [SRC-1BB2FDD5B7-L000079](../../tests/test_hosted_smoke_transcript.py#L79) | 79 | `"    assert not any(call[0].endswith(\"/api/diagnostics\") for call in calls)"` | — |
| [SRC-1BB2FDD5B7-L000080](../../tests/test_hosted_smoke_transcript.py#L80) | 80 | `""` | — |
| [SRC-1BB2FDD5B7-L000081](../../tests/test_hosted_smoke_transcript.py#L81) | 81 | `""` | — |
| [SRC-1BB2FDD5B7-L000082](../../tests/test_hosted_smoke_transcript.py#L82) | 82 | `"def test_hosted_smoke_allows_no_token_only_for_loopback_dev(monkeypatch):"` | — |
| [SRC-1BB2FDD5B7-L000083](../../tests/test_hosted_smoke_transcript.py#L83) | 83 | `"    def fake_request_json(url, *, token=\"\", payload=None, timeout=90):"` | — |
| [SRC-1BB2FDD5B7-L000084](../../tests/test_hosted_smoke_transcript.py#L84) | 84 | `"        if url.endswith(\"/api/health\"):"` | — |
| [SRC-1BB2FDD5B7-L000085](../../tests/test_hosted_smoke_transcript.py#L85) | 85 | `"            return 200, {\"ok\": True, \"build\": {\"sha\": \"unknown\"}}"` | — |
| [SRC-1BB2FDD5B7-L000086](../../tests/test_hosted_smoke_transcript.py#L86) | 86 | `"        if url.endswith(\"/api/agent\"):"` | — |
| [SRC-1BB2FDD5B7-L000087](../../tests/test_hosted_smoke_transcript.py#L87) | 87 | `"            return 200, {"` | — |
| [SRC-1BB2FDD5B7-L000088](../../tests/test_hosted_smoke_transcript.py#L88) | 88 | `"                \"answer\": \"لا توجد إشارة شراء مؤكدة في المصادر التي تم فحصها.\","` | — |
| [SRC-1BB2FDD5B7-L000089](../../tests/test_hosted_smoke_transcript.py#L89) | 89 | `"                \"used_web_search\": True,"` | — |
| [SRC-1BB2FDD5B7-L000090](../../tests/test_hosted_smoke_transcript.py#L90) | 90 | `"                \"used_language_model\": True,"` | — |
| [SRC-1BB2FDD5B7-L000091](../../tests/test_hosted_smoke_transcript.py#L91) | 91 | `"                \"answer_evidence_status\": \"citation_indices_validated_only\","` | — |
| [SRC-1BB2FDD5B7-L000092](../../tests/test_hosted_smoke_transcript.py#L92) | 92 | `"                \"sources\": [{\"url\": \"https://example.test/egypt\"}],"` | — |
| [SRC-1BB2FDD5B7-L000093](../../tests/test_hosted_smoke_transcript.py#L93) | 93 | `"                \"request_budget\": {\"profile\": \"hosted_smoke\", \"timeout_seconds\": 75, \"budget_exhausted\": False, \"deadline_exceeded\": False, \"limits\": {\"search_queries\": 3, \"search_calls\": 12, \"model_calls\": 6, \"page_fetches\": 4, \"tool_calls\": 0}, \"counts\": {\"search_queries\": 1, \"search_calls\": 2, \"model_calls\": 3, \"page_fetches\": 1, \"tool_calls\": 0}},"` | — |
| [SRC-1BB2FDD5B7-L000094](../../tests/test_hosted_smoke_transcript.py#L94) | 94 | `"                \"search_report\": {"` | — |
| [SRC-1BB2FDD5B7-L000095](../../tests/test_hosted_smoke_transcript.py#L95) | 95 | `"                    \"pipeline_completion_status\": \"completed\","` | — |
| [SRC-1BB2FDD5B7-L000096](../../tests/test_hosted_smoke_transcript.py#L96) | 96 | `"                    \"semantic_claim_verification\": {\"status\": \"completed_no_factual_claims\"},"` | — |
| [SRC-1BB2FDD5B7-L000097](../../tests/test_hosted_smoke_transcript.py#L97) | 97 | `"                    \"insufficient_evidence\": False,"` | — |
| [SRC-1BB2FDD5B7-L000098](../../tests/test_hosted_smoke_transcript.py#L98) | 98 | `"                    \"claim_audit_semantics\": \"distinct_model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-1BB2FDD5B7-L000099](../../tests/test_hosted_smoke_transcript.py#L99) | 99 | `"                },"` | — |
| [SRC-1BB2FDD5B7-L000100](../../tests/test_hosted_smoke_transcript.py#L100) | 100 | `"            }"` | — |
| [SRC-1BB2FDD5B7-L000101](../../tests/test_hosted_smoke_transcript.py#L101) | 101 | `"        raise AssertionError(url)"` | — |
| [SRC-1BB2FDD5B7-L000102](../../tests/test_hosted_smoke_transcript.py#L102) | 102 | `""` | — |
| [SRC-1BB2FDD5B7-L000103](../../tests/test_hosted_smoke_transcript.py#L103) | 103 | `"    monkeypatch.setattr(hosted_smoke_test, \"request_json\", fake_request_json)"` | — |
| [SRC-1BB2FDD5B7-L000104](../../tests/test_hosted_smoke_transcript.py#L104) | 104 | `"    report = hosted_smoke_test.run_smoke("` | — |
| [SRC-1BB2FDD5B7-L000105](../../tests/test_hosted_smoke_transcript.py#L105) | 105 | `"        \"http://127.0.0.1:8000\","` | — |
| [SRC-1BB2FDD5B7-L000106](../../tests/test_hosted_smoke_transcript.py#L106) | 106 | `"        \"\","` | — |
| [SRC-1BB2FDD5B7-L000107](../../tests/test_hosted_smoke_transcript.py#L107) | 107 | `"        local_dev_no_token=True,"` | — |
| [SRC-1BB2FDD5B7-L000108](../../tests/test_hosted_smoke_transcript.py#L108) | 108 | `"        allow_provider_usage=True,"` | — |
| [SRC-1BB2FDD5B7-L000109](../../tests/test_hosted_smoke_transcript.py#L109) | 109 | `"    )"` | — |
| [SRC-1BB2FDD5B7-L000110](../../tests/test_hosted_smoke_transcript.py#L110) | 110 | `"    assert report[\"auth_mode\"] == \"local_loopback_dev_bypass\""` | — |
| [SRC-1BB2FDD5B7-L000111](../../tests/test_hosted_smoke_transcript.py#L111) | 111 | `"    assert report[\"transcript\"][0][\"answer\"] == \"لا توجد إشارة شراء مؤكدة في المصادر التي تم فحصها.\""` | — |
| [SRC-1BB2FDD5B7-L000112](../../tests/test_hosted_smoke_transcript.py#L112) | 112 | `""` | — |
| [SRC-1BB2FDD5B7-L000113](../../tests/test_hosted_smoke_transcript.py#L113) | 113 | `""` | — |
| [SRC-1BB2FDD5B7-L000114](../../tests/test_hosted_smoke_transcript.py#L114) | 114 | `"def test_hosted_smoke_rejects_no_token_for_remote_host():"` | — |
| [SRC-1BB2FDD5B7-L000115](../../tests/test_hosted_smoke_transcript.py#L115) | 115 | `"    import pytest"` | — |
| [SRC-1BB2FDD5B7-L000116](../../tests/test_hosted_smoke_transcript.py#L116) | 116 | `""` | — |
| [SRC-1BB2FDD5B7-L000117](../../tests/test_hosted_smoke_transcript.py#L117) | 117 | `"    with pytest.raises(hosted_smoke_test.SmokeError, match=\"localhost/loopback\"):"` | — |
| [SRC-1BB2FDD5B7-L000118](../../tests/test_hosted_smoke_transcript.py#L118) | 118 | `"        hosted_smoke_test.run_smoke("` | — |
| [SRC-1BB2FDD5B7-L000119](../../tests/test_hosted_smoke_transcript.py#L119) | 119 | `"            \"https://omarai.example\","` | — |
| [SRC-1BB2FDD5B7-L000120](../../tests/test_hosted_smoke_transcript.py#L120) | 120 | `"            \"\","` | — |
| [SRC-1BB2FDD5B7-L000121](../../tests/test_hosted_smoke_transcript.py#L121) | 121 | `"            local_dev_no_token=True,"` | — |
| [SRC-1BB2FDD5B7-L000122](../../tests/test_hosted_smoke_transcript.py#L122) | 122 | `"        )"` | — |
## اختبارات

### FILE-EA6EC52573 — [tests/test_intent_router.py](../../tests/test_intent_router.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-EA6EC52573-L000001](../../tests/test_intent_router.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-EA6EC52573-L000002](../../tests/test_intent_router.py#L2) | 2 | `""` | — |
| [SRC-EA6EC52573-L000003](../../tests/test_intent_router.py#L3) | 3 | `"import pytest"` | — |
| [SRC-EA6EC52573-L000004](../../tests/test_intent_router.py#L4) | 4 | `""` | — |
| [SRC-EA6EC52573-L000005](../../tests/test_intent_router.py#L5) | 5 | `"from agents.intent_router import resolve_followup_query, route_intent"` | — |
| [SRC-EA6EC52573-L000006](../../tests/test_intent_router.py#L6) | 6 | `""` | — |
| [SRC-EA6EC52573-L000007](../../tests/test_intent_router.py#L7) | 7 | `""` | — |
| [SRC-EA6EC52573-L000008](../../tests/test_intent_router.py#L8) | 8 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000009](../../tests/test_intent_router.py#L9) | 9 | `"    (\"question\", \"expected\"),"` | — |
| [SRC-EA6EC52573-L000010](../../tests/test_intent_router.py#L10) | 10 | `"    ["` | — |
| [SRC-EA6EC52573-L000011](../../tests/test_intent_router.py#L11) | 11 | `"        (\"ازيك؟ عامل ايه النهاردة؟\", \"LOCAL\"),"` | — |
| [SRC-EA6EC52573-L000012](../../tests/test_intent_router.py#L12) | 12 | `"        (\"Thanks, that helps.\", \"LOCAL\"),"` | — |
| [SRC-EA6EC52573-L000013](../../tests/test_intent_router.py#L13) | 13 | `"        (\"ما عاصمة مصر؟\", \"MODEL_ONLY\"),"` | — |
| [SRC-EA6EC52573-L000014](../../tests/test_intent_router.py#L14) | 14 | `"        (\"كام سعرها؟\", \"CLARIFY\"),"` | — |
| [SRC-EA6EC52573-L000015](../../tests/test_intent_router.py#L15) | 15 | `"        (\"قارنهم\", \"CLARIFY\"),"` | — |
| [SRC-EA6EC52573-L000016](../../tests/test_intent_router.py#L16) | 16 | `"        (\"ما سعر الهاتف اليوم في مصر؟\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000017](../../tests/test_intent_router.py#L17) | 17 | `"        ("` | — |
| [SRC-EA6EC52573-L000018](../../tests/test_intent_router.py#L18) | 18 | `"            \"قارن بين iPhone 17 وSamsung S26 من حيث السعر والبطارية والكاميرا\","` | — |
| [SRC-EA6EC52573-L000019](../../tests/test_intent_router.py#L19) | 19 | `"            \"WEB_DEEP\","` | — |
| [SRC-EA6EC52573-L000020](../../tests/test_intent_router.py#L20) | 20 | `"        ),"` | — |
| [SRC-EA6EC52573-L000021](../../tests/test_intent_router.py#L21) | 21 | `"    ],"` | — |
| [SRC-EA6EC52573-L000022](../../tests/test_intent_router.py#L22) | 22 | `")"` | — |
| [SRC-EA6EC52573-L000023](../../tests/test_intent_router.py#L23) | 23 | `"def test_deterministic_intent_routes(question: str, expected: str) -> None:"` | — |
| [SRC-EA6EC52573-L000024](../../tests/test_intent_router.py#L24) | 24 | `"    decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000025](../../tests/test_intent_router.py#L25) | 25 | `"    assert decision[\"route\"] == expected"` | — |
| [SRC-EA6EC52573-L000026](../../tests/test_intent_router.py#L26) | 26 | `"    assert decision[\"reason\"]"` | — |
| [SRC-EA6EC52573-L000027](../../tests/test_intent_router.py#L27) | 27 | `""` | — |
| [SRC-EA6EC52573-L000028](../../tests/test_intent_router.py#L28) | 28 | `""` | — |
| [SRC-EA6EC52573-L000029](../../tests/test_intent_router.py#L29) | 29 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000030](../../tests/test_intent_router.py#L30) | 30 | `"    (\"question\", \"expected\"),"` | — |
| [SRC-EA6EC52573-L000031](../../tests/test_intent_router.py#L31) | 31 | `"    ["` | — |
| [SRC-EA6EC52573-L000032](../../tests/test_intent_router.py#L32) | 32 | `"        (\"ابحث عن عميل يريد شراء شقة في العاصمة الإدارية بمصر\", \"LEAD_GENERATION\"),"` | — |
| [SRC-EA6EC52573-L000033](../../tests/test_intent_router.py#L33) | 33 | `"        (\"ابحث عن عميل يطلب او يريد شقة في التجمع الخامس\", \"LEAD_GENERATION\"),"` | — |
| [SRC-EA6EC52573-L000034](../../tests/test_intent_router.py#L34) | 34 | `"        (\"ابحث عن ١٠ عملاش يريدون شرا شقة في التجمع الخامس\", \"LEAD_GENERATION\"),"` | — |
| [SRC-EA6EC52573-L000035](../../tests/test_intent_router.py#L35) | 35 | `"        (\"ابحث عن شقق للبيع في العاصمة الإدارية\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000036](../../tests/test_intent_router.py#L36) | 36 | `"        (\"Find buyers looking to buy apartments in New Capital\", \"LEAD_GENERATION\"),"` | — |
| [SRC-EA6EC52573-L000037](../../tests/test_intent_router.py#L37) | 37 | `"        (\"لخص الصفحة https://example.com/article\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000038](../../tests/test_intent_router.py#L38) | 38 | `"        (\"Summarize this page https://example.com/article\", \"WEB_SIMPLE\"),"` | — |
| [SRC-EA6EC52573-L000039](../../tests/test_intent_router.py#L39) | 39 | `"        (\"لخص النص التالي: هذا نص تجريبي\", \"MODEL_ONLY\"),"` | — |
| [SRC-EA6EC52573-L000040](../../tests/test_intent_router.py#L40) | 40 | `"    ],"` | — |
| [SRC-EA6EC52573-L000041](../../tests/test_intent_router.py#L41) | 41 | `")"` | — |
| [SRC-EA6EC52573-L000042](../../tests/test_intent_router.py#L42) | 42 | `"def test_lead_generation_and_summarization_routes(question: str, expected: str) -> None:"` | — |
| [SRC-EA6EC52573-L000043](../../tests/test_intent_router.py#L43) | 43 | `"    decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000044](../../tests/test_intent_router.py#L44) | 44 | `"    assert decision[\"route\"] == expected"` | — |
| [SRC-EA6EC52573-L000045](../../tests/test_intent_router.py#L45) | 45 | `"    assert decision[\"reason\"]"` | — |
| [SRC-EA6EC52573-L000046](../../tests/test_intent_router.py#L46) | 46 | `""` | — |
| [SRC-EA6EC52573-L000047](../../tests/test_intent_router.py#L47) | 47 | `""` | — |
| [SRC-EA6EC52573-L000048](../../tests/test_intent_router.py#L48) | 48 | `"@pytest.mark.parametrize(\"mode\", [\"deep\", \"latest\", \"social\"])"` | — |
| [SRC-EA6EC52573-L000049](../../tests/test_intent_router.py#L49) | 49 | `"def test_explicit_buyer_discovery_intent_survives_selected_research_mode(mode: str) -> None:"` | — |
| [SRC-EA6EC52573-L000050](../../tests/test_intent_router.py#L50) | 50 | `"    question = \"ابحث عن عميل يريد شراء نظام إنذار حريق صناعي في مصر\""` | — |
| [SRC-EA6EC52573-L000051](../../tests/test_intent_router.py#L51) | 51 | `"    decision = route_intent(question, mode=mode)"` | — |
| [SRC-EA6EC52573-L000052](../../tests/test_intent_router.py#L52) | 52 | `""` | — |
| [SRC-EA6EC52573-L000053](../../tests/test_intent_router.py#L53) | 53 | `"    assert decision[\"route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-EA6EC52573-L000054](../../tests/test_intent_router.py#L54) | 54 | `"    assert decision[\"needs_clarification\"] is False"` | — |
| [SRC-EA6EC52573-L000055](../../tests/test_intent_router.py#L55) | 55 | `"    assert decision[\"reason\"] == \"explicit_buyer_discovery_with_selected_research_mode\""` | — |
| [SRC-EA6EC52573-L000056](../../tests/test_intent_router.py#L56) | 56 | `""` | — |
| [SRC-EA6EC52573-L000057](../../tests/test_intent_router.py#L57) | 57 | `""` | — |
| [SRC-EA6EC52573-L000058](../../tests/test_intent_router.py#L58) | 58 | `"def test_generic_explanation_of_lead_generation_is_not_a_lead_search() -> None:"` | — |
| [SRC-EA6EC52573-L000059](../../tests/test_intent_router.py#L59) | 59 | `"    assert route_intent(\"What is lead generation?\")[\"route\"] == \"MODEL_ONLY\""` | — |
| [SRC-EA6EC52573-L000060](../../tests/test_intent_router.py#L60) | 60 | `"    assert route_intent(\"Create a prospect list for apartment buyers\")[\"route\"] == \"LEAD_GENERATION\""` | — |
| [SRC-EA6EC52573-L000061](../../tests/test_intent_router.py#L61) | 61 | `""` | — |
| [SRC-EA6EC52573-L000062](../../tests/test_intent_router.py#L62) | 62 | `""` | — |
| [SRC-EA6EC52573-L000063](../../tests/test_intent_router.py#L63) | 63 | `""` | — |
| [SRC-EA6EC52573-L000064](../../tests/test_intent_router.py#L64) | 64 | `"def test_capability_question_is_local() -> None:"` | — |
| [SRC-EA6EC52573-L000065](../../tests/test_intent_router.py#L65) | 65 | `"    decision = route_intent("` | — |
| [SRC-EA6EC52573-L000066](../../tests/test_intent_router.py#L66) | 66 | `"        \"كيف تستطيع مساعدتي؟\","` | — |
| [SRC-EA6EC52573-L000067](../../tests/test_intent_router.py#L67) | 67 | `"        capability_question=True,"` | — |
| [SRC-EA6EC52573-L000068](../../tests/test_intent_router.py#L68) | 68 | `"        requires_web=False,"` | — |
| [SRC-EA6EC52573-L000069](../../tests/test_intent_router.py#L69) | 69 | `"    )"` | — |
| [SRC-EA6EC52573-L000070](../../tests/test_intent_router.py#L70) | 70 | `"    assert decision[\"route\"] == \"LOCAL\""` | — |
| [SRC-EA6EC52573-L000071](../../tests/test_intent_router.py#L71) | 71 | `"    assert decision[\"reason\"] == \"capability_question\""` | — |
| [SRC-EA6EC52573-L000072](../../tests/test_intent_router.py#L72) | 72 | `""` | — |
| [SRC-EA6EC52573-L000073](../../tests/test_intent_router.py#L73) | 73 | `""` | — |
| [SRC-EA6EC52573-L000074](../../tests/test_intent_router.py#L74) | 74 | `"def test_concrete_research_request_takes_precedence_over_capability_marker() -> None:"` | — |
| [SRC-EA6EC52573-L000075](../../tests/test_intent_router.py#L75) | 75 | `"    decision = route_intent("` | — |
| [SRC-EA6EC52573-L000076](../../tests/test_intent_router.py#L76) | 76 | `"        \"هل تستطيع البحث عن أحدث أسعار الذهب في مصر؟\","` | — |
| [SRC-EA6EC52573-L000077](../../tests/test_intent_router.py#L77) | 77 | `"        capability_question=True,"` | — |
| [SRC-EA6EC52573-L000078](../../tests/test_intent_router.py#L78) | 78 | `"        requires_web=True,"` | — |
| [SRC-EA6EC52573-L000079](../../tests/test_intent_router.py#L79) | 79 | `"    )"` | — |
| [SRC-EA6EC52573-L000080](../../tests/test_intent_router.py#L80) | 80 | `""` | — |
| [SRC-EA6EC52573-L000081](../../tests/test_intent_router.py#L81) | 81 | `"    assert decision[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000082](../../tests/test_intent_router.py#L82) | 82 | `"    assert decision[\"reason\"] == \"freshness_or_explicit_research_signal\""` | — |
| [SRC-EA6EC52573-L000083](../../tests/test_intent_router.py#L83) | 83 | `""` | — |
| [SRC-EA6EC52573-L000084](../../tests/test_intent_router.py#L84) | 84 | `""` | — |
| [SRC-EA6EC52573-L000085](../../tests/test_intent_router.py#L85) | 85 | `"def test_ambiguous_followup_uses_existing_conversation_context() -> None:"` | — |
| [SRC-EA6EC52573-L000086](../../tests/test_intent_router.py#L86) | 86 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000087](../../tests/test_intent_router.py#L87) | 87 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000088](../../tests/test_intent_router.py#L88) | 88 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن هاتف iPhone 17 في السوق المصري.\"},"` | — |
| [SRC-EA6EC52573-L000089](../../tests/test_intent_router.py#L89) | 89 | `"    ]"` | — |
| [SRC-EA6EC52573-L000090](../../tests/test_intent_router.py#L90) | 90 | `"    decision = route_intent(\"كام سعرها؟\", history, requires_web=True)"` | — |
| [SRC-EA6EC52573-L000091](../../tests/test_intent_router.py#L91) | 91 | `"    assert decision[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000092](../../tests/test_intent_router.py#L92) | 92 | `"    assert decision[\"context_available\"] is True"` | — |
| [SRC-EA6EC52573-L000093](../../tests/test_intent_router.py#L93) | 93 | `"    assert decision[\"needs_clarification\"] is False"` | — |
| [SRC-EA6EC52573-L000094](../../tests/test_intent_router.py#L94) | 94 | `""` | — |
| [SRC-EA6EC52573-L000095](../../tests/test_intent_router.py#L95) | 95 | `""` | — |
| [SRC-EA6EC52573-L000096](../../tests/test_intent_router.py#L96) | 96 | `"def test_comparison_followup_requires_context_before_deep_search() -> None:"` | — |
| [SRC-EA6EC52573-L000097](../../tests/test_intent_router.py#L97) | 97 | `"    assert route_intent(\"قارنهم\")[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000098](../../tests/test_intent_router.py#L98) | 98 | `"    history = [{\"role\": \"user\", \"content\": \"قارن iPhone 17 وSamsung S26\"}]"` | — |
| [SRC-EA6EC52573-L000099](../../tests/test_intent_router.py#L99) | 99 | `"    decision = route_intent(\"قارنهم\", history)"` | — |
| [SRC-EA6EC52573-L000100](../../tests/test_intent_router.py#L100) | 100 | `"    assert decision[\"route\"] == \"WEB_DEEP\""` | — |
| [SRC-EA6EC52573-L000101](../../tests/test_intent_router.py#L101) | 101 | `"    assert decision[\"context_available\"] is True"` | — |
| [SRC-EA6EC52573-L000102](../../tests/test_intent_router.py#L102) | 102 | `""` | — |
| [SRC-EA6EC52573-L000103](../../tests/test_intent_router.py#L103) | 103 | `""` | — |
| [SRC-EA6EC52573-L000104](../../tests/test_intent_router.py#L104) | 104 | `"def test_ambiguous_followup_does_not_reuse_stale_topic_after_acknowledgment() -> None:"` | — |
| [SRC-EA6EC52573-L000105](../../tests/test_intent_router.py#L105) | 105 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000106](../../tests/test_intent_router.py#L106) | 106 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000107](../../tests/test_intent_router.py#L107) | 107 | `"        {\"role\": \"assistant\", \"content\": \"سأساعدك في العثور على أسعار حديثة.\"},"` | — |
| [SRC-EA6EC52573-L000108](../../tests/test_intent_router.py#L108) | 108 | `"        {\"role\": \"user\", \"content\": \"شكرا\"},"` | — |
| [SRC-EA6EC52573-L000109](../../tests/test_intent_router.py#L109) | 109 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-EA6EC52573-L000110](../../tests/test_intent_router.py#L110) | 110 | `"    ]"` | — |
| [SRC-EA6EC52573-L000111](../../tests/test_intent_router.py#L111) | 111 | `"    decision = route_intent(\"كام سعرها؟\", history, requires_web=True)"` | — |
| [SRC-EA6EC52573-L000112](../../tests/test_intent_router.py#L112) | 112 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000113](../../tests/test_intent_router.py#L113) | 113 | `"    assert decision[\"context_available\"] is False"` | — |
| [SRC-EA6EC52573-L000114](../../tests/test_intent_router.py#L114) | 114 | `""` | — |
| [SRC-EA6EC52573-L000115](../../tests/test_intent_router.py#L115) | 115 | `""` | — |
| [SRC-EA6EC52573-L000116](../../tests/test_intent_router.py#L116) | 116 | `"def test_explicit_mode_overrides_conversational_shortcuts() -> None:"` | — |
| [SRC-EA6EC52573-L000117](../../tests/test_intent_router.py#L117) | 117 | `"    assert route_intent(\"ازيك؟\", mode=\"deep\")[\"route\"] == \"WEB_DEEP\""` | — |
| [SRC-EA6EC52573-L000118](../../tests/test_intent_router.py#L118) | 118 | `"    assert route_intent(\"ما سعر الهاتف؟\", mode=\"latest\")[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000119](../../tests/test_intent_router.py#L119) | 119 | `""` | — |
| [SRC-EA6EC52573-L000120](../../tests/test_intent_router.py#L120) | 120 | `""` | — |
| [SRC-EA6EC52573-L000121](../../tests/test_intent_router.py#L121) | 121 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000122](../../tests/test_intent_router.py#L122) | 122 | `"    (\"question\", \"expected_route\", \"expected_reason\"),"` | — |
| [SRC-EA6EC52573-L000123](../../tests/test_intent_router.py#L123) | 123 | `"    ["` | — |
| [SRC-EA6EC52573-L000124](../../tests/test_intent_router.py#L124) | 124 | `"        ("` | — |
| [SRC-EA6EC52573-L000125](../../tests/test_intent_router.py#L125) | 125 | `"            \"لخص الصفحة https://example.com/article\","` | — |
| [SRC-EA6EC52573-L000126](../../tests/test_intent_router.py#L126) | 126 | `"            \"WEB_SIMPLE\","` | — |
| [SRC-EA6EC52573-L000127](../../tests/test_intent_router.py#L127) | 127 | `"            \"summarization_request\","` | — |
| [SRC-EA6EC52573-L000128](../../tests/test_intent_router.py#L128) | 128 | `"        ),"` | — |
| [SRC-EA6EC52573-L000129](../../tests/test_intent_router.py#L129) | 129 | `"        ("` | — |
| [SRC-EA6EC52573-L000130](../../tests/test_intent_router.py#L130) | 130 | `"            \"Summarize this page https://example.com/article\","` | — |
| [SRC-EA6EC52573-L000131](../../tests/test_intent_router.py#L131) | 131 | `"            \"WEB_SIMPLE\","` | — |
| [SRC-EA6EC52573-L000132](../../tests/test_intent_router.py#L132) | 132 | `"            \"summarization_request\","` | — |
| [SRC-EA6EC52573-L000133](../../tests/test_intent_router.py#L133) | 133 | `"        ),"` | — |
| [SRC-EA6EC52573-L000134](../../tests/test_intent_router.py#L134) | 134 | `"        (\"لخص الصفحة\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000135](../../tests/test_intent_router.py#L135) | 135 | `"        (\"لخص لي هذا الرابط\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000136](../../tests/test_intent_router.py#L136) | 136 | `"        (\"summarize the page\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000137](../../tests/test_intent_router.py#L137) | 137 | `"        (\"تلخيص المقال\", \"CLARIFY\", \"missing_summarization_input\"),"` | — |
| [SRC-EA6EC52573-L000138](../../tests/test_intent_router.py#L138) | 138 | `"        (\"لخص النص التالي: هذا نص تجريبي\", \"MODEL_ONLY\", \"stable_knowledge_or_conversation\"),"` | — |
| [SRC-EA6EC52573-L000139](../../tests/test_intent_router.py#L139) | 139 | `"        (\"Summarize this text: the test content is here\", \"MODEL_ONLY\", \"stable_knowledge_or_conversation\"),"` | — |
| [SRC-EA6EC52573-L000140](../../tests/test_intent_router.py#L140) | 140 | `"    ],"` | — |
| [SRC-EA6EC52573-L000141](../../tests/test_intent_router.py#L141) | 141 | `")"` | — |
| [SRC-EA6EC52573-L000142](../../tests/test_intent_router.py#L142) | 142 | `"def test_summarization_routing_respects_page_text_and_missing_input("` | — |
| [SRC-EA6EC52573-L000143](../../tests/test_intent_router.py#L143) | 143 | `"    question: str, expected_route: str, expected_reason: str"` | — |
| [SRC-EA6EC52573-L000144](../../tests/test_intent_router.py#L144) | 144 | `") -> None:"` | — |
| [SRC-EA6EC52573-L000145](../../tests/test_intent_router.py#L145) | 145 | `"    decision = route_intent(question, [])"` | — |
| [SRC-EA6EC52573-L000146](../../tests/test_intent_router.py#L146) | 146 | `"    assert decision[\"route\"] == expected_route"` | — |
| [SRC-EA6EC52573-L000147](../../tests/test_intent_router.py#L147) | 147 | `"    assert decision[\"reason\"] == expected_reason"` | — |
| [SRC-EA6EC52573-L000148](../../tests/test_intent_router.py#L148) | 148 | `""` | — |
| [SRC-EA6EC52573-L000149](../../tests/test_intent_router.py#L149) | 149 | `""` | — |
| [SRC-EA6EC52573-L000150](../../tests/test_intent_router.py#L150) | 150 | `"@pytest.mark.parametrize("` | — |
| [SRC-EA6EC52573-L000151](../../tests/test_intent_router.py#L151) | 151 | `"    \"question\","` | — |
| [SRC-EA6EC52573-L000152](../../tests/test_intent_router.py#L152) | 152 | `"    ["` | — |
| [SRC-EA6EC52573-L000153](../../tests/test_intent_router.py#L153) | 153 | `"        \"فين؟\","` | — |
| [SRC-EA6EC52573-L000154](../../tests/test_intent_router.py#L154) | 154 | `"        \"فين هي؟\","` | — |
| [SRC-EA6EC52573-L000155](../../tests/test_intent_router.py#L155) | 155 | `"        \"مكانها فين؟\","` | — |
| [SRC-EA6EC52573-L000156](../../tests/test_intent_router.py#L156) | 156 | `"        \"هل فيه ضمان؟\","` | — |
| [SRC-EA6EC52573-L000157](../../tests/test_intent_router.py#L157) | 157 | `"        \"هل لها ضمان؟\","` | — |
| [SRC-EA6EC52573-L000158](../../tests/test_intent_router.py#L158) | 158 | `"        \"ضمانها إيه؟\","` | — |
| [SRC-EA6EC52573-L000159](../../tests/test_intent_router.py#L159) | 159 | `"        \"Where is it?\","` | — |
| [SRC-EA6EC52573-L000160](../../tests/test_intent_router.py#L160) | 160 | `"        \"Does it have a warranty?\","` | — |
| [SRC-EA6EC52573-L000161](../../tests/test_intent_router.py#L161) | 161 | `"    ],"` | — |
| [SRC-EA6EC52573-L000162](../../tests/test_intent_router.py#L162) | 162 | `")"` | — |
| [SRC-EA6EC52573-L000163](../../tests/test_intent_router.py#L163) | 163 | `"def test_missing_referent_questions_clarify_without_context(question: str) -> None:"` | — |
| [SRC-EA6EC52573-L000164](../../tests/test_intent_router.py#L164) | 164 | `"    decision = route_intent(question, history=None, mode=\"auto\", requires_web=True)"` | — |
| [SRC-EA6EC52573-L000165](../../tests/test_intent_router.py#L165) | 165 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000166](../../tests/test_intent_router.py#L166) | 166 | `"    assert decision[\"needs_clarification\"] is True"` | — |
| [SRC-EA6EC52573-L000167](../../tests/test_intent_router.py#L167) | 167 | `"    assert decision[\"context_available\"] is False"` | — |
| [SRC-EA6EC52573-L000168](../../tests/test_intent_router.py#L168) | 168 | `""` | — |
| [SRC-EA6EC52573-L000169](../../tests/test_intent_router.py#L169) | 169 | `""` | — |
| [SRC-EA6EC52573-L000170](../../tests/test_intent_router.py#L170) | 170 | `"@pytest.mark.parametrize(\"question\", [\"فين؟\", \"هل فيه ضمان؟\", \"كام سعرها؟\"])"` | — |
| [SRC-EA6EC52573-L000171](../../tests/test_intent_router.py#L171) | 171 | `"def test_missing_referent_still_clarifies_in_explicit_search_mode(question: str) -> None:"` | — |
| [SRC-EA6EC52573-L000172](../../tests/test_intent_router.py#L172) | 172 | `"    decision = route_intent(question, history=None, mode=\"deep\")"` | — |
| [SRC-EA6EC52573-L000173](../../tests/test_intent_router.py#L173) | 173 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000174](../../tests/test_intent_router.py#L174) | 174 | `"    assert decision[\"needs_clarification\"] is True"` | — |
| [SRC-EA6EC52573-L000175](../../tests/test_intent_router.py#L175) | 175 | `""` | — |
| [SRC-EA6EC52573-L000176](../../tests/test_intent_router.py#L176) | 176 | `""` | — |
| [SRC-EA6EC52573-L000177](../../tests/test_intent_router.py#L177) | 177 | `"def test_followup_resolver_uses_topic_from_latest_user_turn() -> None:"` | — |
| [SRC-EA6EC52573-L000178](../../tests/test_intent_router.py#L178) | 178 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000179](../../tests/test_intent_router.py#L179) | 179 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر آيفون 16 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000180](../../tests/test_intent_router.py#L180) | 180 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن معلومات موثوقة.\"},"` | — |
| [SRC-EA6EC52573-L000181](../../tests/test_intent_router.py#L181) | 181 | `"    ]"` | — |
| [SRC-EA6EC52573-L000182](../../tests/test_intent_router.py#L182) | 182 | `"    resolved = resolve_followup_query(\"هل فيه ضمان؟\", history)"` | — |
| [SRC-EA6EC52573-L000183](../../tests/test_intent_router.py#L183) | 183 | `"    assert \"آيفون 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000184](../../tests/test_intent_router.py#L184) | 184 | `"    assert \"ضمان\" in resolved"` | — |
| [SRC-EA6EC52573-L000185](../../tests/test_intent_router.py#L185) | 185 | `""` | — |
| [SRC-EA6EC52573-L000186](../../tests/test_intent_router.py#L186) | 186 | `""` | — |
| [SRC-EA6EC52573-L000187](../../tests/test_intent_router.py#L187) | 187 | `"def test_followup_resolver_does_not_resurrect_topic_after_acknowledgment() -> None:"` | — |
| [SRC-EA6EC52573-L000188](../../tests/test_intent_router.py#L188) | 188 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000189](../../tests/test_intent_router.py#L189) | 189 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر آيفون 16 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000190](../../tests/test_intent_router.py#L190) | 190 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن معلومات موثوقة.\"},"` | — |
| [SRC-EA6EC52573-L000191](../../tests/test_intent_router.py#L191) | 191 | `"        {\"role\": \"user\", \"content\": \"شكرًا\"},"` | — |
| [SRC-EA6EC52573-L000192](../../tests/test_intent_router.py#L192) | 192 | `"        {\"role\": \"assistant\", \"content\": \"العفو.\"},"` | — |
| [SRC-EA6EC52573-L000193](../../tests/test_intent_router.py#L193) | 193 | `"    ]"` | — |
| [SRC-EA6EC52573-L000194](../../tests/test_intent_router.py#L194) | 194 | `"    assert resolve_followup_query(\"فين؟\", history) == \"فين؟\""` | — |
| [SRC-EA6EC52573-L000195](../../tests/test_intent_router.py#L195) | 195 | `""` | — |
| [SRC-EA6EC52573-L000196](../../tests/test_intent_router.py#L196) | 196 | `""` | — |
| [SRC-EA6EC52573-L000197](../../tests/test_intent_router.py#L197) | 197 | `"def test_followup_resolver_bounds_output_and_handles_malformed_history() -> None:"` | — |
| [SRC-EA6EC52573-L000198](../../tests/test_intent_router.py#L198) | 198 | `"    history = [{\"role\": \"user\", \"content\": \"س\" * 4000}]"` | — |
| [SRC-EA6EC52573-L000199](../../tests/test_intent_router.py#L199) | 199 | `"    assert len(resolve_followup_query(\"والسعر؟\", history)) <= 500"` | — |
| [SRC-EA6EC52573-L000200](../../tests/test_intent_router.py#L200) | 200 | `"    assert resolve_followup_query(\"فين؟\", {\"role\": \"user\", \"content\": \"topic\"}) == \"فين؟\""` | — |
| [SRC-EA6EC52573-L000201](../../tests/test_intent_router.py#L201) | 201 | `""` | — |
| [SRC-EA6EC52573-L000202](../../tests/test_intent_router.py#L202) | 202 | `"def test_prefixed_elliptical_followup_is_clarified_without_topic():"` | — |
| [SRC-EA6EC52573-L000203](../../tests/test_intent_router.py#L203) | 203 | `"    for question in (\"طب هل فيه ضمان؟\", \"طيب كام سعرها؟\", \"والضمان؟\", \"والسعر؟\"):"` | — |
| [SRC-EA6EC52573-L000204](../../tests/test_intent_router.py#L204) | 204 | `"        decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000205](../../tests/test_intent_router.py#L205) | 205 | `"        assert decision[\"route\"] == \"CLARIFY\", question"` | — |
| [SRC-EA6EC52573-L000206](../../tests/test_intent_router.py#L206) | 206 | `""` | — |
| [SRC-EA6EC52573-L000207](../../tests/test_intent_router.py#L207) | 207 | `"def test_prefixed_elliptical_followup_uses_topic_when_available():"` | — |
| [SRC-EA6EC52573-L000208](../../tests/test_intent_router.py#L208) | 208 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000209](../../tests/test_intent_router.py#L209) | 209 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 16 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000210](../../tests/test_intent_router.py#L210) | 210 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن iPhone 16 في مصر.\"},"` | — |
| [SRC-EA6EC52573-L000211](../../tests/test_intent_router.py#L211) | 211 | `"    ]"` | — |
| [SRC-EA6EC52573-L000212](../../tests/test_intent_router.py#L212) | 212 | `"    for question in (\"طب هل فيه ضمان؟\", \"طيب كام سعرها؟\", \"والضمان؟\"):"` | — |
| [SRC-EA6EC52573-L000213](../../tests/test_intent_router.py#L213) | 213 | `"        decision = route_intent(question, history, requires_web=True)"` | — |
| [SRC-EA6EC52573-L000214](../../tests/test_intent_router.py#L214) | 214 | `"        assert decision[\"route\"] == \"WEB_SIMPLE\", question"` | — |
| [SRC-EA6EC52573-L000215](../../tests/test_intent_router.py#L215) | 215 | `"        resolved = resolve_followup_query(question, history)"` | — |
| [SRC-EA6EC52573-L000216](../../tests/test_intent_router.py#L216) | 216 | `"        assert \"iPhone 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000217](../../tests/test_intent_router.py#L217) | 217 | `"        assert \"مصر\" in resolved"` | — |
| [SRC-EA6EC52573-L000218](../../tests/test_intent_router.py#L218) | 218 | `""` | — |
| [SRC-EA6EC52573-L000219](../../tests/test_intent_router.py#L219) | 219 | `"def test_long_arabic_warranty_followup_resolves_with_context():"` | — |
| [SRC-EA6EC52573-L000220](../../tests/test_intent_router.py#L220) | 220 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000221](../../tests/test_intent_router.py#L221) | 221 | `"        {\"role\": \"user\", \"content\": \"عايز أعرف سعر iPhone 17 نسخة 256 جيجابايت في مصر\"},"` | — |
| [SRC-EA6EC52573-L000222](../../tests/test_intent_router.py#L222) | 222 | `"        {\"role\": \"assistant\", \"content\": \"سأبحث عن السعر.\"},"` | — |
| [SRC-EA6EC52573-L000223](../../tests/test_intent_router.py#L223) | 223 | `"    ]"` | — |
| [SRC-EA6EC52573-L000224](../../tests/test_intent_router.py#L224) | 224 | `"    question = \"وطب الضمان الدولي بيسري في مصر؟\""` | — |
| [SRC-EA6EC52573-L000225](../../tests/test_intent_router.py#L225) | 225 | `"    resolved = resolve_followup_query(question, history)"` | — |
| [SRC-EA6EC52573-L000226](../../tests/test_intent_router.py#L226) | 226 | `"    assert \"iPhone 17\" in resolved"` | — |
| [SRC-EA6EC52573-L000227](../../tests/test_intent_router.py#L227) | 227 | `"    assert question in resolved"` | — |
| [SRC-EA6EC52573-L000228](../../tests/test_intent_router.py#L228) | 228 | `""` | — |
| [SRC-EA6EC52573-L000229](../../tests/test_intent_router.py#L229) | 229 | `"def test_long_arabic_warranty_followup_without_context_clarifies():"` | — |
| [SRC-EA6EC52573-L000230](../../tests/test_intent_router.py#L230) | 230 | `"    question = \"وطب الضمان الدولي بيسري في مصر؟\""` | — |
| [SRC-EA6EC52573-L000231](../../tests/test_intent_router.py#L231) | 231 | `"    decision = route_intent(question)"` | — |
| [SRC-EA6EC52573-L000232](../../tests/test_intent_router.py#L232) | 232 | `"    assert decision[\"route\"] == \"CLARIFY\""` | — |
| [SRC-EA6EC52573-L000233](../../tests/test_intent_router.py#L233) | 233 | `"    assert decision[\"needs_clarification\"] is True"` | — |
| [SRC-EA6EC52573-L000234](../../tests/test_intent_router.py#L234) | 234 | `""` | — |
| [SRC-EA6EC52573-L000235](../../tests/test_intent_router.py#L235) | 235 | `"def test_new_question_starting_with_tayyib_does_not_inherit_old_topic():"` | — |
| [SRC-EA6EC52573-L000236](../../tests/test_intent_router.py#L236) | 236 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000237](../../tests/test_intent_router.py#L237) | 237 | `"        {\"role\": \"user\", \"content\": \"ما سعر iPhone 16 في مصر؟\"},"` | — |
| [SRC-EA6EC52573-L000238](../../tests/test_intent_router.py#L238) | 238 | `"        {\"role\": \"assistant\", \"content\": \"هذه بعض معلومات السعر.\"},"` | — |
| [SRC-EA6EC52573-L000239](../../tests/test_intent_router.py#L239) | 239 | `"    ]"` | — |
| [SRC-EA6EC52573-L000240](../../tests/test_intent_router.py#L240) | 240 | `"    question = \"طيب اشرح الذكاء الاصطناعي في المدارس\""` | — |
| [SRC-EA6EC52573-L000241](../../tests/test_intent_router.py#L241) | 241 | `"    assert resolve_followup_query(question, history) == question"` | — |
| [SRC-EA6EC52573-L000242](../../tests/test_intent_router.py#L242) | 242 | `"    decision = route_intent(question, history)"` | — |
| [SRC-EA6EC52573-L000243](../../tests/test_intent_router.py#L243) | 243 | `"    assert decision[\"route\"] == \"MODEL_ONLY\""` | — |
| [SRC-EA6EC52573-L000244](../../tests/test_intent_router.py#L244) | 244 | `""` | — |
| [SRC-EA6EC52573-L000245](../../tests/test_intent_router.py#L245) | 245 | `"def test_chained_followups_keep_the_last_substantive_topic():"` | — |
| [SRC-EA6EC52573-L000246](../../tests/test_intent_router.py#L246) | 246 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000247](../../tests/test_intent_router.py#L247) | 247 | `"        {\"role\": \"user\", \"content\": \"ما سعر iPhone 16 في مصر؟\"},"` | — |
| [SRC-EA6EC52573-L000248](../../tests/test_intent_router.py#L248) | 248 | `"        {\"role\": \"assistant\", \"content\": \"السعر يختلف حسب المتجر.\"},"` | — |
| [SRC-EA6EC52573-L000249](../../tests/test_intent_router.py#L249) | 249 | `"        {\"role\": \"user\", \"content\": \"والضمان؟\"},"` | — |
| [SRC-EA6EC52573-L000250](../../tests/test_intent_router.py#L250) | 250 | `"        {\"role\": \"assistant\", \"content\": \"سأوضح الضمان.\"},"` | — |
| [SRC-EA6EC52573-L000251](../../tests/test_intent_router.py#L251) | 251 | `"    ]"` | — |
| [SRC-EA6EC52573-L000252](../../tests/test_intent_router.py#L252) | 252 | `"    resolved = resolve_followup_query(\"والبطارية؟\", history)"` | — |
| [SRC-EA6EC52573-L000253](../../tests/test_intent_router.py#L253) | 253 | `"    assert \"iPhone 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000254](../../tests/test_intent_router.py#L254) | 254 | `"    assert \"البطارية\" in resolved"` | — |
| [SRC-EA6EC52573-L000255](../../tests/test_intent_router.py#L255) | 255 | `""` | — |
| [SRC-EA6EC52573-L000256](../../tests/test_intent_router.py#L256) | 256 | `"def test_answer_to_clarification_restores_original_intent():"` | — |
| [SRC-EA6EC52573-L000257](../../tests/test_intent_router.py#L257) | 257 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000258](../../tests/test_intent_router.py#L258) | 258 | `"        {\"role\": \"user\", \"content\": \"كام سعرها؟\"},"` | — |
| [SRC-EA6EC52573-L000259](../../tests/test_intent_router.py#L259) | 259 | `"        {"` | — |
| [SRC-EA6EC52573-L000260](../../tests/test_intent_router.py#L260) | 260 | `"            \"role\": \"assistant\","` | — |
| [SRC-EA6EC52573-L000261](../../tests/test_intent_router.py#L261) | 261 | `"            \"content\": \"تقصد إيه تحديدًا؟ اكتب اسم الشيء أو المنتج المقصود، أو ابعت الرابط، وأكمل معاك من غير ما أخمّن.\","` | — |
| [SRC-EA6EC52573-L000262](../../tests/test_intent_router.py#L262) | 262 | `"        },"` | — |
| [SRC-EA6EC52573-L000263](../../tests/test_intent_router.py#L263) | 263 | `"    ]"` | — |
| [SRC-EA6EC52573-L000264](../../tests/test_intent_router.py#L264) | 264 | `"    decision = route_intent(\"iPhone 16\", history)"` | — |
| [SRC-EA6EC52573-L000265](../../tests/test_intent_router.py#L265) | 265 | `"    assert decision[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000266](../../tests/test_intent_router.py#L266) | 266 | `"    assert decision[\"reason\"] == \"answer_to_pending_clarification\""` | — |
| [SRC-EA6EC52573-L000267](../../tests/test_intent_router.py#L267) | 267 | `"    resolved = resolve_followup_query(\"iPhone 16\", history)"` | — |
| [SRC-EA6EC52573-L000268](../../tests/test_intent_router.py#L268) | 268 | `"    assert \"سعرها\" in resolved"` | — |
| [SRC-EA6EC52573-L000269](../../tests/test_intent_router.py#L269) | 269 | `"    assert \"iPhone 16\" in resolved"` | — |
| [SRC-EA6EC52573-L000270](../../tests/test_intent_router.py#L270) | 270 | `""` | — |
| [SRC-EA6EC52573-L000271](../../tests/test_intent_router.py#L271) | 271 | `"def test_topic_detection_does_not_inherit_old_social_or_depth_intent():"` | — |
| [SRC-EA6EC52573-L000272](../../tests/test_intent_router.py#L272) | 272 | `"    from agents.research import fallback_plan"` | — |
| [SRC-EA6EC52573-L000273](../../tests/test_intent_router.py#L273) | 273 | `""` | — |
| [SRC-EA6EC52573-L000274](../../tests/test_intent_router.py#L274) | 274 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000275](../../tests/test_intent_router.py#L275) | 275 | `"        {\"role\": \"user\", \"content\": \"اجمع آراء مستخدمي السيارات الكهربائية على Reddit\"},"` | — |
| [SRC-EA6EC52573-L000276](../../tests/test_intent_router.py#L276) | 276 | `"        {\"role\": \"assistant\", \"content\": \"هذه النتائج.\"},"` | — |
| [SRC-EA6EC52573-L000277](../../tests/test_intent_router.py#L277) | 277 | `"    ]"` | — |
| [SRC-EA6EC52573-L000278](../../tests/test_intent_router.py#L278) | 278 | `"    plan = fallback_plan(\"اشرح طريقة عمل المحرك الكهربائي\", history)"` | — |
| [SRC-EA6EC52573-L000279](../../tests/test_intent_router.py#L279) | 279 | `"    assert plan[\"social_focus\"] is False"` | — |
| [SRC-EA6EC52573-L000280](../../tests/test_intent_router.py#L280) | 280 | `"    assert plan[\"platforms\"] == []"` | — |
| [SRC-EA6EC52573-L000281](../../tests/test_intent_router.py#L281) | 281 | `"    assert plan[\"depth\"] == \"standard\""` | — |
| [SRC-EA6EC52573-L000282](../../tests/test_intent_router.py#L282) | 282 | `""` | — |
| [SRC-EA6EC52573-L000283](../../tests/test_intent_router.py#L283) | 283 | `"def test_explicit_request_for_reliable_sources_uses_web_search_in_auto_mode():"` | — |
| [SRC-EA6EC52573-L000284](../../tests/test_intent_router.py#L284) | 284 | `"    question = ("` | — |
| [SRC-EA6EC52573-L000285](../../tests/test_intent_router.py#L285) | 285 | `"        \"ما أهم استخدامات الذكاء الاصطناعي في الشركات الصغيرة؟ \""` | — |
| [SRC-EA6EC52573-L000286](../../tests/test_intent_router.py#L286) | 286 | `"        \"اذكر أمثلة ومصادر موثوقة.\""` | — |
| [SRC-EA6EC52573-L000287](../../tests/test_intent_router.py#L287) | 287 | `"    )"` | — |
| [SRC-EA6EC52573-L000288](../../tests/test_intent_router.py#L288) | 288 | `"    decision = route_intent(question, mode=\"auto\")"` | — |
| [SRC-EA6EC52573-L000289](../../tests/test_intent_router.py#L289) | 289 | `"    assert decision[\"route\"] == \"WEB_SIMPLE\""` | — |
| [SRC-EA6EC52573-L000290](../../tests/test_intent_router.py#L290) | 290 | `"    assert decision[\"reason\"] == \"explicit_evidence_request\""` | — |
| [SRC-EA6EC52573-L000291](../../tests/test_intent_router.py#L291) | 291 | `""` | — |
| [SRC-EA6EC52573-L000292](../../tests/test_intent_router.py#L292) | 292 | `"def test_stable_question_without_source_request_remains_model_only():"` | — |
| [SRC-EA6EC52573-L000293](../../tests/test_intent_router.py#L293) | 293 | `"    decision = route_intent(\"اشرح الفرق بين التعلم الخاضع للإشراف وغير الخاضع للإشراف\")"` | — |
| [SRC-EA6EC52573-L000294](../../tests/test_intent_router.py#L294) | 294 | `"    assert decision[\"route\"] == \"MODEL_ONLY\""` | — |
| [SRC-EA6EC52573-L000295](../../tests/test_intent_router.py#L295) | 295 | `""` | — |
| [SRC-EA6EC52573-L000296](../../tests/test_intent_router.py#L296) | 296 | `"def test_attached_arabic_object_pronoun_resolves_against_previous_subject() -> None:"` | — |
| [SRC-EA6EC52573-L000297](../../tests/test_intent_router.py#L297) | 297 | `"    history = ["` | — |
| [SRC-EA6EC52573-L000298](../../tests/test_intent_router.py#L298) | 298 | `"        {\"role\": \"user\", \"content\": \"بفكر أشتري Lenovo ThinkPad E14 في مصر\"},"` | — |
| [SRC-EA6EC52573-L000299](../../tests/test_intent_router.py#L299) | 299 | `"        {\"role\": \"assistant\", \"content\": \"نتحدث عن Lenovo ThinkPad E14 في السوق المصري.\"},"` | — |
| [SRC-EA6EC52573-L000300](../../tests/test_intent_router.py#L300) | 300 | `"    ]"` | — |
| [SRC-EA6EC52573-L000301](../../tests/test_intent_router.py#L301) | 301 | `""` | — |
| [SRC-EA6EC52573-L000302](../../tests/test_intent_router.py#L302) | 302 | `"    resolved = resolve_followup_query(\"أقدر أشتريه منين؟\", history)"` | — |
| [SRC-EA6EC52573-L000303](../../tests/test_intent_router.py#L303) | 303 | `""` | — |
