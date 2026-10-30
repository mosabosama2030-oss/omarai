# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **030**
- سجلات الأسطر: **800**
- النطاق: SRC-4FFD5AFC54-L000296 إلى SRC-547CAF1FE3-L000130
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## ملفات أخرى

### FILE-4FFD5AFC54 — [scripts/run_answer_quality_benchmark.py](../../scripts/run_answer_quality_benchmark.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-4FFD5AFC54-L000296](../../scripts/run_answer_quality_benchmark.py#L296) | 296 | `"    if parsed.path not in {\"\", \"/\"} or parsed.query or parsed.fragment:"` | — |
| [SRC-4FFD5AFC54-L000297](../../scripts/run_answer_quality_benchmark.py#L297) | 297 | `"        raise ValueError(\"Base URL must contain only the origin, without path, query, or fragment.\")"` | — |
| [SRC-4FFD5AFC54-L000298](../../scripts/run_answer_quality_benchmark.py#L298) | 298 | `""` | — |
| [SRC-4FFD5AFC54-L000299](../../scripts/run_answer_quality_benchmark.py#L299) | 299 | `"    loopback = host == \"localhost\""` | — |
| [SRC-4FFD5AFC54-L000300](../../scripts/run_answer_quality_benchmark.py#L300) | 300 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000301](../../scripts/run_answer_quality_benchmark.py#L301) | 301 | `"        loopback = ipaddress.ip_address(host).is_loopback"` | — |
| [SRC-4FFD5AFC54-L000302](../../scripts/run_answer_quality_benchmark.py#L302) | 302 | `"    except ValueError:"` | — |
| [SRC-4FFD5AFC54-L000303](../../scripts/run_answer_quality_benchmark.py#L303) | 303 | `"        pass"` | — |
| [SRC-4FFD5AFC54-L000304](../../scripts/run_answer_quality_benchmark.py#L304) | 304 | `""` | — |
| [SRC-4FFD5AFC54-L000305](../../scripts/run_answer_quality_benchmark.py#L305) | 305 | `"    if scheme == \"http\" and not loopback:"` | — |
| [SRC-4FFD5AFC54-L000306](../../scripts/run_answer_quality_benchmark.py#L306) | 306 | `"        raise ValueError(\"Plain HTTP is allowed only for localhost or a loopback IP.\")"` | — |
| [SRC-4FFD5AFC54-L000307](../../scripts/run_answer_quality_benchmark.py#L307) | 307 | `""` | — |
| [SRC-4FFD5AFC54-L000308](../../scripts/run_answer_quality_benchmark.py#L308) | 308 | `"    if (scheme == \"https\" and port == 443) or (scheme == \"http\" and port == 80):"` | — |
| [SRC-4FFD5AFC54-L000309](../../scripts/run_answer_quality_benchmark.py#L309) | 309 | `"        port = None"` | — |
| [SRC-4FFD5AFC54-L000310](../../scripts/run_answer_quality_benchmark.py#L310) | 310 | `"    host_for_origin = f\"[{host}]\" if \":\" in host else host"` | — |
| [SRC-4FFD5AFC54-L000311](../../scripts/run_answer_quality_benchmark.py#L311) | 311 | `"    origin = f\"{scheme}://{host_for_origin}\" + (f\":{port}\" if port is not None else \"\")"` | — |
| [SRC-4FFD5AFC54-L000312](../../scripts/run_answer_quality_benchmark.py#L312) | 312 | `""` | — |
| [SRC-4FFD5AFC54-L000313](../../scripts/run_answer_quality_benchmark.py#L313) | 313 | `"    if token_present and not loopback:"` | — |
| [SRC-4FFD5AFC54-L000314](../../scripts/run_answer_quality_benchmark.py#L314) | 314 | `"        allowed = os.getenv(\"OMARAI_BENCHMARK_ALLOWED_ORIGIN\", \"\").strip()"` | — |
| [SRC-4FFD5AFC54-L000315](../../scripts/run_answer_quality_benchmark.py#L315) | 315 | `"        if not allowed:"` | — |
| [SRC-4FFD5AFC54-L000316](../../scripts/run_answer_quality_benchmark.py#L316) | 316 | `"            raise ValueError("` | — |
| [SRC-4FFD5AFC54-L000317](../../scripts/run_answer_quality_benchmark.py#L317) | 317 | `"                \"A bearer token requires OMARAI_BENCHMARK_ALLOWED_ORIGIN to match \""` | — |
| [SRC-4FFD5AFC54-L000318](../../scripts/run_answer_quality_benchmark.py#L318) | 318 | `"                \"the exact HTTPS deployment origin.\""` | — |
| [SRC-4FFD5AFC54-L000319](../../scripts/run_answer_quality_benchmark.py#L319) | 319 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000320](../../scripts/run_answer_quality_benchmark.py#L320) | 320 | `"        allowed_origin = validate_base_url(allowed, token_present=False)"` | — |
| [SRC-4FFD5AFC54-L000321](../../scripts/run_answer_quality_benchmark.py#L321) | 321 | `"        if allowed_origin != origin:"` | — |
| [SRC-4FFD5AFC54-L000322](../../scripts/run_answer_quality_benchmark.py#L322) | 322 | `"            raise ValueError("` | — |
| [SRC-4FFD5AFC54-L000323](../../scripts/run_answer_quality_benchmark.py#L323) | 323 | `"                \"Refusing to send the bearer token: base URL does not match \""` | — |
| [SRC-4FFD5AFC54-L000324](../../scripts/run_answer_quality_benchmark.py#L324) | 324 | `"                \"OMARAI_BENCHMARK_ALLOWED_ORIGIN.\""` | — |
| [SRC-4FFD5AFC54-L000325](../../scripts/run_answer_quality_benchmark.py#L325) | 325 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000326](../../scripts/run_answer_quality_benchmark.py#L326) | 326 | `"    return origin"` | — |
| [SRC-4FFD5AFC54-L000327](../../scripts/run_answer_quality_benchmark.py#L327) | 327 | `""` | — |
| [SRC-4FFD5AFC54-L000328](../../scripts/run_answer_quality_benchmark.py#L328) | 328 | `""` | — |
| [SRC-4FFD5AFC54-L000329](../../scripts/run_answer_quality_benchmark.py#L329) | 329 | `"class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):"` | — |
| [SRC-4FFD5AFC54-L000330](../../scripts/run_answer_quality_benchmark.py#L330) | 330 | `"    \"\"\"Do not follow redirects; the bearer token must never move to another origin.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000331](../../scripts/run_answer_quality_benchmark.py#L331) | 331 | `""` | — |
| [SRC-4FFD5AFC54-L000332](../../scripts/run_answer_quality_benchmark.py#L332) | 332 | `"    def redirect_request(self, req, fp, code, msg, headers, newurl):"` | — |
| [SRC-4FFD5AFC54-L000333](../../scripts/run_answer_quality_benchmark.py#L333) | 333 | `"        return None"` | — |
| [SRC-4FFD5AFC54-L000334](../../scripts/run_answer_quality_benchmark.py#L334) | 334 | `""` | — |
| [SRC-4FFD5AFC54-L000335](../../scripts/run_answer_quality_benchmark.py#L335) | 335 | `""` | — |
| [SRC-4FFD5AFC54-L000336](../../scripts/run_answer_quality_benchmark.py#L336) | 336 | `"_NO_REDIRECT_OPENER = urllib.request.build_opener(_NoRedirectHandler())"` | — |
| [SRC-4FFD5AFC54-L000337](../../scripts/run_answer_quality_benchmark.py#L337) | 337 | `""` | — |
| [SRC-4FFD5AFC54-L000338](../../scripts/run_answer_quality_benchmark.py#L338) | 338 | `"REQUIRED_FIELDS = {"` | — |
| [SRC-4FFD5AFC54-L000339](../../scripts/run_answer_quality_benchmark.py#L339) | 339 | `"    \"case_id\","` | — |
| [SRC-4FFD5AFC54-L000340](../../scripts/run_answer_quality_benchmark.py#L340) | 340 | `"    \"category\","` | — |
| [SRC-4FFD5AFC54-L000341](../../scripts/run_answer_quality_benchmark.py#L341) | 341 | `"    \"language\","` | — |
| [SRC-4FFD5AFC54-L000342](../../scripts/run_answer_quality_benchmark.py#L342) | 342 | `"    \"question\","` | — |
| [SRC-4FFD5AFC54-L000343](../../scripts/run_answer_quality_benchmark.py#L343) | 343 | `"    \"expected_strategy\","` | — |
| [SRC-4FFD5AFC54-L000344](../../scripts/run_answer_quality_benchmark.py#L344) | 344 | `"    \"required_behaviors\","` | — |
| [SRC-4FFD5AFC54-L000345](../../scripts/run_answer_quality_benchmark.py#L345) | 345 | `"    \"forbidden_behaviors\","` | — |
| [SRC-4FFD5AFC54-L000346](../../scripts/run_answer_quality_benchmark.py#L346) | 346 | `"    \"evidence_fixture\","` | — |
| [SRC-4FFD5AFC54-L000347](../../scripts/run_answer_quality_benchmark.py#L347) | 347 | `"    \"failure_conditions\","` | — |
| [SRC-4FFD5AFC54-L000348](../../scripts/run_answer_quality_benchmark.py#L348) | 348 | `"    \"evaluation_mode\","` | — |
| [SRC-4FFD5AFC54-L000349](../../scripts/run_answer_quality_benchmark.py#L349) | 349 | `"}"` | — |
| [SRC-4FFD5AFC54-L000350](../../scripts/run_answer_quality_benchmark.py#L350) | 350 | `"ALLOWED_STRATEGIES = {\"local\", \"model_no_search\", \"web_search\", \"clarify\"}"` | — |
| [SRC-4FFD5AFC54-L000351](../../scripts/run_answer_quality_benchmark.py#L351) | 351 | `"ALLOWED_EVAL_MODES = {\"deterministic_structure\", \"fixture_assisted\", \"human_judgment\"}"` | — |
| [SRC-4FFD5AFC54-L000352](../../scripts/run_answer_quality_benchmark.py#L352) | 352 | `""` | — |
| [SRC-4FFD5AFC54-L000353](../../scripts/run_answer_quality_benchmark.py#L353) | 353 | `""` | — |
| [SRC-4FFD5AFC54-L000354](../../scripts/run_answer_quality_benchmark.py#L354) | 354 | `"def _utc_now() -> str:"` | — |
| [SRC-4FFD5AFC54-L000355](../../scripts/run_answer_quality_benchmark.py#L355) | 355 | `"    return datetime.now(UTC).isoformat(timespec=\"seconds\")"` | — |
| [SRC-4FFD5AFC54-L000356](../../scripts/run_answer_quality_benchmark.py#L356) | 356 | `""` | — |
| [SRC-4FFD5AFC54-L000357](../../scripts/run_answer_quality_benchmark.py#L357) | 357 | `""` | — |
| [SRC-4FFD5AFC54-L000358](../../scripts/run_answer_quality_benchmark.py#L358) | 358 | `"def load_corpus(path: Path) -> dict:"` | — |
| [SRC-4FFD5AFC54-L000359](../../scripts/run_answer_quality_benchmark.py#L359) | 359 | `"    if not path.is_file():"` | — |
| [SRC-4FFD5AFC54-L000360](../../scripts/run_answer_quality_benchmark.py#L360) | 360 | `"        raise FileNotFoundError(f\"Corpus not found: {path}\")"` | — |
| [SRC-4FFD5AFC54-L000361](../../scripts/run_answer_quality_benchmark.py#L361) | 361 | `"    data = json.loads(path.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-4FFD5AFC54-L000362](../../scripts/run_answer_quality_benchmark.py#L362) | 362 | `"    if not isinstance(data, dict) or not isinstance(data.get(\"cases\"), list):"` | — |
| [SRC-4FFD5AFC54-L000363](../../scripts/run_answer_quality_benchmark.py#L363) | 363 | `"        raise TypeError(\"Corpus root must be an object with a cases array\")"` | — |
| [SRC-4FFD5AFC54-L000364](../../scripts/run_answer_quality_benchmark.py#L364) | 364 | `"    if data.get(\"parts\"):"` | — |
| [SRC-4FFD5AFC54-L000365](../../scripts/run_answer_quality_benchmark.py#L365) | 365 | `"        raise ValueError(\"Incomplete shard index is not accepted; use merged cases[] corpus\")"` | — |
| [SRC-4FFD5AFC54-L000366](../../scripts/run_answer_quality_benchmark.py#L366) | 366 | `"    return data"` | — |
| [SRC-4FFD5AFC54-L000367](../../scripts/run_answer_quality_benchmark.py#L367) | 367 | `""` | — |
| [SRC-4FFD5AFC54-L000368](../../scripts/run_answer_quality_benchmark.py#L368) | 368 | `""` | — |
| [SRC-4FFD5AFC54-L000369](../../scripts/run_answer_quality_benchmark.py#L369) | 369 | `"def validate_corpus(data: dict) -> list[str]:"` | — |
| [SRC-4FFD5AFC54-L000370](../../scripts/run_answer_quality_benchmark.py#L370) | 370 | `"    \"\"\"Return a list of human-readable problems (empty => OK).\"\"\""` | — |
| [SRC-4FFD5AFC54-L000371](../../scripts/run_answer_quality_benchmark.py#L371) | 371 | `"    problems: list[str] = []"` | — |
| [SRC-4FFD5AFC54-L000372](../../scripts/run_answer_quality_benchmark.py#L372) | 372 | `"    cases = data.get(\"cases\") or []"` | — |
| [SRC-4FFD5AFC54-L000373](../../scripts/run_answer_quality_benchmark.py#L373) | 373 | `"    if data.get(\"case_count\") != len(cases):"` | — |
| [SRC-4FFD5AFC54-L000374](../../scripts/run_answer_quality_benchmark.py#L374) | 374 | `"        problems.append("` | — |
| [SRC-4FFD5AFC54-L000375](../../scripts/run_answer_quality_benchmark.py#L375) | 375 | `"            f\"case_count metadata {data.get('case_count')!r} != len(cases) {len(cases)}\""` | — |
| [SRC-4FFD5AFC54-L000376](../../scripts/run_answer_quality_benchmark.py#L376) | 376 | `"        )"` | — |
| [SRC-4FFD5AFC54-L000377](../../scripts/run_answer_quality_benchmark.py#L377) | 377 | `"    if len(cases) < 40:"` | — |
| [SRC-4FFD5AFC54-L000378](../../scripts/run_answer_quality_benchmark.py#L378) | 378 | `"        problems.append(f\"expected at least 40 cases, found {len(cases)}\")"` | — |
| [SRC-4FFD5AFC54-L000379](../../scripts/run_answer_quality_benchmark.py#L379) | 379 | `"    ids: list[str] = []"` | — |
| [SRC-4FFD5AFC54-L000380](../../scripts/run_answer_quality_benchmark.py#L380) | 380 | `"    for i, case in enumerate(cases):"` | — |
| [SRC-4FFD5AFC54-L000381](../../scripts/run_answer_quality_benchmark.py#L381) | 381 | `"        if not isinstance(case, dict):"` | — |
| [SRC-4FFD5AFC54-L000382](../../scripts/run_answer_quality_benchmark.py#L382) | 382 | `"            problems.append(f\"cases[{i}] is not an object\")"` | — |
| [SRC-4FFD5AFC54-L000383](../../scripts/run_answer_quality_benchmark.py#L383) | 383 | `"            continue"` | — |
| [SRC-4FFD5AFC54-L000384](../../scripts/run_answer_quality_benchmark.py#L384) | 384 | `"        missing = REQUIRED_FIELDS - set(case)"` | — |
| [SRC-4FFD5AFC54-L000385](../../scripts/run_answer_quality_benchmark.py#L385) | 385 | `"        if missing:"` | — |
| [SRC-4FFD5AFC54-L000386](../../scripts/run_answer_quality_benchmark.py#L386) | 386 | `"            problems.append(f\"{case.get('case_id', i)}: missing {sorted(missing)}\")"` | — |
| [SRC-4FFD5AFC54-L000387](../../scripts/run_answer_quality_benchmark.py#L387) | 387 | `"        cid = case.get(\"case_id\")"` | — |
| [SRC-4FFD5AFC54-L000388](../../scripts/run_answer_quality_benchmark.py#L388) | 388 | `"        if isinstance(cid, str):"` | — |
| [SRC-4FFD5AFC54-L000389](../../scripts/run_answer_quality_benchmark.py#L389) | 389 | `"            ids.append(cid)"` | — |
| [SRC-4FFD5AFC54-L000390](../../scripts/run_answer_quality_benchmark.py#L390) | 390 | `"        if case.get(\"expected_strategy\") not in ALLOWED_STRATEGIES:"` | — |
| [SRC-4FFD5AFC54-L000391](../../scripts/run_answer_quality_benchmark.py#L391) | 391 | `"            problems.append(f\"{cid}: bad strategy {case.get('expected_strategy')!r}\")"` | — |
| [SRC-4FFD5AFC54-L000392](../../scripts/run_answer_quality_benchmark.py#L392) | 392 | `"        if case.get(\"evaluation_mode\") not in ALLOWED_EVAL_MODES:"` | — |
| [SRC-4FFD5AFC54-L000393](../../scripts/run_answer_quality_benchmark.py#L393) | 393 | `"            problems.append(f\"{cid}: bad evaluation_mode {case.get('evaluation_mode')!r}\")"` | — |
| [SRC-4FFD5AFC54-L000394](../../scripts/run_answer_quality_benchmark.py#L394) | 394 | `"        q = case.get(\"question\")"` | — |
| [SRC-4FFD5AFC54-L000395](../../scripts/run_answer_quality_benchmark.py#L395) | 395 | `"        if not isinstance(q, str) or len(q.strip()) < 2:"` | — |
| [SRC-4FFD5AFC54-L000396](../../scripts/run_answer_quality_benchmark.py#L396) | 396 | `"            problems.append(f\"{cid}: empty question\")"` | — |
| [SRC-4FFD5AFC54-L000397](../../scripts/run_answer_quality_benchmark.py#L397) | 397 | `"    if len(ids) != len(set(ids)):"` | — |
| [SRC-4FFD5AFC54-L000398](../../scripts/run_answer_quality_benchmark.py#L398) | 398 | `"        problems.append(\"duplicate case_id values\")"` | — |
| [SRC-4FFD5AFC54-L000399](../../scripts/run_answer_quality_benchmark.py#L399) | 399 | `"    return problems"` | — |
| [SRC-4FFD5AFC54-L000400](../../scripts/run_answer_quality_benchmark.py#L400) | 400 | `""` | — |
| [SRC-4FFD5AFC54-L000401](../../scripts/run_answer_quality_benchmark.py#L401) | 401 | `""` | — |
| [SRC-4FFD5AFC54-L000402](../../scripts/run_answer_quality_benchmark.py#L402) | 402 | `"def redact_secrets(text: str) -> str:"` | — |
| [SRC-4FFD5AFC54-L000403](../../scripts/run_answer_quality_benchmark.py#L403) | 403 | `"    \"\"\"Best-effort redaction of common secret patterns from stored outputs.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000404](../../scripts/run_answer_quality_benchmark.py#L404) | 404 | `"    if not text:"` | — |
| [SRC-4FFD5AFC54-L000405](../../scripts/run_answer_quality_benchmark.py#L405) | 405 | `"        return text"` | — |
| [SRC-4FFD5AFC54-L000406](../../scripts/run_answer_quality_benchmark.py#L406) | 406 | `"    out = text"` | — |
| [SRC-4FFD5AFC54-L000407](../../scripts/run_answer_quality_benchmark.py#L407) | 407 | `"    for key in ("` | — |
| [SRC-4FFD5AFC54-L000408](../../scripts/run_answer_quality_benchmark.py#L408) | 408 | `"        \"OPENROUTER_API_KEY\","` | — |
| [SRC-4FFD5AFC54-L000409](../../scripts/run_answer_quality_benchmark.py#L409) | 409 | `"        \"OMARAI_ACCESS_TOKEN\","` | — |
| [SRC-4FFD5AFC54-L000410](../../scripts/run_answer_quality_benchmark.py#L410) | 410 | `"        \"OMARAI_LLM_API_KEY\","` | — |
| [SRC-4FFD5AFC54-L000411](../../scripts/run_answer_quality_benchmark.py#L411) | 411 | `"        \"Authorization\","` | — |
| [SRC-4FFD5AFC54-L000412](../../scripts/run_answer_quality_benchmark.py#L412) | 412 | `"        \"Bearer \","` | — |
| [SRC-4FFD5AFC54-L000413](../../scripts/run_answer_quality_benchmark.py#L413) | 413 | `"    ):"` | — |
| [SRC-4FFD5AFC54-L000414](../../scripts/run_answer_quality_benchmark.py#L414) | 414 | `"        out = out.replace(key, f\"[REDACTED:{key.strip()}]\")"` | — |
| [SRC-4FFD5AFC54-L000415](../../scripts/run_answer_quality_benchmark.py#L415) | 415 | `"    token = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-4FFD5AFC54-L000416](../../scripts/run_answer_quality_benchmark.py#L416) | 416 | `"    if token and token in out:"` | — |
| [SRC-4FFD5AFC54-L000417](../../scripts/run_answer_quality_benchmark.py#L417) | 417 | `"        out = out.replace(token, \"[REDACTED:OMARAI_ACCESS_TOKEN]\")"` | — |
| [SRC-4FFD5AFC54-L000418](../../scripts/run_answer_quality_benchmark.py#L418) | 418 | `"    for env_name in (\"OPENROUTER_API_KEY\", \"OMARAI_LLM_API_KEY\"):"` | — |
| [SRC-4FFD5AFC54-L000419](../../scripts/run_answer_quality_benchmark.py#L419) | 419 | `"        val = os.getenv(env_name, \"\").strip()"` | — |
| [SRC-4FFD5AFC54-L000420](../../scripts/run_answer_quality_benchmark.py#L420) | 420 | `"        if val and val in out:"` | — |
| [SRC-4FFD5AFC54-L000421](../../scripts/run_answer_quality_benchmark.py#L421) | 421 | `"            out = out.replace(val, f\"[REDACTED:{env_name}]\")"` | — |
| [SRC-4FFD5AFC54-L000422](../../scripts/run_answer_quality_benchmark.py#L422) | 422 | `"    return out"` | — |
| [SRC-4FFD5AFC54-L000423](../../scripts/run_answer_quality_benchmark.py#L423) | 423 | `""` | — |
| [SRC-4FFD5AFC54-L000424](../../scripts/run_answer_quality_benchmark.py#L424) | 424 | `""` | — |
| [SRC-4FFD5AFC54-L000425](../../scripts/run_answer_quality_benchmark.py#L425) | 425 | `"def post_agent("` | — |
| [SRC-4FFD5AFC54-L000426](../../scripts/run_answer_quality_benchmark.py#L426) | 426 | `"    base_url: str,"` | — |
| [SRC-4FFD5AFC54-L000427](../../scripts/run_answer_quality_benchmark.py#L427) | 427 | `"    question: str,"` | — |
| [SRC-4FFD5AFC54-L000428](../../scripts/run_answer_quality_benchmark.py#L428) | 428 | `"    timeout: float,"` | — |
| [SRC-4FFD5AFC54-L000429](../../scripts/run_answer_quality_benchmark.py#L429) | 429 | `"    token: str \| None,"` | — |
| [SRC-4FFD5AFC54-L000430](../../scripts/run_answer_quality_benchmark.py#L430) | 430 | `") -> tuple[int, dict \| str]:"` | — |
| [SRC-4FFD5AFC54-L000431](../../scripts/run_answer_quality_benchmark.py#L431) | 431 | `"    origin = validate_base_url(base_url, token_present=bool(token))"` | — |
| [SRC-4FFD5AFC54-L000432](../../scripts/run_answer_quality_benchmark.py#L432) | 432 | `"    url = origin + \"/api/agent\""` | — |
| [SRC-4FFD5AFC54-L000433](../../scripts/run_answer_quality_benchmark.py#L433) | 433 | `"    body = json.dumps({\"question\": question, \"history\": []}, ensure_ascii=False).encode(\"utf-8\")"` | — |
| [SRC-4FFD5AFC54-L000434](../../scripts/run_answer_quality_benchmark.py#L434) | 434 | `"    headers = {\"Content-Type\": \"application/json\", \"Content-Length\": str(len(body))}"` | — |
| [SRC-4FFD5AFC54-L000435](../../scripts/run_answer_quality_benchmark.py#L435) | 435 | `"    if token:"` | — |
| [SRC-4FFD5AFC54-L000436](../../scripts/run_answer_quality_benchmark.py#L436) | 436 | `"        headers[\"Authorization\"] = \"Bearer \" + token"` | — |
| [SRC-4FFD5AFC54-L000437](../../scripts/run_answer_quality_benchmark.py#L437) | 437 | `"    req = urllib.request.Request(url, data=body, headers=headers, method=\"POST\")"` | — |
| [SRC-4FFD5AFC54-L000438](../../scripts/run_answer_quality_benchmark.py#L438) | 438 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000439](../../scripts/run_answer_quality_benchmark.py#L439) | 439 | `"        with _NO_REDIRECT_OPENER.open(req, timeout=timeout) as resp:"` | — |
| [SRC-4FFD5AFC54-L000440](../../scripts/run_answer_quality_benchmark.py#L440) | 440 | `"            raw_bytes = resp.read(MAX_RESPONSE_BYTES + 1)"` | — |
| [SRC-4FFD5AFC54-L000441](../../scripts/run_answer_quality_benchmark.py#L441) | 441 | `"            if len(raw_bytes) > MAX_RESPONSE_BYTES:"` | — |
| [SRC-4FFD5AFC54-L000442](../../scripts/run_answer_quality_benchmark.py#L442) | 442 | `"                return 0, {\"error\": \"ResponseTooLarge\", \"detail\": \"Response exceeded the 2 MB limit.\"}"` | — |
| [SRC-4FFD5AFC54-L000443](../../scripts/run_answer_quality_benchmark.py#L443) | 443 | `"            raw = raw_bytes.decode(\"utf-8\", errors=\"replace\")"` | — |
| [SRC-4FFD5AFC54-L000444](../../scripts/run_answer_quality_benchmark.py#L444) | 444 | `"            status = getattr(resp, \"status\", 200)"` | — |
| [SRC-4FFD5AFC54-L000445](../../scripts/run_answer_quality_benchmark.py#L445) | 445 | `"            try:"` | — |
| [SRC-4FFD5AFC54-L000446](../../scripts/run_answer_quality_benchmark.py#L446) | 446 | `"                return status, json.loads(raw)"` | — |
| [SRC-4FFD5AFC54-L000447](../../scripts/run_answer_quality_benchmark.py#L447) | 447 | `"            except json.JSONDecodeError:"` | — |
| [SRC-4FFD5AFC54-L000448](../../scripts/run_answer_quality_benchmark.py#L448) | 448 | `"                return status, raw"` | — |
| [SRC-4FFD5AFC54-L000449](../../scripts/run_answer_quality_benchmark.py#L449) | 449 | `"    except urllib.error.HTTPError as exc:"` | — |
| [SRC-4FFD5AFC54-L000450](../../scripts/run_answer_quality_benchmark.py#L450) | 450 | `"        raw_bytes = exc.read(MAX_RESPONSE_BYTES + 1)"` | — |
| [SRC-4FFD5AFC54-L000451](../../scripts/run_answer_quality_benchmark.py#L451) | 451 | `"        if len(raw_bytes) > MAX_RESPONSE_BYTES:"` | — |
| [SRC-4FFD5AFC54-L000452](../../scripts/run_answer_quality_benchmark.py#L452) | 452 | `"            return exc.code, {\"error\": \"ResponseTooLarge\", \"detail\": \"Response exceeded the 2 MB limit.\"}"` | — |
| [SRC-4FFD5AFC54-L000453](../../scripts/run_answer_quality_benchmark.py#L453) | 453 | `"        raw = raw_bytes.decode(\"utf-8\", errors=\"replace\")"` | — |
| [SRC-4FFD5AFC54-L000454](../../scripts/run_answer_quality_benchmark.py#L454) | 454 | `"        try:"` | — |
| [SRC-4FFD5AFC54-L000455](../../scripts/run_answer_quality_benchmark.py#L455) | 455 | `"            return exc.code, json.loads(raw)"` | — |
| [SRC-4FFD5AFC54-L000456](../../scripts/run_answer_quality_benchmark.py#L456) | 456 | `"        except json.JSONDecodeError:"` | — |
| [SRC-4FFD5AFC54-L000457](../../scripts/run_answer_quality_benchmark.py#L457) | 457 | `"            return exc.code, raw"` | — |
| [SRC-4FFD5AFC54-L000458](../../scripts/run_answer_quality_benchmark.py#L458) | 458 | `"    except ValueError as exc:"` | — |
| [SRC-4FFD5AFC54-L000459](../../scripts/run_answer_quality_benchmark.py#L459) | 459 | `"        return 0, {\"error\": \"UnsafeBaseURL\", \"detail\": str(exc)}"` | — |
| [SRC-4FFD5AFC54-L000460](../../scripts/run_answer_quality_benchmark.py#L460) | 460 | `"    except (urllib.error.URLError, TimeoutError, OSError) as exc:"` | — |
| [SRC-4FFD5AFC54-L000461](../../scripts/run_answer_quality_benchmark.py#L461) | 461 | `"        return 0, {\"error\": type(exc).__name__, \"detail\": str(exc)}"` | — |
| [SRC-4FFD5AFC54-L000462](../../scripts/run_answer_quality_benchmark.py#L462) | 462 | `""` | — |
| [SRC-4FFD5AFC54-L000463](../../scripts/run_answer_quality_benchmark.py#L463) | 463 | `""` | — |
| [SRC-4FFD5AFC54-L000464](../../scripts/run_answer_quality_benchmark.py#L464) | 464 | `"def get_verified_build_sha(base_url: str, timeout: float, token: str \| None = None) -> str:"` | — |
| [SRC-4FFD5AFC54-L000465](../../scripts/run_answer_quality_benchmark.py#L465) | 465 | `"    \"\"\"Read the deployed build identity from /api/health; never trust a caller-only SHA.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000466](../../scripts/run_answer_quality_benchmark.py#L466) | 466 | `"    origin = validate_base_url(base_url, token_present=bool(token))"` | — |
| [SRC-4FFD5AFC54-L000467](../../scripts/run_answer_quality_benchmark.py#L467) | 467 | `"    request = urllib.request.Request("` | — |
| [SRC-4FFD5AFC54-L000468](../../scripts/run_answer_quality_benchmark.py#L468) | 468 | `"        origin + \"/api/health\","` | — |
| [SRC-4FFD5AFC54-L000469](../../scripts/run_answer_quality_benchmark.py#L469) | 469 | `"        headers={\"Accept\": \"application/json\"},"` | — |
| [SRC-4FFD5AFC54-L000470](../../scripts/run_answer_quality_benchmark.py#L470) | 470 | `"        method=\"GET\","` | — |
| [SRC-4FFD5AFC54-L000471](../../scripts/run_answer_quality_benchmark.py#L471) | 471 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000472](../../scripts/run_answer_quality_benchmark.py#L472) | 472 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000473](../../scripts/run_answer_quality_benchmark.py#L473) | 473 | `"        with _NO_REDIRECT_OPENER.open(request, timeout=timeout) as response:"` | — |
| [SRC-4FFD5AFC54-L000474](../../scripts/run_answer_quality_benchmark.py#L474) | 474 | `"            raw = response.read(64_001)"` | — |
| [SRC-4FFD5AFC54-L000475](../../scripts/run_answer_quality_benchmark.py#L475) | 475 | `"            if len(raw) > 64_000:"` | — |
| [SRC-4FFD5AFC54-L000476](../../scripts/run_answer_quality_benchmark.py#L476) | 476 | `"                raise ValueError(\"/api/health response exceeded the 64 KB limit\")"` | — |
| [SRC-4FFD5AFC54-L000477](../../scripts/run_answer_quality_benchmark.py#L477) | 477 | `"            status = getattr(response, \"status\", 200)"` | — |
| [SRC-4FFD5AFC54-L000478](../../scripts/run_answer_quality_benchmark.py#L478) | 478 | `"            if not 200 <= status < 300:"` | — |
| [SRC-4FFD5AFC54-L000479](../../scripts/run_answer_quality_benchmark.py#L479) | 479 | `"                raise ValueError(f\"/api/health returned HTTP {status}\")"` | — |
| [SRC-4FFD5AFC54-L000480](../../scripts/run_answer_quality_benchmark.py#L480) | 480 | `"    except urllib.error.HTTPError as exc:"` | — |
| [SRC-4FFD5AFC54-L000481](../../scripts/run_answer_quality_benchmark.py#L481) | 481 | `"        raise ValueError(f\"/api/health returned HTTP {exc.code}\") from exc"` | — |
| [SRC-4FFD5AFC54-L000482](../../scripts/run_answer_quality_benchmark.py#L482) | 482 | `"    except (urllib.error.URLError, TimeoutError, OSError) as exc:"` | — |
| [SRC-4FFD5AFC54-L000483](../../scripts/run_answer_quality_benchmark.py#L483) | 483 | `"        raise ValueError(f\"/api/health request failed: {type(exc).__name__}\") from exc"` | — |
| [SRC-4FFD5AFC54-L000484](../../scripts/run_answer_quality_benchmark.py#L484) | 484 | `""` | — |
| [SRC-4FFD5AFC54-L000485](../../scripts/run_answer_quality_benchmark.py#L485) | 485 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000486](../../scripts/run_answer_quality_benchmark.py#L486) | 486 | `"        payload = json.loads(raw.decode(\"utf-8\"))"` | — |
| [SRC-4FFD5AFC54-L000487](../../scripts/run_answer_quality_benchmark.py#L487) | 487 | `"    except (UnicodeDecodeError, json.JSONDecodeError) as exc:"` | — |
| [SRC-4FFD5AFC54-L000488](../../scripts/run_answer_quality_benchmark.py#L488) | 488 | `"        raise ValueError(\"/api/health did not return valid JSON\") from exc"` | — |
| [SRC-4FFD5AFC54-L000489](../../scripts/run_answer_quality_benchmark.py#L489) | 489 | `"    if not isinstance(payload, dict) or payload.get(\"ok\") is not True:"` | — |
| [SRC-4FFD5AFC54-L000490](../../scripts/run_answer_quality_benchmark.py#L490) | 490 | `"        raise ValueError(\"/api/health did not report ok=true\")"` | — |
| [SRC-4FFD5AFC54-L000491](../../scripts/run_answer_quality_benchmark.py#L491) | 491 | `"    build = payload.get(\"build\")"` | — |
| [SRC-4FFD5AFC54-L000492](../../scripts/run_answer_quality_benchmark.py#L492) | 492 | `"    sha = build.get(\"sha\") if isinstance(build, dict) else None"` | — |
| [SRC-4FFD5AFC54-L000493](../../scripts/run_answer_quality_benchmark.py#L493) | 493 | `"    if not isinstance(sha, str) or not re.fullmatch(r\"[0-9a-fA-F]{40}\", sha):"` | — |
| [SRC-4FFD5AFC54-L000494](../../scripts/run_answer_quality_benchmark.py#L494) | 494 | `"        raise ValueError(\"/api/health build.sha is missing or not a full 40-character SHA\")"` | — |
| [SRC-4FFD5AFC54-L000495](../../scripts/run_answer_quality_benchmark.py#L495) | 495 | `"    return sha.lower()"` | — |
| [SRC-4FFD5AFC54-L000496](../../scripts/run_answer_quality_benchmark.py#L496) | 496 | `""` | — |
| [SRC-4FFD5AFC54-L000497](../../scripts/run_answer_quality_benchmark.py#L497) | 497 | `""` | — |
| [SRC-4FFD5AFC54-L000498](../../scripts/run_answer_quality_benchmark.py#L498) | 498 | `"def run_validate(corpus_path: Path, summary: bool) -> int:"` | — |
| [SRC-4FFD5AFC54-L000499](../../scripts/run_answer_quality_benchmark.py#L499) | 499 | `"    data = load_corpus(corpus_path)"` | — |
| [SRC-4FFD5AFC54-L000500](../../scripts/run_answer_quality_benchmark.py#L500) | 500 | `"    problems = validate_corpus(data)"` | — |
| [SRC-4FFD5AFC54-L000501](../../scripts/run_answer_quality_benchmark.py#L501) | 501 | `"    if problems:"` | — |
| [SRC-4FFD5AFC54-L000502](../../scripts/run_answer_quality_benchmark.py#L502) | 502 | `"        print(\"VALIDATE FAIL\")"` | — |
| [SRC-4FFD5AFC54-L000503](../../scripts/run_answer_quality_benchmark.py#L503) | 503 | `"        for p in problems:"` | — |
| [SRC-4FFD5AFC54-L000504](../../scripts/run_answer_quality_benchmark.py#L504) | 504 | `"            print(\" -\", p)"` | — |
| [SRC-4FFD5AFC54-L000505](../../scripts/run_answer_quality_benchmark.py#L505) | 505 | `"        return 1"` | — |
| [SRC-4FFD5AFC54-L000506](../../scripts/run_answer_quality_benchmark.py#L506) | 506 | `"    cases = data[\"cases\"]"` | — |
| [SRC-4FFD5AFC54-L000507](../../scripts/run_answer_quality_benchmark.py#L507) | 507 | `"    cats = sorted({c[\"category\"] for c in cases})"` | — |
| [SRC-4FFD5AFC54-L000508](../../scripts/run_answer_quality_benchmark.py#L508) | 508 | `"    langs = sorted({c[\"language\"] for c in cases})"` | — |
| [SRC-4FFD5AFC54-L000509](../../scripts/run_answer_quality_benchmark.py#L509) | 509 | `"    print(\"VALIDATE OK\")"` | — |
| [SRC-4FFD5AFC54-L000510](../../scripts/run_answer_quality_benchmark.py#L510) | 510 | `"    print(f\"benchmark_id={data.get('benchmark_id')} version={data.get('version')}\")"` | — |
| [SRC-4FFD5AFC54-L000511](../../scripts/run_answer_quality_benchmark.py#L511) | 511 | `"    print(f\"cases={len(cases)} categories={len(cats)} languages={langs}\")"` | — |
| [SRC-4FFD5AFC54-L000512](../../scripts/run_answer_quality_benchmark.py#L512) | 512 | `"    if summary:"` | — |
| [SRC-4FFD5AFC54-L000513](../../scripts/run_answer_quality_benchmark.py#L513) | 513 | `"        from collections import Counter"` | — |
| [SRC-4FFD5AFC54-L000514](../../scripts/run_answer_quality_benchmark.py#L514) | 514 | `""` | — |
| [SRC-4FFD5AFC54-L000515](../../scripts/run_answer_quality_benchmark.py#L515) | 515 | `"        print(\"strategies:\", dict(Counter(c[\"expected_strategy\"] for c in cases)))"` | — |
| [SRC-4FFD5AFC54-L000516](../../scripts/run_answer_quality_benchmark.py#L516) | 516 | `"        print(\"eval_modes:\", dict(Counter(c[\"evaluation_mode\"] for c in cases)))"` | — |
| [SRC-4FFD5AFC54-L000517](../../scripts/run_answer_quality_benchmark.py#L517) | 517 | `"        print(\"categories:\", \", \".join(cats))"` | — |
| [SRC-4FFD5AFC54-L000518](../../scripts/run_answer_quality_benchmark.py#L518) | 518 | `"    print("` | — |
| [SRC-4FFD5AFC54-L000519](../../scripts/run_answer_quality_benchmark.py#L519) | 519 | `"        \"NOTE: Structural validation is not answer-quality evaluation. \""` | — |
| [SRC-4FFD5AFC54-L000520](../../scripts/run_answer_quality_benchmark.py#L520) | 520 | `"        \"All reasoning cases remain NOT_TESTED until reviewed.\""` | — |
| [SRC-4FFD5AFC54-L000521](../../scripts/run_answer_quality_benchmark.py#L521) | 521 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000522](../../scripts/run_answer_quality_benchmark.py#L522) | 522 | `"    return 0"` | — |
| [SRC-4FFD5AFC54-L000523](../../scripts/run_answer_quality_benchmark.py#L523) | 523 | `""` | — |
| [SRC-4FFD5AFC54-L000524](../../scripts/run_answer_quality_benchmark.py#L524) | 524 | `""` | — |
| [SRC-4FFD5AFC54-L000525](../../scripts/run_answer_quality_benchmark.py#L525) | 525 | `"def run_live("` | — |
| [SRC-4FFD5AFC54-L000526](../../scripts/run_answer_quality_benchmark.py#L526) | 526 | `"    corpus_path: Path,"` | — |
| [SRC-4FFD5AFC54-L000527](../../scripts/run_answer_quality_benchmark.py#L527) | 527 | `"    base_url: str,"` | — |
| [SRC-4FFD5AFC54-L000528](../../scripts/run_answer_quality_benchmark.py#L528) | 528 | `"    case_id: str \| None,"` | — |
| [SRC-4FFD5AFC54-L000529](../../scripts/run_answer_quality_benchmark.py#L529) | 529 | `"    limit: int,"` | — |
| [SRC-4FFD5AFC54-L000530](../../scripts/run_answer_quality_benchmark.py#L530) | 530 | `"    timeout: float,"` | — |
| [SRC-4FFD5AFC54-L000531](../../scripts/run_answer_quality_benchmark.py#L531) | 531 | `"    delay: float,"` | — |
| [SRC-4FFD5AFC54-L000532](../../scripts/run_answer_quality_benchmark.py#L532) | 532 | `"    out_path: Path \| None,"` | — |
| [SRC-4FFD5AFC54-L000533](../../scripts/run_answer_quality_benchmark.py#L533) | 533 | `"    build_sha: str \| None = None,"` | — |
| [SRC-4FFD5AFC54-L000534](../../scripts/run_answer_quality_benchmark.py#L534) | 534 | `"    request_costs_path: Path \| None = None,"` | — |
| [SRC-4FFD5AFC54-L000535](../../scripts/run_answer_quality_benchmark.py#L535) | 535 | `") -> int:"` | — |
| [SRC-4FFD5AFC54-L000536](../../scripts/run_answer_quality_benchmark.py#L536) | 536 | `"    data = load_corpus(corpus_path)"` | — |
| [SRC-4FFD5AFC54-L000537](../../scripts/run_answer_quality_benchmark.py#L537) | 537 | `"    problems = validate_corpus(data)"` | — |
| [SRC-4FFD5AFC54-L000538](../../scripts/run_answer_quality_benchmark.py#L538) | 538 | `"    if problems:"` | — |
| [SRC-4FFD5AFC54-L000539](../../scripts/run_answer_quality_benchmark.py#L539) | 539 | `"        print(\"Corpus invalid; refusing live run:\")"` | — |
| [SRC-4FFD5AFC54-L000540](../../scripts/run_answer_quality_benchmark.py#L540) | 540 | `"        for p in problems:"` | — |
| [SRC-4FFD5AFC54-L000541](../../scripts/run_answer_quality_benchmark.py#L541) | 541 | `"            print(\" -\", p)"` | — |
| [SRC-4FFD5AFC54-L000542](../../scripts/run_answer_quality_benchmark.py#L542) | 542 | `"        return 2"` | — |
| [SRC-4FFD5AFC54-L000543](../../scripts/run_answer_quality_benchmark.py#L543) | 543 | `""` | — |
| [SRC-4FFD5AFC54-L000544](../../scripts/run_answer_quality_benchmark.py#L544) | 544 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000545](../../scripts/run_answer_quality_benchmark.py#L545) | 545 | `"        full_case_ids = {case.get(\"case_id\") for case in data.get(\"cases\", []) if isinstance(case, dict)}"` | — |
| [SRC-4FFD5AFC54-L000546](../../scripts/run_answer_quality_benchmark.py#L546) | 546 | `"        request_costs, request_cost_source = _load_request_cost_ledger(request_costs_path, full_case_ids)"` | — |
| [SRC-4FFD5AFC54-L000547](../../scripts/run_answer_quality_benchmark.py#L547) | 547 | `"    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:"` | — |
| [SRC-4FFD5AFC54-L000548](../../scripts/run_answer_quality_benchmark.py#L548) | 548 | `"        print(f\"Invalid request-cost ledger; refusing live run: {exc}\", file=sys.stderr)"` | — |
| [SRC-4FFD5AFC54-L000549](../../scripts/run_answer_quality_benchmark.py#L549) | 549 | `"        return 2"` | — |
| [SRC-4FFD5AFC54-L000550](../../scripts/run_answer_quality_benchmark.py#L550) | 550 | `""` | — |
| [SRC-4FFD5AFC54-L000551](../../scripts/run_answer_quality_benchmark.py#L551) | 551 | `"    token = os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip() or None"` | — |
| [SRC-4FFD5AFC54-L000552](../../scripts/run_answer_quality_benchmark.py#L552) | 552 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000553](../../scripts/run_answer_quality_benchmark.py#L553) | 553 | `"        safe_base_url = validate_base_url(base_url, token_present=bool(token))"` | — |
| [SRC-4FFD5AFC54-L000554](../../scripts/run_answer_quality_benchmark.py#L554) | 554 | `"    except ValueError as exc:"` | — |
| [SRC-4FFD5AFC54-L000555](../../scripts/run_answer_quality_benchmark.py#L555) | 555 | `"        print(f\"Unsafe base URL; refusing live run: {exc}\", file=sys.stderr)"` | — |
| [SRC-4FFD5AFC54-L000556](../../scripts/run_answer_quality_benchmark.py#L556) | 556 | `"        return 2"` | — |
| [SRC-4FFD5AFC54-L000557](../../scripts/run_answer_quality_benchmark.py#L557) | 557 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000558](../../scripts/run_answer_quality_benchmark.py#L558) | 558 | `"        verified_build_sha = get_verified_build_sha(safe_base_url, timeout, token)"` | — |
| [SRC-4FFD5AFC54-L000559](../../scripts/run_answer_quality_benchmark.py#L559) | 559 | `"    except ValueError as exc:"` | — |
| [SRC-4FFD5AFC54-L000560](../../scripts/run_answer_quality_benchmark.py#L560) | 560 | `"        print(f\"Unverified deployed build; refusing live run: {exc}\", file=sys.stderr)"` | — |
| [SRC-4FFD5AFC54-L000561](../../scripts/run_answer_quality_benchmark.py#L561) | 561 | `"        return 2"` | — |
| [SRC-4FFD5AFC54-L000562](../../scripts/run_answer_quality_benchmark.py#L562) | 562 | `"    expected_build_sha = build_sha.strip().lower() if isinstance(build_sha, str) else \"\""` | — |
| [SRC-4FFD5AFC54-L000563](../../scripts/run_answer_quality_benchmark.py#L563) | 563 | `"    if expected_build_sha and expected_build_sha != verified_build_sha:"` | — |
| [SRC-4FFD5AFC54-L000564](../../scripts/run_answer_quality_benchmark.py#L564) | 564 | `"        print("` | — |
| [SRC-4FFD5AFC54-L000565](../../scripts/run_answer_quality_benchmark.py#L565) | 565 | `"            \"Build SHA mismatch: --build-sha does not match /api/health build.sha; \""` | — |
| [SRC-4FFD5AFC54-L000566](../../scripts/run_answer_quality_benchmark.py#L566) | 566 | `"            \"refusing live requests.\","` | — |
| [SRC-4FFD5AFC54-L000567](../../scripts/run_answer_quality_benchmark.py#L567) | 567 | `"            file=sys.stderr,"` | — |
| [SRC-4FFD5AFC54-L000568](../../scripts/run_answer_quality_benchmark.py#L568) | 568 | `"        )"` | — |
| [SRC-4FFD5AFC54-L000569](../../scripts/run_answer_quality_benchmark.py#L569) | 569 | `"        return 2"` | — |
| [SRC-4FFD5AFC54-L000570](../../scripts/run_answer_quality_benchmark.py#L570) | 570 | `"    cases = data[\"cases\"]"` | — |
| [SRC-4FFD5AFC54-L000571](../../scripts/run_answer_quality_benchmark.py#L571) | 571 | `"    if case_id:"` | — |
| [SRC-4FFD5AFC54-L000572](../../scripts/run_answer_quality_benchmark.py#L572) | 572 | `"        cases = [c for c in cases if c[\"case_id\"] == case_id]"` | — |
| [SRC-4FFD5AFC54-L000573](../../scripts/run_answer_quality_benchmark.py#L573) | 573 | `"        if not cases:"` | — |
| [SRC-4FFD5AFC54-L000574](../../scripts/run_answer_quality_benchmark.py#L574) | 574 | `"            print(f\"Unknown case_id: {case_id}\", file=sys.stderr)"` | — |
| [SRC-4FFD5AFC54-L000575](../../scripts/run_answer_quality_benchmark.py#L575) | 575 | `"            return 2"` | — |
| [SRC-4FFD5AFC54-L000576](../../scripts/run_answer_quality_benchmark.py#L576) | 576 | `"    if limit > 0:"` | — |
| [SRC-4FFD5AFC54-L000577](../../scripts/run_answer_quality_benchmark.py#L577) | 577 | `"        cases = cases[:limit]"` | — |
| [SRC-4FFD5AFC54-L000578](../../scripts/run_answer_quality_benchmark.py#L578) | 578 | `""` | — |
| [SRC-4FFD5AFC54-L000579](../../scripts/run_answer_quality_benchmark.py#L579) | 579 | `"    results = []"` | — |
| [SRC-4FFD5AFC54-L000580](../../scripts/run_answer_quality_benchmark.py#L580) | 580 | `"    print("` | — |
| [SRC-4FFD5AFC54-L000581](../../scripts/run_answer_quality_benchmark.py#L581) | 581 | `"        \"LIVE mode: fixtures are NOT injected into the server. \""` | — |
| [SRC-4FFD5AFC54-L000582](../../scripts/run_answer_quality_benchmark.py#L582) | 582 | `"        \"Answers are recorded as NOT_TESTED (quality) unless transport fails.\""` | — |
| [SRC-4FFD5AFC54-L000583](../../scripts/run_answer_quality_benchmark.py#L583) | 583 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000584](../../scripts/run_answer_quality_benchmark.py#L584) | 584 | `"    for case in cases:"` | — |
| [SRC-4FFD5AFC54-L000585](../../scripts/run_answer_quality_benchmark.py#L585) | 585 | `"        cid = case[\"case_id\"]"` | — |
| [SRC-4FFD5AFC54-L000586](../../scripts/run_answer_quality_benchmark.py#L586) | 586 | `"        prompt = case[\"question\"]"` | — |
| [SRC-4FFD5AFC54-L000587](../../scripts/run_answer_quality_benchmark.py#L587) | 587 | `"        request_started = time.perf_counter()"` | — |
| [SRC-4FFD5AFC54-L000588](../../scripts/run_answer_quality_benchmark.py#L588) | 588 | `"        status_code, payload = post_agent(safe_base_url, prompt, timeout, token)"` | — |
| [SRC-4FFD5AFC54-L000589](../../scripts/run_answer_quality_benchmark.py#L589) | 589 | `"        elapsed_ms = round((time.perf_counter() - request_started) * 1000, 2)"` | — |
| [SRC-4FFD5AFC54-L000590](../../scripts/run_answer_quality_benchmark.py#L590) | 590 | `"        if isinstance(payload, dict):"` | — |
| [SRC-4FFD5AFC54-L000591](../../scripts/run_answer_quality_benchmark.py#L591) | 591 | `"            safe_payload = json.loads(redact_secrets(json.dumps(payload, ensure_ascii=False)))"` | — |
| [SRC-4FFD5AFC54-L000592](../../scripts/run_answer_quality_benchmark.py#L592) | 592 | `"        else:"` | — |
| [SRC-4FFD5AFC54-L000593](../../scripts/run_answer_quality_benchmark.py#L593) | 593 | `"            safe_payload = redact_secrets(str(payload))"` | — |
| [SRC-4FFD5AFC54-L000594](../../scripts/run_answer_quality_benchmark.py#L594) | 594 | `""` | — |
| [SRC-4FFD5AFC54-L000595](../../scripts/run_answer_quality_benchmark.py#L595) | 595 | `"        transport_ok = 200 <= status_code < 300"` | — |
| [SRC-4FFD5AFC54-L000596](../../scripts/run_answer_quality_benchmark.py#L596) | 596 | `"        response_metrics = _response_metrics(safe_payload, case[\"expected_strategy\"], transport_ok)"` | — |
| [SRC-4FFD5AFC54-L000597](../../scripts/run_answer_quality_benchmark.py#L597) | 597 | `"        if request_cost_source is not None:"` | — |
| [SRC-4FFD5AFC54-L000598](../../scripts/run_answer_quality_benchmark.py#L598) | 598 | `"            if cid in request_costs:"` | — |
| [SRC-4FFD5AFC54-L000599](../../scripts/run_answer_quality_benchmark.py#L599) | 599 | `"                response_metrics[\"request_cost_usd\"] = request_costs[cid]"` | — |
| [SRC-4FFD5AFC54-L000600](../../scripts/run_answer_quality_benchmark.py#L600) | 600 | `"                response_metrics[\"request_cost_status\"] = \"RECONCILED_COMPLETE_REQUEST_COST\""` | — |
| [SRC-4FFD5AFC54-L000601](../../scripts/run_answer_quality_benchmark.py#L601) | 601 | `"                response_metrics[\"request_cost_source\"] = request_cost_source"` | — |
| [SRC-4FFD5AFC54-L000602](../../scripts/run_answer_quality_benchmark.py#L602) | 602 | `"            else:"` | — |
| [SRC-4FFD5AFC54-L000603](../../scripts/run_answer_quality_benchmark.py#L603) | 603 | `"                response_metrics[\"request_cost_status\"] = \"PARTIAL_EXTERNAL_COST_RECONCILIATION\""` | — |
| [SRC-4FFD5AFC54-L000604](../../scripts/run_answer_quality_benchmark.py#L604) | 604 | `"                response_metrics[\"request_cost_source\"] = request_cost_source"` | — |
| [SRC-4FFD5AFC54-L000605](../../scripts/run_answer_quality_benchmark.py#L605) | 605 | `"        record = {"` | — |
| [SRC-4FFD5AFC54-L000606](../../scripts/run_answer_quality_benchmark.py#L606) | 606 | `"            \"case_id\": cid,"` | — |
| [SRC-4FFD5AFC54-L000607](../../scripts/run_answer_quality_benchmark.py#L607) | 607 | `"            \"benchmark_version\": data.get(\"version\"),"` | — |
| [SRC-4FFD5AFC54-L000608](../../scripts/run_answer_quality_benchmark.py#L608) | 608 | `"            \"benchmark_id\": data.get(\"benchmark_id\"),"` | — |
| [SRC-4FFD5AFC54-L000609](../../scripts/run_answer_quality_benchmark.py#L609) | 609 | `"            \"executed_at_utc\": _utc_now(),"` | — |
| [SRC-4FFD5AFC54-L000610](../../scripts/run_answer_quality_benchmark.py#L610) | 610 | `"            \"mode\": \"live_api\","` | — |
| [SRC-4FFD5AFC54-L000611](../../scripts/run_answer_quality_benchmark.py#L611) | 611 | `"            \"base_url\": safe_base_url,"` | — |
| [SRC-4FFD5AFC54-L000612](../../scripts/run_answer_quality_benchmark.py#L612) | 612 | `"            \"http_status\": status_code,"` | — |
| [SRC-4FFD5AFC54-L000613](../../scripts/run_answer_quality_benchmark.py#L613) | 613 | `"            \"elapsed_ms\": elapsed_ms,"` | — |
| [SRC-4FFD5AFC54-L000614](../../scripts/run_answer_quality_benchmark.py#L614) | 614 | `"            \"build_sha\": verified_build_sha,"` | — |
| [SRC-4FFD5AFC54-L000615](../../scripts/run_answer_quality_benchmark.py#L615) | 615 | `"            \"build_sha_verification\": \"confirmed_by_api_health\","` | — |
| [SRC-4FFD5AFC54-L000616](../../scripts/run_answer_quality_benchmark.py#L616) | 616 | `"            **response_metrics,"` | — |
| [SRC-4FFD5AFC54-L000617](../../scripts/run_answer_quality_benchmark.py#L617) | 617 | `"            \"prompt\": prompt,"` | — |
| [SRC-4FFD5AFC54-L000618](../../scripts/run_answer_quality_benchmark.py#L618) | 618 | `"            \"expected_strategy\": case[\"expected_strategy\"],"` | — |
| [SRC-4FFD5AFC54-L000619](../../scripts/run_answer_quality_benchmark.py#L619) | 619 | `"            \"category\": case[\"category\"],"` | — |
| [SRC-4FFD5AFC54-L000620](../../scripts/run_answer_quality_benchmark.py#L620) | 620 | `"            \"response\": safe_payload,"` | — |
| [SRC-4FFD5AFC54-L000621](../../scripts/run_answer_quality_benchmark.py#L621) | 621 | `"            \"used_web_search\": ("` | — |
| [SRC-4FFD5AFC54-L000622](../../scripts/run_answer_quality_benchmark.py#L622) | 622 | `"                safe_payload.get(\"used_web_search\") if isinstance(safe_payload, dict) else None"` | — |
| [SRC-4FFD5AFC54-L000623](../../scripts/run_answer_quality_benchmark.py#L623) | 623 | `"            ),"` | — |
| [SRC-4FFD5AFC54-L000624](../../scripts/run_answer_quality_benchmark.py#L624) | 624 | `"            \"used_language_model\": ("` | — |
| [SRC-4FFD5AFC54-L000625](../../scripts/run_answer_quality_benchmark.py#L625) | 625 | `"                safe_payload.get(\"used_language_model\")"` | — |
| [SRC-4FFD5AFC54-L000626](../../scripts/run_answer_quality_benchmark.py#L626) | 626 | `"                if isinstance(safe_payload, dict)"` | — |
| [SRC-4FFD5AFC54-L000627](../../scripts/run_answer_quality_benchmark.py#L627) | 627 | `"                else None"` | — |
| [SRC-4FFD5AFC54-L000628](../../scripts/run_answer_quality_benchmark.py#L628) | 628 | `"            ),"` | — |
| [SRC-4FFD5AFC54-L000629](../../scripts/run_answer_quality_benchmark.py#L629) | 629 | `"            \"sources\": ("` | — |
| [SRC-4FFD5AFC54-L000630](../../scripts/run_answer_quality_benchmark.py#L630) | 630 | `"                safe_payload.get(\"sources\") if isinstance(safe_payload, dict) else None"` | — |
| [SRC-4FFD5AFC54-L000631](../../scripts/run_answer_quality_benchmark.py#L631) | 631 | `"            ),"` | — |
| [SRC-4FFD5AFC54-L000632](../../scripts/run_answer_quality_benchmark.py#L632) | 632 | `"            \"status\": \"NOT_TESTED\","` | — |
| [SRC-4FFD5AFC54-L000633](../../scripts/run_answer_quality_benchmark.py#L633) | 633 | `"            \"transport_ok\": transport_ok,"` | — |
| [SRC-4FFD5AFC54-L000634](../../scripts/run_answer_quality_benchmark.py#L634) | 634 | `"            \"reviewer_notes\": ("` | — |
| [SRC-4FFD5AFC54-L000635](../../scripts/run_answer_quality_benchmark.py#L635) | 635 | `"                \"Response collected; human/fixture review required for PASS/FAIL.\""` | — |
| [SRC-4FFD5AFC54-L000636](../../scripts/run_answer_quality_benchmark.py#L636) | 636 | `"                if transport_ok"` | — |
| [SRC-4FFD5AFC54-L000637](../../scripts/run_answer_quality_benchmark.py#L637) | 637 | `"                else \"Transport or HTTP error; quality not graded.\""` | — |
| [SRC-4FFD5AFC54-L000638](../../scripts/run_answer_quality_benchmark.py#L638) | 638 | `"            ),"` | — |
| [SRC-4FFD5AFC54-L000639](../../scripts/run_answer_quality_benchmark.py#L639) | 639 | `"            \"evidence_fixture_injected\": False,"` | — |
| [SRC-4FFD5AFC54-L000640](../../scripts/run_answer_quality_benchmark.py#L640) | 640 | `"        }"` | — |
| [SRC-4FFD5AFC54-L000641](../../scripts/run_answer_quality_benchmark.py#L641) | 641 | `"        results.append(record)"` | — |
| [SRC-4FFD5AFC54-L000642](../../scripts/run_answer_quality_benchmark.py#L642) | 642 | `"        flag = \"OK\" if transport_ok else \"ERR\""` | — |
| [SRC-4FFD5AFC54-L000643](../../scripts/run_answer_quality_benchmark.py#L643) | 643 | `"        print(f\"[{flag}] {cid} http={status_code}\")"` | — |
| [SRC-4FFD5AFC54-L000644](../../scripts/run_answer_quality_benchmark.py#L644) | 644 | `"        if delay > 0:"` | — |
| [SRC-4FFD5AFC54-L000645](../../scripts/run_answer_quality_benchmark.py#L645) | 645 | `"            time.sleep(delay)"` | — |
| [SRC-4FFD5AFC54-L000646](../../scripts/run_answer_quality_benchmark.py#L646) | 646 | `""` | — |
| [SRC-4FFD5AFC54-L000647](../../scripts/run_answer_quality_benchmark.py#L647) | 647 | `"    envelope = {"` | — |
| [SRC-4FFD5AFC54-L000648](../../scripts/run_answer_quality_benchmark.py#L648) | 648 | `"        \"benchmark_id\": data.get(\"benchmark_id\"),"` | — |
| [SRC-4FFD5AFC54-L000649](../../scripts/run_answer_quality_benchmark.py#L649) | 649 | `"        \"benchmark_version\": data.get(\"version\"),"` | — |
| [SRC-4FFD5AFC54-L000650](../../scripts/run_answer_quality_benchmark.py#L650) | 650 | `"        \"mode\": \"live_api\","` | — |
| [SRC-4FFD5AFC54-L000651](../../scripts/run_answer_quality_benchmark.py#L651) | 651 | `"        \"build_sha\": verified_build_sha,"` | — |
| [SRC-4FFD5AFC54-L000652](../../scripts/run_answer_quality_benchmark.py#L652) | 652 | `"        \"build_sha_verification\": \"confirmed_by_api_health\","` | — |
| [SRC-4FFD5AFC54-L000653](../../scripts/run_answer_quality_benchmark.py#L653) | 653 | `"        \"expected_build_sha\": expected_build_sha or None,"` | — |
| [SRC-4FFD5AFC54-L000654](../../scripts/run_answer_quality_benchmark.py#L654) | 654 | `"        \"executed_at_utc\": _utc_now(),"` | — |
| [SRC-4FFD5AFC54-L000655](../../scripts/run_answer_quality_benchmark.py#L655) | 655 | `"        \"case_count\": len(results),"` | — |
| [SRC-4FFD5AFC54-L000656](../../scripts/run_answer_quality_benchmark.py#L656) | 656 | `"        \"results\": results,"` | — |
| [SRC-4FFD5AFC54-L000657](../../scripts/run_answer_quality_benchmark.py#L657) | 657 | `"        \"disclaimer\": ("` | — |
| [SRC-4FFD5AFC54-L000658](../../scripts/run_answer_quality_benchmark.py#L658) | 658 | `"            \"status=NOT_TESTED means answer quality was not auto-graded. \""` | — |
| [SRC-4FFD5AFC54-L000659](../../scripts/run_answer_quality_benchmark.py#L659) | 659 | `"            \"Fixtures in JSON were not applied to the live server.\""` | — |
| [SRC-4FFD5AFC54-L000660](../../scripts/run_answer_quality_benchmark.py#L660) | 660 | `"        ),"` | — |
| [SRC-4FFD5AFC54-L000661](../../scripts/run_answer_quality_benchmark.py#L661) | 661 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000662](../../scripts/run_answer_quality_benchmark.py#L662) | 662 | `"    text = json.dumps(envelope, ensure_ascii=False, indent=2)"` | — |
| [SRC-4FFD5AFC54-L000663](../../scripts/run_answer_quality_benchmark.py#L663) | 663 | `"    if out_path:"` | — |
| [SRC-4FFD5AFC54-L000664](../../scripts/run_answer_quality_benchmark.py#L664) | 664 | `"        out_path.write_text(text + \"\\n\", encoding=\"utf-8\")"` | — |
| [SRC-4FFD5AFC54-L000665](../../scripts/run_answer_quality_benchmark.py#L665) | 665 | `"        print(f\"Wrote {out_path}\")"` | — |
| [SRC-4FFD5AFC54-L000666](../../scripts/run_answer_quality_benchmark.py#L666) | 666 | `"    else:"` | — |
| [SRC-4FFD5AFC54-L000667](../../scripts/run_answer_quality_benchmark.py#L667) | 667 | `"        print(text)"` | — |
| [SRC-4FFD5AFC54-L000668](../../scripts/run_answer_quality_benchmark.py#L668) | 668 | `"    return 0"` | — |
| [SRC-4FFD5AFC54-L000669](../../scripts/run_answer_quality_benchmark.py#L669) | 669 | `""` | — |
| [SRC-4FFD5AFC54-L000670](../../scripts/run_answer_quality_benchmark.py#L670) | 670 | `""` | — |
| [SRC-4FFD5AFC54-L000671](../../scripts/run_answer_quality_benchmark.py#L671) | 671 | `"def main(argv: list[str] \| None = None) -> int:"` | — |
| [SRC-4FFD5AFC54-L000672](../../scripts/run_answer_quality_benchmark.py#L672) | 672 | `"    parser = argparse.ArgumentParser(description=\"Omarai answer-quality benchmark runner\")"` | — |
| [SRC-4FFD5AFC54-L000673](../../scripts/run_answer_quality_benchmark.py#L673) | 673 | `"    parser.add_argument("` | — |
| [SRC-4FFD5AFC54-L000674](../../scripts/run_answer_quality_benchmark.py#L674) | 674 | `"        \"--mode\","` | — |
| [SRC-4FFD5AFC54-L000675](../../scripts/run_answer_quality_benchmark.py#L675) | 675 | `"        choices=(\"validate\", \"live\"),"` | — |
| [SRC-4FFD5AFC54-L000676](../../scripts/run_answer_quality_benchmark.py#L676) | 676 | `"        default=\"validate\","` | — |
| [SRC-4FFD5AFC54-L000677](../../scripts/run_answer_quality_benchmark.py#L677) | 677 | `"        help=\"validate=offline corpus check (default); live=opt-in API calls\","` | — |
| [SRC-4FFD5AFC54-L000678](../../scripts/run_answer_quality_benchmark.py#L678) | 678 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000679](../../scripts/run_answer_quality_benchmark.py#L679) | 679 | `"    parser.add_argument("` | — |
| [SRC-4FFD5AFC54-L000680](../../scripts/run_answer_quality_benchmark.py#L680) | 680 | `"        \"--corpus\","` | — |
| [SRC-4FFD5AFC54-L000681](../../scripts/run_answer_quality_benchmark.py#L681) | 681 | `"        type=Path,"` | — |
| [SRC-4FFD5AFC54-L000682](../../scripts/run_answer_quality_benchmark.py#L682) | 682 | `"        default=DEFAULT_CORPUS,"` | — |
| [SRC-4FFD5AFC54-L000683](../../scripts/run_answer_quality_benchmark.py#L683) | 683 | `"        help=\"Path to answer_quality_cases.json\","` | — |
| [SRC-4FFD5AFC54-L000684](../../scripts/run_answer_quality_benchmark.py#L684) | 684 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000685](../../scripts/run_answer_quality_benchmark.py#L685) | 685 | `"    parser.add_argument(\"--summary\", action=\"store_true\", help=\"Extra validate summary\")"` | — |
| [SRC-4FFD5AFC54-L000686](../../scripts/run_answer_quality_benchmark.py#L686) | 686 | `"    parser.add_argument(\"--base-url\", default=\"http://127.0.0.1:8765\")"` | — |
| [SRC-4FFD5AFC54-L000687](../../scripts/run_answer_quality_benchmark.py#L687) | 687 | `"    parser.add_argument(\"--case-id\", default=None, help=\"Run a single case (live)\")"` | — |
| [SRC-4FFD5AFC54-L000688](../../scripts/run_answer_quality_benchmark.py#L688) | 688 | `"    parser.add_argument(\"--limit\", type=int, default=0, help=\"Max cases in live mode (0=all selected)\")"` | — |
| [SRC-4FFD5AFC54-L000689](../../scripts/run_answer_quality_benchmark.py#L689) | 689 | `"    parser.add_argument(\"--timeout\", type=float, default=60.0)"` | — |
| [SRC-4FFD5AFC54-L000690](../../scripts/run_answer_quality_benchmark.py#L690) | 690 | `"    parser.add_argument(\"--build-sha\", default=None, help=\"Optional expected deployed SHA; checked against /api/health before any benchmark request\")"` | — |
| [SRC-4FFD5AFC54-L000691](../../scripts/run_answer_quality_benchmark.py#L691) | 691 | `"    parser.add_argument(\"--request-costs\", type=Path, default=None, help=\"Optional externally reconciled per-case full-request costs in USD\")"` | — |
| [SRC-4FFD5AFC54-L000692](../../scripts/run_answer_quality_benchmark.py#L692) | 692 | `"    parser.add_argument(\"--delay\", type=float, default=0.0, help=\"Seconds between live requests\")"` | — |
| [SRC-4FFD5AFC54-L000693](../../scripts/run_answer_quality_benchmark.py#L693) | 693 | `"    parser.add_argument(\"--out\", type=Path, default=None, help=\"Write live results JSON\")"` | — |
| [SRC-4FFD5AFC54-L000694](../../scripts/run_answer_quality_benchmark.py#L694) | 694 | `"    args = parser.parse_args(argv)"` | — |
| [SRC-4FFD5AFC54-L000695](../../scripts/run_answer_quality_benchmark.py#L695) | 695 | `""` | — |
| [SRC-4FFD5AFC54-L000696](../../scripts/run_answer_quality_benchmark.py#L696) | 696 | `"    if args.mode == \"validate\":"` | — |
| [SRC-4FFD5AFC54-L000697](../../scripts/run_answer_quality_benchmark.py#L697) | 697 | `"        return run_validate(args.corpus, args.summary)"` | — |
| [SRC-4FFD5AFC54-L000698](../../scripts/run_answer_quality_benchmark.py#L698) | 698 | `"    if args.mode == \"live\":"` | — |
| [SRC-4FFD5AFC54-L000699](../../scripts/run_answer_quality_benchmark.py#L699) | 699 | `"        if not args.case_id and args.limit <= 0:"` | — |
| [SRC-4FFD5AFC54-L000700](../../scripts/run_answer_quality_benchmark.py#L700) | 700 | `"            print("` | — |
| [SRC-4FFD5AFC54-L000701](../../scripts/run_answer_quality_benchmark.py#L701) | 701 | `"                \"Refusing unbounded live run. Pass --case-id and/or --limit > 0.\","` | — |
| [SRC-4FFD5AFC54-L000702](../../scripts/run_answer_quality_benchmark.py#L702) | 702 | `"                file=sys.stderr,"` | — |
| [SRC-4FFD5AFC54-L000703](../../scripts/run_answer_quality_benchmark.py#L703) | 703 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000704](../../scripts/run_answer_quality_benchmark.py#L704) | 704 | `"            return 2"` | — |
| [SRC-4FFD5AFC54-L000705](../../scripts/run_answer_quality_benchmark.py#L705) | 705 | `"        return run_live("` | — |
| [SRC-4FFD5AFC54-L000706](../../scripts/run_answer_quality_benchmark.py#L706) | 706 | `"            args.corpus,"` | — |
| [SRC-4FFD5AFC54-L000707](../../scripts/run_answer_quality_benchmark.py#L707) | 707 | `"            args.base_url,"` | — |
| [SRC-4FFD5AFC54-L000708](../../scripts/run_answer_quality_benchmark.py#L708) | 708 | `"            args.case_id,"` | — |
| [SRC-4FFD5AFC54-L000709](../../scripts/run_answer_quality_benchmark.py#L709) | 709 | `"            args.limit,"` | — |
| [SRC-4FFD5AFC54-L000710](../../scripts/run_answer_quality_benchmark.py#L710) | 710 | `"            args.timeout,"` | — |
| [SRC-4FFD5AFC54-L000711](../../scripts/run_answer_quality_benchmark.py#L711) | 711 | `"            args.delay,"` | — |
| [SRC-4FFD5AFC54-L000712](../../scripts/run_answer_quality_benchmark.py#L712) | 712 | `"            args.out,"` | — |
| [SRC-4FFD5AFC54-L000713](../../scripts/run_answer_quality_benchmark.py#L713) | 713 | `"            args.build_sha,"` | — |
| [SRC-4FFD5AFC54-L000714](../../scripts/run_answer_quality_benchmark.py#L714) | 714 | `"            args.request_costs,"` | — |
| [SRC-4FFD5AFC54-L000715](../../scripts/run_answer_quality_benchmark.py#L715) | 715 | `"        )"` | — |
| [SRC-4FFD5AFC54-L000716](../../scripts/run_answer_quality_benchmark.py#L716) | 716 | `"    return 2"` | — |
| [SRC-4FFD5AFC54-L000717](../../scripts/run_answer_quality_benchmark.py#L717) | 717 | `""` | — |
| [SRC-4FFD5AFC54-L000718](../../scripts/run_answer_quality_benchmark.py#L718) | 718 | `""` | — |
| [SRC-4FFD5AFC54-L000719](../../scripts/run_answer_quality_benchmark.py#L719) | 719 | `"if __name__ == \"__main__\":"` | — |
| [SRC-4FFD5AFC54-L000720](../../scripts/run_answer_quality_benchmark.py#L720) | 720 | `"    raise SystemExit(main())"` | — |
## ملفات أخرى

### FILE-03FF422A16 — [scripts/score_answer_quality_reviews.py](../../scripts/score_answer_quality_reviews.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-03FF422A16-L000001](../../scripts/score_answer_quality_reviews.py#L1) | 1 | `"\"\"\"Score manually reviewed Omarai answer-quality cases without auto-grading."` | — |
| [SRC-03FF422A16-L000002](../../scripts/score_answer_quality_reviews.py#L2) | 2 | `""` | — |
| [SRC-03FF422A16-L000003](../../scripts/score_answer_quality_reviews.py#L3) | 3 | `"This offline tool calculates aggregate retrieval, faithfulness, correctness, citation,"` | — |
| [SRC-03FF422A16-L000004](../../scripts/score_answer_quality_reviews.py#L4) | 4 | `"and writing-quality metrics only from explicit review annotations. Missing judgments"` | — |
| [SRC-03FF422A16-L000005](../../scripts/score_answer_quality_reviews.py#L5) | 5 | `"remain NOT_TESTED; this script never calls an LLM or treats transport success as PASS."` | — |
| [SRC-03FF422A16-L000006](../../scripts/score_answer_quality_reviews.py#L6) | 6 | `"\"\"\""` | — |
| [SRC-03FF422A16-L000007](../../scripts/score_answer_quality_reviews.py#L7) | 7 | `"from __future__ import annotations"` | — |
| [SRC-03FF422A16-L000008](../../scripts/score_answer_quality_reviews.py#L8) | 8 | `""` | — |
| [SRC-03FF422A16-L000009](../../scripts/score_answer_quality_reviews.py#L9) | 9 | `"import argparse"` | — |
| [SRC-03FF422A16-L000010](../../scripts/score_answer_quality_reviews.py#L10) | 10 | `"import json"` | — |
| [SRC-03FF422A16-L000011](../../scripts/score_answer_quality_reviews.py#L11) | 11 | `"import math"` | — |
| [SRC-03FF422A16-L000012](../../scripts/score_answer_quality_reviews.py#L12) | 12 | `"import sys"` | — |
| [SRC-03FF422A16-L000013](../../scripts/score_answer_quality_reviews.py#L13) | 13 | `"from collections import Counter"` | — |
| [SRC-03FF422A16-L000014](../../scripts/score_answer_quality_reviews.py#L14) | 14 | `"from pathlib import Path"` | — |
| [SRC-03FF422A16-L000015](../../scripts/score_answer_quality_reviews.py#L15) | 15 | `"from typing import Any"` | — |
| [SRC-03FF422A16-L000016](../../scripts/score_answer_quality_reviews.py#L16) | 16 | `""` | — |
| [SRC-03FF422A16-L000017](../../scripts/score_answer_quality_reviews.py#L17) | 17 | `"ROOT = Path(__file__).resolve().parents[1]"` | — |
| [SRC-03FF422A16-L000018](../../scripts/score_answer_quality_reviews.py#L18) | 18 | `"DEFAULT_CORPUS = ROOT / \"tests\" / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-03FF422A16-L000019](../../scripts/score_answer_quality_reviews.py#L19) | 19 | `"ALLOWED_STATUSES = {\"REVIEWED\", \"NOT_TESTED\", \"BLOCKED\"}"` | — |
| [SRC-03FF422A16-L000020](../../scripts/score_answer_quality_reviews.py#L20) | 20 | `"COUNT_GROUPS = {"` | — |
| [SRC-03FF422A16-L000021](../../scripts/score_answer_quality_reviews.py#L21) | 21 | `"    \"retrieval\": (\"relevant_retrieved\", \"retrieved_count\", \"relevant_available\"),"` | — |
| [SRC-03FF422A16-L000022](../../scripts/score_answer_quality_reviews.py#L22) | 22 | `"    \"faithfulness\": (\"supported_claims\", \"reviewed_claims\"),"` | — |
| [SRC-03FF422A16-L000023](../../scripts/score_answer_quality_reviews.py#L23) | 23 | `"    \"correctness\": (\"correct_facts\", \"reviewed_facts\"),"` | — |
| [SRC-03FF422A16-L000024](../../scripts/score_answer_quality_reviews.py#L24) | 24 | `"    \"citations\": (\"supported_citations\", \"reviewed_citations\"),"` | — |
| [SRC-03FF422A16-L000025](../../scripts/score_answer_quality_reviews.py#L25) | 25 | `"}"` | — |
| [SRC-03FF422A16-L000026](../../scripts/score_answer_quality_reviews.py#L26) | 26 | `""` | — |
| [SRC-03FF422A16-L000027](../../scripts/score_answer_quality_reviews.py#L27) | 27 | `""` | — |
| [SRC-03FF422A16-L000028](../../scripts/score_answer_quality_reviews.py#L28) | 28 | `"def load_json_object(path: Path) -> dict[str, Any]:"` | — |
| [SRC-03FF422A16-L000029](../../scripts/score_answer_quality_reviews.py#L29) | 29 | `"    if not path.is_file():"` | — |
| [SRC-03FF422A16-L000030](../../scripts/score_answer_quality_reviews.py#L30) | 30 | `"        raise FileNotFoundError(\"Input file not found: \" + str(path))"` | — |
| [SRC-03FF422A16-L000031](../../scripts/score_answer_quality_reviews.py#L31) | 31 | `"    data = json.loads(path.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-03FF422A16-L000032](../../scripts/score_answer_quality_reviews.py#L32) | 32 | `"    if not isinstance(data, dict):"` | — |
| [SRC-03FF422A16-L000033](../../scripts/score_answer_quality_reviews.py#L33) | 33 | `"        raise TypeError(\"JSON root must be an object\")"` | — |
| [SRC-03FF422A16-L000034](../../scripts/score_answer_quality_reviews.py#L34) | 34 | `"    return data"` | — |
| [SRC-03FF422A16-L000035](../../scripts/score_answer_quality_reviews.py#L35) | 35 | `""` | — |
| [SRC-03FF422A16-L000036](../../scripts/score_answer_quality_reviews.py#L36) | 36 | `""` | — |
| [SRC-03FF422A16-L000037](../../scripts/score_answer_quality_reviews.py#L37) | 37 | `"def _is_nonnegative_int(value: Any) -> bool:"` | — |
| [SRC-03FF422A16-L000038](../../scripts/score_answer_quality_reviews.py#L38) | 38 | `"    return isinstance(value, int) and not isinstance(value, bool) and value >= 0"` | — |
| [SRC-03FF422A16-L000039](../../scripts/score_answer_quality_reviews.py#L39) | 39 | `""` | — |
| [SRC-03FF422A16-L000040](../../scripts/score_answer_quality_reviews.py#L40) | 40 | `""` | — |
| [SRC-03FF422A16-L000041](../../scripts/score_answer_quality_reviews.py#L41) | 41 | `"def validate_reviews("` | — |
| [SRC-03FF422A16-L000042](../../scripts/score_answer_quality_reviews.py#L42) | 42 | `"    review_data: dict[str, Any], corpus_data: dict[str, Any]"` | — |
| [SRC-03FF422A16-L000043](../../scripts/score_answer_quality_reviews.py#L43) | 43 | `") -> list[str]:"` | — |
| [SRC-03FF422A16-L000044](../../scripts/score_answer_quality_reviews.py#L44) | 44 | `"    problems: list[str] = []"` | — |
| [SRC-03FF422A16-L000045](../../scripts/score_answer_quality_reviews.py#L45) | 45 | `"    reviews = review_data.get(\"reviews\")"` | — |
| [SRC-03FF422A16-L000046](../../scripts/score_answer_quality_reviews.py#L46) | 46 | `"    corpus_cases = corpus_data.get(\"cases\")"` | — |
| [SRC-03FF422A16-L000047](../../scripts/score_answer_quality_reviews.py#L47) | 47 | `"    if not isinstance(reviews, list):"` | — |
| [SRC-03FF422A16-L000048](../../scripts/score_answer_quality_reviews.py#L48) | 48 | `"        return [\"reviews must be an array\"]"` | — |
| [SRC-03FF422A16-L000049](../../scripts/score_answer_quality_reviews.py#L49) | 49 | `"    if not isinstance(corpus_cases, list):"` | — |
| [SRC-03FF422A16-L000050](../../scripts/score_answer_quality_reviews.py#L50) | 50 | `"        return [\"corpus must contain a cases array\"]"` | — |
| [SRC-03FF422A16-L000051](../../scripts/score_answer_quality_reviews.py#L51) | 51 | `""` | — |
| [SRC-03FF422A16-L000052](../../scripts/score_answer_quality_reviews.py#L52) | 52 | `"    valid_case_ids = {"` | — |
| [SRC-03FF422A16-L000053](../../scripts/score_answer_quality_reviews.py#L53) | 53 | `"        item.get(\"case_id\")"` | — |
| [SRC-03FF422A16-L000054](../../scripts/score_answer_quality_reviews.py#L54) | 54 | `"        for item in corpus_cases"` | — |
| [SRC-03FF422A16-L000055](../../scripts/score_answer_quality_reviews.py#L55) | 55 | `"        if isinstance(item, dict) and isinstance(item.get(\"case_id\"), str)"` | — |
| [SRC-03FF422A16-L000056](../../scripts/score_answer_quality_reviews.py#L56) | 56 | `"    }"` | — |
| [SRC-03FF422A16-L000057](../../scripts/score_answer_quality_reviews.py#L57) | 57 | `"    seen: set[str] = set()"` | — |
| [SRC-03FF422A16-L000058](../../scripts/score_answer_quality_reviews.py#L58) | 58 | `"    for index, item in enumerate(reviews):"` | — |
| [SRC-03FF422A16-L000059](../../scripts/score_answer_quality_reviews.py#L59) | 59 | `"        label = \"reviews[\" + str(index) + \"]\""` | — |
| [SRC-03FF422A16-L000060](../../scripts/score_answer_quality_reviews.py#L60) | 60 | `"        if not isinstance(item, dict):"` | — |
| [SRC-03FF422A16-L000061](../../scripts/score_answer_quality_reviews.py#L61) | 61 | `"            problems.append(label + \" must be an object\")"` | — |
| [SRC-03FF422A16-L000062](../../scripts/score_answer_quality_reviews.py#L62) | 62 | `"            continue"` | — |
| [SRC-03FF422A16-L000063](../../scripts/score_answer_quality_reviews.py#L63) | 63 | `"        case_id = item.get(\"case_id\")"` | — |
| [SRC-03FF422A16-L000064](../../scripts/score_answer_quality_reviews.py#L64) | 64 | `"        if not isinstance(case_id, str) or not case_id.strip():"` | — |
| [SRC-03FF422A16-L000065](../../scripts/score_answer_quality_reviews.py#L65) | 65 | `"            problems.append(label + \": case_id must be a non-empty string\")"` | — |
| [SRC-03FF422A16-L000066](../../scripts/score_answer_quality_reviews.py#L66) | 66 | `"            continue"` | — |
| [SRC-03FF422A16-L000067](../../scripts/score_answer_quality_reviews.py#L67) | 67 | `"        if case_id in seen:"` | — |
| [SRC-03FF422A16-L000068](../../scripts/score_answer_quality_reviews.py#L68) | 68 | `"            problems.append(case_id + \": duplicate review\")"` | — |
| [SRC-03FF422A16-L000069](../../scripts/score_answer_quality_reviews.py#L69) | 69 | `"        seen.add(case_id)"` | — |
| [SRC-03FF422A16-L000070](../../scripts/score_answer_quality_reviews.py#L70) | 70 | `"        if case_id not in valid_case_ids:"` | — |
| [SRC-03FF422A16-L000071](../../scripts/score_answer_quality_reviews.py#L71) | 71 | `"            problems.append(case_id + \": unknown case_id (not in the supplied corpus)\")"` | — |
| [SRC-03FF422A16-L000072](../../scripts/score_answer_quality_reviews.py#L72) | 72 | `"        status = item.get(\"status\")"` | — |
| [SRC-03FF422A16-L000073](../../scripts/score_answer_quality_reviews.py#L73) | 73 | `"        if status not in ALLOWED_STATUSES:"` | — |
| [SRC-03FF422A16-L000074](../../scripts/score_answer_quality_reviews.py#L74) | 74 | `"            problems.append(case_id + \": status must be one of \" + \", \".join(sorted(ALLOWED_STATUSES)))"` | — |
| [SRC-03FF422A16-L000075](../../scripts/score_answer_quality_reviews.py#L75) | 75 | `"            continue"` | — |
| [SRC-03FF422A16-L000076](../../scripts/score_answer_quality_reviews.py#L76) | 76 | `""` | — |
| [SRC-03FF422A16-L000077](../../scripts/score_answer_quality_reviews.py#L77) | 77 | `"        has_score = False"` | — |
| [SRC-03FF422A16-L000078](../../scripts/score_answer_quality_reviews.py#L78) | 78 | `"        for group_name, fields in COUNT_GROUPS.items():"` | — |
| [SRC-03FF422A16-L000079](../../scripts/score_answer_quality_reviews.py#L79) | 79 | `"            group = item.get(group_name)"` | — |
| [SRC-03FF422A16-L000080](../../scripts/score_answer_quality_reviews.py#L80) | 80 | `"            if group is None:"` | — |
| [SRC-03FF422A16-L000081](../../scripts/score_answer_quality_reviews.py#L81) | 81 | `"                continue"` | — |
| [SRC-03FF422A16-L000082](../../scripts/score_answer_quality_reviews.py#L82) | 82 | `"            if not isinstance(group, dict):"` | — |
| [SRC-03FF422A16-L000083](../../scripts/score_answer_quality_reviews.py#L83) | 83 | `"                problems.append(case_id + \": \" + group_name + \" must be an object\")"` | — |
| [SRC-03FF422A16-L000084](../../scripts/score_answer_quality_reviews.py#L84) | 84 | `"                continue"` | — |
| [SRC-03FF422A16-L000085](../../scripts/score_answer_quality_reviews.py#L85) | 85 | `"            has_score = True"` | — |
| [SRC-03FF422A16-L000086](../../scripts/score_answer_quality_reviews.py#L86) | 86 | `"            missing = [field for field in fields if field not in group]"` | — |
| [SRC-03FF422A16-L000087](../../scripts/score_answer_quality_reviews.py#L87) | 87 | `"            if missing:"` | — |
| [SRC-03FF422A16-L000088](../../scripts/score_answer_quality_reviews.py#L88) | 88 | `"                problems.append(case_id + \": \" + group_name + \" missing \" + \", \".join(missing))"` | — |
| [SRC-03FF422A16-L000089](../../scripts/score_answer_quality_reviews.py#L89) | 89 | `"                continue"` | — |
| [SRC-03FF422A16-L000090](../../scripts/score_answer_quality_reviews.py#L90) | 90 | `"            values: dict[str, int] = {}"` | — |
| [SRC-03FF422A16-L000091](../../scripts/score_answer_quality_reviews.py#L91) | 91 | `"            for field in fields:"` | — |
| [SRC-03FF422A16-L000092](../../scripts/score_answer_quality_reviews.py#L92) | 92 | `"                value = group[field]"` | — |
| [SRC-03FF422A16-L000093](../../scripts/score_answer_quality_reviews.py#L93) | 93 | `"                if not _is_nonnegative_int(value):"` | — |
| [SRC-03FF422A16-L000094](../../scripts/score_answer_quality_reviews.py#L94) | 94 | `"                    problems.append(case_id + \": \" + group_name + \".\" + field + \" must be a non-negative integer\")"` | — |
| [SRC-03FF422A16-L000095](../../scripts/score_answer_quality_reviews.py#L95) | 95 | `"                else:"` | — |
| [SRC-03FF422A16-L000096](../../scripts/score_answer_quality_reviews.py#L96) | 96 | `"                    values[field] = value"` | — |
| [SRC-03FF422A16-L000097](../../scripts/score_answer_quality_reviews.py#L97) | 97 | `"            if len(values) != len(fields):"` | — |
| [SRC-03FF422A16-L000098](../../scripts/score_answer_quality_reviews.py#L98) | 98 | `"                continue"` | — |
| [SRC-03FF422A16-L000099](../../scripts/score_answer_quality_reviews.py#L99) | 99 | `"            if group_name == \"retrieval\":"` | — |
| [SRC-03FF422A16-L000100](../../scripts/score_answer_quality_reviews.py#L100) | 100 | `"                if values[\"relevant_retrieved\"] > values[\"retrieved_count\"]:"` | — |
| [SRC-03FF422A16-L000101](../../scripts/score_answer_quality_reviews.py#L101) | 101 | `"                    problems.append(case_id + \": relevant_retrieved cannot exceed retrieved_count\")"` | — |
| [SRC-03FF422A16-L000102](../../scripts/score_answer_quality_reviews.py#L102) | 102 | `"                if values[\"relevant_retrieved\"] > values[\"relevant_available\"]:"` | — |
| [SRC-03FF422A16-L000103](../../scripts/score_answer_quality_reviews.py#L103) | 103 | `"                    problems.append(case_id + \": relevant_retrieved cannot exceed relevant_available\")"` | — |
| [SRC-03FF422A16-L000104](../../scripts/score_answer_quality_reviews.py#L104) | 104 | `"            else:"` | — |
| [SRC-03FF422A16-L000105](../../scripts/score_answer_quality_reviews.py#L105) | 105 | `"                numerator, denominator = fields"` | — |
| [SRC-03FF422A16-L000106](../../scripts/score_answer_quality_reviews.py#L106) | 106 | `"                if values[numerator] > values[denominator]:"` | — |
| [SRC-03FF422A16-L000107](../../scripts/score_answer_quality_reviews.py#L107) | 107 | `"                    problems.append(case_id + \": \" + numerator + \" cannot exceed \" + denominator)"` | — |
| [SRC-03FF422A16-L000108](../../scripts/score_answer_quality_reviews.py#L108) | 108 | `""` | — |
| [SRC-03FF422A16-L000109](../../scripts/score_answer_quality_reviews.py#L109) | 109 | `"        writing = item.get(\"writing_quality\")"` | — |
| [SRC-03FF422A16-L000110](../../scripts/score_answer_quality_reviews.py#L110) | 110 | `"        if writing is not None:"` | — |
| [SRC-03FF422A16-L000111](../../scripts/score_answer_quality_reviews.py#L111) | 111 | `"            has_score = True"` | — |
| [SRC-03FF422A16-L000112](../../scripts/score_answer_quality_reviews.py#L112) | 112 | `"            if ("` | — |
| [SRC-03FF422A16-L000113](../../scripts/score_answer_quality_reviews.py#L113) | 113 | `"                isinstance(writing, bool)"` | — |
| [SRC-03FF422A16-L000114](../../scripts/score_answer_quality_reviews.py#L114) | 114 | `"                or not isinstance(writing, (int, float))"` | — |
| [SRC-03FF422A16-L000115](../../scripts/score_answer_quality_reviews.py#L115) | 115 | `"                or not math.isfinite(float(writing))"` | — |
| [SRC-03FF422A16-L000116](../../scripts/score_answer_quality_reviews.py#L116) | 116 | `"                or float(writing) < 1"` | — |
| [SRC-03FF422A16-L000117](../../scripts/score_answer_quality_reviews.py#L117) | 117 | `"                or float(writing) > 5"` | — |
| [SRC-03FF422A16-L000118](../../scripts/score_answer_quality_reviews.py#L118) | 118 | `"            ):"` | — |
| [SRC-03FF422A16-L000119](../../scripts/score_answer_quality_reviews.py#L119) | 119 | `"                problems.append(case_id + \": writing_quality must be a finite score from 1 to 5\")"` | — |
| [SRC-03FF422A16-L000120](../../scripts/score_answer_quality_reviews.py#L120) | 120 | `""` | — |
| [SRC-03FF422A16-L000121](../../scripts/score_answer_quality_reviews.py#L121) | 121 | `"        if status != \"REVIEWED\" and has_score:"` | — |
| [SRC-03FF422A16-L000122](../../scripts/score_answer_quality_reviews.py#L122) | 122 | `"            problems.append(case_id + \": unreviewed case must not contain metric scores\")"` | — |
| [SRC-03FF422A16-L000123](../../scripts/score_answer_quality_reviews.py#L123) | 123 | `"        if status == \"REVIEWED\" and not has_score:"` | — |
| [SRC-03FF422A16-L000124](../../scripts/score_answer_quality_reviews.py#L124) | 124 | `"            problems.append(case_id + \": REVIEWED case must include at least one scored dimension\")"` | — |
| [SRC-03FF422A16-L000125](../../scripts/score_answer_quality_reviews.py#L125) | 125 | `"    return problems"` | — |
| [SRC-03FF422A16-L000126](../../scripts/score_answer_quality_reviews.py#L126) | 126 | `""` | — |
| [SRC-03FF422A16-L000127](../../scripts/score_answer_quality_reviews.py#L127) | 127 | `""` | — |
| [SRC-03FF422A16-L000128](../../scripts/score_answer_quality_reviews.py#L128) | 128 | `"def _ratio(numerator: int, denominator: int, case_count: int) -> dict[str, Any]:"` | — |
| [SRC-03FF422A16-L000129](../../scripts/score_answer_quality_reviews.py#L129) | 129 | `"    return {"` | — |
| [SRC-03FF422A16-L000130](../../scripts/score_answer_quality_reviews.py#L130) | 130 | `"        \"score\": round(numerator / denominator, 4) if denominator else None,"` | — |
| [SRC-03FF422A16-L000131](../../scripts/score_answer_quality_reviews.py#L131) | 131 | `"        \"numerator\": numerator,"` | — |
| [SRC-03FF422A16-L000132](../../scripts/score_answer_quality_reviews.py#L132) | 132 | `"        \"denominator\": denominator,"` | — |
| [SRC-03FF422A16-L000133](../../scripts/score_answer_quality_reviews.py#L133) | 133 | `"        \"reviewed_case_count\": case_count,"` | — |
| [SRC-03FF422A16-L000134](../../scripts/score_answer_quality_reviews.py#L134) | 134 | `"        \"status\": \"SCORED_FROM_HUMAN_REVIEW\" if denominator else \"NOT_SCORABLE_NO_ANNOTATED_DENOMINATOR\","` | — |
| [SRC-03FF422A16-L000135](../../scripts/score_answer_quality_reviews.py#L135) | 135 | `"    }"` | — |
| [SRC-03FF422A16-L000136](../../scripts/score_answer_quality_reviews.py#L136) | 136 | `""` | — |
| [SRC-03FF422A16-L000137](../../scripts/score_answer_quality_reviews.py#L137) | 137 | `""` | — |
| [SRC-03FF422A16-L000138](../../scripts/score_answer_quality_reviews.py#L138) | 138 | `"def summarize_reviews("` | — |
| [SRC-03FF422A16-L000139](../../scripts/score_answer_quality_reviews.py#L139) | 139 | `"    review_data: dict[str, Any], corpus_data: dict[str, Any]"` | — |
| [SRC-03FF422A16-L000140](../../scripts/score_answer_quality_reviews.py#L140) | 140 | `") -> dict[str, Any]:"` | — |
| [SRC-03FF422A16-L000141](../../scripts/score_answer_quality_reviews.py#L141) | 141 | `"    problems = validate_reviews(review_data, corpus_data)"` | — |
| [SRC-03FF422A16-L000142](../../scripts/score_answer_quality_reviews.py#L142) | 142 | `"    if problems:"` | — |
| [SRC-03FF422A16-L000143](../../scripts/score_answer_quality_reviews.py#L143) | 143 | `"        raise ValueError(\"; \".join(problems))"` | — |
| [SRC-03FF422A16-L000144](../../scripts/score_answer_quality_reviews.py#L144) | 144 | `"    reviews = review_data[\"reviews\"]"` | — |
| [SRC-03FF422A16-L000145](../../scripts/score_answer_quality_reviews.py#L145) | 145 | `"    reviewed = [item for item in reviews if item[\"status\"] == \"REVIEWED\"]"` | — |
| [SRC-03FF422A16-L000146](../../scripts/score_answer_quality_reviews.py#L146) | 146 | `"    status_counts = Counter(item[\"status\"] for item in reviews)"` | — |
| [SRC-03FF422A16-L000147](../../scripts/score_answer_quality_reviews.py#L147) | 147 | `"    corpus_count = len(corpus_data[\"cases\"])"` | — |
| [SRC-03FF422A16-L000148](../../scripts/score_answer_quality_reviews.py#L148) | 148 | `"    reviewed_ids = {item[\"case_id\"] for item in reviewed}"` | — |
| [SRC-03FF422A16-L000149](../../scripts/score_answer_quality_reviews.py#L149) | 149 | `""` | — |
| [SRC-03FF422A16-L000150](../../scripts/score_answer_quality_reviews.py#L150) | 150 | `"    retrieval_rel = retrieval_total = retrieval_available = 0"` | — |
| [SRC-03FF422A16-L000151](../../scripts/score_answer_quality_reviews.py#L151) | 151 | `"    retrieval_cases = set()"` | — |
| [SRC-03FF422A16-L000152](../../scripts/score_answer_quality_reviews.py#L152) | 152 | `"    faithfulness_supported = faithfulness_total = 0"` | — |
| [SRC-03FF422A16-L000153](../../scripts/score_answer_quality_reviews.py#L153) | 153 | `"    faithfulness_cases = set()"` | — |
| [SRC-03FF422A16-L000154](../../scripts/score_answer_quality_reviews.py#L154) | 154 | `"    correctness_correct = correctness_total = 0"` | — |
| [SRC-03FF422A16-L000155](../../scripts/score_answer_quality_reviews.py#L155) | 155 | `"    correctness_cases = set()"` | — |
| [SRC-03FF422A16-L000156](../../scripts/score_answer_quality_reviews.py#L156) | 156 | `"    citation_supported = citation_total = 0"` | — |
| [SRC-03FF422A16-L000157](../../scripts/score_answer_quality_reviews.py#L157) | 157 | `"    citation_cases = set()"` | — |
| [SRC-03FF422A16-L000158](../../scripts/score_answer_quality_reviews.py#L158) | 158 | `"    writing_scores: list[float] = []"` | — |
| [SRC-03FF422A16-L000159](../../scripts/score_answer_quality_reviews.py#L159) | 159 | `""` | — |
| [SRC-03FF422A16-L000160](../../scripts/score_answer_quality_reviews.py#L160) | 160 | `"    for item in reviewed:"` | — |
| [SRC-03FF422A16-L000161](../../scripts/score_answer_quality_reviews.py#L161) | 161 | `"        case_id = item[\"case_id\"]"` | — |
| [SRC-03FF422A16-L000162](../../scripts/score_answer_quality_reviews.py#L162) | 162 | `"        retrieval = item.get(\"retrieval\")"` | — |
| [SRC-03FF422A16-L000163](../../scripts/score_answer_quality_reviews.py#L163) | 163 | `"        if isinstance(retrieval, dict):"` | — |
| [SRC-03FF422A16-L000164](../../scripts/score_answer_quality_reviews.py#L164) | 164 | `"            retrieval_rel += retrieval[\"relevant_retrieved\"]"` | — |
| [SRC-03FF422A16-L000165](../../scripts/score_answer_quality_reviews.py#L165) | 165 | `"            retrieval_total += retrieval[\"retrieved_count\"]"` | — |
| [SRC-03FF422A16-L000166](../../scripts/score_answer_quality_reviews.py#L166) | 166 | `"            retrieval_available += retrieval[\"relevant_available\"]"` | — |
| [SRC-03FF422A16-L000167](../../scripts/score_answer_quality_reviews.py#L167) | 167 | `"            retrieval_cases.add(case_id)"` | — |
| [SRC-03FF422A16-L000168](../../scripts/score_answer_quality_reviews.py#L168) | 168 | `"        faithfulness = item.get(\"faithfulness\")"` | — |
| [SRC-03FF422A16-L000169](../../scripts/score_answer_quality_reviews.py#L169) | 169 | `"        if isinstance(faithfulness, dict):"` | — |
| [SRC-03FF422A16-L000170](../../scripts/score_answer_quality_reviews.py#L170) | 170 | `"            faithfulness_supported += faithfulness[\"supported_claims\"]"` | — |
| [SRC-03FF422A16-L000171](../../scripts/score_answer_quality_reviews.py#L171) | 171 | `"            faithfulness_total += faithfulness[\"reviewed_claims\"]"` | — |
| [SRC-03FF422A16-L000172](../../scripts/score_answer_quality_reviews.py#L172) | 172 | `"            faithfulness_cases.add(case_id)"` | — |
| [SRC-03FF422A16-L000173](../../scripts/score_answer_quality_reviews.py#L173) | 173 | `"        correctness = item.get(\"correctness\")"` | — |
| [SRC-03FF422A16-L000174](../../scripts/score_answer_quality_reviews.py#L174) | 174 | `"        if isinstance(correctness, dict):"` | — |
| [SRC-03FF422A16-L000175](../../scripts/score_answer_quality_reviews.py#L175) | 175 | `"            correctness_correct += correctness[\"correct_facts\"]"` | — |
| [SRC-03FF422A16-L000176](../../scripts/score_answer_quality_reviews.py#L176) | 176 | `"            correctness_total += correctness[\"reviewed_facts\"]"` | — |
| [SRC-03FF422A16-L000177](../../scripts/score_answer_quality_reviews.py#L177) | 177 | `"            correctness_cases.add(case_id)"` | — |
| [SRC-03FF422A16-L000178](../../scripts/score_answer_quality_reviews.py#L178) | 178 | `"        citations = item.get(\"citations\")"` | — |
| [SRC-03FF422A16-L000179](../../scripts/score_answer_quality_reviews.py#L179) | 179 | `"        if isinstance(citations, dict):"` | — |
| [SRC-03FF422A16-L000180](../../scripts/score_answer_quality_reviews.py#L180) | 180 | `"            citation_supported += citations[\"supported_citations\"]"` | — |
| [SRC-03FF422A16-L000181](../../scripts/score_answer_quality_reviews.py#L181) | 181 | `"            citation_total += citations[\"reviewed_citations\"]"` | — |
| [SRC-03FF422A16-L000182](../../scripts/score_answer_quality_reviews.py#L182) | 182 | `"            citation_cases.add(case_id)"` | — |
| [SRC-03FF422A16-L000183](../../scripts/score_answer_quality_reviews.py#L183) | 183 | `"        score = item.get(\"writing_quality\")"` | — |
| [SRC-03FF422A16-L000184](../../scripts/score_answer_quality_reviews.py#L184) | 184 | `"        if score is not None:"` | — |
| [SRC-03FF422A16-L000185](../../scripts/score_answer_quality_reviews.py#L185) | 185 | `"            writing_scores.append(float(score))"` | — |
| [SRC-03FF422A16-L000186](../../scripts/score_answer_quality_reviews.py#L186) | 186 | `""` | — |
| [SRC-03FF422A16-L000187](../../scripts/score_answer_quality_reviews.py#L187) | 187 | `"    return {"` | — |
| [SRC-03FF422A16-L000188](../../scripts/score_answer_quality_reviews.py#L188) | 188 | `"        \"benchmark_id\": corpus_data.get(\"benchmark_id\", \"unknown\"),"` | — |
| [SRC-03FF422A16-L000189](../../scripts/score_answer_quality_reviews.py#L189) | 189 | `"        \"review_schema_version\": review_data.get(\"schema_version\", \"unknown\"),"` | — |
| [SRC-03FF422A16-L000190](../../scripts/score_answer_quality_reviews.py#L190) | 190 | `"        \"scoring_method\": \"aggregate_from_explicit_human_annotations\","` | — |
| [SRC-03FF422A16-L000191](../../scripts/score_answer_quality_reviews.py#L191) | 191 | `"        \"automatic_answer_grading\": False,"` | — |
| [SRC-03FF422A16-L000192](../../scripts/score_answer_quality_reviews.py#L192) | 192 | `"        \"ragas_executed\": False,"` | — |
| [SRC-03FF422A16-L000193](../../scripts/score_answer_quality_reviews.py#L193) | 193 | `"        \"corpus_case_count\": corpus_count,"` | — |
| [SRC-03FF422A16-L000194](../../scripts/score_answer_quality_reviews.py#L194) | 194 | `"        \"submitted_review_count\": len(reviews),"` | — |
| [SRC-03FF422A16-L000195](../../scripts/score_answer_quality_reviews.py#L195) | 195 | `"        \"unique_reviewed_case_count\": len(reviewed_ids),"` | — |
| [SRC-03FF422A16-L000196](../../scripts/score_answer_quality_reviews.py#L196) | 196 | `"        \"case_status_counts\": {status: status_counts.get(status, 0) for status in sorted(ALLOWED_STATUSES)},"` | — |
| [SRC-03FF422A16-L000197](../../scripts/score_answer_quality_reviews.py#L197) | 197 | `"        \"reviewed_case_coverage\": round(len(reviewed_ids) / corpus_count, 4) if corpus_count else 0.0,"` | — |
| [SRC-03FF422A16-L000198](../../scripts/score_answer_quality_reviews.py#L198) | 198 | `"        \"metrics\": {"` | — |
| [SRC-03FF422A16-L000199](../../scripts/score_answer_quality_reviews.py#L199) | 199 | `"            \"retrieval_precision\": _ratio(retrieval_rel, retrieval_total, len(retrieval_cases)),"` | — |
| [SRC-03FF422A16-L000200](../../scripts/score_answer_quality_reviews.py#L200) | 200 | `"            \"retrieval_recall\": _ratio(retrieval_rel, retrieval_available, len(retrieval_cases)),"` | — |
| [SRC-03FF422A16-L000201](../../scripts/score_answer_quality_reviews.py#L201) | 201 | `"            \"faithfulness\": _ratio(faithfulness_supported, faithfulness_total, len(faithfulness_cases)),"` | — |
| [SRC-03FF422A16-L000202](../../scripts/score_answer_quality_reviews.py#L202) | 202 | `"            \"correctness\": _ratio(correctness_correct, correctness_total, len(correctness_cases)),"` | — |
| [SRC-03FF422A16-L000203](../../scripts/score_answer_quality_reviews.py#L203) | 203 | `"            \"citation_support\": _ratio(citation_supported, citation_total, len(citation_cases)),"` | — |
| [SRC-03FF422A16-L000204](../../scripts/score_answer_quality_reviews.py#L204) | 204 | `"            \"writing_quality_1_to_5\": {"` | — |
| [SRC-03FF422A16-L000205](../../scripts/score_answer_quality_reviews.py#L205) | 205 | `"                \"score\": round(sum(writing_scores) / len(writing_scores), 3) if writing_scores else None,"` | — |
| [SRC-03FF422A16-L000206](../../scripts/score_answer_quality_reviews.py#L206) | 206 | `"                \"scale_min\": 1,"` | — |
| [SRC-03FF422A16-L000207](../../scripts/score_answer_quality_reviews.py#L207) | 207 | `"                \"scale_max\": 5,"` | — |
| [SRC-03FF422A16-L000208](../../scripts/score_answer_quality_reviews.py#L208) | 208 | `"                \"reviewed_case_count\": len(writing_scores),"` | — |
| [SRC-03FF422A16-L000209](../../scripts/score_answer_quality_reviews.py#L209) | 209 | `"                \"status\": \"SCORED_FROM_HUMAN_REVIEW\" if writing_scores else \"NOT_SCORABLE_NO_HUMAN_SCORES\","` | — |
| [SRC-03FF422A16-L000210](../../scripts/score_answer_quality_reviews.py#L210) | 210 | `"            },"` | — |
| [SRC-03FF422A16-L000211](../../scripts/score_answer_quality_reviews.py#L211) | 211 | `"        },"` | — |
| [SRC-03FF422A16-L000212](../../scripts/score_answer_quality_reviews.py#L212) | 212 | `"        \"limitations\": ["` | — |
| [SRC-03FF422A16-L000213](../../scripts/score_answer_quality_reviews.py#L213) | 213 | `"            \"Metrics include only explicitly reviewed cases and human-entered labels.\","` | — |
| [SRC-03FF422A16-L000214](../../scripts/score_answer_quality_reviews.py#L214) | 214 | `"            \"Retrieval scores depend on consistent, deduplicated relevance counts and a defined candidate pool.\","` | — |
| [SRC-03FF422A16-L000215](../../scripts/score_answer_quality_reviews.py#L215) | 215 | `"            \"Faithfulness and correctness reflect reviewer judgments, not automatic proof of truth.\","` | — |
| [SRC-03FF422A16-L000216](../../scripts/score_answer_quality_reviews.py#L216) | 216 | `"            \"Writing quality is a 1-to-5 human rating; it is not a fluency model score.\","` | — |
| [SRC-03FF422A16-L000217](../../scripts/score_answer_quality_reviews.py#L217) | 217 | `"            \"RAGAS was not executed and no unobserved case is assigned a PASS.\","` | — |
| [SRC-03FF422A16-L000218](../../scripts/score_answer_quality_reviews.py#L218) | 218 | `"        ],"` | — |
| [SRC-03FF422A16-L000219](../../scripts/score_answer_quality_reviews.py#L219) | 219 | `"    }"` | — |
| [SRC-03FF422A16-L000220](../../scripts/score_answer_quality_reviews.py#L220) | 220 | `""` | — |
| [SRC-03FF422A16-L000221](../../scripts/score_answer_quality_reviews.py#L221) | 221 | `""` | — |
| [SRC-03FF422A16-L000222](../../scripts/score_answer_quality_reviews.py#L222) | 222 | `"def main(argv: list[str] \| None = None) -> int:"` | — |
| [SRC-03FF422A16-L000223](../../scripts/score_answer_quality_reviews.py#L223) | 223 | `"    parser = argparse.ArgumentParser(description=__doc__)"` | — |
| [SRC-03FF422A16-L000224](../../scripts/score_answer_quality_reviews.py#L224) | 224 | `"    parser.add_argument(\"--reviews\", required=True, type=Path, help=\"JSON file containing explicit human review annotations\")"` | — |
| [SRC-03FF422A16-L000225](../../scripts/score_answer_quality_reviews.py#L225) | 225 | `"    parser.add_argument(\"--corpus\", default=DEFAULT_CORPUS, type=Path, help=\"Answer-quality corpus used to validate case IDs\")"` | — |
| [SRC-03FF422A16-L000226](../../scripts/score_answer_quality_reviews.py#L226) | 226 | `"    parser.add_argument(\"--out\", type=Path, help=\"Optional path to write the summary JSON\")"` | — |
| [SRC-03FF422A16-L000227](../../scripts/score_answer_quality_reviews.py#L227) | 227 | `"    args = parser.parse_args(argv)"` | — |
| [SRC-03FF422A16-L000228](../../scripts/score_answer_quality_reviews.py#L228) | 228 | `""` | — |
| [SRC-03FF422A16-L000229](../../scripts/score_answer_quality_reviews.py#L229) | 229 | `"    try:"` | — |
| [SRC-03FF422A16-L000230](../../scripts/score_answer_quality_reviews.py#L230) | 230 | `"        reviews = load_json_object(args.reviews)"` | — |
| [SRC-03FF422A16-L000231](../../scripts/score_answer_quality_reviews.py#L231) | 231 | `"        corpus = load_json_object(args.corpus)"` | — |
| [SRC-03FF422A16-L000232](../../scripts/score_answer_quality_reviews.py#L232) | 232 | `"        summary = summarize_reviews(reviews, corpus)"` | — |
| [SRC-03FF422A16-L000233](../../scripts/score_answer_quality_reviews.py#L233) | 233 | `"    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:"` | — |
| [SRC-03FF422A16-L000234](../../scripts/score_answer_quality_reviews.py#L234) | 234 | `"        print(\"REVIEW SCORECARD INVALID: \" + str(exc), file=sys.stderr)"` | — |
| [SRC-03FF422A16-L000235](../../scripts/score_answer_quality_reviews.py#L235) | 235 | `"        return 2"` | — |
| [SRC-03FF422A16-L000236](../../scripts/score_answer_quality_reviews.py#L236) | 236 | `""` | — |
| [SRC-03FF422A16-L000237](../../scripts/score_answer_quality_reviews.py#L237) | 237 | `"    output = json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True)"` | — |
| [SRC-03FF422A16-L000238](../../scripts/score_answer_quality_reviews.py#L238) | 238 | `"    if args.out:"` | — |
| [SRC-03FF422A16-L000239](../../scripts/score_answer_quality_reviews.py#L239) | 239 | `"        args.out.write_text(output + \"\\n\", encoding=\"utf-8\")"` | — |
| [SRC-03FF422A16-L000240](../../scripts/score_answer_quality_reviews.py#L240) | 240 | `"    print(output)"` | — |
| [SRC-03FF422A16-L000241](../../scripts/score_answer_quality_reviews.py#L241) | 241 | `"    return 0"` | — |
| [SRC-03FF422A16-L000242](../../scripts/score_answer_quality_reviews.py#L242) | 242 | `""` | — |
| [SRC-03FF422A16-L000243](../../scripts/score_answer_quality_reviews.py#L243) | 243 | `""` | — |
| [SRC-03FF422A16-L000244](../../scripts/score_answer_quality_reviews.py#L244) | 244 | `"if __name__ == \"__main__\":"` | — |
| [SRC-03FF422A16-L000245](../../scripts/score_answer_quality_reviews.py#L245) | 245 | `"    raise SystemExit(main())"` | — |
## ملفات أخرى

### FILE-547CAF1FE3 — [scripts/sqlite_backup_restore.py](../../scripts/sqlite_backup_restore.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-547CAF1FE3-L000001](../../scripts/sqlite_backup_restore.py#L1) | 1 | `"#!/usr/bin/env python3"` | — |
| [SRC-547CAF1FE3-L000002](../../scripts/sqlite_backup_restore.py#L2) | 2 | `"\"\"\"Create and restore verified, non-overwriting snapshots of Omarai's SQLite lead DB.\"\"\""` | — |
| [SRC-547CAF1FE3-L000003](../../scripts/sqlite_backup_restore.py#L3) | 3 | `"from __future__ import annotations"` | — |
| [SRC-547CAF1FE3-L000004](../../scripts/sqlite_backup_restore.py#L4) | 4 | `""` | — |
| [SRC-547CAF1FE3-L000005](../../scripts/sqlite_backup_restore.py#L5) | 5 | `"import argparse"` | — |
| [SRC-547CAF1FE3-L000006](../../scripts/sqlite_backup_restore.py#L6) | 6 | `"from contextlib import closing"` | — |
| [SRC-547CAF1FE3-L000007](../../scripts/sqlite_backup_restore.py#L7) | 7 | `"import json"` | — |
| [SRC-547CAF1FE3-L000008](../../scripts/sqlite_backup_restore.py#L8) | 8 | `"import os"` | — |
| [SRC-547CAF1FE3-L000009](../../scripts/sqlite_backup_restore.py#L9) | 9 | `"import sqlite3"` | — |
| [SRC-547CAF1FE3-L000010](../../scripts/sqlite_backup_restore.py#L10) | 10 | `"import sys"` | — |
| [SRC-547CAF1FE3-L000011](../../scripts/sqlite_backup_restore.py#L11) | 11 | `"from pathlib import Path"` | — |
| [SRC-547CAF1FE3-L000012](../../scripts/sqlite_backup_restore.py#L12) | 12 | `"from typing import Any"` | — |
| [SRC-547CAF1FE3-L000013](../../scripts/sqlite_backup_restore.py#L13) | 13 | `""` | — |
| [SRC-547CAF1FE3-L000014](../../scripts/sqlite_backup_restore.py#L14) | 14 | `""` | — |
| [SRC-547CAF1FE3-L000015](../../scripts/sqlite_backup_restore.py#L15) | 15 | `"class BackupError(RuntimeError):"` | — |
| [SRC-547CAF1FE3-L000016](../../scripts/sqlite_backup_restore.py#L16) | 16 | `"    \"\"\"Raised when a backup/restore operation cannot be proven safe.\"\"\""` | — |
| [SRC-547CAF1FE3-L000017](../../scripts/sqlite_backup_restore.py#L17) | 17 | `""` | — |
| [SRC-547CAF1FE3-L000018](../../scripts/sqlite_backup_restore.py#L18) | 18 | `""` | — |
| [SRC-547CAF1FE3-L000019](../../scripts/sqlite_backup_restore.py#L19) | 19 | `"def _open_read_only(path: Path) -> sqlite3.Connection:"` | — |
| [SRC-547CAF1FE3-L000020](../../scripts/sqlite_backup_restore.py#L20) | 20 | `"    \"\"\"Open an existing SQLite database without accidentally creating a missing source.\"\"\""` | — |
| [SRC-547CAF1FE3-L000021](../../scripts/sqlite_backup_restore.py#L21) | 21 | `"    try:"` | — |
| [SRC-547CAF1FE3-L000022](../../scripts/sqlite_backup_restore.py#L22) | 22 | `"        return sqlite3.connect(f\"{path.as_uri()}?mode=ro\", uri=True, timeout=10)"` | — |
| [SRC-547CAF1FE3-L000023](../../scripts/sqlite_backup_restore.py#L23) | 23 | `"    except (OSError, sqlite3.Error) as exc:"` | — |
| [SRC-547CAF1FE3-L000024](../../scripts/sqlite_backup_restore.py#L24) | 24 | `"        raise BackupError(f\"cannot open SQLite source: {type(exc).__name__}\") from exc"` | — |
| [SRC-547CAF1FE3-L000025](../../scripts/sqlite_backup_restore.py#L25) | 25 | `""` | — |
| [SRC-547CAF1FE3-L000026](../../scripts/sqlite_backup_restore.py#L26) | 26 | `""` | — |
| [SRC-547CAF1FE3-L000027](../../scripts/sqlite_backup_restore.py#L27) | 27 | `"def _validate_omarai_database(db: sqlite3.Connection) -> int:"` | — |
| [SRC-547CAF1FE3-L000028](../../scripts/sqlite_backup_restore.py#L28) | 28 | `"    \"\"\"Require a healthy SQLite file containing the Omarai leads table.\"\"\""` | — |
| [SRC-547CAF1FE3-L000029](../../scripts/sqlite_backup_restore.py#L29) | 29 | `"    try:"` | — |
| [SRC-547CAF1FE3-L000030](../../scripts/sqlite_backup_restore.py#L30) | 30 | `"        integrity_row = db.execute(\"PRAGMA integrity_check\").fetchone()"` | — |
| [SRC-547CAF1FE3-L000031](../../scripts/sqlite_backup_restore.py#L31) | 31 | `"        if not integrity_row or integrity_row[0] != \"ok\":"` | — |
| [SRC-547CAF1FE3-L000032](../../scripts/sqlite_backup_restore.py#L32) | 32 | `"            raise BackupError(\"SQLite integrity_check did not return ok\")"` | — |
| [SRC-547CAF1FE3-L000033](../../scripts/sqlite_backup_restore.py#L33) | 33 | `"        table_row = db.execute("` | — |
| [SRC-547CAF1FE3-L000034](../../scripts/sqlite_backup_restore.py#L34) | 34 | `"            \"SELECT 1 FROM sqlite_master WHERE type='table' AND name='leads'\""` | — |
| [SRC-547CAF1FE3-L000035](../../scripts/sqlite_backup_restore.py#L35) | 35 | `"        ).fetchone()"` | — |
| [SRC-547CAF1FE3-L000036](../../scripts/sqlite_backup_restore.py#L36) | 36 | `"        if not table_row:"` | — |
| [SRC-547CAF1FE3-L000037](../../scripts/sqlite_backup_restore.py#L37) | 37 | `"            raise BackupError(\"source is not an Omarai leads database\")"` | — |
| [SRC-547CAF1FE3-L000038](../../scripts/sqlite_backup_restore.py#L38) | 38 | `"        count_row = db.execute(\"SELECT COUNT(*) FROM leads\").fetchone()"` | — |
| [SRC-547CAF1FE3-L000039](../../scripts/sqlite_backup_restore.py#L39) | 39 | `"        if not count_row:"` | — |
| [SRC-547CAF1FE3-L000040](../../scripts/sqlite_backup_restore.py#L40) | 40 | `"            raise BackupError(\"could not count leads in database\")"` | — |
| [SRC-547CAF1FE3-L000041](../../scripts/sqlite_backup_restore.py#L41) | 41 | `"        return int(count_row[0])"` | — |
| [SRC-547CAF1FE3-L000042](../../scripts/sqlite_backup_restore.py#L42) | 42 | `"    except sqlite3.Error as exc:"` | — |
| [SRC-547CAF1FE3-L000043](../../scripts/sqlite_backup_restore.py#L43) | 43 | `"        raise BackupError(f\"SQLite validation failed: {type(exc).__name__}\") from exc"` | — |
| [SRC-547CAF1FE3-L000044](../../scripts/sqlite_backup_restore.py#L44) | 44 | `""` | — |
| [SRC-547CAF1FE3-L000045](../../scripts/sqlite_backup_restore.py#L45) | 45 | `""` | — |
| [SRC-547CAF1FE3-L000046](../../scripts/sqlite_backup_restore.py#L46) | 46 | `"def _create_destination_exclusively(path: Path) -> None:"` | — |
| [SRC-547CAF1FE3-L000047](../../scripts/sqlite_backup_restore.py#L47) | 47 | `"    \"\"\"Create a new destination without overwriting an existing file or following its symlink.\"\"\""` | — |
| [SRC-547CAF1FE3-L000048](../../scripts/sqlite_backup_restore.py#L48) | 48 | `"    path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-547CAF1FE3-L000049](../../scripts/sqlite_backup_restore.py#L49) | 49 | `"    descriptor = os.open(path, os.O_CREAT \| os.O_EXCL \| os.O_WRONLY, 0o600)"` | — |
| [SRC-547CAF1FE3-L000050](../../scripts/sqlite_backup_restore.py#L50) | 50 | `"    os.close(descriptor)"` | — |
| [SRC-547CAF1FE3-L000051](../../scripts/sqlite_backup_restore.py#L51) | 51 | `"    try:"` | — |
| [SRC-547CAF1FE3-L000052](../../scripts/sqlite_backup_restore.py#L52) | 52 | `"        path.chmod(0o600)"` | — |
| [SRC-547CAF1FE3-L000053](../../scripts/sqlite_backup_restore.py#L53) | 53 | `"    except OSError:"` | — |
| [SRC-547CAF1FE3-L000054](../../scripts/sqlite_backup_restore.py#L54) | 54 | `"        # The exclusive-create mode remains the primary permission setting; do not"` | — |
| [SRC-547CAF1FE3-L000055](../../scripts/sqlite_backup_restore.py#L55) | 55 | `"        # discard a completed backup solely because chmod is unavailable on a host."` | — |
| [SRC-547CAF1FE3-L000056](../../scripts/sqlite_backup_restore.py#L56) | 56 | `"        pass"` | — |
| [SRC-547CAF1FE3-L000057](../../scripts/sqlite_backup_restore.py#L57) | 57 | `""` | — |
| [SRC-547CAF1FE3-L000058](../../scripts/sqlite_backup_restore.py#L58) | 58 | `""` | — |
| [SRC-547CAF1FE3-L000059](../../scripts/sqlite_backup_restore.py#L59) | 59 | `"def _copy_verified_database(source: str \| Path, destination: str \| Path) -> dict[str, Any]:"` | — |
| [SRC-547CAF1FE3-L000060](../../scripts/sqlite_backup_restore.py#L60) | 60 | `"    source_path = Path(source).expanduser().resolve(strict=True)"` | — |
| [SRC-547CAF1FE3-L000061](../../scripts/sqlite_backup_restore.py#L61) | 61 | `"    requested_destination = Path(destination).expanduser()"` | — |
| [SRC-547CAF1FE3-L000062](../../scripts/sqlite_backup_restore.py#L62) | 62 | `"    destination_path = requested_destination.resolve(strict=False)"` | — |
| [SRC-547CAF1FE3-L000063](../../scripts/sqlite_backup_restore.py#L63) | 63 | `""` | — |
| [SRC-547CAF1FE3-L000064](../../scripts/sqlite_backup_restore.py#L64) | 64 | `"    if not source_path.is_file():"` | — |
| [SRC-547CAF1FE3-L000065](../../scripts/sqlite_backup_restore.py#L65) | 65 | `"        raise BackupError(\"source must be an existing regular file\")"` | — |
| [SRC-547CAF1FE3-L000066](../../scripts/sqlite_backup_restore.py#L66) | 66 | `"    if source_path == destination_path:"` | — |
| [SRC-547CAF1FE3-L000067](../../scripts/sqlite_backup_restore.py#L67) | 67 | `"        raise BackupError(\"source and destination must be different paths\")"` | — |
| [SRC-547CAF1FE3-L000068](../../scripts/sqlite_backup_restore.py#L68) | 68 | `"    # Check the user-supplied path before resolving it so a dangling symlink is"` | — |
| [SRC-547CAF1FE3-L000069](../../scripts/sqlite_backup_restore.py#L69) | 69 | `"    # never mistaken for an absent destination and followed to a new target."` | — |
| [SRC-547CAF1FE3-L000070](../../scripts/sqlite_backup_restore.py#L70) | 70 | `"    if requested_destination.exists() or requested_destination.is_symlink() or destination_path.exists():"` | — |
| [SRC-547CAF1FE3-L000071](../../scripts/sqlite_backup_restore.py#L71) | 71 | `"        raise FileExistsError(f\"destination already exists: {requested_destination}\")"` | — |
| [SRC-547CAF1FE3-L000072](../../scripts/sqlite_backup_restore.py#L72) | 72 | `""` | — |
| [SRC-547CAF1FE3-L000073](../../scripts/sqlite_backup_restore.py#L73) | 73 | `"    # Validate the source before creating anything at the destination."` | — |
| [SRC-547CAF1FE3-L000074](../../scripts/sqlite_backup_restore.py#L74) | 74 | `"    with closing(_open_read_only(source_path)) as source_db:"` | — |
| [SRC-547CAF1FE3-L000075](../../scripts/sqlite_backup_restore.py#L75) | 75 | `"        source_count = _validate_omarai_database(source_db)"` | — |
| [SRC-547CAF1FE3-L000076](../../scripts/sqlite_backup_restore.py#L76) | 76 | `"        _create_destination_exclusively(destination_path)"` | — |
| [SRC-547CAF1FE3-L000077](../../scripts/sqlite_backup_restore.py#L77) | 77 | `"        try:"` | — |
| [SRC-547CAF1FE3-L000078](../../scripts/sqlite_backup_restore.py#L78) | 78 | `"            with closing(sqlite3.connect(destination_path, timeout=10)) as destination_db:"` | — |
| [SRC-547CAF1FE3-L000079](../../scripts/sqlite_backup_restore.py#L79) | 79 | `"                source_db.backup(destination_db)"` | — |
| [SRC-547CAF1FE3-L000080](../../scripts/sqlite_backup_restore.py#L80) | 80 | `"                destination_db.commit()"` | — |
| [SRC-547CAF1FE3-L000081](../../scripts/sqlite_backup_restore.py#L81) | 81 | `"                restored_count = _validate_omarai_database(destination_db)"` | — |
| [SRC-547CAF1FE3-L000082](../../scripts/sqlite_backup_restore.py#L82) | 82 | `"                if restored_count != source_count:"` | — |
| [SRC-547CAF1FE3-L000083](../../scripts/sqlite_backup_restore.py#L83) | 83 | `"                    raise BackupError("` | — |
| [SRC-547CAF1FE3-L000084](../../scripts/sqlite_backup_restore.py#L84) | 84 | `"                        \"lead count changed during snapshot: \""` | — |
| [SRC-547CAF1FE3-L000085](../../scripts/sqlite_backup_restore.py#L85) | 85 | `"                        f\"source={source_count}, destination={restored_count}\""` | — |
| [SRC-547CAF1FE3-L000086](../../scripts/sqlite_backup_restore.py#L86) | 86 | `"                    )"` | — |
| [SRC-547CAF1FE3-L000087](../../scripts/sqlite_backup_restore.py#L87) | 87 | `"        except Exception:"` | — |
| [SRC-547CAF1FE3-L000088](../../scripts/sqlite_backup_restore.py#L88) | 88 | `"            # Remove only the destination created by this operation; never touch source."` | — |
| [SRC-547CAF1FE3-L000089](../../scripts/sqlite_backup_restore.py#L89) | 89 | `"            try:"` | — |
| [SRC-547CAF1FE3-L000090](../../scripts/sqlite_backup_restore.py#L90) | 90 | `"                destination_path.unlink(missing_ok=True)"` | — |
| [SRC-547CAF1FE3-L000091](../../scripts/sqlite_backup_restore.py#L91) | 91 | `"            except OSError:"` | — |
| [SRC-547CAF1FE3-L000092](../../scripts/sqlite_backup_restore.py#L92) | 92 | `"                pass"` | — |
| [SRC-547CAF1FE3-L000093](../../scripts/sqlite_backup_restore.py#L93) | 93 | `"            raise"` | — |
| [SRC-547CAF1FE3-L000094](../../scripts/sqlite_backup_restore.py#L94) | 94 | `""` | — |
| [SRC-547CAF1FE3-L000095](../../scripts/sqlite_backup_restore.py#L95) | 95 | `"    return {"` | — |
| [SRC-547CAF1FE3-L000096](../../scripts/sqlite_backup_restore.py#L96) | 96 | `"        \"result\": \"passed\","` | — |
| [SRC-547CAF1FE3-L000097](../../scripts/sqlite_backup_restore.py#L97) | 97 | `"        \"source\": str(source_path),"` | — |
| [SRC-547CAF1FE3-L000098](../../scripts/sqlite_backup_restore.py#L98) | 98 | `"        \"destination\": str(destination_path),"` | — |
| [SRC-547CAF1FE3-L000099](../../scripts/sqlite_backup_restore.py#L99) | 99 | `"        \"integrity_check\": \"ok\","` | — |
| [SRC-547CAF1FE3-L000100](../../scripts/sqlite_backup_restore.py#L100) | 100 | `"        \"lead_count\": source_count,"` | — |
| [SRC-547CAF1FE3-L000101](../../scripts/sqlite_backup_restore.py#L101) | 101 | `"        \"overwrite\": False,"` | — |
| [SRC-547CAF1FE3-L000102](../../scripts/sqlite_backup_restore.py#L102) | 102 | `"    }"` | — |
| [SRC-547CAF1FE3-L000103](../../scripts/sqlite_backup_restore.py#L103) | 103 | `""` | — |
| [SRC-547CAF1FE3-L000104](../../scripts/sqlite_backup_restore.py#L104) | 104 | `""` | — |
| [SRC-547CAF1FE3-L000105](../../scripts/sqlite_backup_restore.py#L105) | 105 | `"def backup_database(source: str \| Path, destination: str \| Path) -> dict[str, Any]:"` | — |
| [SRC-547CAF1FE3-L000106](../../scripts/sqlite_backup_restore.py#L106) | 106 | `"    \"\"\"Create a consistent SQLite snapshot of a healthy Omarai leads database.\"\"\""` | — |
| [SRC-547CAF1FE3-L000107](../../scripts/sqlite_backup_restore.py#L107) | 107 | `"    return _copy_verified_database(source, destination)"` | — |
| [SRC-547CAF1FE3-L000108](../../scripts/sqlite_backup_restore.py#L108) | 108 | `""` | — |
| [SRC-547CAF1FE3-L000109](../../scripts/sqlite_backup_restore.py#L109) | 109 | `""` | — |
| [SRC-547CAF1FE3-L000110](../../scripts/sqlite_backup_restore.py#L110) | 110 | `"def restore_database(backup: str \| Path, destination: str \| Path) -> dict[str, Any]:"` | — |
| [SRC-547CAF1FE3-L000111](../../scripts/sqlite_backup_restore.py#L111) | 111 | `"    \"\"\"Restore a snapshot into a new destination; existing files are never overwritten.\"\"\""` | — |
| [SRC-547CAF1FE3-L000112](../../scripts/sqlite_backup_restore.py#L112) | 112 | `"    return _copy_verified_database(backup, destination)"` | — |
| [SRC-547CAF1FE3-L000113](../../scripts/sqlite_backup_restore.py#L113) | 113 | `""` | — |
| [SRC-547CAF1FE3-L000114](../../scripts/sqlite_backup_restore.py#L114) | 114 | `""` | — |
| [SRC-547CAF1FE3-L000115](../../scripts/sqlite_backup_restore.py#L115) | 115 | `"def main() -> int:"` | — |
| [SRC-547CAF1FE3-L000116](../../scripts/sqlite_backup_restore.py#L116) | 116 | `"    parser = argparse.ArgumentParser("` | — |
| [SRC-547CAF1FE3-L000117](../../scripts/sqlite_backup_restore.py#L117) | 117 | `"        description=("` | — |
| [SRC-547CAF1FE3-L000118](../../scripts/sqlite_backup_restore.py#L118) | 118 | `"            \"Back up or restore an Omarai SQLite leads database. \""` | — |
| [SRC-547CAF1FE3-L000119](../../scripts/sqlite_backup_restore.py#L119) | 119 | `"            \"The destination must not already exist.\""` | — |
| [SRC-547CAF1FE3-L000120](../../scripts/sqlite_backup_restore.py#L120) | 120 | `"        )"` | — |
| [SRC-547CAF1FE3-L000121](../../scripts/sqlite_backup_restore.py#L121) | 121 | `"    )"` | — |
| [SRC-547CAF1FE3-L000122](../../scripts/sqlite_backup_restore.py#L122) | 122 | `"    subparsers = parser.add_subparsers(dest=\"command\", required=True)"` | — |
| [SRC-547CAF1FE3-L000123](../../scripts/sqlite_backup_restore.py#L123) | 123 | `"    backup_parser = subparsers.add_parser(\"backup\", help=\"create a verified snapshot\")"` | — |
| [SRC-547CAF1FE3-L000124](../../scripts/sqlite_backup_restore.py#L124) | 124 | `"    backup_parser.add_argument(\"source\", help=\"existing Omarai SQLite database path\")"` | — |
| [SRC-547CAF1FE3-L000125](../../scripts/sqlite_backup_restore.py#L125) | 125 | `"    backup_parser.add_argument(\"destination\", help=\"new backup path; must not exist\")"` | — |
| [SRC-547CAF1FE3-L000126](../../scripts/sqlite_backup_restore.py#L126) | 126 | `"    restore_parser = subparsers.add_parser(\"restore\", help=\"restore to a new database file\")"` | — |
| [SRC-547CAF1FE3-L000127](../../scripts/sqlite_backup_restore.py#L127) | 127 | `"    restore_parser.add_argument(\"source\", help=\"existing verified backup path\")"` | — |
| [SRC-547CAF1FE3-L000128](../../scripts/sqlite_backup_restore.py#L128) | 128 | `"    restore_parser.add_argument(\"destination\", help=\"new restore path; must not exist\")"` | — |
| [SRC-547CAF1FE3-L000129](../../scripts/sqlite_backup_restore.py#L129) | 129 | `"    args = parser.parse_args()"` | — |
| [SRC-547CAF1FE3-L000130](../../scripts/sqlite_backup_restore.py#L130) | 130 | `""` | — |
