# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **014**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L001287 إلى SRC-1AE03B9EC3-L002086
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L001287](../../agents/web_agent.py#L1287) | 1287 | `"        \"\"\"Generate bounded, sector-neutral buyer queries anchored to the requested product.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001288](../../agents/web_agent.py#L1288) | 1288 | `"        subject = _normalize_search_query(question).strip()"` | — |
| [SRC-1AE03B9EC3-L001289](../../agents/web_agent.py#L1289) | 1289 | `"        subject = re.sub(r\"(?<!\\w)عملاش(?!\\w)\", \"عملاء\", subject, flags=re.IGNORECASE)"` | — |
| [SRC-1AE03B9EC3-L001290](../../agents/web_agent.py#L1290) | 1290 | `"        subject = re.sub(r\"(?<!\\w)شرا(?!\\w)\", \"شراء\", subject, flags=re.IGNORECASE)"` | — |
| [SRC-1AE03B9EC3-L001291](../../agents/web_agent.py#L1291) | 1291 | `"        arabic = bool(re.search(r\"[\\u0600-\\u06FF]\", question))"` | — |
| [SRC-1AE03B9EC3-L001292](../../agents/web_agent.py#L1292) | 1292 | `"        if arabic:"` | — |
| [SRC-1AE03B9EC3-L001293](../../agents/web_agent.py#L1293) | 1293 | `"            subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L001294](../../agents/web_agent.py#L1294) | 1294 | `"                r\"^(?:(?:من فضلك\|لو سمحت)\\s*)?(?:ابحث\|بحث\|دور\|دورلي\|اعثر)(?:لي)?\\s+\""` | — |
| [SRC-1AE03B9EC3-L001295](../../agents/web_agent.py#L1295) | 1295 | `"                r\"(?:لي\\s+)?(?:عن\|على)\\s*\","` | — |
| [SRC-1AE03B9EC3-L001296](../../agents/web_agent.py#L1296) | 1296 | `"                \"\", subject, flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L001297](../../agents/web_agent.py#L1297) | 1297 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001298](../../agents/web_agent.py#L1298) | 1298 | `"            subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L001299](../../agents/web_agent.py#L1299) | 1299 | `"                r\"^(?:[0-9٠-٩]+\\s*)?(?:عميل(?:\\s+محتمل)?\|عملاء(?:\\s+محتملين)?\|\""` | — |
| [SRC-1AE03B9EC3-L001300](../../agents/web_agent.py#L1300) | 1300 | `"                r\"عملاش\|مشتري(?:ن)?\|مشترين)\\s*\","` | — |
| [SRC-1AE03B9EC3-L001301](../../agents/web_agent.py#L1301) | 1301 | `"                \"\", subject, flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L001302](../../agents/web_agent.py#L1302) | 1302 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001303](../../agents/web_agent.py#L1303) | 1303 | `"            intent_word = ("` | — |
| [SRC-1AE03B9EC3-L001304](../../agents/web_agent.py#L1304) | 1304 | `"                r\"(?:يطلب(?:ون)?\|يريد(?:ون)?\|عايز(?:ين)?\|عاوز(?:ين)?\|محتاج(?:ين)?\|\""` | — |
| [SRC-1AE03B9EC3-L001305](../../agents/web_agent.py#L1305) | 1305 | `"                r\"مهتم(?:ين)?\|بيطلب(?:وا)?\|يبحث(?:ون)?\|بيبحث(?:وا)?\|يدور(?:وا)?)\""` | — |
| [SRC-1AE03B9EC3-L001306](../../agents/web_agent.py#L1306) | 1306 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001307](../../agents/web_agent.py#L1307) | 1307 | `"            subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L001308](../../agents/web_agent.py#L1308) | 1308 | `"                r\"^(?:(?:الذي\|اللي\|الذين)\\s*)?\" + intent_word"` | — |
| [SRC-1AE03B9EC3-L001309](../../agents/web_agent.py#L1309) | 1309 | `"                + r\"(?:\\s+(?:او\|أو)\\s+\" + intent_word + r\")*\\s*\","` | — |
| [SRC-1AE03B9EC3-L001310](../../agents/web_agent.py#L1310) | 1310 | `"                \"\", subject, flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L001311](../../agents/web_agent.py#L1311) | 1311 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001312](../../agents/web_agent.py#L1312) | 1312 | `"            subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L001313](../../agents/web_agent.py#L1313) | 1313 | `"                r\"^(?:(?:ان\|أن)\\s*)?(?:يشتري\|يشترو\|يشترون\|اشتري\|شراء\|شرا\|لشراء)\\s*\","` | — |
| [SRC-1AE03B9EC3-L001314](../../agents/web_agent.py#L1314) | 1314 | `"                \"\", subject, flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L001315](../../agents/web_agent.py#L1315) | 1315 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001316](../../agents/web_agent.py#L1316) | 1316 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001317](../../agents/web_agent.py#L1317) | 1317 | `"            subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L001318](../../agents/web_agent.py#L1318) | 1318 | `"                r\"^(?:please\\s+)?(?:find\|search for\|look for)\\s+(?:(?:a\|an)\\s+)?\""` | — |
| [SRC-1AE03B9EC3-L001319](../../agents/web_agent.py#L1319) | 1319 | `"                r\"(?:(?:potential\\s+)?(?:customer\|buyer\|prospect\|lead)s?)\\s*\""` | — |
| [SRC-1AE03B9EC3-L001320](../../agents/web_agent.py#L1320) | 1320 | `"                r\"(?:(?:who\|that)\\s*)?(?:(?:wants?\|looking to\|seeking to)\\s+\""` | — |
| [SRC-1AE03B9EC3-L001321](../../agents/web_agent.py#L1321) | 1321 | `"                r\"(?:buy\|purchase)\\s*)?\","` | — |
| [SRC-1AE03B9EC3-L001322](../../agents/web_agent.py#L1322) | 1322 | `"                \"\", subject, flags=re.IGNORECASE,"` | — |
| [SRC-1AE03B9EC3-L001323](../../agents/web_agent.py#L1323) | 1323 | `"            ).strip(\" \\t:;,.-\")"` | — |
| [SRC-1AE03B9EC3-L001324](../../agents/web_agent.py#L1324) | 1324 | `"        if not subject:"` | — |
| [SRC-1AE03B9EC3-L001325](../../agents/web_agent.py#L1325) | 1325 | `"            subject = _normalize_search_query(question).strip()"` | — |
| [SRC-1AE03B9EC3-L001326](../../agents/web_agent.py#L1326) | 1326 | `""` | — |
| [SRC-1AE03B9EC3-L001327](../../agents/web_agent.py#L1327) | 1327 | `"        profile = ProductProfile(name=subject[:240])"` | — |
| [SRC-1AE03B9EC3-L001328](../../agents/web_agent.py#L1328) | 1328 | `"        has_arabic = bool(re.search(r\"[\\u0600-\\u06FF]\", question))"` | — |
| [SRC-1AE03B9EC3-L001329](../../agents/web_agent.py#L1329) | 1329 | `"        has_latin = bool(re.search(r\"[A-Za-z]\", question))"` | — |
| [SRC-1AE03B9EC3-L001330](../../agents/web_agent.py#L1330) | 1330 | `"        locale = \"mixed\" if has_arabic and has_latin else \"ar\" if has_arabic else \"en\""` | — |
| [SRC-1AE03B9EC3-L001331](../../agents/web_agent.py#L1331) | 1331 | `"        return build_buyer_queries("` | — |
| [SRC-1AE03B9EC3-L001332](../../agents/web_agent.py#L1332) | 1332 | `"            profile,"` | — |
| [SRC-1AE03B9EC3-L001333](../../agents/web_agent.py#L1333) | 1333 | `"            locale=locale,"` | — |
| [SRC-1AE03B9EC3-L001334](../../agents/web_agent.py#L1334) | 1334 | `"            existing_queries=existing_queries or (),"` | — |
| [SRC-1AE03B9EC3-L001335](../../agents/web_agent.py#L1335) | 1335 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001336](../../agents/web_agent.py#L1336) | 1336 | `""` | — |
| [SRC-1AE03B9EC3-L001337](../../agents/web_agent.py#L1337) | 1337 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001338](../../agents/web_agent.py#L1338) | 1338 | `"    def _is_listing_discovery(question: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L001339](../../agents/web_agent.py#L1339) | 1339 | `"        \"\"\"Recognize property/job/product discovery where candidates are useful with caveats.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001340](../../agents/web_agent.py#L1340) | 1340 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L001341](../../agents/web_agent.py#L1341) | 1341 | `"        entities = ("` | — |
| [SRC-1AE03B9EC3-L001342](../../agents/web_agent.py#L1342) | 1342 | `"            \"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"فيلا\", \"فلل\", \"وحده سكنيه\","` | — |
| [SRC-1AE03B9EC3-L001343](../../agents/web_agent.py#L1343) | 1343 | `"            \"وحدات سكنيه\", \"apartment\", \"apartments\", \"flat\", \"property listing\","` | — |
| [SRC-1AE03B9EC3-L001344](../../agents/web_agent.py#L1344) | 1344 | `"            \"real estate\", \"house\", \"villa\", \"job opening\", \"وظيفه\", \"وظائف\","` | — |
| [SRC-1AE03B9EC3-L001345](../../agents/web_agent.py#L1345) | 1345 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001346](../../agents/web_agent.py#L1346) | 1346 | `"        actions = ("` | — |
| [SRC-1AE03B9EC3-L001347](../../agents/web_agent.py#L1347) | 1347 | `"            \"ابحث\", \"دور\", \"هات\", \"عايز\", \"عاوز\", \"محتاج\", \"بدور\", \"للبيع\","` | — |
| [SRC-1AE03B9EC3-L001348](../../agents/web_agent.py#L1348) | 1348 | `"            \"للايجار\", \"ايجار\", \"معاينه\", \"اعلان\", \"اعلانات\", \"find\", \"search\","` | — |
| [SRC-1AE03B9EC3-L001349](../../agents/web_agent.py#L1349) | 1349 | `"            \"looking for\", \"for sale\", \"for rent\","` | — |
| [SRC-1AE03B9EC3-L001350](../../agents/web_agent.py#L1350) | 1350 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001351](../../agents/web_agent.py#L1351) | 1351 | `"        normalized_entities = (_normalize_search_query(term).casefold() for term in entities)"` | — |
| [SRC-1AE03B9EC3-L001352](../../agents/web_agent.py#L1352) | 1352 | `"        normalized_actions = (_normalize_search_query(term).casefold() for term in actions)"` | — |
| [SRC-1AE03B9EC3-L001353](../../agents/web_agent.py#L1353) | 1353 | `"        return any(term in value for term in normalized_entities) and any("` | — |
| [SRC-1AE03B9EC3-L001354](../../agents/web_agent.py#L1354) | 1354 | `"            term in value for term in normalized_actions"` | — |
| [SRC-1AE03B9EC3-L001355](../../agents/web_agent.py#L1355) | 1355 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001356](../../agents/web_agent.py#L1356) | 1356 | `""` | — |
| [SRC-1AE03B9EC3-L001357](../../agents/web_agent.py#L1357) | 1357 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001358](../../agents/web_agent.py#L1358) | 1358 | `"    def _requires_web_research(question: str, mode: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L001359](../../agents/web_agent.py#L1359) | 1359 | `"        \"\"\"Use the web only when the user requests it or the answer depends on live data.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001360](../../agents/web_agent.py#L1360) | 1360 | `"        # A question about whether the current answer already searched is a"` | — |
| [SRC-1AE03B9EC3-L001361](../../agents/web_agent.py#L1361) | 1361 | `"        # status query, not a request to launch fresh research in any UI mode."` | — |
| [SRC-1AE03B9EC3-L001362](../../agents/web_agent.py#L1362) | 1362 | `"        if WebAgent._is_current_search_status_question(question):"` | — |
| [SRC-1AE03B9EC3-L001363](../../agents/web_agent.py#L1363) | 1363 | `"            return False"` | — |
| [SRC-1AE03B9EC3-L001364](../../agents/web_agent.py#L1364) | 1364 | `"        if mode != \"auto\":"` | — |
| [SRC-1AE03B9EC3-L001365](../../agents/web_agent.py#L1365) | 1365 | `"            return True"` | — |
| [SRC-1AE03B9EC3-L001366](../../agents/web_agent.py#L1366) | 1366 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L001367](../../agents/web_agent.py#L1367) | 1367 | `"        dynamic_terms = ("` | — |
| [SRC-1AE03B9EC3-L001368](../../agents/web_agent.py#L1368) | 1368 | `"            \"ابحث\", \"بحث عن\", \"دور على\", \"دورلي\", \"هات رابط\", \"هاتلي\","` | — |
| [SRC-1AE03B9EC3-L001369](../../agents/web_agent.py#L1369) | 1369 | `"            \"جيبلي\", \"اعثر على\", \"موقع\", \"رابط\", \"لينك\", \"اخبار\", \"اخر\","` | — |
| [SRC-1AE03B9EC3-L001370](../../agents/web_agent.py#L1370) | 1370 | `"            \"احدث\", \"اليوم\", \"دلوقتي\", \"حاليا\", \"سعر\", \"اسعار\", \"للبيع\","` | — |
| [SRC-1AE03B9EC3-L001371](../../agents/web_agent.py#L1371) | 1371 | `"            \"للايجار\", \"ايجار\", \"معاينه\", \"عميل محتمل\", \"عملاء محتملين\","` | — |
| [SRC-1AE03B9EC3-L001372](../../agents/web_agent.py#L1372) | 1372 | `"            \"وظائف\", \"وظيفه\", \"حجز\", \"موعد\", \"الطقس\", \"سهم\", \"سعر الصرف\","` | — |
| [SRC-1AE03B9EC3-L001373](../../agents/web_agent.py#L1373) | 1373 | `"            \"search\", \"find\", \"look up\", \"latest\", \"today\", \"current\","` | — |
| [SRC-1AE03B9EC3-L001374](../../agents/web_agent.py#L1374) | 1374 | `"            \"news\", \"price\", \"for sale\", \"for rent\", \"real estate\", \"job opening\","` | — |
| [SRC-1AE03B9EC3-L001375](../../agents/web_agent.py#L1375) | 1375 | `"            \"appointment\", \"reservation\", \"weather\", \"stock price\", \"exchange rate\","` | — |
| [SRC-1AE03B9EC3-L001376](../../agents/web_agent.py#L1376) | 1376 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001377](../../agents/web_agent.py#L1377) | 1377 | `"        return any(term in value for term in dynamic_terms) or bool("` | — |
| [SRC-1AE03B9EC3-L001378](../../agents/web_agent.py#L1378) | 1378 | `"            re.search(r\"https?://\", question, flags=re.IGNORECASE)"` | — |
| [SRC-1AE03B9EC3-L001379](../../agents/web_agent.py#L1379) | 1379 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001380](../../agents/web_agent.py#L1380) | 1380 | `""` | — |
| [SRC-1AE03B9EC3-L001381](../../agents/web_agent.py#L1381) | 1381 | `"    def _local_answer_result(self, question: str, answer: str, kind: str) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001382](../../agents/web_agent.py#L1382) | 1382 | `"        \"\"\"Build a consistently shaped answer for non-research conversational requests.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001383](../../agents/web_agent.py#L1383) | 1383 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L001384](../../agents/web_agent.py#L1384) | 1384 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L001385](../../agents/web_agent.py#L1385) | 1385 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L001386](../../agents/web_agent.py#L1386) | 1386 | `"            \"search_query\": question,"` | — |
| [SRC-1AE03B9EC3-L001387](../../agents/web_agent.py#L1387) | 1387 | `"            \"search_queries\": [],"` | — |
| [SRC-1AE03B9EC3-L001388](../../agents/web_agent.py#L1388) | 1388 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L001389](../../agents/web_agent.py#L1389) | 1389 | `"                \"mode\": \"auto\","` | — |
| [SRC-1AE03B9EC3-L001390](../../agents/web_agent.py#L1390) | 1390 | `"                \"planning_method\": \"local_capability_router\","` | — |
| [SRC-1AE03B9EC3-L001391](../../agents/web_agent.py#L1391) | 1391 | `"                \"web_search_skipped\": True,"` | — |
| [SRC-1AE03B9EC3-L001392](../../agents/web_agent.py#L1392) | 1392 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001393](../../agents/web_agent.py#L1393) | 1393 | `"            \"sources\": [],"` | — |
| [SRC-1AE03B9EC3-L001394](../../agents/web_agent.py#L1394) | 1394 | `"            \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L001395](../../agents/web_agent.py#L1395) | 1395 | `"            \"used_web_search\": False,"` | — |
| [SRC-1AE03B9EC3-L001396](../../agents/web_agent.py#L1396) | 1396 | `"            \"search_attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L001397](../../agents/web_agent.py#L1397) | 1397 | `"            \"used_social_search\": False,"` | — |
| [SRC-1AE03B9EC3-L001398](../../agents/web_agent.py#L1398) | 1398 | `"            \"warnings\": [],"` | — |
| [SRC-1AE03B9EC3-L001399](../../agents/web_agent.py#L1399) | 1399 | `"            \"kind\": kind,"` | — |
| [SRC-1AE03B9EC3-L001400](../../agents/web_agent.py#L1400) | 1400 | `"            \"research_quality\": \"not_applicable\","` | — |
| [SRC-1AE03B9EC3-L001401](../../agents/web_agent.py#L1401) | 1401 | `"        }"` | — |
| [SRC-1AE03B9EC3-L001402](../../agents/web_agent.py#L1402) | 1402 | `""` | — |
| [SRC-1AE03B9EC3-L001403](../../agents/web_agent.py#L1403) | 1403 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001404](../../agents/web_agent.py#L1404) | 1404 | `"    def _local_conversation_reply(question: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L001405](../../agents/web_agent.py#L1405) | 1405 | `"        \"\"\"Return a short greeting/acknowledgment without a model or web request.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001406](../../agents/web_agent.py#L1406) | 1406 | `"        value = _normalize_search_query(question).casefold().strip(\" \\t\\r\\n؟?!.,،؛;\")"` | — |
| [SRC-1AE03B9EC3-L001407](../../agents/web_agent.py#L1407) | 1407 | `"        if \"السلام عليكم\" in value:"` | — |
| [SRC-1AE03B9EC3-L001408](../../agents/web_agent.py#L1408) | 1408 | `"            return \"وعليكم السلام ورحمة الله وبركاته. أنا معاك؛ أقدر أساعدك في إيه؟\""` | — |
| [SRC-1AE03B9EC3-L001409](../../agents/web_agent.py#L1409) | 1409 | `"        if any(term in value for term in (\"شكرا\", \"متشكر\", \"متشكره\", \"العفو\")):"` | — |
| [SRC-1AE03B9EC3-L001410](../../agents/web_agent.py#L1410) | 1410 | `"            return \"العفو، تحت أمرك.\""` | — |
| [SRC-1AE03B9EC3-L001411](../../agents/web_agent.py#L1411) | 1411 | `"        if re.search(r\"[a-z]\", value):"` | — |
| [SRC-1AE03B9EC3-L001412](../../agents/web_agent.py#L1412) | 1412 | `"            if any(term in value for term in (\"thanks\", \"thank you\", \"got it\")):"` | — |
| [SRC-1AE03B9EC3-L001413](../../agents/web_agent.py#L1413) | 1413 | `"                return \"You're welcome—glad it helped.\""` | — |
| [SRC-1AE03B9EC3-L001414](../../agents/web_agent.py#L1414) | 1414 | `"            return \"Hi! I'm here and ready to help. What would you like to work on?\""` | — |
| [SRC-1AE03B9EC3-L001415](../../agents/web_agent.py#L1415) | 1415 | `"        return \"أهلًا! أنا معاك. أقدر أساعدك في إيه؟\""` | — |
| [SRC-1AE03B9EC3-L001416](../../agents/web_agent.py#L1416) | 1416 | `""` | — |
| [SRC-1AE03B9EC3-L001417](../../agents/web_agent.py#L1417) | 1417 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L001418](../../agents/web_agent.py#L1418) | 1418 | `"    def _annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L001419](../../agents/web_agent.py#L1419) | 1419 | `"        result: dict[str, Any], route: str, reason: str, mode: str = \"auto\""` | — |
| [SRC-1AE03B9EC3-L001420](../../agents/web_agent.py#L1420) | 1420 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001421](../../agents/web_agent.py#L1421) | 1421 | `"        \"\"\"Attach route diagnostics to both response and research-plan metadata.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001422](../../agents/web_agent.py#L1422) | 1422 | `"        result[\"intent_route\"] = route"` | — |
| [SRC-1AE03B9EC3-L001423](../../agents/web_agent.py#L1423) | 1423 | `"        result[\"intent_route_reason\"] = reason"` | — |
| [SRC-1AE03B9EC3-L001424](../../agents/web_agent.py#L1424) | 1424 | `"        plan = result.get(\"research_plan\")"` | — |
| [SRC-1AE03B9EC3-L001425](../../agents/web_agent.py#L1425) | 1425 | `"        if not isinstance(plan, dict):"` | — |
| [SRC-1AE03B9EC3-L001426](../../agents/web_agent.py#L1426) | 1426 | `"            plan = {}"` | — |
| [SRC-1AE03B9EC3-L001427](../../agents/web_agent.py#L1427) | 1427 | `"            result[\"research_plan\"] = plan"` | — |
| [SRC-1AE03B9EC3-L001428](../../agents/web_agent.py#L1428) | 1428 | `"        plan[\"intent_route\"] = route"` | — |
| [SRC-1AE03B9EC3-L001429](../../agents/web_agent.py#L1429) | 1429 | `"        plan[\"intent_route_reason\"] = reason"` | — |
| [SRC-1AE03B9EC3-L001430](../../agents/web_agent.py#L1430) | 1430 | `"        plan[\"mode\"] = mode"` | — |
| [SRC-1AE03B9EC3-L001431](../../agents/web_agent.py#L1431) | 1431 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L001432](../../agents/web_agent.py#L1432) | 1432 | `""` | — |
| [SRC-1AE03B9EC3-L001433](../../agents/web_agent.py#L1433) | 1433 | `"    def _clarification_result("` | — |
| [SRC-1AE03B9EC3-L001434](../../agents/web_agent.py#L1434) | 1434 | `"        self, question: str, mode: str, decision: dict[str, Any]"` | — |
| [SRC-1AE03B9EC3-L001435](../../agents/web_agent.py#L1435) | 1435 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001436](../../agents/web_agent.py#L1436) | 1436 | `"        \"\"\"Return a bounded clarification result without starting web search.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001437](../../agents/web_agent.py#L1437) | 1437 | `"        if re.search(r\"[a-z]\", question.casefold()):"` | — |
| [SRC-1AE03B9EC3-L001438](../../agents/web_agent.py#L1438) | 1438 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001439](../../agents/web_agent.py#L1439) | 1439 | `"                \"What are you referring to? Please name the item or share its link, \""` | — |
| [SRC-1AE03B9EC3-L001440](../../agents/web_agent.py#L1440) | 1440 | `"                \"and I'll continue without guessing.\""` | — |
| [SRC-1AE03B9EC3-L001441](../../agents/web_agent.py#L1441) | 1441 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001442](../../agents/web_agent.py#L1442) | 1442 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001443](../../agents/web_agent.py#L1443) | 1443 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001444](../../agents/web_agent.py#L1444) | 1444 | `"                \"تقصد إيه تحديدًا؟ اكتب اسم الشيء أو المنتج المقصود، أو ابعت الرابط، \""` | — |
| [SRC-1AE03B9EC3-L001445](../../agents/web_agent.py#L1445) | 1445 | `"                \"وأكمل معاك من غير ما أخمّن.\""` | — |
| [SRC-1AE03B9EC3-L001446](../../agents/web_agent.py#L1446) | 1446 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001447](../../agents/web_agent.py#L1447) | 1447 | `"        result = self._local_answer_result(question, answer, \"clarification_needed\")"` | — |
| [SRC-1AE03B9EC3-L001448](../../agents/web_agent.py#L1448) | 1448 | `"        return self._annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L001449](../../agents/web_agent.py#L1449) | 1449 | `"            result, \"CLARIFY\", str(decision.get(\"reason\", \"missing_referent\")), mode"` | — |
| [SRC-1AE03B9EC3-L001450](../../agents/web_agent.py#L1450) | 1450 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001451](../../agents/web_agent.py#L1451) | 1451 | `""` | — |
| [SRC-1AE03B9EC3-L001452](../../agents/web_agent.py#L1452) | 1452 | `"    def _dialogue_clarification_result("` | — |
| [SRC-1AE03B9EC3-L001453](../../agents/web_agent.py#L1453) | 1453 | `"        self, question: str, mode: str, context: dict[str, Any], reason: str"` | — |
| [SRC-1AE03B9EC3-L001454](../../agents/web_agent.py#L1454) | 1454 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001455](../../agents/web_agent.py#L1455) | 1455 | `"        \"\"\"Expose why context resolution stopped and ask instead of guessing.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001456](../../agents/web_agent.py#L1456) | 1456 | `"        context = dict(context)"` | — |
| [SRC-1AE03B9EC3-L001457](../../agents/web_agent.py#L1457) | 1457 | `"        context[\"needs_clarification\"] = True"` | — |
| [SRC-1AE03B9EC3-L001458](../../agents/web_agent.py#L1458) | 1458 | `"        context[\"status\"] = \"needs_clarification\""` | — |
| [SRC-1AE03B9EC3-L001459](../../agents/web_agent.py#L1459) | 1459 | `"        context[\"resolved_question\"] = question[:MAX_QUESTION_CHARS]"` | — |
| [SRC-1AE03B9EC3-L001460](../../agents/web_agent.py#L1460) | 1460 | `"        context[\"resolution_basis\"] = \"insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L001461](../../agents/web_agent.py#L1461) | 1461 | `"        result = self._clarification_result("` | — |
| [SRC-1AE03B9EC3-L001462](../../agents/web_agent.py#L1462) | 1462 | `"            question, mode, {"` | — |
| [SRC-1AE03B9EC3-L001463](../../agents/web_agent.py#L1463) | 1463 | `"                \"reason\": reason,"` | — |
| [SRC-1AE03B9EC3-L001464](../../agents/web_agent.py#L1464) | 1464 | `"                \"needs_clarification\": True,"` | — |
| [SRC-1AE03B9EC3-L001465](../../agents/web_agent.py#L1465) | 1465 | `"                \"context_available\": bool(context.get(\"is_follow_up\")),"` | — |
| [SRC-1AE03B9EC3-L001466](../../agents/web_agent.py#L1466) | 1466 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001467](../../agents/web_agent.py#L1467) | 1467 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001468](../../agents/web_agent.py#L1468) | 1468 | `"        requested_clarification = context.get(\"clarification_question\")"` | — |
| [SRC-1AE03B9EC3-L001469](../../agents/web_agent.py#L1469) | 1469 | `"        if isinstance(requested_clarification, str) and requested_clarification.strip():"` | — |
| [SRC-1AE03B9EC3-L001470](../../agents/web_agent.py#L1470) | 1470 | `"            result[\"answer\"] = requested_clarification[:400]"` | — |
| [SRC-1AE03B9EC3-L001471](../../agents/web_agent.py#L1471) | 1471 | `"        result[\"dialogue_context\"] = context"` | — |
| [SRC-1AE03B9EC3-L001472](../../agents/web_agent.py#L1472) | 1472 | `"        if isinstance(result.get(\"research_plan\"), dict):"` | — |
| [SRC-1AE03B9EC3-L001473](../../agents/web_agent.py#L1473) | 1473 | `"            result[\"research_plan\"][\"dialogue_context\"] = context"` | — |
| [SRC-1AE03B9EC3-L001474](../../agents/web_agent.py#L1474) | 1474 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L001475](../../agents/web_agent.py#L1475) | 1475 | `""` | — |
| [SRC-1AE03B9EC3-L001476](../../agents/web_agent.py#L1476) | 1476 | `"    def _capability_status_snapshot(self) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001477](../../agents/web_agent.py#L1477) | 1477 | `"        \"\"\"Describe configured capabilities without claiming a live health check.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001478](../../agents/web_agent.py#L1478) | 1478 | `"        status = self.status()"` | — |
| [SRC-1AE03B9EC3-L001479](../../agents/web_agent.py#L1479) | 1479 | `"        not_tested = \"not_tested_in_this_response\""` | — |
| [SRC-1AE03B9EC3-L001480](../../agents/web_agent.py#L1480) | 1480 | `"        providers = ["` | — |
| [SRC-1AE03B9EC3-L001481](../../agents/web_agent.py#L1481) | 1481 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001482](../../agents/web_agent.py#L1482) | 1482 | `"                \"name\": \"duckduckgo_html\","` | — |
| [SRC-1AE03B9EC3-L001483](../../agents/web_agent.py#L1483) | 1483 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001484](../../agents/web_agent.py#L1484) | 1484 | `"                \"configuration_status\": \"built_in_no_api_key\","` | — |
| [SRC-1AE03B9EC3-L001485](../../agents/web_agent.py#L1485) | 1485 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001486](../../agents/web_agent.py#L1486) | 1486 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001487](../../agents/web_agent.py#L1487) | 1487 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001488](../../agents/web_agent.py#L1488) | 1488 | `"                \"name\": \"bing_rss\","` | — |
| [SRC-1AE03B9EC3-L001489](../../agents/web_agent.py#L1489) | 1489 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001490](../../agents/web_agent.py#L1490) | 1490 | `"                \"configuration_status\": \"built_in_no_api_key\","` | — |
| [SRC-1AE03B9EC3-L001491](../../agents/web_agent.py#L1491) | 1491 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001492](../../agents/web_agent.py#L1492) | 1492 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001493](../../agents/web_agent.py#L1493) | 1493 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001494](../../agents/web_agent.py#L1494) | 1494 | `"                \"name\": \"google_news_rss\","` | — |
| [SRC-1AE03B9EC3-L001495](../../agents/web_agent.py#L1495) | 1495 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001496](../../agents/web_agent.py#L1496) | 1496 | `"                \"configuration_status\": \"conditional_no_api_key\","` | — |
| [SRC-1AE03B9EC3-L001497](../../agents/web_agent.py#L1497) | 1497 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001498](../../agents/web_agent.py#L1498) | 1498 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001499](../../agents/web_agent.py#L1499) | 1499 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001500](../../agents/web_agent.py#L1500) | 1500 | `"                \"name\": \"deepseek_search_api\","` | — |
| [SRC-1AE03B9EC3-L001501](../../agents/web_agent.py#L1501) | 1501 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001502](../../agents/web_agent.py#L1502) | 1502 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L001503](../../agents/web_agent.py#L1503) | 1503 | `"                    \"configured\" if status.get(\"deepseek_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001504](../../agents/web_agent.py#L1504) | 1504 | `"                    else \"not_configured\""` | — |
| [SRC-1AE03B9EC3-L001505](../../agents/web_agent.py#L1505) | 1505 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001506](../../agents/web_agent.py#L1506) | 1506 | `"                \"runtime_status\": not_tested if status.get(\"deepseek_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001507](../../agents/web_agent.py#L1507) | 1507 | `"                else \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001508](../../agents/web_agent.py#L1508) | 1508 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001509](../../agents/web_agent.py#L1509) | 1509 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001510](../../agents/web_agent.py#L1510) | 1510 | `"                \"name\": \"brave_search_api\","` | — |
| [SRC-1AE03B9EC3-L001511](../../agents/web_agent.py#L1511) | 1511 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001512](../../agents/web_agent.py#L1512) | 1512 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L001513](../../agents/web_agent.py#L1513) | 1513 | `"                    \"configured\" if status.get(\"brave_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001514](../../agents/web_agent.py#L1514) | 1514 | `"                    else \"not_configured\""` | — |
| [SRC-1AE03B9EC3-L001515](../../agents/web_agent.py#L1515) | 1515 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001516](../../agents/web_agent.py#L1516) | 1516 | `"                \"runtime_status\": not_tested if status.get(\"brave_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001517](../../agents/web_agent.py#L1517) | 1517 | `"                else \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001518](../../agents/web_agent.py#L1518) | 1518 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001519](../../agents/web_agent.py#L1519) | 1519 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001520](../../agents/web_agent.py#L1520) | 1520 | `"                \"name\": \"tavily_search_api\","` | — |
| [SRC-1AE03B9EC3-L001521](../../agents/web_agent.py#L1521) | 1521 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001522](../../agents/web_agent.py#L1522) | 1522 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L001523](../../agents/web_agent.py#L1523) | 1523 | `"                    \"configured\" if status.get(\"tavily_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001524](../../agents/web_agent.py#L1524) | 1524 | `"                    else \"not_configured\""` | — |
| [SRC-1AE03B9EC3-L001525](../../agents/web_agent.py#L1525) | 1525 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001526](../../agents/web_agent.py#L1526) | 1526 | `"                \"runtime_status\": not_tested if status.get(\"tavily_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001527](../../agents/web_agent.py#L1527) | 1527 | `"                else \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001528](../../agents/web_agent.py#L1528) | 1528 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001529](../../agents/web_agent.py#L1529) | 1529 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001530](../../agents/web_agent.py#L1530) | 1530 | `"                \"name\": \"openrouter_web_search\","` | — |
| [SRC-1AE03B9EC3-L001531](../../agents/web_agent.py#L1531) | 1531 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001532](../../agents/web_agent.py#L1532) | 1532 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L001533](../../agents/web_agent.py#L1533) | 1533 | `"                    \"enabled\" if status.get(\"openrouter_web_search_enabled\")"` | — |
| [SRC-1AE03B9EC3-L001534](../../agents/web_agent.py#L1534) | 1534 | `"                    else \"disabled\""` | — |
| [SRC-1AE03B9EC3-L001535](../../agents/web_agent.py#L1535) | 1535 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001536](../../agents/web_agent.py#L1536) | 1536 | `"                \"runtime_status\": not_tested if status.get(\"openrouter_web_search_enabled\")"` | — |
| [SRC-1AE03B9EC3-L001537](../../agents/web_agent.py#L1537) | 1537 | `"                else \"disabled\","` | — |
| [SRC-1AE03B9EC3-L001538](../../agents/web_agent.py#L1538) | 1538 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001539](../../agents/web_agent.py#L1539) | 1539 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L001540](../../agents/web_agent.py#L1540) | 1540 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L001541](../../agents/web_agent.py#L1541) | 1541 | `"            \"web_search\": {"` | — |
| [SRC-1AE03B9EC3-L001542](../../agents/web_agent.py#L1542) | 1542 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001543](../../agents/web_agent.py#L1543) | 1543 | `"                \"local_dependencies_ready\": bool(status.get(\"web_search_ready\")),"` | — |
| [SRC-1AE03B9EC3-L001544](../../agents/web_agent.py#L1544) | 1544 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001545](../../agents/web_agent.py#L1545) | 1545 | `"                \"providers\": providers,"` | — |
| [SRC-1AE03B9EC3-L001546](../../agents/web_agent.py#L1546) | 1546 | `"                \"semantics\": ("` | — |
| [SRC-1AE03B9EC3-L001547](../../agents/web_agent.py#L1547) | 1547 | `"                    \"Configuration and installed dependencies do not prove that a live \""` | — |
| [SRC-1AE03B9EC3-L001548](../../agents/web_agent.py#L1548) | 1548 | `"                    \"network request will succeed.\""` | — |
| [SRC-1AE03B9EC3-L001549](../../agents/web_agent.py#L1549) | 1549 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001550](../../agents/web_agent.py#L1550) | 1550 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001551](../../agents/web_agent.py#L1551) | 1551 | `"            \"language_model\": {"` | — |
| [SRC-1AE03B9EC3-L001552](../../agents/web_agent.py#L1552) | 1552 | `"                \"configured\": bool(status.get(\"language_model_configured\")),"` | — |
| [SRC-1AE03B9EC3-L001553](../../agents/web_agent.py#L1553) | 1553 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001554](../../agents/web_agent.py#L1554) | 1554 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001555](../../agents/web_agent.py#L1555) | 1555 | `"        }"` | — |
| [SRC-1AE03B9EC3-L001556](../../agents/web_agent.py#L1556) | 1556 | `""` | — |
| [SRC-1AE03B9EC3-L001557](../../agents/web_agent.py#L1557) | 1557 | `"    def _self_description_answer(self, question: str) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001558](../../agents/web_agent.py#L1558) | 1558 | `"        \"\"\"Answer self/capability questions without inventing a live health result.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001559](../../agents/web_agent.py#L1559) | 1559 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L001560](../../agents/web_agent.py#L1560) | 1560 | `"        current_search_question = self._is_current_search_status_question(question)"` | — |
| [SRC-1AE03B9EC3-L001561](../../agents/web_agent.py#L1561) | 1561 | `""` | — |
| [SRC-1AE03B9EC3-L001562](../../agents/web_agent.py#L1562) | 1562 | `"        if current_search_question:"` | — |
| [SRC-1AE03B9EC3-L001563](../../agents/web_agent.py#L1563) | 1563 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001564](../../agents/web_agent.py#L1564) | 1564 | `"                \"لا، لم أنفّذ بحثًا حيًا للإجابة عن هذا السؤال تحديدًا؛ هذا السؤال عن \""` | — |
| [SRC-1AE03B9EC3-L001565](../../agents/web_agent.py#L1565) | 1565 | `"                \"طريقة عملي، ولذلك لم أبدأ بحث ويب في هذه الجولة. هذا لا يعني أن البحث \""` | — |
| [SRC-1AE03B9EC3-L001566](../../agents/web_agent.py#L1566) | 1566 | `"                \"غير متاح؛ عند تنفيذ طلب يحتاج إلى معلومات حديثة سأوضح هل جرت محاولة البحث، \""` | — |
| [SRC-1AE03B9EC3-L001567](../../agents/web_agent.py#L1567) | 1567 | `"                \"وما النتائج التي عادت، وما إذا اكتملت الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L001568](../../agents/web_agent.py#L1568) | 1568 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001569](../../agents/web_agent.py#L1569) | 1569 | `"            result = self._local_answer_result(question, answer, \"capability_answer\")"` | — |
| [SRC-1AE03B9EC3-L001570](../../agents/web_agent.py#L1570) | 1570 | `"            result[\"request_execution_status\"] = {"` | — |
| [SRC-1AE03B9EC3-L001571](../../agents/web_agent.py#L1571) | 1571 | `"                \"search_attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L001572](../../agents/web_agent.py#L1572) | 1572 | `"                \"search_outcome\": \"not_attempted\","` | — |
| [SRC-1AE03B9EC3-L001573](../../agents/web_agent.py#L1573) | 1573 | `"                \"semantics\": \"status_of_this_request_only\","` | — |
| [SRC-1AE03B9EC3-L001574](../../agents/web_agent.py#L1574) | 1574 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001575](../../agents/web_agent.py#L1575) | 1575 | `"            result[\"capability_status\"] = self._capability_status_snapshot()"` | — |
| [SRC-1AE03B9EC3-L001576](../../agents/web_agent.py#L1576) | 1576 | `"            return result"` | — |
| [SRC-1AE03B9EC3-L001577](../../agents/web_agent.py#L1577) | 1577 | `""` | — |
| [SRC-1AE03B9EC3-L001578](../../agents/web_agent.py#L1578) | 1578 | `"        capability_phrases = ("` | — |
| [SRC-1AE03B9EC3-L001579](../../agents/web_agent.py#L1579) | 1579 | `"            \"كيف تستطيع مساعدتي\", \"ازاي تقدر تساعدني\", \"ازاي ممكن تساعدني\","` | — |
| [SRC-1AE03B9EC3-L001580](../../agents/web_agent.py#L1580) | 1580 | `"            \"ماذا تستطيع ان تفعل\", \"ما الذي تستطيع فعله\", \"ايه اللي تقدر تعمله\","` | — |
| [SRC-1AE03B9EC3-L001581](../../agents/web_agent.py#L1581) | 1581 | `"            \"what can you do\", \"how can you help me\","` | — |
| [SRC-1AE03B9EC3-L001582](../../agents/web_agent.py#L1582) | 1582 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001583](../../agents/web_agent.py#L1583) | 1583 | `"        if any(term in value for term in capability_phrases):"` | — |
| [SRC-1AE03B9EC3-L001584](../../agents/web_agent.py#L1584) | 1584 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001585](../../agents/web_agent.py#L1585) | 1585 | `"                \"أقدر أساعدك في شرح الأسئلة ووضع خطط عملية، كما يتضمن Omarai مسارًا \""` | — |
| [SRC-1AE03B9EC3-L001586](../../agents/web_agent.py#L1586) | 1586 | `"                \"للبحث في الويب عند الحاجة إلى معلومات حديثة أو روابط أو مقارنة خيارات. \""` | — |
| [SRC-1AE03B9EC3-L001587](../../agents/web_agent.py#L1587) | 1587 | `"                \"سأوضح في كل مهمة ما إذا نُفذ البحث فعلًا وما المصادر التي أمكن جمعها، \""` | — |
| [SRC-1AE03B9EC3-L001588](../../agents/web_agent.py#L1588) | 1588 | `"                \"وما الذي لم يمكن التحقق منه. قد تعمل بعض الموصلات الاختيارية فقط عند \""` | — |
| [SRC-1AE03B9EC3-L001589](../../agents/web_agent.py#L1589) | 1589 | `"                \"ضبط إعداداتها، ولا أضمن الوصول إلى كل موقع أو إلى المجموعات والمنشورات \""` | — |
| [SRC-1AE03B9EC3-L001590](../../agents/web_agent.py#L1590) | 1590 | `"                \"الخاصة. لم أجرِ اختبار اتصال حي في هذه الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L001591](../../agents/web_agent.py#L1591) | 1591 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001592](../../agents/web_agent.py#L1592) | 1592 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001593](../../agents/web_agent.py#L1593) | 1593 | `"            status = self.status()"` | — |
| [SRC-1AE03B9EC3-L001594](../../agents/web_agent.py#L1594) | 1594 | `"            providers = [\"DuckDuckGo HTML\", \"Bing RSS\"]"` | — |
| [SRC-1AE03B9EC3-L001595](../../agents/web_agent.py#L1595) | 1595 | `"            providers.append(\"Google News RSS عند ملاءمة السؤال أو الحاجة إلى معلومات حديثة\")"` | — |
| [SRC-1AE03B9EC3-L001596](../../agents/web_agent.py#L1596) | 1596 | `"            if status.get(\"deepseek_search_api_configured\"):"` | — |
| [SRC-1AE03B9EC3-L001597](../../agents/web_agent.py#L1597) | 1597 | `"                providers.append("` | — |
| [SRC-1AE03B9EC3-L001598](../../agents/web_agent.py#L1598) | 1598 | `"                    \"DeepSeek Search API (مفتاحه مضبوط، لكنه غير مختبر في هذه الإجابة \""` | — |
| [SRC-1AE03B9EC3-L001599](../../agents/web_agent.py#L1599) | 1599 | `"                    \"وقد يستهلك استخدامًا مدفوعًا)\""` | — |
| [SRC-1AE03B9EC3-L001600](../../agents/web_agent.py#L1600) | 1600 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001601](../../agents/web_agent.py#L1601) | 1601 | `"            if status.get(\"brave_search_api_configured\"):"` | — |
| [SRC-1AE03B9EC3-L001602](../../agents/web_agent.py#L1602) | 1602 | `"                providers.append(\"Brave Search API (الإعداد موجود، وليس دليلًا على نجاح الاتصال)\")"` | — |
| [SRC-1AE03B9EC3-L001603](../../agents/web_agent.py#L1603) | 1603 | `"            if status.get(\"tavily_search_api_configured\"):"` | — |
| [SRC-1AE03B9EC3-L001604](../../agents/web_agent.py#L1604) | 1604 | `"                providers.append(\"Tavily Search API (الإعداد موجود، وليس دليلًا على نجاح الاتصال)\")"` | — |
| [SRC-1AE03B9EC3-L001605](../../agents/web_agent.py#L1605) | 1605 | `"            if status.get(\"openrouter_web_search_enabled\"):"` | — |
| [SRC-1AE03B9EC3-L001606](../../agents/web_agent.py#L1606) | 1606 | `"                providers.append(\"بحث OpenRouter المباشر (مفعّل بالإعداد، وقد يستهلك رصيدًا)\")"` | — |
| [SRC-1AE03B9EC3-L001607](../../agents/web_agent.py#L1607) | 1607 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001608](../../agents/web_agent.py#L1608) | 1608 | `"                \"بحسب الكود الحالي، يتضمن Omarai مسار بحث ويب يستخدم: \""` | — |
| [SRC-1AE03B9EC3-L001609](../../agents/web_agent.py#L1609) | 1609 | `"                + \"، \".join(providers)"` | — |
| [SRC-1AE03B9EC3-L001610](../../agents/web_agent.py#L1610) | 1610 | `"                + \". هذه قائمة بالموصلات المضمّنة أو المهيأة، وليست إثباتًا بأنها نجحت \""` | — |
| [SRC-1AE03B9EC3-L001611](../../agents/web_agent.py#L1611) | 1611 | `"                \"في هذه اللحظة. لم أنفّذ اختبار اتصال حي في هذه الإجابة، لذلك لا أستطيع \""` | — |
| [SRC-1AE03B9EC3-L001612](../../agents/web_agent.py#L1612) | 1612 | `"                \"تأكيد توافر الشبكة الآن. عند طلب بحث فعلي، ينبغي أن يوضح التقرير ما إذا \""` | — |
| [SRC-1AE03B9EC3-L001613](../../agents/web_agent.py#L1613) | 1613 | `"                \"بدأت المحاولة، وما الموصلات التي أعادت نتائج، وما الصفحات التي أمكن قراءة \""` | — |
| [SRC-1AE03B9EC3-L001614](../../agents/web_agent.py#L1614) | 1614 | `"                \"محتواها. لا يوجد وصول مضمون إلى كل الإنترنت أو إلى المحتوى الخاص.\""` | — |
| [SRC-1AE03B9EC3-L001615](../../agents/web_agent.py#L1615) | 1615 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001616](../../agents/web_agent.py#L1616) | 1616 | `"        result = self._local_answer_result(question, answer, \"capability_answer\")"` | — |
| [SRC-1AE03B9EC3-L001617](../../agents/web_agent.py#L1617) | 1617 | `"        result[\"capability_status\"] = self._capability_status_snapshot()"` | — |
| [SRC-1AE03B9EC3-L001618](../../agents/web_agent.py#L1618) | 1618 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L001619](../../agents/web_agent.py#L1619) | 1619 | `""` | — |
| [SRC-1AE03B9EC3-L001620](../../agents/web_agent.py#L1620) | 1620 | `"    def _answer_without_search("` | — |
| [SRC-1AE03B9EC3-L001621](../../agents/web_agent.py#L1621) | 1621 | `"        self, question: str, history: list[dict[str, str]]"` | — |
| [SRC-1AE03B9EC3-L001622](../../agents/web_agent.py#L1622) | 1622 | `"    ) -> dict[str, Any] \| None:"` | — |
| [SRC-1AE03B9EC3-L001623](../../agents/web_agent.py#L1623) | 1623 | `"        \"\"\"Answer stable informational questions with the configured LLM, without fake citations.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001624](../../agents/web_agent.py#L1624) | 1624 | `"        if not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L001625](../../agents/web_agent.py#L1625) | 1625 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L001626](../../agents/web_agent.py#L1626) | 1626 | `"        messages: list[dict[str, str]] = ["` | — |
| [SRC-1AE03B9EC3-L001627](../../agents/web_agent.py#L1627) | 1627 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001628](../../agents/web_agent.py#L1628) | 1628 | `"                \"role\": \"system\","` | — |
| [SRC-1AE03B9EC3-L001629](../../agents/web_agent.py#L1629) | 1629 | `"                \"content\": ("` | — |
| [SRC-1AE03B9EC3-L001630](../../agents/web_agent.py#L1630) | 1630 | `"                    \"أنت Omarai، مساعد عربي عملي. أجب مباشرة وباللغة التي استخدمها الشخص، \""` | — |
| [SRC-1AE03B9EC3-L001631](../../agents/web_agent.py#L1631) | 1631 | `"                    \"وافهم المقصود حتى لو كان باللهجة المصرية أو به أخطاء كتابية. هذا المسار \""` | — |
| [SRC-1AE03B9EC3-L001632](../../agents/web_agent.py#L1632) | 1632 | `"                    \"للشرح والمعرفة العامة والأسئلة الحوارية غير المعتمدة على معلومات لحظية. \""` | — |
| [SRC-1AE03B9EC3-L001633](../../agents/web_agent.py#L1633) | 1633 | `"                    \"لا تستخدم أدوات الويب ولا تقل إنك بحثت أو تحققت من مصدر. لا تختلق أرقامًا \""` | — |
| [SRC-1AE03B9EC3-L001634](../../agents/web_agent.py#L1634) | 1634 | `"                    \"أو اقتباسات أو روابط. إذا كان جزء من السؤال يتطلب بيانات حديثة أو تحققًا \""` | — |
| [SRC-1AE03B9EC3-L001635](../../agents/web_agent.py#L1635) | 1635 | `"                    \"خارجيًا، صرّح بذلك بدل الجزم. وضّح عدم اليقين بإيجاز، وأعط إجابة مفيدة \""` | — |
| [SRC-1AE03B9EC3-L001636](../../agents/web_agent.py#L1636) | 1636 | `"                    \"من غير إطالة أو سلسلة تفكير داخلية.\""` | — |
| [SRC-1AE03B9EC3-L001637](../../agents/web_agent.py#L1637) | 1637 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001638](../../agents/web_agent.py#L1638) | 1638 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001639](../../agents/web_agent.py#L1639) | 1639 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L001640](../../agents/web_agent.py#L1640) | 1640 | `"        messages.extend(history[-MAX_HISTORY_ITEMS:])"` | — |
| [SRC-1AE03B9EC3-L001641](../../agents/web_agent.py#L1641) | 1641 | `"        messages.append({\"role\": \"user\", \"content\": question})"` | — |
| [SRC-1AE03B9EC3-L001642](../../agents/web_agent.py#L1642) | 1642 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001643](../../agents/web_agent.py#L1643) | 1643 | `"            answer = self._request_completion("` | — |
| [SRC-1AE03B9EC3-L001644](../../agents/web_agent.py#L1644) | 1644 | `"                messages,"` | — |
| [SRC-1AE03B9EC3-L001645](../../agents/web_agent.py#L1645) | 1645 | `"                max_tokens=1500,"` | — |
| [SRC-1AE03B9EC3-L001646](../../agents/web_agent.py#L1646) | 1646 | `"                temperature=0.2,"` | — |
| [SRC-1AE03B9EC3-L001647](../../agents/web_agent.py#L1647) | 1647 | `"                timeout=self._effective_timeout(min(self.timeout, 28)),"` | — |
| [SRC-1AE03B9EC3-L001648](../../agents/web_agent.py#L1648) | 1648 | `"                model=self.answer_model,"` | — |
| [SRC-1AE03B9EC3-L001649](../../agents/web_agent.py#L1649) | 1649 | `"                enable_web_search=False,"` | — |
| [SRC-1AE03B9EC3-L001650](../../agents/web_agent.py#L1650) | 1650 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001651](../../agents/web_agent.py#L1651) | 1651 | `"        except (RuntimeError, AgentDependencyError):"` | — |
| [SRC-1AE03B9EC3-L001652](../../agents/web_agent.py#L1652) | 1652 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L001653](../../agents/web_agent.py#L1653) | 1653 | `"        # Never turn an overlong completion into a seemingly complete answer by slicing it."` | — |
| [SRC-1AE03B9EC3-L001654](../../agents/web_agent.py#L1654) | 1654 | `"        if len(answer) > 24_000:"` | — |
| [SRC-1AE03B9EC3-L001655](../../agents/web_agent.py#L1655) | 1655 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L001656](../../agents/web_agent.py#L1656) | 1656 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L001657](../../agents/web_agent.py#L1657) | 1657 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L001658](../../agents/web_agent.py#L1658) | 1658 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L001659](../../agents/web_agent.py#L1659) | 1659 | `"            \"search_query\": question,"` | — |
| [SRC-1AE03B9EC3-L001660](../../agents/web_agent.py#L1660) | 1660 | `"            \"search_queries\": [],"` | — |
| [SRC-1AE03B9EC3-L001661](../../agents/web_agent.py#L1661) | 1661 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L001662](../../agents/web_agent.py#L1662) | 1662 | `"                \"mode\": \"auto\","` | — |
| [SRC-1AE03B9EC3-L001663](../../agents/web_agent.py#L1663) | 1663 | `"                \"planning_method\": \"general_qa_without_web\","` | — |
| [SRC-1AE03B9EC3-L001664](../../agents/web_agent.py#L1664) | 1664 | `"                \"web_search_skipped\": True,"` | — |
| [SRC-1AE03B9EC3-L001665](../../agents/web_agent.py#L1665) | 1665 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001666](../../agents/web_agent.py#L1666) | 1666 | `"            \"sources\": [],"` | — |
| [SRC-1AE03B9EC3-L001667](../../agents/web_agent.py#L1667) | 1667 | `"            \"used_language_model\": True,"` | — |
| [SRC-1AE03B9EC3-L001668](../../agents/web_agent.py#L1668) | 1668 | `"            \"used_web_search\": False,"` | — |
| [SRC-1AE03B9EC3-L001669](../../agents/web_agent.py#L1669) | 1669 | `"            \"search_attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L001670](../../agents/web_agent.py#L1670) | 1670 | `"            \"used_social_search\": False,"` | — |
| [SRC-1AE03B9EC3-L001671](../../agents/web_agent.py#L1671) | 1671 | `"            \"warnings\": [],"` | — |
| [SRC-1AE03B9EC3-L001672](../../agents/web_agent.py#L1672) | 1672 | `"            \"kind\": \"general_answer\","` | — |
| [SRC-1AE03B9EC3-L001673](../../agents/web_agent.py#L1673) | 1673 | `"            \"research_quality\": \"not_applicable\","` | — |
| [SRC-1AE03B9EC3-L001674](../../agents/web_agent.py#L1674) | 1674 | `"            \"model_calls\": list(self.model_usage),"` | — |
| [SRC-1AE03B9EC3-L001675](../../agents/web_agent.py#L1675) | 1675 | `"        }"` | — |
| [SRC-1AE03B9EC3-L001676](../../agents/web_agent.py#L1676) | 1676 | `""` | — |
| [SRC-1AE03B9EC3-L001677](../../agents/web_agent.py#L1677) | 1677 | `"    def _search_duckduckgo_html(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001678](../../agents/web_agent.py#L1678) | 1678 | `""` | — |
| [SRC-1AE03B9EC3-L001679](../../agents/web_agent.py#L1679) | 1679 | `"        from bs4 import BeautifulSoup"` | — |
| [SRC-1AE03B9EC3-L001680](../../agents/web_agent.py#L1680) | 1680 | `""` | — |
| [SRC-1AE03B9EC3-L001681](../../agents/web_agent.py#L1681) | 1681 | `"        response = _bounded_http_request(\"GET\", "` | — |
| [SRC-1AE03B9EC3-L001682](../../agents/web_agent.py#L1682) | 1682 | `"            \"https://html.duckduckgo.com/html/\","` | — |
| [SRC-1AE03B9EC3-L001683](../../agents/web_agent.py#L1683) | 1683 | `"            params={\"q\": query},"` | — |
| [SRC-1AE03B9EC3-L001684](../../agents/web_agent.py#L1684) | 1684 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001685](../../agents/web_agent.py#L1685) | 1685 | `"                \"User-Agent\": ("` | — |
| [SRC-1AE03B9EC3-L001686](../../agents/web_agent.py#L1686) | 1686 | `"                    \"Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 \""` | — |
| [SRC-1AE03B9EC3-L001687](../../agents/web_agent.py#L1687) | 1687 | `"                    \"(KHTML, like Gecko) Chrome/124.0 Mobile Safari/537.36\""` | — |
| [SRC-1AE03B9EC3-L001688](../../agents/web_agent.py#L1688) | 1688 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001689](../../agents/web_agent.py#L1689) | 1689 | `"                \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001690](../../agents/web_agent.py#L1690) | 1690 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001691](../../agents/web_agent.py#L1691) | 1691 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001692](../../agents/web_agent.py#L1692) | 1692 | `"            # Search provider redirects are not followed automatically. A 3xx is"` | — |
| [SRC-1AE03B9EC3-L001693](../../agents/web_agent.py#L1693) | 1693 | `"            # reported as a provider failure so the host never fetches an unchecked target."` | — |
| [SRC-1AE03B9EC3-L001694](../../agents/web_agent.py#L1694) | 1694 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001695](../../agents/web_agent.py#L1695) | 1695 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001696](../../agents/web_agent.py#L1696) | 1696 | `"        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001697](../../agents/web_agent.py#L1697) | 1697 | `"            raise RuntimeError(f\"HTTP {response.status_code}\")"` | — |
| [SRC-1AE03B9EC3-L001698](../../agents/web_agent.py#L1698) | 1698 | `"        soup = BeautifulSoup(response.text, \"html.parser\")"` | — |
| [SRC-1AE03B9EC3-L001699](../../agents/web_agent.py#L1699) | 1699 | `"        if soup.select_one(\"form#challenge-form, #challenge-form, .anomaly-modal\"):"` | — |
| [SRC-1AE03B9EC3-L001700](../../agents/web_agent.py#L1700) | 1700 | `"            raise RuntimeError(\"anti-bot challenge returned\")"` | — |
| [SRC-1AE03B9EC3-L001701](../../agents/web_agent.py#L1701) | 1701 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001702](../../agents/web_agent.py#L1702) | 1702 | `"        for card in soup.select(\"div.result\"):"` | — |
| [SRC-1AE03B9EC3-L001703](../../agents/web_agent.py#L1703) | 1703 | `"            link = card.select_one(\"a.result__a\")"` | — |
| [SRC-1AE03B9EC3-L001704](../../agents/web_agent.py#L1704) | 1704 | `"            if not link:"` | — |
| [SRC-1AE03B9EC3-L001705](../../agents/web_agent.py#L1705) | 1705 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001706](../../agents/web_agent.py#L1706) | 1706 | `"            url = _public_http_url(self._unwrap_search_url(str(link.get(\"href\", \"\"))))"` | — |
| [SRC-1AE03B9EC3-L001707](../../agents/web_agent.py#L1707) | 1707 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001708](../../agents/web_agent.py#L1708) | 1708 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001709](../../agents/web_agent.py#L1709) | 1709 | `"            snippet_node = card.select_one(\".result__snippet\")"` | — |
| [SRC-1AE03B9EC3-L001710](../../agents/web_agent.py#L1710) | 1710 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001711](../../agents/web_agent.py#L1711) | 1711 | `"                \"title\": _clean_text(link.get_text(\" \", strip=True), 300),"` | — |
| [SRC-1AE03B9EC3-L001712](../../agents/web_agent.py#L1712) | 1712 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001713](../../agents/web_agent.py#L1713) | 1713 | `"                \"snippet\": _clean_text("` | — |
| [SRC-1AE03B9EC3-L001714](../../agents/web_agent.py#L1714) | 1714 | `"                    snippet_node.get_text(\" \", strip=True) if snippet_node else \"\", 1200"` | — |
| [SRC-1AE03B9EC3-L001715](../../agents/web_agent.py#L1715) | 1715 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001716](../../agents/web_agent.py#L1716) | 1716 | `"                \"provider\": \"duckduckgo_html\","` | — |
| [SRC-1AE03B9EC3-L001717](../../agents/web_agent.py#L1717) | 1717 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001718](../../agents/web_agent.py#L1718) | 1718 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001719](../../agents/web_agent.py#L1719) | 1719 | `"                \"published_at\": \"\","` | — |
| [SRC-1AE03B9EC3-L001720](../../agents/web_agent.py#L1720) | 1720 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001721](../../agents/web_agent.py#L1721) | 1721 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001722](../../agents/web_agent.py#L1722) | 1722 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001723](../../agents/web_agent.py#L1723) | 1723 | `"        if not rows and (\"captcha\" in response.text.casefold() or \"anomaly\" in response.text.casefold()):"` | — |
| [SRC-1AE03B9EC3-L001724](../../agents/web_agent.py#L1724) | 1724 | `"            raise RuntimeError(\"anti-bot challenge returned no result cards\")"` | — |
| [SRC-1AE03B9EC3-L001725](../../agents/web_agent.py#L1725) | 1725 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001726](../../agents/web_agent.py#L1726) | 1726 | `""` | — |
| [SRC-1AE03B9EC3-L001727](../../agents/web_agent.py#L1727) | 1727 | `"    def _search_bing_rss(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001728](../../agents/web_agent.py#L1728) | 1728 | `"        import xml.etree.ElementTree as ET"` | — |
| [SRC-1AE03B9EC3-L001729](../../agents/web_agent.py#L1729) | 1729 | `""` | — |
| [SRC-1AE03B9EC3-L001730](../../agents/web_agent.py#L1730) | 1730 | `"        response = _bounded_http_request(\"GET\", "` | — |
| [SRC-1AE03B9EC3-L001731](../../agents/web_agent.py#L1731) | 1731 | `"            \"https://www.bing.com/search\","` | — |
| [SRC-1AE03B9EC3-L001732](../../agents/web_agent.py#L1732) | 1732 | `"            params={\"format\": \"rss\", \"q\": query},"` | — |
| [SRC-1AE03B9EC3-L001733](../../agents/web_agent.py#L1733) | 1733 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001734](../../agents/web_agent.py#L1734) | 1734 | `"                \"User-Agent\": ("` | — |
| [SRC-1AE03B9EC3-L001735](../../agents/web_agent.py#L1735) | 1735 | `"                    \"Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 \""` | — |
| [SRC-1AE03B9EC3-L001736](../../agents/web_agent.py#L1736) | 1736 | `"                    \"(KHTML, like Gecko) Chrome/124.0 Mobile Safari/537.36\""` | — |
| [SRC-1AE03B9EC3-L001737](../../agents/web_agent.py#L1737) | 1737 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001738](../../agents/web_agent.py#L1738) | 1738 | `"                \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001739](../../agents/web_agent.py#L1739) | 1739 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001740](../../agents/web_agent.py#L1740) | 1740 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001741](../../agents/web_agent.py#L1741) | 1741 | `"            # Refuse automatic redirects from public search endpoints; never fetch an"` | — |
| [SRC-1AE03B9EC3-L001742](../../agents/web_agent.py#L1742) | 1742 | `"            # unchecked redirect target as part of a provider search request."` | — |
| [SRC-1AE03B9EC3-L001743](../../agents/web_agent.py#L1743) | 1743 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001744](../../agents/web_agent.py#L1744) | 1744 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001745](../../agents/web_agent.py#L1745) | 1745 | `"        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001746](../../agents/web_agent.py#L1746) | 1746 | `"            raise RuntimeError(f\"HTTP {response.status_code}\")"` | — |
| [SRC-1AE03B9EC3-L001747](../../agents/web_agent.py#L1747) | 1747 | `"        root = ET.fromstring(response.content)"` | — |
| [SRC-1AE03B9EC3-L001748](../../agents/web_agent.py#L1748) | 1748 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001749](../../agents/web_agent.py#L1749) | 1749 | `"        for item in root.iter():"` | — |
| [SRC-1AE03B9EC3-L001750](../../agents/web_agent.py#L1750) | 1750 | `"            if item.tag.rsplit(\"}\", 1)[-1] != \"item\":"` | — |
| [SRC-1AE03B9EC3-L001751](../../agents/web_agent.py#L1751) | 1751 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001752](../../agents/web_agent.py#L1752) | 1752 | `"            fields = {"` | — |
| [SRC-1AE03B9EC3-L001753](../../agents/web_agent.py#L1753) | 1753 | `"                child.tag.rsplit(\"}\", 1)[-1]: (child.text or \"\")"` | — |
| [SRC-1AE03B9EC3-L001754](../../agents/web_agent.py#L1754) | 1754 | `"                for child in item"` | — |
| [SRC-1AE03B9EC3-L001755](../../agents/web_agent.py#L1755) | 1755 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001756](../../agents/web_agent.py#L1756) | 1756 | `"            url = _public_http_url(fields.get(\"link\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001757](../../agents/web_agent.py#L1757) | 1757 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001758](../../agents/web_agent.py#L1758) | 1758 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001759](../../agents/web_agent.py#L1759) | 1759 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001760](../../agents/web_agent.py#L1760) | 1760 | `"                \"title\": _clean_text(fields.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001761](../../agents/web_agent.py#L1761) | 1761 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001762](../../agents/web_agent.py#L1762) | 1762 | `"                \"snippet\": _clean_text(fields.get(\"description\", \"\"), 1200),"` | — |
| [SRC-1AE03B9EC3-L001763](../../agents/web_agent.py#L1763) | 1763 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-1AE03B9EC3-L001764](../../agents/web_agent.py#L1764) | 1764 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001765](../../agents/web_agent.py#L1765) | 1765 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001766](../../agents/web_agent.py#L1766) | 1766 | `"                \"published_at\": _clean_text(fields.get(\"pubDate\", \"\"), 80),"` | — |
| [SRC-1AE03B9EC3-L001767](../../agents/web_agent.py#L1767) | 1767 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001768](../../agents/web_agent.py#L1768) | 1768 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001769](../../agents/web_agent.py#L1769) | 1769 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001770](../../agents/web_agent.py#L1770) | 1770 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001771](../../agents/web_agent.py#L1771) | 1771 | `""` | — |
| [SRC-1AE03B9EC3-L001772](../../agents/web_agent.py#L1772) | 1772 | `"    def _search_deepseek_api(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001773](../../agents/web_agent.py#L1773) | 1773 | `"        \"\"\"Use DeepSeek's optional Search API as a comparison provider, never by default.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001774](../../agents/web_agent.py#L1774) | 1774 | `"        api_key = os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001775](../../agents/web_agent.py#L1775) | 1775 | `"        if not api_key:"` | — |
| [SRC-1AE03B9EC3-L001776](../../agents/web_agent.py#L1776) | 1776 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001777](../../agents/web_agent.py#L1777) | 1777 | `""` | — |
| [SRC-1AE03B9EC3-L001778](../../agents/web_agent.py#L1778) | 1778 | `"        response = _bounded_http_request(\"POST\", "` | — |
| [SRC-1AE03B9EC3-L001779](../../agents/web_agent.py#L1779) | 1779 | `"            \"https://api.deepseek.com/v1/tools/search\","` | — |
| [SRC-1AE03B9EC3-L001780](../../agents/web_agent.py#L1780) | 1780 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001781](../../agents/web_agent.py#L1781) | 1781 | `"                \"Authorization\": \"Bearer \" + api_key,"` | — |
| [SRC-1AE03B9EC3-L001782](../../agents/web_agent.py#L1782) | 1782 | `"                \"Content-Type\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001783](../../agents/web_agent.py#L1783) | 1783 | `"                \"Accept\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001784](../../agents/web_agent.py#L1784) | 1784 | `"                \"User-Agent\": \"OmaraiResearchAgent/1.0\","` | — |
| [SRC-1AE03B9EC3-L001785](../../agents/web_agent.py#L1785) | 1785 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001786](../../agents/web_agent.py#L1786) | 1786 | `"            json={"` | — |
| [SRC-1AE03B9EC3-L001787](../../agents/web_agent.py#L1787) | 1787 | `"                \"query\": _normalize_search_query(query)[:128] or \"public web search\","` | — |
| [SRC-1AE03B9EC3-L001788](../../agents/web_agent.py#L1788) | 1788 | `"                \"count\": min(MAX_PROVIDER_RESULTS, 10),"` | — |
| [SRC-1AE03B9EC3-L001789](../../agents/web_agent.py#L1789) | 1789 | `"                \"need_content\": False,"` | — |
| [SRC-1AE03B9EC3-L001790](../../agents/web_agent.py#L1790) | 1790 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001791](../../agents/web_agent.py#L1791) | 1791 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001792](../../agents/web_agent.py#L1792) | 1792 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001793](../../agents/web_agent.py#L1793) | 1793 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001794](../../agents/web_agent.py#L1794) | 1794 | `"        response.raise_for_status()"` | — |
| [SRC-1AE03B9EC3-L001795](../../agents/web_agent.py#L1795) | 1795 | `"        payload = response.json()"` | — |
| [SRC-1AE03B9EC3-L001796](../../agents/web_agent.py#L1796) | 1796 | `"        results = payload.get(\"results\", []) if isinstance(payload, dict) else []"` | — |
| [SRC-1AE03B9EC3-L001797](../../agents/web_agent.py#L1797) | 1797 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001798](../../agents/web_agent.py#L1798) | 1798 | `"        for item in results if isinstance(results, list) else []:"` | — |
| [SRC-1AE03B9EC3-L001799](../../agents/web_agent.py#L1799) | 1799 | `"            if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L001800](../../agents/web_agent.py#L1800) | 1800 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001801](../../agents/web_agent.py#L1801) | 1801 | `"            url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001802](../../agents/web_agent.py#L1802) | 1802 | `"            if not url or _blocked_source_url(url):"` | — |
| [SRC-1AE03B9EC3-L001803](../../agents/web_agent.py#L1803) | 1803 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001804](../../agents/web_agent.py#L1804) | 1804 | `"            title = _clean_text(item.get(\"title\", \"\"), 300)"` | — |
| [SRC-1AE03B9EC3-L001805](../../agents/web_agent.py#L1805) | 1805 | `"            summary = item.get(\"summary\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001806](../../agents/web_agent.py#L1806) | 1806 | `"            snippet = item.get(\"snippet\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001807](../../agents/web_agent.py#L1807) | 1807 | `"            if isinstance(summary, str) and summary.strip():"` | — |
| [SRC-1AE03B9EC3-L001808](../../agents/web_agent.py#L1808) | 1808 | `"                snippet = summary"` | — |
| [SRC-1AE03B9EC3-L001809](../../agents/web_agent.py#L1809) | 1809 | `"            if not title or not isinstance(snippet, str) or not snippet.strip():"` | — |
| [SRC-1AE03B9EC3-L001810](../../agents/web_agent.py#L1810) | 1810 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001811](../../agents/web_agent.py#L1811) | 1811 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001812](../../agents/web_agent.py#L1812) | 1812 | `"                \"title\": title,"` | — |
| [SRC-1AE03B9EC3-L001813](../../agents/web_agent.py#L1813) | 1813 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001814](../../agents/web_agent.py#L1814) | 1814 | `"                \"snippet\": _clean_text(snippet, 1600),"` | — |
| [SRC-1AE03B9EC3-L001815](../../agents/web_agent.py#L1815) | 1815 | `"                \"provider\": \"deepseek_search_api\","` | — |
| [SRC-1AE03B9EC3-L001816](../../agents/web_agent.py#L1816) | 1816 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001817](../../agents/web_agent.py#L1817) | 1817 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001818](../../agents/web_agent.py#L1818) | 1818 | `"                \"published_at\": _clean_text(item.get(\"date\", \"\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L001819](../../agents/web_agent.py#L1819) | 1819 | `"                \"publisher_name\": _clean_text(item.get(\"site_name\", \"\") or \"\", 200),"` | — |
| [SRC-1AE03B9EC3-L001820](../../agents/web_agent.py#L1820) | 1820 | `"                \"provider_rerank_score\": item.get(\"rerank_score\"),"` | — |
| [SRC-1AE03B9EC3-L001821](../../agents/web_agent.py#L1821) | 1821 | `"                \"provider_authority_tier\": item.get(\"authority\"),"` | — |
| [SRC-1AE03B9EC3-L001822](../../agents/web_agent.py#L1822) | 1822 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001823](../../agents/web_agent.py#L1823) | 1823 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001824](../../agents/web_agent.py#L1824) | 1824 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001825](../../agents/web_agent.py#L1825) | 1825 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001826](../../agents/web_agent.py#L1826) | 1826 | `""` | — |
| [SRC-1AE03B9EC3-L001827](../../agents/web_agent.py#L1827) | 1827 | `"    def _reset_deepseek_search_budget(self) -> None:"` | — |
| [SRC-1AE03B9EC3-L001828](../../agents/web_agent.py#L1828) | 1828 | `"        \"\"\"Reset the bounded optional Search API request budget for one operation.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001829](../../agents/web_agent.py#L1829) | 1829 | `"        with self._deepseek_budget_lock:"` | — |
| [SRC-1AE03B9EC3-L001830](../../agents/web_agent.py#L1830) | 1830 | `"            self._deepseek_search_requests_reserved = 0"` | — |
| [SRC-1AE03B9EC3-L001831](../../agents/web_agent.py#L1831) | 1831 | `""` | — |
| [SRC-1AE03B9EC3-L001832](../../agents/web_agent.py#L1832) | 1832 | `"    def _reserve_deepseek_search_request(self) -> bool:"` | — |
| [SRC-1AE03B9EC3-L001833](../../agents/web_agent.py#L1833) | 1833 | `"        \"\"\"Reserve one paid search request before concurrent queries invoke the provider.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001834](../../agents/web_agent.py#L1834) | 1834 | `"        if not os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001835](../../agents/web_agent.py#L1835) | 1835 | `"            return False"` | — |
| [SRC-1AE03B9EC3-L001836](../../agents/web_agent.py#L1836) | 1836 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001837](../../agents/web_agent.py#L1837) | 1837 | `"            configured_budget = int("` | — |
| [SRC-1AE03B9EC3-L001838](../../agents/web_agent.py#L1838) | 1838 | `"                os.getenv(\"OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET\", \"1\").strip()"` | — |
| [SRC-1AE03B9EC3-L001839](../../agents/web_agent.py#L1839) | 1839 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001840](../../agents/web_agent.py#L1840) | 1840 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L001841](../../agents/web_agent.py#L1841) | 1841 | `"            configured_budget = 1"` | — |
| [SRC-1AE03B9EC3-L001842](../../agents/web_agent.py#L1842) | 1842 | `"        budget = max(0, min(configured_budget, 3))"` | — |
| [SRC-1AE03B9EC3-L001843](../../agents/web_agent.py#L1843) | 1843 | `"        with self._deepseek_budget_lock:"` | — |
| [SRC-1AE03B9EC3-L001844](../../agents/web_agent.py#L1844) | 1844 | `"            if self._deepseek_search_requests_reserved >= budget:"` | — |
| [SRC-1AE03B9EC3-L001845](../../agents/web_agent.py#L1845) | 1845 | `"                return False"` | — |
| [SRC-1AE03B9EC3-L001846](../../agents/web_agent.py#L1846) | 1846 | `"            self._deepseek_search_requests_reserved += 1"` | — |
| [SRC-1AE03B9EC3-L001847](../../agents/web_agent.py#L1847) | 1847 | `"            return True"` | — |
| [SRC-1AE03B9EC3-L001848](../../agents/web_agent.py#L1848) | 1848 | `""` | — |
| [SRC-1AE03B9EC3-L001849](../../agents/web_agent.py#L1849) | 1849 | `"    def _search_web(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001850](../../agents/web_agent.py#L1850) | 1850 | `"        \"\"\"Run configured search connectors concurrently with isolated failures and relevance checks.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001851](../../agents/web_agent.py#L1851) | 1851 | `"        from agents.research import detect_freshness"` | — |
| [SRC-1AE03B9EC3-L001852](../../agents/web_agent.py#L1852) | 1852 | `""` | — |
| [SRC-1AE03B9EC3-L001853](../../agents/web_agent.py#L1853) | 1853 | `"        query = compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L001854](../../agents/web_agent.py#L1854) | 1854 | `"        if not query:"` | — |
| [SRC-1AE03B9EC3-L001855](../../agents/web_agent.py#L1855) | 1855 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001856](../../agents/web_agent.py#L1856) | 1856 | `"        search_query = _normalize_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L001857](../../agents/web_agent.py#L1857) | 1857 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L001858](../../agents/web_agent.py#L1858) | 1858 | `"        if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L001859](../../agents/web_agent.py#L1859) | 1859 | `"            budget.reserve(\"search_queries\")"` | — |
| [SRC-1AE03B9EC3-L001860](../../agents/web_agent.py#L1860) | 1860 | `"        adapters: list[tuple[str, Any]] = ["` | — |
| [SRC-1AE03B9EC3-L001861](../../agents/web_agent.py#L1861) | 1861 | `"            (\"duckduckgo_html\", self._search_duckduckgo_html),"` | — |
| [SRC-1AE03B9EC3-L001862](../../agents/web_agent.py#L1862) | 1862 | `"            (\"bing_rss\", self._search_bing_rss),"` | — |
| [SRC-1AE03B9EC3-L001863](../../agents/web_agent.py#L1863) | 1863 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L001864](../../agents/web_agent.py#L1864) | 1864 | `"        if not getattr(self, \"allow_optional_providers\", True):"` | — |
| [SRC-1AE03B9EC3-L001865](../../agents/web_agent.py#L1865) | 1865 | `"            for provider in (\"deepseek_search_api\", \"brave_search_api\", \"tavily_search_api\"):"` | — |
| [SRC-1AE03B9EC3-L001866](../../agents/web_agent.py#L1866) | 1866 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001867](../../agents/web_agent.py#L1867) | 1867 | `"                    provider, search_query, \"disabled_by_request\","` | — |
| [SRC-1AE03B9EC3-L001868](../../agents/web_agent.py#L1868) | 1868 | `"                    error=\"optional provider use was not approved for this discovery run\","` | — |
| [SRC-1AE03B9EC3-L001869](../../agents/web_agent.py#L1869) | 1869 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001870](../../agents/web_agent.py#L1870) | 1870 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001871](../../agents/web_agent.py#L1871) | 1871 | `"            # DeepSeek Search is quota/usage metered and remains bounded per operation."` | — |
| [SRC-1AE03B9EC3-L001872](../../agents/web_agent.py#L1872) | 1872 | `"            if not os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001873](../../agents/web_agent.py#L1873) | 1873 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001874](../../agents/web_agent.py#L1874) | 1874 | `"                    \"deepseek_search_api\", search_query, \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001875](../../agents/web_agent.py#L1875) | 1875 | `"                    error=\"DEEPSEEK_SEARCH_API_KEY is not set\","` | — |
| [SRC-1AE03B9EC3-L001876](../../agents/web_agent.py#L1876) | 1876 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001877](../../agents/web_agent.py#L1877) | 1877 | `"            elif self._reserve_deepseek_search_request():"` | — |
| [SRC-1AE03B9EC3-L001878](../../agents/web_agent.py#L1878) | 1878 | `"                adapters.append((\"deepseek_search_api\", self._search_deepseek_api))"` | — |
| [SRC-1AE03B9EC3-L001879](../../agents/web_agent.py#L1879) | 1879 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L001880](../../agents/web_agent.py#L1880) | 1880 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001881](../../agents/web_agent.py#L1881) | 1881 | `"                    \"deepseek_search_api\", search_query, \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L001882](../../agents/web_agent.py#L1882) | 1882 | `"                    error=\"per-operation DeepSeek Search request budget exhausted\","` | — |
| [SRC-1AE03B9EC3-L001883](../../agents/web_agent.py#L1883) | 1883 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001884](../../agents/web_agent.py#L1884) | 1884 | `"            if os.getenv(\"BRAVE_SEARCH_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001885](../../agents/web_agent.py#L1885) | 1885 | `"                adapters.append((\"brave_search_api\", self._search_brave))"` | — |
| [SRC-1AE03B9EC3-L001886](../../agents/web_agent.py#L1886) | 1886 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L001887](../../agents/web_agent.py#L1887) | 1887 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001888](../../agents/web_agent.py#L1888) | 1888 | `"                    \"brave_search_api\", search_query, \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001889](../../agents/web_agent.py#L1889) | 1889 | `"                    error=\"BRAVE_SEARCH_API_KEY is not set\","` | — |
| [SRC-1AE03B9EC3-L001890](../../agents/web_agent.py#L1890) | 1890 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001891](../../agents/web_agent.py#L1891) | 1891 | `"            if os.getenv(\"TAVILY_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001892](../../agents/web_agent.py#L1892) | 1892 | `"                adapters.append((\"tavily_search_api\", self._search_tavily))"` | — |
| [SRC-1AE03B9EC3-L001893](../../agents/web_agent.py#L1893) | 1893 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L001894](../../agents/web_agent.py#L1894) | 1894 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001895](../../agents/web_agent.py#L1895) | 1895 | `"                    \"tavily_search_api\", search_query, \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001896](../../agents/web_agent.py#L1896) | 1896 | `"                    error=\"TAVILY_API_KEY is not set\","` | — |
| [SRC-1AE03B9EC3-L001897](../../agents/web_agent.py#L1897) | 1897 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001898](../../agents/web_agent.py#L1898) | 1898 | `"        if detect_freshness(search_query):"` | — |
| [SRC-1AE03B9EC3-L001899](../../agents/web_agent.py#L1899) | 1899 | `"            adapters.append((\"google_news_rss\", self._search_news))"` | — |
| [SRC-1AE03B9EC3-L001900](../../agents/web_agent.py#L1900) | 1900 | `""` | — |
| [SRC-1AE03B9EC3-L001901](../../agents/web_agent.py#L1901) | 1901 | `"        async def run_one(name: str, method: Any) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001902](../../agents/web_agent.py#L1902) | 1902 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001903](../../agents/web_agent.py#L1903) | 1903 | `"                if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L001904](../../agents/web_agent.py#L1904) | 1904 | `"                    budget.reserve(\"search_calls\")"` | — |
| [SRC-1AE03B9EC3-L001905](../../agents/web_agent.py#L1905) | 1905 | `"                provider_timeout = self._effective_timeout(10.0)"` | — |
| [SRC-1AE03B9EC3-L001906](../../agents/web_agent.py#L1906) | 1906 | `"                raw = await asyncio.wait_for("` | — |
| [SRC-1AE03B9EC3-L001907](../../agents/web_agent.py#L1907) | 1907 | `"                    asyncio.to_thread(method, search_query), timeout=provider_timeout"` | — |
| [SRC-1AE03B9EC3-L001908](../../agents/web_agent.py#L1908) | 1908 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001909](../../agents/web_agent.py#L1909) | 1909 | `"                if not isinstance(raw, list):"` | — |
| [SRC-1AE03B9EC3-L001910](../../agents/web_agent.py#L1910) | 1910 | `"                    raise TypeError(\"connector returned a non-list result\")"` | — |
| [SRC-1AE03B9EC3-L001911](../../agents/web_agent.py#L1911) | 1911 | `"                accepted: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001912](../../agents/web_agent.py#L1912) | 1912 | `"                rejected = 0"` | — |
| [SRC-1AE03B9EC3-L001913](../../agents/web_agent.py#L1913) | 1913 | `"                rejection_counts = {reason: 0 for reason in _PROVIDER_REJECTION_REASONS}"` | — |
| [SRC-1AE03B9EC3-L001914](../../agents/web_agent.py#L1914) | 1914 | `"                for item in raw:"` | — |
| [SRC-1AE03B9EC3-L001915](../../agents/web_agent.py#L1915) | 1915 | `"                    if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L001916](../../agents/web_agent.py#L1916) | 1916 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001917](../../agents/web_agent.py#L1917) | 1917 | `"                        rejection_counts[\"malformed_candidate\"] += 1"` | — |
| [SRC-1AE03B9EC3-L001918](../../agents/web_agent.py#L1918) | 1918 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001919](../../agents/web_agent.py#L1919) | 1919 | `"                    safe_url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001920](../../agents/web_agent.py#L1920) | 1920 | `"                    if not safe_url:"` | — |
| [SRC-1AE03B9EC3-L001921](../../agents/web_agent.py#L1921) | 1921 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001922](../../agents/web_agent.py#L1922) | 1922 | `"                        rejection_counts[\"invalid_url_or_unsafe_target\"] += 1"` | — |
| [SRC-1AE03B9EC3-L001923](../../agents/web_agent.py#L1923) | 1923 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001924](../../agents/web_agent.py#L1924) | 1924 | `"                    if _blocked_source_url(safe_url):"` | — |
| [SRC-1AE03B9EC3-L001925](../../agents/web_agent.py#L1925) | 1925 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001926](../../agents/web_agent.py#L1926) | 1926 | `"                        rejection_counts[\"blocked_domain\"] += 1"` | — |
| [SRC-1AE03B9EC3-L001927](../../agents/web_agent.py#L1927) | 1927 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001928](../../agents/web_agent.py#L1928) | 1928 | `"                    normalized_item = dict(item)"` | — |
| [SRC-1AE03B9EC3-L001929](../../agents/web_agent.py#L1929) | 1929 | `"                    normalized_item[\"url\"] = safe_url"` | — |
| [SRC-1AE03B9EC3-L001930](../../agents/web_agent.py#L1930) | 1930 | `"                    normalized_item.setdefault(\"provider\", name)"` | — |
| [SRC-1AE03B9EC3-L001931](../../agents/web_agent.py#L1931) | 1931 | `"                    normalized_item.setdefault(\"search_query\", search_query)"` | — |
| [SRC-1AE03B9EC3-L001932](../../agents/web_agent.py#L1932) | 1932 | `"                    evidence = \" \".join(str(normalized_item.get(k) or \"\") for k in (\"title\", \"snippet\"))"` | — |
| [SRC-1AE03B9EC3-L001933](../../agents/web_agent.py#L1933) | 1933 | `"                    if _relevance_ratio(search_query, evidence) < _minimum_relevance_ratio(search_query):"` | — |
| [SRC-1AE03B9EC3-L001934](../../agents/web_agent.py#L1934) | 1934 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001935](../../agents/web_agent.py#L1935) | 1935 | `"                        rejection_counts[\"relevance_below_threshold\"] += 1"` | — |
| [SRC-1AE03B9EC3-L001936](../../agents/web_agent.py#L1936) | 1936 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001937](../../agents/web_agent.py#L1937) | 1937 | `"                    accepted.append(normalized_item)"` | — |
| [SRC-1AE03B9EC3-L001938](../../agents/web_agent.py#L1938) | 1938 | `"                if accepted:"` | — |
| [SRC-1AE03B9EC3-L001939](../../agents/web_agent.py#L1939) | 1939 | `"                    status = \"ok\""` | — |
| [SRC-1AE03B9EC3-L001940](../../agents/web_agent.py#L1940) | 1940 | `"                    error = None"` | — |
| [SRC-1AE03B9EC3-L001941](../../agents/web_agent.py#L1941) | 1941 | `"                elif raw:"` | — |
| [SRC-1AE03B9EC3-L001942](../../agents/web_agent.py#L1942) | 1942 | `"                    status = \"filtered_all\""` | — |
| [SRC-1AE03B9EC3-L001943](../../agents/web_agent.py#L1943) | 1943 | `"                    details = \", \".join("` | — |
| [SRC-1AE03B9EC3-L001944](../../agents/web_agent.py#L1944) | 1944 | `"                        f\"{reason}={count}\" for reason, count in rejection_counts.items() if count"` | — |
| [SRC-1AE03B9EC3-L001945](../../agents/web_agent.py#L1945) | 1945 | `"                    ) or \"no reason counters recorded\""` | — |
| [SRC-1AE03B9EC3-L001946](../../agents/web_agent.py#L1946) | 1946 | `"                    error = f\"all candidates rejected; {details}\""` | — |
| [SRC-1AE03B9EC3-L001947](../../agents/web_agent.py#L1947) | 1947 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001948](../../agents/web_agent.py#L1948) | 1948 | `"                    status = \"no_results\""` | — |
| [SRC-1AE03B9EC3-L001949](../../agents/web_agent.py#L1949) | 1949 | `"                    error = \"connector returned no parseable results\""` | — |
| [SRC-1AE03B9EC3-L001950](../../agents/web_agent.py#L1950) | 1950 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001951](../../agents/web_agent.py#L1951) | 1951 | `"                    name, search_query, status, len(raw), rejected, error,"` | — |
| [SRC-1AE03B9EC3-L001952](../../agents/web_agent.py#L1952) | 1952 | `"                    accepted_count=len(accepted), rejection_counts=rejection_counts if raw else None,"` | — |
| [SRC-1AE03B9EC3-L001953](../../agents/web_agent.py#L1953) | 1953 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001954](../../agents/web_agent.py#L1954) | 1954 | `"                return accepted"` | — |
| [SRC-1AE03B9EC3-L001955](../../agents/web_agent.py#L1955) | 1955 | `"            except RequestBudgetExceeded as exc:"` | — |
| [SRC-1AE03B9EC3-L001956](../../agents/web_agent.py#L1956) | 1956 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001957](../../agents/web_agent.py#L1957) | 1957 | `"                    name, search_query, \"budget_exhausted\", error=str(exc)"` | — |
| [SRC-1AE03B9EC3-L001958](../../agents/web_agent.py#L1958) | 1958 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001959](../../agents/web_agent.py#L1959) | 1959 | `"            except TimeoutError:"` | — |
| [SRC-1AE03B9EC3-L001960](../../agents/web_agent.py#L1960) | 1960 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001961](../../agents/web_agent.py#L1961) | 1961 | `"                    name, search_query, \"timeout\", error=\"provider exceeded its bounded request timeout\""` | — |
| [SRC-1AE03B9EC3-L001962](../../agents/web_agent.py#L1962) | 1962 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001963](../../agents/web_agent.py#L1963) | 1963 | `"            except Exception as exc:  # noqa: BLE001 - isolate a connector without leaking provider bodies/secrets"` | — |
| [SRC-1AE03B9EC3-L001964](../../agents/web_agent.py#L1964) | 1964 | `"                detail = f\"{type(exc).__name__}: {exc}\" if isinstance(exc, RuntimeError) else type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L001965](../../agents/web_agent.py#L1965) | 1965 | `"                status = \"failed\""` | — |
| [SRC-1AE03B9EC3-L001966](../../agents/web_agent.py#L1966) | 1966 | `"                status_match = re.search(r\"(?i)\\bHTTP\\s+(\\d{3})\\b\", str(exc))"` | — |
| [SRC-1AE03B9EC3-L001967](../../agents/web_agent.py#L1967) | 1967 | `"                if status_match:"` | — |
| [SRC-1AE03B9EC3-L001968](../../agents/web_agent.py#L1968) | 1968 | `"                    status_code = int(status_match.group(1))"` | — |
| [SRC-1AE03B9EC3-L001969](../../agents/web_agent.py#L1969) | 1969 | `"                    if status_code == 429:"` | — |
| [SRC-1AE03B9EC3-L001970](../../agents/web_agent.py#L1970) | 1970 | `"                        status = \"rate_limited\""` | — |
| [SRC-1AE03B9EC3-L001971](../../agents/web_agent.py#L1971) | 1971 | `"                    elif status_code in {401, 403}:"` | — |
| [SRC-1AE03B9EC3-L001972](../../agents/web_agent.py#L1972) | 1972 | `"                        status = \"unauthorized\""` | — |
| [SRC-1AE03B9EC3-L001973](../../agents/web_agent.py#L1973) | 1973 | `"                    elif status_code == 202 or 300 <= status_code < 600:"` | — |
| [SRC-1AE03B9EC3-L001974](../../agents/web_agent.py#L1974) | 1974 | `"                        # Do not bypass anti-bot/challenge responses; mark the provider degraded."` | — |
| [SRC-1AE03B9EC3-L001975](../../agents/web_agent.py#L1975) | 1975 | `"                        status = \"http_error\""` | — |
| [SRC-1AE03B9EC3-L001976](../../agents/web_agent.py#L1976) | 1976 | `"                self._record_provider_diagnostic(name, search_query, status, error=detail)"` | — |
| [SRC-1AE03B9EC3-L001977](../../agents/web_agent.py#L1977) | 1977 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001978](../../agents/web_agent.py#L1978) | 1978 | `""` | — |
| [SRC-1AE03B9EC3-L001979](../../agents/web_agent.py#L1979) | 1979 | `"        async def run_all() -> list[list[dict[str, Any]]]:"` | — |
| [SRC-1AE03B9EC3-L001980](../../agents/web_agent.py#L1980) | 1980 | `"            return await asyncio.gather(*(run_one(name, method) for name, method in adapters))"` | — |
| [SRC-1AE03B9EC3-L001981](../../agents/web_agent.py#L1981) | 1981 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001982](../../agents/web_agent.py#L1982) | 1982 | `"            provider_batches = asyncio.run(run_all())"` | — |
| [SRC-1AE03B9EC3-L001983](../../agents/web_agent.py#L1983) | 1983 | `"            combined = [item for batch in provider_batches for item in batch]"` | — |
| [SRC-1AE03B9EC3-L001984](../../agents/web_agent.py#L1984) | 1984 | `"            # Scholarly fallback only for explicit research-shaped queries; reuse"` | — |
| [SRC-1AE03B9EC3-L001985](../../agents/web_agent.py#L1985) | 1985 | `"            # run_one so budget, timeouts, public-URL/SSRF, blocklist and relevance"` | — |
| [SRC-1AE03B9EC3-L001986](../../agents/web_agent.py#L1986) | 1986 | `"            # validation are identical to ordinary search connectors."` | — |
| [SRC-1AE03B9EC3-L001987](../../agents/web_agent.py#L1987) | 1987 | `"            academic_markers = ("` | — |
| [SRC-1AE03B9EC3-L001988](../../agents/web_agent.py#L1988) | 1988 | `"                \"دراسة علمية\", \"دراسات\", \"ابحاث\", \"أبحاث\", \"بحث علمي\","` | — |
| [SRC-1AE03B9EC3-L001989](../../agents/web_agent.py#L1989) | 1989 | `"                \"ورقة علمية\", \"أوراق علمية\", \"academic\", \"research\","` | — |
| [SRC-1AE03B9EC3-L001990](../../agents/web_agent.py#L1990) | 1990 | `"                \"scientific study\", \"research paper\", \"peer reviewed\","` | — |
| [SRC-1AE03B9EC3-L001991](../../agents/web_agent.py#L1991) | 1991 | `"                \"peer-reviewed\", \"scholarly\", \"literature review\","` | — |
| [SRC-1AE03B9EC3-L001992](../../agents/web_agent.py#L1992) | 1992 | `"                \"systematic review\", \"arxiv\", \"openalex\", \"crossref\","` | — |
| [SRC-1AE03B9EC3-L001993](../../agents/web_agent.py#L1993) | 1993 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001994](../../agents/web_agent.py#L1994) | 1994 | `"            if len(combined) < 3 and any(marker in search_query.casefold() for marker in academic_markers):"` | — |
| [SRC-1AE03B9EC3-L001995](../../agents/web_agent.py#L1995) | 1995 | `"                academic_adapters: list[tuple[str, Any]] = ["` | — |
| [SRC-1AE03B9EC3-L001996](../../agents/web_agent.py#L1996) | 1996 | `"                    (\"openalex\", lambda q: search_openalex(q, limit=3)),"` | — |
| [SRC-1AE03B9EC3-L001997](../../agents/web_agent.py#L1997) | 1997 | `"                    (\"arxiv\", lambda q: search_arxiv(q, limit=3)),"` | — |
| [SRC-1AE03B9EC3-L001998](../../agents/web_agent.py#L1998) | 1998 | `"                    (\"crossref\", lambda q: search_crossref(q, limit=3)),"` | — |
| [SRC-1AE03B9EC3-L001999](../../agents/web_agent.py#L1999) | 1999 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L002000](../../agents/web_agent.py#L2000) | 2000 | `""` | — |
| [SRC-1AE03B9EC3-L002001](../../agents/web_agent.py#L2001) | 2001 | `"                async def run_academic_all() -> list[list[dict[str, Any]]]:"` | — |
| [SRC-1AE03B9EC3-L002002](../../agents/web_agent.py#L2002) | 2002 | `"                    return await asyncio.gather("` | — |
| [SRC-1AE03B9EC3-L002003](../../agents/web_agent.py#L2003) | 2003 | `"                        *(run_one(name, method) for name, method in academic_adapters)"` | — |
| [SRC-1AE03B9EC3-L002004](../../agents/web_agent.py#L2004) | 2004 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L002005](../../agents/web_agent.py#L2005) | 2005 | `""` | — |
| [SRC-1AE03B9EC3-L002006](../../agents/web_agent.py#L2006) | 2006 | `"                provider_batches.extend(asyncio.run(run_academic_all()))"` | — |
| [SRC-1AE03B9EC3-L002007](../../agents/web_agent.py#L2007) | 2007 | `"        except RuntimeError as exc:"` | — |
| [SRC-1AE03B9EC3-L002008](../../agents/web_agent.py#L2008) | 2008 | `"            # This method is synchronous by contract; the HTTP server invokes it in worker threads."` | — |
| [SRC-1AE03B9EC3-L002009](../../agents/web_agent.py#L2009) | 2009 | `"            raise RuntimeError(\"تعذر تشغيل مجدول موصلات البحث.\") from exc"` | — |
| [SRC-1AE03B9EC3-L002010](../../agents/web_agent.py#L2010) | 2010 | `"        combined = [item for batch in provider_batches for item in batch]"` | — |
| [SRC-1AE03B9EC3-L002011](../../agents/web_agent.py#L2011) | 2011 | `"        # De-duplicate repeated URLs before ranking/fusion."` | — |
| [SRC-1AE03B9EC3-L002012](../../agents/web_agent.py#L2012) | 2012 | `"        unique: dict[str, dict[str, Any]] = {}"` | — |
| [SRC-1AE03B9EC3-L002013](../../agents/web_agent.py#L2013) | 2013 | `"        for item in combined:"` | — |
| [SRC-1AE03B9EC3-L002014](../../agents/web_agent.py#L2014) | 2014 | `"            key = item[\"url\"].split(\"#\", 1)[0].rstrip(\"/\")"` | — |
| [SRC-1AE03B9EC3-L002015](../../agents/web_agent.py#L2015) | 2015 | `"            if key not in unique or len(str(item.get(\"snippet\") or \"\")) > len(str(unique[key].get(\"snippet\") or \"\")):"` | — |
| [SRC-1AE03B9EC3-L002016](../../agents/web_agent.py#L2016) | 2016 | `"                unique[key] = item"` | — |
| [SRC-1AE03B9EC3-L002017](../../agents/web_agent.py#L2017) | 2017 | `"        if not unique:"` | — |
| [SRC-1AE03B9EC3-L002018](../../agents/web_agent.py#L2018) | 2018 | `"            raise RuntimeError(\"لم تُرجع موصلات البحث نتائج مرتبطة وقابلة للاستخدام.\")"` | — |
| [SRC-1AE03B9EC3-L002019](../../agents/web_agent.py#L2019) | 2019 | `"        return list(unique.values())"` | — |
| [SRC-1AE03B9EC3-L002020](../../agents/web_agent.py#L2020) | 2020 | `""` | — |
| [SRC-1AE03B9EC3-L002021](../../agents/web_agent.py#L2021) | 2021 | `"    def _reserve_search_call(self) -> None:"` | — |
| [SRC-1AE03B9EC3-L002022](../../agents/web_agent.py#L2022) | 2022 | `"        \"\"\"Reserve one outbound search/social-provider request before network I/O.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002023](../../agents/web_agent.py#L2023) | 2023 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L002024](../../agents/web_agent.py#L2024) | 2024 | `"        if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L002025](../../agents/web_agent.py#L2025) | 2025 | `"            budget.reserve(\"search_calls\")"` | — |
| [SRC-1AE03B9EC3-L002026](../../agents/web_agent.py#L2026) | 2026 | `""` | — |
| [SRC-1AE03B9EC3-L002027](../../agents/web_agent.py#L2027) | 2027 | `"    def _search_brave(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L002028](../../agents/web_agent.py#L2028) | 2028 | `"        \"\"\"Use Brave's official web-search API when the operator provides an API key.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002029](../../agents/web_agent.py#L2029) | 2029 | `"        api_key = os.getenv(\"BRAVE_SEARCH_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002030](../../agents/web_agent.py#L2030) | 2030 | `"        if not api_key:"` | — |
| [SRC-1AE03B9EC3-L002031](../../agents/web_agent.py#L2031) | 2031 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L002032](../../agents/web_agent.py#L2032) | 2032 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L002033](../../agents/web_agent.py#L2033) | 2033 | `"            from importlib.util import find_spec"` | — |
| [SRC-1AE03B9EC3-L002034](../../agents/web_agent.py#L2034) | 2034 | `"            if find_spec(\"httpx\") is None:"` | — |
| [SRC-1AE03B9EC3-L002035](../../agents/web_agent.py#L2035) | 2035 | `"                raise AgentDependencyError(\"حزمة httpx غير مثبتة.\")"` | — |
| [SRC-1AE03B9EC3-L002036](../../agents/web_agent.py#L2036) | 2036 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L002037](../../agents/web_agent.py#L2037) | 2037 | `"            raise AgentDependencyError(\"حزمة httpx غير مثبتة.\") from exc"` | — |
| [SRC-1AE03B9EC3-L002038](../../agents/web_agent.py#L2038) | 2038 | `"        is_arabic = bool(re.search(r\"[\\u0600-\\u06FF]\", query))"` | — |
| [SRC-1AE03B9EC3-L002039](../../agents/web_agent.py#L2039) | 2039 | `"        response = _bounded_http_request(\"GET\", "` | — |
| [SRC-1AE03B9EC3-L002040](../../agents/web_agent.py#L2040) | 2040 | `"            \"https://api.search.brave.com/res/v1/web/search\","` | — |
| [SRC-1AE03B9EC3-L002041](../../agents/web_agent.py#L2041) | 2041 | `"            params={"` | — |
| [SRC-1AE03B9EC3-L002042](../../agents/web_agent.py#L2042) | 2042 | `"                \"q\": query[:600],"` | — |
| [SRC-1AE03B9EC3-L002043](../../agents/web_agent.py#L2043) | 2043 | `"                \"count\": MAX_PROVIDER_RESULTS,"` | — |
| [SRC-1AE03B9EC3-L002044](../../agents/web_agent.py#L2044) | 2044 | `"                \"country\": \"EG\" if is_arabic else \"US\","` | — |
| [SRC-1AE03B9EC3-L002045](../../agents/web_agent.py#L2045) | 2045 | `"                \"search_lang\": \"ar\" if is_arabic else \"en\","` | — |
| [SRC-1AE03B9EC3-L002046](../../agents/web_agent.py#L2046) | 2046 | `"                \"extra_snippets\": \"true\","` | — |
| [SRC-1AE03B9EC3-L002047](../../agents/web_agent.py#L2047) | 2047 | `"            },"` | — |
| [SRC-1AE03B9EC3-L002048](../../agents/web_agent.py#L2048) | 2048 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L002049](../../agents/web_agent.py#L2049) | 2049 | `"                \"Accept\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L002050](../../agents/web_agent.py#L2050) | 2050 | `"                \"X-Subscription-Token\": api_key,"` | — |
| [SRC-1AE03B9EC3-L002051](../../agents/web_agent.py#L2051) | 2051 | `"                \"User-Agent\": \"OmaraiResearchAgent/1.0\","` | — |
| [SRC-1AE03B9EC3-L002052](../../agents/web_agent.py#L2052) | 2052 | `"            },"` | — |
| [SRC-1AE03B9EC3-L002053](../../agents/web_agent.py#L2053) | 2053 | `"            timeout=self._effective_timeout(8.5),"` | — |
| [SRC-1AE03B9EC3-L002054](../../agents/web_agent.py#L2054) | 2054 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L002055](../../agents/web_agent.py#L2055) | 2055 | `"        )"` | — |
| [SRC-1AE03B9EC3-L002056](../../agents/web_agent.py#L2056) | 2056 | `"        response.raise_for_status()"` | — |
| [SRC-1AE03B9EC3-L002057](../../agents/web_agent.py#L2057) | 2057 | `"        payload = response.json()"` | — |
| [SRC-1AE03B9EC3-L002058](../../agents/web_agent.py#L2058) | 2058 | `"        web_results = payload.get(\"web\", {}).get(\"results\", [])"` | — |
| [SRC-1AE03B9EC3-L002059](../../agents/web_agent.py#L2059) | 2059 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L002060](../../agents/web_agent.py#L2060) | 2060 | `"        for item in web_results if isinstance(web_results, list) else []:"` | — |
| [SRC-1AE03B9EC3-L002061](../../agents/web_agent.py#L2061) | 2061 | `"            if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L002062](../../agents/web_agent.py#L2062) | 2062 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002063](../../agents/web_agent.py#L2063) | 2063 | `"            url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L002064](../../agents/web_agent.py#L2064) | 2064 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L002065](../../agents/web_agent.py#L2065) | 2065 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L002066](../../agents/web_agent.py#L2066) | 2066 | `"            snippets = item.get(\"extra_snippets\", [])"` | — |
| [SRC-1AE03B9EC3-L002067](../../agents/web_agent.py#L2067) | 2067 | `"            extra = \" \".join(x for x in snippets if isinstance(x, str)) if isinstance(snippets, list) else \"\""` | — |
| [SRC-1AE03B9EC3-L002068](../../agents/web_agent.py#L2068) | 2068 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L002069](../../agents/web_agent.py#L2069) | 2069 | `"                \"title\": _clean_text(item.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L002070](../../agents/web_agent.py#L2070) | 2070 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L002071](../../agents/web_agent.py#L2071) | 2071 | `"                \"snippet\": _clean_text(item.get(\"description\", \"\") + \" \" + extra, 1600),"` | — |
| [SRC-1AE03B9EC3-L002072](../../agents/web_agent.py#L2072) | 2072 | `"                \"provider\": \"brave_search_api\","` | — |
| [SRC-1AE03B9EC3-L002073](../../agents/web_agent.py#L2073) | 2073 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L002074](../../agents/web_agent.py#L2074) | 2074 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L002075](../../agents/web_agent.py#L2075) | 2075 | `"                \"published_at\": _clean_text(item.get(\"page_age\", \"\") or item.get(\"published_at\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L002076](../../agents/web_agent.py#L2076) | 2076 | `"            })"` | — |
| [SRC-1AE03B9EC3-L002077](../../agents/web_agent.py#L2077) | 2077 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L002078](../../agents/web_agent.py#L2078) | 2078 | `"                break"` | — |
| [SRC-1AE03B9EC3-L002079](../../agents/web_agent.py#L2079) | 2079 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L002080](../../agents/web_agent.py#L2080) | 2080 | `""` | — |
| [SRC-1AE03B9EC3-L002081](../../agents/web_agent.py#L2081) | 2081 | `"    def _search_tavily(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L002082](../../agents/web_agent.py#L2082) | 2082 | `"        \"\"\"Use Tavily's official search API for structured, extractable live web results.\"\"\""` | — |
| [SRC-1AE03B9EC3-L002083](../../agents/web_agent.py#L2083) | 2083 | `"        api_key = os.getenv(\"TAVILY_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L002084](../../agents/web_agent.py#L2084) | 2084 | `"        if not api_key:"` | — |
| [SRC-1AE03B9EC3-L002085](../../agents/web_agent.py#L2085) | 2085 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L002086](../../agents/web_agent.py#L2086) | 2086 | `"        try:"` | — |
