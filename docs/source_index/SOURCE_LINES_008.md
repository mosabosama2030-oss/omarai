# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **008**
- سجلات الأسطر: **800**
- النطاق: SRC-60066C6786-L000179 إلى SRC-6E58A660BC-L000149
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-60066C6786 — [agents/research_pipeline.py](../../agents/research_pipeline.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-60066C6786-L000179](../../agents/research_pipeline.py#L179) | 179 | `"        query_status = \"blocked_pending_clarification\""` | — |
| [SRC-60066C6786-L000180](../../agents/research_pipeline.py#L180) | 180 | `"    else:"` | — |
| [SRC-60066C6786-L000181](../../agents/research_pipeline.py#L181) | 181 | `"        strategy_matrix = build_query_strategy_matrix("` | — |
| [SRC-60066C6786-L000182](../../agents/research_pipeline.py#L182) | 182 | `"            contextual_question,"` | — |
| [SRC-60066C6786-L000183](../../agents/research_pipeline.py#L183) | 183 | `"            task_spec,"` | — |
| [SRC-60066C6786-L000184](../../agents/research_pipeline.py#L184) | 184 | `"            safe_plan.get(\"queries\", []),"` | — |
| [SRC-60066C6786-L000185](../../agents/research_pipeline.py#L185) | 185 | `"            limit=8,"` | — |
| [SRC-60066C6786-L000186](../../agents/research_pipeline.py#L186) | 186 | `"            compact_fn=compact_fn,"` | — |
| [SRC-60066C6786-L000187](../../agents/research_pipeline.py#L187) | 187 | `"        )"` | — |
| [SRC-60066C6786-L000188](../../agents/research_pipeline.py#L188) | 188 | `"        queries = [item[\"query\"] for item in strategy_matrix]"` | — |
| [SRC-60066C6786-L000189](../../agents/research_pipeline.py#L189) | 189 | `"        query_status = \"completed\""` | — |
| [SRC-60066C6786-L000190](../../agents/research_pipeline.py#L190) | 190 | `""` | — |
| [SRC-60066C6786-L000191](../../agents/research_pipeline.py#L191) | 191 | `"    evidence = evaluate_research_evidence("` | — |
| [SRC-60066C6786-L000192](../../agents/research_pipeline.py#L192) | 192 | `"        aspects, sources, semantic_matcher=semantic_matcher"` | — |
| [SRC-60066C6786-L000193](../../agents/research_pipeline.py#L193) | 193 | `"    )"` | — |
| [SRC-60066C6786-L000194](../../agents/research_pipeline.py#L194) | 194 | `"    return {"` | — |
| [SRC-60066C6786-L000195](../../agents/research_pipeline.py#L195) | 195 | `"        \"contextual_question\": contextual_question,"` | — |
| [SRC-60066C6786-L000196](../../agents/research_pipeline.py#L196) | 196 | `"        \"intent\": intent,"` | — |
| [SRC-60066C6786-L000197](../../agents/research_pipeline.py#L197) | 197 | `"        \"task_spec\": task_spec,"` | — |
| [SRC-60066C6786-L000198](../../agents/research_pipeline.py#L198) | 198 | `"        \"aspects\": aspects,"` | — |
| [SRC-60066C6786-L000199](../../agents/research_pipeline.py#L199) | 199 | `"        \"query_strategy_matrix\": strategy_matrix,"` | — |
| [SRC-60066C6786-L000200](../../agents/research_pipeline.py#L200) | 200 | `"        \"queries\": queries,"` | — |
| [SRC-60066C6786-L000201](../../agents/research_pipeline.py#L201) | 201 | `"        \"evidence\": evidence,"` | — |
| [SRC-60066C6786-L000202](../../agents/research_pipeline.py#L202) | 202 | `"        \"evidence_ledger\": evidence[\"lexical_ledger\"],"` | — |
| [SRC-60066C6786-L000203](../../agents/research_pipeline.py#L203) | 203 | `"        \"stages\": {"` | — |
| [SRC-60066C6786-L000204](../../agents/research_pipeline.py#L204) | 204 | `"            \"context_resolution\": ("` | — |
| [SRC-60066C6786-L000205](../../agents/research_pipeline.py#L205) | 205 | `"                \"completed\""` | — |
| [SRC-60066C6786-L000206](../../agents/research_pipeline.py#L206) | 206 | `"                if history or _has_resolved_dialogue_context(dialogue_context)"` | — |
| [SRC-60066C6786-L000207](../../agents/research_pipeline.py#L207) | 207 | `"                else \"not_needed\""` | — |
| [SRC-60066C6786-L000208](../../agents/research_pipeline.py#L208) | 208 | `"            ),"` | — |
| [SRC-60066C6786-L000209](../../agents/research_pipeline.py#L209) | 209 | `"            \"intent_routing\": \"completed\","` | — |
| [SRC-60066C6786-L000210](../../agents/research_pipeline.py#L210) | 210 | `"            \"task_understanding\": \"completed\","` | — |
| [SRC-60066C6786-L000211](../../agents/research_pipeline.py#L211) | 211 | `"            \"aspect_extraction\": \"completed\","` | — |
| [SRC-60066C6786-L000212](../../agents/research_pipeline.py#L212) | 212 | `"            \"query_planning\": query_status,"` | — |
| [SRC-60066C6786-L000213](../../agents/research_pipeline.py#L213) | 213 | `"            \"lexical_matching\": evidence[\"lexical_matching_status\"],"` | — |
| [SRC-60066C6786-L000214](../../agents/research_pipeline.py#L214) | 214 | `"            \"semantic_matching\": evidence[\"semantic_matching\"][\"status\"],"` | — |
| [SRC-60066C6786-L000215](../../agents/research_pipeline.py#L215) | 215 | `"            \"claim_verification\": evidence[\"claim_verification\"],"` | — |
| [SRC-60066C6786-L000216](../../agents/research_pipeline.py#L216) | 216 | `"        },"` | — |
| [SRC-60066C6786-L000217](../../agents/research_pipeline.py#L217) | 217 | `"    }"` | — |
## الوكيل والمنطق

### FILE-8D00DCEC0D — [agents/sales_domain.py](../../agents/sales_domain.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-8D00DCEC0D-L000001](../../agents/sales_domain.py#L1) | 1 | `"\"\"\"Provider-independent domain contracts for Omarai sales intelligence."` | — |
| [SRC-8D00DCEC0D-L000002](../../agents/sales_domain.py#L2) | 2 | `""` | — |
| [SRC-8D00DCEC0D-L000003](../../agents/sales_domain.py#L3) | 3 | `"These models describe evidence and assessments; they do not discover buyers,"` | — |
| [SRC-8D00DCEC0D-L000004](../../agents/sales_domain.py#L4) | 4 | `"infer identity, calculate purchase probability, or execute external actions."` | — |
| [SRC-8D00DCEC0D-L000005](../../agents/sales_domain.py#L5) | 5 | `"Storage and API integration are deliberately kept separate from this module."` | — |
| [SRC-8D00DCEC0D-L000006](../../agents/sales_domain.py#L6) | 6 | `"\"\"\""` | — |
| [SRC-8D00DCEC0D-L000007](../../agents/sales_domain.py#L7) | 7 | `"from __future__ import annotations"` | — |
| [SRC-8D00DCEC0D-L000008](../../agents/sales_domain.py#L8) | 8 | `""` | — |
| [SRC-8D00DCEC0D-L000009](../../agents/sales_domain.py#L9) | 9 | `"import re"` | — |
| [SRC-8D00DCEC0D-L000010](../../agents/sales_domain.py#L10) | 10 | `"import unicodedata"` | — |
| [SRC-8D00DCEC0D-L000011](../../agents/sales_domain.py#L11) | 11 | `"from dataclasses import dataclass"` | — |
| [SRC-8D00DCEC0D-L000012](../../agents/sales_domain.py#L12) | 12 | `"from collections.abc import Iterable"` | — |
| [SRC-8D00DCEC0D-L000013](../../agents/sales_domain.py#L13) | 13 | `"from datetime import date, datetime"` | — |
| [SRC-8D00DCEC0D-L000014](../../agents/sales_domain.py#L14) | 14 | `"from enum import Enum"` | — |
| [SRC-8D00DCEC0D-L000015](../../agents/sales_domain.py#L15) | 15 | `"from urllib.parse import urlsplit"` | — |
| [SRC-8D00DCEC0D-L000016](../../agents/sales_domain.py#L16) | 16 | `""` | — |
| [SRC-8D00DCEC0D-L000017](../../agents/sales_domain.py#L17) | 17 | `""` | — |
| [SRC-8D00DCEC0D-L000018](../../agents/sales_domain.py#L18) | 18 | `"MAX_NAME_LENGTH = 240"` | — |
| [SRC-8D00DCEC0D-L000019](../../agents/sales_domain.py#L19) | 19 | `"MAX_TEXT_LENGTH = 2_000"` | — |
| [SRC-8D00DCEC0D-L000020](../../agents/sales_domain.py#L20) | 20 | `"MAX_TERM_COUNT = 64"` | — |
| [SRC-8D00DCEC0D-L000021](../../agents/sales_domain.py#L21) | 21 | `"_MAX_CATEGORY_DEPTH = 8"` | — |
| [SRC-8D00DCEC0D-L000022](../../agents/sales_domain.py#L22) | 22 | `""` | — |
| [SRC-8D00DCEC0D-L000023](../../agents/sales_domain.py#L23) | 23 | `"_ARABIC_MARKS = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-8D00DCEC0D-L000024](../../agents/sales_domain.py#L24) | 24 | `"_PUNCTUATION = re.compile(r\"[\\s\\t\\r\\n.,،؛;:!?؟()\\[\\]{}<>\\\"'«»]+\")"` | — |
| [SRC-8D00DCEC0D-L000025](../../agents/sales_domain.py#L25) | 25 | `"_SPACE = re.compile(r\"\\s+\")"` | — |
| [SRC-8D00DCEC0D-L000026](../../agents/sales_domain.py#L26) | 26 | `""` | — |
| [SRC-8D00DCEC0D-L000027](../../agents/sales_domain.py#L27) | 27 | `""` | — |
| [SRC-8D00DCEC0D-L000028](../../agents/sales_domain.py#L28) | 28 | `"class FactOrigin(str, Enum):"` | — |
| [SRC-8D00DCEC0D-L000029](../../agents/sales_domain.py#L29) | 29 | `"    USER_PROVIDED = \"user_provided\""` | — |
| [SRC-8D00DCEC0D-L000030](../../agents/sales_domain.py#L30) | 30 | `"    SOURCE_VERIFIED = \"source_verified\""` | — |
| [SRC-8D00DCEC0D-L000031](../../agents/sales_domain.py#L31) | 31 | `"    INFERRED = \"inferred\""` | — |
| [SRC-8D00DCEC0D-L000032](../../agents/sales_domain.py#L32) | 32 | `"    UNKNOWN = \"unknown\""` | — |
| [SRC-8D00DCEC0D-L000033](../../agents/sales_domain.py#L33) | 33 | `""` | — |
| [SRC-8D00DCEC0D-L000034](../../agents/sales_domain.py#L34) | 34 | `""` | — |
| [SRC-8D00DCEC0D-L000035](../../agents/sales_domain.py#L35) | 35 | `"class DemandSignalType(str, Enum):"` | — |
| [SRC-8D00DCEC0D-L000036](../../agents/sales_domain.py#L36) | 36 | `"    DIRECT_PURCHASE_REQUEST = \"direct_purchase_request\""` | — |
| [SRC-8D00DCEC0D-L000037](../../agents/sales_domain.py#L37) | 37 | `"    REQUEST_FOR_QUOTATION = \"request_for_quotation\""` | — |
| [SRC-8D00DCEC0D-L000038](../../agents/sales_domain.py#L38) | 38 | `"    TENDER_OR_PROCUREMENT = \"tender_or_procurement\""` | — |
| [SRC-8D00DCEC0D-L000039](../../agents/sales_domain.py#L39) | 39 | `"    STATED_NEED = \"stated_need\""` | — |
| [SRC-8D00DCEC0D-L000040](../../agents/sales_domain.py#L40) | 40 | `"    INDIRECT_INDICATOR = \"indirect_indicator\""` | — |
| [SRC-8D00DCEC0D-L000041](../../agents/sales_domain.py#L41) | 41 | `"    ICP_MATCH_ONLY = \"icp_match_only\""` | — |
| [SRC-8D00DCEC0D-L000042](../../agents/sales_domain.py#L42) | 42 | `"    NEGATED = \"negated\""` | — |
| [SRC-8D00DCEC0D-L000043](../../agents/sales_domain.py#L43) | 43 | `"    CANCELLED = \"cancelled\""` | — |
| [SRC-8D00DCEC0D-L000044](../../agents/sales_domain.py#L44) | 44 | `"    EXPIRED = \"expired\""` | — |
| [SRC-8D00DCEC0D-L000045](../../agents/sales_domain.py#L45) | 45 | `"    CONFLICTING = \"conflicting\""` | — |
| [SRC-8D00DCEC0D-L000046](../../agents/sales_domain.py#L46) | 46 | `"    UNKNOWN = \"unknown\""` | — |
| [SRC-8D00DCEC0D-L000047](../../agents/sales_domain.py#L47) | 47 | `""` | — |
| [SRC-8D00DCEC0D-L000048](../../agents/sales_domain.py#L48) | 48 | `""` | — |
| [SRC-8D00DCEC0D-L000049](../../agents/sales_domain.py#L49) | 49 | `"class ProductFit(str, Enum):"` | — |
| [SRC-8D00DCEC0D-L000050](../../agents/sales_domain.py#L50) | 50 | `"    FIT = \"fit\""` | — |
| [SRC-8D00DCEC0D-L000051](../../agents/sales_domain.py#L51) | 51 | `"    NO_FIT = \"no_fit\""` | — |
| [SRC-8D00DCEC0D-L000052](../../agents/sales_domain.py#L52) | 52 | `"    UNASSESSED = \"unassessed\""` | — |
| [SRC-8D00DCEC0D-L000053](../../agents/sales_domain.py#L53) | 53 | `""` | — |
| [SRC-8D00DCEC0D-L000054](../../agents/sales_domain.py#L54) | 54 | `""` | — |
| [SRC-8D00DCEC0D-L000055](../../agents/sales_domain.py#L55) | 55 | `"class EvidenceBasis(str, Enum):"` | — |
| [SRC-8D00DCEC0D-L000056](../../agents/sales_domain.py#L56) | 56 | `"    PAGE_TEXT = \"page_text\""` | — |
| [SRC-8D00DCEC0D-L000057](../../agents/sales_domain.py#L57) | 57 | `"    TITLE = \"title\""` | — |
| [SRC-8D00DCEC0D-L000058](../../agents/sales_domain.py#L58) | 58 | `"    SEARCH_SNIPPET = \"search_snippet\""` | — |
| [SRC-8D00DCEC0D-L000059](../../agents/sales_domain.py#L59) | 59 | `"    OFFICIAL_DOCUMENT = \"official_document\""` | — |
| [SRC-8D00DCEC0D-L000060](../../agents/sales_domain.py#L60) | 60 | `"    USER_PROVIDED = \"user_provided\""` | — |
| [SRC-8D00DCEC0D-L000061](../../agents/sales_domain.py#L61) | 61 | `""` | — |
| [SRC-8D00DCEC0D-L000062](../../agents/sales_domain.py#L62) | 62 | `""` | — |
| [SRC-8D00DCEC0D-L000063](../../agents/sales_domain.py#L63) | 63 | `"class IdentityStatus(str, Enum):"` | — |
| [SRC-8D00DCEC0D-L000064](../../agents/sales_domain.py#L64) | 64 | `"    VERIFIED = \"verified\""` | — |
| [SRC-8D00DCEC0D-L000065](../../agents/sales_domain.py#L65) | 65 | `"    UNVERIFIED = \"unverified\""` | — |
| [SRC-8D00DCEC0D-L000066](../../agents/sales_domain.py#L66) | 66 | `"    UNKNOWN = \"unknown\""` | — |
| [SRC-8D00DCEC0D-L000067](../../agents/sales_domain.py#L67) | 67 | `""` | — |
| [SRC-8D00DCEC0D-L000068](../../agents/sales_domain.py#L68) | 68 | `""` | — |
| [SRC-8D00DCEC0D-L000069](../../agents/sales_domain.py#L69) | 69 | `"class SourceQuality(str, Enum):"` | — |
| [SRC-8D00DCEC0D-L000070](../../agents/sales_domain.py#L70) | 70 | `"    PRIMARY_SOURCE = \"primary_source\""` | — |
| [SRC-8D00DCEC0D-L000071](../../agents/sales_domain.py#L71) | 71 | `"    SECONDARY_SOURCE = \"secondary_source\""` | — |
| [SRC-8D00DCEC0D-L000072](../../agents/sales_domain.py#L72) | 72 | `"    SNIPPET_ONLY = \"snippet_only\""` | — |
| [SRC-8D00DCEC0D-L000073](../../agents/sales_domain.py#L73) | 73 | `"    PAGE_UNREAD = \"page_unread\""` | — |
| [SRC-8D00DCEC0D-L000074](../../agents/sales_domain.py#L74) | 74 | `"    UNKNOWN = \"unknown\""` | — |
| [SRC-8D00DCEC0D-L000075](../../agents/sales_domain.py#L75) | 75 | `""` | — |
| [SRC-8D00DCEC0D-L000076](../../agents/sales_domain.py#L76) | 76 | `""` | — |
| [SRC-8D00DCEC0D-L000077](../../agents/sales_domain.py#L77) | 77 | `"class FreshnessStatus(str, Enum):"` | — |
| [SRC-8D00DCEC0D-L000078](../../agents/sales_domain.py#L78) | 78 | `"    CURRENT = \"current\""` | — |
| [SRC-8D00DCEC0D-L000079](../../agents/sales_domain.py#L79) | 79 | `"    STALE = \"stale\""` | — |
| [SRC-8D00DCEC0D-L000080](../../agents/sales_domain.py#L80) | 80 | `"    UNKNOWN = \"unknown\""` | — |
| [SRC-8D00DCEC0D-L000081](../../agents/sales_domain.py#L81) | 81 | `""` | — |
| [SRC-8D00DCEC0D-L000082](../../agents/sales_domain.py#L82) | 82 | `""` | — |
| [SRC-8D00DCEC0D-L000083](../../agents/sales_domain.py#L83) | 83 | `"class ContactabilityStatus(str, Enum):"` | — |
| [SRC-8D00DCEC0D-L000084](../../agents/sales_domain.py#L84) | 84 | `"    PUBLIC_CHANNEL_AVAILABLE = \"public_channel_available\""` | — |
| [SRC-8D00DCEC0D-L000085](../../agents/sales_domain.py#L85) | 85 | `"    NOT_FOUND = \"not_found\""` | — |
| [SRC-8D00DCEC0D-L000086](../../agents/sales_domain.py#L86) | 86 | `"    NOT_ASSESSED = \"not_assessed\""` | — |
| [SRC-8D00DCEC0D-L000087](../../agents/sales_domain.py#L87) | 87 | `""` | — |
| [SRC-8D00DCEC0D-L000088](../../agents/sales_domain.py#L88) | 88 | `""` | — |
| [SRC-8D00DCEC0D-L000089](../../agents/sales_domain.py#L89) | 89 | `"def normalize_text(value: str) -> str:"` | — |
| [SRC-8D00DCEC0D-L000090](../../agents/sales_domain.py#L90) | 90 | `"    \"\"\"Normalize Arabic/Latin text for deterministic matching, not for display.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000091](../../agents/sales_domain.py#L91) | 91 | `"    if not isinstance(value, str):"` | — |
| [SRC-8D00DCEC0D-L000092](../../agents/sales_domain.py#L92) | 92 | `"        return \"\""` | — |
| [SRC-8D00DCEC0D-L000093](../../agents/sales_domain.py#L93) | 93 | `"    text = unicodedata.normalize(\"NFKC\", value).casefold()"` | — |
| [SRC-8D00DCEC0D-L000094](../../agents/sales_domain.py#L94) | 94 | `"    text = _ARABIC_MARKS.sub(\"\", text)"` | — |
| [SRC-8D00DCEC0D-L000095](../../agents/sales_domain.py#L95) | 95 | `"    text = text.replace(\"ـ\", \"\").translate("` | — |
| [SRC-8D00DCEC0D-L000096](../../agents/sales_domain.py#L96) | 96 | `"        str.maketrans("` | — |
| [SRC-8D00DCEC0D-L000097](../../agents/sales_domain.py#L97) | 97 | `"            {"` | — |
| [SRC-8D00DCEC0D-L000098](../../agents/sales_domain.py#L98) | 98 | `"                \"أ\": \"ا\","` | — |
| [SRC-8D00DCEC0D-L000099](../../agents/sales_domain.py#L99) | 99 | `"                \"إ\": \"ا\","` | — |
| [SRC-8D00DCEC0D-L000100](../../agents/sales_domain.py#L100) | 100 | `"                \"آ\": \"ا\","` | — |
| [SRC-8D00DCEC0D-L000101](../../agents/sales_domain.py#L101) | 101 | `"                \"ٱ\": \"ا\","` | — |
| [SRC-8D00DCEC0D-L000102](../../agents/sales_domain.py#L102) | 102 | `"                \"ى\": \"ي\","` | — |
| [SRC-8D00DCEC0D-L000103](../../agents/sales_domain.py#L103) | 103 | `"                \"ة\": \"ه\","` | — |
| [SRC-8D00DCEC0D-L000104](../../agents/sales_domain.py#L104) | 104 | `"            }"` | — |
| [SRC-8D00DCEC0D-L000105](../../agents/sales_domain.py#L105) | 105 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000106](../../agents/sales_domain.py#L106) | 106 | `"    )"` | — |
| [SRC-8D00DCEC0D-L000107](../../agents/sales_domain.py#L107) | 107 | `"    text = _PUNCTUATION.sub(\" \", text)"` | — |
| [SRC-8D00DCEC0D-L000108](../../agents/sales_domain.py#L108) | 108 | `"    return _SPACE.sub(\" \", text).strip()"` | — |
| [SRC-8D00DCEC0D-L000109](../../agents/sales_domain.py#L109) | 109 | `""` | — |
| [SRC-8D00DCEC0D-L000110](../../agents/sales_domain.py#L110) | 110 | `""` | — |
| [SRC-8D00DCEC0D-L000111](../../agents/sales_domain.py#L111) | 111 | `"def _clean_text(value: str, *, field_name: str, maximum: int = MAX_TEXT_LENGTH) -> str:"` | — |
| [SRC-8D00DCEC0D-L000112](../../agents/sales_domain.py#L112) | 112 | `"    if not isinstance(value, str):"` | — |
| [SRC-8D00DCEC0D-L000113](../../agents/sales_domain.py#L113) | 113 | `"        raise TypeError(f\"{field_name} must be a string\")"` | — |
| [SRC-8D00DCEC0D-L000114](../../agents/sales_domain.py#L114) | 114 | `"    cleaned = value.strip()"` | — |
| [SRC-8D00DCEC0D-L000115](../../agents/sales_domain.py#L115) | 115 | `"    if not cleaned:"` | — |
| [SRC-8D00DCEC0D-L000116](../../agents/sales_domain.py#L116) | 116 | `"        raise ValueError(f\"{field_name} is required\")"` | — |
| [SRC-8D00DCEC0D-L000117](../../agents/sales_domain.py#L117) | 117 | `"    if len(cleaned) > maximum:"` | — |
| [SRC-8D00DCEC0D-L000118](../../agents/sales_domain.py#L118) | 118 | `"        raise ValueError(f\"{field_name} exceeds {maximum} characters\")"` | — |
| [SRC-8D00DCEC0D-L000119](../../agents/sales_domain.py#L119) | 119 | `"    return cleaned"` | — |
| [SRC-8D00DCEC0D-L000120](../../agents/sales_domain.py#L120) | 120 | `""` | — |
| [SRC-8D00DCEC0D-L000121](../../agents/sales_domain.py#L121) | 121 | `""` | — |
| [SRC-8D00DCEC0D-L000122](../../agents/sales_domain.py#L122) | 122 | `"def _clean_terms("` | — |
| [SRC-8D00DCEC0D-L000123](../../agents/sales_domain.py#L123) | 123 | `"    values: Iterable[str],"` | — |
| [SRC-8D00DCEC0D-L000124](../../agents/sales_domain.py#L124) | 124 | `"    *,"` | — |
| [SRC-8D00DCEC0D-L000125](../../agents/sales_domain.py#L125) | 125 | `"    field_name: str,"` | — |
| [SRC-8D00DCEC0D-L000126](../../agents/sales_domain.py#L126) | 126 | `"    maximum_count: int = MAX_TERM_COUNT,"` | — |
| [SRC-8D00DCEC0D-L000127](../../agents/sales_domain.py#L127) | 127 | `") -> tuple[str, ...]:"` | — |
| [SRC-8D00DCEC0D-L000128](../../agents/sales_domain.py#L128) | 128 | `"    if isinstance(values, (str, bytes)):"` | — |
| [SRC-8D00DCEC0D-L000129](../../agents/sales_domain.py#L129) | 129 | `"        raise TypeError(f\"{field_name} must be an iterable of strings, not a string\")"` | — |
| [SRC-8D00DCEC0D-L000130](../../agents/sales_domain.py#L130) | 130 | `"    cleaned: list[str] = []"` | — |
| [SRC-8D00DCEC0D-L000131](../../agents/sales_domain.py#L131) | 131 | `"    seen: set[str] = set()"` | — |
| [SRC-8D00DCEC0D-L000132](../../agents/sales_domain.py#L132) | 132 | `"    for value in values:"` | — |
| [SRC-8D00DCEC0D-L000133](../../agents/sales_domain.py#L133) | 133 | `"        term = _clean_text(value, field_name=field_name, maximum=MAX_NAME_LENGTH)"` | — |
| [SRC-8D00DCEC0D-L000134](../../agents/sales_domain.py#L134) | 134 | `"        key = normalize_text(term)"` | — |
| [SRC-8D00DCEC0D-L000135](../../agents/sales_domain.py#L135) | 135 | `"        if key and key not in seen:"` | — |
| [SRC-8D00DCEC0D-L000136](../../agents/sales_domain.py#L136) | 136 | `"            cleaned.append(term)"` | — |
| [SRC-8D00DCEC0D-L000137](../../agents/sales_domain.py#L137) | 137 | `"            seen.add(key)"` | — |
| [SRC-8D00DCEC0D-L000138](../../agents/sales_domain.py#L138) | 138 | `"        if len(cleaned) > maximum_count:"` | — |
| [SRC-8D00DCEC0D-L000139](../../agents/sales_domain.py#L139) | 139 | `"            raise ValueError(f\"{field_name} exceeds {maximum_count} items\")"` | — |
| [SRC-8D00DCEC0D-L000140](../../agents/sales_domain.py#L140) | 140 | `"    return tuple(cleaned)"` | — |
| [SRC-8D00DCEC0D-L000141](../../agents/sales_domain.py#L141) | 141 | `""` | — |
| [SRC-8D00DCEC0D-L000142](../../agents/sales_domain.py#L142) | 142 | `""` | — |
| [SRC-8D00DCEC0D-L000143](../../agents/sales_domain.py#L143) | 143 | `"def _clean_path(values: Iterable[str], *, field_name: str) -> tuple[str, ...]:"` | — |
| [SRC-8D00DCEC0D-L000144](../../agents/sales_domain.py#L144) | 144 | `"    path = _clean_terms(values, field_name=field_name, maximum_count=_MAX_CATEGORY_DEPTH)"` | — |
| [SRC-8D00DCEC0D-L000145](../../agents/sales_domain.py#L145) | 145 | `"    if not path:"` | — |
| [SRC-8D00DCEC0D-L000146](../../agents/sales_domain.py#L146) | 146 | `"        raise ValueError(f\"{field_name} must contain at least one segment\")"` | — |
| [SRC-8D00DCEC0D-L000147](../../agents/sales_domain.py#L147) | 147 | `"    return path"` | — |
| [SRC-8D00DCEC0D-L000148](../../agents/sales_domain.py#L148) | 148 | `""` | — |
| [SRC-8D00DCEC0D-L000149](../../agents/sales_domain.py#L149) | 149 | `""` | — |
| [SRC-8D00DCEC0D-L000150](../../agents/sales_domain.py#L150) | 150 | `"def _enum_value(enum_type: type[Enum], value: Enum \| str, *, field_name: str) -> Enum:"` | — |
| [SRC-8D00DCEC0D-L000151](../../agents/sales_domain.py#L151) | 151 | `"    try:"` | — |
| [SRC-8D00DCEC0D-L000152](../../agents/sales_domain.py#L152) | 152 | `"        return value if isinstance(value, enum_type) else enum_type(value)"` | — |
| [SRC-8D00DCEC0D-L000153](../../agents/sales_domain.py#L153) | 153 | `"    except (TypeError, ValueError) as exc:"` | — |
| [SRC-8D00DCEC0D-L000154](../../agents/sales_domain.py#L154) | 154 | `"        allowed = \", \".join(item.value for item in enum_type)"` | — |
| [SRC-8D00DCEC0D-L000155](../../agents/sales_domain.py#L155) | 155 | `"        raise ValueError(f\"{field_name} must be one of: {allowed}\") from exc"` | — |
| [SRC-8D00DCEC0D-L000156](../../agents/sales_domain.py#L156) | 156 | `""` | — |
| [SRC-8D00DCEC0D-L000157](../../agents/sales_domain.py#L157) | 157 | `""` | — |
| [SRC-8D00DCEC0D-L000158](../../agents/sales_domain.py#L158) | 158 | `"def _validate_optional_date(value: str \| None, *, field_name: str) -> str \| None:"` | — |
| [SRC-8D00DCEC0D-L000159](../../agents/sales_domain.py#L159) | 159 | `"    if value is None:"` | — |
| [SRC-8D00DCEC0D-L000160](../../agents/sales_domain.py#L160) | 160 | `"        return None"` | — |
| [SRC-8D00DCEC0D-L000161](../../agents/sales_domain.py#L161) | 161 | `"    cleaned = _clean_text(value, field_name=field_name, maximum=32)"` | — |
| [SRC-8D00DCEC0D-L000162](../../agents/sales_domain.py#L162) | 162 | `"    try:"` | — |
| [SRC-8D00DCEC0D-L000163](../../agents/sales_domain.py#L163) | 163 | `"        parsed = date.fromisoformat(cleaned)"` | — |
| [SRC-8D00DCEC0D-L000164](../../agents/sales_domain.py#L164) | 164 | `"    except ValueError as exc:"` | — |
| [SRC-8D00DCEC0D-L000165](../../agents/sales_domain.py#L165) | 165 | `"        raise ValueError(f\"{field_name} must be an ISO date (YYYY-MM-DD)\") from exc"` | — |
| [SRC-8D00DCEC0D-L000166](../../agents/sales_domain.py#L166) | 166 | `"    if parsed.isoformat() != cleaned:"` | — |
| [SRC-8D00DCEC0D-L000167](../../agents/sales_domain.py#L167) | 167 | `"        raise ValueError(f\"{field_name} must use YYYY-MM-DD\")"` | — |
| [SRC-8D00DCEC0D-L000168](../../agents/sales_domain.py#L168) | 168 | `"    return cleaned"` | — |
| [SRC-8D00DCEC0D-L000169](../../agents/sales_domain.py#L169) | 169 | `""` | — |
| [SRC-8D00DCEC0D-L000170](../../agents/sales_domain.py#L170) | 170 | `""` | — |
| [SRC-8D00DCEC0D-L000171](../../agents/sales_domain.py#L171) | 171 | `"def _validate_optional_datetime(value: str \| None, *, field_name: str) -> str \| None:"` | — |
| [SRC-8D00DCEC0D-L000172](../../agents/sales_domain.py#L172) | 172 | `"    if value is None:"` | — |
| [SRC-8D00DCEC0D-L000173](../../agents/sales_domain.py#L173) | 173 | `"        return None"` | — |
| [SRC-8D00DCEC0D-L000174](../../agents/sales_domain.py#L174) | 174 | `"    cleaned = _clean_text(value, field_name=field_name, maximum=64)"` | — |
| [SRC-8D00DCEC0D-L000175](../../agents/sales_domain.py#L175) | 175 | `"    try:"` | — |
| [SRC-8D00DCEC0D-L000176](../../agents/sales_domain.py#L176) | 176 | `"        parsed = datetime.fromisoformat(cleaned)"` | — |
| [SRC-8D00DCEC0D-L000177](../../agents/sales_domain.py#L177) | 177 | `"    except ValueError as exc:"` | — |
| [SRC-8D00DCEC0D-L000178](../../agents/sales_domain.py#L178) | 178 | `"        raise ValueError(f\"{field_name} must be an ISO-8601 datetime\") from exc"` | — |
| [SRC-8D00DCEC0D-L000179](../../agents/sales_domain.py#L179) | 179 | `"    if parsed.tzinfo is None:"` | — |
| [SRC-8D00DCEC0D-L000180](../../agents/sales_domain.py#L180) | 180 | `"        raise ValueError(f\"{field_name} must include a timezone offset\")"` | — |
| [SRC-8D00DCEC0D-L000181](../../agents/sales_domain.py#L181) | 181 | `"    return cleaned"` | — |
| [SRC-8D00DCEC0D-L000182](../../agents/sales_domain.py#L182) | 182 | `""` | — |
| [SRC-8D00DCEC0D-L000183](../../agents/sales_domain.py#L183) | 183 | `""` | — |
| [SRC-8D00DCEC0D-L000184](../../agents/sales_domain.py#L184) | 184 | `"def _validate_http_url(value: str) -> str:"` | — |
| [SRC-8D00DCEC0D-L000185](../../agents/sales_domain.py#L185) | 185 | `"    cleaned = _clean_text(value, field_name=\"source_url\", maximum=2_048)"` | — |
| [SRC-8D00DCEC0D-L000186](../../agents/sales_domain.py#L186) | 186 | `"    parsed = urlsplit(cleaned)"` | — |
| [SRC-8D00DCEC0D-L000187](../../agents/sales_domain.py#L187) | 187 | `"    if parsed.scheme not in {\"http\", \"https\"} or not parsed.hostname:"` | — |
| [SRC-8D00DCEC0D-L000188](../../agents/sales_domain.py#L188) | 188 | `"        raise ValueError(\"source_url must be an absolute HTTP(S) URL\")"` | — |
| [SRC-8D00DCEC0D-L000189](../../agents/sales_domain.py#L189) | 189 | `"    if parsed.username or parsed.password:"` | — |
| [SRC-8D00DCEC0D-L000190](../../agents/sales_domain.py#L190) | 190 | `"        raise ValueError(\"source_url must not contain embedded credentials\")"` | — |
| [SRC-8D00DCEC0D-L000191](../../agents/sales_domain.py#L191) | 191 | `"    return cleaned"` | — |
| [SRC-8D00DCEC0D-L000192](../../agents/sales_domain.py#L192) | 192 | `""` | — |
| [SRC-8D00DCEC0D-L000193](../../agents/sales_domain.py#L193) | 193 | `""` | — |
| [SRC-8D00DCEC0D-L000194](../../agents/sales_domain.py#L194) | 194 | `"def _contains_phrase(text: str, phrase: str) -> bool:"` | — |
| [SRC-8D00DCEC0D-L000195](../../agents/sales_domain.py#L195) | 195 | `"    normalized_text = normalize_text(text)"` | — |
| [SRC-8D00DCEC0D-L000196](../../agents/sales_domain.py#L196) | 196 | `"    normalized_phrase = normalize_text(phrase)"` | — |
| [SRC-8D00DCEC0D-L000197](../../agents/sales_domain.py#L197) | 197 | `"    if not normalized_text or not normalized_phrase:"` | — |
| [SRC-8D00DCEC0D-L000198](../../agents/sales_domain.py#L198) | 198 | `"        return False"` | — |
| [SRC-8D00DCEC0D-L000199](../../agents/sales_domain.py#L199) | 199 | `"    # Unicode-aware word boundaries prevent e.g. \"car\" matching \"cart\"."` | — |
| [SRC-8D00DCEC0D-L000200](../../agents/sales_domain.py#L200) | 200 | `"    return re.search("` | — |
| [SRC-8D00DCEC0D-L000201](../../agents/sales_domain.py#L201) | 201 | `"        rf\"(?<!\\w){re.escape(normalized_phrase)}(?!\\w)\","` | — |
| [SRC-8D00DCEC0D-L000202](../../agents/sales_domain.py#L202) | 202 | `"        normalized_text,"` | — |
| [SRC-8D00DCEC0D-L000203](../../agents/sales_domain.py#L203) | 203 | `"        flags=re.UNICODE,"` | — |
| [SRC-8D00DCEC0D-L000204](../../agents/sales_domain.py#L204) | 204 | `"    ) is not None"` | — |
| [SRC-8D00DCEC0D-L000205](../../agents/sales_domain.py#L205) | 205 | `""` | — |
| [SRC-8D00DCEC0D-L000206](../../agents/sales_domain.py#L206) | 206 | `""` | — |
| [SRC-8D00DCEC0D-L000207](../../agents/sales_domain.py#L207) | 207 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-8D00DCEC0D-L000208](../../agents/sales_domain.py#L208) | 208 | `"class ProductFact:"` | — |
| [SRC-8D00DCEC0D-L000209](../../agents/sales_domain.py#L209) | 209 | `"    \"\"\"One product attribute with an explicit origin and optional evidence pointer.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000210](../../agents/sales_domain.py#L210) | 210 | `""` | — |
| [SRC-8D00DCEC0D-L000211](../../agents/sales_domain.py#L211) | 211 | `"    field: str"` | — |
| [SRC-8D00DCEC0D-L000212](../../agents/sales_domain.py#L212) | 212 | `"    value: str"` | — |
| [SRC-8D00DCEC0D-L000213](../../agents/sales_domain.py#L213) | 213 | `"    origin: FactOrigin = FactOrigin.USER_PROVIDED"` | — |
| [SRC-8D00DCEC0D-L000214](../../agents/sales_domain.py#L214) | 214 | `"    evidence_id: str \| None = None"` | — |
| [SRC-8D00DCEC0D-L000215](../../agents/sales_domain.py#L215) | 215 | `""` | — |
| [SRC-8D00DCEC0D-L000216](../../agents/sales_domain.py#L216) | 216 | `"    def __post_init__(self) -> None:"` | — |
| [SRC-8D00DCEC0D-L000217](../../agents/sales_domain.py#L217) | 217 | `"        object.__setattr__(self, \"field\", _clean_text(self.field, field_name=\"field\", maximum=80))"` | — |
| [SRC-8D00DCEC0D-L000218](../../agents/sales_domain.py#L218) | 218 | `"        object.__setattr__(self, \"value\", _clean_text(self.value, field_name=\"value\"))"` | — |
| [SRC-8D00DCEC0D-L000219](../../agents/sales_domain.py#L219) | 219 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000220](../../agents/sales_domain.py#L220) | 220 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000221](../../agents/sales_domain.py#L221) | 221 | `"            \"origin\","` | — |
| [SRC-8D00DCEC0D-L000222](../../agents/sales_domain.py#L222) | 222 | `"            _enum_value(FactOrigin, self.origin, field_name=\"origin\"),"` | — |
| [SRC-8D00DCEC0D-L000223](../../agents/sales_domain.py#L223) | 223 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000224](../../agents/sales_domain.py#L224) | 224 | `"        if self.evidence_id is not None:"` | — |
| [SRC-8D00DCEC0D-L000225](../../agents/sales_domain.py#L225) | 225 | `"            object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000226](../../agents/sales_domain.py#L226) | 226 | `"                self,"` | — |
| [SRC-8D00DCEC0D-L000227](../../agents/sales_domain.py#L227) | 227 | `"                \"evidence_id\","` | — |
| [SRC-8D00DCEC0D-L000228](../../agents/sales_domain.py#L228) | 228 | `"                _clean_text(self.evidence_id, field_name=\"evidence_id\", maximum=160),"` | — |
| [SRC-8D00DCEC0D-L000229](../../agents/sales_domain.py#L229) | 229 | `"            )"` | — |
| [SRC-8D00DCEC0D-L000230](../../agents/sales_domain.py#L230) | 230 | `"        if self.origin == FactOrigin.SOURCE_VERIFIED and not self.evidence_id:"` | — |
| [SRC-8D00DCEC0D-L000231](../../agents/sales_domain.py#L231) | 231 | `"            raise ValueError(\"source_verified product facts require evidence_id\")"` | — |
| [SRC-8D00DCEC0D-L000232](../../agents/sales_domain.py#L232) | 232 | `""` | — |
| [SRC-8D00DCEC0D-L000233](../../agents/sales_domain.py#L233) | 233 | `"    def to_dict(self) -> dict[str, str \| None]:"` | — |
| [SRC-8D00DCEC0D-L000234](../../agents/sales_domain.py#L234) | 234 | `"        return {"` | — |
| [SRC-8D00DCEC0D-L000235](../../agents/sales_domain.py#L235) | 235 | `"            \"field\": self.field,"` | — |
| [SRC-8D00DCEC0D-L000236](../../agents/sales_domain.py#L236) | 236 | `"            \"value\": self.value,"` | — |
| [SRC-8D00DCEC0D-L000237](../../agents/sales_domain.py#L237) | 237 | `"            \"origin\": self.origin.value,"` | — |
| [SRC-8D00DCEC0D-L000238](../../agents/sales_domain.py#L238) | 238 | `"            \"evidence_id\": self.evidence_id,"` | — |
| [SRC-8D00DCEC0D-L000239](../../agents/sales_domain.py#L239) | 239 | `"        }"` | — |
| [SRC-8D00DCEC0D-L000240](../../agents/sales_domain.py#L240) | 240 | `""` | — |
| [SRC-8D00DCEC0D-L000241](../../agents/sales_domain.py#L241) | 241 | `""` | — |
| [SRC-8D00DCEC0D-L000242](../../agents/sales_domain.py#L242) | 242 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-8D00DCEC0D-L000243](../../agents/sales_domain.py#L243) | 243 | `"class ProductProfile:"` | — |
| [SRC-8D00DCEC0D-L000244](../../agents/sales_domain.py#L244) | 244 | `"    \"\"\"Explicit product/service facts supplied by a user or supported by sources.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000245](../../agents/sales_domain.py#L245) | 245 | `""` | — |
| [SRC-8D00DCEC0D-L000246](../../agents/sales_domain.py#L246) | 246 | `"    name: str"` | — |
| [SRC-8D00DCEC0D-L000247](../../agents/sales_domain.py#L247) | 247 | `"    aliases: tuple[str, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000248](../../agents/sales_domain.py#L248) | 248 | `"    category_path: tuple[str, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000249](../../agents/sales_domain.py#L249) | 249 | `"    use_cases: tuple[str, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000250](../../agents/sales_domain.py#L250) | 250 | `"    problems_solved: tuple[str, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000251](../../agents/sales_domain.py#L251) | 251 | `"    facts: tuple[ProductFact, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000252](../../agents/sales_domain.py#L252) | 252 | `""` | — |
| [SRC-8D00DCEC0D-L000253](../../agents/sales_domain.py#L253) | 253 | `"    def __post_init__(self) -> None:"` | — |
| [SRC-8D00DCEC0D-L000254](../../agents/sales_domain.py#L254) | 254 | `"        object.__setattr__(self, \"name\", _clean_text(self.name, field_name=\"name\", maximum=MAX_NAME_LENGTH))"` | — |
| [SRC-8D00DCEC0D-L000255](../../agents/sales_domain.py#L255) | 255 | `"        object.__setattr__(self, \"aliases\", _clean_terms(self.aliases, field_name=\"aliases\"))"` | — |
| [SRC-8D00DCEC0D-L000256](../../agents/sales_domain.py#L256) | 256 | `"        object.__setattr__(self, \"use_cases\", _clean_terms(self.use_cases, field_name=\"use_cases\"))"` | — |
| [SRC-8D00DCEC0D-L000257](../../agents/sales_domain.py#L257) | 257 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000258](../../agents/sales_domain.py#L258) | 258 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000259](../../agents/sales_domain.py#L259) | 259 | `"            \"problems_solved\","` | — |
| [SRC-8D00DCEC0D-L000260](../../agents/sales_domain.py#L260) | 260 | `"            _clean_terms(self.problems_solved, field_name=\"problems_solved\"),"` | — |
| [SRC-8D00DCEC0D-L000261](../../agents/sales_domain.py#L261) | 261 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000262](../../agents/sales_domain.py#L262) | 262 | `"        if self.category_path:"` | — |
| [SRC-8D00DCEC0D-L000263](../../agents/sales_domain.py#L263) | 263 | `"            object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000264](../../agents/sales_domain.py#L264) | 264 | `"                self,"` | — |
| [SRC-8D00DCEC0D-L000265](../../agents/sales_domain.py#L265) | 265 | `"                \"category_path\","` | — |
| [SRC-8D00DCEC0D-L000266](../../agents/sales_domain.py#L266) | 266 | `"                _clean_path(self.category_path, field_name=\"category_path\"),"` | — |
| [SRC-8D00DCEC0D-L000267](../../agents/sales_domain.py#L267) | 267 | `"            )"` | — |
| [SRC-8D00DCEC0D-L000268](../../agents/sales_domain.py#L268) | 268 | `"        if not all(isinstance(item, ProductFact) for item in self.facts):"` | — |
| [SRC-8D00DCEC0D-L000269](../../agents/sales_domain.py#L269) | 269 | `"            raise TypeError(\"facts must contain ProductFact instances\")"` | — |
| [SRC-8D00DCEC0D-L000270](../../agents/sales_domain.py#L270) | 270 | `"        if len(self.facts) > MAX_TERM_COUNT:"` | — |
| [SRC-8D00DCEC0D-L000271](../../agents/sales_domain.py#L271) | 271 | `"            raise ValueError(f\"facts exceeds {MAX_TERM_COUNT} items\")"` | — |
| [SRC-8D00DCEC0D-L000272](../../agents/sales_domain.py#L272) | 272 | `""` | — |
| [SRC-8D00DCEC0D-L000273](../../agents/sales_domain.py#L273) | 273 | `"    def matching_terms(self, text: str) -> tuple[str, ...]:"` | — |
| [SRC-8D00DCEC0D-L000274](../../agents/sales_domain.py#L274) | 274 | `"        \"\"\"Return explicitly configured product terms mentioned in text."` | — |
| [SRC-8D00DCEC0D-L000275](../../agents/sales_domain.py#L275) | 275 | `""` | — |
| [SRC-8D00DCEC0D-L000276](../../agents/sales_domain.py#L276) | 276 | `"        A mention is not a demand signal and does not establish a buyer or product fit."` | — |
| [SRC-8D00DCEC0D-L000277](../../agents/sales_domain.py#L277) | 277 | `"        \"\"\""` | — |
| [SRC-8D00DCEC0D-L000278](../../agents/sales_domain.py#L278) | 278 | `"        terms = (self.name, *self.aliases)"` | — |
| [SRC-8D00DCEC0D-L000279](../../agents/sales_domain.py#L279) | 279 | `"        return tuple(term for term in terms if _contains_phrase(text, term))"` | — |
| [SRC-8D00DCEC0D-L000280](../../agents/sales_domain.py#L280) | 280 | `""` | — |
| [SRC-8D00DCEC0D-L000281](../../agents/sales_domain.py#L281) | 281 | `"    def to_dict(self) -> dict[str, object]:"` | — |
| [SRC-8D00DCEC0D-L000282](../../agents/sales_domain.py#L282) | 282 | `"        return {"` | — |
| [SRC-8D00DCEC0D-L000283](../../agents/sales_domain.py#L283) | 283 | `"            \"name\": self.name,"` | — |
| [SRC-8D00DCEC0D-L000284](../../agents/sales_domain.py#L284) | 284 | `"            \"aliases\": list(self.aliases),"` | — |
| [SRC-8D00DCEC0D-L000285](../../agents/sales_domain.py#L285) | 285 | `"            \"category_path\": list(self.category_path),"` | — |
| [SRC-8D00DCEC0D-L000286](../../agents/sales_domain.py#L286) | 286 | `"            \"use_cases\": list(self.use_cases),"` | — |
| [SRC-8D00DCEC0D-L000287](../../agents/sales_domain.py#L287) | 287 | `"            \"problems_solved\": list(self.problems_solved),"` | — |
| [SRC-8D00DCEC0D-L000288](../../agents/sales_domain.py#L288) | 288 | `"            \"facts\": [item.to_dict() for item in self.facts],"` | — |
| [SRC-8D00DCEC0D-L000289](../../agents/sales_domain.py#L289) | 289 | `"        }"` | — |
| [SRC-8D00DCEC0D-L000290](../../agents/sales_domain.py#L290) | 290 | `""` | — |
| [SRC-8D00DCEC0D-L000291](../../agents/sales_domain.py#L291) | 291 | `""` | — |
| [SRC-8D00DCEC0D-L000292](../../agents/sales_domain.py#L292) | 292 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-8D00DCEC0D-L000293](../../agents/sales_domain.py#L293) | 293 | `"class MarketProfile:"` | — |
| [SRC-8D00DCEC0D-L000294](../../agents/sales_domain.py#L294) | 294 | `"    \"\"\"Target-market constraints; matching an ICP is not evidence of purchase intent.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000295](../../agents/sales_domain.py#L295) | 295 | `""` | — |
| [SRC-8D00DCEC0D-L000296](../../agents/sales_domain.py#L296) | 296 | `"    locations: tuple[str, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000297](../../agents/sales_domain.py#L297) | 297 | `"    industries: tuple[str, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000298](../../agents/sales_domain.py#L298) | 298 | `"    customer_types: tuple[str, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000299](../../agents/sales_domain.py#L299) | 299 | `"    decision_roles: tuple[str, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000300](../../agents/sales_domain.py#L300) | 300 | `"    exclusions: tuple[str, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000301](../../agents/sales_domain.py#L301) | 301 | `""` | — |
| [SRC-8D00DCEC0D-L000302](../../agents/sales_domain.py#L302) | 302 | `"    def __post_init__(self) -> None:"` | — |
| [SRC-8D00DCEC0D-L000303](../../agents/sales_domain.py#L303) | 303 | `"        for name in (\"locations\", \"industries\", \"customer_types\", \"decision_roles\", \"exclusions\"):"` | — |
| [SRC-8D00DCEC0D-L000304](../../agents/sales_domain.py#L304) | 304 | `"            object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000305](../../agents/sales_domain.py#L305) | 305 | `"                self,"` | — |
| [SRC-8D00DCEC0D-L000306](../../agents/sales_domain.py#L306) | 306 | `"                name,"` | — |
| [SRC-8D00DCEC0D-L000307](../../agents/sales_domain.py#L307) | 307 | `"                _clean_terms(getattr(self, name), field_name=name),"` | — |
| [SRC-8D00DCEC0D-L000308](../../agents/sales_domain.py#L308) | 308 | `"            )"` | — |
| [SRC-8D00DCEC0D-L000309](../../agents/sales_domain.py#L309) | 309 | `""` | — |
| [SRC-8D00DCEC0D-L000310](../../agents/sales_domain.py#L310) | 310 | `"    def to_dict(self) -> dict[str, list[str]]:"` | — |
| [SRC-8D00DCEC0D-L000311](../../agents/sales_domain.py#L311) | 311 | `"        return {"` | — |
| [SRC-8D00DCEC0D-L000312](../../agents/sales_domain.py#L312) | 312 | `"            name: list(getattr(self, name))"` | — |
| [SRC-8D00DCEC0D-L000313](../../agents/sales_domain.py#L313) | 313 | `"            for name in (\"locations\", \"industries\", \"customer_types\", \"decision_roles\", \"exclusions\")"` | — |
| [SRC-8D00DCEC0D-L000314](../../agents/sales_domain.py#L314) | 314 | `"        }"` | — |
| [SRC-8D00DCEC0D-L000315](../../agents/sales_domain.py#L315) | 315 | `""` | — |
| [SRC-8D00DCEC0D-L000316](../../agents/sales_domain.py#L316) | 316 | `""` | — |
| [SRC-8D00DCEC0D-L000317](../../agents/sales_domain.py#L317) | 317 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-8D00DCEC0D-L000318](../../agents/sales_domain.py#L318) | 318 | `"class TaxonomyCategory:"` | — |
| [SRC-8D00DCEC0D-L000319](../../agents/sales_domain.py#L319) | 319 | `"    \"\"\"A caller-defined taxonomy node; no sector is hard-coded in the matcher.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000320](../../agents/sales_domain.py#L320) | 320 | `""` | — |
| [SRC-8D00DCEC0D-L000321](../../agents/sales_domain.py#L321) | 321 | `"    path: tuple[str, ...]"` | — |
| [SRC-8D00DCEC0D-L000322](../../agents/sales_domain.py#L322) | 322 | `"    aliases: tuple[str, ...]"` | — |
| [SRC-8D00DCEC0D-L000323](../../agents/sales_domain.py#L323) | 323 | `""` | — |
| [SRC-8D00DCEC0D-L000324](../../agents/sales_domain.py#L324) | 324 | `"    def __post_init__(self) -> None:"` | — |
| [SRC-8D00DCEC0D-L000325](../../agents/sales_domain.py#L325) | 325 | `"        object.__setattr__(self, \"path\", _clean_path(self.path, field_name=\"path\"))"` | — |
| [SRC-8D00DCEC0D-L000326](../../agents/sales_domain.py#L326) | 326 | `"        object.__setattr__(self, \"aliases\", _clean_terms(self.aliases, field_name=\"aliases\"))"` | — |
| [SRC-8D00DCEC0D-L000327](../../agents/sales_domain.py#L327) | 327 | `"        if not self.aliases:"` | — |
| [SRC-8D00DCEC0D-L000328](../../agents/sales_domain.py#L328) | 328 | `"            raise ValueError(\"taxonomy category requires at least one alias\")"` | — |
| [SRC-8D00DCEC0D-L000329](../../agents/sales_domain.py#L329) | 329 | `""` | — |
| [SRC-8D00DCEC0D-L000330](../../agents/sales_domain.py#L330) | 330 | `""` | — |
| [SRC-8D00DCEC0D-L000331](../../agents/sales_domain.py#L331) | 331 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-8D00DCEC0D-L000332](../../agents/sales_domain.py#L332) | 332 | `"class ProductTaxonomy:"` | — |
| [SRC-8D00DCEC0D-L000333](../../agents/sales_domain.py#L333) | 333 | `"    \"\"\"Extensible taxonomy supplied by configuration or a verified product catalogue.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000334](../../agents/sales_domain.py#L334) | 334 | `""` | — |
| [SRC-8D00DCEC0D-L000335](../../agents/sales_domain.py#L335) | 335 | `"    categories: tuple[TaxonomyCategory, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000336](../../agents/sales_domain.py#L336) | 336 | `""` | — |
| [SRC-8D00DCEC0D-L000337](../../agents/sales_domain.py#L337) | 337 | `"    def __post_init__(self) -> None:"` | — |
| [SRC-8D00DCEC0D-L000338](../../agents/sales_domain.py#L338) | 338 | `"        if not all(isinstance(item, TaxonomyCategory) for item in self.categories):"` | — |
| [SRC-8D00DCEC0D-L000339](../../agents/sales_domain.py#L339) | 339 | `"            raise TypeError(\"categories must contain TaxonomyCategory instances\")"` | — |
| [SRC-8D00DCEC0D-L000340](../../agents/sales_domain.py#L340) | 340 | `"        paths = [tuple(normalize_text(part) for part in item.path) for item in self.categories]"` | — |
| [SRC-8D00DCEC0D-L000341](../../agents/sales_domain.py#L341) | 341 | `"        if len(paths) != len(set(paths)):"` | — |
| [SRC-8D00DCEC0D-L000342](../../agents/sales_domain.py#L342) | 342 | `"            raise ValueError(\"taxonomy category paths must be unique\")"` | — |
| [SRC-8D00DCEC0D-L000343](../../agents/sales_domain.py#L343) | 343 | `""` | — |
| [SRC-8D00DCEC0D-L000344](../../agents/sales_domain.py#L344) | 344 | `"    def match_categories(self, text: str) -> tuple[tuple[str, ...], ...]:"` | — |
| [SRC-8D00DCEC0D-L000345](../../agents/sales_domain.py#L345) | 345 | `"        \"\"\"Return all explicit taxonomy matches; never choose a winner by guessing.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000346](../../agents/sales_domain.py#L346) | 346 | `"        matches = ["` | — |
| [SRC-8D00DCEC0D-L000347](../../agents/sales_domain.py#L347) | 347 | `"            category.path"` | — |
| [SRC-8D00DCEC0D-L000348](../../agents/sales_domain.py#L348) | 348 | `"            for category in self.categories"` | — |
| [SRC-8D00DCEC0D-L000349](../../agents/sales_domain.py#L349) | 349 | `"            if any(_contains_phrase(text, alias) for alias in category.aliases)"` | — |
| [SRC-8D00DCEC0D-L000350](../../agents/sales_domain.py#L350) | 350 | `"        ]"` | — |
| [SRC-8D00DCEC0D-L000351](../../agents/sales_domain.py#L351) | 351 | `"        return tuple(matches)"` | — |
| [SRC-8D00DCEC0D-L000352](../../agents/sales_domain.py#L352) | 352 | `""` | — |
| [SRC-8D00DCEC0D-L000353](../../agents/sales_domain.py#L353) | 353 | `"    def to_list(self) -> list[dict[str, list[str]]]:"` | — |
| [SRC-8D00DCEC0D-L000354](../../agents/sales_domain.py#L354) | 354 | `"        return ["` | — |
| [SRC-8D00DCEC0D-L000355](../../agents/sales_domain.py#L355) | 355 | `"            {\"path\": list(item.path), \"aliases\": list(item.aliases)}"` | — |
| [SRC-8D00DCEC0D-L000356](../../agents/sales_domain.py#L356) | 356 | `"            for item in self.categories"` | — |
| [SRC-8D00DCEC0D-L000357](../../agents/sales_domain.py#L357) | 357 | `"        ]"` | — |
| [SRC-8D00DCEC0D-L000358](../../agents/sales_domain.py#L358) | 358 | `""` | — |
| [SRC-8D00DCEC0D-L000359](../../agents/sales_domain.py#L359) | 359 | `""` | — |
| [SRC-8D00DCEC0D-L000360](../../agents/sales_domain.py#L360) | 360 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-8D00DCEC0D-L000361](../../agents/sales_domain.py#L361) | 361 | `"class DemandEvidence:"` | — |
| [SRC-8D00DCEC0D-L000362](../../agents/sales_domain.py#L362) | 362 | `"    \"\"\"Source provenance for a demand signal; dates remain distinct and optional.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000363](../../agents/sales_domain.py#L363) | 363 | `""` | — |
| [SRC-8D00DCEC0D-L000364](../../agents/sales_domain.py#L364) | 364 | `"    source_id: str"` | — |
| [SRC-8D00DCEC0D-L000365](../../agents/sales_domain.py#L365) | 365 | `"    source_url: str"` | — |
| [SRC-8D00DCEC0D-L000366](../../agents/sales_domain.py#L366) | 366 | `"    excerpt: str"` | — |
| [SRC-8D00DCEC0D-L000367](../../agents/sales_domain.py#L367) | 367 | `"    content_basis: EvidenceBasis"` | — |
| [SRC-8D00DCEC0D-L000368](../../agents/sales_domain.py#L368) | 368 | `"    publication_date: str \| None = None"` | — |
| [SRC-8D00DCEC0D-L000369](../../agents/sales_domain.py#L369) | 369 | `"    event_date: str \| None = None"` | — |
| [SRC-8D00DCEC0D-L000370](../../agents/sales_domain.py#L370) | 370 | `"    observed_at: str \| None = None"` | — |
| [SRC-8D00DCEC0D-L000371](../../agents/sales_domain.py#L371) | 371 | `"    page_read: bool = False"` | — |
| [SRC-8D00DCEC0D-L000372](../../agents/sales_domain.py#L372) | 372 | `""` | — |
| [SRC-8D00DCEC0D-L000373](../../agents/sales_domain.py#L373) | 373 | `"    def __post_init__(self) -> None:"` | — |
| [SRC-8D00DCEC0D-L000374](../../agents/sales_domain.py#L374) | 374 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000375](../../agents/sales_domain.py#L375) | 375 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000376](../../agents/sales_domain.py#L376) | 376 | `"            \"source_id\","` | — |
| [SRC-8D00DCEC0D-L000377](../../agents/sales_domain.py#L377) | 377 | `"            _clean_text(self.source_id, field_name=\"source_id\", maximum=160),"` | — |
| [SRC-8D00DCEC0D-L000378](../../agents/sales_domain.py#L378) | 378 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000379](../../agents/sales_domain.py#L379) | 379 | `"        object.__setattr__(self, \"source_url\", _validate_http_url(self.source_url))"` | — |
| [SRC-8D00DCEC0D-L000380](../../agents/sales_domain.py#L380) | 380 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000381](../../agents/sales_domain.py#L381) | 381 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000382](../../agents/sales_domain.py#L382) | 382 | `"            \"excerpt\","` | — |
| [SRC-8D00DCEC0D-L000383](../../agents/sales_domain.py#L383) | 383 | `"            _clean_text(self.excerpt, field_name=\"excerpt\", maximum=MAX_TEXT_LENGTH),"` | — |
| [SRC-8D00DCEC0D-L000384](../../agents/sales_domain.py#L384) | 384 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000385](../../agents/sales_domain.py#L385) | 385 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000386](../../agents/sales_domain.py#L386) | 386 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000387](../../agents/sales_domain.py#L387) | 387 | `"            \"content_basis\","` | — |
| [SRC-8D00DCEC0D-L000388](../../agents/sales_domain.py#L388) | 388 | `"            _enum_value(EvidenceBasis, self.content_basis, field_name=\"content_basis\"),"` | — |
| [SRC-8D00DCEC0D-L000389](../../agents/sales_domain.py#L389) | 389 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000390](../../agents/sales_domain.py#L390) | 390 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000391](../../agents/sales_domain.py#L391) | 391 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000392](../../agents/sales_domain.py#L392) | 392 | `"            \"publication_date\","` | — |
| [SRC-8D00DCEC0D-L000393](../../agents/sales_domain.py#L393) | 393 | `"            _validate_optional_date(self.publication_date, field_name=\"publication_date\"),"` | — |
| [SRC-8D00DCEC0D-L000394](../../agents/sales_domain.py#L394) | 394 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000395](../../agents/sales_domain.py#L395) | 395 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000396](../../agents/sales_domain.py#L396) | 396 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000397](../../agents/sales_domain.py#L397) | 397 | `"            \"event_date\","` | — |
| [SRC-8D00DCEC0D-L000398](../../agents/sales_domain.py#L398) | 398 | `"            _validate_optional_date(self.event_date, field_name=\"event_date\"),"` | — |
| [SRC-8D00DCEC0D-L000399](../../agents/sales_domain.py#L399) | 399 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000400](../../agents/sales_domain.py#L400) | 400 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000401](../../agents/sales_domain.py#L401) | 401 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000402](../../agents/sales_domain.py#L402) | 402 | `"            \"observed_at\","` | — |
| [SRC-8D00DCEC0D-L000403](../../agents/sales_domain.py#L403) | 403 | `"            _validate_optional_datetime(self.observed_at, field_name=\"observed_at\"),"` | — |
| [SRC-8D00DCEC0D-L000404](../../agents/sales_domain.py#L404) | 404 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000405](../../agents/sales_domain.py#L405) | 405 | `"        if not isinstance(self.page_read, bool):"` | — |
| [SRC-8D00DCEC0D-L000406](../../agents/sales_domain.py#L406) | 406 | `"            raise TypeError(\"page_read must be a boolean\")"` | — |
| [SRC-8D00DCEC0D-L000407](../../agents/sales_domain.py#L407) | 407 | `"        if self.content_basis == EvidenceBasis.SEARCH_SNIPPET and self.page_read:"` | — |
| [SRC-8D00DCEC0D-L000408](../../agents/sales_domain.py#L408) | 408 | `"            raise ValueError(\"a search snippet cannot be marked as a successfully read page\")"` | — |
| [SRC-8D00DCEC0D-L000409](../../agents/sales_domain.py#L409) | 409 | `"        if self.content_basis == EvidenceBasis.PAGE_TEXT and not self.page_read:"` | — |
| [SRC-8D00DCEC0D-L000410](../../agents/sales_domain.py#L410) | 410 | `"            raise ValueError(\"page_text evidence requires page_read=True\")"` | — |
| [SRC-8D00DCEC0D-L000411](../../agents/sales_domain.py#L411) | 411 | `""` | — |
| [SRC-8D00DCEC0D-L000412](../../agents/sales_domain.py#L412) | 412 | `"    def to_dict(self) -> dict[str, object]:"` | — |
| [SRC-8D00DCEC0D-L000413](../../agents/sales_domain.py#L413) | 413 | `"        return {"` | — |
| [SRC-8D00DCEC0D-L000414](../../agents/sales_domain.py#L414) | 414 | `"            \"source_id\": self.source_id,"` | — |
| [SRC-8D00DCEC0D-L000415](../../agents/sales_domain.py#L415) | 415 | `"            \"source_url\": self.source_url,"` | — |
| [SRC-8D00DCEC0D-L000416](../../agents/sales_domain.py#L416) | 416 | `"            \"excerpt\": self.excerpt,"` | — |
| [SRC-8D00DCEC0D-L000417](../../agents/sales_domain.py#L417) | 417 | `"            \"content_basis\": self.content_basis.value,"` | — |
| [SRC-8D00DCEC0D-L000418](../../agents/sales_domain.py#L418) | 418 | `"            \"publication_date\": self.publication_date,"` | — |
| [SRC-8D00DCEC0D-L000419](../../agents/sales_domain.py#L419) | 419 | `"            \"event_date\": self.event_date,"` | — |
| [SRC-8D00DCEC0D-L000420](../../agents/sales_domain.py#L420) | 420 | `"            \"observed_at\": self.observed_at,"` | — |
| [SRC-8D00DCEC0D-L000421](../../agents/sales_domain.py#L421) | 421 | `"            \"page_read\": self.page_read,"` | — |
| [SRC-8D00DCEC0D-L000422](../../agents/sales_domain.py#L422) | 422 | `"        }"` | — |
| [SRC-8D00DCEC0D-L000423](../../agents/sales_domain.py#L423) | 423 | `""` | — |
| [SRC-8D00DCEC0D-L000424](../../agents/sales_domain.py#L424) | 424 | `""` | — |
| [SRC-8D00DCEC0D-L000425](../../agents/sales_domain.py#L425) | 425 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-8D00DCEC0D-L000426](../../agents/sales_domain.py#L426) | 426 | `"class DemandSignal:"` | — |
| [SRC-8D00DCEC0D-L000427](../../agents/sales_domain.py#L427) | 427 | `"    \"\"\"A classified demand signal, kept independent from product-fit assessment.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000428](../../agents/sales_domain.py#L428) | 428 | `""` | — |
| [SRC-8D00DCEC0D-L000429](../../agents/sales_domain.py#L429) | 429 | `"    signal_id: str"` | — |
| [SRC-8D00DCEC0D-L000430](../../agents/sales_domain.py#L430) | 430 | `"    signal_type: DemandSignalType"` | — |
| [SRC-8D00DCEC0D-L000431](../../agents/sales_domain.py#L431) | 431 | `"    evidence: DemandEvidence"` | — |
| [SRC-8D00DCEC0D-L000432](../../agents/sales_domain.py#L432) | 432 | `"    product_fit: ProductFit = ProductFit.UNASSESSED"` | — |
| [SRC-8D00DCEC0D-L000433](../../agents/sales_domain.py#L433) | 433 | `"    identity_status: IdentityStatus = IdentityStatus.UNKNOWN"` | — |
| [SRC-8D00DCEC0D-L000434](../../agents/sales_domain.py#L434) | 434 | `"    classification_reason: str = \"\""` | — |
| [SRC-8D00DCEC0D-L000435](../../agents/sales_domain.py#L435) | 435 | `"    product_fit_reason: str = \"\""` | — |
| [SRC-8D00DCEC0D-L000436](../../agents/sales_domain.py#L436) | 436 | `""` | — |
| [SRC-8D00DCEC0D-L000437](../../agents/sales_domain.py#L437) | 437 | `"    def __post_init__(self) -> None:"` | — |
| [SRC-8D00DCEC0D-L000438](../../agents/sales_domain.py#L438) | 438 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000439](../../agents/sales_domain.py#L439) | 439 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000440](../../agents/sales_domain.py#L440) | 440 | `"            \"signal_id\","` | — |
| [SRC-8D00DCEC0D-L000441](../../agents/sales_domain.py#L441) | 441 | `"            _clean_text(self.signal_id, field_name=\"signal_id\", maximum=160),"` | — |
| [SRC-8D00DCEC0D-L000442](../../agents/sales_domain.py#L442) | 442 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000443](../../agents/sales_domain.py#L443) | 443 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000444](../../agents/sales_domain.py#L444) | 444 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000445](../../agents/sales_domain.py#L445) | 445 | `"            \"signal_type\","` | — |
| [SRC-8D00DCEC0D-L000446](../../agents/sales_domain.py#L446) | 446 | `"            _enum_value(DemandSignalType, self.signal_type, field_name=\"signal_type\"),"` | — |
| [SRC-8D00DCEC0D-L000447](../../agents/sales_domain.py#L447) | 447 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000448](../../agents/sales_domain.py#L448) | 448 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000449](../../agents/sales_domain.py#L449) | 449 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000450](../../agents/sales_domain.py#L450) | 450 | `"            \"product_fit\","` | — |
| [SRC-8D00DCEC0D-L000451](../../agents/sales_domain.py#L451) | 451 | `"            _enum_value(ProductFit, self.product_fit, field_name=\"product_fit\"),"` | — |
| [SRC-8D00DCEC0D-L000452](../../agents/sales_domain.py#L452) | 452 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000453](../../agents/sales_domain.py#L453) | 453 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000454](../../agents/sales_domain.py#L454) | 454 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000455](../../agents/sales_domain.py#L455) | 455 | `"            \"identity_status\","` | — |
| [SRC-8D00DCEC0D-L000456](../../agents/sales_domain.py#L456) | 456 | `"            _enum_value(IdentityStatus, self.identity_status, field_name=\"identity_status\"),"` | — |
| [SRC-8D00DCEC0D-L000457](../../agents/sales_domain.py#L457) | 457 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000458](../../agents/sales_domain.py#L458) | 458 | `"        if not isinstance(self.evidence, DemandEvidence):"` | — |
| [SRC-8D00DCEC0D-L000459](../../agents/sales_domain.py#L459) | 459 | `"            raise TypeError(\"evidence must be a DemandEvidence instance\")"` | — |
| [SRC-8D00DCEC0D-L000460](../../agents/sales_domain.py#L460) | 460 | `"        for name in (\"classification_reason\", \"product_fit_reason\"):"` | — |
| [SRC-8D00DCEC0D-L000461](../../agents/sales_domain.py#L461) | 461 | `"            value = getattr(self, name)"` | — |
| [SRC-8D00DCEC0D-L000462](../../agents/sales_domain.py#L462) | 462 | `"            if not isinstance(value, str):"` | — |
| [SRC-8D00DCEC0D-L000463](../../agents/sales_domain.py#L463) | 463 | `"                raise TypeError(f\"{name} must be a string\")"` | — |
| [SRC-8D00DCEC0D-L000464](../../agents/sales_domain.py#L464) | 464 | `"            if len(value) > 500:"` | — |
| [SRC-8D00DCEC0D-L000465](../../agents/sales_domain.py#L465) | 465 | `"                raise ValueError(f\"{name} exceeds 500 characters\")"` | — |
| [SRC-8D00DCEC0D-L000466](../../agents/sales_domain.py#L466) | 466 | `"        if self.product_fit == ProductFit.UNASSESSED and self.product_fit_reason:"` | — |
| [SRC-8D00DCEC0D-L000467](../../agents/sales_domain.py#L467) | 467 | `"            raise ValueError(\"unassessed product fit must not have a fit rationale\")"` | — |
| [SRC-8D00DCEC0D-L000468](../../agents/sales_domain.py#L468) | 468 | `"        if self.product_fit != ProductFit.UNASSESSED and not self.product_fit_reason.strip():"` | — |
| [SRC-8D00DCEC0D-L000469](../../agents/sales_domain.py#L469) | 469 | `"            raise ValueError(\"assessed product fit requires a rationale\")"` | — |
| [SRC-8D00DCEC0D-L000470](../../agents/sales_domain.py#L470) | 470 | `""` | — |
| [SRC-8D00DCEC0D-L000471](../../agents/sales_domain.py#L471) | 471 | `"    def to_dict(self) -> dict[str, object]:"` | — |
| [SRC-8D00DCEC0D-L000472](../../agents/sales_domain.py#L472) | 472 | `"        return {"` | — |
| [SRC-8D00DCEC0D-L000473](../../agents/sales_domain.py#L473) | 473 | `"            \"signal_id\": self.signal_id,"` | — |
| [SRC-8D00DCEC0D-L000474](../../agents/sales_domain.py#L474) | 474 | `"            \"signal_type\": self.signal_type.value,"` | — |
| [SRC-8D00DCEC0D-L000475](../../agents/sales_domain.py#L475) | 475 | `"            \"evidence\": self.evidence.to_dict(),"` | — |
| [SRC-8D00DCEC0D-L000476](../../agents/sales_domain.py#L476) | 476 | `"            \"product_fit\": self.product_fit.value,"` | — |
| [SRC-8D00DCEC0D-L000477](../../agents/sales_domain.py#L477) | 477 | `"            \"identity_status\": self.identity_status.value,"` | — |
| [SRC-8D00DCEC0D-L000478](../../agents/sales_domain.py#L478) | 478 | `"            \"classification_reason\": self.classification_reason,"` | — |
| [SRC-8D00DCEC0D-L000479](../../agents/sales_domain.py#L479) | 479 | `"            \"product_fit_reason\": self.product_fit_reason,"` | — |
| [SRC-8D00DCEC0D-L000480](../../agents/sales_domain.py#L480) | 480 | `"        }"` | — |
| [SRC-8D00DCEC0D-L000481](../../agents/sales_domain.py#L481) | 481 | `""` | — |
| [SRC-8D00DCEC0D-L000482](../../agents/sales_domain.py#L482) | 482 | `""` | — |
| [SRC-8D00DCEC0D-L000483](../../agents/sales_domain.py#L483) | 483 | `"@dataclass(frozen=True, slots=True)"` | — |
| [SRC-8D00DCEC0D-L000484](../../agents/sales_domain.py#L484) | 484 | `"class LeadQualification:"` | — |
| [SRC-8D00DCEC0D-L000485](../../agents/sales_domain.py#L485) | 485 | `"    \"\"\"Independent qualification dimensions; deliberately contains no purchase score.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000486](../../agents/sales_domain.py#L486) | 486 | `""` | — |
| [SRC-8D00DCEC0D-L000487](../../agents/sales_domain.py#L487) | 487 | `"    signal_id: str"` | — |
| [SRC-8D00DCEC0D-L000488](../../agents/sales_domain.py#L488) | 488 | `"    product_fit: ProductFit = ProductFit.UNASSESSED"` | — |
| [SRC-8D00DCEC0D-L000489](../../agents/sales_domain.py#L489) | 489 | `"    source_quality: SourceQuality = SourceQuality.UNKNOWN"` | — |
| [SRC-8D00DCEC0D-L000490](../../agents/sales_domain.py#L490) | 490 | `"    freshness: FreshnessStatus = FreshnessStatus.UNKNOWN"` | — |
| [SRC-8D00DCEC0D-L000491](../../agents/sales_domain.py#L491) | 491 | `"    identity_status: IdentityStatus = IdentityStatus.UNKNOWN"` | — |
| [SRC-8D00DCEC0D-L000492](../../agents/sales_domain.py#L492) | 492 | `"    contactability: ContactabilityStatus = ContactabilityStatus.NOT_ASSESSED"` | — |
| [SRC-8D00DCEC0D-L000493](../../agents/sales_domain.py#L493) | 493 | `"    missing_information: tuple[str, ...] = ()"` | — |
| [SRC-8D00DCEC0D-L000494](../../agents/sales_domain.py#L494) | 494 | `""` | — |
| [SRC-8D00DCEC0D-L000495](../../agents/sales_domain.py#L495) | 495 | `"    def __post_init__(self) -> None:"` | — |
| [SRC-8D00DCEC0D-L000496](../../agents/sales_domain.py#L496) | 496 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000497](../../agents/sales_domain.py#L497) | 497 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000498](../../agents/sales_domain.py#L498) | 498 | `"            \"signal_id\","` | — |
| [SRC-8D00DCEC0D-L000499](../../agents/sales_domain.py#L499) | 499 | `"            _clean_text(self.signal_id, field_name=\"signal_id\", maximum=160),"` | — |
| [SRC-8D00DCEC0D-L000500](../../agents/sales_domain.py#L500) | 500 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000501](../../agents/sales_domain.py#L501) | 501 | `"        for name, enum_type in ("` | — |
| [SRC-8D00DCEC0D-L000502](../../agents/sales_domain.py#L502) | 502 | `"            (\"product_fit\", ProductFit),"` | — |
| [SRC-8D00DCEC0D-L000503](../../agents/sales_domain.py#L503) | 503 | `"            (\"source_quality\", SourceQuality),"` | — |
| [SRC-8D00DCEC0D-L000504](../../agents/sales_domain.py#L504) | 504 | `"            (\"freshness\", FreshnessStatus),"` | — |
| [SRC-8D00DCEC0D-L000505](../../agents/sales_domain.py#L505) | 505 | `"            (\"identity_status\", IdentityStatus),"` | — |
| [SRC-8D00DCEC0D-L000506](../../agents/sales_domain.py#L506) | 506 | `"            (\"contactability\", ContactabilityStatus),"` | — |
| [SRC-8D00DCEC0D-L000507](../../agents/sales_domain.py#L507) | 507 | `"        ):"` | — |
| [SRC-8D00DCEC0D-L000508](../../agents/sales_domain.py#L508) | 508 | `"            object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000509](../../agents/sales_domain.py#L509) | 509 | `"                self,"` | — |
| [SRC-8D00DCEC0D-L000510](../../agents/sales_domain.py#L510) | 510 | `"                name,"` | — |
| [SRC-8D00DCEC0D-L000511](../../agents/sales_domain.py#L511) | 511 | `"                _enum_value(enum_type, getattr(self, name), field_name=name),"` | — |
| [SRC-8D00DCEC0D-L000512](../../agents/sales_domain.py#L512) | 512 | `"            )"` | — |
| [SRC-8D00DCEC0D-L000513](../../agents/sales_domain.py#L513) | 513 | `"        object.__setattr__("` | — |
| [SRC-8D00DCEC0D-L000514](../../agents/sales_domain.py#L514) | 514 | `"            self,"` | — |
| [SRC-8D00DCEC0D-L000515](../../agents/sales_domain.py#L515) | 515 | `"            \"missing_information\","` | — |
| [SRC-8D00DCEC0D-L000516](../../agents/sales_domain.py#L516) | 516 | `"            _clean_terms(self.missing_information, field_name=\"missing_information\"),"` | — |
| [SRC-8D00DCEC0D-L000517](../../agents/sales_domain.py#L517) | 517 | `"        )"` | — |
| [SRC-8D00DCEC0D-L000518](../../agents/sales_domain.py#L518) | 518 | `""` | — |
| [SRC-8D00DCEC0D-L000519](../../agents/sales_domain.py#L519) | 519 | `"    def to_dict(self) -> dict[str, object]:"` | — |
| [SRC-8D00DCEC0D-L000520](../../agents/sales_domain.py#L520) | 520 | `"        return {"` | — |
| [SRC-8D00DCEC0D-L000521](../../agents/sales_domain.py#L521) | 521 | `"            \"signal_id\": self.signal_id,"` | — |
| [SRC-8D00DCEC0D-L000522](../../agents/sales_domain.py#L522) | 522 | `"            \"product_fit\": self.product_fit.value,"` | — |
| [SRC-8D00DCEC0D-L000523](../../agents/sales_domain.py#L523) | 523 | `"            \"source_quality\": self.source_quality.value,"` | — |
| [SRC-8D00DCEC0D-L000524](../../agents/sales_domain.py#L524) | 524 | `"            \"freshness\": self.freshness.value,"` | — |
| [SRC-8D00DCEC0D-L000525](../../agents/sales_domain.py#L525) | 525 | `"            \"identity_status\": self.identity_status.value,"` | — |
| [SRC-8D00DCEC0D-L000526](../../agents/sales_domain.py#L526) | 526 | `"            \"contactability\": self.contactability.value,"` | — |
| [SRC-8D00DCEC0D-L000527](../../agents/sales_domain.py#L527) | 527 | `"            \"missing_information\": list(self.missing_information),"` | — |
| [SRC-8D00DCEC0D-L000528](../../agents/sales_domain.py#L528) | 528 | `"        }"` | — |
| [SRC-8D00DCEC0D-L000529](../../agents/sales_domain.py#L529) | 529 | `""` | — |
| [SRC-8D00DCEC0D-L000530](../../agents/sales_domain.py#L530) | 530 | `""` | — |
| [SRC-8D00DCEC0D-L000531](../../agents/sales_domain.py#L531) | 531 | `""` | — |
| [SRC-8D00DCEC0D-L000532](../../agents/sales_domain.py#L532) | 532 | `"MAX_BUYER_QUERY_COUNT = 8"` | — |
| [SRC-8D00DCEC0D-L000533](../../agents/sales_domain.py#L533) | 533 | `""` | — |
| [SRC-8D00DCEC0D-L000534](../../agents/sales_domain.py#L534) | 534 | `""` | — |
| [SRC-8D00DCEC0D-L000535](../../agents/sales_domain.py#L535) | 535 | `"def build_buyer_queries("` | — |
| [SRC-8D00DCEC0D-L000536](../../agents/sales_domain.py#L536) | 536 | `"    product: ProductProfile,"` | — |
| [SRC-8D00DCEC0D-L000537](../../agents/sales_domain.py#L537) | 537 | `"    market: MarketProfile \| None = None,"` | — |
| [SRC-8D00DCEC0D-L000538](../../agents/sales_domain.py#L538) | 538 | `"    *,"` | — |
| [SRC-8D00DCEC0D-L000539](../../agents/sales_domain.py#L539) | 539 | `"    locale: str = \"auto\","` | — |
| [SRC-8D00DCEC0D-L000540](../../agents/sales_domain.py#L540) | 540 | `"    existing_queries: Iterable[str] = (),"` | — |
| [SRC-8D00DCEC0D-L000541](../../agents/sales_domain.py#L541) | 541 | `"    limit: int = MAX_BUYER_QUERY_COUNT,"` | — |
| [SRC-8D00DCEC0D-L000542](../../agents/sales_domain.py#L542) | 542 | `") -> list[str]:"` | — |
| [SRC-8D00DCEC0D-L000543](../../agents/sales_domain.py#L543) | 543 | `"    \"\"\"Build bounded, product-anchored buyer queries without sector-specific defaults."` | — |
| [SRC-8D00DCEC0D-L000544](../../agents/sales_domain.py#L544) | 544 | `""` | — |
| [SRC-8D00DCEC0D-L000545](../../agents/sales_domain.py#L545) | 545 | `"    Product-specific terms come only from ProductProfile. The default intent"` | — |
| [SRC-8D00DCEC0D-L000546](../../agents/sales_domain.py#L546) | 546 | `"    vocabulary is sector-neutral; category-specific expansions must be supplied"` | — |
| [SRC-8D00DCEC0D-L000547](../../agents/sales_domain.py#L547) | 547 | `"    by an explicit taxonomy/policy rather than silently defaulting to real estate."` | — |
| [SRC-8D00DCEC0D-L000548](../../agents/sales_domain.py#L548) | 548 | `"    \"\"\""` | — |
| [SRC-8D00DCEC0D-L000549](../../agents/sales_domain.py#L549) | 549 | `"    if not isinstance(product, ProductProfile):"` | — |
| [SRC-8D00DCEC0D-L000550](../../agents/sales_domain.py#L550) | 550 | `"        raise TypeError(\"product must be a ProductProfile instance\")"` | — |
| [SRC-8D00DCEC0D-L000551](../../agents/sales_domain.py#L551) | 551 | `"    if market is not None and not isinstance(market, MarketProfile):"` | — |
| [SRC-8D00DCEC0D-L000552](../../agents/sales_domain.py#L552) | 552 | `"        raise TypeError(\"market must be a MarketProfile instance\")"` | — |
| [SRC-8D00DCEC0D-L000553](../../agents/sales_domain.py#L553) | 553 | `"    if locale not in {\"auto\", \"ar\", \"en\", \"mixed\"}:"` | — |
| [SRC-8D00DCEC0D-L000554](../../agents/sales_domain.py#L554) | 554 | `"        raise ValueError(\"locale must be auto, ar, en, or mixed\")"` | — |
| [SRC-8D00DCEC0D-L000555](../../agents/sales_domain.py#L555) | 555 | `"    if not isinstance(limit, int) or isinstance(limit, bool) or not 1 <= limit <= MAX_BUYER_QUERY_COUNT:"` | — |
| [SRC-8D00DCEC0D-L000556](../../agents/sales_domain.py#L556) | 556 | `"        raise ValueError(f\"limit must be between 1 and {MAX_BUYER_QUERY_COUNT}\")"` | — |
| [SRC-8D00DCEC0D-L000557](../../agents/sales_domain.py#L557) | 557 | `""` | — |
| [SRC-8D00DCEC0D-L000558](../../agents/sales_domain.py#L558) | 558 | `"    if locale == \"auto\":"` | — |
| [SRC-8D00DCEC0D-L000559](../../agents/sales_domain.py#L559) | 559 | `"        locale = \"ar\" if re.search(r\"[\\u0600-\\u06FF]\", product.name) else \"en\""` | — |
| [SRC-8D00DCEC0D-L000560](../../agents/sales_domain.py#L560) | 560 | `""` | — |
| [SRC-8D00DCEC0D-L000561](../../agents/sales_domain.py#L561) | 561 | `"    location_suffix = \" \".join(market.locations) if market else \"\""` | — |
| [SRC-8D00DCEC0D-L000562](../../agents/sales_domain.py#L562) | 562 | `"    product_terms = (product.name, *product.aliases)"` | — |
| [SRC-8D00DCEC0D-L000563](../../agents/sales_domain.py#L563) | 563 | `"    candidates: list[str] = []"` | — |
| [SRC-8D00DCEC0D-L000564](../../agents/sales_domain.py#L564) | 564 | `""` | — |
| [SRC-8D00DCEC0D-L000565](../../agents/sales_domain.py#L565) | 565 | `"    for term in product_terms:"` | — |
| [SRC-8D00DCEC0D-L000566](../../agents/sales_domain.py#L566) | 566 | `"        subject = \" \".join(part for part in (term, location_suffix) if part).strip()"` | — |
| [SRC-8D00DCEC0D-L000567](../../agents/sales_domain.py#L567) | 567 | `"        if locale in {\"ar\", \"mixed\"}:"` | — |
| [SRC-8D00DCEC0D-L000568](../../agents/sales_domain.py#L568) | 568 | `"            candidates.extend("` | — |
| [SRC-8D00DCEC0D-L000569](../../agents/sales_domain.py#L569) | 569 | `"                ("` | — |
| [SRC-8D00DCEC0D-L000570](../../agents/sales_domain.py#L570) | 570 | `"                    f'\"مطلوب شراء\" \"{subject}\"',"` | — |
| [SRC-8D00DCEC0D-L000571](../../agents/sales_domain.py#L571) | 571 | `"                    f'\"عايز اشتري\" \"{subject}\"',"` | — |
| [SRC-8D00DCEC0D-L000572](../../agents/sales_domain.py#L572) | 572 | `"                    f'\"أريد شراء\" \"{subject}\"',"` | — |
| [SRC-8D00DCEC0D-L000573](../../agents/sales_domain.py#L573) | 573 | `"                    f'\"بدور على\" \"{subject}\"',"` | — |
| [SRC-8D00DCEC0D-L000574](../../agents/sales_domain.py#L574) | 574 | `"                    f'\"طلب عرض سعر\" \"{subject}\"',"` | — |
| [SRC-8D00DCEC0D-L000575](../../agents/sales_domain.py#L575) | 575 | `"                    f'site:facebook.com/groups \"{subject}\" (\"مطلوب\" OR \"عايز اشتري\" OR \"بدور على\")',"` | — |
| [SRC-8D00DCEC0D-L000576](../../agents/sales_domain.py#L576) | 576 | `"                )"` | — |
| [SRC-8D00DCEC0D-L000577](../../agents/sales_domain.py#L577) | 577 | `"            )"` | — |
| [SRC-8D00DCEC0D-L000578](../../agents/sales_domain.py#L578) | 578 | `"        if locale in {\"en\", \"mixed\"}:"` | — |
| [SRC-8D00DCEC0D-L000579](../../agents/sales_domain.py#L579) | 579 | `"            candidates.extend("` | — |
| [SRC-8D00DCEC0D-L000580](../../agents/sales_domain.py#L580) | 580 | `"                ("` | — |
| [SRC-8D00DCEC0D-L000581](../../agents/sales_domain.py#L581) | 581 | `"                    f'\"looking to buy\" \"{subject}\"',"` | — |
| [SRC-8D00DCEC0D-L000582](../../agents/sales_domain.py#L582) | 582 | `"                    f'\"want to purchase\" \"{subject}\"',"` | — |
| [SRC-8D00DCEC0D-L000583](../../agents/sales_domain.py#L583) | 583 | `"                    f'\"request for quotation\" \"{subject}\"',"` | — |
| [SRC-8D00DCEC0D-L000584](../../agents/sales_domain.py#L584) | 584 | `"                    f'site:linkedin.com/posts \"{subject}\" (\"looking to buy\" OR \"purchase\")',"` | — |
| [SRC-8D00DCEC0D-L000585](../../agents/sales_domain.py#L585) | 585 | `"                )"` | — |
| [SRC-8D00DCEC0D-L000586](../../agents/sales_domain.py#L586) | 586 | `"            )"` | — |
| [SRC-8D00DCEC0D-L000587](../../agents/sales_domain.py#L587) | 587 | `""` | — |
| [SRC-8D00DCEC0D-L000588](../../agents/sales_domain.py#L588) | 588 | `"    # Planner alternatives are supplementary only. Retain one only when it"` | — |
| [SRC-8D00DCEC0D-L000589](../../agents/sales_domain.py#L589) | 589 | `"    # explicitly mentions a configured product name/alias; do not import an"` | — |
| [SRC-8D00DCEC0D-L000590](../../agents/sales_domain.py#L590) | 590 | `"    # unrelated sector or generic listing query into this product's search."` | — |
| [SRC-8D00DCEC0D-L000591](../../agents/sales_domain.py#L591) | 591 | `"    for query in existing_queries:"` | — |
| [SRC-8D00DCEC0D-L000592](../../agents/sales_domain.py#L592) | 592 | `"        if isinstance(query, str) and product.matching_terms(query):"` | — |
| [SRC-8D00DCEC0D-L000593](../../agents/sales_domain.py#L593) | 593 | `"            candidates.append(query)"` | — |
| [SRC-8D00DCEC0D-L000594](../../agents/sales_domain.py#L594) | 594 | `""` | — |
| [SRC-8D00DCEC0D-L000595](../../agents/sales_domain.py#L595) | 595 | `"    result: list[str] = []"` | — |
| [SRC-8D00DCEC0D-L000596](../../agents/sales_domain.py#L596) | 596 | `"    seen: set[str] = set()"` | — |
| [SRC-8D00DCEC0D-L000597](../../agents/sales_domain.py#L597) | 597 | `"    for query in candidates:"` | — |
| [SRC-8D00DCEC0D-L000598](../../agents/sales_domain.py#L598) | 598 | `"        cleaned = _SPACE.sub(\" \", query).strip()[:500]"` | — |
| [SRC-8D00DCEC0D-L000599](../../agents/sales_domain.py#L599) | 599 | `"        key = normalize_text(cleaned)"` | — |
| [SRC-8D00DCEC0D-L000600](../../agents/sales_domain.py#L600) | 600 | `"        if cleaned and key and key not in seen:"` | — |
| [SRC-8D00DCEC0D-L000601](../../agents/sales_domain.py#L601) | 601 | `"            result.append(cleaned)"` | — |
| [SRC-8D00DCEC0D-L000602](../../agents/sales_domain.py#L602) | 602 | `"            seen.add(key)"` | — |
| [SRC-8D00DCEC0D-L000603](../../agents/sales_domain.py#L603) | 603 | `"        if len(result) >= limit:"` | — |
| [SRC-8D00DCEC0D-L000604](../../agents/sales_domain.py#L604) | 604 | `"            break"` | — |
| [SRC-8D00DCEC0D-L000605](../../agents/sales_domain.py#L605) | 605 | `"    return result"` | — |
| [SRC-8D00DCEC0D-L000606](../../agents/sales_domain.py#L606) | 606 | `""` | — |
| [SRC-8D00DCEC0D-L000607](../../agents/sales_domain.py#L607) | 607 | `""` | — |
| [SRC-8D00DCEC0D-L000608](../../agents/sales_domain.py#L608) | 608 | `"def to_json_dict(value: ProductProfile \| MarketProfile \| DemandEvidence \| DemandSignal \| LeadQualification) -> dict[str, object]:"` | — |
| [SRC-8D00DCEC0D-L000609](../../agents/sales_domain.py#L609) | 609 | `"    \"\"\"Serialize a supported domain object without silently dropping evidence fields.\"\"\""` | — |
| [SRC-8D00DCEC0D-L000610](../../agents/sales_domain.py#L610) | 610 | `"    if not hasattr(value, \"to_dict\"):"` | — |
| [SRC-8D00DCEC0D-L000611](../../agents/sales_domain.py#L611) | 611 | `"        raise TypeError(\"unsupported sales domain object\")"` | — |
| [SRC-8D00DCEC0D-L000612](../../agents/sales_domain.py#L612) | 612 | `"    return value.to_dict()"` | — |
## الوكيل والمنطق

### FILE-6E58A660BC — [agents/search_connectors.py](../../agents/search_connectors.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6E58A660BC-L000001](../../agents/search_connectors.py#L1) | 1 | `"\"\"\"Free academic search connectors for Omarai (M1).\"\"\""` | — |
| [SRC-6E58A660BC-L000002](../../agents/search_connectors.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-6E58A660BC-L000003](../../agents/search_connectors.py#L3) | 3 | `""` | — |
| [SRC-6E58A660BC-L000004](../../agents/search_connectors.py#L4) | 4 | `"import json"` | — |
| [SRC-6E58A660BC-L000005](../../agents/search_connectors.py#L5) | 5 | `"import os"` | — |
| [SRC-6E58A660BC-L000006](../../agents/search_connectors.py#L6) | 6 | `"import re"` | — |
| [SRC-6E58A660BC-L000007](../../agents/search_connectors.py#L7) | 7 | `"import urllib.error"` | — |
| [SRC-6E58A660BC-L000008](../../agents/search_connectors.py#L8) | 8 | `"import urllib.parse"` | — |
| [SRC-6E58A660BC-L000009](../../agents/search_connectors.py#L9) | 9 | `"import urllib.request"` | — |
| [SRC-6E58A660BC-L000010](../../agents/search_connectors.py#L10) | 10 | `"from collections.abc import Callable"` | — |
| [SRC-6E58A660BC-L000011](../../agents/search_connectors.py#L11) | 11 | `"from typing import Any"` | — |
| [SRC-6E58A660BC-L000012](../../agents/search_connectors.py#L12) | 12 | `""` | — |
| [SRC-6E58A660BC-L000013](../../agents/search_connectors.py#L13) | 13 | `"MAX_CONNECTOR_RESULTS = 6"` | — |
| [SRC-6E58A660BC-L000014](../../agents/search_connectors.py#L14) | 14 | `"MAX_CONNECTOR_RESPONSE_BYTES = 2_000_000"` | — |
| [SRC-6E58A660BC-L000015](../../agents/search_connectors.py#L15) | 15 | `"DEFAULT_TIMEOUT_SECONDS = 5"` | — |
| [SRC-6E58A660BC-L000016](../../agents/search_connectors.py#L16) | 16 | `"USER_AGENT = \"OmaraiResearchBot/1.0 (mailto:ops@example.com)\""` | — |
| [SRC-6E58A660BC-L000017](../../agents/search_connectors.py#L17) | 17 | `"ConnectorFn = Callable[[str, int], list[dict[str, Any]]]"` | — |
| [SRC-6E58A660BC-L000018](../../agents/search_connectors.py#L18) | 18 | `""` | — |
| [SRC-6E58A660BC-L000019](../../agents/search_connectors.py#L19) | 19 | `""` | — |
| [SRC-6E58A660BC-L000020](../../agents/search_connectors.py#L20) | 20 | `"def _clean_text(value: Any, limit: int = 1600) -> str:"` | — |
| [SRC-6E58A660BC-L000021](../../agents/search_connectors.py#L21) | 21 | `"    if not isinstance(value, str):"` | — |
| [SRC-6E58A660BC-L000022](../../agents/search_connectors.py#L22) | 22 | `"        return \"\""` | — |
| [SRC-6E58A660BC-L000023](../../agents/search_connectors.py#L23) | 23 | `"    return re.sub(r\"\\s+\", \" \", value).strip()[:limit]"` | — |
| [SRC-6E58A660BC-L000024](../../agents/search_connectors.py#L24) | 24 | `""` | — |
| [SRC-6E58A660BC-L000025](../../agents/search_connectors.py#L25) | 25 | `""` | — |
| [SRC-6E58A660BC-L000026](../../agents/search_connectors.py#L26) | 26 | `"class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):"` | — |
| [SRC-6E58A660BC-L000027](../../agents/search_connectors.py#L27) | 27 | `"    \"\"\"Fail closed on redirects from fixed academic-provider endpoints.\"\"\""` | — |
| [SRC-6E58A660BC-L000028](../../agents/search_connectors.py#L28) | 28 | `""` | — |
| [SRC-6E58A660BC-L000029](../../agents/search_connectors.py#L29) | 29 | `"    def redirect_request(self, req, fp, code, msg, headers, newurl):"` | — |
| [SRC-6E58A660BC-L000030](../../agents/search_connectors.py#L30) | 30 | `"        return None"` | — |
| [SRC-6E58A660BC-L000031](../../agents/search_connectors.py#L31) | 31 | `""` | — |
| [SRC-6E58A660BC-L000032](../../agents/search_connectors.py#L32) | 32 | `""` | — |
| [SRC-6E58A660BC-L000033](../../agents/search_connectors.py#L33) | 33 | `"def _open_provider_request(request: urllib.request.Request, timeout: int):"` | — |
| [SRC-6E58A660BC-L000034](../../agents/search_connectors.py#L34) | 34 | `"    \"\"\"Open a provider request without following an unchecked redirect.\"\"\""` | — |
| [SRC-6E58A660BC-L000035](../../agents/search_connectors.py#L35) | 35 | `"    opener = urllib.request.build_opener(_NoRedirectHandler)"` | — |
| [SRC-6E58A660BC-L000036](../../agents/search_connectors.py#L36) | 36 | `"    return opener.open(request, timeout=timeout)"` | — |
| [SRC-6E58A660BC-L000037](../../agents/search_connectors.py#L37) | 37 | `""` | — |
| [SRC-6E58A660BC-L000038](../../agents/search_connectors.py#L38) | 38 | `""` | — |
| [SRC-6E58A660BC-L000039](../../agents/search_connectors.py#L39) | 39 | `"def _read_bounded(response) -> bytes:"` | — |
| [SRC-6E58A660BC-L000040](../../agents/search_connectors.py#L40) | 40 | `"    \"\"\"Read at most the configured response ceiling plus one sentinel byte.\"\"\""` | — |
| [SRC-6E58A660BC-L000041](../../agents/search_connectors.py#L41) | 41 | `"    body = response.read(MAX_CONNECTOR_RESPONSE_BYTES + 1)"` | — |
| [SRC-6E58A660BC-L000042](../../agents/search_connectors.py#L42) | 42 | `"    if len(body) > MAX_CONNECTOR_RESPONSE_BYTES:"` | — |
| [SRC-6E58A660BC-L000043](../../agents/search_connectors.py#L43) | 43 | `"        raise ValueError(\"academic connector response exceeds the configured size limit\")"` | — |
| [SRC-6E58A660BC-L000044](../../agents/search_connectors.py#L44) | 44 | `"    return body"` | — |
| [SRC-6E58A660BC-L000045](../../agents/search_connectors.py#L45) | 45 | `""` | — |
| [SRC-6E58A660BC-L000046](../../agents/search_connectors.py#L46) | 46 | `""` | — |
| [SRC-6E58A660BC-L000047](../../agents/search_connectors.py#L47) | 47 | `"def _http_get_json(url: str, headers: dict[str, str] \| None = None, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> Any:"` | — |
| [SRC-6E58A660BC-L000048](../../agents/search_connectors.py#L48) | 48 | `"    req_headers = {\"User-Agent\": USER_AGENT, \"Accept\": \"application/json\"}"` | — |
| [SRC-6E58A660BC-L000049](../../agents/search_connectors.py#L49) | 49 | `"    if headers:"` | — |
| [SRC-6E58A660BC-L000050](../../agents/search_connectors.py#L50) | 50 | `"        req_headers.update(headers)"` | — |
| [SRC-6E58A660BC-L000051](../../agents/search_connectors.py#L51) | 51 | `"    request = urllib.request.Request(url, headers=req_headers, method=\"GET\")"` | — |
| [SRC-6E58A660BC-L000052](../../agents/search_connectors.py#L52) | 52 | `"    with _open_provider_request(request, timeout=timeout) as response:"` | — |
| [SRC-6E58A660BC-L000053](../../agents/search_connectors.py#L53) | 53 | `"        return json.loads(_read_bounded(response).decode(\"utf-8\", errors=\"replace\"))"` | — |
| [SRC-6E58A660BC-L000054](../../agents/search_connectors.py#L54) | 54 | `""` | — |
| [SRC-6E58A660BC-L000055](../../agents/search_connectors.py#L55) | 55 | `""` | — |
| [SRC-6E58A660BC-L000056](../../agents/search_connectors.py#L56) | 56 | `"def _http_get_text(url: str, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> str:"` | — |
| [SRC-6E58A660BC-L000057](../../agents/search_connectors.py#L57) | 57 | `"    request = urllib.request.Request(url, headers={\"User-Agent\": USER_AGENT}, method=\"GET\")"` | — |
| [SRC-6E58A660BC-L000058](../../agents/search_connectors.py#L58) | 58 | `"    with _open_provider_request(request, timeout=timeout) as response:"` | — |
| [SRC-6E58A660BC-L000059](../../agents/search_connectors.py#L59) | 59 | `"        return _read_bounded(response).decode(\"utf-8\", errors=\"replace\")"` | — |
| [SRC-6E58A660BC-L000060](../../agents/search_connectors.py#L60) | 60 | `""` | — |
| [SRC-6E58A660BC-L000061](../../agents/search_connectors.py#L61) | 61 | `""` | — |
| [SRC-6E58A660BC-L000062](../../agents/search_connectors.py#L62) | 62 | `"def _result(*, title: str, url: str, snippet: str, provider: str, rank: int, query: str, published_at: str = \"\", source_class: str = \"web\") -> dict[str, Any]:"` | — |
| [SRC-6E58A660BC-L000063](../../agents/search_connectors.py#L63) | 63 | `"    return {"` | — |
| [SRC-6E58A660BC-L000064](../../agents/search_connectors.py#L64) | 64 | `"        \"title\": _clean_text(title, 300),"` | — |
| [SRC-6E58A660BC-L000065](../../agents/search_connectors.py#L65) | 65 | `"        \"url\": (url or \"\").strip(),"` | — |
| [SRC-6E58A660BC-L000066](../../agents/search_connectors.py#L66) | 66 | `"        \"snippet\": _clean_text(snippet, 1600),"` | — |
| [SRC-6E58A660BC-L000067](../../agents/search_connectors.py#L67) | 67 | `"        \"page_fetched\": False,"` | — |
| [SRC-6E58A660BC-L000068](../../agents/search_connectors.py#L68) | 68 | `"        \"provider\": provider,"` | — |
| [SRC-6E58A660BC-L000069](../../agents/search_connectors.py#L69) | 69 | `"        \"provider_rank\": rank,"` | — |
| [SRC-6E58A660BC-L000070](../../agents/search_connectors.py#L70) | 70 | `"        \"search_query\": query,"` | — |
| [SRC-6E58A660BC-L000071](../../agents/search_connectors.py#L71) | 71 | `"        \"published_at\": published_at or \"\","` | — |
| [SRC-6E58A660BC-L000072](../../agents/search_connectors.py#L72) | 72 | `"        \"source_class\": source_class,"` | — |
| [SRC-6E58A660BC-L000073](../../agents/search_connectors.py#L73) | 73 | `"    }"` | — |
| [SRC-6E58A660BC-L000074](../../agents/search_connectors.py#L74) | 74 | `""` | — |
| [SRC-6E58A660BC-L000075](../../agents/search_connectors.py#L75) | 75 | `""` | — |
| [SRC-6E58A660BC-L000076](../../agents/search_connectors.py#L76) | 76 | `"def search_openalex(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000077](../../agents/search_connectors.py#L77) | 77 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000078](../../agents/search_connectors.py#L78) | 78 | `"        return []"` | — |
| [SRC-6E58A660BC-L000079](../../agents/search_connectors.py#L79) | 79 | `"    params = urllib.parse.urlencode({\"search\": query.strip()[:240], \"per_page\": max(1, min(int(limit), MAX_CONNECTOR_RESULTS)), \"mailto\": os.getenv(\"OPENALEX_MAILTO\", \"ops@example.com\")})"` | — |
| [SRC-6E58A660BC-L000080](../../agents/search_connectors.py#L80) | 80 | `"    data = _http_get_json(f\"https://api.openalex.org/works?{params}\")"` | — |
| [SRC-6E58A660BC-L000081](../../agents/search_connectors.py#L81) | 81 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000082](../../agents/search_connectors.py#L82) | 82 | `"    for item in data.get(\"results\", [])[:limit]:"` | — |
| [SRC-6E58A660BC-L000083](../../agents/search_connectors.py#L83) | 83 | `"        if not isinstance(item, dict):"` | — |
| [SRC-6E58A660BC-L000084](../../agents/search_connectors.py#L84) | 84 | `"            continue"` | — |
| [SRC-6E58A660BC-L000085](../../agents/search_connectors.py#L85) | 85 | `"        title = item.get(\"display_name\") or \"\""` | — |
| [SRC-6E58A660BC-L000086](../../agents/search_connectors.py#L86) | 86 | `"        url = \"\""` | — |
| [SRC-6E58A660BC-L000087](../../agents/search_connectors.py#L87) | 87 | `"        primary = item.get(\"primary_location\") or {}"` | — |
| [SRC-6E58A660BC-L000088](../../agents/search_connectors.py#L88) | 88 | `"        if isinstance(primary, dict) and primary.get(\"landing_page_url\"):"` | — |
| [SRC-6E58A660BC-L000089](../../agents/search_connectors.py#L89) | 89 | `"            url = str(primary.get(\"landing_page_url\"))"` | — |
| [SRC-6E58A660BC-L000090](../../agents/search_connectors.py#L90) | 90 | `"        elif item.get(\"id\"):"` | — |
| [SRC-6E58A660BC-L000091](../../agents/search_connectors.py#L91) | 91 | `"            url = str(item.get(\"id\"))"` | — |
| [SRC-6E58A660BC-L000092](../../agents/search_connectors.py#L92) | 92 | `"        concepts = \", \".join(str(c.get(\"display_name\", \"\")) for c in (item.get(\"concepts\") or [])[:5] if isinstance(c, dict))"` | — |
| [SRC-6E58A660BC-L000093](../../agents/search_connectors.py#L93) | 93 | `"        snippet = f\"{title}. {concepts}\".strip(\". \")"` | — |
| [SRC-6E58A660BC-L000094](../../agents/search_connectors.py#L94) | 94 | `"        if title and url:"` | — |
| [SRC-6E58A660BC-L000095](../../agents/search_connectors.py#L95) | 95 | `"            rows.append(_result(title=title, url=url, snippet=snippet or title, provider=\"openalex\", rank=len(rows) + 1, query=query, published_at=str(item.get(\"publication_date\") or \"\"), source_class=\"academic\"))"` | — |
| [SRC-6E58A660BC-L000096](../../agents/search_connectors.py#L96) | 96 | `"    return rows"` | — |
| [SRC-6E58A660BC-L000097](../../agents/search_connectors.py#L97) | 97 | `""` | — |
| [SRC-6E58A660BC-L000098](../../agents/search_connectors.py#L98) | 98 | `""` | — |
| [SRC-6E58A660BC-L000099](../../agents/search_connectors.py#L99) | 99 | `"def search_arxiv(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000100](../../agents/search_connectors.py#L100) | 100 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000101](../../agents/search_connectors.py#L101) | 101 | `"        return []"` | — |
| [SRC-6E58A660BC-L000102](../../agents/search_connectors.py#L102) | 102 | `"    params = urllib.parse.urlencode({\"search_query\": f\"all:{query.strip()[:200]}\", \"start\": 0, \"max_results\": max(1, min(int(limit), MAX_CONNECTOR_RESULTS))})"` | — |
| [SRC-6E58A660BC-L000103](../../agents/search_connectors.py#L103) | 103 | `"    xml_text = _http_get_text(f\"https://export.arxiv.org/api/query?{params}\")"` | — |
| [SRC-6E58A660BC-L000104](../../agents/search_connectors.py#L104) | 104 | `"    entries = re.findall(r\"<entry>(.*?)</entry>\", xml_text, flags=re.DOTALL)"` | — |
| [SRC-6E58A660BC-L000105](../../agents/search_connectors.py#L105) | 105 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000106](../../agents/search_connectors.py#L106) | 106 | `"    for entry in entries[:limit]:"` | — |
| [SRC-6E58A660BC-L000107](../../agents/search_connectors.py#L107) | 107 | `"        title_m = re.search(r\"<title>(.*?)</title>\", entry, re.DOTALL)"` | — |
| [SRC-6E58A660BC-L000108](../../agents/search_connectors.py#L108) | 108 | `"        link_m = re.search(r\"<id>(https?://arxiv\\.org/abs/[^<]+)</id>\", entry)"` | — |
| [SRC-6E58A660BC-L000109](../../agents/search_connectors.py#L109) | 109 | `"        summary_m = re.search(r\"<summary>(.*?)</summary>\", entry, re.DOTALL)"` | — |
| [SRC-6E58A660BC-L000110](../../agents/search_connectors.py#L110) | 110 | `"        published_m = re.search(r\"<published>([^<]+)</published>\", entry)"` | — |
| [SRC-6E58A660BC-L000111](../../agents/search_connectors.py#L111) | 111 | `"        title = _clean_text(title_m.group(1) if title_m else \"\")"` | — |
| [SRC-6E58A660BC-L000112](../../agents/search_connectors.py#L112) | 112 | `"        link = link_m.group(1) if link_m else \"\""` | — |
| [SRC-6E58A660BC-L000113](../../agents/search_connectors.py#L113) | 113 | `"        summary = _clean_text(summary_m.group(1) if summary_m else \"\", 1600)"` | — |
| [SRC-6E58A660BC-L000114](../../agents/search_connectors.py#L114) | 114 | `"        published = published_m.group(1) if published_m else \"\""` | — |
| [SRC-6E58A660BC-L000115](../../agents/search_connectors.py#L115) | 115 | `"        if title and link:"` | — |
| [SRC-6E58A660BC-L000116](../../agents/search_connectors.py#L116) | 116 | `"            rows.append(_result(title=title, url=link, snippet=summary or title, provider=\"arxiv\", rank=len(rows) + 1, query=query, published_at=published, source_class=\"academic\"))"` | — |
| [SRC-6E58A660BC-L000117](../../agents/search_connectors.py#L117) | 117 | `"    return rows"` | — |
| [SRC-6E58A660BC-L000118](../../agents/search_connectors.py#L118) | 118 | `""` | — |
| [SRC-6E58A660BC-L000119](../../agents/search_connectors.py#L119) | 119 | `""` | — |
| [SRC-6E58A660BC-L000120](../../agents/search_connectors.py#L120) | 120 | `"def search_crossref(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000121](../../agents/search_connectors.py#L121) | 121 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000122](../../agents/search_connectors.py#L122) | 122 | `"        return []"` | — |
| [SRC-6E58A660BC-L000123](../../agents/search_connectors.py#L123) | 123 | `"    params = urllib.parse.urlencode({\"query\": query.strip()[:240], \"rows\": max(1, min(int(limit), MAX_CONNECTOR_RESULTS)), \"mailto\": os.getenv(\"CROSSREF_MAILTO\", \"ops@example.com\")})"` | — |
| [SRC-6E58A660BC-L000124](../../agents/search_connectors.py#L124) | 124 | `"    data = _http_get_json(f\"https://api.crossref.org/works?{params}\", headers={\"User-Agent\": USER_AGENT})"` | — |
| [SRC-6E58A660BC-L000125](../../agents/search_connectors.py#L125) | 125 | `"    items = ((data.get(\"message\") or {}).get(\"items\") or [])[:limit]"` | — |
| [SRC-6E58A660BC-L000126](../../agents/search_connectors.py#L126) | 126 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000127](../../agents/search_connectors.py#L127) | 127 | `"    for item in items:"` | — |
| [SRC-6E58A660BC-L000128](../../agents/search_connectors.py#L128) | 128 | `"        if not isinstance(item, dict):"` | — |
| [SRC-6E58A660BC-L000129](../../agents/search_connectors.py#L129) | 129 | `"            continue"` | — |
| [SRC-6E58A660BC-L000130](../../agents/search_connectors.py#L130) | 130 | `"        title_list = item.get(\"title\") or []"` | — |
| [SRC-6E58A660BC-L000131](../../agents/search_connectors.py#L131) | 131 | `"        title = title_list[0] if isinstance(title_list, list) and title_list else \"\""` | — |
| [SRC-6E58A660BC-L000132](../../agents/search_connectors.py#L132) | 132 | `"        url = str(item.get(\"URL\") or \"\")"` | — |
| [SRC-6E58A660BC-L000133](../../agents/search_connectors.py#L133) | 133 | `"        container_list = item.get(\"container-title\") or []"` | — |
| [SRC-6E58A660BC-L000134](../../agents/search_connectors.py#L134) | 134 | `"        container = container_list[0] if isinstance(container_list, list) and container_list else \"\""` | — |
| [SRC-6E58A660BC-L000135](../../agents/search_connectors.py#L135) | 135 | `"        year = \"\""` | — |
| [SRC-6E58A660BC-L000136](../../agents/search_connectors.py#L136) | 136 | `"        issued = item.get(\"issued\") or {}"` | — |
| [SRC-6E58A660BC-L000137](../../agents/search_connectors.py#L137) | 137 | `"        if isinstance(issued, dict) and issued.get(\"date-parts\"):"` | — |
| [SRC-6E58A660BC-L000138](../../agents/search_connectors.py#L138) | 138 | `"            try:"` | — |
| [SRC-6E58A660BC-L000139](../../agents/search_connectors.py#L139) | 139 | `"                year = str(issued[\"date-parts\"][0][0])"` | — |
| [SRC-6E58A660BC-L000140](../../agents/search_connectors.py#L140) | 140 | `"            except (IndexError, TypeError, KeyError):"` | — |
| [SRC-6E58A660BC-L000141](../../agents/search_connectors.py#L141) | 141 | `"                year = \"\""` | — |
| [SRC-6E58A660BC-L000142](../../agents/search_connectors.py#L142) | 142 | `"        snippet = _clean_text(f\"{title}. {container} {year}\".strip())"` | — |
| [SRC-6E58A660BC-L000143](../../agents/search_connectors.py#L143) | 143 | `"        if title and url:"` | — |
| [SRC-6E58A660BC-L000144](../../agents/search_connectors.py#L144) | 144 | `"            rows.append(_result(title=title, url=url, snippet=snippet, provider=\"crossref\", rank=len(rows) + 1, query=query, published_at=year, source_class=\"academic\"))"` | — |
| [SRC-6E58A660BC-L000145](../../agents/search_connectors.py#L145) | 145 | `"    return rows"` | — |
| [SRC-6E58A660BC-L000146](../../agents/search_connectors.py#L146) | 146 | `""` | — |
| [SRC-6E58A660BC-L000147](../../agents/search_connectors.py#L147) | 147 | `""` | — |
| [SRC-6E58A660BC-L000148](../../agents/search_connectors.py#L148) | 148 | `"def search_semantic_scholar(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000149](../../agents/search_connectors.py#L149) | 149 | `"    if not isinstance(query, str) or not query.strip():"` | — |
