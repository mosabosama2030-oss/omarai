# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **011**
- سجلات الأسطر: **800**
- النطاق: SRC-E599346ABE-L001101 إلى SRC-E73001D9AC-L000028
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-E599346ABE — [docs/generate_index.py](../generate_index.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E599346ABE-L001101](../generate_index.py#L1101) | 1101 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001102](../generate_index.py#L1102) | 1102 | `"            )"` | — |
| [SRC-E599346ABE-L001103](../generate_index.py#L1103) | 1103 | `"            refs = pages_by_file.setdefault(source_line.file, [])"` | — |
| [SRC-E599346ABE-L001104](../generate_index.py#L1104) | 1104 | `"            if page_path not in refs:"` | — |
| [SRC-E599346ABE-L001105](../generate_index.py#L1105) | 1105 | `"                refs.append(page_path)"` | — |
| [SRC-E599346ABE-L001106](../generate_index.py#L1106) | 1106 | `"        pages[page_path] = \"\\n\".join(lines) + \"\\n\""` | — |
| [SRC-E599346ABE-L001107](../generate_index.py#L1107) | 1107 | `""` | — |
| [SRC-E599346ABE-L001108](../generate_index.py#L1108) | 1108 | `"    return pages, pages_by_file"` | — |
| [SRC-E599346ABE-L001109](../generate_index.py#L1109) | 1109 | `""` | — |
| [SRC-E599346ABE-L001110](../generate_index.py#L1110) | 1110 | `""` | — |
| [SRC-E599346ABE-L001111](../generate_index.py#L1111) | 1111 | `"def render_source_lines_markdown("` | — |
| [SRC-E599346ABE-L001112](../generate_index.py#L1112) | 1112 | `"    source_lines: list[IndexedLine],"` | — |
| [SRC-E599346ABE-L001113](../generate_index.py#L1113) | 1113 | `"    inventory: list[IndexedFile],"` | — |
| [SRC-E599346ABE-L001114](../generate_index.py#L1114) | 1114 | `"    findings: list[IndexedFinding],"` | — |
| [SRC-E599346ABE-L001115](../generate_index.py#L1115) | 1115 | `"    pages_by_file: dict[str, list[str]] \| None = None,"` | — |
| [SRC-E599346ABE-L001116](../generate_index.py#L1116) | 1116 | `"    source_pages: dict[str, str] \| None = None,"` | — |
| [SRC-E599346ABE-L001117](../generate_index.py#L1117) | 1117 | `") -> str:"` | — |
| [SRC-E599346ABE-L001118](../generate_index.py#L1118) | 1118 | `"    \"\"\"Render a compact table of contents for the sharded full source-line index.\"\"\""` | — |
| [SRC-E599346ABE-L001119](../generate_index.py#L1119) | 1119 | `"    assigned_pages = pages_by_file or {}"` | — |
| [SRC-E599346ABE-L001120](../generate_index.py#L1120) | 1120 | `"    rendered_pages = source_pages or {}"` | — |
| [SRC-E599346ABE-L001121](../generate_index.py#L1121) | 1121 | `"    files_with_lines = sum(item.line_count is not None for item in inventory)"` | — |
| [SRC-E599346ABE-L001122](../generate_index.py#L1122) | 1122 | `"    lines = ["` | — |
| [SRC-E599346ABE-L001123](../generate_index.py#L1123) | 1123 | `"        \"# SOURCE LINES INDEX — Omarai\","` | — |
| [SRC-E599346ABE-L001124](../generate_index.py#L1124) | 1124 | `"        \"\","` | — |
| [SRC-E599346ABE-L001125](../generate_index.py#L1125) | 1125 | `"        \"<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001126](../generate_index.py#L1126) | 1126 | `"        \"\","` | — |
| [SRC-E599346ABE-L001127](../generate_index.py#L1127) | 1127 | `"        \"> هذا دليل الوصول إلى فهرس الأسطر الكامل. يحتوي كل سطر في الملفات النصية المؤهلة على كود SRC- ورقم السطر ونص السطر كاملًا.\","` | — |
| [SRC-E599346ABE-L001128](../generate_index.py#L1128) | 1128 | `"        \"> قُسّم المحتوى إلى صفحات صغيرة حتى تظل كل صفحة قابلة للفتح والبحث بسرعة من الهاتف والمتصفح.\","` | — |
| [SRC-E599346ABE-L001129](../generate_index.py#L1129) | 1129 | `"        \"> ابدأ من [MASTER INDEX](MASTER_INDEX.md) للعثور حسب اسم الملف أو الدالة أو الكلاس أو وسم المراجعة.\","` | — |
| [SRC-E599346ABE-L001130](../generate_index.py#L1130) | 1130 | `"        \"> راجع [INDEX COVERAGE AUDIT](INDEX_COVERAGE_AUDIT.md) للاطلاع على نسبة التغطية وأسباب الاستبعاد.\","` | — |
| [SRC-E599346ABE-L001131](../generate_index.py#L1131) | 1131 | `"        \"\","` | — |
| [SRC-E599346ABE-L001132](../generate_index.py#L1132) | 1132 | `"        \"## ملخص التغطية\","` | — |
| [SRC-E599346ABE-L001133](../generate_index.py#L1133) | 1133 | `"        \"\","` | — |
| [SRC-E599346ABE-L001134](../generate_index.py#L1134) | 1134 | `"        f\"- الملفات في جرد المستودع: **{len(inventory)}**\","` | — |
| [SRC-E599346ABE-L001135](../generate_index.py#L1135) | 1135 | `"        f\"- الملفات النصية المفهرسة سطرًا بسطر: **{files_with_lines}**\","` | — |
| [SRC-E599346ABE-L001136](../generate_index.py#L1136) | 1136 | `"        f\"- الأسطر المفهرسة: **{len(source_lines)}**\","` | — |
| [SRC-E599346ABE-L001137](../generate_index.py#L1137) | 1137 | `"        f\"- وسوم المراجعة/الإصلاح المسجلة: **{len(findings)}**\","` | — |
| [SRC-E599346ABE-L001138](../generate_index.py#L1138) | 1138 | `"        f\"- صفحات الأسطر: **{len(rendered_pages)}**\","` | — |
| [SRC-E599346ABE-L001139](../generate_index.py#L1139) | 1139 | `"        \"\","` | — |
| [SRC-E599346ABE-L001140](../generate_index.py#L1140) | 1140 | `"        \"## صفحات الأسطر\","` | — |
| [SRC-E599346ABE-L001141](../generate_index.py#L1141) | 1141 | `"        \"\","` | — |
| [SRC-E599346ABE-L001142](../generate_index.py#L1142) | 1142 | `"        \"\| الصفحة \| عدد السجلات \| من كود \| إلى كود \|\","` | — |
| [SRC-E599346ABE-L001143](../generate_index.py#L1143) | 1143 | `"        \"\|---\|---:\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001144](../generate_index.py#L1144) | 1144 | `"    ]"` | — |
| [SRC-E599346ABE-L001145](../generate_index.py#L1145) | 1145 | `"    for page_path, page_content in rendered_pages.items():"` | — |
| [SRC-E599346ABE-L001146](../generate_index.py#L1146) | 1146 | `"        count = sum(1 for line in page_content.splitlines() if line.startswith(\"\| [SRC-\"))"` | — |
| [SRC-E599346ABE-L001147](../generate_index.py#L1147) | 1147 | `"        ids = re.findall(r\"\\bSRC-[A-F0-9]+-L\\d{6}\\b\", page_content)"` | — |
| [SRC-E599346ABE-L001148](../generate_index.py#L1148) | 1148 | `"        label = Path(page_path).stem"` | — |
| [SRC-E599346ABE-L001149](../generate_index.py#L1149) | 1149 | `"        lines.append("` | — |
| [SRC-E599346ABE-L001150](../generate_index.py#L1150) | 1150 | `"            f\"\| [{label}]({Path(page_path).relative_to('docs').as_posix()}) \| \""` | — |
| [SRC-E599346ABE-L001151](../generate_index.py#L1151) | 1151 | `"            f\"{count} \| {ids[0] if ids else '—'} \| {ids[-1] if ids else '—'} \|\""` | — |
| [SRC-E599346ABE-L001152](../generate_index.py#L1152) | 1152 | `"        )"` | — |
| [SRC-E599346ABE-L001153](../generate_index.py#L1153) | 1153 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001154](../generate_index.py#L1154) | 1154 | `"        ["` | — |
| [SRC-E599346ABE-L001155](../generate_index.py#L1155) | 1155 | `"            \"\","` | — |
| [SRC-E599346ABE-L001156](../generate_index.py#L1156) | 1156 | `"            \"## جرد الملفات والوصول حسب الاسم\","` | — |
| [SRC-E599346ABE-L001157](../generate_index.py#L1157) | 1157 | `"            \"\","` | — |
| [SRC-E599346ABE-L001158](../generate_index.py#L1158) | 1158 | `"            \"\| معرّف الملف \| التصنيف \| الملف \| الأسطر \| صفحات الفهرسة \|\","` | — |
| [SRC-E599346ABE-L001159](../generate_index.py#L1159) | 1159 | `"            \"\|---\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001160](../generate_index.py#L1160) | 1160 | `"        ]"` | — |
| [SRC-E599346ABE-L001161](../generate_index.py#L1161) | 1161 | `"    )"` | — |
| [SRC-E599346ABE-L001162](../generate_index.py#L1162) | 1162 | `"    for item in sorted(inventory, key=lambda entry: (entry.category, entry.file.casefold())):"` | — |
| [SRC-E599346ABE-L001163](../generate_index.py#L1163) | 1163 | `"        if item.line_count is None:"` | — |
| [SRC-E599346ABE-L001164](../generate_index.py#L1164) | 1164 | `"            line_count = \"بيانات وصفية فقط\""` | — |
| [SRC-E599346ABE-L001165](../generate_index.py#L1165) | 1165 | `"        else:"` | — |
| [SRC-E599346ABE-L001166](../generate_index.py#L1166) | 1166 | `"            line_count = str(item.line_count)"` | — |
| [SRC-E599346ABE-L001167](../generate_index.py#L1167) | 1167 | `"        page_links = assigned_pages.get(item.file, [])"` | — |
| [SRC-E599346ABE-L001168](../generate_index.py#L1168) | 1168 | `"        if page_links:"` | — |
| [SRC-E599346ABE-L001169](../generate_index.py#L1169) | 1169 | `"            link_text = \", \".join("` | — |
| [SRC-E599346ABE-L001170](../generate_index.py#L1170) | 1170 | `"                f\"[{Path(page_path).stem}]({Path(page_path).relative_to('docs').as_posix()})\""` | — |
| [SRC-E599346ABE-L001171](../generate_index.py#L1171) | 1171 | `"                for page_path in page_links"` | — |
| [SRC-E599346ABE-L001172](../generate_index.py#L1172) | 1172 | `"            )"` | — |
| [SRC-E599346ABE-L001173](../generate_index.py#L1173) | 1173 | `"        elif item.line_count == 0:"` | — |
| [SRC-E599346ABE-L001174](../generate_index.py#L1174) | 1174 | `"            link_text = \"ملف نصي فارغ\""` | — |
| [SRC-E599346ABE-L001175](../generate_index.py#L1175) | 1175 | `"        elif item.line_count is None:"` | — |
| [SRC-E599346ABE-L001176](../generate_index.py#L1176) | 1176 | `"            link_text = \"غير مفهرس سطرًا بسطر\""` | — |
| [SRC-E599346ABE-L001177](../generate_index.py#L1177) | 1177 | `"        else:"` | — |
| [SRC-E599346ABE-L001178](../generate_index.py#L1178) | 1178 | `"            link_text = \"لا توجد سجلات\""` | — |
| [SRC-E599346ABE-L001179](../generate_index.py#L1179) | 1179 | `"        target = _source_file_href(item.file, index_directory=\"docs\")"` | — |
| [SRC-E599346ABE-L001180](../generate_index.py#L1180) | 1180 | `"        lines.append("` | — |
| [SRC-E599346ABE-L001181](../generate_index.py#L1181) | 1181 | `"            f\"\| {item.file_id} \| {_markdown_cell(item.category)} \| \""` | — |
| [SRC-E599346ABE-L001182](../generate_index.py#L1182) | 1182 | `"            f\"[{_markdown_cell(item.file)}]({target}) \| {line_count} \| {link_text} \|\""` | — |
| [SRC-E599346ABE-L001183](../generate_index.py#L1183) | 1183 | `"        )"` | — |
| [SRC-E599346ABE-L001184](../generate_index.py#L1184) | 1184 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001185](../generate_index.py#L1185) | 1185 | `"        ["` | — |
| [SRC-E599346ABE-L001186](../generate_index.py#L1186) | 1186 | `"            \"\","` | — |
| [SRC-E599346ABE-L001187](../generate_index.py#L1187) | 1187 | `"            \"## سجل وسوم المراجعة والإصلاح\","` | — |
| [SRC-E599346ABE-L001188](../generate_index.py#L1188) | 1188 | `"            \"\","` | — |
| [SRC-E599346ABE-L001189](../generate_index.py#L1189) | 1189 | `"            \"كل كود FND- في MASTER INDEX يحدد وسمًا صريحًا ويشير إلى كود السطر في إحدى صفحات هذا الفهرس.\","` | — |
| [SRC-E599346ABE-L001190](../generate_index.py#L1190) | 1190 | `"            \"الوسوم المعروفة: TODO وFIXME وBUG وHACK وXXX وREVIEW وSECURITY وDEPRECATED.\","` | — |
| [SRC-E599346ABE-L001191](../generate_index.py#L1191) | 1191 | `"            \"\","` | — |
| [SRC-E599346ABE-L001192](../generate_index.py#L1192) | 1192 | `"            \"## الاستثناءات وحدود التغطية\","` | — |
| [SRC-E599346ABE-L001193](../generate_index.py#L1193) | 1193 | `"            \"\","` | — |
| [SRC-E599346ABE-L001194](../generate_index.py#L1194) | 1194 | `"            \"- ملفات الفهرسة المولّدة نفسها مستثناة لمنع الحلقة الذاتية.\","` | — |
| [SRC-E599346ABE-L001195](../generate_index.py#L1195) | 1195 | `"            \"- تُفهرس سطور كل ملف نصي قابل للقراءة وحجمه حتى 2 MiB؛ الملفات الثنائية أو الأكبر أو غير القابلة للقراءة تظهر في جرد الملفات فقط.\","` | — |
| [SRC-E599346ABE-L001196](../generate_index.py#L1196) | 1196 | `"            \"- الملفات الحساسة المعروفة وقواعد البيانات والبيئات المحلية ومجلدات البناء والاعتماديات مستثناة عمدًا.\","` | — |
| [SRC-E599346ABE-L001197](../generate_index.py#L1197) | 1197 | `"            \"- أكواد الأسطر مشتقة من مسار الملف ورقم السطر؛ يتغير رقم الكود عند تحرك السطر بسبب تغييرات سابقة في الملف.\","` | — |
| [SRC-E599346ABE-L001198](../generate_index.py#L1198) | 1198 | `"            \"- وسوم المراجعة ليست تشخيصًا آليًا لكل عيب منطقي؛ الفهرس يسهل العثور على الكود لكنه لا يستطيع إثبات خلوه من الأخطاء.\","` | — |
| [SRC-E599346ABE-L001199](../generate_index.py#L1199) | 1199 | `"            \"\","` | — |
| [SRC-E599346ABE-L001200](../generate_index.py#L1200) | 1200 | `"        ]"` | — |
| [SRC-E599346ABE-L001201](../generate_index.py#L1201) | 1201 | `"    )"` | — |
| [SRC-E599346ABE-L001202](../generate_index.py#L1202) | 1202 | `"    return \"\\n\".join(lines) + \"\\n\""` | — |
| [SRC-E599346ABE-L001203](../generate_index.py#L1203) | 1203 | `""` | — |
| [SRC-E599346ABE-L001204](../generate_index.py#L1204) | 1204 | `""` | — |
| [SRC-E599346ABE-L001205](../generate_index.py#L1205) | 1205 | `"def render_coverage_audit_markdown("` | — |
| [SRC-E599346ABE-L001206](../generate_index.py#L1206) | 1206 | `"    root: Path,"` | — |
| [SRC-E599346ABE-L001207](../generate_index.py#L1207) | 1207 | `"    inventory: list[IndexedFile],"` | — |
| [SRC-E599346ABE-L001208](../generate_index.py#L1208) | 1208 | `"    source_lines: list[IndexedLine],"` | — |
| [SRC-E599346ABE-L001209](../generate_index.py#L1209) | 1209 | `"    excluded_paths: list[tuple[str, str]],"` | — |
| [SRC-E599346ABE-L001210](../generate_index.py#L1210) | 1210 | `") -> str:"` | — |
| [SRC-E599346ABE-L001211](../generate_index.py#L1211) | 1211 | `"    \"\"\"Render a generated coverage ledger with exact line-index coverage and exclusions.\"\"\""` | — |
| [SRC-E599346ABE-L001212](../generate_index.py#L1212) | 1212 | `"    indexed_files = [item for item in inventory if item.line_count is not None]"` | — |
| [SRC-E599346ABE-L001213](../generate_index.py#L1213) | 1213 | `"    metadata_only = [item for item in inventory if item.line_count is None]"` | — |
| [SRC-E599346ABE-L001214](../generate_index.py#L1214) | 1214 | `"    expected_line_count = sum(item.line_count or 0 for item in indexed_files)"` | — |
| [SRC-E599346ABE-L001215](../generate_index.py#L1215) | 1215 | `"    actual_line_count = len(source_lines)"` | — |
| [SRC-E599346ABE-L001216](../generate_index.py#L1216) | 1216 | `"    coverage_ok = expected_line_count == actual_line_count"` | — |
| [SRC-E599346ABE-L001217](../generate_index.py#L1217) | 1217 | `"    lines = ["` | — |
| [SRC-E599346ABE-L001218](../generate_index.py#L1218) | 1218 | `"        \"# OMARAI INDEX COVERAGE AUDIT\","` | — |
| [SRC-E599346ABE-L001219](../generate_index.py#L1219) | 1219 | `"        \"\","` | — |
| [SRC-E599346ABE-L001220](../generate_index.py#L1220) | 1220 | `"        \"<!-- هذا الملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001221](../generate_index.py#L1221) | 1221 | `"        \"\","` | — |
| [SRC-E599346ABE-L001222](../generate_index.py#L1222) | 1222 | `"        \"> سجل أدلة تغطية الفهرس وحدوده، وليس ادعاءً باكتشاف كل عيب منطقي في البرنامج.\","` | — |
| [SRC-E599346ABE-L001223](../generate_index.py#L1223) | 1223 | `"        \"\","` | — |
| [SRC-E599346ABE-L001224](../generate_index.py#L1224) | 1224 | `"        \"## نتيجة تغطية السطور\","` | — |
| [SRC-E599346ABE-L001225](../generate_index.py#L1225) | 1225 | `"        \"\","` | — |
| [SRC-E599346ABE-L001226](../generate_index.py#L1226) | 1226 | `"        f\"- ملفات المستودع المؤهلة في الجرد: **{len(inventory)}**\","` | — |
| [SRC-E599346ABE-L001227](../generate_index.py#L1227) | 1227 | `"        f\"- الملفات المفهرسة سطرًا بسطر: **{len(indexed_files)}**\","` | — |
| [SRC-E599346ABE-L001228](../generate_index.py#L1228) | 1228 | `"        f\"- الملفات الوصفية فقط التي لا تتوفر سطورها: **{len(metadata_only)}**\","` | — |
| [SRC-E599346ABE-L001229](../generate_index.py#L1229) | 1229 | `"        f\"- السطور المتوقع فهرستها من عدادات الملفات: **{expected_line_count}**\","` | — |
| [SRC-E599346ABE-L001230](../generate_index.py#L1230) | 1230 | `"        f\"- سجلات السطور الفعلية: **{actual_line_count}**\","` | — |
| [SRC-E599346ABE-L001231](../generate_index.py#L1231) | 1231 | `"        f\"- تحقق العدد الإجمالي: **{'PASS' if coverage_ok else 'FAIL'}**\","` | — |
| [SRC-E599346ABE-L001232](../generate_index.py#L1232) | 1232 | `"        f\"- نسبة التغطية الحسابية ضمن الملفات المؤهلة القابلة للقراءة: **{(100.0 if coverage_ok and expected_line_count == actual_line_count else (actual_line_count / expected_line_count * 100 if expected_line_count else 100.0)):.2f}%**\","` | — |
| [SRC-E599346ABE-L001233](../generate_index.py#L1233) | 1233 | `"        \"\","` | — |
| [SRC-E599346ABE-L001234](../generate_index.py#L1234) | 1234 | `"        \"يتحقق المولد كذلك من أن أرقام السطور متتابعة لكل ملف ومن عدم تكرار معرّفات SRC؛ أي فشل يمنع نشر الفهرس.\","` | — |
| [SRC-E599346ABE-L001235](../generate_index.py#L1235) | 1235 | `"        \"\","` | — |
| [SRC-E599346ABE-L001236](../generate_index.py#L1236) | 1236 | `"        \"## الملفات التي لا تُفهرس سطورها\","` | — |
| [SRC-E599346ABE-L001237](../generate_index.py#L1237) | 1237 | `"        \"\","` | — |
| [SRC-E599346ABE-L001238](../generate_index.py#L1238) | 1238 | `"        \"هذه الملفات تظل ظاهرة في جرد MASTER INDEX مع سبب الاستثناء. لا يُدرج التقرير محتوياتها.\","` | — |
| [SRC-E599346ABE-L001239](../generate_index.py#L1239) | 1239 | `"        \"\","` | — |
| [SRC-E599346ABE-L001240](../generate_index.py#L1240) | 1240 | `"        \"\| معرّف الملف \| المسار \| الحجم بالبايت \| السبب \|\","` | — |
| [SRC-E599346ABE-L001241](../generate_index.py#L1241) | 1241 | `"        \"\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001242](../generate_index.py#L1242) | 1242 | `"    ]"` | — |
| [SRC-E599346ABE-L001243](../generate_index.py#L1243) | 1243 | `""` | — |
| [SRC-E599346ABE-L001244](../generate_index.py#L1244) | 1244 | `"    if metadata_only:"` | — |
| [SRC-E599346ABE-L001245](../generate_index.py#L1245) | 1245 | `"        for item in metadata_only:"` | — |
| [SRC-E599346ABE-L001246](../generate_index.py#L1246) | 1246 | `"            reason = _text_index_skip_reason(root / item.file)"` | — |
| [SRC-E599346ABE-L001247](../generate_index.py#L1247) | 1247 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001248](../generate_index.py#L1248) | 1248 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001249](../generate_index.py#L1249) | 1249 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001250](../generate_index.py#L1250) | 1250 | `"                    ("` | — |
| [SRC-E599346ABE-L001251](../generate_index.py#L1251) | 1251 | `"                        item.file_id,"` | — |
| [SRC-E599346ABE-L001252](../generate_index.py#L1252) | 1252 | `"                        _markdown_code_span(item.file),"` | — |
| [SRC-E599346ABE-L001253](../generate_index.py#L1253) | 1253 | `"                        str(item.size_bytes),"` | — |
| [SRC-E599346ABE-L001254](../generate_index.py#L1254) | 1254 | `"                        _markdown_cell(reason),"` | — |
| [SRC-E599346ABE-L001255](../generate_index.py#L1255) | 1255 | `"                    )"` | — |
| [SRC-E599346ABE-L001256](../generate_index.py#L1256) | 1256 | `"                )"` | — |
| [SRC-E599346ABE-L001257](../generate_index.py#L1257) | 1257 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001258](../generate_index.py#L1258) | 1258 | `"            )"` | — |
| [SRC-E599346ABE-L001259](../generate_index.py#L1259) | 1259 | `"    else:"` | — |
| [SRC-E599346ABE-L001260](../generate_index.py#L1260) | 1260 | `"        lines.append(\"\| — \| — \| — \| لا توجد ملفات مؤهلة بالجرد الوصفي فقط. \|\")"` | — |
| [SRC-E599346ABE-L001261](../generate_index.py#L1261) | 1261 | `""` | — |
| [SRC-E599346ABE-L001262](../generate_index.py#L1262) | 1262 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001263](../generate_index.py#L1263) | 1263 | `"        ["` | — |
| [SRC-E599346ABE-L001264](../generate_index.py#L1264) | 1264 | `"            \"\","` | — |
| [SRC-E599346ABE-L001265](../generate_index.py#L1265) | 1265 | `"            \"## المسارات المستبعدة عمدًا\","` | — |
| [SRC-E599346ABE-L001266](../generate_index.py#L1266) | 1266 | `"            \"\","` | — |
| [SRC-E599346ABE-L001267](../generate_index.py#L1267) | 1267 | `"            \"يحتوي هذا السجل أسماء المسارات وأسباب الاستثناء فقط، ولا يقرأ محتوى الأسرار أو قواعد البيانات أو المجلدات المستبعدة.\","` | — |
| [SRC-E599346ABE-L001268](../generate_index.py#L1268) | 1268 | `"            \"\","` | — |
| [SRC-E599346ABE-L001269](../generate_index.py#L1269) | 1269 | `"            \"\| المسار المستبعد \| السبب \|\","` | — |
| [SRC-E599346ABE-L001270](../generate_index.py#L1270) | 1270 | `"            \"\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001271](../generate_index.py#L1271) | 1271 | `"        ]"` | — |
| [SRC-E599346ABE-L001272](../generate_index.py#L1272) | 1272 | `"    )"` | — |
| [SRC-E599346ABE-L001273](../generate_index.py#L1273) | 1273 | `"    if excluded_paths:"` | — |
| [SRC-E599346ABE-L001274](../generate_index.py#L1274) | 1274 | `"        for excluded_path, reason in excluded_paths:"` | — |
| [SRC-E599346ABE-L001275](../generate_index.py#L1275) | 1275 | `"            lines.append(f\"\| {_markdown_code_span(excluded_path)} \| {_markdown_cell(reason)} \|\")"` | — |
| [SRC-E599346ABE-L001276](../generate_index.py#L1276) | 1276 | `"    else:"` | — |
| [SRC-E599346ABE-L001277](../generate_index.py#L1277) | 1277 | `"        lines.append(\"\| — \| لا توجد مسارات مستبعدة مكتشفة. \|\")"` | — |
| [SRC-E599346ABE-L001278](../generate_index.py#L1278) | 1278 | `""` | — |
| [SRC-E599346ABE-L001279](../generate_index.py#L1279) | 1279 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001280](../generate_index.py#L1280) | 1280 | `"        ["` | — |
| [SRC-E599346ABE-L001281](../generate_index.py#L1281) | 1281 | `"            \"\","` | — |
| [SRC-E599346ABE-L001282](../generate_index.py#L1282) | 1282 | `"            \"## ما تعنيه النتيجة وما لا تعنيه\","` | — |
| [SRC-E599346ABE-L001283](../generate_index.py#L1283) | 1283 | `"            \"\","` | — |
| [SRC-E599346ABE-L001284](../generate_index.py#L1284) | 1284 | `"            \"- التغطية بنسبة 100% تعني أن كل سطر منطقي في كل ملف نصي مؤهل وقابل للقراءة ضمن حد الحجم له سجل SRC فريد ورقم سطر مطابق.\","` | — |
| [SRC-E599346ABE-L001285](../generate_index.py#L1285) | 1285 | `"            \"- لا تعني أن كل مسار مستبعد أو كل ملف ثنائي/كبير مفهرس سطرًا بسطر؛ أسباب الاستبعاد مسجلة أعلاه.\","` | — |
| [SRC-E599346ABE-L001286](../generate_index.py#L1286) | 1286 | `"            \"- لا تعني اكتشاف كل عيب برمجي أو أمني أو منطقي. العيوب المعروفة التي يوسمها المطور صراحة تظهر في سجل FND داخل MASTER INDEX.\","` | — |
| [SRC-E599346ABE-L001287](../generate_index.py#L1287) | 1287 | `"            \"- الرموز غير Python مستخرجة بقواعد ساكنة تقريبية؛ استخدم فهرس السطور للوصول إلى النص الأصلي والتحقق يدويًا.\","` | — |
| [SRC-E599346ABE-L001288](../generate_index.py#L1288) | 1288 | `"            \"- المولد لا يعدّل كود التطبيق ولا يدمج الفروع؛ وظيفته بناء الأدلة والفهرس والتحقق من اتساقهما.\","` | — |
| [SRC-E599346ABE-L001289](../generate_index.py#L1289) | 1289 | `"            \"\","` | — |
| [SRC-E599346ABE-L001290](../generate_index.py#L1290) | 1290 | `"            \"[افتح MASTER INDEX](MASTER_INDEX.md) \| [افتح SOURCE LINES INDEX](SOURCE_LINES_INDEX.md)\","` | — |
| [SRC-E599346ABE-L001291](../generate_index.py#L1291) | 1291 | `"            \"\","` | — |
| [SRC-E599346ABE-L001292](../generate_index.py#L1292) | 1292 | `"        ]"` | — |
| [SRC-E599346ABE-L001293](../generate_index.py#L1293) | 1293 | `"    )"` | — |
| [SRC-E599346ABE-L001294](../generate_index.py#L1294) | 1294 | `"    return \"\\n\".join(lines)"` | — |
| [SRC-E599346ABE-L001295](../generate_index.py#L1295) | 1295 | `""` | — |
| [SRC-E599346ABE-L001296](../generate_index.py#L1296) | 1296 | `""` | — |
| [SRC-E599346ABE-L001297](../generate_index.py#L1297) | 1297 | `"def render_markdown("` | — |
| [SRC-E599346ABE-L001298](../generate_index.py#L1298) | 1298 | `"    symbols: list[IndexedSymbol],"` | — |
| [SRC-E599346ABE-L001299](../generate_index.py#L1299) | 1299 | `"    files_scanned: int,"` | — |
| [SRC-E599346ABE-L001300](../generate_index.py#L1300) | 1300 | `"    inventory: list[IndexedFile] \| None = None,"` | — |
| [SRC-E599346ABE-L001301](../generate_index.py#L1301) | 1301 | `"    static_symbols: list[IndexedMarker] \| None = None,"` | — |
| [SRC-E599346ABE-L001302](../generate_index.py#L1302) | 1302 | `"    source_lines: list[IndexedLine] \| None = None,"` | — |
| [SRC-E599346ABE-L001303](../generate_index.py#L1303) | 1303 | `"    findings: list[IndexedFinding] \| None = None,"` | — |
| [SRC-E599346ABE-L001304](../generate_index.py#L1304) | 1304 | `") -> str:"` | — |
| [SRC-E599346ABE-L001305](../generate_index.py#L1305) | 1305 | `"    \"\"\"Render the repository file, symbol, explicit-review-marker, and line-index overview.\"\"\""` | FND-REVIEW-E599346ABE-L001305 |
| [SRC-E599346ABE-L001306](../generate_index.py#L1306) | 1306 | `"    file_inventory = inventory or []"` | — |
| [SRC-E599346ABE-L001307](../generate_index.py#L1307) | 1307 | `"    marker_inventory = static_symbols or []"` | — |
| [SRC-E599346ABE-L001308](../generate_index.py#L1308) | 1308 | `"    line_inventory = source_lines or []"` | — |
| [SRC-E599346ABE-L001309](../generate_index.py#L1309) | 1309 | `"    finding_inventory = findings or []"` | — |
| [SRC-E599346ABE-L001310](../generate_index.py#L1310) | 1310 | `"    documented_count = sum(symbol.documented is True for symbol in symbols)"` | — |
| [SRC-E599346ABE-L001311](../generate_index.py#L1311) | 1311 | `"    missing_count = sum(symbol.documented is False for symbol in symbols)"` | — |
| [SRC-E599346ABE-L001312](../generate_index.py#L1312) | 1312 | `"    not_applicable_count = sum(symbol.documented is None for symbol in symbols)"` | — |
| [SRC-E599346ABE-L001313](../generate_index.py#L1313) | 1313 | `"    lines = ["` | — |
| [SRC-E599346ABE-L001314](../generate_index.py#L1314) | 1314 | `"        \"# MASTER INDEX — Omarai\","` | — |
| [SRC-E599346ABE-L001315](../generate_index.py#L1315) | 1315 | `"        \"\","` | — |
| [SRC-E599346ABE-L001316](../generate_index.py#L1316) | 1316 | `"        \"<!-- هذا الملف مُولَّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001317](../generate_index.py#L1317) | 1317 | `"        \"\","` | — |
| [SRC-E599346ABE-L001318](../generate_index.py#L1318) | 1318 | `"        \"> MASTER INDEX يجمع جرد الملفات والتعريفات المسماة ووسوم المراجعة؛ SOURCE LINES INDEX يحتوي الأسطر الكاملة\","` | — |
| [SRC-E599346ABE-L001319](../generate_index.py#L1319) | 1319 | `"        \"> لكل ملف نصي مؤهل قابل للقراءة، مع معرّف سطر ورقم السطر الأصلي.\","` | — |
| [SRC-E599346ABE-L001320](../generate_index.py#L1320) | 1320 | `"        \"> استخراج الرموز غير Python تقريبي؛ أما فهرسة الأسطر فمخصصة للوصول إلى النص الموجود وليست حكمًا على صحته.\","` | — |
| [SRC-E599346ABE-L001321](../generate_index.py#L1321) | 1321 | `"        \"\","` | — |
| [SRC-E599346ABE-L001322](../generate_index.py#L1322) | 1322 | `"        \"## ملخص الفهرسة\","` | — |
| [SRC-E599346ABE-L001323](../generate_index.py#L1323) | 1323 | `"        \"\","` | — |
| [SRC-E599346ABE-L001324](../generate_index.py#L1324) | 1324 | `"        f\"- ملفات المستودع في الجرد: **{len(file_inventory)}**\","` | — |
| [SRC-E599346ABE-L001325](../generate_index.py#L1325) | 1325 | `"        f\"- ملفات Python المحللة: **{files_scanned}**\","` | — |
| [SRC-E599346ABE-L001326](../generate_index.py#L1326) | 1326 | `"        f\"- تعريفات Python المفهرسة: **{len(symbols)}**\","` | — |
| [SRC-E599346ABE-L001327](../generate_index.py#L1327) | 1327 | `"        f\"- تعريفات Python موثقة بوجود Docstring: **{documented_count}**\","` | — |
| [SRC-E599346ABE-L001328](../generate_index.py#L1328) | 1328 | `"        f\"- تعريفات Python بلا Docstring: **{missing_count}**\","` | — |
| [SRC-E599346ABE-L001329](../generate_index.py#L1329) | 1329 | `"        f\"- تعريفات لا ينطبق عليها Docstring: **{not_applicable_count}**\","` | — |
| [SRC-E599346ABE-L001330](../generate_index.py#L1330) | 1330 | `"        f\"- الرموز الساكنة الإضافية: **{len(marker_inventory)}**\","` | — |
| [SRC-E599346ABE-L001331](../generate_index.py#L1331) | 1331 | `"        f\"- الأسطر النصية المفهرسة حرفيًا: **{len(line_inventory)}**\","` | — |
| [SRC-E599346ABE-L001332](../generate_index.py#L1332) | 1332 | `"        f\"- وسوم المراجعة/الإصلاح المسجلة: **{len(finding_inventory)}**\","` | — |
| [SRC-E599346ABE-L001333](../generate_index.py#L1333) | 1333 | `"        \"\","` | — |
| [SRC-E599346ABE-L001334](../generate_index.py#L1334) | 1334 | `"        \"- فهرس الأسطر الكامل: [SOURCE LINES INDEX](SOURCE_LINES_INDEX.md)\","` | — |
| [SRC-E599346ABE-L001335](../generate_index.py#L1335) | 1335 | `"        \"- تدقيق التغطية والاستثناءات: [INDEX COVERAGE AUDIT](INDEX_COVERAGE_AUDIT.md)\","` | — |
| [SRC-E599346ABE-L001336](../generate_index.py#L1336) | 1336 | `"        \"- كل سجل سطر يحمل معرّفًا من الشكل SRC-<FILEHASH>-L000001.\","` | — |
| [SRC-E599346ABE-L001337](../generate_index.py#L1337) | 1337 | `"        \"\","` | — |
| [SRC-E599346ABE-L001338](../generate_index.py#L1338) | 1338 | `"        \"## جرد ملفات المستودع\","` | — |
| [SRC-E599346ABE-L001339](../generate_index.py#L1339) | 1339 | `"        \"\","` | — |
| [SRC-E599346ABE-L001340](../generate_index.py#L1340) | 1340 | `"        (\"يشمل الملفات المؤهلة من الشفرة والواجهة والاختبارات والوثائق والإعدادات وCI. \""` | — |
| [SRC-E599346ABE-L001341](../generate_index.py#L1341) | 1341 | `"        \"يُستثنى ملف الفهرس المولّد نفسه لتجنب الحلقة الذاتية، كما تُستثنى المجلدات المولّدة \""` | — |
| [SRC-E599346ABE-L001342](../generate_index.py#L1342) | 1342 | `"        \"والبيئات والملفات المحلية الحساسة وقواعد البيانات والمفاتيح المعروفة.\"),"` | — |
| [SRC-E599346ABE-L001343](../generate_index.py#L1343) | 1343 | `"        \"\","` | — |
| [SRC-E599346ABE-L001344](../generate_index.py#L1344) | 1344 | `"        \"\| معرّف الملف \| التصنيف \| الملف \| النوع \| الحجم (بايت) \| عدد الأسطر \| نطاق الفهرسة \|\","` | — |
| [SRC-E599346ABE-L001345](../generate_index.py#L1345) | 1345 | `"        \"\|---\|---\|---\|---\|---:\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001346](../generate_index.py#L1346) | 1346 | `"    ]"` | — |
| [SRC-E599346ABE-L001347](../generate_index.py#L1347) | 1347 | `""` | — |
| [SRC-E599346ABE-L001348](../generate_index.py#L1348) | 1348 | `"    if file_inventory:"` | — |
| [SRC-E599346ABE-L001349](../generate_index.py#L1349) | 1349 | `"        for item in file_inventory:"` | — |
| [SRC-E599346ABE-L001350](../generate_index.py#L1350) | 1350 | `"            line_count = str(item.line_count) if item.line_count is not None else \"غير متاح\""` | — |
| [SRC-E599346ABE-L001351](../generate_index.py#L1351) | 1351 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001352](../generate_index.py#L1352) | 1352 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001353](../generate_index.py#L1353) | 1353 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001354](../generate_index.py#L1354) | 1354 | `"                    ("` | — |
| [SRC-E599346ABE-L001355](../generate_index.py#L1355) | 1355 | `"                        item.file_id,"` | — |
| [SRC-E599346ABE-L001356](../generate_index.py#L1356) | 1356 | `"                        _markdown_cell(item.category),"` | — |
| [SRC-E599346ABE-L001357](../generate_index.py#L1357) | 1357 | `"                        f\"[{_markdown_cell(item.file)}]({_source_file_href(item.file)})\","` | — |
| [SRC-E599346ABE-L001358](../generate_index.py#L1358) | 1358 | `"                        _markdown_cell(item.file_type),"` | — |
| [SRC-E599346ABE-L001359](../generate_index.py#L1359) | 1359 | `"                        str(item.size_bytes),"` | — |
| [SRC-E599346ABE-L001360](../generate_index.py#L1360) | 1360 | `"                        line_count,"` | — |
| [SRC-E599346ABE-L001361](../generate_index.py#L1361) | 1361 | `"                        _markdown_cell(item.indexing_scope),"` | — |
| [SRC-E599346ABE-L001362](../generate_index.py#L1362) | 1362 | `"                    )"` | — |
| [SRC-E599346ABE-L001363](../generate_index.py#L1363) | 1363 | `"                )"` | — |
| [SRC-E599346ABE-L001364](../generate_index.py#L1364) | 1364 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001365](../generate_index.py#L1365) | 1365 | `"            )"` | — |
| [SRC-E599346ABE-L001366](../generate_index.py#L1366) | 1366 | `"    else:"` | — |
| [SRC-E599346ABE-L001367](../generate_index.py#L1367) | 1367 | `"        lines.append(\"\| — \| — \| — \| — \| — \| — \| لم يُمرر جرد ملفات إلى المولّد. \|\")"` | — |
| [SRC-E599346ABE-L001368](../generate_index.py#L1368) | 1368 | `""` | — |
| [SRC-E599346ABE-L001369](../generate_index.py#L1369) | 1369 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001370](../generate_index.py#L1370) | 1370 | `"        ["` | — |
| [SRC-E599346ABE-L001371](../generate_index.py#L1371) | 1371 | `"            \"\","` | — |
| [SRC-E599346ABE-L001372](../generate_index.py#L1372) | 1372 | `"            \"## تعريفات Python من AST\","` | — |
| [SRC-E599346ABE-L001373](../generate_index.py#L1373) | 1373 | `"            \"\","` | — |
| [SRC-E599346ABE-L001374](../generate_index.py#L1374) | 1374 | `"            (\"> تُحسب حالة Docstring للدوال والكلاسات فقط. المتغيرات والثوابت لا تُصنّف \""` | — |
| [SRC-E599346ABE-L001375](../generate_index.py#L1375) | 1375 | `"            \"على أنها موثقة أو ناقصة Docstring.\"),"` | — |
| [SRC-E599346ABE-L001376](../generate_index.py#L1376) | 1376 | `"            \"\","` | — |
| [SRC-E599346ABE-L001377](../generate_index.py#L1377) | 1377 | `"            \"\| الملف \| النوع \| الاسم المؤهل \| الوصف \| حالة Docstring \| السطر \| كود السطر للوصول المباشر \|\","` | — |
| [SRC-E599346ABE-L001378](../generate_index.py#L1378) | 1378 | `"            \"\|---\|---\|---\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001379](../generate_index.py#L1379) | 1379 | `"        ]"` | — |
| [SRC-E599346ABE-L001380](../generate_index.py#L1380) | 1380 | `"    )"` | — |
| [SRC-E599346ABE-L001381](../generate_index.py#L1381) | 1381 | `""` | — |
| [SRC-E599346ABE-L001382](../generate_index.py#L1382) | 1382 | `"    if not symbols:"` | — |
| [SRC-E599346ABE-L001383](../generate_index.py#L1383) | 1383 | `"        lines.append(\"\| — \| — \| — \| لا توجد تعريفات Python في الملفات المؤهلة. \| — \| — \| — \|\")"` | — |
| [SRC-E599346ABE-L001384](../generate_index.py#L1384) | 1384 | `"    else:"` | — |
| [SRC-E599346ABE-L001385](../generate_index.py#L1385) | 1385 | `"        for symbol in symbols:"` | — |
| [SRC-E599346ABE-L001386](../generate_index.py#L1386) | 1386 | `"            if symbol.documented is True:"` | — |
| [SRC-E599346ABE-L001387](../generate_index.py#L1387) | 1387 | `"                status = \"موثق\""` | — |
| [SRC-E599346ABE-L001388](../generate_index.py#L1388) | 1388 | `"            elif symbol.documented is False:"` | — |
| [SRC-E599346ABE-L001389](../generate_index.py#L1389) | 1389 | `"                status = \"ناقص\""` | — |
| [SRC-E599346ABE-L001390](../generate_index.py#L1390) | 1390 | `"            else:"` | — |
| [SRC-E599346ABE-L001391](../generate_index.py#L1391) | 1391 | `"                status = \"لا ينطبق\""` | — |
| [SRC-E599346ABE-L001392](../generate_index.py#L1392) | 1392 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001393](../generate_index.py#L1393) | 1393 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001394](../generate_index.py#L1394) | 1394 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001395](../generate_index.py#L1395) | 1395 | `"                    ("` | — |
| [SRC-E599346ABE-L001396](../generate_index.py#L1396) | 1396 | `"                        f\"[{_markdown_cell(symbol.file)}]({_source_file_href(symbol.file, symbol.line)})\","` | — |
| [SRC-E599346ABE-L001397](../generate_index.py#L1397) | 1397 | `"                        _markdown_cell(symbol.kind),"` | — |
| [SRC-E599346ABE-L001398](../generate_index.py#L1398) | 1398 | `"                        _markdown_cell(symbol.name),"` | — |
| [SRC-E599346ABE-L001399](../generate_index.py#L1399) | 1399 | `"                        _markdown_cell(symbol.description),"` | — |
| [SRC-E599346ABE-L001400](../generate_index.py#L1400) | 1400 | `"                        status,"` | — |
| [SRC-E599346ABE-L001401](../generate_index.py#L1401) | 1401 | `"                        str(symbol.line),"` | — |
| [SRC-E599346ABE-L001402](../generate_index.py#L1402) | 1402 | `"                        f\"[{_source_line_id(symbol.file, symbol.line)}]({_source_file_href(symbol.file, symbol.line)})\","` | — |
| [SRC-E599346ABE-L001403](../generate_index.py#L1403) | 1403 | `"                    )"` | — |
| [SRC-E599346ABE-L001404](../generate_index.py#L1404) | 1404 | `"                )"` | — |
| [SRC-E599346ABE-L001405](../generate_index.py#L1405) | 1405 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001406](../generate_index.py#L1406) | 1406 | `"            )"` | — |
| [SRC-E599346ABE-L001407](../generate_index.py#L1407) | 1407 | `""` | — |
| [SRC-E599346ABE-L001408](../generate_index.py#L1408) | 1408 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001409](../generate_index.py#L1409) | 1409 | `"        ["` | — |
| [SRC-E599346ABE-L001410](../generate_index.py#L1410) | 1410 | `"            \"\","` | — |
| [SRC-E599346ABE-L001411](../generate_index.py#L1411) | 1411 | `"            \"## الرموز الساكنة الإضافية\","` | — |
| [SRC-E599346ABE-L001412](../generate_index.py#L1412) | 1412 | `"            \"\","` | — |
| [SRC-E599346ABE-L001413](../generate_index.py#L1413) | 1413 | `"            (\"هذا القسم للمساعدة في الوصول إلى الواجهة والإعدادات والوثائق؛ \""` | — |
| [SRC-E599346ABE-L001414](../generate_index.py#L1414) | 1414 | `"            \"استخراج الرموز غير المحللة بـAST استدلالي وقد لا يساوي تحليلًا كاملًا للغة.\"),"` | — |
| [SRC-E599346ABE-L001415](../generate_index.py#L1415) | 1415 | `"            \"\","` | — |
| [SRC-E599346ABE-L001416](../generate_index.py#L1416) | 1416 | `"            \"\| الملف \| نوع الرمز \| الاسم/القيمة \| السطر \| كود السطر للوصول المباشر \|\","` | — |
| [SRC-E599346ABE-L001417](../generate_index.py#L1417) | 1417 | `"            \"\|---\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001418](../generate_index.py#L1418) | 1418 | `"        ]"` | — |
| [SRC-E599346ABE-L001419](../generate_index.py#L1419) | 1419 | `"    )"` | — |
| [SRC-E599346ABE-L001420](../generate_index.py#L1420) | 1420 | `"    if marker_inventory:"` | — |
| [SRC-E599346ABE-L001421](../generate_index.py#L1421) | 1421 | `"        for marker in marker_inventory:"` | — |
| [SRC-E599346ABE-L001422](../generate_index.py#L1422) | 1422 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001423](../generate_index.py#L1423) | 1423 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001424](../generate_index.py#L1424) | 1424 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001425](../generate_index.py#L1425) | 1425 | `"                    ("` | — |
| [SRC-E599346ABE-L001426](../generate_index.py#L1426) | 1426 | `"                        f\"[{_markdown_cell(marker.file)}]({_source_file_href(marker.file, marker.line)})\","` | — |
| [SRC-E599346ABE-L001427](../generate_index.py#L1427) | 1427 | `"                        _markdown_cell(marker.kind),"` | — |
| [SRC-E599346ABE-L001428](../generate_index.py#L1428) | 1428 | `"                        _markdown_cell(marker.name),"` | — |
| [SRC-E599346ABE-L001429](../generate_index.py#L1429) | 1429 | `"                        str(marker.line),"` | — |
| [SRC-E599346ABE-L001430](../generate_index.py#L1430) | 1430 | `"                        f\"[{_source_line_id(marker.file, marker.line)}]({_source_file_href(marker.file, marker.line)})\","` | — |
| [SRC-E599346ABE-L001431](../generate_index.py#L1431) | 1431 | `"                    )"` | — |
| [SRC-E599346ABE-L001432](../generate_index.py#L1432) | 1432 | `"                )"` | — |
| [SRC-E599346ABE-L001433](../generate_index.py#L1433) | 1433 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001434](../generate_index.py#L1434) | 1434 | `"            )"` | — |
| [SRC-E599346ABE-L001435](../generate_index.py#L1435) | 1435 | `"    else:"` | — |
| [SRC-E599346ABE-L001436](../generate_index.py#L1436) | 1436 | `"        lines.append(\"\| — \| — \| — \| لم تُكتشف رموز ساكنة إضافية. \| — \|\")"` | — |
| [SRC-E599346ABE-L001437](../generate_index.py#L1437) | 1437 | `""` | — |
| [SRC-E599346ABE-L001438](../generate_index.py#L1438) | 1438 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001439](../generate_index.py#L1439) | 1439 | `"        ["` | — |
| [SRC-E599346ABE-L001440](../generate_index.py#L1440) | 1440 | `"            \"\","` | — |
| [SRC-E599346ABE-L001441](../generate_index.py#L1441) | 1441 | `"            \"## سجل وسوم المراجعة والإصلاح\","` | — |
| [SRC-E599346ABE-L001442](../generate_index.py#L1442) | 1442 | `"            \"\","` | — |
| [SRC-E599346ABE-L001443](../generate_index.py#L1443) | 1443 | `"            \"هذه قائمة بالوسوم الصريحة التي تستدعي المتابعة. وجود الوسم ليس إثباتًا آليًا أن السطر معيب؛ افتح الملف عند رقم السطر وراجع السياق.\","` | — |
| [SRC-E599346ABE-L001444](../generate_index.py#L1444) | 1444 | `"            \"\","` | — |
| [SRC-E599346ABE-L001445](../generate_index.py#L1445) | 1445 | `"            \"\| كود الهفوة/الوسم \| النوع \| الملف \| السطر \| وصف الوسم \| كود السطر \| نص السطر \|\","` | — |
| [SRC-E599346ABE-L001446](../generate_index.py#L1446) | 1446 | `"            \"\|---\|---\|---\|---:\|---\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001447](../generate_index.py#L1447) | 1447 | `"        ]"` | — |
| [SRC-E599346ABE-L001448](../generate_index.py#L1448) | 1448 | `"    )"` | — |
| [SRC-E599346ABE-L001449](../generate_index.py#L1449) | 1449 | `"    if finding_inventory:"` | — |
| [SRC-E599346ABE-L001450](../generate_index.py#L1450) | 1450 | `"        line_map = {source_line.line_id: source_line for source_line in line_inventory}"` | — |
| [SRC-E599346ABE-L001451](../generate_index.py#L1451) | 1451 | `"        for finding in finding_inventory:"` | — |
| [SRC-E599346ABE-L001452](../generate_index.py#L1452) | 1452 | `"            source_line = line_map.get(finding.line_id)"` | — |
| [SRC-E599346ABE-L001453](../generate_index.py#L1453) | 1453 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001454](../generate_index.py#L1454) | 1454 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001455](../generate_index.py#L1455) | 1455 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001456](../generate_index.py#L1456) | 1456 | `"                    ("` | — |
| [SRC-E599346ABE-L001457](../generate_index.py#L1457) | 1457 | `"                        finding.finding_id,"` | — |
| [SRC-E599346ABE-L001458](../generate_index.py#L1458) | 1458 | `"                        finding.marker,"` | — |
| [SRC-E599346ABE-L001459](../generate_index.py#L1459) | 1459 | `"                        f\"[{_markdown_cell(finding.file)}]({_source_file_href(finding.file, source_line.line if source_line else 1)})\","` | — |
| [SRC-E599346ABE-L001460](../generate_index.py#L1460) | 1460 | `"                        str(source_line.line if source_line else \"غير متاح\"),"` | — |
| [SRC-E599346ABE-L001461](../generate_index.py#L1461) | 1461 | `"                        _markdown_cell(finding.description),"` | — |
| [SRC-E599346ABE-L001462](../generate_index.py#L1462) | 1462 | `"                        f\"[{finding.line_id}]({_source_file_href(finding.file, source_line.line if source_line else 1)})\","` | — |
| [SRC-E599346ABE-L001463](../generate_index.py#L1463) | 1463 | `"                        _markdown_code_span(json.dumps(source_line.content, ensure_ascii=False).replace(\"\|\", r\"\\\|\")) if source_line else \"غير متاح\","` | — |
| [SRC-E599346ABE-L001464](../generate_index.py#L1464) | 1464 | `"                    )"` | — |
| [SRC-E599346ABE-L001465](../generate_index.py#L1465) | 1465 | `"                )"` | — |
| [SRC-E599346ABE-L001466](../generate_index.py#L1466) | 1466 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001467](../generate_index.py#L1467) | 1467 | `"            )"` | — |
| [SRC-E599346ABE-L001468](../generate_index.py#L1468) | 1468 | `"    else:"` | — |
| [SRC-E599346ABE-L001469](../generate_index.py#L1469) | 1469 | `"        lines.append(\"\| — \| — \| — \| — \| لم تُكتشف وسوم صريحة من الأنواع المعروفة. \| — \| — \|\")"` | — |
| [SRC-E599346ABE-L001470](../generate_index.py#L1470) | 1470 | `""` | — |
| [SRC-E599346ABE-L001471](../generate_index.py#L1471) | 1471 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001472](../generate_index.py#L1472) | 1472 | `"        ["` | — |
| [SRC-E599346ABE-L001473](../generate_index.py#L1473) | 1473 | `"            \"\","` | — |
| [SRC-E599346ABE-L001474](../generate_index.py#L1474) | 1474 | `"            \"---\","` | — |
| [SRC-E599346ABE-L001475](../generate_index.py#L1475) | 1475 | `"            \"\","` | — |
| [SRC-E599346ABE-L001476](../generate_index.py#L1476) | 1476 | `"            \"## حدود الفهرسة\","` | — |
| [SRC-E599346ABE-L001477](../generate_index.py#L1477) | 1477 | `"            \"\","` | — |
| [SRC-E599346ABE-L001478](../generate_index.py#L1478) | 1478 | `"            \"- كل الأسطر المنطقية للملفات النصية المؤهلة القابلة للقراءة مفهرسة في SOURCE LINES INDEX، لا في هذا الجدول المختصر.\","` | — |
| [SRC-E599346ABE-L001479](../generate_index.py#L1479) | 1479 | `"            \"- الملفات الأكبر من 2 MiB أو غير القابلة للقراءة أو الثنائية تبقى ضمن الجرد الوصفي، دون فهرسة سطورها.\","` | — |
| [SRC-E599346ABE-L001480](../generate_index.py#L1480) | 1480 | `"            \"- لا تُفحص محتويات البيئة الافتراضية والاعتماديات والمجلدات المولدة.\","` | — |
| [SRC-E599346ABE-L001481](../generate_index.py#L1481) | 1481 | `"            \"- لا تُقرأ ملفات البيئة المحلية وقواعد البيانات والمفاتيح المعروفة.\","` | — |
| [SRC-E599346ABE-L001482](../generate_index.py#L1482) | 1482 | `"            \"- تحليل Python يرفض إنشاء فهرس جزئي عند وجود خطأ نحوي في أي ملف Python مؤهل.\","` | — |
| [SRC-E599346ABE-L001483](../generate_index.py#L1483) | 1483 | `"            (\"- يُحدّث هذا الفهرس آليًا عبر GitHub Actions عند دفع تغيير إلى main؛ \""` | — |
| [SRC-E599346ABE-L001484](../generate_index.py#L1484) | 1484 | `"            \"وتظل تغييرات المصدر قيد المراجعة حتى تُدمج وفق سياسة المستودع.\"),"` | — |
| [SRC-E599346ABE-L001485](../generate_index.py#L1485) | 1485 | `"            \"\","` | — |
| [SRC-E599346ABE-L001486](../generate_index.py#L1486) | 1486 | `"        ]"` | — |
| [SRC-E599346ABE-L001487](../generate_index.py#L1487) | 1487 | `"    )"` | — |
| [SRC-E599346ABE-L001488](../generate_index.py#L1488) | 1488 | `"    return \"\\n\".join(lines)"` | — |
| [SRC-E599346ABE-L001489](../generate_index.py#L1489) | 1489 | `""` | — |
| [SRC-E599346ABE-L001490](../generate_index.py#L1490) | 1490 | `""` | — |
| [SRC-E599346ABE-L001491](../generate_index.py#L1491) | 1491 | `"def write_if_changed(output_path: Path, content: str) -> bool:"` | — |
| [SRC-E599346ABE-L001492](../generate_index.py#L1492) | 1492 | `"    \"\"\"Write atomically only when the generated index differs from the existing file.\"\"\""` | — |
| [SRC-E599346ABE-L001493](../generate_index.py#L1493) | 1493 | `"    output_path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-E599346ABE-L001494](../generate_index.py#L1494) | 1494 | `"    try:"` | — |
| [SRC-E599346ABE-L001495](../generate_index.py#L1495) | 1495 | `"        if output_path.read_text(encoding=\"utf-8\") == content:"` | — |
| [SRC-E599346ABE-L001496](../generate_index.py#L1496) | 1496 | `"            return False"` | — |
| [SRC-E599346ABE-L001497](../generate_index.py#L1497) | 1497 | `"    except FileNotFoundError:"` | — |
| [SRC-E599346ABE-L001498](../generate_index.py#L1498) | 1498 | `"        pass"` | — |
| [SRC-E599346ABE-L001499](../generate_index.py#L1499) | 1499 | `""` | — |
| [SRC-E599346ABE-L001500](../generate_index.py#L1500) | 1500 | `"    temporary_path: Path \| None = None"` | — |
| [SRC-E599346ABE-L001501](../generate_index.py#L1501) | 1501 | `"    try:"` | — |
| [SRC-E599346ABE-L001502](../generate_index.py#L1502) | 1502 | `"        with tempfile.NamedTemporaryFile("` | — |
| [SRC-E599346ABE-L001503](../generate_index.py#L1503) | 1503 | `"            mode=\"w\","` | — |
| [SRC-E599346ABE-L001504](../generate_index.py#L1504) | 1504 | `"            encoding=\"utf-8\","` | — |
| [SRC-E599346ABE-L001505](../generate_index.py#L1505) | 1505 | `"            newline=\"\\n\","` | — |
| [SRC-E599346ABE-L001506](../generate_index.py#L1506) | 1506 | `"            dir=output_path.parent,"` | — |
| [SRC-E599346ABE-L001507](../generate_index.py#L1507) | 1507 | `"            prefix=f\".{output_path.name}.\","` | — |
| [SRC-E599346ABE-L001508](../generate_index.py#L1508) | 1508 | `"            suffix=\".tmp\","` | — |
| [SRC-E599346ABE-L001509](../generate_index.py#L1509) | 1509 | `"            delete=False,"` | — |
| [SRC-E599346ABE-L001510](../generate_index.py#L1510) | 1510 | `"        ) as temporary_file:"` | — |
| [SRC-E599346ABE-L001511](../generate_index.py#L1511) | 1511 | `"            temporary_file.write(content)"` | — |
| [SRC-E599346ABE-L001512](../generate_index.py#L1512) | 1512 | `"            temporary_path = Path(temporary_file.name)"` | — |
| [SRC-E599346ABE-L001513](../generate_index.py#L1513) | 1513 | `"        temporary_path.replace(output_path)"` | — |
| [SRC-E599346ABE-L001514](../generate_index.py#L1514) | 1514 | `"    finally:"` | — |
| [SRC-E599346ABE-L001515](../generate_index.py#L1515) | 1515 | `"        if temporary_path is not None and temporary_path.exists():"` | — |
| [SRC-E599346ABE-L001516](../generate_index.py#L1516) | 1516 | `"            temporary_path.unlink()"` | — |
| [SRC-E599346ABE-L001517](../generate_index.py#L1517) | 1517 | `"    return True"` | — |
| [SRC-E599346ABE-L001518](../generate_index.py#L1518) | 1518 | `""` | — |
| [SRC-E599346ABE-L001519](../generate_index.py#L1519) | 1519 | `""` | — |
| [SRC-E599346ABE-L001520](../generate_index.py#L1520) | 1520 | `"def _generate("` | — |
| [SRC-E599346ABE-L001521](../generate_index.py#L1521) | 1521 | `"    root: Path,"` | — |
| [SRC-E599346ABE-L001522](../generate_index.py#L1522) | 1522 | `") -> tuple[str, str, str, dict[str, str], int, int, int, int, int, int, int]:"` | — |
| [SRC-E599346ABE-L001523](../generate_index.py#L1523) | 1523 | `"    \"\"\"Create deterministic overview, source-line pages, and all counts without writing.\"\"\""` | — |
| [SRC-E599346ABE-L001524](../generate_index.py#L1524) | 1524 | `"    inventory = build_file_inventory(root)"` | — |
| [SRC-E599346ABE-L001525](../generate_index.py#L1525) | 1525 | `"    symbols, python_file_count = scan_repository(root)"` | — |
| [SRC-E599346ABE-L001526](../generate_index.py#L1526) | 1526 | `"    static_symbols = scan_static_symbols(root, inventory)"` | — |
| [SRC-E599346ABE-L001527](../generate_index.py#L1527) | 1527 | `"    source_lines = scan_source_lines(root, inventory)"` | — |
| [SRC-E599346ABE-L001528](../generate_index.py#L1528) | 1528 | `"    validate_source_line_coverage(inventory, source_lines)"` | — |
| [SRC-E599346ABE-L001529](../generate_index.py#L1529) | 1529 | `"    findings = scan_finding_annotations(source_lines)"` | — |
| [SRC-E599346ABE-L001530](../generate_index.py#L1530) | 1530 | `"    excluded_paths = discover_excluded_paths(root)"` | — |
| [SRC-E599346ABE-L001531](../generate_index.py#L1531) | 1531 | `"    coverage_audit_markdown = render_coverage_audit_markdown("` | — |
| [SRC-E599346ABE-L001532](../generate_index.py#L1532) | 1532 | `"        root, inventory, source_lines, excluded_paths"` | — |
| [SRC-E599346ABE-L001533](../generate_index.py#L1533) | 1533 | `"    )"` | — |
| [SRC-E599346ABE-L001534](../generate_index.py#L1534) | 1534 | `"    source_pages, pages_by_file = render_source_line_pages("` | — |
| [SRC-E599346ABE-L001535](../generate_index.py#L1535) | 1535 | `"        source_lines, inventory, findings"` | — |
| [SRC-E599346ABE-L001536](../generate_index.py#L1536) | 1536 | `"    )"` | — |
| [SRC-E599346ABE-L001537](../generate_index.py#L1537) | 1537 | `"    markdown = render_markdown("` | — |
| [SRC-E599346ABE-L001538](../generate_index.py#L1538) | 1538 | `"        symbols, python_file_count, inventory, static_symbols, source_lines, findings"` | — |
| [SRC-E599346ABE-L001539](../generate_index.py#L1539) | 1539 | `"    )"` | — |
| [SRC-E599346ABE-L001540](../generate_index.py#L1540) | 1540 | `"    source_lines_markdown = render_source_lines_markdown("` | — |
| [SRC-E599346ABE-L001541](../generate_index.py#L1541) | 1541 | `"        source_lines, inventory, findings, pages_by_file, source_pages"` | — |
| [SRC-E599346ABE-L001542](../generate_index.py#L1542) | 1542 | `"    )"` | — |
| [SRC-E599346ABE-L001543](../generate_index.py#L1543) | 1543 | `"    return ("` | — |
| [SRC-E599346ABE-L001544](../generate_index.py#L1544) | 1544 | `"        markdown,"` | — |
| [SRC-E599346ABE-L001545](../generate_index.py#L1545) | 1545 | `"        source_lines_markdown,"` | — |
| [SRC-E599346ABE-L001546](../generate_index.py#L1546) | 1546 | `"        coverage_audit_markdown,"` | — |
| [SRC-E599346ABE-L001547](../generate_index.py#L1547) | 1547 | `"        source_pages,"` | — |
| [SRC-E599346ABE-L001548](../generate_index.py#L1548) | 1548 | `"        python_file_count,"` | — |
| [SRC-E599346ABE-L001549](../generate_index.py#L1549) | 1549 | `"        len(inventory),"` | — |
| [SRC-E599346ABE-L001550](../generate_index.py#L1550) | 1550 | `"        len(symbols),"` | — |
| [SRC-E599346ABE-L001551](../generate_index.py#L1551) | 1551 | `"        len(source_lines),"` | — |
| [SRC-E599346ABE-L001552](../generate_index.py#L1552) | 1552 | `"        len(findings),"` | — |
| [SRC-E599346ABE-L001553](../generate_index.py#L1553) | 1553 | `"        sum(symbol.documented is True for symbol in symbols),"` | — |
| [SRC-E599346ABE-L001554](../generate_index.py#L1554) | 1554 | `"        sum(symbol.documented is False for symbol in symbols),"` | — |
| [SRC-E599346ABE-L001555](../generate_index.py#L1555) | 1555 | `"    )"` | — |
| [SRC-E599346ABE-L001556](../generate_index.py#L1556) | 1556 | `""` | — |
| [SRC-E599346ABE-L001557](../generate_index.py#L1557) | 1557 | `""` | — |
| [SRC-E599346ABE-L001558](../generate_index.py#L1558) | 1558 | `"def main(argv: Sequence[str] \| None = None) -> int:"` | — |
| [SRC-E599346ABE-L001559](../generate_index.py#L1559) | 1559 | `"    \"\"\"Generate the living repository index or check that the committed copy is current.\"\"\""` | — |
| [SRC-E599346ABE-L001560](../generate_index.py#L1560) | 1560 | `"    parser = argparse.ArgumentParser("` | — |
| [SRC-E599346ABE-L001561](../generate_index.py#L1561) | 1561 | `"        description=\"إنشاء/فحص فهرس مستودع Omarai وملفات الشفرة والرموز الساكنة.\""` | — |
| [SRC-E599346ABE-L001562](../generate_index.py#L1562) | 1562 | `"    )"` | — |
| [SRC-E599346ABE-L001563](../generate_index.py#L1563) | 1563 | `"    parser.add_argument("` | — |
| [SRC-E599346ABE-L001564](../generate_index.py#L1564) | 1564 | `"        \"--root\","` | — |
| [SRC-E599346ABE-L001565](../generate_index.py#L1565) | 1565 | `"        type=Path,"` | — |
| [SRC-E599346ABE-L001566](../generate_index.py#L1566) | 1566 | `"        default=Path(__file__).resolve().parents[1],"` | — |
| [SRC-E599346ABE-L001567](../generate_index.py#L1567) | 1567 | `"        help=\"مسار جذر المستودع (الافتراضي: جذر مشروع Omarai).\","` | — |
| [SRC-E599346ABE-L001568](../generate_index.py#L1568) | 1568 | `"    )"` | — |
| [SRC-E599346ABE-L001569](../generate_index.py#L1569) | 1569 | `"    parser.add_argument("` | — |
| [SRC-E599346ABE-L001570](../generate_index.py#L1570) | 1570 | `"        \"--check\","` | — |
| [SRC-E599346ABE-L001571](../generate_index.py#L1571) | 1571 | `"        action=\"store_true\","` | — |
| [SRC-E599346ABE-L001572](../generate_index.py#L1572) | 1572 | `"        help=\"لا تكتب ملفات؛ أعد حالة فشل إذا كان أي فهرس مولّد قديمًا أو مفقودًا.\","` | — |
| [SRC-E599346ABE-L001573](../generate_index.py#L1573) | 1573 | `"    )"` | — |
| [SRC-E599346ABE-L001574](../generate_index.py#L1574) | 1574 | `"    arguments = parser.parse_args(argv)"` | — |
| [SRC-E599346ABE-L001575](../generate_index.py#L1575) | 1575 | `""` | — |
| [SRC-E599346ABE-L001576](../generate_index.py#L1576) | 1576 | `"    try:"` | — |
| [SRC-E599346ABE-L001577](../generate_index.py#L1577) | 1577 | `"        root = arguments.root.resolve(strict=True)"` | — |
| [SRC-E599346ABE-L001578](../generate_index.py#L1578) | 1578 | `"        if not root.is_dir():"` | — |
| [SRC-E599346ABE-L001579](../generate_index.py#L1579) | 1579 | `"            raise ValueError(f\"المسار المحدد ليس مجلدًا: {root}\")"` | — |
| [SRC-E599346ABE-L001580](../generate_index.py#L1580) | 1580 | `"        ("` | — |
| [SRC-E599346ABE-L001581](../generate_index.py#L1581) | 1581 | `"            markdown,"` | — |
| [SRC-E599346ABE-L001582](../generate_index.py#L1582) | 1582 | `"            source_lines_markdown,"` | — |
| [SRC-E599346ABE-L001583](../generate_index.py#L1583) | 1583 | `"            coverage_audit_markdown,"` | — |
| [SRC-E599346ABE-L001584](../generate_index.py#L1584) | 1584 | `"            source_pages,"` | — |
| [SRC-E599346ABE-L001585](../generate_index.py#L1585) | 1585 | `"            python_file_count,"` | — |
| [SRC-E599346ABE-L001586](../generate_index.py#L1586) | 1586 | `"            repository_file_count,"` | — |
| [SRC-E599346ABE-L001587](../generate_index.py#L1587) | 1587 | `"            symbol_count,"` | — |
| [SRC-E599346ABE-L001588](../generate_index.py#L1588) | 1588 | `"            source_line_count,"` | — |
| [SRC-E599346ABE-L001589](../generate_index.py#L1589) | 1589 | `"            finding_count,"` | — |
| [SRC-E599346ABE-L001590](../generate_index.py#L1590) | 1590 | `"            documented_count,"` | — |
| [SRC-E599346ABE-L001591](../generate_index.py#L1591) | 1591 | `"            missing_count,"` | — |
| [SRC-E599346ABE-L001592](../generate_index.py#L1592) | 1592 | `"        ) = _generate(root)"` | — |
| [SRC-E599346ABE-L001593](../generate_index.py#L1593) | 1593 | `"        output_path = root / INDEX_RELATIVE_PATH"` | — |
| [SRC-E599346ABE-L001594](../generate_index.py#L1594) | 1594 | `"        source_lines_output_path = root / SOURCE_LINES_INDEX_RELATIVE_PATH"` | — |
| [SRC-E599346ABE-L001595](../generate_index.py#L1595) | 1595 | `"        generated_outputs = {"` | — |
| [SRC-E599346ABE-L001596](../generate_index.py#L1596) | 1596 | `"            INDEX_RELATIVE_PATH: markdown,"` | — |
| [SRC-E599346ABE-L001597](../generate_index.py#L1597) | 1597 | `"            SOURCE_LINES_INDEX_RELATIVE_PATH: source_lines_markdown,"` | — |
| [SRC-E599346ABE-L001598](../generate_index.py#L1598) | 1598 | `"            COVERAGE_AUDIT_RELATIVE_PATH: coverage_audit_markdown,"` | — |
| [SRC-E599346ABE-L001599](../generate_index.py#L1599) | 1599 | `"            **source_pages,"` | — |
| [SRC-E599346ABE-L001600](../generate_index.py#L1600) | 1600 | `"        }"` | — |
| [SRC-E599346ABE-L001601](../generate_index.py#L1601) | 1601 | `""` | — |
| [SRC-E599346ABE-L001602](../generate_index.py#L1602) | 1602 | `"        if arguments.check:"` | — |
| [SRC-E599346ABE-L001603](../generate_index.py#L1603) | 1603 | `"            for relative_path, expected_content in generated_outputs.items():"` | — |
| [SRC-E599346ABE-L001604](../generate_index.py#L1604) | 1604 | `"                generated_path = root / relative_path"` | — |
| [SRC-E599346ABE-L001605](../generate_index.py#L1605) | 1605 | `"                try:"` | — |
| [SRC-E599346ABE-L001606](../generate_index.py#L1606) | 1606 | `"                    current_content = generated_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-E599346ABE-L001607](../generate_index.py#L1607) | 1607 | `"                except FileNotFoundError:"` | — |
| [SRC-E599346ABE-L001608](../generate_index.py#L1608) | 1608 | `"                    print("` | — |
| [SRC-E599346ABE-L001609](../generate_index.py#L1609) | 1609 | `"                        f\"فهرس مولّد مفقود: {generated_path}. \""` | — |
| [SRC-E599346ABE-L001610](../generate_index.py#L1610) | 1610 | `"                        \"شغّل python docs/generate_index.py.\","` | — |
| [SRC-E599346ABE-L001611](../generate_index.py#L1611) | 1611 | `"                        file=sys.stderr,"` | — |
| [SRC-E599346ABE-L001612](../generate_index.py#L1612) | 1612 | `"                    )"` | — |
| [SRC-E599346ABE-L001613](../generate_index.py#L1613) | 1613 | `"                    return 1"` | — |
| [SRC-E599346ABE-L001614](../generate_index.py#L1614) | 1614 | `"                if current_content != expected_content:"` | — |
| [SRC-E599346ABE-L001615](../generate_index.py#L1615) | 1615 | `"                    if relative_path == INDEX_RELATIVE_PATH:"` | — |
| [SRC-E599346ABE-L001616](../generate_index.py#L1616) | 1616 | `"                        message = \"الفهرس قديم (الرئيسي)\""` | — |
| [SRC-E599346ABE-L001617](../generate_index.py#L1617) | 1617 | `"                    elif relative_path == SOURCE_LINES_INDEX_RELATIVE_PATH:"` | — |
| [SRC-E599346ABE-L001618](../generate_index.py#L1618) | 1618 | `"                        message = \"فهرس الأسطر قديم\""` | — |
| [SRC-E599346ABE-L001619](../generate_index.py#L1619) | 1619 | `"                    else:"` | — |
| [SRC-E599346ABE-L001620](../generate_index.py#L1620) | 1620 | `"                        message = \"فهرس تغطية الفهرسة قديم\""` | — |
| [SRC-E599346ABE-L001621](../generate_index.py#L1621) | 1621 | `"                    print("` | — |
| [SRC-E599346ABE-L001622](../generate_index.py#L1622) | 1622 | `"                        f\"{message}: {generated_path}. \""` | — |
| [SRC-E599346ABE-L001623](../generate_index.py#L1623) | 1623 | `"                        \"شغّل python docs/generate_index.py.\","` | — |
| [SRC-E599346ABE-L001624](../generate_index.py#L1624) | 1624 | `"                        file=sys.stderr,"` | — |
| [SRC-E599346ABE-L001625](../generate_index.py#L1625) | 1625 | `"                    )"` | — |
| [SRC-E599346ABE-L001626](../generate_index.py#L1626) | 1626 | `"                    return 1"` | — |
| [SRC-E599346ABE-L001627](../generate_index.py#L1627) | 1627 | `""` | — |
| [SRC-E599346ABE-L001628](../generate_index.py#L1628) | 1628 | `"            pages_directory = root / SOURCE_LINES_PAGES_DIR"` | — |
| [SRC-E599346ABE-L001629](../generate_index.py#L1629) | 1629 | `"            expected_page_names = {"` | — |
| [SRC-E599346ABE-L001630](../generate_index.py#L1630) | 1630 | `"                Path(relative_path).name"` | — |
| [SRC-E599346ABE-L001631](../generate_index.py#L1631) | 1631 | `"                for relative_path in source_pages"` | — |
| [SRC-E599346ABE-L001632](../generate_index.py#L1632) | 1632 | `"            }"` | — |
| [SRC-E599346ABE-L001633](../generate_index.py#L1633) | 1633 | `"            if pages_directory.exists():"` | — |
| [SRC-E599346ABE-L001634](../generate_index.py#L1634) | 1634 | `"                actual_page_names = {"` | — |
| [SRC-E599346ABE-L001635](../generate_index.py#L1635) | 1635 | `"                    path.name"` | — |
| [SRC-E599346ABE-L001636](../generate_index.py#L1636) | 1636 | `"                    for path in pages_directory.iterdir()"` | — |
| [SRC-E599346ABE-L001637](../generate_index.py#L1637) | 1637 | `"                    if path.is_file() and SOURCE_LINES_PAGE_RE.fullmatch(path.name)"` | — |
| [SRC-E599346ABE-L001638](../generate_index.py#L1638) | 1638 | `"                }"` | — |
| [SRC-E599346ABE-L001639](../generate_index.py#L1639) | 1639 | `"                stale_pages = actual_page_names - expected_page_names"` | — |
| [SRC-E599346ABE-L001640](../generate_index.py#L1640) | 1640 | `"                if stale_pages:"` | — |
| [SRC-E599346ABE-L001641](../generate_index.py#L1641) | 1641 | `"                    print("` | — |
| [SRC-E599346ABE-L001642](../generate_index.py#L1642) | 1642 | `"                        \"صفحات فهرس قديمة يجب حذفها بإعادة التوليد: \""` | — |
| [SRC-E599346ABE-L001643](../generate_index.py#L1643) | 1643 | `"                        + \", \".join(sorted(stale_pages)),"` | — |
| [SRC-E599346ABE-L001644](../generate_index.py#L1644) | 1644 | `"                        file=sys.stderr,"` | — |
| [SRC-E599346ABE-L001645](../generate_index.py#L1645) | 1645 | `"                    )"` | — |
| [SRC-E599346ABE-L001646](../generate_index.py#L1646) | 1646 | `"                    return 1"` | — |
| [SRC-E599346ABE-L001647](../generate_index.py#L1647) | 1647 | `"            changed = False"` | — |
| [SRC-E599346ABE-L001648](../generate_index.py#L1648) | 1648 | `"        else:"` | — |
| [SRC-E599346ABE-L001649](../generate_index.py#L1649) | 1649 | `"            changed = False"` | — |
| [SRC-E599346ABE-L001650](../generate_index.py#L1650) | 1650 | `"            for relative_path, generated_content in generated_outputs.items():"` | — |
| [SRC-E599346ABE-L001651](../generate_index.py#L1651) | 1651 | `"                if write_if_changed(root / relative_path, generated_content):"` | — |
| [SRC-E599346ABE-L001652](../generate_index.py#L1652) | 1652 | `"                    changed = True"` | — |
| [SRC-E599346ABE-L001653](../generate_index.py#L1653) | 1653 | `""` | — |
| [SRC-E599346ABE-L001654](../generate_index.py#L1654) | 1654 | `"            pages_directory = root / SOURCE_LINES_PAGES_DIR"` | — |
| [SRC-E599346ABE-L001655](../generate_index.py#L1655) | 1655 | `"            if pages_directory.exists():"` | — |
| [SRC-E599346ABE-L001656](../generate_index.py#L1656) | 1656 | `"                expected_page_names = {"` | — |
| [SRC-E599346ABE-L001657](../generate_index.py#L1657) | 1657 | `"                    Path(relative_path).name"` | — |
| [SRC-E599346ABE-L001658](../generate_index.py#L1658) | 1658 | `"                    for relative_path in source_pages"` | — |
| [SRC-E599346ABE-L001659](../generate_index.py#L1659) | 1659 | `"                }"` | — |
| [SRC-E599346ABE-L001660](../generate_index.py#L1660) | 1660 | `"                for path in pages_directory.iterdir():"` | — |
| [SRC-E599346ABE-L001661](../generate_index.py#L1661) | 1661 | `"                    if ("` | — |
| [SRC-E599346ABE-L001662](../generate_index.py#L1662) | 1662 | `"                        path.is_file()"` | — |
| [SRC-E599346ABE-L001663](../generate_index.py#L1663) | 1663 | `"                        and SOURCE_LINES_PAGE_RE.fullmatch(path.name)"` | — |
| [SRC-E599346ABE-L001664](../generate_index.py#L1664) | 1664 | `"                        and path.name not in expected_page_names"` | — |
| [SRC-E599346ABE-L001665](../generate_index.py#L1665) | 1665 | `"                    ):"` | — |
| [SRC-E599346ABE-L001666](../generate_index.py#L1666) | 1666 | `"                        path.unlink()"` | — |
| [SRC-E599346ABE-L001667](../generate_index.py#L1667) | 1667 | `"                        changed = True"` | — |
| [SRC-E599346ABE-L001668](../generate_index.py#L1668) | 1668 | `"    except (IndexGenerationError, OSError, ValueError) as exc:"` | — |
| [SRC-E599346ABE-L001669](../generate_index.py#L1669) | 1669 | `"        print(f\"خطأ في إنشاء فهرس Omarai: {exc}\", file=sys.stderr)"` | — |
| [SRC-E599346ABE-L001670](../generate_index.py#L1670) | 1670 | `"        return 1"` | — |
| [SRC-E599346ABE-L001671](../generate_index.py#L1671) | 1671 | `""` | — |
| [SRC-E599346ABE-L001672](../generate_index.py#L1672) | 1672 | `"    if arguments.check:"` | — |
| [SRC-E599346ABE-L001673](../generate_index.py#L1673) | 1673 | `"        action = \"الفهرس محدث والتحقق ناجح\""` | — |
| [SRC-E599346ABE-L001674](../generate_index.py#L1674) | 1674 | `"    else:"` | — |
| [SRC-E599346ABE-L001675](../generate_index.py#L1675) | 1675 | `"        action = \"تم تحديث\" if changed else \"الفهرس محدث بالفعل\""` | — |
| [SRC-E599346ABE-L001676](../generate_index.py#L1676) | 1676 | `"    print("` | — |
| [SRC-E599346ABE-L001677](../generate_index.py#L1677) | 1677 | `"        f\"{action}: {output_path} \| \""` | — |
| [SRC-E599346ABE-L001678](../generate_index.py#L1678) | 1678 | `"        f\"ملفات المستودع: {repository_file_count} \| \""` | — |
| [SRC-E599346ABE-L001679](../generate_index.py#L1679) | 1679 | `"        f\"ملفات Python: {python_file_count} \| \""` | — |
| [SRC-E599346ABE-L001680](../generate_index.py#L1680) | 1680 | `"        f\"تعريفات Python: {symbol_count} \| \""` | — |
| [SRC-E599346ABE-L001681](../generate_index.py#L1681) | 1681 | `"        f\"أسطر مفهرسة: {source_line_count} \| \""` | — |
| [SRC-E599346ABE-L001682](../generate_index.py#L1682) | 1682 | `"        f\"صفحات أسطر: {len(source_pages)} \| \""` | — |
| [SRC-E599346ABE-L001683](../generate_index.py#L1683) | 1683 | `"        f\"وسوم مراجعة: {finding_count} \| \""` | — |
| [SRC-E599346ABE-L001684](../generate_index.py#L1684) | 1684 | `"        f\"موثق: {documented_count} \| \""` | — |
| [SRC-E599346ABE-L001685](../generate_index.py#L1685) | 1685 | `"        f\"ناقص Docstring: {missing_count}\""` | — |
| [SRC-E599346ABE-L001686](../generate_index.py#L1686) | 1686 | `"    )"` | — |
| [SRC-E599346ABE-L001687](../generate_index.py#L1687) | 1687 | `"    return 0"` | — |
| [SRC-E599346ABE-L001688](../generate_index.py#L1688) | 1688 | `""` | — |
| [SRC-E599346ABE-L001689](../generate_index.py#L1689) | 1689 | `""` | — |
| [SRC-E599346ABE-L001690](../generate_index.py#L1690) | 1690 | `"if __name__ == \"__main__\":"` | — |
| [SRC-E599346ABE-L001691](../generate_index.py#L1691) | 1691 | `"    raise SystemExit(main())"` | — |
## وثائق وفهرسة

### FILE-6E35221BFA — [docs/GO_LIVE_CHECKLIST_AR.md](../GO_LIVE_CHECKLIST_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-6E35221BFA-L000001](../GO_LIVE_CHECKLIST_AR.md#L1) | 1 | `"# قائمة قبول Omarai قبل التشغيل العام"` | — |
| [SRC-6E35221BFA-L000002](../GO_LIVE_CHECKLIST_AR.md#L2) | 2 | `""` | — |
| [SRC-6E35221BFA-L000003](../GO_LIVE_CHECKLIST_AR.md#L3) | 3 | `"هذه القائمة تفصل بين نجاح البناء وبين إثبات أن الوكيل يعمل عبر عنوان استضافة عام."` | — |
| [SRC-6E35221BFA-L000004](../GO_LIVE_CHECKLIST_AR.md#L4) | 4 | `""` | — |
| [SRC-6E35221BFA-L000005](../GO_LIVE_CHECKLIST_AR.md#L5) | 5 | `"راجع أيضًا [مصفوفة أدلة الاختبار](OMARAI_TEST_EVIDENCE_MATRIX_AR.md) للتمييز بين اختبارات الوحدة والـMocks واختبارات الحاوية والقبول الحي، وحالة كل إثبات وحدوده. نتائج CI وحدها لا تعني أن خدمة مستضافة أو كل موفر خارجي يعمل حيًا."` | — |
| [SRC-6E35221BFA-L000006](../GO_LIVE_CHECKLIST_AR.md#L6) | 6 | `""` | — |
| [SRC-6E35221BFA-L000007](../GO_LIVE_CHECKLIST_AR.md#L7) | 7 | `"## إعداد الاستضافة"` | — |
| [SRC-6E35221BFA-L000008](../GO_LIVE_CHECKLIST_AR.md#L8) | 8 | `""` | — |
| [SRC-6E35221BFA-L000009](../GO_LIVE_CHECKLIST_AR.md#L9) | 9 | `"1. اتبع [دليل النشر العربي](DEPLOY_RAILWAY_AR.md) وأنشئ الخدمة يدويًا في حساب الاستضافة."` | — |
| [SRC-6E35221BFA-L000010](../GO_LIVE_CHECKLIST_AR.md#L10) | 10 | ``"2. استخدم المستودع `mosabosama2030-oss/omarai` والفرع `main` وإعداد Docker المرفق."`` | — |
| [SRC-6E35221BFA-L000011](../GO_LIVE_CHECKLIST_AR.md#L11) | 11 | ``"3. اضبط الأسرار من لوحة الاستضافة فقط: `OMARAI_PUBLIC_DEPLOYMENT=1`، ورمز `OMARAI_ACCESS_TOKEN` عشوائي بطول 32 حرفًا على الأقل، ومفتاح مزود النموذج `OPENROUTER_API_KEY` أو `OMARAI_LLM_API_KEY`."`` | — |
| [SRC-6E35221BFA-L000012](../GO_LIVE_CHECKLIST_AR.md#L12) | 12 | ``"4. اترك `OMARAI_OPENROUTER_WEB_SEARCH` غير مضبوط ما لم تراجع التكلفة وتوافق عليها."`` | — |
| [SRC-6E35221BFA-L000013](../GO_LIVE_CHECKLIST_AR.md#L13) | 13 | ``"5. أنشئ نطاق HTTPS وتحقق من `https://your-app.example.com/api/health`."`` | — |
| [SRC-6E35221BFA-L000014](../GO_LIVE_CHECKLIST_AR.md#L14) | 14 | `""` | — |
| [SRC-6E35221BFA-L000015](../GO_LIVE_CHECKLIST_AR.md#L15) | 15 | `"## اختبار قبول حي"` | — |
| [SRC-6E35221BFA-L000016](../GO_LIVE_CHECKLIST_AR.md#L16) | 16 | `""` | — |
| [SRC-6E35221BFA-L000017](../GO_LIVE_CHECKLIST_AR.md#L17) | 17 | ``"أضف GitHub Actions secret باسم `OMARAI_ACCESS_TOKEN` واجعل قيمته مطابقة لرمز الوصول في الاستضافة، وأضف secret باسم `OMARAI_BASE_URL` بقيمة أصل HTTPS للخدمة مثل `https://your-app.example.com` دون مسار إضافي. لا تضع رمز الوصول في مدخلات workflow أو الدردشة أو السجلات. بعد ضبط السرّين، افتح **Actions → Omarai hosted acceptance smoke → Run workflow**. يستهدف الاختبار النطاق المحفوظ في إعدادات المستودع؛ لا يأخذ عنوانًا حرًا من مُشغّل workflow، لتجنب إرسال رمز الوصول إلى وجهة غير مقصودة."`` | — |
| [SRC-6E35221BFA-L000018](../GO_LIVE_CHECKLIST_AR.md#L18) | 18 | `""` | — |
| [SRC-6E35221BFA-L000019](../GO_LIVE_CHECKLIST_AR.md#L19) | 19 | `"الاختبار الحي ينفذ فحص الصحة، ويرفض طلب API بلا رمز، ثم يختبر البحث والنموذج ويطلب إجابة عربية فعلية. قد يستهلك رصيد مزود النموذج أو البحث؛ شغّله فقط بعد الموافقة على ذلك."` | — |
| [SRC-6E35221BFA-L000020](../GO_LIVE_CHECKLIST_AR.md#L20) | 20 | `""` | — |
| [SRC-6E35221BFA-L000021](../GO_LIVE_CHECKLIST_AR.md#L21) | 21 | `"## شروط النجاح"` | — |
| [SRC-6E35221BFA-L000022](../GO_LIVE_CHECKLIST_AR.md#L22) | 22 | `""` | — |
| [SRC-6E35221BFA-L000023](../GO_LIVE_CHECKLIST_AR.md#L23) | 23 | ``"- `/api/health` يعيد HTTP 200 وصحة سليمة."`` | — |
| [SRC-6E35221BFA-L000024](../GO_LIVE_CHECKLIST_AR.md#L24) | 24 | ``"- طلب `POST /api/agent` بلا رمز يعيد HTTP 401."`` | — |
| [SRC-6E35221BFA-L000025](../GO_LIVE_CHECKLIST_AR.md#L25) | 25 | `"- التشخيص يثبت اتصال البحث الفعلي واستلام استجابة فعلية من النموذج."` | — |
| [SRC-6E35221BFA-L000026](../GO_LIVE_CHECKLIST_AR.md#L26) | 26 | `"- السؤال العربي يعيد إجابة ومصادر صالحة، مع التأكد من أن البحث والنموذج مستخدمان."` | — |
| [SRC-6E35221BFA-L000027](../GO_LIVE_CHECKLIST_AR.md#L27) | 27 | `"- لا يظهر أي رمز وصول أو مفتاح API في التقرير."` | — |
| [SRC-6E35221BFA-L000028](../GO_LIVE_CHECKLIST_AR.md#L28) | 28 | `""` | — |
| [SRC-6E35221BFA-L000029](../GO_LIVE_CHECKLIST_AR.md#L29) | 29 | `"## اختبار يدوي على Android"` | — |
| [SRC-6E35221BFA-L000030](../GO_LIVE_CHECKLIST_AR.md#L30) | 30 | `""` | — |
| [SRC-6E35221BFA-L000031](../GO_LIVE_CHECKLIST_AR.md#L31) | 31 | `"بعد نجاح الاختبار الآلي، افتح الموقع من متصفح الهاتف، وأدخل رمز الوصول في الواجهة، ثم اختبر سؤالًا عربيًا وفتح المصادر في تبويب منفصل. جرّب رمزًا خاطئًا وتحقق من رسالة الرفض. استخدم أسئلة عامة فقط، ولا تستخدم بيانات عملاء حقيقية."` | — |
| [SRC-6E35221BFA-L000032](../GO_LIVE_CHECKLIST_AR.md#L32) | 32 | `""` | — |
| [SRC-6E35221BFA-L000033](../GO_LIVE_CHECKLIST_AR.md#L33) | 33 | `"## حدود مهمة"` | — |
| [SRC-6E35221BFA-L000034](../GO_LIVE_CHECKLIST_AR.md#L34) | 34 | `""` | — |
| [SRC-6E35221BFA-L000035](../GO_LIVE_CHECKLIST_AR.md#L35) | 35 | `"إعداد Docker وRailway لا ينشئ خدمة الاستضافة تلقائيًا ولا يضبط أسرار الحساب. قاعدة SQLite قد لا تكون دائمة على حاوية مؤقتة، وحد الطلبات الحالي محفوظ في ذاكرة العملية، والرؤوس التي يرسلها الوكيل العكسي تتطلب إعدادًا موثوقًا. لا تعتبر الاختبار الحي ضمانًا للاستمرارية، ولا تغني هذه القائمة عن مراجعة الأمان أو موافقة صاحب المشروع على الدمج."` | — |
## وثائق وفهرسة

### FILE-C8EA754D73 — [docs/IMPLEMENTATION_SCOPE.md](../IMPLEMENTATION_SCOPE.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-C8EA754D73-L000001](../IMPLEMENTATION_SCOPE.md#L1) | 1 | `"# Omarai — نطاق التنفيذ الفعلي وحدوده"` | — |
| [SRC-C8EA754D73-L000002](../IMPLEMENTATION_SCOPE.md#L2) | 2 | `""` | — |
| [SRC-C8EA754D73-L000003](../IMPLEMENTATION_SCOPE.md#L3) | 3 | `"**Purpose:** Keep this scope note aligned with the source code and operator-visible claims. This document is a scope description, not a certification of compliance or live-provider availability."` | — |
| [SRC-C8EA754D73-L000004](../IMPLEMENTATION_SCOPE.md#L4) | 4 | `""` | — |
| [SRC-C8EA754D73-L000005](../IMPLEMENTATION_SCOPE.md#L5) | 5 | ``"**Baseline reviewed:** `main` at merge commit `c3d3f8b1843cb58a9cbc02a69e8edc9e6410abaa` (2026-10-19), after PR #44 and PR #45 were merged.  "`` | — |
| [SRC-C8EA754D73-L000006](../IMPLEMENTATION_SCOPE.md#L6) | 6 | ``"**Evidence labels:** `VERIFIED` means directly confirmed in source or a named automated check; `INFERRED` means a bounded conclusion from source structure; `UNKNOWN` means live or environmental evidence is not available. A source-level capability must not be described as a live integration test."`` | — |
| [SRC-C8EA754D73-L000007](../IMPLEMENTATION_SCOPE.md#L7) | 7 | `""` | — |
| [SRC-C8EA754D73-L000008](../IMPLEMENTATION_SCOPE.md#L8) | 8 | `"## Implemented in the repository"` | — |
| [SRC-C8EA754D73-L000009](../IMPLEMENTATION_SCOPE.md#L9) | 9 | `""` | — |
| [SRC-C8EA754D73-L000010](../IMPLEMENTATION_SCOPE.md#L10) | 10 | `"- **Lead workspace — VERIFIED in source:** Arabic phrase normalization and heuristic intent scoring; SQLite lead persistence; duplicate detection; source metadata; manual lead-status lifecycle; CSV import/export; CLI and HTTP API."` | — |
| [SRC-C8EA754D73-L000011](../IMPLEMENTATION_SCOPE.md#L11) | 11 | `"- **Research pipeline — VERIFIED in source:** natural-language search planning with deterministic fallback; DuckDuckGo HTML and Bing RSS search; Google News RSS for freshness-sensitive requests; evidence fusion/ranking; selected public page extraction; source/provenance metadata and research diagnostics."` | — |
| [SRC-C8EA754D73-L000012](../IMPLEMENTATION_SCOPE.md#L12) | 12 | `"- **Optional connectors — VERIFIED as conditional code paths only:** Brave and Tavily when configured; DeepSeek Search when explicitly enabled with its API key; selected public social endpoints and official platform APIs when their required credentials are configured. This does not prove a specific credential, account, quota, or live connector currently works."` | — |
| [SRC-C8EA754D73-L000013](../IMPLEMENTATION_SCOPE.md#L13) | 13 | `"- **External language model — VERIFIED in source:** an OpenAI-compatible model endpoint is used for planning, answer generation and model-assisted review when a key is configured. The user question, selected history and page excerpts may be sent to that configured external provider. Omarai is not a locally trained foundation model and does not operate as an offline-only reasoning system."` | — |
| [SRC-C8EA754D73-L000014](../IMPLEMENTATION_SCOPE.md#L14) | 14 | `"- **Evidence and failure reporting — VERIFIED in source:** the answer includes sources, search-attempt outcome and diagnostic metadata; the code expressly describes its second-pass claim review as model-assisted, not an independent deterministic fact-check. Source count, domain count, and coverage indicators are not probabilities of truth or proof of editorial independence."` | — |
| [SRC-C8EA754D73-L000015](../IMPLEMENTATION_SCOPE.md#L15) | 15 | `"- **HTTP/API and UI — VERIFIED in source:** Arabic RTL web interfaces, JSON endpoints, API input checks, same-origin/configured-origin handling, an in-memory per-client rate limiter, and bearer-token protection for protected API routes when public-deployment mode is enabled."` | — |
| [SRC-C8EA754D73-L000016](../IMPLEMENTATION_SCOPE.md#L16) | 16 | `"- **Deployment configuration — VERIFIED in source:** a Dockerfile and hosting configuration exist. Their existence alone does not prove a live service was deployed, is reachable, has persistent disk, or has passed live smoke tests."` | — |
| [SRC-C8EA754D73-L000017](../IMPLEMENTATION_SCOPE.md#L17) | 17 | ``"- **Automated validation — VERIFIED within the listed test scope:** after the budget/concurrency change, GitHub Actions run [39198411650](https://github.com/mosabosama2030-oss/omarai/actions/runs/39198411650) on PR #44 head `de20d029cb9877c8fdef62148f643eb9022b0956` passed Ruff, 232 pytest tests on Python 3.11, 232 pytest tests on Python 3.12, and container/protected-API smoke checks. PR #45 head `35e85ceae13b15f273997eba043b12126652f05a` passed run [39198109298](https://github.com/mosabosama2030-oss/omarai/actions/runs/39198109298), with 224 pytest tests on each Python version and container smoke checks. Both PRs were subsequently merged into the reviewed `main` lineage. These CI results do not prove live search-provider availability, factual correctness, load capacity, deployment health, or database restore."`` | — |
| [SRC-C8EA754D73-L000018](../IMPLEMENTATION_SCOPE.md#L18) | 18 | `""` | — |
| [SRC-C8EA754D73-L000019](../IMPLEMENTATION_SCOPE.md#L19) | 19 | `"## Explicitly out of scope or not yet proven"` | — |
| [SRC-C8EA754D73-L000020](../IMPLEMENTATION_SCOPE.md#L20) | 20 | `""` | — |
| [SRC-C8EA754D73-L000021](../IMPLEMENTATION_SCOPE.md#L21) | 21 | `"- **Multi-user or multi-tenant service — NOT IMPLEMENTED in the reviewed baseline:** the API uses one shared bearer token and a shared lead store; it has no per-user identity, role-based authorization or tenant/data isolation. Anyone who obtains the token has the access granted by that token. Treat a hosted instance as a single-operator service unless and until these controls are implemented and tested."` | — |
| [SRC-C8EA754D73-L000022](../IMPLEMENTATION_SCOPE.md#L22) | 22 | `"- **Deterministic verification of every factual claim — NOT IMPLEMENTED:** citation-index validation and model-assisted review are not an independent proof that every sentence follows from its cited source. Users must be shown this limitation clearly."` | — |
| [SRC-C8EA754D73-L000023](../IMPLEMENTATION_SCOPE.md#L23) | 23 | `"- **Live provider reliability — UNKNOWN unless measured:** unit tests with mocks and a successful container smoke test do not establish that a provider is currently reachable, that credentials are valid, or that the produced answer is accurate."` | — |
| [SRC-C8EA754D73-L000024](../IMPLEMENTATION_SCOPE.md#L24) | 24 | ``"- **Request-wide limits — VERIFIED within automated unit-test scope:** merged code adds `agents/request_budget.py` and attaches a cooperative per-answer time/resource budget across search queries, provider search calls (including direct social HTTP operations), model attempts, page fetches, and optional server-side search-tool calls. The tested defaults are 90 seconds, 8 search queries, 32 provider/social HTTP operations, 8 model HTTP attempts, 8 page fetches, and up to 3 optional server-side tool calls, with hard-capped environment overrides. The API also applies a process-local semaphore to `/api/agent` and `/api/diagnostics` (default 4, hard maximum 8), returning 503 when all slots are occupied. Regression tests cover budget limits and rejection under an occupied slot. The deadline is cooperative, not hard cancellation; the semaphore is not distributed. Live connectors and production load remain UNKNOWN."`` | — |
| [SRC-C8EA754D73-L000025](../IMPLEMENTATION_SCOPE.md#L25) | 25 | `"- **Public operational configuration — UNKNOWN until verified per deployment:** actual reverse-proxy trust, CORS allowlist, TLS termination, secret configuration, deployed commit identity, and live endpoint behavior depend on the chosen host and configuration."` | — |
| [SRC-C8EA754D73-L000026](../IMPLEMENTATION_SCOPE.md#L26) | 26 | `"- **Database continuity — UNKNOWN:** backup, restore, and durable SQLite persistence have not been proven for a specific host. Do not store irreplaceable production leads until backup/restore and storage persistence are tested."` | — |
| [SRC-C8EA754D73-L000027](../IMPLEMENTATION_SCOPE.md#L27) | 27 | `"- **Load and concurrency capacity — UNKNOWN:** a process-local semaphore is present and its rejection path is unit-tested, but that does not establish throughput or a numeric concurrent-user capacity. Do not publish throughput, availability or capacity claims without representative measurements."` | — |
| [SRC-C8EA754D73-L000028](../IMPLEMENTATION_SCOPE.md#L28) | 28 | `"- **Historical secret exposure — UNKNOWN:** a clean scan of the current tree, if obtained, does not prove the entire Git history has never contained a secret."` | — |
| [SRC-C8EA754D73-L000029](../IMPLEMENTATION_SCOPE.md#L29) | 29 | `"- **Automated outbound contact — NOT IMPLEMENTED:** the agent does not send messages or contact people automatically. Any future outbound action must have explicit policy controls and human approval."` | — |
| [SRC-C8EA754D73-L000030](../IMPLEMENTATION_SCOPE.md#L30) | 30 | `""` | — |
| [SRC-C8EA754D73-L000031](../IMPLEMENTATION_SCOPE.md#L31) | 31 | `"## Operating assumptions"` | — |
| [SRC-C8EA754D73-L000032](../IMPLEMENTATION_SCOPE.md#L32) | 32 | `""` | — |
| [SRC-C8EA754D73-L000033](../IMPLEMENTATION_SCOPE.md#L33) | 33 | `"1. Keep the current architecture as a modular monolith unless evidence and a recorded architecture decision justify a change."` | — |
| [SRC-C8EA754D73-L000034](../IMPLEMENTATION_SCOPE.md#L34) | 34 | `"2. Default to a single-operator deployment with a private, randomly generated bearer token; never publish that token or share it as if it were individual user authentication."` | — |
| [SRC-C8EA754D73-L000035](../IMPLEMENTATION_SCOPE.md#L35) | 35 | `"3. Do not submit passwords, API keys, private information, or personal/confidential customer data to an external model provider, especially a free endpoint with its own retention/logging terms."` | — |
| [SRC-C8EA754D73-L000036](../IMPLEMENTATION_SCOPE.md#L36) | 36 | `"4. Treat page text, snippets, social posts, user history, and model output as untrusted data. They are not an authority to override application policy or execute privileged actions."` | — |
| [SRC-C8EA754D73-L000037](../IMPLEMENTATION_SCOPE.md#L37) | 37 | ``"5. Label each live connector probe, deployed smoke test, migration/restore test, and load test as `NOT_RUN` until that specific test actually runs. Do not infer its success from unit-test CI."`` | — |
| [SRC-C8EA754D73-L000038](../IMPLEMENTATION_SCOPE.md#L38) | 38 | `""` | — |
| [SRC-C8EA754D73-L000039](../IMPLEMENTATION_SCOPE.md#L39) | 39 | `"## Recommended next increments"` | — |
| [SRC-C8EA754D73-L000040](../IMPLEMENTATION_SCOPE.md#L40) | 40 | `""` | — |
| [SRC-C8EA754D73-L000041](../IMPLEMENTATION_SCOPE.md#L41) | 41 | `"1. Keep testing the merged cooperative budget against failure paths and resource exhaustion; do not describe it as hard cancellation or load-tested capacity."` | — |
| [SRC-C8EA754D73-L000042](../IMPLEMENTATION_SCOPE.md#L42) | 42 | `"2. Add deterministic citation-integrity controls and adversarial prompt-injection tests while retaining the limitation that source entailment cannot be proved by citation-index checks alone."` | — |
| [SRC-C8EA754D73-L000043](../IMPLEMENTATION_SCOPE.md#L43) | 43 | `"3. Reconcile the shared-token/single-store deployment with the declared single-operator scope; design real identity and data isolation before any multi-user public offering."` | — |
| [SRC-C8EA754D73-L000044](../IMPLEMENTATION_SCOPE.md#L44) | 44 | `"4. Add a repeatable live connector probe and a deployed acceptance report clearly separated from mock/unit-test results."` | — |
| [SRC-C8EA754D73-L000045](../IMPLEMENTATION_SCOPE.md#L45) | 45 | `"5. Test SQLite persistence and backup/restore on the selected host before storing production lead data."` | — |
| [SRC-C8EA754D73-L000046](../IMPLEMENTATION_SCOPE.md#L46) | 46 | ``"6. Reconcile remaining requirements to exact commit SHAs and individual tests; keep untested requirements `UNKNOWN` and unrun checks `NOT_RUN`."`` | — |
| [SRC-C8EA754D73-L000047](../IMPLEMENTATION_SCOPE.md#L47) | 47 | `"7. Keep all external contact and consequential actions human-approved."` | — |
## وثائق وفهرسة

### FILE-21D5D044E2 — [docs/OMARAI_EXCEPTIONS_REGISTER_AR.md](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-21D5D044E2-L000001](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L1) | 1 | `"# Omarai — سجل الاستثناءات والقرارات المؤجلة"` | — |
| [SRC-21D5D044E2-L000002](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L2) | 2 | `""` | — |
| [SRC-21D5D044E2-L000003](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L3) | 3 | `"**المعرف:** OMARAI-EXCEPTIONS-REGISTER-001  "` | — |
| [SRC-21D5D044E2-L000004](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L4) | 4 | `"**التاريخ:** 2026-10-19  "` | — |
| [SRC-21D5D044E2-L000005](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L5) | 5 | `"**الحالة:** مقترح للمراجعة — لم يُعتمد أي استثناء بموجب هذا الملف.  "` | — |
| [SRC-21D5D044E2-L000006](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L6) | 6 | `"**المسؤول عن القرار:** مدير المشروع البشري  "` | — |
| [SRC-21D5D044E2-L000007](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L7) | 7 | ``"**مرجع الحوكمة:** `GOV-003` و`GOV-004` و`GOV-005`"`` | — |
| [SRC-21D5D044E2-L000008](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L8) | 8 | `""` | — |
| [SRC-21D5D044E2-L000009](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L9) | 9 | `"## 1. الغرض وقواعد الاستخدام"` | — |
| [SRC-21D5D044E2-L000010](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L10) | 10 | `""` | — |
| [SRC-21D5D044E2-L000011](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L11) | 11 | ``"يوثق هذا السجل أي استثناء مطلوب من متطلب إلزامي `MUST` أو قرار بتحديد نطاق الإصدار. إعداد هذا السجل أو دمجه لا يعني قبول المخاطر المدرجة."`` | — |
| [SRC-21D5D044E2-L000012](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L12) | 12 | `""` | — |
| [SRC-21D5D044E2-L000013](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L13) | 13 | `"يجب أن يحتوي كل استثناء معتمد على: معرف المتطلب، السبب، النطاق، المخاطر والبيانات/القدرات المتأثرة، البديل التعويضي، صاحب صلاحية الموافقة، تاريخ أو شرط الانتهاء، ودليل إعادة النظر والإغلاق."` | — |
| [SRC-21D5D044E2-L000014](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L14) | 14 | `""` | — |
| [SRC-21D5D044E2-L000015](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L15) | 15 | ``"- `PROPOSED`: مقترح ينتظر قرارًا بشريًا صريحًا."`` | — |
| [SRC-21D5D044E2-L000016](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L16) | 16 | ``"- `WAIVED`: استثناء وافق عليه صاحب الصلاحية، بنطاق وحدود وموعد/شرط انتهاء."`` | — |
| [SRC-21D5D044E2-L000017](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L17) | 17 | ``"- `NOT APPLICABLE`: المتطلب لا ينطبق على نطاق محدد حاليًا مع السبب وشرط إعادة النظر."`` | — |
| [SRC-21D5D044E2-L000018](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L18) | 18 | ``"- `UNKNOWN`: الأدلة لا تكفي للحكم؛ لا يجوز استخدام استثناء لتغطية هذه الحالة."`` | — |
| [SRC-21D5D044E2-L000019](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L19) | 19 | ``"- `NOT RUN`: اختبار مطلوب لم يُنفذ."`` | — |
| [SRC-21D5D044E2-L000020](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L20) | 20 | `""` | — |
| [SRC-21D5D044E2-L000021](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L21) | 21 | `"لا توجد في هذا السجل موافقات بشرية مختلقة أو استثناءات مفتوحة إلى أجل غير محدد. **لا يُسجل أي عنصر كـWAIVED إلا بعد توثيق موافقتك الصريحة.**"` | — |
| [SRC-21D5D044E2-L000022](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L22) | 22 | `""` | — |
| [SRC-21D5D044E2-L000023](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L23) | 23 | `"## 2. سجل الاستثناءات المعتمدة"` | — |
| [SRC-21D5D044E2-L000024](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L24) | 24 | `""` | — |
| [SRC-21D5D044E2-L000025](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L25) | 25 | `"\| معرف الاستثناء \| المتطلب \| النطاق \| الموافِق \| الحالة \| الانتهاء/إعادة النظر \| دليل القرار \|"` | — |
| [SRC-21D5D044E2-L000026](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L26) | 26 | `"\|---\|---\|---\|---\|---\|---\|---\|"` | — |
| [SRC-21D5D044E2-L000027](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L27) | 27 | `"\| — \| — \| لا يوجد استثناء معتمد مسجل في هذا الملف حتى تاريخ اللقطة. \| — \| لا توجد موافقات مسجلة هنا \| — \| لا يثبت ذلك غياب قرار أو موافقة خارج المستودع. \|"` | — |
| [SRC-21D5D044E2-L000028](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L28) | 28 | `""` | — |
| [SRC-21D5D044E2-L000029](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L29) | 29 | `"## 3. مقترحات للمراجعة — ليست استثناءات معتمدة"` | — |
| [SRC-21D5D044E2-L000030](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L30) | 30 | `""` | — |
| [SRC-21D5D044E2-L000031](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L31) | 31 | `"### EX-PROP-001 — حصر النسخة على مشغّل واحد"` | — |
| [SRC-21D5D044E2-L000032](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L32) | 32 | `""` | — |
| [SRC-21D5D044E2-L000033](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L33) | 33 | ``"- **المتطلبات:** `IDN-001` و`IDN-003` ومتطلبات تعدد المستأجرين المشروطة."`` | — |
| [SRC-21D5D044E2-L000034](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L34) | 34 | `"- **المقترح:** تحديد نطاق النسخة التجريبية على أنها خدمة خاصة بمشغّل واحد بدل تقديمها كمنصة متعددة المستخدمين."` | — |
| [SRC-21D5D044E2-L000035](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L35) | 35 | `"- **السبب:** التنفيذ الحالي يستخدم رمز Bearer مشتركًا ومخزن leads مشتركًا؛ لا تظهر هوية فردية أو عزل كامل لبيانات كل مستخدم."` | — |
| [SRC-21D5D044E2-L000036](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L36) | 36 | `"- **المخاطر:** من يحصل على الرمز يحصل على الصلاحيات الممنوحة له؛ قد تختلط بيانات عدة مستخدمين إذا استُخدم النظام على نحو غير مقصود."` | — |
| [SRC-21D5D044E2-L000037](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L37) | 37 | `"- **التعويضات المطلوبة إذا وافق المدير:** إبقاء الخدمة خاصة، استخدام رمز قوي وسري، عدم مشاركة الرمز كأنه حساب مستقل، وعدم إدخال بيانات عملاء مستقلين أو بيانات حساسة."` | — |
| [SRC-21D5D044E2-L000038](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L38) | 38 | `"- **صاحب القرار:** مدير المشروع البشري."` | — |
| [SRC-21D5D044E2-L000039](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L39) | 39 | `"- **الانتهاء/إعادة النظر:** قبل أي عرض عام لعدة مستخدمين، أو تخزين بيانات مستقلة لجهات مختلفة."` | — |
| [SRC-21D5D044E2-L000040](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L40) | 40 | ``"- **الحالة:** `PROPOSED — تنتظر الموافقة`."`` | — |
| [SRC-21D5D044E2-L000041](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L41) | 41 | `""` | — |
| [SRC-21D5D044E2-L000042](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L42) | 42 | `"### EX-PROP-002 — استمرارية البيانات في بيئة تجريبية قابلة للفقد"` | — |
| [SRC-21D5D044E2-L000043](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L43) | 43 | `""` | — |
| [SRC-21D5D044E2-L000044](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L44) | 44 | ``"- **المتطلبات:** `REL-005` و`EXT-002` و`DAT-002` بحسب انطباقها على البيانات المخزنة."`` | — |
| [SRC-21D5D044E2-L000045](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L45) | 45 | `"- **المقترح:** السماح بتجربة لا تعتمد على حفظ بيانات مهمة فقط إذا كانت كل بياناتها اصطناعية أو قابلة لإعادة الإنشاء، مع إبقاء النسخ والاستعادة الدائمة خارج نطاق هذه التجربة."` | — |
| [SRC-21D5D044E2-L000046](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L46) | 46 | `"- **السبب:** النسخ الاحتياطي والاستعادة ودوام تخزين SQLite على مضيف محدد لم تثبت هنا."` | — |
| [SRC-21D5D044E2-L000047](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L47) | 47 | `"- **المخاطر:** فقدان البيانات بعد إعادة إنشاء الحاوية أو تغيير المضيف أو تلف ملف قاعدة البيانات."` | — |
| [SRC-21D5D044E2-L000048](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L48) | 48 | `"- **التعويضات المطلوبة إذا وافق المدير:** عدم إدخال بيانات لا يمكن تعويضها، والتصريح بأن الاستمرارية غير مثبتة."` | — |
| [SRC-21D5D044E2-L000049](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L49) | 49 | `"- **صاحب القرار:** مدير المشروع البشري."` | — |
| [SRC-21D5D044E2-L000050](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L50) | 50 | `"- **الانتهاء/إعادة النظر:** قبل تخزين أي بيانات عمل حقيقية يُعتمد عليها."` | — |
| [SRC-21D5D044E2-L000051](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L51) | 51 | ``"- **الحالة:** `PROPOSED — تنتظر الموافقة`."`` | — |
| [SRC-21D5D044E2-L000052](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L52) | 52 | `""` | — |
| [SRC-21D5D044E2-L000053](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L53) | 53 | `"### EX-PROP-003 — عدم إعلان سعة/توافر غير مقاس"` | — |
| [SRC-21D5D044E2-L000054](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L54) | 54 | `""` | — |
| [SRC-21D5D044E2-L000055](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L55) | 55 | ``"- **المتطلبات:** `PER-004` و`REL-006`، وأي ادعاء أداء أو توافر في `PRD-001`."`` | — |
| [SRC-21D5D044E2-L000056](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L56) | 56 | `"- **المقترح:** عدم نشر أرقام عن throughput أو عدد مستخدمين مدعوم أو نسبة توافر، إلى أن تتوفر قياسات ممثلة."` | — |
| [SRC-21D5D044E2-L000057](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L57) | 57 | `"- **الطبيعة:** هذا في الأساس قيد على الادعاءات، وليس إذنًا بتجاهل ضوابط الأمان أو حدود الموارد."` | — |
| [SRC-21D5D044E2-L000058](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L58) | 58 | `"- **المخاطر:** توقعات غير واقعية من المستخدمين أو توقف الخدمة تحت ضغط لم يُختبر."` | — |
| [SRC-21D5D044E2-L000059](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L59) | 59 | `"- **التعويض:** الإفصاح أن السعة والتوافر غير معروفين، وعدم إعطاء وعود تشغيلية رقمية."` | — |
| [SRC-21D5D044E2-L000060](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L60) | 60 | `"- **صاحب القرار:** مدير المشروع البشري."` | — |
| [SRC-21D5D044E2-L000061](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L61) | 61 | `"- **الانتهاء/إعادة النظر:** عند إجراء اختبار حمل موثق أو تقديم التزام تشغيلي."` | — |
| [SRC-21D5D044E2-L000062](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L62) | 62 | ``"- **الحالة:** `PROPOSED — تنتظر الموافقة`."`` | — |
| [SRC-21D5D044E2-L000063](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L63) | 63 | `""` | — |
| [SRC-21D5D044E2-L000064](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L64) | 64 | `"### EX-PROP-004 — الموصلات الاختيارية غير المتحققة"` | — |
| [SRC-21D5D044E2-L000065](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L65) | 65 | `""` | — |
| [SRC-21D5D044E2-L000066](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L66) | 66 | ``"- **المتطلبات:** `SRH-001` و`TST-005` و`PRD-001`."`` | — |
| [SRC-21D5D044E2-L000067](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L67) | 67 | `"- **المقترح:** عدم إعلان موصل اختياري على أنه يعمل حيًا ما لم ينجح اختبار اتصال فعلي به في بيئة محددة. يكفي توثيقه كقدرة مشروطة بتهيئة صحيحة."` | — |
| [SRC-21D5D044E2-L000068](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L68) | 68 | `"- **الطبيعة:** هذا ليس إعفاء من ضرورة الصدق؛ بل قاعدة لتحديد الادعاء المسموح."` | — |
| [SRC-21D5D044E2-L000069](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L69) | 69 | ``"- **التعويض:** عرض الحالة `NOT_RUN` أو `UNKNOWN` إلى حين إجراء الاختبار."`` | — |
| [SRC-21D5D044E2-L000070](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L70) | 70 | `"- **صاحب القرار:** مدير المشروع البشري عند اعتماد نطاق المنتج."` | — |
| [SRC-21D5D044E2-L000071](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L71) | 71 | `"- **الانتهاء/إعادة النظر:** عند تفعيل الموصل أو الإعلان عنه كقدرة متحققة."` | — |
| [SRC-21D5D044E2-L000072](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L72) | 72 | ``"- **الحالة:** `PROPOSED — تنتظر المراجعة`."`` | — |
| [SRC-21D5D044E2-L000073](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L73) | 73 | `""` | — |
| [SRC-21D5D044E2-L000074](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L74) | 74 | `"## 4. متطلبات لا يجوز اعتبارها مستثناة بهذا السجل"` | — |
| [SRC-21D5D044E2-L000075](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L75) | 75 | `""` | — |
| [SRC-21D5D044E2-L000076](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L76) | 76 | `"لا يمثل أي مقترح أعلاه موافقة على تجاوز:"` | — |
| [SRC-21D5D044E2-L000077](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L77) | 77 | `"- حماية SSRF والحدود الشبكية."` | — |
| [SRC-21D5D044E2-L000078](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L78) | 78 | `"- حماية الطلبات والمهلات الأساسية في API المعرض للإنترنت."` | — |
| [SRC-21D5D044E2-L000079](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L79) | 79 | `"- منع حقن التعليمات من تجاوز سياسة التطبيق أو تسريب الأسرار."` | — |
| [SRC-21D5D044E2-L000080](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L80) | 80 | `"- التحقق من المصادقة والتفويض الملائمين لنطاق الاستخدام."` | — |
| [SRC-21D5D044E2-L000081](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L81) | 81 | `"- الصدق في الاستشهادات وبيان عدم اليقين."` | — |
| [SRC-21D5D044E2-L000082](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L82) | 82 | `"- فحص الأسرار وحماية إعدادات CI/CD."` | — |
| [SRC-21D5D044E2-L000083](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L83) | 83 | `"- اختبار النشر الفعلي قبل الإعلان عن تشغيله."` | — |
| [SRC-21D5D044E2-L000084](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L84) | 84 | `"- اختبار النسخ والاستعادة قبل الاعتماد على بيانات لا يمكن تعويضها."` | — |
| [SRC-21D5D044E2-L000085](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L85) | 85 | `""` | — |
| [SRC-21D5D044E2-L000086](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L86) | 86 | ``"لا يستخدم `NOT APPLICABLE` بدل `UNKNOWN`، ولا يجوز ترقية `PROPOSED` إلى `WAIVED` دون موافقة صريحة قابلة للمراجعة."`` | — |
| [SRC-21D5D044E2-L000087](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L87) | 87 | `""` | — |
| [SRC-21D5D044E2-L000088](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L88) | 88 | `"## 5. سجل قرارات المدير"` | — |
| [SRC-21D5D044E2-L000089](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L89) | 89 | `""` | — |
| [SRC-21D5D044E2-L000090](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L90) | 90 | `"لم تُسجل موافقات في هذا الملف حتى تاريخ الإنشاء. تُضاف الموافقة فقط بعد صدورها صراحة، ويجب أن تتضمن معرف الاستثناء الذي وافق المدير عليه ونطاقه وشروطه. لن يُستنتج القبول من الصمت أو من اعتماد مهام التطوير."` | — |
| [SRC-21D5D044E2-L000091](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L91) | 91 | `""` | — |
| [SRC-21D5D044E2-L000092](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L92) | 92 | `"## 6. مراجعة دورية وإغلاق"` | — |
| [SRC-21D5D044E2-L000093](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L93) | 93 | `""` | — |
| [SRC-21D5D044E2-L000094](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L94) | 94 | `"عند انتهاء كل استثناء أو تغير النطاق:"` | — |
| [SRC-21D5D044E2-L000095](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L95) | 95 | `"1. أعد تشغيل اختبار القبول المناسب."` | — |
| [SRC-21D5D044E2-L000096](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L96) | 96 | `"2. سجل الدليل الجديد وربطه بالـSHA والبيئة."` | — |
| [SRC-21D5D044E2-L000097](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L97) | 97 | `"3. حدّد هل أُغلق الاستثناء أم يحتاج تجديدًا بموافقة جديدة."` | — |
| [SRC-21D5D044E2-L000098](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L98) | 98 | `"4. لا تمدد الاستثناء تلقائيًا."` | — |
| [SRC-21D5D044E2-L000099](../OMARAI_EXCEPTIONS_REGISTER_AR.md#L99) | 99 | `"5. احتفظ بسجل القرار السابق بدل محوه."` | — |
## وثائق وفهرسة

### FILE-E73001D9AC — [docs/OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E73001D9AC-L000001](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L1) | 1 | `"# Omarai — الدستور التأسيسي للهندسة والموثوقية والأمان والذكاء"` | — |
| [SRC-E73001D9AC-L000002](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L2) | 2 | `""` | — |
| [SRC-E73001D9AC-L000003](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L3) | 3 | `"**معرّف الوثيقة:** OMARAI-FOUNDATION-CHARTER-001  "` | — |
| [SRC-E73001D9AC-L000004](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L4) | 4 | `"**الإصدار:** 1.0.0  "` | — |
| [SRC-E73001D9AC-L000005](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L5) | 5 | `"**الحالة:** متطلب تأسيسي مقترح للإقرار والمراجعة؛ بعد اعتماد المالك يصبح مرجعًا حاكمًا للتطوير  "` | — |
| [SRC-E73001D9AC-L000006](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L6) | 6 | `"**النطاق:** جميع مكونات Omarai البرمجية والتشغيلية، وواجهات API، والواجهة العربية، ومحركات البحث، والنماذج، والأدوات، والبيانات، والاستضافة، وسير التطوير والاختبار  "` | — |
| [SRC-E73001D9AC-L000007](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L7) | 7 | `"**الأولوية:** مرجع تصميم وحوكمة؛ لا يثبت بمفرده أن أي قدرة نُفّذت أو اختُبرت  "` | — |
| [SRC-E73001D9AC-L000008](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L8) | 8 | `"**اللغة:** العربية هي لغة الشرح الأساسية، مع استخدام أسماء المصطلحات التقنية الإنجليزية لتوحيد التنفيذ والمراجعة"` | — |
| [SRC-E73001D9AC-L000009](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L9) | 9 | `""` | — |
| [SRC-E73001D9AC-L000010](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L10) | 10 | `"> **القاعدة العليا:** Omarai لا يدّعي قدرة غير مثبتة. كل قدرة مهمة يجب أن تقابلها آلية تنفيذ محددة واختبار قابل لإعادة التشغيل ودليل ناتج عن بيئة معروفة. الاختبارات والقياسات الفعلية مقدّمة على الأوصاف والوعود."` | — |
| [SRC-E73001D9AC-L000011](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L11) | 11 | `""` | — |
| [SRC-E73001D9AC-L000012](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L12) | 12 | `"---"` | — |
| [SRC-E73001D9AC-L000013](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L13) | 13 | `""` | — |
| [SRC-E73001D9AC-L000014](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L14) | 14 | `"> **مرجعان مكملان للمراجعات الواسعة:** تُقرأ هذه الوثيقة مع [خط الأساس الهندسي للمنصات العالمية واسعة النطاق](OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md)، وهو كتالوج المجالات والضوابط، ومع [سجل المتطلبات والتتبع والنضج وبوابات الاعتماد](OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md)، الذي يحدد معرفات المتطلبات وحالاتها والأدلة المقبولة ومراجعات التخصصات ومراحل التنفيذ. ويُستخدم [سجل المتطلبات الأساسية الأولي](OMARAI_REQUIREMENTS_REGISTER.md) كقائمة بدء للتتبع، لا كحكم على التنفيذ الحالي. لا تثبت أي وثيقة وحدها أن الضوابط نُفذت."` | — |
| [SRC-E73001D9AC-L000015](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L15) | 15 | `""` | — |
| [SRC-E73001D9AC-L000016](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L16) | 16 | `"## 0. كيف تُقرأ هذه الوثيقة؟"` | — |
| [SRC-E73001D9AC-L000017](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L17) | 17 | `""` | — |
| [SRC-E73001D9AC-L000018](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L18) | 18 | `"تستخدم الوثيقة الكلمات التالية بدقة:"` | — |
| [SRC-E73001D9AC-L000019](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L19) | 19 | `""` | — |
| [SRC-E73001D9AC-L000020](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L20) | 20 | `"- **MUST / إلزامي:** شرط لا يجوز تجاوزه في التنفيذ المستهدف أو الإصدار الذي يدّعي استيفاءه."` | — |
| [SRC-E73001D9AC-L000021](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L21) | 21 | `"- **SHOULD / مطلوب افتراضيًا:** يُطبّق ما لم يوجد سبب موثق ومراجع لاستثناء محدود."` | — |
| [SRC-E73001D9AC-L000022](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L22) | 22 | `"- **MAY / اختياري:** يُطبّق عندما يحقق قيمة مثبتة ولا يضيف مخاطر غير مقبولة."` | — |
| [SRC-E73001D9AC-L000023](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L23) | 23 | `"- **VERIFIED / متحقق:** تؤيده نتيجة فحص أو اختبار أو قياس محدد يمكن الرجوع إليه."` | — |
| [SRC-E73001D9AC-L000024](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L24) | 24 | `"- **INFERRED / مستنتج:** تفسير مرجح مبني على الأدلة المتاحة، وليس حقيقة اختبارية."` | — |
| [SRC-E73001D9AC-L000025](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L25) | 25 | `"- **PROPOSED / مقترح:** قرار تصميم أو هدف لم يُثبت تنفيذه بعد."` | — |
| [SRC-E73001D9AC-L000026](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L26) | 26 | `"- **UNKNOWN / غير معلوم:** لا تتوفر أدلة كافية للحكم."` | — |
| [SRC-E73001D9AC-L000027](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L27) | 27 | `""` | — |
| [SRC-E73001D9AC-L000028](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L28) | 28 | `"هذه الوثيقة **متطلبات مستقبلية ومعيار مراجعة**، وليست إعلانًا بأن المستودع الحالي يحققها. يجب أن يُسجّل لكل بند مهم: حالته، والدليل، والمخاطر المفتوحة، وخطة المعالجة، والمسؤول عن التحقق. لا تُحوّل كلمة PROPOSED إلى VERIFIED إلا بدليل فعلي."` | — |
