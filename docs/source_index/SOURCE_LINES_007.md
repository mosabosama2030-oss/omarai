# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **007**
- سجلات الأسطر: **800**
- النطاق: SRC-686F71AA50-L000315 إلى SRC-686F71AA50-L001114
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-686F71AA50 — [agents/task_understanding.py](../../agents/task_understanding.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-686F71AA50-L000315](../../agents/task_understanding.py#L315) | 315 | `"    tokens = _TOKEN_RE.findall(text)"` | — |
| [SRC-686F71AA50-L000316](../../agents/task_understanding.py#L316) | 316 | `"    matched: list[str] = []"` | — |
| [SRC-686F71AA50-L000317](../../agents/task_understanding.py#L317) | 317 | `"    prefixes = (\"وال\", \"بال\", \"فال\", \"كال\", \"لل\", \"ال\", \"و\", \"ف\", \"ب\", \"ل\", \"ك\")"` | — |
| [SRC-686F71AA50-L000318](../../agents/task_understanding.py#L318) | 318 | `"    suffixes = (\"هما\", \"هم\", \"هن\", \"ها\", \"ه\", \"كم\", \"كن\", \"ك\", \"نا\", \"ني\", \"ين\", \"ات\", \"ون\")"` | — |
| [SRC-686F71AA50-L000319](../../agents/task_understanding.py#L319) | 319 | `"    english_suffixes = (\"ing\", \"ed\", \"es\", \"s\")"` | — |
| [SRC-686F71AA50-L000320](../../agents/task_understanding.py#L320) | 320 | `"    cache: dict[str, set[str]] = {}"` | — |
| [SRC-686F71AA50-L000321](../../agents/task_understanding.py#L321) | 321 | `""` | — |
| [SRC-686F71AA50-L000322](../../agents/task_understanding.py#L322) | 322 | `"    def token_forms(raw_token: str) -> set[str]:"` | — |
| [SRC-686F71AA50-L000323](../../agents/task_understanding.py#L323) | 323 | `"        original = normalize_text(raw_token)"` | — |
| [SRC-686F71AA50-L000324](../../agents/task_understanding.py#L324) | 324 | `"        if original in cache:"` | — |
| [SRC-686F71AA50-L000325](../../agents/task_understanding.py#L325) | 325 | `"            return cache[original]"` | — |
| [SRC-686F71AA50-L000326](../../agents/task_understanding.py#L326) | 326 | `"        forms = {original} if original else set()"` | — |
| [SRC-686F71AA50-L000327](../../agents/task_understanding.py#L327) | 327 | `"        queue = list(forms)"` | — |
| [SRC-686F71AA50-L000328](../../agents/task_understanding.py#L328) | 328 | `"        while queue:"` | — |
| [SRC-686F71AA50-L000329](../../agents/task_understanding.py#L329) | 329 | `"            current = queue.pop()"` | — |
| [SRC-686F71AA50-L000330](../../agents/task_understanding.py#L330) | 330 | `"            for prefix in prefixes:"` | — |
| [SRC-686F71AA50-L000331](../../agents/task_understanding.py#L331) | 331 | `"                if current.startswith(prefix) and len(current) - len(prefix) >= 3:"` | — |
| [SRC-686F71AA50-L000332](../../agents/task_understanding.py#L332) | 332 | `"                    candidate = current[len(prefix):]"` | — |
| [SRC-686F71AA50-L000333](../../agents/task_understanding.py#L333) | 333 | `"                    if candidate not in forms:"` | — |
| [SRC-686F71AA50-L000334](../../agents/task_understanding.py#L334) | 334 | `"                        forms.add(candidate)"` | — |
| [SRC-686F71AA50-L000335](../../agents/task_understanding.py#L335) | 335 | `"                        queue.append(candidate)"` | — |
| [SRC-686F71AA50-L000336](../../agents/task_understanding.py#L336) | 336 | `"            for suffix in suffixes:"` | — |
| [SRC-686F71AA50-L000337](../../agents/task_understanding.py#L337) | 337 | `"                if current.endswith(suffix) and len(current) - len(suffix) >= 3:"` | — |
| [SRC-686F71AA50-L000338](../../agents/task_understanding.py#L338) | 338 | `"                    candidate = current[:-len(suffix)]"` | — |
| [SRC-686F71AA50-L000339](../../agents/task_understanding.py#L339) | 339 | `"                    if candidate not in forms:"` | — |
| [SRC-686F71AA50-L000340](../../agents/task_understanding.py#L340) | 340 | `"                        forms.add(candidate)"` | — |
| [SRC-686F71AA50-L000341](../../agents/task_understanding.py#L341) | 341 | `"                        queue.append(candidate)"` | — |
| [SRC-686F71AA50-L000342](../../agents/task_understanding.py#L342) | 342 | `"            if current.isascii() and len(current) >= 5:"` | — |
| [SRC-686F71AA50-L000343](../../agents/task_understanding.py#L343) | 343 | `"                for suffix in english_suffixes:"` | — |
| [SRC-686F71AA50-L000344](../../agents/task_understanding.py#L344) | 344 | `"                    if current.endswith(suffix) and len(current) - len(suffix) >= 3:"` | — |
| [SRC-686F71AA50-L000345](../../agents/task_understanding.py#L345) | 345 | `"                        candidate = current[:-len(suffix)]"` | — |
| [SRC-686F71AA50-L000346](../../agents/task_understanding.py#L346) | 346 | `"                        if candidate not in forms:"` | — |
| [SRC-686F71AA50-L000347](../../agents/task_understanding.py#L347) | 347 | `"                            forms.add(candidate)"` | — |
| [SRC-686F71AA50-L000348](../../agents/task_understanding.py#L348) | 348 | `"                            queue.append(candidate)"` | — |
| [SRC-686F71AA50-L000349](../../agents/task_understanding.py#L349) | 349 | `"        cache[original] = forms"` | — |
| [SRC-686F71AA50-L000350](../../agents/task_understanding.py#L350) | 350 | `"        return forms"` | — |
| [SRC-686F71AA50-L000351](../../agents/task_understanding.py#L351) | 351 | `""` | — |
| [SRC-686F71AA50-L000352](../../agents/task_understanding.py#L352) | 352 | `"    token_forms_cache = [token_forms(token) for token in tokens]"` | — |
| [SRC-686F71AA50-L000353](../../agents/task_understanding.py#L353) | 353 | `"    for phrase in phrases:"` | — |
| [SRC-686F71AA50-L000354](../../agents/task_understanding.py#L354) | 354 | `"        normalized = normalize_text(phrase)"` | — |
| [SRC-686F71AA50-L000355](../../agents/task_understanding.py#L355) | 355 | `"        phrase_tokens = _TOKEN_RE.findall(normalized)"` | — |
| [SRC-686F71AA50-L000356](../../agents/task_understanding.py#L356) | 356 | `"        if not phrase_tokens:"` | — |
| [SRC-686F71AA50-L000357](../../agents/task_understanding.py#L357) | 357 | `"            continue"` | — |
| [SRC-686F71AA50-L000358](../../agents/task_understanding.py#L358) | 358 | `"        phrase_forms = [token_forms(token) for token in phrase_tokens]"` | — |
| [SRC-686F71AA50-L000359](../../agents/task_understanding.py#L359) | 359 | `"        width = len(phrase_tokens)"` | — |
| [SRC-686F71AA50-L000360](../../agents/task_understanding.py#L360) | 360 | `"        found = any("` | — |
| [SRC-686F71AA50-L000361](../../agents/task_understanding.py#L361) | 361 | `"            all(token_forms_cache[index + offset] & phrase_forms[offset] for offset in range(width))"` | — |
| [SRC-686F71AA50-L000362](../../agents/task_understanding.py#L362) | 362 | `"            for index in range(max(0, len(tokens) - width + 1))"` | — |
| [SRC-686F71AA50-L000363](../../agents/task_understanding.py#L363) | 363 | `"        )"` | — |
| [SRC-686F71AA50-L000364](../../agents/task_understanding.py#L364) | 364 | `"        if found and normalized not in matched:"` | — |
| [SRC-686F71AA50-L000365](../../agents/task_understanding.py#L365) | 365 | `"            matched.append(normalized)"` | — |
| [SRC-686F71AA50-L000366](../../agents/task_understanding.py#L366) | 366 | `"    return matched"` | — |
| [SRC-686F71AA50-L000367](../../agents/task_understanding.py#L367) | 367 | `""` | — |
| [SRC-686F71AA50-L000368](../../agents/task_understanding.py#L368) | 368 | `"def _has_inline_summary_text(question: str) -> bool:"` | — |
| [SRC-686F71AA50-L000369](../../agents/task_understanding.py#L369) | 369 | `"    \"\"\"Detect explicitly supplied summary text without treating a URL as pasted content.\"\"\""` | — |
| [SRC-686F71AA50-L000370](../../agents/task_understanding.py#L370) | 370 | `"    if not isinstance(question, str) or _URL_RE.search(question):"` | — |
| [SRC-686F71AA50-L000371](../../agents/task_understanding.py#L371) | 371 | `"        return False"` | — |
| [SRC-686F71AA50-L000372](../../agents/task_understanding.py#L372) | 372 | `"    normalized = normalize_text(question)"` | — |
| [SRC-686F71AA50-L000373](../../agents/task_understanding.py#L373) | 373 | `"    markers = ("` | — |
| [SRC-686F71AA50-L000374](../../agents/task_understanding.py#L374) | 374 | `"        \"النص التالي\", \"النص الاتي\", \"النص ده\", \"النص اللي جاي\","` | — |
| [SRC-686F71AA50-L000375](../../agents/task_understanding.py#L375) | 375 | `"        \"المحتوى التالي\", \"هذا النص\", \"following text\", \"the following text\","` | — |
| [SRC-686F71AA50-L000376](../../agents/task_understanding.py#L376) | 376 | `"        \"text below\", \"content below\", \"this text\","` | — |
| [SRC-686F71AA50-L000377](../../agents/task_understanding.py#L377) | 377 | `"    )"` | — |
| [SRC-686F71AA50-L000378](../../agents/task_understanding.py#L378) | 378 | `"    for marker in markers:"` | — |
| [SRC-686F71AA50-L000379](../../agents/task_understanding.py#L379) | 379 | `"        candidate = normalize_text(marker)"` | — |
| [SRC-686F71AA50-L000380](../../agents/task_understanding.py#L380) | 380 | `"        if candidate and candidate in normalized:"` | — |
| [SRC-686F71AA50-L000381](../../agents/task_understanding.py#L381) | 381 | `"            remainder = normalized.split(candidate, 1)[1].strip()"` | — |
| [SRC-686F71AA50-L000382](../../agents/task_understanding.py#L382) | 382 | `"            if len(remainder) >= 8:"` | — |
| [SRC-686F71AA50-L000383](../../agents/task_understanding.py#L383) | 383 | `"                return True"` | — |
| [SRC-686F71AA50-L000384](../../agents/task_understanding.py#L384) | 384 | `"    return bool("` | — |
| [SRC-686F71AA50-L000385](../../agents/task_understanding.py#L385) | 385 | `"        re.search("` | — |
| [SRC-686F71AA50-L000386](../../agents/task_understanding.py#L386) | 386 | `"            r\"^\\s*(?:لخص(?:\\s+لي)?\|تلخيص\|summari[sz]e\|summary)\\s*[:：]\\s*\\S.{12,}$\","` | — |
| [SRC-686F71AA50-L000387](../../agents/task_understanding.py#L387) | 387 | `"            question,"` | — |
| [SRC-686F71AA50-L000388](../../agents/task_understanding.py#L388) | 388 | `"            flags=re.IGNORECASE,"` | — |
| [SRC-686F71AA50-L000389](../../agents/task_understanding.py#L389) | 389 | `"        )"` | — |
| [SRC-686F71AA50-L000390](../../agents/task_understanding.py#L390) | 390 | `"    )"` | — |
| [SRC-686F71AA50-L000391](../../agents/task_understanding.py#L391) | 391 | `""` | — |
| [SRC-686F71AA50-L000392](../../agents/task_understanding.py#L392) | 392 | `""` | — |
| [SRC-686F71AA50-L000393](../../agents/task_understanding.py#L393) | 393 | `"def _has_official_site_target(question: str) -> bool:"` | — |
| [SRC-686F71AA50-L000394](../../agents/task_understanding.py#L394) | 394 | `"    \"\"\"Conservatively check whether an official-site request names a target.\"\"\""` | — |
| [SRC-686F71AA50-L000395](../../agents/task_understanding.py#L395) | 395 | `"    normalized = normalize_text(question)"` | — |
| [SRC-686F71AA50-L000396](../../agents/task_understanding.py#L396) | 396 | `"    for phrase in _PATTERNS[\"official_site_lookup\"]:"` | — |
| [SRC-686F71AA50-L000397](../../agents/task_understanding.py#L397) | 397 | `"        normalized = normalized.replace(normalize_text(phrase), \" \")"` | — |
| [SRC-686F71AA50-L000398](../../agents/task_understanding.py#L398) | 398 | `"    action_phrases = ("` | — |
| [SRC-686F71AA50-L000399](../../agents/task_understanding.py#L399) | 399 | `"        \"من فضلك\", \"لو سمحت\", \"اريد\", \"عايز\", \"عاوزه\", \"ابحث لي عن\","` | — |
| [SRC-686F71AA50-L000400](../../agents/task_understanding.py#L400) | 400 | `"        \"ابحث عن\", \"هات لي\", \"هاتلي\", \"هات\", \"اعثر على\", \"دور على\", \"دورلي على\","` | — |
| [SRC-686F71AA50-L000401](../../agents/task_understanding.py#L401) | 401 | `"        \"find\", \"search for\", \"look up\", \"please\", \"can you\", \"could you\", \"get me\","` | — |
| [SRC-686F71AA50-L000402](../../agents/task_understanding.py#L402) | 402 | `"        \"the\", \"of\", \"for\", \"government\","` | — |
| [SRC-686F71AA50-L000403](../../agents/task_understanding.py#L403) | 403 | `"    )"` | — |
| [SRC-686F71AA50-L000404](../../agents/task_understanding.py#L404) | 404 | `"    for phrase in action_phrases:"` | — |
| [SRC-686F71AA50-L000405](../../agents/task_understanding.py#L405) | 405 | `"        normalized = re.sub("` | — |
| [SRC-686F71AA50-L000406](../../agents/task_understanding.py#L406) | 406 | `"            rf\"(?<!\\w){re.escape(normalize_text(phrase))}(?!\\w)\", \" \", normalized"` | — |
| [SRC-686F71AA50-L000407](../../agents/task_understanding.py#L407) | 407 | `"        )"` | — |
| [SRC-686F71AA50-L000408](../../agents/task_understanding.py#L408) | 408 | `"    generic_target_words = {"` | — |
| [SRC-686F71AA50-L000409](../../agents/task_understanding.py#L409) | 409 | `"        \"الموقع\", \"موقع\", \"الرابط\", \"رابط\", \"لينك\", \"الصفحه\", \"صفحه\","` | — |
| [SRC-686F71AA50-L000410](../../agents/task_understanding.py#L410) | 410 | `"        \"رسمي\", \"الرسمي\", \"الرسمى\", \"حكومي\", \"الحكومي\","` | — |
| [SRC-686F71AA50-L000411](../../agents/task_understanding.py#L411) | 411 | `"        \"وزاره\", \"هيئه\", \"جهة\", \"جهه\", \"حكوميه\","` | — |
| [SRC-686F71AA50-L000412](../../agents/task_understanding.py#L412) | 412 | `"        \"شركه\", \"الشركه\", \"مؤسسه\", \"المؤسسه\", \"بنك\", \"البنك\","` | — |
| [SRC-686F71AA50-L000413](../../agents/task_understanding.py#L413) | 413 | `"        \"منظمه\", \"المنظمه\", \"مصلحه\", \"المصلحه\", \"اداره\", \"الاداره\","` | — |
| [SRC-686F71AA50-L000414](../../agents/task_understanding.py#L414) | 414 | `"        \"وزارة\", \"شركة\", \"الشركة\", \"مؤسسة\", \"الهيئة\", \"الحكومية\","` | — |
| [SRC-686F71AA50-L000415](../../agents/task_understanding.py#L415) | 415 | `"        \"website\", \"site\", \"homepage\", \"official\", \"ministry\", \"agency\","` | — |
| [SRC-686F71AA50-L000416](../../agents/task_understanding.py#L416) | 416 | `"        \"department\", \"organization\", \"organisation\", \"company\", \"bank\","` | — |
| [SRC-686F71AA50-L000417](../../agents/task_understanding.py#L417) | 417 | `"        \"authority\", \"portal\", \"url\", \"link\", \"gov\", \"the\","` | — |
| [SRC-686F71AA50-L000418](../../agents/task_understanding.py#L418) | 418 | `"    }"` | — |
| [SRC-686F71AA50-L000419](../../agents/task_understanding.py#L419) | 419 | `"    ignored = {normalize_text(word) for word in generic_target_words}"` | — |
| [SRC-686F71AA50-L000420](../../agents/task_understanding.py#L420) | 420 | `"    for raw_token in _TOKEN_RE.findall(normalized):"` | — |
| [SRC-686F71AA50-L000421](../../agents/task_understanding.py#L421) | 421 | `"        token = normalize_text(raw_token)"` | — |
| [SRC-686F71AA50-L000422](../../agents/task_understanding.py#L422) | 422 | `"        changed = True"` | — |
| [SRC-686F71AA50-L000423](../../agents/task_understanding.py#L423) | 423 | `"        while changed:"` | — |
| [SRC-686F71AA50-L000424](../../agents/task_understanding.py#L424) | 424 | `"            changed = False"` | — |
| [SRC-686F71AA50-L000425](../../agents/task_understanding.py#L425) | 425 | `"            for prefix in (\"وال\", \"بال\", \"فال\", \"كال\", \"لل\", \"ال\", \"و\", \"ف\", \"ب\", \"ل\", \"ك\"):"` | — |
| [SRC-686F71AA50-L000426](../../agents/task_understanding.py#L426) | 426 | `"                if token.startswith(prefix) and len(token) - len(prefix) >= 3:"` | — |
| [SRC-686F71AA50-L000427](../../agents/task_understanding.py#L427) | 427 | `"                    token = token[len(prefix):]"` | — |
| [SRC-686F71AA50-L000428](../../agents/task_understanding.py#L428) | 428 | `"                    changed = True"` | — |
| [SRC-686F71AA50-L000429](../../agents/task_understanding.py#L429) | 429 | `"                    break"` | — |
| [SRC-686F71AA50-L000430](../../agents/task_understanding.py#L430) | 430 | `"        if token and token not in ignored and len(token) >= 2:"` | — |
| [SRC-686F71AA50-L000431](../../agents/task_understanding.py#L431) | 431 | `"            return True"` | — |
| [SRC-686F71AA50-L000432](../../agents/task_understanding.py#L432) | 432 | `"    return False"` | — |
| [SRC-686F71AA50-L000433](../../agents/task_understanding.py#L433) | 433 | `""` | — |
| [SRC-686F71AA50-L000434](../../agents/task_understanding.py#L434) | 434 | `""` | — |
| [SRC-686F71AA50-L000435](../../agents/task_understanding.py#L435) | 435 | `"def _extract_explicit_locations(question: str) -> list[str]:"` | — |
| [SRC-686F71AA50-L000436](../../agents/task_understanding.py#L436) | 436 | `"    \"\"\"Return only a small, explicit location vocabulary; never infer geolocation.\"\"\""` | — |
| [SRC-686F71AA50-L000437](../../agents/task_understanding.py#L437) | 437 | `"    normalized = normalize_text(question)"` | — |
| [SRC-686F71AA50-L000438](../../agents/task_understanding.py#L438) | 438 | `"    known = ("` | — |
| [SRC-686F71AA50-L000439](../../agents/task_understanding.py#L439) | 439 | `"        (\"مصر\", (\"في مصر\", \"داخل مصر\", \"المصري\", \"المصرية\", \"مصر\", \"egypt\", \"egyptian\")),"` | — |
| [SRC-686F71AA50-L000440](../../agents/task_understanding.py#L440) | 440 | `"        (\"القاهرة\", (\"القاهرة\", \"القاهره\", \"cairo\")),"` | — |
| [SRC-686F71AA50-L000441](../../agents/task_understanding.py#L441) | 441 | `"        (\"الإسكندرية\", (\"الاسكندرية\", \"الاسكندريه\", \"alexandria\")),"` | — |
| [SRC-686F71AA50-L000442](../../agents/task_understanding.py#L442) | 442 | `"        (\"السعودية\", (\"السعودية\", \"السعوديه\", \"saudi arabia\")),"` | — |
| [SRC-686F71AA50-L000443](../../agents/task_understanding.py#L443) | 443 | `"        (\"الإمارات\", (\"الامارات\", \"uae\", \"united arab emirates\")),"` | — |
| [SRC-686F71AA50-L000444](../../agents/task_understanding.py#L444) | 444 | `"        (\"المملكة المتحدة\", (\"المملكة المتحدة\", \"united kingdom\", \"the uk\")),"` | — |
| [SRC-686F71AA50-L000445](../../agents/task_understanding.py#L445) | 445 | `"        (\"الولايات المتحدة\", (\"الولايات المتحدة\", \"united states\", \"the us\")),"` | — |
| [SRC-686F71AA50-L000446](../../agents/task_understanding.py#L446) | 446 | `"    )"` | — |
| [SRC-686F71AA50-L000447](../../agents/task_understanding.py#L447) | 447 | `"    result: list[str] = []"` | — |
| [SRC-686F71AA50-L000448](../../agents/task_understanding.py#L448) | 448 | `"    for canonical, cues in known:"` | — |
| [SRC-686F71AA50-L000449](../../agents/task_understanding.py#L449) | 449 | `"        if any(_contains(normalized, (cue,)) for cue in cues):"` | — |
| [SRC-686F71AA50-L000450](../../agents/task_understanding.py#L450) | 450 | `"            result.append(canonical)"` | — |
| [SRC-686F71AA50-L000451](../../agents/task_understanding.py#L451) | 451 | `"    return result"` | — |
| [SRC-686F71AA50-L000452](../../agents/task_understanding.py#L452) | 452 | `""` | — |
| [SRC-686F71AA50-L000453](../../agents/task_understanding.py#L453) | 453 | `""` | — |
| [SRC-686F71AA50-L000454](../../agents/task_understanding.py#L454) | 454 | `"def _language_profile(question: str) -> str:"` | — |
| [SRC-686F71AA50-L000455](../../agents/task_understanding.py#L455) | 455 | `"    arabic = len(re.findall(r\"[\\u0600-\\u06FF]\", question))"` | — |
| [SRC-686F71AA50-L000456](../../agents/task_understanding.py#L456) | 456 | `"    latin = len(re.findall(r\"[A-Za-z]\", question))"` | — |
| [SRC-686F71AA50-L000457](../../agents/task_understanding.py#L457) | 457 | `"    if arabic and latin:"` | — |
| [SRC-686F71AA50-L000458](../../agents/task_understanding.py#L458) | 458 | `"        return \"mixed\""` | — |
| [SRC-686F71AA50-L000459](../../agents/task_understanding.py#L459) | 459 | `"    if arabic:"` | — |
| [SRC-686F71AA50-L000460](../../agents/task_understanding.py#L460) | 460 | `"        return \"ar\""` | — |
| [SRC-686F71AA50-L000461](../../agents/task_understanding.py#L461) | 461 | `"    if latin:"` | — |
| [SRC-686F71AA50-L000462](../../agents/task_understanding.py#L462) | 462 | `"        return \"en\""` | — |
| [SRC-686F71AA50-L000463](../../agents/task_understanding.py#L463) | 463 | `"    return \"und\""` | — |
| [SRC-686F71AA50-L000464](../../agents/task_understanding.py#L464) | 464 | `""` | — |
| [SRC-686F71AA50-L000465](../../agents/task_understanding.py#L465) | 465 | `""` | — |
| [SRC-686F71AA50-L000466](../../agents/task_understanding.py#L466) | 466 | `"def _primary_family(matches: dict[str, list[str]], mode: str, route: str, normalized: str) -> str:"` | — |
| [SRC-686F71AA50-L000467](../../agents/task_understanding.py#L467) | 467 | `"    # An explicit official-destination request is different from a request for an"` | — |
| [SRC-686F71AA50-L000468](../../agents/task_understanding.py#L468) | 468 | `"    # article mentioning the organization; government verification is a separate slot."` | — |
| [SRC-686F71AA50-L000469](../../agents/task_understanding.py#L469) | 469 | `"    if matches[\"official_site_lookup\"]:"` | — |
| [SRC-686F71AA50-L000470](../../agents/task_understanding.py#L470) | 470 | `"        return \"official_site_lookup\""` | — |
| [SRC-686F71AA50-L000471](../../agents/task_understanding.py#L471) | 471 | `"    for family in ("` | — |
| [SRC-686F71AA50-L000472](../../agents/task_understanding.py#L472) | 472 | `"        \"social_opinions\", \"summarize\", \"troubleshoot\", \"compare\","` | — |
| [SRC-686F71AA50-L000473](../../agents/task_understanding.py#L473) | 473 | `"        \"medical_information\", \"legal_information\", \"coding_or_technical_design\","` | — |
| [SRC-686F71AA50-L000474](../../agents/task_understanding.py#L474) | 474 | `"        \"data_analysis\", \"translation\", \"calculation\", \"planning\","` | — |
| [SRC-686F71AA50-L000475](../../agents/task_understanding.py#L475) | 475 | `"        \"creative_generation\", \"writing_or_editing\", \"lead_generation\","` | — |
| [SRC-686F71AA50-L000476](../../agents/task_understanding.py#L476) | 476 | `"        \"how_to\", \"recommendation\", \"current_information\", \"find_or_discover\","` | — |
| [SRC-686F71AA50-L000477](../../agents/task_understanding.py#L477) | 477 | `"        \"explain_or_define\", \"general_research\","` | — |
| [SRC-686F71AA50-L000478](../../agents/task_understanding.py#L478) | 478 | `"    ):"` | — |
| [SRC-686F71AA50-L000479](../../agents/task_understanding.py#L479) | 479 | `"        if matches.get(family):"` | — |
| [SRC-686F71AA50-L000480](../../agents/task_understanding.py#L480) | 480 | `"            return family"` | — |
| [SRC-686F71AA50-L000481](../../agents/task_understanding.py#L481) | 481 | `"    if route == \"CLARIFY\":"` | — |
| [SRC-686F71AA50-L000482](../../agents/task_understanding.py#L482) | 482 | `"        return \"ambiguous_or_incomplete\""` | — |
| [SRC-686F71AA50-L000483](../../agents/task_understanding.py#L483) | 483 | `"    if route in {\"WEB_SIMPLE\", \"WEB_DEEP\", \"LEAD_GENERATION\"} or mode != \"auto\":"` | — |
| [SRC-686F71AA50-L000484](../../agents/task_understanding.py#L484) | 484 | `"        return \"web_research\""` | — |
| [SRC-686F71AA50-L000485](../../agents/task_understanding.py#L485) | 485 | `"    return \"general_question\""` | — |
| [SRC-686F71AA50-L000486](../../agents/task_understanding.py#L486) | 486 | `""` | — |
| [SRC-686F71AA50-L000487](../../agents/task_understanding.py#L487) | 487 | `""` | — |
| [SRC-686F71AA50-L000488](../../agents/task_understanding.py#L488) | 488 | `"def build_task_spec("` | — |
| [SRC-686F71AA50-L000489](../../agents/task_understanding.py#L489) | 489 | `"    question: str,"` | — |
| [SRC-686F71AA50-L000490](../../agents/task_understanding.py#L490) | 490 | `"    *,"` | — |
| [SRC-686F71AA50-L000491](../../agents/task_understanding.py#L491) | 491 | `"    mode: str = \"auto\","` | — |
| [SRC-686F71AA50-L000492](../../agents/task_understanding.py#L492) | 492 | `"    intent_route: str = \"\","` | — |
| [SRC-686F71AA50-L000493](../../agents/task_understanding.py#L493) | 493 | `"    plan: dict[str, Any] \| None = None,"` | — |
| [SRC-686F71AA50-L000494](../../agents/task_understanding.py#L494) | 494 | `"    dialogue_context: dict[str, Any] \| None = None,"` | — |
| [SRC-686F71AA50-L000495](../../agents/task_understanding.py#L495) | 495 | `") -> dict[str, Any]:"` | — |
| [SRC-686F71AA50-L000496](../../agents/task_understanding.py#L496) | 496 | `"    \"\"\"Build a bounded task specification, interpretation hypotheses, and test matrix.\"\"\""` | — |
| [SRC-686F71AA50-L000497](../../agents/task_understanding.py#L497) | 497 | `"    raw = question if isinstance(question, str) else \"\""` | — |
| [SRC-686F71AA50-L000498](../../agents/task_understanding.py#L498) | 498 | `"    raw = raw[:MAX_TASK_CHARS]"` | — |
| [SRC-686F71AA50-L000499](../../agents/task_understanding.py#L499) | 499 | `"    normalized = normalize_text(raw)"` | — |
| [SRC-686F71AA50-L000500](../../agents/task_understanding.py#L500) | 500 | `"    clean_mode = mode.strip().lower() if isinstance(mode, str) else \"auto\""` | — |
| [SRC-686F71AA50-L000501](../../agents/task_understanding.py#L501) | 501 | `"    if clean_mode not in SUPPORTED_MODES:"` | — |
| [SRC-686F71AA50-L000502](../../agents/task_understanding.py#L502) | 502 | `"        clean_mode = \"auto\""` | — |
| [SRC-686F71AA50-L000503](../../agents/task_understanding.py#L503) | 503 | `"    matches = {"` | — |
| [SRC-686F71AA50-L000504](../../agents/task_understanding.py#L504) | 504 | `"        family: _contains(normalized, phrases)"` | — |
| [SRC-686F71AA50-L000505](../../agents/task_understanding.py#L505) | 505 | `"        for family, phrases in _PATTERNS.items()"` | — |
| [SRC-686F71AA50-L000506](../../agents/task_understanding.py#L506) | 506 | `"        if not family.startswith(\"output_\")"` | — |
| [SRC-686F71AA50-L000507](../../agents/task_understanding.py#L507) | 507 | `"    }"` | — |
| [SRC-686F71AA50-L000508](../../agents/task_understanding.py#L508) | 508 | `"    output_matches = {"` | — |
| [SRC-686F71AA50-L000509](../../agents/task_understanding.py#L509) | 509 | `"        family: _contains(normalized, phrases)"` | — |
| [SRC-686F71AA50-L000510](../../agents/task_understanding.py#L510) | 510 | `"        for family, phrases in _PATTERNS.items()"` | — |
| [SRC-686F71AA50-L000511](../../agents/task_understanding.py#L511) | 511 | `"        if family.startswith(\"output_\")"` | — |
| [SRC-686F71AA50-L000512](../../agents/task_understanding.py#L512) | 512 | `"    }"` | — |
| [SRC-686F71AA50-L000513](../../agents/task_understanding.py#L513) | 513 | `"    aspect_values: list[str] = []"` | — |
| [SRC-686F71AA50-L000514](../../agents/task_understanding.py#L514) | 514 | `"    try:"` | — |
| [SRC-686F71AA50-L000515](../../agents/task_understanding.py#L515) | 515 | `"        from agents.aspect_planning import extract_aspects"` | — |
| [SRC-686F71AA50-L000516](../../agents/task_understanding.py#L516) | 516 | `"        aspect_values = extract_aspects(raw)[:MAX_TASK_ASPECTS]"` | — |
| [SRC-686F71AA50-L000517](../../agents/task_understanding.py#L517) | 517 | `"    except (ImportError, TypeError, ValueError):"` | — |
| [SRC-686F71AA50-L000518](../../agents/task_understanding.py#L518) | 518 | `"        aspect_values = []"` | — |
| [SRC-686F71AA50-L000519](../../agents/task_understanding.py#L519) | 519 | `""` | — |
| [SRC-686F71AA50-L000520](../../agents/task_understanding.py#L520) | 520 | `"    official_destination = bool(matches[\"official_site_lookup\"])"` | — |
| [SRC-686F71AA50-L000521](../../agents/task_understanding.py#L521) | 521 | `"    government_official_site = bool("` | — |
| [SRC-686F71AA50-L000522](../../agents/task_understanding.py#L522) | 522 | `"        official_destination"` | — |
| [SRC-686F71AA50-L000523](../../agents/task_understanding.py#L523) | 523 | `"        and bool(_contains(normalized, _OFFICIAL_WORDS))"` | — |
| [SRC-686F71AA50-L000524](../../agents/task_understanding.py#L524) | 524 | `"    )"` | — |
| [SRC-686F71AA50-L000525](../../agents/task_understanding.py#L525) | 525 | `"    navigation = official_destination or bool("` | — |
| [SRC-686F71AA50-L000526](../../agents/task_understanding.py#L526) | 526 | `"        _URL_RE.search(raw)"` | — |
| [SRC-686F71AA50-L000527](../../agents/task_understanding.py#L527) | 527 | `"        or any(normalize_text(term) in normalized for term in (\"هات رابط\", \"website\", \"homepage\"))"` | — |
| [SRC-686F71AA50-L000528](../../agents/task_understanding.py#L528) | 528 | `"    )"` | — |
| [SRC-686F71AA50-L000529](../../agents/task_understanding.py#L529) | 529 | `"    explicit_freshness = bool(_contains(normalized, _FRESHNESS_CUES))"` | — |
| [SRC-686F71AA50-L000530](../../agents/task_understanding.py#L530) | 530 | `"    current_required = (clean_mode == \"latest\" or explicit_freshness) and not navigation"` | — |
| [SRC-686F71AA50-L000531](../../agents/task_understanding.py#L531) | 531 | `"    social_required = clean_mode == \"social\" or bool(matches[\"social_opinions\"])"` | — |
| [SRC-686F71AA50-L000532](../../agents/task_understanding.py#L532) | 532 | `"    family = _primary_family(matches, clean_mode, intent_route, normalized)"` | — |
| [SRC-686F71AA50-L000533](../../agents/task_understanding.py#L533) | 533 | `""` | — |
| [SRC-686F71AA50-L000534](../../agents/task_understanding.py#L534) | 534 | `"    if family == \"official_site_lookup\":"` | — |
| [SRC-686F71AA50-L000535](../../agents/task_understanding.py#L535) | 535 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000536](../../agents/task_understanding.py#L536) | 536 | `"            \"target_entity_match\","` | — |
| [SRC-686F71AA50-L000537](../../agents/task_understanding.py#L537) | 537 | `"            \"official_domain_or_independently_linked_official_destination\","` | — |
| [SRC-686F71AA50-L000538](../../agents/task_understanding.py#L538) | 538 | `"            \"never_substitute_an_article_or_unrelated_directory\","` | — |
| [SRC-686F71AA50-L000539](../../agents/task_understanding.py#L539) | 539 | `"        ]"` | — |
| [SRC-686F71AA50-L000540](../../agents/task_understanding.py#L540) | 540 | `"        query_strategies = [\"exact_entity\", \"official_domain\", \"government_portal_cross_check\"]"` | — |
| [SRC-686F71AA50-L000541](../../agents/task_understanding.py#L541) | 541 | `"    elif family == \"social_opinions\":"` | — |
| [SRC-686F71AA50-L000542](../../agents/task_understanding.py#L542) | 542 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000543](../../agents/task_understanding.py#L543) | 543 | `"            \"public_social_platform_url\","` | — |
| [SRC-686F71AA50-L000544](../../agents/task_understanding.py#L544) | 544 | `"            \"original_post_or_readable_post_content_when_available\","` | — |
| [SRC-686F71AA50-L000545](../../agents/task_understanding.py#L545) | 545 | `"            \"heuristic_classification_is_not_identity_or_truth_verification\","` | — |
| [SRC-686F71AA50-L000546](../../agents/task_understanding.py#L546) | 546 | `"        ]"` | — |
| [SRC-686F71AA50-L000547](../../agents/task_understanding.py#L547) | 547 | `"        query_strategies = [\"topic_platform\", \"personal_experience\", \"discussion\", \"commercial_exclusion\"]"` | — |
| [SRC-686F71AA50-L000548](../../agents/task_understanding.py#L548) | 548 | `"    elif family == \"summarize\":"` | — |
| [SRC-686F71AA50-L000549](../../agents/task_understanding.py#L549) | 549 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000550](../../agents/task_understanding.py#L550) | 550 | `"            \"read_the_requested_text_or_page\","` | — |
| [SRC-686F71AA50-L000551](../../agents/task_understanding.py#L551) | 551 | `"            \"do_not_summarize_unread_content_from_title_only\","` | — |
| [SRC-686F71AA50-L000552](../../agents/task_understanding.py#L552) | 552 | `"            \"preserve_source_scope_and_important_qualifiers\","` | — |
| [SRC-686F71AA50-L000553](../../agents/task_understanding.py#L553) | 553 | `"        ]"` | — |
| [SRC-686F71AA50-L000554](../../agents/task_understanding.py#L554) | 554 | `"        query_strategies = [\"exact_url_or_supplied_text\", \"page_read\", \"scope_preserving_summary\"]"` | — |
| [SRC-686F71AA50-L000555](../../agents/task_understanding.py#L555) | 555 | `"    elif family == \"troubleshoot\":"` | — |
| [SRC-686F71AA50-L000556](../../agents/task_understanding.py#L556) | 556 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000557](../../agents/task_understanding.py#L557) | 557 | `"            \"preserve_error_message_and_environment\","` | — |
| [SRC-686F71AA50-L000558](../../agents/task_understanding.py#L558) | 558 | `"            \"prefer_manual_or_primary_technical_source\","` | — |
| [SRC-686F71AA50-L000559](../../agents/task_understanding.py#L559) | 559 | `"            \"separate_diagnosis_hypotheses_from_confirmed_cause\","` | — |
| [SRC-686F71AA50-L000560](../../agents/task_understanding.py#L560) | 560 | `"        ]"` | — |
| [SRC-686F71AA50-L000561](../../agents/task_understanding.py#L561) | 561 | `"        query_strategies = [\"symptom_exact_text\", \"cause_hypotheses\", \"official_manual\", \"safe_remedy\"]"` | — |
| [SRC-686F71AA50-L000562](../../agents/task_understanding.py#L562) | 562 | `"    elif family == \"compare\":"` | — |
| [SRC-686F71AA50-L000563](../../agents/task_understanding.py#L563) | 563 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000564](../../agents/task_understanding.py#L564) | 564 | `"            \"preserve_each_explicit_comparison_criterion\","` | — |
| [SRC-686F71AA50-L000565](../../agents/task_understanding.py#L565) | 565 | `"            \"source_support_for_each_material_comparison\","` | — |
| [SRC-686F71AA50-L000566](../../agents/task_understanding.py#L566) | 566 | `"            \"distinguish_primary_specs_from_individual_experience\","` | — |
| [SRC-686F71AA50-L000567](../../agents/task_understanding.py#L567) | 567 | `"        ]"` | — |
| [SRC-686F71AA50-L000568](../../agents/task_understanding.py#L568) | 568 | `"        query_strategies = [\"topic_baseline\", \"one_query_per_criterion\", \"primary_specification\", \"independent_comparison\"]"` | — |
| [SRC-686F71AA50-L000569](../../agents/task_understanding.py#L569) | 569 | `"    elif family == \"how_to\":"` | — |
| [SRC-686F71AA50-L000570](../../agents/task_understanding.py#L570) | 570 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000571](../../agents/task_understanding.py#L571) | 571 | `"            \"ordered_actionable_steps\","` | — |
| [SRC-686F71AA50-L000572](../../agents/task_understanding.py#L572) | 572 | `"            \"surface prerequisites and safety constraints\","` | — |
| [SRC-686F71AA50-L000573](../../agents/task_understanding.py#L573) | 573 | `"            \"distinguish general guidance from product-specific instructions\","` | — |
| [SRC-686F71AA50-L000574](../../agents/task_understanding.py#L574) | 574 | `"        ]"` | — |
| [SRC-686F71AA50-L000575](../../agents/task_understanding.py#L575) | 575 | `"        query_strategies = [\"goal_exact_match\", \"official_guide\", \"stepwise_method\"]"` | — |
| [SRC-686F71AA50-L000576](../../agents/task_understanding.py#L576) | 576 | `"    elif family == \"lead_generation\":"` | — |
| [SRC-686F71AA50-L000577](../../agents/task_understanding.py#L577) | 577 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000578](../../agents/task_understanding.py#L578) | 578 | `"            \"public_buyer_intent_signal\","` | — |
| [SRC-686F71AA50-L000579](../../agents/task_understanding.py#L579) | 579 | `"            \"do_not_treat_listing_or_ad_as_a_buyer\","` | — |
| [SRC-686F71AA50-L000580](../../agents/task_understanding.py#L580) | 580 | `"            \"identity_not_verified_without_separate_evidence\","` | — |
| [SRC-686F71AA50-L000581](../../agents/task_understanding.py#L581) | 581 | `"        ]"` | — |
| [SRC-686F71AA50-L000582](../../agents/task_understanding.py#L582) | 582 | `"        query_strategies = [\"buyer_intent_phrase\", \"public_discussion\", \"recent_signal\"]"` | — |
| [SRC-686F71AA50-L000583](../../agents/task_understanding.py#L583) | 583 | `"    elif family == \"recommendation\":"` | — |
| [SRC-686F71AA50-L000584](../../agents/task_understanding.py#L584) | 584 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000585](../../agents/task_understanding.py#L585) | 585 | `"            \"preserve_budget_location_and_use_case_if_explicit\","` | — |
| [SRC-686F71AA50-L000586](../../agents/task_understanding.py#L586) | 586 | `"            \"compare_alternatives\","` | — |
| [SRC-686F71AA50-L000587](../../agents/task_understanding.py#L587) | 587 | `"            \"make_tradeoffs_and_missing_information_visible\","` | — |
| [SRC-686F71AA50-L000588](../../agents/task_understanding.py#L588) | 588 | `"        ]"` | — |
| [SRC-686F71AA50-L000589](../../agents/task_understanding.py#L589) | 589 | `"        query_strategies = [\"use_case\", \"budget_and_location\", \"pros_cons\", \"alternatives\"]"` | — |
| [SRC-686F71AA50-L000590](../../agents/task_understanding.py#L590) | 590 | `"    elif family == \"medical_information\":"` | — |
| [SRC-686F71AA50-L000591](../../agents/task_understanding.py#L591) | 591 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000592](../../agents/task_understanding.py#L592) | 592 | `"            \"distinguish_general_health_information_from_personal_diagnosis\","` | — |
| [SRC-686F71AA50-L000593](../../agents/task_understanding.py#L593) | 593 | `"            \"prefer_current_authoritative_health_sources_when_research_is_requested\","` | — |
| [SRC-686F71AA50-L000594](../../agents/task_understanding.py#L594) | 594 | `"            \"preserve_units_dosage_context_and_uncertainty\","` | — |
| [SRC-686F71AA50-L000595](../../agents/task_understanding.py#L595) | 595 | `"            \"escalate_urgent_or_emergency_symptoms_to_appropriate_care\","` | — |
| [SRC-686F71AA50-L000596](../../agents/task_understanding.py#L596) | 596 | `"        ]"` | — |
| [SRC-686F71AA50-L000597](../../agents/task_understanding.py#L597) | 597 | `"        query_strategies = [\"authoritative_health_source\", \"symptom_context\", \"limitations_and_urgency\"]"` | — |
| [SRC-686F71AA50-L000598](../../agents/task_understanding.py#L598) | 598 | `"    elif family == \"legal_information\":"` | — |
| [SRC-686F71AA50-L000599](../../agents/task_understanding.py#L599) | 599 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000600](../../agents/task_understanding.py#L600) | 600 | `"            \"identify_jurisdiction_and_effective_date_if_relevant\","` | — |
| [SRC-686F71AA50-L000601](../../agents/task_understanding.py#L601) | 601 | `"            \"prefer_primary_law_or_official_regulatory_text\","` | — |
| [SRC-686F71AA50-L000602](../../agents/task_understanding.py#L602) | 602 | `"            \"distinguish_general_information_from_legal_advice\","` | — |
| [SRC-686F71AA50-L000603](../../agents/task_understanding.py#L603) | 603 | `"        ]"` | — |
| [SRC-686F71AA50-L000604](../../agents/task_understanding.py#L604) | 604 | `"        query_strategies = [\"official_law_text\", \"jurisdiction_and_date\", \"interpretive_context\"]"` | — |
| [SRC-686F71AA50-L000605](../../agents/task_understanding.py#L605) | 605 | `"    elif family == \"coding_or_technical_design\":"` | — |
| [SRC-686F71AA50-L000606](../../agents/task_understanding.py#L606) | 606 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000607](../../agents/task_understanding.py#L607) | 607 | `"            \"preserve_language_version_runtime_and_error_text_if_supplied\","` | — |
| [SRC-686F71AA50-L000608](../../agents/task_understanding.py#L608) | 608 | `"            \"separate_observed_failure_from_cause_hypotheses\","` | — |
| [SRC-686F71AA50-L000609](../../agents/task_understanding.py#L609) | 609 | `"            \"provide_testable_changes_and_regression_tests\","` | — |
| [SRC-686F71AA50-L000610](../../agents/task_understanding.py#L610) | 610 | `"        ]"` | — |
| [SRC-686F71AA50-L000611](../../agents/task_understanding.py#L611) | 611 | `"        query_strategies = [\"minimal_reproducer\", \"documentation_or_api_reference\", \"test_and_verify\"]"` | — |
| [SRC-686F71AA50-L000612](../../agents/task_understanding.py#L612) | 612 | `"    elif family == \"data_analysis\":"` | — |
| [SRC-686F71AA50-L000613](../../agents/task_understanding.py#L613) | 613 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000614](../../agents/task_understanding.py#L614) | 614 | `"            \"preserve_dataset_grain_and_metric_definition\","` | — |
| [SRC-686F71AA50-L000615](../../agents/task_understanding.py#L615) | 615 | `"            \"inspect_missingness_duplicates_outliers_and_time_coverage\","` | — |
| [SRC-686F71AA50-L000616](../../agents/task_understanding.py#L616) | 616 | `"            \"separate_observed_association_from_causal_explanation\","` | — |
| [SRC-686F71AA50-L000617](../../agents/task_understanding.py#L617) | 617 | `"        ]"` | — |
| [SRC-686F71AA50-L000618](../../agents/task_understanding.py#L618) | 618 | `"        query_strategies = [\"schema_and_grain\", \"data_quality\", \"metric_and_segment_checks\"]"` | — |
| [SRC-686F71AA50-L000619](../../agents/task_understanding.py#L619) | 619 | `"    elif family == \"calculation\":"` | — |
| [SRC-686F71AA50-L000620](../../agents/task_understanding.py#L620) | 620 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000621](../../agents/task_understanding.py#L621) | 621 | `"            \"show_formula_and_units_when_useful\","` | — |
| [SRC-686F71AA50-L000622](../../agents/task_understanding.py#L622) | 622 | `"            \"validate_input_units_and_rounding\","` | — |
| [SRC-686F71AA50-L000623](../../agents/task_understanding.py#L623) | 623 | `"            \"distinguish_exact_result_from_assumption_based_estimate\","` | — |
| [SRC-686F71AA50-L000624](../../agents/task_understanding.py#L624) | 624 | `"        ]"` | — |
| [SRC-686F71AA50-L000625](../../agents/task_understanding.py#L625) | 625 | `"        query_strategies = [\"formula\", \"unit_validation\", \"independent_arithmetic_check\"]"` | — |
| [SRC-686F71AA50-L000626](../../agents/task_understanding.py#L626) | 626 | `"    elif family == \"translation\":"` | — |
| [SRC-686F71AA50-L000627](../../agents/task_understanding.py#L627) | 627 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000628](../../agents/task_understanding.py#L628) | 628 | `"            \"preserve_meaning_tone_and_named_entities\","` | — |
| [SRC-686F71AA50-L000629](../../agents/task_understanding.py#L629) | 629 | `"            \"surface_ambiguous_source_phrasing_instead_of_silently_inventing_meaning\","` | — |
| [SRC-686F71AA50-L000630](../../agents/task_understanding.py#L630) | 630 | `"            \"respect_explicit_target_language_and_script\","` | — |
| [SRC-686F71AA50-L000631](../../agents/task_understanding.py#L631) | 631 | `"        ]"` | — |
| [SRC-686F71AA50-L000632](../../agents/task_understanding.py#L632) | 632 | `"        query_strategies = [\"source_text\", \"target_language\", \"terminology_and_tone\"]"` | — |
| [SRC-686F71AA50-L000633](../../agents/task_understanding.py#L633) | 633 | `"    elif family == \"writing_or_editing\":"` | — |
| [SRC-686F71AA50-L000634](../../agents/task_understanding.py#L634) | 634 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000635](../../agents/task_understanding.py#L635) | 635 | `"            \"follow_requested_audience_tone_and_format\","` | — |
| [SRC-686F71AA50-L000636](../../agents/task_understanding.py#L636) | 636 | `"            \"preserve_user_provided_facts_without_adding_unverified_claims\","` | — |
| [SRC-686F71AA50-L000637](../../agents/task_understanding.py#L637) | 637 | `"            \"distinguish_rewrite_from_fact_check\","` | — |
| [SRC-686F71AA50-L000638](../../agents/task_understanding.py#L638) | 638 | `"        ]"` | — |
| [SRC-686F71AA50-L000639](../../agents/task_understanding.py#L639) | 639 | `"        query_strategies = [\"audience_and_purpose\", \"tone_and_format\", \"fact_preservation\"]"` | — |
| [SRC-686F71AA50-L000640](../../agents/task_understanding.py#L640) | 640 | `"    elif family == \"planning\":"` | — |
| [SRC-686F71AA50-L000641](../../agents/task_understanding.py#L641) | 641 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000642](../../agents/task_understanding.py#L642) | 642 | `"            \"preserve_goal_constraints_dependencies_and_deadline\","` | — |
| [SRC-686F71AA50-L000643](../../agents/task_understanding.py#L643) | 643 | `"            \"make_assumptions_and_unavailable_resources_explicit\","` | — |
| [SRC-686F71AA50-L000644](../../agents/task_understanding.py#L644) | 644 | `"            \"separate_proposed_steps_from_completed_actions\","` | — |
| [SRC-686F71AA50-L000645](../../agents/task_understanding.py#L645) | 645 | `"        ]"` | — |
| [SRC-686F71AA50-L000646](../../agents/task_understanding.py#L646) | 646 | `"        query_strategies = [\"goal_and_constraints\", \"dependency_order\", \"risks_and_fallbacks\"]"` | — |
| [SRC-686F71AA50-L000647](../../agents/task_understanding.py#L647) | 647 | `"    elif family == \"creative_generation\":"` | — |
| [SRC-686F71AA50-L000648](../../agents/task_understanding.py#L648) | 648 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000649](../../agents/task_understanding.py#L649) | 649 | `"            \"follow_requested_genre_voice_and_constraints\","` | — |
| [SRC-686F71AA50-L000650](../../agents/task_understanding.py#L650) | 650 | `"            \"do_not_present_invented_story_details_as_real_facts\","` | — |
| [SRC-686F71AA50-L000651](../../agents/task_understanding.py#L651) | 651 | `"            \"preserve_explicit_content_boundaries\","` | — |
| [SRC-686F71AA50-L000652](../../agents/task_understanding.py#L652) | 652 | `"        ]"` | — |
| [SRC-686F71AA50-L000653](../../agents/task_understanding.py#L653) | 653 | `"        query_strategies = [\"genre_and_voice\", \"creative_constraints\", \"revision_options\"]"` | — |
| [SRC-686F71AA50-L000654](../../agents/task_understanding.py#L654) | 654 | `"    else:"` | — |
| [SRC-686F71AA50-L000655](../../agents/task_understanding.py#L655) | 655 | `"        evidence_requirements = ["` | — |
| [SRC-686F71AA50-L000656](../../agents/task_understanding.py#L656) | 656 | `"            \"match_sources_to_the_question\","` | — |
| [SRC-686F71AA50-L000657](../../agents/task_understanding.py#L657) | 657 | `"            \"distinguish_search_snippet_from_read_page\","` | — |
| [SRC-686F71AA50-L000658](../../agents/task_understanding.py#L658) | 658 | `"            \"cite_material_web_claims\","` | — |
| [SRC-686F71AA50-L000659](../../agents/task_understanding.py#L659) | 659 | `"        ]"` | — |
| [SRC-686F71AA50-L000660](../../agents/task_understanding.py#L660) | 660 | `"        query_strategies = [\"exact_topic\", \"primary_source\", \"cross_check_if_needed\"]"` | — |
| [SRC-686F71AA50-L000661](../../agents/task_understanding.py#L661) | 661 | `""` | — |
| [SRC-686F71AA50-L000662](../../agents/task_understanding.py#L662) | 662 | `"    # Source freshness, requested officiality, and social evidence are orthogonal"` | — |
| [SRC-686F71AA50-L000663](../../agents/task_understanding.py#L663) | 663 | `"    # constraints. Preserve them even when another intent is the primary family."` | — |
| [SRC-686F71AA50-L000664](../../agents/task_understanding.py#L664) | 664 | `"    if current_required and not official_destination:"` | — |
| [SRC-686F71AA50-L000665](../../agents/task_understanding.py#L665) | 665 | `"        evidence_requirements.extend(["` | — |
| [SRC-686F71AA50-L000666](../../agents/task_understanding.py#L666) | 666 | `"            \"publication_or_update_date\","` | — |
| [SRC-686F71AA50-L000667](../../agents/task_understanding.py#L667) | 667 | `"            \"page_text_successfully_read\","` | — |
| [SRC-686F71AA50-L000668](../../agents/task_understanding.py#L668) | 668 | `"            \"prefer_primary_current_source\","` | — |
| [SRC-686F71AA50-L000669](../../agents/task_understanding.py#L669) | 669 | `"            \"do_not_use_stale_page_as_current_proof\","` | — |
| [SRC-686F71AA50-L000670](../../agents/task_understanding.py#L670) | 670 | `"        ])"` | — |
| [SRC-686F71AA50-L000671](../../agents/task_understanding.py#L671) | 671 | `"        query_strategies.extend([\"recent_official_update\", \"primary_source\", \"date_check\"])"` | — |
| [SRC-686F71AA50-L000672](../../agents/task_understanding.py#L672) | 672 | `"    if social_required and family != \"social_opinions\":"` | — |
| [SRC-686F71AA50-L000673](../../agents/task_understanding.py#L673) | 673 | `"        evidence_requirements.extend(["` | — |
| [SRC-686F71AA50-L000674](../../agents/task_understanding.py#L674) | 674 | `"            \"public_social_platform_url\","` | — |
| [SRC-686F71AA50-L000675](../../agents/task_understanding.py#L675) | 675 | `"            \"separate_personal_experience_from_promotion\","` | — |
| [SRC-686F71AA50-L000676](../../agents/task_understanding.py#L676) | 676 | `"            \"heuristic_classification_is_not_identity_or_truth_verification\","` | — |
| [SRC-686F71AA50-L000677](../../agents/task_understanding.py#L677) | 677 | `"        ])"` | — |
| [SRC-686F71AA50-L000678](../../agents/task_understanding.py#L678) | 678 | `"        query_strategies.extend([\"personal_experience\", \"discussion\", \"commercial_exclusion\"])"` | — |
| [SRC-686F71AA50-L000679](../../agents/task_understanding.py#L679) | 679 | `"    if official_destination and family != \"official_site_lookup\":"` | — |
| [SRC-686F71AA50-L000680](../../agents/task_understanding.py#L680) | 680 | `"        evidence_requirements.extend(["` | — |
| [SRC-686F71AA50-L000681](../../agents/task_understanding.py#L681) | 681 | `"            \"distinguish_official_destination_from_mentions_or_articles\","` | — |
| [SRC-686F71AA50-L000682](../../agents/task_understanding.py#L682) | 682 | `"            \"do_not_claim_domain_ownership_without_independent_evidence\","` | — |
| [SRC-686F71AA50-L000683](../../agents/task_understanding.py#L683) | 683 | `"        ])"` | — |
| [SRC-686F71AA50-L000684](../../agents/task_understanding.py#L684) | 684 | `"        query_strategies.extend([\"official_domain\", \"government_portal_cross_check\"])"` | — |
| [SRC-686F71AA50-L000685](../../agents/task_understanding.py#L685) | 685 | `"    if \"compare\" in matches and family != \"compare\":"` | — |
| [SRC-686F71AA50-L000686](../../agents/task_understanding.py#L686) | 686 | `"        evidence_requirements.extend(["` | — |
| [SRC-686F71AA50-L000687](../../agents/task_understanding.py#L687) | 687 | `"            \"preserve_explicit_comparison_criteria\","` | — |
| [SRC-686F71AA50-L000688](../../agents/task_understanding.py#L688) | 688 | `"            \"do_not_collapse_multiple_dimensions_into_one_generic_answer\","` | — |
| [SRC-686F71AA50-L000689](../../agents/task_understanding.py#L689) | 689 | `"        ])"` | — |
| [SRC-686F71AA50-L000690](../../agents/task_understanding.py#L690) | 690 | `"        query_strategies.extend([\"one_query_per_criterion\", \"independent_comparison\"])"` | — |
| [SRC-686F71AA50-L000691](../../agents/task_understanding.py#L691) | 691 | `"    if len(explicit_aspects := aspect_values) > 1:"` | — |
| [SRC-686F71AA50-L000692](../../agents/task_understanding.py#L692) | 692 | `"        evidence_requirements.append(\"track_evidence_coverage_per_explicit_aspect\")"` | — |
| [SRC-686F71AA50-L000693](../../agents/task_understanding.py#L693) | 693 | `"        query_strategies.append(\"one_query_per_criterion\")"` | — |
| [SRC-686F71AA50-L000694](../../agents/task_understanding.py#L694) | 694 | `"    query_strategies = list(dict.fromkeys(query_strategies))"` | — |
| [SRC-686F71AA50-L000695](../../agents/task_understanding.py#L695) | 695 | `"    evidence_requirements = list(dict.fromkeys(evidence_requirements))"` | — |
| [SRC-686F71AA50-L000696](../../agents/task_understanding.py#L696) | 696 | `""` | — |
| [SRC-686F71AA50-L000697](../../agents/task_understanding.py#L697) | 697 | `"    location = _extract_explicit_locations(raw)"` | — |
| [SRC-686F71AA50-L000698](../../agents/task_understanding.py#L698) | 698 | `"    years = list(dict.fromkeys(_YEAR_RE.findall(raw)))"` | — |
| [SRC-686F71AA50-L000699](../../agents/task_understanding.py#L699) | 699 | `"    dates = list(dict.fromkeys(_DATE_RE.findall(raw)))"` | — |
| [SRC-686F71AA50-L000700](../../agents/task_understanding.py#L700) | 700 | `"    budgets = [m.group(0).strip()[:100] for m in _BUDGET_RE.finditer(raw)]"` | — |
| [SRC-686F71AA50-L000701](../../agents/task_understanding.py#L701) | 701 | `"    urls = list(dict.fromkeys(_URL_RE.findall(raw)))[:5]"` | — |
| [SRC-686F71AA50-L000702](../../agents/task_understanding.py#L702) | 702 | `"    inline_summary_text = _has_inline_summary_text(raw)"` | — |
| [SRC-686F71AA50-L000703](../../agents/task_understanding.py#L703) | 703 | `"    unresolved_followup = any(normalize_text(cue) in normalized for cue in _FOLLOWUP_CUES)"` | — |
| [SRC-686F71AA50-L000704](../../agents/task_understanding.py#L704) | 704 | `"    missing_required_inputs: list[str] = []"` | — |
| [SRC-686F71AA50-L000705](../../agents/task_understanding.py#L705) | 705 | `"    if intent_route == \"CLARIFY\":"` | — |
| [SRC-686F71AA50-L000706](../../agents/task_understanding.py#L706) | 706 | `"        missing_required_inputs.append(\"unresolved_referent_or_incomplete_request\")"` | — |
| [SRC-686F71AA50-L000707](../../agents/task_understanding.py#L707) | 707 | `"    if official_destination and not _has_official_site_target(raw):"` | — |
| [SRC-686F71AA50-L000708](../../agents/task_understanding.py#L708) | 708 | `"        missing_required_inputs.append(\"official_destination_target_entity\")"` | — |
| [SRC-686F71AA50-L000709](../../agents/task_understanding.py#L709) | 709 | `"    if family == \"summarize\" and not urls and not inline_summary_text:"` | — |
| [SRC-686F71AA50-L000710](../../agents/task_understanding.py#L710) | 710 | `"        missing_required_inputs.append(\"summary_source_url_or_pasted_text\")"` | — |
| [SRC-686F71AA50-L000711](../../agents/task_understanding.py#L711) | 711 | `"    context = dialogue_context if isinstance(dialogue_context, dict) else {}"` | — |
| [SRC-686F71AA50-L000712](../../agents/task_understanding.py#L712) | 712 | `"    explicit_aspects = list(dict.fromkeys(aspect_values))[:MAX_TASK_ASPECTS]"` | — |
| [SRC-686F71AA50-L000713](../../agents/task_understanding.py#L713) | 713 | `""` | — |
| [SRC-686F71AA50-L000714](../../agents/task_understanding.py#L714) | 714 | `"    # Hypotheses are alternatives considered by the deterministic classifier. Counts"` | — |
| [SRC-686F71AA50-L000715](../../agents/task_understanding.py#L715) | 715 | `"    # are matched lexical signals, not calibrated confidence or probability."` | — |
| [SRC-686F71AA50-L000716](../../agents/task_understanding.py#L716) | 716 | `"    hypothesis_rows: list[dict[str, Any]] = []"` | — |
| [SRC-686F71AA50-L000717](../../agents/task_understanding.py#L717) | 717 | `"    for candidate_family, signals in matches.items():"` | — |
| [SRC-686F71AA50-L000718](../../agents/task_understanding.py#L718) | 718 | `"        if signals:"` | — |
| [SRC-686F71AA50-L000719](../../agents/task_understanding.py#L719) | 719 | `"            hypothesis_rows.append({"` | — |
| [SRC-686F71AA50-L000720](../../agents/task_understanding.py#L720) | 720 | `"                \"family\": candidate_family,"` | — |
| [SRC-686F71AA50-L000721](../../agents/task_understanding.py#L721) | 721 | `"                \"matched_signal_count\": len(signals),"` | — |
| [SRC-686F71AA50-L000722](../../agents/task_understanding.py#L722) | 722 | `"                \"signals\": signals[:4],"` | — |
| [SRC-686F71AA50-L000723](../../agents/task_understanding.py#L723) | 723 | `"                \"status\": \"candidate_interpretation\","` | — |
| [SRC-686F71AA50-L000724](../../agents/task_understanding.py#L724) | 724 | `"            })"` | — |
| [SRC-686F71AA50-L000725](../../agents/task_understanding.py#L725) | 725 | `"    hypothesis_rows.sort("` | — |
| [SRC-686F71AA50-L000726](../../agents/task_understanding.py#L726) | 726 | `"        key=lambda item: (-item[\"matched_signal_count\"], item[\"family\"])"` | — |
| [SRC-686F71AA50-L000727](../../agents/task_understanding.py#L727) | 727 | `"    )"` | — |
| [SRC-686F71AA50-L000728](../../agents/task_understanding.py#L728) | 728 | `"    for item in hypothesis_rows:"` | — |
| [SRC-686F71AA50-L000729](../../agents/task_understanding.py#L729) | 729 | `"        item[\"selected\"] = item[\"family\"] == family"` | — |
| [SRC-686F71AA50-L000730](../../agents/task_understanding.py#L730) | 730 | `"    if len(hypothesis_rows) > 8:"` | — |
| [SRC-686F71AA50-L000731](../../agents/task_understanding.py#L731) | 731 | `"        hypothesis_rows = hypothesis_rows[:8]"` | — |
| [SRC-686F71AA50-L000732](../../agents/task_understanding.py#L732) | 732 | `""` | — |
| [SRC-686F71AA50-L000733](../../agents/task_understanding.py#L733) | 733 | `"    # A conflict is a reason to preserve alternatives in diagnostics, not a reason to"` | — |
| [SRC-686F71AA50-L000734](../../agents/task_understanding.py#L734) | 734 | `"    # invent certainty. High ambiguity is limited to unresolved references or a"` | — |
| [SRC-686F71AA50-L000735](../../agents/task_understanding.py#L735) | 735 | `"    # short fragment explicitly marked as contextual."` | — |
| [SRC-686F71AA50-L000736](../../agents/task_understanding.py#L736) | 736 | `"    unresolved = bool(missing_required_inputs) or bool(context.get(\"needs_clarification\")) or ("` | — |
| [SRC-686F71AA50-L000737](../../agents/task_understanding.py#L737) | 737 | `"        len(raw.strip()) <= 28 and unresolved_followup"` | — |
| [SRC-686F71AA50-L000738](../../agents/task_understanding.py#L738) | 738 | `"        and not context.get(\"resolved_question\")"` | — |
| [SRC-686F71AA50-L000739](../../agents/task_understanding.py#L739) | 739 | `"    )"` | — |
| [SRC-686F71AA50-L000740](../../agents/task_understanding.py#L740) | 740 | `"    if unresolved:"` | — |
| [SRC-686F71AA50-L000741](../../agents/task_understanding.py#L741) | 741 | `"        ambiguity_status = \"needs_clarification\""` | — |
| [SRC-686F71AA50-L000742](../../agents/task_understanding.py#L742) | 742 | `"    elif len(hypothesis_rows) >= 3:"` | — |
| [SRC-686F71AA50-L000743](../../agents/task_understanding.py#L743) | 743 | `"        ambiguity_status = \"multiple_overlapping_signals\""` | — |
| [SRC-686F71AA50-L000744](../../agents/task_understanding.py#L744) | 744 | `"    elif len(hypothesis_rows) == 2:"` | — |
| [SRC-686F71AA50-L000745](../../agents/task_understanding.py#L745) | 745 | `"        ambiguity_status = \"some_intent_overlap\""` | — |
| [SRC-686F71AA50-L000746](../../agents/task_understanding.py#L746) | 746 | `"    else:"` | — |
| [SRC-686F71AA50-L000747](../../agents/task_understanding.py#L747) | 747 | `"        ambiguity_status = \"no_strong_lexical_conflict_detected\""` | — |
| [SRC-686F71AA50-L000748](../../agents/task_understanding.py#L748) | 748 | `""` | — |
| [SRC-686F71AA50-L000749](../../agents/task_understanding.py#L749) | 749 | `"    # Tool requirements are advisory planning metadata, not executable permission."` | — |
| [SRC-686F71AA50-L000750](../../agents/task_understanding.py#L750) | 750 | `"    # A clarification route is a hard stop even when the UI has a research mode selected."` | — |
| [SRC-686F71AA50-L000751](../../agents/task_understanding.py#L751) | 751 | `"    route_is_clarification = intent_route == \"CLARIFY\""` | — |
| [SRC-686F71AA50-L000752](../../agents/task_understanding.py#L752) | 752 | `"    route_is_local = intent_route == \"LOCAL\""` | — |
| [SRC-686F71AA50-L000753](../../agents/task_understanding.py#L753) | 753 | `"    search_requested = ("` | — |
| [SRC-686F71AA50-L000754](../../agents/task_understanding.py#L754) | 754 | `"        intent_route in {\"WEB_SIMPLE\", \"WEB_DEEP\", \"LEAD_GENERATION\"}"` | — |
| [SRC-686F71AA50-L000755](../../agents/task_understanding.py#L755) | 755 | `"        or ("` | — |
| [SRC-686F71AA50-L000756](../../agents/task_understanding.py#L756) | 756 | `"            intent_route == \"deterministic_fallback\""` | — |
| [SRC-686F71AA50-L000757](../../agents/task_understanding.py#L757) | 757 | `"            and isinstance(plan, dict)"` | — |
| [SRC-686F71AA50-L000758](../../agents/task_understanding.py#L758) | 758 | `"            and bool(plan.get(\"queries\"))"` | — |
| [SRC-686F71AA50-L000759](../../agents/task_understanding.py#L759) | 759 | `"        )"` | — |
| [SRC-686F71AA50-L000760](../../agents/task_understanding.py#L760) | 760 | `"        or ("` | — |
| [SRC-686F71AA50-L000761](../../agents/task_understanding.py#L761) | 761 | `"            intent_route not in {\"LOCAL\", \"CLARIFY\", \"BUDGET_EXHAUSTED\"}"` | — |
| [SRC-686F71AA50-L000762](../../agents/task_understanding.py#L762) | 762 | `"            and ("` | — |
| [SRC-686F71AA50-L000763](../../agents/task_understanding.py#L763) | 763 | `"                social_required"` | — |
| [SRC-686F71AA50-L000764](../../agents/task_understanding.py#L764) | 764 | `"                or official_destination"` | — |
| [SRC-686F71AA50-L000765](../../agents/task_understanding.py#L765) | 765 | `"                or current_required"` | — |
| [SRC-686F71AA50-L000766](../../agents/task_understanding.py#L766) | 766 | `"                or family in {\"find_or_discover\", \"lead_generation\", \"general_research\"}"` | — |
| [SRC-686F71AA50-L000767](../../agents/task_understanding.py#L767) | 767 | `"            )"` | — |
| [SRC-686F71AA50-L000768](../../agents/task_understanding.py#L768) | 768 | `"        )"` | — |
| [SRC-686F71AA50-L000769](../../agents/task_understanding.py#L769) | 769 | `"        or ("` | — |
| [SRC-686F71AA50-L000770](../../agents/task_understanding.py#L770) | 770 | `"            clean_mode != \"auto\""` | — |
| [SRC-686F71AA50-L000771](../../agents/task_understanding.py#L771) | 771 | `"            and not route_is_clarification"` | — |
| [SRC-686F71AA50-L000772](../../agents/task_understanding.py#L772) | 772 | `"            and not route_is_local"` | — |
| [SRC-686F71AA50-L000773](../../agents/task_understanding.py#L773) | 773 | `"        )"` | — |
| [SRC-686F71AA50-L000774](../../agents/task_understanding.py#L774) | 774 | `"    )"` | — |
| [SRC-686F71AA50-L000775](../../agents/task_understanding.py#L775) | 775 | `"    page_fetch_requested = bool(urls) or ("` | — |
| [SRC-686F71AA50-L000776](../../agents/task_understanding.py#L776) | 776 | `"        family == \"summarize\""` | — |
| [SRC-686F71AA50-L000777](../../agents/task_understanding.py#L777) | 777 | `"        and not inline_summary_text"` | — |
| [SRC-686F71AA50-L000778](../../agents/task_understanding.py#L778) | 778 | `"        and not route_is_clarification"` | — |
| [SRC-686F71AA50-L000779](../../agents/task_understanding.py#L779) | 779 | `"    )"` | — |
| [SRC-686F71AA50-L000780](../../agents/task_understanding.py#L780) | 780 | `"    tools: list[str] = []"` | — |
| [SRC-686F71AA50-L000781](../../agents/task_understanding.py#L781) | 781 | `"    if search_requested and not route_is_clarification:"` | — |
| [SRC-686F71AA50-L000782](../../agents/task_understanding.py#L782) | 782 | `"        tools.append(\"web_search\")"` | — |
| [SRC-686F71AA50-L000783](../../agents/task_understanding.py#L783) | 783 | `"    if page_fetch_requested and not route_is_clarification:"` | — |
| [SRC-686F71AA50-L000784](../../agents/task_understanding.py#L784) | 784 | `"        tools.append(\"page_fetch\")"` | — |
| [SRC-686F71AA50-L000785](../../agents/task_understanding.py#L785) | 785 | `"    if social_required and not route_is_clarification:"` | — |
| [SRC-686F71AA50-L000786](../../agents/task_understanding.py#L786) | 786 | `"        tools.append(\"public_social_search_if_configured\")"` | — |
| [SRC-686F71AA50-L000787](../../agents/task_understanding.py#L787) | 787 | `"    if ("` | — |
| [SRC-686F71AA50-L000788](../../agents/task_understanding.py#L788) | 788 | `"        intent_route in {\"MODEL_ONLY\", \"WEB_SIMPLE\", \"WEB_DEEP\", \"LEAD_GENERATION\", \"deterministic_fallback\"}"` | — |
| [SRC-686F71AA50-L000789](../../agents/task_understanding.py#L789) | 789 | `"        or (clean_mode != \"auto\" and not route_is_clarification and not route_is_local)"` | — |
| [SRC-686F71AA50-L000790](../../agents/task_understanding.py#L790) | 790 | `"    ):"` | — |
| [SRC-686F71AA50-L000791](../../agents/task_understanding.py#L791) | 791 | `"        tools.append(\"language_model_generation_if_configured\")"` | — |
| [SRC-686F71AA50-L000792](../../agents/task_understanding.py#L792) | 792 | `"    if tools and (\"web_search\" in tools or social_required) and not route_is_clarification:"` | — |
| [SRC-686F71AA50-L000793](../../agents/task_understanding.py#L793) | 793 | `"        tools.append(\"claim_review_if_configured\")"` | — |
| [SRC-686F71AA50-L000794](../../agents/task_understanding.py#L794) | 794 | `"    raw_context_entities = context.get(\"entities\")"` | — |
| [SRC-686F71AA50-L000795](../../agents/task_understanding.py#L795) | 795 | `"    context_entities = ["` | — |
| [SRC-686F71AA50-L000796](../../agents/task_understanding.py#L796) | 796 | `"        str(item).strip()[:120]"` | — |
| [SRC-686F71AA50-L000797](../../agents/task_understanding.py#L797) | 797 | `"        for item in raw_context_entities[:8]"` | — |
| [SRC-686F71AA50-L000798](../../agents/task_understanding.py#L798) | 798 | `"        if isinstance(item, str) and item.strip()"` | — |
| [SRC-686F71AA50-L000799](../../agents/task_understanding.py#L799) | 799 | `"    ] if isinstance(raw_context_entities, list) else []"` | — |
| [SRC-686F71AA50-L000800](../../agents/task_understanding.py#L800) | 800 | `"    raw_context_slots = context.get(\"slots\")"` | — |
| [SRC-686F71AA50-L000801](../../agents/task_understanding.py#L801) | 801 | `"    context_slots: dict[str, str] = {}"` | — |
| [SRC-686F71AA50-L000802](../../agents/task_understanding.py#L802) | 802 | `"    if isinstance(raw_context_slots, dict):"` | — |
| [SRC-686F71AA50-L000803](../../agents/task_understanding.py#L803) | 803 | `"        for raw_key, raw_value in list(raw_context_slots.items())[:16]:"` | — |
| [SRC-686F71AA50-L000804](../../agents/task_understanding.py#L804) | 804 | `"            if isinstance(raw_key, str) and isinstance(raw_value, str) and raw_key.strip() and raw_value.strip():"` | — |
| [SRC-686F71AA50-L000805](../../agents/task_understanding.py#L805) | 805 | `"                context_slots[raw_key.strip()[:40]] = raw_value.strip()[:180]"` | — |
| [SRC-686F71AA50-L000806](../../agents/task_understanding.py#L806) | 806 | `"    raw_changed_slots = context.get(\"changed_slots\")"` | — |
| [SRC-686F71AA50-L000807](../../agents/task_understanding.py#L807) | 807 | `"    context_changed_slots = ["` | — |
| [SRC-686F71AA50-L000808](../../agents/task_understanding.py#L808) | 808 | `"        str(item).strip()[:40]"` | — |
| [SRC-686F71AA50-L000809](../../agents/task_understanding.py#L809) | 809 | `"        for item in raw_changed_slots[:8]"` | — |
| [SRC-686F71AA50-L000810](../../agents/task_understanding.py#L810) | 810 | `"        if isinstance(item, str) and item.strip()"` | — |
| [SRC-686F71AA50-L000811](../../agents/task_understanding.py#L811) | 811 | `"    ] if isinstance(raw_changed_slots, list) else []"` | — |
| [SRC-686F71AA50-L000812](../../agents/task_understanding.py#L812) | 812 | `"    context_resolution = {"` | — |
| [SRC-686F71AA50-L000813](../../agents/task_understanding.py#L813) | 813 | `"        \"method\": str(context.get(\"method\") or \"not_provided\")[:80],"` | — |
| [SRC-686F71AA50-L000814](../../agents/task_understanding.py#L814) | 814 | `"        \"resolved_question\": ("` | — |
| [SRC-686F71AA50-L000815](../../agents/task_understanding.py#L815) | 815 | `"            str(context.get(\"resolved_question\") or raw)[:MAX_TASK_CHARS]"` | — |
| [SRC-686F71AA50-L000816](../../agents/task_understanding.py#L816) | 816 | `"            if not context.get(\"topic_shift\") else raw"` | — |
| [SRC-686F71AA50-L000817](../../agents/task_understanding.py#L817) | 817 | `"        ),"` | — |
| [SRC-686F71AA50-L000818](../../agents/task_understanding.py#L818) | 818 | `"        \"topic\": str(context.get(\"topic\") or \"\")[:180],"` | — |
| [SRC-686F71AA50-L000819](../../agents/task_understanding.py#L819) | 819 | `"        \"entities\": context_entities,"` | — |
| [SRC-686F71AA50-L000820](../../agents/task_understanding.py#L820) | 820 | `"        \"slots\": context_slots,"` | — |
| [SRC-686F71AA50-L000821](../../agents/task_understanding.py#L821) | 821 | `"        \"changed_slots\": context_changed_slots,"` | — |
| [SRC-686F71AA50-L000822](../../agents/task_understanding.py#L822) | 822 | `"        \"is_follow_up\": context.get(\"is_follow_up\") is True,"` | — |
| [SRC-686F71AA50-L000823](../../agents/task_understanding.py#L823) | 823 | `"        \"topic_shift\": context.get(\"topic_shift\") is True,"` | — |
| [SRC-686F71AA50-L000824](../../agents/task_understanding.py#L824) | 824 | `"        \"resolution_basis\": str(context.get(\"resolution_basis\") or \"unassessed\")[:80],"` | — |
| [SRC-686F71AA50-L000825](../../agents/task_understanding.py#L825) | 825 | `"        \"confidence_band\": str(context.get(\"confidence_band\") or \"unassessed\")[:30],"` | — |
| [SRC-686F71AA50-L000826](../../agents/task_understanding.py#L826) | 826 | `"        \"needs_clarification\": context.get(\"needs_clarification\") is True,"` | — |
| [SRC-686F71AA50-L000827](../../agents/task_understanding.py#L827) | 827 | `"        \"unresolved_references\": ["` | — |
| [SRC-686F71AA50-L000828](../../agents/task_understanding.py#L828) | 828 | `"            str(item).strip()[:100]"` | — |
| [SRC-686F71AA50-L000829](../../agents/task_understanding.py#L829) | 829 | `"            for item in context.get(\"unresolved_references\", [])[:8]"` | — |
| [SRC-686F71AA50-L000830](../../agents/task_understanding.py#L830) | 830 | `"            if isinstance(item, str) and item.strip()"` | — |
| [SRC-686F71AA50-L000831](../../agents/task_understanding.py#L831) | 831 | `"        ] if isinstance(context.get(\"unresolved_references\"), list) else [],"` | — |
| [SRC-686F71AA50-L000832](../../agents/task_understanding.py#L832) | 832 | `"    }"` | — |
| [SRC-686F71AA50-L000833](../../agents/task_understanding.py#L833) | 833 | `""` | — |
| [SRC-686F71AA50-L000834](../../agents/task_understanding.py#L834) | 834 | `"    constraints = {"` | — |
| [SRC-686F71AA50-L000835](../../agents/task_understanding.py#L835) | 835 | `"        \"explicit_locations\": location,"` | — |
| [SRC-686F71AA50-L000836](../../agents/task_understanding.py#L836) | 836 | `"        \"explicit_years\": years,"` | — |
| [SRC-686F71AA50-L000837](../../agents/task_understanding.py#L837) | 837 | `"        \"explicit_dates\": dates,"` | — |
| [SRC-686F71AA50-L000838](../../agents/task_understanding.py#L838) | 838 | `"        \"explicit_budgets\": budgets,"` | — |
| [SRC-686F71AA50-L000839](../../agents/task_understanding.py#L839) | 839 | `"        \"explicit_urls\": urls,"` | — |
| [SRC-686F71AA50-L000840](../../agents/task_understanding.py#L840) | 840 | `"        \"explicit_aspects\": explicit_aspects,"` | — |
| [SRC-686F71AA50-L000841](../../agents/task_understanding.py#L841) | 841 | `"        \"inline_text_supplied_for_summary\": inline_summary_text,"` | — |
| [SRC-686F71AA50-L000842](../../agents/task_understanding.py#L842) | 842 | `"        \"time_sensitive_request\": current_required,"` | — |
| [SRC-686F71AA50-L000843](../../agents/task_understanding.py#L843) | 843 | `"        \"official_site_required\": government_official_site,"` | — |
| [SRC-686F71AA50-L000844](../../agents/task_understanding.py#L844) | 844 | `"        \"official_destination_required\": official_destination,"` | — |
| [SRC-686F71AA50-L000845](../../agents/task_understanding.py#L845) | 845 | `"        \"social_evidence_requested\": social_required,"` | — |
| [SRC-686F71AA50-L000846](../../agents/task_understanding.py#L846) | 846 | `"        \"language_profile\": _language_profile(raw),"` | — |
| [SRC-686F71AA50-L000847](../../agents/task_understanding.py#L847) | 847 | `"        \"source_policy\": ("` | — |
| [SRC-686F71AA50-L000848](../../agents/task_understanding.py#L848) | 848 | `"            \"government_official_destination\" if government_official_site"` | — |
| [SRC-686F71AA50-L000849](../../agents/task_understanding.py#L849) | 849 | `"            else \"official_destination\" if official_destination"` | — |
| [SRC-686F71AA50-L000850](../../agents/task_understanding.py#L850) | 850 | `"            else \"current_read_page\" if current_required"` | — |
| [SRC-686F71AA50-L000851](../../agents/task_understanding.py#L851) | 851 | `"            else \"public_social_content\" if social_required"` | — |
| [SRC-686F71AA50-L000852](../../agents/task_understanding.py#L852) | 852 | `"            else \"task_relevant_sources\""` | — |
| [SRC-686F71AA50-L000853](../../agents/task_understanding.py#L853) | 853 | `"        ),"` | — |
| [SRC-686F71AA50-L000854](../../agents/task_understanding.py#L854) | 854 | `"        \"source_policies\": list(dict.fromkeys("` | — |
| [SRC-686F71AA50-L000855](../../agents/task_understanding.py#L855) | 855 | `"            ([\"government_official_destination\"] if government_official_site else [])"` | — |
| [SRC-686F71AA50-L000856](../../agents/task_understanding.py#L856) | 856 | `"            + ([\"official_destination\"] if official_destination else [])"` | — |
| [SRC-686F71AA50-L000857](../../agents/task_understanding.py#L857) | 857 | `"            + ([\"current_read_page\"] if current_required else [])"` | — |
| [SRC-686F71AA50-L000858](../../agents/task_understanding.py#L858) | 858 | `"            + ([\"public_social_content\"] if social_required else [])"` | — |
| [SRC-686F71AA50-L000859](../../agents/task_understanding.py#L859) | 859 | `"            + ([\"authoritative_health_content\"] if matches[\"medical_information\"] else [])"` | — |
| [SRC-686F71AA50-L000860](../../agents/task_understanding.py#L860) | 860 | `"            + ([\"official_legal_text\"] if matches[\"legal_information\"] else [])"` | — |
| [SRC-686F71AA50-L000861](../../agents/task_understanding.py#L861) | 861 | `"            + ([\"task_relevant_sources\"] if not (government_official_site or official_destination or current_required or social_required or matches[\"medical_information\"] or matches[\"legal_information\"]) else [])"` | — |
| [SRC-686F71AA50-L000862](../../agents/task_understanding.py#L862) | 862 | `"        )),"` | — |
| [SRC-686F71AA50-L000863](../../agents/task_understanding.py#L863) | 863 | `"    }"` | — |
| [SRC-686F71AA50-L000864](../../agents/task_understanding.py#L864) | 864 | `"    spec = {"` | — |
| [SRC-686F71AA50-L000865](../../agents/task_understanding.py#L865) | 865 | `"        \"schema\": \"omarai.task_spec.v1\","` | — |
| [SRC-686F71AA50-L000866](../../agents/task_understanding.py#L866) | 866 | `"        \"task_family\": family,"` | — |
| [SRC-686F71AA50-L000867](../../agents/task_understanding.py#L867) | 867 | `"        \"mode\": clean_mode,"` | — |
| [SRC-686F71AA50-L000868](../../agents/task_understanding.py#L868) | 868 | `"        \"intent_route\": intent_route or \"unassessed\","` | — |
| [SRC-686F71AA50-L000869](../../agents/task_understanding.py#L869) | 869 | `"        \"normalization\": \"unicode_nfkc_arabic_diacritic_and_letter_normalization\","` | — |
| [SRC-686F71AA50-L000870](../../agents/task_understanding.py#L870) | 870 | `"        \"classification_method\": \"deterministic_multi_pattern_hypotheses\","` | — |
| [SRC-686F71AA50-L000871](../../agents/task_understanding.py#L871) | 871 | `"        \"classification_is_probability\": False,"` | — |
| [SRC-686F71AA50-L000872](../../agents/task_understanding.py#L872) | 872 | `"        \"ambiguity_status\": ambiguity_status,"` | — |
| [SRC-686F71AA50-L000873](../../agents/task_understanding.py#L873) | 873 | `"        \"missing_required_inputs\": list(dict.fromkeys(missing_required_inputs)),"` | — |
| [SRC-686F71AA50-L000874](../../agents/task_understanding.py#L874) | 874 | `"        \"requires_clarification\": ambiguity_status == \"needs_clarification\","` | — |
| [SRC-686F71AA50-L000875](../../agents/task_understanding.py#L875) | 875 | `"        \"context_resolution\": context_resolution,"` | — |
| [SRC-686F71AA50-L000876](../../agents/task_understanding.py#L876) | 876 | `"        \"secondary_task_types\": ["` | — |
| [SRC-686F71AA50-L000877](../../agents/task_understanding.py#L877) | 877 | `"            name for name, signals in matches.items()"` | — |
| [SRC-686F71AA50-L000878](../../agents/task_understanding.py#L878) | 878 | `"            if signals and name != family"` | — |
| [SRC-686F71AA50-L000879](../../agents/task_understanding.py#L879) | 879 | `"        ],"` | — |
| [SRC-686F71AA50-L000880](../../agents/task_understanding.py#L880) | 880 | `"        \"clarification_reason\": ("` | — |
| [SRC-686F71AA50-L000881](../../agents/task_understanding.py#L881) | 881 | `"            \"missing_required_input\""` | — |
| [SRC-686F71AA50-L000882](../../agents/task_understanding.py#L882) | 882 | `"            if missing_required_inputs"` | — |
| [SRC-686F71AA50-L000883](../../agents/task_understanding.py#L883) | 883 | `"            else \"no_strong_lexical_conflict_detected\""` | — |
| [SRC-686F71AA50-L000884](../../agents/task_understanding.py#L884) | 884 | `"        ),"` | — |
| [SRC-686F71AA50-L000885](../../agents/task_understanding.py#L885) | 885 | `"        \"hypothesis_interpretations\": hypothesis_rows,"` | — |
| [SRC-686F71AA50-L000886](../../agents/task_understanding.py#L886) | 886 | `"        \"constraints\": constraints,"` | — |
| [SRC-686F71AA50-L000887](../../agents/task_understanding.py#L887) | 887 | `"        \"output_preferences\": {"` | — |
| [SRC-686F71AA50-L000888](../../agents/task_understanding.py#L888) | 888 | `"            \"concise\": bool(output_matches[\"output_concise\"]),"` | — |
| [SRC-686F71AA50-L000889](../../agents/task_understanding.py#L889) | 889 | `"            \"detailed\": bool(output_matches[\"output_detailed\"]),"` | — |
| [SRC-686F71AA50-L000890](../../agents/task_understanding.py#L890) | 890 | `"            \"examples_requested\": bool(output_matches[\"output_examples\"]),"` | — |
| [SRC-686F71AA50-L000891](../../agents/task_understanding.py#L891) | 891 | `"            \"table_requested\": bool(output_matches[\"output_table\"]),"` | — |
| [SRC-686F71AA50-L000892](../../agents/task_understanding.py#L892) | 892 | `"            \"bullets_or_checklist_requested\": bool(output_matches[\"output_bullets\"]),"` | — |
| [SRC-686F71AA50-L000893](../../agents/task_understanding.py#L893) | 893 | `"            \"beginner_friendly_requested\": bool(output_matches[\"output_beginner_friendly\"]),"` | — |
| [SRC-686F71AA50-L000894](../../agents/task_understanding.py#L894) | 894 | `"            \"citations_requested\": bool(output_matches[\"output_citations\"]),"` | — |
| [SRC-686F71AA50-L000895](../../agents/task_understanding.py#L895) | 895 | `"            \"links_requested\": bool(output_matches[\"output_links\"]),"` | — |
| [SRC-686F71AA50-L000896](../../agents/task_understanding.py#L896) | 896 | `"            \"json_requested\": bool(output_matches[\"output_json\"]),"` | — |
| [SRC-686F71AA50-L000897](../../agents/task_understanding.py#L897) | 897 | `"        },"` | — |
| [SRC-686F71AA50-L000898](../../agents/task_understanding.py#L898) | 898 | `"        \"evidence_requirements\": evidence_requirements,"` | — |
| [SRC-686F71AA50-L000899](../../agents/task_understanding.py#L899) | 899 | `"        \"query_strategies\": query_strategies,"` | — |
| [SRC-686F71AA50-L000900](../../agents/task_understanding.py#L900) | 900 | `"        \"tool_requirements\": list(dict.fromkeys(tools)),"` | — |
| [SRC-686F71AA50-L000901](../../agents/task_understanding.py#L901) | 901 | `"        \"decision_checks\": ["` | — |
| [SRC-686F71AA50-L000902](../../agents/task_understanding.py#L902) | 902 | `"            \"resolve_context_without_carrying_stale_topic\","` | — |
| [SRC-686F71AA50-L000903](../../agents/task_understanding.py#L903) | 903 | `"            \"preserve_explicit_entities_and_constraints\","` | — |
| [SRC-686F71AA50-L000904](../../agents/task_understanding.py#L904) | 904 | `"            \"validate_topic_relevance\","` | — |
| [SRC-686F71AA50-L000905](../../agents/task_understanding.py#L905) | 905 | `"            \"check_tool_permission_and_configuration_before_execution\","` | — |
| [SRC-686F71AA50-L000906](../../agents/task_understanding.py#L906) | 906 | `"            \"bound_query_count_retries_concurrency_and_deadlines\","` | — |
| [SRC-686F71AA50-L000907](../../agents/task_understanding.py#L907) | 907 | `"            \"treat_retrieved_content_as_untrusted_data_not_tool_instructions\","` | — |
| [SRC-686F71AA50-L000908](../../agents/task_understanding.py#L908) | 908 | `"            \"apply_mode_specific_source_guardrails\","` | — |
| [SRC-686F71AA50-L000909](../../agents/task_understanding.py#L909) | 909 | `"            \"distinguish_planned_queries_from_queries_actually_attempted\","` | — |
| [SRC-686F71AA50-L000910](../../agents/task_understanding.py#L910) | 910 | `"            \"distinguish_search_snippets_from_successfully_read_pages\","` | — |
| [SRC-686F71AA50-L000911](../../agents/task_understanding.py#L911) | 911 | `"            \"separate_connector_success_from_evidence_validity\","` | — |
| [SRC-686F71AA50-L000912](../../agents/task_understanding.py#L912) | 912 | `"            \"report_each_failed_stage_without_claiming_unperformed_checks\","` | — |
| [SRC-686F71AA50-L000913](../../agents/task_understanding.py#L913) | 913 | `"            \"cite_claims_or_abstain_when_evidence_is_insufficient\","` | — |
| [SRC-686F71AA50-L000914](../../agents/task_understanding.py#L914) | 914 | `"        ],"` | — |
| [SRC-686F71AA50-L000915](../../agents/task_understanding.py#L915) | 915 | `"        \"reasoning_strategy_ids\": _reasoning_strategy_ids("` | — |
| [SRC-686F71AA50-L000916](../../agents/task_understanding.py#L916) | 916 | `"            family, constraints, context_resolution, missing_required_inputs"` | — |
| [SRC-686F71AA50-L000917](../../agents/task_understanding.py#L917) | 917 | `"        ),"` | — |
| [SRC-686F71AA50-L000918](../../agents/task_understanding.py#L918) | 918 | `"        \"decision_matrix\": [dict(row) for row in _DECISION_MATRIX],"` | — |
| [SRC-686F71AA50-L000919](../../agents/task_understanding.py#L919) | 919 | `"        \"limits\": {"` | — |
| [SRC-686F71AA50-L000920](../../agents/task_understanding.py#L920) | 920 | `"            \"max_question_chars\": MAX_TASK_CHARS,"` | — |
| [SRC-686F71AA50-L000921](../../agents/task_understanding.py#L921) | 921 | `"            \"max_aspects\": MAX_TASK_ASPECTS,"` | — |
| [SRC-686F71AA50-L000922](../../agents/task_understanding.py#L922) | 922 | `"            \"max_query_strategies\": MAX_STRATEGY_QUERIES,"` | — |
| [SRC-686F71AA50-L000923](../../agents/task_understanding.py#L923) | 923 | `"        },"` | — |
| [SRC-686F71AA50-L000924](../../agents/task_understanding.py#L924) | 924 | `"        \"claim\": \"task planning metadata only; not semantic certainty or factual verification\","` | — |
| [SRC-686F71AA50-L000925](../../agents/task_understanding.py#L925) | 925 | `"    }"` | — |
| [SRC-686F71AA50-L000926](../../agents/task_understanding.py#L926) | 926 | `"    if plan and isinstance(plan, dict):"` | — |
| [SRC-686F71AA50-L000927](../../agents/task_understanding.py#L927) | 927 | `"        spec[\"planner_freshness\"] = str(plan.get(\"freshness\") or \"unknown\")"` | — |
| [SRC-686F71AA50-L000928](../../agents/task_understanding.py#L928) | 928 | `"        spec[\"planner_depth\"] = str(plan.get(\"depth\") or \"unknown\")"` | — |
| [SRC-686F71AA50-L000929](../../agents/task_understanding.py#L929) | 929 | `"    return spec"` | — |
| [SRC-686F71AA50-L000930](../../agents/task_understanding.py#L930) | 930 | `""` | — |
| [SRC-686F71AA50-L000931](../../agents/task_understanding.py#L931) | 931 | `""` | — |
| [SRC-686F71AA50-L000932](../../agents/task_understanding.py#L932) | 932 | `"def _query_key(value: str) -> str:"` | — |
| [SRC-686F71AA50-L000933](../../agents/task_understanding.py#L933) | 933 | `"    return normalize_text(value)"` | — |
| [SRC-686F71AA50-L000934](../../agents/task_understanding.py#L934) | 934 | `""` | — |
| [SRC-686F71AA50-L000935](../../agents/task_understanding.py#L935) | 935 | `""` | — |
| [SRC-686F71AA50-L000936](../../agents/task_understanding.py#L936) | 936 | `"def _generated_strategy_candidates(topic: str, spec: dict[str, Any]) -> list[tuple[str, str, str]]:"` | — |
| [SRC-686F71AA50-L000937](../../agents/task_understanding.py#L937) | 937 | `"    family = str(spec.get(\"task_family\") or \"\")"` | — |
| [SRC-686F71AA50-L000938](../../agents/task_understanding.py#L938) | 938 | `"    constraints = spec.get(\"constraints\") if isinstance(spec.get(\"constraints\"), dict) else {}"` | — |
| [SRC-686F71AA50-L000939](../../agents/task_understanding.py#L939) | 939 | `"    aspects = constraints.get(\"explicit_aspects\") if isinstance(constraints.get(\"explicit_aspects\"), list) else []"` | — |
| [SRC-686F71AA50-L000940](../../agents/task_understanding.py#L940) | 940 | `"    candidates: list[tuple[str, str, str]] = []"` | — |
| [SRC-686F71AA50-L000941](../../agents/task_understanding.py#L941) | 941 | `"    if not topic.strip():"` | — |
| [SRC-686F71AA50-L000942](../../agents/task_understanding.py#L942) | 942 | `"        return candidates"` | — |
| [SRC-686F71AA50-L000943](../../agents/task_understanding.py#L943) | 943 | `"    locations = constraints.get(\"explicit_locations\") or []"` | — |
| [SRC-686F71AA50-L000944](../../agents/task_understanding.py#L944) | 944 | `"    location_suffix = \" \".join(str(item) for item in locations[:2])"` | — |
| [SRC-686F71AA50-L000945](../../agents/task_understanding.py#L945) | 945 | `"    hypotheses = spec.get(\"hypothesis_interpretations\")"` | — |
| [SRC-686F71AA50-L000946](../../agents/task_understanding.py#L946) | 946 | `"    hypothesis_families = {"` | — |
| [SRC-686F71AA50-L000947](../../agents/task_understanding.py#L947) | 947 | `"        str(item.get(\"family\"))"` | — |
| [SRC-686F71AA50-L000948](../../agents/task_understanding.py#L948) | 948 | `"        for item in hypotheses"` | — |
| [SRC-686F71AA50-L000949](../../agents/task_understanding.py#L949) | 949 | `"        if isinstance(item, dict) and item.get(\"family\")"` | — |
| [SRC-686F71AA50-L000950](../../agents/task_understanding.py#L950) | 950 | `"    } if isinstance(hypotheses, list) else set()"` | — |
| [SRC-686F71AA50-L000951](../../agents/task_understanding.py#L951) | 951 | `"    if family == \"official_site_lookup\" or constraints.get(\"official_destination_required\"):"` | — |
| [SRC-686F71AA50-L000952](../../agents/task_understanding.py#L952) | 952 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000953](../../agents/task_understanding.py#L953) | 953 | `"            (f\"{topic} الموقع الرسمي\", \"official_destination\", \"exact official-site discovery\"),"` | — |
| [SRC-686F71AA50-L000954](../../agents/task_understanding.py#L954) | 954 | `"            (f\"{topic} official website government portal\", \"official_domain\", \"cross-language destination discovery\"),"` | — |
| [SRC-686F71AA50-L000955](../../agents/task_understanding.py#L955) | 955 | `"        ])"` | — |
| [SRC-686F71AA50-L000956](../../agents/task_understanding.py#L956) | 956 | `"    if constraints.get(\"time_sensitive_request\"):"` | — |
| [SRC-686F71AA50-L000957](../../agents/task_understanding.py#L957) | 957 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000958](../../agents/task_understanding.py#L958) | 958 | `"            (f\"{topic} تحديث رسمي حديث {location_suffix}\".strip(), \"recent_official_update\", \"current-state fact requires fresh primary evidence\"),"` | — |
| [SRC-686F71AA50-L000959](../../agents/task_understanding.py#L959) | 959 | `"            (f\"{topic} latest official update {location_suffix}\".strip(), \"recent_official_update_en\", \"alternate language and source wording\"),"` | — |
| [SRC-686F71AA50-L000960](../../agents/task_understanding.py#L960) | 960 | `"        ])"` | — |
| [SRC-686F71AA50-L000961](../../agents/task_understanding.py#L961) | 961 | `"    if family == \"social_opinions\" or constraints.get(\"social_evidence_requested\"):"` | — |
| [SRC-686F71AA50-L000962](../../agents/task_understanding.py#L962) | 962 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000963](../../agents/task_understanding.py#L963) | 963 | `"            (f\"{topic} تجارب مستخدمين آراء الملاك {location_suffix}\".strip(), \"personal_experience_ar\", \"search for first-person experience rather than generic product mentions\"),"` | — |
| [SRC-686F71AA50-L000964](../../agents/task_understanding.py#L964) | 964 | `"            (f\"{topic} owner experience review {location_suffix}\".strip(), \"personal_experience_en\", \"cross-language owner-experience discovery\"),"` | — |
| [SRC-686F71AA50-L000965](../../agents/task_understanding.py#L965) | 965 | `"            (f\"{topic} common complaints discussion\", \"discussion_and_complaints\", \"look for contrasting experiences and discussions\"),"` | — |
| [SRC-686F71AA50-L000966](../../agents/task_understanding.py#L966) | 966 | `"        ])"` | — |
| [SRC-686F71AA50-L000967](../../agents/task_understanding.py#L967) | 967 | `"    if family == \"compare\" or \"compare\" in hypothesis_families:"` | — |
| [SRC-686F71AA50-L000968](../../agents/task_understanding.py#L968) | 968 | `"        for aspect in aspects[:MAX_TASK_ASPECTS]:"` | — |
| [SRC-686F71AA50-L000969](../../agents/task_understanding.py#L969) | 969 | `"            candidates.append((f\"{topic} {aspect}\", \"explicit_criterion\", f\"separate evidence retrieval for criterion: {aspect}\"))"` | — |
| [SRC-686F71AA50-L000970](../../agents/task_understanding.py#L970) | 970 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000971](../../agents/task_understanding.py#L971) | 971 | `"            (f\"{topic} official specifications\", \"primary_specification\", \"separate technical specifications from opinion\"),"` | — |
| [SRC-686F71AA50-L000972](../../agents/task_understanding.py#L972) | 972 | `"            (f\"{topic} independent comparison pros cons\", \"independent_comparison\", \"seek comparative analysis and trade-offs\"),"` | — |
| [SRC-686F71AA50-L000973](../../agents/task_understanding.py#L973) | 973 | `"        ])"` | — |
| [SRC-686F71AA50-L000974](../../agents/task_understanding.py#L974) | 974 | `"    if family == \"troubleshoot\" or \"troubleshoot\" in hypothesis_families:"` | — |
| [SRC-686F71AA50-L000975](../../agents/task_understanding.py#L975) | 975 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000976](../../agents/task_understanding.py#L976) | 976 | `"            (f\"{topic} الأعطال الشائعة الأسباب والحلول\", \"failure_modes_ar\", \"search causes and remedies without treating hypotheses as confirmed\"),"` | — |
| [SRC-686F71AA50-L000977](../../agents/task_understanding.py#L977) | 977 | `"            (f\"{topic} troubleshooting common failures official manual\", \"failure_modes_en\", \"technical cross-language search and primary manual\"),"` | — |
| [SRC-686F71AA50-L000978](../../agents/task_understanding.py#L978) | 978 | `"        ])"` | — |
| [SRC-686F71AA50-L000979](../../agents/task_understanding.py#L979) | 979 | `"    if family == \"how_to\" or \"how_to\" in hypothesis_families:"` | — |
| [SRC-686F71AA50-L000980](../../agents/task_understanding.py#L980) | 980 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000981](../../agents/task_understanding.py#L981) | 981 | `"            (f\"{topic} خطوات شرح دليل رسمي\", \"procedural_guide_ar\", \"seek stepwise procedure and applicable prerequisites\"),"` | — |
| [SRC-686F71AA50-L000982](../../agents/task_understanding.py#L982) | 982 | `"            (f\"{topic} official guide steps\", \"procedural_guide_en\", \"cross-language guide discovery\"),"` | — |
| [SRC-686F71AA50-L000983](../../agents/task_understanding.py#L983) | 983 | `"        ])"` | — |
| [SRC-686F71AA50-L000984](../../agents/task_understanding.py#L984) | 984 | `"    if family == \"recommendation\" or \"recommendation\" in hypothesis_families:"` | — |
| [SRC-686F71AA50-L000985](../../agents/task_understanding.py#L985) | 985 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000986](../../agents/task_understanding.py#L986) | 986 | `"            (f\"{topic} المميزات العيوب البدائل\", \"tradeoffs_ar\", \"compare trade-offs and alternatives\"),"` | — |
| [SRC-686F71AA50-L000987](../../agents/task_understanding.py#L987) | 987 | `"            (f\"{topic} pros cons alternatives review\", \"tradeoffs_en\", \"cross-language alternatives discovery\"),"` | — |
| [SRC-686F71AA50-L000988](../../agents/task_understanding.py#L988) | 988 | `"        ])"` | — |
| [SRC-686F71AA50-L000989](../../agents/task_understanding.py#L989) | 989 | `"    if family == \"lead_generation\" or \"lead_generation\" in hypothesis_families:"` | — |
| [SRC-686F71AA50-L000990](../../agents/task_understanding.py#L990) | 990 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000991](../../agents/task_understanding.py#L991) | 991 | `"            (f\"{topic} شخص يبحث عن شراء تجربة سؤال\", \"buyer_intent_ar\", \"distinguish explicit buyer intent from product advertisements\"),"` | — |
| [SRC-686F71AA50-L000992](../../agents/task_understanding.py#L992) | 992 | `"            (f\"{topic} looking to buy seeking recommendations\", \"buyer_intent_en\", \"search public discussions for intent signals\"),"` | — |
| [SRC-686F71AA50-L000993](../../agents/task_understanding.py#L993) | 993 | `"        ])"` | — |
| [SRC-686F71AA50-L000994](../../agents/task_understanding.py#L994) | 994 | `"    if family == \"medical_information\" and ("` | — |
| [SRC-686F71AA50-L000995](../../agents/task_understanding.py#L995) | 995 | `"        spec.get(\"mode\") in {\"deep\", \"latest\"} or spec.get(\"intent_route\") == \"WEB_DEEP\""` | — |
| [SRC-686F71AA50-L000996](../../agents/task_understanding.py#L996) | 996 | `"    ):"` | — |
| [SRC-686F71AA50-L000997](../../agents/task_understanding.py#L997) | 997 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L000998](../../agents/task_understanding.py#L998) | 998 | `"            (f\"{topic} مصدر صحي رسمي إرشادات\", \"authoritative_health_source\", \"prefer current public health guidance, not a personal diagnosis\"),"` | — |
| [SRC-686F71AA50-L000999](../../agents/task_understanding.py#L999) | 999 | `"            (f\"{topic} clinical guidance evidence limitations\", \"clinical_evidence_context\", \"look for evidence quality and documented limitations\"),"` | — |
| [SRC-686F71AA50-L001000](../../agents/task_understanding.py#L1000) | 1000 | `"        ])"` | — |
| [SRC-686F71AA50-L001001](../../agents/task_understanding.py#L1001) | 1001 | `"    if family == \"legal_information\" and ("` | — |
| [SRC-686F71AA50-L001002](../../agents/task_understanding.py#L1002) | 1002 | `"        spec.get(\"mode\") in {\"deep\", \"latest\"} or spec.get(\"intent_route\") == \"WEB_DEEP\""` | — |
| [SRC-686F71AA50-L001003](../../agents/task_understanding.py#L1003) | 1003 | `"    ):"` | — |
| [SRC-686F71AA50-L001004](../../agents/task_understanding.py#L1004) | 1004 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L001005](../../agents/task_understanding.py#L1005) | 1005 | `"            (f\"{topic} نص قانوني رسمي التشريع\", \"official_legal_text\", \"seek primary law or regulator text and verify jurisdiction\"),"` | — |
| [SRC-686F71AA50-L001006](../../agents/task_understanding.py#L1006) | 1006 | `"            (f\"{topic} jurisdiction effective date legal interpretation\", \"jurisdiction_and_effective_date\", \"keep jurisdiction and effective date visible\"),"` | — |
| [SRC-686F71AA50-L001007](../../agents/task_understanding.py#L1007) | 1007 | `"        ])"` | — |
| [SRC-686F71AA50-L001008](../../agents/task_understanding.py#L1008) | 1008 | `"    if family == \"coding_or_technical_design\" and ("` | — |
| [SRC-686F71AA50-L001009](../../agents/task_understanding.py#L1009) | 1009 | `"        spec.get(\"mode\") in {\"deep\", \"latest\"} or spec.get(\"intent_route\") == \"WEB_DEEP\""` | — |
| [SRC-686F71AA50-L001010](../../agents/task_understanding.py#L1010) | 1010 | `"    ):"` | — |
| [SRC-686F71AA50-L001011](../../agents/task_understanding.py#L1011) | 1011 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L001012](../../agents/task_understanding.py#L1012) | 1012 | `"            (f\"{topic} official documentation\", \"official_technical_docs\", \"prefer the language/runtime's authoritative documentation\"),"` | — |
| [SRC-686F71AA50-L001013](../../agents/task_understanding.py#L1013) | 1013 | `"            (f\"{topic} exact error regression test\", \"error_and_regression_test\", \"look for a reproducible error and a testable fix\"),"` | — |
| [SRC-686F71AA50-L001014](../../agents/task_understanding.py#L1014) | 1014 | `"        ])"` | — |
| [SRC-686F71AA50-L001015](../../agents/task_understanding.py#L1015) | 1015 | `"    if family == \"planning\" and ("` | — |
| [SRC-686F71AA50-L001016](../../agents/task_understanding.py#L1016) | 1016 | `"        spec.get(\"mode\") in {\"deep\", \"latest\"} or spec.get(\"intent_route\") == \"WEB_DEEP\""` | — |
| [SRC-686F71AA50-L001017](../../agents/task_understanding.py#L1017) | 1017 | `"    ):"` | — |
| [SRC-686F71AA50-L001018](../../agents/task_understanding.py#L1018) | 1018 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L001019](../../agents/task_understanding.py#L1019) | 1019 | `"            (f\"{topic} risks dependencies feasibility\", \"feasibility_and_dependencies\", \"test assumptions, dependencies, and likely blockers\"),"` | — |
| [SRC-686F71AA50-L001020](../../agents/task_understanding.py#L1020) | 1020 | `"            (f\"{topic} alternative plan fallback\", \"alternatives_and_fallback\", \"seek alternatives and fallback approaches\"),"` | — |
| [SRC-686F71AA50-L001021](../../agents/task_understanding.py#L1021) | 1021 | `"        ])"` | — |
| [SRC-686F71AA50-L001022](../../agents/task_understanding.py#L1022) | 1022 | `"    normalized_topic = normalize_text(topic)"` | — |
| [SRC-686F71AA50-L001023](../../agents/task_understanding.py#L1023) | 1023 | `"    property_topic = any("` | — |
| [SRC-686F71AA50-L001024](../../agents/task_understanding.py#L1024) | 1024 | `"        cue in normalized_topic"` | — |
| [SRC-686F71AA50-L001025](../../agents/task_understanding.py#L1025) | 1025 | `"        for cue in (\"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"عقاري\", \"real estate\", \"apartment\", \"property\")"` | — |
| [SRC-686F71AA50-L001026](../../agents/task_understanding.py#L1026) | 1026 | `"    )"` | — |
| [SRC-686F71AA50-L001027](../../agents/task_understanding.py#L1027) | 1027 | `"    if family == \"find_or_discover\" and property_topic:"` | — |
| [SRC-686F71AA50-L001028](../../agents/task_understanding.py#L1028) | 1028 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L001029](../../agents/task_understanding.py#L1029) | 1029 | `"            (f\"{topic} إعلانات عقارية\", \"property_listings\", \"discover relevant listings without treating ads as independent price evidence\"),"` | — |
| [SRC-686F71AA50-L001030](../../agents/task_understanding.py#L1030) | 1030 | `"            (f\"{topic} متوسط أسعار السوق للمتر\", \"property_market_price_per_meter\", \"compare asking prices against market-level context\"),"` | — |
| [SRC-686F71AA50-L001031](../../agents/task_understanding.py#L1031) | 1031 | `"            (f\"{topic} أسعار البيع الفعلية والتقييم العقاري\", \"property_transaction_price_check\", \"distinguish asking prices from completed transaction prices\"),"` | — |
| [SRC-686F71AA50-L001032](../../agents/task_understanding.py#L1032) | 1032 | `"        ])"` | — |
| [SRC-686F71AA50-L001033](../../agents/task_understanding.py#L1033) | 1033 | `"    if ("` | — |
| [SRC-686F71AA50-L001034](../../agents/task_understanding.py#L1034) | 1034 | `"        family in {\"general_research\", \"web_research\", \"find_or_discover\"}"` | — |
| [SRC-686F71AA50-L001035](../../agents/task_understanding.py#L1035) | 1035 | `"        and ("` | — |
| [SRC-686F71AA50-L001036](../../agents/task_understanding.py#L1036) | 1036 | `"            spec.get(\"mode\") in {\"deep\", \"latest\", \"social\"}"` | — |
| [SRC-686F71AA50-L001037](../../agents/task_understanding.py#L1037) | 1037 | `"            or constraints.get(\"time_sensitive_request\")"` | — |
| [SRC-686F71AA50-L001038](../../agents/task_understanding.py#L1038) | 1038 | `"            or spec.get(\"planner_depth\") == \"deep\""` | — |
| [SRC-686F71AA50-L001039](../../agents/task_understanding.py#L1039) | 1039 | `"            or spec.get(\"intent_route\") in {\"WEB_DEEP\", \"LEAD_GENERATION\"}"` | — |
| [SRC-686F71AA50-L001040](../../agents/task_understanding.py#L1040) | 1040 | `"        )"` | — |
| [SRC-686F71AA50-L001041](../../agents/task_understanding.py#L1041) | 1041 | `"    ):"` | — |
| [SRC-686F71AA50-L001042](../../agents/task_understanding.py#L1042) | 1042 | `"        candidates.extend(["` | — |
| [SRC-686F71AA50-L001043](../../agents/task_understanding.py#L1043) | 1043 | `"            (f\"{topic} مصدر رسمي\", \"primary_source_ar\", \"prefer an original or primary source when appropriate\"),"` | — |
| [SRC-686F71AA50-L001044](../../agents/task_understanding.py#L1044) | 1044 | `"            (f\"{topic} official source report\", \"primary_source_en\", \"alternate source-oriented search wording\"),"` | — |
| [SRC-686F71AA50-L001045](../../agents/task_understanding.py#L1045) | 1045 | `"            (f\"{topic} limitations risks independent analysis\", \"independent_analysis\", \"seek counterevidence and limitations\"),"` | — |
| [SRC-686F71AA50-L001046](../../agents/task_understanding.py#L1046) | 1046 | `"        ])"` | — |
| [SRC-686F71AA50-L001047](../../agents/task_understanding.py#L1047) | 1047 | `"    if ("` | — |
| [SRC-686F71AA50-L001048](../../agents/task_understanding.py#L1048) | 1048 | `"        not candidates"` | — |
| [SRC-686F71AA50-L001049](../../agents/task_understanding.py#L1049) | 1049 | `"        and family in {"` | — |
| [SRC-686F71AA50-L001050](../../agents/task_understanding.py#L1050) | 1050 | `"            \"official_site_lookup\", \"current_information\", \"social_opinions\","` | — |
| [SRC-686F71AA50-L001051](../../agents/task_understanding.py#L1051) | 1051 | `"            \"compare\", \"troubleshoot\", \"how_to\", \"recommendation\","` | — |
| [SRC-686F71AA50-L001052](../../agents/task_understanding.py#L1052) | 1052 | `"            \"lead_generation\", \"general_research\", \"web_research\", \"find_or_discover\","` | — |
| [SRC-686F71AA50-L001053](../../agents/task_understanding.py#L1053) | 1053 | `"            \"medical_information\", \"legal_information\", \"coding_or_technical_design\","` | — |
| [SRC-686F71AA50-L001054](../../agents/task_understanding.py#L1054) | 1054 | `"            \"planning\","` | — |
| [SRC-686F71AA50-L001055](../../agents/task_understanding.py#L1055) | 1055 | `"        }"` | — |
| [SRC-686F71AA50-L001056](../../agents/task_understanding.py#L1056) | 1056 | `"        and ("` | — |
| [SRC-686F71AA50-L001057](../../agents/task_understanding.py#L1057) | 1057 | `"            spec.get(\"mode\") in {\"deep\", \"latest\", \"social\"}"` | — |
| [SRC-686F71AA50-L001058](../../agents/task_understanding.py#L1058) | 1058 | `"            or spec.get(\"intent_route\") in {\"WEB_DEEP\", \"LEAD_GENERATION\"}"` | — |
| [SRC-686F71AA50-L001059](../../agents/task_understanding.py#L1059) | 1059 | `"        )"` | — |
| [SRC-686F71AA50-L001060](../../agents/task_understanding.py#L1060) | 1060 | `"    ):"` | — |
| [SRC-686F71AA50-L001061](../../agents/task_understanding.py#L1061) | 1061 | `"        candidates.append("` | — |
| [SRC-686F71AA50-L001062](../../agents/task_understanding.py#L1062) | 1062 | `"            (f\"{topic} مصدر موثوق\", \"source_oriented_alternative\", \"search wording is a hypothesis, not evidence\")"` | — |
| [SRC-686F71AA50-L001063](../../agents/task_understanding.py#L1063) | 1063 | `"        )"` | — |
| [SRC-686F71AA50-L001064](../../agents/task_understanding.py#L1064) | 1064 | `"    return candidates"` | — |
| [SRC-686F71AA50-L001065](../../agents/task_understanding.py#L1065) | 1065 | `""` | — |
| [SRC-686F71AA50-L001066](../../agents/task_understanding.py#L1066) | 1066 | `""` | — |
| [SRC-686F71AA50-L001067](../../agents/task_understanding.py#L1067) | 1067 | `"def _label_existing_query(query: str, index: int, spec: dict[str, Any]) -> tuple[str, str]:"` | — |
| [SRC-686F71AA50-L001068](../../agents/task_understanding.py#L1068) | 1068 | `"    \"\"\"Classify query wording for diagnostics; this is not a retrieval-success claim.\"\"\""` | — |
| [SRC-686F71AA50-L001069](../../agents/task_understanding.py#L1069) | 1069 | `"    normalized = normalize_text(query)"` | — |
| [SRC-686F71AA50-L001070](../../agents/task_understanding.py#L1070) | 1070 | `"    constraints = spec.get(\"constraints\") if isinstance(spec.get(\"constraints\"), dict) else {}"` | — |
| [SRC-686F71AA50-L001071](../../agents/task_understanding.py#L1071) | 1071 | `"    if re.search(r\"\\bsite\\s*:\", query, flags=re.IGNORECASE):"` | — |
| [SRC-686F71AA50-L001072](../../agents/task_understanding.py#L1072) | 1072 | `"        return \"platform_scoped\", \"query explicitly scopes a public site or platform\""` | — |
| [SRC-686F71AA50-L001073](../../agents/task_understanding.py#L1073) | 1073 | `"    if constraints.get(\"official_destination_required\") and any("` | — |
| [SRC-686F71AA50-L001074](../../agents/task_understanding.py#L1074) | 1074 | `"        marker in normalized for marker in (\"الموقع الرسمي\", \"official website\", \"official site\")"` | — |
| [SRC-686F71AA50-L001075](../../agents/task_understanding.py#L1075) | 1075 | `"    ):"` | — |
| [SRC-686F71AA50-L001076](../../agents/task_understanding.py#L1076) | 1076 | `"        return \"official_destination\", \"query wording seeks an official destination\""` | — |
| [SRC-686F71AA50-L001077](../../agents/task_understanding.py#L1077) | 1077 | `"    if constraints.get(\"time_sensitive_request\") and any("` | — |
| [SRC-686F71AA50-L001078](../../agents/task_understanding.py#L1078) | 1078 | `"        marker in normalized for marker in (\"latest\", \"recent\", \"today\", \"تحديث\", \"حديث\", \"احدث\", \"اخر\")"` | — |
| [SRC-686F71AA50-L001079](../../agents/task_understanding.py#L1079) | 1079 | `"    ):"` | — |
| [SRC-686F71AA50-L001080](../../agents/task_understanding.py#L1080) | 1080 | `"        return \"recent_information\", \"query wording seeks current information; dates and page readability still require validation\""` | — |
| [SRC-686F71AA50-L001081](../../agents/task_understanding.py#L1081) | 1081 | `"    if any(marker in normalized for marker in (\"تجارب\", \"اراء\", \"تجربه\", \"experience\", \"owner review\", \"user review\")):"` | — |
| [SRC-686F71AA50-L001082](../../agents/task_understanding.py#L1082) | 1082 | `"        return \"personal_experience\", \"query wording targets user experience; the author's identity and truth remain unverified\""` | — |
| [SRC-686F71AA50-L001083](../../agents/task_understanding.py#L1083) | 1083 | `"    if any(marker in normalized for marker in (\"اعطال\", \"الاسباب\", \"الحلول\", \"troubleshooting\", \"common failures\")):"` | — |
| [SRC-686F71AA50-L001084](../../agents/task_understanding.py#L1084) | 1084 | `"        return \"troubleshooting\", \"query wording targets symptoms, causes, or remedies\""` | — |
| [SRC-686F71AA50-L001085](../../agents/task_understanding.py#L1085) | 1085 | `"    if any(marker in normalized for marker in (\"المقارنة\", \"مقارنة\", \"قارن\", \"comparison\", \"versus\", \"pros cons\", \"trade offs\")):"` | — |
| [SRC-686F71AA50-L001086](../../agents/task_understanding.py#L1086) | 1086 | `"        return \"comparison\", \"query wording targets a comparison or trade-off analysis\""` | — |
| [SRC-686F71AA50-L001087](../../agents/task_understanding.py#L1087) | 1087 | `"    if any(marker in normalized for marker in (\"مصدر رسمي\", \"official source\", \"manual\", \"specifications\", \"مواصفات\")):"` | — |
| [SRC-686F71AA50-L001088](../../agents/task_understanding.py#L1088) | 1088 | `"        return \"primary_source\", \"query wording seeks a primary or technical source\""` | — |
| [SRC-686F71AA50-L001089](../../agents/task_understanding.py#L1089) | 1089 | `"    if index == 0:"` | — |
| [SRC-686F71AA50-L001090](../../agents/task_understanding.py#L1090) | 1090 | `"        return \"planner_seed\", \"initial planner query; relevance and source quality are validated later\""` | — |
| [SRC-686F71AA50-L001091](../../agents/task_understanding.py#L1091) | 1091 | `"    return \"planner_alternative\", \"alternate planner query; label is inferred from wording/position\""` | — |
| [SRC-686F71AA50-L001092](../../agents/task_understanding.py#L1092) | 1092 | `""` | — |
| [SRC-686F71AA50-L001093](../../agents/task_understanding.py#L1093) | 1093 | `""` | — |
| [SRC-686F71AA50-L001094](../../agents/task_understanding.py#L1094) | 1094 | `"def build_query_strategy_matrix("` | — |
| [SRC-686F71AA50-L001095](../../agents/task_understanding.py#L1095) | 1095 | `"    question: str,"` | — |
| [SRC-686F71AA50-L001096](../../agents/task_understanding.py#L1096) | 1096 | `"    task_spec: dict[str, Any],"` | — |
| [SRC-686F71AA50-L001097](../../agents/task_understanding.py#L1097) | 1097 | `"    existing_queries: Any,"` | — |
| [SRC-686F71AA50-L001098](../../agents/task_understanding.py#L1098) | 1098 | `"    *,"` | — |
| [SRC-686F71AA50-L001099](../../agents/task_understanding.py#L1099) | 1099 | `"    limit: int = MAX_STRATEGY_QUERIES,"` | — |
| [SRC-686F71AA50-L001100](../../agents/task_understanding.py#L1100) | 1100 | `"    compact_fn: Any = None,"` | — |
| [SRC-686F71AA50-L001101](../../agents/task_understanding.py#L1101) | 1101 | `") -> list[dict[str, str]]:"` | — |
| [SRC-686F71AA50-L001102](../../agents/task_understanding.py#L1102) | 1102 | `"    \"\"\"Return bounded query candidates, prioritizing task-specific evidence strategies."` | — |
| [SRC-686F71AA50-L001103](../../agents/task_understanding.py#L1103) | 1103 | `""` | — |
| [SRC-686F71AA50-L001104](../../agents/task_understanding.py#L1104) | 1104 | `"    The first existing planner query anchors the topic. Task-aware queries are then"` | — |
| [SRC-686F71AA50-L001105](../../agents/task_understanding.py#L1105) | 1105 | `"    considered before secondary planner queries, so generic alternatives cannot consume"` | — |
| [SRC-686F71AA50-L001106](../../agents/task_understanding.py#L1106) | 1106 | `"    the whole budget and crowd out explicit user criteria."` | — |
| [SRC-686F71AA50-L001107](../../agents/task_understanding.py#L1107) | 1107 | `"    \"\"\""` | — |
| [SRC-686F71AA50-L001108](../../agents/task_understanding.py#L1108) | 1108 | `"    maximum = max(1, min(int(limit), MAX_STRATEGY_QUERIES))"` | — |
| [SRC-686F71AA50-L001109](../../agents/task_understanding.py#L1109) | 1109 | `"    spec = task_spec if isinstance(task_spec, dict) else {}"` | — |
| [SRC-686F71AA50-L001110](../../agents/task_understanding.py#L1110) | 1110 | `"    queries = existing_queries if isinstance(existing_queries, list) else []"` | — |
| [SRC-686F71AA50-L001111](../../agents/task_understanding.py#L1111) | 1111 | `"    rows: list[dict[str, str]] = []"` | — |
| [SRC-686F71AA50-L001112](../../agents/task_understanding.py#L1112) | 1112 | `"    seen: set[str] = set()"` | — |
| [SRC-686F71AA50-L001113](../../agents/task_understanding.py#L1113) | 1113 | `""` | — |
| [SRC-686F71AA50-L001114](../../agents/task_understanding.py#L1114) | 1114 | `"    def add(query: Any, strategy: str, rationale: str, *, enforce_topic: bool = True) -> None:"` | — |
