# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **003**
- سجلات الأسطر: **800**
- النطاق: SRC-59CF4B7DE8-L000056 إلى SRC-1AE03B9EC3-L000195
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-59CF4B7DE8 — [agents/research.py](../../agents/research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
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
| [SRC-59CF4B7DE8-L000120](../../agents/research.py#L120) | 120 | `"_ARABIC_RE = re.compile(r\"[؀-ۿ]\")"` | — |
| [SRC-59CF4B7DE8-L000121](../../agents/research.py#L121) | 121 | `""` | — |
| [SRC-59CF4B7DE8-L000122](../../agents/research.py#L122) | 122 | `""` | — |
| [SRC-59CF4B7DE8-L000123](../../agents/research.py#L123) | 123 | `"def _normalize_arabic(text: str) -> str:"` | — |
| [SRC-59CF4B7DE8-L000124](../../agents/research.py#L124) | 124 | `"    if not text:"` | — |
| [SRC-59CF4B7DE8-L000125](../../agents/research.py#L125) | 125 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000126](../../agents/research.py#L126) | 126 | `"    return (text.replace(\"\\u0623\", \"\\u0627\")"` | — |
| [SRC-59CF4B7DE8-L000127](../../agents/research.py#L127) | 127 | `"                .replace(\"\\u0625\", \"\\u0627\")"` | — |
| [SRC-59CF4B7DE8-L000128](../../agents/research.py#L128) | 128 | `"                .replace(\"\\u0622\", \"\\u0627\")"` | — |
| [SRC-59CF4B7DE8-L000129](../../agents/research.py#L129) | 129 | `"                .replace(\"\\u0629\", \"\\u0647\")"` | — |
| [SRC-59CF4B7DE8-L000130](../../agents/research.py#L130) | 130 | `"                .replace(\"\\u0649\", \"\\u064a\"))"` | — |
| [SRC-59CF4B7DE8-L000131](../../agents/research.py#L131) | 131 | `""` | — |
| [SRC-59CF4B7DE8-L000132](../../agents/research.py#L132) | 132 | `""` | — |
| [SRC-59CF4B7DE8-L000133](../../agents/research.py#L133) | 133 | `"def _contains_any(text: str, terms: tuple) -> bool:"` | — |
| [SRC-59CF4B7DE8-L000134](../../agents/research.py#L134) | 134 | `"    if not text:"` | — |
| [SRC-59CF4B7DE8-L000135](../../agents/research.py#L135) | 135 | `"        return False"` | — |
| [SRC-59CF4B7DE8-L000136](../../agents/research.py#L136) | 136 | `"    haystack = _normalize_arabic(text.casefold())"` | — |
| [SRC-59CF4B7DE8-L000137](../../agents/research.py#L137) | 137 | `"    for term in terms:"` | — |
| [SRC-59CF4B7DE8-L000138](../../agents/research.py#L138) | 138 | `"        if not term:"` | — |
| [SRC-59CF4B7DE8-L000139](../../agents/research.py#L139) | 139 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000140](../../agents/research.py#L140) | 140 | `"        t = _normalize_arabic(term.casefold())"` | — |
| [SRC-59CF4B7DE8-L000141](../../agents/research.py#L141) | 141 | `"        if _ARABIC_RE.search(t):"` | — |
| [SRC-59CF4B7DE8-L000142](../../agents/research.py#L142) | 142 | `"            if t in haystack:"` | — |
| [SRC-59CF4B7DE8-L000143](../../agents/research.py#L143) | 143 | `"                return True"` | — |
| [SRC-59CF4B7DE8-L000144](../../agents/research.py#L144) | 144 | `"        else:"` | — |
| [SRC-59CF4B7DE8-L000145](../../agents/research.py#L145) | 145 | `"            pat = r\"(?<![a-zA-Z0-9])\" + re.escape(t) + r\"(?![a-zA-Z0-9])\""` | — |
| [SRC-59CF4B7DE8-L000146](../../agents/research.py#L146) | 146 | `"            if re.search(pat, haystack):"` | — |
| [SRC-59CF4B7DE8-L000147](../../agents/research.py#L147) | 147 | `"                return True"` | — |
| [SRC-59CF4B7DE8-L000148](../../agents/research.py#L148) | 148 | `"    return False"` | — |
| [SRC-59CF4B7DE8-L000149](../../agents/research.py#L149) | 149 | `""` | — |
| [SRC-59CF4B7DE8-L000150](../../agents/research.py#L150) | 150 | `""` | — |
| [SRC-59CF4B7DE8-L000151](../../agents/research.py#L151) | 151 | `"def detect_social_focus(question: str, history: list[dict[str, str]] \| None = None) -> bool:"` | — |
| [SRC-59CF4B7DE8-L000152](../../agents/research.py#L152) | 152 | `"    context = question + \" \" + \" \".join("` | — |
| [SRC-59CF4B7DE8-L000153](../../agents/research.py#L153) | 153 | `"        item.get(\"content\", \"\") for item in (history or [])[-4:]"` | — |
| [SRC-59CF4B7DE8-L000154](../../agents/research.py#L154) | 154 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000155](../../agents/research.py#L155) | 155 | `"    return _contains_any(context, _SOCIAL_TERMS)"` | — |
| [SRC-59CF4B7DE8-L000156](../../agents/research.py#L156) | 156 | `""` | — |
| [SRC-59CF4B7DE8-L000157](../../agents/research.py#L157) | 157 | `""` | — |
| [SRC-59CF4B7DE8-L000158](../../agents/research.py#L158) | 158 | `"def detect_freshness(question: str) -> bool:"` | — |
| [SRC-59CF4B7DE8-L000159](../../agents/research.py#L159) | 159 | `"    return _contains_any(question, _FRESH_TERMS)"` | — |
| [SRC-59CF4B7DE8-L000160](../../agents/research.py#L160) | 160 | `""` | — |
| [SRC-59CF4B7DE8-L000161](../../agents/research.py#L161) | 161 | `""` | — |
| [SRC-59CF4B7DE8-L000162](../../agents/research.py#L162) | 162 | `"def detect_depth(question: str) -> str:"` | — |
| [SRC-59CF4B7DE8-L000163](../../agents/research.py#L163) | 163 | `"    return \"deep\" if _contains_any(question, _DEEP_TERMS) else \"standard\""` | — |
| [SRC-59CF4B7DE8-L000164](../../agents/research.py#L164) | 164 | `""` | — |
| [SRC-59CF4B7DE8-L000165](../../agents/research.py#L165) | 165 | `""` | — |
| [SRC-59CF4B7DE8-L000166](../../agents/research.py#L166) | 166 | `"def mentioned_social_platforms(text: str) -> list[str]:"` | — |
| [SRC-59CF4B7DE8-L000167](../../agents/research.py#L167) | 167 | `"    rules = ("` | — |
| [SRC-59CF4B7DE8-L000168](../../agents/research.py#L168) | 168 | `"        (\"reddit\", (\"reddit\", \"ريديت\")),"` | — |
| [SRC-59CF4B7DE8-L000169](../../agents/research.py#L169) | 169 | `"        (\"youtube\", (\"youtube\", \"يوتيوب\")),"` | — |
| [SRC-59CF4B7DE8-L000170](../../agents/research.py#L170) | 170 | `"        (\"facebook\", (\"facebook\", \"فيسبوك\", \"فيس بوك\")),"` | — |
| [SRC-59CF4B7DE8-L000171](../../agents/research.py#L171) | 171 | `"        (\"instagram\", (\"instagram\", \"انستجرام\", \"إنستجرام\")),"` | — |
| [SRC-59CF4B7DE8-L000172](../../agents/research.py#L172) | 172 | `"        (\"x\", (\"x.com\", \"twitter\", \"تويتر\", \"اكس\", \"إكس\")),"` | — |
| [SRC-59CF4B7DE8-L000173](../../agents/research.py#L173) | 173 | `"        (\"tiktok\", (\"tiktok\", \"تيك توك\")),"` | — |
| [SRC-59CF4B7DE8-L000174](../../agents/research.py#L174) | 174 | `"        (\"linkedin\", (\"linkedin\", \"لينكدان\", \"لينكدإن\")),"` | — |
| [SRC-59CF4B7DE8-L000175](../../agents/research.py#L175) | 175 | `"        (\"threads\", (\"threads\", \"ثريدز\")),"` | — |
| [SRC-59CF4B7DE8-L000176](../../agents/research.py#L176) | 176 | `"        (\"bluesky\", (\"bluesky\", \"بلو سكاي\")),"` | — |
| [SRC-59CF4B7DE8-L000177](../../agents/research.py#L177) | 177 | `"    )"` | — |
| [SRC-59CF4B7DE8-L000178](../../agents/research.py#L178) | 178 | `"    low = text.casefold()"` | — |
| [SRC-59CF4B7DE8-L000179](../../agents/research.py#L179) | 179 | `"    return [name for name, aliases in rules if any(alias.casefold() in low for alias in aliases)]"` | — |
| [SRC-59CF4B7DE8-L000180](../../agents/research.py#L180) | 180 | `""` | — |
| [SRC-59CF4B7DE8-L000181](../../agents/research.py#L181) | 181 | `""` | — |
| [SRC-59CF4B7DE8-L000182](../../agents/research.py#L182) | 182 | `"def fallback_plan("` | — |
| [SRC-59CF4B7DE8-L000183](../../agents/research.py#L183) | 183 | `"    question: str, history: list[dict[str, str]] \| None = None"` | — |
| [SRC-59CF4B7DE8-L000184](../../agents/research.py#L184) | 184 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000185](../../agents/research.py#L185) | 185 | `"    \"\"\"Build a small but varied plan when no model planner is configured or parsing fails.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000186](../../agents/research.py#L186) | 186 | `"    contextual_question = resolve_followup_query(question, history)"` | — |
| [SRC-59CF4B7DE8-L000187](../../agents/research.py#L187) | 187 | `"    direct_urls = extract_urls(question)"` | — |
| [SRC-59CF4B7DE8-L000188](../../agents/research.py#L188) | 188 | `"    base = _compact(re.sub(r\"https?://[^\\s<>()]+\", \" \", contextual_question), 500)"` | — |
| [SRC-59CF4B7DE8-L000189](../../agents/research.py#L189) | 189 | `"    if not base:"` | — |
| [SRC-59CF4B7DE8-L000190](../../agents/research.py#L190) | 190 | `"        base = \"اقرأ محتوى الصفحة\" if re.search(r\"[\\u0600-\\u06FF]\", question) else \"read the linked page\""` | — |
| [SRC-59CF4B7DE8-L000191](../../agents/research.py#L191) | 191 | `"    social_focus = detect_social_focus(question, history)"` | — |
| [SRC-59CF4B7DE8-L000192](../../agents/research.py#L192) | 192 | `"    fresh = detect_freshness(question)"` | — |
| [SRC-59CF4B7DE8-L000193](../../agents/research.py#L193) | 193 | `"    detected_depth = detect_depth(question)"` | — |
| [SRC-59CF4B7DE8-L000194](../../agents/research.py#L194) | 194 | `"    deep = detected_depth == \"deep\""` | — |
| [SRC-59CF4B7DE8-L000195](../../agents/research.py#L195) | 195 | `"    platforms = mentioned_social_platforms(question + \" \" + \" \".join("` | — |
| [SRC-59CF4B7DE8-L000196](../../agents/research.py#L196) | 196 | `"        item.get(\"content\", \"\") for item in (history or [])[-4:]"` | — |
| [SRC-59CF4B7DE8-L000197](../../agents/research.py#L197) | 197 | `"    ))"` | — |
| [SRC-59CF4B7DE8-L000198](../../agents/research.py#L198) | 198 | `"    queries: list[str] = [base]"` | — |
| [SRC-59CF4B7DE8-L000199](../../agents/research.py#L199) | 199 | `""` | — |
| [SRC-59CF4B7DE8-L000200](../../agents/research.py#L200) | 200 | `"    if fresh and base:"` | — |
| [SRC-59CF4B7DE8-L000201](../../agents/research.py#L201) | 201 | `"        queries.append(_compact(base + \" أحدث مستجدات آخر الأخبار\", 500))"` | — |
| [SRC-59CF4B7DE8-L000202](../../agents/research.py#L202) | 202 | `"    if _contains_any(question, (\"قارن\", \"مقارنة\", \"compare\", \"versus\", \"vs\", \"الفرق بين\")):"` | — |
| [SRC-59CF4B7DE8-L000203](../../agents/research.py#L203) | 203 | `"        queries.append(_compact(base + \" مقارنة مراجعات مميزات عيوب\", 500))"` | — |
| [SRC-59CF4B7DE8-L000204](../../agents/research.py#L204) | 204 | `""` | — |
| [SRC-59CF4B7DE8-L000205](../../agents/research.py#L205) | 205 | `"    if social_focus:"` | — |
| [SRC-59CF4B7DE8-L000206](../../agents/research.py#L206) | 206 | `"        selected = platforms or [\"facebook\", \"instagram\", \"reddit\"]"` | — |
| [SRC-59CF4B7DE8-L000207](../../agents/research.py#L207) | 207 | `"        for platform in selected[:3]:"` | — |
| [SRC-59CF4B7DE8-L000208](../../agents/research.py#L208) | 208 | `"            domain = SOCIAL_DOMAINS[platform]"` | — |
| [SRC-59CF4B7DE8-L000209](../../agents/research.py#L209) | 209 | `"            site_query = _compact(f\"site:{domain} {base}\", 500)"` | — |
| [SRC-59CF4B7DE8-L000210](../../agents/research.py#L210) | 210 | `"            if site_query not in queries:"` | — |
| [SRC-59CF4B7DE8-L000211](../../agents/research.py#L211) | 211 | `"                queries.append(site_query)"` | — |
| [SRC-59CF4B7DE8-L000212](../../agents/research.py#L212) | 212 | `""` | — |
| [SRC-59CF4B7DE8-L000213](../../agents/research.py#L213) | 213 | `"    if deep and not social_focus and len(queries) < MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000214](../../agents/research.py#L214) | 214 | `"        queries.append(_compact(base + \" مصادر موثوقة تقارير إحصاءات\", 500))"` | — |
| [SRC-59CF4B7DE8-L000215](../../agents/research.py#L215) | 215 | `""` | — |
| [SRC-59CF4B7DE8-L000216](../../agents/research.py#L216) | 216 | `"    unique: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000217](../../agents/research.py#L217) | 217 | `"    seen: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000218](../../agents/research.py#L218) | 218 | `"    for query in queries:"` | — |
| [SRC-59CF4B7DE8-L000219](../../agents/research.py#L219) | 219 | `"        value = _compact(query, 500)"` | — |
| [SRC-59CF4B7DE8-L000220](../../agents/research.py#L220) | 220 | `"        key = value.casefold()"` | — |
| [SRC-59CF4B7DE8-L000221](../../agents/research.py#L221) | 221 | `"        if value and key not in seen:"` | — |
| [SRC-59CF4B7DE8-L000222](../../agents/research.py#L222) | 222 | `"            unique.append(value)"` | — |
| [SRC-59CF4B7DE8-L000223](../../agents/research.py#L223) | 223 | `"            seen.add(key)"` | — |
| [SRC-59CF4B7DE8-L000224](../../agents/research.py#L224) | 224 | `"        if len(unique) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000225](../../agents/research.py#L225) | 225 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000226](../../agents/research.py#L226) | 226 | `""` | — |
| [SRC-59CF4B7DE8-L000227](../../agents/research.py#L227) | 227 | `"    return {"` | — |
| [SRC-59CF4B7DE8-L000228](../../agents/research.py#L228) | 228 | `"        \"queries\": unique or [base],"` | — |
| [SRC-59CF4B7DE8-L000229](../../agents/research.py#L229) | 229 | `"        \"direct_urls\": direct_urls,"` | — |
| [SRC-59CF4B7DE8-L000230](../../agents/research.py#L230) | 230 | `"        \"social_focus\": social_focus,"` | — |
| [SRC-59CF4B7DE8-L000231](../../agents/research.py#L231) | 231 | `"        \"freshness\": \"current\" if fresh else \"any\","` | — |
| [SRC-59CF4B7DE8-L000232](../../agents/research.py#L232) | 232 | `"        \"depth\": detected_depth,"` | — |
| [SRC-59CF4B7DE8-L000233](../../agents/research.py#L233) | 233 | `"        \"platforms\": platforms,"` | — |
| [SRC-59CF4B7DE8-L000234](../../agents/research.py#L234) | 234 | `"        \"planning_method\": \"deterministic_fallback\","` | — |
| [SRC-59CF4B7DE8-L000235](../../agents/research.py#L235) | 235 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000236](../../agents/research.py#L236) | 236 | `""` | — |
| [SRC-59CF4B7DE8-L000237](../../agents/research.py#L237) | 237 | `""` | — |
| [SRC-59CF4B7DE8-L000238](../../agents/research.py#L238) | 238 | `"def validate_plan("` | — |
| [SRC-59CF4B7DE8-L000239](../../agents/research.py#L239) | 239 | `"    candidate: Any, question: str, history: list[dict[str, str]] \| None = None"` | — |
| [SRC-59CF4B7DE8-L000240](../../agents/research.py#L240) | 240 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000241](../../agents/research.py#L241) | 241 | `"    fallback = fallback_plan(question, history)"` | — |
| [SRC-59CF4B7DE8-L000242](../../agents/research.py#L242) | 242 | `"    if not isinstance(candidate, dict):"` | — |
| [SRC-59CF4B7DE8-L000243](../../agents/research.py#L243) | 243 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000244](../../agents/research.py#L244) | 244 | `"    raw_queries = candidate.get(\"queries\", [])"` | — |
| [SRC-59CF4B7DE8-L000245](../../agents/research.py#L245) | 245 | `"    if not isinstance(raw_queries, list):"` | — |
| [SRC-59CF4B7DE8-L000246](../../agents/research.py#L246) | 246 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000247](../../agents/research.py#L247) | 247 | `"    queries: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000248](../../agents/research.py#L248) | 248 | `"    seen: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000249](../../agents/research.py#L249) | 249 | `"    for item in raw_queries:"` | — |
| [SRC-59CF4B7DE8-L000250](../../agents/research.py#L250) | 250 | `"        query = _compact(item, 500)"` | — |
| [SRC-59CF4B7DE8-L000251](../../agents/research.py#L251) | 251 | `"        # Never accept prompt-like multi-line payloads as search-query instructions."` | — |
| [SRC-59CF4B7DE8-L000252](../../agents/research.py#L252) | 252 | `"        query = query.replace(\"\\n\", \" \").replace(\"\\r\", \" \")"` | — |
| [SRC-59CF4B7DE8-L000253](../../agents/research.py#L253) | 253 | `"        if len(query) < 2:"` | — |
| [SRC-59CF4B7DE8-L000254](../../agents/research.py#L254) | 254 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000255](../../agents/research.py#L255) | 255 | `"        if query.casefold() not in seen:"` | — |
| [SRC-59CF4B7DE8-L000256](../../agents/research.py#L256) | 256 | `"            seen.add(query.casefold())"` | — |
| [SRC-59CF4B7DE8-L000257](../../agents/research.py#L257) | 257 | `"            queries.append(query)"` | — |
| [SRC-59CF4B7DE8-L000258](../../agents/research.py#L258) | 258 | `"        if len(queries) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-59CF4B7DE8-L000259](../../agents/research.py#L259) | 259 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000260](../../agents/research.py#L260) | 260 | `"    if not queries:"` | — |
| [SRC-59CF4B7DE8-L000261](../../agents/research.py#L261) | 261 | `"        return fallback"` | — |
| [SRC-59CF4B7DE8-L000262](../../agents/research.py#L262) | 262 | `"    base = fallback_plan(question, history)"` | — |
| [SRC-59CF4B7DE8-L000263](../../agents/research.py#L263) | 263 | `"    platforms = candidate.get(\"platforms\")"` | — |
| [SRC-59CF4B7DE8-L000264](../../agents/research.py#L264) | 264 | `"    if not isinstance(platforms, list):"` | — |
| [SRC-59CF4B7DE8-L000265](../../agents/research.py#L265) | 265 | `"        platforms = base[\"platforms\"]"` | — |
| [SRC-59CF4B7DE8-L000266](../../agents/research.py#L266) | 266 | `"    safe_platforms = [p for p in platforms if isinstance(p, str) and p in SOCIAL_DOMAINS]"` | — |
| [SRC-59CF4B7DE8-L000267](../../agents/research.py#L267) | 267 | `"    return {"` | — |
| [SRC-59CF4B7DE8-L000268](../../agents/research.py#L268) | 268 | `"        \"queries\": queries,"` | — |
| [SRC-59CF4B7DE8-L000269](../../agents/research.py#L269) | 269 | `"        \"direct_urls\": fallback[\"direct_urls\"],"` | — |
| [SRC-59CF4B7DE8-L000270](../../agents/research.py#L270) | 270 | `"        \"social_focus\": bool(candidate.get(\"social_focus\", base[\"social_focus\"])),"` | — |
| [SRC-59CF4B7DE8-L000271](../../agents/research.py#L271) | 271 | `"        \"freshness\": \"current\" if candidate.get(\"freshness\") == \"current\" else base[\"freshness\"],"` | — |
| [SRC-59CF4B7DE8-L000272](../../agents/research.py#L272) | 272 | `"        \"depth\": \"deep\" if candidate.get(\"depth\") == \"deep\" else base[\"depth\"],"` | — |
| [SRC-59CF4B7DE8-L000273](../../agents/research.py#L273) | 273 | `"        \"platforms\": list(dict.fromkeys(safe_platforms))[:5],"` | — |
| [SRC-59CF4B7DE8-L000274](../../agents/research.py#L274) | 274 | `"        \"planning_method\": \"language_model\","` | — |
| [SRC-59CF4B7DE8-L000275](../../agents/research.py#L275) | 275 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000276](../../agents/research.py#L276) | 276 | `""` | — |
| [SRC-59CF4B7DE8-L000277](../../agents/research.py#L277) | 277 | `""` | — |
| [SRC-59CF4B7DE8-L000278](../../agents/research.py#L278) | 278 | `"def _canonical_result_url(url: str) -> str:"` | — |
| [SRC-59CF4B7DE8-L000279](../../agents/research.py#L279) | 279 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000280](../../agents/research.py#L280) | 280 | `"        parsed = urlparse(url)"` | — |
| [SRC-59CF4B7DE8-L000281](../../agents/research.py#L281) | 281 | `"        host = (parsed.hostname or \"\").lower().removeprefix(\"www.\")"` | — |
| [SRC-59CF4B7DE8-L000282](../../agents/research.py#L282) | 282 | `"        # Drop fragments and common tracking query parameters before deduplication."` | — |
| [SRC-59CF4B7DE8-L000283](../../agents/research.py#L283) | 283 | `"        parts = []"` | — |
| [SRC-59CF4B7DE8-L000284](../../agents/research.py#L284) | 284 | `"        for part in parsed.query.split(\"&\"):"` | — |
| [SRC-59CF4B7DE8-L000285](../../agents/research.py#L285) | 285 | `"            key = part.split(\"=\", 1)[0].lower()"` | — |
| [SRC-59CF4B7DE8-L000286](../../agents/research.py#L286) | 286 | `"            if key.startswith(\"utm_\") or key in {\"fbclid\", \"gclid\", \"ref\", \"ref_src\"}:"` | — |
| [SRC-59CF4B7DE8-L000287](../../agents/research.py#L287) | 287 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000288](../../agents/research.py#L288) | 288 | `"            if part:"` | — |
| [SRC-59CF4B7DE8-L000289](../../agents/research.py#L289) | 289 | `"                parts.append(part)"` | — |
| [SRC-59CF4B7DE8-L000290](../../agents/research.py#L290) | 290 | `"        query = \"&\".join(sorted(parts))"` | — |
| [SRC-59CF4B7DE8-L000291](../../agents/research.py#L291) | 291 | `"        path = parsed.path.rstrip(\"/\") or \"/\""` | — |
| [SRC-59CF4B7DE8-L000292](../../agents/research.py#L292) | 292 | `"        return f\"{parsed.scheme.lower()}://{host}{path}\" + (f\"?{query}\" if query else \"\")"` | — |
| [SRC-59CF4B7DE8-L000293](../../agents/research.py#L293) | 293 | `"    except (ValueError, TypeError):"` | — |
| [SRC-59CF4B7DE8-L000294](../../agents/research.py#L294) | 294 | `"        return url"` | — |
| [SRC-59CF4B7DE8-L000295](../../agents/research.py#L295) | 295 | `""` | — |
| [SRC-59CF4B7DE8-L000296](../../agents/research.py#L296) | 296 | `""` | — |
| [SRC-59CF4B7DE8-L000297](../../agents/research.py#L297) | 297 | `"def classify_source(url: str) -> dict[str, str]:"` | — |
| [SRC-59CF4B7DE8-L000298](../../agents/research.py#L298) | 298 | `"    host = (urlparse(url).hostname or \"\").lower().removeprefix(\"www.\")"` | — |
| [SRC-59CF4B7DE8-L000299](../../agents/research.py#L299) | 299 | `"    platform = \"web\""` | — |
| [SRC-59CF4B7DE8-L000300](../../agents/research.py#L300) | 300 | `"    mapping = {"` | — |
| [SRC-59CF4B7DE8-L000301](../../agents/research.py#L301) | 301 | `"        \"reddit.com\": \"reddit\", \"old.reddit.com\": \"reddit\","` | — |
| [SRC-59CF4B7DE8-L000302](../../agents/research.py#L302) | 302 | `"        \"youtube.com\": \"youtube\", \"youtu.be\": \"youtube\","` | — |
| [SRC-59CF4B7DE8-L000303](../../agents/research.py#L303) | 303 | `"        \"facebook.com\": \"facebook\", \"instagram.com\": \"instagram\","` | — |
| [SRC-59CF4B7DE8-L000304](../../agents/research.py#L304) | 304 | `"        \"x.com\": \"x\", \"twitter.com\": \"x\", \"tiktok.com\": \"tiktok\","` | — |
| [SRC-59CF4B7DE8-L000305](../../agents/research.py#L305) | 305 | `"        \"linkedin.com\": \"linkedin\", \"threads.net\": \"threads\","` | — |
| [SRC-59CF4B7DE8-L000306](../../agents/research.py#L306) | 306 | `"        \"bsky.app\": \"bluesky\","` | — |
| [SRC-59CF4B7DE8-L000307](../../agents/research.py#L307) | 307 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000308](../../agents/research.py#L308) | 308 | `"    for domain, label in mapping.items():"` | — |
| [SRC-59CF4B7DE8-L000309](../../agents/research.py#L309) | 309 | `"        if host == domain or host.endswith(\".\" + domain):"` | — |
| [SRC-59CF4B7DE8-L000310](../../agents/research.py#L310) | 310 | `"            platform = label"` | — |
| [SRC-59CF4B7DE8-L000311](../../agents/research.py#L311) | 311 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000312](../../agents/research.py#L312) | 312 | `"    trust = \"general\""` | — |
| [SRC-59CF4B7DE8-L000313](../../agents/research.py#L313) | 313 | `"    if host.endswith((\".gov\", \".gov.eg\", \".gov.uk\")):"` | — |
| [SRC-59CF4B7DE8-L000314](../../agents/research.py#L314) | 314 | `"        trust = \"government\""` | — |
| [SRC-59CF4B7DE8-L000315](../../agents/research.py#L315) | 315 | `"    elif host.endswith((\".edu\", \".ac.uk\", \".edu.eg\")):"` | — |
| [SRC-59CF4B7DE8-L000316](../../agents/research.py#L316) | 316 | `"        trust = \"academic\""` | — |
| [SRC-59CF4B7DE8-L000317](../../agents/research.py#L317) | 317 | `"    elif host == \"news.google.com\" or any("` | — |
| [SRC-59CF4B7DE8-L000318](../../agents/research.py#L318) | 318 | `"        name in host"` | — |
| [SRC-59CF4B7DE8-L000319](../../agents/research.py#L319) | 319 | `"        for name in ("` | — |
| [SRC-59CF4B7DE8-L000320](../../agents/research.py#L320) | 320 | `"            \"reuters.com\", \"apnews.com\", \"bbc.com\", \"bbc.co.uk\","` | — |
| [SRC-59CF4B7DE8-L000321](../../agents/research.py#L321) | 321 | `"            \"ft.com\", \"nytimes.com\", \"theguardian.com\","` | — |
| [SRC-59CF4B7DE8-L000322](../../agents/research.py#L322) | 322 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000323](../../agents/research.py#L323) | 323 | `"    ):"` | — |
| [SRC-59CF4B7DE8-L000324](../../agents/research.py#L324) | 324 | `"        trust = \"news\""` | — |
| [SRC-59CF4B7DE8-L000325](../../agents/research.py#L325) | 325 | `"    elif platform != \"web\":"` | — |
| [SRC-59CF4B7DE8-L000326](../../agents/research.py#L326) | 326 | `"        trust = \"social\""` | — |
| [SRC-59CF4B7DE8-L000327](../../agents/research.py#L327) | 327 | `"    return {\"domain\": host, \"platform\": platform, \"source_class\": trust}"` | — |
| [SRC-59CF4B7DE8-L000328](../../agents/research.py#L328) | 328 | `""` | — |
| [SRC-59CF4B7DE8-L000329](../../agents/research.py#L329) | 329 | `""` | — |
| [SRC-59CF4B7DE8-L000330](../../agents/research.py#L330) | 330 | `"def fuse_ranked_results("` | — |
| [SRC-59CF4B7DE8-L000331](../../agents/research.py#L331) | 331 | `"    batches: list[dict[str, Any]], limit: int = MAX_FUSED_RESULTS"` | — |
| [SRC-59CF4B7DE8-L000332](../../agents/research.py#L332) | 332 | `") -> list[dict[str, Any]]:"` | — |
| [SRC-59CF4B7DE8-L000333](../../agents/research.py#L333) | 333 | `"    \"\"\"Reciprocal-rank-fuse result sets across queries/providers and dedupe URLs.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000334](../../agents/research.py#L334) | 334 | `"    accumulated: dict[str, dict[str, Any]] = {}"` | — |
| [SRC-59CF4B7DE8-L000335](../../agents/research.py#L335) | 335 | `"    for batch in batches:"` | — |
| [SRC-59CF4B7DE8-L000336](../../agents/research.py#L336) | 336 | `"        query = _compact(batch.get(\"query\", \"\"), 500)"` | — |
| [SRC-59CF4B7DE8-L000337](../../agents/research.py#L337) | 337 | `"        provider = _compact(batch.get(\"provider\", \"search\"), 80)"` | — |
| [SRC-59CF4B7DE8-L000338](../../agents/research.py#L338) | 338 | `"        results = batch.get(\"results\", [])"` | — |
| [SRC-59CF4B7DE8-L000339](../../agents/research.py#L339) | 339 | `"        if not isinstance(results, list):"` | — |
| [SRC-59CF4B7DE8-L000340](../../agents/research.py#L340) | 340 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000341](../../agents/research.py#L341) | 341 | `"        for position, source in enumerate(results, 1):"` | — |
| [SRC-59CF4B7DE8-L000342](../../agents/research.py#L342) | 342 | `"            if not isinstance(source, dict) or not source.get(\"url\"):"` | — |
| [SRC-59CF4B7DE8-L000343](../../agents/research.py#L343) | 343 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000344](../../agents/research.py#L344) | 344 | `"            url = _canonical_result_url(str(source[\"url\"]))"` | — |
| [SRC-59CF4B7DE8-L000345](../../agents/research.py#L345) | 345 | `"            if not url.startswith((\"https://\", \"http://\")):"` | — |
| [SRC-59CF4B7DE8-L000346](../../agents/research.py#L346) | 346 | `"                continue"` | — |
| [SRC-59CF4B7DE8-L000347](../../agents/research.py#L347) | 347 | `"            entry = accumulated.get(url)"` | — |
| [SRC-59CF4B7DE8-L000348](../../agents/research.py#L348) | 348 | `"            if entry is None:"` | — |
| [SRC-59CF4B7DE8-L000349](../../agents/research.py#L349) | 349 | `"                publisher_url = _compact(source.get(\"publisher_url\") or \"\", 2048)"` | — |
| [SRC-59CF4B7DE8-L000350](../../agents/research.py#L350) | 350 | `"                source_identity_url = publisher_url or str(source[\"url\"])"` | — |
| [SRC-59CF4B7DE8-L000351](../../agents/research.py#L351) | 351 | `"                entry = {"` | — |
| [SRC-59CF4B7DE8-L000352](../../agents/research.py#L352) | 352 | `"                    \"title\": _compact(source.get(\"title\") or \"نتيجة ويب\", 300),"` | — |
| [SRC-59CF4B7DE8-L000353](../../agents/research.py#L353) | 353 | `"                    \"url\": str(source[\"url\"]),"` | — |
| [SRC-59CF4B7DE8-L000354](../../agents/research.py#L354) | 354 | `"                    \"snippet\": _compact(source.get(\"snippet\") or \"\", 1800),"` | — |
| [SRC-59CF4B7DE8-L000355](../../agents/research.py#L355) | 355 | `"                    \"page_text\": _compact(source.get(\"page_text\") or \"\", 12_000),"` | — |
| [SRC-59CF4B7DE8-L000356](../../agents/research.py#L356) | 356 | `"                    \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-59CF4B7DE8-L000357](../../agents/research.py#L357) | 357 | `"                    \"providers\": [],"` | — |
| [SRC-59CF4B7DE8-L000358](../../agents/research.py#L358) | 358 | `"                    \"queries\": [],"` | — |
| [SRC-59CF4B7DE8-L000359](../../agents/research.py#L359) | 359 | `"                    \"rank_score\": 0.0,"` | — |
| [SRC-59CF4B7DE8-L000360](../../agents/research.py#L360) | 360 | `"                    \"best_raw_rank\": position,"` | — |
| [SRC-59CF4B7DE8-L000361](../../agents/research.py#L361) | 361 | `"                    \"published_at\": _compact(source.get(\"published_at\") or \"\", 100),"` | — |
| [SRC-59CF4B7DE8-L000362](../../agents/research.py#L362) | 362 | `"                    \"publisher_name\": _compact(source.get(\"publisher_name\") or \"\", 200),"` | — |
| [SRC-59CF4B7DE8-L000363](../../agents/research.py#L363) | 363 | `"                    \"publisher_url\": publisher_url,"` | — |
| [SRC-59CF4B7DE8-L000364](../../agents/research.py#L364) | 364 | `"                    \"publisher_domain\": _compact(source.get(\"publisher_domain\") or \"\", 300),"` | — |
| [SRC-59CF4B7DE8-L000365](../../agents/research.py#L365) | 365 | `"                }"` | — |
| [SRC-59CF4B7DE8-L000366](../../agents/research.py#L366) | 366 | `"                entry.update(classify_source(source_identity_url))"` | — |
| [SRC-59CF4B7DE8-L000367](../../agents/research.py#L367) | 367 | `"                accumulated[url] = entry"` | — |
| [SRC-59CF4B7DE8-L000368](../../agents/research.py#L368) | 368 | `"            elif source.get(\"publisher_url\") and not entry.get(\"publisher_url\"):"` | — |
| [SRC-59CF4B7DE8-L000369](../../agents/research.py#L369) | 369 | `"                entry[\"publisher_url\"] = _compact(source.get(\"publisher_url\"), 2048)"` | — |
| [SRC-59CF4B7DE8-L000370](../../agents/research.py#L370) | 370 | `"                entry[\"publisher_name\"] = _compact(source.get(\"publisher_name\") or \"\", 200)"` | — |
| [SRC-59CF4B7DE8-L000371](../../agents/research.py#L371) | 371 | `"                entry[\"publisher_domain\"] = _compact(source.get(\"publisher_domain\") or \"\", 300)"` | — |
| [SRC-59CF4B7DE8-L000372](../../agents/research.py#L372) | 372 | `"                entry.update(classify_source(entry[\"publisher_url\"]))"` | — |
| [SRC-59CF4B7DE8-L000373](../../agents/research.py#L373) | 373 | `"            entry[\"rank_score\"] += 1.0 / (60 + position)"` | — |
| [SRC-59CF4B7DE8-L000374](../../agents/research.py#L374) | 374 | `"            entry[\"best_raw_rank\"] = min(entry[\"best_raw_rank\"], position)"` | — |
| [SRC-59CF4B7DE8-L000375](../../agents/research.py#L375) | 375 | `"            if provider and provider not in entry[\"providers\"]:"` | — |
| [SRC-59CF4B7DE8-L000376](../../agents/research.py#L376) | 376 | `"                entry[\"providers\"].append(provider)"` | — |
| [SRC-59CF4B7DE8-L000377](../../agents/research.py#L377) | 377 | `"            if query and query not in entry[\"queries\"]:"` | — |
| [SRC-59CF4B7DE8-L000378](../../agents/research.py#L378) | 378 | `"                entry[\"queries\"].append(query)"` | — |
| [SRC-59CF4B7DE8-L000379](../../agents/research.py#L379) | 379 | `"            if len(str(source.get(\"snippet\") or \"\")) > len(entry[\"snippet\"]):"` | — |
| [SRC-59CF4B7DE8-L000380](../../agents/research.py#L380) | 380 | `"                entry[\"snippet\"] = _compact(source.get(\"snippet\"), 1800)"` | — |
| [SRC-59CF4B7DE8-L000381](../../agents/research.py#L381) | 381 | `"            if source.get(\"published_at\") and not entry.get(\"published_at\"):"` | — |
| [SRC-59CF4B7DE8-L000382](../../agents/research.py#L382) | 382 | `"                entry[\"published_at\"] = _compact(source[\"published_at\"], 100)"` | — |
| [SRC-59CF4B7DE8-L000383](../../agents/research.py#L383) | 383 | `"            if source.get(\"page_text\") and not entry[\"page_text\"]:"` | — |
| [SRC-59CF4B7DE8-L000384](../../agents/research.py#L384) | 384 | `"                entry[\"page_text\"] = _compact(source[\"page_text\"], 12_000)"` | — |
| [SRC-59CF4B7DE8-L000385](../../agents/research.py#L385) | 385 | `"                entry[\"page_fetched\"] = True"` | — |
| [SRC-59CF4B7DE8-L000386](../../agents/research.py#L386) | 386 | `"    # A cross-query result gets a modest consensus bonus; official/academic sources"` | — |
| [SRC-59CF4B7DE8-L000387](../../agents/research.py#L387) | 387 | `"    # get a small prior, never enough to override actual query relevance."` | — |
| [SRC-59CF4B7DE8-L000388](../../agents/research.py#L388) | 388 | `"    for entry in accumulated.values():"` | — |
| [SRC-59CF4B7DE8-L000389](../../agents/research.py#L389) | 389 | `"        entry[\"rank_score\"] += min(len(entry[\"queries\"]), 4) * 0.00015"` | — |
| [SRC-59CF4B7DE8-L000390](../../agents/research.py#L390) | 390 | `"        if entry[\"source_class\"] in {\"government\", \"academic\"}:"` | — |
| [SRC-59CF4B7DE8-L000391](../../agents/research.py#L391) | 391 | `"            entry[\"rank_score\"] += 0.0001"` | — |
| [SRC-59CF4B7DE8-L000392](../../agents/research.py#L392) | 392 | `"        if \"user_supplied_url\" in entry[\"providers\"]:"` | — |
| [SRC-59CF4B7DE8-L000393](../../agents/research.py#L393) | 393 | `"            entry[\"rank_score\"] += 0.5"` | — |
| [SRC-59CF4B7DE8-L000394](../../agents/research.py#L394) | 394 | `"    ranked = sorted(accumulated.values(), key=lambda item: item[\"rank_score\"], reverse=True)"` | — |
| [SRC-59CF4B7DE8-L000395](../../agents/research.py#L395) | 395 | `"    return ranked[:max(1, min(int(limit), MAX_FUSED_RESULTS))]"` | — |
| [SRC-59CF4B7DE8-L000396](../../agents/research.py#L396) | 396 | `""` | — |
| [SRC-59CF4B7DE8-L000397](../../agents/research.py#L397) | 397 | `""` | — |
| [SRC-59CF4B7DE8-L000398](../../agents/research.py#L398) | 398 | `""` | — |
| [SRC-59CF4B7DE8-L000399](../../agents/research.py#L399) | 399 | `"def _parse_publication_date(value: Any, now: datetime \| None = None) -> datetime \| None:"` | — |
| [SRC-59CF4B7DE8-L000400](../../agents/research.py#L400) | 400 | `"    \"\"\"Parse common search/RSS publication dates without guessing missing dates.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000401](../../agents/research.py#L401) | 401 | `"    if not isinstance(value, str) or not value.strip():"` | — |
| [SRC-59CF4B7DE8-L000402](../../agents/research.py#L402) | 402 | `"        return None"` | — |
| [SRC-59CF4B7DE8-L000403](../../agents/research.py#L403) | 403 | `"    raw = value.strip()"` | — |
| [SRC-59CF4B7DE8-L000404](../../agents/research.py#L404) | 404 | `"    current = now or datetime.now(UTC)"` | — |
| [SRC-59CF4B7DE8-L000405](../../agents/research.py#L405) | 405 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000406](../../agents/research.py#L406) | 406 | `"        parsed = parsedate_to_datetime(raw)"` | — |
| [SRC-59CF4B7DE8-L000407](../../agents/research.py#L407) | 407 | `"        if parsed:"` | — |
| [SRC-59CF4B7DE8-L000408](../../agents/research.py#L408) | 408 | `"            return parsed.replace(tzinfo=parsed.tzinfo or UTC).astimezone(UTC)"` | — |
| [SRC-59CF4B7DE8-L000409](../../agents/research.py#L409) | 409 | `"    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-59CF4B7DE8-L000410](../../agents/research.py#L410) | 410 | `"        pass"` | — |
| [SRC-59CF4B7DE8-L000411](../../agents/research.py#L411) | 411 | `"    iso_value = raw.replace(\"Z\", \"+00:00\")"` | — |
| [SRC-59CF4B7DE8-L000412](../../agents/research.py#L412) | 412 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000413](../../agents/research.py#L413) | 413 | `"        parsed = datetime.fromisoformat(iso_value)"` | — |
| [SRC-59CF4B7DE8-L000414](../../agents/research.py#L414) | 414 | `"        return parsed.replace(tzinfo=parsed.tzinfo or UTC).astimezone(UTC)"` | — |
| [SRC-59CF4B7DE8-L000415](../../agents/research.py#L415) | 415 | `"    except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-59CF4B7DE8-L000416](../../agents/research.py#L416) | 416 | `"        pass"` | — |
| [SRC-59CF4B7DE8-L000417](../../agents/research.py#L417) | 417 | `"    for date_format in (\"%b %d, %Y\", \"%B %d, %Y\", \"%Y/%m/%d\", \"%d %b %Y\"):"` | — |
| [SRC-59CF4B7DE8-L000418](../../agents/research.py#L418) | 418 | `"        try:"` | — |
| [SRC-59CF4B7DE8-L000419](../../agents/research.py#L419) | 419 | `"            return datetime.strptime(raw, date_format).replace(tzinfo=UTC)"` | — |
| [SRC-59CF4B7DE8-L000420](../../agents/research.py#L420) | 420 | `"        except ValueError:"` | — |
| [SRC-59CF4B7DE8-L000421](../../agents/research.py#L421) | 421 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000422](../../agents/research.py#L422) | 422 | `"    match = re.search(r\"(\\d+)\\s+(hour\|day\|week\|month\|year)s?\\s+ago\", raw, re.IGNORECASE)"` | — |
| [SRC-59CF4B7DE8-L000423](../../agents/research.py#L423) | 423 | `"    if match:"` | — |
| [SRC-59CF4B7DE8-L000424](../../agents/research.py#L424) | 424 | `"        amount = int(match.group(1))"` | — |
| [SRC-59CF4B7DE8-L000425](../../agents/research.py#L425) | 425 | `"        unit = match.group(2).lower()"` | — |
| [SRC-59CF4B7DE8-L000426](../../agents/research.py#L426) | 426 | `"        durations = {"` | — |
| [SRC-59CF4B7DE8-L000427](../../agents/research.py#L427) | 427 | `"            \"hour\": timedelta(hours=amount),"` | — |
| [SRC-59CF4B7DE8-L000428](../../agents/research.py#L428) | 428 | `"            \"day\": timedelta(days=amount),"` | — |
| [SRC-59CF4B7DE8-L000429](../../agents/research.py#L429) | 429 | `"            \"week\": timedelta(days=7 * amount),"` | — |
| [SRC-59CF4B7DE8-L000430](../../agents/research.py#L430) | 430 | `"            \"month\": timedelta(days=30 * amount),"` | — |
| [SRC-59CF4B7DE8-L000431](../../agents/research.py#L431) | 431 | `"            \"year\": timedelta(days=365 * amount),"` | — |
| [SRC-59CF4B7DE8-L000432](../../agents/research.py#L432) | 432 | `"        }"` | — |
| [SRC-59CF4B7DE8-L000433](../../agents/research.py#L433) | 433 | `"        return current - durations[unit]"` | — |
| [SRC-59CF4B7DE8-L000434](../../agents/research.py#L434) | 434 | `"    if raw.lower() in {\"today\", \"just now\", \"now\"}:"` | — |
| [SRC-59CF4B7DE8-L000435](../../agents/research.py#L435) | 435 | `"        return current"` | — |
| [SRC-59CF4B7DE8-L000436](../../agents/research.py#L436) | 436 | `"    if raw.lower() == \"yesterday\":"` | — |
| [SRC-59CF4B7DE8-L000437](../../agents/research.py#L437) | 437 | `"        return current - timedelta(days=1)"` | — |
| [SRC-59CF4B7DE8-L000438](../../agents/research.py#L438) | 438 | `"    return None"` | — |
| [SRC-59CF4B7DE8-L000439](../../agents/research.py#L439) | 439 | `""` | — |
| [SRC-59CF4B7DE8-L000440](../../agents/research.py#L440) | 440 | `""` | — |
| [SRC-59CF4B7DE8-L000441](../../agents/research.py#L441) | 441 | `"def evidence_signal_report("` | — |
| [SRC-59CF4B7DE8-L000442](../../agents/research.py#L442) | 442 | `"    sources: list[dict[str, Any]],"` | — |
| [SRC-59CF4B7DE8-L000443](../../agents/research.py#L443) | 443 | `"    freshness: str = \"any\","` | — |
| [SRC-59CF4B7DE8-L000444](../../agents/research.py#L444) | 444 | `"    now: datetime \| None = None,"` | — |
| [SRC-59CF4B7DE8-L000445](../../agents/research.py#L445) | 445 | `") -> dict[str, Any]:"` | — |
| [SRC-59CF4B7DE8-L000446](../../agents/research.py#L446) | 446 | `"    \"\"\"Summarize research coverage; signals describe evidence coverage, not factual truth.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000447](../../agents/research.py#L447) | 447 | `"    current = now or datetime.now(UTC)"` | — |
| [SRC-59CF4B7DE8-L000448](../../agents/research.py#L448) | 448 | `"    valid_sources = [source for source in sources if isinstance(source, dict) and source.get(\"url\")]"` | — |
| [SRC-59CF4B7DE8-L000449](../../agents/research.py#L449) | 449 | `"    domains = {"` | — |
| [SRC-59CF4B7DE8-L000450](../../agents/research.py#L450) | 450 | `"        registrable_domain("` | — |
| [SRC-59CF4B7DE8-L000451](../../agents/research.py#L451) | 451 | `"            source.get(\"domain\") or urlparse(str(source.get(\"url\") or \"\")).hostname or \"\""` | — |
| [SRC-59CF4B7DE8-L000452](../../agents/research.py#L452) | 452 | `"        )"` | — |
| [SRC-59CF4B7DE8-L000453](../../agents/research.py#L453) | 453 | `"        for source in valid_sources"` | — |
| [SRC-59CF4B7DE8-L000454](../../agents/research.py#L454) | 454 | `"        if source.get(\"domain\") or source.get(\"url\")"` | — |
| [SRC-59CF4B7DE8-L000455](../../agents/research.py#L455) | 455 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000456](../../agents/research.py#L456) | 456 | `"    domains.discard(\"\")"` | — |
| [SRC-59CF4B7DE8-L000457](../../agents/research.py#L457) | 457 | `"    providers: set[str] = set()"` | — |
| [SRC-59CF4B7DE8-L000458](../../agents/research.py#L458) | 458 | `"    for source in valid_sources:"` | — |
| [SRC-59CF4B7DE8-L000459](../../agents/research.py#L459) | 459 | `"        candidate_providers = source.get(\"providers\", [])"` | — |
| [SRC-59CF4B7DE8-L000460](../../agents/research.py#L460) | 460 | `"        if isinstance(candidate_providers, list):"` | — |
| [SRC-59CF4B7DE8-L000461](../../agents/research.py#L461) | 461 | `"            providers.update(str(item) for item in candidate_providers if item)"` | — |
| [SRC-59CF4B7DE8-L000462](../../agents/research.py#L462) | 462 | `"        elif source.get(\"provider\"):"` | — |
| [SRC-59CF4B7DE8-L000463](../../agents/research.py#L463) | 463 | `"            providers.add(str(source[\"provider\"]))"` | — |
| [SRC-59CF4B7DE8-L000464](../../agents/research.py#L464) | 464 | `"    classes = [str(source.get(\"source_class\") or \"general\") for source in valid_sources]"` | — |
| [SRC-59CF4B7DE8-L000465](../../agents/research.py#L465) | 465 | `"    primary_count = sum(item in {\"government\", \"academic\", \"official\"} for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000466](../../agents/research.py#L466) | 466 | `"    news_count = sum(item == \"news\" for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000467](../../agents/research.py#L467) | 467 | `"    social_count = sum(item == \"social\" for item in classes)"` | — |
| [SRC-59CF4B7DE8-L000468](../../agents/research.py#L468) | 468 | `"    pages_read = sum(bool(source.get(\"page_fetched\")) for source in valid_sources)"` | — |
| [SRC-59CF4B7DE8-L000469](../../agents/research.py#L469) | 469 | `"    dates = ["` | — |
| [SRC-59CF4B7DE8-L000470](../../agents/research.py#L470) | 470 | `"        parsed"` | — |
| [SRC-59CF4B7DE8-L000471](../../agents/research.py#L471) | 471 | `"        for source in valid_sources"` | — |
| [SRC-59CF4B7DE8-L000472](../../agents/research.py#L472) | 472 | `"        if (parsed := _parse_publication_date(source.get(\"published_at\"), current)) is not None"` | — |
| [SRC-59CF4B7DE8-L000473](../../agents/research.py#L473) | 473 | `"    ]"` | — |
| [SRC-59CF4B7DE8-L000474](../../agents/research.py#L474) | 474 | `"    recent_days = 7 if freshness == \"current\" else 30"` | — |
| [SRC-59CF4B7DE8-L000475](../../agents/research.py#L475) | 475 | `"    recent_count = sum((current - parsed).total_seconds() >= 0 and"` | — |
| [SRC-59CF4B7DE8-L000476](../../agents/research.py#L476) | 476 | `"                       (current - parsed) <= timedelta(days=recent_days) for parsed in dates)"` | — |
| [SRC-59CF4B7DE8-L000477](../../agents/research.py#L477) | 477 | `"    future_dates = sum(parsed > current + timedelta(days=1) for parsed in dates)"` | — |
| [SRC-59CF4B7DE8-L000478](../../agents/research.py#L478) | 478 | `"    unique_sources = len(valid_sources)"` | — |
| [SRC-59CF4B7DE8-L000479](../../agents/research.py#L479) | 479 | `"    # Evidence coverage uses several independent dimensions and is deliberately not a"` | — |
| [SRC-59CF4B7DE8-L000480](../../agents/research.py#L480) | 480 | `"    # probability that any factual claim is true."` | — |
| [SRC-59CF4B7DE8-L000481](../../agents/research.py#L481) | 481 | `"    coverage_points = 0"` | — |
| [SRC-59CF4B7DE8-L000482](../../agents/research.py#L482) | 482 | `"    coverage_points += min(unique_sources, 10) * 3"` | — |
| [SRC-59CF4B7DE8-L000483](../../agents/research.py#L483) | 483 | `"    coverage_points += min(len(domains), 8) * 4"` | — |
| [SRC-59CF4B7DE8-L000484](../../agents/research.py#L484) | 484 | `"    coverage_points += min(len(providers), 4) * 5"` | — |
| [SRC-59CF4B7DE8-L000485](../../agents/research.py#L485) | 485 | `"    coverage_points += min(pages_read, 8) * 3"` | — |
| [SRC-59CF4B7DE8-L000486](../../agents/research.py#L486) | 486 | `"    coverage_points += min(primary_count, 4) * 4"` | — |
| [SRC-59CF4B7DE8-L000487](../../agents/research.py#L487) | 487 | `"    coverage_points += min(len(dates), 8) * 2"` | — |
| [SRC-59CF4B7DE8-L000488](../../agents/research.py#L488) | 488 | `"    coverage_score = min(100, coverage_points)"` | — |
| [SRC-59CF4B7DE8-L000489](../../agents/research.py#L489) | 489 | `"    if unique_sources >= 8 and len(domains) >= 5 and len(providers) >= 2 and pages_read >= 3:"` | — |
| [SRC-59CF4B7DE8-L000490](../../agents/research.py#L490) | 490 | `"        coverage_level = \"متعدد المصادر\""` | — |
| [SRC-59CF4B7DE8-L000491](../../agents/research.py#L491) | 491 | `"    elif unique_sources >= 4 and len(domains) >= 3 and len(providers) >= 1:"` | — |
| [SRC-59CF4B7DE8-L000492](../../agents/research.py#L492) | 492 | `"        coverage_level = \"متوسط\""` | — |
| [SRC-59CF4B7DE8-L000493](../../agents/research.py#L493) | 493 | `"    else:"` | — |
| [SRC-59CF4B7DE8-L000494](../../agents/research.py#L494) | 494 | `"        coverage_level = \"محدود\""` | — |
| [SRC-59CF4B7DE8-L000495](../../agents/research.py#L495) | 495 | `""` | — |
| [SRC-59CF4B7DE8-L000496](../../agents/research.py#L496) | 496 | `"    warnings: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000497](../../agents/research.py#L497) | 497 | `"    if unique_sources == 0:"` | — |
| [SRC-59CF4B7DE8-L000498](../../agents/research.py#L498) | 498 | `"        warnings.append(\"لا توجد مصادر قابلة للاستشهاد؛ لا تستنتج حقائق من عدم وجود نتائج.\")"` | — |
| [SRC-59CF4B7DE8-L000499](../../agents/research.py#L499) | 499 | `"    if len(domains) < 3:"` | — |
| [SRC-59CF4B7DE8-L000500](../../agents/research.py#L500) | 500 | `"        warnings.append(\"تنوع النطاقات محدود؛ لا تعتبر تكرار النتيجة تأكيدًا مستقلًا.\")"` | — |
| [SRC-59CF4B7DE8-L000501](../../agents/research.py#L501) | 501 | `"    if pages_read < 2 and unique_sources:"` | — |
| [SRC-59CF4B7DE8-L000502](../../agents/research.py#L502) | 502 | `"        warnings.append(\"تمت قراءة أقل من صفحتين مباشرة؛ بعض الأدلة مقتطفات من محركات البحث فقط.\")"` | — |
| [SRC-59CF4B7DE8-L000503](../../agents/research.py#L503) | 503 | `"    if freshness == \"current\":"` | — |
| [SRC-59CF4B7DE8-L000504](../../agents/research.py#L504) | 504 | `"        if not dates:"` | — |
| [SRC-59CF4B7DE8-L000505](../../agents/research.py#L505) | 505 | `"            warnings.append(\"لا تتوفر تواريخ نشر قابلة للتحليل؛ حداثة النتائج غير مؤكدة.\")"` | — |
| [SRC-59CF4B7DE8-L000506](../../agents/research.py#L506) | 506 | `"        elif recent_count == 0:"` | — |
| [SRC-59CF4B7DE8-L000507](../../agents/research.py#L507) | 507 | `"            warnings.append(f\"لم يُعثر على مصدر مؤرخ خلال آخر {recent_days} يومًا ضمن التواريخ القابلة للتحليل.\")"` | — |
| [SRC-59CF4B7DE8-L000508](../../agents/research.py#L508) | 508 | `"    if future_dates:"` | — |
| [SRC-59CF4B7DE8-L000509](../../agents/research.py#L509) | 509 | `"        warnings.append(\"توجد تواريخ مستقبلية غير متوقعة؛ يجب مراجعتها يدويًا.\")"` | — |
| [SRC-59CF4B7DE8-L000510](../../agents/research.py#L510) | 510 | `"    if social_count and primary_count == 0:"` | — |
| [SRC-59CF4B7DE8-L000511](../../agents/research.py#L511) | 511 | `"        warnings.append(\"المصادر اجتماعية فقط دون مصدر رسمي/أكاديمي؛ تعامل معها كآراء أو إشارات لا كحقائق مثبتة.\")"` | — |
| [SRC-59CF4B7DE8-L000512](../../agents/research.py#L512) | 512 | `"    return {"` | — |
| [SRC-59CF4B7DE8-L000513](../../agents/research.py#L513) | 513 | `"        \"unique_sources\": unique_sources,"` | — |
| [SRC-59CF4B7DE8-L000514](../../agents/research.py#L514) | 514 | `"        \"unique_domains\": len(domains),"` | — |
| [SRC-59CF4B7DE8-L000515](../../agents/research.py#L515) | 515 | `"        \"providers_count\": len(providers),"` | — |
| [SRC-59CF4B7DE8-L000516](../../agents/research.py#L516) | 516 | `"        \"providers\": sorted(providers),"` | — |
| [SRC-59CF4B7DE8-L000517](../../agents/research.py#L517) | 517 | `"        \"pages_read\": pages_read,"` | — |
| [SRC-59CF4B7DE8-L000518](../../agents/research.py#L518) | 518 | `"        \"primary_sources\": primary_count,"` | — |
| [SRC-59CF4B7DE8-L000519](../../agents/research.py#L519) | 519 | `"        \"news_sources\": news_count,"` | — |
| [SRC-59CF4B7DE8-L000520](../../agents/research.py#L520) | 520 | `"        \"social_sources\": social_count,"` | — |
| [SRC-59CF4B7DE8-L000521](../../agents/research.py#L521) | 521 | `"        \"dated_sources\": len(dates),"` | — |
| [SRC-59CF4B7DE8-L000522](../../agents/research.py#L522) | 522 | `"        \"recent_sources\": recent_count,"` | — |
| [SRC-59CF4B7DE8-L000523](../../agents/research.py#L523) | 523 | `"        \"undated_sources\": max(0, unique_sources - len(dates)),"` | — |
| [SRC-59CF4B7DE8-L000524](../../agents/research.py#L524) | 524 | `"        \"date_coverage_percent\": round(100 * len(dates) / unique_sources) if unique_sources else 0,"` | — |
| [SRC-59CF4B7DE8-L000525](../../agents/research.py#L525) | 525 | `"        \"coverage_score\": coverage_score,"` | — |
| [SRC-59CF4B7DE8-L000526](../../agents/research.py#L526) | 526 | `"        \"coverage_level\": coverage_level,"` | — |
| [SRC-59CF4B7DE8-L000527](../../agents/research.py#L527) | 527 | `"        \"score_meaning\": \"مؤشر تغطية وتنوع الأدلة، وليس احتمال صحة الإجابة.\","` | — |
| [SRC-59CF4B7DE8-L000528](../../agents/research.py#L528) | 528 | `"        \"warnings\": warnings,"` | — |
| [SRC-59CF4B7DE8-L000529](../../agents/research.py#L529) | 529 | `"    }"` | — |
| [SRC-59CF4B7DE8-L000530](../../agents/research.py#L530) | 530 | `""` | — |
| [SRC-59CF4B7DE8-L000531](../../agents/research.py#L531) | 531 | `""` | — |
| [SRC-59CF4B7DE8-L000532](../../agents/research.py#L532) | 532 | `""` | — |
| [SRC-59CF4B7DE8-L000533](../../agents/research.py#L533) | 533 | `"# ---------------------------------------------------------------------------"` | — |
| [SRC-59CF4B7DE8-L000534](../../agents/research.py#L534) | 534 | `"# Evidence-aware helpers"` | — |
| [SRC-59CF4B7DE8-L000535](../../agents/research.py#L535) | 535 | `"# ---------------------------------------------------------------------------"` | — |
| [SRC-59CF4B7DE8-L000536](../../agents/research.py#L536) | 536 | `""` | — |
| [SRC-59CF4B7DE8-L000537](../../agents/research.py#L537) | 537 | `"_RELEVANCE_STOPWORDS = {"` | — |
| [SRC-59CF4B7DE8-L000538](../../agents/research.py#L538) | 538 | `"    \"the\", \"a\", \"an\", \"of\", \"in\", \"on\", \"at\", \"to\", \"for\","` | — |
| [SRC-59CF4B7DE8-L000539](../../agents/research.py#L539) | 539 | `"    \"is\", \"are\", \"was\", \"were\", \"be\", \"been\", \"being\","` | — |
| [SRC-59CF4B7DE8-L000540](../../agents/research.py#L540) | 540 | `"    \"and\", \"or\", \"but\", \"not\", \"with\", \"without\","` | — |
| [SRC-59CF4B7DE8-L000541](../../agents/research.py#L541) | 541 | `"    \"this\", \"that\", \"these\", \"those\", \"it\", \"its\","` | — |
| [SRC-59CF4B7DE8-L000542](../../agents/research.py#L542) | 542 | `"}"` | — |
| [SRC-59CF4B7DE8-L000543](../../agents/research.py#L543) | 543 | `""` | — |
| [SRC-59CF4B7DE8-L000544](../../agents/research.py#L544) | 544 | `"_OFFICIAL_CLASSES = {\"government\", \"education\", \"official\"}"` | — |
| [SRC-59CF4B7DE8-L000545](../../agents/research.py#L545) | 545 | `""` | — |
| [SRC-59CF4B7DE8-L000546](../../agents/research.py#L546) | 546 | `""` | — |
| [SRC-59CF4B7DE8-L000547](../../agents/research.py#L547) | 547 | `"def _tokenize(text: str) -> set:"` | — |
| [SRC-59CF4B7DE8-L000548](../../agents/research.py#L548) | 548 | `"    if not text:"` | — |
| [SRC-59CF4B7DE8-L000549](../../agents/research.py#L549) | 549 | `"        return set()"` | — |
| [SRC-59CF4B7DE8-L000550](../../agents/research.py#L550) | 550 | `"    norm = _normalize_arabic(text.casefold())"` | — |
| [SRC-59CF4B7DE8-L000551](../../agents/research.py#L551) | 551 | `"    tokens = re.findall(r\"\\w+\", norm, flags=re.UNICODE)"` | — |
| [SRC-59CF4B7DE8-L000552](../../agents/research.py#L552) | 552 | `"    return {t for t in tokens if len(t) >= 3 and t not in _RELEVANCE_STOPWORDS}"` | — |
| [SRC-59CF4B7DE8-L000553](../../agents/research.py#L553) | 553 | `""` | — |
| [SRC-59CF4B7DE8-L000554](../../agents/research.py#L554) | 554 | `""` | — |
| [SRC-59CF4B7DE8-L000555](../../agents/research.py#L555) | 555 | `"def source_relevance_score(src, query: str) -> dict:"` | — |
| [SRC-59CF4B7DE8-L000556](../../agents/research.py#L556) | 556 | `"    if not isinstance(src, dict):"` | — |
| [SRC-59CF4B7DE8-L000557](../../agents/research.py#L557) | 557 | `"        return {\"accepted\": False, \"score\": 0, \"reason\": \"malformed\"}"` | — |
| [SRC-59CF4B7DE8-L000558](../../agents/research.py#L558) | 558 | `""` | — |
| [SRC-59CF4B7DE8-L000559](../../agents/research.py#L559) | 559 | `"    title = str(src.get(\"title\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000560](../../agents/research.py#L560) | 560 | `"    snippet = str(src.get(\"snippet\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000561](../../agents/research.py#L561) | 561 | `"    page_text = str(src.get(\"page_text\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000562](../../agents/research.py#L562) | 562 | `"    source_class = str(src.get(\"source_class\") or \"general\").lower()"` | — |
| [SRC-59CF4B7DE8-L000563](../../agents/research.py#L563) | 563 | `""` | — |
| [SRC-59CF4B7DE8-L000564](../../agents/research.py#L564) | 564 | `"    q_tokens = _tokenize(query)"` | — |
| [SRC-59CF4B7DE8-L000565](../../agents/research.py#L565) | 565 | `"    if not q_tokens:"` | — |
| [SRC-59CF4B7DE8-L000566](../../agents/research.py#L566) | 566 | `"        return {\"accepted\": False, \"score\": 0, \"reason\": \"no_query_tokens\"}"` | — |
| [SRC-59CF4B7DE8-L000567](../../agents/research.py#L567) | 567 | `""` | — |
| [SRC-59CF4B7DE8-L000568](../../agents/research.py#L568) | 568 | `"    t_tokens = _tokenize(title)"` | — |
| [SRC-59CF4B7DE8-L000569](../../agents/research.py#L569) | 569 | `"    s_tokens = _tokenize(snippet)"` | — |
| [SRC-59CF4B7DE8-L000570](../../agents/research.py#L570) | 570 | `"    p_tokens = _tokenize(page_text[:3000])"` | — |
| [SRC-59CF4B7DE8-L000571](../../agents/research.py#L571) | 571 | `""` | — |
| [SRC-59CF4B7DE8-L000572](../../agents/research.py#L572) | 572 | `"    title_ratio = len(q_tokens & t_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000573](../../agents/research.py#L573) | 573 | `"    snippet_ratio = len(q_tokens & s_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000574](../../agents/research.py#L574) | 574 | `"    page_ratio = len(q_tokens & p_tokens) / max(len(q_tokens), 1)"` | — |
| [SRC-59CF4B7DE8-L000575](../../agents/research.py#L575) | 575 | `""` | — |
| [SRC-59CF4B7DE8-L000576](../../agents/research.py#L576) | 576 | `"    score = int(title_ratio * 15 + snippet_ratio * 20 + page_ratio * 5)"` | — |
| [SRC-59CF4B7DE8-L000577](../../agents/research.py#L577) | 577 | `""` | — |
| [SRC-59CF4B7DE8-L000578](../../agents/research.py#L578) | 578 | `"    if source_class in _OFFICIAL_CLASSES:"` | — |
| [SRC-59CF4B7DE8-L000579](../../agents/research.py#L579) | 579 | `"        if score >= 5:"` | — |
| [SRC-59CF4B7DE8-L000580](../../agents/research.py#L580) | 580 | `"            return {\"accepted\": True, \"score\": score, \"reason\": \"accepted\"}"` | — |
| [SRC-59CF4B7DE8-L000581](../../agents/research.py#L581) | 581 | `"        return {\"accepted\": True, \"score\": score,"` | — |
| [SRC-59CF4B7DE8-L000582](../../agents/research.py#L582) | 582 | `"                \"reason\": \"kept_official_despite_low_overlap\"}"` | — |
| [SRC-59CF4B7DE8-L000583](../../agents/research.py#L583) | 583 | `""` | — |
| [SRC-59CF4B7DE8-L000584](../../agents/research.py#L584) | 584 | `"    if score >= 18:"` | — |
| [SRC-59CF4B7DE8-L000585](../../agents/research.py#L585) | 585 | `"        return {\"accepted\": True, \"score\": score, \"reason\": \"accepted\"}"` | — |
| [SRC-59CF4B7DE8-L000586](../../agents/research.py#L586) | 586 | `"    return {\"accepted\": False, \"score\": score, \"reason\": \"low_overlap\"}"` | — |
| [SRC-59CF4B7DE8-L000587](../../agents/research.py#L587) | 587 | `""` | — |
| [SRC-59CF4B7DE8-L000588](../../agents/research.py#L588) | 588 | `""` | — |
| [SRC-59CF4B7DE8-L000589](../../agents/research.py#L589) | 589 | `"def filter_relevant_sources(sources, query: str, extra_queries=None):"` | — |
| [SRC-59CF4B7DE8-L000590](../../agents/research.py#L590) | 590 | `"    kept = []"` | — |
| [SRC-59CF4B7DE8-L000591](../../agents/research.py#L591) | 591 | `"    diag = []"` | — |
| [SRC-59CF4B7DE8-L000592](../../agents/research.py#L592) | 592 | `"    seen_urls = set()"` | — |
| [SRC-59CF4B7DE8-L000593](../../agents/research.py#L593) | 593 | `"    seen_titles = set()"` | — |
| [SRC-59CF4B7DE8-L000594](../../agents/research.py#L594) | 594 | `"    combined = \" \".join([query] + list(extra_queries or []))"` | — |
| [SRC-59CF4B7DE8-L000595](../../agents/research.py#L595) | 595 | `""` | — |
| [SRC-59CF4B7DE8-L000596](../../agents/research.py#L596) | 596 | `"    for src in sources or []:"` | — |
| [SRC-59CF4B7DE8-L000597](../../agents/research.py#L597) | 597 | `"        if not isinstance(src, dict):"` | — |
| [SRC-59CF4B7DE8-L000598](../../agents/research.py#L598) | 598 | `"            diag.append({\"reason\": \"malformed\", \"url\": \"\"})"` | — |
| [SRC-59CF4B7DE8-L000599](../../agents/research.py#L599) | 599 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000600](../../agents/research.py#L600) | 600 | `"        url = str(src.get(\"url\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000601](../../agents/research.py#L601) | 601 | `"        domain = str(src.get(\"domain\") or \"\").lower()"` | — |
| [SRC-59CF4B7DE8-L000602](../../agents/research.py#L602) | 602 | `"        title = str(src.get(\"title\") or \"\").strip()"` | — |
| [SRC-59CF4B7DE8-L000603](../../agents/research.py#L603) | 603 | `"        url_key = url.rstrip(\"/\").lower()"` | — |
| [SRC-59CF4B7DE8-L000604](../../agents/research.py#L604) | 604 | `"        title_key = title.lower() + \"\|\" + domain"` | — |
| [SRC-59CF4B7DE8-L000605](../../agents/research.py#L605) | 605 | `""` | — |
| [SRC-59CF4B7DE8-L000606](../../agents/research.py#L606) | 606 | `"        if url_key and url_key in seen_urls:"` | — |
| [SRC-59CF4B7DE8-L000607](../../agents/research.py#L607) | 607 | `"            diag.append({\"reason\": \"duplicate_url\", \"url\": url})"` | — |
| [SRC-59CF4B7DE8-L000608](../../agents/research.py#L608) | 608 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000609](../../agents/research.py#L609) | 609 | `"        if title and title_key in seen_titles:"` | — |
| [SRC-59CF4B7DE8-L000610](../../agents/research.py#L610) | 610 | `"            diag.append({\"reason\": \"duplicate_title_domain\", \"url\": url})"` | — |
| [SRC-59CF4B7DE8-L000611](../../agents/research.py#L611) | 611 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000612](../../agents/research.py#L612) | 612 | `""` | — |
| [SRC-59CF4B7DE8-L000613](../../agents/research.py#L613) | 613 | `"        rel = source_relevance_score(src, combined)"` | — |
| [SRC-59CF4B7DE8-L000614](../../agents/research.py#L614) | 614 | `"        if not rel[\"accepted\"]:"` | — |
| [SRC-59CF4B7DE8-L000615](../../agents/research.py#L615) | 615 | `"            diag.append({\"reason\": rel[\"reason\"], \"url\": url, \"score\": rel[\"score\"]})"` | — |
| [SRC-59CF4B7DE8-L000616](../../agents/research.py#L616) | 616 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000617](../../agents/research.py#L617) | 617 | `""` | — |
| [SRC-59CF4B7DE8-L000618](../../agents/research.py#L618) | 618 | `"        kept.append(src)"` | — |
| [SRC-59CF4B7DE8-L000619](../../agents/research.py#L619) | 619 | `"        if url_key:"` | — |
| [SRC-59CF4B7DE8-L000620](../../agents/research.py#L620) | 620 | `"            seen_urls.add(url_key)"` | — |
| [SRC-59CF4B7DE8-L000621](../../agents/research.py#L621) | 621 | `"        if title:"` | — |
| [SRC-59CF4B7DE8-L000622](../../agents/research.py#L622) | 622 | `"            seen_titles.add(title_key)"` | — |
| [SRC-59CF4B7DE8-L000623](../../agents/research.py#L623) | 623 | `"    return kept, diag"` | — |
| [SRC-59CF4B7DE8-L000624](../../agents/research.py#L624) | 624 | `""` | — |
| [SRC-59CF4B7DE8-L000625](../../agents/research.py#L625) | 625 | `""` | — |
| [SRC-59CF4B7DE8-L000626](../../agents/research.py#L626) | 626 | `"def decide_evidence_status(sources, pages_read: int = 0,"` | — |
| [SRC-59CF4B7DE8-L000627](../../agents/research.py#L627) | 627 | `"                           provider_failures: int = 0,"` | — |
| [SRC-59CF4B7DE8-L000628](../../agents/research.py#L628) | 628 | `"                           search_attempted: bool = True) -> dict:"` | — |
| [SRC-59CF4B7DE8-L000629](../../agents/research.py#L629) | 629 | `"    if not search_attempted:"` | — |
| [SRC-59CF4B7DE8-L000630](../../agents/research.py#L630) | 630 | `"        return {\"evidence_status\": \"failed\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000631](../../agents/research.py#L631) | 631 | `""` | — |
| [SRC-59CF4B7DE8-L000632](../../agents/research.py#L632) | 632 | `"    domains = set()"` | — |
| [SRC-59CF4B7DE8-L000633](../../agents/research.py#L633) | 633 | `"    has_official = False"` | — |
| [SRC-59CF4B7DE8-L000634](../../agents/research.py#L634) | 634 | `"    for s in sources or []:"` | — |
| [SRC-59CF4B7DE8-L000635](../../agents/research.py#L635) | 635 | `"        if not isinstance(s, dict):"` | — |
| [SRC-59CF4B7DE8-L000636](../../agents/research.py#L636) | 636 | `"            continue"` | — |
| [SRC-59CF4B7DE8-L000637](../../agents/research.py#L637) | 637 | `"        d = str(s.get(\"domain\") or \"\").lower()"` | — |
| [SRC-59CF4B7DE8-L000638](../../agents/research.py#L638) | 638 | `"        if not d:"` | — |
| [SRC-59CF4B7DE8-L000639](../../agents/research.py#L639) | 639 | `"            url = str(s.get(\"url\") or \"\")"` | — |
| [SRC-59CF4B7DE8-L000640](../../agents/research.py#L640) | 640 | `"            if url:"` | — |
| [SRC-59CF4B7DE8-L000641](../../agents/research.py#L641) | 641 | `"                try:"` | — |
| [SRC-59CF4B7DE8-L000642](../../agents/research.py#L642) | 642 | `"                    from urllib.parse import urlparse"` | — |
| [SRC-59CF4B7DE8-L000643](../../agents/research.py#L643) | 643 | `"                    d = urlparse(url).netloc.lower()"` | — |
| [SRC-59CF4B7DE8-L000644](../../agents/research.py#L644) | 644 | `"                except Exception:"` | — |
| [SRC-59CF4B7DE8-L000645](../../agents/research.py#L645) | 645 | `"                    d = \"\""` | — |
| [SRC-59CF4B7DE8-L000646](../../agents/research.py#L646) | 646 | `"        if d:"` | — |
| [SRC-59CF4B7DE8-L000647](../../agents/research.py#L647) | 647 | `"            domains.add(d)"` | — |
| [SRC-59CF4B7DE8-L000648](../../agents/research.py#L648) | 648 | `"        if str(s.get(\"source_class\") or \"\").lower() in _OFFICIAL_CLASSES:"` | — |
| [SRC-59CF4B7DE8-L000649](../../agents/research.py#L649) | 649 | `"            has_official = True"` | — |
| [SRC-59CF4B7DE8-L000650](../../agents/research.py#L650) | 650 | `""` | — |
| [SRC-59CF4B7DE8-L000651](../../agents/research.py#L651) | 651 | `"    if not sources:"` | — |
| [SRC-59CF4B7DE8-L000652](../../agents/research.py#L652) | 652 | `"        if provider_failures > 0:"` | — |
| [SRC-59CF4B7DE8-L000653](../../agents/research.py#L653) | 653 | `"            return {\"evidence_status\": \"failed\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000654](../../agents/research.py#L654) | 654 | `"        return {\"evidence_status\": \"insufficient\", \"should_abstain\": True}"` | — |
| [SRC-59CF4B7DE8-L000655](../../agents/research.py#L655) | 655 | `""` | — |
| [SRC-59CF4B7DE8-L000656](../../agents/research.py#L656) | 656 | `"    if len(domains) >= 2 or has_official:"` | — |
| [SRC-59CF4B7DE8-L000657](../../agents/research.py#L657) | 657 | `"        return {\"evidence_status\": \"adequate\", \"should_abstain\": False}"` | — |
| [SRC-59CF4B7DE8-L000658](../../agents/research.py#L658) | 658 | `"    if len(domains) >= 1:"` | — |
| [SRC-59CF4B7DE8-L000659](../../agents/research.py#L659) | 659 | `"        return {\"evidence_status\": \"partial\", \"should_abstain\": False}"` | — |
| [SRC-59CF4B7DE8-L000660](../../agents/research.py#L660) | 660 | `"    return {\"evidence_status\": \"insufficient\", \"should_abstain\": True}"` | — |
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
| [SRC-1AE03B9EC3-L000025](../../agents/web_agent.py#L25) | 25 | `"from agents.answer_validation import audit_answer_integrity"` | — |
| [SRC-1AE03B9EC3-L000026](../../agents/web_agent.py#L26) | 26 | `"from agents.request_budget import RequestBudget, RequestBudgetExceeded"` | — |
| [SRC-1AE03B9EC3-L000027](../../agents/web_agent.py#L27) | 27 | `"from agents.research import ("` | — |
| [SRC-1AE03B9EC3-L000028](../../agents/web_agent.py#L28) | 28 | `"    MAX_PLAN_QUERIES,"` | — |
| [SRC-1AE03B9EC3-L000029](../../agents/web_agent.py#L29) | 29 | `"    SOCIAL_DOMAINS,"` | — |
| [SRC-1AE03B9EC3-L000030](../../agents/web_agent.py#L30) | 30 | `"    evidence_signal_report,"` | — |
| [SRC-1AE03B9EC3-L000031](../../agents/web_agent.py#L31) | 31 | `"    fallback_plan,"` | — |
| [SRC-1AE03B9EC3-L000032](../../agents/web_agent.py#L32) | 32 | `"    fuse_ranked_results,"` | — |
| [SRC-1AE03B9EC3-L000033](../../agents/web_agent.py#L33) | 33 | `"    registrable_domain,"` | — |
| [SRC-1AE03B9EC3-L000034](../../agents/web_agent.py#L34) | 34 | `"    validate_plan,"` | — |
| [SRC-1AE03B9EC3-L000035](../../agents/web_agent.py#L35) | 35 | `")"` | — |
| [SRC-1AE03B9EC3-L000036](../../agents/web_agent.py#L36) | 36 | `""` | — |
| [SRC-1AE03B9EC3-L000037](../../agents/web_agent.py#L37) | 37 | `"MAX_QUESTION_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000038](../../agents/web_agent.py#L38) | 38 | `"MAX_HISTORY_ITEMS = 8"` | — |
| [SRC-1AE03B9EC3-L000039](../../agents/web_agent.py#L39) | 39 | `"MAX_HISTORY_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000040](../../agents/web_agent.py#L40) | 40 | `"MAX_SEARCH_RESULTS = 18"` | — |
| [SRC-1AE03B9EC3-L000041](../../agents/web_agent.py#L41) | 41 | `"MAX_PROVIDER_RESULTS = 6"` | — |
| [SRC-1AE03B9EC3-L000042](../../agents/web_agent.py#L42) | 42 | `"MAX_FETCHED_PAGES = 8"` | — |
| [SRC-1AE03B9EC3-L000043](../../agents/web_agent.py#L43) | 43 | `"MAX_LLM_CITED_SOURCES = 12"` | — |
| [SRC-1AE03B9EC3-L000044](../../agents/web_agent.py#L44) | 44 | `"MAX_RESEARCH_WORKERS = 8"` | — |
| [SRC-1AE03B9EC3-L000045](../../agents/web_agent.py#L45) | 45 | `"MAX_PAGE_BYTES = 1_000_000"` | — |
| [SRC-1AE03B9EC3-L000046](../../agents/web_agent.py#L46) | 46 | `"MAX_PAGE_TEXT_CHARS = 12_000"` | — |
| [SRC-1AE03B9EC3-L000047](../../agents/web_agent.py#L47) | 47 | `"LLM_TIMEOUT_SECONDS = 35"` | — |
| [SRC-1AE03B9EC3-L000048](../../agents/web_agent.py#L48) | 48 | `""` | — |
| [SRC-1AE03B9EC3-L000049](../../agents/web_agent.py#L49) | 49 | `"# Only completed connector result-processing states positively confirm an attempt."` | — |
| [SRC-1AE03B9EC3-L000050](../../agents/web_agent.py#L50) | 50 | `"# A generic \"failed\" or timeout diagnostic may occur before a network request is sent."` | — |
| [SRC-1AE03B9EC3-L000051](../../agents/web_agent.py#L51) | 51 | `"_SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES = frozenset({\"ok\", \"no_results\", \"filtered_all\"})"` | — |
| [SRC-1AE03B9EC3-L000052](../../agents/web_agent.py#L52) | 52 | `"_RESEARCH_ERROR_OUTCOMES = frozenset({\"attempted_research_error\", \"unknown_after_research_error\"})"` | — |
| [SRC-1AE03B9EC3-L000053](../../agents/web_agent.py#L53) | 53 | `""` | — |
| [SRC-1AE03B9EC3-L000054](../../agents/web_agent.py#L54) | 54 | `""` | — |
| [SRC-1AE03B9EC3-L000055](../../agents/web_agent.py#L55) | 55 | `"_ARABIC_SEARCH_TRANSLATION = str.maketrans({"` | — |
| [SRC-1AE03B9EC3-L000056](../../agents/web_agent.py#L56) | 56 | `"    \"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ٱ\": \"ا\", \"ى\": \"ي\","` | — |
| [SRC-1AE03B9EC3-L000057](../../agents/web_agent.py#L57) | 57 | `"    \"ؤ\": \"و\", \"ئ\": \"ي\", \"ة\": \"ه\", \"ـ\": \"\","` | — |
| [SRC-1AE03B9EC3-L000058](../../agents/web_agent.py#L58) | 58 | `"})"` | — |
| [SRC-1AE03B9EC3-L000059](../../agents/web_agent.py#L59) | 59 | `"_ARABIC_DIACRITICS_RE = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-1AE03B9EC3-L000060](../../agents/web_agent.py#L60) | 60 | `"_SEARCH_STOPWORDS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000061](../../agents/web_agent.py#L61) | 61 | `"    \"ما\", \"ماذا\", \"من\", \"في\", \"على\", \"عن\", \"الى\", \"إلى\", \"و\", \"او\", \"أو\","` | — |
| [SRC-1AE03B9EC3-L000062](../../agents/web_agent.py#L62) | 62 | `"    \"هل\", \"هو\", \"هي\", \"هذا\", \"هذه\", \"ذلك\", \"تلك\", \"التي\", \"الذي\", \"مع\","` | — |
| [SRC-1AE03B9EC3-L000063](../../agents/web_agent.py#L63) | 63 | `"    \"بين\", \"كيف\", \"لماذا\", \"كم\", \"كان\", \"كانت\", \"يكون\", \"تكون\", \"لي\","` | — |
| [SRC-1AE03B9EC3-L000064](../../agents/web_agent.py#L64) | 64 | `"    \"the\", \"a\", \"an\", \"and\", \"or\", \"in\", \"on\", \"of\", \"to\", \"for\", \"with\","` | — |
| [SRC-1AE03B9EC3-L000065](../../agents/web_agent.py#L65) | 65 | `"    \"is\", \"are\", \"was\", \"were\", \"what\", \"which\", \"who\", \"how\", \"why\", \"when\","` | — |
| [SRC-1AE03B9EC3-L000066](../../agents/web_agent.py#L66) | 66 | `"    \"where\", \"compare\", \"comparison\", \"please\", \"show\", \"find\", \"latest\","` | — |
| [SRC-1AE03B9EC3-L000067](../../agents/web_agent.py#L67) | 67 | `"    \"news\", \"official\", \"sources\", \"source\", \"reports\", \"report\", \"analysis\","` | — |
| [SRC-1AE03B9EC3-L000068](../../agents/web_agent.py#L68) | 68 | `"    \"site\", \"com\", \"org\", \"net\", \"www\","` | — |
| [SRC-1AE03B9EC3-L000069](../../agents/web_agent.py#L69) | 69 | `"})"` | — |
| [SRC-1AE03B9EC3-L000070](../../agents/web_agent.py#L70) | 70 | `"# Ignore generic request/presentation wording when scoring a result against a query."` | — |
| [SRC-1AE03B9EC3-L000071](../../agents/web_agent.py#L71) | 71 | `"# These are query-only stopwords: topic words remain eligible for relevance scoring."` | — |
| [SRC-1AE03B9EC3-L000072](../../agents/web_agent.py#L72) | 72 | `"_QUERY_TASK_STOPWORDS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000073](../../agents/web_agent.py#L73) | 73 | `"    \"اذكر\", \"اذكري\", \"واذكر\", \"اذكروا\", \"استخدم\", \"واستخدم\", \"استخدمي\", \"استعمل\","` | — |
| [SRC-1AE03B9EC3-L000074](../../agents/web_agent.py#L74) | 74 | `"    \"اعرض\", \"واعرض\", \"اعرضي\", \"اجمع\", \"اجب\", \"واجب\", \"جاوب\", \"وضح\", \"ووضح\","` | — |
| [SRC-1AE03B9EC3-L000075](../../agents/web_agent.py#L75) | 75 | `"    \"حلل\", \"قارن\", \"وقارن\", \"ميز\", \"وميز\", \"اهم\","` | — |
| [SRC-1AE03B9EC3-L000076](../../agents/web_agent.py#L76) | 76 | `"    \"مصدر\", \"مصادر\", \"المصدر\", \"المصادر\", \"رابط\", \"روابط\","` | — |
| [SRC-1AE03B9EC3-L000077](../../agents/web_agent.py#L77) | 77 | `"    \"مباشر\", \"مباشره\", \"موثوق\", \"موثوقه\", \"بالعربيه\", \"بالعربي\","` | — |
| [SRC-1AE03B9EC3-L000078](../../agents/web_agent.py#L78) | 78 | `"    \"بايجاز\", \"باختصار\", \"ايجاز\", \"حقائق\", \"الحقائق\", \"والحقائق\","` | — |
| [SRC-1AE03B9EC3-L000079](../../agents/web_agent.py#L79) | 79 | `"    \"استنتاج\", \"استنتاجات\", \"والاستنتاجات\", \"متعدده\", \"متعدد\","` | — |
| [SRC-1AE03B9EC3-L000080](../../agents/web_agent.py#L80) | 80 | `"    \"تواجه\", \"حول\", \"خلال\", \"الايام\", \"ايام\", \"السبعه\", \"سبعه\","` | — |
| [SRC-1AE03B9EC3-L000081](../../agents/web_agent.py#L81) | 81 | `"    \"الماضيه\", \"السابقه\", \"تواريخ\", \"التواريخ\", \"تاريخ\","` | — |
| [SRC-1AE03B9EC3-L000082](../../agents/web_agent.py#L82) | 82 | `"    \"اخبار\", \"الاخبار\", \"احدث\", \"قديمه\", \"جديده\", \"معلومات\","` | — |
| [SRC-1AE03B9EC3-L000083](../../agents/web_agent.py#L83) | 83 | `"    \"باعتبارها\", \"تعرض\", \"لتمثيل\", \"عموما\", \"النتائج\", \"نتائج\","` | — |
| [SRC-1AE03B9EC3-L000084](../../agents/web_agent.py#L84) | 84 | `"    \"كافيه\", \"ايجابيه\", \"الايجابيه\", \"سلبيه\", \"السلبيه\", \"المتاحه\","` | — |
| [SRC-1AE03B9EC3-L000085](../../agents/web_agent.py#L85) | 85 | `"    \"عامه\", \"العامه\","` | — |
| [SRC-1AE03B9EC3-L000086](../../agents/web_agent.py#L86) | 86 | `"    \"cite\", \"citation\", \"citations\", \"link\", \"links\", \"direct\","` | — |
| [SRC-1AE03B9EC3-L000087](../../agents/web_agent.py#L87) | 87 | `"    \"brief\", \"briefly\", \"answer\", \"provide\", \"mention\", \"present\","` | — |
| [SRC-1AE03B9EC3-L000088](../../agents/web_agent.py#L88) | 88 | `"    \"use\", \"multiple\", \"fact\", \"facts\", \"conclusion\", \"conclusions\","` | — |
| [SRC-1AE03B9EC3-L000089](../../agents/web_agent.py#L89) | 89 | `"    \"date\", \"dates\", \"day\", \"days\", \"past\", \"represent\", \"representative\","` | — |
| [SRC-1AE03B9EC3-L000090](../../agents/web_agent.py#L90) | 90 | `"    \"generally\", \"available\", \"information\", \"old\", \"new\", \"positive\", \"negative\","` | — |
| [SRC-1AE03B9EC3-L000091](../../agents/web_agent.py#L91) | 91 | `"    \"latest\", \"current\", \"recent\", \"today\","` | — |
| [SRC-1AE03B9EC3-L000092](../../agents/web_agent.py#L92) | 92 | `"})"` | — |
| [SRC-1AE03B9EC3-L000093](../../agents/web_agent.py#L93) | 93 | `"_SEARCH_SYNONYMS = {"` | — |
| [SRC-1AE03B9EC3-L000094](../../agents/web_agent.py#L94) | 94 | `"    \"استراليا\": {\"australia\"}, \"عاصمة\": {\"capital\"}, \"مصر\": {\"egypt\"},"` | — |
| [SRC-1AE03B9EC3-L000095](../../agents/web_agent.py#L95) | 95 | `"    \"المصري\": {\"egyptian\", \"egypt\"}, \"مركزي\": {\"central\"},"` | — |
| [SRC-1AE03B9EC3-L000096](../../agents/web_agent.py#L96) | 96 | `"    \"المركزي\": {\"central\"}, \"بنك\": {\"bank\"}, \"البنك\": {\"bank\"},"` | — |
| [SRC-1AE03B9EC3-L000097](../../agents/web_agent.py#L97) | 97 | `"    \"قرار\": {\"decision\"}, \"قرارات\": {\"decision\", \"decisions\"},"` | — |
| [SRC-1AE03B9EC3-L000098](../../agents/web_agent.py#L98) | 98 | `"    \"سعر\": {\"price\"}, \"اسعار\": {\"prices\"}, \"استضافة\": {\"hosting\"},"` | — |
| [SRC-1AE03B9EC3-L000099](../../agents/web_agent.py#L99) | 99 | `"    \"شركة\": {\"company\"}, \"شركه\": {\"company\"}, \"ناشئة\": {\"startup\"},"` | — |
| [SRC-1AE03B9EC3-L000100](../../agents/web_agent.py#L100) | 100 | `"    \"صعيد\": {\"upper\"}, \"مقارنة\": {\"compare\", \"comparison\"},"` | — |
| [SRC-1AE03B9EC3-L000101](../../agents/web_agent.py#L101) | 101 | `"    \"تقنية\": {\"technology\"}, \"تقنيات\": {\"technology\"},"` | — |
| [SRC-1AE03B9EC3-L000102](../../agents/web_agent.py#L102) | 102 | `"    \"ميكروسوفت\": {\"microsoft\"}, \"مايكروسوفت\": {\"microsoft\"},"` | — |
| [SRC-1AE03B9EC3-L000103](../../agents/web_agent.py#L103) | 103 | `"    \"microsoft\": {\"ميكروسوفت\", \"مايكروسوفت\"},"` | — |
| [SRC-1AE03B9EC3-L000104](../../agents/web_agent.py#L104) | 104 | `"    \"جمهورية\": {\"republic\"}, \"republic\": {\"جمهورية\"},"` | — |
| [SRC-1AE03B9EC3-L000105](../../agents/web_agent.py#L105) | 105 | `"    \"الرقمية\": {\"digital\"}, \"رقمية\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000106](../../agents/web_agent.py#L106) | 106 | `"    \"الرقميه\": {\"digital\"}, \"رقميه\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000107](../../agents/web_agent.py#L107) | 107 | `"    \"موقع\": {\"website\", \"portal\"}, \"مواقع\": {\"websites\", \"portals\"},"` | — |
| [SRC-1AE03B9EC3-L000108](../../agents/web_agent.py#L108) | 108 | `"    \"التجمع\": {\"settlement\"}, \"تجمع\": {\"settlement\"},"` | — |
| [SRC-1AE03B9EC3-L000109](../../agents/web_agent.py#L109) | 109 | `"    \"الخامس\": {\"fifth\", \"5th\"}, \"خامس\": {\"fifth\", \"5th\"},"` | — |
| [SRC-1AE03B9EC3-L000110](../../agents/web_agent.py#L110) | 110 | `"    \"شقة\": {\"apartment\", \"flat\"}, \"شقق\": {\"apartments\", \"flats\"},"` | — |
| [SRC-1AE03B9EC3-L000111](../../agents/web_agent.py#L111) | 111 | `"    \"عميل\": {\"customer\", \"buyer\"}, \"عملاء\": {\"customers\", \"buyers\"},"` | — |
| [SRC-1AE03B9EC3-L000112](../../agents/web_agent.py#L112) | 112 | `"    \"شراء\": {\"buy\", \"purchase\"}, \"مشتري\": {\"buyer\"},"` | — |
| [SRC-1AE03B9EC3-L000113](../../agents/web_agent.py#L113) | 113 | `"    # Common bilingual concepts exercised by live search acceptance tests."` | — |
| [SRC-1AE03B9EC3-L000114](../../agents/web_agent.py#L114) | 114 | `"    \"سيارة\": {\"car\", \"vehicle\", \"automobile\"},"` | — |
| [SRC-1AE03B9EC3-L000115](../../agents/web_agent.py#L115) | 115 | `"    \"سيارات\": {\"cars\", \"vehicles\", \"automobiles\"},"` | — |
| [SRC-1AE03B9EC3-L000116](../../agents/web_agent.py#L116) | 116 | `"    \"السيارات\": {\"cars\", \"vehicles\", \"automobiles\"},"` | — |
| [SRC-1AE03B9EC3-L000117](../../agents/web_agent.py#L117) | 117 | `"    \"كهربائية\": {\"electric\", \"electrical\", \"ev\"},"` | — |
| [SRC-1AE03B9EC3-L000118](../../agents/web_agent.py#L118) | 118 | `"    \"الكهربائية\": {\"electric\", \"electrical\", \"ev\"},"` | — |
| [SRC-1AE03B9EC3-L000119](../../agents/web_agent.py#L119) | 119 | `"    \"شحن\": {\"charging\", \"charge\", \"chargers\"},"` | — |
| [SRC-1AE03B9EC3-L000120](../../agents/web_agent.py#L120) | 120 | `"    \"الشحن\": {\"charging\", \"charge\", \"chargers\"},"` | — |
| [SRC-1AE03B9EC3-L000121](../../agents/web_agent.py#L121) | 121 | `"    \"تكلفة\": {\"cost\", \"costs\"},"` | — |
| [SRC-1AE03B9EC3-L000122](../../agents/web_agent.py#L122) | 122 | `"    \"التكلفة\": {\"cost\", \"costs\"},"` | — |
| [SRC-1AE03B9EC3-L000123](../../agents/web_agent.py#L123) | 123 | `"    \"تحديات\": {\"challenges\", \"issues\"},"` | — |
| [SRC-1AE03B9EC3-L000124](../../agents/web_agent.py#L124) | 124 | `"    \"التحديات\": {\"challenges\", \"issues\"},"` | — |
| [SRC-1AE03B9EC3-L000125](../../agents/web_agent.py#L125) | 125 | `"    \"البنية\": {\"infrastructure\"},"` | — |
| [SRC-1AE03B9EC3-L000126](../../agents/web_agent.py#L126) | 126 | `"    \"التحتية\": {\"infrastructure\"},"` | — |
| [SRC-1AE03B9EC3-L000127](../../agents/web_agent.py#L127) | 127 | `"    \"وكيل\": {\"agent\"},"` | — |
| [SRC-1AE03B9EC3-L000128](../../agents/web_agent.py#L128) | 128 | `"    \"وكلاء\": {\"agents\", \"agent\"},"` | — |
| [SRC-1AE03B9EC3-L000129](../../agents/web_agent.py#L129) | 129 | `"    \"الذكاء\": {\"intelligence\", \"ai\"},"` | — |
| [SRC-1AE03B9EC3-L000130](../../agents/web_agent.py#L130) | 130 | `"    \"الاصطناعي\": {\"artificial\", \"ai\"},"` | — |
| [SRC-1AE03B9EC3-L000131](../../agents/web_agent.py#L131) | 131 | `"    \"التطورات\": {\"developments\", \"advances\"},"` | — |
| [SRC-1AE03B9EC3-L000132](../../agents/web_agent.py#L132) | 132 | `"    \"اراء\": {\"opinions\", \"reviews\"},"` | — |
| [SRC-1AE03B9EC3-L000133](../../agents/web_agent.py#L133) | 133 | `"    \"تجارب\": {\"experiences\", \"reviews\"},"` | — |
| [SRC-1AE03B9EC3-L000134](../../agents/web_agent.py#L134) | 134 | `"    \"مستخدمين\": {\"users\", \"user\"},"` | — |
| [SRC-1AE03B9EC3-L000135](../../agents/web_agent.py#L135) | 135 | `"    \"المستخدمين\": {\"users\", \"user\"},"` | — |
| [SRC-1AE03B9EC3-L000136](../../agents/web_agent.py#L136) | 136 | `"}"` | — |
| [SRC-1AE03B9EC3-L000137](../../agents/web_agent.py#L137) | 137 | `"_CALENDAR_MONTHS = ("` | — |
| [SRC-1AE03B9EC3-L000138](../../agents/web_agent.py#L138) | 138 | `"    \"يناير\", \"فبراير\", \"مارس\", \"ابريل\", \"أبريل\", \"مايو\", \"يونيو\","` | — |
| [SRC-1AE03B9EC3-L000139](../../agents/web_agent.py#L139) | 139 | `"    \"يوليو\", \"اغسطس\", \"أغسطس\", \"سبتمبر\", \"اكتوبر\", \"أكتوبر\","` | — |
| [SRC-1AE03B9EC3-L000140](../../agents/web_agent.py#L140) | 140 | `"    \"نوفمبر\", \"ديسمبر\", \"january\", \"february\", \"march\", \"april\","` | — |
| [SRC-1AE03B9EC3-L000141](../../agents/web_agent.py#L141) | 141 | `"    \"may\", \"june\", \"july\", \"august\", \"september\", \"october\","` | — |
| [SRC-1AE03B9EC3-L000142](../../agents/web_agent.py#L142) | 142 | `"    \"november\", \"december\","` | — |
| [SRC-1AE03B9EC3-L000143](../../agents/web_agent.py#L143) | 143 | `")"` | — |
| [SRC-1AE03B9EC3-L000144](../../agents/web_agent.py#L144) | 144 | `"_BLOCKED_SOURCE_DOMAINS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000145](../../agents/web_agent.py#L145) | 145 | `"    \"translate.google.com\", \"translate.googleusercontent.com\","` | — |
| [SRC-1AE03B9EC3-L000146](../../agents/web_agent.py#L146) | 146 | `"})"` | — |
| [SRC-1AE03B9EC3-L000147](../../agents/web_agent.py#L147) | 147 | `""` | — |
| [SRC-1AE03B9EC3-L000148](../../agents/web_agent.py#L148) | 148 | `""` | — |
| [SRC-1AE03B9EC3-L000149](../../agents/web_agent.py#L149) | 149 | `"def _normalize_search_query(value: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000150](../../agents/web_agent.py#L150) | 150 | `"    \"\"\"Normalize Arabic letters/diacritics while preserving search operators and dates.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000151](../../agents/web_agent.py#L151) | 151 | `"    value = unicodedata.normalize(\"NFKC\", value or \"\")"` | — |
| [SRC-1AE03B9EC3-L000152](../../agents/web_agent.py#L152) | 152 | `"    value = _ARABIC_DIACRITICS_RE.sub(\"\", value).translate(_ARABIC_SEARCH_TRANSLATION)"` | — |
| [SRC-1AE03B9EC3-L000153](../../agents/web_agent.py#L153) | 153 | `"    return re.sub(r\"\\s+\", \" \", value).strip()"` | — |
| [SRC-1AE03B9EC3-L000154](../../agents/web_agent.py#L154) | 154 | `""` | — |
| [SRC-1AE03B9EC3-L000155](../../agents/web_agent.py#L155) | 155 | `""` | — |
| [SRC-1AE03B9EC3-L000156](../../agents/web_agent.py#L156) | 156 | `"# Normalize synonym keys and values by the same rules as search text. This avoids"` | — |
| [SRC-1AE03B9EC3-L000157](../../agents/web_agent.py#L157) | 157 | `"# Arabic ta-marbuta/alif variants silently disabling Arabic-to-English matching."` | — |
| [SRC-1AE03B9EC3-L000158](../../agents/web_agent.py#L158) | 158 | `"_NORMALIZED_SEARCH_SYNONYMS: dict[str, set[str]] = {}"` | — |
| [SRC-1AE03B9EC3-L000159](../../agents/web_agent.py#L159) | 159 | `"for _synonym_key, _synonym_values in _SEARCH_SYNONYMS.items():"` | — |
| [SRC-1AE03B9EC3-L000160](../../agents/web_agent.py#L160) | 160 | `"    _normalized_key = _normalize_search_query(_synonym_key).casefold()"` | — |
| [SRC-1AE03B9EC3-L000161](../../agents/web_agent.py#L161) | 161 | `"    _NORMALIZED_SEARCH_SYNONYMS.setdefault(_normalized_key, set()).update("` | — |
| [SRC-1AE03B9EC3-L000162](../../agents/web_agent.py#L162) | 162 | `"        _normalize_search_query(value).casefold() for value in _synonym_values"` | — |
| [SRC-1AE03B9EC3-L000163](../../agents/web_agent.py#L163) | 163 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000164](../../agents/web_agent.py#L164) | 164 | `""` | — |
| [SRC-1AE03B9EC3-L000165](../../agents/web_agent.py#L165) | 165 | `""` | — |
| [SRC-1AE03B9EC3-L000166](../../agents/web_agent.py#L166) | 166 | `"def _search_tokens(value: str) -> set[str]:"` | — |
| [SRC-1AE03B9EC3-L000167](../../agents/web_agent.py#L167) | 167 | `"    \"\"\"Tokenize Arabic/English text and expand a small bilingual vocabulary.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000168](../../agents/web_agent.py#L168) | 168 | `"    value = _normalize_search_query(value).casefold()"` | — |
| [SRC-1AE03B9EC3-L000169](../../agents/web_agent.py#L169) | 169 | `"    value = re.sub(r\"(?i)\\bsite\\s*:\\s*\\S+\", \" \", value)"` | — |
| [SRC-1AE03B9EC3-L000170](../../agents/web_agent.py#L170) | 170 | `"    tokens = re.findall(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", value)"` | — |
| [SRC-1AE03B9EC3-L000171](../../agents/web_agent.py#L171) | 171 | `"    result: set[str] = set()"` | — |
| [SRC-1AE03B9EC3-L000172](../../agents/web_agent.py#L172) | 172 | `"    for token in tokens:"` | — |
| [SRC-1AE03B9EC3-L000173](../../agents/web_agent.py#L173) | 173 | `"        if token in _SEARCH_STOPWORDS or len(token) < 2:"` | — |
| [SRC-1AE03B9EC3-L000174](../../agents/web_agent.py#L174) | 174 | `"            continue"` | — |
| [SRC-1AE03B9EC3-L000175](../../agents/web_agent.py#L175) | 175 | `"        forms = {token}"` | — |
| [SRC-1AE03B9EC3-L000176](../../agents/web_agent.py#L176) | 176 | `"        if token.startswith(\"ال\") and len(token) > 4:"` | — |
| [SRC-1AE03B9EC3-L000177](../../agents/web_agent.py#L177) | 177 | `"            forms.add(token[2:])"` | — |
| [SRC-1AE03B9EC3-L000178](../../agents/web_agent.py#L178) | 178 | `"        forms.update(_NORMALIZED_SEARCH_SYNONYMS.get(token, set()))"` | — |
| [SRC-1AE03B9EC3-L000179](../../agents/web_agent.py#L179) | 179 | `"        # Reverse-map common English equivalents so Arabic and English results can match."` | — |
| [SRC-1AE03B9EC3-L000180](../../agents/web_agent.py#L180) | 180 | `"        for arabic, english in _NORMALIZED_SEARCH_SYNONYMS.items():"` | — |
| [SRC-1AE03B9EC3-L000181](../../agents/web_agent.py#L181) | 181 | `"            if token in english:"` | — |
| [SRC-1AE03B9EC3-L000182](../../agents/web_agent.py#L182) | 182 | `"                forms.add(arabic)"` | — |
| [SRC-1AE03B9EC3-L000183](../../agents/web_agent.py#L183) | 183 | `"                if arabic.startswith(\"ال\") and len(arabic) > 4:"` | — |
| [SRC-1AE03B9EC3-L000184](../../agents/web_agent.py#L184) | 184 | `"                    forms.add(arabic[2:])"` | — |
| [SRC-1AE03B9EC3-L000185](../../agents/web_agent.py#L185) | 185 | `"        result.update(forms)"` | — |
| [SRC-1AE03B9EC3-L000186](../../agents/web_agent.py#L186) | 186 | `"    return result"` | — |
| [SRC-1AE03B9EC3-L000187](../../agents/web_agent.py#L187) | 187 | `""` | — |
| [SRC-1AE03B9EC3-L000188](../../agents/web_agent.py#L188) | 188 | `""` | — |
| [SRC-1AE03B9EC3-L000189](../../agents/web_agent.py#L189) | 189 | `"def _relevance_ratio(query: str, evidence: str) -> float:"` | — |
| [SRC-1AE03B9EC3-L000190](../../agents/web_agent.py#L190) | 190 | `"    \"\"\"Fraction of meaningful query concepts present in a candidate's title/snippet.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000191](../../agents/web_agent.py#L191) | 191 | `"    query_text = _normalize_search_query(query).casefold()"` | — |
| [SRC-1AE03B9EC3-L000192](../../agents/web_agent.py#L192) | 192 | `"    query_text = re.sub(r\"(?i)\\bsite\\s*:\\s*\\S+\", \" \", query_text)"` | — |
| [SRC-1AE03B9EC3-L000193](../../agents/web_agent.py#L193) | 193 | `"    query_tokens = {"` | — |
| [SRC-1AE03B9EC3-L000194](../../agents/web_agent.py#L194) | 194 | `"        token for token in re.findall(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", query_text)"` | — |
| [SRC-1AE03B9EC3-L000195](../../agents/web_agent.py#L195) | 195 | `"        if ("` | — |
