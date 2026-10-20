# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **011**
- سجلات الأسطر: **800**
- النطاق: SRC-E599346ABE-L001100 إلى SRC-E73001D9AC-L000192
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## وثائق وفهرسة

### FILE-E599346ABE — [docs/generate_index.py](../generate_index.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-E599346ABE-L001100](../generate_index.py#L1100) | 1100 | `"    documented_count = sum(symbol.documented is True for symbol in symbols)"` | — |
| [SRC-E599346ABE-L001101](../generate_index.py#L1101) | 1101 | `"    missing_count = sum(symbol.documented is False for symbol in symbols)"` | — |
| [SRC-E599346ABE-L001102](../generate_index.py#L1102) | 1102 | `"    not_applicable_count = sum(symbol.documented is None for symbol in symbols)"` | — |
| [SRC-E599346ABE-L001103](../generate_index.py#L1103) | 1103 | `"    lines = ["` | — |
| [SRC-E599346ABE-L001104](../generate_index.py#L1104) | 1104 | `"        \"# MASTER INDEX — Omarai\","` | — |
| [SRC-E599346ABE-L001105](../generate_index.py#L1105) | 1105 | `"        \"\","` | — |
| [SRC-E599346ABE-L001106](../generate_index.py#L1106) | 1106 | `"        \"<!-- هذا الملف مُولَّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->\","` | — |
| [SRC-E599346ABE-L001107](../generate_index.py#L1107) | 1107 | `"        \"\","` | — |
| [SRC-E599346ABE-L001108](../generate_index.py#L1108) | 1108 | `"        \"> MASTER INDEX يجمع جرد الملفات والتعريفات المسماة ووسوم المراجعة؛ SOURCE LINES INDEX يحتوي الأسطر الكاملة\","` | — |
| [SRC-E599346ABE-L001109](../generate_index.py#L1109) | 1109 | `"        \"> لكل ملف نصي مؤهل قابل للقراءة، مع معرّف سطر ورقم السطر الأصلي.\","` | — |
| [SRC-E599346ABE-L001110](../generate_index.py#L1110) | 1110 | `"        \"> استخراج الرموز غير Python تقريبي؛ أما فهرسة الأسطر فمخصصة للوصول إلى النص الموجود وليست حكمًا على صحته.\","` | — |
| [SRC-E599346ABE-L001111](../generate_index.py#L1111) | 1111 | `"        \"\","` | — |
| [SRC-E599346ABE-L001112](../generate_index.py#L1112) | 1112 | `"        \"## ملخص الفهرسة\","` | — |
| [SRC-E599346ABE-L001113](../generate_index.py#L1113) | 1113 | `"        \"\","` | — |
| [SRC-E599346ABE-L001114](../generate_index.py#L1114) | 1114 | `"        f\"- ملفات المستودع في الجرد: **{len(file_inventory)}**\","` | — |
| [SRC-E599346ABE-L001115](../generate_index.py#L1115) | 1115 | `"        f\"- ملفات Python المحللة: **{files_scanned}**\","` | — |
| [SRC-E599346ABE-L001116](../generate_index.py#L1116) | 1116 | `"        f\"- تعريفات Python المفهرسة: **{len(symbols)}**\","` | — |
| [SRC-E599346ABE-L001117](../generate_index.py#L1117) | 1117 | `"        f\"- تعريفات Python موثقة بوجود Docstring: **{documented_count}**\","` | — |
| [SRC-E599346ABE-L001118](../generate_index.py#L1118) | 1118 | `"        f\"- تعريفات Python بلا Docstring: **{missing_count}**\","` | — |
| [SRC-E599346ABE-L001119](../generate_index.py#L1119) | 1119 | `"        f\"- تعريفات لا ينطبق عليها Docstring: **{not_applicable_count}**\","` | — |
| [SRC-E599346ABE-L001120](../generate_index.py#L1120) | 1120 | `"        f\"- الرموز الساكنة الإضافية: **{len(marker_inventory)}**\","` | — |
| [SRC-E599346ABE-L001121](../generate_index.py#L1121) | 1121 | `"        f\"- الأسطر النصية المفهرسة حرفيًا: **{len(line_inventory)}**\","` | — |
| [SRC-E599346ABE-L001122](../generate_index.py#L1122) | 1122 | `"        f\"- وسوم المراجعة/الإصلاح المسجلة: **{len(finding_inventory)}**\","` | — |
| [SRC-E599346ABE-L001123](../generate_index.py#L1123) | 1123 | `"        \"\","` | — |
| [SRC-E599346ABE-L001124](../generate_index.py#L1124) | 1124 | `"        \"- فهرس الأسطر الكامل: [SOURCE LINES INDEX](SOURCE_LINES_INDEX.md)\","` | — |
| [SRC-E599346ABE-L001125](../generate_index.py#L1125) | 1125 | `"        \"- كل سجل سطر يحمل معرّفًا من الشكل SRC-<FILEHASH>-L000001.\","` | — |
| [SRC-E599346ABE-L001126](../generate_index.py#L1126) | 1126 | `"        \"\","` | — |
| [SRC-E599346ABE-L001127](../generate_index.py#L1127) | 1127 | `"        \"## جرد ملفات المستودع\","` | — |
| [SRC-E599346ABE-L001128](../generate_index.py#L1128) | 1128 | `"        \"\","` | — |
| [SRC-E599346ABE-L001129](../generate_index.py#L1129) | 1129 | `"        (\"يشمل الملفات المؤهلة من الشفرة والواجهة والاختبارات والوثائق والإعدادات وCI. \""` | — |
| [SRC-E599346ABE-L001130](../generate_index.py#L1130) | 1130 | `"        \"يُستثنى ملف الفهرس المولّد نفسه لتجنب الحلقة الذاتية، كما تُستثنى المجلدات المولّدة \""` | — |
| [SRC-E599346ABE-L001131](../generate_index.py#L1131) | 1131 | `"        \"والبيئات والملفات المحلية الحساسة وقواعد البيانات والمفاتيح المعروفة.\"),"` | — |
| [SRC-E599346ABE-L001132](../generate_index.py#L1132) | 1132 | `"        \"\","` | — |
| [SRC-E599346ABE-L001133](../generate_index.py#L1133) | 1133 | `"        \"\| معرّف الملف \| التصنيف \| الملف \| النوع \| الحجم (بايت) \| عدد الأسطر \| نطاق الفهرسة \|\","` | — |
| [SRC-E599346ABE-L001134](../generate_index.py#L1134) | 1134 | `"        \"\|---\|---\|---\|---\|---:\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001135](../generate_index.py#L1135) | 1135 | `"    ]"` | — |
| [SRC-E599346ABE-L001136](../generate_index.py#L1136) | 1136 | `""` | — |
| [SRC-E599346ABE-L001137](../generate_index.py#L1137) | 1137 | `"    if file_inventory:"` | — |
| [SRC-E599346ABE-L001138](../generate_index.py#L1138) | 1138 | `"        for item in file_inventory:"` | — |
| [SRC-E599346ABE-L001139](../generate_index.py#L1139) | 1139 | `"            line_count = str(item.line_count) if item.line_count is not None else \"غير متاح\""` | — |
| [SRC-E599346ABE-L001140](../generate_index.py#L1140) | 1140 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001141](../generate_index.py#L1141) | 1141 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001142](../generate_index.py#L1142) | 1142 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001143](../generate_index.py#L1143) | 1143 | `"                    ("` | — |
| [SRC-E599346ABE-L001144](../generate_index.py#L1144) | 1144 | `"                        item.file_id,"` | — |
| [SRC-E599346ABE-L001145](../generate_index.py#L1145) | 1145 | `"                        _markdown_cell(item.category),"` | — |
| [SRC-E599346ABE-L001146](../generate_index.py#L1146) | 1146 | `"                        f\"[{_markdown_cell(item.file)}]({_source_file_href(item.file)})\","` | — |
| [SRC-E599346ABE-L001147](../generate_index.py#L1147) | 1147 | `"                        _markdown_cell(item.file_type),"` | — |
| [SRC-E599346ABE-L001148](../generate_index.py#L1148) | 1148 | `"                        str(item.size_bytes),"` | — |
| [SRC-E599346ABE-L001149](../generate_index.py#L1149) | 1149 | `"                        line_count,"` | — |
| [SRC-E599346ABE-L001150](../generate_index.py#L1150) | 1150 | `"                        _markdown_cell(item.indexing_scope),"` | — |
| [SRC-E599346ABE-L001151](../generate_index.py#L1151) | 1151 | `"                    )"` | — |
| [SRC-E599346ABE-L001152](../generate_index.py#L1152) | 1152 | `"                )"` | — |
| [SRC-E599346ABE-L001153](../generate_index.py#L1153) | 1153 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001154](../generate_index.py#L1154) | 1154 | `"            )"` | — |
| [SRC-E599346ABE-L001155](../generate_index.py#L1155) | 1155 | `"    else:"` | — |
| [SRC-E599346ABE-L001156](../generate_index.py#L1156) | 1156 | `"        lines.append(\"\| — \| — \| — \| — \| — \| — \| لم يُمرر جرد ملفات إلى المولّد. \|\")"` | — |
| [SRC-E599346ABE-L001157](../generate_index.py#L1157) | 1157 | `""` | — |
| [SRC-E599346ABE-L001158](../generate_index.py#L1158) | 1158 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001159](../generate_index.py#L1159) | 1159 | `"        ["` | — |
| [SRC-E599346ABE-L001160](../generate_index.py#L1160) | 1160 | `"            \"\","` | — |
| [SRC-E599346ABE-L001161](../generate_index.py#L1161) | 1161 | `"            \"## تعريفات Python من AST\","` | — |
| [SRC-E599346ABE-L001162](../generate_index.py#L1162) | 1162 | `"            \"\","` | — |
| [SRC-E599346ABE-L001163](../generate_index.py#L1163) | 1163 | `"            (\"> تُحسب حالة Docstring للدوال والكلاسات فقط. المتغيرات والثوابت لا تُصنّف \""` | — |
| [SRC-E599346ABE-L001164](../generate_index.py#L1164) | 1164 | `"            \"على أنها موثقة أو ناقصة Docstring.\"),"` | — |
| [SRC-E599346ABE-L001165](../generate_index.py#L1165) | 1165 | `"            \"\","` | — |
| [SRC-E599346ABE-L001166](../generate_index.py#L1166) | 1166 | `"            \"\| الملف \| النوع \| الاسم المؤهل \| الوصف \| حالة Docstring \| السطر \| كود السطر للوصول المباشر \|\","` | — |
| [SRC-E599346ABE-L001167](../generate_index.py#L1167) | 1167 | `"            \"\|---\|---\|---\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001168](../generate_index.py#L1168) | 1168 | `"        ]"` | — |
| [SRC-E599346ABE-L001169](../generate_index.py#L1169) | 1169 | `"    )"` | — |
| [SRC-E599346ABE-L001170](../generate_index.py#L1170) | 1170 | `""` | — |
| [SRC-E599346ABE-L001171](../generate_index.py#L1171) | 1171 | `"    if not symbols:"` | — |
| [SRC-E599346ABE-L001172](../generate_index.py#L1172) | 1172 | `"        lines.append(\"\| — \| — \| — \| لا توجد تعريفات Python في الملفات المؤهلة. \| — \| — \| — \|\")"` | — |
| [SRC-E599346ABE-L001173](../generate_index.py#L1173) | 1173 | `"    else:"` | — |
| [SRC-E599346ABE-L001174](../generate_index.py#L1174) | 1174 | `"        for symbol in symbols:"` | — |
| [SRC-E599346ABE-L001175](../generate_index.py#L1175) | 1175 | `"            if symbol.documented is True:"` | — |
| [SRC-E599346ABE-L001176](../generate_index.py#L1176) | 1176 | `"                status = \"موثق\""` | — |
| [SRC-E599346ABE-L001177](../generate_index.py#L1177) | 1177 | `"            elif symbol.documented is False:"` | — |
| [SRC-E599346ABE-L001178](../generate_index.py#L1178) | 1178 | `"                status = \"ناقص\""` | — |
| [SRC-E599346ABE-L001179](../generate_index.py#L1179) | 1179 | `"            else:"` | — |
| [SRC-E599346ABE-L001180](../generate_index.py#L1180) | 1180 | `"                status = \"لا ينطبق\""` | — |
| [SRC-E599346ABE-L001181](../generate_index.py#L1181) | 1181 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001182](../generate_index.py#L1182) | 1182 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001183](../generate_index.py#L1183) | 1183 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001184](../generate_index.py#L1184) | 1184 | `"                    ("` | — |
| [SRC-E599346ABE-L001185](../generate_index.py#L1185) | 1185 | `"                        f\"[{_markdown_cell(symbol.file)}]({_source_file_href(symbol.file, symbol.line)})\","` | — |
| [SRC-E599346ABE-L001186](../generate_index.py#L1186) | 1186 | `"                        _markdown_cell(symbol.kind),"` | — |
| [SRC-E599346ABE-L001187](../generate_index.py#L1187) | 1187 | `"                        _markdown_cell(symbol.name),"` | — |
| [SRC-E599346ABE-L001188](../generate_index.py#L1188) | 1188 | `"                        _markdown_cell(symbol.description),"` | — |
| [SRC-E599346ABE-L001189](../generate_index.py#L1189) | 1189 | `"                        status,"` | — |
| [SRC-E599346ABE-L001190](../generate_index.py#L1190) | 1190 | `"                        str(symbol.line),"` | — |
| [SRC-E599346ABE-L001191](../generate_index.py#L1191) | 1191 | `"                        f\"[{_source_line_id(symbol.file, symbol.line)}]({_source_file_href(symbol.file, symbol.line)})\","` | — |
| [SRC-E599346ABE-L001192](../generate_index.py#L1192) | 1192 | `"                    )"` | — |
| [SRC-E599346ABE-L001193](../generate_index.py#L1193) | 1193 | `"                )"` | — |
| [SRC-E599346ABE-L001194](../generate_index.py#L1194) | 1194 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001195](../generate_index.py#L1195) | 1195 | `"            )"` | — |
| [SRC-E599346ABE-L001196](../generate_index.py#L1196) | 1196 | `""` | — |
| [SRC-E599346ABE-L001197](../generate_index.py#L1197) | 1197 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001198](../generate_index.py#L1198) | 1198 | `"        ["` | — |
| [SRC-E599346ABE-L001199](../generate_index.py#L1199) | 1199 | `"            \"\","` | — |
| [SRC-E599346ABE-L001200](../generate_index.py#L1200) | 1200 | `"            \"## الرموز الساكنة الإضافية\","` | — |
| [SRC-E599346ABE-L001201](../generate_index.py#L1201) | 1201 | `"            \"\","` | — |
| [SRC-E599346ABE-L001202](../generate_index.py#L1202) | 1202 | `"            (\"هذا القسم للمساعدة في الوصول إلى الواجهة والإعدادات والوثائق؛ \""` | — |
| [SRC-E599346ABE-L001203](../generate_index.py#L1203) | 1203 | `"            \"استخراج الرموز غير المحللة بـAST استدلالي وقد لا يساوي تحليلًا كاملًا للغة.\"),"` | — |
| [SRC-E599346ABE-L001204](../generate_index.py#L1204) | 1204 | `"            \"\","` | — |
| [SRC-E599346ABE-L001205](../generate_index.py#L1205) | 1205 | `"            \"\| الملف \| نوع الرمز \| الاسم/القيمة \| السطر \| كود السطر للوصول المباشر \|\","` | — |
| [SRC-E599346ABE-L001206](../generate_index.py#L1206) | 1206 | `"            \"\|---\|---\|---\|---:\|---\|\","` | — |
| [SRC-E599346ABE-L001207](../generate_index.py#L1207) | 1207 | `"        ]"` | — |
| [SRC-E599346ABE-L001208](../generate_index.py#L1208) | 1208 | `"    )"` | — |
| [SRC-E599346ABE-L001209](../generate_index.py#L1209) | 1209 | `"    if marker_inventory:"` | — |
| [SRC-E599346ABE-L001210](../generate_index.py#L1210) | 1210 | `"        for marker in marker_inventory:"` | — |
| [SRC-E599346ABE-L001211](../generate_index.py#L1211) | 1211 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001212](../generate_index.py#L1212) | 1212 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001213](../generate_index.py#L1213) | 1213 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001214](../generate_index.py#L1214) | 1214 | `"                    ("` | — |
| [SRC-E599346ABE-L001215](../generate_index.py#L1215) | 1215 | `"                        f\"[{_markdown_cell(marker.file)}]({_source_file_href(marker.file, marker.line)})\","` | — |
| [SRC-E599346ABE-L001216](../generate_index.py#L1216) | 1216 | `"                        _markdown_cell(marker.kind),"` | — |
| [SRC-E599346ABE-L001217](../generate_index.py#L1217) | 1217 | `"                        _markdown_cell(marker.name),"` | — |
| [SRC-E599346ABE-L001218](../generate_index.py#L1218) | 1218 | `"                        str(marker.line),"` | — |
| [SRC-E599346ABE-L001219](../generate_index.py#L1219) | 1219 | `"                        f\"[{_source_line_id(marker.file, marker.line)}]({_source_file_href(marker.file, marker.line)})\","` | — |
| [SRC-E599346ABE-L001220](../generate_index.py#L1220) | 1220 | `"                    )"` | — |
| [SRC-E599346ABE-L001221](../generate_index.py#L1221) | 1221 | `"                )"` | — |
| [SRC-E599346ABE-L001222](../generate_index.py#L1222) | 1222 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001223](../generate_index.py#L1223) | 1223 | `"            )"` | — |
| [SRC-E599346ABE-L001224](../generate_index.py#L1224) | 1224 | `"    else:"` | — |
| [SRC-E599346ABE-L001225](../generate_index.py#L1225) | 1225 | `"        lines.append(\"\| — \| — \| — \| لم تُكتشف رموز ساكنة إضافية. \| — \|\")"` | — |
| [SRC-E599346ABE-L001226](../generate_index.py#L1226) | 1226 | `""` | — |
| [SRC-E599346ABE-L001227](../generate_index.py#L1227) | 1227 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001228](../generate_index.py#L1228) | 1228 | `"        ["` | — |
| [SRC-E599346ABE-L001229](../generate_index.py#L1229) | 1229 | `"            \"\","` | — |
| [SRC-E599346ABE-L001230](../generate_index.py#L1230) | 1230 | `"            \"## سجل وسوم المراجعة والإصلاح\","` | — |
| [SRC-E599346ABE-L001231](../generate_index.py#L1231) | 1231 | `"            \"\","` | — |
| [SRC-E599346ABE-L001232](../generate_index.py#L1232) | 1232 | `"            \"هذه قائمة بالوسوم الصريحة التي تستدعي المتابعة. وجود الوسم ليس إثباتًا آليًا أن السطر معيب؛ افتح الملف عند رقم السطر وراجع السياق.\","` | — |
| [SRC-E599346ABE-L001233](../generate_index.py#L1233) | 1233 | `"            \"\","` | — |
| [SRC-E599346ABE-L001234](../generate_index.py#L1234) | 1234 | `"            \"\| كود الهفوة/الوسم \| النوع \| الملف \| السطر \| وصف الوسم \| كود السطر \| نص السطر \|\","` | — |
| [SRC-E599346ABE-L001235](../generate_index.py#L1235) | 1235 | `"            \"\|---\|---\|---\|---:\|---\|---\|---\|\","` | — |
| [SRC-E599346ABE-L001236](../generate_index.py#L1236) | 1236 | `"        ]"` | — |
| [SRC-E599346ABE-L001237](../generate_index.py#L1237) | 1237 | `"    )"` | — |
| [SRC-E599346ABE-L001238](../generate_index.py#L1238) | 1238 | `"    if finding_inventory:"` | — |
| [SRC-E599346ABE-L001239](../generate_index.py#L1239) | 1239 | `"        line_map = {source_line.line_id: source_line for source_line in line_inventory}"` | — |
| [SRC-E599346ABE-L001240](../generate_index.py#L1240) | 1240 | `"        for finding in finding_inventory:"` | — |
| [SRC-E599346ABE-L001241](../generate_index.py#L1241) | 1241 | `"            source_line = line_map.get(finding.line_id)"` | — |
| [SRC-E599346ABE-L001242](../generate_index.py#L1242) | 1242 | `"            lines.append("` | — |
| [SRC-E599346ABE-L001243](../generate_index.py#L1243) | 1243 | `"                \"\| \""` | — |
| [SRC-E599346ABE-L001244](../generate_index.py#L1244) | 1244 | `"                + \" \| \".join("` | — |
| [SRC-E599346ABE-L001245](../generate_index.py#L1245) | 1245 | `"                    ("` | — |
| [SRC-E599346ABE-L001246](../generate_index.py#L1246) | 1246 | `"                        finding.finding_id,"` | — |
| [SRC-E599346ABE-L001247](../generate_index.py#L1247) | 1247 | `"                        finding.marker,"` | — |
| [SRC-E599346ABE-L001248](../generate_index.py#L1248) | 1248 | `"                        f\"[{_markdown_cell(finding.file)}]({_source_file_href(finding.file, source_line.line if source_line else 1)})\","` | — |
| [SRC-E599346ABE-L001249](../generate_index.py#L1249) | 1249 | `"                        str(source_line.line if source_line else \"غير متاح\"),"` | — |
| [SRC-E599346ABE-L001250](../generate_index.py#L1250) | 1250 | `"                        _markdown_cell(finding.description),"` | — |
| [SRC-E599346ABE-L001251](../generate_index.py#L1251) | 1251 | `"                        f\"[{finding.line_id}]({_source_file_href(finding.file, source_line.line if source_line else 1)})\","` | — |
| [SRC-E599346ABE-L001252](../generate_index.py#L1252) | 1252 | `"                        _markdown_code_span(json.dumps(source_line.content, ensure_ascii=False).replace(\"\|\", r\"\\\|\")) if source_line else \"غير متاح\","` | — |
| [SRC-E599346ABE-L001253](../generate_index.py#L1253) | 1253 | `"                    )"` | — |
| [SRC-E599346ABE-L001254](../generate_index.py#L1254) | 1254 | `"                )"` | — |
| [SRC-E599346ABE-L001255](../generate_index.py#L1255) | 1255 | `"                + \" \|\""` | — |
| [SRC-E599346ABE-L001256](../generate_index.py#L1256) | 1256 | `"            )"` | — |
| [SRC-E599346ABE-L001257](../generate_index.py#L1257) | 1257 | `"    else:"` | — |
| [SRC-E599346ABE-L001258](../generate_index.py#L1258) | 1258 | `"        lines.append(\"\| — \| — \| — \| — \| لم تُكتشف وسوم صريحة من الأنواع المعروفة. \| — \| — \|\")"` | — |
| [SRC-E599346ABE-L001259](../generate_index.py#L1259) | 1259 | `""` | — |
| [SRC-E599346ABE-L001260](../generate_index.py#L1260) | 1260 | `"    lines.extend("` | — |
| [SRC-E599346ABE-L001261](../generate_index.py#L1261) | 1261 | `"        ["` | — |
| [SRC-E599346ABE-L001262](../generate_index.py#L1262) | 1262 | `"            \"\","` | — |
| [SRC-E599346ABE-L001263](../generate_index.py#L1263) | 1263 | `"            \"---\","` | — |
| [SRC-E599346ABE-L001264](../generate_index.py#L1264) | 1264 | `"            \"\","` | — |
| [SRC-E599346ABE-L001265](../generate_index.py#L1265) | 1265 | `"            \"## حدود الفهرسة\","` | — |
| [SRC-E599346ABE-L001266](../generate_index.py#L1266) | 1266 | `"            \"\","` | — |
| [SRC-E599346ABE-L001267](../generate_index.py#L1267) | 1267 | `"            \"- كل الأسطر المنطقية للملفات النصية المؤهلة القابلة للقراءة مفهرسة في SOURCE LINES INDEX، لا في هذا الجدول المختصر.\","` | — |
| [SRC-E599346ABE-L001268](../generate_index.py#L1268) | 1268 | `"            \"- الملفات الأكبر من 2 MiB أو غير القابلة للقراءة أو الثنائية تبقى ضمن الجرد الوصفي، دون فهرسة سطورها.\","` | — |
| [SRC-E599346ABE-L001269](../generate_index.py#L1269) | 1269 | `"            \"- لا تُفحص محتويات البيئة الافتراضية والاعتماديات والمجلدات المولدة.\","` | — |
| [SRC-E599346ABE-L001270](../generate_index.py#L1270) | 1270 | `"            \"- لا تُقرأ ملفات البيئة المحلية وقواعد البيانات والمفاتيح المعروفة.\","` | — |
| [SRC-E599346ABE-L001271](../generate_index.py#L1271) | 1271 | `"            \"- تحليل Python يرفض إنشاء فهرس جزئي عند وجود خطأ نحوي في أي ملف Python مؤهل.\","` | — |
| [SRC-E599346ABE-L001272](../generate_index.py#L1272) | 1272 | `"            (\"- يُحدّث هذا الفهرس آليًا عبر GitHub Actions عند دفع تغيير إلى main؛ \""` | — |
| [SRC-E599346ABE-L001273](../generate_index.py#L1273) | 1273 | `"            \"وتظل تغييرات المصدر قيد المراجعة حتى تُدمج وفق سياسة المستودع.\"),"` | — |
| [SRC-E599346ABE-L001274](../generate_index.py#L1274) | 1274 | `"            \"\","` | — |
| [SRC-E599346ABE-L001275](../generate_index.py#L1275) | 1275 | `"        ]"` | — |
| [SRC-E599346ABE-L001276](../generate_index.py#L1276) | 1276 | `"    )"` | — |
| [SRC-E599346ABE-L001277](../generate_index.py#L1277) | 1277 | `"    return \"\\n\".join(lines)"` | — |
| [SRC-E599346ABE-L001278](../generate_index.py#L1278) | 1278 | `""` | — |
| [SRC-E599346ABE-L001279](../generate_index.py#L1279) | 1279 | `""` | — |
| [SRC-E599346ABE-L001280](../generate_index.py#L1280) | 1280 | `"def write_if_changed(output_path: Path, content: str) -> bool:"` | — |
| [SRC-E599346ABE-L001281](../generate_index.py#L1281) | 1281 | `"    \"\"\"Write atomically only when the generated index differs from the existing file.\"\"\""` | — |
| [SRC-E599346ABE-L001282](../generate_index.py#L1282) | 1282 | `"    output_path.parent.mkdir(parents=True, exist_ok=True)"` | — |
| [SRC-E599346ABE-L001283](../generate_index.py#L1283) | 1283 | `"    try:"` | — |
| [SRC-E599346ABE-L001284](../generate_index.py#L1284) | 1284 | `"        if output_path.read_text(encoding=\"utf-8\") == content:"` | — |
| [SRC-E599346ABE-L001285](../generate_index.py#L1285) | 1285 | `"            return False"` | — |
| [SRC-E599346ABE-L001286](../generate_index.py#L1286) | 1286 | `"    except FileNotFoundError:"` | — |
| [SRC-E599346ABE-L001287](../generate_index.py#L1287) | 1287 | `"        pass"` | — |
| [SRC-E599346ABE-L001288](../generate_index.py#L1288) | 1288 | `""` | — |
| [SRC-E599346ABE-L001289](../generate_index.py#L1289) | 1289 | `"    temporary_path: Path \| None = None"` | — |
| [SRC-E599346ABE-L001290](../generate_index.py#L1290) | 1290 | `"    try:"` | — |
| [SRC-E599346ABE-L001291](../generate_index.py#L1291) | 1291 | `"        with tempfile.NamedTemporaryFile("` | — |
| [SRC-E599346ABE-L001292](../generate_index.py#L1292) | 1292 | `"            mode=\"w\","` | — |
| [SRC-E599346ABE-L001293](../generate_index.py#L1293) | 1293 | `"            encoding=\"utf-8\","` | — |
| [SRC-E599346ABE-L001294](../generate_index.py#L1294) | 1294 | `"            newline=\"\\n\","` | — |
| [SRC-E599346ABE-L001295](../generate_index.py#L1295) | 1295 | `"            dir=output_path.parent,"` | — |
| [SRC-E599346ABE-L001296](../generate_index.py#L1296) | 1296 | `"            prefix=f\".{output_path.name}.\","` | — |
| [SRC-E599346ABE-L001297](../generate_index.py#L1297) | 1297 | `"            suffix=\".tmp\","` | — |
| [SRC-E599346ABE-L001298](../generate_index.py#L1298) | 1298 | `"            delete=False,"` | — |
| [SRC-E599346ABE-L001299](../generate_index.py#L1299) | 1299 | `"        ) as temporary_file:"` | — |
| [SRC-E599346ABE-L001300](../generate_index.py#L1300) | 1300 | `"            temporary_file.write(content)"` | — |
| [SRC-E599346ABE-L001301](../generate_index.py#L1301) | 1301 | `"            temporary_path = Path(temporary_file.name)"` | — |
| [SRC-E599346ABE-L001302](../generate_index.py#L1302) | 1302 | `"        temporary_path.replace(output_path)"` | — |
| [SRC-E599346ABE-L001303](../generate_index.py#L1303) | 1303 | `"    finally:"` | — |
| [SRC-E599346ABE-L001304](../generate_index.py#L1304) | 1304 | `"        if temporary_path is not None and temporary_path.exists():"` | — |
| [SRC-E599346ABE-L001305](../generate_index.py#L1305) | 1305 | `"            temporary_path.unlink()"` | — |
| [SRC-E599346ABE-L001306](../generate_index.py#L1306) | 1306 | `"    return True"` | — |
| [SRC-E599346ABE-L001307](../generate_index.py#L1307) | 1307 | `""` | — |
| [SRC-E599346ABE-L001308](../generate_index.py#L1308) | 1308 | `""` | — |
| [SRC-E599346ABE-L001309](../generate_index.py#L1309) | 1309 | `"def _generate("` | — |
| [SRC-E599346ABE-L001310](../generate_index.py#L1310) | 1310 | `"    root: Path,"` | — |
| [SRC-E599346ABE-L001311](../generate_index.py#L1311) | 1311 | `") -> tuple[str, str, dict[str, str], int, int, int, int, int, int, int]:"` | — |
| [SRC-E599346ABE-L001312](../generate_index.py#L1312) | 1312 | `"    \"\"\"Create deterministic overview, source-line pages, and all counts without writing.\"\"\""` | — |
| [SRC-E599346ABE-L001313](../generate_index.py#L1313) | 1313 | `"    inventory = build_file_inventory(root)"` | — |
| [SRC-E599346ABE-L001314](../generate_index.py#L1314) | 1314 | `"    symbols, python_file_count = scan_repository(root)"` | — |
| [SRC-E599346ABE-L001315](../generate_index.py#L1315) | 1315 | `"    static_symbols = scan_static_symbols(root, inventory)"` | — |
| [SRC-E599346ABE-L001316](../generate_index.py#L1316) | 1316 | `"    source_lines = scan_source_lines(root, inventory)"` | — |
| [SRC-E599346ABE-L001317](../generate_index.py#L1317) | 1317 | `"    findings = scan_finding_annotations(source_lines)"` | — |
| [SRC-E599346ABE-L001318](../generate_index.py#L1318) | 1318 | `"    source_pages, pages_by_file = render_source_line_pages("` | — |
| [SRC-E599346ABE-L001319](../generate_index.py#L1319) | 1319 | `"        source_lines, inventory, findings"` | — |
| [SRC-E599346ABE-L001320](../generate_index.py#L1320) | 1320 | `"    )"` | — |
| [SRC-E599346ABE-L001321](../generate_index.py#L1321) | 1321 | `"    markdown = render_markdown("` | — |
| [SRC-E599346ABE-L001322](../generate_index.py#L1322) | 1322 | `"        symbols, python_file_count, inventory, static_symbols, source_lines, findings"` | — |
| [SRC-E599346ABE-L001323](../generate_index.py#L1323) | 1323 | `"    )"` | — |
| [SRC-E599346ABE-L001324](../generate_index.py#L1324) | 1324 | `"    source_lines_markdown = render_source_lines_markdown("` | — |
| [SRC-E599346ABE-L001325](../generate_index.py#L1325) | 1325 | `"        source_lines, inventory, findings, pages_by_file, source_pages"` | — |
| [SRC-E599346ABE-L001326](../generate_index.py#L1326) | 1326 | `"    )"` | — |
| [SRC-E599346ABE-L001327](../generate_index.py#L1327) | 1327 | `"    return ("` | — |
| [SRC-E599346ABE-L001328](../generate_index.py#L1328) | 1328 | `"        markdown,"` | — |
| [SRC-E599346ABE-L001329](../generate_index.py#L1329) | 1329 | `"        source_lines_markdown,"` | — |
| [SRC-E599346ABE-L001330](../generate_index.py#L1330) | 1330 | `"        source_pages,"` | — |
| [SRC-E599346ABE-L001331](../generate_index.py#L1331) | 1331 | `"        python_file_count,"` | — |
| [SRC-E599346ABE-L001332](../generate_index.py#L1332) | 1332 | `"        len(inventory),"` | — |
| [SRC-E599346ABE-L001333](../generate_index.py#L1333) | 1333 | `"        len(symbols),"` | — |
| [SRC-E599346ABE-L001334](../generate_index.py#L1334) | 1334 | `"        len(source_lines),"` | — |
| [SRC-E599346ABE-L001335](../generate_index.py#L1335) | 1335 | `"        len(findings),"` | — |
| [SRC-E599346ABE-L001336](../generate_index.py#L1336) | 1336 | `"        sum(symbol.documented is True for symbol in symbols),"` | — |
| [SRC-E599346ABE-L001337](../generate_index.py#L1337) | 1337 | `"        sum(symbol.documented is False for symbol in symbols),"` | — |
| [SRC-E599346ABE-L001338](../generate_index.py#L1338) | 1338 | `"    )"` | — |
| [SRC-E599346ABE-L001339](../generate_index.py#L1339) | 1339 | `""` | — |
| [SRC-E599346ABE-L001340](../generate_index.py#L1340) | 1340 | `""` | — |
| [SRC-E599346ABE-L001341](../generate_index.py#L1341) | 1341 | `"def main(argv: Sequence[str] \| None = None) -> int:"` | — |
| [SRC-E599346ABE-L001342](../generate_index.py#L1342) | 1342 | `"    \"\"\"Generate the living repository index or check that the committed copy is current.\"\"\""` | — |
| [SRC-E599346ABE-L001343](../generate_index.py#L1343) | 1343 | `"    parser = argparse.ArgumentParser("` | — |
| [SRC-E599346ABE-L001344](../generate_index.py#L1344) | 1344 | `"        description=\"إنشاء/فحص فهرس مستودع Omarai وملفات الشفرة والرموز الساكنة.\""` | — |
| [SRC-E599346ABE-L001345](../generate_index.py#L1345) | 1345 | `"    )"` | — |
| [SRC-E599346ABE-L001346](../generate_index.py#L1346) | 1346 | `"    parser.add_argument("` | — |
| [SRC-E599346ABE-L001347](../generate_index.py#L1347) | 1347 | `"        \"--root\","` | — |
| [SRC-E599346ABE-L001348](../generate_index.py#L1348) | 1348 | `"        type=Path,"` | — |
| [SRC-E599346ABE-L001349](../generate_index.py#L1349) | 1349 | `"        default=Path(__file__).resolve().parents[1],"` | — |
| [SRC-E599346ABE-L001350](../generate_index.py#L1350) | 1350 | `"        help=\"مسار جذر المستودع (الافتراضي: جذر مشروع Omarai).\","` | — |
| [SRC-E599346ABE-L001351](../generate_index.py#L1351) | 1351 | `"    )"` | — |
| [SRC-E599346ABE-L001352](../generate_index.py#L1352) | 1352 | `"    parser.add_argument("` | — |
| [SRC-E599346ABE-L001353](../generate_index.py#L1353) | 1353 | `"        \"--check\","` | — |
| [SRC-E599346ABE-L001354](../generate_index.py#L1354) | 1354 | `"        action=\"store_true\","` | — |
| [SRC-E599346ABE-L001355](../generate_index.py#L1355) | 1355 | `"        help=\"لا تكتب أي ملف؛ أعد حالة فشل إذا كان MASTER_INDEX.md قديمًا أو مفقودًا.\","` | — |
| [SRC-E599346ABE-L001356](../generate_index.py#L1356) | 1356 | `"    )"` | — |
| [SRC-E599346ABE-L001357](../generate_index.py#L1357) | 1357 | `"    arguments = parser.parse_args(argv)"` | — |
| [SRC-E599346ABE-L001358](../generate_index.py#L1358) | 1358 | `""` | — |
| [SRC-E599346ABE-L001359](../generate_index.py#L1359) | 1359 | `"    try:"` | — |
| [SRC-E599346ABE-L001360](../generate_index.py#L1360) | 1360 | `"        root = arguments.root.resolve(strict=True)"` | — |
| [SRC-E599346ABE-L001361](../generate_index.py#L1361) | 1361 | `"        if not root.is_dir():"` | — |
| [SRC-E599346ABE-L001362](../generate_index.py#L1362) | 1362 | `"            raise ValueError(f\"المسار المحدد ليس مجلدًا: {root}\")"` | — |
| [SRC-E599346ABE-L001363](../generate_index.py#L1363) | 1363 | `"        ("` | — |
| [SRC-E599346ABE-L001364](../generate_index.py#L1364) | 1364 | `"            markdown,"` | — |
| [SRC-E599346ABE-L001365](../generate_index.py#L1365) | 1365 | `"            source_lines_markdown,"` | — |
| [SRC-E599346ABE-L001366](../generate_index.py#L1366) | 1366 | `"            source_pages,"` | — |
| [SRC-E599346ABE-L001367](../generate_index.py#L1367) | 1367 | `"            python_file_count,"` | — |
| [SRC-E599346ABE-L001368](../generate_index.py#L1368) | 1368 | `"            repository_file_count,"` | — |
| [SRC-E599346ABE-L001369](../generate_index.py#L1369) | 1369 | `"            symbol_count,"` | — |
| [SRC-E599346ABE-L001370](../generate_index.py#L1370) | 1370 | `"            source_line_count,"` | — |
| [SRC-E599346ABE-L001371](../generate_index.py#L1371) | 1371 | `"            finding_count,"` | — |
| [SRC-E599346ABE-L001372](../generate_index.py#L1372) | 1372 | `"            documented_count,"` | — |
| [SRC-E599346ABE-L001373](../generate_index.py#L1373) | 1373 | `"            missing_count,"` | — |
| [SRC-E599346ABE-L001374](../generate_index.py#L1374) | 1374 | `"        ) = _generate(root)"` | — |
| [SRC-E599346ABE-L001375](../generate_index.py#L1375) | 1375 | `"        output_path = root / INDEX_RELATIVE_PATH"` | — |
| [SRC-E599346ABE-L001376](../generate_index.py#L1376) | 1376 | `"        source_lines_output_path = root / SOURCE_LINES_INDEX_RELATIVE_PATH"` | — |
| [SRC-E599346ABE-L001377](../generate_index.py#L1377) | 1377 | `"        generated_outputs = {"` | — |
| [SRC-E599346ABE-L001378](../generate_index.py#L1378) | 1378 | `"            INDEX_RELATIVE_PATH: markdown,"` | — |
| [SRC-E599346ABE-L001379](../generate_index.py#L1379) | 1379 | `"            SOURCE_LINES_INDEX_RELATIVE_PATH: source_lines_markdown,"` | — |
| [SRC-E599346ABE-L001380](../generate_index.py#L1380) | 1380 | `"            **source_pages,"` | — |
| [SRC-E599346ABE-L001381](../generate_index.py#L1381) | 1381 | `"        }"` | — |
| [SRC-E599346ABE-L001382](../generate_index.py#L1382) | 1382 | `""` | — |
| [SRC-E599346ABE-L001383](../generate_index.py#L1383) | 1383 | `"        if arguments.check:"` | — |
| [SRC-E599346ABE-L001384](../generate_index.py#L1384) | 1384 | `"            for relative_path, expected_content in generated_outputs.items():"` | — |
| [SRC-E599346ABE-L001385](../generate_index.py#L1385) | 1385 | `"                generated_path = root / relative_path"` | — |
| [SRC-E599346ABE-L001386](../generate_index.py#L1386) | 1386 | `"                try:"` | — |
| [SRC-E599346ABE-L001387](../generate_index.py#L1387) | 1387 | `"                    current_content = generated_path.read_text(encoding=\"utf-8\")"` | — |
| [SRC-E599346ABE-L001388](../generate_index.py#L1388) | 1388 | `"                except FileNotFoundError:"` | — |
| [SRC-E599346ABE-L001389](../generate_index.py#L1389) | 1389 | `"                    print("` | — |
| [SRC-E599346ABE-L001390](../generate_index.py#L1390) | 1390 | `"                        f\"فهرس مولّد مفقود: {generated_path}. \""` | — |
| [SRC-E599346ABE-L001391](../generate_index.py#L1391) | 1391 | `"                        \"شغّل python docs/generate_index.py.\","` | — |
| [SRC-E599346ABE-L001392](../generate_index.py#L1392) | 1392 | `"                        file=sys.stderr,"` | — |
| [SRC-E599346ABE-L001393](../generate_index.py#L1393) | 1393 | `"                    )"` | — |
| [SRC-E599346ABE-L001394](../generate_index.py#L1394) | 1394 | `"                    return 1"` | — |
| [SRC-E599346ABE-L001395](../generate_index.py#L1395) | 1395 | `"                if current_content != expected_content:"` | — |
| [SRC-E599346ABE-L001396](../generate_index.py#L1396) | 1396 | `"                    if relative_path == INDEX_RELATIVE_PATH:"` | — |
| [SRC-E599346ABE-L001397](../generate_index.py#L1397) | 1397 | `"                        message = \"الفهرس قديم (الرئيسي)\""` | — |
| [SRC-E599346ABE-L001398](../generate_index.py#L1398) | 1398 | `"                    else:"` | — |
| [SRC-E599346ABE-L001399](../generate_index.py#L1399) | 1399 | `"                        message = \"فهرس الأسطر قديم\""` | — |
| [SRC-E599346ABE-L001400](../generate_index.py#L1400) | 1400 | `"                    print("` | — |
| [SRC-E599346ABE-L001401](../generate_index.py#L1401) | 1401 | `"                        f\"{message}: {generated_path}. \""` | — |
| [SRC-E599346ABE-L001402](../generate_index.py#L1402) | 1402 | `"                        \"شغّل python docs/generate_index.py.\","` | — |
| [SRC-E599346ABE-L001403](../generate_index.py#L1403) | 1403 | `"                        file=sys.stderr,"` | — |
| [SRC-E599346ABE-L001404](../generate_index.py#L1404) | 1404 | `"                    )"` | — |
| [SRC-E599346ABE-L001405](../generate_index.py#L1405) | 1405 | `"                    return 1"` | — |
| [SRC-E599346ABE-L001406](../generate_index.py#L1406) | 1406 | `""` | — |
| [SRC-E599346ABE-L001407](../generate_index.py#L1407) | 1407 | `"            pages_directory = root / SOURCE_LINES_PAGES_DIR"` | — |
| [SRC-E599346ABE-L001408](../generate_index.py#L1408) | 1408 | `"            expected_page_names = {"` | — |
| [SRC-E599346ABE-L001409](../generate_index.py#L1409) | 1409 | `"                Path(relative_path).name"` | — |
| [SRC-E599346ABE-L001410](../generate_index.py#L1410) | 1410 | `"                for relative_path in source_pages"` | — |
| [SRC-E599346ABE-L001411](../generate_index.py#L1411) | 1411 | `"            }"` | — |
| [SRC-E599346ABE-L001412](../generate_index.py#L1412) | 1412 | `"            if pages_directory.exists():"` | — |
| [SRC-E599346ABE-L001413](../generate_index.py#L1413) | 1413 | `"                actual_page_names = {"` | — |
| [SRC-E599346ABE-L001414](../generate_index.py#L1414) | 1414 | `"                    path.name"` | — |
| [SRC-E599346ABE-L001415](../generate_index.py#L1415) | 1415 | `"                    for path in pages_directory.iterdir()"` | — |
| [SRC-E599346ABE-L001416](../generate_index.py#L1416) | 1416 | `"                    if path.is_file() and SOURCE_LINES_PAGE_RE.fullmatch(path.name)"` | — |
| [SRC-E599346ABE-L001417](../generate_index.py#L1417) | 1417 | `"                }"` | — |
| [SRC-E599346ABE-L001418](../generate_index.py#L1418) | 1418 | `"                stale_pages = actual_page_names - expected_page_names"` | — |
| [SRC-E599346ABE-L001419](../generate_index.py#L1419) | 1419 | `"                if stale_pages:"` | — |
| [SRC-E599346ABE-L001420](../generate_index.py#L1420) | 1420 | `"                    print("` | — |
| [SRC-E599346ABE-L001421](../generate_index.py#L1421) | 1421 | `"                        \"صفحات فهرس قديمة يجب حذفها بإعادة التوليد: \""` | — |
| [SRC-E599346ABE-L001422](../generate_index.py#L1422) | 1422 | `"                        + \", \".join(sorted(stale_pages)),"` | — |
| [SRC-E599346ABE-L001423](../generate_index.py#L1423) | 1423 | `"                        file=sys.stderr,"` | — |
| [SRC-E599346ABE-L001424](../generate_index.py#L1424) | 1424 | `"                    )"` | — |
| [SRC-E599346ABE-L001425](../generate_index.py#L1425) | 1425 | `"                    return 1"` | — |
| [SRC-E599346ABE-L001426](../generate_index.py#L1426) | 1426 | `"            changed = False"` | — |
| [SRC-E599346ABE-L001427](../generate_index.py#L1427) | 1427 | `"        else:"` | — |
| [SRC-E599346ABE-L001428](../generate_index.py#L1428) | 1428 | `"            changed = False"` | — |
| [SRC-E599346ABE-L001429](../generate_index.py#L1429) | 1429 | `"            for relative_path, generated_content in generated_outputs.items():"` | — |
| [SRC-E599346ABE-L001430](../generate_index.py#L1430) | 1430 | `"                if write_if_changed(root / relative_path, generated_content):"` | — |
| [SRC-E599346ABE-L001431](../generate_index.py#L1431) | 1431 | `"                    changed = True"` | — |
| [SRC-E599346ABE-L001432](../generate_index.py#L1432) | 1432 | `""` | — |
| [SRC-E599346ABE-L001433](../generate_index.py#L1433) | 1433 | `"            pages_directory = root / SOURCE_LINES_PAGES_DIR"` | — |
| [SRC-E599346ABE-L001434](../generate_index.py#L1434) | 1434 | `"            if pages_directory.exists():"` | — |
| [SRC-E599346ABE-L001435](../generate_index.py#L1435) | 1435 | `"                expected_page_names = {"` | — |
| [SRC-E599346ABE-L001436](../generate_index.py#L1436) | 1436 | `"                    Path(relative_path).name"` | — |
| [SRC-E599346ABE-L001437](../generate_index.py#L1437) | 1437 | `"                    for relative_path in source_pages"` | — |
| [SRC-E599346ABE-L001438](../generate_index.py#L1438) | 1438 | `"                }"` | — |
| [SRC-E599346ABE-L001439](../generate_index.py#L1439) | 1439 | `"                for path in pages_directory.iterdir():"` | — |
| [SRC-E599346ABE-L001440](../generate_index.py#L1440) | 1440 | `"                    if ("` | — |
| [SRC-E599346ABE-L001441](../generate_index.py#L1441) | 1441 | `"                        path.is_file()"` | — |
| [SRC-E599346ABE-L001442](../generate_index.py#L1442) | 1442 | `"                        and SOURCE_LINES_PAGE_RE.fullmatch(path.name)"` | — |
| [SRC-E599346ABE-L001443](../generate_index.py#L1443) | 1443 | `"                        and path.name not in expected_page_names"` | — |
| [SRC-E599346ABE-L001444](../generate_index.py#L1444) | 1444 | `"                    ):"` | — |
| [SRC-E599346ABE-L001445](../generate_index.py#L1445) | 1445 | `"                        path.unlink()"` | — |
| [SRC-E599346ABE-L001446](../generate_index.py#L1446) | 1446 | `"                        changed = True"` | — |
| [SRC-E599346ABE-L001447](../generate_index.py#L1447) | 1447 | `"    except (IndexGenerationError, OSError, ValueError) as exc:"` | — |
| [SRC-E599346ABE-L001448](../generate_index.py#L1448) | 1448 | `"        print(f\"خطأ في إنشاء فهرس Omarai: {exc}\", file=sys.stderr)"` | — |
| [SRC-E599346ABE-L001449](../generate_index.py#L1449) | 1449 | `"        return 1"` | — |
| [SRC-E599346ABE-L001450](../generate_index.py#L1450) | 1450 | `""` | — |
| [SRC-E599346ABE-L001451](../generate_index.py#L1451) | 1451 | `"    if arguments.check:"` | — |
| [SRC-E599346ABE-L001452](../generate_index.py#L1452) | 1452 | `"        action = \"الفهرس محدث والتحقق ناجح\""` | — |
| [SRC-E599346ABE-L001453](../generate_index.py#L1453) | 1453 | `"    else:"` | — |
| [SRC-E599346ABE-L001454](../generate_index.py#L1454) | 1454 | `"        action = \"تم تحديث\" if changed else \"الفهرس محدث بالفعل\""` | — |
| [SRC-E599346ABE-L001455](../generate_index.py#L1455) | 1455 | `"    print("` | — |
| [SRC-E599346ABE-L001456](../generate_index.py#L1456) | 1456 | `"        f\"{action}: {output_path} \| \""` | — |
| [SRC-E599346ABE-L001457](../generate_index.py#L1457) | 1457 | `"        f\"ملفات المستودع: {repository_file_count} \| \""` | — |
| [SRC-E599346ABE-L001458](../generate_index.py#L1458) | 1458 | `"        f\"ملفات Python: {python_file_count} \| \""` | — |
| [SRC-E599346ABE-L001459](../generate_index.py#L1459) | 1459 | `"        f\"تعريفات Python: {symbol_count} \| \""` | — |
| [SRC-E599346ABE-L001460](../generate_index.py#L1460) | 1460 | `"        f\"أسطر مفهرسة: {source_line_count} \| \""` | — |
| [SRC-E599346ABE-L001461](../generate_index.py#L1461) | 1461 | `"        f\"صفحات أسطر: {len(source_pages)} \| \""` | — |
| [SRC-E599346ABE-L001462](../generate_index.py#L1462) | 1462 | `"        f\"وسوم مراجعة: {finding_count} \| \""` | — |
| [SRC-E599346ABE-L001463](../generate_index.py#L1463) | 1463 | `"        f\"موثق: {documented_count} \| \""` | — |
| [SRC-E599346ABE-L001464](../generate_index.py#L1464) | 1464 | `"        f\"ناقص Docstring: {missing_count}\""` | — |
| [SRC-E599346ABE-L001465](../generate_index.py#L1465) | 1465 | `"    )"` | — |
| [SRC-E599346ABE-L001466](../generate_index.py#L1466) | 1466 | `"    return 0"` | — |
| [SRC-E599346ABE-L001467](../generate_index.py#L1467) | 1467 | `""` | — |
| [SRC-E599346ABE-L001468](../generate_index.py#L1468) | 1468 | `""` | — |
| [SRC-E599346ABE-L001469](../generate_index.py#L1469) | 1469 | `"if __name__ == \"__main__\":"` | — |
| [SRC-E599346ABE-L001470](../generate_index.py#L1470) | 1470 | `"    raise SystemExit(main())"` | — |
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

### FILE-401D6AACE1 — [docs/INDEXING_AND_FINDINGS_GUIDE_AR.md](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L1)

- النوع: **Markdown**
- نطاق الفهرسة: جرد الملف + عناوين Markdown

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-401D6AACE1-L000001](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L1) | 1 | `"# دليل فهرسة Omarai وسجل الهفوات"` | — |
| [SRC-401D6AACE1-L000002](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L2) | 2 | `""` | — |
| [SRC-401D6AACE1-L000003](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L3) | 3 | `"**المعرف:** OMARAI-INDEX-GUIDE-001  "` | — |
| [SRC-401D6AACE1-L000004](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L4) | 4 | `"**الحالة:** طريقة تشغيل ومراجعة؛ لا تعني اكتمال الفهرسة قبل نجاح الفحص على النسخة الحالية."` | — |
| [SRC-401D6AACE1-L000005](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L5) | 5 | `""` | — |
| [SRC-401D6AACE1-L000006](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L6) | 6 | `"## 1. أين أبدأ؟"` | — |
| [SRC-401D6AACE1-L000007](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L7) | 7 | `""` | — |
| [SRC-401D6AACE1-L000008](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L8) | 8 | ``"- `docs/MASTER_INDEX.md`: جرد الملفات وتعريفات Python ورموز واجهة الويب والإعدادات والعناوين."`` | — |
| [SRC-401D6AACE1-L000009](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L9) | 9 | ``"- `docs/SOURCE_LINES_INDEX.md`: دليل إلى صفحات الأسطر."`` | — |
| [SRC-401D6AACE1-L000010](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L10) | 10 | ``"- `docs/source_index/SOURCE_LINES_*.md`: أسطر الملفات النصية المؤهلة، مع معرف ثابت للسطر ورابط إلى موضع المصدر."`` | — |
| [SRC-401D6AACE1-L000011](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L11) | 11 | ``"- `docs/search_code.py`: بحث نصي محلي يعمل من دون API أو خدمة خارجية، ويعرض اسم الملف ورقم السطر والرابط."`` | — |
| [SRC-401D6AACE1-L000012](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L12) | 12 | ``"- `docs/OMARAI_REQUIREMENTS_REGISTER.md`: سجل المتطلبات؛ يجب ربط نتيجة التدقيق بمعرف متطلب مناسب عندما ينطبق."`` | — |
| [SRC-401D6AACE1-L000013](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L13) | 13 | `""` | — |
| [SRC-401D6AACE1-L000014](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L14) | 14 | `"الفهرس وسيلة ملاحة، وليس بديلًا لقراءة الملف الفعلي أو الاختبار. قد تتغير أرقام الأسطر عند التعديل؛ أعد التوليد والفحص بعد كل تغيير مؤثر."` | — |
| [SRC-401D6AACE1-L000015](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L15) | 15 | `""` | — |
| [SRC-401D6AACE1-L000016](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L16) | 16 | `"## 2. البحث من الكمبيوتر أو Termux"` | — |
| [SRC-401D6AACE1-L000017](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L17) | 17 | `""` | — |
| [SRC-401D6AACE1-L000018](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L18) | 18 | `"من جذر المستودع:"` | — |
| [SRC-401D6AACE1-L000019](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L19) | 19 | `""` | — |
| [SRC-401D6AACE1-L000020](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L20) | 20 | ````"```bash"```` | — |
| [SRC-401D6AACE1-L000021](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L21) | 21 | `"python docs/search_code.py \"Handler._allowed_origins\""` | — |
| [SRC-401D6AACE1-L000022](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L22) | 22 | `"python docs/search_code.py \"X-Forwarded-Host\" --context 2"` | — |
| [SRC-401D6AACE1-L000023](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L23) | 23 | `"python docs/search_code.py --regex \"OMARAI_[A-Z_]+\" --ext py"` | — |
| [SRC-401D6AACE1-L000024](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L24) | 24 | `"python docs/generate_index.py"` | — |
| [SRC-401D6AACE1-L000025](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L25) | 25 | `"python docs/generate_index.py --check"` | — |
| [SRC-401D6AACE1-L000026](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L26) | 26 | ````"```"```` | — |
| [SRC-401D6AACE1-L000027](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L27) | 27 | `""` | — |
| [SRC-401D6AACE1-L000028](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L28) | 28 | `"لا يحتاج البحث النصي إلى مفتاح نموذج أو اتصال بالإنترنت. يتطلب تشغيل الأوامر وجود Python، ويفضل Python 3.11 أو 3.12 لمطابقة مصفوفة CI."` | — |
| [SRC-401D6AACE1-L000029](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L29) | 29 | `""` | — |
| [SRC-401D6AACE1-L000030](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L30) | 30 | `"## 3. كيف نسجل الهفوات المعروفة؟"` | — |
| [SRC-401D6AACE1-L000031](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L31) | 31 | `""` | — |
| [SRC-401D6AACE1-L000032](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L32) | 32 | `"إذا رُصدت مشكلة قابلة للتتبع، اكتب وسمًا واضحًا في تعليق قريب من موضعها، مثل:"` | — |
| [SRC-401D6AACE1-L000033](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L33) | 33 | `""` | — |
| [SRC-401D6AACE1-L000034](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L34) | 34 | ````"```python"```` | — |
| [SRC-401D6AACE1-L000035](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L35) | 35 | `"# TODO: DOC-INDEX-001 — توثيق الحالة المتبقية وخطوة إغلاقها."` | FND-TODO-401D6AACE1-L000035 |
| [SRC-401D6AACE1-L000036](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L36) | 36 | `"# FIXME: SEC-001 — وصف قصير للمشكلة المثبتة والاختبار المطلوب."` | FND-FIXME-401D6AACE1-L000036 |
| [SRC-401D6AACE1-L000037](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L37) | 37 | `"# REVIEW: EVD-001 — مراجعة دليل الاستشهاد قبل اعتماد هذا المسار."` | FND-REVIEW-401D6AACE1-L000037 |
| [SRC-401D6AACE1-L000038](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L38) | 38 | ````"```"```` | — |
| [SRC-401D6AACE1-L000039](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L39) | 39 | `""` | — |
| [SRC-401D6AACE1-L000040](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L40) | 40 | ``"تدعم أداة الفهرسة وسومًا صريحة مثل `TODO`, `FIXME`, `BUG`, `HACK`, `XXX`, `REVIEW`, `SECURITY`, و`DEPRECATED` عندما يتبع الوسم وصف. تنشئ الأداة معرف `FND-...` ورابطًا للسطر، وتعرضه في الفهرس الرئيسي. استخدم معرف متطلب موجودًا مثل `SEC-002` أو `API-001` عند انطباقه؛ لا تنشئ معرفًا متعارضًا ولا تعِد استخدام معرف ملغى."`` | — |
| [SRC-401D6AACE1-L000041](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L41) | 41 | `""` | — |
| [SRC-401D6AACE1-L000042](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L42) | 42 | ``"لا تضف وسمًا لمجرد التخمين. صنّف النتيجة `VERIFIED`, `INFERRED`, `PROPOSED`, أو `UNKNOWN`، وحدد الشدة والملف/السطر والأثر والاختبار والقيود في تقرير المراجعة. الوسوم لا تُكتشف إلا إذا كُتبت؛ غيابها لا يثبت غياب العيوب، والفهرسة لا تكتشف كل أخطاء المنطق تلقائيًا."`` | — |
| [SRC-401D6AACE1-L000043](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L43) | 43 | `""` | — |
| [SRC-401D6AACE1-L000044](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L44) | 44 | `"## 4. ما الذي يدخل الفهرس وما حدوده؟"` | — |
| [SRC-401D6AACE1-L000045](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L45) | 45 | `""` | — |
| [SRC-401D6AACE1-L000046](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L46) | 46 | `"الجرد يشمل ملفات المستودع التي يستطيع المولد قراءتها، مع حدود حجم، واستثناء للمجلدات المولدة والملفات الثنائية وقواعد البيانات وامتدادات المفاتيح وملفات الاعتماد الحساسة المعروفة. صفحات الأسطر تتضمن المحتوى المؤهل فقط، وليس الملفات التي استُثنيت أو تجاوزت الحد. هذه القائمة الوقائية ليست ماسح أسرار شاملًا؛ لا تضف أسرارًا إلى المستودع أصلًا، وشغّل فحص الأسرار المناسب قبل النشر."` | — |
| [SRC-401D6AACE1-L000047](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L47) | 47 | `""` | — |
| [SRC-401D6AACE1-L000048](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L48) | 48 | `"تستخدم بعض لغات الواجهة قواعد ساكنة تقريبية، وليست محللات كاملة؛ لذلك قد تُفوّت رموزًا أو تُدرج تطابقات ليست تعريفات. أسطر المصدر وروابط GitHub أدوات للوصول، وليست ضمانًا أن وصفًا أو متطلبًا صحيح."` | — |
| [SRC-401D6AACE1-L000049](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L49) | 49 | `""` | — |
| [SRC-401D6AACE1-L000050](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L50) | 50 | `"## 5. سياسة التحديث والموافقة"` | — |
| [SRC-401D6AACE1-L000051](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L51) | 51 | `""` | — |
| [SRC-401D6AACE1-L000052](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L52) | 52 | `"- لا تعدّل الملفات المولدة يدويًا؛ عدّل المصدر/المولد ثم أعد التوليد."` | — |
| [SRC-401D6AACE1-L000053](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L53) | 53 | ``"- يجب أن ينجح `python docs/generate_index.py --check` بعد التوليد."`` | — |
| [SRC-401D6AACE1-L000054](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L54) | 54 | `"- تغييرات فروع المراجعة يمكن أن تحدّث ناتج الفهرس داخل فرعها فقط."` | — |
| [SRC-401D6AACE1-L000055](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L55) | 55 | ``"- إذا احتاج `main` إلى تحديث، ينشئ workflow فرعًا وPull Request عاديًا. لا يُسمح بدفع مباشر تلقائي إلى `main` أو دمج آلي."`` | — |
| [SRC-401D6AACE1-L000056](../INDEXING_AND_FINDINGS_GUIDE_AR.md#L56) | 56 | ``"- لا يُقال إن الفهرس شامل إلا ضمن الملفات والأنواع والحدود المذكورة؛ سجّل `UNKNOWN` لما لم يُفحص."`` | — |
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
| [SRC-E73001D9AC-L000004](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L4) | 4 | `"**الإصدار:** 1.2.0  "` | — |
| [SRC-E73001D9AC-L000005](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L5) | 5 | `"**الحالة:** متطلب تأسيسي مقترح للإقرار والمراجعة؛ بعد اعتماد المالك يصبح مرجعًا حاكمًا للتطوير  "` | — |
| [SRC-E73001D9AC-L000006](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L6) | 6 | `"**النطاق:** جميع مكونات Omarai البرمجية والتشغيلية، وواجهات API، والواجهة العربية، ومحركات البحث، والنماذج، والأدوات، والبيانات، والاستضافة، وسير التطوير والاختبار  "` | — |
| [SRC-E73001D9AC-L000007](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L7) | 7 | `"**الأولوية:** مرجع تصميم وحوكمة؛ لا يثبت بمفرده أن أي قدرة نُفّذت أو اختُبرت  "` | — |
| [SRC-E73001D9AC-L000008](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L8) | 8 | `"**اللغة:** العربية هي لغة الشرح الأساسية، مع استخدام أسماء المصطلحات التقنية الإنجليزية لتوحيد التنفيذ والمراجعة"` | — |
| [SRC-E73001D9AC-L000009](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L9) | 9 | `""` | — |
| [SRC-E73001D9AC-L000010](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L10) | 10 | `"> **القاعدة العليا:** Omarai لا يدّعي قدرة غير مثبتة. كل قدرة مهمة يجب أن تقابلها آلية تنفيذ محددة واختبار قابل لإعادة التشغيل ودليل ناتج عن بيئة معروفة. الاختبارات والقياسات الفعلية مقدّمة على الأوصاف والوعود."` | — |
| [SRC-E73001D9AC-L000011](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L11) | 11 | `""` | — |
| [SRC-E73001D9AC-L000012](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L12) | 12 | `"---"` | — |
| [SRC-E73001D9AC-L000013](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L13) | 13 | `""` | — |
| [SRC-E73001D9AC-L000014](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L14) | 14 | `"> **مراجع مكملة للمراجعات الواسعة:** تُقرأ هذه الوثيقة مع [خط الأساس الهندسي للمنصات العالمية واسعة النطاق](OMARAI_GLOBAL_PLATFORM_ENGINEERING_BASELINE_AR.md)، ومع [سجل المتطلبات والتتبع والنضج وبوابات الاعتماد](OMARAI_REQUIREMENTS_TRACEABILITY_AND_MATURITY_MODEL_AR.md)، ومع [سجل المتطلبات الأساسية الأولي](OMARAI_REQUIREMENTS_REGISTER.md). وتُقرأ أيضًا مع [المعمارية الحاكمة للقدرات والمهارات وسير العمل والوكلاء](OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md)، التي تفصل مسار التوسع من النواة إلى المهارات وسير العمل والوكلاء. هذه الوثائق مكملة بعضها لبعض وليست بدائل متنافسة؛ لا تثبت أي وثيقة وحدها أن الضوابط نُفذت."` | — |
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
| [SRC-E73001D9AC-L000029](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L29) | 29 | `""` | — |
| [SRC-E73001D9AC-L000030](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L30) | 30 | `"---"` | — |
| [SRC-E73001D9AC-L000031](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L31) | 31 | `""` | — |
| [SRC-E73001D9AC-L000032](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L32) | 32 | `"# الجزء الأول — الرسالة العليا ومبادئ التصميم"` | — |
| [SRC-E73001D9AC-L000033](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L33) | 33 | `""` | — |
| [SRC-E73001D9AC-L000034](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L34) | 34 | `"## 1. الرؤية"` | — |
| [SRC-E73001D9AC-L000035](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L35) | 35 | `""` | — |
| [SRC-E73001D9AC-L000036](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L36) | 36 | `"بناء Omarai كنواة ذكاء اصطناعي عربية عملية تستطيع استقبال الأسئلة والمهام، وفهمها، والبحث عند الحاجة، واستخدام الأدوات التي ثبت عملها، وتوليد إجابات مستندة إلى الأدلة، وإظهار حدود المعرفة بوضوح؛ مع هندسة تتيح النمو من نموذج أولي محدود إلى خدمة إنتاجية موثوقة عندما تسمح الموارد والاستضافة بذلك."` | — |
| [SRC-E73001D9AC-L000037](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L37) | 37 | `""` | — |
| [SRC-E73001D9AC-L000038](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L38) | 38 | `"الطموح هو بلوغ مستوى احترافي في الاعتمادية والأمان والكفاءة، مع الاستفادة من الممارسات الصناعية المعروفة. لا يعني ذلك ادعاء التكافؤ مع المنصات العالمية قبل وجود بنية تشغيلية وميزانية واختبارات وتدقيق خارجي مناسب."` | — |
| [SRC-E73001D9AC-L000039](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L39) | 39 | `""` | — |
| [SRC-E73001D9AC-L000040](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L40) | 40 | `"## 2. المبادئ الحاكمة غير القابلة للتفاوض"` | — |
| [SRC-E73001D9AC-L000041](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L41) | 41 | `""` | — |
| [SRC-E73001D9AC-L000042](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L42) | 42 | `"1. **Evidence over assertion:** لا نعلن نجاحًا بلا دليل."` | — |
| [SRC-E73001D9AC-L000043](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L43) | 43 | `"2. **Security by design:** الأمن جزء من التصميم ودورة التطوير، لا طبقة تجميلية لاحقة."` | — |
| [SRC-E73001D9AC-L000044](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L44) | 44 | `"3. **Reliability before feature growth:** لا نضيف قدرات تُضعف الاستقرار أو تفتح صلاحيات غير مضبوطة."` | — |
| [SRC-E73001D9AC-L000045](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L45) | 45 | `"4. **Least privilege:** أقل صلاحية لازمة لكل مستخدم ومكوّن وأداة."` | — |
| [SRC-E73001D9AC-L000046](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L46) | 46 | `"5. **Fail safely, degrade gracefully:** تعطل مكوّن لا ينبغي أن يسقط النظام كله، والفشل يجب أن يكون محدود الأثر وواضحًا."` | — |
| [SRC-E73001D9AC-L000047](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L47) | 47 | `"6. **Bound every expensive operation:** كل بحث أو استدعاء نموذج أو جلب صفحة أو حلقة تخطيط أو إعادة محاولة له حدود زمنية وكمية وتكلفة."` | — |
| [SRC-E73001D9AC-L000048](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L48) | 48 | `"7. **Simple path first:** السؤال البسيط يسلك المسار الأقصر؛ لا نستدعي التخطيط العميق أو الإنترنت بلا حاجة."` | — |
| [SRC-E73001D9AC-L000049](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L49) | 49 | `"8. **Independent verification:** لا نعتبر مراجعة النموذج لنفسه تحققًا مستقلًا، ولا نعتبر اتفاق محركات البحث إثباتًا للحقيقة."` | — |
| [SRC-E73001D9AC-L000050](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L50) | 50 | `"9. **Privacy by default:** نجمع أقل بيانات لازمة، ونوضح ما يغادر النظام إلى مزودي الخدمة."` | — |
| [SRC-E73001D9AC-L000051](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L51) | 51 | `"10. **Separation of concerns:** حدود واضحة بين الطلبات، والتخطيط، والبحث، وتنفيذ الأدوات، والتحقق، والبيانات، والمراقبة."` | — |
| [SRC-E73001D9AC-L000052](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L52) | 52 | `"11. **Observable behavior:** يجب أن يمكن قياس النجاح والفشل والبطء والاستهلاك، مع حماية الخصوصية."` | — |
| [SRC-E73001D9AC-L000053](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L53) | 53 | `"12. **Reversible decisions:** التغييرات الهندسية الكبيرة تمر عبر قرارات موثقة ويمكن التراجع عنها."` | — |
| [SRC-E73001D9AC-L000054](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L54) | 54 | `"13. **Human control for consequential actions:** لا تمنح النماذج استقلالًا مفتوحًا لإجراء تغييرات حساسة أو آثار خارجية."` | — |
| [SRC-E73001D9AC-L000055](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L55) | 55 | `"14. **No “security by obscurity”:** الحماية تعتمد على ضوابط واختبارات وصلاحيات، لا على إخفاء تفاصيل التصميم."` | — |
| [SRC-E73001D9AC-L000056](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L56) | 56 | `"15. **Cost-aware engineering:** نختار التعقيد والاعتماديات وفق منفعة مقاسة وتكلفة ومخاطر حقيقية، لا لمجرد أن المعمارية تبدو أكبر."` | — |
| [SRC-E73001D9AC-L000057](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L57) | 57 | `"16. **Arabic-first quality:** دعم العربية واتجاه RTL وجودة البحث والاستشهادات جزء من الجودة الأساسية، وليس تحسينًا ثانويًا."` | — |
| [SRC-E73001D9AC-L000058](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L58) | 58 | `"17. **No false universality:** لا نقول إن الأداة تعمل دائمًا، أو إن كل موقع قابل للاستخراج، أو إن كل سؤال يمكن الإجابة عنه يقينًا."` | — |
| [SRC-E73001D9AC-L000059](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L59) | 59 | `"18. **Owner-controlled release:** لا يتم دمج تغييرات جوهرية أو إطلاقها باعتبارها معتمدة نهائيًا دون قرار صاحب المشروع."` | — |
| [SRC-E73001D9AC-L000060](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L60) | 60 | `""` | — |
| [SRC-E73001D9AC-L000061](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L61) | 61 | `"## 3. الطموح الأقصى لا يعني تعقيدًا أقصى"` | — |
| [SRC-E73001D9AC-L000062](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L62) | 62 | `""` | — |
| [SRC-E73001D9AC-L000063](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L63) | 63 | `"يُراجع Omarai بأوسع تغطية تخصصية ممكنة، لكن لا تُنشأ طبقات تشغيلية أو خدمات مستقلة لمجرد زيادة العدد. المقصود هو **أقصى تغطية مفيدة للمخاطر والتخصصات، وأقل تعقيد تشغيلي يحققها**. يبدأ المشروع بوحدات منطقية واضحة؛ ثم تُفصل الخدمات أو تُضاف البنية الموزعة عندما تثبت اختبارات الحمل أو حدود العزل أو التوافر الحاجة إلى ذلك."` | — |
| [SRC-E73001D9AC-L000064](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L64) | 64 | `""` | — |
| [SRC-E73001D9AC-L000065](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L65) | 65 | `"### 3.1 قاعدة حاكمة لتنظيم القدرات والمهارات والوكلاء"` | — |
| [SRC-E73001D9AC-L000066](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L66) | 66 | `""` | — |
| [SRC-E73001D9AC-L000067](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L67) | 67 | `"**[PROPOSED — اعتماد بشري مطلوب]** يكون الاتجاه الافتراضي لتطور القدرات هو: نواة موثوقة ← أدوات وقدرات بعقود وصلاحيات واضحة ← مهارات قابلة لإعادة الاستخدام ← سير عمل محدود وقابل للاختبار ← سياق تنفيذ مؤقت لكل مهمة ← وكلاء يُنشؤون عند ثبوت الحاجة. ولا يُنشأ وكيل مستقل لكل سؤال أو تخصص تلقائيًا."` | — |
| [SRC-E73001D9AC-L000068](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L68) | 68 | `""` | — |
| [SRC-E73001D9AC-L000069](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L69) | 69 | `"- الأداة تنفذ عملية بعقد معلوم؛ والقدرة تحدد ما يُسمح به؛ والمهارة تجمع منطقًا قابلًا لإعادة الاستخدام؛ وسير العمل يحدد ترتيب الخطوات وشروط التوقف؛ وملف تعريف الوكيل وصفة لإعادة الاستخدام، لا برنامج حر."` | — |
| [SRC-E73001D9AC-L000070](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L70) | 70 | `"- الخطة التي يقترحها النموذج بيانات غير موثوقة حتى تُفحص بنيتها وصلاحياتها وميزانيتها؛ لا تمنح أي خطة أو مهارة أو ملف تعريف صلاحيات لنفسه."` | — |
| [SRC-E73001D9AC-L000071](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L71) | 71 | `"- يكون سياق التشغيل مؤقتًا ومعزولًا افتراضيًا. لا تُضاف ذاكرة دائمة أو وكيل دائم إلا لمطلب واضح وسياسة احتفاظ وصلاحيات واختبارات مناسبة."` | — |
| [SRC-E73001D9AC-L000072](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L72) | 72 | `"- تُفصل إدارة المسودات والتعريفات والاعتماد منطقيًا عن تشغيل المهام. لا يستطيع النموذج أو Meta-Agent اعتماد نفسه أو تعديل سقف صلاحيات المنصة."` | — |
| [SRC-E73001D9AC-L000073](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L73) | 73 | `"- لا يُنشأ Meta-Agent ولا يُسمح بتوليد كود تنفيذي في المسار الأساسي قبل إثبات الحاجة بفحوص وقياسات؛ وإذا أضيف Meta-Agent مستقبلًا، يبدأ بإنتاج مسودات تعريفية فقط، تمر بالتحقق والاختبارات والموافقة."` | — |
| [SRC-E73001D9AC-L000074](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L74) | 74 | `"- تبقى مهام البحث والأدلة والأمان والتحقق في الدستور قائمة وواجبة؛ لا يستبدل التنظيم الجديد للقدرات هذه الضوابط."` | — |
| [SRC-E73001D9AC-L000075](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L75) | 75 | `""` | — |
| [SRC-E73001D9AC-L000076](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L76) | 76 | `"التفصيل التنفيذي وبوابات الانتقال موضح في [المعمارية الحاكمة للقدرات والمهارات وسير العمل والوكلاء](OMARAI_SKILL_WORKFLOW_AGENT_ARCHITECTURE_AR.md). هذا توجيه معماري مستهدف، وليس ادعاءً بأن مكوناته كلها منفذة."` | — |
| [SRC-E73001D9AC-L000077](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L77) | 77 | `""` | — |
| [SRC-E73001D9AC-L000078](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L78) | 78 | `"---"` | — |
| [SRC-E73001D9AC-L000079](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L79) | 79 | `""` | — |
| [SRC-E73001D9AC-L000080](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L80) | 80 | `"# الجزء الثاني — حوكمة الخبراء والمراجعة متعددة التخصصات"` | — |
| [SRC-E73001D9AC-L000081](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L81) | 81 | `""` | — |
| [SRC-E73001D9AC-L000082](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L82) | 82 | `"## 4. مجالات الخبرة التي يجب تغطيتها"` | — |
| [SRC-E73001D9AC-L000083](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L83) | 83 | `""` | — |
| [SRC-E73001D9AC-L000084](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L84) | 84 | `"في القرارات المعمارية والأمنية عالية التأثير، تُراجع الآثار من زوايا التخصصات المناسبة التالية. هذه قائمة تغطية للمراجعة، وليست ادعاءً بأن مجموعة خبراء أو وكلاء آليين تعمل حاليًا داخل المستودع."` | — |
| [SRC-E73001D9AC-L000085](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L85) | 85 | `""` | — |
| [SRC-E73001D9AC-L000086](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L86) | 86 | `"1. هندسة البرمجيات والمعمارية."` | — |
| [SRC-E73001D9AC-L000087](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L87) | 87 | `"2. هندسة الأنظمة والتزامن وإدارة الموارد."` | — |
| [SRC-E73001D9AC-L000088](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L88) | 88 | `"3. SRE والاعتمادية والتعافي من الأعطال."` | — |
| [SRC-E73001D9AC-L000089](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L89) | 89 | `"4. الأمن السيبراني وهندسة التهديدات."` | — |
| [SRC-E73001D9AC-L000090](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L90) | 90 | `"5. أمن تطبيقات الويب وواجهات API."` | — |
| [SRC-E73001D9AC-L000091](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L91) | 91 | `"6. أمن تطبيقات LLM والوكلاء ومقاومة حقن التعليمات."` | — |
| [SRC-E73001D9AC-L000092](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L92) | 92 | `"7. أمن الشبكات والـ DNS وقيود الخروج إلى الإنترنت."` | — |
| [SRC-E73001D9AC-L000093](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L93) | 93 | `"8. هندسة الأداء واختبارات الحمل."` | — |
| [SRC-E73001D9AC-L000094](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L94) | 94 | `"9. هندسة البيانات وقواعد البيانات والمخططات والترحيلات."` | — |
| [SRC-E73001D9AC-L000095](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L95) | 95 | `"10. هندسة البحث والاسترجاع وترتيب النتائج."` | — |
| [SRC-E73001D9AC-L000096](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L96) | 96 | `"11. تقييم النماذج والهلوسة والتحقق من الادعاءات."` | — |
| [SRC-E73001D9AC-L000097](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L97) | 97 | `"12. الخصوصية وحوكمة البيانات والاحتفاظ بها."` | — |
| [SRC-E73001D9AC-L000098](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L98) | 98 | `"13. DevOps وسير CI/CD والتوزيع والتراجع."` | — |
| [SRC-E73001D9AC-L000099](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L99) | 99 | `"14. أمن سلسلة التوريد البرمجية والاعتماديات."` | — |
| [SRC-E73001D9AC-L000100](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L100) | 100 | `"15. ضمان الجودة والاختبارات الآلية واختبارات الفشل."` | — |
| [SRC-E73001D9AC-L000101](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L101) | 101 | `"16. التصميم وتجربة المستخدم وإمكانية الوصول وRTL."` | — |
| [SRC-E73001D9AC-L000102](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L102) | 102 | `"17. جودة اللغة العربية والتوطين واتجاهات النصوص."` | — |
| [SRC-E73001D9AC-L000103](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L103) | 103 | `"18. التكلفة والقيود التشغيلية واستهلاك حصص الخدمات المجانية."` | — |
| [SRC-E73001D9AC-L000104](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L104) | 104 | `"19. إدارة الحوادث والاستجابة الأمنية والتعافي من الكوارث."` | — |
| [SRC-E73001D9AC-L000105](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L105) | 105 | `"20. الحوكمة والتوثيق وإدارة التغيير."` | — |
| [SRC-E73001D9AC-L000106](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L106) | 106 | `""` | — |
| [SRC-E73001D9AC-L000107](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L107) | 107 | `"### 4.1 قاعدة المراجعة"` | — |
| [SRC-E73001D9AC-L000108](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L108) | 108 | `""` | — |
| [SRC-E73001D9AC-L000109](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L109) | 109 | `"- التغييرات الصغيرة منخفضة المخاطر تخضع لاختبارات الوحدة والمراجعة المعتادة."` | — |
| [SRC-E73001D9AC-L000110](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L110) | 110 | `"- التغييرات التي تمس الإنترنت أو الصلاحيات أو الذاكرة المشتركة أو التخزين أو تنفيذ الأدوات تخضع لمراجعة أمنية واختبارات فشل مناسبة."` | — |
| [SRC-E73001D9AC-L000111](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L111) | 111 | `"- التغييرات التي تمس المعمارية أو التوسع أو حدود الثقة تخضع لمراجعة معمارية، وتهديدات، وأداء، وتشغيل، وتوثيق قرار."` | — |
| [SRC-E73001D9AC-L000112](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L112) | 112 | `"- عند تعارض آراء المراجعين، يُسجّل التعارض والأدلة والبدائل والمخاطر بدل إخفائه خلف تصويت عددي أو إجابة نموذج لغوي واحدة."` | — |
| [SRC-E73001D9AC-L000113](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L113) | 113 | `"- لا تُستخدم أسماء خبراء أو مراجعات آلية مزعومة كدليل. يُذكر ما إذا كانت المراجعة بشرية أو آلية أو مجرد قائمة تحقق."` | — |
| [SRC-E73001D9AC-L000114](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L114) | 114 | `""` | — |
| [SRC-E73001D9AC-L000115](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L115) | 115 | `"---"` | — |
| [SRC-E73001D9AC-L000116](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L116) | 116 | `""` | — |
| [SRC-E73001D9AC-L000117](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L117) | 117 | `"# الجزء الثالث — المعمارية المنطقية المستهدفة"` | — |
| [SRC-E73001D9AC-L000118](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L118) | 118 | `""` | — |
| [SRC-E73001D9AC-L000119](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L119) | 119 | `"## 5. طبقات النظام وحدود الثقة"` | — |
| [SRC-E73001D9AC-L000120](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L120) | 120 | `""` | — |
| [SRC-E73001D9AC-L000121](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L121) | 121 | `"التقسيم التالي **خريطة منطقية مرجعية**. يجوز دمج طبقات عدة داخل تطبيق واحد في المراحل الأولى، بشرط الحفاظ على حدود المسؤوليات واختبارها. ولا يُشترط أن تتحول كل طبقة إلى خدمة مستقلة."` | — |
| [SRC-E73001D9AC-L000122](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L122) | 122 | `""` | — |
| [SRC-E73001D9AC-L000123](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L123) | 123 | `"### الطبقة 1 — واجهة المستخدم وقنوات الإدخال"` | — |
| [SRC-E73001D9AC-L000124](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L124) | 124 | `"- واجهة عربية RTL واضحة ومتجاوبة."` | — |
| [SRC-E73001D9AC-L000125](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L125) | 125 | `"- تمييز حالة الطلب: مستلم، قيد التنفيذ، مكتمل، متدهور، فشل."` | — |
| [SRC-E73001D9AC-L000126](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L126) | 126 | `"- عرض المصادر والتحذيرات وحدود المعرفة عند الحاجة."` | — |
| [SRC-E73001D9AC-L000127](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L127) | 127 | `"- عدم وضع مفاتيح أو أسرار أو صلاحيات خادم في كود المتصفح."` | — |
| [SRC-E73001D9AC-L000128](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L128) | 128 | `"- عدم اعتبار إخفاء زر في الواجهة وسيلة لتطبيق الصلاحيات؛ يجب فرض الصلاحيات في الخادم."` | — |
| [SRC-E73001D9AC-L000129](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L129) | 129 | `""` | — |
| [SRC-E73001D9AC-L000130](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L130) | 130 | `"### الطبقة 2 — حافة الخدمة وواجهة API"` | — |
| [SRC-E73001D9AC-L000131](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L131) | 131 | `"- التحقق الصارم من بنية الطلب وأنواعه وأحجامه."` | — |
| [SRC-E73001D9AC-L000132](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L132) | 132 | `"- حدود حجم الجسم والمهلات والاتصالات ومعدل الطلبات."` | — |
| [SRC-E73001D9AC-L000133](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L133) | 133 | `"- أخطاء واضحة لا تكشف تفاصيل داخلية أو مسارات ملفات أو أسرارًا."` | — |
| [SRC-E73001D9AC-L000134](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L134) | 134 | `"- سياسة CORS مقيدة بالنطاقات المعتمدة."` | — |
| [SRC-E73001D9AC-L000135](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L135) | 135 | `"- عند استخدام ملفات تعريف الارتباط للمصادقة، تُراجع حماية CSRF وخصائص Secure وHttpOnly وSameSite بحسب تصميم الجلسة."` | — |
| [SRC-E73001D9AC-L000136](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L136) | 136 | `"- واجهات التشخيص والإدارة لا تُعرض للعامة دون حماية مناسبة."` | — |
| [SRC-E73001D9AC-L000137](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L137) | 137 | `""` | — |
| [SRC-E73001D9AC-L000138](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L138) | 138 | `"### الطبقة 3 — الهوية والمستأجرون والصلاحيات"` | — |
| [SRC-E73001D9AC-L000139](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L139) | 139 | `"- لكل مستخدم أو جلسة أو مهمة معرف واضح ونطاق صلاحيات."` | — |
| [SRC-E73001D9AC-L000140](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L140) | 140 | `"- فصل تام بين سياق الطلبات المتزامنة ومنع مشاركة المتغيرات القابلة للتغيير بين المستخدمين."` | — |
| [SRC-E73001D9AC-L000141](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L141) | 141 | `"- تحقق من ملكية كل سجل قبل قراءته أو تعديله أو تصديره."` | — |
| [SRC-E73001D9AC-L000142](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L142) | 142 | `"- لا يكفي تخمين معرف غير قابل للتسلسل لمنع الوصول غير المصرح به؛ يجب التحقق من الصلاحية على الخادم."` | — |
| [SRC-E73001D9AC-L000143](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L143) | 143 | `"- يظل وضع الحلقة المحلية أو الاستخدام الشخصي مختلفًا عن وضع خدمة عامة متعددة المستخدمين، ويجب توثيق الوضع الفعلي لكل نشر."` | — |
| [SRC-E73001D9AC-L000144](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L144) | 144 | `""` | — |
| [SRC-E73001D9AC-L000145](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L145) | 145 | `"### الطبقة 4 — بوابة السياسات وإساءة الاستخدام"` | — |
| [SRC-E73001D9AC-L000146](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L146) | 146 | `"- تحديد أحجام الإدخال والتاريخ المرفق وعدد المصادر والصفحات وعمق المهام."` | — |
| [SRC-E73001D9AC-L000147](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L147) | 147 | `"- تحديد معدل الطلبات وفق الهوية وعنوان المصدر عند ملاءمة ذلك، مع مراعاة NAT والخصوصية."` | — |
| [SRC-E73001D9AC-L000148](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L148) | 148 | `"- فرض ميزانيات للوقت والموارد واستهلاك النموذج والبحث."` | — |
| [SRC-E73001D9AC-L000149](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L149) | 149 | `"- إرجاع 429 عند تجاوز حدود المعدل و503 عند العجز المؤقت عن القبول، مع Retry-After عند ملاءمته."` | — |
| [SRC-E73001D9AC-L000150](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L150) | 150 | `"- حماية الخدمة من حلقات الوكيل غير المنتهية، والطلبات المتضخمة، وإساءة استخدام العمليات المكلفة."` | — |
| [SRC-E73001D9AC-L000151](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L151) | 151 | `"- إضافة CAPTCHA أو تحديات إضافية فقط عند وجود دليل على إساءة استخدام، لا كبديل عن حدود موارد صحيحة."` | — |
| [SRC-E73001D9AC-L000152](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L152) | 152 | `""` | — |
| [SRC-E73001D9AC-L000153](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L153) | 153 | `"### الطبقة 5 — منسق الطلبات (Request Orchestrator)"` | — |
| [SRC-E73001D9AC-L000154](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L154) | 154 | `"- إنشاء سياق مستقل لكل طلب يتضمن deadline وميزانيات محددة وإشارة إلغاء."` | — |
| [SRC-E73001D9AC-L000155](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L155) | 155 | `"- الحفاظ على حدود واضحة لعدد خطوات التخطيط واستدعاءات الأدوات واستدعاءات النماذج والصفحات."` | — |
| [SRC-E73001D9AC-L000156](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L156) | 156 | `"- إنهاء الطلب عند بلوغ الميزانية بدل الاستمرار غير المحدود."` | — |
| [SRC-E73001D9AC-L000157](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L157) | 157 | `"- تمييز الإلغاء بسبب المستخدم من انتهاء الوقت ومن رفض السياسة ومن تعطل المزود."` | — |
| [SRC-E73001D9AC-L000158](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L158) | 158 | `"- تمكين إلغاء المهام التابعة عند إلغاء الطلب الأصلي."` | — |
| [SRC-E73001D9AC-L000159](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L159) | 159 | `"- الحفاظ على معرف تتبع واحد عبر مراحل الطلب، دون وضع أسرار أو بيانات حساسة في المعرف."` | — |
| [SRC-E73001D9AC-L000160](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L160) | 160 | `""` | — |
| [SRC-E73001D9AC-L000161](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L161) | 161 | `"ملاحظة تنفيذية حاكمة: يُنشأ سياق وميزانية منفصلان لكل طلب، ويستخدم المنسق أبسط مسار كافٍ للمهمة. تكون مطابقة المهارات وسير العمل المسجلين هي الخيار الأول قبل إنشاء تعريف وكيل جديد. لا يلزم أن يكون التخطيط مكوّنًا مستقلًا أو خدمة خارجية؛ تحفظ الواجهة والعقد وحدود الصلاحيات حتى لو نُفذت داخل وحدة واحدة."` | — |
| [SRC-E73001D9AC-L000162](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L162) | 162 | `""` | — |
| [SRC-E73001D9AC-L000163](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L163) | 163 | `"### الطبقة 6 — فهم النية والتخطيط"` | — |
| [SRC-E73001D9AC-L000164](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L164) | 164 | `"- مسار مباشر للأسئلة البسيطة التي لا تحتاج إلى بحث."` | — |
| [SRC-E73001D9AC-L000165](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L165) | 165 | `"- مسار بحث للأسئلة التي تتطلب معلومات حديثة أو مصادر."` | — |
| [SRC-E73001D9AC-L000166](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L166) | 166 | `"- مسار متعدد الخطوات للمهام المعقدة فقط."` | — |
| [SRC-E73001D9AC-L000167](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L167) | 167 | `"- مخطط بيانات صارم لخطة النموذج، مع التحقق من كل حقل قبل التنفيذ."` | — |
| [SRC-E73001D9AC-L000168](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L168) | 168 | `"- الخطة التي يصدرها النموذج اقتراح غير موثوق، وليست إذنًا لتنفيذ عملية."` | — |
| [SRC-E73001D9AC-L000169](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L169) | 169 | `"- لا يُسمح للخطة بزيادة الميزانية أو تجاوز الصلاحيات أو تعديل سياسات الأمان."` | — |
| [SRC-E73001D9AC-L000170](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L170) | 170 | `"- الحد من إعادة التخطيط وعدد الخطوات وتكرار الأدوات."` | — |
| [SRC-E73001D9AC-L000171](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L171) | 171 | `"- عند عدم الحاجة إلى بحث جديد، يُعاد استخدام سياق صالح ومحدد العمر بدل إعادة كل العمليات."` | — |
| [SRC-E73001D9AC-L000172](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L172) | 172 | `""` | — |
| [SRC-E73001D9AC-L000173](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L173) | 173 | `"تظل مخرجات التخطيط التي ينتجها النموذج **اقتراحات غير موثوقة**. عند الحاجة إلى تمثيل منظم للمهمة، تستخدم TaskSpec بمدخلات ومخرجات وقيود ومعايير قبول وقدرات مطلوبة؛ لا تمنح المواصفة صلاحيات. تُتحقق الخطة حتميًا قبل التنفيذ، وتُرفض الخطوات غير المعروفة أو المتجاوزة للحدود. الخطط المتكررة والحساسة تُفضّل لها مسارات Workflow محددة يمكن اختبارها، مع إبقاء المسار المباشر للأسئلة البسيطة."` | — |
| [SRC-E73001D9AC-L000174](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L174) | 174 | `""` | — |
| [SRC-E73001D9AC-L000175](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L175) | 175 | `"### الطبقة 7 — طبقة البحث وجلب الصفحات"` | — |
| [SRC-E73001D9AC-L000176](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L176) | 176 | `"- فصل موصلات البحث عن محرك التخطيط وعن منطق الإجابة."` | — |
| [SRC-E73001D9AC-L000177](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L177) | 177 | `"- تحديد timeout وconcurrency وresponse-size وresult-count لكل موصل."` | — |
| [SRC-E73001D9AC-L000178](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L178) | 178 | `"- عزل فشل موصل واحد؛ لا يمنع بقية المصادر من العمل إذا كان المسار يسمح بذلك."` | — |
| [SRC-E73001D9AC-L000179](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L179) | 179 | `"- تحديد تاريخ النتائج ومصدرها ووقت الاسترجاع والطلب الذي جلبها."` | — |
| [SRC-E73001D9AC-L000180](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L180) | 180 | `"- جلب المحتوى العام المسموح فقط؛ لا تجاوز لتسجيل الدخول أو paywall أو ضوابط الوصول."` | — |
| [SRC-E73001D9AC-L000181](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L181) | 181 | `"- احترام شروط استخدام المصادر وحدود الطلبات المسموحة."` | — |
| [SRC-E73001D9AC-L000182](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L182) | 182 | `"- تخزين النتائج مؤقتًا فقط مع سياسة صلاحية وتحديث وحذف مناسبة."` | — |
| [SRC-E73001D9AC-L000183](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L183) | 183 | `"- عدم افتراض استقلال المصادر لمجرد أن النتائج ظهرت في أكثر من محرك."` | — |
| [SRC-E73001D9AC-L000184](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L184) | 184 | `""` | — |
| [SRC-E73001D9AC-L000185](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L185) | 185 | `"### الطبقة 8 — بوابة الأدوات وسجل قدراتها"` | — |
| [SRC-E73001D9AC-L000186](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L186) | 186 | `"كل أداة مسجلة بوصف قابل للتحقق يشمل:"` | — |
| [SRC-E73001D9AC-L000187](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L187) | 187 | `"- الاسم والإصدار والجهة المالكة."` | — |
| [SRC-E73001D9AC-L000188](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L188) | 188 | `"- المدخلات والمخرجات والمخطط المتوقع."` | — |
| [SRC-E73001D9AC-L000189](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L189) | 189 | `"- الصلاحيات التي تحتاجها."` | — |
| [SRC-E73001D9AC-L000190](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L190) | 190 | `"- مهلة التنفيذ والميزانية والحدود القصوى."` | — |
| [SRC-E73001D9AC-L000191](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L191) | 191 | `"- ما إذا كانت للقراءة فقط أم ذات أثر خارجي."` | — |
| [SRC-E73001D9AC-L000192](../OMARAI_FOUNDATIONAL_ENGINEERING_CHARTER_AR.md#L192) | 192 | `"- طريقة فحص صحتها، وحدود الفحص، ووقت آخر تحقق."` | — |
