# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **003**
- سجلات الأسطر: **800**
- النطاق: SRC-59CF4B7DE8-L000598 إلى SRC-1AE03B9EC3-L000721
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-59CF4B7DE8 — [agents/research.py](../../agents/research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-59CF4B7DE8-L000598](../../agents/research.py#L598) | 598 | `"                \"reason\": \"kept_official_despite_low_overlap\"}"` | — |
| [SRC-59CF4B7DE8-L000599](../../agents/research.py#L599) | 599 | `""` | — |
| [SRC-59CF4B7DE8-L000600](../../agents/research.py#L600) | 600 | `"    if score >= 18:"` | — |
| [SRC-59CF4B7DE8-L000601](../../agents/research.py#L601) | 601 | `"        return {\"accepted\": True, \"score\": score, \"reason\": \"accepted\"}"` | — |
| [SRC-59CF4B7DE8-L000602](../../agents/research.py#L602) | 602 | `"    return {\"accepted\": False, \"score\": score, \"reason\": \"low_overlap\"}"` | — |
| [SRC-59CF4B7DE8-L000603](../../agents/research.py#L603) | 603 | `""` | — |
| [SRC-59CF4B7DE8-L000604](../../agents/research.py#L604) | 604 | `""` | — |
| [SRC-59CF4B7DE8-L000605](../../agents/research.py#L605) | 605 | `"def filter_relevant_sources(sources, query: str, extra_queries=None):"` | — |
| [SRC-59CF4B7DE8-L000606](../../agents/research.py#L606) | 606 | `"    kept = []"` | — |
| [SRC-59CF4B7DE8-L000607](../../agents/research.py#L607) | 607 | `"    diag = []"` | — |
| [SRC-59CF4B7DE8-L000608](../../agents/research.py#L608) | 608 | `"    seen_urls = set()"` | — |
| [SRC-59CF4B7DE8-L000609](../../agents/research.py#L609) | 609 | `"    seen_titles = set()"` | — |
| [SRC-59CF4B7DE8-L000610](../../agents/research.py#L610) | 610 | `"    combined = \" \".join([query] + list(extra_queries or []))"` | — |
| [SRC-59CF4B7DE8-L000611](../../agents/research.py#L611) | 611 | `""` | — |
| [SRC-59CF4B7DE8-L000612](../../agents/research.py#L612) | 612 | `"    for src in sources or []:"` | — |
| [SRC-59CF4B7DE8-L000613](../../agents/research.py#L613) | 613 | `"        if not isinstance(src, dict):"` | — |
| [SRC-59CF4B7DE8-L000614](../../agents/research.py#L614) | 614 | `"            diag.append({\"reason\": \"malformed\", \"url\": \"\"})"` | — |
| [SRC-59CF4B7DE8-L000615](../../agents/research.py#L615) | 615 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000616](../../agents/research.py#L616) | 616 | `"        url = str(src.get(\"url\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000617](../../agents/research.py#L617) | 617 | `"        domain = str(src.get(\"domain\") or \"\").lower()"` | — |
| [SRC-59CF4B7DE8-L000618](../../agents/research.py#L618) | 618 | `"        title = str(src.get(\"title\") or \"\").strip()"` | — |
| [SRC-59CF4B7DE8-L000619](../../agents/research.py#L619) | 619 | `"        url_key = url.rstrip(\"/\").lower()"` | — |
| [SRC-59CF4B7DE8-L000620](../../agents/research.py#L620) | 620 | `"        title_key = title.lower() + \"\|\" + domain"` | — |
| [SRC-59CF4B7DE8-L000621](../../agents/research.py#L621) | 621 | `""` | — |
| [SRC-59CF4B7DE8-L000622](../../agents/research.py#L622) | 622 | `"        if url_key and url_key in seen_urls:"` | — |
| [SRC-59CF4B7DE8-L000623](../../agents/research.py#L623) | 623 | `"            diag.append({\"reason\": \"duplicate_url\", \"url\": url})"` | — |
| [SRC-59CF4B7DE8-L000624](../../agents/research.py#L624) | 624 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000625](../../agents/research.py#L625) | 625 | `"        if title and title_key in seen_titles:"` | — |
| [SRC-59CF4B7DE8-L000626](../../agents/research.py#L626) | 626 | `"            diag.append({\"reason\": \"duplicate_title_domain\", \"url\": url})"` | — |
| [SRC-59CF4B7DE8-L000627](../../agents/research.py#L627) | 627 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000628](../../agents/research.py#L628) | 628 | `""` | — |
| [SRC-59CF4B7DE8-L000629](../../agents/research.py#L629) | 629 | `"        rel = source_relevance_score(src, combined)"` | — |
| [SRC-59CF4B7DE8-L000630](../../agents/research.py#L630) | 630 | `"        if not rel[\"accepted\"]:"` | — |
| [SRC-59CF4B7DE8-L000631](../../agents/research.py#L631) | 631 | `"            diag.append({\"reason\": rel[\"reason\"], \"url\": url, \"score\": rel[\"score\"]})"` | — |
| [SRC-59CF4B7DE8-L000632](../../agents/research.py#L632) | 632 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000633](../../agents/research.py#L633) | 633 | `""` | — |
| [SRC-59CF4B7DE8-L000634](../../agents/research.py#L634) | 634 | `"        kept.append(src)"` | — |
| [SRC-59CF4B7DE8-L000635](../../agents/research.py#L635) | 635 | `"        if url_key:"` | — |
| [SRC-59CF4B7DE8-L000636](../../agents/research.py#L636) | 636 | `"            seen_urls.add(url_key)"` | — |
| [SRC-59CF4B7DE8-L000637](../../agents/research.py#L637) | 637 | `"        if title:"` | — |
| [SRC-59CF4B7DE8-L000638](../../agents/research.py#L638) | 638 | `"            seen_titles.add(title_key)"` | — |
| [SRC-59CF4B7DE8-L000639](../../agents/research.py#L639) | 639 | `"    return kept, diag"` | — |
| [SRC-59CF4B7DE8-L000640](../../agents/research.py#L640) | 640 | `""` | — |
| [SRC-59CF4B7DE8-L000641](../../agents/research.py#L641) | 641 | `""` | — |
| [SRC-59CF4B7DE8-L000642](../../agents/research.py#L642) | 642 | `"def decide_evidence_status(sources, pages_read: int = 0,"` | — |
| [SRC-59CF4B7DE8-L000643](../../agents/research.py#L643) | 643 | `"                           provider_failures: int = 0,"` | — |
| [SRC-59CF4B7DE8-L000644](../../agents/research.py#L644) | 644 | `"                           search_attempted: bool = True) -> dict:"` | — |
| [SRC-59CF4B7DE8-L000645](../../agents/research.py#L645) | 645 | `"    if not search_attempted:"` | — |
| [SRC-59CF4B7DE8-L000646](../../agents/research.py#L646) | 646 | `"        return {\"evidence_status\": \"failed\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000647](../../agents/research.py#L647) | 647 | `""` | — |
| [SRC-59CF4B7DE8-L000648](../../agents/research.py#L648) | 648 | `"    domains = set()"` | — |
| [SRC-59CF4B7DE8-L000649](../../agents/research.py#L649) | 649 | `"    has_official = False"` | — |
| [SRC-59CF4B7DE8-L000650](../../agents/research.py#L650) | 650 | `"    for s in sources or []:"` | — |
| [SRC-59CF4B7DE8-L000651](../../agents/research.py#L651) | 651 | `"        if not isinstance(s, dict):"` | — |
| [SRC-59CF4B7DE8-L000652](../../agents/research.py#L652) | 652 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000653](../../agents/research.py#L653) | 653 | `"        d = str(s.get(\"domain\") or \"\").lower()"` | — |
| [SRC-59CF4B7DE8-L000654](../../agents/research.py#L654) | 654 | `"        if not d:"` | — |
| [SRC-59CF4B7DE8-L000655](../../agents/research.py#L655) | 655 | `"            url = str(s.get(\"url\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000656](../../agents/research.py#L656) | 656 | `"            if url:"` | — |
| [SRC-59CF4B7DE8-L000657](../../agents/research.py#L657) | 657 | `"                try:"` | — |
| [SRC-59CF4B7DE8-L000658](../../agents/research.py#L658) | 658 | `"                    from urllib.parse import urlparse"` | — |
| [SRC-59CF4B7DE8-L000659](../../agents/research.py#L659) | 659 | `"                    d = urlparse(url).netloc.lower()"` | — |
| [SRC-59CF4B7DE8-L000660](../../agents/research.py#L660) | 660 | `"                except Exception:"` | — |
| [SRC-59CF4B7DE8-L000661](../../agents/research.py#L661) | 661 | `"                    d = \"\""` | — |
| [SRC-59CF4B7DE8-L000662](../../agents/research.py#L662) | 662 | `"        if d:"` | — |
| [SRC-59CF4B7DE8-L000663](../../agents/research.py#L663) | 663 | `"            domains.add(d)"` | — |
| [SRC-59CF4B7DE8-L000664](../../agents/research.py#L664) | 664 | `"        if str(s.get(\"source_class\") or \"\").lower() in _OFFICIAL_CLASSES:"` | — |
| [SRC-59CF4B7DE8-L000665](../../agents/research.py#L665) | 665 | `"            has_official = True"` | — |
| [SRC-59CF4B7DE8-L000666](../../agents/research.py#L666) | 666 | `""` | — |
| [SRC-59CF4B7DE8-L000667](../../agents/research.py#L667) | 667 | `"    if not sources:"` | — |
| [SRC-59CF4B7DE8-L000668](../../agents/research.py#L668) | 668 | `"        if provider_failures > 0:"` | — |
| [SRC-59CF4B7DE8-L000669](../../agents/research.py#L669) | 669 | `"            return {\"evidence_status\": \"failed\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000670](../../agents/research.py#L670) | 670 | `"        return {\"evidence_status\": \"insufficient\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000671](../../agents/research.py#L671) | 671 | `""` | — |
| [SRC-59CF4B7DE8-L000672](../../agents/research.py#L672) | 672 | `"    if len(domains) >= 2 or has_official:"` | — |
| [SRC-59CF4B7DE8-L000673](../../agents/research.py#L673) | 673 | `"        return {\"evidence_status\": \"adequate\", \"should_abstain\": False}"` | — |
| [SRC-59CF4B7DE8-L000674](../../agents/research.py#L674) | 674 | `"    if len(domains) >= 1:"` | — |
| [SRC-59CF4B7DE8-L000675](../../agents/research.py#L675) | 675 | `"        return {\"evidence_status\": \"partial\", \"should_abstain\": False}"` | — |
| [SRC-59CF4B7DE8-L000676](../../agents/research.py#L676) | 676 | `"    return {\"evidence_status\": \"insufficient\", \"should_abstain\": True}"` | — |
## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L000001](../../agents/web_agent.py#L1) | 1 | `"\"\"\"Grounded natural-language web research for Omarai."` | — |
| [SRC-1AE03B9EC3-L000002](../../agents/web_agent.py#L2) | 2 | `""` | — |
| [SRC-1AE03B9EC3-L000003](../../agents/web_agent.py#L3) | 3 | `"Searches public web results, extracts a small amount of page text, then asks an"` | — |
| [SRC-1AE03B9EC3-L000004](../../agents/web_agent.py#L4) | 4 | `"OpenAI-compatible language model to answer in the user's language with sources."` | — |
| [SRC-1AE03B9EC3-L000005](../../agents/web_agent.py#L5) | 5 | `"API credentials are read only from environment variables and are never returned."` | — |
| [SRC-1AE03B9EC3-L000006](../../agents/web_agent.py#L6) | 6 | `"\"\"\""` | — |
| [SRC-1AE03B9EC3-L000007](../../agents/web_agent.py#L7) | 7 | `"from __future__ import annotations"` | — |
| [SRC-1AE03B9EC3-L000008](../../agents/web_agent.py#L8) | 8 | `""` | — |
| [SRC-1AE03B9EC3-L000009](../../agents/web_agent.py#L9) | 9 | `"import asyncio"` | — |
| [SRC-1AE03B9EC3-L000010](../../agents/web_agent.py#L10) | 10 | `"import datetime as dt"` | — |
| [SRC-1AE03B9EC3-L000011](../../agents/web_agent.py#L11) | 11 | `"import ipaddress"` | — |
| [SRC-1AE03B9EC3-L000012](../../agents/web_agent.py#L12) | 12 | `"import json"` | — |
| [SRC-1AE03B9EC3-L000013](../../agents/web_agent.py#L13) | 13 | `"import os"` | — |
| [SRC-1AE03B9EC3-L000014](../../agents/web_agent.py#L14) | 14 | `"import re"` | — |
| [SRC-1AE03B9EC3-L000015](../../agents/web_agent.py#L15) | 15 | `"import socket"` | — |
| [SRC-1AE03B9EC3-L000016](../../agents/web_agent.py#L16) | 16 | `"import threading"` | — |
| [SRC-1AE03B9EC3-L000017](../../agents/web_agent.py#L17) | 17 | `"import unicodedata"` | — |
| [SRC-1AE03B9EC3-L000018](../../agents/web_agent.py#L18) | 18 | `"import urllib.error"` | — |
| [SRC-1AE03B9EC3-L000019](../../agents/web_agent.py#L19) | 19 | `"import urllib.parse"` | — |
| [SRC-1AE03B9EC3-L000020](../../agents/web_agent.py#L20) | 20 | `"import urllib.request"` | — |
| [SRC-1AE03B9EC3-L000021](../../agents/web_agent.py#L21) | 21 | `"from concurrent.futures import ThreadPoolExecutor, as_completed"` | — |
| [SRC-1AE03B9EC3-L000022](../../agents/web_agent.py#L22) | 22 | `"from typing import Any"` | — |
| [SRC-1AE03B9EC3-L000023](../../agents/web_agent.py#L23) | 23 | `""` | — |
| [SRC-1AE03B9EC3-L000024](../../agents/web_agent.py#L24) | 24 | `"from agents.intent_router import route_intent"` | — |
| [SRC-1AE03B9EC3-L000025](../../agents/web_agent.py#L25) | 25 | `"from agents.request_budget import RequestBudget, RequestBudgetExceeded"` | — |
| [SRC-1AE03B9EC3-L000026](../../agents/web_agent.py#L26) | 26 | `"from agents.research import ("` | — |
| [SRC-1AE03B9EC3-L000027](../../agents/web_agent.py#L27) | 27 | `"    MAX_PLAN_QUERIES,"` | — |
| [SRC-1AE03B9EC3-L000028](../../agents/web_agent.py#L28) | 28 | `"    SOCIAL_DOMAINS,"` | — |
| [SRC-1AE03B9EC3-L000029](../../agents/web_agent.py#L29) | 29 | `"    evidence_signal_report,"` | — |
| [SRC-1AE03B9EC3-L000030](../../agents/web_agent.py#L30) | 30 | `"    fallback_plan,"` | — |
| [SRC-1AE03B9EC3-L000031](../../agents/web_agent.py#L31) | 31 | `"    fuse_ranked_results,"` | — |
| [SRC-1AE03B9EC3-L000032](../../agents/web_agent.py#L32) | 32 | `"    registrable_domain,"` | — |
| [SRC-1AE03B9EC3-L000033](../../agents/web_agent.py#L33) | 33 | `"    validate_plan,"` | — |
| [SRC-1AE03B9EC3-L000034](../../agents/web_agent.py#L34) | 34 | `")"` | — |
| [SRC-1AE03B9EC3-L000035](../../agents/web_agent.py#L35) | 35 | `""` | — |
| [SRC-1AE03B9EC3-L000036](../../agents/web_agent.py#L36) | 36 | `"MAX_QUESTION_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000037](../../agents/web_agent.py#L37) | 37 | `"MAX_HISTORY_ITEMS = 8"` | — |
| [SRC-1AE03B9EC3-L000038](../../agents/web_agent.py#L38) | 38 | `"MAX_HISTORY_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000039](../../agents/web_agent.py#L39) | 39 | `"MAX_SEARCH_RESULTS = 18"` | — |
| [SRC-1AE03B9EC3-L000040](../../agents/web_agent.py#L40) | 40 | `"MAX_PROVIDER_RESULTS = 6"` | — |
| [SRC-1AE03B9EC3-L000041](../../agents/web_agent.py#L41) | 41 | `"MAX_FETCHED_PAGES = 8"` | — |
| [SRC-1AE03B9EC3-L000042](../../agents/web_agent.py#L42) | 42 | `"MAX_LLM_CITED_SOURCES = 12"` | — |
| [SRC-1AE03B9EC3-L000043](../../agents/web_agent.py#L43) | 43 | `"MAX_RESEARCH_WORKERS = 8"` | — |
| [SRC-1AE03B9EC3-L000044](../../agents/web_agent.py#L44) | 44 | `"MAX_PAGE_BYTES = 1_000_000"` | — |
| [SRC-1AE03B9EC3-L000045](../../agents/web_agent.py#L45) | 45 | `"MAX_PAGE_TEXT_CHARS = 12_000"` | — |
| [SRC-1AE03B9EC3-L000046](../../agents/web_agent.py#L46) | 46 | `"LLM_TIMEOUT_SECONDS = 35"` | — |
| [SRC-1AE03B9EC3-L000047](../../agents/web_agent.py#L47) | 47 | `""` | — |
| [SRC-1AE03B9EC3-L000048](../../agents/web_agent.py#L48) | 48 | `"# Only completed connector result-processing states positively confirm an attempt."` | — |
| [SRC-1AE03B9EC3-L000049](../../agents/web_agent.py#L49) | 49 | `"# A generic \"failed\" or timeout diagnostic may occur before a network request is sent."` | — |
| [SRC-1AE03B9EC3-L000050](../../agents/web_agent.py#L50) | 50 | `"_SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES = frozenset({\"ok\", \"no_results\", \"filtered_all\"})"` | — |
| [SRC-1AE03B9EC3-L000051](../../agents/web_agent.py#L51) | 51 | `"_RESEARCH_ERROR_OUTCOMES = frozenset({\"attempted_research_error\", \"unknown_after_research_error\"})"` | — |
| [SRC-1AE03B9EC3-L000052](../../agents/web_agent.py#L52) | 52 | `""` | — |
| [SRC-1AE03B9EC3-L000053](../../agents/web_agent.py#L53) | 53 | `""` | — |
| [SRC-1AE03B9EC3-L000054](../../agents/web_agent.py#L54) | 54 | `"_ARABIC_SEARCH_TRANSLATION = str.maketrans({"` | — |
| [SRC-1AE03B9EC3-L000055](../../agents/web_agent.py#L55) | 55 | `"    \"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ٱ\": \"ا\", \"ى\": \"ي\","` | — |
| [SRC-1AE03B9EC3-L000056](../../agents/web_agent.py#L56) | 56 | `"    \"ؤ\": \"و\", \"ئ\": \"ي\", \"ة\": \"ه\", \"ـ\": \"\","` | — |
| [SRC-1AE03B9EC3-L000057](../../agents/web_agent.py#L57) | 57 | `"})"` | — |
| [SRC-1AE03B9EC3-L000058](../../agents/web_agent.py#L58) | 58 | `"_ARABIC_DIACRITICS_RE = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-1AE03B9EC3-L000059](../../agents/web_agent.py#L59) | 59 | `"_SEARCH_STOPWORDS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000060](../../agents/web_agent.py#L60) | 60 | `"    \"ما\", \"ماذا\", \"من\", \"في\", \"على\", \"عن\", \"الى\", \"إلى\", \"و\", \"او\", \"أو\","` | — |
| [SRC-1AE03B9EC3-L000061](../../agents/web_agent.py#L61) | 61 | `"    \"هل\", \"هو\", \"هي\", \"هذا\", \"هذه\", \"ذلك\", \"تلك\", \"التي\", \"الذي\", \"مع\","` | — |
| [SRC-1AE03B9EC3-L000062](../../agents/web_agent.py#L62) | 62 | `"    \"بين\", \"كيف\", \"لماذا\", \"كم\", \"كان\", \"كانت\", \"يكون\", \"تكون\", \"لي\","` | — |
| [SRC-1AE03B9EC3-L000063](../../agents/web_agent.py#L63) | 63 | `"    \"the\", \"a\", \"an\", \"and\", \"or\", \"in\", \"on\", \"of\", \"to\", \"for\", \"with\","` | — |
| [SRC-1AE03B9EC3-L000064](../../agents/web_agent.py#L64) | 64 | `"    \"is\", \"are\", \"was\", \"were\", \"what\", \"which\", \"who\", \"how\", \"why\", \"when\","` | — |
| [SRC-1AE03B9EC3-L000065](../../agents/web_agent.py#L65) | 65 | `"    \"where\", \"compare\", \"comparison\", \"please\", \"show\", \"find\", \"latest\","` | — |
| [SRC-1AE03B9EC3-L000066](../../agents/web_agent.py#L66) | 66 | `"    \"news\", \"official\", \"sources\", \"source\", \"reports\", \"report\", \"analysis\","` | — |
| [SRC-1AE03B9EC3-L000067](../../agents/web_agent.py#L67) | 67 | `"    \"site\", \"com\", \"org\", \"net\", \"www\","` | — |
| [SRC-1AE03B9EC3-L000068](../../agents/web_agent.py#L68) | 68 | `"})"` | — |
| [SRC-1AE03B9EC3-L000069](../../agents/web_agent.py#L69) | 69 | `"_SEARCH_SYNONYMS = {"` | — |
| [SRC-1AE03B9EC3-L000070](../../agents/web_agent.py#L70) | 70 | `"    \"استراليا\": {\"australia\"}, \"عاصمة\": {\"capital\"}, \"مصر\": {\"egypt\"},"` | — |
| [SRC-1AE03B9EC3-L000071](../../agents/web_agent.py#L71) | 71 | `"    \"المصري\": {\"egyptian\", \"egypt\"}, \"مركزي\": {\"central\"},"` | — |
| [SRC-1AE03B9EC3-L000072](../../agents/web_agent.py#L72) | 72 | `"    \"المركزي\": {\"central\"}, \"بنك\": {\"bank\"}, \"البنك\": {\"bank\"},"` | — |
| [SRC-1AE03B9EC3-L000073](../../agents/web_agent.py#L73) | 73 | `"    \"قرار\": {\"decision\"}, \"قرارات\": {\"decision\", \"decisions\"},"` | — |
| [SRC-1AE03B9EC3-L000074](../../agents/web_agent.py#L74) | 74 | `"    \"سعر\": {\"price\"}, \"اسعار\": {\"prices\"}, \"استضافة\": {\"hosting\"},"` | — |
| [SRC-1AE03B9EC3-L000075](../../agents/web_agent.py#L75) | 75 | `"    \"شركة\": {\"company\"}, \"شركه\": {\"company\"}, \"ناشئة\": {\"startup\"},"` | — |
| [SRC-1AE03B9EC3-L000076](../../agents/web_agent.py#L76) | 76 | `"    \"صعيد\": {\"upper\"}, \"مقارنة\": {\"compare\", \"comparison\"},"` | — |
| [SRC-1AE03B9EC3-L000077](../../agents/web_agent.py#L77) | 77 | `"    \"تقنية\": {\"technology\"}, \"تقنيات\": {\"technology\"},"` | — |
| [SRC-1AE03B9EC3-L000078](../../agents/web_agent.py#L78) | 78 | `"    \"ميكروسوفت\": {\"microsoft\"}, \"مايكروسوفت\": {\"microsoft\"},"` | — |
| [SRC-1AE03B9EC3-L000079](../../agents/web_agent.py#L79) | 79 | `"    \"microsoft\": {\"ميكروسوفت\", \"مايكروسوفت\"},"` | — |
| [SRC-1AE03B9EC3-L000080](../../agents/web_agent.py#L80) | 80 | `"    \"جمهورية\": {\"republic\"}, \"republic\": {\"جمهورية\"},"` | — |
| [SRC-1AE03B9EC3-L000081](../../agents/web_agent.py#L81) | 81 | `"    \"الرقمية\": {\"digital\"}, \"رقمية\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000082](../../agents/web_agent.py#L82) | 82 | `"    \"الرقميه\": {\"digital\"}, \"رقميه\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000083](../../agents/web_agent.py#L83) | 83 | `"    \"موقع\": {\"website\", \"portal\"}, \"مواقع\": {\"websites\", \"portals\"},"` | — |
| [SRC-1AE03B9EC3-L000084](../../agents/web_agent.py#L84) | 84 | `"    \"التجمع\": {\"settlement\"}, \"تجمع\": {\"settlement\"},"` | — |
| [SRC-1AE03B9EC3-L000085](../../agents/web_agent.py#L85) | 85 | `"    \"الخامس\": {\"fifth\", \"5th\"}, \"خامس\": {\"fifth\", \"5th\"},"` | — |
| [SRC-1AE03B9EC3-L000086](../../agents/web_agent.py#L86) | 86 | `"    \"شقة\": {\"apartment\", \"flat\"}, \"شقق\": {\"apartments\", \"flats\"},"` | — |
| [SRC-1AE03B9EC3-L000087](../../agents/web_agent.py#L87) | 87 | `"    \"عميل\": {\"customer\", \"buyer\"}, \"عملاء\": {\"customers\", \"buyers\"},"` | — |
| [SRC-1AE03B9EC3-L000088](../../agents/web_agent.py#L88) | 88 | `"    \"شراء\": {\"buy\", \"purchase\"}, \"مشتري\": {\"buyer\"},"` | — |
| [SRC-1AE03B9EC3-L000089](../../agents/web_agent.py#L89) | 89 | `"}"` | — |
| [SRC-1AE03B9EC3-L000090](../../agents/web_agent.py#L90) | 90 | `"_CALENDAR_MONTHS = ("` | — |
| [SRC-1AE03B9EC3-L000091](../../agents/web_agent.py#L91) | 91 | `"    \"يناير\", \"فبراير\", \"مارس\", \"ابريل\", \"أبريل\", \"مايو\", \"يونيو\","` | — |
| [SRC-1AE03B9EC3-L000092](../../agents/web_agent.py#L92) | 92 | `"    \"يوليو\", \"اغسطس\", \"أغسطس\", \"سبتمبر\", \"اكتوبر\", \"أكتوبر\","` | — |
| [SRC-1AE03B9EC3-L000093](../../agents/web_agent.py#L93) | 93 | `"    \"نوفمبر\", \"ديسمبر\", \"january\", \"february\", \"march\", \"april\","` | — |
| [SRC-1AE03B9EC3-L000094](../../agents/web_agent.py#L94) | 94 | `"    \"may\", \"june\", \"july\", \"august\", \"september\", \"october\","` | — |
| [SRC-1AE03B9EC3-L000095](../../agents/web_agent.py#L95) | 95 | `"    \"november\", \"december\","` | — |
| [SRC-1AE03B9EC3-L000096](../../agents/web_agent.py#L96) | 96 | `")"` | — |
| [SRC-1AE03B9EC3-L000097](../../agents/web_agent.py#L97) | 97 | `"_BLOCKED_SOURCE_DOMAINS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000098](../../agents/web_agent.py#L98) | 98 | `"    \"translate.google.com\", \"translate.googleusercontent.com\","` | — |
| [SRC-1AE03B9EC3-L000099](../../agents/web_agent.py#L99) | 99 | `"})"` | — |
| [SRC-1AE03B9EC3-L000100](../../agents/web_agent.py#L100) | 100 | `""` | — |
| [SRC-1AE03B9EC3-L000101](../../agents/web_agent.py#L101) | 101 | `""` | — |
| [SRC-1AE03B9EC3-L000102](../../agents/web_agent.py#L102) | 102 | `"def _normalize_search_query(value: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000103](../../agents/web_agent.py#L103) | 103 | `"    \"\"\"Normalize Arabic letters/diacritics while preserving search operators and dates.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000104](../../agents/web_agent.py#L104) | 104 | `"    value = unicodedata.normalize(\"NFKC\", value or \"\")"` | — |
| [SRC-1AE03B9EC3-L000105](../../agents/web_agent.py#L105) | 105 | `"    value = _ARABIC_DIACRITICS_RE.sub(\"\", value).translate(_ARABIC_SEARCH_TRANSLATION)"` | — |
| [SRC-1AE03B9EC3-L000106](../../agents/web_agent.py#L106) | 106 | `"    return re.sub(r\"\\s+\", \" \", value).strip()"` | — |
| [SRC-1AE03B9EC3-L000107](../../agents/web_agent.py#L107) | 107 | `""` | — |
| [SRC-1AE03B9EC3-L000108](../../agents/web_agent.py#L108) | 108 | `""` | — |
| [SRC-1AE03B9EC3-L000109](../../agents/web_agent.py#L109) | 109 | `"# Normalize synonym keys and values by the same rules as search text. This avoids"` | — |
| [SRC-1AE03B9EC3-L000110](../../agents/web_agent.py#L110) | 110 | `"# Arabic ta-marbuta/alif variants silently disabling Arabic-to-English matching."` | — |
| [SRC-1AE03B9EC3-L000111](../../agents/web_agent.py#L111) | 111 | `"_NORMALIZED_SEARCH_SYNONYMS: dict[str, set[str]] = {}"` | — |
| [SRC-1AE03B9EC3-L000112](../../agents/web_agent.py#L112) | 112 | `"for _synonym_key, _synonym_values in _SEARCH_SYNONYMS.items():"` | — |
| [SRC-1AE03B9EC3-L000113](../../agents/web_agent.py#L113) | 113 | `"    _normalized_key = _normalize_search_query(_synonym_key).casefold()"` | — |
| [SRC-1AE03B9EC3-L000114](../../agents/web_agent.py#L114) | 114 | `"    _NORMALIZED_SEARCH_SYNONYMS.setdefault(_normalized_key, set()).update("` | — |
| [SRC-1AE03B9EC3-L000115](../../agents/web_agent.py#L115) | 115 | `"        _normalize_search_query(value).casefold() for value in _synonym_values"` | — |
| [SRC-1AE03B9EC3-L000116](../../agents/web_agent.py#L116) | 116 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000117](../../agents/web_agent.py#L117) | 117 | `""` | — |
| [SRC-1AE03B9EC3-L000118](../../agents/web_agent.py#L118) | 118 | `""` | — |
| [SRC-1AE03B9EC3-L000119](../../agents/web_agent.py#L119) | 119 | `"def _search_tokens(value: str) -> set[str]:"` | — |
| [SRC-1AE03B9EC3-L000120](../../agents/web_agent.py#L120) | 120 | `"    \"\"\"Tokenize Arabic/English text and expand a small bilingual vocabulary.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000121](../../agents/web_agent.py#L121) | 121 | `"    value = _normalize_search_query(value).casefold()"` | — |
| [SRC-1AE03B9EC3-L000122](../../agents/web_agent.py#L122) | 122 | `"    value = re.sub(r\"(?i)\\bsite\\s*:\\s*\\S+\", \" \", value)"` | — |
| [SRC-1AE03B9EC3-L000123](../../agents/web_agent.py#L123) | 123 | `"    tokens = re.findall(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", value)"` | — |
| [SRC-1AE03B9EC3-L000124](../../agents/web_agent.py#L124) | 124 | `"    result: set[str] = set()"` | — |
| [SRC-1AE03B9EC3-L000125](../../agents/web_agent.py#L125) | 125 | `"    for token in tokens:"` | — |
| [SRC-1AE03B9EC3-L000126](../../agents/web_agent.py#L126) | 126 | `"        if token in _SEARCH_STOPWORDS or len(token) < 2:"` | — |
| [SRC-1AE03B9EC3-L000127](../../agents/web_agent.py#L127) | 127 | `"            continue"` | — |
| [SRC-1AE03B9EC3-L000128](../../agents/web_agent.py#L128) | 128 | `"        forms = {token}"` | — |
| [SRC-1AE03B9EC3-L000129](../../agents/web_agent.py#L129) | 129 | `"        if token.startswith(\"ال\") and len(token) > 4:"` | — |
| [SRC-1AE03B9EC3-L000130](../../agents/web_agent.py#L130) | 130 | `"            forms.add(token[2:])"` | — |
| [SRC-1AE03B9EC3-L000131](../../agents/web_agent.py#L131) | 131 | `"        forms.update(_NORMALIZED_SEARCH_SYNONYMS.get(token, set()))"` | — |
| [SRC-1AE03B9EC3-L000132](../../agents/web_agent.py#L132) | 132 | `"        # Reverse-map common English equivalents so Arabic and English results can match."` | — |
| [SRC-1AE03B9EC3-L000133](../../agents/web_agent.py#L133) | 133 | `"        for arabic, english in _NORMALIZED_SEARCH_SYNONYMS.items():"` | — |
| [SRC-1AE03B9EC3-L000134](../../agents/web_agent.py#L134) | 134 | `"            if token in english:"` | — |
| [SRC-1AE03B9EC3-L000135](../../agents/web_agent.py#L135) | 135 | `"                forms.add(arabic)"` | — |
| [SRC-1AE03B9EC3-L000136](../../agents/web_agent.py#L136) | 136 | `"                if arabic.startswith(\"ال\") and len(arabic) > 4:"` | — |
| [SRC-1AE03B9EC3-L000137](../../agents/web_agent.py#L137) | 137 | `"                    forms.add(arabic[2:])"` | — |
| [SRC-1AE03B9EC3-L000138](../../agents/web_agent.py#L138) | 138 | `"        result.update(forms)"` | — |
| [SRC-1AE03B9EC3-L000139](../../agents/web_agent.py#L139) | 139 | `"    return result"` | — |
| [SRC-1AE03B9EC3-L000140](../../agents/web_agent.py#L140) | 140 | `""` | — |
| [SRC-1AE03B9EC3-L000141](../../agents/web_agent.py#L141) | 141 | `""` | — |
| [SRC-1AE03B9EC3-L000142](../../agents/web_agent.py#L142) | 142 | `"def _relevance_ratio(query: str, evidence: str) -> float:"` | — |
| [SRC-1AE03B9EC3-L000143](../../agents/web_agent.py#L143) | 143 | `"    \"\"\"Fraction of meaningful query concepts present in a candidate's title/snippet.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000144](../../agents/web_agent.py#L144) | 144 | `"    query_text = _normalize_search_query(query).casefold()"` | — |
| [SRC-1AE03B9EC3-L000145](../../agents/web_agent.py#L145) | 145 | `"    query_text = re.sub(r\"(?i)\\bsite\\s*:\\s*\\S+\", \" \", query_text)"` | — |
| [SRC-1AE03B9EC3-L000146](../../agents/web_agent.py#L146) | 146 | `"    query_tokens = {"` | — |
| [SRC-1AE03B9EC3-L000147](../../agents/web_agent.py#L147) | 147 | `"        token for token in re.findall(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", query_text)"` | — |
| [SRC-1AE03B9EC3-L000148](../../agents/web_agent.py#L148) | 148 | `"        if token not in _SEARCH_STOPWORDS and len(token) >= 2"` | — |
| [SRC-1AE03B9EC3-L000149](../../agents/web_agent.py#L149) | 149 | `"    }"` | — |
| [SRC-1AE03B9EC3-L000150](../../agents/web_agent.py#L150) | 150 | `"    if not query_tokens:"` | — |
| [SRC-1AE03B9EC3-L000151](../../agents/web_agent.py#L151) | 151 | `"        return 1.0"` | — |
| [SRC-1AE03B9EC3-L000152](../../agents/web_agent.py#L152) | 152 | `"    expanded_evidence = _search_tokens(evidence)"` | — |
| [SRC-1AE03B9EC3-L000153](../../agents/web_agent.py#L153) | 153 | `"    matched = sum("` | — |
| [SRC-1AE03B9EC3-L000154](../../agents/web_agent.py#L154) | 154 | `"        1 for token in query_tokens"` | — |
| [SRC-1AE03B9EC3-L000155](../../agents/web_agent.py#L155) | 155 | `"        if token in expanded_evidence"` | — |
| [SRC-1AE03B9EC3-L000156](../../agents/web_agent.py#L156) | 156 | `"        or (token.startswith(\"ال\") and token[2:] in expanded_evidence)"` | — |
| [SRC-1AE03B9EC3-L000157](../../agents/web_agent.py#L157) | 157 | `"        or bool(_NORMALIZED_SEARCH_SYNONYMS.get(token, set()) & expanded_evidence)"` | — |
| [SRC-1AE03B9EC3-L000158](../../agents/web_agent.py#L158) | 158 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000159](../../agents/web_agent.py#L159) | 159 | `"    ratio = matched / len(query_tokens)"` | — |
| [SRC-1AE03B9EC3-L000160](../../agents/web_agent.py#L160) | 160 | `"    # A single generic overlap is not enough for a longer query."` | — |
| [SRC-1AE03B9EC3-L000161](../../agents/web_agent.py#L161) | 161 | `"    if len(query_tokens) >= 4 and matched < 2:"` | — |
| [SRC-1AE03B9EC3-L000162](../../agents/web_agent.py#L162) | 162 | `"        return 0.0"` | — |
| [SRC-1AE03B9EC3-L000163](../../agents/web_agent.py#L163) | 163 | `"    return ratio"` | — |
| [SRC-1AE03B9EC3-L000164](../../agents/web_agent.py#L164) | 164 | `""` | — |
| [SRC-1AE03B9EC3-L000165](../../agents/web_agent.py#L165) | 165 | `""` | — |
| [SRC-1AE03B9EC3-L000166](../../agents/web_agent.py#L166) | 166 | `"def _blocked_source_url(url: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000167](../../agents/web_agent.py#L167) | 167 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000168](../../agents/web_agent.py#L168) | 168 | `"        host = (urllib.parse.urlparse(url).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L000169](../../agents/web_agent.py#L169) | 169 | `"        return any(host == domain or host.endswith(\".\" + domain) for domain in _BLOCKED_SOURCE_DOMAINS)"` | — |
| [SRC-1AE03B9EC3-L000170](../../agents/web_agent.py#L170) | 170 | `"    except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L000171](../../agents/web_agent.py#L171) | 171 | `"        return True"` | — |
| [SRC-1AE03B9EC3-L000172](../../agents/web_agent.py#L172) | 172 | `""` | — |
| [SRC-1AE03B9EC3-L000173](../../agents/web_agent.py#L173) | 173 | `""` | — |
| [SRC-1AE03B9EC3-L000174](../../agents/web_agent.py#L174) | 174 | `"class AgentDependencyError(RuntimeError):"` | — |
| [SRC-1AE03B9EC3-L000175](../../agents/web_agent.py#L175) | 175 | `"    \"\"\"A required optional runtime dependency is unavailable.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000176](../../agents/web_agent.py#L176) | 176 | `""` | — |
| [SRC-1AE03B9EC3-L000177](../../agents/web_agent.py#L177) | 177 | `""` | — |
| [SRC-1AE03B9EC3-L000178](../../agents/web_agent.py#L178) | 178 | `"def _clean_text(value: Any, limit: int) -> str:"` | — |
| [SRC-1AE03B9EC3-L000179](../../agents/web_agent.py#L179) | 179 | `"    if not isinstance(value, str):"` | — |
| [SRC-1AE03B9EC3-L000180](../../agents/web_agent.py#L180) | 180 | `"        return \"\""` | — |
| [SRC-1AE03B9EC3-L000181](../../agents/web_agent.py#L181) | 181 | `"    return \" \".join(value.replace(\"\\x00\", \" \").split())[:limit]"` | — |
| [SRC-1AE03B9EC3-L000182](../../agents/web_agent.py#L182) | 182 | `""` | — |
| [SRC-1AE03B9EC3-L000183](../../agents/web_agent.py#L183) | 183 | `""` | — |
| [SRC-1AE03B9EC3-L000184](../../agents/web_agent.py#L184) | 184 | `"def _public_http_url(value: Any) -> str \| None:"` | — |
| [SRC-1AE03B9EC3-L000185](../../agents/web_agent.py#L185) | 185 | `"    \"\"\"Lexically validate an HTTP URL before using it as a search source.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000186](../../agents/web_agent.py#L186) | 186 | `"    if not isinstance(value, str) or len(value) > 2048:"` | — |
| [SRC-1AE03B9EC3-L000187](../../agents/web_agent.py#L187) | 187 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000188](../../agents/web_agent.py#L188) | 188 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000189](../../agents/web_agent.py#L189) | 189 | `"        parsed = urllib.parse.urlparse(value.strip())"` | — |
| [SRC-1AE03B9EC3-L000190](../../agents/web_agent.py#L190) | 190 | `"        if parsed.scheme not in {\"http\", \"https\"}:"` | — |
| [SRC-1AE03B9EC3-L000191](../../agents/web_agent.py#L191) | 191 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000192](../../agents/web_agent.py#L192) | 192 | `"        if not parsed.hostname or parsed.username is not None or parsed.password is not None:"` | — |
| [SRC-1AE03B9EC3-L000193](../../agents/web_agent.py#L193) | 193 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000194](../../agents/web_agent.py#L194) | 194 | `"        if parsed.port not in (None, 80, 443):"` | — |
| [SRC-1AE03B9EC3-L000195](../../agents/web_agent.py#L195) | 195 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000196](../../agents/web_agent.py#L196) | 196 | `"        host = parsed.hostname.rstrip(\".\").lower()"` | — |
| [SRC-1AE03B9EC3-L000197](../../agents/web_agent.py#L197) | 197 | `"        if not host or host in {\"localhost\"} or host.endswith((\".local\", \".internal\", \".localhost\")):"` | — |
| [SRC-1AE03B9EC3-L000198](../../agents/web_agent.py#L198) | 198 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000199](../../agents/web_agent.py#L199) | 199 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000200](../../agents/web_agent.py#L200) | 200 | `"            ip = ipaddress.ip_address(host)"` | — |
| [SRC-1AE03B9EC3-L000201](../../agents/web_agent.py#L201) | 201 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L000202](../../agents/web_agent.py#L202) | 202 | `"            pass"` | — |
| [SRC-1AE03B9EC3-L000203](../../agents/web_agent.py#L203) | 203 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L000204](../../agents/web_agent.py#L204) | 204 | `"            if not ip.is_global:"` | — |
| [SRC-1AE03B9EC3-L000205](../../agents/web_agent.py#L205) | 205 | `"                return None"` | — |
| [SRC-1AE03B9EC3-L000206](../../agents/web_agent.py#L206) | 206 | `"        return urllib.parse.urlunparse(parsed._replace(fragment=\"\"))"` | — |
| [SRC-1AE03B9EC3-L000207](../../agents/web_agent.py#L207) | 207 | `"    except (ValueError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L000208](../../agents/web_agent.py#L208) | 208 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000209](../../agents/web_agent.py#L209) | 209 | `""` | — |
| [SRC-1AE03B9EC3-L000210](../../agents/web_agent.py#L210) | 210 | `""` | — |
| [SRC-1AE03B9EC3-L000211](../../agents/web_agent.py#L211) | 211 | `"def _public_ip_literals(host: str) -> list[str] \| None:"` | — |
| [SRC-1AE03B9EC3-L000212](../../agents/web_agent.py#L212) | 212 | `"    \"\"\"Resolve host and return its public addresses."` | — |
| [SRC-1AE03B9EC3-L000213](../../agents/web_agent.py#L213) | 213 | `""` | — |
| [SRC-1AE03B9EC3-L000214](../../agents/web_agent.py#L214) | 214 | `"    Returns None when resolution fails or any answer is not a global address."` | — |
| [SRC-1AE03B9EC3-L000215](../../agents/web_agent.py#L215) | 215 | `"    Callers must open the TCP connection to one of these literals. A second DNS"` | — |
| [SRC-1AE03B9EC3-L000216](../../agents/web_agent.py#L216) | 216 | `"    lookup is not equivalent: the name can be rebound to a private address"` | — |
| [SRC-1AE03B9EC3-L000217](../../agents/web_agent.py#L217) | 217 | `"    between the check and the connection (DNS rebinding / TOCTOU)."` | — |
| [SRC-1AE03B9EC3-L000218](../../agents/web_agent.py#L218) | 218 | `"    \"\"\""` | — |
| [SRC-1AE03B9EC3-L000219](../../agents/web_agent.py#L219) | 219 | `"    if not host:"` | — |
| [SRC-1AE03B9EC3-L000220](../../agents/web_agent.py#L220) | 220 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000221](../../agents/web_agent.py#L221) | 221 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000222](../../agents/web_agent.py#L222) | 222 | `"        answers = socket.getaddrinfo(host, None, type=socket.SOCK_STREAM)"` | — |
| [SRC-1AE03B9EC3-L000223](../../agents/web_agent.py#L223) | 223 | `"    except (OSError, socket.gaierror):"` | — |
| [SRC-1AE03B9EC3-L000224](../../agents/web_agent.py#L224) | 224 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000225](../../agents/web_agent.py#L225) | 225 | `"    if not answers:"` | — |
| [SRC-1AE03B9EC3-L000226](../../agents/web_agent.py#L226) | 226 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000227](../../agents/web_agent.py#L227) | 227 | `"    literals: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L000228](../../agents/web_agent.py#L228) | 228 | `"    for answer in answers:"` | — |
| [SRC-1AE03B9EC3-L000229](../../agents/web_agent.py#L229) | 229 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000230](../../agents/web_agent.py#L230) | 230 | `"            address = ipaddress.ip_address(answer[4][0])"` | — |
| [SRC-1AE03B9EC3-L000231](../../agents/web_agent.py#L231) | 231 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L000232](../../agents/web_agent.py#L232) | 232 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000233](../../agents/web_agent.py#L233) | 233 | `"        if not address.is_global:"` | — |
| [SRC-1AE03B9EC3-L000234](../../agents/web_agent.py#L234) | 234 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000235](../../agents/web_agent.py#L235) | 235 | `"        literal = str(address)"` | — |
| [SRC-1AE03B9EC3-L000236](../../agents/web_agent.py#L236) | 236 | `"        if literal not in literals:"` | — |
| [SRC-1AE03B9EC3-L000237](../../agents/web_agent.py#L237) | 237 | `"            literals.append(literal)"` | — |
| [SRC-1AE03B9EC3-L000238](../../agents/web_agent.py#L238) | 238 | `"    return literals or None"` | — |
| [SRC-1AE03B9EC3-L000239](../../agents/web_agent.py#L239) | 239 | `""` | — |
| [SRC-1AE03B9EC3-L000240](../../agents/web_agent.py#L240) | 240 | `""` | — |
| [SRC-1AE03B9EC3-L000241](../../agents/web_agent.py#L241) | 241 | `"def _host_resolves_publicly(host: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000242](../../agents/web_agent.py#L242) | 242 | `"    \"\"\"Reject local/private destinations before fetching a third-party page.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000243](../../agents/web_agent.py#L243) | 243 | `"    return _public_ip_literals(host) is not None"` | — |
| [SRC-1AE03B9EC3-L000244](../../agents/web_agent.py#L244) | 244 | `""` | — |
| [SRC-1AE03B9EC3-L000245](../../agents/web_agent.py#L245) | 245 | `""` | — |
| [SRC-1AE03B9EC3-L000246](../../agents/web_agent.py#L246) | 246 | `"def _pinned_connect_url(logical_url: str, ip: str) -> str \| None:"` | — |
| [SRC-1AE03B9EC3-L000247](../../agents/web_agent.py#L247) | 247 | `"    \"\"\"Rewrite a validated public URL so the connection target is a checked IP.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000248](../../agents/web_agent.py#L248) | 248 | `"    parsed = urllib.parse.urlparse(logical_url)"` | — |
| [SRC-1AE03B9EC3-L000249](../../agents/web_agent.py#L249) | 249 | `"    if parsed.port not in (None, 80, 443):"` | — |
| [SRC-1AE03B9EC3-L000250](../../agents/web_agent.py#L250) | 250 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000251](../../agents/web_agent.py#L251) | 251 | `"    literal = f\"[{ip}]\" if \":\" in ip else ip"` | — |
| [SRC-1AE03B9EC3-L000252](../../agents/web_agent.py#L252) | 252 | `"    netloc = literal if parsed.port is None else f\"{literal}:{parsed.port}\""` | — |
| [SRC-1AE03B9EC3-L000253](../../agents/web_agent.py#L253) | 253 | `"    return urllib.parse.urlunparse(parsed._replace(netloc=netloc))"` | — |
| [SRC-1AE03B9EC3-L000254](../../agents/web_agent.py#L254) | 254 | `""` | — |
| [SRC-1AE03B9EC3-L000255](../../agents/web_agent.py#L255) | 255 | `""` | — |
| [SRC-1AE03B9EC3-L000256](../../agents/web_agent.py#L256) | 256 | `"def _fallback_answer(sources: list[dict[str, Any]], reason: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000257](../../agents/web_agent.py#L257) | 257 | `"    lines = [reason]"` | — |
| [SRC-1AE03B9EC3-L000258](../../agents/web_agent.py#L258) | 258 | `"    usable = [source for source in sources if source.get(\"snippet\")]"` | — |
| [SRC-1AE03B9EC3-L000259](../../agents/web_agent.py#L259) | 259 | `"    for index, source in enumerate(usable[:5], 1):"` | — |
| [SRC-1AE03B9EC3-L000260](../../agents/web_agent.py#L260) | 260 | `"        lines.append("` | — |
| [SRC-1AE03B9EC3-L000261](../../agents/web_agent.py#L261) | 261 | `"            f\"{index}. {source.get('title', 'نتيجة ويب')}: \""` | — |
| [SRC-1AE03B9EC3-L000262](../../agents/web_agent.py#L262) | 262 | `"            f\"{source['snippet']} (المصدر: {source['url']})\""` | — |
| [SRC-1AE03B9EC3-L000263](../../agents/web_agent.py#L263) | 263 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000264](../../agents/web_agent.py#L264) | 264 | `"    if not usable:"` | — |
| [SRC-1AE03B9EC3-L000265](../../agents/web_agent.py#L265) | 265 | `"        lines.append(\"لم أتمكن من استخراج مقتطفات كافية من نتائج الويب.\")"` | — |
| [SRC-1AE03B9EC3-L000266](../../agents/web_agent.py#L266) | 266 | `"    return \"\\n\\n\".join(lines)"` | — |
| [SRC-1AE03B9EC3-L000267](../../agents/web_agent.py#L267) | 267 | `""` | — |
| [SRC-1AE03B9EC3-L000268](../../agents/web_agent.py#L268) | 268 | `""` | — |
| [SRC-1AE03B9EC3-L000269](../../agents/web_agent.py#L269) | 269 | `"class WebAgent:"` | — |
| [SRC-1AE03B9EC3-L000270](../../agents/web_agent.py#L270) | 270 | `"    \"\"\"Search, inspect, and synthesize web evidence for open-ended questions.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000271](../../agents/web_agent.py#L271) | 271 | `""` | — |
| [SRC-1AE03B9EC3-L000272](../../agents/web_agent.py#L272) | 272 | `"    def __init__(self) -> None:"` | — |
| [SRC-1AE03B9EC3-L000273](../../agents/web_agent.py#L273) | 273 | `"        self.api_key = ("` | — |
| [SRC-1AE03B9EC3-L000274](../../agents/web_agent.py#L274) | 274 | `"            os.getenv(\"OMARAI_LLM_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000275](../../agents/web_agent.py#L275) | 275 | `"            or os.getenv(\"OPENROUTER_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000276](../../agents/web_agent.py#L276) | 276 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000277](../../agents/web_agent.py#L277) | 277 | `"        self.base_url = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000278](../../agents/web_agent.py#L278) | 278 | `"            \"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\""` | — |
| [SRC-1AE03B9EC3-L000279](../../agents/web_agent.py#L279) | 279 | `"        ).strip().rstrip(\"/\")"` | — |
| [SRC-1AE03B9EC3-L000280](../../agents/web_agent.py#L280) | 280 | `"        # Pin explicit role models for more consistent behaviour than a random free router."` | — |
| [SRC-1AE03B9EC3-L000281](../../agents/web_agent.py#L281) | 281 | `"        # OMARAI_LLM_MODEL remains a global override for users who want one model everywhere."` | — |
| [SRC-1AE03B9EC3-L000282](../../agents/web_agent.py#L282) | 282 | `"        global_model = os.getenv(\"OMARAI_LLM_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000283](../../agents/web_agent.py#L283) | 283 | `"        self.answer_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000284](../../agents/web_agent.py#L284) | 284 | `"            \"OMARAI_ANSWER_MODEL\", global_model or \"google/gemma-4-31b-it:free\""` | — |
| [SRC-1AE03B9EC3-L000285](../../agents/web_agent.py#L285) | 285 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000286](../../agents/web_agent.py#L286) | 286 | `"        self.planner_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000287](../../agents/web_agent.py#L287) | 287 | `"            \"OMARAI_PLANNER_MODEL\","` | — |
| [SRC-1AE03B9EC3-L000288](../../agents/web_agent.py#L288) | 288 | `"            global_model or \"nvidia/nemotron-3-ultra-550b-a55b:free\","` | — |
| [SRC-1AE03B9EC3-L000289](../../agents/web_agent.py#L289) | 289 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000290](../../agents/web_agent.py#L290) | 290 | `"        self.review_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000291](../../agents/web_agent.py#L291) | 291 | `"            \"OMARAI_REVIEW_MODEL\", self.answer_model"` | — |
| [SRC-1AE03B9EC3-L000292](../../agents/web_agent.py#L292) | 292 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000293](../../agents/web_agent.py#L293) | 293 | `"        self.fallback_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000294](../../agents/web_agent.py#L294) | 294 | `"            \"OMARAI_LLM_FALLBACK_MODEL\", \"openrouter/free\""` | — |
| [SRC-1AE03B9EC3-L000295](../../agents/web_agent.py#L295) | 295 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000296](../../agents/web_agent.py#L296) | 296 | `"        self.model = self.answer_model  # Backwards-compatible alias."` | — |
| [SRC-1AE03B9EC3-L000297](../../agents/web_agent.py#L297) | 297 | `"        self.model_usage: list[dict[str, str]] = []"` | — |
| [SRC-1AE03B9EC3-L000298](../../agents/web_agent.py#L298) | 298 | `"        # Per-answer, bounded diagnostics contain only model identifiers and status metadata."` | — |
| [SRC-1AE03B9EC3-L000299](../../agents/web_agent.py#L299) | 299 | `"        # They intentionally exclude prompts, generated text, and provider response bodies."` | — |
| [SRC-1AE03B9EC3-L000300](../../agents/web_agent.py#L300) | 300 | `"        self.generation_diagnostics: list[dict[str, str]] = []"` | — |
| [SRC-1AE03B9EC3-L000301](../../agents/web_agent.py#L301) | 301 | `"        self.server_search_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L000302](../../agents/web_agent.py#L302) | 302 | `"        self._provider_diagnostics: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L000303](../../agents/web_agent.py#L303) | 303 | `"        self._provider_diagnostics_lock = threading.Lock()"` | — |
| [SRC-1AE03B9EC3-L000304](../../agents/web_agent.py#L304) | 304 | `"        self._deepseek_budget_lock = threading.Lock()"` | — |
| [SRC-1AE03B9EC3-L000305](../../agents/web_agent.py#L305) | 305 | `"        self._deepseek_search_requests_reserved = 0"` | — |
| [SRC-1AE03B9EC3-L000306](../../agents/web_agent.py#L306) | 306 | `"        self.openrouter_web_search_enabled = ("` | — |
| [SRC-1AE03B9EC3-L000307](../../agents/web_agent.py#L307) | 307 | `"            os.getenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"\").strip() == \"1\""` | — |
| [SRC-1AE03B9EC3-L000308](../../agents/web_agent.py#L308) | 308 | `"            and \"openrouter.ai\" in self.base_url.lower()"` | — |
| [SRC-1AE03B9EC3-L000309](../../agents/web_agent.py#L309) | 309 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000310](../../agents/web_agent.py#L310) | 310 | `"        self.timeout = max("` | — |
| [SRC-1AE03B9EC3-L000311](../../agents/web_agent.py#L311) | 311 | `"            5, min(int(os.getenv(\"OMARAI_LLM_TIMEOUT\", str(LLM_TIMEOUT_SECONDS))), 60)"` | — |
| [SRC-1AE03B9EC3-L000312](../../agents/web_agent.py#L312) | 312 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000313](../../agents/web_agent.py#L313) | 313 | `"        self._request_budget: RequestBudget \| None = None"` | — |
| [SRC-1AE03B9EC3-L000314](../../agents/web_agent.py#L314) | 314 | `""` | — |
| [SRC-1AE03B9EC3-L000315](../../agents/web_agent.py#L315) | 315 | `"    def _effective_timeout(self, configured_seconds: float) -> float:"` | — |
| [SRC-1AE03B9EC3-L000316](../../agents/web_agent.py#L316) | 316 | `"        \"\"\"Limit one outbound operation to the remaining per-answer time budget.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000317](../../agents/web_agent.py#L317) | 317 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L000318](../../agents/web_agent.py#L318) | 318 | `"        if budget is None:"` | — |
| [SRC-1AE03B9EC3-L000319](../../agents/web_agent.py#L319) | 319 | `"            return float(configured_seconds)"` | — |
| [SRC-1AE03B9EC3-L000320](../../agents/web_agent.py#L320) | 320 | `"        return budget.timeout_for(configured_seconds)"` | — |
| [SRC-1AE03B9EC3-L000321](../../agents/web_agent.py#L321) | 321 | `""` | — |
| [SRC-1AE03B9EC3-L000322](../../agents/web_agent.py#L322) | 322 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000323](../../agents/web_agent.py#L323) | 323 | `"    def status() -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L000324](../../agents/web_agent.py#L324) | 324 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000325](../../agents/web_agent.py#L325) | 325 | `"            import bs4  # noqa: F401"` | — |
| [SRC-1AE03B9EC3-L000326](../../agents/web_agent.py#L326) | 326 | `"            import httpx  # noqa: F401"` | — |
| [SRC-1AE03B9EC3-L000327](../../agents/web_agent.py#L327) | 327 | `"            search_ready = True"` | — |
| [SRC-1AE03B9EC3-L000328](../../agents/web_agent.py#L328) | 328 | `"        except ImportError:"` | — |
| [SRC-1AE03B9EC3-L000329](../../agents/web_agent.py#L329) | 329 | `"            search_ready = False"` | — |
| [SRC-1AE03B9EC3-L000330](../../agents/web_agent.py#L330) | 330 | `""` | — |
| [SRC-1AE03B9EC3-L000331](../../agents/web_agent.py#L331) | 331 | `"        global_model = os.getenv(\"OMARAI_LLM_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000332](../../agents/web_agent.py#L332) | 332 | `"        answer_model = ("` | — |
| [SRC-1AE03B9EC3-L000333](../../agents/web_agent.py#L333) | 333 | `"            os.getenv(\"OMARAI_ANSWER_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000334](../../agents/web_agent.py#L334) | 334 | `"            or global_model"` | — |
| [SRC-1AE03B9EC3-L000335](../../agents/web_agent.py#L335) | 335 | `"            or \"google/gemma-4-31b-it:free\""` | — |
| [SRC-1AE03B9EC3-L000336](../../agents/web_agent.py#L336) | 336 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000337](../../agents/web_agent.py#L337) | 337 | `"        planner_model = ("` | — |
| [SRC-1AE03B9EC3-L000338](../../agents/web_agent.py#L338) | 338 | `"            os.getenv(\"OMARAI_PLANNER_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000339](../../agents/web_agent.py#L339) | 339 | `"            or global_model"` | — |
| [SRC-1AE03B9EC3-L000340](../../agents/web_agent.py#L340) | 340 | `"            or \"nvidia/nemotron-3-ultra-550b-a55b:free\""` | — |
| [SRC-1AE03B9EC3-L000341](../../agents/web_agent.py#L341) | 341 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000342](../../agents/web_agent.py#L342) | 342 | `"        review_model = os.getenv(\"OMARAI_REVIEW_MODEL\", \"\").strip() or answer_model"` | — |
| [SRC-1AE03B9EC3-L000343](../../agents/web_agent.py#L343) | 343 | `"        fallback_model = ("` | — |
| [SRC-1AE03B9EC3-L000344](../../agents/web_agent.py#L344) | 344 | `"            os.getenv(\"OMARAI_LLM_FALLBACK_MODEL\", \"\").strip() or \"openrouter/free\""` | — |
| [SRC-1AE03B9EC3-L000345](../../agents/web_agent.py#L345) | 345 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000346](../../agents/web_agent.py#L346) | 346 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L000347](../../agents/web_agent.py#L347) | 347 | `"            \"web_search_ready\": search_ready,"` | — |
| [SRC-1AE03B9EC3-L000348](../../agents/web_agent.py#L348) | 348 | `"            \"language_model_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000349](../../agents/web_agent.py#L349) | 349 | `"                os.getenv(\"OMARAI_LLM_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000350](../../agents/web_agent.py#L350) | 350 | `"                or os.getenv(\"OPENROUTER_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000351](../../agents/web_agent.py#L351) | 351 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000352](../../agents/web_agent.py#L352) | 352 | `"            \"language_model_provider\": os.getenv("` | — |
| [SRC-1AE03B9EC3-L000353](../../agents/web_agent.py#L353) | 353 | `"                \"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\""` | — |
| [SRC-1AE03B9EC3-L000354](../../agents/web_agent.py#L354) | 354 | `"            ).strip().rstrip(\"/\"),"` | — |
| [SRC-1AE03B9EC3-L000355](../../agents/web_agent.py#L355) | 355 | `"            \"default_model\": answer_model,"` | — |
| [SRC-1AE03B9EC3-L000356](../../agents/web_agent.py#L356) | 356 | `"            \"planner_model\": planner_model,"` | — |
| [SRC-1AE03B9EC3-L000357](../../agents/web_agent.py#L357) | 357 | `"            \"answer_model\": answer_model,"` | — |
| [SRC-1AE03B9EC3-L000358](../../agents/web_agent.py#L358) | 358 | `"            \"review_model\": review_model,"` | — |
| [SRC-1AE03B9EC3-L000359](../../agents/web_agent.py#L359) | 359 | `"            \"fallback_model\": fallback_model,"` | — |
| [SRC-1AE03B9EC3-L000360](../../agents/web_agent.py#L360) | 360 | `"            \"model_selection_mode\": \"role_specific_with_fallback\","` | — |
| [SRC-1AE03B9EC3-L000361](../../agents/web_agent.py#L361) | 361 | `"            \"external_model_privacy_notice\": ("` | — |
| [SRC-1AE03B9EC3-L000362](../../agents/web_agent.py#L362) | 362 | `"                \"Prompts and selected page excerpts are sent to the configured external model provider. \""` | — |
| [SRC-1AE03B9EC3-L000363](../../agents/web_agent.py#L363) | 363 | `"                \"Do not submit secrets or personal/confidential customer data. The default free NVIDIA \""` | — |
| [SRC-1AE03B9EC3-L000364](../../agents/web_agent.py#L364) | 364 | `"                \"Nemotron endpoint states that sessions may be logged for security and product improvement.\""` | — |
| [SRC-1AE03B9EC3-L000365](../../agents/web_agent.py#L365) | 365 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000366](../../agents/web_agent.py#L366) | 366 | `"            \"search_providers\": ["` | — |
| [SRC-1AE03B9EC3-L000367](../../agents/web_agent.py#L367) | 367 | `"                \"DuckDuckGo HTML\","` | — |
| [SRC-1AE03B9EC3-L000368](../../agents/web_agent.py#L368) | 368 | `"                \"Bing RSS\","` | — |
| [SRC-1AE03B9EC3-L000369](../../agents/web_agent.py#L369) | 369 | `"                \"Google News RSS for fresh queries\","` | — |
| [SRC-1AE03B9EC3-L000370](../../agents/web_agent.py#L370) | 370 | `"                \"DeepSeek Search API when DEEPSEEK_SEARCH_API_KEY is configured (optional; may incur charges)\","` | — |
| [SRC-1AE03B9EC3-L000371](../../agents/web_agent.py#L371) | 371 | `"                \"OpenRouter server-side live web search when OMARAI_OPENROUTER_WEB_SEARCH=1\","` | — |
| [SRC-1AE03B9EC3-L000372](../../agents/web_agent.py#L372) | 372 | `"                \"Brave Search API when BRAVE_SEARCH_API_KEY is configured\","` | — |
| [SRC-1AE03B9EC3-L000373](../../agents/web_agent.py#L373) | 373 | `"                \"Tavily Search API when TAVILY_API_KEY is configured\","` | — |
| [SRC-1AE03B9EC3-L000374](../../agents/web_agent.py#L374) | 374 | `"            ],"` | — |
| [SRC-1AE03B9EC3-L000375](../../agents/web_agent.py#L375) | 375 | `"            \"brave_search_api_configured\": bool(os.getenv(\"BRAVE_SEARCH_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000376](../../agents/web_agent.py#L376) | 376 | `"            \"deepseek_search_api_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000377](../../agents/web_agent.py#L377) | 377 | `"                os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000378](../../agents/web_agent.py#L378) | 378 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000379](../../agents/web_agent.py#L379) | 379 | `"            \"tavily_search_api_configured\": bool(os.getenv(\"TAVILY_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000380](../../agents/web_agent.py#L380) | 380 | `"            \"openrouter_web_search_enabled\": ("` | — |
| [SRC-1AE03B9EC3-L000381](../../agents/web_agent.py#L381) | 381 | `"                os.getenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"\").strip() == \"1\""` | — |
| [SRC-1AE03B9EC3-L000382](../../agents/web_agent.py#L382) | 382 | `"                and \"openrouter.ai\" in os.getenv("` | — |
| [SRC-1AE03B9EC3-L000383](../../agents/web_agent.py#L383) | 383 | `"                    \"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\""` | — |
| [SRC-1AE03B9EC3-L000384](../../agents/web_agent.py#L384) | 384 | `"                ).lower()"` | — |
| [SRC-1AE03B9EC3-L000385](../../agents/web_agent.py#L385) | 385 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000386](../../agents/web_agent.py#L386) | 386 | `"            \"public_social_sources\": ["` | — |
| [SRC-1AE03B9EC3-L000387](../../agents/web_agent.py#L387) | 387 | `"                \"Reddit public RSS and optional authorized Reddit OAuth search\","` | — |
| [SRC-1AE03B9EC3-L000388](../../agents/web_agent.py#L388) | 388 | `"                \"Bluesky public search\","` | — |
| [SRC-1AE03B9EC3-L000389](../../agents/web_agent.py#L389) | 389 | `"                \"indexed public pages from Facebook, Instagram, X, TikTok, LinkedIn, Threads and YouTube\","` | — |
| [SRC-1AE03B9EC3-L000390](../../agents/web_agent.py#L390) | 390 | `"                \"official Instagram public hashtag media when an authorized Graph API token is configured\","` | — |
| [SRC-1AE03B9EC3-L000391](../../agents/web_agent.py#L391) | 391 | `"                \"configured Facebook Pages when a valid authorized page token is configured\","` | — |
| [SRC-1AE03B9EC3-L000392](../../agents/web_agent.py#L392) | 392 | `"                \"official X recent-post API when X_BEARER_TOKEN is configured\","` | — |
| [SRC-1AE03B9EC3-L000393](../../agents/web_agent.py#L393) | 393 | `"            ],"` | — |
| [SRC-1AE03B9EC3-L000394](../../agents/web_agent.py#L394) | 394 | `"            \"reddit_oauth_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000395](../../agents/web_agent.py#L395) | 395 | `"                os.getenv(\"REDDIT_CLIENT_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000396](../../agents/web_agent.py#L396) | 396 | `"                and os.getenv(\"REDDIT_CLIENT_SECRET\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000397](../../agents/web_agent.py#L397) | 397 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000398](../../agents/web_agent.py#L398) | 398 | `"            \"facebook_pages_api_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000399](../../agents/web_agent.py#L399) | 399 | `"                os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000400](../../agents/web_agent.py#L400) | 400 | `"                and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000401](../../agents/web_agent.py#L401) | 401 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000402](../../agents/web_agent.py#L402) | 402 | `"            \"x_api_configured\": bool(os.getenv(\"X_BEARER_TOKEN\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000403](../../agents/web_agent.py#L403) | 403 | `"            \"instagram_graph_api_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000404](../../agents/web_agent.py#L404) | 404 | `"                os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000405](../../agents/web_agent.py#L405) | 405 | `"                and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000406](../../agents/web_agent.py#L406) | 406 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000407](../../agents/web_agent.py#L407) | 407 | `"            \"meta_graph_version\": os.getenv(\"META_GRAPH_VERSION\", \"v25.0\").strip(),"` | — |
| [SRC-1AE03B9EC3-L000408](../../agents/web_agent.py#L408) | 408 | `"            \"youtube_api_configured\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000409](../../agents/web_agent.py#L409) | 409 | `"            \"youtube_direct_api\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000410](../../agents/web_agent.py#L410) | 410 | `"            \"verification_scope\": {"` | — |
| [SRC-1AE03B9EC3-L000411](../../agents/web_agent.py#L411) | 411 | `"                \"kind\": \"configuration_snapshot\","` | — |
| [SRC-1AE03B9EC3-L000412](../../agents/web_agent.py#L412) | 412 | `"                \"live_network_checks_performed\": False,"` | — |
| [SRC-1AE03B9EC3-L000413](../../agents/web_agent.py#L413) | 413 | `"                \"web_search_ready_means\": \"dependencies_importable_not_provider_connectivity\","` | — |
| [SRC-1AE03B9EC3-L000414](../../agents/web_agent.py#L414) | 414 | `"                \"language_model_configured_means\": \"credential_present_not_successful_completion\","` | — |
| [SRC-1AE03B9EC3-L000415](../../agents/web_agent.py#L415) | 415 | `"                \"search_providers_means\": \"supported_or_conditionally_configured_not_live_verified\","` | — |
| [SRC-1AE03B9EC3-L000416](../../agents/web_agent.py#L416) | 416 | `"                \"direct_social_api_flags_mean\": \"credentials_present_not_permissions_or_connectivity_verified\","` | — |
| [SRC-1AE03B9EC3-L000417](../../agents/web_agent.py#L417) | 417 | `"                \"live_diagnostics_endpoint\": \"POST /api/diagnostics\","` | — |
| [SRC-1AE03B9EC3-L000418](../../agents/web_agent.py#L418) | 418 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000419](../../agents/web_agent.py#L419) | 419 | `"        }"` | — |
| [SRC-1AE03B9EC3-L000420](../../agents/web_agent.py#L420) | 420 | `""` | — |
| [SRC-1AE03B9EC3-L000421](../../agents/web_agent.py#L421) | 421 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000422](../../agents/web_agent.py#L422) | 422 | `"    def _unwrap_search_url(value: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000423](../../agents/web_agent.py#L423) | 423 | `"        if value.startswith(\"//\"):"` | — |
| [SRC-1AE03B9EC3-L000424](../../agents/web_agent.py#L424) | 424 | `"            value = \"https:\" + value"` | — |
| [SRC-1AE03B9EC3-L000425](../../agents/web_agent.py#L425) | 425 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000426](../../agents/web_agent.py#L426) | 426 | `"            parsed = urllib.parse.urlparse(value)"` | — |
| [SRC-1AE03B9EC3-L000427](../../agents/web_agent.py#L427) | 427 | `"            host = (parsed.hostname or \"\").lower()"` | — |
| [SRC-1AE03B9EC3-L000428](../../agents/web_agent.py#L428) | 428 | `"            if host.endswith(\"duckduckgo.com\") and parsed.path.startswith(\"/l/\"):"` | — |
| [SRC-1AE03B9EC3-L000429](../../agents/web_agent.py#L429) | 429 | `"                target = urllib.parse.parse_qs(parsed.query).get(\"uddg\", [\"\"])[0]"` | — |
| [SRC-1AE03B9EC3-L000430](../../agents/web_agent.py#L430) | 430 | `"                return urllib.parse.unquote(target) if target else \"\""` | — |
| [SRC-1AE03B9EC3-L000431](../../agents/web_agent.py#L431) | 431 | `"        except (ValueError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L000432](../../agents/web_agent.py#L432) | 432 | `"            return \"\""` | — |
| [SRC-1AE03B9EC3-L000433](../../agents/web_agent.py#L433) | 433 | `"        return value"` | — |
| [SRC-1AE03B9EC3-L000434](../../agents/web_agent.py#L434) | 434 | `""` | — |
| [SRC-1AE03B9EC3-L000435](../../agents/web_agent.py#L435) | 435 | `"    def _record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L000436](../../agents/web_agent.py#L436) | 436 | `"        self, provider: str, query: str, status: str, result_count: int = 0,"` | — |
| [SRC-1AE03B9EC3-L000437](../../agents/web_agent.py#L437) | 437 | `"        rejected_count: int = 0, error: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L000438](../../agents/web_agent.py#L438) | 438 | `"    ) -> None:"` | — |
| [SRC-1AE03B9EC3-L000439](../../agents/web_agent.py#L439) | 439 | `"        record = {"` | — |
| [SRC-1AE03B9EC3-L000440](../../agents/web_agent.py#L440) | 440 | `"            \"provider\": provider,"` | — |
| [SRC-1AE03B9EC3-L000441](../../agents/web_agent.py#L441) | 441 | `"            \"query\": _clean_text(query, 220),"` | — |
| [SRC-1AE03B9EC3-L000442](../../agents/web_agent.py#L442) | 442 | `"            \"status\": status,"` | — |
| [SRC-1AE03B9EC3-L000443](../../agents/web_agent.py#L443) | 443 | `"            \"result_count\": int(result_count),"` | — |
| [SRC-1AE03B9EC3-L000444](../../agents/web_agent.py#L444) | 444 | `"            \"rejected_count\": int(rejected_count),"` | — |
| [SRC-1AE03B9EC3-L000445](../../agents/web_agent.py#L445) | 445 | `"        }"` | — |
| [SRC-1AE03B9EC3-L000446](../../agents/web_agent.py#L446) | 446 | `"        if error:"` | — |
| [SRC-1AE03B9EC3-L000447](../../agents/web_agent.py#L447) | 447 | `"            record[\"error\"] = _clean_text(error, 180)"` | — |
| [SRC-1AE03B9EC3-L000448](../../agents/web_agent.py#L448) | 448 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L000449](../../agents/web_agent.py#L449) | 449 | `"            self._provider_diagnostics.append(record)"` | — |
| [SRC-1AE03B9EC3-L000450](../../agents/web_agent.py#L450) | 450 | `"            # Bound memory when the instance serves many user requests."` | — |
| [SRC-1AE03B9EC3-L000451](../../agents/web_agent.py#L451) | 451 | `"            self._provider_diagnostics = self._provider_diagnostics[-160:]"` | — |
| [SRC-1AE03B9EC3-L000452](../../agents/web_agent.py#L452) | 452 | `""` | — |
| [SRC-1AE03B9EC3-L000453](../../agents/web_agent.py#L453) | 453 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000454](../../agents/web_agent.py#L454) | 454 | `"    def _source_matches_query(query: str, source: dict[str, Any]) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000455](../../agents/web_agent.py#L455) | 455 | `"        if \"user_supplied_url\" in source.get(\"providers\", []):"` | — |
| [SRC-1AE03B9EC3-L000456](../../agents/web_agent.py#L456) | 456 | `"            return True"` | — |
| [SRC-1AE03B9EC3-L000457](../../agents/web_agent.py#L457) | 457 | `"        evidence = \" \".join("` | — |
| [SRC-1AE03B9EC3-L000458](../../agents/web_agent.py#L458) | 458 | `"            str(source.get(key) or \"\")"` | — |
| [SRC-1AE03B9EC3-L000459](../../agents/web_agent.py#L459) | 459 | `"            for key in (\"title\", \"snippet\", \"page_text\")"` | — |
| [SRC-1AE03B9EC3-L000460](../../agents/web_agent.py#L460) | 460 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000461](../../agents/web_agent.py#L461) | 461 | `"        return _relevance_ratio(query, evidence) >= 0.20"` | — |
| [SRC-1AE03B9EC3-L000462](../../agents/web_agent.py#L462) | 462 | `""` | — |
| [SRC-1AE03B9EC3-L000463](../../agents/web_agent.py#L463) | 463 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000464](../../agents/web_agent.py#L464) | 464 | `"    def _normalized_source_url_key(value: Any) -> str:"` | — |
| [SRC-1AE03B9EC3-L000465](../../agents/web_agent.py#L465) | 465 | `"        \"\"\"Normalize a public HTTP(S) URL for duplicate detection across search rounds.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000466](../../agents/web_agent.py#L466) | 466 | `"        if not isinstance(value, str) or not value.strip():"` | — |
| [SRC-1AE03B9EC3-L000467](../../agents/web_agent.py#L467) | 467 | `"            return \"\""` | — |
| [SRC-1AE03B9EC3-L000468](../../agents/web_agent.py#L468) | 468 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000469](../../agents/web_agent.py#L469) | 469 | `"            parsed = urllib.parse.urlsplit(value.strip())"` | — |
| [SRC-1AE03B9EC3-L000470](../../agents/web_agent.py#L470) | 470 | `"            scheme = parsed.scheme.lower()"` | — |
| [SRC-1AE03B9EC3-L000471](../../agents/web_agent.py#L471) | 471 | `"            if scheme not in {\"http\", \"https\"} or not parsed.hostname:"` | — |
| [SRC-1AE03B9EC3-L000472](../../agents/web_agent.py#L472) | 472 | `"                return \"\""` | — |
| [SRC-1AE03B9EC3-L000473](../../agents/web_agent.py#L473) | 473 | `"            host = parsed.hostname.lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L000474](../../agents/web_agent.py#L474) | 474 | `"            port = parsed.port"` | — |
| [SRC-1AE03B9EC3-L000475](../../agents/web_agent.py#L475) | 475 | `"            if (scheme == \"https\" and port == 443) or (scheme == \"http\" and port == 80):"` | — |
| [SRC-1AE03B9EC3-L000476](../../agents/web_agent.py#L476) | 476 | `"                port = None"` | — |
| [SRC-1AE03B9EC3-L000477](../../agents/web_agent.py#L477) | 477 | `"            host_for_url = f\"[{host}]\" if \":\" in host else host"` | — |
| [SRC-1AE03B9EC3-L000478](../../agents/web_agent.py#L478) | 478 | `"            netloc = host_for_url + (f\":{port}\" if port is not None else \"\")"` | — |
| [SRC-1AE03B9EC3-L000479](../../agents/web_agent.py#L479) | 479 | `"            path = parsed.path.rstrip(\"/\") or \"/\""` | — |
| [SRC-1AE03B9EC3-L000480](../../agents/web_agent.py#L480) | 480 | `"            tracking_keys = {\"fbclid\", \"gclid\", \"ref\", \"source\"}"` | — |
| [SRC-1AE03B9EC3-L000481](../../agents/web_agent.py#L481) | 481 | `"            query_items = ["` | — |
| [SRC-1AE03B9EC3-L000482](../../agents/web_agent.py#L482) | 482 | `"                (key, item)"` | — |
| [SRC-1AE03B9EC3-L000483](../../agents/web_agent.py#L483) | 483 | `"                for key, item in urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)"` | — |
| [SRC-1AE03B9EC3-L000484](../../agents/web_agent.py#L484) | 484 | `"                if not key.lower().startswith(\"utm_\") and key.lower() not in tracking_keys"` | — |
| [SRC-1AE03B9EC3-L000485](../../agents/web_agent.py#L485) | 485 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L000486](../../agents/web_agent.py#L486) | 486 | `"            query = urllib.parse.urlencode(query_items, doseq=True)"` | — |
| [SRC-1AE03B9EC3-L000487](../../agents/web_agent.py#L487) | 487 | `"            return urllib.parse.urlunsplit((scheme, netloc, path, query, \"\"))"` | — |
| [SRC-1AE03B9EC3-L000488](../../agents/web_agent.py#L488) | 488 | `"        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L000489](../../agents/web_agent.py#L489) | 489 | `"            return \"\""` | — |
| [SRC-1AE03B9EC3-L000490](../../agents/web_agent.py#L490) | 490 | `""` | — |
| [SRC-1AE03B9EC3-L000491](../../agents/web_agent.py#L491) | 491 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000492](../../agents/web_agent.py#L492) | 492 | `"    def _question_coverage_targets(question: str) -> list[str]:"` | — |
| [SRC-1AE03B9EC3-L000493](../../agents/web_agent.py#L493) | 493 | `"        \"\"\"Extract explicit multi-part answer requirements conservatively; this is not semantic grading.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000494](../../agents/web_agent.py#L494) | 494 | `"        if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-1AE03B9EC3-L000495](../../agents/web_agent.py#L495) | 495 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L000496](../../agents/web_agent.py#L496) | 496 | `"        text = question.strip()[:MAX_QUESTION_CHARS]"` | — |
| [SRC-1AE03B9EC3-L000497](../../agents/web_agent.py#L497) | 497 | `"        marker = re.compile("` | — |
| [SRC-1AE03B9EC3-L000498](../../agents/web_agent.py#L498) | 498 | `"            r\"(?:من\\s+حيث\|من\\s+ناحية\|من\\s+الناحية\|فيما\\s+يتعلق\\s+ب\|فيما\\s+يخص\|\""` | — |
| [SRC-1AE03B9EC3-L000499](../../agents/web_agent.py#L499) | 499 | `"            r\"من\\s+منظور\|in\\s+terms\\s+of\|with\\s+respect\\s+to\|\""` | — |
| [SRC-1AE03B9EC3-L000500](../../agents/web_agent.py#L500) | 500 | `"            r\"from\\s+the\\s+perspective\\s+of\|based\\s+on\\s+the\\s+following\\s+criteria)\""` | — |
| [SRC-1AE03B9EC3-L000501](../../agents/web_agent.py#L501) | 501 | `"            r\"\\s*(.+?)(?=[؟?!.؛;\\n]\|$)\","` | — |
| [SRC-1AE03B9EC3-L000502](../../agents/web_agent.py#L502) | 502 | `"            flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L000503](../../agents/web_agent.py#L503) | 503 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000504](../../agents/web_agent.py#L504) | 504 | `"        match = marker.search(text)"` | — |
| [SRC-1AE03B9EC3-L000505](../../agents/web_agent.py#L505) | 505 | `"        if match:"` | — |
| [SRC-1AE03B9EC3-L000506](../../agents/web_agent.py#L506) | 506 | `"            raw = match.group(1)"` | — |
| [SRC-1AE03B9EC3-L000507](../../agents/web_agent.py#L507) | 507 | `"            # Keep explicit criteria separate from trailing meta-requests such as"` | — |
| [SRC-1AE03B9EC3-L000508](../../agents/web_agent.py#L508) | 508 | `"            # \"explain what cannot be verified\" rather than turning them into a criterion."` | — |
| [SRC-1AE03B9EC3-L000509](../../agents/web_agent.py#L509) | 509 | `"            raw = re.split("` | — |
| [SRC-1AE03B9EC3-L000510](../../agents/web_agent.py#L510) | 510 | `"                r\"(?:،\|,\|؛\|;)\\s*(?:و?اذكر\|و?وضح\|بيّن\|اشرح\|and\\s+(?:explain\|note\|discuss))\\b\","` | — |
| [SRC-1AE03B9EC3-L000511](../../agents/web_agent.py#L511) | 511 | `"                raw,"` | — |
| [SRC-1AE03B9EC3-L000512](../../agents/web_agent.py#L512) | 512 | `"                maxsplit=1,"` | — |
| [SRC-1AE03B9EC3-L000513](../../agents/web_agent.py#L513) | 513 | `"                flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L000514](../../agents/web_agent.py#L514) | 514 | `"            )[0]"` | — |
| [SRC-1AE03B9EC3-L000515](../../agents/web_agent.py#L515) | 515 | `"            pieces = re.split("` | — |
| [SRC-1AE03B9EC3-L000516](../../agents/web_agent.py#L516) | 516 | `"                r\"\\s*(?:،\|,\|؛\|;\|/)\\s*\|\""` | — |
| [SRC-1AE03B9EC3-L000517](../../agents/web_agent.py#L517) | 517 | `"                r\"\\s+\\band\\b\\s+\|\\s+\\bas well as\\b\\s+\|\""` | — |
| [SRC-1AE03B9EC3-L000518](../../agents/web_agent.py#L518) | 518 | `"                r\"\\s+و(?=ال\|[ء-ي])\","` | — |
| [SRC-1AE03B9EC3-L000519](../../agents/web_agent.py#L519) | 519 | `"                raw,"` | — |
| [SRC-1AE03B9EC3-L000520](../../agents/web_agent.py#L520) | 520 | `"                flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L000521](../../agents/web_agent.py#L521) | 521 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000522](../../agents/web_agent.py#L522) | 522 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L000523](../../agents/web_agent.py#L523) | 523 | `"            # If the user explicitly asks separate questions, preserve each clause."` | — |
| [SRC-1AE03B9EC3-L000524](../../agents/web_agent.py#L524) | 524 | `"            question_parts = ["` | — |
| [SRC-1AE03B9EC3-L000525](../../agents/web_agent.py#L525) | 525 | `"                part.strip(\" \\t\\r\\n-•\")"` | — |
| [SRC-1AE03B9EC3-L000526](../../agents/web_agent.py#L526) | 526 | `"                for part in re.split(r\"[؟?]+\", text)"` | — |
| [SRC-1AE03B9EC3-L000527](../../agents/web_agent.py#L527) | 527 | `"                if len(part.strip(\" \\t\\r\\n-•\")) >= 4"` | — |
| [SRC-1AE03B9EC3-L000528](../../agents/web_agent.py#L528) | 528 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L000529](../../agents/web_agent.py#L529) | 529 | `"            pieces = question_parts if len(question_parts) > 1 else []"` | — |
| [SRC-1AE03B9EC3-L000530](../../agents/web_agent.py#L530) | 530 | `""` | — |
| [SRC-1AE03B9EC3-L000531](../../agents/web_agent.py#L531) | 531 | `"        targets: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L000532](../../agents/web_agent.py#L532) | 532 | `"        seen: set[str] = set()"` | — |
| [SRC-1AE03B9EC3-L000533](../../agents/web_agent.py#L533) | 533 | `"        for piece in pieces:"` | — |
| [SRC-1AE03B9EC3-L000534](../../agents/web_agent.py#L534) | 534 | `"            target = re.sub(r\"^[\\s:،,؛;/.!?\\-–—]+\|[\\s:،,؛;/.!?\\-–—]+$\", \"\", piece).strip()"` | — |
| [SRC-1AE03B9EC3-L000535](../../agents/web_agent.py#L535) | 535 | `"            target = re.sub(r\"^(?:و\\s*)\", \"\", target).strip()"` | — |
| [SRC-1AE03B9EC3-L000536](../../agents/web_agent.py#L536) | 536 | `"            if len(target) < 2:"` | — |
| [SRC-1AE03B9EC3-L000537](../../agents/web_agent.py#L537) | 537 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L000538](../../agents/web_agent.py#L538) | 538 | `"            if len(target) > 120:"` | — |
| [SRC-1AE03B9EC3-L000539](../../agents/web_agent.py#L539) | 539 | `"                target = target[:120].rsplit(\" \", 1)[0].strip()"` | — |
| [SRC-1AE03B9EC3-L000540](../../agents/web_agent.py#L540) | 540 | `"            key = _normalize_search_query(target).casefold()"` | — |
| [SRC-1AE03B9EC3-L000541](../../agents/web_agent.py#L541) | 541 | `"            if key and key not in seen:"` | — |
| [SRC-1AE03B9EC3-L000542](../../agents/web_agent.py#L542) | 542 | `"                seen.add(key)"` | — |
| [SRC-1AE03B9EC3-L000543](../../agents/web_agent.py#L543) | 543 | `"                targets.append(target)"` | — |
| [SRC-1AE03B9EC3-L000544](../../agents/web_agent.py#L544) | 544 | `"            if len(targets) >= 8:"` | — |
| [SRC-1AE03B9EC3-L000545](../../agents/web_agent.py#L545) | 545 | `"                break"` | — |
| [SRC-1AE03B9EC3-L000546](../../agents/web_agent.py#L546) | 546 | `"        return targets"` | — |
| [SRC-1AE03B9EC3-L000547](../../agents/web_agent.py#L547) | 547 | `""` | — |
| [SRC-1AE03B9EC3-L000548](../../agents/web_agent.py#L548) | 548 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000549](../../agents/web_agent.py#L549) | 549 | `"    def _is_current_search_status_question(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000550](../../agents/web_agent.py#L550) | 550 | `"        \"\"\"Recognize a question about whether this answer already used web search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000551](../../agents/web_agent.py#L551) | 551 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000552](../../agents/web_agent.py#L552) | 552 | `"        asks_if_searched = any("` | — |
| [SRC-1AE03B9EC3-L000553](../../agents/web_agent.py#L553) | 553 | `"            term in value"` | — |
| [SRC-1AE03B9EC3-L000554](../../agents/web_agent.py#L554) | 554 | `"            for term in (\"بحثت\", \"اجريت بحث\", \"قمت بالبحث\", \"عملت بحث\", \"did you search\", \"did you browse\")"` | — |
| [SRC-1AE03B9EC3-L000555](../../agents/web_agent.py#L555) | 555 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000556](../../agents/web_agent.py#L556) | 556 | `"        references_web = any("` | — |
| [SRC-1AE03B9EC3-L000557](../../agents/web_agent.py#L557) | 557 | `"            term in value for term in (\"انترنت\", \"النت\", \"الويب\", \"ويب\", \"the web\", \"online\")"` | — |
| [SRC-1AE03B9EC3-L000558](../../agents/web_agent.py#L558) | 558 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000559](../../agents/web_agent.py#L559) | 559 | `"        references_current_answer = any("` | — |
| [SRC-1AE03B9EC3-L000560](../../agents/web_agent.py#L560) | 560 | `"            term in value"` | — |
| [SRC-1AE03B9EC3-L000561](../../agents/web_agent.py#L561) | 561 | `"            for term in ("` | — |
| [SRC-1AE03B9EC3-L000562](../../agents/web_agent.py#L562) | 562 | `"                \"اجاب\", \"الرد الحالي\", \"هذا السؤال\", \"هذه الاجابه\","` | — |
| [SRC-1AE03B9EC3-L000563](../../agents/web_agent.py#L563) | 563 | `"                \"this answer\", \"this response\","` | — |
| [SRC-1AE03B9EC3-L000564](../../agents/web_agent.py#L564) | 564 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000565](../../agents/web_agent.py#L565) | 565 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000566](../../agents/web_agent.py#L566) | 566 | `"        return asks_if_searched and references_web and references_current_answer"` | — |
| [SRC-1AE03B9EC3-L000567](../../agents/web_agent.py#L567) | 567 | `""` | — |
| [SRC-1AE03B9EC3-L000568](../../agents/web_agent.py#L568) | 568 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000569](../../agents/web_agent.py#L569) | 569 | `"    def _is_self_question(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000570](../../agents/web_agent.py#L570) | 570 | `"        \"\"\"Recognize questions about Omarai itself so they do not need web search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000571](../../agents/web_agent.py#L571) | 571 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000572](../../agents/web_agent.py#L572) | 572 | `"        capability_phrases = ("` | — |
| [SRC-1AE03B9EC3-L000573](../../agents/web_agent.py#L573) | 573 | `"            \"كيف تستطيع مساعدتي\", \"ازاي تقدر تساعدني\", \"ازاي ممكن تساعدني\","` | — |
| [SRC-1AE03B9EC3-L000574](../../agents/web_agent.py#L574) | 574 | `"            \"ماذا تستطيع ان تفعل\", \"ما الذي تستطيع فعله\", \"ايه اللي تقدر تعمله\","` | — |
| [SRC-1AE03B9EC3-L000575](../../agents/web_agent.py#L575) | 575 | `"            \"what can you do\", \"how can you help me\","` | — |
| [SRC-1AE03B9EC3-L000576](../../agents/web_agent.py#L576) | 576 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000577](../../agents/web_agent.py#L577) | 577 | `"        search_phrases = ("` | — |
| [SRC-1AE03B9EC3-L000578](../../agents/web_agent.py#L578) | 578 | `"            \"كيف تبحث انت\", \"ازاي بتبحث\", \"كيف يعمل البحث عندك\","` | — |
| [SRC-1AE03B9EC3-L000579](../../agents/web_agent.py#L579) | 579 | `"            \"ما المواقع التي تستخدمها\", \"ما محركات البحث التي تستخدمها\","` | — |
| [SRC-1AE03B9EC3-L000580](../../agents/web_agent.py#L580) | 580 | `"            \"ما المواقع التي قدرت\", \"كيف تبحث على الانترنت\","` | — |
| [SRC-1AE03B9EC3-L000581](../../agents/web_agent.py#L581) | 581 | `"            \"هل تستطيع البحث\", \"هل يمكنك البحث\", \"هل تقدر تبحث\","` | — |
| [SRC-1AE03B9EC3-L000582](../../agents/web_agent.py#L582) | 582 | `"            \"هل تستطيع الوصول\", \"هل يمكنك الوصول\","` | — |
| [SRC-1AE03B9EC3-L000583](../../agents/web_agent.py#L583) | 583 | `"            \"هل عندك اتصال بالانترنت\", \"هل عندك اتصال بالانترنيت\","` | — |
| [SRC-1AE03B9EC3-L000584](../../agents/web_agent.py#L584) | 584 | `"            \"هل عندك انترنت\","` | — |
| [SRC-1AE03B9EC3-L000585](../../agents/web_agent.py#L585) | 585 | `"            \"هل بحثت في الانترنت للاجابه الحاليه\","` | — |
| [SRC-1AE03B9EC3-L000586](../../agents/web_agent.py#L586) | 586 | `"            \"هل بحثت علي الانترنت للاجابه الحاليه\","` | — |
| [SRC-1AE03B9EC3-L000587](../../agents/web_agent.py#L587) | 587 | `"            \"هل بحثت في الانترنت لهذا السؤال\","` | — |
| [SRC-1AE03B9EC3-L000588](../../agents/web_agent.py#L588) | 588 | `"            \"هل بحثت في النت للرد ده\","` | — |
| [SRC-1AE03B9EC3-L000589](../../agents/web_agent.py#L589) | 589 | `"            \"did you search the web for this answer\","` | — |
| [SRC-1AE03B9EC3-L000590](../../agents/web_agent.py#L590) | 590 | `"            \"did you browse for this response\","` | — |
| [SRC-1AE03B9EC3-L000591](../../agents/web_agent.py#L591) | 591 | `"            \"how do you search\", \"which search engines\", \"what sites do you use\","` | — |
| [SRC-1AE03B9EC3-L000592](../../agents/web_agent.py#L592) | 592 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000593](../../agents/web_agent.py#L593) | 593 | `"        return ("` | — |
| [SRC-1AE03B9EC3-L000594](../../agents/web_agent.py#L594) | 594 | `"            any(phrase in value for phrase in capability_phrases + search_phrases)"` | — |
| [SRC-1AE03B9EC3-L000595](../../agents/web_agent.py#L595) | 595 | `"            or WebAgent._is_current_search_status_question(question)"` | — |
| [SRC-1AE03B9EC3-L000596](../../agents/web_agent.py#L596) | 596 | `"            or ("` | — |
| [SRC-1AE03B9EC3-L000597](../../agents/web_agent.py#L597) | 597 | `"                \"omarai\" in value"` | — |
| [SRC-1AE03B9EC3-L000598](../../agents/web_agent.py#L598) | 598 | `"                and any(token in value for token in (\"بحث\", \"موقع\", \"تستطيع\", \"تقدر\", \"تعمل\"))"` | — |
| [SRC-1AE03B9EC3-L000599](../../agents/web_agent.py#L599) | 599 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000600](../../agents/web_agent.py#L600) | 600 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000601](../../agents/web_agent.py#L601) | 601 | `""` | — |
| [SRC-1AE03B9EC3-L000602](../../agents/web_agent.py#L602) | 602 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000603](../../agents/web_agent.py#L603) | 603 | `"    def _is_navigation_request(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000604](../../agents/web_agent.py#L604) | 604 | `"        \"\"\"A link-finding task can be useful with one clearly labelled candidate result.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000605](../../agents/web_agent.py#L605) | 605 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000606](../../agents/web_agent.py#L606) | 606 | `"        terms = ("` | — |
| [SRC-1AE03B9EC3-L000607](../../agents/web_agent.py#L607) | 607 | `"            \"موقع\", \"رابط\", \"لينك\", \"الموقع الرسمي\", \"الصفحة الرسمية\","` | — |
| [SRC-1AE03B9EC3-L000608](../../agents/web_agent.py#L608) | 608 | `"            \"official website\", \"website\", \"homepage\", \"link to\","` | — |
| [SRC-1AE03B9EC3-L000609](../../agents/web_agent.py#L609) | 609 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000610](../../agents/web_agent.py#L610) | 610 | `"        return any(term in value for term in terms)"` | — |
| [SRC-1AE03B9EC3-L000611](../../agents/web_agent.py#L611) | 611 | `""` | — |
| [SRC-1AE03B9EC3-L000612](../../agents/web_agent.py#L612) | 612 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000613](../../agents/web_agent.py#L613) | 613 | `"    def _is_lead_search(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000614](../../agents/web_agent.py#L614) | 614 | `"        \"\"\"Keep lead discovery distinct from listing searches and generic explanations.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000615](../../agents/web_agent.py#L615) | 615 | `"        return route_intent(question).get(\"route\") == \"LEAD_GENERATION\""` | — |
| [SRC-1AE03B9EC3-L000616](../../agents/web_agent.py#L616) | 616 | `""` | — |
| [SRC-1AE03B9EC3-L000617](../../agents/web_agent.py#L617) | 617 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000618](../../agents/web_agent.py#L618) | 618 | `"    def _lead_intent_evidence(source: dict[str, Any]) -> dict[str, str] \| None:"` | — |
| [SRC-1AE03B9EC3-L000619](../../agents/web_agent.py#L619) | 619 | `"        \"\"\"Return a narrow, inspectable public buyer-intent phrase signal, if present.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000620](../../agents/web_agent.py#L620) | 620 | `"        phrases = ("` | — |
| [SRC-1AE03B9EC3-L000621](../../agents/web_agent.py#L621) | 621 | `"            \"مطلوب شقه تمليك\", \"مطلوب شقه للشراء\", \"مطلوب شراء شقه\","` | — |
| [SRC-1AE03B9EC3-L000622](../../agents/web_agent.py#L622) | 622 | `"            \"مطلوب عقار للشراء\", \"مطلوب فيلا للشراء\","` | — |
| [SRC-1AE03B9EC3-L000623](../../agents/web_agent.py#L623) | 623 | `"            \"بدور على شقه تمليك\", \"بدور على شقه للشراء\","` | — |
| [SRC-1AE03B9EC3-L000624](../../agents/web_agent.py#L624) | 624 | `"            \"ابحث عن شقه للشراء\", \"عايز اشتري شقه\", \"عاوز اشتري شقه\","` | — |
| [SRC-1AE03B9EC3-L000625](../../agents/web_agent.py#L625) | 625 | `"            \"عايز اشتري عقار\", \"عاوز اشتري عقار\", \"اريد شراء شقه\","` | — |
| [SRC-1AE03B9EC3-L000626](../../agents/web_agent.py#L626) | 626 | `"            \"ارغب في شراء شقه\", \"اريد شراء عقار\", \"ارغب في شراء عقار\","` | — |
| [SRC-1AE03B9EC3-L000627](../../agents/web_agent.py#L627) | 627 | `"            \"looking to buy\", \"looking to purchase\", \"want to buy\","` | — |
| [SRC-1AE03B9EC3-L000628](../../agents/web_agent.py#L628) | 628 | `"            \"wants to buy\", \"want to purchase\", \"wants to purchase\","` | — |
| [SRC-1AE03B9EC3-L000629](../../agents/web_agent.py#L629) | 629 | `"            \"seeking to buy\", \"seeking to purchase\", \"interested in buying\","` | — |
| [SRC-1AE03B9EC3-L000630](../../agents/web_agent.py#L630) | 630 | `"            \"interested in purchasing\", \"buyer looking to buy\","` | — |
| [SRC-1AE03B9EC3-L000631](../../agents/web_agent.py#L631) | 631 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000632](../../agents/web_agent.py#L632) | 632 | `"        for field, basis in ((\"page_text\", \"page_text\"), (\"title\", \"title\"), (\"snippet\", \"search_snippet\")):"` | — |
| [SRC-1AE03B9EC3-L000633](../../agents/web_agent.py#L633) | 633 | `"            raw = source.get(field)"` | — |
| [SRC-1AE03B9EC3-L000634](../../agents/web_agent.py#L634) | 634 | `"            if not isinstance(raw, str) or not raw.strip():"` | — |
| [SRC-1AE03B9EC3-L000635](../../agents/web_agent.py#L635) | 635 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L000636](../../agents/web_agent.py#L636) | 636 | `"            normalized = _normalize_search_query(raw).casefold()"` | — |
| [SRC-1AE03B9EC3-L000637](../../agents/web_agent.py#L637) | 637 | `"            negations = ("` | — |
| [SRC-1AE03B9EC3-L000638](../../agents/web_agent.py#L638) | 638 | `"                \"not looking to buy\", \"not interested in buying\","` | — |
| [SRC-1AE03B9EC3-L000639](../../agents/web_agent.py#L639) | 639 | `"                \"not interested in purchasing\", \"no longer looking to buy\","` | — |
| [SRC-1AE03B9EC3-L000640](../../agents/web_agent.py#L640) | 640 | `"                \"مش بدور على\", \"مش عايز اشتري\", \"مش عاوز اشتري\","` | — |
| [SRC-1AE03B9EC3-L000641](../../agents/web_agent.py#L641) | 641 | `"                \"لا اريد شراء\", \"لا ارغب في شراء\", \"مش محتاج اشتري\","` | — |
| [SRC-1AE03B9EC3-L000642](../../agents/web_agent.py#L642) | 642 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000643](../../agents/web_agent.py#L643) | 643 | `"            if any(_normalize_search_query(term).casefold() in normalized for term in negations):"` | — |
| [SRC-1AE03B9EC3-L000644](../../agents/web_agent.py#L644) | 644 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L000645](../../agents/web_agent.py#L645) | 645 | `"            for phrase in phrases:"` | — |
| [SRC-1AE03B9EC3-L000646](../../agents/web_agent.py#L646) | 646 | `"                needle = _normalize_search_query(phrase).casefold()"` | — |
| [SRC-1AE03B9EC3-L000647](../../agents/web_agent.py#L647) | 647 | `"                if needle and needle in normalized:"` | — |
| [SRC-1AE03B9EC3-L000648](../../agents/web_agent.py#L648) | 648 | `"                    return {\"phrase\": phrase, \"basis\": basis}"` | — |
| [SRC-1AE03B9EC3-L000649](../../agents/web_agent.py#L649) | 649 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000650](../../agents/web_agent.py#L650) | 650 | `""` | — |
| [SRC-1AE03B9EC3-L000651](../../agents/web_agent.py#L651) | 651 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000652](../../agents/web_agent.py#L652) | 652 | `"    def _lead_generation_queries("` | — |
| [SRC-1AE03B9EC3-L000653](../../agents/web_agent.py#L653) | 653 | `"        question: str, existing_queries: list[str] \| None = None"` | — |
| [SRC-1AE03B9EC3-L000654](../../agents/web_agent.py#L654) | 654 | `"    ) -> list[str]:"` | — |
| [SRC-1AE03B9EC3-L000655](../../agents/web_agent.py#L655) | 655 | `"        \"\"\"Create high-intent buyer-search variants without changing the product/location.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000656](../../agents/web_agent.py#L656) | 656 | `"        subject = _normalize_search_query(question).strip()"` | — |
| [SRC-1AE03B9EC3-L000657](../../agents/web_agent.py#L657) | 657 | `"        subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L000658](../../agents/web_agent.py#L658) | 658 | `"            r\"^(?:(?:من فضلك\|لو سمحت)\\s*)?(?:ابحث\|بحث\|دور\|دورلي\|اعثر)\\s+\""` | — |
| [SRC-1AE03B9EC3-L000659](../../agents/web_agent.py#L659) | 659 | `"            r\"(?:عن\|على)\\s+(?:عميل(?:\\s+محتمل)?\|عملاء(?:\\s+محتملين)?\|\""` | — |
| [SRC-1AE03B9EC3-L000660](../../agents/web_agent.py#L660) | 660 | `"            r\"مشتري(?:ن)?\|مشترين)\\s*(?:(?:الذي\|اللي\|الذين)\\s*)?\""` | — |
| [SRC-1AE03B9EC3-L000661](../../agents/web_agent.py#L661) | 661 | `"            r\"(?:(?:يريد\|عايز\|عاوز)\\s*(?:ان\\s*)?(?:يشتري\|شراء))?\\s*\","` | — |
| [SRC-1AE03B9EC3-L000662](../../agents/web_agent.py#L662) | 662 | `"            \"\", subject, flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L000663](../../agents/web_agent.py#L663) | 663 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000664](../../agents/web_agent.py#L664) | 664 | `"        subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L000665](../../agents/web_agent.py#L665) | 665 | `"            r\"^(?:please\\s+)?(?:find\|search for\|look for)\\s+(?:(?:a\|an)\\s+)?\""` | — |
| [SRC-1AE03B9EC3-L000666](../../agents/web_agent.py#L666) | 666 | `"            r\"(?:(?:potential\\s+)?(?:customer\|buyer\|prospect\|lead)s?)\\s*\""` | — |
| [SRC-1AE03B9EC3-L000667](../../agents/web_agent.py#L667) | 667 | `"            r\"(?:(?:who\|that)\\s*)?(?:(?:wants?\|looking to\|seeking to)\\s+\""` | — |
| [SRC-1AE03B9EC3-L000668](../../agents/web_agent.py#L668) | 668 | `"            r\"(?:buy\|purchase)\\s*)?\","` | — |
| [SRC-1AE03B9EC3-L000669](../../agents/web_agent.py#L669) | 669 | `"            \"\", subject, flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L000670](../../agents/web_agent.py#L670) | 670 | `"        ).strip(\" \\t:;,.-\")"` | — |
| [SRC-1AE03B9EC3-L000671](../../agents/web_agent.py#L671) | 671 | `"        if len(_search_tokens(subject)) < 2:"` | — |
| [SRC-1AE03B9EC3-L000672](../../agents/web_agent.py#L672) | 672 | `"            subject = _normalize_search_query(question).strip()"` | — |
| [SRC-1AE03B9EC3-L000673](../../agents/web_agent.py#L673) | 673 | `"        arabic = bool(re.search(r\"[\\u0600-\\u06FF]\", question))"` | — |
| [SRC-1AE03B9EC3-L000674](../../agents/web_agent.py#L674) | 674 | `"        if arabic:"` | — |
| [SRC-1AE03B9EC3-L000675](../../agents/web_agent.py#L675) | 675 | `"            targeted = ["` | — |
| [SRC-1AE03B9EC3-L000676](../../agents/web_agent.py#L676) | 676 | `"                f'\"مطلوب شراء\" {subject}',"` | — |
| [SRC-1AE03B9EC3-L000677](../../agents/web_agent.py#L677) | 677 | `"                f'\"مطلوب شقه تمليك\" {subject}',"` | — |
| [SRC-1AE03B9EC3-L000678](../../agents/web_agent.py#L678) | 678 | `"                f'\"بدور على\" {subject} تمليك',"` | — |
| [SRC-1AE03B9EC3-L000679](../../agents/web_agent.py#L679) | 679 | `"                f'\"عايز اشتري\" {subject}',"` | — |
| [SRC-1AE03B9EC3-L000680](../../agents/web_agent.py#L680) | 680 | `"                f'site:facebook.com/groups \"{subject}\" (\"مطلوب\" OR \"تمليك\")',"` | — |
| [SRC-1AE03B9EC3-L000681](../../agents/web_agent.py#L681) | 681 | `"                f'site:linkedin.com/posts \"{subject}\" (\"looking to buy\" OR \"purchase\")',"` | — |
| [SRC-1AE03B9EC3-L000682](../../agents/web_agent.py#L682) | 682 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L000683](../../agents/web_agent.py#L683) | 683 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L000684](../../agents/web_agent.py#L684) | 684 | `"            targeted = ["` | — |
| [SRC-1AE03B9EC3-L000685](../../agents/web_agent.py#L685) | 685 | `"                f'\"looking to buy\" {subject}',"` | — |
| [SRC-1AE03B9EC3-L000686](../../agents/web_agent.py#L686) | 686 | `"                f'\"want to purchase\" {subject}',"` | — |
| [SRC-1AE03B9EC3-L000687](../../agents/web_agent.py#L687) | 687 | `"                f'site:linkedin.com/posts \"{subject}\" (\"looking to buy\" OR \"purchase\")',"` | — |
| [SRC-1AE03B9EC3-L000688](../../agents/web_agent.py#L688) | 688 | `"                f'site:facebook.com/groups \"{subject}\" (\"looking for\" OR \"want to buy\")',"` | — |
| [SRC-1AE03B9EC3-L000689](../../agents/web_agent.py#L689) | 689 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L000690](../../agents/web_agent.py#L690) | 690 | `"        candidates = targeted + [_normalize_search_query(q) for q in (existing_queries or [])]"` | — |
| [SRC-1AE03B9EC3-L000691](../../agents/web_agent.py#L691) | 691 | `"        return list(dict.fromkeys(q[:500] for q in candidates if q and q.strip()))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L000692](../../agents/web_agent.py#L692) | 692 | `""` | — |
| [SRC-1AE03B9EC3-L000693](../../agents/web_agent.py#L693) | 693 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000694](../../agents/web_agent.py#L694) | 694 | `"    def _is_listing_discovery(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000695](../../agents/web_agent.py#L695) | 695 | `"        \"\"\"Recognize property/job/product discovery where candidates are useful with caveats.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000696](../../agents/web_agent.py#L696) | 696 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L000697](../../agents/web_agent.py#L697) | 697 | `"        entities = ("` | — |
| [SRC-1AE03B9EC3-L000698](../../agents/web_agent.py#L698) | 698 | `"            \"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"فيلا\", \"فلل\", \"وحده سكنيه\","` | — |
| [SRC-1AE03B9EC3-L000699](../../agents/web_agent.py#L699) | 699 | `"            \"وحدات سكنيه\", \"apartment\", \"apartments\", \"flat\", \"property listing\","` | — |
| [SRC-1AE03B9EC3-L000700](../../agents/web_agent.py#L700) | 700 | `"            \"real estate\", \"house\", \"villa\", \"job opening\", \"وظيفه\", \"وظائف\","` | — |
| [SRC-1AE03B9EC3-L000701](../../agents/web_agent.py#L701) | 701 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000702](../../agents/web_agent.py#L702) | 702 | `"        actions = ("` | — |
| [SRC-1AE03B9EC3-L000703](../../agents/web_agent.py#L703) | 703 | `"            \"ابحث\", \"دور\", \"هات\", \"عايز\", \"عاوز\", \"محتاج\", \"بدور\", \"للبيع\","` | — |
| [SRC-1AE03B9EC3-L000704](../../agents/web_agent.py#L704) | 704 | `"            \"للايجار\", \"ايجار\", \"معاينه\", \"اعلان\", \"اعلانات\", \"find\", \"search\","` | — |
| [SRC-1AE03B9EC3-L000705](../../agents/web_agent.py#L705) | 705 | `"            \"looking for\", \"for sale\", \"for rent\","` | — |
| [SRC-1AE03B9EC3-L000706](../../agents/web_agent.py#L706) | 706 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000707](../../agents/web_agent.py#L707) | 707 | `"        normalized_entities = (_normalize_search_query(term).casefold() for term in entities)"` | — |
| [SRC-1AE03B9EC3-L000708](../../agents/web_agent.py#L708) | 708 | `"        normalized_actions = (_normalize_search_query(term).casefold() for term in actions)"` | — |
| [SRC-1AE03B9EC3-L000709](../../agents/web_agent.py#L709) | 709 | `"        return any(term in value for term in normalized_entities) and any("` | — |
| [SRC-1AE03B9EC3-L000710](../../agents/web_agent.py#L710) | 710 | `"            term in value for term in normalized_actions"` | — |
| [SRC-1AE03B9EC3-L000711](../../agents/web_agent.py#L711) | 711 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000712](../../agents/web_agent.py#L712) | 712 | `""` | — |
| [SRC-1AE03B9EC3-L000713](../../agents/web_agent.py#L713) | 713 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000714](../../agents/web_agent.py#L714) | 714 | `"    def _requires_web_research(question: str, mode: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000715](../../agents/web_agent.py#L715) | 715 | `"        \"\"\"Use the web only when the user requests it or the answer depends on live data.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000716](../../agents/web_agent.py#L716) | 716 | `"        # A question about whether the current answer already searched is a"` | — |
| [SRC-1AE03B9EC3-L000717](../../agents/web_agent.py#L717) | 717 | `"        # status query, not a request to launch fresh research in any UI mode."` | — |
| [SRC-1AE03B9EC3-L000718](../../agents/web_agent.py#L718) | 718 | `"        if WebAgent._is_current_search_status_question(question):"` | — |
| [SRC-1AE03B9EC3-L000719](../../agents/web_agent.py#L719) | 719 | `"            return False"` | — |
| [SRC-1AE03B9EC3-L000720](../../agents/web_agent.py#L720) | 720 | `"        if mode != \"auto\":"` | — |
| [SRC-1AE03B9EC3-L000721](../../agents/web_agent.py#L721) | 721 | `"            return True"` | — |
