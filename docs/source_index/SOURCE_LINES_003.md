# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **003**
- سجلات الأسطر: **800**
- النطاق: SRC-FDEEAFDFCA-L000115 إلى SRC-1AE03B9EC3-L000017
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-FDEEAFDFCA — [agents/request_budget.py](../../agents/request_budget.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-59CF4B7DE8-L000043](../../agents/research.py#L43) | 43 | `"    parsed = urlparse(candidate if \"://\" in candidate else \"//\" + candidate)"` | — |
| [SRC-59CF4B7DE8-L000044](../../agents/research.py#L44) | 44 | `"    host = (parsed.hostname or \"\").rstrip(\".\").lower()"` | — |
| [SRC-59CF4B7DE8-L000045](../../agents/research.py#L45) | 45 | `"    if not host:"` | — |
| [SRC-59CF4B7DE8-L000046](../../agents/research.py#L46) | 46 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000047](../../agents/research.py#L47) | 47 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000048](../../agents/research.py#L48) | 48 | `"        return str(ipaddress.ip_address(host))"` | — |
| [SRC-59CF4B7DE8-L000049](../../agents/research.py#L49) | 49 | `"    except ValueError:"` | — |
| [SRC-59CF4B7DE8-L000050](../../agents/research.py#L50) | 50 | `"        pass"` | — |
| [SRC-59CF4B7DE8-L000051](../../agents/research.py#L51) | 51 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000052](../../agents/research.py#L52) | 52 | `"        host = host.encode(\"idna\").decode(\"ascii\").lower()"` | — |
| [SRC-59CF4B7DE8-L000053](../../agents/research.py#L53) | 53 | `"    except UnicodeError:"` | — |
| [SRC-59CF4B7DE8-L000054](../../agents/research.py#L54) | 54 | `"        return host"` | — |
| [SRC-59CF4B7DE8-L000055](../../agents/research.py#L55) | 55 | `"    extracted = _DOMAIN_EXTRACTOR(host)"` | — |
| [SRC-59CF4B7DE8-L000056](../../agents/research.py#L56) | 56 | `"    return (extracted.top_domain_under_public_suffix or host).lower()"` | — |
| [SRC-59CF4B7DE8-L000057](../../agents/research.py#L57) | 57 | `""` | — |
| [SRC-59CF4B7DE8-L000058](../../agents/research.py#L58) | 58 | `"SOCIAL_DOMAINS = {"` | — |
| [SRC-59CF4B7DE8-L000059](../../agents/research.py#L59) | 59 | `"    \"reddit\": \"reddit.com\","` | — |
| [SRC-59CF4B7DE8-L000060](../../agents/research.py#L60) | 60 | `"    \"youtube\": \"youtube.com\","` | — |
| [SRC-59CF4B7DE8-L000061](../../agents/research.py#L61) | 61 | `"    \"facebook\": \"facebook.com\","` | — |
| [SRC-59CF4B7DE8-L000062](../../agents/research.py#L62) | 62 | `"    \"instagram\": \"instagram.com\","` | — |
| [SRC-59CF4B7DE8-L000063](../../agents/research.py#L63) | 63 | `"    \"x\": \"x.com\","` | — |
| [SRC-59CF4B7DE8-L000064](../../agents/research.py#L64) | 64 | `"    \"twitter\": \"twitter.com\","` | — |
| [SRC-59CF4B7DE8-L000065](../../agents/research.py#L65) | 65 | `"    \"tiktok\": \"tiktok.com\","` | — |
| [SRC-59CF4B7DE8-L000066](../../agents/research.py#L66) | 66 | `"    \"linkedin\": \"linkedin.com\","` | — |
| [SRC-59CF4B7DE8-L000067](../../agents/research.py#L67) | 67 | `"    \"threads\": \"threads.net\","` | — |
| [SRC-59CF4B7DE8-L000068](../../agents/research.py#L68) | 68 | `"    \"bluesky\": \"bsky.app\","` | — |
| [SRC-59CF4B7DE8-L000069](../../agents/research.py#L69) | 69 | `"}"` | — |
| [SRC-59CF4B7DE8-L000070](../../agents/research.py#L70) | 70 | `""` | — |
| [SRC-59CF4B7DE8-L000071](../../agents/research.py#L71) | 71 | `"_SOCIAL_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000072](../../agents/research.py#L72) | 72 | `"    \"social media\", \"social network\", \"social posts\", \"social pages\", \"public social\", \"public posts\","` | — |
| [SRC-59CF4B7DE8-L000073](../../agents/research.py#L73) | 73 | `"    \"facebook\", \"instagram\", \"reddit\", \"youtube\", \"twitter\", \"x.com\","` | — |
| [SRC-59CF4B7DE8-L000074](../../agents/research.py#L74) | 74 | `"    \"tiktok\", \"linkedin\", \"threads\", \"bluesky\","` | — |
| [SRC-59CF4B7DE8-L000075](../../agents/research.py#L75) | 75 | `"    \"سوشيال\", \"التواصل الاجتماعي\", \"مواقع التواصل\", \"صفحات التواصل\","` | — |
| [SRC-59CF4B7DE8-L000076](../../agents/research.py#L76) | 76 | `"    \"منشورات\", \"تعليقات الناس\", \"آراء الناس\", \"تجارب المستخدمين\","` | — |
| [SRC-59CF4B7DE8-L000077](../../agents/research.py#L77) | 77 | `"    \"تجارب العملاء\", \"اراء العملاء\", \"آراء العملاء\", \"رأي الناس\","` | — |
| [SRC-59CF4B7DE8-L000078](../../agents/research.py#L78) | 78 | `"    \"كلام الناس\", \"الناس بتقول\", \"مراجعات العملاء\", \"تعليقات العملاء\","` | — |
| [SRC-59CF4B7DE8-L000079](../../agents/research.py#L79) | 79 | `"    \"بوستات\", \"فيدوهات\", \"فيديوهات\", \"ريلز\", \"تويتر\", \"فيسبوك\","` | — |
| [SRC-59CF4B7DE8-L000080](../../agents/research.py#L80) | 80 | `"    \"انستجرام\", \"إنستجرام\", \"تيك توك\", \"لينكدان\", \"لينكدإن\","` | — |
| [SRC-59CF4B7DE8-L000081](../../agents/research.py#L81) | 81 | `"    \"مصادر العملاء\", \"عملاء محتملين\", \"العملاء المحتملين\","` | — |
| [SRC-59CF4B7DE8-L000082](../../agents/research.py#L82) | 82 | `")"` | — |
| [SRC-59CF4B7DE8-L000083](../../agents/research.py#L83) | 83 | `""` | — |
| [SRC-59CF4B7DE8-L000084](../../agents/research.py#L84) | 84 | `"_FRESH_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000085](../../agents/research.py#L85) | 85 | `"    \"latest\", \"current\", \"today\", \"this week\", \"recent\", \"breaking\", \"news\","` | — |
| [SRC-59CF4B7DE8-L000086](../../agents/research.py#L86) | 86 | `"    \"now\", \"2026\", \"latest price\", \"market price\", \"updated\","` | — |
| [SRC-59CF4B7DE8-L000087](../../agents/research.py#L87) | 87 | `"    \"آخر\", \"اخر\", \"احدث\", \"أحدث\", \"حاليا\", \"حالياً\", \"الآن\", \"دلوقتي\", \"النهارده\", \"مؤخرًا\", \"مؤخرا\", \"اليوم\", \"هذا الاسبوع\","` | — |
| [SRC-59CF4B7DE8-L000088](../../agents/research.py#L88) | 88 | `"    \"هذا الأسبوع\", \"آخر الأخبار\", \"اخر الاخبار\", \"مستجدات\", \"حديث\","` | — |
| [SRC-59CF4B7DE8-L000089](../../agents/research.py#L89) | 89 | `"    \"سعر اليوم\", \"الاسعار الحالية\", \"الأسعار الحالية\", \"جديد\","` | — |
| [SRC-59CF4B7DE8-L000090](../../agents/research.py#L90) | 90 | `")"` | — |
| [SRC-59CF4B7DE8-L000091](../../agents/research.py#L91) | 91 | `""` | — |
| [SRC-59CF4B7DE8-L000092](../../agents/research.py#L92) | 92 | `"_DEEP_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000093](../../agents/research.py#L93) | 93 | `"    \"deep research\", \"in-depth\", \"comprehensive\", \"exhaustive\", \"compare\","` | — |
| [SRC-59CF4B7DE8-L000094](../../agents/research.py#L94) | 94 | `"    \"comparison\", \"pros and cons\", \"investigate\", \"evidence\", \"sources\","` | — |
| [SRC-59CF4B7DE8-L000095](../../agents/research.py#L95) | 95 | `"    \"بحث عميق\", \"بحث معمق\", \"بحث مكثف\", \"بحث شامل\", \"بالتفصيل\", \"قارن\","` | — |
| [SRC-59CF4B7DE8-L000096](../../agents/research.py#L96) | 96 | `"    \"مقارنة\", \"استقصاء\", \"تحقق\", \"تأكد\", \"مصادر\", \"أدلة\", \"ادلة\","` | — |
| [SRC-59CF4B7DE8-L000097](../../agents/research.py#L97) | 97 | `"    \"كل الجوانب\", \"بحث واسع\", \"متكامل\","` | — |
| [SRC-59CF4B7DE8-L000098](../../agents/research.py#L98) | 98 | `")"` | — |
| [SRC-59CF4B7DE8-L000099](../../agents/research.py#L99) | 99 | `""` | — |
| [SRC-59CF4B7DE8-L000100](../../agents/research.py#L100) | 100 | `""` | — |
| [SRC-59CF4B7DE8-L000101](../../agents/research.py#L101) | 101 | `"def extract_urls(text: str) -> list[str]:"` | — |
| [SRC-59CF4B7DE8-L000102](../../agents/research.py#L102) | 102 | `"    \"\"\"Extract explicit HTTP(S) URLs without trying to interpret their content as instructions.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000103](../../agents/research.py#L103) | 103 | `"    candidates = re.findall(r\"https?://[^\\s<>()]+\", text or \"\", flags=re.IGNORECASE)"` | — |
| [SRC-59CF4B7DE8-L000104](../../agents/research.py#L104) | 104 | `"    cleaned: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000105](../../agents/research.py#L105) | 105 | `"    for value in candidates:"` | — |
| [SRC-59CF4B7DE8-L000106](../../agents/research.py#L106) | 106 | `"        url = value.rstrip(\".,;!?،؛:)\\\"'»\")"` | — |
| [SRC-59CF4B7DE8-L000107](../../agents/research.py#L107) | 107 | `"        if url and url not in cleaned:"` | — |
| [SRC-59CF4B7DE8-L000108](../../agents/research.py#L108) | 108 | `"            cleaned.append(url[:2048])"` | — |
| [SRC-59CF4B7DE8-L000109](../../agents/research.py#L109) | 109 | `"        if len(cleaned) >= 5:"` | — |
| [SRC-59CF4B7DE8-L000110](../../agents/research.py#L110) | 110 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000111](../../agents/research.py#L111) | 111 | `"    return cleaned"` | — |
| [SRC-59CF4B7DE8-L000112](../../agents/research.py#L112) | 112 | `""` | — |
| [SRC-59CF4B7DE8-L000113](../../agents/research.py#L113) | 113 | `""` | — |
| [SRC-59CF4B7DE8-L000114](../../agents/research.py#L114) | 114 | `"def _compact(value: Any, limit: int = MAX_QUERY_CHARS) -> str:"` | — |
| [SRC-59CF4B7DE8-L000115](../../agents/research.py#L115) | 115 | `"    if not isinstance(value, str):"` | — |
| [SRC-59CF4B7DE8-L000116](../../agents/research.py#L116) | 116 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000117](../../agents/research.py#L117) | 117 | `"    return re.sub(r\"\\s+\", \" \", value).strip()[:limit]"` | — |
| [SRC-59CF4B7DE8-L000118](../../agents/research.py#L118) | 118 | `""` | — |
| [SRC-59CF4B7DE8-L000119](../../agents/research.py#L119) | 119 | `""` | — |
| [SRC-59CF4B7DE8-L000120](../../agents/research.py#L120) | 120 | `"_SEARCH_TOPIC_PRESERVING_META_PREFIX_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000121](../../agents/research.py#L121) | 121 | `"    r\"^(?:(?:و?استخدم\|و?استعمل)\\s+مصادر?\\s+متعددة\\s+\""` | — |
| [SRC-59CF4B7DE8-L000122](../../agents/research.py#L122) | 122 | `"    r\"(?:للبحث\\s+عن\|للعثور\\s+على\|لإيجاد\|عن\|حول\|بشأن)\|\""` | — |
| [SRC-59CF4B7DE8-L000123](../../agents/research.py#L123) | 123 | `"    r\"use\\s+multiple\\s+sources\\s+to\\s+(?:research\|find\|investigate))\\s+\","` | — |
| [SRC-59CF4B7DE8-L000124](../../agents/research.py#L124) | 124 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000125](../../agents/research.py#L125) | 125 | `")"` | — |
| [SRC-59CF4B7DE8-L000126](../../agents/research.py#L126) | 126 | `""` | — |
| [SRC-59CF4B7DE8-L000127](../../agents/research.py#L127) | 127 | `"_SEARCH_META_START_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000128](../../agents/research.py#L128) | 128 | `"    r\"^(?:و?استخدم\|و?استعمل\|و?اجب\|و?أجب\|و?لا تعرض\|و?لا تقدم\|\""` | — |
| [SRC-59CF4B7DE8-L000129](../../agents/research.py#L129) | 129 | `"    r\"please cite\|cite\|provide links\|mention sources\|use multiple sources\|\""` | — |
| [SRC-59CF4B7DE8-L000130](../../agents/research.py#L130) | 130 | `"    r\"don't present\|do not present)\\b\","` | — |
| [SRC-59CF4B7DE8-L000131](../../agents/research.py#L131) | 131 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000132](../../agents/research.py#L132) | 132 | `")"` | — |
| [SRC-59CF4B7DE8-L000133](../../agents/research.py#L133) | 133 | `"# Treat \"اذكر\" as an action unless its object is clearly citation/format metadata."` | — |
| [SRC-59CF4B7DE8-L000134](../../agents/research.py#L134) | 134 | `"# This preserves topic-bearing prompts such as \"اذكر أبرز السيارات الكهربائية...\"."` | — |
| [SRC-59CF4B7DE8-L000135](../../agents/research.py#L135) | 135 | `"_SEARCH_CITATION_META_START_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000136](../../agents/research.py#L136) | 136 | `"    r\"^(?:و?اذكر(?:ي\|وا)?\|mention\|cite\|provide)\\s+\""` | — |
| [SRC-59CF4B7DE8-L000137](../../agents/research.py#L137) | 137 | `"    r\"(?:المصادر\|مصادر\|المصدر\|مصدر(?:[ًٌٍ]ا?\|ا[ًٌٍ]?)?\|\""` | — |
| [SRC-59CF4B7DE8-L000138](../../agents/research.py#L138) | 138 | `"    r\"روابط?\|رابط\|تواريخ?\|تاريخ\|الاخبار\|الأخبار\|\""` | — |
| [SRC-59CF4B7DE8-L000139](../../agents/research.py#L139) | 139 | `"    r\"the original posts\|links\|sources\|dates)(?=\\s\|$\|[،,])\","` | — |
| [SRC-59CF4B7DE8-L000140](../../agents/research.py#L140) | 140 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000141](../../agents/research.py#L141) | 141 | `")"` | — |
| [SRC-59CF4B7DE8-L000142](../../agents/research.py#L142) | 142 | `"# This is a response-quality instruction, not a topic query."` | — |
| [SRC-59CF4B7DE8-L000143](../../agents/research.py#L143) | 143 | `"_SEARCH_UNCERTAINTY_META_START_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000144](../../agents/research.py#L144) | 144 | `"    r\"^و?وضّ?ح\\s+اذا\\s+كانت\\s+النتائج\\s+غير\\s+كافيه\\b\""` | — |
| [SRC-59CF4B7DE8-L000145](../../agents/research.py#L145) | 145 | `"    r\".*(?:لتمثيل\|تمثيل).*(?:اراء\\s+المستخدمين\|المستخدمين)\\b\","` | — |
| [SRC-59CF4B7DE8-L000146](../../agents/research.py#L146) | 146 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000147](../../agents/research.py#L147) | 147 | `")"` | — |
| [SRC-59CF4B7DE8-L000148](../../agents/research.py#L148) | 148 | `""` | — |
| [SRC-59CF4B7DE8-L000149](../../agents/research.py#L149) | 149 | `"_SEARCH_FACTS_INFERENCE_META_ONLY_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000150](../../agents/research.py#L150) | 150 | `"    r\"^و?(?:ميّز\|ميز)\\s+بين\\s+الحقائق\\s+والاستنتاجات\\s*[.!؟؛،,]*$\","` | — |
| [SRC-59CF4B7DE8-L000151](../../agents/research.py#L151) | 151 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000152](../../agents/research.py#L152) | 152 | `")"` | — |
| [SRC-59CF4B7DE8-L000153](../../agents/research.py#L153) | 153 | `"_SEARCH_META_TAIL_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000154](../../agents/research.py#L154) | 154 | `"    r\"\\s*[,،؛;]\\s*(?:و\\s*)?(?:استخدم\|استعمل\|ميّز\|ميز\|اجب\|أجب\|لا تعرض\|لا تقدم\|\""` | — |
| [SRC-59CF4B7DE8-L000155](../../agents/research.py#L155) | 155 | `"    r\"please cite\|cite\|provide links\|mention sources\|use multiple sources\|\""` | — |
| [SRC-59CF4B7DE8-L000156](../../agents/research.py#L156) | 156 | `"    r\"don't present\|do not present\|\""` | — |
| [SRC-59CF4B7DE8-L000157](../../agents/research.py#L157) | 157 | `"    r\"اذكر(?:ي\|وا)?\\s+(?:مصادر?\|المصادر\|مصدر\|روابط?\|رابط\|تواريخ?\|تاريخ\|الاخبار\|الأخبار))\\b.*$\","` | — |
| [SRC-59CF4B7DE8-L000158](../../agents/research.py#L158) | 158 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000159](../../agents/research.py#L159) | 159 | `")"` | — |
| [SRC-59CF4B7DE8-L000160](../../agents/research.py#L160) | 160 | `"_SEARCH_LEADING_ACTION_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000161](../../agents/research.py#L161) | 161 | `"    r\"^(?:حلّل\|حلل\|اجمع\|قارن\|ناقش\|استكشف\|استقصِ\|و?ميّز\|و?ميز\|اعرض\|و?وضح\|و?وضّح\|و?اذكر(?:ي\|وا)?\|\""` | — |
| [SRC-59CF4B7DE8-L000162](../../agents/research.py#L162) | 162 | `"    r\"analyze\|analyse\|compare\|investigate\|collect\|gather\|review\|summarize\|\""` | — |
| [SRC-59CF4B7DE8-L000163](../../agents/research.py#L163) | 163 | `"    r\"(?:ابحث\|بحث\|دورلي\|دور\|اعثر)(?:\\s+(?:عن\|على))?)\\s+\","` | — |
| [SRC-59CF4B7DE8-L000164](../../agents/research.py#L164) | 164 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000165](../../agents/research.py#L165) | 165 | `")"` | — |
| [SRC-59CF4B7DE8-L000166](../../agents/research.py#L166) | 166 | `""` | — |
| [SRC-59CF4B7DE8-L000167](../../agents/research.py#L167) | 167 | `""` | — |
| [SRC-59CF4B7DE8-L000168](../../agents/research.py#L168) | 168 | `"def compact_search_query(value: Any, limit: int = MAX_QUERY_CHARS) -> str:"` | — |
| [SRC-59CF4B7DE8-L000169](../../agents/research.py#L169) | 169 | `"    \"\"\"Reduce a full request to the topic-bearing query; preserve safety checks elsewhere.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000170](../../agents/research.py#L170) | 170 | `"    if not isinstance(value, str):"` | — |
| [SRC-59CF4B7DE8-L000171](../../agents/research.py#L171) | 171 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000172](../../agents/research.py#L172) | 172 | `"    cleaned = re.sub(r\"https?://[^\\s<>()]+\", \" \", value, flags=re.IGNORECASE)"` | — |
| [SRC-59CF4B7DE8-L000173](../../agents/research.py#L173) | 173 | `"    # Split question/sentence boundaries without splitting operators such as site:reddit.com."` | — |
| [SRC-59CF4B7DE8-L000174](../../agents/research.py#L174) | 174 | `"    segments = re.split("` | — |
| [SRC-59CF4B7DE8-L000175](../../agents/research.py#L175) | 175 | `"        r\"(?<=[!?؟؛;])\\s+\|(?<=\\.)\\s+(?=[A-Z\\u0600-\\u06FF])\","` | — |
| [SRC-59CF4B7DE8-L000176](../../agents/research.py#L176) | 176 | `"        cleaned,"` | — |
| [SRC-59CF4B7DE8-L000177](../../agents/research.py#L177) | 177 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000178](../../agents/research.py#L178) | 178 | `"    useful: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000179](../../agents/research.py#L179) | 179 | `"    for segment in segments:"` | — |
| [SRC-59CF4B7DE8-L000180](../../agents/research.py#L180) | 180 | `"        segment = segment.strip()"` | — |
| [SRC-59CF4B7DE8-L000181](../../agents/research.py#L181) | 181 | `"        if not segment:"` | — |
| [SRC-59CF4B7DE8-L000182](../../agents/research.py#L182) | 182 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000183](../../agents/research.py#L183) | 183 | `"        normalized_segment = re.sub(r\"[\\u064B-\\u065F\\u0670]\", \"\", segment)"` | — |
| [SRC-59CF4B7DE8-L000184](../../agents/research.py#L184) | 184 | `"        normalized_segment = _normalize_arabic(normalized_segment).casefold()"` | — |
| [SRC-59CF4B7DE8-L000185](../../agents/research.py#L185) | 185 | `"        if ("` | — |
| [SRC-59CF4B7DE8-L000186](../../agents/research.py#L186) | 186 | `"            _SEARCH_CITATION_META_START_RE.search(normalized_segment)"` | — |
| [SRC-59CF4B7DE8-L000187](../../agents/research.py#L187) | 187 | `"            or _SEARCH_UNCERTAINTY_META_START_RE.search(normalized_segment)"` | — |
| [SRC-59CF4B7DE8-L000188](../../agents/research.py#L188) | 188 | `"            or _SEARCH_FACTS_INFERENCE_META_ONLY_RE.search(normalized_segment)"` | — |
| [SRC-59CF4B7DE8-L000189](../../agents/research.py#L189) | 189 | `"        ):"` | — |
| [SRC-59CF4B7DE8-L000190](../../agents/research.py#L190) | 190 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000191](../../agents/research.py#L191) | 191 | `"        if _SEARCH_META_START_RE.search(normalized_segment):"` | — |
| [SRC-59CF4B7DE8-L000192](../../agents/research.py#L192) | 192 | `"            # Keep a concrete topic when a \"use multiple sources\" directive"` | — |
| [SRC-59CF4B7DE8-L000193](../../agents/research.py#L193) | 193 | `"            # introduces the subject, but discard standalone formatting clauses."` | — |
| [SRC-59CF4B7DE8-L000194](../../agents/research.py#L194) | 194 | `"            preserved = _SEARCH_TOPIC_PRESERVING_META_PREFIX_RE.sub(\"\", segment, count=1).strip()"` | — |
| [SRC-59CF4B7DE8-L000195](../../agents/research.py#L195) | 195 | `"            if not preserved:"` | — |
| [SRC-59CF4B7DE8-L000196](../../agents/research.py#L196) | 196 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000197](../../agents/research.py#L197) | 197 | `"            if preserved == segment:"` | — |
| [SRC-59CF4B7DE8-L000198](../../agents/research.py#L198) | 198 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000199](../../agents/research.py#L199) | 199 | `"            segment = preserved"` | — |
| [SRC-59CF4B7DE8-L000200](../../agents/research.py#L200) | 200 | `"        segment = _SEARCH_META_TAIL_RE.sub(\"\", segment).strip()"` | — |
| [SRC-59CF4B7DE8-L000201](../../agents/research.py#L201) | 201 | `"        segment = _SEARCH_LEADING_ACTION_RE.sub(\"\", segment).strip()"` | — |
| [SRC-59CF4B7DE8-L000202](../../agents/research.py#L202) | 202 | `"        if segment:"` | — |
| [SRC-59CF4B7DE8-L000203](../../agents/research.py#L203) | 203 | `"            useful.append(segment)"` | — |
| [SRC-59CF4B7DE8-L000204](../../agents/research.py#L204) | 204 | `"    result = re.sub(r\"\\s+\", \" \", \" \".join(useful)).strip(\" \\t\\r\\n,،;؛\")"` | — |
| [SRC-59CF4B7DE8-L000205](../../agents/research.py#L205) | 205 | `"    if not result:"` | — |
| [SRC-59CF4B7DE8-L000206](../../agents/research.py#L206) | 206 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000207](../../agents/research.py#L207) | 207 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000208](../../agents/research.py#L208) | 208 | `"        max_chars = max(2, min(int(limit), MAX_QUERY_CHARS))"` | — |
| [SRC-59CF4B7DE8-L000209](../../agents/research.py#L209) | 209 | `"    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-59CF4B7DE8-L000210](../../agents/research.py#L210) | 210 | `"        max_chars = MAX_QUERY_CHARS"` | — |
| [SRC-59CF4B7DE8-L000211](../../agents/research.py#L211) | 211 | `"    if len(result) > max_chars:"` | — |
| [SRC-59CF4B7DE8-L000212](../../agents/research.py#L212) | 212 | `"        shortened = result[:max_chars]"` | — |
| [SRC-59CF4B7DE8-L000213](../../agents/research.py#L213) | 213 | `"        result = shortened.rsplit(\" \", 1)[0] if \" \" in shortened else shortened"` | — |
| [SRC-59CF4B7DE8-L000214](../../agents/research.py#L214) | 214 | `"    return result"` | — |
| [SRC-59CF4B7DE8-L000215](../../agents/research.py#L215) | 215 | `""` | — |
| [SRC-59CF4B7DE8-L000216](../../agents/research.py#L216) | 216 | `""` | — |
| [SRC-59CF4B7DE8-L000217](../../agents/research.py#L217) | 217 | `"_ARABIC_RE = re.compile(r\"[؀-ۿ]\")"` | — |
| [SRC-59CF4B7DE8-L000218](../../agents/research.py#L218) | 218 | `""` | — |
| [SRC-59CF4B7DE8-L000219](../../agents/research.py#L219) | 219 | `""` | — |
| [SRC-59CF4B7DE8-L000220](../../agents/research.py#L220) | 220 | `"def _normalize_arabic(text: str) -> str:"` | — |
| [SRC-59CF4B7DE8-L000221](../../agents/research.py#L221) | 221 | `"    if not text:"` | — |
| [SRC-59CF4B7DE8-L000222](../../agents/research.py#L222) | 222 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000223](../../agents/research.py#L223) | 223 | `"    return (text.replace(\"\\u0623\", \"\\u0627\")"` | — |
| [SRC-59CF4B7DE8-L000224](../../agents/research.py#L224) | 224 | `"                .replace(\"\\u0625\", \"\\u0627\")"` | — |
| [SRC-59CF4B7DE8-L000225](../../agents/research.py#L225) | 225 | `"                .replace(\"\\u0622\", \"\\u0627\")"` | — |
| [SRC-59CF4B7DE8-L000226](../../agents/research.py#L226) | 226 | `"                .replace(\"\\u0629\", \"\\u0647\")"` | — |
| [SRC-59CF4B7DE8-L000227](../../agents/research.py#L227) | 227 | `"                .replace(\"\\u0649\", \"\\u064a\"))"` | — |
| [SRC-59CF4B7DE8-L000228](../../agents/research.py#L228) | 228 | `""` | — |
| [SRC-59CF4B7DE8-L000229](../../agents/research.py#L229) | 229 | `""` | — |
| [SRC-59CF4B7DE8-L000230](../../agents/research.py#L230) | 230 | `"def _contains_any(text: str, terms: tuple) -> bool:"` | — |
| [SRC-59CF4B7DE8-L000231](../../agents/research.py#L231) | 231 | `"    if not text:"` | — |
| [SRC-59CF4B7DE8-L000232](../../agents/research.py#L232) | 232 | `"        return False"` | — |
| [SRC-59CF4B7DE8-L000233](../../agents/research.py#L233) | 233 | `"    haystack = _normalize_arabic(text.casefold())"` | — |
| [SRC-59CF4B7DE8-L000234](../../agents/research.py#L234) | 234 | `"    for term in terms:"` | — |
| [SRC-59CF4B7DE8-L000235](../../agents/research.py#L235) | 235 | `"        if not term:"` | — |
| [SRC-59CF4B7DE8-L000236](../../agents/research.py#L236) | 236 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000237](../../agents/research.py#L237) | 237 | `"        t = _normalize_arabic(term.casefold())"` | — |
| [SRC-59CF4B7DE8-L000238](../../agents/research.py#L238) | 238 | `"        if _ARABIC_RE.search(t):"` | — |
| [SRC-59CF4B7DE8-L000239](../../agents/research.py#L239) | 239 | `"            if t in haystack:"` | — |
| [SRC-59CF4B7DE8-L000240](../../agents/research.py#L240) | 240 | `"                return True"` | — |
| [SRC-59CF4B7DE8-L000241](../../agents/research.py#L241) | 241 | `"        else:"` | — |
| [SRC-59CF4B7DE8-L000242](../../agents/research.py#L242) | 242 | `"            pat = r\"(?<![a-zA-Z0-9])\" + re.escape(t) + r\"(?![a-zA-Z0-9])\""` | — |
| [SRC-59CF4B7DE8-L000243](../../agents/research.py#L243) | 243 | `"            if re.search(pat, haystack):"` | — |
| [SRC-59CF4B7DE8-L000244](../../agents/research.py#L244) | 244 | `"                return True"` | — |
| [SRC-59CF4B7DE8-L000245](../../agents/research.py#L245) | 245 | `"    return False"` | — |
| [SRC-59CF4B7DE8-L000246](../../agents/research.py#L246) | 246 | `""` | — |
| [SRC-59CF4B7DE8-L000247](../../agents/research.py#L247) | 247 | `""` | — |
| [SRC-59CF4B7DE8-L000248](../../agents/research.py#L248) | 248 | `"def detect_social_focus(question: str, history: list[dict[str, str]] \| None = None) -> bool:"` | — |
| [SRC-59CF4B7DE8-L000249](../../agents/research.py#L249) | 249 | `"    context = question + \" \" + \" \".join("` | — |
| [SRC-59CF4B7DE8-L000250](../../agents/research.py#L250) | 250 | `"        item.get(\"content\", \"\") for item in (history or [])[-4:]"` | — |
| [SRC-59CF4B7DE8-L000251](../../agents/research.py#L251) | 251 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000252](../../agents/research.py#L252) | 252 | `"    return _contains_any(context, _SOCIAL_TERMS)"` | — |
| [SRC-59CF4B7DE8-L000253](../../agents/research.py#L253) | 253 | `""` | — |
| [SRC-59CF4B7DE8-L000254](../../agents/research.py#L254) | 254 | `""` | — |
| [SRC-59CF4B7DE8-L000255](../../agents/research.py#L255) | 255 | `"def detect_freshness(question: str) -> bool:"` | — |
| [SRC-59CF4B7DE8-L000256](../../agents/research.py#L256) | 256 | `"    return _contains_any(question, _FRESH_TERMS)"` | — |
| [SRC-59CF4B7DE8-L000257](../../agents/research.py#L257) | 257 | `""` | — |
| [SRC-59CF4B7DE8-L000258](../../agents/research.py#L258) | 258 | `""` | — |
| [SRC-59CF4B7DE8-L000259](../../agents/research.py#L259) | 259 | `"def detect_depth(question: str) -> str:"` | — |
| [SRC-59CF4B7DE8-L000260](../../agents/research.py#L260) | 260 | `"    return \"deep\" if _contains_any(question, _DEEP_TERMS) else \"standard\""` | — |
| [SRC-59CF4B7DE8-L000261](../../agents/research.py#L261) | 261 | `""` | — |
| [SRC-59CF4B7DE8-L000262](../../agents/research.py#L262) | 262 | `""` | — |
| [SRC-59CF4B7DE8-L000263](../../agents/research.py#L263) | 263 | `"def mentioned_social_platforms(text: str) -> list[str]:"` | — |
| [SRC-59CF4B7DE8-L000264](../../agents/research.py#L264) | 264 | `"    rules = ("` | — |
| [SRC-59CF4B7DE8-L000265](../../agents/research.py#L265) | 265 | `"        (\"reddit\", (\"reddit\", \"ريديت\")),"` | — |
| [SRC-59CF4B7DE8-L000266](../../agents/research.py#L266) | 266 | `"        (\"youtube\", (\"youtube\", \"يوتيوب\")),"` | — |
| [SRC-59CF4B7DE8-L000267](../../agents/research.py#L267) | 267 | `"        (\"facebook\", (\"facebook\", \"فيسبوك\", \"فيس بوك\")),"` | — |
| [SRC-59CF4B7DE8-L000268](../../agents/research.py#L268) | 268 | `"        (\"instagram\", (\"instagram\", \"انستجرام\", \"إنستجرام\")),"` | — |
| [SRC-59CF4B7DE8-L000269](../../agents/research.py#L269) | 269 | `"        (\"x\", (\"x.com\", \"twitter\", \"تويتر\", \"اكس\", \"إكس\")),"` | — |
| [SRC-59CF4B7DE8-L000270](../../agents/research.py#L270) | 270 | `"        (\"tiktok\", (\"tiktok\", \"تيك توك\")),"` | — |
| [SRC-59CF4B7DE8-L000271](../../agents/research.py#L271) | 271 | `"        (\"linkedin\", (\"linkedin\", \"لينكدان\", \"لينكدإن\")),"` | — |
| [SRC-59CF4B7DE8-L000272](../../agents/research.py#L272) | 272 | `"        (\"threads\", (\"threads\", \"ثريدز\")),"` | — |
| [SRC-59CF4B7DE8-L000273](../../agents/research.py#L273) | 273 | `"        (\"bluesky\", (\"bluesky\", \"بلو سكاي\")),"` | — |
| [SRC-59CF4B7DE8-L000274](../../agents/research.py#L274) | 274 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000275](../../agents/research.py#L275) | 275 | `"    low = text.casefold()"` | — |
| [SRC-59CF4B7DE8-L000276](../../agents/research.py#L276) | 276 | `"    return [name for name, aliases in rules if any(alias.casefold() in low for alias in aliases)]"` | — |
| [SRC-59CF4B7DE8-L000277](../../agents/research.py#L277) | 277 | `""` | — |
| [SRC-59CF4B7DE8-L000278](../../agents/research.py#L278) | 278 | `""` | — |
| [SRC-59CF4B7DE8-L000279](../../agents/research.py#L279) | 279 | `"def fallback_plan("` | — |
| [SRC-59CF4B7DE8-L000280](../../agents/research.py#L280) | 280 | `"    question: str, history: list[dict[str, str]] \| None = None"` | — |
| [SRC-59CF4B7DE8-L000281](../../agents/research.py#L281) | 281 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000282](../../agents/research.py#L282) | 282 | `"    \"\"\"Build a small but varied plan when no model planner is configured or parsing fails.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000283](../../agents/research.py#L283) | 283 | `"    contextual_question = resolve_followup_query(question, history)"` | — |
| [SRC-59CF4B7DE8-L000284](../../agents/research.py#L284) | 284 | `"    direct_urls = extract_urls(question)"` | — |
| [SRC-59CF4B7DE8-L000285](../../agents/research.py#L285) | 285 | `"    base = compact_search_query(contextual_question)"` | — |
| [SRC-59CF4B7DE8-L000286](../../agents/research.py#L286) | 286 | `"    social_focus = detect_social_focus(question, history)"` | — |
| [SRC-59CF4B7DE8-L000287](../../agents/research.py#L287) | 287 | `"    fresh = detect_freshness(question)"` | — |
| [SRC-59CF4B7DE8-L000288](../../agents/research.py#L288) | 288 | `"    detected_depth = detect_depth(question)"` | — |
| [SRC-59CF4B7DE8-L000289](../../agents/research.py#L289) | 289 | `"    deep = detected_depth == \"deep\""` | — |
| [SRC-59CF4B7DE8-L000290](../../agents/research.py#L290) | 290 | `"    platforms = mentioned_social_platforms(question + \" \" + \" \".join("` | — |
| [SRC-59CF4B7DE8-L000291](../../agents/research.py#L291) | 291 | `"        item.get(\"content\", \"\") for item in (history or [])[-4:]"` | — |
| [SRC-59CF4B7DE8-L000292](../../agents/research.py#L292) | 292 | `"    ))"` | — |
| [SRC-59CF4B7DE8-L000293](../../agents/research.py#L293) | 293 | `"    queries: list[str] = [base] if base else []"` | — |
| [SRC-59CF4B7DE8-L000294](../../agents/research.py#L294) | 294 | `""` | — |
| [SRC-59CF4B7DE8-L000295](../../agents/research.py#L295) | 295 | `"    if fresh and base:"` | — |
| [SRC-59CF4B7DE8-L000296](../../agents/research.py#L296) | 296 | `"        queries.append(compact_search_query(base + \" أحدث مستجدات آخر الأخبار\"))"` | — |
| [SRC-59CF4B7DE8-L000297](../../agents/research.py#L297) | 297 | `"    if base and _contains_any(question, (\"قارن\", \"مقارنة\", \"compare\", \"versus\", \"vs\", \"الفرق بين\")):"` | — |
| [SRC-59CF4B7DE8-L000298](../../agents/research.py#L298) | 298 | `"        queries.append(compact_search_query(base + \" مقارنة مراجعات مميزات عيوب\"))"` | — |
| [SRC-59CF4B7DE8-L000299](../../agents/research.py#L299) | 299 | `""` | — |
| [SRC-59CF4B7DE8-L000300](../../agents/research.py#L300) | 300 | `"    if social_focus and base:"` | — |
| [SRC-59CF4B7DE8-L000301](../../agents/research.py#L301) | 301 | `"        selected = platforms or [\"facebook\", \"instagram\", \"reddit\"]"` | — |
| [SRC-59CF4B7DE8-L000302](../../agents/research.py#L302) | 302 | `"        for platform in selected[:3]:"` | — |
| [SRC-59CF4B7DE8-L000303](../../agents/research.py#L303) | 303 | `"            domain = SOCIAL_DOMAINS[platform]"` | — |
| [SRC-59CF4B7DE8-L000304](../../agents/research.py#L304) | 304 | `"            site_query = compact_search_query(f\"site:{domain} {base}\")"` | — |
| [SRC-59CF4B7DE8-L000305](../../agents/research.py#L305) | 305 | `"            if site_query not in queries:"` | — |
| [SRC-59CF4B7DE8-L000306](../../agents/research.py#L306) | 306 | `"                queries.append(site_query)"` | — |
| [SRC-59CF4B7DE8-L000307](../../agents/research.py#L307) | 307 | `""` | — |
| [SRC-59CF4B7DE8-L000308](../../agents/research.py#L308) | 308 | `"    if deep and base and not social_focus and len(queries) < MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000309](../../agents/research.py#L309) | 309 | `"        queries.append(compact_search_query(base + \" مصادر موثوقة تقارير إحصاءات\"))"` | — |
| [SRC-59CF4B7DE8-L000310](../../agents/research.py#L310) | 310 | `""` | — |
| [SRC-59CF4B7DE8-L000311](../../agents/research.py#L311) | 311 | `"    unique: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000312](../../agents/research.py#L312) | 312 | `"    seen: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000313](../../agents/research.py#L313) | 313 | `"    for query in queries:"` | — |
| [SRC-59CF4B7DE8-L000314](../../agents/research.py#L314) | 314 | `"        value = compact_search_query(query)"` | — |
| [SRC-59CF4B7DE8-L000315](../../agents/research.py#L315) | 315 | `"        key = value.casefold()"` | — |
| [SRC-59CF4B7DE8-L000316](../../agents/research.py#L316) | 316 | `"        if value and key not in seen:"` | — |
| [SRC-59CF4B7DE8-L000317](../../agents/research.py#L317) | 317 | `"            unique.append(value)"` | — |
| [SRC-59CF4B7DE8-L000318](../../agents/research.py#L318) | 318 | `"            seen.add(key)"` | — |
| [SRC-59CF4B7DE8-L000319](../../agents/research.py#L319) | 319 | `"        if len(unique) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000320](../../agents/research.py#L320) | 320 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000321](../../agents/research.py#L321) | 321 | `""` | — |
| [SRC-59CF4B7DE8-L000322](../../agents/research.py#L322) | 322 | `"    return {"` | — |
| [SRC-59CF4B7DE8-L000323](../../agents/research.py#L323) | 323 | `"        \"queries\": unique or ([base] if base else []),"` | — |
| [SRC-59CF4B7DE8-L000324](../../agents/research.py#L324) | 324 | `"        \"direct_urls\": direct_urls,"` | — |
| [SRC-59CF4B7DE8-L000325](../../agents/research.py#L325) | 325 | `"        \"social_focus\": social_focus,"` | — |
| [SRC-59CF4B7DE8-L000326](../../agents/research.py#L326) | 326 | `"        \"freshness\": \"current\" if fresh else \"any\","` | — |
| [SRC-59CF4B7DE8-L000327](../../agents/research.py#L327) | 327 | `"        \"depth\": detected_depth,"` | — |
| [SRC-59CF4B7DE8-L000328](../../agents/research.py#L328) | 328 | `"        \"platforms\": platforms,"` | — |
| [SRC-59CF4B7DE8-L000329](../../agents/research.py#L329) | 329 | `"        \"planning_method\": \"deterministic_fallback\","` | — |
| [SRC-59CF4B7DE8-L000330](../../agents/research.py#L330) | 330 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000331](../../agents/research.py#L331) | 331 | `""` | — |
| [SRC-59CF4B7DE8-L000332](../../agents/research.py#L332) | 332 | `""` | — |
| [SRC-59CF4B7DE8-L000333](../../agents/research.py#L333) | 333 | `"def validate_plan("` | — |
| [SRC-59CF4B7DE8-L000334](../../agents/research.py#L334) | 334 | `"    candidate: Any, question: str, history: list[dict[str, str]] \| None = None"` | — |
| [SRC-59CF4B7DE8-L000335](../../agents/research.py#L335) | 335 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000336](../../agents/research.py#L336) | 336 | `"    fallback = fallback_plan(question, history)"` | — |
| [SRC-59CF4B7DE8-L000337](../../agents/research.py#L337) | 337 | `"    if not isinstance(candidate, dict):"` | — |
| [SRC-59CF4B7DE8-L000338](../../agents/research.py#L338) | 338 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000339](../../agents/research.py#L339) | 339 | `"    raw_queries = candidate.get(\"queries\", [])"` | — |
| [SRC-59CF4B7DE8-L000340](../../agents/research.py#L340) | 340 | `"    if not isinstance(raw_queries, list):"` | — |
| [SRC-59CF4B7DE8-L000341](../../agents/research.py#L341) | 341 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000342](../../agents/research.py#L342) | 342 | `"    queries: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000343](../../agents/research.py#L343) | 343 | `"    seen: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000344](../../agents/research.py#L344) | 344 | `"    for item in raw_queries:"` | — |
| [SRC-59CF4B7DE8-L000345](../../agents/research.py#L345) | 345 | `"        query = compact_search_query(item)"` | — |
| [SRC-59CF4B7DE8-L000346](../../agents/research.py#L346) | 346 | `"        # Never accept prompt-like multi-line payloads as search-query instructions."` | — |
| [SRC-59CF4B7DE8-L000347](../../agents/research.py#L347) | 347 | `"        query = query.replace(\"\\n\", \" \").replace(\"\\r\", \" \")"` | — |
| [SRC-59CF4B7DE8-L000348](../../agents/research.py#L348) | 348 | `"        if len(query) < 2:"` | — |
| [SRC-59CF4B7DE8-L000349](../../agents/research.py#L349) | 349 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000350](../../agents/research.py#L350) | 350 | `"        if query.casefold() not in seen:"` | — |
| [SRC-59CF4B7DE8-L000351](../../agents/research.py#L351) | 351 | `"            seen.add(query.casefold())"` | — |
| [SRC-59CF4B7DE8-L000352](../../agents/research.py#L352) | 352 | `"            queries.append(query)"` | — |
| [SRC-59CF4B7DE8-L000353](../../agents/research.py#L353) | 353 | `"        if len(queries) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000354](../../agents/research.py#L354) | 354 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000355](../../agents/research.py#L355) | 355 | `"    if not queries:"` | — |
| [SRC-59CF4B7DE8-L000356](../../agents/research.py#L356) | 356 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000357](../../agents/research.py#L357) | 357 | `"    base = fallback_plan(question, history)"` | — |
| [SRC-59CF4B7DE8-L000358](../../agents/research.py#L358) | 358 | `"    platforms = candidate.get(\"platforms\")"` | — |
| [SRC-59CF4B7DE8-L000359](../../agents/research.py#L359) | 359 | `"    if not isinstance(platforms, list):"` | — |
| [SRC-59CF4B7DE8-L000360](../../agents/research.py#L360) | 360 | `"        platforms = base[\"platforms\"]"` | — |
| [SRC-59CF4B7DE8-L000361](../../agents/research.py#L361) | 361 | `"    safe_platforms = [p for p in platforms if isinstance(p, str) and p in SOCIAL_DOMAINS]"` | — |
| [SRC-59CF4B7DE8-L000362](../../agents/research.py#L362) | 362 | `"    return {"` | — |
| [SRC-59CF4B7DE8-L000363](../../agents/research.py#L363) | 363 | `"        \"queries\": queries,"` | — |
| [SRC-59CF4B7DE8-L000364](../../agents/research.py#L364) | 364 | `"        \"direct_urls\": fallback[\"direct_urls\"],"` | — |
| [SRC-59CF4B7DE8-L000365](../../agents/research.py#L365) | 365 | `"        \"social_focus\": bool(candidate.get(\"social_focus\", base[\"social_focus\"])),"` | — |
| [SRC-59CF4B7DE8-L000366](../../agents/research.py#L366) | 366 | `"        \"freshness\": \"current\" if candidate.get(\"freshness\") == \"current\" else base[\"freshness\"],"` | — |
| [SRC-59CF4B7DE8-L000367](../../agents/research.py#L367) | 367 | `"        \"depth\": \"deep\" if candidate.get(\"depth\") == \"deep\" else base[\"depth\"],"` | — |
| [SRC-59CF4B7DE8-L000368](../../agents/research.py#L368) | 368 | `"        \"platforms\": list(dict.fromkeys(safe_platforms))[:5],"` | — |
| [SRC-59CF4B7DE8-L000369](../../agents/research.py#L369) | 369 | `"        \"planning_method\": \"language_model\","` | — |
| [SRC-59CF4B7DE8-L000370](../../agents/research.py#L370) | 370 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000371](../../agents/research.py#L371) | 371 | `""` | — |
| [SRC-59CF4B7DE8-L000372](../../agents/research.py#L372) | 372 | `""` | — |
| [SRC-59CF4B7DE8-L000373](../../agents/research.py#L373) | 373 | `"def _canonical_result_url(url: str) -> str:"` | — |
| [SRC-59CF4B7DE8-L000374](../../agents/research.py#L374) | 374 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000375](../../agents/research.py#L375) | 375 | `"        parsed = urlparse(url)"` | — |
| [SRC-59CF4B7DE8-L000376](../../agents/research.py#L376) | 376 | `"        host = (parsed.hostname or \"\").lower().removeprefix(\"www.\")"` | — |
| [SRC-59CF4B7DE8-L000377](../../agents/research.py#L377) | 377 | `"        # Drop fragments and common tracking query parameters before deduplication."` | — |
| [SRC-59CF4B7DE8-L000378](../../agents/research.py#L378) | 378 | `"        parts = []"` | — |
| [SRC-59CF4B7DE8-L000379](../../agents/research.py#L379) | 379 | `"        for part in parsed.query.split(\"&\"):"` | — |
| [SRC-59CF4B7DE8-L000380](../../agents/research.py#L380) | 380 | `"            key = part.split(\"=\", 1)[0].lower()"` | — |
| [SRC-59CF4B7DE8-L000381](../../agents/research.py#L381) | 381 | `"            if key.startswith(\"utm_\") or key in {\"fbclid\", \"gclid\", \"ref\", \"ref_src\"}:"` | — |
| [SRC-59CF4B7DE8-L000382](../../agents/research.py#L382) | 382 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000383](../../agents/research.py#L383) | 383 | `"            if part:"` | — |
| [SRC-59CF4B7DE8-L000384](../../agents/research.py#L384) | 384 | `"                parts.append(part)"` | — |
| [SRC-59CF4B7DE8-L000385](../../agents/research.py#L385) | 385 | `"        query = \"&\".join(sorted(parts))"` | — |
| [SRC-59CF4B7DE8-L000386](../../agents/research.py#L386) | 386 | `"        path = parsed.path.rstrip(\"/\") or \"/\""` | — |
| [SRC-59CF4B7DE8-L000387](../../agents/research.py#L387) | 387 | `"        return f\"{parsed.scheme.lower()}://{host}{path}\" + (f\"?{query}\" if query else \"\")"` | — |
| [SRC-59CF4B7DE8-L000388](../../agents/research.py#L388) | 388 | `"    except (ValueError, TypeError):"` | — |
| [SRC-59CF4B7DE8-L000389](../../agents/research.py#L389) | 389 | `"        return url"` | — |
| [SRC-59CF4B7DE8-L000390](../../agents/research.py#L390) | 390 | `""` | — |
| [SRC-59CF4B7DE8-L000391](../../agents/research.py#L391) | 391 | `""` | — |
| [SRC-59CF4B7DE8-L000392](../../agents/research.py#L392) | 392 | `"def classify_source(url: str) -> dict[str, str]:"` | — |
| [SRC-59CF4B7DE8-L000393](../../agents/research.py#L393) | 393 | `"    host = (urlparse(url).hostname or \"\").lower().removeprefix(\"www.\")"` | — |
| [SRC-59CF4B7DE8-L000394](../../agents/research.py#L394) | 394 | `"    platform = \"web\""` | — |
| [SRC-59CF4B7DE8-L000395](../../agents/research.py#L395) | 395 | `"    mapping = {"` | — |
| [SRC-59CF4B7DE8-L000396](../../agents/research.py#L396) | 396 | `"        \"reddit.com\": \"reddit\", \"old.reddit.com\": \"reddit\","` | — |
| [SRC-59CF4B7DE8-L000397](../../agents/research.py#L397) | 397 | `"        \"youtube.com\": \"youtube\", \"youtu.be\": \"youtube\","` | — |
| [SRC-59CF4B7DE8-L000398](../../agents/research.py#L398) | 398 | `"        \"facebook.com\": \"facebook\", \"instagram.com\": \"instagram\","` | — |
| [SRC-59CF4B7DE8-L000399](../../agents/research.py#L399) | 399 | `"        \"x.com\": \"x\", \"twitter.com\": \"x\", \"tiktok.com\": \"tiktok\","` | — |
| [SRC-59CF4B7DE8-L000400](../../agents/research.py#L400) | 400 | `"        \"linkedin.com\": \"linkedin\", \"threads.net\": \"threads\","` | — |
| [SRC-59CF4B7DE8-L000401](../../agents/research.py#L401) | 401 | `"        \"bsky.app\": \"bluesky\","` | — |
| [SRC-59CF4B7DE8-L000402](../../agents/research.py#L402) | 402 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000403](../../agents/research.py#L403) | 403 | `"    for domain, label in mapping.items():"` | — |
| [SRC-59CF4B7DE8-L000404](../../agents/research.py#L404) | 404 | `"        if host == domain or host.endswith(\".\" + domain):"` | — |
| [SRC-59CF4B7DE8-L000405](../../agents/research.py#L405) | 405 | `"            platform = label"` | — |
| [SRC-59CF4B7DE8-L000406](../../agents/research.py#L406) | 406 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000407](../../agents/research.py#L407) | 407 | `"    trust = \"general\""` | — |
| [SRC-59CF4B7DE8-L000408](../../agents/research.py#L408) | 408 | `"    if host.endswith((\".gov\", \".gov.eg\", \".gov.uk\")):"` | — |
| [SRC-59CF4B7DE8-L000409](../../agents/research.py#L409) | 409 | `"        trust = \"government\""` | — |
| [SRC-59CF4B7DE8-L000410](../../agents/research.py#L410) | 410 | `"    elif host.endswith((\".edu\", \".ac.uk\", \".edu.eg\")):"` | — |
| [SRC-59CF4B7DE8-L000411](../../agents/research.py#L411) | 411 | `"        trust = \"academic\""` | — |
| [SRC-59CF4B7DE8-L000412](../../agents/research.py#L412) | 412 | `"    elif host == \"news.google.com\" or any("` | — |
| [SRC-59CF4B7DE8-L000413](../../agents/research.py#L413) | 413 | `"        name in host"` | — |
| [SRC-59CF4B7DE8-L000414](../../agents/research.py#L414) | 414 | `"        for name in ("` | — |
| [SRC-59CF4B7DE8-L000415](../../agents/research.py#L415) | 415 | `"            \"reuters.com\", \"apnews.com\", \"bbc.com\", \"bbc.co.uk\","` | — |
| [SRC-59CF4B7DE8-L000416](../../agents/research.py#L416) | 416 | `"            \"ft.com\", \"nytimes.com\", \"theguardian.com\","` | — |
| [SRC-59CF4B7DE8-L000417](../../agents/research.py#L417) | 417 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000418](../../agents/research.py#L418) | 418 | `"    ):"` | — |
| [SRC-59CF4B7DE8-L000419](../../agents/research.py#L419) | 419 | `"        trust = \"news\""` | — |
| [SRC-59CF4B7DE8-L000420](../../agents/research.py#L420) | 420 | `"    elif platform != \"web\":"` | — |
| [SRC-59CF4B7DE8-L000421](../../agents/research.py#L421) | 421 | `"        trust = \"social\""` | — |
| [SRC-59CF4B7DE8-L000422](../../agents/research.py#L422) | 422 | `"    return {\"domain\": host, \"platform\": platform, \"source_class\": trust}"` | — |
| [SRC-59CF4B7DE8-L000423](../../agents/research.py#L423) | 423 | `""` | — |
| [SRC-59CF4B7DE8-L000424](../../agents/research.py#L424) | 424 | `""` | — |
| [SRC-59CF4B7DE8-L000425](../../agents/research.py#L425) | 425 | `"def fuse_ranked_results("` | — |
| [SRC-59CF4B7DE8-L000426](../../agents/research.py#L426) | 426 | `"    batches: list[dict[str, Any]], limit: int = MAX_FUSED_RESULTS"` | — |
| [SRC-59CF4B7DE8-L000427](../../agents/research.py#L427) | 427 | `") -> list[dict[str, Any]]:"` | — |
| [SRC-59CF4B7DE8-L000428](../../agents/research.py#L428) | 428 | `"    \"\"\"Reciprocal-rank-fuse result sets across queries/providers and dedupe URLs.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000429](../../agents/research.py#L429) | 429 | `"    accumulated: dict[str, dict[str, Any]] = {}"` | — |
| [SRC-59CF4B7DE8-L000430](../../agents/research.py#L430) | 430 | `"    for batch in batches:"` | — |
| [SRC-59CF4B7DE8-L000431](../../agents/research.py#L431) | 431 | `"        query = _compact(batch.get(\"query\", \"\"), 500)"` | — |
| [SRC-59CF4B7DE8-L000432](../../agents/research.py#L432) | 432 | `"        provider = _compact(batch.get(\"provider\", \"search\"), 80)"` | — |
| [SRC-59CF4B7DE8-L000433](../../agents/research.py#L433) | 433 | `"        results = batch.get(\"results\", [])"` | — |
| [SRC-59CF4B7DE8-L000434](../../agents/research.py#L434) | 434 | `"        if not isinstance(results, list):"` | — |
| [SRC-59CF4B7DE8-L000435](../../agents/research.py#L435) | 435 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000436](../../agents/research.py#L436) | 436 | `"        for position, source in enumerate(results, 1):"` | — |
| [SRC-59CF4B7DE8-L000437](../../agents/research.py#L437) | 437 | `"            if not isinstance(source, dict) or not source.get(\"url\"):"` | — |
| [SRC-59CF4B7DE8-L000438](../../agents/research.py#L438) | 438 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000439](../../agents/research.py#L439) | 439 | `"            url = _canonical_result_url(str(source[\"url\"]))"` | — |
| [SRC-59CF4B7DE8-L000440](../../agents/research.py#L440) | 440 | `"            if not url.startswith((\"https://\", \"http://\")):"` | — |
| [SRC-59CF4B7DE8-L000441](../../agents/research.py#L441) | 441 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000442](../../agents/research.py#L442) | 442 | `"            entry = accumulated.get(url)"` | — |
| [SRC-59CF4B7DE8-L000443](../../agents/research.py#L443) | 443 | `"            if entry is None:"` | — |
| [SRC-59CF4B7DE8-L000444](../../agents/research.py#L444) | 444 | `"                publisher_url = _compact(source.get(\"publisher_url\") or \"\", 2048)"` | — |
| [SRC-59CF4B7DE8-L000445](../../agents/research.py#L445) | 445 | `"                source_identity_url = publisher_url or str(source[\"url\"])"` | — |
| [SRC-59CF4B7DE8-L000446](../../agents/research.py#L446) | 446 | `"                entry = {"` | — |
| [SRC-59CF4B7DE8-L000447](../../agents/research.py#L447) | 447 | `"                    \"title\": _compact(source.get(\"title\") or \"نتيجة ويب\", 300),"` | — |
| [SRC-59CF4B7DE8-L000448](../../agents/research.py#L448) | 448 | `"                    \"url\": str(source[\"url\"]),"` | — |
| [SRC-59CF4B7DE8-L000449](../../agents/research.py#L449) | 449 | `"                    \"snippet\": _compact(source.get(\"snippet\") or \"\", 1800),"` | — |
| [SRC-59CF4B7DE8-L000450](../../agents/research.py#L450) | 450 | `"                    \"page_text\": _compact(source.get(\"page_text\") or \"\", 12_000),"` | — |
| [SRC-59CF4B7DE8-L000451](../../agents/research.py#L451) | 451 | `"                    \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-59CF4B7DE8-L000452](../../agents/research.py#L452) | 452 | `"                    \"providers\": [],"` | — |
| [SRC-59CF4B7DE8-L000453](../../agents/research.py#L453) | 453 | `"                    \"queries\": [],"` | — |
| [SRC-59CF4B7DE8-L000454](../../agents/research.py#L454) | 454 | `"                    \"rank_score\": 0.0,"` | — |
| [SRC-59CF4B7DE8-L000455](../../agents/research.py#L455) | 455 | `"                    \"best_raw_rank\": position,"` | — |
| [SRC-59CF4B7DE8-L000456](../../agents/research.py#L456) | 456 | `"                    \"published_at\": _compact(source.get(\"published_at\") or \"\", 100),"` | — |
| [SRC-59CF4B7DE8-L000457](../../agents/research.py#L457) | 457 | `"                    \"publisher_name\": _compact(source.get(\"publisher_name\") or \"\", 200),"` | — |
| [SRC-59CF4B7DE8-L000458](../../agents/research.py#L458) | 458 | `"                    \"publisher_url\": publisher_url,"` | — |
| [SRC-59CF4B7DE8-L000459](../../agents/research.py#L459) | 459 | `"                    \"publisher_domain\": _compact(source.get(\"publisher_domain\") or \"\", 300),"` | — |
| [SRC-59CF4B7DE8-L000460](../../agents/research.py#L460) | 460 | `"                }"` | — |
| [SRC-59CF4B7DE8-L000461](../../agents/research.py#L461) | 461 | `"                entry.update(classify_source(source_identity_url))"` | — |
| [SRC-59CF4B7DE8-L000462](../../agents/research.py#L462) | 462 | `"                accumulated[url] = entry"` | — |
| [SRC-59CF4B7DE8-L000463](../../agents/research.py#L463) | 463 | `"            elif source.get(\"publisher_url\") and not entry.get(\"publisher_url\"):"` | — |
| [SRC-59CF4B7DE8-L000464](../../agents/research.py#L464) | 464 | `"                entry[\"publisher_url\"] = _compact(source.get(\"publisher_url\"), 2048)"` | — |
| [SRC-59CF4B7DE8-L000465](../../agents/research.py#L465) | 465 | `"                entry[\"publisher_name\"] = _compact(source.get(\"publisher_name\") or \"\", 200)"` | — |
| [SRC-59CF4B7DE8-L000466](../../agents/research.py#L466) | 466 | `"                entry[\"publisher_domain\"] = _compact(source.get(\"publisher_domain\") or \"\", 300)"` | — |
| [SRC-59CF4B7DE8-L000467](../../agents/research.py#L467) | 467 | `"                entry.update(classify_source(entry[\"publisher_url\"]))"` | — |
| [SRC-59CF4B7DE8-L000468](../../agents/research.py#L468) | 468 | `"            entry[\"rank_score\"] += 1.0 / (60 + position)"` | — |
| [SRC-59CF4B7DE8-L000469](../../agents/research.py#L469) | 469 | `"            entry[\"best_raw_rank\"] = min(entry[\"best_raw_rank\"], position)"` | — |
| [SRC-59CF4B7DE8-L000470](../../agents/research.py#L470) | 470 | `"            if provider and provider not in entry[\"providers\"]:"` | — |
| [SRC-59CF4B7DE8-L000471](../../agents/research.py#L471) | 471 | `"                entry[\"providers\"].append(provider)"` | — |
| [SRC-59CF4B7DE8-L000472](../../agents/research.py#L472) | 472 | `"            if query and query not in entry[\"queries\"]:"` | — |
| [SRC-59CF4B7DE8-L000473](../../agents/research.py#L473) | 473 | `"                entry[\"queries\"].append(query)"` | — |
| [SRC-59CF4B7DE8-L000474](../../agents/research.py#L474) | 474 | `"            if len(str(source.get(\"snippet\") or \"\")) > len(entry[\"snippet\"]):"` | — |
| [SRC-59CF4B7DE8-L000475](../../agents/research.py#L475) | 475 | `"                entry[\"snippet\"] = _compact(source.get(\"snippet\"), 1800)"` | — |
| [SRC-59CF4B7DE8-L000476](../../agents/research.py#L476) | 476 | `"            if source.get(\"published_at\") and not entry.get(\"published_at\"):"` | — |
| [SRC-59CF4B7DE8-L000477](../../agents/research.py#L477) | 477 | `"                entry[\"published_at\"] = _compact(source[\"published_at\"], 100)"` | — |
| [SRC-59CF4B7DE8-L000478](../../agents/research.py#L478) | 478 | `"            if source.get(\"page_text\") and not entry[\"page_text\"]:"` | — |
| [SRC-59CF4B7DE8-L000479](../../agents/research.py#L479) | 479 | `"                entry[\"page_text\"] = _compact(source[\"page_text\"], 12_000)"` | — |
| [SRC-59CF4B7DE8-L000480](../../agents/research.py#L480) | 480 | `"                entry[\"page_fetched\"] = True"` | — |
| [SRC-59CF4B7DE8-L000481](../../agents/research.py#L481) | 481 | `"    # A cross-query result gets a modest consensus bonus; official/academic sources"` | — |
| [SRC-59CF4B7DE8-L000482](../../agents/research.py#L482) | 482 | `"    # get a small prior, never enough to override actual query relevance."` | — |
| [SRC-59CF4B7DE8-L000483](../../agents/research.py#L483) | 483 | `"    for entry in accumulated.values():"` | — |
| [SRC-59CF4B7DE8-L000484](../../agents/research.py#L484) | 484 | `"        entry[\"rank_score\"] += min(len(entry[\"queries\"]), 4) * 0.00015"` | — |
| [SRC-59CF4B7DE8-L000485](../../agents/research.py#L485) | 485 | `"        if entry[\"source_class\"] in {\"government\", \"academic\"}:"` | — |
| [SRC-59CF4B7DE8-L000486](../../agents/research.py#L486) | 486 | `"            entry[\"rank_score\"] += 0.0001"` | — |
| [SRC-59CF4B7DE8-L000487](../../agents/research.py#L487) | 487 | `"        if \"user_supplied_url\" in entry[\"providers\"]:"` | — |
| [SRC-59CF4B7DE8-L000488](../../agents/research.py#L488) | 488 | `"            entry[\"rank_score\"] += 0.5"` | — |
| [SRC-59CF4B7DE8-L000489](../../agents/research.py#L489) | 489 | `"    ranked = sorted(accumulated.values(), key=lambda item: item[\"rank_score\"], reverse=True)"` | — |
| [SRC-59CF4B7DE8-L000490](../../agents/research.py#L490) | 490 | `"    return ranked[:max(1, min(int(limit), MAX_FUSED_RESULTS))]"` | — |
| [SRC-59CF4B7DE8-L000491](../../agents/research.py#L491) | 491 | `""` | — |
| [SRC-59CF4B7DE8-L000492](../../agents/research.py#L492) | 492 | `""` | — |
| [SRC-59CF4B7DE8-L000493](../../agents/research.py#L493) | 493 | `""` | — |
| [SRC-59CF4B7DE8-L000494](../../agents/research.py#L494) | 494 | `"def _parse_publication_date(value: Any, now: datetime \| None = None) -> datetime \| None:"` | — |
| [SRC-59CF4B7DE8-L000495](../../agents/research.py#L495) | 495 | `"    \"\"\"Parse common search/RSS publication dates without guessing missing dates.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000496](../../agents/research.py#L496) | 496 | `"    if not isinstance(value, str) or not value.strip():"` | — |
| [SRC-59CF4B7DE8-L000497](../../agents/research.py#L497) | 497 | `"        return None"` | — |
| [SRC-59CF4B7DE8-L000498](../../agents/research.py#L498) | 498 | `"    raw = value.strip()"` | — |
| [SRC-59CF4B7DE8-L000499](../../agents/research.py#L499) | 499 | `"    current = now or datetime.now(UTC)"` | — |
| [SRC-59CF4B7DE8-L000500](../../agents/research.py#L500) | 500 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000501](../../agents/research.py#L501) | 501 | `"        parsed = parsedate_to_datetime(raw)"` | — |
| [SRC-59CF4B7DE8-L000502](../../agents/research.py#L502) | 502 | `"        if parsed:"` | — |
| [SRC-59CF4B7DE8-L000503](../../agents/research.py#L503) | 503 | `"            return parsed.replace(tzinfo=parsed.tzinfo or UTC).astimezone(UTC)"` | — |
| [SRC-59CF4B7DE8-L000504](../../agents/research.py#L504) | 504 | `"    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-59CF4B7DE8-L000505](../../agents/research.py#L505) | 505 | `"        pass"` | — |
| [SRC-59CF4B7DE8-L000506](../../agents/research.py#L506) | 506 | `"    iso_value = raw.replace(\"Z\", \"+00:00\")"` | — |
| [SRC-59CF4B7DE8-L000507](../../agents/research.py#L507) | 507 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000508](../../agents/research.py#L508) | 508 | `"        parsed = datetime.fromisoformat(iso_value)"` | — |
| [SRC-59CF4B7DE8-L000509](../../agents/research.py#L509) | 509 | `"        return parsed.replace(tzinfo=parsed.tzinfo or UTC).astimezone(UTC)"` | — |
| [SRC-59CF4B7DE8-L000510](../../agents/research.py#L510) | 510 | `"    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-59CF4B7DE8-L000511](../../agents/research.py#L511) | 511 | `"        pass"` | — |
| [SRC-59CF4B7DE8-L000512](../../agents/research.py#L512) | 512 | `"    for date_format in (\"%b %d, %Y\", \"%B %d, %Y\", \"%Y/%m/%d\", \"%d %b %Y\"):"` | — |
| [SRC-59CF4B7DE8-L000513](../../agents/research.py#L513) | 513 | `"        try:"` | — |
| [SRC-59CF4B7DE8-L000514](../../agents/research.py#L514) | 514 | `"            return datetime.strptime(raw, date_format).replace(tzinfo=UTC)"` | — |
| [SRC-59CF4B7DE8-L000515](../../agents/research.py#L515) | 515 | `"        except ValueError:"` | — |
| [SRC-59CF4B7DE8-L000516](../../agents/research.py#L516) | 516 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000517](../../agents/research.py#L517) | 517 | `"    match = re.search(r\"(\\d+)\\s+(hour\|day\|week\|month\|year)s?\\s+ago\", raw, re.IGNORECASE)"` | — |
| [SRC-59CF4B7DE8-L000518](../../agents/research.py#L518) | 518 | `"    if match:"` | — |
| [SRC-59CF4B7DE8-L000519](../../agents/research.py#L519) | 519 | `"        amount = int(match.group(1))"` | — |
| [SRC-59CF4B7DE8-L000520](../../agents/research.py#L520) | 520 | `"        unit = match.group(2).lower()"` | — |
| [SRC-59CF4B7DE8-L000521](../../agents/research.py#L521) | 521 | `"        durations = {"` | — |
| [SRC-59CF4B7DE8-L000522](../../agents/research.py#L522) | 522 | `"            \"hour\": timedelta(hours=amount),"` | — |
| [SRC-59CF4B7DE8-L000523](../../agents/research.py#L523) | 523 | `"            \"day\": timedelta(days=amount),"` | — |
| [SRC-59CF4B7DE8-L000524](../../agents/research.py#L524) | 524 | `"            \"week\": timedelta(days=7 * amount),"` | — |
| [SRC-59CF4B7DE8-L000525](../../agents/research.py#L525) | 525 | `"            \"month\": timedelta(days=30 * amount),"` | — |
| [SRC-59CF4B7DE8-L000526](../../agents/research.py#L526) | 526 | `"            \"year\": timedelta(days=365 * amount),"` | — |
| [SRC-59CF4B7DE8-L000527](../../agents/research.py#L527) | 527 | `"        }"` | — |
| [SRC-59CF4B7DE8-L000528](../../agents/research.py#L528) | 528 | `"        return current - durations[unit]"` | — |
| [SRC-59CF4B7DE8-L000529](../../agents/research.py#L529) | 529 | `"    if raw.lower() in {\"today\", \"just now\", \"now\"}:"` | — |
| [SRC-59CF4B7DE8-L000530](../../agents/research.py#L530) | 530 | `"        return current"` | — |
| [SRC-59CF4B7DE8-L000531](../../agents/research.py#L531) | 531 | `"    if raw.lower() == \"yesterday\":"` | — |
| [SRC-59CF4B7DE8-L000532](../../agents/research.py#L532) | 532 | `"        return current - timedelta(days=1)"` | — |
| [SRC-59CF4B7DE8-L000533](../../agents/research.py#L533) | 533 | `"    return None"` | — |
| [SRC-59CF4B7DE8-L000534](../../agents/research.py#L534) | 534 | `""` | — |
| [SRC-59CF4B7DE8-L000535](../../agents/research.py#L535) | 535 | `""` | — |
| [SRC-59CF4B7DE8-L000536](../../agents/research.py#L536) | 536 | `"def evidence_signal_report("` | — |
| [SRC-59CF4B7DE8-L000537](../../agents/research.py#L537) | 537 | `"    sources: list[dict[str, Any]],"` | — |
| [SRC-59CF4B7DE8-L000538](../../agents/research.py#L538) | 538 | `"    freshness: str = \"any\","` | — |
| [SRC-59CF4B7DE8-L000539](../../agents/research.py#L539) | 539 | `"    now: datetime \| None = None,"` | — |
| [SRC-59CF4B7DE8-L000540](../../agents/research.py#L540) | 540 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000541](../../agents/research.py#L541) | 541 | `"    \"\"\"Summarize research coverage; signals describe evidence coverage, not factual truth.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000542](../../agents/research.py#L542) | 542 | `"    current = now or datetime.now(UTC)"` | — |
| [SRC-59CF4B7DE8-L000543](../../agents/research.py#L543) | 543 | `"    valid_sources = [source for source in sources if isinstance(source, dict) and source.get(\"url\")]"` | — |
| [SRC-59CF4B7DE8-L000544](../../agents/research.py#L544) | 544 | `"    domains = {"` | — |
| [SRC-59CF4B7DE8-L000545](../../agents/research.py#L545) | 545 | `"        registrable_domain("` | — |
| [SRC-59CF4B7DE8-L000546](../../agents/research.py#L546) | 546 | `"            source.get(\"domain\") or urlparse(str(source.get(\"url\") or \"\")).hostname or \"\""` | — |
| [SRC-59CF4B7DE8-L000547](../../agents/research.py#L547) | 547 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000548](../../agents/research.py#L548) | 548 | `"        for source in valid_sources"` | — |
| [SRC-59CF4B7DE8-L000549](../../agents/research.py#L549) | 549 | `"        if source.get(\"domain\") or source.get(\"url\")"` | — |
| [SRC-59CF4B7DE8-L000550](../../agents/research.py#L550) | 550 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000551](../../agents/research.py#L551) | 551 | `"    domains.discard(\"\")"` | — |
| [SRC-59CF4B7DE8-L000552](../../agents/research.py#L552) | 552 | `"    providers: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000553](../../agents/research.py#L553) | 553 | `"    for source in valid_sources:"` | — |
| [SRC-59CF4B7DE8-L000554](../../agents/research.py#L554) | 554 | `"        candidate_providers = source.get(\"providers\", [])"` | — |
| [SRC-59CF4B7DE8-L000555](../../agents/research.py#L555) | 555 | `"        if isinstance(candidate_providers, list):"` | — |
| [SRC-59CF4B7DE8-L000556](../../agents/research.py#L556) | 556 | `"            providers.update(str(item) for item in candidate_providers if item)"` | — |
| [SRC-59CF4B7DE8-L000557](../../agents/research.py#L557) | 557 | `"        elif source.get(\"provider\"):"` | — |
| [SRC-59CF4B7DE8-L000558](../../agents/research.py#L558) | 558 | `"            providers.add(str(source[\"provider\"]))"` | — |
| [SRC-59CF4B7DE8-L000559](../../agents/research.py#L559) | 559 | `"    classes = [str(source.get(\"source_class\") or \"general\") for source in valid_sources]"` | — |
| [SRC-59CF4B7DE8-L000560](../../agents/research.py#L560) | 560 | `"    primary_count = sum(item in {\"government\", \"academic\", \"official\"} for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000561](../../agents/research.py#L561) | 561 | `"    news_count = sum(item == \"news\" for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000562](../../agents/research.py#L562) | 562 | `"    social_count = sum(item == \"social\" for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000563](../../agents/research.py#L563) | 563 | `"    pages_read = sum(bool(source.get(\"page_fetched\")) for source in valid_sources)"` | — |
| [SRC-59CF4B7DE8-L000564](../../agents/research.py#L564) | 564 | `"    dates = ["` | — |
| [SRC-59CF4B7DE8-L000565](../../agents/research.py#L565) | 565 | `"        parsed"` | — |
| [SRC-59CF4B7DE8-L000566](../../agents/research.py#L566) | 566 | `"        for source in valid_sources"` | — |
| [SRC-59CF4B7DE8-L000567](../../agents/research.py#L567) | 567 | `"        if (parsed := _parse_publication_date(source.get(\"published_at\"), current)) is not None"` | — |
| [SRC-59CF4B7DE8-L000568](../../agents/research.py#L568) | 568 | `"    ]"` | — |
| [SRC-59CF4B7DE8-L000569](../../agents/research.py#L569) | 569 | `"    recent_days = 7 if freshness == \"current\" else 30"` | — |
| [SRC-59CF4B7DE8-L000570](../../agents/research.py#L570) | 570 | `"    recent_count = sum((current - parsed).total_seconds() >= 0 and"` | — |
| [SRC-59CF4B7DE8-L000571](../../agents/research.py#L571) | 571 | `"                       (current - parsed) <= timedelta(days=recent_days) for parsed in dates)"` | — |
| [SRC-59CF4B7DE8-L000572](../../agents/research.py#L572) | 572 | `"    future_dates = sum(parsed > current + timedelta(days=1) for parsed in dates)"` | — |
| [SRC-59CF4B7DE8-L000573](../../agents/research.py#L573) | 573 | `"    unique_sources = len(valid_sources)"` | — |
| [SRC-59CF4B7DE8-L000574](../../agents/research.py#L574) | 574 | `"    # Evidence coverage uses several independent dimensions and is deliberately not a"` | — |
| [SRC-59CF4B7DE8-L000575](../../agents/research.py#L575) | 575 | `"    # probability that any factual claim is true."` | — |
| [SRC-59CF4B7DE8-L000576](../../agents/research.py#L576) | 576 | `"    coverage_points = 0"` | — |
| [SRC-59CF4B7DE8-L000577](../../agents/research.py#L577) | 577 | `"    coverage_points += min(unique_sources, 10) * 3"` | — |
| [SRC-59CF4B7DE8-L000578](../../agents/research.py#L578) | 578 | `"    coverage_points += min(len(domains), 8) * 4"` | — |
| [SRC-59CF4B7DE8-L000579](../../agents/research.py#L579) | 579 | `"    coverage_points += min(len(providers), 4) * 5"` | — |
| [SRC-59CF4B7DE8-L000580](../../agents/research.py#L580) | 580 | `"    coverage_points += min(pages_read, 8) * 3"` | — |
| [SRC-59CF4B7DE8-L000581](../../agents/research.py#L581) | 581 | `"    coverage_points += min(primary_count, 4) * 4"` | — |
| [SRC-59CF4B7DE8-L000582](../../agents/research.py#L582) | 582 | `"    coverage_points += min(len(dates), 8) * 2"` | — |
| [SRC-59CF4B7DE8-L000583](../../agents/research.py#L583) | 583 | `"    coverage_score = min(100, coverage_points)"` | — |
| [SRC-59CF4B7DE8-L000584](../../agents/research.py#L584) | 584 | `"    if unique_sources >= 8 and len(domains) >= 5 and len(providers) >= 2 and pages_read >= 3:"` | — |
| [SRC-59CF4B7DE8-L000585](../../agents/research.py#L585) | 585 | `"        coverage_level = \"متعدد المصادر\""` | — |
| [SRC-59CF4B7DE8-L000586](../../agents/research.py#L586) | 586 | `"    elif unique_sources >= 4 and len(domains) >= 3 and len(providers) >= 1:"` | — |
| [SRC-59CF4B7DE8-L000587](../../agents/research.py#L587) | 587 | `"        coverage_level = \"متوسط\""` | — |
| [SRC-59CF4B7DE8-L000588](../../agents/research.py#L588) | 588 | `"    else:"` | — |
| [SRC-59CF4B7DE8-L000589](../../agents/research.py#L589) | 589 | `"        coverage_level = \"محدود\""` | — |
| [SRC-59CF4B7DE8-L000590](../../agents/research.py#L590) | 590 | `""` | — |
| [SRC-59CF4B7DE8-L000591](../../agents/research.py#L591) | 591 | `"    warnings: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000592](../../agents/research.py#L592) | 592 | `"    if unique_sources == 0:"` | — |
| [SRC-59CF4B7DE8-L000593](../../agents/research.py#L593) | 593 | `"        warnings.append(\"لا توجد مصادر قابلة للاستشهاد؛ لا تستنتج حقائق من عدم وجود نتائج.\")"` | — |
| [SRC-59CF4B7DE8-L000594](../../agents/research.py#L594) | 594 | `"    if len(domains) < 3:"` | — |
| [SRC-59CF4B7DE8-L000595](../../agents/research.py#L595) | 595 | `"        warnings.append(\"تنوع النطاقات محدود؛ لا تعتبر تكرار النتيجة تأكيدًا مستقلًا.\")"` | — |
| [SRC-59CF4B7DE8-L000596](../../agents/research.py#L596) | 596 | `"    if pages_read < 2 and unique_sources:"` | — |
| [SRC-59CF4B7DE8-L000597](../../agents/research.py#L597) | 597 | `"        warnings.append(\"تمت قراءة أقل من صفحتين مباشرة؛ بعض الأدلة مقتطفات من محركات البحث فقط.\")"` | — |
| [SRC-59CF4B7DE8-L000598](../../agents/research.py#L598) | 598 | `"    if freshness == \"current\":"` | — |
| [SRC-59CF4B7DE8-L000599](../../agents/research.py#L599) | 599 | `"        if not dates:"` | — |
| [SRC-59CF4B7DE8-L000600](../../agents/research.py#L600) | 600 | `"            warnings.append(\"لا تتوفر تواريخ نشر قابلة للتحليل؛ حداثة النتائج غير مؤكدة.\")"` | — |
| [SRC-59CF4B7DE8-L000601](../../agents/research.py#L601) | 601 | `"        elif recent_count == 0:"` | — |
| [SRC-59CF4B7DE8-L000602](../../agents/research.py#L602) | 602 | `"            warnings.append(f\"لم يُعثر على مصدر مؤرخ خلال آخر {recent_days} يومًا ضمن التواريخ القابلة للتحليل.\")"` | — |
| [SRC-59CF4B7DE8-L000603](../../agents/research.py#L603) | 603 | `"    if future_dates:"` | — |
| [SRC-59CF4B7DE8-L000604](../../agents/research.py#L604) | 604 | `"        warnings.append(\"توجد تواريخ مستقبلية غير متوقعة؛ يجب مراجعتها يدويًا.\")"` | — |
| [SRC-59CF4B7DE8-L000605](../../agents/research.py#L605) | 605 | `"    if social_count and primary_count == 0:"` | — |
| [SRC-59CF4B7DE8-L000606](../../agents/research.py#L606) | 606 | `"        warnings.append(\"المصادر اجتماعية فقط دون مصدر رسمي/أكاديمي؛ تعامل معها كآراء أو إشارات لا كحقائق مثبتة.\")"` | — |
| [SRC-59CF4B7DE8-L000607](../../agents/research.py#L607) | 607 | `"    return {"` | — |
| [SRC-59CF4B7DE8-L000608](../../agents/research.py#L608) | 608 | `"        \"unique_sources\": unique_sources,"` | — |
| [SRC-59CF4B7DE8-L000609](../../agents/research.py#L609) | 609 | `"        \"unique_domains\": len(domains),"` | — |
| [SRC-59CF4B7DE8-L000610](../../agents/research.py#L610) | 610 | `"        \"providers_count\": len(providers),"` | — |
| [SRC-59CF4B7DE8-L000611](../../agents/research.py#L611) | 611 | `"        \"providers\": sorted(providers),"` | — |
| [SRC-59CF4B7DE8-L000612](../../agents/research.py#L612) | 612 | `"        \"pages_read\": pages_read,"` | — |
| [SRC-59CF4B7DE8-L000613](../../agents/research.py#L613) | 613 | `"        \"primary_sources\": primary_count,"` | — |
| [SRC-59CF4B7DE8-L000614](../../agents/research.py#L614) | 614 | `"        \"news_sources\": news_count,"` | — |
| [SRC-59CF4B7DE8-L000615](../../agents/research.py#L615) | 615 | `"        \"social_sources\": social_count,"` | — |
| [SRC-59CF4B7DE8-L000616](../../agents/research.py#L616) | 616 | `"        \"dated_sources\": len(dates),"` | — |
| [SRC-59CF4B7DE8-L000617](../../agents/research.py#L617) | 617 | `"        \"recent_sources\": recent_count,"` | — |
| [SRC-59CF4B7DE8-L000618](../../agents/research.py#L618) | 618 | `"        \"undated_sources\": max(0, unique_sources - len(dates)),"` | — |
| [SRC-59CF4B7DE8-L000619](../../agents/research.py#L619) | 619 | `"        \"date_coverage_percent\": round(100 * len(dates) / unique_sources) if unique_sources else 0,"` | — |
| [SRC-59CF4B7DE8-L000620](../../agents/research.py#L620) | 620 | `"        \"coverage_score\": coverage_score,"` | — |
| [SRC-59CF4B7DE8-L000621](../../agents/research.py#L621) | 621 | `"        \"coverage_level\": coverage_level,"` | — |
| [SRC-59CF4B7DE8-L000622](../../agents/research.py#L622) | 622 | `"        \"score_meaning\": \"مؤشر تغطية وتنوع الأدلة، وليس احتمال صحة الإجابة.\","` | — |
| [SRC-59CF4B7DE8-L000623](../../agents/research.py#L623) | 623 | `"        \"warnings\": warnings,"` | — |
| [SRC-59CF4B7DE8-L000624](../../agents/research.py#L624) | 624 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000625](../../agents/research.py#L625) | 625 | `""` | — |
| [SRC-59CF4B7DE8-L000626](../../agents/research.py#L626) | 626 | `""` | — |
| [SRC-59CF4B7DE8-L000627](../../agents/research.py#L627) | 627 | `""` | — |
| [SRC-59CF4B7DE8-L000628](../../agents/research.py#L628) | 628 | `"# ---------------------------------------------------------------------------"` | — |
| [SRC-59CF4B7DE8-L000629](../../agents/research.py#L629) | 629 | `"# Evidence-aware helpers"` | — |
| [SRC-59CF4B7DE8-L000630](../../agents/research.py#L630) | 630 | `"# ---------------------------------------------------------------------------"` | — |
| [SRC-59CF4B7DE8-L000631](../../agents/research.py#L631) | 631 | `""` | — |
| [SRC-59CF4B7DE8-L000632](../../agents/research.py#L632) | 632 | `"_RELEVANCE_STOPWORDS = {"` | — |
| [SRC-59CF4B7DE8-L000633](../../agents/research.py#L633) | 633 | `"    \"the\", \"a\", \"an\", \"of\", \"in\", \"on\", \"at\", \"to\", \"for\","` | — |
| [SRC-59CF4B7DE8-L000634](../../agents/research.py#L634) | 634 | `"    \"is\", \"are\", \"was\", \"were\", \"be\", \"been\", \"being\","` | — |
| [SRC-59CF4B7DE8-L000635](../../agents/research.py#L635) | 635 | `"    \"and\", \"or\", \"but\", \"not\", \"with\", \"without\","` | — |
| [SRC-59CF4B7DE8-L000636](../../agents/research.py#L636) | 636 | `"    \"this\", \"that\", \"these\", \"those\", \"it\", \"its\","` | — |
| [SRC-59CF4B7DE8-L000637](../../agents/research.py#L637) | 637 | `"}"` | — |
| [SRC-59CF4B7DE8-L000638](../../agents/research.py#L638) | 638 | `""` | — |
| [SRC-59CF4B7DE8-L000639](../../agents/research.py#L639) | 639 | `"_OFFICIAL_CLASSES = {\"government\", \"education\", \"official\"}"` | — |
| [SRC-59CF4B7DE8-L000640](../../agents/research.py#L640) | 640 | `""` | — |
| [SRC-59CF4B7DE8-L000641](../../agents/research.py#L641) | 641 | `""` | — |
| [SRC-59CF4B7DE8-L000642](../../agents/research.py#L642) | 642 | `"def _tokenize(text: str) -> set:"` | — |
| [SRC-59CF4B7DE8-L000643](../../agents/research.py#L643) | 643 | `"    if not text:"` | — |
| [SRC-59CF4B7DE8-L000644](../../agents/research.py#L644) | 644 | `"        return set()"` | — |
| [SRC-59CF4B7DE8-L000645](../../agents/research.py#L645) | 645 | `"    norm = _normalize_arabic(text.casefold())"` | — |
| [SRC-59CF4B7DE8-L000646](../../agents/research.py#L646) | 646 | `"    tokens = re.findall(r\"\\w+\", norm, flags=re.UNICODE)"` | — |
| [SRC-59CF4B7DE8-L000647](../../agents/research.py#L647) | 647 | `"    return {t for t in tokens if len(t) >= 3 and t not in _RELEVANCE_STOPWORDS}"` | — |
| [SRC-59CF4B7DE8-L000648](../../agents/research.py#L648) | 648 | `""` | — |
| [SRC-59CF4B7DE8-L000649](../../agents/research.py#L649) | 649 | `""` | — |
| [SRC-59CF4B7DE8-L000650](../../agents/research.py#L650) | 650 | `"def source_relevance_score(src, query: str) -> dict:"` | — |
| [SRC-59CF4B7DE8-L000651](../../agents/research.py#L651) | 651 | `"    if not isinstance(src, dict):"` | — |
| [SRC-59CF4B7DE8-L000652](../../agents/research.py#L652) | 652 | `"        return {\"accepted\": False, \"score\": 0, \"reason\": \"malformed\"}"` | — |
| [SRC-59CF4B7DE8-L000653](../../agents/research.py#L653) | 653 | `""` | — |
| [SRC-59CF4B7DE8-L000654](../../agents/research.py#L654) | 654 | `"    title = str(src.get(\"title\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000655](../../agents/research.py#L655) | 655 | `"    snippet = str(src.get(\"snippet\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000656](../../agents/research.py#L656) | 656 | `"    page_text = str(src.get(\"page_text\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000657](../../agents/research.py#L657) | 657 | `"    source_class = str(src.get(\"source_class\") or \"general\").lower()"` | — |
| [SRC-59CF4B7DE8-L000658](../../agents/research.py#L658) | 658 | `""` | — |
| [SRC-59CF4B7DE8-L000659](../../agents/research.py#L659) | 659 | `"    q_tokens = _tokenize(query)"` | — |
| [SRC-59CF4B7DE8-L000660](../../agents/research.py#L660) | 660 | `"    if not q_tokens:"` | — |
| [SRC-59CF4B7DE8-L000661](../../agents/research.py#L661) | 661 | `"        return {\"accepted\": False, \"score\": 0, \"reason\": \"no_query_tokens\"}"` | — |
| [SRC-59CF4B7DE8-L000662](../../agents/research.py#L662) | 662 | `""` | — |
| [SRC-59CF4B7DE8-L000663](../../agents/research.py#L663) | 663 | `"    t_tokens = _tokenize(title)"` | — |
| [SRC-59CF4B7DE8-L000664](../../agents/research.py#L664) | 664 | `"    s_tokens = _tokenize(snippet)"` | — |
| [SRC-59CF4B7DE8-L000665](../../agents/research.py#L665) | 665 | `"    p_tokens = _tokenize(page_text[:3000])"` | — |
| [SRC-59CF4B7DE8-L000666](../../agents/research.py#L666) | 666 | `""` | — |
| [SRC-59CF4B7DE8-L000667](../../agents/research.py#L667) | 667 | `"    title_ratio = len(q_tokens & t_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000668](../../agents/research.py#L668) | 668 | `"    snippet_ratio = len(q_tokens & s_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000669](../../agents/research.py#L669) | 669 | `"    page_ratio = len(q_tokens & p_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000670](../../agents/research.py#L670) | 670 | `""` | — |
| [SRC-59CF4B7DE8-L000671](../../agents/research.py#L671) | 671 | `"    score = int(title_ratio * 15 + snippet_ratio * 20 + page_ratio * 5)"` | — |
| [SRC-59CF4B7DE8-L000672](../../agents/research.py#L672) | 672 | `""` | — |
| [SRC-59CF4B7DE8-L000673](../../agents/research.py#L673) | 673 | `"    if source_class in _OFFICIAL_CLASSES:"` | — |
| [SRC-59CF4B7DE8-L000674](../../agents/research.py#L674) | 674 | `"        if score >= 5:"` | — |
| [SRC-59CF4B7DE8-L000675](../../agents/research.py#L675) | 675 | `"            return {\"accepted\": True, \"score\": score, \"reason\": \"accepted\"}"` | — |
| [SRC-59CF4B7DE8-L000676](../../agents/research.py#L676) | 676 | `"        return {\"accepted\": True, \"score\": score,"` | — |
| [SRC-59CF4B7DE8-L000677](../../agents/research.py#L677) | 677 | `"                \"reason\": \"kept_official_despite_low_overlap\"}"` | — |
| [SRC-59CF4B7DE8-L000678](../../agents/research.py#L678) | 678 | `""` | — |
| [SRC-59CF4B7DE8-L000679](../../agents/research.py#L679) | 679 | `"    if score >= 18:"` | — |
| [SRC-59CF4B7DE8-L000680](../../agents/research.py#L680) | 680 | `"        return {\"accepted\": True, \"score\": score, \"reason\": \"accepted\"}"` | — |
| [SRC-59CF4B7DE8-L000681](../../agents/research.py#L681) | 681 | `"    return {\"accepted\": False, \"score\": score, \"reason\": \"low_overlap\"}"` | — |
| [SRC-59CF4B7DE8-L000682](../../agents/research.py#L682) | 682 | `""` | — |
| [SRC-59CF4B7DE8-L000683](../../agents/research.py#L683) | 683 | `""` | — |
| [SRC-59CF4B7DE8-L000684](../../agents/research.py#L684) | 684 | `"def filter_relevant_sources(sources, query: str, extra_queries=None):"` | — |
| [SRC-59CF4B7DE8-L000685](../../agents/research.py#L685) | 685 | `"    kept = []"` | — |
| [SRC-59CF4B7DE8-L000686](../../agents/research.py#L686) | 686 | `"    diag = []"` | — |
| [SRC-59CF4B7DE8-L000687](../../agents/research.py#L687) | 687 | `"    seen_urls = set()"` | — |
| [SRC-59CF4B7DE8-L000688](../../agents/research.py#L688) | 688 | `"    seen_titles = set()"` | — |
| [SRC-59CF4B7DE8-L000689](../../agents/research.py#L689) | 689 | `"    combined = \" \".join([query] + list(extra_queries or []))"` | — |
| [SRC-59CF4B7DE8-L000690](../../agents/research.py#L690) | 690 | `""` | — |
| [SRC-59CF4B7DE8-L000691](../../agents/research.py#L691) | 691 | `"    for src in sources or []:"` | — |
| [SRC-59CF4B7DE8-L000692](../../agents/research.py#L692) | 692 | `"        if not isinstance(src, dict):"` | — |
| [SRC-59CF4B7DE8-L000693](../../agents/research.py#L693) | 693 | `"            diag.append({\"reason\": \"malformed\", \"url\": \"\"})"` | — |
| [SRC-59CF4B7DE8-L000694](../../agents/research.py#L694) | 694 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000695](../../agents/research.py#L695) | 695 | `"        url = str(src.get(\"url\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000696](../../agents/research.py#L696) | 696 | `"        domain = str(src.get(\"domain\") or \"\").lower()"` | — |
| [SRC-59CF4B7DE8-L000697](../../agents/research.py#L697) | 697 | `"        title = str(src.get(\"title\") or \"\").strip()"` | — |
| [SRC-59CF4B7DE8-L000698](../../agents/research.py#L698) | 698 | `"        url_key = url.rstrip(\"/\").lower()"` | — |
| [SRC-59CF4B7DE8-L000699](../../agents/research.py#L699) | 699 | `"        title_key = title.lower() + \"\|\" + domain"` | — |
| [SRC-59CF4B7DE8-L000700](../../agents/research.py#L700) | 700 | `""` | — |
| [SRC-59CF4B7DE8-L000701](../../agents/research.py#L701) | 701 | `"        if url_key and url_key in seen_urls:"` | — |
| [SRC-59CF4B7DE8-L000702](../../agents/research.py#L702) | 702 | `"            diag.append({\"reason\": \"duplicate_url\", \"url\": url})"` | — |
| [SRC-59CF4B7DE8-L000703](../../agents/research.py#L703) | 703 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000704](../../agents/research.py#L704) | 704 | `"        if title and title_key in seen_titles:"` | — |
| [SRC-59CF4B7DE8-L000705](../../agents/research.py#L705) | 705 | `"            diag.append({\"reason\": \"duplicate_title_domain\", \"url\": url})"` | — |
| [SRC-59CF4B7DE8-L000706](../../agents/research.py#L706) | 706 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000707](../../agents/research.py#L707) | 707 | `""` | — |
| [SRC-59CF4B7DE8-L000708](../../agents/research.py#L708) | 708 | `"        rel = source_relevance_score(src, combined)"` | — |
| [SRC-59CF4B7DE8-L000709](../../agents/research.py#L709) | 709 | `"        if not rel[\"accepted\"]:"` | — |
| [SRC-59CF4B7DE8-L000710](../../agents/research.py#L710) | 710 | `"            diag.append({\"reason\": rel[\"reason\"], \"url\": url, \"score\": rel[\"score\"]})"` | — |
| [SRC-59CF4B7DE8-L000711](../../agents/research.py#L711) | 711 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000712](../../agents/research.py#L712) | 712 | `""` | — |
| [SRC-59CF4B7DE8-L000713](../../agents/research.py#L713) | 713 | `"        kept.append(src)"` | — |
| [SRC-59CF4B7DE8-L000714](../../agents/research.py#L714) | 714 | `"        if url_key:"` | — |
| [SRC-59CF4B7DE8-L000715](../../agents/research.py#L715) | 715 | `"            seen_urls.add(url_key)"` | — |
| [SRC-59CF4B7DE8-L000716](../../agents/research.py#L716) | 716 | `"        if title:"` | — |
| [SRC-59CF4B7DE8-L000717](../../agents/research.py#L717) | 717 | `"            seen_titles.add(title_key)"` | — |
| [SRC-59CF4B7DE8-L000718](../../agents/research.py#L718) | 718 | `"    return kept, diag"` | — |
| [SRC-59CF4B7DE8-L000719](../../agents/research.py#L719) | 719 | `""` | — |
| [SRC-59CF4B7DE8-L000720](../../agents/research.py#L720) | 720 | `""` | — |
| [SRC-59CF4B7DE8-L000721](../../agents/research.py#L721) | 721 | `"def decide_evidence_status(sources, pages_read: int = 0,"` | — |
| [SRC-59CF4B7DE8-L000722](../../agents/research.py#L722) | 722 | `"                           provider_failures: int = 0,"` | — |
| [SRC-59CF4B7DE8-L000723](../../agents/research.py#L723) | 723 | `"                           search_attempted: bool = True) -> dict:"` | — |
| [SRC-59CF4B7DE8-L000724](../../agents/research.py#L724) | 724 | `"    if not search_attempted:"` | — |
| [SRC-59CF4B7DE8-L000725](../../agents/research.py#L725) | 725 | `"        return {\"evidence_status\": \"failed\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000726](../../agents/research.py#L726) | 726 | `""` | — |
| [SRC-59CF4B7DE8-L000727](../../agents/research.py#L727) | 727 | `"    domains = set()"` | — |
| [SRC-59CF4B7DE8-L000728](../../agents/research.py#L728) | 728 | `"    has_official = False"` | — |
| [SRC-59CF4B7DE8-L000729](../../agents/research.py#L729) | 729 | `"    for s in sources or []:"` | — |
| [SRC-59CF4B7DE8-L000730](../../agents/research.py#L730) | 730 | `"        if not isinstance(s, dict):"` | — |
| [SRC-59CF4B7DE8-L000731](../../agents/research.py#L731) | 731 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000732](../../agents/research.py#L732) | 732 | `"        d = str(s.get(\"domain\") or \"\").lower()"` | — |
| [SRC-59CF4B7DE8-L000733](../../agents/research.py#L733) | 733 | `"        if not d:"` | — |
| [SRC-59CF4B7DE8-L000734](../../agents/research.py#L734) | 734 | `"            url = str(s.get(\"url\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000735](../../agents/research.py#L735) | 735 | `"            if url:"` | — |
| [SRC-59CF4B7DE8-L000736](../../agents/research.py#L736) | 736 | `"                try:"` | — |
| [SRC-59CF4B7DE8-L000737](../../agents/research.py#L737) | 737 | `"                    from urllib.parse import urlparse"` | — |
| [SRC-59CF4B7DE8-L000738](../../agents/research.py#L738) | 738 | `"                    d = urlparse(url).netloc.lower()"` | — |
| [SRC-59CF4B7DE8-L000739](../../agents/research.py#L739) | 739 | `"                except Exception:"` | — |
| [SRC-59CF4B7DE8-L000740](../../agents/research.py#L740) | 740 | `"                    d = \"\""` | — |
| [SRC-59CF4B7DE8-L000741](../../agents/research.py#L741) | 741 | `"        if d:"` | — |
| [SRC-59CF4B7DE8-L000742](../../agents/research.py#L742) | 742 | `"            domains.add(d)"` | — |
| [SRC-59CF4B7DE8-L000743](../../agents/research.py#L743) | 743 | `"        if str(s.get(\"source_class\") or \"\").lower() in _OFFICIAL_CLASSES:"` | — |
| [SRC-59CF4B7DE8-L000744](../../agents/research.py#L744) | 744 | `"            has_official = True"` | — |
| [SRC-59CF4B7DE8-L000745](../../agents/research.py#L745) | 745 | `""` | — |
| [SRC-59CF4B7DE8-L000746](../../agents/research.py#L746) | 746 | `"    if not sources:"` | — |
| [SRC-59CF4B7DE8-L000747](../../agents/research.py#L747) | 747 | `"        if provider_failures > 0:"` | — |
| [SRC-59CF4B7DE8-L000748](../../agents/research.py#L748) | 748 | `"            return {\"evidence_status\": \"failed\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000749](../../agents/research.py#L749) | 749 | `"        return {\"evidence_status\": \"insufficient\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000750](../../agents/research.py#L750) | 750 | `""` | — |
| [SRC-59CF4B7DE8-L000751](../../agents/research.py#L751) | 751 | `"    if len(domains) >= 2 or has_official:"` | — |
| [SRC-59CF4B7DE8-L000752](../../agents/research.py#L752) | 752 | `"        return {\"evidence_status\": \"adequate\", \"should_abstain\": False}"` | — |
| [SRC-59CF4B7DE8-L000753](../../agents/research.py#L753) | 753 | `"    if len(domains) >= 1:"` | — |
| [SRC-59CF4B7DE8-L000754](../../agents/research.py#L754) | 754 | `"        return {\"evidence_status\": \"partial\", \"should_abstain\": False}"` | — |
| [SRC-59CF4B7DE8-L000755](../../agents/research.py#L755) | 755 | `"    return {\"evidence_status\": \"insufficient\", \"should_abstain\": True}"` | — |
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
