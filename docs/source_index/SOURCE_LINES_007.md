# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **007**
- سجلات الأسطر: **800**
- النطاق: SRC-686F71AA50-L001124 إلى SRC-1AE03B9EC3-L000183
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
| [SRC-0799EEEB02-L000064](../../agents/tool_execution_status.py#L64) | 64 | `"        if isinstance(item, str) and item in _TOOL_LABELS"` | — |
| [SRC-0799EEEB02-L000065](../../agents/tool_execution_status.py#L65) | 65 | `"    } if isinstance(requirements, list) else set()"` | — |
| [SRC-0799EEEB02-L000066](../../agents/tool_execution_status.py#L66) | 66 | `""` | — |
| [SRC-0799EEEB02-L000067](../../agents/tool_execution_status.py#L67) | 67 | `"    outcome = str(search_report.get(\"search_outcome\") or \"unknown\")"` | — |
| [SRC-0799EEEB02-L000068](../../agents/tool_execution_status.py#L68) | 68 | `"    attempted = output.get(\"search_attempted\", search_report.get(\"search_attempted\"))"` | — |
| [SRC-0799EEEB02-L000069](../../agents/tool_execution_status.py#L69) | 69 | `"    reported_accepted_sources = _nonnegative_int("` | — |
| [SRC-0799EEEB02-L000070](../../agents/tool_execution_status.py#L70) | 70 | `"        search_report.get(\"usable_sources_after_filtering\")"` | — |
| [SRC-0799EEEB02-L000071](../../agents/tool_execution_status.py#L71) | 71 | `"    )"` | — |
| [SRC-0799EEEB02-L000072](../../agents/tool_execution_status.py#L72) | 72 | `"    reported_pages_read = _nonnegative_int(search_report.get(\"pages_fetched\"))"` | — |
| [SRC-0799EEEB02-L000073](../../agents/tool_execution_status.py#L73) | 73 | `"    pages_attempted = _nonnegative_int(search_report.get(\"pages_fetch_attempted\"))"` | — |
| [SRC-0799EEEB02-L000074](../../agents/tool_execution_status.py#L74) | 74 | `"    raw_source_rows = output.get(\"sources\")"` | — |
| [SRC-0799EEEB02-L000075](../../agents/tool_execution_status.py#L75) | 75 | `"    returned_sources_known = isinstance(raw_source_rows, list)"` | — |
| [SRC-0799EEEB02-L000076](../../agents/tool_execution_status.py#L76) | 76 | `"    source_rows = raw_source_rows if returned_sources_known else []"` | — |
| [SRC-0799EEEB02-L000077](../../agents/tool_execution_status.py#L77) | 77 | `"    readable_page_rows = sum("` | — |
| [SRC-0799EEEB02-L000078](../../agents/tool_execution_status.py#L78) | 78 | `"        1 for source in source_rows"` | — |
| [SRC-0799EEEB02-L000079](../../agents/tool_execution_status.py#L79) | 79 | `"        if isinstance(source, dict)"` | — |
| [SRC-0799EEEB02-L000080](../../agents/tool_execution_status.py#L80) | 80 | `"        and source.get(\"page_fetched\") is True"` | — |
| [SRC-0799EEEB02-L000081](../../agents/tool_execution_status.py#L81) | 81 | `"    )"` | — |
| [SRC-0799EEEB02-L000082](../../agents/tool_execution_status.py#L82) | 82 | `"    # The public return value is the final accepted source set. Prefer it when"` | — |
| [SRC-0799EEEB02-L000083](../../agents/tool_execution_status.py#L83) | 83 | `"    # present; preserve report counters separately so disagreements stay visible."` | — |
| [SRC-0799EEEB02-L000084](../../agents/tool_execution_status.py#L84) | 84 | `"    returned_source_count = len(source_rows) if returned_sources_known else None"` | — |
| [SRC-0799EEEB02-L000085](../../agents/tool_execution_status.py#L85) | 85 | `"    accepted_sources = ("` | — |
| [SRC-0799EEEB02-L000086](../../agents/tool_execution_status.py#L86) | 86 | `"        returned_source_count if returned_sources_known else reported_accepted_sources"` | — |
| [SRC-0799EEEB02-L000087](../../agents/tool_execution_status.py#L87) | 87 | `"    )"` | — |
| [SRC-0799EEEB02-L000088](../../agents/tool_execution_status.py#L88) | 88 | `"    pages_read = reported_pages_read if reported_pages_read is not None else readable_page_rows"` | — |
| [SRC-0799EEEB02-L000089](../../agents/tool_execution_status.py#L89) | 89 | `"    source_count_mismatch = ("` | — |
| [SRC-0799EEEB02-L000090](../../agents/tool_execution_status.py#L90) | 90 | `"        returned_sources_known"` | — |
| [SRC-0799EEEB02-L000091](../../agents/tool_execution_status.py#L91) | 91 | `"        and reported_accepted_sources is not None"` | — |
| [SRC-0799EEEB02-L000092](../../agents/tool_execution_status.py#L92) | 92 | `"        and reported_accepted_sources != returned_source_count"` | — |
| [SRC-0799EEEB02-L000093](../../agents/tool_execution_status.py#L93) | 93 | `"    )"` | — |
| [SRC-0799EEEB02-L000094](../../agents/tool_execution_status.py#L94) | 94 | `"    page_count_mismatch = ("` | — |
| [SRC-0799EEEB02-L000095](../../agents/tool_execution_status.py#L95) | 95 | `"        returned_sources_known"` | — |
| [SRC-0799EEEB02-L000096](../../agents/tool_execution_status.py#L96) | 96 | `"        and reported_pages_read is not None"` | — |
| [SRC-0799EEEB02-L000097](../../agents/tool_execution_status.py#L97) | 97 | `"        and reported_pages_read != readable_page_rows"` | — |
| [SRC-0799EEEB02-L000098](../../agents/tool_execution_status.py#L98) | 98 | `"    )"` | — |
| [SRC-0799EEEB02-L000099](../../agents/tool_execution_status.py#L99) | 99 | `""` | — |
| [SRC-0799EEEB02-L000100](../../agents/tool_execution_status.py#L100) | 100 | `"    rows: list[dict[str, Any]] = []"` | — |
| [SRC-0799EEEB02-L000101](../../agents/tool_execution_status.py#L101) | 101 | `""` | — |
| [SRC-0799EEEB02-L000102](../../agents/tool_execution_status.py#L102) | 102 | `"    # Search completion and evidence acceptance are distinct: zero accepted sources"` | — |
| [SRC-0799EEEB02-L000103](../../agents/tool_execution_status.py#L103) | 103 | `"    # means this retrieval attempt supplied no eligible evidence, not that the fact"` | — |
| [SRC-0799EEEB02-L000104](../../agents/tool_execution_status.py#L104) | 104 | `"    # or source does not exist."` | — |
| [SRC-0799EEEB02-L000105](../../agents/tool_execution_status.py#L105) | 105 | `"    tool = \"web_search\""` | — |
| [SRC-0799EEEB02-L000106](../../agents/tool_execution_status.py#L106) | 106 | `"    if tool not in required:"` | — |
| [SRC-0799EEEB02-L000107](../../agents/tool_execution_status.py#L107) | 107 | `"        status = \"not_required\""` | — |
| [SRC-0799EEEB02-L000108](../../agents/tool_execution_status.py#L108) | 108 | `"    elif outcome == \"attempted_research_error\":"` | — |
| [SRC-0799EEEB02-L000109](../../agents/tool_execution_status.py#L109) | 109 | `"        status = \"failed\""` | — |
| [SRC-0799EEEB02-L000110](../../agents/tool_execution_status.py#L110) | 110 | `"    elif outcome in {\"unknown_after_research_error\", \"unknown_after_budget_exhaustion\"}:"` | — |
| [SRC-0799EEEB02-L000111](../../agents/tool_execution_status.py#L111) | 111 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000112](../../agents/tool_execution_status.py#L112) | 112 | `"    elif outcome == \"not_attempted\" or attempted is False:"` | — |
| [SRC-0799EEEB02-L000113](../../agents/tool_execution_status.py#L113) | 113 | `"        status = \"not_attempted\""` | — |
| [SRC-0799EEEB02-L000114](../../agents/tool_execution_status.py#L114) | 114 | `"    elif source_count_mismatch:"` | — |
| [SRC-0799EEEB02-L000115](../../agents/tool_execution_status.py#L115) | 115 | `"        status = \"counter_mismatch\""` | — |
| [SRC-0799EEEB02-L000116](../../agents/tool_execution_status.py#L116) | 116 | `"    elif attempted is True:"` | — |
| [SRC-0799EEEB02-L000117](../../agents/tool_execution_status.py#L117) | 117 | `"        if accepted_sources is not None:"` | — |
| [SRC-0799EEEB02-L000118](../../agents/tool_execution_status.py#L118) | 118 | `"            status = \"completed_with_results\" if accepted_sources > 0 else \"completed_no_usable_results\""` | — |
| [SRC-0799EEEB02-L000119](../../agents/tool_execution_status.py#L119) | 119 | `"        elif outcome == \"attempted_with_usable_sources\":"` | — |
| [SRC-0799EEEB02-L000120](../../agents/tool_execution_status.py#L120) | 120 | `"            status = \"completed_with_results\""` | — |
| [SRC-0799EEEB02-L000121](../../agents/tool_execution_status.py#L121) | 121 | `"        elif outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-0799EEEB02-L000122](../../agents/tool_execution_status.py#L122) | 122 | `"            status = \"completed_no_usable_results\""` | — |
| [SRC-0799EEEB02-L000123](../../agents/tool_execution_status.py#L123) | 123 | `"        else:"` | — |
| [SRC-0799EEEB02-L000124](../../agents/tool_execution_status.py#L124) | 124 | `"            status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000125](../../agents/tool_execution_status.py#L125) | 125 | `"    else:"` | — |
| [SRC-0799EEEB02-L000126](../../agents/tool_execution_status.py#L126) | 126 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000127](../../agents/tool_execution_status.py#L127) | 127 | `"    rows.append(_status_row(tool, tool in required, status, {"` | — |
| [SRC-0799EEEB02-L000128](../../agents/tool_execution_status.py#L128) | 128 | `"        \"search_outcome\": outcome,"` | — |
| [SRC-0799EEEB02-L000129](../../agents/tool_execution_status.py#L129) | 129 | `"        \"search_attempted\": attempted if isinstance(attempted, bool) else None,"` | — |
| [SRC-0799EEEB02-L000130](../../agents/tool_execution_status.py#L130) | 130 | `"        \"accepted_source_count\": accepted_sources,"` | — |
| [SRC-0799EEEB02-L000131](../../agents/tool_execution_status.py#L131) | 131 | `"        \"reported_accepted_source_count\": reported_accepted_sources,"` | — |
| [SRC-0799EEEB02-L000132](../../agents/tool_execution_status.py#L132) | 132 | `"        \"counter_consistency\": ("` | — |
| [SRC-0799EEEB02-L000133](../../agents/tool_execution_status.py#L133) | 133 | `"            \"mismatch\" if source_count_mismatch else \"consistent\""` | — |
| [SRC-0799EEEB02-L000134](../../agents/tool_execution_status.py#L134) | 134 | `"            if returned_sources_known and reported_accepted_sources is not None"` | — |
| [SRC-0799EEEB02-L000135](../../agents/tool_execution_status.py#L135) | 135 | `"            else \"not_comparable\""` | — |
| [SRC-0799EEEB02-L000136](../../agents/tool_execution_status.py#L136) | 136 | `"        ),"` | — |
| [SRC-0799EEEB02-L000137](../../agents/tool_execution_status.py#L137) | 137 | `"    }))"` | — |
| [SRC-0799EEEB02-L000138](../../agents/tool_execution_status.py#L138) | 138 | `""` | — |
| [SRC-0799EEEB02-L000139](../../agents/tool_execution_status.py#L139) | 139 | `"    tool = \"page_fetch\""` | — |
| [SRC-0799EEEB02-L000140](../../agents/tool_execution_status.py#L140) | 140 | `"    if tool not in required:"` | — |
| [SRC-0799EEEB02-L000141](../../agents/tool_execution_status.py#L141) | 141 | `"        status = \"not_required\""` | — |
| [SRC-0799EEEB02-L000142](../../agents/tool_execution_status.py#L142) | 142 | `"    elif page_count_mismatch:"` | — |
| [SRC-0799EEEB02-L000143](../../agents/tool_execution_status.py#L143) | 143 | `"        status = \"counter_mismatch\""` | — |
| [SRC-0799EEEB02-L000144](../../agents/tool_execution_status.py#L144) | 144 | `"    elif pages_read > 0:"` | — |
| [SRC-0799EEEB02-L000145](../../agents/tool_execution_status.py#L145) | 145 | `"        status = \"completed_with_read_pages\""` | — |
| [SRC-0799EEEB02-L000146](../../agents/tool_execution_status.py#L146) | 146 | `"    elif pages_attempted is not None and pages_attempted > 0:"` | — |
| [SRC-0799EEEB02-L000147](../../agents/tool_execution_status.py#L147) | 147 | `"        status = \"attempted_no_readable_pages\""` | — |
| [SRC-0799EEEB02-L000148](../../agents/tool_execution_status.py#L148) | 148 | `"    elif pages_attempted is None:"` | — |
| [SRC-0799EEEB02-L000149](../../agents/tool_execution_status.py#L149) | 149 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000150](../../agents/tool_execution_status.py#L150) | 150 | `"    elif outcome in _ERROR_OUTCOMES:"` | — |
| [SRC-0799EEEB02-L000151](../../agents/tool_execution_status.py#L151) | 151 | `"        status = \"not_attempted_after_search_error\""` | — |
| [SRC-0799EEEB02-L000152](../../agents/tool_execution_status.py#L152) | 152 | `"    elif attempted is True:"` | — |
| [SRC-0799EEEB02-L000153](../../agents/tool_execution_status.py#L153) | 153 | `"        status = \"not_attempted_no_fetchable_candidates\""` | — |
| [SRC-0799EEEB02-L000154](../../agents/tool_execution_status.py#L154) | 154 | `"    elif attempted is False:"` | — |
| [SRC-0799EEEB02-L000155](../../agents/tool_execution_status.py#L155) | 155 | `"        status = \"not_attempted\""` | — |
| [SRC-0799EEEB02-L000156](../../agents/tool_execution_status.py#L156) | 156 | `"    else:"` | — |
| [SRC-0799EEEB02-L000157](../../agents/tool_execution_status.py#L157) | 157 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000158](../../agents/tool_execution_status.py#L158) | 158 | `"    rows.append(_status_row(tool, tool in required, status, {"` | — |
| [SRC-0799EEEB02-L000159](../../agents/tool_execution_status.py#L159) | 159 | `"        \"pages_fetch_attempted\": pages_attempted,"` | — |
| [SRC-0799EEEB02-L000160](../../agents/tool_execution_status.py#L160) | 160 | `"        \"pages_read\": pages_read,"` | — |
| [SRC-0799EEEB02-L000161](../../agents/tool_execution_status.py#L161) | 161 | `"        \"reported_pages_fetched\": reported_pages_read,"` | — |
| [SRC-0799EEEB02-L000162](../../agents/tool_execution_status.py#L162) | 162 | `"        \"pages_read_from_returned_sources\": readable_page_rows,"` | — |
| [SRC-0799EEEB02-L000163](../../agents/tool_execution_status.py#L163) | 163 | `"        \"counter_consistency\": ("` | — |
| [SRC-0799EEEB02-L000164](../../agents/tool_execution_status.py#L164) | 164 | `"            \"mismatch\" if page_count_mismatch else \"consistent\""` | — |
| [SRC-0799EEEB02-L000165](../../agents/tool_execution_status.py#L165) | 165 | `"            if returned_sources_known and reported_pages_read is not None"` | — |
| [SRC-0799EEEB02-L000166](../../agents/tool_execution_status.py#L166) | 166 | `"            else \"not_comparable\""` | — |
| [SRC-0799EEEB02-L000167](../../agents/tool_execution_status.py#L167) | 167 | `"        ),"` | — |
| [SRC-0799EEEB02-L000168](../../agents/tool_execution_status.py#L168) | 168 | `"    }))"` | — |
| [SRC-0799EEEB02-L000169](../../agents/tool_execution_status.py#L169) | 169 | `""` | — |
| [SRC-0799EEEB02-L000170](../../agents/tool_execution_status.py#L170) | 170 | `"    tool = \"public_social_search_if_configured\""` | — |
| [SRC-0799EEEB02-L000171](../../agents/tool_execution_status.py#L171) | 171 | `"    raw_social_results = _nonnegative_int(search_report.get(\"social_direct_results\"))"` | — |
| [SRC-0799EEEB02-L000172](../../agents/tool_execution_status.py#L172) | 172 | `"    social_results = raw_social_results or 0"` | — |
| [SRC-0799EEEB02-L000173](../../agents/tool_execution_status.py#L173) | 173 | `"    social_sources = sum("` | — |
| [SRC-0799EEEB02-L000174](../../agents/tool_execution_status.py#L174) | 174 | `"        1 for source in source_rows"` | — |
| [SRC-0799EEEB02-L000175](../../agents/tool_execution_status.py#L175) | 175 | `"        if isinstance(source, dict)"` | — |
| [SRC-0799EEEB02-L000176](../../agents/tool_execution_status.py#L176) | 176 | `"        and ("` | — |
| [SRC-0799EEEB02-L000177](../../agents/tool_execution_status.py#L177) | 177 | `"            str(source.get(\"platform\") or \"\").lower() in _SOCIAL_PLATFORMS"` | — |
| [SRC-0799EEEB02-L000178](../../agents/tool_execution_status.py#L178) | 178 | `"            or str(source.get(\"source_class\") or \"\").lower() == \"social\""` | — |
| [SRC-0799EEEB02-L000179](../../agents/tool_execution_status.py#L179) | 179 | `"        )"` | — |
| [SRC-0799EEEB02-L000180](../../agents/tool_execution_status.py#L180) | 180 | `"    )"` | — |
| [SRC-0799EEEB02-L000181](../../agents/tool_execution_status.py#L181) | 181 | `"    connector_summary = search_report.get(\"connector_summary\")"` | — |
| [SRC-0799EEEB02-L000182](../../agents/tool_execution_status.py#L182) | 182 | `"    connector_summary = connector_summary if isinstance(connector_summary, dict) else {}"` | — |
| [SRC-0799EEEB02-L000183](../../agents/tool_execution_status.py#L183) | 183 | `"    connector_rows = connector_summary.get(\"connectors\")"` | — |
| [SRC-0799EEEB02-L000184](../../agents/tool_execution_status.py#L184) | 184 | `"    connector_rows = connector_rows if isinstance(connector_rows, list) else []"` | — |
| [SRC-0799EEEB02-L000185](../../agents/tool_execution_status.py#L185) | 185 | `"    social_connector_names = {"` | — |
| [SRC-0799EEEB02-L000186](../../agents/tool_execution_status.py#L186) | 186 | `"        \"reddit_public_rss\", \"bluesky_public_search\", \"reddit_oauth_api\","` | — |
| [SRC-0799EEEB02-L000187](../../agents/tool_execution_status.py#L187) | 187 | `"        \"facebook_pages_api\", \"instagram_graph_api\", \"x_official_api\","` | — |
| [SRC-0799EEEB02-L000188](../../agents/tool_execution_status.py#L188) | 188 | `"        \"youtube_data_api\","` | — |
| [SRC-0799EEEB02-L000189](../../agents/tool_execution_status.py#L189) | 189 | `"    }"` | — |
| [SRC-0799EEEB02-L000190](../../agents/tool_execution_status.py#L190) | 190 | `"    social_connector_states = ["` | — |
| [SRC-0799EEEB02-L000191](../../agents/tool_execution_status.py#L191) | 191 | `"        row for row in connector_rows"` | — |
| [SRC-0799EEEB02-L000192](../../agents/tool_execution_status.py#L192) | 192 | `"        if isinstance(row, dict) and row.get(\"name\") in social_connector_names"` | — |
| [SRC-0799EEEB02-L000193](../../agents/tool_execution_status.py#L193) | 193 | `"    ]"` | — |
| [SRC-0799EEEB02-L000194](../../agents/tool_execution_status.py#L194) | 194 | `"    attempted_social_connectors = ["` | — |
| [SRC-0799EEEB02-L000195](../../agents/tool_execution_status.py#L195) | 195 | `"        row for row in social_connector_states if row.get(\"attempted\") is True"` | — |
| [SRC-0799EEEB02-L000196](../../agents/tool_execution_status.py#L196) | 196 | `"    ]"` | — |
| [SRC-0799EEEB02-L000197](../../agents/tool_execution_status.py#L197) | 197 | `"    social_connector_errors = ["` | — |
| [SRC-0799EEEB02-L000198](../../agents/tool_execution_status.py#L198) | 198 | `"        row for row in social_connector_states"` | — |
| [SRC-0799EEEB02-L000199](../../agents/tool_execution_status.py#L199) | 199 | `"        if row.get(\"status\") in {"` | — |
| [SRC-0799EEEB02-L000200](../../agents/tool_execution_status.py#L200) | 200 | `"            \"failed\", \"error\", \"timeout\", \"http_error\", \"unauthorized\","` | — |
| [SRC-0799EEEB02-L000201](../../agents/tool_execution_status.py#L201) | 201 | `"            \"rate_limited\", \"budget_exhausted\","` | — |
| [SRC-0799EEEB02-L000202](../../agents/tool_execution_status.py#L202) | 202 | `"        }"` | — |
| [SRC-0799EEEB02-L000203](../../agents/tool_execution_status.py#L203) | 203 | `"    ]"` | — |
| [SRC-0799EEEB02-L000204](../../agents/tool_execution_status.py#L204) | 204 | `"    social_configured_connectors = ["` | — |
| [SRC-0799EEEB02-L000205](../../agents/tool_execution_status.py#L205) | 205 | `"        row for row in social_connector_states"` | — |
| [SRC-0799EEEB02-L000206](../../agents/tool_execution_status.py#L206) | 206 | `"        if row.get(\"configured\") is True"` | — |
| [SRC-0799EEEB02-L000207](../../agents/tool_execution_status.py#L207) | 207 | `"    ]"` | — |
| [SRC-0799EEEB02-L000208](../../agents/tool_execution_status.py#L208) | 208 | `"    social_not_configured_connectors = ["` | — |
| [SRC-0799EEEB02-L000209](../../agents/tool_execution_status.py#L209) | 209 | `"        row for row in social_connector_states"` | — |
| [SRC-0799EEEB02-L000210](../../agents/tool_execution_status.py#L210) | 210 | `"        if row.get(\"configured\") is False"` | — |
| [SRC-0799EEEB02-L000211](../../agents/tool_execution_status.py#L211) | 211 | `"    ]"` | — |
| [SRC-0799EEEB02-L000212](../../agents/tool_execution_status.py#L212) | 212 | `"    if tool not in required:"` | — |
| [SRC-0799EEEB02-L000213](../../agents/tool_execution_status.py#L213) | 213 | `"        status = \"not_required\""` | — |
| [SRC-0799EEEB02-L000214](../../agents/tool_execution_status.py#L214) | 214 | `"    elif social_results > 0 or social_sources > 0:"` | — |
| [SRC-0799EEEB02-L000215](../../agents/tool_execution_status.py#L215) | 215 | `"        status = \"completed_with_results\""` | — |
| [SRC-0799EEEB02-L000216](../../agents/tool_execution_status.py#L216) | 216 | `"    elif outcome in _ERROR_OUTCOMES and outcome == \"attempted_research_error\":"` | — |
| [SRC-0799EEEB02-L000217](../../agents/tool_execution_status.py#L217) | 217 | `"        status = \"failed\""` | — |
| [SRC-0799EEEB02-L000218](../../agents/tool_execution_status.py#L218) | 218 | `"    elif outcome in _ERROR_OUTCOMES:"` | — |
| [SRC-0799EEEB02-L000219](../../agents/tool_execution_status.py#L219) | 219 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000220](../../agents/tool_execution_status.py#L220) | 220 | `"    elif attempted_social_connectors:"` | — |
| [SRC-0799EEEB02-L000221](../../agents/tool_execution_status.py#L221) | 221 | `"        status = \"failed\" if social_connector_errors else \"completed_no_usable_results\""` | — |
| [SRC-0799EEEB02-L000222](../../agents/tool_execution_status.py#L222) | 222 | `"    elif social_configured_connectors and all("` | — |
| [SRC-0799EEEB02-L000223](../../agents/tool_execution_status.py#L223) | 223 | `"        row.get(\"attempted\") is False for row in social_configured_connectors"` | — |
| [SRC-0799EEEB02-L000224](../../agents/tool_execution_status.py#L224) | 224 | `"    ):"` | — |
| [SRC-0799EEEB02-L000225](../../agents/tool_execution_status.py#L225) | 225 | `"        status = \"not_attempted\""` | — |
| [SRC-0799EEEB02-L000226](../../agents/tool_execution_status.py#L226) | 226 | `"    elif social_not_configured_connectors and ("` | — |
| [SRC-0799EEEB02-L000227](../../agents/tool_execution_status.py#L227) | 227 | `"        not social_configured_connectors or not attempted_social_connectors"` | — |
| [SRC-0799EEEB02-L000228](../../agents/tool_execution_status.py#L228) | 228 | `"    ):"` | — |
| [SRC-0799EEEB02-L000229](../../agents/tool_execution_status.py#L229) | 229 | `"        status = \"not_configured\""` | — |
| [SRC-0799EEEB02-L000230](../../agents/tool_execution_status.py#L230) | 230 | `"    elif raw_social_results is None and not social_connector_states:"` | — |
| [SRC-0799EEEB02-L000231](../../agents/tool_execution_status.py#L231) | 231 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000232](../../agents/tool_execution_status.py#L232) | 232 | `"    elif attempted is False:"` | — |
| [SRC-0799EEEB02-L000233](../../agents/tool_execution_status.py#L233) | 233 | `"        status = \"not_attempted\""` | — |
| [SRC-0799EEEB02-L000234](../../agents/tool_execution_status.py#L234) | 234 | `"    else:"` | — |
| [SRC-0799EEEB02-L000235](../../agents/tool_execution_status.py#L235) | 235 | `"        # A general web search attempt is not proof that social connectors ran."` | — |
| [SRC-0799EEEB02-L000236](../../agents/tool_execution_status.py#L236) | 236 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000237](../../agents/tool_execution_status.py#L237) | 237 | `"    rows.append(_status_row(tool, tool in required, status, {"` | — |
| [SRC-0799EEEB02-L000238](../../agents/tool_execution_status.py#L238) | 238 | `"        \"social_direct_results\": social_results,"` | — |
| [SRC-0799EEEB02-L000239](../../agents/tool_execution_status.py#L239) | 239 | `"        \"social_result_count_known\": raw_social_results is not None,"` | — |
| [SRC-0799EEEB02-L000240](../../agents/tool_execution_status.py#L240) | 240 | `"        \"accepted_social_sources\": social_sources,"` | — |
| [SRC-0799EEEB02-L000241](../../agents/tool_execution_status.py#L241) | 241 | `"        \"social_connectors_observed\": ["` | — |
| [SRC-0799EEEB02-L000242](../../agents/tool_execution_status.py#L242) | 242 | `"            {"` | — |
| [SRC-0799EEEB02-L000243](../../agents/tool_execution_status.py#L243) | 243 | `"                \"name\": row.get(\"name\"),"` | — |
| [SRC-0799EEEB02-L000244](../../agents/tool_execution_status.py#L244) | 244 | `"                \"configured\": row.get(\"configured\"),"` | — |
| [SRC-0799EEEB02-L000245](../../agents/tool_execution_status.py#L245) | 245 | `"                \"attempted\": row.get(\"attempted\"),"` | — |
| [SRC-0799EEEB02-L000246](../../agents/tool_execution_status.py#L246) | 246 | `"                \"status\": row.get(\"status\"),"` | — |
| [SRC-0799EEEB02-L000247](../../agents/tool_execution_status.py#L247) | 247 | `"            }"` | — |
| [SRC-0799EEEB02-L000248](../../agents/tool_execution_status.py#L248) | 248 | `"            for row in social_connector_states[:8]"` | — |
| [SRC-0799EEEB02-L000249](../../agents/tool_execution_status.py#L249) | 249 | `"        ],"` | — |
| [SRC-0799EEEB02-L000250](../../agents/tool_execution_status.py#L250) | 250 | `"        \"search_outcome\": outcome,"` | — |
| [SRC-0799EEEB02-L000251](../../agents/tool_execution_status.py#L251) | 251 | `"        \"interpretation\": ("` | — |
| [SRC-0799EEEB02-L000252](../../agents/tool_execution_status.py#L252) | 252 | `"            \"A general web search attempt does not prove that a social connector was attempted.\""` | — |
| [SRC-0799EEEB02-L000253](../../agents/tool_execution_status.py#L253) | 253 | `"        ),"` | — |
| [SRC-0799EEEB02-L000254](../../agents/tool_execution_status.py#L254) | 254 | `"    }))"` | — |
| [SRC-0799EEEB02-L000255](../../agents/tool_execution_status.py#L255) | 255 | `""` | — |
| [SRC-0799EEEB02-L000256](../../agents/tool_execution_status.py#L256) | 256 | `"    tool = \"language_model_generation_if_configured\""` | — |
| [SRC-0799EEEB02-L000257](../../agents/tool_execution_status.py#L257) | 257 | `"    final_status = str(output.get(\"final_answer_status\") or \"\")"` | — |
| [SRC-0799EEEB02-L000258](../../agents/tool_execution_status.py#L258) | 258 | `"    used_model = output.get(\"used_language_model\") is True"` | — |
| [SRC-0799EEEB02-L000259](../../agents/tool_execution_status.py#L259) | 259 | `"    if tool not in required:"` | — |
| [SRC-0799EEEB02-L000260](../../agents/tool_execution_status.py#L260) | 260 | `"        status = \"not_required\""` | — |
| [SRC-0799EEEB02-L000261](../../agents/tool_execution_status.py#L261) | 261 | `"    elif used_model:"` | — |
| [SRC-0799EEEB02-L000262](../../agents/tool_execution_status.py#L262) | 262 | `"        status = \"completed\""` | — |
| [SRC-0799EEEB02-L000263](../../agents/tool_execution_status.py#L263) | 263 | `"    elif final_status in {"` | — |
| [SRC-0799EEEB02-L000264](../../agents/tool_execution_status.py#L264) | 264 | `"        \"model_not_configured_fallback\", \"model_not_configured\","` | — |
| [SRC-0799EEEB02-L000265](../../agents/tool_execution_status.py#L265) | 265 | `"    }:"` | — |
| [SRC-0799EEEB02-L000266](../../agents/tool_execution_status.py#L266) | 266 | `"        status = \"not_configured\""` | — |
| [SRC-0799EEEB02-L000267](../../agents/tool_execution_status.py#L267) | 267 | `"    elif final_status in {"` | — |
| [SRC-0799EEEB02-L000268](../../agents/tool_execution_status.py#L268) | 268 | `"        \"generation_failed\", \"generation_failed_with_source_fallback\","` | — |
| [SRC-0799EEEB02-L000269](../../agents/tool_execution_status.py#L269) | 269 | `"        \"budget_exhausted\", \"budget_exhausted_with_source_fallback\","` | — |
| [SRC-0799EEEB02-L000270](../../agents/tool_execution_status.py#L270) | 270 | `"    }:"` | — |
| [SRC-0799EEEB02-L000271](../../agents/tool_execution_status.py#L271) | 271 | `"        status = \"failed\""` | — |
| [SRC-0799EEEB02-L000272](../../agents/tool_execution_status.py#L272) | 272 | `"    elif final_status in {"` | — |
| [SRC-0799EEEB02-L000273](../../agents/tool_execution_status.py#L273) | 273 | `"        \"clarification_required\", \"insufficient_evidence_no_generation\","` | — |
| [SRC-0799EEEB02-L000274](../../agents/tool_execution_status.py#L274) | 274 | `"        \"not_attempted\", \"local_response_no_generation\","` | — |
| [SRC-0799EEEB02-L000275](../../agents/tool_execution_status.py#L275) | 275 | `"    }:"` | — |
| [SRC-0799EEEB02-L000276](../../agents/tool_execution_status.py#L276) | 276 | `"        status = \"not_attempted\""` | — |
| [SRC-0799EEEB02-L000277](../../agents/tool_execution_status.py#L277) | 277 | `"    elif output.get(\"kind\") == \"insufficient_evidence\":"` | — |
| [SRC-0799EEEB02-L000278](../../agents/tool_execution_status.py#L278) | 278 | `"        status = \"not_attempted_no_evidence\""` | — |
| [SRC-0799EEEB02-L000279](../../agents/tool_execution_status.py#L279) | 279 | `"    else:"` | — |
| [SRC-0799EEEB02-L000280](../../agents/tool_execution_status.py#L280) | 280 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000281](../../agents/tool_execution_status.py#L281) | 281 | `"    rows.append(_status_row(tool, tool in required, status, {"` | — |
| [SRC-0799EEEB02-L000282](../../agents/tool_execution_status.py#L282) | 282 | `"        \"used_language_model\": used_model,"` | — |
| [SRC-0799EEEB02-L000283](../../agents/tool_execution_status.py#L283) | 283 | `"        \"final_answer_status\": final_status or \"unknown\","` | — |
| [SRC-0799EEEB02-L000284](../../agents/tool_execution_status.py#L284) | 284 | `"    }))"` | — |
| [SRC-0799EEEB02-L000285](../../agents/tool_execution_status.py#L285) | 285 | `""` | — |
| [SRC-0799EEEB02-L000286](../../agents/tool_execution_status.py#L286) | 286 | `"    tool = \"claim_review_if_configured\""` | — |
| [SRC-0799EEEB02-L000287](../../agents/tool_execution_status.py#L287) | 287 | `"    review_status = str("` | — |
| [SRC-0799EEEB02-L000288](../../agents/tool_execution_status.py#L288) | 288 | `"        search_report.get(\"claim_audit\")"` | — |
| [SRC-0799EEEB02-L000289](../../agents/tool_execution_status.py#L289) | 289 | `"        or search_report.get(\"second_pass_review\")"` | — |
| [SRC-0799EEEB02-L000290](../../agents/tool_execution_status.py#L290) | 290 | `"        or \"unknown\""` | — |
| [SRC-0799EEEB02-L000291](../../agents/tool_execution_status.py#L291) | 291 | `"    )"` | — |
| [SRC-0799EEEB02-L000292](../../agents/tool_execution_status.py#L292) | 292 | `"    if tool not in required:"` | — |
| [SRC-0799EEEB02-L000293](../../agents/tool_execution_status.py#L293) | 293 | `"        status = \"not_required\""` | — |
| [SRC-0799EEEB02-L000294](../../agents/tool_execution_status.py#L294) | 294 | `"    elif review_status == \"model_claim_audit_completed\":"` | — |
| [SRC-0799EEEB02-L000295](../../agents/tool_execution_status.py#L295) | 295 | `"        status = \"completed_model_assisted_review\""` | — |
| [SRC-0799EEEB02-L000296](../../agents/tool_execution_status.py#L296) | 296 | `"    elif review_status in {"` | — |
| [SRC-0799EEEB02-L000297](../../agents/tool_execution_status.py#L297) | 297 | `"        \"model_claim_audit_unavailable\", \"review_failed_with_source_fallback\","` | — |
| [SRC-0799EEEB02-L000298](../../agents/tool_execution_status.py#L298) | 298 | `"    }:"` | — |
| [SRC-0799EEEB02-L000299](../../agents/tool_execution_status.py#L299) | 299 | `"        status = \"failed\""` | — |
| [SRC-0799EEEB02-L000300](../../agents/tool_execution_status.py#L300) | 300 | `"    elif review_status in {\"not_run\", \"not_assessed\", \"not_verified\"}:"` | — |
| [SRC-0799EEEB02-L000301](../../agents/tool_execution_status.py#L301) | 301 | `"        status = ("` | — |
| [SRC-0799EEEB02-L000302](../../agents/tool_execution_status.py#L302) | 302 | `"            \"not_attempted_no_evidence\""` | — |
| [SRC-0799EEEB02-L000303](../../agents/tool_execution_status.py#L303) | 303 | `"            if not source_rows else \"not_attempted\""` | — |
| [SRC-0799EEEB02-L000304](../../agents/tool_execution_status.py#L304) | 304 | `"        )"` | — |
| [SRC-0799EEEB02-L000305](../../agents/tool_execution_status.py#L305) | 305 | `"    else:"` | — |
| [SRC-0799EEEB02-L000306](../../agents/tool_execution_status.py#L306) | 306 | `"        status = \"unknown\""` | — |
| [SRC-0799EEEB02-L000307](../../agents/tool_execution_status.py#L307) | 307 | `"    rows.append(_status_row(tool, tool in required, status, {"` | — |
| [SRC-0799EEEB02-L000308](../../agents/tool_execution_status.py#L308) | 308 | `"        \"review_status\": review_status,"` | — |
| [SRC-0799EEEB02-L000309](../../agents/tool_execution_status.py#L309) | 309 | `"        \"independent_fact_check\": False,"` | — |
| [SRC-0799EEEB02-L000310](../../agents/tool_execution_status.py#L310) | 310 | `"    }))"` | — |
| [SRC-0799EEEB02-L000311](../../agents/tool_execution_status.py#L311) | 311 | `"    return rows"` | — |
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
| [SRC-1AE03B9EC3-L000051](../../agents/web_agent.py#L51) | 51 | `"from agents.tool_execution_status import build_tool_execution_matrix"` | — |
| [SRC-1AE03B9EC3-L000052](../../agents/web_agent.py#L52) | 52 | `"from agents.task_understanding import ("` | — |
| [SRC-1AE03B9EC3-L000053](../../agents/web_agent.py#L53) | 53 | `"    build_query_strategy_matrix,"` | — |
| [SRC-1AE03B9EC3-L000054](../../agents/web_agent.py#L54) | 54 | `"    build_task_spec,"` | — |
| [SRC-1AE03B9EC3-L000055](../../agents/web_agent.py#L55) | 55 | `"    reasoning_guidance_for_task_spec,"` | — |
| [SRC-1AE03B9EC3-L000056](../../agents/web_agent.py#L56) | 56 | `"    validate_task_spec,"` | — |
| [SRC-1AE03B9EC3-L000057](../../agents/web_agent.py#L57) | 57 | `")"` | — |
| [SRC-1AE03B9EC3-L000058](../../agents/web_agent.py#L58) | 58 | `""` | — |
| [SRC-1AE03B9EC3-L000059](../../agents/web_agent.py#L59) | 59 | `"MAX_QUESTION_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000060](../../agents/web_agent.py#L60) | 60 | `"MAX_HISTORY_ITEMS = 8"` | — |
| [SRC-1AE03B9EC3-L000061](../../agents/web_agent.py#L61) | 61 | `"MAX_HISTORY_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000062](../../agents/web_agent.py#L62) | 62 | `"MAX_SEARCH_RESULTS = 18"` | — |
| [SRC-1AE03B9EC3-L000063](../../agents/web_agent.py#L63) | 63 | `"MAX_PROVIDER_RESULTS = 6"` | — |
| [SRC-1AE03B9EC3-L000064](../../agents/web_agent.py#L64) | 64 | `"MAX_FETCHED_PAGES = 8"` | — |
| [SRC-1AE03B9EC3-L000065](../../agents/web_agent.py#L65) | 65 | `"MAX_LLM_CITED_SOURCES = 12"` | — |
| [SRC-1AE03B9EC3-L000066](../../agents/web_agent.py#L66) | 66 | `"MAX_RESEARCH_WORKERS = 8"` | — |
| [SRC-1AE03B9EC3-L000067](../../agents/web_agent.py#L67) | 67 | `"MAX_PAGE_BYTES = 1_000_000"` | — |
| [SRC-1AE03B9EC3-L000068](../../agents/web_agent.py#L68) | 68 | `"MAX_PAGE_TEXT_CHARS = 12_000"` | — |
| [SRC-1AE03B9EC3-L000069](../../agents/web_agent.py#L69) | 69 | `"LLM_TIMEOUT_SECONDS = 35"` | — |
| [SRC-1AE03B9EC3-L000070](../../agents/web_agent.py#L70) | 70 | `""` | — |
| [SRC-1AE03B9EC3-L000071](../../agents/web_agent.py#L71) | 71 | `"# Only completed connector result-processing states positively confirm an attempt."` | — |
| [SRC-1AE03B9EC3-L000072](../../agents/web_agent.py#L72) | 72 | `"# A generic \"failed\" or timeout diagnostic may occur before a network request is sent."` | — |
| [SRC-1AE03B9EC3-L000073](../../agents/web_agent.py#L73) | 73 | `"_SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES = frozenset({\"ok\", \"no_results\", \"filtered_all\"})"` | — |
| [SRC-1AE03B9EC3-L000074](../../agents/web_agent.py#L74) | 74 | `"_RESEARCH_ERROR_OUTCOMES = frozenset({\"attempted_research_error\", \"unknown_after_research_error\"})"` | — |
| [SRC-1AE03B9EC3-L000075](../../agents/web_agent.py#L75) | 75 | `"_PROVIDER_REJECTION_REASONS = ("` | — |
| [SRC-1AE03B9EC3-L000076](../../agents/web_agent.py#L76) | 76 | `"    \"malformed_candidate\","` | — |
| [SRC-1AE03B9EC3-L000077](../../agents/web_agent.py#L77) | 77 | `"    \"invalid_url_or_unsafe_target\","` | — |
| [SRC-1AE03B9EC3-L000078](../../agents/web_agent.py#L78) | 78 | `"    \"blocked_domain\","` | — |
| [SRC-1AE03B9EC3-L000079](../../agents/web_agent.py#L79) | 79 | `"    \"relevance_below_threshold\","` | — |
| [SRC-1AE03B9EC3-L000080](../../agents/web_agent.py#L80) | 80 | `")"` | — |
| [SRC-1AE03B9EC3-L000081](../../agents/web_agent.py#L81) | 81 | `""` | — |
| [SRC-1AE03B9EC3-L000082](../../agents/web_agent.py#L82) | 82 | `""` | — |
| [SRC-1AE03B9EC3-L000083](../../agents/web_agent.py#L83) | 83 | `"_ARABIC_SEARCH_TRANSLATION = str.maketrans({"` | — |
| [SRC-1AE03B9EC3-L000084](../../agents/web_agent.py#L84) | 84 | `"    \"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ٱ\": \"ا\", \"ى\": \"ي\","` | — |
| [SRC-1AE03B9EC3-L000085](../../agents/web_agent.py#L85) | 85 | `"    \"ؤ\": \"و\", \"ئ\": \"ي\", \"ة\": \"ه\", \"ـ\": \"\","` | — |
| [SRC-1AE03B9EC3-L000086](../../agents/web_agent.py#L86) | 86 | `"})"` | — |
| [SRC-1AE03B9EC3-L000087](../../agents/web_agent.py#L87) | 87 | `"_ARABIC_DIACRITICS_RE = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-1AE03B9EC3-L000088](../../agents/web_agent.py#L88) | 88 | `"_SEARCH_STOPWORDS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000089](../../agents/web_agent.py#L89) | 89 | `"    \"ما\", \"ماذا\", \"من\", \"في\", \"على\", \"عن\", \"الى\", \"إلى\", \"و\", \"او\", \"أو\","` | — |
| [SRC-1AE03B9EC3-L000090](../../agents/web_agent.py#L90) | 90 | `"    \"هل\", \"هو\", \"هي\", \"هذا\", \"هذه\", \"ذلك\", \"تلك\", \"التي\", \"الذي\", \"مع\","` | — |
| [SRC-1AE03B9EC3-L000091](../../agents/web_agent.py#L91) | 91 | `"    \"بين\", \"كيف\", \"لماذا\", \"كم\", \"كان\", \"كانت\", \"يكون\", \"تكون\", \"لي\","` | — |
| [SRC-1AE03B9EC3-L000092](../../agents/web_agent.py#L92) | 92 | `"    \"the\", \"a\", \"an\", \"and\", \"or\", \"in\", \"on\", \"of\", \"to\", \"for\", \"with\","` | — |
| [SRC-1AE03B9EC3-L000093](../../agents/web_agent.py#L93) | 93 | `"    \"is\", \"are\", \"was\", \"were\", \"what\", \"which\", \"who\", \"how\", \"why\", \"when\","` | — |
| [SRC-1AE03B9EC3-L000094](../../agents/web_agent.py#L94) | 94 | `"    \"where\", \"compare\", \"comparison\", \"please\", \"show\", \"find\", \"latest\","` | — |
| [SRC-1AE03B9EC3-L000095](../../agents/web_agent.py#L95) | 95 | `"    \"news\", \"official\", \"sources\", \"source\", \"reports\", \"report\", \"analysis\","` | — |
| [SRC-1AE03B9EC3-L000096](../../agents/web_agent.py#L96) | 96 | `"    \"site\", \"com\", \"org\", \"net\", \"www\","` | — |
| [SRC-1AE03B9EC3-L000097](../../agents/web_agent.py#L97) | 97 | `"    # Arabic request/format words are not useful topic concepts for matching search snippets."` | — |
| [SRC-1AE03B9EC3-L000098](../../agents/web_agent.py#L98) | 98 | `"    \"اذكر\", \"مصدر\", \"مصادر\", \"موثوق\", \"موثوقة\", \"رابط\", \"روابط\", \"مباشر\","` | — |
| [SRC-1AE03B9EC3-L000099](../../agents/web_agent.py#L99) | 99 | `"    \"مباشرة\", \"اجب\", \"بالعربية\", \"العربية\", \"بايجاز\", \"بالايجاز\", \"ايجاز\","` | — |
| [SRC-1AE03B9EC3-L000100](../../agents/web_agent.py#L100) | 100 | `"    \"باختصار\", \"اختصار\", \"استخدم\", \"اعرض\", \"وضح\", \"حلل\", \"قارن\", \"متعددة\","` | — |
| [SRC-1AE03B9EC3-L000101](../../agents/web_agent.py#L101) | 101 | `"    \"اهم\", \"الحقائق\", \"حقائق\", \"استنتاج\", \"استنتاجات\", \"الاستنتاجات\","` | — |
| [SRC-1AE03B9EC3-L000102](../../agents/web_agent.py#L102) | 102 | `"    \"تواريخ\", \"تاريخ\", \"الاخبار\", \"اخبار\", \"المصادر\", \"معلومات\", \"قديمة\","` | — |
| [SRC-1AE03B9EC3-L000103](../../agents/web_agent.py#L103) | 103 | `"    \"قديمه\", \"جديدة\", \"جديده\", \"خلال\", \"الايام\", \"ايام\", \"السبعة\", \"سبعة\","` | — |
| [SRC-1AE03B9EC3-L000104](../../agents/web_agent.py#L104) | 104 | `"    \"الماضية\", \"ماضية\", \"الاسبوع\", \"حاليا\", \"الان\", \"احدث\", \"ولا\","` | — |
| [SRC-1AE03B9EC3-L000105](../../agents/web_agent.py#L105) | 105 | `"    \"تعرض\", \"باعتبارها\","` | — |
| [SRC-1AE03B9EC3-L000106](../../agents/web_agent.py#L106) | 106 | `"})"` | — |
| [SRC-1AE03B9EC3-L000107](../../agents/web_agent.py#L107) | 107 | `"# Search-expansion modifiers are useful after a real topic, but must not stand in"` | — |
| [SRC-1AE03B9EC3-L000108](../../agents/web_agent.py#L108) | 108 | `"# for a topic if a future planner/expansion path loses its subject."` | — |
| [SRC-1AE03B9EC3-L000109](../../agents/web_agent.py#L109) | 109 | `"_GENERIC_QUERY_MODIFIER_TOKENS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000110](../../agents/web_agent.py#L110) | 110 | `"    \"risk\", \"risks\", \"limitation\", \"limitations\", \"alternative\", \"alternatives\","` | — |
| [SRC-1AE03B9EC3-L000111](../../agents/web_agent.py#L111) | 111 | `"    \"recent\", \"data\", \"review\", \"reviews\", \"comparison\", \"compare\", \"official\","` | — |
| [SRC-1AE03B9EC3-L000112](../../agents/web_agent.py#L112) | 112 | `"    \"primary\", \"source\", \"sources\", \"evidence\", \"report\", \"reports\", \"case\", \"cases\","` | — |
| [SRC-1AE03B9EC3-L000113](../../agents/web_agent.py#L113) | 113 | `"    \"study\", \"studies\", \"analysis\", \"latest\", \"news\", \"update\", \"updates\","` | — |
| [SRC-1AE03B9EC3-L000114](../../agents/web_agent.py#L114) | 114 | `"    \"announcement\", \"announcements\", \"comprehensive\", \"research\", \"statistic\","` | — |
| [SRC-1AE03B9EC3-L000115](../../agents/web_agent.py#L115) | 115 | `"    \"statistics\", \"trend\", \"trends\","` | — |
| [SRC-1AE03B9EC3-L000116](../../agents/web_agent.py#L116) | 116 | `"})"` | — |
| [SRC-1AE03B9EC3-L000117](../../agents/web_agent.py#L117) | 117 | `"_SEARCH_SYNONYMS = {"` | — |
| [SRC-1AE03B9EC3-L000118](../../agents/web_agent.py#L118) | 118 | `"    \"استراليا\": {\"australia\"}, \"عاصمة\": {\"capital\"}, \"مصر\": {\"egypt\"},"` | — |
| [SRC-1AE03B9EC3-L000119](../../agents/web_agent.py#L119) | 119 | `"    \"المصري\": {\"egyptian\", \"egypt\"}, \"مركزي\": {\"central\"},"` | — |
| [SRC-1AE03B9EC3-L000120](../../agents/web_agent.py#L120) | 120 | `"    \"المركزي\": {\"central\"}, \"بنك\": {\"bank\"}, \"البنك\": {\"bank\"},"` | — |
| [SRC-1AE03B9EC3-L000121](../../agents/web_agent.py#L121) | 121 | `"    \"قرار\": {\"decision\"}, \"قرارات\": {\"decision\", \"decisions\"},"` | — |
| [SRC-1AE03B9EC3-L000122](../../agents/web_agent.py#L122) | 122 | `"    \"سعر\": {\"price\"}, \"اسعار\": {\"prices\"}, \"استضافة\": {\"hosting\"},"` | — |
| [SRC-1AE03B9EC3-L000123](../../agents/web_agent.py#L123) | 123 | `"    \"شركة\": {\"company\"}, \"شركه\": {\"company\"}, \"ناشئة\": {\"startup\"},"` | — |
| [SRC-1AE03B9EC3-L000124](../../agents/web_agent.py#L124) | 124 | `"    \"صعيد\": {\"upper\"}, \"مقارنة\": {\"compare\", \"comparison\"},"` | — |
| [SRC-1AE03B9EC3-L000125](../../agents/web_agent.py#L125) | 125 | `"    \"تقنية\": {\"technology\"}, \"تقنيات\": {\"technology\"},"` | — |
| [SRC-1AE03B9EC3-L000126](../../agents/web_agent.py#L126) | 126 | `"    \"ميكروسوفت\": {\"microsoft\"}, \"مايكروسوفت\": {\"microsoft\"},"` | — |
| [SRC-1AE03B9EC3-L000127](../../agents/web_agent.py#L127) | 127 | `"    \"microsoft\": {\"ميكروسوفت\", \"مايكروسوفت\"},"` | — |
| [SRC-1AE03B9EC3-L000128](../../agents/web_agent.py#L128) | 128 | `"    \"جمهورية\": {\"republic\"}, \"republic\": {\"جمهورية\"},"` | — |
| [SRC-1AE03B9EC3-L000129](../../agents/web_agent.py#L129) | 129 | `"    \"الرقمية\": {\"digital\"}, \"رقمية\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000130](../../agents/web_agent.py#L130) | 130 | `"    \"الرقميه\": {\"digital\"}, \"رقميه\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000131](../../agents/web_agent.py#L131) | 131 | `"    \"موقع\": {\"website\", \"portal\"}, \"مواقع\": {\"websites\", \"portals\"},"` | — |
| [SRC-1AE03B9EC3-L000132](../../agents/web_agent.py#L132) | 132 | `"    \"التجمع\": {\"settlement\"}, \"تجمع\": {\"settlement\"},"` | — |
| [SRC-1AE03B9EC3-L000133](../../agents/web_agent.py#L133) | 133 | `"    \"الخامس\": {\"fifth\", \"5th\"}, \"خامس\": {\"fifth\", \"5th\"},"` | — |
| [SRC-1AE03B9EC3-L000134](../../agents/web_agent.py#L134) | 134 | `"    \"شقة\": {\"apartment\", \"flat\"}, \"شقق\": {\"apartments\", \"flats\"},"` | — |
| [SRC-1AE03B9EC3-L000135](../../agents/web_agent.py#L135) | 135 | `"    \"عميل\": {\"customer\", \"buyer\"}, \"عملاء\": {\"customers\", \"buyers\"},"` | — |
| [SRC-1AE03B9EC3-L000136](../../agents/web_agent.py#L136) | 136 | `"    \"شراء\": {\"buy\", \"purchase\"}, \"مشتري\": {\"buyer\"},"` | — |
| [SRC-1AE03B9EC3-L000137](../../agents/web_agent.py#L137) | 137 | `"    # Small, explicit Arabic-English topic vocabulary; this helps Arabic prompts"` | — |
| [SRC-1AE03B9EC3-L000138](../../agents/web_agent.py#L138) | 138 | `"    # match English-indexed results without relaxing URL or destination safety."` | — |
| [SRC-1AE03B9EC3-L000139](../../agents/web_agent.py#L139) | 139 | `"    \"سيارة\": {\"car\", \"vehicle\"}, \"السيارة\": {\"car\", \"vehicle\"},"` | — |
| [SRC-1AE03B9EC3-L000140](../../agents/web_agent.py#L140) | 140 | `"    \"سيارات\": {\"cars\", \"vehicles\"}, \"السيارات\": {\"cars\", \"vehicles\"},"` | — |
| [SRC-1AE03B9EC3-L000141](../../agents/web_agent.py#L141) | 141 | `"    \"كهربائي\": {\"electric\"}, \"كهربائية\": {\"electric\"},"` | — |
| [SRC-1AE03B9EC3-L000142](../../agents/web_agent.py#L142) | 142 | `"    \"الكهربائي\": {\"electric\"}, \"الكهربائية\": {\"electric\"},"` | — |
| [SRC-1AE03B9EC3-L000143](../../agents/web_agent.py#L143) | 143 | `"    \"شحن\": {\"charging\", \"charge\"}, \"الشحن\": {\"charging\", \"charge\"},"` | — |
| [SRC-1AE03B9EC3-L000144](../../agents/web_agent.py#L144) | 144 | `"    \"شاحن\": {\"charger\"}, \"بطارية\": {\"battery\"}, \"بطاريات\": {\"batteries\"},"` | — |
| [SRC-1AE03B9EC3-L000145](../../agents/web_agent.py#L145) | 145 | `"    \"تكلفة\": {\"cost\", \"costs\"}, \"التكلفة\": {\"cost\", \"costs\"},"` | — |
| [SRC-1AE03B9EC3-L000146](../../agents/web_agent.py#L146) | 146 | `"    \"البنية\": {\"infrastructure\"}, \"التحتية\": {\"infrastructure\"},"` | — |
| [SRC-1AE03B9EC3-L000147](../../agents/web_agent.py#L147) | 147 | `"    \"تحدي\": {\"challenge\"}, \"تحديات\": {\"challenges\"}, \"التحديات\": {\"challenges\"},"` | — |
| [SRC-1AE03B9EC3-L000148](../../agents/web_agent.py#L148) | 148 | `"    \"وكيل\": {\"agent\"}, \"الوكيل\": {\"agent\"},"` | — |
| [SRC-1AE03B9EC3-L000149](../../agents/web_agent.py#L149) | 149 | `"    \"وكلاء\": {\"agents\"}, \"الوكلاء\": {\"agents\"},"` | — |
| [SRC-1AE03B9EC3-L000150](../../agents/web_agent.py#L150) | 150 | `"    # Bilingual vocabulary for AI use-case searches. Keep the relevance floor"` | — |
| [SRC-1AE03B9EC3-L000151](../../agents/web_agent.py#L151) | 151 | `"    # unchanged; expand only concepts that commonly appear in Arabic news titles."` | — |
| [SRC-1AE03B9EC3-L000152](../../agents/web_agent.py#L152) | 152 | `"    \"استخدام\": {\"use\", \"usage\", \"application\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000153](../../agents/web_agent.py#L153) | 153 | `"    \"استخدامات\": {\"use\", \"usage\", \"application\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000154](../../agents/web_agent.py#L154) | 154 | `"    \"استعمال\": {\"use\", \"usage\", \"application\"},"` | — |
| [SRC-1AE03B9EC3-L000155](../../agents/web_agent.py#L155) | 155 | `"    \"استعمالات\": {\"use\", \"usage\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000156](../../agents/web_agent.py#L156) | 156 | `"    \"حالة\": {\"case\"}, \"حالات\": {\"cases\", \"case\"},"` | — |
| [SRC-1AE03B9EC3-L000157](../../agents/web_agent.py#L157) | 157 | `"    \"اعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000158](../../agents/web_agent.py#L158) | 158 | `"    \"الاعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000159](../../agents/web_agent.py#L159) | 159 | `"    \"للاعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000160](../../agents/web_agent.py#L160) | 160 | `"    \"شركات\": {\"company\", \"companies\", \"business\", \"businesses\"},"` | — |
| [SRC-1AE03B9EC3-L000161](../../agents/web_agent.py#L161) | 161 | `"    \"الشركات\": {\"company\", \"companies\", \"business\", \"businesses\"},"` | — |
| [SRC-1AE03B9EC3-L000162](../../agents/web_agent.py#L162) | 162 | `"    \"صغير\": {\"small\"}, \"صغيرة\": {\"small\"}, \"الصغير\": {\"small\"}, \"الصغيرة\": {\"small\"},"` | — |
| [SRC-1AE03B9EC3-L000163](../../agents/web_agent.py#L163) | 163 | `"    \"ذكاء\": {\"intelligence\", \"ai\"}, \"الذكاء\": {\"intelligence\", \"ai\"},"` | — |
| [SRC-1AE03B9EC3-L000164](../../agents/web_agent.py#L164) | 164 | `"    \"اصطناعي\": {\"artificial\", \"ai\"}, \"الاصطناعي\": {\"artificial\", \"ai\"},"` | — |
| [SRC-1AE03B9EC3-L000165](../../agents/web_agent.py#L165) | 165 | `"    \"تطور\": {\"development\", \"advance\"}, \"تطورات\": {\"developments\", \"advances\", \"updates\", \"latest\"},"` | — |
| [SRC-1AE03B9EC3-L000166](../../agents/web_agent.py#L166) | 166 | `"    \"التطورات\": {\"developments\", \"advances\", \"updates\", \"latest\"},"` | — |
| [SRC-1AE03B9EC3-L000167](../../agents/web_agent.py#L167) | 167 | `"    \"اراء\": {\"opinions\", \"views\"}, \"تجربة\": {\"experience\"}, \"تجارب\": {\"experiences\", \"reviews\"},"` | — |
| [SRC-1AE03B9EC3-L000168](../../agents/web_agent.py#L168) | 168 | `"    \"مستخدم\": {\"user\"}, \"المستخدم\": {\"user\"}, \"مستخدمين\": {\"users\"},"` | — |
| [SRC-1AE03B9EC3-L000169](../../agents/web_agent.py#L169) | 169 | `"    \"المستخدمين\": {\"users\"}, \"مالكون\": {\"owners\"}, \"المالكون\": {\"owners\"},"` | — |
| [SRC-1AE03B9EC3-L000170](../../agents/web_agent.py#L170) | 170 | `"}"` | — |
| [SRC-1AE03B9EC3-L000171](../../agents/web_agent.py#L171) | 171 | `"_CALENDAR_MONTHS = ("` | — |
| [SRC-1AE03B9EC3-L000172](../../agents/web_agent.py#L172) | 172 | `"    \"يناير\", \"فبراير\", \"مارس\", \"ابريل\", \"أبريل\", \"مايو\", \"يونيو\","` | — |
| [SRC-1AE03B9EC3-L000173](../../agents/web_agent.py#L173) | 173 | `"    \"يوليو\", \"اغسطس\", \"أغسطس\", \"سبتمبر\", \"اكتوبر\", \"أكتوبر\","` | — |
| [SRC-1AE03B9EC3-L000174](../../agents/web_agent.py#L174) | 174 | `"    \"نوفمبر\", \"ديسمبر\", \"january\", \"february\", \"march\", \"april\","` | — |
| [SRC-1AE03B9EC3-L000175](../../agents/web_agent.py#L175) | 175 | `"    \"may\", \"june\", \"july\", \"august\", \"september\", \"october\","` | — |
| [SRC-1AE03B9EC3-L000176](../../agents/web_agent.py#L176) | 176 | `"    \"november\", \"december\","` | — |
| [SRC-1AE03B9EC3-L000177](../../agents/web_agent.py#L177) | 177 | `")"` | — |
| [SRC-1AE03B9EC3-L000178](../../agents/web_agent.py#L178) | 178 | `"_BLOCKED_SOURCE_DOMAINS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000179](../../agents/web_agent.py#L179) | 179 | `"    \"translate.google.com\", \"translate.googleusercontent.com\","` | — |
| [SRC-1AE03B9EC3-L000180](../../agents/web_agent.py#L180) | 180 | `"})"` | — |
| [SRC-1AE03B9EC3-L000181](../../agents/web_agent.py#L181) | 181 | `""` | — |
| [SRC-1AE03B9EC3-L000182](../../agents/web_agent.py#L182) | 182 | `""` | — |
| [SRC-1AE03B9EC3-L000183](../../agents/web_agent.py#L183) | 183 | `"def _normalize_search_query(value: str) -> str:"` | — |
