# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **007**
- سجلات الأسطر: **800**
- النطاق: SRC-686F71AA50-L001124 إلى SRC-1AE03B9EC3-L000494
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-686F71AA50 — [agents/task_understanding.py](../../agents/task_understanding.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-686F71AA50-L001124](../../agents/task_understanding.py#L1124) | 1124 | `"        key = _query_key(candidate)"` | — |
| [SRC-686F71AA50-L001125](../../agents/task_understanding.py#L1125) | 1125 | `"        if not candidate or not key or key in seen:"` | — |
| [SRC-686F71AA50-L001126](../../agents/task_understanding.py#L1126) | 1126 | `"            return"` | — |
| [SRC-686F71AA50-L001127](../../agents/task_understanding.py#L1127) | 1127 | `"        # Search modifications must preserve a subject anchor. Existing planner"` | — |
| [SRC-686F71AA50-L001128](../../agents/task_understanding.py#L1128) | 1128 | `"        # queries are retained because they may already contain resolved context."` | — |
| [SRC-686F71AA50-L001129](../../agents/task_understanding.py#L1129) | 1129 | `"        anchor_query = str(queries[0]).strip() if queries and isinstance(queries[0], str) else str(question or \"\")"` | — |
| [SRC-686F71AA50-L001130](../../agents/task_understanding.py#L1130) | 1130 | `"        topic_tokens = _TOKEN_RE.findall(_query_key(anchor_query))"` | — |
| [SRC-686F71AA50-L001131](../../agents/task_understanding.py#L1131) | 1131 | `"        query_tokens = _TOKEN_RE.findall(key)"` | — |
| [SRC-686F71AA50-L001132](../../agents/task_understanding.py#L1132) | 1132 | `"        if enforce_topic and len(topic_tokens) >= 2 and not any("` | — |
| [SRC-686F71AA50-L001133](../../agents/task_understanding.py#L1133) | 1133 | `"            token in query_tokens for token in topic_tokens[:3]"` | — |
| [SRC-686F71AA50-L001134](../../agents/task_understanding.py#L1134) | 1134 | `"        ):"` | — |
| [SRC-686F71AA50-L001135](../../agents/task_understanding.py#L1135) | 1135 | `"            return"` | — |
| [SRC-686F71AA50-L001136](../../agents/task_understanding.py#L1136) | 1136 | `"        seen.add(key)"` | — |
| [SRC-686F71AA50-L001137](../../agents/task_understanding.py#L1137) | 1137 | `"        rows.append({\"query\": candidate, \"strategy\": strategy, \"rationale\": rationale})"` | — |
| [SRC-686F71AA50-L001138](../../agents/task_understanding.py#L1138) | 1138 | `""` | — |
| [SRC-686F71AA50-L001139](../../agents/task_understanding.py#L1139) | 1139 | `"    constraints = spec.get(\"constraints\") if isinstance(spec.get(\"constraints\"), dict) else {}"` | — |
| [SRC-686F71AA50-L001140](../../agents/task_understanding.py#L1140) | 1140 | `"    explicit_aspects = ("` | — |
| [SRC-686F71AA50-L001141](../../agents/task_understanding.py#L1141) | 1141 | `"        constraints.get(\"explicit_aspects\")"` | — |
| [SRC-686F71AA50-L001142](../../agents/task_understanding.py#L1142) | 1142 | `"        if isinstance(constraints.get(\"explicit_aspects\"), list)"` | — |
| [SRC-686F71AA50-L001143](../../agents/task_understanding.py#L1143) | 1143 | `"        else []"` | — |
| [SRC-686F71AA50-L001144](../../agents/task_understanding.py#L1144) | 1144 | `"    )"` | — |
| [SRC-686F71AA50-L001145](../../agents/task_understanding.py#L1145) | 1145 | `"    # Use the dedicated aspect extractor as a second deterministic pass. This"` | — |
| [SRC-686F71AA50-L001146](../../agents/task_understanding.py#L1146) | 1146 | `"    # guards against a classifier losing the final criterion in a long list."` | — |
| [SRC-686F71AA50-L001147](../../agents/task_understanding.py#L1147) | 1147 | `"    try:"` | — |
| [SRC-686F71AA50-L001148](../../agents/task_understanding.py#L1148) | 1148 | `"        from agents.aspect_planning import extract_aspects"` | — |
| [SRC-686F71AA50-L001149](../../agents/task_understanding.py#L1149) | 1149 | `"        independently_extracted = extract_aspects(question)"` | — |
| [SRC-686F71AA50-L001150](../../agents/task_understanding.py#L1150) | 1150 | `"    except (ImportError, TypeError, ValueError):"` | — |
| [SRC-686F71AA50-L001151](../../agents/task_understanding.py#L1151) | 1151 | `"        independently_extracted = []"` | — |
| [SRC-686F71AA50-L001152](../../agents/task_understanding.py#L1152) | 1152 | `"    merged_aspects: list[str] = []"` | — |
| [SRC-686F71AA50-L001153](../../agents/task_understanding.py#L1153) | 1153 | `"    aspect_keys: set[str] = set()"` | — |
| [SRC-686F71AA50-L001154](../../agents/task_understanding.py#L1154) | 1154 | `"    for aspect in [*explicit_aspects, *independently_extracted]:"` | — |
| [SRC-686F71AA50-L001155](../../agents/task_understanding.py#L1155) | 1155 | `"        if not isinstance(aspect, str) or not aspect.strip():"` | — |
| [SRC-686F71AA50-L001156](../../agents/task_understanding.py#L1156) | 1156 | `"            continue"` | — |
| [SRC-686F71AA50-L001157](../../agents/task_understanding.py#L1157) | 1157 | `"        key = _query_key(aspect)"` | — |
| [SRC-686F71AA50-L001158](../../agents/task_understanding.py#L1158) | 1158 | `"        if key and key not in aspect_keys:"` | — |
| [SRC-686F71AA50-L001159](../../agents/task_understanding.py#L1159) | 1159 | `"            aspect_keys.add(key)"` | — |
| [SRC-686F71AA50-L001160](../../agents/task_understanding.py#L1160) | 1160 | `"            merged_aspects.append(aspect.strip())"` | — |
| [SRC-686F71AA50-L001161](../../agents/task_understanding.py#L1161) | 1161 | `"        if len(merged_aspects) >= MAX_TASK_ASPECTS:"` | — |
| [SRC-686F71AA50-L001162](../../agents/task_understanding.py#L1162) | 1162 | `"            break"` | — |
| [SRC-686F71AA50-L001163](../../agents/task_understanding.py#L1163) | 1163 | `"    explicit_aspects = merged_aspects"` | — |
| [SRC-686F71AA50-L001164](../../agents/task_understanding.py#L1164) | 1164 | `"    spec_for_candidates = dict(spec)"` | — |
| [SRC-686F71AA50-L001165](../../agents/task_understanding.py#L1165) | 1165 | `"    candidate_constraints = dict(constraints)"` | — |
| [SRC-686F71AA50-L001166](../../agents/task_understanding.py#L1166) | 1166 | `"    candidate_constraints[\"explicit_aspects\"] = explicit_aspects"` | — |
| [SRC-686F71AA50-L001167](../../agents/task_understanding.py#L1167) | 1167 | `"    spec_for_candidates[\"constraints\"] = candidate_constraints"` | — |
| [SRC-686F71AA50-L001168](../../agents/task_understanding.py#L1168) | 1168 | `"    # If every query slot is needed to represent explicit comparison criteria,"` | — |
| [SRC-686F71AA50-L001169](../../agents/task_understanding.py#L1169) | 1169 | `"    # spend the budget on those criteria rather than a generic planner seed."` | — |
| [SRC-686F71AA50-L001170](../../agents/task_understanding.py#L1170) | 1170 | `"    reserve_all_slots_for_criteria = ("` | — |
| [SRC-686F71AA50-L001171](../../agents/task_understanding.py#L1171) | 1171 | `"        spec.get(\"task_family\") == \"compare\""` | — |
| [SRC-686F71AA50-L001172](../../agents/task_understanding.py#L1172) | 1172 | `"        and len(explicit_aspects) >= maximum"` | — |
| [SRC-686F71AA50-L001173](../../agents/task_understanding.py#L1173) | 1173 | `"    )"` | — |
| [SRC-686F71AA50-L001174](../../agents/task_understanding.py#L1174) | 1174 | `"    if queries and not reserve_all_slots_for_criteria:"` | — |
| [SRC-686F71AA50-L001175](../../agents/task_understanding.py#L1175) | 1175 | `"        seed = queries[0]"` | — |
| [SRC-686F71AA50-L001176](../../agents/task_understanding.py#L1176) | 1176 | `"        strategy, rationale = ("` | — |
| [SRC-686F71AA50-L001177](../../agents/task_understanding.py#L1177) | 1177 | `"            _label_existing_query(seed, 0, spec)"` | — |
| [SRC-686F71AA50-L001178](../../agents/task_understanding.py#L1178) | 1178 | `"            if isinstance(seed, str)"` | — |
| [SRC-686F71AA50-L001179](../../agents/task_understanding.py#L1179) | 1179 | `"            else (\"malformed\", \"planner seed is not a string\")"` | — |
| [SRC-686F71AA50-L001180](../../agents/task_understanding.py#L1180) | 1180 | `"        )"` | — |
| [SRC-686F71AA50-L001181](../../agents/task_understanding.py#L1181) | 1181 | `"        add(seed, strategy, rationale, enforce_topic=False)"` | — |
| [SRC-686F71AA50-L001182](../../agents/task_understanding.py#L1182) | 1182 | `""` | — |
| [SRC-686F71AA50-L001183](../../agents/task_understanding.py#L1183) | 1183 | `"    if not rows and ("` | — |
| [SRC-686F71AA50-L001184](../../agents/task_understanding.py#L1184) | 1184 | `"        spec.get(\"ambiguity_status\") == \"needs_clarification\""` | — |
| [SRC-686F71AA50-L001185](../../agents/task_understanding.py#L1185) | 1185 | `"        or spec.get(\"task_family\") == \"ambiguous_or_incomplete\""` | — |
| [SRC-686F71AA50-L001186](../../agents/task_understanding.py#L1186) | 1186 | `"    ):"` | — |
| [SRC-686F71AA50-L001187](../../agents/task_understanding.py#L1187) | 1187 | `"        return rows"` | — |
| [SRC-686F71AA50-L001188](../../agents/task_understanding.py#L1188) | 1188 | `""` | — |
| [SRC-686F71AA50-L001189](../../agents/task_understanding.py#L1189) | 1189 | `"    base = str(queries[0]).strip() if queries and isinstance(queries[0], str) else \"\""` | — |
| [SRC-686F71AA50-L001190](../../agents/task_understanding.py#L1190) | 1190 | `"    if not base:"` | — |
| [SRC-686F71AA50-L001191](../../agents/task_understanding.py#L1191) | 1191 | `"        base = re.sub("` | — |
| [SRC-686F71AA50-L001192](../../agents/task_understanding.py#L1192) | 1192 | `"            r\"^(?:من فضلك\|لو سمحت\|ابحث لي\|ابحث\|دورلي\|دور\|اعثر على\|please\|search for\|find\|look up)\\s*\","` | — |
| [SRC-686F71AA50-L001193](../../agents/task_understanding.py#L1193) | 1193 | `"            \"\", str(question or \"\").strip(), flags=re.IGNORECASE,"` | — |
| [SRC-686F71AA50-L001194](../../agents/task_understanding.py#L1194) | 1194 | `"        )"` | — |
| [SRC-686F71AA50-L001195](../../agents/task_understanding.py#L1195) | 1195 | `"    base = _QUERY_STOP.sub(\"\", base).strip(\" \\t\\r\\n-،,؛;\")"` | — |
| [SRC-686F71AA50-L001196](../../agents/task_understanding.py#L1196) | 1196 | `"    if not base:"` | — |
| [SRC-686F71AA50-L001197](../../agents/task_understanding.py#L1197) | 1197 | `"        return rows"` | — |
| [SRC-686F71AA50-L001198](../../agents/task_understanding.py#L1198) | 1198 | `""` | — |
| [SRC-686F71AA50-L001199](../../agents/task_understanding.py#L1199) | 1199 | `"    candidates = _generated_strategy_candidates(base, spec_for_candidates)"` | — |
| [SRC-686F71AA50-L001200](../../agents/task_understanding.py#L1200) | 1200 | `"    preserve_planner_alternatives_early = ("` | — |
| [SRC-686F71AA50-L001201](../../agents/task_understanding.py#L1201) | 1201 | `"        spec.get(\"task_family\") == \"find_or_discover\""` | — |
| [SRC-686F71AA50-L001202](../../agents/task_understanding.py#L1202) | 1202 | `"        and bool(constraints.get(\"explicit_budgets\"))"` | — |
| [SRC-686F71AA50-L001203](../../agents/task_understanding.py#L1203) | 1203 | `"        and not constraints.get(\"social_evidence_requested\")"` | — |
| [SRC-686F71AA50-L001204](../../agents/task_understanding.py#L1204) | 1204 | `"        and not constraints.get(\"time_sensitive_request\")"` | — |
| [SRC-686F71AA50-L001205](../../agents/task_understanding.py#L1205) | 1205 | `"        and not constraints.get(\"official_destination_required\")"` | — |
| [SRC-686F71AA50-L001206](../../agents/task_understanding.py#L1206) | 1206 | `"    )"` | — |
| [SRC-686F71AA50-L001207](../../agents/task_understanding.py#L1207) | 1207 | `"    if preserve_planner_alternatives_early:"` | — |
| [SRC-686F71AA50-L001208](../../agents/task_understanding.py#L1208) | 1208 | `"        for index, query in enumerate(queries[1:], start=1):"` | — |
| [SRC-686F71AA50-L001209](../../agents/task_understanding.py#L1209) | 1209 | `"            if len(rows) >= maximum:"` | — |
| [SRC-686F71AA50-L001210](../../agents/task_understanding.py#L1210) | 1210 | `"                break"` | — |
| [SRC-686F71AA50-L001211](../../agents/task_understanding.py#L1211) | 1211 | `"            if isinstance(query, str):"` | — |
| [SRC-686F71AA50-L001212](../../agents/task_understanding.py#L1212) | 1212 | `"                strategy, rationale = _label_existing_query(query, index, spec)"` | — |
| [SRC-686F71AA50-L001213](../../agents/task_understanding.py#L1213) | 1213 | `"                add(query, strategy, rationale, enforce_topic=False)"` | — |
| [SRC-686F71AA50-L001214](../../agents/task_understanding.py#L1214) | 1214 | `""` | — |
| [SRC-686F71AA50-L001215](../../agents/task_understanding.py#L1215) | 1215 | `"    for query, strategy, rationale in candidates:"` | — |
| [SRC-686F71AA50-L001216](../../agents/task_understanding.py#L1216) | 1216 | `"        add(query, strategy, rationale)"` | — |
| [SRC-686F71AA50-L001217](../../agents/task_understanding.py#L1217) | 1217 | `"        if len(rows) >= maximum:"` | — |
| [SRC-686F71AA50-L001218](../../agents/task_understanding.py#L1218) | 1218 | `"            break"` | — |
| [SRC-686F71AA50-L001219](../../agents/task_understanding.py#L1219) | 1219 | `""` | — |
| [SRC-686F71AA50-L001220](../../agents/task_understanding.py#L1220) | 1220 | `"    # Preserve other planner alternatives only after task-targeted candidates."` | — |
| [SRC-686F71AA50-L001221](../../agents/task_understanding.py#L1221) | 1221 | `"    for index, query in enumerate(queries[1:], start=1):"` | — |
| [SRC-686F71AA50-L001222](../../agents/task_understanding.py#L1222) | 1222 | `"        if len(rows) >= maximum:"` | — |
| [SRC-686F71AA50-L001223](../../agents/task_understanding.py#L1223) | 1223 | `"            break"` | — |
| [SRC-686F71AA50-L001224](../../agents/task_understanding.py#L1224) | 1224 | `"        if isinstance(query, str):"` | — |
| [SRC-686F71AA50-L001225](../../agents/task_understanding.py#L1225) | 1225 | `"            strategy, rationale = _label_existing_query(query, index, spec)"` | — |
| [SRC-686F71AA50-L001226](../../agents/task_understanding.py#L1226) | 1226 | `"        else:"` | — |
| [SRC-686F71AA50-L001227](../../agents/task_understanding.py#L1227) | 1227 | `"            strategy, rationale = \"malformed\", \"planner alternative is not a string\""` | — |
| [SRC-686F71AA50-L001228](../../agents/task_understanding.py#L1228) | 1228 | `"        add(query, strategy, rationale, enforce_topic=False)"` | — |
| [SRC-686F71AA50-L001229](../../agents/task_understanding.py#L1229) | 1229 | `"    return rows"` | — |
| [SRC-686F71AA50-L001230](../../agents/task_understanding.py#L1230) | 1230 | `""` | — |
| [SRC-686F71AA50-L001231](../../agents/task_understanding.py#L1231) | 1231 | `"def validate_task_spec(value: Any) -> dict[str, Any]:"` | — |
| [SRC-686F71AA50-L001232](../../agents/task_understanding.py#L1232) | 1232 | `"    \"\"\"Return an allowlisted, bounded JSON representation of TaskSpec-like input.\"\"\""` | — |
| [SRC-686F71AA50-L001233](../../agents/task_understanding.py#L1233) | 1233 | `"    unavailable = {"` | — |
| [SRC-686F71AA50-L001234](../../agents/task_understanding.py#L1234) | 1234 | `"        \"schema\": \"omarai.task_spec.v1\","` | — |
| [SRC-686F71AA50-L001235](../../agents/task_understanding.py#L1235) | 1235 | `"        \"status\": \"not_available\","` | — |
| [SRC-686F71AA50-L001236](../../agents/task_understanding.py#L1236) | 1236 | `"        \"claim\": \"no validated task specification supplied\","` | — |
| [SRC-686F71AA50-L001237](../../agents/task_understanding.py#L1237) | 1237 | `"    }"` | — |
| [SRC-686F71AA50-L001238](../../agents/task_understanding.py#L1238) | 1238 | `"    if not isinstance(value, dict) or value.get(\"schema\") != \"omarai.task_spec.v1\":"` | — |
| [SRC-686F71AA50-L001239](../../agents/task_understanding.py#L1239) | 1239 | `"        return unavailable"` | — |
| [SRC-686F71AA50-L001240](../../agents/task_understanding.py#L1240) | 1240 | `""` | — |
| [SRC-686F71AA50-L001241](../../agents/task_understanding.py#L1241) | 1241 | `"    def clean_text(item: Any, limit: int = 160) -> str:"` | — |
| [SRC-686F71AA50-L001242](../../agents/task_understanding.py#L1242) | 1242 | `"        if not isinstance(item, str):"` | — |
| [SRC-686F71AA50-L001243](../../agents/task_understanding.py#L1243) | 1243 | `"            return \"\""` | — |
| [SRC-686F71AA50-L001244](../../agents/task_understanding.py#L1244) | 1244 | `"        return _SPACE.sub(\" \", unicodedata.normalize(\"NFKC\", item).replace(\"\\x00\", \" \")).strip()[:limit]"` | — |
| [SRC-686F71AA50-L001245](../../agents/task_understanding.py#L1245) | 1245 | `""` | — |
| [SRC-686F71AA50-L001246](../../agents/task_understanding.py#L1246) | 1246 | `"    def clean_list(item: Any, *, items: int = 16, chars: int = 160) -> list[str]:"` | — |
| [SRC-686F71AA50-L001247](../../agents/task_understanding.py#L1247) | 1247 | `"        if not isinstance(item, list):"` | — |
| [SRC-686F71AA50-L001248](../../agents/task_understanding.py#L1248) | 1248 | `"            return []"` | — |
| [SRC-686F71AA50-L001249](../../agents/task_understanding.py#L1249) | 1249 | `"        result: list[str] = []"` | — |
| [SRC-686F71AA50-L001250](../../agents/task_understanding.py#L1250) | 1250 | `"        seen: set[str] = set()"` | — |
| [SRC-686F71AA50-L001251](../../agents/task_understanding.py#L1251) | 1251 | `"        for raw_item in item[:items * 2]:"` | — |
| [SRC-686F71AA50-L001252](../../agents/task_understanding.py#L1252) | 1252 | `"            cleaned = clean_text(raw_item, chars)"` | — |
| [SRC-686F71AA50-L001253](../../agents/task_understanding.py#L1253) | 1253 | `"            key = cleaned.casefold()"` | — |
| [SRC-686F71AA50-L001254](../../agents/task_understanding.py#L1254) | 1254 | `"            if cleaned and key not in seen:"` | — |
| [SRC-686F71AA50-L001255](../../agents/task_understanding.py#L1255) | 1255 | `"                result.append(cleaned)"` | — |
| [SRC-686F71AA50-L001256](../../agents/task_understanding.py#L1256) | 1256 | `"                seen.add(key)"` | — |
| [SRC-686F71AA50-L001257](../../agents/task_understanding.py#L1257) | 1257 | `"            if len(result) >= items:"` | — |
| [SRC-686F71AA50-L001258](../../agents/task_understanding.py#L1258) | 1258 | `"                break"` | — |
| [SRC-686F71AA50-L001259](../../agents/task_understanding.py#L1259) | 1259 | `"        return result"` | — |
| [SRC-686F71AA50-L001260](../../agents/task_understanding.py#L1260) | 1260 | `""` | — |
| [SRC-686F71AA50-L001261](../../agents/task_understanding.py#L1261) | 1261 | `"    raw_constraints = value.get(\"constraints\")"` | — |
| [SRC-686F71AA50-L001262](../../agents/task_understanding.py#L1262) | 1262 | `"    raw_constraints = raw_constraints if isinstance(raw_constraints, dict) else {}"` | — |
| [SRC-686F71AA50-L001263](../../agents/task_understanding.py#L1263) | 1263 | `"    list_constraint_keys = ("` | — |
| [SRC-686F71AA50-L001264](../../agents/task_understanding.py#L1264) | 1264 | `"        \"explicit_locations\", \"explicit_years\", \"explicit_dates\","` | — |
| [SRC-686F71AA50-L001265](../../agents/task_understanding.py#L1265) | 1265 | `"        \"explicit_budgets\", \"explicit_urls\", \"explicit_aspects\", \"source_policies\","` | — |
| [SRC-686F71AA50-L001266](../../agents/task_understanding.py#L1266) | 1266 | `"    )"` | — |
| [SRC-686F71AA50-L001267](../../agents/task_understanding.py#L1267) | 1267 | `"    constraints: dict[str, Any] = {"` | — |
| [SRC-686F71AA50-L001268](../../agents/task_understanding.py#L1268) | 1268 | `"        key: clean_list(raw_constraints.get(key), items=8 if key == \"explicit_aspects\" else 5, chars=300 if key == \"explicit_urls\" else 120)"` | — |
| [SRC-686F71AA50-L001269](../../agents/task_understanding.py#L1269) | 1269 | `"        for key in list_constraint_keys"` | — |
| [SRC-686F71AA50-L001270](../../agents/task_understanding.py#L1270) | 1270 | `"    }"` | — |
| [SRC-686F71AA50-L001271](../../agents/task_understanding.py#L1271) | 1271 | `"    for key in ("` | — |
| [SRC-686F71AA50-L001272](../../agents/task_understanding.py#L1272) | 1272 | `"        \"inline_text_supplied_for_summary\","` | — |
| [SRC-686F71AA50-L001273](../../agents/task_understanding.py#L1273) | 1273 | `"        \"time_sensitive_request\","` | — |
| [SRC-686F71AA50-L001274](../../agents/task_understanding.py#L1274) | 1274 | `"        \"official_site_required\","` | — |
| [SRC-686F71AA50-L001275](../../agents/task_understanding.py#L1275) | 1275 | `"        \"official_destination_required\","` | — |
| [SRC-686F71AA50-L001276](../../agents/task_understanding.py#L1276) | 1276 | `"        \"social_evidence_requested\","` | — |
| [SRC-686F71AA50-L001277](../../agents/task_understanding.py#L1277) | 1277 | `"    ):"` | — |
| [SRC-686F71AA50-L001278](../../agents/task_understanding.py#L1278) | 1278 | `"        constraints[key] = raw_constraints.get(key) is True"` | — |
| [SRC-686F71AA50-L001279](../../agents/task_understanding.py#L1279) | 1279 | `"    language_profile = raw_constraints.get(\"language_profile\")"` | — |
| [SRC-686F71AA50-L001280](../../agents/task_understanding.py#L1280) | 1280 | `"    constraints[\"language_profile\"] = ("` | — |
| [SRC-686F71AA50-L001281](../../agents/task_understanding.py#L1281) | 1281 | `"        language_profile"` | — |
| [SRC-686F71AA50-L001282](../../agents/task_understanding.py#L1282) | 1282 | `"        if isinstance(language_profile, str) and language_profile in {\"ar\", \"en\", \"mixed\", \"und\"}"` | — |
| [SRC-686F71AA50-L001283](../../agents/task_understanding.py#L1283) | 1283 | `"        else \"und\""` | — |
| [SRC-686F71AA50-L001284](../../agents/task_understanding.py#L1284) | 1284 | `"    )"` | — |
| [SRC-686F71AA50-L001285](../../agents/task_understanding.py#L1285) | 1285 | `"    allowed_source_policies = {"` | — |
| [SRC-686F71AA50-L001286](../../agents/task_understanding.py#L1286) | 1286 | `"        \"government_official_destination\", \"official_destination\", \"current_read_page\","` | — |
| [SRC-686F71AA50-L001287](../../agents/task_understanding.py#L1287) | 1287 | `"        \"public_social_content\", \"authoritative_health_content\", \"official_legal_text\","` | — |
| [SRC-686F71AA50-L001288](../../agents/task_understanding.py#L1288) | 1288 | `"        \"task_relevant_sources\", \"unassessed\","` | — |
| [SRC-686F71AA50-L001289](../../agents/task_understanding.py#L1289) | 1289 | `"    }"` | — |
| [SRC-686F71AA50-L001290](../../agents/task_understanding.py#L1290) | 1290 | `"    source_policy = clean_text(raw_constraints.get(\"source_policy\"), 80)"` | — |
| [SRC-686F71AA50-L001291](../../agents/task_understanding.py#L1291) | 1291 | `"    constraints[\"source_policy\"] = source_policy if source_policy in allowed_source_policies else \"unassessed\""` | — |
| [SRC-686F71AA50-L001292](../../agents/task_understanding.py#L1292) | 1292 | `"    constraints[\"source_policies\"] = ["` | — |
| [SRC-686F71AA50-L001293](../../agents/task_understanding.py#L1293) | 1293 | `"        item for item in constraints[\"source_policies\"]"` | — |
| [SRC-686F71AA50-L001294](../../agents/task_understanding.py#L1294) | 1294 | `"        if item in allowed_source_policies"` | — |
| [SRC-686F71AA50-L001295](../../agents/task_understanding.py#L1295) | 1295 | `"    ]"` | — |
| [SRC-686F71AA50-L001296](../../agents/task_understanding.py#L1296) | 1296 | `""` | — |
| [SRC-686F71AA50-L001297](../../agents/task_understanding.py#L1297) | 1297 | `"    raw_preferences = value.get(\"output_preferences\")"` | — |
| [SRC-686F71AA50-L001298](../../agents/task_understanding.py#L1298) | 1298 | `"    raw_preferences = raw_preferences if isinstance(raw_preferences, dict) else {}"` | — |
| [SRC-686F71AA50-L001299](../../agents/task_understanding.py#L1299) | 1299 | `"    preference_keys = ("` | — |
| [SRC-686F71AA50-L001300](../../agents/task_understanding.py#L1300) | 1300 | `"        \"concise\", \"detailed\", \"examples_requested\", \"table_requested\","` | — |
| [SRC-686F71AA50-L001301](../../agents/task_understanding.py#L1301) | 1301 | `"        \"bullets_or_checklist_requested\", \"beginner_friendly_requested\","` | — |
| [SRC-686F71AA50-L001302](../../agents/task_understanding.py#L1302) | 1302 | `"        \"citations_requested\", \"links_requested\", \"json_requested\","` | — |
| [SRC-686F71AA50-L001303](../../agents/task_understanding.py#L1303) | 1303 | `"    )"` | — |
| [SRC-686F71AA50-L001304](../../agents/task_understanding.py#L1304) | 1304 | `"    output_preferences = {key: raw_preferences.get(key) is True for key in preference_keys}"` | — |
| [SRC-686F71AA50-L001305](../../agents/task_understanding.py#L1305) | 1305 | `""` | — |
| [SRC-686F71AA50-L001306](../../agents/task_understanding.py#L1306) | 1306 | `"    raw_context = value.get(\"context_resolution\")"` | — |
| [SRC-686F71AA50-L001307](../../agents/task_understanding.py#L1307) | 1307 | `"    raw_context = raw_context if isinstance(raw_context, dict) else {}"` | — |
| [SRC-686F71AA50-L001308](../../agents/task_understanding.py#L1308) | 1308 | `"    raw_slots = raw_context.get(\"slots\")"` | — |
| [SRC-686F71AA50-L001309](../../agents/task_understanding.py#L1309) | 1309 | `"    slots: dict[str, str] = {}"` | — |
| [SRC-686F71AA50-L001310](../../agents/task_understanding.py#L1310) | 1310 | `"    if isinstance(raw_slots, dict):"` | — |
| [SRC-686F71AA50-L001311](../../agents/task_understanding.py#L1311) | 1311 | `"        for raw_key, raw_value in list(raw_slots.items())[:16]:"` | — |
| [SRC-686F71AA50-L001312](../../agents/task_understanding.py#L1312) | 1312 | `"            key = clean_text(raw_key, 40)"` | — |
| [SRC-686F71AA50-L001313](../../agents/task_understanding.py#L1313) | 1313 | `"            item = clean_text(raw_value, 180)"` | — |
| [SRC-686F71AA50-L001314](../../agents/task_understanding.py#L1314) | 1314 | `"            if key and item:"` | — |
| [SRC-686F71AA50-L001315](../../agents/task_understanding.py#L1315) | 1315 | `"                slots[key] = item"` | — |
| [SRC-686F71AA50-L001316](../../agents/task_understanding.py#L1316) | 1316 | `"    context_resolution = {"` | — |
| [SRC-686F71AA50-L001317](../../agents/task_understanding.py#L1317) | 1317 | `"        \"method\": clean_text(raw_context.get(\"method\"), 80) or \"not_provided\","` | — |
| [SRC-686F71AA50-L001318](../../agents/task_understanding.py#L1318) | 1318 | `"        \"resolved_question\": clean_text(raw_context.get(\"resolved_question\"), MAX_TASK_CHARS),"` | — |
| [SRC-686F71AA50-L001319](../../agents/task_understanding.py#L1319) | 1319 | `"        \"topic\": clean_text(raw_context.get(\"topic\"), 180),"` | — |
| [SRC-686F71AA50-L001320](../../agents/task_understanding.py#L1320) | 1320 | `"        \"entities\": clean_list(raw_context.get(\"entities\"), items=8, chars=120),"` | — |
| [SRC-686F71AA50-L001321](../../agents/task_understanding.py#L1321) | 1321 | `"        \"slots\": slots,"` | — |
| [SRC-686F71AA50-L001322](../../agents/task_understanding.py#L1322) | 1322 | `"        \"changed_slots\": clean_list(raw_context.get(\"changed_slots\"), items=8, chars=40),"` | — |
| [SRC-686F71AA50-L001323](../../agents/task_understanding.py#L1323) | 1323 | `"        \"is_follow_up\": raw_context.get(\"is_follow_up\") is True,"` | — |
| [SRC-686F71AA50-L001324](../../agents/task_understanding.py#L1324) | 1324 | `"        \"topic_shift\": raw_context.get(\"topic_shift\") is True,"` | — |
| [SRC-686F71AA50-L001325](../../agents/task_understanding.py#L1325) | 1325 | `"        \"resolution_basis\": clean_text(raw_context.get(\"resolution_basis\"), 80) or \"unassessed\","` | — |
| [SRC-686F71AA50-L001326](../../agents/task_understanding.py#L1326) | 1326 | `"        \"confidence_band\": ("` | — |
| [SRC-686F71AA50-L001327](../../agents/task_understanding.py#L1327) | 1327 | `"            raw_context.get(\"confidence_band\")"` | — |
| [SRC-686F71AA50-L001328](../../agents/task_understanding.py#L1328) | 1328 | `"            if isinstance(raw_context.get(\"confidence_band\"), str)"` | — |
| [SRC-686F71AA50-L001329](../../agents/task_understanding.py#L1329) | 1329 | `"            and raw_context.get(\"confidence_band\") in {\"low\", \"medium\", \"high\", \"unassessed\"}"` | — |
| [SRC-686F71AA50-L001330](../../agents/task_understanding.py#L1330) | 1330 | `"            else \"unassessed\""` | — |
| [SRC-686F71AA50-L001331](../../agents/task_understanding.py#L1331) | 1331 | `"        ),"` | — |
| [SRC-686F71AA50-L001332](../../agents/task_understanding.py#L1332) | 1332 | `"        \"needs_clarification\": raw_context.get(\"needs_clarification\") is True,"` | — |
| [SRC-686F71AA50-L001333](../../agents/task_understanding.py#L1333) | 1333 | `"        \"unresolved_references\": clean_list(raw_context.get(\"unresolved_references\"), items=8, chars=100),"` | — |
| [SRC-686F71AA50-L001334](../../agents/task_understanding.py#L1334) | 1334 | `"    }"` | — |
| [SRC-686F71AA50-L001335](../../agents/task_understanding.py#L1335) | 1335 | `""` | — |
| [SRC-686F71AA50-L001336](../../agents/task_understanding.py#L1336) | 1336 | `"    raw_hypotheses = value.get(\"hypothesis_interpretations\")"` | — |
| [SRC-686F71AA50-L001337](../../agents/task_understanding.py#L1337) | 1337 | `"    hypotheses: list[dict[str, Any]] = []"` | — |
| [SRC-686F71AA50-L001338](../../agents/task_understanding.py#L1338) | 1338 | `"    if isinstance(raw_hypotheses, list):"` | — |
| [SRC-686F71AA50-L001339](../../agents/task_understanding.py#L1339) | 1339 | `"        for item in raw_hypotheses[:8]:"` | — |
| [SRC-686F71AA50-L001340](../../agents/task_understanding.py#L1340) | 1340 | `"            if not isinstance(item, dict):"` | — |
| [SRC-686F71AA50-L001341](../../agents/task_understanding.py#L1341) | 1341 | `"                continue"` | — |
| [SRC-686F71AA50-L001342](../../agents/task_understanding.py#L1342) | 1342 | `"            count = item.get(\"matched_signal_count\")"` | — |
| [SRC-686F71AA50-L001343](../../agents/task_understanding.py#L1343) | 1343 | `"            hypotheses.append({"` | — |
| [SRC-686F71AA50-L001344](../../agents/task_understanding.py#L1344) | 1344 | `"                \"family\": clean_text(item.get(\"family\"), 80),"` | — |
| [SRC-686F71AA50-L001345](../../agents/task_understanding.py#L1345) | 1345 | `"                \"matched_signal_count\": max(0, min(32, count)) if isinstance(count, int) else 0,"` | — |
| [SRC-686F71AA50-L001346](../../agents/task_understanding.py#L1346) | 1346 | `"                \"signals\": clean_list(item.get(\"signals\"), items=4, chars=100),"` | — |
| [SRC-686F71AA50-L001347](../../agents/task_understanding.py#L1347) | 1347 | `"                \"status\": clean_text(item.get(\"status\"), 60) or \"unassessed\","` | — |
| [SRC-686F71AA50-L001348](../../agents/task_understanding.py#L1348) | 1348 | `"                \"selected\": item.get(\"selected\") is True,"` | — |
| [SRC-686F71AA50-L001349](../../agents/task_understanding.py#L1349) | 1349 | `"            })"` | — |
| [SRC-686F71AA50-L001350](../../agents/task_understanding.py#L1350) | 1350 | `""` | — |
| [SRC-686F71AA50-L001351](../../agents/task_understanding.py#L1351) | 1351 | `"    allowed_families = {"` | — |
| [SRC-686F71AA50-L001352](../../agents/task_understanding.py#L1352) | 1352 | `"        name for name in _PATTERNS if not name.startswith(\"output_\")"` | — |
| [SRC-686F71AA50-L001353](../../agents/task_understanding.py#L1353) | 1353 | `"    } \| {\"general_question\", \"ambiguous_or_incomplete\", \"web_research\"}"` | — |
| [SRC-686F71AA50-L001354](../../agents/task_understanding.py#L1354) | 1354 | `"    raw_family = clean_text(value.get(\"task_family\"), 80)"` | — |
| [SRC-686F71AA50-L001355](../../agents/task_understanding.py#L1355) | 1355 | `"    raw_mode = clean_text(value.get(\"mode\"), 20)"` | — |
| [SRC-686F71AA50-L001356](../../agents/task_understanding.py#L1356) | 1356 | `"    raw_route = clean_text(value.get(\"intent_route\"), 40)"` | — |
| [SRC-686F71AA50-L001357](../../agents/task_understanding.py#L1357) | 1357 | `"    allowed_routes = {"` | — |
| [SRC-686F71AA50-L001358](../../agents/task_understanding.py#L1358) | 1358 | `"        \"LOCAL\", \"MODEL_ONLY\", \"CLARIFY\", \"WEB_SIMPLE\", \"WEB_DEEP\","` | — |
| [SRC-686F71AA50-L001359](../../agents/task_understanding.py#L1359) | 1359 | `"        \"LEAD_GENERATION\", \"BUDGET_EXHAUSTED\", \"deterministic_fallback\","` | — |
| [SRC-686F71AA50-L001360](../../agents/task_understanding.py#L1360) | 1360 | `"        \"validated_language_model_plan\", \"unassessed\","` | — |
| [SRC-686F71AA50-L001361](../../agents/task_understanding.py#L1361) | 1361 | `"    }"` | — |
| [SRC-686F71AA50-L001362](../../agents/task_understanding.py#L1362) | 1362 | `"    allowed_tools = {"` | — |
| [SRC-686F71AA50-L001363](../../agents/task_understanding.py#L1363) | 1363 | `"        \"web_search\", \"page_fetch\", \"public_social_search_if_configured\","` | — |
| [SRC-686F71AA50-L001364](../../agents/task_understanding.py#L1364) | 1364 | `"        \"language_model_generation_if_configured\", \"claim_review_if_configured\","` | — |
| [SRC-686F71AA50-L001365](../../agents/task_understanding.py#L1365) | 1365 | `"    }"` | — |
| [SRC-686F71AA50-L001366](../../agents/task_understanding.py#L1366) | 1366 | `"    allowed_slots = {"` | — |
| [SRC-686F71AA50-L001367](../../agents/task_understanding.py#L1367) | 1367 | `"        \"aspect\", \"audience\", \"budget\", \"capacity\", \"country\", \"currency\","` | — |
| [SRC-686F71AA50-L001368](../../agents/task_understanding.py#L1368) | 1368 | `"        \"entity\", \"goal\", \"language\", \"location\", \"model\", \"platform\","` | — |
| [SRC-686F71AA50-L001369](../../agents/task_understanding.py#L1369) | 1369 | `"        \"product\", \"time_range\", \"variant\", \"version\","` | — |
| [SRC-686F71AA50-L001370](../../agents/task_understanding.py#L1370) | 1370 | `"    }"` | — |
| [SRC-686F71AA50-L001371](../../agents/task_understanding.py#L1371) | 1371 | `"    context_resolution[\"slots\"] = {"` | — |
| [SRC-686F71AA50-L001372](../../agents/task_understanding.py#L1372) | 1372 | `"        key: item for key, item in context_resolution[\"slots\"].items()"` | — |
| [SRC-686F71AA50-L001373](../../agents/task_understanding.py#L1373) | 1373 | `"        if key in allowed_slots"` | — |
| [SRC-686F71AA50-L001374](../../agents/task_understanding.py#L1374) | 1374 | `"    }"` | — |
| [SRC-686F71AA50-L001375](../../agents/task_understanding.py#L1375) | 1375 | `"    hypotheses = ["` | — |
| [SRC-686F71AA50-L001376](../../agents/task_understanding.py#L1376) | 1376 | `"        item for item in hypotheses"` | — |
| [SRC-686F71AA50-L001377](../../agents/task_understanding.py#L1377) | 1377 | `"        if item.get(\"family\") in allowed_families"` | — |
| [SRC-686F71AA50-L001378](../../agents/task_understanding.py#L1378) | 1378 | `"    ]"` | — |
| [SRC-686F71AA50-L001379](../../agents/task_understanding.py#L1379) | 1379 | `"    raw_secondary = clean_list(value.get(\"secondary_task_types\"), items=16, chars=80)"` | — |
| [SRC-686F71AA50-L001380](../../agents/task_understanding.py#L1380) | 1380 | `"    spec = {"` | — |
| [SRC-686F71AA50-L001381](../../agents/task_understanding.py#L1381) | 1381 | `"        \"schema\": \"omarai.task_spec.v1\","` | — |
| [SRC-686F71AA50-L001382](../../agents/task_understanding.py#L1382) | 1382 | `"        \"task_family\": raw_family if raw_family in allowed_families else \"general_question\","` | — |
| [SRC-686F71AA50-L001383](../../agents/task_understanding.py#L1383) | 1383 | `"        \"mode\": raw_mode if raw_mode in SUPPORTED_MODES else \"auto\","` | — |
| [SRC-686F71AA50-L001384](../../agents/task_understanding.py#L1384) | 1384 | `"        \"intent_route\": raw_route if raw_route in allowed_routes else \"unassessed\","` | — |
| [SRC-686F71AA50-L001385](../../agents/task_understanding.py#L1385) | 1385 | `"        \"classification_method\": clean_text(value.get(\"classification_method\"), 100),"` | — |
| [SRC-686F71AA50-L001386](../../agents/task_understanding.py#L1386) | 1386 | `"        \"classification_is_probability\": False,"` | — |
| [SRC-686F71AA50-L001387](../../agents/task_understanding.py#L1387) | 1387 | `"        \"ambiguity_status\": clean_text(value.get(\"ambiguity_status\"), 80) or \"unassessed\","` | — |
| [SRC-686F71AA50-L001388](../../agents/task_understanding.py#L1388) | 1388 | `"        \"missing_required_inputs\": ["` | — |
| [SRC-686F71AA50-L001389](../../agents/task_understanding.py#L1389) | 1389 | `"            item for item in clean_list(value.get(\"missing_required_inputs\"), items=8, chars=100)"` | — |
| [SRC-686F71AA50-L001390](../../agents/task_understanding.py#L1390) | 1390 | `"            if item in {"` | — |
| [SRC-686F71AA50-L001391](../../agents/task_understanding.py#L1391) | 1391 | `"                \"unresolved_referent_or_incomplete_request\","` | — |
| [SRC-686F71AA50-L001392](../../agents/task_understanding.py#L1392) | 1392 | `"                \"official_destination_target_entity\","` | — |
| [SRC-686F71AA50-L001393](../../agents/task_understanding.py#L1393) | 1393 | `"                \"summary_source_url_or_pasted_text\","` | — |
| [SRC-686F71AA50-L001394](../../agents/task_understanding.py#L1394) | 1394 | `"            }"` | — |
| [SRC-686F71AA50-L001395](../../agents/task_understanding.py#L1395) | 1395 | `"        ],"` | — |
| [SRC-686F71AA50-L001396](../../agents/task_understanding.py#L1396) | 1396 | `"        \"requires_clarification\": value.get(\"requires_clarification\") is True,"` | — |
| [SRC-686F71AA50-L001397](../../agents/task_understanding.py#L1397) | 1397 | `"        \"clarification_reason\": clean_text(value.get(\"clarification_reason\"), 80) or \"unassessed\","` | — |
| [SRC-686F71AA50-L001398](../../agents/task_understanding.py#L1398) | 1398 | `"        \"context_resolution\": context_resolution,"` | — |
| [SRC-686F71AA50-L001399](../../agents/task_understanding.py#L1399) | 1399 | `"        \"secondary_task_types\": ["` | — |
| [SRC-686F71AA50-L001400](../../agents/task_understanding.py#L1400) | 1400 | `"            item for item in raw_secondary if item in allowed_families"` | — |
| [SRC-686F71AA50-L001401](../../agents/task_understanding.py#L1401) | 1401 | `"        ],"` | — |
| [SRC-686F71AA50-L001402](../../agents/task_understanding.py#L1402) | 1402 | `"        \"constraints\": constraints,"` | — |
| [SRC-686F71AA50-L001403](../../agents/task_understanding.py#L1403) | 1403 | `"        \"output_preferences\": output_preferences,"` | — |
| [SRC-686F71AA50-L001404](../../agents/task_understanding.py#L1404) | 1404 | `"        \"evidence_requirements\": clean_list(value.get(\"evidence_requirements\"), items=32, chars=180),"` | — |
| [SRC-686F71AA50-L001405](../../agents/task_understanding.py#L1405) | 1405 | `"        \"query_strategies\": clean_list(value.get(\"query_strategies\"), items=32, chars=100),"` | — |
| [SRC-686F71AA50-L001406](../../agents/task_understanding.py#L1406) | 1406 | `"        \"tool_requirements\": ["` | — |
| [SRC-686F71AA50-L001407](../../agents/task_understanding.py#L1407) | 1407 | `"            item for item in clean_list(value.get(\"tool_requirements\"), items=12, chars=100)"` | — |
| [SRC-686F71AA50-L001408](../../agents/task_understanding.py#L1408) | 1408 | `"            if item in allowed_tools"` | — |
| [SRC-686F71AA50-L001409](../../agents/task_understanding.py#L1409) | 1409 | `"        ],"` | — |
| [SRC-686F71AA50-L001410](../../agents/task_understanding.py#L1410) | 1410 | `"        \"decision_checks\": clean_list(value.get(\"decision_checks\"), items=24, chars=120),"` | — |
| [SRC-686F71AA50-L001411](../../agents/task_understanding.py#L1411) | 1411 | `"        \"reasoning_strategy_ids\": ["` | — |
| [SRC-686F71AA50-L001412](../../agents/task_understanding.py#L1412) | 1412 | `"            item for item in clean_list(value.get(\"reasoning_strategy_ids\"), items=12, chars=80)"` | — |
| [SRC-686F71AA50-L001413](../../agents/task_understanding.py#L1413) | 1413 | `"            if item in _REASONING_GUIDANCE"` | — |
| [SRC-686F71AA50-L001414](../../agents/task_understanding.py#L1414) | 1414 | `"        ],"` | — |
| [SRC-686F71AA50-L001415](../../agents/task_understanding.py#L1415) | 1415 | `"        # The matrix is code-owned. Ignore arbitrary incoming rows and return the"` | — |
| [SRC-686F71AA50-L001416](../../agents/task_understanding.py#L1416) | 1416 | `"        # canonical allowlisted policy so untrusted task/planner data cannot rewrite it."` | — |
| [SRC-686F71AA50-L001417](../../agents/task_understanding.py#L1417) | 1417 | `"        \"decision_matrix\": [dict(row) for row in _DECISION_MATRIX],"` | — |
| [SRC-686F71AA50-L001418](../../agents/task_understanding.py#L1418) | 1418 | `"        \"hypothesis_interpretations\": hypotheses,"` | — |
| [SRC-686F71AA50-L001419](../../agents/task_understanding.py#L1419) | 1419 | `"        \"limits\": {"` | — |
| [SRC-686F71AA50-L001420](../../agents/task_understanding.py#L1420) | 1420 | `"            \"max_question_chars\": MAX_TASK_CHARS,"` | — |
| [SRC-686F71AA50-L001421](../../agents/task_understanding.py#L1421) | 1421 | `"            \"max_aspects\": MAX_TASK_ASPECTS,"` | — |
| [SRC-686F71AA50-L001422](../../agents/task_understanding.py#L1422) | 1422 | `"            \"max_query_strategies\": MAX_STRATEGY_QUERIES,"` | — |
| [SRC-686F71AA50-L001423](../../agents/task_understanding.py#L1423) | 1423 | `"        },"` | — |
| [SRC-686F71AA50-L001424](../../agents/task_understanding.py#L1424) | 1424 | `"        \"claim\": \"task planning metadata only; not semantic certainty or factual verification\","` | — |
| [SRC-686F71AA50-L001425](../../agents/task_understanding.py#L1425) | 1425 | `"    }"` | — |
| [SRC-686F71AA50-L001426](../../agents/task_understanding.py#L1426) | 1426 | `"    for key in (\"planner_freshness\", \"planner_depth\"):"` | — |
| [SRC-686F71AA50-L001427](../../agents/task_understanding.py#L1427) | 1427 | `"        if key in value:"` | — |
| [SRC-686F71AA50-L001428](../../agents/task_understanding.py#L1428) | 1428 | `"            spec[key] = clean_text(value.get(key), 40) or \"unknown\""` | — |
| [SRC-686F71AA50-L001429](../../agents/task_understanding.py#L1429) | 1429 | `"    return spec"` | — |
## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L000001](../../agents/web_agent.py#L1) | 1 | `"\"\"\"Grounded natural-language web research for Omarai."` | — |
| [SRC-1AE03B9EC3-L000002](../../agents/web_agent.py#L2) | 2 | `""` | — |
| [SRC-1AE03B9EC3-L000003](../../agents/web_agent.py#L3) | 3 | `"Searches public web results, extracts a small amount of page text, then asks an"` | — |
| [SRC-1AE03B9EC3-L000004](../../agents/web_agent.py#L4) | 4 | `"OpenAI-compatible language model to answer in the user's language with sources."` | — |
| [SRC-1AE03B9EC3-L000005](../../agents/web_agent.py#L5) | 5 | `"API credentials are read only from environment variables and are never returned."` | — |
| [SRC-1AE03B9EC3-L000006](../../agents/web_agent.py#L6) | 6 | `"\"\"\""` | — |
| [SRC-1AE03B9EC3-L000007](../../agents/web_agent.py#L7) | 7 | `"from __future__ import annotations"` | — |
| [SRC-1AE03B9EC3-L000008](../../agents/web_agent.py#L8) | 8 | `""` | — |
| [SRC-1AE03B9EC3-L000009](../../agents/web_agent.py#L9) | 9 | `"import asyncio"` | — |
| [SRC-1AE03B9EC3-L000010](../../agents/web_agent.py#L10) | 10 | `"import datetime as dt"` | — |
| [SRC-1AE03B9EC3-L000011](../../agents/web_agent.py#L11) | 11 | `"import ipaddress"` | — |
| [SRC-1AE03B9EC3-L000012](../../agents/web_agent.py#L12) | 12 | `"import json"` | — |
| [SRC-1AE03B9EC3-L000013](../../agents/web_agent.py#L13) | 13 | `"import os"` | — |
| [SRC-1AE03B9EC3-L000014](../../agents/web_agent.py#L14) | 14 | `"import re"` | — |
| [SRC-1AE03B9EC3-L000015](../../agents/web_agent.py#L15) | 15 | `"import socket"` | — |
| [SRC-1AE03B9EC3-L000016](../../agents/web_agent.py#L16) | 16 | `"import threading"` | — |
| [SRC-1AE03B9EC3-L000017](../../agents/web_agent.py#L17) | 17 | `"import unicodedata"` | — |
| [SRC-1AE03B9EC3-L000018](../../agents/web_agent.py#L18) | 18 | `"import urllib.error"` | — |
| [SRC-1AE03B9EC3-L000019](../../agents/web_agent.py#L19) | 19 | `"import urllib.parse"` | — |
| [SRC-1AE03B9EC3-L000020](../../agents/web_agent.py#L20) | 20 | `"import urllib.request"` | — |
| [SRC-1AE03B9EC3-L000021](../../agents/web_agent.py#L21) | 21 | `"from concurrent.futures import ThreadPoolExecutor, as_completed"` | — |
| [SRC-1AE03B9EC3-L000022](../../agents/web_agent.py#L22) | 22 | `"from typing import Any"` | — |
| [SRC-1AE03B9EC3-L000023](../../agents/web_agent.py#L23) | 23 | `""` | — |
| [SRC-1AE03B9EC3-L000024](../../agents/web_agent.py#L24) | 24 | `"from agents.intent_router import resolve_followup_query, route_intent"` | — |
| [SRC-1AE03B9EC3-L000025](../../agents/web_agent.py#L25) | 25 | `"from agents.dialogue_state import ("` | — |
| [SRC-1AE03B9EC3-L000026](../../agents/web_agent.py#L26) | 26 | `"    fallback_dialogue_context,"` | — |
| [SRC-1AE03B9EC3-L000027](../../agents/web_agent.py#L27) | 27 | `"    might_be_context_dependent,"` | — |
| [SRC-1AE03B9EC3-L000028](../../agents/web_agent.py#L28) | 28 | `"    validate_dialogue_context,"` | — |
| [SRC-1AE03B9EC3-L000029](../../agents/web_agent.py#L29) | 29 | `")"` | — |
| [SRC-1AE03B9EC3-L000030](../../agents/web_agent.py#L30) | 30 | `"from agents.answer_validation import audit_answer_integrity"` | — |
| [SRC-1AE03B9EC3-L000031](../../agents/web_agent.py#L31) | 31 | `"from agents.claim_evidence import build_claim_evidence_ledger"` | — |
| [SRC-1AE03B9EC3-L000032](../../agents/web_agent.py#L32) | 32 | `"from agents.request_budget import RequestBudget, RequestBudgetExceeded"` | — |
| [SRC-1AE03B9EC3-L000033](../../agents/web_agent.py#L33) | 33 | `"from agents.aspect_planning import ("` | — |
| [SRC-1AE03B9EC3-L000034](../../agents/web_agent.py#L34) | 34 | `"    arabic_aspect_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L000035](../../agents/web_agent.py#L35) | 35 | `"    build_evidence_ledger,"` | — |
| [SRC-1AE03B9EC3-L000036](../../agents/web_agent.py#L36) | 36 | `"    extract_aspects,"` | — |
| [SRC-1AE03B9EC3-L000037](../../agents/web_agent.py#L37) | 37 | `"    repair_queries_for_missing_aspects,"` | — |
| [SRC-1AE03B9EC3-L000038](../../agents/web_agent.py#L38) | 38 | `")"` | — |
| [SRC-1AE03B9EC3-L000039](../../agents/web_agent.py#L39) | 39 | `"from agents.search_connectors import search_arxiv, search_crossref, search_openalex"` | — |
| [SRC-1AE03B9EC3-L000040](../../agents/web_agent.py#L40) | 40 | `"from agents.research import ("` | — |
| [SRC-1AE03B9EC3-L000041](../../agents/web_agent.py#L41) | 41 | `"    MAX_PLAN_QUERIES,"` | — |
| [SRC-1AE03B9EC3-L000042](../../agents/web_agent.py#L42) | 42 | `"    SOCIAL_DOMAINS,"` | — |
| [SRC-1AE03B9EC3-L000043](../../agents/web_agent.py#L43) | 43 | `"    compact_search_query,"` | — |
| [SRC-1AE03B9EC3-L000044](../../agents/web_agent.py#L44) | 44 | `"    evidence_signal_report,"` | — |
| [SRC-1AE03B9EC3-L000045](../../agents/web_agent.py#L45) | 45 | `"    fallback_plan,"` | — |
| [SRC-1AE03B9EC3-L000046](../../agents/web_agent.py#L46) | 46 | `"    fuse_ranked_results,"` | — |
| [SRC-1AE03B9EC3-L000047](../../agents/web_agent.py#L47) | 47 | `"    registrable_domain,"` | — |
| [SRC-1AE03B9EC3-L000048](../../agents/web_agent.py#L48) | 48 | `"    validate_plan,"` | — |
| [SRC-1AE03B9EC3-L000049](../../agents/web_agent.py#L49) | 49 | `")"` | — |
| [SRC-1AE03B9EC3-L000050](../../agents/web_agent.py#L50) | 50 | `"from agents.research_guardrails import apply_source_guardrails"` | — |
| [SRC-1AE03B9EC3-L000051](../../agents/web_agent.py#L51) | 51 | `"from agents.task_understanding import ("` | — |
| [SRC-1AE03B9EC3-L000052](../../agents/web_agent.py#L52) | 52 | `"    build_query_strategy_matrix,"` | — |
| [SRC-1AE03B9EC3-L000053](../../agents/web_agent.py#L53) | 53 | `"    build_task_spec,"` | — |
| [SRC-1AE03B9EC3-L000054](../../agents/web_agent.py#L54) | 54 | `"    reasoning_guidance_for_task_spec,"` | — |
| [SRC-1AE03B9EC3-L000055](../../agents/web_agent.py#L55) | 55 | `"    validate_task_spec,"` | — |
| [SRC-1AE03B9EC3-L000056](../../agents/web_agent.py#L56) | 56 | `")"` | — |
| [SRC-1AE03B9EC3-L000057](../../agents/web_agent.py#L57) | 57 | `""` | — |
| [SRC-1AE03B9EC3-L000058](../../agents/web_agent.py#L58) | 58 | `"MAX_QUESTION_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000059](../../agents/web_agent.py#L59) | 59 | `"MAX_HISTORY_ITEMS = 8"` | — |
| [SRC-1AE03B9EC3-L000060](../../agents/web_agent.py#L60) | 60 | `"MAX_HISTORY_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000061](../../agents/web_agent.py#L61) | 61 | `"MAX_SEARCH_RESULTS = 18"` | — |
| [SRC-1AE03B9EC3-L000062](../../agents/web_agent.py#L62) | 62 | `"MAX_PROVIDER_RESULTS = 6"` | — |
| [SRC-1AE03B9EC3-L000063](../../agents/web_agent.py#L63) | 63 | `"MAX_FETCHED_PAGES = 8"` | — |
| [SRC-1AE03B9EC3-L000064](../../agents/web_agent.py#L64) | 64 | `"MAX_LLM_CITED_SOURCES = 12"` | — |
| [SRC-1AE03B9EC3-L000065](../../agents/web_agent.py#L65) | 65 | `"MAX_RESEARCH_WORKERS = 8"` | — |
| [SRC-1AE03B9EC3-L000066](../../agents/web_agent.py#L66) | 66 | `"MAX_PAGE_BYTES = 1_000_000"` | — |
| [SRC-1AE03B9EC3-L000067](../../agents/web_agent.py#L67) | 67 | `"MAX_PAGE_TEXT_CHARS = 12_000"` | — |
| [SRC-1AE03B9EC3-L000068](../../agents/web_agent.py#L68) | 68 | `"LLM_TIMEOUT_SECONDS = 35"` | — |
| [SRC-1AE03B9EC3-L000069](../../agents/web_agent.py#L69) | 69 | `""` | — |
| [SRC-1AE03B9EC3-L000070](../../agents/web_agent.py#L70) | 70 | `"# Only completed connector result-processing states positively confirm an attempt."` | — |
| [SRC-1AE03B9EC3-L000071](../../agents/web_agent.py#L71) | 71 | `"# A generic \"failed\" or timeout diagnostic may occur before a network request is sent."` | — |
| [SRC-1AE03B9EC3-L000072](../../agents/web_agent.py#L72) | 72 | `"_SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES = frozenset({\"ok\", \"no_results\", \"filtered_all\"})"` | — |
| [SRC-1AE03B9EC3-L000073](../../agents/web_agent.py#L73) | 73 | `"_RESEARCH_ERROR_OUTCOMES = frozenset({\"attempted_research_error\", \"unknown_after_research_error\"})"` | — |
| [SRC-1AE03B9EC3-L000074](../../agents/web_agent.py#L74) | 74 | `"_PROVIDER_REJECTION_REASONS = ("` | — |
| [SRC-1AE03B9EC3-L000075](../../agents/web_agent.py#L75) | 75 | `"    \"malformed_candidate\","` | — |
| [SRC-1AE03B9EC3-L000076](../../agents/web_agent.py#L76) | 76 | `"    \"invalid_url_or_unsafe_target\","` | — |
| [SRC-1AE03B9EC3-L000077](../../agents/web_agent.py#L77) | 77 | `"    \"blocked_domain\","` | — |
| [SRC-1AE03B9EC3-L000078](../../agents/web_agent.py#L78) | 78 | `"    \"relevance_below_threshold\","` | — |
| [SRC-1AE03B9EC3-L000079](../../agents/web_agent.py#L79) | 79 | `")"` | — |
| [SRC-1AE03B9EC3-L000080](../../agents/web_agent.py#L80) | 80 | `""` | — |
| [SRC-1AE03B9EC3-L000081](../../agents/web_agent.py#L81) | 81 | `""` | — |
| [SRC-1AE03B9EC3-L000082](../../agents/web_agent.py#L82) | 82 | `"_ARABIC_SEARCH_TRANSLATION = str.maketrans({"` | — |
| [SRC-1AE03B9EC3-L000083](../../agents/web_agent.py#L83) | 83 | `"    \"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ٱ\": \"ا\", \"ى\": \"ي\","` | — |
| [SRC-1AE03B9EC3-L000084](../../agents/web_agent.py#L84) | 84 | `"    \"ؤ\": \"و\", \"ئ\": \"ي\", \"ة\": \"ه\", \"ـ\": \"\","` | — |
| [SRC-1AE03B9EC3-L000085](../../agents/web_agent.py#L85) | 85 | `"})"` | — |
| [SRC-1AE03B9EC3-L000086](../../agents/web_agent.py#L86) | 86 | `"_ARABIC_DIACRITICS_RE = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-1AE03B9EC3-L000087](../../agents/web_agent.py#L87) | 87 | `"_SEARCH_STOPWORDS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000088](../../agents/web_agent.py#L88) | 88 | `"    \"ما\", \"ماذا\", \"من\", \"في\", \"على\", \"عن\", \"الى\", \"إلى\", \"و\", \"او\", \"أو\","` | — |
| [SRC-1AE03B9EC3-L000089](../../agents/web_agent.py#L89) | 89 | `"    \"هل\", \"هو\", \"هي\", \"هذا\", \"هذه\", \"ذلك\", \"تلك\", \"التي\", \"الذي\", \"مع\","` | — |
| [SRC-1AE03B9EC3-L000090](../../agents/web_agent.py#L90) | 90 | `"    \"بين\", \"كيف\", \"لماذا\", \"كم\", \"كان\", \"كانت\", \"يكون\", \"تكون\", \"لي\","` | — |
| [SRC-1AE03B9EC3-L000091](../../agents/web_agent.py#L91) | 91 | `"    \"the\", \"a\", \"an\", \"and\", \"or\", \"in\", \"on\", \"of\", \"to\", \"for\", \"with\","` | — |
| [SRC-1AE03B9EC3-L000092](../../agents/web_agent.py#L92) | 92 | `"    \"is\", \"are\", \"was\", \"were\", \"what\", \"which\", \"who\", \"how\", \"why\", \"when\","` | — |
| [SRC-1AE03B9EC3-L000093](../../agents/web_agent.py#L93) | 93 | `"    \"where\", \"compare\", \"comparison\", \"please\", \"show\", \"find\", \"latest\","` | — |
| [SRC-1AE03B9EC3-L000094](../../agents/web_agent.py#L94) | 94 | `"    \"news\", \"official\", \"sources\", \"source\", \"reports\", \"report\", \"analysis\","` | — |
| [SRC-1AE03B9EC3-L000095](../../agents/web_agent.py#L95) | 95 | `"    \"site\", \"com\", \"org\", \"net\", \"www\","` | — |
| [SRC-1AE03B9EC3-L000096](../../agents/web_agent.py#L96) | 96 | `"    # Arabic request/format words are not useful topic concepts for matching search snippets."` | — |
| [SRC-1AE03B9EC3-L000097](../../agents/web_agent.py#L97) | 97 | `"    \"اذكر\", \"مصدر\", \"مصادر\", \"موثوق\", \"موثوقة\", \"رابط\", \"روابط\", \"مباشر\","` | — |
| [SRC-1AE03B9EC3-L000098](../../agents/web_agent.py#L98) | 98 | `"    \"مباشرة\", \"اجب\", \"بالعربية\", \"العربية\", \"بايجاز\", \"بالايجاز\", \"ايجاز\","` | — |
| [SRC-1AE03B9EC3-L000099](../../agents/web_agent.py#L99) | 99 | `"    \"باختصار\", \"اختصار\", \"استخدم\", \"اعرض\", \"وضح\", \"حلل\", \"قارن\", \"متعددة\","` | — |
| [SRC-1AE03B9EC3-L000100](../../agents/web_agent.py#L100) | 100 | `"    \"اهم\", \"الحقائق\", \"حقائق\", \"استنتاج\", \"استنتاجات\", \"الاستنتاجات\","` | — |
| [SRC-1AE03B9EC3-L000101](../../agents/web_agent.py#L101) | 101 | `"    \"تواريخ\", \"تاريخ\", \"الاخبار\", \"اخبار\", \"المصادر\", \"معلومات\", \"قديمة\","` | — |
| [SRC-1AE03B9EC3-L000102](../../agents/web_agent.py#L102) | 102 | `"    \"قديمه\", \"جديدة\", \"جديده\", \"خلال\", \"الايام\", \"ايام\", \"السبعة\", \"سبعة\","` | — |
| [SRC-1AE03B9EC3-L000103](../../agents/web_agent.py#L103) | 103 | `"    \"الماضية\", \"ماضية\", \"الاسبوع\", \"حاليا\", \"الان\", \"احدث\", \"ولا\","` | — |
| [SRC-1AE03B9EC3-L000104](../../agents/web_agent.py#L104) | 104 | `"    \"تعرض\", \"باعتبارها\","` | — |
| [SRC-1AE03B9EC3-L000105](../../agents/web_agent.py#L105) | 105 | `"})"` | — |
| [SRC-1AE03B9EC3-L000106](../../agents/web_agent.py#L106) | 106 | `"# Search-expansion modifiers are useful after a real topic, but must not stand in"` | — |
| [SRC-1AE03B9EC3-L000107](../../agents/web_agent.py#L107) | 107 | `"# for a topic if a future planner/expansion path loses its subject."` | — |
| [SRC-1AE03B9EC3-L000108](../../agents/web_agent.py#L108) | 108 | `"_GENERIC_QUERY_MODIFIER_TOKENS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000109](../../agents/web_agent.py#L109) | 109 | `"    \"risk\", \"risks\", \"limitation\", \"limitations\", \"alternative\", \"alternatives\","` | — |
| [SRC-1AE03B9EC3-L000110](../../agents/web_agent.py#L110) | 110 | `"    \"recent\", \"data\", \"review\", \"reviews\", \"comparison\", \"compare\", \"official\","` | — |
| [SRC-1AE03B9EC3-L000111](../../agents/web_agent.py#L111) | 111 | `"    \"primary\", \"source\", \"sources\", \"evidence\", \"report\", \"reports\", \"case\", \"cases\","` | — |
| [SRC-1AE03B9EC3-L000112](../../agents/web_agent.py#L112) | 112 | `"    \"study\", \"studies\", \"analysis\", \"latest\", \"news\", \"update\", \"updates\","` | — |
| [SRC-1AE03B9EC3-L000113](../../agents/web_agent.py#L113) | 113 | `"    \"announcement\", \"announcements\", \"comprehensive\", \"research\", \"statistic\","` | — |
| [SRC-1AE03B9EC3-L000114](../../agents/web_agent.py#L114) | 114 | `"    \"statistics\", \"trend\", \"trends\","` | — |
| [SRC-1AE03B9EC3-L000115](../../agents/web_agent.py#L115) | 115 | `"})"` | — |
| [SRC-1AE03B9EC3-L000116](../../agents/web_agent.py#L116) | 116 | `"_SEARCH_SYNONYMS = {"` | — |
| [SRC-1AE03B9EC3-L000117](../../agents/web_agent.py#L117) | 117 | `"    \"استراليا\": {\"australia\"}, \"عاصمة\": {\"capital\"}, \"مصر\": {\"egypt\"},"` | — |
| [SRC-1AE03B9EC3-L000118](../../agents/web_agent.py#L118) | 118 | `"    \"المصري\": {\"egyptian\", \"egypt\"}, \"مركزي\": {\"central\"},"` | — |
| [SRC-1AE03B9EC3-L000119](../../agents/web_agent.py#L119) | 119 | `"    \"المركزي\": {\"central\"}, \"بنك\": {\"bank\"}, \"البنك\": {\"bank\"},"` | — |
| [SRC-1AE03B9EC3-L000120](../../agents/web_agent.py#L120) | 120 | `"    \"قرار\": {\"decision\"}, \"قرارات\": {\"decision\", \"decisions\"},"` | — |
| [SRC-1AE03B9EC3-L000121](../../agents/web_agent.py#L121) | 121 | `"    \"سعر\": {\"price\"}, \"اسعار\": {\"prices\"}, \"استضافة\": {\"hosting\"},"` | — |
| [SRC-1AE03B9EC3-L000122](../../agents/web_agent.py#L122) | 122 | `"    \"شركة\": {\"company\"}, \"شركه\": {\"company\"}, \"ناشئة\": {\"startup\"},"` | — |
| [SRC-1AE03B9EC3-L000123](../../agents/web_agent.py#L123) | 123 | `"    \"صعيد\": {\"upper\"}, \"مقارنة\": {\"compare\", \"comparison\"},"` | — |
| [SRC-1AE03B9EC3-L000124](../../agents/web_agent.py#L124) | 124 | `"    \"تقنية\": {\"technology\"}, \"تقنيات\": {\"technology\"},"` | — |
| [SRC-1AE03B9EC3-L000125](../../agents/web_agent.py#L125) | 125 | `"    \"ميكروسوفت\": {\"microsoft\"}, \"مايكروسوفت\": {\"microsoft\"},"` | — |
| [SRC-1AE03B9EC3-L000126](../../agents/web_agent.py#L126) | 126 | `"    \"microsoft\": {\"ميكروسوفت\", \"مايكروسوفت\"},"` | — |
| [SRC-1AE03B9EC3-L000127](../../agents/web_agent.py#L127) | 127 | `"    \"جمهورية\": {\"republic\"}, \"republic\": {\"جمهورية\"},"` | — |
| [SRC-1AE03B9EC3-L000128](../../agents/web_agent.py#L128) | 128 | `"    \"الرقمية\": {\"digital\"}, \"رقمية\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000129](../../agents/web_agent.py#L129) | 129 | `"    \"الرقميه\": {\"digital\"}, \"رقميه\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000130](../../agents/web_agent.py#L130) | 130 | `"    \"موقع\": {\"website\", \"portal\"}, \"مواقع\": {\"websites\", \"portals\"},"` | — |
| [SRC-1AE03B9EC3-L000131](../../agents/web_agent.py#L131) | 131 | `"    \"التجمع\": {\"settlement\"}, \"تجمع\": {\"settlement\"},"` | — |
| [SRC-1AE03B9EC3-L000132](../../agents/web_agent.py#L132) | 132 | `"    \"الخامس\": {\"fifth\", \"5th\"}, \"خامس\": {\"fifth\", \"5th\"},"` | — |
| [SRC-1AE03B9EC3-L000133](../../agents/web_agent.py#L133) | 133 | `"    \"شقة\": {\"apartment\", \"flat\"}, \"شقق\": {\"apartments\", \"flats\"},"` | — |
| [SRC-1AE03B9EC3-L000134](../../agents/web_agent.py#L134) | 134 | `"    \"عميل\": {\"customer\", \"buyer\"}, \"عملاء\": {\"customers\", \"buyers\"},"` | — |
| [SRC-1AE03B9EC3-L000135](../../agents/web_agent.py#L135) | 135 | `"    \"شراء\": {\"buy\", \"purchase\"}, \"مشتري\": {\"buyer\"},"` | — |
| [SRC-1AE03B9EC3-L000136](../../agents/web_agent.py#L136) | 136 | `"    # Small, explicit Arabic-English topic vocabulary; this helps Arabic prompts"` | — |
| [SRC-1AE03B9EC3-L000137](../../agents/web_agent.py#L137) | 137 | `"    # match English-indexed results without relaxing URL or destination safety."` | — |
| [SRC-1AE03B9EC3-L000138](../../agents/web_agent.py#L138) | 138 | `"    \"سيارة\": {\"car\", \"vehicle\"}, \"السيارة\": {\"car\", \"vehicle\"},"` | — |
| [SRC-1AE03B9EC3-L000139](../../agents/web_agent.py#L139) | 139 | `"    \"سيارات\": {\"cars\", \"vehicles\"}, \"السيارات\": {\"cars\", \"vehicles\"},"` | — |
| [SRC-1AE03B9EC3-L000140](../../agents/web_agent.py#L140) | 140 | `"    \"كهربائي\": {\"electric\"}, \"كهربائية\": {\"electric\"},"` | — |
| [SRC-1AE03B9EC3-L000141](../../agents/web_agent.py#L141) | 141 | `"    \"الكهربائي\": {\"electric\"}, \"الكهربائية\": {\"electric\"},"` | — |
| [SRC-1AE03B9EC3-L000142](../../agents/web_agent.py#L142) | 142 | `"    \"شحن\": {\"charging\", \"charge\"}, \"الشحن\": {\"charging\", \"charge\"},"` | — |
| [SRC-1AE03B9EC3-L000143](../../agents/web_agent.py#L143) | 143 | `"    \"شاحن\": {\"charger\"}, \"بطارية\": {\"battery\"}, \"بطاريات\": {\"batteries\"},"` | — |
| [SRC-1AE03B9EC3-L000144](../../agents/web_agent.py#L144) | 144 | `"    \"تكلفة\": {\"cost\", \"costs\"}, \"التكلفة\": {\"cost\", \"costs\"},"` | — |
| [SRC-1AE03B9EC3-L000145](../../agents/web_agent.py#L145) | 145 | `"    \"البنية\": {\"infrastructure\"}, \"التحتية\": {\"infrastructure\"},"` | — |
| [SRC-1AE03B9EC3-L000146](../../agents/web_agent.py#L146) | 146 | `"    \"تحدي\": {\"challenge\"}, \"تحديات\": {\"challenges\"}, \"التحديات\": {\"challenges\"},"` | — |
| [SRC-1AE03B9EC3-L000147](../../agents/web_agent.py#L147) | 147 | `"    \"وكيل\": {\"agent\"}, \"الوكيل\": {\"agent\"},"` | — |
| [SRC-1AE03B9EC3-L000148](../../agents/web_agent.py#L148) | 148 | `"    \"وكلاء\": {\"agents\"}, \"الوكلاء\": {\"agents\"},"` | — |
| [SRC-1AE03B9EC3-L000149](../../agents/web_agent.py#L149) | 149 | `"    # Bilingual vocabulary for AI use-case searches. Keep the relevance floor"` | — |
| [SRC-1AE03B9EC3-L000150](../../agents/web_agent.py#L150) | 150 | `"    # unchanged; expand only concepts that commonly appear in Arabic news titles."` | — |
| [SRC-1AE03B9EC3-L000151](../../agents/web_agent.py#L151) | 151 | `"    \"استخدام\": {\"use\", \"usage\", \"application\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000152](../../agents/web_agent.py#L152) | 152 | `"    \"استخدامات\": {\"use\", \"usage\", \"application\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000153](../../agents/web_agent.py#L153) | 153 | `"    \"استعمال\": {\"use\", \"usage\", \"application\"},"` | — |
| [SRC-1AE03B9EC3-L000154](../../agents/web_agent.py#L154) | 154 | `"    \"استعمالات\": {\"use\", \"usage\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000155](../../agents/web_agent.py#L155) | 155 | `"    \"حالة\": {\"case\"}, \"حالات\": {\"cases\", \"case\"},"` | — |
| [SRC-1AE03B9EC3-L000156](../../agents/web_agent.py#L156) | 156 | `"    \"اعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000157](../../agents/web_agent.py#L157) | 157 | `"    \"الاعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000158](../../agents/web_agent.py#L158) | 158 | `"    \"للاعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000159](../../agents/web_agent.py#L159) | 159 | `"    \"شركات\": {\"company\", \"companies\", \"business\", \"businesses\"},"` | — |
| [SRC-1AE03B9EC3-L000160](../../agents/web_agent.py#L160) | 160 | `"    \"الشركات\": {\"company\", \"companies\", \"business\", \"businesses\"},"` | — |
| [SRC-1AE03B9EC3-L000161](../../agents/web_agent.py#L161) | 161 | `"    \"صغير\": {\"small\"}, \"صغيرة\": {\"small\"}, \"الصغير\": {\"small\"}, \"الصغيرة\": {\"small\"},"` | — |
| [SRC-1AE03B9EC3-L000162](../../agents/web_agent.py#L162) | 162 | `"    \"ذكاء\": {\"intelligence\", \"ai\"}, \"الذكاء\": {\"intelligence\", \"ai\"},"` | — |
| [SRC-1AE03B9EC3-L000163](../../agents/web_agent.py#L163) | 163 | `"    \"اصطناعي\": {\"artificial\", \"ai\"}, \"الاصطناعي\": {\"artificial\", \"ai\"},"` | — |
| [SRC-1AE03B9EC3-L000164](../../agents/web_agent.py#L164) | 164 | `"    \"تطور\": {\"development\", \"advance\"}, \"تطورات\": {\"developments\", \"advances\", \"updates\", \"latest\"},"` | — |
| [SRC-1AE03B9EC3-L000165](../../agents/web_agent.py#L165) | 165 | `"    \"التطورات\": {\"developments\", \"advances\", \"updates\", \"latest\"},"` | — |
| [SRC-1AE03B9EC3-L000166](../../agents/web_agent.py#L166) | 166 | `"    \"اراء\": {\"opinions\", \"views\"}, \"تجربة\": {\"experience\"}, \"تجارب\": {\"experiences\", \"reviews\"},"` | — |
| [SRC-1AE03B9EC3-L000167](../../agents/web_agent.py#L167) | 167 | `"    \"مستخدم\": {\"user\"}, \"المستخدم\": {\"user\"}, \"مستخدمين\": {\"users\"},"` | — |
| [SRC-1AE03B9EC3-L000168](../../agents/web_agent.py#L168) | 168 | `"    \"المستخدمين\": {\"users\"}, \"مالكون\": {\"owners\"}, \"المالكون\": {\"owners\"},"` | — |
| [SRC-1AE03B9EC3-L000169](../../agents/web_agent.py#L169) | 169 | `"}"` | — |
| [SRC-1AE03B9EC3-L000170](../../agents/web_agent.py#L170) | 170 | `"_CALENDAR_MONTHS = ("` | — |
| [SRC-1AE03B9EC3-L000171](../../agents/web_agent.py#L171) | 171 | `"    \"يناير\", \"فبراير\", \"مارس\", \"ابريل\", \"أبريل\", \"مايو\", \"يونيو\","` | — |
| [SRC-1AE03B9EC3-L000172](../../agents/web_agent.py#L172) | 172 | `"    \"يوليو\", \"اغسطس\", \"أغسطس\", \"سبتمبر\", \"اكتوبر\", \"أكتوبر\","` | — |
| [SRC-1AE03B9EC3-L000173](../../agents/web_agent.py#L173) | 173 | `"    \"نوفمبر\", \"ديسمبر\", \"january\", \"february\", \"march\", \"april\","` | — |
| [SRC-1AE03B9EC3-L000174](../../agents/web_agent.py#L174) | 174 | `"    \"may\", \"june\", \"july\", \"august\", \"september\", \"october\","` | — |
| [SRC-1AE03B9EC3-L000175](../../agents/web_agent.py#L175) | 175 | `"    \"november\", \"december\","` | — |
| [SRC-1AE03B9EC3-L000176](../../agents/web_agent.py#L176) | 176 | `")"` | — |
| [SRC-1AE03B9EC3-L000177](../../agents/web_agent.py#L177) | 177 | `"_BLOCKED_SOURCE_DOMAINS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000178](../../agents/web_agent.py#L178) | 178 | `"    \"translate.google.com\", \"translate.googleusercontent.com\","` | — |
| [SRC-1AE03B9EC3-L000179](../../agents/web_agent.py#L179) | 179 | `"})"` | — |
| [SRC-1AE03B9EC3-L000180](../../agents/web_agent.py#L180) | 180 | `""` | — |
| [SRC-1AE03B9EC3-L000181](../../agents/web_agent.py#L181) | 181 | `""` | — |
| [SRC-1AE03B9EC3-L000182](../../agents/web_agent.py#L182) | 182 | `"def _normalize_search_query(value: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000183](../../agents/web_agent.py#L183) | 183 | `"    \"\"\"Normalize Arabic letters/diacritics while preserving search operators and dates.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000184](../../agents/web_agent.py#L184) | 184 | `"    value = unicodedata.normalize(\"NFKC\", value or \"\")"` | — |
| [SRC-1AE03B9EC3-L000185](../../agents/web_agent.py#L185) | 185 | `"    value = _ARABIC_DIACRITICS_RE.sub(\"\", value).translate(_ARABIC_SEARCH_TRANSLATION)"` | — |
| [SRC-1AE03B9EC3-L000186](../../agents/web_agent.py#L186) | 186 | `"    return re.sub(r\"\\s+\", \" \", value).strip()"` | — |
| [SRC-1AE03B9EC3-L000187](../../agents/web_agent.py#L187) | 187 | `""` | — |
| [SRC-1AE03B9EC3-L000188](../../agents/web_agent.py#L188) | 188 | `""` | — |
| [SRC-1AE03B9EC3-L000189](../../agents/web_agent.py#L189) | 189 | `"# Normalize stop words too: otherwise Arabic letter normalization (e.g. ة→ه, أ→ا)"` | — |
| [SRC-1AE03B9EC3-L000190](../../agents/web_agent.py#L190) | 190 | `"# can leave request-format wording in the token set and distort relevance scores."` | — |
| [SRC-1AE03B9EC3-L000191](../../agents/web_agent.py#L191) | 191 | `"_NORMALIZED_SEARCH_STOPWORDS = frozenset("` | — |
| [SRC-1AE03B9EC3-L000192](../../agents/web_agent.py#L192) | 192 | `"    _normalize_search_query(word).casefold() for word in _SEARCH_STOPWORDS"` | — |
| [SRC-1AE03B9EC3-L000193](../../agents/web_agent.py#L193) | 193 | `")"` | — |
| [SRC-1AE03B9EC3-L000194](../../agents/web_agent.py#L194) | 194 | `""` | — |
| [SRC-1AE03B9EC3-L000195](../../agents/web_agent.py#L195) | 195 | `""` | — |
| [SRC-1AE03B9EC3-L000196](../../agents/web_agent.py#L196) | 196 | `"# Normalize synonym keys and values by the same rules as search text. This avoids"` | — |
| [SRC-1AE03B9EC3-L000197](../../agents/web_agent.py#L197) | 197 | `"# Arabic ta-marbuta/alif variants silently disabling Arabic-to-English matching."` | — |
| [SRC-1AE03B9EC3-L000198](../../agents/web_agent.py#L198) | 198 | `"_NORMALIZED_SEARCH_SYNONYMS: dict[str, set[str]] = {}"` | — |
| [SRC-1AE03B9EC3-L000199](../../agents/web_agent.py#L199) | 199 | `"for _synonym_key, _synonym_values in _SEARCH_SYNONYMS.items():"` | — |
| [SRC-1AE03B9EC3-L000200](../../agents/web_agent.py#L200) | 200 | `"    _normalized_key = _normalize_search_query(_synonym_key).casefold()"` | — |
| [SRC-1AE03B9EC3-L000201](../../agents/web_agent.py#L201) | 201 | `"    _NORMALIZED_SEARCH_SYNONYMS.setdefault(_normalized_key, set()).update("` | — |
| [SRC-1AE03B9EC3-L000202](../../agents/web_agent.py#L202) | 202 | `"        _normalize_search_query(value).casefold() for value in _synonym_values"` | — |
| [SRC-1AE03B9EC3-L000203](../../agents/web_agent.py#L203) | 203 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000204](../../agents/web_agent.py#L204) | 204 | `""` | — |
| [SRC-1AE03B9EC3-L000205](../../agents/web_agent.py#L205) | 205 | `""` | — |
| [SRC-1AE03B9EC3-L000206](../../agents/web_agent.py#L206) | 206 | `"def _search_tokens(value: str) -> set[str]:"` | — |
| [SRC-1AE03B9EC3-L000207](../../agents/web_agent.py#L207) | 207 | `"    \"\"\"Tokenize Arabic/English text and expand a small bilingual vocabulary.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000208](../../agents/web_agent.py#L208) | 208 | `"    value = _normalize_search_query(value).casefold()"` | — |
| [SRC-1AE03B9EC3-L000209](../../agents/web_agent.py#L209) | 209 | `"    value = re.sub(r\"(?i)\\bsite\\s*:\\s*\\S+\", \" \", value)"` | — |
| [SRC-1AE03B9EC3-L000210](../../agents/web_agent.py#L210) | 210 | `"    tokens = re.findall(r\"[a-z0-9]+\|[\\u0620-\\u064A\\u066E-\\u06D3]+\", value)"` | — |
| [SRC-1AE03B9EC3-L000211](../../agents/web_agent.py#L211) | 211 | `"    result: set[str] = set()"` | — |
| [SRC-1AE03B9EC3-L000212](../../agents/web_agent.py#L212) | 212 | `"    for token in tokens:"` | — |
| [SRC-1AE03B9EC3-L000213](../../agents/web_agent.py#L213) | 213 | `"        if token in _NORMALIZED_SEARCH_STOPWORDS or len(token) < 2:"` | — |
| [SRC-1AE03B9EC3-L000214](../../agents/web_agent.py#L214) | 214 | `"            continue"` | — |
| [SRC-1AE03B9EC3-L000215](../../agents/web_agent.py#L215) | 215 | `"        forms = {token}"` | — |
| [SRC-1AE03B9EC3-L000216](../../agents/web_agent.py#L216) | 216 | `"        if token.startswith(\"ال\") and len(token) > 4:"` | — |
| [SRC-1AE03B9EC3-L000217](../../agents/web_agent.py#L217) | 217 | `"            forms.add(token[2:])"` | — |
| [SRC-1AE03B9EC3-L000218](../../agents/web_agent.py#L218) | 218 | `"        forms.update(_NORMALIZED_SEARCH_SYNONYMS.get(token, set()))"` | — |
| [SRC-1AE03B9EC3-L000219](../../agents/web_agent.py#L219) | 219 | `"        # Reverse-map common English equivalents so Arabic and English results can match."` | — |
| [SRC-1AE03B9EC3-L000220](../../agents/web_agent.py#L220) | 220 | `"        for arabic, english in _NORMALIZED_SEARCH_SYNONYMS.items():"` | — |
| [SRC-1AE03B9EC3-L000221](../../agents/web_agent.py#L221) | 221 | `"            if token in english:"` | — |
| [SRC-1AE03B9EC3-L000222](../../agents/web_agent.py#L222) | 222 | `"                forms.add(arabic)"` | — |
| [SRC-1AE03B9EC3-L000223](../../agents/web_agent.py#L223) | 223 | `"                if arabic.startswith(\"ال\") and len(arabic) > 4:"` | — |
| [SRC-1AE03B9EC3-L000224](../../agents/web_agent.py#L224) | 224 | `"                    forms.add(arabic[2:])"` | — |
| [SRC-1AE03B9EC3-L000225](../../agents/web_agent.py#L225) | 225 | `"        result.update(forms)"` | — |
| [SRC-1AE03B9EC3-L000226](../../agents/web_agent.py#L226) | 226 | `"    return result"` | — |
| [SRC-1AE03B9EC3-L000227](../../agents/web_agent.py#L227) | 227 | `""` | — |
| [SRC-1AE03B9EC3-L000228](../../agents/web_agent.py#L228) | 228 | `""` | — |
| [SRC-1AE03B9EC3-L000229](../../agents/web_agent.py#L229) | 229 | `"def _relevance_query_tokens(query: str) -> set[str]:"` | — |
| [SRC-1AE03B9EC3-L000230](../../agents/web_agent.py#L230) | 230 | `"    \"\"\"Return topic concepts after removing answer-format and query-expansion wording.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000231](../../agents/web_agent.py#L231) | 231 | `"    query = compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L000232](../../agents/web_agent.py#L232) | 232 | `"    if not query:"` | — |
| [SRC-1AE03B9EC3-L000233](../../agents/web_agent.py#L233) | 233 | `"        return set()"` | — |
| [SRC-1AE03B9EC3-L000234](../../agents/web_agent.py#L234) | 234 | `"    query_text = _normalize_search_query(query).casefold()"` | — |
| [SRC-1AE03B9EC3-L000235](../../agents/web_agent.py#L235) | 235 | `"    query_text = re.sub(r\"(?i)\\bsite\\s*:\\s*\\S+\", \" \", query_text)"` | — |
| [SRC-1AE03B9EC3-L000236](../../agents/web_agent.py#L236) | 236 | `"    return {"` | — |
| [SRC-1AE03B9EC3-L000237](../../agents/web_agent.py#L237) | 237 | `"        token for token in re.findall(r\"[a-z0-9]+\|[\\u0620-\\u064A\\u066E-\\u06D3]+\", query_text)"` | — |
| [SRC-1AE03B9EC3-L000238](../../agents/web_agent.py#L238) | 238 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L000239](../../agents/web_agent.py#L239) | 239 | `"            token not in _NORMALIZED_SEARCH_STOPWORDS"` | — |
| [SRC-1AE03B9EC3-L000240](../../agents/web_agent.py#L240) | 240 | `"            and token not in _GENERIC_QUERY_MODIFIER_TOKENS"` | — |
| [SRC-1AE03B9EC3-L000241](../../agents/web_agent.py#L241) | 241 | `"            and len(token) >= 2"` | — |
| [SRC-1AE03B9EC3-L000242](../../agents/web_agent.py#L242) | 242 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000243](../../agents/web_agent.py#L243) | 243 | `"    }"` | — |
| [SRC-1AE03B9EC3-L000244](../../agents/web_agent.py#L244) | 244 | `""` | — |
| [SRC-1AE03B9EC3-L000245](../../agents/web_agent.py#L245) | 245 | `""` | — |
| [SRC-1AE03B9EC3-L000246](../../agents/web_agent.py#L246) | 246 | `"def _minimum_relevance_ratio(_query: str) -> float:"` | — |
| [SRC-1AE03B9EC3-L000247](../../agents/web_agent.py#L247) | 247 | `"    \"\"\"Keep the established 20% relevance floor after query normalization and token cleanup.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000248](../../agents/web_agent.py#L248) | 248 | `"    return 0.20"` | — |
| [SRC-1AE03B9EC3-L000249](../../agents/web_agent.py#L249) | 249 | `""` | — |
| [SRC-1AE03B9EC3-L000250](../../agents/web_agent.py#L250) | 250 | `""` | — |
| [SRC-1AE03B9EC3-L000251](../../agents/web_agent.py#L251) | 251 | `"def _relevance_ratio(query: str, evidence: str) -> float:"` | — |
| [SRC-1AE03B9EC3-L000252](../../agents/web_agent.py#L252) | 252 | `"    \"\"\"Fraction of meaningful query concepts present in a candidate's title/snippet.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000253](../../agents/web_agent.py#L253) | 253 | `"    query_tokens = _relevance_query_tokens(query)"` | — |
| [SRC-1AE03B9EC3-L000254](../../agents/web_agent.py#L254) | 254 | `"    if not query_tokens:"` | — |
| [SRC-1AE03B9EC3-L000255](../../agents/web_agent.py#L255) | 255 | `"        # Relevance cannot be established from an instruction-only query."` | — |
| [SRC-1AE03B9EC3-L000256](../../agents/web_agent.py#L256) | 256 | `"        return 0.0"` | — |
| [SRC-1AE03B9EC3-L000257](../../agents/web_agent.py#L257) | 257 | `"    expanded_evidence = _search_tokens(evidence)"` | — |
| [SRC-1AE03B9EC3-L000258](../../agents/web_agent.py#L258) | 258 | `"    matched = sum("` | — |
| [SRC-1AE03B9EC3-L000259](../../agents/web_agent.py#L259) | 259 | `"        1 for token in query_tokens"` | — |
| [SRC-1AE03B9EC3-L000260](../../agents/web_agent.py#L260) | 260 | `"        if token in expanded_evidence"` | — |
| [SRC-1AE03B9EC3-L000261](../../agents/web_agent.py#L261) | 261 | `"        or (token.startswith(\"ال\") and token[2:] in expanded_evidence)"` | — |
| [SRC-1AE03B9EC3-L000262](../../agents/web_agent.py#L262) | 262 | `"        or bool(_NORMALIZED_SEARCH_SYNONYMS.get(token, set()) & expanded_evidence)"` | — |
| [SRC-1AE03B9EC3-L000263](../../agents/web_agent.py#L263) | 263 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000264](../../agents/web_agent.py#L264) | 264 | `"    ratio = matched / len(query_tokens)"` | — |
| [SRC-1AE03B9EC3-L000265](../../agents/web_agent.py#L265) | 265 | `"    # On longer questions, two matching topic concepts are required; request wording"` | — |
| [SRC-1AE03B9EC3-L000266](../../agents/web_agent.py#L266) | 266 | `"    # should not silently raise that floor to three or four concepts."` | — |
| [SRC-1AE03B9EC3-L000267](../../agents/web_agent.py#L267) | 267 | `"    if len(query_tokens) >= 4 and matched < 2:"` | — |
| [SRC-1AE03B9EC3-L000268](../../agents/web_agent.py#L268) | 268 | `"        return 0.0"` | — |
| [SRC-1AE03B9EC3-L000269](../../agents/web_agent.py#L269) | 269 | `"    return ratio"` | — |
| [SRC-1AE03B9EC3-L000270](../../agents/web_agent.py#L270) | 270 | `""` | — |
| [SRC-1AE03B9EC3-L000271](../../agents/web_agent.py#L271) | 271 | `"def _blocked_source_url(url: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000272](../../agents/web_agent.py#L272) | 272 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000273](../../agents/web_agent.py#L273) | 273 | `"        host = (urllib.parse.urlparse(url).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L000274](../../agents/web_agent.py#L274) | 274 | `"        return any(host == domain or host.endswith(\".\" + domain) for domain in _BLOCKED_SOURCE_DOMAINS)"` | — |
| [SRC-1AE03B9EC3-L000275](../../agents/web_agent.py#L275) | 275 | `"    except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L000276](../../agents/web_agent.py#L276) | 276 | `"        return True"` | — |
| [SRC-1AE03B9EC3-L000277](../../agents/web_agent.py#L277) | 277 | `""` | — |
| [SRC-1AE03B9EC3-L000278](../../agents/web_agent.py#L278) | 278 | `""` | — |
| [SRC-1AE03B9EC3-L000279](../../agents/web_agent.py#L279) | 279 | `"class AgentDependencyError(RuntimeError):"` | — |
| [SRC-1AE03B9EC3-L000280](../../agents/web_agent.py#L280) | 280 | `"    \"\"\"A required optional runtime dependency is unavailable.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000281](../../agents/web_agent.py#L281) | 281 | `""` | — |
| [SRC-1AE03B9EC3-L000282](../../agents/web_agent.py#L282) | 282 | `""` | — |
| [SRC-1AE03B9EC3-L000283](../../agents/web_agent.py#L283) | 283 | `"def _clean_text(value: Any, limit: int) -> str:"` | — |
| [SRC-1AE03B9EC3-L000284](../../agents/web_agent.py#L284) | 284 | `"    if not isinstance(value, str):"` | — |
| [SRC-1AE03B9EC3-L000285](../../agents/web_agent.py#L285) | 285 | `"        return \"\""` | — |
| [SRC-1AE03B9EC3-L000286](../../agents/web_agent.py#L286) | 286 | `"    return \" \".join(value.replace(\"\\x00\", \" \").split())[:limit]"` | — |
| [SRC-1AE03B9EC3-L000287](../../agents/web_agent.py#L287) | 287 | `""` | — |
| [SRC-1AE03B9EC3-L000288](../../agents/web_agent.py#L288) | 288 | `""` | — |
| [SRC-1AE03B9EC3-L000289](../../agents/web_agent.py#L289) | 289 | `"def _public_http_url(value: Any) -> str \| None:"` | — |
| [SRC-1AE03B9EC3-L000290](../../agents/web_agent.py#L290) | 290 | `"    \"\"\"Lexically validate an HTTP URL before using it as a search source.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000291](../../agents/web_agent.py#L291) | 291 | `"    if not isinstance(value, str) or len(value) > 2048:"` | — |
| [SRC-1AE03B9EC3-L000292](../../agents/web_agent.py#L292) | 292 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000293](../../agents/web_agent.py#L293) | 293 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000294](../../agents/web_agent.py#L294) | 294 | `"        parsed = urllib.parse.urlparse(value.strip())"` | — |
| [SRC-1AE03B9EC3-L000295](../../agents/web_agent.py#L295) | 295 | `"        if parsed.scheme not in {\"http\", \"https\"}:"` | — |
| [SRC-1AE03B9EC3-L000296](../../agents/web_agent.py#L296) | 296 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000297](../../agents/web_agent.py#L297) | 297 | `"        if not parsed.hostname or parsed.username is not None or parsed.password is not None:"` | — |
| [SRC-1AE03B9EC3-L000298](../../agents/web_agent.py#L298) | 298 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000299](../../agents/web_agent.py#L299) | 299 | `"        if parsed.port not in (None, 80, 443):"` | — |
| [SRC-1AE03B9EC3-L000300](../../agents/web_agent.py#L300) | 300 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000301](../../agents/web_agent.py#L301) | 301 | `"        host = parsed.hostname.rstrip(\".\").lower()"` | — |
| [SRC-1AE03B9EC3-L000302](../../agents/web_agent.py#L302) | 302 | `"        if not host or host in {\"localhost\"} or host.endswith((\".local\", \".internal\", \".localhost\")):"` | — |
| [SRC-1AE03B9EC3-L000303](../../agents/web_agent.py#L303) | 303 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000304](../../agents/web_agent.py#L304) | 304 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000305](../../agents/web_agent.py#L305) | 305 | `"            ip = ipaddress.ip_address(host)"` | — |
| [SRC-1AE03B9EC3-L000306](../../agents/web_agent.py#L306) | 306 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L000307](../../agents/web_agent.py#L307) | 307 | `"            pass"` | — |
| [SRC-1AE03B9EC3-L000308](../../agents/web_agent.py#L308) | 308 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L000309](../../agents/web_agent.py#L309) | 309 | `"            if not ip.is_global:"` | — |
| [SRC-1AE03B9EC3-L000310](../../agents/web_agent.py#L310) | 310 | `"                return None"` | — |
| [SRC-1AE03B9EC3-L000311](../../agents/web_agent.py#L311) | 311 | `"        return urllib.parse.urlunparse(parsed._replace(fragment=\"\"))"` | — |
| [SRC-1AE03B9EC3-L000312](../../agents/web_agent.py#L312) | 312 | `"    except (ValueError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L000313](../../agents/web_agent.py#L313) | 313 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000314](../../agents/web_agent.py#L314) | 314 | `""` | — |
| [SRC-1AE03B9EC3-L000315](../../agents/web_agent.py#L315) | 315 | `""` | — |
| [SRC-1AE03B9EC3-L000316](../../agents/web_agent.py#L316) | 316 | `"def _public_ip_literals(host: str) -> list[str] \| None:"` | — |
| [SRC-1AE03B9EC3-L000317](../../agents/web_agent.py#L317) | 317 | `"    \"\"\"Resolve host and return its public addresses."` | — |
| [SRC-1AE03B9EC3-L000318](../../agents/web_agent.py#L318) | 318 | `""` | — |
| [SRC-1AE03B9EC3-L000319](../../agents/web_agent.py#L319) | 319 | `"    Returns None when resolution fails or any answer is not a global address."` | — |
| [SRC-1AE03B9EC3-L000320](../../agents/web_agent.py#L320) | 320 | `"    Callers must open the TCP connection to one of these literals. A second DNS"` | — |
| [SRC-1AE03B9EC3-L000321](../../agents/web_agent.py#L321) | 321 | `"    lookup is not equivalent: the name can be rebound to a private address"` | — |
| [SRC-1AE03B9EC3-L000322](../../agents/web_agent.py#L322) | 322 | `"    between the check and the connection (DNS rebinding / TOCTOU)."` | — |
| [SRC-1AE03B9EC3-L000323](../../agents/web_agent.py#L323) | 323 | `"    \"\"\""` | — |
| [SRC-1AE03B9EC3-L000324](../../agents/web_agent.py#L324) | 324 | `"    if not host:"` | — |
| [SRC-1AE03B9EC3-L000325](../../agents/web_agent.py#L325) | 325 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000326](../../agents/web_agent.py#L326) | 326 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000327](../../agents/web_agent.py#L327) | 327 | `"        answers = socket.getaddrinfo(host, None, type=socket.SOCK_STREAM)"` | — |
| [SRC-1AE03B9EC3-L000328](../../agents/web_agent.py#L328) | 328 | `"    except (OSError, socket.gaierror):"` | — |
| [SRC-1AE03B9EC3-L000329](../../agents/web_agent.py#L329) | 329 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000330](../../agents/web_agent.py#L330) | 330 | `"    if not answers:"` | — |
| [SRC-1AE03B9EC3-L000331](../../agents/web_agent.py#L331) | 331 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000332](../../agents/web_agent.py#L332) | 332 | `"    literals: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L000333](../../agents/web_agent.py#L333) | 333 | `"    for answer in answers:"` | — |
| [SRC-1AE03B9EC3-L000334](../../agents/web_agent.py#L334) | 334 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000335](../../agents/web_agent.py#L335) | 335 | `"            address = ipaddress.ip_address(answer[4][0])"` | — |
| [SRC-1AE03B9EC3-L000336](../../agents/web_agent.py#L336) | 336 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L000337](../../agents/web_agent.py#L337) | 337 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000338](../../agents/web_agent.py#L338) | 338 | `"        if not address.is_global:"` | — |
| [SRC-1AE03B9EC3-L000339](../../agents/web_agent.py#L339) | 339 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000340](../../agents/web_agent.py#L340) | 340 | `"        literal = str(address)"` | — |
| [SRC-1AE03B9EC3-L000341](../../agents/web_agent.py#L341) | 341 | `"        if literal not in literals:"` | — |
| [SRC-1AE03B9EC3-L000342](../../agents/web_agent.py#L342) | 342 | `"            literals.append(literal)"` | — |
| [SRC-1AE03B9EC3-L000343](../../agents/web_agent.py#L343) | 343 | `"    return literals or None"` | — |
| [SRC-1AE03B9EC3-L000344](../../agents/web_agent.py#L344) | 344 | `""` | — |
| [SRC-1AE03B9EC3-L000345](../../agents/web_agent.py#L345) | 345 | `""` | — |
| [SRC-1AE03B9EC3-L000346](../../agents/web_agent.py#L346) | 346 | `"def _host_resolves_publicly(host: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000347](../../agents/web_agent.py#L347) | 347 | `"    \"\"\"Reject local/private destinations before fetching a third-party page.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000348](../../agents/web_agent.py#L348) | 348 | `"    return _public_ip_literals(host) is not None"` | — |
| [SRC-1AE03B9EC3-L000349](../../agents/web_agent.py#L349) | 349 | `""` | — |
| [SRC-1AE03B9EC3-L000350](../../agents/web_agent.py#L350) | 350 | `""` | — |
| [SRC-1AE03B9EC3-L000351](../../agents/web_agent.py#L351) | 351 | `"def _pinned_connect_url(logical_url: str, ip: str) -> str \| None:"` | — |
| [SRC-1AE03B9EC3-L000352](../../agents/web_agent.py#L352) | 352 | `"    \"\"\"Rewrite a validated public URL so the connection target is a checked IP.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000353](../../agents/web_agent.py#L353) | 353 | `"    parsed = urllib.parse.urlparse(logical_url)"` | — |
| [SRC-1AE03B9EC3-L000354](../../agents/web_agent.py#L354) | 354 | `"    if parsed.port not in (None, 80, 443):"` | — |
| [SRC-1AE03B9EC3-L000355](../../agents/web_agent.py#L355) | 355 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000356](../../agents/web_agent.py#L356) | 356 | `"    literal = f\"[{ip}]\" if \":\" in ip else ip"` | — |
| [SRC-1AE03B9EC3-L000357](../../agents/web_agent.py#L357) | 357 | `"    netloc = literal if parsed.port is None else f\"{literal}:{parsed.port}\""` | — |
| [SRC-1AE03B9EC3-L000358](../../agents/web_agent.py#L358) | 358 | `"    return urllib.parse.urlunparse(parsed._replace(netloc=netloc))"` | — |
| [SRC-1AE03B9EC3-L000359](../../agents/web_agent.py#L359) | 359 | `""` | — |
| [SRC-1AE03B9EC3-L000360](../../agents/web_agent.py#L360) | 360 | `""` | — |
| [SRC-1AE03B9EC3-L000361](../../agents/web_agent.py#L361) | 361 | `"def _fallback_answer(sources: list[dict[str, Any]], reason: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000362](../../agents/web_agent.py#L362) | 362 | `"    lines = [reason]"` | — |
| [SRC-1AE03B9EC3-L000363](../../agents/web_agent.py#L363) | 363 | `"    usable = [source for source in sources if source.get(\"snippet\")]"` | — |
| [SRC-1AE03B9EC3-L000364](../../agents/web_agent.py#L364) | 364 | `"    for index, source in enumerate(usable[:5], 1):"` | — |
| [SRC-1AE03B9EC3-L000365](../../agents/web_agent.py#L365) | 365 | `"        lines.append("` | — |
| [SRC-1AE03B9EC3-L000366](../../agents/web_agent.py#L366) | 366 | `"            f\"{index}. {source.get('title', 'نتيجة ويب')}: \""` | — |
| [SRC-1AE03B9EC3-L000367](../../agents/web_agent.py#L367) | 367 | `"            f\"{source['snippet']} (المصدر: {source['url']})\""` | — |
| [SRC-1AE03B9EC3-L000368](../../agents/web_agent.py#L368) | 368 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000369](../../agents/web_agent.py#L369) | 369 | `"    if not usable:"` | — |
| [SRC-1AE03B9EC3-L000370](../../agents/web_agent.py#L370) | 370 | `"        lines.append(\"لم أتمكن من استخراج مقتطفات كافية من نتائج الويب.\")"` | — |
| [SRC-1AE03B9EC3-L000371](../../agents/web_agent.py#L371) | 371 | `"    return \"\\n\\n\".join(lines)"` | — |
| [SRC-1AE03B9EC3-L000372](../../agents/web_agent.py#L372) | 372 | `""` | — |
| [SRC-1AE03B9EC3-L000373](../../agents/web_agent.py#L373) | 373 | `""` | — |
| [SRC-1AE03B9EC3-L000374](../../agents/web_agent.py#L374) | 374 | `"class PageFetchResult(tuple):"` | — |
| [SRC-1AE03B9EC3-L000375](../../agents/web_agent.py#L375) | 375 | `"    \"\"\"Two-item tuple compatible with legacy callers, with structured extraction status.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000376](../../agents/web_agent.py#L376) | 376 | `""` | — |
| [SRC-1AE03B9EC3-L000377](../../agents/web_agent.py#L377) | 377 | `"    def __new__("` | — |
| [SRC-1AE03B9EC3-L000378](../../agents/web_agent.py#L378) | 378 | `"        cls,"` | — |
| [SRC-1AE03B9EC3-L000379](../../agents/web_agent.py#L379) | 379 | `"        title: str = \"\","` | — |
| [SRC-1AE03B9EC3-L000380](../../agents/web_agent.py#L380) | 380 | `"        page_text: str = \"\","` | — |
| [SRC-1AE03B9EC3-L000381](../../agents/web_agent.py#L381) | 381 | `"        status: str = \"unknown\","` | — |
| [SRC-1AE03B9EC3-L000382](../../agents/web_agent.py#L382) | 382 | `"        error_class: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L000383](../../agents/web_agent.py#L383) | 383 | `"    ):"` | — |
| [SRC-1AE03B9EC3-L000384](../../agents/web_agent.py#L384) | 384 | `"        value = super().__new__(cls, (title, page_text))"` | — |
| [SRC-1AE03B9EC3-L000385](../../agents/web_agent.py#L385) | 385 | `"        value.status = status"` | — |
| [SRC-1AE03B9EC3-L000386](../../agents/web_agent.py#L386) | 386 | `"        value.error_class = error_class"` | — |
| [SRC-1AE03B9EC3-L000387](../../agents/web_agent.py#L387) | 387 | `"        return value"` | — |
| [SRC-1AE03B9EC3-L000388](../../agents/web_agent.py#L388) | 388 | `""` | — |
| [SRC-1AE03B9EC3-L000389](../../agents/web_agent.py#L389) | 389 | `""` | — |
| [SRC-1AE03B9EC3-L000390](../../agents/web_agent.py#L390) | 390 | `"def enforce_aspect_answer_completeness(result: dict[str, Any]) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L000391](../../agents/web_agent.py#L391) | 391 | `"    \"\"\"Withhold a final answer if any explicit axis lacks a text candidate."` | — |
| [SRC-1AE03B9EC3-L000392](../../agents/web_agent.py#L392) | 392 | `""` | — |
| [SRC-1AE03B9EC3-L000393](../../agents/web_agent.py#L393) | 393 | `"    Lexical coverage is only a conservative evidence-presence check, not semantic"` | — |
| [SRC-1AE03B9EC3-L000394](../../agents/web_agent.py#L394) | 394 | `"    verification. A missing candidate therefore blocks a *complete* answer rather"` | — |
| [SRC-1AE03B9EC3-L000395](../../agents/web_agent.py#L395) | 395 | `"    than asserting the underlying fact is unavailable everywhere."` | — |
| [SRC-1AE03B9EC3-L000396](../../agents/web_agent.py#L396) | 396 | `"    \"\"\""` | — |
| [SRC-1AE03B9EC3-L000397](../../agents/web_agent.py#L397) | 397 | `"    search_report = result.get(\"search_report\")"` | — |
| [SRC-1AE03B9EC3-L000398](../../agents/web_agent.py#L398) | 398 | `"    if not isinstance(search_report, dict):"` | — |
| [SRC-1AE03B9EC3-L000399](../../agents/web_agent.py#L399) | 399 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L000400](../../agents/web_agent.py#L400) | 400 | `"    prior_ledger = search_report.get(\"evidence_ledger\")"` | — |
| [SRC-1AE03B9EC3-L000401](../../agents/web_agent.py#L401) | 401 | `"    if not isinstance(prior_ledger, dict):"` | — |
| [SRC-1AE03B9EC3-L000402](../../agents/web_agent.py#L402) | 402 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L000403](../../agents/web_agent.py#L403) | 403 | `"    aspects = prior_ledger.get(\"aspects\")"` | — |
| [SRC-1AE03B9EC3-L000404](../../agents/web_agent.py#L404) | 404 | `"    if not isinstance(aspects, list) or not aspects:"` | — |
| [SRC-1AE03B9EC3-L000405](../../agents/web_agent.py#L405) | 405 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L000406](../../agents/web_agent.py#L406) | 406 | `"    targets = ["` | — |
| [SRC-1AE03B9EC3-L000407](../../agents/web_agent.py#L407) | 407 | `"        item[:120]"` | — |
| [SRC-1AE03B9EC3-L000408](../../agents/web_agent.py#L408) | 408 | `"        for item in aspects"` | — |
| [SRC-1AE03B9EC3-L000409](../../agents/web_agent.py#L409) | 409 | `"        if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L000410](../../agents/web_agent.py#L410) | 410 | `"    ][:8]"` | — |
| [SRC-1AE03B9EC3-L000411](../../agents/web_agent.py#L411) | 411 | `"    if not targets:"` | — |
| [SRC-1AE03B9EC3-L000412](../../agents/web_agent.py#L412) | 412 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L000413](../../agents/web_agent.py#L413) | 413 | `""` | — |
| [SRC-1AE03B9EC3-L000414](../../agents/web_agent.py#L414) | 414 | `"    raw_sources = result.get(\"sources\")"` | — |
| [SRC-1AE03B9EC3-L000415](../../agents/web_agent.py#L415) | 415 | `"    sources = ("` | — |
| [SRC-1AE03B9EC3-L000416](../../agents/web_agent.py#L416) | 416 | `"        [item for item in raw_sources if isinstance(item, dict)]"` | — |
| [SRC-1AE03B9EC3-L000417](../../agents/web_agent.py#L417) | 417 | `"        if isinstance(raw_sources, list)"` | — |
| [SRC-1AE03B9EC3-L000418](../../agents/web_agent.py#L418) | 418 | `"        else []"` | — |
| [SRC-1AE03B9EC3-L000419](../../agents/web_agent.py#L419) | 419 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000420](../../agents/web_agent.py#L420) | 420 | `"    ledger = build_evidence_ledger(targets, sources)"` | — |
| [SRC-1AE03B9EC3-L000421](../../agents/web_agent.py#L421) | 421 | `"    search_report[\"evidence_ledger\"] = ledger"` | — |
| [SRC-1AE03B9EC3-L000422](../../agents/web_agent.py#L422) | 422 | `"    search_report[\"aspects\"] = targets"` | — |
| [SRC-1AE03B9EC3-L000423](../../agents/web_agent.py#L423) | 423 | `"    search_report[\"aspect_diagnostics_ar\"] = arabic_aspect_diagnostics(ledger)"` | — |
| [SRC-1AE03B9EC3-L000424](../../agents/web_agent.py#L424) | 424 | `"    search_report[\"aspect_evidence_gaps\"] = list(ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L000425](../../agents/web_agent.py#L425) | 425 | `"    search_report[\"aspect_coverage_lexical_ratio\"] = ledger.get(\"coverage_ratio\")"` | — |
| [SRC-1AE03B9EC3-L000426](../../agents/web_agent.py#L426) | 426 | `"    search_report[\"aspect_coverage_is_not_truth_score\"] = True"` | — |
| [SRC-1AE03B9EC3-L000427](../../agents/web_agent.py#L427) | 427 | `""` | — |
| [SRC-1AE03B9EC3-L000428](../../agents/web_agent.py#L428) | 428 | `"    result[\"aspects\"] = targets"` | — |
| [SRC-1AE03B9EC3-L000429](../../agents/web_agent.py#L429) | 429 | `"    result[\"aspect_evidence_gaps\"] = list(ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L000430](../../agents/web_agent.py#L430) | 430 | `"    result[\"aspect_diagnostics_ar\"] = list(search_report[\"aspect_diagnostics_ar\"])"` | — |
| [SRC-1AE03B9EC3-L000431](../../agents/web_agent.py#L431) | 431 | `"    result[\"aspect_coverage_lexical_ratio\"] = ledger.get(\"coverage_ratio\")"` | — |
| [SRC-1AE03B9EC3-L000432](../../agents/web_agent.py#L432) | 432 | `"    result[\"aspect_coverage_is_not_truth_score\"] = True"` | — |
| [SRC-1AE03B9EC3-L000433](../../agents/web_agent.py#L433) | 433 | `""` | — |
| [SRC-1AE03B9EC3-L000434](../../agents/web_agent.py#L434) | 434 | `"    missing = list(ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L000435](../../agents/web_agent.py#L435) | 435 | `"    if missing:"` | — |
| [SRC-1AE03B9EC3-L000436](../../agents/web_agent.py#L436) | 436 | `"        result[\"answer\"] = ("` | — |
| [SRC-1AE03B9EC3-L000437](../../agents/web_agent.py#L437) | 437 | `"            \"لم أقدّم إجابة نهائية؛ لأن نتائج البحث المتاحة لا تتضمن مرشحًا نصيًا كافيًا \""` | — |
| [SRC-1AE03B9EC3-L000438](../../agents/web_agent.py#L438) | 438 | `"            \"لكل المحاور المطلوبة. المحاور التي تحتاج إلى دليل إضافي: \""` | — |
| [SRC-1AE03B9EC3-L000439](../../agents/web_agent.py#L439) | 439 | `"            + \"، \".join(str(item) for item in missing)"` | — |
| [SRC-1AE03B9EC3-L000440](../../agents/web_agent.py#L440) | 440 | `"            + \". لن أعرض مسودة جزئية على أنها إجابة مكتملة. وهذا النقص يصف النتائج التي جُمعت \""` | — |
| [SRC-1AE03B9EC3-L000441](../../agents/web_agent.py#L441) | 441 | `"            \"فقط، ولا يثبت عدم وجود معلومات عنها خارجها.\""` | — |
| [SRC-1AE03B9EC3-L000442](../../agents/web_agent.py#L442) | 442 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000443](../../agents/web_agent.py#L443) | 443 | `"        result[\"answer_was_withheld\"] = True"` | — |
| [SRC-1AE03B9EC3-L000444](../../agents/web_agent.py#L444) | 444 | `"        result[\"answer_completeness_status\"] = \"incomplete_evidence_withheld\""` | — |
| [SRC-1AE03B9EC3-L000445](../../agents/web_agent.py#L445) | 445 | `"        result[\"final_answer_status\"] = \"incomplete_evidence_withheld\""` | — |
| [SRC-1AE03B9EC3-L000446](../../agents/web_agent.py#L446) | 446 | `"        result[\"task_fulfillment_status\"] = \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L000447](../../agents/web_agent.py#L447) | 447 | `"        search_report[\"task_fulfillment_status\"] = \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L000448](../../agents/web_agent.py#L448) | 448 | `"        answer_coverage = result.get(\"answer_coverage\")"` | — |
| [SRC-1AE03B9EC3-L000449](../../agents/web_agent.py#L449) | 449 | `"        if isinstance(answer_coverage, dict):"` | — |
| [SRC-1AE03B9EC3-L000450](../../agents/web_agent.py#L450) | 450 | `"            answer_coverage[\"task_fulfillment_status\"] = \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L000451](../../agents/web_agent.py#L451) | 451 | `"        warning = \"حُجبت الإجابة النهائية لوجود محاور مطلوبة بلا مرشح نصي كافٍ.\""` | — |
| [SRC-1AE03B9EC3-L000452](../../agents/web_agent.py#L452) | 452 | `"        warnings = result.setdefault(\"warnings\", [])"` | — |
| [SRC-1AE03B9EC3-L000453](../../agents/web_agent.py#L453) | 453 | `"        if isinstance(warnings, list) and warning not in warnings:"` | — |
| [SRC-1AE03B9EC3-L000454](../../agents/web_agent.py#L454) | 454 | `"            warnings.append(warning)"` | — |
| [SRC-1AE03B9EC3-L000455](../../agents/web_agent.py#L455) | 455 | `"    else:"` | — |
| [SRC-1AE03B9EC3-L000456](../../agents/web_agent.py#L456) | 456 | `"        result[\"answer_was_withheld\"] = False"` | — |
| [SRC-1AE03B9EC3-L000457](../../agents/web_agent.py#L457) | 457 | `"        result[\"answer_completeness_status\"] = ("` | — |
| [SRC-1AE03B9EC3-L000458](../../agents/web_agent.py#L458) | 458 | `"            \"no_lexical_gaps_detected_semantic_completeness_not_proven\""` | — |
| [SRC-1AE03B9EC3-L000459](../../agents/web_agent.py#L459) | 459 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000460](../../agents/web_agent.py#L460) | 460 | `"    return result"` | — |
| [SRC-1AE03B9EC3-L000461](../../agents/web_agent.py#L461) | 461 | `""` | — |
| [SRC-1AE03B9EC3-L000462](../../agents/web_agent.py#L462) | 462 | `""` | — |
| [SRC-1AE03B9EC3-L000463](../../agents/web_agent.py#L463) | 463 | `"class WebAgent:"` | — |
| [SRC-1AE03B9EC3-L000464](../../agents/web_agent.py#L464) | 464 | `"    \"\"\"Search, inspect, and synthesize web evidence for open-ended questions.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000465](../../agents/web_agent.py#L465) | 465 | `""` | — |
| [SRC-1AE03B9EC3-L000466](../../agents/web_agent.py#L466) | 466 | `"    def __init__(self) -> None:"` | — |
| [SRC-1AE03B9EC3-L000467](../../agents/web_agent.py#L467) | 467 | `"        self.api_key = ("` | — |
| [SRC-1AE03B9EC3-L000468](../../agents/web_agent.py#L468) | 468 | `"            os.getenv(\"OMARAI_LLM_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000469](../../agents/web_agent.py#L469) | 469 | `"            or os.getenv(\"OPENROUTER_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000470](../../agents/web_agent.py#L470) | 470 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000471](../../agents/web_agent.py#L471) | 471 | `"        self.base_url = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000472](../../agents/web_agent.py#L472) | 472 | `"            \"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\""` | — |
| [SRC-1AE03B9EC3-L000473](../../agents/web_agent.py#L473) | 473 | `"        ).strip().rstrip(\"/\")"` | — |
| [SRC-1AE03B9EC3-L000474](../../agents/web_agent.py#L474) | 474 | `"        # Pin explicit role models for more consistent behaviour than a random free router."` | — |
| [SRC-1AE03B9EC3-L000475](../../agents/web_agent.py#L475) | 475 | `"        # OMARAI_LLM_MODEL remains a global override for users who want one model everywhere."` | — |
| [SRC-1AE03B9EC3-L000476](../../agents/web_agent.py#L476) | 476 | `"        global_model = os.getenv(\"OMARAI_LLM_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000477](../../agents/web_agent.py#L477) | 477 | `"        self.answer_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000478](../../agents/web_agent.py#L478) | 478 | `"            \"OMARAI_ANSWER_MODEL\", global_model or \"google/gemma-4-31b-it:free\""` | — |
| [SRC-1AE03B9EC3-L000479](../../agents/web_agent.py#L479) | 479 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000480](../../agents/web_agent.py#L480) | 480 | `"        self.planner_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000481](../../agents/web_agent.py#L481) | 481 | `"            \"OMARAI_PLANNER_MODEL\","` | — |
| [SRC-1AE03B9EC3-L000482](../../agents/web_agent.py#L482) | 482 | `"            global_model or \"nvidia/nemotron-3-ultra-550b-a55b:free\","` | — |
| [SRC-1AE03B9EC3-L000483](../../agents/web_agent.py#L483) | 483 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000484](../../agents/web_agent.py#L484) | 484 | `"        self.review_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000485](../../agents/web_agent.py#L485) | 485 | `"            \"OMARAI_REVIEW_MODEL\", self.answer_model"` | — |
| [SRC-1AE03B9EC3-L000486](../../agents/web_agent.py#L486) | 486 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000487](../../agents/web_agent.py#L487) | 487 | `"        self.fallback_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000488](../../agents/web_agent.py#L488) | 488 | `"            \"OMARAI_LLM_FALLBACK_MODEL\", \"openrouter/free\""` | — |
| [SRC-1AE03B9EC3-L000489](../../agents/web_agent.py#L489) | 489 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000490](../../agents/web_agent.py#L490) | 490 | `"        self.model = self.answer_model  # Backwards-compatible alias."` | — |
| [SRC-1AE03B9EC3-L000491](../../agents/web_agent.py#L491) | 491 | `"        self.model_usage: list[dict[str, str]] = []"` | — |
| [SRC-1AE03B9EC3-L000492](../../agents/web_agent.py#L492) | 492 | `"        # Per-answer, bounded diagnostics contain only model identifiers and status metadata."` | — |
| [SRC-1AE03B9EC3-L000493](../../agents/web_agent.py#L493) | 493 | `"        # They intentionally exclude prompts, generated text, and provider response bodies."` | — |
| [SRC-1AE03B9EC3-L000494](../../agents/web_agent.py#L494) | 494 | `"        self.generation_diagnostics: list[dict[str, str]] = []"` | — |
