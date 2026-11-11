# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **038**
- سجلات الأسطر: **800**
- النطاق: SRC-A8360B1B03-L000392 إلى SRC-4FFD5AFC54-L000545
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## ملفات أخرى

### FILE-A8360B1B03 — [scripts/hosted_smoke_test.py](../../scripts/hosted_smoke_test.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-A8360B1B03-L000392](../../scripts/hosted_smoke_test.py#L392) | 392 | `"            \"max_page_fetches\": HOSTED_SMOKE_BUDGET_MAX[\"page_fetches\"],"` | — |
| [SRC-A8360B1B03-L000393](../../scripts/hosted_smoke_test.py#L393) | 393 | `"            \"tool_calls\": HOSTED_SMOKE_BUDGET_MAX[\"tool_calls\"],"` | — |
| [SRC-A8360B1B03-L000394](../../scripts/hosted_smoke_test.py#L394) | 394 | `"            \"note\": \"Server-enforced per-request ceilings; operator settings may be stricter.\","` | — |
| [SRC-A8360B1B03-L000395](../../scripts/hosted_smoke_test.py#L395) | 395 | `"        },"` | — |
| [SRC-A8360B1B03-L000396](../../scripts/hosted_smoke_test.py#L396) | 396 | `"    }"` | — |
| [SRC-A8360B1B03-L000397](../../scripts/hosted_smoke_test.py#L397) | 397 | `"    status, answer = request_json("` | — |
| [SRC-A8360B1B03-L000398](../../scripts/hosted_smoke_test.py#L398) | 398 | `"        f\"{origin}/api/agent\", token=token, timeout=timeout,"` | — |
| [SRC-A8360B1B03-L000399](../../scripts/hosted_smoke_test.py#L399) | 399 | `"        payload={"` | — |
| [SRC-A8360B1B03-L000400](../../scripts/hosted_smoke_test.py#L400) | 400 | `"            \"question\": LIVE_TEST_QUESTION,"` | — |
| [SRC-A8360B1B03-L000401](../../scripts/hosted_smoke_test.py#L401) | 401 | `"            \"history\": [], \"mode\": \"auto\", \"request_profile\": \"hosted_smoke\","` | — |
| [SRC-A8360B1B03-L000402](../../scripts/hosted_smoke_test.py#L402) | 402 | `"        },"` | — |
| [SRC-A8360B1B03-L000403](../../scripts/hosted_smoke_test.py#L403) | 403 | `"    )"` | — |
| [SRC-A8360B1B03-L000404](../../scripts/hosted_smoke_test.py#L404) | 404 | `"    if status != 200 or not answer:"` | — |
| [SRC-A8360B1B03-L000405](../../scripts/hosted_smoke_test.py#L405) | 405 | `"        if isinstance(answer, dict) and isinstance(answer.get(\"_smoke_http\"), dict):"` | — |
| [SRC-A8360B1B03-L000406](../../scripts/hosted_smoke_test.py#L406) | 406 | `"            partial_report[\"http_response\"] = answer[\"_smoke_http\"]"` | — |
| [SRC-A8360B1B03-L000407](../../scripts/hosted_smoke_test.py#L407) | 407 | `"        raise SmokeError(f\"Authenticated agent request failed (HTTP {status}).\", partial_report)"` | — |
| [SRC-A8360B1B03-L000408](../../scripts/hosted_smoke_test.py#L408) | 408 | `"    sources = answer.get(\"sources\")"` | — |
| [SRC-A8360B1B03-L000409](../../scripts/hosted_smoke_test.py#L409) | 409 | `"    usable = ["` | — |
| [SRC-A8360B1B03-L000410](../../scripts/hosted_smoke_test.py#L410) | 410 | `"        item for item in sources if isinstance(item, dict)"` | — |
| [SRC-A8360B1B03-L000411](../../scripts/hosted_smoke_test.py#L411) | 411 | `"        and isinstance(item.get(\"url\"), str)"` | — |
| [SRC-A8360B1B03-L000412](../../scripts/hosted_smoke_test.py#L412) | 412 | `"        and urllib.parse.urlsplit(item[\"url\"]).scheme in {\"http\", \"https\"}"` | — |
| [SRC-A8360B1B03-L000413](../../scripts/hosted_smoke_test.py#L413) | 413 | `"        and urllib.parse.urlsplit(item[\"url\"]).hostname"` | — |
| [SRC-A8360B1B03-L000414](../../scripts/hosted_smoke_test.py#L414) | 414 | `"    ] if isinstance(sources, list) else []"` | — |
| [SRC-A8360B1B03-L000415](../../scripts/hosted_smoke_test.py#L415) | 415 | `"    search_report = answer.get(\"search_report\")"` | — |
| [SRC-A8360B1B03-L000416](../../scripts/hosted_smoke_test.py#L416) | 416 | `"    raw_answer = answer.get(\"answer\")"` | — |
| [SRC-A8360B1B03-L000417](../../scripts/hosted_smoke_test.py#L417) | 417 | `"    answer_text = raw_answer.strip() if isinstance(raw_answer, str) else \"\""` | — |
| [SRC-A8360B1B03-L000418](../../scripts/hosted_smoke_test.py#L418) | 418 | `"    source_records = ["` | — |
| [SRC-A8360B1B03-L000419](../../scripts/hosted_smoke_test.py#L419) | 419 | `"        {"` | — |
| [SRC-A8360B1B03-L000420](../../scripts/hosted_smoke_test.py#L420) | 420 | `"            \"title\": str(item.get(\"title\") or \"\")[:300],"` | — |
| [SRC-A8360B1B03-L000421](../../scripts/hosted_smoke_test.py#L421) | 421 | `"            \"url\": str(item.get(\"url\") or \"\")[:2048],"` | — |
| [SRC-A8360B1B03-L000422](../../scripts/hosted_smoke_test.py#L422) | 422 | `"            \"provider\": str(item.get(\"provider\") or \"\")[:80],"` | — |
| [SRC-A8360B1B03-L000423](../../scripts/hosted_smoke_test.py#L423) | 423 | `"            \"snippet\": str(item.get(\"snippet\") or \"\")[:1200],"` | — |
| [SRC-A8360B1B03-L000424](../../scripts/hosted_smoke_test.py#L424) | 424 | `"            \"published_at\": str(item.get(\"published_at\") or \"\")[:100],"` | — |
| [SRC-A8360B1B03-L000425](../../scripts/hosted_smoke_test.py#L425) | 425 | `"        }"` | — |
| [SRC-A8360B1B03-L000426](../../scripts/hosted_smoke_test.py#L426) | 426 | `"        for item in usable"` | — |
| [SRC-A8360B1B03-L000427](../../scripts/hosted_smoke_test.py#L427) | 427 | `"    ]"` | — |
| [SRC-A8360B1B03-L000428](../../scripts/hosted_smoke_test.py#L428) | 428 | `"    transcript = {"` | — |
| [SRC-A8360B1B03-L000429](../../scripts/hosted_smoke_test.py#L429) | 429 | `"        \"case_id\": \"sales_intent_fire_alarm_egypt\","` | — |
| [SRC-A8360B1B03-L000430](../../scripts/hosted_smoke_test.py#L430) | 430 | `"        \"question\": LIVE_TEST_QUESTION,"` | — |
| [SRC-A8360B1B03-L000431](../../scripts/hosted_smoke_test.py#L431) | 431 | `"        \"answer\": answer_text,"` | — |
| [SRC-A8360B1B03-L000432](../../scripts/hosted_smoke_test.py#L432) | 432 | `"        \"used_web_search\": answer.get(\"used_web_search\") is True,"` | — |
| [SRC-A8360B1B03-L000433](../../scripts/hosted_smoke_test.py#L433) | 433 | `"        \"used_language_model\": answer.get(\"used_language_model\") is True,"` | — |
| [SRC-A8360B1B03-L000434](../../scripts/hosted_smoke_test.py#L434) | 434 | `"        \"sources\": source_records,"` | — |
| [SRC-A8360B1B03-L000435](../../scripts/hosted_smoke_test.py#L435) | 435 | `"        \"pipeline_completion_status\": ("` | — |
| [SRC-A8360B1B03-L000436](../../scripts/hosted_smoke_test.py#L436) | 436 | `"            search_report.get(\"pipeline_completion_status\")"` | — |
| [SRC-A8360B1B03-L000437](../../scripts/hosted_smoke_test.py#L437) | 437 | `"            if isinstance(search_report, dict) else None"` | — |
| [SRC-A8360B1B03-L000438](../../scripts/hosted_smoke_test.py#L438) | 438 | `"        ),"` | — |
| [SRC-A8360B1B03-L000439](../../scripts/hosted_smoke_test.py#L439) | 439 | `"        \"answer_evidence_status\": answer.get(\"answer_evidence_status\"),"` | — |
| [SRC-A8360B1B03-L000440](../../scripts/hosted_smoke_test.py#L440) | 440 | `"        \"semantic_claim_verification_status\": ("` | — |
| [SRC-A8360B1B03-L000441](../../scripts/hosted_smoke_test.py#L441) | 441 | `"            search_report.get(\"semantic_claim_verification\", {}).get(\"status\")"` | — |
| [SRC-A8360B1B03-L000442](../../scripts/hosted_smoke_test.py#L442) | 442 | `"            if isinstance(search_report, dict)"` | — |
| [SRC-A8360B1B03-L000443](../../scripts/hosted_smoke_test.py#L443) | 443 | `"            and isinstance(search_report.get(\"semantic_claim_verification\"), dict)"` | — |
| [SRC-A8360B1B03-L000444](../../scripts/hosted_smoke_test.py#L444) | 444 | `"            else None"` | — |
| [SRC-A8360B1B03-L000445](../../scripts/hosted_smoke_test.py#L445) | 445 | `"        ),"` | — |
| [SRC-A8360B1B03-L000446](../../scripts/hosted_smoke_test.py#L446) | 446 | `"        \"request_budget\": answer.get(\"request_budget\"),"` | — |
| [SRC-A8360B1B03-L000447](../../scripts/hosted_smoke_test.py#L447) | 447 | `"    }"` | — |
| [SRC-A8360B1B03-L000448](../../scripts/hosted_smoke_test.py#L448) | 448 | `"    partial_report[\"transcript\"] = [transcript]"` | — |
| [SRC-A8360B1B03-L000449](../../scripts/hosted_smoke_test.py#L449) | 449 | `"    if not answer_text:"` | — |
| [SRC-A8360B1B03-L000450](../../scripts/hosted_smoke_test.py#L450) | 450 | `"        raise SmokeError(\"Agent request returned an empty or whitespace-only answer.\", partial_report)"` | — |
| [SRC-A8360B1B03-L000451](../../scripts/hosted_smoke_test.py#L451) | 451 | `"    if answer.get(\"used_web_search\") is not True or not usable:"` | — |
| [SRC-A8360B1B03-L000452](../../scripts/hosted_smoke_test.py#L452) | 452 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000453](../../scripts/hosted_smoke_test.py#L453) | 453 | `"            \"Agent request did not return a live web search with usable source URLs.\","` | — |
| [SRC-A8360B1B03-L000454](../../scripts/hosted_smoke_test.py#L454) | 454 | `"            partial_report,"` | — |
| [SRC-A8360B1B03-L000455](../../scripts/hosted_smoke_test.py#L455) | 455 | `"        )"` | — |
| [SRC-A8360B1B03-L000456](../../scripts/hosted_smoke_test.py#L456) | 456 | `"    if answer.get(\"used_language_model\") is not True:"` | — |
| [SRC-A8360B1B03-L000457](../../scripts/hosted_smoke_test.py#L457) | 457 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000458](../../scripts/hosted_smoke_test.py#L458) | 458 | `"            \"Agent request did not confirm that a language model was used.\","` | — |
| [SRC-A8360B1B03-L000459](../../scripts/hosted_smoke_test.py#L459) | 459 | `"            partial_report,"` | — |
| [SRC-A8360B1B03-L000460](../../scripts/hosted_smoke_test.py#L460) | 460 | `"        )"` | — |
| [SRC-A8360B1B03-L000461](../../scripts/hosted_smoke_test.py#L461) | 461 | `"    request_budget = answer.get(\"request_budget\")"` | — |
| [SRC-A8360B1B03-L000462](../../scripts/hosted_smoke_test.py#L462) | 462 | `"    if not isinstance(request_budget, dict) or request_budget.get(\"profile\") != \"hosted_smoke\":"` | — |
| [SRC-A8360B1B03-L000463](../../scripts/hosted_smoke_test.py#L463) | 463 | `"        raise SmokeError(\"Agent response did not confirm the hosted_smoke request budget profile.\", partial_report)"` | — |
| [SRC-A8360B1B03-L000464](../../scripts/hosted_smoke_test.py#L464) | 464 | `"    budget_limits = request_budget.get(\"limits\")"` | — |
| [SRC-A8360B1B03-L000465](../../scripts/hosted_smoke_test.py#L465) | 465 | `"    budget_counts = request_budget.get(\"counts\")"` | — |
| [SRC-A8360B1B03-L000466](../../scripts/hosted_smoke_test.py#L466) | 466 | `"    if not isinstance(budget_limits, dict) or not isinstance(budget_counts, dict):"` | — |
| [SRC-A8360B1B03-L000467](../../scripts/hosted_smoke_test.py#L467) | 467 | `"        raise SmokeError(\"Agent response omitted request-budget limits or counters.\", partial_report)"` | — |
| [SRC-A8360B1B03-L000468](../../scripts/hosted_smoke_test.py#L468) | 468 | `"    for resource, maximum in HOSTED_SMOKE_BUDGET_MAX.items():"` | — |
| [SRC-A8360B1B03-L000469](../../scripts/hosted_smoke_test.py#L469) | 469 | `"        limit = budget_limits.get(resource)"` | — |
| [SRC-A8360B1B03-L000470](../../scripts/hosted_smoke_test.py#L470) | 470 | `"        count = budget_counts.get(resource)"` | — |
| [SRC-A8360B1B03-L000471](../../scripts/hosted_smoke_test.py#L471) | 471 | `"        if ("` | — |
| [SRC-A8360B1B03-L000472](../../scripts/hosted_smoke_test.py#L472) | 472 | `"            isinstance(limit, bool) or not isinstance(limit, int)"` | — |
| [SRC-A8360B1B03-L000473](../../scripts/hosted_smoke_test.py#L473) | 473 | `"            or isinstance(count, bool) or not isinstance(count, int)"` | — |
| [SRC-A8360B1B03-L000474](../../scripts/hosted_smoke_test.py#L474) | 474 | `"            or limit < 0 or limit > maximum"` | — |
| [SRC-A8360B1B03-L000475](../../scripts/hosted_smoke_test.py#L475) | 475 | `"            or count < 0 or count > limit"` | — |
| [SRC-A8360B1B03-L000476](../../scripts/hosted_smoke_test.py#L476) | 476 | `"        ):"` | — |
| [SRC-A8360B1B03-L000477](../../scripts/hosted_smoke_test.py#L477) | 477 | `"            raise SmokeError("` | — |
| [SRC-A8360B1B03-L000478](../../scripts/hosted_smoke_test.py#L478) | 478 | `"                f\"Agent hosted_smoke request budget is missing, exceeded, or invalid for {resource}.\","` | — |
| [SRC-A8360B1B03-L000479](../../scripts/hosted_smoke_test.py#L479) | 479 | `"                partial_report,"` | — |
| [SRC-A8360B1B03-L000480](../../scripts/hosted_smoke_test.py#L480) | 480 | `"            )"` | — |
| [SRC-A8360B1B03-L000481](../../scripts/hosted_smoke_test.py#L481) | 481 | `"    if ("` | — |
| [SRC-A8360B1B03-L000482](../../scripts/hosted_smoke_test.py#L482) | 482 | `"        budget_counts[\"search_queries\"] < 1"` | — |
| [SRC-A8360B1B03-L000483](../../scripts/hosted_smoke_test.py#L483) | 483 | `"        or budget_counts[\"search_calls\"] < 1"` | — |
| [SRC-A8360B1B03-L000484](../../scripts/hosted_smoke_test.py#L484) | 484 | `"        or budget_counts[\"model_calls\"] < 1"` | — |
| [SRC-A8360B1B03-L000485](../../scripts/hosted_smoke_test.py#L485) | 485 | `"    ):"` | — |
| [SRC-A8360B1B03-L000486](../../scripts/hosted_smoke_test.py#L486) | 486 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000487](../../scripts/hosted_smoke_test.py#L487) | 487 | `"            \"Agent hosted_smoke request budget counters do not prove search and model work occurred.\","` | — |
| [SRC-A8360B1B03-L000488](../../scripts/hosted_smoke_test.py#L488) | 488 | `"            partial_report,"` | — |
| [SRC-A8360B1B03-L000489](../../scripts/hosted_smoke_test.py#L489) | 489 | `"        )"` | — |
| [SRC-A8360B1B03-L000490](../../scripts/hosted_smoke_test.py#L490) | 490 | `"    budget_timeout = request_budget.get(\"timeout_seconds\")"` | — |
| [SRC-A8360B1B03-L000491](../../scripts/hosted_smoke_test.py#L491) | 491 | `"    if ("` | — |
| [SRC-A8360B1B03-L000492](../../scripts/hosted_smoke_test.py#L492) | 492 | `"        isinstance(budget_timeout, bool)"` | — |
| [SRC-A8360B1B03-L000493](../../scripts/hosted_smoke_test.py#L493) | 493 | `"        or not isinstance(budget_timeout, (int, float))"` | — |
| [SRC-A8360B1B03-L000494](../../scripts/hosted_smoke_test.py#L494) | 494 | `"        or budget_timeout <= 0"` | — |
| [SRC-A8360B1B03-L000495](../../scripts/hosted_smoke_test.py#L495) | 495 | `"        or budget_timeout > 75"` | — |
| [SRC-A8360B1B03-L000496](../../scripts/hosted_smoke_test.py#L496) | 496 | `"        or request_budget.get(\"budget_exhausted\") is not False"` | — |
| [SRC-A8360B1B03-L000497](../../scripts/hosted_smoke_test.py#L497) | 497 | `"        or request_budget.get(\"deadline_exceeded\") is not False"` | — |
| [SRC-A8360B1B03-L000498](../../scripts/hosted_smoke_test.py#L498) | 498 | `"    ):"` | — |
| [SRC-A8360B1B03-L000499](../../scripts/hosted_smoke_test.py#L499) | 499 | `"        raise SmokeError(\"Agent hosted_smoke request budget was exhausted or exceeded its timeout ceiling.\", partial_report)"` | — |
| [SRC-A8360B1B03-L000500](../../scripts/hosted_smoke_test.py#L500) | 500 | `"    checks[\"request_budget\"] = {"` | — |
| [SRC-A8360B1B03-L000501](../../scripts/hosted_smoke_test.py#L501) | 501 | `"        \"status\": \"passed\","` | — |
| [SRC-A8360B1B03-L000502](../../scripts/hosted_smoke_test.py#L502) | 502 | `"        \"profile\": \"hosted_smoke\","` | — |
| [SRC-A8360B1B03-L000503](../../scripts/hosted_smoke_test.py#L503) | 503 | `"        \"timeout_seconds\": budget_timeout,"` | — |
| [SRC-A8360B1B03-L000504](../../scripts/hosted_smoke_test.py#L504) | 504 | `"        \"limits\": budget_limits,"` | — |
| [SRC-A8360B1B03-L000505](../../scripts/hosted_smoke_test.py#L505) | 505 | `"        \"counts\": budget_counts,"` | — |
| [SRC-A8360B1B03-L000506](../../scripts/hosted_smoke_test.py#L506) | 506 | `"        \"budget_exhausted\": False,"` | — |
| [SRC-A8360B1B03-L000507](../../scripts/hosted_smoke_test.py#L507) | 507 | `"        \"deadline_exceeded\": False,"` | — |
| [SRC-A8360B1B03-L000508](../../scripts/hosted_smoke_test.py#L508) | 508 | `"    }"` | — |
| [SRC-A8360B1B03-L000509](../../scripts/hosted_smoke_test.py#L509) | 509 | `"    if not isinstance(search_report, dict):"` | — |
| [SRC-A8360B1B03-L000510](../../scripts/hosted_smoke_test.py#L510) | 510 | `"        raise SmokeError(\"Agent request did not return a structured search report.\", partial_report)"` | — |
| [SRC-A8360B1B03-L000511](../../scripts/hosted_smoke_test.py#L511) | 511 | `"    pipeline_status = search_report.get(\"pipeline_completion_status\")"` | — |
| [SRC-A8360B1B03-L000512](../../scripts/hosted_smoke_test.py#L512) | 512 | `"    if pipeline_status != \"completed\":"` | — |
| [SRC-A8360B1B03-L000513](../../scripts/hosted_smoke_test.py#L513) | 513 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000514](../../scripts/hosted_smoke_test.py#L514) | 514 | `"            f\"Agent research pipeline did not complete (status: {pipeline_status or 'missing'}).\","` | — |
| [SRC-A8360B1B03-L000515](../../scripts/hosted_smoke_test.py#L515) | 515 | `"            partial_report,"` | — |
| [SRC-A8360B1B03-L000516](../../scripts/hosted_smoke_test.py#L516) | 516 | `"        )"` | — |
| [SRC-A8360B1B03-L000517](../../scripts/hosted_smoke_test.py#L517) | 517 | `"    semantic_verification = search_report.get(\"semantic_claim_verification\")"` | — |
| [SRC-A8360B1B03-L000518](../../scripts/hosted_smoke_test.py#L518) | 518 | `"    semantic_status = ("` | — |
| [SRC-A8360B1B03-L000519](../../scripts/hosted_smoke_test.py#L519) | 519 | `"        semantic_verification.get(\"status\")"` | — |
| [SRC-A8360B1B03-L000520](../../scripts/hosted_smoke_test.py#L520) | 520 | `"        if isinstance(semantic_verification, dict) else None"` | — |
| [SRC-A8360B1B03-L000521](../../scripts/hosted_smoke_test.py#L521) | 521 | `"    )"` | — |
| [SRC-A8360B1B03-L000522](../../scripts/hosted_smoke_test.py#L522) | 522 | `"    if semantic_status not in {"` | — |
| [SRC-A8360B1B03-L000523](../../scripts/hosted_smoke_test.py#L523) | 523 | `"        \"completed_all_claims_supported\","` | — |
| [SRC-A8360B1B03-L000524](../../scripts/hosted_smoke_test.py#L524) | 524 | `"        \"completed_no_factual_claims\","` | — |
| [SRC-A8360B1B03-L000525](../../scripts/hosted_smoke_test.py#L525) | 525 | `"    }:"` | — |
| [SRC-A8360B1B03-L000526](../../scripts/hosted_smoke_test.py#L526) | 526 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000527](../../scripts/hosted_smoke_test.py#L527) | 527 | `"            f\"Agent semantic claim-support review did not pass (status: {semantic_status or 'missing'}).\","` | — |
| [SRC-A8360B1B03-L000528](../../scripts/hosted_smoke_test.py#L528) | 528 | `"            partial_report,"` | — |
| [SRC-A8360B1B03-L000529](../../scripts/hosted_smoke_test.py#L529) | 529 | `"        )"` | — |
| [SRC-A8360B1B03-L000530](../../scripts/hosted_smoke_test.py#L530) | 530 | `"    if search_report.get(\"insufficient_evidence\") is not False:"` | — |
| [SRC-A8360B1B03-L000531](../../scripts/hosted_smoke_test.py#L531) | 531 | `"        raise SmokeError(\"Agent search report flags insufficient evidence or omits that check.\", partial_report)"` | — |
| [SRC-A8360B1B03-L000532](../../scripts/hosted_smoke_test.py#L532) | 532 | `"    if search_report.get(\"claim_audit_semantics\") != \"distinct_model_assessed_source_support_not_ground_truth\":"` | — |
| [SRC-A8360B1B03-L000533](../../scripts/hosted_smoke_test.py#L533) | 533 | `"        raise SmokeError(\"Agent claim-audit semantics are missing or not the expected source-support assessment.\", partial_report)"` | — |
| [SRC-A8360B1B03-L000534](../../scripts/hosted_smoke_test.py#L534) | 534 | `"    evidence_status = answer.get(\"answer_evidence_status\")"` | — |
| [SRC-A8360B1B03-L000535](../../scripts/hosted_smoke_test.py#L535) | 535 | `"    if evidence_status != \"citation_indices_validated_only\":"` | — |
| [SRC-A8360B1B03-L000536](../../scripts/hosted_smoke_test.py#L536) | 536 | `"        raise SmokeError("` | — |
| [SRC-A8360B1B03-L000537](../../scripts/hosted_smoke_test.py#L537) | 537 | `"            f\"Agent answer evidence status is not acceptable for hosted acceptance (status: {evidence_status or 'missing'}).\","` | — |
| [SRC-A8360B1B03-L000538](../../scripts/hosted_smoke_test.py#L538) | 538 | `"            partial_report,"` | — |
| [SRC-A8360B1B03-L000539](../../scripts/hosted_smoke_test.py#L539) | 539 | `"        )"` | — |
| [SRC-A8360B1B03-L000540](../../scripts/hosted_smoke_test.py#L540) | 540 | `"    checks[\"search\"] = {"` | — |
| [SRC-A8360B1B03-L000541](../../scripts/hosted_smoke_test.py#L541) | 541 | `"        \"status\": \"passed\","` | — |
| [SRC-A8360B1B03-L000542](../../scripts/hosted_smoke_test.py#L542) | 542 | `"        \"pages_fetched\": search_report.get(\"pages_fetched\", 0),"` | — |
| [SRC-A8360B1B03-L000543](../../scripts/hosted_smoke_test.py#L543) | 543 | `"        \"providers_reported\": search_report.get(\"providers_used\", []),"` | — |
| [SRC-A8360B1B03-L000544](../../scripts/hosted_smoke_test.py#L544) | 544 | `"        \"pipeline_completion_status\": pipeline_status,"` | — |
| [SRC-A8360B1B03-L000545](../../scripts/hosted_smoke_test.py#L545) | 545 | `"    }"` | — |
| [SRC-A8360B1B03-L000546](../../scripts/hosted_smoke_test.py#L546) | 546 | `"    checks[\"semantic_claim_support\"] = {"` | — |
| [SRC-A8360B1B03-L000547](../../scripts/hosted_smoke_test.py#L547) | 547 | `"        \"status\": \"passed\","` | — |
| [SRC-A8360B1B03-L000548](../../scripts/hosted_smoke_test.py#L548) | 548 | `"        \"verification_status\": semantic_status,"` | — |
| [SRC-A8360B1B03-L000549](../../scripts/hosted_smoke_test.py#L549) | 549 | `"        \"insufficient_evidence\": False,"` | — |
| [SRC-A8360B1B03-L000550](../../scripts/hosted_smoke_test.py#L550) | 550 | `"        \"semantics\": \"model_assessed_source_support_not_ground_truth\","` | — |
| [SRC-A8360B1B03-L000551](../../scripts/hosted_smoke_test.py#L551) | 551 | `"    }"` | — |
| [SRC-A8360B1B03-L000552](../../scripts/hosted_smoke_test.py#L552) | 552 | `"    checks[\"language_model\"] = {"` | — |
| [SRC-A8360B1B03-L000553](../../scripts/hosted_smoke_test.py#L553) | 553 | `"        \"status\": \"passed\","` | — |
| [SRC-A8360B1B03-L000554](../../scripts/hosted_smoke_test.py#L554) | 554 | `"        \"response_received\": True,"` | — |
| [SRC-A8360B1B03-L000555](../../scripts/hosted_smoke_test.py#L555) | 555 | `"        \"verified_by\": \"agent_request\","` | — |
| [SRC-A8360B1B03-L000556](../../scripts/hosted_smoke_test.py#L556) | 556 | `"    }"` | — |
| [SRC-A8360B1B03-L000557](../../scripts/hosted_smoke_test.py#L557) | 557 | `"    checks[\"agent_request\"] = {"` | — |
| [SRC-A8360B1B03-L000558](../../scripts/hosted_smoke_test.py#L558) | 558 | `"        \"status\": \"passed\", \"source_count\": len(usable),"` | — |
| [SRC-A8360B1B03-L000559](../../scripts/hosted_smoke_test.py#L559) | 559 | `"        \"direct_pages_read\": search_report.get(\"pages_fetched\"),"` | — |
| [SRC-A8360B1B03-L000560](../../scripts/hosted_smoke_test.py#L560) | 560 | `"        \"providers_reported\": search_report.get(\"providers_used\", []),"` | — |
| [SRC-A8360B1B03-L000561](../../scripts/hosted_smoke_test.py#L561) | 561 | `"        \"answer_received\": True,"` | — |
| [SRC-A8360B1B03-L000562](../../scripts/hosted_smoke_test.py#L562) | 562 | `"        \"pipeline_completion_status\": pipeline_status,"` | — |
| [SRC-A8360B1B03-L000563](../../scripts/hosted_smoke_test.py#L563) | 563 | `"        \"answer_evidence_status\": evidence_status,"` | — |
| [SRC-A8360B1B03-L000564](../../scripts/hosted_smoke_test.py#L564) | 564 | `"    }"` | — |
| [SRC-A8360B1B03-L000565](../../scripts/hosted_smoke_test.py#L565) | 565 | `"    partial_report.update({"` | — |
| [SRC-A8360B1B03-L000566](../../scripts/hosted_smoke_test.py#L566) | 566 | `"        \"result\": \"passed\","` | — |
| [SRC-A8360B1B03-L000567](../../scripts/hosted_smoke_test.py#L567) | 567 | `"        \"checks\": checks,"` | — |
| [SRC-A8360B1B03-L000568](../../scripts/hosted_smoke_test.py#L568) | 568 | `"        \"note\": ("` | — |
| [SRC-A8360B1B03-L000569](../../scripts/hosted_smoke_test.py#L569) | 569 | `"            \"Transcript contains the exact fixed test question, answer, and returned source metadata. \""` | — |
| [SRC-A8360B1B03-L000570](../../scripts/hosted_smoke_test.py#L570) | 570 | `"            \"This proves the request path worked at test time, not continuous uptime. The approved \""` | — |
| [SRC-A8360B1B03-L000571](../../scripts/hosted_smoke_test.py#L571) | 571 | `"            \"live phase makes one authenticated agent request; that request may fan out to multiple \""` | — |
| [SRC-A8360B1B03-L000572](../../scripts/hosted_smoke_test.py#L572) | 572 | `"            \"configured search providers. The server enforces at most 3 planned queries, 12 provider requests, \""` | — |
| [SRC-A8360B1B03-L000573](../../scripts/hosted_smoke_test.py#L573) | 573 | `"            \"6 model calls, 4 page fetches, and zero external tool calls for this smoke profile; \""` | — |
| [SRC-A8360B1B03-L000574](../../scripts/hosted_smoke_test.py#L574) | 574 | `"            \"operator settings may be stricter. Provider usage may incur charges.\""` | — |
| [SRC-A8360B1B03-L000575](../../scripts/hosted_smoke_test.py#L575) | 575 | `"        ),"` | — |
| [SRC-A8360B1B03-L000576](../../scripts/hosted_smoke_test.py#L576) | 576 | `"    })"` | — |
| [SRC-A8360B1B03-L000577](../../scripts/hosted_smoke_test.py#L577) | 577 | `"    return partial_report"` | — |
| [SRC-A8360B1B03-L000578](../../scripts/hosted_smoke_test.py#L578) | 578 | `""` | — |
| [SRC-A8360B1B03-L000579](../../scripts/hosted_smoke_test.py#L579) | 579 | `""` | — |
| [SRC-A8360B1B03-L000580](../../scripts/hosted_smoke_test.py#L580) | 580 | `"def main() -> int:"` | — |
| [SRC-A8360B1B03-L000581](../../scripts/hosted_smoke_test.py#L581) | 581 | `"    parser = argparse.ArgumentParser(description=\"Run live acceptance checks against hosted Omarai.\")"` | — |
| [SRC-A8360B1B03-L000582](../../scripts/hosted_smoke_test.py#L582) | 582 | `"    parser.add_argument(\"--base-url\", default=os.getenv(\"OMARAI_BASE_URL\", \"\"))"` | — |
| [SRC-A8360B1B03-L000583](../../scripts/hosted_smoke_test.py#L583) | 583 | `"    parser.add_argument(\"--timeout\", type=float, default=90)"` | — |
| [SRC-A8360B1B03-L000584](../../scripts/hosted_smoke_test.py#L584) | 584 | `"    parser.add_argument("` | — |
| [SRC-A8360B1B03-L000585](../../scripts/hosted_smoke_test.py#L585) | 585 | `"        \"--expected-sha\","` | — |
| [SRC-A8360B1B03-L000586](../../scripts/hosted_smoke_test.py#L586) | 586 | `"        default=os.getenv(\"OMARAI_EXPECTED_BUILD_SHA\", \"\"),"` | — |
| [SRC-A8360B1B03-L000587](../../scripts/hosted_smoke_test.py#L587) | 587 | `"        help=\"Require the deployed image to report this full 40-character source Git SHA.\","` | — |
| [SRC-A8360B1B03-L000588](../../scripts/hosted_smoke_test.py#L588) | 588 | `"    )"` | — |
| [SRC-A8360B1B03-L000589](../../scripts/hosted_smoke_test.py#L589) | 589 | `"    parser.add_argument(\"--allow-http\", action=\"store_true\","` | — |
| [SRC-A8360B1B03-L000590](../../scripts/hosted_smoke_test.py#L590) | 590 | `"                        help=\"Allow HTTP only for localhost/127.0.0.1/::1 testing.\")"` | — |
| [SRC-A8360B1B03-L000591](../../scripts/hosted_smoke_test.py#L591) | 591 | `"    parser.add_argument("` | — |
| [SRC-A8360B1B03-L000592](../../scripts/hosted_smoke_test.py#L592) | 592 | `"        \"--local-dev-no-token\","` | — |
| [SRC-A8360B1B03-L000593](../../scripts/hosted_smoke_test.py#L593) | 593 | `"        action=\"store_true\","` | — |
| [SRC-A8360B1B03-L000594](../../scripts/hosted_smoke_test.py#L594) | 594 | `"        help=\"Use the app's existing no-token development bypass on loopback only; never for hosted URLs.\","` | — |
| [SRC-A8360B1B03-L000595](../../scripts/hosted_smoke_test.py#L595) | 595 | `"    )"` | — |
| [SRC-A8360B1B03-L000596](../../scripts/hosted_smoke_test.py#L596) | 596 | `"    parser.add_argument("` | — |
| [SRC-A8360B1B03-L000597](../../scripts/hosted_smoke_test.py#L597) | 597 | `"        \"--allow-provider-usage\","` | — |
| [SRC-A8360B1B03-L000598](../../scripts/hosted_smoke_test.py#L598) | 598 | `"        action=\"store_true\","` | — |
| [SRC-A8360B1B03-L000599](../../scripts/hosted_smoke_test.py#L599) | 599 | `"        help=("` | — |
| [SRC-A8360B1B03-L000600](../../scripts/hosted_smoke_test.py#L600) | 600 | `"            \"Explicitly authorize one live agent request under the server-enforced hosted_smoke \""` | — |
| [SRC-A8360B1B03-L000601](../../scripts/hosted_smoke_test.py#L601) | 601 | `"            \"budget: up to 3 planned queries, 12 provider requests, 6 model calls, 4 page fetches, \""` | — |
| [SRC-A8360B1B03-L000602](../../scripts/hosted_smoke_test.py#L602) | 602 | `"            \"and zero external tool calls. Operator settings may be stricter.\""` | — |
| [SRC-A8360B1B03-L000603](../../scripts/hosted_smoke_test.py#L603) | 603 | `"        ),"` | — |
| [SRC-A8360B1B03-L000604](../../scripts/hosted_smoke_test.py#L604) | 604 | `"    )"` | — |
| [SRC-A8360B1B03-L000605](../../scripts/hosted_smoke_test.py#L605) | 605 | `"    parser.add_argument("` | — |
| [SRC-A8360B1B03-L000606](../../scripts/hosted_smoke_test.py#L606) | 606 | `"        \"--preflight-only\","` | — |
| [SRC-A8360B1B03-L000607](../../scripts/hosted_smoke_test.py#L607) | 607 | `"        action=\"store_true\","` | — |
| [SRC-A8360B1B03-L000608](../../scripts/hosted_smoke_test.py#L608) | 608 | `"        help=\"Run health/build/authentication checks only; never call search providers or a language model.\","` | — |
| [SRC-A8360B1B03-L000609](../../scripts/hosted_smoke_test.py#L609) | 609 | `"    )"` | — |
| [SRC-A8360B1B03-L000610](../../scripts/hosted_smoke_test.py#L610) | 610 | `"    parser.add_argument("` | — |
| [SRC-A8360B1B03-L000611](../../scripts/hosted_smoke_test.py#L611) | 611 | `"        \"--output\","` | — |
| [SRC-A8360B1B03-L000612](../../scripts/hosted_smoke_test.py#L612) | 612 | `"        default=\"\","` | — |
| [SRC-A8360B1B03-L000613](../../scripts/hosted_smoke_test.py#L613) | 613 | `"        help=\"Optional path for a JSON report containing the exact test question, answer, and sources.\","` | — |
| [SRC-A8360B1B03-L000614](../../scripts/hosted_smoke_test.py#L614) | 614 | `"    )"` | — |
| [SRC-A8360B1B03-L000615](../../scripts/hosted_smoke_test.py#L615) | 615 | `"    args = parser.parse_args()"` | — |
| [SRC-A8360B1B03-L000616](../../scripts/hosted_smoke_test.py#L616) | 616 | `"    try:"` | — |
| [SRC-A8360B1B03-L000617](../../scripts/hosted_smoke_test.py#L617) | 617 | `"        result = run_smoke("` | — |
| [SRC-A8360B1B03-L000618](../../scripts/hosted_smoke_test.py#L618) | 618 | `"            args.base_url,"` | — |
| [SRC-A8360B1B03-L000619](../../scripts/hosted_smoke_test.py#L619) | 619 | `"            os.getenv(\"OMARAI_ACCESS_TOKEN\", \"\").strip(),"` | — |
| [SRC-A8360B1B03-L000620](../../scripts/hosted_smoke_test.py#L620) | 620 | `"            timeout=max(5, min(args.timeout, 240)),"` | — |
| [SRC-A8360B1B03-L000621](../../scripts/hosted_smoke_test.py#L621) | 621 | `"            allow_http=args.allow_http,"` | — |
| [SRC-A8360B1B03-L000622](../../scripts/hosted_smoke_test.py#L622) | 622 | `"            expected_sha=args.expected_sha or None,"` | — |
| [SRC-A8360B1B03-L000623](../../scripts/hosted_smoke_test.py#L623) | 623 | `"            local_dev_no_token=args.local_dev_no_token,"` | — |
| [SRC-A8360B1B03-L000624](../../scripts/hosted_smoke_test.py#L624) | 624 | `"            allow_provider_usage=args.allow_provider_usage,"` | — |
| [SRC-A8360B1B03-L000625](../../scripts/hosted_smoke_test.py#L625) | 625 | `"            preflight_only=args.preflight_only,"` | — |
| [SRC-A8360B1B03-L000626](../../scripts/hosted_smoke_test.py#L626) | 626 | `"        )"` | — |
| [SRC-A8360B1B03-L000627](../../scripts/hosted_smoke_test.py#L627) | 627 | `"    except SmokeError as exc:"` | — |
| [SRC-A8360B1B03-L000628](../../scripts/hosted_smoke_test.py#L628) | 628 | `"        failed_report = {**exc.report, \"result\": \"failed\", \"error\": str(exc)}"` | — |
| [SRC-A8360B1B03-L000629](../../scripts/hosted_smoke_test.py#L629) | 629 | `"        rendered = json.dumps(failed_report, ensure_ascii=False, indent=2)"` | — |
| [SRC-A8360B1B03-L000630](../../scripts/hosted_smoke_test.py#L630) | 630 | `"        if args.output:"` | — |
| [SRC-A8360B1B03-L000631](../../scripts/hosted_smoke_test.py#L631) | 631 | `"            output_path = Path(args.output)"` | — |
| [SRC-A8360B1B03-L000632](../../scripts/hosted_smoke_test.py#L632) | 632 | `"            output_path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-A8360B1B03-L000633](../../scripts/hosted_smoke_test.py#L633) | 633 | `"            output_path.write_text(rendered + \"\\n\", encoding=\"utf-8\")"` | — |
| [SRC-A8360B1B03-L000634](../../scripts/hosted_smoke_test.py#L634) | 634 | `"        print(rendered)"` | — |
| [SRC-A8360B1B03-L000635](../../scripts/hosted_smoke_test.py#L635) | 635 | `"        return 1"` | — |
| [SRC-A8360B1B03-L000636](../../scripts/hosted_smoke_test.py#L636) | 636 | `"    rendered = json.dumps(result, ensure_ascii=False, indent=2)"` | — |
| [SRC-A8360B1B03-L000637](../../scripts/hosted_smoke_test.py#L637) | 637 | `"    if args.output:"` | — |
| [SRC-A8360B1B03-L000638](../../scripts/hosted_smoke_test.py#L638) | 638 | `"        output_path = Path(args.output)"` | — |
| [SRC-A8360B1B03-L000639](../../scripts/hosted_smoke_test.py#L639) | 639 | `"        output_path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-A8360B1B03-L000640](../../scripts/hosted_smoke_test.py#L640) | 640 | `"        output_path.write_text(rendered + \"\\n\", encoding=\"utf-8\")"` | — |
| [SRC-A8360B1B03-L000641](../../scripts/hosted_smoke_test.py#L641) | 641 | `"    print(rendered)"` | — |
| [SRC-A8360B1B03-L000642](../../scripts/hosted_smoke_test.py#L642) | 642 | `"    return 0"` | — |
| [SRC-A8360B1B03-L000643](../../scripts/hosted_smoke_test.py#L643) | 643 | `""` | — |
| [SRC-A8360B1B03-L000644](../../scripts/hosted_smoke_test.py#L644) | 644 | `""` | — |
| [SRC-A8360B1B03-L000645](../../scripts/hosted_smoke_test.py#L645) | 645 | `"if __name__ == \"__main__\":"` | — |
| [SRC-A8360B1B03-L000646](../../scripts/hosted_smoke_test.py#L646) | 646 | `"    sys.exit(main())"` | — |
## ملفات أخرى

### FILE-4FFD5AFC54 — [scripts/run_answer_quality_benchmark.py](../../scripts/run_answer_quality_benchmark.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-4FFD5AFC54-L000001](../../scripts/run_answer_quality_benchmark.py#L1) | 1 | `"\"\"\"Offline / optional live runner for OMARAI-REDTEAM-001 answer-quality cases."` | — |
| [SRC-4FFD5AFC54-L000002](../../scripts/run_answer_quality_benchmark.py#L2) | 2 | `""` | — |
| [SRC-4FFD5AFC54-L000003](../../scripts/run_answer_quality_benchmark.py#L3) | 3 | `"Modes"` | — |
| [SRC-4FFD5AFC54-L000004](../../scripts/run_answer_quality_benchmark.py#L4) | 4 | `"-----"` | — |
| [SRC-4FFD5AFC54-L000005](../../scripts/run_answer_quality_benchmark.py#L5) | 5 | `"validate (default)"` | — |
| [SRC-4FFD5AFC54-L000006](../../scripts/run_answer_quality_benchmark.py#L6) | 6 | `"    Load and structurally validate the corpus. No network."` | — |
| [SRC-4FFD5AFC54-L000007](../../scripts/run_answer_quality_benchmark.py#L7) | 7 | `""` | — |
| [SRC-4FFD5AFC54-L000008](../../scripts/run_answer_quality_benchmark.py#L8) | 8 | `"live (explicit opt-in)"` | — |
| [SRC-4FFD5AFC54-L000009](../../scripts/run_answer_quality_benchmark.py#L9) | 9 | `"    POST selected cases to an existing Omarai HTTP API (/api/agent)."` | — |
| [SRC-4FFD5AFC54-L000010](../../scripts/run_answer_quality_benchmark.py#L10) | 10 | `"    Does NOT inject JSON evidence fixtures into the server."` | — |
| [SRC-4FFD5AFC54-L000011](../../scripts/run_answer_quality_benchmark.py#L11) | 11 | `"    Does NOT auto-grade PASS/FAIL for answer quality; records NOT_TESTED"` | — |
| [SRC-4FFD5AFC54-L000012](../../scripts/run_answer_quality_benchmark.py#L12) | 12 | `"    unless a transport/auth error makes the run unusable."` | — |
| [SRC-4FFD5AFC54-L000013](../../scripts/run_answer_quality_benchmark.py#L13) | 13 | `""` | — |
| [SRC-4FFD5AFC54-L000014](../../scripts/run_answer_quality_benchmark.py#L14) | 14 | `"Standard library only. Secrets only via environment (never CLI flags for tokens)."` | — |
| [SRC-4FFD5AFC54-L000015](../../scripts/run_answer_quality_benchmark.py#L15) | 15 | `""` | — |
| [SRC-4FFD5AFC54-L000016](../../scripts/run_answer_quality_benchmark.py#L16) | 16 | `"Examples"` | — |
| [SRC-4FFD5AFC54-L000017](../../scripts/run_answer_quality_benchmark.py#L17) | 17 | `"--------"` | — |
| [SRC-4FFD5AFC54-L000018](../../scripts/run_answer_quality_benchmark.py#L18) | 18 | `"  python scripts/run_answer_quality_benchmark.py"` | — |
| [SRC-4FFD5AFC54-L000019](../../scripts/run_answer_quality_benchmark.py#L19) | 19 | `"  python scripts/run_answer_quality_benchmark.py --mode validate --summary"` | — |
| [SRC-4FFD5AFC54-L000020](../../scripts/run_answer_quality_benchmark.py#L20) | 20 | `"  python scripts/run_answer_quality_benchmark.py --mode live --base-url http://127.0.0.1:8765 \\\\"` | — |
| [SRC-4FFD5AFC54-L000021](../../scripts/run_answer_quality_benchmark.py#L21) | 21 | `"      --case-id AQ-001 --limit 1 --out /tmp/aq_results.json"` | — |
| [SRC-4FFD5AFC54-L000022](../../scripts/run_answer_quality_benchmark.py#L22) | 22 | `"\"\"\""` | — |
| [SRC-4FFD5AFC54-L000023](../../scripts/run_answer_quality_benchmark.py#L23) | 23 | `"from __future__ import annotations"` | — |
| [SRC-4FFD5AFC54-L000024](../../scripts/run_answer_quality_benchmark.py#L24) | 24 | `""` | — |
| [SRC-4FFD5AFC54-L000025](../../scripts/run_answer_quality_benchmark.py#L25) | 25 | `"import argparse"` | — |
| [SRC-4FFD5AFC54-L000026](../../scripts/run_answer_quality_benchmark.py#L26) | 26 | `"import ipaddress"` | — |
| [SRC-4FFD5AFC54-L000027](../../scripts/run_answer_quality_benchmark.py#L27) | 27 | `"import json"` | — |
| [SRC-4FFD5AFC54-L000028](../../scripts/run_answer_quality_benchmark.py#L28) | 28 | `"import math"` | — |
| [SRC-4FFD5AFC54-L000029](../../scripts/run_answer_quality_benchmark.py#L29) | 29 | `"import os"` | — |
| [SRC-4FFD5AFC54-L000030](../../scripts/run_answer_quality_benchmark.py#L30) | 30 | `"import re"` | — |
| [SRC-4FFD5AFC54-L000031](../../scripts/run_answer_quality_benchmark.py#L31) | 31 | `"import sys"` | — |
| [SRC-4FFD5AFC54-L000032](../../scripts/run_answer_quality_benchmark.py#L32) | 32 | `"import time"` | — |
| [SRC-4FFD5AFC54-L000033](../../scripts/run_answer_quality_benchmark.py#L33) | 33 | `"import urllib.error"` | — |
| [SRC-4FFD5AFC54-L000034](../../scripts/run_answer_quality_benchmark.py#L34) | 34 | `"import urllib.parse"` | — |
| [SRC-4FFD5AFC54-L000035](../../scripts/run_answer_quality_benchmark.py#L35) | 35 | `"import urllib.request"` | — |
| [SRC-4FFD5AFC54-L000036](../../scripts/run_answer_quality_benchmark.py#L36) | 36 | `"from datetime import UTC, datetime"` | — |
| [SRC-4FFD5AFC54-L000037](../../scripts/run_answer_quality_benchmark.py#L37) | 37 | `"from pathlib import Path"` | — |
| [SRC-4FFD5AFC54-L000038](../../scripts/run_answer_quality_benchmark.py#L38) | 38 | `""` | — |
| [SRC-4FFD5AFC54-L000039](../../scripts/run_answer_quality_benchmark.py#L39) | 39 | `"ROOT = Path(__file__).resolve().parents[1]"` | — |
| [SRC-4FFD5AFC54-L000040](../../scripts/run_answer_quality_benchmark.py#L40) | 40 | `"DEFAULT_CORPUS = ROOT / \"tests\" / \"fixtures\" / \"answer_quality_cases.json\""` | — |
| [SRC-4FFD5AFC54-L000041](../../scripts/run_answer_quality_benchmark.py#L41) | 41 | `"MAX_RESPONSE_BYTES = 2_000_000"` | — |
| [SRC-4FFD5AFC54-L000042](../../scripts/run_answer_quality_benchmark.py#L42) | 42 | `""` | — |
| [SRC-4FFD5AFC54-L000043](../../scripts/run_answer_quality_benchmark.py#L43) | 43 | `""` | — |
| [SRC-4FFD5AFC54-L000044](../../scripts/run_answer_quality_benchmark.py#L44) | 44 | `"def _load_request_cost_ledger(path: Path \| None, valid_case_ids: set[str]) -> tuple[dict[str, float], str \| None]:"` | — |
| [SRC-4FFD5AFC54-L000045](../../scripts/run_answer_quality_benchmark.py#L45) | 45 | `"    \"\"\"Load reconciled, externally sourced whole-request USD costs; never estimate them.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000046](../../scripts/run_answer_quality_benchmark.py#L46) | 46 | `"    if path is None:"` | — |
| [SRC-4FFD5AFC54-L000047](../../scripts/run_answer_quality_benchmark.py#L47) | 47 | `"        return {}, None"` | — |
| [SRC-4FFD5AFC54-L000048](../../scripts/run_answer_quality_benchmark.py#L48) | 48 | `"    ledger = json.loads(path.read_text(encoding=\"utf-8\"))"` | — |
| [SRC-4FFD5AFC54-L000049](../../scripts/run_answer_quality_benchmark.py#L49) | 49 | `"    if not isinstance(ledger, dict):"` | — |
| [SRC-4FFD5AFC54-L000050](../../scripts/run_answer_quality_benchmark.py#L50) | 50 | `"        raise ValueError(\"request-cost ledger root must be an object\")"` | — |
| [SRC-4FFD5AFC54-L000051](../../scripts/run_answer_quality_benchmark.py#L51) | 51 | `"    if ledger.get(\"currency\") != \"USD\" or ledger.get(\"scope\") != \"complete_request\":"` | — |
| [SRC-4FFD5AFC54-L000052](../../scripts/run_answer_quality_benchmark.py#L52) | 52 | `"        raise ValueError(\"request-cost ledger must declare currency=USD and scope=complete_request\")"` | — |
| [SRC-4FFD5AFC54-L000053](../../scripts/run_answer_quality_benchmark.py#L53) | 53 | `"    source = ledger.get(\"source\")"` | — |
| [SRC-4FFD5AFC54-L000054](../../scripts/run_answer_quality_benchmark.py#L54) | 54 | `"    if not isinstance(source, str) or not source.strip():"` | — |
| [SRC-4FFD5AFC54-L000055](../../scripts/run_answer_quality_benchmark.py#L55) | 55 | `"        raise ValueError(\"request-cost ledger needs a non-empty source describing the reconciliation\")"` | — |
| [SRC-4FFD5AFC54-L000056](../../scripts/run_answer_quality_benchmark.py#L56) | 56 | `"    entries = ledger.get(\"costs\")"` | — |
| [SRC-4FFD5AFC54-L000057](../../scripts/run_answer_quality_benchmark.py#L57) | 57 | `"    if not isinstance(entries, list):"` | — |
| [SRC-4FFD5AFC54-L000058](../../scripts/run_answer_quality_benchmark.py#L58) | 58 | `"        raise ValueError(\"request-cost ledger must contain a costs array\")"` | — |
| [SRC-4FFD5AFC54-L000059](../../scripts/run_answer_quality_benchmark.py#L59) | 59 | `"    costs: dict[str, float] = {}"` | — |
| [SRC-4FFD5AFC54-L000060](../../scripts/run_answer_quality_benchmark.py#L60) | 60 | `"    for index, entry in enumerate(entries):"` | — |
| [SRC-4FFD5AFC54-L000061](../../scripts/run_answer_quality_benchmark.py#L61) | 61 | `"        if not isinstance(entry, dict):"` | — |
| [SRC-4FFD5AFC54-L000062](../../scripts/run_answer_quality_benchmark.py#L62) | 62 | `"            raise ValueError(f\"request-cost ledger costs[{index}] must be an object\")"` | — |
| [SRC-4FFD5AFC54-L000063](../../scripts/run_answer_quality_benchmark.py#L63) | 63 | `"        case_id = entry.get(\"case_id\")"` | — |
| [SRC-4FFD5AFC54-L000064](../../scripts/run_answer_quality_benchmark.py#L64) | 64 | `"        if not isinstance(case_id, str) or case_id not in valid_case_ids:"` | — |
| [SRC-4FFD5AFC54-L000065](../../scripts/run_answer_quality_benchmark.py#L65) | 65 | `"            raise ValueError(f\"request-cost ledger costs[{index}] has an unknown case_id\")"` | — |
| [SRC-4FFD5AFC54-L000066](../../scripts/run_answer_quality_benchmark.py#L66) | 66 | `"        if case_id in costs:"` | — |
| [SRC-4FFD5AFC54-L000067](../../scripts/run_answer_quality_benchmark.py#L67) | 67 | `"            raise ValueError(f\"request-cost ledger has duplicate case_id {case_id}\")"` | — |
| [SRC-4FFD5AFC54-L000068](../../scripts/run_answer_quality_benchmark.py#L68) | 68 | `"        value = _finite_nonnegative_number(entry.get(\"cost_usd\"))"` | — |
| [SRC-4FFD5AFC54-L000069](../../scripts/run_answer_quality_benchmark.py#L69) | 69 | `"        if value is None:"` | — |
| [SRC-4FFD5AFC54-L000070](../../scripts/run_answer_quality_benchmark.py#L70) | 70 | `"            raise ValueError(f\"request-cost ledger {case_id} cost_usd must be finite and non-negative\")"` | — |
| [SRC-4FFD5AFC54-L000071](../../scripts/run_answer_quality_benchmark.py#L71) | 71 | `"        costs[case_id] = value"` | — |
| [SRC-4FFD5AFC54-L000072](../../scripts/run_answer_quality_benchmark.py#L72) | 72 | `"    return costs, source.strip()"` | — |
| [SRC-4FFD5AFC54-L000073](../../scripts/run_answer_quality_benchmark.py#L73) | 73 | `""` | — |
| [SRC-4FFD5AFC54-L000074](../../scripts/run_answer_quality_benchmark.py#L74) | 74 | `""` | — |
| [SRC-4FFD5AFC54-L000075](../../scripts/run_answer_quality_benchmark.py#L75) | 75 | `"def _model_calls_from_payload(payload: dict) -> list[dict]:"` | — |
| [SRC-4FFD5AFC54-L000076](../../scripts/run_answer_quality_benchmark.py#L76) | 76 | `"    \"\"\"Read only structured per-request model-call metadata from an API response.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000077](../../scripts/run_answer_quality_benchmark.py#L77) | 77 | `"    report = payload.get(\"search_report\")"` | — |
| [SRC-4FFD5AFC54-L000078](../../scripts/run_answer_quality_benchmark.py#L78) | 78 | `"    understanding = payload.get(\"task_understanding\")"` | — |
| [SRC-4FFD5AFC54-L000079](../../scripts/run_answer_quality_benchmark.py#L79) | 79 | `"    candidates = ["` | — |
| [SRC-4FFD5AFC54-L000080](../../scripts/run_answer_quality_benchmark.py#L80) | 80 | `"        payload.get(\"model_calls\"),"` | — |
| [SRC-4FFD5AFC54-L000081](../../scripts/run_answer_quality_benchmark.py#L81) | 81 | `"        report.get(\"model_calls\") if isinstance(report, dict) else None,"` | — |
| [SRC-4FFD5AFC54-L000082](../../scripts/run_answer_quality_benchmark.py#L82) | 82 | `"        understanding.get(\"model_calls\") if isinstance(understanding, dict) else None,"` | — |
| [SRC-4FFD5AFC54-L000083](../../scripts/run_answer_quality_benchmark.py#L83) | 83 | `"    ]"` | — |
| [SRC-4FFD5AFC54-L000084](../../scripts/run_answer_quality_benchmark.py#L84) | 84 | `"    for candidate in candidates:"` | — |
| [SRC-4FFD5AFC54-L000085](../../scripts/run_answer_quality_benchmark.py#L85) | 85 | `"        if isinstance(candidate, list) and candidate:"` | — |
| [SRC-4FFD5AFC54-L000086](../../scripts/run_answer_quality_benchmark.py#L86) | 86 | `"            return [item for item in candidate if isinstance(item, dict)]"` | — |
| [SRC-4FFD5AFC54-L000087](../../scripts/run_answer_quality_benchmark.py#L87) | 87 | `"    return []"` | — |
| [SRC-4FFD5AFC54-L000088](../../scripts/run_answer_quality_benchmark.py#L88) | 88 | `""` | — |
| [SRC-4FFD5AFC54-L000089](../../scripts/run_answer_quality_benchmark.py#L89) | 89 | `""` | — |
| [SRC-4FFD5AFC54-L000090](../../scripts/run_answer_quality_benchmark.py#L90) | 90 | `"def _finite_nonnegative_number(value) -> float \| None:"` | — |
| [SRC-4FFD5AFC54-L000091](../../scripts/run_answer_quality_benchmark.py#L91) | 91 | `"    if isinstance(value, bool) or not isinstance(value, (int, float)):"` | — |
| [SRC-4FFD5AFC54-L000092](../../scripts/run_answer_quality_benchmark.py#L92) | 92 | `"        return None"` | — |
| [SRC-4FFD5AFC54-L000093](../../scripts/run_answer_quality_benchmark.py#L93) | 93 | `"    number = float(value)"` | — |
| [SRC-4FFD5AFC54-L000094](../../scripts/run_answer_quality_benchmark.py#L94) | 94 | `"    if not math.isfinite(number) or number < 0:"` | — |
| [SRC-4FFD5AFC54-L000095](../../scripts/run_answer_quality_benchmark.py#L95) | 95 | `"        return None"` | — |
| [SRC-4FFD5AFC54-L000096](../../scripts/run_answer_quality_benchmark.py#L96) | 96 | `"    return number"` | — |
| [SRC-4FFD5AFC54-L000097](../../scripts/run_answer_quality_benchmark.py#L97) | 97 | `""` | — |
| [SRC-4FFD5AFC54-L000098](../../scripts/run_answer_quality_benchmark.py#L98) | 98 | `""` | — |
| [SRC-4FFD5AFC54-L000099](../../scripts/run_answer_quality_benchmark.py#L99) | 99 | `"def _response_metrics(payload: dict \| str, expected_strategy: str, transport_ok: bool) -> dict:"` | — |
| [SRC-4FFD5AFC54-L000100](../../scripts/run_answer_quality_benchmark.py#L100) | 100 | `"    \"\"\"Derive conservative telemetry; never infer semantic correctness from HTTP 200.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000101](../../scripts/run_answer_quality_benchmark.py#L101) | 101 | `"    if not isinstance(payload, dict):"` | — |
| [SRC-4FFD5AFC54-L000102](../../scripts/run_answer_quality_benchmark.py#L102) | 102 | `"        payload = {}"` | — |
| [SRC-4FFD5AFC54-L000103](../../scripts/run_answer_quality_benchmark.py#L103) | 103 | `"    report = payload.get(\"search_report\")"` | — |
| [SRC-4FFD5AFC54-L000104](../../scripts/run_answer_quality_benchmark.py#L104) | 104 | `"    report = report if isinstance(report, dict) else {}"` | — |
| [SRC-4FFD5AFC54-L000105](../../scripts/run_answer_quality_benchmark.py#L105) | 105 | `"    outcome = report.get(\"search_outcome\")"` | — |
| [SRC-4FFD5AFC54-L000106](../../scripts/run_answer_quality_benchmark.py#L106) | 106 | `"    pipeline = report.get(\"pipeline_completion_status\")"` | — |
| [SRC-4FFD5AFC54-L000107](../../scripts/run_answer_quality_benchmark.py#L107) | 107 | `"    source_rows = payload.get(\"sources\")"` | — |
| [SRC-4FFD5AFC54-L000108](../../scripts/run_answer_quality_benchmark.py#L108) | 108 | `"    source_rows_known = isinstance(source_rows, list)"` | — |
| [SRC-4FFD5AFC54-L000109](../../scripts/run_answer_quality_benchmark.py#L109) | 109 | `"    source_count = len(source_rows) if source_rows_known else None"` | — |
| [SRC-4FFD5AFC54-L000110](../../scripts/run_answer_quality_benchmark.py#L110) | 110 | `"    if expected_strategy != \"web_search\":"` | — |
| [SRC-4FFD5AFC54-L000111](../../scripts/run_answer_quality_benchmark.py#L111) | 111 | `"        tool_status = \"NOT_APPLICABLE\""` | — |
| [SRC-4FFD5AFC54-L000112](../../scripts/run_answer_quality_benchmark.py#L112) | 112 | `"    elif not transport_ok:"` | — |
| [SRC-4FFD5AFC54-L000113](../../scripts/run_answer_quality_benchmark.py#L113) | 113 | `"        tool_status = \"TRANSPORT_FAILED\""` | — |
| [SRC-4FFD5AFC54-L000114](../../scripts/run_answer_quality_benchmark.py#L114) | 114 | `"    elif outcome == \"attempted_with_usable_sources\":"` | — |
| [SRC-4FFD5AFC54-L000115](../../scripts/run_answer_quality_benchmark.py#L115) | 115 | `"        if source_count is None:"` | — |
| [SRC-4FFD5AFC54-L000116](../../scripts/run_answer_quality_benchmark.py#L116) | 116 | `"            tool_status = \"UNKNOWN_SOURCE_COUNT\""` | — |
| [SRC-4FFD5AFC54-L000117](../../scripts/run_answer_quality_benchmark.py#L117) | 117 | `"        elif source_count == 0:"` | — |
| [SRC-4FFD5AFC54-L000118](../../scripts/run_answer_quality_benchmark.py#L118) | 118 | `"            tool_status = \"INCONSISTENT_SEARCH_OUTCOME_NO_RETURNED_SOURCES\""` | — |
| [SRC-4FFD5AFC54-L000119](../../scripts/run_answer_quality_benchmark.py#L119) | 119 | `"        else:"` | — |
| [SRC-4FFD5AFC54-L000120](../../scripts/run_answer_quality_benchmark.py#L120) | 120 | `"            tool_status = \"SUCCESS_WITH_USABLE_RESULTS\""` | — |
| [SRC-4FFD5AFC54-L000121](../../scripts/run_answer_quality_benchmark.py#L121) | 121 | `"    elif outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-4FFD5AFC54-L000122](../../scripts/run_answer_quality_benchmark.py#L122) | 122 | `"        if source_count is not None and source_count > 0:"` | — |
| [SRC-4FFD5AFC54-L000123](../../scripts/run_answer_quality_benchmark.py#L123) | 123 | `"            tool_status = \"INCONSISTENT_SEARCH_OUTCOME_WITH_RETURNED_SOURCES\""` | — |
| [SRC-4FFD5AFC54-L000124](../../scripts/run_answer_quality_benchmark.py#L124) | 124 | `"        else:"` | — |
| [SRC-4FFD5AFC54-L000125](../../scripts/run_answer_quality_benchmark.py#L125) | 125 | `"            tool_status = \"ATTEMPTED_NO_USABLE_RESULTS\""` | — |
| [SRC-4FFD5AFC54-L000126](../../scripts/run_answer_quality_benchmark.py#L126) | 126 | `"    elif outcome == \"attempted_research_error\":"` | — |
| [SRC-4FFD5AFC54-L000127](../../scripts/run_answer_quality_benchmark.py#L127) | 127 | `"        tool_status = \"TOOL_FAILED\""` | — |
| [SRC-4FFD5AFC54-L000128](../../scripts/run_answer_quality_benchmark.py#L128) | 128 | `"    elif outcome == \"unknown_after_budget_exhaustion\":"` | — |
| [SRC-4FFD5AFC54-L000129](../../scripts/run_answer_quality_benchmark.py#L129) | 129 | `"        tool_status = \"BUDGET_EXHAUSTED\""` | — |
| [SRC-4FFD5AFC54-L000130](../../scripts/run_answer_quality_benchmark.py#L130) | 130 | `"    elif outcome == \"not_attempted\":"` | — |
| [SRC-4FFD5AFC54-L000131](../../scripts/run_answer_quality_benchmark.py#L131) | 131 | `"        tool_status = \"NOT_ATTEMPTED\""` | — |
| [SRC-4FFD5AFC54-L000132](../../scripts/run_answer_quality_benchmark.py#L132) | 132 | `"    else:"` | — |
| [SRC-4FFD5AFC54-L000133](../../scripts/run_answer_quality_benchmark.py#L133) | 133 | `"        tool_status = \"UNKNOWN\""` | — |
| [SRC-4FFD5AFC54-L000134](../../scripts/run_answer_quality_benchmark.py#L134) | 134 | `""` | — |
| [SRC-4FFD5AFC54-L000135](../../scripts/run_answer_quality_benchmark.py#L135) | 135 | `"    task_understanding = payload.get(\"task_understanding\")"` | — |
| [SRC-4FFD5AFC54-L000136](../../scripts/run_answer_quality_benchmark.py#L136) | 136 | `"    task_understanding = task_understanding if isinstance(task_understanding, dict) else {}"` | — |
| [SRC-4FFD5AFC54-L000137](../../scripts/run_answer_quality_benchmark.py#L137) | 137 | `"    tool_execution = task_understanding.get(\"tool_execution\")"` | — |
| [SRC-4FFD5AFC54-L000138](../../scripts/run_answer_quality_benchmark.py#L138) | 138 | `"    tool_execution = tool_execution if isinstance(tool_execution, dict) else {}"` | — |
| [SRC-4FFD5AFC54-L000139](../../scripts/run_answer_quality_benchmark.py#L139) | 139 | `"    raw_tool_rows = tool_execution.get(\"tool_status_matrix\")"` | — |
| [SRC-4FFD5AFC54-L000140](../../scripts/run_answer_quality_benchmark.py#L140) | 140 | `"    requirements_raw = tool_execution.get(\"required_tools\")"` | — |
| [SRC-4FFD5AFC54-L000141](../../scripts/run_answer_quality_benchmark.py#L141) | 141 | `"    required_tool_matrix_present = ("` | — |
| [SRC-4FFD5AFC54-L000142](../../scripts/run_answer_quality_benchmark.py#L142) | 142 | `"        isinstance(raw_tool_rows, list) and isinstance(requirements_raw, list)"` | — |
| [SRC-4FFD5AFC54-L000143](../../scripts/run_answer_quality_benchmark.py#L143) | 143 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000144](../../scripts/run_answer_quality_benchmark.py#L144) | 144 | `"    matrix_rows = [row for row in raw_tool_rows if isinstance(row, dict)] if isinstance(raw_tool_rows, list) else []"` | — |
| [SRC-4FFD5AFC54-L000145](../../scripts/run_answer_quality_benchmark.py#L145) | 145 | `"    required_tool_names = ["` | — |
| [SRC-4FFD5AFC54-L000146](../../scripts/run_answer_quality_benchmark.py#L146) | 146 | `"        name.strip()"` | — |
| [SRC-4FFD5AFC54-L000147](../../scripts/run_answer_quality_benchmark.py#L147) | 147 | `"        for name in requirements_raw"` | — |
| [SRC-4FFD5AFC54-L000148](../../scripts/run_answer_quality_benchmark.py#L148) | 148 | `"        if isinstance(name, str) and name.strip()"` | — |
| [SRC-4FFD5AFC54-L000149](../../scripts/run_answer_quality_benchmark.py#L149) | 149 | `"    ] if isinstance(requirements_raw, list) else []"` | — |
| [SRC-4FFD5AFC54-L000150](../../scripts/run_answer_quality_benchmark.py#L150) | 150 | `"    allowed_statuses = {"` | — |
| [SRC-4FFD5AFC54-L000151](../../scripts/run_answer_quality_benchmark.py#L151) | 151 | `"        \"web_search\": {"` | — |
| [SRC-4FFD5AFC54-L000152](../../scripts/run_answer_quality_benchmark.py#L152) | 152 | `"            \"failed\", \"unknown\", \"not_attempted\", \"counter_mismatch\","` | — |
| [SRC-4FFD5AFC54-L000153](../../scripts/run_answer_quality_benchmark.py#L153) | 153 | `"            \"completed_with_results\", \"completed_no_usable_results\","` | — |
| [SRC-4FFD5AFC54-L000154](../../scripts/run_answer_quality_benchmark.py#L154) | 154 | `"        },"` | — |
| [SRC-4FFD5AFC54-L000155](../../scripts/run_answer_quality_benchmark.py#L155) | 155 | `"        \"page_fetch\": {"` | — |
| [SRC-4FFD5AFC54-L000156](../../scripts/run_answer_quality_benchmark.py#L156) | 156 | `"            \"counter_mismatch\", \"completed_with_read_pages\","` | — |
| [SRC-4FFD5AFC54-L000157](../../scripts/run_answer_quality_benchmark.py#L157) | 157 | `"            \"attempted_no_readable_pages\", \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000158](../../scripts/run_answer_quality_benchmark.py#L158) | 158 | `"            \"not_attempted_after_search_error\", \"not_attempted_no_fetchable_candidates\","` | — |
| [SRC-4FFD5AFC54-L000159](../../scripts/run_answer_quality_benchmark.py#L159) | 159 | `"            \"not_attempted\","` | — |
| [SRC-4FFD5AFC54-L000160](../../scripts/run_answer_quality_benchmark.py#L160) | 160 | `"        },"` | — |
| [SRC-4FFD5AFC54-L000161](../../scripts/run_answer_quality_benchmark.py#L161) | 161 | `"        \"public_social_search_if_configured\": {"` | — |
| [SRC-4FFD5AFC54-L000162](../../scripts/run_answer_quality_benchmark.py#L162) | 162 | `"            \"completed_with_results\", \"failed\", \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000163](../../scripts/run_answer_quality_benchmark.py#L163) | 163 | `"            \"completed_no_usable_results\", \"not_attempted\", \"not_configured\","` | — |
| [SRC-4FFD5AFC54-L000164](../../scripts/run_answer_quality_benchmark.py#L164) | 164 | `"        },"` | — |
| [SRC-4FFD5AFC54-L000165](../../scripts/run_answer_quality_benchmark.py#L165) | 165 | `"        \"language_model_generation_if_configured\": {"` | — |
| [SRC-4FFD5AFC54-L000166](../../scripts/run_answer_quality_benchmark.py#L166) | 166 | `"            \"completed\", \"not_configured\", \"failed\", \"not_attempted\","` | — |
| [SRC-4FFD5AFC54-L000167](../../scripts/run_answer_quality_benchmark.py#L167) | 167 | `"            \"not_attempted_no_evidence\", \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000168](../../scripts/run_answer_quality_benchmark.py#L168) | 168 | `"        },"` | — |
| [SRC-4FFD5AFC54-L000169](../../scripts/run_answer_quality_benchmark.py#L169) | 169 | `"        \"claim_review_if_configured\": {"` | — |
| [SRC-4FFD5AFC54-L000170](../../scripts/run_answer_quality_benchmark.py#L170) | 170 | `"            \"completed_model_assisted_review\", \"failed\","` | — |
| [SRC-4FFD5AFC54-L000171](../../scripts/run_answer_quality_benchmark.py#L171) | 171 | `"            \"not_attempted_no_evidence\", \"not_attempted\", \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000172](../../scripts/run_answer_quality_benchmark.py#L172) | 172 | `"        },"` | — |
| [SRC-4FFD5AFC54-L000173](../../scripts/run_answer_quality_benchmark.py#L173) | 173 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000174](../../scripts/run_answer_quality_benchmark.py#L174) | 174 | `"    successful_statuses = {"` | — |
| [SRC-4FFD5AFC54-L000175](../../scripts/run_answer_quality_benchmark.py#L175) | 175 | `"        \"web_search\": {\"completed_with_results\"},"` | — |
| [SRC-4FFD5AFC54-L000176](../../scripts/run_answer_quality_benchmark.py#L176) | 176 | `"        \"page_fetch\": {\"completed_with_read_pages\"},"` | — |
| [SRC-4FFD5AFC54-L000177](../../scripts/run_answer_quality_benchmark.py#L177) | 177 | `"        \"public_social_search_if_configured\": {\"completed_with_results\"},"` | — |
| [SRC-4FFD5AFC54-L000178](../../scripts/run_answer_quality_benchmark.py#L178) | 178 | `"        \"language_model_generation_if_configured\": {\"completed\"},"` | — |
| [SRC-4FFD5AFC54-L000179](../../scripts/run_answer_quality_benchmark.py#L179) | 179 | `"        \"claim_review_if_configured\": {\"completed_model_assisted_review\"},"` | — |
| [SRC-4FFD5AFC54-L000180](../../scripts/run_answer_quality_benchmark.py#L180) | 180 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000181](../../scripts/run_answer_quality_benchmark.py#L181) | 181 | `"    required_tool_statuses = []"` | — |
| [SRC-4FFD5AFC54-L000182](../../scripts/run_answer_quality_benchmark.py#L182) | 182 | `"    required_name_set = set(required_tool_names)"` | — |
| [SRC-4FFD5AFC54-L000183](../../scripts/run_answer_quality_benchmark.py#L183) | 183 | `"    reported_required_names = {"` | — |
| [SRC-4FFD5AFC54-L000184](../../scripts/run_answer_quality_benchmark.py#L184) | 184 | `"        row.get(\"tool\")"` | — |
| [SRC-4FFD5AFC54-L000185](../../scripts/run_answer_quality_benchmark.py#L185) | 185 | `"        for row in matrix_rows"` | — |
| [SRC-4FFD5AFC54-L000186](../../scripts/run_answer_quality_benchmark.py#L186) | 186 | `"        if row.get(\"required_by_task_spec\") is True and isinstance(row.get(\"tool\"), str)"` | — |
| [SRC-4FFD5AFC54-L000187](../../scripts/run_answer_quality_benchmark.py#L187) | 187 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000188](../../scripts/run_answer_quality_benchmark.py#L188) | 188 | `"    required_tool_matrix_complete = ("` | — |
| [SRC-4FFD5AFC54-L000189](../../scripts/run_answer_quality_benchmark.py#L189) | 189 | `"        required_tool_matrix_present"` | — |
| [SRC-4FFD5AFC54-L000190](../../scripts/run_answer_quality_benchmark.py#L190) | 190 | `"        and len(required_tool_names) == len(required_name_set)"` | — |
| [SRC-4FFD5AFC54-L000191](../../scripts/run_answer_quality_benchmark.py#L191) | 191 | `"        and reported_required_names == required_name_set"` | — |
| [SRC-4FFD5AFC54-L000192](../../scripts/run_answer_quality_benchmark.py#L192) | 192 | `"    )"` | — |
| [SRC-4FFD5AFC54-L000193](../../scripts/run_answer_quality_benchmark.py#L193) | 193 | `"    for tool in dict.fromkeys(required_tool_names):"` | — |
| [SRC-4FFD5AFC54-L000194](../../scripts/run_answer_quality_benchmark.py#L194) | 194 | `"        matches = ["` | — |
| [SRC-4FFD5AFC54-L000195](../../scripts/run_answer_quality_benchmark.py#L195) | 195 | `"            row for row in matrix_rows"` | — |
| [SRC-4FFD5AFC54-L000196](../../scripts/run_answer_quality_benchmark.py#L196) | 196 | `"            if row.get(\"tool\") == tool and row.get(\"required_by_task_spec\") is True"` | — |
| [SRC-4FFD5AFC54-L000197](../../scripts/run_answer_quality_benchmark.py#L197) | 197 | `"        ]"` | — |
| [SRC-4FFD5AFC54-L000198](../../scripts/run_answer_quality_benchmark.py#L198) | 198 | `"        if len(matches) == 0:"` | — |
| [SRC-4FFD5AFC54-L000199](../../scripts/run_answer_quality_benchmark.py#L199) | 199 | `"            status = \"missing_matrix_row\""` | — |
| [SRC-4FFD5AFC54-L000200](../../scripts/run_answer_quality_benchmark.py#L200) | 200 | `"            status_observed = False"` | — |
| [SRC-4FFD5AFC54-L000201](../../scripts/run_answer_quality_benchmark.py#L201) | 201 | `"            successful = False"` | — |
| [SRC-4FFD5AFC54-L000202](../../scripts/run_answer_quality_benchmark.py#L202) | 202 | `"            required_tool_matrix_complete = False"` | — |
| [SRC-4FFD5AFC54-L000203](../../scripts/run_answer_quality_benchmark.py#L203) | 203 | `"        elif len(matches) > 1:"` | — |
| [SRC-4FFD5AFC54-L000204](../../scripts/run_answer_quality_benchmark.py#L204) | 204 | `"            status = \"duplicate_matrix_rows\""` | — |
| [SRC-4FFD5AFC54-L000205](../../scripts/run_answer_quality_benchmark.py#L205) | 205 | `"            status_observed = False"` | — |
| [SRC-4FFD5AFC54-L000206](../../scripts/run_answer_quality_benchmark.py#L206) | 206 | `"            successful = False"` | — |
| [SRC-4FFD5AFC54-L000207](../../scripts/run_answer_quality_benchmark.py#L207) | 207 | `"            required_tool_matrix_complete = False"` | — |
| [SRC-4FFD5AFC54-L000208](../../scripts/run_answer_quality_benchmark.py#L208) | 208 | `"        else:"` | — |
| [SRC-4FFD5AFC54-L000209](../../scripts/run_answer_quality_benchmark.py#L209) | 209 | `"            raw_status = matches[0].get(\"status\")"` | — |
| [SRC-4FFD5AFC54-L000210](../../scripts/run_answer_quality_benchmark.py#L210) | 210 | `"            status_observed = isinstance(raw_status, str) and bool(raw_status.strip())"` | — |
| [SRC-4FFD5AFC54-L000211](../../scripts/run_answer_quality_benchmark.py#L211) | 211 | `"            status = raw_status if status_observed else \"missing_status\""` | — |
| [SRC-4FFD5AFC54-L000212](../../scripts/run_answer_quality_benchmark.py#L212) | 212 | `"            status_valid = status_observed and status in allowed_statuses.get(tool, set())"` | — |
| [SRC-4FFD5AFC54-L000213](../../scripts/run_answer_quality_benchmark.py#L213) | 213 | `"            successful = status_valid and status in successful_statuses.get(tool, set())"` | — |
| [SRC-4FFD5AFC54-L000214](../../scripts/run_answer_quality_benchmark.py#L214) | 214 | `"            if not status_valid:"` | — |
| [SRC-4FFD5AFC54-L000215](../../scripts/run_answer_quality_benchmark.py#L215) | 215 | `"                required_tool_matrix_complete = False"` | — |
| [SRC-4FFD5AFC54-L000216](../../scripts/run_answer_quality_benchmark.py#L216) | 216 | `"        required_tool_statuses.append({"` | — |
| [SRC-4FFD5AFC54-L000217](../../scripts/run_answer_quality_benchmark.py#L217) | 217 | `"            \"tool\": tool,"` | — |
| [SRC-4FFD5AFC54-L000218](../../scripts/run_answer_quality_benchmark.py#L218) | 218 | `"            \"status\": status,"` | — |
| [SRC-4FFD5AFC54-L000219](../../scripts/run_answer_quality_benchmark.py#L219) | 219 | `"            \"status_observed\": status_observed,"` | — |
| [SRC-4FFD5AFC54-L000220](../../scripts/run_answer_quality_benchmark.py#L220) | 220 | `"            \"status_valid\": status_valid if len(matches) == 1 else False,"` | — |
| [SRC-4FFD5AFC54-L000221](../../scripts/run_answer_quality_benchmark.py#L221) | 221 | `"            \"successful_completion\": successful,"` | — |
| [SRC-4FFD5AFC54-L000222](../../scripts/run_answer_quality_benchmark.py#L222) | 222 | `"        })"` | — |
| [SRC-4FFD5AFC54-L000223](../../scripts/run_answer_quality_benchmark.py#L223) | 223 | `"    if expected_strategy == \"web_search\" and \"web_search\" not in required_name_set:"` | — |
| [SRC-4FFD5AFC54-L000224](../../scripts/run_answer_quality_benchmark.py#L224) | 224 | `"        required_tool_matrix_complete = False"` | — |
| [SRC-4FFD5AFC54-L000225](../../scripts/run_answer_quality_benchmark.py#L225) | 225 | `""` | — |
| [SRC-4FFD5AFC54-L000226](../../scripts/run_answer_quality_benchmark.py#L226) | 226 | `"    calls = _model_calls_from_payload(payload)"` | — |
| [SRC-4FFD5AFC54-L000227](../../scripts/run_answer_quality_benchmark.py#L227) | 227 | `"    reported_costs = []"` | — |
| [SRC-4FFD5AFC54-L000228](../../scripts/run_answer_quality_benchmark.py#L228) | 228 | `"    for call in calls:"` | — |
| [SRC-4FFD5AFC54-L000229](../../scripts/run_answer_quality_benchmark.py#L229) | 229 | `"        usage = call.get(\"provider_usage\")"` | — |
| [SRC-4FFD5AFC54-L000230](../../scripts/run_answer_quality_benchmark.py#L230) | 230 | `"        if not isinstance(usage, dict):"` | — |
| [SRC-4FFD5AFC54-L000231](../../scripts/run_answer_quality_benchmark.py#L231) | 231 | `"            continue"` | — |
| [SRC-4FFD5AFC54-L000232](../../scripts/run_answer_quality_benchmark.py#L232) | 232 | `"        cost = _finite_nonnegative_number(usage.get(\"cost_usd\"))"` | — |
| [SRC-4FFD5AFC54-L000233](../../scripts/run_answer_quality_benchmark.py#L233) | 233 | `"        if cost is not None:"` | — |
| [SRC-4FFD5AFC54-L000234](../../scripts/run_answer_quality_benchmark.py#L234) | 234 | `"            reported_costs.append(cost)"` | — |
| [SRC-4FFD5AFC54-L000235](../../scripts/run_answer_quality_benchmark.py#L235) | 235 | `""` | — |
| [SRC-4FFD5AFC54-L000236](../../scripts/run_answer_quality_benchmark.py#L236) | 236 | `"    if not calls:"` | — |
| [SRC-4FFD5AFC54-L000237](../../scripts/run_answer_quality_benchmark.py#L237) | 237 | `"        cost_status = \"NO_MODEL_CALL_METADATA\""` | — |
| [SRC-4FFD5AFC54-L000238](../../scripts/run_answer_quality_benchmark.py#L238) | 238 | `"    elif len(reported_costs) == len(calls):"` | — |
| [SRC-4FFD5AFC54-L000239](../../scripts/run_answer_quality_benchmark.py#L239) | 239 | `"        cost_status = \"COMPLETE_FOR_RETURNED_MODEL_CALLS\""` | — |
| [SRC-4FFD5AFC54-L000240](../../scripts/run_answer_quality_benchmark.py#L240) | 240 | `"    elif reported_costs:"` | — |
| [SRC-4FFD5AFC54-L000241](../../scripts/run_answer_quality_benchmark.py#L241) | 241 | `"        cost_status = \"PARTIAL_PROVIDER_REPORTED_MODEL_COST\""` | — |
| [SRC-4FFD5AFC54-L000242](../../scripts/run_answer_quality_benchmark.py#L242) | 242 | `"    else:"` | — |
| [SRC-4FFD5AFC54-L000243](../../scripts/run_answer_quality_benchmark.py#L243) | 243 | `"        cost_status = \"PROVIDER_COST_NOT_REPORTED\""` | — |
| [SRC-4FFD5AFC54-L000244](../../scripts/run_answer_quality_benchmark.py#L244) | 244 | `""` | — |
| [SRC-4FFD5AFC54-L000245](../../scripts/run_answer_quality_benchmark.py#L245) | 245 | `"    return {"` | — |
| [SRC-4FFD5AFC54-L000246](../../scripts/run_answer_quality_benchmark.py#L246) | 246 | `"        \"search_outcome\": outcome if isinstance(outcome, str) else \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000247](../../scripts/run_answer_quality_benchmark.py#L247) | 247 | `"        \"pipeline_completion_status\": pipeline if isinstance(pipeline, str) else \"unknown\","` | — |
| [SRC-4FFD5AFC54-L000248](../../scripts/run_answer_quality_benchmark.py#L248) | 248 | `"        \"tool_status\": tool_status,"` | — |
| [SRC-4FFD5AFC54-L000249](../../scripts/run_answer_quality_benchmark.py#L249) | 249 | `"        \"required_tool_statuses\": required_tool_statuses,"` | — |
| [SRC-4FFD5AFC54-L000250](../../scripts/run_answer_quality_benchmark.py#L250) | 250 | `"        \"required_tool_success_count\": sum(1 for row in required_tool_statuses if row[\"successful_completion\"]),"` | — |
| [SRC-4FFD5AFC54-L000251](../../scripts/run_answer_quality_benchmark.py#L251) | 251 | `"        \"required_tool_count\": len(required_tool_statuses),"` | — |
| [SRC-4FFD5AFC54-L000252](../../scripts/run_answer_quality_benchmark.py#L252) | 252 | `"        \"required_tool_success_rate\": ("` | — |
| [SRC-4FFD5AFC54-L000253](../../scripts/run_answer_quality_benchmark.py#L253) | 253 | `"            round("` | — |
| [SRC-4FFD5AFC54-L000254](../../scripts/run_answer_quality_benchmark.py#L254) | 254 | `"                sum(1 for row in required_tool_statuses if row[\"successful_completion\"])"` | — |
| [SRC-4FFD5AFC54-L000255](../../scripts/run_answer_quality_benchmark.py#L255) | 255 | `"                / len(required_tool_statuses),"` | — |
| [SRC-4FFD5AFC54-L000256](../../scripts/run_answer_quality_benchmark.py#L256) | 256 | `"                4,"` | — |
| [SRC-4FFD5AFC54-L000257](../../scripts/run_answer_quality_benchmark.py#L257) | 257 | `"            )"` | — |
| [SRC-4FFD5AFC54-L000258](../../scripts/run_answer_quality_benchmark.py#L258) | 258 | `"            if required_tool_statuses"` | — |
| [SRC-4FFD5AFC54-L000259](../../scripts/run_answer_quality_benchmark.py#L259) | 259 | `"            else None"` | — |
| [SRC-4FFD5AFC54-L000260](../../scripts/run_answer_quality_benchmark.py#L260) | 260 | `"        ),"` | — |
| [SRC-4FFD5AFC54-L000261](../../scripts/run_answer_quality_benchmark.py#L261) | 261 | `"        \"required_tool_status_metrics_status\": ("` | — |
| [SRC-4FFD5AFC54-L000262](../../scripts/run_answer_quality_benchmark.py#L262) | 262 | `"            \"NOT_MEASURED_TOOL_REQUIREMENTS_OR_MATRIX_UNKNOWN\""` | — |
| [SRC-4FFD5AFC54-L000263](../../scripts/run_answer_quality_benchmark.py#L263) | 263 | `"            if not required_tool_matrix_present"` | — |
| [SRC-4FFD5AFC54-L000264](../../scripts/run_answer_quality_benchmark.py#L264) | 264 | `"            else \"SCORED_FROM_TOOL_EXECUTION_MATRIX\""` | — |
| [SRC-4FFD5AFC54-L000265](../../scripts/run_answer_quality_benchmark.py#L265) | 265 | `"            if required_tool_matrix_complete"` | — |
| [SRC-4FFD5AFC54-L000266](../../scripts/run_answer_quality_benchmark.py#L266) | 266 | `"            else \"INCOMPLETE_TOOL_STATUS_MATRIX\""` | — |
| [SRC-4FFD5AFC54-L000267](../../scripts/run_answer_quality_benchmark.py#L267) | 267 | `"        ),"` | — |
| [SRC-4FFD5AFC54-L000268](../../scripts/run_answer_quality_benchmark.py#L268) | 268 | `"        \"required_tool_matrix_present\": required_tool_matrix_present,"` | — |
| [SRC-4FFD5AFC54-L000269](../../scripts/run_answer_quality_benchmark.py#L269) | 269 | `"        \"required_tool_matrix_complete\": required_tool_matrix_complete,"` | — |
| [SRC-4FFD5AFC54-L000270](../../scripts/run_answer_quality_benchmark.py#L270) | 270 | `"        \"source_count\": source_count,"` | — |
| [SRC-4FFD5AFC54-L000271](../../scripts/run_answer_quality_benchmark.py#L271) | 271 | `"        \"model_call_count\": len(calls),"` | — |
| [SRC-4FFD5AFC54-L000272](../../scripts/run_answer_quality_benchmark.py#L272) | 272 | `"        \"provider_reported_model_cost_usd\": round(sum(reported_costs), 10) if reported_costs else None,"` | — |
| [SRC-4FFD5AFC54-L000273](../../scripts/run_answer_quality_benchmark.py#L273) | 273 | `"        \"provider_reported_model_cost_call_count\": len(reported_costs),"` | — |
| [SRC-4FFD5AFC54-L000274](../../scripts/run_answer_quality_benchmark.py#L274) | 274 | `"        \"provider_reported_model_cost_status\": cost_status,"` | — |
| [SRC-4FFD5AFC54-L000275](../../scripts/run_answer_quality_benchmark.py#L275) | 275 | `"        \"request_cost_usd\": None,"` | — |
| [SRC-4FFD5AFC54-L000276](../../scripts/run_answer_quality_benchmark.py#L276) | 276 | `"        \"request_cost_status\": \"NOT_MEASURED_TOTAL_CONNECTOR_COSTS_NOT_EXPOSED\","` | — |
| [SRC-4FFD5AFC54-L000277](../../scripts/run_answer_quality_benchmark.py#L277) | 277 | `"    }"` | — |
| [SRC-4FFD5AFC54-L000278](../../scripts/run_answer_quality_benchmark.py#L278) | 278 | `""` | — |
| [SRC-4FFD5AFC54-L000279](../../scripts/run_answer_quality_benchmark.py#L279) | 279 | `""` | — |
| [SRC-4FFD5AFC54-L000280](../../scripts/run_answer_quality_benchmark.py#L280) | 280 | `"def validate_base_url(base_url: str, *, token_present: bool = False) -> str:"` | — |
| [SRC-4FFD5AFC54-L000281](../../scripts/run_answer_quality_benchmark.py#L281) | 281 | `"    \"\"\"Validate and normalize an API origin before any request can carry a token.\"\"\""` | — |
| [SRC-4FFD5AFC54-L000282](../../scripts/run_answer_quality_benchmark.py#L282) | 282 | `"    if not isinstance(base_url, str) or not base_url.strip():"` | — |
| [SRC-4FFD5AFC54-L000283](../../scripts/run_answer_quality_benchmark.py#L283) | 283 | `"        raise ValueError(\"Base URL must be a non-empty HTTP(S) origin.\")"` | — |
| [SRC-4FFD5AFC54-L000284](../../scripts/run_answer_quality_benchmark.py#L284) | 284 | `"    try:"` | — |
| [SRC-4FFD5AFC54-L000285](../../scripts/run_answer_quality_benchmark.py#L285) | 285 | `"        parsed = urllib.parse.urlsplit(base_url.strip())"` | — |
| [SRC-4FFD5AFC54-L000286](../../scripts/run_answer_quality_benchmark.py#L286) | 286 | `"        scheme = parsed.scheme.lower()"` | — |
| [SRC-4FFD5AFC54-L000287](../../scripts/run_answer_quality_benchmark.py#L287) | 287 | `"        host = (parsed.hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-4FFD5AFC54-L000288](../../scripts/run_answer_quality_benchmark.py#L288) | 288 | `"        port = parsed.port"` | — |
| [SRC-4FFD5AFC54-L000289](../../scripts/run_answer_quality_benchmark.py#L289) | 289 | `"    except ValueError as exc:"` | — |
| [SRC-4FFD5AFC54-L000290](../../scripts/run_answer_quality_benchmark.py#L290) | 290 | `"        raise ValueError(\"Base URL is malformed.\") from exc"` | — |
| [SRC-4FFD5AFC54-L000291](../../scripts/run_answer_quality_benchmark.py#L291) | 291 | `""` | — |
| [SRC-4FFD5AFC54-L000292](../../scripts/run_answer_quality_benchmark.py#L292) | 292 | `"    if scheme not in {\"http\", \"https\"} or not host:"` | — |
| [SRC-4FFD5AFC54-L000293](../../scripts/run_answer_quality_benchmark.py#L293) | 293 | `"        raise ValueError(\"Base URL must use HTTP or HTTPS and include a hostname.\")"` | — |
| [SRC-4FFD5AFC54-L000294](../../scripts/run_answer_quality_benchmark.py#L294) | 294 | `"    if parsed.username is not None or parsed.password is not None:"` | — |
| [SRC-4FFD5AFC54-L000295](../../scripts/run_answer_quality_benchmark.py#L295) | 295 | `"        raise ValueError(\"Base URL must not include a username or password.\")"` | — |
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
