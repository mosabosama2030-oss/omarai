# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **005**
- سجلات الأسطر: **800**
- النطاق: SRC-59CF4B7DE8-L000418 إلى SRC-3AA6165B18-L000014
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-59CF4B7DE8 — [agents/research.py](../../agents/research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-59CF4B7DE8-L000418](../../agents/research.py#L418) | 418 | `"            domain = SOCIAL_DOMAINS[platform]"` | — |
| [SRC-59CF4B7DE8-L000419](../../agents/research.py#L419) | 419 | `"            site_query = compact_search_query(f\"site:{domain} {base}\")"` | — |
| [SRC-59CF4B7DE8-L000420](../../agents/research.py#L420) | 420 | `"            if site_query not in queries:"` | — |
| [SRC-59CF4B7DE8-L000421](../../agents/research.py#L421) | 421 | `"                queries.append(site_query)"` | — |
| [SRC-59CF4B7DE8-L000422](../../agents/research.py#L422) | 422 | `""` | — |
| [SRC-59CF4B7DE8-L000423](../../agents/research.py#L423) | 423 | `"    if deep and base and not social_focus and len(queries) < MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000424](../../agents/research.py#L424) | 424 | `"        queries.append(compact_search_query(base + \" مصادر موثوقة تقارير إحصاءات\"))"` | — |
| [SRC-59CF4B7DE8-L000425](../../agents/research.py#L425) | 425 | `""` | — |
| [SRC-59CF4B7DE8-L000426](../../agents/research.py#L426) | 426 | `"    if requirement_queries:"` | — |
| [SRC-59CF4B7DE8-L000427](../../agents/research.py#L427) | 427 | `"        optional_queries = list(queries)"` | — |
| [SRC-59CF4B7DE8-L000428](../../agents/research.py#L428) | 428 | `"        if len(requirement_queries) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000429](../../agents/research.py#L429) | 429 | `"            priority_queries = [item[\"query\"] for item in requirement_queries]"` | — |
| [SRC-59CF4B7DE8-L000430](../../agents/research.py#L430) | 430 | `"        else:"` | — |
| [SRC-59CF4B7DE8-L000431](../../agents/research.py#L431) | 431 | `"            priority_queries = ([base] if base else []) + ["` | — |
| [SRC-59CF4B7DE8-L000432](../../agents/research.py#L432) | 432 | `"                item[\"query\"] for item in requirement_queries"` | — |
| [SRC-59CF4B7DE8-L000433](../../agents/research.py#L433) | 433 | `"            ]"` | — |
| [SRC-59CF4B7DE8-L000434](../../agents/research.py#L434) | 434 | `"        priority_seen = {item.casefold() for item in priority_queries}"` | — |
| [SRC-59CF4B7DE8-L000435](../../agents/research.py#L435) | 435 | `"        queries = priority_queries + ["` | — |
| [SRC-59CF4B7DE8-L000436](../../agents/research.py#L436) | 436 | `"            item for item in optional_queries if item.casefold() not in priority_seen"` | — |
| [SRC-59CF4B7DE8-L000437](../../agents/research.py#L437) | 437 | `"        ]"` | — |
| [SRC-59CF4B7DE8-L000438](../../agents/research.py#L438) | 438 | `""` | — |
| [SRC-59CF4B7DE8-L000439](../../agents/research.py#L439) | 439 | `"    unique: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000440](../../agents/research.py#L440) | 440 | `"    seen: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000441](../../agents/research.py#L441) | 441 | `"    for query in queries:"` | — |
| [SRC-59CF4B7DE8-L000442](../../agents/research.py#L442) | 442 | `"        value = compact_search_query(query)"` | — |
| [SRC-59CF4B7DE8-L000443](../../agents/research.py#L443) | 443 | `"        key = value.casefold()"` | — |
| [SRC-59CF4B7DE8-L000444](../../agents/research.py#L444) | 444 | `"        if value and key not in seen:"` | — |
| [SRC-59CF4B7DE8-L000445](../../agents/research.py#L445) | 445 | `"            unique.append(value)"` | — |
| [SRC-59CF4B7DE8-L000446](../../agents/research.py#L446) | 446 | `"            seen.add(key)"` | — |
| [SRC-59CF4B7DE8-L000447](../../agents/research.py#L447) | 447 | `"        if len(unique) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000448](../../agents/research.py#L448) | 448 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000449](../../agents/research.py#L449) | 449 | `""` | — |
| [SRC-59CF4B7DE8-L000450](../../agents/research.py#L450) | 450 | `"    base_plan = {"` | — |
| [SRC-59CF4B7DE8-L000451](../../agents/research.py#L451) | 451 | `"        \"queries\": unique or ([base] if base else []),"` | — |
| [SRC-59CF4B7DE8-L000452](../../agents/research.py#L452) | 452 | `"        \"coverage_targets\": coverage_targets,"` | — |
| [SRC-59CF4B7DE8-L000453](../../agents/research.py#L453) | 453 | `"        \"requirement_queries\": requirement_queries,"` | — |
| [SRC-59CF4B7DE8-L000454](../../agents/research.py#L454) | 454 | `"        \"direct_urls\": direct_urls,"` | — |
| [SRC-59CF4B7DE8-L000455](../../agents/research.py#L455) | 455 | `"        \"social_focus\": social_focus,"` | — |
| [SRC-59CF4B7DE8-L000456](../../agents/research.py#L456) | 456 | `"        \"freshness\": \"current\" if fresh else \"any\","` | — |
| [SRC-59CF4B7DE8-L000457](../../agents/research.py#L457) | 457 | `"        \"depth\": detected_depth,"` | — |
| [SRC-59CF4B7DE8-L000458](../../agents/research.py#L458) | 458 | `"        \"platforms\": platforms,"` | — |
| [SRC-59CF4B7DE8-L000459](../../agents/research.py#L459) | 459 | `"        \"planning_method\": \"deterministic_fallback\","` | — |
| [SRC-59CF4B7DE8-L000460](../../agents/research.py#L460) | 460 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000461](../../agents/research.py#L461) | 461 | `"    return _attach_task_understanding("` | — |
| [SRC-59CF4B7DE8-L000462](../../agents/research.py#L462) | 462 | `"        base_plan, contextual_question, intent_route=\"deterministic_fallback\""` | — |
| [SRC-59CF4B7DE8-L000463](../../agents/research.py#L463) | 463 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000464](../../agents/research.py#L464) | 464 | `""` | — |
| [SRC-59CF4B7DE8-L000465](../../agents/research.py#L465) | 465 | `""` | — |
| [SRC-59CF4B7DE8-L000466](../../agents/research.py#L466) | 466 | `"def validate_plan("` | — |
| [SRC-59CF4B7DE8-L000467](../../agents/research.py#L467) | 467 | `"    candidate: Any, question: str, history: list[dict[str, str]] \| None = None"` | — |
| [SRC-59CF4B7DE8-L000468](../../agents/research.py#L468) | 468 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000469](../../agents/research.py#L469) | 469 | `"    fallback = fallback_plan(question, history)"` | — |
| [SRC-59CF4B7DE8-L000470](../../agents/research.py#L470) | 470 | `"    if not isinstance(candidate, dict):"` | — |
| [SRC-59CF4B7DE8-L000471](../../agents/research.py#L471) | 471 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000472](../../agents/research.py#L472) | 472 | `"    raw_queries = candidate.get(\"queries\", [])"` | — |
| [SRC-59CF4B7DE8-L000473](../../agents/research.py#L473) | 473 | `"    if not isinstance(raw_queries, list):"` | — |
| [SRC-59CF4B7DE8-L000474](../../agents/research.py#L474) | 474 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000475](../../agents/research.py#L475) | 475 | `"    queries: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000476](../../agents/research.py#L476) | 476 | `"    seen: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000477](../../agents/research.py#L477) | 477 | `"    for item in raw_queries:"` | — |
| [SRC-59CF4B7DE8-L000478](../../agents/research.py#L478) | 478 | `"        query = compact_search_query(item)"` | — |
| [SRC-59CF4B7DE8-L000479](../../agents/research.py#L479) | 479 | `"        # Never accept prompt-like multi-line payloads as search-query instructions."` | — |
| [SRC-59CF4B7DE8-L000480](../../agents/research.py#L480) | 480 | `"        query = query.replace(\"\\n\", \" \").replace(\"\\r\", \" \")"` | — |
| [SRC-59CF4B7DE8-L000481](../../agents/research.py#L481) | 481 | `"        if len(query) < 2:"` | — |
| [SRC-59CF4B7DE8-L000482](../../agents/research.py#L482) | 482 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000483](../../agents/research.py#L483) | 483 | `"        if query.casefold() not in seen:"` | — |
| [SRC-59CF4B7DE8-L000484](../../agents/research.py#L484) | 484 | `"            seen.add(query.casefold())"` | — |
| [SRC-59CF4B7DE8-L000485](../../agents/research.py#L485) | 485 | `"            queries.append(query)"` | — |
| [SRC-59CF4B7DE8-L000486](../../agents/research.py#L486) | 486 | `"        if len(queries) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000487](../../agents/research.py#L487) | 487 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000488](../../agents/research.py#L488) | 488 | `"    if not queries:"` | — |
| [SRC-59CF4B7DE8-L000489](../../agents/research.py#L489) | 489 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000490](../../agents/research.py#L490) | 490 | `"    base = fallback_plan(question, history)"` | — |
| [SRC-59CF4B7DE8-L000491](../../agents/research.py#L491) | 491 | `"    coverage_targets = list(base.get(\"coverage_targets\") or [])"` | — |
| [SRC-59CF4B7DE8-L000492](../../agents/research.py#L492) | 492 | `"    requirement_queries = list(base.get(\"requirement_queries\") or [])"` | — |
| [SRC-59CF4B7DE8-L000493](../../agents/research.py#L493) | 493 | `"    if requirement_queries:"` | — |
| [SRC-59CF4B7DE8-L000494](../../agents/research.py#L494) | 494 | `"        required_prefix: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000495](../../agents/research.py#L495) | 495 | `"        if len(requirement_queries) < MAX_PLAN_QUERIES and base.get(\"queries\"):"` | — |
| [SRC-59CF4B7DE8-L000496](../../agents/research.py#L496) | 496 | `"            required_prefix.append(base[\"queries\"][0])"` | — |
| [SRC-59CF4B7DE8-L000497](../../agents/research.py#L497) | 497 | `"        required_prefix.extend("` | — |
| [SRC-59CF4B7DE8-L000498](../../agents/research.py#L498) | 498 | `"            item[\"query\"] for item in requirement_queries if item.get(\"query\")"` | — |
| [SRC-59CF4B7DE8-L000499](../../agents/research.py#L499) | 499 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000500](../../agents/research.py#L500) | 500 | `"        queries = list(dict.fromkeys(required_prefix + queries))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-59CF4B7DE8-L000501](../../agents/research.py#L501) | 501 | `"    platforms = candidate.get(\"platforms\")"` | — |
| [SRC-59CF4B7DE8-L000502](../../agents/research.py#L502) | 502 | `"    if not isinstance(platforms, list):"` | — |
| [SRC-59CF4B7DE8-L000503](../../agents/research.py#L503) | 503 | `"        platforms = base[\"platforms\"]"` | — |
| [SRC-59CF4B7DE8-L000504](../../agents/research.py#L504) | 504 | `"    safe_platforms = [p for p in platforms if isinstance(p, str) and p in SOCIAL_DOMAINS]"` | — |
| [SRC-59CF4B7DE8-L000505](../../agents/research.py#L505) | 505 | `"    validated_plan = {"` | — |
| [SRC-59CF4B7DE8-L000506](../../agents/research.py#L506) | 506 | `"        \"queries\": queries,"` | — |
| [SRC-59CF4B7DE8-L000507](../../agents/research.py#L507) | 507 | `"        \"coverage_targets\": coverage_targets,"` | — |
| [SRC-59CF4B7DE8-L000508](../../agents/research.py#L508) | 508 | `"        \"requirement_queries\": requirement_queries,"` | — |
| [SRC-59CF4B7DE8-L000509](../../agents/research.py#L509) | 509 | `"        \"direct_urls\": fallback[\"direct_urls\"],"` | — |
| [SRC-59CF4B7DE8-L000510](../../agents/research.py#L510) | 510 | `"        \"social_focus\": bool(candidate.get(\"social_focus\", base[\"social_focus\"])),"` | — |
| [SRC-59CF4B7DE8-L000511](../../agents/research.py#L511) | 511 | `"        \"freshness\": \"current\" if candidate.get(\"freshness\") == \"current\" else base[\"freshness\"],"` | — |
| [SRC-59CF4B7DE8-L000512](../../agents/research.py#L512) | 512 | `"        \"depth\": \"deep\" if candidate.get(\"depth\") == \"deep\" else base[\"depth\"],"` | — |
| [SRC-59CF4B7DE8-L000513](../../agents/research.py#L513) | 513 | `"        \"platforms\": list(dict.fromkeys(safe_platforms))[:5],"` | — |
| [SRC-59CF4B7DE8-L000514](../../agents/research.py#L514) | 514 | `"        \"planning_method\": \"language_model\","` | — |
| [SRC-59CF4B7DE8-L000515](../../agents/research.py#L515) | 515 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000516](../../agents/research.py#L516) | 516 | `"    return _attach_task_understanding("` | — |
| [SRC-59CF4B7DE8-L000517](../../agents/research.py#L517) | 517 | `"        validated_plan,"` | — |
| [SRC-59CF4B7DE8-L000518](../../agents/research.py#L518) | 518 | `"        resolve_followup_query(question, history),"` | — |
| [SRC-59CF4B7DE8-L000519](../../agents/research.py#L519) | 519 | `"        intent_route=\"validated_language_model_plan\","` | — |
| [SRC-59CF4B7DE8-L000520](../../agents/research.py#L520) | 520 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000521](../../agents/research.py#L521) | 521 | `""` | — |
| [SRC-59CF4B7DE8-L000522](../../agents/research.py#L522) | 522 | `""` | — |
| [SRC-59CF4B7DE8-L000523](../../agents/research.py#L523) | 523 | `"def _canonical_result_url(url: str) -> str:"` | — |
| [SRC-59CF4B7DE8-L000524](../../agents/research.py#L524) | 524 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000525](../../agents/research.py#L525) | 525 | `"        parsed = urlparse(url)"` | — |
| [SRC-59CF4B7DE8-L000526](../../agents/research.py#L526) | 526 | `"        host = (parsed.hostname or \"\").lower().removeprefix(\"www.\")"` | — |
| [SRC-59CF4B7DE8-L000527](../../agents/research.py#L527) | 527 | `"        # Drop fragments and common tracking query parameters before deduplication."` | — |
| [SRC-59CF4B7DE8-L000528](../../agents/research.py#L528) | 528 | `"        parts = []"` | — |
| [SRC-59CF4B7DE8-L000529](../../agents/research.py#L529) | 529 | `"        for part in parsed.query.split(\"&\"):"` | — |
| [SRC-59CF4B7DE8-L000530](../../agents/research.py#L530) | 530 | `"            key = part.split(\"=\", 1)[0].lower()"` | — |
| [SRC-59CF4B7DE8-L000531](../../agents/research.py#L531) | 531 | `"            if key.startswith(\"utm_\") or key in {\"fbclid\", \"gclid\", \"ref\", \"ref_src\"}:"` | — |
| [SRC-59CF4B7DE8-L000532](../../agents/research.py#L532) | 532 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000533](../../agents/research.py#L533) | 533 | `"            if part:"` | — |
| [SRC-59CF4B7DE8-L000534](../../agents/research.py#L534) | 534 | `"                parts.append(part)"` | — |
| [SRC-59CF4B7DE8-L000535](../../agents/research.py#L535) | 535 | `"        query = \"&\".join(sorted(parts))"` | — |
| [SRC-59CF4B7DE8-L000536](../../agents/research.py#L536) | 536 | `"        path = parsed.path.rstrip(\"/\") or \"/\""` | — |
| [SRC-59CF4B7DE8-L000537](../../agents/research.py#L537) | 537 | `"        return f\"{parsed.scheme.lower()}://{host}{path}\" + (f\"?{query}\" if query else \"\")"` | — |
| [SRC-59CF4B7DE8-L000538](../../agents/research.py#L538) | 538 | `"    except (ValueError, TypeError):"` | — |
| [SRC-59CF4B7DE8-L000539](../../agents/research.py#L539) | 539 | `"        return url"` | — |
| [SRC-59CF4B7DE8-L000540](../../agents/research.py#L540) | 540 | `""` | — |
| [SRC-59CF4B7DE8-L000541](../../agents/research.py#L541) | 541 | `""` | — |
| [SRC-59CF4B7DE8-L000542](../../agents/research.py#L542) | 542 | `"def classify_source(url: str) -> dict[str, str]:"` | — |
| [SRC-59CF4B7DE8-L000543](../../agents/research.py#L543) | 543 | `"    host = (urlparse(url).hostname or \"\").lower().removeprefix(\"www.\")"` | — |
| [SRC-59CF4B7DE8-L000544](../../agents/research.py#L544) | 544 | `"    platform = \"web\""` | — |
| [SRC-59CF4B7DE8-L000545](../../agents/research.py#L545) | 545 | `"    mapping = {"` | — |
| [SRC-59CF4B7DE8-L000546](../../agents/research.py#L546) | 546 | `"        \"reddit.com\": \"reddit\", \"old.reddit.com\": \"reddit\","` | — |
| [SRC-59CF4B7DE8-L000547](../../agents/research.py#L547) | 547 | `"        \"youtube.com\": \"youtube\", \"youtu.be\": \"youtube\","` | — |
| [SRC-59CF4B7DE8-L000548](../../agents/research.py#L548) | 548 | `"        \"facebook.com\": \"facebook\", \"instagram.com\": \"instagram\","` | — |
| [SRC-59CF4B7DE8-L000549](../../agents/research.py#L549) | 549 | `"        \"x.com\": \"x\", \"twitter.com\": \"x\", \"tiktok.com\": \"tiktok\","` | — |
| [SRC-59CF4B7DE8-L000550](../../agents/research.py#L550) | 550 | `"        \"linkedin.com\": \"linkedin\", \"threads.net\": \"threads\","` | — |
| [SRC-59CF4B7DE8-L000551](../../agents/research.py#L551) | 551 | `"        \"bsky.app\": \"bluesky\","` | — |
| [SRC-59CF4B7DE8-L000552](../../agents/research.py#L552) | 552 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000553](../../agents/research.py#L553) | 553 | `"    for domain, label in mapping.items():"` | — |
| [SRC-59CF4B7DE8-L000554](../../agents/research.py#L554) | 554 | `"        if host == domain or host.endswith(\".\" + domain):"` | — |
| [SRC-59CF4B7DE8-L000555](../../agents/research.py#L555) | 555 | `"            platform = label"` | — |
| [SRC-59CF4B7DE8-L000556](../../agents/research.py#L556) | 556 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000557](../../agents/research.py#L557) | 557 | `"    trust = \"general\""` | — |
| [SRC-59CF4B7DE8-L000558](../../agents/research.py#L558) | 558 | `"    if host.endswith((\".gov\", \".gov.eg\", \".gov.uk\")):"` | — |
| [SRC-59CF4B7DE8-L000559](../../agents/research.py#L559) | 559 | `"        trust = \"government\""` | — |
| [SRC-59CF4B7DE8-L000560](../../agents/research.py#L560) | 560 | `"    elif host.endswith((\".edu\", \".ac.uk\", \".edu.eg\")):"` | — |
| [SRC-59CF4B7DE8-L000561](../../agents/research.py#L561) | 561 | `"        trust = \"academic\""` | — |
| [SRC-59CF4B7DE8-L000562](../../agents/research.py#L562) | 562 | `"    elif host == \"news.google.com\" or any("` | — |
| [SRC-59CF4B7DE8-L000563](../../agents/research.py#L563) | 563 | `"        host == name or host.endswith(\".\" + name)"` | — |
| [SRC-59CF4B7DE8-L000564](../../agents/research.py#L564) | 564 | `"        for name in ("` | — |
| [SRC-59CF4B7DE8-L000565](../../agents/research.py#L565) | 565 | `"            \"reuters.com\", \"apnews.com\", \"bbc.com\", \"bbc.co.uk\","` | — |
| [SRC-59CF4B7DE8-L000566](../../agents/research.py#L566) | 566 | `"            \"ft.com\", \"nytimes.com\", \"theguardian.com\","` | — |
| [SRC-59CF4B7DE8-L000567](../../agents/research.py#L567) | 567 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000568](../../agents/research.py#L568) | 568 | `"    ):"` | — |
| [SRC-59CF4B7DE8-L000569](../../agents/research.py#L569) | 569 | `"        # Match publisher host boundaries; lookalike domains must not inherit a"` | — |
| [SRC-59CF4B7DE8-L000570](../../agents/research.py#L570) | 570 | `"        # news label merely because their hostname contains a trusted brand string."` | — |
| [SRC-59CF4B7DE8-L000571](../../agents/research.py#L571) | 571 | `"        trust = \"news\""` | — |
| [SRC-59CF4B7DE8-L000572](../../agents/research.py#L572) | 572 | `"    elif platform != \"web\":"` | — |
| [SRC-59CF4B7DE8-L000573](../../agents/research.py#L573) | 573 | `"        trust = \"social\""` | — |
| [SRC-59CF4B7DE8-L000574](../../agents/research.py#L574) | 574 | `"    return {\"domain\": host, \"platform\": platform, \"source_class\": trust}"` | — |
| [SRC-59CF4B7DE8-L000575](../../agents/research.py#L575) | 575 | `""` | — |
| [SRC-59CF4B7DE8-L000576](../../agents/research.py#L576) | 576 | `""` | — |
| [SRC-59CF4B7DE8-L000577](../../agents/research.py#L577) | 577 | `"def fuse_ranked_results("` | — |
| [SRC-59CF4B7DE8-L000578](../../agents/research.py#L578) | 578 | `"    batches: list[dict[str, Any]], limit: int = MAX_FUSED_RESULTS"` | — |
| [SRC-59CF4B7DE8-L000579](../../agents/research.py#L579) | 579 | `") -> list[dict[str, Any]]:"` | — |
| [SRC-59CF4B7DE8-L000580](../../agents/research.py#L580) | 580 | `"    \"\"\"Reciprocal-rank-fuse result sets across queries/providers and dedupe URLs.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000581](../../agents/research.py#L581) | 581 | `"    accumulated: dict[str, dict[str, Any]] = {}"` | — |
| [SRC-59CF4B7DE8-L000582](../../agents/research.py#L582) | 582 | `"    for batch in batches:"` | — |
| [SRC-59CF4B7DE8-L000583](../../agents/research.py#L583) | 583 | `"        query = _compact(batch.get(\"query\", \"\"), 500)"` | — |
| [SRC-59CF4B7DE8-L000584](../../agents/research.py#L584) | 584 | `"        provider = _compact(batch.get(\"provider\", \"search\"), 80)"` | — |
| [SRC-59CF4B7DE8-L000585](../../agents/research.py#L585) | 585 | `"        results = batch.get(\"results\", [])"` | — |
| [SRC-59CF4B7DE8-L000586](../../agents/research.py#L586) | 586 | `"        if not isinstance(results, list):"` | — |
| [SRC-59CF4B7DE8-L000587](../../agents/research.py#L587) | 587 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000588](../../agents/research.py#L588) | 588 | `"        for position, source in enumerate(results, 1):"` | — |
| [SRC-59CF4B7DE8-L000589](../../agents/research.py#L589) | 589 | `"            if not isinstance(source, dict) or not source.get(\"url\"):"` | — |
| [SRC-59CF4B7DE8-L000590](../../agents/research.py#L590) | 590 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000591](../../agents/research.py#L591) | 591 | `"            url = _canonical_result_url(str(source[\"url\"]))"` | — |
| [SRC-59CF4B7DE8-L000592](../../agents/research.py#L592) | 592 | `"            if not url.startswith((\"https://\", \"http://\")):"` | — |
| [SRC-59CF4B7DE8-L000593](../../agents/research.py#L593) | 593 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000594](../../agents/research.py#L594) | 594 | `"            entry = accumulated.get(url)"` | — |
| [SRC-59CF4B7DE8-L000595](../../agents/research.py#L595) | 595 | `"            if entry is None:"` | — |
| [SRC-59CF4B7DE8-L000596](../../agents/research.py#L596) | 596 | `"                publisher_url = _compact(source.get(\"publisher_url\") or \"\", 2048)"` | — |
| [SRC-59CF4B7DE8-L000597](../../agents/research.py#L597) | 597 | `"                source_identity_url = publisher_url or str(source[\"url\"])"` | — |
| [SRC-59CF4B7DE8-L000598](../../agents/research.py#L598) | 598 | `"                entry = {"` | — |
| [SRC-59CF4B7DE8-L000599](../../agents/research.py#L599) | 599 | `"                    \"title\": _compact(source.get(\"title\") or \"نتيجة ويب\", 300),"` | — |
| [SRC-59CF4B7DE8-L000600](../../agents/research.py#L600) | 600 | `"                    \"url\": str(source[\"url\"]),"` | — |
| [SRC-59CF4B7DE8-L000601](../../agents/research.py#L601) | 601 | `"                    \"snippet\": _compact(source.get(\"snippet\") or \"\", 1800),"` | — |
| [SRC-59CF4B7DE8-L000602](../../agents/research.py#L602) | 602 | `"                    \"page_text\": _compact(source.get(\"page_text\") or \"\", 12_000),"` | — |
| [SRC-59CF4B7DE8-L000603](../../agents/research.py#L603) | 603 | `"                    \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-59CF4B7DE8-L000604](../../agents/research.py#L604) | 604 | `"                    \"providers\": [],"` | — |
| [SRC-59CF4B7DE8-L000605](../../agents/research.py#L605) | 605 | `"                    \"queries\": [],"` | — |
| [SRC-59CF4B7DE8-L000606](../../agents/research.py#L606) | 606 | `"                    \"rank_score\": 0.0,"` | — |
| [SRC-59CF4B7DE8-L000607](../../agents/research.py#L607) | 607 | `"                    \"best_raw_rank\": position,"` | — |
| [SRC-59CF4B7DE8-L000608](../../agents/research.py#L608) | 608 | `"                    \"published_at\": _compact(source.get(\"published_at\") or \"\", 100),"` | — |
| [SRC-59CF4B7DE8-L000609](../../agents/research.py#L609) | 609 | `"                    \"publisher_name\": _compact(source.get(\"publisher_name\") or \"\", 200),"` | — |
| [SRC-59CF4B7DE8-L000610](../../agents/research.py#L610) | 610 | `"                    \"publisher_url\": publisher_url,"` | — |
| [SRC-59CF4B7DE8-L000611](../../agents/research.py#L611) | 611 | `"                    \"publisher_domain\": _compact(source.get(\"publisher_domain\") or \"\", 300),"` | — |
| [SRC-59CF4B7DE8-L000612](../../agents/research.py#L612) | 612 | `"                }"` | — |
| [SRC-59CF4B7DE8-L000613](../../agents/research.py#L613) | 613 | `"                entry.update(classify_source(source_identity_url))"` | — |
| [SRC-59CF4B7DE8-L000614](../../agents/research.py#L614) | 614 | `"                accumulated[url] = entry"` | — |
| [SRC-59CF4B7DE8-L000615](../../agents/research.py#L615) | 615 | `"            elif source.get(\"publisher_url\") and not entry.get(\"publisher_url\"):"` | — |
| [SRC-59CF4B7DE8-L000616](../../agents/research.py#L616) | 616 | `"                entry[\"publisher_url\"] = _compact(source.get(\"publisher_url\"), 2048)"` | — |
| [SRC-59CF4B7DE8-L000617](../../agents/research.py#L617) | 617 | `"                entry[\"publisher_name\"] = _compact(source.get(\"publisher_name\") or \"\", 200)"` | — |
| [SRC-59CF4B7DE8-L000618](../../agents/research.py#L618) | 618 | `"                entry[\"publisher_domain\"] = _compact(source.get(\"publisher_domain\") or \"\", 300)"` | — |
| [SRC-59CF4B7DE8-L000619](../../agents/research.py#L619) | 619 | `"                entry.update(classify_source(entry[\"publisher_url\"]))"` | — |
| [SRC-59CF4B7DE8-L000620](../../agents/research.py#L620) | 620 | `"            entry[\"rank_score\"] += 1.0 / (60 + position)"` | — |
| [SRC-59CF4B7DE8-L000621](../../agents/research.py#L621) | 621 | `"            entry[\"best_raw_rank\"] = min(entry[\"best_raw_rank\"], position)"` | — |
| [SRC-59CF4B7DE8-L000622](../../agents/research.py#L622) | 622 | `"            if provider and provider not in entry[\"providers\"]:"` | — |
| [SRC-59CF4B7DE8-L000623](../../agents/research.py#L623) | 623 | `"                entry[\"providers\"].append(provider)"` | — |
| [SRC-59CF4B7DE8-L000624](../../agents/research.py#L624) | 624 | `"            if query and query not in entry[\"queries\"]:"` | — |
| [SRC-59CF4B7DE8-L000625](../../agents/research.py#L625) | 625 | `"                entry[\"queries\"].append(query)"` | — |
| [SRC-59CF4B7DE8-L000626](../../agents/research.py#L626) | 626 | `"            if len(str(source.get(\"snippet\") or \"\")) > len(entry[\"snippet\"]):"` | — |
| [SRC-59CF4B7DE8-L000627](../../agents/research.py#L627) | 627 | `"                entry[\"snippet\"] = _compact(source.get(\"snippet\"), 1800)"` | — |
| [SRC-59CF4B7DE8-L000628](../../agents/research.py#L628) | 628 | `"            if source.get(\"published_at\") and not entry.get(\"published_at\"):"` | — |
| [SRC-59CF4B7DE8-L000629](../../agents/research.py#L629) | 629 | `"                entry[\"published_at\"] = _compact(source[\"published_at\"], 100)"` | — |
| [SRC-59CF4B7DE8-L000630](../../agents/research.py#L630) | 630 | `"            if source.get(\"page_text\") and not entry[\"page_text\"]:"` | — |
| [SRC-59CF4B7DE8-L000631](../../agents/research.py#L631) | 631 | `"                entry[\"page_text\"] = _compact(source[\"page_text\"], 12_000)"` | — |
| [SRC-59CF4B7DE8-L000632](../../agents/research.py#L632) | 632 | `"                entry[\"page_fetched\"] = True"` | — |
| [SRC-59CF4B7DE8-L000633](../../agents/research.py#L633) | 633 | `"    # A cross-query result gets a modest consensus bonus; official/academic sources"` | — |
| [SRC-59CF4B7DE8-L000634](../../agents/research.py#L634) | 634 | `"    # get a small prior, never enough to override actual query relevance."` | — |
| [SRC-59CF4B7DE8-L000635](../../agents/research.py#L635) | 635 | `"    for entry in accumulated.values():"` | — |
| [SRC-59CF4B7DE8-L000636](../../agents/research.py#L636) | 636 | `"        entry[\"rank_score\"] += min(len(entry[\"queries\"]), 4) * 0.00015"` | — |
| [SRC-59CF4B7DE8-L000637](../../agents/research.py#L637) | 637 | `"        if entry[\"source_class\"] in {\"government\", \"academic\"}:"` | — |
| [SRC-59CF4B7DE8-L000638](../../agents/research.py#L638) | 638 | `"            entry[\"rank_score\"] += 0.0001"` | — |
| [SRC-59CF4B7DE8-L000639](../../agents/research.py#L639) | 639 | `"        if \"user_supplied_url\" in entry[\"providers\"]:"` | — |
| [SRC-59CF4B7DE8-L000640](../../agents/research.py#L640) | 640 | `"            entry[\"rank_score\"] += 0.5"` | — |
| [SRC-59CF4B7DE8-L000641](../../agents/research.py#L641) | 641 | `"    ranked = sorted(accumulated.values(), key=lambda item: item[\"rank_score\"], reverse=True)"` | — |
| [SRC-59CF4B7DE8-L000642](../../agents/research.py#L642) | 642 | `"    return ranked[:max(1, min(int(limit), MAX_FUSED_RESULTS))]"` | — |
| [SRC-59CF4B7DE8-L000643](../../agents/research.py#L643) | 643 | `""` | — |
| [SRC-59CF4B7DE8-L000644](../../agents/research.py#L644) | 644 | `""` | — |
| [SRC-59CF4B7DE8-L000645](../../agents/research.py#L645) | 645 | `""` | — |
| [SRC-59CF4B7DE8-L000646](../../agents/research.py#L646) | 646 | `"def _parse_publication_date(value: Any, now: datetime \| None = None) -> datetime \| None:"` | — |
| [SRC-59CF4B7DE8-L000647](../../agents/research.py#L647) | 647 | `"    \"\"\"Parse common search/RSS publication dates without guessing missing dates.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000648](../../agents/research.py#L648) | 648 | `"    if not isinstance(value, str) or not value.strip():"` | — |
| [SRC-59CF4B7DE8-L000649](../../agents/research.py#L649) | 649 | `"        return None"` | — |
| [SRC-59CF4B7DE8-L000650](../../agents/research.py#L650) | 650 | `"    raw = value.strip()"` | — |
| [SRC-59CF4B7DE8-L000651](../../agents/research.py#L651) | 651 | `"    current = now or datetime.now(UTC)"` | — |
| [SRC-59CF4B7DE8-L000652](../../agents/research.py#L652) | 652 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000653](../../agents/research.py#L653) | 653 | `"        parsed = parsedate_to_datetime(raw)"` | — |
| [SRC-59CF4B7DE8-L000654](../../agents/research.py#L654) | 654 | `"        if parsed:"` | — |
| [SRC-59CF4B7DE8-L000655](../../agents/research.py#L655) | 655 | `"            return parsed.replace(tzinfo=parsed.tzinfo or UTC).astimezone(UTC)"` | — |
| [SRC-59CF4B7DE8-L000656](../../agents/research.py#L656) | 656 | `"    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-59CF4B7DE8-L000657](../../agents/research.py#L657) | 657 | `"        pass"` | — |
| [SRC-59CF4B7DE8-L000658](../../agents/research.py#L658) | 658 | `"    iso_value = raw.replace(\"Z\", \"+00:00\")"` | — |
| [SRC-59CF4B7DE8-L000659](../../agents/research.py#L659) | 659 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000660](../../agents/research.py#L660) | 660 | `"        parsed = datetime.fromisoformat(iso_value)"` | — |
| [SRC-59CF4B7DE8-L000661](../../agents/research.py#L661) | 661 | `"        return parsed.replace(tzinfo=parsed.tzinfo or UTC).astimezone(UTC)"` | — |
| [SRC-59CF4B7DE8-L000662](../../agents/research.py#L662) | 662 | `"    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-59CF4B7DE8-L000663](../../agents/research.py#L663) | 663 | `"        pass"` | — |
| [SRC-59CF4B7DE8-L000664](../../agents/research.py#L664) | 664 | `"    for date_format in (\"%b %d, %Y\", \"%B %d, %Y\", \"%Y/%m/%d\", \"%d %b %Y\"):"` | — |
| [SRC-59CF4B7DE8-L000665](../../agents/research.py#L665) | 665 | `"        try:"` | — |
| [SRC-59CF4B7DE8-L000666](../../agents/research.py#L666) | 666 | `"            return datetime.strptime(raw, date_format).replace(tzinfo=UTC)"` | — |
| [SRC-59CF4B7DE8-L000667](../../agents/research.py#L667) | 667 | `"        except ValueError:"` | — |
| [SRC-59CF4B7DE8-L000668](../../agents/research.py#L668) | 668 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000669](../../agents/research.py#L669) | 669 | `"    match = re.search(r\"(\\d+)\\s+(hour\|day\|week\|month\|year)s?\\s+ago\", raw, re.IGNORECASE)"` | — |
| [SRC-59CF4B7DE8-L000670](../../agents/research.py#L670) | 670 | `"    if match:"` | — |
| [SRC-59CF4B7DE8-L000671](../../agents/research.py#L671) | 671 | `"        amount = int(match.group(1))"` | — |
| [SRC-59CF4B7DE8-L000672](../../agents/research.py#L672) | 672 | `"        unit = match.group(2).lower()"` | — |
| [SRC-59CF4B7DE8-L000673](../../agents/research.py#L673) | 673 | `"        durations = {"` | — |
| [SRC-59CF4B7DE8-L000674](../../agents/research.py#L674) | 674 | `"            \"hour\": timedelta(hours=amount),"` | — |
| [SRC-59CF4B7DE8-L000675](../../agents/research.py#L675) | 675 | `"            \"day\": timedelta(days=amount),"` | — |
| [SRC-59CF4B7DE8-L000676](../../agents/research.py#L676) | 676 | `"            \"week\": timedelta(days=7 * amount),"` | — |
| [SRC-59CF4B7DE8-L000677](../../agents/research.py#L677) | 677 | `"            \"month\": timedelta(days=30 * amount),"` | — |
| [SRC-59CF4B7DE8-L000678](../../agents/research.py#L678) | 678 | `"            \"year\": timedelta(days=365 * amount),"` | — |
| [SRC-59CF4B7DE8-L000679](../../agents/research.py#L679) | 679 | `"        }"` | — |
| [SRC-59CF4B7DE8-L000680](../../agents/research.py#L680) | 680 | `"        return current - durations[unit]"` | — |
| [SRC-59CF4B7DE8-L000681](../../agents/research.py#L681) | 681 | `"    if raw.lower() in {\"today\", \"just now\", \"now\"}:"` | — |
| [SRC-59CF4B7DE8-L000682](../../agents/research.py#L682) | 682 | `"        return current"` | — |
| [SRC-59CF4B7DE8-L000683](../../agents/research.py#L683) | 683 | `"    if raw.lower() == \"yesterday\":"` | — |
| [SRC-59CF4B7DE8-L000684](../../agents/research.py#L684) | 684 | `"        return current - timedelta(days=1)"` | — |
| [SRC-59CF4B7DE8-L000685](../../agents/research.py#L685) | 685 | `"    return None"` | — |
| [SRC-59CF4B7DE8-L000686](../../agents/research.py#L686) | 686 | `""` | — |
| [SRC-59CF4B7DE8-L000687](../../agents/research.py#L687) | 687 | `""` | — |
| [SRC-59CF4B7DE8-L000688](../../agents/research.py#L688) | 688 | `"def evidence_signal_report("` | — |
| [SRC-59CF4B7DE8-L000689](../../agents/research.py#L689) | 689 | `"    sources: list[dict[str, Any]],"` | — |
| [SRC-59CF4B7DE8-L000690](../../agents/research.py#L690) | 690 | `"    freshness: str = \"any\","` | — |
| [SRC-59CF4B7DE8-L000691](../../agents/research.py#L691) | 691 | `"    now: datetime \| None = None,"` | — |
| [SRC-59CF4B7DE8-L000692](../../agents/research.py#L692) | 692 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000693](../../agents/research.py#L693) | 693 | `"    \"\"\"Summarize research coverage; signals describe evidence coverage, not factual truth.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000694](../../agents/research.py#L694) | 694 | `"    current = now or datetime.now(UTC)"` | — |
| [SRC-59CF4B7DE8-L000695](../../agents/research.py#L695) | 695 | `"    valid_sources = [source for source in sources if isinstance(source, dict) and source.get(\"url\")]"` | — |
| [SRC-59CF4B7DE8-L000696](../../agents/research.py#L696) | 696 | `"    domains = {"` | — |
| [SRC-59CF4B7DE8-L000697](../../agents/research.py#L697) | 697 | `"        registrable_domain("` | — |
| [SRC-59CF4B7DE8-L000698](../../agents/research.py#L698) | 698 | `"            source.get(\"domain\") or urlparse(str(source.get(\"url\") or \"\")).hostname or \"\""` | — |
| [SRC-59CF4B7DE8-L000699](../../agents/research.py#L699) | 699 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000700](../../agents/research.py#L700) | 700 | `"        for source in valid_sources"` | — |
| [SRC-59CF4B7DE8-L000701](../../agents/research.py#L701) | 701 | `"        if source.get(\"domain\") or source.get(\"url\")"` | — |
| [SRC-59CF4B7DE8-L000702](../../agents/research.py#L702) | 702 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000703](../../agents/research.py#L703) | 703 | `"    domains.discard(\"\")"` | — |
| [SRC-59CF4B7DE8-L000704](../../agents/research.py#L704) | 704 | `"    providers: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000705](../../agents/research.py#L705) | 705 | `"    for source in valid_sources:"` | — |
| [SRC-59CF4B7DE8-L000706](../../agents/research.py#L706) | 706 | `"        candidate_providers = source.get(\"providers\", [])"` | — |
| [SRC-59CF4B7DE8-L000707](../../agents/research.py#L707) | 707 | `"        if isinstance(candidate_providers, list):"` | — |
| [SRC-59CF4B7DE8-L000708](../../agents/research.py#L708) | 708 | `"            providers.update(str(item) for item in candidate_providers if item)"` | — |
| [SRC-59CF4B7DE8-L000709](../../agents/research.py#L709) | 709 | `"        elif source.get(\"provider\"):"` | — |
| [SRC-59CF4B7DE8-L000710](../../agents/research.py#L710) | 710 | `"            providers.add(str(source[\"provider\"]))"` | — |
| [SRC-59CF4B7DE8-L000711](../../agents/research.py#L711) | 711 | `"    classes = [str(source.get(\"source_class\") or \"general\") for source in valid_sources]"` | — |
| [SRC-59CF4B7DE8-L000712](../../agents/research.py#L712) | 712 | `"    primary_count = sum(item in {\"government\", \"academic\", \"official\"} for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000713](../../agents/research.py#L713) | 713 | `"    news_count = sum(item == \"news\" for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000714](../../agents/research.py#L714) | 714 | `"    social_count = sum(item == \"social\" for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000715](../../agents/research.py#L715) | 715 | `"    pages_read = sum(bool(source.get(\"page_fetched\")) for source in valid_sources)"` | — |
| [SRC-59CF4B7DE8-L000716](../../agents/research.py#L716) | 716 | `"    dates = ["` | — |
| [SRC-59CF4B7DE8-L000717](../../agents/research.py#L717) | 717 | `"        parsed"` | — |
| [SRC-59CF4B7DE8-L000718](../../agents/research.py#L718) | 718 | `"        for source in valid_sources"` | — |
| [SRC-59CF4B7DE8-L000719](../../agents/research.py#L719) | 719 | `"        if (parsed := _parse_publication_date(source.get(\"published_at\"), current)) is not None"` | — |
| [SRC-59CF4B7DE8-L000720](../../agents/research.py#L720) | 720 | `"    ]"` | — |
| [SRC-59CF4B7DE8-L000721](../../agents/research.py#L721) | 721 | `"    recent_days = 7 if freshness == \"current\" else 30"` | — |
| [SRC-59CF4B7DE8-L000722](../../agents/research.py#L722) | 722 | `"    recent_count = sum((current - parsed).total_seconds() >= 0 and"` | — |
| [SRC-59CF4B7DE8-L000723](../../agents/research.py#L723) | 723 | `"                       (current - parsed) <= timedelta(days=recent_days) for parsed in dates)"` | — |
| [SRC-59CF4B7DE8-L000724](../../agents/research.py#L724) | 724 | `"    future_dates = sum(parsed > current + timedelta(days=1) for parsed in dates)"` | — |
| [SRC-59CF4B7DE8-L000725](../../agents/research.py#L725) | 725 | `"    unique_sources = len(valid_sources)"` | — |
| [SRC-59CF4B7DE8-L000726](../../agents/research.py#L726) | 726 | `"    # Evidence coverage uses several independent dimensions and is deliberately not a"` | — |
| [SRC-59CF4B7DE8-L000727](../../agents/research.py#L727) | 727 | `"    # probability that any factual claim is true."` | — |
| [SRC-59CF4B7DE8-L000728](../../agents/research.py#L728) | 728 | `"    coverage_points = 0"` | — |
| [SRC-59CF4B7DE8-L000729](../../agents/research.py#L729) | 729 | `"    coverage_points += min(unique_sources, 10) * 3"` | — |
| [SRC-59CF4B7DE8-L000730](../../agents/research.py#L730) | 730 | `"    coverage_points += min(len(domains), 8) * 4"` | — |
| [SRC-59CF4B7DE8-L000731](../../agents/research.py#L731) | 731 | `"    coverage_points += min(len(providers), 4) * 5"` | — |
| [SRC-59CF4B7DE8-L000732](../../agents/research.py#L732) | 732 | `"    coverage_points += min(pages_read, 8) * 3"` | — |
| [SRC-59CF4B7DE8-L000733](../../agents/research.py#L733) | 733 | `"    coverage_points += min(primary_count, 4) * 4"` | — |
| [SRC-59CF4B7DE8-L000734](../../agents/research.py#L734) | 734 | `"    coverage_points += min(len(dates), 8) * 2"` | — |
| [SRC-59CF4B7DE8-L000735](../../agents/research.py#L735) | 735 | `"    coverage_score = min(100, coverage_points)"` | — |
| [SRC-59CF4B7DE8-L000736](../../agents/research.py#L736) | 736 | `"    if unique_sources >= 8 and len(domains) >= 5 and len(providers) >= 2 and pages_read >= 3:"` | — |
| [SRC-59CF4B7DE8-L000737](../../agents/research.py#L737) | 737 | `"        coverage_level = \"متعدد المصادر\""` | — |
| [SRC-59CF4B7DE8-L000738](../../agents/research.py#L738) | 738 | `"    elif unique_sources >= 4 and len(domains) >= 3 and len(providers) >= 1:"` | — |
| [SRC-59CF4B7DE8-L000739](../../agents/research.py#L739) | 739 | `"        coverage_level = \"متوسط\""` | — |
| [SRC-59CF4B7DE8-L000740](../../agents/research.py#L740) | 740 | `"    else:"` | — |
| [SRC-59CF4B7DE8-L000741](../../agents/research.py#L741) | 741 | `"        coverage_level = \"محدود\""` | — |
| [SRC-59CF4B7DE8-L000742](../../agents/research.py#L742) | 742 | `""` | — |
| [SRC-59CF4B7DE8-L000743](../../agents/research.py#L743) | 743 | `"    warnings: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000744](../../agents/research.py#L744) | 744 | `"    if unique_sources == 0:"` | — |
| [SRC-59CF4B7DE8-L000745](../../agents/research.py#L745) | 745 | `"        warnings.append(\"لا توجد مصادر قابلة للاستشهاد؛ لا تستنتج حقائق من عدم وجود نتائج.\")"` | — |
| [SRC-59CF4B7DE8-L000746](../../agents/research.py#L746) | 746 | `"    if len(domains) < 3:"` | — |
| [SRC-59CF4B7DE8-L000747](../../agents/research.py#L747) | 747 | `"        warnings.append(\"تنوع النطاقات محدود؛ لا تعتبر تكرار النتيجة تأكيدًا مستقلًا.\")"` | — |
| [SRC-59CF4B7DE8-L000748](../../agents/research.py#L748) | 748 | `"    if pages_read < 2 and unique_sources:"` | — |
| [SRC-59CF4B7DE8-L000749](../../agents/research.py#L749) | 749 | `"        warnings.append(\"تمت قراءة أقل من صفحتين مباشرة؛ بعض الأدلة مقتطفات من محركات البحث فقط.\")"` | — |
| [SRC-59CF4B7DE8-L000750](../../agents/research.py#L750) | 750 | `"    if freshness == \"current\":"` | — |
| [SRC-59CF4B7DE8-L000751](../../agents/research.py#L751) | 751 | `"        if not dates:"` | — |
| [SRC-59CF4B7DE8-L000752](../../agents/research.py#L752) | 752 | `"            warnings.append(\"لا تتوفر تواريخ نشر قابلة للتحليل؛ حداثة النتائج غير مؤكدة.\")"` | — |
| [SRC-59CF4B7DE8-L000753](../../agents/research.py#L753) | 753 | `"        elif recent_count == 0:"` | — |
| [SRC-59CF4B7DE8-L000754](../../agents/research.py#L754) | 754 | `"            warnings.append(f\"لم يُعثر على مصدر مؤرخ خلال آخر {recent_days} يومًا ضمن التواريخ القابلة للتحليل.\")"` | — |
| [SRC-59CF4B7DE8-L000755](../../agents/research.py#L755) | 755 | `"    if future_dates:"` | — |
| [SRC-59CF4B7DE8-L000756](../../agents/research.py#L756) | 756 | `"        warnings.append(\"توجد تواريخ مستقبلية غير متوقعة؛ يجب مراجعتها يدويًا.\")"` | — |
| [SRC-59CF4B7DE8-L000757](../../agents/research.py#L757) | 757 | `"    if social_count and primary_count == 0:"` | — |
| [SRC-59CF4B7DE8-L000758](../../agents/research.py#L758) | 758 | `"        warnings.append(\"المصادر اجتماعية فقط دون مصدر رسمي/أكاديمي؛ تعامل معها كآراء أو إشارات لا كحقائق مثبتة.\")"` | — |
| [SRC-59CF4B7DE8-L000759](../../agents/research.py#L759) | 759 | `"    return {"` | — |
| [SRC-59CF4B7DE8-L000760](../../agents/research.py#L760) | 760 | `"        \"unique_sources\": unique_sources,"` | — |
| [SRC-59CF4B7DE8-L000761](../../agents/research.py#L761) | 761 | `"        \"unique_domains\": len(domains),"` | — |
| [SRC-59CF4B7DE8-L000762](../../agents/research.py#L762) | 762 | `"        \"providers_count\": len(providers),"` | — |
| [SRC-59CF4B7DE8-L000763](../../agents/research.py#L763) | 763 | `"        \"providers\": sorted(providers),"` | — |
| [SRC-59CF4B7DE8-L000764](../../agents/research.py#L764) | 764 | `"        \"pages_read\": pages_read,"` | — |
| [SRC-59CF4B7DE8-L000765](../../agents/research.py#L765) | 765 | `"        \"primary_sources\": primary_count,"` | — |
| [SRC-59CF4B7DE8-L000766](../../agents/research.py#L766) | 766 | `"        \"news_sources\": news_count,"` | — |
| [SRC-59CF4B7DE8-L000767](../../agents/research.py#L767) | 767 | `"        \"social_sources\": social_count,"` | — |
| [SRC-59CF4B7DE8-L000768](../../agents/research.py#L768) | 768 | `"        \"dated_sources\": len(dates),"` | — |
| [SRC-59CF4B7DE8-L000769](../../agents/research.py#L769) | 769 | `"        \"recent_sources\": recent_count,"` | — |
| [SRC-59CF4B7DE8-L000770](../../agents/research.py#L770) | 770 | `"        \"undated_sources\": max(0, unique_sources - len(dates)),"` | — |
| [SRC-59CF4B7DE8-L000771](../../agents/research.py#L771) | 771 | `"        \"date_coverage_percent\": round(100 * len(dates) / unique_sources) if unique_sources else 0,"` | — |
| [SRC-59CF4B7DE8-L000772](../../agents/research.py#L772) | 772 | `"        \"coverage_score\": coverage_score,"` | — |
| [SRC-59CF4B7DE8-L000773](../../agents/research.py#L773) | 773 | `"        \"coverage_level\": coverage_level,"` | — |
| [SRC-59CF4B7DE8-L000774](../../agents/research.py#L774) | 774 | `"        \"score_meaning\": \"مؤشر تغطية وتنوع الأدلة، وليس احتمال صحة الإجابة.\","` | — |
| [SRC-59CF4B7DE8-L000775](../../agents/research.py#L775) | 775 | `"        \"warnings\": warnings,"` | — |
| [SRC-59CF4B7DE8-L000776](../../agents/research.py#L776) | 776 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000777](../../agents/research.py#L777) | 777 | `""` | — |
| [SRC-59CF4B7DE8-L000778](../../agents/research.py#L778) | 778 | `""` | — |
| [SRC-59CF4B7DE8-L000779](../../agents/research.py#L779) | 779 | `""` | — |
| [SRC-59CF4B7DE8-L000780](../../agents/research.py#L780) | 780 | `"# ---------------------------------------------------------------------------"` | — |
| [SRC-59CF4B7DE8-L000781](../../agents/research.py#L781) | 781 | `"# Evidence-aware helpers"` | — |
| [SRC-59CF4B7DE8-L000782](../../agents/research.py#L782) | 782 | `"# ---------------------------------------------------------------------------"` | — |
| [SRC-59CF4B7DE8-L000783](../../agents/research.py#L783) | 783 | `""` | — |
| [SRC-59CF4B7DE8-L000784](../../agents/research.py#L784) | 784 | `"_RELEVANCE_STOPWORDS = {"` | — |
| [SRC-59CF4B7DE8-L000785](../../agents/research.py#L785) | 785 | `"    \"the\", \"a\", \"an\", \"of\", \"in\", \"on\", \"at\", \"to\", \"for\","` | — |
| [SRC-59CF4B7DE8-L000786](../../agents/research.py#L786) | 786 | `"    \"is\", \"are\", \"was\", \"were\", \"be\", \"been\", \"being\","` | — |
| [SRC-59CF4B7DE8-L000787](../../agents/research.py#L787) | 787 | `"    \"and\", \"or\", \"but\", \"not\", \"with\", \"without\","` | — |
| [SRC-59CF4B7DE8-L000788](../../agents/research.py#L788) | 788 | `"    \"this\", \"that\", \"these\", \"those\", \"it\", \"its\","` | — |
| [SRC-59CF4B7DE8-L000789](../../agents/research.py#L789) | 789 | `"}"` | — |
| [SRC-59CF4B7DE8-L000790](../../agents/research.py#L790) | 790 | `""` | — |
| [SRC-59CF4B7DE8-L000791](../../agents/research.py#L791) | 791 | `"_OFFICIAL_CLASSES = {\"government\", \"education\", \"official\"}"` | — |
| [SRC-59CF4B7DE8-L000792](../../agents/research.py#L792) | 792 | `""` | — |
| [SRC-59CF4B7DE8-L000793](../../agents/research.py#L793) | 793 | `""` | — |
| [SRC-59CF4B7DE8-L000794](../../agents/research.py#L794) | 794 | `"def _tokenize(text: str) -> set:"` | — |
| [SRC-59CF4B7DE8-L000795](../../agents/research.py#L795) | 795 | `"    if not text:"` | — |
| [SRC-59CF4B7DE8-L000796](../../agents/research.py#L796) | 796 | `"        return set()"` | — |
| [SRC-59CF4B7DE8-L000797](../../agents/research.py#L797) | 797 | `"    norm = _normalize_arabic(text.casefold())"` | — |
| [SRC-59CF4B7DE8-L000798](../../agents/research.py#L798) | 798 | `"    tokens = re.findall(r\"\\w+\", norm, flags=re.UNICODE)"` | — |
| [SRC-59CF4B7DE8-L000799](../../agents/research.py#L799) | 799 | `"    return {t for t in tokens if len(t) >= 3 and t not in _RELEVANCE_STOPWORDS}"` | — |
| [SRC-59CF4B7DE8-L000800](../../agents/research.py#L800) | 800 | `""` | — |
| [SRC-59CF4B7DE8-L000801](../../agents/research.py#L801) | 801 | `""` | — |
| [SRC-59CF4B7DE8-L000802](../../agents/research.py#L802) | 802 | `"def source_relevance_score(src, query: str) -> dict:"` | — |
| [SRC-59CF4B7DE8-L000803](../../agents/research.py#L803) | 803 | `"    if not isinstance(src, dict):"` | — |
| [SRC-59CF4B7DE8-L000804](../../agents/research.py#L804) | 804 | `"        return {\"accepted\": False, \"score\": 0, \"reason\": \"malformed\"}"` | — |
| [SRC-59CF4B7DE8-L000805](../../agents/research.py#L805) | 805 | `""` | — |
| [SRC-59CF4B7DE8-L000806](../../agents/research.py#L806) | 806 | `"    title = str(src.get(\"title\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000807](../../agents/research.py#L807) | 807 | `"    snippet = str(src.get(\"snippet\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000808](../../agents/research.py#L808) | 808 | `"    page_text = str(src.get(\"page_text\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000809](../../agents/research.py#L809) | 809 | `"    source_class = str(src.get(\"source_class\") or \"general\").lower()"` | — |
| [SRC-59CF4B7DE8-L000810](../../agents/research.py#L810) | 810 | `""` | — |
| [SRC-59CF4B7DE8-L000811](../../agents/research.py#L811) | 811 | `"    q_tokens = _tokenize(query)"` | — |
| [SRC-59CF4B7DE8-L000812](../../agents/research.py#L812) | 812 | `"    if not q_tokens:"` | — |
| [SRC-59CF4B7DE8-L000813](../../agents/research.py#L813) | 813 | `"        return {\"accepted\": False, \"score\": 0, \"reason\": \"no_query_tokens\"}"` | — |
| [SRC-59CF4B7DE8-L000814](../../agents/research.py#L814) | 814 | `""` | — |
| [SRC-59CF4B7DE8-L000815](../../agents/research.py#L815) | 815 | `"    t_tokens = _tokenize(title)"` | — |
| [SRC-59CF4B7DE8-L000816](../../agents/research.py#L816) | 816 | `"    s_tokens = _tokenize(snippet)"` | — |
| [SRC-59CF4B7DE8-L000817](../../agents/research.py#L817) | 817 | `"    p_tokens = _tokenize(page_text[:3000])"` | — |
| [SRC-59CF4B7DE8-L000818](../../agents/research.py#L818) | 818 | `""` | — |
| [SRC-59CF4B7DE8-L000819](../../agents/research.py#L819) | 819 | `"    title_ratio = len(q_tokens & t_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000820](../../agents/research.py#L820) | 820 | `"    snippet_ratio = len(q_tokens & s_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000821](../../agents/research.py#L821) | 821 | `"    page_ratio = len(q_tokens & p_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000822](../../agents/research.py#L822) | 822 | `""` | — |
| [SRC-59CF4B7DE8-L000823](../../agents/research.py#L823) | 823 | `"    score = int(title_ratio * 15 + snippet_ratio * 20 + page_ratio * 5)"` | — |
| [SRC-59CF4B7DE8-L000824](../../agents/research.py#L824) | 824 | `""` | — |
| [SRC-59CF4B7DE8-L000825](../../agents/research.py#L825) | 825 | `"    if source_class in _OFFICIAL_CLASSES:"` | — |
| [SRC-59CF4B7DE8-L000826](../../agents/research.py#L826) | 826 | `"        if score >= 5:"` | — |
| [SRC-59CF4B7DE8-L000827](../../agents/research.py#L827) | 827 | `"            return {\"accepted\": True, \"score\": score, \"reason\": \"accepted\"}"` | — |
| [SRC-59CF4B7DE8-L000828](../../agents/research.py#L828) | 828 | `"        return {\"accepted\": True, \"score\": score,"` | — |
| [SRC-59CF4B7DE8-L000829](../../agents/research.py#L829) | 829 | `"                \"reason\": \"kept_official_despite_low_overlap\"}"` | — |
| [SRC-59CF4B7DE8-L000830](../../agents/research.py#L830) | 830 | `""` | — |
| [SRC-59CF4B7DE8-L000831](../../agents/research.py#L831) | 831 | `"    if score >= 18:"` | — |
| [SRC-59CF4B7DE8-L000832](../../agents/research.py#L832) | 832 | `"        return {\"accepted\": True, \"score\": score, \"reason\": \"accepted\"}"` | — |
| [SRC-59CF4B7DE8-L000833](../../agents/research.py#L833) | 833 | `"    return {\"accepted\": False, \"score\": score, \"reason\": \"low_overlap\"}"` | — |
| [SRC-59CF4B7DE8-L000834](../../agents/research.py#L834) | 834 | `""` | — |
| [SRC-59CF4B7DE8-L000835](../../agents/research.py#L835) | 835 | `""` | — |
| [SRC-59CF4B7DE8-L000836](../../agents/research.py#L836) | 836 | `"def filter_relevant_sources(sources, query: str, extra_queries=None):"` | — |
| [SRC-59CF4B7DE8-L000837](../../agents/research.py#L837) | 837 | `"    kept = []"` | — |
| [SRC-59CF4B7DE8-L000838](../../agents/research.py#L838) | 838 | `"    diag = []"` | — |
| [SRC-59CF4B7DE8-L000839](../../agents/research.py#L839) | 839 | `"    seen_urls = set()"` | — |
| [SRC-59CF4B7DE8-L000840](../../agents/research.py#L840) | 840 | `"    seen_titles = set()"` | — |
| [SRC-59CF4B7DE8-L000841](../../agents/research.py#L841) | 841 | `"    combined = \" \".join([query] + list(extra_queries or []))"` | — |
| [SRC-59CF4B7DE8-L000842](../../agents/research.py#L842) | 842 | `""` | — |
| [SRC-59CF4B7DE8-L000843](../../agents/research.py#L843) | 843 | `"    for src in sources or []:"` | — |
| [SRC-59CF4B7DE8-L000844](../../agents/research.py#L844) | 844 | `"        if not isinstance(src, dict):"` | — |
| [SRC-59CF4B7DE8-L000845](../../agents/research.py#L845) | 845 | `"            diag.append({\"reason\": \"malformed\", \"url\": \"\"})"` | — |
| [SRC-59CF4B7DE8-L000846](../../agents/research.py#L846) | 846 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000847](../../agents/research.py#L847) | 847 | `"        url = str(src.get(\"url\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000848](../../agents/research.py#L848) | 848 | `"        domain = str(src.get(\"domain\") or \"\").lower()"` | — |
| [SRC-59CF4B7DE8-L000849](../../agents/research.py#L849) | 849 | `"        title = str(src.get(\"title\") or \"\").strip()"` | — |
| [SRC-59CF4B7DE8-L000850](../../agents/research.py#L850) | 850 | `"        url_key = url.rstrip(\"/\").lower()"` | — |
| [SRC-59CF4B7DE8-L000851](../../agents/research.py#L851) | 851 | `"        title_key = title.lower() + \"\|\" + domain"` | — |
| [SRC-59CF4B7DE8-L000852](../../agents/research.py#L852) | 852 | `""` | — |
| [SRC-59CF4B7DE8-L000853](../../agents/research.py#L853) | 853 | `"        if url_key and url_key in seen_urls:"` | — |
| [SRC-59CF4B7DE8-L000854](../../agents/research.py#L854) | 854 | `"            diag.append({\"reason\": \"duplicate_url\", \"url\": url})"` | — |
| [SRC-59CF4B7DE8-L000855](../../agents/research.py#L855) | 855 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000856](../../agents/research.py#L856) | 856 | `"        if title and title_key in seen_titles:"` | — |
| [SRC-59CF4B7DE8-L000857](../../agents/research.py#L857) | 857 | `"            diag.append({\"reason\": \"duplicate_title_domain\", \"url\": url})"` | — |
| [SRC-59CF4B7DE8-L000858](../../agents/research.py#L858) | 858 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000859](../../agents/research.py#L859) | 859 | `""` | — |
| [SRC-59CF4B7DE8-L000860](../../agents/research.py#L860) | 860 | `"        rel = source_relevance_score(src, combined)"` | — |
| [SRC-59CF4B7DE8-L000861](../../agents/research.py#L861) | 861 | `"        if not rel[\"accepted\"]:"` | — |
| [SRC-59CF4B7DE8-L000862](../../agents/research.py#L862) | 862 | `"            diag.append({\"reason\": rel[\"reason\"], \"url\": url, \"score\": rel[\"score\"]})"` | — |
| [SRC-59CF4B7DE8-L000863](../../agents/research.py#L863) | 863 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000864](../../agents/research.py#L864) | 864 | `""` | — |
| [SRC-59CF4B7DE8-L000865](../../agents/research.py#L865) | 865 | `"        kept.append(src)"` | — |
| [SRC-59CF4B7DE8-L000866](../../agents/research.py#L866) | 866 | `"        if url_key:"` | — |
| [SRC-59CF4B7DE8-L000867](../../agents/research.py#L867) | 867 | `"            seen_urls.add(url_key)"` | — |
| [SRC-59CF4B7DE8-L000868](../../agents/research.py#L868) | 868 | `"        if title:"` | — |
| [SRC-59CF4B7DE8-L000869](../../agents/research.py#L869) | 869 | `"            seen_titles.add(title_key)"` | — |
| [SRC-59CF4B7DE8-L000870](../../agents/research.py#L870) | 870 | `"    return kept, diag"` | — |
| [SRC-59CF4B7DE8-L000871](../../agents/research.py#L871) | 871 | `""` | — |
| [SRC-59CF4B7DE8-L000872](../../agents/research.py#L872) | 872 | `""` | — |
| [SRC-59CF4B7DE8-L000873](../../agents/research.py#L873) | 873 | `"def decide_evidence_status(sources, pages_read: int = 0,"` | — |
| [SRC-59CF4B7DE8-L000874](../../agents/research.py#L874) | 874 | `"                           provider_failures: int = 0,"` | — |
| [SRC-59CF4B7DE8-L000875](../../agents/research.py#L875) | 875 | `"                           search_attempted: bool = True) -> dict:"` | — |
| [SRC-59CF4B7DE8-L000876](../../agents/research.py#L876) | 876 | `"    if not search_attempted:"` | — |
| [SRC-59CF4B7DE8-L000877](../../agents/research.py#L877) | 877 | `"        return {\"evidence_status\": \"failed\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000878](../../agents/research.py#L878) | 878 | `""` | — |
| [SRC-59CF4B7DE8-L000879](../../agents/research.py#L879) | 879 | `"    domains = set()"` | — |
| [SRC-59CF4B7DE8-L000880](../../agents/research.py#L880) | 880 | `"    has_official = False"` | — |
| [SRC-59CF4B7DE8-L000881](../../agents/research.py#L881) | 881 | `"    for s in sources or []:"` | — |
| [SRC-59CF4B7DE8-L000882](../../agents/research.py#L882) | 882 | `"        if not isinstance(s, dict):"` | — |
| [SRC-59CF4B7DE8-L000883](../../agents/research.py#L883) | 883 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000884](../../agents/research.py#L884) | 884 | `"        d = str(s.get(\"domain\") or \"\").lower()"` | — |
| [SRC-59CF4B7DE8-L000885](../../agents/research.py#L885) | 885 | `"        if not d:"` | — |
| [SRC-59CF4B7DE8-L000886](../../agents/research.py#L886) | 886 | `"            url = str(s.get(\"url\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000887](../../agents/research.py#L887) | 887 | `"            if url:"` | — |
| [SRC-59CF4B7DE8-L000888](../../agents/research.py#L888) | 888 | `"                try:"` | — |
| [SRC-59CF4B7DE8-L000889](../../agents/research.py#L889) | 889 | `"                    from urllib.parse import urlparse"` | — |
| [SRC-59CF4B7DE8-L000890](../../agents/research.py#L890) | 890 | `"                    d = urlparse(url).netloc.lower()"` | — |
| [SRC-59CF4B7DE8-L000891](../../agents/research.py#L891) | 891 | `"                except Exception:"` | — |
| [SRC-59CF4B7DE8-L000892](../../agents/research.py#L892) | 892 | `"                    d = \"\""` | — |
| [SRC-59CF4B7DE8-L000893](../../agents/research.py#L893) | 893 | `"        if d:"` | — |
| [SRC-59CF4B7DE8-L000894](../../agents/research.py#L894) | 894 | `"            domains.add(d)"` | — |
| [SRC-59CF4B7DE8-L000895](../../agents/research.py#L895) | 895 | `"        if str(s.get(\"source_class\") or \"\").lower() in _OFFICIAL_CLASSES:"` | — |
| [SRC-59CF4B7DE8-L000896](../../agents/research.py#L896) | 896 | `"            has_official = True"` | — |
| [SRC-59CF4B7DE8-L000897](../../agents/research.py#L897) | 897 | `""` | — |
| [SRC-59CF4B7DE8-L000898](../../agents/research.py#L898) | 898 | `"    if not sources:"` | — |
| [SRC-59CF4B7DE8-L000899](../../agents/research.py#L899) | 899 | `"        if provider_failures > 0:"` | — |
| [SRC-59CF4B7DE8-L000900](../../agents/research.py#L900) | 900 | `"            return {\"evidence_status\": \"failed\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000901](../../agents/research.py#L901) | 901 | `"        return {\"evidence_status\": \"insufficient\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000902](../../agents/research.py#L902) | 902 | `""` | — |
| [SRC-59CF4B7DE8-L000903](../../agents/research.py#L903) | 903 | `"    if len(domains) >= 2 or has_official:"` | — |
| [SRC-59CF4B7DE8-L000904](../../agents/research.py#L904) | 904 | `"        return {\"evidence_status\": \"adequate\", \"should_abstain\": False}"` | — |
| [SRC-59CF4B7DE8-L000905](../../agents/research.py#L905) | 905 | `"    if len(domains) >= 1:"` | — |
| [SRC-59CF4B7DE8-L000906](../../agents/research.py#L906) | 906 | `"        return {\"evidence_status\": \"partial\", \"should_abstain\": False}"` | — |
| [SRC-59CF4B7DE8-L000907](../../agents/research.py#L907) | 907 | `"    return {\"evidence_status\": \"insufficient\", \"should_abstain\": True}"` | — |
## الوكيل والمنطق

### FILE-1E32639872 — [agents/research_completion.py](../../agents/research_completion.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1E32639872-L000001](../../agents/research_completion.py#L1) | 1 | `"\"\"\"Truthful research completion diagnostics, separate from factual correctness.\"\"\""` | — |
| [SRC-1E32639872-L000002](../../agents/research_completion.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-1E32639872-L000003](../../agents/research_completion.py#L3) | 3 | `""` | — |
| [SRC-1E32639872-L000004](../../agents/research_completion.py#L4) | 4 | `"from typing import Any"` | — |
| [SRC-1E32639872-L000005](../../agents/research_completion.py#L5) | 5 | `"from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit"` | — |
| [SRC-1E32639872-L000006](../../agents/research_completion.py#L6) | 6 | `""` | — |
| [SRC-1E32639872-L000007](../../agents/research_completion.py#L7) | 7 | `"from agents.research import registrable_domain"` | — |
| [SRC-1E32639872-L000008](../../agents/research_completion.py#L8) | 8 | `""` | — |
| [SRC-1E32639872-L000009](../../agents/research_completion.py#L9) | 9 | `"_RESEARCH_KINDS = frozenset({"` | — |
| [SRC-1E32639872-L000010](../../agents/research_completion.py#L10) | 10 | `"    \"web_research\", \"web_fallback\", \"insufficient_evidence\","` | — |
| [SRC-1E32639872-L000011](../../agents/research_completion.py#L11) | 11 | `"    \"lead_discovery_no_qualified_candidates\","` | — |
| [SRC-1E32639872-L000012](../../agents/research_completion.py#L12) | 12 | `"})"` | — |
| [SRC-1E32639872-L000013](../../agents/research_completion.py#L13) | 13 | `"_RESEARCH_ERRORS = frozenset({"` | — |
| [SRC-1E32639872-L000014](../../agents/research_completion.py#L14) | 14 | `"    \"attempted_research_error\", \"unknown_after_research_error\","` | — |
| [SRC-1E32639872-L000015](../../agents/research_completion.py#L15) | 15 | `"    \"unknown_after_budget_exhaustion\","` | — |
| [SRC-1E32639872-L000016](../../agents/research_completion.py#L16) | 16 | `"})"` | — |
| [SRC-1E32639872-L000017](../../agents/research_completion.py#L17) | 17 | `"_CONNECTOR_OK = frozenset({\"ok\", \"no_results\", \"filtered_all\", \"passed\"})"` | — |
| [SRC-1E32639872-L000018](../../agents/research_completion.py#L18) | 18 | `"_CONNECTOR_ERRORS = frozenset({"` | — |
| [SRC-1E32639872-L000019](../../agents/research_completion.py#L19) | 19 | `"    \"failed\", \"timeout\", \"error\", \"not_configured\", \"disabled\","` | — |
| [SRC-1E32639872-L000020](../../agents/research_completion.py#L20) | 20 | `"    \"rate_limited\", \"blocked\","` | — |
| [SRC-1E32639872-L000021](../../agents/research_completion.py#L21) | 21 | `"})"` | — |
| [SRC-1E32639872-L000022](../../agents/research_completion.py#L22) | 22 | `"_TRACKING_KEYS = frozenset({\"fbclid\", \"gclid\", \"mc_cid\", \"mc_eid\"})"` | — |
| [SRC-1E32639872-L000023](../../agents/research_completion.py#L23) | 23 | `""` | — |
| [SRC-1E32639872-L000024](../../agents/research_completion.py#L24) | 24 | `""` | — |
| [SRC-1E32639872-L000025](../../agents/research_completion.py#L25) | 25 | `"def _dict(value: Any) -> dict[str, Any]:"` | — |
| [SRC-1E32639872-L000026](../../agents/research_completion.py#L26) | 26 | `"    return value if isinstance(value, dict) else {}"` | — |
| [SRC-1E32639872-L000027](../../agents/research_completion.py#L27) | 27 | `""` | — |
| [SRC-1E32639872-L000028](../../agents/research_completion.py#L28) | 28 | `""` | — |
| [SRC-1E32639872-L000029](../../agents/research_completion.py#L29) | 29 | `"def _list(value: Any) -> list[Any]:"` | — |
| [SRC-1E32639872-L000030](../../agents/research_completion.py#L30) | 30 | `"    return value if isinstance(value, list) else []"` | — |
| [SRC-1E32639872-L000031](../../agents/research_completion.py#L31) | 31 | `""` | — |
| [SRC-1E32639872-L000032](../../agents/research_completion.py#L32) | 32 | `""` | — |
| [SRC-1E32639872-L000033](../../agents/research_completion.py#L33) | 33 | `"def _int(value: Any) -> int \| None:"` | — |
| [SRC-1E32639872-L000034](../../agents/research_completion.py#L34) | 34 | `"    if isinstance(value, bool):"` | — |
| [SRC-1E32639872-L000035](../../agents/research_completion.py#L35) | 35 | `"        return None"` | — |
| [SRC-1E32639872-L000036](../../agents/research_completion.py#L36) | 36 | `"    try:"` | — |
| [SRC-1E32639872-L000037](../../agents/research_completion.py#L37) | 37 | `"        return max(0, int(value))"` | — |
| [SRC-1E32639872-L000038](../../agents/research_completion.py#L38) | 38 | `"    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1E32639872-L000039](../../agents/research_completion.py#L39) | 39 | `"        return None"` | — |
| [SRC-1E32639872-L000040](../../agents/research_completion.py#L40) | 40 | `""` | — |
| [SRC-1E32639872-L000041](../../agents/research_completion.py#L41) | 41 | `""` | — |
| [SRC-1E32639872-L000042](../../agents/research_completion.py#L42) | 42 | `"def _readable(source: dict[str, Any]) -> bool:"` | — |
| [SRC-1E32639872-L000043](../../agents/research_completion.py#L43) | 43 | `"    return bool(source.get(\"page_fetched\")) and ("` | — |
| [SRC-1E32639872-L000044](../../agents/research_completion.py#L44) | 44 | `"        bool(str(source.get(\"page_text\") or \"\").strip())"` | — |
| [SRC-1E32639872-L000045](../../agents/research_completion.py#L45) | 45 | `"        or source.get(\"readable_page_text_available\") is True"` | — |
| [SRC-1E32639872-L000046](../../agents/research_completion.py#L46) | 46 | `"    )"` | — |
| [SRC-1E32639872-L000047](../../agents/research_completion.py#L47) | 47 | `""` | — |
| [SRC-1E32639872-L000048](../../agents/research_completion.py#L48) | 48 | `""` | — |
| [SRC-1E32639872-L000049](../../agents/research_completion.py#L49) | 49 | `"def _url_key(value: Any) -> str:"` | — |
| [SRC-1E32639872-L000050](../../agents/research_completion.py#L50) | 50 | `"    try:"` | — |
| [SRC-1E32639872-L000051](../../agents/research_completion.py#L51) | 51 | `"        parts = urlsplit(str(value or \"\").strip())"` | — |
| [SRC-1E32639872-L000052](../../agents/research_completion.py#L52) | 52 | `"        scheme = parts.scheme.lower()"` | — |
| [SRC-1E32639872-L000053](../../agents/research_completion.py#L53) | 53 | `"        if scheme not in {\"http\", \"https\"} or not parts.hostname:"` | — |
| [SRC-1E32639872-L000054](../../agents/research_completion.py#L54) | 54 | `"            return \"\""` | — |
| [SRC-1E32639872-L000055](../../agents/research_completion.py#L55) | 55 | `"        host = parts.hostname.lower().rstrip(\".\")"` | — |
| [SRC-1E32639872-L000056](../../agents/research_completion.py#L56) | 56 | `"        port = parts.port"` | — |
| [SRC-1E32639872-L000057](../../agents/research_completion.py#L57) | 57 | `"        netloc = host if port is None or (scheme, port) in {"` | — |
| [SRC-1E32639872-L000058](../../agents/research_completion.py#L58) | 58 | `"            (\"http\", 80), (\"https\", 443)"` | — |
| [SRC-1E32639872-L000059](../../agents/research_completion.py#L59) | 59 | `"        } else f\"{host}:{port}\""` | — |
| [SRC-1E32639872-L000060](../../agents/research_completion.py#L60) | 60 | `"        query = ["` | — |
| [SRC-1E32639872-L000061](../../agents/research_completion.py#L61) | 61 | `"            (key, val) for key, val in parse_qsl(parts.query, keep_blank_values=True)"` | — |
| [SRC-1E32639872-L000062](../../agents/research_completion.py#L62) | 62 | `"            if key.casefold() not in _TRACKING_KEYS"` | — |
| [SRC-1E32639872-L000063](../../agents/research_completion.py#L63) | 63 | `"            and not key.casefold().startswith(\"utm_\")"` | — |
| [SRC-1E32639872-L000064](../../agents/research_completion.py#L64) | 64 | `"        ]"` | — |
| [SRC-1E32639872-L000065](../../agents/research_completion.py#L65) | 65 | `"        path = parts.path.rstrip(\"/\") or \"/\""` | — |
| [SRC-1E32639872-L000066](../../agents/research_completion.py#L66) | 66 | `"        return urlunsplit((scheme, netloc, path, urlencode(sorted(query)), \"\"))"` | — |
| [SRC-1E32639872-L000067](../../agents/research_completion.py#L67) | 67 | `"    except (TypeError, ValueError):"` | — |
| [SRC-1E32639872-L000068](../../agents/research_completion.py#L68) | 68 | `"        return \"\""` | — |
| [SRC-1E32639872-L000069](../../agents/research_completion.py#L69) | 69 | `""` | — |
| [SRC-1E32639872-L000070](../../agents/research_completion.py#L70) | 70 | `""` | — |
| [SRC-1E32639872-L000071](../../agents/research_completion.py#L71) | 71 | `"def build_research_completion(result: dict[str, Any]) -> dict[str, Any]:"` | — |
| [SRC-1E32639872-L000072](../../agents/research_completion.py#L72) | 72 | `"    \"\"\"Compute phase states and final counters without claiming semantic verification.\"\"\""` | — |
| [SRC-1E32639872-L000073](../../agents/research_completion.py#L73) | 73 | `"    result = _dict(result)"` | — |
| [SRC-1E32639872-L000074](../../agents/research_completion.py#L74) | 74 | `"    report = _dict(result.get(\"search_report\"))"` | — |
| [SRC-1E32639872-L000075](../../agents/research_completion.py#L75) | 75 | `"    raw_sources = _list(result.get(\"sources\"))"` | — |
| [SRC-1E32639872-L000076](../../agents/research_completion.py#L76) | 76 | `"    sources = [item for item in raw_sources if isinstance(item, dict)]"` | — |
| [SRC-1E32639872-L000077](../../agents/research_completion.py#L77) | 77 | `"    kind = str(result.get(\"kind\") or \"\")"` | — |
| [SRC-1E32639872-L000078](../../agents/research_completion.py#L78) | 78 | `"    if kind not in _RESEARCH_KINDS and not report:"` | — |
| [SRC-1E32639872-L000079](../../agents/research_completion.py#L79) | 79 | `"        return {"` | — |
| [SRC-1E32639872-L000080](../../agents/research_completion.py#L80) | 80 | `"            \"status\": \"not_applicable\" if kind in {"` | — |
| [SRC-1E32639872-L000081](../../agents/research_completion.py#L81) | 81 | `"                \"capability_answer\", \"local_conversation\", \"clarification\""` | — |
| [SRC-1E32639872-L000082](../../agents/research_completion.py#L82) | 82 | `"            } else \"not_run\","` | — |
| [SRC-1E32639872-L000083](../../agents/research_completion.py#L83) | 83 | `"            \"semantic_verification\": \"not_performed\","` | — |
| [SRC-1E32639872-L000084](../../agents/research_completion.py#L84) | 84 | `"        }"` | — |
| [SRC-1E32639872-L000085](../../agents/research_completion.py#L85) | 85 | `""` | — |
| [SRC-1E32639872-L000086](../../agents/research_completion.py#L86) | 86 | `"    budget = _dict(result.get(\"request_budget\") or report.get(\"request_budget\"))"` | — |
| [SRC-1E32639872-L000087](../../agents/research_completion.py#L87) | 87 | `"    exhausted = bool(budget.get(\"budget_exhausted\")) or bool("` | — |
| [SRC-1E32639872-L000088](../../agents/research_completion.py#L88) | 88 | `"        budget.get(\"deadline_exceeded\")"` | — |
| [SRC-1E32639872-L000089](../../agents/research_completion.py#L89) | 89 | `"    )"` | — |
| [SRC-1E32639872-L000090](../../agents/research_completion.py#L90) | 90 | `"    guardrails = _dict(report.get(\"source_guardrails\"))"` | — |
| [SRC-1E32639872-L000091](../../agents/research_completion.py#L91) | 91 | `"    final_guards = _dict(guardrails.get(\"final\") or guardrails.get(\"initial\"))"` | — |
| [SRC-1E32639872-L000092](../../agents/research_completion.py#L92) | 92 | `"    rejection_counts = _dict(final_guards.get(\"rejection_counts\"))"` | — |
| [SRC-1E32639872-L000093](../../agents/research_completion.py#L93) | 93 | `"    rejected = sum("` | — |
| [SRC-1E32639872-L000094](../../agents/research_completion.py#L94) | 94 | `"        count for count in (_int(value) for value in rejection_counts.values())"` | — |
| [SRC-1E32639872-L000095](../../agents/research_completion.py#L95) | 95 | `"        if count is not None"` | — |
| [SRC-1E32639872-L000096](../../agents/research_completion.py#L96) | 96 | `"    )"` | — |
| [SRC-1E32639872-L000097](../../agents/research_completion.py#L97) | 97 | `"    attempted_value = result.get(\"search_attempted\")"` | — |
| [SRC-1E32639872-L000098](../../agents/research_completion.py#L98) | 98 | `"    if attempted_value is None:"` | — |
| [SRC-1E32639872-L000099](../../agents/research_completion.py#L99) | 99 | `"        attempted_value = report.get(\"search_attempted\")"` | — |
| [SRC-1E32639872-L000100](../../agents/research_completion.py#L100) | 100 | `"    attempted = attempted_value if isinstance(attempted_value, bool) else None"` | — |
| [SRC-1E32639872-L000101](../../agents/research_completion.py#L101) | 101 | `""` | — |
| [SRC-1E32639872-L000102](../../agents/research_completion.py#L102) | 102 | `"    fetched = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1E32639872-L000103](../../agents/research_completion.py#L103) | 103 | `"    read = sum(_readable(source) for source in sources)"` | — |
| [SRC-1E32639872-L000104](../../agents/research_completion.py#L104) | 104 | `"    snippet_only = sum("` | — |
| [SRC-1E32639872-L000105](../../agents/research_completion.py#L105) | 105 | `"        bool(str(source.get(\"snippet\") or \"\").strip()) and not _readable(source)"` | — |
| [SRC-1E32639872-L000106](../../agents/research_completion.py#L106) | 106 | `"        for source in sources"` | — |
| [SRC-1E32639872-L000107](../../agents/research_completion.py#L107) | 107 | `"    )"` | — |
| [SRC-1E32639872-L000108](../../agents/research_completion.py#L108) | 108 | `"    unflagged_text = sum("` | — |
| [SRC-1E32639872-L000109](../../agents/research_completion.py#L109) | 109 | `"        ("` | — |
| [SRC-1E32639872-L000110](../../agents/research_completion.py#L110) | 110 | `"            bool(str(source.get(\"page_text\") or \"\").strip())"` | — |
| [SRC-1E32639872-L000111](../../agents/research_completion.py#L111) | 111 | `"            and not bool(source.get(\"page_fetched\"))"` | — |
| [SRC-1E32639872-L000112](../../agents/research_completion.py#L112) | 112 | `"        )"` | — |
| [SRC-1E32639872-L000113](../../agents/research_completion.py#L113) | 113 | `"        or source.get(\"page_text_present_without_fetch_flag\") is True"` | — |
| [SRC-1E32639872-L000114](../../agents/research_completion.py#L114) | 114 | `"        for source in sources"` | — |
| [SRC-1E32639872-L000115](../../agents/research_completion.py#L115) | 115 | `"    )"` | — |
| [SRC-1E32639872-L000116](../../agents/research_completion.py#L116) | 116 | `"    url_keys = [_url_key(source.get(\"url\")) for source in sources]"` | — |
| [SRC-1E32639872-L000117](../../agents/research_completion.py#L117) | 117 | `"    url_keys = [key for key in url_keys if key]"` | — |
| [SRC-1E32639872-L000118](../../agents/research_completion.py#L118) | 118 | `"    unique_urls = set(url_keys)"` | — |
| [SRC-1E32639872-L000119](../../agents/research_completion.py#L119) | 119 | `"    domains = set()"` | — |
| [SRC-1E32639872-L000120](../../agents/research_completion.py#L120) | 120 | `"    for source in sources:"` | — |
| [SRC-1E32639872-L000121](../../agents/research_completion.py#L121) | 121 | `"        key = _url_key(source.get(\"url\"))"` | — |
| [SRC-1E32639872-L000122](../../agents/research_completion.py#L122) | 122 | `"        if not key:"` | — |
| [SRC-1E32639872-L000123](../../agents/research_completion.py#L123) | 123 | `"            continue"` | — |
| [SRC-1E32639872-L000124](../../agents/research_completion.py#L124) | 124 | `"        host = source.get(\"domain\") or urlsplit(key).hostname or \"\""` | — |
| [SRC-1E32639872-L000125](../../agents/research_completion.py#L125) | 125 | `"        domains.add(registrable_domain(str(host)))"` | — |
| [SRC-1E32639872-L000126](../../agents/research_completion.py#L126) | 126 | `"    domains.discard(\"\")"` | — |
| [SRC-1E32639872-L000127](../../agents/research_completion.py#L127) | 127 | `""` | — |
| [SRC-1E32639872-L000128](../../agents/research_completion.py#L128) | 128 | `"    query_rows = _list(report.get(\"query_results\"))"` | — |
| [SRC-1E32639872-L000129](../../agents/research_completion.py#L129) | 129 | `"    query_total = None"` | — |
| [SRC-1E32639872-L000130](../../agents/research_completion.py#L130) | 130 | `"    if query_rows and all("` | — |
| [SRC-1E32639872-L000131](../../agents/research_completion.py#L131) | 131 | `"        isinstance(row, dict) and _int(row.get(\"results\")) is not None"` | — |
| [SRC-1E32639872-L000132](../../agents/research_completion.py#L132) | 132 | `"        for row in query_rows"` | — |
| [SRC-1E32639872-L000133](../../agents/research_completion.py#L133) | 133 | `"    ):"` | — |
| [SRC-1E32639872-L000134](../../agents/research_completion.py#L134) | 134 | `"        query_total = sum(_int(row.get(\"results\")) or 0 for row in query_rows)"` | — |
| [SRC-1E32639872-L000135](../../agents/research_completion.py#L135) | 135 | `"    zero_results = bool(query_rows) and all("` | — |
| [SRC-1E32639872-L000136](../../agents/research_completion.py#L136) | 136 | `"        isinstance(row, dict) and _int(row.get(\"results\")) == 0"` | — |
| [SRC-1E32639872-L000137](../../agents/research_completion.py#L137) | 137 | `"        for row in query_rows"` | — |
| [SRC-1E32639872-L000138](../../agents/research_completion.py#L138) | 138 | `"    )"` | — |
| [SRC-1E32639872-L000139](../../agents/research_completion.py#L139) | 139 | `""` | — |
| [SRC-1E32639872-L000140](../../agents/research_completion.py#L140) | 140 | `"    connector_counts: dict[str, int] = {}"` | — |
| [SRC-1E32639872-L000141](../../agents/research_completion.py#L141) | 141 | `"    for item in _list(report.get(\"provider_diagnostics\")):"` | — |
| [SRC-1E32639872-L000142](../../agents/research_completion.py#L142) | 142 | `"        if not isinstance(item, dict):"` | — |
| [SRC-1E32639872-L000143](../../agents/research_completion.py#L143) | 143 | `"            continue"` | — |
| [SRC-1E32639872-L000144](../../agents/research_completion.py#L144) | 144 | `"        status_value = str(item.get(\"status\") or \"unknown\").strip().lower()"` | — |
| [SRC-1E32639872-L000145](../../agents/research_completion.py#L145) | 145 | `"        connector_counts[status_value] = connector_counts.get(status_value, 0) + 1"` | — |
| [SRC-1E32639872-L000146](../../agents/research_completion.py#L146) | 146 | `"    connector_ok = sum("` | — |
| [SRC-1E32639872-L000147](../../agents/research_completion.py#L147) | 147 | `"        count for status_value, count in connector_counts.items()"` | — |
| [SRC-1E32639872-L000148](../../agents/research_completion.py#L148) | 148 | `"        if status_value in _CONNECTOR_OK"` | — |
| [SRC-1E32639872-L000149](../../agents/research_completion.py#L149) | 149 | `"    )"` | — |
| [SRC-1E32639872-L000150](../../agents/research_completion.py#L150) | 150 | `"    connector_errors = sum("` | — |
| [SRC-1E32639872-L000151](../../agents/research_completion.py#L151) | 151 | `"        count for status_value, count in connector_counts.items()"` | — |
| [SRC-1E32639872-L000152](../../agents/research_completion.py#L152) | 152 | `"        if status_value in _CONNECTOR_ERRORS"` | — |
| [SRC-1E32639872-L000153](../../agents/research_completion.py#L153) | 153 | `"    )"` | — |
| [SRC-1E32639872-L000154](../../agents/research_completion.py#L154) | 154 | `""` | — |
| [SRC-1E32639872-L000155](../../agents/research_completion.py#L155) | 155 | `"    reported_sources = _int(report.get(\"unique_sources\"))"` | — |
| [SRC-1E32639872-L000156](../../agents/research_completion.py#L156) | 156 | `"    reported_fetched = _int(report.get(\"pages_fetched\"))"` | — |
| [SRC-1E32639872-L000157](../../agents/research_completion.py#L157) | 157 | `"    counter_issues = []"` | — |
| [SRC-1E32639872-L000158](../../agents/research_completion.py#L158) | 158 | `"    if reported_sources is not None and reported_sources != len(sources):"` | — |
| [SRC-1E32639872-L000159](../../agents/research_completion.py#L159) | 159 | `"        counter_issues.append(\"reported_unique_sources_differs_from_final_source_list\")"` | — |
| [SRC-1E32639872-L000160](../../agents/research_completion.py#L160) | 160 | `"    if reported_fetched is not None and reported_fetched != fetched:"` | — |
| [SRC-1E32639872-L000161](../../agents/research_completion.py#L161) | 161 | `"        counter_issues.append(\"reported_pages_fetched_differs_from_final_source_list\")"` | — |
| [SRC-1E32639872-L000162](../../agents/research_completion.py#L162) | 162 | `""` | — |
| [SRC-1E32639872-L000163](../../agents/research_completion.py#L163) | 163 | `"    model_used = result.get(\"used_language_model\") is True"` | — |
| [SRC-1E32639872-L000164](../../agents/research_completion.py#L164) | 164 | `"    final_status = str(result.get(\"final_answer_status\") or \"\")"` | — |
| [SRC-1E32639872-L000165](../../agents/research_completion.py#L165) | 165 | `"    integrity = _dict(result.get(\"answer_integrity\"))"` | — |
| [SRC-1E32639872-L000166](../../agents/research_completion.py#L166) | 166 | `"    gap_count = sum("` | — |
| [SRC-1E32639872-L000167](../../agents/research_completion.py#L167) | 167 | `"        _int(integrity.get(key)) or 0"` | — |
| [SRC-1E32639872-L000168](../../agents/research_completion.py#L168) | 168 | `"        for key in (\"potentially_missing_target_count\", \"source_evidence_gap_count\")"` | — |
| [SRC-1E32639872-L000169](../../agents/research_completion.py#L169) | 169 | `"    )"` | — |
| [SRC-1E32639872-L000170](../../agents/research_completion.py#L170) | 170 | `"    fulfillment = str("` | — |
| [SRC-1E32639872-L000171](../../agents/research_completion.py#L171) | 171 | `"        result.get(\"task_fulfillment_status\") or report.get(\"task_fulfillment_status\") or \"\""` | — |
| [SRC-1E32639872-L000172](../../agents/research_completion.py#L172) | 172 | `"    )"` | — |
| [SRC-1E32639872-L000173](../../agents/research_completion.py#L173) | 173 | `"    citations = _dict(result.get(\"citation_validation\") or result.get(\"citation_check\"))"` | — |
| [SRC-1E32639872-L000174](../../agents/research_completion.py#L174) | 174 | `"    citation_count = _int(citations.get(\"valid_citation_count\")) or 0"` | — |
| [SRC-1E32639872-L000175](../../agents/research_completion.py#L175) | 175 | `"    generation_failed = any("` | — |
| [SRC-1E32639872-L000176](../../agents/research_completion.py#L176) | 176 | `"        token in final_status for token in (\"failed\", \"unavailable\", \"budget_exhausted\")"` | — |
| [SRC-1E32639872-L000177](../../agents/research_completion.py#L177) | 177 | `"    )"` | — |
| [SRC-1E32639872-L000178](../../agents/research_completion.py#L178) | 178 | `""` | — |
| [SRC-1E32639872-L000179](../../agents/research_completion.py#L179) | 179 | `"    if exhausted:"` | — |
| [SRC-1E32639872-L000180](../../agents/research_completion.py#L180) | 180 | `"        status = \"execution_stopped_budget\""` | — |
| [SRC-1E32639872-L000181](../../agents/research_completion.py#L181) | 181 | `"    elif not sources:"` | — |
| [SRC-1E32639872-L000182](../../agents/research_completion.py#L182) | 182 | `"        if rejected:"` | — |
| [SRC-1E32639872-L000183](../../agents/research_completion.py#L183) | 183 | `"            status = \"no_eligible_sources_after_filtering\""` | — |
| [SRC-1E32639872-L000184](../../agents/research_completion.py#L184) | 184 | `"        elif str(report.get(\"search_outcome\") or \"\") in _RESEARCH_ERRORS or ("` | — |
| [SRC-1E32639872-L000185](../../agents/research_completion.py#L185) | 185 | `"            connector_errors and not connector_ok"` | — |
| [SRC-1E32639872-L000186](../../agents/research_completion.py#L186) | 186 | `"        ):"` | — |
| [SRC-1E32639872-L000187](../../agents/research_completion.py#L187) | 187 | `"            status = \"search_failed_or_incomplete\""` | — |
| [SRC-1E32639872-L000188](../../agents/research_completion.py#L188) | 188 | `"        elif zero_results:"` | — |
| [SRC-1E32639872-L000189](../../agents/research_completion.py#L189) | 189 | `"            status = \"no_results_returned\""` | — |
| [SRC-1E32639872-L000190](../../agents/research_completion.py#L190) | 190 | `"        elif attempted is False:"` | — |
| [SRC-1E32639872-L000191](../../agents/research_completion.py#L191) | 191 | `"            status = \"search_not_attempted\""` | — |
| [SRC-1E32639872-L000192](../../agents/research_completion.py#L192) | 192 | `"        else:"` | — |
| [SRC-1E32639872-L000193](../../agents/research_completion.py#L193) | 193 | `"            status = \"insufficient_evidence\""` | — |
| [SRC-1E32639872-L000194](../../agents/research_completion.py#L194) | 194 | `"    elif not model_used:"` | — |
| [SRC-1E32639872-L000195](../../agents/research_completion.py#L195) | 195 | `"        status = ("` | — |
| [SRC-1E32639872-L000196](../../agents/research_completion.py#L196) | 196 | `"            \"source_snippets_only_generation_not_completed\""` | — |
| [SRC-1E32639872-L000197](../../agents/research_completion.py#L197) | 197 | `"            if read == 0 else \"evidence_collected_generation_not_completed\""` | — |
| [SRC-1E32639872-L000198](../../agents/research_completion.py#L198) | 198 | `"        )"` | — |
| [SRC-1E32639872-L000199](../../agents/research_completion.py#L199) | 199 | `"    elif generation_failed:"` | — |
| [SRC-1E32639872-L000200](../../agents/research_completion.py#L200) | 200 | `"        status = \"answer_generation_or_review_failed\""` | — |
| [SRC-1E32639872-L000201](../../agents/research_completion.py#L201) | 201 | `"    elif gap_count or fulfillment in {"` | — |
| [SRC-1E32639872-L000202](../../agents/research_completion.py#L202) | 202 | `"        \"possible_gap_detected\", \"source_evidence_gap_unresolved\","` | — |
| [SRC-1E32639872-L000203](../../agents/research_completion.py#L203) | 203 | `"        \"not_assessed_insufficient_evidence\","` | — |
| [SRC-1E32639872-L000204](../../agents/research_completion.py#L204) | 204 | `"    }:"` | — |
| [SRC-1E32639872-L000205](../../agents/research_completion.py#L205) | 205 | `"        status = \"partial_answer_evidence_gaps_detected\""` | — |
| [SRC-1E32639872-L000206](../../agents/research_completion.py#L206) | 206 | `"    elif citation_count:"` | — |
| [SRC-1E32639872-L000207](../../agents/research_completion.py#L207) | 207 | `"        status = \"answer_generated_citations_range_checked_semantic_support_unverified\""` | — |
| [SRC-1E32639872-L000208](../../agents/research_completion.py#L208) | 208 | `"    else:"` | — |
| [SRC-1E32639872-L000209](../../agents/research_completion.py#L209) | 209 | `"        status = \"answer_generated_without_valid_citation_markers\""` | — |
| [SRC-1E32639872-L000210](../../agents/research_completion.py#L210) | 210 | `""` | — |
| [SRC-1E32639872-L000211](../../agents/research_completion.py#L211) | 211 | `"    if attempted is False:"` | — |
| [SRC-1E32639872-L000212](../../agents/research_completion.py#L212) | 212 | `"        search_phase = \"not_attempted\""` | — |
| [SRC-1E32639872-L000213](../../agents/research_completion.py#L213) | 213 | `"    elif attempted is None:"` | — |
| [SRC-1E32639872-L000214](../../agents/research_completion.py#L214) | 214 | `"        search_phase = \"unknown\""` | — |
| [SRC-1E32639872-L000215](../../agents/research_completion.py#L215) | 215 | `"    elif connector_errors and not connector_ok and not sources:"` | — |
| [SRC-1E32639872-L000216](../../agents/research_completion.py#L216) | 216 | `"        search_phase = \"failed_or_incomplete\""` | — |
| [SRC-1E32639872-L000217](../../agents/research_completion.py#L217) | 217 | `"    elif sources:"` | — |
| [SRC-1E32639872-L000218](../../agents/research_completion.py#L218) | 218 | `"        search_phase = \"results_received\""` | — |
| [SRC-1E32639872-L000219](../../agents/research_completion.py#L219) | 219 | `"    elif zero_results:"` | — |
| [SRC-1E32639872-L000220](../../agents/research_completion.py#L220) | 220 | `"        search_phase = \"completed_no_results\""` | — |
| [SRC-1E32639872-L000221](../../agents/research_completion.py#L221) | 221 | `"    else:"` | — |
| [SRC-1E32639872-L000222](../../agents/research_completion.py#L222) | 222 | `"        search_phase = \"attempted_no_usable_sources\""` | — |
| [SRC-1E32639872-L000223](../../agents/research_completion.py#L223) | 223 | `""` | — |
| [SRC-1E32639872-L000224](../../agents/research_completion.py#L224) | 224 | `"    if not sources:"` | — |
| [SRC-1E32639872-L000225](../../agents/research_completion.py#L225) | 225 | `"        read_phase = \"not_applicable_no_eligible_sources\""` | — |
| [SRC-1E32639872-L000226](../../agents/research_completion.py#L226) | 226 | `"    elif read == len(sources):"` | — |
| [SRC-1E32639872-L000227](../../agents/research_completion.py#L227) | 227 | `"        read_phase = \"all_final_sources_read\""` | — |
| [SRC-1E32639872-L000228](../../agents/research_completion.py#L228) | 228 | `"    elif read:"` | — |
| [SRC-1E32639872-L000229](../../agents/research_completion.py#L229) | 229 | `"        read_phase = \"some_final_sources_read\""` | — |
| [SRC-1E32639872-L000230](../../agents/research_completion.py#L230) | 230 | `"    else:"` | — |
| [SRC-1E32639872-L000231](../../agents/research_completion.py#L231) | 231 | `"        read_phase = \"no_final_source_page_read\""` | — |
| [SRC-1E32639872-L000232](../../agents/research_completion.py#L232) | 232 | `""` | — |
| [SRC-1E32639872-L000233](../../agents/research_completion.py#L233) | 233 | `"    if kind == \"insufficient_evidence\" or not sources:"` | — |
| [SRC-1E32639872-L000234](../../agents/research_completion.py#L234) | 234 | `"        generation_phase = \"not_attempted_or_withheld\""` | — |
| [SRC-1E32639872-L000235](../../agents/research_completion.py#L235) | 235 | `"    elif model_used and not generation_failed:"` | — |
| [SRC-1E32639872-L000236](../../agents/research_completion.py#L236) | 236 | `"        generation_phase = \"answer_generated\""` | — |
| [SRC-1E32639872-L000237](../../agents/research_completion.py#L237) | 237 | `"    elif model_used:"` | — |
| [SRC-1E32639872-L000238](../../agents/research_completion.py#L238) | 238 | `"        generation_phase = \"failed_or_unavailable\""` | — |
| [SRC-1E32639872-L000239](../../agents/research_completion.py#L239) | 239 | `"    else:"` | — |
| [SRC-1E32639872-L000240](../../agents/research_completion.py#L240) | 240 | `"        generation_phase = \"not_completed\""` | — |
| [SRC-1E32639872-L000241](../../agents/research_completion.py#L241) | 241 | `""` | — |
| [SRC-1E32639872-L000242](../../agents/research_completion.py#L242) | 242 | `"    return {"` | — |
| [SRC-1E32639872-L000243](../../agents/research_completion.py#L243) | 243 | `"        \"status\": status,"` | — |
| [SRC-1E32639872-L000244](../../agents/research_completion.py#L244) | 244 | `"        \"status_semantics\": \"pipeline_state_not_probability_of_factual_correctness\","` | — |
| [SRC-1E32639872-L000245](../../agents/research_completion.py#L245) | 245 | `"        \"phases\": {"` | — |
| [SRC-1E32639872-L000246](../../agents/research_completion.py#L246) | 246 | `"            \"planning\": \"completed\" if isinstance(result.get(\"research_plan\"), dict) else \"unknown\","` | — |
| [SRC-1E32639872-L000247](../../agents/research_completion.py#L247) | 247 | `"            \"search\": search_phase,"` | — |
| [SRC-1E32639872-L000248](../../agents/research_completion.py#L248) | 248 | `"            \"source_filtering\": ("` | — |
| [SRC-1E32639872-L000249](../../agents/research_completion.py#L249) | 249 | `"                \"sources_retained\" if sources else"` | — |
| [SRC-1E32639872-L000250](../../agents/research_completion.py#L250) | 250 | `"                \"rejected_all_candidates\" if rejected else \"no_eligible_sources\""` | — |
| [SRC-1E32639872-L000251](../../agents/research_completion.py#L251) | 251 | `"            ),"` | — |
| [SRC-1E32639872-L000252](../../agents/research_completion.py#L252) | 252 | `"            \"page_reading\": read_phase,"` | — |
| [SRC-1E32639872-L000253](../../agents/research_completion.py#L253) | 253 | `"            \"answer_generation\": generation_phase,"` | — |
| [SRC-1E32639872-L000254](../../agents/research_completion.py#L254) | 254 | `"            \"citation_validation\": str(citations.get(\"status\") or \"not_run\"),"` | — |
| [SRC-1E32639872-L000255](../../agents/research_completion.py#L255) | 255 | `"            \"semantic_verification\": \"not_performed\","` | — |
| [SRC-1E32639872-L000256](../../agents/research_completion.py#L256) | 256 | `"        },"` | — |
| [SRC-1E32639872-L000257](../../agents/research_completion.py#L257) | 257 | `"        \"counters\": {"` | — |
| [SRC-1E32639872-L000258](../../agents/research_completion.py#L258) | 258 | `"            \"queries_planned\": _int(report.get(\"queries_planned\")),"` | — |
| [SRC-1E32639872-L000259](../../agents/research_completion.py#L259) | 259 | `"            \"queries_attempted\": _int(report.get(\"queries_attempted\")),"` | — |
| [SRC-1E32639872-L000260](../../agents/research_completion.py#L260) | 260 | `"            \"per_query_result_count_sum\": query_total,"` | — |
| [SRC-1E32639872-L000261](../../agents/research_completion.py#L261) | 261 | `"            \"per_query_result_count_sum_semantics\": \"sum_of_reported_per_query_counts_not_deduplicated_sources\","` | — |
| [SRC-1E32639872-L000262](../../agents/research_completion.py#L262) | 262 | `"            \"query_result_row_count\": len(query_rows),"` | — |
| [SRC-1E32639872-L000263](../../agents/research_completion.py#L263) | 263 | `"            \"query_result_rows_with_counts\": sum("` | — |
| [SRC-1E32639872-L000264](../../agents/research_completion.py#L264) | 264 | `"                isinstance(row, dict) and _int(row.get(\"results\")) is not None"` | — |
| [SRC-1E32639872-L000265](../../agents/research_completion.py#L265) | 265 | `"                for row in query_rows"` | — |
| [SRC-1E32639872-L000266](../../agents/research_completion.py#L266) | 266 | `"            ),"` | — |
| [SRC-1E32639872-L000267](../../agents/research_completion.py#L267) | 267 | `"            \"final_source_list_count\": len(sources),"` | — |
| [SRC-1E32639872-L000268](../../agents/research_completion.py#L268) | 268 | `"            \"unique_normalized_url_count\": len(unique_urls),"` | — |
| [SRC-1E32639872-L000269](../../agents/research_completion.py#L269) | 269 | `"            \"duplicate_normalized_url_count\": max(0, len(url_keys) - len(unique_urls)),"` | — |
| [SRC-1E32639872-L000270](../../agents/research_completion.py#L270) | 270 | `"            \"distinct_registrable_domain_count\": len(domains),"` | — |
| [SRC-1E32639872-L000271](../../agents/research_completion.py#L271) | 271 | `"            \"pages_fetched_flag_count\": fetched,"` | — |
| [SRC-1E32639872-L000272](../../agents/research_completion.py#L272) | 272 | `"            \"pages_read_with_text_count\": read,"` | — |
| [SRC-1E32639872-L000273](../../agents/research_completion.py#L273) | 273 | `"            \"snippet_only_source_count\": snippet_only,"` | — |
| [SRC-1E32639872-L000274](../../agents/research_completion.py#L274) | 274 | `"            \"page_text_without_fetched_flag_count\": unflagged_text,"` | — |
| [SRC-1E32639872-L000275](../../agents/research_completion.py#L275) | 275 | `"            \"connector_status_counts\": connector_counts,"` | — |
| [SRC-1E32639872-L000276](../../agents/research_completion.py#L276) | 276 | `"            \"connector_failure_count\": connector_errors,"` | — |
| [SRC-1E32639872-L000277](../../agents/research_completion.py#L277) | 277 | `"            \"connector_success_count\": connector_ok,"` | — |
| [SRC-1E32639872-L000278](../../agents/research_completion.py#L278) | 278 | `"            \"guardrail_rejected_candidate_count\": rejected,"` | — |
| [SRC-1E32639872-L000279](../../agents/research_completion.py#L279) | 279 | `"        },"` | — |
| [SRC-1E32639872-L000280](../../agents/research_completion.py#L280) | 280 | `"        \"counter_consistency\": {"` | — |
| [SRC-1E32639872-L000281](../../agents/research_completion.py#L281) | 281 | `"            \"status\": \"mismatch_detected\" if counter_issues else ("` | — |
| [SRC-1E32639872-L000282](../../agents/research_completion.py#L282) | 282 | `"                \"matched\" if reported_sources is not None or reported_fetched is not None"` | — |
| [SRC-1E32639872-L000283](../../agents/research_completion.py#L283) | 283 | `"                else \"not_computable\""` | — |
| [SRC-1E32639872-L000284](../../agents/research_completion.py#L284) | 284 | `"            ),"` | — |
| [SRC-1E32639872-L000285](../../agents/research_completion.py#L285) | 285 | `"            \"reported_unique_sources\": reported_sources,"` | — |
| [SRC-1E32639872-L000286](../../agents/research_completion.py#L286) | 286 | `"            \"recomputed_final_source_count\": len(sources),"` | — |
| [SRC-1E32639872-L000287](../../agents/research_completion.py#L287) | 287 | `"            \"reported_pages_fetched\": reported_fetched,"` | — |
| [SRC-1E32639872-L000288](../../agents/research_completion.py#L288) | 288 | `"            \"recomputed_pages_fetched_flag_count\": fetched,"` | — |
| [SRC-1E32639872-L000289](../../agents/research_completion.py#L289) | 289 | `"            \"issues\": counter_issues,"` | — |
| [SRC-1E32639872-L000290](../../agents/research_completion.py#L290) | 290 | `"        },"` | — |
| [SRC-1E32639872-L000291](../../agents/research_completion.py#L291) | 291 | `"        \"semantic_verification\": \"not_performed\","` | — |
| [SRC-1E32639872-L000292](../../agents/research_completion.py#L292) | 292 | `"        \"warning\": ("` | — |
| [SRC-1E32639872-L000293](../../agents/research_completion.py#L293) | 293 | `"            \"Readable pages and valid citation indexes do not prove semantic support \""` | — |
| [SRC-1E32639872-L000294](../../agents/research_completion.py#L294) | 294 | `"            \"for each claim in the answer.\""` | — |
| [SRC-1E32639872-L000295](../../agents/research_completion.py#L295) | 295 | `"        ),"` | — |
| [SRC-1E32639872-L000296](../../agents/research_completion.py#L296) | 296 | `"    }"` | — |
## الوكيل والمنطق

### FILE-3AA6165B18 — [agents/research_guardrails.py](../../agents/research_guardrails.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-3AA6165B18-L000001](../../agents/research_guardrails.py#L1) | 1 | `"\"\"\"Task-specific guardrails for search evidence."` | — |
| [SRC-3AA6165B18-L000002](../../agents/research_guardrails.py#L2) | 2 | `""` | — |
| [SRC-3AA6165B18-L000003](../../agents/research_guardrails.py#L3) | 3 | `"These checks are conservative retrieval filters, not proof of factual correctness."` | — |
| [SRC-3AA6165B18-L000004](../../agents/research_guardrails.py#L4) | 4 | `"\"\"\""` | — |
| [SRC-3AA6165B18-L000005](../../agents/research_guardrails.py#L5) | 5 | `"from __future__ import annotations"` | — |
| [SRC-3AA6165B18-L000006](../../agents/research_guardrails.py#L6) | 6 | `""` | — |
| [SRC-3AA6165B18-L000007](../../agents/research_guardrails.py#L7) | 7 | `"import re"` | — |
| [SRC-3AA6165B18-L000008](../../agents/research_guardrails.py#L8) | 8 | `"from datetime import UTC, datetime, timedelta"` | — |
| [SRC-3AA6165B18-L000009](../../agents/research_guardrails.py#L9) | 9 | `"from typing import Any"` | — |
| [SRC-3AA6165B18-L000010](../../agents/research_guardrails.py#L10) | 10 | `"from urllib.parse import urlsplit"` | — |
| [SRC-3AA6165B18-L000011](../../agents/research_guardrails.py#L11) | 11 | `""` | — |
| [SRC-3AA6165B18-L000012](../../agents/research_guardrails.py#L12) | 12 | `"from agents.research import ("` | — |
| [SRC-3AA6165B18-L000013](../../agents/research_guardrails.py#L13) | 13 | `"    SOCIAL_DOMAINS,"` | — |
| [SRC-3AA6165B18-L000014](../../agents/research_guardrails.py#L14) | 14 | `"    _parse_publication_date,"` | — |
