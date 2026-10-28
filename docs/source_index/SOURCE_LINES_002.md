# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **002**
- سجلات الأسطر: **800**
- النطاق: SRC-138992B1FC-L000198 إلى SRC-2D53795445-L000125
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-138992B1FC — [agents/answer_validation.py](../../agents/answer_validation.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-138992B1FC-L000198](../../agents/answer_validation.py#L198) | 198 | `"    citable_sources = safe_sources[:12]"` | — |
| [SRC-138992B1FC-L000199](../../agents/answer_validation.py#L199) | 199 | `"    source_token_sets: list[set[str]] = []"` | — |
| [SRC-138992B1FC-L000200](../../agents/answer_validation.py#L200) | 200 | `"    source_bases: list[str] = []"` | — |
| [SRC-138992B1FC-L000201](../../agents/answer_validation.py#L201) | 201 | `"    for source in citable_sources:"` | — |
| [SRC-138992B1FC-L000202](../../agents/answer_validation.py#L202) | 202 | `"        page_text = str(source.get(\"page_text\") or \"\")"` | — |
| [SRC-138992B1FC-L000203](../../agents/answer_validation.py#L203) | 203 | `"        snippet = str(source.get(\"snippet\") or \"\")"` | — |
| [SRC-138992B1FC-L000204](../../agents/answer_validation.py#L204) | 204 | `"        title = str(source.get(\"title\") or \"\")"` | — |
| [SRC-138992B1FC-L000205](../../agents/answer_validation.py#L205) | 205 | `"        if bool(source.get(\"page_fetched\")) and page_text.strip():"` | — |
| [SRC-138992B1FC-L000206](../../agents/answer_validation.py#L206) | 206 | `"            selected_text = page_text"` | — |
| [SRC-138992B1FC-L000207](../../agents/answer_validation.py#L207) | 207 | `"            basis = \"extracted_page_text\""` | — |
| [SRC-138992B1FC-L000208](../../agents/answer_validation.py#L208) | 208 | `"        elif snippet.strip():"` | — |
| [SRC-138992B1FC-L000209](../../agents/answer_validation.py#L209) | 209 | `"            selected_text = snippet"` | — |
| [SRC-138992B1FC-L000210](../../agents/answer_validation.py#L210) | 210 | `"            basis = \"search_snippet\""` | — |
| [SRC-138992B1FC-L000211](../../agents/answer_validation.py#L211) | 211 | `"        elif title.strip():"` | — |
| [SRC-138992B1FC-L000212](../../agents/answer_validation.py#L212) | 212 | `"            selected_text = title"` | — |
| [SRC-138992B1FC-L000213](../../agents/answer_validation.py#L213) | 213 | `"            basis = \"title_only\""` | — |
| [SRC-138992B1FC-L000214](../../agents/answer_validation.py#L214) | 214 | `"        else:"` | — |
| [SRC-138992B1FC-L000215](../../agents/answer_validation.py#L215) | 215 | `"            selected_text = \"\""` | — |
| [SRC-138992B1FC-L000216](../../agents/answer_validation.py#L216) | 216 | `"            basis = \"no_readable_text\""` | — |
| [SRC-138992B1FC-L000217](../../agents/answer_validation.py#L217) | 217 | `"        source_token_sets.append(set(_tokens(selected_text, drop_stopwords=True)))"` | — |
| [SRC-138992B1FC-L000218](../../agents/answer_validation.py#L218) | 218 | `"        source_bases.append(basis)"` | — |
| [SRC-138992B1FC-L000219](../../agents/answer_validation.py#L219) | 219 | `""` | — |
| [SRC-138992B1FC-L000220](../../agents/answer_validation.py#L220) | 220 | `"    citation_alignment: list[dict[str, Any]] = []"` | — |
| [SRC-138992B1FC-L000221](../../agents/answer_validation.py#L221) | 221 | `"    sentence_parts = ["` | — |
| [SRC-138992B1FC-L000222](../../agents/answer_validation.py#L222) | 222 | `"        part.strip()"` | — |
| [SRC-138992B1FC-L000223](../../agents/answer_validation.py#L223) | 223 | `"        for part in re.split(r\"(?<=[.!?؟])\\s+\|\\n+\", answer_text)"` | — |
| [SRC-138992B1FC-L000224](../../agents/answer_validation.py#L224) | 224 | `"        if part.strip()"` | — |
| [SRC-138992B1FC-L000225](../../agents/answer_validation.py#L225) | 225 | `"    ]"` | — |
| [SRC-138992B1FC-L000226](../../agents/answer_validation.py#L226) | 226 | `"    for sentence_number, sentence in enumerate(sentence_parts[:40], 1):"` | — |
| [SRC-138992B1FC-L000227](../../agents/answer_validation.py#L227) | 227 | `"        cited_indices = ["` | — |
| [SRC-138992B1FC-L000228](../../agents/answer_validation.py#L228) | 228 | `"            int(match.group(1))"` | — |
| [SRC-138992B1FC-L000229](../../agents/answer_validation.py#L229) | 229 | `"            for match in _CITATION.finditer(sentence)"` | — |
| [SRC-138992B1FC-L000230](../../agents/answer_validation.py#L230) | 230 | `"        ]"` | — |
| [SRC-138992B1FC-L000231](../../agents/answer_validation.py#L231) | 231 | `"        if not cited_indices:"` | — |
| [SRC-138992B1FC-L000232](../../agents/answer_validation.py#L232) | 232 | `"            continue"` | — |
| [SRC-138992B1FC-L000233](../../agents/answer_validation.py#L233) | 233 | `"        claim_tokens = list(dict.fromkeys(_tokens(_CITATION.sub(\" \", sentence), drop_stopwords=True)))"` | — |
| [SRC-138992B1FC-L000234](../../agents/answer_validation.py#L234) | 234 | `"        cited_checks: list[dict[str, Any]] = []"` | — |
| [SRC-138992B1FC-L000235](../../agents/answer_validation.py#L235) | 235 | `"        for source_index in list(dict.fromkeys(cited_indices))[:8]:"` | — |
| [SRC-138992B1FC-L000236](../../agents/answer_validation.py#L236) | 236 | `"            if source_index < 1 or source_index > len(source_token_sets):"` | — |
| [SRC-138992B1FC-L000237](../../agents/answer_validation.py#L237) | 237 | `"                cited_checks.append({"` | — |
| [SRC-138992B1FC-L000238](../../agents/answer_validation.py#L238) | 238 | `"                    \"source_index\": source_index,"` | — |
| [SRC-138992B1FC-L000239](../../agents/answer_validation.py#L239) | 239 | `"                    \"status\": \"source_index_out_of_scope\","` | — |
| [SRC-138992B1FC-L000240](../../agents/answer_validation.py#L240) | 240 | `"                    \"evidence_basis\": \"unavailable\","` | — |
| [SRC-138992B1FC-L000241](../../agents/answer_validation.py#L241) | 241 | `"                    \"matched_terms\": [],"` | — |
| [SRC-138992B1FC-L000242](../../agents/answer_validation.py#L242) | 242 | `"                    \"overlap_ratio\": 0.0,"` | — |
| [SRC-138992B1FC-L000243](../../agents/answer_validation.py#L243) | 243 | `"                })"` | — |
| [SRC-138992B1FC-L000244](../../agents/answer_validation.py#L244) | 244 | `"                continue"` | — |
| [SRC-138992B1FC-L000245](../../agents/answer_validation.py#L245) | 245 | `"            available_tokens = source_token_sets[source_index - 1]"` | — |
| [SRC-138992B1FC-L000246](../../agents/answer_validation.py#L246) | 246 | `"            overlap = [token for token in claim_tokens if token in available_tokens]"` | — |
| [SRC-138992B1FC-L000247](../../agents/answer_validation.py#L247) | 247 | `"            ratio = len(overlap) / len(claim_tokens) if claim_tokens else 0.0"` | — |
| [SRC-138992B1FC-L000248](../../agents/answer_validation.py#L248) | 248 | `"            # A lexical match is only a weak proxy for relevance, not entailment."` | — |
| [SRC-138992B1FC-L000249](../../agents/answer_validation.py#L249) | 249 | `"            # Require both relative coverage and at least two content-token matches."` | — |
| [SRC-138992B1FC-L000250](../../agents/answer_validation.py#L250) | 250 | `"            enough_overlap = len(overlap) >= 2 and ratio >= 0.5"` | — |
| [SRC-138992B1FC-L000251](../../agents/answer_validation.py#L251) | 251 | `"            cited_checks.append({"` | — |
| [SRC-138992B1FC-L000252](../../agents/answer_validation.py#L252) | 252 | `"                \"source_index\": source_index,"` | — |
| [SRC-138992B1FC-L000253](../../agents/answer_validation.py#L253) | 253 | `"                \"status\": \"lexical_overlap_signal_found\" if enough_overlap else \"weak_lexical_overlap\","` | — |
| [SRC-138992B1FC-L000254](../../agents/answer_validation.py#L254) | 254 | `"                \"evidence_basis\": source_bases[source_index - 1],"` | — |
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
| [SRC-01273BA196-L000008](../../agents/aspect_planning.py#L8) | 8 | `"MAX_ASPECTS = 8"` | — |
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
| [SRC-01273BA196-L000021](../../agents/aspect_planning.py#L21) | 21 | `"_DIMENSION_GROUPS = ("` | — |
| [SRC-01273BA196-L000022](../../agents/aspect_planning.py#L22) | 22 | `"    (\"السعر\", (\"السعر\", \"سعر\", \"الأسعار\", \"الاسعار\", \"التكلفة\", \"التكلفه\", \"price\", \"cost\", \"pricing\")),"` | — |
| [SRC-01273BA196-L000023](../../agents/aspect_planning.py#L23) | 23 | `"    (\"البطارية\", (\"البطارية\", \"البطاريه\", \"البطاريات\", \"battery\", \"batteries\")),"` | — |
| [SRC-01273BA196-L000024](../../agents/aspect_planning.py#L24) | 24 | `"    (\"الشحن\", (\"الشحن\", \"charging\", \"charge time\")),"` | — |
| [SRC-01273BA196-L000025](../../agents/aspect_planning.py#L25) | 25 | `"    (\"الضمان\", (\"الضمان\", \"ضمان\", \"warranty\")),"` | — |
| [SRC-01273BA196-L000026](../../agents/aspect_planning.py#L26) | 26 | `"    (\"الصيانة\", (\"الصيانة\", \"الصيانه\", \"الإصلاح\", \"الاصلاح\", \"maintenance\", \"repair\")),"` | — |
| [SRC-01273BA196-L000027](../../agents/aspect_planning.py#L27) | 27 | `"    (\"الأمان\", (\"الأمان\", \"الامان\", \"safety\", \"security\")),"` | — |
| [SRC-01273BA196-L000028](../../agents/aspect_planning.py#L28) | 28 | `"    (\"الكاميرا\", (\"الكاميرا\", \"كاميرا\", \"camera\")),"` | — |
| [SRC-01273BA196-L000029](../../agents/aspect_planning.py#L29) | 29 | `"    (\"الأداء\", (\"الأداء\", \"الاداء\", \"performance\")),"` | — |
| [SRC-01273BA196-L000030](../../agents/aspect_planning.py#L30) | 30 | `"    (\"المميزات\", (\"المميزات\", \"المزايا\", \"features\", \"pros\")),"` | — |
| [SRC-01273BA196-L000031](../../agents/aspect_planning.py#L31) | 31 | `"    (\"العيوب\", (\"العيوب\", \"drawbacks\", \"cons\")),"` | — |
| [SRC-01273BA196-L000032](../../agents/aspect_planning.py#L32) | 32 | `"    (\"المراجعات\", (\"المراجعات\", \"الآراء\", \"الاراء\", \"reviews\", \"opinions\")),"` | — |
| [SRC-01273BA196-L000033](../../agents/aspect_planning.py#L33) | 33 | `"    (\"الخصوصية\", (\"الخصوصية\", \"privacy\")),"` | — |
| [SRC-01273BA196-L000034](../../agents/aspect_planning.py#L34) | 34 | `"    (\"الاعتمادية\", (\"الاعتمادية\", \"الموثوقية\", \"reliability\")),"` | — |
| [SRC-01273BA196-L000035](../../agents/aspect_planning.py#L35) | 35 | `"    (\"الدعم\", (\"الدعم\", \"support\")),"` | — |
| [SRC-01273BA196-L000036](../../agents/aspect_planning.py#L36) | 36 | `"    (\"السرعة\", (\"السرعة\", \"speed\")),"` | — |
| [SRC-01273BA196-L000037](../../agents/aspect_planning.py#L37) | 37 | `"    (\"الجودة\", (\"الجودة\", \"الجوده\", \"quality\")),"` | — |
| [SRC-01273BA196-L000038](../../agents/aspect_planning.py#L38) | 38 | `"    (\"التوفر\", (\"التوفر\", \"التوافر\", \"availability\")),"` | — |
| [SRC-01273BA196-L000039](../../agents/aspect_planning.py#L39) | 39 | `"    (\"المدى\", (\"المدى\", \"range\")),"` | — |
| [SRC-01273BA196-L000040](../../agents/aspect_planning.py#L40) | 40 | `")"` | — |
| [SRC-01273BA196-L000041](../../agents/aspect_planning.py#L41) | 41 | `"_COMPOUND_CONNECTOR_RE = re.compile("` | — |
| [SRC-01273BA196-L000042](../../agents/aspect_planning.py#L42) | 42 | `"    r\"(?:بالإضافة\\s+إلى\|بالاضافة\\s+الى\|إلى\\s+جانب\|الى\\s+جانب\|\""` | — |
| [SRC-01273BA196-L000043](../../agents/aspect_planning.py#L43) | 43 | `"    r\"فضلًا\\s+عن\|فضلا\\s+عن\|بجانب\|as\\s+well\\s+as\|in\\s+addition\\s+to\|\""` | — |
| [SRC-01273BA196-L000044](../../agents/aspect_planning.py#L44) | 44 | `"    r\"along\\s+with\|however\|whereas)\","` | — |
| [SRC-01273BA196-L000045](../../agents/aspect_planning.py#L45) | 45 | `"    flags=re.IGNORECASE,"` | — |
| [SRC-01273BA196-L000046](../../agents/aspect_planning.py#L46) | 46 | `")"` | — |
| [SRC-01273BA196-L000047](../../agents/aspect_planning.py#L47) | 47 | `""` | — |
| [SRC-01273BA196-L000048](../../agents/aspect_planning.py#L48) | 48 | `""` | — |
| [SRC-01273BA196-L000049](../../agents/aspect_planning.py#L49) | 49 | `"def _normalize_space(value: str) -> str:"` | — |
| [SRC-01273BA196-L000050](../../agents/aspect_planning.py#L50) | 50 | `"    return re.sub(r\"\\s+\", \" \", (value or \"\")).strip()"` | — |
| [SRC-01273BA196-L000051](../../agents/aspect_planning.py#L51) | 51 | `""` | — |
| [SRC-01273BA196-L000052](../../agents/aspect_planning.py#L52) | 52 | `""` | — |
| [SRC-01273BA196-L000053](../../agents/aspect_planning.py#L53) | 53 | `"def _normalize_key(value: str) -> str:"` | — |
| [SRC-01273BA196-L000054](../../agents/aspect_planning.py#L54) | 54 | `"    text = _normalize_space(value).casefold()"` | — |
| [SRC-01273BA196-L000055](../../agents/aspect_planning.py#L55) | 55 | `"    text = text.translate(str.maketrans({\"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ة\": \"ه\", \"ى\": \"ي\"}))"` | — |
| [SRC-01273BA196-L000056](../../agents/aspect_planning.py#L56) | 56 | `"    return text"` | — |
| [SRC-01273BA196-L000057](../../agents/aspect_planning.py#L57) | 57 | `""` | — |
| [SRC-01273BA196-L000058](../../agents/aspect_planning.py#L58) | 58 | `""` | — |
| [SRC-01273BA196-L000059](../../agents/aspect_planning.py#L59) | 59 | `"def extract_aspects(question: str) -> list[str]:"` | — |
| [SRC-01273BA196-L000060](../../agents/aspect_planning.py#L60) | 60 | `"    if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-01273BA196-L000061](../../agents/aspect_planning.py#L61) | 61 | `"        return []"` | — |
| [SRC-01273BA196-L000062](../../agents/aspect_planning.py#L62) | 62 | `"    text = question.strip()[:4000]"` | — |
| [SRC-01273BA196-L000063](../../agents/aspect_planning.py#L63) | 63 | `"    match = _ASPECT_MARKER_RE.search(text)"` | — |
| [SRC-01273BA196-L000064](../../agents/aspect_planning.py#L64) | 64 | `"    pieces: list[str] = []"` | — |
| [SRC-01273BA196-L000065](../../agents/aspect_planning.py#L65) | 65 | `"    if match:"` | — |
| [SRC-01273BA196-L000066](../../agents/aspect_planning.py#L66) | 66 | `"        raw = match.group(1)"` | — |
| [SRC-01273BA196-L000067](../../agents/aspect_planning.py#L67) | 67 | `"        raw = re.split("` | — |
| [SRC-01273BA196-L000068](../../agents/aspect_planning.py#L68) | 68 | `"            r\"(?:،\|,\|؛\|;)\\s*(?:و?اذكر\|و?وضح\|بيّن\|اشرح\|and\\s+(?:explain\|note\|discuss))\\b\","` | — |
| [SRC-01273BA196-L000069](../../agents/aspect_planning.py#L69) | 69 | `"            raw, maxsplit=1, flags=re.IGNORECASE,"` | — |
| [SRC-01273BA196-L000070](../../agents/aspect_planning.py#L70) | 70 | `"        )[0]"` | — |
| [SRC-01273BA196-L000071](../../agents/aspect_planning.py#L71) | 71 | `"        pieces = re.split("` | — |
| [SRC-01273BA196-L000072](../../agents/aspect_planning.py#L72) | 72 | `"            r\"\\s*(?:،\|,\|؛\|;\|/)\\s*\|\\s+\\band\\b\\s+\|\\s+\\bas well as\\b\\s+\|\""` | — |
| [SRC-01273BA196-L000073](../../agents/aspect_planning.py#L73) | 73 | `"            r\"\\s+و(?=ال\|[ء-ي])\|\\s+(?:بالإضافة\\s+إلى\|بالاضافة\\s+الى\|\""` | — |
| [SRC-01273BA196-L000074](../../agents/aspect_planning.py#L74) | 74 | `"            r\"إلى\\s+جانب\|الى\\s+جانب\|فضلًا\\s+عن\|فضلا\\s+عن\|بجانب\|\""` | — |
| [SRC-01273BA196-L000075](../../agents/aspect_planning.py#L75) | 75 | `"            r\"in\\s+addition\\s+to\|along\\s+with)\\s+\","` | — |
| [SRC-01273BA196-L000076](../../agents/aspect_planning.py#L76) | 76 | `"            raw, flags=re.IGNORECASE,"` | — |
| [SRC-01273BA196-L000077](../../agents/aspect_planning.py#L77) | 77 | `"        )"` | — |
| [SRC-01273BA196-L000078](../../agents/aspect_planning.py#L78) | 78 | `"    else:"` | — |
| [SRC-01273BA196-L000079](../../agents/aspect_planning.py#L79) | 79 | `"        question_parts = ["` | — |
| [SRC-01273BA196-L000080](../../agents/aspect_planning.py#L80) | 80 | `"            part.strip(\" \\t\\r\\n-•\")"` | — |
| [SRC-01273BA196-L000081](../../agents/aspect_planning.py#L81) | 81 | `"            for part in re.split(r\"[؟?]+\", text)"` | — |
| [SRC-01273BA196-L000082](../../agents/aspect_planning.py#L82) | 82 | `"            if len(part.strip(\" \\t\\r\\n-•\")) >= 4"` | — |
| [SRC-01273BA196-L000083](../../agents/aspect_planning.py#L83) | 83 | `"        ]"` | — |
| [SRC-01273BA196-L000084](../../agents/aspect_planning.py#L84) | 84 | `"        if len(question_parts) > 1:"` | — |
| [SRC-01273BA196-L000085](../../agents/aspect_planning.py#L85) | 85 | `"            pieces = question_parts"` | — |
| [SRC-01273BA196-L000086](../../agents/aspect_planning.py#L86) | 86 | `"        else:"` | — |
| [SRC-01273BA196-L000087](../../agents/aspect_planning.py#L87) | 87 | `"            normalized_text = _normalize_key(text)"` | — |
| [SRC-01273BA196-L000088](../../agents/aspect_planning.py#L88) | 88 | `"            found_facets = ["` | — |
| [SRC-01273BA196-L000089](../../agents/aspect_planning.py#L89) | 89 | `"                canonical"` | — |
| [SRC-01273BA196-L000090](../../agents/aspect_planning.py#L90) | 90 | `"                for canonical, aliases in _DIMENSION_GROUPS"` | — |
| [SRC-01273BA196-L000091](../../agents/aspect_planning.py#L91) | 91 | `"                if any(_normalize_key(alias) in normalized_text for alias in aliases)"` | — |
| [SRC-01273BA196-L000092](../../agents/aspect_planning.py#L92) | 92 | `"            ]"` | — |
| [SRC-01273BA196-L000093](../../agents/aspect_planning.py#L93) | 93 | `"            # Joined facet nouns (e.g. \"price and warranty\") are compound"` | — |
| [SRC-01273BA196-L000094](../../agents/aspect_planning.py#L94) | 94 | `"            # requirements even when the user omits a formal comparison phrase."` | — |
| [SRC-01273BA196-L000095](../../agents/aspect_planning.py#L95) | 95 | `"            if ("` | — |
| [SRC-01273BA196-L000096](../../agents/aspect_planning.py#L96) | 96 | `"                len(found_facets) >= 2"` | — |
| [SRC-01273BA196-L000097](../../agents/aspect_planning.py#L97) | 97 | `"                or _COMPARE_RE.search(text)"` | — |
| [SRC-01273BA196-L000098](../../agents/aspect_planning.py#L98) | 98 | `"                or _COMPOUND_CONNECTOR_RE.search(text)"` | — |
| [SRC-01273BA196-L000099](../../agents/aspect_planning.py#L99) | 99 | `"            ):"` | — |
| [SRC-01273BA196-L000100](../../agents/aspect_planning.py#L100) | 100 | `"                pieces = found_facets[:MAX_ASPECTS]"` | — |
| [SRC-01273BA196-L000101](../../agents/aspect_planning.py#L101) | 101 | `"    targets: list[str] = []"` | — |
| [SRC-01273BA196-L000102](../../agents/aspect_planning.py#L102) | 102 | `"    seen: set[str] = set()"` | — |
| [SRC-01273BA196-L000103](../../agents/aspect_planning.py#L103) | 103 | `"    for piece in pieces:"` | — |
| [SRC-01273BA196-L000104](../../agents/aspect_planning.py#L104) | 104 | `"        target = re.sub(r\"^[\\s:،,؛;/.!?\\-–—]+\|[\\s:،,؛;/.!?\\-–—]+$\", \"\", piece).strip()"` | — |
| [SRC-01273BA196-L000105](../../agents/aspect_planning.py#L105) | 105 | `"        target = re.sub(r\"^(?:و\\s*)\", \"\", target).strip()"` | — |
| [SRC-01273BA196-L000106](../../agents/aspect_planning.py#L106) | 106 | `"        if len(target) < 2:"` | — |
| [SRC-01273BA196-L000107](../../agents/aspect_planning.py#L107) | 107 | `"            continue"` | — |
| [SRC-01273BA196-L000108](../../agents/aspect_planning.py#L108) | 108 | `"        if len(target) > 120:"` | — |
| [SRC-01273BA196-L000109](../../agents/aspect_planning.py#L109) | 109 | `"            target = target[:120].rsplit(\" \", 1)[0].strip()"` | — |
| [SRC-01273BA196-L000110](../../agents/aspect_planning.py#L110) | 110 | `"        key = _normalize_key(target)"` | — |
| [SRC-01273BA196-L000111](../../agents/aspect_planning.py#L111) | 111 | `"        if key and key not in seen:"` | — |
| [SRC-01273BA196-L000112](../../agents/aspect_planning.py#L112) | 112 | `"            seen.add(key)"` | — |
| [SRC-01273BA196-L000113](../../agents/aspect_planning.py#L113) | 113 | `"            targets.append(target)"` | — |
| [SRC-01273BA196-L000114](../../agents/aspect_planning.py#L114) | 114 | `"        if len(targets) >= MAX_ASPECTS:"` | — |
| [SRC-01273BA196-L000115](../../agents/aspect_planning.py#L115) | 115 | `"            break"` | — |
| [SRC-01273BA196-L000116](../../agents/aspect_planning.py#L116) | 116 | `"    return targets"` | — |
| [SRC-01273BA196-L000117](../../agents/aspect_planning.py#L117) | 117 | `""` | — |
| [SRC-01273BA196-L000118](../../agents/aspect_planning.py#L118) | 118 | `""` | — |
| [SRC-01273BA196-L000119](../../agents/aspect_planning.py#L119) | 119 | `"def build_aspect_queries(topic_query: str, aspects: list[str], *, limit: int = MAX_PLAN_QUERIES) -> list[str]:"` | — |
| [SRC-01273BA196-L000120](../../agents/aspect_planning.py#L120) | 120 | `"    queries: list[str] = []"` | — |
| [SRC-01273BA196-L000121](../../agents/aspect_planning.py#L121) | 121 | `"    seen: set[str] = set()"` | — |
| [SRC-01273BA196-L000122](../../agents/aspect_planning.py#L122) | 122 | `"    topic = _normalize_space(topic_query)"` | — |
| [SRC-01273BA196-L000123](../../agents/aspect_planning.py#L123) | 123 | `"    if topic:"` | — |
| [SRC-01273BA196-L000124](../../agents/aspect_planning.py#L124) | 124 | `"        queries.append(topic)"` | — |
| [SRC-01273BA196-L000125](../../agents/aspect_planning.py#L125) | 125 | `"        seen.add(_normalize_key(topic))"` | — |
| [SRC-01273BA196-L000126](../../agents/aspect_planning.py#L126) | 126 | `"    for aspect in aspects:"` | — |
| [SRC-01273BA196-L000127](../../agents/aspect_planning.py#L127) | 127 | `"        aspect_clean = _normalize_space(str(aspect))"` | — |
| [SRC-01273BA196-L000128](../../agents/aspect_planning.py#L128) | 128 | `"        if not aspect_clean:"` | — |
| [SRC-01273BA196-L000129](../../agents/aspect_planning.py#L129) | 129 | `"            continue"` | — |
| [SRC-01273BA196-L000130](../../agents/aspect_planning.py#L130) | 130 | `"        candidate = _normalize_space(f\"{topic} {aspect_clean}\" if topic else aspect_clean)[:240]"` | — |
| [SRC-01273BA196-L000131](../../agents/aspect_planning.py#L131) | 131 | `"        key = _normalize_key(candidate)"` | — |
| [SRC-01273BA196-L000132](../../agents/aspect_planning.py#L132) | 132 | `"        if key and key not in seen:"` | — |
| [SRC-01273BA196-L000133](../../agents/aspect_planning.py#L133) | 133 | `"            seen.add(key)"` | — |
| [SRC-01273BA196-L000134](../../agents/aspect_planning.py#L134) | 134 | `"            queries.append(candidate)"` | — |
| [SRC-01273BA196-L000135](../../agents/aspect_planning.py#L135) | 135 | `"        if len(queries) >= max(1, min(int(limit), MAX_PLAN_QUERIES)):"` | — |
| [SRC-01273BA196-L000136](../../agents/aspect_planning.py#L136) | 136 | `"            break"` | — |
| [SRC-01273BA196-L000137](../../agents/aspect_planning.py#L137) | 137 | `"    return queries"` | — |
| [SRC-01273BA196-L000138](../../agents/aspect_planning.py#L138) | 138 | `""` | — |
| [SRC-01273BA196-L000139](../../agents/aspect_planning.py#L139) | 139 | `""` | — |
| [SRC-01273BA196-L000140](../../agents/aspect_planning.py#L140) | 140 | `"def augment_plan_with_aspects("` | — |
| [SRC-01273BA196-L000141](../../agents/aspect_planning.py#L141) | 141 | `"    plan: dict[str, Any], question: str, topic_query: str, *, compact_fn: Any = None,"` | — |
| [SRC-01273BA196-L000142](../../agents/aspect_planning.py#L142) | 142 | `") -> dict[str, Any]:"` | — |
| [SRC-01273BA196-L000143](../../agents/aspect_planning.py#L143) | 143 | `"    out = dict(plan or {})"` | — |
| [SRC-01273BA196-L000144](../../agents/aspect_planning.py#L144) | 144 | `"    aspects = extract_aspects(question)"` | — |
| [SRC-01273BA196-L000145](../../agents/aspect_planning.py#L145) | 145 | `"    out[\"aspects\"] = aspects"` | — |
| [SRC-01273BA196-L000146](../../agents/aspect_planning.py#L146) | 146 | `"    base_queries = [str(q).strip() for q in (out.get(\"queries\") or []) if isinstance(q, str) and q.strip()]"` | — |
| [SRC-01273BA196-L000147](../../agents/aspect_planning.py#L147) | 147 | `"    topic = topic_query or (base_queries[0] if base_queries else \"\")"` | — |
| [SRC-01273BA196-L000148](../../agents/aspect_planning.py#L148) | 148 | `"    if compact_fn is not None:"` | — |
| [SRC-01273BA196-L000149](../../agents/aspect_planning.py#L149) | 149 | `"        try:"` | — |
| [SRC-01273BA196-L000150](../../agents/aspect_planning.py#L150) | 150 | `"            topic = compact_fn(topic) or topic"` | — |
| [SRC-01273BA196-L000151](../../agents/aspect_planning.py#L151) | 151 | `"        except (TypeError, ValueError):"` | — |
| [SRC-01273BA196-L000152](../../agents/aspect_planning.py#L152) | 152 | `"            pass"` | — |
| [SRC-01273BA196-L000153](../../agents/aspect_planning.py#L153) | 153 | `"    aspect_queries = build_aspect_queries(topic, aspects)"` | — |
| [SRC-01273BA196-L000154](../../agents/aspect_planning.py#L154) | 154 | `"    if compact_fn is not None:"` | — |
| [SRC-01273BA196-L000155](../../agents/aspect_planning.py#L155) | 155 | `"        compacted: list[str] = []"` | — |
| [SRC-01273BA196-L000156](../../agents/aspect_planning.py#L156) | 156 | `"        seen: set[str] = set()"` | — |
| [SRC-01273BA196-L000157](../../agents/aspect_planning.py#L157) | 157 | `"        for q in aspect_queries + base_queries:"` | — |
| [SRC-01273BA196-L000158](../../agents/aspect_planning.py#L158) | 158 | `"            try:"` | — |
| [SRC-01273BA196-L000159](../../agents/aspect_planning.py#L159) | 159 | `"                cq = compact_fn(q)"` | — |
| [SRC-01273BA196-L000160](../../agents/aspect_planning.py#L160) | 160 | `"            except (TypeError, ValueError):"` | — |
| [SRC-01273BA196-L000161](../../agents/aspect_planning.py#L161) | 161 | `"                cq = q"` | — |
| [SRC-01273BA196-L000162](../../agents/aspect_planning.py#L162) | 162 | `"            if not cq:"` | — |
| [SRC-01273BA196-L000163](../../agents/aspect_planning.py#L163) | 163 | `"                continue"` | — |
| [SRC-01273BA196-L000164](../../agents/aspect_planning.py#L164) | 164 | `"            key = _normalize_key(cq)"` | — |
| [SRC-01273BA196-L000165](../../agents/aspect_planning.py#L165) | 165 | `"            if key not in seen:"` | — |
| [SRC-01273BA196-L000166](../../agents/aspect_planning.py#L166) | 166 | `"                seen.add(key)"` | — |
| [SRC-01273BA196-L000167](../../agents/aspect_planning.py#L167) | 167 | `"                compacted.append(cq)"` | — |
| [SRC-01273BA196-L000168](../../agents/aspect_planning.py#L168) | 168 | `"            if len(compacted) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-01273BA196-L000169](../../agents/aspect_planning.py#L169) | 169 | `"                break"` | — |
| [SRC-01273BA196-L000170](../../agents/aspect_planning.py#L170) | 170 | `"        out[\"queries\"] = compacted"` | — |
| [SRC-01273BA196-L000171](../../agents/aspect_planning.py#L171) | 171 | `"    else:"` | — |
| [SRC-01273BA196-L000172](../../agents/aspect_planning.py#L172) | 172 | `"        merged: list[str] = []"` | — |
| [SRC-01273BA196-L000173](../../agents/aspect_planning.py#L173) | 173 | `"        seen_m: set[str] = set()"` | — |
| [SRC-01273BA196-L000174](../../agents/aspect_planning.py#L174) | 174 | `"        for q in aspect_queries + base_queries:"` | — |
| [SRC-01273BA196-L000175](../../agents/aspect_planning.py#L175) | 175 | `"            key = _normalize_key(q)"` | — |
| [SRC-01273BA196-L000176](../../agents/aspect_planning.py#L176) | 176 | `"            if key and key not in seen_m:"` | — |
| [SRC-01273BA196-L000177](../../agents/aspect_planning.py#L177) | 177 | `"                seen_m.add(key)"` | — |
| [SRC-01273BA196-L000178](../../agents/aspect_planning.py#L178) | 178 | `"                merged.append(q)"` | — |
| [SRC-01273BA196-L000179](../../agents/aspect_planning.py#L179) | 179 | `"            if len(merged) >= MAX_PLAN_QUERIES:"` | — |
| [SRC-01273BA196-L000180](../../agents/aspect_planning.py#L180) | 180 | `"                break"` | — |
| [SRC-01273BA196-L000181](../../agents/aspect_planning.py#L181) | 181 | `"        out[\"queries\"] = merged"` | — |
| [SRC-01273BA196-L000182](../../agents/aspect_planning.py#L182) | 182 | `"    out[\"aspect_queries\"] = list(out.get(\"queries\") or [])"` | — |
| [SRC-01273BA196-L000183](../../agents/aspect_planning.py#L183) | 183 | `"    return out"` | — |
| [SRC-01273BA196-L000184](../../agents/aspect_planning.py#L184) | 184 | `""` | — |
| [SRC-01273BA196-L000185](../../agents/aspect_planning.py#L185) | 185 | `""` | — |
| [SRC-01273BA196-L000186](../../agents/aspect_planning.py#L186) | 186 | `"def _source_text(source: dict[str, Any]) -> str:"` | — |
| [SRC-01273BA196-L000187](../../agents/aspect_planning.py#L187) | 187 | `"    return \" \".join(str(source.get(key) or \"\") for key in (\"title\", \"snippet\", \"page_text\"))"` | — |
| [SRC-01273BA196-L000188](../../agents/aspect_planning.py#L188) | 188 | `""` | — |
| [SRC-01273BA196-L000189](../../agents/aspect_planning.py#L189) | 189 | `""` | — |
| [SRC-01273BA196-L000190](../../agents/aspect_planning.py#L190) | 190 | `"def build_evidence_ledger(aspects: list[str], sources: list[dict[str, Any]], *, min_term_len: int = 2) -> dict[str, Any]:"` | — |
| [SRC-01273BA196-L000191](../../agents/aspect_planning.py#L191) | 191 | `"    ledger: dict[str, Any] = {\"aspects\": [], \"covered\": [], \"missing\": [], \"by_aspect\": {}}"` | — |
| [SRC-01273BA196-L000192](../../agents/aspect_planning.py#L192) | 192 | `"    if not aspects:"` | — |
| [SRC-01273BA196-L000193](../../agents/aspect_planning.py#L193) | 193 | `"        ledger[\"note\"] = \"no_explicit_aspects\""` | — |
| [SRC-01273BA196-L000194](../../agents/aspect_planning.py#L194) | 194 | `"        return ledger"` | — |
| [SRC-01273BA196-L000195](../../agents/aspect_planning.py#L195) | 195 | `"    for aspect in aspects:"` | — |
| [SRC-01273BA196-L000196](../../agents/aspect_planning.py#L196) | 196 | `"        tokens = [t for t in re.findall(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", _normalize_key(aspect)) if len(t) >= min_term_len]"` | — |
| [SRC-01273BA196-L000197](../../agents/aspect_planning.py#L197) | 197 | `"        matches: list[dict[str, Any]] = []"` | — |
| [SRC-01273BA196-L000198](../../agents/aspect_planning.py#L198) | 198 | `"        for source in sources or []:"` | — |
| [SRC-01273BA196-L000199](../../agents/aspect_planning.py#L199) | 199 | `"            if not isinstance(source, dict):"` | — |
| [SRC-01273BA196-L000200](../../agents/aspect_planning.py#L200) | 200 | `"                continue"` | — |
| [SRC-01273BA196-L000201](../../agents/aspect_planning.py#L201) | 201 | `"            hay = _normalize_key(_source_text(source))"` | — |
| [SRC-01273BA196-L000202](../../agents/aspect_planning.py#L202) | 202 | `"            if not hay:"` | — |
| [SRC-01273BA196-L000203](../../agents/aspect_planning.py#L203) | 203 | `"                continue"` | — |
| [SRC-01273BA196-L000204](../../agents/aspect_planning.py#L204) | 204 | `"            hit = sum(1 for t in tokens if t in hay)"` | — |
| [SRC-01273BA196-L000205](../../agents/aspect_planning.py#L205) | 205 | `"            if tokens and hit >= max(1, (len(tokens) + 1) // 2):"` | — |
| [SRC-01273BA196-L000206](../../agents/aspect_planning.py#L206) | 206 | `"                evidence_type = \"page_text\" if source.get(\"page_text\") else \"snippet\" if source.get(\"snippet\") else \"title\""` | — |
| [SRC-01273BA196-L000207](../../agents/aspect_planning.py#L207) | 207 | `"                matches.append({"` | — |
| [SRC-01273BA196-L000208](../../agents/aspect_planning.py#L208) | 208 | `"                    \"url\": source.get(\"url\", \"\"),"` | — |
| [SRC-01273BA196-L000209](../../agents/aspect_planning.py#L209) | 209 | `"                    \"title\": source.get(\"title\", \"\"),"` | — |
| [SRC-01273BA196-L000210](../../agents/aspect_planning.py#L210) | 210 | `"                    \"provider\": source.get(\"provider\") or (source.get(\"providers\") or [\"unknown\"])[0],"` | — |
| [SRC-01273BA196-L000211](../../agents/aspect_planning.py#L211) | 211 | `"                    \"evidence_type\": evidence_type,"` | — |
| [SRC-01273BA196-L000212](../../agents/aspect_planning.py#L212) | 212 | `"                    \"lexical_hits\": hit,"` | — |
| [SRC-01273BA196-L000213](../../agents/aspect_planning.py#L213) | 213 | `"                    \"search_query\": source.get(\"search_query\") or ((source.get(\"queries\") or [\"\"])[0] if source.get(\"queries\") else \"\"),"` | — |
| [SRC-01273BA196-L000214](../../agents/aspect_planning.py#L214) | 214 | `"                })"` | — |
| [SRC-01273BA196-L000215](../../agents/aspect_planning.py#L215) | 215 | `"        entry = {\"aspect\": aspect, \"candidate_count\": len(matches), \"candidates\": matches[:5], \"has_lexical_candidate\": bool(matches)}"` | — |
| [SRC-01273BA196-L000216](../../agents/aspect_planning.py#L216) | 216 | `"        ledger[\"by_aspect\"][aspect] = entry"` | — |
| [SRC-01273BA196-L000217](../../agents/aspect_planning.py#L217) | 217 | `"        ledger[\"aspects\"].append(aspect)"` | — |
| [SRC-01273BA196-L000218](../../agents/aspect_planning.py#L218) | 218 | `"        if matches:"` | — |
| [SRC-01273BA196-L000219](../../agents/aspect_planning.py#L219) | 219 | `"            ledger[\"covered\"].append(aspect)"` | — |
| [SRC-01273BA196-L000220](../../agents/aspect_planning.py#L220) | 220 | `"        else:"` | — |
| [SRC-01273BA196-L000221](../../agents/aspect_planning.py#L221) | 221 | `"            ledger[\"missing\"].append(aspect)"` | — |
| [SRC-01273BA196-L000222](../../agents/aspect_planning.py#L222) | 222 | `"    ledger[\"coverage_ratio\"] = round(len(ledger[\"covered\"]) / max(1, len(aspects)), 3)"` | — |
| [SRC-01273BA196-L000223](../../agents/aspect_planning.py#L223) | 223 | `"    return ledger"` | — |
| [SRC-01273BA196-L000224](../../agents/aspect_planning.py#L224) | 224 | `""` | — |
| [SRC-01273BA196-L000225](../../agents/aspect_planning.py#L225) | 225 | `""` | — |
| [SRC-01273BA196-L000226](../../agents/aspect_planning.py#L226) | 226 | `"def repair_queries_for_missing_aspects("` | — |
| [SRC-01273BA196-L000227](../../agents/aspect_planning.py#L227) | 227 | `"    topic_query: str, missing_aspects: list[str], *, limit: int = 3, compact_fn: Any = None,"` | — |
| [SRC-01273BA196-L000228](../../agents/aspect_planning.py#L228) | 228 | `") -> list[str]:"` | — |
| [SRC-01273BA196-L000229](../../agents/aspect_planning.py#L229) | 229 | `"    topic = _normalize_space(topic_query)"` | — |
| [SRC-01273BA196-L000230](../../agents/aspect_planning.py#L230) | 230 | `"    out: list[str] = []"` | — |
| [SRC-01273BA196-L000231](../../agents/aspect_planning.py#L231) | 231 | `"    seen: set[str] = set()"` | — |
| [SRC-01273BA196-L000232](../../agents/aspect_planning.py#L232) | 232 | `"    for aspect in missing_aspects:"` | — |
| [SRC-01273BA196-L000233](../../agents/aspect_planning.py#L233) | 233 | `"        aspect_clean = _normalize_space(str(aspect))"` | — |
| [SRC-01273BA196-L000234](../../agents/aspect_planning.py#L234) | 234 | `"        if not aspect_clean:"` | — |
| [SRC-01273BA196-L000235](../../agents/aspect_planning.py#L235) | 235 | `"            continue"` | — |
| [SRC-01273BA196-L000236](../../agents/aspect_planning.py#L236) | 236 | `"        raw = f\"{topic} {aspect_clean}\".strip() if topic else aspect_clean"` | — |
| [SRC-01273BA196-L000237](../../agents/aspect_planning.py#L237) | 237 | `"        if compact_fn is not None:"` | — |
| [SRC-01273BA196-L000238](../../agents/aspect_planning.py#L238) | 238 | `"            try:"` | — |
| [SRC-01273BA196-L000239](../../agents/aspect_planning.py#L239) | 239 | `"                raw = compact_fn(raw) or raw"` | — |
| [SRC-01273BA196-L000240](../../agents/aspect_planning.py#L240) | 240 | `"            except (TypeError, ValueError):"` | — |
| [SRC-01273BA196-L000241](../../agents/aspect_planning.py#L241) | 241 | `"                pass"` | — |
| [SRC-01273BA196-L000242](../../agents/aspect_planning.py#L242) | 242 | `"        raw = _normalize_space(raw)[:240]"` | — |
| [SRC-01273BA196-L000243](../../agents/aspect_planning.py#L243) | 243 | `"        key = _normalize_key(raw)"` | — |
| [SRC-01273BA196-L000244](../../agents/aspect_planning.py#L244) | 244 | `"        if raw and key not in seen:"` | — |
| [SRC-01273BA196-L000245](../../agents/aspect_planning.py#L245) | 245 | `"            seen.add(key)"` | — |
| [SRC-01273BA196-L000246](../../agents/aspect_planning.py#L246) | 246 | `"            out.append(raw)"` | — |
| [SRC-01273BA196-L000247](../../agents/aspect_planning.py#L247) | 247 | `"        if len(out) >= max(1, min(int(limit), 3)):"` | — |
| [SRC-01273BA196-L000248](../../agents/aspect_planning.py#L248) | 248 | `"            break"` | — |
| [SRC-01273BA196-L000249](../../agents/aspect_planning.py#L249) | 249 | `"    return out"` | — |
| [SRC-01273BA196-L000250](../../agents/aspect_planning.py#L250) | 250 | `""` | — |
| [SRC-01273BA196-L000251](../../agents/aspect_planning.py#L251) | 251 | `""` | — |
| [SRC-01273BA196-L000252](../../agents/aspect_planning.py#L252) | 252 | `"def arabic_aspect_diagnostics(ledger: dict[str, Any]) -> list[str]:"` | — |
| [SRC-01273BA196-L000253](../../agents/aspect_planning.py#L253) | 253 | `"    lines: list[str] = []"` | — |
| [SRC-01273BA196-L000254](../../agents/aspect_planning.py#L254) | 254 | `"    if not ledger or ledger.get(\"note\") == \"no_explicit_aspects\":"` | — |
| [SRC-01273BA196-L000255](../../agents/aspect_planning.py#L255) | 255 | `"        return lines"` | — |
| [SRC-01273BA196-L000256](../../agents/aspect_planning.py#L256) | 256 | `"    covered = ledger.get(\"covered\") or []"` | — |
| [SRC-01273BA196-L000257](../../agents/aspect_planning.py#L257) | 257 | `"    missing = ledger.get(\"missing\") or []"` | — |
| [SRC-01273BA196-L000258](../../agents/aspect_planning.py#L258) | 258 | `"    if covered:"` | — |
| [SRC-01273BA196-L000259](../../agents/aspect_planning.py#L259) | 259 | `"        lines.append(\"محاور وُجد لها مرشح نصي واحد على الأقل: \" + \"، \".join(str(x) for x in covered))"` | — |
| [SRC-01273BA196-L000260](../../agents/aspect_planning.py#L260) | 260 | `"    if missing:"` | — |
| [SRC-01273BA196-L000261](../../agents/aspect_planning.py#L261) | 261 | `"        lines.append("` | — |
| [SRC-01273BA196-L000262](../../agents/aspect_planning.py#L262) | 262 | `"            \"محاور بلا مرشح نصي كافٍ في النتائج الحالية: \""` | — |
| [SRC-01273BA196-L000263](../../agents/aspect_planning.py#L263) | 263 | `"            + \"، \".join(str(x) for x in missing)"` | — |
| [SRC-01273BA196-L000264](../../agents/aspect_planning.py#L264) | 264 | `"            + \". هذا لا ينفي وجود معلومات خارج النتائج المجلوبة.\""` | — |
| [SRC-01273BA196-L000265](../../agents/aspect_planning.py#L265) | 265 | `"        )"` | — |
| [SRC-01273BA196-L000266](../../agents/aspect_planning.py#L266) | 266 | `"    ratio = ledger.get(\"coverage_ratio\")"` | — |
| [SRC-01273BA196-L000267](../../agents/aspect_planning.py#L267) | 267 | `"    if isinstance(ratio, (int, float)):"` | — |
| [SRC-01273BA196-L000268](../../agents/aspect_planning.py#L268) | 268 | `"        lines.append(f\"نسبة تغطية المحاور لفظيًا (تقريبية): {int(ratio * 100)}٪.\")"` | — |
| [SRC-01273BA196-L000269](../../agents/aspect_planning.py#L269) | 269 | `"    lines.append(\"تنبيه: وجود مقتطف يطابق كلمات المحور لا يثبت صحة الادعاء.\")"` | — |
| [SRC-01273BA196-L000270](../../agents/aspect_planning.py#L270) | 270 | `"    return lines"` | — |
## الوكيل والمنطق

### FILE-7D6FC391EC — [agents/claim_evidence.py](../../agents/claim_evidence.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-7D6FC391EC-L000001](../../agents/claim_evidence.py#L1) | 1 | `"\"\"\"Sentence-level source tracing for Omarai."` | — |
| [SRC-7D6FC391EC-L000002](../../agents/claim_evidence.py#L2) | 2 | `""` | — |
| [SRC-7D6FC391EC-L000003](../../agents/claim_evidence.py#L3) | 3 | `"This maps citation markers to the exact bounded source list sent to the model."` | — |
| [SRC-7D6FC391EC-L000004](../../agents/claim_evidence.py#L4) | 4 | `"It does not prove truth, citation entailment, or semantic completeness."` | — |
| [SRC-7D6FC391EC-L000005](../../agents/claim_evidence.py#L5) | 5 | `"\"\"\""` | — |
| [SRC-7D6FC391EC-L000006](../../agents/claim_evidence.py#L6) | 6 | `"from __future__ import annotations"` | — |
| [SRC-7D6FC391EC-L000007](../../agents/claim_evidence.py#L7) | 7 | `""` | — |
| [SRC-7D6FC391EC-L000008](../../agents/claim_evidence.py#L8) | 8 | `"import re"` | — |
| [SRC-7D6FC391EC-L000009](../../agents/claim_evidence.py#L9) | 9 | `"from typing import Any"` | — |
| [SRC-7D6FC391EC-L000010](../../agents/claim_evidence.py#L10) | 10 | `""` | — |
| [SRC-7D6FC391EC-L000011](../../agents/claim_evidence.py#L11) | 11 | `"_CITATION = re.compile(r\"\\[(?:المصدر\|source)\\s+(\\d+)\\]\", re.IGNORECASE)"` | — |
| [SRC-7D6FC391EC-L000012](../../agents/claim_evidence.py#L12) | 12 | `"_SENTENCE_SPLIT = re.compile(r\"(?<=[.!?؟])\\s+\|\\n+\")"` | — |
| [SRC-7D6FC391EC-L000013](../../agents/claim_evidence.py#L13) | 13 | `""` | — |
| [SRC-7D6FC391EC-L000014](../../agents/claim_evidence.py#L14) | 14 | `""` | — |
| [SRC-7D6FC391EC-L000015](../../agents/claim_evidence.py#L15) | 15 | `"def _evidence_basis(source: dict[str, Any]) -> str:"` | — |
| [SRC-7D6FC391EC-L000016](../../agents/claim_evidence.py#L16) | 16 | `"    if bool(source.get(\"page_fetched\")) and str(source.get(\"page_text\") or \"\").strip():"` | — |
| [SRC-7D6FC391EC-L000017](../../agents/claim_evidence.py#L17) | 17 | `"        return \"extracted_page_text\""` | — |
| [SRC-7D6FC391EC-L000018](../../agents/claim_evidence.py#L18) | 18 | `"    if str(source.get(\"snippet\") or \"\").strip():"` | — |
| [SRC-7D6FC391EC-L000019](../../agents/claim_evidence.py#L19) | 19 | `"        return \"search_snippet\""` | — |
| [SRC-7D6FC391EC-L000020](../../agents/claim_evidence.py#L20) | 20 | `"    if str(source.get(\"title\") or \"\").strip():"` | — |
| [SRC-7D6FC391EC-L000021](../../agents/claim_evidence.py#L21) | 21 | `"        return \"title_only\""` | — |
| [SRC-7D6FC391EC-L000022](../../agents/claim_evidence.py#L22) | 22 | `"    return \"no_readable_evidence\""` | — |
| [SRC-7D6FC391EC-L000023](../../agents/claim_evidence.py#L23) | 23 | `""` | — |
| [SRC-7D6FC391EC-L000024](../../agents/claim_evidence.py#L24) | 24 | `""` | — |
| [SRC-7D6FC391EC-L000025](../../agents/claim_evidence.py#L25) | 25 | `"def build_claim_evidence_ledger("` | — |
| [SRC-7D6FC391EC-L000026](../../agents/claim_evidence.py#L26) | 26 | `"    answer: str,"` | — |
| [SRC-7D6FC391EC-L000027](../../agents/claim_evidence.py#L27) | 27 | `"    sources: list[dict[str, Any]] \| None,"` | — |
| [SRC-7D6FC391EC-L000028](../../agents/claim_evidence.py#L28) | 28 | `"    answer_integrity: dict[str, Any] \| None = None,"` | — |
| [SRC-7D6FC391EC-L000029](../../agents/claim_evidence.py#L29) | 29 | `"    *,"` | — |
| [SRC-7D6FC391EC-L000030](../../agents/claim_evidence.py#L30) | 30 | `"    max_segments: int = 40,"` | — |
| [SRC-7D6FC391EC-L000031](../../agents/claim_evidence.py#L31) | 31 | `"    max_citable_sources: int = 12,"` | — |
| [SRC-7D6FC391EC-L000032](../../agents/claim_evidence.py#L32) | 32 | `") -> dict[str, Any]:"` | — |
| [SRC-7D6FC391EC-L000033](../../agents/claim_evidence.py#L33) | 33 | `"    \"\"\"Return bounded sentence candidates with validated source-index traceability.\"\"\""` | — |
| [SRC-7D6FC391EC-L000034](../../agents/claim_evidence.py#L34) | 34 | `"    safe_answer = str(answer or \"\")[:24000]"` | — |
| [SRC-7D6FC391EC-L000035](../../agents/claim_evidence.py#L35) | 35 | `"    safe_sources = ["` | — |
| [SRC-7D6FC391EC-L000036](../../agents/claim_evidence.py#L36) | 36 | `"        source for source in (sources or []) if isinstance(source, dict)"` | — |
| [SRC-7D6FC391EC-L000037](../../agents/claim_evidence.py#L37) | 37 | `"    ][:max(0, min(int(max_citable_sources), 40))]"` | — |
| [SRC-7D6FC391EC-L000038](../../agents/claim_evidence.py#L38) | 38 | `"    segments = ["` | — |
| [SRC-7D6FC391EC-L000039](../../agents/claim_evidence.py#L39) | 39 | `"        part.strip()"` | — |
| [SRC-7D6FC391EC-L000040](../../agents/claim_evidence.py#L40) | 40 | `"        for part in _SENTENCE_SPLIT.split(safe_answer)"` | — |
| [SRC-7D6FC391EC-L000041](../../agents/claim_evidence.py#L41) | 41 | `"        if part and part.strip()"` | — |
| [SRC-7D6FC391EC-L000042](../../agents/claim_evidence.py#L42) | 42 | `"    ]"` | — |
| [SRC-7D6FC391EC-L000043](../../agents/claim_evidence.py#L43) | 43 | `"    truncated = len(segments) > max_segments"` | — |
| [SRC-7D6FC391EC-L000044](../../agents/claim_evidence.py#L44) | 44 | `"    segments = segments[:max(0, min(int(max_segments), 100))]"` | — |
| [SRC-7D6FC391EC-L000045](../../agents/claim_evidence.py#L45) | 45 | `"    integrity = answer_integrity if isinstance(answer_integrity, dict) else {}"` | — |
| [SRC-7D6FC391EC-L000046](../../agents/claim_evidence.py#L46) | 46 | `"    alignments = integrity.get(\"citation_lexical_alignment\")"` | — |
| [SRC-7D6FC391EC-L000047](../../agents/claim_evidence.py#L47) | 47 | `"    alignment_by_sentence = {"` | — |
| [SRC-7D6FC391EC-L000048](../../agents/claim_evidence.py#L48) | 48 | `"        int(item[\"sentence_number\"]): item"` | — |
| [SRC-7D6FC391EC-L000049](../../agents/claim_evidence.py#L49) | 49 | `"        for item in alignments"` | — |
| [SRC-7D6FC391EC-L000050](../../agents/claim_evidence.py#L50) | 50 | `"        if isinstance(item, dict) and isinstance(item.get(\"sentence_number\"), int)"` | — |
| [SRC-7D6FC391EC-L000051](../../agents/claim_evidence.py#L51) | 51 | `"    } if isinstance(alignments, list) else {}"` | — |
| [SRC-7D6FC391EC-L000052](../../agents/claim_evidence.py#L52) | 52 | `""` | — |
| [SRC-7D6FC391EC-L000053](../../agents/claim_evidence.py#L53) | 53 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-7D6FC391EC-L000054](../../agents/claim_evidence.py#L54) | 54 | `"    valid_refs = invalid_refs = cited = uncited = readable_cited = 0"` | — |
| [SRC-7D6FC391EC-L000055](../../agents/claim_evidence.py#L55) | 55 | `"    lexical_signals = weak_signals = 0"` | — |
| [SRC-7D6FC391EC-L000056](../../agents/claim_evidence.py#L56) | 56 | `""` | — |
| [SRC-7D6FC391EC-L000057](../../agents/claim_evidence.py#L57) | 57 | `"    for number, segment in enumerate(segments, 1):"` | — |
| [SRC-7D6FC391EC-L000058](../../agents/claim_evidence.py#L58) | 58 | `"        indexes = list(dict.fromkeys(int(m.group(1)) for m in _CITATION.finditer(segment)))[:8]"` | — |
| [SRC-7D6FC391EC-L000059](../../agents/claim_evidence.py#L59) | 59 | `"        refs: list[dict[str, Any]] = []"` | — |
| [SRC-7D6FC391EC-L000060](../../agents/claim_evidence.py#L60) | 60 | `"        has_readable = False"` | — |
| [SRC-7D6FC391EC-L000061](../../agents/claim_evidence.py#L61) | 61 | `"        for index in indexes:"` | — |
| [SRC-7D6FC391EC-L000062](../../agents/claim_evidence.py#L62) | 62 | `"            if index < 1 or index > len(safe_sources):"` | — |
| [SRC-7D6FC391EC-L000063](../../agents/claim_evidence.py#L63) | 63 | `"                invalid_refs += 1"` | — |
| [SRC-7D6FC391EC-L000064](../../agents/claim_evidence.py#L64) | 64 | `"                refs.append({"` | — |
| [SRC-7D6FC391EC-L000065](../../agents/claim_evidence.py#L65) | 65 | `"                    \"source_index\": index, \"reference_status\": \"index_out_of_citable_range\","` | — |
| [SRC-7D6FC391EC-L000066](../../agents/claim_evidence.py#L66) | 66 | `"                    \"title\": \"\", \"url\": \"\", \"evidence_basis\": \"unavailable\","` | — |
| [SRC-7D6FC391EC-L000067](../../agents/claim_evidence.py#L67) | 67 | `"                })"` | — |
| [SRC-7D6FC391EC-L000068](../../agents/claim_evidence.py#L68) | 68 | `"                continue"` | — |
| [SRC-7D6FC391EC-L000069](../../agents/claim_evidence.py#L69) | 69 | `"            source = safe_sources[index - 1]"` | — |
| [SRC-7D6FC391EC-L000070](../../agents/claim_evidence.py#L70) | 70 | `"            basis = _evidence_basis(source)"` | — |
| [SRC-7D6FC391EC-L000071](../../agents/claim_evidence.py#L71) | 71 | `"            valid_refs += 1"` | — |
| [SRC-7D6FC391EC-L000072](../../agents/claim_evidence.py#L72) | 72 | `"            # Titles are useful metadata, but not readable source text for checking entailment."` | — |
| [SRC-7D6FC391EC-L000073](../../agents/claim_evidence.py#L73) | 73 | `"            has_readable = has_readable or basis in {\"extracted_page_text\", \"search_snippet\"}"` | — |
| [SRC-7D6FC391EC-L000074](../../agents/claim_evidence.py#L74) | 74 | `"            refs.append({"` | — |
| [SRC-7D6FC391EC-L000075](../../agents/claim_evidence.py#L75) | 75 | `"                \"source_index\": index,"` | — |
| [SRC-7D6FC391EC-L000076](../../agents/claim_evidence.py#L76) | 76 | `"                \"reference_status\": ("` | — |
| [SRC-7D6FC391EC-L000077](../../agents/claim_evidence.py#L77) | 77 | `"                    \"valid_index_with_readable_evidence\""` | — |
| [SRC-7D6FC391EC-L000078](../../agents/claim_evidence.py#L78) | 78 | `"                    if basis in {\"extracted_page_text\", \"search_snippet\"}"` | — |
| [SRC-7D6FC391EC-L000079](../../agents/claim_evidence.py#L79) | 79 | `"                    else \"valid_index_without_readable_evidence\""` | — |
| [SRC-7D6FC391EC-L000080](../../agents/claim_evidence.py#L80) | 80 | `"                ),"` | — |
| [SRC-7D6FC391EC-L000081](../../agents/claim_evidence.py#L81) | 81 | `"                \"title\": str(source.get(\"title\") or \"\")[:240],"` | — |
| [SRC-7D6FC391EC-L000082](../../agents/claim_evidence.py#L82) | 82 | `"                \"url\": str(source.get(\"url\") or \"\")[:2048],"` | — |
| [SRC-7D6FC391EC-L000083](../../agents/claim_evidence.py#L83) | 83 | `"                \"provider\": str(source.get(\"provider\") or \"\")[:80],"` | — |
| [SRC-7D6FC391EC-L000084](../../agents/claim_evidence.py#L84) | 84 | `"                \"evidence_basis\": basis,"` | — |
| [SRC-7D6FC391EC-L000085](../../agents/claim_evidence.py#L85) | 85 | `"            })"` | — |
| [SRC-7D6FC391EC-L000086](../../agents/claim_evidence.py#L86) | 86 | `""` | — |
| [SRC-7D6FC391EC-L000087](../../agents/claim_evidence.py#L87) | 87 | `"        cited += bool(indexes)"` | — |
| [SRC-7D6FC391EC-L000088](../../agents/claim_evidence.py#L88) | 88 | `"        uncited += not bool(indexes)"` | — |
| [SRC-7D6FC391EC-L000089](../../agents/claim_evidence.py#L89) | 89 | `"        readable_cited += bool(indexes) and has_readable"` | — |
| [SRC-7D6FC391EC-L000090](../../agents/claim_evidence.py#L90) | 90 | `"        alignment = alignment_by_sentence.get(number, {})"` | — |
| [SRC-7D6FC391EC-L000091](../../agents/claim_evidence.py#L91) | 91 | `"        lexical_status = str(alignment.get(\"status\") or \"not_assessed_no_citation_alignment\")"` | — |
| [SRC-7D6FC391EC-L000092](../../agents/claim_evidence.py#L92) | 92 | `"        lexical_signals += lexical_status == \"lexical_overlap_signal_found\""` | — |
| [SRC-7D6FC391EC-L000093](../../agents/claim_evidence.py#L93) | 93 | `"        weak_signals += lexical_status == \"weak_lexical_overlap\""` | — |
| [SRC-7D6FC391EC-L000094](../../agents/claim_evidence.py#L94) | 94 | `"        if any(ref[\"reference_status\"] == \"index_out_of_citable_range\" for ref in refs):"` | — |
| [SRC-7D6FC391EC-L000095](../../agents/claim_evidence.py#L95) | 95 | `"            status = \"citation_index_out_of_range\""` | — |
| [SRC-7D6FC391EC-L000096](../../agents/claim_evidence.py#L96) | 96 | `"        elif indexes and not has_readable:"` | — |
| [SRC-7D6FC391EC-L000097](../../agents/claim_evidence.py#L97) | 97 | `"            status = \"valid_index_without_readable_evidence\""` | — |
| [SRC-7D6FC391EC-L000098](../../agents/claim_evidence.py#L98) | 98 | `"        elif indexes:"` | — |
| [SRC-7D6FC391EC-L000099](../../agents/claim_evidence.py#L99) | 99 | `"            status = \"cited_source_attached\""` | — |
| [SRC-7D6FC391EC-L000100](../../agents/claim_evidence.py#L100) | 100 | `"        else:"` | — |
| [SRC-7D6FC391EC-L000101](../../agents/claim_evidence.py#L101) | 101 | `"            status = \"no_citation_marker\""` | — |
| [SRC-7D6FC391EC-L000102](../../agents/claim_evidence.py#L102) | 102 | `""` | — |
| [SRC-7D6FC391EC-L000103](../../agents/claim_evidence.py#L103) | 103 | `"        rows.append({"` | — |
| [SRC-7D6FC391EC-L000104](../../agents/claim_evidence.py#L104) | 104 | `"            \"segment_id\": f\"S{number:03d}\","` | — |
| [SRC-7D6FC391EC-L000105](../../agents/claim_evidence.py#L105) | 105 | `"            \"segment_number\": number,"` | — |
| [SRC-7D6FC391EC-L000106](../../agents/claim_evidence.py#L106) | 106 | `"            \"unit_kind\": \"sentence_candidate_not_semantically_classified\","` | — |
| [SRC-7D6FC391EC-L000107](../../agents/claim_evidence.py#L107) | 107 | `"            \"text\": segment[:1200],"` | — |
| [SRC-7D6FC391EC-L000108](../../agents/claim_evidence.py#L108) | 108 | `"            \"citation_indexes\": indexes,"` | — |
| [SRC-7D6FC391EC-L000109](../../agents/claim_evidence.py#L109) | 109 | `"            \"citation_status\": status,"` | — |
| [SRC-7D6FC391EC-L000110](../../agents/claim_evidence.py#L110) | 110 | `"            \"lexical_audit_status\": lexical_status,"` | — |
| [SRC-7D6FC391EC-L000111](../../agents/claim_evidence.py#L111) | 111 | `"            \"sources\": refs,"` | — |
| [SRC-7D6FC391EC-L000112](../../agents/claim_evidence.py#L112) | 112 | `"        })"` | — |
| [SRC-7D6FC391EC-L000113](../../agents/claim_evidence.py#L113) | 113 | `""` | — |
| [SRC-7D6FC391EC-L000114](../../agents/claim_evidence.py#L114) | 114 | `"    total = len(rows)"` | — |
| [SRC-7D6FC391EC-L000115](../../agents/claim_evidence.py#L115) | 115 | `"    return {"` | — |
| [SRC-7D6FC391EC-L000116](../../agents/claim_evidence.py#L116) | 116 | `"        \"schema_version\": \"1.0\","` | — |
| [SRC-7D6FC391EC-L000117](../../agents/claim_evidence.py#L117) | 117 | `"        \"status\": \"built\","` | — |
| [SRC-7D6FC391EC-L000118](../../agents/claim_evidence.py#L118) | 118 | `"        \"method\": \"bounded_sentence_level_citation_trace\","` | — |
| [SRC-7D6FC391EC-L000119](../../agents/claim_evidence.py#L119) | 119 | `"        \"semantic_verification\": False,"` | — |
| [SRC-7D6FC391EC-L000120](../../agents/claim_evidence.py#L120) | 120 | `"        \"claim_entailment\": \"not_checked\","` | — |
| [SRC-7D6FC391EC-L000121](../../agents/claim_evidence.py#L121) | 121 | `"        \"fact_correctness\": \"not_checked\","` | — |
| [SRC-7D6FC391EC-L000122](../../agents/claim_evidence.py#L122) | 122 | `"        \"max_segments\": max_segments,"` | — |
| [SRC-7D6FC391EC-L000123](../../agents/claim_evidence.py#L123) | 123 | `"        \"max_citable_sources\": len(safe_sources),"` | — |
| [SRC-7D6FC391EC-L000124](../../agents/claim_evidence.py#L124) | 124 | `"        \"truncated\": truncated,"` | — |
| [SRC-7D6FC391EC-L000125](../../agents/claim_evidence.py#L125) | 125 | `"        \"summary\": {"` | — |
| [SRC-7D6FC391EC-L000126](../../agents/claim_evidence.py#L126) | 126 | `"            \"segment_candidate_count\": total,"` | — |
| [SRC-7D6FC391EC-L000127](../../agents/claim_evidence.py#L127) | 127 | `"            \"segments_with_citations\": cited,"` | — |
| [SRC-7D6FC391EC-L000128](../../agents/claim_evidence.py#L128) | 128 | `"            \"segments_without_citation_markers\": uncited,"` | — |
| [SRC-7D6FC391EC-L000129](../../agents/claim_evidence.py#L129) | 129 | `"            \"valid_source_reference_count\": valid_refs,"` | — |
| [SRC-7D6FC391EC-L000130](../../agents/claim_evidence.py#L130) | 130 | `"            \"out_of_range_reference_count\": invalid_refs,"` | — |
| [SRC-7D6FC391EC-L000131](../../agents/claim_evidence.py#L131) | 131 | `"            \"cited_segments_with_readable_source_evidence\": readable_cited,"` | — |
| [SRC-7D6FC391EC-L000132](../../agents/claim_evidence.py#L132) | 132 | `"            \"citation_lexical_signal_count\": lexical_signals,"` | — |
| [SRC-7D6FC391EC-L000133](../../agents/claim_evidence.py#L133) | 133 | `"            \"weak_citation_lexical_signal_count\": weak_signals,"` | — |
| [SRC-7D6FC391EC-L000134](../../agents/claim_evidence.py#L134) | 134 | `"            \"citation_coverage_ratio\": round(cited / total, 3) if total else 0.0,"` | — |
| [SRC-7D6FC391EC-L000135](../../agents/claim_evidence.py#L135) | 135 | `"        },"` | — |
| [SRC-7D6FC391EC-L000136](../../agents/claim_evidence.py#L136) | 136 | `"        \"segments\": rows,"` | — |
| [SRC-7D6FC391EC-L000137](../../agents/claim_evidence.py#L137) | 137 | `"        \"limitations\": ["` | — |
| [SRC-7D6FC391EC-L000138](../../agents/claim_evidence.py#L138) | 138 | `"            \"Sentence candidates are not independently classified into semantic claims.\","` | — |
| [SRC-7D6FC391EC-L000139](../../agents/claim_evidence.py#L139) | 139 | `"            \"An in-range index proves only that the source was in the bounded list.\","` | — |
| [SRC-7D6FC391EC-L000140](../../agents/claim_evidence.py#L140) | 140 | `"            \"Readable text and lexical overlap do not prove that a source entails a claim.\","` | — |
| [SRC-7D6FC391EC-L000141](../../agents/claim_evidence.py#L141) | 141 | `"            \"Correctness, source independence, contradiction resolution, and semantic faithfulness were not verified.\","` | — |
| [SRC-7D6FC391EC-L000142](../../agents/claim_evidence.py#L142) | 142 | `"        ],"` | — |
| [SRC-7D6FC391EC-L000143](../../agents/claim_evidence.py#L143) | 143 | `"    }"` | — |
## الوكيل والمنطق

### FILE-2D53795445 — [agents/dialogue_state.py](../../agents/dialogue_state.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-2D53795445-L000001](../../agents/dialogue_state.py#L1) | 1 | `"\"\"\"Validated dialogue-context records for Omarai."` | — |
| [SRC-2D53795445-L000002](../../agents/dialogue_state.py#L2) | 2 | `""` | — |
| [SRC-2D53795445-L000003](../../agents/dialogue_state.py#L3) | 3 | `"The language model may propose semantic context, but all returned state is bounded,"` | — |
| [SRC-2D53795445-L000004](../../agents/dialogue_state.py#L4) | 4 | `"normalized, and explicitly marked as model-derived or deterministic fallback. This"` | — |
| [SRC-2D53795445-L000005](../../agents/dialogue_state.py#L5) | 5 | `"module never performs I/O and never stores cross-request user state."` | — |
| [SRC-2D53795445-L000006](../../agents/dialogue_state.py#L6) | 6 | `"\"\"\""` | — |
| [SRC-2D53795445-L000007](../../agents/dialogue_state.py#L7) | 7 | `"from __future__ import annotations"` | — |
| [SRC-2D53795445-L000008](../../agents/dialogue_state.py#L8) | 8 | `""` | — |
| [SRC-2D53795445-L000009](../../agents/dialogue_state.py#L9) | 9 | `"import re"` | — |
| [SRC-2D53795445-L000010](../../agents/dialogue_state.py#L10) | 10 | `"import unicodedata"` | — |
| [SRC-2D53795445-L000011](../../agents/dialogue_state.py#L11) | 11 | `"from typing import Any"` | — |
| [SRC-2D53795445-L000012](../../agents/dialogue_state.py#L12) | 12 | `""` | — |
| [SRC-2D53795445-L000013](../../agents/dialogue_state.py#L13) | 13 | `"from agents.intent_router import resolve_followup_query"` | — |
| [SRC-2D53795445-L000014](../../agents/dialogue_state.py#L14) | 14 | `""` | — |
| [SRC-2D53795445-L000015](../../agents/dialogue_state.py#L15) | 15 | `"MAX_RESOLVED_QUESTION_CHARS = 500"` | — |
| [SRC-2D53795445-L000016](../../agents/dialogue_state.py#L16) | 16 | `"MAX_CONTEXT_TEXT_CHARS = 180"` | — |
| [SRC-2D53795445-L000017](../../agents/dialogue_state.py#L17) | 17 | `"MAX_ENTITIES = 8"` | — |
| [SRC-2D53795445-L000018](../../agents/dialogue_state.py#L18) | 18 | `"MAX_SLOT_VALUES = 16"` | — |
| [SRC-2D53795445-L000019](../../agents/dialogue_state.py#L19) | 19 | `""` | — |
| [SRC-2D53795445-L000020](../../agents/dialogue_state.py#L20) | 20 | `"_ALLOWED_INTENTS = frozenset({"` | — |
| [SRC-2D53795445-L000021](../../agents/dialogue_state.py#L21) | 21 | `"    \"answer_general\","` | — |
| [SRC-2D53795445-L000022](../../agents/dialogue_state.py#L22) | 22 | `"    \"compare\","` | — |
| [SRC-2D53795445-L000023](../../agents/dialogue_state.py#L23) | 23 | `"    \"current_information\","` | — |
| [SRC-2D53795445-L000024](../../agents/dialogue_state.py#L24) | 24 | `"    \"explain\","` | — |
| [SRC-2D53795445-L000025](../../agents/dialogue_state.py#L25) | 25 | `"    \"find_official_site\","` | — |
| [SRC-2D53795445-L000026](../../agents/dialogue_state.py#L26) | 26 | `"    \"find_product\","` | — |
| [SRC-2D53795445-L000027](../../agents/dialogue_state.py#L27) | 27 | `"    \"how_to\","` | — |
| [SRC-2D53795445-L000028](../../agents/dialogue_state.py#L28) | 28 | `"    \"lead_generation\","` | — |
| [SRC-2D53795445-L000029](../../agents/dialogue_state.py#L29) | 29 | `"    \"recommend\","` | — |
| [SRC-2D53795445-L000030](../../agents/dialogue_state.py#L30) | 30 | `"    \"social_opinions\","` | — |
| [SRC-2D53795445-L000031](../../agents/dialogue_state.py#L31) | 31 | `"    \"summarize\","` | — |
| [SRC-2D53795445-L000032](../../agents/dialogue_state.py#L32) | 32 | `"    \"troubleshoot\","` | — |
| [SRC-2D53795445-L000033](../../agents/dialogue_state.py#L33) | 33 | `"    \"unknown\","` | — |
| [SRC-2D53795445-L000034](../../agents/dialogue_state.py#L34) | 34 | `"})"` | — |
| [SRC-2D53795445-L000035](../../agents/dialogue_state.py#L35) | 35 | `"_ALLOWED_SLOT_KEYS = frozenset({"` | — |
| [SRC-2D53795445-L000036](../../agents/dialogue_state.py#L36) | 36 | `"    \"aspect\", \"audience\", \"budget\", \"capacity\", \"country\", \"currency\","` | — |
| [SRC-2D53795445-L000037](../../agents/dialogue_state.py#L37) | 37 | `"    \"entity\", \"goal\", \"language\", \"location\", \"model\", \"platform\", \"product\","` | — |
| [SRC-2D53795445-L000038](../../agents/dialogue_state.py#L38) | 38 | `"    \"time_range\", \"variant\", \"version\","` | — |
| [SRC-2D53795445-L000039](../../agents/dialogue_state.py#L39) | 39 | `"})"` | — |
| [SRC-2D53795445-L000040](../../agents/dialogue_state.py#L40) | 40 | `"_ALLOWED_CHANGED_SLOTS = _ALLOWED_SLOT_KEYS \| frozenset({\"topic\", \"intent\"})"` | — |
| [SRC-2D53795445-L000041](../../agents/dialogue_state.py#L41) | 41 | `"_ALLOWED_RESOLUTION_BASES = frozenset({"` | — |
| [SRC-2D53795445-L000042](../../agents/dialogue_state.py#L42) | 42 | `"    \"current_message\", \"explicit_confirmation\", \"history_inferred\","` | — |
| [SRC-2D53795445-L000043](../../agents/dialogue_state.py#L43) | 43 | `"    \"insufficient_evidence\", \"deterministic_fallback\","` | — |
| [SRC-2D53795445-L000044](../../agents/dialogue_state.py#L44) | 44 | `"})"` | — |
| [SRC-2D53795445-L000045](../../agents/dialogue_state.py#L45) | 45 | `"_ALLOWED_CONFIDENCE_BANDS = frozenset({\"low\", \"medium\", \"high\", \"unassessed\"})"` | — |
| [SRC-2D53795445-L000046](../../agents/dialogue_state.py#L46) | 46 | `"_WHITESPACE = re.compile(r\"\\s+\")"` | — |
| [SRC-2D53795445-L000047](../../agents/dialogue_state.py#L47) | 47 | `""` | — |
| [SRC-2D53795445-L000048](../../agents/dialogue_state.py#L48) | 48 | `""` | — |
| [SRC-2D53795445-L000049](../../agents/dialogue_state.py#L49) | 49 | `"def _clean_text(value: Any, limit: int) -> str:"` | — |
| [SRC-2D53795445-L000050](../../agents/dialogue_state.py#L50) | 50 | `"    if not isinstance(value, str):"` | — |
| [SRC-2D53795445-L000051](../../agents/dialogue_state.py#L51) | 51 | `"        return \"\""` | — |
| [SRC-2D53795445-L000052](../../agents/dialogue_state.py#L52) | 52 | `"    value = unicodedata.normalize(\"NFKC\", value)"` | — |
| [SRC-2D53795445-L000053](../../agents/dialogue_state.py#L53) | 53 | `"    value = value.replace(\"\\x00\", \" \")"` | — |
| [SRC-2D53795445-L000054](../../agents/dialogue_state.py#L54) | 54 | `"    value = _WHITESPACE.sub(\" \", value).strip()"` | — |
| [SRC-2D53795445-L000055](../../agents/dialogue_state.py#L55) | 55 | `"    return value[:limit]"` | — |
| [SRC-2D53795445-L000056](../../agents/dialogue_state.py#L56) | 56 | `""` | — |
| [SRC-2D53795445-L000057](../../agents/dialogue_state.py#L57) | 57 | `""` | — |
| [SRC-2D53795445-L000058](../../agents/dialogue_state.py#L58) | 58 | `"def _clean_string_list(value: Any, *, max_items: int, max_chars: int) -> list[str]:"` | — |
| [SRC-2D53795445-L000059](../../agents/dialogue_state.py#L59) | 59 | `"    if not isinstance(value, list):"` | — |
| [SRC-2D53795445-L000060](../../agents/dialogue_state.py#L60) | 60 | `"        return []"` | — |
| [SRC-2D53795445-L000061](../../agents/dialogue_state.py#L61) | 61 | `"    result: list[str] = []"` | — |
| [SRC-2D53795445-L000062](../../agents/dialogue_state.py#L62) | 62 | `"    seen: set[str] = set()"` | — |
| [SRC-2D53795445-L000063](../../agents/dialogue_state.py#L63) | 63 | `"    for item in value[:max_items * 2]:"` | — |
| [SRC-2D53795445-L000064](../../agents/dialogue_state.py#L64) | 64 | `"        clean = _clean_text(item, max_chars)"` | — |
| [SRC-2D53795445-L000065](../../agents/dialogue_state.py#L65) | 65 | `"        key = clean.casefold()"` | — |
| [SRC-2D53795445-L000066](../../agents/dialogue_state.py#L66) | 66 | `"        if clean and key not in seen:"` | — |
| [SRC-2D53795445-L000067](../../agents/dialogue_state.py#L67) | 67 | `"            result.append(clean)"` | — |
| [SRC-2D53795445-L000068](../../agents/dialogue_state.py#L68) | 68 | `"            seen.add(key)"` | — |
| [SRC-2D53795445-L000069](../../agents/dialogue_state.py#L69) | 69 | `"        if len(result) >= max_items:"` | — |
| [SRC-2D53795445-L000070](../../agents/dialogue_state.py#L70) | 70 | `"            break"` | — |
| [SRC-2D53795445-L000071](../../agents/dialogue_state.py#L71) | 71 | `"    return result"` | — |
| [SRC-2D53795445-L000072](../../agents/dialogue_state.py#L72) | 72 | `""` | — |
| [SRC-2D53795445-L000073](../../agents/dialogue_state.py#L73) | 73 | `""` | — |
| [SRC-2D53795445-L000074](../../agents/dialogue_state.py#L74) | 74 | `"def fallback_dialogue_context(question: str, history: Any = None) -> dict[str, Any]:"` | — |
| [SRC-2D53795445-L000075](../../agents/dialogue_state.py#L75) | 75 | `"    \"\"\"Build a conservative context record from the deterministic follow-up resolver.\"\"\""` | — |
| [SRC-2D53795445-L000076](../../agents/dialogue_state.py#L76) | 76 | `"    current = _clean_text(question, MAX_RESOLVED_QUESTION_CHARS)"` | — |
| [SRC-2D53795445-L000077](../../agents/dialogue_state.py#L77) | 77 | `"    resolved = _clean_text("` | — |
| [SRC-2D53795445-L000078](../../agents/dialogue_state.py#L78) | 78 | `"        resolve_followup_query(current, history) or current,"` | — |
| [SRC-2D53795445-L000079](../../agents/dialogue_state.py#L79) | 79 | `"        MAX_RESOLVED_QUESTION_CHARS,"` | — |
| [SRC-2D53795445-L000080](../../agents/dialogue_state.py#L80) | 80 | `"    )"` | — |
| [SRC-2D53795445-L000081](../../agents/dialogue_state.py#L81) | 81 | `"    is_follow_up = bool(resolved and current and resolved.casefold() != current.casefold())"` | — |
| [SRC-2D53795445-L000082](../../agents/dialogue_state.py#L82) | 82 | `"    return {"` | — |
| [SRC-2D53795445-L000083](../../agents/dialogue_state.py#L83) | 83 | `"        \"status\": \"fallback\","` | — |
| [SRC-2D53795445-L000084](../../agents/dialogue_state.py#L84) | 84 | `"        \"method\": \"deterministic_followup_heuristic\","` | — |
| [SRC-2D53795445-L000085](../../agents/dialogue_state.py#L85) | 85 | `"        \"resolved_question\": resolved or current,"` | — |
| [SRC-2D53795445-L000086](../../agents/dialogue_state.py#L86) | 86 | `"        \"intent\": \"unknown\","` | — |
| [SRC-2D53795445-L000087](../../agents/dialogue_state.py#L87) | 87 | `"        \"topic\": \"\","` | — |
| [SRC-2D53795445-L000088](../../agents/dialogue_state.py#L88) | 88 | `"        \"entities\": [],"` | — |
| [SRC-2D53795445-L000089](../../agents/dialogue_state.py#L89) | 89 | `"        \"slots\": {},"` | — |
| [SRC-2D53795445-L000090](../../agents/dialogue_state.py#L90) | 90 | `"        \"changed_slots\": [],"` | — |
| [SRC-2D53795445-L000091](../../agents/dialogue_state.py#L91) | 91 | `"        \"is_follow_up\": is_follow_up,"` | — |
| [SRC-2D53795445-L000092](../../agents/dialogue_state.py#L92) | 92 | `"        \"topic_shift\": False,"` | — |
| [SRC-2D53795445-L000093](../../agents/dialogue_state.py#L93) | 93 | `"        \"needs_web\": False,"` | — |
| [SRC-2D53795445-L000094](../../agents/dialogue_state.py#L94) | 94 | `"        \"research_depth\": \"standard\","` | — |
| [SRC-2D53795445-L000095](../../agents/dialogue_state.py#L95) | 95 | `"        \"needs_clarification\": False,"` | — |
| [SRC-2D53795445-L000096](../../agents/dialogue_state.py#L96) | 96 | `"        \"clarification_question\": \"\","` | — |
| [SRC-2D53795445-L000097](../../agents/dialogue_state.py#L97) | 97 | `"        \"unresolved_references\": [],"` | — |
| [SRC-2D53795445-L000098](../../agents/dialogue_state.py#L98) | 98 | `"        \"resolution_basis\": \"deterministic_fallback\","` | — |
| [SRC-2D53795445-L000099](../../agents/dialogue_state.py#L99) | 99 | `"        \"confidence_band\": \"unassessed\","` | — |
| [SRC-2D53795445-L000100](../../agents/dialogue_state.py#L100) | 100 | `"    }"` | — |
| [SRC-2D53795445-L000101](../../agents/dialogue_state.py#L101) | 101 | `""` | — |
| [SRC-2D53795445-L000102](../../agents/dialogue_state.py#L102) | 102 | `""` | — |
| [SRC-2D53795445-L000103](../../agents/dialogue_state.py#L103) | 103 | `"def validate_dialogue_context("` | — |
| [SRC-2D53795445-L000104](../../agents/dialogue_state.py#L104) | 104 | `"    candidate: Any,"` | — |
| [SRC-2D53795445-L000105](../../agents/dialogue_state.py#L105) | 105 | `"    question: str,"` | — |
| [SRC-2D53795445-L000106](../../agents/dialogue_state.py#L106) | 106 | `"    history: Any = None,"` | — |
| [SRC-2D53795445-L000107](../../agents/dialogue_state.py#L107) | 107 | `"    *,"` | — |
| [SRC-2D53795445-L000108](../../agents/dialogue_state.py#L108) | 108 | `"    fallback: dict[str, Any] \| None = None,"` | — |
| [SRC-2D53795445-L000109](../../agents/dialogue_state.py#L109) | 109 | `") -> dict[str, Any]:"` | — |
| [SRC-2D53795445-L000110](../../agents/dialogue_state.py#L110) | 110 | `"    \"\"\"Validate bounded context output from a planner without treating it as truth.\"\"\""` | — |
| [SRC-2D53795445-L000111](../../agents/dialogue_state.py#L111) | 111 | `"    baseline = dict(fallback or fallback_dialogue_context(question, history))"` | — |
| [SRC-2D53795445-L000112](../../agents/dialogue_state.py#L112) | 112 | `"    if not isinstance(candidate, dict):"` | — |
| [SRC-2D53795445-L000113](../../agents/dialogue_state.py#L113) | 113 | `"        return baseline"` | — |
| [SRC-2D53795445-L000114](../../agents/dialogue_state.py#L114) | 114 | `""` | — |
| [SRC-2D53795445-L000115](../../agents/dialogue_state.py#L115) | 115 | `"    current = _clean_text(question, MAX_RESOLVED_QUESTION_CHARS)"` | — |
| [SRC-2D53795445-L000116](../../agents/dialogue_state.py#L116) | 116 | `"    resolved = _clean_text(candidate.get(\"resolved_question\"), MAX_RESOLVED_QUESTION_CHARS)"` | — |
| [SRC-2D53795445-L000117](../../agents/dialogue_state.py#L117) | 117 | `"    if not resolved:"` | — |
| [SRC-2D53795445-L000118](../../agents/dialogue_state.py#L118) | 118 | `"        return baseline"` | — |
| [SRC-2D53795445-L000119](../../agents/dialogue_state.py#L119) | 119 | `""` | — |
| [SRC-2D53795445-L000120](../../agents/dialogue_state.py#L120) | 120 | `"    has_history = isinstance(history, list) and any("` | — |
| [SRC-2D53795445-L000121](../../agents/dialogue_state.py#L121) | 121 | `"        isinstance(item, dict)"` | — |
| [SRC-2D53795445-L000122](../../agents/dialogue_state.py#L122) | 122 | `"        and item.get(\"role\") in {\"user\", \"assistant\"}"` | — |
| [SRC-2D53795445-L000123](../../agents/dialogue_state.py#L123) | 123 | `"        and isinstance(item.get(\"content\"), str)"` | — |
| [SRC-2D53795445-L000124](../../agents/dialogue_state.py#L124) | 124 | `"        and item.get(\"content\", \"\").strip()"` | — |
| [SRC-2D53795445-L000125](../../agents/dialogue_state.py#L125) | 125 | `"        for item in history"` | — |
