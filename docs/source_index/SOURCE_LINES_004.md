# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **004**
- سجلات الأسطر: **800**
- النطاق: SRC-5587371288-L000457 إلى SRC-59CF4B7DE8-L000417
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-5587371288 — [agents/intent_router.py](../../agents/intent_router.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-5587371288-L000457](../../agents/intent_router.py#L457) | 457 | `"            \"route\": \"LOCAL\","` | — |
| [SRC-5587371288-L000458](../../agents/intent_router.py#L458) | 458 | `"            \"reason\": \"capability_question\","` | — |
| [SRC-5587371288-L000459](../../agents/intent_router.py#L459) | 459 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000460](../../agents/intent_router.py#L460) | 460 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000461](../../agents/intent_router.py#L461) | 461 | `"        }"` | — |
| [SRC-5587371288-L000462](../../agents/intent_router.py#L462) | 462 | `""` | — |
| [SRC-5587371288-L000463](../../agents/intent_router.py#L463) | 463 | `"    if _is_smalltalk(question):"` | — |
| [SRC-5587371288-L000464](../../agents/intent_router.py#L464) | 464 | `"        return {"` | — |
| [SRC-5587371288-L000465](../../agents/intent_router.py#L465) | 465 | `"            \"route\": \"LOCAL\","` | — |
| [SRC-5587371288-L000466](../../agents/intent_router.py#L466) | 466 | `"            \"reason\": \"short_conversational_turn\","` | — |
| [SRC-5587371288-L000467](../../agents/intent_router.py#L467) | 467 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000468](../../agents/intent_router.py#L468) | 468 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000469](../../agents/intent_router.py#L469) | 469 | `"        }"` | — |
| [SRC-5587371288-L000470](../../agents/intent_router.py#L470) | 470 | `""` | — |
| [SRC-5587371288-L000471](../../agents/intent_router.py#L471) | 471 | `"    # A page/link summary needs a concrete source. Pasted text is handled locally;"` | — |
| [SRC-5587371288-L000472](../../agents/intent_router.py#L472) | 472 | `"    # an absent source must trigger clarification rather than a search for \"the page\"."` | — |
| [SRC-5587371288-L000473](../../agents/intent_router.py#L473) | 473 | `"    if _is_page_summarization_request(question):"` | — |
| [SRC-5587371288-L000474](../../agents/intent_router.py#L474) | 474 | `"        if _has_inline_summary_text(question):"` | — |
| [SRC-5587371288-L000475](../../agents/intent_router.py#L475) | 475 | `"            return {"` | — |
| [SRC-5587371288-L000476](../../agents/intent_router.py#L476) | 476 | `"                \"route\": \"MODEL_ONLY\","` | — |
| [SRC-5587371288-L000477](../../agents/intent_router.py#L477) | 477 | `"                \"reason\": \"summarization_text_provided\","` | — |
| [SRC-5587371288-L000478](../../agents/intent_router.py#L478) | 478 | `"                \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000479](../../agents/intent_router.py#L479) | 479 | `"                \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000480](../../agents/intent_router.py#L480) | 480 | `"            }"` | — |
| [SRC-5587371288-L000481](../../agents/intent_router.py#L481) | 481 | `"        if re.search(r\"https?://\", question, flags=re.IGNORECASE):"` | — |
| [SRC-5587371288-L000482](../../agents/intent_router.py#L482) | 482 | `"            return {"` | — |
| [SRC-5587371288-L000483](../../agents/intent_router.py#L483) | 483 | `"                \"route\": \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000484](../../agents/intent_router.py#L484) | 484 | `"                \"reason\": \"summarization_request\","` | — |
| [SRC-5587371288-L000485](../../agents/intent_router.py#L485) | 485 | `"                \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000486](../../agents/intent_router.py#L486) | 486 | `"                \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000487](../../agents/intent_router.py#L487) | 487 | `"            }"` | — |
| [SRC-5587371288-L000488](../../agents/intent_router.py#L488) | 488 | `"        return {"` | — |
| [SRC-5587371288-L000489](../../agents/intent_router.py#L489) | 489 | `"            \"route\": \"CLARIFY\","` | — |
| [SRC-5587371288-L000490](../../agents/intent_router.py#L490) | 490 | `"            \"reason\": \"missing_summarization_input\","` | — |
| [SRC-5587371288-L000491](../../agents/intent_router.py#L491) | 491 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000492](../../agents/intent_router.py#L492) | 492 | `"            \"needs_clarification\": True,"` | — |
| [SRC-5587371288-L000493](../../agents/intent_router.py#L493) | 493 | `"        }"` | — |
| [SRC-5587371288-L000494](../../agents/intent_router.py#L494) | 494 | `""` | — |
| [SRC-5587371288-L000495](../../agents/intent_router.py#L495) | 495 | `"    ambiguous = _is_contextual_followup(question) or _needs_clarification(question)"` | — |
| [SRC-5587371288-L000496](../../agents/intent_router.py#L496) | 496 | `"    if ambiguous:"` | — |
| [SRC-5587371288-L000497](../../agents/intent_router.py#L497) | 497 | `"        return {"` | — |
| [SRC-5587371288-L000498](../../agents/intent_router.py#L498) | 498 | `"            \"route\": \"WEB_DEEP\" if _is_deep(question) else \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000499](../../agents/intent_router.py#L499) | 499 | `"            \"reason\": \"ambiguous_followup_with_context\","` | — |
| [SRC-5587371288-L000500](../../agents/intent_router.py#L500) | 500 | `"            \"context_available\": True,"` | — |
| [SRC-5587371288-L000501](../../agents/intent_router.py#L501) | 501 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000502](../../agents/intent_router.py#L502) | 502 | `"        }"` | — |
| [SRC-5587371288-L000503](../../agents/intent_router.py#L503) | 503 | `""` | — |
| [SRC-5587371288-L000504](../../agents/intent_router.py#L504) | 504 | `"    if _is_lead_generation_request(question):"` | — |
| [SRC-5587371288-L000505](../../agents/intent_router.py#L505) | 505 | `"        return {"` | — |
| [SRC-5587371288-L000506](../../agents/intent_router.py#L506) | 506 | `"            \"route\": \"LEAD_GENERATION\","` | — |
| [SRC-5587371288-L000507](../../agents/intent_router.py#L507) | 507 | `"            \"reason\": \"explicit_prospect_or_buyer_discovery_request\","` | — |
| [SRC-5587371288-L000508](../../agents/intent_router.py#L508) | 508 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000509](../../agents/intent_router.py#L509) | 509 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000510](../../agents/intent_router.py#L510) | 510 | `"        }"` | — |
| [SRC-5587371288-L000511](../../agents/intent_router.py#L511) | 511 | `""` | — |
| [SRC-5587371288-L000512](../../agents/intent_router.py#L512) | 512 | `"    if _is_deep(question):"` | — |
| [SRC-5587371288-L000513](../../agents/intent_router.py#L513) | 513 | `"        return {"` | — |
| [SRC-5587371288-L000514](../../agents/intent_router.py#L514) | 514 | `"            \"route\": \"WEB_DEEP\","` | — |
| [SRC-5587371288-L000515](../../agents/intent_router.py#L515) | 515 | `"            \"reason\": \"comparison_or_multi_part_research\","` | — |
| [SRC-5587371288-L000516](../../agents/intent_router.py#L516) | 516 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000517](../../agents/intent_router.py#L517) | 517 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000518](../../agents/intent_router.py#L518) | 518 | `"        }"` | — |
| [SRC-5587371288-L000519](../../agents/intent_router.py#L519) | 519 | `""` | — |
| [SRC-5587371288-L000520](../../agents/intent_router.py#L520) | 520 | `"    if requires_web or _has_live_signal(question) or _has_explicit_source_request(question):"` | — |
| [SRC-5587371288-L000521](../../agents/intent_router.py#L521) | 521 | `"        return {"` | — |
| [SRC-5587371288-L000522](../../agents/intent_router.py#L522) | 522 | `"            \"route\": \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000523](../../agents/intent_router.py#L523) | 523 | `"            \"reason\": ("` | — |
| [SRC-5587371288-L000524](../../agents/intent_router.py#L524) | 524 | `"                \"explicit_evidence_request\""` | — |
| [SRC-5587371288-L000525](../../agents/intent_router.py#L525) | 525 | `"                if _has_explicit_source_request(question)"` | — |
| [SRC-5587371288-L000526](../../agents/intent_router.py#L526) | 526 | `"                else \"freshness_or_explicit_research_signal\""` | — |
| [SRC-5587371288-L000527](../../agents/intent_router.py#L527) | 527 | `"            ),"` | — |
| [SRC-5587371288-L000528](../../agents/intent_router.py#L528) | 528 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000529](../../agents/intent_router.py#L529) | 529 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000530](../../agents/intent_router.py#L530) | 530 | `"        }"` | — |
| [SRC-5587371288-L000531](../../agents/intent_router.py#L531) | 531 | `""` | — |
| [SRC-5587371288-L000532](../../agents/intent_router.py#L532) | 532 | `"    return {"` | — |
| [SRC-5587371288-L000533](../../agents/intent_router.py#L533) | 533 | `"        \"route\": \"MODEL_ONLY\","` | — |
| [SRC-5587371288-L000534](../../agents/intent_router.py#L534) | 534 | `"        \"reason\": \"stable_knowledge_or_conversation\","` | — |
| [SRC-5587371288-L000535](../../agents/intent_router.py#L535) | 535 | `"        \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000536](../../agents/intent_router.py#L536) | 536 | `"        \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000537](../../agents/intent_router.py#L537) | 537 | `"    }"` | — |
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
| [SRC-C9CF9B54F8-L000006](../../agents/omarai.py#L6) | 6 | `"import json"` | — |
| [SRC-C9CF9B54F8-L000007](../../agents/omarai.py#L7) | 7 | `"import re"` | — |
| [SRC-C9CF9B54F8-L000008](../../agents/omarai.py#L8) | 8 | `"import sqlite3"` | — |
| [SRC-C9CF9B54F8-L000009](../../agents/omarai.py#L9) | 9 | `"import unicodedata"` | — |
| [SRC-C9CF9B54F8-L000010](../../agents/omarai.py#L10) | 10 | `"from datetime import UTC, datetime"` | — |
| [SRC-C9CF9B54F8-L000011](../../agents/omarai.py#L11) | 11 | `"from pathlib import Path"` | — |
| [SRC-C9CF9B54F8-L000012](../../agents/omarai.py#L12) | 12 | `"from urllib.parse import urlparse"` | — |
| [SRC-C9CF9B54F8-L000013](../../agents/omarai.py#L13) | 13 | `""` | — |
| [SRC-C9CF9B54F8-L000014](../../agents/omarai.py#L14) | 14 | `"MAX_TEXT = 12000"` | — |
| [SRC-C9CF9B54F8-L000015](../../agents/omarai.py#L15) | 15 | `"_TRANSLATION = str.maketrans({\"أ\":\"ا\",\"إ\":\"ا\",\"آ\":\"ا\",\"ٱ\":\"ا\",\"ى\":\"ي\",\"ئ\":\"ي\",\"ؤ\":\"و\",\"ـ\":\"\"})"` | — |
| [SRC-C9CF9B54F8-L000016](../../agents/omarai.py#L16) | 16 | `"SIGNALS = {"` | — |
| [SRC-C9CF9B54F8-L000017](../../agents/omarai.py#L17) | 17 | `"    \"high\": (35, (\"عايز اشتري\", \"عاوز اشتري\", \"بدور على شقة\", \"بدور على عقار\", \"مطلوب شقة\", \"عايز وحدة\", \"محتاج اشتري\")),"` | — |
| [SRC-C9CF9B54F8-L000018](../../agents/omarai.py#L18) | 18 | `"    \"next_step\": (20, (\"ممكن معاينة\", \"عايز اعاين\", \"عاوز اعاين\", \"ابعت التفاصيل\", \"ابعت اللوكيشن\", \"ميعاد للمعاينة\")),"` | — |
| [SRC-C9CF9B54F8-L000019](../../agents/omarai.py#L19) | 19 | `"    \"budget\": (15, (\"السعر كام\", \"مقدم كام\", \"ميزانيتي\", \"معايا مقدم\", \"تقسيط\", \"على اقساط\", \"في حدود\")),"` | — |
| [SRC-C9CF9B54F8-L000020](../../agents/omarai.py#L20) | 20 | `"    \"explore\": (10, (\"بدور على\", \"فيه شقق\", \"ايه المتاح\", \"عايز اعرف الاسعار\")),"` | — |
| [SRC-C9CF9B54F8-L000021](../../agents/omarai.py#L21) | 21 | `"}"` | — |
| [SRC-C9CF9B54F8-L000022](../../agents/omarai.py#L22) | 22 | `"NOT_BUYER = (\"مش عايز اشتري\", \"مش عاوز اشتري\", \"عايز ابيع\", \"عاوز ابيع\", \"عندي شقة للبيع\", \"انا وسيط\", \"انا سمسار\", \"عايز ايجار\", \"للايجار\")"` | — |
| [SRC-C9CF9B54F8-L000023](../../agents/omarai.py#L23) | 23 | `""` | — |
| [SRC-C9CF9B54F8-L000024](../../agents/omarai.py#L24) | 24 | `"def normalize(text: str) -> str:"` | — |
| [SRC-C9CF9B54F8-L000025](../../agents/omarai.py#L25) | 25 | `"    value = unicodedata.normalize(\"NFKC\", str(text)).translate(_TRANSLATION)"` | — |
| [SRC-C9CF9B54F8-L000026](../../agents/omarai.py#L26) | 26 | `"    value = \"\".join(c for c in value if not unicodedata.category(c).startswith(\"M\"))"` | — |
| [SRC-C9CF9B54F8-L000027](../../agents/omarai.py#L27) | 27 | `"    return re.sub(r\"\\s+\", \" \", re.sub(r\"[^\\w\\s]\", \" \", value.casefold())).strip()"` | — |
| [SRC-C9CF9B54F8-L000028](../../agents/omarai.py#L28) | 28 | `""` | — |
| [SRC-C9CF9B54F8-L000029](../../agents/omarai.py#L29) | 29 | `"def now_utc() -> str:"` | — |
| [SRC-C9CF9B54F8-L000030](../../agents/omarai.py#L30) | 30 | `"    return datetime.now(UTC).isoformat(timespec=\"seconds\").replace(\"+00:00\", \"Z\")"` | — |
| [SRC-C9CF9B54F8-L000031](../../agents/omarai.py#L31) | 31 | `""` | — |
| [SRC-C9CF9B54F8-L000032](../../agents/omarai.py#L32) | 32 | `"def _csv_safe_cell(value: object) -> str:"` | — |
| [SRC-C9CF9B54F8-L000033](../../agents/omarai.py#L33) | 33 | `"    \"\"\"Prefix spreadsheet formulas even when hidden whitespace/control chars precede them.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000034](../../agents/omarai.py#L34) | 34 | `"    text = \"\" if value is None else str(value)"` | — |
| [SRC-C9CF9B54F8-L000035](../../agents/omarai.py#L35) | 35 | `"    if not text:"` | — |
| [SRC-C9CF9B54F8-L000036](../../agents/omarai.py#L36) | 36 | `"        return text"` | — |
| [SRC-C9CF9B54F8-L000037](../../agents/omarai.py#L37) | 37 | `"    index = 0"` | — |
| [SRC-C9CF9B54F8-L000038](../../agents/omarai.py#L38) | 38 | `"    while index < len(text) and ("` | — |
| [SRC-C9CF9B54F8-L000039](../../agents/omarai.py#L39) | 39 | `"        text[index].isspace()"` | — |
| [SRC-C9CF9B54F8-L000040](../../agents/omarai.py#L40) | 40 | `"        or unicodedata.category(text[index]) in {\"Cc\", \"Cf\"}"` | — |
| [SRC-C9CF9B54F8-L000041](../../agents/omarai.py#L41) | 41 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000042](../../agents/omarai.py#L42) | 42 | `"        index += 1"` | — |
| [SRC-C9CF9B54F8-L000043](../../agents/omarai.py#L43) | 43 | `"    first_non_format = text[index:index + 1]"` | — |
| [SRC-C9CF9B54F8-L000044](../../agents/omarai.py#L44) | 44 | `"    formula_prefixes = {\"=\", \"+\", \"-\", \"@\", \"＝\", \"＋\", \"－\", \"＠\"}"` | — |
| [SRC-C9CF9B54F8-L000045](../../agents/omarai.py#L45) | 45 | `"    if text[0] in \"\\t\\r\\n\" or first_non_format in formula_prefixes:"` | — |
| [SRC-C9CF9B54F8-L000046](../../agents/omarai.py#L46) | 46 | `"        # OWASP notes that a tab inside the quoted CSV field is more resilient"` | — |
| [SRC-C9CF9B54F8-L000047](../../agents/omarai.py#L47) | 47 | `"        # in Excel than an apostrophe, although no CSV mitigation is universal."` | — |
| [SRC-C9CF9B54F8-L000048](../../agents/omarai.py#L48) | 48 | `"        return \"\\t\" + text"` | — |
| [SRC-C9CF9B54F8-L000049](../../agents/omarai.py#L49) | 49 | `"    return text"` | — |
| [SRC-C9CF9B54F8-L000050](../../agents/omarai.py#L50) | 50 | `""` | — |
| [SRC-C9CF9B54F8-L000051](../../agents/omarai.py#L51) | 51 | `"def analyze(text: str, product_terms=(), location_terms=()) -> dict:"` | — |
| [SRC-C9CF9B54F8-L000052](../../agents/omarai.py#L52) | 52 | `"    if not isinstance(text, str) or not text.strip():"` | — |
| [SRC-C9CF9B54F8-L000053](../../agents/omarai.py#L53) | 53 | `"        raise ValueError(\"text must not be empty\")"` | — |
| [SRC-C9CF9B54F8-L000054](../../agents/omarai.py#L54) | 54 | `"    if len(text) > MAX_TEXT:"` | — |
| [SRC-C9CF9B54F8-L000055](../../agents/omarai.py#L55) | 55 | `"        raise ValueError(f\"text must be at most {MAX_TEXT} characters\")"` | — |
| [SRC-C9CF9B54F8-L000056](../../agents/omarai.py#L56) | 56 | `"    body = normalize(text)"` | — |
| [SRC-C9CF9B54F8-L000057](../../agents/omarai.py#L57) | 57 | `"    excluded = [p for p in NOT_BUYER if normalize(p) in body]"` | — |
| [SRC-C9CF9B54F8-L000058](../../agents/omarai.py#L58) | 58 | `"    if excluded:"` | — |
| [SRC-C9CF9B54F8-L000059](../../agents/omarai.py#L59) | 59 | `"        return {\"score\": 0, \"label\": \"not_buyer_signal\", \"summary\": \"قد لا تكون إشارة شراء مباشرة؛ راجع النص يدويًا.\", \"matched_signals\": [{\"phrase\": p, \"category\": \"exclusion\", \"points\": 0} for p in excluded], \"warnings\": [\"تصنيف أولي وليس حكمًا نهائيًا.\"]}"` | — |
| [SRC-C9CF9B54F8-L000060](../../agents/omarai.py#L60) | 60 | `"    matches = []"` | — |
| [SRC-C9CF9B54F8-L000061](../../agents/omarai.py#L61) | 61 | `"    for category, (points, phrases) in SIGNALS.items():"` | — |
| [SRC-C9CF9B54F8-L000062](../../agents/omarai.py#L62) | 62 | `"        found = next((p for p in phrases if normalize(p) in body), None)"` | — |
| [SRC-C9CF9B54F8-L000063](../../agents/omarai.py#L63) | 63 | `"        if found:"` | — |
| [SRC-C9CF9B54F8-L000064](../../agents/omarai.py#L64) | 64 | `"            matches.append({\"phrase\": found, \"category\": category, \"points\": points})"` | — |
| [SRC-C9CF9B54F8-L000065](../../agents/omarai.py#L65) | 65 | `"    for category, terms in ((\"product_context\", product_terms), (\"location_context\", location_terms)):"` | — |
| [SRC-C9CF9B54F8-L000066](../../agents/omarai.py#L66) | 66 | `"        found = next((normalize(t) for t in terms if isinstance(t, str) and normalize(t) and normalize(t) in body), None)"` | — |
| [SRC-C9CF9B54F8-L000067](../../agents/omarai.py#L67) | 67 | `"        if found:"` | — |
| [SRC-C9CF9B54F8-L000068](../../agents/omarai.py#L68) | 68 | `"            matches.append({\"phrase\": found, \"category\": category, \"points\": 10})"` | — |
| [SRC-C9CF9B54F8-L000069](../../agents/omarai.py#L69) | 69 | `"    score = min(100, sum(x[\"points\"] for x in matches))"` | — |
| [SRC-C9CF9B54F8-L000070](../../agents/omarai.py#L70) | 70 | `"    label = \"high_intent\" if score >= 55 and any(x[\"category\"] == \"high\" for x in matches) else \"medium_intent\" if score >= 40 else \"early_research\" if score >= 20 else \"unclear\""` | — |
| [SRC-C9CF9B54F8-L000071](../../agents/omarai.py#L71) | 71 | `"    return {\"score\": score, \"label\": label, \"summary\": {\"high_intent\":\"إشارة قوية نسبيًا وفق قواعد بسيطة وتحتاج مراجعة بشرية.\",\"medium_intent\":\"مؤشرات اهتمام تستحق التأهيل والتحقق.\",\"early_research\":\"اهتمام مبكر؛ ليس عميلًا مؤهلًا بعد.\",\"unclear\":\"لا توجد مؤشرات كافية.\"}[label], \"matched_signals\": matches, \"warnings\": [\"الدرجة ليست احتمالًا إحصائيًا للشراء.\", \"لا تثبت هوية الكاتب أو قدرته على الدفع أو نيته.\", \"استخدم مصادر عامة ومسموحًا بمعالجتها فقط.\"]}"` | — |
| [SRC-C9CF9B54F8-L000072](../../agents/omarai.py#L72) | 72 | `""` | — |
| [SRC-C9CF9B54F8-L000073](../../agents/omarai.py#L73) | 73 | `"def validate_url(url: str) -> str:"` | — |
| [SRC-C9CF9B54F8-L000074](../../agents/omarai.py#L74) | 74 | `"    parsed = urlparse(str(url or \"\").strip())"` | — |
| [SRC-C9CF9B54F8-L000075](../../agents/omarai.py#L75) | 75 | `"    if parsed.scheme not in (\"http\", \"https\") or not parsed.netloc or parsed.username or parsed.password:"` | — |
| [SRC-C9CF9B54F8-L000076](../../agents/omarai.py#L76) | 76 | `"        raise ValueError(\"source_url must be an absolute http(s) URL without embedded credentials\")"` | — |
| [SRC-C9CF9B54F8-L000077](../../agents/omarai.py#L77) | 77 | `"    if len(url) > 2048:"` | — |
| [SRC-C9CF9B54F8-L000078](../../agents/omarai.py#L78) | 78 | `"        raise ValueError(\"source_url is too long\")"` | — |
| [SRC-C9CF9B54F8-L000079](../../agents/omarai.py#L79) | 79 | `"    return url.strip()"` | — |
| [SRC-C9CF9B54F8-L000080](../../agents/omarai.py#L80) | 80 | `""` | — |
| [SRC-C9CF9B54F8-L000081](../../agents/omarai.py#L81) | 81 | `"class LeadStore:"` | — |
| [SRC-C9CF9B54F8-L000082](../../agents/omarai.py#L82) | 82 | `"    def __init__(self, path: str \| Path \| None = None):"` | — |
| [SRC-C9CF9B54F8-L000083](../../agents/omarai.py#L83) | 83 | `"        self.path = Path(path or Path.home()/\".omarai\"/\"omarai.sqlite3\").expanduser()"` | — |
| [SRC-C9CF9B54F8-L000084](../../agents/omarai.py#L84) | 84 | `"        self.path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-C9CF9B54F8-L000085](../../agents/omarai.py#L85) | 85 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000086](../../agents/omarai.py#L86) | 86 | `"            db.execute(\"\"\"CREATE TABLE IF NOT EXISTS leads ("` | — |
| [SRC-C9CF9B54F8-L000087](../../agents/omarai.py#L87) | 87 | `"            id TEXT PRIMARY KEY, fingerprint TEXT UNIQUE NOT NULL, text TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000088](../../agents/omarai.py#L88) | 88 | `"            source_url TEXT NOT NULL, platform TEXT NOT NULL, observed_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000089](../../agents/omarai.py#L89) | 89 | `"            assessment TEXT NOT NULL, status TEXT NOT NULL, note TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000090](../../agents/omarai.py#L90) | 90 | `"            created_at TEXT NOT NULL, updated_at TEXT NOT NULL)\"\"\")"` | — |
| [SRC-C9CF9B54F8-L000091](../../agents/omarai.py#L91) | 91 | `"            db.execute(\"CREATE INDEX IF NOT EXISTS leads_status_idx ON leads(status, created_at DESC)\")"` | — |
| [SRC-C9CF9B54F8-L000092](../../agents/omarai.py#L92) | 92 | `"    def connect(self):"` | — |
| [SRC-C9CF9B54F8-L000093](../../agents/omarai.py#L93) | 93 | `"        db = sqlite3.connect(self.path, timeout=10)"` | — |
| [SRC-C9CF9B54F8-L000094](../../agents/omarai.py#L94) | 94 | `"        db.row_factory = sqlite3.Row"` | — |
| [SRC-C9CF9B54F8-L000095](../../agents/omarai.py#L95) | 95 | `"        return db"` | — |
| [SRC-C9CF9B54F8-L000096](../../agents/omarai.py#L96) | 96 | `"    def add(self, text: str, source_url: str, platform: str=\"manual\", observed_at: str \| None=None, note: str=\"\", product_terms=(), location_terms=()):"` | — |
| [SRC-C9CF9B54F8-L000097](../../agents/omarai.py#L97) | 97 | `"        if not isinstance(text, str) or not text.strip():"` | — |
| [SRC-C9CF9B54F8-L000098](../../agents/omarai.py#L98) | 98 | `"            raise ValueError(\"text is required\")"` | — |
| [SRC-C9CF9B54F8-L000099](../../agents/omarai.py#L99) | 99 | `"        if len(text) > MAX_TEXT:"` | — |
| [SRC-C9CF9B54F8-L000100](../../agents/omarai.py#L100) | 100 | `"            raise ValueError(\"text is too long\")"` | — |
| [SRC-C9CF9B54F8-L000101](../../agents/omarai.py#L101) | 101 | `"        url = validate_url(source_url)"` | — |
| [SRC-C9CF9B54F8-L000102](../../agents/omarai.py#L102) | 102 | `"        normalized = normalize(text)"` | — |
| [SRC-C9CF9B54F8-L000103](../../agents/omarai.py#L103) | 103 | `"        fingerprint = hashlib.sha256((url.rstrip(\"/\") + \"\\n\" + normalized).encode()).hexdigest()"` | — |
| [SRC-C9CF9B54F8-L000104](../../agents/omarai.py#L104) | 104 | `"        lead_id = fingerprint[:24]"` | — |
| [SRC-C9CF9B54F8-L000105](../../agents/omarai.py#L105) | 105 | `"        timestamp = observed_at or now_utc()"` | — |
| [SRC-C9CF9B54F8-L000106](../../agents/omarai.py#L106) | 106 | `"        assessment = analyze(text, product_terms=product_terms, location_terms=location_terms)"` | — |
| [SRC-C9CF9B54F8-L000107](../../agents/omarai.py#L107) | 107 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L000108](../../agents/omarai.py#L108) | 108 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000109](../../agents/omarai.py#L109) | 109 | `"            cursor = db.execute(\"\"\"INSERT OR IGNORE INTO leads"` | — |
| [SRC-C9CF9B54F8-L000110](../../agents/omarai.py#L110) | 110 | `"            (id,fingerprint,text,source_url,platform,observed_at,assessment,status,note,created_at,updated_at)"` | — |
| [SRC-C9CF9B54F8-L000111](../../agents/omarai.py#L111) | 111 | `"            VALUES(?,?,?,?,?,?,?,?,?,?,?)\"\"\", (lead_id,fingerprint,text.strip(),url,str(platform)[:80],timestamp,json.dumps(assessment,ensure_ascii=False),\"new\",str(note)[:1000],now,now))"` | — |
| [SRC-C9CF9B54F8-L000112](../../agents/omarai.py#L112) | 112 | `"            row = db.execute(\"SELECT * FROM leads WHERE id=?\", (lead_id,)).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000113](../../agents/omarai.py#L113) | 113 | `"        return self.to_dict(row), cursor.rowcount == 1"` | — |
| [SRC-C9CF9B54F8-L000114](../../agents/omarai.py#L114) | 114 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000115](../../agents/omarai.py#L115) | 115 | `"    def to_dict(row):"` | — |
| [SRC-C9CF9B54F8-L000116](../../agents/omarai.py#L116) | 116 | `"        item = dict(row)"` | — |
| [SRC-C9CF9B54F8-L000117](../../agents/omarai.py#L117) | 117 | `"        item[\"assessment\"] = json.loads(item[\"assessment\"])"` | — |
| [SRC-C9CF9B54F8-L000118](../../agents/omarai.py#L118) | 118 | `"        return item"` | — |
| [SRC-C9CF9B54F8-L000119](../../agents/omarai.py#L119) | 119 | `"    def list(self, status: str \| None=None, limit: int=100):"` | — |
| [SRC-C9CF9B54F8-L000120](../../agents/omarai.py#L120) | 120 | `"        limit = max(1,min(int(limit),500))"` | — |
| [SRC-C9CF9B54F8-L000121](../../agents/omarai.py#L121) | 121 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000122](../../agents/omarai.py#L122) | 122 | `"            rows = db.execute(\"SELECT * FROM leads WHERE (? IS NULL OR status=?) ORDER BY created_at DESC LIMIT ?\",(status,status,limit)).fetchall()"` | — |
| [SRC-C9CF9B54F8-L000123](../../agents/omarai.py#L123) | 123 | `"        return [self.to_dict(r) for r in rows]"` | — |
| [SRC-C9CF9B54F8-L000124](../../agents/omarai.py#L124) | 124 | `"    def update_status(self, lead_id: str, status: str):"` | — |
| [SRC-C9CF9B54F8-L000125](../../agents/omarai.py#L125) | 125 | `"        allowed={\"new\",\"qualified\",\"contacted\",\"converted\",\"rejected\",\"needs_review\"}"` | — |
| [SRC-C9CF9B54F8-L000126](../../agents/omarai.py#L126) | 126 | `"        if status not in allowed:"` | — |
| [SRC-C9CF9B54F8-L000127](../../agents/omarai.py#L127) | 127 | `"            raise ValueError(\"unsupported status\")"` | — |
| [SRC-C9CF9B54F8-L000128](../../agents/omarai.py#L128) | 128 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000129](../../agents/omarai.py#L129) | 129 | `"            db.execute(\"UPDATE leads SET status=?,updated_at=? WHERE id=?\",(status,now_utc(),lead_id))"` | — |
| [SRC-C9CF9B54F8-L000130](../../agents/omarai.py#L130) | 130 | `"            row=db.execute(\"SELECT * FROM leads WHERE id=?\",(lead_id,)).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000131](../../agents/omarai.py#L131) | 131 | `"        return self.to_dict(row) if row else None"` | — |
| [SRC-C9CF9B54F8-L000132](../../agents/omarai.py#L132) | 132 | `"    def import_csv(self, filename: str):"` | — |
| [SRC-C9CF9B54F8-L000133](../../agents/omarai.py#L133) | 133 | `"        results={\"created\":0,\"duplicates\":0,\"errors\":[]}"` | — |
| [SRC-C9CF9B54F8-L000134](../../agents/omarai.py#L134) | 134 | `"        with open(filename, newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-C9CF9B54F8-L000135](../../agents/omarai.py#L135) | 135 | `"            reader=csv.DictReader(stream)"` | — |
| [SRC-C9CF9B54F8-L000136](../../agents/omarai.py#L136) | 136 | `"            required={\"text\",\"source_url\",\"platform\"}"` | — |
| [SRC-C9CF9B54F8-L000137](../../agents/omarai.py#L137) | 137 | `"            if not reader.fieldnames or not required.issubset(reader.fieldnames):"` | — |
| [SRC-C9CF9B54F8-L000138](../../agents/omarai.py#L138) | 138 | `"                raise ValueError(\"CSV must contain text,source_url,platform columns\")"` | — |
| [SRC-C9CF9B54F8-L000139](../../agents/omarai.py#L139) | 139 | `"            for line,row in enumerate(reader,2):"` | — |
| [SRC-C9CF9B54F8-L000140](../../agents/omarai.py#L140) | 140 | `"                try:"` | — |
| [SRC-C9CF9B54F8-L000141](../../agents/omarai.py#L141) | 141 | `"                    _,created=self.add(row[\"text\"],row[\"source_url\"],row[\"platform\"],row.get(\"observed_at\") or None,row.get(\"note\") or \"\")"` | — |
| [SRC-C9CF9B54F8-L000142](../../agents/omarai.py#L142) | 142 | `"                    results[\"created\" if created else \"duplicates\"] += 1"` | — |
| [SRC-C9CF9B54F8-L000143](../../agents/omarai.py#L143) | 143 | `"                except (ValueError, TypeError) as exc:"` | — |
| [SRC-C9CF9B54F8-L000144](../../agents/omarai.py#L144) | 144 | `"                    results[\"errors\"].append({\"line\":line,\"error\":str(exc)})"` | — |
| [SRC-C9CF9B54F8-L000145](../../agents/omarai.py#L145) | 145 | `"        return results"` | — |
| [SRC-C9CF9B54F8-L000146](../../agents/omarai.py#L146) | 146 | `"    def export_csv(self, filename: str):"` | — |
| [SRC-C9CF9B54F8-L000147](../../agents/omarai.py#L147) | 147 | `"        rows=self.list(limit=500)"` | — |
| [SRC-C9CF9B54F8-L000148](../../agents/omarai.py#L148) | 148 | `"        with open(filename,\"w\",newline=\"\",encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-C9CF9B54F8-L000149](../../agents/omarai.py#L149) | 149 | `"            fields=[\"id\",\"text\",\"source_url\",\"platform\",\"observed_at\",\"assessment\",\"status\",\"note\",\"created_at\"]"` | — |
| [SRC-C9CF9B54F8-L000150](../../agents/omarai.py#L150) | 150 | `"            writer=csv.DictWriter(stream, fieldnames=fields, quoting=csv.QUOTE_ALL)"` | — |
| [SRC-C9CF9B54F8-L000151](../../agents/omarai.py#L151) | 151 | `"            writer.writeheader()"` | — |
| [SRC-C9CF9B54F8-L000152](../../agents/omarai.py#L152) | 152 | `"            for row in rows:"` | — |
| [SRC-C9CF9B54F8-L000153](../../agents/omarai.py#L153) | 153 | `"                values = {"` | — |
| [SRC-C9CF9B54F8-L000154](../../agents/omarai.py#L154) | 154 | `"                    key: json.dumps(row[key], ensure_ascii=False)"` | — |
| [SRC-C9CF9B54F8-L000155](../../agents/omarai.py#L155) | 155 | `"                    if key == \"assessment\""` | — |
| [SRC-C9CF9B54F8-L000156](../../agents/omarai.py#L156) | 156 | `"                    else row.get(key, \"\")"` | — |
| [SRC-C9CF9B54F8-L000157](../../agents/omarai.py#L157) | 157 | `"                    for key in fields"` | — |
| [SRC-C9CF9B54F8-L000158](../../agents/omarai.py#L158) | 158 | `"                }"` | — |
| [SRC-C9CF9B54F8-L000159](../../agents/omarai.py#L159) | 159 | `"                writer.writerow({key: _csv_safe_cell(value) for key, value in values.items()})"` | — |
| [SRC-C9CF9B54F8-L000160](../../agents/omarai.py#L160) | 160 | `"        return len(rows)"` | — |
## الوكيل والمنطق

### FILE-FDEEAFDFCA — [agents/request_budget.py](../../agents/request_budget.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-FDEEAFDFCA-L000001](../../agents/request_budget.py#L1) | 1 | `"\"\"\"Cooperative per-request resource budgets for Omarai's web-research pipeline."` | — |
| [SRC-FDEEAFDFCA-L000002](../../agents/request_budget.py#L2) | 2 | `""` | — |
| [SRC-FDEEAFDFCA-L000003](../../agents/request_budget.py#L3) | 3 | `"The budget limits work that has not started yet and caps the timeout supplied to"` | — |
| [SRC-FDEEAFDFCA-L000004](../../agents/request_budget.py#L4) | 4 | `"each outbound operation by the remaining request window. Socket libraries may"` | — |
| [SRC-FDEEAFDFCA-L000005](../../agents/request_budget.py#L5) | 5 | `"still overrun a cooperative deadline slightly while unwinding an in-flight call;"` | — |
| [SRC-FDEEAFDFCA-L000006](../../agents/request_budget.py#L6) | 6 | `"this is not a hard real-time cancellation primitive."` | — |
| [SRC-FDEEAFDFCA-L000007](../../agents/request_budget.py#L7) | 7 | `"\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000008](../../agents/request_budget.py#L8) | 8 | `"from __future__ import annotations"` | — |
| [SRC-FDEEAFDFCA-L000009](../../agents/request_budget.py#L9) | 9 | `""` | — |
| [SRC-FDEEAFDFCA-L000010](../../agents/request_budget.py#L10) | 10 | `"import os"` | — |
| [SRC-FDEEAFDFCA-L000011](../../agents/request_budget.py#L11) | 11 | `"import threading"` | — |
| [SRC-FDEEAFDFCA-L000012](../../agents/request_budget.py#L12) | 12 | `"import time"` | — |
| [SRC-FDEEAFDFCA-L000013](../../agents/request_budget.py#L13) | 13 | `"from collections.abc import Callable, Mapping"` | — |
| [SRC-FDEEAFDFCA-L000014](../../agents/request_budget.py#L14) | 14 | `"from typing import Any"` | — |
| [SRC-FDEEAFDFCA-L000015](../../agents/request_budget.py#L15) | 15 | `""` | — |
| [SRC-FDEEAFDFCA-L000016](../../agents/request_budget.py#L16) | 16 | `""` | — |
| [SRC-FDEEAFDFCA-L000017](../../agents/request_budget.py#L17) | 17 | `"class RequestBudgetExceeded(Exception):"` | — |
| [SRC-FDEEAFDFCA-L000018](../../agents/request_budget.py#L18) | 18 | `"    \"\"\"Raised when a request cannot start more work within its resource budget.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000019](../../agents/request_budget.py#L19) | 19 | `""` | — |
| [SRC-FDEEAFDFCA-L000020](../../agents/request_budget.py#L20) | 20 | `""` | — |
| [SRC-FDEEAFDFCA-L000021](../../agents/request_budget.py#L21) | 21 | `"DEFAULT_TIMEOUT_SECONDS = 90"` | — |
| [SRC-FDEEAFDFCA-L000022](../../agents/request_budget.py#L22) | 22 | `"MAX_TIMEOUT_SECONDS = 120"` | — |
| [SRC-FDEEAFDFCA-L000023](../../agents/request_budget.py#L23) | 23 | `"RESOURCE_LIMITS = {"` | — |
| [SRC-FDEEAFDFCA-L000024](../../agents/request_budget.py#L24) | 24 | `"    \"search_queries\": (8, 8),"` | — |
| [SRC-FDEEAFDFCA-L000025](../../agents/request_budget.py#L25) | 25 | `"    \"search_calls\": (32, 40),"` | — |
| [SRC-FDEEAFDFCA-L000026](../../agents/request_budget.py#L26) | 26 | `"    \"model_calls\": (8, 12),"` | — |
| [SRC-FDEEAFDFCA-L000027](../../agents/request_budget.py#L27) | 27 | `"    \"page_fetches\": (8, 8),"` | — |
| [SRC-FDEEAFDFCA-L000028](../../agents/request_budget.py#L28) | 28 | `"    \"tool_calls\": (3, 3),"` | — |
| [SRC-FDEEAFDFCA-L000029](../../agents/request_budget.py#L29) | 29 | `"}"` | — |
| [SRC-FDEEAFDFCA-L000030](../../agents/request_budget.py#L30) | 30 | `""` | — |
| [SRC-FDEEAFDFCA-L000031](../../agents/request_budget.py#L31) | 31 | `""` | — |
| [SRC-FDEEAFDFCA-L000032](../../agents/request_budget.py#L32) | 32 | `"def _bounded_env_int(name: str, default: int, minimum: int, maximum: int) -> int:"` | — |
| [SRC-FDEEAFDFCA-L000033](../../agents/request_budget.py#L33) | 33 | `"    raw = os.getenv(name, \"\").strip()"` | — |
| [SRC-FDEEAFDFCA-L000034](../../agents/request_budget.py#L34) | 34 | `"    try:"` | — |
| [SRC-FDEEAFDFCA-L000035](../../agents/request_budget.py#L35) | 35 | `"        value = int(raw) if raw else default"` | — |
| [SRC-FDEEAFDFCA-L000036](../../agents/request_budget.py#L36) | 36 | `"    except (TypeError, ValueError):"` | — |
| [SRC-FDEEAFDFCA-L000037](../../agents/request_budget.py#L37) | 37 | `"        value = default"` | — |
| [SRC-FDEEAFDFCA-L000038](../../agents/request_budget.py#L38) | 38 | `"    return max(minimum, min(value, maximum))"` | — |
| [SRC-FDEEAFDFCA-L000039](../../agents/request_budget.py#L39) | 39 | `""` | — |
| [SRC-FDEEAFDFCA-L000040](../../agents/request_budget.py#L40) | 40 | `""` | — |
| [SRC-FDEEAFDFCA-L000041](../../agents/request_budget.py#L41) | 41 | `"class RequestBudget:"` | — |
| [SRC-FDEEAFDFCA-L000042](../../agents/request_budget.py#L42) | 42 | `"    \"\"\"Thread-safe counters and a cooperative monotonic deadline for one answer.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000043](../../agents/request_budget.py#L43) | 43 | `""` | — |
| [SRC-FDEEAFDFCA-L000044](../../agents/request_budget.py#L44) | 44 | `"    def __init__("` | — |
| [SRC-FDEEAFDFCA-L000045](../../agents/request_budget.py#L45) | 45 | `"        self,"` | — |
| [SRC-FDEEAFDFCA-L000046](../../agents/request_budget.py#L46) | 46 | `"        timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,"` | — |
| [SRC-FDEEAFDFCA-L000047](../../agents/request_budget.py#L47) | 47 | `"        limits: Mapping[str, int] \| None = None,"` | — |
| [SRC-FDEEAFDFCA-L000048](../../agents/request_budget.py#L48) | 48 | `"        clock: Callable[[], float] = time.monotonic,"` | — |
| [SRC-FDEEAFDFCA-L000049](../../agents/request_budget.py#L49) | 49 | `"    ) -> None:"` | — |
| [SRC-FDEEAFDFCA-L000050](../../agents/request_budget.py#L50) | 50 | `"        self._clock = clock"` | — |
| [SRC-FDEEAFDFCA-L000051](../../agents/request_budget.py#L51) | 51 | `"        bounded_timeout = max(10, min(int(timeout_seconds), MAX_TIMEOUT_SECONDS))"` | — |
| [SRC-FDEEAFDFCA-L000052](../../agents/request_budget.py#L52) | 52 | `"        self.started_at = clock()"` | — |
| [SRC-FDEEAFDFCA-L000053](../../agents/request_budget.py#L53) | 53 | `"        self.deadline = self.started_at + bounded_timeout"` | — |
| [SRC-FDEEAFDFCA-L000054](../../agents/request_budget.py#L54) | 54 | `"        self._limits = {"` | — |
| [SRC-FDEEAFDFCA-L000055](../../agents/request_budget.py#L55) | 55 | `"            key: max(0, min(int(value), RESOURCE_LIMITS[key][1]))"` | — |
| [SRC-FDEEAFDFCA-L000056](../../agents/request_budget.py#L56) | 56 | `"            for key, (default, _maximum) in RESOURCE_LIMITS.items()"` | — |
| [SRC-FDEEAFDFCA-L000057](../../agents/request_budget.py#L57) | 57 | `"            for value in [limits[key] if limits and key in limits else default]"` | — |
| [SRC-FDEEAFDFCA-L000058](../../agents/request_budget.py#L58) | 58 | `"        }"` | — |
| [SRC-FDEEAFDFCA-L000059](../../agents/request_budget.py#L59) | 59 | `"        self._counts = {key: 0 for key in self._limits}"` | — |
| [SRC-FDEEAFDFCA-L000060](../../agents/request_budget.py#L60) | 60 | `"        self._exhausted_reasons: set[str] = set()"` | — |
| [SRC-FDEEAFDFCA-L000061](../../agents/request_budget.py#L61) | 61 | `"        self._lock = threading.Lock()"` | — |
| [SRC-FDEEAFDFCA-L000062](../../agents/request_budget.py#L62) | 62 | `""` | — |
| [SRC-FDEEAFDFCA-L000063](../../agents/request_budget.py#L63) | 63 | `"    @classmethod"` | — |
| [SRC-FDEEAFDFCA-L000064](../../agents/request_budget.py#L64) | 64 | `"    def from_environment(cls) -> RequestBudget:"` | — |
| [SRC-FDEEAFDFCA-L000065](../../agents/request_budget.py#L65) | 65 | `"        timeout = _bounded_env_int("` | — |
| [SRC-FDEEAFDFCA-L000066](../../agents/request_budget.py#L66) | 66 | `"            \"OMARAI_REQUEST_BUDGET_SECONDS\","` | — |
| [SRC-FDEEAFDFCA-L000067](../../agents/request_budget.py#L67) | 67 | `"            DEFAULT_TIMEOUT_SECONDS,"` | — |
| [SRC-FDEEAFDFCA-L000068](../../agents/request_budget.py#L68) | 68 | `"            10,"` | — |
| [SRC-FDEEAFDFCA-L000069](../../agents/request_budget.py#L69) | 69 | `"            MAX_TIMEOUT_SECONDS,"` | — |
| [SRC-FDEEAFDFCA-L000070](../../agents/request_budget.py#L70) | 70 | `"        )"` | — |
| [SRC-FDEEAFDFCA-L000071](../../agents/request_budget.py#L71) | 71 | `"        limits = {"` | — |
| [SRC-FDEEAFDFCA-L000072](../../agents/request_budget.py#L72) | 72 | `"            key: _bounded_env_int("` | — |
| [SRC-FDEEAFDFCA-L000073](../../agents/request_budget.py#L73) | 73 | `"                f\"OMARAI_REQUEST_MAX_{key.upper()}\","` | — |
| [SRC-FDEEAFDFCA-L000074](../../agents/request_budget.py#L74) | 74 | `"                defaults[0],"` | — |
| [SRC-FDEEAFDFCA-L000075](../../agents/request_budget.py#L75) | 75 | `"                0 if key == \"tool_calls\" else 1,"` | — |
| [SRC-FDEEAFDFCA-L000076](../../agents/request_budget.py#L76) | 76 | `"                defaults[1],"` | — |
| [SRC-FDEEAFDFCA-L000077](../../agents/request_budget.py#L77) | 77 | `"            )"` | — |
| [SRC-FDEEAFDFCA-L000078](../../agents/request_budget.py#L78) | 78 | `"            for key, defaults in RESOURCE_LIMITS.items()"` | — |
| [SRC-FDEEAFDFCA-L000079](../../agents/request_budget.py#L79) | 79 | `"        }"` | — |
| [SRC-FDEEAFDFCA-L000080](../../agents/request_budget.py#L80) | 80 | `"        return cls(timeout_seconds=timeout, limits=limits)"` | — |
| [SRC-FDEEAFDFCA-L000081](../../agents/request_budget.py#L81) | 81 | `""` | — |
| [SRC-FDEEAFDFCA-L000082](../../agents/request_budget.py#L82) | 82 | `"    def remaining_seconds(self) -> float:"` | — |
| [SRC-FDEEAFDFCA-L000083](../../agents/request_budget.py#L83) | 83 | `"        return max(0.0, self.deadline - self._clock())"` | — |
| [SRC-FDEEAFDFCA-L000084](../../agents/request_budget.py#L84) | 84 | `""` | — |
| [SRC-FDEEAFDFCA-L000085](../../agents/request_budget.py#L85) | 85 | `"    def timeout_for(self, configured_seconds: float) -> float:"` | — |
| [SRC-FDEEAFDFCA-L000086](../../agents/request_budget.py#L86) | 86 | `"        \"\"\"Cap one outbound timeout to time remaining; raise instead of starting at zero.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000087](../../agents/request_budget.py#L87) | 87 | `"        remaining = self.remaining_seconds()"` | — |
| [SRC-FDEEAFDFCA-L000088](../../agents/request_budget.py#L88) | 88 | `"        if remaining <= 0:"` | — |
| [SRC-FDEEAFDFCA-L000089](../../agents/request_budget.py#L89) | 89 | `"            with self._lock:"` | — |
| [SRC-FDEEAFDFCA-L000090](../../agents/request_budget.py#L90) | 90 | `"                self._exhausted_reasons.add(\"deadline\")"` | — |
| [SRC-FDEEAFDFCA-L000091](../../agents/request_budget.py#L91) | 91 | `"            raise RequestBudgetExceeded(\"انتهت ميزانية وقت الطلب.\")"` | — |
| [SRC-FDEEAFDFCA-L000092](../../agents/request_budget.py#L92) | 92 | `"        return min(float(configured_seconds), remaining)"` | — |
| [SRC-FDEEAFDFCA-L000093](../../agents/request_budget.py#L93) | 93 | `""` | — |
| [SRC-FDEEAFDFCA-L000094](../../agents/request_budget.py#L94) | 94 | `"    def remaining_units(self, resource: str) -> int:"` | — |
| [SRC-FDEEAFDFCA-L000095](../../agents/request_budget.py#L95) | 95 | `"        \"\"\"Return unused units for a resource; zero means disabled, exhausted, or expired.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000096](../../agents/request_budget.py#L96) | 96 | `"        if resource not in self._limits:"` | — |
| [SRC-FDEEAFDFCA-L000097](../../agents/request_budget.py#L97) | 97 | `"            raise ValueError(f\"unknown request-budget resource: {resource}\")"` | — |
| [SRC-FDEEAFDFCA-L000098](../../agents/request_budget.py#L98) | 98 | `"        if self.remaining_seconds() <= 0:"` | — |
| [SRC-FDEEAFDFCA-L000099](../../agents/request_budget.py#L99) | 99 | `"            return 0"` | — |
| [SRC-FDEEAFDFCA-L000100](../../agents/request_budget.py#L100) | 100 | `"        with self._lock:"` | — |
| [SRC-FDEEAFDFCA-L000101](../../agents/request_budget.py#L101) | 101 | `"            return max(0, self._limits[resource] - self._counts[resource])"` | — |
| [SRC-FDEEAFDFCA-L000102](../../agents/request_budget.py#L102) | 102 | `""` | — |
| [SRC-FDEEAFDFCA-L000103](../../agents/request_budget.py#L103) | 103 | `"    def reserve(self, resource: str, amount: int = 1) -> None:"` | — |
| [SRC-FDEEAFDFCA-L000104](../../agents/request_budget.py#L104) | 104 | `"        \"\"\"Atomically reserve resource units before initiating external work.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000105](../../agents/request_budget.py#L105) | 105 | `"        if resource not in self._limits:"` | — |
| [SRC-FDEEAFDFCA-L000106](../../agents/request_budget.py#L106) | 106 | `"            raise ValueError(f\"unknown request-budget resource: {resource}\")"` | — |
| [SRC-FDEEAFDFCA-L000107](../../agents/request_budget.py#L107) | 107 | `"        if amount < 1:"` | — |
| [SRC-FDEEAFDFCA-L000108](../../agents/request_budget.py#L108) | 108 | `"            raise ValueError(\"reservation amount must be positive\")"` | — |
| [SRC-FDEEAFDFCA-L000109](../../agents/request_budget.py#L109) | 109 | `"        with self._lock:"` | — |
| [SRC-FDEEAFDFCA-L000110](../../agents/request_budget.py#L110) | 110 | `"            if self.remaining_seconds() <= 0:"` | — |
| [SRC-FDEEAFDFCA-L000111](../../agents/request_budget.py#L111) | 111 | `"                self._exhausted_reasons.add(\"deadline\")"` | — |
| [SRC-FDEEAFDFCA-L000112](../../agents/request_budget.py#L112) | 112 | `"                raise RequestBudgetExceeded(\"انتهت ميزانية وقت الطلب.\")"` | — |
| [SRC-FDEEAFDFCA-L000113](../../agents/request_budget.py#L113) | 113 | `"            limit = self._limits[resource]"` | — |
| [SRC-FDEEAFDFCA-L000114](../../agents/request_budget.py#L114) | 114 | `"            if self._counts[resource] + amount > limit:"` | — |
| [SRC-FDEEAFDFCA-L000115](../../agents/request_budget.py#L115) | 115 | `"                self._exhausted_reasons.add(resource)"` | — |
| [SRC-FDEEAFDFCA-L000116](../../agents/request_budget.py#L116) | 116 | `"                raise RequestBudgetExceeded("` | — |
| [SRC-FDEEAFDFCA-L000117](../../agents/request_budget.py#L117) | 117 | `"                    f\"تم بلوغ حد موارد الطلب: {resource}.\""` | — |
| [SRC-FDEEAFDFCA-L000118](../../agents/request_budget.py#L118) | 118 | `"                )"` | — |
| [SRC-FDEEAFDFCA-L000119](../../agents/request_budget.py#L119) | 119 | `"            self._counts[resource] += amount"` | — |
| [SRC-FDEEAFDFCA-L000120](../../agents/request_budget.py#L120) | 120 | `""` | — |
| [SRC-FDEEAFDFCA-L000121](../../agents/request_budget.py#L121) | 121 | `"    def snapshot(self) -> dict[str, Any]:"` | — |
| [SRC-FDEEAFDFCA-L000122](../../agents/request_budget.py#L122) | 122 | `"        with self._lock:"` | — |
| [SRC-FDEEAFDFCA-L000123](../../agents/request_budget.py#L123) | 123 | `"            counts = dict(self._counts)"` | — |
| [SRC-FDEEAFDFCA-L000124](../../agents/request_budget.py#L124) | 124 | `"            limits = dict(self._limits)"` | — |
| [SRC-FDEEAFDFCA-L000125](../../agents/request_budget.py#L125) | 125 | `"            exhausted_reasons = sorted(self._exhausted_reasons)"` | — |
| [SRC-FDEEAFDFCA-L000126](../../agents/request_budget.py#L126) | 126 | `"        remaining = self.remaining_seconds()"` | — |
| [SRC-FDEEAFDFCA-L000127](../../agents/request_budget.py#L127) | 127 | `"        return {"` | — |
| [SRC-FDEEAFDFCA-L000128](../../agents/request_budget.py#L128) | 128 | `"            \"policy\": \"cooperative_per_request_budget\","` | — |
| [SRC-FDEEAFDFCA-L000129](../../agents/request_budget.py#L129) | 129 | `"            \"timeout_seconds\": round(self.deadline - self.started_at, 3),"` | — |
| [SRC-FDEEAFDFCA-L000130](../../agents/request_budget.py#L130) | 130 | `"            \"elapsed_seconds\": round(max(0.0, self._clock() - self.started_at), 3),"` | — |
| [SRC-FDEEAFDFCA-L000131](../../agents/request_budget.py#L131) | 131 | `"            \"remaining_seconds\": round(remaining, 3),"` | — |
| [SRC-FDEEAFDFCA-L000132](../../agents/request_budget.py#L132) | 132 | `"            \"deadline_exceeded\": remaining <= 0,"` | — |
| [SRC-FDEEAFDFCA-L000133](../../agents/request_budget.py#L133) | 133 | `"            \"budget_exhausted\": bool(exhausted_reasons) or remaining <= 0,"` | — |
| [SRC-FDEEAFDFCA-L000134](../../agents/request_budget.py#L134) | 134 | `"            \"exhausted_reasons\": exhausted_reasons,"` | — |
| [SRC-FDEEAFDFCA-L000135](../../agents/request_budget.py#L135) | 135 | `"            \"counts\": counts,"` | — |
| [SRC-FDEEAFDFCA-L000136](../../agents/request_budget.py#L136) | 136 | `"            \"limits\": limits,"` | — |
| [SRC-FDEEAFDFCA-L000137](../../agents/request_budget.py#L137) | 137 | `"            \"resources_at_limit\": ["` | — |
| [SRC-FDEEAFDFCA-L000138](../../agents/request_budget.py#L138) | 138 | `"                key for key, limit in limits.items() if limit > 0 and counts[key] >= limit"` | — |
| [SRC-FDEEAFDFCA-L000139](../../agents/request_budget.py#L139) | 139 | `"            ],"` | — |
| [SRC-FDEEAFDFCA-L000140](../../agents/request_budget.py#L140) | 140 | `"            \"disabled_resources\": [key for key, limit in limits.items() if limit == 0],"` | — |
| [SRC-FDEEAFDFCA-L000141](../../agents/request_budget.py#L141) | 141 | `"            \"hard_cancellation_guaranteed\": False,"` | — |
| [SRC-FDEEAFDFCA-L000142](../../agents/request_budget.py#L142) | 142 | `"        }"` | — |
## الوكيل والمنطق

### FILE-59CF4B7DE8 — [agents/research.py](../../agents/research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-59CF4B7DE8-L000001](../../agents/research.py#L1) | 1 | `"\"\"\"Research planning, domain targeting, and multi-query source ranking."` | — |
| [SRC-59CF4B7DE8-L000002](../../agents/research.py#L2) | 2 | `""` | — |
| [SRC-59CF4B7DE8-L000003](../../agents/research.py#L3) | 3 | `"This module is deterministic by design: the language model may propose a plan,"` | — |
| [SRC-59CF4B7DE8-L000004](../../agents/research.py#L4) | 4 | `"but all queries, result counts and source records are validated before use."` | — |
| [SRC-59CF4B7DE8-L000005](../../agents/research.py#L5) | 5 | `"\"\"\""` | — |
| [SRC-59CF4B7DE8-L000006](../../agents/research.py#L6) | 6 | `"from __future__ import annotations"` | — |
| [SRC-59CF4B7DE8-L000007](../../agents/research.py#L7) | 7 | `""` | — |
| [SRC-59CF4B7DE8-L000008](../../agents/research.py#L8) | 8 | `"import ipaddress"` | — |
| [SRC-59CF4B7DE8-L000009](../../agents/research.py#L9) | 9 | `"import re"` | — |
| [SRC-59CF4B7DE8-L000010](../../agents/research.py#L10) | 10 | `"from datetime import UTC, datetime, timedelta"` | — |
| [SRC-59CF4B7DE8-L000011](../../agents/research.py#L11) | 11 | `"from email.utils import parsedate_to_datetime"` | — |
| [SRC-59CF4B7DE8-L000012](../../agents/research.py#L12) | 12 | `"from typing import Any"` | — |
| [SRC-59CF4B7DE8-L000013](../../agents/research.py#L13) | 13 | `"from urllib.parse import urlparse"` | — |
| [SRC-59CF4B7DE8-L000014](../../agents/research.py#L14) | 14 | `""` | — |
| [SRC-59CF4B7DE8-L000015](../../agents/research.py#L15) | 15 | `"import tldextract"` | — |
| [SRC-59CF4B7DE8-L000016](../../agents/research.py#L16) | 16 | `""` | — |
| [SRC-59CF4B7DE8-L000017](../../agents/research.py#L17) | 17 | `"from agents.aspect_planning import extract_aspects"` | — |
| [SRC-59CF4B7DE8-L000018](../../agents/research.py#L18) | 18 | `"from agents.intent_router import resolve_followup_query"` | — |
| [SRC-59CF4B7DE8-L000019](../../agents/research.py#L19) | 19 | `"from agents.task_understanding import build_query_strategy_matrix, build_task_spec"` | — |
| [SRC-59CF4B7DE8-L000020](../../agents/research.py#L20) | 20 | `""` | — |
| [SRC-59CF4B7DE8-L000021](../../agents/research.py#L21) | 21 | `"MAX_PLAN_QUERIES = 8"` | — |
| [SRC-59CF4B7DE8-L000022](../../agents/research.py#L22) | 22 | `"MAX_QUERY_CHARS = 240"` | — |
| [SRC-59CF4B7DE8-L000023](../../agents/research.py#L23) | 23 | `"MAX_FUSED_RESULTS = 18"` | — |
| [SRC-59CF4B7DE8-L000024](../../agents/research.py#L24) | 24 | `""` | — |
| [SRC-59CF4B7DE8-L000025](../../agents/research.py#L25) | 25 | `""` | — |
| [SRC-59CF4B7DE8-L000026](../../agents/research.py#L26) | 26 | `"# Use the Public Suffix List snapshot bundled with tldextract; never fetch it at"` | — |
| [SRC-59CF4B7DE8-L000027](../../agents/research.py#L27) | 27 | `"# runtime. Including private suffixes keeps tenant-hosted sites (e.g. github.io)"` | — |
| [SRC-59CF4B7DE8-L000028](../../agents/research.py#L28) | 28 | `"# separate, while subdomains belonging to one registrable site share one identity."` | — |
| [SRC-59CF4B7DE8-L000029](../../agents/research.py#L29) | 29 | `"_DOMAIN_EXTRACTOR = tldextract.TLDExtract("` | — |
| [SRC-59CF4B7DE8-L000030](../../agents/research.py#L30) | 30 | `"    suffix_list_urls=(),"` | — |
| [SRC-59CF4B7DE8-L000031](../../agents/research.py#L31) | 31 | `"    include_psl_private_domains=True,"` | — |
| [SRC-59CF4B7DE8-L000032](../../agents/research.py#L32) | 32 | `")"` | — |
| [SRC-59CF4B7DE8-L000033](../../agents/research.py#L33) | 33 | `""` | — |
| [SRC-59CF4B7DE8-L000034](../../agents/research.py#L34) | 34 | `""` | — |
| [SRC-59CF4B7DE8-L000035](../../agents/research.py#L35) | 35 | `"def registrable_domain(value: Any) -> str:"` | — |
| [SRC-59CF4B7DE8-L000036](../../agents/research.py#L36) | 36 | `"    \"\"\"Return a normalized registrable domain (or normalized IP/unknown hostname)."` | — |
| [SRC-59CF4B7DE8-L000037](../../agents/research.py#L37) | 37 | `""` | — |
| [SRC-59CF4B7DE8-L000038](../../agents/research.py#L38) | 38 | `"    This is a conservative source-diversity key, not proof that two publishers"` | — |
| [SRC-59CF4B7DE8-L000039](../../agents/research.py#L39) | 39 | `"    are editorially independent. It prevents sibling subdomains from being"` | — |
| [SRC-59CF4B7DE8-L000040](../../agents/research.py#L40) | 40 | `"    counted as separate domains in the evidence coverage threshold."` | — |
| [SRC-59CF4B7DE8-L000041](../../agents/research.py#L41) | 41 | `"    \"\"\""` | — |
| [SRC-59CF4B7DE8-L000042](../../agents/research.py#L42) | 42 | `"    candidate = str(value or \"\").strip()"` | — |
| [SRC-59CF4B7DE8-L000043](../../agents/research.py#L43) | 43 | `"    if not candidate:"` | — |
| [SRC-59CF4B7DE8-L000044](../../agents/research.py#L44) | 44 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000045](../../agents/research.py#L45) | 45 | `"    parsed = urlparse(candidate if \"://\" in candidate else \"//\" + candidate)"` | — |
| [SRC-59CF4B7DE8-L000046](../../agents/research.py#L46) | 46 | `"    host = (parsed.hostname or \"\").rstrip(\".\").lower()"` | — |
| [SRC-59CF4B7DE8-L000047](../../agents/research.py#L47) | 47 | `"    if not host:"` | — |
| [SRC-59CF4B7DE8-L000048](../../agents/research.py#L48) | 48 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000049](../../agents/research.py#L49) | 49 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000050](../../agents/research.py#L50) | 50 | `"        return str(ipaddress.ip_address(host))"` | — |
| [SRC-59CF4B7DE8-L000051](../../agents/research.py#L51) | 51 | `"    except ValueError:"` | — |
| [SRC-59CF4B7DE8-L000052](../../agents/research.py#L52) | 52 | `"        pass"` | — |
| [SRC-59CF4B7DE8-L000053](../../agents/research.py#L53) | 53 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000054](../../agents/research.py#L54) | 54 | `"        host = host.encode(\"idna\").decode(\"ascii\").lower()"` | — |
| [SRC-59CF4B7DE8-L000055](../../agents/research.py#L55) | 55 | `"    except UnicodeError:"` | — |
| [SRC-59CF4B7DE8-L000056](../../agents/research.py#L56) | 56 | `"        return host"` | — |
| [SRC-59CF4B7DE8-L000057](../../agents/research.py#L57) | 57 | `"    extracted = _DOMAIN_EXTRACTOR(host)"` | — |
| [SRC-59CF4B7DE8-L000058](../../agents/research.py#L58) | 58 | `"    return (extracted.top_domain_under_public_suffix or host).lower()"` | — |
| [SRC-59CF4B7DE8-L000059](../../agents/research.py#L59) | 59 | `""` | — |
| [SRC-59CF4B7DE8-L000060](../../agents/research.py#L60) | 60 | `"SOCIAL_DOMAINS = {"` | — |
| [SRC-59CF4B7DE8-L000061](../../agents/research.py#L61) | 61 | `"    \"reddit\": \"reddit.com\","` | — |
| [SRC-59CF4B7DE8-L000062](../../agents/research.py#L62) | 62 | `"    \"youtube\": \"youtube.com\","` | — |
| [SRC-59CF4B7DE8-L000063](../../agents/research.py#L63) | 63 | `"    \"facebook\": \"facebook.com\","` | — |
| [SRC-59CF4B7DE8-L000064](../../agents/research.py#L64) | 64 | `"    \"instagram\": \"instagram.com\","` | — |
| [SRC-59CF4B7DE8-L000065](../../agents/research.py#L65) | 65 | `"    \"x\": \"x.com\","` | — |
| [SRC-59CF4B7DE8-L000066](../../agents/research.py#L66) | 66 | `"    \"twitter\": \"twitter.com\","` | — |
| [SRC-59CF4B7DE8-L000067](../../agents/research.py#L67) | 67 | `"    \"tiktok\": \"tiktok.com\","` | — |
| [SRC-59CF4B7DE8-L000068](../../agents/research.py#L68) | 68 | `"    \"linkedin\": \"linkedin.com\","` | — |
| [SRC-59CF4B7DE8-L000069](../../agents/research.py#L69) | 69 | `"    \"threads\": \"threads.net\","` | — |
| [SRC-59CF4B7DE8-L000070](../../agents/research.py#L70) | 70 | `"    \"bluesky\": \"bsky.app\","` | — |
| [SRC-59CF4B7DE8-L000071](../../agents/research.py#L71) | 71 | `"}"` | — |
| [SRC-59CF4B7DE8-L000072](../../agents/research.py#L72) | 72 | `""` | — |
| [SRC-59CF4B7DE8-L000073](../../agents/research.py#L73) | 73 | `"_SOCIAL_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000074](../../agents/research.py#L74) | 74 | `"    \"social media\", \"social network\", \"social posts\", \"social pages\", \"public social\", \"public posts\","` | — |
| [SRC-59CF4B7DE8-L000075](../../agents/research.py#L75) | 75 | `"    \"facebook\", \"instagram\", \"reddit\", \"youtube\", \"twitter\", \"x.com\","` | — |
| [SRC-59CF4B7DE8-L000076](../../agents/research.py#L76) | 76 | `"    \"tiktok\", \"linkedin\", \"threads\", \"bluesky\","` | — |
| [SRC-59CF4B7DE8-L000077](../../agents/research.py#L77) | 77 | `"    \"سوشيال\", \"التواصل الاجتماعي\", \"مواقع التواصل\", \"صفحات التواصل\","` | — |
| [SRC-59CF4B7DE8-L000078](../../agents/research.py#L78) | 78 | `"    \"منشورات\", \"تعليقات الناس\", \"آراء الناس\", \"تجارب المستخدمين\","` | — |
| [SRC-59CF4B7DE8-L000079](../../agents/research.py#L79) | 79 | `"    \"تجارب العملاء\", \"اراء العملاء\", \"آراء العملاء\", \"رأي الناس\","` | — |
| [SRC-59CF4B7DE8-L000080](../../agents/research.py#L80) | 80 | `"    \"كلام الناس\", \"الناس بتقول\", \"مراجعات العملاء\", \"تعليقات العملاء\","` | — |
| [SRC-59CF4B7DE8-L000081](../../agents/research.py#L81) | 81 | `"    \"بوستات\", \"فيدوهات\", \"فيديوهات\", \"ريلز\", \"تويتر\", \"فيسبوك\","` | — |
| [SRC-59CF4B7DE8-L000082](../../agents/research.py#L82) | 82 | `"    \"انستجرام\", \"إنستجرام\", \"تيك توك\", \"لينكدان\", \"لينكدإن\","` | — |
| [SRC-59CF4B7DE8-L000083](../../agents/research.py#L83) | 83 | `"    \"مصادر العملاء\", \"عملاء محتملين\", \"العملاء المحتملين\","` | — |
| [SRC-59CF4B7DE8-L000084](../../agents/research.py#L84) | 84 | `")"` | — |
| [SRC-59CF4B7DE8-L000085](../../agents/research.py#L85) | 85 | `""` | — |
| [SRC-59CF4B7DE8-L000086](../../agents/research.py#L86) | 86 | `"_FRESH_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000087](../../agents/research.py#L87) | 87 | `"    \"latest\", \"current\", \"today\", \"this week\", \"recent\", \"breaking\", \"news\","` | — |
| [SRC-59CF4B7DE8-L000088](../../agents/research.py#L88) | 88 | `"    \"now\", \"2026\", \"latest price\", \"market price\", \"updated\","` | — |
| [SRC-59CF4B7DE8-L000089](../../agents/research.py#L89) | 89 | `"    \"آخر\", \"اخر\", \"احدث\", \"أحدث\", \"حاليا\", \"حالياً\", \"الآن\", \"دلوقتي\", \"النهارده\", \"مؤخرًا\", \"مؤخرا\", \"اليوم\", \"هذا الاسبوع\","` | — |
| [SRC-59CF4B7DE8-L000090](../../agents/research.py#L90) | 90 | `"    \"هذا الأسبوع\", \"آخر الأخبار\", \"اخر الاخبار\", \"مستجدات\", \"حديث\","` | — |
| [SRC-59CF4B7DE8-L000091](../../agents/research.py#L91) | 91 | `"    \"سعر اليوم\", \"الاسعار الحالية\", \"الأسعار الحالية\", \"جديد\","` | — |
| [SRC-59CF4B7DE8-L000092](../../agents/research.py#L92) | 92 | `")"` | — |
| [SRC-59CF4B7DE8-L000093](../../agents/research.py#L93) | 93 | `""` | — |
| [SRC-59CF4B7DE8-L000094](../../agents/research.py#L94) | 94 | `"_DEEP_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000095](../../agents/research.py#L95) | 95 | `"    \"deep research\", \"in-depth\", \"comprehensive\", \"exhaustive\", \"compare\","` | — |
| [SRC-59CF4B7DE8-L000096](../../agents/research.py#L96) | 96 | `"    \"comparison\", \"pros and cons\", \"investigate\", \"evidence\", \"sources\","` | — |
| [SRC-59CF4B7DE8-L000097](../../agents/research.py#L97) | 97 | `"    \"بحث عميق\", \"بحث معمق\", \"بحث مكثف\", \"بحث شامل\", \"بالتفصيل\", \"قارن\","` | — |
| [SRC-59CF4B7DE8-L000098](../../agents/research.py#L98) | 98 | `"    \"مقارنة\", \"استقصاء\", \"تحقق\", \"تأكد\", \"مصادر\", \"أدلة\", \"ادلة\","` | — |
| [SRC-59CF4B7DE8-L000099](../../agents/research.py#L99) | 99 | `"    \"كل الجوانب\", \"بحث واسع\", \"متكامل\","` | — |
| [SRC-59CF4B7DE8-L000100](../../agents/research.py#L100) | 100 | `")"` | — |
| [SRC-59CF4B7DE8-L000101](../../agents/research.py#L101) | 101 | `""` | — |
| [SRC-59CF4B7DE8-L000102](../../agents/research.py#L102) | 102 | `""` | — |
| [SRC-59CF4B7DE8-L000103](../../agents/research.py#L103) | 103 | `"def extract_urls(text: str) -> list[str]:"` | — |
| [SRC-59CF4B7DE8-L000104](../../agents/research.py#L104) | 104 | `"    \"\"\"Extract explicit HTTP(S) URLs without trying to interpret their content as instructions.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000105](../../agents/research.py#L105) | 105 | `"    candidates = re.findall(r\"https?://[^\\s<>()]+\", text or \"\", flags=re.IGNORECASE)"` | — |
| [SRC-59CF4B7DE8-L000106](../../agents/research.py#L106) | 106 | `"    cleaned: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000107](../../agents/research.py#L107) | 107 | `"    for value in candidates:"` | — |
| [SRC-59CF4B7DE8-L000108](../../agents/research.py#L108) | 108 | `"        url = value.rstrip(\".,;!?،؛:)\\\"'»\")"` | — |
| [SRC-59CF4B7DE8-L000109](../../agents/research.py#L109) | 109 | `"        if url and url not in cleaned:"` | — |
| [SRC-59CF4B7DE8-L000110](../../agents/research.py#L110) | 110 | `"            cleaned.append(url[:2048])"` | — |
| [SRC-59CF4B7DE8-L000111](../../agents/research.py#L111) | 111 | `"        if len(cleaned) >= 5:"` | — |
| [SRC-59CF4B7DE8-L000112](../../agents/research.py#L112) | 112 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000113](../../agents/research.py#L113) | 113 | `"    return cleaned"` | — |
| [SRC-59CF4B7DE8-L000114](../../agents/research.py#L114) | 114 | `""` | — |
| [SRC-59CF4B7DE8-L000115](../../agents/research.py#L115) | 115 | `""` | — |
| [SRC-59CF4B7DE8-L000116](../../agents/research.py#L116) | 116 | `"def _compact(value: Any, limit: int = MAX_QUERY_CHARS) -> str:"` | — |
| [SRC-59CF4B7DE8-L000117](../../agents/research.py#L117) | 117 | `"    if not isinstance(value, str):"` | — |
| [SRC-59CF4B7DE8-L000118](../../agents/research.py#L118) | 118 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000119](../../agents/research.py#L119) | 119 | `"    return re.sub(r\"\\s+\", \" \", value).strip()[:limit]"` | — |
| [SRC-59CF4B7DE8-L000120](../../agents/research.py#L120) | 120 | `""` | — |
| [SRC-59CF4B7DE8-L000121](../../agents/research.py#L121) | 121 | `""` | — |
| [SRC-59CF4B7DE8-L000122](../../agents/research.py#L122) | 122 | `"_SEARCH_TOPIC_PRESERVING_META_PREFIX_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000123](../../agents/research.py#L123) | 123 | `"    r\"^(?:(?:و?استخدم\|و?استعمل)\\s+مصادر?\\s+متعددة\\s+\""` | — |
| [SRC-59CF4B7DE8-L000124](../../agents/research.py#L124) | 124 | `"    r\"(?:للبحث\\s+عن\|للعثور\\s+على\|لإيجاد\|عن\|حول\|بشأن)\|\""` | — |
| [SRC-59CF4B7DE8-L000125](../../agents/research.py#L125) | 125 | `"    r\"use\\s+multiple\\s+sources\\s+to\\s+(?:research\|find\|investigate))\\s+\","` | — |
| [SRC-59CF4B7DE8-L000126](../../agents/research.py#L126) | 126 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000127](../../agents/research.py#L127) | 127 | `")"` | — |
| [SRC-59CF4B7DE8-L000128](../../agents/research.py#L128) | 128 | `""` | — |
| [SRC-59CF4B7DE8-L000129](../../agents/research.py#L129) | 129 | `"_SEARCH_META_START_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000130](../../agents/research.py#L130) | 130 | `"    r\"^(?:و?استخدم\|و?استعمل\|و?اجب\|و?أجب\|و?لا تعرض\|و?لا تقدم\|\""` | — |
| [SRC-59CF4B7DE8-L000131](../../agents/research.py#L131) | 131 | `"    r\"please cite\|cite\|provide links\|mention sources\|use multiple sources\|\""` | — |
| [SRC-59CF4B7DE8-L000132](../../agents/research.py#L132) | 132 | `"    r\"don't present\|do not present)\\b\","` | — |
| [SRC-59CF4B7DE8-L000133](../../agents/research.py#L133) | 133 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000134](../../agents/research.py#L134) | 134 | `")"` | — |
| [SRC-59CF4B7DE8-L000135](../../agents/research.py#L135) | 135 | `"# Treat \"اذكر\" as an action unless its object is clearly citation/format metadata."` | — |
| [SRC-59CF4B7DE8-L000136](../../agents/research.py#L136) | 136 | `"# This preserves topic-bearing prompts such as \"اذكر أبرز السيارات الكهربائية...\"."` | — |
| [SRC-59CF4B7DE8-L000137](../../agents/research.py#L137) | 137 | `"_SEARCH_CITATION_META_START_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000138](../../agents/research.py#L138) | 138 | `"    r\"^(?:و?اذكر(?:ي\|وا)?\|mention\|cite\|provide)\\s+\""` | — |
| [SRC-59CF4B7DE8-L000139](../../agents/research.py#L139) | 139 | `"    r\"(?:المصادر\|مصادر\|المصدر\|مصدر(?:[ًٌٍ]ا?\|ا[ًٌٍ]?)?\|\""` | — |
| [SRC-59CF4B7DE8-L000140](../../agents/research.py#L140) | 140 | `"    r\"روابط?\|رابط\|تواريخ?\|تاريخ\|الاخبار\|الأخبار\|\""` | — |
| [SRC-59CF4B7DE8-L000141](../../agents/research.py#L141) | 141 | `"    r\"the original posts\|links\|sources\|dates)(?=\\s\|$\|[،,])\","` | — |
| [SRC-59CF4B7DE8-L000142](../../agents/research.py#L142) | 142 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000143](../../agents/research.py#L143) | 143 | `")"` | — |
| [SRC-59CF4B7DE8-L000144](../../agents/research.py#L144) | 144 | `"# This is a response-quality instruction, not a topic query."` | — |
| [SRC-59CF4B7DE8-L000145](../../agents/research.py#L145) | 145 | `"_SEARCH_UNCERTAINTY_META_START_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000146](../../agents/research.py#L146) | 146 | `"    r\"^و?وضّ?ح\\s+اذا\\s+كانت\\s+النتائج\\s+غير\\s+كافيه\\b\""` | — |
| [SRC-59CF4B7DE8-L000147](../../agents/research.py#L147) | 147 | `"    r\".*(?:لتمثيل\|تمثيل).*(?:اراء\\s+المستخدمين\|المستخدمين)\\b\","` | — |
| [SRC-59CF4B7DE8-L000148](../../agents/research.py#L148) | 148 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000149](../../agents/research.py#L149) | 149 | `")"` | — |
| [SRC-59CF4B7DE8-L000150](../../agents/research.py#L150) | 150 | `""` | — |
| [SRC-59CF4B7DE8-L000151](../../agents/research.py#L151) | 151 | `"_SEARCH_FACTS_INFERENCE_META_ONLY_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000152](../../agents/research.py#L152) | 152 | `"    r\"^و?(?:ميّز\|ميز)\\s+بين\\s+الحقائق\\s+والاستنتاجات\\s*[.!؟؛،,]*$\","` | — |
| [SRC-59CF4B7DE8-L000153](../../agents/research.py#L153) | 153 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000154](../../agents/research.py#L154) | 154 | `")"` | — |
| [SRC-59CF4B7DE8-L000155](../../agents/research.py#L155) | 155 | `"_SEARCH_META_TAIL_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000156](../../agents/research.py#L156) | 156 | `"    r\"\\s*[,،؛;]\\s*(?:و\\s*)?(?:استخدم\|استعمل\|ميّز\|ميز\|اجب\|أجب\|لا تعرض\|لا تقدم\|\""` | — |
| [SRC-59CF4B7DE8-L000157](../../agents/research.py#L157) | 157 | `"    r\"please cite\|cite\|provide links\|mention sources\|use multiple sources\|\""` | — |
| [SRC-59CF4B7DE8-L000158](../../agents/research.py#L158) | 158 | `"    r\"don't present\|do not present\|\""` | — |
| [SRC-59CF4B7DE8-L000159](../../agents/research.py#L159) | 159 | `"    r\"اذكر(?:ي\|وا)?\\s+(?:مصادر?\|المصادر\|مصدر\|روابط?\|رابط\|تواريخ?\|تاريخ\|الاخبار\|الأخبار))\\b.*$\","` | — |
| [SRC-59CF4B7DE8-L000160](../../agents/research.py#L160) | 160 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000161](../../agents/research.py#L161) | 161 | `")"` | — |
| [SRC-59CF4B7DE8-L000162](../../agents/research.py#L162) | 162 | `"_SEARCH_LEADING_ACTION_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000163](../../agents/research.py#L163) | 163 | `"    r\"^(?:حلّل\|حلل\|اجمع\|قارن\|ناقش\|استكشف\|استقصِ\|و?ميّز\|و?ميز\|اعرض\|و?وضح\|و?وضّح\|و?اذكر(?:ي\|وا)?\|\""` | — |
| [SRC-59CF4B7DE8-L000164](../../agents/research.py#L164) | 164 | `"    r\"analyze\|analyse\|compare\|investigate\|collect\|gather\|review\|summarize\|\""` | — |
| [SRC-59CF4B7DE8-L000165](../../agents/research.py#L165) | 165 | `"    r\"(?:ابحث\|بحث\|دورلي\|دور\|اعثر)(?:\\s+(?:عن\|على))?)\\s+\","` | — |
| [SRC-59CF4B7DE8-L000166](../../agents/research.py#L166) | 166 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000167](../../agents/research.py#L167) | 167 | `")"` | — |
| [SRC-59CF4B7DE8-L000168](../../agents/research.py#L168) | 168 | `""` | — |
| [SRC-59CF4B7DE8-L000169](../../agents/research.py#L169) | 169 | `""` | — |
| [SRC-59CF4B7DE8-L000170](../../agents/research.py#L170) | 170 | `"def compact_search_query(value: Any, limit: int = MAX_QUERY_CHARS) -> str:"` | — |
| [SRC-59CF4B7DE8-L000171](../../agents/research.py#L171) | 171 | `"    \"\"\"Reduce a full request to the topic-bearing query; preserve safety checks elsewhere.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000172](../../agents/research.py#L172) | 172 | `"    if not isinstance(value, str):"` | — |
| [SRC-59CF4B7DE8-L000173](../../agents/research.py#L173) | 173 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000174](../../agents/research.py#L174) | 174 | `"    cleaned = re.sub(r\"https?://[^\\s<>()]+\", \" \", value, flags=re.IGNORECASE)"` | — |
| [SRC-59CF4B7DE8-L000175](../../agents/research.py#L175) | 175 | `"    # Split question/sentence boundaries without splitting operators such as site:reddit.com."` | — |
| [SRC-59CF4B7DE8-L000176](../../agents/research.py#L176) | 176 | `"    segments = re.split("` | — |
| [SRC-59CF4B7DE8-L000177](../../agents/research.py#L177) | 177 | `"        r\"(?<=[!?؟؛;])\\s+\|(?<=\\.)\\s+(?=[A-Z\\u0600-\\u06FF])\","` | — |
| [SRC-59CF4B7DE8-L000178](../../agents/research.py#L178) | 178 | `"        cleaned,"` | — |
| [SRC-59CF4B7DE8-L000179](../../agents/research.py#L179) | 179 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000180](../../agents/research.py#L180) | 180 | `"    useful: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000181](../../agents/research.py#L181) | 181 | `"    for segment in segments:"` | — |
| [SRC-59CF4B7DE8-L000182](../../agents/research.py#L182) | 182 | `"        segment = segment.strip()"` | — |
| [SRC-59CF4B7DE8-L000183](../../agents/research.py#L183) | 183 | `"        if not segment:"` | — |
| [SRC-59CF4B7DE8-L000184](../../agents/research.py#L184) | 184 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000185](../../agents/research.py#L185) | 185 | `"        normalized_segment = re.sub(r\"[\\u064B-\\u065F\\u0670]\", \"\", segment)"` | — |
| [SRC-59CF4B7DE8-L000186](../../agents/research.py#L186) | 186 | `"        normalized_segment = _normalize_arabic(normalized_segment).casefold()"` | — |
| [SRC-59CF4B7DE8-L000187](../../agents/research.py#L187) | 187 | `"        if ("` | — |
| [SRC-59CF4B7DE8-L000188](../../agents/research.py#L188) | 188 | `"            _SEARCH_CITATION_META_START_RE.search(normalized_segment)"` | — |
| [SRC-59CF4B7DE8-L000189](../../agents/research.py#L189) | 189 | `"            or _SEARCH_UNCERTAINTY_META_START_RE.search(normalized_segment)"` | — |
| [SRC-59CF4B7DE8-L000190](../../agents/research.py#L190) | 190 | `"            or _SEARCH_FACTS_INFERENCE_META_ONLY_RE.search(normalized_segment)"` | — |
| [SRC-59CF4B7DE8-L000191](../../agents/research.py#L191) | 191 | `"        ):"` | — |
| [SRC-59CF4B7DE8-L000192](../../agents/research.py#L192) | 192 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000193](../../agents/research.py#L193) | 193 | `"        if _SEARCH_META_START_RE.search(normalized_segment):"` | — |
| [SRC-59CF4B7DE8-L000194](../../agents/research.py#L194) | 194 | `"            # Keep a concrete topic when a \"use multiple sources\" directive"` | — |
| [SRC-59CF4B7DE8-L000195](../../agents/research.py#L195) | 195 | `"            # introduces the subject, but discard standalone formatting clauses."` | — |
| [SRC-59CF4B7DE8-L000196](../../agents/research.py#L196) | 196 | `"            preserved = _SEARCH_TOPIC_PRESERVING_META_PREFIX_RE.sub(\"\", segment, count=1).strip()"` | — |
| [SRC-59CF4B7DE8-L000197](../../agents/research.py#L197) | 197 | `"            if not preserved:"` | — |
| [SRC-59CF4B7DE8-L000198](../../agents/research.py#L198) | 198 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000199](../../agents/research.py#L199) | 199 | `"            if preserved == segment:"` | — |
| [SRC-59CF4B7DE8-L000200](../../agents/research.py#L200) | 200 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000201](../../agents/research.py#L201) | 201 | `"            segment = preserved"` | — |
| [SRC-59CF4B7DE8-L000202](../../agents/research.py#L202) | 202 | `"        segment = _SEARCH_META_TAIL_RE.sub(\"\", segment).strip()"` | — |
| [SRC-59CF4B7DE8-L000203](../../agents/research.py#L203) | 203 | `"        segment = _SEARCH_LEADING_ACTION_RE.sub(\"\", segment).strip()"` | — |
| [SRC-59CF4B7DE8-L000204](../../agents/research.py#L204) | 204 | `"        if segment:"` | — |
| [SRC-59CF4B7DE8-L000205](../../agents/research.py#L205) | 205 | `"            useful.append(segment)"` | — |
| [SRC-59CF4B7DE8-L000206](../../agents/research.py#L206) | 206 | `"    result = re.sub(r\"\\s+\", \" \", \" \".join(useful)).strip(\" \\t\\r\\n,،;؛\")"` | — |
| [SRC-59CF4B7DE8-L000207](../../agents/research.py#L207) | 207 | `"    if not result:"` | — |
| [SRC-59CF4B7DE8-L000208](../../agents/research.py#L208) | 208 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000209](../../agents/research.py#L209) | 209 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000210](../../agents/research.py#L210) | 210 | `"        max_chars = max(2, min(int(limit), MAX_QUERY_CHARS))"` | — |
| [SRC-59CF4B7DE8-L000211](../../agents/research.py#L211) | 211 | `"    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-59CF4B7DE8-L000212](../../agents/research.py#L212) | 212 | `"        max_chars = MAX_QUERY_CHARS"` | — |
| [SRC-59CF4B7DE8-L000213](../../agents/research.py#L213) | 213 | `"    if len(result) > max_chars:"` | — |
| [SRC-59CF4B7DE8-L000214](../../agents/research.py#L214) | 214 | `"        shortened = result[:max_chars]"` | — |
| [SRC-59CF4B7DE8-L000215](../../agents/research.py#L215) | 215 | `"        result = shortened.rsplit(\" \", 1)[0] if \" \" in shortened else shortened"` | — |
| [SRC-59CF4B7DE8-L000216](../../agents/research.py#L216) | 216 | `"    return result"` | — |
| [SRC-59CF4B7DE8-L000217](../../agents/research.py#L217) | 217 | `""` | — |
| [SRC-59CF4B7DE8-L000218](../../agents/research.py#L218) | 218 | `""` | — |
| [SRC-59CF4B7DE8-L000219](../../agents/research.py#L219) | 219 | `"_ARABIC_RE = re.compile(r\"[؀-ۿ]\")"` | — |
| [SRC-59CF4B7DE8-L000220](../../agents/research.py#L220) | 220 | `""` | — |
| [SRC-59CF4B7DE8-L000221](../../agents/research.py#L221) | 221 | `""` | — |
| [SRC-59CF4B7DE8-L000222](../../agents/research.py#L222) | 222 | `"def _normalize_arabic(text: str) -> str:"` | — |
| [SRC-59CF4B7DE8-L000223](../../agents/research.py#L223) | 223 | `"    if not text:"` | — |
| [SRC-59CF4B7DE8-L000224](../../agents/research.py#L224) | 224 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000225](../../agents/research.py#L225) | 225 | `"    return (text.replace(\"\\u0623\", \"\\u0627\")"` | — |
| [SRC-59CF4B7DE8-L000226](../../agents/research.py#L226) | 226 | `"                .replace(\"\\u0625\", \"\\u0627\")"` | — |
| [SRC-59CF4B7DE8-L000227](../../agents/research.py#L227) | 227 | `"                .replace(\"\\u0622\", \"\\u0627\")"` | — |
| [SRC-59CF4B7DE8-L000228](../../agents/research.py#L228) | 228 | `"                .replace(\"\\u0629\", \"\\u0647\")"` | — |
| [SRC-59CF4B7DE8-L000229](../../agents/research.py#L229) | 229 | `"                .replace(\"\\u0649\", \"\\u064a\"))"` | — |
| [SRC-59CF4B7DE8-L000230](../../agents/research.py#L230) | 230 | `""` | — |
| [SRC-59CF4B7DE8-L000231](../../agents/research.py#L231) | 231 | `""` | — |
| [SRC-59CF4B7DE8-L000232](../../agents/research.py#L232) | 232 | `"def _contains_any(text: str, terms: tuple) -> bool:"` | — |
| [SRC-59CF4B7DE8-L000233](../../agents/research.py#L233) | 233 | `"    if not text:"` | — |
| [SRC-59CF4B7DE8-L000234](../../agents/research.py#L234) | 234 | `"        return False"` | — |
| [SRC-59CF4B7DE8-L000235](../../agents/research.py#L235) | 235 | `"    haystack = _normalize_arabic(text.casefold())"` | — |
| [SRC-59CF4B7DE8-L000236](../../agents/research.py#L236) | 236 | `"    for term in terms:"` | — |
| [SRC-59CF4B7DE8-L000237](../../agents/research.py#L237) | 237 | `"        if not term:"` | — |
| [SRC-59CF4B7DE8-L000238](../../agents/research.py#L238) | 238 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000239](../../agents/research.py#L239) | 239 | `"        t = _normalize_arabic(term.casefold())"` | — |
| [SRC-59CF4B7DE8-L000240](../../agents/research.py#L240) | 240 | `"        if _ARABIC_RE.search(t):"` | — |
| [SRC-59CF4B7DE8-L000241](../../agents/research.py#L241) | 241 | `"            if t in haystack:"` | — |
| [SRC-59CF4B7DE8-L000242](../../agents/research.py#L242) | 242 | `"                return True"` | — |
| [SRC-59CF4B7DE8-L000243](../../agents/research.py#L243) | 243 | `"        else:"` | — |
| [SRC-59CF4B7DE8-L000244](../../agents/research.py#L244) | 244 | `"            pat = r\"(?<![a-zA-Z0-9])\" + re.escape(t) + r\"(?![a-zA-Z0-9])\""` | — |
| [SRC-59CF4B7DE8-L000245](../../agents/research.py#L245) | 245 | `"            if re.search(pat, haystack):"` | — |
| [SRC-59CF4B7DE8-L000246](../../agents/research.py#L246) | 246 | `"                return True"` | — |
| [SRC-59CF4B7DE8-L000247](../../agents/research.py#L247) | 247 | `"    return False"` | — |
| [SRC-59CF4B7DE8-L000248](../../agents/research.py#L248) | 248 | `""` | — |
| [SRC-59CF4B7DE8-L000249](../../agents/research.py#L249) | 249 | `""` | — |
| [SRC-59CF4B7DE8-L000250](../../agents/research.py#L250) | 250 | `"def detect_social_focus(question: str, history: list[dict[str, str]] \| None = None) -> bool:"` | — |
| [SRC-59CF4B7DE8-L000251](../../agents/research.py#L251) | 251 | `"    context = question + \" \" + \" \".join("` | — |
| [SRC-59CF4B7DE8-L000252](../../agents/research.py#L252) | 252 | `"        item.get(\"content\", \"\") for item in (history or [])[-4:]"` | — |
| [SRC-59CF4B7DE8-L000253](../../agents/research.py#L253) | 253 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000254](../../agents/research.py#L254) | 254 | `"    return _contains_any(context, _SOCIAL_TERMS)"` | — |
| [SRC-59CF4B7DE8-L000255](../../agents/research.py#L255) | 255 | `""` | — |
| [SRC-59CF4B7DE8-L000256](../../agents/research.py#L256) | 256 | `""` | — |
| [SRC-59CF4B7DE8-L000257](../../agents/research.py#L257) | 257 | `"def detect_freshness(question: str) -> bool:"` | — |
| [SRC-59CF4B7DE8-L000258](../../agents/research.py#L258) | 258 | `"    return _contains_any(question, _FRESH_TERMS)"` | — |
| [SRC-59CF4B7DE8-L000259](../../agents/research.py#L259) | 259 | `""` | — |
| [SRC-59CF4B7DE8-L000260](../../agents/research.py#L260) | 260 | `""` | — |
| [SRC-59CF4B7DE8-L000261](../../agents/research.py#L261) | 261 | `"def detect_depth(question: str) -> str:"` | — |
| [SRC-59CF4B7DE8-L000262](../../agents/research.py#L262) | 262 | `"    return \"deep\" if _contains_any(question, _DEEP_TERMS) else \"standard\""` | — |
| [SRC-59CF4B7DE8-L000263](../../agents/research.py#L263) | 263 | `""` | — |
| [SRC-59CF4B7DE8-L000264](../../agents/research.py#L264) | 264 | `""` | — |
| [SRC-59CF4B7DE8-L000265](../../agents/research.py#L265) | 265 | `"def extract_question_coverage_targets(question: str) -> list[str]:"` | — |
| [SRC-59CF4B7DE8-L000266](../../agents/research.py#L266) | 266 | `"    \"\"\"Extract explicit multi-part requirements; this is a heuristic, not semantic parsing.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000267](../../agents/research.py#L267) | 267 | `"    if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-59CF4B7DE8-L000268](../../agents/research.py#L268) | 268 | `"        return []"` | — |
| [SRC-59CF4B7DE8-L000269](../../agents/research.py#L269) | 269 | `"    text = question.strip()[:4000]"` | — |
| [SRC-59CF4B7DE8-L000270](../../agents/research.py#L270) | 270 | `"    marker = re.compile("` | — |
| [SRC-59CF4B7DE8-L000271](../../agents/research.py#L271) | 271 | `"        r\"(?:من\\s+حيث\|من\\s+ناحية\|من\\s+الناحية\|فيما\\s+يتعلق\\s+ب\|فيما\\s+يخص\|\""` | — |
| [SRC-59CF4B7DE8-L000272](../../agents/research.py#L272) | 272 | `"        r\"من\\s+منظور\|in\\s+terms\\s+of\|with\\s+respect\\s+to\|\""` | — |
| [SRC-59CF4B7DE8-L000273](../../agents/research.py#L273) | 273 | `"        r\"from\\s+the\\s+perspective\\s+of\|based\\s+on\\s+the\\s+following\\s+criteria)\""` | — |
| [SRC-59CF4B7DE8-L000274](../../agents/research.py#L274) | 274 | `"        r\"\\s*(.+?)(?=[؟?!.؛;\\n]\|$)\","` | — |
| [SRC-59CF4B7DE8-L000275](../../agents/research.py#L275) | 275 | `"        flags=re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000276](../../agents/research.py#L276) | 276 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000277](../../agents/research.py#L277) | 277 | `"    match = marker.search(text)"` | — |
| [SRC-59CF4B7DE8-L000278](../../agents/research.py#L278) | 278 | `"    if match:"` | — |
| [SRC-59CF4B7DE8-L000279](../../agents/research.py#L279) | 279 | `"        raw = match.group(1)"` | — |
| [SRC-59CF4B7DE8-L000280](../../agents/research.py#L280) | 280 | `"        raw = re.split("` | — |
| [SRC-59CF4B7DE8-L000281](../../agents/research.py#L281) | 281 | `"            r\"(?:،\|,\|؛\|;)\\s*(?:و?اذكر\|و?وضح\|بيّن\|اشرح\|and\\s+(?:explain\|note\|discuss))\\b\","` | — |
| [SRC-59CF4B7DE8-L000282](../../agents/research.py#L282) | 282 | `"            raw,"` | — |
| [SRC-59CF4B7DE8-L000283](../../agents/research.py#L283) | 283 | `"            maxsplit=1,"` | — |
| [SRC-59CF4B7DE8-L000284](../../agents/research.py#L284) | 284 | `"            flags=re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000285](../../agents/research.py#L285) | 285 | `"        )[0]"` | — |
| [SRC-59CF4B7DE8-L000286](../../agents/research.py#L286) | 286 | `"        pieces = re.split("` | — |
| [SRC-59CF4B7DE8-L000287](../../agents/research.py#L287) | 287 | `"            r\"\\s*(?:،\|,\|؛\|;\|/)\\s*\|\""` | — |
| [SRC-59CF4B7DE8-L000288](../../agents/research.py#L288) | 288 | `"            r\"\\s+\\band\\b\\s+\|\\s+\\bas well as\\b\\s+\|\""` | — |
| [SRC-59CF4B7DE8-L000289](../../agents/research.py#L289) | 289 | `"            r\"\\s+و(?=ال\|[ء-ي])\","` | — |
| [SRC-59CF4B7DE8-L000290](../../agents/research.py#L290) | 290 | `"            raw,"` | — |
| [SRC-59CF4B7DE8-L000291](../../agents/research.py#L291) | 291 | `"            flags=re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000292](../../agents/research.py#L292) | 292 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000293](../../agents/research.py#L293) | 293 | `"    else:"` | — |
| [SRC-59CF4B7DE8-L000294](../../agents/research.py#L294) | 294 | `"        question_parts = ["` | — |
| [SRC-59CF4B7DE8-L000295](../../agents/research.py#L295) | 295 | `"            part.strip(\" \\t\\r\\n-•\")"` | — |
| [SRC-59CF4B7DE8-L000296](../../agents/research.py#L296) | 296 | `"            for part in re.split(r\"[؟?]+\", text)"` | — |
| [SRC-59CF4B7DE8-L000297](../../agents/research.py#L297) | 297 | `"            if len(part.strip(\" \\t\\r\\n-•\")) >= 4"` | — |
| [SRC-59CF4B7DE8-L000298](../../agents/research.py#L298) | 298 | `"        ]"` | — |
| [SRC-59CF4B7DE8-L000299](../../agents/research.py#L299) | 299 | `"        pieces = question_parts if len(question_parts) > 1 else []"` | — |
| [SRC-59CF4B7DE8-L000300](../../agents/research.py#L300) | 300 | `"        # Reuse the shared aspect vocabulary for compound factual questions that do"` | — |
| [SRC-59CF4B7DE8-L000301](../../agents/research.py#L301) | 301 | `"        # not use a formal comparison marker (e.g. capital + population). This is"` | — |
| [SRC-59CF4B7DE8-L000302](../../agents/research.py#L302) | 302 | `"        # deterministic decomposition only; it does not claim semantic verification."` | — |
| [SRC-59CF4B7DE8-L000303](../../agents/research.py#L303) | 303 | `"        if not pieces:"` | — |
| [SRC-59CF4B7DE8-L000304](../../agents/research.py#L304) | 304 | `"            pieces = extract_aspects(text)"` | — |
| [SRC-59CF4B7DE8-L000305](../../agents/research.py#L305) | 305 | `""` | — |
| [SRC-59CF4B7DE8-L000306](../../agents/research.py#L306) | 306 | `"    targets: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000307](../../agents/research.py#L307) | 307 | `"    seen: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000308](../../agents/research.py#L308) | 308 | `"    for piece in pieces:"` | — |
| [SRC-59CF4B7DE8-L000309](../../agents/research.py#L309) | 309 | `"        target = re.sub(r\"^[\\s:،,؛;/.!?\\-–—]+\|[\\s:،,؛;/.!?\\-–—]+$\", \"\", piece).strip()"` | — |
| [SRC-59CF4B7DE8-L000310](../../agents/research.py#L310) | 310 | `"        target = re.sub(r\"^(?:و\\s*)\", \"\", target).strip()"` | — |
| [SRC-59CF4B7DE8-L000311](../../agents/research.py#L311) | 311 | `"        if len(target) < 2:"` | — |
| [SRC-59CF4B7DE8-L000312](../../agents/research.py#L312) | 312 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000313](../../agents/research.py#L313) | 313 | `"        if len(target) > 120:"` | — |
| [SRC-59CF4B7DE8-L000314](../../agents/research.py#L314) | 314 | `"            target = target[:120].rsplit(\" \", 1)[0].strip()"` | — |
| [SRC-59CF4B7DE8-L000315](../../agents/research.py#L315) | 315 | `"        key = _normalize_arabic(compact_search_query(target)).casefold()"` | — |
| [SRC-59CF4B7DE8-L000316](../../agents/research.py#L316) | 316 | `"        if key and key not in seen:"` | — |
| [SRC-59CF4B7DE8-L000317](../../agents/research.py#L317) | 317 | `"            seen.add(key)"` | — |
| [SRC-59CF4B7DE8-L000318](../../agents/research.py#L318) | 318 | `"            targets.append(target)"` | — |
| [SRC-59CF4B7DE8-L000319](../../agents/research.py#L319) | 319 | `"        if len(targets) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000320](../../agents/research.py#L320) | 320 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000321](../../agents/research.py#L321) | 321 | `"    return targets"` | — |
| [SRC-59CF4B7DE8-L000322](../../agents/research.py#L322) | 322 | `""` | — |
| [SRC-59CF4B7DE8-L000323](../../agents/research.py#L323) | 323 | `""` | — |
| [SRC-59CF4B7DE8-L000324](../../agents/research.py#L324) | 324 | `"def build_requirement_queries("` | — |
| [SRC-59CF4B7DE8-L000325](../../agents/research.py#L325) | 325 | `"    base_query: str, targets: list[str] \| None = None"` | — |
| [SRC-59CF4B7DE8-L000326](../../agents/research.py#L326) | 326 | `") -> list[dict[str, str]]:"` | — |
| [SRC-59CF4B7DE8-L000327](../../agents/research.py#L327) | 327 | `"    \"\"\"Create one bounded search query per explicit requirement.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000328](../../agents/research.py#L328) | 328 | `"    if not base_query or not targets:"` | — |
| [SRC-59CF4B7DE8-L000329](../../agents/research.py#L329) | 329 | `"        return []"` | — |
| [SRC-59CF4B7DE8-L000330](../../agents/research.py#L330) | 330 | `"    output: list[dict[str, str]] = []"` | — |
| [SRC-59CF4B7DE8-L000331](../../agents/research.py#L331) | 331 | `"    for target in targets[:MAX_PLAN_QUERIES]:"` | — |
| [SRC-59CF4B7DE8-L000332](../../agents/research.py#L332) | 332 | `"        if not isinstance(target, str) or not target.strip():"` | — |
| [SRC-59CF4B7DE8-L000333](../../agents/research.py#L333) | 333 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000334](../../agents/research.py#L334) | 334 | `"        clean_target = target.strip()[:120]"` | — |
| [SRC-59CF4B7DE8-L000335](../../agents/research.py#L335) | 335 | `"        prefix_limit = max("` | — |
| [SRC-59CF4B7DE8-L000336](../../agents/research.py#L336) | 336 | `"            80,"` | — |
| [SRC-59CF4B7DE8-L000337](../../agents/research.py#L337) | 337 | `"            MAX_QUERY_CHARS - min(len(clean_target), MAX_QUERY_CHARS - 80) - 1,"` | — |
| [SRC-59CF4B7DE8-L000338](../../agents/research.py#L338) | 338 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000339](../../agents/research.py#L339) | 339 | `"        prefix = compact_search_query(base_query, limit=prefix_limit)"` | — |
| [SRC-59CF4B7DE8-L000340](../../agents/research.py#L340) | 340 | `"        query = compact_search_query("` | — |
| [SRC-59CF4B7DE8-L000341](../../agents/research.py#L341) | 341 | `"            f\"{prefix} {clean_target}\", limit=MAX_QUERY_CHARS"` | — |
| [SRC-59CF4B7DE8-L000342](../../agents/research.py#L342) | 342 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000343](../../agents/research.py#L343) | 343 | `"        if query:"` | — |
| [SRC-59CF4B7DE8-L000344](../../agents/research.py#L344) | 344 | `"            output.append({\"target\": clean_target, \"query\": query})"` | — |
| [SRC-59CF4B7DE8-L000345](../../agents/research.py#L345) | 345 | `"    return output"` | — |
| [SRC-59CF4B7DE8-L000346](../../agents/research.py#L346) | 346 | `""` | — |
| [SRC-59CF4B7DE8-L000347](../../agents/research.py#L347) | 347 | `""` | — |
| [SRC-59CF4B7DE8-L000348](../../agents/research.py#L348) | 348 | `""` | — |
| [SRC-59CF4B7DE8-L000349](../../agents/research.py#L349) | 349 | `"def mentioned_social_platforms(text: str) -> list[str]:"` | — |
| [SRC-59CF4B7DE8-L000350](../../agents/research.py#L350) | 350 | `"    rules = ("` | — |
| [SRC-59CF4B7DE8-L000351](../../agents/research.py#L351) | 351 | `"        (\"reddit\", (\"reddit\", \"ريديت\")),"` | — |
| [SRC-59CF4B7DE8-L000352](../../agents/research.py#L352) | 352 | `"        (\"youtube\", (\"youtube\", \"يوتيوب\")),"` | — |
| [SRC-59CF4B7DE8-L000353](../../agents/research.py#L353) | 353 | `"        (\"facebook\", (\"facebook\", \"فيسبوك\", \"فيس بوك\")),"` | — |
| [SRC-59CF4B7DE8-L000354](../../agents/research.py#L354) | 354 | `"        (\"instagram\", (\"instagram\", \"انستجرام\", \"إنستجرام\")),"` | — |
| [SRC-59CF4B7DE8-L000355](../../agents/research.py#L355) | 355 | `"        (\"x\", (\"x.com\", \"twitter\", \"تويتر\", \"اكس\", \"إكس\")),"` | — |
| [SRC-59CF4B7DE8-L000356](../../agents/research.py#L356) | 356 | `"        (\"tiktok\", (\"tiktok\", \"تيك توك\")),"` | — |
| [SRC-59CF4B7DE8-L000357](../../agents/research.py#L357) | 357 | `"        (\"linkedin\", (\"linkedin\", \"لينكدان\", \"لينكدإن\")),"` | — |
| [SRC-59CF4B7DE8-L000358](../../agents/research.py#L358) | 358 | `"        (\"threads\", (\"threads\", \"ثريدز\")),"` | — |
| [SRC-59CF4B7DE8-L000359](../../agents/research.py#L359) | 359 | `"        (\"bluesky\", (\"bluesky\", \"بلو سكاي\")),"` | — |
| [SRC-59CF4B7DE8-L000360](../../agents/research.py#L360) | 360 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000361](../../agents/research.py#L361) | 361 | `"    low = text.casefold()"` | — |
| [SRC-59CF4B7DE8-L000362](../../agents/research.py#L362) | 362 | `"    return [name for name, aliases in rules if any(alias.casefold() in low for alias in aliases)]"` | — |
| [SRC-59CF4B7DE8-L000363](../../agents/research.py#L363) | 363 | `""` | — |
| [SRC-59CF4B7DE8-L000364](../../agents/research.py#L364) | 364 | `""` | — |
| [SRC-59CF4B7DE8-L000365](../../agents/research.py#L365) | 365 | `"def _attach_task_understanding("` | — |
| [SRC-59CF4B7DE8-L000366](../../agents/research.py#L366) | 366 | `"    plan: dict[str, Any],"` | — |
| [SRC-59CF4B7DE8-L000367](../../agents/research.py#L367) | 367 | `"    question: str,"` | — |
| [SRC-59CF4B7DE8-L000368](../../agents/research.py#L368) | 368 | `"    *,"` | — |
| [SRC-59CF4B7DE8-L000369](../../agents/research.py#L369) | 369 | `"    intent_route: str = \"deterministic_fallback\","` | — |
| [SRC-59CF4B7DE8-L000370](../../agents/research.py#L370) | 370 | `"    mode: str = \"auto\","` | — |
| [SRC-59CF4B7DE8-L000371](../../agents/research.py#L371) | 371 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000372](../../agents/research.py#L372) | 372 | `"    \"\"\"Attach deterministic task interpretation and a bounded strategy matrix.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000373](../../agents/research.py#L373) | 373 | `"    result = dict(plan)"` | — |
| [SRC-59CF4B7DE8-L000374](../../agents/research.py#L374) | 374 | `"    spec = build_task_spec("` | — |
| [SRC-59CF4B7DE8-L000375](../../agents/research.py#L375) | 375 | `"        question,"` | — |
| [SRC-59CF4B7DE8-L000376](../../agents/research.py#L376) | 376 | `"        mode=mode,"` | — |
| [SRC-59CF4B7DE8-L000377](../../agents/research.py#L377) | 377 | `"        intent_route=intent_route,"` | — |
| [SRC-59CF4B7DE8-L000378](../../agents/research.py#L378) | 378 | `"        plan=result,"` | — |
| [SRC-59CF4B7DE8-L000379](../../agents/research.py#L379) | 379 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000380](../../agents/research.py#L380) | 380 | `"    matrix = build_query_strategy_matrix("` | — |
| [SRC-59CF4B7DE8-L000381](../../agents/research.py#L381) | 381 | `"        question,"` | — |
| [SRC-59CF4B7DE8-L000382](../../agents/research.py#L382) | 382 | `"        spec,"` | — |
| [SRC-59CF4B7DE8-L000383](../../agents/research.py#L383) | 383 | `"        result.get(\"queries\", []),"` | — |
| [SRC-59CF4B7DE8-L000384](../../agents/research.py#L384) | 384 | `"        limit=MAX_PLAN_QUERIES,"` | — |
| [SRC-59CF4B7DE8-L000385](../../agents/research.py#L385) | 385 | `"        compact_fn=compact_search_query,"` | — |
| [SRC-59CF4B7DE8-L000386](../../agents/research.py#L386) | 386 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000387](../../agents/research.py#L387) | 387 | `"    # This layer records strategies but does not mutate executable queries."` | — |
| [SRC-59CF4B7DE8-L000388](../../agents/research.py#L388) | 388 | `"    # The request runner applies them only after it knows the selected mode and budget."` | — |
| [SRC-59CF4B7DE8-L000389](../../agents/research.py#L389) | 389 | `"    result[\"task_spec\"] = spec"` | — |
| [SRC-59CF4B7DE8-L000390](../../agents/research.py#L390) | 390 | `"    result[\"query_strategy_matrix\"] = matrix"` | — |
| [SRC-59CF4B7DE8-L000391](../../agents/research.py#L391) | 391 | `"    return result"` | — |
| [SRC-59CF4B7DE8-L000392](../../agents/research.py#L392) | 392 | `""` | — |
| [SRC-59CF4B7DE8-L000393](../../agents/research.py#L393) | 393 | `""` | — |
| [SRC-59CF4B7DE8-L000394](../../agents/research.py#L394) | 394 | `"def fallback_plan("` | — |
| [SRC-59CF4B7DE8-L000395](../../agents/research.py#L395) | 395 | `"    question: str, history: list[dict[str, str]] \| None = None"` | — |
| [SRC-59CF4B7DE8-L000396](../../agents/research.py#L396) | 396 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000397](../../agents/research.py#L397) | 397 | `"    \"\"\"Build a small but varied plan when no model planner is configured or parsing fails.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000398](../../agents/research.py#L398) | 398 | `"    contextual_question = resolve_followup_query(question, history)"` | — |
| [SRC-59CF4B7DE8-L000399](../../agents/research.py#L399) | 399 | `"    direct_urls = extract_urls(question)"` | — |
| [SRC-59CF4B7DE8-L000400](../../agents/research.py#L400) | 400 | `"    base = compact_search_query(contextual_question)"` | — |
| [SRC-59CF4B7DE8-L000401](../../agents/research.py#L401) | 401 | `"    coverage_targets = extract_question_coverage_targets(question)"` | — |
| [SRC-59CF4B7DE8-L000402](../../agents/research.py#L402) | 402 | `"    requirement_queries = build_requirement_queries(base, coverage_targets)"` | — |
| [SRC-59CF4B7DE8-L000403](../../agents/research.py#L403) | 403 | `"    social_focus = detect_social_focus(contextual_question)"` | — |
| [SRC-59CF4B7DE8-L000404](../../agents/research.py#L404) | 404 | `"    fresh = detect_freshness(contextual_question)"` | — |
| [SRC-59CF4B7DE8-L000405](../../agents/research.py#L405) | 405 | `"    detected_depth = detect_depth(contextual_question)"` | — |
| [SRC-59CF4B7DE8-L000406](../../agents/research.py#L406) | 406 | `"    deep = detected_depth == \"deep\""` | — |
| [SRC-59CF4B7DE8-L000407](../../agents/research.py#L407) | 407 | `"    platforms = mentioned_social_platforms(contextual_question)"` | — |
| [SRC-59CF4B7DE8-L000408](../../agents/research.py#L408) | 408 | `"    queries: list[str] = [base] if base else []"` | — |
| [SRC-59CF4B7DE8-L000409](../../agents/research.py#L409) | 409 | `""` | — |
| [SRC-59CF4B7DE8-L000410](../../agents/research.py#L410) | 410 | `"    if fresh and base:"` | — |
| [SRC-59CF4B7DE8-L000411](../../agents/research.py#L411) | 411 | `"        queries.append(compact_search_query(base + \" أحدث مستجدات آخر الأخبار\"))"` | — |
| [SRC-59CF4B7DE8-L000412](../../agents/research.py#L412) | 412 | `"    if base and _contains_any(contextual_question, (\"قارن\", \"مقارنة\", \"compare\", \"versus\", \"vs\", \"الفرق بين\")):"` | — |
| [SRC-59CF4B7DE8-L000413](../../agents/research.py#L413) | 413 | `"        queries.append(compact_search_query(base + \" مقارنة مراجعات مميزات عيوب\"))"` | — |
| [SRC-59CF4B7DE8-L000414](../../agents/research.py#L414) | 414 | `""` | — |
| [SRC-59CF4B7DE8-L000415](../../agents/research.py#L415) | 415 | `"    if social_focus and base:"` | — |
| [SRC-59CF4B7DE8-L000416](../../agents/research.py#L416) | 416 | `"        selected = platforms or [\"facebook\", \"instagram\", \"reddit\"]"` | — |
| [SRC-59CF4B7DE8-L000417](../../agents/research.py#L417) | 417 | `"        for platform in selected[:3]:"` | — |
