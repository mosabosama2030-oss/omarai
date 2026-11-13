# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **012**
- سجلات الأسطر: **800**
- النطاق: SRC-686F71AA50-L001351 إلى SRC-0799EEEB02-L000063
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-686F71AA50 — [agents/task_understanding.py](../../agents/task_understanding.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-686F71AA50-L001351](../../agents/task_understanding.py#L1351) | 1351 | `"            \"aspect\": {"` | — |
| [SRC-686F71AA50-L001352](../../agents/task_understanding.py#L1352) | 1352 | `"                normalize_text(\"الضمان\"): (\"الضمان\", \"ضمان\", \"warranty\", \"guarantee\"),"` | — |
| [SRC-686F71AA50-L001353](../../agents/task_understanding.py#L1353) | 1353 | `"                normalize_text(\"التقييمات\"): (\"التقييمات\", \"التقييم\", \"reviews\", \"ratings\", \"review\"),"` | — |
| [SRC-686F71AA50-L001354](../../agents/task_understanding.py#L1354) | 1354 | `"                normalize_text(\"المراجعات\"): (\"المراجعات\", \"مراجعات\", \"reviews\", \"ratings\"),"` | — |
| [SRC-686F71AA50-L001355](../../agents/task_understanding.py#L1355) | 1355 | `"                normalize_text(\"الصيانة\"): (\"الصيانة\", \"الصيانه\", \"maintenance\", \"repair\", \"service\"),"` | — |
| [SRC-686F71AA50-L001356](../../agents/task_understanding.py#L1356) | 1356 | `"                normalize_text(\"السعر\"): (\"السعر\", \"سعر\", \"price\", \"pricing\", \"cost\"),"` | — |
| [SRC-686F71AA50-L001357](../../agents/task_understanding.py#L1357) | 1357 | `"            },"` | — |
| [SRC-686F71AA50-L001358](../../agents/task_understanding.py#L1358) | 1358 | `"            \"capacity\": {"` | — |
| [SRC-686F71AA50-L001359](../../agents/task_understanding.py#L1359) | 1359 | `"                normalize_text(\"256 جيجابايت\"): (\"256 جيجابايت\", \"256gb\", \"256 gb\"),"` | — |
| [SRC-686F71AA50-L001360](../../agents/task_understanding.py#L1360) | 1360 | `"                normalize_text(\"512 جيجابايت\"): (\"512 جيجابايت\", \"512gb\", \"512 gb\"),"` | — |
| [SRC-686F71AA50-L001361](../../agents/task_understanding.py#L1361) | 1361 | `"                normalize_text(\"1 تيرابايت\"): (\"1 تيرابايت\", \"1tb\", \"1 tb\", \"1024gb\"),"` | — |
| [SRC-686F71AA50-L001362](../../agents/task_understanding.py#L1362) | 1362 | `"            },"` | — |
| [SRC-686F71AA50-L001363](../../agents/task_understanding.py#L1363) | 1363 | `"        }"` | — |
| [SRC-686F71AA50-L001364](../../agents/task_understanding.py#L1364) | 1364 | `"        changed = ("` | — |
| [SRC-686F71AA50-L001365](../../agents/task_understanding.py#L1365) | 1365 | `"            context_resolution.get(\"changed_slots\")"` | — |
| [SRC-686F71AA50-L001366](../../agents/task_understanding.py#L1366) | 1366 | `"            if isinstance(context_resolution.get(\"changed_slots\"), list) else []"` | — |
| [SRC-686F71AA50-L001367](../../agents/task_understanding.py#L1367) | 1367 | `"        )"` | — |
| [SRC-686F71AA50-L001368](../../agents/task_understanding.py#L1368) | 1368 | `"        slots = ("` | — |
| [SRC-686F71AA50-L001369](../../agents/task_understanding.py#L1369) | 1369 | `"            context_resolution.get(\"slots\")"` | — |
| [SRC-686F71AA50-L001370](../../agents/task_understanding.py#L1370) | 1370 | `"            if isinstance(context_resolution.get(\"slots\"), dict) else {}"` | — |
| [SRC-686F71AA50-L001371](../../agents/task_understanding.py#L1371) | 1371 | `"        )"` | — |
| [SRC-686F71AA50-L001372](../../agents/task_understanding.py#L1372) | 1372 | `"        relevant = ["` | — |
| [SRC-686F71AA50-L001373](../../agents/task_understanding.py#L1373) | 1373 | `"            slot for slot in changed"` | — |
| [SRC-686F71AA50-L001374](../../agents/task_understanding.py#L1374) | 1374 | `"            if slot in {"` | — |
| [SRC-686F71AA50-L001375](../../agents/task_understanding.py#L1375) | 1375 | `"                \"location\", \"country\", \"budget\", \"currency\", \"time_range\","` | — |
| [SRC-686F71AA50-L001376](../../agents/task_understanding.py#L1376) | 1376 | `"                \"capacity\", \"aspect\", \"version\", \"entity\", \"product\", \"model\", \"variant\","` | — |
| [SRC-686F71AA50-L001377](../../agents/task_understanding.py#L1377) | 1377 | `"            }"` | — |
| [SRC-686F71AA50-L001378](../../agents/task_understanding.py#L1378) | 1378 | `"        ]"` | — |
| [SRC-686F71AA50-L001379](../../agents/task_understanding.py#L1379) | 1379 | `"        if not relevant:"` | — |
| [SRC-686F71AA50-L001380](../../agents/task_understanding.py#L1380) | 1380 | `"            return False"` | — |
| [SRC-686F71AA50-L001381](../../agents/task_understanding.py#L1381) | 1381 | `"        for slot in relevant:"` | — |
| [SRC-686F71AA50-L001382](../../agents/task_understanding.py#L1382) | 1382 | `"            value = slots.get(slot)"` | — |
| [SRC-686F71AA50-L001383](../../agents/task_understanding.py#L1383) | 1383 | `"            if not isinstance(value, str) or not value.strip():"` | — |
| [SRC-686F71AA50-L001384](../../agents/task_understanding.py#L1384) | 1384 | `"                return False"` | — |
| [SRC-686F71AA50-L001385](../../agents/task_understanding.py#L1385) | 1385 | `"            normalized_value = normalize_text(value)"` | — |
| [SRC-686F71AA50-L001386](../../agents/task_understanding.py#L1386) | 1386 | `"            candidates = aliases.get(slot, {}).get(normalized_value, (value,))"` | — |
| [SRC-686F71AA50-L001387](../../agents/task_understanding.py#L1387) | 1387 | `"            if slot == \"budget\":"` | — |
| [SRC-686F71AA50-L001388](../../agents/task_understanding.py#L1388) | 1388 | `"                numbers = {"` | — |
| [SRC-686F71AA50-L001389](../../agents/task_understanding.py#L1389) | 1389 | `"                    item.replace(\",\", \"\").replace(\".\", \"\")"` | — |
| [SRC-686F71AA50-L001390](../../agents/task_understanding.py#L1390) | 1390 | `"                    for item in re.findall(r\"\\d+(?:[,.]\\d+)*\", normalized_value)"` | — |
| [SRC-686F71AA50-L001391](../../agents/task_understanding.py#L1391) | 1391 | `"                }"` | — |
| [SRC-686F71AA50-L001392](../../agents/task_understanding.py#L1392) | 1392 | `"                seed_numbers = {"` | — |
| [SRC-686F71AA50-L001393](../../agents/task_understanding.py#L1393) | 1393 | `"                    item.replace(\",\", \"\").replace(\".\", \"\")"` | — |
| [SRC-686F71AA50-L001394](../../agents/task_understanding.py#L1394) | 1394 | `"                    for item in re.findall(r\"\\d+(?:[,.]\\d+)*\", normalized_seed)"` | — |
| [SRC-686F71AA50-L001395](../../agents/task_understanding.py#L1395) | 1395 | `"                }"` | — |
| [SRC-686F71AA50-L001396](../../agents/task_understanding.py#L1396) | 1396 | `"                if not numbers or not numbers.issubset(seed_numbers):"` | — |
| [SRC-686F71AA50-L001397](../../agents/task_understanding.py#L1397) | 1397 | `"                    return False"` | — |
| [SRC-686F71AA50-L001398](../../agents/task_understanding.py#L1398) | 1398 | `"                continue"` | — |
| [SRC-686F71AA50-L001399](../../agents/task_understanding.py#L1399) | 1399 | `"            if slot == \"capacity\":"` | — |
| [SRC-686F71AA50-L001400](../../agents/task_understanding.py#L1400) | 1400 | `"                numbers = {"` | — |
| [SRC-686F71AA50-L001401](../../agents/task_understanding.py#L1401) | 1401 | `"                    item.replace(\",\", \"\").replace(\".\", \"\")"` | — |
| [SRC-686F71AA50-L001402](../../agents/task_understanding.py#L1402) | 1402 | `"                    for item in re.findall(r\"\\d+(?:[,.]\\d+)*\", normalized_value)"` | — |
| [SRC-686F71AA50-L001403](../../agents/task_understanding.py#L1403) | 1403 | `"                }"` | — |
| [SRC-686F71AA50-L001404](../../agents/task_understanding.py#L1404) | 1404 | `"                seed_numbers = {"` | — |
| [SRC-686F71AA50-L001405](../../agents/task_understanding.py#L1405) | 1405 | `"                    item.replace(\",\", \"\").replace(\".\", \"\")"` | — |
| [SRC-686F71AA50-L001406](../../agents/task_understanding.py#L1406) | 1406 | `"                    for item in re.findall(r\"\\d+(?:[,.]\\d+)*\", normalized_seed)"` | — |
| [SRC-686F71AA50-L001407](../../agents/task_understanding.py#L1407) | 1407 | `"                }"` | — |
| [SRC-686F71AA50-L001408](../../agents/task_understanding.py#L1408) | 1408 | `"                if numbers and numbers.issubset(seed_numbers):"` | — |
| [SRC-686F71AA50-L001409](../../agents/task_understanding.py#L1409) | 1409 | `"                    continue"` | — |
| [SRC-686F71AA50-L001410](../../agents/task_understanding.py#L1410) | 1410 | `"            if not any(normalize_text(alias) in normalized_seed for alias in candidates):"` | — |
| [SRC-686F71AA50-L001411](../../agents/task_understanding.py#L1411) | 1411 | `"                return False"` | — |
| [SRC-686F71AA50-L001412](../../agents/task_understanding.py#L1412) | 1412 | `"        return True"` | — |
| [SRC-686F71AA50-L001413](../../agents/task_understanding.py#L1413) | 1413 | `""` | — |
| [SRC-686F71AA50-L001414](../../agents/task_understanding.py#L1414) | 1414 | `"    planner_seed_is_current = planner_seed_has_current_changed_slots(planner_seed)"` | — |
| [SRC-686F71AA50-L001415](../../agents/task_understanding.py#L1415) | 1415 | `"    primary_seed = ("` | — |
| [SRC-686F71AA50-L001416](../../agents/task_understanding.py#L1416) | 1416 | `"        planner_seed"` | — |
| [SRC-686F71AA50-L001417](../../agents/task_understanding.py#L1417) | 1417 | `"        if planner_seed_is_current"` | — |
| [SRC-686F71AA50-L001418](../../agents/task_understanding.py#L1418) | 1418 | `"        else (resolved_context_seed or context_anchor)"` | — |
| [SRC-686F71AA50-L001419](../../agents/task_understanding.py#L1419) | 1419 | `"        if replace_stale_planner_queries"` | — |
| [SRC-686F71AA50-L001420](../../agents/task_understanding.py#L1420) | 1420 | `"        else (planner_seed or str(question or \"\"))"` | — |
| [SRC-686F71AA50-L001421](../../agents/task_understanding.py#L1421) | 1421 | `"    )"` | — |
| [SRC-686F71AA50-L001422](../../agents/task_understanding.py#L1422) | 1422 | `"    # When the planner seed already contains the updated slots, use that seed"` | — |
| [SRC-686F71AA50-L001423](../../agents/task_understanding.py#L1423) | 1423 | `"    # as the subject anchor too. A different-language context label must not"` | — |
| [SRC-686F71AA50-L001424](../../agents/task_understanding.py#L1424) | 1424 | `"    # reject relevant strategy variants written in the seed's language."` | — |
| [SRC-686F71AA50-L001425](../../agents/task_understanding.py#L1425) | 1425 | `"    topic_anchor_query = ("` | — |
| [SRC-686F71AA50-L001426](../../agents/task_understanding.py#L1426) | 1426 | `"        planner_seed"` | — |
| [SRC-686F71AA50-L001427](../../agents/task_understanding.py#L1427) | 1427 | `"        if planner_seed_is_current"` | — |
| [SRC-686F71AA50-L001428](../../agents/task_understanding.py#L1428) | 1428 | `"        else (context_anchor or planner_seed or str(question or \"\"))"` | — |
| [SRC-686F71AA50-L001429](../../agents/task_understanding.py#L1429) | 1429 | `"    )"` | — |
| [SRC-686F71AA50-L001430](../../agents/task_understanding.py#L1430) | 1430 | `"    if not context_anchor:"` | — |
| [SRC-686F71AA50-L001431](../../agents/task_understanding.py#L1431) | 1431 | `"        topic_anchor_query = re.sub("` | — |
| [SRC-686F71AA50-L001432](../../agents/task_understanding.py#L1432) | 1432 | `"            r\"^(?:من فضلك\|لو سمحت\|ابحث لي\|ابحث\|دورلي\|دور\|اعثر على\|رشح لي\|رشح\|\""` | — |
| [SRC-686F71AA50-L001433](../../agents/task_understanding.py#L1433) | 1433 | `"            r\"please\|search for\|find\|look up\|recommend)\\s*\","` | — |
| [SRC-686F71AA50-L001434](../../agents/task_understanding.py#L1434) | 1434 | `"            \"\","` | — |
| [SRC-686F71AA50-L001435](../../agents/task_understanding.py#L1435) | 1435 | `"            topic_anchor_query,"` | — |
| [SRC-686F71AA50-L001436](../../agents/task_understanding.py#L1436) | 1436 | `"            flags=re.IGNORECASE,"` | — |
| [SRC-686F71AA50-L001437](../../agents/task_understanding.py#L1437) | 1437 | `"        )"` | — |
| [SRC-686F71AA50-L001438](../../agents/task_understanding.py#L1438) | 1438 | `""` | — |
| [SRC-686F71AA50-L001439](../../agents/task_understanding.py#L1439) | 1439 | `"    def add(query: Any, strategy: str, rationale: str, *, enforce_topic: bool = True) -> None:"` | — |
| [SRC-686F71AA50-L001440](../../agents/task_understanding.py#L1440) | 1440 | `"        if not isinstance(query, str) or not query.strip() or len(rows) >= maximum:"` | — |
| [SRC-686F71AA50-L001441](../../agents/task_understanding.py#L1441) | 1441 | `"            return"` | — |
| [SRC-686F71AA50-L001442](../../agents/task_understanding.py#L1442) | 1442 | `"        candidate = query.strip()"` | — |
| [SRC-686F71AA50-L001443](../../agents/task_understanding.py#L1443) | 1443 | `"        if compact_fn is not None:"` | — |
| [SRC-686F71AA50-L001444](../../agents/task_understanding.py#L1444) | 1444 | `"            try:"` | — |
| [SRC-686F71AA50-L001445](../../agents/task_understanding.py#L1445) | 1445 | `"                candidate = compact_fn(candidate) or \"\""` | — |
| [SRC-686F71AA50-L001446](../../agents/task_understanding.py#L1446) | 1446 | `"            except (TypeError, ValueError):"` | — |
| [SRC-686F71AA50-L001447](../../agents/task_understanding.py#L1447) | 1447 | `"                candidate = \"\""` | — |
| [SRC-686F71AA50-L001448](../../agents/task_understanding.py#L1448) | 1448 | `"        candidate = _collapse_repeated_query_phrases("` | — |
| [SRC-686F71AA50-L001449](../../agents/task_understanding.py#L1449) | 1449 | `"            _SPACE.sub(\" \", candidate).strip()"` | — |
| [SRC-686F71AA50-L001450](../../agents/task_understanding.py#L1450) | 1450 | `"        )"` | — |
| [SRC-686F71AA50-L001451](../../agents/task_understanding.py#L1451) | 1451 | `"        # Preserve explicit geography, commercial bounds, and material semantic slots"` | — |
| [SRC-686F71AA50-L001452](../../agents/task_understanding.py#L1452) | 1452 | `"        # from a validated follow-up. Never inherit them after a topic shift or clarification."` | — |
| [SRC-686F71AA50-L001453](../../agents/task_understanding.py#L1453) | 1453 | `"        scope_terms: list[tuple[str, str]] = []"` | — |
| [SRC-686F71AA50-L001454](../../agents/task_understanding.py#L1454) | 1454 | `"        raw_locations = constraints.get(\"explicit_locations\")"` | — |
| [SRC-686F71AA50-L001455](../../agents/task_understanding.py#L1455) | 1455 | `"        if isinstance(raw_locations, list):"` | — |
| [SRC-686F71AA50-L001456](../../agents/task_understanding.py#L1456) | 1456 | `"            scope_terms.extend("` | — |
| [SRC-686F71AA50-L001457](../../agents/task_understanding.py#L1457) | 1457 | `"                (item.strip(), \"location\") for item in raw_locations[:5]"` | — |
| [SRC-686F71AA50-L001458](../../agents/task_understanding.py#L1458) | 1458 | `"                if isinstance(item, str) and item.strip()"` | — |
| [SRC-686F71AA50-L001459](../../agents/task_understanding.py#L1459) | 1459 | `"            )"` | — |
| [SRC-686F71AA50-L001460](../../agents/task_understanding.py#L1460) | 1460 | `"        raw_budgets = constraints.get(\"explicit_budgets\")"` | — |
| [SRC-686F71AA50-L001461](../../agents/task_understanding.py#L1461) | 1461 | `"        if isinstance(raw_budgets, list):"` | — |
| [SRC-686F71AA50-L001462](../../agents/task_understanding.py#L1462) | 1462 | `"            scope_terms.extend("` | — |
| [SRC-686F71AA50-L001463](../../agents/task_understanding.py#L1463) | 1463 | `"                (item.strip(), \"budget\") for item in raw_budgets[:3]"` | — |
| [SRC-686F71AA50-L001464](../../agents/task_understanding.py#L1464) | 1464 | `"                if isinstance(item, str) and item.strip()"` | — |
| [SRC-686F71AA50-L001465](../../agents/task_understanding.py#L1465) | 1465 | `"            )"` | — |
| [SRC-686F71AA50-L001466](../../agents/task_understanding.py#L1466) | 1466 | `""` | — |
| [SRC-686F71AA50-L001467](../../agents/task_understanding.py#L1467) | 1467 | `"        context_resolution = ("` | — |
| [SRC-686F71AA50-L001468](../../agents/task_understanding.py#L1468) | 1468 | `"            spec.get(\"context_resolution\")"` | — |
| [SRC-686F71AA50-L001469](../../agents/task_understanding.py#L1469) | 1469 | `"            if isinstance(spec.get(\"context_resolution\"), dict) else {}"` | — |
| [SRC-686F71AA50-L001470](../../agents/task_understanding.py#L1470) | 1470 | `"        )"` | — |
| [SRC-686F71AA50-L001471](../../agents/task_understanding.py#L1471) | 1471 | `"        context_slots = ("` | — |
| [SRC-686F71AA50-L001472](../../agents/task_understanding.py#L1472) | 1472 | `"            context_resolution.get(\"slots\")"` | — |
| [SRC-686F71AA50-L001473](../../agents/task_understanding.py#L1473) | 1473 | `"            if isinstance(context_resolution.get(\"slots\"), dict) else {}"` | — |
| [SRC-686F71AA50-L001474](../../agents/task_understanding.py#L1474) | 1474 | `"        )"` | — |
| [SRC-686F71AA50-L001475](../../agents/task_understanding.py#L1475) | 1475 | `"        if ("` | — |
| [SRC-686F71AA50-L001476](../../agents/task_understanding.py#L1476) | 1476 | `"            context_resolution.get(\"is_follow_up\") is True"` | — |
| [SRC-686F71AA50-L001477](../../agents/task_understanding.py#L1477) | 1477 | `"            and context_resolution.get(\"topic_shift\") is not True"` | — |
| [SRC-686F71AA50-L001478](../../agents/task_understanding.py#L1478) | 1478 | `"            and context_resolution.get(\"needs_clarification\") is not True"` | — |
| [SRC-686F71AA50-L001479](../../agents/task_understanding.py#L1479) | 1479 | `"        ):"` | — |
| [SRC-686F71AA50-L001480](../../agents/task_understanding.py#L1480) | 1480 | `"            for slot_key in (\"product\", \"model\", \"version\", \"variant\", \"capacity\", \"aspect\"):"` | — |
| [SRC-686F71AA50-L001481](../../agents/task_understanding.py#L1481) | 1481 | `"                slot_value = context_slots.get(slot_key)"` | — |
| [SRC-686F71AA50-L001482](../../agents/task_understanding.py#L1482) | 1482 | `"                if isinstance(slot_value, str) and slot_value.strip():"` | — |
| [SRC-686F71AA50-L001483](../../agents/task_understanding.py#L1483) | 1483 | `"                    scope_terms.append((slot_value.strip(), slot_key))"` | — |
| [SRC-686F71AA50-L001484](../../agents/task_understanding.py#L1484) | 1484 | `"            changed_slots = set(context_resolution.get(\"changed_slots\") or [])"` | — |
| [SRC-686F71AA50-L001485](../../agents/task_understanding.py#L1485) | 1485 | `"            resolved_context_question = str(context_resolution.get(\"resolved_question\") or \"\")"` | — |
| [SRC-686F71AA50-L001486](../../agents/task_understanding.py#L1486) | 1486 | `"            price_context = bool(re.search("` | — |
| [SRC-686F71AA50-L001487](../../agents/task_understanding.py#L1487) | 1487 | `"                r\"(?:سعر\|اسعار\|ثمن\|تكلفه\|price\|pricing\|cost)\","` | — |
| [SRC-686F71AA50-L001488](../../agents/task_understanding.py#L1488) | 1488 | `"                normalize_text(resolved_context_question),"` | — |
| [SRC-686F71AA50-L001489](../../agents/task_understanding.py#L1489) | 1489 | `"            ))"` | — |
| [SRC-686F71AA50-L001490](../../agents/task_understanding.py#L1490) | 1490 | `"            if \"currency\" in changed_slots or price_context or spec.get(\"task_family\") in {"` | — |
| [SRC-686F71AA50-L001491](../../agents/task_understanding.py#L1491) | 1491 | `"                \"compare\", \"recommendation\", \"find_or_discover\""` | — |
| [SRC-686F71AA50-L001492](../../agents/task_understanding.py#L1492) | 1492 | `"            }:"` | — |
| [SRC-686F71AA50-L001493](../../agents/task_understanding.py#L1493) | 1493 | `"                currency = context_slots.get(\"currency\")"` | — |
| [SRC-686F71AA50-L001494](../../agents/task_understanding.py#L1494) | 1494 | `"                if isinstance(currency, str) and currency.strip():"` | — |
| [SRC-686F71AA50-L001495](../../agents/task_understanding.py#L1495) | 1495 | `"                    scope_terms.append((currency.strip(), \"currency\"))"` | — |
| [SRC-686F71AA50-L001496](../../agents/task_understanding.py#L1496) | 1496 | `"            if \"time_range\" in changed_slots or constraints.get(\"time_sensitive_request\"):"` | — |
| [SRC-686F71AA50-L001497](../../agents/task_understanding.py#L1497) | 1497 | `"                time_range = context_slots.get(\"time_range\")"` | — |
| [SRC-686F71AA50-L001498](../../agents/task_understanding.py#L1498) | 1498 | `"                if isinstance(time_range, str) and time_range.strip():"` | — |
| [SRC-686F71AA50-L001499](../../agents/task_understanding.py#L1499) | 1499 | `"                    scope_terms.append((time_range.strip(), \"time_range\"))"` | — |
| [SRC-686F71AA50-L001500](../../agents/task_understanding.py#L1500) | 1500 | `""` | — |
| [SRC-686F71AA50-L001501](../../agents/task_understanding.py#L1501) | 1501 | `"        # Bound the seed before matching aliases; otherwise a scope term beyond the"` | — |
| [SRC-686F71AA50-L001502](../../agents/task_understanding.py#L1502) | 1502 | `"        # provider query limit could be mistaken for a retained constraint."` | — |
| [SRC-686F71AA50-L001503](../../agents/task_understanding.py#L1503) | 1503 | `"        candidate = candidate[:240]"` | — |
| [SRC-686F71AA50-L001504](../../agents/task_understanding.py#L1504) | 1504 | `"        normalized_candidate = normalize_text(candidate)"` | — |
| [SRC-686F71AA50-L001505](../../agents/task_understanding.py#L1505) | 1505 | `"        location_aliases = {"` | — |
| [SRC-686F71AA50-L001506](../../agents/task_understanding.py#L1506) | 1506 | `"            normalize_text(\"مصر\"): (\"مصر\", \"egypt\", \"egyptian\"),"` | — |
| [SRC-686F71AA50-L001507](../../agents/task_understanding.py#L1507) | 1507 | `"            normalize_text(\"القاهرة\"): (\"القاهرة\", \"القاهره\", \"cairo\"),"` | — |
| [SRC-686F71AA50-L001508](../../agents/task_understanding.py#L1508) | 1508 | `"            normalize_text(\"الإسكندرية\"): (\"الإسكندرية\", \"الاسكندرية\", \"الاسكندريه\", \"alexandria\"),"` | — |
| [SRC-686F71AA50-L001509](../../agents/task_understanding.py#L1509) | 1509 | `"            normalize_text(\"الجيزة\"): (\"الجيزة\", \"الجيزه\", \"giza\"),"` | — |
| [SRC-686F71AA50-L001510](../../agents/task_understanding.py#L1510) | 1510 | `"            normalize_text(\"العاصمة الإدارية\"): (\"العاصمة الإدارية\", \"العاصمه الاداريه\", \"new administrative capital\"),"` | — |
| [SRC-686F71AA50-L001511](../../agents/task_understanding.py#L1511) | 1511 | `"            normalize_text(\"القاهرة الجديدة\"): (\"القاهرة الجديدة\", \"القاهره الجديده\", \"new cairo\"),"` | — |
| [SRC-686F71AA50-L001512](../../agents/task_understanding.py#L1512) | 1512 | `"            normalize_text(\"السعودية\"): (\"السعودية\", \"السعوديه\", \"saudi arabia\", \"ksa\"),"` | — |
| [SRC-686F71AA50-L001513](../../agents/task_understanding.py#L1513) | 1513 | `"            normalize_text(\"الإمارات\"): (\"الإمارات\", \"الامارات\", \"uae\", \"united arab emirates\"),"` | — |
| [SRC-686F71AA50-L001514](../../agents/task_understanding.py#L1514) | 1514 | `"            normalize_text(\"المملكة المتحدة\"): (\"المملكة المتحدة\", \"united kingdom\", \"the uk\"),"` | — |
| [SRC-686F71AA50-L001515](../../agents/task_understanding.py#L1515) | 1515 | `"            normalize_text(\"الولايات المتحدة\"): (\"الولايات المتحدة\", \"united states\", \"the us\"),"` | — |
| [SRC-686F71AA50-L001516](../../agents/task_understanding.py#L1516) | 1516 | `"        }"` | — |
| [SRC-686F71AA50-L001517](../../agents/task_understanding.py#L1517) | 1517 | `"        slot_aliases = {"` | — |
| [SRC-686F71AA50-L001518](../../agents/task_understanding.py#L1518) | 1518 | `"            \"currency\": {"` | — |
| [SRC-686F71AA50-L001519](../../agents/task_understanding.py#L1519) | 1519 | `"                normalize_text(\"اليورو\"): (\"اليورو\", \"يورو\", \"eur\", \"euro\", \"euros\"),"` | — |
| [SRC-686F71AA50-L001520](../../agents/task_understanding.py#L1520) | 1520 | `"                normalize_text(\"الدولار\"): (\"الدولار\", \"دولار\", \"usd\", \"us dollar\", \"dollar\", \"dollars\"),"` | — |
| [SRC-686F71AA50-L001521](../../agents/task_understanding.py#L1521) | 1521 | `"                normalize_text(\"الجنيه المصري\"): (\"الجنيه المصري\", \"جنيه مصري\", \"egp\", \"egyptian pound\", \"egyptian pounds\"),"` | — |
| [SRC-686F71AA50-L001522](../../agents/task_understanding.py#L1522) | 1522 | `"                normalize_text(\"الريال السعودي\"): (\"الريال السعودي\", \"ريال سعودي\", \"sar\", \"saudi riyal\"),"` | — |
| [SRC-686F71AA50-L001523](../../agents/task_understanding.py#L1523) | 1523 | `"                normalize_text(\"الدرهم الإماراتي\"): (\"الدرهم الإماراتي\", \"درهم إماراتي\", \"aed\", \"uae dirham\"),"` | — |
| [SRC-686F71AA50-L001524](../../agents/task_understanding.py#L1524) | 1524 | `"            },"` | — |
| [SRC-686F71AA50-L001525](../../agents/task_understanding.py#L1525) | 1525 | `"            \"aspect\": {"` | — |
| [SRC-686F71AA50-L001526](../../agents/task_understanding.py#L1526) | 1526 | `"                normalize_text(\"الضمان\"): (\"الضمان\", \"ضمان\", \"warranty\", \"guarantee\"),"` | — |
| [SRC-686F71AA50-L001527](../../agents/task_understanding.py#L1527) | 1527 | `"                normalize_text(\"التقييمات\"): (\"التقييمات\", \"التقييم\", \"reviews\", \"ratings\", \"review\"),"` | — |
| [SRC-686F71AA50-L001528](../../agents/task_understanding.py#L1528) | 1528 | `"                normalize_text(\"المراجعات\"): (\"المراجعات\", \"مراجعات\", \"reviews\", \"ratings\"),"` | — |
| [SRC-686F71AA50-L001529](../../agents/task_understanding.py#L1529) | 1529 | `"                normalize_text(\"الصيانة\"): (\"الصيانة\", \"الصيانه\", \"maintenance\", \"repair\", \"service\"),"` | — |
| [SRC-686F71AA50-L001530](../../agents/task_understanding.py#L1530) | 1530 | `"                normalize_text(\"السعر\"): (\"السعر\", \"سعر\", \"price\", \"pricing\", \"cost\"),"` | — |
| [SRC-686F71AA50-L001531](../../agents/task_understanding.py#L1531) | 1531 | `"            },"` | — |
| [SRC-686F71AA50-L001532](../../agents/task_understanding.py#L1532) | 1532 | `"            \"capacity\": {"` | — |
| [SRC-686F71AA50-L001533](../../agents/task_understanding.py#L1533) | 1533 | `"                normalize_text(\"256 جيجابايت\"): (\"256 جيجابايت\", \"256gb\", \"256 gb\"),"` | — |
| [SRC-686F71AA50-L001534](../../agents/task_understanding.py#L1534) | 1534 | `"                normalize_text(\"512 جيجابايت\"): (\"512 جيجابايت\", \"512gb\", \"512 gb\"),"` | — |
| [SRC-686F71AA50-L001535](../../agents/task_understanding.py#L1535) | 1535 | `"                normalize_text(\"1 تيرابايت\"): (\"1 تيرابايت\", \"1tb\", \"1 tb\", \"1024gb\"),"` | — |
| [SRC-686F71AA50-L001536](../../agents/task_understanding.py#L1536) | 1536 | `"            },"` | — |
| [SRC-686F71AA50-L001537](../../agents/task_understanding.py#L1537) | 1537 | `"        }"` | — |
| [SRC-686F71AA50-L001538](../../agents/task_understanding.py#L1538) | 1538 | `"        normalized_planner_seed = normalize_text(planner_seed)"` | — |
| [SRC-686F71AA50-L001539](../../agents/task_understanding.py#L1539) | 1539 | `""` | — |
| [SRC-686F71AA50-L001540](../../agents/task_understanding.py#L1540) | 1540 | `"        def _scope_aliases(term: str, slot_key: str) -> tuple[str, ...]:"` | — |
| [SRC-686F71AA50-L001541](../../agents/task_understanding.py#L1541) | 1541 | `"            normalized_scope = normalize_text(term)"` | — |
| [SRC-686F71AA50-L001542](../../agents/task_understanding.py#L1542) | 1542 | `"            if slot_key == \"location\":"` | — |
| [SRC-686F71AA50-L001543](../../agents/task_understanding.py#L1543) | 1543 | `"                return location_aliases.get(normalized_scope, (term,))"` | — |
| [SRC-686F71AA50-L001544](../../agents/task_understanding.py#L1544) | 1544 | `"            return slot_aliases.get(slot_key, {}).get(normalized_scope, (term,))"` | — |
| [SRC-686F71AA50-L001545](../../agents/task_understanding.py#L1545) | 1545 | `""` | — |
| [SRC-686F71AA50-L001546](../../agents/task_understanding.py#L1546) | 1546 | `"        def _preferred_planner_alias(term: str, slot_key: str) -> str:"` | — |
| [SRC-686F71AA50-L001547](../../agents/task_understanding.py#L1547) | 1547 | `"            # Reuse the language/token already present in the planner seed so that"` | — |
| [SRC-686F71AA50-L001548](../../agents/task_understanding.py#L1548) | 1548 | `"            # all strategy variants keep one consistent country/currency/capacity"` | — |
| [SRC-686F71AA50-L001549](../../agents/task_understanding.py#L1549) | 1549 | `"            # representation instead of appending a duplicate in another language."` | — |
| [SRC-686F71AA50-L001550](../../agents/task_understanding.py#L1550) | 1550 | `"            for alias in _scope_aliases(term, slot_key):"` | — |
| [SRC-686F71AA50-L001551](../../agents/task_understanding.py#L1551) | 1551 | `"                normalized_alias = normalize_text(alias)"` | — |
| [SRC-686F71AA50-L001552](../../agents/task_understanding.py#L1552) | 1552 | `"                if normalized_alias and re.search("` | — |
| [SRC-686F71AA50-L001553](../../agents/task_understanding.py#L1553) | 1553 | `"                    rf\"(?<!\\w){re.escape(normalized_alias)}(?!\\w)\","` | — |
| [SRC-686F71AA50-L001554](../../agents/task_understanding.py#L1554) | 1554 | `"                    normalized_planner_seed,"` | — |
| [SRC-686F71AA50-L001555](../../agents/task_understanding.py#L1555) | 1555 | `"                ):"` | — |
| [SRC-686F71AA50-L001556](../../agents/task_understanding.py#L1556) | 1556 | `"                    return alias"` | — |
| [SRC-686F71AA50-L001557](../../agents/task_understanding.py#L1557) | 1557 | `"            return term"` | — |
| [SRC-686F71AA50-L001558](../../agents/task_understanding.py#L1558) | 1558 | `""` | — |
| [SRC-686F71AA50-L001559](../../agents/task_understanding.py#L1559) | 1559 | `"        def scope_already_present(term: str, slot_key: str) -> bool:"` | — |
| [SRC-686F71AA50-L001560](../../agents/task_understanding.py#L1560) | 1560 | `"            normalized_scope = normalize_text(term)"` | — |
| [SRC-686F71AA50-L001561](../../agents/task_understanding.py#L1561) | 1561 | `"            if not normalized_scope:"` | — |
| [SRC-686F71AA50-L001562](../../agents/task_understanding.py#L1562) | 1562 | `"                return True"` | — |
| [SRC-686F71AA50-L001563](../../agents/task_understanding.py#L1563) | 1563 | `"            aliases = ("` | — |
| [SRC-686F71AA50-L001564](../../agents/task_understanding.py#L1564) | 1564 | `"                location_aliases.get(normalized_scope, (term,))"` | — |
| [SRC-686F71AA50-L001565](../../agents/task_understanding.py#L1565) | 1565 | `"                if slot_key == \"location\""` | — |
| [SRC-686F71AA50-L001566](../../agents/task_understanding.py#L1566) | 1566 | `"                else slot_aliases.get(slot_key, {}).get(normalized_scope, (term,))"` | — |
| [SRC-686F71AA50-L001567](../../agents/task_understanding.py#L1567) | 1567 | `"            )"` | — |
| [SRC-686F71AA50-L001568](../../agents/task_understanding.py#L1568) | 1568 | `"            if any("` | — |
| [SRC-686F71AA50-L001569](../../agents/task_understanding.py#L1569) | 1569 | `"                re.search("` | — |
| [SRC-686F71AA50-L001570](../../agents/task_understanding.py#L1570) | 1570 | `"                    rf\"(?<!\\w){re.escape(normalize_text(alias))}(?!\\w)\","` | — |
| [SRC-686F71AA50-L001571](../../agents/task_understanding.py#L1571) | 1571 | `"                    normalized_candidate,"` | — |
| [SRC-686F71AA50-L001572](../../agents/task_understanding.py#L1572) | 1572 | `"                )"` | — |
| [SRC-686F71AA50-L001573](../../agents/task_understanding.py#L1573) | 1573 | `"                for alias in aliases"` | — |
| [SRC-686F71AA50-L001574](../../agents/task_understanding.py#L1574) | 1574 | `"                if normalize_text(alias)"` | — |
| [SRC-686F71AA50-L001575](../../agents/task_understanding.py#L1575) | 1575 | `"            ):"` | — |
| [SRC-686F71AA50-L001576](../../agents/task_understanding.py#L1576) | 1576 | `"                return True"` | — |
| [SRC-686F71AA50-L001577](../../agents/task_understanding.py#L1577) | 1577 | `"            if slot_key == \"capacity\":"` | — |
| [SRC-686F71AA50-L001578](../../agents/task_understanding.py#L1578) | 1578 | `"                scope_numbers = {"` | — |
| [SRC-686F71AA50-L001579](../../agents/task_understanding.py#L1579) | 1579 | `"                    item.replace(\",\", \"\").replace(\".\", \"\")"` | — |
| [SRC-686F71AA50-L001580](../../agents/task_understanding.py#L1580) | 1580 | `"                    for item in re.findall(r\"\\d+(?:[,.]\\d+)*\", normalize_text(term))"` | — |
| [SRC-686F71AA50-L001581](../../agents/task_understanding.py#L1581) | 1581 | `"                }"` | — |
| [SRC-686F71AA50-L001582](../../agents/task_understanding.py#L1582) | 1582 | `"                query_numbers = {"` | — |
| [SRC-686F71AA50-L001583](../../agents/task_understanding.py#L1583) | 1583 | `"                    item.replace(\",\", \"\").replace(\".\", \"\")"` | — |
| [SRC-686F71AA50-L001584](../../agents/task_understanding.py#L1584) | 1584 | `"                    for item in re.findall(r\"\\d+(?:[,.]\\d+)*\", normalized_candidate)"` | — |
| [SRC-686F71AA50-L001585](../../agents/task_understanding.py#L1585) | 1585 | `"                }"` | — |
| [SRC-686F71AA50-L001586](../../agents/task_understanding.py#L1586) | 1586 | `"                if scope_numbers & query_numbers:"` | — |
| [SRC-686F71AA50-L001587](../../agents/task_understanding.py#L1587) | 1587 | `"                    capacity_units = ("` | — |
| [SRC-686F71AA50-L001588](../../agents/task_understanding.py#L1588) | 1588 | `"                        \"gb\", \"gigabyte\", \"gigabytes\", \"جيجا\", \"جيجابايت\","` | — |
| [SRC-686F71AA50-L001589](../../agents/task_understanding.py#L1589) | 1589 | `"                        \"tb\", \"terabyte\", \"terabytes\", \"تيرا\", \"تيرابايت\","` | — |
| [SRC-686F71AA50-L001590](../../agents/task_understanding.py#L1590) | 1590 | `"                    )"` | — |
| [SRC-686F71AA50-L001591](../../agents/task_understanding.py#L1591) | 1591 | `"                    if any(normalize_text(unit) in normalized_candidate for unit in capacity_units):"` | — |
| [SRC-686F71AA50-L001592](../../agents/task_understanding.py#L1592) | 1592 | `"                        return True"` | — |
| [SRC-686F71AA50-L001593](../../agents/task_understanding.py#L1593) | 1593 | `"            return False"` | — |
| [SRC-686F71AA50-L001594](../../agents/task_understanding.py#L1594) | 1594 | `""` | — |
| [SRC-686F71AA50-L001595](../../agents/task_understanding.py#L1595) | 1595 | `"        missing_scope_terms: list[str] = []"` | — |
| [SRC-686F71AA50-L001596](../../agents/task_understanding.py#L1596) | 1596 | `"        seen_scope_terms: set[str] = set()"` | — |
| [SRC-686F71AA50-L001597](../../agents/task_understanding.py#L1597) | 1597 | `"        for raw_scope_term, slot_key in scope_terms:"` | — |
| [SRC-686F71AA50-L001598](../../agents/task_understanding.py#L1598) | 1598 | `"            scope_term = _preferred_planner_alias(raw_scope_term, slot_key)"` | — |
| [SRC-686F71AA50-L001599](../../agents/task_understanding.py#L1599) | 1599 | `"            normalized_scope = normalize_text(raw_scope_term)"` | — |
| [SRC-686F71AA50-L001600](../../agents/task_understanding.py#L1600) | 1600 | `"            if not normalized_scope or normalized_scope in seen_scope_terms:"` | — |
| [SRC-686F71AA50-L001601](../../agents/task_understanding.py#L1601) | 1601 | `"                continue"` | — |
| [SRC-686F71AA50-L001602](../../agents/task_understanding.py#L1602) | 1602 | `"            seen_scope_terms.add(normalized_scope)"` | — |
| [SRC-686F71AA50-L001603](../../agents/task_understanding.py#L1603) | 1603 | `"            if not scope_already_present(scope_term, slot_key):"` | — |
| [SRC-686F71AA50-L001604](../../agents/task_understanding.py#L1604) | 1604 | `"                missing_scope_terms.append(scope_term)"` | — |
| [SRC-686F71AA50-L001605](../../agents/task_understanding.py#L1605) | 1605 | `""` | — |
| [SRC-686F71AA50-L001606](../../agents/task_understanding.py#L1606) | 1606 | `"        if missing_scope_terms:"` | — |
| [SRC-686F71AA50-L001607](../../agents/task_understanding.py#L1607) | 1607 | `"            # Reserve room for the constraint suffix. Keep the query's topic and"` | — |
| [SRC-686F71AA50-L001608](../../agents/task_understanding.py#L1608) | 1608 | `"            # strategy angle instead of blindly cutting its final words."` | — |
| [SRC-686F71AA50-L001609](../../agents/task_understanding.py#L1609) | 1609 | `"            selected_scope_terms: list[str] = []"` | — |
| [SRC-686F71AA50-L001610](../../agents/task_understanding.py#L1610) | 1610 | `"            for term in missing_scope_terms:"` | — |
| [SRC-686F71AA50-L001611](../../agents/task_understanding.py#L1611) | 1611 | `"                candidate_terms = [*selected_scope_terms, term]"` | — |
| [SRC-686F71AA50-L001612](../../agents/task_understanding.py#L1612) | 1612 | `"                if len(\" \".join(candidate_terms)) <= 150:"` | — |
| [SRC-686F71AA50-L001613](../../agents/task_understanding.py#L1613) | 1613 | `"                    selected_scope_terms.append(term)"` | — |
| [SRC-686F71AA50-L001614](../../agents/task_understanding.py#L1614) | 1614 | `"            scope_suffix = \" \".join(selected_scope_terms)"` | — |
| [SRC-686F71AA50-L001615](../../agents/task_understanding.py#L1615) | 1615 | `"            max_topic_chars = max(60, 239 - len(scope_suffix))"` | — |
| [SRC-686F71AA50-L001616](../../agents/task_understanding.py#L1616) | 1616 | `"            if len(candidate) > max_topic_chars:"` | — |
| [SRC-686F71AA50-L001617](../../agents/task_understanding.py#L1617) | 1617 | `"                tail_chars = min(72, max(24, max_topic_chars // 3))"` | — |
| [SRC-686F71AA50-L001618](../../agents/task_understanding.py#L1618) | 1618 | `"                head_chars = max(40, max_topic_chars - tail_chars - 1)"` | — |
| [SRC-686F71AA50-L001619](../../agents/task_understanding.py#L1619) | 1619 | `"                head = candidate[:head_chars].rsplit(\" \", 1)[0].strip()"` | — |
| [SRC-686F71AA50-L001620](../../agents/task_understanding.py#L1620) | 1620 | `"                tail = candidate[-tail_chars:].strip()"` | — |
| [SRC-686F71AA50-L001621](../../agents/task_understanding.py#L1621) | 1621 | `"                candidate = _SPACE.sub(\" \", f\"{head} {tail}\").strip()"` | — |
| [SRC-686F71AA50-L001622](../../agents/task_understanding.py#L1622) | 1622 | `"            candidate = _SPACE.sub(\" \", f\"{candidate} {scope_suffix}\").strip()"` | — |
| [SRC-686F71AA50-L001623](../../agents/task_understanding.py#L1623) | 1623 | `"        candidate = candidate[:240]"` | — |
| [SRC-686F71AA50-L001624](../../agents/task_understanding.py#L1624) | 1624 | `"        key = _query_key(candidate)"` | — |
| [SRC-686F71AA50-L001625](../../agents/task_understanding.py#L1625) | 1625 | `"        if not candidate or not key or key in seen:"` | — |
| [SRC-686F71AA50-L001626](../../agents/task_understanding.py#L1626) | 1626 | `"            return"` | — |
| [SRC-686F71AA50-L001627](../../agents/task_understanding.py#L1627) | 1627 | `"        # Search modifications must preserve a subject anchor. Existing planner"` | — |
| [SRC-686F71AA50-L001628](../../agents/task_understanding.py#L1628) | 1628 | `"        # queries are retained because they may already contain resolved context."` | — |
| [SRC-686F71AA50-L001629](../../agents/task_understanding.py#L1629) | 1629 | `"        topic_tokens = _TOKEN_RE.findall(_query_key(topic_anchor_query))"` | — |
| [SRC-686F71AA50-L001630](../../agents/task_understanding.py#L1630) | 1630 | `"        query_tokens = _TOKEN_RE.findall(key)"` | — |
| [SRC-686F71AA50-L001631](../../agents/task_understanding.py#L1631) | 1631 | `"        if enforce_topic and len(topic_tokens) >= 2 and not any("` | — |
| [SRC-686F71AA50-L001632](../../agents/task_understanding.py#L1632) | 1632 | `"            token in query_tokens for token in topic_tokens[:3]"` | — |
| [SRC-686F71AA50-L001633](../../agents/task_understanding.py#L1633) | 1633 | `"        ):"` | — |
| [SRC-686F71AA50-L001634](../../agents/task_understanding.py#L1634) | 1634 | `"            return"` | — |
| [SRC-686F71AA50-L001635](../../agents/task_understanding.py#L1635) | 1635 | `"        seen.add(key)"` | — |
| [SRC-686F71AA50-L001636](../../agents/task_understanding.py#L1636) | 1636 | `"        rows.append({\"query\": candidate, \"strategy\": strategy, \"rationale\": rationale})"` | — |
| [SRC-686F71AA50-L001637](../../agents/task_understanding.py#L1637) | 1637 | `""` | — |
| [SRC-686F71AA50-L001638](../../agents/task_understanding.py#L1638) | 1638 | `"    constraints = spec.get(\"constraints\") if isinstance(spec.get(\"constraints\"), dict) else {}"` | — |
| [SRC-686F71AA50-L001639](../../agents/task_understanding.py#L1639) | 1639 | `"    explicit_aspects = ("` | — |
| [SRC-686F71AA50-L001640](../../agents/task_understanding.py#L1640) | 1640 | `"        constraints.get(\"explicit_aspects\")"` | — |
| [SRC-686F71AA50-L001641](../../agents/task_understanding.py#L1641) | 1641 | `"        if isinstance(constraints.get(\"explicit_aspects\"), list)"` | — |
| [SRC-686F71AA50-L001642](../../agents/task_understanding.py#L1642) | 1642 | `"        else []"` | — |
| [SRC-686F71AA50-L001643](../../agents/task_understanding.py#L1643) | 1643 | `"    )"` | — |
| [SRC-686F71AA50-L001644](../../agents/task_understanding.py#L1644) | 1644 | `"    # Use the dedicated aspect extractor as a second deterministic pass. This"` | — |
| [SRC-686F71AA50-L001645](../../agents/task_understanding.py#L1645) | 1645 | `"    # guards against a classifier losing the final criterion in a long list."` | — |
| [SRC-686F71AA50-L001646](../../agents/task_understanding.py#L1646) | 1646 | `"    try:"` | — |
| [SRC-686F71AA50-L001647](../../agents/task_understanding.py#L1647) | 1647 | `"        from agents.aspect_planning import extract_aspects"` | — |
| [SRC-686F71AA50-L001648](../../agents/task_understanding.py#L1648) | 1648 | `"        independently_extracted = extract_aspects(question)"` | — |
| [SRC-686F71AA50-L001649](../../agents/task_understanding.py#L1649) | 1649 | `"    except (ImportError, TypeError, ValueError):"` | — |
| [SRC-686F71AA50-L001650](../../agents/task_understanding.py#L1650) | 1650 | `"        independently_extracted = []"` | — |
| [SRC-686F71AA50-L001651](../../agents/task_understanding.py#L1651) | 1651 | `"    merged_aspects: list[str] = []"` | — |
| [SRC-686F71AA50-L001652](../../agents/task_understanding.py#L1652) | 1652 | `"    aspect_keys: set[str] = set()"` | — |
| [SRC-686F71AA50-L001653](../../agents/task_understanding.py#L1653) | 1653 | `"    for aspect in [*explicit_aspects, *independently_extracted]:"` | — |
| [SRC-686F71AA50-L001654](../../agents/task_understanding.py#L1654) | 1654 | `"        if not isinstance(aspect, str) or not aspect.strip():"` | — |
| [SRC-686F71AA50-L001655](../../agents/task_understanding.py#L1655) | 1655 | `"            continue"` | — |
| [SRC-686F71AA50-L001656](../../agents/task_understanding.py#L1656) | 1656 | `"        key = _query_key(aspect)"` | — |
| [SRC-686F71AA50-L001657](../../agents/task_understanding.py#L1657) | 1657 | `"        if key and key not in aspect_keys:"` | — |
| [SRC-686F71AA50-L001658](../../agents/task_understanding.py#L1658) | 1658 | `"            aspect_keys.add(key)"` | — |
| [SRC-686F71AA50-L001659](../../agents/task_understanding.py#L1659) | 1659 | `"            merged_aspects.append(aspect.strip())"` | — |
| [SRC-686F71AA50-L001660](../../agents/task_understanding.py#L1660) | 1660 | `"        if len(merged_aspects) >= MAX_TASK_ASPECTS:"` | — |
| [SRC-686F71AA50-L001661](../../agents/task_understanding.py#L1661) | 1661 | `"            break"` | — |
| [SRC-686F71AA50-L001662](../../agents/task_understanding.py#L1662) | 1662 | `"    explicit_aspects = merged_aspects"` | — |
| [SRC-686F71AA50-L001663](../../agents/task_understanding.py#L1663) | 1663 | `"    spec_for_candidates = dict(spec)"` | — |
| [SRC-686F71AA50-L001664](../../agents/task_understanding.py#L1664) | 1664 | `"    candidate_constraints = dict(constraints)"` | — |
| [SRC-686F71AA50-L001665](../../agents/task_understanding.py#L1665) | 1665 | `"    candidate_constraints[\"explicit_aspects\"] = explicit_aspects"` | — |
| [SRC-686F71AA50-L001666](../../agents/task_understanding.py#L1666) | 1666 | `"    spec_for_candidates[\"constraints\"] = candidate_constraints"` | — |
| [SRC-686F71AA50-L001667](../../agents/task_understanding.py#L1667) | 1667 | `"    # If every query slot is needed to represent explicit comparison criteria,"` | — |
| [SRC-686F71AA50-L001668](../../agents/task_understanding.py#L1668) | 1668 | `"    # spend the budget on those criteria rather than a generic planner seed."` | — |
| [SRC-686F71AA50-L001669](../../agents/task_understanding.py#L1669) | 1669 | `"    reserve_all_slots_for_criteria = ("` | — |
| [SRC-686F71AA50-L001670](../../agents/task_understanding.py#L1670) | 1670 | `"        spec.get(\"task_family\") == \"compare\""` | — |
| [SRC-686F71AA50-L001671](../../agents/task_understanding.py#L1671) | 1671 | `"        and len(explicit_aspects) >= maximum"` | — |
| [SRC-686F71AA50-L001672](../../agents/task_understanding.py#L1672) | 1672 | `"    )"` | — |
| [SRC-686F71AA50-L001673](../../agents/task_understanding.py#L1673) | 1673 | `"    has_planner_seed = bool("` | — |
| [SRC-686F71AA50-L001674](../../agents/task_understanding.py#L1674) | 1674 | `"        queries and isinstance(queries[0], str) and queries[0].strip()"` | — |
| [SRC-686F71AA50-L001675](../../agents/task_understanding.py#L1675) | 1675 | `"    )"` | — |
| [SRC-686F71AA50-L001676](../../agents/task_understanding.py#L1676) | 1676 | `"    has_resolved_replacement_seed = ("` | — |
| [SRC-686F71AA50-L001677](../../agents/task_understanding.py#L1677) | 1677 | `"        replace_stale_planner_queries and bool(resolved_context_seed)"` | — |
| [SRC-686F71AA50-L001678](../../agents/task_understanding.py#L1678) | 1678 | `"    )"` | — |
| [SRC-686F71AA50-L001679](../../agents/task_understanding.py#L1679) | 1679 | `"    if ("` | — |
| [SRC-686F71AA50-L001680](../../agents/task_understanding.py#L1680) | 1680 | `"        (has_planner_seed or has_resolved_replacement_seed)"` | — |
| [SRC-686F71AA50-L001681](../../agents/task_understanding.py#L1681) | 1681 | `"        and spec.get(\"task_family\") != \"lead_generation\""` | — |
| [SRC-686F71AA50-L001682](../../agents/task_understanding.py#L1682) | 1682 | `"        and not reserve_all_slots_for_criteria"` | — |
| [SRC-686F71AA50-L001683](../../agents/task_understanding.py#L1683) | 1683 | `"    ):"` | — |
| [SRC-686F71AA50-L001684](../../agents/task_understanding.py#L1684) | 1684 | `"        seed = primary_seed"` | — |
| [SRC-686F71AA50-L001685](../../agents/task_understanding.py#L1685) | 1685 | `"        strategy, rationale = ("` | — |
| [SRC-686F71AA50-L001686](../../agents/task_understanding.py#L1686) | 1686 | `"            ("` | — |
| [SRC-686F71AA50-L001687](../../agents/task_understanding.py#L1687) | 1687 | `"                \"context_entity_replacement\","` | — |
| [SRC-686F71AA50-L001688](../../agents/task_understanding.py#L1688) | 1688 | `"                \"replace a stale planner seed with the newly resolved product/entity\","` | — |
| [SRC-686F71AA50-L001689](../../agents/task_understanding.py#L1689) | 1689 | `"            )"` | — |
| [SRC-686F71AA50-L001690](../../agents/task_understanding.py#L1690) | 1690 | `"            if entity_replacement"` | — |
| [SRC-686F71AA50-L001691](../../agents/task_understanding.py#L1691) | 1691 | `"            else ("` | — |
| [SRC-686F71AA50-L001692](../../agents/task_understanding.py#L1692) | 1692 | `"                \"context_slot_replacement\","` | — |
| [SRC-686F71AA50-L001693](../../agents/task_understanding.py#L1693) | 1693 | `"                \"replace stale planner constraints with the resolved location, budget, currency, or aspect\","` | — |
| [SRC-686F71AA50-L001694](../../agents/task_understanding.py#L1694) | 1694 | `"            )"` | — |
| [SRC-686F71AA50-L001695](../../agents/task_understanding.py#L1695) | 1695 | `"            if scope_replacement"` | — |
| [SRC-686F71AA50-L001696](../../agents/task_understanding.py#L1696) | 1696 | `"            else ("` | — |
| [SRC-686F71AA50-L001697](../../agents/task_understanding.py#L1697) | 1697 | `"                _label_existing_query(seed, 0, spec)"` | — |
| [SRC-686F71AA50-L001698](../../agents/task_understanding.py#L1698) | 1698 | `"                if isinstance(seed, str)"` | — |
| [SRC-686F71AA50-L001699](../../agents/task_understanding.py#L1699) | 1699 | `"                else (\"malformed\", \"planner seed is not a string\")"` | — |
| [SRC-686F71AA50-L001700](../../agents/task_understanding.py#L1700) | 1700 | `"            )"` | — |
| [SRC-686F71AA50-L001701](../../agents/task_understanding.py#L1701) | 1701 | `"        )"` | — |
| [SRC-686F71AA50-L001702](../../agents/task_understanding.py#L1702) | 1702 | `"        add(seed, strategy, rationale, enforce_topic=False)"` | — |
| [SRC-686F71AA50-L001703](../../agents/task_understanding.py#L1703) | 1703 | `""` | — |
| [SRC-686F71AA50-L001704](../../agents/task_understanding.py#L1704) | 1704 | `"    # A contextual follow-up can introduce a material slot change without"` | — |
| [SRC-686F71AA50-L001705](../../agents/task_understanding.py#L1705) | 1705 | `"    # creating a new lexical task family (for example \"سعره؟\" after a product"` | — |
| [SRC-686F71AA50-L001706](../../agents/task_understanding.py#L1706) | 1706 | `"    # comparison). Preserve the planner seed, then add one complementary source"` | — |
| [SRC-686F71AA50-L001707](../../agents/task_understanding.py#L1707) | 1707 | `"    # angle so the changed slots are not trapped in a single broad query."` | — |
| [SRC-686F71AA50-L001708](../../agents/task_understanding.py#L1708) | 1708 | `"    raw_changed_slots = context_resolution.get(\"changed_slots\")"` | — |
| [SRC-686F71AA50-L001709](../../agents/task_understanding.py#L1709) | 1709 | `"    context_slots = ("` | — |
| [SRC-686F71AA50-L001710](../../agents/task_understanding.py#L1710) | 1710 | `"        context_resolution.get(\"slots\")"` | — |
| [SRC-686F71AA50-L001711](../../agents/task_understanding.py#L1711) | 1711 | `"        if isinstance(context_resolution.get(\"slots\"), dict) else {}"` | — |
| [SRC-686F71AA50-L001712](../../agents/task_understanding.py#L1712) | 1712 | `"    )"` | — |
| [SRC-686F71AA50-L001713](../../agents/task_understanding.py#L1713) | 1713 | `"    if ("` | — |
| [SRC-686F71AA50-L001714](../../agents/task_understanding.py#L1714) | 1714 | `"        rows"` | — |
| [SRC-686F71AA50-L001715](../../agents/task_understanding.py#L1715) | 1715 | `"        and inherit_context"` | — |
| [SRC-686F71AA50-L001716](../../agents/task_understanding.py#L1716) | 1716 | `"        and isinstance(raw_changed_slots, list)"` | — |
| [SRC-686F71AA50-L001717](../../agents/task_understanding.py#L1717) | 1717 | `"        and any("` | — |
| [SRC-686F71AA50-L001718](../../agents/task_understanding.py#L1718) | 1718 | `"            slot in {\"currency\", \"capacity\", \"aspect\", \"location\", \"budget\", \"time_range\"}"` | — |
| [SRC-686F71AA50-L001719](../../agents/task_understanding.py#L1719) | 1719 | `"            and isinstance(context_slots.get(slot), str)"` | — |
| [SRC-686F71AA50-L001720](../../agents/task_understanding.py#L1720) | 1720 | `"            and context_slots.get(slot, \"\").strip()"` | — |
| [SRC-686F71AA50-L001721](../../agents/task_understanding.py#L1721) | 1721 | `"            for slot in raw_changed_slots"` | — |
| [SRC-686F71AA50-L001722](../../agents/task_understanding.py#L1722) | 1722 | `"        )"` | — |
| [SRC-686F71AA50-L001723](../../agents/task_understanding.py#L1723) | 1723 | `"    ):"` | — |
| [SRC-686F71AA50-L001724](../../agents/task_understanding.py#L1724) | 1724 | `"        context_seed = primary_seed or topic_anchor_query"` | — |
| [SRC-686F71AA50-L001725](../../agents/task_understanding.py#L1725) | 1725 | `"        source_angle = ("` | — |
| [SRC-686F71AA50-L001726](../../agents/task_understanding.py#L1726) | 1726 | `"            \"مصدر رسمي\""` | — |
| [SRC-686F71AA50-L001727](../../agents/task_understanding.py#L1727) | 1727 | `"            if re.search(r\"[\\u0600-\\u06FF]\", context_seed)"` | — |
| [SRC-686F71AA50-L001728](../../agents/task_understanding.py#L1728) | 1728 | `"            else \"official source\""` | — |
| [SRC-686F71AA50-L001729](../../agents/task_understanding.py#L1729) | 1729 | `"        )"` | — |
| [SRC-686F71AA50-L001730](../../agents/task_understanding.py#L1730) | 1730 | `"        add("` | — |
| [SRC-686F71AA50-L001731](../../agents/task_understanding.py#L1731) | 1731 | `"            f\"{context_seed} {source_angle}\","` | — |
| [SRC-686F71AA50-L001732](../../agents/task_understanding.py#L1732) | 1732 | `"            \"context_slot_refinement\","` | — |
| [SRC-686F71AA50-L001733](../../agents/task_understanding.py#L1733) | 1733 | `"            \"complement the planner seed with a source-focused query while retaining confirmed dialogue slots\","` | — |
| [SRC-686F71AA50-L001734](../../agents/task_understanding.py#L1734) | 1734 | `"            enforce_topic=False,"` | — |
| [SRC-686F71AA50-L001735](../../agents/task_understanding.py#L1735) | 1735 | `"        )"` | — |
| [SRC-686F71AA50-L001736](../../agents/task_understanding.py#L1736) | 1736 | `""` | — |
| [SRC-686F71AA50-L001737](../../agents/task_understanding.py#L1737) | 1737 | `"    if not rows and ("` | — |
| [SRC-686F71AA50-L001738](../../agents/task_understanding.py#L1738) | 1738 | `"        spec.get(\"ambiguity_status\") == \"needs_clarification\""` | — |
| [SRC-686F71AA50-L001739](../../agents/task_understanding.py#L1739) | 1739 | `"        or spec.get(\"task_family\") == \"ambiguous_or_incomplete\""` | — |
| [SRC-686F71AA50-L001740](../../agents/task_understanding.py#L1740) | 1740 | `"    ):"` | — |
| [SRC-686F71AA50-L001741](../../agents/task_understanding.py#L1741) | 1741 | `"        return rows"` | — |
| [SRC-686F71AA50-L001742](../../agents/task_understanding.py#L1742) | 1742 | `""` | — |
| [SRC-686F71AA50-L001743](../../agents/task_understanding.py#L1743) | 1743 | `"    base = _collapse_repeated_query_phrases(primary_seed) if primary_seed else \"\""` | — |
| [SRC-686F71AA50-L001744](../../agents/task_understanding.py#L1744) | 1744 | `"    if not base:"` | — |
| [SRC-686F71AA50-L001745](../../agents/task_understanding.py#L1745) | 1745 | `"        base = re.sub("` | — |
| [SRC-686F71AA50-L001746](../../agents/task_understanding.py#L1746) | 1746 | `"            r\"^(?:من فضلك\|لو سمحت\|ابحث لي\|ابحث\|دورلي\|دور\|اعثر على\|please\|search for\|find\|look up)\\s*\","` | — |
| [SRC-686F71AA50-L001747](../../agents/task_understanding.py#L1747) | 1747 | `"            \"\", str(question or \"\").strip(), flags=re.IGNORECASE,"` | — |
| [SRC-686F71AA50-L001748](../../agents/task_understanding.py#L1748) | 1748 | `"        )"` | — |
| [SRC-686F71AA50-L001749](../../agents/task_understanding.py#L1749) | 1749 | `"    if ("` | — |
| [SRC-686F71AA50-L001750](../../agents/task_understanding.py#L1750) | 1750 | `"        context_anchor"` | — |
| [SRC-686F71AA50-L001751](../../agents/task_understanding.py#L1751) | 1751 | `"        and re.search(r\"[\\u0600-\\u06FF]\", primary_seed)"` | — |
| [SRC-686F71AA50-L001752](../../agents/task_understanding.py#L1752) | 1752 | `"    ):"` | — |
| [SRC-686F71AA50-L001753](../../agents/task_understanding.py#L1753) | 1753 | `"        # For Arabic planner seeds, prefer the resolved topic/entities to remove"` | — |
| [SRC-686F71AA50-L001754](../../agents/task_understanding.py#L1754) | 1754 | `"        # imperative prefixes. For English seeds, keep the seed language so"` | — |
| [SRC-686F71AA50-L001755](../../agents/task_understanding.py#L1755) | 1755 | `"        # location/currency aliases are not re-appended in Arabic."` | — |
| [SRC-686F71AA50-L001756](../../agents/task_understanding.py#L1756) | 1756 | `"        base = context_anchor[:180]"` | — |
| [SRC-686F71AA50-L001757](../../agents/task_understanding.py#L1757) | 1757 | `"    elif not base and context_anchor:"` | — |
| [SRC-686F71AA50-L001758](../../agents/task_understanding.py#L1758) | 1758 | `"        base = context_anchor[:180]"` | — |
| [SRC-686F71AA50-L001759](../../agents/task_understanding.py#L1759) | 1759 | `"    base = _QUERY_STOP.sub(\"\", base).strip(\" \\t\\r\\n-،,؛;\")"` | — |
| [SRC-686F71AA50-L001760](../../agents/task_understanding.py#L1760) | 1760 | `"    if not base:"` | — |
| [SRC-686F71AA50-L001761](../../agents/task_understanding.py#L1761) | 1761 | `"        return rows"` | — |
| [SRC-686F71AA50-L001762](../../agents/task_understanding.py#L1762) | 1762 | `""` | — |
| [SRC-686F71AA50-L001763](../../agents/task_understanding.py#L1763) | 1763 | `"    # A lead-generation task must preserve the supplied product-anchored queries"` | — |
| [SRC-686F71AA50-L001764](../../agents/task_understanding.py#L1764) | 1764 | `"    # in purchaser language. General research angles (reports, risks, listings)"` | — |
| [SRC-686F71AA50-L001765](../../agents/task_understanding.py#L1765) | 1765 | `"    # are not substitutes for direct buyer-intent discovery."` | — |
| [SRC-686F71AA50-L001766](../../agents/task_understanding.py#L1766) | 1766 | `"    if spec.get(\"task_family\") == \"lead_generation\":"` | — |
| [SRC-686F71AA50-L001767](../../agents/task_understanding.py#L1767) | 1767 | `"        if replace_stale_planner_queries:"` | — |
| [SRC-686F71AA50-L001768](../../agents/task_understanding.py#L1768) | 1768 | `"            # Preserve purchaser language, but rebuild from the corrected product"` | — |
| [SRC-686F71AA50-L001769](../../agents/task_understanding.py#L1769) | 1769 | `"            # and slots rather than combining a superseded city/budget with the new one."` | — |
| [SRC-686F71AA50-L001770](../../agents/task_understanding.py#L1770) | 1770 | `"            buyer_seed = context_anchor or primary_seed or base"` | — |
| [SRC-686F71AA50-L001771](../../agents/task_understanding.py#L1771) | 1771 | `"            buyer_queries = ("` | — |
| [SRC-686F71AA50-L001772](../../agents/task_understanding.py#L1772) | 1772 | `"                f'\"مطلوب شراء\" {buyer_seed}',"` | — |
| [SRC-686F71AA50-L001773](../../agents/task_understanding.py#L1773) | 1773 | `"                f'\"طلب عرض سعر\" {buyer_seed}',"` | — |
| [SRC-686F71AA50-L001774](../../agents/task_understanding.py#L1774) | 1774 | `"                f'\"looking to buy\" {buyer_seed}',"` | — |
| [SRC-686F71AA50-L001775](../../agents/task_understanding.py#L1775) | 1775 | `"                f'\"request for quotation\" {buyer_seed}',"` | — |
| [SRC-686F71AA50-L001776](../../agents/task_understanding.py#L1776) | 1776 | `"            )"` | — |
| [SRC-686F71AA50-L001777](../../agents/task_understanding.py#L1777) | 1777 | `"            for query in buyer_queries:"` | — |
| [SRC-686F71AA50-L001778](../../agents/task_understanding.py#L1778) | 1778 | `"                add("` | — |
| [SRC-686F71AA50-L001779](../../agents/task_understanding.py#L1779) | 1779 | `"                    query,"` | — |
| [SRC-686F71AA50-L001780](../../agents/task_understanding.py#L1780) | 1780 | `"                    \"buyer_intent\","` | — |
| [SRC-686F71AA50-L001781](../../agents/task_understanding.py#L1781) | 1781 | `"                    \"rebuild purchaser-language query from the resolved buyer need and current constraints\","` | — |
| [SRC-686F71AA50-L001782](../../agents/task_understanding.py#L1782) | 1782 | `"                    enforce_topic=False,"` | — |
| [SRC-686F71AA50-L001783](../../agents/task_understanding.py#L1783) | 1783 | `"                )"` | — |
| [SRC-686F71AA50-L001784](../../agents/task_understanding.py#L1784) | 1784 | `"                if len(rows) >= maximum:"` | — |
| [SRC-686F71AA50-L001785](../../agents/task_understanding.py#L1785) | 1785 | `"                    break"` | — |
| [SRC-686F71AA50-L001786](../../agents/task_understanding.py#L1786) | 1786 | `"            return rows"` | — |
| [SRC-686F71AA50-L001787](../../agents/task_understanding.py#L1787) | 1787 | `"        for query in queries:"` | — |
| [SRC-686F71AA50-L001788](../../agents/task_understanding.py#L1788) | 1788 | `"            add("` | — |
| [SRC-686F71AA50-L001789](../../agents/task_understanding.py#L1789) | 1789 | `"                query,"` | — |
| [SRC-686F71AA50-L001790](../../agents/task_understanding.py#L1790) | 1790 | `"                \"buyer_intent\","` | — |
| [SRC-686F71AA50-L001791](../../agents/task_understanding.py#L1791) | 1791 | `"                \"product-anchored purchaser-language query\","` | — |
| [SRC-686F71AA50-L001792](../../agents/task_understanding.py#L1792) | 1792 | `"                enforce_topic=False,"` | — |
| [SRC-686F71AA50-L001793](../../agents/task_understanding.py#L1793) | 1793 | `"            )"` | — |
| [SRC-686F71AA50-L001794](../../agents/task_understanding.py#L1794) | 1794 | `"            if len(rows) >= maximum:"` | — |
| [SRC-686F71AA50-L001795](../../agents/task_understanding.py#L1795) | 1795 | `"                break"` | — |
| [SRC-686F71AA50-L001796](../../agents/task_understanding.py#L1796) | 1796 | `"        return rows"` | — |
| [SRC-686F71AA50-L001797](../../agents/task_understanding.py#L1797) | 1797 | `""` | — |
| [SRC-686F71AA50-L001798](../../agents/task_understanding.py#L1798) | 1798 | `"    candidates = _generated_strategy_candidates(base, spec_for_candidates)"` | — |
| [SRC-686F71AA50-L001799](../../agents/task_understanding.py#L1799) | 1799 | `"    for query, strategy, rationale in candidates:"` | — |
| [SRC-686F71AA50-L001800](../../agents/task_understanding.py#L1800) | 1800 | `"        add("` | — |
| [SRC-686F71AA50-L001801](../../agents/task_understanding.py#L1801) | 1801 | `"            query, strategy, rationale,"` | — |
| [SRC-686F71AA50-L001802](../../agents/task_understanding.py#L1802) | 1802 | `"            enforce_topic=(strategy != \"explicit_criterion\"),"` | — |
| [SRC-686F71AA50-L001803](../../agents/task_understanding.py#L1803) | 1803 | `"        )"` | — |
| [SRC-686F71AA50-L001804](../../agents/task_understanding.py#L1804) | 1804 | `"        if len(rows) >= maximum:"` | — |
| [SRC-686F71AA50-L001805](../../agents/task_understanding.py#L1805) | 1805 | `"            break"` | — |
| [SRC-686F71AA50-L001806](../../agents/task_understanding.py#L1806) | 1806 | `""` | — |
| [SRC-686F71AA50-L001807](../../agents/task_understanding.py#L1807) | 1807 | `"    # A brief confirmed follow-up can be fully understood yet produce no"` | — |
| [SRC-686F71AA50-L001808](../../agents/task_understanding.py#L1808) | 1808 | `"    # family-specific candidate (for example \"سعره؟\"). Add one primary-source"` | — |
| [SRC-686F71AA50-L001809](../../agents/task_understanding.py#L1809) | 1809 | `"    # alternative using the planner seed's language so alias checks prevent"` | — |
| [SRC-686F71AA50-L001810](../../agents/task_understanding.py#L1810) | 1810 | `"    # duplicating EUR/256GB/warranty as Arabic-only terms."` | — |
| [SRC-686F71AA50-L001811](../../agents/task_understanding.py#L1811) | 1811 | `"    if ("` | — |
| [SRC-686F71AA50-L001812](../../agents/task_understanding.py#L1812) | 1812 | `"        len(rows) == 1"` | — |
| [SRC-686F71AA50-L001813](../../agents/task_understanding.py#L1813) | 1813 | `"        and inherit_context"` | — |
| [SRC-686F71AA50-L001814](../../agents/task_understanding.py#L1814) | 1814 | `"        and context_anchor"` | — |
| [SRC-686F71AA50-L001815](../../agents/task_understanding.py#L1815) | 1815 | `"        and queries"` | — |
| [SRC-686F71AA50-L001816](../../agents/task_understanding.py#L1816) | 1816 | `"        and isinstance(queries[0], str)"` | — |
| [SRC-686F71AA50-L001817](../../agents/task_understanding.py#L1817) | 1817 | `"    ):"` | — |
| [SRC-686F71AA50-L001818](../../agents/task_understanding.py#L1818) | 1818 | `"        source_language_seed = planner_seed or primary_seed"` | — |
| [SRC-686F71AA50-L001819](../../agents/task_understanding.py#L1819) | 1819 | `"        seed_language_is_arabic = bool(re.search(r\"[\\u0600-\\u06FF]\", source_language_seed))"` | — |
| [SRC-686F71AA50-L001820](../../agents/task_understanding.py#L1820) | 1820 | `"        source_phrase = \"مصدر رسمي\" if seed_language_is_arabic else \"official source\""` | — |
| [SRC-686F71AA50-L001821](../../agents/task_understanding.py#L1821) | 1821 | `"        add("` | — |
| [SRC-686F71AA50-L001822](../../agents/task_understanding.py#L1822) | 1822 | `"            f\"{primary_seed} {source_phrase}\","` | — |
| [SRC-686F71AA50-L001823](../../agents/task_understanding.py#L1823) | 1823 | `"            \"dialogue_followup_primary_source\","` | — |
| [SRC-686F71AA50-L001824](../../agents/task_understanding.py#L1824) | 1824 | `"            \"retrieve primary evidence for a confirmed contextual follow-up\","` | — |
| [SRC-686F71AA50-L001825](../../agents/task_understanding.py#L1825) | 1825 | `"            enforce_topic=False,"` | — |
| [SRC-686F71AA50-L001826](../../agents/task_understanding.py#L1826) | 1826 | `"        )"` | — |
| [SRC-686F71AA50-L001827](../../agents/task_understanding.py#L1827) | 1827 | `""` | — |
| [SRC-686F71AA50-L001828](../../agents/task_understanding.py#L1828) | 1828 | `"    # Preserve other planner alternatives only after task-targeted candidates."` | — |
| [SRC-686F71AA50-L001829](../../agents/task_understanding.py#L1829) | 1829 | `"    for index, query in enumerate(queries[1:], start=1):"` | — |
| [SRC-686F71AA50-L001830](../../agents/task_understanding.py#L1830) | 1830 | `"        if len(rows) >= maximum:"` | — |
| [SRC-686F71AA50-L001831](../../agents/task_understanding.py#L1831) | 1831 | `"            break"` | — |
| [SRC-686F71AA50-L001832](../../agents/task_understanding.py#L1832) | 1832 | `"        # Once a contextual slot has been corrected, old alternatives are not"` | — |
| [SRC-686F71AA50-L001833](../../agents/task_understanding.py#L1833) | 1833 | `"        # safe to reuse: they may preserve the superseded city, currency, or budget."` | — |
| [SRC-686F71AA50-L001834](../../agents/task_understanding.py#L1834) | 1834 | `"        if scope_replacement:"` | — |
| [SRC-686F71AA50-L001835](../../agents/task_understanding.py#L1835) | 1835 | `"            continue"` | — |
| [SRC-686F71AA50-L001836](../../agents/task_understanding.py#L1836) | 1836 | `"        if ("` | — |
| [SRC-686F71AA50-L001837](../../agents/task_understanding.py#L1837) | 1837 | `"            entity_replacement"` | — |
| [SRC-686F71AA50-L001838](../../agents/task_understanding.py#L1838) | 1838 | `"            and entity_replacement_terms"` | — |
| [SRC-686F71AA50-L001839](../../agents/task_understanding.py#L1839) | 1839 | `"            and not any("` | — |
| [SRC-686F71AA50-L001840](../../agents/task_understanding.py#L1840) | 1840 | `"                normalize_text(term) in normalize_text(query)"` | — |
| [SRC-686F71AA50-L001841](../../agents/task_understanding.py#L1841) | 1841 | `"                for term in entity_replacement_terms"` | — |
| [SRC-686F71AA50-L001842](../../agents/task_understanding.py#L1842) | 1842 | `"            )"` | — |
| [SRC-686F71AA50-L001843](../../agents/task_understanding.py#L1843) | 1843 | `"        ):"` | — |
| [SRC-686F71AA50-L001844](../../agents/task_understanding.py#L1844) | 1844 | `"            continue"` | — |
| [SRC-686F71AA50-L001845](../../agents/task_understanding.py#L1845) | 1845 | `"        if isinstance(query, str):"` | — |
| [SRC-686F71AA50-L001846](../../agents/task_understanding.py#L1846) | 1846 | `"            strategy, rationale = _label_existing_query(query, index, spec)"` | — |
| [SRC-686F71AA50-L001847](../../agents/task_understanding.py#L1847) | 1847 | `"        else:"` | — |
| [SRC-686F71AA50-L001848](../../agents/task_understanding.py#L1848) | 1848 | `"            strategy, rationale = \"malformed\", \"planner alternative is not a string\""` | — |
| [SRC-686F71AA50-L001849](../../agents/task_understanding.py#L1849) | 1849 | `"        add(query, strategy, rationale, enforce_topic=False)"` | — |
| [SRC-686F71AA50-L001850](../../agents/task_understanding.py#L1850) | 1850 | `"    return rows"` | — |
| [SRC-686F71AA50-L001851](../../agents/task_understanding.py#L1851) | 1851 | `""` | — |
| [SRC-686F71AA50-L001852](../../agents/task_understanding.py#L1852) | 1852 | `"def validate_task_spec(value: Any) -> dict[str, Any]:"` | — |
| [SRC-686F71AA50-L001853](../../agents/task_understanding.py#L1853) | 1853 | `"    \"\"\"Return an allowlisted, bounded JSON representation of TaskSpec-like input.\"\"\""` | — |
| [SRC-686F71AA50-L001854](../../agents/task_understanding.py#L1854) | 1854 | `"    unavailable = {"` | — |
| [SRC-686F71AA50-L001855](../../agents/task_understanding.py#L1855) | 1855 | `"        \"schema\": \"omarai.task_spec.v1\","` | — |
| [SRC-686F71AA50-L001856](../../agents/task_understanding.py#L1856) | 1856 | `"        \"status\": \"not_available\","` | — |
| [SRC-686F71AA50-L001857](../../agents/task_understanding.py#L1857) | 1857 | `"        \"claim\": \"no validated task specification supplied\","` | — |
| [SRC-686F71AA50-L001858](../../agents/task_understanding.py#L1858) | 1858 | `"    }"` | — |
| [SRC-686F71AA50-L001859](../../agents/task_understanding.py#L1859) | 1859 | `"    if not isinstance(value, dict) or value.get(\"schema\") != \"omarai.task_spec.v1\":"` | — |
| [SRC-686F71AA50-L001860](../../agents/task_understanding.py#L1860) | 1860 | `"        return unavailable"` | — |
| [SRC-686F71AA50-L001861](../../agents/task_understanding.py#L1861) | 1861 | `""` | — |
| [SRC-686F71AA50-L001862](../../agents/task_understanding.py#L1862) | 1862 | `"    def clean_text(item: Any, limit: int = 160) -> str:"` | — |
| [SRC-686F71AA50-L001863](../../agents/task_understanding.py#L1863) | 1863 | `"        if not isinstance(item, str):"` | — |
| [SRC-686F71AA50-L001864](../../agents/task_understanding.py#L1864) | 1864 | `"            return \"\""` | — |
| [SRC-686F71AA50-L001865](../../agents/task_understanding.py#L1865) | 1865 | `"        return _SPACE.sub(\" \", unicodedata.normalize(\"NFKC\", item).replace(\"\\x00\", \" \")).strip()[:limit]"` | — |
| [SRC-686F71AA50-L001866](../../agents/task_understanding.py#L1866) | 1866 | `""` | — |
| [SRC-686F71AA50-L001867](../../agents/task_understanding.py#L1867) | 1867 | `"    def clean_list(item: Any, *, items: int = 16, chars: int = 160) -> list[str]:"` | — |
| [SRC-686F71AA50-L001868](../../agents/task_understanding.py#L1868) | 1868 | `"        if not isinstance(item, list):"` | — |
| [SRC-686F71AA50-L001869](../../agents/task_understanding.py#L1869) | 1869 | `"            return []"` | — |
| [SRC-686F71AA50-L001870](../../agents/task_understanding.py#L1870) | 1870 | `"        result: list[str] = []"` | — |
| [SRC-686F71AA50-L001871](../../agents/task_understanding.py#L1871) | 1871 | `"        seen: set[str] = set()"` | — |
| [SRC-686F71AA50-L001872](../../agents/task_understanding.py#L1872) | 1872 | `"        for raw_item in item[:items * 2]:"` | — |
| [SRC-686F71AA50-L001873](../../agents/task_understanding.py#L1873) | 1873 | `"            cleaned = clean_text(raw_item, chars)"` | — |
| [SRC-686F71AA50-L001874](../../agents/task_understanding.py#L1874) | 1874 | `"            key = cleaned.casefold()"` | — |
| [SRC-686F71AA50-L001875](../../agents/task_understanding.py#L1875) | 1875 | `"            if cleaned and key not in seen:"` | — |
| [SRC-686F71AA50-L001876](../../agents/task_understanding.py#L1876) | 1876 | `"                result.append(cleaned)"` | — |
| [SRC-686F71AA50-L001877](../../agents/task_understanding.py#L1877) | 1877 | `"                seen.add(key)"` | — |
| [SRC-686F71AA50-L001878](../../agents/task_understanding.py#L1878) | 1878 | `"            if len(result) >= items:"` | — |
| [SRC-686F71AA50-L001879](../../agents/task_understanding.py#L1879) | 1879 | `"                break"` | — |
| [SRC-686F71AA50-L001880](../../agents/task_understanding.py#L1880) | 1880 | `"        return result"` | — |
| [SRC-686F71AA50-L001881](../../agents/task_understanding.py#L1881) | 1881 | `""` | — |
| [SRC-686F71AA50-L001882](../../agents/task_understanding.py#L1882) | 1882 | `"    raw_constraints = value.get(\"constraints\")"` | — |
| [SRC-686F71AA50-L001883](../../agents/task_understanding.py#L1883) | 1883 | `"    raw_constraints = raw_constraints if isinstance(raw_constraints, dict) else {}"` | — |
| [SRC-686F71AA50-L001884](../../agents/task_understanding.py#L1884) | 1884 | `"    list_constraint_keys = ("` | — |
| [SRC-686F71AA50-L001885](../../agents/task_understanding.py#L1885) | 1885 | `"        \"explicit_locations\", \"explicit_years\", \"explicit_dates\","` | — |
| [SRC-686F71AA50-L001886](../../agents/task_understanding.py#L1886) | 1886 | `"        \"explicit_budgets\", \"explicit_urls\", \"explicit_aspects\", \"source_policies\","` | — |
| [SRC-686F71AA50-L001887](../../agents/task_understanding.py#L1887) | 1887 | `"    )"` | — |
| [SRC-686F71AA50-L001888](../../agents/task_understanding.py#L1888) | 1888 | `"    constraints: dict[str, Any] = {"` | — |
| [SRC-686F71AA50-L001889](../../agents/task_understanding.py#L1889) | 1889 | `"        key: clean_list(raw_constraints.get(key), items=8 if key == \"explicit_aspects\" else 5, chars=300 if key == \"explicit_urls\" else 120)"` | — |
| [SRC-686F71AA50-L001890](../../agents/task_understanding.py#L1890) | 1890 | `"        for key in list_constraint_keys"` | — |
| [SRC-686F71AA50-L001891](../../agents/task_understanding.py#L1891) | 1891 | `"    }"` | — |
| [SRC-686F71AA50-L001892](../../agents/task_understanding.py#L1892) | 1892 | `"    for key in ("` | — |
| [SRC-686F71AA50-L001893](../../agents/task_understanding.py#L1893) | 1893 | `"        \"inline_text_supplied_for_summary\","` | — |
| [SRC-686F71AA50-L001894](../../agents/task_understanding.py#L1894) | 1894 | `"        \"time_sensitive_request\","` | — |
| [SRC-686F71AA50-L001895](../../agents/task_understanding.py#L1895) | 1895 | `"        \"official_site_required\","` | — |
| [SRC-686F71AA50-L001896](../../agents/task_understanding.py#L1896) | 1896 | `"        \"official_destination_required\","` | — |
| [SRC-686F71AA50-L001897](../../agents/task_understanding.py#L1897) | 1897 | `"        \"social_evidence_requested\","` | — |
| [SRC-686F71AA50-L001898](../../agents/task_understanding.py#L1898) | 1898 | `"    ):"` | — |
| [SRC-686F71AA50-L001899](../../agents/task_understanding.py#L1899) | 1899 | `"        constraints[key] = raw_constraints.get(key) is True"` | — |
| [SRC-686F71AA50-L001900](../../agents/task_understanding.py#L1900) | 1900 | `"    language_profile = raw_constraints.get(\"language_profile\")"` | — |
| [SRC-686F71AA50-L001901](../../agents/task_understanding.py#L1901) | 1901 | `"    constraints[\"language_profile\"] = ("` | — |
| [SRC-686F71AA50-L001902](../../agents/task_understanding.py#L1902) | 1902 | `"        language_profile"` | — |
| [SRC-686F71AA50-L001903](../../agents/task_understanding.py#L1903) | 1903 | `"        if isinstance(language_profile, str) and language_profile in {\"ar\", \"en\", \"mixed\", \"und\"}"` | — |
| [SRC-686F71AA50-L001904](../../agents/task_understanding.py#L1904) | 1904 | `"        else \"und\""` | — |
| [SRC-686F71AA50-L001905](../../agents/task_understanding.py#L1905) | 1905 | `"    )"` | — |
| [SRC-686F71AA50-L001906](../../agents/task_understanding.py#L1906) | 1906 | `"    allowed_source_policies = {"` | — |
| [SRC-686F71AA50-L001907](../../agents/task_understanding.py#L1907) | 1907 | `"        \"government_official_destination\", \"official_destination\", \"current_read_page\","` | — |
| [SRC-686F71AA50-L001908](../../agents/task_understanding.py#L1908) | 1908 | `"        \"public_social_content\", \"authoritative_health_content\", \"official_legal_text\","` | — |
| [SRC-686F71AA50-L001909](../../agents/task_understanding.py#L1909) | 1909 | `"        \"task_relevant_sources\", \"unassessed\","` | — |
| [SRC-686F71AA50-L001910](../../agents/task_understanding.py#L1910) | 1910 | `"    }"` | — |
| [SRC-686F71AA50-L001911](../../agents/task_understanding.py#L1911) | 1911 | `"    source_policy = clean_text(raw_constraints.get(\"source_policy\"), 80)"` | — |
| [SRC-686F71AA50-L001912](../../agents/task_understanding.py#L1912) | 1912 | `"    constraints[\"source_policy\"] = source_policy if source_policy in allowed_source_policies else \"unassessed\""` | — |
| [SRC-686F71AA50-L001913](../../agents/task_understanding.py#L1913) | 1913 | `"    constraints[\"source_policies\"] = ["` | — |
| [SRC-686F71AA50-L001914](../../agents/task_understanding.py#L1914) | 1914 | `"        item for item in constraints[\"source_policies\"]"` | — |
| [SRC-686F71AA50-L001915](../../agents/task_understanding.py#L1915) | 1915 | `"        if item in allowed_source_policies"` | — |
| [SRC-686F71AA50-L001916](../../agents/task_understanding.py#L1916) | 1916 | `"    ]"` | — |
| [SRC-686F71AA50-L001917](../../agents/task_understanding.py#L1917) | 1917 | `""` | — |
| [SRC-686F71AA50-L001918](../../agents/task_understanding.py#L1918) | 1918 | `"    raw_preferences = value.get(\"output_preferences\")"` | — |
| [SRC-686F71AA50-L001919](../../agents/task_understanding.py#L1919) | 1919 | `"    raw_preferences = raw_preferences if isinstance(raw_preferences, dict) else {}"` | — |
| [SRC-686F71AA50-L001920](../../agents/task_understanding.py#L1920) | 1920 | `"    preference_keys = ("` | — |
| [SRC-686F71AA50-L001921](../../agents/task_understanding.py#L1921) | 1921 | `"        \"concise\", \"detailed\", \"examples_requested\", \"table_requested\","` | — |
| [SRC-686F71AA50-L001922](../../agents/task_understanding.py#L1922) | 1922 | `"        \"bullets_or_checklist_requested\", \"beginner_friendly_requested\","` | — |
| [SRC-686F71AA50-L001923](../../agents/task_understanding.py#L1923) | 1923 | `"        \"citations_requested\", \"links_requested\", \"json_requested\","` | — |
| [SRC-686F71AA50-L001924](../../agents/task_understanding.py#L1924) | 1924 | `"    )"` | — |
| [SRC-686F71AA50-L001925](../../agents/task_understanding.py#L1925) | 1925 | `"    output_preferences = {key: raw_preferences.get(key) is True for key in preference_keys}"` | — |
| [SRC-686F71AA50-L001926](../../agents/task_understanding.py#L1926) | 1926 | `""` | — |
| [SRC-686F71AA50-L001927](../../agents/task_understanding.py#L1927) | 1927 | `"    raw_context = value.get(\"context_resolution\")"` | — |
| [SRC-686F71AA50-L001928](../../agents/task_understanding.py#L1928) | 1928 | `"    raw_context = raw_context if isinstance(raw_context, dict) else {}"` | — |
| [SRC-686F71AA50-L001929](../../agents/task_understanding.py#L1929) | 1929 | `"    raw_slots = raw_context.get(\"slots\")"` | — |
| [SRC-686F71AA50-L001930](../../agents/task_understanding.py#L1930) | 1930 | `"    slots: dict[str, str] = {}"` | — |
| [SRC-686F71AA50-L001931](../../agents/task_understanding.py#L1931) | 1931 | `"    if isinstance(raw_slots, dict):"` | — |
| [SRC-686F71AA50-L001932](../../agents/task_understanding.py#L1932) | 1932 | `"        for raw_key, raw_value in list(raw_slots.items())[:16]:"` | — |
| [SRC-686F71AA50-L001933](../../agents/task_understanding.py#L1933) | 1933 | `"            key = clean_text(raw_key, 40)"` | — |
| [SRC-686F71AA50-L001934](../../agents/task_understanding.py#L1934) | 1934 | `"            item = clean_text(raw_value, 180)"` | — |
| [SRC-686F71AA50-L001935](../../agents/task_understanding.py#L1935) | 1935 | `"            if key and item:"` | — |
| [SRC-686F71AA50-L001936](../../agents/task_understanding.py#L1936) | 1936 | `"                slots[key] = item"` | — |
| [SRC-686F71AA50-L001937](../../agents/task_understanding.py#L1937) | 1937 | `"    context_resolution = {"` | — |
| [SRC-686F71AA50-L001938](../../agents/task_understanding.py#L1938) | 1938 | `"        \"method\": clean_text(raw_context.get(\"method\"), 80) or \"not_provided\","` | — |
| [SRC-686F71AA50-L001939](../../agents/task_understanding.py#L1939) | 1939 | `"        \"resolved_question\": clean_text(raw_context.get(\"resolved_question\"), MAX_TASK_CHARS),"` | — |
| [SRC-686F71AA50-L001940](../../agents/task_understanding.py#L1940) | 1940 | `"        \"topic\": clean_text(raw_context.get(\"topic\"), 180),"` | — |
| [SRC-686F71AA50-L001941](../../agents/task_understanding.py#L1941) | 1941 | `"        \"entities\": clean_list(raw_context.get(\"entities\"), items=8, chars=120),"` | — |
| [SRC-686F71AA50-L001942](../../agents/task_understanding.py#L1942) | 1942 | `"        \"slots\": slots,"` | — |
| [SRC-686F71AA50-L001943](../../agents/task_understanding.py#L1943) | 1943 | `"        \"changed_slots\": clean_list(raw_context.get(\"changed_slots\"), items=8, chars=40),"` | — |
| [SRC-686F71AA50-L001944](../../agents/task_understanding.py#L1944) | 1944 | `"        \"is_follow_up\": raw_context.get(\"is_follow_up\") is True,"` | — |
| [SRC-686F71AA50-L001945](../../agents/task_understanding.py#L1945) | 1945 | `"        \"topic_shift\": raw_context.get(\"topic_shift\") is True,"` | — |
| [SRC-686F71AA50-L001946](../../agents/task_understanding.py#L1946) | 1946 | `"        \"resolution_basis\": clean_text(raw_context.get(\"resolution_basis\"), 80) or \"unassessed\","` | — |
| [SRC-686F71AA50-L001947](../../agents/task_understanding.py#L1947) | 1947 | `"        \"confidence_band\": ("` | — |
| [SRC-686F71AA50-L001948](../../agents/task_understanding.py#L1948) | 1948 | `"            raw_context.get(\"confidence_band\")"` | — |
| [SRC-686F71AA50-L001949](../../agents/task_understanding.py#L1949) | 1949 | `"            if isinstance(raw_context.get(\"confidence_band\"), str)"` | — |
| [SRC-686F71AA50-L001950](../../agents/task_understanding.py#L1950) | 1950 | `"            and raw_context.get(\"confidence_band\") in {\"low\", \"medium\", \"high\", \"unassessed\"}"` | — |
| [SRC-686F71AA50-L001951](../../agents/task_understanding.py#L1951) | 1951 | `"            else \"unassessed\""` | — |
| [SRC-686F71AA50-L001952](../../agents/task_understanding.py#L1952) | 1952 | `"        ),"` | — |
| [SRC-686F71AA50-L001953](../../agents/task_understanding.py#L1953) | 1953 | `"        \"needs_clarification\": raw_context.get(\"needs_clarification\") is True,"` | — |
| [SRC-686F71AA50-L001954](../../agents/task_understanding.py#L1954) | 1954 | `"        \"unresolved_references\": clean_list(raw_context.get(\"unresolved_references\"), items=8, chars=100),"` | — |
| [SRC-686F71AA50-L001955](../../agents/task_understanding.py#L1955) | 1955 | `"    }"` | — |
| [SRC-686F71AA50-L001956](../../agents/task_understanding.py#L1956) | 1956 | `""` | — |
| [SRC-686F71AA50-L001957](../../agents/task_understanding.py#L1957) | 1957 | `"    raw_hypotheses = value.get(\"hypothesis_interpretations\")"` | — |
| [SRC-686F71AA50-L001958](../../agents/task_understanding.py#L1958) | 1958 | `"    hypotheses: list[dict[str, Any]] = []"` | — |
| [SRC-686F71AA50-L001959](../../agents/task_understanding.py#L1959) | 1959 | `"    if isinstance(raw_hypotheses, list):"` | — |
| [SRC-686F71AA50-L001960](../../agents/task_understanding.py#L1960) | 1960 | `"        for item in raw_hypotheses[:8]:"` | — |
| [SRC-686F71AA50-L001961](../../agents/task_understanding.py#L1961) | 1961 | `"            if not isinstance(item, dict):"` | — |
| [SRC-686F71AA50-L001962](../../agents/task_understanding.py#L1962) | 1962 | `"                continue"` | — |
| [SRC-686F71AA50-L001963](../../agents/task_understanding.py#L1963) | 1963 | `"            count = item.get(\"matched_signal_count\")"` | — |
| [SRC-686F71AA50-L001964](../../agents/task_understanding.py#L1964) | 1964 | `"            hypotheses.append({"` | — |
| [SRC-686F71AA50-L001965](../../agents/task_understanding.py#L1965) | 1965 | `"                \"family\": clean_text(item.get(\"family\"), 80),"` | — |
| [SRC-686F71AA50-L001966](../../agents/task_understanding.py#L1966) | 1966 | `"                \"matched_signal_count\": max(0, min(32, count)) if isinstance(count, int) else 0,"` | — |
| [SRC-686F71AA50-L001967](../../agents/task_understanding.py#L1967) | 1967 | `"                \"signals\": clean_list(item.get(\"signals\"), items=4, chars=100),"` | — |
| [SRC-686F71AA50-L001968](../../agents/task_understanding.py#L1968) | 1968 | `"                \"status\": clean_text(item.get(\"status\"), 60) or \"unassessed\","` | — |
| [SRC-686F71AA50-L001969](../../agents/task_understanding.py#L1969) | 1969 | `"                \"selected\": item.get(\"selected\") is True,"` | — |
| [SRC-686F71AA50-L001970](../../agents/task_understanding.py#L1970) | 1970 | `"            })"` | — |
| [SRC-686F71AA50-L001971](../../agents/task_understanding.py#L1971) | 1971 | `""` | — |
| [SRC-686F71AA50-L001972](../../agents/task_understanding.py#L1972) | 1972 | `"    allowed_families = {"` | — |
| [SRC-686F71AA50-L001973](../../agents/task_understanding.py#L1973) | 1973 | `"        name for name in _PATTERNS if not name.startswith(\"output_\")"` | — |
| [SRC-686F71AA50-L001974](../../agents/task_understanding.py#L1974) | 1974 | `"    } \| {\"general_question\", \"ambiguous_or_incomplete\", \"web_research\"}"` | — |
| [SRC-686F71AA50-L001975](../../agents/task_understanding.py#L1975) | 1975 | `"    raw_family = clean_text(value.get(\"task_family\"), 80)"` | — |
| [SRC-686F71AA50-L001976](../../agents/task_understanding.py#L1976) | 1976 | `"    raw_mode = clean_text(value.get(\"mode\"), 20)"` | — |
| [SRC-686F71AA50-L001977](../../agents/task_understanding.py#L1977) | 1977 | `"    raw_route = clean_text(value.get(\"intent_route\"), 40)"` | — |
| [SRC-686F71AA50-L001978](../../agents/task_understanding.py#L1978) | 1978 | `"    allowed_routes = {"` | — |
| [SRC-686F71AA50-L001979](../../agents/task_understanding.py#L1979) | 1979 | `"        \"LOCAL\", \"MODEL_ONLY\", \"CLARIFY\", \"WEB_SIMPLE\", \"WEB_DEEP\","` | — |
| [SRC-686F71AA50-L001980](../../agents/task_understanding.py#L1980) | 1980 | `"        \"LEAD_GENERATION\", \"BUDGET_EXHAUSTED\", \"deterministic_fallback\","` | — |
| [SRC-686F71AA50-L001981](../../agents/task_understanding.py#L1981) | 1981 | `"        \"validated_language_model_plan\", \"unassessed\","` | — |
| [SRC-686F71AA50-L001982](../../agents/task_understanding.py#L1982) | 1982 | `"    }"` | — |
| [SRC-686F71AA50-L001983](../../agents/task_understanding.py#L1983) | 1983 | `"    allowed_tools = {"` | — |
| [SRC-686F71AA50-L001984](../../agents/task_understanding.py#L1984) | 1984 | `"        \"web_search\", \"page_fetch\", \"public_social_search_if_configured\","` | — |
| [SRC-686F71AA50-L001985](../../agents/task_understanding.py#L1985) | 1985 | `"        \"language_model_generation_if_configured\", \"claim_review_if_configured\","` | — |
| [SRC-686F71AA50-L001986](../../agents/task_understanding.py#L1986) | 1986 | `"    }"` | — |
| [SRC-686F71AA50-L001987](../../agents/task_understanding.py#L1987) | 1987 | `"    allowed_slots = TASK_CONTEXT_SLOT_KEYS"` | — |
| [SRC-686F71AA50-L001988](../../agents/task_understanding.py#L1988) | 1988 | `"    context_resolution[\"slots\"] = {"` | — |
| [SRC-686F71AA50-L001989](../../agents/task_understanding.py#L1989) | 1989 | `"        key: item for key, item in context_resolution[\"slots\"].items()"` | — |
| [SRC-686F71AA50-L001990](../../agents/task_understanding.py#L1990) | 1990 | `"        if key in allowed_slots"` | — |
| [SRC-686F71AA50-L001991](../../agents/task_understanding.py#L1991) | 1991 | `"    }"` | — |
| [SRC-686F71AA50-L001992](../../agents/task_understanding.py#L1992) | 1992 | `"    hypotheses = ["` | — |
| [SRC-686F71AA50-L001993](../../agents/task_understanding.py#L1993) | 1993 | `"        item for item in hypotheses"` | — |
| [SRC-686F71AA50-L001994](../../agents/task_understanding.py#L1994) | 1994 | `"        if item.get(\"family\") in allowed_families"` | — |
| [SRC-686F71AA50-L001995](../../agents/task_understanding.py#L1995) | 1995 | `"    ]"` | — |
| [SRC-686F71AA50-L001996](../../agents/task_understanding.py#L1996) | 1996 | `"    raw_secondary = clean_list(value.get(\"secondary_task_types\"), items=16, chars=80)"` | — |
| [SRC-686F71AA50-L001997](../../agents/task_understanding.py#L1997) | 1997 | `"    spec = {"` | — |
| [SRC-686F71AA50-L001998](../../agents/task_understanding.py#L1998) | 1998 | `"        \"schema\": \"omarai.task_spec.v1\","` | — |
| [SRC-686F71AA50-L001999](../../agents/task_understanding.py#L1999) | 1999 | `"        \"task_family\": raw_family if raw_family in allowed_families else \"general_question\","` | — |
| [SRC-686F71AA50-L002000](../../agents/task_understanding.py#L2000) | 2000 | `"        \"mode\": raw_mode if raw_mode in SUPPORTED_MODES else \"auto\","` | — |
| [SRC-686F71AA50-L002001](../../agents/task_understanding.py#L2001) | 2001 | `"        \"intent_route\": raw_route if raw_route in allowed_routes else \"unassessed\","` | — |
| [SRC-686F71AA50-L002002](../../agents/task_understanding.py#L2002) | 2002 | `"        \"classification_method\": clean_text(value.get(\"classification_method\"), 100),"` | — |
| [SRC-686F71AA50-L002003](../../agents/task_understanding.py#L2003) | 2003 | `"        \"classification_is_probability\": False,"` | — |
| [SRC-686F71AA50-L002004](../../agents/task_understanding.py#L2004) | 2004 | `"        \"ambiguity_status\": clean_text(value.get(\"ambiguity_status\"), 80) or \"unassessed\","` | — |
| [SRC-686F71AA50-L002005](../../agents/task_understanding.py#L2005) | 2005 | `"        \"missing_required_inputs\": ["` | — |
| [SRC-686F71AA50-L002006](../../agents/task_understanding.py#L2006) | 2006 | `"            item for item in clean_list(value.get(\"missing_required_inputs\"), items=8, chars=100)"` | — |
| [SRC-686F71AA50-L002007](../../agents/task_understanding.py#L2007) | 2007 | `"            if item in {"` | — |
| [SRC-686F71AA50-L002008](../../agents/task_understanding.py#L2008) | 2008 | `"                \"unresolved_referent_or_incomplete_request\","` | — |
| [SRC-686F71AA50-L002009](../../agents/task_understanding.py#L2009) | 2009 | `"                \"official_destination_target_entity\","` | — |
| [SRC-686F71AA50-L002010](../../agents/task_understanding.py#L2010) | 2010 | `"                \"summary_source_url_or_pasted_text\","` | — |
| [SRC-686F71AA50-L002011](../../agents/task_understanding.py#L2011) | 2011 | `"            }"` | — |
| [SRC-686F71AA50-L002012](../../agents/task_understanding.py#L2012) | 2012 | `"        ],"` | — |
| [SRC-686F71AA50-L002013](../../agents/task_understanding.py#L2013) | 2013 | `"        \"requires_clarification\": value.get(\"requires_clarification\") is True,"` | — |
| [SRC-686F71AA50-L002014](../../agents/task_understanding.py#L2014) | 2014 | `"        \"clarification_reason\": clean_text(value.get(\"clarification_reason\"), 80) or \"unassessed\","` | — |
| [SRC-686F71AA50-L002015](../../agents/task_understanding.py#L2015) | 2015 | `"        \"context_resolution\": context_resolution,"` | — |
| [SRC-686F71AA50-L002016](../../agents/task_understanding.py#L2016) | 2016 | `"        \"secondary_task_types\": ["` | — |
| [SRC-686F71AA50-L002017](../../agents/task_understanding.py#L2017) | 2017 | `"            item for item in raw_secondary if item in allowed_families"` | — |
| [SRC-686F71AA50-L002018](../../agents/task_understanding.py#L2018) | 2018 | `"        ],"` | — |
| [SRC-686F71AA50-L002019](../../agents/task_understanding.py#L2019) | 2019 | `"        \"constraints\": constraints,"` | — |
| [SRC-686F71AA50-L002020](../../agents/task_understanding.py#L2020) | 2020 | `"        \"output_preferences\": output_preferences,"` | — |
| [SRC-686F71AA50-L002021](../../agents/task_understanding.py#L2021) | 2021 | `"        \"evidence_requirements\": clean_list(value.get(\"evidence_requirements\"), items=32, chars=180),"` | — |
| [SRC-686F71AA50-L002022](../../agents/task_understanding.py#L2022) | 2022 | `"        \"query_strategies\": clean_list(value.get(\"query_strategies\"), items=32, chars=100),"` | — |
| [SRC-686F71AA50-L002023](../../agents/task_understanding.py#L2023) | 2023 | `"        \"tool_requirements\": ["` | — |
| [SRC-686F71AA50-L002024](../../agents/task_understanding.py#L2024) | 2024 | `"            item for item in clean_list(value.get(\"tool_requirements\"), items=12, chars=100)"` | — |
| [SRC-686F71AA50-L002025](../../agents/task_understanding.py#L2025) | 2025 | `"            if item in allowed_tools"` | — |
| [SRC-686F71AA50-L002026](../../agents/task_understanding.py#L2026) | 2026 | `"        ],"` | — |
| [SRC-686F71AA50-L002027](../../agents/task_understanding.py#L2027) | 2027 | `"        \"decision_checks\": clean_list(value.get(\"decision_checks\"), items=24, chars=120),"` | — |
| [SRC-686F71AA50-L002028](../../agents/task_understanding.py#L2028) | 2028 | `"        \"reasoning_strategy_ids\": ["` | — |
| [SRC-686F71AA50-L002029](../../agents/task_understanding.py#L2029) | 2029 | `"            item for item in clean_list(value.get(\"reasoning_strategy_ids\"), items=12, chars=80)"` | — |
| [SRC-686F71AA50-L002030](../../agents/task_understanding.py#L2030) | 2030 | `"            if item in _REASONING_GUIDANCE"` | — |
| [SRC-686F71AA50-L002031](../../agents/task_understanding.py#L2031) | 2031 | `"        ],"` | — |
| [SRC-686F71AA50-L002032](../../agents/task_understanding.py#L2032) | 2032 | `"        # The matrix is code-owned. Ignore arbitrary incoming rows and return the"` | — |
| [SRC-686F71AA50-L002033](../../agents/task_understanding.py#L2033) | 2033 | `"        # canonical allowlisted policy so untrusted task/planner data cannot rewrite it."` | — |
| [SRC-686F71AA50-L002034](../../agents/task_understanding.py#L2034) | 2034 | `"        \"decision_matrix\": [dict(row) for row in _DECISION_MATRIX],"` | — |
| [SRC-686F71AA50-L002035](../../agents/task_understanding.py#L2035) | 2035 | `"        \"hypothesis_interpretations\": hypotheses,"` | — |
| [SRC-686F71AA50-L002036](../../agents/task_understanding.py#L2036) | 2036 | `"        \"limits\": {"` | — |
| [SRC-686F71AA50-L002037](../../agents/task_understanding.py#L2037) | 2037 | `"            \"max_question_chars\": MAX_TASK_CHARS,"` | — |
| [SRC-686F71AA50-L002038](../../agents/task_understanding.py#L2038) | 2038 | `"            \"max_aspects\": MAX_TASK_ASPECTS,"` | — |
| [SRC-686F71AA50-L002039](../../agents/task_understanding.py#L2039) | 2039 | `"            \"max_query_strategies\": MAX_STRATEGY_QUERIES,"` | — |
| [SRC-686F71AA50-L002040](../../agents/task_understanding.py#L2040) | 2040 | `"        },"` | — |
| [SRC-686F71AA50-L002041](../../agents/task_understanding.py#L2041) | 2041 | `"        \"claim\": \"task planning metadata only; not semantic certainty or factual verification\","` | — |
| [SRC-686F71AA50-L002042](../../agents/task_understanding.py#L2042) | 2042 | `"    }"` | — |
| [SRC-686F71AA50-L002043](../../agents/task_understanding.py#L2043) | 2043 | `"    for key in (\"planner_freshness\", \"planner_depth\"):"` | — |
| [SRC-686F71AA50-L002044](../../agents/task_understanding.py#L2044) | 2044 | `"        if key in value:"` | — |
| [SRC-686F71AA50-L002045](../../agents/task_understanding.py#L2045) | 2045 | `"            spec[key] = clean_text(value.get(key), 40) or \"unknown\""` | — |
| [SRC-686F71AA50-L002046](../../agents/task_understanding.py#L2046) | 2046 | `"    return spec"` | — |
## الوكيل والمنطق

### FILE-FC84E5B115 — [agents/text_normalization.py](../../agents/text_normalization.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-FC84E5B115-L000001](../../agents/text_normalization.py#L1) | 1 | `"\"\"\"Shared public text normalization primitives for Arabic and English matching."` | — |
| [SRC-FC84E5B115-L000002](../../agents/text_normalization.py#L2) | 2 | `""` | — |
| [SRC-FC84E5B115-L000003](../../agents/text_normalization.py#L3) | 3 | `"This module owns Unicode/Arabic normalization and token extraction. It has no knowledge"` | — |
| [SRC-FC84E5B115-L000004](../../agents/text_normalization.py#L4) | 4 | `"of search, sources, citations, or answer policy."` | — |
| [SRC-FC84E5B115-L000005](../../agents/text_normalization.py#L5) | 5 | `"\"\"\""` | — |
| [SRC-FC84E5B115-L000006](../../agents/text_normalization.py#L6) | 6 | `"from __future__ import annotations"` | — |
| [SRC-FC84E5B115-L000007](../../agents/text_normalization.py#L7) | 7 | `""` | — |
| [SRC-FC84E5B115-L000008](../../agents/text_normalization.py#L8) | 8 | `"import re"` | — |
| [SRC-FC84E5B115-L000009](../../agents/text_normalization.py#L9) | 9 | `"import unicodedata"` | — |
| [SRC-FC84E5B115-L000010](../../agents/text_normalization.py#L10) | 10 | `"from typing import Any"` | — |
| [SRC-FC84E5B115-L000011](../../agents/text_normalization.py#L11) | 11 | `""` | — |
| [SRC-FC84E5B115-L000012](../../agents/text_normalization.py#L12) | 12 | `"_DIGITS = str.maketrans(\"٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹\", \"01234567890123456789\")"` | — |
| [SRC-FC84E5B115-L000013](../../agents/text_normalization.py#L13) | 13 | `"_ARABIC_NORMALIZATION = str.maketrans({"` | — |
| [SRC-FC84E5B115-L000014](../../agents/text_normalization.py#L14) | 14 | `"    \"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ٱ\": \"ا\", \"ى\": \"ي\","` | — |
| [SRC-FC84E5B115-L000015](../../agents/text_normalization.py#L15) | 15 | `"    \"ؤ\": \"و\", \"ئ\": \"ي\", \"ة\": \"ه\", \"ـ\": \"\","` | — |
| [SRC-FC84E5B115-L000016](../../agents/text_normalization.py#L16) | 16 | `"})"` | — |
| [SRC-FC84E5B115-L000017](../../agents/text_normalization.py#L17) | 17 | `"_DIACRITICS = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-FC84E5B115-L000018](../../agents/text_normalization.py#L18) | 18 | `"_TOKEN = re.compile(r\"[a-z0-9]+\|[\\u0621-\\u064A\\u0660-\\u0669]+\", re.IGNORECASE)"` | — |
| [SRC-FC84E5B115-L000019](../../agents/text_normalization.py#L19) | 19 | `""` | — |
| [SRC-FC84E5B115-L000020](../../agents/text_normalization.py#L20) | 20 | `"_STOPWORDS = {"` | — |
| [SRC-FC84E5B115-L000021](../../agents/text_normalization.py#L21) | 21 | `"    \"من\", \"في\", \"على\", \"عن\", \"الى\", \"و\", \"او\", \"هل\", \"ما\", \"ماذا\", \"كيف\","` | — |
| [SRC-FC84E5B115-L000022](../../agents/text_normalization.py#L22) | 22 | `"    \"مع\", \"بين\", \"هذا\", \"هذه\", \"ذلك\", \"تلك\", \"الذي\", \"التي\", \"هو\", \"هي\","` | — |
| [SRC-FC84E5B115-L000023](../../agents/text_normalization.py#L23) | 23 | `"    \"the\", \"a\", \"an\", \"and\", \"or\", \"in\", \"on\", \"of\", \"to\", \"for\", \"with\","` | — |
| [SRC-FC84E5B115-L000024](../../agents/text_normalization.py#L24) | 24 | `"    \"from\", \"is\", \"are\", \"what\", \"which\", \"who\", \"how\", \"why\", \"when\","` | — |
| [SRC-FC84E5B115-L000025](../../agents/text_normalization.py#L25) | 25 | `"    \"where\", \"compare\", \"comparison\", \"based\", \"terms\", \"respect\","` | — |
| [SRC-FC84E5B115-L000026](../../agents/text_normalization.py#L26) | 26 | `"}"` | — |
| [SRC-FC84E5B115-L000027](../../agents/text_normalization.py#L27) | 27 | `""` | — |
| [SRC-FC84E5B115-L000028](../../agents/text_normalization.py#L28) | 28 | `""` | — |
| [SRC-FC84E5B115-L000029](../../agents/text_normalization.py#L29) | 29 | `"def normalize_text(value: Any) -> str:"` | — |
| [SRC-FC84E5B115-L000030](../../agents/text_normalization.py#L30) | 30 | `"    \"\"\"Normalize Unicode, Arabic letter variants, diacritics, and Arabic-Indic digits.\"\"\""` | — |
| [SRC-FC84E5B115-L000031](../../agents/text_normalization.py#L31) | 31 | `"    text = unicodedata.normalize(\"NFKC\", str(value or \"\")).casefold().translate(_DIGITS)"` | — |
| [SRC-FC84E5B115-L000032](../../agents/text_normalization.py#L32) | 32 | `"    text = _DIACRITICS.sub(\"\", text).translate(_ARABIC_NORMALIZATION)"` | — |
| [SRC-FC84E5B115-L000033](../../agents/text_normalization.py#L33) | 33 | `"    return text"` | — |
| [SRC-FC84E5B115-L000034](../../agents/text_normalization.py#L34) | 34 | `""` | — |
| [SRC-FC84E5B115-L000035](../../agents/text_normalization.py#L35) | 35 | `""` | — |
| [SRC-FC84E5B115-L000036](../../agents/text_normalization.py#L36) | 36 | `"def tokenize_text(value: Any, *, drop_stopwords: bool = False) -> list[str]:"` | — |
| [SRC-FC84E5B115-L000037](../../agents/text_normalization.py#L37) | 37 | `"    \"\"\"Tokenize normalized Arabic/English text with optional stopword removal.\"\"\""` | — |
| [SRC-FC84E5B115-L000038](../../agents/text_normalization.py#L38) | 38 | `"    tokens = _TOKEN.findall(normalize_text(value))"` | — |
| [SRC-FC84E5B115-L000039](../../agents/text_normalization.py#L39) | 39 | `"    if drop_stopwords:"` | — |
| [SRC-FC84E5B115-L000040](../../agents/text_normalization.py#L40) | 40 | `"        tokens = [token for token in tokens if token not in _STOPWORDS]"` | — |
| [SRC-FC84E5B115-L000041](../../agents/text_normalization.py#L41) | 41 | `"    return tokens"` | — |
## الوكيل والمنطق

### FILE-0799EEEB02 — [agents/tool_execution_status.py](../../agents/tool_execution_status.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-0799EEEB02-L000001](../../agents/tool_execution_status.py#L1) | 1 | `"\"\"\"Truthful task-tool execution status, separate from task planning and evidence quality.\"\"\""` | — |
| [SRC-0799EEEB02-L000002](../../agents/tool_execution_status.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-0799EEEB02-L000003](../../agents/tool_execution_status.py#L3) | 3 | `""` | — |
| [SRC-0799EEEB02-L000004](../../agents/tool_execution_status.py#L4) | 4 | `"from typing import Any"` | — |
| [SRC-0799EEEB02-L000005](../../agents/tool_execution_status.py#L5) | 5 | `""` | — |
| [SRC-0799EEEB02-L000006](../../agents/tool_execution_status.py#L6) | 6 | `"_TOOL_LABELS = {"` | — |
| [SRC-0799EEEB02-L000007](../../agents/tool_execution_status.py#L7) | 7 | `"    \"web_search\": \"البحث على الويب\","` | — |
| [SRC-0799EEEB02-L000008](../../agents/tool_execution_status.py#L8) | 8 | `"    \"page_fetch\": \"فتح الصفحات وقراءة النص\","` | — |
| [SRC-0799EEEB02-L000009](../../agents/tool_execution_status.py#L9) | 9 | `"    \"public_social_search_if_configured\": \"البحث في المحتوى الاجتماعي العام\","` | — |
| [SRC-0799EEEB02-L000010](../../agents/tool_execution_status.py#L10) | 10 | `"    \"language_model_generation_if_configured\": \"توليد الإجابة بالنموذج\","` | — |
| [SRC-0799EEEB02-L000011](../../agents/tool_execution_status.py#L11) | 11 | `"    \"claim_review_if_configured\": \"مراجعة الإجابة بمساعدة النموذج\","` | — |
| [SRC-0799EEEB02-L000012](../../agents/tool_execution_status.py#L12) | 12 | `"}"` | — |
| [SRC-0799EEEB02-L000013](../../agents/tool_execution_status.py#L13) | 13 | `"_ERROR_OUTCOMES = {"` | — |
| [SRC-0799EEEB02-L000014](../../agents/tool_execution_status.py#L14) | 14 | `"    \"attempted_research_error\","` | — |
| [SRC-0799EEEB02-L000015](../../agents/tool_execution_status.py#L15) | 15 | `"    \"unknown_after_research_error\","` | — |
| [SRC-0799EEEB02-L000016](../../agents/tool_execution_status.py#L16) | 16 | `"    \"unknown_after_budget_exhaustion\","` | — |
| [SRC-0799EEEB02-L000017](../../agents/tool_execution_status.py#L17) | 17 | `"}"` | — |
| [SRC-0799EEEB02-L000018](../../agents/tool_execution_status.py#L18) | 18 | `"_SOCIAL_PLATFORMS = {"` | — |
| [SRC-0799EEEB02-L000019](../../agents/tool_execution_status.py#L19) | 19 | `"    \"reddit\", \"youtube\", \"facebook\", \"instagram\", \"x\", \"twitter\","` | — |
| [SRC-0799EEEB02-L000020](../../agents/tool_execution_status.py#L20) | 20 | `"    \"tiktok\", \"linkedin\", \"threads\", \"bluesky\","` | — |
| [SRC-0799EEEB02-L000021](../../agents/tool_execution_status.py#L21) | 21 | `"}"` | — |
| [SRC-0799EEEB02-L000022](../../agents/tool_execution_status.py#L22) | 22 | `""` | — |
| [SRC-0799EEEB02-L000023](../../agents/tool_execution_status.py#L23) | 23 | `""` | — |
| [SRC-0799EEEB02-L000024](../../agents/tool_execution_status.py#L24) | 24 | `"def _nonnegative_int(value: Any) -> int \| None:"` | — |
| [SRC-0799EEEB02-L000025](../../agents/tool_execution_status.py#L25) | 25 | `"    if isinstance(value, bool):"` | — |
| [SRC-0799EEEB02-L000026](../../agents/tool_execution_status.py#L26) | 26 | `"        return None"` | — |
| [SRC-0799EEEB02-L000027](../../agents/tool_execution_status.py#L27) | 27 | `"    if isinstance(value, int):"` | — |
| [SRC-0799EEEB02-L000028](../../agents/tool_execution_status.py#L28) | 28 | `"        return max(0, value)"` | — |
| [SRC-0799EEEB02-L000029](../../agents/tool_execution_status.py#L29) | 29 | `"    if isinstance(value, float) and value.is_integer():"` | — |
| [SRC-0799EEEB02-L000030](../../agents/tool_execution_status.py#L30) | 30 | `"        return max(0, int(value))"` | — |
| [SRC-0799EEEB02-L000031](../../agents/tool_execution_status.py#L31) | 31 | `"    return None"` | — |
| [SRC-0799EEEB02-L000032](../../agents/tool_execution_status.py#L32) | 32 | `""` | — |
| [SRC-0799EEEB02-L000033](../../agents/tool_execution_status.py#L33) | 33 | `""` | — |
| [SRC-0799EEEB02-L000034](../../agents/tool_execution_status.py#L34) | 34 | `"def _status_row("` | — |
| [SRC-0799EEEB02-L000035](../../agents/tool_execution_status.py#L35) | 35 | `"    tool: str,"` | — |
| [SRC-0799EEEB02-L000036](../../agents/tool_execution_status.py#L36) | 36 | `"    required: bool,"` | — |
| [SRC-0799EEEB02-L000037](../../agents/tool_execution_status.py#L37) | 37 | `"    status: str,"` | — |
| [SRC-0799EEEB02-L000038](../../agents/tool_execution_status.py#L38) | 38 | `"    basis: dict[str, Any],"` | — |
| [SRC-0799EEEB02-L000039](../../agents/tool_execution_status.py#L39) | 39 | `") -> dict[str, Any]:"` | — |
| [SRC-0799EEEB02-L000040](../../agents/tool_execution_status.py#L40) | 40 | `"    return {"` | — |
| [SRC-0799EEEB02-L000041](../../agents/tool_execution_status.py#L41) | 41 | `"        \"tool\": tool,"` | — |
| [SRC-0799EEEB02-L000042](../../agents/tool_execution_status.py#L42) | 42 | `"        \"label_ar\": _TOOL_LABELS[tool],"` | — |
| [SRC-0799EEEB02-L000043](../../agents/tool_execution_status.py#L43) | 43 | `"        \"required_by_task_spec\": required,"` | — |
| [SRC-0799EEEB02-L000044](../../agents/tool_execution_status.py#L44) | 44 | `"        \"status\": status,"` | — |
| [SRC-0799EEEB02-L000045](../../agents/tool_execution_status.py#L45) | 45 | `"        \"basis\": basis,"` | — |
| [SRC-0799EEEB02-L000046](../../agents/tool_execution_status.py#L46) | 46 | `"        \"semantics\": ("` | — |
| [SRC-0799EEEB02-L000047](../../agents/tool_execution_status.py#L47) | 47 | `"            \"حالة مسار التنفيذ المرصودة فقط؛ لا تثبت صحة المحتوى أو كفاية الدليل.\""` | — |
| [SRC-0799EEEB02-L000048](../../agents/tool_execution_status.py#L48) | 48 | `"        ),"` | — |
| [SRC-0799EEEB02-L000049](../../agents/tool_execution_status.py#L49) | 49 | `"    }"` | — |
| [SRC-0799EEEB02-L000050](../../agents/tool_execution_status.py#L50) | 50 | `""` | — |
| [SRC-0799EEEB02-L000051](../../agents/tool_execution_status.py#L51) | 51 | `""` | — |
| [SRC-0799EEEB02-L000052](../../agents/tool_execution_status.py#L52) | 52 | `"def build_tool_execution_matrix("` | — |
| [SRC-0799EEEB02-L000053](../../agents/tool_execution_status.py#L53) | 53 | `"    task_spec: dict[str, Any] \| None,"` | — |
| [SRC-0799EEEB02-L000054](../../agents/tool_execution_status.py#L54) | 54 | `"    result: dict[str, Any] \| None,"` | — |
| [SRC-0799EEEB02-L000055](../../agents/tool_execution_status.py#L55) | 55 | `"    report: dict[str, Any] \| None,"` | — |
| [SRC-0799EEEB02-L000056](../../agents/tool_execution_status.py#L56) | 56 | `") -> list[dict[str, Any]]:"` | — |
| [SRC-0799EEEB02-L000057](../../agents/tool_execution_status.py#L57) | 57 | `"    \"\"\"Map planned tool requirements to observed outcomes without inferring success.\"\"\""` | — |
| [SRC-0799EEEB02-L000058](../../agents/tool_execution_status.py#L58) | 58 | `"    spec = task_spec if isinstance(task_spec, dict) else {}"` | — |
| [SRC-0799EEEB02-L000059](../../agents/tool_execution_status.py#L59) | 59 | `"    output = result if isinstance(result, dict) else {}"` | — |
| [SRC-0799EEEB02-L000060](../../agents/tool_execution_status.py#L60) | 60 | `"    search_report = report if isinstance(report, dict) else {}"` | — |
| [SRC-0799EEEB02-L000061](../../agents/tool_execution_status.py#L61) | 61 | `"    requirements = spec.get(\"tool_requirements\")"` | — |
| [SRC-0799EEEB02-L000062](../../agents/tool_execution_status.py#L62) | 62 | `"    required = {"` | — |
| [SRC-0799EEEB02-L000063](../../agents/tool_execution_status.py#L63) | 63 | `"        item for item in requirements"` | — |
