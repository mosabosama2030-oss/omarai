# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **010**
- سجلات الأسطر: **800**
- النطاق: SRC-E599346ABE-L000300 إلى SRC-E599346ABE-L001099
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-E599346ABE — [docs/generate_index.py](../generate_index.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E599346ABE-L000300](../generate_index.py#L300) | 300 | `""` | — |
| [SRC-E599346ABE-L000301](../generate_index.py#L301) | 301 | `"    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:"` | — |
| [SRC-E599346ABE-L000302](../generate_index.py#L302) | 302 | `"        \"\"\"Record a synchronous function or method and nested definitions.\"\"\""` | — |
| [SRC-E599346ABE-L000303](../generate_index.py#L303) | 303 | `"        self._record_definition(node, \"دالة\")"` | — |
| [SRC-E599346ABE-L000304](../generate_index.py#L304) | 304 | `"        self.scope.append(node.name)"` | — |
| [SRC-E599346ABE-L000305](../generate_index.py#L305) | 305 | `"        self.function_depth += 1"` | — |
| [SRC-E599346ABE-L000306](../generate_index.py#L306) | 306 | `"        try:"` | — |
| [SRC-E599346ABE-L000307](../generate_index.py#L307) | 307 | `"            self.generic_visit(node)"` | — |
| [SRC-E599346ABE-L000308](../generate_index.py#L308) | 308 | `"        finally:"` | — |
| [SRC-E599346ABE-L000309](../generate_index.py#L309) | 309 | `"            self.function_depth -= 1"` | — |
| [SRC-E599346ABE-L000310](../generate_index.py#L310) | 310 | `"            self.scope.pop()"` | — |
| [SRC-E599346ABE-L000311](../generate_index.py#L311) | 311 | `""` | — |
| [SRC-E599346ABE-L000312](../generate_index.py#L312) | 312 | `"    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:"` | — |
| [SRC-E599346ABE-L000313](../generate_index.py#L313) | 313 | `"        \"\"\"Record an asynchronous function or method and nested definitions.\"\"\""` | — |
| [SRC-E599346ABE-L000314](../generate_index.py#L314) | 314 | `"        self._record_definition(node, \"دالة غير متزامنة\")"` | — |
| [SRC-E599346ABE-L000315](../generate_index.py#L315) | 315 | `"        self.scope.append(node.name)"` | — |
| [SRC-E599346ABE-L000316](../generate_index.py#L316) | 316 | `"        self.function_depth += 1"` | — |
| [SRC-E599346ABE-L000317](../generate_index.py#L317) | 317 | `"        try:"` | — |
| [SRC-E599346ABE-L000318](../generate_index.py#L318) | 318 | `"            self.generic_visit(node)"` | — |
| [SRC-E599346ABE-L000319](../generate_index.py#L319) | 319 | `"        finally:"` | — |
| [SRC-E599346ABE-L000320](../generate_index.py#L320) | 320 | `"            self.function_depth -= 1"` | — |
| [SRC-E599346ABE-L000321](../generate_index.py#L321) | 321 | `"            self.scope.pop()"` | — |
| [SRC-E599346ABE-L000322](../generate_index.py#L322) | 322 | `""` | — |
| [SRC-E599346ABE-L000323](../generate_index.py#L323) | 323 | `""` | — |
| [SRC-E599346ABE-L000324](../generate_index.py#L324) | 324 | `"def _is_sensitive_or_runtime_path(path: Path) -> bool:"` | — |
| [SRC-E599346ABE-L000325](../generate_index.py#L325) | 325 | `"    \"\"\"Exclude known local secrets, credential directories, runtime data and keys.\"\"\""` | — |
| [SRC-E599346ABE-L000326](../generate_index.py#L326) | 326 | `"    name = path.name.lower()"` | — |
| [SRC-E599346ABE-L000327](../generate_index.py#L327) | 327 | `"    parent_names = {part.lower() for part in path.parts[:-1]}"` | — |
| [SRC-E599346ABE-L000328](../generate_index.py#L328) | 328 | `"    if name in SENSITIVE_FILENAMES:"` | — |
| [SRC-E599346ABE-L000329](../generate_index.py#L329) | 329 | `"        return True"` | — |
| [SRC-E599346ABE-L000330](../generate_index.py#L330) | 330 | `"    if parent_names & SENSITIVE_DIRECTORY_NAMES:"` | — |
| [SRC-E599346ABE-L000331](../generate_index.py#L331) | 331 | `"        return True"` | — |
| [SRC-E599346ABE-L000332](../generate_index.py#L332) | 332 | `"    if name.startswith(\".env\") and name != \".env.example\":"` | — |
| [SRC-E599346ABE-L000333](../generate_index.py#L333) | 333 | `"        return True"` | — |
| [SRC-E599346ABE-L000334](../generate_index.py#L334) | 334 | `"    if name.endswith((\".example\", \".sample\", \".template\")):"` | — |
| [SRC-E599346ABE-L000335](../generate_index.py#L335) | 335 | `"        return False"` | — |
| [SRC-E599346ABE-L000336](../generate_index.py#L336) | 336 | `"    if SENSITIVE_NAME_RE.search(name) and path.suffix.lower() in SENSITIVE_CONFIG_SUFFIXES:"` | — |
| [SRC-E599346ABE-L000337](../generate_index.py#L337) | 337 | `"        return True"` | — |
| [SRC-E599346ABE-L000338](../generate_index.py#L338) | 338 | `"    return path.suffix.lower() in EXCLUDED_SUFFIXES"` | — |
| [SRC-E599346ABE-L000339](../generate_index.py#L339) | 339 | `""` | — |
| [SRC-E599346ABE-L000340](../generate_index.py#L340) | 340 | `""` | — |
| [SRC-E599346ABE-L000341](../generate_index.py#L341) | 341 | `"def _stable_file_id(relative_file: str) -> str:"` | — |
| [SRC-E599346ABE-L000342](../generate_index.py#L342) | 342 | `"    \"\"\"Return a deterministic path-derived identifier without hashing file contents.\"\"\""` | — |
| [SRC-E599346ABE-L000343](../generate_index.py#L343) | 343 | `"    digest = hashlib.sha256(relative_file.encode(\"utf-8\")).hexdigest()[:10].upper()"` | — |
| [SRC-E599346ABE-L000344](../generate_index.py#L344) | 344 | `"    return f\"FILE-{digest}\""` | — |
| [SRC-E599346ABE-L000345](../generate_index.py#L345) | 345 | `""` | — |
| [SRC-E599346ABE-L000346](../generate_index.py#L346) | 346 | `""` | — |
| [SRC-E599346ABE-L000347](../generate_index.py#L347) | 347 | `"def _category_for_path(relative_file: str) -> str:"` | — |
| [SRC-E599346ABE-L000348](../generate_index.py#L348) | 348 | `"    \"\"\"Assign an understandable navigation category from the repository-relative path.\"\"\""` | — |
| [SRC-E599346ABE-L000349](../generate_index.py#L349) | 349 | `"    normalized = relative_file.replace(\"\\\\\", \"/\")"` | — |
| [SRC-E599346ABE-L000350](../generate_index.py#L350) | 350 | `"    name = Path(normalized).name.lower()"` | — |
| [SRC-E599346ABE-L000351](../generate_index.py#L351) | 351 | `"    suffix = Path(normalized).suffix.lower()"` | — |
| [SRC-E599346ABE-L000352](../generate_index.py#L352) | 352 | `"    if normalized.startswith(\"tests/\") or \"/tests/\" in normalized:"` | — |
| [SRC-E599346ABE-L000353](../generate_index.py#L353) | 353 | `"        return \"اختبارات\""` | — |
| [SRC-E599346ABE-L000354](../generate_index.py#L354) | 354 | `"    if normalized.startswith(\".github/workflows/\"):"` | — |
| [SRC-E599346ABE-L000355](../generate_index.py#L355) | 355 | `"        return \"CI وأتمتة\""` | — |
| [SRC-E599346ABE-L000356](../generate_index.py#L356) | 356 | `"    if normalized.startswith(\"agents/\"):"` | — |
| [SRC-E599346ABE-L000357](../generate_index.py#L357) | 357 | `"        return \"الوكيل والمنطق\""` | — |
| [SRC-E599346ABE-L000358](../generate_index.py#L358) | 358 | `"    if normalized.startswith(\"api/\"):"` | — |
| [SRC-E599346ABE-L000359](../generate_index.py#L359) | 359 | `"        return \"واجهات API\""` | — |
| [SRC-E599346ABE-L000360](../generate_index.py#L360) | 360 | `"    if normalized.startswith(\"cli/\"):"` | — |
| [SRC-E599346ABE-L000361](../generate_index.py#L361) | 361 | `"        return \"واجهة سطر الأوامر\""` | — |
| [SRC-E599346ABE-L000362](../generate_index.py#L362) | 362 | `"    if normalized.startswith(\"docs/\"):"` | — |
| [SRC-E599346ABE-L000363](../generate_index.py#L363) | 363 | `"        return \"وثائق وفهرسة\""` | — |
| [SRC-E599346ABE-L000364](../generate_index.py#L364) | 364 | `"    if normalized.startswith((\"web/\", \"static/\", \"templates/\")) or suffix in {"` | — |
| [SRC-E599346ABE-L000365](../generate_index.py#L365) | 365 | `"        \".html\", \".htm\", \".css\", \".scss\", \".js\", \".mjs\", \".cjs\", \".jsx\", \".ts\", \".tsx\","` | — |
| [SRC-E599346ABE-L000366](../generate_index.py#L366) | 366 | `"        \".vue\", \".svelte\","` | — |
| [SRC-E599346ABE-L000367](../generate_index.py#L367) | 367 | `"    }:"` | — |
| [SRC-E599346ABE-L000368](../generate_index.py#L368) | 368 | `"        return \"واجهة الويب\""` | — |
| [SRC-E599346ABE-L000369](../generate_index.py#L369) | 369 | `"    if name in {"` | — |
| [SRC-E599346ABE-L000370](../generate_index.py#L370) | 370 | `"        \"dockerfile\", \"makefile\", \"procfile\", \"pyproject.toml\","` | — |
| [SRC-E599346ABE-L000371](../generate_index.py#L371) | 371 | `"        \"requirements.txt\", \"requirements-dev.txt\", \".gitignore\","` | — |
| [SRC-E599346ABE-L000372](../generate_index.py#L372) | 372 | `"        \".dockerignore\", \".editorconfig\","` | — |
| [SRC-E599346ABE-L000373](../generate_index.py#L373) | 373 | `"    } or suffix in {\".yml\", \".yaml\", \".toml\", \".ini\", \".cfg\", \".json\", \".jsonl\", \".xml\"}:"` | — |
| [SRC-E599346ABE-L000374](../generate_index.py#L374) | 374 | `"        return \"إعدادات وتشغيل\""` | — |
| [SRC-E599346ABE-L000375](../generate_index.py#L375) | 375 | `"    if suffix in {\".md\", \".rst\", \".txt\"}:"` | — |
| [SRC-E599346ABE-L000376](../generate_index.py#L376) | 376 | `"        return \"وثائق ونصوص\""` | — |
| [SRC-E599346ABE-L000377](../generate_index.py#L377) | 377 | `"    return \"ملفات أخرى\""` | — |
| [SRC-E599346ABE-L000378](../generate_index.py#L378) | 378 | `""` | — |
| [SRC-E599346ABE-L000379](../generate_index.py#L379) | 379 | `""` | — |
| [SRC-E599346ABE-L000380](../generate_index.py#L380) | 380 | `"def discover_repository_files(root: Path) -> list[Path]:"` | — |
| [SRC-E599346ABE-L000381](../generate_index.py#L381) | 381 | `"    \"\"\"Return the stable file inventory, excluding the generated index and runtime data.\"\"\""` | — |
| [SRC-E599346ABE-L000382](../generate_index.py#L382) | 382 | `"    discovered: list[Path] = []"` | — |
| [SRC-E599346ABE-L000383](../generate_index.py#L383) | 383 | `"    for current_directory, directory_names, file_names in os.walk("` | — |
| [SRC-E599346ABE-L000384](../generate_index.py#L384) | 384 | `"        root,"` | — |
| [SRC-E599346ABE-L000385](../generate_index.py#L385) | 385 | `"        topdown=True,"` | — |
| [SRC-E599346ABE-L000386](../generate_index.py#L386) | 386 | `"        followlinks=False,"` | — |
| [SRC-E599346ABE-L000387](../generate_index.py#L387) | 387 | `"    ):"` | — |
| [SRC-E599346ABE-L000388](../generate_index.py#L388) | 388 | `"        directory_names[:] = sorted("` | — |
| [SRC-E599346ABE-L000389](../generate_index.py#L389) | 389 | `"            name"` | — |
| [SRC-E599346ABE-L000390](../generate_index.py#L390) | 390 | `"            for name in directory_names"` | — |
| [SRC-E599346ABE-L000391](../generate_index.py#L391) | 391 | `"            if name not in EXCLUDED_DIRECTORIES"` | — |
| [SRC-E599346ABE-L000392](../generate_index.py#L392) | 392 | `"            and not name.lower().endswith((\".egg-info\", \".dist-info\"))"` | — |
| [SRC-E599346ABE-L000393](../generate_index.py#L393) | 393 | `"            and not (Path(current_directory) / name).is_symlink()"` | — |
| [SRC-E599346ABE-L000394](../generate_index.py#L394) | 394 | `"        )"` | — |
| [SRC-E599346ABE-L000395](../generate_index.py#L395) | 395 | `"        for file_name in sorted(file_names):"` | — |
| [SRC-E599346ABE-L000396](../generate_index.py#L396) | 396 | `"            candidate = Path(current_directory) / file_name"` | — |
| [SRC-E599346ABE-L000397](../generate_index.py#L397) | 397 | `"            if candidate.is_symlink() or _is_sensitive_or_runtime_path(candidate):"` | — |
| [SRC-E599346ABE-L000398](../generate_index.py#L398) | 398 | `"                continue"` | — |
| [SRC-E599346ABE-L000399](../generate_index.py#L399) | 399 | `"            relative_file = candidate.relative_to(root).as_posix()"` | — |
| [SRC-E599346ABE-L000400](../generate_index.py#L400) | 400 | `"            if ("` | — |
| [SRC-E599346ABE-L000401](../generate_index.py#L401) | 401 | `"                relative_file in INDEX_OUTPUT_PATHS"` | — |
| [SRC-E599346ABE-L000402](../generate_index.py#L402) | 402 | `"                or relative_file.startswith(SOURCE_LINES_PAGES_DIR + \"/\")"` | — |
| [SRC-E599346ABE-L000403](../generate_index.py#L403) | 403 | `"            ):"` | — |
| [SRC-E599346ABE-L000404](../generate_index.py#L404) | 404 | `"                # Exclude generated index outputs to prevent self-indexing loops."` | — |
| [SRC-E599346ABE-L000405](../generate_index.py#L405) | 405 | `"                continue"` | — |
| [SRC-E599346ABE-L000406](../generate_index.py#L406) | 406 | `"            discovered.append(candidate)"` | — |
| [SRC-E599346ABE-L000407](../generate_index.py#L407) | 407 | `""` | — |
| [SRC-E599346ABE-L000408](../generate_index.py#L408) | 408 | `"    return sorted("` | — |
| [SRC-E599346ABE-L000409](../generate_index.py#L409) | 409 | `"        discovered,"` | — |
| [SRC-E599346ABE-L000410](../generate_index.py#L410) | 410 | `"        key=lambda path: path.relative_to(root).as_posix().casefold(),"` | — |
| [SRC-E599346ABE-L000411](../generate_index.py#L411) | 411 | `"    )"` | — |
| [SRC-E599346ABE-L000412](../generate_index.py#L412) | 412 | `""` | — |
| [SRC-E599346ABE-L000413](../generate_index.py#L413) | 413 | `""` | — |
| [SRC-E599346ABE-L000414](../generate_index.py#L414) | 414 | `"def _read_text_bounded(path: Path) -> str \| None:"` | — |
| [SRC-E599346ABE-L000415](../generate_index.py#L415) | 415 | `"    \"\"\"Read supported UTF-8 text files only when they are within the scan-size bound.\"\"\""` | — |
| [SRC-E599346ABE-L000416](../generate_index.py#L416) | 416 | `"    try:"` | — |
| [SRC-E599346ABE-L000417](../generate_index.py#L417) | 417 | `"        if path.stat().st_size > MAX_INDEXED_TEXT_BYTES:"` | — |
| [SRC-E599346ABE-L000418](../generate_index.py#L418) | 418 | `"            return None"` | — |
| [SRC-E599346ABE-L000419](../generate_index.py#L419) | 419 | `"        if path.suffix.lower() == \".py\":"` | — |
| [SRC-E599346ABE-L000420](../generate_index.py#L420) | 420 | `"            with tokenize.open(str(path)) as source_stream:"` | — |
| [SRC-E599346ABE-L000421](../generate_index.py#L421) | 421 | `"                text = source_stream.read()"` | — |
| [SRC-E599346ABE-L000422](../generate_index.py#L422) | 422 | `"        else:"` | — |
| [SRC-E599346ABE-L000423](../generate_index.py#L423) | 423 | `"            text = path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-E599346ABE-L000424](../generate_index.py#L424) | 424 | `"        if \"\\x00\" in text:"` | — |
| [SRC-E599346ABE-L000425](../generate_index.py#L425) | 425 | `"            return None"` | — |
| [SRC-E599346ABE-L000426](../generate_index.py#L426) | 426 | `"        return text"` | — |
| [SRC-E599346ABE-L000427](../generate_index.py#L427) | 427 | `"    except (OSError, UnicodeError, LookupError, tokenize.TokenError):"` | — |
| [SRC-E599346ABE-L000428](../generate_index.py#L428) | 428 | `"        return None"` | — |
| [SRC-E599346ABE-L000429](../generate_index.py#L429) | 429 | `""` | — |
| [SRC-E599346ABE-L000430](../generate_index.py#L430) | 430 | `""` | — |
| [SRC-E599346ABE-L000431](../generate_index.py#L431) | 431 | `"def _count_lines(text: str) -> int:"` | — |
| [SRC-E599346ABE-L000432](../generate_index.py#L432) | 432 | `"    \"\"\"Count source lines without adding an extra line for a trailing newline.\"\"\""` | — |
| [SRC-E599346ABE-L000433](../generate_index.py#L433) | 433 | `"    if not text:"` | — |
| [SRC-E599346ABE-L000434](../generate_index.py#L434) | 434 | `"        return 0"` | — |
| [SRC-E599346ABE-L000435](../generate_index.py#L435) | 435 | `"    return text.count(\"\\n\") + (not text.endswith(\"\\n\"))"` | — |
| [SRC-E599346ABE-L000436](../generate_index.py#L436) | 436 | `""` | — |
| [SRC-E599346ABE-L000437](../generate_index.py#L437) | 437 | `""` | — |
| [SRC-E599346ABE-L000438](../generate_index.py#L438) | 438 | `"def _file_type(path: Path) -> str:"` | — |
| [SRC-E599346ABE-L000439](../generate_index.py#L439) | 439 | `"    \"\"\"Return a readable file type based on a known filename or extension.\"\"\""` | — |
| [SRC-E599346ABE-L000440](../generate_index.py#L440) | 440 | `"    name = path.name.lower()"` | — |
| [SRC-E599346ABE-L000441](../generate_index.py#L441) | 441 | `"    if name in {\"dockerfile\", \"makefile\", \"procfile\"}:"` | — |
| [SRC-E599346ABE-L000442](../generate_index.py#L442) | 442 | `"        return name.capitalize()"` | — |
| [SRC-E599346ABE-L000443](../generate_index.py#L443) | 443 | `"    suffix = path.suffix.lower()"` | — |
| [SRC-E599346ABE-L000444](../generate_index.py#L444) | 444 | `"    labels = {"` | — |
| [SRC-E599346ABE-L000445](../generate_index.py#L445) | 445 | `"        \".py\": \"Python\","` | — |
| [SRC-E599346ABE-L000446](../generate_index.py#L446) | 446 | `"        \".html\": \"HTML\","` | — |
| [SRC-E599346ABE-L000447](../generate_index.py#L447) | 447 | `"        \".htm\": \"HTML\","` | — |
| [SRC-E599346ABE-L000448](../generate_index.py#L448) | 448 | `"        \".js\": \"JavaScript\","` | — |
| [SRC-E599346ABE-L000449](../generate_index.py#L449) | 449 | `"        \".mjs\": \"JavaScript module\","` | — |
| [SRC-E599346ABE-L000450](../generate_index.py#L450) | 450 | `"        \".cjs\": \"CommonJS\","` | — |
| [SRC-E599346ABE-L000451](../generate_index.py#L451) | 451 | `"        \".jsx\": \"React JSX\","` | — |
| [SRC-E599346ABE-L000452](../generate_index.py#L452) | 452 | `"        \".ts\": \"TypeScript\","` | — |
| [SRC-E599346ABE-L000453](../generate_index.py#L453) | 453 | `"        \".tsx\": \"TypeScript JSX\","` | — |
| [SRC-E599346ABE-L000454](../generate_index.py#L454) | 454 | `"        \".css\": \"CSS\","` | — |
| [SRC-E599346ABE-L000455](../generate_index.py#L455) | 455 | `"        \".scss\": \"SCSS\","` | — |
| [SRC-E599346ABE-L000456](../generate_index.py#L456) | 456 | `"        \".md\": \"Markdown\","` | — |
| [SRC-E599346ABE-L000457](../generate_index.py#L457) | 457 | `"        \".yml\": \"YAML\","` | — |
| [SRC-E599346ABE-L000458](../generate_index.py#L458) | 458 | `"        \".yaml\": \"YAML\","` | — |
| [SRC-E599346ABE-L000459](../generate_index.py#L459) | 459 | `"        \".json\": \"JSON\","` | — |
| [SRC-E599346ABE-L000460](../generate_index.py#L460) | 460 | `"        \".toml\": \"TOML\","` | — |
| [SRC-E599346ABE-L000461](../generate_index.py#L461) | 461 | `"        \".sh\": \"Shell\","` | — |
| [SRC-E599346ABE-L000462](../generate_index.py#L462) | 462 | `"        \".sql\": \"SQL\","` | — |
| [SRC-E599346ABE-L000463](../generate_index.py#L463) | 463 | `"        \".txt\": \"Text\","` | — |
| [SRC-E599346ABE-L000464](../generate_index.py#L464) | 464 | `"        \".svg\": \"SVG\","` | — |
| [SRC-E599346ABE-L000465](../generate_index.py#L465) | 465 | `"        \".png\": \"PNG image\","` | — |
| [SRC-E599346ABE-L000466](../generate_index.py#L466) | 466 | `"        \".jpg\": \"JPEG image\","` | — |
| [SRC-E599346ABE-L000467](../generate_index.py#L467) | 467 | `"        \".jpeg\": \"JPEG image\","` | — |
| [SRC-E599346ABE-L000468](../generate_index.py#L468) | 468 | `"        \".webp\": \"WebP image\","` | — |
| [SRC-E599346ABE-L000469](../generate_index.py#L469) | 469 | `"    }"` | — |
| [SRC-E599346ABE-L000470](../generate_index.py#L470) | 470 | `"    return labels.get(suffix, suffix[1:].upper() if suffix else \"بدون امتداد\")"` | — |
| [SRC-E599346ABE-L000471](../generate_index.py#L471) | 471 | `""` | — |
| [SRC-E599346ABE-L000472](../generate_index.py#L472) | 472 | `""` | — |
| [SRC-E599346ABE-L000473](../generate_index.py#L473) | 473 | `"def _indexing_scope(path: Path, text: str \| None) -> str:"` | — |
| [SRC-E599346ABE-L000474](../generate_index.py#L474) | 474 | `"    \"\"\"Describe precisely whether a file receives symbol extraction or path inventory only.\"\"\""` | — |
| [SRC-E599346ABE-L000475](../generate_index.py#L475) | 475 | `"    if text is None:"` | — |
| [SRC-E599346ABE-L000476](../generate_index.py#L476) | 476 | `"        return \"جرد المسار والحجم فقط (ثنائي/غير مقروء/أكبر من حد الفحص)\""` | — |
| [SRC-E599346ABE-L000477](../generate_index.py#L477) | 477 | `"    suffix = path.suffix.lower()"` | — |
| [SRC-E599346ABE-L000478](../generate_index.py#L478) | 478 | `"    if suffix in PYTHON_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000479](../generate_index.py#L479) | 479 | `"        return \"جرد الملف + AST Python\""` | — |
| [SRC-E599346ABE-L000480](../generate_index.py#L480) | 480 | `"    if suffix in JAVASCRIPT_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000481](../generate_index.py#L481) | 481 | `"        return \"جرد الملف + رموز JavaScript/TypeScript ساكنة\""` | — |
| [SRC-E599346ABE-L000482](../generate_index.py#L482) | 482 | `"    if suffix in CSS_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000483](../generate_index.py#L483) | 483 | `"        return \"جرد الملف + محددات CSS والمتغيرات المخصصة\""` | — |
| [SRC-E599346ABE-L000484](../generate_index.py#L484) | 484 | `"    if suffix in {\".html\", \".htm\"}:"` | — |
| [SRC-E599346ABE-L000485](../generate_index.py#L485) | 485 | `"        return \"جرد الملف + معرفات HTML والرموز داخل script/style\""` | — |
| [SRC-E599346ABE-L000486](../generate_index.py#L486) | 486 | `"    if suffix == \".md\":"` | — |
| [SRC-E599346ABE-L000487](../generate_index.py#L487) | 487 | `"        return \"جرد الملف + عناوين Markdown\""` | — |
| [SRC-E599346ABE-L000488](../generate_index.py#L488) | 488 | `"    if suffix in CONFIG_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000489](../generate_index.py#L489) | 489 | `"        return \"جرد الملف + مفاتيح إعداد ساكنة\""` | — |
| [SRC-E599346ABE-L000490](../generate_index.py#L490) | 490 | `"    if suffix == \".sh\":"` | — |
| [SRC-E599346ABE-L000491](../generate_index.py#L491) | 491 | `"        return \"جرد الملف + دوال Shell\""` | — |
| [SRC-E599346ABE-L000492](../generate_index.py#L492) | 492 | `"    if path.name.lower() in {\"dockerfile\", \"makefile\", \"procfile\"}:"` | — |
| [SRC-E599346ABE-L000493](../generate_index.py#L493) | 493 | `"        return \"جرد الملف + أسماء إعدادات عامة إن وجدت\""` | — |
| [SRC-E599346ABE-L000494](../generate_index.py#L494) | 494 | `"    if path.name.lower() == \".env.example\" or suffix == \".example\":"` | — |
| [SRC-E599346ABE-L000495](../generate_index.py#L495) | 495 | `"        return \"جرد الملف + أسماء إعدادات عامة إن وجدت\""` | — |
| [SRC-E599346ABE-L000496](../generate_index.py#L496) | 496 | `"    return \"جرد ملف نصي فقط\""` | — |
| [SRC-E599346ABE-L000497](../generate_index.py#L497) | 497 | `""` | — |
| [SRC-E599346ABE-L000498](../generate_index.py#L498) | 498 | `""` | — |
| [SRC-E599346ABE-L000499](../generate_index.py#L499) | 499 | `"def build_file_inventory(root: Path) -> list[IndexedFile]:"` | — |
| [SRC-E599346ABE-L000500](../generate_index.py#L500) | 500 | `"    \"\"\"Inventory repository files and record whether static symbol scanning was possible.\"\"\""` | — |
| [SRC-E599346ABE-L000501](../generate_index.py#L501) | 501 | `"    inventory: list[IndexedFile] = []"` | — |
| [SRC-E599346ABE-L000502](../generate_index.py#L502) | 502 | `"    for path in discover_repository_files(root):"` | — |
| [SRC-E599346ABE-L000503](../generate_index.py#L503) | 503 | `"        text = _read_text_bounded(path)"` | — |
| [SRC-E599346ABE-L000504](../generate_index.py#L504) | 504 | `"        inventory.append("` | — |
| [SRC-E599346ABE-L000505](../generate_index.py#L505) | 505 | `"            IndexedFile("` | — |
| [SRC-E599346ABE-L000506](../generate_index.py#L506) | 506 | `"                file=path.relative_to(root).as_posix(),"` | — |
| [SRC-E599346ABE-L000507](../generate_index.py#L507) | 507 | `"                file_type=_file_type(path),"` | — |
| [SRC-E599346ABE-L000508](../generate_index.py#L508) | 508 | `"                size_bytes=path.stat().st_size,"` | — |
| [SRC-E599346ABE-L000509](../generate_index.py#L509) | 509 | `"                line_count=_count_lines(text) if text is not None else None,"` | — |
| [SRC-E599346ABE-L000510](../generate_index.py#L510) | 510 | `"                indexing_scope=_indexing_scope(path, text),"` | — |
| [SRC-E599346ABE-L000511](../generate_index.py#L511) | 511 | `"                file_id=_stable_file_id(path.relative_to(root).as_posix()),"` | — |
| [SRC-E599346ABE-L000512](../generate_index.py#L512) | 512 | `"                category=_category_for_path(path.relative_to(root).as_posix()),"` | — |
| [SRC-E599346ABE-L000513](../generate_index.py#L513) | 513 | `"            )"` | — |
| [SRC-E599346ABE-L000514](../generate_index.py#L514) | 514 | `"        )"` | — |
| [SRC-E599346ABE-L000515](../generate_index.py#L515) | 515 | `"    return inventory"` | — |
| [SRC-E599346ABE-L000516](../generate_index.py#L516) | 516 | `""` | — |
| [SRC-E599346ABE-L000517](../generate_index.py#L517) | 517 | `""` | — |
| [SRC-E599346ABE-L000518](../generate_index.py#L518) | 518 | `"def discover_python_files(root: Path) -> list[Path]:"` | — |
| [SRC-E599346ABE-L000519](../generate_index.py#L519) | 519 | `"    \"\"\"Return sorted Python files from the eligible repository inventory.\"\"\""` | — |
| [SRC-E599346ABE-L000520](../generate_index.py#L520) | 520 | `"    return ["` | — |
| [SRC-E599346ABE-L000521](../generate_index.py#L521) | 521 | `"        path"` | — |
| [SRC-E599346ABE-L000522](../generate_index.py#L522) | 522 | `"        for path in discover_repository_files(root)"` | — |
| [SRC-E599346ABE-L000523](../generate_index.py#L523) | 523 | `"        if path.suffix.lower() == \".py\""` | — |
| [SRC-E599346ABE-L000524](../generate_index.py#L524) | 524 | `"    ]"` | — |
| [SRC-E599346ABE-L000525](../generate_index.py#L525) | 525 | `""` | — |
| [SRC-E599346ABE-L000526](../generate_index.py#L526) | 526 | `""` | — |
| [SRC-E599346ABE-L000527](../generate_index.py#L527) | 527 | `"def scan_repository(root: Path) -> tuple[list[IndexedSymbol], int]:"` | — |
| [SRC-E599346ABE-L000528](../generate_index.py#L528) | 528 | `"    \"\"\"Parse every eligible Python file or fail without producing a partial index.\"\"\""` | — |
| [SRC-E599346ABE-L000529](../generate_index.py#L529) | 529 | `"    python_files = discover_python_files(root)"` | — |
| [SRC-E599346ABE-L000530](../generate_index.py#L530) | 530 | `"    all_symbols: list[IndexedSymbol] = []"` | — |
| [SRC-E599346ABE-L000531](../generate_index.py#L531) | 531 | `"    failures: list[str] = []"` | — |
| [SRC-E599346ABE-L000532](../generate_index.py#L532) | 532 | `""` | — |
| [SRC-E599346ABE-L000533](../generate_index.py#L533) | 533 | `"    for source_path in python_files:"` | — |
| [SRC-E599346ABE-L000534](../generate_index.py#L534) | 534 | `"        relative_file = source_path.relative_to(root).as_posix()"` | — |
| [SRC-E599346ABE-L000535](../generate_index.py#L535) | 535 | `"        try:"` | — |
| [SRC-E599346ABE-L000536](../generate_index.py#L536) | 536 | `"            with tokenize.open(str(source_path)) as source_stream:"` | — |
| [SRC-E599346ABE-L000537](../generate_index.py#L537) | 537 | `"                source = source_stream.read()"` | — |
| [SRC-E599346ABE-L000538](../generate_index.py#L538) | 538 | `"            syntax_tree = ast.parse(source, filename=relative_file)"` | — |
| [SRC-E599346ABE-L000539](../generate_index.py#L539) | 539 | `"        except SyntaxError as exc:"` | — |
| [SRC-E599346ABE-L000540](../generate_index.py#L540) | 540 | `"            location = f\"السطر {exc.lineno}: {exc.msg}\" if exc.lineno else exc.msg"` | — |
| [SRC-E599346ABE-L000541](../generate_index.py#L541) | 541 | `"            failures.append(f\"{relative_file}: {location}\")"` | — |
| [SRC-E599346ABE-L000542](../generate_index.py#L542) | 542 | `"            continue"` | — |
| [SRC-E599346ABE-L000543](../generate_index.py#L543) | 543 | `"        except (OSError, UnicodeError, LookupError, tokenize.TokenError) as exc:"` | — |
| [SRC-E599346ABE-L000544](../generate_index.py#L544) | 544 | `"            failures.append(f\"{relative_file}: {type(exc).__name__}: {exc}\")"` | — |
| [SRC-E599346ABE-L000545](../generate_index.py#L545) | 545 | `"            continue"` | — |
| [SRC-E599346ABE-L000546](../generate_index.py#L546) | 546 | `""` | — |
| [SRC-E599346ABE-L000547](../generate_index.py#L547) | 547 | `"        visitor = SymbolVisitor(relative_file)"` | — |
| [SRC-E599346ABE-L000548](../generate_index.py#L548) | 548 | `"        visitor.visit(syntax_tree)"` | — |
| [SRC-E599346ABE-L000549](../generate_index.py#L549) | 549 | `"        all_symbols.extend(visitor.symbols)"` | — |
| [SRC-E599346ABE-L000550](../generate_index.py#L550) | 550 | `""` | — |
| [SRC-E599346ABE-L000551](../generate_index.py#L551) | 551 | `"    if failures:"` | — |
| [SRC-E599346ABE-L000552](../generate_index.py#L552) | 552 | `"        detail = \"\\n\".join(f\"- {failure}\" for failure in failures)"` | — |
| [SRC-E599346ABE-L000553](../generate_index.py#L553) | 553 | `"        raise IndexGenerationError("` | — |
| [SRC-E599346ABE-L000554](../generate_index.py#L554) | 554 | `"            \"تعذر إنشاء فهرس Python كامل؛ لم يُكتب MASTER_INDEX.md. \""` | — |
| [SRC-E599346ABE-L000555](../generate_index.py#L555) | 555 | `"            \"أصلح الملفات التالية ثم أعد التشغيل:\\n\" + detail"` | — |
| [SRC-E599346ABE-L000556](../generate_index.py#L556) | 556 | `"        )"` | — |
| [SRC-E599346ABE-L000557](../generate_index.py#L557) | 557 | `""` | — |
| [SRC-E599346ABE-L000558](../generate_index.py#L558) | 558 | `"    all_symbols.sort("` | — |
| [SRC-E599346ABE-L000559](../generate_index.py#L559) | 559 | `"        key=lambda symbol: ("` | — |
| [SRC-E599346ABE-L000560](../generate_index.py#L560) | 560 | `"            symbol.file.casefold(),"` | — |
| [SRC-E599346ABE-L000561](../generate_index.py#L561) | 561 | `"            symbol.line,"` | — |
| [SRC-E599346ABE-L000562](../generate_index.py#L562) | 562 | `"            symbol.name.casefold(),"` | — |
| [SRC-E599346ABE-L000563](../generate_index.py#L563) | 563 | `"            symbol.kind,"` | — |
| [SRC-E599346ABE-L000564](../generate_index.py#L564) | 564 | `"        )"` | — |
| [SRC-E599346ABE-L000565](../generate_index.py#L565) | 565 | `"    )"` | — |
| [SRC-E599346ABE-L000566](../generate_index.py#L566) | 566 | `"    return all_symbols, len(python_files)"` | — |
| [SRC-E599346ABE-L000567](../generate_index.py#L567) | 567 | `""` | — |
| [SRC-E599346ABE-L000568](../generate_index.py#L568) | 568 | `""` | — |
| [SRC-E599346ABE-L000569](../generate_index.py#L569) | 569 | `"def _line_at(source: str, offset: int, base_line: int = 1) -> int:"` | — |
| [SRC-E599346ABE-L000570](../generate_index.py#L570) | 570 | `"    \"\"\"Return a 1-based line number for a match in the supplied source fragment.\"\"\""` | — |
| [SRC-E599346ABE-L000571](../generate_index.py#L571) | 571 | `"    return base_line + source.count(\"\\n\", 0, offset)"` | — |
| [SRC-E599346ABE-L000572](../generate_index.py#L572) | 572 | `""` | — |
| [SRC-E599346ABE-L000573](../generate_index.py#L573) | 573 | `""` | — |
| [SRC-E599346ABE-L000574](../generate_index.py#L574) | 574 | `"def _add_marker("` | — |
| [SRC-E599346ABE-L000575](../generate_index.py#L575) | 575 | `"    markers: list[IndexedMarker],"` | — |
| [SRC-E599346ABE-L000576](../generate_index.py#L576) | 576 | `"    seen: set[tuple[str, str, str]],"` | — |
| [SRC-E599346ABE-L000577](../generate_index.py#L577) | 577 | `"    relative_file: str,"` | — |
| [SRC-E599346ABE-L000578](../generate_index.py#L578) | 578 | `"    name: str,"` | — |
| [SRC-E599346ABE-L000579](../generate_index.py#L579) | 579 | `"    kind: str,"` | — |
| [SRC-E599346ABE-L000580](../generate_index.py#L580) | 580 | `"    line: int,"` | — |
| [SRC-E599346ABE-L000581](../generate_index.py#L581) | 581 | `") -> None:"` | — |
| [SRC-E599346ABE-L000582](../generate_index.py#L582) | 582 | `"    \"\"\"Add the first occurrence of a symbol category within one file.\"\"\""` | — |
| [SRC-E599346ABE-L000583](../generate_index.py#L583) | 583 | `"    clean_name = \" \".join(name.strip().split())"` | — |
| [SRC-E599346ABE-L000584](../generate_index.py#L584) | 584 | `"    if not clean_name:"` | — |
| [SRC-E599346ABE-L000585](../generate_index.py#L585) | 585 | `"        return"` | — |
| [SRC-E599346ABE-L000586](../generate_index.py#L586) | 586 | `"    key = (relative_file, clean_name, kind)"` | — |
| [SRC-E599346ABE-L000587](../generate_index.py#L587) | 587 | `"    if key in seen:"` | — |
| [SRC-E599346ABE-L000588](../generate_index.py#L588) | 588 | `"        return"` | — |
| [SRC-E599346ABE-L000589](../generate_index.py#L589) | 589 | `"    seen.add(key)"` | — |
| [SRC-E599346ABE-L000590](../generate_index.py#L590) | 590 | `"    markers.append("` | — |
| [SRC-E599346ABE-L000591](../generate_index.py#L591) | 591 | `"        IndexedMarker("` | — |
| [SRC-E599346ABE-L000592](../generate_index.py#L592) | 592 | `"            file=relative_file,"` | — |
| [SRC-E599346ABE-L000593](../generate_index.py#L593) | 593 | `"            name=clean_name,"` | — |
| [SRC-E599346ABE-L000594](../generate_index.py#L594) | 594 | `"            kind=kind,"` | — |
| [SRC-E599346ABE-L000595](../generate_index.py#L595) | 595 | `"            line=max(line, 1),"` | — |
| [SRC-E599346ABE-L000596](../generate_index.py#L596) | 596 | `"        )"` | — |
| [SRC-E599346ABE-L000597](../generate_index.py#L597) | 597 | `"    )"` | — |
| [SRC-E599346ABE-L000598](../generate_index.py#L598) | 598 | `""` | — |
| [SRC-E599346ABE-L000599](../generate_index.py#L599) | 599 | `""` | — |
| [SRC-E599346ABE-L000600](../generate_index.py#L600) | 600 | `"def _scan_javascript("` | — |
| [SRC-E599346ABE-L000601](../generate_index.py#L601) | 601 | `"    source: str,"` | — |
| [SRC-E599346ABE-L000602](../generate_index.py#L602) | 602 | `"    relative_file: str,"` | — |
| [SRC-E599346ABE-L000603](../generate_index.py#L603) | 603 | `"    markers: list[IndexedMarker],"` | — |
| [SRC-E599346ABE-L000604](../generate_index.py#L604) | 604 | `"    seen: set[tuple[str, str, str]],"` | — |
| [SRC-E599346ABE-L000605](../generate_index.py#L605) | 605 | `"    base_line: int = 1,"` | — |
| [SRC-E599346ABE-L000606](../generate_index.py#L606) | 606 | `") -> None:"` | — |
| [SRC-E599346ABE-L000607](../generate_index.py#L607) | 607 | `"    \"\"\"Extract navigational JS/TS declarations using bounded regular-expression heuristics.\"\"\""` | — |
| [SRC-E599346ABE-L000608](../generate_index.py#L608) | 608 | `"    for pattern, kind in ("` | — |
| [SRC-E599346ABE-L000609](../generate_index.py#L609) | 609 | `"        (JS_FUNCTION_RE, \"دالة JavaScript/TypeScript\"),"` | — |
| [SRC-E599346ABE-L000610](../generate_index.py#L610) | 610 | `"        (JS_CLASS_RE, \"كلاس JavaScript/TypeScript\"),"` | — |
| [SRC-E599346ABE-L000611](../generate_index.py#L611) | 611 | `"    ):"` | — |
| [SRC-E599346ABE-L000612](../generate_index.py#L612) | 612 | `"        for match in pattern.finditer(source):"` | — |
| [SRC-E599346ABE-L000613](../generate_index.py#L613) | 613 | `"            _add_marker("` | — |
| [SRC-E599346ABE-L000614](../generate_index.py#L614) | 614 | `"                markers,"` | — |
| [SRC-E599346ABE-L000615](../generate_index.py#L615) | 615 | `"                seen,"` | — |
| [SRC-E599346ABE-L000616](../generate_index.py#L616) | 616 | `"                relative_file,"` | — |
| [SRC-E599346ABE-L000617](../generate_index.py#L617) | 617 | `"                match.group(1),"` | — |
| [SRC-E599346ABE-L000618](../generate_index.py#L618) | 618 | `"                kind,"` | — |
| [SRC-E599346ABE-L000619](../generate_index.py#L619) | 619 | `"                _line_at(source, match.start(), base_line),"` | — |
| [SRC-E599346ABE-L000620](../generate_index.py#L620) | 620 | `"            )"` | — |
| [SRC-E599346ABE-L000621](../generate_index.py#L621) | 621 | `""` | — |
| [SRC-E599346ABE-L000622](../generate_index.py#L622) | 622 | `"    function_variable_locations: set[tuple[str, int]] = set()"` | — |
| [SRC-E599346ABE-L000623](../generate_index.py#L623) | 623 | `"    for pattern in (JS_ARROW_ASSIGNMENT_RE, JS_FUNCTION_ASSIGNMENT_RE):"` | — |
| [SRC-E599346ABE-L000624](../generate_index.py#L624) | 624 | `"        for match in pattern.finditer(source):"` | — |
| [SRC-E599346ABE-L000625](../generate_index.py#L625) | 625 | `"            line = _line_at(source, match.start(), base_line)"` | — |
| [SRC-E599346ABE-L000626](../generate_index.py#L626) | 626 | `"            name = match.group(1)"` | — |
| [SRC-E599346ABE-L000627](../generate_index.py#L627) | 627 | `"            function_variable_locations.add((name, line))"` | — |
| [SRC-E599346ABE-L000628](../generate_index.py#L628) | 628 | `"            _add_marker("` | — |
| [SRC-E599346ABE-L000629](../generate_index.py#L629) | 629 | `"                markers,"` | — |
| [SRC-E599346ABE-L000630](../generate_index.py#L630) | 630 | `"                seen,"` | — |
| [SRC-E599346ABE-L000631](../generate_index.py#L631) | 631 | `"                relative_file,"` | — |
| [SRC-E599346ABE-L000632](../generate_index.py#L632) | 632 | `"                name,"` | — |
| [SRC-E599346ABE-L000633](../generate_index.py#L633) | 633 | `"                \"دالة JavaScript/TypeScript\","` | — |
| [SRC-E599346ABE-L000634](../generate_index.py#L634) | 634 | `"                line,"` | — |
| [SRC-E599346ABE-L000635](../generate_index.py#L635) | 635 | `"            )"` | — |
| [SRC-E599346ABE-L000636](../generate_index.py#L636) | 636 | `""` | — |
| [SRC-E599346ABE-L000637](../generate_index.py#L637) | 637 | `"    for match in JS_VARIABLE_RE.finditer(source):"` | — |
| [SRC-E599346ABE-L000638](../generate_index.py#L638) | 638 | `"        line = _line_at(source, match.start(), base_line)"` | — |
| [SRC-E599346ABE-L000639](../generate_index.py#L639) | 639 | `"        name = match.group(1)"` | — |
| [SRC-E599346ABE-L000640](../generate_index.py#L640) | 640 | `"        if (name, line) in function_variable_locations:"` | — |
| [SRC-E599346ABE-L000641](../generate_index.py#L641) | 641 | `"            continue"` | — |
| [SRC-E599346ABE-L000642](../generate_index.py#L642) | 642 | `"        _add_marker("` | — |
| [SRC-E599346ABE-L000643](../generate_index.py#L643) | 643 | `"            markers,"` | — |
| [SRC-E599346ABE-L000644](../generate_index.py#L644) | 644 | `"            seen,"` | — |
| [SRC-E599346ABE-L000645](../generate_index.py#L645) | 645 | `"            relative_file,"` | — |
| [SRC-E599346ABE-L000646](../generate_index.py#L646) | 646 | `"            name,"` | — |
| [SRC-E599346ABE-L000647](../generate_index.py#L647) | 647 | `"            \"متغير JavaScript/TypeScript\","` | — |
| [SRC-E599346ABE-L000648](../generate_index.py#L648) | 648 | `"            line,"` | — |
| [SRC-E599346ABE-L000649](../generate_index.py#L649) | 649 | `"        )"` | — |
| [SRC-E599346ABE-L000650](../generate_index.py#L650) | 650 | `""` | — |
| [SRC-E599346ABE-L000651](../generate_index.py#L651) | 651 | `""` | — |
| [SRC-E599346ABE-L000652](../generate_index.py#L652) | 652 | `"def _scan_css("` | — |
| [SRC-E599346ABE-L000653](../generate_index.py#L653) | 653 | `"    source: str,"` | — |
| [SRC-E599346ABE-L000654](../generate_index.py#L654) | 654 | `"    relative_file: str,"` | — |
| [SRC-E599346ABE-L000655](../generate_index.py#L655) | 655 | `"    markers: list[IndexedMarker],"` | — |
| [SRC-E599346ABE-L000656](../generate_index.py#L656) | 656 | `"    seen: set[tuple[str, str, str]],"` | — |
| [SRC-E599346ABE-L000657](../generate_index.py#L657) | 657 | `"    base_line: int = 1,"` | — |
| [SRC-E599346ABE-L000658](../generate_index.py#L658) | 658 | `") -> None:"` | — |
| [SRC-E599346ABE-L000659](../generate_index.py#L659) | 659 | `"    \"\"\"Extract CSS class/id selectors and custom properties; this is not a full CSS parser.\"\"\""` | — |
| [SRC-E599346ABE-L000660](../generate_index.py#L660) | 660 | `"    cleaned = CSS_COMMENT_RE.sub("` | — |
| [SRC-E599346ABE-L000661](../generate_index.py#L661) | 661 | `"        lambda match: \"\".join(\"\\n\" if char == \"\\n\" else \" \" for char in match.group(0)),"` | — |
| [SRC-E599346ABE-L000662](../generate_index.py#L662) | 662 | `"        source,"` | — |
| [SRC-E599346ABE-L000663](../generate_index.py#L663) | 663 | `"    )"` | — |
| [SRC-E599346ABE-L000664](../generate_index.py#L664) | 664 | `"    patterns = ("` | — |
| [SRC-E599346ABE-L000665](../generate_index.py#L665) | 665 | `"        (CSS_CUSTOM_PROPERTY_RE, \"متغير CSS مخصص\"),"` | — |
| [SRC-E599346ABE-L000666](../generate_index.py#L666) | 666 | `"        (CSS_CLASS_RE, \"محدد class في CSS\"),"` | — |
| [SRC-E599346ABE-L000667](../generate_index.py#L667) | 667 | `"        (CSS_ID_RE, \"محدد id في CSS\"),"` | — |
| [SRC-E599346ABE-L000668](../generate_index.py#L668) | 668 | `"    )"` | — |
| [SRC-E599346ABE-L000669](../generate_index.py#L669) | 669 | `"    for pattern, kind in patterns:"` | — |
| [SRC-E599346ABE-L000670](../generate_index.py#L670) | 670 | `"        for match in pattern.finditer(cleaned):"` | — |
| [SRC-E599346ABE-L000671](../generate_index.py#L671) | 671 | `"            _add_marker("` | — |
| [SRC-E599346ABE-L000672](../generate_index.py#L672) | 672 | `"                markers,"` | — |
| [SRC-E599346ABE-L000673](../generate_index.py#L673) | 673 | `"                seen,"` | — |
| [SRC-E599346ABE-L000674](../generate_index.py#L674) | 674 | `"                relative_file,"` | — |
| [SRC-E599346ABE-L000675](../generate_index.py#L675) | 675 | `"                match.group(1),"` | — |
| [SRC-E599346ABE-L000676](../generate_index.py#L676) | 676 | `"                kind,"` | — |
| [SRC-E599346ABE-L000677](../generate_index.py#L677) | 677 | `"                _line_at(cleaned, match.start(), base_line),"` | — |
| [SRC-E599346ABE-L000678](../generate_index.py#L678) | 678 | `"            )"` | — |
| [SRC-E599346ABE-L000679](../generate_index.py#L679) | 679 | `""` | — |
| [SRC-E599346ABE-L000680](../generate_index.py#L680) | 680 | `""` | — |
| [SRC-E599346ABE-L000681](../generate_index.py#L681) | 681 | `"def _scan_html("` | — |
| [SRC-E599346ABE-L000682](../generate_index.py#L682) | 682 | `"    source: str,"` | — |
| [SRC-E599346ABE-L000683](../generate_index.py#L683) | 683 | `"    relative_file: str,"` | — |
| [SRC-E599346ABE-L000684](../generate_index.py#L684) | 684 | `"    markers: list[IndexedMarker],"` | — |
| [SRC-E599346ABE-L000685](../generate_index.py#L685) | 685 | `"    seen: set[tuple[str, str, str]],"` | — |
| [SRC-E599346ABE-L000686](../generate_index.py#L686) | 686 | `") -> None:"` | — |
| [SRC-E599346ABE-L000687](../generate_index.py#L687) | 687 | `"    \"\"\"Extract HTML navigation attributes plus embedded JS and CSS declarations.\"\"\""` | — |
| [SRC-E599346ABE-L000688](../generate_index.py#L688) | 688 | `"    for match in HTML_ATTRIBUTE_RE.finditer(source):"` | — |
| [SRC-E599346ABE-L000689](../generate_index.py#L689) | 689 | `"        attribute = match.group(1).lower()"` | — |
| [SRC-E599346ABE-L000690](../generate_index.py#L690) | 690 | `"        raw_value = match.group(3).strip()"` | — |
| [SRC-E599346ABE-L000691](../generate_index.py#L691) | 691 | `"        for value in raw_value.split() if attribute == \"data-testid\" else [raw_value]:"` | — |
| [SRC-E599346ABE-L000692](../generate_index.py#L692) | 692 | `"            _add_marker("` | — |
| [SRC-E599346ABE-L000693](../generate_index.py#L693) | 693 | `"                markers,"` | — |
| [SRC-E599346ABE-L000694](../generate_index.py#L694) | 694 | `"                seen,"` | — |
| [SRC-E599346ABE-L000695](../generate_index.py#L695) | 695 | `"                relative_file,"` | — |
| [SRC-E599346ABE-L000696](../generate_index.py#L696) | 696 | `"                value,"` | — |
| [SRC-E599346ABE-L000697](../generate_index.py#L697) | 697 | `"                f\"قيمة سمة HTML ({attribute})\","` | — |
| [SRC-E599346ABE-L000698](../generate_index.py#L698) | 698 | `"                _line_at(source, match.start()),"` | — |
| [SRC-E599346ABE-L000699](../generate_index.py#L699) | 699 | `"            )"` | — |
| [SRC-E599346ABE-L000700](../generate_index.py#L700) | 700 | `""` | — |
| [SRC-E599346ABE-L000701](../generate_index.py#L701) | 701 | `"    for match in HTML_SCRIPT_RE.finditer(source):"` | — |
| [SRC-E599346ABE-L000702](../generate_index.py#L702) | 702 | `"        script = match.group(1)"` | — |
| [SRC-E599346ABE-L000703](../generate_index.py#L703) | 703 | `"        base_line = _line_at(source, match.start(1))"` | — |
| [SRC-E599346ABE-L000704](../generate_index.py#L704) | 704 | `"        _scan_javascript(script, relative_file, markers, seen, base_line)"` | — |
| [SRC-E599346ABE-L000705](../generate_index.py#L705) | 705 | `"    for match in HTML_STYLE_RE.finditer(source):"` | — |
| [SRC-E599346ABE-L000706](../generate_index.py#L706) | 706 | `"        style = match.group(1)"` | — |
| [SRC-E599346ABE-L000707](../generate_index.py#L707) | 707 | `"        base_line = _line_at(source, match.start(1))"` | — |
| [SRC-E599346ABE-L000708](../generate_index.py#L708) | 708 | `"        _scan_css(style, relative_file, markers, seen, base_line)"` | — |
| [SRC-E599346ABE-L000709](../generate_index.py#L709) | 709 | `""` | — |
| [SRC-E599346ABE-L000710](../generate_index.py#L710) | 710 | `""` | — |
| [SRC-E599346ABE-L000711](../generate_index.py#L711) | 711 | `"def _scan_config_keys("` | — |
| [SRC-E599346ABE-L000712](../generate_index.py#L712) | 712 | `"    source: str,"` | — |
| [SRC-E599346ABE-L000713](../generate_index.py#L713) | 713 | `"    suffix: str,"` | — |
| [SRC-E599346ABE-L000714](../generate_index.py#L714) | 714 | `"    relative_file: str,"` | — |
| [SRC-E599346ABE-L000715](../generate_index.py#L715) | 715 | `"    markers: list[IndexedMarker],"` | — |
| [SRC-E599346ABE-L000716](../generate_index.py#L716) | 716 | `"    seen: set[tuple[str, str, str]],"` | — |
| [SRC-E599346ABE-L000717](../generate_index.py#L717) | 717 | `") -> None:"` | — |
| [SRC-E599346ABE-L000718](../generate_index.py#L718) | 718 | `"    \"\"\"Extract configuration keys/sections without evaluating or loading configuration.\"\"\""` | — |
| [SRC-E599346ABE-L000719](../generate_index.py#L719) | 719 | `"    if suffix in {\".yml\", \".yaml\"}:"` | — |
| [SRC-E599346ABE-L000720](../generate_index.py#L720) | 720 | `"        patterns = ((YAML_KEY_RE, \"مفتاح إعداد YAML\"),)"` | — |
| [SRC-E599346ABE-L000721](../generate_index.py#L721) | 721 | `"    elif suffix == \".toml\":"` | — |
| [SRC-E599346ABE-L000722](../generate_index.py#L722) | 722 | `"        patterns = ("` | — |
| [SRC-E599346ABE-L000723](../generate_index.py#L723) | 723 | `"            (TOML_SECTION_RE, \"قسم TOML\"),"` | — |
| [SRC-E599346ABE-L000724](../generate_index.py#L724) | 724 | `"            (TOML_KEY_RE, \"مفتاح إعداد TOML\"),"` | — |
| [SRC-E599346ABE-L000725](../generate_index.py#L725) | 725 | `"        )"` | — |
| [SRC-E599346ABE-L000726](../generate_index.py#L726) | 726 | `"    elif suffix == \".json\":"` | — |
| [SRC-E599346ABE-L000727](../generate_index.py#L727) | 727 | `"        patterns = ((JSON_KEY_RE, \"مفتاح JSON\"),)"` | — |
| [SRC-E599346ABE-L000728](../generate_index.py#L728) | 728 | `"    elif suffix in {\".ini\", \".cfg\"}:"` | — |
| [SRC-E599346ABE-L000729](../generate_index.py#L729) | 729 | `"        patterns = ("` | — |
| [SRC-E599346ABE-L000730](../generate_index.py#L730) | 730 | `"            (INI_SECTION_RE, \"قسم إعداد\"),"` | — |
| [SRC-E599346ABE-L000731](../generate_index.py#L731) | 731 | `"            (INI_KEY_RE, \"مفتاح إعداد\"),"` | — |
| [SRC-E599346ABE-L000732](../generate_index.py#L732) | 732 | `"        )"` | — |
| [SRC-E599346ABE-L000733](../generate_index.py#L733) | 733 | `"    else:"` | — |
| [SRC-E599346ABE-L000734](../generate_index.py#L734) | 734 | `"        patterns = ()"` | — |
| [SRC-E599346ABE-L000735](../generate_index.py#L735) | 735 | `"    for pattern, kind in patterns:"` | — |
| [SRC-E599346ABE-L000736](../generate_index.py#L736) | 736 | `"        for match in pattern.finditer(source):"` | — |
| [SRC-E599346ABE-L000737](../generate_index.py#L737) | 737 | `"            _add_marker("` | — |
| [SRC-E599346ABE-L000738](../generate_index.py#L738) | 738 | `"                markers,"` | — |
| [SRC-E599346ABE-L000739](../generate_index.py#L739) | 739 | `"                seen,"` | — |
| [SRC-E599346ABE-L000740](../generate_index.py#L740) | 740 | `"                relative_file,"` | — |
| [SRC-E599346ABE-L000741](../generate_index.py#L741) | 741 | `"                match.group(1),"` | — |
| [SRC-E599346ABE-L000742](../generate_index.py#L742) | 742 | `"                kind,"` | — |
| [SRC-E599346ABE-L000743](../generate_index.py#L743) | 743 | `"                _line_at(source, match.start()),"` | — |
| [SRC-E599346ABE-L000744](../generate_index.py#L744) | 744 | `"            )"` | — |
| [SRC-E599346ABE-L000745](../generate_index.py#L745) | 745 | `""` | — |
| [SRC-E599346ABE-L000746](../generate_index.py#L746) | 746 | `""` | — |
| [SRC-E599346ABE-L000747](../generate_index.py#L747) | 747 | `"def scan_static_symbols(root: Path, inventory: list[IndexedFile]) -> list[IndexedMarker]:"` | — |
| [SRC-E599346ABE-L000748](../generate_index.py#L748) | 748 | `"    \"\"\"Extract supplementary navigational symbols from frontend, docs, config and scripts.\"\"\""` | — |
| [SRC-E599346ABE-L000749](../generate_index.py#L749) | 749 | `"    markers: list[IndexedMarker] = []"` | — |
| [SRC-E599346ABE-L000750](../generate_index.py#L750) | 750 | `"    seen: set[tuple[str, str, str]] = set()"` | — |
| [SRC-E599346ABE-L000751](../generate_index.py#L751) | 751 | `"    for indexed_file in inventory:"` | — |
| [SRC-E599346ABE-L000752](../generate_index.py#L752) | 752 | `"        path = root / indexed_file.file"` | — |
| [SRC-E599346ABE-L000753](../generate_index.py#L753) | 753 | `"        suffix = path.suffix.lower()"` | — |
| [SRC-E599346ABE-L000754](../generate_index.py#L754) | 754 | `"        file_name = path.name.lower()"` | — |
| [SRC-E599346ABE-L000755](../generate_index.py#L755) | 755 | `"        is_example_env = file_name == \".env.example\""` | — |
| [SRC-E599346ABE-L000756](../generate_index.py#L756) | 756 | `"        if suffix not in TEXT_SCAN_EXTENSIONS and not is_example_env and file_name not in {"` | — |
| [SRC-E599346ABE-L000757](../generate_index.py#L757) | 757 | `"            \"dockerfile\","` | — |
| [SRC-E599346ABE-L000758](../generate_index.py#L758) | 758 | `"            \"makefile\","` | — |
| [SRC-E599346ABE-L000759](../generate_index.py#L759) | 759 | `"            \"procfile\","` | — |
| [SRC-E599346ABE-L000760](../generate_index.py#L760) | 760 | `"        }:"` | — |
| [SRC-E599346ABE-L000761](../generate_index.py#L761) | 761 | `"            continue"` | — |
| [SRC-E599346ABE-L000762](../generate_index.py#L762) | 762 | `""` | — |
| [SRC-E599346ABE-L000763](../generate_index.py#L763) | 763 | `"        source = _read_text_bounded(path)"` | — |
| [SRC-E599346ABE-L000764](../generate_index.py#L764) | 764 | `"        if source is None:"` | — |
| [SRC-E599346ABE-L000765](../generate_index.py#L765) | 765 | `"            continue"` | — |
| [SRC-E599346ABE-L000766](../generate_index.py#L766) | 766 | `""` | — |
| [SRC-E599346ABE-L000767](../generate_index.py#L767) | 767 | `"        if suffix in JAVASCRIPT_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000768](../generate_index.py#L768) | 768 | `"            _scan_javascript(source, indexed_file.file, markers, seen)"` | — |
| [SRC-E599346ABE-L000769](../generate_index.py#L769) | 769 | `"        elif suffix in CSS_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000770](../generate_index.py#L770) | 770 | `"            _scan_css(source, indexed_file.file, markers, seen)"` | — |
| [SRC-E599346ABE-L000771](../generate_index.py#L771) | 771 | `"        elif suffix in {\".html\", \".htm\"}:"` | — |
| [SRC-E599346ABE-L000772](../generate_index.py#L772) | 772 | `"            _scan_html(source, indexed_file.file, markers, seen)"` | — |
| [SRC-E599346ABE-L000773](../generate_index.py#L773) | 773 | `"        elif suffix == \".md\":"` | — |
| [SRC-E599346ABE-L000774](../generate_index.py#L774) | 774 | `"            for match in MARKDOWN_HEADING_RE.finditer(source):"` | — |
| [SRC-E599346ABE-L000775](../generate_index.py#L775) | 775 | `"                heading = match.group(2).strip()"` | — |
| [SRC-E599346ABE-L000776](../generate_index.py#L776) | 776 | `"                _add_marker("` | — |
| [SRC-E599346ABE-L000777](../generate_index.py#L777) | 777 | `"                    markers,"` | — |
| [SRC-E599346ABE-L000778](../generate_index.py#L778) | 778 | `"                    seen,"` | — |
| [SRC-E599346ABE-L000779](../generate_index.py#L779) | 779 | `"                    indexed_file.file,"` | — |
| [SRC-E599346ABE-L000780](../generate_index.py#L780) | 780 | `"                    heading,"` | — |
| [SRC-E599346ABE-L000781](../generate_index.py#L781) | 781 | `"                    f\"عنوان Markdown (H{len(match.group(1))})\","` | — |
| [SRC-E599346ABE-L000782](../generate_index.py#L782) | 782 | `"                    _line_at(source, match.start()),"` | — |
| [SRC-E599346ABE-L000783](../generate_index.py#L783) | 783 | `"                )"` | — |
| [SRC-E599346ABE-L000784](../generate_index.py#L784) | 784 | `"        elif suffix == \".sh\":"` | — |
| [SRC-E599346ABE-L000785](../generate_index.py#L785) | 785 | `"            for match in SHELL_FUNCTION_RE.finditer(source):"` | — |
| [SRC-E599346ABE-L000786](../generate_index.py#L786) | 786 | `"                _add_marker("` | — |
| [SRC-E599346ABE-L000787](../generate_index.py#L787) | 787 | `"                    markers,"` | — |
| [SRC-E599346ABE-L000788](../generate_index.py#L788) | 788 | `"                    seen,"` | — |
| [SRC-E599346ABE-L000789](../generate_index.py#L789) | 789 | `"                    indexed_file.file,"` | — |
| [SRC-E599346ABE-L000790](../generate_index.py#L790) | 790 | `"                    match.group(1),"` | — |
| [SRC-E599346ABE-L000791](../generate_index.py#L791) | 791 | `"                    \"دالة Shell\","` | — |
| [SRC-E599346ABE-L000792](../generate_index.py#L792) | 792 | `"                    _line_at(source, match.start()),"` | — |
| [SRC-E599346ABE-L000793](../generate_index.py#L793) | 793 | `"                )"` | — |
| [SRC-E599346ABE-L000794](../generate_index.py#L794) | 794 | `"        elif suffix in CONFIG_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L000795](../generate_index.py#L795) | 795 | `"            _scan_config_keys(source, suffix, indexed_file.file, markers, seen)"` | — |
| [SRC-E599346ABE-L000796](../generate_index.py#L796) | 796 | `""` | — |
| [SRC-E599346ABE-L000797](../generate_index.py#L797) | 797 | `"        if suffix in TEXT_SCAN_EXTENSIONS or is_example_env or file_name in {"` | — |
| [SRC-E599346ABE-L000798](../generate_index.py#L798) | 798 | `"            \"dockerfile\","` | — |
| [SRC-E599346ABE-L000799](../generate_index.py#L799) | 799 | `"            \"makefile\","` | — |
| [SRC-E599346ABE-L000800](../generate_index.py#L800) | 800 | `"            \"procfile\","` | — |
| [SRC-E599346ABE-L000801](../generate_index.py#L801) | 801 | `"        }:"` | — |
| [SRC-E599346ABE-L000802](../generate_index.py#L802) | 802 | `"            for match in UPPER_SNAKE_RE.finditer(source):"` | — |
| [SRC-E599346ABE-L000803](../generate_index.py#L803) | 803 | `"                _add_marker("` | — |
| [SRC-E599346ABE-L000804](../generate_index.py#L804) | 804 | `"                    markers,"` | — |
| [SRC-E599346ABE-L000805](../generate_index.py#L805) | 805 | `"                    seen,"` | — |
| [SRC-E599346ABE-L000806](../generate_index.py#L806) | 806 | `"                    indexed_file.file,"` | — |
| [SRC-E599346ABE-L000807](../generate_index.py#L807) | 807 | `"                    match.group(0),"` | — |
| [SRC-E599346ABE-L000808](../generate_index.py#L808) | 808 | `"                    \"اسم ثابت/إعداد بصيغة UPPER_SNAKE_CASE\","` | — |
| [SRC-E599346ABE-L000809](../generate_index.py#L809) | 809 | `"                    _line_at(source, match.start()),"` | — |
| [SRC-E599346ABE-L000810](../generate_index.py#L810) | 810 | `"                )"` | — |
| [SRC-E599346ABE-L000811](../generate_index.py#L811) | 811 | `""` | — |
| [SRC-E599346ABE-L000812](../generate_index.py#L812) | 812 | `"        if suffix in PYTHON_EXTENSIONS \| JAVASCRIPT_EXTENSIONS \| {\".html\", \".htm\"}:"` | — |
| [SRC-E599346ABE-L000813](../generate_index.py#L813) | 813 | `"            for match in API_PATH_RE.finditer(source):"` | — |
| [SRC-E599346ABE-L000814](../generate_index.py#L814) | 814 | `"                _add_marker("` | — |
| [SRC-E599346ABE-L000815](../generate_index.py#L815) | 815 | `"                    markers,"` | — |
| [SRC-E599346ABE-L000816](../generate_index.py#L816) | 816 | `"                    seen,"` | — |
| [SRC-E599346ABE-L000817](../generate_index.py#L817) | 817 | `"                    indexed_file.file,"` | — |
| [SRC-E599346ABE-L000818](../generate_index.py#L818) | 818 | `"                    match.group(1),"` | — |
| [SRC-E599346ABE-L000819](../generate_index.py#L819) | 819 | `"                    \"مسار API/واجهة محتمل\","` | — |
| [SRC-E599346ABE-L000820](../generate_index.py#L820) | 820 | `"                    _line_at(source, match.start()),"` | — |
| [SRC-E599346ABE-L000821](../generate_index.py#L821) | 821 | `"                )"` | — |
| [SRC-E599346ABE-L000822](../generate_index.py#L822) | 822 | `""` | — |
| [SRC-E599346ABE-L000823](../generate_index.py#L823) | 823 | `"    markers.sort("` | — |
| [SRC-E599346ABE-L000824](../generate_index.py#L824) | 824 | `"        key=lambda marker: ("` | — |
| [SRC-E599346ABE-L000825](../generate_index.py#L825) | 825 | `"            marker.file.casefold(),"` | — |
| [SRC-E599346ABE-L000826](../generate_index.py#L826) | 826 | `"            marker.line,"` | — |
| [SRC-E599346ABE-L000827](../generate_index.py#L827) | 827 | `"            marker.kind.casefold(),"` | — |
| [SRC-E599346ABE-L000828](../generate_index.py#L828) | 828 | `"            marker.name.casefold(),"` | — |
| [SRC-E599346ABE-L000829](../generate_index.py#L829) | 829 | `"        )"` | — |
| [SRC-E599346ABE-L000830](../generate_index.py#L830) | 830 | `"    )"` | — |
| [SRC-E599346ABE-L000831](../generate_index.py#L831) | 831 | `"    return markers"` | — |
| [SRC-E599346ABE-L000832](../generate_index.py#L832) | 832 | `""` | — |
| [SRC-E599346ABE-L000833](../generate_index.py#L833) | 833 | `""` | — |
| [SRC-E599346ABE-L000834](../generate_index.py#L834) | 834 | `"def _source_file_href("` | — |
| [SRC-E599346ABE-L000835](../generate_index.py#L835) | 835 | `"    relative_file: str,"` | — |
| [SRC-E599346ABE-L000836](../generate_index.py#L836) | 836 | `"    line: int = 1,"` | — |
| [SRC-E599346ABE-L000837](../generate_index.py#L837) | 837 | `"    index_directory: str = \"docs\","` | — |
| [SRC-E599346ABE-L000838](../generate_index.py#L838) | 838 | `") -> str:"` | — |
| [SRC-E599346ABE-L000839](../generate_index.py#L839) | 839 | `"    \"\"\"Return a relative source link from a generated index page to the original file.\"\"\""` | — |
| [SRC-E599346ABE-L000840](../generate_index.py#L840) | 840 | `"    normalized = relative_file.replace(\"\\\\\", \"/\")"` | — |
| [SRC-E599346ABE-L000841](../generate_index.py#L841) | 841 | `"    target = posixpath.relpath(normalized, index_directory)"` | — |
| [SRC-E599346ABE-L000842](../generate_index.py#L842) | 842 | `"    return f\"{quote(target, safe='/._-')}#L{max(line, 1)}\""` | — |
| [SRC-E599346ABE-L000843](../generate_index.py#L843) | 843 | `""` | — |
| [SRC-E599346ABE-L000844](../generate_index.py#L844) | 844 | `""` | — |
| [SRC-E599346ABE-L000845](../generate_index.py#L845) | 845 | `"def _source_line_id(relative_file: str, line: int) -> str:"` | — |
| [SRC-E599346ABE-L000846](../generate_index.py#L846) | 846 | `"    \"\"\"Return a consistent line code wherever a symbol, finding, or source line is shown.\"\"\""` | — |
| [SRC-E599346ABE-L000847](../generate_index.py#L847) | 847 | `"    file_hash = _stable_file_id(relative_file).removeprefix(\"FILE-\")"` | — |
| [SRC-E599346ABE-L000848](../generate_index.py#L848) | 848 | `"    return f\"SRC-{file_hash}-L{line:06d}\""` | — |
| [SRC-E599346ABE-L000849](../generate_index.py#L849) | 849 | `""` | — |
| [SRC-E599346ABE-L000850](../generate_index.py#L850) | 850 | `""` | — |
| [SRC-E599346ABE-L000851](../generate_index.py#L851) | 851 | `"def _markdown_cell(value: str) -> str:"` | — |
| [SRC-E599346ABE-L000852](../generate_index.py#L852) | 852 | `"    \"\"\"Normalize text and escape Markdown table delimiters.\"\"\""` | — |
| [SRC-E599346ABE-L000853](../generate_index.py#L853) | 853 | `"    return \" \".join(value.replace(\"\\r\", \" \").replace(\"\\n\", \" \").split()).replace("` | — |
| [SRC-E599346ABE-L000854](../generate_index.py#L854) | 854 | `"        \"\|\", r\"\\\|\""` | — |
| [SRC-E599346ABE-L000855](../generate_index.py#L855) | 855 | `"    )"` | — |
| [SRC-E599346ABE-L000856](../generate_index.py#L856) | 856 | `""` | — |
| [SRC-E599346ABE-L000857](../generate_index.py#L857) | 857 | `""` | — |
| [SRC-E599346ABE-L000858](../generate_index.py#L858) | 858 | `"def scan_source_lines(root: Path, inventory: list[IndexedFile]) -> list[IndexedLine]:"` | — |
| [SRC-E599346ABE-L000859](../generate_index.py#L859) | 859 | `"    \"\"\"Index every logical line of each eligible text file readable within the size bound.\"\"\""` | — |
| [SRC-E599346ABE-L000860](../generate_index.py#L860) | 860 | `"    indexed_lines: list[IndexedLine] = []"` | — |
| [SRC-E599346ABE-L000861](../generate_index.py#L861) | 861 | `"    for item in inventory:"` | — |
| [SRC-E599346ABE-L000862](../generate_index.py#L862) | 862 | `"        source = _read_text_bounded(root / item.file)"` | — |
| [SRC-E599346ABE-L000863](../generate_index.py#L863) | 863 | `"        if source is None:"` | — |
| [SRC-E599346ABE-L000864](../generate_index.py#L864) | 864 | `"            continue"` | — |
| [SRC-E599346ABE-L000865](../generate_index.py#L865) | 865 | `"        for line_number, content in enumerate(source.splitlines(), start=1):"` | — |
| [SRC-E599346ABE-L000866](../generate_index.py#L866) | 866 | `"            indexed_lines.append("` | — |
| [SRC-E599346ABE-L000867](../generate_index.py#L867) | 867 | `"                IndexedLine("` | — |
| [SRC-E599346ABE-L000868](../generate_index.py#L868) | 868 | `"                    file=item.file,"` | — |
| [SRC-E599346ABE-L000869](../generate_index.py#L869) | 869 | `"                    file_id=item.file_id,"` | — |
| [SRC-E599346ABE-L000870](../generate_index.py#L870) | 870 | `"                    line_id=_source_line_id(item.file, line_number),"` | — |
| [SRC-E599346ABE-L000871](../generate_index.py#L871) | 871 | `"                    category=item.category,"` | — |
| [SRC-E599346ABE-L000872](../generate_index.py#L872) | 872 | `"                    line=line_number,"` | — |
| [SRC-E599346ABE-L000873](../generate_index.py#L873) | 873 | `"                    content=content,"` | — |
| [SRC-E599346ABE-L000874](../generate_index.py#L874) | 874 | `"                )"` | — |
| [SRC-E599346ABE-L000875](../generate_index.py#L875) | 875 | `"            )"` | — |
| [SRC-E599346ABE-L000876](../generate_index.py#L876) | 876 | `"    indexed_lines.sort(key=lambda item: (item.file.casefold(), item.line))"` | — |
| [SRC-E599346ABE-L000877](../generate_index.py#L877) | 877 | `"    return indexed_lines"` | — |
| [SRC-E599346ABE-L000878](../generate_index.py#L878) | 878 | `""` | — |
| [SRC-E599346ABE-L000879](../generate_index.py#L879) | 879 | `""` | — |
| [SRC-E599346ABE-L000880](../generate_index.py#L880) | 880 | `"def scan_finding_annotations(source_lines: list[IndexedLine]) -> list[IndexedFinding]:"` | — |
| [SRC-E599346ABE-L000881](../generate_index.py#L881) | 881 | `"    \"\"\"Index explicit review/fix markers; they are hints for review, not proven defects.\"\"\""` | — |
| [SRC-E599346ABE-L000882](../generate_index.py#L882) | 882 | `"    findings: list[IndexedFinding] = []"` | — |
| [SRC-E599346ABE-L000883](../generate_index.py#L883) | 883 | `"    for source_line in source_lines:"` | — |
| [SRC-E599346ABE-L000884](../generate_index.py#L884) | 884 | `"        match = FINDING_MARKER_RE.search(source_line.content)"` | — |
| [SRC-E599346ABE-L000885](../generate_index.py#L885) | 885 | `"        if match is None:"` | — |
| [SRC-E599346ABE-L000886](../generate_index.py#L886) | 886 | `"            continue"` | — |
| [SRC-E599346ABE-L000887](../generate_index.py#L887) | 887 | `"        marker = match.group(1).upper()"` | — |
| [SRC-E599346ABE-L000888](../generate_index.py#L888) | 888 | `"        detail = (match.group(2) or \"\").strip()"` | — |
| [SRC-E599346ABE-L000889](../generate_index.py#L889) | 889 | `"        description = marker if not detail else f\"{marker}: {detail}\""` | — |
| [SRC-E599346ABE-L000890](../generate_index.py#L890) | 890 | `"        findings.append("` | — |
| [SRC-E599346ABE-L000891](../generate_index.py#L891) | 891 | `"            IndexedFinding("` | — |
| [SRC-E599346ABE-L000892](../generate_index.py#L892) | 892 | `"                finding_id=("` | — |
| [SRC-E599346ABE-L000893](../generate_index.py#L893) | 893 | `"                    f\"FND-{marker}-{source_line.file_id.removeprefix('FILE-')}\""` | — |
| [SRC-E599346ABE-L000894](../generate_index.py#L894) | 894 | `"                    f\"-L{source_line.line:06d}\""` | — |
| [SRC-E599346ABE-L000895](../generate_index.py#L895) | 895 | `"                ),"` | — |
| [SRC-E599346ABE-L000896](../generate_index.py#L896) | 896 | `"                file=source_line.file,"` | — |
| [SRC-E599346ABE-L000897](../generate_index.py#L897) | 897 | `"                line_id=source_line.line_id,"` | — |
| [SRC-E599346ABE-L000898](../generate_index.py#L898) | 898 | `"                marker=marker,"` | — |
| [SRC-E599346ABE-L000899](../generate_index.py#L899) | 899 | `"                description=description,"` | — |
| [SRC-E599346ABE-L000900](../generate_index.py#L900) | 900 | `"            )"` | — |
| [SRC-E599346ABE-L000901](../generate_index.py#L901) | 901 | `"        )"` | — |
| [SRC-E599346ABE-L000902](../generate_index.py#L902) | 902 | `"    findings.sort(key=lambda item: (item.marker, item.file.casefold(), item.line_id))"` | — |
| [SRC-E599346ABE-L000903](../generate_index.py#L903) | 903 | `"    return findings"` | — |
| [SRC-E599346ABE-L000904](../generate_index.py#L904) | 904 | `""` | — |
| [SRC-E599346ABE-L000905](../generate_index.py#L905) | 905 | `""` | — |
| [SRC-E599346ABE-L000906](../generate_index.py#L906) | 906 | `"def _markdown_code_span(value: str) -> str:"` | — |
| [SRC-E599346ABE-L000907](../generate_index.py#L907) | 907 | `"    \"\"\"Render a Markdown inline-code span safely, including backticks in source text.\"\"\""` | — |
| [SRC-E599346ABE-L000908](../generate_index.py#L908) | 908 | `"    tick = chr(96)"` | — |
| [SRC-E599346ABE-L000909](../generate_index.py#L909) | 909 | `"    longest = max("` | — |
| [SRC-E599346ABE-L000910](../generate_index.py#L910) | 910 | `"        (len(match.group(0)) for match in re.finditer(r\"\\u0060+\", value)),"` | — |
| [SRC-E599346ABE-L000911](../generate_index.py#L911) | 911 | `"        default=0,"` | — |
| [SRC-E599346ABE-L000912](../generate_index.py#L912) | 912 | `"    )"` | — |
| [SRC-E599346ABE-L000913](../generate_index.py#L913) | 913 | `"    fence = tick * (longest + 1)"` | — |
| [SRC-E599346ABE-L000914](../generate_index.py#L914) | 914 | `"    content = f\" {value} \" if value.startswith(tick) or value.endswith(tick) else value"` | — |
| [SRC-E599346ABE-L000915](../generate_index.py#L915) | 915 | `"    return f\"{fence}{content}{fence}\""` | — |
| [SRC-E599346ABE-L000916](../generate_index.py#L916) | 916 | `""` | — |
| [SRC-E599346ABE-L000917](../generate_index.py#L917) | 917 | `""` | — |
| [SRC-E599346ABE-L000918](../generate_index.py#L918) | 918 | `"def render_source_line_pages("` | — |
| [SRC-E599346ABE-L000919](../generate_index.py#L919) | 919 | `"    source_lines: list[IndexedLine],"` | — |
| [SRC-E599346ABE-L000920](../generate_index.py#L920) | 920 | `"    inventory: list[IndexedFile],"` | — |
| [SRC-E599346ABE-L000921](../generate_index.py#L921) | 921 | `"    findings: list[IndexedFinding],"` | — |
| [SRC-E599346ABE-L000922](../generate_index.py#L922) | 922 | `") -> tuple[dict[str, str], dict[str, list[str]]]:"` | — |
| [SRC-E599346ABE-L000923](../generate_index.py#L923) | 923 | `"    \"\"\"Split line-level records into deterministic small pages and map each file to its pages.\"\"\""` | — |
| [SRC-E599346ABE-L000924](../generate_index.py#L924) | 924 | `"    pages: dict[str, str] = {}"` | — |
| [SRC-E599346ABE-L000925](../generate_index.py#L925) | 925 | `"    pages_by_file: dict[str, list[str]] = {}"` | — |
| [SRC-E599346ABE-L000926](../generate_index.py#L926) | 926 | `"    inventory_by_path = {item.file: item for item in inventory}"` | — |
| [SRC-E599346ABE-L000927](../generate_index.py#L927) | 927 | `"    findings_by_line = {finding.line_id: finding for finding in findings}"` | — |
| [SRC-E599346ABE-L000928](../generate_index.py#L928) | 928 | `""` | — |
| [SRC-E599346ABE-L000929](../generate_index.py#L929) | 929 | `"    for page_number, start in enumerate("` | — |
| [SRC-E599346ABE-L000930](../generate_index.py#L930) | 930 | `"        range(0, len(source_lines), SOURCE_LINES_PAGE_SIZE),"` | — |
| [SRC-E599346ABE-L000931](../generate_index.py#L931) | 931 | `"        start=1,"` | — |
| [SRC-E599346ABE-L000932](../generate_index.py#L932) | 932 | `"    ):"` | — |
| [SRC-E599346ABE-L000933](../generate_index.py#L933) | 933 | `"        chunk = source_lines[start : start + SOURCE_LINES_PAGE_SIZE]"` | — |
| [SRC-E599346ABE-L000934](../generate_index.py#L934) | 934 | `"        page_path = f\"{SOURCE_LINES_PAGES_DIR}/SOURCE_LINES_{page_number:03d}.md\""` | — |
| [SRC-E599346ABE-L000935](../generate_index.py#L935) | 935 | `"        lines = ["` | — |
| [SRC-E599346ABE-L000936](../generate_index.py#L936) | 936 | `"            \"# Omarai Source Lines\","` | — |
| [SRC-E599346ABE-L000937](../generate_index.py#L937) | 937 | `"            \"\","` | — |
| [SRC-E599346ABE-L000938](../generate_index.py#L938) | 938 | `"            \"<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L000939](../generate_index.py#L939) | 939 | `"            \"\","` | — |
| [SRC-E599346ABE-L000940](../generate_index.py#L940) | 940 | `"            f\"- الصفحة: **{page_number:03d}**\","` | — |
| [SRC-E599346ABE-L000941](../generate_index.py#L941) | 941 | `"            f\"- سجلات الأسطر: **{len(chunk)}**\","` | — |
| [SRC-E599346ABE-L000942](../generate_index.py#L942) | 942 | `"            f\"- النطاق: {chunk[0].line_id} إلى {chunk[-1].line_id}\","` | — |
| [SRC-E599346ABE-L000943](../generate_index.py#L943) | 943 | `"            \"- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)\","` | — |
| [SRC-E599346ABE-L000944](../generate_index.py#L944) | 944 | `"            \"\","` | — |
| [SRC-E599346ABE-L000945](../generate_index.py#L945) | 945 | `"        ]"` | — |
| [SRC-E599346ABE-L000946](../generate_index.py#L946) | 946 | `"        current_file: str \| None = None"` | — |
| [SRC-E599346ABE-L000947](../generate_index.py#L947) | 947 | `"        for source_line in chunk:"` | — |
| [SRC-E599346ABE-L000948](../generate_index.py#L948) | 948 | `"            item = inventory_by_path[source_line.file]"` | — |
| [SRC-E599346ABE-L000949](../generate_index.py#L949) | 949 | `"            if source_line.file != current_file:"` | — |
| [SRC-E599346ABE-L000950](../generate_index.py#L950) | 950 | `"                current_file = source_line.file"` | — |
| [SRC-E599346ABE-L000951](../generate_index.py#L951) | 951 | `"                lines.extend("` | — |
| [SRC-E599346ABE-L000952](../generate_index.py#L952) | 952 | `"                    ["` | — |
| [SRC-E599346ABE-L000953](../generate_index.py#L953) | 953 | `"                        f\"## {item.category}\","` | — |
| [SRC-E599346ABE-L000954](../generate_index.py#L954) | 954 | `"                        \"\","` | — |
| [SRC-E599346ABE-L000955](../generate_index.py#L955) | 955 | `"                        f\"### {item.file_id} — [{_markdown_cell(item.file)}]({_source_file_href(item.file, index_directory=SOURCE_LINES_PAGES_DIR)})\","` | — |
| [SRC-E599346ABE-L000956](../generate_index.py#L956) | 956 | `"                        \"\","` | — |
| [SRC-E599346ABE-L000957](../generate_index.py#L957) | 957 | `"                        f\"- النوع: **{item.file_type}**\","` | — |
| [SRC-E599346ABE-L000958](../generate_index.py#L958) | 958 | `"                        f\"- نطاق الفهرسة: {_markdown_cell(item.indexing_scope)}\","` | — |
| [SRC-E599346ABE-L000959](../generate_index.py#L959) | 959 | `"                        \"\","` | — |
| [SRC-E599346ABE-L000960](../generate_index.py#L960) | 960 | `"                        \"\| كود السطر \| السطر \| النص الكامل للسطر \| كود الوسم \|\","` | — |
| [SRC-E599346ABE-L000961](../generate_index.py#L961) | 961 | `"                        \"\|---\|---:\|---\|---\|\","` | — |
| [SRC-E599346ABE-L000962](../generate_index.py#L962) | 962 | `"                    ]"` | — |
| [SRC-E599346ABE-L000963](../generate_index.py#L963) | 963 | `"                )"` | — |
| [SRC-E599346ABE-L000964](../generate_index.py#L964) | 964 | `"            finding = findings_by_line.get(source_line.line_id)"` | — |
| [SRC-E599346ABE-L000965](../generate_index.py#L965) | 965 | `"            finding_code = finding.finding_id if finding else \"—\""` | — |
| [SRC-E599346ABE-L000966](../generate_index.py#L966) | 966 | `"            exact_text = json.dumps(source_line.content, ensure_ascii=False)"` | — |
| [SRC-E599346ABE-L000967](../generate_index.py#L967) | 967 | `"            escaped_text = exact_text.replace(\"\|\", r\"\\\|\")"` | — |
| [SRC-E599346ABE-L000968](../generate_index.py#L968) | 968 | `"            href = _source_file_href("` | — |
| [SRC-E599346ABE-L000969](../generate_index.py#L969) | 969 | `"                source_line.file,"` | — |
| [SRC-E599346ABE-L000970](../generate_index.py#L970) | 970 | `"                source_line.line,"` | — |
| [SRC-E599346ABE-L000971](../generate_index.py#L971) | 971 | `"                index_directory=SOURCE_LINES_PAGES_DIR,"` | — |
| [SRC-E599346ABE-L000972](../generate_index.py#L972) | 972 | `"            )"` | — |
| [SRC-E599346ABE-L000973](../generate_index.py#L973) | 973 | `"            line_code = f\"[{source_line.line_id}]({href})\""` | — |
| [SRC-E599346ABE-L000974](../generate_index.py#L974) | 974 | `"            lines.append("` | — |
| [SRC-E599346ABE-L000975](../generate_index.py#L975) | 975 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L000976](../generate_index.py#L976) | 976 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L000977](../generate_index.py#L977) | 977 | `"                    ("` | — |
| [SRC-E599346ABE-L000978](../generate_index.py#L978) | 978 | `"                        line_code,"` | — |
| [SRC-E599346ABE-L000979](../generate_index.py#L979) | 979 | `"                        str(source_line.line),"` | — |
| [SRC-E599346ABE-L000980](../generate_index.py#L980) | 980 | `"                        _markdown_code_span(escaped_text),"` | — |
| [SRC-E599346ABE-L000981](../generate_index.py#L981) | 981 | `"                        finding_code,"` | — |
| [SRC-E599346ABE-L000982](../generate_index.py#L982) | 982 | `"                    )"` | — |
| [SRC-E599346ABE-L000983](../generate_index.py#L983) | 983 | `"                )"` | — |
| [SRC-E599346ABE-L000984](../generate_index.py#L984) | 984 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L000985](../generate_index.py#L985) | 985 | `"            )"` | — |
| [SRC-E599346ABE-L000986](../generate_index.py#L986) | 986 | `"            refs = pages_by_file.setdefault(source_line.file, [])"` | — |
| [SRC-E599346ABE-L000987](../generate_index.py#L987) | 987 | `"            if page_path not in refs:"` | — |
| [SRC-E599346ABE-L000988](../generate_index.py#L988) | 988 | `"                refs.append(page_path)"` | — |
| [SRC-E599346ABE-L000989](../generate_index.py#L989) | 989 | `"        pages[page_path] = \"\\n\".join(lines) + \"\\n\""` | — |
| [SRC-E599346ABE-L000990](../generate_index.py#L990) | 990 | `""` | — |
| [SRC-E599346ABE-L000991](../generate_index.py#L991) | 991 | `"    return pages, pages_by_file"` | — |
| [SRC-E599346ABE-L000992](../generate_index.py#L992) | 992 | `""` | — |
| [SRC-E599346ABE-L000993](../generate_index.py#L993) | 993 | `""` | — |
| [SRC-E599346ABE-L000994](../generate_index.py#L994) | 994 | `"def render_source_lines_markdown("` | — |
| [SRC-E599346ABE-L000995](../generate_index.py#L995) | 995 | `"    source_lines: list[IndexedLine],"` | — |
| [SRC-E599346ABE-L000996](../generate_index.py#L996) | 996 | `"    inventory: list[IndexedFile],"` | — |
| [SRC-E599346ABE-L000997](../generate_index.py#L997) | 997 | `"    findings: list[IndexedFinding],"` | — |
| [SRC-E599346ABE-L000998](../generate_index.py#L998) | 998 | `"    pages_by_file: dict[str, list[str]] \| None = None,"` | — |
| [SRC-E599346ABE-L000999](../generate_index.py#L999) | 999 | `"    source_pages: dict[str, str] \| None = None,"` | — |
| [SRC-E599346ABE-L001000](../generate_index.py#L1000) | 1000 | `") -> str:"` | — |
| [SRC-E599346ABE-L001001](../generate_index.py#L1001) | 1001 | `"    \"\"\"Render a compact table of contents for the sharded full source-line index.\"\"\""` | — |
| [SRC-E599346ABE-L001002](../generate_index.py#L1002) | 1002 | `"    assigned_pages = pages_by_file or {}"` | — |
| [SRC-E599346ABE-L001003](../generate_index.py#L1003) | 1003 | `"    rendered_pages = source_pages or {}"` | — |
| [SRC-E599346ABE-L001004](../generate_index.py#L1004) | 1004 | `"    files_with_lines = sum(item.line_count is not None for item in inventory)"` | — |
| [SRC-E599346ABE-L001005](../generate_index.py#L1005) | 1005 | `"    lines = ["` | — |
| [SRC-E599346ABE-L001006](../generate_index.py#L1006) | 1006 | `"        \"# SOURCE LINES INDEX — Omarai\","` | — |
| [SRC-E599346ABE-L001007](../generate_index.py#L1007) | 1007 | `"        \"\","` | — |
| [SRC-E599346ABE-L001008](../generate_index.py#L1008) | 1008 | `"        \"<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001009](../generate_index.py#L1009) | 1009 | `"        \"\","` | — |
| [SRC-E599346ABE-L001010](../generate_index.py#L1010) | 1010 | `"        \"> هذا دليل الوصول إلى فهرس الأسطر الكامل. يحتوي كل سطر في الملفات النصية المؤهلة على كود SRC- ورقم السطر ونص السطر كاملًا.\","` | — |
| [SRC-E599346ABE-L001011](../generate_index.py#L1011) | 1011 | `"        \"> قُسّم المحتوى إلى صفحات صغيرة حتى تظل كل صفحة قابلة للفتح والبحث بسرعة من الهاتف والمتصفح.\","` | — |
| [SRC-E599346ABE-L001012](../generate_index.py#L1012) | 1012 | `"        \"> ابدأ من [MASTER INDEX](MASTER_INDEX.md) للعثور حسب اسم الملف أو الدالة أو الكلاس أو وسم المراجعة.\","` | — |
| [SRC-E599346ABE-L001013](../generate_index.py#L1013) | 1013 | `"        \"\","` | — |
| [SRC-E599346ABE-L001014](../generate_index.py#L1014) | 1014 | `"        \"## ملخص التغطية\","` | — |
| [SRC-E599346ABE-L001015](../generate_index.py#L1015) | 1015 | `"        \"\","` | — |
| [SRC-E599346ABE-L001016](../generate_index.py#L1016) | 1016 | `"        f\"- الملفات في جرد المستودع: **{len(inventory)}**\","` | — |
| [SRC-E599346ABE-L001017](../generate_index.py#L1017) | 1017 | `"        f\"- الملفات النصية المفهرسة سطرًا بسطر: **{files_with_lines}**\","` | — |
| [SRC-E599346ABE-L001018](../generate_index.py#L1018) | 1018 | `"        f\"- الأسطر المفهرسة: **{len(source_lines)}**\","` | — |
| [SRC-E599346ABE-L001019](../generate_index.py#L1019) | 1019 | `"        f\"- وسوم المراجعة/الإصلاح المسجلة: **{len(findings)}**\","` | — |
| [SRC-E599346ABE-L001020](../generate_index.py#L1020) | 1020 | `"        f\"- صفحات الأسطر: **{len(rendered_pages)}**\","` | — |
| [SRC-E599346ABE-L001021](../generate_index.py#L1021) | 1021 | `"        \"\","` | — |
| [SRC-E599346ABE-L001022](../generate_index.py#L1022) | 1022 | `"        \"## صفحات الأسطر\","` | — |
| [SRC-E599346ABE-L001023](../generate_index.py#L1023) | 1023 | `"        \"\","` | — |
| [SRC-E599346ABE-L001024](../generate_index.py#L1024) | 1024 | `"        \"\| الصفحة \| عدد السجلات \| من كود \| إلى كود \|\","` | — |
| [SRC-E599346ABE-L001025](../generate_index.py#L1025) | 1025 | `"        \"\|---\|---:\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001026](../generate_index.py#L1026) | 1026 | `"    ]"` | — |
| [SRC-E599346ABE-L001027](../generate_index.py#L1027) | 1027 | `"    for page_path, page_content in rendered_pages.items():"` | — |
| [SRC-E599346ABE-L001028](../generate_index.py#L1028) | 1028 | `"        count = sum(1 for line in page_content.splitlines() if line.startswith(\"\| [SRC-\"))"` | — |
| [SRC-E599346ABE-L001029](../generate_index.py#L1029) | 1029 | `"        ids = re.findall(r\"\\bSRC-[A-F0-9]+-L\\d{6}\\b\", page_content)"` | — |
| [SRC-E599346ABE-L001030](../generate_index.py#L1030) | 1030 | `"        label = Path(page_path).stem"` | — |
| [SRC-E599346ABE-L001031](../generate_index.py#L1031) | 1031 | `"        lines.append("` | — |
| [SRC-E599346ABE-L001032](../generate_index.py#L1032) | 1032 | `"            f\"\| [{label}]({Path(page_path).relative_to('docs').as_posix()}) \| \""` | — |
| [SRC-E599346ABE-L001033](../generate_index.py#L1033) | 1033 | `"            f\"{count} \| {ids[0] if ids else '—'} \| {ids[-1] if ids else '—'} \|\""` | — |
| [SRC-E599346ABE-L001034](../generate_index.py#L1034) | 1034 | `"        )"` | — |
| [SRC-E599346ABE-L001035](../generate_index.py#L1035) | 1035 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001036](../generate_index.py#L1036) | 1036 | `"        ["` | — |
| [SRC-E599346ABE-L001037](../generate_index.py#L1037) | 1037 | `"            \"\","` | — |
| [SRC-E599346ABE-L001038](../generate_index.py#L1038) | 1038 | `"            \"## جرد الملفات والوصول حسب الاسم\","` | — |
| [SRC-E599346ABE-L001039](../generate_index.py#L1039) | 1039 | `"            \"\","` | — |
| [SRC-E599346ABE-L001040](../generate_index.py#L1040) | 1040 | `"            \"\| معرّف الملف \| التصنيف \| الملف \| الأسطر \| صفحات الفهرسة \|\","` | — |
| [SRC-E599346ABE-L001041](../generate_index.py#L1041) | 1041 | `"            \"\|---\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001042](../generate_index.py#L1042) | 1042 | `"        ]"` | — |
| [SRC-E599346ABE-L001043](../generate_index.py#L1043) | 1043 | `"    )"` | — |
| [SRC-E599346ABE-L001044](../generate_index.py#L1044) | 1044 | `"    for item in sorted(inventory, key=lambda entry: (entry.category, entry.file.casefold())):"` | — |
| [SRC-E599346ABE-L001045](../generate_index.py#L1045) | 1045 | `"        if item.line_count is None:"` | — |
| [SRC-E599346ABE-L001046](../generate_index.py#L1046) | 1046 | `"            line_count = \"بيانات وصفية فقط\""` | — |
| [SRC-E599346ABE-L001047](../generate_index.py#L1047) | 1047 | `"        else:"` | — |
| [SRC-E599346ABE-L001048](../generate_index.py#L1048) | 1048 | `"            line_count = str(item.line_count)"` | — |
| [SRC-E599346ABE-L001049](../generate_index.py#L1049) | 1049 | `"        page_links = assigned_pages.get(item.file, [])"` | — |
| [SRC-E599346ABE-L001050](../generate_index.py#L1050) | 1050 | `"        if page_links:"` | — |
| [SRC-E599346ABE-L001051](../generate_index.py#L1051) | 1051 | `"            link_text = \", \".join("` | — |
| [SRC-E599346ABE-L001052](../generate_index.py#L1052) | 1052 | `"                f\"[{Path(page_path).stem}]({Path(page_path).relative_to('docs').as_posix()})\""` | — |
| [SRC-E599346ABE-L001053](../generate_index.py#L1053) | 1053 | `"                for page_path in page_links"` | — |
| [SRC-E599346ABE-L001054](../generate_index.py#L1054) | 1054 | `"            )"` | — |
| [SRC-E599346ABE-L001055](../generate_index.py#L1055) | 1055 | `"        elif item.line_count == 0:"` | — |
| [SRC-E599346ABE-L001056](../generate_index.py#L1056) | 1056 | `"            link_text = \"ملف نصي فارغ\""` | — |
| [SRC-E599346ABE-L001057](../generate_index.py#L1057) | 1057 | `"        elif item.line_count is None:"` | — |
| [SRC-E599346ABE-L001058](../generate_index.py#L1058) | 1058 | `"            link_text = \"غير مفهرس سطرًا بسطر\""` | — |
| [SRC-E599346ABE-L001059](../generate_index.py#L1059) | 1059 | `"        else:"` | — |
| [SRC-E599346ABE-L001060](../generate_index.py#L1060) | 1060 | `"            link_text = \"لا توجد سجلات\""` | — |
| [SRC-E599346ABE-L001061](../generate_index.py#L1061) | 1061 | `"        target = _source_file_href(item.file, index_directory=\"docs\")"` | — |
| [SRC-E599346ABE-L001062](../generate_index.py#L1062) | 1062 | `"        lines.append("` | — |
| [SRC-E599346ABE-L001063](../generate_index.py#L1063) | 1063 | `"            f\"\| {item.file_id} \| {_markdown_cell(item.category)} \| \""` | — |
| [SRC-E599346ABE-L001064](../generate_index.py#L1064) | 1064 | `"            f\"[{_markdown_cell(item.file)}]({target}) \| {line_count} \| {link_text} \|\""` | — |
| [SRC-E599346ABE-L001065](../generate_index.py#L1065) | 1065 | `"        )"` | — |
| [SRC-E599346ABE-L001066](../generate_index.py#L1066) | 1066 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001067](../generate_index.py#L1067) | 1067 | `"        ["` | — |
| [SRC-E599346ABE-L001068](../generate_index.py#L1068) | 1068 | `"            \"\","` | — |
| [SRC-E599346ABE-L001069](../generate_index.py#L1069) | 1069 | `"            \"## سجل وسوم المراجعة والإصلاح\","` | — |
| [SRC-E599346ABE-L001070](../generate_index.py#L1070) | 1070 | `"            \"\","` | — |
| [SRC-E599346ABE-L001071](../generate_index.py#L1071) | 1071 | `"            \"كل كود FND- في MASTER INDEX يحدد وسمًا صريحًا ويشير إلى كود السطر في إحدى صفحات هذا الفهرس.\","` | — |
| [SRC-E599346ABE-L001072](../generate_index.py#L1072) | 1072 | `"            \"الوسوم المعروفة: TODO وFIXME وBUG وHACK وXXX وREVIEW وSECURITY وDEPRECATED.\","` | — |
| [SRC-E599346ABE-L001073](../generate_index.py#L1073) | 1073 | `"            \"\","` | — |
| [SRC-E599346ABE-L001074](../generate_index.py#L1074) | 1074 | `"            \"## الاستثناءات وحدود التغطية\","` | — |
| [SRC-E599346ABE-L001075](../generate_index.py#L1075) | 1075 | `"            \"\","` | — |
| [SRC-E599346ABE-L001076](../generate_index.py#L1076) | 1076 | `"            \"- ملفات الفهرسة المولّدة نفسها مستثناة لمنع الحلقة الذاتية.\","` | — |
| [SRC-E599346ABE-L001077](../generate_index.py#L1077) | 1077 | `"            \"- تُفهرس سطور كل ملف نصي قابل للقراءة وحجمه حتى 2 MiB؛ الملفات الثنائية أو الأكبر أو غير القابلة للقراءة تظهر في جرد الملفات فقط.\","` | — |
| [SRC-E599346ABE-L001078](../generate_index.py#L1078) | 1078 | `"            \"- الملفات الحساسة المعروفة وقواعد البيانات والبيئات المحلية ومجلدات البناء والاعتماديات مستثناة عمدًا.\","` | — |
| [SRC-E599346ABE-L001079](../generate_index.py#L1079) | 1079 | `"            \"- أكواد الأسطر مشتقة من مسار الملف ورقم السطر؛ يتغير رقم الكود عند تحرك السطر بسبب تغييرات سابقة في الملف.\","` | — |
| [SRC-E599346ABE-L001080](../generate_index.py#L1080) | 1080 | `"            \"- وسوم المراجعة ليست تشخيصًا آليًا لكل عيب منطقي؛ الفهرس يسهل العثور على الكود لكنه لا يستطيع إثبات خلوه من الأخطاء.\","` | — |
| [SRC-E599346ABE-L001081](../generate_index.py#L1081) | 1081 | `"            \"\","` | — |
| [SRC-E599346ABE-L001082](../generate_index.py#L1082) | 1082 | `"        ]"` | — |
| [SRC-E599346ABE-L001083](../generate_index.py#L1083) | 1083 | `"    )"` | — |
| [SRC-E599346ABE-L001084](../generate_index.py#L1084) | 1084 | `"    return \"\\n\".join(lines) + \"\\n\""` | — |
| [SRC-E599346ABE-L001085](../generate_index.py#L1085) | 1085 | `""` | — |
| [SRC-E599346ABE-L001086](../generate_index.py#L1086) | 1086 | `""` | — |
| [SRC-E599346ABE-L001087](../generate_index.py#L1087) | 1087 | `"def render_markdown("` | — |
| [SRC-E599346ABE-L001088](../generate_index.py#L1088) | 1088 | `"    symbols: list[IndexedSymbol],"` | — |
| [SRC-E599346ABE-L001089](../generate_index.py#L1089) | 1089 | `"    files_scanned: int,"` | — |
| [SRC-E599346ABE-L001090](../generate_index.py#L1090) | 1090 | `"    inventory: list[IndexedFile] \| None = None,"` | — |
| [SRC-E599346ABE-L001091](../generate_index.py#L1091) | 1091 | `"    static_symbols: list[IndexedMarker] \| None = None,"` | — |
| [SRC-E599346ABE-L001092](../generate_index.py#L1092) | 1092 | `"    source_lines: list[IndexedLine] \| None = None,"` | — |
| [SRC-E599346ABE-L001093](../generate_index.py#L1093) | 1093 | `"    findings: list[IndexedFinding] \| None = None,"` | — |
| [SRC-E599346ABE-L001094](../generate_index.py#L1094) | 1094 | `") -> str:"` | — |
| [SRC-E599346ABE-L001095](../generate_index.py#L1095) | 1095 | `"    \"\"\"Render the repository file, symbol, explicit-review-marker, and line-index overview.\"\"\""` | FND-REVIEW-E599346ABE-L001095 |
| [SRC-E599346ABE-L001096](../generate_index.py#L1096) | 1096 | `"    file_inventory = inventory or []"` | — |
| [SRC-E599346ABE-L001097](../generate_index.py#L1097) | 1097 | `"    marker_inventory = static_symbols or []"` | — |
| [SRC-E599346ABE-L001098](../generate_index.py#L1098) | 1098 | `"    line_inventory = source_lines or []"` | — |
| [SRC-E599346ABE-L001099](../generate_index.py#L1099) | 1099 | `"    finding_inventory = findings or []"` | — |
