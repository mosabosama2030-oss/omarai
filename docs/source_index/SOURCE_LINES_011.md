# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **011**
- سجلات الأسطر: **800**
- النطاق: SRC-E599346ABE-L001101 إلى SRC-E599346ABE-L001900
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-E599346ABE — [docs/generate_index.py](../generate_index.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E599346ABE-L001101](../generate_index.py#L1101) | 1101 | `"                i += 2"` | — |
| [SRC-E599346ABE-L001102](../generate_index.py#L1102) | 1102 | `"                continue"` | — |
| [SRC-E599346ABE-L001103](../generate_index.py#L1103) | 1103 | `""` | — |
| [SRC-E599346ABE-L001104](../generate_index.py#L1104) | 1104 | `"            if hash_comments and ch == \"#\" and (i == 0 or line[i - 1].isspace()):"` | — |
| [SRC-E599346ABE-L001105](../generate_index.py#L1105) | 1105 | `"                _append_comment_text(comments, line_number, line[i + 1:].rstrip(\"\\r\\n\"))"` | — |
| [SRC-E599346ABE-L001106](../generate_index.py#L1106) | 1106 | `"                break"` | — |
| [SRC-E599346ABE-L001107](../generate_index.py#L1107) | 1107 | `"            i += 1"` | — |
| [SRC-E599346ABE-L001108](../generate_index.py#L1108) | 1108 | `""` | — |
| [SRC-E599346ABE-L001109](../generate_index.py#L1109) | 1109 | `"        if quote in (\"'\", '\"') and not line.rstrip(\"\\r\\n\").endswith(\"\\\\\"):"` | — |
| [SRC-E599346ABE-L001110](../generate_index.py#L1110) | 1110 | `"            quote = None"` | — |
| [SRC-E599346ABE-L001111](../generate_index.py#L1111) | 1111 | `""` | — |
| [SRC-E599346ABE-L001112](../generate_index.py#L1112) | 1112 | `"    return comments"` | — |
| [SRC-E599346ABE-L001113](../generate_index.py#L1113) | 1113 | `""` | — |
| [SRC-E599346ABE-L001114](../generate_index.py#L1114) | 1114 | `""` | — |
| [SRC-E599346ABE-L001115](../generate_index.py#L1115) | 1115 | `"def _html_comment_map(source: str) -> dict[int, list[str]]:"` | — |
| [SRC-E599346ABE-L001116](../generate_index.py#L1116) | 1116 | `"    \"\"\"Return HTML comments while ignoring HTML-looking text inside script/style blocks.\"\"\""` | — |
| [SRC-E599346ABE-L001117](../generate_index.py#L1117) | 1117 | `"    comments: dict[int, list[str]] = {}"` | — |
| [SRC-E599346ABE-L001118](../generate_index.py#L1118) | 1118 | `"    masked_chars = list(source)"` | — |
| [SRC-E599346ABE-L001119](../generate_index.py#L1119) | 1119 | `"    for pattern in (HTML_SCRIPT_RE, HTML_STYLE_RE):"` | — |
| [SRC-E599346ABE-L001120](../generate_index.py#L1120) | 1120 | `"        for match in pattern.finditer(source):"` | — |
| [SRC-E599346ABE-L001121](../generate_index.py#L1121) | 1121 | `"            for position in range(match.start(), match.end()):"` | — |
| [SRC-E599346ABE-L001122](../generate_index.py#L1122) | 1122 | `"                if masked_chars[position] != \"\\\\n\":"` | — |
| [SRC-E599346ABE-L001123](../generate_index.py#L1123) | 1123 | `"                    masked_chars[position] = \" \""` | — |
| [SRC-E599346ABE-L001124](../generate_index.py#L1124) | 1124 | `"    masked_source = \"\".join(masked_chars)"` | — |
| [SRC-E599346ABE-L001125](../generate_index.py#L1125) | 1125 | `"    comment_re = re.compile(r\"<!--(.*?)-->\", re.DOTALL)"` | — |
| [SRC-E599346ABE-L001126](../generate_index.py#L1126) | 1126 | `"    for match in comment_re.finditer(masked_source):"` | — |
| [SRC-E599346ABE-L001127](../generate_index.py#L1127) | 1127 | `"        starting_line = _line_at(source, match.start(1))"` | — |
| [SRC-E599346ABE-L001128](../generate_index.py#L1128) | 1128 | `"        _append_comment_text("` | — |
| [SRC-E599346ABE-L001129](../generate_index.py#L1129) | 1129 | `"            comments,"` | — |
| [SRC-E599346ABE-L001130](../generate_index.py#L1130) | 1130 | `"            starting_line,"` | — |
| [SRC-E599346ABE-L001131](../generate_index.py#L1131) | 1131 | `"            source[match.start(1):match.end(1)],"` | — |
| [SRC-E599346ABE-L001132](../generate_index.py#L1132) | 1132 | `"        )"` | — |
| [SRC-E599346ABE-L001133](../generate_index.py#L1133) | 1133 | `"    return comments"` | — |
| [SRC-E599346ABE-L001134](../generate_index.py#L1134) | 1134 | `""` | — |
| [SRC-E599346ABE-L001135](../generate_index.py#L1135) | 1135 | `""` | — |
| [SRC-E599346ABE-L001136](../generate_index.py#L1136) | 1136 | `"def _markdown_annotation_map(source: str) -> dict[int, list[str]]:"` | — |
| [SRC-E599346ABE-L001137](../generate_index.py#L1137) | 1137 | `"    \"\"\"Accept explicit annotations at the start of Markdown prose, skipping fenced code.\"\"\""` | — |
| [SRC-E599346ABE-L001138](../generate_index.py#L1138) | 1138 | `"    comments: dict[int, list[str]] = {}"` | — |
| [SRC-E599346ABE-L001139](../generate_index.py#L1139) | 1139 | `"    in_fence = False"` | — |
| [SRC-E599346ABE-L001140](../generate_index.py#L1140) | 1140 | `"    fence_character = \"\""` | — |
| [SRC-E599346ABE-L001141](../generate_index.py#L1141) | 1141 | `"    fence_width = 0"` | — |
| [SRC-E599346ABE-L001142](../generate_index.py#L1142) | 1142 | `"    marker_start_re = re.compile("` | — |
| [SRC-E599346ABE-L001143](../generate_index.py#L1143) | 1143 | `"        rf\"^\\s*(?:(?:[-*+]\|>)\\s*)?({_FINDING_MARKER_ALTERNATION})\\s*:\\s*(.*)$\""` | — |
| [SRC-E599346ABE-L001144](../generate_index.py#L1144) | 1144 | `"    )"` | — |
| [SRC-E599346ABE-L001145](../generate_index.py#L1145) | 1145 | `"    for line_number, line in enumerate(source.splitlines(), start=1):"` | — |
| [SRC-E599346ABE-L001146](../generate_index.py#L1146) | 1146 | `"        fence_match = re.match(r\"^\\s*(~{3,})\", line) or re.match("` | — |
| [SRC-E599346ABE-L001147](../generate_index.py#L1147) | 1147 | `"            r\"^\\s*(\" + re.escape(chr(96)) + \"{3,})\", line"` | — |
| [SRC-E599346ABE-L001148](../generate_index.py#L1148) | 1148 | `"        )"` | — |
| [SRC-E599346ABE-L001149](../generate_index.py#L1149) | 1149 | `"        if fence_match:"` | — |
| [SRC-E599346ABE-L001150](../generate_index.py#L1150) | 1150 | `"            fence = fence_match.group(1)"` | — |
| [SRC-E599346ABE-L001151](../generate_index.py#L1151) | 1151 | `"            if not in_fence:"` | — |
| [SRC-E599346ABE-L001152](../generate_index.py#L1152) | 1152 | `"                in_fence = True"` | — |
| [SRC-E599346ABE-L001153](../generate_index.py#L1153) | 1153 | `"                fence_character = fence[0]"` | — |
| [SRC-E599346ABE-L001154](../generate_index.py#L1154) | 1154 | `"                fence_width = len(fence)"` | — |
| [SRC-E599346ABE-L001155](../generate_index.py#L1155) | 1155 | `"            elif fence[0] == fence_character and len(fence) >= fence_width:"` | — |
| [SRC-E599346ABE-L001156](../generate_index.py#L1156) | 1156 | `"                in_fence = False"` | — |
| [SRC-E599346ABE-L001157](../generate_index.py#L1157) | 1157 | `"            continue"` | — |
| [SRC-E599346ABE-L001158](../generate_index.py#L1158) | 1158 | `"        if in_fence:"` | — |
| [SRC-E599346ABE-L001159](../generate_index.py#L1159) | 1159 | `"            continue"` | — |
| [SRC-E599346ABE-L001160](../generate_index.py#L1160) | 1160 | `"        match = marker_start_re.match(line)"` | — |
| [SRC-E599346ABE-L001161](../generate_index.py#L1161) | 1161 | `"        if match:"` | — |
| [SRC-E599346ABE-L001162](../generate_index.py#L1162) | 1162 | `"            comments.setdefault(line_number, []).append("` | — |
| [SRC-E599346ABE-L001163](../generate_index.py#L1163) | 1163 | `"                f\"{match.group(1)}: {match.group(2)}\""` | — |
| [SRC-E599346ABE-L001164](../generate_index.py#L1164) | 1164 | `"            )"` | — |
| [SRC-E599346ABE-L001165](../generate_index.py#L1165) | 1165 | `"    return comments"` | — |
| [SRC-E599346ABE-L001166](../generate_index.py#L1166) | 1166 | `""` | — |
| [SRC-E599346ABE-L001167](../generate_index.py#L1167) | 1167 | `""` | — |
| [SRC-E599346ABE-L001168](../generate_index.py#L1168) | 1168 | `"def _finding_comments_by_file(relative_file: str, source: str) -> dict[int, list[str]]:"` | — |
| [SRC-E599346ABE-L001169](../generate_index.py#L1169) | 1169 | `"    \"\"\"Extract intended comment/prose annotations by file type, not arbitrary tokens.\"\"\""` | — |
| [SRC-E599346ABE-L001170](../generate_index.py#L1170) | 1170 | `"    path = Path(relative_file)"` | — |
| [SRC-E599346ABE-L001171](../generate_index.py#L1171) | 1171 | `"    suffix = path.suffix.lower()"` | — |
| [SRC-E599346ABE-L001172](../generate_index.py#L1172) | 1172 | `"    name = path.name.lower()"` | — |
| [SRC-E599346ABE-L001173](../generate_index.py#L1173) | 1173 | `"    if suffix == \".py\":"` | — |
| [SRC-E599346ABE-L001174](../generate_index.py#L1174) | 1174 | `"        return _python_comment_map(source)"` | — |
| [SRC-E599346ABE-L001175](../generate_index.py#L1175) | 1175 | `"    if suffix in JAVASCRIPT_EXTENSIONS \| CSS_EXTENSIONS:"` | — |
| [SRC-E599346ABE-L001176](../generate_index.py#L1176) | 1176 | `"        return _c_style_comment_map(source, hash_comments=suffix == \".scss\")"` | — |
| [SRC-E599346ABE-L001177](../generate_index.py#L1177) | 1177 | `"    if suffix in {\".html\", \".htm\"}:"` | — |
| [SRC-E599346ABE-L001178](../generate_index.py#L1178) | 1178 | `"        comments = _html_comment_map(source)"` | — |
| [SRC-E599346ABE-L001179](../generate_index.py#L1179) | 1179 | `"        for pattern in (HTML_SCRIPT_RE, HTML_STYLE_RE):"` | — |
| [SRC-E599346ABE-L001180](../generate_index.py#L1180) | 1180 | `"            for match in pattern.finditer(source):"` | — |
| [SRC-E599346ABE-L001181](../generate_index.py#L1181) | 1181 | `"                embedded = match.group(1)"` | — |
| [SRC-E599346ABE-L001182](../generate_index.py#L1182) | 1182 | `"                local_comments = _c_style_comment_map(embedded)"` | — |
| [SRC-E599346ABE-L001183](../generate_index.py#L1183) | 1183 | `"                base_line = _line_at(source, match.start(1))"` | — |
| [SRC-E599346ABE-L001184](../generate_index.py#L1184) | 1184 | `"                for local_line, fragments in local_comments.items():"` | — |
| [SRC-E599346ABE-L001185](../generate_index.py#L1185) | 1185 | `"                    for fragment in fragments:"` | — |
| [SRC-E599346ABE-L001186](../generate_index.py#L1186) | 1186 | `"                        comments.setdefault(base_line + local_line - 1, []).append(fragment)"` | — |
| [SRC-E599346ABE-L001187](../generate_index.py#L1187) | 1187 | `"        return comments"` | — |
| [SRC-E599346ABE-L001188](../generate_index.py#L1188) | 1188 | `"    if suffix in {\".md\", \".rst\"}:"` | — |
| [SRC-E599346ABE-L001189](../generate_index.py#L1189) | 1189 | `"        return _markdown_annotation_map(source)"` | — |
| [SRC-E599346ABE-L001190](../generate_index.py#L1190) | 1190 | `"    if suffix in {\".yml\", \".yaml\", \".toml\", \".ini\", \".cfg\", \".sh\"} or name in {"` | — |
| [SRC-E599346ABE-L001191](../generate_index.py#L1191) | 1191 | `"        \"dockerfile\","` | — |
| [SRC-E599346ABE-L001192](../generate_index.py#L1192) | 1192 | `"        \"makefile\","` | — |
| [SRC-E599346ABE-L001193](../generate_index.py#L1193) | 1193 | `"        \"procfile\","` | — |
| [SRC-E599346ABE-L001194](../generate_index.py#L1194) | 1194 | `"    }:"` | — |
| [SRC-E599346ABE-L001195](../generate_index.py#L1195) | 1195 | `"        return _c_style_comment_map(source, hash_comments=True)"` | — |
| [SRC-E599346ABE-L001196](../generate_index.py#L1196) | 1196 | `"    if suffix == \".txt\":"` | — |
| [SRC-E599346ABE-L001197](../generate_index.py#L1197) | 1197 | `"        return _markdown_annotation_map(source)"` | — |
| [SRC-E599346ABE-L001198](../generate_index.py#L1198) | 1198 | `"    return {}"` | — |
| [SRC-E599346ABE-L001199](../generate_index.py#L1199) | 1199 | `""` | — |
| [SRC-E599346ABE-L001200](../generate_index.py#L1200) | 1200 | `""` | — |
| [SRC-E599346ABE-L001201](../generate_index.py#L1201) | 1201 | `"def scan_finding_annotations(source_lines: list[IndexedLine]) -> list[IndexedFinding]:"` | — |
| [SRC-E599346ABE-L001202](../generate_index.py#L1202) | 1202 | `"    \"\"\"Index explicit comments/prose annotations, not incidental words in source code.\"\"\""` | — |
| [SRC-E599346ABE-L001203](../generate_index.py#L1203) | 1203 | `"    findings: list[IndexedFinding] = []"` | — |
| [SRC-E599346ABE-L001204](../generate_index.py#L1204) | 1204 | `"    by_file: dict[str, list[IndexedLine]] = {}"` | — |
| [SRC-E599346ABE-L001205](../generate_index.py#L1205) | 1205 | `"    for source_line in source_lines:"` | — |
| [SRC-E599346ABE-L001206](../generate_index.py#L1206) | 1206 | `"        by_file.setdefault(source_line.file, []).append(source_line)"` | — |
| [SRC-E599346ABE-L001207](../generate_index.py#L1207) | 1207 | `""` | — |
| [SRC-E599346ABE-L001208](../generate_index.py#L1208) | 1208 | `"    for relative_file, records in by_file.items():"` | — |
| [SRC-E599346ABE-L001209](../generate_index.py#L1209) | 1209 | `"        records.sort(key=lambda item: item.line)"` | — |
| [SRC-E599346ABE-L001210](../generate_index.py#L1210) | 1210 | `"        source = \"\\n\".join(item.content for item in records)"` | — |
| [SRC-E599346ABE-L001211](../generate_index.py#L1211) | 1211 | `"        comments = _finding_comments_by_file(relative_file, source)"` | — |
| [SRC-E599346ABE-L001212](../generate_index.py#L1212) | 1212 | `"        record_by_line = {item.line: item for item in records}"` | — |
| [SRC-E599346ABE-L001213](../generate_index.py#L1213) | 1213 | `""` | — |
| [SRC-E599346ABE-L001214](../generate_index.py#L1214) | 1214 | `"        for line_number, fragments in comments.items():"` | — |
| [SRC-E599346ABE-L001215](../generate_index.py#L1215) | 1215 | `"            source_line = record_by_line.get(line_number)"` | — |
| [SRC-E599346ABE-L001216](../generate_index.py#L1216) | 1216 | `"            if source_line is None:"` | — |
| [SRC-E599346ABE-L001217](../generate_index.py#L1217) | 1217 | `"                continue"` | — |
| [SRC-E599346ABE-L001218](../generate_index.py#L1218) | 1218 | `"            matches = ["` | — |
| [SRC-E599346ABE-L001219](../generate_index.py#L1219) | 1219 | `"                match"` | — |
| [SRC-E599346ABE-L001220](../generate_index.py#L1220) | 1220 | `"                for fragment in fragments"` | — |
| [SRC-E599346ABE-L001221](../generate_index.py#L1221) | 1221 | `"                for match in FINDING_MARKER_RE.finditer("` | — |
| [SRC-E599346ABE-L001222](../generate_index.py#L1222) | 1222 | `"                    fragment.lstrip().lstrip(\"*\").strip()"` | — |
| [SRC-E599346ABE-L001223](../generate_index.py#L1223) | 1223 | `"                )"` | — |
| [SRC-E599346ABE-L001224](../generate_index.py#L1224) | 1224 | `"            ]"` | — |
| [SRC-E599346ABE-L001225](../generate_index.py#L1225) | 1225 | `"            if not matches:"` | — |
| [SRC-E599346ABE-L001226](../generate_index.py#L1226) | 1226 | `"                continue"` | — |
| [SRC-E599346ABE-L001227](../generate_index.py#L1227) | 1227 | `"            totals: dict[str, int] = {}"` | — |
| [SRC-E599346ABE-L001228](../generate_index.py#L1228) | 1228 | `"            for match in matches:"` | — |
| [SRC-E599346ABE-L001229](../generate_index.py#L1229) | 1229 | `"                marker = match.group(1)"` | — |
| [SRC-E599346ABE-L001230](../generate_index.py#L1230) | 1230 | `"                totals[marker] = totals.get(marker, 0) + 1"` | — |
| [SRC-E599346ABE-L001231](../generate_index.py#L1231) | 1231 | `"            occurrences: dict[str, int] = {}"` | — |
| [SRC-E599346ABE-L001232](../generate_index.py#L1232) | 1232 | `"            for match in matches:"` | — |
| [SRC-E599346ABE-L001233](../generate_index.py#L1233) | 1233 | `"                marker = match.group(1)"` | — |
| [SRC-E599346ABE-L001234](../generate_index.py#L1234) | 1234 | `"                occurrences[marker] = occurrences.get(marker, 0) + 1"` | — |
| [SRC-E599346ABE-L001235](../generate_index.py#L1235) | 1235 | `"                detail = (match.group(2) or \"\").strip()"` | — |
| [SRC-E599346ABE-L001236](../generate_index.py#L1236) | 1236 | `"                description = marker if not detail else f\"{marker}: {detail}\""` | — |
| [SRC-E599346ABE-L001237](../generate_index.py#L1237) | 1237 | `"                finding_id = ("` | — |
| [SRC-E599346ABE-L001238](../generate_index.py#L1238) | 1238 | `"                    f\"FND-{marker}-{source_line.file_id.removeprefix('FILE-')}\""` | — |
| [SRC-E599346ABE-L001239](../generate_index.py#L1239) | 1239 | `"                    f\"-L{source_line.line:06d}\""` | — |
| [SRC-E599346ABE-L001240](../generate_index.py#L1240) | 1240 | `"                )"` | — |
| [SRC-E599346ABE-L001241](../generate_index.py#L1241) | 1241 | `"                if totals[marker] > 1:"` | — |
| [SRC-E599346ABE-L001242](../generate_index.py#L1242) | 1242 | `"                    finding_id += f\"-M{occurrences[marker]:02d}\""` | — |
| [SRC-E599346ABE-L001243](../generate_index.py#L1243) | 1243 | `"                findings.append("` | — |
| [SRC-E599346ABE-L001244](../generate_index.py#L1244) | 1244 | `"                    IndexedFinding("` | — |
| [SRC-E599346ABE-L001245](../generate_index.py#L1245) | 1245 | `"                        finding_id=finding_id,"` | — |
| [SRC-E599346ABE-L001246](../generate_index.py#L1246) | 1246 | `"                        file=source_line.file,"` | — |
| [SRC-E599346ABE-L001247](../generate_index.py#L1247) | 1247 | `"                        line_id=source_line.line_id,"` | — |
| [SRC-E599346ABE-L001248](../generate_index.py#L1248) | 1248 | `"                        marker=marker,"` | — |
| [SRC-E599346ABE-L001249](../generate_index.py#L1249) | 1249 | `"                        description=description,"` | — |
| [SRC-E599346ABE-L001250](../generate_index.py#L1250) | 1250 | `"                    )"` | — |
| [SRC-E599346ABE-L001251](../generate_index.py#L1251) | 1251 | `"                )"` | — |
| [SRC-E599346ABE-L001252](../generate_index.py#L1252) | 1252 | `"    findings.sort("` | — |
| [SRC-E599346ABE-L001253](../generate_index.py#L1253) | 1253 | `"        key=lambda item: (item.marker, item.file.casefold(), item.line_id, item.finding_id)"` | — |
| [SRC-E599346ABE-L001254](../generate_index.py#L1254) | 1254 | `"    )"` | — |
| [SRC-E599346ABE-L001255](../generate_index.py#L1255) | 1255 | `"    return findings"` | — |
| [SRC-E599346ABE-L001256](../generate_index.py#L1256) | 1256 | `""` | — |
| [SRC-E599346ABE-L001257](../generate_index.py#L1257) | 1257 | `""` | — |
| [SRC-E599346ABE-L001258](../generate_index.py#L1258) | 1258 | `"def _markdown_code_span(value: str) -> str:"` | — |
| [SRC-E599346ABE-L001259](../generate_index.py#L1259) | 1259 | `"    \"\"\"Render a Markdown inline-code span safely, including backticks in source text.\"\"\""` | — |
| [SRC-E599346ABE-L001260](../generate_index.py#L1260) | 1260 | `"    tick = chr(96)"` | — |
| [SRC-E599346ABE-L001261](../generate_index.py#L1261) | 1261 | `"    longest = max("` | — |
| [SRC-E599346ABE-L001262](../generate_index.py#L1262) | 1262 | `"        (len(match.group(0)) for match in re.finditer(r\"\\u0060+\", value)),"` | — |
| [SRC-E599346ABE-L001263](../generate_index.py#L1263) | 1263 | `"        default=0,"` | — |
| [SRC-E599346ABE-L001264](../generate_index.py#L1264) | 1264 | `"    )"` | — |
| [SRC-E599346ABE-L001265](../generate_index.py#L1265) | 1265 | `"    fence = tick * (longest + 1)"` | — |
| [SRC-E599346ABE-L001266](../generate_index.py#L1266) | 1266 | `"    content = f\" {value} \" if value.startswith(tick) or value.endswith(tick) else value"` | — |
| [SRC-E599346ABE-L001267](../generate_index.py#L1267) | 1267 | `"    return f\"{fence}{content}{fence}\""` | — |
| [SRC-E599346ABE-L001268](../generate_index.py#L1268) | 1268 | `""` | — |
| [SRC-E599346ABE-L001269](../generate_index.py#L1269) | 1269 | `""` | — |
| [SRC-E599346ABE-L001270](../generate_index.py#L1270) | 1270 | `"def render_source_line_pages("` | — |
| [SRC-E599346ABE-L001271](../generate_index.py#L1271) | 1271 | `"    source_lines: list[IndexedLine],"` | — |
| [SRC-E599346ABE-L001272](../generate_index.py#L1272) | 1272 | `"    inventory: list[IndexedFile],"` | — |
| [SRC-E599346ABE-L001273](../generate_index.py#L1273) | 1273 | `"    findings: list[IndexedFinding],"` | — |
| [SRC-E599346ABE-L001274](../generate_index.py#L1274) | 1274 | `") -> tuple[dict[str, str], dict[str, list[str]]]:"` | — |
| [SRC-E599346ABE-L001275](../generate_index.py#L1275) | 1275 | `"    \"\"\"Split line-level records into deterministic small pages and map each file to its pages.\"\"\""` | — |
| [SRC-E599346ABE-L001276](../generate_index.py#L1276) | 1276 | `"    pages: dict[str, str] = {}"` | — |
| [SRC-E599346ABE-L001277](../generate_index.py#L1277) | 1277 | `"    pages_by_file: dict[str, list[str]] = {}"` | — |
| [SRC-E599346ABE-L001278](../generate_index.py#L1278) | 1278 | `"    inventory_by_path = {item.file: item for item in inventory}"` | — |
| [SRC-E599346ABE-L001279](../generate_index.py#L1279) | 1279 | `"    findings_by_line: dict[str, list[IndexedFinding]] = {}"` | — |
| [SRC-E599346ABE-L001280](../generate_index.py#L1280) | 1280 | `"    for finding in findings:"` | — |
| [SRC-E599346ABE-L001281](../generate_index.py#L1281) | 1281 | `"        findings_by_line.setdefault(finding.line_id, []).append(finding)"` | — |
| [SRC-E599346ABE-L001282](../generate_index.py#L1282) | 1282 | `""` | — |
| [SRC-E599346ABE-L001283](../generate_index.py#L1283) | 1283 | `"    for page_number, start in enumerate("` | — |
| [SRC-E599346ABE-L001284](../generate_index.py#L1284) | 1284 | `"        range(0, len(source_lines), SOURCE_LINES_PAGE_SIZE),"` | — |
| [SRC-E599346ABE-L001285](../generate_index.py#L1285) | 1285 | `"        start=1,"` | — |
| [SRC-E599346ABE-L001286](../generate_index.py#L1286) | 1286 | `"    ):"` | — |
| [SRC-E599346ABE-L001287](../generate_index.py#L1287) | 1287 | `"        chunk = source_lines[start : start + SOURCE_LINES_PAGE_SIZE]"` | — |
| [SRC-E599346ABE-L001288](../generate_index.py#L1288) | 1288 | `"        page_path = f\"{SOURCE_LINES_PAGES_DIR}/SOURCE_LINES_{page_number:03d}.md\""` | — |
| [SRC-E599346ABE-L001289](../generate_index.py#L1289) | 1289 | `"        lines = ["` | — |
| [SRC-E599346ABE-L001290](../generate_index.py#L1290) | 1290 | `"            \"# Omarai Source Lines\","` | — |
| [SRC-E599346ABE-L001291](../generate_index.py#L1291) | 1291 | `"            \"\","` | — |
| [SRC-E599346ABE-L001292](../generate_index.py#L1292) | 1292 | `"            \"<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001293](../generate_index.py#L1293) | 1293 | `"            \"\","` | — |
| [SRC-E599346ABE-L001294](../generate_index.py#L1294) | 1294 | `"            f\"- الصفحة: **{page_number:03d}**\","` | — |
| [SRC-E599346ABE-L001295](../generate_index.py#L1295) | 1295 | `"            f\"- سجلات الأسطر: **{len(chunk)}**\","` | — |
| [SRC-E599346ABE-L001296](../generate_index.py#L1296) | 1296 | `"            f\"- النطاق: {chunk[0].line_id} إلى {chunk[-1].line_id}\","` | — |
| [SRC-E599346ABE-L001297](../generate_index.py#L1297) | 1297 | `"            \"- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)\","` | — |
| [SRC-E599346ABE-L001298](../generate_index.py#L1298) | 1298 | `"            \"\","` | — |
| [SRC-E599346ABE-L001299](../generate_index.py#L1299) | 1299 | `"        ]"` | — |
| [SRC-E599346ABE-L001300](../generate_index.py#L1300) | 1300 | `"        current_file: str \| None = None"` | — |
| [SRC-E599346ABE-L001301](../generate_index.py#L1301) | 1301 | `"        for source_line in chunk:"` | — |
| [SRC-E599346ABE-L001302](../generate_index.py#L1302) | 1302 | `"            item = inventory_by_path[source_line.file]"` | — |
| [SRC-E599346ABE-L001303](../generate_index.py#L1303) | 1303 | `"            if source_line.file != current_file:"` | — |
| [SRC-E599346ABE-L001304](../generate_index.py#L1304) | 1304 | `"                current_file = source_line.file"` | — |
| [SRC-E599346ABE-L001305](../generate_index.py#L1305) | 1305 | `"                lines.extend("` | — |
| [SRC-E599346ABE-L001306](../generate_index.py#L1306) | 1306 | `"                    ["` | — |
| [SRC-E599346ABE-L001307](../generate_index.py#L1307) | 1307 | `"                        f\"## {item.category}\","` | — |
| [SRC-E599346ABE-L001308](../generate_index.py#L1308) | 1308 | `"                        \"\","` | — |
| [SRC-E599346ABE-L001309](../generate_index.py#L1309) | 1309 | `"                        f\"### {item.file_id} — [{_markdown_cell(item.file)}]({_source_file_href(item.file, index_directory=SOURCE_LINES_PAGES_DIR)})\","` | — |
| [SRC-E599346ABE-L001310](../generate_index.py#L1310) | 1310 | `"                        \"\","` | — |
| [SRC-E599346ABE-L001311](../generate_index.py#L1311) | 1311 | `"                        f\"- النوع: **{item.file_type}**\","` | — |
| [SRC-E599346ABE-L001312](../generate_index.py#L1312) | 1312 | `"                        f\"- نطاق الفهرسة: {_markdown_cell(item.indexing_scope)}\","` | — |
| [SRC-E599346ABE-L001313](../generate_index.py#L1313) | 1313 | `"                        \"\","` | — |
| [SRC-E599346ABE-L001314](../generate_index.py#L1314) | 1314 | `"                        \"\| كود السطر \| السطر \| النص الكامل للسطر \| كود الوسم \|\","` | — |
| [SRC-E599346ABE-L001315](../generate_index.py#L1315) | 1315 | `"                        \"\|---\|---:\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001316](../generate_index.py#L1316) | 1316 | `"                    ]"` | — |
| [SRC-E599346ABE-L001317](../generate_index.py#L1317) | 1317 | `"                )"` | — |
| [SRC-E599346ABE-L001318](../generate_index.py#L1318) | 1318 | `"            line_findings = findings_by_line.get(source_line.line_id, [])"` | — |
| [SRC-E599346ABE-L001319](../generate_index.py#L1319) | 1319 | `"            finding_code = \", \".join(item.finding_id for item in line_findings) or \"—\""` | — |
| [SRC-E599346ABE-L001320](../generate_index.py#L1320) | 1320 | `"            exact_text = json.dumps(source_line.content, ensure_ascii=False)"` | — |
| [SRC-E599346ABE-L001321](../generate_index.py#L1321) | 1321 | `"            escaped_text = exact_text.replace(\"\|\", r\"\\\|\")"` | — |
| [SRC-E599346ABE-L001322](../generate_index.py#L1322) | 1322 | `"            href = _source_file_href("` | — |
| [SRC-E599346ABE-L001323](../generate_index.py#L1323) | 1323 | `"                source_line.file,"` | — |
| [SRC-E599346ABE-L001324](../generate_index.py#L1324) | 1324 | `"                source_line.line,"` | — |
| [SRC-E599346ABE-L001325](../generate_index.py#L1325) | 1325 | `"                index_directory=SOURCE_LINES_PAGES_DIR,"` | — |
| [SRC-E599346ABE-L001326](../generate_index.py#L1326) | 1326 | `"            )"` | — |
| [SRC-E599346ABE-L001327](../generate_index.py#L1327) | 1327 | `"            line_code = f\"[{source_line.line_id}]({href})\""` | — |
| [SRC-E599346ABE-L001328](../generate_index.py#L1328) | 1328 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001329](../generate_index.py#L1329) | 1329 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001330](../generate_index.py#L1330) | 1330 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001331](../generate_index.py#L1331) | 1331 | `"                    ("` | — |
| [SRC-E599346ABE-L001332](../generate_index.py#L1332) | 1332 | `"                        line_code,"` | — |
| [SRC-E599346ABE-L001333](../generate_index.py#L1333) | 1333 | `"                        str(source_line.line),"` | — |
| [SRC-E599346ABE-L001334](../generate_index.py#L1334) | 1334 | `"                        _markdown_code_span(escaped_text),"` | — |
| [SRC-E599346ABE-L001335](../generate_index.py#L1335) | 1335 | `"                        finding_code,"` | — |
| [SRC-E599346ABE-L001336](../generate_index.py#L1336) | 1336 | `"                    )"` | — |
| [SRC-E599346ABE-L001337](../generate_index.py#L1337) | 1337 | `"                )"` | — |
| [SRC-E599346ABE-L001338](../generate_index.py#L1338) | 1338 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001339](../generate_index.py#L1339) | 1339 | `"            )"` | — |
| [SRC-E599346ABE-L001340](../generate_index.py#L1340) | 1340 | `"            refs = pages_by_file.setdefault(source_line.file, [])"` | — |
| [SRC-E599346ABE-L001341](../generate_index.py#L1341) | 1341 | `"            if page_path not in refs:"` | — |
| [SRC-E599346ABE-L001342](../generate_index.py#L1342) | 1342 | `"                refs.append(page_path)"` | — |
| [SRC-E599346ABE-L001343](../generate_index.py#L1343) | 1343 | `"        pages[page_path] = \"\\n\".join(lines) + \"\\n\""` | — |
| [SRC-E599346ABE-L001344](../generate_index.py#L1344) | 1344 | `""` | — |
| [SRC-E599346ABE-L001345](../generate_index.py#L1345) | 1345 | `"    return pages, pages_by_file"` | — |
| [SRC-E599346ABE-L001346](../generate_index.py#L1346) | 1346 | `""` | — |
| [SRC-E599346ABE-L001347](../generate_index.py#L1347) | 1347 | `""` | — |
| [SRC-E599346ABE-L001348](../generate_index.py#L1348) | 1348 | `"def render_source_lines_markdown("` | — |
| [SRC-E599346ABE-L001349](../generate_index.py#L1349) | 1349 | `"    source_lines: list[IndexedLine],"` | — |
| [SRC-E599346ABE-L001350](../generate_index.py#L1350) | 1350 | `"    inventory: list[IndexedFile],"` | — |
| [SRC-E599346ABE-L001351](../generate_index.py#L1351) | 1351 | `"    findings: list[IndexedFinding],"` | — |
| [SRC-E599346ABE-L001352](../generate_index.py#L1352) | 1352 | `"    pages_by_file: dict[str, list[str]] \| None = None,"` | — |
| [SRC-E599346ABE-L001353](../generate_index.py#L1353) | 1353 | `"    source_pages: dict[str, str] \| None = None,"` | — |
| [SRC-E599346ABE-L001354](../generate_index.py#L1354) | 1354 | `") -> str:"` | — |
| [SRC-E599346ABE-L001355](../generate_index.py#L1355) | 1355 | `"    \"\"\"Render a compact table of contents for the sharded full source-line index.\"\"\""` | — |
| [SRC-E599346ABE-L001356](../generate_index.py#L1356) | 1356 | `"    assigned_pages = pages_by_file or {}"` | — |
| [SRC-E599346ABE-L001357](../generate_index.py#L1357) | 1357 | `"    rendered_pages = source_pages or {}"` | — |
| [SRC-E599346ABE-L001358](../generate_index.py#L1358) | 1358 | `"    files_with_lines = sum(item.line_count is not None for item in inventory)"` | — |
| [SRC-E599346ABE-L001359](../generate_index.py#L1359) | 1359 | `"    lines = ["` | — |
| [SRC-E599346ABE-L001360](../generate_index.py#L1360) | 1360 | `"        \"# SOURCE LINES INDEX — Omarai\","` | — |
| [SRC-E599346ABE-L001361](../generate_index.py#L1361) | 1361 | `"        \"\","` | — |
| [SRC-E599346ABE-L001362](../generate_index.py#L1362) | 1362 | `"        \"<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001363](../generate_index.py#L1363) | 1363 | `"        \"\","` | — |
| [SRC-E599346ABE-L001364](../generate_index.py#L1364) | 1364 | `"        \"> هذا دليل الوصول إلى فهرس الأسطر الكامل. يحتوي كل سطر في الملفات النصية المؤهلة على كود SRC- ورقم السطر ونص السطر كاملًا.\","` | — |
| [SRC-E599346ABE-L001365](../generate_index.py#L1365) | 1365 | `"        \"> قُسّم المحتوى إلى صفحات صغيرة حتى تظل كل صفحة قابلة للفتح والبحث بسرعة من الهاتف والمتصفح.\","` | — |
| [SRC-E599346ABE-L001366](../generate_index.py#L1366) | 1366 | `"        \"> ابدأ من [MASTER INDEX](MASTER_INDEX.md) للعثور حسب اسم الملف أو الدالة أو الكلاس أو وسم المراجعة.\","` | — |
| [SRC-E599346ABE-L001367](../generate_index.py#L1367) | 1367 | `"        \"> راجع [INDEX COVERAGE AUDIT](INDEX_COVERAGE_AUDIT.md) للاطلاع على نسبة التغطية وأسباب الاستبعاد.\","` | — |
| [SRC-E599346ABE-L001368](../generate_index.py#L1368) | 1368 | `"        \"\","` | — |
| [SRC-E599346ABE-L001369](../generate_index.py#L1369) | 1369 | `"        \"## ملخص التغطية\","` | — |
| [SRC-E599346ABE-L001370](../generate_index.py#L1370) | 1370 | `"        \"\","` | — |
| [SRC-E599346ABE-L001371](../generate_index.py#L1371) | 1371 | `"        f\"- الملفات في جرد المستودع: **{len(inventory)}**\","` | — |
| [SRC-E599346ABE-L001372](../generate_index.py#L1372) | 1372 | `"        f\"- الملفات النصية المفهرسة سطرًا بسطر: **{files_with_lines}**\","` | — |
| [SRC-E599346ABE-L001373](../generate_index.py#L1373) | 1373 | `"        f\"- الأسطر المفهرسة: **{len(source_lines)}**\","` | — |
| [SRC-E599346ABE-L001374](../generate_index.py#L1374) | 1374 | `"        f\"- وسوم المراجعة/الإصلاح المسجلة: **{len(findings)}**\","` | — |
| [SRC-E599346ABE-L001375](../generate_index.py#L1375) | 1375 | `"        f\"- صفحات الأسطر: **{len(rendered_pages)}**\","` | — |
| [SRC-E599346ABE-L001376](../generate_index.py#L1376) | 1376 | `"        \"\","` | — |
| [SRC-E599346ABE-L001377](../generate_index.py#L1377) | 1377 | `"        \"## صفحات الأسطر\","` | — |
| [SRC-E599346ABE-L001378](../generate_index.py#L1378) | 1378 | `"        \"\","` | — |
| [SRC-E599346ABE-L001379](../generate_index.py#L1379) | 1379 | `"        \"\| الصفحة \| عدد السجلات \| من كود \| إلى كود \|\","` | — |
| [SRC-E599346ABE-L001380](../generate_index.py#L1380) | 1380 | `"        \"\|---\|---:\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001381](../generate_index.py#L1381) | 1381 | `"    ]"` | — |
| [SRC-E599346ABE-L001382](../generate_index.py#L1382) | 1382 | `"    for page_path, page_content in rendered_pages.items():"` | — |
| [SRC-E599346ABE-L001383](../generate_index.py#L1383) | 1383 | `"        count = sum(1 for line in page_content.splitlines() if line.startswith(\"\| [SRC-\"))"` | — |
| [SRC-E599346ABE-L001384](../generate_index.py#L1384) | 1384 | `"        ids = re.findall(r\"\\bSRC-[A-F0-9]+-L\\d{6}\\b\", page_content)"` | — |
| [SRC-E599346ABE-L001385](../generate_index.py#L1385) | 1385 | `"        label = Path(page_path).stem"` | — |
| [SRC-E599346ABE-L001386](../generate_index.py#L1386) | 1386 | `"        lines.append("` | — |
| [SRC-E599346ABE-L001387](../generate_index.py#L1387) | 1387 | `"            f\"\| [{label}]({Path(page_path).relative_to('docs').as_posix()}) \| \""` | — |
| [SRC-E599346ABE-L001388](../generate_index.py#L1388) | 1388 | `"            f\"{count} \| {ids[0] if ids else '—'} \| {ids[-1] if ids else '—'} \|\""` | — |
| [SRC-E599346ABE-L001389](../generate_index.py#L1389) | 1389 | `"        )"` | — |
| [SRC-E599346ABE-L001390](../generate_index.py#L1390) | 1390 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001391](../generate_index.py#L1391) | 1391 | `"        ["` | — |
| [SRC-E599346ABE-L001392](../generate_index.py#L1392) | 1392 | `"            \"\","` | — |
| [SRC-E599346ABE-L001393](../generate_index.py#L1393) | 1393 | `"            \"## جرد الملفات والوصول حسب الاسم\","` | — |
| [SRC-E599346ABE-L001394](../generate_index.py#L1394) | 1394 | `"            \"\","` | — |
| [SRC-E599346ABE-L001395](../generate_index.py#L1395) | 1395 | `"            \"\| معرّف الملف \| التصنيف \| الملف \| الأسطر \| صفحات الفهرسة \|\","` | — |
| [SRC-E599346ABE-L001396](../generate_index.py#L1396) | 1396 | `"            \"\|---\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001397](../generate_index.py#L1397) | 1397 | `"        ]"` | — |
| [SRC-E599346ABE-L001398](../generate_index.py#L1398) | 1398 | `"    )"` | — |
| [SRC-E599346ABE-L001399](../generate_index.py#L1399) | 1399 | `"    for item in sorted(inventory, key=lambda entry: (entry.category, entry.file.casefold())):"` | — |
| [SRC-E599346ABE-L001400](../generate_index.py#L1400) | 1400 | `"        if item.line_count is None:"` | — |
| [SRC-E599346ABE-L001401](../generate_index.py#L1401) | 1401 | `"            line_count = \"بيانات وصفية فقط\""` | — |
| [SRC-E599346ABE-L001402](../generate_index.py#L1402) | 1402 | `"        else:"` | — |
| [SRC-E599346ABE-L001403](../generate_index.py#L1403) | 1403 | `"            line_count = str(item.line_count)"` | — |
| [SRC-E599346ABE-L001404](../generate_index.py#L1404) | 1404 | `"        page_links = assigned_pages.get(item.file, [])"` | — |
| [SRC-E599346ABE-L001405](../generate_index.py#L1405) | 1405 | `"        if page_links:"` | — |
| [SRC-E599346ABE-L001406](../generate_index.py#L1406) | 1406 | `"            link_text = \", \".join("` | — |
| [SRC-E599346ABE-L001407](../generate_index.py#L1407) | 1407 | `"                f\"[{Path(page_path).stem}]({Path(page_path).relative_to('docs').as_posix()})\""` | — |
| [SRC-E599346ABE-L001408](../generate_index.py#L1408) | 1408 | `"                for page_path in page_links"` | — |
| [SRC-E599346ABE-L001409](../generate_index.py#L1409) | 1409 | `"            )"` | — |
| [SRC-E599346ABE-L001410](../generate_index.py#L1410) | 1410 | `"        elif item.line_count == 0:"` | — |
| [SRC-E599346ABE-L001411](../generate_index.py#L1411) | 1411 | `"            link_text = \"ملف نصي فارغ\""` | — |
| [SRC-E599346ABE-L001412](../generate_index.py#L1412) | 1412 | `"        elif item.line_count is None:"` | — |
| [SRC-E599346ABE-L001413](../generate_index.py#L1413) | 1413 | `"            link_text = \"غير مفهرس سطرًا بسطر\""` | — |
| [SRC-E599346ABE-L001414](../generate_index.py#L1414) | 1414 | `"        else:"` | — |
| [SRC-E599346ABE-L001415](../generate_index.py#L1415) | 1415 | `"            link_text = \"لا توجد سجلات\""` | — |
| [SRC-E599346ABE-L001416](../generate_index.py#L1416) | 1416 | `"        target = _source_file_href(item.file, index_directory=\"docs\")"` | — |
| [SRC-E599346ABE-L001417](../generate_index.py#L1417) | 1417 | `"        lines.append("` | — |
| [SRC-E599346ABE-L001418](../generate_index.py#L1418) | 1418 | `"            f\"\| {item.file_id} \| {_markdown_cell(item.category)} \| \""` | — |
| [SRC-E599346ABE-L001419](../generate_index.py#L1419) | 1419 | `"            f\"[{_markdown_cell(item.file)}]({target}) \| {line_count} \| {link_text} \|\""` | — |
| [SRC-E599346ABE-L001420](../generate_index.py#L1420) | 1420 | `"        )"` | — |
| [SRC-E599346ABE-L001421](../generate_index.py#L1421) | 1421 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001422](../generate_index.py#L1422) | 1422 | `"        ["` | — |
| [SRC-E599346ABE-L001423](../generate_index.py#L1423) | 1423 | `"            \"\","` | — |
| [SRC-E599346ABE-L001424](../generate_index.py#L1424) | 1424 | `"            \"## سجل وسوم المراجعة والإصلاح\","` | — |
| [SRC-E599346ABE-L001425](../generate_index.py#L1425) | 1425 | `"            \"\","` | — |
| [SRC-E599346ABE-L001426](../generate_index.py#L1426) | 1426 | `"            \"كل كود FND- في MASTER INDEX يحدد وسمًا صريحًا ويشير إلى كود السطر في إحدى صفحات هذا الفهرس.\","` | — |
| [SRC-E599346ABE-L001427](../generate_index.py#L1427) | 1427 | `"            \"الوسوم المعروفة: TODO وFIXME وBUG وHACK وXXX وREVIEW وSECURITY وDEPRECATED وISSUE وDEFECT وREGRESSION وRISK وGAP وERROR وWARNING وPERF وPRIVACY وDATA_LOSS وACCESSIBILITY.\","` | — |
| [SRC-E599346ABE-L001428](../generate_index.py#L1428) | 1428 | `"            \"\","` | — |
| [SRC-E599346ABE-L001429](../generate_index.py#L1429) | 1429 | `"            \"## الاستثناءات وحدود التغطية\","` | — |
| [SRC-E599346ABE-L001430](../generate_index.py#L1430) | 1430 | `"            \"\","` | — |
| [SRC-E599346ABE-L001431](../generate_index.py#L1431) | 1431 | `"            \"- ملفات الفهرسة المولّدة نفسها مستثناة لمنع الحلقة الذاتية.\","` | — |
| [SRC-E599346ABE-L001432](../generate_index.py#L1432) | 1432 | `"            \"- تُفهرس سطور كل ملف نصي قابل للقراءة وحجمه حتى 2 MiB؛ الملفات الثنائية أو الأكبر أو غير القابلة للقراءة تظهر في جرد الملفات فقط.\","` | — |
| [SRC-E599346ABE-L001433](../generate_index.py#L1433) | 1433 | `"            \"- الملفات الحساسة المعروفة وقواعد البيانات والبيئات المحلية ومجلدات البناء والاعتماديات مستثناة عمدًا.\","` | — |
| [SRC-E599346ABE-L001434](../generate_index.py#L1434) | 1434 | `"            \"- أكواد الأسطر مشتقة من مسار الملف ورقم السطر؛ يتغير رقم الكود عند تحرك السطر بسبب تغييرات سابقة في الملف.\","` | — |
| [SRC-E599346ABE-L001435](../generate_index.py#L1435) | 1435 | `"            \"- وسوم المراجعة ليست تشخيصًا آليًا لكل عيب منطقي؛ الفهرس يسهل العثور على الكود لكنه لا يستطيع إثبات خلوه من الأخطاء.\","` | — |
| [SRC-E599346ABE-L001436](../generate_index.py#L1436) | 1436 | `"            \"\","` | — |
| [SRC-E599346ABE-L001437](../generate_index.py#L1437) | 1437 | `"        ]"` | — |
| [SRC-E599346ABE-L001438](../generate_index.py#L1438) | 1438 | `"    )"` | — |
| [SRC-E599346ABE-L001439](../generate_index.py#L1439) | 1439 | `"    return \"\\n\".join(lines) + \"\\n\""` | — |
| [SRC-E599346ABE-L001440](../generate_index.py#L1440) | 1440 | `""` | — |
| [SRC-E599346ABE-L001441](../generate_index.py#L1441) | 1441 | `""` | — |
| [SRC-E599346ABE-L001442](../generate_index.py#L1442) | 1442 | `"def render_coverage_audit_markdown("` | — |
| [SRC-E599346ABE-L001443](../generate_index.py#L1443) | 1443 | `"    root: Path,"` | — |
| [SRC-E599346ABE-L001444](../generate_index.py#L1444) | 1444 | `"    inventory: list[IndexedFile],"` | — |
| [SRC-E599346ABE-L001445](../generate_index.py#L1445) | 1445 | `"    source_lines: list[IndexedLine],"` | — |
| [SRC-E599346ABE-L001446](../generate_index.py#L1446) | 1446 | `"    excluded_paths: list[tuple[str, str]],"` | — |
| [SRC-E599346ABE-L001447](../generate_index.py#L1447) | 1447 | `") -> str:"` | — |
| [SRC-E599346ABE-L001448](../generate_index.py#L1448) | 1448 | `"    \"\"\"Render a generated coverage ledger with exact line-index coverage and exclusions.\"\"\""` | — |
| [SRC-E599346ABE-L001449](../generate_index.py#L1449) | 1449 | `"    indexed_files = [item for item in inventory if item.line_count is not None]"` | — |
| [SRC-E599346ABE-L001450](../generate_index.py#L1450) | 1450 | `"    metadata_only = [item for item in inventory if item.line_count is None]"` | — |
| [SRC-E599346ABE-L001451](../generate_index.py#L1451) | 1451 | `"    expected_line_count = sum(item.line_count or 0 for item in indexed_files)"` | — |
| [SRC-E599346ABE-L001452](../generate_index.py#L1452) | 1452 | `"    actual_line_count = len(source_lines)"` | — |
| [SRC-E599346ABE-L001453](../generate_index.py#L1453) | 1453 | `"    coverage_ok = expected_line_count == actual_line_count"` | — |
| [SRC-E599346ABE-L001454](../generate_index.py#L1454) | 1454 | `"    lines = ["` | — |
| [SRC-E599346ABE-L001455](../generate_index.py#L1455) | 1455 | `"        \"# OMARAI INDEX COVERAGE AUDIT\","` | — |
| [SRC-E599346ABE-L001456](../generate_index.py#L1456) | 1456 | `"        \"\","` | — |
| [SRC-E599346ABE-L001457](../generate_index.py#L1457) | 1457 | `"        \"<!-- هذا الملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001458](../generate_index.py#L1458) | 1458 | `"        \"\","` | — |
| [SRC-E599346ABE-L001459](../generate_index.py#L1459) | 1459 | `"        \"> سجل أدلة تغطية الفهرس وحدوده، وليس ادعاءً باكتشاف كل عيب منطقي في البرنامج.\","` | — |
| [SRC-E599346ABE-L001460](../generate_index.py#L1460) | 1460 | `"        \"\","` | — |
| [SRC-E599346ABE-L001461](../generate_index.py#L1461) | 1461 | `"        \"## نتيجة تغطية السطور\","` | — |
| [SRC-E599346ABE-L001462](../generate_index.py#L1462) | 1462 | `"        \"\","` | — |
| [SRC-E599346ABE-L001463](../generate_index.py#L1463) | 1463 | `"        f\"- ملفات المستودع المؤهلة في الجرد: **{len(inventory)}**\","` | — |
| [SRC-E599346ABE-L001464](../generate_index.py#L1464) | 1464 | `"        f\"- الملفات المفهرسة سطرًا بسطر: **{len(indexed_files)}**\","` | — |
| [SRC-E599346ABE-L001465](../generate_index.py#L1465) | 1465 | `"        f\"- الملفات الوصفية فقط التي لا تتوفر سطورها: **{len(metadata_only)}**\","` | — |
| [SRC-E599346ABE-L001466](../generate_index.py#L1466) | 1466 | `"        f\"- السطور المتوقع فهرستها من عدادات الملفات: **{expected_line_count}**\","` | — |
| [SRC-E599346ABE-L001467](../generate_index.py#L1467) | 1467 | `"        f\"- سجلات السطور الفعلية: **{actual_line_count}**\","` | — |
| [SRC-E599346ABE-L001468](../generate_index.py#L1468) | 1468 | `"        f\"- تحقق العدد الإجمالي: **{'PASS' if coverage_ok else 'FAIL'}**\","` | — |
| [SRC-E599346ABE-L001469](../generate_index.py#L1469) | 1469 | `"        f\"- نسبة التغطية الحسابية ضمن الملفات المؤهلة القابلة للقراءة: **{(100.0 if coverage_ok and expected_line_count == actual_line_count else (actual_line_count / expected_line_count * 100 if expected_line_count else 100.0)):.2f}%**\","` | — |
| [SRC-E599346ABE-L001470](../generate_index.py#L1470) | 1470 | `"        \"\","` | — |
| [SRC-E599346ABE-L001471](../generate_index.py#L1471) | 1471 | `"        \"يتحقق المولد كذلك من أن أرقام السطور متتابعة لكل ملف ومن عدم تكرار معرّفات SRC؛ أي فشل يمنع نشر الفهرس.\","` | — |
| [SRC-E599346ABE-L001472](../generate_index.py#L1472) | 1472 | `"        \"\","` | — |
| [SRC-E599346ABE-L001473](../generate_index.py#L1473) | 1473 | `"        \"## الملفات التي لا تُفهرس سطورها\","` | — |
| [SRC-E599346ABE-L001474](../generate_index.py#L1474) | 1474 | `"        \"\","` | — |
| [SRC-E599346ABE-L001475](../generate_index.py#L1475) | 1475 | `"        \"هذه الملفات تظل ظاهرة في جرد MASTER INDEX مع سبب الاستثناء. لا يُدرج التقرير محتوياتها.\","` | — |
| [SRC-E599346ABE-L001476](../generate_index.py#L1476) | 1476 | `"        \"\","` | — |
| [SRC-E599346ABE-L001477](../generate_index.py#L1477) | 1477 | `"        \"\| معرّف الملف \| المسار \| الحجم بالبايت \| السبب \|\","` | — |
| [SRC-E599346ABE-L001478](../generate_index.py#L1478) | 1478 | `"        \"\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001479](../generate_index.py#L1479) | 1479 | `"    ]"` | — |
| [SRC-E599346ABE-L001480](../generate_index.py#L1480) | 1480 | `""` | — |
| [SRC-E599346ABE-L001481](../generate_index.py#L1481) | 1481 | `"    if metadata_only:"` | — |
| [SRC-E599346ABE-L001482](../generate_index.py#L1482) | 1482 | `"        for item in metadata_only:"` | — |
| [SRC-E599346ABE-L001483](../generate_index.py#L1483) | 1483 | `"            reason = _text_index_skip_reason(root / item.file)"` | — |
| [SRC-E599346ABE-L001484](../generate_index.py#L1484) | 1484 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001485](../generate_index.py#L1485) | 1485 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001486](../generate_index.py#L1486) | 1486 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001487](../generate_index.py#L1487) | 1487 | `"                    ("` | — |
| [SRC-E599346ABE-L001488](../generate_index.py#L1488) | 1488 | `"                        item.file_id,"` | — |
| [SRC-E599346ABE-L001489](../generate_index.py#L1489) | 1489 | `"                        _markdown_code_span(item.file),"` | — |
| [SRC-E599346ABE-L001490](../generate_index.py#L1490) | 1490 | `"                        str(item.size_bytes),"` | — |
| [SRC-E599346ABE-L001491](../generate_index.py#L1491) | 1491 | `"                        _markdown_cell(reason),"` | — |
| [SRC-E599346ABE-L001492](../generate_index.py#L1492) | 1492 | `"                    )"` | — |
| [SRC-E599346ABE-L001493](../generate_index.py#L1493) | 1493 | `"                )"` | — |
| [SRC-E599346ABE-L001494](../generate_index.py#L1494) | 1494 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001495](../generate_index.py#L1495) | 1495 | `"            )"` | — |
| [SRC-E599346ABE-L001496](../generate_index.py#L1496) | 1496 | `"    else:"` | — |
| [SRC-E599346ABE-L001497](../generate_index.py#L1497) | 1497 | `"        lines.append(\"\| — \| — \| — \| لا توجد ملفات مؤهلة بالجرد الوصفي فقط. \|\")"` | — |
| [SRC-E599346ABE-L001498](../generate_index.py#L1498) | 1498 | `""` | — |
| [SRC-E599346ABE-L001499](../generate_index.py#L1499) | 1499 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001500](../generate_index.py#L1500) | 1500 | `"        ["` | — |
| [SRC-E599346ABE-L001501](../generate_index.py#L1501) | 1501 | `"            \"\","` | — |
| [SRC-E599346ABE-L001502](../generate_index.py#L1502) | 1502 | `"            \"## المسارات المستبعدة عمدًا\","` | — |
| [SRC-E599346ABE-L001503](../generate_index.py#L1503) | 1503 | `"            \"\","` | — |
| [SRC-E599346ABE-L001504](../generate_index.py#L1504) | 1504 | `"            \"يحتوي هذا السجل أسماء المسارات وأسباب الاستثناء فقط، ولا يقرأ محتوى الأسرار أو قواعد البيانات أو المجلدات المستبعدة.\","` | — |
| [SRC-E599346ABE-L001505](../generate_index.py#L1505) | 1505 | `"            \"\","` | — |
| [SRC-E599346ABE-L001506](../generate_index.py#L1506) | 1506 | `"            \"\| المسار المستبعد \| السبب \|\","` | — |
| [SRC-E599346ABE-L001507](../generate_index.py#L1507) | 1507 | `"            \"\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001508](../generate_index.py#L1508) | 1508 | `"        ]"` | — |
| [SRC-E599346ABE-L001509](../generate_index.py#L1509) | 1509 | `"    )"` | — |
| [SRC-E599346ABE-L001510](../generate_index.py#L1510) | 1510 | `"    if excluded_paths:"` | — |
| [SRC-E599346ABE-L001511](../generate_index.py#L1511) | 1511 | `"        for excluded_path, reason in excluded_paths:"` | — |
| [SRC-E599346ABE-L001512](../generate_index.py#L1512) | 1512 | `"            lines.append(f\"\| {_markdown_code_span(excluded_path)} \| {_markdown_cell(reason)} \|\")"` | — |
| [SRC-E599346ABE-L001513](../generate_index.py#L1513) | 1513 | `"    else:"` | — |
| [SRC-E599346ABE-L001514](../generate_index.py#L1514) | 1514 | `"        lines.append(\"\| — \| لا توجد مسارات مستبعدة مكتشفة. \|\")"` | — |
| [SRC-E599346ABE-L001515](../generate_index.py#L1515) | 1515 | `""` | — |
| [SRC-E599346ABE-L001516](../generate_index.py#L1516) | 1516 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001517](../generate_index.py#L1517) | 1517 | `"        ["` | — |
| [SRC-E599346ABE-L001518](../generate_index.py#L1518) | 1518 | `"            \"\","` | — |
| [SRC-E599346ABE-L001519](../generate_index.py#L1519) | 1519 | `"            \"## ما تعنيه النتيجة وما لا تعنيه\","` | — |
| [SRC-E599346ABE-L001520](../generate_index.py#L1520) | 1520 | `"            \"\","` | — |
| [SRC-E599346ABE-L001521](../generate_index.py#L1521) | 1521 | `"            \"- التغطية بنسبة 100% تعني أن كل سطر منطقي في كل ملف نصي مؤهل وقابل للقراءة ضمن حد الحجم له سجل SRC فريد ورقم سطر مطابق.\","` | — |
| [SRC-E599346ABE-L001522](../generate_index.py#L1522) | 1522 | `"            \"- لا تعني أن كل مسار مستبعد أو كل ملف ثنائي/كبير مفهرس سطرًا بسطر؛ أسباب الاستبعاد مسجلة أعلاه.\","` | — |
| [SRC-E599346ABE-L001523](../generate_index.py#L1523) | 1523 | `"            \"- لا تعني اكتشاف كل عيب برمجي أو أمني أو منطقي. العيوب المعروفة التي يوسمها المطور صراحة تظهر في سجل FND داخل MASTER INDEX.\","` | — |
| [SRC-E599346ABE-L001524](../generate_index.py#L1524) | 1524 | `"            \"- الرموز غير Python مستخرجة بقواعد ساكنة تقريبية؛ استخدم فهرس السطور للوصول إلى النص الأصلي والتحقق يدويًا.\","` | — |
| [SRC-E599346ABE-L001525](../generate_index.py#L1525) | 1525 | `"            \"- المولد لا يعدّل كود التطبيق ولا يدمج الفروع؛ وظيفته بناء الأدلة والفهرس والتحقق من اتساقهما.\","` | — |
| [SRC-E599346ABE-L001526](../generate_index.py#L1526) | 1526 | `"            \"\","` | — |
| [SRC-E599346ABE-L001527](../generate_index.py#L1527) | 1527 | `"            \"[افتح MASTER INDEX](MASTER_INDEX.md) \| [افتح SOURCE LINES INDEX](SOURCE_LINES_INDEX.md)\","` | — |
| [SRC-E599346ABE-L001528](../generate_index.py#L1528) | 1528 | `"            \"\","` | — |
| [SRC-E599346ABE-L001529](../generate_index.py#L1529) | 1529 | `"        ]"` | — |
| [SRC-E599346ABE-L001530](../generate_index.py#L1530) | 1530 | `"    )"` | — |
| [SRC-E599346ABE-L001531](../generate_index.py#L1531) | 1531 | `"    return \"\\n\".join(lines)"` | — |
| [SRC-E599346ABE-L001532](../generate_index.py#L1532) | 1532 | `""` | — |
| [SRC-E599346ABE-L001533](../generate_index.py#L1533) | 1533 | `""` | — |
| [SRC-E599346ABE-L001534](../generate_index.py#L1534) | 1534 | `"def render_markdown("` | — |
| [SRC-E599346ABE-L001535](../generate_index.py#L1535) | 1535 | `"    symbols: list[IndexedSymbol],"` | — |
| [SRC-E599346ABE-L001536](../generate_index.py#L1536) | 1536 | `"    files_scanned: int,"` | — |
| [SRC-E599346ABE-L001537](../generate_index.py#L1537) | 1537 | `"    inventory: list[IndexedFile] \| None = None,"` | — |
| [SRC-E599346ABE-L001538](../generate_index.py#L1538) | 1538 | `"    static_symbols: list[IndexedMarker] \| None = None,"` | — |
| [SRC-E599346ABE-L001539](../generate_index.py#L1539) | 1539 | `"    source_lines: list[IndexedLine] \| None = None,"` | — |
| [SRC-E599346ABE-L001540](../generate_index.py#L1540) | 1540 | `"    findings: list[IndexedFinding] \| None = None,"` | — |
| [SRC-E599346ABE-L001541](../generate_index.py#L1541) | 1541 | `") -> str:"` | — |
| [SRC-E599346ABE-L001542](../generate_index.py#L1542) | 1542 | `"    \"\"\"Render the repository file, symbol, explicit-review-marker, and line-index overview.\"\"\""` | — |
| [SRC-E599346ABE-L001543](../generate_index.py#L1543) | 1543 | `"    file_inventory = inventory or []"` | — |
| [SRC-E599346ABE-L001544](../generate_index.py#L1544) | 1544 | `"    marker_inventory = static_symbols or []"` | — |
| [SRC-E599346ABE-L001545](../generate_index.py#L1545) | 1545 | `"    line_inventory = source_lines or []"` | — |
| [SRC-E599346ABE-L001546](../generate_index.py#L1546) | 1546 | `"    finding_inventory = findings or []"` | — |
| [SRC-E599346ABE-L001547](../generate_index.py#L1547) | 1547 | `"    documented_count = sum(symbol.documented is True for symbol in symbols)"` | — |
| [SRC-E599346ABE-L001548](../generate_index.py#L1548) | 1548 | `"    missing_count = sum(symbol.documented is False for symbol in symbols)"` | — |
| [SRC-E599346ABE-L001549](../generate_index.py#L1549) | 1549 | `"    not_applicable_count = sum(symbol.documented is None for symbol in symbols)"` | — |
| [SRC-E599346ABE-L001550](../generate_index.py#L1550) | 1550 | `"    lines = ["` | — |
| [SRC-E599346ABE-L001551](../generate_index.py#L1551) | 1551 | `"        \"# MASTER INDEX — Omarai\","` | — |
| [SRC-E599346ABE-L001552](../generate_index.py#L1552) | 1552 | `"        \"\","` | — |
| [SRC-E599346ABE-L001553](../generate_index.py#L1553) | 1553 | `"        \"<!-- هذا الملف مُولَّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001554](../generate_index.py#L1554) | 1554 | `"        \"\","` | — |
| [SRC-E599346ABE-L001555](../generate_index.py#L1555) | 1555 | `"        \"> MASTER INDEX يجمع جرد الملفات والتعريفات المسماة ووسوم المراجعة؛ SOURCE LINES INDEX يحتوي الأسطر الكاملة\","` | — |
| [SRC-E599346ABE-L001556](../generate_index.py#L1556) | 1556 | `"        \"> لكل ملف نصي مؤهل قابل للقراءة، مع معرّف سطر ورقم السطر الأصلي.\","` | — |
| [SRC-E599346ABE-L001557](../generate_index.py#L1557) | 1557 | `"        \"> استخراج الرموز غير Python تقريبي؛ أما فهرسة الأسطر فمخصصة للوصول إلى النص الموجود وليست حكمًا على صحته.\","` | — |
| [SRC-E599346ABE-L001558](../generate_index.py#L1558) | 1558 | `"        \"\","` | — |
| [SRC-E599346ABE-L001559](../generate_index.py#L1559) | 1559 | `"        \"## ملخص الفهرسة\","` | — |
| [SRC-E599346ABE-L001560](../generate_index.py#L1560) | 1560 | `"        \"\","` | — |
| [SRC-E599346ABE-L001561](../generate_index.py#L1561) | 1561 | `"        f\"- ملفات المستودع في الجرد: **{len(file_inventory)}**\","` | — |
| [SRC-E599346ABE-L001562](../generate_index.py#L1562) | 1562 | `"        f\"- ملفات Python المحللة: **{files_scanned}**\","` | — |
| [SRC-E599346ABE-L001563](../generate_index.py#L1563) | 1563 | `"        f\"- تعريفات Python المفهرسة: **{len(symbols)}**\","` | — |
| [SRC-E599346ABE-L001564](../generate_index.py#L1564) | 1564 | `"        f\"- تعريفات Python موثقة بوجود Docstring: **{documented_count}**\","` | — |
| [SRC-E599346ABE-L001565](../generate_index.py#L1565) | 1565 | `"        f\"- تعريفات Python بلا Docstring: **{missing_count}**\","` | — |
| [SRC-E599346ABE-L001566](../generate_index.py#L1566) | 1566 | `"        f\"- تعريفات لا ينطبق عليها Docstring: **{not_applicable_count}**\","` | — |
| [SRC-E599346ABE-L001567](../generate_index.py#L1567) | 1567 | `"        f\"- الرموز الساكنة الإضافية: **{len(marker_inventory)}**\","` | — |
| [SRC-E599346ABE-L001568](../generate_index.py#L1568) | 1568 | `"        f\"- الأسطر النصية المفهرسة حرفيًا: **{len(line_inventory)}**\","` | — |
| [SRC-E599346ABE-L001569](../generate_index.py#L1569) | 1569 | `"        f\"- وسوم المراجعة/الإصلاح المسجلة: **{len(finding_inventory)}**\","` | — |
| [SRC-E599346ABE-L001570](../generate_index.py#L1570) | 1570 | `"        \"\","` | — |
| [SRC-E599346ABE-L001571](../generate_index.py#L1571) | 1571 | `"        \"- فهرس الأسطر الكامل: [SOURCE LINES INDEX](SOURCE_LINES_INDEX.md)\","` | — |
| [SRC-E599346ABE-L001572](../generate_index.py#L1572) | 1572 | `"        \"- تدقيق التغطية والاستثناءات: [INDEX COVERAGE AUDIT](INDEX_COVERAGE_AUDIT.md)\","` | — |
| [SRC-E599346ABE-L001573](../generate_index.py#L1573) | 1573 | `"        \"- كل سجل سطر يحمل معرّفًا من الشكل SRC-<FILEHASH>-L000001.\","` | — |
| [SRC-E599346ABE-L001574](../generate_index.py#L1574) | 1574 | `"        \"\","` | — |
| [SRC-E599346ABE-L001575](../generate_index.py#L1575) | 1575 | `"        \"## جرد ملفات المستودع\","` | — |
| [SRC-E599346ABE-L001576](../generate_index.py#L1576) | 1576 | `"        \"\","` | — |
| [SRC-E599346ABE-L001577](../generate_index.py#L1577) | 1577 | `"        (\"يشمل الملفات المؤهلة من الشفرة والواجهة والاختبارات والوثائق والإعدادات وCI. \""` | — |
| [SRC-E599346ABE-L001578](../generate_index.py#L1578) | 1578 | `"        \"يُستثنى ملف الفهرس المولّد نفسه لتجنب الحلقة الذاتية، كما تُستثنى المجلدات المولّدة \""` | — |
| [SRC-E599346ABE-L001579](../generate_index.py#L1579) | 1579 | `"        \"والبيئات والملفات المحلية الحساسة وقواعد البيانات والمفاتيح المعروفة.\"),"` | — |
| [SRC-E599346ABE-L001580](../generate_index.py#L1580) | 1580 | `"        \"\","` | — |
| [SRC-E599346ABE-L001581](../generate_index.py#L1581) | 1581 | `"        \"\| معرّف الملف \| التصنيف \| الملف \| النوع \| الحجم (بايت) \| عدد الأسطر \| نطاق الفهرسة \|\","` | — |
| [SRC-E599346ABE-L001582](../generate_index.py#L1582) | 1582 | `"        \"\|---\|---\|---\|---\|---:\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001583](../generate_index.py#L1583) | 1583 | `"    ]"` | — |
| [SRC-E599346ABE-L001584](../generate_index.py#L1584) | 1584 | `""` | — |
| [SRC-E599346ABE-L001585](../generate_index.py#L1585) | 1585 | `"    if file_inventory:"` | — |
| [SRC-E599346ABE-L001586](../generate_index.py#L1586) | 1586 | `"        for item in file_inventory:"` | — |
| [SRC-E599346ABE-L001587](../generate_index.py#L1587) | 1587 | `"            line_count = str(item.line_count) if item.line_count is not None else \"غير متاح\""` | — |
| [SRC-E599346ABE-L001588](../generate_index.py#L1588) | 1588 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001589](../generate_index.py#L1589) | 1589 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001590](../generate_index.py#L1590) | 1590 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001591](../generate_index.py#L1591) | 1591 | `"                    ("` | — |
| [SRC-E599346ABE-L001592](../generate_index.py#L1592) | 1592 | `"                        item.file_id,"` | — |
| [SRC-E599346ABE-L001593](../generate_index.py#L1593) | 1593 | `"                        _markdown_cell(item.category),"` | — |
| [SRC-E599346ABE-L001594](../generate_index.py#L1594) | 1594 | `"                        f\"[{_markdown_cell(item.file)}]({_source_file_href(item.file)})\","` | — |
| [SRC-E599346ABE-L001595](../generate_index.py#L1595) | 1595 | `"                        _markdown_cell(item.file_type),"` | — |
| [SRC-E599346ABE-L001596](../generate_index.py#L1596) | 1596 | `"                        str(item.size_bytes),"` | — |
| [SRC-E599346ABE-L001597](../generate_index.py#L1597) | 1597 | `"                        line_count,"` | — |
| [SRC-E599346ABE-L001598](../generate_index.py#L1598) | 1598 | `"                        _markdown_cell(item.indexing_scope),"` | — |
| [SRC-E599346ABE-L001599](../generate_index.py#L1599) | 1599 | `"                    )"` | — |
| [SRC-E599346ABE-L001600](../generate_index.py#L1600) | 1600 | `"                )"` | — |
| [SRC-E599346ABE-L001601](../generate_index.py#L1601) | 1601 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001602](../generate_index.py#L1602) | 1602 | `"            )"` | — |
| [SRC-E599346ABE-L001603](../generate_index.py#L1603) | 1603 | `"    else:"` | — |
| [SRC-E599346ABE-L001604](../generate_index.py#L1604) | 1604 | `"        lines.append(\"\| — \| — \| — \| — \| — \| — \| لم يُمرر جرد ملفات إلى المولّد. \|\")"` | — |
| [SRC-E599346ABE-L001605](../generate_index.py#L1605) | 1605 | `""` | — |
| [SRC-E599346ABE-L001606](../generate_index.py#L1606) | 1606 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001607](../generate_index.py#L1607) | 1607 | `"        ["` | — |
| [SRC-E599346ABE-L001608](../generate_index.py#L1608) | 1608 | `"            \"\","` | — |
| [SRC-E599346ABE-L001609](../generate_index.py#L1609) | 1609 | `"            \"## تعريفات Python من AST\","` | — |
| [SRC-E599346ABE-L001610](../generate_index.py#L1610) | 1610 | `"            \"\","` | — |
| [SRC-E599346ABE-L001611](../generate_index.py#L1611) | 1611 | `"            (\"> تُحسب حالة Docstring للدوال والكلاسات فقط. المتغيرات والثوابت لا تُصنّف \""` | — |
| [SRC-E599346ABE-L001612](../generate_index.py#L1612) | 1612 | `"            \"على أنها موثقة أو ناقصة Docstring.\"),"` | — |
| [SRC-E599346ABE-L001613](../generate_index.py#L1613) | 1613 | `"            \"\","` | — |
| [SRC-E599346ABE-L001614](../generate_index.py#L1614) | 1614 | `"            \"\| الملف \| النوع \| الاسم المؤهل \| الوصف \| حالة Docstring \| السطر \| كود السطر للوصول المباشر \|\","` | — |
| [SRC-E599346ABE-L001615](../generate_index.py#L1615) | 1615 | `"            \"\|---\|---\|---\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001616](../generate_index.py#L1616) | 1616 | `"        ]"` | — |
| [SRC-E599346ABE-L001617](../generate_index.py#L1617) | 1617 | `"    )"` | — |
| [SRC-E599346ABE-L001618](../generate_index.py#L1618) | 1618 | `""` | — |
| [SRC-E599346ABE-L001619](../generate_index.py#L1619) | 1619 | `"    if not symbols:"` | — |
| [SRC-E599346ABE-L001620](../generate_index.py#L1620) | 1620 | `"        lines.append(\"\| — \| — \| — \| لا توجد تعريفات Python في الملفات المؤهلة. \| — \| — \| — \|\")"` | — |
| [SRC-E599346ABE-L001621](../generate_index.py#L1621) | 1621 | `"    else:"` | — |
| [SRC-E599346ABE-L001622](../generate_index.py#L1622) | 1622 | `"        for symbol in symbols:"` | — |
| [SRC-E599346ABE-L001623](../generate_index.py#L1623) | 1623 | `"            if symbol.documented is True:"` | — |
| [SRC-E599346ABE-L001624](../generate_index.py#L1624) | 1624 | `"                status = \"موثق\""` | — |
| [SRC-E599346ABE-L001625](../generate_index.py#L1625) | 1625 | `"            elif symbol.documented is False:"` | — |
| [SRC-E599346ABE-L001626](../generate_index.py#L1626) | 1626 | `"                status = \"ناقص\""` | — |
| [SRC-E599346ABE-L001627](../generate_index.py#L1627) | 1627 | `"            else:"` | — |
| [SRC-E599346ABE-L001628](../generate_index.py#L1628) | 1628 | `"                status = \"لا ينطبق\""` | — |
| [SRC-E599346ABE-L001629](../generate_index.py#L1629) | 1629 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001630](../generate_index.py#L1630) | 1630 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001631](../generate_index.py#L1631) | 1631 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001632](../generate_index.py#L1632) | 1632 | `"                    ("` | — |
| [SRC-E599346ABE-L001633](../generate_index.py#L1633) | 1633 | `"                        f\"[{_markdown_cell(symbol.file)}]({_source_file_href(symbol.file, symbol.line)})\","` | — |
| [SRC-E599346ABE-L001634](../generate_index.py#L1634) | 1634 | `"                        _markdown_cell(symbol.kind),"` | — |
| [SRC-E599346ABE-L001635](../generate_index.py#L1635) | 1635 | `"                        _markdown_cell(symbol.name),"` | — |
| [SRC-E599346ABE-L001636](../generate_index.py#L1636) | 1636 | `"                        _markdown_cell(symbol.description),"` | — |
| [SRC-E599346ABE-L001637](../generate_index.py#L1637) | 1637 | `"                        status,"` | — |
| [SRC-E599346ABE-L001638](../generate_index.py#L1638) | 1638 | `"                        str(symbol.line),"` | — |
| [SRC-E599346ABE-L001639](../generate_index.py#L1639) | 1639 | `"                        f\"[{_source_line_id(symbol.file, symbol.line)}]({_source_file_href(symbol.file, symbol.line)})\","` | — |
| [SRC-E599346ABE-L001640](../generate_index.py#L1640) | 1640 | `"                    )"` | — |
| [SRC-E599346ABE-L001641](../generate_index.py#L1641) | 1641 | `"                )"` | — |
| [SRC-E599346ABE-L001642](../generate_index.py#L1642) | 1642 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001643](../generate_index.py#L1643) | 1643 | `"            )"` | — |
| [SRC-E599346ABE-L001644](../generate_index.py#L1644) | 1644 | `""` | — |
| [SRC-E599346ABE-L001645](../generate_index.py#L1645) | 1645 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001646](../generate_index.py#L1646) | 1646 | `"        ["` | — |
| [SRC-E599346ABE-L001647](../generate_index.py#L1647) | 1647 | `"            \"\","` | — |
| [SRC-E599346ABE-L001648](../generate_index.py#L1648) | 1648 | `"            \"## الرموز الساكنة الإضافية\","` | — |
| [SRC-E599346ABE-L001649](../generate_index.py#L1649) | 1649 | `"            \"\","` | — |
| [SRC-E599346ABE-L001650](../generate_index.py#L1650) | 1650 | `"            (\"هذا القسم للمساعدة في الوصول إلى الواجهة والإعدادات والوثائق؛ \""` | — |
| [SRC-E599346ABE-L001651](../generate_index.py#L1651) | 1651 | `"            \"استخراج الرموز غير المحللة بـAST استدلالي وقد لا يساوي تحليلًا كاملًا للغة.\"),"` | — |
| [SRC-E599346ABE-L001652](../generate_index.py#L1652) | 1652 | `"            \"\","` | — |
| [SRC-E599346ABE-L001653](../generate_index.py#L1653) | 1653 | `"            \"\| الملف \| نوع الرمز \| الاسم/القيمة \| السطر \| كود السطر للوصول المباشر \|\","` | — |
| [SRC-E599346ABE-L001654](../generate_index.py#L1654) | 1654 | `"            \"\|---\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001655](../generate_index.py#L1655) | 1655 | `"        ]"` | — |
| [SRC-E599346ABE-L001656](../generate_index.py#L1656) | 1656 | `"    )"` | — |
| [SRC-E599346ABE-L001657](../generate_index.py#L1657) | 1657 | `"    if marker_inventory:"` | — |
| [SRC-E599346ABE-L001658](../generate_index.py#L1658) | 1658 | `"        for marker in marker_inventory:"` | — |
| [SRC-E599346ABE-L001659](../generate_index.py#L1659) | 1659 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001660](../generate_index.py#L1660) | 1660 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001661](../generate_index.py#L1661) | 1661 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001662](../generate_index.py#L1662) | 1662 | `"                    ("` | — |
| [SRC-E599346ABE-L001663](../generate_index.py#L1663) | 1663 | `"                        f\"[{_markdown_cell(marker.file)}]({_source_file_href(marker.file, marker.line)})\","` | — |
| [SRC-E599346ABE-L001664](../generate_index.py#L1664) | 1664 | `"                        _markdown_cell(marker.kind),"` | — |
| [SRC-E599346ABE-L001665](../generate_index.py#L1665) | 1665 | `"                        _markdown_cell(marker.name),"` | — |
| [SRC-E599346ABE-L001666](../generate_index.py#L1666) | 1666 | `"                        str(marker.line),"` | — |
| [SRC-E599346ABE-L001667](../generate_index.py#L1667) | 1667 | `"                        f\"[{_source_line_id(marker.file, marker.line)}]({_source_file_href(marker.file, marker.line)})\","` | — |
| [SRC-E599346ABE-L001668](../generate_index.py#L1668) | 1668 | `"                    )"` | — |
| [SRC-E599346ABE-L001669](../generate_index.py#L1669) | 1669 | `"                )"` | — |
| [SRC-E599346ABE-L001670](../generate_index.py#L1670) | 1670 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001671](../generate_index.py#L1671) | 1671 | `"            )"` | — |
| [SRC-E599346ABE-L001672](../generate_index.py#L1672) | 1672 | `"    else:"` | — |
| [SRC-E599346ABE-L001673](../generate_index.py#L1673) | 1673 | `"        lines.append(\"\| — \| — \| — \| لم تُكتشف رموز ساكنة إضافية. \| — \|\")"` | — |
| [SRC-E599346ABE-L001674](../generate_index.py#L1674) | 1674 | `""` | — |
| [SRC-E599346ABE-L001675](../generate_index.py#L1675) | 1675 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001676](../generate_index.py#L1676) | 1676 | `"        ["` | — |
| [SRC-E599346ABE-L001677](../generate_index.py#L1677) | 1677 | `"            \"\","` | — |
| [SRC-E599346ABE-L001678](../generate_index.py#L1678) | 1678 | `"            \"## سجل وسوم المراجعة والإصلاح\","` | — |
| [SRC-E599346ABE-L001679](../generate_index.py#L1679) | 1679 | `"            \"\","` | — |
| [SRC-E599346ABE-L001680](../generate_index.py#L1680) | 1680 | `"            \"هذه قائمة بالوسوم الصريحة التي تستدعي المتابعة. وجود الوسم ليس إثباتًا آليًا أن السطر معيب؛ افتح الملف عند رقم السطر وراجع السياق.\","` | — |
| [SRC-E599346ABE-L001681](../generate_index.py#L1681) | 1681 | `"            \"\","` | — |
| [SRC-E599346ABE-L001682](../generate_index.py#L1682) | 1682 | `"            \"\| كود الهفوة/الوسم \| النوع \| الملف \| السطر \| وصف الوسم \| كود السطر \| نص السطر \|\","` | — |
| [SRC-E599346ABE-L001683](../generate_index.py#L1683) | 1683 | `"            \"\|---\|---\|---\|---:\|---\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001684](../generate_index.py#L1684) | 1684 | `"        ]"` | — |
| [SRC-E599346ABE-L001685](../generate_index.py#L1685) | 1685 | `"    )"` | — |
| [SRC-E599346ABE-L001686](../generate_index.py#L1686) | 1686 | `"    if finding_inventory:"` | — |
| [SRC-E599346ABE-L001687](../generate_index.py#L1687) | 1687 | `"        line_map = {source_line.line_id: source_line for source_line in line_inventory}"` | — |
| [SRC-E599346ABE-L001688](../generate_index.py#L1688) | 1688 | `"        for finding in finding_inventory:"` | — |
| [SRC-E599346ABE-L001689](../generate_index.py#L1689) | 1689 | `"            source_line = line_map.get(finding.line_id)"` | — |
| [SRC-E599346ABE-L001690](../generate_index.py#L1690) | 1690 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001691](../generate_index.py#L1691) | 1691 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001692](../generate_index.py#L1692) | 1692 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001693](../generate_index.py#L1693) | 1693 | `"                    ("` | — |
| [SRC-E599346ABE-L001694](../generate_index.py#L1694) | 1694 | `"                        finding.finding_id,"` | — |
| [SRC-E599346ABE-L001695](../generate_index.py#L1695) | 1695 | `"                        finding.marker,"` | — |
| [SRC-E599346ABE-L001696](../generate_index.py#L1696) | 1696 | `"                        f\"[{_markdown_cell(finding.file)}]({_source_file_href(finding.file, source_line.line if source_line else 1)})\","` | — |
| [SRC-E599346ABE-L001697](../generate_index.py#L1697) | 1697 | `"                        str(source_line.line if source_line else \"غير متاح\"),"` | — |
| [SRC-E599346ABE-L001698](../generate_index.py#L1698) | 1698 | `"                        _markdown_cell(finding.description),"` | — |
| [SRC-E599346ABE-L001699](../generate_index.py#L1699) | 1699 | `"                        f\"[{finding.line_id}]({_source_file_href(finding.file, source_line.line if source_line else 1)})\","` | — |
| [SRC-E599346ABE-L001700](../generate_index.py#L1700) | 1700 | `"                        _markdown_code_span(json.dumps(source_line.content, ensure_ascii=False).replace(\"\|\", r\"\\\|\")) if source_line else \"غير متاح\","` | — |
| [SRC-E599346ABE-L001701](../generate_index.py#L1701) | 1701 | `"                    )"` | — |
| [SRC-E599346ABE-L001702](../generate_index.py#L1702) | 1702 | `"                )"` | — |
| [SRC-E599346ABE-L001703](../generate_index.py#L1703) | 1703 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001704](../generate_index.py#L1704) | 1704 | `"            )"` | — |
| [SRC-E599346ABE-L001705](../generate_index.py#L1705) | 1705 | `"    else:"` | — |
| [SRC-E599346ABE-L001706](../generate_index.py#L1706) | 1706 | `"        lines.append(\"\| — \| — \| — \| — \| لم تُكتشف وسوم صريحة من الأنواع المعروفة. \| — \| — \|\")"` | — |
| [SRC-E599346ABE-L001707](../generate_index.py#L1707) | 1707 | `""` | — |
| [SRC-E599346ABE-L001708](../generate_index.py#L1708) | 1708 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001709](../generate_index.py#L1709) | 1709 | `"        ["` | — |
| [SRC-E599346ABE-L001710](../generate_index.py#L1710) | 1710 | `"            \"\","` | — |
| [SRC-E599346ABE-L001711](../generate_index.py#L1711) | 1711 | `"            \"---\","` | — |
| [SRC-E599346ABE-L001712](../generate_index.py#L1712) | 1712 | `"            \"\","` | — |
| [SRC-E599346ABE-L001713](../generate_index.py#L1713) | 1713 | `"            \"## حدود الفهرسة\","` | — |
| [SRC-E599346ABE-L001714](../generate_index.py#L1714) | 1714 | `"            \"\","` | — |
| [SRC-E599346ABE-L001715](../generate_index.py#L1715) | 1715 | `"            \"- كل الأسطر المنطقية للملفات النصية المؤهلة القابلة للقراءة مفهرسة في SOURCE LINES INDEX، لا في هذا الجدول المختصر.\","` | — |
| [SRC-E599346ABE-L001716](../generate_index.py#L1716) | 1716 | `"            \"- الملفات الأكبر من 2 MiB أو غير القابلة للقراءة أو الثنائية تبقى ضمن الجرد الوصفي، دون فهرسة سطورها.\","` | — |
| [SRC-E599346ABE-L001717](../generate_index.py#L1717) | 1717 | `"            \"- لا تُفحص محتويات البيئة الافتراضية والاعتماديات والمجلدات المولدة.\","` | — |
| [SRC-E599346ABE-L001718](../generate_index.py#L1718) | 1718 | `"            \"- لا تُقرأ ملفات البيئة المحلية وقواعد البيانات والمفاتيح المعروفة.\","` | — |
| [SRC-E599346ABE-L001719](../generate_index.py#L1719) | 1719 | `"            \"- تحليل Python يرفض إنشاء فهرس جزئي عند وجود خطأ نحوي في أي ملف Python مؤهل.\","` | — |
| [SRC-E599346ABE-L001720](../generate_index.py#L1720) | 1720 | `"            (\"- يُحدّث هذا الفهرس آليًا عبر GitHub Actions عند دفع تغيير إلى main؛ \""` | — |
| [SRC-E599346ABE-L001721](../generate_index.py#L1721) | 1721 | `"            \"وتظل تغييرات المصدر قيد المراجعة حتى تُدمج وفق سياسة المستودع.\"),"` | — |
| [SRC-E599346ABE-L001722](../generate_index.py#L1722) | 1722 | `"            \"\","` | — |
| [SRC-E599346ABE-L001723](../generate_index.py#L1723) | 1723 | `"        ]"` | — |
| [SRC-E599346ABE-L001724](../generate_index.py#L1724) | 1724 | `"    )"` | — |
| [SRC-E599346ABE-L001725](../generate_index.py#L1725) | 1725 | `"    return \"\\n\".join(lines)"` | — |
| [SRC-E599346ABE-L001726](../generate_index.py#L1726) | 1726 | `""` | — |
| [SRC-E599346ABE-L001727](../generate_index.py#L1727) | 1727 | `""` | — |
| [SRC-E599346ABE-L001728](../generate_index.py#L1728) | 1728 | `"def write_if_changed(output_path: Path, content: str) -> bool:"` | — |
| [SRC-E599346ABE-L001729](../generate_index.py#L1729) | 1729 | `"    \"\"\"Write atomically only when the generated index differs from the existing file.\"\"\""` | — |
| [SRC-E599346ABE-L001730](../generate_index.py#L1730) | 1730 | `"    output_path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-E599346ABE-L001731](../generate_index.py#L1731) | 1731 | `"    try:"` | — |
| [SRC-E599346ABE-L001732](../generate_index.py#L1732) | 1732 | `"        if output_path.read_text(encoding=\"utf-8\") == content:"` | — |
| [SRC-E599346ABE-L001733](../generate_index.py#L1733) | 1733 | `"            return False"` | — |
| [SRC-E599346ABE-L001734](../generate_index.py#L1734) | 1734 | `"    except FileNotFoundError:"` | — |
| [SRC-E599346ABE-L001735](../generate_index.py#L1735) | 1735 | `"        pass"` | — |
| [SRC-E599346ABE-L001736](../generate_index.py#L1736) | 1736 | `""` | — |
| [SRC-E599346ABE-L001737](../generate_index.py#L1737) | 1737 | `"    temporary_path: Path \| None = None"` | — |
| [SRC-E599346ABE-L001738](../generate_index.py#L1738) | 1738 | `"    try:"` | — |
| [SRC-E599346ABE-L001739](../generate_index.py#L1739) | 1739 | `"        with tempfile.NamedTemporaryFile("` | — |
| [SRC-E599346ABE-L001740](../generate_index.py#L1740) | 1740 | `"            mode=\"w\","` | — |
| [SRC-E599346ABE-L001741](../generate_index.py#L1741) | 1741 | `"            encoding=\"utf-8\","` | — |
| [SRC-E599346ABE-L001742](../generate_index.py#L1742) | 1742 | `"            newline=\"\\n\","` | — |
| [SRC-E599346ABE-L001743](../generate_index.py#L1743) | 1743 | `"            dir=output_path.parent,"` | — |
| [SRC-E599346ABE-L001744](../generate_index.py#L1744) | 1744 | `"            prefix=f\".{output_path.name}.\","` | — |
| [SRC-E599346ABE-L001745](../generate_index.py#L1745) | 1745 | `"            suffix=\".tmp\","` | — |
| [SRC-E599346ABE-L001746](../generate_index.py#L1746) | 1746 | `"            delete=False,"` | — |
| [SRC-E599346ABE-L001747](../generate_index.py#L1747) | 1747 | `"        ) as temporary_file:"` | — |
| [SRC-E599346ABE-L001748](../generate_index.py#L1748) | 1748 | `"            temporary_file.write(content)"` | — |
| [SRC-E599346ABE-L001749](../generate_index.py#L1749) | 1749 | `"            temporary_path = Path(temporary_file.name)"` | — |
| [SRC-E599346ABE-L001750](../generate_index.py#L1750) | 1750 | `"        temporary_path.replace(output_path)"` | — |
| [SRC-E599346ABE-L001751](../generate_index.py#L1751) | 1751 | `"    finally:"` | — |
| [SRC-E599346ABE-L001752](../generate_index.py#L1752) | 1752 | `"        if temporary_path is not None and temporary_path.exists():"` | — |
| [SRC-E599346ABE-L001753](../generate_index.py#L1753) | 1753 | `"            temporary_path.unlink()"` | — |
| [SRC-E599346ABE-L001754](../generate_index.py#L1754) | 1754 | `"    return True"` | — |
| [SRC-E599346ABE-L001755](../generate_index.py#L1755) | 1755 | `""` | — |
| [SRC-E599346ABE-L001756](../generate_index.py#L1756) | 1756 | `""` | — |
| [SRC-E599346ABE-L001757](../generate_index.py#L1757) | 1757 | `"def _generate("` | — |
| [SRC-E599346ABE-L001758](../generate_index.py#L1758) | 1758 | `"    root: Path,"` | — |
| [SRC-E599346ABE-L001759](../generate_index.py#L1759) | 1759 | `") -> tuple[str, str, str, dict[str, str], int, int, int, int, int, int, int]:"` | — |
| [SRC-E599346ABE-L001760](../generate_index.py#L1760) | 1760 | `"    \"\"\"Create deterministic overview, source-line pages, and all counts without writing.\"\"\""` | — |
| [SRC-E599346ABE-L001761](../generate_index.py#L1761) | 1761 | `"    inventory = build_file_inventory(root)"` | — |
| [SRC-E599346ABE-L001762](../generate_index.py#L1762) | 1762 | `"    symbols, python_file_count = scan_repository(root)"` | — |
| [SRC-E599346ABE-L001763](../generate_index.py#L1763) | 1763 | `"    static_symbols = scan_static_symbols(root, inventory)"` | — |
| [SRC-E599346ABE-L001764](../generate_index.py#L1764) | 1764 | `"    source_lines = scan_source_lines(root, inventory)"` | — |
| [SRC-E599346ABE-L001765](../generate_index.py#L1765) | 1765 | `"    validate_source_line_coverage(inventory, source_lines)"` | — |
| [SRC-E599346ABE-L001766](../generate_index.py#L1766) | 1766 | `"    findings = scan_finding_annotations(source_lines)"` | — |
| [SRC-E599346ABE-L001767](../generate_index.py#L1767) | 1767 | `"    excluded_paths = discover_excluded_paths(root)"` | — |
| [SRC-E599346ABE-L001768](../generate_index.py#L1768) | 1768 | `"    coverage_audit_markdown = render_coverage_audit_markdown("` | — |
| [SRC-E599346ABE-L001769](../generate_index.py#L1769) | 1769 | `"        root, inventory, source_lines, excluded_paths"` | — |
| [SRC-E599346ABE-L001770](../generate_index.py#L1770) | 1770 | `"    )"` | — |
| [SRC-E599346ABE-L001771](../generate_index.py#L1771) | 1771 | `"    source_pages, pages_by_file = render_source_line_pages("` | — |
| [SRC-E599346ABE-L001772](../generate_index.py#L1772) | 1772 | `"        source_lines, inventory, findings"` | — |
| [SRC-E599346ABE-L001773](../generate_index.py#L1773) | 1773 | `"    )"` | — |
| [SRC-E599346ABE-L001774](../generate_index.py#L1774) | 1774 | `"    markdown = render_markdown("` | — |
| [SRC-E599346ABE-L001775](../generate_index.py#L1775) | 1775 | `"        symbols, python_file_count, inventory, static_symbols, source_lines, findings"` | — |
| [SRC-E599346ABE-L001776](../generate_index.py#L1776) | 1776 | `"    )"` | — |
| [SRC-E599346ABE-L001777](../generate_index.py#L1777) | 1777 | `"    source_lines_markdown = render_source_lines_markdown("` | — |
| [SRC-E599346ABE-L001778](../generate_index.py#L1778) | 1778 | `"        source_lines, inventory, findings, pages_by_file, source_pages"` | — |
| [SRC-E599346ABE-L001779](../generate_index.py#L1779) | 1779 | `"    )"` | — |
| [SRC-E599346ABE-L001780](../generate_index.py#L1780) | 1780 | `"    return ("` | — |
| [SRC-E599346ABE-L001781](../generate_index.py#L1781) | 1781 | `"        markdown,"` | — |
| [SRC-E599346ABE-L001782](../generate_index.py#L1782) | 1782 | `"        source_lines_markdown,"` | — |
| [SRC-E599346ABE-L001783](../generate_index.py#L1783) | 1783 | `"        coverage_audit_markdown,"` | — |
| [SRC-E599346ABE-L001784](../generate_index.py#L1784) | 1784 | `"        source_pages,"` | — |
| [SRC-E599346ABE-L001785](../generate_index.py#L1785) | 1785 | `"        python_file_count,"` | — |
| [SRC-E599346ABE-L001786](../generate_index.py#L1786) | 1786 | `"        len(inventory),"` | — |
| [SRC-E599346ABE-L001787](../generate_index.py#L1787) | 1787 | `"        len(symbols),"` | — |
| [SRC-E599346ABE-L001788](../generate_index.py#L1788) | 1788 | `"        len(source_lines),"` | — |
| [SRC-E599346ABE-L001789](../generate_index.py#L1789) | 1789 | `"        len(findings),"` | — |
| [SRC-E599346ABE-L001790](../generate_index.py#L1790) | 1790 | `"        sum(symbol.documented is True for symbol in symbols),"` | — |
| [SRC-E599346ABE-L001791](../generate_index.py#L1791) | 1791 | `"        sum(symbol.documented is False for symbol in symbols),"` | — |
| [SRC-E599346ABE-L001792](../generate_index.py#L1792) | 1792 | `"    )"` | — |
| [SRC-E599346ABE-L001793](../generate_index.py#L1793) | 1793 | `""` | — |
| [SRC-E599346ABE-L001794](../generate_index.py#L1794) | 1794 | `""` | — |
| [SRC-E599346ABE-L001795](../generate_index.py#L1795) | 1795 | `"def main(argv: Sequence[str] \| None = None) -> int:"` | — |
| [SRC-E599346ABE-L001796](../generate_index.py#L1796) | 1796 | `"    \"\"\"Generate the living repository index or check that the committed copy is current.\"\"\""` | — |
| [SRC-E599346ABE-L001797](../generate_index.py#L1797) | 1797 | `"    parser = argparse.ArgumentParser("` | — |
| [SRC-E599346ABE-L001798](../generate_index.py#L1798) | 1798 | `"        description=\"إنشاء/فحص فهرس مستودع Omarai وملفات الشفرة والرموز الساكنة.\""` | — |
| [SRC-E599346ABE-L001799](../generate_index.py#L1799) | 1799 | `"    )"` | — |
| [SRC-E599346ABE-L001800](../generate_index.py#L1800) | 1800 | `"    parser.add_argument("` | — |
| [SRC-E599346ABE-L001801](../generate_index.py#L1801) | 1801 | `"        \"--root\","` | — |
| [SRC-E599346ABE-L001802](../generate_index.py#L1802) | 1802 | `"        type=Path,"` | — |
| [SRC-E599346ABE-L001803](../generate_index.py#L1803) | 1803 | `"        default=Path(__file__).resolve().parents[1],"` | — |
| [SRC-E599346ABE-L001804](../generate_index.py#L1804) | 1804 | `"        help=\"مسار جذر المستودع (الافتراضي: جذر مشروع Omarai).\","` | — |
| [SRC-E599346ABE-L001805](../generate_index.py#L1805) | 1805 | `"    )"` | — |
| [SRC-E599346ABE-L001806](../generate_index.py#L1806) | 1806 | `"    parser.add_argument("` | — |
| [SRC-E599346ABE-L001807](../generate_index.py#L1807) | 1807 | `"        \"--check\","` | — |
| [SRC-E599346ABE-L001808](../generate_index.py#L1808) | 1808 | `"        action=\"store_true\","` | — |
| [SRC-E599346ABE-L001809](../generate_index.py#L1809) | 1809 | `"        help=\"لا تكتب ملفات؛ أعد حالة فشل إذا كان أي فهرس مولّد قديمًا أو مفقودًا.\","` | — |
| [SRC-E599346ABE-L001810](../generate_index.py#L1810) | 1810 | `"    )"` | — |
| [SRC-E599346ABE-L001811](../generate_index.py#L1811) | 1811 | `"    arguments = parser.parse_args(argv)"` | — |
| [SRC-E599346ABE-L001812](../generate_index.py#L1812) | 1812 | `""` | — |
| [SRC-E599346ABE-L001813](../generate_index.py#L1813) | 1813 | `"    try:"` | — |
| [SRC-E599346ABE-L001814](../generate_index.py#L1814) | 1814 | `"        root = arguments.root.resolve(strict=True)"` | — |
| [SRC-E599346ABE-L001815](../generate_index.py#L1815) | 1815 | `"        if not root.is_dir():"` | — |
| [SRC-E599346ABE-L001816](../generate_index.py#L1816) | 1816 | `"            raise ValueError(f\"المسار المحدد ليس مجلدًا: {root}\")"` | — |
| [SRC-E599346ABE-L001817](../generate_index.py#L1817) | 1817 | `"        ("` | — |
| [SRC-E599346ABE-L001818](../generate_index.py#L1818) | 1818 | `"            markdown,"` | — |
| [SRC-E599346ABE-L001819](../generate_index.py#L1819) | 1819 | `"            source_lines_markdown,"` | — |
| [SRC-E599346ABE-L001820](../generate_index.py#L1820) | 1820 | `"            coverage_audit_markdown,"` | — |
| [SRC-E599346ABE-L001821](../generate_index.py#L1821) | 1821 | `"            source_pages,"` | — |
| [SRC-E599346ABE-L001822](../generate_index.py#L1822) | 1822 | `"            python_file_count,"` | — |
| [SRC-E599346ABE-L001823](../generate_index.py#L1823) | 1823 | `"            repository_file_count,"` | — |
| [SRC-E599346ABE-L001824](../generate_index.py#L1824) | 1824 | `"            symbol_count,"` | — |
| [SRC-E599346ABE-L001825](../generate_index.py#L1825) | 1825 | `"            source_line_count,"` | — |
| [SRC-E599346ABE-L001826](../generate_index.py#L1826) | 1826 | `"            finding_count,"` | — |
| [SRC-E599346ABE-L001827](../generate_index.py#L1827) | 1827 | `"            documented_count,"` | — |
| [SRC-E599346ABE-L001828](../generate_index.py#L1828) | 1828 | `"            missing_count,"` | — |
| [SRC-E599346ABE-L001829](../generate_index.py#L1829) | 1829 | `"        ) = _generate(root)"` | — |
| [SRC-E599346ABE-L001830](../generate_index.py#L1830) | 1830 | `"        output_path = root / INDEX_RELATIVE_PATH"` | — |
| [SRC-E599346ABE-L001831](../generate_index.py#L1831) | 1831 | `"        source_lines_output_path = root / SOURCE_LINES_INDEX_RELATIVE_PATH"` | — |
| [SRC-E599346ABE-L001832](../generate_index.py#L1832) | 1832 | `"        generated_outputs = {"` | — |
| [SRC-E599346ABE-L001833](../generate_index.py#L1833) | 1833 | `"            INDEX_RELATIVE_PATH: markdown,"` | — |
| [SRC-E599346ABE-L001834](../generate_index.py#L1834) | 1834 | `"            SOURCE_LINES_INDEX_RELATIVE_PATH: source_lines_markdown,"` | — |
| [SRC-E599346ABE-L001835](../generate_index.py#L1835) | 1835 | `"            COVERAGE_AUDIT_RELATIVE_PATH: coverage_audit_markdown,"` | — |
| [SRC-E599346ABE-L001836](../generate_index.py#L1836) | 1836 | `"            **source_pages,"` | — |
| [SRC-E599346ABE-L001837](../generate_index.py#L1837) | 1837 | `"        }"` | — |
| [SRC-E599346ABE-L001838](../generate_index.py#L1838) | 1838 | `""` | — |
| [SRC-E599346ABE-L001839](../generate_index.py#L1839) | 1839 | `"        if arguments.check:"` | — |
| [SRC-E599346ABE-L001840](../generate_index.py#L1840) | 1840 | `"            for relative_path, expected_content in generated_outputs.items():"` | — |
| [SRC-E599346ABE-L001841](../generate_index.py#L1841) | 1841 | `"                generated_path = root / relative_path"` | — |
| [SRC-E599346ABE-L001842](../generate_index.py#L1842) | 1842 | `"                try:"` | — |
| [SRC-E599346ABE-L001843](../generate_index.py#L1843) | 1843 | `"                    current_content = generated_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-E599346ABE-L001844](../generate_index.py#L1844) | 1844 | `"                except FileNotFoundError:"` | — |
| [SRC-E599346ABE-L001845](../generate_index.py#L1845) | 1845 | `"                    print("` | — |
| [SRC-E599346ABE-L001846](../generate_index.py#L1846) | 1846 | `"                        f\"فهرس مولّد مفقود: {generated_path}. \""` | — |
| [SRC-E599346ABE-L001847](../generate_index.py#L1847) | 1847 | `"                        \"شغّل python docs/generate_index.py.\","` | — |
| [SRC-E599346ABE-L001848](../generate_index.py#L1848) | 1848 | `"                        file=sys.stderr,"` | — |
| [SRC-E599346ABE-L001849](../generate_index.py#L1849) | 1849 | `"                    )"` | — |
| [SRC-E599346ABE-L001850](../generate_index.py#L1850) | 1850 | `"                    return 1"` | — |
| [SRC-E599346ABE-L001851](../generate_index.py#L1851) | 1851 | `"                if current_content != expected_content:"` | — |
| [SRC-E599346ABE-L001852](../generate_index.py#L1852) | 1852 | `"                    if relative_path == INDEX_RELATIVE_PATH:"` | — |
| [SRC-E599346ABE-L001853](../generate_index.py#L1853) | 1853 | `"                        message = \"الفهرس قديم (الرئيسي)\""` | — |
| [SRC-E599346ABE-L001854](../generate_index.py#L1854) | 1854 | `"                    elif relative_path == SOURCE_LINES_INDEX_RELATIVE_PATH:"` | — |
| [SRC-E599346ABE-L001855](../generate_index.py#L1855) | 1855 | `"                        message = \"فهرس الأسطر قديم\""` | — |
| [SRC-E599346ABE-L001856](../generate_index.py#L1856) | 1856 | `"                    else:"` | — |
| [SRC-E599346ABE-L001857](../generate_index.py#L1857) | 1857 | `"                        message = \"فهرس تغطية الفهرسة قديم\""` | — |
| [SRC-E599346ABE-L001858](../generate_index.py#L1858) | 1858 | `"                    print("` | — |
| [SRC-E599346ABE-L001859](../generate_index.py#L1859) | 1859 | `"                        f\"{message}: {generated_path}. \""` | — |
| [SRC-E599346ABE-L001860](../generate_index.py#L1860) | 1860 | `"                        \"شغّل python docs/generate_index.py.\","` | — |
| [SRC-E599346ABE-L001861](../generate_index.py#L1861) | 1861 | `"                        file=sys.stderr,"` | — |
| [SRC-E599346ABE-L001862](../generate_index.py#L1862) | 1862 | `"                    )"` | — |
| [SRC-E599346ABE-L001863](../generate_index.py#L1863) | 1863 | `"                    return 1"` | — |
| [SRC-E599346ABE-L001864](../generate_index.py#L1864) | 1864 | `""` | — |
| [SRC-E599346ABE-L001865](../generate_index.py#L1865) | 1865 | `"            pages_directory = root / SOURCE_LINES_PAGES_DIR"` | — |
| [SRC-E599346ABE-L001866](../generate_index.py#L1866) | 1866 | `"            expected_page_names = {"` | — |
| [SRC-E599346ABE-L001867](../generate_index.py#L1867) | 1867 | `"                Path(relative_path).name"` | — |
| [SRC-E599346ABE-L001868](../generate_index.py#L1868) | 1868 | `"                for relative_path in source_pages"` | — |
| [SRC-E599346ABE-L001869](../generate_index.py#L1869) | 1869 | `"            }"` | — |
| [SRC-E599346ABE-L001870](../generate_index.py#L1870) | 1870 | `"            if pages_directory.exists():"` | — |
| [SRC-E599346ABE-L001871](../generate_index.py#L1871) | 1871 | `"                actual_page_names = {"` | — |
| [SRC-E599346ABE-L001872](../generate_index.py#L1872) | 1872 | `"                    path.name"` | — |
| [SRC-E599346ABE-L001873](../generate_index.py#L1873) | 1873 | `"                    for path in pages_directory.iterdir()"` | — |
| [SRC-E599346ABE-L001874](../generate_index.py#L1874) | 1874 | `"                    if path.is_file() and SOURCE_LINES_PAGE_RE.fullmatch(path.name)"` | — |
| [SRC-E599346ABE-L001875](../generate_index.py#L1875) | 1875 | `"                }"` | — |
| [SRC-E599346ABE-L001876](../generate_index.py#L1876) | 1876 | `"                stale_pages = actual_page_names - expected_page_names"` | — |
| [SRC-E599346ABE-L001877](../generate_index.py#L1877) | 1877 | `"                if stale_pages:"` | — |
| [SRC-E599346ABE-L001878](../generate_index.py#L1878) | 1878 | `"                    print("` | — |
| [SRC-E599346ABE-L001879](../generate_index.py#L1879) | 1879 | `"                        \"صفحات فهرس قديمة يجب حذفها بإعادة التوليد: \""` | — |
| [SRC-E599346ABE-L001880](../generate_index.py#L1880) | 1880 | `"                        + \", \".join(sorted(stale_pages)),"` | — |
| [SRC-E599346ABE-L001881](../generate_index.py#L1881) | 1881 | `"                        file=sys.stderr,"` | — |
| [SRC-E599346ABE-L001882](../generate_index.py#L1882) | 1882 | `"                    )"` | — |
| [SRC-E599346ABE-L001883](../generate_index.py#L1883) | 1883 | `"                    return 1"` | — |
| [SRC-E599346ABE-L001884](../generate_index.py#L1884) | 1884 | `"            changed = False"` | — |
| [SRC-E599346ABE-L001885](../generate_index.py#L1885) | 1885 | `"        else:"` | — |
| [SRC-E599346ABE-L001886](../generate_index.py#L1886) | 1886 | `"            changed = False"` | — |
| [SRC-E599346ABE-L001887](../generate_index.py#L1887) | 1887 | `"            for relative_path, generated_content in generated_outputs.items():"` | — |
| [SRC-E599346ABE-L001888](../generate_index.py#L1888) | 1888 | `"                if write_if_changed(root / relative_path, generated_content):"` | — |
| [SRC-E599346ABE-L001889](../generate_index.py#L1889) | 1889 | `"                    changed = True"` | — |
| [SRC-E599346ABE-L001890](../generate_index.py#L1890) | 1890 | `""` | — |
| [SRC-E599346ABE-L001891](../generate_index.py#L1891) | 1891 | `"            pages_directory = root / SOURCE_LINES_PAGES_DIR"` | — |
| [SRC-E599346ABE-L001892](../generate_index.py#L1892) | 1892 | `"            if pages_directory.exists():"` | — |
| [SRC-E599346ABE-L001893](../generate_index.py#L1893) | 1893 | `"                expected_page_names = {"` | — |
| [SRC-E599346ABE-L001894](../generate_index.py#L1894) | 1894 | `"                    Path(relative_path).name"` | — |
| [SRC-E599346ABE-L001895](../generate_index.py#L1895) | 1895 | `"                    for relative_path in source_pages"` | — |
| [SRC-E599346ABE-L001896](../generate_index.py#L1896) | 1896 | `"                }"` | — |
| [SRC-E599346ABE-L001897](../generate_index.py#L1897) | 1897 | `"                for path in pages_directory.iterdir():"` | — |
| [SRC-E599346ABE-L001898](../generate_index.py#L1898) | 1898 | `"                    if ("` | — |
| [SRC-E599346ABE-L001899](../generate_index.py#L1899) | 1899 | `"                        path.is_file()"` | — |
| [SRC-E599346ABE-L001900](../generate_index.py#L1900) | 1900 | `"                        and SOURCE_LINES_PAGE_RE.fullmatch(path.name)"` | — |
