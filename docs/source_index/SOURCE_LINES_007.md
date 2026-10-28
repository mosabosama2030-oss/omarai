# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **007**
- سجلات الأسطر: **800**
- النطاق: SRC-686F71AA50-L001124 إلى SRC-1AE03B9EC3-L000664
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-686F71AA50 — [agents/task_understanding.py](../../agents/task_understanding.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-686F71AA50-L001124](../../agents/task_understanding.py#L1124) | 1124 | `"    unavailable = {"` | — |
| [SRC-686F71AA50-L001125](../../agents/task_understanding.py#L1125) | 1125 | `"        \"schema\": \"omarai.task_spec.v1\","` | — |
| [SRC-686F71AA50-L001126](../../agents/task_understanding.py#L1126) | 1126 | `"        \"status\": \"not_available\","` | — |
| [SRC-686F71AA50-L001127](../../agents/task_understanding.py#L1127) | 1127 | `"        \"claim\": \"no validated task specification supplied\","` | — |
| [SRC-686F71AA50-L001128](../../agents/task_understanding.py#L1128) | 1128 | `"    }"` | — |
| [SRC-686F71AA50-L001129](../../agents/task_understanding.py#L1129) | 1129 | `"    if not isinstance(value, dict) or value.get(\"schema\") != \"omarai.task_spec.v1\":"` | — |
| [SRC-686F71AA50-L001130](../../agents/task_understanding.py#L1130) | 1130 | `"        return unavailable"` | — |
| [SRC-686F71AA50-L001131](../../agents/task_understanding.py#L1131) | 1131 | `""` | — |
| [SRC-686F71AA50-L001132](../../agents/task_understanding.py#L1132) | 1132 | `"    def clean_text(item: Any, limit: int = 160) -> str:"` | — |
| [SRC-686F71AA50-L001133](../../agents/task_understanding.py#L1133) | 1133 | `"        if not isinstance(item, str):"` | — |
| [SRC-686F71AA50-L001134](../../agents/task_understanding.py#L1134) | 1134 | `"            return \"\""` | — |
| [SRC-686F71AA50-L001135](../../agents/task_understanding.py#L1135) | 1135 | `"        return _SPACE.sub(\" \", unicodedata.normalize(\"NFKC\", item).replace(\"\\x00\", \" \")).strip()[:limit]"` | — |
| [SRC-686F71AA50-L001136](../../agents/task_understanding.py#L1136) | 1136 | `""` | — |
| [SRC-686F71AA50-L001137](../../agents/task_understanding.py#L1137) | 1137 | `"    def clean_list(item: Any, *, items: int = 16, chars: int = 160) -> list[str]:"` | — |
| [SRC-686F71AA50-L001138](../../agents/task_understanding.py#L1138) | 1138 | `"        if not isinstance(item, list):"` | — |
| [SRC-686F71AA50-L001139](../../agents/task_understanding.py#L1139) | 1139 | `"            return []"` | — |
| [SRC-686F71AA50-L001140](../../agents/task_understanding.py#L1140) | 1140 | `"        result: list[str] = []"` | — |
| [SRC-686F71AA50-L001141](../../agents/task_understanding.py#L1141) | 1141 | `"        seen: set[str] = set()"` | — |
| [SRC-686F71AA50-L001142](../../agents/task_understanding.py#L1142) | 1142 | `"        for raw_item in item[:items * 2]:"` | — |
| [SRC-686F71AA50-L001143](../../agents/task_understanding.py#L1143) | 1143 | `"            cleaned = clean_text(raw_item, chars)"` | — |
| [SRC-686F71AA50-L001144](../../agents/task_understanding.py#L1144) | 1144 | `"            key = cleaned.casefold()"` | — |
| [SRC-686F71AA50-L001145](../../agents/task_understanding.py#L1145) | 1145 | `"            if cleaned and key not in seen:"` | — |
| [SRC-686F71AA50-L001146](../../agents/task_understanding.py#L1146) | 1146 | `"                result.append(cleaned)"` | — |
| [SRC-686F71AA50-L001147](../../agents/task_understanding.py#L1147) | 1147 | `"                seen.add(key)"` | — |
| [SRC-686F71AA50-L001148](../../agents/task_understanding.py#L1148) | 1148 | `"            if len(result) >= items:"` | — |
| [SRC-686F71AA50-L001149](../../agents/task_understanding.py#L1149) | 1149 | `"                break"` | — |
| [SRC-686F71AA50-L001150](../../agents/task_understanding.py#L1150) | 1150 | `"        return result"` | — |
| [SRC-686F71AA50-L001151](../../agents/task_understanding.py#L1151) | 1151 | `""` | — |
| [SRC-686F71AA50-L001152](../../agents/task_understanding.py#L1152) | 1152 | `"    raw_constraints = value.get(\"constraints\")"` | — |
| [SRC-686F71AA50-L001153](../../agents/task_understanding.py#L1153) | 1153 | `"    raw_constraints = raw_constraints if isinstance(raw_constraints, dict) else {}"` | — |
| [SRC-686F71AA50-L001154](../../agents/task_understanding.py#L1154) | 1154 | `"    list_constraint_keys = ("` | — |
| [SRC-686F71AA50-L001155](../../agents/task_understanding.py#L1155) | 1155 | `"        \"explicit_locations\", \"explicit_years\", \"explicit_dates\","` | — |
| [SRC-686F71AA50-L001156](../../agents/task_understanding.py#L1156) | 1156 | `"        \"explicit_budgets\", \"explicit_urls\", \"explicit_aspects\", \"source_policies\","` | — |
| [SRC-686F71AA50-L001157](../../agents/task_understanding.py#L1157) | 1157 | `"    )"` | — |
| [SRC-686F71AA50-L001158](../../agents/task_understanding.py#L1158) | 1158 | `"    constraints: dict[str, Any] = {"` | — |
| [SRC-686F71AA50-L001159](../../agents/task_understanding.py#L1159) | 1159 | `"        key: clean_list(raw_constraints.get(key), items=8 if key == \"explicit_aspects\" else 5, chars=300 if key == \"explicit_urls\" else 120)"` | — |
| [SRC-686F71AA50-L001160](../../agents/task_understanding.py#L1160) | 1160 | `"        for key in list_constraint_keys"` | — |
| [SRC-686F71AA50-L001161](../../agents/task_understanding.py#L1161) | 1161 | `"    }"` | — |
| [SRC-686F71AA50-L001162](../../agents/task_understanding.py#L1162) | 1162 | `"    for key in ("` | — |
| [SRC-686F71AA50-L001163](../../agents/task_understanding.py#L1163) | 1163 | `"        \"inline_text_supplied_for_summary\","` | — |
| [SRC-686F71AA50-L001164](../../agents/task_understanding.py#L1164) | 1164 | `"        \"time_sensitive_request\","` | — |
| [SRC-686F71AA50-L001165](../../agents/task_understanding.py#L1165) | 1165 | `"        \"official_site_required\","` | — |
| [SRC-686F71AA50-L001166](../../agents/task_understanding.py#L1166) | 1166 | `"        \"official_destination_required\","` | — |
| [SRC-686F71AA50-L001167](../../agents/task_understanding.py#L1167) | 1167 | `"        \"social_evidence_requested\","` | — |
| [SRC-686F71AA50-L001168](../../agents/task_understanding.py#L1168) | 1168 | `"    ):"` | — |
| [SRC-686F71AA50-L001169](../../agents/task_understanding.py#L1169) | 1169 | `"        constraints[key] = raw_constraints.get(key) is True"` | — |
| [SRC-686F71AA50-L001170](../../agents/task_understanding.py#L1170) | 1170 | `"    language_profile = raw_constraints.get(\"language_profile\")"` | — |
| [SRC-686F71AA50-L001171](../../agents/task_understanding.py#L1171) | 1171 | `"    constraints[\"language_profile\"] = ("` | — |
| [SRC-686F71AA50-L001172](../../agents/task_understanding.py#L1172) | 1172 | `"        language_profile if language_profile in {\"ar\", \"en\", \"mixed\", \"und\"} else \"und\""` | — |
| [SRC-686F71AA50-L001173](../../agents/task_understanding.py#L1173) | 1173 | `"    )"` | — |
| [SRC-686F71AA50-L001174](../../agents/task_understanding.py#L1174) | 1174 | `"    constraints[\"source_policy\"] = clean_text(raw_constraints.get(\"source_policy\"), 80) or \"unassessed\""` | — |
| [SRC-686F71AA50-L001175](../../agents/task_understanding.py#L1175) | 1175 | `""` | — |
| [SRC-686F71AA50-L001176](../../agents/task_understanding.py#L1176) | 1176 | `"    raw_preferences = value.get(\"output_preferences\")"` | — |
| [SRC-686F71AA50-L001177](../../agents/task_understanding.py#L1177) | 1177 | `"    raw_preferences = raw_preferences if isinstance(raw_preferences, dict) else {}"` | — |
| [SRC-686F71AA50-L001178](../../agents/task_understanding.py#L1178) | 1178 | `"    preference_keys = ("` | — |
| [SRC-686F71AA50-L001179](../../agents/task_understanding.py#L1179) | 1179 | `"        \"concise\", \"detailed\", \"examples_requested\", \"table_requested\","` | — |
| [SRC-686F71AA50-L001180](../../agents/task_understanding.py#L1180) | 1180 | `"        \"bullets_or_checklist_requested\", \"beginner_friendly_requested\","` | — |
| [SRC-686F71AA50-L001181](../../agents/task_understanding.py#L1181) | 1181 | `"        \"citations_requested\", \"links_requested\", \"json_requested\","` | — |
| [SRC-686F71AA50-L001182](../../agents/task_understanding.py#L1182) | 1182 | `"    )"` | — |
| [SRC-686F71AA50-L001183](../../agents/task_understanding.py#L1183) | 1183 | `"    output_preferences = {key: raw_preferences.get(key) is True for key in preference_keys}"` | — |
| [SRC-686F71AA50-L001184](../../agents/task_understanding.py#L1184) | 1184 | `""` | — |
| [SRC-686F71AA50-L001185](../../agents/task_understanding.py#L1185) | 1185 | `"    raw_context = value.get(\"context_resolution\")"` | — |
| [SRC-686F71AA50-L001186](../../agents/task_understanding.py#L1186) | 1186 | `"    raw_context = raw_context if isinstance(raw_context, dict) else {}"` | — |
| [SRC-686F71AA50-L001187](../../agents/task_understanding.py#L1187) | 1187 | `"    raw_slots = raw_context.get(\"slots\")"` | — |
| [SRC-686F71AA50-L001188](../../agents/task_understanding.py#L1188) | 1188 | `"    slots: dict[str, str] = {}"` | — |
| [SRC-686F71AA50-L001189](../../agents/task_understanding.py#L1189) | 1189 | `"    if isinstance(raw_slots, dict):"` | — |
| [SRC-686F71AA50-L001190](../../agents/task_understanding.py#L1190) | 1190 | `"        for raw_key, raw_value in list(raw_slots.items())[:16]:"` | — |
| [SRC-686F71AA50-L001191](../../agents/task_understanding.py#L1191) | 1191 | `"            key = clean_text(raw_key, 40)"` | — |
| [SRC-686F71AA50-L001192](../../agents/task_understanding.py#L1192) | 1192 | `"            item = clean_text(raw_value, 180)"` | — |
| [SRC-686F71AA50-L001193](../../agents/task_understanding.py#L1193) | 1193 | `"            if key and item:"` | — |
| [SRC-686F71AA50-L001194](../../agents/task_understanding.py#L1194) | 1194 | `"                slots[key] = item"` | — |
| [SRC-686F71AA50-L001195](../../agents/task_understanding.py#L1195) | 1195 | `"    context_resolution = {"` | — |
| [SRC-686F71AA50-L001196](../../agents/task_understanding.py#L1196) | 1196 | `"        \"method\": clean_text(raw_context.get(\"method\"), 80) or \"not_provided\","` | — |
| [SRC-686F71AA50-L001197](../../agents/task_understanding.py#L1197) | 1197 | `"        \"resolved_question\": clean_text(raw_context.get(\"resolved_question\"), MAX_TASK_CHARS),"` | — |
| [SRC-686F71AA50-L001198](../../agents/task_understanding.py#L1198) | 1198 | `"        \"topic\": clean_text(raw_context.get(\"topic\"), 180),"` | — |
| [SRC-686F71AA50-L001199](../../agents/task_understanding.py#L1199) | 1199 | `"        \"entities\": clean_list(raw_context.get(\"entities\"), items=8, chars=120),"` | — |
| [SRC-686F71AA50-L001200](../../agents/task_understanding.py#L1200) | 1200 | `"        \"slots\": slots,"` | — |
| [SRC-686F71AA50-L001201](../../agents/task_understanding.py#L1201) | 1201 | `"        \"changed_slots\": clean_list(raw_context.get(\"changed_slots\"), items=8, chars=40),"` | — |
| [SRC-686F71AA50-L001202](../../agents/task_understanding.py#L1202) | 1202 | `"        \"is_follow_up\": raw_context.get(\"is_follow_up\") is True,"` | — |
| [SRC-686F71AA50-L001203](../../agents/task_understanding.py#L1203) | 1203 | `"        \"topic_shift\": raw_context.get(\"topic_shift\") is True,"` | — |
| [SRC-686F71AA50-L001204](../../agents/task_understanding.py#L1204) | 1204 | `"        \"resolution_basis\": clean_text(raw_context.get(\"resolution_basis\"), 80) or \"unassessed\","` | — |
| [SRC-686F71AA50-L001205](../../agents/task_understanding.py#L1205) | 1205 | `"        \"confidence_band\": ("` | — |
| [SRC-686F71AA50-L001206](../../agents/task_understanding.py#L1206) | 1206 | `"            raw_context.get(\"confidence_band\")"` | — |
| [SRC-686F71AA50-L001207](../../agents/task_understanding.py#L1207) | 1207 | `"            if raw_context.get(\"confidence_band\") in {\"low\", \"medium\", \"high\", \"unassessed\"}"` | — |
| [SRC-686F71AA50-L001208](../../agents/task_understanding.py#L1208) | 1208 | `"            else \"unassessed\""` | — |
| [SRC-686F71AA50-L001209](../../agents/task_understanding.py#L1209) | 1209 | `"        ),"` | — |
| [SRC-686F71AA50-L001210](../../agents/task_understanding.py#L1210) | 1210 | `"        \"needs_clarification\": raw_context.get(\"needs_clarification\") is True,"` | — |
| [SRC-686F71AA50-L001211](../../agents/task_understanding.py#L1211) | 1211 | `"        \"unresolved_references\": clean_list(raw_context.get(\"unresolved_references\"), items=8, chars=100),"` | — |
| [SRC-686F71AA50-L001212](../../agents/task_understanding.py#L1212) | 1212 | `"    }"` | — |
| [SRC-686F71AA50-L001213](../../agents/task_understanding.py#L1213) | 1213 | `""` | — |
| [SRC-686F71AA50-L001214](../../agents/task_understanding.py#L1214) | 1214 | `"    raw_hypotheses = value.get(\"hypothesis_interpretations\")"` | — |
| [SRC-686F71AA50-L001215](../../agents/task_understanding.py#L1215) | 1215 | `"    hypotheses: list[dict[str, Any]] = []"` | — |
| [SRC-686F71AA50-L001216](../../agents/task_understanding.py#L1216) | 1216 | `"    if isinstance(raw_hypotheses, list):"` | — |
| [SRC-686F71AA50-L001217](../../agents/task_understanding.py#L1217) | 1217 | `"        for item in raw_hypotheses[:8]:"` | — |
| [SRC-686F71AA50-L001218](../../agents/task_understanding.py#L1218) | 1218 | `"            if not isinstance(item, dict):"` | — |
| [SRC-686F71AA50-L001219](../../agents/task_understanding.py#L1219) | 1219 | `"                continue"` | — |
| [SRC-686F71AA50-L001220](../../agents/task_understanding.py#L1220) | 1220 | `"            count = item.get(\"matched_signal_count\")"` | — |
| [SRC-686F71AA50-L001221](../../agents/task_understanding.py#L1221) | 1221 | `"            hypotheses.append({"` | — |
| [SRC-686F71AA50-L001222](../../agents/task_understanding.py#L1222) | 1222 | `"                \"family\": clean_text(item.get(\"family\"), 80),"` | — |
| [SRC-686F71AA50-L001223](../../agents/task_understanding.py#L1223) | 1223 | `"                \"matched_signal_count\": max(0, min(32, count)) if isinstance(count, int) else 0,"` | — |
| [SRC-686F71AA50-L001224](../../agents/task_understanding.py#L1224) | 1224 | `"                \"signals\": clean_list(item.get(\"signals\"), items=4, chars=100),"` | — |
| [SRC-686F71AA50-L001225](../../agents/task_understanding.py#L1225) | 1225 | `"                \"status\": clean_text(item.get(\"status\"), 60) or \"unassessed\","` | — |
| [SRC-686F71AA50-L001226](../../agents/task_understanding.py#L1226) | 1226 | `"                \"selected\": item.get(\"selected\") is True,"` | — |
| [SRC-686F71AA50-L001227](../../agents/task_understanding.py#L1227) | 1227 | `"            })"` | — |
| [SRC-686F71AA50-L001228](../../agents/task_understanding.py#L1228) | 1228 | `""` | — |
| [SRC-686F71AA50-L001229](../../agents/task_understanding.py#L1229) | 1229 | `"    spec = {"` | — |
| [SRC-686F71AA50-L001230](../../agents/task_understanding.py#L1230) | 1230 | `"        \"schema\": \"omarai.task_spec.v1\","` | — |
| [SRC-686F71AA50-L001231](../../agents/task_understanding.py#L1231) | 1231 | `"        \"task_family\": clean_text(value.get(\"task_family\"), 80) or \"general_question\","` | — |
| [SRC-686F71AA50-L001232](../../agents/task_understanding.py#L1232) | 1232 | `"        \"mode\": clean_text(value.get(\"mode\"), 20) or \"auto\","` | — |
| [SRC-686F71AA50-L001233](../../agents/task_understanding.py#L1233) | 1233 | `"        \"intent_route\": clean_text(value.get(\"intent_route\"), 40) or \"unassessed\","` | — |
| [SRC-686F71AA50-L001234](../../agents/task_understanding.py#L1234) | 1234 | `"        \"classification_method\": clean_text(value.get(\"classification_method\"), 100),"` | — |
| [SRC-686F71AA50-L001235](../../agents/task_understanding.py#L1235) | 1235 | `"        \"classification_is_probability\": False,"` | — |
| [SRC-686F71AA50-L001236](../../agents/task_understanding.py#L1236) | 1236 | `"        \"ambiguity_status\": clean_text(value.get(\"ambiguity_status\"), 80) or \"unassessed\","` | — |
| [SRC-686F71AA50-L001237](../../agents/task_understanding.py#L1237) | 1237 | `"        \"missing_required_inputs\": clean_list(value.get(\"missing_required_inputs\"), items=8, chars=100),"` | — |
| [SRC-686F71AA50-L001238](../../agents/task_understanding.py#L1238) | 1238 | `"        \"requires_clarification\": value.get(\"requires_clarification\") is True,"` | — |
| [SRC-686F71AA50-L001239](../../agents/task_understanding.py#L1239) | 1239 | `"        \"clarification_reason\": clean_text(value.get(\"clarification_reason\"), 80) or \"unassessed\","` | — |
| [SRC-686F71AA50-L001240](../../agents/task_understanding.py#L1240) | 1240 | `"        \"context_resolution\": context_resolution,"` | — |
| [SRC-686F71AA50-L001241](../../agents/task_understanding.py#L1241) | 1241 | `"        \"secondary_task_types\": clean_list(value.get(\"secondary_task_types\"), items=16, chars=80),"` | — |
| [SRC-686F71AA50-L001242](../../agents/task_understanding.py#L1242) | 1242 | `"        \"constraints\": constraints,"` | — |
| [SRC-686F71AA50-L001243](../../agents/task_understanding.py#L1243) | 1243 | `"        \"output_preferences\": output_preferences,"` | — |
| [SRC-686F71AA50-L001244](../../agents/task_understanding.py#L1244) | 1244 | `"        \"evidence_requirements\": clean_list(value.get(\"evidence_requirements\"), items=32, chars=180),"` | — |
| [SRC-686F71AA50-L001245](../../agents/task_understanding.py#L1245) | 1245 | `"        \"query_strategies\": clean_list(value.get(\"query_strategies\"), items=32, chars=100),"` | — |
| [SRC-686F71AA50-L001246](../../agents/task_understanding.py#L1246) | 1246 | `"        \"tool_requirements\": clean_list(value.get(\"tool_requirements\"), items=12, chars=100),"` | — |
| [SRC-686F71AA50-L001247](../../agents/task_understanding.py#L1247) | 1247 | `"        \"decision_checks\": clean_list(value.get(\"decision_checks\"), items=24, chars=120),"` | — |
| [SRC-686F71AA50-L001248](../../agents/task_understanding.py#L1248) | 1248 | `"        \"hypothesis_interpretations\": hypotheses,"` | — |
| [SRC-686F71AA50-L001249](../../agents/task_understanding.py#L1249) | 1249 | `"        \"limits\": {"` | — |
| [SRC-686F71AA50-L001250](../../agents/task_understanding.py#L1250) | 1250 | `"            \"max_question_chars\": MAX_TASK_CHARS,"` | — |
| [SRC-686F71AA50-L001251](../../agents/task_understanding.py#L1251) | 1251 | `"            \"max_aspects\": MAX_TASK_ASPECTS,"` | — |
| [SRC-686F71AA50-L001252](../../agents/task_understanding.py#L1252) | 1252 | `"            \"max_query_strategies\": MAX_STRATEGY_QUERIES,"` | — |
| [SRC-686F71AA50-L001253](../../agents/task_understanding.py#L1253) | 1253 | `"        },"` | — |
| [SRC-686F71AA50-L001254](../../agents/task_understanding.py#L1254) | 1254 | `"        \"claim\": \"task planning metadata only; not semantic certainty or factual verification\","` | — |
| [SRC-686F71AA50-L001255](../../agents/task_understanding.py#L1255) | 1255 | `"    }"` | — |
| [SRC-686F71AA50-L001256](../../agents/task_understanding.py#L1256) | 1256 | `"    for key in (\"planner_freshness\", \"planner_depth\"):"` | — |
| [SRC-686F71AA50-L001257](../../agents/task_understanding.py#L1257) | 1257 | `"        if key in value:"` | — |
| [SRC-686F71AA50-L001258](../../agents/task_understanding.py#L1258) | 1258 | `"            spec[key] = clean_text(value.get(key), 40) or \"unknown\""` | — |
| [SRC-686F71AA50-L001259](../../agents/task_understanding.py#L1259) | 1259 | `"    return spec"` | — |
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
| [SRC-1AE03B9EC3-L000051](../../agents/web_agent.py#L51) | 51 | `"from agents.task_understanding import build_query_strategy_matrix, build_task_spec"` | — |
| [SRC-1AE03B9EC3-L000052](../../agents/web_agent.py#L52) | 52 | `""` | — |
| [SRC-1AE03B9EC3-L000053](../../agents/web_agent.py#L53) | 53 | `"MAX_QUESTION_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000054](../../agents/web_agent.py#L54) | 54 | `"MAX_HISTORY_ITEMS = 8"` | — |
| [SRC-1AE03B9EC3-L000055](../../agents/web_agent.py#L55) | 55 | `"MAX_HISTORY_CHARS = 4000"` | — |
| [SRC-1AE03B9EC3-L000056](../../agents/web_agent.py#L56) | 56 | `"MAX_SEARCH_RESULTS = 18"` | — |
| [SRC-1AE03B9EC3-L000057](../../agents/web_agent.py#L57) | 57 | `"MAX_PROVIDER_RESULTS = 6"` | — |
| [SRC-1AE03B9EC3-L000058](../../agents/web_agent.py#L58) | 58 | `"MAX_FETCHED_PAGES = 8"` | — |
| [SRC-1AE03B9EC3-L000059](../../agents/web_agent.py#L59) | 59 | `"MAX_LLM_CITED_SOURCES = 12"` | — |
| [SRC-1AE03B9EC3-L000060](../../agents/web_agent.py#L60) | 60 | `"MAX_RESEARCH_WORKERS = 8"` | — |
| [SRC-1AE03B9EC3-L000061](../../agents/web_agent.py#L61) | 61 | `"MAX_PAGE_BYTES = 1_000_000"` | — |
| [SRC-1AE03B9EC3-L000062](../../agents/web_agent.py#L62) | 62 | `"MAX_PAGE_TEXT_CHARS = 12_000"` | — |
| [SRC-1AE03B9EC3-L000063](../../agents/web_agent.py#L63) | 63 | `"LLM_TIMEOUT_SECONDS = 35"` | — |
| [SRC-1AE03B9EC3-L000064](../../agents/web_agent.py#L64) | 64 | `""` | — |
| [SRC-1AE03B9EC3-L000065](../../agents/web_agent.py#L65) | 65 | `"# Only completed connector result-processing states positively confirm an attempt."` | — |
| [SRC-1AE03B9EC3-L000066](../../agents/web_agent.py#L66) | 66 | `"# A generic \"failed\" or timeout diagnostic may occur before a network request is sent."` | — |
| [SRC-1AE03B9EC3-L000067](../../agents/web_agent.py#L67) | 67 | `"_SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES = frozenset({\"ok\", \"no_results\", \"filtered_all\"})"` | — |
| [SRC-1AE03B9EC3-L000068](../../agents/web_agent.py#L68) | 68 | `"_RESEARCH_ERROR_OUTCOMES = frozenset({\"attempted_research_error\", \"unknown_after_research_error\"})"` | — |
| [SRC-1AE03B9EC3-L000069](../../agents/web_agent.py#L69) | 69 | `"_PROVIDER_REJECTION_REASONS = ("` | — |
| [SRC-1AE03B9EC3-L000070](../../agents/web_agent.py#L70) | 70 | `"    \"malformed_candidate\","` | — |
| [SRC-1AE03B9EC3-L000071](../../agents/web_agent.py#L71) | 71 | `"    \"invalid_url_or_unsafe_target\","` | — |
| [SRC-1AE03B9EC3-L000072](../../agents/web_agent.py#L72) | 72 | `"    \"blocked_domain\","` | — |
| [SRC-1AE03B9EC3-L000073](../../agents/web_agent.py#L73) | 73 | `"    \"relevance_below_threshold\","` | — |
| [SRC-1AE03B9EC3-L000074](../../agents/web_agent.py#L74) | 74 | `")"` | — |
| [SRC-1AE03B9EC3-L000075](../../agents/web_agent.py#L75) | 75 | `""` | — |
| [SRC-1AE03B9EC3-L000076](../../agents/web_agent.py#L76) | 76 | `""` | — |
| [SRC-1AE03B9EC3-L000077](../../agents/web_agent.py#L77) | 77 | `"_ARABIC_SEARCH_TRANSLATION = str.maketrans({"` | — |
| [SRC-1AE03B9EC3-L000078](../../agents/web_agent.py#L78) | 78 | `"    \"أ\": \"ا\", \"إ\": \"ا\", \"آ\": \"ا\", \"ٱ\": \"ا\", \"ى\": \"ي\","` | — |
| [SRC-1AE03B9EC3-L000079](../../agents/web_agent.py#L79) | 79 | `"    \"ؤ\": \"و\", \"ئ\": \"ي\", \"ة\": \"ه\", \"ـ\": \"\","` | — |
| [SRC-1AE03B9EC3-L000080](../../agents/web_agent.py#L80) | 80 | `"})"` | — |
| [SRC-1AE03B9EC3-L000081](../../agents/web_agent.py#L81) | 81 | `"_ARABIC_DIACRITICS_RE = re.compile(r\"[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED]\")"` | — |
| [SRC-1AE03B9EC3-L000082](../../agents/web_agent.py#L82) | 82 | `"_SEARCH_STOPWORDS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000083](../../agents/web_agent.py#L83) | 83 | `"    \"ما\", \"ماذا\", \"من\", \"في\", \"على\", \"عن\", \"الى\", \"إلى\", \"و\", \"او\", \"أو\","` | — |
| [SRC-1AE03B9EC3-L000084](../../agents/web_agent.py#L84) | 84 | `"    \"هل\", \"هو\", \"هي\", \"هذا\", \"هذه\", \"ذلك\", \"تلك\", \"التي\", \"الذي\", \"مع\","` | — |
| [SRC-1AE03B9EC3-L000085](../../agents/web_agent.py#L85) | 85 | `"    \"بين\", \"كيف\", \"لماذا\", \"كم\", \"كان\", \"كانت\", \"يكون\", \"تكون\", \"لي\","` | — |
| [SRC-1AE03B9EC3-L000086](../../agents/web_agent.py#L86) | 86 | `"    \"the\", \"a\", \"an\", \"and\", \"or\", \"in\", \"on\", \"of\", \"to\", \"for\", \"with\","` | — |
| [SRC-1AE03B9EC3-L000087](../../agents/web_agent.py#L87) | 87 | `"    \"is\", \"are\", \"was\", \"were\", \"what\", \"which\", \"who\", \"how\", \"why\", \"when\","` | — |
| [SRC-1AE03B9EC3-L000088](../../agents/web_agent.py#L88) | 88 | `"    \"where\", \"compare\", \"comparison\", \"please\", \"show\", \"find\", \"latest\","` | — |
| [SRC-1AE03B9EC3-L000089](../../agents/web_agent.py#L89) | 89 | `"    \"news\", \"official\", \"sources\", \"source\", \"reports\", \"report\", \"analysis\","` | — |
| [SRC-1AE03B9EC3-L000090](../../agents/web_agent.py#L90) | 90 | `"    \"site\", \"com\", \"org\", \"net\", \"www\","` | — |
| [SRC-1AE03B9EC3-L000091](../../agents/web_agent.py#L91) | 91 | `"    # Arabic request/format words are not useful topic concepts for matching search snippets."` | — |
| [SRC-1AE03B9EC3-L000092](../../agents/web_agent.py#L92) | 92 | `"    \"اذكر\", \"مصدر\", \"مصادر\", \"موثوق\", \"موثوقة\", \"رابط\", \"روابط\", \"مباشر\","` | — |
| [SRC-1AE03B9EC3-L000093](../../agents/web_agent.py#L93) | 93 | `"    \"مباشرة\", \"اجب\", \"بالعربية\", \"العربية\", \"بايجاز\", \"بالايجاز\", \"ايجاز\","` | — |
| [SRC-1AE03B9EC3-L000094](../../agents/web_agent.py#L94) | 94 | `"    \"باختصار\", \"اختصار\", \"استخدم\", \"اعرض\", \"وضح\", \"حلل\", \"قارن\", \"متعددة\","` | — |
| [SRC-1AE03B9EC3-L000095](../../agents/web_agent.py#L95) | 95 | `"    \"اهم\", \"الحقائق\", \"حقائق\", \"استنتاج\", \"استنتاجات\", \"الاستنتاجات\","` | — |
| [SRC-1AE03B9EC3-L000096](../../agents/web_agent.py#L96) | 96 | `"    \"تواريخ\", \"تاريخ\", \"الاخبار\", \"اخبار\", \"المصادر\", \"معلومات\", \"قديمة\","` | — |
| [SRC-1AE03B9EC3-L000097](../../agents/web_agent.py#L97) | 97 | `"    \"قديمه\", \"جديدة\", \"جديده\", \"خلال\", \"الايام\", \"ايام\", \"السبعة\", \"سبعة\","` | — |
| [SRC-1AE03B9EC3-L000098](../../agents/web_agent.py#L98) | 98 | `"    \"الماضية\", \"ماضية\", \"الاسبوع\", \"حاليا\", \"الان\", \"احدث\", \"ولا\","` | — |
| [SRC-1AE03B9EC3-L000099](../../agents/web_agent.py#L99) | 99 | `"    \"تعرض\", \"باعتبارها\","` | — |
| [SRC-1AE03B9EC3-L000100](../../agents/web_agent.py#L100) | 100 | `"})"` | — |
| [SRC-1AE03B9EC3-L000101](../../agents/web_agent.py#L101) | 101 | `"# Search-expansion modifiers are useful after a real topic, but must not stand in"` | — |
| [SRC-1AE03B9EC3-L000102](../../agents/web_agent.py#L102) | 102 | `"# for a topic if a future planner/expansion path loses its subject."` | — |
| [SRC-1AE03B9EC3-L000103](../../agents/web_agent.py#L103) | 103 | `"_GENERIC_QUERY_MODIFIER_TOKENS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000104](../../agents/web_agent.py#L104) | 104 | `"    \"risk\", \"risks\", \"limitation\", \"limitations\", \"alternative\", \"alternatives\","` | — |
| [SRC-1AE03B9EC3-L000105](../../agents/web_agent.py#L105) | 105 | `"    \"recent\", \"data\", \"review\", \"reviews\", \"comparison\", \"compare\", \"official\","` | — |
| [SRC-1AE03B9EC3-L000106](../../agents/web_agent.py#L106) | 106 | `"    \"primary\", \"source\", \"sources\", \"evidence\", \"report\", \"reports\", \"case\", \"cases\","` | — |
| [SRC-1AE03B9EC3-L000107](../../agents/web_agent.py#L107) | 107 | `"    \"study\", \"studies\", \"analysis\", \"latest\", \"news\", \"update\", \"updates\","` | — |
| [SRC-1AE03B9EC3-L000108](../../agents/web_agent.py#L108) | 108 | `"    \"announcement\", \"announcements\", \"comprehensive\", \"research\", \"statistic\","` | — |
| [SRC-1AE03B9EC3-L000109](../../agents/web_agent.py#L109) | 109 | `"    \"statistics\", \"trend\", \"trends\","` | — |
| [SRC-1AE03B9EC3-L000110](../../agents/web_agent.py#L110) | 110 | `"})"` | — |
| [SRC-1AE03B9EC3-L000111](../../agents/web_agent.py#L111) | 111 | `"_SEARCH_SYNONYMS = {"` | — |
| [SRC-1AE03B9EC3-L000112](../../agents/web_agent.py#L112) | 112 | `"    \"استراليا\": {\"australia\"}, \"عاصمة\": {\"capital\"}, \"مصر\": {\"egypt\"},"` | — |
| [SRC-1AE03B9EC3-L000113](../../agents/web_agent.py#L113) | 113 | `"    \"المصري\": {\"egyptian\", \"egypt\"}, \"مركزي\": {\"central\"},"` | — |
| [SRC-1AE03B9EC3-L000114](../../agents/web_agent.py#L114) | 114 | `"    \"المركزي\": {\"central\"}, \"بنك\": {\"bank\"}, \"البنك\": {\"bank\"},"` | — |
| [SRC-1AE03B9EC3-L000115](../../agents/web_agent.py#L115) | 115 | `"    \"قرار\": {\"decision\"}, \"قرارات\": {\"decision\", \"decisions\"},"` | — |
| [SRC-1AE03B9EC3-L000116](../../agents/web_agent.py#L116) | 116 | `"    \"سعر\": {\"price\"}, \"اسعار\": {\"prices\"}, \"استضافة\": {\"hosting\"},"` | — |
| [SRC-1AE03B9EC3-L000117](../../agents/web_agent.py#L117) | 117 | `"    \"شركة\": {\"company\"}, \"شركه\": {\"company\"}, \"ناشئة\": {\"startup\"},"` | — |
| [SRC-1AE03B9EC3-L000118](../../agents/web_agent.py#L118) | 118 | `"    \"صعيد\": {\"upper\"}, \"مقارنة\": {\"compare\", \"comparison\"},"` | — |
| [SRC-1AE03B9EC3-L000119](../../agents/web_agent.py#L119) | 119 | `"    \"تقنية\": {\"technology\"}, \"تقنيات\": {\"technology\"},"` | — |
| [SRC-1AE03B9EC3-L000120](../../agents/web_agent.py#L120) | 120 | `"    \"ميكروسوفت\": {\"microsoft\"}, \"مايكروسوفت\": {\"microsoft\"},"` | — |
| [SRC-1AE03B9EC3-L000121](../../agents/web_agent.py#L121) | 121 | `"    \"microsoft\": {\"ميكروسوفت\", \"مايكروسوفت\"},"` | — |
| [SRC-1AE03B9EC3-L000122](../../agents/web_agent.py#L122) | 122 | `"    \"جمهورية\": {\"republic\"}, \"republic\": {\"جمهورية\"},"` | — |
| [SRC-1AE03B9EC3-L000123](../../agents/web_agent.py#L123) | 123 | `"    \"الرقمية\": {\"digital\"}, \"رقمية\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000124](../../agents/web_agent.py#L124) | 124 | `"    \"الرقميه\": {\"digital\"}, \"رقميه\": {\"digital\"},"` | — |
| [SRC-1AE03B9EC3-L000125](../../agents/web_agent.py#L125) | 125 | `"    \"موقع\": {\"website\", \"portal\"}, \"مواقع\": {\"websites\", \"portals\"},"` | — |
| [SRC-1AE03B9EC3-L000126](../../agents/web_agent.py#L126) | 126 | `"    \"التجمع\": {\"settlement\"}, \"تجمع\": {\"settlement\"},"` | — |
| [SRC-1AE03B9EC3-L000127](../../agents/web_agent.py#L127) | 127 | `"    \"الخامس\": {\"fifth\", \"5th\"}, \"خامس\": {\"fifth\", \"5th\"},"` | — |
| [SRC-1AE03B9EC3-L000128](../../agents/web_agent.py#L128) | 128 | `"    \"شقة\": {\"apartment\", \"flat\"}, \"شقق\": {\"apartments\", \"flats\"},"` | — |
| [SRC-1AE03B9EC3-L000129](../../agents/web_agent.py#L129) | 129 | `"    \"عميل\": {\"customer\", \"buyer\"}, \"عملاء\": {\"customers\", \"buyers\"},"` | — |
| [SRC-1AE03B9EC3-L000130](../../agents/web_agent.py#L130) | 130 | `"    \"شراء\": {\"buy\", \"purchase\"}, \"مشتري\": {\"buyer\"},"` | — |
| [SRC-1AE03B9EC3-L000131](../../agents/web_agent.py#L131) | 131 | `"    # Small, explicit Arabic-English topic vocabulary; this helps Arabic prompts"` | — |
| [SRC-1AE03B9EC3-L000132](../../agents/web_agent.py#L132) | 132 | `"    # match English-indexed results without relaxing URL or destination safety."` | — |
| [SRC-1AE03B9EC3-L000133](../../agents/web_agent.py#L133) | 133 | `"    \"سيارة\": {\"car\", \"vehicle\"}, \"السيارة\": {\"car\", \"vehicle\"},"` | — |
| [SRC-1AE03B9EC3-L000134](../../agents/web_agent.py#L134) | 134 | `"    \"سيارات\": {\"cars\", \"vehicles\"}, \"السيارات\": {\"cars\", \"vehicles\"},"` | — |
| [SRC-1AE03B9EC3-L000135](../../agents/web_agent.py#L135) | 135 | `"    \"كهربائي\": {\"electric\"}, \"كهربائية\": {\"electric\"},"` | — |
| [SRC-1AE03B9EC3-L000136](../../agents/web_agent.py#L136) | 136 | `"    \"الكهربائي\": {\"electric\"}, \"الكهربائية\": {\"electric\"},"` | — |
| [SRC-1AE03B9EC3-L000137](../../agents/web_agent.py#L137) | 137 | `"    \"شحن\": {\"charging\", \"charge\"}, \"الشحن\": {\"charging\", \"charge\"},"` | — |
| [SRC-1AE03B9EC3-L000138](../../agents/web_agent.py#L138) | 138 | `"    \"شاحن\": {\"charger\"}, \"بطارية\": {\"battery\"}, \"بطاريات\": {\"batteries\"},"` | — |
| [SRC-1AE03B9EC3-L000139](../../agents/web_agent.py#L139) | 139 | `"    \"تكلفة\": {\"cost\", \"costs\"}, \"التكلفة\": {\"cost\", \"costs\"},"` | — |
| [SRC-1AE03B9EC3-L000140](../../agents/web_agent.py#L140) | 140 | `"    \"البنية\": {\"infrastructure\"}, \"التحتية\": {\"infrastructure\"},"` | — |
| [SRC-1AE03B9EC3-L000141](../../agents/web_agent.py#L141) | 141 | `"    \"تحدي\": {\"challenge\"}, \"تحديات\": {\"challenges\"}, \"التحديات\": {\"challenges\"},"` | — |
| [SRC-1AE03B9EC3-L000142](../../agents/web_agent.py#L142) | 142 | `"    \"وكيل\": {\"agent\"}, \"الوكيل\": {\"agent\"},"` | — |
| [SRC-1AE03B9EC3-L000143](../../agents/web_agent.py#L143) | 143 | `"    \"وكلاء\": {\"agents\"}, \"الوكلاء\": {\"agents\"},"` | — |
| [SRC-1AE03B9EC3-L000144](../../agents/web_agent.py#L144) | 144 | `"    # Bilingual vocabulary for AI use-case searches. Keep the relevance floor"` | — |
| [SRC-1AE03B9EC3-L000145](../../agents/web_agent.py#L145) | 145 | `"    # unchanged; expand only concepts that commonly appear in Arabic news titles."` | — |
| [SRC-1AE03B9EC3-L000146](../../agents/web_agent.py#L146) | 146 | `"    \"استخدام\": {\"use\", \"usage\", \"application\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000147](../../agents/web_agent.py#L147) | 147 | `"    \"استخدامات\": {\"use\", \"usage\", \"application\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000148](../../agents/web_agent.py#L148) | 148 | `"    \"استعمال\": {\"use\", \"usage\", \"application\"},"` | — |
| [SRC-1AE03B9EC3-L000149](../../agents/web_agent.py#L149) | 149 | `"    \"استعمالات\": {\"use\", \"usage\", \"applications\"},"` | — |
| [SRC-1AE03B9EC3-L000150](../../agents/web_agent.py#L150) | 150 | `"    \"حالة\": {\"case\"}, \"حالات\": {\"cases\", \"case\"},"` | — |
| [SRC-1AE03B9EC3-L000151](../../agents/web_agent.py#L151) | 151 | `"    \"اعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000152](../../agents/web_agent.py#L152) | 152 | `"    \"الاعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000153](../../agents/web_agent.py#L153) | 153 | `"    \"للاعمال\": {\"business\", \"businesses\", \"work\"},"` | — |
| [SRC-1AE03B9EC3-L000154](../../agents/web_agent.py#L154) | 154 | `"    \"شركات\": {\"company\", \"companies\", \"business\", \"businesses\"},"` | — |
| [SRC-1AE03B9EC3-L000155](../../agents/web_agent.py#L155) | 155 | `"    \"الشركات\": {\"company\", \"companies\", \"business\", \"businesses\"},"` | — |
| [SRC-1AE03B9EC3-L000156](../../agents/web_agent.py#L156) | 156 | `"    \"صغير\": {\"small\"}, \"صغيرة\": {\"small\"}, \"الصغير\": {\"small\"}, \"الصغيرة\": {\"small\"},"` | — |
| [SRC-1AE03B9EC3-L000157](../../agents/web_agent.py#L157) | 157 | `"    \"ذكاء\": {\"intelligence\", \"ai\"}, \"الذكاء\": {\"intelligence\", \"ai\"},"` | — |
| [SRC-1AE03B9EC3-L000158](../../agents/web_agent.py#L158) | 158 | `"    \"اصطناعي\": {\"artificial\", \"ai\"}, \"الاصطناعي\": {\"artificial\", \"ai\"},"` | — |
| [SRC-1AE03B9EC3-L000159](../../agents/web_agent.py#L159) | 159 | `"    \"تطور\": {\"development\", \"advance\"}, \"تطورات\": {\"developments\", \"advances\", \"updates\", \"latest\"},"` | — |
| [SRC-1AE03B9EC3-L000160](../../agents/web_agent.py#L160) | 160 | `"    \"التطورات\": {\"developments\", \"advances\", \"updates\", \"latest\"},"` | — |
| [SRC-1AE03B9EC3-L000161](../../agents/web_agent.py#L161) | 161 | `"    \"اراء\": {\"opinions\", \"views\"}, \"تجربة\": {\"experience\"}, \"تجارب\": {\"experiences\", \"reviews\"},"` | — |
| [SRC-1AE03B9EC3-L000162](../../agents/web_agent.py#L162) | 162 | `"    \"مستخدم\": {\"user\"}, \"المستخدم\": {\"user\"}, \"مستخدمين\": {\"users\"},"` | — |
| [SRC-1AE03B9EC3-L000163](../../agents/web_agent.py#L163) | 163 | `"    \"المستخدمين\": {\"users\"}, \"مالكون\": {\"owners\"}, \"المالكون\": {\"owners\"},"` | — |
| [SRC-1AE03B9EC3-L000164](../../agents/web_agent.py#L164) | 164 | `"}"` | — |
| [SRC-1AE03B9EC3-L000165](../../agents/web_agent.py#L165) | 165 | `"_CALENDAR_MONTHS = ("` | — |
| [SRC-1AE03B9EC3-L000166](../../agents/web_agent.py#L166) | 166 | `"    \"يناير\", \"فبراير\", \"مارس\", \"ابريل\", \"أبريل\", \"مايو\", \"يونيو\","` | — |
| [SRC-1AE03B9EC3-L000167](../../agents/web_agent.py#L167) | 167 | `"    \"يوليو\", \"اغسطس\", \"أغسطس\", \"سبتمبر\", \"اكتوبر\", \"أكتوبر\","` | — |
| [SRC-1AE03B9EC3-L000168](../../agents/web_agent.py#L168) | 168 | `"    \"نوفمبر\", \"ديسمبر\", \"january\", \"february\", \"march\", \"april\","` | — |
| [SRC-1AE03B9EC3-L000169](../../agents/web_agent.py#L169) | 169 | `"    \"may\", \"june\", \"july\", \"august\", \"september\", \"october\","` | — |
| [SRC-1AE03B9EC3-L000170](../../agents/web_agent.py#L170) | 170 | `"    \"november\", \"december\","` | — |
| [SRC-1AE03B9EC3-L000171](../../agents/web_agent.py#L171) | 171 | `")"` | — |
| [SRC-1AE03B9EC3-L000172](../../agents/web_agent.py#L172) | 172 | `"_BLOCKED_SOURCE_DOMAINS = frozenset({"` | — |
| [SRC-1AE03B9EC3-L000173](../../agents/web_agent.py#L173) | 173 | `"    \"translate.google.com\", \"translate.googleusercontent.com\","` | — |
| [SRC-1AE03B9EC3-L000174](../../agents/web_agent.py#L174) | 174 | `"})"` | — |
| [SRC-1AE03B9EC3-L000175](../../agents/web_agent.py#L175) | 175 | `""` | — |
| [SRC-1AE03B9EC3-L000176](../../agents/web_agent.py#L176) | 176 | `""` | — |
| [SRC-1AE03B9EC3-L000177](../../agents/web_agent.py#L177) | 177 | `"def _normalize_search_query(value: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000178](../../agents/web_agent.py#L178) | 178 | `"    \"\"\"Normalize Arabic letters/diacritics while preserving search operators and dates.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000179](../../agents/web_agent.py#L179) | 179 | `"    value = unicodedata.normalize(\"NFKC\", value or \"\")"` | — |
| [SRC-1AE03B9EC3-L000180](../../agents/web_agent.py#L180) | 180 | `"    value = _ARABIC_DIACRITICS_RE.sub(\"\", value).translate(_ARABIC_SEARCH_TRANSLATION)"` | — |
| [SRC-1AE03B9EC3-L000181](../../agents/web_agent.py#L181) | 181 | `"    return re.sub(r\"\\s+\", \" \", value).strip()"` | — |
| [SRC-1AE03B9EC3-L000182](../../agents/web_agent.py#L182) | 182 | `""` | — |
| [SRC-1AE03B9EC3-L000183](../../agents/web_agent.py#L183) | 183 | `""` | — |
| [SRC-1AE03B9EC3-L000184](../../agents/web_agent.py#L184) | 184 | `"# Normalize stop words too: otherwise Arabic letter normalization (e.g. ة→ه, أ→ا)"` | — |
| [SRC-1AE03B9EC3-L000185](../../agents/web_agent.py#L185) | 185 | `"# can leave request-format wording in the token set and distort relevance scores."` | — |
| [SRC-1AE03B9EC3-L000186](../../agents/web_agent.py#L186) | 186 | `"_NORMALIZED_SEARCH_STOPWORDS = frozenset("` | — |
| [SRC-1AE03B9EC3-L000187](../../agents/web_agent.py#L187) | 187 | `"    _normalize_search_query(word).casefold() for word in _SEARCH_STOPWORDS"` | — |
| [SRC-1AE03B9EC3-L000188](../../agents/web_agent.py#L188) | 188 | `")"` | — |
| [SRC-1AE03B9EC3-L000189](../../agents/web_agent.py#L189) | 189 | `""` | — |
| [SRC-1AE03B9EC3-L000190](../../agents/web_agent.py#L190) | 190 | `""` | — |
| [SRC-1AE03B9EC3-L000191](../../agents/web_agent.py#L191) | 191 | `"# Normalize synonym keys and values by the same rules as search text. This avoids"` | — |
| [SRC-1AE03B9EC3-L000192](../../agents/web_agent.py#L192) | 192 | `"# Arabic ta-marbuta/alif variants silently disabling Arabic-to-English matching."` | — |
| [SRC-1AE03B9EC3-L000193](../../agents/web_agent.py#L193) | 193 | `"_NORMALIZED_SEARCH_SYNONYMS: dict[str, set[str]] = {}"` | — |
| [SRC-1AE03B9EC3-L000194](../../agents/web_agent.py#L194) | 194 | `"for _synonym_key, _synonym_values in _SEARCH_SYNONYMS.items():"` | — |
| [SRC-1AE03B9EC3-L000195](../../agents/web_agent.py#L195) | 195 | `"    _normalized_key = _normalize_search_query(_synonym_key).casefold()"` | — |
| [SRC-1AE03B9EC3-L000196](../../agents/web_agent.py#L196) | 196 | `"    _NORMALIZED_SEARCH_SYNONYMS.setdefault(_normalized_key, set()).update("` | — |
| [SRC-1AE03B9EC3-L000197](../../agents/web_agent.py#L197) | 197 | `"        _normalize_search_query(value).casefold() for value in _synonym_values"` | — |
| [SRC-1AE03B9EC3-L000198](../../agents/web_agent.py#L198) | 198 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000199](../../agents/web_agent.py#L199) | 199 | `""` | — |
| [SRC-1AE03B9EC3-L000200](../../agents/web_agent.py#L200) | 200 | `""` | — |
| [SRC-1AE03B9EC3-L000201](../../agents/web_agent.py#L201) | 201 | `"def _search_tokens(value: str) -> set[str]:"` | — |
| [SRC-1AE03B9EC3-L000202](../../agents/web_agent.py#L202) | 202 | `"    \"\"\"Tokenize Arabic/English text and expand a small bilingual vocabulary.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000203](../../agents/web_agent.py#L203) | 203 | `"    value = _normalize_search_query(value).casefold()"` | — |
| [SRC-1AE03B9EC3-L000204](../../agents/web_agent.py#L204) | 204 | `"    value = re.sub(r\"(?i)\\bsite\\s*:\\s*\\S+\", \" \", value)"` | — |
| [SRC-1AE03B9EC3-L000205](../../agents/web_agent.py#L205) | 205 | `"    tokens = re.findall(r\"[a-z0-9]+\|[\\u0620-\\u064A\\u066E-\\u06D3]+\", value)"` | — |
| [SRC-1AE03B9EC3-L000206](../../agents/web_agent.py#L206) | 206 | `"    result: set[str] = set()"` | — |
| [SRC-1AE03B9EC3-L000207](../../agents/web_agent.py#L207) | 207 | `"    for token in tokens:"` | — |
| [SRC-1AE03B9EC3-L000208](../../agents/web_agent.py#L208) | 208 | `"        if token in _NORMALIZED_SEARCH_STOPWORDS or len(token) < 2:"` | — |
| [SRC-1AE03B9EC3-L000209](../../agents/web_agent.py#L209) | 209 | `"            continue"` | — |
| [SRC-1AE03B9EC3-L000210](../../agents/web_agent.py#L210) | 210 | `"        forms = {token}"` | — |
| [SRC-1AE03B9EC3-L000211](../../agents/web_agent.py#L211) | 211 | `"        if token.startswith(\"ال\") and len(token) > 4:"` | — |
| [SRC-1AE03B9EC3-L000212](../../agents/web_agent.py#L212) | 212 | `"            forms.add(token[2:])"` | — |
| [SRC-1AE03B9EC3-L000213](../../agents/web_agent.py#L213) | 213 | `"        forms.update(_NORMALIZED_SEARCH_SYNONYMS.get(token, set()))"` | — |
| [SRC-1AE03B9EC3-L000214](../../agents/web_agent.py#L214) | 214 | `"        # Reverse-map common English equivalents so Arabic and English results can match."` | — |
| [SRC-1AE03B9EC3-L000215](../../agents/web_agent.py#L215) | 215 | `"        for arabic, english in _NORMALIZED_SEARCH_SYNONYMS.items():"` | — |
| [SRC-1AE03B9EC3-L000216](../../agents/web_agent.py#L216) | 216 | `"            if token in english:"` | — |
| [SRC-1AE03B9EC3-L000217](../../agents/web_agent.py#L217) | 217 | `"                forms.add(arabic)"` | — |
| [SRC-1AE03B9EC3-L000218](../../agents/web_agent.py#L218) | 218 | `"                if arabic.startswith(\"ال\") and len(arabic) > 4:"` | — |
| [SRC-1AE03B9EC3-L000219](../../agents/web_agent.py#L219) | 219 | `"                    forms.add(arabic[2:])"` | — |
| [SRC-1AE03B9EC3-L000220](../../agents/web_agent.py#L220) | 220 | `"        result.update(forms)"` | — |
| [SRC-1AE03B9EC3-L000221](../../agents/web_agent.py#L221) | 221 | `"    return result"` | — |
| [SRC-1AE03B9EC3-L000222](../../agents/web_agent.py#L222) | 222 | `""` | — |
| [SRC-1AE03B9EC3-L000223](../../agents/web_agent.py#L223) | 223 | `""` | — |
| [SRC-1AE03B9EC3-L000224](../../agents/web_agent.py#L224) | 224 | `"def _relevance_query_tokens(query: str) -> set[str]:"` | — |
| [SRC-1AE03B9EC3-L000225](../../agents/web_agent.py#L225) | 225 | `"    \"\"\"Return topic concepts after removing answer-format and query-expansion wording.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000226](../../agents/web_agent.py#L226) | 226 | `"    query = compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L000227](../../agents/web_agent.py#L227) | 227 | `"    if not query:"` | — |
| [SRC-1AE03B9EC3-L000228](../../agents/web_agent.py#L228) | 228 | `"        return set()"` | — |
| [SRC-1AE03B9EC3-L000229](../../agents/web_agent.py#L229) | 229 | `"    query_text = _normalize_search_query(query).casefold()"` | — |
| [SRC-1AE03B9EC3-L000230](../../agents/web_agent.py#L230) | 230 | `"    query_text = re.sub(r\"(?i)\\bsite\\s*:\\s*\\S+\", \" \", query_text)"` | — |
| [SRC-1AE03B9EC3-L000231](../../agents/web_agent.py#L231) | 231 | `"    return {"` | — |
| [SRC-1AE03B9EC3-L000232](../../agents/web_agent.py#L232) | 232 | `"        token for token in re.findall(r\"[a-z0-9]+\|[\\u0620-\\u064A\\u066E-\\u06D3]+\", query_text)"` | — |
| [SRC-1AE03B9EC3-L000233](../../agents/web_agent.py#L233) | 233 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L000234](../../agents/web_agent.py#L234) | 234 | `"            token not in _NORMALIZED_SEARCH_STOPWORDS"` | — |
| [SRC-1AE03B9EC3-L000235](../../agents/web_agent.py#L235) | 235 | `"            and token not in _GENERIC_QUERY_MODIFIER_TOKENS"` | — |
| [SRC-1AE03B9EC3-L000236](../../agents/web_agent.py#L236) | 236 | `"            and len(token) >= 2"` | — |
| [SRC-1AE03B9EC3-L000237](../../agents/web_agent.py#L237) | 237 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000238](../../agents/web_agent.py#L238) | 238 | `"    }"` | — |
| [SRC-1AE03B9EC3-L000239](../../agents/web_agent.py#L239) | 239 | `""` | — |
| [SRC-1AE03B9EC3-L000240](../../agents/web_agent.py#L240) | 240 | `""` | — |
| [SRC-1AE03B9EC3-L000241](../../agents/web_agent.py#L241) | 241 | `"def _minimum_relevance_ratio(_query: str) -> float:"` | — |
| [SRC-1AE03B9EC3-L000242](../../agents/web_agent.py#L242) | 242 | `"    \"\"\"Keep the established 20% relevance floor after query normalization and token cleanup.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000243](../../agents/web_agent.py#L243) | 243 | `"    return 0.20"` | — |
| [SRC-1AE03B9EC3-L000244](../../agents/web_agent.py#L244) | 244 | `""` | — |
| [SRC-1AE03B9EC3-L000245](../../agents/web_agent.py#L245) | 245 | `""` | — |
| [SRC-1AE03B9EC3-L000246](../../agents/web_agent.py#L246) | 246 | `"def _relevance_ratio(query: str, evidence: str) -> float:"` | — |
| [SRC-1AE03B9EC3-L000247](../../agents/web_agent.py#L247) | 247 | `"    \"\"\"Fraction of meaningful query concepts present in a candidate's title/snippet.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000248](../../agents/web_agent.py#L248) | 248 | `"    query_tokens = _relevance_query_tokens(query)"` | — |
| [SRC-1AE03B9EC3-L000249](../../agents/web_agent.py#L249) | 249 | `"    if not query_tokens:"` | — |
| [SRC-1AE03B9EC3-L000250](../../agents/web_agent.py#L250) | 250 | `"        # Relevance cannot be established from an instruction-only query."` | — |
| [SRC-1AE03B9EC3-L000251](../../agents/web_agent.py#L251) | 251 | `"        return 0.0"` | — |
| [SRC-1AE03B9EC3-L000252](../../agents/web_agent.py#L252) | 252 | `"    expanded_evidence = _search_tokens(evidence)"` | — |
| [SRC-1AE03B9EC3-L000253](../../agents/web_agent.py#L253) | 253 | `"    matched = sum("` | — |
| [SRC-1AE03B9EC3-L000254](../../agents/web_agent.py#L254) | 254 | `"        1 for token in query_tokens"` | — |
| [SRC-1AE03B9EC3-L000255](../../agents/web_agent.py#L255) | 255 | `"        if token in expanded_evidence"` | — |
| [SRC-1AE03B9EC3-L000256](../../agents/web_agent.py#L256) | 256 | `"        or (token.startswith(\"ال\") and token[2:] in expanded_evidence)"` | — |
| [SRC-1AE03B9EC3-L000257](../../agents/web_agent.py#L257) | 257 | `"        or bool(_NORMALIZED_SEARCH_SYNONYMS.get(token, set()) & expanded_evidence)"` | — |
| [SRC-1AE03B9EC3-L000258](../../agents/web_agent.py#L258) | 258 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000259](../../agents/web_agent.py#L259) | 259 | `"    ratio = matched / len(query_tokens)"` | — |
| [SRC-1AE03B9EC3-L000260](../../agents/web_agent.py#L260) | 260 | `"    # On longer questions, two matching topic concepts are required; request wording"` | — |
| [SRC-1AE03B9EC3-L000261](../../agents/web_agent.py#L261) | 261 | `"    # should not silently raise that floor to three or four concepts."` | — |
| [SRC-1AE03B9EC3-L000262](../../agents/web_agent.py#L262) | 262 | `"    if len(query_tokens) >= 4 and matched < 2:"` | — |
| [SRC-1AE03B9EC3-L000263](../../agents/web_agent.py#L263) | 263 | `"        return 0.0"` | — |
| [SRC-1AE03B9EC3-L000264](../../agents/web_agent.py#L264) | 264 | `"    return ratio"` | — |
| [SRC-1AE03B9EC3-L000265](../../agents/web_agent.py#L265) | 265 | `""` | — |
| [SRC-1AE03B9EC3-L000266](../../agents/web_agent.py#L266) | 266 | `"def _blocked_source_url(url: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000267](../../agents/web_agent.py#L267) | 267 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000268](../../agents/web_agent.py#L268) | 268 | `"        host = (urllib.parse.urlparse(url).hostname or \"\").lower().rstrip(\".\")"` | — |
| [SRC-1AE03B9EC3-L000269](../../agents/web_agent.py#L269) | 269 | `"        return any(host == domain or host.endswith(\".\" + domain) for domain in _BLOCKED_SOURCE_DOMAINS)"` | — |
| [SRC-1AE03B9EC3-L000270](../../agents/web_agent.py#L270) | 270 | `"    except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L000271](../../agents/web_agent.py#L271) | 271 | `"        return True"` | — |
| [SRC-1AE03B9EC3-L000272](../../agents/web_agent.py#L272) | 272 | `""` | — |
| [SRC-1AE03B9EC3-L000273](../../agents/web_agent.py#L273) | 273 | `""` | — |
| [SRC-1AE03B9EC3-L000274](../../agents/web_agent.py#L274) | 274 | `"class AgentDependencyError(RuntimeError):"` | — |
| [SRC-1AE03B9EC3-L000275](../../agents/web_agent.py#L275) | 275 | `"    \"\"\"A required optional runtime dependency is unavailable.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000276](../../agents/web_agent.py#L276) | 276 | `""` | — |
| [SRC-1AE03B9EC3-L000277](../../agents/web_agent.py#L277) | 277 | `""` | — |
| [SRC-1AE03B9EC3-L000278](../../agents/web_agent.py#L278) | 278 | `"def _clean_text(value: Any, limit: int) -> str:"` | — |
| [SRC-1AE03B9EC3-L000279](../../agents/web_agent.py#L279) | 279 | `"    if not isinstance(value, str):"` | — |
| [SRC-1AE03B9EC3-L000280](../../agents/web_agent.py#L280) | 280 | `"        return \"\""` | — |
| [SRC-1AE03B9EC3-L000281](../../agents/web_agent.py#L281) | 281 | `"    return \" \".join(value.replace(\"\\x00\", \" \").split())[:limit]"` | — |
| [SRC-1AE03B9EC3-L000282](../../agents/web_agent.py#L282) | 282 | `""` | — |
| [SRC-1AE03B9EC3-L000283](../../agents/web_agent.py#L283) | 283 | `""` | — |
| [SRC-1AE03B9EC3-L000284](../../agents/web_agent.py#L284) | 284 | `"def _public_http_url(value: Any) -> str \| None:"` | — |
| [SRC-1AE03B9EC3-L000285](../../agents/web_agent.py#L285) | 285 | `"    \"\"\"Lexically validate an HTTP URL before using it as a search source.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000286](../../agents/web_agent.py#L286) | 286 | `"    if not isinstance(value, str) or len(value) > 2048:"` | — |
| [SRC-1AE03B9EC3-L000287](../../agents/web_agent.py#L287) | 287 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000288](../../agents/web_agent.py#L288) | 288 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000289](../../agents/web_agent.py#L289) | 289 | `"        parsed = urllib.parse.urlparse(value.strip())"` | — |
| [SRC-1AE03B9EC3-L000290](../../agents/web_agent.py#L290) | 290 | `"        if parsed.scheme not in {\"http\", \"https\"}:"` | — |
| [SRC-1AE03B9EC3-L000291](../../agents/web_agent.py#L291) | 291 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000292](../../agents/web_agent.py#L292) | 292 | `"        if not parsed.hostname or parsed.username is not None or parsed.password is not None:"` | — |
| [SRC-1AE03B9EC3-L000293](../../agents/web_agent.py#L293) | 293 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000294](../../agents/web_agent.py#L294) | 294 | `"        if parsed.port not in (None, 80, 443):"` | — |
| [SRC-1AE03B9EC3-L000295](../../agents/web_agent.py#L295) | 295 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000296](../../agents/web_agent.py#L296) | 296 | `"        host = parsed.hostname.rstrip(\".\").lower()"` | — |
| [SRC-1AE03B9EC3-L000297](../../agents/web_agent.py#L297) | 297 | `"        if not host or host in {\"localhost\"} or host.endswith((\".local\", \".internal\", \".localhost\")):"` | — |
| [SRC-1AE03B9EC3-L000298](../../agents/web_agent.py#L298) | 298 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000299](../../agents/web_agent.py#L299) | 299 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000300](../../agents/web_agent.py#L300) | 300 | `"            ip = ipaddress.ip_address(host)"` | — |
| [SRC-1AE03B9EC3-L000301](../../agents/web_agent.py#L301) | 301 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L000302](../../agents/web_agent.py#L302) | 302 | `"            pass"` | — |
| [SRC-1AE03B9EC3-L000303](../../agents/web_agent.py#L303) | 303 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L000304](../../agents/web_agent.py#L304) | 304 | `"            if not ip.is_global:"` | — |
| [SRC-1AE03B9EC3-L000305](../../agents/web_agent.py#L305) | 305 | `"                return None"` | — |
| [SRC-1AE03B9EC3-L000306](../../agents/web_agent.py#L306) | 306 | `"        return urllib.parse.urlunparse(parsed._replace(fragment=\"\"))"` | — |
| [SRC-1AE03B9EC3-L000307](../../agents/web_agent.py#L307) | 307 | `"    except (ValueError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L000308](../../agents/web_agent.py#L308) | 308 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000309](../../agents/web_agent.py#L309) | 309 | `""` | — |
| [SRC-1AE03B9EC3-L000310](../../agents/web_agent.py#L310) | 310 | `""` | — |
| [SRC-1AE03B9EC3-L000311](../../agents/web_agent.py#L311) | 311 | `"def _public_ip_literals(host: str) -> list[str] \| None:"` | — |
| [SRC-1AE03B9EC3-L000312](../../agents/web_agent.py#L312) | 312 | `"    \"\"\"Resolve host and return its public addresses."` | — |
| [SRC-1AE03B9EC3-L000313](../../agents/web_agent.py#L313) | 313 | `""` | — |
| [SRC-1AE03B9EC3-L000314](../../agents/web_agent.py#L314) | 314 | `"    Returns None when resolution fails or any answer is not a global address."` | — |
| [SRC-1AE03B9EC3-L000315](../../agents/web_agent.py#L315) | 315 | `"    Callers must open the TCP connection to one of these literals. A second DNS"` | — |
| [SRC-1AE03B9EC3-L000316](../../agents/web_agent.py#L316) | 316 | `"    lookup is not equivalent: the name can be rebound to a private address"` | — |
| [SRC-1AE03B9EC3-L000317](../../agents/web_agent.py#L317) | 317 | `"    between the check and the connection (DNS rebinding / TOCTOU)."` | — |
| [SRC-1AE03B9EC3-L000318](../../agents/web_agent.py#L318) | 318 | `"    \"\"\""` | — |
| [SRC-1AE03B9EC3-L000319](../../agents/web_agent.py#L319) | 319 | `"    if not host:"` | — |
| [SRC-1AE03B9EC3-L000320](../../agents/web_agent.py#L320) | 320 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000321](../../agents/web_agent.py#L321) | 321 | `"    try:"` | — |
| [SRC-1AE03B9EC3-L000322](../../agents/web_agent.py#L322) | 322 | `"        answers = socket.getaddrinfo(host, None, type=socket.SOCK_STREAM)"` | — |
| [SRC-1AE03B9EC3-L000323](../../agents/web_agent.py#L323) | 323 | `"    except (OSError, socket.gaierror):"` | — |
| [SRC-1AE03B9EC3-L000324](../../agents/web_agent.py#L324) | 324 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000325](../../agents/web_agent.py#L325) | 325 | `"    if not answers:"` | — |
| [SRC-1AE03B9EC3-L000326](../../agents/web_agent.py#L326) | 326 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000327](../../agents/web_agent.py#L327) | 327 | `"    literals: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L000328](../../agents/web_agent.py#L328) | 328 | `"    for answer in answers:"` | — |
| [SRC-1AE03B9EC3-L000329](../../agents/web_agent.py#L329) | 329 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000330](../../agents/web_agent.py#L330) | 330 | `"            address = ipaddress.ip_address(answer[4][0])"` | — |
| [SRC-1AE03B9EC3-L000331](../../agents/web_agent.py#L331) | 331 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L000332](../../agents/web_agent.py#L332) | 332 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000333](../../agents/web_agent.py#L333) | 333 | `"        if not address.is_global:"` | — |
| [SRC-1AE03B9EC3-L000334](../../agents/web_agent.py#L334) | 334 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L000335](../../agents/web_agent.py#L335) | 335 | `"        literal = str(address)"` | — |
| [SRC-1AE03B9EC3-L000336](../../agents/web_agent.py#L336) | 336 | `"        if literal not in literals:"` | — |
| [SRC-1AE03B9EC3-L000337](../../agents/web_agent.py#L337) | 337 | `"            literals.append(literal)"` | — |
| [SRC-1AE03B9EC3-L000338](../../agents/web_agent.py#L338) | 338 | `"    return literals or None"` | — |
| [SRC-1AE03B9EC3-L000339](../../agents/web_agent.py#L339) | 339 | `""` | — |
| [SRC-1AE03B9EC3-L000340](../../agents/web_agent.py#L340) | 340 | `""` | — |
| [SRC-1AE03B9EC3-L000341](../../agents/web_agent.py#L341) | 341 | `"def _host_resolves_publicly(host: str) -> bool:"` | — |
| [SRC-1AE03B9EC3-L000342](../../agents/web_agent.py#L342) | 342 | `"    \"\"\"Reject local/private destinations before fetching a third-party page.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000343](../../agents/web_agent.py#L343) | 343 | `"    return _public_ip_literals(host) is not None"` | — |
| [SRC-1AE03B9EC3-L000344](../../agents/web_agent.py#L344) | 344 | `""` | — |
| [SRC-1AE03B9EC3-L000345](../../agents/web_agent.py#L345) | 345 | `""` | — |
| [SRC-1AE03B9EC3-L000346](../../agents/web_agent.py#L346) | 346 | `"def _pinned_connect_url(logical_url: str, ip: str) -> str \| None:"` | — |
| [SRC-1AE03B9EC3-L000347](../../agents/web_agent.py#L347) | 347 | `"    \"\"\"Rewrite a validated public URL so the connection target is a checked IP.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000348](../../agents/web_agent.py#L348) | 348 | `"    parsed = urllib.parse.urlparse(logical_url)"` | — |
| [SRC-1AE03B9EC3-L000349](../../agents/web_agent.py#L349) | 349 | `"    if parsed.port not in (None, 80, 443):"` | — |
| [SRC-1AE03B9EC3-L000350](../../agents/web_agent.py#L350) | 350 | `"        return None"` | — |
| [SRC-1AE03B9EC3-L000351](../../agents/web_agent.py#L351) | 351 | `"    literal = f\"[{ip}]\" if \":\" in ip else ip"` | — |
| [SRC-1AE03B9EC3-L000352](../../agents/web_agent.py#L352) | 352 | `"    netloc = literal if parsed.port is None else f\"{literal}:{parsed.port}\""` | — |
| [SRC-1AE03B9EC3-L000353](../../agents/web_agent.py#L353) | 353 | `"    return urllib.parse.urlunparse(parsed._replace(netloc=netloc))"` | — |
| [SRC-1AE03B9EC3-L000354](../../agents/web_agent.py#L354) | 354 | `""` | — |
| [SRC-1AE03B9EC3-L000355](../../agents/web_agent.py#L355) | 355 | `""` | — |
| [SRC-1AE03B9EC3-L000356](../../agents/web_agent.py#L356) | 356 | `"def _fallback_answer(sources: list[dict[str, Any]], reason: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000357](../../agents/web_agent.py#L357) | 357 | `"    lines = [reason]"` | — |
| [SRC-1AE03B9EC3-L000358](../../agents/web_agent.py#L358) | 358 | `"    usable = [source for source in sources if source.get(\"snippet\")]"` | — |
| [SRC-1AE03B9EC3-L000359](../../agents/web_agent.py#L359) | 359 | `"    for index, source in enumerate(usable[:5], 1):"` | — |
| [SRC-1AE03B9EC3-L000360](../../agents/web_agent.py#L360) | 360 | `"        lines.append("` | — |
| [SRC-1AE03B9EC3-L000361](../../agents/web_agent.py#L361) | 361 | `"            f\"{index}. {source.get('title', 'نتيجة ويب')}: \""` | — |
| [SRC-1AE03B9EC3-L000362](../../agents/web_agent.py#L362) | 362 | `"            f\"{source['snippet']} (المصدر: {source['url']})\""` | — |
| [SRC-1AE03B9EC3-L000363](../../agents/web_agent.py#L363) | 363 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000364](../../agents/web_agent.py#L364) | 364 | `"    if not usable:"` | — |
| [SRC-1AE03B9EC3-L000365](../../agents/web_agent.py#L365) | 365 | `"        lines.append(\"لم أتمكن من استخراج مقتطفات كافية من نتائج الويب.\")"` | — |
| [SRC-1AE03B9EC3-L000366](../../agents/web_agent.py#L366) | 366 | `"    return \"\\n\\n\".join(lines)"` | — |
| [SRC-1AE03B9EC3-L000367](../../agents/web_agent.py#L367) | 367 | `""` | — |
| [SRC-1AE03B9EC3-L000368](../../agents/web_agent.py#L368) | 368 | `""` | — |
| [SRC-1AE03B9EC3-L000369](../../agents/web_agent.py#L369) | 369 | `"class PageFetchResult(tuple):"` | — |
| [SRC-1AE03B9EC3-L000370](../../agents/web_agent.py#L370) | 370 | `"    \"\"\"Two-item tuple compatible with legacy callers, with structured extraction status.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000371](../../agents/web_agent.py#L371) | 371 | `""` | — |
| [SRC-1AE03B9EC3-L000372](../../agents/web_agent.py#L372) | 372 | `"    def __new__("` | — |
| [SRC-1AE03B9EC3-L000373](../../agents/web_agent.py#L373) | 373 | `"        cls,"` | — |
| [SRC-1AE03B9EC3-L000374](../../agents/web_agent.py#L374) | 374 | `"        title: str = \"\","` | — |
| [SRC-1AE03B9EC3-L000375](../../agents/web_agent.py#L375) | 375 | `"        page_text: str = \"\","` | — |
| [SRC-1AE03B9EC3-L000376](../../agents/web_agent.py#L376) | 376 | `"        status: str = \"unknown\","` | — |
| [SRC-1AE03B9EC3-L000377](../../agents/web_agent.py#L377) | 377 | `"        error_class: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L000378](../../agents/web_agent.py#L378) | 378 | `"    ):"` | — |
| [SRC-1AE03B9EC3-L000379](../../agents/web_agent.py#L379) | 379 | `"        value = super().__new__(cls, (title, page_text))"` | — |
| [SRC-1AE03B9EC3-L000380](../../agents/web_agent.py#L380) | 380 | `"        value.status = status"` | — |
| [SRC-1AE03B9EC3-L000381](../../agents/web_agent.py#L381) | 381 | `"        value.error_class = error_class"` | — |
| [SRC-1AE03B9EC3-L000382](../../agents/web_agent.py#L382) | 382 | `"        return value"` | — |
| [SRC-1AE03B9EC3-L000383](../../agents/web_agent.py#L383) | 383 | `""` | — |
| [SRC-1AE03B9EC3-L000384](../../agents/web_agent.py#L384) | 384 | `""` | — |
| [SRC-1AE03B9EC3-L000385](../../agents/web_agent.py#L385) | 385 | `"def enforce_aspect_answer_completeness(result: dict[str, Any]) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L000386](../../agents/web_agent.py#L386) | 386 | `"    \"\"\"Withhold a final answer if any explicit axis lacks a text candidate."` | — |
| [SRC-1AE03B9EC3-L000387](../../agents/web_agent.py#L387) | 387 | `""` | — |
| [SRC-1AE03B9EC3-L000388](../../agents/web_agent.py#L388) | 388 | `"    Lexical coverage is only a conservative evidence-presence check, not semantic"` | — |
| [SRC-1AE03B9EC3-L000389](../../agents/web_agent.py#L389) | 389 | `"    verification. A missing candidate therefore blocks a *complete* answer rather"` | — |
| [SRC-1AE03B9EC3-L000390](../../agents/web_agent.py#L390) | 390 | `"    than asserting the underlying fact is unavailable everywhere."` | — |
| [SRC-1AE03B9EC3-L000391](../../agents/web_agent.py#L391) | 391 | `"    \"\"\""` | — |
| [SRC-1AE03B9EC3-L000392](../../agents/web_agent.py#L392) | 392 | `"    search_report = result.get(\"search_report\")"` | — |
| [SRC-1AE03B9EC3-L000393](../../agents/web_agent.py#L393) | 393 | `"    if not isinstance(search_report, dict):"` | — |
| [SRC-1AE03B9EC3-L000394](../../agents/web_agent.py#L394) | 394 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L000395](../../agents/web_agent.py#L395) | 395 | `"    prior_ledger = search_report.get(\"evidence_ledger\")"` | — |
| [SRC-1AE03B9EC3-L000396](../../agents/web_agent.py#L396) | 396 | `"    if not isinstance(prior_ledger, dict):"` | — |
| [SRC-1AE03B9EC3-L000397](../../agents/web_agent.py#L397) | 397 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L000398](../../agents/web_agent.py#L398) | 398 | `"    aspects = prior_ledger.get(\"aspects\")"` | — |
| [SRC-1AE03B9EC3-L000399](../../agents/web_agent.py#L399) | 399 | `"    if not isinstance(aspects, list) or not aspects:"` | — |
| [SRC-1AE03B9EC3-L000400](../../agents/web_agent.py#L400) | 400 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L000401](../../agents/web_agent.py#L401) | 401 | `"    targets = ["` | — |
| [SRC-1AE03B9EC3-L000402](../../agents/web_agent.py#L402) | 402 | `"        item[:120]"` | — |
| [SRC-1AE03B9EC3-L000403](../../agents/web_agent.py#L403) | 403 | `"        for item in aspects"` | — |
| [SRC-1AE03B9EC3-L000404](../../agents/web_agent.py#L404) | 404 | `"        if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L000405](../../agents/web_agent.py#L405) | 405 | `"    ][:8]"` | — |
| [SRC-1AE03B9EC3-L000406](../../agents/web_agent.py#L406) | 406 | `"    if not targets:"` | — |
| [SRC-1AE03B9EC3-L000407](../../agents/web_agent.py#L407) | 407 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L000408](../../agents/web_agent.py#L408) | 408 | `""` | — |
| [SRC-1AE03B9EC3-L000409](../../agents/web_agent.py#L409) | 409 | `"    raw_sources = result.get(\"sources\")"` | — |
| [SRC-1AE03B9EC3-L000410](../../agents/web_agent.py#L410) | 410 | `"    sources = ("` | — |
| [SRC-1AE03B9EC3-L000411](../../agents/web_agent.py#L411) | 411 | `"        [item for item in raw_sources if isinstance(item, dict)]"` | — |
| [SRC-1AE03B9EC3-L000412](../../agents/web_agent.py#L412) | 412 | `"        if isinstance(raw_sources, list)"` | — |
| [SRC-1AE03B9EC3-L000413](../../agents/web_agent.py#L413) | 413 | `"        else []"` | — |
| [SRC-1AE03B9EC3-L000414](../../agents/web_agent.py#L414) | 414 | `"    )"` | — |
| [SRC-1AE03B9EC3-L000415](../../agents/web_agent.py#L415) | 415 | `"    ledger = build_evidence_ledger(targets, sources)"` | — |
| [SRC-1AE03B9EC3-L000416](../../agents/web_agent.py#L416) | 416 | `"    search_report[\"evidence_ledger\"] = ledger"` | — |
| [SRC-1AE03B9EC3-L000417](../../agents/web_agent.py#L417) | 417 | `"    search_report[\"aspects\"] = targets"` | — |
| [SRC-1AE03B9EC3-L000418](../../agents/web_agent.py#L418) | 418 | `"    search_report[\"aspect_diagnostics_ar\"] = arabic_aspect_diagnostics(ledger)"` | — |
| [SRC-1AE03B9EC3-L000419](../../agents/web_agent.py#L419) | 419 | `"    search_report[\"aspect_evidence_gaps\"] = list(ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L000420](../../agents/web_agent.py#L420) | 420 | `"    search_report[\"aspect_coverage_lexical_ratio\"] = ledger.get(\"coverage_ratio\")"` | — |
| [SRC-1AE03B9EC3-L000421](../../agents/web_agent.py#L421) | 421 | `"    search_report[\"aspect_coverage_is_not_truth_score\"] = True"` | — |
| [SRC-1AE03B9EC3-L000422](../../agents/web_agent.py#L422) | 422 | `""` | — |
| [SRC-1AE03B9EC3-L000423](../../agents/web_agent.py#L423) | 423 | `"    result[\"aspects\"] = targets"` | — |
| [SRC-1AE03B9EC3-L000424](../../agents/web_agent.py#L424) | 424 | `"    result[\"aspect_evidence_gaps\"] = list(ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L000425](../../agents/web_agent.py#L425) | 425 | `"    result[\"aspect_diagnostics_ar\"] = list(search_report[\"aspect_diagnostics_ar\"])"` | — |
| [SRC-1AE03B9EC3-L000426](../../agents/web_agent.py#L426) | 426 | `"    result[\"aspect_coverage_lexical_ratio\"] = ledger.get(\"coverage_ratio\")"` | — |
| [SRC-1AE03B9EC3-L000427](../../agents/web_agent.py#L427) | 427 | `"    result[\"aspect_coverage_is_not_truth_score\"] = True"` | — |
| [SRC-1AE03B9EC3-L000428](../../agents/web_agent.py#L428) | 428 | `""` | — |
| [SRC-1AE03B9EC3-L000429](../../agents/web_agent.py#L429) | 429 | `"    missing = list(ledger.get(\"missing\") or [])"` | — |
| [SRC-1AE03B9EC3-L000430](../../agents/web_agent.py#L430) | 430 | `"    if missing:"` | — |
| [SRC-1AE03B9EC3-L000431](../../agents/web_agent.py#L431) | 431 | `"        result[\"answer\"] = ("` | — |
| [SRC-1AE03B9EC3-L000432](../../agents/web_agent.py#L432) | 432 | `"            \"لم أقدّم إجابة نهائية؛ لأن نتائج البحث المتاحة لا تتضمن مرشحًا نصيًا كافيًا \""` | — |
| [SRC-1AE03B9EC3-L000433](../../agents/web_agent.py#L433) | 433 | `"            \"لكل المحاور المطلوبة. المحاور التي تحتاج إلى دليل إضافي: \""` | — |
| [SRC-1AE03B9EC3-L000434](../../agents/web_agent.py#L434) | 434 | `"            + \"، \".join(str(item) for item in missing)"` | — |
| [SRC-1AE03B9EC3-L000435](../../agents/web_agent.py#L435) | 435 | `"            + \". لن أعرض مسودة جزئية على أنها إجابة مكتملة. وهذا النقص يصف النتائج التي جُمعت \""` | — |
| [SRC-1AE03B9EC3-L000436](../../agents/web_agent.py#L436) | 436 | `"            \"فقط، ولا يثبت عدم وجود معلومات عنها خارجها.\""` | — |
| [SRC-1AE03B9EC3-L000437](../../agents/web_agent.py#L437) | 437 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000438](../../agents/web_agent.py#L438) | 438 | `"        result[\"answer_was_withheld\"] = True"` | — |
| [SRC-1AE03B9EC3-L000439](../../agents/web_agent.py#L439) | 439 | `"        result[\"answer_completeness_status\"] = \"incomplete_evidence_withheld\""` | — |
| [SRC-1AE03B9EC3-L000440](../../agents/web_agent.py#L440) | 440 | `"        result[\"final_answer_status\"] = \"incomplete_evidence_withheld\""` | — |
| [SRC-1AE03B9EC3-L000441](../../agents/web_agent.py#L441) | 441 | `"        result[\"task_fulfillment_status\"] = \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L000442](../../agents/web_agent.py#L442) | 442 | `"        search_report[\"task_fulfillment_status\"] = \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L000443](../../agents/web_agent.py#L443) | 443 | `"        answer_coverage = result.get(\"answer_coverage\")"` | — |
| [SRC-1AE03B9EC3-L000444](../../agents/web_agent.py#L444) | 444 | `"        if isinstance(answer_coverage, dict):"` | — |
| [SRC-1AE03B9EC3-L000445](../../agents/web_agent.py#L445) | 445 | `"            answer_coverage[\"task_fulfillment_status\"] = \"possible_gap_detected\""` | — |
| [SRC-1AE03B9EC3-L000446](../../agents/web_agent.py#L446) | 446 | `"        warning = \"حُجبت الإجابة النهائية لوجود محاور مطلوبة بلا مرشح نصي كافٍ.\""` | — |
| [SRC-1AE03B9EC3-L000447](../../agents/web_agent.py#L447) | 447 | `"        warnings = result.setdefault(\"warnings\", [])"` | — |
| [SRC-1AE03B9EC3-L000448](../../agents/web_agent.py#L448) | 448 | `"        if isinstance(warnings, list) and warning not in warnings:"` | — |
| [SRC-1AE03B9EC3-L000449](../../agents/web_agent.py#L449) | 449 | `"            warnings.append(warning)"` | — |
| [SRC-1AE03B9EC3-L000450](../../agents/web_agent.py#L450) | 450 | `"    else:"` | — |
| [SRC-1AE03B9EC3-L000451](../../agents/web_agent.py#L451) | 451 | `"        result[\"answer_was_withheld\"] = False"` | — |
| [SRC-1AE03B9EC3-L000452](../../agents/web_agent.py#L452) | 452 | `"        result[\"answer_completeness_status\"] = ("` | — |
| [SRC-1AE03B9EC3-L000453](../../agents/web_agent.py#L453) | 453 | `"            \"no_lexical_gaps_detected_semantic_completeness_not_proven\""` | — |
| [SRC-1AE03B9EC3-L000454](../../agents/web_agent.py#L454) | 454 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000455](../../agents/web_agent.py#L455) | 455 | `"    return result"` | — |
| [SRC-1AE03B9EC3-L000456](../../agents/web_agent.py#L456) | 456 | `""` | — |
| [SRC-1AE03B9EC3-L000457](../../agents/web_agent.py#L457) | 457 | `""` | — |
| [SRC-1AE03B9EC3-L000458](../../agents/web_agent.py#L458) | 458 | `"class WebAgent:"` | — |
| [SRC-1AE03B9EC3-L000459](../../agents/web_agent.py#L459) | 459 | `"    \"\"\"Search, inspect, and synthesize web evidence for open-ended questions.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000460](../../agents/web_agent.py#L460) | 460 | `""` | — |
| [SRC-1AE03B9EC3-L000461](../../agents/web_agent.py#L461) | 461 | `"    def __init__(self) -> None:"` | — |
| [SRC-1AE03B9EC3-L000462](../../agents/web_agent.py#L462) | 462 | `"        self.api_key = ("` | — |
| [SRC-1AE03B9EC3-L000463](../../agents/web_agent.py#L463) | 463 | `"            os.getenv(\"OMARAI_LLM_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000464](../../agents/web_agent.py#L464) | 464 | `"            or os.getenv(\"OPENROUTER_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000465](../../agents/web_agent.py#L465) | 465 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000466](../../agents/web_agent.py#L466) | 466 | `"        self.base_url = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000467](../../agents/web_agent.py#L467) | 467 | `"            \"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\""` | — |
| [SRC-1AE03B9EC3-L000468](../../agents/web_agent.py#L468) | 468 | `"        ).strip().rstrip(\"/\")"` | — |
| [SRC-1AE03B9EC3-L000469](../../agents/web_agent.py#L469) | 469 | `"        # Pin explicit role models for more consistent behaviour than a random free router."` | — |
| [SRC-1AE03B9EC3-L000470](../../agents/web_agent.py#L470) | 470 | `"        # OMARAI_LLM_MODEL remains a global override for users who want one model everywhere."` | — |
| [SRC-1AE03B9EC3-L000471](../../agents/web_agent.py#L471) | 471 | `"        global_model = os.getenv(\"OMARAI_LLM_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000472](../../agents/web_agent.py#L472) | 472 | `"        self.answer_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000473](../../agents/web_agent.py#L473) | 473 | `"            \"OMARAI_ANSWER_MODEL\", global_model or \"google/gemma-4-31b-it:free\""` | — |
| [SRC-1AE03B9EC3-L000474](../../agents/web_agent.py#L474) | 474 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000475](../../agents/web_agent.py#L475) | 475 | `"        self.planner_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000476](../../agents/web_agent.py#L476) | 476 | `"            \"OMARAI_PLANNER_MODEL\","` | — |
| [SRC-1AE03B9EC3-L000477](../../agents/web_agent.py#L477) | 477 | `"            global_model or \"nvidia/nemotron-3-ultra-550b-a55b:free\","` | — |
| [SRC-1AE03B9EC3-L000478](../../agents/web_agent.py#L478) | 478 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000479](../../agents/web_agent.py#L479) | 479 | `"        self.review_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000480](../../agents/web_agent.py#L480) | 480 | `"            \"OMARAI_REVIEW_MODEL\", self.answer_model"` | — |
| [SRC-1AE03B9EC3-L000481](../../agents/web_agent.py#L481) | 481 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000482](../../agents/web_agent.py#L482) | 482 | `"        self.fallback_model = os.getenv("` | — |
| [SRC-1AE03B9EC3-L000483](../../agents/web_agent.py#L483) | 483 | `"            \"OMARAI_LLM_FALLBACK_MODEL\", \"openrouter/free\""` | — |
| [SRC-1AE03B9EC3-L000484](../../agents/web_agent.py#L484) | 484 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L000485](../../agents/web_agent.py#L485) | 485 | `"        self.model = self.answer_model  # Backwards-compatible alias."` | — |
| [SRC-1AE03B9EC3-L000486](../../agents/web_agent.py#L486) | 486 | `"        self.model_usage: list[dict[str, str]] = []"` | — |
| [SRC-1AE03B9EC3-L000487](../../agents/web_agent.py#L487) | 487 | `"        # Per-answer, bounded diagnostics contain only model identifiers and status metadata."` | — |
| [SRC-1AE03B9EC3-L000488](../../agents/web_agent.py#L488) | 488 | `"        # They intentionally exclude prompts, generated text, and provider response bodies."` | — |
| [SRC-1AE03B9EC3-L000489](../../agents/web_agent.py#L489) | 489 | `"        self.generation_diagnostics: list[dict[str, str]] = []"` | — |
| [SRC-1AE03B9EC3-L000490](../../agents/web_agent.py#L490) | 490 | `"        self.server_search_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L000491](../../agents/web_agent.py#L491) | 491 | `"        self._provider_diagnostics: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L000492](../../agents/web_agent.py#L492) | 492 | `"        self._provider_diagnostics_lock = threading.Lock()"` | — |
| [SRC-1AE03B9EC3-L000493](../../agents/web_agent.py#L493) | 493 | `"        self._deepseek_budget_lock = threading.Lock()"` | — |
| [SRC-1AE03B9EC3-L000494](../../agents/web_agent.py#L494) | 494 | `"        self._deepseek_search_requests_reserved = 0"` | — |
| [SRC-1AE03B9EC3-L000495](../../agents/web_agent.py#L495) | 495 | `"        self.openrouter_web_search_enabled = ("` | — |
| [SRC-1AE03B9EC3-L000496](../../agents/web_agent.py#L496) | 496 | `"            os.getenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"\").strip() == \"1\""` | — |
| [SRC-1AE03B9EC3-L000497](../../agents/web_agent.py#L497) | 497 | `"            and \"openrouter.ai\" in self.base_url.lower()"` | — |
| [SRC-1AE03B9EC3-L000498](../../agents/web_agent.py#L498) | 498 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000499](../../agents/web_agent.py#L499) | 499 | `"        self.timeout = max("` | — |
| [SRC-1AE03B9EC3-L000500](../../agents/web_agent.py#L500) | 500 | `"            5, min(int(os.getenv(\"OMARAI_LLM_TIMEOUT\", str(LLM_TIMEOUT_SECONDS))), 60)"` | — |
| [SRC-1AE03B9EC3-L000501](../../agents/web_agent.py#L501) | 501 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000502](../../agents/web_agent.py#L502) | 502 | `"        self._request_budget: RequestBudget \| None = None"` | — |
| [SRC-1AE03B9EC3-L000503](../../agents/web_agent.py#L503) | 503 | `""` | — |
| [SRC-1AE03B9EC3-L000504](../../agents/web_agent.py#L504) | 504 | `"    def _effective_timeout(self, configured_seconds: float) -> float:"` | — |
| [SRC-1AE03B9EC3-L000505](../../agents/web_agent.py#L505) | 505 | `"        \"\"\"Limit one outbound operation to the remaining per-answer time budget.\"\"\""` | — |
| [SRC-1AE03B9EC3-L000506](../../agents/web_agent.py#L506) | 506 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L000507](../../agents/web_agent.py#L507) | 507 | `"        if budget is None:"` | — |
| [SRC-1AE03B9EC3-L000508](../../agents/web_agent.py#L508) | 508 | `"            return float(configured_seconds)"` | — |
| [SRC-1AE03B9EC3-L000509](../../agents/web_agent.py#L509) | 509 | `"        return budget.timeout_for(configured_seconds)"` | — |
| [SRC-1AE03B9EC3-L000510](../../agents/web_agent.py#L510) | 510 | `""` | — |
| [SRC-1AE03B9EC3-L000511](../../agents/web_agent.py#L511) | 511 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000512](../../agents/web_agent.py#L512) | 512 | `"    def status() -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L000513](../../agents/web_agent.py#L513) | 513 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000514](../../agents/web_agent.py#L514) | 514 | `"            import bs4  # noqa: F401"` | — |
| [SRC-1AE03B9EC3-L000515](../../agents/web_agent.py#L515) | 515 | `"            import httpx  # noqa: F401"` | — |
| [SRC-1AE03B9EC3-L000516](../../agents/web_agent.py#L516) | 516 | `"            search_ready = True"` | — |
| [SRC-1AE03B9EC3-L000517](../../agents/web_agent.py#L517) | 517 | `"        except ImportError:"` | — |
| [SRC-1AE03B9EC3-L000518](../../agents/web_agent.py#L518) | 518 | `"            search_ready = False"` | — |
| [SRC-1AE03B9EC3-L000519](../../agents/web_agent.py#L519) | 519 | `""` | — |
| [SRC-1AE03B9EC3-L000520](../../agents/web_agent.py#L520) | 520 | `"        global_model = os.getenv(\"OMARAI_LLM_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000521](../../agents/web_agent.py#L521) | 521 | `"        answer_model = ("` | — |
| [SRC-1AE03B9EC3-L000522](../../agents/web_agent.py#L522) | 522 | `"            os.getenv(\"OMARAI_ANSWER_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000523](../../agents/web_agent.py#L523) | 523 | `"            or global_model"` | — |
| [SRC-1AE03B9EC3-L000524](../../agents/web_agent.py#L524) | 524 | `"            or \"google/gemma-4-31b-it:free\""` | — |
| [SRC-1AE03B9EC3-L000525](../../agents/web_agent.py#L525) | 525 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000526](../../agents/web_agent.py#L526) | 526 | `"        planner_model = ("` | — |
| [SRC-1AE03B9EC3-L000527](../../agents/web_agent.py#L527) | 527 | `"            os.getenv(\"OMARAI_PLANNER_MODEL\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000528](../../agents/web_agent.py#L528) | 528 | `"            or global_model"` | — |
| [SRC-1AE03B9EC3-L000529](../../agents/web_agent.py#L529) | 529 | `"            or \"nvidia/nemotron-3-ultra-550b-a55b:free\""` | — |
| [SRC-1AE03B9EC3-L000530](../../agents/web_agent.py#L530) | 530 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000531](../../agents/web_agent.py#L531) | 531 | `"        review_model = os.getenv(\"OMARAI_REVIEW_MODEL\", \"\").strip() or answer_model"` | — |
| [SRC-1AE03B9EC3-L000532](../../agents/web_agent.py#L532) | 532 | `"        fallback_model = ("` | — |
| [SRC-1AE03B9EC3-L000533](../../agents/web_agent.py#L533) | 533 | `"            os.getenv(\"OMARAI_LLM_FALLBACK_MODEL\", \"\").strip() or \"openrouter/free\""` | — |
| [SRC-1AE03B9EC3-L000534](../../agents/web_agent.py#L534) | 534 | `"        )"` | — |
| [SRC-1AE03B9EC3-L000535](../../agents/web_agent.py#L535) | 535 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L000536](../../agents/web_agent.py#L536) | 536 | `"            \"web_search_ready\": search_ready,"` | — |
| [SRC-1AE03B9EC3-L000537](../../agents/web_agent.py#L537) | 537 | `"            \"language_model_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000538](../../agents/web_agent.py#L538) | 538 | `"                os.getenv(\"OMARAI_LLM_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000539](../../agents/web_agent.py#L539) | 539 | `"                or os.getenv(\"OPENROUTER_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000540](../../agents/web_agent.py#L540) | 540 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000541](../../agents/web_agent.py#L541) | 541 | `"            \"language_model_provider\": os.getenv("` | — |
| [SRC-1AE03B9EC3-L000542](../../agents/web_agent.py#L542) | 542 | `"                \"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\""` | — |
| [SRC-1AE03B9EC3-L000543](../../agents/web_agent.py#L543) | 543 | `"            ).strip().rstrip(\"/\"),"` | — |
| [SRC-1AE03B9EC3-L000544](../../agents/web_agent.py#L544) | 544 | `"            \"default_model\": answer_model,"` | — |
| [SRC-1AE03B9EC3-L000545](../../agents/web_agent.py#L545) | 545 | `"            \"planner_model\": planner_model,"` | — |
| [SRC-1AE03B9EC3-L000546](../../agents/web_agent.py#L546) | 546 | `"            \"answer_model\": answer_model,"` | — |
| [SRC-1AE03B9EC3-L000547](../../agents/web_agent.py#L547) | 547 | `"            \"review_model\": review_model,"` | — |
| [SRC-1AE03B9EC3-L000548](../../agents/web_agent.py#L548) | 548 | `"            \"fallback_model\": fallback_model,"` | — |
| [SRC-1AE03B9EC3-L000549](../../agents/web_agent.py#L549) | 549 | `"            \"model_selection_mode\": \"role_specific_with_fallback\","` | — |
| [SRC-1AE03B9EC3-L000550](../../agents/web_agent.py#L550) | 550 | `"            \"external_model_privacy_notice\": ("` | — |
| [SRC-1AE03B9EC3-L000551](../../agents/web_agent.py#L551) | 551 | `"                \"Prompts and selected page excerpts are sent to the configured external model provider. \""` | — |
| [SRC-1AE03B9EC3-L000552](../../agents/web_agent.py#L552) | 552 | `"                \"Do not submit secrets or personal/confidential customer data. The default free NVIDIA \""` | — |
| [SRC-1AE03B9EC3-L000553](../../agents/web_agent.py#L553) | 553 | `"                \"Nemotron endpoint states that sessions may be logged for security and product improvement.\""` | — |
| [SRC-1AE03B9EC3-L000554](../../agents/web_agent.py#L554) | 554 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000555](../../agents/web_agent.py#L555) | 555 | `"            \"search_providers\": ["` | — |
| [SRC-1AE03B9EC3-L000556](../../agents/web_agent.py#L556) | 556 | `"                \"DuckDuckGo HTML\","` | — |
| [SRC-1AE03B9EC3-L000557](../../agents/web_agent.py#L557) | 557 | `"                \"Bing RSS\","` | — |
| [SRC-1AE03B9EC3-L000558](../../agents/web_agent.py#L558) | 558 | `"                \"Google News RSS for fresh queries\","` | — |
| [SRC-1AE03B9EC3-L000559](../../agents/web_agent.py#L559) | 559 | `"                \"DeepSeek Search API when DEEPSEEK_SEARCH_API_KEY is configured (optional; may incur charges)\","` | — |
| [SRC-1AE03B9EC3-L000560](../../agents/web_agent.py#L560) | 560 | `"                \"OpenRouter server-side live web search when OMARAI_OPENROUTER_WEB_SEARCH=1\","` | — |
| [SRC-1AE03B9EC3-L000561](../../agents/web_agent.py#L561) | 561 | `"                \"Brave Search API when BRAVE_SEARCH_API_KEY is configured\","` | — |
| [SRC-1AE03B9EC3-L000562](../../agents/web_agent.py#L562) | 562 | `"                \"Tavily Search API when TAVILY_API_KEY is configured\","` | — |
| [SRC-1AE03B9EC3-L000563](../../agents/web_agent.py#L563) | 563 | `"            ],"` | — |
| [SRC-1AE03B9EC3-L000564](../../agents/web_agent.py#L564) | 564 | `"            \"brave_search_api_configured\": bool(os.getenv(\"BRAVE_SEARCH_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000565](../../agents/web_agent.py#L565) | 565 | `"            \"deepseek_search_api_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000566](../../agents/web_agent.py#L566) | 566 | `"                os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000567](../../agents/web_agent.py#L567) | 567 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000568](../../agents/web_agent.py#L568) | 568 | `"            \"tavily_search_api_configured\": bool(os.getenv(\"TAVILY_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000569](../../agents/web_agent.py#L569) | 569 | `"            \"openrouter_web_search_enabled\": ("` | — |
| [SRC-1AE03B9EC3-L000570](../../agents/web_agent.py#L570) | 570 | `"                os.getenv(\"OMARAI_OPENROUTER_WEB_SEARCH\", \"\").strip() == \"1\""` | — |
| [SRC-1AE03B9EC3-L000571](../../agents/web_agent.py#L571) | 571 | `"                and \"openrouter.ai\" in os.getenv("` | — |
| [SRC-1AE03B9EC3-L000572](../../agents/web_agent.py#L572) | 572 | `"                    \"OMARAI_LLM_BASE_URL\", \"https://openrouter.ai/api/v1\""` | — |
| [SRC-1AE03B9EC3-L000573](../../agents/web_agent.py#L573) | 573 | `"                ).lower()"` | — |
| [SRC-1AE03B9EC3-L000574](../../agents/web_agent.py#L574) | 574 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000575](../../agents/web_agent.py#L575) | 575 | `"            \"public_social_sources\": ["` | — |
| [SRC-1AE03B9EC3-L000576](../../agents/web_agent.py#L576) | 576 | `"                \"Reddit public RSS and optional authorized Reddit OAuth search\","` | — |
| [SRC-1AE03B9EC3-L000577](../../agents/web_agent.py#L577) | 577 | `"                \"Bluesky public search\","` | — |
| [SRC-1AE03B9EC3-L000578](../../agents/web_agent.py#L578) | 578 | `"                \"indexed public pages from Facebook, Instagram, X, TikTok, LinkedIn, Threads and YouTube\","` | — |
| [SRC-1AE03B9EC3-L000579](../../agents/web_agent.py#L579) | 579 | `"                \"official Instagram public hashtag media when an authorized Graph API token is configured\","` | — |
| [SRC-1AE03B9EC3-L000580](../../agents/web_agent.py#L580) | 580 | `"                \"configured Facebook Pages when a valid authorized page token is configured\","` | — |
| [SRC-1AE03B9EC3-L000581](../../agents/web_agent.py#L581) | 581 | `"                \"official X recent-post API when X_BEARER_TOKEN is configured\","` | — |
| [SRC-1AE03B9EC3-L000582](../../agents/web_agent.py#L582) | 582 | `"            ],"` | — |
| [SRC-1AE03B9EC3-L000583](../../agents/web_agent.py#L583) | 583 | `"            \"reddit_oauth_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000584](../../agents/web_agent.py#L584) | 584 | `"                os.getenv(\"REDDIT_CLIENT_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000585](../../agents/web_agent.py#L585) | 585 | `"                and os.getenv(\"REDDIT_CLIENT_SECRET\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000586](../../agents/web_agent.py#L586) | 586 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000587](../../agents/web_agent.py#L587) | 587 | `"            \"facebook_pages_api_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000588](../../agents/web_agent.py#L588) | 588 | `"                os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000589](../../agents/web_agent.py#L589) | 589 | `"                and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000590](../../agents/web_agent.py#L590) | 590 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000591](../../agents/web_agent.py#L591) | 591 | `"            \"x_api_configured\": bool(os.getenv(\"X_BEARER_TOKEN\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000592](../../agents/web_agent.py#L592) | 592 | `"            \"instagram_graph_api_configured\": bool("` | — |
| [SRC-1AE03B9EC3-L000593](../../agents/web_agent.py#L593) | 593 | `"                os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000594](../../agents/web_agent.py#L594) | 594 | `"                and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L000595](../../agents/web_agent.py#L595) | 595 | `"            ),"` | — |
| [SRC-1AE03B9EC3-L000596](../../agents/web_agent.py#L596) | 596 | `"            \"meta_graph_version\": os.getenv(\"META_GRAPH_VERSION\", \"v25.0\").strip(),"` | — |
| [SRC-1AE03B9EC3-L000597](../../agents/web_agent.py#L597) | 597 | `"            \"youtube_api_configured\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000598](../../agents/web_agent.py#L598) | 598 | `"            \"youtube_direct_api\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L000599](../../agents/web_agent.py#L599) | 599 | `"            \"verification_scope\": {"` | — |
| [SRC-1AE03B9EC3-L000600](../../agents/web_agent.py#L600) | 600 | `"                \"kind\": \"configuration_snapshot\","` | — |
| [SRC-1AE03B9EC3-L000601](../../agents/web_agent.py#L601) | 601 | `"                \"live_network_checks_performed\": False,"` | — |
| [SRC-1AE03B9EC3-L000602](../../agents/web_agent.py#L602) | 602 | `"                \"web_search_ready_means\": \"dependencies_importable_not_provider_connectivity\","` | — |
| [SRC-1AE03B9EC3-L000603](../../agents/web_agent.py#L603) | 603 | `"                \"language_model_configured_means\": \"credential_present_not_successful_completion\","` | — |
| [SRC-1AE03B9EC3-L000604](../../agents/web_agent.py#L604) | 604 | `"                \"search_providers_means\": \"supported_or_conditionally_configured_not_live_verified\","` | — |
| [SRC-1AE03B9EC3-L000605](../../agents/web_agent.py#L605) | 605 | `"                \"direct_social_api_flags_mean\": \"credentials_present_not_permissions_or_connectivity_verified\","` | — |
| [SRC-1AE03B9EC3-L000606](../../agents/web_agent.py#L606) | 606 | `"                \"live_diagnostics_endpoint\": \"POST /api/diagnostics\","` | — |
| [SRC-1AE03B9EC3-L000607](../../agents/web_agent.py#L607) | 607 | `"            },"` | — |
| [SRC-1AE03B9EC3-L000608](../../agents/web_agent.py#L608) | 608 | `"        }"` | — |
| [SRC-1AE03B9EC3-L000609](../../agents/web_agent.py#L609) | 609 | `""` | — |
| [SRC-1AE03B9EC3-L000610](../../agents/web_agent.py#L610) | 610 | `"    @staticmethod"` | — |
| [SRC-1AE03B9EC3-L000611](../../agents/web_agent.py#L611) | 611 | `"    def _unwrap_search_url(value: str) -> str:"` | — |
| [SRC-1AE03B9EC3-L000612](../../agents/web_agent.py#L612) | 612 | `"        if value.startswith(\"//\"):"` | — |
| [SRC-1AE03B9EC3-L000613](../../agents/web_agent.py#L613) | 613 | `"            value = \"https:\" + value"` | — |
| [SRC-1AE03B9EC3-L000614](../../agents/web_agent.py#L614) | 614 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L000615](../../agents/web_agent.py#L615) | 615 | `"            parsed = urllib.parse.urlparse(value)"` | — |
| [SRC-1AE03B9EC3-L000616](../../agents/web_agent.py#L616) | 616 | `"            host = (parsed.hostname or \"\").lower()"` | — |
| [SRC-1AE03B9EC3-L000617](../../agents/web_agent.py#L617) | 617 | `"            if host.endswith(\"duckduckgo.com\") and parsed.path.startswith(\"/l/\"):"` | — |
| [SRC-1AE03B9EC3-L000618](../../agents/web_agent.py#L618) | 618 | `"                target = urllib.parse.parse_qs(parsed.query).get(\"uddg\", [\"\"])[0]"` | — |
| [SRC-1AE03B9EC3-L000619](../../agents/web_agent.py#L619) | 619 | `"                return urllib.parse.unquote(target) if target else \"\""` | — |
| [SRC-1AE03B9EC3-L000620](../../agents/web_agent.py#L620) | 620 | `"        except (ValueError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L000621](../../agents/web_agent.py#L621) | 621 | `"            return \"\""` | — |
| [SRC-1AE03B9EC3-L000622](../../agents/web_agent.py#L622) | 622 | `"        return value"` | — |
| [SRC-1AE03B9EC3-L000623](../../agents/web_agent.py#L623) | 623 | `""` | — |
| [SRC-1AE03B9EC3-L000624](../../agents/web_agent.py#L624) | 624 | `"    def _record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L000625](../../agents/web_agent.py#L625) | 625 | `"        self, provider: str, query: str, status: str, result_count: int = 0,"` | — |
| [SRC-1AE03B9EC3-L000626](../../agents/web_agent.py#L626) | 626 | `"        rejected_count: int = 0, error: str \| None = None,"` | — |
| [SRC-1AE03B9EC3-L000627](../../agents/web_agent.py#L627) | 627 | `"        accepted_count: int \| None = None,"` | — |
| [SRC-1AE03B9EC3-L000628](../../agents/web_agent.py#L628) | 628 | `"        rejection_counts: dict[str, int] \| None = None,"` | — |
| [SRC-1AE03B9EC3-L000629](../../agents/web_agent.py#L629) | 629 | `"    ) -> None:"` | — |
| [SRC-1AE03B9EC3-L000630](../../agents/web_agent.py#L630) | 630 | `"        def redact(value: Any, limit: int) -> str:"` | — |
| [SRC-1AE03B9EC3-L000631](../../agents/web_agent.py#L631) | 631 | `"            safe = _clean_text(str(value or \"\"), limit)"` | — |
| [SRC-1AE03B9EC3-L000632](../../agents/web_agent.py#L632) | 632 | `"            safe = re.sub("` | — |
| [SRC-1AE03B9EC3-L000633](../../agents/web_agent.py#L633) | 633 | `"                r\"(?i)(bearer\\s+)[A-Za-z0-9._~+/-]+=*\","` | — |
| [SRC-1AE03B9EC3-L000634](../../agents/web_agent.py#L634) | 634 | `"                r\"\\1[REDACTED]\","` | — |
| [SRC-1AE03B9EC3-L000635](../../agents/web_agent.py#L635) | 635 | `"                safe,"` | — |
| [SRC-1AE03B9EC3-L000636](../../agents/web_agent.py#L636) | 636 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000637](../../agents/web_agent.py#L637) | 637 | `"            safe = re.sub("` | — |
| [SRC-1AE03B9EC3-L000638](../../agents/web_agent.py#L638) | 638 | `"                r\"(?i)\\b(api[_-]?key\|access[_-]?token\|refresh[_-]?token\|token\|secret\|password)\\s*[:=]\\s*[^\\s,;]+\","` | — |
| [SRC-1AE03B9EC3-L000639](../../agents/web_agent.py#L639) | 639 | `"                r\"\\1=[REDACTED]\","` | — |
| [SRC-1AE03B9EC3-L000640](../../agents/web_agent.py#L640) | 640 | `"                safe,"` | — |
| [SRC-1AE03B9EC3-L000641](../../agents/web_agent.py#L641) | 641 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000642](../../agents/web_agent.py#L642) | 642 | `"            safe = re.sub("` | — |
| [SRC-1AE03B9EC3-L000643](../../agents/web_agent.py#L643) | 643 | `"                r\"(?i)([?&](?:api[_-]?key\|access[_-]?token\|token\|key)=)[^&\\s]+\","` | — |
| [SRC-1AE03B9EC3-L000644](../../agents/web_agent.py#L644) | 644 | `"                r\"\\1[REDACTED]\","` | — |
| [SRC-1AE03B9EC3-L000645](../../agents/web_agent.py#L645) | 645 | `"                safe,"` | — |
| [SRC-1AE03B9EC3-L000646](../../agents/web_agent.py#L646) | 646 | `"            )"` | — |
| [SRC-1AE03B9EC3-L000647](../../agents/web_agent.py#L647) | 647 | `"            return safe[:limit]"` | — |
| [SRC-1AE03B9EC3-L000648](../../agents/web_agent.py#L648) | 648 | `""` | — |
| [SRC-1AE03B9EC3-L000649](../../agents/web_agent.py#L649) | 649 | `"        record = {"` | — |
| [SRC-1AE03B9EC3-L000650](../../agents/web_agent.py#L650) | 650 | `"            \"provider\": provider,"` | — |
| [SRC-1AE03B9EC3-L000651](../../agents/web_agent.py#L651) | 651 | `"            \"query\": redact(query, 220),"` | — |
| [SRC-1AE03B9EC3-L000652](../../agents/web_agent.py#L652) | 652 | `"            \"status\": status,"` | — |
| [SRC-1AE03B9EC3-L000653](../../agents/web_agent.py#L653) | 653 | `"            \"result_count\": int(result_count),"` | — |
| [SRC-1AE03B9EC3-L000654](../../agents/web_agent.py#L654) | 654 | `"            \"accepted_count\": int(result_count if accepted_count is None else accepted_count),"` | — |
| [SRC-1AE03B9EC3-L000655](../../agents/web_agent.py#L655) | 655 | `"            \"rejected_count\": int(rejected_count),"` | — |
| [SRC-1AE03B9EC3-L000656](../../agents/web_agent.py#L656) | 656 | `"        }"` | — |
| [SRC-1AE03B9EC3-L000657](../../agents/web_agent.py#L657) | 657 | `"        if isinstance(rejection_counts, dict):"` | — |
| [SRC-1AE03B9EC3-L000658](../../agents/web_agent.py#L658) | 658 | `"            safe_counts: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L000659](../../agents/web_agent.py#L659) | 659 | `"            for reason in _PROVIDER_REJECTION_REASONS:"` | — |
| [SRC-1AE03B9EC3-L000660](../../agents/web_agent.py#L660) | 660 | `"                try:"` | — |
| [SRC-1AE03B9EC3-L000661](../../agents/web_agent.py#L661) | 661 | `"                    safe_counts[reason] = max(0, int(rejection_counts.get(reason, 0) or 0))"` | — |
| [SRC-1AE03B9EC3-L000662](../../agents/web_agent.py#L662) | 662 | `"                except (TypeError, ValueError, OverflowError):"` | — |
| [SRC-1AE03B9EC3-L000663](../../agents/web_agent.py#L663) | 663 | `"                    safe_counts[reason] = 0"` | — |
| [SRC-1AE03B9EC3-L000664](../../agents/web_agent.py#L664) | 664 | `"            record[\"rejection_counts\"] = safe_counts"` | — |
