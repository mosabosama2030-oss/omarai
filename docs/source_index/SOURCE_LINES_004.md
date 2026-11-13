# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **004**
- سجلات الأسطر: **800**
- النطاق: SRC-5587371288-L000404 إلى SRC-C9CF9B54F8-L000599
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-5587371288 — [agents/intent_router.py](../../agents/intent_router.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-5587371288-L000404](../../agents/intent_router.py#L404) | 404 | `"        \"source-backed\", \"cite your sources\","` | — |
| [SRC-5587371288-L000405](../../agents/intent_router.py#L405) | 405 | `"    )"` | — |
| [SRC-5587371288-L000406](../../agents/intent_router.py#L406) | 406 | `"    return any(_normalize(marker) in normalized for marker in markers)"` | — |
| [SRC-5587371288-L000407](../../agents/intent_router.py#L407) | 407 | `""` | — |
| [SRC-5587371288-L000408](../../agents/intent_router.py#L408) | 408 | `""` | — |
| [SRC-5587371288-L000409](../../agents/intent_router.py#L409) | 409 | `"def _is_deep(question: str) -> bool:"` | — |
| [SRC-5587371288-L000410](../../agents/intent_router.py#L410) | 410 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000411](../../agents/intent_router.py#L411) | 411 | `"    if any(_normalize(term) in normalized for term in _DEEP_TERMS):"` | — |
| [SRC-5587371288-L000412](../../agents/intent_router.py#L412) | 412 | `"        return True"` | — |
| [SRC-5587371288-L000413](../../agents/intent_router.py#L413) | 413 | `"    # Explicit multi-dimension comparisons need evidence from more than one angle."` | — |
| [SRC-5587371288-L000414](../../agents/intent_router.py#L414) | 414 | `"    dimensions = ("` | — |
| [SRC-5587371288-L000415](../../agents/intent_router.py#L415) | 415 | `"        \"السعر\", \"سعر\", \"بطاريه\", \"كاميرا\", \"اداء\", \"امان\", \"تكلفه\","` | — |
| [SRC-5587371288-L000416](../../agents/intent_router.py#L416) | 416 | `"        \"الصيانه\", \"الجوده\", \"المميزات\", \"العيوب\", \"الاراء\", \"المراجعات\","` | — |
| [SRC-5587371288-L000417](../../agents/intent_router.py#L417) | 417 | `"        \"price\", \"battery\", \"camera\", \"performance\", \"safety\", \"cost\","` | — |
| [SRC-5587371288-L000418](../../agents/intent_router.py#L418) | 418 | `"        \"maintenance\", \"quality\", \"features\", \"drawbacks\", \"reviews\","` | — |
| [SRC-5587371288-L000419](../../agents/intent_router.py#L419) | 419 | `"    )"` | — |
| [SRC-5587371288-L000420](../../agents/intent_router.py#L420) | 420 | `"    matched_dimensions = sum(1 for item in dimensions if _normalize(item) in normalized)"` | — |
| [SRC-5587371288-L000421](../../agents/intent_router.py#L421) | 421 | `"    return matched_dimensions >= 2 and any("` | — |
| [SRC-5587371288-L000422](../../agents/intent_router.py#L422) | 422 | `"        marker in normalized for marker in _MULTIPART_MARKERS"` | — |
| [SRC-5587371288-L000423](../../agents/intent_router.py#L423) | 423 | `"    )"` | — |
| [SRC-5587371288-L000424](../../agents/intent_router.py#L424) | 424 | `""` | — |
| [SRC-5587371288-L000425](../../agents/intent_router.py#L425) | 425 | `""` | — |
| [SRC-5587371288-L000426](../../agents/intent_router.py#L426) | 426 | `"def _is_page_summarization_request(question: str) -> bool:"` | — |
| [SRC-5587371288-L000427](../../agents/intent_router.py#L427) | 427 | `"    \"\"\"Recognize a request to summarize a specific web page or link.\"\"\""` | — |
| [SRC-5587371288-L000428](../../agents/intent_router.py#L428) | 428 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000429](../../agents/intent_router.py#L429) | 429 | `"    terms = (\"لخص\", \"تلخيص\", \"ملخص\", \"summarize\", \"summarise\", \"summary\")"` | — |
| [SRC-5587371288-L000430](../../agents/intent_router.py#L430) | 430 | `"    page_references = ("` | — |
| [SRC-5587371288-L000431](../../agents/intent_router.py#L431) | 431 | `"        \"صفحه\", \"الصفحه\", \"مقال\", \"المقال\", \"رابط\", \"لينك\", \"url\","` | — |
| [SRC-5587371288-L000432](../../agents/intent_router.py#L432) | 432 | `"        \"link\", \"article\", \"page\", \"webpage\", \"web page\", \"website\","` | — |
| [SRC-5587371288-L000433](../../agents/intent_router.py#L433) | 433 | `"    )"` | — |
| [SRC-5587371288-L000434](../../agents/intent_router.py#L434) | 434 | `"    return ("` | — |
| [SRC-5587371288-L000435](../../agents/intent_router.py#L435) | 435 | `"        any(_normalize(term) in normalized for term in terms)"` | — |
| [SRC-5587371288-L000436](../../agents/intent_router.py#L436) | 436 | `"        and ("` | — |
| [SRC-5587371288-L000437](../../agents/intent_router.py#L437) | 437 | `"            bool(re.search(r\"https?://\", question, flags=re.IGNORECASE))"` | — |
| [SRC-5587371288-L000438](../../agents/intent_router.py#L438) | 438 | `"            or any(_normalize(term) in normalized for term in page_references)"` | — |
| [SRC-5587371288-L000439](../../agents/intent_router.py#L439) | 439 | `"        )"` | — |
| [SRC-5587371288-L000440](../../agents/intent_router.py#L440) | 440 | `"    )"` | — |
| [SRC-5587371288-L000441](../../agents/intent_router.py#L441) | 441 | `""` | — |
| [SRC-5587371288-L000442](../../agents/intent_router.py#L442) | 442 | `""` | — |
| [SRC-5587371288-L000443](../../agents/intent_router.py#L443) | 443 | `"def _has_inline_summary_text(question: str) -> bool:"` | — |
| [SRC-5587371288-L000444](../../agents/intent_router.py#L444) | 444 | `"    \"\"\"Detect text explicitly pasted after a summary instruction, not a web page URL.\"\"\""` | — |
| [SRC-5587371288-L000445](../../agents/intent_router.py#L445) | 445 | `"    if re.search(r\"https?://\", question, flags=re.IGNORECASE):"` | — |
| [SRC-5587371288-L000446](../../agents/intent_router.py#L446) | 446 | `"        return False"` | — |
| [SRC-5587371288-L000447](../../agents/intent_router.py#L447) | 447 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000448](../../agents/intent_router.py#L448) | 448 | `"    markers = ("` | — |
| [SRC-5587371288-L000449](../../agents/intent_router.py#L449) | 449 | `"        \"النص التالي\", \"النص الاتي\", \"النص ده\", \"النص اللي جاي\","` | — |
| [SRC-5587371288-L000450](../../agents/intent_router.py#L450) | 450 | `"        \"this text\", \"following text\", \"the following text\", \"text below\","` | — |
| [SRC-5587371288-L000451](../../agents/intent_router.py#L451) | 451 | `"        \"text to summarize\", \"content below\","` | — |
| [SRC-5587371288-L000452](../../agents/intent_router.py#L452) | 452 | `"    )"` | — |
| [SRC-5587371288-L000453](../../agents/intent_router.py#L453) | 453 | `"    for marker in markers:"` | — |
| [SRC-5587371288-L000454](../../agents/intent_router.py#L454) | 454 | `"        normalized_marker = _normalize(marker)"` | — |
| [SRC-5587371288-L000455](../../agents/intent_router.py#L455) | 455 | `"        if normalized_marker in normalized:"` | — |
| [SRC-5587371288-L000456](../../agents/intent_router.py#L456) | 456 | `"            remainder = normalized.split(normalized_marker, 1)[1].strip()"` | — |
| [SRC-5587371288-L000457](../../agents/intent_router.py#L457) | 457 | `"            if len(remainder) >= 8:"` | — |
| [SRC-5587371288-L000458](../../agents/intent_router.py#L458) | 458 | `"                return True"` | — |
| [SRC-5587371288-L000459](../../agents/intent_router.py#L459) | 459 | `"    # Also allow a concise direct form such as \"لخص: [pasted paragraph]\"."` | — |
| [SRC-5587371288-L000460](../../agents/intent_router.py#L460) | 460 | `"    return bool("` | — |
| [SRC-5587371288-L000461](../../agents/intent_router.py#L461) | 461 | `"        re.search("` | — |
| [SRC-5587371288-L000462](../../agents/intent_router.py#L462) | 462 | `"            r\"^\\s*(?:لخص(?:\\s+لي)?\|تلخيص\|summari[sz]e\|summary)\\s*[:：]\\s*\\S.{12,}$\","` | — |
| [SRC-5587371288-L000463](../../agents/intent_router.py#L463) | 463 | `"            question,"` | — |
| [SRC-5587371288-L000464](../../agents/intent_router.py#L464) | 464 | `"            flags=re.IGNORECASE,"` | — |
| [SRC-5587371288-L000465](../../agents/intent_router.py#L465) | 465 | `"        )"` | — |
| [SRC-5587371288-L000466](../../agents/intent_router.py#L466) | 466 | `"    )"` | — |
| [SRC-5587371288-L000467](../../agents/intent_router.py#L467) | 467 | `""` | — |
| [SRC-5587371288-L000468](../../agents/intent_router.py#L468) | 468 | `""` | — |
| [SRC-5587371288-L000469](../../agents/intent_router.py#L469) | 469 | `"def route_intent("` | — |
| [SRC-5587371288-L000470](../../agents/intent_router.py#L470) | 470 | `"    question: str,"` | — |
| [SRC-5587371288-L000471](../../agents/intent_router.py#L471) | 471 | `"    history: Any = None,"` | — |
| [SRC-5587371288-L000472](../../agents/intent_router.py#L472) | 472 | `"    mode: str = \"auto\","` | — |
| [SRC-5587371288-L000473](../../agents/intent_router.py#L473) | 473 | `"    *,"` | — |
| [SRC-5587371288-L000474](../../agents/intent_router.py#L474) | 474 | `"    capability_question: bool = False,"` | — |
| [SRC-5587371288-L000475](../../agents/intent_router.py#L475) | 475 | `"    requires_web: bool = False,"` | — |
| [SRC-5587371288-L000476](../../agents/intent_router.py#L476) | 476 | `") -> dict[str, Any]:"` | — |
| [SRC-5587371288-L000477](../../agents/intent_router.py#L477) | 477 | `"    \"\"\"Return a deterministic route and auditable reason for a user question.\"\"\""` | — |
| [SRC-5587371288-L000478](../../agents/intent_router.py#L478) | 478 | `"    clean_mode = mode.strip().lower() if isinstance(mode, str) else \"auto\""` | — |
| [SRC-5587371288-L000479](../../agents/intent_router.py#L479) | 479 | `""` | — |
| [SRC-5587371288-L000480](../../agents/intent_router.py#L480) | 480 | `"    # If the assistant just asked for a missing referent, bind the user's concise"` | — |
| [SRC-5587371288-L000481](../../agents/intent_router.py#L481) | 481 | `"    # reply to that pending question instead of answering the entity name in isolation."` | — |
| [SRC-5587371288-L000482](../../agents/intent_router.py#L482) | 482 | `"    if _is_clarification_answer(question, history):"` | — |
| [SRC-5587371288-L000483](../../agents/intent_router.py#L483) | 483 | `"        return {"` | — |
| [SRC-5587371288-L000484](../../agents/intent_router.py#L484) | 484 | `"            \"route\": \"WEB_DEEP\" if clean_mode == \"deep\" else \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000485](../../agents/intent_router.py#L485) | 485 | `"            \"reason\": \"answer_to_pending_clarification\","` | — |
| [SRC-5587371288-L000486](../../agents/intent_router.py#L486) | 486 | `"            \"context_available\": True,"` | — |
| [SRC-5587371288-L000487](../../agents/intent_router.py#L487) | 487 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000488](../../agents/intent_router.py#L488) | 488 | `"        }"` | — |
| [SRC-5587371288-L000489](../../agents/intent_router.py#L489) | 489 | `""` | — |
| [SRC-5587371288-L000490](../../agents/intent_router.py#L490) | 490 | `"    context_available = _has_context(history)"` | — |
| [SRC-5587371288-L000491](../../agents/intent_router.py#L491) | 491 | `""` | — |
| [SRC-5587371288-L000492](../../agents/intent_router.py#L492) | 492 | `"    # A search mode cannot supply a missing subject. Clarify genuinely elliptical"` | — |
| [SRC-5587371288-L000493](../../agents/intent_router.py#L493) | 493 | `"    # questions before honoring the UI's explicit research mode."` | — |
| [SRC-5587371288-L000494](../../agents/intent_router.py#L494) | 494 | `"    if _needs_clarification(question) and not context_available:"` | — |
| [SRC-5587371288-L000495](../../agents/intent_router.py#L495) | 495 | `"        return {"` | — |
| [SRC-5587371288-L000496](../../agents/intent_router.py#L496) | 496 | `"            \"route\": \"CLARIFY\","` | — |
| [SRC-5587371288-L000497](../../agents/intent_router.py#L497) | 497 | `"            \"reason\": \"missing_referent_and_no_conversation_context\","` | — |
| [SRC-5587371288-L000498](../../agents/intent_router.py#L498) | 498 | `"            \"context_available\": False,"` | — |
| [SRC-5587371288-L000499](../../agents/intent_router.py#L499) | 499 | `"            \"needs_clarification\": True,"` | — |
| [SRC-5587371288-L000500](../../agents/intent_router.py#L500) | 500 | `"        }"` | — |
| [SRC-5587371288-L000501](../../agents/intent_router.py#L501) | 501 | `""` | — |
| [SRC-5587371288-L000502](../../agents/intent_router.py#L502) | 502 | `"    # An explicitly selected mode controls research depth when the request itself"` | — |
| [SRC-5587371288-L000503](../../agents/intent_router.py#L503) | 503 | `"    # is sufficiently specified."` | — |
| [SRC-5587371288-L000504](../../agents/intent_router.py#L504) | 504 | `"    if clean_mode != \"auto\":"` | — |
| [SRC-5587371288-L000505](../../agents/intent_router.py#L505) | 505 | `"        # Research depth is a mode constraint; it must not erase the user's"` | — |
| [SRC-5587371288-L000506](../../agents/intent_router.py#L506) | 506 | `"        # explicit buyer-discovery intent or turn leads into generic web research."` | — |
| [SRC-5587371288-L000507](../../agents/intent_router.py#L507) | 507 | `"        if _is_lead_generation_request(question):"` | — |
| [SRC-5587371288-L000508](../../agents/intent_router.py#L508) | 508 | `"            return {"` | — |
| [SRC-5587371288-L000509](../../agents/intent_router.py#L509) | 509 | `"                \"route\": \"LEAD_GENERATION\","` | — |
| [SRC-5587371288-L000510](../../agents/intent_router.py#L510) | 510 | `"                \"reason\": \"explicit_buyer_discovery_with_selected_research_mode\","` | — |
| [SRC-5587371288-L000511](../../agents/intent_router.py#L511) | 511 | `"                \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000512](../../agents/intent_router.py#L512) | 512 | `"                \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000513](../../agents/intent_router.py#L513) | 513 | `"            }"` | — |
| [SRC-5587371288-L000514](../../agents/intent_router.py#L514) | 514 | `"        route = \"WEB_DEEP\" if clean_mode == \"deep\" else \"WEB_SIMPLE\""` | — |
| [SRC-5587371288-L000515](../../agents/intent_router.py#L515) | 515 | `"        return {"` | — |
| [SRC-5587371288-L000516](../../agents/intent_router.py#L516) | 516 | `"            \"route\": route,"` | — |
| [SRC-5587371288-L000517](../../agents/intent_router.py#L517) | 517 | `"            \"reason\": \"explicit_mode\","` | — |
| [SRC-5587371288-L000518](../../agents/intent_router.py#L518) | 518 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000519](../../agents/intent_router.py#L519) | 519 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000520](../../agents/intent_router.py#L520) | 520 | `"        }"` | — |
| [SRC-5587371288-L000521](../../agents/intent_router.py#L521) | 521 | `""` | — |
| [SRC-5587371288-L000522](../../agents/intent_router.py#L522) | 522 | `"    if capability_question and not requires_web:"` | — |
| [SRC-5587371288-L000523](../../agents/intent_router.py#L523) | 523 | `"        return {"` | — |
| [SRC-5587371288-L000524](../../agents/intent_router.py#L524) | 524 | `"            \"route\": \"LOCAL\","` | — |
| [SRC-5587371288-L000525](../../agents/intent_router.py#L525) | 525 | `"            \"reason\": \"capability_question\","` | — |
| [SRC-5587371288-L000526](../../agents/intent_router.py#L526) | 526 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000527](../../agents/intent_router.py#L527) | 527 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000528](../../agents/intent_router.py#L528) | 528 | `"        }"` | — |
| [SRC-5587371288-L000529](../../agents/intent_router.py#L529) | 529 | `""` | — |
| [SRC-5587371288-L000530](../../agents/intent_router.py#L530) | 530 | `"    if _is_smalltalk(question):"` | — |
| [SRC-5587371288-L000531](../../agents/intent_router.py#L531) | 531 | `"        return {"` | — |
| [SRC-5587371288-L000532](../../agents/intent_router.py#L532) | 532 | `"            \"route\": \"LOCAL\","` | — |
| [SRC-5587371288-L000533](../../agents/intent_router.py#L533) | 533 | `"            \"reason\": \"short_conversational_turn\","` | — |
| [SRC-5587371288-L000534](../../agents/intent_router.py#L534) | 534 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000535](../../agents/intent_router.py#L535) | 535 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000536](../../agents/intent_router.py#L536) | 536 | `"        }"` | — |
| [SRC-5587371288-L000537](../../agents/intent_router.py#L537) | 537 | `""` | — |
| [SRC-5587371288-L000538](../../agents/intent_router.py#L538) | 538 | `"    # A page/link summary needs a concrete source. Pasted text is handled locally;"` | — |
| [SRC-5587371288-L000539](../../agents/intent_router.py#L539) | 539 | `"    # an absent source must trigger clarification rather than a search for \"the page\"."` | — |
| [SRC-5587371288-L000540](../../agents/intent_router.py#L540) | 540 | `"    if _is_page_summarization_request(question):"` | — |
| [SRC-5587371288-L000541](../../agents/intent_router.py#L541) | 541 | `"        if _has_inline_summary_text(question):"` | — |
| [SRC-5587371288-L000542](../../agents/intent_router.py#L542) | 542 | `"            return {"` | — |
| [SRC-5587371288-L000543](../../agents/intent_router.py#L543) | 543 | `"                \"route\": \"MODEL_ONLY\","` | — |
| [SRC-5587371288-L000544](../../agents/intent_router.py#L544) | 544 | `"                \"reason\": \"summarization_text_provided\","` | — |
| [SRC-5587371288-L000545](../../agents/intent_router.py#L545) | 545 | `"                \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000546](../../agents/intent_router.py#L546) | 546 | `"                \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000547](../../agents/intent_router.py#L547) | 547 | `"            }"` | — |
| [SRC-5587371288-L000548](../../agents/intent_router.py#L548) | 548 | `"        if re.search(r\"https?://\", question, flags=re.IGNORECASE):"` | — |
| [SRC-5587371288-L000549](../../agents/intent_router.py#L549) | 549 | `"            return {"` | — |
| [SRC-5587371288-L000550](../../agents/intent_router.py#L550) | 550 | `"                \"route\": \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000551](../../agents/intent_router.py#L551) | 551 | `"                \"reason\": \"summarization_request\","` | — |
| [SRC-5587371288-L000552](../../agents/intent_router.py#L552) | 552 | `"                \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000553](../../agents/intent_router.py#L553) | 553 | `"                \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000554](../../agents/intent_router.py#L554) | 554 | `"            }"` | — |
| [SRC-5587371288-L000555](../../agents/intent_router.py#L555) | 555 | `"        return {"` | — |
| [SRC-5587371288-L000556](../../agents/intent_router.py#L556) | 556 | `"            \"route\": \"CLARIFY\","` | — |
| [SRC-5587371288-L000557](../../agents/intent_router.py#L557) | 557 | `"            \"reason\": \"missing_summarization_input\","` | — |
| [SRC-5587371288-L000558](../../agents/intent_router.py#L558) | 558 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000559](../../agents/intent_router.py#L559) | 559 | `"            \"needs_clarification\": True,"` | — |
| [SRC-5587371288-L000560](../../agents/intent_router.py#L560) | 560 | `"        }"` | — |
| [SRC-5587371288-L000561](../../agents/intent_router.py#L561) | 561 | `""` | — |
| [SRC-5587371288-L000562](../../agents/intent_router.py#L562) | 562 | `"    ambiguous = _is_contextual_followup(question) or _needs_clarification(question)"` | — |
| [SRC-5587371288-L000563](../../agents/intent_router.py#L563) | 563 | `"    if ambiguous:"` | — |
| [SRC-5587371288-L000564](../../agents/intent_router.py#L564) | 564 | `"        return {"` | — |
| [SRC-5587371288-L000565](../../agents/intent_router.py#L565) | 565 | `"            \"route\": \"WEB_DEEP\" if _is_deep(question) else \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000566](../../agents/intent_router.py#L566) | 566 | `"            \"reason\": \"ambiguous_followup_with_context\","` | — |
| [SRC-5587371288-L000567](../../agents/intent_router.py#L567) | 567 | `"            \"context_available\": True,"` | — |
| [SRC-5587371288-L000568](../../agents/intent_router.py#L568) | 568 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000569](../../agents/intent_router.py#L569) | 569 | `"        }"` | — |
| [SRC-5587371288-L000570](../../agents/intent_router.py#L570) | 570 | `""` | — |
| [SRC-5587371288-L000571](../../agents/intent_router.py#L571) | 571 | `"    if _is_lead_generation_request(question):"` | — |
| [SRC-5587371288-L000572](../../agents/intent_router.py#L572) | 572 | `"        return {"` | — |
| [SRC-5587371288-L000573](../../agents/intent_router.py#L573) | 573 | `"            \"route\": \"LEAD_GENERATION\","` | — |
| [SRC-5587371288-L000574](../../agents/intent_router.py#L574) | 574 | `"            \"reason\": \"explicit_prospect_or_buyer_discovery_request\","` | — |
| [SRC-5587371288-L000575](../../agents/intent_router.py#L575) | 575 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000576](../../agents/intent_router.py#L576) | 576 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000577](../../agents/intent_router.py#L577) | 577 | `"        }"` | — |
| [SRC-5587371288-L000578](../../agents/intent_router.py#L578) | 578 | `""` | — |
| [SRC-5587371288-L000579](../../agents/intent_router.py#L579) | 579 | `"    if _is_deep(question):"` | — |
| [SRC-5587371288-L000580](../../agents/intent_router.py#L580) | 580 | `"        return {"` | — |
| [SRC-5587371288-L000581](../../agents/intent_router.py#L581) | 581 | `"            \"route\": \"WEB_DEEP\","` | — |
| [SRC-5587371288-L000582](../../agents/intent_router.py#L582) | 582 | `"            \"reason\": \"comparison_or_multi_part_research\","` | — |
| [SRC-5587371288-L000583](../../agents/intent_router.py#L583) | 583 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000584](../../agents/intent_router.py#L584) | 584 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000585](../../agents/intent_router.py#L585) | 585 | `"        }"` | — |
| [SRC-5587371288-L000586](../../agents/intent_router.py#L586) | 586 | `""` | — |
| [SRC-5587371288-L000587](../../agents/intent_router.py#L587) | 587 | `"    if requires_web or _has_live_signal(question) or _has_explicit_source_request(question):"` | — |
| [SRC-5587371288-L000588](../../agents/intent_router.py#L588) | 588 | `"        return {"` | — |
| [SRC-5587371288-L000589](../../agents/intent_router.py#L589) | 589 | `"            \"route\": \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000590](../../agents/intent_router.py#L590) | 590 | `"            \"reason\": ("` | — |
| [SRC-5587371288-L000591](../../agents/intent_router.py#L591) | 591 | `"                \"explicit_evidence_request\""` | — |
| [SRC-5587371288-L000592](../../agents/intent_router.py#L592) | 592 | `"                if _has_explicit_source_request(question)"` | — |
| [SRC-5587371288-L000593](../../agents/intent_router.py#L593) | 593 | `"                else \"freshness_or_explicit_research_signal\""` | — |
| [SRC-5587371288-L000594](../../agents/intent_router.py#L594) | 594 | `"            ),"` | — |
| [SRC-5587371288-L000595](../../agents/intent_router.py#L595) | 595 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000596](../../agents/intent_router.py#L596) | 596 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000597](../../agents/intent_router.py#L597) | 597 | `"        }"` | — |
| [SRC-5587371288-L000598](../../agents/intent_router.py#L598) | 598 | `""` | — |
| [SRC-5587371288-L000599](../../agents/intent_router.py#L599) | 599 | `"    return {"` | — |
| [SRC-5587371288-L000600](../../agents/intent_router.py#L600) | 600 | `"        \"route\": \"MODEL_ONLY\","` | — |
| [SRC-5587371288-L000601](../../agents/intent_router.py#L601) | 601 | `"        \"reason\": \"stable_knowledge_or_conversation\","` | — |
| [SRC-5587371288-L000602](../../agents/intent_router.py#L602) | 602 | `"        \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000603](../../agents/intent_router.py#L603) | 603 | `"        \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000604](../../agents/intent_router.py#L604) | 604 | `"    }"` | — |
## الوكيل والمنطق

### FILE-C9CF9B54F8 — [agents/omarai.py](../../agents/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C9CF9B54F8-L000001](../../agents/omarai.py#L1) | 1 | `"\"\"\"Explainable Arabic lead-intent analysis and local SQLite storage.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000002](../../agents/omarai.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-C9CF9B54F8-L000003](../../agents/omarai.py#L3) | 3 | `""` | — |
| [SRC-C9CF9B54F8-L000004](../../agents/omarai.py#L4) | 4 | `"import csv"` | — |
| [SRC-C9CF9B54F8-L000005](../../agents/omarai.py#L5) | 5 | `"import hashlib"` | — |
| [SRC-C9CF9B54F8-L000006](../../agents/omarai.py#L6) | 6 | `"import hmac"` | — |
| [SRC-C9CF9B54F8-L000007](../../agents/omarai.py#L7) | 7 | `"import ipaddress"` | — |
| [SRC-C9CF9B54F8-L000008](../../agents/omarai.py#L8) | 8 | `"import json"` | — |
| [SRC-C9CF9B54F8-L000009](../../agents/omarai.py#L9) | 9 | `"import re"` | — |
| [SRC-C9CF9B54F8-L000010](../../agents/omarai.py#L10) | 10 | `"import secrets"` | — |
| [SRC-C9CF9B54F8-L000011](../../agents/omarai.py#L11) | 11 | `"import sqlite3"` | — |
| [SRC-C9CF9B54F8-L000012](../../agents/omarai.py#L12) | 12 | `"import unicodedata"` | — |
| [SRC-C9CF9B54F8-L000013](../../agents/omarai.py#L13) | 13 | `"from contextlib import contextmanager"` | — |
| [SRC-C9CF9B54F8-L000014](../../agents/omarai.py#L14) | 14 | `"from collections.abc import Iterator"` | — |
| [SRC-C9CF9B54F8-L000015](../../agents/omarai.py#L15) | 15 | `"from typing import Any"` | — |
| [SRC-C9CF9B54F8-L000016](../../agents/omarai.py#L16) | 16 | `"from datetime import UTC, datetime, timedelta"` | — |
| [SRC-C9CF9B54F8-L000017](../../agents/omarai.py#L17) | 17 | `"from pathlib import Path"` | — |
| [SRC-C9CF9B54F8-L000018](../../agents/omarai.py#L18) | 18 | `"import uuid"` | — |
| [SRC-C9CF9B54F8-L000019](../../agents/omarai.py#L19) | 19 | `"from urllib.parse import urlparse"` | — |
| [SRC-C9CF9B54F8-L000020](../../agents/omarai.py#L20) | 20 | `""` | — |
| [SRC-C9CF9B54F8-L000021](../../agents/omarai.py#L21) | 21 | `"from agents.sales_domain import ("` | — |
| [SRC-C9CF9B54F8-L000022](../../agents/omarai.py#L22) | 22 | `"    ContactabilityStatus,"` | — |
| [SRC-C9CF9B54F8-L000023](../../agents/omarai.py#L23) | 23 | `"    DemandEvidence,"` | — |
| [SRC-C9CF9B54F8-L000024](../../agents/omarai.py#L24) | 24 | `"    DemandSignal,"` | — |
| [SRC-C9CF9B54F8-L000025](../../agents/omarai.py#L25) | 25 | `"    DemandSignalType,"` | — |
| [SRC-C9CF9B54F8-L000026](../../agents/omarai.py#L26) | 26 | `"    EvidenceBasis,"` | — |
| [SRC-C9CF9B54F8-L000027](../../agents/omarai.py#L27) | 27 | `"    FreshnessStatus,"` | — |
| [SRC-C9CF9B54F8-L000028](../../agents/omarai.py#L28) | 28 | `"    IdentityStatus,"` | — |
| [SRC-C9CF9B54F8-L000029](../../agents/omarai.py#L29) | 29 | `"    LeadQualification,"` | — |
| [SRC-C9CF9B54F8-L000030](../../agents/omarai.py#L30) | 30 | `"    ProductFit,"` | — |
| [SRC-C9CF9B54F8-L000031](../../agents/omarai.py#L31) | 31 | `"    SourceQuality,"` | — |
| [SRC-C9CF9B54F8-L000032](../../agents/omarai.py#L32) | 32 | `")"` | — |
| [SRC-C9CF9B54F8-L000033](../../agents/omarai.py#L33) | 33 | `""` | — |
| [SRC-C9CF9B54F8-L000034](../../agents/omarai.py#L34) | 34 | `"MAX_TEXT = 12000"` | — |
| [SRC-C9CF9B54F8-L000035](../../agents/omarai.py#L35) | 35 | `"DEFAULT_TENANT_ID = \"tenant_default\""` | — |
| [SRC-C9CF9B54F8-L000036](../../agents/omarai.py#L36) | 36 | `"DEFAULT_USER_ID = \"user_local_admin\""` | — |
| [SRC-C9CF9B54F8-L000037](../../agents/omarai.py#L37) | 37 | `"_TRANSLATION = str.maketrans({\"أ\":\"ا\",\"إ\":\"ا\",\"آ\":\"ا\",\"ٱ\":\"ا\",\"ى\":\"ي\",\"ئ\":\"ي\",\"ؤ\":\"و\",\"ـ\":\"\"})"` | — |
| [SRC-C9CF9B54F8-L000038](../../agents/omarai.py#L38) | 38 | `"SIGNALS = {"` | — |
| [SRC-C9CF9B54F8-L000039](../../agents/omarai.py#L39) | 39 | `"    # Direct demand language is sector-neutral. A product mention alone is never"` | — |
| [SRC-C9CF9B54F8-L000040](../../agents/omarai.py#L40) | 40 | `"    # sufficient to establish buying intent."` | — |
| [SRC-C9CF9B54F8-L000041](../../agents/omarai.py#L41) | 41 | `"    \"high\": (35, ("` | — |
| [SRC-C9CF9B54F8-L000042](../../agents/omarai.py#L42) | 42 | `"        \"عايز اشتري\", \"عاوز اشتري\", \"محتاج اشتري\","` | — |
| [SRC-C9CF9B54F8-L000043](../../agents/omarai.py#L43) | 43 | `"        # Retain established property-language compatibility while allowing any sector."` | — |
| [SRC-C9CF9B54F8-L000044](../../agents/omarai.py#L44) | 44 | `"        \"بدور على شقة\", \"بدور على عقار\", \"مطلوب شقة\", \"عايز وحدة\","` | — |
| [SRC-C9CF9B54F8-L000045](../../agents/omarai.py#L45) | 45 | `"    )),"` | — |
| [SRC-C9CF9B54F8-L000046](../../agents/omarai.py#L46) | 46 | `"    \"direct_demand\": (55, ("` | — |
| [SRC-C9CF9B54F8-L000047](../../agents/omarai.py#L47) | 47 | `"        \"نحتاج شراء\", \"نبحث عن مورد\", \"مطلوب مورد\", \"مطلوب توريد\","` | — |
| [SRC-C9CF9B54F8-L000048](../../agents/omarai.py#L48) | 48 | `"        \"نحتاج توريد\", \"محتاجين توريد\", \"نحتاج نظام\", \"محتاجين نظام\","` | — |
| [SRC-C9CF9B54F8-L000049](../../agents/omarai.py#L49) | 49 | `"        \"نحتاج خدمة\", \"نحتاج عرض سعر\", \"مطلوب شراء\", \"طلب شراء\", \"طلب عرض سعر\","` | — |
| [SRC-C9CF9B54F8-L000050](../../agents/omarai.py#L50) | 50 | `"        \"طلب عروض اسعار\", \"مناقصة توريد\", \"نبحث عن شركة\", \"نحتاج شركة\","` | — |
| [SRC-C9CF9B54F8-L000051](../../agents/omarai.py#L51) | 51 | `"        # Sector-neutral procurement phrasing (e.g. fire-alarm systems, signage, CCTV)."` | — |
| [SRC-C9CF9B54F8-L000052](../../agents/omarai.py#L52) | 52 | `"        \"ابحث عن مورد\", \"ابحث عن شركة\", \"مطلوب نظام\", \"مطلوب خدمة\", \"مطلوب شركة\","` | — |
| [SRC-C9CF9B54F8-L000053](../../agents/omarai.py#L53) | 53 | `"        \"مطلوب تركيب\", \"مطلوب صيانة\", \"نحتاج تركيب\", \"نحتاج صيانة\", \"محتاجين شركة\","` | — |
| [SRC-C9CF9B54F8-L000054](../../agents/omarai.py#L54) | 54 | `"        \"محتاج مورد\", \"محتاج عرض سعر\", \"عايز عرض سعر\", \"نرغب في شراء\", \"نرغب بشراء\","` | — |
| [SRC-C9CF9B54F8-L000055](../../agents/omarai.py#L55) | 55 | `"        \"نرغب في توريد\", \"اريد شراء\","` | — |
| [SRC-C9CF9B54F8-L000056](../../agents/omarai.py#L56) | 56 | `"        \"looking to buy\", \"need to purchase\", \"seeking a supplier\","` | — |
| [SRC-C9CF9B54F8-L000057](../../agents/omarai.py#L57) | 57 | `"        \"need a supplier\", \"request for quotation\", \"purchase request\","` | — |
| [SRC-C9CF9B54F8-L000058](../../agents/omarai.py#L58) | 58 | `"        \"procurement request\", \"rfq\", \"request a quote\","` | — |
| [SRC-C9CF9B54F8-L000059](../../agents/omarai.py#L59) | 59 | `"    )),"` | — |
| [SRC-C9CF9B54F8-L000060](../../agents/omarai.py#L60) | 60 | `"    \"next_step\": (20, ("` | — |
| [SRC-C9CF9B54F8-L000061](../../agents/omarai.py#L61) | 61 | `"        \"ممكن معاينة\", \"عايز اعاين\", \"عاوز اعاين\", \"ابعت التفاصيل\","` | — |
| [SRC-C9CF9B54F8-L000062](../../agents/omarai.py#L62) | 62 | `"        \"ابعت اللوكيشن\", \"ميعاد للمعاينة\", \"ابعت عرض سعر\", \"ارسل عرض سعر\","` | — |
| [SRC-C9CF9B54F8-L000063](../../agents/omarai.py#L63) | 63 | `"        \"نحتاج عرض سعر\", \"يرجى تقديم عرض\", \"send a quotation\","` | — |
| [SRC-C9CF9B54F8-L000064](../../agents/omarai.py#L64) | 64 | `"        \"send quote\", \"contact for quote\","` | — |
| [SRC-C9CF9B54F8-L000065](../../agents/omarai.py#L65) | 65 | `"    )),"` | — |
| [SRC-C9CF9B54F8-L000066](../../agents/omarai.py#L66) | 66 | `"    \"budget\": (15, ("` | — |
| [SRC-C9CF9B54F8-L000067](../../agents/omarai.py#L67) | 67 | `"        \"السعر كام\", \"مقدم كام\", \"ميزانيتي\", \"معايا مقدم\", \"تقسيط\","` | — |
| [SRC-C9CF9B54F8-L000068](../../agents/omarai.py#L68) | 68 | `"        \"على اقساط\", \"في حدود\", \"ما هي التكلفة\", \"what is the price\","` | — |
| [SRC-C9CF9B54F8-L000069](../../agents/omarai.py#L69) | 69 | `"        \"what does it cost\", \"budget is\","` | — |
| [SRC-C9CF9B54F8-L000070](../../agents/omarai.py#L70) | 70 | `"    )),"` | — |
| [SRC-C9CF9B54F8-L000071](../../agents/omarai.py#L71) | 71 | `"    \"explore\": (10, ("` | — |
| [SRC-C9CF9B54F8-L000072](../../agents/omarai.py#L72) | 72 | `"        \"بدور على\", \"فيه شقق\", \"ايه المتاح\", \"عايز اعرف الاسعار\","` | — |
| [SRC-C9CF9B54F8-L000073](../../agents/omarai.py#L73) | 73 | `"        \"ابحث عن\", \"نبحث عن\", \"looking for\", \"seeking information\","` | — |
| [SRC-C9CF9B54F8-L000074](../../agents/omarai.py#L74) | 74 | `"    )),"` | — |
| [SRC-C9CF9B54F8-L000075](../../agents/omarai.py#L75) | 75 | `"}"` | — |
| [SRC-C9CF9B54F8-L000076](../../agents/omarai.py#L76) | 76 | `"NOT_BUYER = ("` | — |
| [SRC-C9CF9B54F8-L000077](../../agents/omarai.py#L77) | 77 | `"    \"مش عايز اشتري\", \"مش عاوز اشتري\", \"مش بدور على\", \"مش محتاج\","` | — |
| [SRC-C9CF9B54F8-L000078](../../agents/omarai.py#L78) | 78 | `"    \"مش محتاجين\", \"لا نحتاج\", \"لا نبحث عن\", \"لسنا بحاجة\","` | — |
| [SRC-C9CF9B54F8-L000079](../../agents/omarai.py#L79) | 79 | `"    \"ما عنديش نية\", \"مش ناوي\", \"مش مهتم\", \"مش هشتري\","` | — |
| [SRC-C9CF9B54F8-L000080](../../agents/omarai.py#L80) | 80 | `"    \"not interested\", \"not looking for\", \"do not need\", \"don't need\", \"not seeking\","` | — |
| [SRC-C9CF9B54F8-L000081](../../agents/omarai.py#L81) | 81 | `"    \"عايز ابيع\", \"عاوز ابيع\", \"عندي شقة للبيع\", \"انا وسيط\", \"انا سمسار\","` | — |
| [SRC-C9CF9B54F8-L000082](../../agents/omarai.py#L82) | 82 | `"    \"عايز ايجار\", \"للايجار\", \"not looking for\", \"do not need\","` | — |
| [SRC-C9CF9B54F8-L000083](../../agents/omarai.py#L83) | 83 | `"    \"don't need\", \"not seeking\","` | — |
| [SRC-C9CF9B54F8-L000084](../../agents/omarai.py#L84) | 84 | `")"` | — |
| [SRC-C9CF9B54F8-L000085](../../agents/omarai.py#L85) | 85 | `"CLOSED_OR_STALE = ("` | — |
| [SRC-C9CF9B54F8-L000086](../../agents/omarai.py#L86) | 86 | `"    \"تم الغاء الطلب\", \"الغيت الطلب\", \"لغيت الطلب\","` | — |
| [SRC-C9CF9B54F8-L000087](../../agents/omarai.py#L87) | 87 | `"    \"تم الشراء\", \"اشترينا\", \"اشتريت بالفعل\", \"تم التعاقد\", \"تعاقدنا\","` | — |
| [SRC-C9CF9B54F8-L000088](../../agents/omarai.py#L88) | 88 | `"    \"وجدنا مورد\", \"تم اختيار المورد\", \"تم التوريد\", \"اكتمل التوريد\","` | — |
| [SRC-C9CF9B54F8-L000089](../../agents/omarai.py#L89) | 89 | `"    \"تم حل المشكلة\", \"لم نعد بحاجة\", \"already purchased\", \"we purchased\","` | — |
| [SRC-C9CF9B54F8-L000090](../../agents/omarai.py#L90) | 90 | `"    \"contract awarded\", \"supplier selected\", \"need fulfilled\","` | — |
| [SRC-C9CF9B54F8-L000091](../../agents/omarai.py#L91) | 91 | `"    \"no longer needed\", \"كنت بدور على\", \"كنت محتاج\", \"كنت ابحث عن\","` | — |
| [SRC-C9CF9B54F8-L000092](../../agents/omarai.py#L92) | 92 | `"    \"was looking for\", \"previously needed\","` | — |
| [SRC-C9CF9B54F8-L000093](../../agents/omarai.py#L93) | 93 | `")"` | — |
| [SRC-C9CF9B54F8-L000094](../../agents/omarai.py#L94) | 94 | `""` | — |
| [SRC-C9CF9B54F8-L000095](../../agents/omarai.py#L95) | 95 | `"def normalize(text: str) -> str:"` | — |
| [SRC-C9CF9B54F8-L000096](../../agents/omarai.py#L96) | 96 | `"    value = unicodedata.normalize(\"NFKC\", str(text)).translate(_TRANSLATION)"` | — |
| [SRC-C9CF9B54F8-L000097](../../agents/omarai.py#L97) | 97 | `"    value = \"\".join(c for c in value if not unicodedata.category(c).startswith(\"M\"))"` | — |
| [SRC-C9CF9B54F8-L000098](../../agents/omarai.py#L98) | 98 | `"    return re.sub(r\"\\s+\", \" \", re.sub(r\"[^\\w\\s]\", \" \", value.casefold())).strip()"` | — |
| [SRC-C9CF9B54F8-L000099](../../agents/omarai.py#L99) | 99 | `""` | — |
| [SRC-C9CF9B54F8-L000100](../../agents/omarai.py#L100) | 100 | `"def now_utc() -> str:"` | — |
| [SRC-C9CF9B54F8-L000101](../../agents/omarai.py#L101) | 101 | `"    return datetime.now(UTC).isoformat(timespec=\"seconds\").replace(\"+00:00\", \"Z\")"` | — |
| [SRC-C9CF9B54F8-L000102](../../agents/omarai.py#L102) | 102 | `""` | — |
| [SRC-C9CF9B54F8-L000103](../../agents/omarai.py#L103) | 103 | `"def _csv_safe_cell(value: object) -> str:"` | — |
| [SRC-C9CF9B54F8-L000104](../../agents/omarai.py#L104) | 104 | `"    \"\"\"Prefix spreadsheet formulas even when hidden whitespace/control chars precede them.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000105](../../agents/omarai.py#L105) | 105 | `"    text = \"\" if value is None else str(value)"` | — |
| [SRC-C9CF9B54F8-L000106](../../agents/omarai.py#L106) | 106 | `"    if not text:"` | — |
| [SRC-C9CF9B54F8-L000107](../../agents/omarai.py#L107) | 107 | `"        return text"` | — |
| [SRC-C9CF9B54F8-L000108](../../agents/omarai.py#L108) | 108 | `"    index = 0"` | — |
| [SRC-C9CF9B54F8-L000109](../../agents/omarai.py#L109) | 109 | `"    while index < len(text) and ("` | — |
| [SRC-C9CF9B54F8-L000110](../../agents/omarai.py#L110) | 110 | `"        text[index].isspace()"` | — |
| [SRC-C9CF9B54F8-L000111](../../agents/omarai.py#L111) | 111 | `"        or unicodedata.category(text[index]) in {\"Cc\", \"Cf\"}"` | — |
| [SRC-C9CF9B54F8-L000112](../../agents/omarai.py#L112) | 112 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000113](../../agents/omarai.py#L113) | 113 | `"        index += 1"` | — |
| [SRC-C9CF9B54F8-L000114](../../agents/omarai.py#L114) | 114 | `"    first_non_format = text[index:index + 1]"` | — |
| [SRC-C9CF9B54F8-L000115](../../agents/omarai.py#L115) | 115 | `"    formula_prefixes = {\"=\", \"+\", \"-\", \"@\", \"＝\", \"＋\", \"－\", \"＠\"}"` | — |
| [SRC-C9CF9B54F8-L000116](../../agents/omarai.py#L116) | 116 | `"    if text[0] in \"\\t\\r\\n\" or first_non_format in formula_prefixes:"` | — |
| [SRC-C9CF9B54F8-L000117](../../agents/omarai.py#L117) | 117 | `"        # OWASP notes that a tab inside the quoted CSV field is more resilient"` | — |
| [SRC-C9CF9B54F8-L000118](../../agents/omarai.py#L118) | 118 | `"        # in Excel than an apostrophe, although no CSV mitigation is universal."` | — |
| [SRC-C9CF9B54F8-L000119](../../agents/omarai.py#L119) | 119 | `"        return \"\\t\" + text"` | — |
| [SRC-C9CF9B54F8-L000120](../../agents/omarai.py#L120) | 120 | `"    return text"` | — |
| [SRC-C9CF9B54F8-L000121](../../agents/omarai.py#L121) | 121 | `""` | — |
| [SRC-C9CF9B54F8-L000122](../../agents/omarai.py#L122) | 122 | `"def _signal_type_for_matches(matches: list[dict]) -> DemandSignalType:"` | — |
| [SRC-C9CF9B54F8-L000123](../../agents/omarai.py#L123) | 123 | `"    categories = {item[\"category\"] for item in matches}"` | — |
| [SRC-C9CF9B54F8-L000124](../../agents/omarai.py#L124) | 124 | `"    phrases = {normalize(item[\"phrase\"]) for item in matches}"` | — |
| [SRC-C9CF9B54F8-L000125](../../agents/omarai.py#L125) | 125 | `"    if \"direct_demand\" in categories:"` | — |
| [SRC-C9CF9B54F8-L000126](../../agents/omarai.py#L126) | 126 | `"        if any(token in phrases for token in {"` | — |
| [SRC-C9CF9B54F8-L000127](../../agents/omarai.py#L127) | 127 | `"            normalize(\"طلب عرض سعر\"), normalize(\"طلب عروض اسعار\"),"` | — |
| [SRC-C9CF9B54F8-L000128](../../agents/omarai.py#L128) | 128 | `"            normalize(\"نحتاج عرض سعر\"), normalize(\"محتاج عرض سعر\"), normalize(\"عايز عرض سعر\"),"` | — |
| [SRC-C9CF9B54F8-L000129](../../agents/omarai.py#L129) | 129 | `"            normalize(\"request for quotation\"), normalize(\"rfq\"),"` | — |
| [SRC-C9CF9B54F8-L000130](../../agents/omarai.py#L130) | 130 | `"            normalize(\"request a quote\"),"` | — |
| [SRC-C9CF9B54F8-L000131](../../agents/omarai.py#L131) | 131 | `"        }):"` | — |
| [SRC-C9CF9B54F8-L000132](../../agents/omarai.py#L132) | 132 | `"            return DemandSignalType.REQUEST_FOR_QUOTATION"` | — |
| [SRC-C9CF9B54F8-L000133](../../agents/omarai.py#L133) | 133 | `"        if any(token in phrases for token in {"` | — |
| [SRC-C9CF9B54F8-L000134](../../agents/omarai.py#L134) | 134 | `"            normalize(\"مناقصة توريد\"), normalize(\"procurement request\"),"` | — |
| [SRC-C9CF9B54F8-L000135](../../agents/omarai.py#L135) | 135 | `"        }):"` | — |
| [SRC-C9CF9B54F8-L000136](../../agents/omarai.py#L136) | 136 | `"            return DemandSignalType.TENDER_OR_PROCUREMENT"` | — |
| [SRC-C9CF9B54F8-L000137](../../agents/omarai.py#L137) | 137 | `"        return DemandSignalType.DIRECT_PURCHASE_REQUEST"` | — |
| [SRC-C9CF9B54F8-L000138](../../agents/omarai.py#L138) | 138 | `"    if \"high\" in categories:"` | — |
| [SRC-C9CF9B54F8-L000139](../../agents/omarai.py#L139) | 139 | `"        return DemandSignalType.STATED_NEED"` | — |
| [SRC-C9CF9B54F8-L000140](../../agents/omarai.py#L140) | 140 | `"    if categories.intersection({\"next_step\", \"budget\", \"explore\"}):"` | — |
| [SRC-C9CF9B54F8-L000141](../../agents/omarai.py#L141) | 141 | `"        return DemandSignalType.INDIRECT_INDICATOR"` | — |
| [SRC-C9CF9B54F8-L000142](../../agents/omarai.py#L142) | 142 | `"    return DemandSignalType.UNKNOWN"` | — |
| [SRC-C9CF9B54F8-L000143](../../agents/omarai.py#L143) | 143 | `""` | — |
| [SRC-C9CF9B54F8-L000144](../../agents/omarai.py#L144) | 144 | `""` | — |
| [SRC-C9CF9B54F8-L000145](../../agents/omarai.py#L145) | 145 | `"def _contains_normalized_phrase(body: str, phrase: str) -> bool:"` | — |
| [SRC-C9CF9B54F8-L000146](../../agents/omarai.py#L146) | 146 | `"    \"\"\"Match a normalized phrase while allowing common attached Arabic clitics.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000147](../../agents/omarai.py#L147) | 147 | `"    normalized_phrase = normalize(phrase)"` | — |
| [SRC-C9CF9B54F8-L000148](../../agents/omarai.py#L148) | 148 | `"    if not normalized_phrase:"` | — |
| [SRC-C9CF9B54F8-L000149](../../agents/omarai.py#L149) | 149 | `"        return False"` | — |
| [SRC-C9CF9B54F8-L000150](../../agents/omarai.py#L150) | 150 | `"    # Arabic conjunctions/prepositions are commonly attached to the next word"` | — |
| [SRC-C9CF9B54F8-L000151](../../agents/omarai.py#L151) | 151 | `"    # (e.g. \"وممكن معاينة\"); allow one such prefix without partial-word matches."` | — |
| [SRC-C9CF9B54F8-L000152](../../agents/omarai.py#L152) | 152 | `"    pattern = rf\"(?<!\\w)(?:[وفبكل])?{re.escape(normalized_phrase)}(?!\\w)\""` | — |
| [SRC-C9CF9B54F8-L000153](../../agents/omarai.py#L153) | 153 | `"    return re.search(pattern, body, flags=re.UNICODE) is not None"` | — |
| [SRC-C9CF9B54F8-L000154](../../agents/omarai.py#L154) | 154 | `""` | — |
| [SRC-C9CF9B54F8-L000155](../../agents/omarai.py#L155) | 155 | `""` | — |
| [SRC-C9CF9B54F8-L000156](../../agents/omarai.py#L156) | 156 | `"def analyze(text: str, product_terms=(), location_terms=()) -> dict:"` | — |
| [SRC-C9CF9B54F8-L000157](../../agents/omarai.py#L157) | 157 | `"    \"\"\"Score explicit demand language without treating product fit as purchase intent.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000158](../../agents/omarai.py#L158) | 158 | `"    if not isinstance(text, str) or not text.strip():"` | — |
| [SRC-C9CF9B54F8-L000159](../../agents/omarai.py#L159) | 159 | `"        raise ValueError(\"text must not be empty\")"` | — |
| [SRC-C9CF9B54F8-L000160](../../agents/omarai.py#L160) | 160 | `"    if len(text) > MAX_TEXT:"` | — |
| [SRC-C9CF9B54F8-L000161](../../agents/omarai.py#L161) | 161 | `"        raise ValueError(f\"text must be at most {MAX_TEXT} characters\")"` | — |
| [SRC-C9CF9B54F8-L000162](../../agents/omarai.py#L162) | 162 | `""` | — |
| [SRC-C9CF9B54F8-L000163](../../agents/omarai.py#L163) | 163 | `"    body = normalize(text)"` | — |
| [SRC-C9CF9B54F8-L000164](../../agents/omarai.py#L164) | 164 | `"    closed = [phrase for phrase in CLOSED_OR_STALE if _contains_normalized_phrase(body, phrase)]"` | — |
| [SRC-C9CF9B54F8-L000165](../../agents/omarai.py#L165) | 165 | `"    if closed:"` | — |
| [SRC-C9CF9B54F8-L000166](../../agents/omarai.py#L166) | 166 | `"        return {"` | — |
| [SRC-C9CF9B54F8-L000167](../../agents/omarai.py#L167) | 167 | `"            \"score\": 0,"` | — |
| [SRC-C9CF9B54F8-L000168](../../agents/omarai.py#L168) | 168 | `"            \"label\": \"closed_or_stale_signal\","` | — |
| [SRC-C9CF9B54F8-L000169](../../agents/omarai.py#L169) | 169 | `"            \"signal_type\": ("` | — |
| [SRC-C9CF9B54F8-L000170](../../agents/omarai.py#L170) | 170 | `"                DemandSignalType.CANCELLED.value"` | — |
| [SRC-C9CF9B54F8-L000171](../../agents/omarai.py#L171) | 171 | `"                if any(normalize(phrase) in {normalize(\"تم الغاء الطلب\"), normalize(\"الغيت الطلب\"), normalize(\"لغيت الطلب\")} for phrase in closed)"` | — |
| [SRC-C9CF9B54F8-L000172](../../agents/omarai.py#L172) | 172 | `"                else DemandSignalType.EXPIRED.value"` | — |
| [SRC-C9CF9B54F8-L000173](../../agents/omarai.py#L173) | 173 | `"            ),"` | — |
| [SRC-C9CF9B54F8-L000174](../../agents/omarai.py#L174) | 174 | `"            \"summary\": \"الإشارة قديمة أو تم تلبية الاحتياج؛ لا تُعامل كطلب شراء نشط.\","` | — |
| [SRC-C9CF9B54F8-L000175](../../agents/omarai.py#L175) | 175 | `"            \"matched_signals\": ["` | — |
| [SRC-C9CF9B54F8-L000176](../../agents/omarai.py#L176) | 176 | `"                {\"phrase\": phrase, \"category\": \"closed_or_stale\", \"points\": 0}"` | — |
| [SRC-C9CF9B54F8-L000177](../../agents/omarai.py#L177) | 177 | `"                for phrase in closed"` | — |
| [SRC-C9CF9B54F8-L000178](../../agents/omarai.py#L178) | 178 | `"            ],"` | — |
| [SRC-C9CF9B54F8-L000179](../../agents/omarai.py#L179) | 179 | `"            \"warnings\": [\"تحقق من التاريخ والسياق قبل أي متابعة.\"],"` | — |
| [SRC-C9CF9B54F8-L000180](../../agents/omarai.py#L180) | 180 | `"        }"` | — |
| [SRC-C9CF9B54F8-L000181](../../agents/omarai.py#L181) | 181 | `""` | — |
| [SRC-C9CF9B54F8-L000182](../../agents/omarai.py#L182) | 182 | `"    excluded = [phrase for phrase in NOT_BUYER if _contains_normalized_phrase(body, phrase)]"` | — |
| [SRC-C9CF9B54F8-L000183](../../agents/omarai.py#L183) | 183 | `"    if excluded:"` | — |
| [SRC-C9CF9B54F8-L000184](../../agents/omarai.py#L184) | 184 | `"        return {"` | — |
| [SRC-C9CF9B54F8-L000185](../../agents/omarai.py#L185) | 185 | `"            \"score\": 0,"` | — |
| [SRC-C9CF9B54F8-L000186](../../agents/omarai.py#L186) | 186 | `"            \"label\": \"not_buyer_signal\","` | — |
| [SRC-C9CF9B54F8-L000187](../../agents/omarai.py#L187) | 187 | `"            \"signal_type\": DemandSignalType.NEGATED.value,"` | — |
| [SRC-C9CF9B54F8-L000188](../../agents/omarai.py#L188) | 188 | `"            \"summary\": \"النص ينفي الاحتياج أو لا يمثل طلب شراء نشطًا؛ راجعه يدويًا.\","` | — |
| [SRC-C9CF9B54F8-L000189](../../agents/omarai.py#L189) | 189 | `"            \"matched_signals\": ["` | — |
| [SRC-C9CF9B54F8-L000190](../../agents/omarai.py#L190) | 190 | `"                {\"phrase\": phrase, \"category\": \"exclusion\", \"points\": 0}"` | — |
| [SRC-C9CF9B54F8-L000191](../../agents/omarai.py#L191) | 191 | `"                for phrase in excluded"` | — |
| [SRC-C9CF9B54F8-L000192](../../agents/omarai.py#L192) | 192 | `"            ],"` | — |
| [SRC-C9CF9B54F8-L000193](../../agents/omarai.py#L193) | 193 | `"            \"warnings\": [\"لا تُصنّف النفي كإشارة شراء.\"],"` | — |
| [SRC-C9CF9B54F8-L000194](../../agents/omarai.py#L194) | 194 | `"        }"` | — |
| [SRC-C9CF9B54F8-L000195](../../agents/omarai.py#L195) | 195 | `""` | — |
| [SRC-C9CF9B54F8-L000196](../../agents/omarai.py#L196) | 196 | `"    matches = []"` | — |
| [SRC-C9CF9B54F8-L000197](../../agents/omarai.py#L197) | 197 | `"    for category, (points, phrases) in SIGNALS.items():"` | — |
| [SRC-C9CF9B54F8-L000198](../../agents/omarai.py#L198) | 198 | `"        found = next("` | — |
| [SRC-C9CF9B54F8-L000199](../../agents/omarai.py#L199) | 199 | `"            (phrase for phrase in phrases if _contains_normalized_phrase(body, phrase)),"` | — |
| [SRC-C9CF9B54F8-L000200](../../agents/omarai.py#L200) | 200 | `"            None,"` | — |
| [SRC-C9CF9B54F8-L000201](../../agents/omarai.py#L201) | 201 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000202](../../agents/omarai.py#L202) | 202 | `"        if found:"` | — |
| [SRC-C9CF9B54F8-L000203](../../agents/omarai.py#L203) | 203 | `"            matches.append({\"phrase\": found, \"category\": category, \"points\": points})"` | — |
| [SRC-C9CF9B54F8-L000204](../../agents/omarai.py#L204) | 204 | `""` | — |
| [SRC-C9CF9B54F8-L000205](../../agents/omarai.py#L205) | 205 | `"    # Product and location matches are contextual dimensions only. They must"` | — |
| [SRC-C9CF9B54F8-L000206](../../agents/omarai.py#L206) | 206 | `"    # never inflate the demand score or turn a catalogue mention into a lead."` | — |
| [SRC-C9CF9B54F8-L000207](../../agents/omarai.py#L207) | 207 | `"    for category, terms in ((\"product_context\", product_terms), (\"location_context\", location_terms)):"` | — |
| [SRC-C9CF9B54F8-L000208](../../agents/omarai.py#L208) | 208 | `"        found = next("` | — |
| [SRC-C9CF9B54F8-L000209](../../agents/omarai.py#L209) | 209 | `"            ("` | — |
| [SRC-C9CF9B54F8-L000210](../../agents/omarai.py#L210) | 210 | `"                normalize(term)"` | — |
| [SRC-C9CF9B54F8-L000211](../../agents/omarai.py#L211) | 211 | `"                for term in terms"` | — |
| [SRC-C9CF9B54F8-L000212](../../agents/omarai.py#L212) | 212 | `"                if isinstance(term, str)"` | — |
| [SRC-C9CF9B54F8-L000213](../../agents/omarai.py#L213) | 213 | `"                and normalize(term)"` | — |
| [SRC-C9CF9B54F8-L000214](../../agents/omarai.py#L214) | 214 | `"                and _contains_normalized_phrase(body, term)"` | — |
| [SRC-C9CF9B54F8-L000215](../../agents/omarai.py#L215) | 215 | `"            ),"` | — |
| [SRC-C9CF9B54F8-L000216](../../agents/omarai.py#L216) | 216 | `"            None,"` | — |
| [SRC-C9CF9B54F8-L000217](../../agents/omarai.py#L217) | 217 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000218](../../agents/omarai.py#L218) | 218 | `"        if found:"` | — |
| [SRC-C9CF9B54F8-L000219](../../agents/omarai.py#L219) | 219 | `"            matches.append({\"phrase\": found, \"category\": category, \"points\": 0})"` | — |
| [SRC-C9CF9B54F8-L000220](../../agents/omarai.py#L220) | 220 | `""` | — |
| [SRC-C9CF9B54F8-L000221](../../agents/omarai.py#L221) | 221 | `"    signal_type = _signal_type_for_matches(matches)"` | — |
| [SRC-C9CF9B54F8-L000222](../../agents/omarai.py#L222) | 222 | `"    score = min(100, sum(item[\"points\"] for item in matches))"` | — |
| [SRC-C9CF9B54F8-L000223](../../agents/omarai.py#L223) | 223 | `"    label = ("` | — |
| [SRC-C9CF9B54F8-L000224](../../agents/omarai.py#L224) | 224 | `"        \"high_intent\""` | — |
| [SRC-C9CF9B54F8-L000225](../../agents/omarai.py#L225) | 225 | `"        if score >= 55 and any("` | — |
| [SRC-C9CF9B54F8-L000226](../../agents/omarai.py#L226) | 226 | `"            item[\"category\"] in {\"high\", \"direct_demand\"} for item in matches"` | — |
| [SRC-C9CF9B54F8-L000227](../../agents/omarai.py#L227) | 227 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000228](../../agents/omarai.py#L228) | 228 | `"        else \"medium_intent\""` | — |
| [SRC-C9CF9B54F8-L000229](../../agents/omarai.py#L229) | 229 | `"        if score >= 40"` | — |
| [SRC-C9CF9B54F8-L000230](../../agents/omarai.py#L230) | 230 | `"        else \"early_research\""` | — |
| [SRC-C9CF9B54F8-L000231](../../agents/omarai.py#L231) | 231 | `"        if score >= 20"` | — |
| [SRC-C9CF9B54F8-L000232](../../agents/omarai.py#L232) | 232 | `"        else \"unclear\""` | — |
| [SRC-C9CF9B54F8-L000233](../../agents/omarai.py#L233) | 233 | `"    )"` | — |
| [SRC-C9CF9B54F8-L000234](../../agents/omarai.py#L234) | 234 | `"    return {"` | — |
| [SRC-C9CF9B54F8-L000235](../../agents/omarai.py#L235) | 235 | `"        \"score\": score,"` | — |
| [SRC-C9CF9B54F8-L000236](../../agents/omarai.py#L236) | 236 | `"        \"label\": label,"` | — |
| [SRC-C9CF9B54F8-L000237](../../agents/omarai.py#L237) | 237 | `"        \"signal_type\": signal_type.value,"` | — |
| [SRC-C9CF9B54F8-L000238](../../agents/omarai.py#L238) | 238 | `"        \"summary\": {"` | — |
| [SRC-C9CF9B54F8-L000239](../../agents/omarai.py#L239) | 239 | `"            \"high_intent\": \"إشارة طلب مباشرة نسبيًا؛ يلزم التحقق من المصدر والحداثة.\","` | — |
| [SRC-C9CF9B54F8-L000240](../../agents/omarai.py#L240) | 240 | `"            \"medium_intent\": \"مؤشرات اهتمام تستحق التأهيل والتحقق.\","` | — |
| [SRC-C9CF9B54F8-L000241](../../agents/omarai.py#L241) | 241 | `"            \"early_research\": \"اهتمام مبكر؛ ليس طلب شراء مؤكدًا.\","` | — |
| [SRC-C9CF9B54F8-L000242](../../agents/omarai.py#L242) | 242 | `"            \"unclear\": \"لا توجد لغة طلب كافية؛ ذكر المنتج وحده لا يكفي.\","` | — |
| [SRC-C9CF9B54F8-L000243](../../agents/omarai.py#L243) | 243 | `"        }[label],"` | — |
| [SRC-C9CF9B54F8-L000244](../../agents/omarai.py#L244) | 244 | `"        \"matched_signals\": matches,"` | — |
| [SRC-C9CF9B54F8-L000245](../../agents/omarai.py#L245) | 245 | `"        \"warnings\": ["` | — |
| [SRC-C9CF9B54F8-L000246](../../agents/omarai.py#L246) | 246 | `"            \"الدرجة ترتيبية وليست احتمالًا إحصائيًا للشراء.\","` | — |
| [SRC-C9CF9B54F8-L000247](../../agents/omarai.py#L247) | 247 | `"            \"لا تثبت هوية الكاتب أو قدرته على الدفع أو نيته.\","` | — |
| [SRC-C9CF9B54F8-L000248](../../agents/omarai.py#L248) | 248 | `"            \"ملاءمة المنتج والموقع سياق منفصل ولا يرفعان درجة الطلب.\","` | — |
| [SRC-C9CF9B54F8-L000249](../../agents/omarai.py#L249) | 249 | `"            \"استخدم مصادر عامة ومسموحًا بمعالجتها فقط.\","` | — |
| [SRC-C9CF9B54F8-L000250](../../agents/omarai.py#L250) | 250 | `"        ],"` | — |
| [SRC-C9CF9B54F8-L000251](../../agents/omarai.py#L251) | 251 | `"    }"` | — |
| [SRC-C9CF9B54F8-L000252](../../agents/omarai.py#L252) | 252 | `""` | — |
| [SRC-C9CF9B54F8-L000253](../../agents/omarai.py#L253) | 253 | `"def validate_url(url: str) -> str:"` | — |
| [SRC-C9CF9B54F8-L000254](../../agents/omarai.py#L254) | 254 | `"    parsed = urlparse(str(url or \"\").strip())"` | — |
| [SRC-C9CF9B54F8-L000255](../../agents/omarai.py#L255) | 255 | `"    if parsed.scheme not in (\"http\", \"https\") or not parsed.netloc or parsed.username or parsed.password:"` | — |
| [SRC-C9CF9B54F8-L000256](../../agents/omarai.py#L256) | 256 | `"        raise ValueError(\"source_url must be an absolute http(s) URL without embedded credentials\")"` | — |
| [SRC-C9CF9B54F8-L000257](../../agents/omarai.py#L257) | 257 | `"    if len(url) > 2048:"` | — |
| [SRC-C9CF9B54F8-L000258](../../agents/omarai.py#L258) | 258 | `"        raise ValueError(\"source_url is too long\")"` | — |
| [SRC-C9CF9B54F8-L000259](../../agents/omarai.py#L259) | 259 | `"    return url.strip()"` | — |
| [SRC-C9CF9B54F8-L000260](../../agents/omarai.py#L260) | 260 | `""` | — |
| [SRC-C9CF9B54F8-L000261](../../agents/omarai.py#L261) | 261 | `"def _qmark_to_psycopg(sql: str) -> str:"` | — |
| [SRC-C9CF9B54F8-L000262](../../agents/omarai.py#L262) | 262 | `"    \"\"\"Translate DB-API qmark placeholders without touching quoted SQL literals.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000263](../../agents/omarai.py#L263) | 263 | `"    output: list[str] = []"` | — |
| [SRC-C9CF9B54F8-L000264](../../agents/omarai.py#L264) | 264 | `"    quote: str \| None = None"` | — |
| [SRC-C9CF9B54F8-L000265](../../agents/omarai.py#L265) | 265 | `"    index = 0"` | — |
| [SRC-C9CF9B54F8-L000266](../../agents/omarai.py#L266) | 266 | `"    while index < len(sql):"` | — |
| [SRC-C9CF9B54F8-L000267](../../agents/omarai.py#L267) | 267 | `"        char = sql[index]"` | — |
| [SRC-C9CF9B54F8-L000268](../../agents/omarai.py#L268) | 268 | `"        if quote is not None:"` | — |
| [SRC-C9CF9B54F8-L000269](../../agents/omarai.py#L269) | 269 | `"            output.append(char)"` | — |
| [SRC-C9CF9B54F8-L000270](../../agents/omarai.py#L270) | 270 | `"            if char == quote:"` | — |
| [SRC-C9CF9B54F8-L000271](../../agents/omarai.py#L271) | 271 | `"                if index + 1 < len(sql) and sql[index + 1] == quote:"` | — |
| [SRC-C9CF9B54F8-L000272](../../agents/omarai.py#L272) | 272 | `"                    output.append(sql[index + 1])"` | — |
| [SRC-C9CF9B54F8-L000273](../../agents/omarai.py#L273) | 273 | `"                    index += 1"` | — |
| [SRC-C9CF9B54F8-L000274](../../agents/omarai.py#L274) | 274 | `"                else:"` | — |
| [SRC-C9CF9B54F8-L000275](../../agents/omarai.py#L275) | 275 | `"                    quote = None"` | — |
| [SRC-C9CF9B54F8-L000276](../../agents/omarai.py#L276) | 276 | `"        elif char in (\"'\", '\"'):"` | — |
| [SRC-C9CF9B54F8-L000277](../../agents/omarai.py#L277) | 277 | `"            quote = char"` | — |
| [SRC-C9CF9B54F8-L000278](../../agents/omarai.py#L278) | 278 | `"            output.append(char)"` | — |
| [SRC-C9CF9B54F8-L000279](../../agents/omarai.py#L279) | 279 | `"        elif char == \"?\":"` | — |
| [SRC-C9CF9B54F8-L000280](../../agents/omarai.py#L280) | 280 | `"            output.append(\"%s\")"` | — |
| [SRC-C9CF9B54F8-L000281](../../agents/omarai.py#L281) | 281 | `"        else:"` | — |
| [SRC-C9CF9B54F8-L000282](../../agents/omarai.py#L282) | 282 | `"            output.append(char)"` | — |
| [SRC-C9CF9B54F8-L000283](../../agents/omarai.py#L283) | 283 | `"        index += 1"` | — |
| [SRC-C9CF9B54F8-L000284](../../agents/omarai.py#L284) | 284 | `"    return \"\".join(output)"` | — |
| [SRC-C9CF9B54F8-L000285](../../agents/omarai.py#L285) | 285 | `""` | — |
| [SRC-C9CF9B54F8-L000286](../../agents/omarai.py#L286) | 286 | `""` | — |
| [SRC-C9CF9B54F8-L000287](../../agents/omarai.py#L287) | 287 | `"class _PostgresConnection:"` | — |
| [SRC-C9CF9B54F8-L000288](../../agents/omarai.py#L288) | 288 | `"    \"\"\"Small execute adapter keeping LeadStore SQL parameters backend-neutral.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000289](../../agents/omarai.py#L289) | 289 | `""` | — |
| [SRC-C9CF9B54F8-L000290](../../agents/omarai.py#L290) | 290 | `"    def __init__(self, connection):"` | — |
| [SRC-C9CF9B54F8-L000291](../../agents/omarai.py#L291) | 291 | `"        self._connection = connection"` | — |
| [SRC-C9CF9B54F8-L000292](../../agents/omarai.py#L292) | 292 | `""` | — |
| [SRC-C9CF9B54F8-L000293](../../agents/omarai.py#L293) | 293 | `"    def execute(self, sql: str, params=()):"` | — |
| [SRC-C9CF9B54F8-L000294](../../agents/omarai.py#L294) | 294 | `"        statement = sql"` | — |
| [SRC-C9CF9B54F8-L000295](../../agents/omarai.py#L295) | 295 | `"        if statement.lstrip().upper().startswith(\"INSERT OR IGNORE INTO\"):"` | — |
| [SRC-C9CF9B54F8-L000296](../../agents/omarai.py#L296) | 296 | `"            statement = statement.replace(\"INSERT OR IGNORE INTO\", \"INSERT INTO\", 1)"` | — |
| [SRC-C9CF9B54F8-L000297](../../agents/omarai.py#L297) | 297 | `"            statement = statement.rstrip().rstrip(\";\") + \" ON CONFLICT DO NOTHING\""` | — |
| [SRC-C9CF9B54F8-L000298](../../agents/omarai.py#L298) | 298 | `"        return self._connection.execute(_qmark_to_psycopg(statement), params)"` | — |
| [SRC-C9CF9B54F8-L000299](../../agents/omarai.py#L299) | 299 | `""` | — |
| [SRC-C9CF9B54F8-L000300](../../agents/omarai.py#L300) | 300 | `""` | — |
| [SRC-C9CF9B54F8-L000301](../../agents/omarai.py#L301) | 301 | `"class LeadStore:"` | — |
| [SRC-C9CF9B54F8-L000302](../../agents/omarai.py#L302) | 302 | `"    \"\"\"Tenant-scoped local SQLite or managed PostgreSQL lead storage.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000303](../../agents/omarai.py#L303) | 303 | `""` | — |
| [SRC-C9CF9B54F8-L000304](../../agents/omarai.py#L304) | 304 | `"    ALLOWED_STATUSES = frozenset({"` | — |
| [SRC-C9CF9B54F8-L000305](../../agents/omarai.py#L305) | 305 | `"        \"new\", \"qualified\", \"contacted\", \"converted\", \"rejected\", \"needs_review\""` | — |
| [SRC-C9CF9B54F8-L000306](../../agents/omarai.py#L306) | 306 | `"    })"` | — |
| [SRC-C9CF9B54F8-L000307](../../agents/omarai.py#L307) | 307 | `"    ALLOWED_ROLES = frozenset({\"owner\", \"admin\", \"manager\", \"sales_agent\", \"viewer\"})"` | — |
| [SRC-C9CF9B54F8-L000308](../../agents/omarai.py#L308) | 308 | `""` | — |
| [SRC-C9CF9B54F8-L000309](../../agents/omarai.py#L309) | 309 | `"    def __init__("` | — |
| [SRC-C9CF9B54F8-L000310](../../agents/omarai.py#L310) | 310 | `"        self,"` | — |
| [SRC-C9CF9B54F8-L000311](../../agents/omarai.py#L311) | 311 | `"        path: str \| Path \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000312](../../agents/omarai.py#L312) | 312 | `"        *,"` | — |
| [SRC-C9CF9B54F8-L000313](../../agents/omarai.py#L313) | 313 | `"        database_url: str \| None = None,"` | — |
| [SRC-C9CF9B54F8-L000314](../../agents/omarai.py#L314) | 314 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000315](../../agents/omarai.py#L315) | 315 | `"        clean_database_url = str(database_url or \"\").strip()"` | — |
| [SRC-C9CF9B54F8-L000316](../../agents/omarai.py#L316) | 316 | `"        if clean_database_url and path is not None:"` | — |
| [SRC-C9CF9B54F8-L000317](../../agents/omarai.py#L317) | 317 | `"            raise ValueError(\"configure either database_url or a SQLite path, not both\")"` | — |
| [SRC-C9CF9B54F8-L000318](../../agents/omarai.py#L318) | 318 | `"        if clean_database_url:"` | — |
| [SRC-C9CF9B54F8-L000319](../../agents/omarai.py#L319) | 319 | `"            if not clean_database_url.startswith((\"postgresql://\", \"postgres://\")):"` | — |
| [SRC-C9CF9B54F8-L000320](../../agents/omarai.py#L320) | 320 | `"                raise ValueError(\"database_url must use the PostgreSQL URL scheme\")"` | — |
| [SRC-C9CF9B54F8-L000321](../../agents/omarai.py#L321) | 321 | `"            self.backend = \"postgresql\""` | — |
| [SRC-C9CF9B54F8-L000322](../../agents/omarai.py#L322) | 322 | `"            self.database_url = clean_database_url"` | — |
| [SRC-C9CF9B54F8-L000323](../../agents/omarai.py#L323) | 323 | `"            self.path = None"` | — |
| [SRC-C9CF9B54F8-L000324](../../agents/omarai.py#L324) | 324 | `"        else:"` | — |
| [SRC-C9CF9B54F8-L000325](../../agents/omarai.py#L325) | 325 | `"            self.backend = \"sqlite\""` | — |
| [SRC-C9CF9B54F8-L000326](../../agents/omarai.py#L326) | 326 | `"            self.database_url = None"` | — |
| [SRC-C9CF9B54F8-L000327](../../agents/omarai.py#L327) | 327 | `"            self.path = Path(path or Path.home() / \".omarai\" / \"omarai.sqlite3\").expanduser()"` | — |
| [SRC-C9CF9B54F8-L000328](../../agents/omarai.py#L328) | 328 | `"            self.path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-C9CF9B54F8-L000329](../../agents/omarai.py#L329) | 329 | `""` | — |
| [SRC-C9CF9B54F8-L000330](../../agents/omarai.py#L330) | 330 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000331](../../agents/omarai.py#L331) | 331 | `"            self._initialize_schema(db)"` | — |
| [SRC-C9CF9B54F8-L000332](../../agents/omarai.py#L332) | 332 | `""` | — |
| [SRC-C9CF9B54F8-L000333](../../agents/omarai.py#L333) | 333 | `"    @contextmanager"` | — |
| [SRC-C9CF9B54F8-L000334](../../agents/omarai.py#L334) | 334 | `"    def connect(self) -> Iterator[Any]:"` | — |
| [SRC-C9CF9B54F8-L000335](../../agents/omarai.py#L335) | 335 | `"        \"\"\"Yield one transaction-scoped connection and always close it.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000336](../../agents/omarai.py#L336) | 336 | `"        if self.backend == \"postgresql\":"` | — |
| [SRC-C9CF9B54F8-L000337](../../agents/omarai.py#L337) | 337 | `"            try:"` | — |
| [SRC-C9CF9B54F8-L000338](../../agents/omarai.py#L338) | 338 | `"                import psycopg"` | — |
| [SRC-C9CF9B54F8-L000339](../../agents/omarai.py#L339) | 339 | `"                from psycopg.rows import dict_row"` | — |
| [SRC-C9CF9B54F8-L000340](../../agents/omarai.py#L340) | 340 | `"            except ImportError as exc:"` | — |
| [SRC-C9CF9B54F8-L000341](../../agents/omarai.py#L341) | 341 | `"                raise RuntimeError("` | — |
| [SRC-C9CF9B54F8-L000342](../../agents/omarai.py#L342) | 342 | `"                    \"PostgreSQL storage requires the psycopg package\""` | — |
| [SRC-C9CF9B54F8-L000343](../../agents/omarai.py#L343) | 343 | `"                ) from exc"` | — |
| [SRC-C9CF9B54F8-L000344](../../agents/omarai.py#L344) | 344 | `"            with psycopg.connect("` | — |
| [SRC-C9CF9B54F8-L000345](../../agents/omarai.py#L345) | 345 | `"                self.database_url,"` | — |
| [SRC-C9CF9B54F8-L000346](../../agents/omarai.py#L346) | 346 | `"                connect_timeout=10,"` | — |
| [SRC-C9CF9B54F8-L000347](../../agents/omarai.py#L347) | 347 | `"                row_factory=dict_row,"` | — |
| [SRC-C9CF9B54F8-L000348](../../agents/omarai.py#L348) | 348 | `"            ) as connection:"` | — |
| [SRC-C9CF9B54F8-L000349](../../agents/omarai.py#L349) | 349 | `"                yield _PostgresConnection(connection)"` | — |
| [SRC-C9CF9B54F8-L000350](../../agents/omarai.py#L350) | 350 | `"            return"` | — |
| [SRC-C9CF9B54F8-L000351](../../agents/omarai.py#L351) | 351 | `""` | — |
| [SRC-C9CF9B54F8-L000352](../../agents/omarai.py#L352) | 352 | `"        db = sqlite3.connect(self.path, timeout=10)"` | — |
| [SRC-C9CF9B54F8-L000353](../../agents/omarai.py#L353) | 353 | `"        try:"` | — |
| [SRC-C9CF9B54F8-L000354](../../agents/omarai.py#L354) | 354 | `"            db.row_factory = sqlite3.Row"` | — |
| [SRC-C9CF9B54F8-L000355](../../agents/omarai.py#L355) | 355 | `"            db.execute(\"PRAGMA foreign_keys = ON\")"` | — |
| [SRC-C9CF9B54F8-L000356](../../agents/omarai.py#L356) | 356 | `"            with db:"` | — |
| [SRC-C9CF9B54F8-L000357](../../agents/omarai.py#L357) | 357 | `"                yield db"` | — |
| [SRC-C9CF9B54F8-L000358](../../agents/omarai.py#L358) | 358 | `"        finally:"` | — |
| [SRC-C9CF9B54F8-L000359](../../agents/omarai.py#L359) | 359 | `"            db.close()"` | — |
| [SRC-C9CF9B54F8-L000360](../../agents/omarai.py#L360) | 360 | `""` | — |
| [SRC-C9CF9B54F8-L000361](../../agents/omarai.py#L361) | 361 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000362](../../agents/omarai.py#L362) | 362 | `"    def _create_leads_table(db):"` | — |
| [SRC-C9CF9B54F8-L000363](../../agents/omarai.py#L363) | 363 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000364](../../agents/omarai.py#L364) | 364 | `"            \"\"\"CREATE TABLE IF NOT EXISTS leads ("` | — |
| [SRC-C9CF9B54F8-L000365](../../agents/omarai.py#L365) | 365 | `"                id TEXT PRIMARY KEY,"` | — |
| [SRC-C9CF9B54F8-L000366](../../agents/omarai.py#L366) | 366 | `"                tenant_id TEXT NOT NULL REFERENCES tenants(id),"` | — |
| [SRC-C9CF9B54F8-L000367](../../agents/omarai.py#L367) | 367 | `"                fingerprint TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000368](../../agents/omarai.py#L368) | 368 | `"                text TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000369](../../agents/omarai.py#L369) | 369 | `"                source_url TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000370](../../agents/omarai.py#L370) | 370 | `"                platform TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000371](../../agents/omarai.py#L371) | 371 | `"                observed_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000372](../../agents/omarai.py#L372) | 372 | `"                assessment TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000373](../../agents/omarai.py#L373) | 373 | `"                status TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000374](../../agents/omarai.py#L374) | 374 | `"                note TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000375](../../agents/omarai.py#L375) | 375 | `"                created_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000376](../../agents/omarai.py#L376) | 376 | `"                updated_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000377](../../agents/omarai.py#L377) | 377 | `"                UNIQUE (tenant_id, fingerprint)"` | — |
| [SRC-C9CF9B54F8-L000378](../../agents/omarai.py#L378) | 378 | `"            )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000379](../../agents/omarai.py#L379) | 379 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000380](../../agents/omarai.py#L380) | 380 | `""` | — |
| [SRC-C9CF9B54F8-L000381](../../agents/omarai.py#L381) | 381 | `"    def _initialize_schema(self, db):"` | — |
| [SRC-C9CF9B54F8-L000382](../../agents/omarai.py#L382) | 382 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000383](../../agents/omarai.py#L383) | 383 | `"            \"\"\"CREATE TABLE IF NOT EXISTS tenants ("` | — |
| [SRC-C9CF9B54F8-L000384](../../agents/omarai.py#L384) | 384 | `"                id TEXT PRIMARY KEY,"` | — |
| [SRC-C9CF9B54F8-L000385](../../agents/omarai.py#L385) | 385 | `"                name TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000386](../../agents/omarai.py#L386) | 386 | `"                slug TEXT NOT NULL UNIQUE,"` | — |
| [SRC-C9CF9B54F8-L000387](../../agents/omarai.py#L387) | 387 | `"                active INTEGER NOT NULL DEFAULT 1,"` | — |
| [SRC-C9CF9B54F8-L000388](../../agents/omarai.py#L388) | 388 | `"                created_at TEXT NOT NULL"` | — |
| [SRC-C9CF9B54F8-L000389](../../agents/omarai.py#L389) | 389 | `"            )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000390](../../agents/omarai.py#L390) | 390 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000391](../../agents/omarai.py#L391) | 391 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000392](../../agents/omarai.py#L392) | 392 | `"            \"\"\"CREATE TABLE IF NOT EXISTS users ("` | — |
| [SRC-C9CF9B54F8-L000393](../../agents/omarai.py#L393) | 393 | `"                id TEXT PRIMARY KEY,"` | — |
| [SRC-C9CF9B54F8-L000394](../../agents/omarai.py#L394) | 394 | `"                email TEXT NOT NULL UNIQUE,"` | — |
| [SRC-C9CF9B54F8-L000395](../../agents/omarai.py#L395) | 395 | `"                display_name TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000396](../../agents/omarai.py#L396) | 396 | `"                active INTEGER NOT NULL DEFAULT 1,"` | — |
| [SRC-C9CF9B54F8-L000397](../../agents/omarai.py#L397) | 397 | `"                created_at TEXT NOT NULL"` | — |
| [SRC-C9CF9B54F8-L000398](../../agents/omarai.py#L398) | 398 | `"            )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000399](../../agents/omarai.py#L399) | 399 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000400](../../agents/omarai.py#L400) | 400 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000401](../../agents/omarai.py#L401) | 401 | `"            \"\"\"CREATE TABLE IF NOT EXISTS tenant_memberships ("` | — |
| [SRC-C9CF9B54F8-L000402](../../agents/omarai.py#L402) | 402 | `"                tenant_id TEXT NOT NULL REFERENCES tenants(id),"` | — |
| [SRC-C9CF9B54F8-L000403](../../agents/omarai.py#L403) | 403 | `"                user_id TEXT NOT NULL REFERENCES users(id),"` | — |
| [SRC-C9CF9B54F8-L000404](../../agents/omarai.py#L404) | 404 | `"                role TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000405](../../agents/omarai.py#L405) | 405 | `"                active INTEGER NOT NULL DEFAULT 1,"` | — |
| [SRC-C9CF9B54F8-L000406](../../agents/omarai.py#L406) | 406 | `"                created_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000407](../../agents/omarai.py#L407) | 407 | `"                PRIMARY KEY (tenant_id, user_id)"` | — |
| [SRC-C9CF9B54F8-L000408](../../agents/omarai.py#L408) | 408 | `"            )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000409](../../agents/omarai.py#L409) | 409 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000410](../../agents/omarai.py#L410) | 410 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000411](../../agents/omarai.py#L411) | 411 | `"            \"\"\"CREATE TABLE IF NOT EXISTS api_tokens ("` | — |
| [SRC-C9CF9B54F8-L000412](../../agents/omarai.py#L412) | 412 | `"                token_hash TEXT PRIMARY KEY,"` | — |
| [SRC-C9CF9B54F8-L000413](../../agents/omarai.py#L413) | 413 | `"                tenant_id TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000414](../../agents/omarai.py#L414) | 414 | `"                user_id TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000415](../../agents/omarai.py#L415) | 415 | `"                label TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000416](../../agents/omarai.py#L416) | 416 | `"                active INTEGER NOT NULL DEFAULT 1,"` | — |
| [SRC-C9CF9B54F8-L000417](../../agents/omarai.py#L417) | 417 | `"                created_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000418](../../agents/omarai.py#L418) | 418 | `"                expires_at TEXT,"` | — |
| [SRC-C9CF9B54F8-L000419](../../agents/omarai.py#L419) | 419 | `"                FOREIGN KEY (tenant_id, user_id)"` | — |
| [SRC-C9CF9B54F8-L000420](../../agents/omarai.py#L420) | 420 | `"                    REFERENCES tenant_memberships(tenant_id, user_id)"` | — |
| [SRC-C9CF9B54F8-L000421](../../agents/omarai.py#L421) | 421 | `"            )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000422](../../agents/omarai.py#L422) | 422 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000423](../../agents/omarai.py#L423) | 423 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000424](../../agents/omarai.py#L424) | 424 | `"            \"\"\"CREATE TABLE IF NOT EXISTS web_sessions ("` | — |
| [SRC-C9CF9B54F8-L000425](../../agents/omarai.py#L425) | 425 | `"                session_hash TEXT PRIMARY KEY,"` | — |
| [SRC-C9CF9B54F8-L000426](../../agents/omarai.py#L426) | 426 | `"                credential_hash TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000427](../../agents/omarai.py#L427) | 427 | `"                is_shared_token INTEGER NOT NULL DEFAULT 0,"` | — |
| [SRC-C9CF9B54F8-L000428](../../agents/omarai.py#L428) | 428 | `"                tenant_id TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000429](../../agents/omarai.py#L429) | 429 | `"                user_id TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000430](../../agents/omarai.py#L430) | 430 | `"                created_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000431](../../agents/omarai.py#L431) | 431 | `"                expires_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000432](../../agents/omarai.py#L432) | 432 | `"                revoked_at TEXT,"` | — |
| [SRC-C9CF9B54F8-L000433](../../agents/omarai.py#L433) | 433 | `"                FOREIGN KEY (tenant_id, user_id)"` | — |
| [SRC-C9CF9B54F8-L000434](../../agents/omarai.py#L434) | 434 | `"                    REFERENCES tenant_memberships(tenant_id, user_id)"` | — |
| [SRC-C9CF9B54F8-L000435](../../agents/omarai.py#L435) | 435 | `"            )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000436](../../agents/omarai.py#L436) | 436 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000437](../../agents/omarai.py#L437) | 437 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000438](../../agents/omarai.py#L438) | 438 | `"            \"CREATE INDEX IF NOT EXISTS idx_web_sessions_expiry \""` | — |
| [SRC-C9CF9B54F8-L000439](../../agents/omarai.py#L439) | 439 | `"            \"ON web_sessions(expires_at, revoked_at)\""` | — |
| [SRC-C9CF9B54F8-L000440](../../agents/omarai.py#L440) | 440 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000441](../../agents/omarai.py#L441) | 441 | `""` | — |
| [SRC-C9CF9B54F8-L000442](../../agents/omarai.py#L442) | 442 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L000443](../../agents/omarai.py#L443) | 443 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000444](../../agents/omarai.py#L444) | 444 | `"            \"\"\"INSERT OR IGNORE INTO tenants (id, name, slug, active, created_at)"` | — |
| [SRC-C9CF9B54F8-L000445](../../agents/omarai.py#L445) | 445 | `"               VALUES (?, ?, ?, 1, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000446](../../agents/omarai.py#L446) | 446 | `"            (DEFAULT_TENANT_ID, \"Omarai Workspace\", \"omarai-default\", now),"` | — |
| [SRC-C9CF9B54F8-L000447](../../agents/omarai.py#L447) | 447 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000448](../../agents/omarai.py#L448) | 448 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000449](../../agents/omarai.py#L449) | 449 | `"            \"\"\"INSERT OR IGNORE INTO users"` | — |
| [SRC-C9CF9B54F8-L000450](../../agents/omarai.py#L450) | 450 | `"               (id, email, display_name, active, created_at)"` | — |
| [SRC-C9CF9B54F8-L000451](../../agents/omarai.py#L451) | 451 | `"               VALUES (?, ?, ?, 1, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000452](../../agents/omarai.py#L452) | 452 | `"            (DEFAULT_USER_ID, \"local-admin@omarai.invalid\", \"Omarai Local Admin\", now),"` | — |
| [SRC-C9CF9B54F8-L000453](../../agents/omarai.py#L453) | 453 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000454](../../agents/omarai.py#L454) | 454 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000455](../../agents/omarai.py#L455) | 455 | `"            \"\"\"INSERT OR IGNORE INTO tenant_memberships"` | — |
| [SRC-C9CF9B54F8-L000456](../../agents/omarai.py#L456) | 456 | `"               (tenant_id, user_id, role, active, created_at)"` | — |
| [SRC-C9CF9B54F8-L000457](../../agents/omarai.py#L457) | 457 | `"               VALUES (?, ?, 'owner', 1, ?)\"\"\","` | — |
| [SRC-C9CF9B54F8-L000458](../../agents/omarai.py#L458) | 458 | `"            (DEFAULT_TENANT_ID, DEFAULT_USER_ID, now),"` | — |
| [SRC-C9CF9B54F8-L000459](../../agents/omarai.py#L459) | 459 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000460](../../agents/omarai.py#L460) | 460 | `""` | — |
| [SRC-C9CF9B54F8-L000461](../../agents/omarai.py#L461) | 461 | `"        if self.backend == \"sqlite\":"` | — |
| [SRC-C9CF9B54F8-L000462](../../agents/omarai.py#L462) | 462 | `"            table = db.execute("` | — |
| [SRC-C9CF9B54F8-L000463](../../agents/omarai.py#L463) | 463 | `"                \"SELECT 1 FROM sqlite_master WHERE type='table' AND name='leads'\""` | — |
| [SRC-C9CF9B54F8-L000464](../../agents/omarai.py#L464) | 464 | `"            ).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000465](../../agents/omarai.py#L465) | 465 | `"            if table:"` | — |
| [SRC-C9CF9B54F8-L000466](../../agents/omarai.py#L466) | 466 | `"                columns = {"` | — |
| [SRC-C9CF9B54F8-L000467](../../agents/omarai.py#L467) | 467 | `"                    row[\"name\"] for row in db.execute(\"PRAGMA table_info(leads)\").fetchall()"` | — |
| [SRC-C9CF9B54F8-L000468](../../agents/omarai.py#L468) | 468 | `"                }"` | — |
| [SRC-C9CF9B54F8-L000469](../../agents/omarai.py#L469) | 469 | `"                unique_fingerprint = False"` | — |
| [SRC-C9CF9B54F8-L000470](../../agents/omarai.py#L470) | 470 | `"                for index in db.execute(\"PRAGMA index_list(leads)\").fetchall():"` | — |
| [SRC-C9CF9B54F8-L000471](../../agents/omarai.py#L471) | 471 | `"                    if not index[\"unique\"]:"` | — |
| [SRC-C9CF9B54F8-L000472](../../agents/omarai.py#L472) | 472 | `"                        continue"` | — |
| [SRC-C9CF9B54F8-L000473](../../agents/omarai.py#L473) | 473 | `"                    index_columns = ["` | — |
| [SRC-C9CF9B54F8-L000474](../../agents/omarai.py#L474) | 474 | `"                        row[\"name\"]"` | — |
| [SRC-C9CF9B54F8-L000475](../../agents/omarai.py#L475) | 475 | `"                        for row in db.execute("` | — |
| [SRC-C9CF9B54F8-L000476](../../agents/omarai.py#L476) | 476 | `"                            f\"PRAGMA index_info('{index['name']}')\""` | — |
| [SRC-C9CF9B54F8-L000477](../../agents/omarai.py#L477) | 477 | `"                        ).fetchall()"` | — |
| [SRC-C9CF9B54F8-L000478](../../agents/omarai.py#L478) | 478 | `"                    ]"` | — |
| [SRC-C9CF9B54F8-L000479](../../agents/omarai.py#L479) | 479 | `"                    if index_columns == [\"fingerprint\"]:"` | — |
| [SRC-C9CF9B54F8-L000480](../../agents/omarai.py#L480) | 480 | `"                        unique_fingerprint = True"` | — |
| [SRC-C9CF9B54F8-L000481](../../agents/omarai.py#L481) | 481 | `"                        break"` | — |
| [SRC-C9CF9B54F8-L000482](../../agents/omarai.py#L482) | 482 | `"                if \"tenant_id\" not in columns or unique_fingerprint:"` | — |
| [SRC-C9CF9B54F8-L000483](../../agents/omarai.py#L483) | 483 | `"                    db.execute(\"ALTER TABLE leads RENAME TO leads_legacy_migration\")"` | — |
| [SRC-C9CF9B54F8-L000484](../../agents/omarai.py#L484) | 484 | `"                    self._create_leads_table(db)"` | — |
| [SRC-C9CF9B54F8-L000485](../../agents/omarai.py#L485) | 485 | `"                    legacy_columns = {"` | — |
| [SRC-C9CF9B54F8-L000486](../../agents/omarai.py#L486) | 486 | `"                        row[\"name\"]"` | — |
| [SRC-C9CF9B54F8-L000487](../../agents/omarai.py#L487) | 487 | `"                        for row in db.execute("` | — |
| [SRC-C9CF9B54F8-L000488](../../agents/omarai.py#L488) | 488 | `"                            \"PRAGMA table_info(leads_legacy_migration)\""` | — |
| [SRC-C9CF9B54F8-L000489](../../agents/omarai.py#L489) | 489 | `"                        ).fetchall()"` | — |
| [SRC-C9CF9B54F8-L000490](../../agents/omarai.py#L490) | 490 | `"                    }"` | — |
| [SRC-C9CF9B54F8-L000491](../../agents/omarai.py#L491) | 491 | `"                    tenant_expression = ("` | — |
| [SRC-C9CF9B54F8-L000492](../../agents/omarai.py#L492) | 492 | `"                        \"tenant_id\" if \"tenant_id\" in legacy_columns else \"?\""` | — |
| [SRC-C9CF9B54F8-L000493](../../agents/omarai.py#L493) | 493 | `"                    )"` | — |
| [SRC-C9CF9B54F8-L000494](../../agents/omarai.py#L494) | 494 | `"                    if tenant_expression == \"?\":"` | — |
| [SRC-C9CF9B54F8-L000495](../../agents/omarai.py#L495) | 495 | `"                        db.execute("` | — |
| [SRC-C9CF9B54F8-L000496](../../agents/omarai.py#L496) | 496 | `"                            \"\"\"INSERT OR IGNORE INTO leads"` | — |
| [SRC-C9CF9B54F8-L000497](../../agents/omarai.py#L497) | 497 | `"                                (id, tenant_id, fingerprint, text, source_url, platform,"` | — |
| [SRC-C9CF9B54F8-L000498](../../agents/omarai.py#L498) | 498 | `"                                 observed_at, assessment, status, note, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L000499](../../agents/omarai.py#L499) | 499 | `"                                SELECT id, ?, fingerprint, text, source_url, platform,"` | — |
| [SRC-C9CF9B54F8-L000500](../../agents/omarai.py#L500) | 500 | `"                                       observed_at, assessment, status, note, created_at, updated_at"` | — |
| [SRC-C9CF9B54F8-L000501](../../agents/omarai.py#L501) | 501 | `"                                FROM leads_legacy_migration\"\"\","` | — |
| [SRC-C9CF9B54F8-L000502](../../agents/omarai.py#L502) | 502 | `"                            (DEFAULT_TENANT_ID,),"` | — |
| [SRC-C9CF9B54F8-L000503](../../agents/omarai.py#L503) | 503 | `"                        )"` | — |
| [SRC-C9CF9B54F8-L000504](../../agents/omarai.py#L504) | 504 | `"                    else:"` | — |
| [SRC-C9CF9B54F8-L000505](../../agents/omarai.py#L505) | 505 | `"                        db.execute("` | — |
| [SRC-C9CF9B54F8-L000506](../../agents/omarai.py#L506) | 506 | `"                            \"\"\"INSERT OR IGNORE INTO leads"` | — |
| [SRC-C9CF9B54F8-L000507](../../agents/omarai.py#L507) | 507 | `"                                (id, tenant_id, fingerprint, text, source_url, platform,"` | — |
| [SRC-C9CF9B54F8-L000508](../../agents/omarai.py#L508) | 508 | `"                                 observed_at, assessment, status, note, created_at, updated_at)"` | — |
| [SRC-C9CF9B54F8-L000509](../../agents/omarai.py#L509) | 509 | `"                                SELECT id, tenant_id, fingerprint, text, source_url, platform,"` | — |
| [SRC-C9CF9B54F8-L000510](../../agents/omarai.py#L510) | 510 | `"                                       observed_at, assessment, status, note, created_at, updated_at"` | — |
| [SRC-C9CF9B54F8-L000511](../../agents/omarai.py#L511) | 511 | `"                                FROM leads_legacy_migration\"\"\""` | — |
| [SRC-C9CF9B54F8-L000512](../../agents/omarai.py#L512) | 512 | `"                        )"` | — |
| [SRC-C9CF9B54F8-L000513](../../agents/omarai.py#L513) | 513 | `"                    legacy_count = db.execute("` | — |
| [SRC-C9CF9B54F8-L000514](../../agents/omarai.py#L514) | 514 | `"                        \"SELECT COUNT(*) FROM leads_legacy_migration\""` | — |
| [SRC-C9CF9B54F8-L000515](../../agents/omarai.py#L515) | 515 | `"                    ).fetchone()[0]"` | — |
| [SRC-C9CF9B54F8-L000516](../../agents/omarai.py#L516) | 516 | `"                    migrated_count = db.execute("` | — |
| [SRC-C9CF9B54F8-L000517](../../agents/omarai.py#L517) | 517 | `"                        \"SELECT COUNT(*) FROM leads\""` | — |
| [SRC-C9CF9B54F8-L000518](../../agents/omarai.py#L518) | 518 | `"                    ).fetchone()[0]"` | — |
| [SRC-C9CF9B54F8-L000519](../../agents/omarai.py#L519) | 519 | `"                    missing_rows = db.execute("` | — |
| [SRC-C9CF9B54F8-L000520](../../agents/omarai.py#L520) | 520 | `"                        \"\"\"SELECT COUNT(*)"` | — |
| [SRC-C9CF9B54F8-L000521](../../agents/omarai.py#L521) | 521 | `"                           FROM leads_legacy_migration legacy"` | — |
| [SRC-C9CF9B54F8-L000522](../../agents/omarai.py#L522) | 522 | `"                           LEFT JOIN leads migrated"` | — |
| [SRC-C9CF9B54F8-L000523](../../agents/omarai.py#L523) | 523 | `"                             ON migrated.id=legacy.id"` | — |
| [SRC-C9CF9B54F8-L000524](../../agents/omarai.py#L524) | 524 | `"                            AND migrated.fingerprint=legacy.fingerprint"` | — |
| [SRC-C9CF9B54F8-L000525](../../agents/omarai.py#L525) | 525 | `"                           WHERE migrated.id IS NULL\"\"\""` | — |
| [SRC-C9CF9B54F8-L000526](../../agents/omarai.py#L526) | 526 | `"                    ).fetchone()[0]"` | — |
| [SRC-C9CF9B54F8-L000527](../../agents/omarai.py#L527) | 527 | `"                    foreign_key_errors = db.execute("` | — |
| [SRC-C9CF9B54F8-L000528](../../agents/omarai.py#L528) | 528 | `"                        \"PRAGMA foreign_key_check(leads)\""` | — |
| [SRC-C9CF9B54F8-L000529](../../agents/omarai.py#L529) | 529 | `"                    ).fetchall()"` | — |
| [SRC-C9CF9B54F8-L000530](../../agents/omarai.py#L530) | 530 | `"                    if ("` | — |
| [SRC-C9CF9B54F8-L000531](../../agents/omarai.py#L531) | 531 | `"                        migrated_count != legacy_count"` | — |
| [SRC-C9CF9B54F8-L000532](../../agents/omarai.py#L532) | 532 | `"                        or missing_rows"` | — |
| [SRC-C9CF9B54F8-L000533](../../agents/omarai.py#L533) | 533 | `"                        or foreign_key_errors"` | — |
| [SRC-C9CF9B54F8-L000534](../../agents/omarai.py#L534) | 534 | `"                    ):"` | — |
| [SRC-C9CF9B54F8-L000535](../../agents/omarai.py#L535) | 535 | `"                        raise RuntimeError("` | — |
| [SRC-C9CF9B54F8-L000536](../../agents/omarai.py#L536) | 536 | `"                            \"lead migration verification failed; legacy data was retained\""` | — |
| [SRC-C9CF9B54F8-L000537](../../agents/omarai.py#L537) | 537 | `"                        )"` | — |
| [SRC-C9CF9B54F8-L000538](../../agents/omarai.py#L538) | 538 | `"                    # Drop the old table only after count, identity, and FK checks pass."` | — |
| [SRC-C9CF9B54F8-L000539](../../agents/omarai.py#L539) | 539 | `"                    db.execute(\"DROP TABLE leads_legacy_migration\")"` | — |
| [SRC-C9CF9B54F8-L000540](../../agents/omarai.py#L540) | 540 | `"            else:"` | — |
| [SRC-C9CF9B54F8-L000541](../../agents/omarai.py#L541) | 541 | `"                self._create_leads_table(db)"` | — |
| [SRC-C9CF9B54F8-L000542](../../agents/omarai.py#L542) | 542 | `"        else:"` | — |
| [SRC-C9CF9B54F8-L000543](../../agents/omarai.py#L543) | 543 | `"            self._create_leads_table(db)"` | — |
| [SRC-C9CF9B54F8-L000544](../../agents/omarai.py#L544) | 544 | `""` | — |
| [SRC-C9CF9B54F8-L000545](../../agents/omarai.py#L545) | 545 | `"        db.execute(\"DROP INDEX IF EXISTS leads_status_idx\")"` | — |
| [SRC-C9CF9B54F8-L000546](../../agents/omarai.py#L546) | 546 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000547](../../agents/omarai.py#L547) | 547 | `"            \"CREATE INDEX IF NOT EXISTS leads_tenant_status_idx \""` | — |
| [SRC-C9CF9B54F8-L000548](../../agents/omarai.py#L548) | 548 | `"            \"ON leads(tenant_id, status, created_at DESC)\""` | — |
| [SRC-C9CF9B54F8-L000549](../../agents/omarai.py#L549) | 549 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000550](../../agents/omarai.py#L550) | 550 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000551](../../agents/omarai.py#L551) | 551 | `"            \"CREATE INDEX IF NOT EXISTS memberships_user_active_idx \""` | — |
| [SRC-C9CF9B54F8-L000552](../../agents/omarai.py#L552) | 552 | `"            \"ON tenant_memberships(user_id, active, tenant_id)\""` | — |
| [SRC-C9CF9B54F8-L000553](../../agents/omarai.py#L553) | 553 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000554](../../agents/omarai.py#L554) | 554 | `""` | — |
| [SRC-C9CF9B54F8-L000555](../../agents/omarai.py#L555) | 555 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000556](../../agents/omarai.py#L556) | 556 | `"            \"\"\"CREATE TABLE IF NOT EXISTS product_profiles ("` | — |
| [SRC-C9CF9B54F8-L000557](../../agents/omarai.py#L557) | 557 | `"                id TEXT PRIMARY KEY,"` | — |
| [SRC-C9CF9B54F8-L000558](../../agents/omarai.py#L558) | 558 | `"                tenant_id TEXT NOT NULL REFERENCES tenants(id),"` | — |
| [SRC-C9CF9B54F8-L000559](../../agents/omarai.py#L559) | 559 | `"                normalized_name TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000560](../../agents/omarai.py#L560) | 560 | `"                name TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000561](../../agents/omarai.py#L561) | 561 | `"                profile_json TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000562](../../agents/omarai.py#L562) | 562 | `"                created_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000563](../../agents/omarai.py#L563) | 563 | `"                updated_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000564](../../agents/omarai.py#L564) | 564 | `"                UNIQUE (id, tenant_id),"` | — |
| [SRC-C9CF9B54F8-L000565](../../agents/omarai.py#L565) | 565 | `"                UNIQUE (tenant_id, normalized_name)"` | — |
| [SRC-C9CF9B54F8-L000566](../../agents/omarai.py#L566) | 566 | `"            )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000567](../../agents/omarai.py#L567) | 567 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000568](../../agents/omarai.py#L568) | 568 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000569](../../agents/omarai.py#L569) | 569 | `"            \"\"\"CREATE TABLE IF NOT EXISTS discovery_runs ("` | — |
| [SRC-C9CF9B54F8-L000570](../../agents/omarai.py#L570) | 570 | `"                id TEXT PRIMARY KEY,"` | — |
| [SRC-C9CF9B54F8-L000571](../../agents/omarai.py#L571) | 571 | `"                tenant_id TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000572](../../agents/omarai.py#L572) | 572 | `"                profile_id TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000573](../../agents/omarai.py#L573) | 573 | `"                answer TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000574](../../agents/omarai.py#L574) | 574 | `"                kind TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000575](../../agents/omarai.py#L575) | 575 | `"                search_queries_json TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000576](../../agents/omarai.py#L576) | 576 | `"                search_report_json TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000577](../../agents/omarai.py#L577) | 577 | `"                sources_json TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000578](../../agents/omarai.py#L578) | 578 | `"                created_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000579](../../agents/omarai.py#L579) | 579 | `"                FOREIGN KEY (profile_id, tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000580](../../agents/omarai.py#L580) | 580 | `"                    REFERENCES product_profiles(id, tenant_id)"` | — |
| [SRC-C9CF9B54F8-L000581](../../agents/omarai.py#L581) | 581 | `"            )\"\"\""` | — |
| [SRC-C9CF9B54F8-L000582](../../agents/omarai.py#L582) | 582 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000583](../../agents/omarai.py#L583) | 583 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000584](../../agents/omarai.py#L584) | 584 | `"            \"CREATE INDEX IF NOT EXISTS product_profiles_tenant_updated_idx \""` | — |
| [SRC-C9CF9B54F8-L000585](../../agents/omarai.py#L585) | 585 | `"            \"ON product_profiles(tenant_id, updated_at DESC)\""` | — |
| [SRC-C9CF9B54F8-L000586](../../agents/omarai.py#L586) | 586 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000587](../../agents/omarai.py#L587) | 587 | `"        db.execute("` | — |
| [SRC-C9CF9B54F8-L000588](../../agents/omarai.py#L588) | 588 | `"            \"CREATE INDEX IF NOT EXISTS discovery_runs_tenant_created_idx \""` | — |
| [SRC-C9CF9B54F8-L000589](../../agents/omarai.py#L589) | 589 | `"            \"ON discovery_runs(tenant_id, created_at DESC)\""` | — |
| [SRC-C9CF9B54F8-L000590](../../agents/omarai.py#L590) | 590 | `"        )"` | — |
| [SRC-C9CF9B54F8-L000591](../../agents/omarai.py#L591) | 591 | `""` | — |
| [SRC-C9CF9B54F8-L000592](../../agents/omarai.py#L592) | 592 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000593](../../agents/omarai.py#L593) | 593 | `"    def _tenant(tenant_id: str \| None) -> str:"` | — |
| [SRC-C9CF9B54F8-L000594](../../agents/omarai.py#L594) | 594 | `"        value = DEFAULT_TENANT_ID if tenant_id is None else str(tenant_id).strip()"` | — |
| [SRC-C9CF9B54F8-L000595](../../agents/omarai.py#L595) | 595 | `"        if not value or len(value) > 128:"` | — |
| [SRC-C9CF9B54F8-L000596](../../agents/omarai.py#L596) | 596 | `"            raise ValueError(\"tenant_id is invalid\")"` | — |
| [SRC-C9CF9B54F8-L000597](../../agents/omarai.py#L597) | 597 | `"        return value"` | — |
| [SRC-C9CF9B54F8-L000598](../../agents/omarai.py#L598) | 598 | `""` | — |
| [SRC-C9CF9B54F8-L000599](../../agents/omarai.py#L599) | 599 | `"    def default_principal(self) -> dict:"` | — |
