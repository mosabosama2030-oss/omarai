# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **003**
- سجلات الأسطر: **800**
- النطاق: SRC-7D6FC391EC-L000169 إلى SRC-5587371288-L000456
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-7D6FC391EC — [agents/claim_evidence.py](../../agents/claim_evidence.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-7D6FC391EC-L000169](../../agents/claim_evidence.py#L169) | 169 | `"        has_readable = False"` | — |
| [SRC-7D6FC391EC-L000170](../../agents/claim_evidence.py#L170) | 170 | `"        for index in indexes:"` | — |
| [SRC-7D6FC391EC-L000171](../../agents/claim_evidence.py#L171) | 171 | `"            if index < 1 or index > len(safe_sources):"` | — |
| [SRC-7D6FC391EC-L000172](../../agents/claim_evidence.py#L172) | 172 | `"                invalid_refs += 1"` | — |
| [SRC-7D6FC391EC-L000173](../../agents/claim_evidence.py#L173) | 173 | `"                refs.append({"` | — |
| [SRC-7D6FC391EC-L000174](../../agents/claim_evidence.py#L174) | 174 | `"                    \"source_index\": index, \"reference_status\": \"index_out_of_citable_range\","` | — |
| [SRC-7D6FC391EC-L000175](../../agents/claim_evidence.py#L175) | 175 | `"                    \"title\": \"\", \"url\": \"\", \"evidence_basis\": \"unavailable\","` | — |
| [SRC-7D6FC391EC-L000176](../../agents/claim_evidence.py#L176) | 176 | `"                })"` | — |
| [SRC-7D6FC391EC-L000177](../../agents/claim_evidence.py#L177) | 177 | `"                continue"` | — |
| [SRC-7D6FC391EC-L000178](../../agents/claim_evidence.py#L178) | 178 | `"            source = safe_sources[index - 1]"` | — |
| [SRC-7D6FC391EC-L000179](../../agents/claim_evidence.py#L179) | 179 | `"            basis = _evidence_basis(source)"` | — |
| [SRC-7D6FC391EC-L000180](../../agents/claim_evidence.py#L180) | 180 | `"            valid_refs += 1"` | — |
| [SRC-7D6FC391EC-L000181](../../agents/claim_evidence.py#L181) | 181 | `"            # Titles are useful metadata, but not readable source text for checking entailment."` | — |
| [SRC-7D6FC391EC-L000182](../../agents/claim_evidence.py#L182) | 182 | `"            has_readable = has_readable or basis in {\"extracted_page_text\", \"search_snippet\"}"` | — |
| [SRC-7D6FC391EC-L000183](../../agents/claim_evidence.py#L183) | 183 | `"            refs.append({"` | — |
| [SRC-7D6FC391EC-L000184](../../agents/claim_evidence.py#L184) | 184 | `"                \"source_index\": index,"` | — |
| [SRC-7D6FC391EC-L000185](../../agents/claim_evidence.py#L185) | 185 | `"                \"reference_status\": ("` | — |
| [SRC-7D6FC391EC-L000186](../../agents/claim_evidence.py#L186) | 186 | `"                    \"valid_index_with_readable_evidence\""` | — |
| [SRC-7D6FC391EC-L000187](../../agents/claim_evidence.py#L187) | 187 | `"                    if basis in {\"extracted_page_text\", \"search_snippet\"}"` | — |
| [SRC-7D6FC391EC-L000188](../../agents/claim_evidence.py#L188) | 188 | `"                    else \"valid_index_without_readable_evidence\""` | — |
| [SRC-7D6FC391EC-L000189](../../agents/claim_evidence.py#L189) | 189 | `"                ),"` | — |
| [SRC-7D6FC391EC-L000190](../../agents/claim_evidence.py#L190) | 190 | `"                \"title\": str(source.get(\"title\") or \"\")[:240],"` | — |
| [SRC-7D6FC391EC-L000191](../../agents/claim_evidence.py#L191) | 191 | `"                \"url\": str(source.get(\"url\") or \"\")[:2048],"` | — |
| [SRC-7D6FC391EC-L000192](../../agents/claim_evidence.py#L192) | 192 | `"                \"provider\": str(source.get(\"provider\") or \"\")[:80],"` | — |
| [SRC-7D6FC391EC-L000193](../../agents/claim_evidence.py#L193) | 193 | `"                \"evidence_basis\": basis,"` | — |
| [SRC-7D6FC391EC-L000194](../../agents/claim_evidence.py#L194) | 194 | `"                \"metadata_audit\": audit_source_metadata(source, claim_text=f\"{question_context} {segment}\"),"` | — |
| [SRC-7D6FC391EC-L000195](../../agents/claim_evidence.py#L195) | 195 | `"            })"` | — |
| [SRC-7D6FC391EC-L000196](../../agents/claim_evidence.py#L196) | 196 | `""` | — |
| [SRC-7D6FC391EC-L000197](../../agents/claim_evidence.py#L197) | 197 | `"        cited += bool(indexes)"` | — |
| [SRC-7D6FC391EC-L000198](../../agents/claim_evidence.py#L198) | 198 | `"        uncited += not bool(indexes)"` | — |
| [SRC-7D6FC391EC-L000199](../../agents/claim_evidence.py#L199) | 199 | `"        readable_cited += bool(indexes) and has_readable"` | — |
| [SRC-7D6FC391EC-L000200](../../agents/claim_evidence.py#L200) | 200 | `"        alignment = alignment_by_sentence.get(number, {})"` | — |
| [SRC-7D6FC391EC-L000201](../../agents/claim_evidence.py#L201) | 201 | `"        lexical_status = str(alignment.get(\"status\") or \"not_assessed_no_citation_alignment\")"` | — |
| [SRC-7D6FC391EC-L000202](../../agents/claim_evidence.py#L202) | 202 | `"        lexical_signals += lexical_status == \"lexical_overlap_signal_found\""` | — |
| [SRC-7D6FC391EC-L000203](../../agents/claim_evidence.py#L203) | 203 | `"        weak_signals += lexical_status == \"weak_lexical_overlap\""` | — |
| [SRC-7D6FC391EC-L000204](../../agents/claim_evidence.py#L204) | 204 | `"        if any(ref[\"reference_status\"] == \"index_out_of_citable_range\" for ref in refs):"` | — |
| [SRC-7D6FC391EC-L000205](../../agents/claim_evidence.py#L205) | 205 | `"            status = \"citation_index_out_of_range\""` | — |
| [SRC-7D6FC391EC-L000206](../../agents/claim_evidence.py#L206) | 206 | `"        elif indexes and not has_readable:"` | — |
| [SRC-7D6FC391EC-L000207](../../agents/claim_evidence.py#L207) | 207 | `"            status = \"valid_index_without_readable_evidence\""` | — |
| [SRC-7D6FC391EC-L000208](../../agents/claim_evidence.py#L208) | 208 | `"        elif indexes:"` | — |
| [SRC-7D6FC391EC-L000209](../../agents/claim_evidence.py#L209) | 209 | `"            status = \"cited_source_attached\""` | — |
| [SRC-7D6FC391EC-L000210](../../agents/claim_evidence.py#L210) | 210 | `"        else:"` | — |
| [SRC-7D6FC391EC-L000211](../../agents/claim_evidence.py#L211) | 211 | `"            status = \"no_citation_marker\""` | — |
| [SRC-7D6FC391EC-L000212](../../agents/claim_evidence.py#L212) | 212 | `""` | — |
| [SRC-7D6FC391EC-L000213](../../agents/claim_evidence.py#L213) | 213 | `"        rows.append({"` | — |
| [SRC-7D6FC391EC-L000214](../../agents/claim_evidence.py#L214) | 214 | `"            \"segment_id\": f\"S{number:03d}\","` | — |
| [SRC-7D6FC391EC-L000215](../../agents/claim_evidence.py#L215) | 215 | `"            \"segment_number\": number,"` | — |
| [SRC-7D6FC391EC-L000216](../../agents/claim_evidence.py#L216) | 216 | `"            \"unit_kind\": \"sentence_candidate_not_semantically_classified\","` | — |
| [SRC-7D6FC391EC-L000217](../../agents/claim_evidence.py#L217) | 217 | `"            \"text\": segment[:1200],"` | — |
| [SRC-7D6FC391EC-L000218](../../agents/claim_evidence.py#L218) | 218 | `"            \"citation_indexes\": indexes,"` | — |
| [SRC-7D6FC391EC-L000219](../../agents/claim_evidence.py#L219) | 219 | `"            \"citation_status\": status,"` | — |
| [SRC-7D6FC391EC-L000220](../../agents/claim_evidence.py#L220) | 220 | `"            \"lexical_audit_status\": lexical_status,"` | — |
| [SRC-7D6FC391EC-L000221](../../agents/claim_evidence.py#L221) | 221 | `"            \"sources\": refs,"` | — |
| [SRC-7D6FC391EC-L000222](../../agents/claim_evidence.py#L222) | 222 | `"        })"` | — |
| [SRC-7D6FC391EC-L000223](../../agents/claim_evidence.py#L223) | 223 | `""` | — |
| [SRC-7D6FC391EC-L000224](../../agents/claim_evidence.py#L224) | 224 | `"    total = len(rows)"` | — |
| [SRC-7D6FC391EC-L000225](../../agents/claim_evidence.py#L225) | 225 | `"    return {"` | — |
| [SRC-7D6FC391EC-L000226](../../agents/claim_evidence.py#L226) | 226 | `"        \"schema_version\": \"1.0\","` | — |
| [SRC-7D6FC391EC-L000227](../../agents/claim_evidence.py#L227) | 227 | `"        \"status\": \"built\","` | — |
| [SRC-7D6FC391EC-L000228](../../agents/claim_evidence.py#L228) | 228 | `"        \"method\": \"bounded_sentence_level_citation_trace\","` | — |
| [SRC-7D6FC391EC-L000229](../../agents/claim_evidence.py#L229) | 229 | `"        \"semantic_verification\": False,"` | — |
| [SRC-7D6FC391EC-L000230](../../agents/claim_evidence.py#L230) | 230 | `"        \"claim_entailment\": \"not_checked\","` | — |
| [SRC-7D6FC391EC-L000231](../../agents/claim_evidence.py#L231) | 231 | `"        \"fact_correctness\": \"not_checked\","` | — |
| [SRC-7D6FC391EC-L000232](../../agents/claim_evidence.py#L232) | 232 | `"        \"max_segments\": max_segments,"` | — |
| [SRC-7D6FC391EC-L000233](../../agents/claim_evidence.py#L233) | 233 | `"        \"max_citable_sources\": len(safe_sources),"` | — |
| [SRC-7D6FC391EC-L000234](../../agents/claim_evidence.py#L234) | 234 | `"        \"truncated\": truncated,"` | — |
| [SRC-7D6FC391EC-L000235](../../agents/claim_evidence.py#L235) | 235 | `"        \"summary\": {"` | — |
| [SRC-7D6FC391EC-L000236](../../agents/claim_evidence.py#L236) | 236 | `"            \"segment_candidate_count\": total,"` | — |
| [SRC-7D6FC391EC-L000237](../../agents/claim_evidence.py#L237) | 237 | `"            \"segments_with_citations\": cited,"` | — |
| [SRC-7D6FC391EC-L000238](../../agents/claim_evidence.py#L238) | 238 | `"            \"segments_without_citation_markers\": uncited,"` | — |
| [SRC-7D6FC391EC-L000239](../../agents/claim_evidence.py#L239) | 239 | `"            \"valid_source_reference_count\": valid_refs,"` | — |
| [SRC-7D6FC391EC-L000240](../../agents/claim_evidence.py#L240) | 240 | `"            \"out_of_range_reference_count\": invalid_refs,"` | — |
| [SRC-7D6FC391EC-L000241](../../agents/claim_evidence.py#L241) | 241 | `"            \"cited_segments_with_readable_source_evidence\": readable_cited,"` | — |
| [SRC-7D6FC391EC-L000242](../../agents/claim_evidence.py#L242) | 242 | `"            \"citation_lexical_signal_count\": lexical_signals,"` | — |
| [SRC-7D6FC391EC-L000243](../../agents/claim_evidence.py#L243) | 243 | `"            \"weak_citation_lexical_signal_count\": weak_signals,"` | — |
| [SRC-7D6FC391EC-L000244](../../agents/claim_evidence.py#L244) | 244 | `"            \"citation_coverage_ratio\": round(cited / total, 3) if total else 0.0,"` | — |
| [SRC-7D6FC391EC-L000245](../../agents/claim_evidence.py#L245) | 245 | `"        },"` | — |
| [SRC-7D6FC391EC-L000246](../../agents/claim_evidence.py#L246) | 246 | `"        \"segments\": rows,"` | — |
| [SRC-7D6FC391EC-L000247](../../agents/claim_evidence.py#L247) | 247 | `"        \"limitations\": ["` | — |
| [SRC-7D6FC391EC-L000248](../../agents/claim_evidence.py#L248) | 248 | `"            \"Sentence candidates are not independently classified into semantic claims.\","` | — |
| [SRC-7D6FC391EC-L000249](../../agents/claim_evidence.py#L249) | 249 | `"            \"An in-range index proves only that the source was in the bounded list.\","` | — |
| [SRC-7D6FC391EC-L000250](../../agents/claim_evidence.py#L250) | 250 | `"            \"Readable text and lexical overlap do not prove that a source entails a claim.\","` | — |
| [SRC-7D6FC391EC-L000251](../../agents/claim_evidence.py#L251) | 251 | `"            \"Correctness, source independence, contradiction resolution, and semantic faithfulness were not verified.\","` | — |
| [SRC-7D6FC391EC-L000252](../../agents/claim_evidence.py#L252) | 252 | `"        ],"` | — |
| [SRC-7D6FC391EC-L000253](../../agents/claim_evidence.py#L253) | 253 | `"    }"` | — |
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
| [SRC-2D53795445-L000126](../../agents/dialogue_state.py#L126) | 126 | `"    )"` | — |
| [SRC-2D53795445-L000127](../../agents/dialogue_state.py#L127) | 127 | `"    topic_shift = candidate.get(\"topic_shift\") is True"` | — |
| [SRC-2D53795445-L000128](../../agents/dialogue_state.py#L128) | 128 | `"    model_marked_follow_up = candidate.get(\"is_follow_up\") is True"` | — |
| [SRC-2D53795445-L000129](../../agents/dialogue_state.py#L129) | 129 | `"    is_follow_up = model_marked_follow_up and has_history and not topic_shift"` | — |
| [SRC-2D53795445-L000130](../../agents/dialogue_state.py#L130) | 130 | `""` | — |
| [SRC-2D53795445-L000131](../../agents/dialogue_state.py#L131) | 131 | `"    # Context is inherited only when the semantic resolver explicitly says this is"` | — |
| [SRC-2D53795445-L000132](../../agents/dialogue_state.py#L132) | 132 | `"    # a follow-up. A standalone turn must not retain an old entity merely because"` | — |
| [SRC-2D53795445-L000133](../../agents/dialogue_state.py#L133) | 133 | `"    # the model accidentally emitted a blended resolved_question."` | — |
| [SRC-2D53795445-L000134](../../agents/dialogue_state.py#L134) | 134 | `"    rejected_stale_context = ("` | — |
| [SRC-2D53795445-L000135](../../agents/dialogue_state.py#L135) | 135 | `"        not model_marked_follow_up"` | — |
| [SRC-2D53795445-L000136](../../agents/dialogue_state.py#L136) | 136 | `"        and resolved.casefold() != current.casefold()"` | — |
| [SRC-2D53795445-L000137](../../agents/dialogue_state.py#L137) | 137 | `"    )"` | — |
| [SRC-2D53795445-L000138](../../agents/dialogue_state.py#L138) | 138 | `"    reset_context = topic_shift or not has_history or rejected_stale_context"` | — |
| [SRC-2D53795445-L000139](../../agents/dialogue_state.py#L139) | 139 | `"    if reset_context:"` | — |
| [SRC-2D53795445-L000140](../../agents/dialogue_state.py#L140) | 140 | `"        resolved = current"` | — |
| [SRC-2D53795445-L000141](../../agents/dialogue_state.py#L141) | 141 | `"        is_follow_up = False"` | — |
| [SRC-2D53795445-L000142](../../agents/dialogue_state.py#L142) | 142 | `""` | — |
| [SRC-2D53795445-L000143](../../agents/dialogue_state.py#L143) | 143 | `"    needs_clarification = candidate.get(\"needs_clarification\") is True"` | — |
| [SRC-2D53795445-L000144](../../agents/dialogue_state.py#L144) | 144 | `"    if needs_clarification:"` | — |
| [SRC-2D53795445-L000145](../../agents/dialogue_state.py#L145) | 145 | `"        # Never issue a search based on a reference the model itself says is unresolved."` | — |
| [SRC-2D53795445-L000146](../../agents/dialogue_state.py#L146) | 146 | `"        resolved = current"` | — |
| [SRC-2D53795445-L000147](../../agents/dialogue_state.py#L147) | 147 | `""` | — |
| [SRC-2D53795445-L000148](../../agents/dialogue_state.py#L148) | 148 | `"    intent = candidate.get(\"intent\")"` | — |
| [SRC-2D53795445-L000149](../../agents/dialogue_state.py#L149) | 149 | `"    if not isinstance(intent, str) or intent not in _ALLOWED_INTENTS:"` | — |
| [SRC-2D53795445-L000150](../../agents/dialogue_state.py#L150) | 150 | `"        intent = \"unknown\""` | — |
| [SRC-2D53795445-L000151](../../agents/dialogue_state.py#L151) | 151 | `""` | — |
| [SRC-2D53795445-L000152](../../agents/dialogue_state.py#L152) | 152 | `"    raw_slots = candidate.get(\"slots\")"` | — |
| [SRC-2D53795445-L000153](../../agents/dialogue_state.py#L153) | 153 | `"    slots: dict[str, str] = {}"` | — |
| [SRC-2D53795445-L000154](../../agents/dialogue_state.py#L154) | 154 | `"    # Do not carry extracted entities/slots from a rejected or explicitly shifted"` | — |
| [SRC-2D53795445-L000155](../../agents/dialogue_state.py#L155) | 155 | `"    # topic into downstream planning. The current message will be parsed on its own."` | — |
| [SRC-2D53795445-L000156](../../agents/dialogue_state.py#L156) | 156 | `"    clear_inherited_metadata = topic_shift or rejected_stale_context or not has_history"` | — |
| [SRC-2D53795445-L000157](../../agents/dialogue_state.py#L157) | 157 | `"    if isinstance(raw_slots, dict) and not clear_inherited_metadata:"` | — |
| [SRC-2D53795445-L000158](../../agents/dialogue_state.py#L158) | 158 | `"        for raw_key, raw_value in list(raw_slots.items())[:MAX_SLOT_VALUES]:"` | — |
| [SRC-2D53795445-L000159](../../agents/dialogue_state.py#L159) | 159 | `"            key = _clean_text(raw_key, 40)"` | — |
| [SRC-2D53795445-L000160](../../agents/dialogue_state.py#L160) | 160 | `"            value = _clean_text(raw_value, MAX_CONTEXT_TEXT_CHARS)"` | — |
| [SRC-2D53795445-L000161](../../agents/dialogue_state.py#L161) | 161 | `"            if key in _ALLOWED_SLOT_KEYS and value:"` | — |
| [SRC-2D53795445-L000162](../../agents/dialogue_state.py#L162) | 162 | `"                slots[key] = value"` | — |
| [SRC-2D53795445-L000163](../../agents/dialogue_state.py#L163) | 163 | `""` | — |
| [SRC-2D53795445-L000164](../../agents/dialogue_state.py#L164) | 164 | `"    changed_slots = ["` | — |
| [SRC-2D53795445-L000165](../../agents/dialogue_state.py#L165) | 165 | `"        item for item in _clean_string_list("` | — |
| [SRC-2D53795445-L000166](../../agents/dialogue_state.py#L166) | 166 | `"            candidate.get(\"changed_slots\"), max_items=8, max_chars=40"` | — |
| [SRC-2D53795445-L000167](../../agents/dialogue_state.py#L167) | 167 | `"        )"` | — |
| [SRC-2D53795445-L000168](../../agents/dialogue_state.py#L168) | 168 | `"        if item in _ALLOWED_CHANGED_SLOTS"` | — |
| [SRC-2D53795445-L000169](../../agents/dialogue_state.py#L169) | 169 | `"    ]"` | — |
| [SRC-2D53795445-L000170](../../agents/dialogue_state.py#L170) | 170 | `"    resolution_basis = candidate.get(\"resolution_basis\")"` | — |
| [SRC-2D53795445-L000171](../../agents/dialogue_state.py#L171) | 171 | `"    if not isinstance(resolution_basis, str) or resolution_basis not in _ALLOWED_RESOLUTION_BASES:"` | — |
| [SRC-2D53795445-L000172](../../agents/dialogue_state.py#L172) | 172 | `"        resolution_basis = \"history_inferred\" if is_follow_up else \"current_message\""` | — |
| [SRC-2D53795445-L000173](../../agents/dialogue_state.py#L173) | 173 | `"    if topic_shift:"` | — |
| [SRC-2D53795445-L000174](../../agents/dialogue_state.py#L174) | 174 | `"        resolution_basis = \"current_message\""` | — |
| [SRC-2D53795445-L000175](../../agents/dialogue_state.py#L175) | 175 | `""` | — |
| [SRC-2D53795445-L000176](../../agents/dialogue_state.py#L176) | 176 | `"    depth = candidate.get(\"research_depth\")"` | — |
| [SRC-2D53795445-L000177](../../agents/dialogue_state.py#L177) | 177 | `"    if depth not in {\"standard\", \"deep\"}:"` | — |
| [SRC-2D53795445-L000178](../../agents/dialogue_state.py#L178) | 178 | `"        depth = \"standard\""` | — |
| [SRC-2D53795445-L000179](../../agents/dialogue_state.py#L179) | 179 | `""` | — |
| [SRC-2D53795445-L000180](../../agents/dialogue_state.py#L180) | 180 | `"    confidence_band = candidate.get(\"confidence_band\")"` | — |
| [SRC-2D53795445-L000181](../../agents/dialogue_state.py#L181) | 181 | `"    if confidence_band not in _ALLOWED_CONFIDENCE_BANDS:"` | — |
| [SRC-2D53795445-L000182](../../agents/dialogue_state.py#L182) | 182 | `"        confidence_band = \"unassessed\""` | — |
| [SRC-2D53795445-L000183](../../agents/dialogue_state.py#L183) | 183 | `""` | — |
| [SRC-2D53795445-L000184](../../agents/dialogue_state.py#L184) | 184 | `"    clarification_question = _clean_text("` | — |
| [SRC-2D53795445-L000185](../../agents/dialogue_state.py#L185) | 185 | `"        candidate.get(\"clarification_question\"), 400"` | — |
| [SRC-2D53795445-L000186](../../agents/dialogue_state.py#L186) | 186 | `"    ) if needs_clarification else \"\""` | — |
| [SRC-2D53795445-L000187](../../agents/dialogue_state.py#L187) | 187 | `""` | — |
| [SRC-2D53795445-L000188](../../agents/dialogue_state.py#L188) | 188 | `"    status = ("` | — |
| [SRC-2D53795445-L000189](../../agents/dialogue_state.py#L189) | 189 | `"        \"needs_clarification\" if needs_clarification"` | — |
| [SRC-2D53795445-L000190](../../agents/dialogue_state.py#L190) | 190 | `"        else \"topic_shift\" if topic_shift"` | — |
| [SRC-2D53795445-L000191](../../agents/dialogue_state.py#L191) | 191 | `"        else \"resolved\""` | — |
| [SRC-2D53795445-L000192](../../agents/dialogue_state.py#L192) | 192 | `"    )"` | — |
| [SRC-2D53795445-L000193](../../agents/dialogue_state.py#L193) | 193 | `"    return {"` | — |
| [SRC-2D53795445-L000194](../../agents/dialogue_state.py#L194) | 194 | `"        \"status\": status,"` | — |
| [SRC-2D53795445-L000195](../../agents/dialogue_state.py#L195) | 195 | `"        \"method\": \"llm_semantic_context\","` | — |
| [SRC-2D53795445-L000196](../../agents/dialogue_state.py#L196) | 196 | `"        \"resolved_question\": resolved,"` | — |
| [SRC-2D53795445-L000197](../../agents/dialogue_state.py#L197) | 197 | `"        \"intent\": intent,"` | — |
| [SRC-2D53795445-L000198](../../agents/dialogue_state.py#L198) | 198 | `"        \"topic\": ("` | — |
| [SRC-2D53795445-L000199](../../agents/dialogue_state.py#L199) | 199 | `"            \"\" if clear_inherited_metadata"` | — |
| [SRC-2D53795445-L000200](../../agents/dialogue_state.py#L200) | 200 | `"            else _clean_text(candidate.get(\"topic\"), MAX_CONTEXT_TEXT_CHARS)"` | — |
| [SRC-2D53795445-L000201](../../agents/dialogue_state.py#L201) | 201 | `"        ),"` | — |
| [SRC-2D53795445-L000202](../../agents/dialogue_state.py#L202) | 202 | `"        \"entities\": ("` | — |
| [SRC-2D53795445-L000203](../../agents/dialogue_state.py#L203) | 203 | `"            [] if clear_inherited_metadata else _clean_string_list("` | — |
| [SRC-2D53795445-L000204](../../agents/dialogue_state.py#L204) | 204 | `"                candidate.get(\"entities\"), max_items=MAX_ENTITIES, max_chars=MAX_CONTEXT_TEXT_CHARS"` | — |
| [SRC-2D53795445-L000205](../../agents/dialogue_state.py#L205) | 205 | `"            )"` | — |
| [SRC-2D53795445-L000206](../../agents/dialogue_state.py#L206) | 206 | `"        ),"` | — |
| [SRC-2D53795445-L000207](../../agents/dialogue_state.py#L207) | 207 | `"        \"slots\": slots,"` | — |
| [SRC-2D53795445-L000208](../../agents/dialogue_state.py#L208) | 208 | `"        \"changed_slots\": [] if clear_inherited_metadata else changed_slots,"` | — |
| [SRC-2D53795445-L000209](../../agents/dialogue_state.py#L209) | 209 | `"        \"is_follow_up\": is_follow_up,"` | — |
| [SRC-2D53795445-L000210](../../agents/dialogue_state.py#L210) | 210 | `"        \"topic_shift\": topic_shift,"` | — |
| [SRC-2D53795445-L000211](../../agents/dialogue_state.py#L211) | 211 | `"        \"needs_web\": candidate.get(\"needs_web\") is True,"` | — |
| [SRC-2D53795445-L000212](../../agents/dialogue_state.py#L212) | 212 | `"        \"research_depth\": depth,"` | — |
| [SRC-2D53795445-L000213](../../agents/dialogue_state.py#L213) | 213 | `"        \"needs_clarification\": needs_clarification,"` | — |
| [SRC-2D53795445-L000214](../../agents/dialogue_state.py#L214) | 214 | `"        \"clarification_question\": clarification_question,"` | — |
| [SRC-2D53795445-L000215](../../agents/dialogue_state.py#L215) | 215 | `"        \"unresolved_references\": _clean_string_list("` | — |
| [SRC-2D53795445-L000216](../../agents/dialogue_state.py#L216) | 216 | `"            candidate.get(\"unresolved_references\"), max_items=8, max_chars=100"` | — |
| [SRC-2D53795445-L000217](../../agents/dialogue_state.py#L217) | 217 | `"        ),"` | — |
| [SRC-2D53795445-L000218](../../agents/dialogue_state.py#L218) | 218 | `"        \"resolution_basis\": resolution_basis,"` | — |
| [SRC-2D53795445-L000219](../../agents/dialogue_state.py#L219) | 219 | `"        \"confidence_band\": confidence_band,"` | — |
| [SRC-2D53795445-L000220](../../agents/dialogue_state.py#L220) | 220 | `"    }"` | — |
| [SRC-2D53795445-L000221](../../agents/dialogue_state.py#L221) | 221 | `""` | — |
| [SRC-2D53795445-L000222](../../agents/dialogue_state.py#L222) | 222 | `""` | — |
| [SRC-2D53795445-L000223](../../agents/dialogue_state.py#L223) | 223 | `"def might_be_context_dependent(question: str) -> bool:"` | — |
| [SRC-2D53795445-L000224](../../agents/dialogue_state.py#L224) | 224 | `"    \"\"\"Cheap trigger only; it does not decide the meaning of a contextual message.\"\"\""` | — |
| [SRC-2D53795445-L000225](../../agents/dialogue_state.py#L225) | 225 | `"    current = _clean_text(question, MAX_RESOLVED_QUESTION_CHARS).casefold()"` | — |
| [SRC-2D53795445-L000226](../../agents/dialogue_state.py#L226) | 226 | `"    if not current or len(current) > 220:"` | — |
| [SRC-2D53795445-L000227](../../agents/dialogue_state.py#L227) | 227 | `"        return False"` | — |
| [SRC-2D53795445-L000228](../../agents/dialogue_state.py#L228) | 228 | `"    lead_in = re.search("` | — |
| [SRC-2D53795445-L000229](../../agents/dialogue_state.py#L229) | 229 | `"        r\"^(?:و?طب\|و?طيب\|و?تمام\|ثم\|كمان\|وبالنسبه\|بالنسبه\|\""` | — |
| [SRC-2D53795445-L000230](../../agents/dialogue_state.py#L230) | 230 | `"        r\"(?:و)?(?:ال)?(?:سعر\|اسعار\|ثمن\|ضمان\|بطاريه\|كاميرا\|مكان\|رابط\|\""` | — |
| [SRC-2D53795445-L000231](../../agents/dialogue_state.py#L231) | 231 | `"        r\"مصدر\|مميزات\|عيوب\|فرق\|توفر\|سرعه\|اداء\|جوده\|صيانه)\\b\|\""` | — |
| [SRC-2D53795445-L000232](../../agents/dialogue_state.py#L232) | 232 | `"        r\"and\\s+(?:what\|the\|how)\|what\\s+about\|how\\s+about\|\""` | — |
| [SRC-2D53795445-L000233](../../agents/dialogue_state.py#L233) | 233 | `"        r\"then\\b\|also\\b\|as\\s+for\\b\|and\\s+its\\b)\","` | — |
| [SRC-2D53795445-L000234](../../agents/dialogue_state.py#L234) | 234 | `"        current,"` | — |
| [SRC-2D53795445-L000235](../../agents/dialogue_state.py#L235) | 235 | `"    )"` | — |
| [SRC-2D53795445-L000236](../../agents/dialogue_state.py#L236) | 236 | `"    reference = re.search("` | — |
| [SRC-2D53795445-L000237](../../agents/dialogue_state.py#L237) | 237 | `"        r\"\\b(?:it\|its\|they\|them\|their\|this\|that\|these\|those\|there\|\""` | — |
| [SRC-2D53795445-L000238](../../agents/dialogue_state.py#L238) | 238 | `"        r\"he\|she\|هو\|هي\|هذا\|هذه\|هذان\|هاتان\|هؤلاء\|ذلك\|تلك\|اللذان\|اللتان\|\""` | — |
| [SRC-2D53795445-L000239](../../agents/dialogue_state.py#L239) | 239 | `"        r\"الذي\|التي\|الذين\|ده\|دي\|دا\|دول\|عليه\|عليها\|فيه\|فيها\|لها\|له\|\""` | — |
| [SRC-2D53795445-L000240](../../agents/dialogue_state.py#L240) | 240 | `"        r\"سعرها\|سعره\|ضمانها\|ضمانه\|بطاريتها\|كاميرتها)\\b\","` | — |
| [SRC-2D53795445-L000241](../../agents/dialogue_state.py#L241) | 241 | `"        current,"` | — |
| [SRC-2D53795445-L000242](../../agents/dialogue_state.py#L242) | 242 | `"    )"` | — |
| [SRC-2D53795445-L000243](../../agents/dialogue_state.py#L243) | 243 | `"    fragment = re.fullmatch("` | — |
| [SRC-2D53795445-L000244](../../agents/dialogue_state.py#L244) | 244 | `"        r\"[؟?\\s]*(?:و)?(?:السعر\|الاسعار\|الضمان\|البطاريه\|الكاميرا\|\""` | — |
| [SRC-2D53795445-L000245](../../agents/dialogue_state.py#L245) | 245 | `"        r\"المكان\|الرابط\|المصدر\|المميزات\|العيوب\|سعر\|ضمان\|بطاريه\|كاميرا\|\""` | — |
| [SRC-2D53795445-L000246](../../agents/dialogue_state.py#L246) | 246 | `"        r\"مكان\|رابط\|مصدر\|warranty\|price\|battery\|camera\|location\|source\|pros\|cons)\""` | — |
| [SRC-2D53795445-L000247](../../agents/dialogue_state.py#L247) | 247 | `"        r\"[؟?\\s]*\","` | — |
| [SRC-2D53795445-L000248](../../agents/dialogue_state.py#L248) | 248 | `"        current,"` | — |
| [SRC-2D53795445-L000249](../../agents/dialogue_state.py#L249) | 249 | `"    )"` | — |
| [SRC-2D53795445-L000250](../../agents/dialogue_state.py#L250) | 250 | `"    # Arabic object pronouns are often attached to verbs, as in \"أشتريه\""` | — |
| [SRC-2D53795445-L000251](../../agents/dialogue_state.py#L251) | 251 | `"    # or \"أستخدمها\"; whitespace-token pronoun lists miss these natural follow-ups."` | — |
| [SRC-2D53795445-L000252](../../agents/dialogue_state.py#L252) | 252 | `"    attached_reference = re.search("` | — |
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
| [SRC-5587371288-L000164](../../agents/intent_router.py#L164) | 164 | `""` | — |
| [SRC-5587371288-L000165](../../agents/intent_router.py#L165) | 165 | `""` | — |
| [SRC-5587371288-L000166](../../agents/intent_router.py#L166) | 166 | `"def _starts_with_contextual_aspect(question: str) -> bool:"` | — |
| [SRC-5587371288-L000167](../../agents/intent_router.py#L167) | 167 | `"    \"\"\"Recognize aspect-led follow-ups without merging standalone new topics.\"\"\""` | — |
| [SRC-5587371288-L000168](../../agents/intent_router.py#L168) | 168 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000169](../../agents/intent_router.py#L169) | 169 | `"    if _CONTEXTUAL_ENGLISH_ASPECT_RE.match(normalized):"` | — |
| [SRC-5587371288-L000170](../../agents/intent_router.py#L170) | 170 | `"        return True"` | — |
| [SRC-5587371288-L000171](../../agents/intent_router.py#L171) | 171 | `"    stripped = _strip_followup_leadin(normalized)"` | — |
| [SRC-5587371288-L000172](../../agents/intent_router.py#L172) | 172 | `"    if stripped != normalized:"` | — |
| [SRC-5587371288-L000173](../../agents/intent_router.py#L173) | 173 | `"        return bool(_CONTEXTUAL_ASPECT_RE.match(stripped))"` | — |
| [SRC-5587371288-L000174](../../agents/intent_router.py#L174) | 174 | `"    if normalized.startswith(\"و\"):"` | — |
| [SRC-5587371288-L000175](../../agents/intent_router.py#L175) | 175 | `"        return bool(_CONTEXTUAL_ASPECT_RE.match(normalized[1:]))"` | — |
| [SRC-5587371288-L000176](../../agents/intent_router.py#L176) | 176 | `"    return False"` | — |
| [SRC-5587371288-L000177](../../agents/intent_router.py#L177) | 177 | `""` | — |
| [SRC-5587371288-L000178](../../agents/intent_router.py#L178) | 178 | `""` | — |
| [SRC-5587371288-L000179](../../agents/intent_router.py#L179) | 179 | `"def _needs_clarification(question: str) -> bool:"` | — |
| [SRC-5587371288-L000180](../../agents/intent_router.py#L180) | 180 | `"    normalized = _strip_followup_leadin(_normalize(question))"` | — |
| [SRC-5587371288-L000181](../../agents/intent_router.py#L181) | 181 | `"    ambiguous = {_normalize(item) for item in _AMBIGUOUS_ARABIC}"` | — |
| [SRC-5587371288-L000182](../../agents/intent_router.py#L182) | 182 | `"    ambiguous.update(_normalize(item) for item in _AMBIGUOUS_ENGLISH)"` | — |
| [SRC-5587371288-L000183](../../agents/intent_router.py#L183) | 183 | `"    if ("` | — |
| [SRC-5587371288-L000184](../../agents/intent_router.py#L184) | 184 | `"        normalized in ambiguous"` | — |
| [SRC-5587371288-L000185](../../agents/intent_router.py#L185) | 185 | `"        or normalized in _FOLLOWUP_ASPECT_FRAGMENTS"` | — |
| [SRC-5587371288-L000186](../../agents/intent_router.py#L186) | 186 | `"        or _starts_with_contextual_aspect(question)"` | — |
| [SRC-5587371288-L000187](../../agents/intent_router.py#L187) | 187 | `"    ):"` | — |
| [SRC-5587371288-L000188](../../agents/intent_router.py#L188) | 188 | `"        return True"` | — |
| [SRC-5587371288-L000189](../../agents/intent_router.py#L189) | 189 | `"    # Common inflected forms and short property-only follow-ups."` | — |
| [SRC-5587371288-L000190](../../agents/intent_router.py#L190) | 190 | `"    return bool("` | — |
| [SRC-5587371288-L000191](../../agents/intent_router.py#L191) | 191 | `"        re.fullmatch(r\"(?:كام\|كم\|بكام)\\s+(?:سعر\|ثمن)\\s*(?:ها\|ه\|هم)\", normalized)"` | — |
| [SRC-5587371288-L000192](../../agents/intent_router.py#L192) | 192 | `"        or re.fullmatch(r\"(?:قارن\|قارنلي)\\s+(?:بينهم\|بينهما\|دول\|دي\|دولتين)\", normalized)"` | — |
| [SRC-5587371288-L000193](../../agents/intent_router.py#L193) | 193 | `"        or re.fullmatch(r\"(?:و)?(?:السعر\|الاسعار\|التكلفه\|الضمان\|المميزات\|العيوب\|البطاريه\|الكاميرا\|المكان\|المصدر\|الرابط\|التاريخ)\", normalized)"` | — |
| [SRC-5587371288-L000194](../../agents/intent_router.py#L194) | 194 | `"    )"` | — |
| [SRC-5587371288-L000195](../../agents/intent_router.py#L195) | 195 | `""` | — |
| [SRC-5587371288-L000196](../../agents/intent_router.py#L196) | 196 | `""` | — |
| [SRC-5587371288-L000197](../../agents/intent_router.py#L197) | 197 | `"def _is_clarification_message(content: Any) -> bool:"` | — |
| [SRC-5587371288-L000198](../../agents/intent_router.py#L198) | 198 | `"    if not isinstance(content, str):"` | — |
| [SRC-5587371288-L000199](../../agents/intent_router.py#L199) | 199 | `"        return False"` | — |
| [SRC-5587371288-L000200](../../agents/intent_router.py#L200) | 200 | `"    normalized = _normalize(content)"` | — |
| [SRC-5587371288-L000201](../../agents/intent_router.py#L201) | 201 | `"    return any(marker in normalized for marker in ("` | — |
| [SRC-5587371288-L000202](../../agents/intent_router.py#L202) | 202 | `"        \"تقصد ايه تحديدا\", \"اكتب اسم الشيء\", \"ابعت الرابط\","` | — |
| [SRC-5587371288-L000203](../../agents/intent_router.py#L203) | 203 | `"        \"what are you referring to\", \"please name the item\","` | — |
| [SRC-5587371288-L000204](../../agents/intent_router.py#L204) | 204 | `"        \"share its link\", \"clarify what you mean\","` | — |
| [SRC-5587371288-L000205](../../agents/intent_router.py#L205) | 205 | `"    ))"` | — |
| [SRC-5587371288-L000206](../../agents/intent_router.py#L206) | 206 | `""` | — |
| [SRC-5587371288-L000207](../../agents/intent_router.py#L207) | 207 | `""` | — |
| [SRC-5587371288-L000208](../../agents/intent_router.py#L208) | 208 | `"def _latest_context_anchor(history: Any) -> str:"` | — |
| [SRC-5587371288-L000209](../../agents/intent_router.py#L209) | 209 | `"    \"\"\"Find the latest substantive user topic, skipping ellipsis follow-ups only."` | — |
| [SRC-5587371288-L000210](../../agents/intent_router.py#L210) | 210 | `""` | — |
| [SRC-5587371288-L000211](../../agents/intent_router.py#L211) | 211 | `"    A recent acknowledgment is a hard boundary: never search past it for stale topics."` | — |
| [SRC-5587371288-L000212](../../agents/intent_router.py#L212) | 212 | `"    Short entity replies can anchor context when the assistant explicitly asked for one."` | — |
| [SRC-5587371288-L000213](../../agents/intent_router.py#L213) | 213 | `"    \"\"\""` | — |
| [SRC-5587371288-L000214](../../agents/intent_router.py#L214) | 214 | `"    if not isinstance(history, list):"` | — |
| [SRC-5587371288-L000215](../../agents/intent_router.py#L215) | 215 | `"        return \"\""` | — |
| [SRC-5587371288-L000216](../../agents/intent_router.py#L216) | 216 | `"    bounded = history[-MAX_CONTEXT_TURNS:]"` | — |
| [SRC-5587371288-L000217](../../agents/intent_router.py#L217) | 217 | `"    for index in range(len(bounded) - 1, -1, -1):"` | — |
| [SRC-5587371288-L000218](../../agents/intent_router.py#L218) | 218 | `"        item = bounded[index]"` | — |
| [SRC-5587371288-L000219](../../agents/intent_router.py#L219) | 219 | `"        if not isinstance(item, dict) or item.get(\"role\") != \"user\":"` | — |
| [SRC-5587371288-L000220](../../agents/intent_router.py#L220) | 220 | `"            continue"` | — |
| [SRC-5587371288-L000221](../../agents/intent_router.py#L221) | 221 | `"        content = item.get(\"content\")"` | — |
| [SRC-5587371288-L000222](../../agents/intent_router.py#L222) | 222 | `"        if not isinstance(content, str):"` | — |
| [SRC-5587371288-L000223](../../agents/intent_router.py#L223) | 223 | `"            continue"` | — |
| [SRC-5587371288-L000224](../../agents/intent_router.py#L224) | 224 | `"        normalized = _normalize(content)"` | — |
| [SRC-5587371288-L000225](../../agents/intent_router.py#L225) | 225 | `"        if not normalized or _is_smalltalk(normalized):"` | — |
| [SRC-5587371288-L000226](../../agents/intent_router.py#L226) | 226 | `"            return \"\""` | — |
| [SRC-5587371288-L000227](../../agents/intent_router.py#L227) | 227 | `"        if _needs_clarification(content):"` | — |
| [SRC-5587371288-L000228](../../agents/intent_router.py#L228) | 228 | `"            continue"` | — |
| [SRC-5587371288-L000229](../../agents/intent_router.py#L229) | 229 | `"        meaningful = re.findall(r\"[a-z0-9]+\|[\\u0600-\\u06FF]+\", normalized)"` | — |
| [SRC-5587371288-L000230](../../agents/intent_router.py#L230) | 230 | `"        if len(meaningful) >= 2 and len(normalized) >= 8:"` | — |
| [SRC-5587371288-L000231](../../agents/intent_router.py#L231) | 231 | `"            return re.sub(r\"\\s+\", \" \", content).strip()[:300]"` | — |
| [SRC-5587371288-L000232](../../agents/intent_router.py#L232) | 232 | `"        if index > 0:"` | — |
| [SRC-5587371288-L000233](../../agents/intent_router.py#L233) | 233 | `"            previous = bounded[index - 1]"` | — |
| [SRC-5587371288-L000234](../../agents/intent_router.py#L234) | 234 | `"            if isinstance(previous, dict) and previous.get(\"role\") == \"assistant\" and _is_clarification_message(previous.get(\"content\")):"` | — |
| [SRC-5587371288-L000235](../../agents/intent_router.py#L235) | 235 | `"                return re.sub(r\"\\s+\", \" \", content).strip()[:120]"` | — |
| [SRC-5587371288-L000236](../../agents/intent_router.py#L236) | 236 | `"        return \"\""` | — |
| [SRC-5587371288-L000237](../../agents/intent_router.py#L237) | 237 | `"    return \"\""` | — |
| [SRC-5587371288-L000238](../../agents/intent_router.py#L238) | 238 | `""` | — |
| [SRC-5587371288-L000239](../../agents/intent_router.py#L239) | 239 | `""` | — |
| [SRC-5587371288-L000240](../../agents/intent_router.py#L240) | 240 | `"def _pending_clarification_query(history: Any) -> str:"` | — |
| [SRC-5587371288-L000241](../../agents/intent_router.py#L241) | 241 | `"    \"\"\"Return the unresolved elliptical question immediately awaiting a user slot-fill.\"\"\""` | — |
| [SRC-5587371288-L000242](../../agents/intent_router.py#L242) | 242 | `"    if not isinstance(history, list) or not history:"` | — |
| [SRC-5587371288-L000243](../../agents/intent_router.py#L243) | 243 | `"        return \"\""` | — |
| [SRC-5587371288-L000244](../../agents/intent_router.py#L244) | 244 | `"    last_index = len(history) - 1"` | — |
| [SRC-5587371288-L000245](../../agents/intent_router.py#L245) | 245 | `"    while last_index >= 0 and not ("` | — |
| [SRC-5587371288-L000246](../../agents/intent_router.py#L246) | 246 | `"        isinstance(history[last_index], dict)"` | — |
| [SRC-5587371288-L000247](../../agents/intent_router.py#L247) | 247 | `"        and isinstance(history[last_index].get(\"content\"), str)"` | — |
| [SRC-5587371288-L000248](../../agents/intent_router.py#L248) | 248 | `"        and history[last_index].get(\"content\", \"\").strip()"` | — |
| [SRC-5587371288-L000249](../../agents/intent_router.py#L249) | 249 | `"    ):"` | — |
| [SRC-5587371288-L000250](../../agents/intent_router.py#L250) | 250 | `"        last_index -= 1"` | — |
| [SRC-5587371288-L000251](../../agents/intent_router.py#L251) | 251 | `"    if last_index < 0 or history[last_index].get(\"role\") != \"assistant\":"` | — |
| [SRC-5587371288-L000252](../../agents/intent_router.py#L252) | 252 | `"        return \"\""` | — |
| [SRC-5587371288-L000253](../../agents/intent_router.py#L253) | 253 | `"    if not _is_clarification_message(history[last_index].get(\"content\")):"` | — |
| [SRC-5587371288-L000254](../../agents/intent_router.py#L254) | 254 | `"        return \"\""` | — |
| [SRC-5587371288-L000255](../../agents/intent_router.py#L255) | 255 | `"    for index in range(last_index - 1, -1, -1):"` | — |
| [SRC-5587371288-L000256](../../agents/intent_router.py#L256) | 256 | `"        item = history[index]"` | — |
| [SRC-5587371288-L000257](../../agents/intent_router.py#L257) | 257 | `"        if isinstance(item, dict) and item.get(\"role\") == \"user\":"` | — |
| [SRC-5587371288-L000258](../../agents/intent_router.py#L258) | 258 | `"            content = item.get(\"content\")"` | — |
| [SRC-5587371288-L000259](../../agents/intent_router.py#L259) | 259 | `"            if not isinstance(content, str) or not _needs_clarification(content):"` | — |
| [SRC-5587371288-L000260](../../agents/intent_router.py#L260) | 260 | `"                return \"\""` | — |
| [SRC-5587371288-L000261](../../agents/intent_router.py#L261) | 261 | `"            if _latest_context_anchor(history[:index]):"` | — |
| [SRC-5587371288-L000262](../../agents/intent_router.py#L262) | 262 | `"                return \"\""` | — |
| [SRC-5587371288-L000263](../../agents/intent_router.py#L263) | 263 | `"            return content.strip()[:180]"` | — |
| [SRC-5587371288-L000264](../../agents/intent_router.py#L264) | 264 | `"    return \"\""` | — |
| [SRC-5587371288-L000265](../../agents/intent_router.py#L265) | 265 | `""` | — |
| [SRC-5587371288-L000266](../../agents/intent_router.py#L266) | 266 | `""` | — |
| [SRC-5587371288-L000267](../../agents/intent_router.py#L267) | 267 | `"def _is_clarification_answer(question: str, history: Any) -> bool:"` | — |
| [SRC-5587371288-L000268](../../agents/intent_router.py#L268) | 268 | `"    \"\"\"Recognize a concise answer to Omarai's immediately preceding clarification.\"\"\""` | — |
| [SRC-5587371288-L000269](../../agents/intent_router.py#L269) | 269 | `"    if not _pending_clarification_query(history) or not isinstance(question, str):"` | — |
| [SRC-5587371288-L000270](../../agents/intent_router.py#L270) | 270 | `"        return False"` | — |
| [SRC-5587371288-L000271](../../agents/intent_router.py#L271) | 271 | `"    query = question.strip()"` | — |
| [SRC-5587371288-L000272](../../agents/intent_router.py#L272) | 272 | `"    if not query or len(query) >= 100 or _needs_clarification(query) or _is_smalltalk(query):"` | — |
| [SRC-5587371288-L000273](../../agents/intent_router.py#L273) | 273 | `"        return False"` | — |
| [SRC-5587371288-L000274](../../agents/intent_router.py#L274) | 274 | `"    # A self-contained live request should not be mistaken for a slot-fill."` | — |
| [SRC-5587371288-L000275](../../agents/intent_router.py#L275) | 275 | `"    return not (_has_live_signal(query) or re.search(r\"https?://\", query, re.IGNORECASE))"` | — |
| [SRC-5587371288-L000276](../../agents/intent_router.py#L276) | 276 | `""` | — |
| [SRC-5587371288-L000277](../../agents/intent_router.py#L277) | 277 | `""` | — |
| [SRC-5587371288-L000278](../../agents/intent_router.py#L278) | 278 | `"def _is_contextual_followup(question: str) -> bool:"` | — |
| [SRC-5587371288-L000279](../../agents/intent_router.py#L279) | 279 | `"    \"\"\"Detect short referent-dependent follow-ups without treating every 'okay' as one.\"\"\""` | — |
| [SRC-5587371288-L000280](../../agents/intent_router.py#L280) | 280 | `"    if not isinstance(question, str) or len(question.strip()) >= 100:"` | — |
| [SRC-5587371288-L000281](../../agents/intent_router.py#L281) | 281 | `"        return False"` | — |
| [SRC-5587371288-L000282](../../agents/intent_router.py#L282) | 282 | `"    if re.search(r\"https?://\", question, re.IGNORECASE):"` | — |
| [SRC-5587371288-L000283](../../agents/intent_router.py#L283) | 283 | `"        return False"` | — |
| [SRC-5587371288-L000284](../../agents/intent_router.py#L284) | 284 | `"    normalized = _strip_followup_leadin(_normalize(question))"` | — |
| [SRC-5587371288-L000285](../../agents/intent_router.py#L285) | 285 | `"    if _needs_clarification(question) or _starts_with_contextual_aspect(question):"` | — |
| [SRC-5587371288-L000286](../../agents/intent_router.py#L286) | 286 | `"        return True"` | — |
| [SRC-5587371288-L000287](../../agents/intent_router.py#L287) | 287 | `"    # Pronouns and deictic references are strong signals only in a short turn."` | — |
| [SRC-5587371288-L000288](../../agents/intent_router.py#L288) | 288 | `"    detached_reference = re.fullmatch("` | — |
| [SRC-5587371288-L000289](../../agents/intent_router.py#L289) | 289 | `"        r\"(?:و)?(?:هي\|هو\|دي\|ده\|دول\|هما\|ذلك\|تلك\|عليها\|عليه\|فيها\|فيه\|لها\|له\|\""` | — |
| [SRC-5587371288-L000290](../../agents/intent_router.py#L290) | 290 | `"        r\"سعرها\|سعره\|مكانها\|مكانه\|ضمانها\|ضمانه\|بطاريتها\|كاميرتها\|مميزاتها\|عيوبها)\","` | — |
| [SRC-5587371288-L000291](../../agents/intent_router.py#L291) | 291 | `"        normalized,"` | — |
| [SRC-5587371288-L000292](../../agents/intent_router.py#L292) | 292 | `"    )"` | — |
| [SRC-5587371288-L000293](../../agents/intent_router.py#L293) | 293 | `"    # Arabic often attaches object pronouns to verbs (e.g. \"أشتريه\", \"أستخدمها\")."` | — |
| [SRC-5587371288-L000294](../../agents/intent_router.py#L294) | 294 | `"    # These are easy to miss with whitespace-token pronoun lists."` | — |
| [SRC-5587371288-L000295](../../agents/intent_router.py#L295) | 295 | `"    attached_reference = re.search("` | — |
| [SRC-5587371288-L000296](../../agents/intent_router.py#L296) | 296 | `"        r\"\\b(?:استخدم\|اشتري\|اجيب\|اشغل\|افتح\|اصلح\|احط\|اجرب\|اربط\|اوصل\|اخد\|اخلي\|\""` | — |
| [SRC-5587371288-L000297](../../agents/intent_router.py#L297) | 297 | `"        r\"اركب\|انقل\|ادفع\|اطلب\|احجز)[\\u0600-\\u06FF]{0,18}(?:ه\|ها\|هم\|هما\|هن\|ك\|كم\|كن)\\b\","` | — |
| [SRC-5587371288-L000298](../../agents/intent_router.py#L298) | 298 | `"        normalized,"` | — |
| [SRC-5587371288-L000299](../../agents/intent_router.py#L299) | 299 | `"    )"` | — |
| [SRC-5587371288-L000300](../../agents/intent_router.py#L300) | 300 | `"    return bool(detached_reference or attached_reference)"` | — |
| [SRC-5587371288-L000301](../../agents/intent_router.py#L301) | 301 | `""` | — |
| [SRC-5587371288-L000302](../../agents/intent_router.py#L302) | 302 | `""` | — |
| [SRC-5587371288-L000303](../../agents/intent_router.py#L303) | 303 | `"def resolve_followup_query(question: str, history: Any = None) -> str:"` | — |
| [SRC-5587371288-L000304](../../agents/intent_router.py#L304) | 304 | `"    \"\"\"Resolve a short contextual follow-up against the nearest substantive topic."` | — |
| [SRC-5587371288-L000305](../../agents/intent_router.py#L305) | 305 | `""` | — |
| [SRC-5587371288-L000306](../../agents/intent_router.py#L306) | 306 | `"    Repeated follow-ups retain the original topic. An answer to an explicit"` | — |
| [SRC-5587371288-L000307](../../agents/intent_router.py#L307) | 307 | `"    clarification is joined to the pending question. New standalone questions are"` | — |
| [SRC-5587371288-L000308](../../agents/intent_router.py#L308) | 308 | `"    never merged merely because they start with 'طيب' or 'طب'."` | — |
| [SRC-5587371288-L000309](../../agents/intent_router.py#L309) | 309 | `"    \"\"\""` | — |
| [SRC-5587371288-L000310](../../agents/intent_router.py#L310) | 310 | `"    if not isinstance(question, str):"` | — |
| [SRC-5587371288-L000311](../../agents/intent_router.py#L311) | 311 | `"        return \"\""` | — |
| [SRC-5587371288-L000312](../../agents/intent_router.py#L312) | 312 | `"    query = re.sub(r\"\\s+\", \" \", question).strip()"` | — |
| [SRC-5587371288-L000313](../../agents/intent_router.py#L313) | 313 | `"    if not query:"` | — |
| [SRC-5587371288-L000314](../../agents/intent_router.py#L314) | 314 | `"        return \"\""` | — |
| [SRC-5587371288-L000315](../../agents/intent_router.py#L315) | 315 | `"    pending = _pending_clarification_query(history)"` | — |
| [SRC-5587371288-L000316](../../agents/intent_router.py#L316) | 316 | `"    if pending and _is_clarification_answer(query, history):"` | — |
| [SRC-5587371288-L000317](../../agents/intent_router.py#L317) | 317 | `"        return f\"{pending[:220]} — {query[:180]}\"[:500]"` | — |
| [SRC-5587371288-L000318](../../agents/intent_router.py#L318) | 318 | `"    if len(query) >= 100 or not isinstance(history, list):"` | — |
| [SRC-5587371288-L000319](../../agents/intent_router.py#L319) | 319 | `"        return query[:500]"` | — |
| [SRC-5587371288-L000320](../../agents/intent_router.py#L320) | 320 | `"    if not _is_contextual_followup(query):"` | — |
| [SRC-5587371288-L000321](../../agents/intent_router.py#L321) | 321 | `"        return query[:500]"` | — |
| [SRC-5587371288-L000322](../../agents/intent_router.py#L322) | 322 | `"    previous = _latest_context_anchor(history)"` | — |
| [SRC-5587371288-L000323](../../agents/intent_router.py#L323) | 323 | `"    if not previous:"` | — |
| [SRC-5587371288-L000324](../../agents/intent_router.py#L324) | 324 | `"        return query[:500]"` | — |
| [SRC-5587371288-L000325](../../agents/intent_router.py#L325) | 325 | `"    return f\"{previous[:300]} — {query[:180]}\"[:500]"` | — |
| [SRC-5587371288-L000326](../../agents/intent_router.py#L326) | 326 | `""` | — |
| [SRC-5587371288-L000327](../../agents/intent_router.py#L327) | 327 | `""` | — |
| [SRC-5587371288-L000328](../../agents/intent_router.py#L328) | 328 | `"def _has_explicit_source_request(question: str) -> bool:"` | — |
| [SRC-5587371288-L000329](../../agents/intent_router.py#L329) | 329 | `"    \"\"\"Recognize explicit requests for evidence/citations that require web-backed retrieval.\"\"\""` | — |
| [SRC-5587371288-L000330](../../agents/intent_router.py#L330) | 330 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000331](../../agents/intent_router.py#L331) | 331 | `"    markers = ("` | — |
| [SRC-5587371288-L000332](../../agents/intent_router.py#L332) | 332 | `"        \"اذكر مصادر\", \"اذكر المصدر\", \"مصادر موثوقة\", \"مصدر موثوق\","` | — |
| [SRC-5587371288-L000333](../../agents/intent_router.py#L333) | 333 | `"        \"مصادر رسمية\", \"مصادر حديثة\", \"مع مصادر\", \"مع المصادر\","` | — |
| [SRC-5587371288-L000334](../../agents/intent_router.py#L334) | 334 | `"        \"بالمصادر\", \"روابط المصادر\", \"ارفق المصادر\", \"أرفق المصادر\","` | — |
| [SRC-5587371288-L000335](../../agents/intent_router.py#L335) | 335 | `"        \"استشهد بمصادر\", \"وثق الاجابة\", \"وثق الإجابة\", \"المراجع\","` | — |
| [SRC-5587371288-L000336](../../agents/intent_router.py#L336) | 336 | `"        \"with sources\", \"cite sources\", \"trusted sources\", \"reliable sources\","` | — |
| [SRC-5587371288-L000337](../../agents/intent_router.py#L337) | 337 | `"        \"official sources\", \"include references\", \"with citations\","` | — |
| [SRC-5587371288-L000338](../../agents/intent_router.py#L338) | 338 | `"        \"source-backed\", \"cite your sources\","` | — |
| [SRC-5587371288-L000339](../../agents/intent_router.py#L339) | 339 | `"    )"` | — |
| [SRC-5587371288-L000340](../../agents/intent_router.py#L340) | 340 | `"    return any(_normalize(marker) in normalized for marker in markers)"` | — |
| [SRC-5587371288-L000341](../../agents/intent_router.py#L341) | 341 | `""` | — |
| [SRC-5587371288-L000342](../../agents/intent_router.py#L342) | 342 | `""` | — |
| [SRC-5587371288-L000343](../../agents/intent_router.py#L343) | 343 | `"def _is_deep(question: str) -> bool:"` | — |
| [SRC-5587371288-L000344](../../agents/intent_router.py#L344) | 344 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000345](../../agents/intent_router.py#L345) | 345 | `"    if any(_normalize(term) in normalized for term in _DEEP_TERMS):"` | — |
| [SRC-5587371288-L000346](../../agents/intent_router.py#L346) | 346 | `"        return True"` | — |
| [SRC-5587371288-L000347](../../agents/intent_router.py#L347) | 347 | `"    # Explicit multi-dimension comparisons need evidence from more than one angle."` | — |
| [SRC-5587371288-L000348](../../agents/intent_router.py#L348) | 348 | `"    dimensions = ("` | — |
| [SRC-5587371288-L000349](../../agents/intent_router.py#L349) | 349 | `"        \"السعر\", \"سعر\", \"بطاريه\", \"كاميرا\", \"اداء\", \"امان\", \"تكلفه\","` | — |
| [SRC-5587371288-L000350](../../agents/intent_router.py#L350) | 350 | `"        \"الصيانه\", \"الجوده\", \"المميزات\", \"العيوب\", \"الاراء\", \"المراجعات\","` | — |
| [SRC-5587371288-L000351](../../agents/intent_router.py#L351) | 351 | `"        \"price\", \"battery\", \"camera\", \"performance\", \"safety\", \"cost\","` | — |
| [SRC-5587371288-L000352](../../agents/intent_router.py#L352) | 352 | `"        \"maintenance\", \"quality\", \"features\", \"drawbacks\", \"reviews\","` | — |
| [SRC-5587371288-L000353](../../agents/intent_router.py#L353) | 353 | `"    )"` | — |
| [SRC-5587371288-L000354](../../agents/intent_router.py#L354) | 354 | `"    matched_dimensions = sum(1 for item in dimensions if _normalize(item) in normalized)"` | — |
| [SRC-5587371288-L000355](../../agents/intent_router.py#L355) | 355 | `"    return matched_dimensions >= 2 and any("` | — |
| [SRC-5587371288-L000356](../../agents/intent_router.py#L356) | 356 | `"        marker in normalized for marker in _MULTIPART_MARKERS"` | — |
| [SRC-5587371288-L000357](../../agents/intent_router.py#L357) | 357 | `"    )"` | — |
| [SRC-5587371288-L000358](../../agents/intent_router.py#L358) | 358 | `""` | — |
| [SRC-5587371288-L000359](../../agents/intent_router.py#L359) | 359 | `""` | — |
| [SRC-5587371288-L000360](../../agents/intent_router.py#L360) | 360 | `"def _is_page_summarization_request(question: str) -> bool:"` | — |
| [SRC-5587371288-L000361](../../agents/intent_router.py#L361) | 361 | `"    \"\"\"Recognize a request to summarize a specific web page or link.\"\"\""` | — |
| [SRC-5587371288-L000362](../../agents/intent_router.py#L362) | 362 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000363](../../agents/intent_router.py#L363) | 363 | `"    terms = (\"لخص\", \"تلخيص\", \"ملخص\", \"summarize\", \"summarise\", \"summary\")"` | — |
| [SRC-5587371288-L000364](../../agents/intent_router.py#L364) | 364 | `"    page_references = ("` | — |
| [SRC-5587371288-L000365](../../agents/intent_router.py#L365) | 365 | `"        \"صفحه\", \"الصفحه\", \"مقال\", \"المقال\", \"رابط\", \"لينك\", \"url\","` | — |
| [SRC-5587371288-L000366](../../agents/intent_router.py#L366) | 366 | `"        \"link\", \"article\", \"page\", \"webpage\", \"web page\", \"website\","` | — |
| [SRC-5587371288-L000367](../../agents/intent_router.py#L367) | 367 | `"    )"` | — |
| [SRC-5587371288-L000368](../../agents/intent_router.py#L368) | 368 | `"    return ("` | — |
| [SRC-5587371288-L000369](../../agents/intent_router.py#L369) | 369 | `"        any(_normalize(term) in normalized for term in terms)"` | — |
| [SRC-5587371288-L000370](../../agents/intent_router.py#L370) | 370 | `"        and ("` | — |
| [SRC-5587371288-L000371](../../agents/intent_router.py#L371) | 371 | `"            bool(re.search(r\"https?://\", question, flags=re.IGNORECASE))"` | — |
| [SRC-5587371288-L000372](../../agents/intent_router.py#L372) | 372 | `"            or any(_normalize(term) in normalized for term in page_references)"` | — |
| [SRC-5587371288-L000373](../../agents/intent_router.py#L373) | 373 | `"        )"` | — |
| [SRC-5587371288-L000374](../../agents/intent_router.py#L374) | 374 | `"    )"` | — |
| [SRC-5587371288-L000375](../../agents/intent_router.py#L375) | 375 | `""` | — |
| [SRC-5587371288-L000376](../../agents/intent_router.py#L376) | 376 | `""` | — |
| [SRC-5587371288-L000377](../../agents/intent_router.py#L377) | 377 | `"def _has_inline_summary_text(question: str) -> bool:"` | — |
| [SRC-5587371288-L000378](../../agents/intent_router.py#L378) | 378 | `"    \"\"\"Detect text explicitly pasted after a summary instruction, not a web page URL.\"\"\""` | — |
| [SRC-5587371288-L000379](../../agents/intent_router.py#L379) | 379 | `"    if re.search(r\"https?://\", question, flags=re.IGNORECASE):"` | — |
| [SRC-5587371288-L000380](../../agents/intent_router.py#L380) | 380 | `"        return False"` | — |
| [SRC-5587371288-L000381](../../agents/intent_router.py#L381) | 381 | `"    normalized = _normalize(question)"` | — |
| [SRC-5587371288-L000382](../../agents/intent_router.py#L382) | 382 | `"    markers = ("` | — |
| [SRC-5587371288-L000383](../../agents/intent_router.py#L383) | 383 | `"        \"النص التالي\", \"النص الاتي\", \"النص ده\", \"النص اللي جاي\","` | — |
| [SRC-5587371288-L000384](../../agents/intent_router.py#L384) | 384 | `"        \"this text\", \"following text\", \"the following text\", \"text below\","` | — |
| [SRC-5587371288-L000385](../../agents/intent_router.py#L385) | 385 | `"        \"text to summarize\", \"content below\","` | — |
| [SRC-5587371288-L000386](../../agents/intent_router.py#L386) | 386 | `"    )"` | — |
| [SRC-5587371288-L000387](../../agents/intent_router.py#L387) | 387 | `"    for marker in markers:"` | — |
| [SRC-5587371288-L000388](../../agents/intent_router.py#L388) | 388 | `"        normalized_marker = _normalize(marker)"` | — |
| [SRC-5587371288-L000389](../../agents/intent_router.py#L389) | 389 | `"        if normalized_marker in normalized:"` | — |
| [SRC-5587371288-L000390](../../agents/intent_router.py#L390) | 390 | `"            remainder = normalized.split(normalized_marker, 1)[1].strip()"` | — |
| [SRC-5587371288-L000391](../../agents/intent_router.py#L391) | 391 | `"            if len(remainder) >= 8:"` | — |
| [SRC-5587371288-L000392](../../agents/intent_router.py#L392) | 392 | `"                return True"` | — |
| [SRC-5587371288-L000393](../../agents/intent_router.py#L393) | 393 | `"    # Also allow a concise direct form such as \"لخص: [pasted paragraph]\"."` | — |
| [SRC-5587371288-L000394](../../agents/intent_router.py#L394) | 394 | `"    return bool("` | — |
| [SRC-5587371288-L000395](../../agents/intent_router.py#L395) | 395 | `"        re.search("` | — |
| [SRC-5587371288-L000396](../../agents/intent_router.py#L396) | 396 | `"            r\"^\\s*(?:لخص(?:\\s+لي)?\|تلخيص\|summari[sz]e\|summary)\\s*[:：]\\s*\\S.{12,}$\","` | — |
| [SRC-5587371288-L000397](../../agents/intent_router.py#L397) | 397 | `"            question,"` | — |
| [SRC-5587371288-L000398](../../agents/intent_router.py#L398) | 398 | `"            flags=re.IGNORECASE,"` | — |
| [SRC-5587371288-L000399](../../agents/intent_router.py#L399) | 399 | `"        )"` | — |
| [SRC-5587371288-L000400](../../agents/intent_router.py#L400) | 400 | `"    )"` | — |
| [SRC-5587371288-L000401](../../agents/intent_router.py#L401) | 401 | `""` | — |
| [SRC-5587371288-L000402](../../agents/intent_router.py#L402) | 402 | `""` | — |
| [SRC-5587371288-L000403](../../agents/intent_router.py#L403) | 403 | `"def route_intent("` | — |
| [SRC-5587371288-L000404](../../agents/intent_router.py#L404) | 404 | `"    question: str,"` | — |
| [SRC-5587371288-L000405](../../agents/intent_router.py#L405) | 405 | `"    history: Any = None,"` | — |
| [SRC-5587371288-L000406](../../agents/intent_router.py#L406) | 406 | `"    mode: str = \"auto\","` | — |
| [SRC-5587371288-L000407](../../agents/intent_router.py#L407) | 407 | `"    *,"` | — |
| [SRC-5587371288-L000408](../../agents/intent_router.py#L408) | 408 | `"    capability_question: bool = False,"` | — |
| [SRC-5587371288-L000409](../../agents/intent_router.py#L409) | 409 | `"    requires_web: bool = False,"` | — |
| [SRC-5587371288-L000410](../../agents/intent_router.py#L410) | 410 | `") -> dict[str, Any]:"` | — |
| [SRC-5587371288-L000411](../../agents/intent_router.py#L411) | 411 | `"    \"\"\"Return a deterministic route and auditable reason for a user question.\"\"\""` | — |
| [SRC-5587371288-L000412](../../agents/intent_router.py#L412) | 412 | `"    clean_mode = mode.strip().lower() if isinstance(mode, str) else \"auto\""` | — |
| [SRC-5587371288-L000413](../../agents/intent_router.py#L413) | 413 | `""` | — |
| [SRC-5587371288-L000414](../../agents/intent_router.py#L414) | 414 | `"    # If the assistant just asked for a missing referent, bind the user's concise"` | — |
| [SRC-5587371288-L000415](../../agents/intent_router.py#L415) | 415 | `"    # reply to that pending question instead of answering the entity name in isolation."` | — |
| [SRC-5587371288-L000416](../../agents/intent_router.py#L416) | 416 | `"    if _is_clarification_answer(question, history):"` | — |
| [SRC-5587371288-L000417](../../agents/intent_router.py#L417) | 417 | `"        return {"` | — |
| [SRC-5587371288-L000418](../../agents/intent_router.py#L418) | 418 | `"            \"route\": \"WEB_DEEP\" if clean_mode == \"deep\" else \"WEB_SIMPLE\","` | — |
| [SRC-5587371288-L000419](../../agents/intent_router.py#L419) | 419 | `"            \"reason\": \"answer_to_pending_clarification\","` | — |
| [SRC-5587371288-L000420](../../agents/intent_router.py#L420) | 420 | `"            \"context_available\": True,"` | — |
| [SRC-5587371288-L000421](../../agents/intent_router.py#L421) | 421 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000422](../../agents/intent_router.py#L422) | 422 | `"        }"` | — |
| [SRC-5587371288-L000423](../../agents/intent_router.py#L423) | 423 | `""` | — |
| [SRC-5587371288-L000424](../../agents/intent_router.py#L424) | 424 | `"    context_available = _has_context(history)"` | — |
| [SRC-5587371288-L000425](../../agents/intent_router.py#L425) | 425 | `""` | — |
| [SRC-5587371288-L000426](../../agents/intent_router.py#L426) | 426 | `"    # A search mode cannot supply a missing subject. Clarify genuinely elliptical"` | — |
| [SRC-5587371288-L000427](../../agents/intent_router.py#L427) | 427 | `"    # questions before honoring the UI's explicit research mode."` | — |
| [SRC-5587371288-L000428](../../agents/intent_router.py#L428) | 428 | `"    if _needs_clarification(question) and not context_available:"` | — |
| [SRC-5587371288-L000429](../../agents/intent_router.py#L429) | 429 | `"        return {"` | — |
| [SRC-5587371288-L000430](../../agents/intent_router.py#L430) | 430 | `"            \"route\": \"CLARIFY\","` | — |
| [SRC-5587371288-L000431](../../agents/intent_router.py#L431) | 431 | `"            \"reason\": \"missing_referent_and_no_conversation_context\","` | — |
| [SRC-5587371288-L000432](../../agents/intent_router.py#L432) | 432 | `"            \"context_available\": False,"` | — |
| [SRC-5587371288-L000433](../../agents/intent_router.py#L433) | 433 | `"            \"needs_clarification\": True,"` | — |
| [SRC-5587371288-L000434](../../agents/intent_router.py#L434) | 434 | `"        }"` | — |
| [SRC-5587371288-L000435](../../agents/intent_router.py#L435) | 435 | `""` | — |
| [SRC-5587371288-L000436](../../agents/intent_router.py#L436) | 436 | `"    # An explicitly selected mode controls research depth when the request itself"` | — |
| [SRC-5587371288-L000437](../../agents/intent_router.py#L437) | 437 | `"    # is sufficiently specified."` | — |
| [SRC-5587371288-L000438](../../agents/intent_router.py#L438) | 438 | `"    if clean_mode != \"auto\":"` | — |
| [SRC-5587371288-L000439](../../agents/intent_router.py#L439) | 439 | `"        route = \"WEB_DEEP\" if clean_mode == \"deep\" else \"WEB_SIMPLE\""` | — |
| [SRC-5587371288-L000440](../../agents/intent_router.py#L440) | 440 | `"        return {"` | — |
| [SRC-5587371288-L000441](../../agents/intent_router.py#L441) | 441 | `"            \"route\": route,"` | — |
| [SRC-5587371288-L000442](../../agents/intent_router.py#L442) | 442 | `"            \"reason\": \"explicit_mode\","` | — |
| [SRC-5587371288-L000443](../../agents/intent_router.py#L443) | 443 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000444](../../agents/intent_router.py#L444) | 444 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000445](../../agents/intent_router.py#L445) | 445 | `"        }"` | — |
| [SRC-5587371288-L000446](../../agents/intent_router.py#L446) | 446 | `""` | — |
| [SRC-5587371288-L000447](../../agents/intent_router.py#L447) | 447 | `"    if capability_question:"` | — |
| [SRC-5587371288-L000448](../../agents/intent_router.py#L448) | 448 | `"        return {"` | — |
| [SRC-5587371288-L000449](../../agents/intent_router.py#L449) | 449 | `"            \"route\": \"LOCAL\","` | — |
| [SRC-5587371288-L000450](../../agents/intent_router.py#L450) | 450 | `"            \"reason\": \"capability_question\","` | — |
| [SRC-5587371288-L000451](../../agents/intent_router.py#L451) | 451 | `"            \"context_available\": context_available,"` | — |
| [SRC-5587371288-L000452](../../agents/intent_router.py#L452) | 452 | `"            \"needs_clarification\": False,"` | — |
| [SRC-5587371288-L000453](../../agents/intent_router.py#L453) | 453 | `"        }"` | — |
| [SRC-5587371288-L000454](../../agents/intent_router.py#L454) | 454 | `""` | — |
| [SRC-5587371288-L000455](../../agents/intent_router.py#L455) | 455 | `"    if _is_smalltalk(question):"` | — |
| [SRC-5587371288-L000456](../../agents/intent_router.py#L456) | 456 | `"        return {"` | — |
