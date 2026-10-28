# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **036**
- سجلات الأسطر: **800**
- النطاق: SRC-6BF96689A8-L000283 إلى SRC-AFEDC2645A-L000073
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-6BF96689A8 — [tests/test_research.py](../../tests/test_research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6BF96689A8-L000283](../../tests/test_research.py#L283) | 283 | `""` | — |
| [SRC-6BF96689A8-L000284](../../tests/test_research.py#L284) | 284 | `"    agent = WebAgent()"` | — |
| [SRC-6BF96689A8-L000285](../../tests/test_research.py#L285) | 285 | `"    seen = []"` | — |
| [SRC-6BF96689A8-L000286](../../tests/test_research.py#L286) | 286 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: seen.append(query) or [])"` | — |
| [SRC-6BF96689A8-L000287](../../tests/test_research.py#L287) | 287 | `"    sources, _warnings, report = agent._collect_research({"` | — |
| [SRC-6BF96689A8-L000288](../../tests/test_research.py#L288) | 288 | `"        \"queries\": ["` | — |
| [SRC-6BF96689A8-L000289](../../tests/test_research.py#L289) | 289 | `"            \"ما عاصمة مصر؟ اذكر مصدرًا موثوقًا مع رابط مباشر، وأجب بالعربية بإيجاز.\""` | — |
| [SRC-6BF96689A8-L000290](../../tests/test_research.py#L290) | 290 | `"        ],"` | — |
| [SRC-6BF96689A8-L000291](../../tests/test_research.py#L291) | 291 | `"        \"direct_urls\": [],"` | — |
| [SRC-6BF96689A8-L000292](../../tests/test_research.py#L292) | 292 | `"        \"social_focus\": False,"` | — |
| [SRC-6BF96689A8-L000293](../../tests/test_research.py#L293) | 293 | `"        \"freshness\": \"any\","` | — |
| [SRC-6BF96689A8-L000294](../../tests/test_research.py#L294) | 294 | `"        \"depth\": \"standard\","` | — |
| [SRC-6BF96689A8-L000295](../../tests/test_research.py#L295) | 295 | `"        \"platforms\": [],"` | — |
| [SRC-6BF96689A8-L000296](../../tests/test_research.py#L296) | 296 | `"    })"` | — |
| [SRC-6BF96689A8-L000297](../../tests/test_research.py#L297) | 297 | `""` | — |
| [SRC-6BF96689A8-L000298](../../tests/test_research.py#L298) | 298 | `"    assert sources == []"` | — |
| [SRC-6BF96689A8-L000299](../../tests/test_research.py#L299) | 299 | `"    assert seen == [\"ما عاصمة مصر؟\"]"` | — |
| [SRC-6BF96689A8-L000300](../../tests/test_research.py#L300) | 300 | `"    assert report[\"queries_planned\"] == 1"` | — |
| [SRC-6BF96689A8-L000301](../../tests/test_research.py#L301) | 301 | `"    assert report[\"queries_attempted\"] == 1"` | — |
| [SRC-6BF96689A8-L000302](../../tests/test_research.py#L302) | 302 | `""` | — |
| [SRC-6BF96689A8-L000303](../../tests/test_research.py#L303) | 303 | `""` | — |
| [SRC-6BF96689A8-L000304](../../tests/test_research.py#L304) | 304 | `"def test_collect_research_skips_provider_calls_without_topic_or_direct_url(monkeypatch):"` | — |
| [SRC-6BF96689A8-L000305](../../tests/test_research.py#L305) | 305 | `"    from agents.web_agent import WebAgent"` | — |
| [SRC-6BF96689A8-L000306](../../tests/test_research.py#L306) | 306 | `""` | — |
| [SRC-6BF96689A8-L000307](../../tests/test_research.py#L307) | 307 | `"    agent = WebAgent()"` | — |
| [SRC-6BF96689A8-L000308](../../tests/test_research.py#L308) | 308 | `"    seen = []"` | — |
| [SRC-6BF96689A8-L000309](../../tests/test_research.py#L309) | 309 | `"    monkeypatch.setattr(agent, \"_search_web\", lambda query: seen.append(query) or [])"` | — |
| [SRC-6BF96689A8-L000310](../../tests/test_research.py#L310) | 310 | `"    sources, warnings, report = agent._collect_research({"` | — |
| [SRC-6BF96689A8-L000311](../../tests/test_research.py#L311) | 311 | `"        \"queries\": [\"اذكر مصادر موثوقة، روابط مباشرة، باختصار\"],"` | — |
| [SRC-6BF96689A8-L000312](../../tests/test_research.py#L312) | 312 | `"        \"direct_urls\": [],"` | — |
| [SRC-6BF96689A8-L000313](../../tests/test_research.py#L313) | 313 | `"        \"social_focus\": False,"` | — |
| [SRC-6BF96689A8-L000314](../../tests/test_research.py#L314) | 314 | `"        \"freshness\": \"any\","` | — |
| [SRC-6BF96689A8-L000315](../../tests/test_research.py#L315) | 315 | `"        \"depth\": \"standard\","` | — |
| [SRC-6BF96689A8-L000316](../../tests/test_research.py#L316) | 316 | `"        \"platforms\": [],"` | — |
| [SRC-6BF96689A8-L000317](../../tests/test_research.py#L317) | 317 | `"    })"` | — |
| [SRC-6BF96689A8-L000318](../../tests/test_research.py#L318) | 318 | `""` | — |
| [SRC-6BF96689A8-L000319](../../tests/test_research.py#L319) | 319 | `"    assert sources == []"` | — |
| [SRC-6BF96689A8-L000320](../../tests/test_research.py#L320) | 320 | `"    assert report[\"queries_planned\"] == 0"` | — |
| [SRC-6BF96689A8-L000321](../../tests/test_research.py#L321) | 321 | `"    assert report[\"queries_attempted\"] == 0"` | — |
| [SRC-6BF96689A8-L000322](../../tests/test_research.py#L322) | 322 | `"    assert seen == []"` | — |
| [SRC-6BF96689A8-L000323](../../tests/test_research.py#L323) | 323 | `"    assert any(\"لم تُستدعَ محركات البحث\" in warning for warning in warnings)"` | — |
| [SRC-6BF96689A8-L000324](../../tests/test_research.py#L324) | 324 | `""` | — |
| [SRC-6BF96689A8-L000325](../../tests/test_research.py#L325) | 325 | `""` | — |
| [SRC-6BF96689A8-L000326](../../tests/test_research.py#L326) | 326 | `"def test_fallback_plan_keeps_direct_url_without_generic_keyword_query():"` | — |
| [SRC-6BF96689A8-L000327](../../tests/test_research.py#L327) | 327 | `"    plan = fallback_plan(\"https://example.com/research\")"` | — |
| [SRC-6BF96689A8-L000328](../../tests/test_research.py#L328) | 328 | `"    assert plan[\"direct_urls\"] == [\"https://example.com/research\"]"` | — |
| [SRC-6BF96689A8-L000329](../../tests/test_research.py#L329) | 329 | `"    assert plan[\"queries\"] == []"` | — |
## اختبارات

### FILE-01E35ABC46 — [tests/test_research_guardrails.py](../../tests/test_research_guardrails.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-01E35ABC46-L000001](../../tests/test_research_guardrails.py#L1) | 1 | `"\"\"\"Regression and adversarial tests for depth, freshness, relevance, evidence.\"\"\""` | — |
| [SRC-01E35ABC46-L000002](../../tests/test_research_guardrails.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-01E35ABC46-L000003](../../tests/test_research_guardrails.py#L3) | 3 | `""` | — |
| [SRC-01E35ABC46-L000004](../../tests/test_research_guardrails.py#L4) | 4 | `"from datetime import UTC, datetime"` | — |
| [SRC-01E35ABC46-L000005](../../tests/test_research_guardrails.py#L5) | 5 | `""` | — |
| [SRC-01E35ABC46-L000006](../../tests/test_research_guardrails.py#L6) | 6 | `"from agents.research_guardrails import ("` | — |
| [SRC-01E35ABC46-L000007](../../tests/test_research_guardrails.py#L7) | 7 | `"    apply_source_guardrails,"` | — |
| [SRC-01E35ABC46-L000008](../../tests/test_research_guardrails.py#L8) | 8 | `"    assess_current_source,"` | — |
| [SRC-01E35ABC46-L000009](../../tests/test_research_guardrails.py#L9) | 9 | `"    classify_social_source,"` | — |
| [SRC-01E35ABC46-L000010](../../tests/test_research_guardrails.py#L10) | 10 | `"    requires_official_government_domain,"` | — |
| [SRC-01E35ABC46-L000011](../../tests/test_research_guardrails.py#L11) | 11 | `")"` | — |
| [SRC-01E35ABC46-L000012](../../tests/test_research_guardrails.py#L12) | 12 | `"from agents.research import ("` | — |
| [SRC-01E35ABC46-L000013](../../tests/test_research_guardrails.py#L13) | 13 | `"    decide_evidence_status,"` | — |
| [SRC-01E35ABC46-L000014](../../tests/test_research_guardrails.py#L14) | 14 | `"    detect_depth,"` | — |
| [SRC-01E35ABC46-L000015](../../tests/test_research_guardrails.py#L15) | 15 | `"    detect_freshness,"` | — |
| [SRC-01E35ABC46-L000016](../../tests/test_research_guardrails.py#L16) | 16 | `"    filter_relevant_sources,"` | — |
| [SRC-01E35ABC46-L000017](../../tests/test_research_guardrails.py#L17) | 17 | `"    source_relevance_score,"` | — |
| [SRC-01E35ABC46-L000018](../../tests/test_research_guardrails.py#L18) | 18 | `")"` | — |
| [SRC-01E35ABC46-L000019](../../tests/test_research_guardrails.py#L19) | 19 | `""` | — |
| [SRC-01E35ABC46-L000020](../../tests/test_research_guardrails.py#L20) | 20 | `""` | — |
| [SRC-01E35ABC46-L000021](../../tests/test_research_guardrails.py#L21) | 21 | `"# --- detect_depth -----------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000022](../../tests/test_research_guardrails.py#L22) | 22 | `""` | — |
| [SRC-01E35ABC46-L000023](../../tests/test_research_guardrails.py#L23) | 23 | `"def test_depth_deep_english_phrases():"` | — |
| [SRC-01E35ABC46-L000024](../../tests/test_research_guardrails.py#L24) | 24 | `"    assert detect_depth(\"Please do a deep research on climate policy\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000025](../../tests/test_research_guardrails.py#L25) | 25 | `"    assert detect_depth(\"in-depth comparison of EV batteries\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000026](../../tests/test_research_guardrails.py#L26) | 26 | `"    assert detect_depth(\"comprehensive analysis of market risks\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000027](../../tests/test_research_guardrails.py#L27) | 27 | `""` | — |
| [SRC-01E35ABC46-L000028](../../tests/test_research_guardrails.py#L28) | 28 | `""` | — |
| [SRC-01E35ABC46-L000029](../../tests/test_research_guardrails.py#L29) | 29 | `"def test_depth_deep_arabic_phrases():"` | — |
| [SRC-01E35ABC46-L000030](../../tests/test_research_guardrails.py#L30) | 30 | `"    assert detect_depth(\"أريد بحث عميق عن الذكاء الاصطناعي\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000031](../../tests/test_research_guardrails.py#L31) | 31 | `"    assert detect_depth(\"قارن بين السيارات الكهربائية والبنزين\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000032](../../tests/test_research_guardrails.py#L32) | 32 | `"    assert detect_depth(\"بحث شامل بالتفصيل عن الذهب\") == \"deep\""` | — |
| [SRC-01E35ABC46-L000033](../../tests/test_research_guardrails.py#L33) | 33 | `""` | — |
| [SRC-01E35ABC46-L000034](../../tests/test_research_guardrails.py#L34) | 34 | `""` | — |
| [SRC-01E35ABC46-L000035](../../tests/test_research_guardrails.py#L35) | 35 | `"def test_depth_standard_ordinary_questions():"` | — |
| [SRC-01E35ABC46-L000036](../../tests/test_research_guardrails.py#L36) | 36 | `"    assert detect_depth(\"what is the capital of France\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000037](../../tests/test_research_guardrails.py#L37) | 37 | `"    assert detect_depth(\"ما عاصمة مصر\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000038](../../tests/test_research_guardrails.py#L38) | 38 | `"    assert detect_depth(\"I know about electric cars\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000039](../../tests/test_research_guardrails.py#L39) | 39 | `"    assert detect_depth(\"hello\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000040](../../tests/test_research_guardrails.py#L40) | 40 | `"    assert detect_depth(\"\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000041](../../tests/test_research_guardrails.py#L41) | 41 | `""` | — |
| [SRC-01E35ABC46-L000042](../../tests/test_research_guardrails.py#L42) | 42 | `""` | — |
| [SRC-01E35ABC46-L000043](../../tests/test_research_guardrails.py#L43) | 43 | `"def test_depth_does_not_trigger_on_partial_words():"` | — |
| [SRC-01E35ABC46-L000044](../../tests/test_research_guardrails.py#L44) | 44 | `"    # \"sources\" is a deep term; ensure isolated ordinary use still works via whole-word"` | — |
| [SRC-01E35ABC46-L000045](../../tests/test_research_guardrails.py#L45) | 45 | `"    assert detect_depth(\"the river sources of the Nile\") in {\"deep\", \"standard\"}  # may match"` | — |
| [SRC-01E35ABC46-L000046](../../tests/test_research_guardrails.py#L46) | 46 | `"    assert detect_depth(\"tell me a joke\") == \"standard\""` | — |
| [SRC-01E35ABC46-L000047](../../tests/test_research_guardrails.py#L47) | 47 | `""` | — |
| [SRC-01E35ABC46-L000048](../../tests/test_research_guardrails.py#L48) | 48 | `""` | — |
| [SRC-01E35ABC46-L000049](../../tests/test_research_guardrails.py#L49) | 49 | `"# --- detect_freshness -------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000050](../../tests/test_research_guardrails.py#L50) | 50 | `""` | — |
| [SRC-01E35ABC46-L000051](../../tests/test_research_guardrails.py#L51) | 51 | `"def test_freshness_positive_english():"` | — |
| [SRC-01E35ABC46-L000052](../../tests/test_research_guardrails.py#L52) | 52 | `"    assert detect_freshness(\"what is happening now\") is True"` | — |
| [SRC-01E35ABC46-L000053](../../tests/test_research_guardrails.py#L53) | 53 | `"    assert detect_freshness(\"latest news about Egypt\") is True"` | — |
| [SRC-01E35ABC46-L000054](../../tests/test_research_guardrails.py#L54) | 54 | `"    assert detect_freshness(\"price today of gold\") is True"` | — |
| [SRC-01E35ABC46-L000055](../../tests/test_research_guardrails.py#L55) | 55 | `"    assert detect_freshness(\"breaking news\") is True"` | — |
| [SRC-01E35ABC46-L000056](../../tests/test_research_guardrails.py#L56) | 56 | `""` | — |
| [SRC-01E35ABC46-L000057](../../tests/test_research_guardrails.py#L57) | 57 | `""` | — |
| [SRC-01E35ABC46-L000058](../../tests/test_research_guardrails.py#L58) | 58 | `"def test_freshness_positive_arabic():"` | — |
| [SRC-01E35ABC46-L000059](../../tests/test_research_guardrails.py#L59) | 59 | `"    assert detect_freshness(\"ما هي آخر الأخبار عن الذهب\") is True"` | — |
| [SRC-01E35ABC46-L000060](../../tests/test_research_guardrails.py#L60) | 60 | `"    assert detect_freshness(\"سعر اليوم للدولار\") is True"` | — |
| [SRC-01E35ABC46-L000061](../../tests/test_research_guardrails.py#L61) | 61 | `"    assert detect_freshness(\"مستجدات السوق حاليا\") is True"` | — |
| [SRC-01E35ABC46-L000062](../../tests/test_research_guardrails.py#L62) | 62 | `""` | — |
| [SRC-01E35ABC46-L000063](../../tests/test_research_guardrails.py#L63) | 63 | `""` | — |
| [SRC-01E35ABC46-L000064](../../tests/test_research_guardrails.py#L64) | 64 | `"def test_freshness_negative_know_and_snowden():"` | — |
| [SRC-01E35ABC46-L000065](../../tests/test_research_guardrails.py#L65) | 65 | `"    assert detect_freshness(\"I know about cars\") is False"` | — |
| [SRC-01E35ABC46-L000066](../../tests/test_research_guardrails.py#L66) | 66 | `"    assert detect_freshness(\"Snowden revelations summary\") is False"` | — |
| [SRC-01E35ABC46-L000067](../../tests/test_research_guardrails.py#L67) | 67 | `"    assert detect_freshness(\"knowledge graph basics\") is False"` | — |
| [SRC-01E35ABC46-L000068](../../tests/test_research_guardrails.py#L68) | 68 | `"    assert detect_freshness(\"ما عاصمة فرنسا\") is False"` | — |
| [SRC-01E35ABC46-L000069](../../tests/test_research_guardrails.py#L69) | 69 | `""` | — |
| [SRC-01E35ABC46-L000070](../../tests/test_research_guardrails.py#L70) | 70 | `""` | — |
| [SRC-01E35ABC46-L000071](../../tests/test_research_guardrails.py#L71) | 71 | `"# --- relevance gate ---------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000072](../../tests/test_research_guardrails.py#L72) | 72 | `""` | — |
| [SRC-01E35ABC46-L000073](../../tests/test_research_guardrails.py#L73) | 73 | `"def test_relevance_keeps_matching_source():"` | — |
| [SRC-01E35ABC46-L000074](../../tests/test_research_guardrails.py#L74) | 74 | `"    src = {"` | — |
| [SRC-01E35ABC46-L000075](../../tests/test_research_guardrails.py#L75) | 75 | `"        \"title\": \"أسعار السيارات الكهربائية في مصر 2026\","` | — |
| [SRC-01E35ABC46-L000076](../../tests/test_research_guardrails.py#L76) | 76 | `"        \"url\": \"https://example.com/ev-egypt\","` | — |
| [SRC-01E35ABC46-L000077](../../tests/test_research_guardrails.py#L77) | 77 | `"        \"snippet\": \"ارتفعت حصة السيارات الكهربائية في السوق المصري هذا العام.\","` | — |
| [SRC-01E35ABC46-L000078](../../tests/test_research_guardrails.py#L78) | 78 | `"        \"domain\": \"example.com\","` | — |
| [SRC-01E35ABC46-L000079](../../tests/test_research_guardrails.py#L79) | 79 | `"        \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000080](../../tests/test_research_guardrails.py#L80) | 80 | `"        \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000081](../../tests/test_research_guardrails.py#L81) | 81 | `"    }"` | — |
| [SRC-01E35ABC46-L000082](../../tests/test_research_guardrails.py#L82) | 82 | `"    rel = source_relevance_score(src, \"أسعار السيارات الكهربائية في مصر\")"` | — |
| [SRC-01E35ABC46-L000083](../../tests/test_research_guardrails.py#L83) | 83 | `"    assert rel[\"accepted\"] is True"` | — |
| [SRC-01E35ABC46-L000084](../../tests/test_research_guardrails.py#L84) | 84 | `"    assert rel[\"score\"] >= 18"` | — |
| [SRC-01E35ABC46-L000085](../../tests/test_research_guardrails.py#L85) | 85 | `""` | — |
| [SRC-01E35ABC46-L000086](../../tests/test_research_guardrails.py#L86) | 86 | `"    # English-English match"` | — |
| [SRC-01E35ABC46-L000087](../../tests/test_research_guardrails.py#L87) | 87 | `"    src_en = {"` | — |
| [SRC-01E35ABC46-L000088](../../tests/test_research_guardrails.py#L88) | 88 | `"        \"title\": \"Electric vehicles in Egypt 2026\","` | — |
| [SRC-01E35ABC46-L000089](../../tests/test_research_guardrails.py#L89) | 89 | `"        \"url\": \"https://example.com/ev-egypt-en\","` | — |
| [SRC-01E35ABC46-L000090](../../tests/test_research_guardrails.py#L90) | 90 | `"        \"snippet\": \"Market share of electric cars in Egypt rose this year.\","` | — |
| [SRC-01E35ABC46-L000091](../../tests/test_research_guardrails.py#L91) | 91 | `"        \"domain\": \"example.com\","` | — |
| [SRC-01E35ABC46-L000092](../../tests/test_research_guardrails.py#L92) | 92 | `"        \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000093](../../tests/test_research_guardrails.py#L93) | 93 | `"        \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000094](../../tests/test_research_guardrails.py#L94) | 94 | `"    }"` | — |
| [SRC-01E35ABC46-L000095](../../tests/test_research_guardrails.py#L95) | 95 | `"    rel_en = source_relevance_score(src_en, \"electric vehicles Egypt market share\")"` | — |
| [SRC-01E35ABC46-L000096](../../tests/test_research_guardrails.py#L96) | 96 | `"    assert rel_en[\"accepted\"] is True"` | — |
| [SRC-01E35ABC46-L000097](../../tests/test_research_guardrails.py#L97) | 97 | `""` | — |
| [SRC-01E35ABC46-L000098](../../tests/test_research_guardrails.py#L98) | 98 | `""` | — |
| [SRC-01E35ABC46-L000099](../../tests/test_research_guardrails.py#L99) | 99 | `"def test_relevance_rejects_unrelated():"` | — |
| [SRC-01E35ABC46-L000100](../../tests/test_research_guardrails.py#L100) | 100 | `"    src = {"` | — |
| [SRC-01E35ABC46-L000101](../../tests/test_research_guardrails.py#L101) | 101 | `"        \"title\": \"Best pasta recipes\","` | — |
| [SRC-01E35ABC46-L000102](../../tests/test_research_guardrails.py#L102) | 102 | `"        \"url\": \"https://cooking.example/pasta\","` | — |
| [SRC-01E35ABC46-L000103](../../tests/test_research_guardrails.py#L103) | 103 | `"        \"snippet\": \"How to make carbonara at home with eggs and cheese.\","` | — |
| [SRC-01E35ABC46-L000104](../../tests/test_research_guardrails.py#L104) | 104 | `"        \"domain\": \"cooking.example\","` | — |
| [SRC-01E35ABC46-L000105](../../tests/test_research_guardrails.py#L105) | 105 | `"        \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000106](../../tests/test_research_guardrails.py#L106) | 106 | `"        \"providers\": [\"bing\"],"` | — |
| [SRC-01E35ABC46-L000107](../../tests/test_research_guardrails.py#L107) | 107 | `"    }"` | — |
| [SRC-01E35ABC46-L000108](../../tests/test_research_guardrails.py#L108) | 108 | `"    rel = source_relevance_score(src, \"أسعار السيارات الكهربائية في مصر\")"` | — |
| [SRC-01E35ABC46-L000109](../../tests/test_research_guardrails.py#L109) | 109 | `"    assert rel[\"accepted\"] is False"` | — |
| [SRC-01E35ABC46-L000110](../../tests/test_research_guardrails.py#L110) | 110 | `""` | — |
| [SRC-01E35ABC46-L000111](../../tests/test_research_guardrails.py#L111) | 111 | `""` | — |
| [SRC-01E35ABC46-L000112](../../tests/test_research_guardrails.py#L112) | 112 | `"def test_relevance_keeps_official_despite_wording():"` | — |
| [SRC-01E35ABC46-L000113](../../tests/test_research_guardrails.py#L113) | 113 | `"    src = {"` | — |
| [SRC-01E35ABC46-L000114](../../tests/test_research_guardrails.py#L114) | 114 | `"        \"title\": \"Official statistical bulletin Q1\","` | — |
| [SRC-01E35ABC46-L000115](../../tests/test_research_guardrails.py#L115) | 115 | `"        \"url\": \"https://www.capmas.gov.eg/bulletin\","` | — |
| [SRC-01E35ABC46-L000116](../../tests/test_research_guardrails.py#L116) | 116 | `"        \"snippet\": \"National statistics release.\","` | — |
| [SRC-01E35ABC46-L000117](../../tests/test_research_guardrails.py#L117) | 117 | `"        \"domain\": \"capmas.gov.eg\","` | — |
| [SRC-01E35ABC46-L000118](../../tests/test_research_guardrails.py#L118) | 118 | `"        \"source_class\": \"government\","` | — |
| [SRC-01E35ABC46-L000119](../../tests/test_research_guardrails.py#L119) | 119 | `"        \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000120](../../tests/test_research_guardrails.py#L120) | 120 | `"    }"` | — |
| [SRC-01E35ABC46-L000121](../../tests/test_research_guardrails.py#L121) | 121 | `"    rel = source_relevance_score(src, \"أسعار السيارات الكهربائية في مصر\")"` | — |
| [SRC-01E35ABC46-L000122](../../tests/test_research_guardrails.py#L122) | 122 | `"    assert rel[\"accepted\"] is True"` | — |
| [SRC-01E35ABC46-L000123](../../tests/test_research_guardrails.py#L123) | 123 | `"    assert rel[\"reason\"] in {\"accepted\", \"kept_official_despite_low_overlap\"}"` | — |
| [SRC-01E35ABC46-L000124](../../tests/test_research_guardrails.py#L124) | 124 | `""` | — |
| [SRC-01E35ABC46-L000125](../../tests/test_research_guardrails.py#L125) | 125 | `""` | — |
| [SRC-01E35ABC46-L000126](../../tests/test_research_guardrails.py#L126) | 126 | `"def test_filter_deduplicates():"` | — |
| [SRC-01E35ABC46-L000127](../../tests/test_research_guardrails.py#L127) | 127 | `"    sources = ["` | — |
| [SRC-01E35ABC46-L000128](../../tests/test_research_guardrails.py#L128) | 128 | `"        {"` | — |
| [SRC-01E35ABC46-L000129](../../tests/test_research_guardrails.py#L129) | 129 | `"            \"title\": \"Same Article Title\","` | — |
| [SRC-01E35ABC46-L000130](../../tests/test_research_guardrails.py#L130) | 130 | `"            \"url\": \"https://a.example/1\","` | — |
| [SRC-01E35ABC46-L000131](../../tests/test_research_guardrails.py#L131) | 131 | `"            \"snippet\": \"electric vehicles Egypt market\","` | — |
| [SRC-01E35ABC46-L000132](../../tests/test_research_guardrails.py#L132) | 132 | `"            \"domain\": \"a.example\","` | — |
| [SRC-01E35ABC46-L000133](../../tests/test_research_guardrails.py#L133) | 133 | `"            \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000134](../../tests/test_research_guardrails.py#L134) | 134 | `"            \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000135](../../tests/test_research_guardrails.py#L135) | 135 | `"        },"` | — |
| [SRC-01E35ABC46-L000136](../../tests/test_research_guardrails.py#L136) | 136 | `"        {"` | — |
| [SRC-01E35ABC46-L000137](../../tests/test_research_guardrails.py#L137) | 137 | `"            \"title\": \"Same Article Title\","` | — |
| [SRC-01E35ABC46-L000138](../../tests/test_research_guardrails.py#L138) | 138 | `"            \"url\": \"https://a.example/1?utm=x\","` | — |
| [SRC-01E35ABC46-L000139](../../tests/test_research_guardrails.py#L139) | 139 | `"            \"snippet\": \"electric vehicles Egypt market again\","` | — |
| [SRC-01E35ABC46-L000140](../../tests/test_research_guardrails.py#L140) | 140 | `"            \"domain\": \"a.example\","` | — |
| [SRC-01E35ABC46-L000141](../../tests/test_research_guardrails.py#L141) | 141 | `"            \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000142](../../tests/test_research_guardrails.py#L142) | 142 | `"            \"providers\": [\"bing\"],"` | — |
| [SRC-01E35ABC46-L000143](../../tests/test_research_guardrails.py#L143) | 143 | `"        },"` | — |
| [SRC-01E35ABC46-L000144](../../tests/test_research_guardrails.py#L144) | 144 | `"    ]"` | — |
| [SRC-01E35ABC46-L000145](../../tests/test_research_guardrails.py#L145) | 145 | `"    kept, diag = filter_relevant_sources("` | — |
| [SRC-01E35ABC46-L000146](../../tests/test_research_guardrails.py#L146) | 146 | `"        sources, \"electric vehicles Egypt\", [\"electric vehicles Egypt\"]"` | — |
| [SRC-01E35ABC46-L000147](../../tests/test_research_guardrails.py#L147) | 147 | `"    )"` | — |
| [SRC-01E35ABC46-L000148](../../tests/test_research_guardrails.py#L148) | 148 | `"    assert len(kept) == 1"` | — |
| [SRC-01E35ABC46-L000149](../../tests/test_research_guardrails.py#L149) | 149 | `"    assert any(d[\"reason\"] == \"duplicate_title_domain\" for d in diag)"` | — |
| [SRC-01E35ABC46-L000150](../../tests/test_research_guardrails.py#L150) | 150 | `""` | — |
| [SRC-01E35ABC46-L000151](../../tests/test_research_guardrails.py#L151) | 151 | `""` | — |
| [SRC-01E35ABC46-L000152](../../tests/test_research_guardrails.py#L152) | 152 | `"def test_filter_empty_and_failed_extract():"` | — |
| [SRC-01E35ABC46-L000153](../../tests/test_research_guardrails.py#L153) | 153 | `"    kept, diag = filter_relevant_sources([], \"anything\")"` | — |
| [SRC-01E35ABC46-L000154](../../tests/test_research_guardrails.py#L154) | 154 | `"    assert kept == []"` | — |
| [SRC-01E35ABC46-L000155](../../tests/test_research_guardrails.py#L155) | 155 | `"    assert diag == []"` | — |
| [SRC-01E35ABC46-L000156](../../tests/test_research_guardrails.py#L156) | 156 | `"    src = {"` | — |
| [SRC-01E35ABC46-L000157](../../tests/test_research_guardrails.py#L157) | 157 | `"        \"title\": \"\","` | — |
| [SRC-01E35ABC46-L000158](../../tests/test_research_guardrails.py#L158) | 158 | `"        \"url\": \"https://example.com/x\","` | — |
| [SRC-01E35ABC46-L000159](../../tests/test_research_guardrails.py#L159) | 159 | `"        \"snippet\": \"\","` | — |
| [SRC-01E35ABC46-L000160](../../tests/test_research_guardrails.py#L160) | 160 | `"        \"page_text\": \"\","` | — |
| [SRC-01E35ABC46-L000161](../../tests/test_research_guardrails.py#L161) | 161 | `"        \"domain\": \"example.com\","` | — |
| [SRC-01E35ABC46-L000162](../../tests/test_research_guardrails.py#L162) | 162 | `"        \"source_class\": \"general\","` | — |
| [SRC-01E35ABC46-L000163](../../tests/test_research_guardrails.py#L163) | 163 | `"        \"providers\": [\"ddg\"],"` | — |
| [SRC-01E35ABC46-L000164](../../tests/test_research_guardrails.py#L164) | 164 | `"    }"` | — |
| [SRC-01E35ABC46-L000165](../../tests/test_research_guardrails.py#L165) | 165 | `"    _kept2, diag2 = filter_relevant_sources([src], \"unrelated pasta recipes\")"` | — |
| [SRC-01E35ABC46-L000166](../../tests/test_research_guardrails.py#L166) | 166 | `"    # May reject for low overlap"` | — |
| [SRC-01E35ABC46-L000167](../../tests/test_research_guardrails.py#L167) | 167 | `"    assert isinstance(diag2, list)"` | — |
| [SRC-01E35ABC46-L000168](../../tests/test_research_guardrails.py#L168) | 168 | `""` | — |
| [SRC-01E35ABC46-L000169](../../tests/test_research_guardrails.py#L169) | 169 | `""` | — |
| [SRC-01E35ABC46-L000170](../../tests/test_research_guardrails.py#L170) | 170 | `"# --- evidence status --------------------------------------------------------"` | — |
| [SRC-01E35ABC46-L000171](../../tests/test_research_guardrails.py#L171) | 171 | `""` | — |
| [SRC-01E35ABC46-L000172](../../tests/test_research_guardrails.py#L172) | 172 | `"def test_evidence_adequate():"` | — |
| [SRC-01E35ABC46-L000173](../../tests/test_research_guardrails.py#L173) | 173 | `"    sources = ["` | — |
| [SRC-01E35ABC46-L000174](../../tests/test_research_guardrails.py#L174) | 174 | `"        {\"url\": f\"https://a{i}.example/p\", \"domain\": f\"a{i}.example\","` | — |
| [SRC-01E35ABC46-L000175](../../tests/test_research_guardrails.py#L175) | 175 | `"         \"snippet\": \"content\", \"page_fetched\": True, \"source_class\": \"general\"}"` | — |
| [SRC-01E35ABC46-L000176](../../tests/test_research_guardrails.py#L176) | 176 | `"        for i in range(4)"` | — |
| [SRC-01E35ABC46-L000177](../../tests/test_research_guardrails.py#L177) | 177 | `"    ]"` | — |
| [SRC-01E35ABC46-L000178](../../tests/test_research_guardrails.py#L178) | 178 | `"    sources[0][\"source_class\"] = \"government\""` | — |
| [SRC-01E35ABC46-L000179](../../tests/test_research_guardrails.py#L179) | 179 | `"    decision = decide_evidence_status(sources, pages_read=2)"` | — |
| [SRC-01E35ABC46-L000180](../../tests/test_research_guardrails.py#L180) | 180 | `"    assert decision[\"evidence_status\"] == \"adequate\""` | — |
| [SRC-01E35ABC46-L000181](../../tests/test_research_guardrails.py#L181) | 181 | `"    assert decision[\"should_abstain\"] is False"` | — |
| [SRC-01E35ABC46-L000182](../../tests/test_research_guardrails.py#L182) | 182 | `""` | — |
| [SRC-01E35ABC46-L000183](../../tests/test_research_guardrails.py#L183) | 183 | `""` | — |
| [SRC-01E35ABC46-L000184](../../tests/test_research_guardrails.py#L184) | 184 | `"def test_evidence_insufficient_empty():"` | — |
| [SRC-01E35ABC46-L000185](../../tests/test_research_guardrails.py#L185) | 185 | `"    decision = decide_evidence_status([], search_attempted=True)"` | — |
| [SRC-01E35ABC46-L000186](../../tests/test_research_guardrails.py#L186) | 186 | `"    assert decision[\"evidence_status\"] == \"insufficient\""` | — |
| [SRC-01E35ABC46-L000187](../../tests/test_research_guardrails.py#L187) | 187 | `"    assert decision[\"should_abstain\"] is True"` | — |
| [SRC-01E35ABC46-L000188](../../tests/test_research_guardrails.py#L188) | 188 | `""` | — |
| [SRC-01E35ABC46-L000189](../../tests/test_research_guardrails.py#L189) | 189 | `""` | — |
| [SRC-01E35ABC46-L000190](../../tests/test_research_guardrails.py#L190) | 190 | `"def test_evidence_failed_provider():"` | — |
| [SRC-01E35ABC46-L000191](../../tests/test_research_guardrails.py#L191) | 191 | `"    decision = decide_evidence_status([], provider_failures=2, search_attempted=True)"` | — |
| [SRC-01E35ABC46-L000192](../../tests/test_research_guardrails.py#L192) | 192 | `"    assert decision[\"evidence_status\"] == \"failed\""` | — |
| [SRC-01E35ABC46-L000193](../../tests/test_research_guardrails.py#L193) | 193 | `"    assert decision[\"should_abstain\"] is True"` | — |
| [SRC-01E35ABC46-L000194](../../tests/test_research_guardrails.py#L194) | 194 | `""` | — |
| [SRC-01E35ABC46-L000195](../../tests/test_research_guardrails.py#L195) | 195 | `""` | — |
| [SRC-01E35ABC46-L000196](../../tests/test_research_guardrails.py#L196) | 196 | `"def test_evidence_partial_single_source():"` | — |
| [SRC-01E35ABC46-L000197](../../tests/test_research_guardrails.py#L197) | 197 | `"    sources = ["` | — |
| [SRC-01E35ABC46-L000198](../../tests/test_research_guardrails.py#L198) | 198 | `"        {\"url\": \"https://a.example/p\", \"domain\": \"a.example\","` | — |
| [SRC-01E35ABC46-L000199](../../tests/test_research_guardrails.py#L199) | 199 | `"         \"snippet\": \"some text\", \"page_fetched\": True, \"source_class\": \"general\"}"` | — |
| [SRC-01E35ABC46-L000200](../../tests/test_research_guardrails.py#L200) | 200 | `"    ]"` | — |
| [SRC-01E35ABC46-L000201](../../tests/test_research_guardrails.py#L201) | 201 | `"    decision = decide_evidence_status(sources, pages_read=1)"` | — |
| [SRC-01E35ABC46-L000202](../../tests/test_research_guardrails.py#L202) | 202 | `"    assert decision[\"evidence_status\"] == \"partial\""` | — |
| [SRC-01E35ABC46-L000203](../../tests/test_research_guardrails.py#L203) | 203 | `"    assert decision[\"should_abstain\"] is False"` | — |
| [SRC-01E35ABC46-L000204](../../tests/test_research_guardrails.py#L204) | 204 | `""` | — |
| [SRC-01E35ABC46-L000205](../../tests/test_research_guardrails.py#L205) | 205 | `""` | — |
| [SRC-01E35ABC46-L000206](../../tests/test_research_guardrails.py#L206) | 206 | `""` | — |
| [SRC-01E35ABC46-L000207](../../tests/test_research_guardrails.py#L207) | 207 | `"# --- task-specific evidence guardrails ---------------------------------------"` | — |
| [SRC-01E35ABC46-L000208](../../tests/test_research_guardrails.py#L208) | 208 | `""` | — |
| [SRC-01E35ABC46-L000209](../../tests/test_research_guardrails.py#L209) | 209 | `"_GUARDRAIL_NOW = datetime(2026, 10, 28, 12, 0, tzinfo=UTC)"` | — |
| [SRC-01E35ABC46-L000210](../../tests/test_research_guardrails.py#L210) | 210 | `""` | — |
| [SRC-01E35ABC46-L000211](../../tests/test_research_guardrails.py#L211) | 211 | `""` | — |
| [SRC-01E35ABC46-L000212](../../tests/test_research_guardrails.py#L212) | 212 | `"def _guardrail_source("` | — |
| [SRC-01E35ABC46-L000213](../../tests/test_research_guardrails.py#L213) | 213 | `"    url: str,"` | — |
| [SRC-01E35ABC46-L000214](../../tests/test_research_guardrails.py#L214) | 214 | `"    *,"` | — |
| [SRC-01E35ABC46-L000215](../../tests/test_research_guardrails.py#L215) | 215 | `"    title: str = \"معلومات عن وزارة الاتصالات\","` | — |
| [SRC-01E35ABC46-L000216](../../tests/test_research_guardrails.py#L216) | 216 | `"    snippet: str = \"معلومات عن وزارة الاتصالات وتكنولوجيا المعلومات في مصر\","` | — |
| [SRC-01E35ABC46-L000217](../../tests/test_research_guardrails.py#L217) | 217 | `"    published_at: str = \"2026-10-27T10:00:00Z\","` | — |
| [SRC-01E35ABC46-L000218](../../tests/test_research_guardrails.py#L218) | 218 | `"    page_fetched: bool = True,"` | — |
| [SRC-01E35ABC46-L000219](../../tests/test_research_guardrails.py#L219) | 219 | `"    page_text: str = \"نص مقروء من الصفحة عن وزارة الاتصالات\","` | — |
| [SRC-01E35ABC46-L000220](../../tests/test_research_guardrails.py#L220) | 220 | `") -> dict:"` | — |
| [SRC-01E35ABC46-L000221](../../tests/test_research_guardrails.py#L221) | 221 | `"    return {"` | — |
| [SRC-01E35ABC46-L000222](../../tests/test_research_guardrails.py#L222) | 222 | `"        \"title\": title,"` | — |
| [SRC-01E35ABC46-L000223](../../tests/test_research_guardrails.py#L223) | 223 | `"        \"url\": url,"` | — |
| [SRC-01E35ABC46-L000224](../../tests/test_research_guardrails.py#L224) | 224 | `"        \"snippet\": snippet,"` | — |
| [SRC-01E35ABC46-L000225](../../tests/test_research_guardrails.py#L225) | 225 | `"        \"published_at\": published_at,"` | — |
| [SRC-01E35ABC46-L000226](../../tests/test_research_guardrails.py#L226) | 226 | `"        \"page_fetched\": page_fetched,"` | — |
| [SRC-01E35ABC46-L000227](../../tests/test_research_guardrails.py#L227) | 227 | `"        \"page_text\": page_text,"` | — |
| [SRC-01E35ABC46-L000228](../../tests/test_research_guardrails.py#L228) | 228 | `"    }"` | — |
| [SRC-01E35ABC46-L000229](../../tests/test_research_guardrails.py#L229) | 229 | `""` | — |
| [SRC-01E35ABC46-L000230](../../tests/test_research_guardrails.py#L230) | 230 | `""` | — |
| [SRC-01E35ABC46-L000231](../../tests/test_research_guardrails.py#L231) | 231 | `"def test_official_government_website_request_rejects_tourism_domain() -> None:"` | — |
| [SRC-01E35ABC46-L000232](../../tests/test_research_guardrails.py#L232) | 232 | `"    question = \"ابحث عن الموقع الرسمي لوزارة الاتصالات وتكنولوجيا المعلومات المصرية\""` | — |
| [SRC-01E35ABC46-L000233](../../tests/test_research_guardrails.py#L233) | 233 | `"    assert requires_official_government_domain(question)"` | — |
| [SRC-01E35ABC46-L000234](../../tests/test_research_guardrails.py#L234) | 234 | `"    candidates = ["` | — |
| [SRC-01E35ABC46-L000235](../../tests/test_research_guardrails.py#L235) | 235 | `"        _guardrail_source("` | — |
| [SRC-01E35ABC46-L000236](../../tests/test_research_guardrails.py#L236) | 236 | `"            \"https://visitegypt.com/\","` | — |
| [SRC-01E35ABC46-L000237](../../tests/test_research_guardrails.py#L237) | 237 | `"            title=\"وزارة الاتصالات في مصر ومعلومات سياحية\","` | — |
| [SRC-01E35ABC46-L000238](../../tests/test_research_guardrails.py#L238) | 238 | `"        ),"` | — |
| [SRC-01E35ABC46-L000239](../../tests/test_research_guardrails.py#L239) | 239 | `"        _guardrail_source("` | — |
| [SRC-01E35ABC46-L000240](../../tests/test_research_guardrails.py#L240) | 240 | `"            \"https://mcit.gov.eg/\","` | — |
| [SRC-01E35ABC46-L000241](../../tests/test_research_guardrails.py#L241) | 241 | `"            title=\"وزارة الاتصالات وتكنولوجيا المعلومات - الموقع الرسمي\","` | — |
| [SRC-01E35ABC46-L000242](../../tests/test_research_guardrails.py#L242) | 242 | `"        ),"` | — |
| [SRC-01E35ABC46-L000243](../../tests/test_research_guardrails.py#L243) | 243 | `"    ]"` | — |
| [SRC-01E35ABC46-L000244](../../tests/test_research_guardrails.py#L244) | 244 | `""` | — |
| [SRC-01E35ABC46-L000245](../../tests/test_research_guardrails.py#L245) | 245 | `"    accepted, report = apply_source_guardrails("` | — |
| [SRC-01E35ABC46-L000246](../../tests/test_research_guardrails.py#L246) | 246 | `"        question, \"auto\", {\"freshness\": \"any\"}, candidates, now=_GUARDRAIL_NOW"` | — |
| [SRC-01E35ABC46-L000247](../../tests/test_research_guardrails.py#L247) | 247 | `"    )"` | — |
| [SRC-01E35ABC46-L000248](../../tests/test_research_guardrails.py#L248) | 248 | `""` | — |
| [SRC-01E35ABC46-L000249](../../tests/test_research_guardrails.py#L249) | 249 | `"    assert [item[\"url\"] for item in accepted] == [\"https://mcit.gov.eg/\"]"` | — |
| [SRC-01E35ABC46-L000250](../../tests/test_research_guardrails.py#L250) | 250 | `"    assert report[\"official_government_domain_required\"] is True"` | — |
| [SRC-01E35ABC46-L000251](../../tests/test_research_guardrails.py#L251) | 251 | `"    assert report[\"rejection_counts\"] == {\"not_an_official_government_domain\": 1}"` | — |
| [SRC-01E35ABC46-L000252](../../tests/test_research_guardrails.py#L252) | 252 | `"    assert \"not independently verified\" in report[\"official_domain_policy\"]"` | — |
| [SRC-01E35ABC46-L000253](../../tests/test_research_guardrails.py#L253) | 253 | `""` | — |
| [SRC-01E35ABC46-L000254](../../tests/test_research_guardrails.py#L254) | 254 | `""` | — |
| [SRC-01E35ABC46-L000255](../../tests/test_research_guardrails.py#L255) | 255 | `"def test_official_request_fails_closed_when_only_non_government_result_exists() -> None:"` | — |
| [SRC-01E35ABC46-L000256](../../tests/test_research_guardrails.py#L256) | 256 | `"    accepted, report = apply_source_guardrails("` | — |
| [SRC-01E35ABC46-L000257](../../tests/test_research_guardrails.py#L257) | 257 | `"        \"الموقع الرسمي لوزارة الاتصالات المصرية\","` | — |
| [SRC-01E35ABC46-L000258](../../tests/test_research_guardrails.py#L258) | 258 | `"        \"auto\","` | — |
| [SRC-01E35ABC46-L000259](../../tests/test_research_guardrails.py#L259) | 259 | `"        {\"freshness\": \"any\"},"` | — |
| [SRC-01E35ABC46-L000260](../../tests/test_research_guardrails.py#L260) | 260 | `"        [_guardrail_source(\"https://visitegypt.com/\")],"` | — |
| [SRC-01E35ABC46-L000261](../../tests/test_research_guardrails.py#L261) | 261 | `"        now=_GUARDRAIL_NOW,"` | — |
| [SRC-01E35ABC46-L000262](../../tests/test_research_guardrails.py#L262) | 262 | `"    )"` | — |
| [SRC-01E35ABC46-L000263](../../tests/test_research_guardrails.py#L263) | 263 | `""` | — |
| [SRC-01E35ABC46-L000264](../../tests/test_research_guardrails.py#L264) | 264 | `"    assert accepted == []"` | — |
| [SRC-01E35ABC46-L000265](../../tests/test_research_guardrails.py#L265) | 265 | `"    assert report[\"accepted_sources\"] == 0"` | — |
| [SRC-01E35ABC46-L000266](../../tests/test_research_guardrails.py#L266) | 266 | `"    assert report[\"current_evidence_status\"] == \"not_required\""` | — |
| [SRC-01E35ABC46-L000267](../../tests/test_research_guardrails.py#L267) | 267 | `""` | — |
| [SRC-01E35ABC46-L000268](../../tests/test_research_guardrails.py#L268) | 268 | `""` | — |
| [SRC-01E35ABC46-L000269](../../tests/test_research_guardrails.py#L269) | 269 | `"def test_current_evidence_requires_recent_date_and_readable_page() -> None:"` | — |
| [SRC-01E35ABC46-L000270](../../tests/test_research_guardrails.py#L270) | 270 | `"    recent = _guardrail_source(\"https://example.com/current\")"` | — |
| [SRC-01E35ABC46-L000271](../../tests/test_research_guardrails.py#L271) | 271 | `"    stale = _guardrail_source("` | — |
| [SRC-01E35ABC46-L000272](../../tests/test_research_guardrails.py#L272) | 272 | `"        \"https://example.org/old\", published_at=\"2024-06-01T10:00:00Z\""` | — |
| [SRC-01E35ABC46-L000273](../../tests/test_research_guardrails.py#L273) | 273 | `"    )"` | — |
| [SRC-01E35ABC46-L000274](../../tests/test_research_guardrails.py#L274) | 274 | `"    undated = _guardrail_source(\"https://example.net/undated\", published_at=\"\")"` | — |
| [SRC-01E35ABC46-L000275](../../tests/test_research_guardrails.py#L275) | 275 | `"    unread = _guardrail_source("` | — |
| [SRC-01E35ABC46-L000276](../../tests/test_research_guardrails.py#L276) | 276 | `"        \"https://example.edu/unread\", page_fetched=False, page_text=\"\""` | — |
| [SRC-01E35ABC46-L000277](../../tests/test_research_guardrails.py#L277) | 277 | `"    )"` | — |
| [SRC-01E35ABC46-L000278](../../tests/test_research_guardrails.py#L278) | 278 | `""` | — |
| [SRC-01E35ABC46-L000279](../../tests/test_research_guardrails.py#L279) | 279 | `"    assert assess_current_source(recent, now=_GUARDRAIL_NOW)[\"eligible\"] is True"` | — |
| [SRC-01E35ABC46-L000280](../../tests/test_research_guardrails.py#L280) | 280 | `"    assert assess_current_source(stale, now=_GUARDRAIL_NOW)[\"status\"] == \"stale\""` | — |
| [SRC-01E35ABC46-L000281](../../tests/test_research_guardrails.py#L281) | 281 | `"    assert assess_current_source(undated, now=_GUARDRAIL_NOW)[\"status\"] == \"date_unavailable\""` | — |
| [SRC-01E35ABC46-L000282](../../tests/test_research_guardrails.py#L282) | 282 | `"    assert assess_current_source(unread, now=_GUARDRAIL_NOW)[\"status\"] == \"page_not_read\""` | — |
| [SRC-01E35ABC46-L000283](../../tests/test_research_guardrails.py#L283) | 283 | `""` | — |
| [SRC-01E35ABC46-L000284](../../tests/test_research_guardrails.py#L284) | 284 | `""` | — |
| [SRC-01E35ABC46-L000285](../../tests/test_research_guardrails.py#L285) | 285 | `"def test_latest_mode_excludes_old_undated_and_unread_pages() -> None:"` | — |
| [SRC-01E35ABC46-L000286](../../tests/test_research_guardrails.py#L286) | 286 | `"    candidates = ["` | — |
| [SRC-01E35ABC46-L000287](../../tests/test_research_guardrails.py#L287) | 287 | `"        _guardrail_source(\"https://example.com/recent\"),"` | — |
| [SRC-01E35ABC46-L000288](../../tests/test_research_guardrails.py#L288) | 288 | `"        _guardrail_source("` | — |
| [SRC-01E35ABC46-L000289](../../tests/test_research_guardrails.py#L289) | 289 | `"            \"https://example.org/old\", published_at=\"2023-11-15T10:00:00Z\""` | — |
| [SRC-01E35ABC46-L000290](../../tests/test_research_guardrails.py#L290) | 290 | `"        ),"` | — |
| [SRC-01E35ABC46-L000291](../../tests/test_research_guardrails.py#L291) | 291 | `"        _guardrail_source(\"https://example.net/undated\", published_at=\"\"),"` | — |
| [SRC-01E35ABC46-L000292](../../tests/test_research_guardrails.py#L292) | 292 | `"        _guardrail_source("` | — |
| [SRC-01E35ABC46-L000293](../../tests/test_research_guardrails.py#L293) | 293 | `"            \"https://example.edu/unread\", page_fetched=False, page_text=\"\""` | — |
| [SRC-01E35ABC46-L000294](../../tests/test_research_guardrails.py#L294) | 294 | `"        ),"` | — |
| [SRC-01E35ABC46-L000295](../../tests/test_research_guardrails.py#L295) | 295 | `"    ]"` | — |
| [SRC-01E35ABC46-L000296](../../tests/test_research_guardrails.py#L296) | 296 | `"    accepted, report = apply_source_guardrails("` | — |
| [SRC-01E35ABC46-L000297](../../tests/test_research_guardrails.py#L297) | 297 | `"        \"مواعيد عمل مكتب الجوازات اليوم\","` | — |
| [SRC-01E35ABC46-L000298](../../tests/test_research_guardrails.py#L298) | 298 | `"        \"latest\","` | — |
| [SRC-01E35ABC46-L000299](../../tests/test_research_guardrails.py#L299) | 299 | `"        {\"freshness\": \"current\"},"` | — |
| [SRC-01E35ABC46-L000300](../../tests/test_research_guardrails.py#L300) | 300 | `"        candidates,"` | — |
| [SRC-01E35ABC46-L000301](../../tests/test_research_guardrails.py#L301) | 301 | `"        now=_GUARDRAIL_NOW,"` | — |
| [SRC-01E35ABC46-L000302](../../tests/test_research_guardrails.py#L302) | 302 | `"    )"` | — |
| [SRC-01E35ABC46-L000303](../../tests/test_research_guardrails.py#L303) | 303 | `""` | — |
| [SRC-01E35ABC46-L000304](../../tests/test_research_guardrails.py#L304) | 304 | `"    assert [item[\"url\"] for item in accepted] == [\"https://example.com/recent\"]"` | — |
| [SRC-01E35ABC46-L000305](../../tests/test_research_guardrails.py#L305) | 305 | `"    assert report[\"current_evidence_required\"] is True"` | — |
| [SRC-01E35ABC46-L000306](../../tests/test_research_guardrails.py#L306) | 306 | `"    assert report[\"current_evidence_status\"] == \"eligible_recent_read_pages_only\""` | — |
| [SRC-01E35ABC46-L000307](../../tests/test_research_guardrails.py#L307) | 307 | `"    assert report[\"rejection_counts\"] == {"` | — |
| [SRC-01E35ABC46-L000308](../../tests/test_research_guardrails.py#L308) | 308 | `"        \"stale\": 1,"` | — |
| [SRC-01E35ABC46-L000309](../../tests/test_research_guardrails.py#L309) | 309 | `"        \"date_unavailable\": 1,"` | — |
| [SRC-01E35ABC46-L000310](../../tests/test_research_guardrails.py#L310) | 310 | `"        \"page_not_read\": 1,"` | — |
| [SRC-01E35ABC46-L000311](../../tests/test_research_guardrails.py#L311) | 311 | `"    }"` | — |
| [SRC-01E35ABC46-L000312](../../tests/test_research_guardrails.py#L312) | 312 | `""` | — |
| [SRC-01E35ABC46-L000313](../../tests/test_research_guardrails.py#L313) | 313 | `""` | — |
| [SRC-01E35ABC46-L000314](../../tests/test_research_guardrails.py#L314) | 314 | `"def test_official_site_navigation_does_not_require_news_publication_date() -> None:"` | — |
| [SRC-01E35ABC46-L000315](../../tests/test_research_guardrails.py#L315) | 315 | `"    question = \"ابحث عن الموقع الرسمي لوزارة الاتصالات وتكنولوجيا المعلومات المصرية\""` | — |
| [SRC-01E35ABC46-L000316](../../tests/test_research_guardrails.py#L316) | 316 | `"    official_page = _guardrail_source("` | — |
| [SRC-01E35ABC46-L000317](../../tests/test_research_guardrails.py#L317) | 317 | `"        \"https://mcit.gov.eg/\","` | — |
| [SRC-01E35ABC46-L000318](../../tests/test_research_guardrails.py#L318) | 318 | `"        published_at=\"\","` | — |
| [SRC-01E35ABC46-L000319](../../tests/test_research_guardrails.py#L319) | 319 | `"        title=\"وزارة الاتصالات وتكنولوجيا المعلومات - الموقع الرسمي\","` | — |
| [SRC-01E35ABC46-L000320](../../tests/test_research_guardrails.py#L320) | 320 | `"    )"` | — |
| [SRC-01E35ABC46-L000321](../../tests/test_research_guardrails.py#L321) | 321 | `""` | — |
| [SRC-01E35ABC46-L000322](../../tests/test_research_guardrails.py#L322) | 322 | `"    accepted, report = apply_source_guardrails("` | — |
| [SRC-01E35ABC46-L000323](../../tests/test_research_guardrails.py#L323) | 323 | `"        question,"` | — |
| [SRC-01E35ABC46-L000324](../../tests/test_research_guardrails.py#L324) | 324 | `"        \"latest\","` | — |
| [SRC-01E35ABC46-L000325](../../tests/test_research_guardrails.py#L325) | 325 | `"        {\"freshness\": \"current\"},"` | — |
| [SRC-01E35ABC46-L000326](../../tests/test_research_guardrails.py#L326) | 326 | `"        [official_page],"` | — |
| [SRC-01E35ABC46-L000327](../../tests/test_research_guardrails.py#L327) | 327 | `"        now=_GUARDRAIL_NOW,"` | — |
| [SRC-01E35ABC46-L000328](../../tests/test_research_guardrails.py#L328) | 328 | `"    )"` | — |
| [SRC-01E35ABC46-L000329](../../tests/test_research_guardrails.py#L329) | 329 | `""` | — |
| [SRC-01E35ABC46-L000330](../../tests/test_research_guardrails.py#L330) | 330 | `"    assert len(accepted) == 1"` | — |
| [SRC-01E35ABC46-L000331](../../tests/test_research_guardrails.py#L331) | 331 | `"    assert report[\"current_evidence_required\"] is False"` | — |
| [SRC-01E35ABC46-L000332](../../tests/test_research_guardrails.py#L332) | 332 | `""` | — |
| [SRC-01E35ABC46-L000333](../../tests/test_research_guardrails.py#L333) | 333 | `""` | — |
| [SRC-01E35ABC46-L000334](../../tests/test_research_guardrails.py#L334) | 334 | `"def test_social_mode_rejects_non_social_sources_and_classifies_public_posts() -> None:"` | — |
| [SRC-01E35ABC46-L000335](../../tests/test_research_guardrails.py#L335) | 335 | `"    question = \"اجمع آراء وتجارب الناس حول نيسان صني 2022 في مصر\""` | — |
| [SRC-01E35ABC46-L000336](../../tests/test_research_guardrails.py#L336) | 336 | `"    personal_post = _guardrail_source("` | — |
| [SRC-01E35ABC46-L000337](../../tests/test_research_guardrails.py#L337) | 337 | `"        \"https://www.reddit.com/r/cars/comments/example\","` | — |
| [SRC-01E35ABC46-L000338](../../tests/test_research_guardrails.py#L338) | 338 | `"        title=\"تجربتي مع نيسان صني\","` | — |
| [SRC-01E35ABC46-L000339](../../tests/test_research_guardrails.py#L339) | 339 | `"        snippet=\"أنا امتلك السيارة واستخدمتها يوميًا لمدة عام\","` | — |
| [SRC-01E35ABC46-L000340](../../tests/test_research_guardrails.py#L340) | 340 | `"    )"` | — |
| [SRC-01E35ABC46-L000341](../../tests/test_research_guardrails.py#L341) | 341 | `"    promotional_post = _guardrail_source("` | — |
| [SRC-01E35ABC46-L000342](../../tests/test_research_guardrails.py#L342) | 342 | `"        \"https://www.reddit.com/r/cars/comments/ad\","` | — |
| [SRC-01E35ABC46-L000343](../../tests/test_research_guardrails.py#L343) | 343 | `"        title=\"نيسان صني 2022 للبيع\","` | — |
| [SRC-01E35ABC46-L000344](../../tests/test_research_guardrails.py#L344) | 344 | `"        snippet=\"سعر خاص، تواصل معنا عبر واتساب\","` | — |
| [SRC-01E35ABC46-L000345](../../tests/test_research_guardrails.py#L345) | 345 | `"    )"` | — |
| [SRC-01E35ABC46-L000346](../../tests/test_research_guardrails.py#L346) | 346 | `"    editorial_review = _guardrail_source("` | — |
| [SRC-01E35ABC46-L000347](../../tests/test_research_guardrails.py#L347) | 347 | `"        \"https://example.com/car-review\","` | — |
| [SRC-01E35ABC46-L000348](../../tests/test_research_guardrails.py#L348) | 348 | `"        title=\"مراجعة نيسان صني\","` | — |
| [SRC-01E35ABC46-L000349](../../tests/test_research_guardrails.py#L349) | 349 | `"    )"` | — |
| [SRC-01E35ABC46-L000350](../../tests/test_research_guardrails.py#L350) | 350 | `""` | — |
| [SRC-01E35ABC46-L000351](../../tests/test_research_guardrails.py#L351) | 351 | `"    accepted, report = apply_source_guardrails("` | — |
| [SRC-01E35ABC46-L000352](../../tests/test_research_guardrails.py#L352) | 352 | `"        question,"` | — |
| [SRC-01E35ABC46-L000353](../../tests/test_research_guardrails.py#L353) | 353 | `"        \"social\","` | — |
| [SRC-01E35ABC46-L000354](../../tests/test_research_guardrails.py#L354) | 354 | `"        {\"social_focus\": True, \"freshness\": \"any\"},"` | — |
| [SRC-01E35ABC46-L000355](../../tests/test_research_guardrails.py#L355) | 355 | `"        [personal_post, promotional_post, editorial_review],"` | — |
| [SRC-01E35ABC46-L000356](../../tests/test_research_guardrails.py#L356) | 356 | `"        now=_GUARDRAIL_NOW,"` | — |
| [SRC-01E35ABC46-L000357](../../tests/test_research_guardrails.py#L357) | 357 | `"    )"` | — |
| [SRC-01E35ABC46-L000358](../../tests/test_research_guardrails.py#L358) | 358 | `""` | — |
| [SRC-01E35ABC46-L000359](../../tests/test_research_guardrails.py#L359) | 359 | `"    labels = {item[\"url\"]: item[\"opinion_source_classification\"] for item in accepted}"` | — |
| [SRC-01E35ABC46-L000360](../../tests/test_research_guardrails.py#L360) | 360 | `"    assert labels[personal_post[\"url\"]] == \"personal_experience_candidate\""` | — |
| [SRC-01E35ABC46-L000361](../../tests/test_research_guardrails.py#L361) | 361 | `"    assert labels[promotional_post[\"url\"]] == \"promotional_or_commercial\""` | — |
| [SRC-01E35ABC46-L000362](../../tests/test_research_guardrails.py#L362) | 362 | `"    assert editorial_review[\"url\"] not in labels"` | — |
| [SRC-01E35ABC46-L000363](../../tests/test_research_guardrails.py#L363) | 363 | `"    assert report[\"social_platform_only\"] is True"` | — |
| [SRC-01E35ABC46-L000364](../../tests/test_research_guardrails.py#L364) | 364 | `"    assert report[\"rejection_counts\"] == {\"not_a_social_platform_source\": 1}"` | — |
| [SRC-01E35ABC46-L000365](../../tests/test_research_guardrails.py#L365) | 365 | `"    assert all("` | — |
| [SRC-01E35ABC46-L000366](../../tests/test_research_guardrails.py#L366) | 366 | `"        item[\"opinion_classification_method\"] == \"heuristic_only\""` | — |
| [SRC-01E35ABC46-L000367](../../tests/test_research_guardrails.py#L367) | 367 | `"        for item in accepted"` | — |
| [SRC-01E35ABC46-L000368](../../tests/test_research_guardrails.py#L368) | 368 | `"    )"` | — |
| [SRC-01E35ABC46-L000369](../../tests/test_research_guardrails.py#L369) | 369 | `""` | — |
| [SRC-01E35ABC46-L000370](../../tests/test_research_guardrails.py#L370) | 370 | `""` | — |
| [SRC-01E35ABC46-L000371](../../tests/test_research_guardrails.py#L371) | 371 | `"def test_social_classification_does_not_claim_unknown_post_is_verified_experience() -> None:"` | — |
| [SRC-01E35ABC46-L000372](../../tests/test_research_guardrails.py#L372) | 372 | `"    result = classify_social_source("` | — |
| [SRC-01E35ABC46-L000373](../../tests/test_research_guardrails.py#L373) | 373 | `"        _guardrail_source("` | — |
| [SRC-01E35ABC46-L000374](../../tests/test_research_guardrails.py#L374) | 374 | `"            \"https://www.youtube.com/watch?v=example\","` | — |
| [SRC-01E35ABC46-L000375](../../tests/test_research_guardrails.py#L375) | 375 | `"            title=\"Nissan Sunny 2022\","` | — |
| [SRC-01E35ABC46-L000376](../../tests/test_research_guardrails.py#L376) | 376 | `"            snippet=\"معلومات ومقاطع عن السيارة\","` | — |
| [SRC-01E35ABC46-L000377](../../tests/test_research_guardrails.py#L377) | 377 | `"        )"` | — |
| [SRC-01E35ABC46-L000378](../../tests/test_research_guardrails.py#L378) | 378 | `"    )"` | — |
| [SRC-01E35ABC46-L000379](../../tests/test_research_guardrails.py#L379) | 379 | `""` | — |
| [SRC-01E35ABC46-L000380](../../tests/test_research_guardrails.py#L380) | 380 | `"    assert result[\"opinion_source_classification\"] == \"social_post_unclassified\""` | — |
| [SRC-01E35ABC46-L000381](../../tests/test_research_guardrails.py#L381) | 381 | `"    assert result[\"opinion_classification_method\"] == \"heuristic_only\""` | — |
| [SRC-01E35ABC46-L000382](../../tests/test_research_guardrails.py#L382) | 382 | `"    assert \"manual review\" in result[\"opinion_classification_basis\"]"` | — |
| [SRC-01E35ABC46-L000383](../../tests/test_research_guardrails.py#L383) | 383 | `""` | — |
| [SRC-01E35ABC46-L000384](../../tests/test_research_guardrails.py#L384) | 384 | `""` | — |
| [SRC-01E35ABC46-L000385](../../tests/test_research_guardrails.py#L385) | 385 | `"def test_today_query_requires_current_evidence_even_in_auto_mode() -> None:"` | — |
| [SRC-01E35ABC46-L000386](../../tests/test_research_guardrails.py#L386) | 386 | `"    accepted, report = apply_source_guardrails("` | — |
| [SRC-01E35ABC46-L000387](../../tests/test_research_guardrails.py#L387) | 387 | `"        \"ما مواعيد العمل اليوم؟\","` | — |
| [SRC-01E35ABC46-L000388](../../tests/test_research_guardrails.py#L388) | 388 | `"        \"auto\","` | — |
| [SRC-01E35ABC46-L000389](../../tests/test_research_guardrails.py#L389) | 389 | `"        {\"freshness\": \"current\"},"` | — |
| [SRC-01E35ABC46-L000390](../../tests/test_research_guardrails.py#L390) | 390 | `"        ["` | — |
| [SRC-01E35ABC46-L000391](../../tests/test_research_guardrails.py#L391) | 391 | `"            _guardrail_source("` | — |
| [SRC-01E35ABC46-L000392](../../tests/test_research_guardrails.py#L392) | 392 | `"                \"https://example.com/old\", published_at=\"2024-01-01T10:00:00Z\""` | — |
| [SRC-01E35ABC46-L000393](../../tests/test_research_guardrails.py#L393) | 393 | `"            )"` | — |
| [SRC-01E35ABC46-L000394](../../tests/test_research_guardrails.py#L394) | 394 | `"        ],"` | — |
| [SRC-01E35ABC46-L000395](../../tests/test_research_guardrails.py#L395) | 395 | `"        now=_GUARDRAIL_NOW,"` | — |
| [SRC-01E35ABC46-L000396](../../tests/test_research_guardrails.py#L396) | 396 | `"    )"` | — |
| [SRC-01E35ABC46-L000397](../../tests/test_research_guardrails.py#L397) | 397 | `""` | — |
| [SRC-01E35ABC46-L000398](../../tests/test_research_guardrails.py#L398) | 398 | `"    assert accepted == []"` | — |
| [SRC-01E35ABC46-L000399](../../tests/test_research_guardrails.py#L399) | 399 | `"    assert report[\"current_evidence_required\"] is True"` | — |
| [SRC-01E35ABC46-L000400](../../tests/test_research_guardrails.py#L400) | 400 | `"    assert report[\"rejection_counts\"] == {\"stale\": 1}"` | — |
| [SRC-01E35ABC46-L000401](../../tests/test_research_guardrails.py#L401) | 401 | `""` | — |
| [SRC-01E35ABC46-L000402](../../tests/test_research_guardrails.py#L402) | 402 | `""` | — |
| [SRC-01E35ABC46-L000403](../../tests/test_research_guardrails.py#L403) | 403 | `"def test_recent_source_date_is_not_enough_without_readable_page_text() -> None:"` | — |
| [SRC-01E35ABC46-L000404](../../tests/test_research_guardrails.py#L404) | 404 | `"    item = _guardrail_source("` | — |
| [SRC-01E35ABC46-L000405](../../tests/test_research_guardrails.py#L405) | 405 | `"        \"https://example.com/unread\","` | — |
| [SRC-01E35ABC46-L000406](../../tests/test_research_guardrails.py#L406) | 406 | `"        published_at=\"2026-10-27T10:00:00Z\","` | — |
| [SRC-01E35ABC46-L000407](../../tests/test_research_guardrails.py#L407) | 407 | `"        page_fetched=True,"` | — |
| [SRC-01E35ABC46-L000408](../../tests/test_research_guardrails.py#L408) | 408 | `"        page_text=\"   \","` | — |
| [SRC-01E35ABC46-L000409](../../tests/test_research_guardrails.py#L409) | 409 | `"    )"` | — |
| [SRC-01E35ABC46-L000410](../../tests/test_research_guardrails.py#L410) | 410 | `"    assert assess_current_source(item, now=_GUARDRAIL_NOW)[\"status\"] == \"page_not_read\""` | — |
| [SRC-01E35ABC46-L000411](../../tests/test_research_guardrails.py#L411) | 411 | `""` | — |
| [SRC-01E35ABC46-L000412](../../tests/test_research_guardrails.py#L412) | 412 | `""` | — |
| [SRC-01E35ABC46-L000413](../../tests/test_research_guardrails.py#L413) | 413 | `""` | — |
| [SRC-01E35ABC46-L000414](../../tests/test_research_guardrails.py#L414) | 414 | `"def test_social_classification_matches_english_first_person_phrases_case_insensitively() -> None:"` | — |
| [SRC-01E35ABC46-L000415](../../tests/test_research_guardrails.py#L415) | 415 | `"    result = classify_social_source("` | — |
| [SRC-01E35ABC46-L000416](../../tests/test_research_guardrails.py#L416) | 416 | `"        _guardrail_source("` | — |
| [SRC-01E35ABC46-L000417](../../tests/test_research_guardrails.py#L417) | 417 | `"            \"https://www.reddit.com/r/cars/comments/owner\","` | — |
| [SRC-01E35ABC46-L000418](../../tests/test_research_guardrails.py#L418) | 418 | `"            title=\"Nissan Sunny ownership\","` | — |
| [SRC-01E35ABC46-L000419](../../tests/test_research_guardrails.py#L419) | 419 | `"            snippet=\"I OWN the car and I use it for my daily commute\","` | — |
| [SRC-01E35ABC46-L000420](../../tests/test_research_guardrails.py#L420) | 420 | `"        )"` | — |
| [SRC-01E35ABC46-L000421](../../tests/test_research_guardrails.py#L421) | 421 | `"    )"` | — |
| [SRC-01E35ABC46-L000422](../../tests/test_research_guardrails.py#L422) | 422 | `""` | — |
| [SRC-01E35ABC46-L000423](../../tests/test_research_guardrails.py#L423) | 423 | `"    assert result[\"opinion_source_classification\"] == \"personal_experience_candidate\""` | — |
| [SRC-01E35ABC46-L000424](../../tests/test_research_guardrails.py#L424) | 424 | `""` | — |
| [SRC-01E35ABC46-L000425](../../tests/test_research_guardrails.py#L425) | 425 | `""` | — |
| [SRC-01E35ABC46-L000426](../../tests/test_research_guardrails.py#L426) | 426 | `"def test_official_domain_check_rejects_suffix_spoofing() -> None:"` | — |
| [SRC-01E35ABC46-L000427](../../tests/test_research_guardrails.py#L427) | 427 | `"    question = \"ابحث عن الموقع الرسمي لوزارة الاتصالات المصرية\""` | — |
| [SRC-01E35ABC46-L000428](../../tests/test_research_guardrails.py#L428) | 428 | `"    accepted, report = apply_source_guardrails("` | — |
| [SRC-01E35ABC46-L000429](../../tests/test_research_guardrails.py#L429) | 429 | `"        question,"` | — |
| [SRC-01E35ABC46-L000430](../../tests/test_research_guardrails.py#L430) | 430 | `"        \"auto\","` | — |
| [SRC-01E35ABC46-L000431](../../tests/test_research_guardrails.py#L431) | 431 | `"        {\"freshness\": \"any\"},"` | — |
| [SRC-01E35ABC46-L000432](../../tests/test_research_guardrails.py#L432) | 432 | `"        ["` | — |
| [SRC-01E35ABC46-L000433](../../tests/test_research_guardrails.py#L433) | 433 | `"            _guardrail_source("` | — |
| [SRC-01E35ABC46-L000434](../../tests/test_research_guardrails.py#L434) | 434 | `"                \"https://mcit.gov.eg.attacker.example/\","` | — |
| [SRC-01E35ABC46-L000435](../../tests/test_research_guardrails.py#L435) | 435 | `"                title=\"وزارة الاتصالات المصرية الموقع الرسمي\","` | — |
| [SRC-01E35ABC46-L000436](../../tests/test_research_guardrails.py#L436) | 436 | `"            )"` | — |
| [SRC-01E35ABC46-L000437](../../tests/test_research_guardrails.py#L437) | 437 | `"        ],"` | — |
| [SRC-01E35ABC46-L000438](../../tests/test_research_guardrails.py#L438) | 438 | `"        now=_GUARDRAIL_NOW,"` | — |
| [SRC-01E35ABC46-L000439](../../tests/test_research_guardrails.py#L439) | 439 | `"    )"` | — |
| [SRC-01E35ABC46-L000440](../../tests/test_research_guardrails.py#L440) | 440 | `""` | — |
| [SRC-01E35ABC46-L000441](../../tests/test_research_guardrails.py#L441) | 441 | `"    assert accepted == []"` | — |
| [SRC-01E35ABC46-L000442](../../tests/test_research_guardrails.py#L442) | 442 | `"    assert report[\"rejection_counts\"] == {\"not_an_official_government_domain\": 1}"` | — |
## اختبارات

### FILE-2614DCB6FB — [tests/test_search_code.py](../../tests/test_search_code.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2614DCB6FB-L000001](../../tests/test_search_code.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-2614DCB6FB-L000002](../../tests/test_search_code.py#L2) | 2 | `""` | — |
| [SRC-2614DCB6FB-L000003](../../tests/test_search_code.py#L3) | 3 | `"import importlib.util"` | — |
| [SRC-2614DCB6FB-L000004](../../tests/test_search_code.py#L4) | 4 | `"import re"` | — |
| [SRC-2614DCB6FB-L000005](../../tests/test_search_code.py#L5) | 5 | `"import sys"` | — |
| [SRC-2614DCB6FB-L000006](../../tests/test_search_code.py#L6) | 6 | `"from pathlib import Path"` | — |
| [SRC-2614DCB6FB-L000007](../../tests/test_search_code.py#L7) | 7 | `""` | — |
| [SRC-2614DCB6FB-L000008](../../tests/test_search_code.py#L8) | 8 | `"SEARCH_PATH = Path(__file__).resolve().parents[1] / \"docs\" / \"search_code.py\""` | — |
| [SRC-2614DCB6FB-L000009](../../tests/test_search_code.py#L9) | 9 | `"SEARCH_SPEC = importlib.util.spec_from_file_location(\"omarai_search_code_for_tests\", SEARCH_PATH)"` | — |
| [SRC-2614DCB6FB-L000010](../../tests/test_search_code.py#L10) | 10 | `"assert SEARCH_SPEC is not None"` | — |
| [SRC-2614DCB6FB-L000011](../../tests/test_search_code.py#L11) | 11 | `"assert SEARCH_SPEC.loader is not None"` | — |
| [SRC-2614DCB6FB-L000012](../../tests/test_search_code.py#L12) | 12 | `"SEARCH = importlib.util.module_from_spec(SEARCH_SPEC)"` | — |
| [SRC-2614DCB6FB-L000013](../../tests/test_search_code.py#L13) | 13 | `"sys.modules[SEARCH_SPEC.name] = SEARCH"` | — |
| [SRC-2614DCB6FB-L000014](../../tests/test_search_code.py#L14) | 14 | `"SEARCH_SPEC.loader.exec_module(SEARCH)"` | — |
| [SRC-2614DCB6FB-L000015](../../tests/test_search_code.py#L15) | 15 | `""` | — |
| [SRC-2614DCB6FB-L000016](../../tests/test_search_code.py#L16) | 16 | `""` | — |
| [SRC-2614DCB6FB-L000017](../../tests/test_search_code.py#L17) | 17 | `"def test_search_returns_stable_file_line_and_source_link(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000018](../../tests/test_search_code.py#L18) | 18 | `"    \"\"\"Text search returns the exact file and 1-based line without network access.\"\"\""` | — |
| [SRC-2614DCB6FB-L000019](../../tests/test_search_code.py#L19) | 19 | `"    source = tmp_path / \"app.py\""` | — |
| [SRC-2614DCB6FB-L000020](../../tests/test_search_code.py#L20) | 20 | `"    source.write_text(\"first = 1\\nneedle = 2\\nlast = 3\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000021](../../tests/test_search_code.py#L21) | 21 | `""` | — |
| [SRC-2614DCB6FB-L000022](../../tests/test_search_code.py#L22) | 22 | `"    hits = SEARCH.search_repository(tmp_path, \"needle\")"` | — |
| [SRC-2614DCB6FB-L000023](../../tests/test_search_code.py#L23) | 23 | `""` | — |
| [SRC-2614DCB6FB-L000024](../../tests/test_search_code.py#L24) | 24 | `"    assert len(hits) == 1"` | — |
| [SRC-2614DCB6FB-L000025](../../tests/test_search_code.py#L25) | 25 | `"    assert hits[0].file == \"app.py\""` | — |
| [SRC-2614DCB6FB-L000026](../../tests/test_search_code.py#L26) | 26 | `"    assert hits[0].line == 2"` | — |
| [SRC-2614DCB6FB-L000027](../../tests/test_search_code.py#L27) | 27 | `"    assert \"needle = 2\" in hits[0].text"` | — |
| [SRC-2614DCB6FB-L000028](../../tests/test_search_code.py#L28) | 28 | `"    assert hits[0].link.endswith(\"/app.py#L2\")"` | — |
| [SRC-2614DCB6FB-L000029](../../tests/test_search_code.py#L29) | 29 | `""` | — |
| [SRC-2614DCB6FB-L000030](../../tests/test_search_code.py#L30) | 30 | `""` | — |
| [SRC-2614DCB6FB-L000031](../../tests/test_search_code.py#L31) | 31 | `"def test_search_supports_multiline_context_and_regex(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000032](../../tests/test_search_code.py#L32) | 32 | `"    \"\"\"The context argument returns the requested number of adjacent lines.\"\"\""` | — |
| [SRC-2614DCB6FB-L000033](../../tests/test_search_code.py#L33) | 33 | `"    source = tmp_path / \"app.py\""` | — |
| [SRC-2614DCB6FB-L000034](../../tests/test_search_code.py#L34) | 34 | `"    source.write_text(\"before one\\nbefore two\\nVALUE_42 = 7\\nafter one\\nafter two\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000035](../../tests/test_search_code.py#L35) | 35 | `""` | — |
| [SRC-2614DCB6FB-L000036](../../tests/test_search_code.py#L36) | 36 | `"    hits = SEARCH.search_repository("` | — |
| [SRC-2614DCB6FB-L000037](../../tests/test_search_code.py#L37) | 37 | `"        tmp_path, r\"VALUE_\\d+\", use_regex=True, context=2"` | — |
| [SRC-2614DCB6FB-L000038](../../tests/test_search_code.py#L38) | 38 | `"    )"` | — |
| [SRC-2614DCB6FB-L000039](../../tests/test_search_code.py#L39) | 39 | `""` | — |
| [SRC-2614DCB6FB-L000040](../../tests/test_search_code.py#L40) | 40 | `"    assert len(hits) == 1"` | — |
| [SRC-2614DCB6FB-L000041](../../tests/test_search_code.py#L41) | 41 | `"    assert hits[0].context_before.splitlines() == [\"before one\", \"before two\"]"` | — |
| [SRC-2614DCB6FB-L000042](../../tests/test_search_code.py#L42) | 42 | `"    assert hits[0].context_after.splitlines() == [\"after one\", \"after two\"]"` | — |
| [SRC-2614DCB6FB-L000043](../../tests/test_search_code.py#L43) | 43 | `""` | — |
| [SRC-2614DCB6FB-L000044](../../tests/test_search_code.py#L44) | 44 | `""` | — |
| [SRC-2614DCB6FB-L000045](../../tests/test_search_code.py#L45) | 45 | `"def test_search_excludes_common_secret_files_and_runtime_directories(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000046](../../tests/test_search_code.py#L46) | 46 | `"    \"\"\"Local searches skip common secret paths and binary/runtime data.\"\"\""` | — |
| [SRC-2614DCB6FB-L000047](../../tests/test_search_code.py#L47) | 47 | `"    (tmp_path / \"app.py\").write_text(\"safe_value = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000048](../../tests/test_search_code.py#L48) | 48 | `"    (tmp_path / \".env\").write_text(\"TOKEN=private-value\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000049](../../tests/test_search_code.py#L49) | 49 | `"    (tmp_path / \"credentials.json\").write_text('{\"token\":\"private-value\"}\\n', encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000050](../../tests/test_search_code.py#L50) | 50 | `"    aws_dir = tmp_path / \".aws\""` | — |
| [SRC-2614DCB6FB-L000051](../../tests/test_search_code.py#L51) | 51 | `"    aws_dir.mkdir()"` | — |
| [SRC-2614DCB6FB-L000052](../../tests/test_search_code.py#L52) | 52 | `"    (aws_dir / \"credentials\").write_text(\"token=private-value\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000053](../../tests/test_search_code.py#L53) | 53 | `"    data_dir = tmp_path / \"data\""` | — |
| [SRC-2614DCB6FB-L000054](../../tests/test_search_code.py#L54) | 54 | `"    data_dir.mkdir()"` | — |
| [SRC-2614DCB6FB-L000055](../../tests/test_search_code.py#L55) | 55 | `"    (data_dir / \"records.sqlite3\").write_bytes(b\"database-token\")"` | — |
| [SRC-2614DCB6FB-L000056](../../tests/test_search_code.py#L56) | 56 | `"    (tmp_path / \"credentials.example\").write_text(\"TOKEN=replace-me\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000057](../../tests/test_search_code.py#L57) | 57 | `""` | — |
| [SRC-2614DCB6FB-L000058](../../tests/test_search_code.py#L58) | 58 | `"    hits = SEARCH.search_repository(tmp_path, \"private-value\")"` | — |
| [SRC-2614DCB6FB-L000059](../../tests/test_search_code.py#L59) | 59 | `"    safe_example = SEARCH.search_repository(tmp_path, \"replace-me\")"` | — |
| [SRC-2614DCB6FB-L000060](../../tests/test_search_code.py#L60) | 60 | `""` | — |
| [SRC-2614DCB6FB-L000061](../../tests/test_search_code.py#L61) | 61 | `"    assert hits == []"` | — |
| [SRC-2614DCB6FB-L000062](../../tests/test_search_code.py#L62) | 62 | `"    assert len(safe_example) == 1"` | — |
| [SRC-2614DCB6FB-L000063](../../tests/test_search_code.py#L63) | 63 | `"    assert safe_example[0].file == \"credentials.example\""` | — |
| [SRC-2614DCB6FB-L000064](../../tests/test_search_code.py#L64) | 64 | `""` | — |
| [SRC-2614DCB6FB-L000065](../../tests/test_search_code.py#L65) | 65 | `""` | — |
| [SRC-2614DCB6FB-L000066](../../tests/test_search_code.py#L66) | 66 | `"def test_search_validates_query_limits_and_reports_invalid_regex(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000067](../../tests/test_search_code.py#L67) | 67 | `"    \"\"\"Invalid search controls fail clearly instead of silently returning confusing results.\"\"\""` | — |
| [SRC-2614DCB6FB-L000068](../../tests/test_search_code.py#L68) | 68 | `"    try:"` | — |
| [SRC-2614DCB6FB-L000069](../../tests/test_search_code.py#L69) | 69 | `"        SEARCH.search_repository(tmp_path, \"\")"` | — |
| [SRC-2614DCB6FB-L000070](../../tests/test_search_code.py#L70) | 70 | `"    except ValueError as exc:"` | — |
| [SRC-2614DCB6FB-L000071](../../tests/test_search_code.py#L71) | 71 | `"        assert \"فارغ\" in str(exc)"` | — |
| [SRC-2614DCB6FB-L000072](../../tests/test_search_code.py#L72) | 72 | `"    else:"` | — |
| [SRC-2614DCB6FB-L000073](../../tests/test_search_code.py#L73) | 73 | `"        raise AssertionError(\"An empty search query should be rejected.\")"` | — |
| [SRC-2614DCB6FB-L000074](../../tests/test_search_code.py#L74) | 74 | `""` | — |
| [SRC-2614DCB6FB-L000075](../../tests/test_search_code.py#L75) | 75 | `"    for kwargs in ({\"max_results\": 0}, {\"context\": -1}):"` | — |
| [SRC-2614DCB6FB-L000076](../../tests/test_search_code.py#L76) | 76 | `"        try:"` | — |
| [SRC-2614DCB6FB-L000077](../../tests/test_search_code.py#L77) | 77 | `"            SEARCH.search_repository(tmp_path, \"needle\", **kwargs)"` | — |
| [SRC-2614DCB6FB-L000078](../../tests/test_search_code.py#L78) | 78 | `"        except ValueError:"` | — |
| [SRC-2614DCB6FB-L000079](../../tests/test_search_code.py#L79) | 79 | `"            continue"` | — |
| [SRC-2614DCB6FB-L000080](../../tests/test_search_code.py#L80) | 80 | `"        raise AssertionError(f\"Invalid search limits should be rejected: {kwargs}\")"` | — |
| [SRC-2614DCB6FB-L000081](../../tests/test_search_code.py#L81) | 81 | `""` | — |
| [SRC-2614DCB6FB-L000082](../../tests/test_search_code.py#L82) | 82 | `"    try:"` | — |
| [SRC-2614DCB6FB-L000083](../../tests/test_search_code.py#L83) | 83 | `"        SEARCH.search_repository(tmp_path, \"(\", use_regex=True)"` | — |
| [SRC-2614DCB6FB-L000084](../../tests/test_search_code.py#L84) | 84 | `"    except re.error:"` | — |
| [SRC-2614DCB6FB-L000085](../../tests/test_search_code.py#L85) | 85 | `"        pass"` | — |
| [SRC-2614DCB6FB-L000086](../../tests/test_search_code.py#L86) | 86 | `"    else:"` | — |
| [SRC-2614DCB6FB-L000087](../../tests/test_search_code.py#L87) | 87 | `"        raise AssertionError(\"An invalid regular expression should be rejected.\")"` | — |
| [SRC-2614DCB6FB-L000088](../../tests/test_search_code.py#L88) | 88 | `""` | — |
| [SRC-2614DCB6FB-L000089](../../tests/test_search_code.py#L89) | 89 | `"def test_search_links_use_the_requested_revision_not_main(tmp_path: Path) -> None:"` | — |
| [SRC-2614DCB6FB-L000090](../../tests/test_search_code.py#L90) | 90 | `"    source = tmp_path / \"app.py\""` | — |
| [SRC-2614DCB6FB-L000091](../../tests/test_search_code.py#L91) | 91 | `"    source.write_text(\"needle = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000092](../../tests/test_search_code.py#L92) | 92 | `""` | — |
| [SRC-2614DCB6FB-L000093](../../tests/test_search_code.py#L93) | 93 | `"    hits = SEARCH.search_repository("` | — |
| [SRC-2614DCB6FB-L000094](../../tests/test_search_code.py#L94) | 94 | `"        tmp_path, \"needle\", repository_ref=\"fix/review-branch\""` | — |
| [SRC-2614DCB6FB-L000095](../../tests/test_search_code.py#L95) | 95 | `"    )"` | — |
| [SRC-2614DCB6FB-L000096](../../tests/test_search_code.py#L96) | 96 | `""` | — |
| [SRC-2614DCB6FB-L000097](../../tests/test_search_code.py#L97) | 97 | `"    assert len(hits) == 1"` | — |
| [SRC-2614DCB6FB-L000098](../../tests/test_search_code.py#L98) | 98 | `"    assert hits[0].link == ("` | — |
| [SRC-2614DCB6FB-L000099](../../tests/test_search_code.py#L99) | 99 | `"        \"https://github.com/mosabosama2030-oss/omarai/\""` | — |
| [SRC-2614DCB6FB-L000100](../../tests/test_search_code.py#L100) | 100 | `"        \"blob/fix/review-branch/app.py#L1\""` | — |
| [SRC-2614DCB6FB-L000101](../../tests/test_search_code.py#L101) | 101 | `"    )"` | — |
| [SRC-2614DCB6FB-L000102](../../tests/test_search_code.py#L102) | 102 | `""` | — |
| [SRC-2614DCB6FB-L000103](../../tests/test_search_code.py#L103) | 103 | `""` | — |
| [SRC-2614DCB6FB-L000104](../../tests/test_search_code.py#L104) | 104 | `"def test_default_repository_ref_prefers_explicit_environment_override("` | — |
| [SRC-2614DCB6FB-L000105](../../tests/test_search_code.py#L105) | 105 | `"    monkeypatch, tmp_path: Path"` | — |
| [SRC-2614DCB6FB-L000106](../../tests/test_search_code.py#L106) | 106 | `") -> None:"` | — |
| [SRC-2614DCB6FB-L000107](../../tests/test_search_code.py#L107) | 107 | `"    monkeypatch.setenv(\"OMARAI_GITHUB_REF\", \"feature/current-review\")"` | — |
| [SRC-2614DCB6FB-L000108](../../tests/test_search_code.py#L108) | 108 | `"    monkeypatch.setenv(\"GITHUB_SHA\", \"a\" * 40)"` | — |
| [SRC-2614DCB6FB-L000109](../../tests/test_search_code.py#L109) | 109 | `""` | — |
| [SRC-2614DCB6FB-L000110](../../tests/test_search_code.py#L110) | 110 | `"    assert SEARCH.default_repository_ref(tmp_path) == \"feature/current-review\""` | — |
| [SRC-2614DCB6FB-L000111](../../tests/test_search_code.py#L111) | 111 | `""` | — |
| [SRC-2614DCB6FB-L000112](../../tests/test_search_code.py#L112) | 112 | `""` | — |
| [SRC-2614DCB6FB-L000113](../../tests/test_search_code.py#L113) | 113 | `"def test_default_repository_ref_uses_valid_ci_sha("` | — |
| [SRC-2614DCB6FB-L000114](../../tests/test_search_code.py#L114) | 114 | `"    monkeypatch, tmp_path: Path"` | — |
| [SRC-2614DCB6FB-L000115](../../tests/test_search_code.py#L115) | 115 | `") -> None:"` | — |
| [SRC-2614DCB6FB-L000116](../../tests/test_search_code.py#L116) | 116 | `"    monkeypatch.delenv(\"OMARAI_GITHUB_REF\", raising=False)"` | — |
| [SRC-2614DCB6FB-L000117](../../tests/test_search_code.py#L117) | 117 | `"    monkeypatch.setenv(\"GITHUB_SHA\", \"B\" * 40)"` | — |
| [SRC-2614DCB6FB-L000118](../../tests/test_search_code.py#L118) | 118 | `""` | — |
| [SRC-2614DCB6FB-L000119](../../tests/test_search_code.py#L119) | 119 | `"    assert SEARCH.default_repository_ref(tmp_path) == \"b\" * 40"` | — |
| [SRC-2614DCB6FB-L000120](../../tests/test_search_code.py#L120) | 120 | `""` | — |
| [SRC-2614DCB6FB-L000121](../../tests/test_search_code.py#L121) | 121 | `"def test_cli_uses_explicit_ref_for_source_links(tmp_path: Path, capsys) -> None:"` | — |
| [SRC-2614DCB6FB-L000122](../../tests/test_search_code.py#L122) | 122 | `"    source = tmp_path / \"app.py\""` | — |
| [SRC-2614DCB6FB-L000123](../../tests/test_search_code.py#L123) | 123 | `"    source.write_text(\"needle = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-2614DCB6FB-L000124](../../tests/test_search_code.py#L124) | 124 | `""` | — |
| [SRC-2614DCB6FB-L000125](../../tests/test_search_code.py#L125) | 125 | `"    exit_code = SEARCH.main(["` | — |
| [SRC-2614DCB6FB-L000126](../../tests/test_search_code.py#L126) | 126 | `"        \"needle\", \"--root\", str(tmp_path), \"--ref\", \"fix/cli-review\""` | — |
| [SRC-2614DCB6FB-L000127](../../tests/test_search_code.py#L127) | 127 | `"    ])"` | — |
| [SRC-2614DCB6FB-L000128](../../tests/test_search_code.py#L128) | 128 | `""` | — |
| [SRC-2614DCB6FB-L000129](../../tests/test_search_code.py#L129) | 129 | `"    output = capsys.readouterr().out"` | — |
| [SRC-2614DCB6FB-L000130](../../tests/test_search_code.py#L130) | 130 | `"    assert exit_code == 0"` | — |
| [SRC-2614DCB6FB-L000131](../../tests/test_search_code.py#L131) | 131 | `"    assert \"blob/fix/cli-review/app.py#L1\" in output"` | — |
| [SRC-2614DCB6FB-L000132](../../tests/test_search_code.py#L132) | 132 | `"    assert \"blob/main/app.py#L1\" not in output"` | — |
| [SRC-2614DCB6FB-L000133](../../tests/test_search_code.py#L133) | 133 | `""` | — |
## اختبارات

### FILE-1C0D3D1206 — [tests/test_sqlite_backup_restore.py](../../tests/test_sqlite_backup_restore.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1C0D3D1206-L000001](../../tests/test_sqlite_backup_restore.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-1C0D3D1206-L000002](../../tests/test_sqlite_backup_restore.py#L2) | 2 | `""` | — |
| [SRC-1C0D3D1206-L000003](../../tests/test_sqlite_backup_restore.py#L3) | 3 | `"import sqlite3"` | — |
| [SRC-1C0D3D1206-L000004](../../tests/test_sqlite_backup_restore.py#L4) | 4 | `""` | — |
| [SRC-1C0D3D1206-L000005](../../tests/test_sqlite_backup_restore.py#L5) | 5 | `"import pytest"` | — |
| [SRC-1C0D3D1206-L000006](../../tests/test_sqlite_backup_restore.py#L6) | 6 | `""` | — |
| [SRC-1C0D3D1206-L000007](../../tests/test_sqlite_backup_restore.py#L7) | 7 | `"from agents.omarai import LeadStore"` | — |
| [SRC-1C0D3D1206-L000008](../../tests/test_sqlite_backup_restore.py#L8) | 8 | `"from scripts.sqlite_backup_restore import BackupError, backup_database, restore_database"` | — |
| [SRC-1C0D3D1206-L000009](../../tests/test_sqlite_backup_restore.py#L9) | 9 | `""` | — |
| [SRC-1C0D3D1206-L000010](../../tests/test_sqlite_backup_restore.py#L10) | 10 | `""` | — |
| [SRC-1C0D3D1206-L000011](../../tests/test_sqlite_backup_restore.py#L11) | 11 | `"def test_backup_and_restore_preserve_omarai_leads(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000012](../../tests/test_sqlite_backup_restore.py#L12) | 12 | `"    source_path = tmp_path / \"live.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000013](../../tests/test_sqlite_backup_restore.py#L13) | 13 | `"    source = LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000014](../../tests/test_sqlite_backup_restore.py#L14) | 14 | `"    first, created_first = source.add("` | — |
| [SRC-1C0D3D1206-L000015](../../tests/test_sqlite_backup_restore.py#L15) | 15 | `"        \"بدور على شقة في التجمع وممكن معاينة\","` | — |
| [SRC-1C0D3D1206-L000016](../../tests/test_sqlite_backup_restore.py#L16) | 16 | `"        \"https://example.com/posts/1\","` | — |
| [SRC-1C0D3D1206-L000017](../../tests/test_sqlite_backup_restore.py#L17) | 17 | `"        platform=\"manual\","` | — |
| [SRC-1C0D3D1206-L000018](../../tests/test_sqlite_backup_restore.py#L18) | 18 | `"        note=\"سجل اختبار أول\","` | — |
| [SRC-1C0D3D1206-L000019](../../tests/test_sqlite_backup_restore.py#L19) | 19 | `"    )"` | — |
| [SRC-1C0D3D1206-L000020](../../tests/test_sqlite_backup_restore.py#L20) | 20 | `"    second, created_second = source.add("` | — |
| [SRC-1C0D3D1206-L000021](../../tests/test_sqlite_backup_restore.py#L21) | 21 | `"        \"محتاج شقة للإيجار الشهر القادم\","` | — |
| [SRC-1C0D3D1206-L000022](../../tests/test_sqlite_backup_restore.py#L22) | 22 | `"        \"https://example.com/posts/2\","` | — |
| [SRC-1C0D3D1206-L000023](../../tests/test_sqlite_backup_restore.py#L23) | 23 | `"        platform=\"manual\","` | — |
| [SRC-1C0D3D1206-L000024](../../tests/test_sqlite_backup_restore.py#L24) | 24 | `"        note=\"سجل اختبار ثان\","` | — |
| [SRC-1C0D3D1206-L000025](../../tests/test_sqlite_backup_restore.py#L25) | 25 | `"    )"` | — |
| [SRC-1C0D3D1206-L000026](../../tests/test_sqlite_backup_restore.py#L26) | 26 | `"    assert created_first and created_second"` | — |
| [SRC-1C0D3D1206-L000027](../../tests/test_sqlite_backup_restore.py#L27) | 27 | `"    source.update_status(first[\"id\"], \"qualified\")"` | — |
| [SRC-1C0D3D1206-L000028](../../tests/test_sqlite_backup_restore.py#L28) | 28 | `""` | — |
| [SRC-1C0D3D1206-L000029](../../tests/test_sqlite_backup_restore.py#L29) | 29 | `"    snapshot_path = tmp_path / \"backups\" / \"snapshot.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000030](../../tests/test_sqlite_backup_restore.py#L30) | 30 | `"    backup_report = backup_database(source_path, snapshot_path)"` | — |
| [SRC-1C0D3D1206-L000031](../../tests/test_sqlite_backup_restore.py#L31) | 31 | `"    assert backup_report[\"result\"] == \"passed\""` | — |
| [SRC-1C0D3D1206-L000032](../../tests/test_sqlite_backup_restore.py#L32) | 32 | `"    assert backup_report[\"integrity_check\"] == \"ok\""` | — |
| [SRC-1C0D3D1206-L000033](../../tests/test_sqlite_backup_restore.py#L33) | 33 | `"    assert backup_report[\"lead_count\"] == 2"` | — |
| [SRC-1C0D3D1206-L000034](../../tests/test_sqlite_backup_restore.py#L34) | 34 | `"    assert backup_report[\"overwrite\"] is False"` | — |
| [SRC-1C0D3D1206-L000035](../../tests/test_sqlite_backup_restore.py#L35) | 35 | `""` | — |
| [SRC-1C0D3D1206-L000036](../../tests/test_sqlite_backup_restore.py#L36) | 36 | `"    restored_path = tmp_path / \"restored\" / \"restored.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000037](../../tests/test_sqlite_backup_restore.py#L37) | 37 | `"    restore_report = restore_database(snapshot_path, restored_path)"` | — |
| [SRC-1C0D3D1206-L000038](../../tests/test_sqlite_backup_restore.py#L38) | 38 | `"    assert restore_report[\"result\"] == \"passed\""` | — |
| [SRC-1C0D3D1206-L000039](../../tests/test_sqlite_backup_restore.py#L39) | 39 | `"    assert restore_report[\"integrity_check\"] == \"ok\""` | — |
| [SRC-1C0D3D1206-L000040](../../tests/test_sqlite_backup_restore.py#L40) | 40 | `"    assert restore_report[\"lead_count\"] == 2"` | — |
| [SRC-1C0D3D1206-L000041](../../tests/test_sqlite_backup_restore.py#L41) | 41 | `""` | — |
| [SRC-1C0D3D1206-L000042](../../tests/test_sqlite_backup_restore.py#L42) | 42 | `"    restored = LeadStore(restored_path)"` | — |
| [SRC-1C0D3D1206-L000043](../../tests/test_sqlite_backup_restore.py#L43) | 43 | `"    original_rows = {row[\"id\"]: row for row in source.list(limit=500)}"` | — |
| [SRC-1C0D3D1206-L000044](../../tests/test_sqlite_backup_restore.py#L44) | 44 | `"    restored_rows = {row[\"id\"]: row for row in restored.list(limit=500)}"` | — |
| [SRC-1C0D3D1206-L000045](../../tests/test_sqlite_backup_restore.py#L45) | 45 | `"    assert restored_rows == original_rows"` | — |
| [SRC-1C0D3D1206-L000046](../../tests/test_sqlite_backup_restore.py#L46) | 46 | `"    assert restored_rows[first[\"id\"]][\"status\"] == \"qualified\""` | — |
| [SRC-1C0D3D1206-L000047](../../tests/test_sqlite_backup_restore.py#L47) | 47 | `"    assert second[\"id\"] in restored_rows"` | — |
| [SRC-1C0D3D1206-L000048](../../tests/test_sqlite_backup_restore.py#L48) | 48 | `""` | — |
| [SRC-1C0D3D1206-L000049](../../tests/test_sqlite_backup_restore.py#L49) | 49 | `""` | — |
| [SRC-1C0D3D1206-L000050](../../tests/test_sqlite_backup_restore.py#L50) | 50 | `"def test_backup_never_overwrites_an_existing_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000051](../../tests/test_sqlite_backup_restore.py#L51) | 51 | `"    source_path = tmp_path / \"source.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000052](../../tests/test_sqlite_backup_restore.py#L52) | 52 | `"    LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000053](../../tests/test_sqlite_backup_restore.py#L53) | 53 | `"    destination = tmp_path / \"keep-me.txt\""` | — |
| [SRC-1C0D3D1206-L000054](../../tests/test_sqlite_backup_restore.py#L54) | 54 | `"    destination.write_text(\"do not overwrite\", encoding=\"utf-8\")"` | — |
| [SRC-1C0D3D1206-L000055](../../tests/test_sqlite_backup_restore.py#L55) | 55 | `""` | — |
| [SRC-1C0D3D1206-L000056](../../tests/test_sqlite_backup_restore.py#L56) | 56 | `"    with pytest.raises(FileExistsError):"` | — |
| [SRC-1C0D3D1206-L000057](../../tests/test_sqlite_backup_restore.py#L57) | 57 | `"        backup_database(source_path, destination)"` | — |
| [SRC-1C0D3D1206-L000058](../../tests/test_sqlite_backup_restore.py#L58) | 58 | `""` | — |
| [SRC-1C0D3D1206-L000059](../../tests/test_sqlite_backup_restore.py#L59) | 59 | `"    assert destination.read_text(encoding=\"utf-8\") == \"do not overwrite\""` | — |
| [SRC-1C0D3D1206-L000060](../../tests/test_sqlite_backup_restore.py#L60) | 60 | `""` | — |
| [SRC-1C0D3D1206-L000061](../../tests/test_sqlite_backup_restore.py#L61) | 61 | `""` | — |
| [SRC-1C0D3D1206-L000062](../../tests/test_sqlite_backup_restore.py#L62) | 62 | `"def test_backup_rejects_non_omarai_sqlite_database_without_leaving_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000063](../../tests/test_sqlite_backup_restore.py#L63) | 63 | `"    source_path = tmp_path / \"unrelated.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000064](../../tests/test_sqlite_backup_restore.py#L64) | 64 | `"    with sqlite3.connect(source_path) as db:"` | — |
| [SRC-1C0D3D1206-L000065](../../tests/test_sqlite_backup_restore.py#L65) | 65 | `"        db.execute(\"CREATE TABLE unrelated (value TEXT)\")"` | — |
| [SRC-1C0D3D1206-L000066](../../tests/test_sqlite_backup_restore.py#L66) | 66 | `""` | — |
| [SRC-1C0D3D1206-L000067](../../tests/test_sqlite_backup_restore.py#L67) | 67 | `"    destination = tmp_path / \"should-not-exist.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000068](../../tests/test_sqlite_backup_restore.py#L68) | 68 | `"    with pytest.raises(BackupError, match=\"not an Omarai leads database\"):"` | — |
| [SRC-1C0D3D1206-L000069](../../tests/test_sqlite_backup_restore.py#L69) | 69 | `"        backup_database(source_path, destination)"` | — |
| [SRC-1C0D3D1206-L000070](../../tests/test_sqlite_backup_restore.py#L70) | 70 | `""` | — |
| [SRC-1C0D3D1206-L000071](../../tests/test_sqlite_backup_restore.py#L71) | 71 | `"    assert not destination.exists()"` | — |
| [SRC-1C0D3D1206-L000072](../../tests/test_sqlite_backup_restore.py#L72) | 72 | `""` | — |
| [SRC-1C0D3D1206-L000073](../../tests/test_sqlite_backup_restore.py#L73) | 73 | `""` | — |
| [SRC-1C0D3D1206-L000074](../../tests/test_sqlite_backup_restore.py#L74) | 74 | `"def test_backup_rejects_same_source_and_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000075](../../tests/test_sqlite_backup_restore.py#L75) | 75 | `"    source_path = tmp_path / \"source.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000076](../../tests/test_sqlite_backup_restore.py#L76) | 76 | `"    LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000077](../../tests/test_sqlite_backup_restore.py#L77) | 77 | `""` | — |
| [SRC-1C0D3D1206-L000078](../../tests/test_sqlite_backup_restore.py#L78) | 78 | `"    with pytest.raises(BackupError, match=\"different paths\"):"` | — |
| [SRC-1C0D3D1206-L000079](../../tests/test_sqlite_backup_restore.py#L79) | 79 | `"        backup_database(source_path, source_path)"` | — |
| [SRC-1C0D3D1206-L000080](../../tests/test_sqlite_backup_restore.py#L80) | 80 | `""` | — |
| [SRC-1C0D3D1206-L000081](../../tests/test_sqlite_backup_restore.py#L81) | 81 | `""` | — |
| [SRC-1C0D3D1206-L000082](../../tests/test_sqlite_backup_restore.py#L82) | 82 | `"def test_restore_rejects_corrupt_backup_without_overwriting_source(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000083](../../tests/test_sqlite_backup_restore.py#L83) | 83 | `"    backup_path = tmp_path / \"corrupt.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000084](../../tests/test_sqlite_backup_restore.py#L84) | 84 | `"    backup_path.write_bytes(b\"not a sqlite database\")"` | — |
| [SRC-1C0D3D1206-L000085](../../tests/test_sqlite_backup_restore.py#L85) | 85 | `"    destination = tmp_path / \"restore.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000086](../../tests/test_sqlite_backup_restore.py#L86) | 86 | `""` | — |
| [SRC-1C0D3D1206-L000087](../../tests/test_sqlite_backup_restore.py#L87) | 87 | `"    with pytest.raises(BackupError):"` | — |
| [SRC-1C0D3D1206-L000088](../../tests/test_sqlite_backup_restore.py#L88) | 88 | `"        restore_database(backup_path, destination)"` | — |
| [SRC-1C0D3D1206-L000089](../../tests/test_sqlite_backup_restore.py#L89) | 89 | `""` | — |
| [SRC-1C0D3D1206-L000090](../../tests/test_sqlite_backup_restore.py#L90) | 90 | `"    assert backup_path.read_bytes() == b\"not a sqlite database\""` | — |
| [SRC-1C0D3D1206-L000091](../../tests/test_sqlite_backup_restore.py#L91) | 91 | `"    assert not destination.exists()"` | — |
| [SRC-1C0D3D1206-L000092](../../tests/test_sqlite_backup_restore.py#L92) | 92 | `""` | — |
| [SRC-1C0D3D1206-L000093](../../tests/test_sqlite_backup_restore.py#L93) | 93 | `"def test_backup_rejects_dangling_symlink_destination(tmp_path):"` | — |
| [SRC-1C0D3D1206-L000094](../../tests/test_sqlite_backup_restore.py#L94) | 94 | `"    source_path = tmp_path / \"source.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000095](../../tests/test_sqlite_backup_restore.py#L95) | 95 | `"    LeadStore(source_path)"` | — |
| [SRC-1C0D3D1206-L000096](../../tests/test_sqlite_backup_restore.py#L96) | 96 | `"    target_path = tmp_path / \"target.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000097](../../tests/test_sqlite_backup_restore.py#L97) | 97 | `"    destination_link = tmp_path / \"backup-link.sqlite3\""` | — |
| [SRC-1C0D3D1206-L000098](../../tests/test_sqlite_backup_restore.py#L98) | 98 | `"    destination_link.symlink_to(target_path)"` | — |
| [SRC-1C0D3D1206-L000099](../../tests/test_sqlite_backup_restore.py#L99) | 99 | `""` | — |
| [SRC-1C0D3D1206-L000100](../../tests/test_sqlite_backup_restore.py#L100) | 100 | `"    with pytest.raises(FileExistsError):"` | — |
| [SRC-1C0D3D1206-L000101](../../tests/test_sqlite_backup_restore.py#L101) | 101 | `"        backup_database(source_path, destination_link)"` | — |
| [SRC-1C0D3D1206-L000102](../../tests/test_sqlite_backup_restore.py#L102) | 102 | `""` | — |
| [SRC-1C0D3D1206-L000103](../../tests/test_sqlite_backup_restore.py#L103) | 103 | `"    assert destination_link.is_symlink()"` | — |
| [SRC-1C0D3D1206-L000104](../../tests/test_sqlite_backup_restore.py#L104) | 104 | `"    assert not target_path.exists()"` | — |
| [SRC-1C0D3D1206-L000105](../../tests/test_sqlite_backup_restore.py#L105) | 105 | `""` | — |
## اختبارات

### FILE-AFEDC2645A — [tests/test_task_understanding.py](../../tests/test_task_understanding.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-AFEDC2645A-L000001](../../tests/test_task_understanding.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-AFEDC2645A-L000002](../../tests/test_task_understanding.py#L2) | 2 | `""` | — |
| [SRC-AFEDC2645A-L000003](../../tests/test_task_understanding.py#L3) | 3 | `"import pytest"` | — |
| [SRC-AFEDC2645A-L000004](../../tests/test_task_understanding.py#L4) | 4 | `""` | — |
| [SRC-AFEDC2645A-L000005](../../tests/test_task_understanding.py#L5) | 5 | `"from agents.task_understanding import build_query_strategy_matrix, build_task_spec"` | — |
| [SRC-AFEDC2645A-L000006](../../tests/test_task_understanding.py#L6) | 6 | `""` | — |
| [SRC-AFEDC2645A-L000007](../../tests/test_task_understanding.py#L7) | 7 | `""` | — |
| [SRC-AFEDC2645A-L000008](../../tests/test_task_understanding.py#L8) | 8 | `"@pytest.mark.parametrize("` | — |
| [SRC-AFEDC2645A-L000009](../../tests/test_task_understanding.py#L9) | 9 | `"    (\"question\", \"family\"),"` | — |
| [SRC-AFEDC2645A-L000010](../../tests/test_task_understanding.py#L10) | 10 | `"    ["` | — |
| [SRC-AFEDC2645A-L000011](../../tests/test_task_understanding.py#L11) | 11 | `"        (\"ابحث عن الموقع الرسمي لوزارة الاتصالات في مصر\", \"official_site_lookup\"),"` | — |
| [SRC-AFEDC2645A-L000012](../../tests/test_task_understanding.py#L12) | 12 | `"        (\"مواعيد عمل مكتب الجوازات اليوم في العباسية\", \"current_information\"),"` | — |
| [SRC-AFEDC2645A-L000013](../../tests/test_task_understanding.py#L13) | 13 | `"        (\"قارن نيسان صني 2022 وهيونداي أكسنت من حيث السعر والصيانة\", \"compare\"),"` | — |
| [SRC-AFEDC2645A-L000014](../../tests/test_task_understanding.py#L14) | 14 | `"        (\"عايز تجارب ملاك BYD Dolphin في مصر\", \"social_opinions\"),"` | — |
| [SRC-AFEDC2645A-L000015](../../tests/test_task_understanding.py#L15) | 15 | `"        (\"ازاي أصلح خطأ الشبكة في لوحة إنذار الحريق؟\", \"troubleshoot\"),"` | — |
| [SRC-AFEDC2645A-L000016](../../tests/test_task_understanding.py#L16) | 16 | `"        (\"اشرح خطوات صيانة حساس الدخان\", \"how_to\"),"` | — |
| [SRC-AFEDC2645A-L000017](../../tests/test_task_understanding.py#L17) | 17 | `"        (\"لخص الصفحة https://example.com/article\", \"summarize\"),"` | — |
| [SRC-AFEDC2645A-L000018](../../tests/test_task_understanding.py#L18) | 18 | `"        (\"ابحث عن مشترين يريدون شراء شقة في القاهرة\", \"lead_generation\"),"` | — |
| [SRC-AFEDC2645A-L000019](../../tests/test_task_understanding.py#L19) | 19 | `"        (\"رشح لي أفضل سيارة بميزانية أقل من 500000 جنيه\", \"recommendation\"),"` | — |
| [SRC-AFEDC2645A-L000020](../../tests/test_task_understanding.py#L20) | 20 | `"        (\"ما معنى نظام الإنذار المعنون؟\", \"explain_or_define\"),"` | — |
| [SRC-AFEDC2645A-L000021](../../tests/test_task_understanding.py#L21) | 21 | `"    ],"` | — |
| [SRC-AFEDC2645A-L000022](../../tests/test_task_understanding.py#L22) | 22 | `")"` | — |
| [SRC-AFEDC2645A-L000023](../../tests/test_task_understanding.py#L23) | 23 | `"def test_task_family_covers_diverse_natural_language_patterns(question, family):"` | — |
| [SRC-AFEDC2645A-L000024](../../tests/test_task_understanding.py#L24) | 24 | `"    spec = build_task_spec(question, mode=\"auto\", intent_route=\"WEB_SIMPLE\")"` | — |
| [SRC-AFEDC2645A-L000025](../../tests/test_task_understanding.py#L25) | 25 | `"    assert spec[\"task_family\"] == family"` | — |
| [SRC-AFEDC2645A-L000026](../../tests/test_task_understanding.py#L26) | 26 | `"    assert spec[\"classification_is_probability\"] is False"` | — |
| [SRC-AFEDC2645A-L000027](../../tests/test_task_understanding.py#L27) | 27 | `"    assert spec[\"decision_checks\"]"` | — |
| [SRC-AFEDC2645A-L000028](../../tests/test_task_understanding.py#L28) | 28 | `""` | — |
| [SRC-AFEDC2645A-L000029](../../tests/test_task_understanding.py#L29) | 29 | `""` | — |
| [SRC-AFEDC2645A-L000030](../../tests/test_task_understanding.py#L30) | 30 | `"def test_task_spec_preserves_only_explicit_constraints():"` | — |
| [SRC-AFEDC2645A-L000031](../../tests/test_task_understanding.py#L31) | 31 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000032](../../tests/test_task_understanding.py#L32) | 32 | `"        \"قارن نيسان صني 2022 مع BYD Dolphin في مصر، بميزانية أقل من 400 ألف جنيه\","` | — |
| [SRC-AFEDC2645A-L000033](../../tests/test_task_understanding.py#L33) | 33 | `"        mode=\"deep\","` | — |
| [SRC-AFEDC2645A-L000034](../../tests/test_task_understanding.py#L34) | 34 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000035](../../tests/test_task_understanding.py#L35) | 35 | `"    )"` | — |
| [SRC-AFEDC2645A-L000036](../../tests/test_task_understanding.py#L36) | 36 | `"    constraints = spec[\"constraints\"]"` | — |
| [SRC-AFEDC2645A-L000037](../../tests/test_task_understanding.py#L37) | 37 | `"    assert \"2022\" in constraints[\"explicit_years\"]"` | — |
| [SRC-AFEDC2645A-L000038](../../tests/test_task_understanding.py#L38) | 38 | `"    assert \"مصر\" in constraints[\"explicit_locations\"]"` | — |
| [SRC-AFEDC2645A-L000039](../../tests/test_task_understanding.py#L39) | 39 | `"    assert constraints[\"explicit_budgets\"]"` | — |
| [SRC-AFEDC2645A-L000040](../../tests/test_task_understanding.py#L40) | 40 | `"    assert constraints[\"language_profile\"] in {\"ar\", \"mixed\"}"` | — |
| [SRC-AFEDC2645A-L000041](../../tests/test_task_understanding.py#L41) | 41 | `""` | — |
| [SRC-AFEDC2645A-L000042](../../tests/test_task_understanding.py#L42) | 42 | `""` | — |
| [SRC-AFEDC2645A-L000043](../../tests/test_task_understanding.py#L43) | 43 | `"def test_latest_mode_requires_current_evidence_for_stateful_facts():"` | — |
| [SRC-AFEDC2645A-L000044](../../tests/test_task_understanding.py#L44) | 44 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000045](../../tests/test_task_understanding.py#L45) | 45 | `"        \"مواعيد عمل مكتب الجوازات اليوم\","` | — |
| [SRC-AFEDC2645A-L000046](../../tests/test_task_understanding.py#L46) | 46 | `"        mode=\"latest\","` | — |
| [SRC-AFEDC2645A-L000047](../../tests/test_task_understanding.py#L47) | 47 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000048](../../tests/test_task_understanding.py#L48) | 48 | `"    )"` | — |
| [SRC-AFEDC2645A-L000049](../../tests/test_task_understanding.py#L49) | 49 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is True"` | — |
| [SRC-AFEDC2645A-L000050](../../tests/test_task_understanding.py#L50) | 50 | `"    assert \"page_text_successfully_read\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000051](../../tests/test_task_understanding.py#L51) | 51 | `"    assert \"date_check\" in spec[\"query_strategies\"]"` | — |
| [SRC-AFEDC2645A-L000052](../../tests/test_task_understanding.py#L52) | 52 | `""` | — |
| [SRC-AFEDC2645A-L000053](../../tests/test_task_understanding.py#L53) | 53 | `""` | — |
| [SRC-AFEDC2645A-L000054](../../tests/test_task_understanding.py#L54) | 54 | `"def test_official_site_navigation_is_not_misclassified_as_current_news():"` | — |
| [SRC-AFEDC2645A-L000055](../../tests/test_task_understanding.py#L55) | 55 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000056](../../tests/test_task_understanding.py#L56) | 56 | `"        \"ابحث عن الموقع الرسمي لوزارة الاتصالات في مصر\","` | — |
| [SRC-AFEDC2645A-L000057](../../tests/test_task_understanding.py#L57) | 57 | `"        mode=\"latest\","` | — |
| [SRC-AFEDC2645A-L000058](../../tests/test_task_understanding.py#L58) | 58 | `"        intent_route=\"WEB_SIMPLE\","` | — |
| [SRC-AFEDC2645A-L000059](../../tests/test_task_understanding.py#L59) | 59 | `"    )"` | — |
| [SRC-AFEDC2645A-L000060](../../tests/test_task_understanding.py#L60) | 60 | `"    assert spec[\"task_family\"] == \"official_site_lookup\""` | — |
| [SRC-AFEDC2645A-L000061](../../tests/test_task_understanding.py#L61) | 61 | `"    assert spec[\"constraints\"][\"official_site_required\"] is True"` | — |
| [SRC-AFEDC2645A-L000062](../../tests/test_task_understanding.py#L62) | 62 | `"    assert spec[\"constraints\"][\"time_sensitive_request\"] is False"` | — |
| [SRC-AFEDC2645A-L000063](../../tests/test_task_understanding.py#L63) | 63 | `""` | — |
| [SRC-AFEDC2645A-L000064](../../tests/test_task_understanding.py#L64) | 64 | `""` | — |
| [SRC-AFEDC2645A-L000065](../../tests/test_task_understanding.py#L65) | 65 | `"def test_social_request_separates_experience_from_truth_verification():"` | — |
| [SRC-AFEDC2645A-L000066](../../tests/test_task_understanding.py#L66) | 66 | `"    spec = build_task_spec("` | — |
| [SRC-AFEDC2645A-L000067](../../tests/test_task_understanding.py#L67) | 67 | `"        \"أريد آراء وتجارب ملاك نيسان صني 2022 في مصر\","` | — |
| [SRC-AFEDC2645A-L000068](../../tests/test_task_understanding.py#L68) | 68 | `"        mode=\"social\","` | — |
| [SRC-AFEDC2645A-L000069](../../tests/test_task_understanding.py#L69) | 69 | `"        intent_route=\"WEB_DEEP\","` | — |
| [SRC-AFEDC2645A-L000070](../../tests/test_task_understanding.py#L70) | 70 | `"    )"` | — |
| [SRC-AFEDC2645A-L000071](../../tests/test_task_understanding.py#L71) | 71 | `"    assert spec[\"constraints\"][\"social_evidence_requested\"] is True"` | — |
| [SRC-AFEDC2645A-L000072](../../tests/test_task_understanding.py#L72) | 72 | `"    assert \"heuristic_classification_is_not_identity_or_truth_verification\" in spec[\"evidence_requirements\"]"` | — |
| [SRC-AFEDC2645A-L000073](../../tests/test_task_understanding.py#L73) | 73 | `"    assert \"personal_experience\" in spec[\"query_strategies\"]"` | — |
