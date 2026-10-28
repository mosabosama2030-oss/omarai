# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **005**
- سجلات الأسطر: **800**
- النطاق: SRC-3AA6165B18-L000002 إلى SRC-1AE03B9EC3-L000375
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-3AA6165B18 — [agents/research_guardrails.py](../../agents/research_guardrails.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-3AA6165B18-L000012](../../agents/research_guardrails.py#L12) | 12 | `"from agents.research import SOCIAL_DOMAINS, _parse_publication_date"` | — |
| [SRC-3AA6165B18-L000013](../../agents/research_guardrails.py#L13) | 13 | `""` | — |
| [SRC-3AA6165B18-L000014](../../agents/research_guardrails.py#L14) | 14 | `"_CURRENT_EVIDENCE_MAX_AGE_DAYS = 7"` | — |
| [SRC-3AA6165B18-L000015](../../agents/research_guardrails.py#L15) | 15 | `"_GOVERNMENT_SUFFIXES = ("` | — |
| [SRC-3AA6165B18-L000016](../../agents/research_guardrails.py#L16) | 16 | `"    \".gov\", \".gov.eg\", \".gov.uk\", \".gov.sa\", \".gov.ae\", \".gov.au\","` | — |
| [SRC-3AA6165B18-L000017](../../agents/research_guardrails.py#L17) | 17 | `"    \".gov.in\", \".gov.cn\", \".gov.br\", \".gob.mx\", \".go.jp\", \".gc.ca\","` | — |
| [SRC-3AA6165B18-L000018](../../agents/research_guardrails.py#L18) | 18 | `"    \".govt.nz\", \".gouv.fr\","` | — |
| [SRC-3AA6165B18-L000019](../../agents/research_guardrails.py#L19) | 19 | `")"` | — |
| [SRC-3AA6165B18-L000020](../../agents/research_guardrails.py#L20) | 20 | `"_OFFICIAL_WORDS = ("` | — |
| [SRC-3AA6165B18-L000021](../../agents/research_guardrails.py#L21) | 21 | `"    \"الموقع الرسمي\", \"موقع رسمي\", \"الصفحة الرسمية\", \"الموقع الحكومي\","` | — |
| [SRC-3AA6165B18-L000022](../../agents/research_guardrails.py#L22) | 22 | `"    \"official website\", \"official site\", \"official homepage\","` | — |
| [SRC-3AA6165B18-L000023](../../agents/research_guardrails.py#L23) | 23 | `")"` | — |
| [SRC-3AA6165B18-L000024](../../agents/research_guardrails.py#L24) | 24 | `"_GOVERNMENT_ENTITY_WORDS = ("` | — |
| [SRC-3AA6165B18-L000025](../../agents/research_guardrails.py#L25) | 25 | `"    \"وزارة\", \"الوزارة\", \"وزاره\", \"هيئة حكومية\", \"جهة حكومية\", \"مصلحة حكومية\","` | — |
| [SRC-3AA6165B18-L000026](../../agents/research_guardrails.py#L26) | 26 | `"    \"ministry\", \"government agency\", \"government ministry\", \"department of\","` | — |
| [SRC-3AA6165B18-L000027](../../agents/research_guardrails.py#L27) | 27 | `")"` | — |
| [SRC-3AA6165B18-L000028](../../agents/research_guardrails.py#L28) | 28 | `"_TODAY_WORDS = ("` | — |
| [SRC-3AA6165B18-L000029](../../agents/research_guardrails.py#L29) | 29 | `"    \"اليوم\", \"النهارده\", \"النهاردة\", \"دلوقتي\", \"الآن\", \"حاليا\","` | — |
| [SRC-3AA6165B18-L000030](../../agents/research_guardrails.py#L30) | 30 | `"    \"today\", \"right now\", \"currently\", \"current hours\","` | — |
| [SRC-3AA6165B18-L000031](../../agents/research_guardrails.py#L31) | 31 | `")"` | — |
| [SRC-3AA6165B18-L000032](../../agents/research_guardrails.py#L32) | 32 | `"_PROMOTION_TERMS = ("` | — |
| [SRC-3AA6165B18-L000033](../../agents/research_guardrails.py#L33) | 33 | `"    \"للبيع\", \"للايجار\", \"للإيجار\", \"تواصل معنا\", \"اتصل الآن\", \"واتساب\","` | — |
| [SRC-3AA6165B18-L000034](../../agents/research_guardrails.py#L34) | 34 | `"    \"للحجز\", \"اشتر الآن\", \"اطلب الآن\", \"خصم\", \"عرض خاص\", \"السعر يبدأ\","` | — |
| [SRC-3AA6165B18-L000035](../../agents/research_guardrails.py#L35) | 35 | `"    \"for sale\", \"contact us\", \"call now\", \"whatsapp\", \"buy now\", \"shop now\","` | — |
| [SRC-3AA6165B18-L000036](../../agents/research_guardrails.py#L36) | 36 | `"    \"special offer\", \"discount\", \"sponsored\", \"affiliate\","` | — |
| [SRC-3AA6165B18-L000037](../../agents/research_guardrails.py#L37) | 37 | `")"` | — |
| [SRC-3AA6165B18-L000038](../../agents/research_guardrails.py#L38) | 38 | `"_PERSONAL_EXPERIENCE_TERMS = ("` | — |
| [SRC-3AA6165B18-L000039](../../agents/research_guardrails.py#L39) | 39 | `"    \"أنا امتلك\", \"انا امتلك\", \"أنا أملك\", \"انا املك\", \"عندي\", \"معايا\","` | — |
| [SRC-3AA6165B18-L000040](../../agents/research_guardrails.py#L40) | 40 | `"    \"جربت\", \"استخدمت\", \"اشتريت\", \"امتلكت\", \"تجربتي\", \"عن تجربتي\","` | — |
| [SRC-3AA6165B18-L000041](../../agents/research_guardrails.py#L41) | 41 | `"    \"بقالى\", \"بقالي\", \"I own\", \"I bought\", \"I have owned\", \"my experience\","` | — |
| [SRC-3AA6165B18-L000042](../../agents/research_guardrails.py#L42) | 42 | `"    \"I've had\", \"i have had\", \"I use\", \"I drove\", \"in my experience\","` | — |
| [SRC-3AA6165B18-L000043](../../agents/research_guardrails.py#L43) | 43 | `")"` | — |
| [SRC-3AA6165B18-L000044](../../agents/research_guardrails.py#L44) | 44 | `"_DISCUSSION_TERMS = ("` | — |
| [SRC-3AA6165B18-L000045](../../agents/research_guardrails.py#L45) | 45 | `"    \"حد جرب\", \"هل جرب\", \"مين جرب\", \"ما رأيكم\", \"ايه رأيكم\", \"ماذا تظنون\","` | — |
| [SRC-3AA6165B18-L000046](../../agents/research_guardrails.py#L46) | 46 | `"    \"anyone tried\", \"has anyone\", \"what do you think\", \"looking for opinions\","` | — |
| [SRC-3AA6165B18-L000047](../../agents/research_guardrails.py#L47) | 47 | `")"` | — |
| [SRC-3AA6165B18-L000048](../../agents/research_guardrails.py#L48) | 48 | `""` | — |
| [SRC-3AA6165B18-L000049](../../agents/research_guardrails.py#L49) | 49 | `""` | — |
| [SRC-3AA6165B18-L000050](../../agents/research_guardrails.py#L50) | 50 | `"def _normalized(value: Any) -> str:"` | — |
| [SRC-3AA6165B18-L000051](../../agents/research_guardrails.py#L51) | 51 | `"    return re.sub(r\"\\s+\", \" \", str(value or \"\")).strip().casefold()"` | — |
| [SRC-3AA6165B18-L000052](../../agents/research_guardrails.py#L52) | 52 | `""` | — |
| [SRC-3AA6165B18-L000053](../../agents/research_guardrails.py#L53) | 53 | `""` | — |
| [SRC-3AA6165B18-L000054](../../agents/research_guardrails.py#L54) | 54 | `"def _host(value: Any) -> str:"` | — |
| [SRC-3AA6165B18-L000055](../../agents/research_guardrails.py#L55) | 55 | `"    try:"` | — |
| [SRC-3AA6165B18-L000056](../../agents/research_guardrails.py#L56) | 56 | `"        return (urlsplit(str(value or \"\").strip()).hostname or \"\").rstrip(\".\").lower()"` | — |
| [SRC-3AA6165B18-L000057](../../agents/research_guardrails.py#L57) | 57 | `"    except (TypeError, ValueError):"` | — |
| [SRC-3AA6165B18-L000058](../../agents/research_guardrails.py#L58) | 58 | `"        return \"\""` | — |
| [SRC-3AA6165B18-L000059](../../agents/research_guardrails.py#L59) | 59 | `""` | — |
| [SRC-3AA6165B18-L000060](../../agents/research_guardrails.py#L60) | 60 | `""` | — |
| [SRC-3AA6165B18-L000061](../../agents/research_guardrails.py#L61) | 61 | `"def is_social_platform_url(url: Any) -> bool:"` | — |
| [SRC-3AA6165B18-L000062](../../agents/research_guardrails.py#L62) | 62 | `"    \"\"\"Return whether a URL belongs to a recognized public social platform.\"\"\""` | — |
| [SRC-3AA6165B18-L000063](../../agents/research_guardrails.py#L63) | 63 | `"    host = _host(url)"` | — |
| [SRC-3AA6165B18-L000064](../../agents/research_guardrails.py#L64) | 64 | `"    if not host:"` | — |
| [SRC-3AA6165B18-L000065](../../agents/research_guardrails.py#L65) | 65 | `"        return False"` | — |
| [SRC-3AA6165B18-L000066](../../agents/research_guardrails.py#L66) | 66 | `"    return any(host == domain or host.endswith(\".\" + domain)"` | — |
| [SRC-3AA6165B18-L000067](../../agents/research_guardrails.py#L67) | 67 | `"               for domain in SOCIAL_DOMAINS.values())"` | — |
| [SRC-3AA6165B18-L000068](../../agents/research_guardrails.py#L68) | 68 | `""` | — |
| [SRC-3AA6165B18-L000069](../../agents/research_guardrails.py#L69) | 69 | `""` | — |
| [SRC-3AA6165B18-L000070](../../agents/research_guardrails.py#L70) | 70 | `"def _is_navigation_request(question: str) -> bool:"` | — |
| [SRC-3AA6165B18-L000071](../../agents/research_guardrails.py#L71) | 71 | `"    value = _normalized(question)"` | — |
| [SRC-3AA6165B18-L000072](../../agents/research_guardrails.py#L72) | 72 | `"    return any(term in value for term in ("` | — |
| [SRC-3AA6165B18-L000073](../../agents/research_guardrails.py#L73) | 73 | `"        \"موقع\", \"رابط\", \"لينك\", \"homepage\", \"website\", \"official site\","` | — |
| [SRC-3AA6165B18-L000074](../../agents/research_guardrails.py#L74) | 74 | `"        \"official website\", \"link to\","` | — |
| [SRC-3AA6165B18-L000075](../../agents/research_guardrails.py#L75) | 75 | `"    ))"` | — |
| [SRC-3AA6165B18-L000076](../../agents/research_guardrails.py#L76) | 76 | `""` | — |
| [SRC-3AA6165B18-L000077](../../agents/research_guardrails.py#L77) | 77 | `""` | — |
| [SRC-3AA6165B18-L000078](../../agents/research_guardrails.py#L78) | 78 | `"def requires_official_government_domain(question: str) -> bool:"` | — |
| [SRC-3AA6165B18-L000079](../../agents/research_guardrails.py#L79) | 79 | `"    \"\"\"Detect explicit requests for a government's official site, not articles about it.\"\"\""` | — |
| [SRC-3AA6165B18-L000080](../../agents/research_guardrails.py#L80) | 80 | `"    value = _normalized(question)"` | — |
| [SRC-3AA6165B18-L000081](../../agents/research_guardrails.py#L81) | 81 | `"    return ("` | — |
| [SRC-3AA6165B18-L000082](../../agents/research_guardrails.py#L82) | 82 | `"        any(term in value for term in _OFFICIAL_WORDS)"` | — |
| [SRC-3AA6165B18-L000083](../../agents/research_guardrails.py#L83) | 83 | `"        and any(term in value for term in _GOVERNMENT_ENTITY_WORDS)"` | — |
| [SRC-3AA6165B18-L000084](../../agents/research_guardrails.py#L84) | 84 | `"    )"` | — |
| [SRC-3AA6165B18-L000085](../../agents/research_guardrails.py#L85) | 85 | `""` | — |
| [SRC-3AA6165B18-L000086](../../agents/research_guardrails.py#L86) | 86 | `""` | — |
| [SRC-3AA6165B18-L000087](../../agents/research_guardrails.py#L87) | 87 | `"def _is_government_domain(url: Any) -> bool:"` | — |
| [SRC-3AA6165B18-L000088](../../agents/research_guardrails.py#L88) | 88 | `"    host = _host(url)"` | — |
| [SRC-3AA6165B18-L000089](../../agents/research_guardrails.py#L89) | 89 | `"    if not host:"` | — |
| [SRC-3AA6165B18-L000090](../../agents/research_guardrails.py#L90) | 90 | `"        return False"` | — |
| [SRC-3AA6165B18-L000091](../../agents/research_guardrails.py#L91) | 91 | `"    return any(host == suffix.lstrip(\".\") or host.endswith(suffix)"` | — |
| [SRC-3AA6165B18-L000092](../../agents/research_guardrails.py#L92) | 92 | `"               for suffix in _GOVERNMENT_SUFFIXES)"` | — |
| [SRC-3AA6165B18-L000093](../../agents/research_guardrails.py#L93) | 93 | `""` | — |
| [SRC-3AA6165B18-L000094](../../agents/research_guardrails.py#L94) | 94 | `""` | — |
| [SRC-3AA6165B18-L000095](../../agents/research_guardrails.py#L95) | 95 | `"def assess_current_source("` | — |
| [SRC-3AA6165B18-L000096](../../agents/research_guardrails.py#L96) | 96 | `"    source: dict[str, Any],"` | — |
| [SRC-3AA6165B18-L000097](../../agents/research_guardrails.py#L97) | 97 | `"    *,"` | — |
| [SRC-3AA6165B18-L000098](../../agents/research_guardrails.py#L98) | 98 | `"    now: datetime \| None = None,"` | — |
| [SRC-3AA6165B18-L000099](../../agents/research_guardrails.py#L99) | 99 | `"    max_age_days: int = _CURRENT_EVIDENCE_MAX_AGE_DAYS,"` | — |
| [SRC-3AA6165B18-L000100](../../agents/research_guardrails.py#L100) | 100 | `") -> dict[str, Any]:"` | — |
| [SRC-3AA6165B18-L000101](../../agents/research_guardrails.py#L101) | 101 | `"    \"\"\"Assess whether a read page can support a current-state claim.\"\"\""` | — |
| [SRC-3AA6165B18-L000102](../../agents/research_guardrails.py#L102) | 102 | `"    current = now or datetime.now(UTC)"` | — |
| [SRC-3AA6165B18-L000103](../../agents/research_guardrails.py#L103) | 103 | `"    if current.tzinfo is None:"` | — |
| [SRC-3AA6165B18-L000104](../../agents/research_guardrails.py#L104) | 104 | `"        current = current.replace(tzinfo=UTC)"` | — |
| [SRC-3AA6165B18-L000105](../../agents/research_guardrails.py#L105) | 105 | `"    published = _parse_publication_date(source.get(\"published_at\"), current)"` | — |
| [SRC-3AA6165B18-L000106](../../agents/research_guardrails.py#L106) | 106 | `"    if published is None:"` | — |
| [SRC-3AA6165B18-L000107](../../agents/research_guardrails.py#L107) | 107 | `"        return {\"eligible\": False, \"status\": \"date_unavailable\", \"age_days\": None}"` | — |
| [SRC-3AA6165B18-L000108](../../agents/research_guardrails.py#L108) | 108 | `"    if published > current + timedelta(days=1):"` | — |
| [SRC-3AA6165B18-L000109](../../agents/research_guardrails.py#L109) | 109 | `"        return {\"eligible\": False, \"status\": \"future_date\", \"age_days\": None}"` | — |
| [SRC-3AA6165B18-L000110](../../agents/research_guardrails.py#L110) | 110 | `"    age_days = max(0, (current - published).total_seconds() / 86400)"` | — |
| [SRC-3AA6165B18-L000111](../../agents/research_guardrails.py#L111) | 111 | `"    if age_days > max_age_days:"` | — |
| [SRC-3AA6165B18-L000112](../../agents/research_guardrails.py#L112) | 112 | `"        return {"` | — |
| [SRC-3AA6165B18-L000113](../../agents/research_guardrails.py#L113) | 113 | `"            \"eligible\": False,"` | — |
| [SRC-3AA6165B18-L000114](../../agents/research_guardrails.py#L114) | 114 | `"            \"status\": \"stale\","` | — |
| [SRC-3AA6165B18-L000115](../../agents/research_guardrails.py#L115) | 115 | `"            \"age_days\": round(age_days, 2),"` | — |
| [SRC-3AA6165B18-L000116](../../agents/research_guardrails.py#L116) | 116 | `"            \"max_age_days\": max_age_days,"` | — |
| [SRC-3AA6165B18-L000117](../../agents/research_guardrails.py#L117) | 117 | `"        }"` | — |
| [SRC-3AA6165B18-L000118](../../agents/research_guardrails.py#L118) | 118 | `"    if not bool(source.get(\"page_fetched\")) or not str(source.get(\"page_text\") or \"\").strip():"` | — |
| [SRC-3AA6165B18-L000119](../../agents/research_guardrails.py#L119) | 119 | `"        return {"` | — |
| [SRC-3AA6165B18-L000120](../../agents/research_guardrails.py#L120) | 120 | `"            \"eligible\": False,"` | — |
| [SRC-3AA6165B18-L000121](../../agents/research_guardrails.py#L121) | 121 | `"            \"status\": \"page_not_read\","` | — |
| [SRC-3AA6165B18-L000122](../../agents/research_guardrails.py#L122) | 122 | `"            \"age_days\": round(age_days, 2),"` | — |
| [SRC-3AA6165B18-L000123](../../agents/research_guardrails.py#L123) | 123 | `"            \"max_age_days\": max_age_days,"` | — |
| [SRC-3AA6165B18-L000124](../../agents/research_guardrails.py#L124) | 124 | `"        }"` | — |
| [SRC-3AA6165B18-L000125](../../agents/research_guardrails.py#L125) | 125 | `"    return {"` | — |
| [SRC-3AA6165B18-L000126](../../agents/research_guardrails.py#L126) | 126 | `"        \"eligible\": True,"` | — |
| [SRC-3AA6165B18-L000127](../../agents/research_guardrails.py#L127) | 127 | `"        \"status\": \"recent_page_read\","` | — |
| [SRC-3AA6165B18-L000128](../../agents/research_guardrails.py#L128) | 128 | `"        \"age_days\": round(age_days, 2),"` | — |
| [SRC-3AA6165B18-L000129](../../agents/research_guardrails.py#L129) | 129 | `"        \"max_age_days\": max_age_days,"` | — |
| [SRC-3AA6165B18-L000130](../../agents/research_guardrails.py#L130) | 130 | `"    }"` | — |
| [SRC-3AA6165B18-L000131](../../agents/research_guardrails.py#L131) | 131 | `""` | — |
| [SRC-3AA6165B18-L000132](../../agents/research_guardrails.py#L132) | 132 | `""` | — |
| [SRC-3AA6165B18-L000133](../../agents/research_guardrails.py#L133) | 133 | `"def classify_social_source(source: dict[str, Any]) -> dict[str, str]:"` | — |
| [SRC-3AA6165B18-L000134](../../agents/research_guardrails.py#L134) | 134 | `"    \"\"\"Apply a transparent, non-authoritative label to public social content.\"\"\""` | — |
| [SRC-3AA6165B18-L000135](../../agents/research_guardrails.py#L135) | 135 | `"    url = source.get(\"url\", \"\")"` | — |
| [SRC-3AA6165B18-L000136](../../agents/research_guardrails.py#L136) | 136 | `"    host = _host(url)"` | — |
| [SRC-3AA6165B18-L000137](../../agents/research_guardrails.py#L137) | 137 | `"    platform = next(("` | — |
| [SRC-3AA6165B18-L000138](../../agents/research_guardrails.py#L138) | 138 | `"        name for name, domain in SOCIAL_DOMAINS.items()"` | — |
| [SRC-3AA6165B18-L000139](../../agents/research_guardrails.py#L139) | 139 | `"        if host == domain or host.endswith(\".\" + domain)"` | — |
| [SRC-3AA6165B18-L000140](../../agents/research_guardrails.py#L140) | 140 | `"    ), \"\")"` | — |
| [SRC-3AA6165B18-L000141](../../agents/research_guardrails.py#L141) | 141 | `"    if not platform:"` | — |
| [SRC-3AA6165B18-L000142](../../agents/research_guardrails.py#L142) | 142 | `"        return {"` | — |
| [SRC-3AA6165B18-L000143](../../agents/research_guardrails.py#L143) | 143 | `"            \"opinion_source_classification\": \"not_a_social_post\","` | — |
| [SRC-3AA6165B18-L000144](../../agents/research_guardrails.py#L144) | 144 | `"            \"opinion_classification_basis\": \"URL host is not a recognized social platform\","` | — |
| [SRC-3AA6165B18-L000145](../../agents/research_guardrails.py#L145) | 145 | `"            \"opinion_classification_method\": \"heuristic_only\","` | — |
| [SRC-3AA6165B18-L000146](../../agents/research_guardrails.py#L146) | 146 | `"        }"` | — |
| [SRC-3AA6165B18-L000147](../../agents/research_guardrails.py#L147) | 147 | `""` | — |
| [SRC-3AA6165B18-L000148](../../agents/research_guardrails.py#L148) | 148 | `"    text = _normalized(\" \".join("` | — |
| [SRC-3AA6165B18-L000149](../../agents/research_guardrails.py#L149) | 149 | `"        str(source.get(field) or \"\")"` | — |
| [SRC-3AA6165B18-L000150](../../agents/research_guardrails.py#L150) | 150 | `"        for field in (\"title\", \"snippet\", \"page_text\")"` | — |
| [SRC-3AA6165B18-L000151](../../agents/research_guardrails.py#L151) | 151 | `"    ))"` | — |
| [SRC-3AA6165B18-L000152](../../agents/research_guardrails.py#L152) | 152 | `"    if any(term in text for term in _PROMOTION_TERMS):"` | — |
| [SRC-3AA6165B18-L000153](../../agents/research_guardrails.py#L153) | 153 | `"        label = \"promotional_or_commercial\""` | — |
| [SRC-3AA6165B18-L000154](../../agents/research_guardrails.py#L154) | 154 | `"        basis = \"commercial language detected\""` | — |
| [SRC-3AA6165B18-L000155](../../agents/research_guardrails.py#L155) | 155 | `"    elif any(term in text for term in _PERSONAL_EXPERIENCE_TERMS):"` | — |
| [SRC-3AA6165B18-L000156](../../agents/research_guardrails.py#L156) | 156 | `"        label = \"personal_experience_candidate\""` | — |
| [SRC-3AA6165B18-L000157](../../agents/research_guardrails.py#L157) | 157 | `"        basis = \"first-person experience language detected\""` | — |
| [SRC-3AA6165B18-L000158](../../agents/research_guardrails.py#L158) | 158 | `"    elif any(term in text for term in _DISCUSSION_TERMS):"` | — |
| [SRC-3AA6165B18-L000159](../../agents/research_guardrails.py#L159) | 159 | `"        label = \"discussion_or_question\""` | — |
| [SRC-3AA6165B18-L000160](../../agents/research_guardrails.py#L160) | 160 | `"        basis = \"question or discussion language detected\""` | — |
| [SRC-3AA6165B18-L000161](../../agents/research_guardrails.py#L161) | 161 | `"    else:"` | — |
| [SRC-3AA6165B18-L000162](../../agents/research_guardrails.py#L162) | 162 | `"        label = \"social_post_unclassified\""` | — |
| [SRC-3AA6165B18-L000163](../../agents/research_guardrails.py#L163) | 163 | `"        basis = \"no clear experience/discussion signal; manual review needed\""` | — |
| [SRC-3AA6165B18-L000164](../../agents/research_guardrails.py#L164) | 164 | `"    return {"` | — |
| [SRC-3AA6165B18-L000165](../../agents/research_guardrails.py#L165) | 165 | `"        \"opinion_source_classification\": label,"` | — |
| [SRC-3AA6165B18-L000166](../../agents/research_guardrails.py#L166) | 166 | `"        \"opinion_classification_basis\": basis,"` | — |
| [SRC-3AA6165B18-L000167](../../agents/research_guardrails.py#L167) | 167 | `"        \"opinion_classification_method\": \"heuristic_only\","` | — |
| [SRC-3AA6165B18-L000168](../../agents/research_guardrails.py#L168) | 168 | `"    }"` | — |
| [SRC-3AA6165B18-L000169](../../agents/research_guardrails.py#L169) | 169 | `""` | — |
| [SRC-3AA6165B18-L000170](../../agents/research_guardrails.py#L170) | 170 | `""` | — |
| [SRC-3AA6165B18-L000171](../../agents/research_guardrails.py#L171) | 171 | `"def apply_source_guardrails("` | — |
| [SRC-3AA6165B18-L000172](../../agents/research_guardrails.py#L172) | 172 | `"    question: str,"` | — |
| [SRC-3AA6165B18-L000173](../../agents/research_guardrails.py#L173) | 173 | `"    mode: str,"` | — |
| [SRC-3AA6165B18-L000174](../../agents/research_guardrails.py#L174) | 174 | `"    plan: dict[str, Any],"` | — |
| [SRC-3AA6165B18-L000175](../../agents/research_guardrails.py#L175) | 175 | `"    sources: list[dict[str, Any]],"` | — |
| [SRC-3AA6165B18-L000176](../../agents/research_guardrails.py#L176) | 176 | `"    *,"` | — |
| [SRC-3AA6165B18-L000177](../../agents/research_guardrails.py#L177) | 177 | `"    now: datetime \| None = None,"` | — |
| [SRC-3AA6165B18-L000178](../../agents/research_guardrails.py#L178) | 178 | `") -> tuple[list[dict[str, Any]], dict[str, Any]]:"` | — |
| [SRC-3AA6165B18-L000179](../../agents/research_guardrails.py#L179) | 179 | `"    \"\"\"Apply official-domain, current-evidence, and explicit social-mode guards."` | — |
| [SRC-3AA6165B18-L000180](../../agents/research_guardrails.py#L180) | 180 | `""` | — |
| [SRC-3AA6165B18-L000181](../../agents/research_guardrails.py#L181) | 181 | `"    Rejection counters describe this filter stage only. They are not search-engine"` | — |
| [SRC-3AA6165B18-L000182](../../agents/research_guardrails.py#L182) | 182 | `"    totals, and passing them is not a semantic fact check."` | — |
| [SRC-3AA6165B18-L000183](../../agents/research_guardrails.py#L183) | 183 | `"    \"\"\""` | — |
| [SRC-3AA6165B18-L000184](../../agents/research_guardrails.py#L184) | 184 | `"    clean_mode = str(mode or \"auto\").strip().lower()"` | — |
| [SRC-3AA6165B18-L000185](../../agents/research_guardrails.py#L185) | 185 | `"    official_required = requires_official_government_domain(question)"` | — |
| [SRC-3AA6165B18-L000186](../../agents/research_guardrails.py#L186) | 186 | `"    freshness_required = ("` | — |
| [SRC-3AA6165B18-L000187](../../agents/research_guardrails.py#L187) | 187 | `"        (clean_mode == \"latest\" or plan.get(\"freshness\") == \"current\")"` | — |
| [SRC-3AA6165B18-L000188](../../agents/research_guardrails.py#L188) | 188 | `"        and not _is_navigation_request(question)"` | — |
| [SRC-3AA6165B18-L000189](../../agents/research_guardrails.py#L189) | 189 | `"    )"` | — |
| [SRC-3AA6165B18-L000190](../../agents/research_guardrails.py#L190) | 190 | `"    social_required = clean_mode == \"social\""` | — |
| [SRC-3AA6165B18-L000191](../../agents/research_guardrails.py#L191) | 191 | `"    retained: list[dict[str, Any]] = []"` | — |
| [SRC-3AA6165B18-L000192](../../agents/research_guardrails.py#L192) | 192 | `"    rejected: dict[str, int] = {}"` | — |
| [SRC-3AA6165B18-L000193](../../agents/research_guardrails.py#L193) | 193 | `"    reasons: list[dict[str, str]] = []"` | — |
| [SRC-3AA6165B18-L000194](../../agents/research_guardrails.py#L194) | 194 | `""` | — |
| [SRC-3AA6165B18-L000195](../../agents/research_guardrails.py#L195) | 195 | `"    def reject(reason: str, source: dict[str, Any]) -> None:"` | — |
| [SRC-3AA6165B18-L000196](../../agents/research_guardrails.py#L196) | 196 | `"        rejected[reason] = rejected.get(reason, 0) + 1"` | — |
| [SRC-3AA6165B18-L000197](../../agents/research_guardrails.py#L197) | 197 | `"        reasons.append({"` | — |
| [SRC-3AA6165B18-L000198](../../agents/research_guardrails.py#L198) | 198 | `"            \"reason\": reason,"` | — |
| [SRC-3AA6165B18-L000199](../../agents/research_guardrails.py#L199) | 199 | `"            \"url\": str(source.get(\"url\") or \"\")[:2048],"` | — |
| [SRC-3AA6165B18-L000200](../../agents/research_guardrails.py#L200) | 200 | `"        })"` | — |
| [SRC-3AA6165B18-L000201](../../agents/research_guardrails.py#L201) | 201 | `""` | — |
| [SRC-3AA6165B18-L000202](../../agents/research_guardrails.py#L202) | 202 | `"    for candidate in sources if isinstance(sources, list) else []:"` | — |
| [SRC-3AA6165B18-L000203](../../agents/research_guardrails.py#L203) | 203 | `"        if not isinstance(candidate, dict):"` | — |
| [SRC-3AA6165B18-L000204](../../agents/research_guardrails.py#L204) | 204 | `"            rejected[\"malformed_candidate\"] = rejected.get(\"malformed_candidate\", 0) + 1"` | — |
| [SRC-3AA6165B18-L000205](../../agents/research_guardrails.py#L205) | 205 | `"            reasons.append({\"reason\": \"malformed_candidate\", \"url\": \"\"})"` | — |
| [SRC-3AA6165B18-L000206](../../agents/research_guardrails.py#L206) | 206 | `"            continue"` | — |
| [SRC-3AA6165B18-L000207](../../agents/research_guardrails.py#L207) | 207 | `"        source = dict(candidate)"` | — |
| [SRC-3AA6165B18-L000208](../../agents/research_guardrails.py#L208) | 208 | `"        if official_required and not _is_government_domain(source.get(\"url\")):"` | — |
| [SRC-3AA6165B18-L000209](../../agents/research_guardrails.py#L209) | 209 | `"            reject(\"not_an_official_government_domain\", source)"` | — |
| [SRC-3AA6165B18-L000210](../../agents/research_guardrails.py#L210) | 210 | `"            continue"` | — |
| [SRC-3AA6165B18-L000211](../../agents/research_guardrails.py#L211) | 211 | `"        if social_required and not is_social_platform_url(source.get(\"url\")):"` | — |
| [SRC-3AA6165B18-L000212](../../agents/research_guardrails.py#L212) | 212 | `"            reject(\"not_a_social_platform_source\", source)"` | — |
| [SRC-3AA6165B18-L000213](../../agents/research_guardrails.py#L213) | 213 | `"            continue"` | — |
| [SRC-3AA6165B18-L000214](../../agents/research_guardrails.py#L214) | 214 | `"        if freshness_required:"` | — |
| [SRC-3AA6165B18-L000215](../../agents/research_guardrails.py#L215) | 215 | `"            freshness = assess_current_source(source, now=now)"` | — |
| [SRC-3AA6165B18-L000216](../../agents/research_guardrails.py#L216) | 216 | `"            source[\"current_evidence_assessment\"] = freshness"` | — |
| [SRC-3AA6165B18-L000217](../../agents/research_guardrails.py#L217) | 217 | `"            if not freshness[\"eligible\"]:"` | — |
| [SRC-3AA6165B18-L000218](../../agents/research_guardrails.py#L218) | 218 | `"                reject(str(freshness[\"status\"]), source)"` | — |
| [SRC-3AA6165B18-L000219](../../agents/research_guardrails.py#L219) | 219 | `"                continue"` | — |
| [SRC-3AA6165B18-L000220](../../agents/research_guardrails.py#L220) | 220 | `"        if social_required or bool(plan.get(\"social_focus\")):"` | — |
| [SRC-3AA6165B18-L000221](../../agents/research_guardrails.py#L221) | 221 | `"            source.update(classify_social_source(source))"` | — |
| [SRC-3AA6165B18-L000222](../../agents/research_guardrails.py#L222) | 222 | `"        retained.append(source)"` | — |
| [SRC-3AA6165B18-L000223](../../agents/research_guardrails.py#L223) | 223 | `""` | — |
| [SRC-3AA6165B18-L000224](../../agents/research_guardrails.py#L224) | 224 | `"    status = \"passed\" if not rejected else \"filtered\""` | — |
| [SRC-3AA6165B18-L000225](../../agents/research_guardrails.py#L225) | 225 | `"    if freshness_required and retained:"` | — |
| [SRC-3AA6165B18-L000226](../../agents/research_guardrails.py#L226) | 226 | `"        current_status = \"eligible_recent_read_pages_only\""` | — |
| [SRC-3AA6165B18-L000227](../../agents/research_guardrails.py#L227) | 227 | `"    elif freshness_required:"` | — |
| [SRC-3AA6165B18-L000228](../../agents/research_guardrails.py#L228) | 228 | `"        current_status = \"no_current_eligible_evidence\""` | — |
| [SRC-3AA6165B18-L000229](../../agents/research_guardrails.py#L229) | 229 | `"    else:"` | — |
| [SRC-3AA6165B18-L000230](../../agents/research_guardrails.py#L230) | 230 | `"        current_status = \"not_required\""` | — |
| [SRC-3AA6165B18-L000231](../../agents/research_guardrails.py#L231) | 231 | `"    summary = {"` | — |
| [SRC-3AA6165B18-L000232](../../agents/research_guardrails.py#L232) | 232 | `"        \"status\": status,"` | — |
| [SRC-3AA6165B18-L000233](../../agents/research_guardrails.py#L233) | 233 | `"        \"input_sources\": len(sources) if isinstance(sources, list) else 0,"` | — |
| [SRC-3AA6165B18-L000234](../../agents/research_guardrails.py#L234) | 234 | `"        \"accepted_sources\": len(retained),"` | — |
| [SRC-3AA6165B18-L000235](../../agents/research_guardrails.py#L235) | 235 | `"        \"rejected_sources\": sum(rejected.values()),"` | — |
| [SRC-3AA6165B18-L000236](../../agents/research_guardrails.py#L236) | 236 | `"        \"rejection_counts\": rejected,"` | — |
| [SRC-3AA6165B18-L000237](../../agents/research_guardrails.py#L237) | 237 | `"        \"rejection_details\": reasons[:20],"` | — |
| [SRC-3AA6165B18-L000238](../../agents/research_guardrails.py#L238) | 238 | `"        \"official_government_domain_required\": official_required,"` | — |
| [SRC-3AA6165B18-L000239](../../agents/research_guardrails.py#L239) | 239 | `"        \"official_domain_policy\": ("` | — |
| [SRC-3AA6165B18-L000240](../../agents/research_guardrails.py#L240) | 240 | `"            \"government-domain candidate only; organization ownership is not independently verified\""` | — |
| [SRC-3AA6165B18-L000241](../../agents/research_guardrails.py#L241) | 241 | `"            if official_required else \"not_required\""` | — |
| [SRC-3AA6165B18-L000242](../../agents/research_guardrails.py#L242) | 242 | `"        ),"` | — |
| [SRC-3AA6165B18-L000243](../../agents/research_guardrails.py#L243) | 243 | `"        \"current_evidence_required\": freshness_required,"` | — |
| [SRC-3AA6165B18-L000244](../../agents/research_guardrails.py#L244) | 244 | `"        \"current_evidence_status\": current_status,"` | — |
| [SRC-3AA6165B18-L000245](../../agents/research_guardrails.py#L245) | 245 | `"        \"current_evidence_max_age_days\": _CURRENT_EVIDENCE_MAX_AGE_DAYS if freshness_required else None,"` | — |
| [SRC-3AA6165B18-L000246](../../agents/research_guardrails.py#L246) | 246 | `"        \"social_platform_only\": social_required,"` | — |
| [SRC-3AA6165B18-L000247](../../agents/research_guardrails.py#L247) | 247 | `"        \"interpretation\": \"retrieval guardrail only; passing is not proof of claim correctness\","` | — |
| [SRC-3AA6165B18-L000248](../../agents/research_guardrails.py#L248) | 248 | `"    }"` | — |
| [SRC-3AA6165B18-L000249](../../agents/research_guardrails.py#L249) | 249 | `"    return retained, summary"` | — |
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
| [SRC-6E58A660BC-L000014](../../agents/search_connectors.py#L14) | 14 | `"DEFAULT_TIMEOUT_SECONDS = 5"` | — |
| [SRC-6E58A660BC-L000015](../../agents/search_connectors.py#L15) | 15 | `"USER_AGENT = \"OmaraiResearchBot/1.0 (mailto:ops@example.com)\""` | — |
| [SRC-6E58A660BC-L000016](../../agents/search_connectors.py#L16) | 16 | `"ConnectorFn = Callable[[str, int], list[dict[str, Any]]]"` | — |
| [SRC-6E58A660BC-L000017](../../agents/search_connectors.py#L17) | 17 | `""` | — |
| [SRC-6E58A660BC-L000018](../../agents/search_connectors.py#L18) | 18 | `""` | — |
| [SRC-6E58A660BC-L000019](../../agents/search_connectors.py#L19) | 19 | `"def _clean_text(value: Any, limit: int = 1600) -> str:"` | — |
| [SRC-6E58A660BC-L000020](../../agents/search_connectors.py#L20) | 20 | `"    if not isinstance(value, str):"` | — |
| [SRC-6E58A660BC-L000021](../../agents/search_connectors.py#L21) | 21 | `"        return \"\""` | — |
| [SRC-6E58A660BC-L000022](../../agents/search_connectors.py#L22) | 22 | `"    return re.sub(r\"\\s+\", \" \", value).strip()[:limit]"` | — |
| [SRC-6E58A660BC-L000023](../../agents/search_connectors.py#L23) | 23 | `""` | — |
| [SRC-6E58A660BC-L000024](../../agents/search_connectors.py#L24) | 24 | `""` | — |
| [SRC-6E58A660BC-L000025](../../agents/search_connectors.py#L25) | 25 | `"def _http_get_json(url: str, headers: dict[str, str] \| None = None, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> Any:"` | — |
| [SRC-6E58A660BC-L000026](../../agents/search_connectors.py#L26) | 26 | `"    req_headers = {\"User-Agent\": USER_AGENT, \"Accept\": \"application/json\"}"` | — |
| [SRC-6E58A660BC-L000027](../../agents/search_connectors.py#L27) | 27 | `"    if headers:"` | — |
| [SRC-6E58A660BC-L000028](../../agents/search_connectors.py#L28) | 28 | `"        req_headers.update(headers)"` | — |
| [SRC-6E58A660BC-L000029](../../agents/search_connectors.py#L29) | 29 | `"    request = urllib.request.Request(url, headers=req_headers, method=\"GET\")"` | — |
| [SRC-6E58A660BC-L000030](../../agents/search_connectors.py#L30) | 30 | `"    with urllib.request.urlopen(request, timeout=timeout) as response:"` | — |
| [SRC-6E58A660BC-L000031](../../agents/search_connectors.py#L31) | 31 | `"        return json.loads(response.read().decode(\"utf-8\", errors=\"replace\"))"` | — |
| [SRC-6E58A660BC-L000032](../../agents/search_connectors.py#L32) | 32 | `""` | — |
| [SRC-6E58A660BC-L000033](../../agents/search_connectors.py#L33) | 33 | `""` | — |
| [SRC-6E58A660BC-L000034](../../agents/search_connectors.py#L34) | 34 | `"def _http_get_text(url: str, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> str:"` | — |
| [SRC-6E58A660BC-L000035](../../agents/search_connectors.py#L35) | 35 | `"    request = urllib.request.Request(url, headers={\"User-Agent\": USER_AGENT}, method=\"GET\")"` | — |
| [SRC-6E58A660BC-L000036](../../agents/search_connectors.py#L36) | 36 | `"    with urllib.request.urlopen(request, timeout=timeout) as response:"` | — |
| [SRC-6E58A660BC-L000037](../../agents/search_connectors.py#L37) | 37 | `"        return response.read().decode(\"utf-8\", errors=\"replace\")"` | — |
| [SRC-6E58A660BC-L000038](../../agents/search_connectors.py#L38) | 38 | `""` | — |
| [SRC-6E58A660BC-L000039](../../agents/search_connectors.py#L39) | 39 | `""` | — |
| [SRC-6E58A660BC-L000040](../../agents/search_connectors.py#L40) | 40 | `"def _result(*, title: str, url: str, snippet: str, provider: str, rank: int, query: str, published_at: str = \"\", source_class: str = \"web\") -> dict[str, Any]:"` | — |
| [SRC-6E58A660BC-L000041](../../agents/search_connectors.py#L41) | 41 | `"    return {"` | — |
| [SRC-6E58A660BC-L000042](../../agents/search_connectors.py#L42) | 42 | `"        \"title\": _clean_text(title, 300),"` | — |
| [SRC-6E58A660BC-L000043](../../agents/search_connectors.py#L43) | 43 | `"        \"url\": (url or \"\").strip(),"` | — |
| [SRC-6E58A660BC-L000044](../../agents/search_connectors.py#L44) | 44 | `"        \"snippet\": _clean_text(snippet, 1600),"` | — |
| [SRC-6E58A660BC-L000045](../../agents/search_connectors.py#L45) | 45 | `"        \"page_fetched\": False,"` | — |
| [SRC-6E58A660BC-L000046](../../agents/search_connectors.py#L46) | 46 | `"        \"provider\": provider,"` | — |
| [SRC-6E58A660BC-L000047](../../agents/search_connectors.py#L47) | 47 | `"        \"provider_rank\": rank,"` | — |
| [SRC-6E58A660BC-L000048](../../agents/search_connectors.py#L48) | 48 | `"        \"search_query\": query,"` | — |
| [SRC-6E58A660BC-L000049](../../agents/search_connectors.py#L49) | 49 | `"        \"published_at\": published_at or \"\","` | — |
| [SRC-6E58A660BC-L000050](../../agents/search_connectors.py#L50) | 50 | `"        \"source_class\": source_class,"` | — |
| [SRC-6E58A660BC-L000051](../../agents/search_connectors.py#L51) | 51 | `"    }"` | — |
| [SRC-6E58A660BC-L000052](../../agents/search_connectors.py#L52) | 52 | `""` | — |
| [SRC-6E58A660BC-L000053](../../agents/search_connectors.py#L53) | 53 | `""` | — |
| [SRC-6E58A660BC-L000054](../../agents/search_connectors.py#L54) | 54 | `"def search_openalex(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000055](../../agents/search_connectors.py#L55) | 55 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000056](../../agents/search_connectors.py#L56) | 56 | `"        return []"` | — |
| [SRC-6E58A660BC-L000057](../../agents/search_connectors.py#L57) | 57 | `"    params = urllib.parse.urlencode({\"search\": query.strip()[:240], \"per_page\": max(1, min(int(limit), MAX_CONNECTOR_RESULTS)), \"mailto\": os.getenv(\"OPENALEX_MAILTO\", \"ops@example.com\")})"` | — |
| [SRC-6E58A660BC-L000058](../../agents/search_connectors.py#L58) | 58 | `"    data = _http_get_json(f\"https://api.openalex.org/works?{params}\")"` | — |
| [SRC-6E58A660BC-L000059](../../agents/search_connectors.py#L59) | 59 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000060](../../agents/search_connectors.py#L60) | 60 | `"    for item in data.get(\"results\", [])[:limit]:"` | — |
| [SRC-6E58A660BC-L000061](../../agents/search_connectors.py#L61) | 61 | `"        if not isinstance(item, dict):"` | — |
| [SRC-6E58A660BC-L000062](../../agents/search_connectors.py#L62) | 62 | `"            continue"` | — |
| [SRC-6E58A660BC-L000063](../../agents/search_connectors.py#L63) | 63 | `"        title = item.get(\"display_name\") or \"\""` | — |
| [SRC-6E58A660BC-L000064](../../agents/search_connectors.py#L64) | 64 | `"        url = \"\""` | — |
| [SRC-6E58A660BC-L000065](../../agents/search_connectors.py#L65) | 65 | `"        primary = item.get(\"primary_location\") or {}"` | — |
| [SRC-6E58A660BC-L000066](../../agents/search_connectors.py#L66) | 66 | `"        if isinstance(primary, dict) and primary.get(\"landing_page_url\"):"` | — |
| [SRC-6E58A660BC-L000067](../../agents/search_connectors.py#L67) | 67 | `"            url = str(primary.get(\"landing_page_url\"))"` | — |
| [SRC-6E58A660BC-L000068](../../agents/search_connectors.py#L68) | 68 | `"        elif item.get(\"id\"):"` | — |
| [SRC-6E58A660BC-L000069](../../agents/search_connectors.py#L69) | 69 | `"            url = str(item.get(\"id\"))"` | — |
| [SRC-6E58A660BC-L000070](../../agents/search_connectors.py#L70) | 70 | `"        concepts = \", \".join(str(c.get(\"display_name\", \"\")) for c in (item.get(\"concepts\") or [])[:5] if isinstance(c, dict))"` | — |
| [SRC-6E58A660BC-L000071](../../agents/search_connectors.py#L71) | 71 | `"        snippet = f\"{title}. {concepts}\".strip(\". \")"` | — |
| [SRC-6E58A660BC-L000072](../../agents/search_connectors.py#L72) | 72 | `"        if title and url:"` | — |
| [SRC-6E58A660BC-L000073](../../agents/search_connectors.py#L73) | 73 | `"            rows.append(_result(title=title, url=url, snippet=snippet or title, provider=\"openalex\", rank=len(rows) + 1, query=query, published_at=str(item.get(\"publication_date\") or \"\"), source_class=\"academic\"))"` | — |
| [SRC-6E58A660BC-L000074](../../agents/search_connectors.py#L74) | 74 | `"    return rows"` | — |
| [SRC-6E58A660BC-L000075](../../agents/search_connectors.py#L75) | 75 | `""` | — |
| [SRC-6E58A660BC-L000076](../../agents/search_connectors.py#L76) | 76 | `""` | — |
| [SRC-6E58A660BC-L000077](../../agents/search_connectors.py#L77) | 77 | `"def search_arxiv(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000078](../../agents/search_connectors.py#L78) | 78 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000079](../../agents/search_connectors.py#L79) | 79 | `"        return []"` | — |
| [SRC-6E58A660BC-L000080](../../agents/search_connectors.py#L80) | 80 | `"    params = urllib.parse.urlencode({\"search_query\": f\"all:{query.strip()[:200]}\", \"start\": 0, \"max_results\": max(1, min(int(limit), MAX_CONNECTOR_RESULTS))})"` | — |
| [SRC-6E58A660BC-L000081](../../agents/search_connectors.py#L81) | 81 | `"    xml_text = _http_get_text(f\"https://export.arxiv.org/api/query?{params}\")"` | — |
| [SRC-6E58A660BC-L000082](../../agents/search_connectors.py#L82) | 82 | `"    entries = re.findall(r\"<entry>(.*?)</entry>\", xml_text, flags=re.DOTALL)"` | — |
| [SRC-6E58A660BC-L000083](../../agents/search_connectors.py#L83) | 83 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000084](../../agents/search_connectors.py#L84) | 84 | `"    for entry in entries[:limit]:"` | — |
| [SRC-6E58A660BC-L000085](../../agents/search_connectors.py#L85) | 85 | `"        title_m = re.search(r\"<title>(.*?)</title>\", entry, re.DOTALL)"` | — |
| [SRC-6E58A660BC-L000086](../../agents/search_connectors.py#L86) | 86 | `"        link_m = re.search(r\"<id>(https?://arxiv\\.org/abs/[^<]+)</id>\", entry)"` | — |
| [SRC-6E58A660BC-L000087](../../agents/search_connectors.py#L87) | 87 | `"        summary_m = re.search(r\"<summary>(.*?)</summary>\", entry, re.DOTALL)"` | — |
| [SRC-6E58A660BC-L000088](../../agents/search_connectors.py#L88) | 88 | `"        published_m = re.search(r\"<published>([^<]+)</published>\", entry)"` | — |
| [SRC-6E58A660BC-L000089](../../agents/search_connectors.py#L89) | 89 | `"        title = _clean_text(title_m.group(1) if title_m else \"\")"` | — |
| [SRC-6E58A660BC-L000090](../../agents/search_connectors.py#L90) | 90 | `"        link = link_m.group(1) if link_m else \"\""` | — |
| [SRC-6E58A660BC-L000091](../../agents/search_connectors.py#L91) | 91 | `"        summary = _clean_text(summary_m.group(1) if summary_m else \"\", 1600)"` | — |
| [SRC-6E58A660BC-L000092](../../agents/search_connectors.py#L92) | 92 | `"        published = published_m.group(1) if published_m else \"\""` | — |
| [SRC-6E58A660BC-L000093](../../agents/search_connectors.py#L93) | 93 | `"        if title and link:"` | — |
| [SRC-6E58A660BC-L000094](../../agents/search_connectors.py#L94) | 94 | `"            rows.append(_result(title=title, url=link, snippet=summary or title, provider=\"arxiv\", rank=len(rows) + 1, query=query, published_at=published, source_class=\"academic\"))"` | — |
| [SRC-6E58A660BC-L000095](../../agents/search_connectors.py#L95) | 95 | `"    return rows"` | — |
| [SRC-6E58A660BC-L000096](../../agents/search_connectors.py#L96) | 96 | `""` | — |
| [SRC-6E58A660BC-L000097](../../agents/search_connectors.py#L97) | 97 | `""` | — |
| [SRC-6E58A660BC-L000098](../../agents/search_connectors.py#L98) | 98 | `"def search_crossref(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000099](../../agents/search_connectors.py#L99) | 99 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000100](../../agents/search_connectors.py#L100) | 100 | `"        return []"` | — |
| [SRC-6E58A660BC-L000101](../../agents/search_connectors.py#L101) | 101 | `"    params = urllib.parse.urlencode({\"query\": query.strip()[:240], \"rows\": max(1, min(int(limit), MAX_CONNECTOR_RESULTS)), \"mailto\": os.getenv(\"CROSSREF_MAILTO\", \"ops@example.com\")})"` | — |
| [SRC-6E58A660BC-L000102](../../agents/search_connectors.py#L102) | 102 | `"    data = _http_get_json(f\"https://api.crossref.org/works?{params}\", headers={\"User-Agent\": USER_AGENT})"` | — |
| [SRC-6E58A660BC-L000103](../../agents/search_connectors.py#L103) | 103 | `"    items = ((data.get(\"message\") or {}).get(\"items\") or [])[:limit]"` | — |
| [SRC-6E58A660BC-L000104](../../agents/search_connectors.py#L104) | 104 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000105](../../agents/search_connectors.py#L105) | 105 | `"    for item in items:"` | — |
| [SRC-6E58A660BC-L000106](../../agents/search_connectors.py#L106) | 106 | `"        if not isinstance(item, dict):"` | — |
| [SRC-6E58A660BC-L000107](../../agents/search_connectors.py#L107) | 107 | `"            continue"` | — |
| [SRC-6E58A660BC-L000108](../../agents/search_connectors.py#L108) | 108 | `"        title_list = item.get(\"title\") or []"` | — |
| [SRC-6E58A660BC-L000109](../../agents/search_connectors.py#L109) | 109 | `"        title = title_list[0] if isinstance(title_list, list) and title_list else \"\""` | — |
| [SRC-6E58A660BC-L000110](../../agents/search_connectors.py#L110) | 110 | `"        url = str(item.get(\"URL\") or \"\")"` | — |
| [SRC-6E58A660BC-L000111](../../agents/search_connectors.py#L111) | 111 | `"        container_list = item.get(\"container-title\") or []"` | — |
| [SRC-6E58A660BC-L000112](../../agents/search_connectors.py#L112) | 112 | `"        container = container_list[0] if isinstance(container_list, list) and container_list else \"\""` | — |
| [SRC-6E58A660BC-L000113](../../agents/search_connectors.py#L113) | 113 | `"        year = \"\""` | — |
| [SRC-6E58A660BC-L000114](../../agents/search_connectors.py#L114) | 114 | `"        issued = item.get(\"issued\") or {}"` | — |
| [SRC-6E58A660BC-L000115](../../agents/search_connectors.py#L115) | 115 | `"        if isinstance(issued, dict) and issued.get(\"date-parts\"):"` | — |
| [SRC-6E58A660BC-L000116](../../agents/search_connectors.py#L116) | 116 | `"            try:"` | — |
| [SRC-6E58A660BC-L000117](../../agents/search_connectors.py#L117) | 117 | `"                year = str(issued[\"date-parts\"][0][0])"` | — |
| [SRC-6E58A660BC-L000118](../../agents/search_connectors.py#L118) | 118 | `"            except (IndexError, TypeError, KeyError):"` | — |
| [SRC-6E58A660BC-L000119](../../agents/search_connectors.py#L119) | 119 | `"                year = \"\""` | — |
| [SRC-6E58A660BC-L000120](../../agents/search_connectors.py#L120) | 120 | `"        snippet = _clean_text(f\"{title}. {container} {year}\".strip())"` | — |
| [SRC-6E58A660BC-L000121](../../agents/search_connectors.py#L121) | 121 | `"        if title and url:"` | — |
| [SRC-6E58A660BC-L000122](../../agents/search_connectors.py#L122) | 122 | `"            rows.append(_result(title=title, url=url, snippet=snippet, provider=\"crossref\", rank=len(rows) + 1, query=query, published_at=year, source_class=\"academic\"))"` | — |
| [SRC-6E58A660BC-L000123](../../agents/search_connectors.py#L123) | 123 | `"    return rows"` | — |
| [SRC-6E58A660BC-L000124](../../agents/search_connectors.py#L124) | 124 | `""` | — |
| [SRC-6E58A660BC-L000125](../../agents/search_connectors.py#L125) | 125 | `""` | — |
| [SRC-6E58A660BC-L000126](../../agents/search_connectors.py#L126) | 126 | `"def search_semantic_scholar(query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000127](../../agents/search_connectors.py#L127) | 127 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000128](../../agents/search_connectors.py#L128) | 128 | `"        return []"` | — |
| [SRC-6E58A660BC-L000129](../../agents/search_connectors.py#L129) | 129 | `"    key = os.getenv(\"SEMANTIC_SCHOLAR_API_KEY\", \"\").strip()"` | — |
| [SRC-6E58A660BC-L000130](../../agents/search_connectors.py#L130) | 130 | `"    params = urllib.parse.urlencode({\"query\": query.strip()[:240], \"limit\": max(1, min(int(limit), MAX_CONNECTOR_RESULTS)), \"fields\": \"title,url,abstract,year,externalIds\"})"` | — |
| [SRC-6E58A660BC-L000131](../../agents/search_connectors.py#L131) | 131 | `"    headers = {\"User-Agent\": USER_AGENT}"` | — |
| [SRC-6E58A660BC-L000132](../../agents/search_connectors.py#L132) | 132 | `"    if key:"` | — |
| [SRC-6E58A660BC-L000133](../../agents/search_connectors.py#L133) | 133 | `"        headers[\"x-api-key\"] = key"` | — |
| [SRC-6E58A660BC-L000134](../../agents/search_connectors.py#L134) | 134 | `"    data = _http_get_json(f\"https://api.semanticscholar.org/graph/v1/paper/search?{params}\", headers=headers)"` | — |
| [SRC-6E58A660BC-L000135](../../agents/search_connectors.py#L135) | 135 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000136](../../agents/search_connectors.py#L136) | 136 | `"    for item in (data.get(\"data\") or [])[:limit]:"` | — |
| [SRC-6E58A660BC-L000137](../../agents/search_connectors.py#L137) | 137 | `"        if not isinstance(item, dict):"` | — |
| [SRC-6E58A660BC-L000138](../../agents/search_connectors.py#L138) | 138 | `"            continue"` | — |
| [SRC-6E58A660BC-L000139](../../agents/search_connectors.py#L139) | 139 | `"        title = item.get(\"title\") or \"\""` | — |
| [SRC-6E58A660BC-L000140](../../agents/search_connectors.py#L140) | 140 | `"        url = item.get(\"url\") or \"\""` | — |
| [SRC-6E58A660BC-L000141](../../agents/search_connectors.py#L141) | 141 | `"        if not url and isinstance(item.get(\"externalIds\"), dict):"` | — |
| [SRC-6E58A660BC-L000142](../../agents/search_connectors.py#L142) | 142 | `"            doi = item[\"externalIds\"].get(\"DOI\")"` | — |
| [SRC-6E58A660BC-L000143](../../agents/search_connectors.py#L143) | 143 | `"            if doi:"` | — |
| [SRC-6E58A660BC-L000144](../../agents/search_connectors.py#L144) | 144 | `"                url = f\"https://doi.org/{doi}\""` | — |
| [SRC-6E58A660BC-L000145](../../agents/search_connectors.py#L145) | 145 | `"        snippet = item.get(\"abstract\") or title"` | — |
| [SRC-6E58A660BC-L000146](../../agents/search_connectors.py#L146) | 146 | `"        year = str(item.get(\"year\") or \"\")"` | — |
| [SRC-6E58A660BC-L000147](../../agents/search_connectors.py#L147) | 147 | `"        if title and url:"` | — |
| [SRC-6E58A660BC-L000148](../../agents/search_connectors.py#L148) | 148 | `"            rows.append(_result(title=title, url=url, snippet=snippet, provider=\"semantic_scholar\", rank=len(rows) + 1, query=query, published_at=year, source_class=\"academic\"))"` | — |
| [SRC-6E58A660BC-L000149](../../agents/search_connectors.py#L149) | 149 | `"    return rows"` | — |
| [SRC-6E58A660BC-L000150](../../agents/search_connectors.py#L150) | 150 | `""` | — |
| [SRC-6E58A660BC-L000151](../../agents/search_connectors.py#L151) | 151 | `""` | — |
| [SRC-6E58A660BC-L000152](../../agents/search_connectors.py#L152) | 152 | `"CONNECTOR_REGISTRY: dict[str, dict[str, Any]] = {"` | — |
| [SRC-6E58A660BC-L000153](../../agents/search_connectors.py#L153) | 153 | `"    \"openalex\": {\"fn\": search_openalex, \"source_class\": \"academic\", \"requires_key\": False},"` | — |
| [SRC-6E58A660BC-L000154](../../agents/search_connectors.py#L154) | 154 | `"    \"arxiv\": {\"fn\": search_arxiv, \"source_class\": \"academic\", \"requires_key\": False},"` | — |
| [SRC-6E58A660BC-L000155](../../agents/search_connectors.py#L155) | 155 | `"    \"crossref\": {\"fn\": search_crossref, \"source_class\": \"academic\", \"requires_key\": False},"` | — |
| [SRC-6E58A660BC-L000156](../../agents/search_connectors.py#L156) | 156 | `"    \"semantic_scholar\": {\"fn\": search_semantic_scholar, \"source_class\": \"academic\", \"requires_key\": False},"` | — |
| [SRC-6E58A660BC-L000157](../../agents/search_connectors.py#L157) | 157 | `"}"` | — |
| [SRC-6E58A660BC-L000158](../../agents/search_connectors.py#L158) | 158 | `""` | — |
| [SRC-6E58A660BC-L000159](../../agents/search_connectors.py#L159) | 159 | `""` | — |
| [SRC-6E58A660BC-L000160](../../agents/search_connectors.py#L160) | 160 | `"def run_connector(name: str, query: str, limit: int = MAX_CONNECTOR_RESULTS) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000161](../../agents/search_connectors.py#L161) | 161 | `"    meta = CONNECTOR_REGISTRY.get(name)"` | — |
| [SRC-6E58A660BC-L000162](../../agents/search_connectors.py#L162) | 162 | `"    if not meta or meta.get(\"fn\") is None:"` | — |
| [SRC-6E58A660BC-L000163](../../agents/search_connectors.py#L163) | 163 | `"        return []"` | — |
| [SRC-6E58A660BC-L000164](../../agents/search_connectors.py#L164) | 164 | `"    if not isinstance(query, str) or not query.strip():"` | — |
| [SRC-6E58A660BC-L000165](../../agents/search_connectors.py#L165) | 165 | `"        return []"` | — |
| [SRC-6E58A660BC-L000166](../../agents/search_connectors.py#L166) | 166 | `"    try:"` | — |
| [SRC-6E58A660BC-L000167](../../agents/search_connectors.py#L167) | 167 | `"        rows = meta[\"fn\"](query, limit=limit) or []"` | — |
| [SRC-6E58A660BC-L000168](../../agents/search_connectors.py#L168) | 168 | `"        return [row for row in rows if isinstance(row, dict) and row.get(\"url\") and row.get(\"title\")]"` | — |
| [SRC-6E58A660BC-L000169](../../agents/search_connectors.py#L169) | 169 | `"    except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError, ValueError, KeyError, TypeError, json.JSONDecodeError, OSError):"` | — |
| [SRC-6E58A660BC-L000170](../../agents/search_connectors.py#L170) | 170 | `"        return []"` | — |
| [SRC-6E58A660BC-L000171](../../agents/search_connectors.py#L171) | 171 | `""` | — |
| [SRC-6E58A660BC-L000172](../../agents/search_connectors.py#L172) | 172 | `""` | — |
| [SRC-6E58A660BC-L000173](../../agents/search_connectors.py#L173) | 173 | `"def run_free_academic_connectors(query: str, limit_per: int = 4) -> list[dict[str, Any]]:"` | — |
| [SRC-6E58A660BC-L000174](../../agents/search_connectors.py#L174) | 174 | `"    combined: list[dict[str, Any]] = []"` | — |
| [SRC-6E58A660BC-L000175](../../agents/search_connectors.py#L175) | 175 | `"    for name in (\"openalex\", \"arxiv\", \"crossref\"):"` | — |
| [SRC-6E58A660BC-L000176](../../agents/search_connectors.py#L176) | 176 | `"        combined.extend(run_connector(name, query, limit=limit_per))"` | — |
| [SRC-6E58A660BC-L000177](../../agents/search_connectors.py#L177) | 177 | `"    return combined"` | — |
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
| [SRC-1AE03B9EC3-L000024](../../agents/web_agent.py#L24) | 24 | `"from agents.intent_router import resolve_followup_query, route_intent"` | — |
| [SRC-1AE03B9EC3-L000025](../../agents/web_agent.py#L25) | 25 | `"from agents.dialogue_state import ("` | — |
| [SRC-1AE03B9EC3-L000026](../../agents/web_agent.py#L26) | 26 | `"    fallback_dialogue_context,"` | — |
| [SRC-1AE03B9EC3-L000027](../../agents/web_agent.py#L27) | 27 | `"    might_be_context_dependent,"` | — |
| [SRC-1AE03B9EC3-L000028](../../agents/web_agent.py#L28) | 28 | `"    validate_dialogue_context,"` | — |
| [SRC-1AE03B9EC3-L000029](../../agents/web_agent.py#L29) | 29 | `")"` | — |
| [SRC-1AE03B9EC3-L000030](../../agents/web_agent.py#L30) | 30 | `"from agents.answer_validation import audit_answer_integrity"` | — |
| [SRC-1AE03B9EC3-L000031](../../agents/web_agent.py#L31) | 31 | `"from agents.claim_evidence import build_claim_evidence_ledger"` | — |
| [SRC-1AE03B9EC3-L000032](../../agents/web_agent.py#L32) | 32 | `"from agents.request_budget import RequestBudget, RequestBudgetExceeded"` | — |
| [SRC-1AE03B9EC3-L000033](../../agents/web_agent.py#L33) | 33 | `"from agents.aspect_planning import ("` | — |
| [SRC-1AE03B9EC3-L000034](../../agents/web_agent.py#L34) | 34 | `"    arabic_aspect_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L000035](../../agents/web_agent.py#L35) | 35 | `"    build_evidence_ledger,"` | — |
| [SRC-1AE03B9EC3-L000036](../../agents/web_agent.py#L36) | 36 | `"    extract_aspects,"` | — |
| [SRC-1AE03B9EC3-L000037](../../agents/web_agent.py#L37) | 37 | `"    repair_queries_for_missing_aspects,"` | — |
| [SRC-1AE03B9EC3-L000038](../../agents/web_agent.py#L38) | 38 | `")"` | — |
| [SRC-1AE03B9EC3-L000039](../../agents/web_agent.py#L39) | 39 | `"from agents.search_connectors import search_arxiv, search_crossref, search_openalex"` | — |
| [SRC-1AE03B9EC3-L000040](../../agents/web_agent.py#L40) | 40 | `"from agents.research import ("` | — |
| [SRC-1AE03B9EC3-L000041](../../agents/web_agent.py#L41) | 41 | `"    MAX_PLAN_QUERIES,"` | — |
| [SRC-1AE03B9EC3-L000042](../../agents/web_agent.py#L42) | 42 | `"    SOCIAL_DOMAINS,"` | — |
| [SRC-1AE03B9EC3-L000043](../../agents/web_agent.py#L43) | 43 | `"    compact_search_query,"` | — |
| [SRC-1AE03B9EC3-L000044](../../agents/web_agent.py#L44) | 44 | `"    evidence_signal_report,"` | — |
| [SRC-1AE03B9EC3-L000045](../../agents/web_agent.py#L45) | 45 | `"    fallback_plan,"` | — |
| [SRC-1AE03B9EC3-L000046](../../agents/web_agent.py#L46) | 46 | `"    fuse_ranked_results,"` | — |
| [SRC-1AE03B9EC3-L000047](../../agents/web_agent.py#L47) | 47 | `"    registrable_domain,"` | — |
| [SRC-1AE03B9EC3-L000048](../../agents/web_agent.py#L48) | 48 | `"    validate_plan,"` | — |
| [SRC-1AE03B9EC3-L000049](../../agents/web_agent.py#L49) | 49 | `")"` | — |
| [SRC-1AE03B9EC3-L000050](../../agents/web_agent.py#L50) | 50 | `""` | — |
| [SRC-1AE03B9EC3-L000051](../../agents/web_agent.py#L51) | 51 | `"MAX_QUESTION_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000052](../../agents/web_agent.py#L52) | 52 | `"MAX_HISTORY_ITEMS = 8"` | — |
| [SRC-1AE03B9EC3-L000053](../../agents/web_agent.py#L53) | 53 | `"MAX_HISTORY_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000054](../../agents/web_agent.py#L54) | 54 | `"MAX_SEARCH_RESULTS = 18"` | — |
| [SRC-1AE03B9EC3-L000055](../../agents/web_agent.py#L55) | 55 | `"MAX_PROVIDER_RESULTS = 6"` | — |
| [SRC-1AE03B9EC3-L000056](../../agents/web_agent.py#L56) | 56 | `"MAX_FETCHED_PAGES = 8"` | — |
| [SRC-1AE03B9EC3-L000057](../../agents/web_agent.py#L57) | 57 | `"MAX_LLM_CITED_SOURCES = 12"` | — |
| [SRC-1AE03B9EC3-L000058](../../agents/web_agent.py#L58) | 58 | `"MAX_RESEARCH_WORKERS = 8"` | — |
| [SRC-1AE03B9EC3-L000059](../../agents/web_agent.py#L59) | 59 | `"MAX_PAGE_BYTES = 1_000_000"` | — |
| [SRC-1AE03B9EC3-L000060](../../agents/web_agent.py#L60) | 60 | `"MAX_PAGE_TEXT_CHARS = 12_000"` | — |
| [SRC-1AE03B9EC3-L000061](../../agents/web_agent.py#L61) | 61 | `"LLM_TIMEOUT_SECONDS = 35"` | — |
| [SRC-1AE03B9EC3-L000062](../../agents/web_agent.py#L62) | 62 | `""` | — |
| [SRC-1AE03B9EC3-L000063](../../agents/web_agent.py#L63) | 63 | `"# Only completed connector result-processing states positively confirm an attempt."` | — |
| [SRC-1AE03B9EC3-L000064](../../agents/web_agent.py#L64) | 64 | `"# A generic \"failed\" or timeout diagnostic may occur before a network request is sent."` | — |
| [SRC-1AE03B9EC3-L000065](../../agents/web_agent.py#L65) | 65 | `"_SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES = frozenset({\"ok\", \"no_results\", \"filtered_all\"})"` | — |
| [SRC-1AE03B9EC3-L000066](../../agents/web_agent.py#L66) | 66 | `"_RESEARCH_ERROR_OUTCOMES = frozenset({\"attempted_research_error\", \"unknown_after_research_error\"})"` | — |
| [SRC-1AE03B9EC3-L000067](../../agents/web_agent.py#L67) | 67 | `"_PROVIDER_REJECTION_REASONS = ("` | — |
| [SRC-1AE03B9EC3-L000068](../../agents/web_agent.py#L68) | 68 | `"    \"malformed_candidate\","` | — |
| [SRC-1AE03B9EC3-L000069](../../agents/web_agent.py#L69) | 69 | `"    \"invalid_url_or_unsafe_target\","` | — |
| [SRC-1AE03B9EC3-L000070](../../agents/web_agent.py#L70) | 70 | `"    \"blocked_domain\","` | — |
| [SRC-1AE03B9EC3-L000071](../../agents/web_agent.py#L71) | 71 | `"    \"relevance_below_threshold\","` | — |
| [SRC-1AE03B9EC3-L000072](../../agents/web_agent.py#L72) | 72 | `")"` | — |
| [SRC-1AE03B9EC3-L000073](../../agents/web_agent.py#L73) | 73 | `""` | — |
| [SRC-1AE03B9EC3-L000074](../../agents/web_agent.py#L74) | 74 | `""` | — |
| [SRC-1AE03B9EC3-L000075](../../agents/web_agent.py#L75) | 75 | `"_ARABIC_SEARCH_TRANSLATION = str.maketrans({"` | — |
| [SRC-1AE03B9EC3-L000076](../../agents/web_agent.py#L76) | 76 | `"    \"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ٱ\": \"ا\", \"ى\": \"ي\","` | — |
| [SRC-1AE03B9EC3-L000077](../../agents/web_agent.py#L77) | 77 | `"    \"ؤ\": \"و\", \"ئ\": \"ي\", \"ة\": \"ه\", \"ـ\": \"\","` | — |
| [SRC-1AE03B9EC3-L000078](../../agents/web_agent.py#L78) | 78 | `"})"` | — |
| [SRC-1AE03B9EC3-L000079](../../agents/web_agent.py#L79) | 79 | `"_ARABIC_DIACRITICS_RE = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-1AE03B9EC3-L000080](../../agents/web_agent.py#L80) | 80 | `"_SEARCH_STOPWORDS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000081](../../agents/web_agent.py#L81) | 81 | `"    \"ما\", \"ماذا\", \"من\", \"في\", \"على\", \"عن\", \"الى\", \"إلى\", \"و\", \"او\", \"أو\","` | — |
| [SRC-1AE03B9EC3-L000082](../../agents/web_agent.py#L82) | 82 | `"    \"هل\", \"هو\", \"هي\", \"هذا\", \"هذه\", \"ذلك\", \"تلك\", \"التي\", \"الذي\", \"مع\","` | — |
| [SRC-1AE03B9EC3-L000083](../../agents/web_agent.py#L83) | 83 | `"    \"بين\", \"كيف\", \"لماذا\", \"كم\", \"كان\", \"كانت\", \"يكون\", \"تكون\", \"لي\","` | — |
| [SRC-1AE03B9EC3-L000084](../../agents/web_agent.py#L84) | 84 | `"    \"the\", \"a\", \"an\", \"and\", \"or\", \"in\", \"on\", \"of\", \"to\", \"for\", \"with\","` | — |
| [SRC-1AE03B9EC3-L000085](../../agents/web_agent.py#L85) | 85 | `"    \"is\", \"are\", \"was\", \"were\", \"what\", \"which\", \"who\", \"how\", \"why\", \"when\","` | — |
| [SRC-1AE03B9EC3-L000086](../../agents/web_agent.py#L86) | 86 | `"    \"where\", \"compare\", \"comparison\", \"please\", \"show\", \"find\", \"latest\","` | — |
| [SRC-1AE03B9EC3-L000087](../../agents/web_agent.py#L87) | 87 | `"    \"news\", \"official\", \"sources\", \"source\", \"reports\", \"report\", \"analysis\","` | — |
| [SRC-1AE03B9EC3-L000088](../../agents/web_agent.py#L88) | 88 | `"    \"site\", \"com\", \"org\", \"net\", \"www\","` | — |
| [SRC-1AE03B9EC3-L000089](../../agents/web_agent.py#L89) | 89 | `"    # Arabic request/format words are not useful topic concepts for matching search snippets."` | — |
| [SRC-1AE03B9EC3-L000090](../../agents/web_agent.py#L90) | 90 | `"    \"اذكر\", \"مصدر\", \"مصادر\", \"موثوق\", \"موثوقة\", \"رابط\", \"روابط\", \"مباشر\","` | — |
| [SRC-1AE03B9EC3-L000091](../../agents/web_agent.py#L91) | 91 | `"    \"مباشرة\", \"اجب\", \"بالعربية\", \"العربية\", \"بايجاز\", \"بالايجاز\", \"ايجاز\","` | — |
| [SRC-1AE03B9EC3-L000092](../../agents/web_agent.py#L92) | 92 | `"    \"باختصار\", \"اختصار\", \"استخدم\", \"اعرض\", \"وضح\", \"حلل\", \"قارن\", \"متعددة\","` | — |
| [SRC-1AE03B9EC3-L000093](../../agents/web_agent.py#L93) | 93 | `"    \"اهم\", \"الحقائق\", \"حقائق\", \"استنتاج\", \"استنتاجات\", \"الاستنتاجات\","` | — |
| [SRC-1AE03B9EC3-L000094](../../agents/web_agent.py#L94) | 94 | `"    \"تواريخ\", \"تاريخ\", \"الاخبار\", \"اخبار\", \"المصادر\", \"معلومات\", \"قديمة\","` | — |
| [SRC-1AE03B9EC3-L000095](../../agents/web_agent.py#L95) | 95 | `"    \"قديمه\", \"جديدة\", \"جديده\", \"خلال\", \"الايام\", \"ايام\", \"السبعة\", \"سبعة\","` | — |
| [SRC-1AE03B9EC3-L000096](../../agents/web_agent.py#L96) | 96 | `"    \"الماضية\", \"ماضية\", \"الاسبوع\", \"حاليا\", \"الان\", \"احدث\", \"ولا\","` | — |
| [SRC-1AE03B9EC3-L000097](../../agents/web_agent.py#L97) | 97 | `"    \"تعرض\", \"باعتبارها\","` | — |
| [SRC-1AE03B9EC3-L000098](../../agents/web_agent.py#L98) | 98 | `"})"` | — |
| [SRC-1AE03B9EC3-L000099](../../agents/web_agent.py#L99) | 99 | `"# Search-expansion modifiers are useful after a real topic, but must not stand in"` | — |
| [SRC-1AE03B9EC3-L000100](../../agents/web_agent.py#L100) | 100 | `"# for a topic if a future planner/expansion path loses its subject."` | — |
| [SRC-1AE03B9EC3-L000101](../../agents/web_agent.py#L101) | 101 | `"_GENERIC_QUERY_MODIFIER_TOKENS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000102](../../agents/web_agent.py#L102) | 102 | `"    \"risk\", \"risks\", \"limitation\", \"limitations\", \"alternative\", \"alternatives\","` | — |
| [SRC-1AE03B9EC3-L000103](../../agents/web_agent.py#L103) | 103 | `"    \"recent\", \"data\", \"review\", \"reviews\", \"comparison\", \"compare\", \"official\","` | — |
| [SRC-1AE03B9EC3-L000104](../../agents/web_agent.py#L104) | 104 | `"    \"primary\", \"source\", \"sources\", \"evidence\", \"report\", \"reports\", \"case\", \"cases\","` | — |
| [SRC-1AE03B9EC3-L000105](../../agents/web_agent.py#L105) | 105 | `"    \"study\", \"studies\", \"analysis\", \"latest\", \"news\", \"update\", \"updates\","` | — |
| [SRC-1AE03B9EC3-L000106](../../agents/web_agent.py#L106) | 106 | `"    \"announcement\", \"announcements\", \"comprehensive\", \"research\", \"statistic\","` | — |
| [SRC-1AE03B9EC3-L000107](../../agents/web_agent.py#L107) | 107 | `"    \"statistics\", \"trend\", \"trends\","` | — |
| [SRC-1AE03B9EC3-L000108](../../agents/web_agent.py#L108) | 108 | `"})"` | — |
| [SRC-1AE03B9EC3-L000109](../../agents/web_agent.py#L109) | 109 | `"_SEARCH_SYNONYMS = {"` | — |
| [SRC-1AE03B9EC3-L000110](../../agents/web_agent.py#L110) | 110 | `"    \"استراليا\": {\"australia\"}, \"عاصمة\": {\"capital\"}, \"مصر\": {\"egypt\"},"` | — |
| [SRC-1AE03B9EC3-L000111](../../agents/web_agent.py#L111) | 111 | `"    \"المصري\": {\"egyptian\", \"egypt\"}, \"مركزي\": {\"central\"},"` | — |
| [SRC-1AE03B9EC3-L000112](../../agents/web_agent.py#L112) | 112 | `"    \"المركزي\": {\"central\"}, \"بنك\": {\"bank\"}, \"البنك\": {\"bank\"},"` | — |
| [SRC-1AE03B9EC3-L000113](../../agents/web_agent.py#L113) | 113 | `"    \"قرار\": {\"decision\"}, \"قرارات\": {\"decision\", \"decisions\"},"` | — |
| [SRC-1AE03B9EC3-L000114](../../agents/web_agent.py#L114) | 114 | `"    \"سعر\": {\"price\"}, \"اسعار\": {\"prices\"}, \"استضافة\": {\"hosting\"},"` | — |
| [SRC-1AE03B9EC3-L000115](../../agents/web_agent.py#L115) | 115 | `"    \"شركة\": {\"company\"}, \"شركه\": {\"company\"}, \"ناشئة\": {\"startup\"},"` | — |
| [SRC-1AE03B9EC3-L000116](../../agents/web_agent.py#L116) | 116 | `"    \"صعيد\": {\"upper\"}, \"مقارنة\": {\"compare\", \"comparison\"},"` | — |
| [SRC-1AE03B9EC3-L000117](../../agents/web_agent.py#L117) | 117 | `"    \"تقنية\": {\"technology\"}, \"تقنيات\": {\"technology\"},"` | — |
| [SRC-1AE03B9EC3-L000118](../../agents/web_agent.py#L118) | 118 | `"    \"ميكروسوفت\": {\"microsoft\"}, \"مايكروسوفت\": {\"microsoft\"},"` | — |
| [SRC-1AE03B9EC3-L000119](../../agents/web_agent.py#L119) | 119 | `"    \"microsoft\": {\"ميكروسوفت\", \"مايكروسوفت\"},"` | — |
| [SRC-1AE03B9EC3-L000120](../../agents/web_agent.py#L120) | 120 | `"    \"جمهورية\": {\"republic\"}, \"republic\": {\"جمهورية\"},"` | — |
| [SRC-1AE03B9EC3-L000121](../../agents/web_agent.py#L121) | 121 | `"    \"الرقمية\": {\"digital\"}, \"رقمية\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000122](../../agents/web_agent.py#L122) | 122 | `"    \"الرقميه\": {\"digital\"}, \"رقميه\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000123](../../agents/web_agent.py#L123) | 123 | `"    \"موقع\": {\"website\", \"portal\"}, \"مواقع\": {\"websites\", \"portals\"},"` | — |
| [SRC-1AE03B9EC3-L000124](../../agents/web_agent.py#L124) | 124 | `"    \"التجمع\": {\"settlement\"}, \"تجمع\": {\"settlement\"},"` | — |
| [SRC-1AE03B9EC3-L000125](../../agents/web_agent.py#L125) | 125 | `"    \"الخامس\": {\"fifth\", \"5th\"}, \"خامس\": {\"fifth\", \"5th\"},"` | — |
| [SRC-1AE03B9EC3-L000126](../../agents/web_agent.py#L126) | 126 | `"    \"شقة\": {\"apartment\", \"flat\"}, \"شقق\": {\"apartments\", \"flats\"},"` | — |
| [SRC-1AE03B9EC3-L000127](../../agents/web_agent.py#L127) | 127 | `"    \"عميل\": {\"customer\", \"buyer\"}, \"عملاء\": {\"customers\", \"buyers\"},"` | — |
| [SRC-1AE03B9EC3-L000128](../../agents/web_agent.py#L128) | 128 | `"    \"شراء\": {\"buy\", \"purchase\"}, \"مشتري\": {\"buyer\"},"` | — |
| [SRC-1AE03B9EC3-L000129](../../agents/web_agent.py#L129) | 129 | `"    # Small, explicit Arabic-English topic vocabulary; this helps Arabic prompts"` | — |
| [SRC-1AE03B9EC3-L000130](../../agents/web_agent.py#L130) | 130 | `"    # match English-indexed results without relaxing URL or destination safety."` | — |
| [SRC-1AE03B9EC3-L000131](../../agents/web_agent.py#L131) | 131 | `"    \"سيارة\": {\"car\", \"vehicle\"}, \"السيارة\": {\"car\", \"vehicle\"},"` | — |
| [SRC-1AE03B9EC3-L000132](../../agents/web_agent.py#L132) | 132 | `"    \"سيارات\": {\"cars\", \"vehicles\"}, \"السيارات\": {\"cars\", \"vehicles\"},"` | — |
| [SRC-1AE03B9EC3-L000133](../../agents/web_agent.py#L133) | 133 | `"    \"كهربائي\": {\"electric\"}, \"كهربائية\": {\"electric\"},"` | — |
| [SRC-1AE03B9EC3-L000134](../../agents/web_agent.py#L134) | 134 | `"    \"الكهربائي\": {\"electric\"}, \"الكهربائية\": {\"electric\"},"` | — |
| [SRC-1AE03B9EC3-L000135](../../agents/web_agent.py#L135) | 135 | `"    \"شحن\": {\"charging\", \"charge\"}, \"الشحن\": {\"charging\", \"charge\"},"` | — |
| [SRC-1AE03B9EC3-L000136](../../agents/web_agent.py#L136) | 136 | `"    \"شاحن\": {\"charger\"}, \"بطارية\": {\"battery\"}, \"بطاريات\": {\"batteries\"},"` | — |
| [SRC-1AE03B9EC3-L000137](../../agents/web_agent.py#L137) | 137 | `"    \"تكلفة\": {\"cost\", \"costs\"}, \"التكلفة\": {\"cost\", \"costs\"},"` | — |
| [SRC-1AE03B9EC3-L000138](../../agents/web_agent.py#L138) | 138 | `"    \"البنية\": {\"infrastructure\"}, \"التحتية\": {\"infrastructure\"},"` | — |
| [SRC-1AE03B9EC3-L000139](../../agents/web_agent.py#L139) | 139 | `"    \"تحدي\": {\"challenge\"}, \"تحديات\": {\"challenges\"}, \"التحديات\": {\"challenges\"},"` | — |
| [SRC-1AE03B9EC3-L000140](../../agents/web_agent.py#L140) | 140 | `"    \"وكيل\": {\"agent\"}, \"الوكيل\": {\"agent\"},"` | — |
| [SRC-1AE03B9EC3-L000141](../../agents/web_agent.py#L141) | 141 | `"    \"وكلاء\": {\"agents\"}, \"الوكلاء\": {\"agents\"},"` | — |
| [SRC-1AE03B9EC3-L000142](../../agents/web_agent.py#L142) | 142 | `"    # Bilingual vocabulary for AI use-case searches. Keep the relevance floor"` | — |
| [SRC-1AE03B9EC3-L000143](../../agents/web_agent.py#L143) | 143 | `"    # unchanged; expand only concepts that commonly appear in Arabic news titles."` | — |
| [SRC-1AE03B9EC3-L000144](../../agents/web_agent.py#L144) | 144 | `"    \"استخدام\": {\"use\", \"usage\", \"application\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000145](../../agents/web_agent.py#L145) | 145 | `"    \"استخدامات\": {\"use\", \"usage\", \"application\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000146](../../agents/web_agent.py#L146) | 146 | `"    \"استعمال\": {\"use\", \"usage\", \"application\"},"` | — |
| [SRC-1AE03B9EC3-L000147](../../agents/web_agent.py#L147) | 147 | `"    \"استعمالات\": {\"use\", \"usage\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000148](../../agents/web_agent.py#L148) | 148 | `"    \"حالة\": {\"case\"}, \"حالات\": {\"cases\", \"case\"},"` | — |
| [SRC-1AE03B9EC3-L000149](../../agents/web_agent.py#L149) | 149 | `"    \"اعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000150](../../agents/web_agent.py#L150) | 150 | `"    \"الاعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000151](../../agents/web_agent.py#L151) | 151 | `"    \"للاعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000152](../../agents/web_agent.py#L152) | 152 | `"    \"شركات\": {\"company\", \"companies\", \"business\", \"businesses\"},"` | — |
| [SRC-1AE03B9EC3-L000153](../../agents/web_agent.py#L153) | 153 | `"    \"الشركات\": {\"company\", \"companies\", \"business\", \"businesses\"},"` | — |
| [SRC-1AE03B9EC3-L000154](../../agents/web_agent.py#L154) | 154 | `"    \"صغير\": {\"small\"}, \"صغيرة\": {\"small\"}, \"الصغير\": {\"small\"}, \"الصغيرة\": {\"small\"},"` | — |
| [SRC-1AE03B9EC3-L000155](../../agents/web_agent.py#L155) | 155 | `"    \"ذكاء\": {\"intelligence\", \"ai\"}, \"الذكاء\": {\"intelligence\", \"ai\"},"` | — |
| [SRC-1AE03B9EC3-L000156](../../agents/web_agent.py#L156) | 156 | `"    \"اصطناعي\": {\"artificial\", \"ai\"}, \"الاصطناعي\": {\"artificial\", \"ai\"},"` | — |
| [SRC-1AE03B9EC3-L000157](../../agents/web_agent.py#L157) | 157 | `"    \"تطور\": {\"development\", \"advance\"}, \"تطورات\": {\"developments\", \"advances\", \"updates\", \"latest\"},"` | — |
| [SRC-1AE03B9EC3-L000158](../../agents/web_agent.py#L158) | 158 | `"    \"التطورات\": {\"developments\", \"advances\", \"updates\", \"latest\"},"` | — |
| [SRC-1AE03B9EC3-L000159](../../agents/web_agent.py#L159) | 159 | `"    \"اراء\": {\"opinions\", \"views\"}, \"تجربة\": {\"experience\"}, \"تجارب\": {\"experiences\", \"reviews\"},"` | — |
| [SRC-1AE03B9EC3-L000160](../../agents/web_agent.py#L160) | 160 | `"    \"مستخدم\": {\"user\"}, \"المستخدم\": {\"user\"}, \"مستخدمين\": {\"users\"},"` | — |
| [SRC-1AE03B9EC3-L000161](../../agents/web_agent.py#L161) | 161 | `"    \"المستخدمين\": {\"users\"}, \"مالكون\": {\"owners\"}, \"المالكون\": {\"owners\"},"` | — |
| [SRC-1AE03B9EC3-L000162](../../agents/web_agent.py#L162) | 162 | `"}"` | — |
| [SRC-1AE03B9EC3-L000163](../../agents/web_agent.py#L163) | 163 | `"_CALENDAR_MONTHS = ("` | — |
| [SRC-1AE03B9EC3-L000164](../../agents/web_agent.py#L164) | 164 | `"    \"يناير\", \"فبراير\", \"مارس\", \"ابريل\", \"أبريل\", \"مايو\", \"يونيو\","` | — |
| [SRC-1AE03B9EC3-L000165](../../agents/web_agent.py#L165) | 165 | `"    \"يوليو\", \"اغسطس\", \"أغسطس\", \"سبتمبر\", \"اكتوبر\", \"أكتوبر\","` | — |
| [SRC-1AE03B9EC3-L000166](../../agents/web_agent.py#L166) | 166 | `"    \"نوفمبر\", \"ديسمبر\", \"january\", \"february\", \"march\", \"april\","` | — |
| [SRC-1AE03B9EC3-L000167](../../agents/web_agent.py#L167) | 167 | `"    \"may\", \"june\", \"july\", \"august\", \"september\", \"october\","` | — |
| [SRC-1AE03B9EC3-L000168](../../agents/web_agent.py#L168) | 168 | `"    \"november\", \"december\","` | — |
| [SRC-1AE03B9EC3-L000169](../../agents/web_agent.py#L169) | 169 | `")"` | — |
| [SRC-1AE03B9EC3-L000170](../../agents/web_agent.py#L170) | 170 | `"_BLOCKED_SOURCE_DOMAINS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000171](../../agents/web_agent.py#L171) | 171 | `"    \"translate.google.com\", \"translate.googleusercontent.com\","` | — |
| [SRC-1AE03B9EC3-L000172](../../agents/web_agent.py#L172) | 172 | `"})"` | — |
| [SRC-1AE03B9EC3-L000173](../../agents/web_agent.py#L173) | 173 | `""` | — |
| [SRC-1AE03B9EC3-L000174](../../agents/web_agent.py#L174) | 174 | `""` | — |
| [SRC-1AE03B9EC3-L000175](../../agents/web_agent.py#L175) | 175 | `"def _normalize_search_query(value: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000176](../../agents/web_agent.py#L176) | 176 | `"    \"\"\"Normalize Arabic letters/diacritics while preserving search operators and dates.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000177](../../agents/web_agent.py#L177) | 177 | `"    value = unicodedata.normalize(\"NFKC\", value or \"\")"` | — |
| [SRC-1AE03B9EC3-L000178](../../agents/web_agent.py#L178) | 178 | `"    value = _ARABIC_DIACRITICS_RE.sub(\"\", value).translate(_ARABIC_SEARCH_TRANSLATION)"` | — |
| [SRC-1AE03B9EC3-L000179](../../agents/web_agent.py#L179) | 179 | `"    return re.sub(r\"\\s+\", \" \", value).strip()"` | — |
| [SRC-1AE03B9EC3-L000180](../../agents/web_agent.py#L180) | 180 | `""` | — |
| [SRC-1AE03B9EC3-L000181](../../agents/web_agent.py#L181) | 181 | `""` | — |
| [SRC-1AE03B9EC3-L000182](../../agents/web_agent.py#L182) | 182 | `"# Normalize stop words too: otherwise Arabic letter normalization (e.g. ة→ه, أ→ا)"` | — |
| [SRC-1AE03B9EC3-L000183](../../agents/web_agent.py#L183) | 183 | `"# can leave request-format wording in the token set and distort relevance scores."` | — |
| [SRC-1AE03B9EC3-L000184](../../agents/web_agent.py#L184) | 184 | `"_NORMALIZED_SEARCH_STOPWORDS = frozenset("` | — |
| [SRC-1AE03B9EC3-L000185](../../agents/web_agent.py#L185) | 185 | `"    _normalize_search_query(word).casefold() for word in _SEARCH_STOPWORDS"` | — |
| [SRC-1AE03B9EC3-L000186](../../agents/web_agent.py#L186) | 186 | `")"` | — |
| [SRC-1AE03B9EC3-L000187](../../agents/web_agent.py#L187) | 187 | `""` | — |
| [SRC-1AE03B9EC3-L000188](../../agents/web_agent.py#L188) | 188 | `""` | — |
| [SRC-1AE03B9EC3-L000189](../../agents/web_agent.py#L189) | 189 | `"# Normalize synonym keys and values by the same rules as search text. This avoids"` | — |
| [SRC-1AE03B9EC3-L000190](../../agents/web_agent.py#L190) | 190 | `"# Arabic ta-marbuta/alif variants silently disabling Arabic-to-English matching."` | — |
| [SRC-1AE03B9EC3-L000191](../../agents/web_agent.py#L191) | 191 | `"_NORMALIZED_SEARCH_SYNONYMS: dict[str, set[str]] = {}"` | — |
| [SRC-1AE03B9EC3-L000192](../../agents/web_agent.py#L192) | 192 | `"for _synonym_key, _synonym_values in _SEARCH_SYNONYMS.items():"` | — |
| [SRC-1AE03B9EC3-L000193](../../agents/web_agent.py#L193) | 193 | `"    _normalized_key = _normalize_search_query(_synonym_key).casefold()"` | — |
| [SRC-1AE03B9EC3-L000194](../../agents/web_agent.py#L194) | 194 | `"    _NORMALIZED_SEARCH_SYNONYMS.setdefault(_normalized_key, set()).update("` | — |
| [SRC-1AE03B9EC3-L000195](../../agents/web_agent.py#L195) | 195 | `"        _normalize_search_query(value).casefold() for value in _synonym_values"` | — |
| [SRC-1AE03B9EC3-L000196](../../agents/web_agent.py#L196) | 196 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000197](../../agents/web_agent.py#L197) | 197 | `""` | — |
| [SRC-1AE03B9EC3-L000198](../../agents/web_agent.py#L198) | 198 | `""` | — |
| [SRC-1AE03B9EC3-L000199](../../agents/web_agent.py#L199) | 199 | `"def _search_tokens(value: str) -> set[str]:"` | — |
| [SRC-1AE03B9EC3-L000200](../../agents/web_agent.py#L200) | 200 | `"    \"\"\"Tokenize Arabic/English text and expand a small bilingual vocabulary.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000201](../../agents/web_agent.py#L201) | 201 | `"    value = _normalize_search_query(value).casefold()"` | — |
| [SRC-1AE03B9EC3-L000202](../../agents/web_agent.py#L202) | 202 | `"    value = re.sub(r\"(?i)\\bsite\\s*:\\s*\\S+\", \" \", value)"` | — |
| [SRC-1AE03B9EC3-L000203](../../agents/web_agent.py#L203) | 203 | `"    tokens = re.findall(r\"[a-z0-9]+\|[\\u0620-\\u064A\\u066E-\\u06D3]+\", value)"` | — |
| [SRC-1AE03B9EC3-L000204](../../agents/web_agent.py#L204) | 204 | `"    result: set[str] = set()"` | — |
| [SRC-1AE03B9EC3-L000205](../../agents/web_agent.py#L205) | 205 | `"    for token in tokens:"` | — |
| [SRC-1AE03B9EC3-L000206](../../agents/web_agent.py#L206) | 206 | `"        if token in _NORMALIZED_SEARCH_STOPWORDS or len(token) < 2:"` | — |
| [SRC-1AE03B9EC3-L000207](../../agents/web_agent.py#L207) | 207 | `"            continue"` | — |
| [SRC-1AE03B9EC3-L000208](../../agents/web_agent.py#L208) | 208 | `"        forms = {token}"` | — |
| [SRC-1AE03B9EC3-L000209](../../agents/web_agent.py#L209) | 209 | `"        if token.startswith(\"ال\") and len(token) > 4:"` | — |
| [SRC-1AE03B9EC3-L000210](../../agents/web_agent.py#L210) | 210 | `"            forms.add(token[2:])"` | — |
| [SRC-1AE03B9EC3-L000211](../../agents/web_agent.py#L211) | 211 | `"        forms.update(_NORMALIZED_SEARCH_SYNONYMS.get(token, set()))"` | — |
| [SRC-1AE03B9EC3-L000212](../../agents/web_agent.py#L212) | 212 | `"        # Reverse-map common English equivalents so Arabic and English results can match."` | — |
| [SRC-1AE03B9EC3-L000213](../../agents/web_agent.py#L213) | 213 | `"        for arabic, english in _NORMALIZED_SEARCH_SYNONYMS.items():"` | — |
| [SRC-1AE03B9EC3-L000214](../../agents/web_agent.py#L214) | 214 | `"            if token in english:"` | — |
| [SRC-1AE03B9EC3-L000215](../../agents/web_agent.py#L215) | 215 | `"                forms.add(arabic)"` | — |
| [SRC-1AE03B9EC3-L000216](../../agents/web_agent.py#L216) | 216 | `"                if arabic.startswith(\"ال\") and len(arabic) > 4:"` | — |
| [SRC-1AE03B9EC3-L000217](../../agents/web_agent.py#L217) | 217 | `"                    forms.add(arabic[2:])"` | — |
| [SRC-1AE03B9EC3-L000218](../../agents/web_agent.py#L218) | 218 | `"        result.update(forms)"` | — |
| [SRC-1AE03B9EC3-L000219](../../agents/web_agent.py#L219) | 219 | `"    return result"` | — |
| [SRC-1AE03B9EC3-L000220](../../agents/web_agent.py#L220) | 220 | `""` | — |
| [SRC-1AE03B9EC3-L000221](../../agents/web_agent.py#L221) | 221 | `""` | — |
| [SRC-1AE03B9EC3-L000222](../../agents/web_agent.py#L222) | 222 | `"def _relevance_query_tokens(query: str) -> set[str]:"` | — |
| [SRC-1AE03B9EC3-L000223](../../agents/web_agent.py#L223) | 223 | `"    \"\"\"Return topic concepts after removing answer-format and query-expansion wording.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000224](../../agents/web_agent.py#L224) | 224 | `"    query = compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L000225](../../agents/web_agent.py#L225) | 225 | `"    if not query:"` | — |
| [SRC-1AE03B9EC3-L000226](../../agents/web_agent.py#L226) | 226 | `"        return set()"` | — |
| [SRC-1AE03B9EC3-L000227](../../agents/web_agent.py#L227) | 227 | `"    query_text = _normalize_search_query(query).casefold()"` | — |
| [SRC-1AE03B9EC3-L000228](../../agents/web_agent.py#L228) | 228 | `"    query_text = re.sub(r\"(?i)\\bsite\\s*:\\s*\\S+\", \" \", query_text)"` | — |
| [SRC-1AE03B9EC3-L000229](../../agents/web_agent.py#L229) | 229 | `"    return {"` | — |
| [SRC-1AE03B9EC3-L000230](../../agents/web_agent.py#L230) | 230 | `"        token for token in re.findall(r\"[a-z0-9]+\|[\\u0620-\\u064A\\u066E-\\u06D3]+\", query_text)"` | — |
| [SRC-1AE03B9EC3-L000231](../../agents/web_agent.py#L231) | 231 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L000232](../../agents/web_agent.py#L232) | 232 | `"            token not in _NORMALIZED_SEARCH_STOPWORDS"` | — |
| [SRC-1AE03B9EC3-L000233](../../agents/web_agent.py#L233) | 233 | `"            and token not in _GENERIC_QUERY_MODIFIER_TOKENS"` | — |
| [SRC-1AE03B9EC3-L000234](../../agents/web_agent.py#L234) | 234 | `"            and len(token) >= 2"` | — |
| [SRC-1AE03B9EC3-L000235](../../agents/web_agent.py#L235) | 235 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000236](../../agents/web_agent.py#L236) | 236 | `"    }"` | — |
| [SRC-1AE03B9EC3-L000237](../../agents/web_agent.py#L237) | 237 | `""` | — |
| [SRC-1AE03B9EC3-L000238](../../agents/web_agent.py#L238) | 238 | `""` | — |
| [SRC-1AE03B9EC3-L000239](../../agents/web_agent.py#L239) | 239 | `"def _minimum_relevance_ratio(_query: str) -> float:"` | — |
| [SRC-1AE03B9EC3-L000240](../../agents/web_agent.py#L240) | 240 | `"    \"\"\"Keep the established 20% relevance floor after query normalization and token cleanup.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000241](../../agents/web_agent.py#L241) | 241 | `"    return 0.20"` | — |
| [SRC-1AE03B9EC3-L000242](../../agents/web_agent.py#L242) | 242 | `""` | — |
| [SRC-1AE03B9EC3-L000243](../../agents/web_agent.py#L243) | 243 | `""` | — |
| [SRC-1AE03B9EC3-L000244](../../agents/web_agent.py#L244) | 244 | `"def _relevance_ratio(query: str, evidence: str) -> float:"` | — |
| [SRC-1AE03B9EC3-L000245](../../agents/web_agent.py#L245) | 245 | `"    \"\"\"Fraction of meaningful query concepts present in a candidate's title/snippet.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000246](../../agents/web_agent.py#L246) | 246 | `"    query_tokens = _relevance_query_tokens(query)"` | — |
| [SRC-1AE03B9EC3-L000247](../../agents/web_agent.py#L247) | 247 | `"    if not query_tokens:"` | — |
| [SRC-1AE03B9EC3-L000248](../../agents/web_agent.py#L248) | 248 | `"        # Relevance cannot be established from an instruction-only query."` | — |
| [SRC-1AE03B9EC3-L000249](../../agents/web_agent.py#L249) | 249 | `"        return 0.0"` | — |
| [SRC-1AE03B9EC3-L000250](../../agents/web_agent.py#L250) | 250 | `"    expanded_evidence = _search_tokens(evidence)"` | — |
| [SRC-1AE03B9EC3-L000251](../../agents/web_agent.py#L251) | 251 | `"    matched = sum("` | — |
| [SRC-1AE03B9EC3-L000252](../../agents/web_agent.py#L252) | 252 | `"        1 for token in query_tokens"` | — |
| [SRC-1AE03B9EC3-L000253](../../agents/web_agent.py#L253) | 253 | `"        if token in expanded_evidence"` | — |
| [SRC-1AE03B9EC3-L000254](../../agents/web_agent.py#L254) | 254 | `"        or (token.startswith(\"ال\") and token[2:] in expanded_evidence)"` | — |
| [SRC-1AE03B9EC3-L000255](../../agents/web_agent.py#L255) | 255 | `"        or bool(_NORMALIZED_SEARCH_SYNONYMS.get(token, set()) & expanded_evidence)"` | — |
| [SRC-1AE03B9EC3-L000256](../../agents/web_agent.py#L256) | 256 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000257](../../agents/web_agent.py#L257) | 257 | `"    ratio = matched / len(query_tokens)"` | — |
| [SRC-1AE03B9EC3-L000258](../../agents/web_agent.py#L258) | 258 | `"    # On longer questions, two matching topic concepts are required; request wording"` | — |
| [SRC-1AE03B9EC3-L000259](../../agents/web_agent.py#L259) | 259 | `"    # should not silently raise that floor to three or four concepts."` | — |
| [SRC-1AE03B9EC3-L000260](../../agents/web_agent.py#L260) | 260 | `"    if len(query_tokens) >= 4 and matched < 2:"` | — |
| [SRC-1AE03B9EC3-L000261](../../agents/web_agent.py#L261) | 261 | `"        return 0.0"` | — |
| [SRC-1AE03B9EC3-L000262](../../agents/web_agent.py#L262) | 262 | `"    return ratio"` | — |
| [SRC-1AE03B9EC3-L000263](../../agents/web_agent.py#L263) | 263 | `""` | — |
| [SRC-1AE03B9EC3-L000264](../../agents/web_agent.py#L264) | 264 | `"def _blocked_source_url(url: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000265](../../agents/web_agent.py#L265) | 265 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000266](../../agents/web_agent.py#L266) | 266 | `"        host = (urllib.parse.urlparse(url).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L000267](../../agents/web_agent.py#L267) | 267 | `"        return any(host == domain or host.endswith(\".\" + domain) for domain in _BLOCKED_SOURCE_DOMAINS)"` | — |
| [SRC-1AE03B9EC3-L000268](../../agents/web_agent.py#L268) | 268 | `"    except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L000269](../../agents/web_agent.py#L269) | 269 | `"        return True"` | — |
| [SRC-1AE03B9EC3-L000270](../../agents/web_agent.py#L270) | 270 | `""` | — |
| [SRC-1AE03B9EC3-L000271](../../agents/web_agent.py#L271) | 271 | `""` | — |
| [SRC-1AE03B9EC3-L000272](../../agents/web_agent.py#L272) | 272 | `"class AgentDependencyError(RuntimeError):"` | — |
| [SRC-1AE03B9EC3-L000273](../../agents/web_agent.py#L273) | 273 | `"    \"\"\"A required optional runtime dependency is unavailable.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000274](../../agents/web_agent.py#L274) | 274 | `""` | — |
| [SRC-1AE03B9EC3-L000275](../../agents/web_agent.py#L275) | 275 | `""` | — |
| [SRC-1AE03B9EC3-L000276](../../agents/web_agent.py#L276) | 276 | `"def _clean_text(value: Any, limit: int) -> str:"` | — |
| [SRC-1AE03B9EC3-L000277](../../agents/web_agent.py#L277) | 277 | `"    if not isinstance(value, str):"` | — |
| [SRC-1AE03B9EC3-L000278](../../agents/web_agent.py#L278) | 278 | `"        return \"\""` | — |
| [SRC-1AE03B9EC3-L000279](../../agents/web_agent.py#L279) | 279 | `"    return \" \".join(value.replace(\"\\x00\", \" \").split())[:limit]"` | — |
| [SRC-1AE03B9EC3-L000280](../../agents/web_agent.py#L280) | 280 | `""` | — |
| [SRC-1AE03B9EC3-L000281](../../agents/web_agent.py#L281) | 281 | `""` | — |
| [SRC-1AE03B9EC3-L000282](../../agents/web_agent.py#L282) | 282 | `"def _public_http_url(value: Any) -> str \| None:"` | — |
| [SRC-1AE03B9EC3-L000283](../../agents/web_agent.py#L283) | 283 | `"    \"\"\"Lexically validate an HTTP URL before using it as a search source.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000284](../../agents/web_agent.py#L284) | 284 | `"    if not isinstance(value, str) or len(value) > 2048:"` | — |
| [SRC-1AE03B9EC3-L000285](../../agents/web_agent.py#L285) | 285 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000286](../../agents/web_agent.py#L286) | 286 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000287](../../agents/web_agent.py#L287) | 287 | `"        parsed = urllib.parse.urlparse(value.strip())"` | — |
| [SRC-1AE03B9EC3-L000288](../../agents/web_agent.py#L288) | 288 | `"        if parsed.scheme not in {\"http\", \"https\"}:"` | — |
| [SRC-1AE03B9EC3-L000289](../../agents/web_agent.py#L289) | 289 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000290](../../agents/web_agent.py#L290) | 290 | `"        if not parsed.hostname or parsed.username is not None or parsed.password is not None:"` | — |
| [SRC-1AE03B9EC3-L000291](../../agents/web_agent.py#L291) | 291 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000292](../../agents/web_agent.py#L292) | 292 | `"        if parsed.port not in (None, 80, 443):"` | — |
| [SRC-1AE03B9EC3-L000293](../../agents/web_agent.py#L293) | 293 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000294](../../agents/web_agent.py#L294) | 294 | `"        host = parsed.hostname.rstrip(\".\").lower()"` | — |
| [SRC-1AE03B9EC3-L000295](../../agents/web_agent.py#L295) | 295 | `"        if not host or host in {\"localhost\"} or host.endswith((\".local\", \".internal\", \".localhost\")):"` | — |
| [SRC-1AE03B9EC3-L000296](../../agents/web_agent.py#L296) | 296 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000297](../../agents/web_agent.py#L297) | 297 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000298](../../agents/web_agent.py#L298) | 298 | `"            ip = ipaddress.ip_address(host)"` | — |
| [SRC-1AE03B9EC3-L000299](../../agents/web_agent.py#L299) | 299 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L000300](../../agents/web_agent.py#L300) | 300 | `"            pass"` | — |
| [SRC-1AE03B9EC3-L000301](../../agents/web_agent.py#L301) | 301 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L000302](../../agents/web_agent.py#L302) | 302 | `"            if not ip.is_global:"` | — |
| [SRC-1AE03B9EC3-L000303](../../agents/web_agent.py#L303) | 303 | `"                return None"` | — |
| [SRC-1AE03B9EC3-L000304](../../agents/web_agent.py#L304) | 304 | `"        return urllib.parse.urlunparse(parsed._replace(fragment=\"\"))"` | — |
| [SRC-1AE03B9EC3-L000305](../../agents/web_agent.py#L305) | 305 | `"    except (ValueError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L000306](../../agents/web_agent.py#L306) | 306 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000307](../../agents/web_agent.py#L307) | 307 | `""` | — |
| [SRC-1AE03B9EC3-L000308](../../agents/web_agent.py#L308) | 308 | `""` | — |
| [SRC-1AE03B9EC3-L000309](../../agents/web_agent.py#L309) | 309 | `"def _public_ip_literals(host: str) -> list[str] \| None:"` | — |
| [SRC-1AE03B9EC3-L000310](../../agents/web_agent.py#L310) | 310 | `"    \"\"\"Resolve host and return its public addresses."` | — |
| [SRC-1AE03B9EC3-L000311](../../agents/web_agent.py#L311) | 311 | `""` | — |
| [SRC-1AE03B9EC3-L000312](../../agents/web_agent.py#L312) | 312 | `"    Returns None when resolution fails or any answer is not a global address."` | — |
| [SRC-1AE03B9EC3-L000313](../../agents/web_agent.py#L313) | 313 | `"    Callers must open the TCP connection to one of these literals. A second DNS"` | — |
| [SRC-1AE03B9EC3-L000314](../../agents/web_agent.py#L314) | 314 | `"    lookup is not equivalent: the name can be rebound to a private address"` | — |
| [SRC-1AE03B9EC3-L000315](../../agents/web_agent.py#L315) | 315 | `"    between the check and the connection (DNS rebinding / TOCTOU)."` | — |
| [SRC-1AE03B9EC3-L000316](../../agents/web_agent.py#L316) | 316 | `"    \"\"\""` | — |
| [SRC-1AE03B9EC3-L000317](../../agents/web_agent.py#L317) | 317 | `"    if not host:"` | — |
| [SRC-1AE03B9EC3-L000318](../../agents/web_agent.py#L318) | 318 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000319](../../agents/web_agent.py#L319) | 319 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000320](../../agents/web_agent.py#L320) | 320 | `"        answers = socket.getaddrinfo(host, None, type=socket.SOCK_STREAM)"` | — |
| [SRC-1AE03B9EC3-L000321](../../agents/web_agent.py#L321) | 321 | `"    except (OSError, socket.gaierror):"` | — |
| [SRC-1AE03B9EC3-L000322](../../agents/web_agent.py#L322) | 322 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000323](../../agents/web_agent.py#L323) | 323 | `"    if not answers:"` | — |
| [SRC-1AE03B9EC3-L000324](../../agents/web_agent.py#L324) | 324 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000325](../../agents/web_agent.py#L325) | 325 | `"    literals: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L000326](../../agents/web_agent.py#L326) | 326 | `"    for answer in answers:"` | — |
| [SRC-1AE03B9EC3-L000327](../../agents/web_agent.py#L327) | 327 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000328](../../agents/web_agent.py#L328) | 328 | `"            address = ipaddress.ip_address(answer[4][0])"` | — |
| [SRC-1AE03B9EC3-L000329](../../agents/web_agent.py#L329) | 329 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L000330](../../agents/web_agent.py#L330) | 330 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000331](../../agents/web_agent.py#L331) | 331 | `"        if not address.is_global:"` | — |
| [SRC-1AE03B9EC3-L000332](../../agents/web_agent.py#L332) | 332 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000333](../../agents/web_agent.py#L333) | 333 | `"        literal = str(address)"` | — |
| [SRC-1AE03B9EC3-L000334](../../agents/web_agent.py#L334) | 334 | `"        if literal not in literals:"` | — |
| [SRC-1AE03B9EC3-L000335](../../agents/web_agent.py#L335) | 335 | `"            literals.append(literal)"` | — |
| [SRC-1AE03B9EC3-L000336](../../agents/web_agent.py#L336) | 336 | `"    return literals or None"` | — |
| [SRC-1AE03B9EC3-L000337](../../agents/web_agent.py#L337) | 337 | `""` | — |
| [SRC-1AE03B9EC3-L000338](../../agents/web_agent.py#L338) | 338 | `""` | — |
| [SRC-1AE03B9EC3-L000339](../../agents/web_agent.py#L339) | 339 | `"def _host_resolves_publicly(host: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000340](../../agents/web_agent.py#L340) | 340 | `"    \"\"\"Reject local/private destinations before fetching a third-party page.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000341](../../agents/web_agent.py#L341) | 341 | `"    return _public_ip_literals(host) is not None"` | — |
| [SRC-1AE03B9EC3-L000342](../../agents/web_agent.py#L342) | 342 | `""` | — |
| [SRC-1AE03B9EC3-L000343](../../agents/web_agent.py#L343) | 343 | `""` | — |
| [SRC-1AE03B9EC3-L000344](../../agents/web_agent.py#L344) | 344 | `"def _pinned_connect_url(logical_url: str, ip: str) -> str \| None:"` | — |
| [SRC-1AE03B9EC3-L000345](../../agents/web_agent.py#L345) | 345 | `"    \"\"\"Rewrite a validated public URL so the connection target is a checked IP.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000346](../../agents/web_agent.py#L346) | 346 | `"    parsed = urllib.parse.urlparse(logical_url)"` | — |
| [SRC-1AE03B9EC3-L000347](../../agents/web_agent.py#L347) | 347 | `"    if parsed.port not in (None, 80, 443):"` | — |
| [SRC-1AE03B9EC3-L000348](../../agents/web_agent.py#L348) | 348 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000349](../../agents/web_agent.py#L349) | 349 | `"    literal = f\"[{ip}]\" if \":\" in ip else ip"` | — |
| [SRC-1AE03B9EC3-L000350](../../agents/web_agent.py#L350) | 350 | `"    netloc = literal if parsed.port is None else f\"{literal}:{parsed.port}\""` | — |
| [SRC-1AE03B9EC3-L000351](../../agents/web_agent.py#L351) | 351 | `"    return urllib.parse.urlunparse(parsed._replace(netloc=netloc))"` | — |
| [SRC-1AE03B9EC3-L000352](../../agents/web_agent.py#L352) | 352 | `""` | — |
| [SRC-1AE03B9EC3-L000353](../../agents/web_agent.py#L353) | 353 | `""` | — |
| [SRC-1AE03B9EC3-L000354](../../agents/web_agent.py#L354) | 354 | `"def _fallback_answer(sources: list[dict[str, Any]], reason: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000355](../../agents/web_agent.py#L355) | 355 | `"    lines = [reason]"` | — |
| [SRC-1AE03B9EC3-L000356](../../agents/web_agent.py#L356) | 356 | `"    usable = [source for source in sources if source.get(\"snippet\")]"` | — |
| [SRC-1AE03B9EC3-L000357](../../agents/web_agent.py#L357) | 357 | `"    for index, source in enumerate(usable[:5], 1):"` | — |
| [SRC-1AE03B9EC3-L000358](../../agents/web_agent.py#L358) | 358 | `"        lines.append("` | — |
| [SRC-1AE03B9EC3-L000359](../../agents/web_agent.py#L359) | 359 | `"            f\"{index}. {source.get('title', 'نتيجة ويب')}: \""` | — |
| [SRC-1AE03B9EC3-L000360](../../agents/web_agent.py#L360) | 360 | `"            f\"{source['snippet']} (المصدر: {source['url']})\""` | — |
| [SRC-1AE03B9EC3-L000361](../../agents/web_agent.py#L361) | 361 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000362](../../agents/web_agent.py#L362) | 362 | `"    if not usable:"` | — |
| [SRC-1AE03B9EC3-L000363](../../agents/web_agent.py#L363) | 363 | `"        lines.append(\"لم أتمكن من استخراج مقتطفات كافية من نتائج الويب.\")"` | — |
| [SRC-1AE03B9EC3-L000364](../../agents/web_agent.py#L364) | 364 | `"    return \"\\n\\n\".join(lines)"` | — |
| [SRC-1AE03B9EC3-L000365](../../agents/web_agent.py#L365) | 365 | `""` | — |
| [SRC-1AE03B9EC3-L000366](../../agents/web_agent.py#L366) | 366 | `""` | — |
| [SRC-1AE03B9EC3-L000367](../../agents/web_agent.py#L367) | 367 | `"class PageFetchResult(tuple):"` | — |
| [SRC-1AE03B9EC3-L000368](../../agents/web_agent.py#L368) | 368 | `"    \"\"\"Two-item tuple compatible with legacy callers, with structured extraction status.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000369](../../agents/web_agent.py#L369) | 369 | `""` | — |
| [SRC-1AE03B9EC3-L000370](../../agents/web_agent.py#L370) | 370 | `"    def __new__("` | — |
| [SRC-1AE03B9EC3-L000371](../../agents/web_agent.py#L371) | 371 | `"        cls,"` | — |
| [SRC-1AE03B9EC3-L000372](../../agents/web_agent.py#L372) | 372 | `"        title: str = \"\","` | — |
| [SRC-1AE03B9EC3-L000373](../../agents/web_agent.py#L373) | 373 | `"        page_text: str = \"\","` | — |
| [SRC-1AE03B9EC3-L000374](../../agents/web_agent.py#L374) | 374 | `"        status: str = \"unknown\","` | — |
| [SRC-1AE03B9EC3-L000375](../../agents/web_agent.py#L375) | 375 | `"        error_class: str \| None = None,"` | — |
