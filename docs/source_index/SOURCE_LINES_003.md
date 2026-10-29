# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **003**
- سجلات الأسطر: **800**
- النطاق: SRC-2D53795445-L000253 إلى SRC-FDEEAFDFCA-L000074
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-2D53795445 — [agents/dialogue_state.py](../../agents/dialogue_state.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2D53795445-L000253](../../agents/dialogue_state.py#L253) | 253 | `"        r\"\\b(?:استخدم\|أستخدم\|اشتري\|أشتري\|اجيب\|أجيب\|اشغل\|أشغل\|افتح\|أفتح\|\""` | — |
| [SRC-2D53795445-L000254](../../agents/dialogue_state.py#L254) | 254 | `"        r\"اصلح\|أصلح\|احط\|أحط\|اجرب\|أجرب\|اربط\|أربط\|اوصل\|أوصل\|اخد\|آخد\|\""` | — |
| [SRC-2D53795445-L000255](../../agents/dialogue_state.py#L255) | 255 | `"        r\"اخلي\|أخلي\|اركب\|أركب\|انقل\|أنقل\|ادفع\|أدفع\|اطلب\|أطلب\|احجز\|أحجز)\""` | — |
| [SRC-2D53795445-L000256](../../agents/dialogue_state.py#L256) | 256 | `"        r\"[\\u0600-\\u06FF]{0,18}(?:ه\|ها\|هم\|هما\|هن\|ك\|كم\|كن)\\b\","` | — |
| [SRC-2D53795445-L000257](../../agents/dialogue_state.py#L257) | 257 | `"        current,"` | — |
| [SRC-2D53795445-L000258](../../agents/dialogue_state.py#L258) | 258 | `"    )"` | — |
| [SRC-2D53795445-L000259](../../agents/dialogue_state.py#L259) | 259 | `"    return bool(lead_in or reference or fragment or attached_reference)"` | — |
## الوكيل والمنطق

### FILE-5587371288 — [agents/intent_router.py](../../agents/intent_router.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-5587371288-L000001](../../agents/intent_router.py#L1) | 1 | `"\"\"\"Small deterministic intent routing for Omarai's answer engine."` | — |
| [SRC-5587371288-L000002](../../agents/intent_router.py#L2) | 2 | `""` | — |
| [SRC-5587371288-L000003](../../agents/intent_router.py#L3) | 3 | `"This module chooses a strategy; it does not search, call a model, or claim that"` | — |
| [SRC-5587371288-L000004](../../agents/intent_router.py#L4) | 4 | `"an answer is factually verified. Keep the rules explicit and unit-testable."` | — |
| [SRC-5587371288-L000005](../../agents/intent_router.py#L5) | 5 | `"\"\"\""` | — |
| [SRC-5587371288-L000006](../../agents/intent_router.py#L6) | 6 | `"from __future__ import annotations"` | — |
| [SRC-5587371288-L000007](../../agents/intent_router.py#L7) | 7 | `""` | — |
| [SRC-5587371288-L000008](../../agents/intent_router.py#L8) | 8 | `"import re"` | — |
| [SRC-5587371288-L000009](../../agents/intent_router.py#L9) | 9 | `"import unicodedata"` | — |
| [SRC-5587371288-L000010](../../agents/intent_router.py#L10) | 10 | `"from typing import Any"` | — |
| [SRC-5587371288-L000011](../../agents/intent_router.py#L11) | 11 | `""` | — |
| [SRC-5587371288-L000012](../../agents/intent_router.py#L12) | 12 | `"MAX_CONTEXT_TURNS = 8"` | — |
| [SRC-5587371288-L000013](../../agents/intent_router.py#L13) | 13 | `""` | — |
| [SRC-5587371288-L000014](../../agents/intent_router.py#L14) | 14 | `"ROUTES = frozenset({"` | — |
| [SRC-5587371288-L000015](../../agents/intent_router.py#L15) | 15 | `"    \"LOCAL\", \"MODEL_ONLY\", \"CLARIFY\", \"WEB_SIMPLE\", \"WEB_DEEP\","` | — |
| [SRC-5587371288-L000016](../../agents/intent_router.py#L16) | 16 | `"    \"LEAD_GENERATION\","` | — |
| [SRC-5587371288-L000017](../../agents/intent_router.py#L17) | 17 | `"})"` | — |
| [SRC-5587371288-L000018](../../agents/intent_router.py#L18) | 18 | `""` | — |
| [SRC-5587371288-L000019](../../agents/intent_router.py#L19) | 19 | `"_ARABIC_DIACRITICS = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-5587371288-L000020](../../agents/intent_router.py#L20) | 20 | `"_PUNCTUATION = re.compile(r\"[؟?!.،,؛;:()\\[\\]{}\\\"'«»]+\")"` | — |
| [SRC-5587371288-L000021](../../agents/intent_router.py#L21) | 21 | `"_SPACE = re.compile(r\"\\s+\")"` | — |
| [SRC-5587371288-L000022](../../agents/intent_router.py#L22) | 22 | `""` | — |
| [SRC-5587371288-L000023](../../agents/intent_router.py#L23) | 23 | `"_SMALLTALK = frozenset({"` | — |
| [SRC-5587371288-L000024](../../agents/intent_router.py#L24) | 24 | `"    \"hi\", \"hello\", \"hey\", \"hello there\", \"hi there\","` | — |
| [SRC-5587371288-L000025](../../agents/intent_router.py#L25) | 25 | `"    \"thanks\", \"thank you\", \"thanks that helps\", \"thank you that helps\","` | — |
| [SRC-5587371288-L000026](../../agents/intent_router.py#L26) | 26 | `"    \"got it\", \"okay thanks\", \"ok thanks\", \"how are you\", \"how are you doing\","` | — |
| [SRC-5587371288-L000027](../../agents/intent_router.py#L27) | 27 | `"    \"hello how are you\", \"hi how are you\","` | — |
| [SRC-5587371288-L000028](../../agents/intent_router.py#L28) | 28 | `"    \"ازيك\", \"ازيك عامل ايه\", \"ازيك عامل ايه النهارده\", \"عامل ايه\", \"عامله ايه\", \"اهلا\", \"مرحبا\","` | — |
| [SRC-5587371288-L000029](../../agents/intent_router.py#L29) | 29 | `"    \"السلام عليكم\", \"السلام عليكم ورحمه الله وبركاته\","` | — |
| [SRC-5587371288-L000030](../../agents/intent_router.py#L30) | 30 | `"    \"صباح الخير\", \"مساء الخير\", \"شكرا\", \"شكرا لك\", \"متشكر\", \"متشكره\","` | — |
| [SRC-5587371288-L000031](../../agents/intent_router.py#L31) | 31 | `"    \"تمام شكرا\", \"تمام\", \"حسنا\", \"العفو\","` | — |
| [SRC-5587371288-L000032](../../agents/intent_router.py#L32) | 32 | `"})"` | — |
| [SRC-5587371288-L000033](../../agents/intent_router.py#L33) | 33 | `""` | — |
| [SRC-5587371288-L000034](../../agents/intent_router.py#L34) | 34 | `"# Elliptical questions whose subject normally must be recovered from dialogue."` | — |
| [SRC-5587371288-L000035](../../agents/intent_router.py#L35) | 35 | `"_AMBIGUOUS_ARABIC = frozenset({"` | — |
| [SRC-5587371288-L000036](../../agents/intent_router.py#L36) | 36 | `"    \"كام سعرها\", \"كم سعرها\", \"بكام سعرها\", \"سعرها كام\", \"سعرها بكام\","` | — |
| [SRC-5587371288-L000037](../../agents/intent_router.py#L37) | 37 | `"    \"كام تمنها\", \"كم تمنها\", \"بكام دي\", \"بكام ده\", \"سعره كام\", \"كام سعره\","` | — |
| [SRC-5587371288-L000038](../../agents/intent_router.py#L38) | 38 | `"    \"كم سعره\", \"قارنهم\", \"قارنهملي\", \"قارن بينهم\", \"قارن بينهما\","` | — |
| [SRC-5587371288-L000039](../../agents/intent_router.py#L39) | 39 | `"    \"ما رايك فيها\", \"ايه رايك فيها\", \"هل هي كويسه\", \"هل هو كويس\","` | — |
| [SRC-5587371288-L000040](../../agents/intent_router.py#L40) | 40 | `"    \"هل دي كويسه\", \"هل ده كويس\", \"هل هو جيد\", \"هل هي جيده\","` | — |
| [SRC-5587371288-L000041](../../agents/intent_router.py#L41) | 41 | `"    \"اشتريها ولا لا\", \"اشتريه ولا لا\","` | — |
| [SRC-5587371288-L000042](../../agents/intent_router.py#L42) | 42 | `"    \"فين\", \"فين هي\", \"فين هو\", \"فين مكانها\", \"فين مكانه\","` | — |
| [SRC-5587371288-L000043](../../agents/intent_router.py#L43) | 43 | `"    \"مكانها فين\", \"مكانه فين\", \"موجوده فين\", \"موجود فين\","` | — |
| [SRC-5587371288-L000044](../../agents/intent_router.py#L44) | 44 | `"    \"فين الاقيها\", \"فين الاقيه\","` | — |
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
| [SRC-5587371288-L000093](../../agents/intent_router.py#L93) | 93 | `"    \"\"\"Return true only when history has a usable topic anchor, not a bare follow-up.\"\"\""` | — |
| [SRC-5587371288-L000094](../../agents/intent_router.py#L94) | 94 | `"    return bool(_latest_context_anchor(history))"` | — |
| [SRC-5587371288-L000095](../../agents/intent_router.py#L95) | 95 | `""` | — |
| [SRC-5587371288-L000096](../../agents/intent_router.py#L96) | 96 | `""` | — |
| [SRC-5587371288-L000097](../../agents/intent_router.py#L97) | 97 | `"def _has_live_signal(question: str) -> bool:"` | — |
| [SRC-5587371288-L000098](../../agents/intent_router.py#L98) | 98 | `"    \"\"\"Recognize common time-sensitive or explicit-search requests without a model.\"\"\""` | — |
| [SRC-5587371288-L000099](../../agents/intent_router.py#L99) | 99 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000100](../../agents/intent_router.py#L100) | 100 | `"    live_terms = ("` | — |
| [SRC-5587371288-L000101](../../agents/intent_router.py#L101) | 101 | `"        \"ابحث\", \"بحث عن\", \"دور على\", \"دورلي\", \"هات رابط\", \"هاتلي\", \"جيبلي\","` | — |
| [SRC-5587371288-L000102](../../agents/intent_router.py#L102) | 102 | `"        \"اعثر على\", \"موقع\", \"رابط\", \"لينك\", \"اخبار\", \"اخر\", \"احدث\", \"اليوم\","` | — |
| [SRC-5587371288-L000103](../../agents/intent_router.py#L103) | 103 | `"        \"دلوقتي\", \"حاليا\", \"سعر\", \"اسعار\", \"للبيع\", \"للايجار\", \"ايجار\","` | — |
| [SRC-5587371288-L000104](../../agents/intent_router.py#L104) | 104 | `"        \"معاينه\", \"عميل محتمل\", \"عملاء محتملين\", \"وظائف\", \"وظيفه\", \"حجز\","` | — |
| [SRC-5587371288-L000105](../../agents/intent_router.py#L105) | 105 | `"        \"موعد\", \"الطقس\", \"سهم\", \"سعر الصرف\", \"search\", \"find\", \"look up\","` | — |
| [SRC-5587371288-L000106](../../agents/intent_router.py#L106) | 106 | `"        \"latest\", \"today\", \"current\", \"news\", \"price\", \"for sale\", \"for rent\","` | — |
| [SRC-5587371288-L000107](../../agents/intent_router.py#L107) | 107 | `"        \"real estate\", \"job opening\", \"appointment\", \"reservation\", \"weather\","` | — |
| [SRC-5587371288-L000108](../../agents/intent_router.py#L108) | 108 | `"        \"stock price\", \"exchange rate\","` | — |
| [SRC-5587371288-L000109](../../agents/intent_router.py#L109) | 109 | `"    )"` | — |
| [SRC-5587371288-L000110](../../agents/intent_router.py#L110) | 110 | `"    return any(_normalize(term) in normalized for term in live_terms) or bool("` | — |
| [SRC-5587371288-L000111](../../agents/intent_router.py#L111) | 111 | `"        re.search(r\"https?://\", question, flags=re.IGNORECASE)"` | — |
| [SRC-5587371288-L000112](../../agents/intent_router.py#L112) | 112 | `"    )"` | — |
| [SRC-5587371288-L000113](../../agents/intent_router.py#L113) | 113 | `""` | — |
| [SRC-5587371288-L000114](../../agents/intent_router.py#L114) | 114 | `""` | — |
| [SRC-5587371288-L000115](../../agents/intent_router.py#L115) | 115 | `"def _is_lead_generation_request(question: str) -> bool:"` | — |
| [SRC-5587371288-L000116](../../agents/intent_router.py#L116) | 116 | `"    \"\"\"Recognize an explicit request to discover prospective buyers/customers."` | — |
| [SRC-5587371288-L000117](../../agents/intent_router.py#L117) | 117 | `""` | — |
| [SRC-5587371288-L000118](../../agents/intent_router.py#L118) | 118 | `"    A product or property listing request alone is not lead generation. This"` | — |
| [SRC-5587371288-L000119](../../agents/intent_router.py#L119) | 119 | `"    route requires a prospect/customer target plus an action to find one."` | — |
| [SRC-5587371288-L000120](../../agents/intent_router.py#L120) | 120 | `"    \"\"\""` | — |
| [SRC-5587371288-L000121](../../agents/intent_router.py#L121) | 121 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000122](../../agents/intent_router.py#L122) | 122 | `"    arabic_actions = (\"ابحث عن\", \"دور على\", \"دورلي على\", \"اعثر على\", \"هاتلي\", \"هات\")"` | — |
| [SRC-5587371288-L000123](../../agents/intent_router.py#L123) | 123 | `"    arabic_targets = (\"عميل\", \"عملاء\", \"مشتري\", \"مشتر\", \"مشترين\", \"عملاء محتملين\")"` | — |
| [SRC-5587371288-L000124](../../agents/intent_router.py#L124) | 124 | `"    english_patterns = ("` | — |
| [SRC-5587371288-L000125](../../agents/intent_router.py#L125) | 125 | `"        r\"\\b(?:find\|search for\|look for\|identify\|generate\|build\|create)\\b.{0,45}\\b(?:buyers?\|customers?\|prospects?\|leads?)\\b\|\\b(?:find\|build\|create\|generate)\\s+(?:a\\s+)?(?:lead generation\|prospect list)\\b\","` | — |
| [SRC-5587371288-L000126](../../agents/intent_router.py#L126) | 126 | `"    )"` | — |
| [SRC-5587371288-L000127](../../agents/intent_router.py#L127) | 127 | `"    if any(action in normalized for action in arabic_actions) and any("` | — |
| [SRC-5587371288-L000128](../../agents/intent_router.py#L128) | 128 | `"        target in normalized for target in arabic_targets"` | — |
| [SRC-5587371288-L000129](../../agents/intent_router.py#L129) | 129 | `"    ):"` | — |
| [SRC-5587371288-L000130](../../agents/intent_router.py#L130) | 130 | `"        return True"` | — |
| [SRC-5587371288-L000131](../../agents/intent_router.py#L131) | 131 | `"    if any(re.search(pattern, normalized) for pattern in english_patterns):"` | — |
| [SRC-5587371288-L000132](../../agents/intent_router.py#L132) | 132 | `"        return True"` | — |
| [SRC-5587371288-L000133](../../agents/intent_router.py#L133) | 133 | `"    return bool("` | — |
| [SRC-5587371288-L000134](../../agents/intent_router.py#L134) | 134 | `"        re.search("` | — |
| [SRC-5587371288-L000135](../../agents/intent_router.py#L135) | 135 | `"            r\"\\b(?:buyers?\|customers?\|prospects?\|leads?)\\b.{0,45}\\b\""` | — |
| [SRC-5587371288-L000136](../../agents/intent_router.py#L136) | 136 | `"            r\"(?:looking to buy\|want to buy\|wants to buy\|seeking to purchase)\\b\","` | — |
| [SRC-5587371288-L000137](../../agents/intent_router.py#L137) | 137 | `"            normalized,"` | — |
| [SRC-5587371288-L000138](../../agents/intent_router.py#L138) | 138 | `"        )"` | — |
| [SRC-5587371288-L000139](../../agents/intent_router.py#L139) | 139 | `"    )"` | — |
| [SRC-5587371288-L000140](../../agents/intent_router.py#L140) | 140 | `""` | — |
| [SRC-5587371288-L000141](../../agents/intent_router.py#L141) | 141 | `""` | — |
| [SRC-5587371288-L000142](../../agents/intent_router.py#L142) | 142 | `"_FOLLOWUP_LEAD_IN_RE = re.compile("` | — |
| [SRC-5587371288-L000143](../../agents/intent_router.py#L143) | 143 | `"    r\"^(?:(?:و?طيب\|و?طب\|و?تمام\|well\|okay\|ok\|so)\\s+)+\","` | — |
| [SRC-5587371288-L000144](../../agents/intent_router.py#L144) | 144 | `"    re.IGNORECASE,"` | — |
| [SRC-5587371288-L000145](../../agents/intent_router.py#L145) | 145 | `")"` | — |
| [SRC-5587371288-L000146](../../agents/intent_router.py#L146) | 146 | `""` | — |
| [SRC-5587371288-L000147](../../agents/intent_router.py#L147) | 147 | `"_FOLLOWUP_ASPECT_FRAGMENTS = frozenset({"` | — |
| [SRC-5587371288-L000148](../../agents/intent_router.py#L148) | 148 | `"    \"السعر\", \"سعرها كام\", \"سعره كام\", \"سعرها\", \"سعره\", \"والسعر\", \"وسعرها\","` | — |
| [SRC-5587371288-L000149](../../agents/intent_router.py#L149) | 149 | `"    \"الاسعار\", \"والاسعار\", \"الاسعار الحاليه\", \"اسعار الحاليه\", \"السعر الحالي\","` | — |
| [SRC-5587371288-L000150](../../agents/intent_router.py#L150) | 150 | `"    \"سعر اليوم\", \"اسعار اليوم\", \"التكلفه\", \"والتكلفه\", \"الضمان\", \"والضمان\","` | — |
| [SRC-5587371288-L000151](../../agents/intent_router.py#L151) | 151 | `"    \"ضمانها\", \"ضمانه\", \"البطاريه\", \"والبطاريه\", \"الكاميرا\", \"والكاميرا\","` | — |
| [SRC-5587371288-L000152](../../agents/intent_router.py#L152) | 152 | `"    \"المميزات\", \"والمميزات\", \"العيوب\", \"والعيوب\", \"المكان\", \"والمكان\","` | — |
| [SRC-5587371288-L000153](../../agents/intent_router.py#L153) | 153 | `"    \"المصدر\", \"والمصدر\", \"الرابط\", \"والرابط\", \"التاريخ\", \"والتاريخ\","` | — |
| [SRC-5587371288-L000154](../../agents/intent_router.py#L154) | 154 | `"    \"المراجعات\", \"والمراجعات\", \"الاراء\", \"والاراء\", \"and the price\","` | — |
| [SRC-5587371288-L000155](../../agents/intent_router.py#L155) | 155 | `"    \"and the warranty\", \"what about the warranty\", \"what about the price\","` | — |
| [SRC-5587371288-L000156](../../agents/intent_router.py#L156) | 156 | `"    \"its price\", \"the warranty\", \"the location\", \"the pros\", \"the cons\","` | — |
| [SRC-5587371288-L000157](../../agents/intent_router.py#L157) | 157 | `"})"` | — |
| [SRC-5587371288-L000158](../../agents/intent_router.py#L158) | 158 | `""` | — |
| [SRC-5587371288-L000159](../../agents/intent_router.py#L159) | 159 | `""` | — |
| [SRC-5587371288-L000160](../../agents/intent_router.py#L160) | 160 | `"def _strip_followup_leadin(value: str) -> str:"` | — |
| [SRC-5587371288-L000161](../../agents/intent_router.py#L161) | 161 | `"    return _FOLLOWUP_LEAD_IN_RE.sub(\"\", value).strip()"` | — |
| [SRC-5587371288-L000162](../../agents/intent_router.py#L162) | 162 | `""` | — |
| [SRC-5587371288-L000163](../../agents/intent_router.py#L163) | 163 | `""` | — |
| [SRC-5587371288-L000164](../../agents/intent_router.py#L164) | 164 | `"_FOLLOWUP_LEAD_IN_RE = re.compile("` | — |
| [SRC-5587371288-L000165](../../agents/intent_router.py#L165) | 165 | `"    r\"^(?:(?:و?طيب\|و?طب\|و?تمام\|well\|okay\|ok\|so)\\s+)+\","` | — |
| [SRC-5587371288-L000166](../../agents/intent_router.py#L166) | 166 | `"    re.IGNORECASE,"` | — |
| [SRC-5587371288-L000167](../../agents/intent_router.py#L167) | 167 | `")"` | — |
| [SRC-5587371288-L000168](../../agents/intent_router.py#L168) | 168 | `""` | — |
| [SRC-5587371288-L000169](../../agents/intent_router.py#L169) | 169 | `"_FOLLOWUP_ASPECT_FRAGMENTS = frozenset({"` | — |
| [SRC-5587371288-L000170](../../agents/intent_router.py#L170) | 170 | `"    \"السعر\", \"سعرها كام\", \"سعره كام\", \"سعرها\", \"سعره\", \"والسعر\", \"وسعرها\","` | — |
| [SRC-5587371288-L000171](../../agents/intent_router.py#L171) | 171 | `"    \"الاسعار\", \"والاسعار\", \"الاسعار الحاليه\", \"اسعار الحاليه\", \"السعر الحالي\","` | — |
| [SRC-5587371288-L000172](../../agents/intent_router.py#L172) | 172 | `"    \"سعر اليوم\", \"اسعار اليوم\", \"التكلفه\", \"والتكلفه\", \"الضمان\", \"والضمان\","` | — |
| [SRC-5587371288-L000173](../../agents/intent_router.py#L173) | 173 | `"    \"ضمانها\", \"ضمانه\", \"البطاريه\", \"والبطاريه\", \"الكاميرا\", \"والكاميرا\","` | — |
| [SRC-5587371288-L000174](../../agents/intent_router.py#L174) | 174 | `"    \"المميزات\", \"والمميزات\", \"العيوب\", \"والعيوب\", \"المكان\", \"والمكان\","` | — |
| [SRC-5587371288-L000175](../../agents/intent_router.py#L175) | 175 | `"    \"المصدر\", \"والمصدر\", \"الرابط\", \"والرابط\", \"التاريخ\", \"والتاريخ\","` | — |
| [SRC-5587371288-L000176](../../agents/intent_router.py#L176) | 176 | `"    \"المراجعات\", \"والمراجعات\", \"الاراء\", \"والاراء\", \"and the price\","` | — |
| [SRC-5587371288-L000177](../../agents/intent_router.py#L177) | 177 | `"    \"and the warranty\", \"what about the warranty\", \"what about the price\","` | — |
| [SRC-5587371288-L000178](../../agents/intent_router.py#L178) | 178 | `"    \"its price\", \"the warranty\", \"the location\", \"the pros\", \"the cons\","` | — |
| [SRC-5587371288-L000179](../../agents/intent_router.py#L179) | 179 | `"})"` | — |
| [SRC-5587371288-L000180](../../agents/intent_router.py#L180) | 180 | `""` | — |
| [SRC-5587371288-L000181](../../agents/intent_router.py#L181) | 181 | `""` | — |
| [SRC-5587371288-L000182](../../agents/intent_router.py#L182) | 182 | `"_CONTEXTUAL_ASPECT_RE = re.compile("` | — |
| [SRC-5587371288-L000183](../../agents/intent_router.py#L183) | 183 | `"    r\"^(?:ال)?(?:سعر\|ثمن\|اسعار\|تكلفه\|ضمان\|بطاريه\|كاميرا\|مميزات\|عيوب\|\""` | — |
| [SRC-5587371288-L000184](../../agents/intent_router.py#L184) | 184 | `"    r\"مكان\|مصدر\|رابط\|تاريخ\|مراجعات\|اراء\|توفر\|سرعه\|اداء\|جوده\|صيانه)\""` | — |
| [SRC-5587371288-L000185](../../agents/intent_router.py#L185) | 185 | `")"` | — |
| [SRC-5587371288-L000186](../../agents/intent_router.py#L186) | 186 | `"_CONTEXTUAL_ENGLISH_ASPECT_RE = re.compile("` | — |
| [SRC-5587371288-L000187](../../agents/intent_router.py#L187) | 187 | `"    r\"^(?:what about(?: its)?\|how about(?: its)?\|and (?:the\|its\|their)\|its) +\""` | — |
| [SRC-5587371288-L000188](../../agents/intent_router.py#L188) | 188 | `"    r\"(?:price\|warranty\|battery\|camera\|location\|source\|link\|date\|pros\|cons)\""` | — |
| [SRC-5587371288-L000189](../../agents/intent_router.py#L189) | 189 | `")"` | — |
| [SRC-5587371288-L000190](../../agents/intent_router.py#L190) | 190 | `""` | — |
| [SRC-5587371288-L000191](../../agents/intent_router.py#L191) | 191 | `""` | — |
| [SRC-5587371288-L000192](../../agents/intent_router.py#L192) | 192 | `"def _strip_followup_leadin(value: str) -> str:"` | — |
| [SRC-5587371288-L000193](../../agents/intent_router.py#L193) | 193 | `"    return _FOLLOWUP_LEAD_IN_RE.sub(\"\", value).strip()"` | — |
| [SRC-5587371288-L000194](../../agents/intent_router.py#L194) | 194 | `""` | — |
| [SRC-5587371288-L000195](../../agents/intent_router.py#L195) | 195 | `""` | — |
| [SRC-5587371288-L000196](../../agents/intent_router.py#L196) | 196 | `"def _starts_with_contextual_aspect(question: str) -> bool:"` | — |
| [SRC-5587371288-L000197](../../agents/intent_router.py#L197) | 197 | `"    \"\"\"Recognize aspect-led follow-ups without merging standalone new topics.\"\"\""` | — |
| [SRC-5587371288-L000198](../../agents/intent_router.py#L198) | 198 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000199](../../agents/intent_router.py#L199) | 199 | `"    if _CONTEXTUAL_ENGLISH_ASPECT_RE.match(normalized):"` | — |
| [SRC-5587371288-L000200](../../agents/intent_router.py#L200) | 200 | `"        return True"` | — |
| [SRC-5587371288-L000201](../../agents/intent_router.py#L201) | 201 | `"    stripped = _strip_followup_leadin(normalized)"` | — |
| [SRC-5587371288-L000202](../../agents/intent_router.py#L202) | 202 | `"    if stripped != normalized:"` | — |
| [SRC-5587371288-L000203](../../agents/intent_router.py#L203) | 203 | `"        return bool(_CONTEXTUAL_ASPECT_RE.match(stripped))"` | — |
| [SRC-5587371288-L000204](../../agents/intent_router.py#L204) | 204 | `"    if normalized.startswith(\"و\"):"` | — |
| [SRC-5587371288-L000205](../../agents/intent_router.py#L205) | 205 | `"        return bool(_CONTEXTUAL_ASPECT_RE.match(normalized[1:]))"` | — |
| [SRC-5587371288-L000206](../../agents/intent_router.py#L206) | 206 | `"    return False"` | — |
| [SRC-5587371288-L000207](../../agents/intent_router.py#L207) | 207 | `""` | — |
| [SRC-5587371288-L000208](../../agents/intent_router.py#L208) | 208 | `""` | — |
| [SRC-5587371288-L000209](../../agents/intent_router.py#L209) | 209 | `"def _needs_clarification(question: str) -> bool:"` | — |
| [SRC-5587371288-L000210](../../agents/intent_router.py#L210) | 210 | `"    normalized = _strip_followup_leadin(_normalize(question))"` | — |
| [SRC-5587371288-L000211](../../agents/intent_router.py#L211) | 211 | `"    ambiguous = {_normalize(item) for item in _AMBIGUOUS_ARABIC}"` | — |
| [SRC-5587371288-L000212](../../agents/intent_router.py#L212) | 212 | `"    ambiguous.update(_normalize(item) for item in _AMBIGUOUS_ENGLISH)"` | — |
| [SRC-5587371288-L000213](../../agents/intent_router.py#L213) | 213 | `"    if ("` | — |
| [SRC-5587371288-L000214](../../agents/intent_router.py#L214) | 214 | `"        normalized in ambiguous"` | — |
| [SRC-5587371288-L000215](../../agents/intent_router.py#L215) | 215 | `"        or normalized in _FOLLOWUP_ASPECT_FRAGMENTS"` | — |
| [SRC-5587371288-L000216](../../agents/intent_router.py#L216) | 216 | `"        or _starts_with_contextual_aspect(question)"` | — |
| [SRC-5587371288-L000217](../../agents/intent_router.py#L217) | 217 | `"    ):"` | — |
| [SRC-5587371288-L000218](../../agents/intent_router.py#L218) | 218 | `"        return True"` | — |
| [SRC-5587371288-L000219](../../agents/intent_router.py#L219) | 219 | `"    # Common inflected forms and short property-only follow-ups."` | — |
| [SRC-5587371288-L000220](../../agents/intent_router.py#L220) | 220 | `"    return bool("` | — |
| [SRC-5587371288-L000221](../../agents/intent_router.py#L221) | 221 | `"        re.fullmatch(r\"(?:كام\|كم\|بكام)\\s+(?:سعر\|ثمن)\\s*(?:ها\|ه\|هم)\", normalized)"` | — |
| [SRC-5587371288-L000222](../../agents/intent_router.py#L222) | 222 | `"        or re.fullmatch(r\"(?:قارن\|قارنلي)\\s+(?:بينهم\|بينهما\|دول\|دي\|دولتين)\", normalized)"` | — |
| [SRC-5587371288-L000223](../../agents/intent_router.py#L223) | 223 | `"        or re.fullmatch(r\"(?:و)?(?:السعر\|الاسعار\|التكلفه\|الضمان\|المميزات\|العيوب\|البطاريه\|الكاميرا\|المكان\|المصدر\|الرابط\|التاريخ)\", normalized)"` | — |
| [SRC-5587371288-L000224](../../agents/intent_router.py#L224) | 224 | `"    )"` | — |
| [SRC-5587371288-L000225](../../agents/intent_router.py#L225) | 225 | `""` | — |
| [SRC-5587371288-L000226](../../agents/intent_router.py#L226) | 226 | `""` | — |
| [SRC-5587371288-L000227](../../agents/intent_router.py#L227) | 227 | `"def _is_clarification_message(content: Any) -> bool:"` | — |
| [SRC-5587371288-L000228](../../agents/intent_router.py#L228) | 228 | `"    if not isinstance(content, str):"` | — |
| [SRC-5587371288-L000229](../../agents/intent_router.py#L229) | 229 | `"        return False"` | — |
| [SRC-5587371288-L000230](../../agents/intent_router.py#L230) | 230 | `"    normalized = _normalize(content)"` | — |
| [SRC-5587371288-L000231](../../agents/intent_router.py#L231) | 231 | `"    return any(marker in normalized for marker in ("` | — |
| [SRC-5587371288-L000232](../../agents/intent_router.py#L232) | 232 | `"        \"تقصد ايه تحديدا\", \"اكتب اسم الشيء\", \"ابعت الرابط\","` | — |
| [SRC-5587371288-L000233](../../agents/intent_router.py#L233) | 233 | `"        \"what are you referring to\", \"please name the item\","` | — |
| [SRC-5587371288-L000234](../../agents/intent_router.py#L234) | 234 | `"        \"share its link\", \"clarify what you mean\","` | — |
| [SRC-5587371288-L000235](../../agents/intent_router.py#L235) | 235 | `"    ))"` | — |
| [SRC-5587371288-L000236](../../agents/intent_router.py#L236) | 236 | `""` | — |
| [SRC-5587371288-L000237](../../agents/intent_router.py#L237) | 237 | `""` | — |
| [SRC-5587371288-L000238](../../agents/intent_router.py#L238) | 238 | `"def _latest_context_anchor(history: Any) -> str:"` | — |
| [SRC-5587371288-L000239](../../agents/intent_router.py#L239) | 239 | `"    \"\"\"Find the latest substantive user topic, skipping ellipsis follow-ups only."` | — |
| [SRC-5587371288-L000240](../../agents/intent_router.py#L240) | 240 | `""` | — |
| [SRC-5587371288-L000241](../../agents/intent_router.py#L241) | 241 | `"    A recent acknowledgment is a hard boundary: never search past it for stale topics."` | — |
| [SRC-5587371288-L000242](../../agents/intent_router.py#L242) | 242 | `"    Short entity replies can anchor context when the assistant explicitly asked for one."` | — |
| [SRC-5587371288-L000243](../../agents/intent_router.py#L243) | 243 | `"    \"\"\""` | — |
| [SRC-5587371288-L000244](../../agents/intent_router.py#L244) | 244 | `"    if not isinstance(history, list):"` | — |
| [SRC-5587371288-L000245](../../agents/intent_router.py#L245) | 245 | `"        return \"\""` | — |
| [SRC-5587371288-L000246](../../agents/intent_router.py#L246) | 246 | `"    bounded = history[-MAX_CONTEXT_TURNS:]"` | — |
| [SRC-5587371288-L000247](../../agents/intent_router.py#L247) | 247 | `"    for index in range(len(bounded) - 1, -1, -1):"` | — |
| [SRC-5587371288-L000248](../../agents/intent_router.py#L248) | 248 | `"        item = bounded[index]"` | — |
| [SRC-5587371288-L000249](../../agents/intent_router.py#L249) | 249 | `"        if not isinstance(item, dict) or item.get(\"role\") != \"user\":"` | — |
| [SRC-5587371288-L000250](../../agents/intent_router.py#L250) | 250 | `"            continue"` | — |
| [SRC-5587371288-L000251](../../agents/intent_router.py#L251) | 251 | `"        content = item.get(\"content\")"` | — |
| [SRC-5587371288-L000252](../../agents/intent_router.py#L252) | 252 | `"        if not isinstance(content, str):"` | — |
| [SRC-5587371288-L000253](../../agents/intent_router.py#L253) | 253 | `"            continue"` | — |
| [SRC-5587371288-L000254](../../agents/intent_router.py#L254) | 254 | `"        normalized = _normalize(content)"` | — |
| [SRC-5587371288-L000255](../../agents/intent_router.py#L255) | 255 | `"        if not normalized or _is_smalltalk(normalized):"` | — |
| [SRC-5587371288-L000256](../../agents/intent_router.py#L256) | 256 | `"            return \"\""` | — |
| [SRC-5587371288-L000257](../../agents/intent_router.py#L257) | 257 | `"        if _needs_clarification(content):"` | — |
| [SRC-5587371288-L000258](../../agents/intent_router.py#L258) | 258 | `"            continue"` | — |
| [SRC-5587371288-L000259](../../agents/intent_router.py#L259) | 259 | `"        meaningful = re.findall(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", normalized)"` | — |
| [SRC-5587371288-L000260](../../agents/intent_router.py#L260) | 260 | `"        if len(meaningful) >= 2 and len(normalized) >= 8:"` | — |
| [SRC-5587371288-L000261](../../agents/intent_router.py#L261) | 261 | `"            return re.sub(r\"\\s+\", \" \", content).strip()[:300]"` | — |
| [SRC-5587371288-L000262](../../agents/intent_router.py#L262) | 262 | `"        if index > 0:"` | — |
| [SRC-5587371288-L000263](../../agents/intent_router.py#L263) | 263 | `"            previous = bounded[index - 1]"` | — |
| [SRC-5587371288-L000264](../../agents/intent_router.py#L264) | 264 | `"            if isinstance(previous, dict) and previous.get(\"role\") == \"assistant\" and _is_clarification_message(previous.get(\"content\")):"` | — |
| [SRC-5587371288-L000265](../../agents/intent_router.py#L265) | 265 | `"                return re.sub(r\"\\s+\", \" \", content).strip()[:120]"` | — |
| [SRC-5587371288-L000266](../../agents/intent_router.py#L266) | 266 | `"        return \"\""` | — |
| [SRC-5587371288-L000267](../../agents/intent_router.py#L267) | 267 | `"    return \"\""` | — |
| [SRC-5587371288-L000268](../../agents/intent_router.py#L268) | 268 | `""` | — |
| [SRC-5587371288-L000269](../../agents/intent_router.py#L269) | 269 | `""` | — |
| [SRC-5587371288-L000270](../../agents/intent_router.py#L270) | 270 | `"def _pending_clarification_query(history: Any) -> str:"` | — |
| [SRC-5587371288-L000271](../../agents/intent_router.py#L271) | 271 | `"    \"\"\"Return the unresolved elliptical question immediately awaiting a user slot-fill.\"\"\""` | — |
| [SRC-5587371288-L000272](../../agents/intent_router.py#L272) | 272 | `"    if not isinstance(history, list) or not history:"` | — |
| [SRC-5587371288-L000273](../../agents/intent_router.py#L273) | 273 | `"        return \"\""` | — |
| [SRC-5587371288-L000274](../../agents/intent_router.py#L274) | 274 | `"    last_index = len(history) - 1"` | — |
| [SRC-5587371288-L000275](../../agents/intent_router.py#L275) | 275 | `"    while last_index >= 0 and not ("` | — |
| [SRC-5587371288-L000276](../../agents/intent_router.py#L276) | 276 | `"        isinstance(history[last_index], dict)"` | — |
| [SRC-5587371288-L000277](../../agents/intent_router.py#L277) | 277 | `"        and isinstance(history[last_index].get(\"content\"), str)"` | — |
| [SRC-5587371288-L000278](../../agents/intent_router.py#L278) | 278 | `"        and history[last_index].get(\"content\", \"\").strip()"` | — |
| [SRC-5587371288-L000279](../../agents/intent_router.py#L279) | 279 | `"    ):"` | — |
| [SRC-5587371288-L000280](../../agents/intent_router.py#L280) | 280 | `"        last_index -= 1"` | — |
| [SRC-5587371288-L000281](../../agents/intent_router.py#L281) | 281 | `"    if last_index < 0 or history[last_index].get(\"role\") != \"assistant\":"` | — |
| [SRC-5587371288-L000282](../../agents/intent_router.py#L282) | 282 | `"        return \"\""` | — |
| [SRC-5587371288-L000283](../../agents/intent_router.py#L283) | 283 | `"    if not _is_clarification_message(history[last_index].get(\"content\")):"` | — |
| [SRC-5587371288-L000284](../../agents/intent_router.py#L284) | 284 | `"        return \"\""` | — |
| [SRC-5587371288-L000285](../../agents/intent_router.py#L285) | 285 | `"    for index in range(last_index - 1, -1, -1):"` | — |
| [SRC-5587371288-L000286](../../agents/intent_router.py#L286) | 286 | `"        item = history[index]"` | — |
| [SRC-5587371288-L000287](../../agents/intent_router.py#L287) | 287 | `"        if isinstance(item, dict) and item.get(\"role\") == \"user\":"` | — |
| [SRC-5587371288-L000288](../../agents/intent_router.py#L288) | 288 | `"            content = item.get(\"content\")"` | — |
| [SRC-5587371288-L000289](../../agents/intent_router.py#L289) | 289 | `"            if not isinstance(content, str) or not _needs_clarification(content):"` | — |
| [SRC-5587371288-L000290](../../agents/intent_router.py#L290) | 290 | `"                return \"\""` | — |
| [SRC-5587371288-L000291](../../agents/intent_router.py#L291) | 291 | `"            if _latest_context_anchor(history[:index]):"` | — |
| [SRC-5587371288-L000292](../../agents/intent_router.py#L292) | 292 | `"                return \"\""` | — |
| [SRC-5587371288-L000293](../../agents/intent_router.py#L293) | 293 | `"            return content.strip()[:180]"` | — |
| [SRC-5587371288-L000294](../../agents/intent_router.py#L294) | 294 | `"    return \"\""` | — |
| [SRC-5587371288-L000295](../../agents/intent_router.py#L295) | 295 | `""` | — |
| [SRC-5587371288-L000296](../../agents/intent_router.py#L296) | 296 | `""` | — |
| [SRC-5587371288-L000297](../../agents/intent_router.py#L297) | 297 | `"def _is_clarification_answer(question: str, history: Any) -> bool:"` | — |
| [SRC-5587371288-L000298](../../agents/intent_router.py#L298) | 298 | `"    \"\"\"Recognize a concise answer to Omarai's immediately preceding clarification.\"\"\""` | — |
| [SRC-5587371288-L000299](../../agents/intent_router.py#L299) | 299 | `"    if not _pending_clarification_query(history) or not isinstance(question, str):"` | — |
| [SRC-5587371288-L000300](../../agents/intent_router.py#L300) | 300 | `"        return False"` | — |
| [SRC-5587371288-L000301](../../agents/intent_router.py#L301) | 301 | `"    query = question.strip()"` | — |
| [SRC-5587371288-L000302](../../agents/intent_router.py#L302) | 302 | `"    if not query or len(query) >= 100 or _needs_clarification(query) or _is_smalltalk(query):"` | — |
| [SRC-5587371288-L000303](../../agents/intent_router.py#L303) | 303 | `"        return False"` | — |
| [SRC-5587371288-L000304](../../agents/intent_router.py#L304) | 304 | `"    # A self-contained live request should not be mistaken for a slot-fill."` | — |
| [SRC-5587371288-L000305](../../agents/intent_router.py#L305) | 305 | `"    return not (_has_live_signal(query) or re.search(r\"https?://\", query, re.IGNORECASE))"` | — |
| [SRC-5587371288-L000306](../../agents/intent_router.py#L306) | 306 | `""` | — |
| [SRC-5587371288-L000307](../../agents/intent_router.py#L307) | 307 | `""` | — |
| [SRC-5587371288-L000308](../../agents/intent_router.py#L308) | 308 | `"def _is_contextual_followup(question: str) -> bool:"` | — |
| [SRC-5587371288-L000309](../../agents/intent_router.py#L309) | 309 | `"    \"\"\"Detect short referent-dependent follow-ups without treating every 'okay' as one.\"\"\""` | — |
| [SRC-5587371288-L000310](../../agents/intent_router.py#L310) | 310 | `"    if not isinstance(question, str) or len(question.strip()) >= 100:"` | — |
| [SRC-5587371288-L000311](../../agents/intent_router.py#L311) | 311 | `"        return False"` | — |
| [SRC-5587371288-L000312](../../agents/intent_router.py#L312) | 312 | `"    if re.search(r\"https?://\", question, re.IGNORECASE):"` | — |
| [SRC-5587371288-L000313](../../agents/intent_router.py#L313) | 313 | `"        return False"` | — |
| [SRC-5587371288-L000314](../../agents/intent_router.py#L314) | 314 | `"    normalized = _strip_followup_leadin(_normalize(question))"` | — |
| [SRC-5587371288-L000315](../../agents/intent_router.py#L315) | 315 | `"    if _needs_clarification(question) or _starts_with_contextual_aspect(question):"` | — |
| [SRC-5587371288-L000316](../../agents/intent_router.py#L316) | 316 | `"        return True"` | — |
| [SRC-5587371288-L000317](../../agents/intent_router.py#L317) | 317 | `"    # Pronouns and deictic references are strong signals only in a short turn."` | — |
| [SRC-5587371288-L000318](../../agents/intent_router.py#L318) | 318 | `"    detached_reference = re.fullmatch("` | — |
| [SRC-5587371288-L000319](../../agents/intent_router.py#L319) | 319 | `"        r\"(?:و)?(?:هي\|هو\|دي\|ده\|دول\|هما\|ذلك\|تلك\|عليها\|عليه\|فيها\|فيه\|لها\|له\|\""` | — |
| [SRC-5587371288-L000320](../../agents/intent_router.py#L320) | 320 | `"        r\"سعرها\|سعره\|مكانها\|مكانه\|ضمانها\|ضمانه\|بطاريتها\|كاميرتها\|مميزاتها\|عيوبها)\","` | — |
| [SRC-5587371288-L000321](../../agents/intent_router.py#L321) | 321 | `"        normalized,"` | — |
| [SRC-5587371288-L000322](../../agents/intent_router.py#L322) | 322 | `"    )"` | — |
| [SRC-5587371288-L000323](../../agents/intent_router.py#L323) | 323 | `"    # Arabic often attaches object pronouns to verbs (e.g. \"أشتريه\", \"أستخدمها\")."` | — |
| [SRC-5587371288-L000324](../../agents/intent_router.py#L324) | 324 | `"    # These are easy to miss with whitespace-token pronoun lists."` | — |
| [SRC-5587371288-L000325](../../agents/intent_router.py#L325) | 325 | `"    attached_reference = re.search("` | — |
| [SRC-5587371288-L000326](../../agents/intent_router.py#L326) | 326 | `"        r\"\\b(?:استخدم\|اشتري\|اجيب\|اشغل\|افتح\|اصلح\|احط\|اجرب\|اربط\|اوصل\|اخد\|اخلي\|\""` | — |
| [SRC-5587371288-L000327](../../agents/intent_router.py#L327) | 327 | `"        r\"اركب\|انقل\|ادفع\|اطلب\|احجز)[\\u0600-\\u06FF]{0,18}(?:ه\|ها\|هم\|هما\|هن\|ك\|كم\|كن)\\b\","` | — |
| [SRC-5587371288-L000328](../../agents/intent_router.py#L328) | 328 | `"        normalized,"` | — |
| [SRC-5587371288-L000329](../../agents/intent_router.py#L329) | 329 | `"    )"` | — |
| [SRC-5587371288-L000330](../../agents/intent_router.py#L330) | 330 | `"    return bool(detached_reference or attached_reference)"` | — |
| [SRC-5587371288-L000331](../../agents/intent_router.py#L331) | 331 | `""` | — |
| [SRC-5587371288-L000332](../../agents/intent_router.py#L332) | 332 | `""` | — |
| [SRC-5587371288-L000333](../../agents/intent_router.py#L333) | 333 | `"def resolve_followup_query(question: str, history: Any = None) -> str:"` | — |
| [SRC-5587371288-L000334](../../agents/intent_router.py#L334) | 334 | `"    \"\"\"Resolve a short contextual follow-up against the nearest substantive topic."` | — |
| [SRC-5587371288-L000335](../../agents/intent_router.py#L335) | 335 | `""` | — |
| [SRC-5587371288-L000336](../../agents/intent_router.py#L336) | 336 | `"    Repeated follow-ups retain the original topic. An answer to an explicit"` | — |
| [SRC-5587371288-L000337](../../agents/intent_router.py#L337) | 337 | `"    clarification is joined to the pending question. New standalone questions are"` | — |
| [SRC-5587371288-L000338](../../agents/intent_router.py#L338) | 338 | `"    never merged merely because they start with 'طيب' or 'طب'."` | — |
| [SRC-5587371288-L000339](../../agents/intent_router.py#L339) | 339 | `"    \"\"\""` | — |
| [SRC-5587371288-L000340](../../agents/intent_router.py#L340) | 340 | `"    if not isinstance(question, str):"` | — |
| [SRC-5587371288-L000341](../../agents/intent_router.py#L341) | 341 | `"        return \"\""` | — |
| [SRC-5587371288-L000342](../../agents/intent_router.py#L342) | 342 | `"    query = re.sub(r\"\\s+\", \" \", question).strip()"` | — |
| [SRC-5587371288-L000343](../../agents/intent_router.py#L343) | 343 | `"    if not query:"` | — |
| [SRC-5587371288-L000344](../../agents/intent_router.py#L344) | 344 | `"        return \"\""` | — |
| [SRC-5587371288-L000345](../../agents/intent_router.py#L345) | 345 | `"    pending = _pending_clarification_query(history)"` | — |
| [SRC-5587371288-L000346](../../agents/intent_router.py#L346) | 346 | `"    if pending and _is_clarification_answer(query, history):"` | — |
| [SRC-5587371288-L000347](../../agents/intent_router.py#L347) | 347 | `"        return f\"{pending[:220]} — {query[:180]}\"[:500]"` | — |
| [SRC-5587371288-L000348](../../agents/intent_router.py#L348) | 348 | `"    if len(query) >= 100 or not isinstance(history, list):"` | — |
| [SRC-5587371288-L000349](../../agents/intent_router.py#L349) | 349 | `"        return query[:500]"` | — |
| [SRC-5587371288-L000350](../../agents/intent_router.py#L350) | 350 | `"    if not _is_contextual_followup(query):"` | — |
| [SRC-5587371288-L000351](../../agents/intent_router.py#L351) | 351 | `"        return query[:500]"` | — |
| [SRC-5587371288-L000352](../../agents/intent_router.py#L352) | 352 | `"    previous = _latest_context_anchor(history)"` | — |
| [SRC-5587371288-L000353](../../agents/intent_router.py#L353) | 353 | `"    if not previous:"` | — |
| [SRC-5587371288-L000354](../../agents/intent_router.py#L354) | 354 | `"        return query[:500]"` | — |
| [SRC-5587371288-L000355](../../agents/intent_router.py#L355) | 355 | `"    return f\"{previous[:300]} — {query[:180]}\"[:500]"` | — |
| [SRC-5587371288-L000356](../../agents/intent_router.py#L356) | 356 | `""` | — |
| [SRC-5587371288-L000357](../../agents/intent_router.py#L357) | 357 | `""` | — |
| [SRC-5587371288-L000358](../../agents/intent_router.py#L358) | 358 | `"def _has_explicit_source_request(question: str) -> bool:"` | — |
| [SRC-5587371288-L000359](../../agents/intent_router.py#L359) | 359 | `"    \"\"\"Recognize explicit requests for evidence/citations that require web-backed retrieval.\"\"\""` | — |
| [SRC-5587371288-L000360](../../agents/intent_router.py#L360) | 360 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000361](../../agents/intent_router.py#L361) | 361 | `"    markers = ("` | — |
| [SRC-5587371288-L000362](../../agents/intent_router.py#L362) | 362 | `"        \"اذكر مصادر\", \"اذكر المصدر\", \"مصادر موثوقة\", \"مصدر موثوق\","` | — |
| [SRC-5587371288-L000363](../../agents/intent_router.py#L363) | 363 | `"        \"مصادر رسمية\", \"مصادر حديثة\", \"مع مصادر\", \"مع المصادر\","` | — |
| [SRC-5587371288-L000364](../../agents/intent_router.py#L364) | 364 | `"        \"بالمصادر\", \"روابط المصادر\", \"ارفق المصادر\", \"أرفق المصادر\","` | — |
| [SRC-5587371288-L000365](../../agents/intent_router.py#L365) | 365 | `"        \"استشهد بمصادر\", \"وثق الاجابة\", \"وثق الإجابة\", \"المراجع\","` | — |
| [SRC-5587371288-L000366](../../agents/intent_router.py#L366) | 366 | `"        \"with sources\", \"cite sources\", \"trusted sources\", \"reliable sources\","` | — |
| [SRC-5587371288-L000367](../../agents/intent_router.py#L367) | 367 | `"        \"official sources\", \"include references\", \"with citations\","` | — |
| [SRC-5587371288-L000368](../../agents/intent_router.py#L368) | 368 | `"        \"source-backed\", \"cite your sources\","` | — |
| [SRC-5587371288-L000369](../../agents/intent_router.py#L369) | 369 | `"    )"` | — |
| [SRC-5587371288-L000370](../../agents/intent_router.py#L370) | 370 | `"    return any(_normalize(marker) in normalized for marker in markers)"` | — |
| [SRC-5587371288-L000371](../../agents/intent_router.py#L371) | 371 | `""` | — |
| [SRC-5587371288-L000372](../../agents/intent_router.py#L372) | 372 | `""` | — |
| [SRC-5587371288-L000373](../../agents/intent_router.py#L373) | 373 | `"def _is_deep(question: str) -> bool:"` | — |
| [SRC-5587371288-L000374](../../agents/intent_router.py#L374) | 374 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000375](../../agents/intent_router.py#L375) | 375 | `"    if any(_normalize(term) in normalized for term in _DEEP_TERMS):"` | — |
| [SRC-5587371288-L000376](../../agents/intent_router.py#L376) | 376 | `"        return True"` | — |
| [SRC-5587371288-L000377](../../agents/intent_router.py#L377) | 377 | `"    # Explicit multi-dimension comparisons need evidence from more than one angle."` | — |
| [SRC-5587371288-L000378](../../agents/intent_router.py#L378) | 378 | `"    dimensions = ("` | — |
| [SRC-5587371288-L000379](../../agents/intent_router.py#L379) | 379 | `"        \"السعر\", \"سعر\", \"بطاريه\", \"كاميرا\", \"اداء\", \"امان\", \"تكلفه\","` | — |
| [SRC-5587371288-L000380](../../agents/intent_router.py#L380) | 380 | `"        \"الصيانه\", \"الجوده\", \"المميزات\", \"العيوب\", \"الاراء\", \"المراجعات\","` | — |
| [SRC-5587371288-L000381](../../agents/intent_router.py#L381) | 381 | `"        \"price\", \"battery\", \"camera\", \"performance\", \"safety\", \"cost\","` | — |
| [SRC-5587371288-L000382](../../agents/intent_router.py#L382) | 382 | `"        \"maintenance\", \"quality\", \"features\", \"drawbacks\", \"reviews\","` | — |
| [SRC-5587371288-L000383](../../agents/intent_router.py#L383) | 383 | `"    )"` | — |
| [SRC-5587371288-L000384](../../agents/intent_router.py#L384) | 384 | `"    matched_dimensions = sum(1 for item in dimensions if _normalize(item) in normalized)"` | — |
| [SRC-5587371288-L000385](../../agents/intent_router.py#L385) | 385 | `"    return matched_dimensions >= 2 and any("` | — |
| [SRC-5587371288-L000386](../../agents/intent_router.py#L386) | 386 | `"        marker in normalized for marker in _MULTIPART_MARKERS"` | — |
| [SRC-5587371288-L000387](../../agents/intent_router.py#L387) | 387 | `"    )"` | — |
| [SRC-5587371288-L000388](../../agents/intent_router.py#L388) | 388 | `""` | — |
| [SRC-5587371288-L000389](../../agents/intent_router.py#L389) | 389 | `""` | — |
| [SRC-5587371288-L000390](../../agents/intent_router.py#L390) | 390 | `"def _is_page_summarization_request(question: str) -> bool:"` | — |
| [SRC-5587371288-L000391](../../agents/intent_router.py#L391) | 391 | `"    \"\"\"Recognize a request to summarize a specific web page or link.\"\"\""` | — |
| [SRC-5587371288-L000392](../../agents/intent_router.py#L392) | 392 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000393](../../agents/intent_router.py#L393) | 393 | `"    terms = (\"لخص\", \"تلخيص\", \"ملخص\", \"summarize\", \"summarise\", \"summary\")"` | — |
| [SRC-5587371288-L000394](../../agents/intent_router.py#L394) | 394 | `"    page_references = ("` | — |
| [SRC-5587371288-L000395](../../agents/intent_router.py#L395) | 395 | `"        \"صفحه\", \"الصفحه\", \"مقال\", \"المقال\", \"رابط\", \"لينك\", \"url\","` | — |
| [SRC-5587371288-L000396](../../agents/intent_router.py#L396) | 396 | `"        \"link\", \"article\", \"page\", \"webpage\", \"web page\", \"website\","` | — |
| [SRC-5587371288-L000397](../../agents/intent_router.py#L397) | 397 | `"    )"` | — |
| [SRC-5587371288-L000398](../../agents/intent_router.py#L398) | 398 | `"    return ("` | — |
| [SRC-5587371288-L000399](../../agents/intent_router.py#L399) | 399 | `"        any(_normalize(term) in normalized for term in terms)"` | — |
| [SRC-5587371288-L000400](../../agents/intent_router.py#L400) | 400 | `"        and ("` | — |
| [SRC-5587371288-L000401](../../agents/intent_router.py#L401) | 401 | `"            bool(re.search(r\"https?://\", question, flags=re.IGNORECASE))"` | — |
| [SRC-5587371288-L000402](../../agents/intent_router.py#L402) | 402 | `"            or any(_normalize(term) in normalized for term in page_references)"` | — |
| [SRC-5587371288-L000403](../../agents/intent_router.py#L403) | 403 | `"        )"` | — |
| [SRC-5587371288-L000404](../../agents/intent_router.py#L404) | 404 | `"    )"` | — |
| [SRC-5587371288-L000405](../../agents/intent_router.py#L405) | 405 | `""` | — |
| [SRC-5587371288-L000406](../../agents/intent_router.py#L406) | 406 | `""` | — |
| [SRC-5587371288-L000407](../../agents/intent_router.py#L407) | 407 | `"def _has_inline_summary_text(question: str) -> bool:"` | — |
| [SRC-5587371288-L000408](../../agents/intent_router.py#L408) | 408 | `"    \"\"\"Detect text explicitly pasted after a summary instruction, not a web page URL.\"\"\""` | — |
| [SRC-5587371288-L000409](../../agents/intent_router.py#L409) | 409 | `"    if re.search(r\"https?://\", question, flags=re.IGNORECASE):"` | — |
| [SRC-5587371288-L000410](../../agents/intent_router.py#L410) | 410 | `"        return False"` | — |
| [SRC-5587371288-L000411](../../agents/intent_router.py#L411) | 411 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000412](../../agents/intent_router.py#L412) | 412 | `"    markers = ("` | — |
| [SRC-5587371288-L000413](../../agents/intent_router.py#L413) | 413 | `"        \"النص التالي\", \"النص الاتي\", \"النص ده\", \"النص اللي جاي\","` | — |
| [SRC-5587371288-L000414](../../agents/intent_router.py#L414) | 414 | `"        \"this text\", \"following text\", \"the following text\", \"text below\","` | — |
| [SRC-5587371288-L000415](../../agents/intent_router.py#L415) | 415 | `"        \"text to summarize\", \"content below\","` | — |
| [SRC-5587371288-L000416](../../agents/intent_router.py#L416) | 416 | `"    )"` | — |
| [SRC-5587371288-L000417](../../agents/intent_router.py#L417) | 417 | `"    for marker in markers:"` | — |
| [SRC-5587371288-L000418](../../agents/intent_router.py#L418) | 418 | `"        normalized_marker = _normalize(marker)"` | — |
| [SRC-5587371288-L000419](../../agents/intent_router.py#L419) | 419 | `"        if normalized_marker in normalized:"` | — |
| [SRC-5587371288-L000420](../../agents/intent_router.py#L420) | 420 | `"            remainder = normalized.split(normalized_marker, 1)[1].strip()"` | — |
| [SRC-5587371288-L000421](../../agents/intent_router.py#L421) | 421 | `"            if len(remainder) >= 8:"` | — |
| [SRC-5587371288-L000422](../../agents/intent_router.py#L422) | 422 | `"                return True"` | — |
| [SRC-5587371288-L000423](../../agents/intent_router.py#L423) | 423 | `"    # Also allow a concise direct form such as \"لخص: [pasted paragraph]\"."` | — |
| [SRC-5587371288-L000424](../../agents/intent_router.py#L424) | 424 | `"    return bool("` | — |
| [SRC-5587371288-L000425](../../agents/intent_router.py#L425) | 425 | `"        re.search("` | — |
| [SRC-5587371288-L000426](../../agents/intent_router.py#L426) | 426 | `"            r\"^\\s*(?:لخص(?:\\s+لي)?\|تلخيص\|summari[sz]e\|summary)\\s*[:：]\\s*\\S.{12,}$\","` | — |
| [SRC-5587371288-L000427](../../agents/intent_router.py#L427) | 427 | `"            question,"` | — |
| [SRC-5587371288-L000428](../../agents/intent_router.py#L428) | 428 | `"            flags=re.IGNORECASE,"` | — |
| [SRC-5587371288-L000429](../../agents/intent_router.py#L429) | 429 | `"        )"` | — |
| [SRC-5587371288-L000430](../../agents/intent_router.py#L430) | 430 | `"    )"` | — |
| [SRC-5587371288-L000431](../../agents/intent_router.py#L431) | 431 | `""` | — |
| [SRC-5587371288-L000432](../../agents/intent_router.py#L432) | 432 | `""` | — |
| [SRC-5587371288-L000433](../../agents/intent_router.py#L433) | 433 | `"def route_intent("` | — |
| [SRC-5587371288-L000434](../../agents/intent_router.py#L434) | 434 | `"    question: str,"` | — |
| [SRC-5587371288-L000435](../../agents/intent_router.py#L435) | 435 | `"    history: Any = None,"` | — |
| [SRC-5587371288-L000436](../../agents/intent_router.py#L436) | 436 | `"    mode: str = \"auto\","` | — |
| [SRC-5587371288-L000437](../../agents/intent_router.py#L437) | 437 | `"    *,"` | — |
| [SRC-5587371288-L000438](../../agents/intent_router.py#L438) | 438 | `"    capability_question: bool = False,"` | — |
| [SRC-5587371288-L000439](../../agents/intent_router.py#L439) | 439 | `"    requires_web: bool = False,"` | — |
| [SRC-5587371288-L000440](../../agents/intent_router.py#L440) | 440 | `") -> dict[str, Any]:"` | — |
| [SRC-5587371288-L000441](../../agents/intent_router.py#L441) | 441 | `"    \"\"\"Return a deterministic route and auditable reason for a user question.\"\"\""` | — |
| [SRC-5587371288-L000442](../../agents/intent_router.py#L442) | 442 | `"    clean_mode = mode.strip().lower() if isinstance(mode, str) else \"auto\""` | — |
| [SRC-5587371288-L000443](../../agents/intent_router.py#L443) | 443 | `""` | — |
| [SRC-5587371288-L000444](../../agents/intent_router.py#L444) | 444 | `"    # If the assistant just asked for a missing referent, bind the user's concise"` | — |
| [SRC-5587371288-L000445](../../agents/intent_router.py#L445) | 445 | `"    # reply to that pending question instead of answering the entity name in isolation."` | — |
| [SRC-5587371288-L000446](../../agents/intent_router.py#L446) | 446 | `"    if _is_clarification_answer(question, history):"` | — |
| [SRC-5587371288-L000447](../../agents/intent_router.py#L447) | 447 | `"        return {"` | — |
| [SRC-5587371288-L000448](../../agents/intent_router.py#L448) | 448 | `"            \"route\": \"WEB_DEEP\" if clean_mode == \"deep\" else \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000449](../../agents/intent_router.py#L449) | 449 | `"            \"reason\": \"answer_to_pending_clarification\","` | — |
| [SRC-5587371288-L000450](../../agents/intent_router.py#L450) | 450 | `"            \"context_available\": True,"` | — |
| [SRC-5587371288-L000451](../../agents/intent_router.py#L451) | 451 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000452](../../agents/intent_router.py#L452) | 452 | `"        }"` | — |
| [SRC-5587371288-L000453](../../agents/intent_router.py#L453) | 453 | `""` | — |
| [SRC-5587371288-L000454](../../agents/intent_router.py#L454) | 454 | `"    context_available = _has_context(history)"` | — |
| [SRC-5587371288-L000455](../../agents/intent_router.py#L455) | 455 | `""` | — |
| [SRC-5587371288-L000456](../../agents/intent_router.py#L456) | 456 | `"    # A search mode cannot supply a missing subject. Clarify genuinely elliptical"` | — |
| [SRC-5587371288-L000457](../../agents/intent_router.py#L457) | 457 | `"    # questions before honoring the UI's explicit research mode."` | — |
| [SRC-5587371288-L000458](../../agents/intent_router.py#L458) | 458 | `"    if _needs_clarification(question) and not context_available:"` | — |
| [SRC-5587371288-L000459](../../agents/intent_router.py#L459) | 459 | `"        return {"` | — |
| [SRC-5587371288-L000460](../../agents/intent_router.py#L460) | 460 | `"            \"route\": \"CLARIFY\","` | — |
| [SRC-5587371288-L000461](../../agents/intent_router.py#L461) | 461 | `"            \"reason\": \"missing_referent_and_no_conversation_context\","` | — |
| [SRC-5587371288-L000462](../../agents/intent_router.py#L462) | 462 | `"            \"context_available\": False,"` | — |
| [SRC-5587371288-L000463](../../agents/intent_router.py#L463) | 463 | `"            \"needs_clarification\": True,"` | — |
| [SRC-5587371288-L000464](../../agents/intent_router.py#L464) | 464 | `"        }"` | — |
| [SRC-5587371288-L000465](../../agents/intent_router.py#L465) | 465 | `""` | — |
| [SRC-5587371288-L000466](../../agents/intent_router.py#L466) | 466 | `"    # An explicitly selected mode controls research depth when the request itself"` | — |
| [SRC-5587371288-L000467](../../agents/intent_router.py#L467) | 467 | `"    # is sufficiently specified."` | — |
| [SRC-5587371288-L000468](../../agents/intent_router.py#L468) | 468 | `"    if clean_mode != \"auto\":"` | — |
| [SRC-5587371288-L000469](../../agents/intent_router.py#L469) | 469 | `"        route = \"WEB_DEEP\" if clean_mode == \"deep\" else \"WEB_SIMPLE\""` | — |
| [SRC-5587371288-L000470](../../agents/intent_router.py#L470) | 470 | `"        return {"` | — |
| [SRC-5587371288-L000471](../../agents/intent_router.py#L471) | 471 | `"            \"route\": route,"` | — |
| [SRC-5587371288-L000472](../../agents/intent_router.py#L472) | 472 | `"            \"reason\": \"explicit_mode\","` | — |
| [SRC-5587371288-L000473](../../agents/intent_router.py#L473) | 473 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000474](../../agents/intent_router.py#L474) | 474 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000475](../../agents/intent_router.py#L475) | 475 | `"        }"` | — |
| [SRC-5587371288-L000476](../../agents/intent_router.py#L476) | 476 | `""` | — |
| [SRC-5587371288-L000477](../../agents/intent_router.py#L477) | 477 | `"    if capability_question:"` | — |
| [SRC-5587371288-L000478](../../agents/intent_router.py#L478) | 478 | `"        return {"` | — |
| [SRC-5587371288-L000479](../../agents/intent_router.py#L479) | 479 | `"            \"route\": \"LOCAL\","` | — |
| [SRC-5587371288-L000480](../../agents/intent_router.py#L480) | 480 | `"            \"reason\": \"capability_question\","` | — |
| [SRC-5587371288-L000481](../../agents/intent_router.py#L481) | 481 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000482](../../agents/intent_router.py#L482) | 482 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000483](../../agents/intent_router.py#L483) | 483 | `"        }"` | — |
| [SRC-5587371288-L000484](../../agents/intent_router.py#L484) | 484 | `""` | — |
| [SRC-5587371288-L000485](../../agents/intent_router.py#L485) | 485 | `"    if _is_smalltalk(question):"` | — |
| [SRC-5587371288-L000486](../../agents/intent_router.py#L486) | 486 | `"        return {"` | — |
| [SRC-5587371288-L000487](../../agents/intent_router.py#L487) | 487 | `"            \"route\": \"LOCAL\","` | — |
| [SRC-5587371288-L000488](../../agents/intent_router.py#L488) | 488 | `"            \"reason\": \"short_conversational_turn\","` | — |
| [SRC-5587371288-L000489](../../agents/intent_router.py#L489) | 489 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000490](../../agents/intent_router.py#L490) | 490 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000491](../../agents/intent_router.py#L491) | 491 | `"        }"` | — |
| [SRC-5587371288-L000492](../../agents/intent_router.py#L492) | 492 | `""` | — |
| [SRC-5587371288-L000493](../../agents/intent_router.py#L493) | 493 | `"    # A page/link summary needs a concrete source. Pasted text is handled locally;"` | — |
| [SRC-5587371288-L000494](../../agents/intent_router.py#L494) | 494 | `"    # an absent source must trigger clarification rather than a search for \"the page\"."` | — |
| [SRC-5587371288-L000495](../../agents/intent_router.py#L495) | 495 | `"    if _is_page_summarization_request(question):"` | — |
| [SRC-5587371288-L000496](../../agents/intent_router.py#L496) | 496 | `"        if _has_inline_summary_text(question):"` | — |
| [SRC-5587371288-L000497](../../agents/intent_router.py#L497) | 497 | `"            return {"` | — |
| [SRC-5587371288-L000498](../../agents/intent_router.py#L498) | 498 | `"                \"route\": \"MODEL_ONLY\","` | — |
| [SRC-5587371288-L000499](../../agents/intent_router.py#L499) | 499 | `"                \"reason\": \"summarization_text_provided\","` | — |
| [SRC-5587371288-L000500](../../agents/intent_router.py#L500) | 500 | `"                \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000501](../../agents/intent_router.py#L501) | 501 | `"                \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000502](../../agents/intent_router.py#L502) | 502 | `"            }"` | — |
| [SRC-5587371288-L000503](../../agents/intent_router.py#L503) | 503 | `"        if re.search(r\"https?://\", question, flags=re.IGNORECASE):"` | — |
| [SRC-5587371288-L000504](../../agents/intent_router.py#L504) | 504 | `"            return {"` | — |
| [SRC-5587371288-L000505](../../agents/intent_router.py#L505) | 505 | `"                \"route\": \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000506](../../agents/intent_router.py#L506) | 506 | `"                \"reason\": \"summarization_request\","` | — |
| [SRC-5587371288-L000507](../../agents/intent_router.py#L507) | 507 | `"                \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000508](../../agents/intent_router.py#L508) | 508 | `"                \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000509](../../agents/intent_router.py#L509) | 509 | `"            }"` | — |
| [SRC-5587371288-L000510](../../agents/intent_router.py#L510) | 510 | `"        return {"` | — |
| [SRC-5587371288-L000511](../../agents/intent_router.py#L511) | 511 | `"            \"route\": \"CLARIFY\","` | — |
| [SRC-5587371288-L000512](../../agents/intent_router.py#L512) | 512 | `"            \"reason\": \"missing_summarization_input\","` | — |
| [SRC-5587371288-L000513](../../agents/intent_router.py#L513) | 513 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000514](../../agents/intent_router.py#L514) | 514 | `"            \"needs_clarification\": True,"` | — |
| [SRC-5587371288-L000515](../../agents/intent_router.py#L515) | 515 | `"        }"` | — |
| [SRC-5587371288-L000516](../../agents/intent_router.py#L516) | 516 | `""` | — |
| [SRC-5587371288-L000517](../../agents/intent_router.py#L517) | 517 | `"    ambiguous = _is_contextual_followup(question) or _needs_clarification(question)"` | — |
| [SRC-5587371288-L000518](../../agents/intent_router.py#L518) | 518 | `"    if ambiguous:"` | — |
| [SRC-5587371288-L000519](../../agents/intent_router.py#L519) | 519 | `"        return {"` | — |
| [SRC-5587371288-L000520](../../agents/intent_router.py#L520) | 520 | `"            \"route\": \"WEB_DEEP\" if _is_deep(question) else \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000521](../../agents/intent_router.py#L521) | 521 | `"            \"reason\": \"ambiguous_followup_with_context\","` | — |
| [SRC-5587371288-L000522](../../agents/intent_router.py#L522) | 522 | `"            \"context_available\": True,"` | — |
| [SRC-5587371288-L000523](../../agents/intent_router.py#L523) | 523 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000524](../../agents/intent_router.py#L524) | 524 | `"        }"` | — |
| [SRC-5587371288-L000525](../../agents/intent_router.py#L525) | 525 | `""` | — |
| [SRC-5587371288-L000526](../../agents/intent_router.py#L526) | 526 | `"    if _is_lead_generation_request(question):"` | — |
| [SRC-5587371288-L000527](../../agents/intent_router.py#L527) | 527 | `"        return {"` | — |
| [SRC-5587371288-L000528](../../agents/intent_router.py#L528) | 528 | `"            \"route\": \"LEAD_GENERATION\","` | — |
| [SRC-5587371288-L000529](../../agents/intent_router.py#L529) | 529 | `"            \"reason\": \"explicit_prospect_or_buyer_discovery_request\","` | — |
| [SRC-5587371288-L000530](../../agents/intent_router.py#L530) | 530 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000531](../../agents/intent_router.py#L531) | 531 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000532](../../agents/intent_router.py#L532) | 532 | `"        }"` | — |
| [SRC-5587371288-L000533](../../agents/intent_router.py#L533) | 533 | `""` | — |
| [SRC-5587371288-L000534](../../agents/intent_router.py#L534) | 534 | `"    if _is_deep(question):"` | — |
| [SRC-5587371288-L000535](../../agents/intent_router.py#L535) | 535 | `"        return {"` | — |
| [SRC-5587371288-L000536](../../agents/intent_router.py#L536) | 536 | `"            \"route\": \"WEB_DEEP\","` | — |
| [SRC-5587371288-L000537](../../agents/intent_router.py#L537) | 537 | `"            \"reason\": \"comparison_or_multi_part_research\","` | — |
| [SRC-5587371288-L000538](../../agents/intent_router.py#L538) | 538 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000539](../../agents/intent_router.py#L539) | 539 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000540](../../agents/intent_router.py#L540) | 540 | `"        }"` | — |
| [SRC-5587371288-L000541](../../agents/intent_router.py#L541) | 541 | `""` | — |
| [SRC-5587371288-L000542](../../agents/intent_router.py#L542) | 542 | `"    if requires_web or _has_live_signal(question) or _has_explicit_source_request(question):"` | — |
| [SRC-5587371288-L000543](../../agents/intent_router.py#L543) | 543 | `"        return {"` | — |
| [SRC-5587371288-L000544](../../agents/intent_router.py#L544) | 544 | `"            \"route\": \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000545](../../agents/intent_router.py#L545) | 545 | `"            \"reason\": ("` | — |
| [SRC-5587371288-L000546](../../agents/intent_router.py#L546) | 546 | `"                \"explicit_evidence_request\""` | — |
| [SRC-5587371288-L000547](../../agents/intent_router.py#L547) | 547 | `"                if _has_explicit_source_request(question)"` | — |
| [SRC-5587371288-L000548](../../agents/intent_router.py#L548) | 548 | `"                else \"freshness_or_explicit_research_signal\""` | — |
| [SRC-5587371288-L000549](../../agents/intent_router.py#L549) | 549 | `"            ),"` | — |
| [SRC-5587371288-L000550](../../agents/intent_router.py#L550) | 550 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000551](../../agents/intent_router.py#L551) | 551 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000552](../../agents/intent_router.py#L552) | 552 | `"        }"` | — |
| [SRC-5587371288-L000553](../../agents/intent_router.py#L553) | 553 | `""` | — |
| [SRC-5587371288-L000554](../../agents/intent_router.py#L554) | 554 | `"    return {"` | — |
| [SRC-5587371288-L000555](../../agents/intent_router.py#L555) | 555 | `"        \"route\": \"MODEL_ONLY\","` | — |
| [SRC-5587371288-L000556](../../agents/intent_router.py#L556) | 556 | `"        \"reason\": \"stable_knowledge_or_conversation\","` | — |
| [SRC-5587371288-L000557](../../agents/intent_router.py#L557) | 557 | `"        \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000558](../../agents/intent_router.py#L558) | 558 | `"        \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000559](../../agents/intent_router.py#L559) | 559 | `"    }"` | — |
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
