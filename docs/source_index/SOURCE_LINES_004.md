# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **004**
- سجلات الأسطر: **800**
- النطاق: SRC-5587371288-L000412 إلى SRC-59CF4B7DE8-L000042
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-5587371288 — [agents/intent_router.py](../../agents/intent_router.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-5587371288-L000412](../../agents/intent_router.py#L412) | 412 | `"    question: str,"` | — |
| [SRC-5587371288-L000413](../../agents/intent_router.py#L413) | 413 | `"    history: Any = None,"` | — |
| [SRC-5587371288-L000414](../../agents/intent_router.py#L414) | 414 | `"    mode: str = \"auto\","` | — |
| [SRC-5587371288-L000415](../../agents/intent_router.py#L415) | 415 | `"    *,"` | — |
| [SRC-5587371288-L000416](../../agents/intent_router.py#L416) | 416 | `"    capability_question: bool = False,"` | — |
| [SRC-5587371288-L000417](../../agents/intent_router.py#L417) | 417 | `"    requires_web: bool = False,"` | — |
| [SRC-5587371288-L000418](../../agents/intent_router.py#L418) | 418 | `") -> dict[str, Any]:"` | — |
| [SRC-5587371288-L000419](../../agents/intent_router.py#L419) | 419 | `"    \"\"\"Return a deterministic route and auditable reason for a user question.\"\"\""` | — |
| [SRC-5587371288-L000420](../../agents/intent_router.py#L420) | 420 | `"    clean_mode = mode.strip().lower() if isinstance(mode, str) else \"auto\""` | — |
| [SRC-5587371288-L000421](../../agents/intent_router.py#L421) | 421 | `""` | — |
| [SRC-5587371288-L000422](../../agents/intent_router.py#L422) | 422 | `"    # If the assistant just asked for a missing referent, bind the user's concise"` | — |
| [SRC-5587371288-L000423](../../agents/intent_router.py#L423) | 423 | `"    # reply to that pending question instead of answering the entity name in isolation."` | — |
| [SRC-5587371288-L000424](../../agents/intent_router.py#L424) | 424 | `"    if _is_clarification_answer(question, history):"` | — |
| [SRC-5587371288-L000425](../../agents/intent_router.py#L425) | 425 | `"        return {"` | — |
| [SRC-5587371288-L000426](../../agents/intent_router.py#L426) | 426 | `"            \"route\": \"WEB_DEEP\" if clean_mode == \"deep\" else \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000427](../../agents/intent_router.py#L427) | 427 | `"            \"reason\": \"answer_to_pending_clarification\","` | — |
| [SRC-5587371288-L000428](../../agents/intent_router.py#L428) | 428 | `"            \"context_available\": True,"` | — |
| [SRC-5587371288-L000429](../../agents/intent_router.py#L429) | 429 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000430](../../agents/intent_router.py#L430) | 430 | `"        }"` | — |
| [SRC-5587371288-L000431](../../agents/intent_router.py#L431) | 431 | `""` | — |
| [SRC-5587371288-L000432](../../agents/intent_router.py#L432) | 432 | `"    context_available = _has_context(history)"` | — |
| [SRC-5587371288-L000433](../../agents/intent_router.py#L433) | 433 | `""` | — |
| [SRC-5587371288-L000434](../../agents/intent_router.py#L434) | 434 | `"    # A search mode cannot supply a missing subject. Clarify genuinely elliptical"` | — |
| [SRC-5587371288-L000435](../../agents/intent_router.py#L435) | 435 | `"    # questions before honoring the UI's explicit research mode."` | — |
| [SRC-5587371288-L000436](../../agents/intent_router.py#L436) | 436 | `"    if _needs_clarification(question) and not context_available:"` | — |
| [SRC-5587371288-L000437](../../agents/intent_router.py#L437) | 437 | `"        return {"` | — |
| [SRC-5587371288-L000438](../../agents/intent_router.py#L438) | 438 | `"            \"route\": \"CLARIFY\","` | — |
| [SRC-5587371288-L000439](../../agents/intent_router.py#L439) | 439 | `"            \"reason\": \"missing_referent_and_no_conversation_context\","` | — |
| [SRC-5587371288-L000440](../../agents/intent_router.py#L440) | 440 | `"            \"context_available\": False,"` | — |
| [SRC-5587371288-L000441](../../agents/intent_router.py#L441) | 441 | `"            \"needs_clarification\": True,"` | — |
| [SRC-5587371288-L000442](../../agents/intent_router.py#L442) | 442 | `"        }"` | — |
| [SRC-5587371288-L000443](../../agents/intent_router.py#L443) | 443 | `""` | — |
| [SRC-5587371288-L000444](../../agents/intent_router.py#L444) | 444 | `"    # An explicitly selected mode controls research depth when the request itself"` | — |
| [SRC-5587371288-L000445](../../agents/intent_router.py#L445) | 445 | `"    # is sufficiently specified."` | — |
| [SRC-5587371288-L000446](../../agents/intent_router.py#L446) | 446 | `"    if clean_mode != \"auto\":"` | — |
| [SRC-5587371288-L000447](../../agents/intent_router.py#L447) | 447 | `"        route = \"WEB_DEEP\" if clean_mode == \"deep\" else \"WEB_SIMPLE\""` | — |
| [SRC-5587371288-L000448](../../agents/intent_router.py#L448) | 448 | `"        return {"` | — |
| [SRC-5587371288-L000449](../../agents/intent_router.py#L449) | 449 | `"            \"route\": route,"` | — |
| [SRC-5587371288-L000450](../../agents/intent_router.py#L450) | 450 | `"            \"reason\": \"explicit_mode\","` | — |
| [SRC-5587371288-L000451](../../agents/intent_router.py#L451) | 451 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000452](../../agents/intent_router.py#L452) | 452 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000453](../../agents/intent_router.py#L453) | 453 | `"        }"` | — |
| [SRC-5587371288-L000454](../../agents/intent_router.py#L454) | 454 | `""` | — |
| [SRC-5587371288-L000455](../../agents/intent_router.py#L455) | 455 | `"    if capability_question:"` | — |
| [SRC-5587371288-L000456](../../agents/intent_router.py#L456) | 456 | `"        return {"` | — |
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

### FILE-9D8012A1A0 — [agents/memory_bank.py](../../agents/memory_bank.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-9D8012A1A0-L000001](../../agents/memory_bank.py#L1) | 1 | `"\"\"\"Structured claim–evidence memory bank for Omarai."` | — |
| [SRC-9D8012A1A0-L000002](../../agents/memory_bank.py#L2) | 2 | `""` | — |
| [SRC-9D8012A1A0-L000003](../../agents/memory_bank.py#L3) | 3 | `"Every generated claim can be bound to one or more evidence snippets with a"` | — |
| [SRC-9D8012A1A0-L000004](../../agents/memory_bank.py#L4) | 4 | `"stable evidence_id. Generation should be constrained by this graph so fluency"` | — |
| [SRC-9D8012A1A0-L000005](../../agents/memory_bank.py#L5) | 5 | `"never outruns support."` | — |
| [SRC-9D8012A1A0-L000006](../../agents/memory_bank.py#L6) | 6 | `""` | — |
| [SRC-9D8012A1A0-L000007](../../agents/memory_bank.py#L7) | 7 | `"Lexical support ≠ semantic entailment. Status labels are honest about that."` | — |
| [SRC-9D8012A1A0-L000008](../../agents/memory_bank.py#L8) | 8 | `""` | — |
| [SRC-9D8012A1A0-L000009](../../agents/memory_bank.py#L9) | 9 | `"Compatible conceptually with agents.claim_evidence.build_claim_evidence_ledger"` | — |
| [SRC-9D8012A1A0-L000010](../../agents/memory_bank.py#L10) | 10 | `"(sentence-level citation index tracing on main)."` | — |
| [SRC-9D8012A1A0-L000011](../../agents/memory_bank.py#L11) | 11 | `"\"\"\""` | — |
| [SRC-9D8012A1A0-L000012](../../agents/memory_bank.py#L12) | 12 | `"from __future__ import annotations"` | — |
| [SRC-9D8012A1A0-L000013](../../agents/memory_bank.py#L13) | 13 | `""` | — |
| [SRC-9D8012A1A0-L000014](../../agents/memory_bank.py#L14) | 14 | `"import hashlib"` | — |
| [SRC-9D8012A1A0-L000015](../../agents/memory_bank.py#L15) | 15 | `"import re"` | — |
| [SRC-9D8012A1A0-L000016](../../agents/memory_bank.py#L16) | 16 | `"import time"` | — |
| [SRC-9D8012A1A0-L000017](../../agents/memory_bank.py#L17) | 17 | `"from dataclasses import asdict, dataclass, field"` | — |
| [SRC-9D8012A1A0-L000018](../../agents/memory_bank.py#L18) | 18 | `"from typing import Any"` | — |
| [SRC-9D8012A1A0-L000019](../../agents/memory_bank.py#L19) | 19 | `""` | — |
| [SRC-9D8012A1A0-L000020](../../agents/memory_bank.py#L20) | 20 | `"_TOKEN = re.compile(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", re.I)"` | — |
| [SRC-9D8012A1A0-L000021](../../agents/memory_bank.py#L21) | 21 | `"_SENTENCE_SPLIT = re.compile(r\"(?<=[.!?؟])\\s+\|\\n+\")"` | — |
| [SRC-9D8012A1A0-L000022](../../agents/memory_bank.py#L22) | 22 | `"_CITATION_MARK = re.compile(r\"\\[(?:المصدر\|source)\\s+(\\d+)\\]\", re.I)"` | — |
| [SRC-9D8012A1A0-L000023](../../agents/memory_bank.py#L23) | 23 | `"_STOP = {"` | — |
| [SRC-9D8012A1A0-L000024](../../agents/memory_bank.py#L24) | 24 | `"    \"من\", \"في\", \"على\", \"عن\", \"الى\", \"و\", \"او\", \"هل\", \"ما\", \"ال\", \"the\", \"a\", \"an\","` | — |
| [SRC-9D8012A1A0-L000025](../../agents/memory_bank.py#L25) | 25 | `"    \"and\", \"or\", \"in\", \"on\", \"of\", \"to\", \"for\", \"with\", \"is\", \"are\", \"this\", \"that\","` | — |
| [SRC-9D8012A1A0-L000026](../../agents/memory_bank.py#L26) | 26 | `"    \"إلى\", \"أن\", \"إن\", \"كان\", \"يكون\", \"غير\", \"بين\", \"حتى\", \"قد\", \"لم\", \"لن\","` | — |
| [SRC-9D8012A1A0-L000027](../../agents/memory_bank.py#L27) | 27 | `"}"` | — |
| [SRC-9D8012A1A0-L000028](../../agents/memory_bank.py#L28) | 28 | `""` | — |
| [SRC-9D8012A1A0-L000029](../../agents/memory_bank.py#L29) | 29 | `""` | — |
| [SRC-9D8012A1A0-L000030](../../agents/memory_bank.py#L30) | 30 | `"def _norm(text: str) -> str:"` | — |
| [SRC-9D8012A1A0-L000031](../../agents/memory_bank.py#L31) | 31 | `"    text = (text or \"\").casefold()"` | — |
| [SRC-9D8012A1A0-L000032](../../agents/memory_bank.py#L32) | 32 | `"    text = text.translate(str.maketrans({\"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ة\": \"ه\", \"ى\": \"ي\"}))"` | — |
| [SRC-9D8012A1A0-L000033](../../agents/memory_bank.py#L33) | 33 | `"    return re.sub(r\"\\s+\", \" \", text).strip()"` | — |
| [SRC-9D8012A1A0-L000034](../../agents/memory_bank.py#L34) | 34 | `""` | — |
| [SRC-9D8012A1A0-L000035](../../agents/memory_bank.py#L35) | 35 | `""` | — |
| [SRC-9D8012A1A0-L000036](../../agents/memory_bank.py#L36) | 36 | `"def _tokens(text: str) -> set[str]:"` | — |
| [SRC-9D8012A1A0-L000037](../../agents/memory_bank.py#L37) | 37 | `"    return {t for t in _TOKEN.findall(_norm(text)) if len(t) >= 2 and t not in _STOP}"` | — |
| [SRC-9D8012A1A0-L000038](../../agents/memory_bank.py#L38) | 38 | `""` | — |
| [SRC-9D8012A1A0-L000039](../../agents/memory_bank.py#L39) | 39 | `""` | — |
| [SRC-9D8012A1A0-L000040](../../agents/memory_bank.py#L40) | 40 | `"def _evidence_id(url: str, snippet: str) -> str:"` | — |
| [SRC-9D8012A1A0-L000041](../../agents/memory_bank.py#L41) | 41 | `"    raw = f\"{url}\|{snippet[:160]}\".encode(\"utf-8\", errors=\"replace\")"` | — |
| [SRC-9D8012A1A0-L000042](../../agents/memory_bank.py#L42) | 42 | `"    return \"ev_\" + hashlib.sha1(raw).hexdigest()[:12]"` | — |
| [SRC-9D8012A1A0-L000043](../../agents/memory_bank.py#L43) | 43 | `""` | — |
| [SRC-9D8012A1A0-L000044](../../agents/memory_bank.py#L44) | 44 | `""` | — |
| [SRC-9D8012A1A0-L000045](../../agents/memory_bank.py#L45) | 45 | `"def _claim_id(text: str) -> str:"` | — |
| [SRC-9D8012A1A0-L000046](../../agents/memory_bank.py#L46) | 46 | `"    return \"cl_\" + hashlib.sha1((text or \"\").encode(\"utf-8\", errors=\"replace\")).hexdigest()[:10]"` | — |
| [SRC-9D8012A1A0-L000047](../../agents/memory_bank.py#L47) | 47 | `""` | — |
| [SRC-9D8012A1A0-L000048](../../agents/memory_bank.py#L48) | 48 | `""` | — |
| [SRC-9D8012A1A0-L000049](../../agents/memory_bank.py#L49) | 49 | `"@dataclass"` | — |
| [SRC-9D8012A1A0-L000050](../../agents/memory_bank.py#L50) | 50 | `"class Evidence:"` | — |
| [SRC-9D8012A1A0-L000051](../../agents/memory_bank.py#L51) | 51 | `"    evidence_id: str"` | — |
| [SRC-9D8012A1A0-L000052](../../agents/memory_bank.py#L52) | 52 | `"    url: str"` | — |
| [SRC-9D8012A1A0-L000053](../../agents/memory_bank.py#L53) | 53 | `"    title: str"` | — |
| [SRC-9D8012A1A0-L000054](../../agents/memory_bank.py#L54) | 54 | `"    snippet: str"` | — |
| [SRC-9D8012A1A0-L000055](../../agents/memory_bank.py#L55) | 55 | `"    provider: str = \"\""` | — |
| [SRC-9D8012A1A0-L000056](../../agents/memory_bank.py#L56) | 56 | `"    source_class: str = \"web\""` | — |
| [SRC-9D8012A1A0-L000057](../../agents/memory_bank.py#L57) | 57 | `"    page_fetched: bool = False"` | — |
| [SRC-9D8012A1A0-L000058](../../agents/memory_bank.py#L58) | 58 | `"    source_index: int = 0"` | — |
| [SRC-9D8012A1A0-L000059](../../agents/memory_bank.py#L59) | 59 | `""` | — |
| [SRC-9D8012A1A0-L000060](../../agents/memory_bank.py#L60) | 60 | `"    def to_dict(self) -> dict[str, Any]:"` | — |
| [SRC-9D8012A1A0-L000061](../../agents/memory_bank.py#L61) | 61 | `"        return asdict(self)"` | — |
| [SRC-9D8012A1A0-L000062](../../agents/memory_bank.py#L62) | 62 | `""` | — |
| [SRC-9D8012A1A0-L000063](../../agents/memory_bank.py#L63) | 63 | `"    @property"` | — |
| [SRC-9D8012A1A0-L000064](../../agents/memory_bank.py#L64) | 64 | `"    def readable(self) -> bool:"` | — |
| [SRC-9D8012A1A0-L000065](../../agents/memory_bank.py#L65) | 65 | `"        return bool(self.snippet.strip()) or self.page_fetched"` | — |
| [SRC-9D8012A1A0-L000066](../../agents/memory_bank.py#L66) | 66 | `""` | — |
| [SRC-9D8012A1A0-L000067](../../agents/memory_bank.py#L67) | 67 | `""` | — |
| [SRC-9D8012A1A0-L000068](../../agents/memory_bank.py#L68) | 68 | `"@dataclass"` | — |
| [SRC-9D8012A1A0-L000069](../../agents/memory_bank.py#L69) | 69 | `"class Claim:"` | — |
| [SRC-9D8012A1A0-L000070](../../agents/memory_bank.py#L70) | 70 | `"    claim_id: str"` | — |
| [SRC-9D8012A1A0-L000071](../../agents/memory_bank.py#L71) | 71 | `"    text: str"` | — |
| [SRC-9D8012A1A0-L000072](../../agents/memory_bank.py#L72) | 72 | `"    evidence_ids: list[str] = field(default_factory=list)"` | — |
| [SRC-9D8012A1A0-L000073](../../agents/memory_bank.py#L73) | 73 | `"    support_score: float = 0.0"` | — |
| [SRC-9D8012A1A0-L000074](../../agents/memory_bank.py#L74) | 74 | `"    status: str = \"unsupported\""` | — |
| [SRC-9D8012A1A0-L000075](../../agents/memory_bank.py#L75) | 75 | `"    aspect: str = \"\""` | — |
| [SRC-9D8012A1A0-L000076](../../agents/memory_bank.py#L76) | 76 | `""` | — |
| [SRC-9D8012A1A0-L000077](../../agents/memory_bank.py#L77) | 77 | `"    def to_dict(self) -> dict[str, Any]:"` | — |
| [SRC-9D8012A1A0-L000078](../../agents/memory_bank.py#L78) | 78 | `"        return asdict(self)"` | — |
| [SRC-9D8012A1A0-L000079](../../agents/memory_bank.py#L79) | 79 | `""` | — |
| [SRC-9D8012A1A0-L000080](../../agents/memory_bank.py#L80) | 80 | `""` | — |
| [SRC-9D8012A1A0-L000081](../../agents/memory_bank.py#L81) | 81 | `"class MemoryBank:"` | — |
| [SRC-9D8012A1A0-L000082](../../agents/memory_bank.py#L82) | 82 | `"    \"\"\"In-session claim↔evidence graph for agentic RAG.\"\"\""` | — |
| [SRC-9D8012A1A0-L000083](../../agents/memory_bank.py#L83) | 83 | `""` | — |
| [SRC-9D8012A1A0-L000084](../../agents/memory_bank.py#L84) | 84 | `"    def __init__(self, session_id: str = \"\") -> None:"` | — |
| [SRC-9D8012A1A0-L000085](../../agents/memory_bank.py#L85) | 85 | `"        self.session_id = session_id or f\"s_{int(time.time())}\""` | — |
| [SRC-9D8012A1A0-L000086](../../agents/memory_bank.py#L86) | 86 | `"        self.evidence: dict[str, Evidence] = {}"` | — |
| [SRC-9D8012A1A0-L000087](../../agents/memory_bank.py#L87) | 87 | `"        self.claims: list[Claim] = []"` | — |
| [SRC-9D8012A1A0-L000088](../../agents/memory_bank.py#L88) | 88 | `"        self.notes: list[str] = []"` | — |
| [SRC-9D8012A1A0-L000089](../../agents/memory_bank.py#L89) | 89 | `"        self._index_by_id: dict[str, int] = {}"` | — |
| [SRC-9D8012A1A0-L000090](../../agents/memory_bank.py#L90) | 90 | `""` | — |
| [SRC-9D8012A1A0-L000091](../../agents/memory_bank.py#L91) | 91 | `"    def ingest_sources(self, sources: list[dict[str, Any]] \| None) -> int:"` | — |
| [SRC-9D8012A1A0-L000092](../../agents/memory_bank.py#L92) | 92 | `"        added = 0"` | — |
| [SRC-9D8012A1A0-L000093](../../agents/memory_bank.py#L93) | 93 | `"        for src in sources or []:"` | — |
| [SRC-9D8012A1A0-L000094](../../agents/memory_bank.py#L94) | 94 | `"            if not isinstance(src, dict):"` | — |
| [SRC-9D8012A1A0-L000095](../../agents/memory_bank.py#L95) | 95 | `"                continue"` | — |
| [SRC-9D8012A1A0-L000096](../../agents/memory_bank.py#L96) | 96 | `"            url = str(src.get(\"url\") or \"\").strip()"` | — |
| [SRC-9D8012A1A0-L000097](../../agents/memory_bank.py#L97) | 97 | `"            title = str(src.get(\"title\") or \"\").strip()"` | — |
| [SRC-9D8012A1A0-L000098](../../agents/memory_bank.py#L98) | 98 | `"            snippet = str("` | — |
| [SRC-9D8012A1A0-L000099](../../agents/memory_bank.py#L99) | 99 | `"                src.get(\"snippet\") or src.get(\"page_text\") or src.get(\"content\") or \"\""` | — |
| [SRC-9D8012A1A0-L000100](../../agents/memory_bank.py#L100) | 100 | `"            ).strip()"` | — |
| [SRC-9D8012A1A0-L000101](../../agents/memory_bank.py#L101) | 101 | `"            if not url and not snippet and not title:"` | — |
| [SRC-9D8012A1A0-L000102](../../agents/memory_bank.py#L102) | 102 | `"                continue"` | — |
| [SRC-9D8012A1A0-L000103](../../agents/memory_bank.py#L103) | 103 | `"            eid = _evidence_id(url, snippet or title)"` | — |
| [SRC-9D8012A1A0-L000104](../../agents/memory_bank.py#L104) | 104 | `"            if eid in self.evidence:"` | — |
| [SRC-9D8012A1A0-L000105](../../agents/memory_bank.py#L105) | 105 | `"                continue"` | — |
| [SRC-9D8012A1A0-L000106](../../agents/memory_bank.py#L106) | 106 | `"            idx = len(self.evidence) + 1"` | — |
| [SRC-9D8012A1A0-L000107](../../agents/memory_bank.py#L107) | 107 | `"            self.evidence[eid] = Evidence("` | — |
| [SRC-9D8012A1A0-L000108](../../agents/memory_bank.py#L108) | 108 | `"                evidence_id=eid,"` | — |
| [SRC-9D8012A1A0-L000109](../../agents/memory_bank.py#L109) | 109 | `"                url=url[:2048],"` | — |
| [SRC-9D8012A1A0-L000110](../../agents/memory_bank.py#L110) | 110 | `"                title=title[:300],"` | — |
| [SRC-9D8012A1A0-L000111](../../agents/memory_bank.py#L111) | 111 | `"                snippet=(snippet or title)[:1600],"` | — |
| [SRC-9D8012A1A0-L000112](../../agents/memory_bank.py#L112) | 112 | `"                provider=str("` | — |
| [SRC-9D8012A1A0-L000113](../../agents/memory_bank.py#L113) | 113 | `"                    src.get(\"provider\")"` | — |
| [SRC-9D8012A1A0-L000114](../../agents/memory_bank.py#L114) | 114 | `"                    or (src.get(\"providers\") or [\"\"])[0]"` | — |
| [SRC-9D8012A1A0-L000115](../../agents/memory_bank.py#L115) | 115 | `"                    or \"\""` | — |
| [SRC-9D8012A1A0-L000116](../../agents/memory_bank.py#L116) | 116 | `"                )[:80],"` | — |
| [SRC-9D8012A1A0-L000117](../../agents/memory_bank.py#L117) | 117 | `"                source_class=str(src.get(\"source_class\") or \"web\")[:40],"` | — |
| [SRC-9D8012A1A0-L000118](../../agents/memory_bank.py#L118) | 118 | `"                page_fetched=bool(src.get(\"page_fetched\")),"` | — |
| [SRC-9D8012A1A0-L000119](../../agents/memory_bank.py#L119) | 119 | `"                source_index=idx,"` | — |
| [SRC-9D8012A1A0-L000120](../../agents/memory_bank.py#L120) | 120 | `"            )"` | — |
| [SRC-9D8012A1A0-L000121](../../agents/memory_bank.py#L121) | 121 | `"            self._index_by_id[eid] = idx"` | — |
| [SRC-9D8012A1A0-L000122](../../agents/memory_bank.py#L122) | 122 | `"            added += 1"` | — |
| [SRC-9D8012A1A0-L000123](../../agents/memory_bank.py#L123) | 123 | `"        return added"` | — |
| [SRC-9D8012A1A0-L000124](../../agents/memory_bank.py#L124) | 124 | `""` | — |
| [SRC-9D8012A1A0-L000125](../../agents/memory_bank.py#L125) | 125 | `"    def _score_claim_against(self, claim_text: str, ev: Evidence) -> float:"` | — |
| [SRC-9D8012A1A0-L000126](../../agents/memory_bank.py#L126) | 126 | `"        ct = _tokens(claim_text)"` | — |
| [SRC-9D8012A1A0-L000127](../../agents/memory_bank.py#L127) | 127 | `"        et = _tokens(f\"{ev.title} {ev.snippet}\")"` | — |
| [SRC-9D8012A1A0-L000128](../../agents/memory_bank.py#L128) | 128 | `"        if not ct or not et:"` | — |
| [SRC-9D8012A1A0-L000129](../../agents/memory_bank.py#L129) | 129 | `"            return 0.0"` | — |
| [SRC-9D8012A1A0-L000130](../../agents/memory_bank.py#L130) | 130 | `"        return len(ct & et) / max(1, len(ct))"` | — |
| [SRC-9D8012A1A0-L000131](../../agents/memory_bank.py#L131) | 131 | `""` | — |
| [SRC-9D8012A1A0-L000132](../../agents/memory_bank.py#L132) | 132 | `"    def bind_claim("` | — |
| [SRC-9D8012A1A0-L000133](../../agents/memory_bank.py#L133) | 133 | `"        self,"` | — |
| [SRC-9D8012A1A0-L000134](../../agents/memory_bank.py#L134) | 134 | `"        text: str,"` | — |
| [SRC-9D8012A1A0-L000135](../../agents/memory_bank.py#L135) | 135 | `"        *,"` | — |
| [SRC-9D8012A1A0-L000136](../../agents/memory_bank.py#L136) | 136 | `"        min_score: float = 0.25,"` | — |
| [SRC-9D8012A1A0-L000137](../../agents/memory_bank.py#L137) | 137 | `"        aspect: str = \"\","` | — |
| [SRC-9D8012A1A0-L000138](../../agents/memory_bank.py#L138) | 138 | `"        top_k: int = 3,"` | — |
| [SRC-9D8012A1A0-L000139](../../agents/memory_bank.py#L139) | 139 | `"    ) -> Claim:"` | — |
| [SRC-9D8012A1A0-L000140](../../agents/memory_bank.py#L140) | 140 | `"        text = re.sub(r\"\\s+\", \" \", (text or \"\").strip())"` | — |
| [SRC-9D8012A1A0-L000141](../../agents/memory_bank.py#L141) | 141 | `"        clean = _CITATION_MARK.sub(\"\", text).strip()"` | — |
| [SRC-9D8012A1A0-L000142](../../agents/memory_bank.py#L142) | 142 | `"        cid = _claim_id(clean)"` | — |
| [SRC-9D8012A1A0-L000143](../../agents/memory_bank.py#L143) | 143 | `"        scored: list[tuple[float, str]] = []"` | — |
| [SRC-9D8012A1A0-L000144](../../agents/memory_bank.py#L144) | 144 | `"        for eid, ev in self.evidence.items():"` | — |
| [SRC-9D8012A1A0-L000145](../../agents/memory_bank.py#L145) | 145 | `"            s = self._score_claim_against(clean, ev)"` | — |
| [SRC-9D8012A1A0-L000146](../../agents/memory_bank.py#L146) | 146 | `"            if s >= min_score:"` | — |
| [SRC-9D8012A1A0-L000147](../../agents/memory_bank.py#L147) | 147 | `"                scored.append((s, eid))"` | — |
| [SRC-9D8012A1A0-L000148](../../agents/memory_bank.py#L148) | 148 | `"        scored.sort(reverse=True)"` | — |
| [SRC-9D8012A1A0-L000149](../../agents/memory_bank.py#L149) | 149 | `"        top = scored[: max(1, min(int(top_k), 5))]"` | — |
| [SRC-9D8012A1A0-L000150](../../agents/memory_bank.py#L150) | 150 | `"        score = top[0][0] if top else 0.0"` | — |
| [SRC-9D8012A1A0-L000151](../../agents/memory_bank.py#L151) | 151 | `"        if score >= 0.45:"` | — |
| [SRC-9D8012A1A0-L000152](../../agents/memory_bank.py#L152) | 152 | `"            status = \"supported\""` | — |
| [SRC-9D8012A1A0-L000153](../../agents/memory_bank.py#L153) | 153 | `"        elif score >= min_score:"` | — |
| [SRC-9D8012A1A0-L000154](../../agents/memory_bank.py#L154) | 154 | `"            status = \"weak\""` | — |
| [SRC-9D8012A1A0-L000155](../../agents/memory_bank.py#L155) | 155 | `"        else:"` | — |
| [SRC-9D8012A1A0-L000156](../../agents/memory_bank.py#L156) | 156 | `"            status = \"unsupported\""` | — |
| [SRC-9D8012A1A0-L000157](../../agents/memory_bank.py#L157) | 157 | `"        claim = Claim("` | — |
| [SRC-9D8012A1A0-L000158](../../agents/memory_bank.py#L158) | 158 | `"            claim_id=cid,"` | — |
| [SRC-9D8012A1A0-L000159](../../agents/memory_bank.py#L159) | 159 | `"            text=clean[:500],"` | — |
| [SRC-9D8012A1A0-L000160](../../agents/memory_bank.py#L160) | 160 | `"            evidence_ids=[eid for _, eid in top],"` | — |
| [SRC-9D8012A1A0-L000161](../../agents/memory_bank.py#L161) | 161 | `"            support_score=round(score, 3),"` | — |
| [SRC-9D8012A1A0-L000162](../../agents/memory_bank.py#L162) | 162 | `"            status=status,"` | — |
| [SRC-9D8012A1A0-L000163](../../agents/memory_bank.py#L163) | 163 | `"            aspect=str(aspect or \"\")[:80],"` | — |
| [SRC-9D8012A1A0-L000164](../../agents/memory_bank.py#L164) | 164 | `"        )"` | — |
| [SRC-9D8012A1A0-L000165](../../agents/memory_bank.py#L165) | 165 | `"        self.claims.append(claim)"` | — |
| [SRC-9D8012A1A0-L000166](../../agents/memory_bank.py#L166) | 166 | `"        return claim"` | — |
| [SRC-9D8012A1A0-L000167](../../agents/memory_bank.py#L167) | 167 | `""` | — |
| [SRC-9D8012A1A0-L000168](../../agents/memory_bank.py#L168) | 168 | `"    def bind_answer("` | — |
| [SRC-9D8012A1A0-L000169](../../agents/memory_bank.py#L169) | 169 | `"        self,"` | — |
| [SRC-9D8012A1A0-L000170](../../agents/memory_bank.py#L170) | 170 | `"        answer: str,"` | — |
| [SRC-9D8012A1A0-L000171](../../agents/memory_bank.py#L171) | 171 | `"        *,"` | — |
| [SRC-9D8012A1A0-L000172](../../agents/memory_bank.py#L172) | 172 | `"        min_score: float = 0.25,"` | — |
| [SRC-9D8012A1A0-L000173](../../agents/memory_bank.py#L173) | 173 | `"        aspects: list[str] \| None = None,"` | — |
| [SRC-9D8012A1A0-L000174](../../agents/memory_bank.py#L174) | 174 | `"    ) -> list[Claim]:"` | — |
| [SRC-9D8012A1A0-L000175](../../agents/memory_bank.py#L175) | 175 | `"        sentences = split_answer_into_claim_sentences(answer)"` | — |
| [SRC-9D8012A1A0-L000176](../../agents/memory_bank.py#L176) | 176 | `"        bound: list[Claim] = []"` | — |
| [SRC-9D8012A1A0-L000177](../../agents/memory_bank.py#L177) | 177 | `"        aspect_list = list(aspects or [])"` | — |
| [SRC-9D8012A1A0-L000178](../../agents/memory_bank.py#L178) | 178 | `"        for i, sentence in enumerate(sentences):"` | — |
| [SRC-9D8012A1A0-L000179](../../agents/memory_bank.py#L179) | 179 | `"            aspect = aspect_list[i] if i < len(aspect_list) else \"\""` | — |
| [SRC-9D8012A1A0-L000180](../../agents/memory_bank.py#L180) | 180 | `"            if not aspect:"` | — |
| [SRC-9D8012A1A0-L000181](../../agents/memory_bank.py#L181) | 181 | `"                for a in aspect_list:"` | — |
| [SRC-9D8012A1A0-L000182](../../agents/memory_bank.py#L182) | 182 | `"                    if a and a.casefold() in sentence.casefold():"` | — |
| [SRC-9D8012A1A0-L000183](../../agents/memory_bank.py#L183) | 183 | `"                        aspect = a"` | — |
| [SRC-9D8012A1A0-L000184](../../agents/memory_bank.py#L184) | 184 | `"                        break"` | — |
| [SRC-9D8012A1A0-L000185](../../agents/memory_bank.py#L185) | 185 | `"            bound.append(self.bind_claim(sentence, min_score=min_score, aspect=aspect))"` | — |
| [SRC-9D8012A1A0-L000186](../../agents/memory_bank.py#L186) | 186 | `"        return bound"` | — |
| [SRC-9D8012A1A0-L000187](../../agents/memory_bank.py#L187) | 187 | `""` | — |
| [SRC-9D8012A1A0-L000188](../../agents/memory_bank.py#L188) | 188 | `"    def format_claim_with_citations(self, claim: Claim) -> str:"` | — |
| [SRC-9D8012A1A0-L000189](../../agents/memory_bank.py#L189) | 189 | `"        if not claim.evidence_ids:"` | — |
| [SRC-9D8012A1A0-L000190](../../agents/memory_bank.py#L190) | 190 | `"            return claim.text"` | — |
| [SRC-9D8012A1A0-L000191](../../agents/memory_bank.py#L191) | 191 | `"        markers: list[str] = []"` | — |
| [SRC-9D8012A1A0-L000192](../../agents/memory_bank.py#L192) | 192 | `"        for eid in claim.evidence_ids:"` | — |
| [SRC-9D8012A1A0-L000193](../../agents/memory_bank.py#L193) | 193 | `"            idx = self._index_by_id.get(eid)"` | — |
| [SRC-9D8012A1A0-L000194](../../agents/memory_bank.py#L194) | 194 | `"            if idx:"` | — |
| [SRC-9D8012A1A0-L000195](../../agents/memory_bank.py#L195) | 195 | `"                markers.append(f\"[المصدر {idx}]\")"` | — |
| [SRC-9D8012A1A0-L000196](../../agents/memory_bank.py#L196) | 196 | `"        if not markers:"` | — |
| [SRC-9D8012A1A0-L000197](../../agents/memory_bank.py#L197) | 197 | `"            return claim.text"` | — |
| [SRC-9D8012A1A0-L000198](../../agents/memory_bank.py#L198) | 198 | `"        return f\"{claim.text} {' '.join(dict.fromkeys(markers))}\""` | — |
| [SRC-9D8012A1A0-L000199](../../agents/memory_bank.py#L199) | 199 | `""` | — |
| [SRC-9D8012A1A0-L000200](../../agents/memory_bank.py#L200) | 200 | `"    def render_supported_answer(self, *, drop_unsupported: bool = True) -> str:"` | — |
| [SRC-9D8012A1A0-L000201](../../agents/memory_bank.py#L201) | 201 | `"        lines: list[str] = []"` | — |
| [SRC-9D8012A1A0-L000202](../../agents/memory_bank.py#L202) | 202 | `"        for claim in self.claims:"` | — |
| [SRC-9D8012A1A0-L000203](../../agents/memory_bank.py#L203) | 203 | `"            if drop_unsupported and claim.status == \"unsupported\":"` | — |
| [SRC-9D8012A1A0-L000204](../../agents/memory_bank.py#L204) | 204 | `"                continue"` | — |
| [SRC-9D8012A1A0-L000205](../../agents/memory_bank.py#L205) | 205 | `"            lines.append(self.format_claim_with_citations(claim))"` | — |
| [SRC-9D8012A1A0-L000206](../../agents/memory_bank.py#L206) | 206 | `"        return \"\\n\".join(lines)"` | — |
| [SRC-9D8012A1A0-L000207](../../agents/memory_bank.py#L207) | 207 | `""` | — |
| [SRC-9D8012A1A0-L000208](../../agents/memory_bank.py#L208) | 208 | `"    def citation_map(self) -> list[dict[str, Any]]:"` | — |
| [SRC-9D8012A1A0-L000209](../../agents/memory_bank.py#L209) | 209 | `"        rows = []"` | — |
| [SRC-9D8012A1A0-L000210](../../agents/memory_bank.py#L210) | 210 | `"        for eid, ev in self.evidence.items():"` | — |
| [SRC-9D8012A1A0-L000211](../../agents/memory_bank.py#L211) | 211 | `"            rows.append({"` | — |
| [SRC-9D8012A1A0-L000212](../../agents/memory_bank.py#L212) | 212 | `"                \"index\": ev.source_index or self._index_by_id.get(eid, 0),"` | — |
| [SRC-9D8012A1A0-L000213](../../agents/memory_bank.py#L213) | 213 | `"                \"evidence_id\": eid,"` | — |
| [SRC-9D8012A1A0-L000214](../../agents/memory_bank.py#L214) | 214 | `"                \"title\": ev.title,"` | — |
| [SRC-9D8012A1A0-L000215](../../agents/memory_bank.py#L215) | 215 | `"                \"url\": ev.url,"` | — |
| [SRC-9D8012A1A0-L000216](../../agents/memory_bank.py#L216) | 216 | `"                \"provider\": ev.provider,"` | — |
| [SRC-9D8012A1A0-L000217](../../agents/memory_bank.py#L217) | 217 | `"                \"source_class\": ev.source_class,"` | — |
| [SRC-9D8012A1A0-L000218](../../agents/memory_bank.py#L218) | 218 | `"                \"readable\": ev.readable,"` | — |
| [SRC-9D8012A1A0-L000219](../../agents/memory_bank.py#L219) | 219 | `"            })"` | — |
| [SRC-9D8012A1A0-L000220](../../agents/memory_bank.py#L220) | 220 | `"        return sorted(rows, key=lambda r: r[\"index\"])"` | — |
| [SRC-9D8012A1A0-L000221](../../agents/memory_bank.py#L221) | 221 | `""` | — |
| [SRC-9D8012A1A0-L000222](../../agents/memory_bank.py#L222) | 222 | `"    def stats(self) -> dict[str, Any]:"` | — |
| [SRC-9D8012A1A0-L000223](../../agents/memory_bank.py#L223) | 223 | `"        supported = sum(1 for c in self.claims if c.status == \"supported\")"` | — |
| [SRC-9D8012A1A0-L000224](../../agents/memory_bank.py#L224) | 224 | `"        weak = sum(1 for c in self.claims if c.status == \"weak\")"` | — |
| [SRC-9D8012A1A0-L000225](../../agents/memory_bank.py#L225) | 225 | `"        unsupported = sum(1 for c in self.claims if c.status == \"unsupported\")"` | — |
| [SRC-9D8012A1A0-L000226](../../agents/memory_bank.py#L226) | 226 | `"        total = len(self.claims)"` | — |
| [SRC-9D8012A1A0-L000227](../../agents/memory_bank.py#L227) | 227 | `"        return {"` | — |
| [SRC-9D8012A1A0-L000228](../../agents/memory_bank.py#L228) | 228 | `"            \"session_id\": self.session_id,"` | — |
| [SRC-9D8012A1A0-L000229](../../agents/memory_bank.py#L229) | 229 | `"            \"evidence_count\": len(self.evidence),"` | — |
| [SRC-9D8012A1A0-L000230](../../agents/memory_bank.py#L230) | 230 | `"            \"claim_count\": total,"` | — |
| [SRC-9D8012A1A0-L000231](../../agents/memory_bank.py#L231) | 231 | `"            \"supported\": supported,"` | — |
| [SRC-9D8012A1A0-L000232](../../agents/memory_bank.py#L232) | 232 | `"            \"weak\": weak,"` | — |
| [SRC-9D8012A1A0-L000233](../../agents/memory_bank.py#L233) | 233 | `"            \"unsupported\": unsupported,"` | — |
| [SRC-9D8012A1A0-L000234](../../agents/memory_bank.py#L234) | 234 | `"            \"support_ratio\": round("` | — |
| [SRC-9D8012A1A0-L000235](../../agents/memory_bank.py#L235) | 235 | `"                (supported + 0.5 * weak) / max(1, total), 3"` | — |
| [SRC-9D8012A1A0-L000236](../../agents/memory_bank.py#L236) | 236 | `"            ) if total else 0.0,"` | — |
| [SRC-9D8012A1A0-L000237](../../agents/memory_bank.py#L237) | 237 | `"            \"readable_evidence\": sum(1 for e in self.evidence.values() if e.readable),"` | — |
| [SRC-9D8012A1A0-L000238](../../agents/memory_bank.py#L238) | 238 | `"        }"` | — |
| [SRC-9D8012A1A0-L000239](../../agents/memory_bank.py#L239) | 239 | `""` | — |
| [SRC-9D8012A1A0-L000240](../../agents/memory_bank.py#L240) | 240 | `"    def graph(self) -> dict[str, Any]:"` | — |
| [SRC-9D8012A1A0-L000241](../../agents/memory_bank.py#L241) | 241 | `"        edges = []"` | — |
| [SRC-9D8012A1A0-L000242](../../agents/memory_bank.py#L242) | 242 | `"        for c in self.claims:"` | — |
| [SRC-9D8012A1A0-L000243](../../agents/memory_bank.py#L243) | 243 | `"            for eid in c.evidence_ids:"` | — |
| [SRC-9D8012A1A0-L000244](../../agents/memory_bank.py#L244) | 244 | `"                edges.append({"` | — |
| [SRC-9D8012A1A0-L000245](../../agents/memory_bank.py#L245) | 245 | `"                    \"claim_id\": c.claim_id,"` | — |
| [SRC-9D8012A1A0-L000246](../../agents/memory_bank.py#L246) | 246 | `"                    \"evidence_id\": eid,"` | — |
| [SRC-9D8012A1A0-L000247](../../agents/memory_bank.py#L247) | 247 | `"                    \"status\": c.status,"` | — |
| [SRC-9D8012A1A0-L000248](../../agents/memory_bank.py#L248) | 248 | `"                    \"support_score\": c.support_score,"` | — |
| [SRC-9D8012A1A0-L000249](../../agents/memory_bank.py#L249) | 249 | `"                    \"aspect\": c.aspect,"` | — |
| [SRC-9D8012A1A0-L000250](../../agents/memory_bank.py#L250) | 250 | `"                })"` | — |
| [SRC-9D8012A1A0-L000251](../../agents/memory_bank.py#L251) | 251 | `"        return {"` | — |
| [SRC-9D8012A1A0-L000252](../../agents/memory_bank.py#L252) | 252 | `"            \"nodes_claims\": [c.to_dict() for c in self.claims],"` | — |
| [SRC-9D8012A1A0-L000253](../../agents/memory_bank.py#L253) | 253 | `"            \"nodes_evidence\": [e.to_dict() for e in self.evidence.values()],"` | — |
| [SRC-9D8012A1A0-L000254](../../agents/memory_bank.py#L254) | 254 | `"            \"edges\": edges,"` | — |
| [SRC-9D8012A1A0-L000255](../../agents/memory_bank.py#L255) | 255 | `"        }"` | — |
| [SRC-9D8012A1A0-L000256](../../agents/memory_bank.py#L256) | 256 | `""` | — |
| [SRC-9D8012A1A0-L000257](../../agents/memory_bank.py#L257) | 257 | `"    def to_claim_evidence_ledger_shape(self) -> dict[str, Any]:"` | — |
| [SRC-9D8012A1A0-L000258](../../agents/memory_bank.py#L258) | 258 | `"        segments = []"` | — |
| [SRC-9D8012A1A0-L000259](../../agents/memory_bank.py#L259) | 259 | `"        for i, c in enumerate(self.claims, start=1):"` | — |
| [SRC-9D8012A1A0-L000260](../../agents/memory_bank.py#L260) | 260 | `"            refs = []"` | — |
| [SRC-9D8012A1A0-L000261](../../agents/memory_bank.py#L261) | 261 | `"            for eid in c.evidence_ids:"` | — |
| [SRC-9D8012A1A0-L000262](../../agents/memory_bank.py#L262) | 262 | `"                ev = self.evidence.get(eid)"` | — |
| [SRC-9D8012A1A0-L000263](../../agents/memory_bank.py#L263) | 263 | `"                if not ev:"` | — |
| [SRC-9D8012A1A0-L000264](../../agents/memory_bank.py#L264) | 264 | `"                    continue"` | — |
| [SRC-9D8012A1A0-L000265](../../agents/memory_bank.py#L265) | 265 | `"                refs.append({"` | — |
| [SRC-9D8012A1A0-L000266](../../agents/memory_bank.py#L266) | 266 | `"                    \"source_index\": ev.source_index,"` | — |
| [SRC-9D8012A1A0-L000267](../../agents/memory_bank.py#L267) | 267 | `"                    \"reference_status\": ("` | — |
| [SRC-9D8012A1A0-L000268](../../agents/memory_bank.py#L268) | 268 | `"                        \"valid_index_with_readable_evidence\""` | — |
| [SRC-9D8012A1A0-L000269](../../agents/memory_bank.py#L269) | 269 | `"                        if ev.readable"` | — |
| [SRC-9D8012A1A0-L000270](../../agents/memory_bank.py#L270) | 270 | `"                        else \"valid_index_without_readable_evidence\""` | — |
| [SRC-9D8012A1A0-L000271](../../agents/memory_bank.py#L271) | 271 | `"                    ),"` | — |
| [SRC-9D8012A1A0-L000272](../../agents/memory_bank.py#L272) | 272 | `"                    \"title\": ev.title,"` | — |
| [SRC-9D8012A1A0-L000273](../../agents/memory_bank.py#L273) | 273 | `"                    \"url\": ev.url,"` | — |
| [SRC-9D8012A1A0-L000274](../../agents/memory_bank.py#L274) | 274 | `"                    \"evidence_basis\": ("` | — |
| [SRC-9D8012A1A0-L000275](../../agents/memory_bank.py#L275) | 275 | `"                        \"extracted_page_text\" if ev.page_fetched else \"search_snippet\""` | — |
| [SRC-9D8012A1A0-L000276](../../agents/memory_bank.py#L276) | 276 | `"                    ),"` | — |
| [SRC-9D8012A1A0-L000277](../../agents/memory_bank.py#L277) | 277 | `"                })"` | — |
| [SRC-9D8012A1A0-L000278](../../agents/memory_bank.py#L278) | 278 | `"            if c.status == \"supported\":"` | — |
| [SRC-9D8012A1A0-L000279](../../agents/memory_bank.py#L279) | 279 | `"                status = \"cited_source_attached\""` | — |
| [SRC-9D8012A1A0-L000280](../../agents/memory_bank.py#L280) | 280 | `"            elif c.status == \"weak\":"` | — |
| [SRC-9D8012A1A0-L000281](../../agents/memory_bank.py#L281) | 281 | `"                status = \"weak_lexical_overlap\""` | — |
| [SRC-9D8012A1A0-L000282](../../agents/memory_bank.py#L282) | 282 | `"            else:"` | — |
| [SRC-9D8012A1A0-L000283](../../agents/memory_bank.py#L283) | 283 | `"                status = \"uncited\""` | — |
| [SRC-9D8012A1A0-L000284](../../agents/memory_bank.py#L284) | 284 | `"            segments.append({"` | — |
| [SRC-9D8012A1A0-L000285](../../agents/memory_bank.py#L285) | 285 | `"                \"sentence_number\": i,"` | — |
| [SRC-9D8012A1A0-L000286](../../agents/memory_bank.py#L286) | 286 | `"                \"text\": c.text,"` | — |
| [SRC-9D8012A1A0-L000287](../../agents/memory_bank.py#L287) | 287 | `"                \"status\": status,"` | — |
| [SRC-9D8012A1A0-L000288](../../agents/memory_bank.py#L288) | 288 | `"                \"support_score\": c.support_score,"` | — |
| [SRC-9D8012A1A0-L000289](../../agents/memory_bank.py#L289) | 289 | `"                \"refs\": refs,"` | — |
| [SRC-9D8012A1A0-L000290](../../agents/memory_bank.py#L290) | 290 | `"                \"aspect\": c.aspect,"` | — |
| [SRC-9D8012A1A0-L000291](../../agents/memory_bank.py#L291) | 291 | `"            })"` | — |
| [SRC-9D8012A1A0-L000292](../../agents/memory_bank.py#L292) | 292 | `"        return {"` | — |
| [SRC-9D8012A1A0-L000293](../../agents/memory_bank.py#L293) | 293 | `"            \"method\": \"memory_bank_lexical_bind\","` | — |
| [SRC-9D8012A1A0-L000294](../../agents/memory_bank.py#L294) | 294 | `"            \"segments\": segments,"` | — |
| [SRC-9D8012A1A0-L000295](../../agents/memory_bank.py#L295) | 295 | `"            \"stats\": self.stats(),"` | — |
| [SRC-9D8012A1A0-L000296](../../agents/memory_bank.py#L296) | 296 | `"            \"citation_map\": self.citation_map(),"` | — |
| [SRC-9D8012A1A0-L000297](../../agents/memory_bank.py#L297) | 297 | `"            \"honesty\": ("` | — |
| [SRC-9D8012A1A0-L000298](../../agents/memory_bank.py#L298) | 298 | `"                \"الربط لفظي/معجمي عبر MemoryBank؛ ليس إثباتًا دلاليًا لصدق الادعاء.\""` | — |
| [SRC-9D8012A1A0-L000299](../../agents/memory_bank.py#L299) | 299 | `"            ),"` | — |
| [SRC-9D8012A1A0-L000300](../../agents/memory_bank.py#L300) | 300 | `"        }"` | — |
| [SRC-9D8012A1A0-L000301](../../agents/memory_bank.py#L301) | 301 | `""` | — |
| [SRC-9D8012A1A0-L000302](../../agents/memory_bank.py#L302) | 302 | `"    def to_dict(self) -> dict[str, Any]:"` | — |
| [SRC-9D8012A1A0-L000303](../../agents/memory_bank.py#L303) | 303 | `"        return {"` | — |
| [SRC-9D8012A1A0-L000304](../../agents/memory_bank.py#L304) | 304 | `"            \"session_id\": self.session_id,"` | — |
| [SRC-9D8012A1A0-L000305](../../agents/memory_bank.py#L305) | 305 | `"            \"evidence\": [e.to_dict() for e in self.evidence.values()],"` | — |
| [SRC-9D8012A1A0-L000306](../../agents/memory_bank.py#L306) | 306 | `"            \"claims\": [c.to_dict() for c in self.claims],"` | — |
| [SRC-9D8012A1A0-L000307](../../agents/memory_bank.py#L307) | 307 | `"            \"notes\": list(self.notes),"` | — |
| [SRC-9D8012A1A0-L000308](../../agents/memory_bank.py#L308) | 308 | `"            \"stats\": self.stats(),"` | — |
| [SRC-9D8012A1A0-L000309](../../agents/memory_bank.py#L309) | 309 | `"            \"citation_map\": self.citation_map(),"` | — |
| [SRC-9D8012A1A0-L000310](../../agents/memory_bank.py#L310) | 310 | `"            \"graph\": self.graph(),"` | — |
| [SRC-9D8012A1A0-L000311](../../agents/memory_bank.py#L311) | 311 | `"        }"` | — |
| [SRC-9D8012A1A0-L000312](../../agents/memory_bank.py#L312) | 312 | `""` | — |
| [SRC-9D8012A1A0-L000313](../../agents/memory_bank.py#L313) | 313 | `""` | — |
| [SRC-9D8012A1A0-L000314](../../agents/memory_bank.py#L314) | 314 | `"def split_answer_into_claim_sentences(answer: str, *, min_len: int = 12) -> list[str]:"` | — |
| [SRC-9D8012A1A0-L000315](../../agents/memory_bank.py#L315) | 315 | `"    parts = [p.strip() for p in _SENTENCE_SPLIT.split(answer or \"\") if p and p.strip()]"` | — |
| [SRC-9D8012A1A0-L000316](../../agents/memory_bank.py#L316) | 316 | `"    return [p for p in parts if len(p) >= min_len][:40]"` | — |
| [SRC-9D8012A1A0-L000317](../../agents/memory_bank.py#L317) | 317 | `""` | — |
| [SRC-9D8012A1A0-L000318](../../agents/memory_bank.py#L318) | 318 | `""` | — |
| [SRC-9D8012A1A0-L000319](../../agents/memory_bank.py#L319) | 319 | `"def build_memory_from_sources_and_answer("` | — |
| [SRC-9D8012A1A0-L000320](../../agents/memory_bank.py#L320) | 320 | `"    sources: list[dict[str, Any]] \| None,"` | — |
| [SRC-9D8012A1A0-L000321](../../agents/memory_bank.py#L321) | 321 | `"    answer: str,"` | — |
| [SRC-9D8012A1A0-L000322](../../agents/memory_bank.py#L322) | 322 | `"    *,"` | — |
| [SRC-9D8012A1A0-L000323](../../agents/memory_bank.py#L323) | 323 | `"    aspects: list[str] \| None = None,"` | — |
| [SRC-9D8012A1A0-L000324](../../agents/memory_bank.py#L324) | 324 | `"    session_id: str = \"\","` | — |
| [SRC-9D8012A1A0-L000325](../../agents/memory_bank.py#L325) | 325 | `"    min_score: float = 0.25,"` | — |
| [SRC-9D8012A1A0-L000326](../../agents/memory_bank.py#L326) | 326 | `") -> MemoryBank:"` | — |
| [SRC-9D8012A1A0-L000327](../../agents/memory_bank.py#L327) | 327 | `"    bank = MemoryBank(session_id=session_id)"` | — |
| [SRC-9D8012A1A0-L000328](../../agents/memory_bank.py#L328) | 328 | `"    bank.ingest_sources(sources)"` | — |
| [SRC-9D8012A1A0-L000329](../../agents/memory_bank.py#L329) | 329 | `"    bank.bind_answer(answer, min_score=min_score, aspects=aspects)"` | — |
| [SRC-9D8012A1A0-L000330](../../agents/memory_bank.py#L330) | 330 | `"    return bank"` | — |
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
| [SRC-59CF4B7DE8-L000017](../../agents/research.py#L17) | 17 | `"from agents.intent_router import resolve_followup_query"` | — |
| [SRC-59CF4B7DE8-L000018](../../agents/research.py#L18) | 18 | `""` | — |
| [SRC-59CF4B7DE8-L000019](../../agents/research.py#L19) | 19 | `"MAX_PLAN_QUERIES = 8"` | — |
| [SRC-59CF4B7DE8-L000020](../../agents/research.py#L20) | 20 | `"MAX_QUERY_CHARS = 240"` | — |
| [SRC-59CF4B7DE8-L000021](../../agents/research.py#L21) | 21 | `"MAX_FUSED_RESULTS = 18"` | — |
| [SRC-59CF4B7DE8-L000022](../../agents/research.py#L22) | 22 | `""` | — |
| [SRC-59CF4B7DE8-L000023](../../agents/research.py#L23) | 23 | `""` | — |
| [SRC-59CF4B7DE8-L000024](../../agents/research.py#L24) | 24 | `"# Use the Public Suffix List snapshot bundled with tldextract; never fetch it at"` | — |
| [SRC-59CF4B7DE8-L000025](../../agents/research.py#L25) | 25 | `"# runtime. Including private suffixes keeps tenant-hosted sites (e.g. github.io)"` | — |
| [SRC-59CF4B7DE8-L000026](../../agents/research.py#L26) | 26 | `"# separate, while subdomains belonging to one registrable site share one identity."` | — |
| [SRC-59CF4B7DE8-L000027](../../agents/research.py#L27) | 27 | `"_DOMAIN_EXTRACTOR = tldextract.TLDExtract("` | — |
| [SRC-59CF4B7DE8-L000028](../../agents/research.py#L28) | 28 | `"    suffix_list_urls=(),"` | — |
| [SRC-59CF4B7DE8-L000029](../../agents/research.py#L29) | 29 | `"    include_psl_private_domains=True,"` | — |
| [SRC-59CF4B7DE8-L000030](../../agents/research.py#L30) | 30 | `")"` | — |
| [SRC-59CF4B7DE8-L000031](../../agents/research.py#L31) | 31 | `""` | — |
| [SRC-59CF4B7DE8-L000032](../../agents/research.py#L32) | 32 | `""` | — |
| [SRC-59CF4B7DE8-L000033](../../agents/research.py#L33) | 33 | `"def registrable_domain(value: Any) -> str:"` | — |
| [SRC-59CF4B7DE8-L000034](../../agents/research.py#L34) | 34 | `"    \"\"\"Return a normalized registrable domain (or normalized IP/unknown hostname)."` | — |
| [SRC-59CF4B7DE8-L000035](../../agents/research.py#L35) | 35 | `""` | — |
| [SRC-59CF4B7DE8-L000036](../../agents/research.py#L36) | 36 | `"    This is a conservative source-diversity key, not proof that two publishers"` | — |
| [SRC-59CF4B7DE8-L000037](../../agents/research.py#L37) | 37 | `"    are editorially independent. It prevents sibling subdomains from being"` | — |
| [SRC-59CF4B7DE8-L000038](../../agents/research.py#L38) | 38 | `"    counted as separate domains in the evidence coverage threshold."` | — |
| [SRC-59CF4B7DE8-L000039](../../agents/research.py#L39) | 39 | `"    \"\"\""` | — |
| [SRC-59CF4B7DE8-L000040](../../agents/research.py#L40) | 40 | `"    candidate = str(value or \"\").strip()"` | — |
| [SRC-59CF4B7DE8-L000041](../../agents/research.py#L41) | 41 | `"    if not candidate:"` | — |
| [SRC-59CF4B7DE8-L000042](../../agents/research.py#L42) | 42 | `"        return \"\""` | — |
