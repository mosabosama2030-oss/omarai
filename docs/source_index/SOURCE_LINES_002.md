# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **002**
- سجلات الأسطر: **800**
- النطاق: SRC-5587371288-L000045 إلى SRC-59CF4B7DE8-L000151
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-5587371288 — [agents/intent_router.py](../../agents/intent_router.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-5587371288-L000045](../../agents/intent_router.py#L45) | 45 | `"    \"هل فيه ضمان\", \"فيه ضمان\", \"هل لها ضمان\", \"هل له ضمان\","` | — |
| [SRC-5587371288-L000046](../../agents/intent_router.py#L46) | 46 | `"    \"هل عليها ضمان\", \"هل عليه ضمان\", \"هل يوجد ضمان\","` | — |
| [SRC-5587371288-L000047](../../agents/intent_router.py#L47) | 47 | `"    \"ضمانها ايه\", \"ضمانه ايه\","` | — |
| [SRC-5587371288-L000048](../../agents/intent_router.py#L48) | 48 | `"})"` | — |
| [SRC-5587371288-L000049](../../agents/intent_router.py#L49) | 49 | `"_AMBIGUOUS_ENGLISH = frozenset({"` | — |
| [SRC-5587371288-L000050](../../agents/intent_router.py#L50) | 50 | `"    \"how much is it\", \"how much does it cost\", \"what is its price\","` | — |
| [SRC-5587371288-L000051](../../agents/intent_router.py#L51) | 51 | `"    \"what about it\", \"what about this\", \"is it good\", \"is this good\","` | — |
| [SRC-5587371288-L000052](../../agents/intent_router.py#L52) | 52 | `"    \"does it work\", \"compare them\", \"compare these\", \"compare the two\","` | — |
| [SRC-5587371288-L000053](../../agents/intent_router.py#L53) | 53 | `"    \"what do you think of it\", \"should i buy it\", \"is it worth it\","` | — |
| [SRC-5587371288-L000054](../../agents/intent_router.py#L54) | 54 | `"    \"where is it\", \"where can i find it\", \"is there a warranty\","` | — |
| [SRC-5587371288-L000055](../../agents/intent_router.py#L55) | 55 | `"    \"does it have a warranty\", \"is it covered by warranty\","` | — |
| [SRC-5587371288-L000056](../../agents/intent_router.py#L56) | 56 | `"})"` | — |
| [SRC-5587371288-L000057](../../agents/intent_router.py#L57) | 57 | `"_DEEP_TERMS = ("` | — |
| [SRC-5587371288-L000058](../../agents/intent_router.py#L58) | 58 | `"    \"بحث عميق\", \"بحث معمق\", \"بحث مكثف\", \"بحث شامل\", \"بالتفصيل\","` | — |
| [SRC-5587371288-L000059](../../agents/intent_router.py#L59) | 59 | `"    \"قارن\", \"مقارنه\", \"حلل بعمق\", \"مزايا وعيوب\", \"الايجابيات والسلبيات\","` | — |
| [SRC-5587371288-L000060](../../agents/intent_router.py#L60) | 60 | `"    \"كل الجوانب\", \"دراسه مقارنه\", \"compare\", \"comparison\", \"deep research\","` | — |
| [SRC-5587371288-L000061](../../agents/intent_router.py#L61) | 61 | `"    \"in-depth\", \"comprehensive\", \"pros and cons\", \"trade-offs\","` | — |
| [SRC-5587371288-L000062](../../agents/intent_router.py#L62) | 62 | `")"` | — |
| [SRC-5587371288-L000063](../../agents/intent_router.py#L63) | 63 | `"_MULTIPART_MARKERS = ("` | — |
| [SRC-5587371288-L000064](../../agents/intent_router.py#L64) | 64 | `"    \"بالاضافه الى\", \"مع مراعاه\", \"من حيث\", \"وكذلك\", \"و ايضا\", \"والفرق\","` | — |
| [SRC-5587371288-L000065](../../agents/intent_router.py#L65) | 65 | `"    \"على ان تشمل\", \"and also\", \"as well as\", \"taking into account\","` | — |
| [SRC-5587371288-L000066](../../agents/intent_router.py#L66) | 66 | `"    \"in terms of\", \"along with\","` | — |
| [SRC-5587371288-L000067](../../agents/intent_router.py#L67) | 67 | `")"` | — |
| [SRC-5587371288-L000068](../../agents/intent_router.py#L68) | 68 | `""` | — |
| [SRC-5587371288-L000069](../../agents/intent_router.py#L69) | 69 | `""` | — |
| [SRC-5587371288-L000070](../../agents/intent_router.py#L70) | 70 | `"def _normalize(value: str) -> str:"` | — |
| [SRC-5587371288-L000071](../../agents/intent_router.py#L71) | 71 | `"    value = unicodedata.normalize(\"NFKC\", value or \"\").casefold()"` | — |
| [SRC-5587371288-L000072](../../agents/intent_router.py#L72) | 72 | `"    value = _ARABIC_DIACRITICS.sub(\"\", value)"` | — |
| [SRC-5587371288-L000073](../../agents/intent_router.py#L73) | 73 | `"    value = value.translate(str.maketrans({"` | — |
| [SRC-5587371288-L000074](../../agents/intent_router.py#L74) | 74 | `"        \"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ٱ\": \"ا\", \"ى\": \"ي\", \"ة\": \"ه\", \"ـ\": \"\","` | — |
| [SRC-5587371288-L000075](../../agents/intent_router.py#L75) | 75 | `"    }))"` | — |
| [SRC-5587371288-L000076](../../agents/intent_router.py#L76) | 76 | `"    value = _PUNCTUATION.sub(\" \", value)"` | — |
| [SRC-5587371288-L000077](../../agents/intent_router.py#L77) | 77 | `"    return _SPACE.sub(\" \", value).strip()"` | — |
| [SRC-5587371288-L000078](../../agents/intent_router.py#L78) | 78 | `""` | — |
| [SRC-5587371288-L000079](../../agents/intent_router.py#L79) | 79 | `""` | — |
| [SRC-5587371288-L000080](../../agents/intent_router.py#L80) | 80 | `"def _is_smalltalk(question: str) -> bool:"` | — |
| [SRC-5587371288-L000081](../../agents/intent_router.py#L81) | 81 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000082](../../agents/intent_router.py#L82) | 82 | `"    if normalized in {_normalize(item) for item in _SMALLTALK}:"` | — |
| [SRC-5587371288-L000083](../../agents/intent_router.py#L83) | 83 | `"        return True"` | — |
| [SRC-5587371288-L000084](../../agents/intent_router.py#L84) | 84 | `"    # Keep these patterns narrow: an opening greeting followed by a real question"` | — |
| [SRC-5587371288-L000085](../../agents/intent_router.py#L85) | 85 | `"    # is not itself a greeting-only request."` | — |
| [SRC-5587371288-L000086](../../agents/intent_router.py#L86) | 86 | `"    return bool("` | — |
| [SRC-5587371288-L000087](../../agents/intent_router.py#L87) | 87 | `"        normalized.startswith(\"السلام عليكم \")"` | — |
| [SRC-5587371288-L000088](../../agents/intent_router.py#L88) | 88 | `"        and normalized[14:].strip() in _SMALLTALK"` | — |
| [SRC-5587371288-L000089](../../agents/intent_router.py#L89) | 89 | `"    )"` | — |
| [SRC-5587371288-L000090](../../agents/intent_router.py#L90) | 90 | `""` | — |
| [SRC-5587371288-L000091](../../agents/intent_router.py#L91) | 91 | `""` | — |
| [SRC-5587371288-L000092](../../agents/intent_router.py#L92) | 92 | `"def _has_context(history: Any) -> bool:"` | — |
| [SRC-5587371288-L000093](../../agents/intent_router.py#L93) | 93 | `"    \"\"\"Check whether the latest user turn can plausibly anchor a short follow-up."` | — |
| [SRC-5587371288-L000094](../../agents/intent_router.py#L94) | 94 | `""` | — |
| [SRC-5587371288-L000095](../../agents/intent_router.py#L95) | 95 | `"    Do not resurrect an older topic after the user's most recent turn was only"` | — |
| [SRC-5587371288-L000096](../../agents/intent_router.py#L96) | 96 | `"    an acknowledgment; stale context is a common source of wrong referents."` | — |
| [SRC-5587371288-L000097](../../agents/intent_router.py#L97) | 97 | `"    \"\"\""` | — |
| [SRC-5587371288-L000098](../../agents/intent_router.py#L98) | 98 | `"    if not isinstance(history, list):"` | — |
| [SRC-5587371288-L000099](../../agents/intent_router.py#L99) | 99 | `"        return False"` | — |
| [SRC-5587371288-L000100](../../agents/intent_router.py#L100) | 100 | `"    for item in reversed(history[-MAX_CONTEXT_TURNS:]):"` | — |
| [SRC-5587371288-L000101](../../agents/intent_router.py#L101) | 101 | `"        if not isinstance(item, dict) or item.get(\"role\") != \"user\":"` | — |
| [SRC-5587371288-L000102](../../agents/intent_router.py#L102) | 102 | `"            continue"` | — |
| [SRC-5587371288-L000103](../../agents/intent_router.py#L103) | 103 | `"        content = item.get(\"content\")"` | — |
| [SRC-5587371288-L000104](../../agents/intent_router.py#L104) | 104 | `"        if not isinstance(content, str):"` | — |
| [SRC-5587371288-L000105](../../agents/intent_router.py#L105) | 105 | `"            continue"` | — |
| [SRC-5587371288-L000106](../../agents/intent_router.py#L106) | 106 | `"        normalized = _normalize(content)"` | — |
| [SRC-5587371288-L000107](../../agents/intent_router.py#L107) | 107 | `"        if not normalized or _is_smalltalk(normalized):"` | — |
| [SRC-5587371288-L000108](../../agents/intent_router.py#L108) | 108 | `"            return False"` | — |
| [SRC-5587371288-L000109](../../agents/intent_router.py#L109) | 109 | `"        meaningful = re.findall(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", normalized)"` | — |
| [SRC-5587371288-L000110](../../agents/intent_router.py#L110) | 110 | `"        return len(meaningful) >= 2 and len(normalized) >= 8"` | — |
| [SRC-5587371288-L000111](../../agents/intent_router.py#L111) | 111 | `"    return False"` | — |
| [SRC-5587371288-L000112](../../agents/intent_router.py#L112) | 112 | `""` | — |
| [SRC-5587371288-L000113](../../agents/intent_router.py#L113) | 113 | `""` | — |
| [SRC-5587371288-L000114](../../agents/intent_router.py#L114) | 114 | `"def _has_live_signal(question: str) -> bool:"` | — |
| [SRC-5587371288-L000115](../../agents/intent_router.py#L115) | 115 | `"    \"\"\"Recognize common time-sensitive or explicit-search requests without a model.\"\"\""` | — |
| [SRC-5587371288-L000116](../../agents/intent_router.py#L116) | 116 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000117](../../agents/intent_router.py#L117) | 117 | `"    live_terms = ("` | — |
| [SRC-5587371288-L000118](../../agents/intent_router.py#L118) | 118 | `"        \"ابحث\", \"بحث عن\", \"دور على\", \"دورلي\", \"هات رابط\", \"هاتلي\", \"جيبلي\","` | — |
| [SRC-5587371288-L000119](../../agents/intent_router.py#L119) | 119 | `"        \"اعثر على\", \"موقع\", \"رابط\", \"لينك\", \"اخبار\", \"اخر\", \"احدث\", \"اليوم\","` | — |
| [SRC-5587371288-L000120](../../agents/intent_router.py#L120) | 120 | `"        \"دلوقتي\", \"حاليا\", \"سعر\", \"اسعار\", \"للبيع\", \"للايجار\", \"ايجار\","` | — |
| [SRC-5587371288-L000121](../../agents/intent_router.py#L121) | 121 | `"        \"معاينه\", \"عميل محتمل\", \"عملاء محتملين\", \"وظائف\", \"وظيفه\", \"حجز\","` | — |
| [SRC-5587371288-L000122](../../agents/intent_router.py#L122) | 122 | `"        \"موعد\", \"الطقس\", \"سهم\", \"سعر الصرف\", \"search\", \"find\", \"look up\","` | — |
| [SRC-5587371288-L000123](../../agents/intent_router.py#L123) | 123 | `"        \"latest\", \"today\", \"current\", \"news\", \"price\", \"for sale\", \"for rent\","` | — |
| [SRC-5587371288-L000124](../../agents/intent_router.py#L124) | 124 | `"        \"real estate\", \"job opening\", \"appointment\", \"reservation\", \"weather\","` | — |
| [SRC-5587371288-L000125](../../agents/intent_router.py#L125) | 125 | `"        \"stock price\", \"exchange rate\","` | — |
| [SRC-5587371288-L000126](../../agents/intent_router.py#L126) | 126 | `"    )"` | — |
| [SRC-5587371288-L000127](../../agents/intent_router.py#L127) | 127 | `"    return any(_normalize(term) in normalized for term in live_terms) or bool("` | — |
| [SRC-5587371288-L000128](../../agents/intent_router.py#L128) | 128 | `"        re.search(r\"https?://\", question, flags=re.IGNORECASE)"` | — |
| [SRC-5587371288-L000129](../../agents/intent_router.py#L129) | 129 | `"    )"` | — |
| [SRC-5587371288-L000130](../../agents/intent_router.py#L130) | 130 | `""` | — |
| [SRC-5587371288-L000131](../../agents/intent_router.py#L131) | 131 | `""` | — |
| [SRC-5587371288-L000132](../../agents/intent_router.py#L132) | 132 | `"def _is_lead_generation_request(question: str) -> bool:"` | — |
| [SRC-5587371288-L000133](../../agents/intent_router.py#L133) | 133 | `"    \"\"\"Recognize an explicit request to discover prospective buyers/customers."` | — |
| [SRC-5587371288-L000134](../../agents/intent_router.py#L134) | 134 | `""` | — |
| [SRC-5587371288-L000135](../../agents/intent_router.py#L135) | 135 | `"    A product or property listing request alone is not lead generation. This"` | — |
| [SRC-5587371288-L000136](../../agents/intent_router.py#L136) | 136 | `"    route requires a prospect/customer target plus an action to find one."` | — |
| [SRC-5587371288-L000137](../../agents/intent_router.py#L137) | 137 | `"    \"\"\""` | — |
| [SRC-5587371288-L000138](../../agents/intent_router.py#L138) | 138 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000139](../../agents/intent_router.py#L139) | 139 | `"    arabic_actions = (\"ابحث عن\", \"دور على\", \"دورلي على\", \"اعثر على\", \"هاتلي\", \"هات\")"` | — |
| [SRC-5587371288-L000140](../../agents/intent_router.py#L140) | 140 | `"    arabic_targets = (\"عميل\", \"عملاء\", \"مشتري\", \"مشتر\", \"مشترين\", \"عملاء محتملين\")"` | — |
| [SRC-5587371288-L000141](../../agents/intent_router.py#L141) | 141 | `"    english_patterns = ("` | — |
| [SRC-5587371288-L000142](../../agents/intent_router.py#L142) | 142 | `"        r\"\\b(?:find\|search for\|look for\|identify\|generate\|build\|create)\\b.{0,45}\\b(?:buyers?\|customers?\|prospects?\|leads?)\\b\|\\b(?:find\|build\|create\|generate)\\s+(?:a\\s+)?(?:lead generation\|prospect list)\\b\","` | — |
| [SRC-5587371288-L000143](../../agents/intent_router.py#L143) | 143 | `"    )"` | — |
| [SRC-5587371288-L000144](../../agents/intent_router.py#L144) | 144 | `"    if any(action in normalized for action in arabic_actions) and any("` | — |
| [SRC-5587371288-L000145](../../agents/intent_router.py#L145) | 145 | `"        target in normalized for target in arabic_targets"` | — |
| [SRC-5587371288-L000146](../../agents/intent_router.py#L146) | 146 | `"    ):"` | — |
| [SRC-5587371288-L000147](../../agents/intent_router.py#L147) | 147 | `"        return True"` | — |
| [SRC-5587371288-L000148](../../agents/intent_router.py#L148) | 148 | `"    if any(re.search(pattern, normalized) for pattern in english_patterns):"` | — |
| [SRC-5587371288-L000149](../../agents/intent_router.py#L149) | 149 | `"        return True"` | — |
| [SRC-5587371288-L000150](../../agents/intent_router.py#L150) | 150 | `"    return bool("` | — |
| [SRC-5587371288-L000151](../../agents/intent_router.py#L151) | 151 | `"        re.search("` | — |
| [SRC-5587371288-L000152](../../agents/intent_router.py#L152) | 152 | `"            r\"\\b(?:buyers?\|customers?\|prospects?\|leads?)\\b.{0,45}\\b\""` | — |
| [SRC-5587371288-L000153](../../agents/intent_router.py#L153) | 153 | `"            r\"(?:looking to buy\|want to buy\|wants to buy\|seeking to purchase)\\b\","` | — |
| [SRC-5587371288-L000154](../../agents/intent_router.py#L154) | 154 | `"            normalized,"` | — |
| [SRC-5587371288-L000155](../../agents/intent_router.py#L155) | 155 | `"        )"` | — |
| [SRC-5587371288-L000156](../../agents/intent_router.py#L156) | 156 | `"    )"` | — |
| [SRC-5587371288-L000157](../../agents/intent_router.py#L157) | 157 | `""` | — |
| [SRC-5587371288-L000158](../../agents/intent_router.py#L158) | 158 | `""` | — |
| [SRC-5587371288-L000159](../../agents/intent_router.py#L159) | 159 | `"def _needs_clarification(question: str) -> bool:"` | — |
| [SRC-5587371288-L000160](../../agents/intent_router.py#L160) | 160 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000161](../../agents/intent_router.py#L161) | 161 | `"    if ("` | — |
| [SRC-5587371288-L000162](../../agents/intent_router.py#L162) | 162 | `"        normalized in {_normalize(item) for item in _AMBIGUOUS_ARABIC}"` | — |
| [SRC-5587371288-L000163](../../agents/intent_router.py#L163) | 163 | `"        or normalized in {_normalize(item) for item in _AMBIGUOUS_ENGLISH}"` | — |
| [SRC-5587371288-L000164](../../agents/intent_router.py#L164) | 164 | `"    ):"` | — |
| [SRC-5587371288-L000165](../../agents/intent_router.py#L165) | 165 | `"        return True"` | — |
| [SRC-5587371288-L000166](../../agents/intent_router.py#L166) | 166 | `"    # Common inflected forms missed by exact phrase matching."` | — |
| [SRC-5587371288-L000167](../../agents/intent_router.py#L167) | 167 | `"    return bool("` | — |
| [SRC-5587371288-L000168](../../agents/intent_router.py#L168) | 168 | `"        re.fullmatch(r\"(?:كام\|كم\|بكام)\\s+(?:سعر\|ثمن)\\s*(?:ها\|ه\|هم)\", normalized)"` | — |
| [SRC-5587371288-L000169](../../agents/intent_router.py#L169) | 169 | `"        or re.fullmatch(r\"(?:قارن\|قارنلي)\\s+(?:بينهم\|بينهما\|دول\|دي\|دولتين)\", normalized)"` | — |
| [SRC-5587371288-L000170](../../agents/intent_router.py#L170) | 170 | `"    )"` | — |
| [SRC-5587371288-L000171](../../agents/intent_router.py#L171) | 171 | `""` | — |
| [SRC-5587371288-L000172](../../agents/intent_router.py#L172) | 172 | `""` | — |
| [SRC-5587371288-L000173](../../agents/intent_router.py#L173) | 173 | `"_FOLLOW_UP_MARKERS = ("` | — |
| [SRC-5587371288-L000174](../../agents/intent_router.py#L174) | 174 | `"    \"والسعر\", \"وسعر\", \"والاسعار\", \"طيب \", \"طب \", \"وماذا\", \"وكمان\","` | — |
| [SRC-5587371288-L000175](../../agents/intent_router.py#L175) | 175 | `"    \"التكلفه\", \"والتاريخ\", \"والمميزات\", \"والعيوب\", \"المصدر\","` | — |
| [SRC-5587371288-L000176](../../agents/intent_router.py#L176) | 176 | `"    \"and the price\", \"what about\", \"how about\", \"and also\","` | — |
| [SRC-5587371288-L000177](../../agents/intent_router.py#L177) | 177 | `"    \"how much is it\", \"what is its price\", \"where is it\","` | — |
| [SRC-5587371288-L000178](../../agents/intent_router.py#L178) | 178 | `")"` | — |
| [SRC-5587371288-L000179](../../agents/intent_router.py#L179) | 179 | `""` | — |
| [SRC-5587371288-L000180](../../agents/intent_router.py#L180) | 180 | `""` | — |
| [SRC-5587371288-L000181](../../agents/intent_router.py#L181) | 181 | `"def resolve_followup_query(question: str, history: Any = None) -> str:"` | — |
| [SRC-5587371288-L000182](../../agents/intent_router.py#L182) | 182 | `"    \"\"\"Resolve a short contextual follow-up using the latest eligible user turn."` | — |
| [SRC-5587371288-L000183](../../agents/intent_router.py#L183) | 183 | `""` | — |
| [SRC-5587371288-L000184](../../agents/intent_router.py#L184) | 184 | `"    This is the single source of truth used by both research planning paths. It"` | — |
| [SRC-5587371288-L000185](../../agents/intent_router.py#L185) | 185 | `"    deliberately refuses to resurrect older topics after a greeting/acknowledgment."` | — |
| [SRC-5587371288-L000186](../../agents/intent_router.py#L186) | 186 | `"    The merged query preserves the original user wording and is bounded."` | — |
| [SRC-5587371288-L000187](../../agents/intent_router.py#L187) | 187 | `"    \"\"\""` | — |
| [SRC-5587371288-L000188](../../agents/intent_router.py#L188) | 188 | `"    if not isinstance(question, str):"` | — |
| [SRC-5587371288-L000189](../../agents/intent_router.py#L189) | 189 | `"        return \"\""` | — |
| [SRC-5587371288-L000190](../../agents/intent_router.py#L190) | 190 | `"    query = re.sub(r\"\\s+\", \" \", question).strip()"` | — |
| [SRC-5587371288-L000191](../../agents/intent_router.py#L191) | 191 | `"    if not query:"` | — |
| [SRC-5587371288-L000192](../../agents/intent_router.py#L192) | 192 | `"        return \"\""` | — |
| [SRC-5587371288-L000193](../../agents/intent_router.py#L193) | 193 | `"    if len(query) >= 100 or not _has_context(history):"` | — |
| [SRC-5587371288-L000194](../../agents/intent_router.py#L194) | 194 | `"        return query[:500]"` | — |
| [SRC-5587371288-L000195](../../agents/intent_router.py#L195) | 195 | `""` | — |
| [SRC-5587371288-L000196](../../agents/intent_router.py#L196) | 196 | `"    normalized = _normalize(query)"` | — |
| [SRC-5587371288-L000197](../../agents/intent_router.py#L197) | 197 | `"    is_follow_up = _needs_clarification(query) or any("` | — |
| [SRC-5587371288-L000198](../../agents/intent_router.py#L198) | 198 | `"        _normalize(marker) in normalized for marker in _FOLLOW_UP_MARKERS"` | — |
| [SRC-5587371288-L000199](../../agents/intent_router.py#L199) | 199 | `"    )"` | — |
| [SRC-5587371288-L000200](../../agents/intent_router.py#L200) | 200 | `"    if not is_follow_up or not isinstance(history, list):"` | — |
| [SRC-5587371288-L000201](../../agents/intent_router.py#L201) | 201 | `"        return query[:500]"` | — |
| [SRC-5587371288-L000202](../../agents/intent_router.py#L202) | 202 | `""` | — |
| [SRC-5587371288-L000203](../../agents/intent_router.py#L203) | 203 | `"    previous = next("` | — |
| [SRC-5587371288-L000204](../../agents/intent_router.py#L204) | 204 | `"        ("` | — |
| [SRC-5587371288-L000205](../../agents/intent_router.py#L205) | 205 | `"            re.sub(r\"\\s+\", \" \", item.get(\"content\", \"\")).strip()"` | — |
| [SRC-5587371288-L000206](../../agents/intent_router.py#L206) | 206 | `"            for item in reversed(history[-MAX_CONTEXT_TURNS:])"` | — |
| [SRC-5587371288-L000207](../../agents/intent_router.py#L207) | 207 | `"            if isinstance(item, dict)"` | — |
| [SRC-5587371288-L000208](../../agents/intent_router.py#L208) | 208 | `"            and item.get(\"role\") == \"user\""` | — |
| [SRC-5587371288-L000209](../../agents/intent_router.py#L209) | 209 | `"            and isinstance(item.get(\"content\"), str)"` | — |
| [SRC-5587371288-L000210](../../agents/intent_router.py#L210) | 210 | `"            and item.get(\"content\", \"\").strip()"` | — |
| [SRC-5587371288-L000211](../../agents/intent_router.py#L211) | 211 | `"        ),"` | — |
| [SRC-5587371288-L000212](../../agents/intent_router.py#L212) | 212 | `"        \"\","` | — |
| [SRC-5587371288-L000213](../../agents/intent_router.py#L213) | 213 | `"    )"` | — |
| [SRC-5587371288-L000214](../../agents/intent_router.py#L214) | 214 | `"    if not previous:"` | — |
| [SRC-5587371288-L000215](../../agents/intent_router.py#L215) | 215 | `"        return query[:500]"` | — |
| [SRC-5587371288-L000216](../../agents/intent_router.py#L216) | 216 | `"    combined = f\"{previous[:300]} — {query[:180]}\""` | — |
| [SRC-5587371288-L000217](../../agents/intent_router.py#L217) | 217 | `"    return combined[:500]"` | — |
| [SRC-5587371288-L000218](../../agents/intent_router.py#L218) | 218 | `""` | — |
| [SRC-5587371288-L000219](../../agents/intent_router.py#L219) | 219 | `""` | — |
| [SRC-5587371288-L000220](../../agents/intent_router.py#L220) | 220 | `"def _is_deep(question: str) -> bool:"` | — |
| [SRC-5587371288-L000221](../../agents/intent_router.py#L221) | 221 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000222](../../agents/intent_router.py#L222) | 222 | `"    if any(_normalize(term) in normalized for term in _DEEP_TERMS):"` | — |
| [SRC-5587371288-L000223](../../agents/intent_router.py#L223) | 223 | `"        return True"` | — |
| [SRC-5587371288-L000224](../../agents/intent_router.py#L224) | 224 | `"    # Explicit multi-dimension comparisons need evidence from more than one angle."` | — |
| [SRC-5587371288-L000225](../../agents/intent_router.py#L225) | 225 | `"    dimensions = ("` | — |
| [SRC-5587371288-L000226](../../agents/intent_router.py#L226) | 226 | `"        \"السعر\", \"سعر\", \"بطاريه\", \"كاميرا\", \"اداء\", \"امان\", \"تكلفه\","` | — |
| [SRC-5587371288-L000227](../../agents/intent_router.py#L227) | 227 | `"        \"الصيانه\", \"الجوده\", \"المميزات\", \"العيوب\", \"الاراء\", \"المراجعات\","` | — |
| [SRC-5587371288-L000228](../../agents/intent_router.py#L228) | 228 | `"        \"price\", \"battery\", \"camera\", \"performance\", \"safety\", \"cost\","` | — |
| [SRC-5587371288-L000229](../../agents/intent_router.py#L229) | 229 | `"        \"maintenance\", \"quality\", \"features\", \"drawbacks\", \"reviews\","` | — |
| [SRC-5587371288-L000230](../../agents/intent_router.py#L230) | 230 | `"    )"` | — |
| [SRC-5587371288-L000231](../../agents/intent_router.py#L231) | 231 | `"    matched_dimensions = sum(1 for item in dimensions if _normalize(item) in normalized)"` | — |
| [SRC-5587371288-L000232](../../agents/intent_router.py#L232) | 232 | `"    return matched_dimensions >= 2 and any("` | — |
| [SRC-5587371288-L000233](../../agents/intent_router.py#L233) | 233 | `"        marker in normalized for marker in _MULTIPART_MARKERS"` | — |
| [SRC-5587371288-L000234](../../agents/intent_router.py#L234) | 234 | `"    )"` | — |
| [SRC-5587371288-L000235](../../agents/intent_router.py#L235) | 235 | `""` | — |
| [SRC-5587371288-L000236](../../agents/intent_router.py#L236) | 236 | `""` | — |
| [SRC-5587371288-L000237](../../agents/intent_router.py#L237) | 237 | `"def _is_page_summarization_request(question: str) -> bool:"` | — |
| [SRC-5587371288-L000238](../../agents/intent_router.py#L238) | 238 | `"    \"\"\"Recognize a request to summarize a specific web page or link.\"\"\""` | — |
| [SRC-5587371288-L000239](../../agents/intent_router.py#L239) | 239 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000240](../../agents/intent_router.py#L240) | 240 | `"    terms = (\"لخص\", \"تلخيص\", \"ملخص\", \"summarize\", \"summarise\", \"summary\")"` | — |
| [SRC-5587371288-L000241](../../agents/intent_router.py#L241) | 241 | `"    page_references = ("` | — |
| [SRC-5587371288-L000242](../../agents/intent_router.py#L242) | 242 | `"        \"صفحه\", \"الصفحه\", \"مقال\", \"المقال\", \"رابط\", \"لينك\", \"url\","` | — |
| [SRC-5587371288-L000243](../../agents/intent_router.py#L243) | 243 | `"        \"link\", \"article\", \"page\", \"webpage\", \"web page\", \"website\","` | — |
| [SRC-5587371288-L000244](../../agents/intent_router.py#L244) | 244 | `"    )"` | — |
| [SRC-5587371288-L000245](../../agents/intent_router.py#L245) | 245 | `"    return ("` | — |
| [SRC-5587371288-L000246](../../agents/intent_router.py#L246) | 246 | `"        any(_normalize(term) in normalized for term in terms)"` | — |
| [SRC-5587371288-L000247](../../agents/intent_router.py#L247) | 247 | `"        and ("` | — |
| [SRC-5587371288-L000248](../../agents/intent_router.py#L248) | 248 | `"            bool(re.search(r\"https?://\", question, flags=re.IGNORECASE))"` | — |
| [SRC-5587371288-L000249](../../agents/intent_router.py#L249) | 249 | `"            or any(_normalize(term) in normalized for term in page_references)"` | — |
| [SRC-5587371288-L000250](../../agents/intent_router.py#L250) | 250 | `"        )"` | — |
| [SRC-5587371288-L000251](../../agents/intent_router.py#L251) | 251 | `"    )"` | — |
| [SRC-5587371288-L000252](../../agents/intent_router.py#L252) | 252 | `""` | — |
| [SRC-5587371288-L000253](../../agents/intent_router.py#L253) | 253 | `""` | — |
| [SRC-5587371288-L000254](../../agents/intent_router.py#L254) | 254 | `"def _has_inline_summary_text(question: str) -> bool:"` | — |
| [SRC-5587371288-L000255](../../agents/intent_router.py#L255) | 255 | `"    \"\"\"Detect text explicitly pasted after a summary instruction, not a web page URL.\"\"\""` | — |
| [SRC-5587371288-L000256](../../agents/intent_router.py#L256) | 256 | `"    if re.search(r\"https?://\", question, flags=re.IGNORECASE):"` | — |
| [SRC-5587371288-L000257](../../agents/intent_router.py#L257) | 257 | `"        return False"` | — |
| [SRC-5587371288-L000258](../../agents/intent_router.py#L258) | 258 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000259](../../agents/intent_router.py#L259) | 259 | `"    markers = ("` | — |
| [SRC-5587371288-L000260](../../agents/intent_router.py#L260) | 260 | `"        \"النص التالي\", \"النص الاتي\", \"النص ده\", \"النص اللي جاي\","` | — |
| [SRC-5587371288-L000261](../../agents/intent_router.py#L261) | 261 | `"        \"this text\", \"following text\", \"the following text\", \"text below\","` | — |
| [SRC-5587371288-L000262](../../agents/intent_router.py#L262) | 262 | `"        \"text to summarize\", \"content below\","` | — |
| [SRC-5587371288-L000263](../../agents/intent_router.py#L263) | 263 | `"    )"` | — |
| [SRC-5587371288-L000264](../../agents/intent_router.py#L264) | 264 | `"    for marker in markers:"` | — |
| [SRC-5587371288-L000265](../../agents/intent_router.py#L265) | 265 | `"        normalized_marker = _normalize(marker)"` | — |
| [SRC-5587371288-L000266](../../agents/intent_router.py#L266) | 266 | `"        if normalized_marker in normalized:"` | — |
| [SRC-5587371288-L000267](../../agents/intent_router.py#L267) | 267 | `"            remainder = normalized.split(normalized_marker, 1)[1].strip()"` | — |
| [SRC-5587371288-L000268](../../agents/intent_router.py#L268) | 268 | `"            if len(remainder) >= 8:"` | — |
| [SRC-5587371288-L000269](../../agents/intent_router.py#L269) | 269 | `"                return True"` | — |
| [SRC-5587371288-L000270](../../agents/intent_router.py#L270) | 270 | `"    # Also allow a concise direct form such as \"لخص: [pasted paragraph]\"."` | — |
| [SRC-5587371288-L000271](../../agents/intent_router.py#L271) | 271 | `"    return bool("` | — |
| [SRC-5587371288-L000272](../../agents/intent_router.py#L272) | 272 | `"        re.search("` | — |
| [SRC-5587371288-L000273](../../agents/intent_router.py#L273) | 273 | `"            r\"^\\s*(?:لخص(?:\\s+لي)?\|تلخيص\|summari[sz]e\|summary)\\s*[:：]\\s*\\S.{12,}$\","` | — |
| [SRC-5587371288-L000274](../../agents/intent_router.py#L274) | 274 | `"            question,"` | — |
| [SRC-5587371288-L000275](../../agents/intent_router.py#L275) | 275 | `"            flags=re.IGNORECASE,"` | — |
| [SRC-5587371288-L000276](../../agents/intent_router.py#L276) | 276 | `"        )"` | — |
| [SRC-5587371288-L000277](../../agents/intent_router.py#L277) | 277 | `"    )"` | — |
| [SRC-5587371288-L000278](../../agents/intent_router.py#L278) | 278 | `""` | — |
| [SRC-5587371288-L000279](../../agents/intent_router.py#L279) | 279 | `""` | — |
| [SRC-5587371288-L000280](../../agents/intent_router.py#L280) | 280 | `"def route_intent("` | — |
| [SRC-5587371288-L000281](../../agents/intent_router.py#L281) | 281 | `"    question: str,"` | — |
| [SRC-5587371288-L000282](../../agents/intent_router.py#L282) | 282 | `"    history: Any = None,"` | — |
| [SRC-5587371288-L000283](../../agents/intent_router.py#L283) | 283 | `"    mode: str = \"auto\","` | — |
| [SRC-5587371288-L000284](../../agents/intent_router.py#L284) | 284 | `"    *,"` | — |
| [SRC-5587371288-L000285](../../agents/intent_router.py#L285) | 285 | `"    capability_question: bool = False,"` | — |
| [SRC-5587371288-L000286](../../agents/intent_router.py#L286) | 286 | `"    requires_web: bool = False,"` | — |
| [SRC-5587371288-L000287](../../agents/intent_router.py#L287) | 287 | `") -> dict[str, Any]:"` | — |
| [SRC-5587371288-L000288](../../agents/intent_router.py#L288) | 288 | `"    \"\"\"Return a deterministic route and auditable reason for a user question.\"\"\""` | — |
| [SRC-5587371288-L000289](../../agents/intent_router.py#L289) | 289 | `"    clean_mode = mode.strip().lower() if isinstance(mode, str) else \"auto\""` | — |
| [SRC-5587371288-L000290](../../agents/intent_router.py#L290) | 290 | `"    context_available = _has_context(history)"` | — |
| [SRC-5587371288-L000291](../../agents/intent_router.py#L291) | 291 | `""` | — |
| [SRC-5587371288-L000292](../../agents/intent_router.py#L292) | 292 | `"    # A search mode cannot supply a missing subject. Clarify genuinely elliptical"` | — |
| [SRC-5587371288-L000293](../../agents/intent_router.py#L293) | 293 | `"    # questions before honoring the UI's explicit research mode."` | — |
| [SRC-5587371288-L000294](../../agents/intent_router.py#L294) | 294 | `"    if _needs_clarification(question) and not context_available:"` | — |
| [SRC-5587371288-L000295](../../agents/intent_router.py#L295) | 295 | `"        return {"` | — |
| [SRC-5587371288-L000296](../../agents/intent_router.py#L296) | 296 | `"            \"route\": \"CLARIFY\","` | — |
| [SRC-5587371288-L000297](../../agents/intent_router.py#L297) | 297 | `"            \"reason\": \"missing_referent_and_no_conversation_context\","` | — |
| [SRC-5587371288-L000298](../../agents/intent_router.py#L298) | 298 | `"            \"context_available\": False,"` | — |
| [SRC-5587371288-L000299](../../agents/intent_router.py#L299) | 299 | `"            \"needs_clarification\": True,"` | — |
| [SRC-5587371288-L000300](../../agents/intent_router.py#L300) | 300 | `"        }"` | — |
| [SRC-5587371288-L000301](../../agents/intent_router.py#L301) | 301 | `""` | — |
| [SRC-5587371288-L000302](../../agents/intent_router.py#L302) | 302 | `"    # An explicitly selected mode controls research depth when the request itself"` | — |
| [SRC-5587371288-L000303](../../agents/intent_router.py#L303) | 303 | `"    # is sufficiently specified."` | — |
| [SRC-5587371288-L000304](../../agents/intent_router.py#L304) | 304 | `"    if clean_mode != \"auto\":"` | — |
| [SRC-5587371288-L000305](../../agents/intent_router.py#L305) | 305 | `"        route = \"WEB_DEEP\" if clean_mode == \"deep\" else \"WEB_SIMPLE\""` | — |
| [SRC-5587371288-L000306](../../agents/intent_router.py#L306) | 306 | `"        return {"` | — |
| [SRC-5587371288-L000307](../../agents/intent_router.py#L307) | 307 | `"            \"route\": route,"` | — |
| [SRC-5587371288-L000308](../../agents/intent_router.py#L308) | 308 | `"            \"reason\": \"explicit_mode\","` | — |
| [SRC-5587371288-L000309](../../agents/intent_router.py#L309) | 309 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000310](../../agents/intent_router.py#L310) | 310 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000311](../../agents/intent_router.py#L311) | 311 | `"        }"` | — |
| [SRC-5587371288-L000312](../../agents/intent_router.py#L312) | 312 | `""` | — |
| [SRC-5587371288-L000313](../../agents/intent_router.py#L313) | 313 | `"    if capability_question:"` | — |
| [SRC-5587371288-L000314](../../agents/intent_router.py#L314) | 314 | `"        return {"` | — |
| [SRC-5587371288-L000315](../../agents/intent_router.py#L315) | 315 | `"            \"route\": \"LOCAL\","` | — |
| [SRC-5587371288-L000316](../../agents/intent_router.py#L316) | 316 | `"            \"reason\": \"capability_question\","` | — |
| [SRC-5587371288-L000317](../../agents/intent_router.py#L317) | 317 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000318](../../agents/intent_router.py#L318) | 318 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000319](../../agents/intent_router.py#L319) | 319 | `"        }"` | — |
| [SRC-5587371288-L000320](../../agents/intent_router.py#L320) | 320 | `""` | — |
| [SRC-5587371288-L000321](../../agents/intent_router.py#L321) | 321 | `"    if _is_smalltalk(question):"` | — |
| [SRC-5587371288-L000322](../../agents/intent_router.py#L322) | 322 | `"        return {"` | — |
| [SRC-5587371288-L000323](../../agents/intent_router.py#L323) | 323 | `"            \"route\": \"LOCAL\","` | — |
| [SRC-5587371288-L000324](../../agents/intent_router.py#L324) | 324 | `"            \"reason\": \"short_conversational_turn\","` | — |
| [SRC-5587371288-L000325](../../agents/intent_router.py#L325) | 325 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000326](../../agents/intent_router.py#L326) | 326 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000327](../../agents/intent_router.py#L327) | 327 | `"        }"` | — |
| [SRC-5587371288-L000328](../../agents/intent_router.py#L328) | 328 | `""` | — |
| [SRC-5587371288-L000329](../../agents/intent_router.py#L329) | 329 | `"    # A page/link summary needs a concrete source. Pasted text is handled locally;"` | — |
| [SRC-5587371288-L000330](../../agents/intent_router.py#L330) | 330 | `"    # an absent source must trigger clarification rather than a search for \"the page\"."` | — |
| [SRC-5587371288-L000331](../../agents/intent_router.py#L331) | 331 | `"    if _is_page_summarization_request(question):"` | — |
| [SRC-5587371288-L000332](../../agents/intent_router.py#L332) | 332 | `"        if _has_inline_summary_text(question):"` | — |
| [SRC-5587371288-L000333](../../agents/intent_router.py#L333) | 333 | `"            return {"` | — |
| [SRC-5587371288-L000334](../../agents/intent_router.py#L334) | 334 | `"                \"route\": \"MODEL_ONLY\","` | — |
| [SRC-5587371288-L000335](../../agents/intent_router.py#L335) | 335 | `"                \"reason\": \"summarization_text_provided\","` | — |
| [SRC-5587371288-L000336](../../agents/intent_router.py#L336) | 336 | `"                \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000337](../../agents/intent_router.py#L337) | 337 | `"                \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000338](../../agents/intent_router.py#L338) | 338 | `"            }"` | — |
| [SRC-5587371288-L000339](../../agents/intent_router.py#L339) | 339 | `"        if re.search(r\"https?://\", question, flags=re.IGNORECASE):"` | — |
| [SRC-5587371288-L000340](../../agents/intent_router.py#L340) | 340 | `"            return {"` | — |
| [SRC-5587371288-L000341](../../agents/intent_router.py#L341) | 341 | `"                \"route\": \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000342](../../agents/intent_router.py#L342) | 342 | `"                \"reason\": \"summarization_request\","` | — |
| [SRC-5587371288-L000343](../../agents/intent_router.py#L343) | 343 | `"                \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000344](../../agents/intent_router.py#L344) | 344 | `"                \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000345](../../agents/intent_router.py#L345) | 345 | `"            }"` | — |
| [SRC-5587371288-L000346](../../agents/intent_router.py#L346) | 346 | `"        return {"` | — |
| [SRC-5587371288-L000347](../../agents/intent_router.py#L347) | 347 | `"            \"route\": \"CLARIFY\","` | — |
| [SRC-5587371288-L000348](../../agents/intent_router.py#L348) | 348 | `"            \"reason\": \"missing_summarization_input\","` | — |
| [SRC-5587371288-L000349](../../agents/intent_router.py#L349) | 349 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000350](../../agents/intent_router.py#L350) | 350 | `"            \"needs_clarification\": True,"` | — |
| [SRC-5587371288-L000351](../../agents/intent_router.py#L351) | 351 | `"        }"` | — |
| [SRC-5587371288-L000352](../../agents/intent_router.py#L352) | 352 | `""` | — |
| [SRC-5587371288-L000353](../../agents/intent_router.py#L353) | 353 | `"    ambiguous = _needs_clarification(question)"` | — |
| [SRC-5587371288-L000354](../../agents/intent_router.py#L354) | 354 | `"    if ambiguous:"` | — |
| [SRC-5587371288-L000355](../../agents/intent_router.py#L355) | 355 | `"        return {"` | — |
| [SRC-5587371288-L000356](../../agents/intent_router.py#L356) | 356 | `"            \"route\": \"WEB_DEEP\" if _is_deep(question) else \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000357](../../agents/intent_router.py#L357) | 357 | `"            \"reason\": \"ambiguous_followup_with_context\","` | — |
| [SRC-5587371288-L000358](../../agents/intent_router.py#L358) | 358 | `"            \"context_available\": True,"` | — |
| [SRC-5587371288-L000359](../../agents/intent_router.py#L359) | 359 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000360](../../agents/intent_router.py#L360) | 360 | `"        }"` | — |
| [SRC-5587371288-L000361](../../agents/intent_router.py#L361) | 361 | `""` | — |
| [SRC-5587371288-L000362](../../agents/intent_router.py#L362) | 362 | `"    if _is_lead_generation_request(question):"` | — |
| [SRC-5587371288-L000363](../../agents/intent_router.py#L363) | 363 | `"        return {"` | — |
| [SRC-5587371288-L000364](../../agents/intent_router.py#L364) | 364 | `"            \"route\": \"LEAD_GENERATION\","` | — |
| [SRC-5587371288-L000365](../../agents/intent_router.py#L365) | 365 | `"            \"reason\": \"explicit_prospect_or_buyer_discovery_request\","` | — |
| [SRC-5587371288-L000366](../../agents/intent_router.py#L366) | 366 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000367](../../agents/intent_router.py#L367) | 367 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000368](../../agents/intent_router.py#L368) | 368 | `"        }"` | — |
| [SRC-5587371288-L000369](../../agents/intent_router.py#L369) | 369 | `""` | — |
| [SRC-5587371288-L000370](../../agents/intent_router.py#L370) | 370 | `"    if _is_deep(question):"` | — |
| [SRC-5587371288-L000371](../../agents/intent_router.py#L371) | 371 | `"        return {"` | — |
| [SRC-5587371288-L000372](../../agents/intent_router.py#L372) | 372 | `"            \"route\": \"WEB_DEEP\","` | — |
| [SRC-5587371288-L000373](../../agents/intent_router.py#L373) | 373 | `"            \"reason\": \"comparison_or_multi_part_research\","` | — |
| [SRC-5587371288-L000374](../../agents/intent_router.py#L374) | 374 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000375](../../agents/intent_router.py#L375) | 375 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000376](../../agents/intent_router.py#L376) | 376 | `"        }"` | — |
| [SRC-5587371288-L000377](../../agents/intent_router.py#L377) | 377 | `""` | — |
| [SRC-5587371288-L000378](../../agents/intent_router.py#L378) | 378 | `"    if requires_web or _has_live_signal(question):"` | — |
| [SRC-5587371288-L000379](../../agents/intent_router.py#L379) | 379 | `"        return {"` | — |
| [SRC-5587371288-L000380](../../agents/intent_router.py#L380) | 380 | `"            \"route\": \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000381](../../agents/intent_router.py#L381) | 381 | `"            \"reason\": \"freshness_or_explicit_research_signal\","` | — |
| [SRC-5587371288-L000382](../../agents/intent_router.py#L382) | 382 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000383](../../agents/intent_router.py#L383) | 383 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000384](../../agents/intent_router.py#L384) | 384 | `"        }"` | — |
| [SRC-5587371288-L000385](../../agents/intent_router.py#L385) | 385 | `""` | — |
| [SRC-5587371288-L000386](../../agents/intent_router.py#L386) | 386 | `"    return {"` | — |
| [SRC-5587371288-L000387](../../agents/intent_router.py#L387) | 387 | `"        \"route\": \"MODEL_ONLY\","` | — |
| [SRC-5587371288-L000388](../../agents/intent_router.py#L388) | 388 | `"        \"reason\": \"stable_knowledge_or_conversation\","` | — |
| [SRC-5587371288-L000389](../../agents/intent_router.py#L389) | 389 | `"        \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000390](../../agents/intent_router.py#L390) | 390 | `"        \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000391](../../agents/intent_router.py#L391) | 391 | `"    }"` | — |
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
