# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **012**
- سجلات الأسطر: **800**
- النطاق: SRC-E599346ABE-L001292 إلى SRC-21D5D044E2-L000031
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-E599346ABE — [docs/generate_index.py](../generate_index.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E599346ABE-L001292](../generate_index.py#L1292) | 1292 | `"                        line_id=source_line.line_id,"` | — |
| [SRC-E599346ABE-L001293](../generate_index.py#L1293) | 1293 | `"                        marker=marker,"` | — |
| [SRC-E599346ABE-L001294](../generate_index.py#L1294) | 1294 | `"                        description=description,"` | — |
| [SRC-E599346ABE-L001295](../generate_index.py#L1295) | 1295 | `"                    )"` | — |
| [SRC-E599346ABE-L001296](../generate_index.py#L1296) | 1296 | `"                )"` | — |
| [SRC-E599346ABE-L001297](../generate_index.py#L1297) | 1297 | `"    findings.sort("` | — |
| [SRC-E599346ABE-L001298](../generate_index.py#L1298) | 1298 | `"        key=lambda item: (item.marker, item.file.casefold(), item.line_id, item.finding_id)"` | — |
| [SRC-E599346ABE-L001299](../generate_index.py#L1299) | 1299 | `"    )"` | — |
| [SRC-E599346ABE-L001300](../generate_index.py#L1300) | 1300 | `"    return findings"` | — |
| [SRC-E599346ABE-L001301](../generate_index.py#L1301) | 1301 | `""` | — |
| [SRC-E599346ABE-L001302](../generate_index.py#L1302) | 1302 | `""` | — |
| [SRC-E599346ABE-L001303](../generate_index.py#L1303) | 1303 | `"def _markdown_code_span(value: str) -> str:"` | — |
| [SRC-E599346ABE-L001304](../generate_index.py#L1304) | 1304 | `"    \"\"\"Render a Markdown inline-code span safely, including backticks in source text.\"\"\""` | — |
| [SRC-E599346ABE-L001305](../generate_index.py#L1305) | 1305 | `"    tick = chr(96)"` | — |
| [SRC-E599346ABE-L001306](../generate_index.py#L1306) | 1306 | `"    longest = max("` | — |
| [SRC-E599346ABE-L001307](../generate_index.py#L1307) | 1307 | `"        (len(match.group(0)) for match in re.finditer(r\"\\u0060+\", value)),"` | — |
| [SRC-E599346ABE-L001308](../generate_index.py#L1308) | 1308 | `"        default=0,"` | — |
| [SRC-E599346ABE-L001309](../generate_index.py#L1309) | 1309 | `"    )"` | — |
| [SRC-E599346ABE-L001310](../generate_index.py#L1310) | 1310 | `"    fence = tick * (longest + 1)"` | — |
| [SRC-E599346ABE-L001311](../generate_index.py#L1311) | 1311 | `"    content = f\" {value} \" if value.startswith(tick) or value.endswith(tick) else value"` | — |
| [SRC-E599346ABE-L001312](../generate_index.py#L1312) | 1312 | `"    return f\"{fence}{content}{fence}\""` | — |
| [SRC-E599346ABE-L001313](../generate_index.py#L1313) | 1313 | `""` | — |
| [SRC-E599346ABE-L001314](../generate_index.py#L1314) | 1314 | `""` | — |
| [SRC-E599346ABE-L001315](../generate_index.py#L1315) | 1315 | `"def render_source_line_pages("` | — |
| [SRC-E599346ABE-L001316](../generate_index.py#L1316) | 1316 | `"    source_lines: list[IndexedLine],"` | — |
| [SRC-E599346ABE-L001317](../generate_index.py#L1317) | 1317 | `"    inventory: list[IndexedFile],"` | — |
| [SRC-E599346ABE-L001318](../generate_index.py#L1318) | 1318 | `"    findings: list[IndexedFinding],"` | — |
| [SRC-E599346ABE-L001319](../generate_index.py#L1319) | 1319 | `") -> tuple[dict[str, str], dict[str, list[str]]]:"` | — |
| [SRC-E599346ABE-L001320](../generate_index.py#L1320) | 1320 | `"    \"\"\"Split line-level records into deterministic small pages and map each file to its pages.\"\"\""` | — |
| [SRC-E599346ABE-L001321](../generate_index.py#L1321) | 1321 | `"    pages: dict[str, str] = {}"` | — |
| [SRC-E599346ABE-L001322](../generate_index.py#L1322) | 1322 | `"    pages_by_file: dict[str, list[str]] = {}"` | — |
| [SRC-E599346ABE-L001323](../generate_index.py#L1323) | 1323 | `"    inventory_by_path = {item.file: item for item in inventory}"` | — |
| [SRC-E599346ABE-L001324](../generate_index.py#L1324) | 1324 | `"    findings_by_line: dict[str, list[IndexedFinding]] = {}"` | — |
| [SRC-E599346ABE-L001325](../generate_index.py#L1325) | 1325 | `"    for finding in findings:"` | — |
| [SRC-E599346ABE-L001326](../generate_index.py#L1326) | 1326 | `"        findings_by_line.setdefault(finding.line_id, []).append(finding)"` | — |
| [SRC-E599346ABE-L001327](../generate_index.py#L1327) | 1327 | `""` | — |
| [SRC-E599346ABE-L001328](../generate_index.py#L1328) | 1328 | `"    for page_number, start in enumerate("` | — |
| [SRC-E599346ABE-L001329](../generate_index.py#L1329) | 1329 | `"        range(0, len(source_lines), SOURCE_LINES_PAGE_SIZE),"` | — |
| [SRC-E599346ABE-L001330](../generate_index.py#L1330) | 1330 | `"        start=1,"` | — |
| [SRC-E599346ABE-L001331](../generate_index.py#L1331) | 1331 | `"    ):"` | — |
| [SRC-E599346ABE-L001332](../generate_index.py#L1332) | 1332 | `"        chunk = source_lines[start : start + SOURCE_LINES_PAGE_SIZE]"` | — |
| [SRC-E599346ABE-L001333](../generate_index.py#L1333) | 1333 | `"        page_path = f\"{SOURCE_LINES_PAGES_DIR}/SOURCE_LINES_{page_number:03d}.md\""` | — |
| [SRC-E599346ABE-L001334](../generate_index.py#L1334) | 1334 | `"        lines = ["` | — |
| [SRC-E599346ABE-L001335](../generate_index.py#L1335) | 1335 | `"            \"# Omarai Source Lines\","` | — |
| [SRC-E599346ABE-L001336](../generate_index.py#L1336) | 1336 | `"            \"\","` | — |
| [SRC-E599346ABE-L001337](../generate_index.py#L1337) | 1337 | `"            \"<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001338](../generate_index.py#L1338) | 1338 | `"            \"\","` | — |
| [SRC-E599346ABE-L001339](../generate_index.py#L1339) | 1339 | `"            f\"- الصفحة: **{page_number:03d}**\","` | — |
| [SRC-E599346ABE-L001340](../generate_index.py#L1340) | 1340 | `"            f\"- سجلات الأسطر: **{len(chunk)}**\","` | — |
| [SRC-E599346ABE-L001341](../generate_index.py#L1341) | 1341 | `"            f\"- النطاق: {chunk[0].line_id} إلى {chunk[-1].line_id}\","` | — |
| [SRC-E599346ABE-L001342](../generate_index.py#L1342) | 1342 | `"            \"- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)\","` | — |
| [SRC-E599346ABE-L001343](../generate_index.py#L1343) | 1343 | `"            \"\","` | — |
| [SRC-E599346ABE-L001344](../generate_index.py#L1344) | 1344 | `"        ]"` | — |
| [SRC-E599346ABE-L001345](../generate_index.py#L1345) | 1345 | `"        current_file: str \| None = None"` | — |
| [SRC-E599346ABE-L001346](../generate_index.py#L1346) | 1346 | `"        for source_line in chunk:"` | — |
| [SRC-E599346ABE-L001347](../generate_index.py#L1347) | 1347 | `"            item = inventory_by_path[source_line.file]"` | — |
| [SRC-E599346ABE-L001348](../generate_index.py#L1348) | 1348 | `"            if source_line.file != current_file:"` | — |
| [SRC-E599346ABE-L001349](../generate_index.py#L1349) | 1349 | `"                current_file = source_line.file"` | — |
| [SRC-E599346ABE-L001350](../generate_index.py#L1350) | 1350 | `"                lines.extend("` | — |
| [SRC-E599346ABE-L001351](../generate_index.py#L1351) | 1351 | `"                    ["` | — |
| [SRC-E599346ABE-L001352](../generate_index.py#L1352) | 1352 | `"                        f\"## {item.category}\","` | — |
| [SRC-E599346ABE-L001353](../generate_index.py#L1353) | 1353 | `"                        \"\","` | — |
| [SRC-E599346ABE-L001354](../generate_index.py#L1354) | 1354 | `"                        f\"### {item.file_id} — [{_markdown_cell(item.file)}]({_source_file_href(item.file, index_directory=SOURCE_LINES_PAGES_DIR)})\","` | — |
| [SRC-E599346ABE-L001355](../generate_index.py#L1355) | 1355 | `"                        \"\","` | — |
| [SRC-E599346ABE-L001356](../generate_index.py#L1356) | 1356 | `"                        f\"- النوع: **{item.file_type}**\","` | — |
| [SRC-E599346ABE-L001357](../generate_index.py#L1357) | 1357 | `"                        f\"- نطاق الفهرسة: {_markdown_cell(item.indexing_scope)}\","` | — |
| [SRC-E599346ABE-L001358](../generate_index.py#L1358) | 1358 | `"                        \"\","` | — |
| [SRC-E599346ABE-L001359](../generate_index.py#L1359) | 1359 | `"                        \"\| كود السطر \| السطر \| النص الكامل للسطر \| كود الوسم \|\","` | — |
| [SRC-E599346ABE-L001360](../generate_index.py#L1360) | 1360 | `"                        \"\|---\|---:\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001361](../generate_index.py#L1361) | 1361 | `"                    ]"` | — |
| [SRC-E599346ABE-L001362](../generate_index.py#L1362) | 1362 | `"                )"` | — |
| [SRC-E599346ABE-L001363](../generate_index.py#L1363) | 1363 | `"            line_findings = findings_by_line.get(source_line.line_id, [])"` | — |
| [SRC-E599346ABE-L001364](../generate_index.py#L1364) | 1364 | `"            finding_code = \", \".join(item.finding_id for item in line_findings) or \"—\""` | — |
| [SRC-E599346ABE-L001365](../generate_index.py#L1365) | 1365 | `"            exact_text = json.dumps(source_line.content, ensure_ascii=False)"` | — |
| [SRC-E599346ABE-L001366](../generate_index.py#L1366) | 1366 | `"            escaped_text = exact_text.replace(\"\|\", r\"\\\|\")"` | — |
| [SRC-E599346ABE-L001367](../generate_index.py#L1367) | 1367 | `"            href = _source_file_href("` | — |
| [SRC-E599346ABE-L001368](../generate_index.py#L1368) | 1368 | `"                source_line.file,"` | — |
| [SRC-E599346ABE-L001369](../generate_index.py#L1369) | 1369 | `"                source_line.line,"` | — |
| [SRC-E599346ABE-L001370](../generate_index.py#L1370) | 1370 | `"                index_directory=SOURCE_LINES_PAGES_DIR,"` | — |
| [SRC-E599346ABE-L001371](../generate_index.py#L1371) | 1371 | `"            )"` | — |
| [SRC-E599346ABE-L001372](../generate_index.py#L1372) | 1372 | `"            line_code = f\"[{source_line.line_id}]({href})\""` | — |
| [SRC-E599346ABE-L001373](../generate_index.py#L1373) | 1373 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001374](../generate_index.py#L1374) | 1374 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001375](../generate_index.py#L1375) | 1375 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001376](../generate_index.py#L1376) | 1376 | `"                    ("` | — |
| [SRC-E599346ABE-L001377](../generate_index.py#L1377) | 1377 | `"                        line_code,"` | — |
| [SRC-E599346ABE-L001378](../generate_index.py#L1378) | 1378 | `"                        str(source_line.line),"` | — |
| [SRC-E599346ABE-L001379](../generate_index.py#L1379) | 1379 | `"                        _markdown_code_span(escaped_text),"` | — |
| [SRC-E599346ABE-L001380](../generate_index.py#L1380) | 1380 | `"                        finding_code,"` | — |
| [SRC-E599346ABE-L001381](../generate_index.py#L1381) | 1381 | `"                    )"` | — |
| [SRC-E599346ABE-L001382](../generate_index.py#L1382) | 1382 | `"                )"` | — |
| [SRC-E599346ABE-L001383](../generate_index.py#L1383) | 1383 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001384](../generate_index.py#L1384) | 1384 | `"            )"` | — |
| [SRC-E599346ABE-L001385](../generate_index.py#L1385) | 1385 | `"            refs = pages_by_file.setdefault(source_line.file, [])"` | — |
| [SRC-E599346ABE-L001386](../generate_index.py#L1386) | 1386 | `"            if page_path not in refs:"` | — |
| [SRC-E599346ABE-L001387](../generate_index.py#L1387) | 1387 | `"                refs.append(page_path)"` | — |
| [SRC-E599346ABE-L001388](../generate_index.py#L1388) | 1388 | `"        pages[page_path] = \"\\n\".join(lines) + \"\\n\""` | — |
| [SRC-E599346ABE-L001389](../generate_index.py#L1389) | 1389 | `""` | — |
| [SRC-E599346ABE-L001390](../generate_index.py#L1390) | 1390 | `"    return pages, pages_by_file"` | — |
| [SRC-E599346ABE-L001391](../generate_index.py#L1391) | 1391 | `""` | — |
| [SRC-E599346ABE-L001392](../generate_index.py#L1392) | 1392 | `""` | — |
| [SRC-E599346ABE-L001393](../generate_index.py#L1393) | 1393 | `"def render_source_lines_markdown("` | — |
| [SRC-E599346ABE-L001394](../generate_index.py#L1394) | 1394 | `"    source_lines: list[IndexedLine],"` | — |
| [SRC-E599346ABE-L001395](../generate_index.py#L1395) | 1395 | `"    inventory: list[IndexedFile],"` | — |
| [SRC-E599346ABE-L001396](../generate_index.py#L1396) | 1396 | `"    findings: list[IndexedFinding],"` | — |
| [SRC-E599346ABE-L001397](../generate_index.py#L1397) | 1397 | `"    pages_by_file: dict[str, list[str]] \| None = None,"` | — |
| [SRC-E599346ABE-L001398](../generate_index.py#L1398) | 1398 | `"    source_pages: dict[str, str] \| None = None,"` | — |
| [SRC-E599346ABE-L001399](../generate_index.py#L1399) | 1399 | `") -> str:"` | — |
| [SRC-E599346ABE-L001400](../generate_index.py#L1400) | 1400 | `"    \"\"\"Render a compact table of contents for the sharded full source-line index.\"\"\""` | — |
| [SRC-E599346ABE-L001401](../generate_index.py#L1401) | 1401 | `"    assigned_pages = pages_by_file or {}"` | — |
| [SRC-E599346ABE-L001402](../generate_index.py#L1402) | 1402 | `"    rendered_pages = source_pages or {}"` | — |
| [SRC-E599346ABE-L001403](../generate_index.py#L1403) | 1403 | `"    files_with_lines = sum(item.line_count is not None for item in inventory)"` | — |
| [SRC-E599346ABE-L001404](../generate_index.py#L1404) | 1404 | `"    lines = ["` | — |
| [SRC-E599346ABE-L001405](../generate_index.py#L1405) | 1405 | `"        \"# SOURCE LINES INDEX — Omarai\","` | — |
| [SRC-E599346ABE-L001406](../generate_index.py#L1406) | 1406 | `"        \"\","` | — |
| [SRC-E599346ABE-L001407](../generate_index.py#L1407) | 1407 | `"        \"<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001408](../generate_index.py#L1408) | 1408 | `"        \"\","` | — |
| [SRC-E599346ABE-L001409](../generate_index.py#L1409) | 1409 | `"        \"> هذا دليل الوصول إلى فهرس الأسطر الكامل. يحتوي كل سطر في الملفات النصية المؤهلة على كود SRC- ورقم السطر ونص السطر كاملًا.\","` | — |
| [SRC-E599346ABE-L001410](../generate_index.py#L1410) | 1410 | `"        \"> قُسّم المحتوى إلى صفحات صغيرة حتى تظل كل صفحة قابلة للفتح والبحث بسرعة من الهاتف والمتصفح.\","` | — |
| [SRC-E599346ABE-L001411](../generate_index.py#L1411) | 1411 | `"        \"> ابدأ من [MASTER INDEX](MASTER_INDEX.md) للعثور حسب اسم الملف أو الدالة أو الكلاس أو وسم المراجعة.\","` | — |
| [SRC-E599346ABE-L001412](../generate_index.py#L1412) | 1412 | `"        \"> راجع [INDEX COVERAGE AUDIT](INDEX_COVERAGE_AUDIT.md) للاطلاع على نسبة التغطية وأسباب الاستبعاد.\","` | — |
| [SRC-E599346ABE-L001413](../generate_index.py#L1413) | 1413 | `"        \"\","` | — |
| [SRC-E599346ABE-L001414](../generate_index.py#L1414) | 1414 | `"        \"## ملخص التغطية\","` | — |
| [SRC-E599346ABE-L001415](../generate_index.py#L1415) | 1415 | `"        \"\","` | — |
| [SRC-E599346ABE-L001416](../generate_index.py#L1416) | 1416 | `"        f\"- الملفات في جرد المستودع: **{len(inventory)}**\","` | — |
| [SRC-E599346ABE-L001417](../generate_index.py#L1417) | 1417 | `"        f\"- الملفات النصية المفهرسة سطرًا بسطر: **{files_with_lines}**\","` | — |
| [SRC-E599346ABE-L001418](../generate_index.py#L1418) | 1418 | `"        f\"- الأسطر المفهرسة: **{len(source_lines)}**\","` | — |
| [SRC-E599346ABE-L001419](../generate_index.py#L1419) | 1419 | `"        f\"- وسوم المراجعة/الإصلاح المسجلة: **{len(findings)}**\","` | — |
| [SRC-E599346ABE-L001420](../generate_index.py#L1420) | 1420 | `"        f\"- صفحات الأسطر: **{len(rendered_pages)}**\","` | — |
| [SRC-E599346ABE-L001421](../generate_index.py#L1421) | 1421 | `"        \"\","` | — |
| [SRC-E599346ABE-L001422](../generate_index.py#L1422) | 1422 | `"        \"## صفحات الأسطر\","` | — |
| [SRC-E599346ABE-L001423](../generate_index.py#L1423) | 1423 | `"        \"\","` | — |
| [SRC-E599346ABE-L001424](../generate_index.py#L1424) | 1424 | `"        \"\| الصفحة \| عدد السجلات \| من كود \| إلى كود \|\","` | — |
| [SRC-E599346ABE-L001425](../generate_index.py#L1425) | 1425 | `"        \"\|---\|---:\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001426](../generate_index.py#L1426) | 1426 | `"    ]"` | — |
| [SRC-E599346ABE-L001427](../generate_index.py#L1427) | 1427 | `"    for page_path, page_content in rendered_pages.items():"` | — |
| [SRC-E599346ABE-L001428](../generate_index.py#L1428) | 1428 | `"        count = sum(1 for line in page_content.splitlines() if line.startswith(\"\| [SRC-\"))"` | — |
| [SRC-E599346ABE-L001429](../generate_index.py#L1429) | 1429 | `"        ids = re.findall(r\"\\bSRC-[A-F0-9]+-L\\d{6}\\b\", page_content)"` | — |
| [SRC-E599346ABE-L001430](../generate_index.py#L1430) | 1430 | `"        label = Path(page_path).stem"` | — |
| [SRC-E599346ABE-L001431](../generate_index.py#L1431) | 1431 | `"        lines.append("` | — |
| [SRC-E599346ABE-L001432](../generate_index.py#L1432) | 1432 | `"            f\"\| [{label}]({Path(page_path).relative_to('docs').as_posix()}) \| \""` | — |
| [SRC-E599346ABE-L001433](../generate_index.py#L1433) | 1433 | `"            f\"{count} \| {ids[0] if ids else '—'} \| {ids[-1] if ids else '—'} \|\""` | — |
| [SRC-E599346ABE-L001434](../generate_index.py#L1434) | 1434 | `"        )"` | — |
| [SRC-E599346ABE-L001435](../generate_index.py#L1435) | 1435 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001436](../generate_index.py#L1436) | 1436 | `"        ["` | — |
| [SRC-E599346ABE-L001437](../generate_index.py#L1437) | 1437 | `"            \"\","` | — |
| [SRC-E599346ABE-L001438](../generate_index.py#L1438) | 1438 | `"            \"## جرد الملفات والوصول حسب الاسم\","` | — |
| [SRC-E599346ABE-L001439](../generate_index.py#L1439) | 1439 | `"            \"\","` | — |
| [SRC-E599346ABE-L001440](../generate_index.py#L1440) | 1440 | `"            \"\| معرّف الملف \| التصنيف \| الملف \| الأسطر \| صفحات الفهرسة \|\","` | — |
| [SRC-E599346ABE-L001441](../generate_index.py#L1441) | 1441 | `"            \"\|---\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001442](../generate_index.py#L1442) | 1442 | `"        ]"` | — |
| [SRC-E599346ABE-L001443](../generate_index.py#L1443) | 1443 | `"    )"` | — |
| [SRC-E599346ABE-L001444](../generate_index.py#L1444) | 1444 | `"    for item in sorted(inventory, key=lambda entry: (entry.category, entry.file.casefold())):"` | — |
| [SRC-E599346ABE-L001445](../generate_index.py#L1445) | 1445 | `"        if item.line_count is None:"` | — |
| [SRC-E599346ABE-L001446](../generate_index.py#L1446) | 1446 | `"            line_count = \"بيانات وصفية فقط\""` | — |
| [SRC-E599346ABE-L001447](../generate_index.py#L1447) | 1447 | `"        else:"` | — |
| [SRC-E599346ABE-L001448](../generate_index.py#L1448) | 1448 | `"            line_count = str(item.line_count)"` | — |
| [SRC-E599346ABE-L001449](../generate_index.py#L1449) | 1449 | `"        page_links = assigned_pages.get(item.file, [])"` | — |
| [SRC-E599346ABE-L001450](../generate_index.py#L1450) | 1450 | `"        if page_links:"` | — |
| [SRC-E599346ABE-L001451](../generate_index.py#L1451) | 1451 | `"            link_text = \", \".join("` | — |
| [SRC-E599346ABE-L001452](../generate_index.py#L1452) | 1452 | `"                f\"[{Path(page_path).stem}]({Path(page_path).relative_to('docs').as_posix()})\""` | — |
| [SRC-E599346ABE-L001453](../generate_index.py#L1453) | 1453 | `"                for page_path in page_links"` | — |
| [SRC-E599346ABE-L001454](../generate_index.py#L1454) | 1454 | `"            )"` | — |
| [SRC-E599346ABE-L001455](../generate_index.py#L1455) | 1455 | `"        elif item.line_count == 0:"` | — |
| [SRC-E599346ABE-L001456](../generate_index.py#L1456) | 1456 | `"            link_text = \"ملف نصي فارغ\""` | — |
| [SRC-E599346ABE-L001457](../generate_index.py#L1457) | 1457 | `"        elif item.line_count is None:"` | — |
| [SRC-E599346ABE-L001458](../generate_index.py#L1458) | 1458 | `"            link_text = \"غير مفهرس سطرًا بسطر\""` | — |
| [SRC-E599346ABE-L001459](../generate_index.py#L1459) | 1459 | `"        else:"` | — |
| [SRC-E599346ABE-L001460](../generate_index.py#L1460) | 1460 | `"            link_text = \"لا توجد سجلات\""` | — |
| [SRC-E599346ABE-L001461](../generate_index.py#L1461) | 1461 | `"        target = _source_file_href(item.file, index_directory=\"docs\")"` | — |
| [SRC-E599346ABE-L001462](../generate_index.py#L1462) | 1462 | `"        lines.append("` | — |
| [SRC-E599346ABE-L001463](../generate_index.py#L1463) | 1463 | `"            f\"\| {item.file_id} \| {_markdown_cell(item.category)} \| \""` | — |
| [SRC-E599346ABE-L001464](../generate_index.py#L1464) | 1464 | `"            f\"[{_markdown_cell(item.file)}]({target}) \| {line_count} \| {link_text} \|\""` | — |
| [SRC-E599346ABE-L001465](../generate_index.py#L1465) | 1465 | `"        )"` | — |
| [SRC-E599346ABE-L001466](../generate_index.py#L1466) | 1466 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001467](../generate_index.py#L1467) | 1467 | `"        ["` | — |
| [SRC-E599346ABE-L001468](../generate_index.py#L1468) | 1468 | `"            \"\","` | — |
| [SRC-E599346ABE-L001469](../generate_index.py#L1469) | 1469 | `"            \"## سجل وسوم المراجعة والإصلاح\","` | — |
| [SRC-E599346ABE-L001470](../generate_index.py#L1470) | 1470 | `"            \"\","` | — |
| [SRC-E599346ABE-L001471](../generate_index.py#L1471) | 1471 | `"            \"كل كود FND- في MASTER INDEX يحدد وسمًا صريحًا ويشير إلى كود السطر في إحدى صفحات هذا الفهرس.\","` | — |
| [SRC-E599346ABE-L001472](../generate_index.py#L1472) | 1472 | `"            \"الوسوم المعروفة: TODO وFIXME وBUG وHACK وXXX وREVIEW وSECURITY وDEPRECATED وISSUE وDEFECT وREGRESSION وRISK وGAP وERROR وWARNING وPERF وPRIVACY وDATA_LOSS وACCESSIBILITY.\","` | — |
| [SRC-E599346ABE-L001473](../generate_index.py#L1473) | 1473 | `"            \"\","` | — |
| [SRC-E599346ABE-L001474](../generate_index.py#L1474) | 1474 | `"            \"## الاستثناءات وحدود التغطية\","` | — |
| [SRC-E599346ABE-L001475](../generate_index.py#L1475) | 1475 | `"            \"\","` | — |
| [SRC-E599346ABE-L001476](../generate_index.py#L1476) | 1476 | `"            \"- ملفات الفهرسة المولّدة نفسها مستثناة لمنع الحلقة الذاتية.\","` | — |
| [SRC-E599346ABE-L001477](../generate_index.py#L1477) | 1477 | `"            \"- تُفهرس سطور كل ملف نصي قابل للقراءة وحجمه حتى 2 MiB؛ الملفات الثنائية أو الأكبر أو غير القابلة للقراءة تظهر في جرد الملفات فقط.\","` | — |
| [SRC-E599346ABE-L001478](../generate_index.py#L1478) | 1478 | `"            \"- الملفات الحساسة المعروفة وقواعد البيانات والبيئات المحلية ومجلدات البناء والاعتماديات مستثناة عمدًا.\","` | — |
| [SRC-E599346ABE-L001479](../generate_index.py#L1479) | 1479 | `"            \"- أكواد الأسطر مشتقة من مسار الملف ورقم السطر؛ يتغير رقم الكود عند تحرك السطر بسبب تغييرات سابقة في الملف.\","` | — |
| [SRC-E599346ABE-L001480](../generate_index.py#L1480) | 1480 | `"            \"- وسوم المراجعة ليست تشخيصًا آليًا لكل عيب منطقي؛ الفهرس يسهل العثور على الكود لكنه لا يستطيع إثبات خلوه من الأخطاء.\","` | — |
| [SRC-E599346ABE-L001481](../generate_index.py#L1481) | 1481 | `"            \"\","` | — |
| [SRC-E599346ABE-L001482](../generate_index.py#L1482) | 1482 | `"        ]"` | — |
| [SRC-E599346ABE-L001483](../generate_index.py#L1483) | 1483 | `"    )"` | — |
| [SRC-E599346ABE-L001484](../generate_index.py#L1484) | 1484 | `"    return \"\\n\".join(lines) + \"\\n\""` | — |
| [SRC-E599346ABE-L001485](../generate_index.py#L1485) | 1485 | `""` | — |
| [SRC-E599346ABE-L001486](../generate_index.py#L1486) | 1486 | `""` | — |
| [SRC-E599346ABE-L001487](../generate_index.py#L1487) | 1487 | `"def render_coverage_audit_markdown("` | — |
| [SRC-E599346ABE-L001488](../generate_index.py#L1488) | 1488 | `"    root: Path,"` | — |
| [SRC-E599346ABE-L001489](../generate_index.py#L1489) | 1489 | `"    inventory: list[IndexedFile],"` | — |
| [SRC-E599346ABE-L001490](../generate_index.py#L1490) | 1490 | `"    source_lines: list[IndexedLine],"` | — |
| [SRC-E599346ABE-L001491](../generate_index.py#L1491) | 1491 | `"    excluded_paths: list[tuple[str, str]],"` | — |
| [SRC-E599346ABE-L001492](../generate_index.py#L1492) | 1492 | `") -> str:"` | — |
| [SRC-E599346ABE-L001493](../generate_index.py#L1493) | 1493 | `"    \"\"\"Render a generated coverage ledger with exact line-index coverage and exclusions.\"\"\""` | — |
| [SRC-E599346ABE-L001494](../generate_index.py#L1494) | 1494 | `"    indexed_files = [item for item in inventory if item.line_count is not None]"` | — |
| [SRC-E599346ABE-L001495](../generate_index.py#L1495) | 1495 | `"    metadata_only = [item for item in inventory if item.line_count is None]"` | — |
| [SRC-E599346ABE-L001496](../generate_index.py#L1496) | 1496 | `"    expected_line_count = sum(item.line_count or 0 for item in indexed_files)"` | — |
| [SRC-E599346ABE-L001497](../generate_index.py#L1497) | 1497 | `"    actual_line_count = len(source_lines)"` | — |
| [SRC-E599346ABE-L001498](../generate_index.py#L1498) | 1498 | `"    coverage_ok = expected_line_count == actual_line_count"` | — |
| [SRC-E599346ABE-L001499](../generate_index.py#L1499) | 1499 | `"    lines = ["` | — |
| [SRC-E599346ABE-L001500](../generate_index.py#L1500) | 1500 | `"        \"# OMARAI INDEX COVERAGE AUDIT\","` | — |
| [SRC-E599346ABE-L001501](../generate_index.py#L1501) | 1501 | `"        \"\","` | — |
| [SRC-E599346ABE-L001502](../generate_index.py#L1502) | 1502 | `"        \"<!-- هذا الملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001503](../generate_index.py#L1503) | 1503 | `"        \"\","` | — |
| [SRC-E599346ABE-L001504](../generate_index.py#L1504) | 1504 | `"        \"> سجل أدلة تغطية الفهرس وحدوده، وليس ادعاءً باكتشاف كل عيب منطقي في البرنامج.\","` | — |
| [SRC-E599346ABE-L001505](../generate_index.py#L1505) | 1505 | `"        \"\","` | — |
| [SRC-E599346ABE-L001506](../generate_index.py#L1506) | 1506 | `"        \"## نتيجة تغطية السطور\","` | — |
| [SRC-E599346ABE-L001507](../generate_index.py#L1507) | 1507 | `"        \"\","` | — |
| [SRC-E599346ABE-L001508](../generate_index.py#L1508) | 1508 | `"        f\"- ملفات المستودع المؤهلة في الجرد: **{len(inventory)}**\","` | — |
| [SRC-E599346ABE-L001509](../generate_index.py#L1509) | 1509 | `"        f\"- الملفات المفهرسة سطرًا بسطر: **{len(indexed_files)}**\","` | — |
| [SRC-E599346ABE-L001510](../generate_index.py#L1510) | 1510 | `"        f\"- الملفات الوصفية فقط التي لا تتوفر سطورها: **{len(metadata_only)}**\","` | — |
| [SRC-E599346ABE-L001511](../generate_index.py#L1511) | 1511 | `"        f\"- السطور المتوقع فهرستها من عدادات الملفات: **{expected_line_count}**\","` | — |
| [SRC-E599346ABE-L001512](../generate_index.py#L1512) | 1512 | `"        f\"- سجلات السطور الفعلية: **{actual_line_count}**\","` | — |
| [SRC-E599346ABE-L001513](../generate_index.py#L1513) | 1513 | `"        f\"- تحقق العدد الإجمالي: **{'PASS' if coverage_ok else 'FAIL'}**\","` | — |
| [SRC-E599346ABE-L001514](../generate_index.py#L1514) | 1514 | `"        f\"- نسبة التغطية الحسابية ضمن الملفات المؤهلة القابلة للقراءة: **{(100.0 if coverage_ok and expected_line_count == actual_line_count else (actual_line_count / expected_line_count * 100 if expected_line_count else 100.0)):.2f}%**\","` | — |
| [SRC-E599346ABE-L001515](../generate_index.py#L1515) | 1515 | `"        \"\","` | — |
| [SRC-E599346ABE-L001516](../generate_index.py#L1516) | 1516 | `"        \"يتحقق المولد كذلك من أن أرقام السطور متتابعة لكل ملف ومن عدم تكرار معرّفات SRC؛ أي فشل يمنع نشر الفهرس.\","` | — |
| [SRC-E599346ABE-L001517](../generate_index.py#L1517) | 1517 | `"        \"\","` | — |
| [SRC-E599346ABE-L001518](../generate_index.py#L1518) | 1518 | `"        \"## الملفات التي لا تُفهرس سطورها\","` | — |
| [SRC-E599346ABE-L001519](../generate_index.py#L1519) | 1519 | `"        \"\","` | — |
| [SRC-E599346ABE-L001520](../generate_index.py#L1520) | 1520 | `"        \"هذه الملفات تظل ظاهرة في جرد MASTER INDEX مع سبب الاستثناء. لا يُدرج التقرير محتوياتها.\","` | — |
| [SRC-E599346ABE-L001521](../generate_index.py#L1521) | 1521 | `"        \"\","` | — |
| [SRC-E599346ABE-L001522](../generate_index.py#L1522) | 1522 | `"        \"\| معرّف الملف \| المسار \| الحجم بالبايت \| السبب \|\","` | — |
| [SRC-E599346ABE-L001523](../generate_index.py#L1523) | 1523 | `"        \"\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001524](../generate_index.py#L1524) | 1524 | `"    ]"` | — |
| [SRC-E599346ABE-L001525](../generate_index.py#L1525) | 1525 | `""` | — |
| [SRC-E599346ABE-L001526](../generate_index.py#L1526) | 1526 | `"    if metadata_only:"` | — |
| [SRC-E599346ABE-L001527](../generate_index.py#L1527) | 1527 | `"        for item in metadata_only:"` | — |
| [SRC-E599346ABE-L001528](../generate_index.py#L1528) | 1528 | `"            reason = _text_index_skip_reason(root / item.file)"` | — |
| [SRC-E599346ABE-L001529](../generate_index.py#L1529) | 1529 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001530](../generate_index.py#L1530) | 1530 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001531](../generate_index.py#L1531) | 1531 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001532](../generate_index.py#L1532) | 1532 | `"                    ("` | — |
| [SRC-E599346ABE-L001533](../generate_index.py#L1533) | 1533 | `"                        item.file_id,"` | — |
| [SRC-E599346ABE-L001534](../generate_index.py#L1534) | 1534 | `"                        _markdown_code_span(item.file),"` | — |
| [SRC-E599346ABE-L001535](../generate_index.py#L1535) | 1535 | `"                        str(item.size_bytes),"` | — |
| [SRC-E599346ABE-L001536](../generate_index.py#L1536) | 1536 | `"                        _markdown_cell(reason),"` | — |
| [SRC-E599346ABE-L001537](../generate_index.py#L1537) | 1537 | `"                    )"` | — |
| [SRC-E599346ABE-L001538](../generate_index.py#L1538) | 1538 | `"                )"` | — |
| [SRC-E599346ABE-L001539](../generate_index.py#L1539) | 1539 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001540](../generate_index.py#L1540) | 1540 | `"            )"` | — |
| [SRC-E599346ABE-L001541](../generate_index.py#L1541) | 1541 | `"    else:"` | — |
| [SRC-E599346ABE-L001542](../generate_index.py#L1542) | 1542 | `"        lines.append(\"\| — \| — \| — \| لا توجد ملفات مؤهلة بالجرد الوصفي فقط. \|\")"` | — |
| [SRC-E599346ABE-L001543](../generate_index.py#L1543) | 1543 | `""` | — |
| [SRC-E599346ABE-L001544](../generate_index.py#L1544) | 1544 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001545](../generate_index.py#L1545) | 1545 | `"        ["` | — |
| [SRC-E599346ABE-L001546](../generate_index.py#L1546) | 1546 | `"            \"\","` | — |
| [SRC-E599346ABE-L001547](../generate_index.py#L1547) | 1547 | `"            \"## المسارات المستبعدة عمدًا\","` | — |
| [SRC-E599346ABE-L001548](../generate_index.py#L1548) | 1548 | `"            \"\","` | — |
| [SRC-E599346ABE-L001549](../generate_index.py#L1549) | 1549 | `"            \"يحتوي هذا السجل أسماء المسارات وأسباب الاستثناء فقط، ولا يقرأ محتوى الأسرار أو قواعد البيانات أو المجلدات المستبعدة.\","` | — |
| [SRC-E599346ABE-L001550](../generate_index.py#L1550) | 1550 | `"            \"\","` | — |
| [SRC-E599346ABE-L001551](../generate_index.py#L1551) | 1551 | `"            \"\| المسار المستبعد \| السبب \|\","` | — |
| [SRC-E599346ABE-L001552](../generate_index.py#L1552) | 1552 | `"            \"\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001553](../generate_index.py#L1553) | 1553 | `"        ]"` | — |
| [SRC-E599346ABE-L001554](../generate_index.py#L1554) | 1554 | `"    )"` | — |
| [SRC-E599346ABE-L001555](../generate_index.py#L1555) | 1555 | `"    if excluded_paths:"` | — |
| [SRC-E599346ABE-L001556](../generate_index.py#L1556) | 1556 | `"        for excluded_path, reason in excluded_paths:"` | — |
| [SRC-E599346ABE-L001557](../generate_index.py#L1557) | 1557 | `"            lines.append(f\"\| {_markdown_code_span(excluded_path)} \| {_markdown_cell(reason)} \|\")"` | — |
| [SRC-E599346ABE-L001558](../generate_index.py#L1558) | 1558 | `"    else:"` | — |
| [SRC-E599346ABE-L001559](../generate_index.py#L1559) | 1559 | `"        lines.append(\"\| — \| لا توجد مسارات مستبعدة مكتشفة. \|\")"` | — |
| [SRC-E599346ABE-L001560](../generate_index.py#L1560) | 1560 | `""` | — |
| [SRC-E599346ABE-L001561](../generate_index.py#L1561) | 1561 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001562](../generate_index.py#L1562) | 1562 | `"        ["` | — |
| [SRC-E599346ABE-L001563](../generate_index.py#L1563) | 1563 | `"            \"\","` | — |
| [SRC-E599346ABE-L001564](../generate_index.py#L1564) | 1564 | `"            \"## ما تعنيه النتيجة وما لا تعنيه\","` | — |
| [SRC-E599346ABE-L001565](../generate_index.py#L1565) | 1565 | `"            \"\","` | — |
| [SRC-E599346ABE-L001566](../generate_index.py#L1566) | 1566 | `"            \"- التغطية بنسبة 100% تعني أن كل سطر منطقي في كل ملف نصي مؤهل وقابل للقراءة ضمن حد الحجم له سجل SRC فريد ورقم سطر مطابق.\","` | — |
| [SRC-E599346ABE-L001567](../generate_index.py#L1567) | 1567 | `"            \"- لا تعني أن كل مسار مستبعد أو كل ملف ثنائي/كبير مفهرس سطرًا بسطر؛ أسباب الاستبعاد مسجلة أعلاه.\","` | — |
| [SRC-E599346ABE-L001568](../generate_index.py#L1568) | 1568 | `"            \"- لا تعني اكتشاف كل عيب برمجي أو أمني أو منطقي. العيوب المعروفة التي يوسمها المطور صراحة تظهر في سجل FND داخل MASTER INDEX.\","` | — |
| [SRC-E599346ABE-L001569](../generate_index.py#L1569) | 1569 | `"            \"- الرموز غير Python مستخرجة بقواعد ساكنة تقريبية؛ استخدم فهرس السطور للوصول إلى النص الأصلي والتحقق يدويًا.\","` | — |
| [SRC-E599346ABE-L001570](../generate_index.py#L1570) | 1570 | `"            \"- المولد لا يعدّل كود التطبيق ولا يدمج الفروع؛ وظيفته بناء الأدلة والفهرس والتحقق من اتساقهما.\","` | — |
| [SRC-E599346ABE-L001571](../generate_index.py#L1571) | 1571 | `"            \"\","` | — |
| [SRC-E599346ABE-L001572](../generate_index.py#L1572) | 1572 | `"            \"[افتح MASTER INDEX](MASTER_INDEX.md) \| [افتح SOURCE LINES INDEX](SOURCE_LINES_INDEX.md)\","` | — |
| [SRC-E599346ABE-L001573](../generate_index.py#L1573) | 1573 | `"            \"\","` | — |
| [SRC-E599346ABE-L001574](../generate_index.py#L1574) | 1574 | `"        ]"` | — |
| [SRC-E599346ABE-L001575](../generate_index.py#L1575) | 1575 | `"    )"` | — |
| [SRC-E599346ABE-L001576](../generate_index.py#L1576) | 1576 | `"    return \"\\n\".join(lines)"` | — |
| [SRC-E599346ABE-L001577](../generate_index.py#L1577) | 1577 | `""` | — |
| [SRC-E599346ABE-L001578](../generate_index.py#L1578) | 1578 | `""` | — |
| [SRC-E599346ABE-L001579](../generate_index.py#L1579) | 1579 | `"def render_markdown("` | — |
| [SRC-E599346ABE-L001580](../generate_index.py#L1580) | 1580 | `"    symbols: list[IndexedSymbol],"` | — |
| [SRC-E599346ABE-L001581](../generate_index.py#L1581) | 1581 | `"    files_scanned: int,"` | — |
| [SRC-E599346ABE-L001582](../generate_index.py#L1582) | 1582 | `"    inventory: list[IndexedFile] \| None = None,"` | — |
| [SRC-E599346ABE-L001583](../generate_index.py#L1583) | 1583 | `"    static_symbols: list[IndexedMarker] \| None = None,"` | — |
| [SRC-E599346ABE-L001584](../generate_index.py#L1584) | 1584 | `"    source_lines: list[IndexedLine] \| None = None,"` | — |
| [SRC-E599346ABE-L001585](../generate_index.py#L1585) | 1585 | `"    findings: list[IndexedFinding] \| None = None,"` | — |
| [SRC-E599346ABE-L001586](../generate_index.py#L1586) | 1586 | `") -> str:"` | — |
| [SRC-E599346ABE-L001587](../generate_index.py#L1587) | 1587 | `"    \"\"\"Render the repository file, symbol, explicit-review-marker, and line-index overview.\"\"\""` | — |
| [SRC-E599346ABE-L001588](../generate_index.py#L1588) | 1588 | `"    file_inventory = inventory or []"` | — |
| [SRC-E599346ABE-L001589](../generate_index.py#L1589) | 1589 | `"    marker_inventory = static_symbols or []"` | — |
| [SRC-E599346ABE-L001590](../generate_index.py#L1590) | 1590 | `"    line_inventory = source_lines or []"` | — |
| [SRC-E599346ABE-L001591](../generate_index.py#L1591) | 1591 | `"    finding_inventory = findings or []"` | — |
| [SRC-E599346ABE-L001592](../generate_index.py#L1592) | 1592 | `"    documented_count = sum(symbol.documented is True for symbol in symbols)"` | — |
| [SRC-E599346ABE-L001593](../generate_index.py#L1593) | 1593 | `"    missing_count = sum(symbol.documented is False for symbol in symbols)"` | — |
| [SRC-E599346ABE-L001594](../generate_index.py#L1594) | 1594 | `"    not_applicable_count = sum(symbol.documented is None for symbol in symbols)"` | — |
| [SRC-E599346ABE-L001595](../generate_index.py#L1595) | 1595 | `"    lines = ["` | — |
| [SRC-E599346ABE-L001596](../generate_index.py#L1596) | 1596 | `"        \"# MASTER INDEX — Omarai\","` | — |
| [SRC-E599346ABE-L001597](../generate_index.py#L1597) | 1597 | `"        \"\","` | — |
| [SRC-E599346ABE-L001598](../generate_index.py#L1598) | 1598 | `"        \"<!-- هذا الملف مُولَّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001599](../generate_index.py#L1599) | 1599 | `"        \"\","` | — |
| [SRC-E599346ABE-L001600](../generate_index.py#L1600) | 1600 | `"        \"> MASTER INDEX يجمع جرد الملفات والتعريفات المسماة ووسوم المراجعة؛ SOURCE LINES INDEX يحتوي الأسطر الكاملة\","` | — |
| [SRC-E599346ABE-L001601](../generate_index.py#L1601) | 1601 | `"        \"> لكل ملف نصي مؤهل قابل للقراءة، مع معرّف سطر ورقم السطر الأصلي.\","` | — |
| [SRC-E599346ABE-L001602](../generate_index.py#L1602) | 1602 | `"        \"> استخراج الرموز غير Python تقريبي؛ أما فهرسة الأسطر فمخصصة للوصول إلى النص الموجود وليست حكمًا على صحته.\","` | — |
| [SRC-E599346ABE-L001603](../generate_index.py#L1603) | 1603 | `"        \"\","` | — |
| [SRC-E599346ABE-L001604](../generate_index.py#L1604) | 1604 | `"        \"## ملخص الفهرسة\","` | — |
| [SRC-E599346ABE-L001605](../generate_index.py#L1605) | 1605 | `"        \"\","` | — |
| [SRC-E599346ABE-L001606](../generate_index.py#L1606) | 1606 | `"        f\"- ملفات المستودع في الجرد: **{len(file_inventory)}**\","` | — |
| [SRC-E599346ABE-L001607](../generate_index.py#L1607) | 1607 | `"        f\"- ملفات Python المحللة: **{files_scanned}**\","` | — |
| [SRC-E599346ABE-L001608](../generate_index.py#L1608) | 1608 | `"        f\"- تعريفات Python المفهرسة: **{len(symbols)}**\","` | — |
| [SRC-E599346ABE-L001609](../generate_index.py#L1609) | 1609 | `"        f\"- تعريفات Python موثقة بوجود Docstring: **{documented_count}**\","` | — |
| [SRC-E599346ABE-L001610](../generate_index.py#L1610) | 1610 | `"        f\"- تعريفات Python بلا Docstring: **{missing_count}**\","` | — |
| [SRC-E599346ABE-L001611](../generate_index.py#L1611) | 1611 | `"        f\"- تعريفات لا ينطبق عليها Docstring: **{not_applicable_count}**\","` | — |
| [SRC-E599346ABE-L001612](../generate_index.py#L1612) | 1612 | `"        f\"- الرموز الساكنة الإضافية: **{len(marker_inventory)}**\","` | — |
| [SRC-E599346ABE-L001613](../generate_index.py#L1613) | 1613 | `"        f\"- الأسطر النصية المفهرسة حرفيًا: **{len(line_inventory)}**\","` | — |
| [SRC-E599346ABE-L001614](../generate_index.py#L1614) | 1614 | `"        f\"- وسوم المراجعة/الإصلاح المسجلة: **{len(finding_inventory)}**\","` | — |
| [SRC-E599346ABE-L001615](../generate_index.py#L1615) | 1615 | `"        \"\","` | — |
| [SRC-E599346ABE-L001616](../generate_index.py#L1616) | 1616 | `"        \"- فهرس الأسطر الكامل: [SOURCE LINES INDEX](SOURCE_LINES_INDEX.md)\","` | — |
| [SRC-E599346ABE-L001617](../generate_index.py#L1617) | 1617 | `"        \"- تدقيق التغطية والاستثناءات: [INDEX COVERAGE AUDIT](INDEX_COVERAGE_AUDIT.md)\","` | — |
| [SRC-E599346ABE-L001618](../generate_index.py#L1618) | 1618 | `"        \"- كل سجل سطر يحمل معرّفًا من الشكل SRC-<FILEHASH>-L000001.\","` | — |
| [SRC-E599346ABE-L001619](../generate_index.py#L1619) | 1619 | `"        \"\","` | — |
| [SRC-E599346ABE-L001620](../generate_index.py#L1620) | 1620 | `"        \"## جرد ملفات المستودع\","` | — |
| [SRC-E599346ABE-L001621](../generate_index.py#L1621) | 1621 | `"        \"\","` | — |
| [SRC-E599346ABE-L001622](../generate_index.py#L1622) | 1622 | `"        (\"يشمل الملفات المؤهلة من الشفرة والواجهة والاختبارات والوثائق والإعدادات وCI. \""` | — |
| [SRC-E599346ABE-L001623](../generate_index.py#L1623) | 1623 | `"        \"يُستثنى ملف الفهرس المولّد نفسه لتجنب الحلقة الذاتية، كما تُستثنى المجلدات المولّدة \""` | — |
| [SRC-E599346ABE-L001624](../generate_index.py#L1624) | 1624 | `"        \"والبيئات والملفات المحلية الحساسة وقواعد البيانات والمفاتيح المعروفة.\"),"` | — |
| [SRC-E599346ABE-L001625](../generate_index.py#L1625) | 1625 | `"        \"\","` | — |
| [SRC-E599346ABE-L001626](../generate_index.py#L1626) | 1626 | `"        \"\| معرّف الملف \| التصنيف \| الملف \| النوع \| الحجم (بايت) \| عدد الأسطر \| نطاق الفهرسة \|\","` | — |
| [SRC-E599346ABE-L001627](../generate_index.py#L1627) | 1627 | `"        \"\|---\|---\|---\|---\|---:\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001628](../generate_index.py#L1628) | 1628 | `"    ]"` | — |
| [SRC-E599346ABE-L001629](../generate_index.py#L1629) | 1629 | `""` | — |
| [SRC-E599346ABE-L001630](../generate_index.py#L1630) | 1630 | `"    if file_inventory:"` | — |
| [SRC-E599346ABE-L001631](../generate_index.py#L1631) | 1631 | `"        for item in file_inventory:"` | — |
| [SRC-E599346ABE-L001632](../generate_index.py#L1632) | 1632 | `"            line_count = str(item.line_count) if item.line_count is not None else \"غير متاح\""` | — |
| [SRC-E599346ABE-L001633](../generate_index.py#L1633) | 1633 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001634](../generate_index.py#L1634) | 1634 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001635](../generate_index.py#L1635) | 1635 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001636](../generate_index.py#L1636) | 1636 | `"                    ("` | — |
| [SRC-E599346ABE-L001637](../generate_index.py#L1637) | 1637 | `"                        item.file_id,"` | — |
| [SRC-E599346ABE-L001638](../generate_index.py#L1638) | 1638 | `"                        _markdown_cell(item.category),"` | — |
| [SRC-E599346ABE-L001639](../generate_index.py#L1639) | 1639 | `"                        f\"[{_markdown_cell(item.file)}]({_source_file_href(item.file)})\","` | — |
| [SRC-E599346ABE-L001640](../generate_index.py#L1640) | 1640 | `"                        _markdown_cell(item.file_type),"` | — |
| [SRC-E599346ABE-L001641](../generate_index.py#L1641) | 1641 | `"                        str(item.size_bytes),"` | — |
| [SRC-E599346ABE-L001642](../generate_index.py#L1642) | 1642 | `"                        line_count,"` | — |
| [SRC-E599346ABE-L001643](../generate_index.py#L1643) | 1643 | `"                        _markdown_cell(item.indexing_scope),"` | — |
| [SRC-E599346ABE-L001644](../generate_index.py#L1644) | 1644 | `"                    )"` | — |
| [SRC-E599346ABE-L001645](../generate_index.py#L1645) | 1645 | `"                )"` | — |
| [SRC-E599346ABE-L001646](../generate_index.py#L1646) | 1646 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001647](../generate_index.py#L1647) | 1647 | `"            )"` | — |
| [SRC-E599346ABE-L001648](../generate_index.py#L1648) | 1648 | `"    else:"` | — |
| [SRC-E599346ABE-L001649](../generate_index.py#L1649) | 1649 | `"        lines.append(\"\| — \| — \| — \| — \| — \| — \| لم يُمرر جرد ملفات إلى المولّد. \|\")"` | — |
| [SRC-E599346ABE-L001650](../generate_index.py#L1650) | 1650 | `""` | — |
| [SRC-E599346ABE-L001651](../generate_index.py#L1651) | 1651 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001652](../generate_index.py#L1652) | 1652 | `"        ["` | — |
| [SRC-E599346ABE-L001653](../generate_index.py#L1653) | 1653 | `"            \"\","` | — |
| [SRC-E599346ABE-L001654](../generate_index.py#L1654) | 1654 | `"            \"## تعريفات Python من AST\","` | — |
| [SRC-E599346ABE-L001655](../generate_index.py#L1655) | 1655 | `"            \"\","` | — |
| [SRC-E599346ABE-L001656](../generate_index.py#L1656) | 1656 | `"            (\"> تُحسب حالة Docstring للدوال والكلاسات فقط. المتغيرات والثوابت لا تُصنّف \""` | — |
| [SRC-E599346ABE-L001657](../generate_index.py#L1657) | 1657 | `"            \"على أنها موثقة أو ناقصة Docstring.\"),"` | — |
| [SRC-E599346ABE-L001658](../generate_index.py#L1658) | 1658 | `"            \"\","` | — |
| [SRC-E599346ABE-L001659](../generate_index.py#L1659) | 1659 | `"            \"\| الملف \| النوع \| الاسم المؤهل \| الوصف \| حالة Docstring \| السطر \| كود السطر للوصول المباشر \|\","` | — |
| [SRC-E599346ABE-L001660](../generate_index.py#L1660) | 1660 | `"            \"\|---\|---\|---\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001661](../generate_index.py#L1661) | 1661 | `"        ]"` | — |
| [SRC-E599346ABE-L001662](../generate_index.py#L1662) | 1662 | `"    )"` | — |
| [SRC-E599346ABE-L001663](../generate_index.py#L1663) | 1663 | `""` | — |
| [SRC-E599346ABE-L001664](../generate_index.py#L1664) | 1664 | `"    if not symbols:"` | — |
| [SRC-E599346ABE-L001665](../generate_index.py#L1665) | 1665 | `"        lines.append(\"\| — \| — \| — \| لا توجد تعريفات Python في الملفات المؤهلة. \| — \| — \| — \|\")"` | — |
| [SRC-E599346ABE-L001666](../generate_index.py#L1666) | 1666 | `"    else:"` | — |
| [SRC-E599346ABE-L001667](../generate_index.py#L1667) | 1667 | `"        for symbol in symbols:"` | — |
| [SRC-E599346ABE-L001668](../generate_index.py#L1668) | 1668 | `"            if symbol.documented is True:"` | — |
| [SRC-E599346ABE-L001669](../generate_index.py#L1669) | 1669 | `"                status = \"موثق\""` | — |
| [SRC-E599346ABE-L001670](../generate_index.py#L1670) | 1670 | `"            elif symbol.documented is False:"` | — |
| [SRC-E599346ABE-L001671](../generate_index.py#L1671) | 1671 | `"                status = \"ناقص\""` | — |
| [SRC-E599346ABE-L001672](../generate_index.py#L1672) | 1672 | `"            else:"` | — |
| [SRC-E599346ABE-L001673](../generate_index.py#L1673) | 1673 | `"                status = \"لا ينطبق\""` | — |
| [SRC-E599346ABE-L001674](../generate_index.py#L1674) | 1674 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001675](../generate_index.py#L1675) | 1675 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001676](../generate_index.py#L1676) | 1676 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001677](../generate_index.py#L1677) | 1677 | `"                    ("` | — |
| [SRC-E599346ABE-L001678](../generate_index.py#L1678) | 1678 | `"                        f\"[{_markdown_cell(symbol.file)}]({_source_file_href(symbol.file, symbol.line)})\","` | — |
| [SRC-E599346ABE-L001679](../generate_index.py#L1679) | 1679 | `"                        _markdown_cell(symbol.kind),"` | — |
| [SRC-E599346ABE-L001680](../generate_index.py#L1680) | 1680 | `"                        _markdown_cell(symbol.name),"` | — |
| [SRC-E599346ABE-L001681](../generate_index.py#L1681) | 1681 | `"                        _markdown_cell(symbol.description),"` | — |
| [SRC-E599346ABE-L001682](../generate_index.py#L1682) | 1682 | `"                        status,"` | — |
| [SRC-E599346ABE-L001683](../generate_index.py#L1683) | 1683 | `"                        str(symbol.line),"` | — |
| [SRC-E599346ABE-L001684](../generate_index.py#L1684) | 1684 | `"                        f\"[{_source_line_id(symbol.file, symbol.line)}]({_source_file_href(symbol.file, symbol.line)})\","` | — |
| [SRC-E599346ABE-L001685](../generate_index.py#L1685) | 1685 | `"                    )"` | — |
| [SRC-E599346ABE-L001686](../generate_index.py#L1686) | 1686 | `"                )"` | — |
| [SRC-E599346ABE-L001687](../generate_index.py#L1687) | 1687 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001688](../generate_index.py#L1688) | 1688 | `"            )"` | — |
| [SRC-E599346ABE-L001689](../generate_index.py#L1689) | 1689 | `""` | — |
| [SRC-E599346ABE-L001690](../generate_index.py#L1690) | 1690 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001691](../generate_index.py#L1691) | 1691 | `"        ["` | — |
| [SRC-E599346ABE-L001692](../generate_index.py#L1692) | 1692 | `"            \"\","` | — |
| [SRC-E599346ABE-L001693](../generate_index.py#L1693) | 1693 | `"            \"## الرموز الساكنة الإضافية\","` | — |
| [SRC-E599346ABE-L001694](../generate_index.py#L1694) | 1694 | `"            \"\","` | — |
| [SRC-E599346ABE-L001695](../generate_index.py#L1695) | 1695 | `"            (\"هذا القسم للمساعدة في الوصول إلى الواجهة والإعدادات والوثائق؛ \""` | — |
| [SRC-E599346ABE-L001696](../generate_index.py#L1696) | 1696 | `"            \"استخراج الرموز غير المحللة بـAST استدلالي وقد لا يساوي تحليلًا كاملًا للغة.\"),"` | — |
| [SRC-E599346ABE-L001697](../generate_index.py#L1697) | 1697 | `"            \"\","` | — |
| [SRC-E599346ABE-L001698](../generate_index.py#L1698) | 1698 | `"            \"\| الملف \| نوع الرمز \| الاسم/القيمة \| السطر \| كود السطر للوصول المباشر \|\","` | — |
| [SRC-E599346ABE-L001699](../generate_index.py#L1699) | 1699 | `"            \"\|---\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001700](../generate_index.py#L1700) | 1700 | `"        ]"` | — |
| [SRC-E599346ABE-L001701](../generate_index.py#L1701) | 1701 | `"    )"` | — |
| [SRC-E599346ABE-L001702](../generate_index.py#L1702) | 1702 | `"    if marker_inventory:"` | — |
| [SRC-E599346ABE-L001703](../generate_index.py#L1703) | 1703 | `"        for marker in marker_inventory:"` | — |
| [SRC-E599346ABE-L001704](../generate_index.py#L1704) | 1704 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001705](../generate_index.py#L1705) | 1705 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001706](../generate_index.py#L1706) | 1706 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001707](../generate_index.py#L1707) | 1707 | `"                    ("` | — |
| [SRC-E599346ABE-L001708](../generate_index.py#L1708) | 1708 | `"                        f\"[{_markdown_cell(marker.file)}]({_source_file_href(marker.file, marker.line)})\","` | — |
| [SRC-E599346ABE-L001709](../generate_index.py#L1709) | 1709 | `"                        _markdown_cell(marker.kind),"` | — |
| [SRC-E599346ABE-L001710](../generate_index.py#L1710) | 1710 | `"                        _markdown_cell(marker.name),"` | — |
| [SRC-E599346ABE-L001711](../generate_index.py#L1711) | 1711 | `"                        str(marker.line),"` | — |
| [SRC-E599346ABE-L001712](../generate_index.py#L1712) | 1712 | `"                        f\"[{_source_line_id(marker.file, marker.line)}]({_source_file_href(marker.file, marker.line)})\","` | — |
| [SRC-E599346ABE-L001713](../generate_index.py#L1713) | 1713 | `"                    )"` | — |
| [SRC-E599346ABE-L001714](../generate_index.py#L1714) | 1714 | `"                )"` | — |
| [SRC-E599346ABE-L001715](../generate_index.py#L1715) | 1715 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001716](../generate_index.py#L1716) | 1716 | `"            )"` | — |
| [SRC-E599346ABE-L001717](../generate_index.py#L1717) | 1717 | `"    else:"` | — |
| [SRC-E599346ABE-L001718](../generate_index.py#L1718) | 1718 | `"        lines.append(\"\| — \| — \| — \| لم تُكتشف رموز ساكنة إضافية. \| — \|\")"` | — |
| [SRC-E599346ABE-L001719](../generate_index.py#L1719) | 1719 | `""` | — |
| [SRC-E599346ABE-L001720](../generate_index.py#L1720) | 1720 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001721](../generate_index.py#L1721) | 1721 | `"        ["` | — |
| [SRC-E599346ABE-L001722](../generate_index.py#L1722) | 1722 | `"            \"\","` | — |
| [SRC-E599346ABE-L001723](../generate_index.py#L1723) | 1723 | `"            \"## سجل وسوم المراجعة والإصلاح\","` | — |
| [SRC-E599346ABE-L001724](../generate_index.py#L1724) | 1724 | `"            \"\","` | — |
| [SRC-E599346ABE-L001725](../generate_index.py#L1725) | 1725 | `"            \"هذه قائمة بالوسوم الصريحة التي تستدعي المتابعة. وجود الوسم ليس إثباتًا آليًا أن السطر معيب؛ افتح الملف عند رقم السطر وراجع السياق.\","` | — |
| [SRC-E599346ABE-L001726](../generate_index.py#L1726) | 1726 | `"            \"\","` | — |
| [SRC-E599346ABE-L001727](../generate_index.py#L1727) | 1727 | `"            \"\| كود الهفوة/الوسم \| النوع \| الملف \| السطر \| وصف الوسم \| كود السطر \| نص السطر \|\","` | — |
| [SRC-E599346ABE-L001728](../generate_index.py#L1728) | 1728 | `"            \"\|---\|---\|---\|---:\|---\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001729](../generate_index.py#L1729) | 1729 | `"        ]"` | — |
| [SRC-E599346ABE-L001730](../generate_index.py#L1730) | 1730 | `"    )"` | — |
| [SRC-E599346ABE-L001731](../generate_index.py#L1731) | 1731 | `"    if finding_inventory:"` | — |
| [SRC-E599346ABE-L001732](../generate_index.py#L1732) | 1732 | `"        line_map = {source_line.line_id: source_line for source_line in line_inventory}"` | — |
| [SRC-E599346ABE-L001733](../generate_index.py#L1733) | 1733 | `"        for finding in finding_inventory:"` | — |
| [SRC-E599346ABE-L001734](../generate_index.py#L1734) | 1734 | `"            source_line = line_map.get(finding.line_id)"` | — |
| [SRC-E599346ABE-L001735](../generate_index.py#L1735) | 1735 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001736](../generate_index.py#L1736) | 1736 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001737](../generate_index.py#L1737) | 1737 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001738](../generate_index.py#L1738) | 1738 | `"                    ("` | — |
| [SRC-E599346ABE-L001739](../generate_index.py#L1739) | 1739 | `"                        finding.finding_id,"` | — |
| [SRC-E599346ABE-L001740](../generate_index.py#L1740) | 1740 | `"                        finding.marker,"` | — |
| [SRC-E599346ABE-L001741](../generate_index.py#L1741) | 1741 | `"                        f\"[{_markdown_cell(finding.file)}]({_source_file_href(finding.file, source_line.line if source_line else 1)})\","` | — |
| [SRC-E599346ABE-L001742](../generate_index.py#L1742) | 1742 | `"                        str(source_line.line if source_line else \"غير متاح\"),"` | — |
| [SRC-E599346ABE-L001743](../generate_index.py#L1743) | 1743 | `"                        _markdown_cell(finding.description),"` | — |
| [SRC-E599346ABE-L001744](../generate_index.py#L1744) | 1744 | `"                        f\"[{finding.line_id}]({_source_file_href(finding.file, source_line.line if source_line else 1)})\","` | — |
| [SRC-E599346ABE-L001745](../generate_index.py#L1745) | 1745 | `"                        _markdown_code_span(json.dumps(source_line.content, ensure_ascii=False).replace(\"\|\", r\"\\\|\")) if source_line else \"غير متاح\","` | — |
| [SRC-E599346ABE-L001746](../generate_index.py#L1746) | 1746 | `"                    )"` | — |
| [SRC-E599346ABE-L001747](../generate_index.py#L1747) | 1747 | `"                )"` | — |
| [SRC-E599346ABE-L001748](../generate_index.py#L1748) | 1748 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001749](../generate_index.py#L1749) | 1749 | `"            )"` | — |
| [SRC-E599346ABE-L001750](../generate_index.py#L1750) | 1750 | `"    else:"` | — |
| [SRC-E599346ABE-L001751](../generate_index.py#L1751) | 1751 | `"        lines.append(\"\| — \| — \| — \| — \| لم تُكتشف وسوم صريحة من الأنواع المعروفة. \| — \| — \|\")"` | — |
| [SRC-E599346ABE-L001752](../generate_index.py#L1752) | 1752 | `""` | — |
| [SRC-E599346ABE-L001753](../generate_index.py#L1753) | 1753 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001754](../generate_index.py#L1754) | 1754 | `"        ["` | — |
| [SRC-E599346ABE-L001755](../generate_index.py#L1755) | 1755 | `"            \"\","` | — |
| [SRC-E599346ABE-L001756](../generate_index.py#L1756) | 1756 | `"            \"---\","` | — |
| [SRC-E599346ABE-L001757](../generate_index.py#L1757) | 1757 | `"            \"\","` | — |
| [SRC-E599346ABE-L001758](../generate_index.py#L1758) | 1758 | `"            \"## حدود الفهرسة\","` | — |
| [SRC-E599346ABE-L001759](../generate_index.py#L1759) | 1759 | `"            \"\","` | — |
| [SRC-E599346ABE-L001760](../generate_index.py#L1760) | 1760 | `"            \"- كل الأسطر المنطقية للملفات النصية المؤهلة القابلة للقراءة مفهرسة في SOURCE LINES INDEX، لا في هذا الجدول المختصر.\","` | — |
| [SRC-E599346ABE-L001761](../generate_index.py#L1761) | 1761 | `"            \"- الملفات الأكبر من 2 MiB أو غير القابلة للقراءة أو الثنائية تبقى ضمن الجرد الوصفي، دون فهرسة سطورها.\","` | — |
| [SRC-E599346ABE-L001762](../generate_index.py#L1762) | 1762 | `"            \"- لا تُفحص محتويات البيئة الافتراضية والاعتماديات والمجلدات المولدة.\","` | — |
| [SRC-E599346ABE-L001763](../generate_index.py#L1763) | 1763 | `"            \"- لا تُقرأ ملفات البيئة المحلية وقواعد البيانات والمفاتيح المعروفة.\","` | — |
| [SRC-E599346ABE-L001764](../generate_index.py#L1764) | 1764 | `"            \"- تحليل Python يرفض إنشاء فهرس جزئي عند وجود خطأ نحوي في أي ملف Python مؤهل.\","` | — |
| [SRC-E599346ABE-L001765](../generate_index.py#L1765) | 1765 | `"            (\"- يُحدّث هذا الفهرس آليًا عبر GitHub Actions عند دفع تغيير إلى main؛ \""` | — |
| [SRC-E599346ABE-L001766](../generate_index.py#L1766) | 1766 | `"            \"وتظل تغييرات المصدر قيد المراجعة حتى تُدمج وفق سياسة المستودع.\"),"` | — |
| [SRC-E599346ABE-L001767](../generate_index.py#L1767) | 1767 | `"            \"\","` | — |
| [SRC-E599346ABE-L001768](../generate_index.py#L1768) | 1768 | `"        ]"` | — |
| [SRC-E599346ABE-L001769](../generate_index.py#L1769) | 1769 | `"    )"` | — |
| [SRC-E599346ABE-L001770](../generate_index.py#L1770) | 1770 | `"    return \"\\n\".join(lines)"` | — |
| [SRC-E599346ABE-L001771](../generate_index.py#L1771) | 1771 | `""` | — |
| [SRC-E599346ABE-L001772](../generate_index.py#L1772) | 1772 | `""` | — |
| [SRC-E599346ABE-L001773](../generate_index.py#L1773) | 1773 | `"def write_if_changed(output_path: Path, content: str) -> bool:"` | — |
| [SRC-E599346ABE-L001774](../generate_index.py#L1774) | 1774 | `"    \"\"\"Write atomically only when the generated index differs from the existing file.\"\"\""` | — |
| [SRC-E599346ABE-L001775](../generate_index.py#L1775) | 1775 | `"    output_path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-E599346ABE-L001776](../generate_index.py#L1776) | 1776 | `"    try:"` | — |
| [SRC-E599346ABE-L001777](../generate_index.py#L1777) | 1777 | `"        if output_path.read_text(encoding=\"utf-8\") == content:"` | — |
| [SRC-E599346ABE-L001778](../generate_index.py#L1778) | 1778 | `"            return False"` | — |
| [SRC-E599346ABE-L001779](../generate_index.py#L1779) | 1779 | `"    except FileNotFoundError:"` | — |
| [SRC-E599346ABE-L001780](../generate_index.py#L1780) | 1780 | `"        pass"` | — |
| [SRC-E599346ABE-L001781](../generate_index.py#L1781) | 1781 | `""` | — |
| [SRC-E599346ABE-L001782](../generate_index.py#L1782) | 1782 | `"    temporary_path: Path \| None = None"` | — |
| [SRC-E599346ABE-L001783](../generate_index.py#L1783) | 1783 | `"    try:"` | — |
| [SRC-E599346ABE-L001784](../generate_index.py#L1784) | 1784 | `"        with tempfile.NamedTemporaryFile("` | — |
| [SRC-E599346ABE-L001785](../generate_index.py#L1785) | 1785 | `"            mode=\"w\","` | — |
| [SRC-E599346ABE-L001786](../generate_index.py#L1786) | 1786 | `"            encoding=\"utf-8\","` | — |
| [SRC-E599346ABE-L001787](../generate_index.py#L1787) | 1787 | `"            newline=\"\\n\","` | — |
| [SRC-E599346ABE-L001788](../generate_index.py#L1788) | 1788 | `"            dir=output_path.parent,"` | — |
| [SRC-E599346ABE-L001789](../generate_index.py#L1789) | 1789 | `"            prefix=f\".{output_path.name}.\","` | — |
| [SRC-E599346ABE-L001790](../generate_index.py#L1790) | 1790 | `"            suffix=\".tmp\","` | — |
| [SRC-E599346ABE-L001791](../generate_index.py#L1791) | 1791 | `"            delete=False,"` | — |
| [SRC-E599346ABE-L001792](../generate_index.py#L1792) | 1792 | `"        ) as temporary_file:"` | — |
| [SRC-E599346ABE-L001793](../generate_index.py#L1793) | 1793 | `"            temporary_file.write(content)"` | — |
| [SRC-E599346ABE-L001794](../generate_index.py#L1794) | 1794 | `"            temporary_path = Path(temporary_file.name)"` | — |
| [SRC-E599346ABE-L001795](../generate_index.py#L1795) | 1795 | `"        temporary_path.replace(output_path)"` | — |
| [SRC-E599346ABE-L001796](../generate_index.py#L1796) | 1796 | `"    finally:"` | — |
| [SRC-E599346ABE-L001797](../generate_index.py#L1797) | 1797 | `"        if temporary_path is not None and temporary_path.exists():"` | — |
| [SRC-E599346ABE-L001798](../generate_index.py#L1798) | 1798 | `"            temporary_path.unlink()"` | — |
| [SRC-E599346ABE-L001799](../generate_index.py#L1799) | 1799 | `"    return True"` | — |
| [SRC-E599346ABE-L001800](../generate_index.py#L1800) | 1800 | `""` | — |
| [SRC-E599346ABE-L001801](../generate_index.py#L1801) | 1801 | `""` | — |
| [SRC-E599346ABE-L001802](../generate_index.py#L1802) | 1802 | `"def _generate("` | — |
| [SRC-E599346ABE-L001803](../generate_index.py#L1803) | 1803 | `"    root: Path,"` | — |
| [SRC-E599346ABE-L001804](../generate_index.py#L1804) | 1804 | `") -> tuple[str, str, str, dict[str, str], int, int, int, int, int, int, int]:"` | — |
| [SRC-E599346ABE-L001805](../generate_index.py#L1805) | 1805 | `"    \"\"\"Create deterministic overview, source-line pages, and all counts without writing.\"\"\""` | — |
| [SRC-E599346ABE-L001806](../generate_index.py#L1806) | 1806 | `"    inventory = build_file_inventory(root)"` | — |
| [SRC-E599346ABE-L001807](../generate_index.py#L1807) | 1807 | `"    symbols, python_file_count = scan_repository(root)"` | — |
| [SRC-E599346ABE-L001808](../generate_index.py#L1808) | 1808 | `"    static_symbols = scan_static_symbols(root, inventory)"` | — |
| [SRC-E599346ABE-L001809](../generate_index.py#L1809) | 1809 | `"    source_lines = scan_source_lines(root, inventory)"` | — |
| [SRC-E599346ABE-L001810](../generate_index.py#L1810) | 1810 | `"    validate_source_line_coverage(root, inventory, source_lines)"` | — |
| [SRC-E599346ABE-L001811](../generate_index.py#L1811) | 1811 | `"    findings = scan_finding_annotations(source_lines)"` | — |
| [SRC-E599346ABE-L001812](../generate_index.py#L1812) | 1812 | `"    excluded_paths = discover_excluded_paths(root)"` | — |
| [SRC-E599346ABE-L001813](../generate_index.py#L1813) | 1813 | `"    coverage_audit_markdown = render_coverage_audit_markdown("` | — |
| [SRC-E599346ABE-L001814](../generate_index.py#L1814) | 1814 | `"        root, inventory, source_lines, excluded_paths"` | — |
| [SRC-E599346ABE-L001815](../generate_index.py#L1815) | 1815 | `"    )"` | — |
| [SRC-E599346ABE-L001816](../generate_index.py#L1816) | 1816 | `"    source_pages, pages_by_file = render_source_line_pages("` | — |
| [SRC-E599346ABE-L001817](../generate_index.py#L1817) | 1817 | `"        source_lines, inventory, findings"` | — |
| [SRC-E599346ABE-L001818](../generate_index.py#L1818) | 1818 | `"    )"` | — |
| [SRC-E599346ABE-L001819](../generate_index.py#L1819) | 1819 | `"    markdown = render_markdown("` | — |
| [SRC-E599346ABE-L001820](../generate_index.py#L1820) | 1820 | `"        symbols, python_file_count, inventory, static_symbols, source_lines, findings"` | — |
| [SRC-E599346ABE-L001821](../generate_index.py#L1821) | 1821 | `"    )"` | — |
| [SRC-E599346ABE-L001822](../generate_index.py#L1822) | 1822 | `"    source_lines_markdown = render_source_lines_markdown("` | — |
| [SRC-E599346ABE-L001823](../generate_index.py#L1823) | 1823 | `"        source_lines, inventory, findings, pages_by_file, source_pages"` | — |
| [SRC-E599346ABE-L001824](../generate_index.py#L1824) | 1824 | `"    )"` | — |
| [SRC-E599346ABE-L001825](../generate_index.py#L1825) | 1825 | `"    return ("` | — |
| [SRC-E599346ABE-L001826](../generate_index.py#L1826) | 1826 | `"        markdown,"` | — |
| [SRC-E599346ABE-L001827](../generate_index.py#L1827) | 1827 | `"        source_lines_markdown,"` | — |
| [SRC-E599346ABE-L001828](../generate_index.py#L1828) | 1828 | `"        coverage_audit_markdown,"` | — |
| [SRC-E599346ABE-L001829](../generate_index.py#L1829) | 1829 | `"        source_pages,"` | — |
| [SRC-E599346ABE-L001830](../generate_index.py#L1830) | 1830 | `"        python_file_count,"` | — |
| [SRC-E599346ABE-L001831](../generate_index.py#L1831) | 1831 | `"        len(inventory),"` | — |
| [SRC-E599346ABE-L001832](../generate_index.py#L1832) | 1832 | `"        len(symbols),"` | — |
| [SRC-E599346ABE-L001833](../generate_index.py#L1833) | 1833 | `"        len(source_lines),"` | — |
| [SRC-E599346ABE-L001834](../generate_index.py#L1834) | 1834 | `"        len(findings),"` | — |
| [SRC-E599346ABE-L001835](../generate_index.py#L1835) | 1835 | `"        sum(symbol.documented is True for symbol in symbols),"` | — |
| [SRC-E599346ABE-L001836](../generate_index.py#L1836) | 1836 | `"        sum(symbol.documented is False for symbol in symbols),"` | — |
| [SRC-E599346ABE-L001837](../generate_index.py#L1837) | 1837 | `"    )"` | — |
| [SRC-E599346ABE-L001838](../generate_index.py#L1838) | 1838 | `""` | — |
| [SRC-E599346ABE-L001839](../generate_index.py#L1839) | 1839 | `""` | — |
| [SRC-E599346ABE-L001840](../generate_index.py#L1840) | 1840 | `"def main(argv: Sequence[str] \| None = None) -> int:"` | — |
| [SRC-E599346ABE-L001841](../generate_index.py#L1841) | 1841 | `"    \"\"\"Generate the living repository index or check that the committed copy is current.\"\"\""` | — |
| [SRC-E599346ABE-L001842](../generate_index.py#L1842) | 1842 | `"    parser = argparse.ArgumentParser("` | — |
| [SRC-E599346ABE-L001843](../generate_index.py#L1843) | 1843 | `"        description=\"إنشاء/فحص فهرس مستودع Omarai وملفات الشفرة والرموز الساكنة.\""` | — |
| [SRC-E599346ABE-L001844](../generate_index.py#L1844) | 1844 | `"    )"` | — |
| [SRC-E599346ABE-L001845](../generate_index.py#L1845) | 1845 | `"    parser.add_argument("` | — |
| [SRC-E599346ABE-L001846](../generate_index.py#L1846) | 1846 | `"        \"--root\","` | — |
| [SRC-E599346ABE-L001847](../generate_index.py#L1847) | 1847 | `"        type=Path,"` | — |
| [SRC-E599346ABE-L001848](../generate_index.py#L1848) | 1848 | `"        default=Path(__file__).resolve().parents[1],"` | — |
| [SRC-E599346ABE-L001849](../generate_index.py#L1849) | 1849 | `"        help=\"مسار جذر المستودع (الافتراضي: جذر مشروع Omarai).\","` | — |
| [SRC-E599346ABE-L001850](../generate_index.py#L1850) | 1850 | `"    )"` | — |
| [SRC-E599346ABE-L001851](../generate_index.py#L1851) | 1851 | `"    parser.add_argument("` | — |
| [SRC-E599346ABE-L001852](../generate_index.py#L1852) | 1852 | `"        \"--check\","` | — |
| [SRC-E599346ABE-L001853](../generate_index.py#L1853) | 1853 | `"        action=\"store_true\","` | — |
| [SRC-E599346ABE-L001854](../generate_index.py#L1854) | 1854 | `"        help=\"لا تكتب ملفات؛ أعد حالة فشل إذا كان أي فهرس مولّد قديمًا أو مفقودًا.\","` | — |
| [SRC-E599346ABE-L001855](../generate_index.py#L1855) | 1855 | `"    )"` | — |
| [SRC-E599346ABE-L001856](../generate_index.py#L1856) | 1856 | `"    arguments = parser.parse_args(argv)"` | — |
| [SRC-E599346ABE-L001857](../generate_index.py#L1857) | 1857 | `""` | — |
| [SRC-E599346ABE-L001858](../generate_index.py#L1858) | 1858 | `"    try:"` | — |
| [SRC-E599346ABE-L001859](../generate_index.py#L1859) | 1859 | `"        root = arguments.root.resolve(strict=True)"` | — |
| [SRC-E599346ABE-L001860](../generate_index.py#L1860) | 1860 | `"        if not root.is_dir():"` | — |
| [SRC-E599346ABE-L001861](../generate_index.py#L1861) | 1861 | `"            raise ValueError(f\"المسار المحدد ليس مجلدًا: {root}\")"` | — |
| [SRC-E599346ABE-L001862](../generate_index.py#L1862) | 1862 | `"        ("` | — |
| [SRC-E599346ABE-L001863](../generate_index.py#L1863) | 1863 | `"            markdown,"` | — |
| [SRC-E599346ABE-L001864](../generate_index.py#L1864) | 1864 | `"            source_lines_markdown,"` | — |
| [SRC-E599346ABE-L001865](../generate_index.py#L1865) | 1865 | `"            coverage_audit_markdown,"` | — |
| [SRC-E599346ABE-L001866](../generate_index.py#L1866) | 1866 | `"            source_pages,"` | — |
| [SRC-E599346ABE-L001867](../generate_index.py#L1867) | 1867 | `"            python_file_count,"` | — |
| [SRC-E599346ABE-L001868](../generate_index.py#L1868) | 1868 | `"            repository_file_count,"` | — |
| [SRC-E599346ABE-L001869](../generate_index.py#L1869) | 1869 | `"            symbol_count,"` | — |
| [SRC-E599346ABE-L001870](../generate_index.py#L1870) | 1870 | `"            source_line_count,"` | — |
| [SRC-E599346ABE-L001871](../generate_index.py#L1871) | 1871 | `"            finding_count,"` | — |
| [SRC-E599346ABE-L001872](../generate_index.py#L1872) | 1872 | `"            documented_count,"` | — |
| [SRC-E599346ABE-L001873](../generate_index.py#L1873) | 1873 | `"            missing_count,"` | — |
| [SRC-E599346ABE-L001874](../generate_index.py#L1874) | 1874 | `"        ) = _generate(root)"` | — |
| [SRC-E599346ABE-L001875](../generate_index.py#L1875) | 1875 | `"        output_path = root / INDEX_RELATIVE_PATH"` | — |
| [SRC-E599346ABE-L001876](../generate_index.py#L1876) | 1876 | `"        source_lines_output_path = root / SOURCE_LINES_INDEX_RELATIVE_PATH"` | — |
| [SRC-E599346ABE-L001877](../generate_index.py#L1877) | 1877 | `"        generated_outputs = {"` | — |
| [SRC-E599346ABE-L001878](../generate_index.py#L1878) | 1878 | `"            INDEX_RELATIVE_PATH: markdown,"` | — |
| [SRC-E599346ABE-L001879](../generate_index.py#L1879) | 1879 | `"            SOURCE_LINES_INDEX_RELATIVE_PATH: source_lines_markdown,"` | — |
| [SRC-E599346ABE-L001880](../generate_index.py#L1880) | 1880 | `"            COVERAGE_AUDIT_RELATIVE_PATH: coverage_audit_markdown,"` | — |
| [SRC-E599346ABE-L001881](../generate_index.py#L1881) | 1881 | `"            **source_pages,"` | — |
| [SRC-E599346ABE-L001882](../generate_index.py#L1882) | 1882 | `"        }"` | — |
| [SRC-E599346ABE-L001883](../generate_index.py#L1883) | 1883 | `""` | — |
| [SRC-E599346ABE-L001884](../generate_index.py#L1884) | 1884 | `"        if arguments.check:"` | — |
| [SRC-E599346ABE-L001885](../generate_index.py#L1885) | 1885 | `"            for relative_path, expected_content in generated_outputs.items():"` | — |
| [SRC-E599346ABE-L001886](../generate_index.py#L1886) | 1886 | `"                generated_path = root / relative_path"` | — |
| [SRC-E599346ABE-L001887](../generate_index.py#L1887) | 1887 | `"                try:"` | — |
| [SRC-E599346ABE-L001888](../generate_index.py#L1888) | 1888 | `"                    current_content = generated_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-E599346ABE-L001889](../generate_index.py#L1889) | 1889 | `"                except FileNotFoundError:"` | — |
| [SRC-E599346ABE-L001890](../generate_index.py#L1890) | 1890 | `"                    print("` | — |
| [SRC-E599346ABE-L001891](../generate_index.py#L1891) | 1891 | `"                        f\"فهرس مولّد مفقود: {generated_path}. \""` | — |
| [SRC-E599346ABE-L001892](../generate_index.py#L1892) | 1892 | `"                        \"شغّل python docs/generate_index.py.\","` | — |
| [SRC-E599346ABE-L001893](../generate_index.py#L1893) | 1893 | `"                        file=sys.stderr,"` | — |
| [SRC-E599346ABE-L001894](../generate_index.py#L1894) | 1894 | `"                    )"` | — |
| [SRC-E599346ABE-L001895](../generate_index.py#L1895) | 1895 | `"                    return 1"` | — |
| [SRC-E599346ABE-L001896](../generate_index.py#L1896) | 1896 | `"                if current_content != expected_content:"` | — |
| [SRC-E599346ABE-L001897](../generate_index.py#L1897) | 1897 | `"                    if relative_path == INDEX_RELATIVE_PATH:"` | — |
| [SRC-E599346ABE-L001898](../generate_index.py#L1898) | 1898 | `"                        message = \"الفهرس قديم (الرئيسي)\""` | — |
| [SRC-E599346ABE-L001899](../generate_index.py#L1899) | 1899 | `"                    elif relative_path == SOURCE_LINES_INDEX_RELATIVE_PATH:"` | — |
| [SRC-E599346ABE-L001900](../generate_index.py#L1900) | 1900 | `"                        message = \"فهرس الأسطر قديم\""` | — |
| [SRC-E599346ABE-L001901](../generate_index.py#L1901) | 1901 | `"                    else:"` | — |
| [SRC-E599346ABE-L001902](../generate_index.py#L1902) | 1902 | `"                        message = \"فهرس تغطية الفهرسة قديم\""` | — |
| [SRC-E599346ABE-L001903](../generate_index.py#L1903) | 1903 | `"                    print("` | — |
| [SRC-E599346ABE-L001904](../generate_index.py#L1904) | 1904 | `"                        f\"{message}: {generated_path}. \""` | — |
| [SRC-E599346ABE-L001905](../generate_index.py#L1905) | 1905 | `"                        \"شغّل python docs/generate_index.py.\","` | — |
| [SRC-E599346ABE-L001906](../generate_index.py#L1906) | 1906 | `"                        file=sys.stderr,"` | — |
| [SRC-E599346ABE-L001907](../generate_index.py#L1907) | 1907 | `"                    )"` | — |
| [SRC-E599346ABE-L001908](../generate_index.py#L1908) | 1908 | `"                    return 1"` | — |
| [SRC-E599346ABE-L001909](../generate_index.py#L1909) | 1909 | `""` | — |
| [SRC-E599346ABE-L001910](../generate_index.py#L1910) | 1910 | `"            pages_directory = root / SOURCE_LINES_PAGES_DIR"` | — |
| [SRC-E599346ABE-L001911](../generate_index.py#L1911) | 1911 | `"            expected_page_names = {"` | — |
| [SRC-E599346ABE-L001912](../generate_index.py#L1912) | 1912 | `"                Path(relative_path).name"` | — |
| [SRC-E599346ABE-L001913](../generate_index.py#L1913) | 1913 | `"                for relative_path in source_pages"` | — |
| [SRC-E599346ABE-L001914](../generate_index.py#L1914) | 1914 | `"            }"` | — |
| [SRC-E599346ABE-L001915](../generate_index.py#L1915) | 1915 | `"            if pages_directory.exists():"` | — |
| [SRC-E599346ABE-L001916](../generate_index.py#L1916) | 1916 | `"                actual_page_names = {"` | — |
| [SRC-E599346ABE-L001917](../generate_index.py#L1917) | 1917 | `"                    path.name"` | — |
| [SRC-E599346ABE-L001918](../generate_index.py#L1918) | 1918 | `"                    for path in pages_directory.iterdir()"` | — |
| [SRC-E599346ABE-L001919](../generate_index.py#L1919) | 1919 | `"                    if path.is_file() and SOURCE_LINES_PAGE_RE.fullmatch(path.name)"` | — |
| [SRC-E599346ABE-L001920](../generate_index.py#L1920) | 1920 | `"                }"` | — |
| [SRC-E599346ABE-L001921](../generate_index.py#L1921) | 1921 | `"                stale_pages = actual_page_names - expected_page_names"` | — |
| [SRC-E599346ABE-L001922](../generate_index.py#L1922) | 1922 | `"                if stale_pages:"` | — |
| [SRC-E599346ABE-L001923](../generate_index.py#L1923) | 1923 | `"                    print("` | — |
| [SRC-E599346ABE-L001924](../generate_index.py#L1924) | 1924 | `"                        \"صفحات فهرس قديمة يجب حذفها بإعادة التوليد: \""` | — |
| [SRC-E599346ABE-L001925](../generate_index.py#L1925) | 1925 | `"                        + \", \".join(sorted(stale_pages)),"` | — |
| [SRC-E599346ABE-L001926](../generate_index.py#L1926) | 1926 | `"                        file=sys.stderr,"` | — |
| [SRC-E599346ABE-L001927](../generate_index.py#L1927) | 1927 | `"                    )"` | — |
| [SRC-E599346ABE-L001928](../generate_index.py#L1928) | 1928 | `"                    return 1"` | — |
| [SRC-E599346ABE-L001929](../generate_index.py#L1929) | 1929 | `"            changed = False"` | — |
| [SRC-E599346ABE-L001930](../generate_index.py#L1930) | 1930 | `"        else:"` | — |
| [SRC-E599346ABE-L001931](../generate_index.py#L1931) | 1931 | `"            changed = False"` | — |
| [SRC-E599346ABE-L001932](../generate_index.py#L1932) | 1932 | `"            for relative_path, generated_content in generated_outputs.items():"` | — |
| [SRC-E599346ABE-L001933](../generate_index.py#L1933) | 1933 | `"                if write_if_changed(root / relative_path, generated_content):"` | — |
| [SRC-E599346ABE-L001934](../generate_index.py#L1934) | 1934 | `"                    changed = True"` | — |
| [SRC-E599346ABE-L001935](../generate_index.py#L1935) | 1935 | `""` | — |
| [SRC-E599346ABE-L001936](../generate_index.py#L1936) | 1936 | `"            pages_directory = root / SOURCE_LINES_PAGES_DIR"` | — |
| [SRC-E599346ABE-L001937](../generate_index.py#L1937) | 1937 | `"            if pages_directory.exists():"` | — |
| [SRC-E599346ABE-L001938](../generate_index.py#L1938) | 1938 | `"                expected_page_names = {"` | — |
| [SRC-E599346ABE-L001939](../generate_index.py#L1939) | 1939 | `"                    Path(relative_path).name"` | — |
| [SRC-E599346ABE-L001940](../generate_index.py#L1940) | 1940 | `"                    for relative_path in source_pages"` | — |
| [SRC-E599346ABE-L001941](../generate_index.py#L1941) | 1941 | `"                }"` | — |
| [SRC-E599346ABE-L001942](../generate_index.py#L1942) | 1942 | `"                for path in pages_directory.iterdir():"` | — |
| [SRC-E599346ABE-L001943](../generate_index.py#L1943) | 1943 | `"                    if ("` | — |
| [SRC-E599346ABE-L001944](../generate_index.py#L1944) | 1944 | `"                        path.is_file()"` | — |
| [SRC-E599346ABE-L001945](../generate_index.py#L1945) | 1945 | `"                        and SOURCE_LINES_PAGE_RE.fullmatch(path.name)"` | — |
| [SRC-E599346ABE-L001946](../generate_index.py#L1946) | 1946 | `"                        and path.name not in expected_page_names"` | — |
| [SRC-E599346ABE-L001947](../generate_index.py#L1947) | 1947 | `"                    ):"` | — |
| [SRC-E599346ABE-L001948](../generate_index.py#L1948) | 1948 | `"                        path.unlink()"` | — |
| [SRC-E599346ABE-L001949](../generate_index.py#L1949) | 1949 | `"                        changed = True"` | — |
| [SRC-E599346ABE-L001950](../generate_index.py#L1950) | 1950 | `"    except (IndexGenerationError, OSError, ValueError) as exc:"` | — |
| [SRC-E599346ABE-L001951](../generate_index.py#L1951) | 1951 | `"        print(f\"خطأ في إنشاء فهرس Omarai: {exc}\", file=sys.stderr)"` | — |
| [SRC-E599346ABE-L001952](../generate_index.py#L1952) | 1952 | `"        return 1"` | — |
| [SRC-E599346ABE-L001953](../generate_index.py#L1953) | 1953 | `""` | — |
| [SRC-E599346ABE-L001954](../generate_index.py#L1954) | 1954 | `"    if arguments.check:"` | — |
| [SRC-E599346ABE-L001955](../generate_index.py#L1955) | 1955 | `"        action = \"الفهرس محدث والتحقق ناجح\""` | — |
| [SRC-E599346ABE-L001956](../generate_index.py#L1956) | 1956 | `"    else:"` | — |
| [SRC-E599346ABE-L001957](../generate_index.py#L1957) | 1957 | `"        action = \"تم تحديث\" if changed else \"الفهرس محدث بالفعل\""` | — |
| [SRC-E599346ABE-L001958](../generate_index.py#L1958) | 1958 | `"    print("` | — |
| [SRC-E599346ABE-L001959](../generate_index.py#L1959) | 1959 | `"        f\"{action}: {output_path} \| \""` | — |
| [SRC-E599346ABE-L001960](../generate_index.py#L1960) | 1960 | `"        f\"ملفات المستودع: {repository_file_count} \| \""` | — |
| [SRC-E599346ABE-L001961](../generate_index.py#L1961) | 1961 | `"        f\"ملفات Python: {python_file_count} \| \""` | — |
| [SRC-E599346ABE-L001962](../generate_index.py#L1962) | 1962 | `"        f\"تعريفات Python: {symbol_count} \| \""` | — |
| [SRC-E599346ABE-L001963](../generate_index.py#L1963) | 1963 | `"        f\"أسطر مفهرسة: {source_line_count} \| \""` | — |
| [SRC-E599346ABE-L001964](../generate_index.py#L1964) | 1964 | `"        f\"صفحات أسطر: {len(source_pages)} \| \""` | — |
| [SRC-E599346ABE-L001965](../generate_index.py#L1965) | 1965 | `"        f\"وسوم مراجعة: {finding_count} \| \""` | — |
| [SRC-E599346ABE-L001966](../generate_index.py#L1966) | 1966 | `"        f\"موثق: {documented_count} \| \""` | — |
| [SRC-E599346ABE-L001967](../generate_index.py#L1967) | 1967 | `"        f\"ناقص Docstring: {missing_count}\""` | — |
| [SRC-E599346ABE-L001968](../generate_index.py#L1968) | 1968 | `"    )"` | — |
| [SRC-E599346ABE-L001969](../generate_index.py#L1969) | 1969 | `"    return 0"` | — |
| [SRC-E599346ABE-L001970](../generate_index.py#L1970) | 1970 | `""` | — |
| [SRC-E599346ABE-L001971](../generate_index.py#L1971) | 1971 | `""` | — |
| [SRC-E599346ABE-L001972](../generate_index.py#L1972) | 1972 | `"if __name__ == \"__main__\":"` | — |
| [SRC-E599346ABE-L001973](../generate_index.py#L1973) | 1973 | `"    raise SystemExit(main())"` | — |
## وثائق وفهرسة

### FILE-6E35221BFA — [docs/GO_LIVE_CHECKLIST_AR.md](../GO_LIVE_CHECKLIST_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6E35221BFA-L000001](../GO_LIVE_CHECKLIST_AR.md#L1) | 1 | `"# قائمة قبول Omarai قبل التشغيل العام"` | — |
| [SRC-6E35221BFA-L000002](../GO_LIVE_CHECKLIST_AR.md#L2) | 2 | `""` | — |
| [SRC-6E35221BFA-L000003](../GO_LIVE_CHECKLIST_AR.md#L3) | 3 | `"هذه القائمة تفصل بين نجاح البناء وبين إثبات أن الوكيل يعمل عبر عنوان استضافة عام."` | — |
| [SRC-6E35221BFA-L000004](../GO_LIVE_CHECKLIST_AR.md#L4) | 4 | `""` | — |
| [SRC-6E35221BFA-L000005](../GO_LIVE_CHECKLIST_AR.md#L5) | 5 | `"راجع أيضًا [مصفوفة أدلة الاختبار](OMARAI_TEST_EVIDENCE_MATRIX_AR.md) للتمييز بين اختبارات الوحدة والـMocks واختبارات الحاوية والقبول الحي، وحالة كل إثبات وحدوده. نتائج CI وحدها لا تعني أن خدمة مستضافة أو كل موفر خارجي يعمل حيًا."` | — |
| [SRC-6E35221BFA-L000006](../GO_LIVE_CHECKLIST_AR.md#L6) | 6 | `""` | — |
| [SRC-6E35221BFA-L000007](../GO_LIVE_CHECKLIST_AR.md#L7) | 7 | `"## إعداد الاستضافة"` | — |
| [SRC-6E35221BFA-L000008](../GO_LIVE_CHECKLIST_AR.md#L8) | 8 | `""` | — |
| [SRC-6E35221BFA-L000009](../GO_LIVE_CHECKLIST_AR.md#L9) | 9 | `"1. اتبع [دليل النشر العربي](DEPLOY_RAILWAY_AR.md) وأنشئ الخدمة يدويًا في حساب الاستضافة."` | — |
| [SRC-6E35221BFA-L000010](../GO_LIVE_CHECKLIST_AR.md#L10) | 10 | ``"2. استخدم المستودع `mosabosama2030-oss/omarai` والفرع `main` وإعداد Docker المرفق."`` | — |
| [SRC-6E35221BFA-L000011](../GO_LIVE_CHECKLIST_AR.md#L11) | 11 | ``"3. اضبط الأسرار من لوحة الاستضافة فقط: `OMARAI_PUBLIC_DEPLOYMENT=1`، ورمز `OMARAI_ACCESS_TOKEN` عشوائي بطول 32 حرفًا على الأقل، ومفتاح مزود النموذج `OPENROUTER_API_KEY` أو `OMARAI_LLM_API_KEY`."`` | — |
| [SRC-6E35221BFA-L000012](../GO_LIVE_CHECKLIST_AR.md#L12) | 12 | ``"4. اترك `OMARAI_OPENROUTER_WEB_SEARCH` غير مضبوط ما لم تراجع التكلفة وتوافق عليها."`` | — |
| [SRC-6E35221BFA-L000013](../GO_LIVE_CHECKLIST_AR.md#L13) | 13 | ``"5. أنشئ نطاق HTTPS وتحقق من `https://your-app.example.com/api/health`."`` | — |
| [SRC-6E35221BFA-L000014](../GO_LIVE_CHECKLIST_AR.md#L14) | 14 | ``"6. عند بناء صورة Docker، مرّر SHA الكامل للمصدر عبر وسيط البناء: `--build-arg OMARAI_BUILD_SHA=\"$(git rev-parse HEAD)\"`. يجب أن تعيد `/api/health` قيمة `build.sha` المطابقة لذلك الـSHA."`` | — |
| [SRC-6E35221BFA-L000015](../GO_LIVE_CHECKLIST_AR.md#L15) | 15 | `"7. إذا كانت منصة الاستضافة لا تسمح بتمرير وسيط البناء، فربط SHA يظل غير مثبت؛ لا تعتبر قبول النشر مكتملًا حتى تتوفر طريقة موثوقة لخبز نسخة المصدر في الصورة."` | — |
| [SRC-6E35221BFA-L000016](../GO_LIVE_CHECKLIST_AR.md#L16) | 16 | `""` | — |
| [SRC-6E35221BFA-L000017](../GO_LIVE_CHECKLIST_AR.md#L17) | 17 | ``"**حد الثقة الخاص بـ CORS خلف الوكيل العكسي:** يحسب Omarai أصل الخدمة من `Host`، ولا يثق برأس `X-Forwarded-Host` الذي قد يرسله العميل. إذا كانت منصة الاستضافة تعيد كتابة `Host` إلى اسم داخلي، اضبط `OMARAI_ALLOWED_ORIGINS=https://your-app.example.com` في إعدادات الخدمة لاستخدام النطاق العام الدقيق. لا تستخدم wildcard ولا تضف نطاقًا لا تملكه."`` | — |
| [SRC-6E35221BFA-L000018](../GO_LIVE_CHECKLIST_AR.md#L18) | 18 | `""` | — |
| [SRC-6E35221BFA-L000019](../GO_LIVE_CHECKLIST_AR.md#L19) | 19 | `"## اختبار قبول حي"` | — |
| [SRC-6E35221BFA-L000020](../GO_LIVE_CHECKLIST_AR.md#L20) | 20 | `""` | — |
| [SRC-6E35221BFA-L000021](../GO_LIVE_CHECKLIST_AR.md#L21) | 21 | ``"أضف GitHub Actions secret باسم `OMARAI_ACCESS_TOKEN` واجعل قيمته مطابقة لرمز الوصول في الاستضافة، وأضف secret باسم `OMARAI_BASE_URL` بقيمة أصل HTTPS للخدمة مثل `https://your-app.example.com` دون مسار إضافي. لا تضع رمز الوصول في مدخلات workflow أو الدردشة أو السجلات. بعد ضبط السرّين، افتح **Actions → Omarai hosted acceptance smoke → Run workflow**. يستهدف الاختبار النطاق المحفوظ في إعدادات المستودع؛ لا يأخذ عنوانًا حرًا من مُشغّل workflow، لتجنب إرسال رمز الوصول إلى وجهة غير مقصودة."`` | — |
| [SRC-6E35221BFA-L000022](../GO_LIVE_CHECKLIST_AR.md#L22) | 22 | `""` | — |
| [SRC-6E35221BFA-L000023](../GO_LIVE_CHECKLIST_AR.md#L23) | 23 | `"الاختبار الحي ينفذ فحص الصحة، ويرفض طلب API بلا رمز، ثم يختبر البحث والنموذج ويطلب إجابة عربية فعلية. قد يستهلك رصيد مزود النموذج أو البحث؛ شغّله فقط بعد الموافقة على ذلك."` | — |
| [SRC-6E35221BFA-L000024](../GO_LIVE_CHECKLIST_AR.md#L24) | 24 | `""` | — |
| [SRC-6E35221BFA-L000025](../GO_LIVE_CHECKLIST_AR.md#L25) | 25 | `"## شروط النجاح"` | — |
| [SRC-6E35221BFA-L000026](../GO_LIVE_CHECKLIST_AR.md#L26) | 26 | `""` | — |
| [SRC-6E35221BFA-L000027](../GO_LIVE_CHECKLIST_AR.md#L27) | 27 | ``"- `/api/health` يعيد HTTP 200 وصحة سليمة."`` | — |
| [SRC-6E35221BFA-L000028](../GO_LIVE_CHECKLIST_AR.md#L28) | 28 | ``"- `build.sha` يطابق SHA كاملًا للصورة المستهدفة، وليس `unknown`."`` | — |
| [SRC-6E35221BFA-L000029](../GO_LIVE_CHECKLIST_AR.md#L29) | 29 | ``"- طلب `POST /api/agent` بلا رمز يعيد HTTP 401."`` | — |
| [SRC-6E35221BFA-L000030](../GO_LIVE_CHECKLIST_AR.md#L30) | 30 | `"- التشخيص يثبت اتصال البحث الفعلي واستلام استجابة فعلية من النموذج."` | — |
| [SRC-6E35221BFA-L000031](../GO_LIVE_CHECKLIST_AR.md#L31) | 31 | `"- السؤال العربي يعيد إجابة ومصادر صالحة، مع التأكد من أن البحث والنموذج مستخدمان."` | — |
| [SRC-6E35221BFA-L000032](../GO_LIVE_CHECKLIST_AR.md#L32) | 32 | `"- لا يظهر أي رمز وصول أو مفتاح API في التقرير."` | — |
| [SRC-6E35221BFA-L000033](../GO_LIVE_CHECKLIST_AR.md#L33) | 33 | `""` | — |
| [SRC-6E35221BFA-L000034](../GO_LIVE_CHECKLIST_AR.md#L34) | 34 | `"## اختبار يدوي على Android"` | — |
| [SRC-6E35221BFA-L000035](../GO_LIVE_CHECKLIST_AR.md#L35) | 35 | `""` | — |
| [SRC-6E35221BFA-L000036](../GO_LIVE_CHECKLIST_AR.md#L36) | 36 | `"بعد نجاح الاختبار الآلي، افتح الموقع من متصفح الهاتف، وأدخل رمز الوصول في الواجهة، ثم اختبر سؤالًا عربيًا وفتح المصادر في تبويب منفصل. جرّب رمزًا خاطئًا وتحقق من رسالة الرفض. استخدم أسئلة عامة فقط، ولا تستخدم بيانات عملاء حقيقية."` | — |
| [SRC-6E35221BFA-L000037](../GO_LIVE_CHECKLIST_AR.md#L37) | 37 | `""` | — |
| [SRC-6E35221BFA-L000038](../GO_LIVE_CHECKLIST_AR.md#L38) | 38 | `"## حدود مهمة"` | — |
| [SRC-6E35221BFA-L000039](../GO_LIVE_CHECKLIST_AR.md#L39) | 39 | `""` | — |
| [SRC-6E35221BFA-L000040](../GO_LIVE_CHECKLIST_AR.md#L40) | 40 | `"إعداد Docker وRailway لا ينشئ خدمة الاستضافة تلقائيًا ولا يضبط أسرار الحساب. قاعدة SQLite قد لا تكون دائمة على حاوية مؤقتة، وحد الطلبات الحالي محفوظ في ذاكرة العملية، والرؤوس التي يرسلها الوكيل العكسي تتطلب إعدادًا موثوقًا. لا تعتبر الاختبار الحي ضمانًا للاستمرارية، ولا تغني هذه القائمة عن مراجعة الأمان أو موافقة صاحب المشروع على الدمج."` | — |
## وثائق وفهرسة

### FILE-C8EA754D73 — [docs/IMPLEMENTATION_SCOPE.md](../IMPLEMENTATION_SCOPE.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C8EA754D73-L000001](../IMPLEMENTATION_SCOPE.md#L1) | 1 | `"# Omarai — نطاق التنفيذ الفعلي وحدوده"` | — |
| [SRC-C8EA754D73-L000002](../IMPLEMENTATION_SCOPE.md#L2) | 2 | `""` | — |
| [SRC-C8EA754D73-L000003](../IMPLEMENTATION_SCOPE.md#L3) | 3 | `"**Purpose:** Keep this scope note aligned with the source code and operator-visible claims. This document is a scope description, not a certification of compliance or live-provider availability."` | — |
| [SRC-C8EA754D73-L000004](../IMPLEMENTATION_SCOPE.md#L4) | 4 | `""` | — |
| [SRC-C8EA754D73-L000005](../IMPLEMENTATION_SCOPE.md#L5) | 5 | ``"**Baseline reviewed:** `main` at merge commit `c3d3f8b1843cb58a9cbc02a69e8edc9e6410abaa` (2026-10-19), after PR #44 and PR #45 were merged.  "`` | — |
| [SRC-C8EA754D73-L000006](../IMPLEMENTATION_SCOPE.md#L6) | 6 | ``"**Evidence labels:** `VERIFIED` means directly confirmed in source or a named automated check; `INFERRED` means a bounded conclusion from source structure; `UNKNOWN` means live or environmental evidence is not available. A source-level capability must not be described as a live integration test."`` | — |
| [SRC-C8EA754D73-L000007](../IMPLEMENTATION_SCOPE.md#L7) | 7 | `""` | — |
| [SRC-C8EA754D73-L000008](../IMPLEMENTATION_SCOPE.md#L8) | 8 | `"## Implemented in the repository"` | — |
| [SRC-C8EA754D73-L000009](../IMPLEMENTATION_SCOPE.md#L9) | 9 | `""` | — |
| [SRC-C8EA754D73-L000010](../IMPLEMENTATION_SCOPE.md#L10) | 10 | `"- **Lead workspace — VERIFIED in source:** Arabic phrase normalization and heuristic intent scoring; SQLite lead persistence; duplicate detection; source metadata; manual lead-status lifecycle; CSV import/export; CLI and HTTP API."` | — |
| [SRC-C8EA754D73-L000011](../IMPLEMENTATION_SCOPE.md#L11) | 11 | `"- **Research pipeline — VERIFIED in source:** natural-language search planning with deterministic fallback; DuckDuckGo HTML and Bing RSS search; Google News RSS for freshness-sensitive requests; evidence fusion/ranking; selected public page extraction; source/provenance metadata and research diagnostics."` | — |
| [SRC-C8EA754D73-L000012](../IMPLEMENTATION_SCOPE.md#L12) | 12 | `"- **Optional connectors — VERIFIED as conditional code paths only:** Brave and Tavily when configured; DeepSeek Search when explicitly enabled with its API key; selected public social endpoints and official platform APIs when their required credentials are configured. This does not prove a specific credential, account, quota, or live connector currently works."` | — |
| [SRC-C8EA754D73-L000013](../IMPLEMENTATION_SCOPE.md#L13) | 13 | `"- **External language model — VERIFIED in source:** an OpenAI-compatible model endpoint is used for planning, answer generation and model-assisted review when a key is configured. The user question, selected history and page excerpts may be sent to that configured external provider. Omarai is not a locally trained foundation model and does not operate as an offline-only reasoning system."` | — |
| [SRC-C8EA754D73-L000014](../IMPLEMENTATION_SCOPE.md#L14) | 14 | `"- **Evidence and failure reporting — VERIFIED in source:** the answer includes sources, search-attempt outcome and diagnostic metadata; the code expressly describes its second-pass claim review as model-assisted, not an independent deterministic fact-check. Source count, domain count, and coverage indicators are not probabilities of truth or proof of editorial independence."` | — |
| [SRC-C8EA754D73-L000015](../IMPLEMENTATION_SCOPE.md#L15) | 15 | `"- **HTTP/API and UI — VERIFIED in source:** Arabic RTL web interfaces, JSON endpoints, API input checks, same-origin/configured-origin handling, an in-memory per-client rate limiter, and bearer-token protection for protected API routes when public-deployment mode is enabled."` | — |
| [SRC-C8EA754D73-L000016](../IMPLEMENTATION_SCOPE.md#L16) | 16 | `"- **Deployment configuration — VERIFIED in source:** a Dockerfile and hosting configuration exist. Their existence alone does not prove a live service was deployed, is reachable, has persistent disk, or has passed live smoke tests."` | — |
| [SRC-C8EA754D73-L000017](../IMPLEMENTATION_SCOPE.md#L17) | 17 | ``"- **Automated validation — VERIFIED within the listed test scope:** after the budget/concurrency change, GitHub Actions run [39198411650](https://github.com/mosabosama2030-oss/omarai/actions/runs/39198411650) on PR #44 head `de20d029cb9877c8fdef62148f643eb9022b0956` passed Ruff, 232 pytest tests on Python 3.11, 232 pytest tests on Python 3.12, and container/protected-API smoke checks. PR #45 head `35e85ceae13b15f273997eba043b12126652f05a` passed run [39198109298](https://github.com/mosabosama2030-oss/omarai/actions/runs/39198109298), with 224 pytest tests on each Python version and container smoke checks. Both PRs were subsequently merged into the reviewed `main` lineage. These CI results do not prove live search-provider availability, factual correctness, load capacity, deployment health, or database restore."`` | — |
| [SRC-C8EA754D73-L000018](../IMPLEMENTATION_SCOPE.md#L18) | 18 | `""` | — |
| [SRC-C8EA754D73-L000019](../IMPLEMENTATION_SCOPE.md#L19) | 19 | `"## Explicitly out of scope or not yet proven"` | — |
| [SRC-C8EA754D73-L000020](../IMPLEMENTATION_SCOPE.md#L20) | 20 | `""` | — |
| [SRC-C8EA754D73-L000021](../IMPLEMENTATION_SCOPE.md#L21) | 21 | `"- **Multi-user or multi-tenant service — NOT IMPLEMENTED in the reviewed baseline:** the API uses one shared bearer token and a shared lead store; it has no per-user identity, role-based authorization or tenant/data isolation. Anyone who obtains the token has the access granted by that token. Treat a hosted instance as a single-operator service unless and until these controls are implemented and tested."` | — |
| [SRC-C8EA754D73-L000022](../IMPLEMENTATION_SCOPE.md#L22) | 22 | `"- **Deterministic verification of every factual claim — NOT IMPLEMENTED:** citation-index validation and model-assisted review are not an independent proof that every sentence follows from its cited source. Users must be shown this limitation clearly."` | — |
| [SRC-C8EA754D73-L000023](../IMPLEMENTATION_SCOPE.md#L23) | 23 | `"- **Live provider reliability — UNKNOWN unless measured:** unit tests with mocks and a successful container smoke test do not establish that a provider is currently reachable, that credentials are valid, or that the produced answer is accurate."` | — |
| [SRC-C8EA754D73-L000024](../IMPLEMENTATION_SCOPE.md#L24) | 24 | ``"- **Request-wide limits — VERIFIED within automated unit-test scope:** merged code adds `agents/request_budget.py` and attaches a cooperative per-answer time/resource budget across search queries, provider search calls (including direct social HTTP operations), model attempts, page fetches, and optional server-side search-tool calls. The tested defaults are 90 seconds, 8 search queries, 32 provider/social HTTP operations, 8 model HTTP attempts, 8 page fetches, and up to 3 optional server-side tool calls, with hard-capped environment overrides. The API also applies a process-local semaphore to `/api/agent` and `/api/diagnostics` (default 4, hard maximum 8), returning 503 when all slots are occupied. Regression tests cover budget limits and rejection under an occupied slot. The deadline is cooperative, not hard cancellation; the semaphore is not distributed. Live connectors and production load remain UNKNOWN."`` | — |
| [SRC-C8EA754D73-L000025](../IMPLEMENTATION_SCOPE.md#L25) | 25 | `"- **Public operational configuration — UNKNOWN until verified per deployment:** actual reverse-proxy trust, CORS allowlist, TLS termination, secret configuration, deployed commit identity, and live endpoint behavior depend on the chosen host and configuration."` | — |
| [SRC-C8EA754D73-L000026](../IMPLEMENTATION_SCOPE.md#L26) | 26 | `"- **Database continuity — UNKNOWN:** backup, restore, and durable SQLite persistence have not been proven for a specific host. Do not store irreplaceable production leads until backup/restore and storage persistence are tested."` | — |
| [SRC-C8EA754D73-L000027](../IMPLEMENTATION_SCOPE.md#L27) | 27 | `"- **Load and concurrency capacity — UNKNOWN:** a process-local semaphore is present and its rejection path is unit-tested, but that does not establish throughput or a numeric concurrent-user capacity. Do not publish throughput, availability or capacity claims without representative measurements."` | — |
| [SRC-C8EA754D73-L000028](../IMPLEMENTATION_SCOPE.md#L28) | 28 | `"- **Historical secret exposure — UNKNOWN:** a clean scan of the current tree, if obtained, does not prove the entire Git history has never contained a secret."` | — |
| [SRC-C8EA754D73-L000029](../IMPLEMENTATION_SCOPE.md#L29) | 29 | `"- **Automated outbound contact — NOT IMPLEMENTED:** the agent does not send messages or contact people automatically. Any future outbound action must have explicit policy controls and human approval."` | — |
| [SRC-C8EA754D73-L000030](../IMPLEMENTATION_SCOPE.md#L30) | 30 | `""` | — |
| [SRC-C8EA754D73-L000031](../IMPLEMENTATION_SCOPE.md#L31) | 31 | `"## Operating assumptions"` | — |
| [SRC-C8EA754D73-L000032](../IMPLEMENTATION_SCOPE.md#L32) | 32 | `""` | — |
| [SRC-C8EA754D73-L000033](../IMPLEMENTATION_SCOPE.md#L33) | 33 | `"1. Keep the current architecture as a modular monolith unless evidence and a recorded architecture decision justify a change."` | — |
| [SRC-C8EA754D73-L000034](../IMPLEMENTATION_SCOPE.md#L34) | 34 | `"2. Default to a single-operator deployment with a private, randomly generated bearer token; never publish that token or share it as if it were individual user authentication."` | — |
| [SRC-C8EA754D73-L000035](../IMPLEMENTATION_SCOPE.md#L35) | 35 | `"3. Do not submit passwords, API keys, private information, or personal/confidential customer data to an external model provider, especially a free endpoint with its own retention/logging terms."` | — |
| [SRC-C8EA754D73-L000036](../IMPLEMENTATION_SCOPE.md#L36) | 36 | `"4. Treat page text, snippets, social posts, user history, and model output as untrusted data. They are not an authority to override application policy or execute privileged actions."` | — |
| [SRC-C8EA754D73-L000037](../IMPLEMENTATION_SCOPE.md#L37) | 37 | ``"5. Label each live connector probe, deployed smoke test, migration/restore test, and load test as `NOT_RUN` until that specific test actually runs. Do not infer its success from unit-test CI."`` | — |
| [SRC-C8EA754D73-L000038](../IMPLEMENTATION_SCOPE.md#L38) | 38 | `""` | — |
| [SRC-C8EA754D73-L000039](../IMPLEMENTATION_SCOPE.md#L39) | 39 | `"## Recommended next increments"` | — |
| [SRC-C8EA754D73-L000040](../IMPLEMENTATION_SCOPE.md#L40) | 40 | `""` | — |
| [SRC-C8EA754D73-L000041](../IMPLEMENTATION_SCOPE.md#L41) | 41 | `"1. Keep testing the merged cooperative budget against failure paths and resource exhaustion; do not describe it as hard cancellation or load-tested capacity."` | — |
| [SRC-C8EA754D73-L000042](../IMPLEMENTATION_SCOPE.md#L42) | 42 | `"2. Add deterministic citation-integrity controls and adversarial prompt-injection tests while retaining the limitation that source entailment cannot be proved by citation-index checks alone."` | — |
| [SRC-C8EA754D73-L000043](../IMPLEMENTATION_SCOPE.md#L43) | 43 | `"3. Reconcile the shared-token/single-store deployment with the declared single-operator scope; design real identity and data isolation before any multi-user public offering."` | — |
| [SRC-C8EA754D73-L000044](../IMPLEMENTATION_SCOPE.md#L44) | 44 | `"4. Add a repeatable live connector probe and a deployed acceptance report clearly separated from mock/unit-test results."` | — |
| [SRC-C8EA754D73-L000045](../IMPLEMENTATION_SCOPE.md#L45) | 45 | `"5. Test SQLite persistence and backup/restore on the selected host before storing production lead data."` | — |
| [SRC-C8EA754D73-L000046](../IMPLEMENTATION_SCOPE.md#L46) | 46 | ``"6. Reconcile remaining requirements to exact commit SHAs and individual tests; keep untested requirements `UNKNOWN` and unrun checks `NOT_RUN`."`` | — |
| [SRC-C8EA754D73-L000047](../IMPLEMENTATION_SCOPE.md#L47) | 47 | `"7. Keep all external contact and consequential actions human-approved."` | — |
## وثائق وفهرسة

### FILE-21D5D044E2 — [docs/OMARAI_EXCEPTIONS_REGISTER_AR.md](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-21D5D044E2-L000001](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L1) | 1 | `"# Omarai — سجل الاستثناءات والقرارات المؤجلة"` | — |
| [SRC-21D5D044E2-L000002](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L2) | 2 | `""` | — |
| [SRC-21D5D044E2-L000003](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L3) | 3 | `"**المعرف:** OMARAI-EXCEPTIONS-REGISTER-001  "` | — |
| [SRC-21D5D044E2-L000004](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L4) | 4 | `"**التاريخ:** 2026-10-19  "` | — |
| [SRC-21D5D044E2-L000005](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L5) | 5 | `"**الحالة:** مقترح للمراجعة — لم يُعتمد أي استثناء بموجب هذا الملف.  "` | — |
| [SRC-21D5D044E2-L000006](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L6) | 6 | `"**المسؤول عن القرار:** مدير المشروع البشري  "` | — |
| [SRC-21D5D044E2-L000007](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L7) | 7 | ``"**مرجع الحوكمة:** `GOV-003` و`GOV-004` و`GOV-005`"`` | — |
| [SRC-21D5D044E2-L000008](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L8) | 8 | `""` | — |
| [SRC-21D5D044E2-L000009](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L9) | 9 | `"## 1. الغرض وقواعد الاستخدام"` | — |
| [SRC-21D5D044E2-L000010](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L10) | 10 | `""` | — |
| [SRC-21D5D044E2-L000011](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L11) | 11 | ``"يوثق هذا السجل أي استثناء مطلوب من متطلب إلزامي `MUST` أو قرار بتحديد نطاق الإصدار. إعداد هذا السجل أو دمجه لا يعني قبول المخاطر المدرجة."`` | — |
| [SRC-21D5D044E2-L000012](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L12) | 12 | `""` | — |
| [SRC-21D5D044E2-L000013](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L13) | 13 | `"يجب أن يحتوي كل استثناء معتمد على: معرف المتطلب، السبب، النطاق، المخاطر والبيانات/القدرات المتأثرة، البديل التعويضي، صاحب صلاحية الموافقة، تاريخ أو شرط الانتهاء، ودليل إعادة النظر والإغلاق."` | — |
| [SRC-21D5D044E2-L000014](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L14) | 14 | `""` | — |
| [SRC-21D5D044E2-L000015](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L15) | 15 | ``"- `PROPOSED`: مقترح ينتظر قرارًا بشريًا صريحًا."`` | — |
| [SRC-21D5D044E2-L000016](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L16) | 16 | ``"- `WAIVED`: استثناء وافق عليه صاحب الصلاحية، بنطاق وحدود وموعد/شرط انتهاء."`` | — |
| [SRC-21D5D044E2-L000017](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L17) | 17 | ``"- `NOT APPLICABLE`: المتطلب لا ينطبق على نطاق محدد حاليًا مع السبب وشرط إعادة النظر."`` | — |
| [SRC-21D5D044E2-L000018](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L18) | 18 | ``"- `UNKNOWN`: الأدلة لا تكفي للحكم؛ لا يجوز استخدام استثناء لتغطية هذه الحالة."`` | — |
| [SRC-21D5D044E2-L000019](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L19) | 19 | ``"- `NOT RUN`: اختبار مطلوب لم يُنفذ."`` | — |
| [SRC-21D5D044E2-L000020](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L20) | 20 | `""` | — |
| [SRC-21D5D044E2-L000021](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L21) | 21 | `"لا توجد في هذا السجل موافقات بشرية مختلقة أو استثناءات مفتوحة إلى أجل غير محدد. **لا يُسجل أي عنصر كـWAIVED إلا بعد توثيق موافقتك الصريحة.**"` | — |
| [SRC-21D5D044E2-L000022](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L22) | 22 | `""` | — |
| [SRC-21D5D044E2-L000023](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L23) | 23 | `"## 2. سجل الاستثناءات المعتمدة"` | — |
| [SRC-21D5D044E2-L000024](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L24) | 24 | `""` | — |
| [SRC-21D5D044E2-L000025](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L25) | 25 | `"\| معرف الاستثناء \| المتطلب \| النطاق \| الموافِق \| الحالة \| الانتهاء/إعادة النظر \| دليل القرار \|"` | — |
| [SRC-21D5D044E2-L000026](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L26) | 26 | `"\|---\|---\|---\|---\|---\|---\|---\|"` | — |
| [SRC-21D5D044E2-L000027](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L27) | 27 | `"\| — \| — \| لا يوجد استثناء معتمد مسجل في هذا الملف حتى تاريخ اللقطة. \| — \| لا توجد موافقات مسجلة هنا \| — \| لا يثبت ذلك غياب قرار أو موافقة خارج المستودع. \|"` | — |
| [SRC-21D5D044E2-L000028](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L28) | 28 | `""` | — |
| [SRC-21D5D044E2-L000029](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L29) | 29 | `"## 3. مقترحات للمراجعة — ليست استثناءات معتمدة"` | — |
| [SRC-21D5D044E2-L000030](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L30) | 30 | `""` | — |
| [SRC-21D5D044E2-L000031](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L31) | 31 | `"### EX-PROP-001 — حصر النسخة على مشغّل واحد"` | — |
