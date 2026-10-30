# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **003**
- سجلات الأسطر: **800**
- النطاق: SRC-7D6FC391EC-L000169 إلى SRC-59CF4B7DE8-L000153
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
| [SRC-5587371288-L000001](../../agents/intent_router.py#L1) | 1 | `"PLACEHOLDER_IR"` | — |
## الوكيل والمنطق

### FILE-C9CF9B54F8 — [agents/omarai.py](../../agents/omarai.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C9CF9B54F8-L000001](../../agents/omarai.py#L1) | 1 | `"\"\"\"Explainable Arabic lead-intent analysis and local SQLite storage.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000002](../../agents/omarai.py#L2) | 2 | `"from __future__ import annotations"` | — |
| [SRC-C9CF9B54F8-L000003](../../agents/omarai.py#L3) | 3 | `""` | — |
| [SRC-C9CF9B54F8-L000004](../../agents/omarai.py#L4) | 4 | `"import csv"` | — |
| [SRC-C9CF9B54F8-L000005](../../agents/omarai.py#L5) | 5 | `"import hashlib"` | — |
| [SRC-C9CF9B54F8-L000006](../../agents/omarai.py#L6) | 6 | `"import json"` | — |
| [SRC-C9CF9B54F8-L000007](../../agents/omarai.py#L7) | 7 | `"import re"` | — |
| [SRC-C9CF9B54F8-L000008](../../agents/omarai.py#L8) | 8 | `"import sqlite3"` | — |
| [SRC-C9CF9B54F8-L000009](../../agents/omarai.py#L9) | 9 | `"import unicodedata"` | — |
| [SRC-C9CF9B54F8-L000010](../../agents/omarai.py#L10) | 10 | `"from datetime import UTC, datetime"` | — |
| [SRC-C9CF9B54F8-L000011](../../agents/omarai.py#L11) | 11 | `"from pathlib import Path"` | — |
| [SRC-C9CF9B54F8-L000012](../../agents/omarai.py#L12) | 12 | `"from urllib.parse import urlparse"` | — |
| [SRC-C9CF9B54F8-L000013](../../agents/omarai.py#L13) | 13 | `""` | — |
| [SRC-C9CF9B54F8-L000014](../../agents/omarai.py#L14) | 14 | `"MAX_TEXT = 12000"` | — |
| [SRC-C9CF9B54F8-L000015](../../agents/omarai.py#L15) | 15 | `"_TRANSLATION = str.maketrans({\"أ\":\"ا\",\"إ\":\"ا\",\"آ\":\"ا\",\"ٱ\":\"ا\",\"ى\":\"ي\",\"ئ\":\"ي\",\"ؤ\":\"و\",\"ـ\":\"\"})"` | — |
| [SRC-C9CF9B54F8-L000016](../../agents/omarai.py#L16) | 16 | `"SIGNALS = {"` | — |
| [SRC-C9CF9B54F8-L000017](../../agents/omarai.py#L17) | 17 | `"    \"high\": (35, (\"عايز اشتري\", \"عاوز اشتري\", \"بدور على شقة\", \"بدور على عقار\", \"مطلوب شقة\", \"عايز وحدة\", \"محتاج اشتري\")),"` | — |
| [SRC-C9CF9B54F8-L000018](../../agents/omarai.py#L18) | 18 | `"    \"next_step\": (20, (\"ممكن معاينة\", \"عايز اعاين\", \"عاوز اعاين\", \"ابعت التفاصيل\", \"ابعت اللوكيشن\", \"ميعاد للمعاينة\")),"` | — |
| [SRC-C9CF9B54F8-L000019](../../agents/omarai.py#L19) | 19 | `"    \"budget\": (15, (\"السعر كام\", \"مقدم كام\", \"ميزانيتي\", \"معايا مقدم\", \"تقسيط\", \"على اقساط\", \"في حدود\")),"` | — |
| [SRC-C9CF9B54F8-L000020](../../agents/omarai.py#L20) | 20 | `"    \"explore\": (10, (\"بدور على\", \"فيه شقق\", \"ايه المتاح\", \"عايز اعرف الاسعار\")),"` | — |
| [SRC-C9CF9B54F8-L000021](../../agents/omarai.py#L21) | 21 | `"}"` | — |
| [SRC-C9CF9B54F8-L000022](../../agents/omarai.py#L22) | 22 | `"NOT_BUYER = (\"مش عايز اشتري\", \"مش عاوز اشتري\", \"عايز ابيع\", \"عاوز ابيع\", \"عندي شقة للبيع\", \"انا وسيط\", \"انا سمسار\", \"عايز ايجار\", \"للايجار\")"` | — |
| [SRC-C9CF9B54F8-L000023](../../agents/omarai.py#L23) | 23 | `""` | — |
| [SRC-C9CF9B54F8-L000024](../../agents/omarai.py#L24) | 24 | `"def normalize(text: str) -> str:"` | — |
| [SRC-C9CF9B54F8-L000025](../../agents/omarai.py#L25) | 25 | `"    value = unicodedata.normalize(\"NFKC\", str(text)).translate(_TRANSLATION)"` | — |
| [SRC-C9CF9B54F8-L000026](../../agents/omarai.py#L26) | 26 | `"    value = \"\".join(c for c in value if not unicodedata.category(c).startswith(\"M\"))"` | — |
| [SRC-C9CF9B54F8-L000027](../../agents/omarai.py#L27) | 27 | `"    return re.sub(r\"\\s+\", \" \", re.sub(r\"[^\\w\\s]\", \" \", value.casefold())).strip()"` | — |
| [SRC-C9CF9B54F8-L000028](../../agents/omarai.py#L28) | 28 | `""` | — |
| [SRC-C9CF9B54F8-L000029](../../agents/omarai.py#L29) | 29 | `"def now_utc() -> str:"` | — |
| [SRC-C9CF9B54F8-L000030](../../agents/omarai.py#L30) | 30 | `"    return datetime.now(UTC).isoformat(timespec=\"seconds\").replace(\"+00:00\", \"Z\")"` | — |
| [SRC-C9CF9B54F8-L000031](../../agents/omarai.py#L31) | 31 | `""` | — |
| [SRC-C9CF9B54F8-L000032](../../agents/omarai.py#L32) | 32 | `"def _csv_safe_cell(value: object) -> str:"` | — |
| [SRC-C9CF9B54F8-L000033](../../agents/omarai.py#L33) | 33 | `"    \"\"\"Prefix spreadsheet formulas even when hidden whitespace/control chars precede them.\"\"\""` | — |
| [SRC-C9CF9B54F8-L000034](../../agents/omarai.py#L34) | 34 | `"    text = \"\" if value is None else str(value)"` | — |
| [SRC-C9CF9B54F8-L000035](../../agents/omarai.py#L35) | 35 | `"    if not text:"` | — |
| [SRC-C9CF9B54F8-L000036](../../agents/omarai.py#L36) | 36 | `"        return text"` | — |
| [SRC-C9CF9B54F8-L000037](../../agents/omarai.py#L37) | 37 | `"    index = 0"` | — |
| [SRC-C9CF9B54F8-L000038](../../agents/omarai.py#L38) | 38 | `"    while index < len(text) and ("` | — |
| [SRC-C9CF9B54F8-L000039](../../agents/omarai.py#L39) | 39 | `"        text[index].isspace()"` | — |
| [SRC-C9CF9B54F8-L000040](../../agents/omarai.py#L40) | 40 | `"        or unicodedata.category(text[index]) in {\"Cc\", \"Cf\"}"` | — |
| [SRC-C9CF9B54F8-L000041](../../agents/omarai.py#L41) | 41 | `"    ):"` | — |
| [SRC-C9CF9B54F8-L000042](../../agents/omarai.py#L42) | 42 | `"        index += 1"` | — |
| [SRC-C9CF9B54F8-L000043](../../agents/omarai.py#L43) | 43 | `"    first_non_format = text[index:index + 1]"` | — |
| [SRC-C9CF9B54F8-L000044](../../agents/omarai.py#L44) | 44 | `"    formula_prefixes = {\"=\", \"+\", \"-\", \"@\", \"＝\", \"＋\", \"－\", \"＠\"}"` | — |
| [SRC-C9CF9B54F8-L000045](../../agents/omarai.py#L45) | 45 | `"    if text[0] in \"\\t\\r\\n\" or first_non_format in formula_prefixes:"` | — |
| [SRC-C9CF9B54F8-L000046](../../agents/omarai.py#L46) | 46 | `"        # OWASP notes that a tab inside the quoted CSV field is more resilient"` | — |
| [SRC-C9CF9B54F8-L000047](../../agents/omarai.py#L47) | 47 | `"        # in Excel than an apostrophe, although no CSV mitigation is universal."` | — |
| [SRC-C9CF9B54F8-L000048](../../agents/omarai.py#L48) | 48 | `"        return \"\\t\" + text"` | — |
| [SRC-C9CF9B54F8-L000049](../../agents/omarai.py#L49) | 49 | `"    return text"` | — |
| [SRC-C9CF9B54F8-L000050](../../agents/omarai.py#L50) | 50 | `""` | — |
| [SRC-C9CF9B54F8-L000051](../../agents/omarai.py#L51) | 51 | `"def analyze(text: str, product_terms=(), location_terms=()) -> dict:"` | — |
| [SRC-C9CF9B54F8-L000052](../../agents/omarai.py#L52) | 52 | `"    if not isinstance(text, str) or not text.strip():"` | — |
| [SRC-C9CF9B54F8-L000053](../../agents/omarai.py#L53) | 53 | `"        raise ValueError(\"text must not be empty\")"` | — |
| [SRC-C9CF9B54F8-L000054](../../agents/omarai.py#L54) | 54 | `"    if len(text) > MAX_TEXT:"` | — |
| [SRC-C9CF9B54F8-L000055](../../agents/omarai.py#L55) | 55 | `"        raise ValueError(f\"text must be at most {MAX_TEXT} characters\")"` | — |
| [SRC-C9CF9B54F8-L000056](../../agents/omarai.py#L56) | 56 | `"    body = normalize(text)"` | — |
| [SRC-C9CF9B54F8-L000057](../../agents/omarai.py#L57) | 57 | `"    excluded = [p for p in NOT_BUYER if normalize(p) in body]"` | — |
| [SRC-C9CF9B54F8-L000058](../../agents/omarai.py#L58) | 58 | `"    if excluded:"` | — |
| [SRC-C9CF9B54F8-L000059](../../agents/omarai.py#L59) | 59 | `"        return {\"score\": 0, \"label\": \"not_buyer_signal\", \"summary\": \"قد لا تكون إشارة شراء مباشرة؛ راجع النص يدويًا.\", \"matched_signals\": [{\"phrase\": p, \"category\": \"exclusion\", \"points\": 0} for p in excluded], \"warnings\": [\"تصنيف أولي وليس حكمًا نهائيًا.\"]}"` | — |
| [SRC-C9CF9B54F8-L000060](../../agents/omarai.py#L60) | 60 | `"    matches = []"` | — |
| [SRC-C9CF9B54F8-L000061](../../agents/omarai.py#L61) | 61 | `"    for category, (points, phrases) in SIGNALS.items():"` | — |
| [SRC-C9CF9B54F8-L000062](../../agents/omarai.py#L62) | 62 | `"        found = next((p for p in phrases if normalize(p) in body), None)"` | — |
| [SRC-C9CF9B54F8-L000063](../../agents/omarai.py#L63) | 63 | `"        if found:"` | — |
| [SRC-C9CF9B54F8-L000064](../../agents/omarai.py#L64) | 64 | `"            matches.append({\"phrase\": found, \"category\": category, \"points\": points})"` | — |
| [SRC-C9CF9B54F8-L000065](../../agents/omarai.py#L65) | 65 | `"    for category, terms in ((\"product_context\", product_terms), (\"location_context\", location_terms)):"` | — |
| [SRC-C9CF9B54F8-L000066](../../agents/omarai.py#L66) | 66 | `"        found = next((normalize(t) for t in terms if isinstance(t, str) and normalize(t) and normalize(t) in body), None)"` | — |
| [SRC-C9CF9B54F8-L000067](../../agents/omarai.py#L67) | 67 | `"        if found:"` | — |
| [SRC-C9CF9B54F8-L000068](../../agents/omarai.py#L68) | 68 | `"            matches.append({\"phrase\": found, \"category\": category, \"points\": 10})"` | — |
| [SRC-C9CF9B54F8-L000069](../../agents/omarai.py#L69) | 69 | `"    score = min(100, sum(x[\"points\"] for x in matches))"` | — |
| [SRC-C9CF9B54F8-L000070](../../agents/omarai.py#L70) | 70 | `"    label = \"high_intent\" if score >= 55 and any(x[\"category\"] == \"high\" for x in matches) else \"medium_intent\" if score >= 40 else \"early_research\" if score >= 20 else \"unclear\""` | — |
| [SRC-C9CF9B54F8-L000071](../../agents/omarai.py#L71) | 71 | `"    return {\"score\": score, \"label\": label, \"summary\": {\"high_intent\":\"إشارة قوية نسبيًا وفق قواعد بسيطة وتحتاج مراجعة بشرية.\",\"medium_intent\":\"مؤشرات اهتمام تستحق التأهيل والتحقق.\",\"early_research\":\"اهتمام مبكر؛ ليس عميلًا مؤهلًا بعد.\",\"unclear\":\"لا توجد مؤشرات كافية.\"}[label], \"matched_signals\": matches, \"warnings\": [\"الدرجة ليست احتمالًا إحصائيًا للشراء.\", \"لا تثبت هوية الكاتب أو قدرته على الدفع أو نيته.\", \"استخدم مصادر عامة ومسموحًا بمعالجتها فقط.\"]}"` | — |
| [SRC-C9CF9B54F8-L000072](../../agents/omarai.py#L72) | 72 | `""` | — |
| [SRC-C9CF9B54F8-L000073](../../agents/omarai.py#L73) | 73 | `"def validate_url(url: str) -> str:"` | — |
| [SRC-C9CF9B54F8-L000074](../../agents/omarai.py#L74) | 74 | `"    parsed = urlparse(str(url or \"\").strip())"` | — |
| [SRC-C9CF9B54F8-L000075](../../agents/omarai.py#L75) | 75 | `"    if parsed.scheme not in (\"http\", \"https\") or not parsed.netloc or parsed.username or parsed.password:"` | — |
| [SRC-C9CF9B54F8-L000076](../../agents/omarai.py#L76) | 76 | `"        raise ValueError(\"source_url must be an absolute http(s) URL without embedded credentials\")"` | — |
| [SRC-C9CF9B54F8-L000077](../../agents/omarai.py#L77) | 77 | `"    if len(url) > 2048:"` | — |
| [SRC-C9CF9B54F8-L000078](../../agents/omarai.py#L78) | 78 | `"        raise ValueError(\"source_url is too long\")"` | — |
| [SRC-C9CF9B54F8-L000079](../../agents/omarai.py#L79) | 79 | `"    return url.strip()"` | — |
| [SRC-C9CF9B54F8-L000080](../../agents/omarai.py#L80) | 80 | `""` | — |
| [SRC-C9CF9B54F8-L000081](../../agents/omarai.py#L81) | 81 | `"class LeadStore:"` | — |
| [SRC-C9CF9B54F8-L000082](../../agents/omarai.py#L82) | 82 | `"    def __init__(self, path: str \| Path \| None = None):"` | — |
| [SRC-C9CF9B54F8-L000083](../../agents/omarai.py#L83) | 83 | `"        self.path = Path(path or Path.home()/\".omarai\"/\"omarai.sqlite3\").expanduser()"` | — |
| [SRC-C9CF9B54F8-L000084](../../agents/omarai.py#L84) | 84 | `"        self.path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-C9CF9B54F8-L000085](../../agents/omarai.py#L85) | 85 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000086](../../agents/omarai.py#L86) | 86 | `"            db.execute(\"\"\"CREATE TABLE IF NOT EXISTS leads ("` | — |
| [SRC-C9CF9B54F8-L000087](../../agents/omarai.py#L87) | 87 | `"            id TEXT PRIMARY KEY, fingerprint TEXT UNIQUE NOT NULL, text TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000088](../../agents/omarai.py#L88) | 88 | `"            source_url TEXT NOT NULL, platform TEXT NOT NULL, observed_at TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000089](../../agents/omarai.py#L89) | 89 | `"            assessment TEXT NOT NULL, status TEXT NOT NULL, note TEXT NOT NULL,"` | — |
| [SRC-C9CF9B54F8-L000090](../../agents/omarai.py#L90) | 90 | `"            created_at TEXT NOT NULL, updated_at TEXT NOT NULL)\"\"\")"` | — |
| [SRC-C9CF9B54F8-L000091](../../agents/omarai.py#L91) | 91 | `"            db.execute(\"CREATE INDEX IF NOT EXISTS leads_status_idx ON leads(status, created_at DESC)\")"` | — |
| [SRC-C9CF9B54F8-L000092](../../agents/omarai.py#L92) | 92 | `"    def connect(self):"` | — |
| [SRC-C9CF9B54F8-L000093](../../agents/omarai.py#L93) | 93 | `"        db = sqlite3.connect(self.path, timeout=10)"` | — |
| [SRC-C9CF9B54F8-L000094](../../agents/omarai.py#L94) | 94 | `"        db.row_factory = sqlite3.Row"` | — |
| [SRC-C9CF9B54F8-L000095](../../agents/omarai.py#L95) | 95 | `"        return db"` | — |
| [SRC-C9CF9B54F8-L000096](../../agents/omarai.py#L96) | 96 | `"    def add(self, text: str, source_url: str, platform: str=\"manual\", observed_at: str \| None=None, note: str=\"\", product_terms=(), location_terms=()):"` | — |
| [SRC-C9CF9B54F8-L000097](../../agents/omarai.py#L97) | 97 | `"        if not isinstance(text, str) or not text.strip():"` | — |
| [SRC-C9CF9B54F8-L000098](../../agents/omarai.py#L98) | 98 | `"            raise ValueError(\"text is required\")"` | — |
| [SRC-C9CF9B54F8-L000099](../../agents/omarai.py#L99) | 99 | `"        if len(text) > MAX_TEXT:"` | — |
| [SRC-C9CF9B54F8-L000100](../../agents/omarai.py#L100) | 100 | `"            raise ValueError(\"text is too long\")"` | — |
| [SRC-C9CF9B54F8-L000101](../../agents/omarai.py#L101) | 101 | `"        url = validate_url(source_url)"` | — |
| [SRC-C9CF9B54F8-L000102](../../agents/omarai.py#L102) | 102 | `"        normalized = normalize(text)"` | — |
| [SRC-C9CF9B54F8-L000103](../../agents/omarai.py#L103) | 103 | `"        fingerprint = hashlib.sha256((url.rstrip(\"/\") + \"\\n\" + normalized).encode()).hexdigest()"` | — |
| [SRC-C9CF9B54F8-L000104](../../agents/omarai.py#L104) | 104 | `"        lead_id = fingerprint[:24]"` | — |
| [SRC-C9CF9B54F8-L000105](../../agents/omarai.py#L105) | 105 | `"        timestamp = observed_at or now_utc()"` | — |
| [SRC-C9CF9B54F8-L000106](../../agents/omarai.py#L106) | 106 | `"        assessment = analyze(text, product_terms=product_terms, location_terms=location_terms)"` | — |
| [SRC-C9CF9B54F8-L000107](../../agents/omarai.py#L107) | 107 | `"        now = now_utc()"` | — |
| [SRC-C9CF9B54F8-L000108](../../agents/omarai.py#L108) | 108 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000109](../../agents/omarai.py#L109) | 109 | `"            cursor = db.execute(\"\"\"INSERT OR IGNORE INTO leads"` | — |
| [SRC-C9CF9B54F8-L000110](../../agents/omarai.py#L110) | 110 | `"            (id,fingerprint,text,source_url,platform,observed_at,assessment,status,note,created_at,updated_at)"` | — |
| [SRC-C9CF9B54F8-L000111](../../agents/omarai.py#L111) | 111 | `"            VALUES(?,?,?,?,?,?,?,?,?,?,?)\"\"\", (lead_id,fingerprint,text.strip(),url,str(platform)[:80],timestamp,json.dumps(assessment,ensure_ascii=False),\"new\",str(note)[:1000],now,now))"` | — |
| [SRC-C9CF9B54F8-L000112](../../agents/omarai.py#L112) | 112 | `"            row = db.execute(\"SELECT * FROM leads WHERE id=?\", (lead_id,)).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000113](../../agents/omarai.py#L113) | 113 | `"        return self.to_dict(row), cursor.rowcount == 1"` | — |
| [SRC-C9CF9B54F8-L000114](../../agents/omarai.py#L114) | 114 | `"    @staticmethod"` | — |
| [SRC-C9CF9B54F8-L000115](../../agents/omarai.py#L115) | 115 | `"    def to_dict(row):"` | — |
| [SRC-C9CF9B54F8-L000116](../../agents/omarai.py#L116) | 116 | `"        item = dict(row)"` | — |
| [SRC-C9CF9B54F8-L000117](../../agents/omarai.py#L117) | 117 | `"        item[\"assessment\"] = json.loads(item[\"assessment\"])"` | — |
| [SRC-C9CF9B54F8-L000118](../../agents/omarai.py#L118) | 118 | `"        return item"` | — |
| [SRC-C9CF9B54F8-L000119](../../agents/omarai.py#L119) | 119 | `"    def list(self, status: str \| None=None, limit: int=100):"` | — |
| [SRC-C9CF9B54F8-L000120](../../agents/omarai.py#L120) | 120 | `"        limit = max(1,min(int(limit),500))"` | — |
| [SRC-C9CF9B54F8-L000121](../../agents/omarai.py#L121) | 121 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000122](../../agents/omarai.py#L122) | 122 | `"            rows = db.execute(\"SELECT * FROM leads WHERE (? IS NULL OR status=?) ORDER BY created_at DESC LIMIT ?\",(status,status,limit)).fetchall()"` | — |
| [SRC-C9CF9B54F8-L000123](../../agents/omarai.py#L123) | 123 | `"        return [self.to_dict(r) for r in rows]"` | — |
| [SRC-C9CF9B54F8-L000124](../../agents/omarai.py#L124) | 124 | `"    def update_status(self, lead_id: str, status: str):"` | — |
| [SRC-C9CF9B54F8-L000125](../../agents/omarai.py#L125) | 125 | `"        allowed={\"new\",\"qualified\",\"contacted\",\"converted\",\"rejected\",\"needs_review\"}"` | — |
| [SRC-C9CF9B54F8-L000126](../../agents/omarai.py#L126) | 126 | `"        if status not in allowed:"` | — |
| [SRC-C9CF9B54F8-L000127](../../agents/omarai.py#L127) | 127 | `"            raise ValueError(\"unsupported status\")"` | — |
| [SRC-C9CF9B54F8-L000128](../../agents/omarai.py#L128) | 128 | `"        with self.connect() as db:"` | — |
| [SRC-C9CF9B54F8-L000129](../../agents/omarai.py#L129) | 129 | `"            db.execute(\"UPDATE leads SET status=?,updated_at=? WHERE id=?\",(status,now_utc(),lead_id))"` | — |
| [SRC-C9CF9B54F8-L000130](../../agents/omarai.py#L130) | 130 | `"            row=db.execute(\"SELECT * FROM leads WHERE id=?\",(lead_id,)).fetchone()"` | — |
| [SRC-C9CF9B54F8-L000131](../../agents/omarai.py#L131) | 131 | `"        return self.to_dict(row) if row else None"` | — |
| [SRC-C9CF9B54F8-L000132](../../agents/omarai.py#L132) | 132 | `"    def import_csv(self, filename: str):"` | — |
| [SRC-C9CF9B54F8-L000133](../../agents/omarai.py#L133) | 133 | `"        results={\"created\":0,\"duplicates\":0,\"errors\":[]}"` | — |
| [SRC-C9CF9B54F8-L000134](../../agents/omarai.py#L134) | 134 | `"        with open(filename, newline=\"\", encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-C9CF9B54F8-L000135](../../agents/omarai.py#L135) | 135 | `"            reader=csv.DictReader(stream)"` | — |
| [SRC-C9CF9B54F8-L000136](../../agents/omarai.py#L136) | 136 | `"            required={\"text\",\"source_url\",\"platform\"}"` | — |
| [SRC-C9CF9B54F8-L000137](../../agents/omarai.py#L137) | 137 | `"            if not reader.fieldnames or not required.issubset(reader.fieldnames):"` | — |
| [SRC-C9CF9B54F8-L000138](../../agents/omarai.py#L138) | 138 | `"                raise ValueError(\"CSV must contain text,source_url,platform columns\")"` | — |
| [SRC-C9CF9B54F8-L000139](../../agents/omarai.py#L139) | 139 | `"            for line,row in enumerate(reader,2):"` | — |
| [SRC-C9CF9B54F8-L000140](../../agents/omarai.py#L140) | 140 | `"                try:"` | — |
| [SRC-C9CF9B54F8-L000141](../../agents/omarai.py#L141) | 141 | `"                    _,created=self.add(row[\"text\"],row[\"source_url\"],row[\"platform\"],row.get(\"observed_at\") or None,row.get(\"note\") or \"\")"` | — |
| [SRC-C9CF9B54F8-L000142](../../agents/omarai.py#L142) | 142 | `"                    results[\"created\" if created else \"duplicates\"] += 1"` | — |
| [SRC-C9CF9B54F8-L000143](../../agents/omarai.py#L143) | 143 | `"                except (ValueError, TypeError) as exc:"` | — |
| [SRC-C9CF9B54F8-L000144](../../agents/omarai.py#L144) | 144 | `"                    results[\"errors\"].append({\"line\":line,\"error\":str(exc)})"` | — |
| [SRC-C9CF9B54F8-L000145](../../agents/omarai.py#L145) | 145 | `"        return results"` | — |
| [SRC-C9CF9B54F8-L000146](../../agents/omarai.py#L146) | 146 | `"    def export_csv(self, filename: str):"` | — |
| [SRC-C9CF9B54F8-L000147](../../agents/omarai.py#L147) | 147 | `"        rows=self.list(limit=500)"` | — |
| [SRC-C9CF9B54F8-L000148](../../agents/omarai.py#L148) | 148 | `"        with open(filename,\"w\",newline=\"\",encoding=\"utf-8-sig\") as stream:"` | — |
| [SRC-C9CF9B54F8-L000149](../../agents/omarai.py#L149) | 149 | `"            fields=[\"id\",\"text\",\"source_url\",\"platform\",\"observed_at\",\"assessment\",\"status\",\"note\",\"created_at\"]"` | — |
| [SRC-C9CF9B54F8-L000150](../../agents/omarai.py#L150) | 150 | `"            writer=csv.DictWriter(stream, fieldnames=fields, quoting=csv.QUOTE_ALL)"` | — |
| [SRC-C9CF9B54F8-L000151](../../agents/omarai.py#L151) | 151 | `"            writer.writeheader()"` | — |
| [SRC-C9CF9B54F8-L000152](../../agents/omarai.py#L152) | 152 | `"            for row in rows:"` | — |
| [SRC-C9CF9B54F8-L000153](../../agents/omarai.py#L153) | 153 | `"                values = {"` | — |
| [SRC-C9CF9B54F8-L000154](../../agents/omarai.py#L154) | 154 | `"                    key: json.dumps(row[key], ensure_ascii=False)"` | — |
| [SRC-C9CF9B54F8-L000155](../../agents/omarai.py#L155) | 155 | `"                    if key == \"assessment\""` | — |
| [SRC-C9CF9B54F8-L000156](../../agents/omarai.py#L156) | 156 | `"                    else row.get(key, \"\")"` | — |
| [SRC-C9CF9B54F8-L000157](../../agents/omarai.py#L157) | 157 | `"                    for key in fields"` | — |
| [SRC-C9CF9B54F8-L000158](../../agents/omarai.py#L158) | 158 | `"                }"` | — |
| [SRC-C9CF9B54F8-L000159](../../agents/omarai.py#L159) | 159 | `"                writer.writerow({key: _csv_safe_cell(value) for key, value in values.items()})"` | — |
| [SRC-C9CF9B54F8-L000160](../../agents/omarai.py#L160) | 160 | `"        return len(rows)"` | — |
## الوكيل والمنطق

### FILE-FDEEAFDFCA — [agents/request_budget.py](../../agents/request_budget.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-FDEEAFDFCA-L000001](../../agents/request_budget.py#L1) | 1 | `"\"\"\"Cooperative per-request resource budgets for Omarai's web-research pipeline."` | — |
| [SRC-FDEEAFDFCA-L000002](../../agents/request_budget.py#L2) | 2 | `""` | — |
| [SRC-FDEEAFDFCA-L000003](../../agents/request_budget.py#L3) | 3 | `"The budget limits work that has not started yet and caps the timeout supplied to"` | — |
| [SRC-FDEEAFDFCA-L000004](../../agents/request_budget.py#L4) | 4 | `"each outbound operation by the remaining request window. Socket libraries may"` | — |
| [SRC-FDEEAFDFCA-L000005](../../agents/request_budget.py#L5) | 5 | `"still overrun a cooperative deadline slightly while unwinding an in-flight call;"` | — |
| [SRC-FDEEAFDFCA-L000006](../../agents/request_budget.py#L6) | 6 | `"this is not a hard real-time cancellation primitive."` | — |
| [SRC-FDEEAFDFCA-L000007](../../agents/request_budget.py#L7) | 7 | `"\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000008](../../agents/request_budget.py#L8) | 8 | `"from __future__ import annotations"` | — |
| [SRC-FDEEAFDFCA-L000009](../../agents/request_budget.py#L9) | 9 | `""` | — |
| [SRC-FDEEAFDFCA-L000010](../../agents/request_budget.py#L10) | 10 | `"import os"` | — |
| [SRC-FDEEAFDFCA-L000011](../../agents/request_budget.py#L11) | 11 | `"import threading"` | — |
| [SRC-FDEEAFDFCA-L000012](../../agents/request_budget.py#L12) | 12 | `"import time"` | — |
| [SRC-FDEEAFDFCA-L000013](../../agents/request_budget.py#L13) | 13 | `"from collections.abc import Callable, Mapping"` | — |
| [SRC-FDEEAFDFCA-L000014](../../agents/request_budget.py#L14) | 14 | `"from typing import Any"` | — |
| [SRC-FDEEAFDFCA-L000015](../../agents/request_budget.py#L15) | 15 | `""` | — |
| [SRC-FDEEAFDFCA-L000016](../../agents/request_budget.py#L16) | 16 | `""` | — |
| [SRC-FDEEAFDFCA-L000017](../../agents/request_budget.py#L17) | 17 | `"class RequestBudgetExceeded(Exception):"` | — |
| [SRC-FDEEAFDFCA-L000018](../../agents/request_budget.py#L18) | 18 | `"    \"\"\"Raised when a request cannot start more work within its resource budget.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000019](../../agents/request_budget.py#L19) | 19 | `""` | — |
| [SRC-FDEEAFDFCA-L000020](../../agents/request_budget.py#L20) | 20 | `""` | — |
| [SRC-FDEEAFDFCA-L000021](../../agents/request_budget.py#L21) | 21 | `"DEFAULT_TIMEOUT_SECONDS = 90"` | — |
| [SRC-FDEEAFDFCA-L000022](../../agents/request_budget.py#L22) | 22 | `"MAX_TIMEOUT_SECONDS = 120"` | — |
| [SRC-FDEEAFDFCA-L000023](../../agents/request_budget.py#L23) | 23 | `"RESOURCE_LIMITS = {"` | — |
| [SRC-FDEEAFDFCA-L000024](../../agents/request_budget.py#L24) | 24 | `"    \"search_queries\": (8, 8),"` | — |
| [SRC-FDEEAFDFCA-L000025](../../agents/request_budget.py#L25) | 25 | `"    \"search_calls\": (32, 40),"` | — |
| [SRC-FDEEAFDFCA-L000026](../../agents/request_budget.py#L26) | 26 | `"    \"model_calls\": (8, 12),"` | — |
| [SRC-FDEEAFDFCA-L000027](../../agents/request_budget.py#L27) | 27 | `"    \"page_fetches\": (8, 8),"` | — |
| [SRC-FDEEAFDFCA-L000028](../../agents/request_budget.py#L28) | 28 | `"    \"tool_calls\": (3, 3),"` | — |
| [SRC-FDEEAFDFCA-L000029](../../agents/request_budget.py#L29) | 29 | `"}"` | — |
| [SRC-FDEEAFDFCA-L000030](../../agents/request_budget.py#L30) | 30 | `""` | — |
| [SRC-FDEEAFDFCA-L000031](../../agents/request_budget.py#L31) | 31 | `""` | — |
| [SRC-FDEEAFDFCA-L000032](../../agents/request_budget.py#L32) | 32 | `"def _bounded_env_int(name: str, default: int, minimum: int, maximum: int) -> int:"` | — |
| [SRC-FDEEAFDFCA-L000033](../../agents/request_budget.py#L33) | 33 | `"    raw = os.getenv(name, \"\").strip()"` | — |
| [SRC-FDEEAFDFCA-L000034](../../agents/request_budget.py#L34) | 34 | `"    try:"` | — |
| [SRC-FDEEAFDFCA-L000035](../../agents/request_budget.py#L35) | 35 | `"        value = int(raw) if raw else default"` | — |
| [SRC-FDEEAFDFCA-L000036](../../agents/request_budget.py#L36) | 36 | `"    except (TypeError, ValueError):"` | — |
| [SRC-FDEEAFDFCA-L000037](../../agents/request_budget.py#L37) | 37 | `"        value = default"` | — |
| [SRC-FDEEAFDFCA-L000038](../../agents/request_budget.py#L38) | 38 | `"    return max(minimum, min(value, maximum))"` | — |
| [SRC-FDEEAFDFCA-L000039](../../agents/request_budget.py#L39) | 39 | `""` | — |
| [SRC-FDEEAFDFCA-L000040](../../agents/request_budget.py#L40) | 40 | `""` | — |
| [SRC-FDEEAFDFCA-L000041](../../agents/request_budget.py#L41) | 41 | `"class RequestBudget:"` | — |
| [SRC-FDEEAFDFCA-L000042](../../agents/request_budget.py#L42) | 42 | `"    \"\"\"Thread-safe counters and a cooperative monotonic deadline for one answer.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000043](../../agents/request_budget.py#L43) | 43 | `""` | — |
| [SRC-FDEEAFDFCA-L000044](../../agents/request_budget.py#L44) | 44 | `"    def __init__("` | — |
| [SRC-FDEEAFDFCA-L000045](../../agents/request_budget.py#L45) | 45 | `"        self,"` | — |
| [SRC-FDEEAFDFCA-L000046](../../agents/request_budget.py#L46) | 46 | `"        timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,"` | — |
| [SRC-FDEEAFDFCA-L000047](../../agents/request_budget.py#L47) | 47 | `"        limits: Mapping[str, int] \| None = None,"` | — |
| [SRC-FDEEAFDFCA-L000048](../../agents/request_budget.py#L48) | 48 | `"        clock: Callable[[], float] = time.monotonic,"` | — |
| [SRC-FDEEAFDFCA-L000049](../../agents/request_budget.py#L49) | 49 | `"    ) -> None:"` | — |
| [SRC-FDEEAFDFCA-L000050](../../agents/request_budget.py#L50) | 50 | `"        self._clock = clock"` | — |
| [SRC-FDEEAFDFCA-L000051](../../agents/request_budget.py#L51) | 51 | `"        bounded_timeout = max(10, min(int(timeout_seconds), MAX_TIMEOUT_SECONDS))"` | — |
| [SRC-FDEEAFDFCA-L000052](../../agents/request_budget.py#L52) | 52 | `"        self.started_at = clock()"` | — |
| [SRC-FDEEAFDFCA-L000053](../../agents/request_budget.py#L53) | 53 | `"        self.deadline = self.started_at + bounded_timeout"` | — |
| [SRC-FDEEAFDFCA-L000054](../../agents/request_budget.py#L54) | 54 | `"        self._limits = {"` | — |
| [SRC-FDEEAFDFCA-L000055](../../agents/request_budget.py#L55) | 55 | `"            key: max(0, min(int(value), RESOURCE_LIMITS[key][1]))"` | — |
| [SRC-FDEEAFDFCA-L000056](../../agents/request_budget.py#L56) | 56 | `"            for key, (default, _maximum) in RESOURCE_LIMITS.items()"` | — |
| [SRC-FDEEAFDFCA-L000057](../../agents/request_budget.py#L57) | 57 | `"            for value in [limits[key] if limits and key in limits else default]"` | — |
| [SRC-FDEEAFDFCA-L000058](../../agents/request_budget.py#L58) | 58 | `"        }"` | — |
| [SRC-FDEEAFDFCA-L000059](../../agents/request_budget.py#L59) | 59 | `"        self._counts = {key: 0 for key in self._limits}"` | — |
| [SRC-FDEEAFDFCA-L000060](../../agents/request_budget.py#L60) | 60 | `"        self._exhausted_reasons: set[str] = set()"` | — |
| [SRC-FDEEAFDFCA-L000061](../../agents/request_budget.py#L61) | 61 | `"        self._lock = threading.Lock()"` | — |
| [SRC-FDEEAFDFCA-L000062](../../agents/request_budget.py#L62) | 62 | `""` | — |
| [SRC-FDEEAFDFCA-L000063](../../agents/request_budget.py#L63) | 63 | `"    @classmethod"` | — |
| [SRC-FDEEAFDFCA-L000064](../../agents/request_budget.py#L64) | 64 | `"    def from_environment(cls) -> RequestBudget:"` | — |
| [SRC-FDEEAFDFCA-L000065](../../agents/request_budget.py#L65) | 65 | `"        timeout = _bounded_env_int("` | — |
| [SRC-FDEEAFDFCA-L000066](../../agents/request_budget.py#L66) | 66 | `"            \"OMARAI_REQUEST_BUDGET_SECONDS\","` | — |
| [SRC-FDEEAFDFCA-L000067](../../agents/request_budget.py#L67) | 67 | `"            DEFAULT_TIMEOUT_SECONDS,"` | — |
| [SRC-FDEEAFDFCA-L000068](../../agents/request_budget.py#L68) | 68 | `"            10,"` | — |
| [SRC-FDEEAFDFCA-L000069](../../agents/request_budget.py#L69) | 69 | `"            MAX_TIMEOUT_SECONDS,"` | — |
| [SRC-FDEEAFDFCA-L000070](../../agents/request_budget.py#L70) | 70 | `"        )"` | — |
| [SRC-FDEEAFDFCA-L000071](../../agents/request_budget.py#L71) | 71 | `"        limits = {"` | — |
| [SRC-FDEEAFDFCA-L000072](../../agents/request_budget.py#L72) | 72 | `"            key: _bounded_env_int("` | — |
| [SRC-FDEEAFDFCA-L000073](../../agents/request_budget.py#L73) | 73 | `"                f\"OMARAI_REQUEST_MAX_{key.upper()}\","` | — |
| [SRC-FDEEAFDFCA-L000074](../../agents/request_budget.py#L74) | 74 | `"                defaults[0],"` | — |
| [SRC-FDEEAFDFCA-L000075](../../agents/request_budget.py#L75) | 75 | `"                0 if key == \"tool_calls\" else 1,"` | — |
| [SRC-FDEEAFDFCA-L000076](../../agents/request_budget.py#L76) | 76 | `"                defaults[1],"` | — |
| [SRC-FDEEAFDFCA-L000077](../../agents/request_budget.py#L77) | 77 | `"            )"` | — |
| [SRC-FDEEAFDFCA-L000078](../../agents/request_budget.py#L78) | 78 | `"            for key, defaults in RESOURCE_LIMITS.items()"` | — |
| [SRC-FDEEAFDFCA-L000079](../../agents/request_budget.py#L79) | 79 | `"        }"` | — |
| [SRC-FDEEAFDFCA-L000080](../../agents/request_budget.py#L80) | 80 | `"        return cls(timeout_seconds=timeout, limits=limits)"` | — |
| [SRC-FDEEAFDFCA-L000081](../../agents/request_budget.py#L81) | 81 | `""` | — |
| [SRC-FDEEAFDFCA-L000082](../../agents/request_budget.py#L82) | 82 | `"    def remaining_seconds(self) -> float:"` | — |
| [SRC-FDEEAFDFCA-L000083](../../agents/request_budget.py#L83) | 83 | `"        return max(0.0, self.deadline - self._clock())"` | — |
| [SRC-FDEEAFDFCA-L000084](../../agents/request_budget.py#L84) | 84 | `""` | — |
| [SRC-FDEEAFDFCA-L000085](../../agents/request_budget.py#L85) | 85 | `"    def timeout_for(self, configured_seconds: float) -> float:"` | — |
| [SRC-FDEEAFDFCA-L000086](../../agents/request_budget.py#L86) | 86 | `"        \"\"\"Cap one outbound timeout to time remaining; raise instead of starting at zero.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000087](../../agents/request_budget.py#L87) | 87 | `"        remaining = self.remaining_seconds()"` | — |
| [SRC-FDEEAFDFCA-L000088](../../agents/request_budget.py#L88) | 88 | `"        if remaining <= 0:"` | — |
| [SRC-FDEEAFDFCA-L000089](../../agents/request_budget.py#L89) | 89 | `"            with self._lock:"` | — |
| [SRC-FDEEAFDFCA-L000090](../../agents/request_budget.py#L90) | 90 | `"                self._exhausted_reasons.add(\"deadline\")"` | — |
| [SRC-FDEEAFDFCA-L000091](../../agents/request_budget.py#L91) | 91 | `"            raise RequestBudgetExceeded(\"انتهت ميزانية وقت الطلب.\")"` | — |
| [SRC-FDEEAFDFCA-L000092](../../agents/request_budget.py#L92) | 92 | `"        return min(float(configured_seconds), remaining)"` | — |
| [SRC-FDEEAFDFCA-L000093](../../agents/request_budget.py#L93) | 93 | `""` | — |
| [SRC-FDEEAFDFCA-L000094](../../agents/request_budget.py#L94) | 94 | `"    def remaining_units(self, resource: str) -> int:"` | — |
| [SRC-FDEEAFDFCA-L000095](../../agents/request_budget.py#L95) | 95 | `"        \"\"\"Return unused units for a resource; zero means disabled, exhausted, or expired.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000096](../../agents/request_budget.py#L96) | 96 | `"        if resource not in self._limits:"` | — |
| [SRC-FDEEAFDFCA-L000097](../../agents/request_budget.py#L97) | 97 | `"            raise ValueError(f\"unknown request-budget resource: {resource}\")"` | — |
| [SRC-FDEEAFDFCA-L000098](../../agents/request_budget.py#L98) | 98 | `"        if self.remaining_seconds() <= 0:"` | — |
| [SRC-FDEEAFDFCA-L000099](../../agents/request_budget.py#L99) | 99 | `"            return 0"` | — |
| [SRC-FDEEAFDFCA-L000100](../../agents/request_budget.py#L100) | 100 | `"        with self._lock:"` | — |
| [SRC-FDEEAFDFCA-L000101](../../agents/request_budget.py#L101) | 101 | `"            return max(0, self._limits[resource] - self._counts[resource])"` | — |
| [SRC-FDEEAFDFCA-L000102](../../agents/request_budget.py#L102) | 102 | `""` | — |
| [SRC-FDEEAFDFCA-L000103](../../agents/request_budget.py#L103) | 103 | `"    def reserve(self, resource: str, amount: int = 1) -> None:"` | — |
| [SRC-FDEEAFDFCA-L000104](../../agents/request_budget.py#L104) | 104 | `"        \"\"\"Atomically reserve resource units before initiating external work.\"\"\""` | — |
| [SRC-FDEEAFDFCA-L000105](../../agents/request_budget.py#L105) | 105 | `"        if resource not in self._limits:"` | — |
| [SRC-FDEEAFDFCA-L000106](../../agents/request_budget.py#L106) | 106 | `"            raise ValueError(f\"unknown request-budget resource: {resource}\")"` | — |
| [SRC-FDEEAFDFCA-L000107](../../agents/request_budget.py#L107) | 107 | `"        if amount < 1:"` | — |
| [SRC-FDEEAFDFCA-L000108](../../agents/request_budget.py#L108) | 108 | `"            raise ValueError(\"reservation amount must be positive\")"` | — |
| [SRC-FDEEAFDFCA-L000109](../../agents/request_budget.py#L109) | 109 | `"        with self._lock:"` | — |
| [SRC-FDEEAFDFCA-L000110](../../agents/request_budget.py#L110) | 110 | `"            if self.remaining_seconds() <= 0:"` | — |
| [SRC-FDEEAFDFCA-L000111](../../agents/request_budget.py#L111) | 111 | `"                self._exhausted_reasons.add(\"deadline\")"` | — |
| [SRC-FDEEAFDFCA-L000112](../../agents/request_budget.py#L112) | 112 | `"                raise RequestBudgetExceeded(\"انتهت ميزانية وقت الطلب.\")"` | — |
| [SRC-FDEEAFDFCA-L000113](../../agents/request_budget.py#L113) | 113 | `"            limit = self._limits[resource]"` | — |
| [SRC-FDEEAFDFCA-L000114](../../agents/request_budget.py#L114) | 114 | `"            if self._counts[resource] + amount > limit:"` | — |
| [SRC-FDEEAFDFCA-L000115](../../agents/request_budget.py#L115) | 115 | `"                self._exhausted_reasons.add(resource)"` | — |
| [SRC-FDEEAFDFCA-L000116](../../agents/request_budget.py#L116) | 116 | `"                raise RequestBudgetExceeded("` | — |
| [SRC-FDEEAFDFCA-L000117](../../agents/request_budget.py#L117) | 117 | `"                    f\"تم بلوغ حد موارد الطلب: {resource}.\""` | — |
| [SRC-FDEEAFDFCA-L000118](../../agents/request_budget.py#L118) | 118 | `"                )"` | — |
| [SRC-FDEEAFDFCA-L000119](../../agents/request_budget.py#L119) | 119 | `"            self._counts[resource] += amount"` | — |
| [SRC-FDEEAFDFCA-L000120](../../agents/request_budget.py#L120) | 120 | `""` | — |
| [SRC-FDEEAFDFCA-L000121](../../agents/request_budget.py#L121) | 121 | `"    def snapshot(self) -> dict[str, Any]:"` | — |
| [SRC-FDEEAFDFCA-L000122](../../agents/request_budget.py#L122) | 122 | `"        with self._lock:"` | — |
| [SRC-FDEEAFDFCA-L000123](../../agents/request_budget.py#L123) | 123 | `"            counts = dict(self._counts)"` | — |
| [SRC-FDEEAFDFCA-L000124](../../agents/request_budget.py#L124) | 124 | `"            limits = dict(self._limits)"` | — |
| [SRC-FDEEAFDFCA-L000125](../../agents/request_budget.py#L125) | 125 | `"            exhausted_reasons = sorted(self._exhausted_reasons)"` | — |
| [SRC-FDEEAFDFCA-L000126](../../agents/request_budget.py#L126) | 126 | `"        remaining = self.remaining_seconds()"` | — |
| [SRC-FDEEAFDFCA-L000127](../../agents/request_budget.py#L127) | 127 | `"        return {"` | — |
| [SRC-FDEEAFDFCA-L000128](../../agents/request_budget.py#L128) | 128 | `"            \"policy\": \"cooperative_per_request_budget\","` | — |
| [SRC-FDEEAFDFCA-L000129](../../agents/request_budget.py#L129) | 129 | `"            \"timeout_seconds\": round(self.deadline - self.started_at, 3),"` | — |
| [SRC-FDEEAFDFCA-L000130](../../agents/request_budget.py#L130) | 130 | `"            \"elapsed_seconds\": round(max(0.0, self._clock() - self.started_at), 3),"` | — |
| [SRC-FDEEAFDFCA-L000131](../../agents/request_budget.py#L131) | 131 | `"            \"remaining_seconds\": round(remaining, 3),"` | — |
| [SRC-FDEEAFDFCA-L000132](../../agents/request_budget.py#L132) | 132 | `"            \"deadline_exceeded\": remaining <= 0,"` | — |
| [SRC-FDEEAFDFCA-L000133](../../agents/request_budget.py#L133) | 133 | `"            \"budget_exhausted\": bool(exhausted_reasons) or remaining <= 0,"` | — |
| [SRC-FDEEAFDFCA-L000134](../../agents/request_budget.py#L134) | 134 | `"            \"exhausted_reasons\": exhausted_reasons,"` | — |
| [SRC-FDEEAFDFCA-L000135](../../agents/request_budget.py#L135) | 135 | `"            \"counts\": counts,"` | — |
| [SRC-FDEEAFDFCA-L000136](../../agents/request_budget.py#L136) | 136 | `"            \"limits\": limits,"` | — |
| [SRC-FDEEAFDFCA-L000137](../../agents/request_budget.py#L137) | 137 | `"            \"resources_at_limit\": ["` | — |
| [SRC-FDEEAFDFCA-L000138](../../agents/request_budget.py#L138) | 138 | `"                key for key, limit in limits.items() if limit > 0 and counts[key] >= limit"` | — |
| [SRC-FDEEAFDFCA-L000139](../../agents/request_budget.py#L139) | 139 | `"            ],"` | — |
| [SRC-FDEEAFDFCA-L000140](../../agents/request_budget.py#L140) | 140 | `"            \"disabled_resources\": [key for key, limit in limits.items() if limit == 0],"` | — |
| [SRC-FDEEAFDFCA-L000141](../../agents/request_budget.py#L141) | 141 | `"            \"hard_cancellation_guaranteed\": False,"` | — |
| [SRC-FDEEAFDFCA-L000142](../../agents/request_budget.py#L142) | 142 | `"        }"` | — |
## الوكيل والمنطق

### FILE-59CF4B7DE8 — [agents/research.py](../../agents/research.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-59CF4B7DE8-L000001](../../agents/research.py#L1) | 1 | `"\"\"\"Research planning, domain targeting, and multi-query source ranking."` | — |
| [SRC-59CF4B7DE8-L000002](../../agents/research.py#L2) | 2 | `""` | — |
| [SRC-59CF4B7DE8-L000003](../../agents/research.py#L3) | 3 | `"This module is deterministic by design: the language model may propose a plan,"` | — |
| [SRC-59CF4B7DE8-L000004](../../agents/research.py#L4) | 4 | `"but all queries, result counts and source records are validated before use."` | — |
| [SRC-59CF4B7DE8-L000005](../../agents/research.py#L5) | 5 | `"\"\"\""` | — |
| [SRC-59CF4B7DE8-L000006](../../agents/research.py#L6) | 6 | `"from __future__ import annotations"` | — |
| [SRC-59CF4B7DE8-L000007](../../agents/research.py#L7) | 7 | `""` | — |
| [SRC-59CF4B7DE8-L000008](../../agents/research.py#L8) | 8 | `"import ipaddress"` | — |
| [SRC-59CF4B7DE8-L000009](../../agents/research.py#L9) | 9 | `"import re"` | — |
| [SRC-59CF4B7DE8-L000010](../../agents/research.py#L10) | 10 | `"from datetime import UTC, datetime, timedelta"` | — |
| [SRC-59CF4B7DE8-L000011](../../agents/research.py#L11) | 11 | `"from email.utils import parsedate_to_datetime"` | — |
| [SRC-59CF4B7DE8-L000012](../../agents/research.py#L12) | 12 | `"from typing import Any"` | — |
| [SRC-59CF4B7DE8-L000013](../../agents/research.py#L13) | 13 | `"from urllib.parse import urlparse"` | — |
| [SRC-59CF4B7DE8-L000014](../../agents/research.py#L14) | 14 | `""` | — |
| [SRC-59CF4B7DE8-L000015](../../agents/research.py#L15) | 15 | `"import tldextract"` | — |
| [SRC-59CF4B7DE8-L000016](../../agents/research.py#L16) | 16 | `""` | — |
| [SRC-59CF4B7DE8-L000017](../../agents/research.py#L17) | 17 | `"from agents.aspect_planning import extract_aspects"` | — |
| [SRC-59CF4B7DE8-L000018](../../agents/research.py#L18) | 18 | `"from agents.intent_router import resolve_followup_query"` | — |
| [SRC-59CF4B7DE8-L000019](../../agents/research.py#L19) | 19 | `"from agents.task_understanding import build_query_strategy_matrix, build_task_spec"` | — |
| [SRC-59CF4B7DE8-L000020](../../agents/research.py#L20) | 20 | `""` | — |
| [SRC-59CF4B7DE8-L000021](../../agents/research.py#L21) | 21 | `"MAX_PLAN_QUERIES = 8"` | — |
| [SRC-59CF4B7DE8-L000022](../../agents/research.py#L22) | 22 | `"MAX_QUERY_CHARS = 240"` | — |
| [SRC-59CF4B7DE8-L000023](../../agents/research.py#L23) | 23 | `"MAX_FUSED_RESULTS = 18"` | — |
| [SRC-59CF4B7DE8-L000024](../../agents/research.py#L24) | 24 | `""` | — |
| [SRC-59CF4B7DE8-L000025](../../agents/research.py#L25) | 25 | `""` | — |
| [SRC-59CF4B7DE8-L000026](../../agents/research.py#L26) | 26 | `"# Use the Public Suffix List snapshot bundled with tldextract; never fetch it at"` | — |
| [SRC-59CF4B7DE8-L000027](../../agents/research.py#L27) | 27 | `"# runtime. Including private suffixes keeps tenant-hosted sites (e.g. github.io)"` | — |
| [SRC-59CF4B7DE8-L000028](../../agents/research.py#L28) | 28 | `"# separate, while subdomains belonging to one registrable site share one identity."` | — |
| [SRC-59CF4B7DE8-L000029](../../agents/research.py#L29) | 29 | `"_DOMAIN_EXTRACTOR = tldextract.TLDExtract("` | — |
| [SRC-59CF4B7DE8-L000030](../../agents/research.py#L30) | 30 | `"    suffix_list_urls=(),"` | — |
| [SRC-59CF4B7DE8-L000031](../../agents/research.py#L31) | 31 | `"    include_psl_private_domains=True,"` | — |
| [SRC-59CF4B7DE8-L000032](../../agents/research.py#L32) | 32 | `")"` | — |
| [SRC-59CF4B7DE8-L000033](../../agents/research.py#L33) | 33 | `""` | — |
| [SRC-59CF4B7DE8-L000034](../../agents/research.py#L34) | 34 | `""` | — |
| [SRC-59CF4B7DE8-L000035](../../agents/research.py#L35) | 35 | `"def registrable_domain(value: Any) -> str:"` | — |
| [SRC-59CF4B7DE8-L000036](../../agents/research.py#L36) | 36 | `"    \"\"\"Return a normalized registrable domain (or normalized IP/unknown hostname)."` | — |
| [SRC-59CF4B7DE8-L000037](../../agents/research.py#L37) | 37 | `""` | — |
| [SRC-59CF4B7DE8-L000038](../../agents/research.py#L38) | 38 | `"    This is a conservative source-diversity key, not proof that two publishers"` | — |
| [SRC-59CF4B7DE8-L000039](../../agents/research.py#L39) | 39 | `"    are editorially independent. It prevents sibling subdomains from being"` | — |
| [SRC-59CF4B7DE8-L000040](../../agents/research.py#L40) | 40 | `"    counted as separate domains in the evidence coverage threshold."` | — |
| [SRC-59CF4B7DE8-L000041](../../agents/research.py#L41) | 41 | `"    \"\"\""` | — |
| [SRC-59CF4B7DE8-L000042](../../agents/research.py#L42) | 42 | `"    candidate = str(value or \"\").strip()"` | — |
| [SRC-59CF4B7DE8-L000043](../../agents/research.py#L43) | 43 | `"    if not candidate:"` | — |
| [SRC-59CF4B7DE8-L000044](../../agents/research.py#L44) | 44 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000045](../../agents/research.py#L45) | 45 | `"    parsed = urlparse(candidate if \"://\" in candidate else \"//\" + candidate)"` | — |
| [SRC-59CF4B7DE8-L000046](../../agents/research.py#L46) | 46 | `"    host = (parsed.hostname or \"\").rstrip(\".\").lower()"` | — |
| [SRC-59CF4B7DE8-L000047](../../agents/research.py#L47) | 47 | `"    if not host:"` | — |
| [SRC-59CF4B7DE8-L000048](../../agents/research.py#L48) | 48 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000049](../../agents/research.py#L49) | 49 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000050](../../agents/research.py#L50) | 50 | `"        return str(ipaddress.ip_address(host))"` | — |
| [SRC-59CF4B7DE8-L000051](../../agents/research.py#L51) | 51 | `"    except ValueError:"` | — |
| [SRC-59CF4B7DE8-L000052](../../agents/research.py#L52) | 52 | `"        pass"` | — |
| [SRC-59CF4B7DE8-L000053](../../agents/research.py#L53) | 53 | `"    try:"` | — |
| [SRC-59CF4B7DE8-L000054](../../agents/research.py#L54) | 54 | `"        host = host.encode(\"idna\").decode(\"ascii\").lower()"` | — |
| [SRC-59CF4B7DE8-L000055](../../agents/research.py#L55) | 55 | `"    except UnicodeError:"` | — |
| [SRC-59CF4B7DE8-L000056](../../agents/research.py#L56) | 56 | `"        return host"` | — |
| [SRC-59CF4B7DE8-L000057](../../agents/research.py#L57) | 57 | `"    extracted = _DOMAIN_EXTRACTOR(host)"` | — |
| [SRC-59CF4B7DE8-L000058](../../agents/research.py#L58) | 58 | `"    return (extracted.top_domain_under_public_suffix or host).lower()"` | — |
| [SRC-59CF4B7DE8-L000059](../../agents/research.py#L59) | 59 | `""` | — |
| [SRC-59CF4B7DE8-L000060](../../agents/research.py#L60) | 60 | `"SOCIAL_DOMAINS = {"` | — |
| [SRC-59CF4B7DE8-L000061](../../agents/research.py#L61) | 61 | `"    \"reddit\": \"reddit.com\","` | — |
| [SRC-59CF4B7DE8-L000062](../../agents/research.py#L62) | 62 | `"    \"youtube\": \"youtube.com\","` | — |
| [SRC-59CF4B7DE8-L000063](../../agents/research.py#L63) | 63 | `"    \"facebook\": \"facebook.com\","` | — |
| [SRC-59CF4B7DE8-L000064](../../agents/research.py#L64) | 64 | `"    \"instagram\": \"instagram.com\","` | — |
| [SRC-59CF4B7DE8-L000065](../../agents/research.py#L65) | 65 | `"    \"x\": \"x.com\","` | — |
| [SRC-59CF4B7DE8-L000066](../../agents/research.py#L66) | 66 | `"    \"twitter\": \"twitter.com\","` | — |
| [SRC-59CF4B7DE8-L000067](../../agents/research.py#L67) | 67 | `"    \"tiktok\": \"tiktok.com\","` | — |
| [SRC-59CF4B7DE8-L000068](../../agents/research.py#L68) | 68 | `"    \"linkedin\": \"linkedin.com\","` | — |
| [SRC-59CF4B7DE8-L000069](../../agents/research.py#L69) | 69 | `"    \"threads\": \"threads.net\","` | — |
| [SRC-59CF4B7DE8-L000070](../../agents/research.py#L70) | 70 | `"    \"bluesky\": \"bsky.app\","` | — |
| [SRC-59CF4B7DE8-L000071](../../agents/research.py#L71) | 71 | `"}"` | — |
| [SRC-59CF4B7DE8-L000072](../../agents/research.py#L72) | 72 | `""` | — |
| [SRC-59CF4B7DE8-L000073](../../agents/research.py#L73) | 73 | `"_SOCIAL_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000074](../../agents/research.py#L74) | 74 | `"    \"social media\", \"social network\", \"social posts\", \"social pages\", \"public social\", \"public posts\","` | — |
| [SRC-59CF4B7DE8-L000075](../../agents/research.py#L75) | 75 | `"    \"facebook\", \"instagram\", \"reddit\", \"youtube\", \"twitter\", \"x.com\","` | — |
| [SRC-59CF4B7DE8-L000076](../../agents/research.py#L76) | 76 | `"    \"tiktok\", \"linkedin\", \"threads\", \"bluesky\","` | — |
| [SRC-59CF4B7DE8-L000077](../../agents/research.py#L77) | 77 | `"    \"سوشيال\", \"التواصل الاجتماعي\", \"مواقع التواصل\", \"صفحات التواصل\","` | — |
| [SRC-59CF4B7DE8-L000078](../../agents/research.py#L78) | 78 | `"    \"منشورات\", \"تعليقات الناس\", \"آراء الناس\", \"تجارب المستخدمين\","` | — |
| [SRC-59CF4B7DE8-L000079](../../agents/research.py#L79) | 79 | `"    \"تجارب العملاء\", \"اراء العملاء\", \"آراء العملاء\", \"رأي الناس\","` | — |
| [SRC-59CF4B7DE8-L000080](../../agents/research.py#L80) | 80 | `"    \"كلام الناس\", \"الناس بتقول\", \"مراجعات العملاء\", \"تعليقات العملاء\","` | — |
| [SRC-59CF4B7DE8-L000081](../../agents/research.py#L81) | 81 | `"    \"بوستات\", \"فيدوهات\", \"فيديوهات\", \"ريلز\", \"تويتر\", \"فيسبوك\","` | — |
| [SRC-59CF4B7DE8-L000082](../../agents/research.py#L82) | 82 | `"    \"انستجرام\", \"إنستجرام\", \"تيك توك\", \"لينكدان\", \"لينكدإن\","` | — |
| [SRC-59CF4B7DE8-L000083](../../agents/research.py#L83) | 83 | `"    \"مصادر العملاء\", \"عملاء محتملين\", \"العملاء المحتملين\","` | — |
| [SRC-59CF4B7DE8-L000084](../../agents/research.py#L84) | 84 | `")"` | — |
| [SRC-59CF4B7DE8-L000085](../../agents/research.py#L85) | 85 | `""` | — |
| [SRC-59CF4B7DE8-L000086](../../agents/research.py#L86) | 86 | `"_FRESH_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000087](../../agents/research.py#L87) | 87 | `"    \"latest\", \"current\", \"today\", \"this week\", \"recent\", \"breaking\", \"news\","` | — |
| [SRC-59CF4B7DE8-L000088](../../agents/research.py#L88) | 88 | `"    \"now\", \"2026\", \"latest price\", \"market price\", \"updated\","` | — |
| [SRC-59CF4B7DE8-L000089](../../agents/research.py#L89) | 89 | `"    \"آخر\", \"اخر\", \"احدث\", \"أحدث\", \"حاليا\", \"حالياً\", \"الآن\", \"دلوقتي\", \"النهارده\", \"مؤخرًا\", \"مؤخرا\", \"اليوم\", \"هذا الاسبوع\","` | — |
| [SRC-59CF4B7DE8-L000090](../../agents/research.py#L90) | 90 | `"    \"هذا الأسبوع\", \"آخر الأخبار\", \"اخر الاخبار\", \"مستجدات\", \"حديث\","` | — |
| [SRC-59CF4B7DE8-L000091](../../agents/research.py#L91) | 91 | `"    \"سعر اليوم\", \"الاسعار الحالية\", \"الأسعار الحالية\", \"جديد\","` | — |
| [SRC-59CF4B7DE8-L000092](../../agents/research.py#L92) | 92 | `")"` | — |
| [SRC-59CF4B7DE8-L000093](../../agents/research.py#L93) | 93 | `""` | — |
| [SRC-59CF4B7DE8-L000094](../../agents/research.py#L94) | 94 | `"_DEEP_TERMS = ("` | — |
| [SRC-59CF4B7DE8-L000095](../../agents/research.py#L95) | 95 | `"    \"deep research\", \"in-depth\", \"comprehensive\", \"exhaustive\", \"compare\","` | — |
| [SRC-59CF4B7DE8-L000096](../../agents/research.py#L96) | 96 | `"    \"comparison\", \"pros and cons\", \"investigate\", \"evidence\", \"sources\","` | — |
| [SRC-59CF4B7DE8-L000097](../../agents/research.py#L97) | 97 | `"    \"بحث عميق\", \"بحث معمق\", \"بحث مكثف\", \"بحث شامل\", \"بالتفصيل\", \"قارن\","` | — |
| [SRC-59CF4B7DE8-L000098](../../agents/research.py#L98) | 98 | `"    \"مقارنة\", \"استقصاء\", \"تحقق\", \"تأكد\", \"مصادر\", \"أدلة\", \"ادلة\","` | — |
| [SRC-59CF4B7DE8-L000099](../../agents/research.py#L99) | 99 | `"    \"كل الجوانب\", \"بحث واسع\", \"متكامل\","` | — |
| [SRC-59CF4B7DE8-L000100](../../agents/research.py#L100) | 100 | `")"` | — |
| [SRC-59CF4B7DE8-L000101](../../agents/research.py#L101) | 101 | `""` | — |
| [SRC-59CF4B7DE8-L000102](../../agents/research.py#L102) | 102 | `""` | — |
| [SRC-59CF4B7DE8-L000103](../../agents/research.py#L103) | 103 | `"def extract_urls(text: str) -> list[str]:"` | — |
| [SRC-59CF4B7DE8-L000104](../../agents/research.py#L104) | 104 | `"    \"\"\"Extract explicit HTTP(S) URLs without trying to interpret their content as instructions.\"\"\""` | — |
| [SRC-59CF4B7DE8-L000105](../../agents/research.py#L105) | 105 | `"    candidates = re.findall(r\"https?://[^\\s<>()]+\", text or \"\", flags=re.IGNORECASE)"` | — |
| [SRC-59CF4B7DE8-L000106](../../agents/research.py#L106) | 106 | `"    cleaned: list[str] = []"` | — |
| [SRC-59CF4B7DE8-L000107](../../agents/research.py#L107) | 107 | `"    for value in candidates:"` | — |
| [SRC-59CF4B7DE8-L000108](../../agents/research.py#L108) | 108 | `"        url = value.rstrip(\".,;!?،؛:)\\\"'»\")"` | — |
| [SRC-59CF4B7DE8-L000109](../../agents/research.py#L109) | 109 | `"        if url and url not in cleaned:"` | — |
| [SRC-59CF4B7DE8-L000110](../../agents/research.py#L110) | 110 | `"            cleaned.append(url[:2048])"` | — |
| [SRC-59CF4B7DE8-L000111](../../agents/research.py#L111) | 111 | `"        if len(cleaned) >= 5:"` | — |
| [SRC-59CF4B7DE8-L000112](../../agents/research.py#L112) | 112 | `"            break"` | — |
| [SRC-59CF4B7DE8-L000113](../../agents/research.py#L113) | 113 | `"    return cleaned"` | — |
| [SRC-59CF4B7DE8-L000114](../../agents/research.py#L114) | 114 | `""` | — |
| [SRC-59CF4B7DE8-L000115](../../agents/research.py#L115) | 115 | `""` | — |
| [SRC-59CF4B7DE8-L000116](../../agents/research.py#L116) | 116 | `"def _compact(value: Any, limit: int = MAX_QUERY_CHARS) -> str:"` | — |
| [SRC-59CF4B7DE8-L000117](../../agents/research.py#L117) | 117 | `"    if not isinstance(value, str):"` | — |
| [SRC-59CF4B7DE8-L000118](../../agents/research.py#L118) | 118 | `"        return \"\""` | — |
| [SRC-59CF4B7DE8-L000119](../../agents/research.py#L119) | 119 | `"    return re.sub(r\"\\s+\", \" \", value).strip()[:limit]"` | — |
| [SRC-59CF4B7DE8-L000120](../../agents/research.py#L120) | 120 | `""` | — |
| [SRC-59CF4B7DE8-L000121](../../agents/research.py#L121) | 121 | `""` | — |
| [SRC-59CF4B7DE8-L000122](../../agents/research.py#L122) | 122 | `"_SEARCH_TOPIC_PRESERVING_META_PREFIX_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000123](../../agents/research.py#L123) | 123 | `"    r\"^(?:(?:و?استخدم\|و?استعمل)\\s+مصادر?\\s+متعددة\\s+\""` | — |
| [SRC-59CF4B7DE8-L000124](../../agents/research.py#L124) | 124 | `"    r\"(?:للبحث\\s+عن\|للعثور\\s+على\|لإيجاد\|عن\|حول\|بشأن)\|\""` | — |
| [SRC-59CF4B7DE8-L000125](../../agents/research.py#L125) | 125 | `"    r\"use\\s+multiple\\s+sources\\s+to\\s+(?:research\|find\|investigate))\\s+\","` | — |
| [SRC-59CF4B7DE8-L000126](../../agents/research.py#L126) | 126 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000127](../../agents/research.py#L127) | 127 | `")"` | — |
| [SRC-59CF4B7DE8-L000128](../../agents/research.py#L128) | 128 | `""` | — |
| [SRC-59CF4B7DE8-L000129](../../agents/research.py#L129) | 129 | `"_SEARCH_META_START_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000130](../../agents/research.py#L130) | 130 | `"    r\"^(?:و?استخدم\|و?استعمل\|و?اجب\|و?أجب\|و?لا تعرض\|و?لا تقدم\|\""` | — |
| [SRC-59CF4B7DE8-L000131](../../agents/research.py#L131) | 131 | `"    r\"please cite\|cite\|provide links\|mention sources\|use multiple sources\|\""` | — |
| [SRC-59CF4B7DE8-L000132](../../agents/research.py#L132) | 132 | `"    r\"don't present\|do not present)\\b\","` | — |
| [SRC-59CF4B7DE8-L000133](../../agents/research.py#L133) | 133 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000134](../../agents/research.py#L134) | 134 | `")"` | — |
| [SRC-59CF4B7DE8-L000135](../../agents/research.py#L135) | 135 | `"# Treat \"اذكر\" as an action unless its object is clearly citation/format metadata."` | — |
| [SRC-59CF4B7DE8-L000136](../../agents/research.py#L136) | 136 | `"# This preserves topic-bearing prompts such as \"اذكر أبرز السيارات الكهربائية...\"."` | — |
| [SRC-59CF4B7DE8-L000137](../../agents/research.py#L137) | 137 | `"_SEARCH_CITATION_META_START_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000138](../../agents/research.py#L138) | 138 | `"    r\"^(?:و?اذكر(?:ي\|وا)?\|mention\|cite\|provide)\\s+\""` | — |
| [SRC-59CF4B7DE8-L000139](../../agents/research.py#L139) | 139 | `"    r\"(?:المصادر\|مصادر\|المصدر\|مصدر(?:[ًٌٍ]ا?\|ا[ًٌٍ]?)?\|\""` | — |
| [SRC-59CF4B7DE8-L000140](../../agents/research.py#L140) | 140 | `"    r\"روابط?\|رابط\|تواريخ?\|تاريخ\|الاخبار\|الأخبار\|\""` | — |
| [SRC-59CF4B7DE8-L000141](../../agents/research.py#L141) | 141 | `"    r\"the original posts\|links\|sources\|dates)(?=\\s\|$\|[،,])\","` | — |
| [SRC-59CF4B7DE8-L000142](../../agents/research.py#L142) | 142 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000143](../../agents/research.py#L143) | 143 | `")"` | — |
| [SRC-59CF4B7DE8-L000144](../../agents/research.py#L144) | 144 | `"# This is a response-quality instruction, not a topic query."` | — |
| [SRC-59CF4B7DE8-L000145](../../agents/research.py#L145) | 145 | `"_SEARCH_UNCERTAINTY_META_START_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000146](../../agents/research.py#L146) | 146 | `"    r\"^و?وضّ?ح\\s+اذا\\s+كانت\\s+النتائج\\s+غير\\s+كافيه\\b\""` | — |
| [SRC-59CF4B7DE8-L000147](../../agents/research.py#L147) | 147 | `"    r\".*(?:لتمثيل\|تمثيل).*(?:اراء\\s+المستخدمين\|المستخدمين)\\b\","` | — |
| [SRC-59CF4B7DE8-L000148](../../agents/research.py#L148) | 148 | `"    re.IGNORECASE,"` | — |
| [SRC-59CF4B7DE8-L000149](../../agents/research.py#L149) | 149 | `")"` | — |
| [SRC-59CF4B7DE8-L000150](../../agents/research.py#L150) | 150 | `""` | — |
| [SRC-59CF4B7DE8-L000151](../../agents/research.py#L151) | 151 | `"_SEARCH_FACTS_INFERENCE_META_ONLY_RE = re.compile("` | — |
| [SRC-59CF4B7DE8-L000152](../../agents/research.py#L152) | 152 | `"    r\"^و?(?:ميّز\|ميز)\\s+بين\\s+الحقائق\\s+والاستنتاجات\\s*[.!؟؛،,]*$\","` | — |
| [SRC-59CF4B7DE8-L000153](../../agents/research.py#L153) | 153 | `"    re.IGNORECASE,"` | — |
