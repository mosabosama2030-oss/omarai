# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **002**
- سجلات الأسطر: **800**
- النطاق: SRC-138992B1FC-L000255 إلى SRC-5587371288-L000379
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-138992B1FC — [agents/answer_validation.py](../../agents/answer_validation.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-138992B1FC-L000255](../../agents/answer_validation.py#L255) | 255 | `"                \"matched_terms\": overlap[:8],"` | — |
| [SRC-138992B1FC-L000256](../../agents/answer_validation.py#L256) | 256 | `"                \"overlap_ratio\": round(ratio, 3),"` | — |
| [SRC-138992B1FC-L000257](../../agents/answer_validation.py#L257) | 257 | `"            })"` | — |
| [SRC-138992B1FC-L000258](../../agents/answer_validation.py#L258) | 258 | `"        sentence_status = ("` | — |
| [SRC-138992B1FC-L000259](../../agents/answer_validation.py#L259) | 259 | `"            \"lexical_overlap_signal_found\""` | — |
| [SRC-138992B1FC-L000260](../../agents/answer_validation.py#L260) | 260 | `"            if any(item[\"status\"] == \"lexical_overlap_signal_found\" for item in cited_checks)"` | — |
| [SRC-138992B1FC-L000261](../../agents/answer_validation.py#L261) | 261 | `"            else \"weak_lexical_overlap\""` | — |
| [SRC-138992B1FC-L000262](../../agents/answer_validation.py#L262) | 262 | `"        )"` | — |
| [SRC-138992B1FC-L000263](../../agents/answer_validation.py#L263) | 263 | `"        citation_alignment.append({"` | — |
| [SRC-138992B1FC-L000264](../../agents/answer_validation.py#L264) | 264 | `"            \"sentence_number\": sentence_number,"` | — |
| [SRC-138992B1FC-L000265](../../agents/answer_validation.py#L265) | 265 | `"            \"status\": sentence_status,"` | — |
| [SRC-138992B1FC-L000266](../../agents/answer_validation.py#L266) | 266 | `"            \"claim_terms_checked\": claim_tokens[:16],"` | — |
| [SRC-138992B1FC-L000267](../../agents/answer_validation.py#L267) | 267 | `"            \"citations\": cited_checks,"` | — |
| [SRC-138992B1FC-L000268](../../agents/answer_validation.py#L268) | 268 | `"        })"` | — |
| [SRC-138992B1FC-L000269](../../agents/answer_validation.py#L269) | 269 | `""` | — |
| [SRC-138992B1FC-L000270](../../agents/answer_validation.py#L270) | 270 | `""` | — |
| [SRC-138992B1FC-L000271](../../agents/answer_validation.py#L271) | 271 | `"    # Check numeric literals against the exact source indices cited in each sentence."` | — |
| [SRC-138992B1FC-L000272](../../agents/answer_validation.py#L272) | 272 | `"    # Values found in some unrelated source do not count as support for this citation."` | — |
| [SRC-138992B1FC-L000273](../../agents/answer_validation.py#L273) | 273 | `"    source_numbers_by_index = {"` | — |
| [SRC-138992B1FC-L000274](../../agents/answer_validation.py#L274) | 274 | `"        index: _numeric_literals(text)"` | — |
| [SRC-138992B1FC-L000275](../../agents/answer_validation.py#L275) | 275 | `"        for index, text in source_text_by_index.items()"` | — |
| [SRC-138992B1FC-L000276](../../agents/answer_validation.py#L276) | 276 | `"    }"` | — |
| [SRC-138992B1FC-L000277](../../agents/answer_validation.py#L277) | 277 | `"    citation_numeric_support: list[dict[str, Any]] = []"` | — |
| [SRC-138992B1FC-L000278](../../agents/answer_validation.py#L278) | 278 | `"    for sentence_number, sentence in enumerate(sentence_parts[:40], 1):"` | — |
| [SRC-138992B1FC-L000279](../../agents/answer_validation.py#L279) | 279 | `"        cited_indices = list(dict.fromkeys("` | — |
| [SRC-138992B1FC-L000280](../../agents/answer_validation.py#L280) | 280 | `"            int(match.group(1)) for match in _CITATION.finditer(sentence)"` | — |
| [SRC-138992B1FC-L000281](../../agents/answer_validation.py#L281) | 281 | `"        ))"` | — |
| [SRC-138992B1FC-L000282](../../agents/answer_validation.py#L282) | 282 | `"        if not cited_indices:"` | — |
| [SRC-138992B1FC-L000283](../../agents/answer_validation.py#L283) | 283 | `"            continue"` | — |
| [SRC-138992B1FC-L000284](../../agents/answer_validation.py#L284) | 284 | `"        claim_numbers = sorted(_numeric_literals(sentence, question=question))"` | — |
| [SRC-138992B1FC-L000285](../../agents/answer_validation.py#L285) | 285 | `"        valid_indices = [index for index in cited_indices if 1 <= index <= len(citable_sources)]"` | — |
| [SRC-138992B1FC-L000286](../../agents/answer_validation.py#L286) | 286 | `"        supported_numbers = {"` | — |
| [SRC-138992B1FC-L000287](../../agents/answer_validation.py#L287) | 287 | `"            number"` | — |
| [SRC-138992B1FC-L000288](../../agents/answer_validation.py#L288) | 288 | `"            for number in claim_numbers"` | — |
| [SRC-138992B1FC-L000289](../../agents/answer_validation.py#L289) | 289 | `"            if any(number in source_numbers_by_index.get(index, set()) for index in valid_indices)"` | — |
| [SRC-138992B1FC-L000290](../../agents/answer_validation.py#L290) | 290 | `"        }"` | — |
| [SRC-138992B1FC-L000291](../../agents/answer_validation.py#L291) | 291 | `"        unsupported_for_citation = ["` | — |
| [SRC-138992B1FC-L000292](../../agents/answer_validation.py#L292) | 292 | `"            number for number in claim_numbers if number not in supported_numbers"` | — |
| [SRC-138992B1FC-L000293](../../agents/answer_validation.py#L293) | 293 | `"        ]"` | — |
| [SRC-138992B1FC-L000294](../../agents/answer_validation.py#L294) | 294 | `"        citation_numeric_support.append({"` | — |
| [SRC-138992B1FC-L000295](../../agents/answer_validation.py#L295) | 295 | `"            \"sentence_number\": sentence_number,"` | — |
| [SRC-138992B1FC-L000296](../../agents/answer_validation.py#L296) | 296 | `"            \"cited_source_indexes\": cited_indices[:8],"` | — |
| [SRC-138992B1FC-L000297](../../agents/answer_validation.py#L297) | 297 | `"            \"claim_numeric_literals\": claim_numbers[:30],"` | — |
| [SRC-138992B1FC-L000298](../../agents/answer_validation.py#L298) | 298 | `"            \"potentially_unsupported_numeric_literals\": unsupported_for_citation[:30],"` | — |
| [SRC-138992B1FC-L000299](../../agents/answer_validation.py#L299) | 299 | `"            \"status\": ("` | — |
| [SRC-138992B1FC-L000300](../../agents/answer_validation.py#L300) | 300 | `"                \"potentially_unsupported_numeric_literals_for_cited_sources\""` | — |
| [SRC-138992B1FC-L000301](../../agents/answer_validation.py#L301) | 301 | `"                if unsupported_for_citation"` | — |
| [SRC-138992B1FC-L000302](../../agents/answer_validation.py#L302) | 302 | `"                else \"numeric_literals_seen_in_cited_source_text\""` | — |
| [SRC-138992B1FC-L000303](../../agents/answer_validation.py#L303) | 303 | `"                if claim_numbers and valid_indices"` | — |
| [SRC-138992B1FC-L000304](../../agents/answer_validation.py#L304) | 304 | `"                else \"no_numeric_literals_to_check\""` | — |
| [SRC-138992B1FC-L000305](../../agents/answer_validation.py#L305) | 305 | `"                if not claim_numbers"` | — |
| [SRC-138992B1FC-L000306](../../agents/answer_validation.py#L306) | 306 | `"                else \"not_assessable_no_readable_cited_source\""` | — |
| [SRC-138992B1FC-L000307](../../agents/answer_validation.py#L307) | 307 | `"            ),"` | — |
| [SRC-138992B1FC-L000308](../../agents/answer_validation.py#L308) | 308 | `"        })"` | — |
| [SRC-138992B1FC-L000309](../../agents/answer_validation.py#L309) | 309 | `""` | — |
| [SRC-138992B1FC-L000310](../../agents/answer_validation.py#L310) | 310 | `"    value_evidence: dict[str, list[dict[str, Any]]] = {}"` | — |
| [SRC-138992B1FC-L000311](../../agents/answer_validation.py#L311) | 311 | `"    for source_index in source_text_by_index:"` | — |
| [SRC-138992B1FC-L000312](../../agents/answer_validation.py#L312) | 312 | `"        source = safe_sources[source_index - 1]"` | — |
| [SRC-138992B1FC-L000313](../../agents/answer_validation.py#L313) | 313 | `"        page_text = str(source.get(\"page_text\") or \"\")"` | — |
| [SRC-138992B1FC-L000314](../../agents/answer_validation.py#L314) | 314 | `"        snippet = str(source.get(\"snippet\") or \"\")"` | — |
| [SRC-138992B1FC-L000315](../../agents/answer_validation.py#L315) | 315 | `"        selected_evidence = page_text if bool(source.get(\"page_fetched\")) and page_text.strip() else snippet"` | — |
| [SRC-138992B1FC-L000316](../../agents/answer_validation.py#L316) | 316 | `"        if not selected_evidence.strip():"` | — |
| [SRC-138992B1FC-L000317](../../agents/answer_validation.py#L317) | 317 | `"            selected_evidence = str(source.get(\"title\") or \"\")"` | — |
| [SRC-138992B1FC-L000318](../../agents/answer_validation.py#L318) | 318 | `"        for dimension, number in _numeric_values_with_cues(selected_evidence):"` | — |
| [SRC-138992B1FC-L000319](../../agents/answer_validation.py#L319) | 319 | `"            value_evidence.setdefault(dimension, []).append({"` | — |
| [SRC-138992B1FC-L000320](../../agents/answer_validation.py#L320) | 320 | `"                \"source_index\": source_index,"` | — |
| [SRC-138992B1FC-L000321](../../agents/answer_validation.py#L321) | 321 | `"                \"value\": number,"` | — |
| [SRC-138992B1FC-L000322](../../agents/answer_validation.py#L322) | 322 | `"            })"` | — |
| [SRC-138992B1FC-L000323](../../agents/answer_validation.py#L323) | 323 | `"    potential_value_discrepancies: list[dict[str, Any]] = []"` | — |
| [SRC-138992B1FC-L000324](../../agents/answer_validation.py#L324) | 324 | `"    for dimension, entries in sorted(value_evidence.items()):"` | — |
| [SRC-138992B1FC-L000325](../../agents/answer_validation.py#L325) | 325 | `"        unique_values = list(dict.fromkeys(entry[\"value\"] for entry in entries))"` | — |
| [SRC-138992B1FC-L000326](../../agents/answer_validation.py#L326) | 326 | `"        source_indexes = sorted({entry[\"source_index\"] for entry in entries})"` | — |
| [SRC-138992B1FC-L000327](../../agents/answer_validation.py#L327) | 327 | `"        if len(unique_values) < 2 or len(source_indexes) < 2:"` | — |
| [SRC-138992B1FC-L000328](../../agents/answer_validation.py#L328) | 328 | `"            continue"` | — |
| [SRC-138992B1FC-L000329](../../agents/answer_validation.py#L329) | 329 | `"        by_value = []"` | — |
| [SRC-138992B1FC-L000330](../../agents/answer_validation.py#L330) | 330 | `"        for value in unique_values[:8]:"` | — |
| [SRC-138992B1FC-L000331](../../agents/answer_validation.py#L331) | 331 | `"            supporting_indexes = sorted({"` | — |
| [SRC-138992B1FC-L000332](../../agents/answer_validation.py#L332) | 332 | `"                entry[\"source_index\"] for entry in entries if entry[\"value\"] == value"` | — |
| [SRC-138992B1FC-L000333](../../agents/answer_validation.py#L333) | 333 | `"            })"` | — |
| [SRC-138992B1FC-L000334](../../agents/answer_validation.py#L334) | 334 | `"            by_value.append({\"value\": value, \"source_indexes\": supporting_indexes[:8]})"` | — |
| [SRC-138992B1FC-L000335](../../agents/answer_validation.py#L335) | 335 | `"        potential_value_discrepancies.append({"` | — |
| [SRC-138992B1FC-L000336](../../agents/answer_validation.py#L336) | 336 | `"            \"dimension\": dimension,"` | — |
| [SRC-138992B1FC-L000337](../../agents/answer_validation.py#L337) | 337 | `"            \"values\": by_value,"` | — |
| [SRC-138992B1FC-L000338](../../agents/answer_validation.py#L338) | 338 | `"            \"source_indexes\": source_indexes[:12],"` | — |
| [SRC-138992B1FC-L000339](../../agents/answer_validation.py#L339) | 339 | `"            \"status\": \"potential_variation_or_conflict_requires_entity_review\","` | — |
| [SRC-138992B1FC-L000340](../../agents/answer_validation.py#L340) | 340 | `"        })"` | — |
| [SRC-138992B1FC-L000341](../../agents/answer_validation.py#L341) | 341 | `""` | — |
| [SRC-138992B1FC-L000342](../../agents/answer_validation.py#L342) | 342 | `"    weak_citation_alignment_count = sum("` | — |
| [SRC-138992B1FC-L000343](../../agents/answer_validation.py#L343) | 343 | `"        item[\"status\"] == \"weak_lexical_overlap\""` | — |
| [SRC-138992B1FC-L000344](../../agents/answer_validation.py#L344) | 344 | `"        for item in citation_alignment"` | — |
| [SRC-138992B1FC-L000345](../../agents/answer_validation.py#L345) | 345 | `"    )"` | — |
| [SRC-138992B1FC-L000346](../../agents/answer_validation.py#L346) | 346 | `"    target_checks: list[dict[str, Any]] = []"` | — |
| [SRC-138992B1FC-L000347](../../agents/answer_validation.py#L347) | 347 | `"    source_evidence_gap_count = 0"` | — |
| [SRC-138992B1FC-L000348](../../agents/answer_validation.py#L348) | 348 | `"    for target in (coverage_targets or [])[:8]:"` | — |
| [SRC-138992B1FC-L000349](../../agents/answer_validation.py#L349) | 349 | `"        target_tokens = list(dict.fromkeys(_criterion_tokens(target)))"` | — |
| [SRC-138992B1FC-L000350](../../agents/answer_validation.py#L350) | 350 | `"        overlap = [token for token in target_tokens if token in answer_tokens]"` | — |
| [SRC-138992B1FC-L000351](../../agents/answer_validation.py#L351) | 351 | `"        ratio = len(overlap) / len(target_tokens) if target_tokens else 0.0"` | — |
| [SRC-138992B1FC-L000352](../../agents/answer_validation.py#L352) | 352 | `"        likely_covered = bool(overlap) and ("` | — |
| [SRC-138992B1FC-L000353](../../agents/answer_validation.py#L353) | 353 | `"            ratio >= 0.5 if len(target_tokens) > 1 else True"` | — |
| [SRC-138992B1FC-L000354](../../agents/answer_validation.py#L354) | 354 | `"        )"` | — |
| [SRC-138992B1FC-L000355](../../agents/answer_validation.py#L355) | 355 | `""` | — |
| [SRC-138992B1FC-L000356](../../agents/answer_validation.py#L356) | 356 | `"        # Track criterion-level source signals separately from answer wording."` | — |
| [SRC-138992B1FC-L000357](../../agents/answer_validation.py#L357) | 357 | `"        # A term appearing in a source is not proof that the source supports a claim;"` | — |
| [SRC-138992B1FC-L000358](../../agents/answer_validation.py#L358) | 358 | `"        # this is a bounded retrieval/evidence diagnostic only."` | — |
| [SRC-138992B1FC-L000359](../../agents/answer_validation.py#L359) | 359 | `"        source_checks: list[dict[str, Any]] = []"` | — |
| [SRC-138992B1FC-L000360](../../agents/answer_validation.py#L360) | 360 | `"        for source_index, source in enumerate(safe_sources[:40], 1):"` | — |
| [SRC-138992B1FC-L000361](../../agents/answer_validation.py#L361) | 361 | `"            page_text = str(source.get(\"page_text\") or \"\")"` | — |
| [SRC-138992B1FC-L000362](../../agents/answer_validation.py#L362) | 362 | `"            snippet = str(source.get(\"snippet\") or \"\")"` | — |
| [SRC-138992B1FC-L000363](../../agents/answer_validation.py#L363) | 363 | `"            title = str(source.get(\"title\") or \"\")"` | — |
| [SRC-138992B1FC-L000364](../../agents/answer_validation.py#L364) | 364 | `"            if bool(source.get(\"page_fetched\")) and page_text.strip():"` | — |
| [SRC-138992B1FC-L000365](../../agents/answer_validation.py#L365) | 365 | `"                selected_text, basis = page_text, \"extracted_page_text\""` | — |
| [SRC-138992B1FC-L000366](../../agents/answer_validation.py#L366) | 366 | `"            elif snippet.strip():"` | — |
| [SRC-138992B1FC-L000367](../../agents/answer_validation.py#L367) | 367 | `"                selected_text, basis = snippet, \"search_snippet\""` | — |
| [SRC-138992B1FC-L000368](../../agents/answer_validation.py#L368) | 368 | `"            elif title.strip():"` | — |
| [SRC-138992B1FC-L000369](../../agents/answer_validation.py#L369) | 369 | `"                selected_text, basis = title, \"title_only\""` | — |
| [SRC-138992B1FC-L000370](../../agents/answer_validation.py#L370) | 370 | `"            else:"` | — |
| [SRC-138992B1FC-L000371](../../agents/answer_validation.py#L371) | 371 | `"                continue"` | — |
| [SRC-138992B1FC-L000372](../../agents/answer_validation.py#L372) | 372 | `"            source_tokens = set(_tokens(selected_text[:16000], drop_stopwords=True))"` | — |
| [SRC-138992B1FC-L000373](../../agents/answer_validation.py#L373) | 373 | `"            source_overlap = ["` | — |
| [SRC-138992B1FC-L000374](../../agents/answer_validation.py#L374) | 374 | `"                token for token in target_tokens"` | — |
| [SRC-138992B1FC-L000375](../../agents/answer_validation.py#L375) | 375 | `"                if _criterion_token_variants(token) & source_tokens"` | — |
| [SRC-138992B1FC-L000376](../../agents/answer_validation.py#L376) | 376 | `"            ]"` | — |
| [SRC-138992B1FC-L000377](../../agents/answer_validation.py#L377) | 377 | `"            source_ratio = len(source_overlap) / len(target_tokens) if target_tokens else 0.0"` | — |
| [SRC-138992B1FC-L000378](../../agents/answer_validation.py#L378) | 378 | `"            source_signal = bool(source_overlap) and ("` | — |
| [SRC-138992B1FC-L000379](../../agents/answer_validation.py#L379) | 379 | `"                source_ratio >= 0.5 if len(target_tokens) > 1 else True"` | — |
| [SRC-138992B1FC-L000380](../../agents/answer_validation.py#L380) | 380 | `"            )"` | — |
| [SRC-138992B1FC-L000381](../../agents/answer_validation.py#L381) | 381 | `"            if source_signal:"` | — |
| [SRC-138992B1FC-L000382](../../agents/answer_validation.py#L382) | 382 | `"                source_checks.append({"` | — |
| [SRC-138992B1FC-L000383](../../agents/answer_validation.py#L383) | 383 | `"                    \"source_index\": source_index,"` | — |
| [SRC-138992B1FC-L000384](../../agents/answer_validation.py#L384) | 384 | `"                    \"status\": \"lexical_signal_found\","` | — |
| [SRC-138992B1FC-L000385](../../agents/answer_validation.py#L385) | 385 | `"                    \"evidence_basis\": basis,"` | — |
| [SRC-138992B1FC-L000386](../../agents/answer_validation.py#L386) | 386 | `"                    \"matched_terms\": source_overlap[:8],"` | — |
| [SRC-138992B1FC-L000387](../../agents/answer_validation.py#L387) | 387 | `"                    \"token_overlap_ratio\": round(source_ratio, 3),"` | — |
| [SRC-138992B1FC-L000388](../../agents/answer_validation.py#L388) | 388 | `"                })"` | — |
| [SRC-138992B1FC-L000389](../../agents/answer_validation.py#L389) | 389 | `"        if not source_checks:"` | — |
| [SRC-138992B1FC-L000390](../../agents/answer_validation.py#L390) | 390 | `"            source_evidence_gap_count += 1"` | — |
| [SRC-138992B1FC-L000391](../../agents/answer_validation.py#L391) | 391 | `"        target_checks.append({"` | — |
| [SRC-138992B1FC-L000392](../../agents/answer_validation.py#L392) | 392 | `"            \"target\": str(target)[:120],"` | — |
| [SRC-138992B1FC-L000393](../../agents/answer_validation.py#L393) | 393 | `"            \"status\": \"lexical_signal_found\" if likely_covered else \"possibly_missing\","` | — |
| [SRC-138992B1FC-L000394](../../agents/answer_validation.py#L394) | 394 | `"            \"matched_terms\": overlap[:12],"` | — |
| [SRC-138992B1FC-L000395](../../agents/answer_validation.py#L395) | 395 | `"            \"missing_terms\": [token for token in target_tokens if token not in answer_tokens][:12],"` | — |
| [SRC-138992B1FC-L000396](../../agents/answer_validation.py#L396) | 396 | `"            \"token_overlap_ratio\": round(ratio, 3),"` | — |
| [SRC-138992B1FC-L000397](../../agents/answer_validation.py#L397) | 397 | `"            \"source_evidence_status\": ("` | — |
| [SRC-138992B1FC-L000398](../../agents/answer_validation.py#L398) | 398 | `"                \"source_lexical_signal_found\" if source_checks else \"no_source_lexical_signal\""` | — |
| [SRC-138992B1FC-L000399](../../agents/answer_validation.py#L399) | 399 | `"            ),"` | — |
| [SRC-138992B1FC-L000400](../../agents/answer_validation.py#L400) | 400 | `"            \"source_evidence_checks\": source_checks[:12],"` | — |
| [SRC-138992B1FC-L000401](../../agents/answer_validation.py#L401) | 401 | `"        })"` | — |
| [SRC-138992B1FC-L000402](../../agents/answer_validation.py#L402) | 402 | `""` | — |
| [SRC-138992B1FC-L000403](../../agents/answer_validation.py#L403) | 403 | `"    citation_count = len(re.findall(r\"\\[(?:المصدر\|source)\\s+\\d+\\]\", answer_text, re.IGNORECASE))"` | — |
| [SRC-138992B1FC-L000404](../../agents/answer_validation.py#L404) | 404 | `"    if extracted_page_count:"` | — |
| [SRC-138992B1FC-L000405](../../agents/answer_validation.py#L405) | 405 | `"        source_scope = \"contains_extracted_page_text_and_or_snippets\""` | — |
| [SRC-138992B1FC-L000406](../../agents/answer_validation.py#L406) | 406 | `"    elif snippet_count:"` | — |
| [SRC-138992B1FC-L000407](../../agents/answer_validation.py#L407) | 407 | `"        source_scope = \"search_snippets_only\""` | — |
| [SRC-138992B1FC-L000408](../../agents/answer_validation.py#L408) | 408 | `"    else:"` | — |
| [SRC-138992B1FC-L000409](../../agents/answer_validation.py#L409) | 409 | `"        source_scope = \"no_readable_source_text\""` | — |
| [SRC-138992B1FC-L000410](../../agents/answer_validation.py#L410) | 410 | `""` | — |
| [SRC-138992B1FC-L000411](../../agents/answer_validation.py#L411) | 411 | `"    if not source_texts:"` | — |
| [SRC-138992B1FC-L000412](../../agents/answer_validation.py#L412) | 412 | `"        numeric_status = \"not_assessable_no_readable_source_text\""` | — |
| [SRC-138992B1FC-L000413](../../agents/answer_validation.py#L413) | 413 | `"    elif unsupported_numbers:"` | — |
| [SRC-138992B1FC-L000414](../../agents/answer_validation.py#L414) | 414 | `"        numeric_status = \"potentially_unsupported_numeric_literals\""` | — |
| [SRC-138992B1FC-L000415](../../agents/answer_validation.py#L415) | 415 | `"    elif answer_number_literals:"` | — |
| [SRC-138992B1FC-L000416](../../agents/answer_validation.py#L416) | 416 | `"        numeric_status = \"all_checked_numeric_literals_appear_in_source_text\""` | — |
| [SRC-138992B1FC-L000417](../../agents/answer_validation.py#L417) | 417 | `"    else:"` | — |
| [SRC-138992B1FC-L000418](../../agents/answer_validation.py#L418) | 418 | `"        numeric_status = \"no_specific_numeric_literals_checked\""` | — |
| [SRC-138992B1FC-L000419](../../agents/answer_validation.py#L419) | 419 | `""` | — |
| [SRC-138992B1FC-L000420](../../agents/answer_validation.py#L420) | 420 | `"    return {"` | — |
| [SRC-138992B1FC-L000421](../../agents/answer_validation.py#L421) | 421 | `"        \"method\": \"deterministic_lexical_screen_only\","` | — |
| [SRC-138992B1FC-L000422](../../agents/answer_validation.py#L422) | 422 | `"        \"semantic_verification\": False,"` | — |
| [SRC-138992B1FC-L000423](../../agents/answer_validation.py#L423) | 423 | `"        \"independent_fact_check\": False,"` | — |
| [SRC-138992B1FC-L000424](../../agents/answer_validation.py#L424) | 424 | `"        \"answer_nonempty\": bool(answer_text.strip()),"` | — |
| [SRC-138992B1FC-L000425](../../agents/answer_validation.py#L425) | 425 | `"        \"source_count\": len(safe_sources),"` | — |
| [SRC-138992B1FC-L000426](../../agents/answer_validation.py#L426) | 426 | `"        \"source_evidence_scope\": source_scope,"` | — |
| [SRC-138992B1FC-L000427](../../agents/answer_validation.py#L427) | 427 | `"        \"pages_with_extracted_text\": extracted_page_count,"` | — |
| [SRC-138992B1FC-L000428](../../agents/answer_validation.py#L428) | 428 | `"        \"sources_with_snippets_only\": snippet_count,"` | — |
| [SRC-138992B1FC-L000429](../../agents/answer_validation.py#L429) | 429 | `"        \"citation_marker_count\": citation_count,"` | — |
| [SRC-138992B1FC-L000430](../../agents/answer_validation.py#L430) | 430 | `"        \"citation_entailment\": \"not_checked\","` | — |
| [SRC-138992B1FC-L000431](../../agents/answer_validation.py#L431) | 431 | `"        \"citation_lexical_alignment_method\": \"content_word_overlap_heuristic_not_entailment\","` | — |
| [SRC-138992B1FC-L000432](../../agents/answer_validation.py#L432) | 432 | `"        \"citation_lexical_alignment\": citation_alignment[:30],"` | — |
| [SRC-138992B1FC-L000433](../../agents/answer_validation.py#L433) | 433 | `"        \"weak_citation_alignment_count\": weak_citation_alignment_count,"` | — |
| [SRC-138992B1FC-L000434](../../agents/answer_validation.py#L434) | 434 | `"        \"citation_numeric_support\": citation_numeric_support[:30],"` | — |
| [SRC-138992B1FC-L000435](../../agents/answer_validation.py#L435) | 435 | `"        \"potentially_unsupported_numeric_by_citation_count\": sum("` | — |
| [SRC-138992B1FC-L000436](../../agents/answer_validation.py#L436) | 436 | `"            len(item[\"potentially_unsupported_numeric_literals\"])"` | — |
| [SRC-138992B1FC-L000437](../../agents/answer_validation.py#L437) | 437 | `"            for item in citation_numeric_support"` | — |
| [SRC-138992B1FC-L000438](../../agents/answer_validation.py#L438) | 438 | `"        ),"` | — |
| [SRC-138992B1FC-L000439](../../agents/answer_validation.py#L439) | 439 | `"        \"potential_value_discrepancies\": potential_value_discrepancies[:8],"` | — |
| [SRC-138992B1FC-L000440](../../agents/answer_validation.py#L440) | 440 | `"        \"potential_value_discrepancy_count\": len(potential_value_discrepancies),"` | — |
| [SRC-138992B1FC-L000441](../../agents/answer_validation.py#L441) | 441 | `"        \"numeric_check_status\": numeric_status,"` | — |
| [SRC-138992B1FC-L000442](../../agents/answer_validation.py#L442) | 442 | `"        \"checked_numeric_literals\": sorted(answer_number_literals)[:40],"` | — |
| [SRC-138992B1FC-L000443](../../agents/answer_validation.py#L443) | 443 | `"        \"potentially_unsupported_numeric_literals\": unsupported_numbers[:40],"` | — |
| [SRC-138992B1FC-L000444](../../agents/answer_validation.py#L444) | 444 | `"        \"potentially_unsupported_numeric_count\": len(unsupported_numbers),"` | — |
| [SRC-138992B1FC-L000445](../../agents/answer_validation.py#L445) | 445 | `"        \"target_coverage\": target_checks,"` | — |
| [SRC-138992B1FC-L000446](../../agents/answer_validation.py#L446) | 446 | `"        \"potentially_missing_target_count\": sum("` | — |
| [SRC-138992B1FC-L000447](../../agents/answer_validation.py#L447) | 447 | `"            item[\"status\"] == \"possibly_missing\" for item in target_checks"` | — |
| [SRC-138992B1FC-L000448](../../agents/answer_validation.py#L448) | 448 | `"        ),"` | — |
| [SRC-138992B1FC-L000449](../../agents/answer_validation.py#L449) | 449 | `"        \"source_evidence_gap_count\": source_evidence_gap_count,"` | — |
| [SRC-138992B1FC-L000450](../../agents/answer_validation.py#L450) | 450 | `"        \"source_evidence_assessment\": \"criterion_level_lexical_signals_not_claim_support_or_entailment\","` | — |
| [SRC-138992B1FC-L000451](../../agents/answer_validation.py#L451) | 451 | `"        \"limitations\": ["` | — |
| [SRC-138992B1FC-L000452](../../agents/answer_validation.py#L452) | 452 | `"            \"Token overlap does not prove that an answer fulfills the intended task.\","` | — |
| [SRC-138992B1FC-L000453](../../agents/answer_validation.py#L453) | 453 | `"            \"A number appearing in any source does not prove that the source supports the claim.\","` | — |
| [SRC-138992B1FC-L000454](../../agents/answer_validation.py#L454) | 454 | `"            \"Citation token overlap can be coincidental and does not establish that the source entails the claim.\","` | — |
| [SRC-138992B1FC-L000455](../../agents/answer_validation.py#L455) | 455 | `"            \"Value-discrepancy flags may reflect different products, periods, or units; they are not automatic contradiction findings.\","` | — |
| [SRC-138992B1FC-L000456](../../agents/answer_validation.py#L456) | 456 | `"            \"Contradictory sources and citation-to-claim entailment require claim-level review.\","` | — |
| [SRC-138992B1FC-L000457](../../agents/answer_validation.py#L457) | 457 | `"            \"Search snippets may be partial; extracted page text is still not independent verification.\","` | — |
| [SRC-138992B1FC-L000458](../../agents/answer_validation.py#L458) | 458 | `"        ],"` | — |
| [SRC-138992B1FC-L000459](../../agents/answer_validation.py#L459) | 459 | `"    }"` | — |
## الوكيل والمنطق

### FILE-01273BA196 — [agents/aspect_planning.py](../../agents/aspect_planning.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-01273BA196-L000001](../../agents/aspect_planning.py#L1) | 1 | `"\"\"\"Compound-question aspect extraction and per-aspect search planning for Omarai.\"\"\""` | — |
| [SRC-01273BA196-L000002](../../agents/aspect_planning.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-01273BA196-L000003](../../agents/aspect_planning.py#L3) | 3 | `""` | — |
| [SRC-01273BA196-L000004](../../agents/aspect_planning.py#L4) | 4 | `"import re"` | — |
| [SRC-01273BA196-L000005](../../agents/aspect_planning.py#L5) | 5 | `"from typing import Any"` | — |
| [SRC-01273BA196-L000006](../../agents/aspect_planning.py#L6) | 6 | `""` | — |
| [SRC-01273BA196-L000007](../../agents/aspect_planning.py#L7) | 7 | `"MAX_PLAN_QUERIES = 8"` | — |
| [SRC-01273BA196-L000008](../../agents/aspect_planning.py#L8) | 8 | `"MAX_ASPECTS = 6"` | — |
| [SRC-01273BA196-L000009](../../agents/aspect_planning.py#L9) | 9 | `""` | — |
| [SRC-01273BA196-L000010](../../agents/aspect_planning.py#L10) | 10 | `"_ASPECT_MARKER_RE = re.compile("` | — |
| [SRC-01273BA196-L000011](../../agents/aspect_planning.py#L11) | 11 | `"    r\"(?:من\\s+حيث\|من\\s+ناحية\|من\\s+الناحية\|فيما\\s+يتعلق\\s+ب\|فيما\\s+يخص\|\""` | — |
| [SRC-01273BA196-L000012](../../agents/aspect_planning.py#L12) | 12 | `"    r\"من\\s+منظور\|in\\s+terms\\s+of\|with\\s+respect\\s+to\|\""` | — |
| [SRC-01273BA196-L000013](../../agents/aspect_planning.py#L13) | 13 | `"    r\"from\\s+the\\s+perspective\\s+of\|based\\s+on\\s+the\\s+following\\s+criteria)\""` | — |
| [SRC-01273BA196-L000014](../../agents/aspect_planning.py#L14) | 14 | `"    r\"\\s*(.+?)(?=[؟?!.؛;\\n]\|$)\","` | — |
| [SRC-01273BA196-L000015](../../agents/aspect_planning.py#L15) | 15 | `"    flags=re.IGNORECASE,"` | — |
| [SRC-01273BA196-L000016](../../agents/aspect_planning.py#L16) | 16 | `")"` | — |
| [SRC-01273BA196-L000017](../../agents/aspect_planning.py#L17) | 17 | `"_COMPARE_RE = re.compile("` | — |
| [SRC-01273BA196-L000018](../../agents/aspect_planning.py#L18) | 18 | `"    r\"(?:قارن(?:ي\|وا)?\|مقارنة\|compare\|versus\|\\bvs\\.?\\b\|الفرق\\s+بين)\","` | — |
| [SRC-01273BA196-L000019](../../agents/aspect_planning.py#L19) | 19 | `"    flags=re.IGNORECASE,"` | — |
| [SRC-01273BA196-L000020](../../agents/aspect_planning.py#L20) | 20 | `")"` | — |
| [SRC-01273BA196-L000021](../../agents/aspect_planning.py#L21) | 21 | `"_DIMENSION_TERMS = ("` | — |
| [SRC-01273BA196-L000022](../../agents/aspect_planning.py#L22) | 22 | `"    \"السعر\", \"سعر\", \"الأسعار\", \"الاسعار\", \"التكلفة\", \"التكلفه\","` | — |
| [SRC-01273BA196-L000023](../../agents/aspect_planning.py#L23) | 23 | `"    \"البطارية\", \"البطاريه\", \"الشحن\", \"الضمان\", \"الصيانة\", \"الصيانه\","` | — |
| [SRC-01273BA196-L000024](../../agents/aspect_planning.py#L24) | 24 | `"    \"الأمان\", \"الامان\", \"الكاميرا\", \"الأداء\", \"الاداء\", \"المميزات\", \"العيوب\","` | — |
| [SRC-01273BA196-L000025](../../agents/aspect_planning.py#L25) | 25 | `"    \"المراجعات\", \"الآراء\", \"الاراء\", \"price\", \"cost\", \"battery\", \"charging\","` | — |
| [SRC-01273BA196-L000026](../../agents/aspect_planning.py#L26) | 26 | `"    \"warranty\", \"maintenance\", \"safety\", \"camera\", \"performance\", \"pros\", \"cons\", \"reviews\","` | — |
| [SRC-01273BA196-L000027](../../agents/aspect_planning.py#L27) | 27 | `")"` | — |
| [SRC-01273BA196-L000028](../../agents/aspect_planning.py#L28) | 28 | `""` | — |
| [SRC-01273BA196-L000029](../../agents/aspect_planning.py#L29) | 29 | `""` | — |
| [SRC-01273BA196-L000030](../../agents/aspect_planning.py#L30) | 30 | `"def _normalize_space(value: str) -> str:"` | — |
| [SRC-01273BA196-L000031](../../agents/aspect_planning.py#L31) | 31 | `"    return re.sub(r\"\\s+\", \" \", (value or \"\")).strip()"` | — |
| [SRC-01273BA196-L000032](../../agents/aspect_planning.py#L32) | 32 | `""` | — |
| [SRC-01273BA196-L000033](../../agents/aspect_planning.py#L33) | 33 | `""` | — |
| [SRC-01273BA196-L000034](../../agents/aspect_planning.py#L34) | 34 | `"def _normalize_key(value: str) -> str:"` | — |
| [SRC-01273BA196-L000035](../../agents/aspect_planning.py#L35) | 35 | `"    text = _normalize_space(value).casefold()"` | — |
| [SRC-01273BA196-L000036](../../agents/aspect_planning.py#L36) | 36 | `"    return text.translate(str.maketrans({\"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ة\": \"ه\", \"ى\": \"ي\"}))"` | — |
| [SRC-01273BA196-L000037](../../agents/aspect_planning.py#L37) | 37 | `""` | — |
| [SRC-01273BA196-L000038](../../agents/aspect_planning.py#L38) | 38 | `""` | — |
| [SRC-01273BA196-L000039](../../agents/aspect_planning.py#L39) | 39 | `"def extract_aspects(question: str) -> list[str]:"` | — |
| [SRC-01273BA196-L000040](../../agents/aspect_planning.py#L40) | 40 | `"    if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-01273BA196-L000041](../../agents/aspect_planning.py#L41) | 41 | `"        return []"` | — |
| [SRC-01273BA196-L000042](../../agents/aspect_planning.py#L42) | 42 | `"    text = question.strip()[:4000]"` | — |
| [SRC-01273BA196-L000043](../../agents/aspect_planning.py#L43) | 43 | `"    match = _ASPECT_MARKER_RE.search(text)"` | — |
| [SRC-01273BA196-L000044](../../agents/aspect_planning.py#L44) | 44 | `"    pieces: list[str] = []"` | — |
| [SRC-01273BA196-L000045](../../agents/aspect_planning.py#L45) | 45 | `"    if match:"` | — |
| [SRC-01273BA196-L000046](../../agents/aspect_planning.py#L46) | 46 | `"        raw = match.group(1)"` | — |
| [SRC-01273BA196-L000047](../../agents/aspect_planning.py#L47) | 47 | `"        raw = re.split("` | — |
| [SRC-01273BA196-L000048](../../agents/aspect_planning.py#L48) | 48 | `"            r\"(?:،\|,\|؛\|;)\\s*(?:و?اذكر\|و?وضح\|بيّن\|اشرح\|and\\s+(?:explain\|note\|discuss))\\b\","` | — |
| [SRC-01273BA196-L000049](../../agents/aspect_planning.py#L49) | 49 | `"            raw, maxsplit=1, flags=re.IGNORECASE,"` | — |
| [SRC-01273BA196-L000050](../../agents/aspect_planning.py#L50) | 50 | `"        )[0]"` | — |
| [SRC-01273BA196-L000051](../../agents/aspect_planning.py#L51) | 51 | `"        pieces = re.split("` | — |
| [SRC-01273BA196-L000052](../../agents/aspect_planning.py#L52) | 52 | `"            r\"\\s*(?:،\|,\|؛\|;\|/)\\s+\|\\s+\\band\\b\\s+\|\\s+\\bas well as\\b\\s+\|\\s+و(?=ال\|[ء-ي])\","` | — |
| [SRC-01273BA196-L000053](../../agents/aspect_planning.py#L53) | 53 | `"            raw, flags=re.IGNORECASE,"` | — |
| [SRC-01273BA196-L000054](../../agents/aspect_planning.py#L54) | 54 | `"        )"` | — |
| [SRC-01273BA196-L000055](../../agents/aspect_planning.py#L55) | 55 | `"    else:"` | — |
| [SRC-01273BA196-L000056](../../agents/aspect_planning.py#L56) | 56 | `"        question_parts = [p.strip(\" \\t\\r\\n-•\") for p in re.split(r\"[؟?]+\", text) if len(p.strip(\" \\t\\r\\n-•\")) >= 4]"` | — |
| [SRC-01273BA196-L000057](../../agents/aspect_planning.py#L57) | 57 | `"        if len(question_parts) > 1:"` | — |
| [SRC-01273BA196-L000058](../../agents/aspect_planning.py#L58) | 58 | `"            pieces = question_parts"` | — |
| [SRC-01273BA196-L000059](../../agents/aspect_planning.py#L59) | 59 | `"        elif _COMPARE_RE.search(text):"` | — |
| [SRC-01273BA196-L000060](../../agents/aspect_planning.py#L60) | 60 | `"            found = []"` | — |
| [SRC-01273BA196-L000061](../../agents/aspect_planning.py#L61) | 61 | `"            for term in _DIMENSION_TERMS:"` | — |
| [SRC-01273BA196-L000062](../../agents/aspect_planning.py#L62) | 62 | `"                if term in text and term not in found:"` | — |
| [SRC-01273BA196-L000063](../../agents/aspect_planning.py#L63) | 63 | `"                    found.append(term)"` | — |
| [SRC-01273BA196-L000064](../../agents/aspect_planning.py#L64) | 64 | `"                if len(found) >= MAX_ASPECTS:"` | — |
| [SRC-01273BA196-L000065](../../agents/aspect_planning.py#L65) | 65 | `"                    break"` | — |
| [SRC-01273BA196-L000066](../../agents/aspect_planning.py#L66) | 66 | `"            pieces = found"` | — |
| [SRC-01273BA196-L000067](../../agents/aspect_planning.py#L67) | 67 | `"    targets: list[str] = []"` | — |
| [SRC-01273BA196-L000068](../../agents/aspect_planning.py#L68) | 68 | `"    seen: set[str] = set()"` | — |
| [SRC-01273BA196-L000069](../../agents/aspect_planning.py#L69) | 69 | `"    for piece in pieces:"` | — |
| [SRC-01273BA196-L000070](../../agents/aspect_planning.py#L70) | 70 | `"        target = re.sub(r\"^[\\s:،,؛;/.!?\\-–—]+\|[\\s:،,؛;/.!?\\-–—]+$\", \"\", piece).strip()"` | — |
| [SRC-01273BA196-L000071](../../agents/aspect_planning.py#L71) | 71 | `"        target = re.sub(r\"^(?:و\\s*)\", \"\", target).strip()"` | — |
| [SRC-01273BA196-L000072](../../agents/aspect_planning.py#L72) | 72 | `"        if len(target) < 2:"` | — |
| [SRC-01273BA196-L000073](../../agents/aspect_planning.py#L73) | 73 | `"            continue"` | — |
| [SRC-01273BA196-L000074](../../agents/aspect_planning.py#L74) | 74 | `"        if len(target) > 120:"` | — |
| [SRC-01273BA196-L000075](../../agents/aspect_planning.py#L75) | 75 | `"            target = target[:120].rsplit(\" \", 1)[0].strip()"` | — |
| [SRC-01273BA196-L000076](../../agents/aspect_planning.py#L76) | 76 | `"        key = _normalize_key(target)"` | — |
| [SRC-01273BA196-L000077](../../agents/aspect_planning.py#L77) | 77 | `"        if key and key not in seen:"` | — |
| [SRC-01273BA196-L000078](../../agents/aspect_planning.py#L78) | 78 | `"            seen.add(key)"` | — |
| [SRC-01273BA196-L000079](../../agents/aspect_planning.py#L79) | 79 | `"            targets.append(target)"` | — |
| [SRC-01273BA196-L000080](../../agents/aspect_planning.py#L80) | 80 | `"        if len(targets) >= MAX_ASPECTS:"` | — |
| [SRC-01273BA196-L000081](../../agents/aspect_planning.py#L81) | 81 | `"            break"` | — |
| [SRC-01273BA196-L000082](../../agents/aspect_planning.py#L82) | 82 | `"    return targets"` | — |
| [SRC-01273BA196-L000083](../../agents/aspect_planning.py#L83) | 83 | `""` | — |
| [SRC-01273BA196-L000084](../../agents/aspect_planning.py#L84) | 84 | `""` | — |
| [SRC-01273BA196-L000085](../../agents/aspect_planning.py#L85) | 85 | `"def build_aspect_queries(topic_query: str, aspects: list[str], *, limit: int = MAX_PLAN_QUERIES) -> list[str]:"` | — |
| [SRC-01273BA196-L000086](../../agents/aspect_planning.py#L86) | 86 | `"    queries: list[str] = []"` | — |
| [SRC-01273BA196-L000087](../../agents/aspect_planning.py#L87) | 87 | `"    seen: set[str] = set()"` | — |
| [SRC-01273BA196-L000088](../../agents/aspect_planning.py#L88) | 88 | `"    topic = _normalize_space(topic_query)"` | — |
| [SRC-01273BA196-L000089](../../agents/aspect_planning.py#L89) | 89 | `"    if topic:"` | — |
| [SRC-01273BA196-L000090](../../agents/aspect_planning.py#L90) | 90 | `"        queries.append(topic)"` | — |
| [SRC-01273BA196-L000091](../../agents/aspect_planning.py#L91) | 91 | `"        seen.add(_normalize_key(topic))"` | — |
| [SRC-01273BA196-L000092](../../agents/aspect_planning.py#L92) | 92 | `"    for aspect in aspects:"` | — |
| [SRC-01273BA196-L000093](../../agents/aspect_planning.py#L93) | 93 | `"        aspect_clean = _normalize_space(str(aspect))"` | — |
| [SRC-01273BA196-L000094](../../agents/aspect_planning.py#L94) | 94 | `"        if not aspect_clean:"` | — |
| [SRC-01273BA196-L000095](../../agents/aspect_planning.py#L95) | 95 | `"            continue"` | — |
| [SRC-01273BA196-L000096](../../agents/aspect_planning.py#L96) | 96 | `"        candidate = f\"{topic} {aspect_clean}\".strip() if topic else aspect_clean"` | — |
| [SRC-01273BA196-L000097](../../agents/aspect_planning.py#L97) | 97 | `"        candidate = _normalize_space(candidate)[:240]"` | — |
| [SRC-01273BA196-L000098](../../agents/aspect_planning.py#L98) | 98 | `"        key = _normalize_key(candidate)"` | — |
| [SRC-01273BA196-L000099](../../agents/aspect_planning.py#L99) | 99 | `"        if key and key not in seen:"` | — |
| [SRC-01273BA196-L000100](../../agents/aspect_planning.py#L100) | 100 | `"            seen.add(key)"` | — |
| [SRC-01273BA196-L000101](../../agents/aspect_planning.py#L101) | 101 | `"            queries.append(candidate)"` | — |
| [SRC-01273BA196-L000102](../../agents/aspect_planning.py#L102) | 102 | `"        if len(queries) >= max(1, min(int(limit), MAX_PLAN_QUERIES)):"` | — |
| [SRC-01273BA196-L000103](../../agents/aspect_planning.py#L103) | 103 | `"            break"` | — |
| [SRC-01273BA196-L000104](../../agents/aspect_planning.py#L104) | 104 | `"    return queries"` | — |
| [SRC-01273BA196-L000105](../../agents/aspect_planning.py#L105) | 105 | `""` | — |
| [SRC-01273BA196-L000106](../../agents/aspect_planning.py#L106) | 106 | `""` | — |
| [SRC-01273BA196-L000107](../../agents/aspect_planning.py#L107) | 107 | `"def augment_plan_with_aspects(plan: dict[str, Any], question: str, topic_query: str, *, compact_fn: Any = None) -> dict[str, Any]:"` | — |
| [SRC-01273BA196-L000108](../../agents/aspect_planning.py#L108) | 108 | `"    out = dict(plan or {})"` | — |
| [SRC-01273BA196-L000109](../../agents/aspect_planning.py#L109) | 109 | `"    aspects = extract_aspects(question)"` | — |
| [SRC-01273BA196-L000110](../../agents/aspect_planning.py#L110) | 110 | `"    out[\"aspects\"] = aspects"` | — |
| [SRC-01273BA196-L000111](../../agents/aspect_planning.py#L111) | 111 | `"    base_queries = [str(q).strip() for q in (out.get(\"queries\") or []) if isinstance(q, str) and q.strip()]"` | — |
| [SRC-01273BA196-L000112](../../agents/aspect_planning.py#L112) | 112 | `"    topic = topic_query or (base_queries[0] if base_queries else \"\")"` | — |
| [SRC-01273BA196-L000113](../../agents/aspect_planning.py#L113) | 113 | `"    if compact_fn is not None:"` | — |
| [SRC-01273BA196-L000114](../../agents/aspect_planning.py#L114) | 114 | `"        try:"` | — |
| [SRC-01273BA196-L000115](../../agents/aspect_planning.py#L115) | 115 | `"            topic = compact_fn(topic) or topic"` | — |
| [SRC-01273BA196-L000116](../../agents/aspect_planning.py#L116) | 116 | `"        except (TypeError, ValueError):"` | — |
| [SRC-01273BA196-L000117](../../agents/aspect_planning.py#L117) | 117 | `"            pass"` | — |
| [SRC-01273BA196-L000118](../../agents/aspect_planning.py#L118) | 118 | `"    aspect_queries = build_aspect_queries(topic, aspects)"` | — |
| [SRC-01273BA196-L000119](../../agents/aspect_planning.py#L119) | 119 | `"    merged_src = aspect_queries + base_queries"` | — |
| [SRC-01273BA196-L000120](../../agents/aspect_planning.py#L120) | 120 | `"    compacted: list[str] = []"` | — |
| [SRC-01273BA196-L000121](../../agents/aspect_planning.py#L121) | 121 | `"    seen: set[str] = set()"` | — |
| [SRC-01273BA196-L000122](../../agents/aspect_planning.py#L122) | 122 | `"    for q in merged_src:"` | — |
| [SRC-01273BA196-L000123](../../agents/aspect_planning.py#L123) | 123 | `"        cq = q"` | — |
| [SRC-01273BA196-L000124](../../agents/aspect_planning.py#L124) | 124 | `"        if compact_fn is not None:"` | — |
| [SRC-01273BA196-L000125](../../agents/aspect_planning.py#L125) | 125 | `"            try:"` | — |
| [SRC-01273BA196-L000126](../../agents/aspect_planning.py#L126) | 126 | `"                cq = compact_fn(q) or q"` | — |
| [SRC-01273BA196-L000127](../../agents/aspect_planning.py#L127) | 127 | `"            except (TypeError, ValueError):"` | — |
| [SRC-01273BA196-L000128](../../agents/aspect_planning.py#L128) | 128 | `"                cq = q"` | — |
| [SRC-01273BA196-L000129](../../agents/aspect_planning.py#L129) | 129 | `"        if not cq:"` | — |
| [SRC-01273BA196-L000130](../../agents/aspect_planning.py#L130) | 130 | `"            continue"` | — |
| [SRC-01273BA196-L000131](../../agents/aspect_planning.py#L131) | 131 | `"        key = _normalize_key(cq)"` | — |
| [SRC-01273BA196-L000132](../../agents/aspect_planning.py#L132) | 132 | `"        if key not in seen:"` | — |
| [SRC-01273BA196-L000133](../../agents/aspect_planning.py#L133) | 133 | `"            seen.add(key)"` | — |
| [SRC-01273BA196-L000134](../../agents/aspect_planning.py#L134) | 134 | `"            compacted.append(cq)"` | — |
| [SRC-01273BA196-L000135](../../agents/aspect_planning.py#L135) | 135 | `"        if len(compacted) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-01273BA196-L000136](../../agents/aspect_planning.py#L136) | 136 | `"            break"` | — |
| [SRC-01273BA196-L000137](../../agents/aspect_planning.py#L137) | 137 | `"    out[\"queries\"] = compacted"` | — |
| [SRC-01273BA196-L000138](../../agents/aspect_planning.py#L138) | 138 | `"    out[\"aspect_queries\"] = list(compacted)"` | — |
| [SRC-01273BA196-L000139](../../agents/aspect_planning.py#L139) | 139 | `"    return out"` | — |
| [SRC-01273BA196-L000140](../../agents/aspect_planning.py#L140) | 140 | `""` | — |
| [SRC-01273BA196-L000141](../../agents/aspect_planning.py#L141) | 141 | `""` | — |
| [SRC-01273BA196-L000142](../../agents/aspect_planning.py#L142) | 142 | `"def _source_text(source: dict[str, Any]) -> str:"` | — |
| [SRC-01273BA196-L000143](../../agents/aspect_planning.py#L143) | 143 | `"    return \" \".join(str(source.get(k) or \"\") for k in (\"title\", \"snippet\", \"page_text\"))"` | — |
| [SRC-01273BA196-L000144](../../agents/aspect_planning.py#L144) | 144 | `""` | — |
| [SRC-01273BA196-L000145](../../agents/aspect_planning.py#L145) | 145 | `""` | — |
| [SRC-01273BA196-L000146](../../agents/aspect_planning.py#L146) | 146 | `"def build_evidence_ledger(aspects: list[str], sources: list[dict[str, Any]], *, min_term_len: int = 2) -> dict[str, Any]:"` | — |
| [SRC-01273BA196-L000147](../../agents/aspect_planning.py#L147) | 147 | `"    ledger: dict[str, Any] = {\"aspects\": [], \"covered\": [], \"missing\": [], \"by_aspect\": {}}"` | — |
| [SRC-01273BA196-L000148](../../agents/aspect_planning.py#L148) | 148 | `"    if not aspects:"` | — |
| [SRC-01273BA196-L000149](../../agents/aspect_planning.py#L149) | 149 | `"        ledger[\"note\"] = \"no_explicit_aspects\""` | — |
| [SRC-01273BA196-L000150](../../agents/aspect_planning.py#L150) | 150 | `"        return ledger"` | — |
| [SRC-01273BA196-L000151](../../agents/aspect_planning.py#L151) | 151 | `"    for aspect in aspects:"` | — |
| [SRC-01273BA196-L000152](../../agents/aspect_planning.py#L152) | 152 | `"        tokens = [t for t in re.findall(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", _normalize_key(aspect)) if len(t) >= min_term_len]"` | — |
| [SRC-01273BA196-L000153](../../agents/aspect_planning.py#L153) | 153 | `"        matches: list[dict[str, Any]] = []"` | — |
| [SRC-01273BA196-L000154](../../agents/aspect_planning.py#L154) | 154 | `"        for source in sources or []:"` | — |
| [SRC-01273BA196-L000155](../../agents/aspect_planning.py#L155) | 155 | `"            if not isinstance(source, dict):"` | — |
| [SRC-01273BA196-L000156](../../agents/aspect_planning.py#L156) | 156 | `"                continue"` | — |
| [SRC-01273BA196-L000157](../../agents/aspect_planning.py#L157) | 157 | `"            hay = _normalize_key(_source_text(source))"` | — |
| [SRC-01273BA196-L000158](../../agents/aspect_planning.py#L158) | 158 | `"            if not hay:"` | — |
| [SRC-01273BA196-L000159](../../agents/aspect_planning.py#L159) | 159 | `"                continue"` | — |
| [SRC-01273BA196-L000160](../../agents/aspect_planning.py#L160) | 160 | `"            hit = sum(1 for t in tokens if t in hay)"` | — |
| [SRC-01273BA196-L000161](../../agents/aspect_planning.py#L161) | 161 | `"            if tokens and hit >= max(1, (len(tokens) + 1) // 2):"` | — |
| [SRC-01273BA196-L000162](../../agents/aspect_planning.py#L162) | 162 | `"                evidence_type = \"page_text\" if source.get(\"page_text\") else \"snippet\" if source.get(\"snippet\") else \"title\""` | — |
| [SRC-01273BA196-L000163](../../agents/aspect_planning.py#L163) | 163 | `"                matches.append({"` | — |
| [SRC-01273BA196-L000164](../../agents/aspect_planning.py#L164) | 164 | `"                    \"url\": source.get(\"url\", \"\"),"` | — |
| [SRC-01273BA196-L000165](../../agents/aspect_planning.py#L165) | 165 | `"                    \"title\": source.get(\"title\", \"\"),"` | — |
| [SRC-01273BA196-L000166](../../agents/aspect_planning.py#L166) | 166 | `"                    \"provider\": source.get(\"provider\") or (source.get(\"providers\") or [\"unknown\"])[0],"` | — |
| [SRC-01273BA196-L000167](../../agents/aspect_planning.py#L167) | 167 | `"                    \"evidence_type\": evidence_type,"` | — |
| [SRC-01273BA196-L000168](../../agents/aspect_planning.py#L168) | 168 | `"                    \"lexical_hits\": hit,"` | — |
| [SRC-01273BA196-L000169](../../agents/aspect_planning.py#L169) | 169 | `"                    \"search_query\": source.get(\"search_query\") or ((source.get(\"queries\") or [\"\"])[0] if source.get(\"queries\") else \"\"),"` | — |
| [SRC-01273BA196-L000170](../../agents/aspect_planning.py#L170) | 170 | `"                })"` | — |
| [SRC-01273BA196-L000171](../../agents/aspect_planning.py#L171) | 171 | `"        ledger[\"by_aspect\"][aspect] = {\"aspect\": aspect, \"candidate_count\": len(matches), \"candidates\": matches[:5], \"has_lexical_candidate\": bool(matches)}"` | — |
| [SRC-01273BA196-L000172](../../agents/aspect_planning.py#L172) | 172 | `"        ledger[\"aspects\"].append(aspect)"` | — |
| [SRC-01273BA196-L000173](../../agents/aspect_planning.py#L173) | 173 | `"        (ledger[\"covered\"] if matches else ledger[\"missing\"]).append(aspect)"` | — |
| [SRC-01273BA196-L000174](../../agents/aspect_planning.py#L174) | 174 | `"    ledger[\"coverage_ratio\"] = round(len(ledger[\"covered\"]) / max(1, len(aspects)), 3)"` | — |
| [SRC-01273BA196-L000175](../../agents/aspect_planning.py#L175) | 175 | `"    return ledger"` | — |
| [SRC-01273BA196-L000176](../../agents/aspect_planning.py#L176) | 176 | `""` | — |
| [SRC-01273BA196-L000177](../../agents/aspect_planning.py#L177) | 177 | `""` | — |
| [SRC-01273BA196-L000178](../../agents/aspect_planning.py#L178) | 178 | `"def repair_queries_for_missing_aspects(topic_query: str, missing_aspects: list[str], *, limit: int = 3, compact_fn: Any = None) -> list[str]:"` | — |
| [SRC-01273BA196-L000179](../../agents/aspect_planning.py#L179) | 179 | `"    topic = _normalize_space(topic_query)"` | — |
| [SRC-01273BA196-L000180](../../agents/aspect_planning.py#L180) | 180 | `"    out: list[str] = []"` | — |
| [SRC-01273BA196-L000181](../../agents/aspect_planning.py#L181) | 181 | `"    seen: set[str] = set()"` | — |
| [SRC-01273BA196-L000182](../../agents/aspect_planning.py#L182) | 182 | `"    for aspect in missing_aspects:"` | — |
| [SRC-01273BA196-L000183](../../agents/aspect_planning.py#L183) | 183 | `"        aspect_clean = _normalize_space(str(aspect))"` | — |
| [SRC-01273BA196-L000184](../../agents/aspect_planning.py#L184) | 184 | `"        if not aspect_clean:"` | — |
| [SRC-01273BA196-L000185](../../agents/aspect_planning.py#L185) | 185 | `"            continue"` | — |
| [SRC-01273BA196-L000186](../../agents/aspect_planning.py#L186) | 186 | `"        raw = f\"{topic} {aspect_clean}\".strip() if topic else aspect_clean"` | — |
| [SRC-01273BA196-L000187](../../agents/aspect_planning.py#L187) | 187 | `"        if compact_fn is not None:"` | — |
| [SRC-01273BA196-L000188](../../agents/aspect_planning.py#L188) | 188 | `"            try:"` | — |
| [SRC-01273BA196-L000189](../../agents/aspect_planning.py#L189) | 189 | `"                raw = compact_fn(raw) or raw"` | — |
| [SRC-01273BA196-L000190](../../agents/aspect_planning.py#L190) | 190 | `"            except (TypeError, ValueError):"` | — |
| [SRC-01273BA196-L000191](../../agents/aspect_planning.py#L191) | 191 | `"                pass"` | — |
| [SRC-01273BA196-L000192](../../agents/aspect_planning.py#L192) | 192 | `"        raw = _normalize_space(raw)[:240]"` | — |
| [SRC-01273BA196-L000193](../../agents/aspect_planning.py#L193) | 193 | `"        key = _normalize_key(raw)"` | — |
| [SRC-01273BA196-L000194](../../agents/aspect_planning.py#L194) | 194 | `"        if raw and key not in seen:"` | — |
| [SRC-01273BA196-L000195](../../agents/aspect_planning.py#L195) | 195 | `"            seen.add(key)"` | — |
| [SRC-01273BA196-L000196](../../agents/aspect_planning.py#L196) | 196 | `"            out.append(raw)"` | — |
| [SRC-01273BA196-L000197](../../agents/aspect_planning.py#L197) | 197 | `"        if len(out) >= max(1, min(int(limit), 3)):"` | — |
| [SRC-01273BA196-L000198](../../agents/aspect_planning.py#L198) | 198 | `"            break"` | — |
| [SRC-01273BA196-L000199](../../agents/aspect_planning.py#L199) | 199 | `"    return out"` | — |
| [SRC-01273BA196-L000200](../../agents/aspect_planning.py#L200) | 200 | `""` | — |
| [SRC-01273BA196-L000201](../../agents/aspect_planning.py#L201) | 201 | `""` | — |
| [SRC-01273BA196-L000202](../../agents/aspect_planning.py#L202) | 202 | `"def arabic_aspect_diagnostics(ledger: dict[str, Any]) -> list[str]:"` | — |
| [SRC-01273BA196-L000203](../../agents/aspect_planning.py#L203) | 203 | `"    lines: list[str] = []"` | — |
| [SRC-01273BA196-L000204](../../agents/aspect_planning.py#L204) | 204 | `"    if not ledger or ledger.get(\"note\") == \"no_explicit_aspects\":"` | — |
| [SRC-01273BA196-L000205](../../agents/aspect_planning.py#L205) | 205 | `"        return lines"` | — |
| [SRC-01273BA196-L000206](../../agents/aspect_planning.py#L206) | 206 | `"    covered = ledger.get(\"covered\") or []"` | — |
| [SRC-01273BA196-L000207](../../agents/aspect_planning.py#L207) | 207 | `"    missing = ledger.get(\"missing\") or []"` | — |
| [SRC-01273BA196-L000208](../../agents/aspect_planning.py#L208) | 208 | `"    if covered:"` | — |
| [SRC-01273BA196-L000209](../../agents/aspect_planning.py#L209) | 209 | `"        lines.append(\"محاور وُجد لها مرشح نصي واحد على الأقل: \" + \"، \".join(str(x) for x in covered))"` | — |
| [SRC-01273BA196-L000210](../../agents/aspect_planning.py#L210) | 210 | `"    if missing:"` | — |
| [SRC-01273BA196-L000211](../../agents/aspect_planning.py#L211) | 211 | `"        lines.append(\"محاور بلا مرشح نصي كافٍ في النتائج الحالية: \" + \"، \".join(str(x) for x in missing) + \". هذا لا ينفي وجود معلومات خارج النتائج المجلوبة.\")"` | — |
| [SRC-01273BA196-L000212](../../agents/aspect_planning.py#L212) | 212 | `"    ratio = ledger.get(\"coverage_ratio\")"` | — |
| [SRC-01273BA196-L000213](../../agents/aspect_planning.py#L213) | 213 | `"    if isinstance(ratio, (int, float)):"` | — |
| [SRC-01273BA196-L000214](../../agents/aspect_planning.py#L214) | 214 | `"        lines.append(f\"نسبة تغطية المحاور لفظيًا (تقريبية): {int(ratio * 100)}٪.\")"` | — |
| [SRC-01273BA196-L000215](../../agents/aspect_planning.py#L215) | 215 | `"    lines.append(\"تنبيه: وجود مقتطف يطابق كلمات المحور لا يثبت صحة الادعاء.\")"` | — |
| [SRC-01273BA196-L000216](../../agents/aspect_planning.py#L216) | 216 | `"    return lines"` | — |
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
| [SRC-5587371288-L000164](../../agents/intent_router.py#L164) | 164 | `"def _needs_clarification(question: str) -> bool:"` | — |
| [SRC-5587371288-L000165](../../agents/intent_router.py#L165) | 165 | `"    normalized = _strip_followup_leadin(_normalize(question))"` | — |
| [SRC-5587371288-L000166](../../agents/intent_router.py#L166) | 166 | `"    ambiguous = {_normalize(item) for item in _AMBIGUOUS_ARABIC}"` | — |
| [SRC-5587371288-L000167](../../agents/intent_router.py#L167) | 167 | `"    ambiguous.update(_normalize(item) for item in _AMBIGUOUS_ENGLISH)"` | — |
| [SRC-5587371288-L000168](../../agents/intent_router.py#L168) | 168 | `"    if normalized in ambiguous or normalized in _FOLLOWUP_ASPECT_FRAGMENTS:"` | — |
| [SRC-5587371288-L000169](../../agents/intent_router.py#L169) | 169 | `"        return True"` | — |
| [SRC-5587371288-L000170](../../agents/intent_router.py#L170) | 170 | `"    # Common inflected forms and short property-only follow-ups."` | — |
| [SRC-5587371288-L000171](../../agents/intent_router.py#L171) | 171 | `"    return bool("` | — |
| [SRC-5587371288-L000172](../../agents/intent_router.py#L172) | 172 | `"        re.fullmatch(r\"(?:كام\|كم\|بكام)\\s+(?:سعر\|ثمن)\\s*(?:ها\|ه\|هم)\", normalized)"` | — |
| [SRC-5587371288-L000173](../../agents/intent_router.py#L173) | 173 | `"        or re.fullmatch(r\"(?:قارن\|قارنلي)\\s+(?:بينهم\|بينهما\|دول\|دي\|دولتين)\", normalized)"` | — |
| [SRC-5587371288-L000174](../../agents/intent_router.py#L174) | 174 | `"        or re.fullmatch(r\"(?:و)?(?:السعر\|الاسعار\|التكلفه\|الضمان\|المميزات\|العيوب\|البطاريه\|الكاميرا\|المكان\|المصدر\|الرابط\|التاريخ)\", normalized)"` | — |
| [SRC-5587371288-L000175](../../agents/intent_router.py#L175) | 175 | `"    )"` | — |
| [SRC-5587371288-L000176](../../agents/intent_router.py#L176) | 176 | `""` | — |
| [SRC-5587371288-L000177](../../agents/intent_router.py#L177) | 177 | `""` | — |
| [SRC-5587371288-L000178](../../agents/intent_router.py#L178) | 178 | `"def _is_clarification_message(content: Any) -> bool:"` | — |
| [SRC-5587371288-L000179](../../agents/intent_router.py#L179) | 179 | `"    if not isinstance(content, str):"` | — |
| [SRC-5587371288-L000180](../../agents/intent_router.py#L180) | 180 | `"        return False"` | — |
| [SRC-5587371288-L000181](../../agents/intent_router.py#L181) | 181 | `"    normalized = _normalize(content)"` | — |
| [SRC-5587371288-L000182](../../agents/intent_router.py#L182) | 182 | `"    return any(marker in normalized for marker in ("` | — |
| [SRC-5587371288-L000183](../../agents/intent_router.py#L183) | 183 | `"        \"تقصد ايه تحديدا\", \"اكتب اسم الشيء\", \"ابعت الرابط\","` | — |
| [SRC-5587371288-L000184](../../agents/intent_router.py#L184) | 184 | `"        \"what are you referring to\", \"please name the item\","` | — |
| [SRC-5587371288-L000185](../../agents/intent_router.py#L185) | 185 | `"        \"share its link\", \"clarify what you mean\","` | — |
| [SRC-5587371288-L000186](../../agents/intent_router.py#L186) | 186 | `"    ))"` | — |
| [SRC-5587371288-L000187](../../agents/intent_router.py#L187) | 187 | `""` | — |
| [SRC-5587371288-L000188](../../agents/intent_router.py#L188) | 188 | `""` | — |
| [SRC-5587371288-L000189](../../agents/intent_router.py#L189) | 189 | `"def _latest_context_anchor(history: Any) -> str:"` | — |
| [SRC-5587371288-L000190](../../agents/intent_router.py#L190) | 190 | `"    \"\"\"Find the latest substantive user topic, skipping ellipsis follow-ups only."` | — |
| [SRC-5587371288-L000191](../../agents/intent_router.py#L191) | 191 | `""` | — |
| [SRC-5587371288-L000192](../../agents/intent_router.py#L192) | 192 | `"    A recent acknowledgment is a hard boundary: never search past it for stale topics."` | — |
| [SRC-5587371288-L000193](../../agents/intent_router.py#L193) | 193 | `"    Short entity replies can anchor context when the assistant explicitly asked for one."` | — |
| [SRC-5587371288-L000194](../../agents/intent_router.py#L194) | 194 | `"    \"\"\""` | — |
| [SRC-5587371288-L000195](../../agents/intent_router.py#L195) | 195 | `"    if not isinstance(history, list):"` | — |
| [SRC-5587371288-L000196](../../agents/intent_router.py#L196) | 196 | `"        return \"\""` | — |
| [SRC-5587371288-L000197](../../agents/intent_router.py#L197) | 197 | `"    bounded = history[-MAX_CONTEXT_TURNS:]"` | — |
| [SRC-5587371288-L000198](../../agents/intent_router.py#L198) | 198 | `"    for index in range(len(bounded) - 1, -1, -1):"` | — |
| [SRC-5587371288-L000199](../../agents/intent_router.py#L199) | 199 | `"        item = bounded[index]"` | — |
| [SRC-5587371288-L000200](../../agents/intent_router.py#L200) | 200 | `"        if not isinstance(item, dict) or item.get(\"role\") != \"user\":"` | — |
| [SRC-5587371288-L000201](../../agents/intent_router.py#L201) | 201 | `"            continue"` | — |
| [SRC-5587371288-L000202](../../agents/intent_router.py#L202) | 202 | `"        content = item.get(\"content\")"` | — |
| [SRC-5587371288-L000203](../../agents/intent_router.py#L203) | 203 | `"        if not isinstance(content, str):"` | — |
| [SRC-5587371288-L000204](../../agents/intent_router.py#L204) | 204 | `"            continue"` | — |
| [SRC-5587371288-L000205](../../agents/intent_router.py#L205) | 205 | `"        normalized = _normalize(content)"` | — |
| [SRC-5587371288-L000206](../../agents/intent_router.py#L206) | 206 | `"        if not normalized or _is_smalltalk(normalized):"` | — |
| [SRC-5587371288-L000207](../../agents/intent_router.py#L207) | 207 | `"            return \"\""` | — |
| [SRC-5587371288-L000208](../../agents/intent_router.py#L208) | 208 | `"        if _needs_clarification(content):"` | — |
| [SRC-5587371288-L000209](../../agents/intent_router.py#L209) | 209 | `"            continue"` | — |
| [SRC-5587371288-L000210](../../agents/intent_router.py#L210) | 210 | `"        meaningful = re.findall(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", normalized)"` | — |
| [SRC-5587371288-L000211](../../agents/intent_router.py#L211) | 211 | `"        if len(meaningful) >= 2 and len(normalized) >= 8:"` | — |
| [SRC-5587371288-L000212](../../agents/intent_router.py#L212) | 212 | `"            return re.sub(r\"\\s+\", \" \", content).strip()[:300]"` | — |
| [SRC-5587371288-L000213](../../agents/intent_router.py#L213) | 213 | `"        if index > 0:"` | — |
| [SRC-5587371288-L000214](../../agents/intent_router.py#L214) | 214 | `"            previous = bounded[index - 1]"` | — |
| [SRC-5587371288-L000215](../../agents/intent_router.py#L215) | 215 | `"            if isinstance(previous, dict) and previous.get(\"role\") == \"assistant\" and _is_clarification_message(previous.get(\"content\")):"` | — |
| [SRC-5587371288-L000216](../../agents/intent_router.py#L216) | 216 | `"                return re.sub(r\"\\s+\", \" \", content).strip()[:120]"` | — |
| [SRC-5587371288-L000217](../../agents/intent_router.py#L217) | 217 | `"        return \"\""` | — |
| [SRC-5587371288-L000218](../../agents/intent_router.py#L218) | 218 | `"    return \"\""` | — |
| [SRC-5587371288-L000219](../../agents/intent_router.py#L219) | 219 | `""` | — |
| [SRC-5587371288-L000220](../../agents/intent_router.py#L220) | 220 | `""` | — |
| [SRC-5587371288-L000221](../../agents/intent_router.py#L221) | 221 | `"def _pending_clarification_query(history: Any) -> str:"` | — |
| [SRC-5587371288-L000222](../../agents/intent_router.py#L222) | 222 | `"    \"\"\"Return the unresolved elliptical question immediately awaiting a user slot-fill.\"\"\""` | — |
| [SRC-5587371288-L000223](../../agents/intent_router.py#L223) | 223 | `"    if not isinstance(history, list) or not history:"` | — |
| [SRC-5587371288-L000224](../../agents/intent_router.py#L224) | 224 | `"        return \"\""` | — |
| [SRC-5587371288-L000225](../../agents/intent_router.py#L225) | 225 | `"    last_index = len(history) - 1"` | — |
| [SRC-5587371288-L000226](../../agents/intent_router.py#L226) | 226 | `"    while last_index >= 0 and not ("` | — |
| [SRC-5587371288-L000227](../../agents/intent_router.py#L227) | 227 | `"        isinstance(history[last_index], dict)"` | — |
| [SRC-5587371288-L000228](../../agents/intent_router.py#L228) | 228 | `"        and isinstance(history[last_index].get(\"content\"), str)"` | — |
| [SRC-5587371288-L000229](../../agents/intent_router.py#L229) | 229 | `"        and history[last_index].get(\"content\", \"\").strip()"` | — |
| [SRC-5587371288-L000230](../../agents/intent_router.py#L230) | 230 | `"    ):"` | — |
| [SRC-5587371288-L000231](../../agents/intent_router.py#L231) | 231 | `"        last_index -= 1"` | — |
| [SRC-5587371288-L000232](../../agents/intent_router.py#L232) | 232 | `"    if last_index < 0 or history[last_index].get(\"role\") != \"assistant\":"` | — |
| [SRC-5587371288-L000233](../../agents/intent_router.py#L233) | 233 | `"        return \"\""` | — |
| [SRC-5587371288-L000234](../../agents/intent_router.py#L234) | 234 | `"    if not _is_clarification_message(history[last_index].get(\"content\")):"` | — |
| [SRC-5587371288-L000235](../../agents/intent_router.py#L235) | 235 | `"        return \"\""` | — |
| [SRC-5587371288-L000236](../../agents/intent_router.py#L236) | 236 | `"    for index in range(last_index - 1, -1, -1):"` | — |
| [SRC-5587371288-L000237](../../agents/intent_router.py#L237) | 237 | `"        item = history[index]"` | — |
| [SRC-5587371288-L000238](../../agents/intent_router.py#L238) | 238 | `"        if isinstance(item, dict) and item.get(\"role\") == \"user\":"` | — |
| [SRC-5587371288-L000239](../../agents/intent_router.py#L239) | 239 | `"            content = item.get(\"content\")"` | — |
| [SRC-5587371288-L000240](../../agents/intent_router.py#L240) | 240 | `"            if not isinstance(content, str) or not _needs_clarification(content):"` | — |
| [SRC-5587371288-L000241](../../agents/intent_router.py#L241) | 241 | `"                return \"\""` | — |
| [SRC-5587371288-L000242](../../agents/intent_router.py#L242) | 242 | `"            if _latest_context_anchor(history[:index]):"` | — |
| [SRC-5587371288-L000243](../../agents/intent_router.py#L243) | 243 | `"                return \"\""` | — |
| [SRC-5587371288-L000244](../../agents/intent_router.py#L244) | 244 | `"            return content.strip()[:180]"` | — |
| [SRC-5587371288-L000245](../../agents/intent_router.py#L245) | 245 | `"    return \"\""` | — |
| [SRC-5587371288-L000246](../../agents/intent_router.py#L246) | 246 | `""` | — |
| [SRC-5587371288-L000247](../../agents/intent_router.py#L247) | 247 | `""` | — |
| [SRC-5587371288-L000248](../../agents/intent_router.py#L248) | 248 | `"def _is_clarification_answer(question: str, history: Any) -> bool:"` | — |
| [SRC-5587371288-L000249](../../agents/intent_router.py#L249) | 249 | `"    \"\"\"Recognize a concise answer to Omarai's immediately preceding clarification.\"\"\""` | — |
| [SRC-5587371288-L000250](../../agents/intent_router.py#L250) | 250 | `"    if not _pending_clarification_query(history) or not isinstance(question, str):"` | — |
| [SRC-5587371288-L000251](../../agents/intent_router.py#L251) | 251 | `"        return False"` | — |
| [SRC-5587371288-L000252](../../agents/intent_router.py#L252) | 252 | `"    query = question.strip()"` | — |
| [SRC-5587371288-L000253](../../agents/intent_router.py#L253) | 253 | `"    if not query or len(query) >= 100 or _needs_clarification(query) or _is_smalltalk(query):"` | — |
| [SRC-5587371288-L000254](../../agents/intent_router.py#L254) | 254 | `"        return False"` | — |
| [SRC-5587371288-L000255](../../agents/intent_router.py#L255) | 255 | `"    # A self-contained live request should not be mistaken for a slot-fill."` | — |
| [SRC-5587371288-L000256](../../agents/intent_router.py#L256) | 256 | `"    return not (_has_live_signal(query) or re.search(r\"https?://\", query, re.IGNORECASE))"` | — |
| [SRC-5587371288-L000257](../../agents/intent_router.py#L257) | 257 | `""` | — |
| [SRC-5587371288-L000258](../../agents/intent_router.py#L258) | 258 | `""` | — |
| [SRC-5587371288-L000259](../../agents/intent_router.py#L259) | 259 | `"def _is_contextual_followup(question: str) -> bool:"` | — |
| [SRC-5587371288-L000260](../../agents/intent_router.py#L260) | 260 | `"    \"\"\"Detect short referent-dependent follow-ups without treating every 'okay' as one.\"\"\""` | — |
| [SRC-5587371288-L000261](../../agents/intent_router.py#L261) | 261 | `"    if not isinstance(question, str) or len(question.strip()) >= 100:"` | — |
| [SRC-5587371288-L000262](../../agents/intent_router.py#L262) | 262 | `"        return False"` | — |
| [SRC-5587371288-L000263](../../agents/intent_router.py#L263) | 263 | `"    if re.search(r\"https?://\", question, re.IGNORECASE):"` | — |
| [SRC-5587371288-L000264](../../agents/intent_router.py#L264) | 264 | `"        return False"` | — |
| [SRC-5587371288-L000265](../../agents/intent_router.py#L265) | 265 | `"    normalized = _strip_followup_leadin(_normalize(question))"` | — |
| [SRC-5587371288-L000266](../../agents/intent_router.py#L266) | 266 | `"    if _needs_clarification(question):"` | — |
| [SRC-5587371288-L000267](../../agents/intent_router.py#L267) | 267 | `"        return True"` | — |
| [SRC-5587371288-L000268](../../agents/intent_router.py#L268) | 268 | `"    # Pronouns and deictic references are strong signals only in a short turn."` | — |
| [SRC-5587371288-L000269](../../agents/intent_router.py#L269) | 269 | `"    return bool("` | — |
| [SRC-5587371288-L000270](../../agents/intent_router.py#L270) | 270 | `"        re.fullmatch("` | — |
| [SRC-5587371288-L000271](../../agents/intent_router.py#L271) | 271 | `"            r\"(?:و)?(?:هي\|هو\|دي\|ده\|دول\|هما\|ذلك\|تلك\|عليها\|عليه\|فيها\|فيه\|لها\|له\|\""` | — |
| [SRC-5587371288-L000272](../../agents/intent_router.py#L272) | 272 | `"            r\"سعرها\|سعره\|مكانها\|مكانه\|ضمانها\|ضمانه\|بطاريتها\|كاميرتها\|مميزاتها\|عيوبها)\","` | — |
| [SRC-5587371288-L000273](../../agents/intent_router.py#L273) | 273 | `"            normalized,"` | — |
| [SRC-5587371288-L000274](../../agents/intent_router.py#L274) | 274 | `"        )"` | — |
| [SRC-5587371288-L000275](../../agents/intent_router.py#L275) | 275 | `"    )"` | — |
| [SRC-5587371288-L000276](../../agents/intent_router.py#L276) | 276 | `""` | — |
| [SRC-5587371288-L000277](../../agents/intent_router.py#L277) | 277 | `""` | — |
| [SRC-5587371288-L000278](../../agents/intent_router.py#L278) | 278 | `"def resolve_followup_query(question: str, history: Any = None) -> str:"` | — |
| [SRC-5587371288-L000279](../../agents/intent_router.py#L279) | 279 | `"    \"\"\"Resolve a short contextual follow-up against the nearest substantive topic."` | — |
| [SRC-5587371288-L000280](../../agents/intent_router.py#L280) | 280 | `""` | — |
| [SRC-5587371288-L000281](../../agents/intent_router.py#L281) | 281 | `"    Repeated follow-ups retain the original topic. An answer to an explicit"` | — |
| [SRC-5587371288-L000282](../../agents/intent_router.py#L282) | 282 | `"    clarification is joined to the pending question. New standalone questions are"` | — |
| [SRC-5587371288-L000283](../../agents/intent_router.py#L283) | 283 | `"    never merged merely because they start with 'طيب' or 'طب'."` | — |
| [SRC-5587371288-L000284](../../agents/intent_router.py#L284) | 284 | `"    \"\"\""` | — |
| [SRC-5587371288-L000285](../../agents/intent_router.py#L285) | 285 | `"    if not isinstance(question, str):"` | — |
| [SRC-5587371288-L000286](../../agents/intent_router.py#L286) | 286 | `"        return \"\""` | — |
| [SRC-5587371288-L000287](../../agents/intent_router.py#L287) | 287 | `"    query = re.sub(r\"\\s+\", \" \", question).strip()"` | — |
| [SRC-5587371288-L000288](../../agents/intent_router.py#L288) | 288 | `"    if not query:"` | — |
| [SRC-5587371288-L000289](../../agents/intent_router.py#L289) | 289 | `"        return \"\""` | — |
| [SRC-5587371288-L000290](../../agents/intent_router.py#L290) | 290 | `"    pending = _pending_clarification_query(history)"` | — |
| [SRC-5587371288-L000291](../../agents/intent_router.py#L291) | 291 | `"    if pending and _is_clarification_answer(query, history):"` | — |
| [SRC-5587371288-L000292](../../agents/intent_router.py#L292) | 292 | `"        return f\"{pending[:220]} — {query[:180]}\"[:500]"` | — |
| [SRC-5587371288-L000293](../../agents/intent_router.py#L293) | 293 | `"    if len(query) >= 100 or not isinstance(history, list):"` | — |
| [SRC-5587371288-L000294](../../agents/intent_router.py#L294) | 294 | `"        return query[:500]"` | — |
| [SRC-5587371288-L000295](../../agents/intent_router.py#L295) | 295 | `"    if not _is_contextual_followup(query):"` | — |
| [SRC-5587371288-L000296](../../agents/intent_router.py#L296) | 296 | `"        return query[:500]"` | — |
| [SRC-5587371288-L000297](../../agents/intent_router.py#L297) | 297 | `"    previous = _latest_context_anchor(history)"` | — |
| [SRC-5587371288-L000298](../../agents/intent_router.py#L298) | 298 | `"    if not previous:"` | — |
| [SRC-5587371288-L000299](../../agents/intent_router.py#L299) | 299 | `"        return query[:500]"` | — |
| [SRC-5587371288-L000300](../../agents/intent_router.py#L300) | 300 | `"    return f\"{previous[:300]} — {query[:180]}\"[:500]"` | — |
| [SRC-5587371288-L000301](../../agents/intent_router.py#L301) | 301 | `""` | — |
| [SRC-5587371288-L000302](../../agents/intent_router.py#L302) | 302 | `""` | — |
| [SRC-5587371288-L000303](../../agents/intent_router.py#L303) | 303 | `"def _has_explicit_source_request(question: str) -> bool:"` | — |
| [SRC-5587371288-L000304](../../agents/intent_router.py#L304) | 304 | `"    \"\"\"Recognize explicit requests for evidence/citations that require web-backed retrieval.\"\"\""` | — |
| [SRC-5587371288-L000305](../../agents/intent_router.py#L305) | 305 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000306](../../agents/intent_router.py#L306) | 306 | `"    markers = ("` | — |
| [SRC-5587371288-L000307](../../agents/intent_router.py#L307) | 307 | `"        \"اذكر مصادر\", \"اذكر المصدر\", \"مصادر موثوقة\", \"مصدر موثوق\","` | — |
| [SRC-5587371288-L000308](../../agents/intent_router.py#L308) | 308 | `"        \"مصادر رسمية\", \"مصادر حديثة\", \"مع مصادر\", \"مع المصادر\","` | — |
| [SRC-5587371288-L000309](../../agents/intent_router.py#L309) | 309 | `"        \"بالمصادر\", \"روابط المصادر\", \"ارفق المصادر\", \"أرفق المصادر\","` | — |
| [SRC-5587371288-L000310](../../agents/intent_router.py#L310) | 310 | `"        \"استشهد بمصادر\", \"وثق الاجابة\", \"وثق الإجابة\", \"المراجع\","` | — |
| [SRC-5587371288-L000311](../../agents/intent_router.py#L311) | 311 | `"        \"with sources\", \"cite sources\", \"trusted sources\", \"reliable sources\","` | — |
| [SRC-5587371288-L000312](../../agents/intent_router.py#L312) | 312 | `"        \"official sources\", \"include references\", \"with citations\","` | — |
| [SRC-5587371288-L000313](../../agents/intent_router.py#L313) | 313 | `"        \"source-backed\", \"cite your sources\","` | — |
| [SRC-5587371288-L000314](../../agents/intent_router.py#L314) | 314 | `"    )"` | — |
| [SRC-5587371288-L000315](../../agents/intent_router.py#L315) | 315 | `"    return any(_normalize(marker) in normalized for marker in markers)"` | — |
| [SRC-5587371288-L000316](../../agents/intent_router.py#L316) | 316 | `""` | — |
| [SRC-5587371288-L000317](../../agents/intent_router.py#L317) | 317 | `""` | — |
| [SRC-5587371288-L000318](../../agents/intent_router.py#L318) | 318 | `"def _is_deep(question: str) -> bool:"` | — |
| [SRC-5587371288-L000319](../../agents/intent_router.py#L319) | 319 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000320](../../agents/intent_router.py#L320) | 320 | `"    if any(_normalize(term) in normalized for term in _DEEP_TERMS):"` | — |
| [SRC-5587371288-L000321](../../agents/intent_router.py#L321) | 321 | `"        return True"` | — |
| [SRC-5587371288-L000322](../../agents/intent_router.py#L322) | 322 | `"    # Explicit multi-dimension comparisons need evidence from more than one angle."` | — |
| [SRC-5587371288-L000323](../../agents/intent_router.py#L323) | 323 | `"    dimensions = ("` | — |
| [SRC-5587371288-L000324](../../agents/intent_router.py#L324) | 324 | `"        \"السعر\", \"سعر\", \"بطاريه\", \"كاميرا\", \"اداء\", \"امان\", \"تكلفه\","` | — |
| [SRC-5587371288-L000325](../../agents/intent_router.py#L325) | 325 | `"        \"الصيانه\", \"الجوده\", \"المميزات\", \"العيوب\", \"الاراء\", \"المراجعات\","` | — |
| [SRC-5587371288-L000326](../../agents/intent_router.py#L326) | 326 | `"        \"price\", \"battery\", \"camera\", \"performance\", \"safety\", \"cost\","` | — |
| [SRC-5587371288-L000327](../../agents/intent_router.py#L327) | 327 | `"        \"maintenance\", \"quality\", \"features\", \"drawbacks\", \"reviews\","` | — |
| [SRC-5587371288-L000328](../../agents/intent_router.py#L328) | 328 | `"    )"` | — |
| [SRC-5587371288-L000329](../../agents/intent_router.py#L329) | 329 | `"    matched_dimensions = sum(1 for item in dimensions if _normalize(item) in normalized)"` | — |
| [SRC-5587371288-L000330](../../agents/intent_router.py#L330) | 330 | `"    return matched_dimensions >= 2 and any("` | — |
| [SRC-5587371288-L000331](../../agents/intent_router.py#L331) | 331 | `"        marker in normalized for marker in _MULTIPART_MARKERS"` | — |
| [SRC-5587371288-L000332](../../agents/intent_router.py#L332) | 332 | `"    )"` | — |
| [SRC-5587371288-L000333](../../agents/intent_router.py#L333) | 333 | `""` | — |
| [SRC-5587371288-L000334](../../agents/intent_router.py#L334) | 334 | `""` | — |
| [SRC-5587371288-L000335](../../agents/intent_router.py#L335) | 335 | `"def _is_page_summarization_request(question: str) -> bool:"` | — |
| [SRC-5587371288-L000336](../../agents/intent_router.py#L336) | 336 | `"    \"\"\"Recognize a request to summarize a specific web page or link.\"\"\""` | — |
| [SRC-5587371288-L000337](../../agents/intent_router.py#L337) | 337 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000338](../../agents/intent_router.py#L338) | 338 | `"    terms = (\"لخص\", \"تلخيص\", \"ملخص\", \"summarize\", \"summarise\", \"summary\")"` | — |
| [SRC-5587371288-L000339](../../agents/intent_router.py#L339) | 339 | `"    page_references = ("` | — |
| [SRC-5587371288-L000340](../../agents/intent_router.py#L340) | 340 | `"        \"صفحه\", \"الصفحه\", \"مقال\", \"المقال\", \"رابط\", \"لينك\", \"url\","` | — |
| [SRC-5587371288-L000341](../../agents/intent_router.py#L341) | 341 | `"        \"link\", \"article\", \"page\", \"webpage\", \"web page\", \"website\","` | — |
| [SRC-5587371288-L000342](../../agents/intent_router.py#L342) | 342 | `"    )"` | — |
| [SRC-5587371288-L000343](../../agents/intent_router.py#L343) | 343 | `"    return ("` | — |
| [SRC-5587371288-L000344](../../agents/intent_router.py#L344) | 344 | `"        any(_normalize(term) in normalized for term in terms)"` | — |
| [SRC-5587371288-L000345](../../agents/intent_router.py#L345) | 345 | `"        and ("` | — |
| [SRC-5587371288-L000346](../../agents/intent_router.py#L346) | 346 | `"            bool(re.search(r\"https?://\", question, flags=re.IGNORECASE))"` | — |
| [SRC-5587371288-L000347](../../agents/intent_router.py#L347) | 347 | `"            or any(_normalize(term) in normalized for term in page_references)"` | — |
| [SRC-5587371288-L000348](../../agents/intent_router.py#L348) | 348 | `"        )"` | — |
| [SRC-5587371288-L000349](../../agents/intent_router.py#L349) | 349 | `"    )"` | — |
| [SRC-5587371288-L000350](../../agents/intent_router.py#L350) | 350 | `""` | — |
| [SRC-5587371288-L000351](../../agents/intent_router.py#L351) | 351 | `""` | — |
| [SRC-5587371288-L000352](../../agents/intent_router.py#L352) | 352 | `"def _has_inline_summary_text(question: str) -> bool:"` | — |
| [SRC-5587371288-L000353](../../agents/intent_router.py#L353) | 353 | `"    \"\"\"Detect text explicitly pasted after a summary instruction, not a web page URL.\"\"\""` | — |
| [SRC-5587371288-L000354](../../agents/intent_router.py#L354) | 354 | `"    if re.search(r\"https?://\", question, flags=re.IGNORECASE):"` | — |
| [SRC-5587371288-L000355](../../agents/intent_router.py#L355) | 355 | `"        return False"` | — |
| [SRC-5587371288-L000356](../../agents/intent_router.py#L356) | 356 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000357](../../agents/intent_router.py#L357) | 357 | `"    markers = ("` | — |
| [SRC-5587371288-L000358](../../agents/intent_router.py#L358) | 358 | `"        \"النص التالي\", \"النص الاتي\", \"النص ده\", \"النص اللي جاي\","` | — |
| [SRC-5587371288-L000359](../../agents/intent_router.py#L359) | 359 | `"        \"this text\", \"following text\", \"the following text\", \"text below\","` | — |
| [SRC-5587371288-L000360](../../agents/intent_router.py#L360) | 360 | `"        \"text to summarize\", \"content below\","` | — |
| [SRC-5587371288-L000361](../../agents/intent_router.py#L361) | 361 | `"    )"` | — |
| [SRC-5587371288-L000362](../../agents/intent_router.py#L362) | 362 | `"    for marker in markers:"` | — |
| [SRC-5587371288-L000363](../../agents/intent_router.py#L363) | 363 | `"        normalized_marker = _normalize(marker)"` | — |
| [SRC-5587371288-L000364](../../agents/intent_router.py#L364) | 364 | `"        if normalized_marker in normalized:"` | — |
| [SRC-5587371288-L000365](../../agents/intent_router.py#L365) | 365 | `"            remainder = normalized.split(normalized_marker, 1)[1].strip()"` | — |
| [SRC-5587371288-L000366](../../agents/intent_router.py#L366) | 366 | `"            if len(remainder) >= 8:"` | — |
| [SRC-5587371288-L000367](../../agents/intent_router.py#L367) | 367 | `"                return True"` | — |
| [SRC-5587371288-L000368](../../agents/intent_router.py#L368) | 368 | `"    # Also allow a concise direct form such as \"لخص: [pasted paragraph]\"."` | — |
| [SRC-5587371288-L000369](../../agents/intent_router.py#L369) | 369 | `"    return bool("` | — |
| [SRC-5587371288-L000370](../../agents/intent_router.py#L370) | 370 | `"        re.search("` | — |
| [SRC-5587371288-L000371](../../agents/intent_router.py#L371) | 371 | `"            r\"^\\s*(?:لخص(?:\\s+لي)?\|تلخيص\|summari[sz]e\|summary)\\s*[:：]\\s*\\S.{12,}$\","` | — |
| [SRC-5587371288-L000372](../../agents/intent_router.py#L372) | 372 | `"            question,"` | — |
| [SRC-5587371288-L000373](../../agents/intent_router.py#L373) | 373 | `"            flags=re.IGNORECASE,"` | — |
| [SRC-5587371288-L000374](../../agents/intent_router.py#L374) | 374 | `"        )"` | — |
| [SRC-5587371288-L000375](../../agents/intent_router.py#L375) | 375 | `"    )"` | — |
| [SRC-5587371288-L000376](../../agents/intent_router.py#L376) | 376 | `""` | — |
| [SRC-5587371288-L000377](../../agents/intent_router.py#L377) | 377 | `""` | — |
| [SRC-5587371288-L000378](../../agents/intent_router.py#L378) | 378 | `"def route_intent("` | — |
| [SRC-5587371288-L000379](../../agents/intent_router.py#L379) | 379 | `"    question: str,"` | — |
