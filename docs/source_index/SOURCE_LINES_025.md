# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **025**
- سجلات الأسطر: **800**
- النطاق: SRC-FA4E1423C3-L000231 إلى SRC-829A979985-L000555
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## اختبارات

### FILE-FA4E1423C3 — [tests/test_generate_index.py](../../tests/test_generate_index.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-FA4E1423C3-L000231](../../tests/test_generate_index.py#L231) | 231 | `"    )"` | — |
| [SRC-FA4E1423C3-L000232](../../tests/test_generate_index.py#L232) | 232 | `"    output_path = tmp_path / \"docs\" / \"MASTER_INDEX.md\""` | — |
| [SRC-FA4E1423C3-L000233](../../tests/test_generate_index.py#L233) | 233 | `""` | — |
| [SRC-FA4E1423C3-L000234](../../tests/test_generate_index.py#L234) | 234 | `"    assert first_markdown == second_markdown"` | — |
| [SRC-FA4E1423C3-L000235](../../tests/test_generate_index.py#L235) | 235 | `"    assert INDEXER.write_if_changed(output_path, first_markdown) is True"` | — |
| [SRC-FA4E1423C3-L000236](../../tests/test_generate_index.py#L236) | 236 | `"    assert INDEXER.write_if_changed(output_path, second_markdown) is False"` | — |
| [SRC-FA4E1423C3-L000237](../../tests/test_generate_index.py#L237) | 237 | `""` | — |
| [SRC-FA4E1423C3-L000238](../../tests/test_generate_index.py#L238) | 238 | `""` | — |
| [SRC-FA4E1423C3-L000239](../../tests/test_generate_index.py#L239) | 239 | `"def test_check_mode_detects_stale_index_without_modifying_it(tmp_path: Path, capsys) -> None:"` | — |
| [SRC-FA4E1423C3-L000240](../../tests/test_generate_index.py#L240) | 240 | `"    \"\"\"Check mode fails on a stale index and leaves the existing file untouched.\"\"\""` | — |
| [SRC-FA4E1423C3-L000241](../../tests/test_generate_index.py#L241) | 241 | `"    (tmp_path / \"app.py\").write_text(\"VALUE = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000242](../../tests/test_generate_index.py#L242) | 242 | `"    docs_dir = tmp_path / \"docs\""` | — |
| [SRC-FA4E1423C3-L000243](../../tests/test_generate_index.py#L243) | 243 | `"    docs_dir.mkdir()"` | — |
| [SRC-FA4E1423C3-L000244](../../tests/test_generate_index.py#L244) | 244 | `"    index_path = docs_dir / \"MASTER_INDEX.md\""` | — |
| [SRC-FA4E1423C3-L000245](../../tests/test_generate_index.py#L245) | 245 | `"    index_path.write_text(\"stale\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000246](../../tests/test_generate_index.py#L246) | 246 | `""` | — |
| [SRC-FA4E1423C3-L000247](../../tests/test_generate_index.py#L247) | 247 | `"    assert INDEXER.main([\"--root\", str(tmp_path), \"--check\"]) == 1"` | — |
| [SRC-FA4E1423C3-L000248](../../tests/test_generate_index.py#L248) | 248 | `"    assert index_path.read_text(encoding=\"utf-8\") == \"stale\""` | — |
| [SRC-FA4E1423C3-L000249](../../tests/test_generate_index.py#L249) | 249 | `"    assert \"الفهرس قديم\" in capsys.readouterr().err"` | — |
| [SRC-FA4E1423C3-L000250](../../tests/test_generate_index.py#L250) | 250 | `""` | — |
| [SRC-FA4E1423C3-L000251](../../tests/test_generate_index.py#L251) | 251 | `"    assert INDEXER.main([\"--root\", str(tmp_path)]) == 0"` | — |
| [SRC-FA4E1423C3-L000252](../../tests/test_generate_index.py#L252) | 252 | `"    assert INDEXER.main([\"--root\", str(tmp_path), \"--check\"]) == 0"` | — |
| [SRC-FA4E1423C3-L000253](../../tests/test_generate_index.py#L253) | 253 | `""` | — |
| [SRC-FA4E1423C3-L000254](../../tests/test_generate_index.py#L254) | 254 | `""` | — |
| [SRC-FA4E1423C3-L000255](../../tests/test_generate_index.py#L255) | 255 | `"def test_indexes_every_eligible_text_line_with_file_and_line_ids(tmp_path: Path) -> None:"` | — |
| [SRC-FA4E1423C3-L000256](../../tests/test_generate_index.py#L256) | 256 | `"    \"\"\"All readable text lines, including blank lines and unfamiliar extensions, are searchable.\"\"\""` | — |
| [SRC-FA4E1423C3-L000257](../../tests/test_generate_index.py#L257) | 257 | `"    (tmp_path / \"app.py\").write_text("` | — |
| [SRC-FA4E1423C3-L000258](../../tests/test_generate_index.py#L258) | 258 | `"        'VALUE = 1\\n\\n'"` | — |
| [SRC-FA4E1423C3-L000259](../../tests/test_generate_index.py#L259) | 259 | `"        'def greet():\\n'"` | — |
| [SRC-FA4E1423C3-L000260](../../tests/test_generate_index.py#L260) | 260 | `"        '    return \"hello\"\\n',"` | — |
| [SRC-FA4E1423C3-L000261](../../tests/test_generate_index.py#L261) | 261 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000262](../../tests/test_generate_index.py#L262) | 262 | `"    )"` | — |
| [SRC-FA4E1423C3-L000263](../../tests/test_generate_index.py#L263) | 263 | `"    docs_dir = tmp_path / \"docs\""` | — |
| [SRC-FA4E1423C3-L000264](../../tests/test_generate_index.py#L264) | 264 | `"    docs_dir.mkdir()"` | — |
| [SRC-FA4E1423C3-L000265](../../tests/test_generate_index.py#L265) | 265 | `"    (docs_dir / \"guide.txt\").write_text("` | — |
| [SRC-FA4E1423C3-L000266](../../tests/test_generate_index.py#L266) | 266 | `"        \"First documented step.\\nSecond documented step.\\n\","` | — |
| [SRC-FA4E1423C3-L000267](../../tests/test_generate_index.py#L267) | 267 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000268](../../tests/test_generate_index.py#L268) | 268 | `"    )"` | — |
| [SRC-FA4E1423C3-L000269](../../tests/test_generate_index.py#L269) | 269 | `"    (tmp_path / \".env\").write_text(\"PRIVATE_TOKEN=do-not-index\\n\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000270](../../tests/test_generate_index.py#L270) | 270 | `"    (tmp_path / \"payload.bin\").write_bytes(b\"\\x00\\x01\\x02\")"` | — |
| [SRC-FA4E1423C3-L000271](../../tests/test_generate_index.py#L271) | 271 | `""` | — |
| [SRC-FA4E1423C3-L000272](../../tests/test_generate_index.py#L272) | 272 | `"    inventory = INDEXER.build_file_inventory(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000273](../../tests/test_generate_index.py#L273) | 273 | `"    source_lines = INDEXER.scan_source_lines(tmp_path, inventory)"` | — |
| [SRC-FA4E1423C3-L000274](../../tests/test_generate_index.py#L274) | 274 | `"    findings = INDEXER.scan_finding_annotations(source_lines)"` | — |
| [SRC-FA4E1423C3-L000275](../../tests/test_generate_index.py#L275) | 275 | `"    line_by_file_and_number = {(line.file, line.line): line for line in source_lines}"` | — |
| [SRC-FA4E1423C3-L000276](../../tests/test_generate_index.py#L276) | 276 | `"    pages, pages_by_file = INDEXER.render_source_line_pages(source_lines, inventory, findings)"` | — |
| [SRC-FA4E1423C3-L000277](../../tests/test_generate_index.py#L277) | 277 | `"    lines_markdown = INDEXER.render_source_lines_markdown("` | — |
| [SRC-FA4E1423C3-L000278](../../tests/test_generate_index.py#L278) | 278 | `"        source_lines, inventory, findings, pages_by_file, pages"` | — |
| [SRC-FA4E1423C3-L000279](../../tests/test_generate_index.py#L279) | 279 | `"    )"` | — |
| [SRC-FA4E1423C3-L000280](../../tests/test_generate_index.py#L280) | 280 | `"    all_page_content = \"\\n\".join(pages.values())"` | — |
| [SRC-FA4E1423C3-L000281](../../tests/test_generate_index.py#L281) | 281 | `""` | — |
| [SRC-FA4E1423C3-L000282](../../tests/test_generate_index.py#L282) | 282 | `"    assert (\"app.py\", 1) in line_by_file_and_number"` | — |
| [SRC-FA4E1423C3-L000283](../../tests/test_generate_index.py#L283) | 283 | `"    assert (\"app.py\", 2) in line_by_file_and_number"` | — |
| [SRC-FA4E1423C3-L000284](../../tests/test_generate_index.py#L284) | 284 | `"    assert line_by_file_and_number[(\"app.py\", 2)].content == \"\""` | — |
| [SRC-FA4E1423C3-L000285](../../tests/test_generate_index.py#L285) | 285 | `"    assert line_by_file_and_number[(\"app.py\", 4)].content == '    return \"hello\"'"` | — |
| [SRC-FA4E1423C3-L000286](../../tests/test_generate_index.py#L286) | 286 | `"    assert line_by_file_and_number[(\"docs/guide.txt\", 2)].content == \"Second documented step.\""` | — |
| [SRC-FA4E1423C3-L000287](../../tests/test_generate_index.py#L287) | 287 | `"    assert line_by_file_and_number[(\"app.py\", 1)].line_id.startswith(\"SRC-\")"` | — |
| [SRC-FA4E1423C3-L000288](../../tests/test_generate_index.py#L288) | 288 | `"    assert line_by_file_and_number[(\"app.py\", 1)].file_id.startswith(\"FILE-\")"` | — |
| [SRC-FA4E1423C3-L000289](../../tests/test_generate_index.py#L289) | 289 | `"    assert line_by_file_and_number[(\"app.py\", 1)].category == \"ملفات أخرى\""` | — |
| [SRC-FA4E1423C3-L000290](../../tests/test_generate_index.py#L290) | 290 | `"    assert \"PRIVATE_TOKEN\" not in lines_markdown"` | — |
| [SRC-FA4E1423C3-L000291](../../tests/test_generate_index.py#L291) | 291 | `"    assert \"payload.bin\" not in {line.file for line in source_lines}"` | — |
| [SRC-FA4E1423C3-L000292](../../tests/test_generate_index.py#L292) | 292 | `"    assert \"Second documented step.\" in all_page_content"` | — |
| [SRC-FA4E1423C3-L000293](../../tests/test_generate_index.py#L293) | 293 | `"    assert \"SRC-\" in all_page_content"` | — |
| [SRC-FA4E1423C3-L000294](../../tests/test_generate_index.py#L294) | 294 | `"    assert \"SOURCE_LINES_001\" in lines_markdown"` | — |
| [SRC-FA4E1423C3-L000295](../../tests/test_generate_index.py#L295) | 295 | `"    assert pages_by_file[\"app.py\"]"` | — |
| [SRC-FA4E1423C3-L000296](../../tests/test_generate_index.py#L296) | 296 | `""` | — |
| [SRC-FA4E1423C3-L000297](../../tests/test_generate_index.py#L297) | 297 | `""` | — |
| [SRC-FA4E1423C3-L000298](../../tests/test_generate_index.py#L298) | 298 | `"def test_explicit_review_markers_have_unique_codes_and_source_line_links("` | — |
| [SRC-FA4E1423C3-L000299](../../tests/test_generate_index.py#L299) | 299 | `"    tmp_path: Path,"` | — |
| [SRC-FA4E1423C3-L000300](../../tests/test_generate_index.py#L300) | 300 | `") -> None:"` | — |
| [SRC-FA4E1423C3-L000301](../../tests/test_generate_index.py#L301) | 301 | `"    \"\"\"TODO/FIXME/BUG-style annotations receive stable named IDs linked to their exact lines.\"\"\""` | — |
| [SRC-FA4E1423C3-L000302](../../tests/test_generate_index.py#L302) | 302 | `"    (tmp_path / \"module.py\").write_text("` | — |
| [SRC-FA4E1423C3-L000303](../../tests/test_generate_index.py#L303) | 303 | `"        \"# TODO: verify fallback\\n\""` | — |
| [SRC-FA4E1423C3-L000304](../../tests/test_generate_index.py#L304) | 304 | `"        \"value = 1  # FIXME: handle overflow\\n\""` | — |
| [SRC-FA4E1423C3-L000305](../../tests/test_generate_index.py#L305) | 305 | `"        \"# SECURITY: check token handling\\n\""` | — |
| [SRC-FA4E1423C3-L000306](../../tests/test_generate_index.py#L306) | 306 | `"        \"def ready():\\n\""` | — |
| [SRC-FA4E1423C3-L000307](../../tests/test_generate_index.py#L307) | 307 | `"        \"    return True\\n\","` | — |
| [SRC-FA4E1423C3-L000308](../../tests/test_generate_index.py#L308) | 308 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000309](../../tests/test_generate_index.py#L309) | 309 | `"    )"` | — |
| [SRC-FA4E1423C3-L000310](../../tests/test_generate_index.py#L310) | 310 | `""` | — |
| [SRC-FA4E1423C3-L000311](../../tests/test_generate_index.py#L311) | 311 | `"    inventory = INDEXER.build_file_inventory(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000312](../../tests/test_generate_index.py#L312) | 312 | `"    source_lines = INDEXER.scan_source_lines(tmp_path, inventory)"` | — |
| [SRC-FA4E1423C3-L000313](../../tests/test_generate_index.py#L313) | 313 | `"    findings = INDEXER.scan_finding_annotations(source_lines)"` | — |
| [SRC-FA4E1423C3-L000314](../../tests/test_generate_index.py#L314) | 314 | `""` | — |
| [SRC-FA4E1423C3-L000315](../../tests/test_generate_index.py#L315) | 315 | `"    assert [item.marker for item in findings] == [\"FIXME\", \"SECURITY\", \"TODO\"]"` | — |
| [SRC-FA4E1423C3-L000316](../../tests/test_generate_index.py#L316) | 316 | `"    assert len({item.finding_id for item in findings}) == 3"` | — |
| [SRC-FA4E1423C3-L000317](../../tests/test_generate_index.py#L317) | 317 | `"    for finding in findings:"` | — |
| [SRC-FA4E1423C3-L000318](../../tests/test_generate_index.py#L318) | 318 | `"        assert finding.finding_id.startswith(f\"FND-{finding.marker}-\")"` | — |
| [SRC-FA4E1423C3-L000319](../../tests/test_generate_index.py#L319) | 319 | `"        assert finding.line_id.startswith(\"SRC-\")"` | — |
| [SRC-FA4E1423C3-L000320](../../tests/test_generate_index.py#L320) | 320 | `"        assert finding.file == \"module.py\""` | — |
| [SRC-FA4E1423C3-L000321](../../tests/test_generate_index.py#L321) | 321 | `""` | — |
| [SRC-FA4E1423C3-L000322](../../tests/test_generate_index.py#L322) | 322 | `""` | — |
| [SRC-FA4E1423C3-L000323](../../tests/test_generate_index.py#L323) | 323 | `"def test_check_mode_validates_all_generated_indexes(tmp_path: Path, capsys) -> None:"` | — |
| [SRC-FA4E1423C3-L000324](../../tests/test_generate_index.py#L324) | 324 | `"    \"\"\"Check mode detects stale master, line, and coverage indexes.\"\"\""` | — |
| [SRC-FA4E1423C3-L000325](../../tests/test_generate_index.py#L325) | 325 | `""` | — |
| [SRC-FA4E1423C3-L000326](../../tests/test_generate_index.py#L326) | 326 | `"    (tmp_path / \"app.py\").write_text(\"VALUE = 1\\n\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000327](../../tests/test_generate_index.py#L327) | 327 | `""` | — |
| [SRC-FA4E1423C3-L000328](../../tests/test_generate_index.py#L328) | 328 | `"    assert INDEXER.main([\"--root\", str(tmp_path)]) == 0"` | — |
| [SRC-FA4E1423C3-L000329](../../tests/test_generate_index.py#L329) | 329 | `"    master_path = tmp_path / INDEXER.INDEX_RELATIVE_PATH"` | — |
| [SRC-FA4E1423C3-L000330](../../tests/test_generate_index.py#L330) | 330 | `"    line_index_path = tmp_path / INDEXER.SOURCE_LINES_INDEX_RELATIVE_PATH"` | — |
| [SRC-FA4E1423C3-L000331](../../tests/test_generate_index.py#L331) | 331 | `"    coverage_path = tmp_path / INDEXER.COVERAGE_AUDIT_RELATIVE_PATH"` | — |
| [SRC-FA4E1423C3-L000332](../../tests/test_generate_index.py#L332) | 332 | `"    assert master_path.exists()"` | — |
| [SRC-FA4E1423C3-L000333](../../tests/test_generate_index.py#L333) | 333 | `"    assert line_index_path.exists()"` | — |
| [SRC-FA4E1423C3-L000334](../../tests/test_generate_index.py#L334) | 334 | `"    assert coverage_path.exists()"` | — |
| [SRC-FA4E1423C3-L000335](../../tests/test_generate_index.py#L335) | 335 | `"    assert INDEXER.main([\"--root\", str(tmp_path), \"--check\"]) == 0"` | — |
| [SRC-FA4E1423C3-L000336](../../tests/test_generate_index.py#L336) | 336 | `""` | — |
| [SRC-FA4E1423C3-L000337](../../tests/test_generate_index.py#L337) | 337 | `"    original_line_index = line_index_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000338](../../tests/test_generate_index.py#L338) | 338 | `"    line_index_path.write_text(\"stale line index\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000339](../../tests/test_generate_index.py#L339) | 339 | `"    assert INDEXER.main([\"--root\", str(tmp_path), \"--check\"]) == 1"` | — |
| [SRC-FA4E1423C3-L000340](../../tests/test_generate_index.py#L340) | 340 | `"    assert line_index_path.read_text(encoding=\"utf-8\") == \"stale line index\""` | — |
| [SRC-FA4E1423C3-L000341](../../tests/test_generate_index.py#L341) | 341 | `"    assert \"فهرس الأسطر قديم\" in capsys.readouterr().err"` | — |
| [SRC-FA4E1423C3-L000342](../../tests/test_generate_index.py#L342) | 342 | `""` | — |
| [SRC-FA4E1423C3-L000343](../../tests/test_generate_index.py#L343) | 343 | `"    line_index_path.write_text(original_line_index, encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000344](../../tests/test_generate_index.py#L344) | 344 | `"    coverage_path.write_text(\"stale coverage audit\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000345](../../tests/test_generate_index.py#L345) | 345 | `"    assert INDEXER.main([\"--root\", str(tmp_path), \"--check\"]) == 1"` | — |
| [SRC-FA4E1423C3-L000346](../../tests/test_generate_index.py#L346) | 346 | `"    assert coverage_path.read_text(encoding=\"utf-8\") == \"stale coverage audit\""` | — |
| [SRC-FA4E1423C3-L000347](../../tests/test_generate_index.py#L347) | 347 | `"    assert \"فهرس تغطية الفهرسة قديم\" in capsys.readouterr().err"` | — |
| [SRC-FA4E1423C3-L000348](../../tests/test_generate_index.py#L348) | 348 | `""` | — |
| [SRC-FA4E1423C3-L000349](../../tests/test_generate_index.py#L349) | 349 | `""` | — |
| [SRC-FA4E1423C3-L000350](../../tests/test_generate_index.py#L350) | 350 | `""` | — |
| [SRC-FA4E1423C3-L000351](../../tests/test_generate_index.py#L351) | 351 | `"def test_source_line_coverage_validator_rejects_missing_or_duplicate_lines(tmp_path: Path) -> None:"` | — |
| [SRC-FA4E1423C3-L000352](../../tests/test_generate_index.py#L352) | 352 | `"    \"\"\"A gap or duplicate in line IDs prevents the generator from claiming full coverage.\"\"\""` | — |
| [SRC-FA4E1423C3-L000353](../../tests/test_generate_index.py#L353) | 353 | `"    source_file = tmp_path / \"src.py\""` | — |
| [SRC-FA4E1423C3-L000354](../../tests/test_generate_index.py#L354) | 354 | `"    source_file.write_text(\"FIRST = 1\\nSECOND = 2\\n\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000355](../../tests/test_generate_index.py#L355) | 355 | `"    inventory = INDEXER.build_file_inventory(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000356](../../tests/test_generate_index.py#L356) | 356 | `"    lines = INDEXER.scan_source_lines(tmp_path, inventory)"` | — |
| [SRC-FA4E1423C3-L000357](../../tests/test_generate_index.py#L357) | 357 | `""` | — |
| [SRC-FA4E1423C3-L000358](../../tests/test_generate_index.py#L358) | 358 | `"    INDEXER.validate_source_line_coverage(tmp_path, inventory, lines)"` | — |
| [SRC-FA4E1423C3-L000359](../../tests/test_generate_index.py#L359) | 359 | `"    with pytest.raises(INDEXER.IndexGenerationError, match=\"اكتمال فهرسة السطور\"):"` | — |
| [SRC-FA4E1423C3-L000360](../../tests/test_generate_index.py#L360) | 360 | `"        INDEXER.validate_source_line_coverage(tmp_path, inventory, lines[:-1])"` | — |
| [SRC-FA4E1423C3-L000361](../../tests/test_generate_index.py#L361) | 361 | `"    with pytest.raises(INDEXER.IndexGenerationError, match=\"معرّف SRC مكرر\"):"` | — |
| [SRC-FA4E1423C3-L000362](../../tests/test_generate_index.py#L362) | 362 | `"        INDEXER.validate_source_line_coverage(tmp_path, inventory, lines + [lines[0]])"` | — |
| [SRC-FA4E1423C3-L000363](../../tests/test_generate_index.py#L363) | 363 | `"    corrupted = [replace(lines[0], content=\"not the source\"), *lines[1:]]"` | — |
| [SRC-FA4E1423C3-L000364](../../tests/test_generate_index.py#L364) | 364 | `"    with pytest.raises(INDEXER.IndexGenerationError, match=\"نص السطر لا يطابق المصدر\"):"` | — |
| [SRC-FA4E1423C3-L000365](../../tests/test_generate_index.py#L365) | 365 | `"        INDEXER.validate_source_line_coverage(tmp_path, inventory, corrupted)"` | — |
| [SRC-FA4E1423C3-L000366](../../tests/test_generate_index.py#L366) | 366 | `""` | — |
| [SRC-FA4E1423C3-L000367](../../tests/test_generate_index.py#L367) | 367 | `""` | — |
| [SRC-FA4E1423C3-L000368](../../tests/test_generate_index.py#L368) | 368 | `"def test_coverage_audit_discloses_metadata_only_and_excluded_paths_without_secrets("` | — |
| [SRC-FA4E1423C3-L000369](../../tests/test_generate_index.py#L369) | 369 | `"    tmp_path: Path,"` | — |
| [SRC-FA4E1423C3-L000370](../../tests/test_generate_index.py#L370) | 370 | `") -> None:"` | — |
| [SRC-FA4E1423C3-L000371](../../tests/test_generate_index.py#L371) | 371 | `"    \"\"\"Coverage report states exact skipped-file reasons without exposing secret contents.\"\"\""` | — |
| [SRC-FA4E1423C3-L000372](../../tests/test_generate_index.py#L372) | 372 | `"    (tmp_path / \"source.py\").write_text(\"VALUE = 7\\n\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000373](../../tests/test_generate_index.py#L373) | 373 | `"    (tmp_path / \".env\").write_text(\"PRIVATE_API_TOKEN=never-print-this-secret\\n\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000374](../../tests/test_generate_index.py#L374) | 374 | `"    (tmp_path / \"large.txt\").write_bytes(b\"x\" * (INDEXER.MAX_INDEXED_TEXT_BYTES + 1))"` | — |
| [SRC-FA4E1423C3-L000375](../../tests/test_generate_index.py#L375) | 375 | `"    (tmp_path / \".venv\" / \"lib\").mkdir(parents=True)"` | — |
| [SRC-FA4E1423C3-L000376](../../tests/test_generate_index.py#L376) | 376 | `"    (tmp_path / \".venv\" / \"lib\" / \"hidden.py\").write_text(\"PRIVATE = True\\n\", encoding=\"utf-8\")"` | — |
| [SRC-FA4E1423C3-L000377](../../tests/test_generate_index.py#L377) | 377 | `""` | — |
| [SRC-FA4E1423C3-L000378](../../tests/test_generate_index.py#L378) | 378 | `"    inventory = INDEXER.build_file_inventory(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000379](../../tests/test_generate_index.py#L379) | 379 | `"    lines = INDEXER.scan_source_lines(tmp_path, inventory)"` | — |
| [SRC-FA4E1423C3-L000380](../../tests/test_generate_index.py#L380) | 380 | `"    INDEXER.validate_source_line_coverage(tmp_path, inventory, lines)"` | — |
| [SRC-FA4E1423C3-L000381](../../tests/test_generate_index.py#L381) | 381 | `"    exclusions = INDEXER.discover_excluded_paths(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000382](../../tests/test_generate_index.py#L382) | 382 | `"    report = INDEXER.render_coverage_audit_markdown(tmp_path, inventory, lines, exclusions)"` | — |
| [SRC-FA4E1423C3-L000383](../../tests/test_generate_index.py#L383) | 383 | `""` | — |
| [SRC-FA4E1423C3-L000384](../../tests/test_generate_index.py#L384) | 384 | `"    assert \"100.00%\" in report"` | — |
| [SRC-FA4E1423C3-L000385](../../tests/test_generate_index.py#L385) | 385 | `"    assert \"large.txt\" in report"` | — |
| [SRC-FA4E1423C3-L000386](../../tests/test_generate_index.py#L386) | 386 | `"    assert f\"يتجاوز حد الفهرسة ({INDEXER.MAX_INDEXED_TEXT_BYTES} بايت)\" in report"` | — |
| [SRC-FA4E1423C3-L000387](../../tests/test_generate_index.py#L387) | 387 | `"    assert \".env\" in report"` | — |
| [SRC-FA4E1423C3-L000388](../../tests/test_generate_index.py#L388) | 388 | `"    assert \".venv/\" in report"` | — |
| [SRC-FA4E1423C3-L000389](../../tests/test_generate_index.py#L389) | 389 | `"    assert \"لم تُقرأ محتوياته\" in report"` | — |
| [SRC-FA4E1423C3-L000390](../../tests/test_generate_index.py#L390) | 390 | `"    assert \"never-print-this-secret\" not in report"` | — |
| [SRC-FA4E1423C3-L000391](../../tests/test_generate_index.py#L391) | 391 | `"    assert \"PRIVATE_API_TOKEN\" not in report"` | — |
| [SRC-FA4E1423C3-L000392](../../tests/test_generate_index.py#L392) | 392 | `"    assert \"PRIVATE = True\" not in report"` | — |
| [SRC-FA4E1423C3-L000393](../../tests/test_generate_index.py#L393) | 393 | `""` | — |
| [SRC-FA4E1423C3-L000394](../../tests/test_generate_index.py#L394) | 394 | `""` | — |
| [SRC-FA4E1423C3-L000395](../../tests/test_generate_index.py#L395) | 395 | `"def test_multiple_review_markers_on_one_line_each_get_a_unique_finding_code("` | — |
| [SRC-FA4E1423C3-L000396](../../tests/test_generate_index.py#L396) | 396 | `"    tmp_path: Path,"` | — |
| [SRC-FA4E1423C3-L000397](../../tests/test_generate_index.py#L397) | 397 | `") -> None:"` | — |
| [SRC-FA4E1423C3-L000398](../../tests/test_generate_index.py#L398) | 398 | `"    \"\"\"Different and repeated review tags on a single line must not overwrite each other.\"\"\""` | — |
| [SRC-FA4E1423C3-L000399](../../tests/test_generate_index.py#L399) | 399 | `"    source_file = tmp_path / \"module.py\""` | — |
| [SRC-FA4E1423C3-L000400](../../tests/test_generate_index.py#L400) | 400 | `"    source_file.write_text("` | — |
| [SRC-FA4E1423C3-L000401](../../tests/test_generate_index.py#L401) | 401 | `"        \"# BUG: first defect; FIXME: repair it; BUG: second defect\\n\","` | — |
| [SRC-FA4E1423C3-L000402](../../tests/test_generate_index.py#L402) | 402 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000403](../../tests/test_generate_index.py#L403) | 403 | `"    )"` | — |
| [SRC-FA4E1423C3-L000404](../../tests/test_generate_index.py#L404) | 404 | `""` | — |
| [SRC-FA4E1423C3-L000405](../../tests/test_generate_index.py#L405) | 405 | `"    inventory = INDEXER.build_file_inventory(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000406](../../tests/test_generate_index.py#L406) | 406 | `"    source_lines = INDEXER.scan_source_lines(tmp_path, inventory)"` | — |
| [SRC-FA4E1423C3-L000407](../../tests/test_generate_index.py#L407) | 407 | `"    findings = INDEXER.scan_finding_annotations(source_lines)"` | — |
| [SRC-FA4E1423C3-L000408](../../tests/test_generate_index.py#L408) | 408 | `"    pages, _ = INDEXER.render_source_line_pages(source_lines, inventory, findings)"` | — |
| [SRC-FA4E1423C3-L000409](../../tests/test_generate_index.py#L409) | 409 | `""` | — |
| [SRC-FA4E1423C3-L000410](../../tests/test_generate_index.py#L410) | 410 | `"    assert len(findings) == 3"` | — |
| [SRC-FA4E1423C3-L000411](../../tests/test_generate_index.py#L411) | 411 | `"    assert {item.marker for item in findings} == {\"BUG\", \"FIXME\"}"` | — |
| [SRC-FA4E1423C3-L000412](../../tests/test_generate_index.py#L412) | 412 | `"    assert len({item.finding_id for item in findings}) == 3"` | — |
| [SRC-FA4E1423C3-L000413](../../tests/test_generate_index.py#L413) | 413 | `"    bug_ids = [item.finding_id for item in findings if item.marker == \"BUG\"]"` | — |
| [SRC-FA4E1423C3-L000414](../../tests/test_generate_index.py#L414) | 414 | `"    assert any(item.endswith(\"-M01\") for item in bug_ids)"` | — |
| [SRC-FA4E1423C3-L000415](../../tests/test_generate_index.py#L415) | 415 | `"    assert any(item.endswith(\"-M02\") for item in bug_ids)"` | — |
| [SRC-FA4E1423C3-L000416](../../tests/test_generate_index.py#L416) | 416 | `"    page_content = \"\\n\".join(pages.values())"` | — |
| [SRC-FA4E1423C3-L000417](../../tests/test_generate_index.py#L417) | 417 | `"    assert all(item.finding_id in page_content for item in findings)"` | — |
| [SRC-FA4E1423C3-L000418](../../tests/test_generate_index.py#L418) | 418 | `""` | — |
| [SRC-FA4E1423C3-L000419](../../tests/test_generate_index.py#L419) | 419 | `""` | — |
| [SRC-FA4E1423C3-L000420](../../tests/test_generate_index.py#L420) | 420 | `"def test_finding_scan_ignores_incidental_words_but_finds_real_annotations("` | — |
| [SRC-FA4E1423C3-L000421](../../tests/test_generate_index.py#L421) | 421 | `"    tmp_path: Path,"` | — |
| [SRC-FA4E1423C3-L000422](../../tests/test_generate_index.py#L422) | 422 | `") -> None:"` | — |
| [SRC-FA4E1423C3-L000423](../../tests/test_generate_index.py#L423) | 423 | `"    \"\"\"Only explicit comment or prose markers become findings, never syntax/URLs/strings.\"\"\""` | — |
| [SRC-FA4E1423C3-L000424](../../tests/test_generate_index.py#L424) | 424 | `"    (tmp_path / \"sample.py\").write_text("` | — |
| [SRC-FA4E1423C3-L000425](../../tests/test_generate_index.py#L425) | 425 | `"        'framework_url = \"https://example.org/risk-management-framework\"\\n'"` | — |
| [SRC-FA4E1423C3-L000426](../../tests/test_generate_index.py#L426) | 426 | `"        'error = \"ordinary error variable\"\\n'"` | — |
| [SRC-FA4E1423C3-L000427](../../tests/test_generate_index.py#L427) | 427 | `"        'template = \"# BUG: this is inside a string\"\\n'"` | — |
| [SRC-FA4E1423C3-L000428](../../tests/test_generate_index.py#L428) | 428 | `"        '# BUG: real Python defect\\n',"` | — |
| [SRC-FA4E1423C3-L000429](../../tests/test_generate_index.py#L429) | 429 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000430](../../tests/test_generate_index.py#L430) | 430 | `"    )"` | — |
| [SRC-FA4E1423C3-L000431](../../tests/test_generate_index.py#L431) | 431 | `"    (tmp_path / \"app.js\").write_text("` | — |
| [SRC-FA4E1423C3-L000432](../../tests/test_generate_index.py#L432) | 432 | `"        'const template = \"// BUG: not a comment\";\\n'"` | — |
| [SRC-FA4E1423C3-L000433](../../tests/test_generate_index.py#L433) | 433 | `"        'const error = 1;\\n'"` | — |
| [SRC-FA4E1423C3-L000434](../../tests/test_generate_index.py#L434) | 434 | `"        'const x = 2; // FIXME: actual JS issue\\n'"` | — |
| [SRC-FA4E1423C3-L000435](../../tests/test_generate_index.py#L435) | 435 | `"        '/* SECURITY: actual CSS/JS comment issue */\\n',"` | — |
| [SRC-FA4E1423C3-L000436](../../tests/test_generate_index.py#L436) | 436 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000437](../../tests/test_generate_index.py#L437) | 437 | `"    )"` | — |
| [SRC-FA4E1423C3-L000438](../../tests/test_generate_index.py#L438) | 438 | `"    (tmp_path / \"styles.css\").write_text("` | — |
| [SRC-FA4E1423C3-L000439](../../tests/test_generate_index.py#L439) | 439 | `"        \".box{gap:8px;color:red}\\n\""` | — |
| [SRC-FA4E1423C3-L000440](../../tests/test_generate_index.py#L440) | 440 | `"        \"/* GAP: deliberate comment annotation */\\n\","` | — |
| [SRC-FA4E1423C3-L000441](../../tests/test_generate_index.py#L441) | 441 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000442](../../tests/test_generate_index.py#L442) | 442 | `"    )"` | — |
| [SRC-FA4E1423C3-L000443](../../tests/test_generate_index.py#L443) | 443 | `"    (tmp_path / \"page.html\").write_text("` | — |
| [SRC-FA4E1423C3-L000444](../../tests/test_generate_index.py#L444) | 444 | `"        '<!-- REVIEW: check the navigation landmark -->\\n'"` | — |
| [SRC-FA4E1423C3-L000445](../../tests/test_generate_index.py#L445) | 445 | `"        '<script>const template = \"<!-- BUG: not a markup comment -->\";</script>\\n',"` | — |
| [SRC-FA4E1423C3-L000446](../../tests/test_generate_index.py#L446) | 446 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000447](../../tests/test_generate_index.py#L447) | 447 | `"    )"` | — |
| [SRC-FA4E1423C3-L000448](../../tests/test_generate_index.py#L448) | 448 | `"    (tmp_path / \"guide.md\").write_text("` | — |
| [SRC-FA4E1423C3-L000449](../../tests/test_generate_index.py#L449) | 449 | `"        \"The risk-management framework reports an error.\\n\""` | — |
| [SRC-FA4E1423C3-L000450](../../tests/test_generate_index.py#L450) | 450 | ````"        \"```text\\n\""```` | — |
| [SRC-FA4E1423C3-L000451](../../tests/test_generate_index.py#L451) | 451 | `"        \"# BUG: this sample should be ignored\\n\""` | — |
| [SRC-FA4E1423C3-L000452](../../tests/test_generate_index.py#L452) | 452 | ````"        \"```\\n\""```` | — |
| [SRC-FA4E1423C3-L000453](../../tests/test_generate_index.py#L453) | 453 | `"        \"- DEFECT: this explicitly documented defect should be indexed\\n\","` | — |
| [SRC-FA4E1423C3-L000454](../../tests/test_generate_index.py#L454) | 454 | `"        encoding=\"utf-8\","` | — |
| [SRC-FA4E1423C3-L000455](../../tests/test_generate_index.py#L455) | 455 | `"    )"` | — |
| [SRC-FA4E1423C3-L000456](../../tests/test_generate_index.py#L456) | 456 | `""` | — |
| [SRC-FA4E1423C3-L000457](../../tests/test_generate_index.py#L457) | 457 | `"    inventory = INDEXER.build_file_inventory(tmp_path)"` | — |
| [SRC-FA4E1423C3-L000458](../../tests/test_generate_index.py#L458) | 458 | `"    source_lines = INDEXER.scan_source_lines(tmp_path, inventory)"` | — |
| [SRC-FA4E1423C3-L000459](../../tests/test_generate_index.py#L459) | 459 | `"    findings = INDEXER.scan_finding_annotations(source_lines)"` | — |
| [SRC-FA4E1423C3-L000460](../../tests/test_generate_index.py#L460) | 460 | `"    summarized = {(item.file, item.marker, item.description) for item in findings}"` | — |
| [SRC-FA4E1423C3-L000461](../../tests/test_generate_index.py#L461) | 461 | `""` | — |
| [SRC-FA4E1423C3-L000462](../../tests/test_generate_index.py#L462) | 462 | `"    assert {item.marker for item in findings} == {"` | — |
| [SRC-FA4E1423C3-L000463](../../tests/test_generate_index.py#L463) | 463 | `"        \"BUG\", \"FIXME\", \"SECURITY\", \"GAP\", \"REVIEW\", \"DEFECT\""` | — |
| [SRC-FA4E1423C3-L000464](../../tests/test_generate_index.py#L464) | 464 | `"    }"` | — |
| [SRC-FA4E1423C3-L000465](../../tests/test_generate_index.py#L465) | 465 | `"    assert any(path == \"sample.py\" and marker == \"BUG\" and \"real Python defect\" in desc"` | — |
| [SRC-FA4E1423C3-L000466](../../tests/test_generate_index.py#L466) | 466 | `"               for path, marker, desc in summarized)"` | — |
| [SRC-FA4E1423C3-L000467](../../tests/test_generate_index.py#L467) | 467 | `"    assert any(path == \"app.js\" and marker == \"FIXME\" for path, marker, _ in summarized)"` | — |
| [SRC-FA4E1423C3-L000468](../../tests/test_generate_index.py#L468) | 468 | `"    assert any(path == \"app.js\" and marker == \"SECURITY\" for path, marker, _ in summarized)"` | — |
| [SRC-FA4E1423C3-L000469](../../tests/test_generate_index.py#L469) | 469 | `"    assert any(path == \"styles.css\" and marker == \"GAP\" for path, marker, _ in summarized)"` | — |
| [SRC-FA4E1423C3-L000470](../../tests/test_generate_index.py#L470) | 470 | `"    assert any(path == \"page.html\" and marker == \"REVIEW\" for path, marker, _ in summarized)"` | — |
| [SRC-FA4E1423C3-L000471](../../tests/test_generate_index.py#L471) | 471 | `"    assert any(path == \"guide.md\" and marker == \"DEFECT\" for path, marker, _ in summarized)"` | — |
| [SRC-FA4E1423C3-L000472](../../tests/test_generate_index.py#L472) | 472 | `"    assert not any(\"risk-management\" in desc.lower() for _, _, desc in summarized)"` | — |
| [SRC-FA4E1423C3-L000473](../../tests/test_generate_index.py#L473) | 473 | `"    assert not any(\"ordinary error variable\" in desc for _, _, desc in summarized)"` | — |
| [SRC-FA4E1423C3-L000474](../../tests/test_generate_index.py#L474) | 474 | `"    assert not any(\"inside a string\" in desc for _, _, desc in summarized)"` | — |
| [SRC-FA4E1423C3-L000475](../../tests/test_generate_index.py#L475) | 475 | `"    assert not any(\"sample should be ignored\" in desc for _, _, desc in summarized)"` | — |
## اختبارات

### FILE-829A979985 — [tests/test_generation_acceptance_matrix.py](../../tests/test_generation_acceptance_matrix.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-829A979985-L000001](../../tests/test_generation_acceptance_matrix.py#L1) | 1 | `"from __future__ import annotations"` | — |
| [SRC-829A979985-L000002](../../tests/test_generation_acceptance_matrix.py#L2) | 2 | `""` | — |
| [SRC-829A979985-L000003](../../tests/test_generation_acceptance_matrix.py#L3) | 3 | `"import json"` | — |
| [SRC-829A979985-L000004](../../tests/test_generation_acceptance_matrix.py#L4) | 4 | `""` | — |
| [SRC-829A979985-L000005](../../tests/test_generation_acceptance_matrix.py#L5) | 5 | `"import pytest"` | — |
| [SRC-829A979985-L000006](../../tests/test_generation_acceptance_matrix.py#L6) | 6 | `""` | — |
| [SRC-829A979985-L000007](../../tests/test_generation_acceptance_matrix.py#L7) | 7 | `"from agents.request_budget import RequestBudget, RequestBudgetExceeded"` | — |
| [SRC-829A979985-L000008](../../tests/test_generation_acceptance_matrix.py#L8) | 8 | `"from agents.web_agent import WebAgent"` | — |
| [SRC-829A979985-L000009](../../tests/test_generation_acceptance_matrix.py#L9) | 9 | `""` | — |
| [SRC-829A979985-L000010](../../tests/test_generation_acceptance_matrix.py#L10) | 10 | `""` | — |
| [SRC-829A979985-L000011](../../tests/test_generation_acceptance_matrix.py#L11) | 11 | `"class FakeCompletionResponse:"` | — |
| [SRC-829A979985-L000012](../../tests/test_generation_acceptance_matrix.py#L12) | 12 | `"    def __init__("` | — |
| [SRC-829A979985-L000013](../../tests/test_generation_acceptance_matrix.py#L13) | 13 | `"        self,"` | — |
| [SRC-829A979985-L000014](../../tests/test_generation_acceptance_matrix.py#L14) | 14 | `"        content: str,"` | — |
| [SRC-829A979985-L000015](../../tests/test_generation_acceptance_matrix.py#L15) | 15 | `"        finish_reason: str \| None,"` | — |
| [SRC-829A979985-L000016](../../tests/test_generation_acceptance_matrix.py#L16) | 16 | `"        *,"` | — |
| [SRC-829A979985-L000017](../../tests/test_generation_acceptance_matrix.py#L17) | 17 | `"        include_reason: bool = True,"` | — |
| [SRC-829A979985-L000018](../../tests/test_generation_acceptance_matrix.py#L18) | 18 | `"    ) -> None:"` | — |
| [SRC-829A979985-L000019](../../tests/test_generation_acceptance_matrix.py#L19) | 19 | `"        choice = {\"message\": {\"content\": content}}"` | — |
| [SRC-829A979985-L000020](../../tests/test_generation_acceptance_matrix.py#L20) | 20 | `"        if include_reason:"` | — |
| [SRC-829A979985-L000021](../../tests/test_generation_acceptance_matrix.py#L21) | 21 | `"            choice[\"finish_reason\"] = finish_reason"` | — |
| [SRC-829A979985-L000022](../../tests/test_generation_acceptance_matrix.py#L22) | 22 | `"        self.body = json.dumps({\"choices\": [choice]}).encode(\"utf-8\")"` | — |
| [SRC-829A979985-L000023](../../tests/test_generation_acceptance_matrix.py#L23) | 23 | `""` | — |
| [SRC-829A979985-L000024](../../tests/test_generation_acceptance_matrix.py#L24) | 24 | `"    def __enter__(self):"` | — |
| [SRC-829A979985-L000025](../../tests/test_generation_acceptance_matrix.py#L25) | 25 | `"        return self"` | — |
| [SRC-829A979985-L000026](../../tests/test_generation_acceptance_matrix.py#L26) | 26 | `""` | — |
| [SRC-829A979985-L000027](../../tests/test_generation_acceptance_matrix.py#L27) | 27 | `"    def __exit__(self, exc_type, exc, traceback):"` | — |
| [SRC-829A979985-L000028](../../tests/test_generation_acceptance_matrix.py#L28) | 28 | `"        return False"` | — |
| [SRC-829A979985-L000029](../../tests/test_generation_acceptance_matrix.py#L29) | 29 | `""` | — |
| [SRC-829A979985-L000030](../../tests/test_generation_acceptance_matrix.py#L30) | 30 | `"    def read(self, limit: int) -> bytes:"` | — |
| [SRC-829A979985-L000031](../../tests/test_generation_acceptance_matrix.py#L31) | 31 | `"        return self.body[:limit]"` | — |
| [SRC-829A979985-L000032](../../tests/test_generation_acceptance_matrix.py#L32) | 32 | `""` | — |
| [SRC-829A979985-L000033](../../tests/test_generation_acceptance_matrix.py#L33) | 33 | `""` | — |
| [SRC-829A979985-L000034](../../tests/test_generation_acceptance_matrix.py#L34) | 34 | `"def source("` | — |
| [SRC-829A979985-L000035](../../tests/test_generation_acceptance_matrix.py#L35) | 35 | `"    url: str,"` | — |
| [SRC-829A979985-L000036](../../tests/test_generation_acceptance_matrix.py#L36) | 36 | `"    domain: str,"` | — |
| [SRC-829A979985-L000037](../../tests/test_generation_acceptance_matrix.py#L37) | 37 | `"    *,"` | — |
| [SRC-829A979985-L000038](../../tests/test_generation_acceptance_matrix.py#L38) | 38 | `"    page_fetched: bool,"` | — |
| [SRC-829A979985-L000039](../../tests/test_generation_acceptance_matrix.py#L39) | 39 | `"    page_text: str = \"\","` | — |
| [SRC-829A979985-L000040](../../tests/test_generation_acceptance_matrix.py#L40) | 40 | `"    snippet: str = \"\","` | — |
| [SRC-829A979985-L000041](../../tests/test_generation_acceptance_matrix.py#L41) | 41 | `"    provider: str = \"test_provider\","` | — |
| [SRC-829A979985-L000042](../../tests/test_generation_acceptance_matrix.py#L42) | 42 | `") -> dict:"` | — |
| [SRC-829A979985-L000043](../../tests/test_generation_acceptance_matrix.py#L43) | 43 | `"    return {"` | — |
| [SRC-829A979985-L000044](../../tests/test_generation_acceptance_matrix.py#L44) | 44 | `"        \"title\": f\"نتيجة عن {domain}\","` | — |
| [SRC-829A979985-L000045](../../tests/test_generation_acceptance_matrix.py#L45) | 45 | `"        \"url\": url,"` | — |
| [SRC-829A979985-L000046](../../tests/test_generation_acceptance_matrix.py#L46) | 46 | `"        \"snippet\": snippet or page_text[:200],"` | — |
| [SRC-829A979985-L000047](../../tests/test_generation_acceptance_matrix.py#L47) | 47 | `"        \"page_text\": page_text,"` | — |
| [SRC-829A979985-L000048](../../tests/test_generation_acceptance_matrix.py#L48) | 48 | `"        \"page_fetched\": page_fetched,"` | — |
| [SRC-829A979985-L000049](../../tests/test_generation_acceptance_matrix.py#L49) | 49 | `"        \"providers\": [provider],"` | — |
| [SRC-829A979985-L000050](../../tests/test_generation_acceptance_matrix.py#L50) | 50 | `"        \"queries\": [\"قارن بين سعر المنتج ومساحته\"],"` | — |
| [SRC-829A979985-L000051](../../tests/test_generation_acceptance_matrix.py#L51) | 51 | `"        \"domain\": domain,"` | — |
| [SRC-829A979985-L000052](../../tests/test_generation_acceptance_matrix.py#L52) | 52 | `"        \"source_class\": \"general\","` | — |
| [SRC-829A979985-L000053](../../tests/test_generation_acceptance_matrix.py#L53) | 53 | `"        \"platform\": \"web\","` | — |
| [SRC-829A979985-L000054](../../tests/test_generation_acceptance_matrix.py#L54) | 54 | `"        \"published_at\": \"\","` | — |
| [SRC-829A979985-L000055](../../tests/test_generation_acceptance_matrix.py#L55) | 55 | `"        \"rank_score\": 0.8,"` | — |
| [SRC-829A979985-L000056](../../tests/test_generation_acceptance_matrix.py#L56) | 56 | `"    }"` | — |
| [SRC-829A979985-L000057](../../tests/test_generation_acceptance_matrix.py#L57) | 57 | `""` | — |
| [SRC-829A979985-L000058](../../tests/test_generation_acceptance_matrix.py#L58) | 58 | `""` | — |
| [SRC-829A979985-L000059](../../tests/test_generation_acceptance_matrix.py#L59) | 59 | `"@pytest.mark.parametrize("` | — |
| [SRC-829A979985-L000060](../../tests/test_generation_acceptance_matrix.py#L60) | 60 | `"    \"finish_reason\","` | — |
| [SRC-829A979985-L000061](../../tests/test_generation_acceptance_matrix.py#L61) | 61 | `"    [\"tool_calls\", \"function_call\", \"error\", \"abort\", \"cancelled\", \"vendor_specific_done\"],"` | — |
| [SRC-829A979985-L000062](../../tests/test_generation_acceptance_matrix.py#L62) | 62 | `")"` | — |
| [SRC-829A979985-L000063](../../tests/test_generation_acceptance_matrix.py#L63) | 63 | `"def test_only_normal_stop_is_accepted_as_a_complete_text_answer("` | — |
| [SRC-829A979985-L000064](../../tests/test_generation_acceptance_matrix.py#L64) | 64 | `"    monkeypatch, finish_reason"` | — |
| [SRC-829A979985-L000065](../../tests/test_generation_acceptance_matrix.py#L65) | 65 | `"):"` | — |
| [SRC-829A979985-L000066](../../tests/test_generation_acceptance_matrix.py#L66) | 66 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000067](../../tests/test_generation_acceptance_matrix.py#L67) | 67 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-829A979985-L000068](../../tests/test_generation_acceptance_matrix.py#L68) | 68 | `"    agent.fallback_model = \"\""` | — |
| [SRC-829A979985-L000069](../../tests/test_generation_acceptance_matrix.py#L69) | 69 | `"    partial_text = \"نص لا يجب قبوله كإجابة نهائية\""` | — |
| [SRC-829A979985-L000070](../../tests/test_generation_acceptance_matrix.py#L70) | 70 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000071](../../tests/test_generation_acceptance_matrix.py#L71) | 71 | `"        \"agents.web_agent.urllib.request.urlopen\","` | — |
| [SRC-829A979985-L000072](../../tests/test_generation_acceptance_matrix.py#L72) | 72 | `"        lambda request, timeout: FakeCompletionResponse(partial_text, finish_reason),"` | — |
| [SRC-829A979985-L000073](../../tests/test_generation_acceptance_matrix.py#L73) | 73 | `"    )"` | — |
| [SRC-829A979985-L000074](../../tests/test_generation_acceptance_matrix.py#L74) | 74 | `""` | — |
| [SRC-829A979985-L000075](../../tests/test_generation_acceptance_matrix.py#L75) | 75 | `"    with pytest.raises(RuntimeError):"` | — |
| [SRC-829A979985-L000076](../../tests/test_generation_acceptance_matrix.py#L76) | 76 | `"        agent._request_completion("` | — |
| [SRC-829A979985-L000077](../../tests/test_generation_acceptance_matrix.py#L77) | 77 | `"            [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-829A979985-L000078](../../tests/test_generation_acceptance_matrix.py#L78) | 78 | `"            model=\"primary/model\","` | — |
| [SRC-829A979985-L000079](../../tests/test_generation_acceptance_matrix.py#L79) | 79 | `"        )"` | — |
| [SRC-829A979985-L000080](../../tests/test_generation_acceptance_matrix.py#L80) | 80 | `""` | — |
| [SRC-829A979985-L000081](../../tests/test_generation_acceptance_matrix.py#L81) | 81 | `"    assert agent.model_usage == []"` | — |
| [SRC-829A979985-L000082](../../tests/test_generation_acceptance_matrix.py#L82) | 82 | `"    assert agent.generation_diagnostics == ["` | — |
| [SRC-829A979985-L000083](../../tests/test_generation_acceptance_matrix.py#L83) | 83 | `"        {"` | — |
| [SRC-829A979985-L000084](../../tests/test_generation_acceptance_matrix.py#L84) | 84 | `"            \"requested_model\": \"primary/model\","` | — |
| [SRC-829A979985-L000085](../../tests/test_generation_acceptance_matrix.py#L85) | 85 | `"            \"attempted_model\": \"primary/model\","` | — |
| [SRC-829A979985-L000086](../../tests/test_generation_acceptance_matrix.py#L86) | 86 | `"            \"status\": \"finish_reason_not_accepted\","` | — |
| [SRC-829A979985-L000087](../../tests/test_generation_acceptance_matrix.py#L87) | 87 | `"            \"finish_reason\": finish_reason,"` | — |
| [SRC-829A979985-L000088](../../tests/test_generation_acceptance_matrix.py#L88) | 88 | `"        }"` | — |
| [SRC-829A979985-L000089](../../tests/test_generation_acceptance_matrix.py#L89) | 89 | `"    ]"` | — |
| [SRC-829A979985-L000090](../../tests/test_generation_acceptance_matrix.py#L90) | 90 | `""` | — |
| [SRC-829A979985-L000091](../../tests/test_generation_acceptance_matrix.py#L91) | 91 | `""` | — |
| [SRC-829A979985-L000092](../../tests/test_generation_acceptance_matrix.py#L92) | 92 | `"def test_both_models_truncated_fail_without_returning_either_partial_answer(monkeypatch):"` | — |
| [SRC-829A979985-L000093](../../tests/test_generation_acceptance_matrix.py#L93) | 93 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000094](../../tests/test_generation_acceptance_matrix.py#L94) | 94 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-829A979985-L000095](../../tests/test_generation_acceptance_matrix.py#L95) | 95 | `"    agent.fallback_model = \"fallback/model\""` | — |
| [SRC-829A979985-L000096](../../tests/test_generation_acceptance_matrix.py#L96) | 96 | `"    calls: list[str] = []"` | — |
| [SRC-829A979985-L000097](../../tests/test_generation_acceptance_matrix.py#L97) | 97 | `""` | — |
| [SRC-829A979985-L000098](../../tests/test_generation_acceptance_matrix.py#L98) | 98 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-829A979985-L000099](../../tests/test_generation_acceptance_matrix.py#L99) | 99 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-829A979985-L000100](../../tests/test_generation_acceptance_matrix.py#L100) | 100 | `"        calls.append(model)"` | — |
| [SRC-829A979985-L000101](../../tests/test_generation_acceptance_matrix.py#L101) | 101 | `"        return FakeCompletionResponse(f\"نص مبتور من {model}\", \"length\")"` | — |
| [SRC-829A979985-L000102](../../tests/test_generation_acceptance_matrix.py#L102) | 102 | `""` | — |
| [SRC-829A979985-L000103](../../tests/test_generation_acceptance_matrix.py#L103) | 103 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-829A979985-L000104](../../tests/test_generation_acceptance_matrix.py#L104) | 104 | `""` | — |
| [SRC-829A979985-L000105](../../tests/test_generation_acceptance_matrix.py#L105) | 105 | `"    with pytest.raises(RuntimeError, match=\"مبتورة\"):"` | — |
| [SRC-829A979985-L000106](../../tests/test_generation_acceptance_matrix.py#L106) | 106 | `"        agent._request_completion("` | — |
| [SRC-829A979985-L000107](../../tests/test_generation_acceptance_matrix.py#L107) | 107 | `"            [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-829A979985-L000108](../../tests/test_generation_acceptance_matrix.py#L108) | 108 | `"            model=\"primary/model\","` | — |
| [SRC-829A979985-L000109](../../tests/test_generation_acceptance_matrix.py#L109) | 109 | `"        )"` | — |
| [SRC-829A979985-L000110](../../tests/test_generation_acceptance_matrix.py#L110) | 110 | `""` | — |
| [SRC-829A979985-L000111](../../tests/test_generation_acceptance_matrix.py#L111) | 111 | `"    assert calls == [\"primary/model\", \"fallback/model\"]"` | — |
| [SRC-829A979985-L000112](../../tests/test_generation_acceptance_matrix.py#L112) | 112 | `"    assert agent.model_usage == []"` | — |
| [SRC-829A979985-L000113](../../tests/test_generation_acceptance_matrix.py#L113) | 113 | `"    assert [item[\"status\"] for item in agent.generation_diagnostics] == ["` | — |
| [SRC-829A979985-L000114](../../tests/test_generation_acceptance_matrix.py#L114) | 114 | `"        \"truncated\","` | — |
| [SRC-829A979985-L000115](../../tests/test_generation_acceptance_matrix.py#L115) | 115 | `"        \"truncated\","` | — |
| [SRC-829A979985-L000116](../../tests/test_generation_acceptance_matrix.py#L116) | 116 | `"    ]"` | — |
| [SRC-829A979985-L000117](../../tests/test_generation_acceptance_matrix.py#L117) | 117 | `"    assert all(\"مبتور\" not in str(item) for item in agent.generation_diagnostics)"` | — |
| [SRC-829A979985-L000118](../../tests/test_generation_acceptance_matrix.py#L118) | 118 | `""` | — |
| [SRC-829A979985-L000119](../../tests/test_generation_acceptance_matrix.py#L119) | 119 | `""` | — |
| [SRC-829A979985-L000120](../../tests/test_generation_acceptance_matrix.py#L120) | 120 | `"def test_model_fallback_cannot_exceed_request_model_call_budget(monkeypatch):"` | — |
| [SRC-829A979985-L000121](../../tests/test_generation_acceptance_matrix.py#L121) | 121 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000122](../../tests/test_generation_acceptance_matrix.py#L122) | 122 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-829A979985-L000123](../../tests/test_generation_acceptance_matrix.py#L123) | 123 | `"    agent.fallback_model = \"fallback/model\""` | — |
| [SRC-829A979985-L000124](../../tests/test_generation_acceptance_matrix.py#L124) | 124 | `"    budget = RequestBudget(timeout_seconds=60, limits={\"model_calls\": 1})"` | — |
| [SRC-829A979985-L000125](../../tests/test_generation_acceptance_matrix.py#L125) | 125 | `"    agent._request_budget = budget"` | — |
| [SRC-829A979985-L000126](../../tests/test_generation_acceptance_matrix.py#L126) | 126 | `"    calls: list[str] = []"` | — |
| [SRC-829A979985-L000127](../../tests/test_generation_acceptance_matrix.py#L127) | 127 | `""` | — |
| [SRC-829A979985-L000128](../../tests/test_generation_acceptance_matrix.py#L128) | 128 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-829A979985-L000129](../../tests/test_generation_acceptance_matrix.py#L129) | 129 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-829A979985-L000130](../../tests/test_generation_acceptance_matrix.py#L130) | 130 | `"        calls.append(model)"` | — |
| [SRC-829A979985-L000131](../../tests/test_generation_acceptance_matrix.py#L131) | 131 | `"        return FakeCompletionResponse(\"محتوى مبتور\", \"length\")"` | — |
| [SRC-829A979985-L000132](../../tests/test_generation_acceptance_matrix.py#L132) | 132 | `""` | — |
| [SRC-829A979985-L000133](../../tests/test_generation_acceptance_matrix.py#L133) | 133 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-829A979985-L000134](../../tests/test_generation_acceptance_matrix.py#L134) | 134 | `""` | — |
| [SRC-829A979985-L000135](../../tests/test_generation_acceptance_matrix.py#L135) | 135 | `"    with pytest.raises(RequestBudgetExceeded):"` | — |
| [SRC-829A979985-L000136](../../tests/test_generation_acceptance_matrix.py#L136) | 136 | `"        agent._request_completion("` | — |
| [SRC-829A979985-L000137](../../tests/test_generation_acceptance_matrix.py#L137) | 137 | `"            [{\"role\": \"user\", \"content\": \"اختبار\"}],"` | — |
| [SRC-829A979985-L000138](../../tests/test_generation_acceptance_matrix.py#L138) | 138 | `"            model=\"primary/model\","` | — |
| [SRC-829A979985-L000139](../../tests/test_generation_acceptance_matrix.py#L139) | 139 | `"        )"` | — |
| [SRC-829A979985-L000140](../../tests/test_generation_acceptance_matrix.py#L140) | 140 | `""` | — |
| [SRC-829A979985-L000141](../../tests/test_generation_acceptance_matrix.py#L141) | 141 | `"    assert calls == [\"primary/model\"]"` | — |
| [SRC-829A979985-L000142](../../tests/test_generation_acceptance_matrix.py#L142) | 142 | `"    assert budget.snapshot()[\"counts\"][\"model_calls\"] == 1"` | — |
| [SRC-829A979985-L000143](../../tests/test_generation_acceptance_matrix.py#L143) | 143 | `"    assert [item[\"status\"] for item in agent.generation_diagnostics] == [\"truncated\"]"` | — |
| [SRC-829A979985-L000144](../../tests/test_generation_acceptance_matrix.py#L144) | 144 | `"    assert agent.model_usage == []"` | — |
| [SRC-829A979985-L000145](../../tests/test_generation_acceptance_matrix.py#L145) | 145 | `""` | — |
| [SRC-829A979985-L000146](../../tests/test_generation_acceptance_matrix.py#L146) | 146 | `""` | — |
| [SRC-829A979985-L000147](../../tests/test_generation_acceptance_matrix.py#L147) | 147 | `"def test_capability_snapshot_separates_configuration_from_live_health(monkeypatch):"` | — |
| [SRC-829A979985-L000148](../../tests/test_generation_acceptance_matrix.py#L148) | 148 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000149](../../tests/test_generation_acceptance_matrix.py#L149) | 149 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000150](../../tests/test_generation_acceptance_matrix.py#L150) | 150 | `"        agent,"` | — |
| [SRC-829A979985-L000151](../../tests/test_generation_acceptance_matrix.py#L151) | 151 | `"        \"status\","` | — |
| [SRC-829A979985-L000152](../../tests/test_generation_acceptance_matrix.py#L152) | 152 | `"        lambda: {"` | — |
| [SRC-829A979985-L000153](../../tests/test_generation_acceptance_matrix.py#L153) | 153 | `"            \"web_search_ready\": True,"` | — |
| [SRC-829A979985-L000154](../../tests/test_generation_acceptance_matrix.py#L154) | 154 | `"            \"language_model_configured\": True,"` | — |
| [SRC-829A979985-L000155](../../tests/test_generation_acceptance_matrix.py#L155) | 155 | `"            \"deepseek_search_api_configured\": True,"` | — |
| [SRC-829A979985-L000156](../../tests/test_generation_acceptance_matrix.py#L156) | 156 | `"            \"brave_search_api_configured\": True,"` | — |
| [SRC-829A979985-L000157](../../tests/test_generation_acceptance_matrix.py#L157) | 157 | `"            \"tavily_search_api_configured\": False,"` | — |
| [SRC-829A979985-L000158](../../tests/test_generation_acceptance_matrix.py#L158) | 158 | `"            \"openrouter_web_search_enabled\": False,"` | — |
| [SRC-829A979985-L000159](../../tests/test_generation_acceptance_matrix.py#L159) | 159 | `"        },"` | — |
| [SRC-829A979985-L000160](../../tests/test_generation_acceptance_matrix.py#L160) | 160 | `"    )"` | — |
| [SRC-829A979985-L000161](../../tests/test_generation_acceptance_matrix.py#L161) | 161 | `""` | — |
| [SRC-829A979985-L000162](../../tests/test_generation_acceptance_matrix.py#L162) | 162 | `"    snapshot = agent._capability_status_snapshot()"` | — |
| [SRC-829A979985-L000163](../../tests/test_generation_acceptance_matrix.py#L163) | 163 | `"    providers = {item[\"name\"]: item for item in snapshot[\"web_search\"][\"providers\"]}"` | — |
| [SRC-829A979985-L000164](../../tests/test_generation_acceptance_matrix.py#L164) | 164 | `""` | — |
| [SRC-829A979985-L000165](../../tests/test_generation_acceptance_matrix.py#L165) | 165 | `"    assert snapshot[\"web_search\"][\"implemented\"] is True"` | — |
| [SRC-829A979985-L000166](../../tests/test_generation_acceptance_matrix.py#L166) | 166 | `"    assert snapshot[\"web_search\"][\"local_dependencies_ready\"] is True"` | — |
| [SRC-829A979985-L000167](../../tests/test_generation_acceptance_matrix.py#L167) | 167 | `"    assert snapshot[\"web_search\"][\"runtime_status\"] == \"not_tested_in_this_response\""` | — |
| [SRC-829A979985-L000168](../../tests/test_generation_acceptance_matrix.py#L168) | 168 | `"    assert providers[\"duckduckgo_html\"][\"configuration_status\"] == \"built_in_no_api_key\""` | — |
| [SRC-829A979985-L000169](../../tests/test_generation_acceptance_matrix.py#L169) | 169 | `"    assert providers[\"duckduckgo_html\"][\"runtime_status\"] == \"not_tested_in_this_response\""` | — |
| [SRC-829A979985-L000170](../../tests/test_generation_acceptance_matrix.py#L170) | 170 | `"    assert providers[\"deepseek_search_api\"][\"configuration_status\"] == \"configured\""` | — |
| [SRC-829A979985-L000171](../../tests/test_generation_acceptance_matrix.py#L171) | 171 | `"    assert providers[\"deepseek_search_api\"][\"runtime_status\"] == \"not_tested_in_this_response\""` | — |
| [SRC-829A979985-L000172](../../tests/test_generation_acceptance_matrix.py#L172) | 172 | `"    assert providers[\"brave_search_api\"][\"configuration_status\"] == \"configured\""` | — |
| [SRC-829A979985-L000173](../../tests/test_generation_acceptance_matrix.py#L173) | 173 | `"    assert providers[\"brave_search_api\"][\"runtime_status\"] == \"not_tested_in_this_response\""` | — |
| [SRC-829A979985-L000174](../../tests/test_generation_acceptance_matrix.py#L174) | 174 | `"    assert providers[\"tavily_search_api\"][\"configuration_status\"] == \"not_configured\""` | — |
| [SRC-829A979985-L000175](../../tests/test_generation_acceptance_matrix.py#L175) | 175 | `"    assert providers[\"tavily_search_api\"][\"runtime_status\"] == \"not_configured\""` | — |
| [SRC-829A979985-L000176](../../tests/test_generation_acceptance_matrix.py#L176) | 176 | `"    assert providers[\"openrouter_web_search\"][\"configuration_status\"] == \"disabled\""` | — |
| [SRC-829A979985-L000177](../../tests/test_generation_acceptance_matrix.py#L177) | 177 | `"    assert providers[\"openrouter_web_search\"][\"runtime_status\"] == \"disabled\""` | — |
| [SRC-829A979985-L000178](../../tests/test_generation_acceptance_matrix.py#L178) | 178 | `""` | — |
| [SRC-829A979985-L000179](../../tests/test_generation_acceptance_matrix.py#L179) | 179 | `""` | — |
| [SRC-829A979985-L000180](../../tests/test_generation_acceptance_matrix.py#L180) | 180 | `"def test_capability_answer_discloses_optional_deepseek_search_status(monkeypatch):"` | — |
| [SRC-829A979985-L000181](../../tests/test_generation_acceptance_matrix.py#L181) | 181 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000182](../../tests/test_generation_acceptance_matrix.py#L182) | 182 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000183](../../tests/test_generation_acceptance_matrix.py#L183) | 183 | `"        agent,"` | — |
| [SRC-829A979985-L000184](../../tests/test_generation_acceptance_matrix.py#L184) | 184 | `"        \"status\","` | — |
| [SRC-829A979985-L000185](../../tests/test_generation_acceptance_matrix.py#L185) | 185 | `"        lambda: {"` | — |
| [SRC-829A979985-L000186](../../tests/test_generation_acceptance_matrix.py#L186) | 186 | `"            \"web_search_ready\": True,"` | — |
| [SRC-829A979985-L000187](../../tests/test_generation_acceptance_matrix.py#L187) | 187 | `"            \"language_model_configured\": True,"` | — |
| [SRC-829A979985-L000188](../../tests/test_generation_acceptance_matrix.py#L188) | 188 | `"            \"deepseek_search_api_configured\": True,"` | — |
| [SRC-829A979985-L000189](../../tests/test_generation_acceptance_matrix.py#L189) | 189 | `"            \"brave_search_api_configured\": False,"` | — |
| [SRC-829A979985-L000190](../../tests/test_generation_acceptance_matrix.py#L190) | 190 | `"            \"tavily_search_api_configured\": False,"` | — |
| [SRC-829A979985-L000191](../../tests/test_generation_acceptance_matrix.py#L191) | 191 | `"            \"openrouter_web_search_enabled\": False,"` | — |
| [SRC-829A979985-L000192](../../tests/test_generation_acceptance_matrix.py#L192) | 192 | `"        },"` | — |
| [SRC-829A979985-L000193](../../tests/test_generation_acceptance_matrix.py#L193) | 193 | `"    )"` | — |
| [SRC-829A979985-L000194](../../tests/test_generation_acceptance_matrix.py#L194) | 194 | `""` | — |
| [SRC-829A979985-L000195](../../tests/test_generation_acceptance_matrix.py#L195) | 195 | `"    result = agent.answer(\"ما محركات البحث التي تستخدمها؟\")"` | — |
| [SRC-829A979985-L000196](../../tests/test_generation_acceptance_matrix.py#L196) | 196 | `""` | — |
| [SRC-829A979985-L000197](../../tests/test_generation_acceptance_matrix.py#L197) | 197 | `"    assert result[\"kind\"] == \"capability_answer\""` | — |
| [SRC-829A979985-L000198](../../tests/test_generation_acceptance_matrix.py#L198) | 198 | `"    assert \"DeepSeek Search API\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000199](../../tests/test_generation_acceptance_matrix.py#L199) | 199 | `"    assert \"غير مختبر في هذه الإجابة\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000200](../../tests/test_generation_acceptance_matrix.py#L200) | 200 | `"    assert \"قد يستهلك استخدامًا مدفوعًا\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000201](../../tests/test_generation_acceptance_matrix.py#L201) | 201 | `"    provider = next("` | — |
| [SRC-829A979985-L000202](../../tests/test_generation_acceptance_matrix.py#L202) | 202 | `"        item for item in result[\"capability_status\"][\"web_search\"][\"providers\"]"` | — |
| [SRC-829A979985-L000203](../../tests/test_generation_acceptance_matrix.py#L203) | 203 | `"        if item[\"name\"] == \"deepseek_search_api\""` | — |
| [SRC-829A979985-L000204](../../tests/test_generation_acceptance_matrix.py#L204) | 204 | `"    )"` | — |
| [SRC-829A979985-L000205](../../tests/test_generation_acceptance_matrix.py#L205) | 205 | `"    assert provider[\"configuration_status\"] == \"configured\""` | — |
| [SRC-829A979985-L000206](../../tests/test_generation_acceptance_matrix.py#L206) | 206 | `"    assert provider[\"runtime_status\"] == \"not_tested_in_this_response\""` | — |
| [SRC-829A979985-L000207](../../tests/test_generation_acceptance_matrix.py#L207) | 207 | `""` | — |
| [SRC-829A979985-L000208](../../tests/test_generation_acceptance_matrix.py#L208) | 208 | `""` | — |
| [SRC-829A979985-L000209](../../tests/test_generation_acceptance_matrix.py#L209) | 209 | `"def test_operational_truth_overrides_a_model_claim_about_this_request(monkeypatch):"` | — |
| [SRC-829A979985-L000210](../../tests/test_generation_acceptance_matrix.py#L210) | 210 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000211](../../tests/test_generation_acceptance_matrix.py#L211) | 211 | `"    model_calls: list[str] = []"` | — |
| [SRC-829A979985-L000212](../../tests/test_generation_acceptance_matrix.py#L212) | 212 | `""` | — |
| [SRC-829A979985-L000213](../../tests/test_generation_acceptance_matrix.py#L213) | 213 | `"    def dishonest_model(*args, **kwargs):"` | — |
| [SRC-829A979985-L000214](../../tests/test_generation_acceptance_matrix.py#L214) | 214 | `"        model_calls.append(\"called\")"` | — |
| [SRC-829A979985-L000215](../../tests/test_generation_acceptance_matrix.py#L215) | 215 | `"        return \"نعم، بحثت في الإنترنت وتحققت من المصادر.\""` | — |
| [SRC-829A979985-L000216](../../tests/test_generation_acceptance_matrix.py#L216) | 216 | `""` | — |
| [SRC-829A979985-L000217](../../tests/test_generation_acceptance_matrix.py#L217) | 217 | `"    monkeypatch.setattr(agent, \"_request_completion\", dishonest_model)"` | — |
| [SRC-829A979985-L000218](../../tests/test_generation_acceptance_matrix.py#L218) | 218 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000219](../../tests/test_generation_acceptance_matrix.py#L219) | 219 | `"        agent,"` | — |
| [SRC-829A979985-L000220](../../tests/test_generation_acceptance_matrix.py#L220) | 220 | `"        \"_collect_research\","` | — |
| [SRC-829A979985-L000221](../../tests/test_generation_acceptance_matrix.py#L221) | 221 | `"        lambda plan: pytest.fail(\"A current-search status question must stay local\"),"` | — |
| [SRC-829A979985-L000222](../../tests/test_generation_acceptance_matrix.py#L222) | 222 | `"    )"` | — |
| [SRC-829A979985-L000223](../../tests/test_generation_acceptance_matrix.py#L223) | 223 | `""` | — |
| [SRC-829A979985-L000224](../../tests/test_generation_acceptance_matrix.py#L224) | 224 | `"    result = agent.answer(\"هل بحثت في الانترنت للاجابة الحالية؟\", mode=\"deep\")"` | — |
| [SRC-829A979985-L000225](../../tests/test_generation_acceptance_matrix.py#L225) | 225 | `""` | — |
| [SRC-829A979985-L000226](../../tests/test_generation_acceptance_matrix.py#L226) | 226 | `"    assert model_calls == []"` | — |
| [SRC-829A979985-L000227](../../tests/test_generation_acceptance_matrix.py#L227) | 227 | `"    assert result[\"search_attempted\"] is False"` | — |
| [SRC-829A979985-L000228](../../tests/test_generation_acceptance_matrix.py#L228) | 228 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-829A979985-L000229](../../tests/test_generation_acceptance_matrix.py#L229) | 229 | `"    assert result[\"request_execution_status\"][\"search_outcome\"] == \"not_attempted\""` | — |
| [SRC-829A979985-L000230](../../tests/test_generation_acceptance_matrix.py#L230) | 230 | `"    assert \"لم أنفّذ بحثًا حيًا للإجابة عن هذا السؤال تحديدًا\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000231](../../tests/test_generation_acceptance_matrix.py#L231) | 231 | `"    assert \"تحققت من المصادر\" not in result[\"answer\"]"` | — |
| [SRC-829A979985-L000232](../../tests/test_generation_acceptance_matrix.py#L232) | 232 | `""` | — |
| [SRC-829A979985-L000233](../../tests/test_generation_acceptance_matrix.py#L233) | 233 | `""` | — |
| [SRC-829A979985-L000234](../../tests/test_generation_acceptance_matrix.py#L234) | 234 | `"def test_generation_budget_exhaustion_preserves_partial_sources(monkeypatch):"` | — |
| [SRC-829A979985-L000235](../../tests/test_generation_acceptance_matrix.py#L235) | 235 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000236](../../tests/test_generation_acceptance_matrix.py#L236) | 236 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-829A979985-L000237](../../tests/test_generation_acceptance_matrix.py#L237) | 237 | `"    question = \"ابحث عن أحدث معلومات حول الطاقة المتجددة\""` | — |
| [SRC-829A979985-L000238](../../tests/test_generation_acceptance_matrix.py#L238) | 238 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_MODEL_CALLS\", \"1\")"` | — |
| [SRC-829A979985-L000239](../../tests/test_generation_acceptance_matrix.py#L239) | 239 | `"    sources = ["` | — |
| [SRC-829A979985-L000240](../../tests/test_generation_acceptance_matrix.py#L240) | 240 | `"        source("` | — |
| [SRC-829A979985-L000241](../../tests/test_generation_acceptance_matrix.py#L241) | 241 | `"            \"https://one.example/energy\","` | — |
| [SRC-829A979985-L000242](../../tests/test_generation_acceptance_matrix.py#L242) | 242 | `"            \"one.example\","` | — |
| [SRC-829A979985-L000243](../../tests/test_generation_acceptance_matrix.py#L243) | 243 | `"            page_fetched=True,"` | — |
| [SRC-829A979985-L000244](../../tests/test_generation_acceptance_matrix.py#L244) | 244 | `"            page_text=\"معلومة مستخرجة من المصدر الأول عن الطاقة المتجددة.\","` | — |
| [SRC-829A979985-L000245](../../tests/test_generation_acceptance_matrix.py#L245) | 245 | `"            provider=\"duckduckgo_html\","` | — |
| [SRC-829A979985-L000246](../../tests/test_generation_acceptance_matrix.py#L246) | 246 | `"        ),"` | — |
| [SRC-829A979985-L000247](../../tests/test_generation_acceptance_matrix.py#L247) | 247 | `"        source("` | — |
| [SRC-829A979985-L000248](../../tests/test_generation_acceptance_matrix.py#L248) | 248 | `"            \"https://two.example/energy\","` | — |
| [SRC-829A979985-L000249](../../tests/test_generation_acceptance_matrix.py#L249) | 249 | `"            \"two.example\","` | — |
| [SRC-829A979985-L000250](../../tests/test_generation_acceptance_matrix.py#L250) | 250 | `"            page_fetched=False,"` | — |
| [SRC-829A979985-L000251](../../tests/test_generation_acceptance_matrix.py#L251) | 251 | `"            snippet=\"مقتطف المصدر الثاني عن الطاقة المتجددة.\","` | — |
| [SRC-829A979985-L000252](../../tests/test_generation_acceptance_matrix.py#L252) | 252 | `"            provider=\"bing_rss\","` | — |
| [SRC-829A979985-L000253](../../tests/test_generation_acceptance_matrix.py#L253) | 253 | `"        ),"` | — |
| [SRC-829A979985-L000254](../../tests/test_generation_acceptance_matrix.py#L254) | 254 | `"    ]"` | — |
| [SRC-829A979985-L000255](../../tests/test_generation_acceptance_matrix.py#L255) | 255 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000256](../../tests/test_generation_acceptance_matrix.py#L256) | 256 | `"        agent,"` | — |
| [SRC-829A979985-L000257](../../tests/test_generation_acceptance_matrix.py#L257) | 257 | `"        \"_plan_search\","` | — |
| [SRC-829A979985-L000258](../../tests/test_generation_acceptance_matrix.py#L258) | 258 | `"        lambda question, history: {"` | — |
| [SRC-829A979985-L000259](../../tests/test_generation_acceptance_matrix.py#L259) | 259 | `"            \"queries\": [question],"` | — |
| [SRC-829A979985-L000260](../../tests/test_generation_acceptance_matrix.py#L260) | 260 | `"            \"direct_urls\": [],"` | — |
| [SRC-829A979985-L000261](../../tests/test_generation_acceptance_matrix.py#L261) | 261 | `"            \"social_focus\": False,"` | — |
| [SRC-829A979985-L000262](../../tests/test_generation_acceptance_matrix.py#L262) | 262 | `"            \"freshness\": \"current\","` | — |
| [SRC-829A979985-L000263](../../tests/test_generation_acceptance_matrix.py#L263) | 263 | `"            \"depth\": \"standard\","` | — |
| [SRC-829A979985-L000264](../../tests/test_generation_acceptance_matrix.py#L264) | 264 | `"            \"platforms\": [],"` | — |
| [SRC-829A979985-L000265](../../tests/test_generation_acceptance_matrix.py#L265) | 265 | `"            \"planning_method\": \"test\","` | — |
| [SRC-829A979985-L000266](../../tests/test_generation_acceptance_matrix.py#L266) | 266 | `"        },"` | — |
| [SRC-829A979985-L000267](../../tests/test_generation_acceptance_matrix.py#L267) | 267 | `"    )"` | — |
| [SRC-829A979985-L000268](../../tests/test_generation_acceptance_matrix.py#L268) | 268 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000269](../../tests/test_generation_acceptance_matrix.py#L269) | 269 | `"        agent,"` | — |
| [SRC-829A979985-L000270](../../tests/test_generation_acceptance_matrix.py#L270) | 270 | `"        \"_collect_research\","` | — |
| [SRC-829A979985-L000271](../../tests/test_generation_acceptance_matrix.py#L271) | 271 | `"        lambda plan: ("` | — |
| [SRC-829A979985-L000272](../../tests/test_generation_acceptance_matrix.py#L272) | 272 | `"            sources,"` | — |
| [SRC-829A979985-L000273](../../tests/test_generation_acceptance_matrix.py#L273) | 273 | `"            [],"` | — |
| [SRC-829A979985-L000274](../../tests/test_generation_acceptance_matrix.py#L274) | 274 | `"            {"` | — |
| [SRC-829A979985-L000275](../../tests/test_generation_acceptance_matrix.py#L275) | 275 | `"                \"queries_planned\": 1,"` | — |
| [SRC-829A979985-L000276](../../tests/test_generation_acceptance_matrix.py#L276) | 276 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-829A979985-L000277](../../tests/test_generation_acceptance_matrix.py#L277) | 277 | `"                \"search_attempted\": True,"` | — |
| [SRC-829A979985-L000278](../../tests/test_generation_acceptance_matrix.py#L278) | 278 | `"                \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-829A979985-L000279](../../tests/test_generation_acceptance_matrix.py#L279) | 279 | `"                \"unique_sources\": 2,"` | — |
| [SRC-829A979985-L000280](../../tests/test_generation_acceptance_matrix.py#L280) | 280 | `"                \"pages_fetched\": 1,"` | — |
| [SRC-829A979985-L000281](../../tests/test_generation_acceptance_matrix.py#L281) | 281 | `"                \"providers_used\": [\"duckduckgo_html\", \"bing_rss\"],"` | — |
| [SRC-829A979985-L000282](../../tests/test_generation_acceptance_matrix.py#L282) | 282 | `"                \"provider_counts\": {\"duckduckgo_html\": 1, \"bing_rss\": 1},"` | — |
| [SRC-829A979985-L000283](../../tests/test_generation_acceptance_matrix.py#L283) | 283 | `"                \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-829A979985-L000284](../../tests/test_generation_acceptance_matrix.py#L284) | 284 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-829A979985-L000285](../../tests/test_generation_acceptance_matrix.py#L285) | 285 | `"                \"provider_diagnostics\": [],"` | — |
| [SRC-829A979985-L000286](../../tests/test_generation_acceptance_matrix.py#L286) | 286 | `"                \"evidence_signals\": {},"` | — |
| [SRC-829A979985-L000287](../../tests/test_generation_acceptance_matrix.py#L287) | 287 | `"            },"` | — |
| [SRC-829A979985-L000288](../../tests/test_generation_acceptance_matrix.py#L288) | 288 | `"        ),"` | — |
| [SRC-829A979985-L000289](../../tests/test_generation_acceptance_matrix.py#L289) | 289 | `"    )"` | — |
| [SRC-829A979985-L000290](../../tests/test_generation_acceptance_matrix.py#L290) | 290 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, item: True)"` | — |
| [SRC-829A979985-L000291](../../tests/test_generation_acceptance_matrix.py#L291) | 291 | `"    calls: list[str] = []"` | — |
| [SRC-829A979985-L000292](../../tests/test_generation_acceptance_matrix.py#L292) | 292 | `""` | — |
| [SRC-829A979985-L000293](../../tests/test_generation_acceptance_matrix.py#L293) | 293 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-829A979985-L000294](../../tests/test_generation_acceptance_matrix.py#L294) | 294 | `"        model = json.loads(request.data.decode(\"utf-8\"))[\"model\"]"` | — |
| [SRC-829A979985-L000295](../../tests/test_generation_acceptance_matrix.py#L295) | 295 | `"        calls.append(model)"` | — |
| [SRC-829A979985-L000296](../../tests/test_generation_acceptance_matrix.py#L296) | 296 | `"        return FakeCompletionResponse(\"إجابة مبتورة لا يجوز عرضها\", \"length\")"` | — |
| [SRC-829A979985-L000297](../../tests/test_generation_acceptance_matrix.py#L297) | 297 | `""` | — |
| [SRC-829A979985-L000298](../../tests/test_generation_acceptance_matrix.py#L298) | 298 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-829A979985-L000299](../../tests/test_generation_acceptance_matrix.py#L299) | 299 | `""` | — |
| [SRC-829A979985-L000300](../../tests/test_generation_acceptance_matrix.py#L300) | 300 | `"    result = agent.answer(question)"` | — |
| [SRC-829A979985-L000301](../../tests/test_generation_acceptance_matrix.py#L301) | 301 | `""` | — |
| [SRC-829A979985-L000302](../../tests/test_generation_acceptance_matrix.py#L302) | 302 | `"    assert len(calls) == 1"` | — |
| [SRC-829A979985-L000303](../../tests/test_generation_acceptance_matrix.py#L303) | 303 | `"    assert result[\"request_budget\"][\"counts\"][\"model_calls\"] == 1"` | — |
| [SRC-829A979985-L000304](../../tests/test_generation_acceptance_matrix.py#L304) | 304 | `"    assert \"model_calls\" in result[\"request_budget\"][\"exhausted_reasons\"]"` | — |
| [SRC-829A979985-L000305](../../tests/test_generation_acceptance_matrix.py#L305) | 305 | `"    assert result[\"final_answer_status\"] == \"budget_exhausted_with_source_fallback\""` | — |
| [SRC-829A979985-L000306](../../tests/test_generation_acceptance_matrix.py#L306) | 306 | `"    assert result[\"used_language_model\"] is False"` | — |
| [SRC-829A979985-L000307](../../tests/test_generation_acceptance_matrix.py#L307) | 307 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-829A979985-L000308](../../tests/test_generation_acceptance_matrix.py#L308) | 308 | `"    assert len(result[\"sources\"]) == 2"` | — |
| [SRC-829A979985-L000309](../../tests/test_generation_acceptance_matrix.py#L309) | 309 | `"    assert \"إجابة مبتورة لا يجوز عرضها\" not in result[\"answer\"]"` | — |
| [SRC-829A979985-L000310](../../tests/test_generation_acceptance_matrix.py#L310) | 310 | `"    assert \"مقتطف المصدر الثاني عن الطاقة المتجددة\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000311](../../tests/test_generation_acceptance_matrix.py#L311) | 311 | `"    assert result[\"generation_diagnostics\"][0][\"status\"] == \"truncated\""` | — |
| [SRC-829A979985-L000312](../../tests/test_generation_acceptance_matrix.py#L312) | 312 | `""` | — |
| [SRC-829A979985-L000313](../../tests/test_generation_acceptance_matrix.py#L313) | 313 | `""` | — |
| [SRC-829A979985-L000314](../../tests/test_generation_acceptance_matrix.py#L314) | 314 | `"def test_review_budget_exhaustion_discards_draft_and_preserves_sources(monkeypatch):"` | — |
| [SRC-829A979985-L000315](../../tests/test_generation_acceptance_matrix.py#L315) | 315 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000316](../../tests/test_generation_acceptance_matrix.py#L316) | 316 | `"    agent.api_key = \"test-key\""` | — |
| [SRC-829A979985-L000317](../../tests/test_generation_acceptance_matrix.py#L317) | 317 | `"    question = \"قارن بين الخيارات من حيث السعر، المساحة، والبيانات الناقصة\""` | — |
| [SRC-829A979985-L000318](../../tests/test_generation_acceptance_matrix.py#L318) | 318 | `"    monkeypatch.setenv(\"OMARAI_REQUEST_MAX_MODEL_CALLS\", \"1\")"` | — |
| [SRC-829A979985-L000319](../../tests/test_generation_acceptance_matrix.py#L319) | 319 | `"    sources = ["` | — |
| [SRC-829A979985-L000320](../../tests/test_generation_acceptance_matrix.py#L320) | 320 | `"        source("` | — |
| [SRC-829A979985-L000321](../../tests/test_generation_acceptance_matrix.py#L321) | 321 | `"            \"https://one.example/product\","` | — |
| [SRC-829A979985-L000322](../../tests/test_generation_acceptance_matrix.py#L322) | 322 | `"            \"one.example\","` | — |
| [SRC-829A979985-L000323](../../tests/test_generation_acceptance_matrix.py#L323) | 323 | `"            page_fetched=True,"` | — |
| [SRC-829A979985-L000324](../../tests/test_generation_acceptance_matrix.py#L324) | 324 | `"            page_text=\"السعر الإجمالي 100000 جنيه والمساحة 100 متر.\","` | — |
| [SRC-829A979985-L000325](../../tests/test_generation_acceptance_matrix.py#L325) | 325 | `"            provider=\"duckduckgo_html\","` | — |
| [SRC-829A979985-L000326](../../tests/test_generation_acceptance_matrix.py#L326) | 326 | `"        ),"` | — |
| [SRC-829A979985-L000327](../../tests/test_generation_acceptance_matrix.py#L327) | 327 | `"        source("` | — |
| [SRC-829A979985-L000328](../../tests/test_generation_acceptance_matrix.py#L328) | 328 | `"            \"https://two.example/product\","` | — |
| [SRC-829A979985-L000329](../../tests/test_generation_acceptance_matrix.py#L329) | 329 | `"            \"two.example\","` | — |
| [SRC-829A979985-L000330](../../tests/test_generation_acceptance_matrix.py#L330) | 330 | `"            page_fetched=False,"` | — |
| [SRC-829A979985-L000331](../../tests/test_generation_acceptance_matrix.py#L331) | 331 | `"            snippet=\"إعلان يذكر سعرًا دون بيان المساحة.\","` | — |
| [SRC-829A979985-L000332](../../tests/test_generation_acceptance_matrix.py#L332) | 332 | `"            provider=\"bing_rss\","` | — |
| [SRC-829A979985-L000333](../../tests/test_generation_acceptance_matrix.py#L333) | 333 | `"        ),"` | — |
| [SRC-829A979985-L000334](../../tests/test_generation_acceptance_matrix.py#L334) | 334 | `"    ]"` | — |
| [SRC-829A979985-L000335](../../tests/test_generation_acceptance_matrix.py#L335) | 335 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000336](../../tests/test_generation_acceptance_matrix.py#L336) | 336 | `"        agent,"` | — |
| [SRC-829A979985-L000337](../../tests/test_generation_acceptance_matrix.py#L337) | 337 | `"        \"_plan_search\","` | — |
| [SRC-829A979985-L000338](../../tests/test_generation_acceptance_matrix.py#L338) | 338 | `"        lambda question, history: {"` | — |
| [SRC-829A979985-L000339](../../tests/test_generation_acceptance_matrix.py#L339) | 339 | `"            \"queries\": [question],"` | — |
| [SRC-829A979985-L000340](../../tests/test_generation_acceptance_matrix.py#L340) | 340 | `"            \"direct_urls\": [],"` | — |
| [SRC-829A979985-L000341](../../tests/test_generation_acceptance_matrix.py#L341) | 341 | `"            \"social_focus\": False,"` | — |
| [SRC-829A979985-L000342](../../tests/test_generation_acceptance_matrix.py#L342) | 342 | `"            \"freshness\": \"any\","` | — |
| [SRC-829A979985-L000343](../../tests/test_generation_acceptance_matrix.py#L343) | 343 | `"            \"depth\": \"deep\","` | — |
| [SRC-829A979985-L000344](../../tests/test_generation_acceptance_matrix.py#L344) | 344 | `"            \"platforms\": [],"` | — |
| [SRC-829A979985-L000345](../../tests/test_generation_acceptance_matrix.py#L345) | 345 | `"            \"planning_method\": \"test\","` | — |
| [SRC-829A979985-L000346](../../tests/test_generation_acceptance_matrix.py#L346) | 346 | `"        },"` | — |
| [SRC-829A979985-L000347](../../tests/test_generation_acceptance_matrix.py#L347) | 347 | `"    )"` | — |
| [SRC-829A979985-L000348](../../tests/test_generation_acceptance_matrix.py#L348) | 348 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000349](../../tests/test_generation_acceptance_matrix.py#L349) | 349 | `"        agent,"` | — |
| [SRC-829A979985-L000350](../../tests/test_generation_acceptance_matrix.py#L350) | 350 | `"        \"_collect_research\","` | — |
| [SRC-829A979985-L000351](../../tests/test_generation_acceptance_matrix.py#L351) | 351 | `"        lambda plan: ("` | — |
| [SRC-829A979985-L000352](../../tests/test_generation_acceptance_matrix.py#L352) | 352 | `"            sources,"` | — |
| [SRC-829A979985-L000353](../../tests/test_generation_acceptance_matrix.py#L353) | 353 | `"            [],"` | — |
| [SRC-829A979985-L000354](../../tests/test_generation_acceptance_matrix.py#L354) | 354 | `"            {"` | — |
| [SRC-829A979985-L000355](../../tests/test_generation_acceptance_matrix.py#L355) | 355 | `"                \"queries_planned\": 1,"` | — |
| [SRC-829A979985-L000356](../../tests/test_generation_acceptance_matrix.py#L356) | 356 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-829A979985-L000357](../../tests/test_generation_acceptance_matrix.py#L357) | 357 | `"                \"search_attempted\": True,"` | — |
| [SRC-829A979985-L000358](../../tests/test_generation_acceptance_matrix.py#L358) | 358 | `"                \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-829A979985-L000359](../../tests/test_generation_acceptance_matrix.py#L359) | 359 | `"                \"unique_sources\": 2,"` | — |
| [SRC-829A979985-L000360](../../tests/test_generation_acceptance_matrix.py#L360) | 360 | `"                \"pages_fetched\": 1,"` | — |
| [SRC-829A979985-L000361](../../tests/test_generation_acceptance_matrix.py#L361) | 361 | `"                \"providers_used\": [\"duckduckgo_html\", \"bing_rss\"],"` | — |
| [SRC-829A979985-L000362](../../tests/test_generation_acceptance_matrix.py#L362) | 362 | `"                \"provider_counts\": {\"duckduckgo_html\": 1, \"bing_rss\": 1},"` | — |
| [SRC-829A979985-L000363](../../tests/test_generation_acceptance_matrix.py#L363) | 363 | `"                \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-829A979985-L000364](../../tests/test_generation_acceptance_matrix.py#L364) | 364 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-829A979985-L000365](../../tests/test_generation_acceptance_matrix.py#L365) | 365 | `"                \"provider_diagnostics\": [],"` | — |
| [SRC-829A979985-L000366](../../tests/test_generation_acceptance_matrix.py#L366) | 366 | `"                \"evidence_signals\": {},"` | — |
| [SRC-829A979985-L000367](../../tests/test_generation_acceptance_matrix.py#L367) | 367 | `"            },"` | — |
| [SRC-829A979985-L000368](../../tests/test_generation_acceptance_matrix.py#L368) | 368 | `"        ),"` | — |
| [SRC-829A979985-L000369](../../tests/test_generation_acceptance_matrix.py#L369) | 369 | `"    )"` | — |
| [SRC-829A979985-L000370](../../tests/test_generation_acceptance_matrix.py#L370) | 370 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, item: True)"` | — |
| [SRC-829A979985-L000371](../../tests/test_generation_acceptance_matrix.py#L371) | 371 | `"    calls: list[str] = []"` | — |
| [SRC-829A979985-L000372](../../tests/test_generation_acceptance_matrix.py#L372) | 372 | `""` | — |
| [SRC-829A979985-L000373](../../tests/test_generation_acceptance_matrix.py#L373) | 373 | `"    def fake_urlopen(request, timeout):"` | — |
| [SRC-829A979985-L000374](../../tests/test_generation_acceptance_matrix.py#L374) | 374 | `"        calls.append(json.loads(request.data.decode(\"utf-8\"))[\"model\"])"` | — |
| [SRC-829A979985-L000375](../../tests/test_generation_acceptance_matrix.py#L375) | 375 | `"        return FakeCompletionResponse("` | — |
| [SRC-829A979985-L000376](../../tests/test_generation_acceptance_matrix.py#L376) | 376 | `"            \"مسودة تحليل مولدة لكنها لم تخضع للتدقيق النهائي [المصدر 1].\","` | — |
| [SRC-829A979985-L000377](../../tests/test_generation_acceptance_matrix.py#L377) | 377 | `"            \"stop\","` | — |
| [SRC-829A979985-L000378](../../tests/test_generation_acceptance_matrix.py#L378) | 378 | `"        )"` | — |
| [SRC-829A979985-L000379](../../tests/test_generation_acceptance_matrix.py#L379) | 379 | `""` | — |
| [SRC-829A979985-L000380](../../tests/test_generation_acceptance_matrix.py#L380) | 380 | `"    monkeypatch.setattr(\"agents.web_agent.urllib.request.urlopen\", fake_urlopen)"` | — |
| [SRC-829A979985-L000381](../../tests/test_generation_acceptance_matrix.py#L381) | 381 | `""` | — |
| [SRC-829A979985-L000382](../../tests/test_generation_acceptance_matrix.py#L382) | 382 | `"    result = agent.answer(question)"` | — |
| [SRC-829A979985-L000383](../../tests/test_generation_acceptance_matrix.py#L383) | 383 | `""` | — |
| [SRC-829A979985-L000384](../../tests/test_generation_acceptance_matrix.py#L384) | 384 | `"    assert len(calls) == 1"` | — |
| [SRC-829A979985-L000385](../../tests/test_generation_acceptance_matrix.py#L385) | 385 | `"    assert result[\"request_budget\"][\"counts\"][\"model_calls\"] == 1"` | — |
| [SRC-829A979985-L000386](../../tests/test_generation_acceptance_matrix.py#L386) | 386 | `"    assert \"model_calls\" in result[\"request_budget\"][\"exhausted_reasons\"]"` | — |
| [SRC-829A979985-L000387](../../tests/test_generation_acceptance_matrix.py#L387) | 387 | `"    assert result[\"final_answer_status\"] == \"budget_exhausted_with_source_fallback\""` | — |
| [SRC-829A979985-L000388](../../tests/test_generation_acceptance_matrix.py#L388) | 388 | `"    assert result[\"search_report\"][\"second_pass_review\"] == \"model_claim_audit_unavailable\""` | — |
| [SRC-829A979985-L000389](../../tests/test_generation_acceptance_matrix.py#L389) | 389 | `"    assert len(result[\"sources\"]) == 2"` | — |
| [SRC-829A979985-L000390](../../tests/test_generation_acceptance_matrix.py#L390) | 390 | `"    assert \"مسودة تحليل مولدة لكنها لم تخضع للتدقيق النهائي\" not in result[\"answer\"]"` | — |
| [SRC-829A979985-L000391](../../tests/test_generation_acceptance_matrix.py#L391) | 391 | `"    assert \"السعر الإجمالي 100000 جنيه والمساحة 100 متر.\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000392](../../tests/test_generation_acceptance_matrix.py#L392) | 392 | `""` | — |
| [SRC-829A979985-L000393](../../tests/test_generation_acceptance_matrix.py#L393) | 393 | `""` | — |
| [SRC-829A979985-L000394](../../tests/test_generation_acceptance_matrix.py#L394) | 394 | `"def test_search_failure_is_not_reported_as_no_attempt_or_completed_answer(monkeypatch):"` | — |
| [SRC-829A979985-L000395](../../tests/test_generation_acceptance_matrix.py#L395) | 395 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000396](../../tests/test_generation_acceptance_matrix.py#L396) | 396 | `"    question = \"ابحث عن أحدث معلومات حول الطاقة المتجددة\""` | — |
| [SRC-829A979985-L000397](../../tests/test_generation_acceptance_matrix.py#L397) | 397 | `""` | — |
| [SRC-829A979985-L000398](../../tests/test_generation_acceptance_matrix.py#L398) | 398 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000399](../../tests/test_generation_acceptance_matrix.py#L399) | 399 | `"        agent,"` | — |
| [SRC-829A979985-L000400](../../tests/test_generation_acceptance_matrix.py#L400) | 400 | `"        \"_plan_search\","` | — |
| [SRC-829A979985-L000401](../../tests/test_generation_acceptance_matrix.py#L401) | 401 | `"        lambda question, history: {"` | — |
| [SRC-829A979985-L000402](../../tests/test_generation_acceptance_matrix.py#L402) | 402 | `"            \"queries\": [question],"` | — |
| [SRC-829A979985-L000403](../../tests/test_generation_acceptance_matrix.py#L403) | 403 | `"            \"direct_urls\": [],"` | — |
| [SRC-829A979985-L000404](../../tests/test_generation_acceptance_matrix.py#L404) | 404 | `"            \"social_focus\": False,"` | — |
| [SRC-829A979985-L000405](../../tests/test_generation_acceptance_matrix.py#L405) | 405 | `"            \"freshness\": \"current\","` | — |
| [SRC-829A979985-L000406](../../tests/test_generation_acceptance_matrix.py#L406) | 406 | `"            \"depth\": \"standard\","` | — |
| [SRC-829A979985-L000407](../../tests/test_generation_acceptance_matrix.py#L407) | 407 | `"            \"platforms\": [],"` | — |
| [SRC-829A979985-L000408](../../tests/test_generation_acceptance_matrix.py#L408) | 408 | `"            \"planning_method\": \"test\","` | — |
| [SRC-829A979985-L000409](../../tests/test_generation_acceptance_matrix.py#L409) | 409 | `"        },"` | — |
| [SRC-829A979985-L000410](../../tests/test_generation_acceptance_matrix.py#L410) | 410 | `"    )"` | — |
| [SRC-829A979985-L000411](../../tests/test_generation_acceptance_matrix.py#L411) | 411 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000412](../../tests/test_generation_acceptance_matrix.py#L412) | 412 | `"        agent,"` | — |
| [SRC-829A979985-L000413](../../tests/test_generation_acceptance_matrix.py#L413) | 413 | `"        \"_collect_research\","` | — |
| [SRC-829A979985-L000414](../../tests/test_generation_acceptance_matrix.py#L414) | 414 | `"        lambda plan: ("` | — |
| [SRC-829A979985-L000415](../../tests/test_generation_acceptance_matrix.py#L415) | 415 | `"            [],"` | — |
| [SRC-829A979985-L000416](../../tests/test_generation_acceptance_matrix.py#L416) | 416 | `"            [\"تعذر الاتصال بموصلات البحث\"],"` | — |
| [SRC-829A979985-L000417](../../tests/test_generation_acceptance_matrix.py#L417) | 417 | `"            {"` | — |
| [SRC-829A979985-L000418](../../tests/test_generation_acceptance_matrix.py#L418) | 418 | `"                \"queries_planned\": 1,"` | — |
| [SRC-829A979985-L000419](../../tests/test_generation_acceptance_matrix.py#L419) | 419 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-829A979985-L000420](../../tests/test_generation_acceptance_matrix.py#L420) | 420 | `"                \"search_attempted\": True,"` | — |
| [SRC-829A979985-L000421](../../tests/test_generation_acceptance_matrix.py#L421) | 421 | `"                \"search_outcome\": \"attempted_no_usable_sources\","` | — |
| [SRC-829A979985-L000422](../../tests/test_generation_acceptance_matrix.py#L422) | 422 | `"                \"unique_sources\": 0,"` | — |
| [SRC-829A979985-L000423](../../tests/test_generation_acceptance_matrix.py#L423) | 423 | `"                \"pages_fetched\": 0,"` | — |
| [SRC-829A979985-L000424](../../tests/test_generation_acceptance_matrix.py#L424) | 424 | `"                \"providers_used\": [],"` | — |
| [SRC-829A979985-L000425](../../tests/test_generation_acceptance_matrix.py#L425) | 425 | `"                \"provider_diagnostics\": ["` | — |
| [SRC-829A979985-L000426](../../tests/test_generation_acceptance_matrix.py#L426) | 426 | `"                    {\"provider\": \"duckduckgo_html\", \"status\": \"failed\"},"` | — |
| [SRC-829A979985-L000427](../../tests/test_generation_acceptance_matrix.py#L427) | 427 | `"                    {\"provider\": \"bing_rss\", \"status\": \"timeout\"},"` | — |
| [SRC-829A979985-L000428](../../tests/test_generation_acceptance_matrix.py#L428) | 428 | `"                ],"` | — |
| [SRC-829A979985-L000429](../../tests/test_generation_acceptance_matrix.py#L429) | 429 | `"                \"evidence_signals\": {},"` | — |
| [SRC-829A979985-L000430](../../tests/test_generation_acceptance_matrix.py#L430) | 430 | `"            },"` | — |
| [SRC-829A979985-L000431](../../tests/test_generation_acceptance_matrix.py#L431) | 431 | `"        ),"` | — |
| [SRC-829A979985-L000432](../../tests/test_generation_acceptance_matrix.py#L432) | 432 | `"    )"` | — |
| [SRC-829A979985-L000433](../../tests/test_generation_acceptance_matrix.py#L433) | 433 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000434](../../tests/test_generation_acceptance_matrix.py#L434) | 434 | `"        agent,"` | — |
| [SRC-829A979985-L000435](../../tests/test_generation_acceptance_matrix.py#L435) | 435 | `"        \"_generate\","` | — |
| [SRC-829A979985-L000436](../../tests/test_generation_acceptance_matrix.py#L436) | 436 | `"        lambda *args, **kwargs: pytest.fail(\"No final synthesis without usable sources\"),"` | — |
| [SRC-829A979985-L000437](../../tests/test_generation_acceptance_matrix.py#L437) | 437 | `"    )"` | — |
| [SRC-829A979985-L000438](../../tests/test_generation_acceptance_matrix.py#L438) | 438 | `""` | — |
| [SRC-829A979985-L000439](../../tests/test_generation_acceptance_matrix.py#L439) | 439 | `"    result = agent.answer(question)"` | — |
| [SRC-829A979985-L000440](../../tests/test_generation_acceptance_matrix.py#L440) | 440 | `""` | — |
| [SRC-829A979985-L000441](../../tests/test_generation_acceptance_matrix.py#L441) | 441 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-829A979985-L000442](../../tests/test_generation_acceptance_matrix.py#L442) | 442 | `"    assert result[\"used_web_search\"] is False"` | — |
| [SRC-829A979985-L000443](../../tests/test_generation_acceptance_matrix.py#L443) | 443 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_no_usable_sources\""` | — |
| [SRC-829A979985-L000444](../../tests/test_generation_acceptance_matrix.py#L444) | 444 | `"    assert result[\"final_answer_status\"] == \"insufficient_evidence_no_generation\""` | — |
| [SRC-829A979985-L000445](../../tests/test_generation_acceptance_matrix.py#L445) | 445 | `"    assert result[\"used_language_model\"] is False"` | — |
| [SRC-829A979985-L000446](../../tests/test_generation_acceptance_matrix.py#L446) | 446 | `"    assert result[\"research_quality\"] == \"failed\""` | — |
| [SRC-829A979985-L000447](../../tests/test_generation_acceptance_matrix.py#L447) | 447 | `""` | — |
| [SRC-829A979985-L000448](../../tests/test_generation_acceptance_matrix.py#L448) | 448 | `""` | — |
| [SRC-829A979985-L000449](../../tests/test_generation_acceptance_matrix.py#L449) | 449 | `"def test_research_exception_does_not_claim_no_results_or_no_search(monkeypatch):"` | — |
| [SRC-829A979985-L000450](../../tests/test_generation_acceptance_matrix.py#L450) | 450 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000451](../../tests/test_generation_acceptance_matrix.py#L451) | 451 | `"    question = \"ابحث عن أحدث معلومات حول الطاقة المتجددة\""` | — |
| [SRC-829A979985-L000452](../../tests/test_generation_acceptance_matrix.py#L452) | 452 | `""` | — |
| [SRC-829A979985-L000453](../../tests/test_generation_acceptance_matrix.py#L453) | 453 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000454](../../tests/test_generation_acceptance_matrix.py#L454) | 454 | `"        agent,"` | — |
| [SRC-829A979985-L000455](../../tests/test_generation_acceptance_matrix.py#L455) | 455 | `"        \"_plan_search\","` | — |
| [SRC-829A979985-L000456](../../tests/test_generation_acceptance_matrix.py#L456) | 456 | `"        lambda question, history: {"` | — |
| [SRC-829A979985-L000457](../../tests/test_generation_acceptance_matrix.py#L457) | 457 | `"            \"queries\": [question],"` | — |
| [SRC-829A979985-L000458](../../tests/test_generation_acceptance_matrix.py#L458) | 458 | `"            \"direct_urls\": [],"` | — |
| [SRC-829A979985-L000459](../../tests/test_generation_acceptance_matrix.py#L459) | 459 | `"            \"social_focus\": False,"` | — |
| [SRC-829A979985-L000460](../../tests/test_generation_acceptance_matrix.py#L460) | 460 | `"            \"freshness\": \"current\","` | — |
| [SRC-829A979985-L000461](../../tests/test_generation_acceptance_matrix.py#L461) | 461 | `"            \"depth\": \"standard\","` | — |
| [SRC-829A979985-L000462](../../tests/test_generation_acceptance_matrix.py#L462) | 462 | `"            \"platforms\": [],"` | — |
| [SRC-829A979985-L000463](../../tests/test_generation_acceptance_matrix.py#L463) | 463 | `"            \"planning_method\": \"test\","` | — |
| [SRC-829A979985-L000464](../../tests/test_generation_acceptance_matrix.py#L464) | 464 | `"        },"` | — |
| [SRC-829A979985-L000465](../../tests/test_generation_acceptance_matrix.py#L465) | 465 | `"    )"` | — |
| [SRC-829A979985-L000466](../../tests/test_generation_acceptance_matrix.py#L466) | 466 | `""` | — |
| [SRC-829A979985-L000467](../../tests/test_generation_acceptance_matrix.py#L467) | 467 | `"    def collect_fails_before_diagnostics(plan):"` | — |
| [SRC-829A979985-L000468](../../tests/test_generation_acceptance_matrix.py#L468) | 468 | `"        raise RuntimeError(\"collector failed before the attempt status was known\")"` | — |
| [SRC-829A979985-L000469](../../tests/test_generation_acceptance_matrix.py#L469) | 469 | `""` | — |
| [SRC-829A979985-L000470](../../tests/test_generation_acceptance_matrix.py#L470) | 470 | `"    monkeypatch.setattr(agent, \"_collect_research\", collect_fails_before_diagnostics)"` | — |
| [SRC-829A979985-L000471](../../tests/test_generation_acceptance_matrix.py#L471) | 471 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000472](../../tests/test_generation_acceptance_matrix.py#L472) | 472 | `"        agent,"` | — |
| [SRC-829A979985-L000473](../../tests/test_generation_acceptance_matrix.py#L473) | 473 | `"        \"_generate\","` | — |
| [SRC-829A979985-L000474](../../tests/test_generation_acceptance_matrix.py#L474) | 474 | `"        lambda *args, **kwargs: pytest.fail(\"No synthesis when the research state is unknown\"),"` | — |
| [SRC-829A979985-L000475](../../tests/test_generation_acceptance_matrix.py#L475) | 475 | `"    )"` | — |
| [SRC-829A979985-L000476](../../tests/test_generation_acceptance_matrix.py#L476) | 476 | `""` | — |
| [SRC-829A979985-L000477](../../tests/test_generation_acceptance_matrix.py#L477) | 477 | `"    result = agent.answer(question)"` | — |
| [SRC-829A979985-L000478](../../tests/test_generation_acceptance_matrix.py#L478) | 478 | `""` | — |
| [SRC-829A979985-L000479](../../tests/test_generation_acceptance_matrix.py#L479) | 479 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"unknown_after_research_error\""` | — |
| [SRC-829A979985-L000480](../../tests/test_generation_acceptance_matrix.py#L480) | 480 | `"    assert result[\"search_report\"][\"unique_sources\"] is None"` | — |
| [SRC-829A979985-L000481](../../tests/test_generation_acceptance_matrix.py#L481) | 481 | `"    assert result[\"search_report\"][\"pages_fetched\"] is None"` | — |
| [SRC-829A979985-L000482](../../tests/test_generation_acceptance_matrix.py#L482) | 482 | `"    assert result[\"search_attempted\"] is None"` | — |
| [SRC-829A979985-L000483](../../tests/test_generation_acceptance_matrix.py#L483) | 483 | `"    assert result[\"final_answer_status\"] == \"insufficient_evidence_no_generation\""` | — |
| [SRC-829A979985-L000484](../../tests/test_generation_acceptance_matrix.py#L484) | 484 | `"    assert \"لا أستطيع الجزم\" in result[\"answer\"]"` | — |
| [SRC-829A979985-L000485](../../tests/test_generation_acceptance_matrix.py#L485) | 485 | `"    assert \"لم أجد معلومات موثوقة كافية\" not in result[\"answer\"]"` | — |
| [SRC-829A979985-L000486](../../tests/test_generation_acceptance_matrix.py#L486) | 486 | `""` | — |
| [SRC-829A979985-L000487](../../tests/test_generation_acceptance_matrix.py#L487) | 487 | `""` | — |
| [SRC-829A979985-L000488](../../tests/test_generation_acceptance_matrix.py#L488) | 488 | `"def test_search_extraction_generation_and_task_review_remain_distinct(monkeypatch):"` | — |
| [SRC-829A979985-L000489](../../tests/test_generation_acceptance_matrix.py#L489) | 489 | `"    agent = WebAgent()"` | — |
| [SRC-829A979985-L000490](../../tests/test_generation_acceptance_matrix.py#L490) | 490 | `"    question = \"قارن بين الخيارات من حيث السعر، المساحة، والبيانات الناقصة\""` | — |
| [SRC-829A979985-L000491](../../tests/test_generation_acceptance_matrix.py#L491) | 491 | `"    sources = ["` | — |
| [SRC-829A979985-L000492](../../tests/test_generation_acceptance_matrix.py#L492) | 492 | `"        source("` | — |
| [SRC-829A979985-L000493](../../tests/test_generation_acceptance_matrix.py#L493) | 493 | `"            \"https://one.example/product\","` | — |
| [SRC-829A979985-L000494](../../tests/test_generation_acceptance_matrix.py#L494) | 494 | `"            \"one.example\","` | — |
| [SRC-829A979985-L000495](../../tests/test_generation_acceptance_matrix.py#L495) | 495 | `"            page_fetched=True,"` | — |
| [SRC-829A979985-L000496](../../tests/test_generation_acceptance_matrix.py#L496) | 496 | `"            page_text=\"السعر الإجمالي 100000 جنيه والمساحة 100 متر.\","` | — |
| [SRC-829A979985-L000497](../../tests/test_generation_acceptance_matrix.py#L497) | 497 | `"            provider=\"duckduckgo_html\","` | — |
| [SRC-829A979985-L000498](../../tests/test_generation_acceptance_matrix.py#L498) | 498 | `"        ),"` | — |
| [SRC-829A979985-L000499](../../tests/test_generation_acceptance_matrix.py#L499) | 499 | `"        source("` | — |
| [SRC-829A979985-L000500](../../tests/test_generation_acceptance_matrix.py#L500) | 500 | `"            \"https://two.example/product\","` | — |
| [SRC-829A979985-L000501](../../tests/test_generation_acceptance_matrix.py#L501) | 501 | `"            \"two.example\","` | — |
| [SRC-829A979985-L000502](../../tests/test_generation_acceptance_matrix.py#L502) | 502 | `"            page_fetched=False,"` | — |
| [SRC-829A979985-L000503](../../tests/test_generation_acceptance_matrix.py#L503) | 503 | `"            snippet=\"إعلان يذكر سعرًا دون بيان المساحة.\","` | — |
| [SRC-829A979985-L000504](../../tests/test_generation_acceptance_matrix.py#L504) | 504 | `"            provider=\"bing_rss\","` | — |
| [SRC-829A979985-L000505](../../tests/test_generation_acceptance_matrix.py#L505) | 505 | `"        ),"` | — |
| [SRC-829A979985-L000506](../../tests/test_generation_acceptance_matrix.py#L506) | 506 | `"    ]"` | — |
| [SRC-829A979985-L000507](../../tests/test_generation_acceptance_matrix.py#L507) | 507 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000508](../../tests/test_generation_acceptance_matrix.py#L508) | 508 | `"        agent,"` | — |
| [SRC-829A979985-L000509](../../tests/test_generation_acceptance_matrix.py#L509) | 509 | `"        \"_plan_search\","` | — |
| [SRC-829A979985-L000510](../../tests/test_generation_acceptance_matrix.py#L510) | 510 | `"        lambda question, history: {"` | — |
| [SRC-829A979985-L000511](../../tests/test_generation_acceptance_matrix.py#L511) | 511 | `"            \"queries\": [question],"` | — |
| [SRC-829A979985-L000512](../../tests/test_generation_acceptance_matrix.py#L512) | 512 | `"            \"direct_urls\": [],"` | — |
| [SRC-829A979985-L000513](../../tests/test_generation_acceptance_matrix.py#L513) | 513 | `"            \"social_focus\": False,"` | — |
| [SRC-829A979985-L000514](../../tests/test_generation_acceptance_matrix.py#L514) | 514 | `"            \"freshness\": \"any\","` | — |
| [SRC-829A979985-L000515](../../tests/test_generation_acceptance_matrix.py#L515) | 515 | `"            \"depth\": \"deep\","` | — |
| [SRC-829A979985-L000516](../../tests/test_generation_acceptance_matrix.py#L516) | 516 | `"            \"platforms\": [],"` | — |
| [SRC-829A979985-L000517](../../tests/test_generation_acceptance_matrix.py#L517) | 517 | `"            \"planning_method\": \"test\","` | — |
| [SRC-829A979985-L000518](../../tests/test_generation_acceptance_matrix.py#L518) | 518 | `"        },"` | — |
| [SRC-829A979985-L000519](../../tests/test_generation_acceptance_matrix.py#L519) | 519 | `"    )"` | — |
| [SRC-829A979985-L000520](../../tests/test_generation_acceptance_matrix.py#L520) | 520 | `"    monkeypatch.setattr("` | — |
| [SRC-829A979985-L000521](../../tests/test_generation_acceptance_matrix.py#L521) | 521 | `"        agent,"` | — |
| [SRC-829A979985-L000522](../../tests/test_generation_acceptance_matrix.py#L522) | 522 | `"        \"_collect_research\","` | — |
| [SRC-829A979985-L000523](../../tests/test_generation_acceptance_matrix.py#L523) | 523 | `"        lambda plan: ("` | — |
| [SRC-829A979985-L000524](../../tests/test_generation_acceptance_matrix.py#L524) | 524 | `"            sources,"` | — |
| [SRC-829A979985-L000525](../../tests/test_generation_acceptance_matrix.py#L525) | 525 | `"            [],"` | — |
| [SRC-829A979985-L000526](../../tests/test_generation_acceptance_matrix.py#L526) | 526 | `"            {"` | — |
| [SRC-829A979985-L000527](../../tests/test_generation_acceptance_matrix.py#L527) | 527 | `"                \"queries_planned\": 1,"` | — |
| [SRC-829A979985-L000528](../../tests/test_generation_acceptance_matrix.py#L528) | 528 | `"                \"queries_attempted\": 1,"` | — |
| [SRC-829A979985-L000529](../../tests/test_generation_acceptance_matrix.py#L529) | 529 | `"                \"search_attempted\": True,"` | — |
| [SRC-829A979985-L000530](../../tests/test_generation_acceptance_matrix.py#L530) | 530 | `"                \"search_outcome\": \"attempted_with_usable_sources\","` | — |
| [SRC-829A979985-L000531](../../tests/test_generation_acceptance_matrix.py#L531) | 531 | `"                \"unique_sources\": 2,"` | — |
| [SRC-829A979985-L000532](../../tests/test_generation_acceptance_matrix.py#L532) | 532 | `"                \"pages_fetched\": 1,"` | — |
| [SRC-829A979985-L000533](../../tests/test_generation_acceptance_matrix.py#L533) | 533 | `"                \"providers_used\": [\"duckduckgo_html\", \"bing_rss\"],"` | — |
| [SRC-829A979985-L000534](../../tests/test_generation_acceptance_matrix.py#L534) | 534 | `"                \"provider_counts\": {\"duckduckgo_html\": 1, \"bing_rss\": 1},"` | — |
| [SRC-829A979985-L000535](../../tests/test_generation_acceptance_matrix.py#L535) | 535 | `"                \"platform_counts\": {\"web\": 2},"` | — |
| [SRC-829A979985-L000536](../../tests/test_generation_acceptance_matrix.py#L536) | 536 | `"                \"social_direct_results\": 0,"` | — |
| [SRC-829A979985-L000537](../../tests/test_generation_acceptance_matrix.py#L537) | 537 | `"                \"provider_diagnostics\": [],"` | — |
| [SRC-829A979985-L000538](../../tests/test_generation_acceptance_matrix.py#L538) | 538 | `"                \"evidence_signals\": {},"` | — |
| [SRC-829A979985-L000539](../../tests/test_generation_acceptance_matrix.py#L539) | 539 | `"            },"` | — |
| [SRC-829A979985-L000540](../../tests/test_generation_acceptance_matrix.py#L540) | 540 | `"        ),"` | — |
| [SRC-829A979985-L000541](../../tests/test_generation_acceptance_matrix.py#L541) | 541 | `"    )"` | — |
| [SRC-829A979985-L000542](../../tests/test_generation_acceptance_matrix.py#L542) | 542 | `"    monkeypatch.setattr(agent, \"_source_matches_query\", lambda query, item: True)"` | — |
| [SRC-829A979985-L000543](../../tests/test_generation_acceptance_matrix.py#L543) | 543 | `"    final_draft = \"الخلاصة: يوجد اختلاف في اكتمال البيانات، ولا يمكن حسم المقارنة من المقتطف وحده [المصدر 1].\""` | — |
| [SRC-829A979985-L000544](../../tests/test_generation_acceptance_matrix.py#L544) | 544 | `"    monkeypatch.setattr(agent, \"_generate\", lambda *args, **kwargs: final_draft)"` | — |
| [SRC-829A979985-L000545](../../tests/test_generation_acceptance_matrix.py#L545) | 545 | `"    monkeypatch.setattr(agent, \"_review_answer\", lambda question, answer, sources: answer)"` | — |
| [SRC-829A979985-L000546](../../tests/test_generation_acceptance_matrix.py#L546) | 546 | `""` | — |
| [SRC-829A979985-L000547](../../tests/test_generation_acceptance_matrix.py#L547) | 547 | `"    result = agent.answer(question)"` | — |
| [SRC-829A979985-L000548](../../tests/test_generation_acceptance_matrix.py#L548) | 548 | `""` | — |
| [SRC-829A979985-L000549](../../tests/test_generation_acceptance_matrix.py#L549) | 549 | `"    assert result[\"search_attempted\"] is True"` | — |
| [SRC-829A979985-L000550](../../tests/test_generation_acceptance_matrix.py#L550) | 550 | `"    assert result[\"used_web_search\"] is True"` | — |
| [SRC-829A979985-L000551](../../tests/test_generation_acceptance_matrix.py#L551) | 551 | `"    assert len(result[\"sources\"]) == 2"` | — |
| [SRC-829A979985-L000552](../../tests/test_generation_acceptance_matrix.py#L552) | 552 | `"    assert result[\"search_report\"][\"search_outcome\"] == \"attempted_with_usable_sources\""` | — |
| [SRC-829A979985-L000553](../../tests/test_generation_acceptance_matrix.py#L553) | 553 | `"    assert result[\"search_report\"][\"pages_fetched\"] == 1"` | — |
| [SRC-829A979985-L000554](../../tests/test_generation_acceptance_matrix.py#L554) | 554 | `"    assert result[\"final_answer_status\"] == \"model_answer_generated\""` | — |
| [SRC-829A979985-L000555](../../tests/test_generation_acceptance_matrix.py#L555) | 555 | `"    assert result[\"search_report\"][\"second_pass_review\"] == \"model_claim_audit_completed\""` | — |
