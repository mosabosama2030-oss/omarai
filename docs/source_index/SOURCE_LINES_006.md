# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **006**
- سجلات الأسطر: **800**
- النطاق: SRC-1E32639872-L000301 إلى SRC-8D00DCEC0D-L000256
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1E32639872 — [agents/research_completion.py](../../agents/research_completion.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1E32639872-L000301](../../agents/research_completion.py#L301) | 301 | `"            \"connector_status_counts\": connector_counts,"` | — |
| [SRC-1E32639872-L000302](../../agents/research_completion.py#L302) | 302 | `"            \"connector_failure_count\": connector_errors,"` | — |
| [SRC-1E32639872-L000303](../../agents/research_completion.py#L303) | 303 | `"            \"connector_success_count\": connector_ok,"` | — |
| [SRC-1E32639872-L000304](../../agents/research_completion.py#L304) | 304 | `"            \"guardrail_rejected_candidate_count\": rejected,"` | — |
| [SRC-1E32639872-L000305](../../agents/research_completion.py#L305) | 305 | `"            \"potentially_unsupported_numeric_count\": unsupported_numeric_count,"` | — |
| [SRC-1E32639872-L000306](../../agents/research_completion.py#L306) | 306 | `"            \"potentially_unsupported_numeric_by_citation_count\": unsupported_numeric_by_citation_count,"` | — |
| [SRC-1E32639872-L000307](../../agents/research_completion.py#L307) | 307 | `"            \"weak_citation_alignment_count\": weak_citation_alignment_count,"` | — |
| [SRC-1E32639872-L000308](../../agents/research_completion.py#L308) | 308 | `"            \"citation_support_warning_count\": citation_support_warning_count,"` | — |
| [SRC-1E32639872-L000309](../../agents/research_completion.py#L309) | 309 | `"        },"` | — |
| [SRC-1E32639872-L000310](../../agents/research_completion.py#L310) | 310 | `"        \"counter_consistency\": {"` | — |
| [SRC-1E32639872-L000311](../../agents/research_completion.py#L311) | 311 | `"            \"status\": \"mismatch_detected\" if counter_issues else ("` | — |
| [SRC-1E32639872-L000312](../../agents/research_completion.py#L312) | 312 | `"                \"matched\" if reported_sources is not None or reported_fetched is not None"` | — |
| [SRC-1E32639872-L000313](../../agents/research_completion.py#L313) | 313 | `"                else \"not_computable\""` | — |
| [SRC-1E32639872-L000314](../../agents/research_completion.py#L314) | 314 | `"            ),"` | — |
| [SRC-1E32639872-L000315](../../agents/research_completion.py#L315) | 315 | `"            \"reported_unique_sources\": reported_sources,"` | — |
| [SRC-1E32639872-L000316](../../agents/research_completion.py#L316) | 316 | `"            \"recomputed_final_source_count\": len(sources),"` | — |
| [SRC-1E32639872-L000317](../../agents/research_completion.py#L317) | 317 | `"            \"reported_pages_fetched\": reported_fetched,"` | — |
| [SRC-1E32639872-L000318](../../agents/research_completion.py#L318) | 318 | `"            \"recomputed_pages_fetched_flag_count\": fetched,"` | — |
| [SRC-1E32639872-L000319](../../agents/research_completion.py#L319) | 319 | `"            \"issues\": counter_issues,"` | — |
| [SRC-1E32639872-L000320](../../agents/research_completion.py#L320) | 320 | `"        },"` | — |
| [SRC-1E32639872-L000321](../../agents/research_completion.py#L321) | 321 | `"        \"semantic_verification\": \"not_performed\","` | — |
| [SRC-1E32639872-L000322](../../agents/research_completion.py#L322) | 322 | `"        \"warning\": ("` | — |
| [SRC-1E32639872-L000323](../../agents/research_completion.py#L323) | 323 | `"            \"Readable pages and valid citation indexes do not prove semantic support \""` | — |
| [SRC-1E32639872-L000324](../../agents/research_completion.py#L324) | 324 | `"            \"for each claim in the answer.\""` | — |
| [SRC-1E32639872-L000325](../../agents/research_completion.py#L325) | 325 | `"        ),"` | — |
| [SRC-1E32639872-L000326](../../agents/research_completion.py#L326) | 326 | `"    }"` | — |
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
| [SRC-3AA6165B18-L000015](../../agents/research_guardrails.py#L15) | 15 | `"    detect_freshness,"` | — |
| [SRC-3AA6165B18-L000016](../../agents/research_guardrails.py#L16) | 16 | `")"` | — |
| [SRC-3AA6165B18-L000017](../../agents/research_guardrails.py#L17) | 17 | `""` | — |
| [SRC-3AA6165B18-L000018](../../agents/research_guardrails.py#L18) | 18 | `"_CURRENT_EVIDENCE_MAX_AGE_DAYS = 7"` | — |
| [SRC-3AA6165B18-L000019](../../agents/research_guardrails.py#L19) | 19 | `"_GOVERNMENT_SUFFIXES = ("` | — |
| [SRC-3AA6165B18-L000020](../../agents/research_guardrails.py#L20) | 20 | `"    \".gov\", \".gov.eg\", \".gov.uk\", \".gov.sa\", \".gov.ae\", \".gov.au\","` | — |
| [SRC-3AA6165B18-L000021](../../agents/research_guardrails.py#L21) | 21 | `"    \".gov.in\", \".gov.cn\", \".gov.br\", \".gob.mx\", \".go.jp\", \".gc.ca\","` | — |
| [SRC-3AA6165B18-L000022](../../agents/research_guardrails.py#L22) | 22 | `"    \".govt.nz\", \".gouv.fr\","` | — |
| [SRC-3AA6165B18-L000023](../../agents/research_guardrails.py#L23) | 23 | `")"` | — |
| [SRC-3AA6165B18-L000024](../../agents/research_guardrails.py#L24) | 24 | `"_CURRENT_GOVERNMENT_SERVICE_TERMS = ("` | — |
| [SRC-3AA6165B18-L000025](../../agents/research_guardrails.py#L25) | 25 | `"    \"الجوازات\", \"مكتب الجوازات\", \"مصلحة الجوازات\", \"السجل المدني\","` | — |
| [SRC-3AA6165B18-L000026](../../agents/research_guardrails.py#L26) | 26 | `"    \"الشهر العقاري\", \"مكتب المرور\", \"إدارة المرور\", \"مكتب حكومي\","` | — |
| [SRC-3AA6165B18-L000027](../../agents/research_guardrails.py#L27) | 27 | `"    \"خدمة حكومية\", \"مصلحة حكومية\", \"وزارة\", \"هيئة حكومية\","` | — |
| [SRC-3AA6165B18-L000028](../../agents/research_guardrails.py#L28) | 28 | `"    \"passport office\", \"civil registry\", \"traffic office\","` | — |
| [SRC-3AA6165B18-L000029](../../agents/research_guardrails.py#L29) | 29 | `"    \"government office\", \"government service\","` | — |
| [SRC-3AA6165B18-L000030](../../agents/research_guardrails.py#L30) | 30 | `")"` | — |
| [SRC-3AA6165B18-L000031](../../agents/research_guardrails.py#L31) | 31 | `"_GOVERNMENT_HOURS_TERMS = ("` | — |
| [SRC-3AA6165B18-L000032](../../agents/research_guardrails.py#L32) | 32 | `"    \"مواعيد\", \"مواعيد العمل\", \"ساعات العمل\", \"يفتح\", \"مفتوح\","` | — |
| [SRC-3AA6165B18-L000033](../../agents/research_guardrails.py#L33) | 33 | `"    \"يغلق\", \"مواعيد الدوام\", \"working hours\", \"opening hours\","` | — |
| [SRC-3AA6165B18-L000034](../../agents/research_guardrails.py#L34) | 34 | `"    \"office hours\", \"open today\", \"closes today\","` | — |
| [SRC-3AA6165B18-L000035](../../agents/research_guardrails.py#L35) | 35 | `")"` | — |
| [SRC-3AA6165B18-L000036](../../agents/research_guardrails.py#L36) | 36 | `"_OFFICIAL_WORDS = ("` | — |
| [SRC-3AA6165B18-L000037](../../agents/research_guardrails.py#L37) | 37 | `"    \"الموقع الرسمي\", \"موقع رسمي\", \"الصفحة الرسمية\", \"الموقع الحكومي\","` | — |
| [SRC-3AA6165B18-L000038](../../agents/research_guardrails.py#L38) | 38 | `"    \"official website\", \"official site\", \"official homepage\","` | — |
| [SRC-3AA6165B18-L000039](../../agents/research_guardrails.py#L39) | 39 | `")"` | — |
| [SRC-3AA6165B18-L000040](../../agents/research_guardrails.py#L40) | 40 | `"_GOVERNMENT_ENTITY_WORDS = ("` | — |
| [SRC-3AA6165B18-L000041](../../agents/research_guardrails.py#L41) | 41 | `"    \"وزارة\", \"الوزارة\", \"وزاره\", \"هيئة حكومية\", \"جهة حكومية\", \"مصلحة حكومية\","` | — |
| [SRC-3AA6165B18-L000042](../../agents/research_guardrails.py#L42) | 42 | `"    \"ministry\", \"government agency\", \"government ministry\", \"department of\","` | — |
| [SRC-3AA6165B18-L000043](../../agents/research_guardrails.py#L43) | 43 | `")"` | — |
| [SRC-3AA6165B18-L000044](../../agents/research_guardrails.py#L44) | 44 | `"_TODAY_WORDS = ("` | — |
| [SRC-3AA6165B18-L000045](../../agents/research_guardrails.py#L45) | 45 | `"    \"اليوم\", \"النهارده\", \"النهاردة\", \"دلوقتي\", \"الآن\", \"حاليا\","` | — |
| [SRC-3AA6165B18-L000046](../../agents/research_guardrails.py#L46) | 46 | `"    \"today\", \"right now\", \"currently\", \"current hours\","` | — |
| [SRC-3AA6165B18-L000047](../../agents/research_guardrails.py#L47) | 47 | `")"` | — |
| [SRC-3AA6165B18-L000048](../../agents/research_guardrails.py#L48) | 48 | `"_PROMOTION_TERMS = ("` | — |
| [SRC-3AA6165B18-L000049](../../agents/research_guardrails.py#L49) | 49 | `"    \"للبيع\", \"للايجار\", \"للإيجار\", \"تواصل معنا\", \"اتصل الآن\", \"واتساب\","` | — |
| [SRC-3AA6165B18-L000050](../../agents/research_guardrails.py#L50) | 50 | `"    \"للحجز\", \"اشتر الآن\", \"اطلب الآن\", \"خصم\", \"عرض خاص\", \"السعر يبدأ\","` | — |
| [SRC-3AA6165B18-L000051](../../agents/research_guardrails.py#L51) | 51 | `"    \"for sale\", \"contact us\", \"call now\", \"whatsapp\", \"buy now\", \"shop now\","` | — |
| [SRC-3AA6165B18-L000052](../../agents/research_guardrails.py#L52) | 52 | `"    \"special offer\", \"discount\", \"sponsored\", \"affiliate\","` | — |
| [SRC-3AA6165B18-L000053](../../agents/research_guardrails.py#L53) | 53 | `")"` | — |
| [SRC-3AA6165B18-L000054](../../agents/research_guardrails.py#L54) | 54 | `"_PERSONAL_EXPERIENCE_TERMS = ("` | — |
| [SRC-3AA6165B18-L000055](../../agents/research_guardrails.py#L55) | 55 | `"    \"أنا امتلك\", \"انا امتلك\", \"أنا أملك\", \"انا املك\", \"عندي\", \"معايا\","` | — |
| [SRC-3AA6165B18-L000056](../../agents/research_guardrails.py#L56) | 56 | `"    \"جربت\", \"استخدمت\", \"اشتريت\", \"امتلكت\", \"تجربتي\", \"عن تجربتي\","` | — |
| [SRC-3AA6165B18-L000057](../../agents/research_guardrails.py#L57) | 57 | `"    \"بقالى\", \"بقالي\", \"I own\", \"I bought\", \"I have owned\", \"my experience\","` | — |
| [SRC-3AA6165B18-L000058](../../agents/research_guardrails.py#L58) | 58 | `"    \"I've had\", \"i have had\", \"I use\", \"I drove\", \"in my experience\","` | — |
| [SRC-3AA6165B18-L000059](../../agents/research_guardrails.py#L59) | 59 | `")"` | — |
| [SRC-3AA6165B18-L000060](../../agents/research_guardrails.py#L60) | 60 | `"_DISCUSSION_TERMS = ("` | — |
| [SRC-3AA6165B18-L000061](../../agents/research_guardrails.py#L61) | 61 | `"    \"حد جرب\", \"هل جرب\", \"مين جرب\", \"ما رأيكم\", \"ايه رأيكم\", \"ماذا تظنون\","` | — |
| [SRC-3AA6165B18-L000062](../../agents/research_guardrails.py#L62) | 62 | `"    \"anyone tried\", \"has anyone\", \"what do you think\", \"looking for opinions\","` | — |
| [SRC-3AA6165B18-L000063](../../agents/research_guardrails.py#L63) | 63 | `")"` | — |
| [SRC-3AA6165B18-L000064](../../agents/research_guardrails.py#L64) | 64 | `""` | — |
| [SRC-3AA6165B18-L000065](../../agents/research_guardrails.py#L65) | 65 | `""` | — |
| [SRC-3AA6165B18-L000066](../../agents/research_guardrails.py#L66) | 66 | `"def _normalized(value: Any) -> str:"` | — |
| [SRC-3AA6165B18-L000067](../../agents/research_guardrails.py#L67) | 67 | `"    return re.sub(r\"\\s+\", \" \", str(value or \"\")).strip().casefold()"` | — |
| [SRC-3AA6165B18-L000068](../../agents/research_guardrails.py#L68) | 68 | `""` | — |
| [SRC-3AA6165B18-L000069](../../agents/research_guardrails.py#L69) | 69 | `""` | — |
| [SRC-3AA6165B18-L000070](../../agents/research_guardrails.py#L70) | 70 | `"def _host(value: Any) -> str:"` | — |
| [SRC-3AA6165B18-L000071](../../agents/research_guardrails.py#L71) | 71 | `"    try:"` | — |
| [SRC-3AA6165B18-L000072](../../agents/research_guardrails.py#L72) | 72 | `"        return (urlsplit(str(value or \"\").strip()).hostname or \"\").rstrip(\".\").lower()"` | — |
| [SRC-3AA6165B18-L000073](../../agents/research_guardrails.py#L73) | 73 | `"    except (TypeError, ValueError):"` | — |
| [SRC-3AA6165B18-L000074](../../agents/research_guardrails.py#L74) | 74 | `"        return \"\""` | — |
| [SRC-3AA6165B18-L000075](../../agents/research_guardrails.py#L75) | 75 | `""` | — |
| [SRC-3AA6165B18-L000076](../../agents/research_guardrails.py#L76) | 76 | `""` | — |
| [SRC-3AA6165B18-L000077](../../agents/research_guardrails.py#L77) | 77 | `"def is_social_platform_url(url: Any) -> bool:"` | — |
| [SRC-3AA6165B18-L000078](../../agents/research_guardrails.py#L78) | 78 | `"    \"\"\"Return whether a URL belongs to a recognized public social platform.\"\"\""` | — |
| [SRC-3AA6165B18-L000079](../../agents/research_guardrails.py#L79) | 79 | `"    host = _host(url)"` | — |
| [SRC-3AA6165B18-L000080](../../agents/research_guardrails.py#L80) | 80 | `"    if not host:"` | — |
| [SRC-3AA6165B18-L000081](../../agents/research_guardrails.py#L81) | 81 | `"        return False"` | — |
| [SRC-3AA6165B18-L000082](../../agents/research_guardrails.py#L82) | 82 | `"    return any(host == domain or host.endswith(\".\" + domain)"` | — |
| [SRC-3AA6165B18-L000083](../../agents/research_guardrails.py#L83) | 83 | `"               for domain in SOCIAL_DOMAINS.values())"` | — |
| [SRC-3AA6165B18-L000084](../../agents/research_guardrails.py#L84) | 84 | `""` | — |
| [SRC-3AA6165B18-L000085](../../agents/research_guardrails.py#L85) | 85 | `""` | — |
| [SRC-3AA6165B18-L000086](../../agents/research_guardrails.py#L86) | 86 | `"def _is_navigation_request(question: str) -> bool:"` | — |
| [SRC-3AA6165B18-L000087](../../agents/research_guardrails.py#L87) | 87 | `"    value = _normalized(question)"` | — |
| [SRC-3AA6165B18-L000088](../../agents/research_guardrails.py#L88) | 88 | `"    return any(term in value for term in ("` | — |
| [SRC-3AA6165B18-L000089](../../agents/research_guardrails.py#L89) | 89 | `"        \"موقع\", \"رابط\", \"لينك\", \"homepage\", \"website\", \"official site\","` | — |
| [SRC-3AA6165B18-L000090](../../agents/research_guardrails.py#L90) | 90 | `"        \"official website\", \"link to\","` | — |
| [SRC-3AA6165B18-L000091](../../agents/research_guardrails.py#L91) | 91 | `"    ))"` | — |
| [SRC-3AA6165B18-L000092](../../agents/research_guardrails.py#L92) | 92 | `""` | — |
| [SRC-3AA6165B18-L000093](../../agents/research_guardrails.py#L93) | 93 | `""` | — |
| [SRC-3AA6165B18-L000094](../../agents/research_guardrails.py#L94) | 94 | `"def requires_official_government_domain(question: str) -> bool:"` | — |
| [SRC-3AA6165B18-L000095](../../agents/research_guardrails.py#L95) | 95 | `"    \"\"\"Detect explicit requests for a government's official site, not articles about it.\"\"\""` | — |
| [SRC-3AA6165B18-L000096](../../agents/research_guardrails.py#L96) | 96 | `"    value = _normalized(question)"` | — |
| [SRC-3AA6165B18-L000097](../../agents/research_guardrails.py#L97) | 97 | `"    return ("` | — |
| [SRC-3AA6165B18-L000098](../../agents/research_guardrails.py#L98) | 98 | `"        any(term in value for term in _OFFICIAL_WORDS)"` | — |
| [SRC-3AA6165B18-L000099](../../agents/research_guardrails.py#L99) | 99 | `"        and any(term in value for term in _GOVERNMENT_ENTITY_WORDS)"` | — |
| [SRC-3AA6165B18-L000100](../../agents/research_guardrails.py#L100) | 100 | `"    )"` | — |
| [SRC-3AA6165B18-L000101](../../agents/research_guardrails.py#L101) | 101 | `""` | — |
| [SRC-3AA6165B18-L000102](../../agents/research_guardrails.py#L102) | 102 | `""` | — |
| [SRC-3AA6165B18-L000103](../../agents/research_guardrails.py#L103) | 103 | `"def _is_government_domain(url: Any) -> bool:"` | — |
| [SRC-3AA6165B18-L000104](../../agents/research_guardrails.py#L104) | 104 | `"    host = _host(url)"` | — |
| [SRC-3AA6165B18-L000105](../../agents/research_guardrails.py#L105) | 105 | `"    if not host:"` | — |
| [SRC-3AA6165B18-L000106](../../agents/research_guardrails.py#L106) | 106 | `"        return False"` | — |
| [SRC-3AA6165B18-L000107](../../agents/research_guardrails.py#L107) | 107 | `"    return any(host == suffix.lstrip(\".\") or host.endswith(suffix)"` | — |
| [SRC-3AA6165B18-L000108](../../agents/research_guardrails.py#L108) | 108 | `"               for suffix in _GOVERNMENT_SUFFIXES)"` | — |
| [SRC-3AA6165B18-L000109](../../agents/research_guardrails.py#L109) | 109 | `""` | — |
| [SRC-3AA6165B18-L000110](../../agents/research_guardrails.py#L110) | 110 | `""` | — |
| [SRC-3AA6165B18-L000111](../../agents/research_guardrails.py#L111) | 111 | `"def requires_official_current_government_source(question: str) -> bool:"` | — |
| [SRC-3AA6165B18-L000112](../../agents/research_guardrails.py#L112) | 112 | `"    \"\"\"Require an official-domain candidate for current government service hours.\"\"\""` | — |
| [SRC-3AA6165B18-L000113](../../agents/research_guardrails.py#L113) | 113 | `"    value = _normalized(question)"` | — |
| [SRC-3AA6165B18-L000114](../../agents/research_guardrails.py#L114) | 114 | `"    has_service = any("` | — |
| [SRC-3AA6165B18-L000115](../../agents/research_guardrails.py#L115) | 115 | `"        _normalized(term) in value for term in _CURRENT_GOVERNMENT_SERVICE_TERMS"` | — |
| [SRC-3AA6165B18-L000116](../../agents/research_guardrails.py#L116) | 116 | `"    )"` | — |
| [SRC-3AA6165B18-L000117](../../agents/research_guardrails.py#L117) | 117 | `"    has_hours = any("` | — |
| [SRC-3AA6165B18-L000118](../../agents/research_guardrails.py#L118) | 118 | `"        _normalized(term) in value for term in _GOVERNMENT_HOURS_TERMS"` | — |
| [SRC-3AA6165B18-L000119](../../agents/research_guardrails.py#L119) | 119 | `"    )"` | — |
| [SRC-3AA6165B18-L000120](../../agents/research_guardrails.py#L120) | 120 | `"    return detect_freshness(question) and has_service and has_hours"` | — |
| [SRC-3AA6165B18-L000121](../../agents/research_guardrails.py#L121) | 121 | `""` | — |
| [SRC-3AA6165B18-L000122](../../agents/research_guardrails.py#L122) | 122 | `""` | — |
| [SRC-3AA6165B18-L000123](../../agents/research_guardrails.py#L123) | 123 | `"def assess_current_source("` | — |
| [SRC-3AA6165B18-L000124](../../agents/research_guardrails.py#L124) | 124 | `"    source: dict[str, Any],"` | — |
| [SRC-3AA6165B18-L000125](../../agents/research_guardrails.py#L125) | 125 | `"    *,"` | — |
| [SRC-3AA6165B18-L000126](../../agents/research_guardrails.py#L126) | 126 | `"    now: datetime \| None = None,"` | — |
| [SRC-3AA6165B18-L000127](../../agents/research_guardrails.py#L127) | 127 | `"    max_age_days: int = _CURRENT_EVIDENCE_MAX_AGE_DAYS,"` | — |
| [SRC-3AA6165B18-L000128](../../agents/research_guardrails.py#L128) | 128 | `") -> dict[str, Any]:"` | — |
| [SRC-3AA6165B18-L000129](../../agents/research_guardrails.py#L129) | 129 | `"    \"\"\"Assess whether a read page can support a current-state claim.\"\"\""` | — |
| [SRC-3AA6165B18-L000130](../../agents/research_guardrails.py#L130) | 130 | `"    current = now or datetime.now(UTC)"` | — |
| [SRC-3AA6165B18-L000131](../../agents/research_guardrails.py#L131) | 131 | `"    if current.tzinfo is None:"` | — |
| [SRC-3AA6165B18-L000132](../../agents/research_guardrails.py#L132) | 132 | `"        current = current.replace(tzinfo=UTC)"` | — |
| [SRC-3AA6165B18-L000133](../../agents/research_guardrails.py#L133) | 133 | `"    published = _parse_publication_date(source.get(\"published_at\"), current)"` | — |
| [SRC-3AA6165B18-L000134](../../agents/research_guardrails.py#L134) | 134 | `"    if published is None:"` | — |
| [SRC-3AA6165B18-L000135](../../agents/research_guardrails.py#L135) | 135 | `"        return {\"eligible\": False, \"status\": \"date_unavailable\", \"age_days\": None}"` | — |
| [SRC-3AA6165B18-L000136](../../agents/research_guardrails.py#L136) | 136 | `"    if published > current + timedelta(days=1):"` | — |
| [SRC-3AA6165B18-L000137](../../agents/research_guardrails.py#L137) | 137 | `"        return {\"eligible\": False, \"status\": \"future_date\", \"age_days\": None}"` | — |
| [SRC-3AA6165B18-L000138](../../agents/research_guardrails.py#L138) | 138 | `"    age_days = max(0, (current - published).total_seconds() / 86400)"` | — |
| [SRC-3AA6165B18-L000139](../../agents/research_guardrails.py#L139) | 139 | `"    if age_days > max_age_days:"` | — |
| [SRC-3AA6165B18-L000140](../../agents/research_guardrails.py#L140) | 140 | `"        return {"` | — |
| [SRC-3AA6165B18-L000141](../../agents/research_guardrails.py#L141) | 141 | `"            \"eligible\": False,"` | — |
| [SRC-3AA6165B18-L000142](../../agents/research_guardrails.py#L142) | 142 | `"            \"status\": \"stale\","` | — |
| [SRC-3AA6165B18-L000143](../../agents/research_guardrails.py#L143) | 143 | `"            \"age_days\": round(age_days, 2),"` | — |
| [SRC-3AA6165B18-L000144](../../agents/research_guardrails.py#L144) | 144 | `"            \"max_age_days\": max_age_days,"` | — |
| [SRC-3AA6165B18-L000145](../../agents/research_guardrails.py#L145) | 145 | `"        }"` | — |
| [SRC-3AA6165B18-L000146](../../agents/research_guardrails.py#L146) | 146 | `"    if not bool(source.get(\"page_fetched\")) or not str(source.get(\"page_text\") or \"\").strip():"` | — |
| [SRC-3AA6165B18-L000147](../../agents/research_guardrails.py#L147) | 147 | `"        return {"` | — |
| [SRC-3AA6165B18-L000148](../../agents/research_guardrails.py#L148) | 148 | `"            \"eligible\": False,"` | — |
| [SRC-3AA6165B18-L000149](../../agents/research_guardrails.py#L149) | 149 | `"            \"status\": \"page_not_read\","` | — |
| [SRC-3AA6165B18-L000150](../../agents/research_guardrails.py#L150) | 150 | `"            \"age_days\": round(age_days, 2),"` | — |
| [SRC-3AA6165B18-L000151](../../agents/research_guardrails.py#L151) | 151 | `"            \"max_age_days\": max_age_days,"` | — |
| [SRC-3AA6165B18-L000152](../../agents/research_guardrails.py#L152) | 152 | `"        }"` | — |
| [SRC-3AA6165B18-L000153](../../agents/research_guardrails.py#L153) | 153 | `"    return {"` | — |
| [SRC-3AA6165B18-L000154](../../agents/research_guardrails.py#L154) | 154 | `"        \"eligible\": True,"` | — |
| [SRC-3AA6165B18-L000155](../../agents/research_guardrails.py#L155) | 155 | `"        \"status\": \"recent_page_read\","` | — |
| [SRC-3AA6165B18-L000156](../../agents/research_guardrails.py#L156) | 156 | `"        \"age_days\": round(age_days, 2),"` | — |
| [SRC-3AA6165B18-L000157](../../agents/research_guardrails.py#L157) | 157 | `"        \"max_age_days\": max_age_days,"` | — |
| [SRC-3AA6165B18-L000158](../../agents/research_guardrails.py#L158) | 158 | `"    }"` | — |
| [SRC-3AA6165B18-L000159](../../agents/research_guardrails.py#L159) | 159 | `""` | — |
| [SRC-3AA6165B18-L000160](../../agents/research_guardrails.py#L160) | 160 | `""` | — |
| [SRC-3AA6165B18-L000161](../../agents/research_guardrails.py#L161) | 161 | `"def classify_social_source(source: dict[str, Any]) -> dict[str, str]:"` | — |
| [SRC-3AA6165B18-L000162](../../agents/research_guardrails.py#L162) | 162 | `"    \"\"\"Apply a transparent, non-authoritative label to public social content.\"\"\""` | — |
| [SRC-3AA6165B18-L000163](../../agents/research_guardrails.py#L163) | 163 | `"    url = source.get(\"url\", \"\")"` | — |
| [SRC-3AA6165B18-L000164](../../agents/research_guardrails.py#L164) | 164 | `"    host = _host(url)"` | — |
| [SRC-3AA6165B18-L000165](../../agents/research_guardrails.py#L165) | 165 | `"    platform = next(("` | — |
| [SRC-3AA6165B18-L000166](../../agents/research_guardrails.py#L166) | 166 | `"        name for name, domain in SOCIAL_DOMAINS.items()"` | — |
| [SRC-3AA6165B18-L000167](../../agents/research_guardrails.py#L167) | 167 | `"        if host == domain or host.endswith(\".\" + domain)"` | — |
| [SRC-3AA6165B18-L000168](../../agents/research_guardrails.py#L168) | 168 | `"    ), \"\")"` | — |
| [SRC-3AA6165B18-L000169](../../agents/research_guardrails.py#L169) | 169 | `"    if not platform:"` | — |
| [SRC-3AA6165B18-L000170](../../agents/research_guardrails.py#L170) | 170 | `"        return {"` | — |
| [SRC-3AA6165B18-L000171](../../agents/research_guardrails.py#L171) | 171 | `"            \"opinion_source_classification\": \"not_a_social_post\","` | — |
| [SRC-3AA6165B18-L000172](../../agents/research_guardrails.py#L172) | 172 | `"            \"opinion_classification_basis\": \"URL host is not a recognized social platform\","` | — |
| [SRC-3AA6165B18-L000173](../../agents/research_guardrails.py#L173) | 173 | `"            \"opinion_classification_method\": \"heuristic_only\","` | — |
| [SRC-3AA6165B18-L000174](../../agents/research_guardrails.py#L174) | 174 | `"        }"` | — |
| [SRC-3AA6165B18-L000175](../../agents/research_guardrails.py#L175) | 175 | `""` | — |
| [SRC-3AA6165B18-L000176](../../agents/research_guardrails.py#L176) | 176 | `"    text = _normalized(\" \".join("` | — |
| [SRC-3AA6165B18-L000177](../../agents/research_guardrails.py#L177) | 177 | `"        str(source.get(field) or \"\")"` | — |
| [SRC-3AA6165B18-L000178](../../agents/research_guardrails.py#L178) | 178 | `"        for field in (\"title\", \"snippet\", \"page_text\")"` | — |
| [SRC-3AA6165B18-L000179](../../agents/research_guardrails.py#L179) | 179 | `"    ))"` | — |
| [SRC-3AA6165B18-L000180](../../agents/research_guardrails.py#L180) | 180 | `"    # Normalize the vocabulary as well as the source text so English phrases"` | — |
| [SRC-3AA6165B18-L000181](../../agents/research_guardrails.py#L181) | 181 | `"    # remain case-insensitive (for example, \"I own\" versus \"i own\")."` | — |
| [SRC-3AA6165B18-L000182](../../agents/research_guardrails.py#L182) | 182 | `"    def has_term(terms: tuple[str, ...]) -> bool:"` | — |
| [SRC-3AA6165B18-L000183](../../agents/research_guardrails.py#L183) | 183 | `"        return any(_normalized(term) in text for term in terms)"` | — |
| [SRC-3AA6165B18-L000184](../../agents/research_guardrails.py#L184) | 184 | `"    if has_term(_PROMOTION_TERMS):"` | — |
| [SRC-3AA6165B18-L000185](../../agents/research_guardrails.py#L185) | 185 | `"        label = \"promotional_or_commercial\""` | — |
| [SRC-3AA6165B18-L000186](../../agents/research_guardrails.py#L186) | 186 | `"        basis = \"commercial language detected\""` | — |
| [SRC-3AA6165B18-L000187](../../agents/research_guardrails.py#L187) | 187 | `"    elif has_term(_PERSONAL_EXPERIENCE_TERMS):"` | — |
| [SRC-3AA6165B18-L000188](../../agents/research_guardrails.py#L188) | 188 | `"        label = \"personal_experience_candidate\""` | — |
| [SRC-3AA6165B18-L000189](../../agents/research_guardrails.py#L189) | 189 | `"        basis = \"first-person experience language detected\""` | — |
| [SRC-3AA6165B18-L000190](../../agents/research_guardrails.py#L190) | 190 | `"    elif has_term(_DISCUSSION_TERMS):"` | — |
| [SRC-3AA6165B18-L000191](../../agents/research_guardrails.py#L191) | 191 | `"        label = \"discussion_or_question\""` | — |
| [SRC-3AA6165B18-L000192](../../agents/research_guardrails.py#L192) | 192 | `"        basis = \"question or discussion language detected\""` | — |
| [SRC-3AA6165B18-L000193](../../agents/research_guardrails.py#L193) | 193 | `"    else:"` | — |
| [SRC-3AA6165B18-L000194](../../agents/research_guardrails.py#L194) | 194 | `"        label = \"social_post_unclassified\""` | — |
| [SRC-3AA6165B18-L000195](../../agents/research_guardrails.py#L195) | 195 | `"        basis = \"no clear experience/discussion signal; manual review needed\""` | — |
| [SRC-3AA6165B18-L000196](../../agents/research_guardrails.py#L196) | 196 | `"    return {"` | — |
| [SRC-3AA6165B18-L000197](../../agents/research_guardrails.py#L197) | 197 | `"        \"opinion_source_classification\": label,"` | — |
| [SRC-3AA6165B18-L000198](../../agents/research_guardrails.py#L198) | 198 | `"        \"opinion_classification_basis\": basis,"` | — |
| [SRC-3AA6165B18-L000199](../../agents/research_guardrails.py#L199) | 199 | `"        \"opinion_classification_method\": \"heuristic_only\","` | — |
| [SRC-3AA6165B18-L000200](../../agents/research_guardrails.py#L200) | 200 | `"    }"` | — |
| [SRC-3AA6165B18-L000201](../../agents/research_guardrails.py#L201) | 201 | `""` | — |
| [SRC-3AA6165B18-L000202](../../agents/research_guardrails.py#L202) | 202 | `""` | — |
| [SRC-3AA6165B18-L000203](../../agents/research_guardrails.py#L203) | 203 | `"def apply_source_guardrails("` | — |
| [SRC-3AA6165B18-L000204](../../agents/research_guardrails.py#L204) | 204 | `"    question: str,"` | — |
| [SRC-3AA6165B18-L000205](../../agents/research_guardrails.py#L205) | 205 | `"    mode: str,"` | — |
| [SRC-3AA6165B18-L000206](../../agents/research_guardrails.py#L206) | 206 | `"    plan: dict[str, Any],"` | — |
| [SRC-3AA6165B18-L000207](../../agents/research_guardrails.py#L207) | 207 | `"    sources: list[dict[str, Any]],"` | — |
| [SRC-3AA6165B18-L000208](../../agents/research_guardrails.py#L208) | 208 | `"    *,"` | — |
| [SRC-3AA6165B18-L000209](../../agents/research_guardrails.py#L209) | 209 | `"    now: datetime \| None = None,"` | — |
| [SRC-3AA6165B18-L000210](../../agents/research_guardrails.py#L210) | 210 | `") -> tuple[list[dict[str, Any]], dict[str, Any]]:"` | — |
| [SRC-3AA6165B18-L000211](../../agents/research_guardrails.py#L211) | 211 | `"    \"\"\"Apply official-domain, current-evidence, and explicit social-mode guards."` | — |
| [SRC-3AA6165B18-L000212](../../agents/research_guardrails.py#L212) | 212 | `""` | — |
| [SRC-3AA6165B18-L000213](../../agents/research_guardrails.py#L213) | 213 | `"    Rejection counters describe this filter stage only. They are not search-engine"` | — |
| [SRC-3AA6165B18-L000214](../../agents/research_guardrails.py#L214) | 214 | `"    totals, and passing them is not a semantic fact check."` | — |
| [SRC-3AA6165B18-L000215](../../agents/research_guardrails.py#L215) | 215 | `"    \"\"\""` | — |
| [SRC-3AA6165B18-L000216](../../agents/research_guardrails.py#L216) | 216 | `"    clean_mode = str(mode or \"auto\").strip().lower()"` | — |
| [SRC-3AA6165B18-L000217](../../agents/research_guardrails.py#L217) | 217 | `"    explicit_official_site_request = requires_official_government_domain(question)"` | — |
| [SRC-3AA6165B18-L000218](../../agents/research_guardrails.py#L218) | 218 | `"    current_government_hours_request = requires_official_current_government_source(question)"` | — |
| [SRC-3AA6165B18-L000219](../../agents/research_guardrails.py#L219) | 219 | `"    official_required = explicit_official_site_request or current_government_hours_request"` | — |
| [SRC-3AA6165B18-L000220](../../agents/research_guardrails.py#L220) | 220 | `"    # Latest mode always requires a recent read page. Auto mode also does so for"` | — |
| [SRC-3AA6165B18-L000221](../../agents/research_guardrails.py#L221) | 221 | `"    # explicitly current questions when the planner recognizes freshness, plus"` | — |
| [SRC-3AA6165B18-L000222](../../agents/research_guardrails.py#L222) | 222 | `"    # current government-service hours even if the planner misses that signal."` | — |
| [SRC-3AA6165B18-L000223](../../agents/research_guardrails.py#L223) | 223 | `"    explicit_current_request = detect_freshness(question)"` | — |
| [SRC-3AA6165B18-L000224](../../agents/research_guardrails.py#L224) | 224 | `"    freshness_required = ("` | — |
| [SRC-3AA6165B18-L000225](../../agents/research_guardrails.py#L225) | 225 | `"        ("` | — |
| [SRC-3AA6165B18-L000226](../../agents/research_guardrails.py#L226) | 226 | `"            clean_mode == \"latest\""` | — |
| [SRC-3AA6165B18-L000227](../../agents/research_guardrails.py#L227) | 227 | `"            or ("` | — |
| [SRC-3AA6165B18-L000228](../../agents/research_guardrails.py#L228) | 228 | `"                plan.get(\"freshness\") == \"current\""` | — |
| [SRC-3AA6165B18-L000229](../../agents/research_guardrails.py#L229) | 229 | `"                and explicit_current_request"` | — |
| [SRC-3AA6165B18-L000230](../../agents/research_guardrails.py#L230) | 230 | `"            )"` | — |
| [SRC-3AA6165B18-L000231](../../agents/research_guardrails.py#L231) | 231 | `"            or current_government_hours_request"` | — |
| [SRC-3AA6165B18-L000232](../../agents/research_guardrails.py#L232) | 232 | `"        )"` | — |
| [SRC-3AA6165B18-L000233](../../agents/research_guardrails.py#L233) | 233 | `"        and not _is_navigation_request(question)"` | — |
| [SRC-3AA6165B18-L000234](../../agents/research_guardrails.py#L234) | 234 | `"    )"` | — |
| [SRC-3AA6165B18-L000235](../../agents/research_guardrails.py#L235) | 235 | `"    social_required = clean_mode == \"social\""` | — |
| [SRC-3AA6165B18-L000236](../../agents/research_guardrails.py#L236) | 236 | `"    retained: list[dict[str, Any]] = []"` | — |
| [SRC-3AA6165B18-L000237](../../agents/research_guardrails.py#L237) | 237 | `"    rejected: dict[str, int] = {}"` | — |
| [SRC-3AA6165B18-L000238](../../agents/research_guardrails.py#L238) | 238 | `"    reasons: list[dict[str, str]] = []"` | — |
| [SRC-3AA6165B18-L000239](../../agents/research_guardrails.py#L239) | 239 | `""` | — |
| [SRC-3AA6165B18-L000240](../../agents/research_guardrails.py#L240) | 240 | `"    def reject(reason: str, source: dict[str, Any]) -> None:"` | — |
| [SRC-3AA6165B18-L000241](../../agents/research_guardrails.py#L241) | 241 | `"        rejected[reason] = rejected.get(reason, 0) + 1"` | — |
| [SRC-3AA6165B18-L000242](../../agents/research_guardrails.py#L242) | 242 | `"        reasons.append({"` | — |
| [SRC-3AA6165B18-L000243](../../agents/research_guardrails.py#L243) | 243 | `"            \"reason\": reason,"` | — |
| [SRC-3AA6165B18-L000244](../../agents/research_guardrails.py#L244) | 244 | `"            \"url\": str(source.get(\"url\") or \"\")[:2048],"` | — |
| [SRC-3AA6165B18-L000245](../../agents/research_guardrails.py#L245) | 245 | `"        })"` | — |
| [SRC-3AA6165B18-L000246](../../agents/research_guardrails.py#L246) | 246 | `""` | — |
| [SRC-3AA6165B18-L000247](../../agents/research_guardrails.py#L247) | 247 | `"    for candidate in (sources if isinstance(sources, list) else []):"` | — |
| [SRC-3AA6165B18-L000248](../../agents/research_guardrails.py#L248) | 248 | `"        if not isinstance(candidate, dict):"` | — |
| [SRC-3AA6165B18-L000249](../../agents/research_guardrails.py#L249) | 249 | `"            rejected[\"malformed_candidate\"] = rejected.get(\"malformed_candidate\", 0) + 1"` | — |
| [SRC-3AA6165B18-L000250](../../agents/research_guardrails.py#L250) | 250 | `"            reasons.append({\"reason\": \"malformed_candidate\", \"url\": \"\"})"` | — |
| [SRC-3AA6165B18-L000251](../../agents/research_guardrails.py#L251) | 251 | `"            continue"` | — |
| [SRC-3AA6165B18-L000252](../../agents/research_guardrails.py#L252) | 252 | `"        source = dict(candidate)"` | — |
| [SRC-3AA6165B18-L000253](../../agents/research_guardrails.py#L253) | 253 | `"        if official_required and not _is_government_domain(source.get(\"url\")):"` | — |
| [SRC-3AA6165B18-L000254](../../agents/research_guardrails.py#L254) | 254 | `"            reject(\"not_an_official_government_domain\", source)"` | — |
| [SRC-3AA6165B18-L000255](../../agents/research_guardrails.py#L255) | 255 | `"            continue"` | — |
| [SRC-3AA6165B18-L000256](../../agents/research_guardrails.py#L256) | 256 | `"        if social_required and not is_social_platform_url(source.get(\"url\")):"` | — |
| [SRC-3AA6165B18-L000257](../../agents/research_guardrails.py#L257) | 257 | `"            reject(\"not_a_social_platform_source\", source)"` | — |
| [SRC-3AA6165B18-L000258](../../agents/research_guardrails.py#L258) | 258 | `"            continue"` | — |
| [SRC-3AA6165B18-L000259](../../agents/research_guardrails.py#L259) | 259 | `"        if freshness_required:"` | — |
| [SRC-3AA6165B18-L000260](../../agents/research_guardrails.py#L260) | 260 | `"            freshness = assess_current_source(source, now=now)"` | — |
| [SRC-3AA6165B18-L000261](../../agents/research_guardrails.py#L261) | 261 | `"            source[\"current_evidence_assessment\"] = freshness"` | — |
| [SRC-3AA6165B18-L000262](../../agents/research_guardrails.py#L262) | 262 | `"            if not freshness[\"eligible\"]:"` | — |
| [SRC-3AA6165B18-L000263](../../agents/research_guardrails.py#L263) | 263 | `"                reject(str(freshness[\"status\"]), source)"` | — |
| [SRC-3AA6165B18-L000264](../../agents/research_guardrails.py#L264) | 264 | `"                continue"` | — |
| [SRC-3AA6165B18-L000265](../../agents/research_guardrails.py#L265) | 265 | `"        if social_required or bool(plan.get(\"social_focus\")):"` | — |
| [SRC-3AA6165B18-L000266](../../agents/research_guardrails.py#L266) | 266 | `"            source.update(classify_social_source(source))"` | — |
| [SRC-3AA6165B18-L000267](../../agents/research_guardrails.py#L267) | 267 | `"        retained.append(source)"` | — |
| [SRC-3AA6165B18-L000268](../../agents/research_guardrails.py#L268) | 268 | `""` | — |
| [SRC-3AA6165B18-L000269](../../agents/research_guardrails.py#L269) | 269 | `"    status = \"passed\" if not rejected else \"filtered\""` | — |
| [SRC-3AA6165B18-L000270](../../agents/research_guardrails.py#L270) | 270 | `"    if freshness_required and retained:"` | — |
| [SRC-3AA6165B18-L000271](../../agents/research_guardrails.py#L271) | 271 | `"        current_status = \"eligible_recent_read_pages_only\""` | — |
| [SRC-3AA6165B18-L000272](../../agents/research_guardrails.py#L272) | 272 | `"    elif freshness_required:"` | — |
| [SRC-3AA6165B18-L000273](../../agents/research_guardrails.py#L273) | 273 | `"        current_status = \"no_current_eligible_evidence\""` | — |
| [SRC-3AA6165B18-L000274](../../agents/research_guardrails.py#L274) | 274 | `"    else:"` | — |
| [SRC-3AA6165B18-L000275](../../agents/research_guardrails.py#L275) | 275 | `"        current_status = \"not_required\""` | — |
| [SRC-3AA6165B18-L000276](../../agents/research_guardrails.py#L276) | 276 | `"    summary = {"` | — |
| [SRC-3AA6165B18-L000277](../../agents/research_guardrails.py#L277) | 277 | `"        \"status\": status,"` | — |
| [SRC-3AA6165B18-L000278](../../agents/research_guardrails.py#L278) | 278 | `"        \"input_sources\": len(sources) if isinstance(sources, list) else 0,"` | — |
| [SRC-3AA6165B18-L000279](../../agents/research_guardrails.py#L279) | 279 | `"        \"accepted_sources\": len(retained),"` | — |
| [SRC-3AA6165B18-L000280](../../agents/research_guardrails.py#L280) | 280 | `"        \"rejected_sources\": sum(rejected.values()),"` | — |
| [SRC-3AA6165B18-L000281](../../agents/research_guardrails.py#L281) | 281 | `"        \"rejection_counts\": rejected,"` | — |
| [SRC-3AA6165B18-L000282](../../agents/research_guardrails.py#L282) | 282 | `"        \"rejection_details\": reasons[:20],"` | — |
| [SRC-3AA6165B18-L000283](../../agents/research_guardrails.py#L283) | 283 | `"        \"official_government_domain_required\": official_required,"` | — |
| [SRC-3AA6165B18-L000284](../../agents/research_guardrails.py#L284) | 284 | `"        \"official_government_domain_reason\": ("` | — |
| [SRC-3AA6165B18-L000285](../../agents/research_guardrails.py#L285) | 285 | `"            \"explicit_official_site_request\""` | — |
| [SRC-3AA6165B18-L000286](../../agents/research_guardrails.py#L286) | 286 | `"            if explicit_official_site_request"` | — |
| [SRC-3AA6165B18-L000287](../../agents/research_guardrails.py#L287) | 287 | `"            else \"current_government_service_hours\""` | — |
| [SRC-3AA6165B18-L000288](../../agents/research_guardrails.py#L288) | 288 | `"            if current_government_hours_request"` | — |
| [SRC-3AA6165B18-L000289](../../agents/research_guardrails.py#L289) | 289 | `"            else \"not_required\""` | — |
| [SRC-3AA6165B18-L000290](../../agents/research_guardrails.py#L290) | 290 | `"        ),"` | — |
| [SRC-3AA6165B18-L000291](../../agents/research_guardrails.py#L291) | 291 | `"        \"official_domain_policy\": ("` | — |
| [SRC-3AA6165B18-L000292](../../agents/research_guardrails.py#L292) | 292 | `"            \"government-domain candidate only; organization ownership is not independently verified\""` | — |
| [SRC-3AA6165B18-L000293](../../agents/research_guardrails.py#L293) | 293 | `"            if official_required else \"not_required\""` | — |
| [SRC-3AA6165B18-L000294](../../agents/research_guardrails.py#L294) | 294 | `"        ),"` | — |
| [SRC-3AA6165B18-L000295](../../agents/research_guardrails.py#L295) | 295 | `"        \"current_evidence_required\": freshness_required,"` | — |
| [SRC-3AA6165B18-L000296](../../agents/research_guardrails.py#L296) | 296 | `"        \"current_evidence_status\": current_status,"` | — |
| [SRC-3AA6165B18-L000297](../../agents/research_guardrails.py#L297) | 297 | `"        \"current_evidence_max_age_days\": _CURRENT_EVIDENCE_MAX_AGE_DAYS if freshness_required else None,"` | — |
| [SRC-3AA6165B18-L000298](../../agents/research_guardrails.py#L298) | 298 | `"        \"social_platform_only\": social_required,"` | — |
| [SRC-3AA6165B18-L000299](../../agents/research_guardrails.py#L299) | 299 | `"        \"interpretation\": \"retrieval guardrail only; passing is not proof of claim correctness\","` | — |
| [SRC-3AA6165B18-L000300](../../agents/research_guardrails.py#L300) | 300 | `"    }"` | — |
| [SRC-3AA6165B18-L000301](../../agents/research_guardrails.py#L301) | 301 | `"    return retained, summary"` | — |
## الوكيل والمنطق

### FILE-60066C6786 — [agents/research_pipeline.py](../../agents/research_pipeline.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-60066C6786-L000001](../../agents/research_pipeline.py#L1) | 1 | `"\"\"\"One bounded orchestration path for Omarai's hybrid research pipeline."` | — |
| [SRC-60066C6786-L000002](../../agents/research_pipeline.py#L2) | 2 | `""` | — |
| [SRC-60066C6786-L000003](../../agents/research_pipeline.py#L3) | 3 | `"The coordinator composes existing deterministic interpreters and the existing"` | — |
| [SRC-60066C6786-L000004](../../agents/research_pipeline.py#L4) | 4 | `"language-model planner output. Lexical evidence matching remains a candidate"` | — |
| [SRC-60066C6786-L000005](../../agents/research_pipeline.py#L5) | 5 | `"signal; semantic matching is explicitly unassessed unless a scorer is injected."` | — |
| [SRC-60066C6786-L000006](../../agents/research_pipeline.py#L6) | 6 | `"\"\"\""` | — |
| [SRC-60066C6786-L000007](../../agents/research_pipeline.py#L7) | 7 | `"from __future__ import annotations"` | — |
| [SRC-60066C6786-L000008](../../agents/research_pipeline.py#L8) | 8 | `""` | — |
| [SRC-60066C6786-L000009](../../agents/research_pipeline.py#L9) | 9 | `"from collections.abc import Callable"` | — |
| [SRC-60066C6786-L000010](../../agents/research_pipeline.py#L10) | 10 | `"import math"` | — |
| [SRC-60066C6786-L000011](../../agents/research_pipeline.py#L11) | 11 | `"from typing import Any"` | — |
| [SRC-60066C6786-L000012](../../agents/research_pipeline.py#L12) | 12 | `""` | — |
| [SRC-60066C6786-L000013](../../agents/research_pipeline.py#L13) | 13 | `"from agents.aspect_planning import build_evidence_ledger, extract_aspects"` | — |
| [SRC-60066C6786-L000014](../../agents/research_pipeline.py#L14) | 14 | `"from agents.intent_router import ROUTES, resolve_followup_query, route_intent"` | — |
| [SRC-60066C6786-L000015](../../agents/research_pipeline.py#L15) | 15 | `"from agents.task_understanding import ("` | — |
| [SRC-60066C6786-L000016](../../agents/research_pipeline.py#L16) | 16 | `"    MAX_TASK_ASPECTS,"` | — |
| [SRC-60066C6786-L000017](../../agents/research_pipeline.py#L17) | 17 | `"    build_query_strategy_matrix,"` | — |
| [SRC-60066C6786-L000018](../../agents/research_pipeline.py#L18) | 18 | `"    build_task_spec,"` | — |
| [SRC-60066C6786-L000019](../../agents/research_pipeline.py#L19) | 19 | `")"` | — |
| [SRC-60066C6786-L000020](../../agents/research_pipeline.py#L20) | 20 | `""` | — |
| [SRC-60066C6786-L000021](../../agents/research_pipeline.py#L21) | 21 | `"MAX_PIPELINE_QUESTION_CHARS = 4000"` | — |
| [SRC-60066C6786-L000022](../../agents/research_pipeline.py#L22) | 22 | `"MAX_PIPELINE_SOURCES = 18"` | — |
| [SRC-60066C6786-L000023](../../agents/research_pipeline.py#L23) | 23 | `""` | — |
| [SRC-60066C6786-L000024](../../agents/research_pipeline.py#L24) | 24 | `""` | — |
| [SRC-60066C6786-L000025](../../agents/research_pipeline.py#L25) | 25 | `"def _clean_aspects(task_spec: dict[str, Any], question: str) -> list[str]:"` | — |
| [SRC-60066C6786-L000026](../../agents/research_pipeline.py#L26) | 26 | `"    constraints = task_spec.get(\"constraints\")"` | — |
| [SRC-60066C6786-L000027](../../agents/research_pipeline.py#L27) | 27 | `"    declared = constraints.get(\"explicit_aspects\", []) if isinstance(constraints, dict) else []"` | — |
| [SRC-60066C6786-L000028](../../agents/research_pipeline.py#L28) | 28 | `"    extracted = extract_aspects(question)"` | — |
| [SRC-60066C6786-L000029](../../agents/research_pipeline.py#L29) | 29 | `"    aspects: list[str] = []"` | — |
| [SRC-60066C6786-L000030](../../agents/research_pipeline.py#L30) | 30 | `"    seen: set[str] = set()"` | — |
| [SRC-60066C6786-L000031](../../agents/research_pipeline.py#L31) | 31 | `"    for value in [*(declared if isinstance(declared, list) else []), *extracted]:"` | — |
| [SRC-60066C6786-L000032](../../agents/research_pipeline.py#L32) | 32 | `"        if not isinstance(value, str):"` | — |
| [SRC-60066C6786-L000033](../../agents/research_pipeline.py#L33) | 33 | `"            continue"` | — |
| [SRC-60066C6786-L000034](../../agents/research_pipeline.py#L34) | 34 | `"        item = \" \".join(value.split())[:120]"` | — |
| [SRC-60066C6786-L000035](../../agents/research_pipeline.py#L35) | 35 | `"        key = item.casefold()"` | — |
| [SRC-60066C6786-L000036](../../agents/research_pipeline.py#L36) | 36 | `"        if item and key not in seen:"` | — |
| [SRC-60066C6786-L000037](../../agents/research_pipeline.py#L37) | 37 | `"            seen.add(key)"` | — |
| [SRC-60066C6786-L000038](../../agents/research_pipeline.py#L38) | 38 | `"            aspects.append(item)"` | — |
| [SRC-60066C6786-L000039](../../agents/research_pipeline.py#L39) | 39 | `"        if len(aspects) >= MAX_TASK_ASPECTS:"` | — |
| [SRC-60066C6786-L000040](../../agents/research_pipeline.py#L40) | 40 | `"            break"` | — |
| [SRC-60066C6786-L000041](../../agents/research_pipeline.py#L41) | 41 | `"    return aspects"` | — |
| [SRC-60066C6786-L000042](../../agents/research_pipeline.py#L42) | 42 | `""` | — |
| [SRC-60066C6786-L000043](../../agents/research_pipeline.py#L43) | 43 | `""` | — |
| [SRC-60066C6786-L000044](../../agents/research_pipeline.py#L44) | 44 | `""` | — |
| [SRC-60066C6786-L000045](../../agents/research_pipeline.py#L45) | 45 | `"def _has_resolved_dialogue_context(dialogue_context: dict[str, Any] \| None) -> bool:"` | — |
| [SRC-60066C6786-L000046](../../agents/research_pipeline.py#L46) | 46 | `"    if not isinstance(dialogue_context, dict):"` | — |
| [SRC-60066C6786-L000047](../../agents/research_pipeline.py#L47) | 47 | `"        return False"` | — |
| [SRC-60066C6786-L000048](../../agents/research_pipeline.py#L48) | 48 | `"    resolved_question = dialogue_context.get(\"resolved_question\")"` | — |
| [SRC-60066C6786-L000049](../../agents/research_pipeline.py#L49) | 49 | `"    return bool("` | — |
| [SRC-60066C6786-L000050](../../agents/research_pipeline.py#L50) | 50 | `"        isinstance(resolved_question, str) and resolved_question.strip()"` | — |
| [SRC-60066C6786-L000051](../../agents/research_pipeline.py#L51) | 51 | `"    ) or dialogue_context.get(\"topic_shift\") is True or dialogue_context.get("` | — |
| [SRC-60066C6786-L000052](../../agents/research_pipeline.py#L52) | 52 | `"        \"needs_clarification\""` | — |
| [SRC-60066C6786-L000053](../../agents/research_pipeline.py#L53) | 53 | `"    ) is True"` | — |
| [SRC-60066C6786-L000054](../../agents/research_pipeline.py#L54) | 54 | `""` | — |
| [SRC-60066C6786-L000055](../../agents/research_pipeline.py#L55) | 55 | `""` | — |
| [SRC-60066C6786-L000056](../../agents/research_pipeline.py#L56) | 56 | `"def evaluate_research_evidence("` | — |
| [SRC-60066C6786-L000057](../../agents/research_pipeline.py#L57) | 57 | `"    aspects: list[str],"` | — |
| [SRC-60066C6786-L000058](../../agents/research_pipeline.py#L58) | 58 | `"    sources: list[dict[str, Any]] \| None,"` | — |
| [SRC-60066C6786-L000059](../../agents/research_pipeline.py#L59) | 59 | `"    *,"` | — |
| [SRC-60066C6786-L000060](../../agents/research_pipeline.py#L60) | 60 | `"    semantic_matcher: Callable[[str, dict[str, Any]], Any] \| None = None,"` | — |
| [SRC-60066C6786-L000061](../../agents/research_pipeline.py#L61) | 61 | `") -> dict[str, Any]:"` | — |
| [SRC-60066C6786-L000062](../../agents/research_pipeline.py#L62) | 62 | `"    \"\"\"Evaluate per-aspect candidates without equating relevance with claim truth.\"\"\""` | — |
| [SRC-60066C6786-L000063](../../agents/research_pipeline.py#L63) | 63 | `"    raw_aspects = aspects if isinstance(aspects, list) else []"` | — |
| [SRC-60066C6786-L000064](../../agents/research_pipeline.py#L64) | 64 | `"    safe_aspects = ["` | — |
| [SRC-60066C6786-L000065](../../agents/research_pipeline.py#L65) | 65 | `"        item[:120] for item in raw_aspects[:MAX_TASK_ASPECTS]"` | — |
| [SRC-60066C6786-L000066](../../agents/research_pipeline.py#L66) | 66 | `"        if isinstance(item, str) and item.strip()"` | — |
| [SRC-60066C6786-L000067](../../agents/research_pipeline.py#L67) | 67 | `"    ]"` | — |
| [SRC-60066C6786-L000068](../../agents/research_pipeline.py#L68) | 68 | `"    safe_sources = ["` | — |
| [SRC-60066C6786-L000069](../../agents/research_pipeline.py#L69) | 69 | `"        item for item in (sources or [])[:MAX_PIPELINE_SOURCES]"` | — |
| [SRC-60066C6786-L000070](../../agents/research_pipeline.py#L70) | 70 | `"        if isinstance(item, dict)"` | — |
| [SRC-60066C6786-L000071](../../agents/research_pipeline.py#L71) | 71 | `"    ]"` | — |
| [SRC-60066C6786-L000072](../../agents/research_pipeline.py#L72) | 72 | `"    lexical_ledger = build_evidence_ledger(safe_aspects, safe_sources)"` | — |
| [SRC-60066C6786-L000073](../../agents/research_pipeline.py#L73) | 73 | `"    lexical_matching_status = ("` | — |
| [SRC-60066C6786-L000074](../../agents/research_pipeline.py#L74) | 74 | `"        \"evaluated\""` | — |
| [SRC-60066C6786-L000075](../../agents/research_pipeline.py#L75) | 75 | `"        if safe_aspects"` | — |
| [SRC-60066C6786-L000076](../../agents/research_pipeline.py#L76) | 76 | `"        and any("` | — |
| [SRC-60066C6786-L000077](../../agents/research_pipeline.py#L77) | 77 | `"            any(str(source.get(field) or \"\").strip() for field in (\"title\", \"snippet\", \"page_text\"))"` | — |
| [SRC-60066C6786-L000078](../../agents/research_pipeline.py#L78) | 78 | `"            for source in safe_sources"` | — |
| [SRC-60066C6786-L000079](../../agents/research_pipeline.py#L79) | 79 | `"        )"` | — |
| [SRC-60066C6786-L000080](../../agents/research_pipeline.py#L80) | 80 | `"        else \"not_assessed\""` | — |
| [SRC-60066C6786-L000081](../../agents/research_pipeline.py#L81) | 81 | `"    )"` | — |
| [SRC-60066C6786-L000082](../../agents/research_pipeline.py#L82) | 82 | `"    semantic_status = \"not_configured\""` | — |
| [SRC-60066C6786-L000083](../../agents/research_pipeline.py#L83) | 83 | `"    semantic_candidates: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-60066C6786-L000084](../../agents/research_pipeline.py#L84) | 84 | `"    semantic_errors = 0"` | — |
| [SRC-60066C6786-L000085](../../agents/research_pipeline.py#L85) | 85 | `""` | — |
| [SRC-60066C6786-L000086](../../agents/research_pipeline.py#L86) | 86 | `"    if callable(semantic_matcher) and safe_aspects and safe_sources:"` | — |
| [SRC-60066C6786-L000087](../../agents/research_pipeline.py#L87) | 87 | `"        semantic_status = \"evaluated\""` | — |
| [SRC-60066C6786-L000088](../../agents/research_pipeline.py#L88) | 88 | `"        for aspect in safe_aspects:"` | — |
| [SRC-60066C6786-L000089](../../agents/research_pipeline.py#L89) | 89 | `"            ranked: list[dict[str, Any]] = []"` | — |
| [SRC-60066C6786-L000090](../../agents/research_pipeline.py#L90) | 90 | `"            for source_index, source in enumerate(safe_sources):"` | — |
| [SRC-60066C6786-L000091](../../agents/research_pipeline.py#L91) | 91 | `"                try:"` | — |
| [SRC-60066C6786-L000092](../../agents/research_pipeline.py#L92) | 92 | `"                    raw_score = semantic_matcher(aspect, source)"` | — |
| [SRC-60066C6786-L000093](../../agents/research_pipeline.py#L93) | 93 | `"                    if isinstance(raw_score, bool):"` | — |
| [SRC-60066C6786-L000094](../../agents/research_pipeline.py#L94) | 94 | `"                        continue"` | — |
| [SRC-60066C6786-L000095](../../agents/research_pipeline.py#L95) | 95 | `"                    score = float(raw_score)"` | — |
| [SRC-60066C6786-L000096](../../agents/research_pipeline.py#L96) | 96 | `"                except Exception:"` | — |
| [SRC-60066C6786-L000097](../../agents/research_pipeline.py#L97) | 97 | `"                    semantic_errors += 1"` | — |
| [SRC-60066C6786-L000098](../../agents/research_pipeline.py#L98) | 98 | `"                    continue"` | — |
| [SRC-60066C6786-L000099](../../agents/research_pipeline.py#L99) | 99 | `"                if not math.isfinite(score) or not 0.0 <= score <= 1.0:"` | — |
| [SRC-60066C6786-L000100](../../agents/research_pipeline.py#L100) | 100 | `"                    continue"` | — |
| [SRC-60066C6786-L000101](../../agents/research_pipeline.py#L101) | 101 | `"                ranked.append({"` | — |
| [SRC-60066C6786-L000102](../../agents/research_pipeline.py#L102) | 102 | `"                    \"source_index\": source_index,"` | — |
| [SRC-60066C6786-L000103](../../agents/research_pipeline.py#L103) | 103 | `"                    \"score\": round(score, 4),"` | — |
| [SRC-60066C6786-L000104](../../agents/research_pipeline.py#L104) | 104 | `"                })"` | — |
| [SRC-60066C6786-L000105](../../agents/research_pipeline.py#L105) | 105 | `"            semantic_candidates[aspect] = sorted("` | — |
| [SRC-60066C6786-L000106](../../agents/research_pipeline.py#L106) | 106 | `"                ranked, key=lambda item: item[\"score\"], reverse=True"` | — |
| [SRC-60066C6786-L000107](../../agents/research_pipeline.py#L107) | 107 | `"            )[:5]"` | — |
| [SRC-60066C6786-L000108](../../agents/research_pipeline.py#L108) | 108 | `""` | — |
| [SRC-60066C6786-L000109](../../agents/research_pipeline.py#L109) | 109 | `"    return {"` | — |
| [SRC-60066C6786-L000110](../../agents/research_pipeline.py#L110) | 110 | `"        \"lexical_ledger\": lexical_ledger,"` | — |
| [SRC-60066C6786-L000111](../../agents/research_pipeline.py#L111) | 111 | `"        \"lexical_matching_status\": lexical_matching_status,"` | — |
| [SRC-60066C6786-L000112](../../agents/research_pipeline.py#L112) | 112 | `"        \"semantic_matching\": {"` | — |
| [SRC-60066C6786-L000113](../../agents/research_pipeline.py#L113) | 113 | `"            \"status\": \"degraded\" if semantic_errors else semantic_status,"` | — |
| [SRC-60066C6786-L000114](../../agents/research_pipeline.py#L114) | 114 | `"            \"errors\": semantic_errors,"` | — |
| [SRC-60066C6786-L000115](../../agents/research_pipeline.py#L115) | 115 | `"            \"candidates\": semantic_candidates,"` | — |
| [SRC-60066C6786-L000116](../../agents/research_pipeline.py#L116) | 116 | `"            \"meaning\": ("` | — |
| [SRC-60066C6786-L000117](../../agents/research_pipeline.py#L117) | 117 | `"                \"ترتيب مرشحات الصلة فقط؛ لا يثبت صحة الادعاءات أو كفاية الاستشهاد.\""` | — |
| [SRC-60066C6786-L000118](../../agents/research_pipeline.py#L118) | 118 | `"            ),"` | — |
| [SRC-60066C6786-L000119](../../agents/research_pipeline.py#L119) | 119 | `"        },"` | — |
| [SRC-60066C6786-L000120](../../agents/research_pipeline.py#L120) | 120 | `"        \"claim_verification\": \"delegated_to_existing_validator\","` | — |
| [SRC-60066C6786-L000121](../../agents/research_pipeline.py#L121) | 121 | `"    }"` | — |
| [SRC-60066C6786-L000122](../../agents/research_pipeline.py#L122) | 122 | `""` | — |
| [SRC-60066C6786-L000123](../../agents/research_pipeline.py#L123) | 123 | `""` | — |
| [SRC-60066C6786-L000124](../../agents/research_pipeline.py#L124) | 124 | `"def build_research_pipeline("` | — |
| [SRC-60066C6786-L000125](../../agents/research_pipeline.py#L125) | 125 | `"    question: str,"` | — |
| [SRC-60066C6786-L000126](../../agents/research_pipeline.py#L126) | 126 | `"    plan: dict[str, Any] \| None = None,"` | — |
| [SRC-60066C6786-L000127](../../agents/research_pipeline.py#L127) | 127 | `"    *,"` | — |
| [SRC-60066C6786-L000128](../../agents/research_pipeline.py#L128) | 128 | `"    history: list[dict[str, str]] \| None = None,"` | — |
| [SRC-60066C6786-L000129](../../agents/research_pipeline.py#L129) | 129 | `"    mode: str = \"auto\","` | — |
| [SRC-60066C6786-L000130](../../agents/research_pipeline.py#L130) | 130 | `"    intent_route: str = \"\","` | — |
| [SRC-60066C6786-L000131](../../agents/research_pipeline.py#L131) | 131 | `"    dialogue_context: dict[str, Any] \| None = None,"` | — |
| [SRC-60066C6786-L000132](../../agents/research_pipeline.py#L132) | 132 | `"    sources: list[dict[str, Any]] \| None = None,"` | — |
| [SRC-60066C6786-L000133](../../agents/research_pipeline.py#L133) | 133 | `"    compact_fn: Callable[[str], str] \| None = None,"` | — |
| [SRC-60066C6786-L000134](../../agents/research_pipeline.py#L134) | 134 | `"    semantic_matcher: Callable[[str, dict[str, Any]], Any] \| None = None,"` | — |
| [SRC-60066C6786-L000135](../../agents/research_pipeline.py#L135) | 135 | `") -> dict[str, Any]:"` | — |
| [SRC-60066C6786-L000136](../../agents/research_pipeline.py#L136) | 136 | `"    \"\"\"Run context→intent→task→aspects→queries→evidence as one auditable pipeline.\"\"\""` | — |
| [SRC-60066C6786-L000137](../../agents/research_pipeline.py#L137) | 137 | `"    raw_question = question[:MAX_PIPELINE_QUESTION_CHARS] if isinstance(question, str) else \"\""` | — |
| [SRC-60066C6786-L000138](../../agents/research_pipeline.py#L138) | 138 | `"    supplied_context = dialogue_context if isinstance(dialogue_context, dict) else {}"` | — |
| [SRC-60066C6786-L000139](../../agents/research_pipeline.py#L139) | 139 | `"    resolved_question = supplied_context.get(\"resolved_question\")"` | — |
| [SRC-60066C6786-L000140](../../agents/research_pipeline.py#L140) | 140 | `"    contextual_question = ("` | — |
| [SRC-60066C6786-L000141](../../agents/research_pipeline.py#L141) | 141 | `"        raw_question"` | — |
| [SRC-60066C6786-L000142](../../agents/research_pipeline.py#L142) | 142 | `"        if supplied_context.get(\"topic_shift\") is True"` | — |
| [SRC-60066C6786-L000143](../../agents/research_pipeline.py#L143) | 143 | `"        else str(resolved_question)[:MAX_PIPELINE_QUESTION_CHARS].strip()"` | — |
| [SRC-60066C6786-L000144](../../agents/research_pipeline.py#L144) | 144 | `"        if isinstance(resolved_question, str) and resolved_question.strip()"` | — |
| [SRC-60066C6786-L000145](../../agents/research_pipeline.py#L145) | 145 | `"        else resolve_followup_query(raw_question, history)"` | — |
| [SRC-60066C6786-L000146](../../agents/research_pipeline.py#L146) | 146 | `"        if history and raw_question.strip()"` | — |
| [SRC-60066C6786-L000147](../../agents/research_pipeline.py#L147) | 147 | `"        else raw_question"` | — |
| [SRC-60066C6786-L000148](../../agents/research_pipeline.py#L148) | 148 | `"    )"` | — |
| [SRC-60066C6786-L000149](../../agents/research_pipeline.py#L149) | 149 | `"    supplied_route = intent_route if isinstance(intent_route, str) else \"\""` | — |
| [SRC-60066C6786-L000150](../../agents/research_pipeline.py#L150) | 150 | `"    intent = ("` | — |
| [SRC-60066C6786-L000151](../../agents/research_pipeline.py#L151) | 151 | `"        {"` | — |
| [SRC-60066C6786-L000152](../../agents/research_pipeline.py#L152) | 152 | `"            \"route\": supplied_route,"` | — |
| [SRC-60066C6786-L000153](../../agents/research_pipeline.py#L153) | 153 | `"            \"reason\": \"upstream_route\","` | — |
| [SRC-60066C6786-L000154](../../agents/research_pipeline.py#L154) | 154 | `"            \"context_available\": bool(history) or _has_resolved_dialogue_context(dialogue_context),"` | — |
| [SRC-60066C6786-L000155](../../agents/research_pipeline.py#L155) | 155 | `"            \"needs_clarification\": supplied_route == \"CLARIFY\","` | — |
| [SRC-60066C6786-L000156](../../agents/research_pipeline.py#L156) | 156 | `"        }"` | — |
| [SRC-60066C6786-L000157](../../agents/research_pipeline.py#L157) | 157 | `"        if supplied_route in ROUTES"` | — |
| [SRC-60066C6786-L000158](../../agents/research_pipeline.py#L158) | 158 | `"        else route_intent(contextual_question, history, mode=mode)"` | — |
| [SRC-60066C6786-L000159](../../agents/research_pipeline.py#L159) | 159 | `"    )"` | — |
| [SRC-60066C6786-L000160](../../agents/research_pipeline.py#L160) | 160 | `"    route = intent.get(\"route\", \"CLARIFY\")"` | — |
| [SRC-60066C6786-L000161](../../agents/research_pipeline.py#L161) | 161 | `"    safe_plan = dict(plan) if isinstance(plan, dict) else {}"` | — |
| [SRC-60066C6786-L000162](../../agents/research_pipeline.py#L162) | 162 | `"    task_spec = build_task_spec("` | — |
| [SRC-60066C6786-L000163](../../agents/research_pipeline.py#L163) | 163 | `"        contextual_question,"` | — |
| [SRC-60066C6786-L000164](../../agents/research_pipeline.py#L164) | 164 | `"        mode=mode,"` | — |
| [SRC-60066C6786-L000165](../../agents/research_pipeline.py#L165) | 165 | `"        intent_route=route,"` | — |
| [SRC-60066C6786-L000166](../../agents/research_pipeline.py#L166) | 166 | `"        plan=safe_plan,"` | — |
| [SRC-60066C6786-L000167](../../agents/research_pipeline.py#L167) | 167 | `"        dialogue_context=dialogue_context if isinstance(dialogue_context, dict) else None,"` | — |
| [SRC-60066C6786-L000168](../../agents/research_pipeline.py#L168) | 168 | `"    )"` | — |
| [SRC-60066C6786-L000169](../../agents/research_pipeline.py#L169) | 169 | `"    aspects = _clean_aspects(task_spec, contextual_question)"` | — |
| [SRC-60066C6786-L000170](../../agents/research_pipeline.py#L170) | 170 | `"    task_requires_clarification = bool(task_spec.get(\"requires_clarification\"))"` | — |
| [SRC-60066C6786-L000171](../../agents/research_pipeline.py#L171) | 171 | `"    if task_requires_clarification and not intent.get(\"needs_clarification\"):"` | — |
| [SRC-60066C6786-L000172](../../agents/research_pipeline.py#L172) | 172 | `"        intent = dict(intent)"` | — |
| [SRC-60066C6786-L000173](../../agents/research_pipeline.py#L173) | 173 | `"        intent[\"needs_clarification\"] = True"` | — |
| [SRC-60066C6786-L000174](../../agents/research_pipeline.py#L174) | 174 | `"        intent[\"reason\"] = \"task_spec_missing_required_input\""` | — |
| [SRC-60066C6786-L000175](../../agents/research_pipeline.py#L175) | 175 | `""` | — |
| [SRC-60066C6786-L000176](../../agents/research_pipeline.py#L176) | 176 | `"    if route == \"CLARIFY\" or intent.get(\"needs_clarification\") or task_requires_clarification:"` | — |
| [SRC-60066C6786-L000177](../../agents/research_pipeline.py#L177) | 177 | `"        strategy_matrix: list[dict[str, str]] = []"` | — |
| [SRC-60066C6786-L000178](../../agents/research_pipeline.py#L178) | 178 | `"        queries: list[str] = []"` | — |
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
