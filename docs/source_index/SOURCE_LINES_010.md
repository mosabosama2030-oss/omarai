# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **010**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L001108 إلى SRC-1AE03B9EC3-L001907
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L001108](../../agents/web_agent.py#L1108) | 1108 | `"                else \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001109](../../agents/web_agent.py#L1109) | 1109 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001110](../../agents/web_agent.py#L1110) | 1110 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001111](../../agents/web_agent.py#L1111) | 1111 | `"                \"name\": \"tavily_search_api\","` | — |
| [SRC-1AE03B9EC3-L001112](../../agents/web_agent.py#L1112) | 1112 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001113](../../agents/web_agent.py#L1113) | 1113 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L001114](../../agents/web_agent.py#L1114) | 1114 | `"                    \"configured\" if status.get(\"tavily_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001115](../../agents/web_agent.py#L1115) | 1115 | `"                    else \"not_configured\""` | — |
| [SRC-1AE03B9EC3-L001116](../../agents/web_agent.py#L1116) | 1116 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001117](../../agents/web_agent.py#L1117) | 1117 | `"                \"runtime_status\": not_tested if status.get(\"tavily_search_api_configured\")"` | — |
| [SRC-1AE03B9EC3-L001118](../../agents/web_agent.py#L1118) | 1118 | `"                else \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001119](../../agents/web_agent.py#L1119) | 1119 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001120](../../agents/web_agent.py#L1120) | 1120 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001121](../../agents/web_agent.py#L1121) | 1121 | `"                \"name\": \"openrouter_web_search\","` | — |
| [SRC-1AE03B9EC3-L001122](../../agents/web_agent.py#L1122) | 1122 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001123](../../agents/web_agent.py#L1123) | 1123 | `"                \"configuration_status\": ("` | — |
| [SRC-1AE03B9EC3-L001124](../../agents/web_agent.py#L1124) | 1124 | `"                    \"enabled\" if status.get(\"openrouter_web_search_enabled\")"` | — |
| [SRC-1AE03B9EC3-L001125](../../agents/web_agent.py#L1125) | 1125 | `"                    else \"disabled\""` | — |
| [SRC-1AE03B9EC3-L001126](../../agents/web_agent.py#L1126) | 1126 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001127](../../agents/web_agent.py#L1127) | 1127 | `"                \"runtime_status\": not_tested if status.get(\"openrouter_web_search_enabled\")"` | — |
| [SRC-1AE03B9EC3-L001128](../../agents/web_agent.py#L1128) | 1128 | `"                else \"disabled\","` | — |
| [SRC-1AE03B9EC3-L001129](../../agents/web_agent.py#L1129) | 1129 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001130](../../agents/web_agent.py#L1130) | 1130 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L001131](../../agents/web_agent.py#L1131) | 1131 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L001132](../../agents/web_agent.py#L1132) | 1132 | `"            \"web_search\": {"` | — |
| [SRC-1AE03B9EC3-L001133](../../agents/web_agent.py#L1133) | 1133 | `"                \"implemented\": True,"` | — |
| [SRC-1AE03B9EC3-L001134](../../agents/web_agent.py#L1134) | 1134 | `"                \"local_dependencies_ready\": bool(status.get(\"web_search_ready\")),"` | — |
| [SRC-1AE03B9EC3-L001135](../../agents/web_agent.py#L1135) | 1135 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001136](../../agents/web_agent.py#L1136) | 1136 | `"                \"providers\": providers,"` | — |
| [SRC-1AE03B9EC3-L001137](../../agents/web_agent.py#L1137) | 1137 | `"                \"semantics\": ("` | — |
| [SRC-1AE03B9EC3-L001138](../../agents/web_agent.py#L1138) | 1138 | `"                    \"Configuration and installed dependencies do not prove that a live \""` | — |
| [SRC-1AE03B9EC3-L001139](../../agents/web_agent.py#L1139) | 1139 | `"                    \"network request will succeed.\""` | — |
| [SRC-1AE03B9EC3-L001140](../../agents/web_agent.py#L1140) | 1140 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001141](../../agents/web_agent.py#L1141) | 1141 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001142](../../agents/web_agent.py#L1142) | 1142 | `"            \"language_model\": {"` | — |
| [SRC-1AE03B9EC3-L001143](../../agents/web_agent.py#L1143) | 1143 | `"                \"configured\": bool(status.get(\"language_model_configured\")),"` | — |
| [SRC-1AE03B9EC3-L001144](../../agents/web_agent.py#L1144) | 1144 | `"                \"runtime_status\": not_tested,"` | — |
| [SRC-1AE03B9EC3-L001145](../../agents/web_agent.py#L1145) | 1145 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001146](../../agents/web_agent.py#L1146) | 1146 | `"        }"` | — |
| [SRC-1AE03B9EC3-L001147](../../agents/web_agent.py#L1147) | 1147 | `""` | — |
| [SRC-1AE03B9EC3-L001148](../../agents/web_agent.py#L1148) | 1148 | `"    def _self_description_answer(self, question: str) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L001149](../../agents/web_agent.py#L1149) | 1149 | `"        \"\"\"Answer self/capability questions without inventing a live health result.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001150](../../agents/web_agent.py#L1150) | 1150 | `"        value = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L001151](../../agents/web_agent.py#L1151) | 1151 | `"        current_search_question = self._is_current_search_status_question(question)"` | — |
| [SRC-1AE03B9EC3-L001152](../../agents/web_agent.py#L1152) | 1152 | `""` | — |
| [SRC-1AE03B9EC3-L001153](../../agents/web_agent.py#L1153) | 1153 | `"        if current_search_question:"` | — |
| [SRC-1AE03B9EC3-L001154](../../agents/web_agent.py#L1154) | 1154 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001155](../../agents/web_agent.py#L1155) | 1155 | `"                \"لا، لم أنفّذ بحثًا حيًا للإجابة عن هذا السؤال تحديدًا؛ هذا السؤال عن \""` | — |
| [SRC-1AE03B9EC3-L001156](../../agents/web_agent.py#L1156) | 1156 | `"                \"طريقة عملي، ولذلك لم أبدأ بحث ويب في هذه الجولة. هذا لا يعني أن البحث \""` | — |
| [SRC-1AE03B9EC3-L001157](../../agents/web_agent.py#L1157) | 1157 | `"                \"غير متاح؛ عند تنفيذ طلب يحتاج إلى معلومات حديثة سأوضح هل جرت محاولة البحث، \""` | — |
| [SRC-1AE03B9EC3-L001158](../../agents/web_agent.py#L1158) | 1158 | `"                \"وما النتائج التي عادت، وما إذا اكتملت الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L001159](../../agents/web_agent.py#L1159) | 1159 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001160](../../agents/web_agent.py#L1160) | 1160 | `"            result = self._local_answer_result(question, answer, \"capability_answer\")"` | — |
| [SRC-1AE03B9EC3-L001161](../../agents/web_agent.py#L1161) | 1161 | `"            result[\"request_execution_status\"] = {"` | — |
| [SRC-1AE03B9EC3-L001162](../../agents/web_agent.py#L1162) | 1162 | `"                \"search_attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L001163](../../agents/web_agent.py#L1163) | 1163 | `"                \"search_outcome\": \"not_attempted\","` | — |
| [SRC-1AE03B9EC3-L001164](../../agents/web_agent.py#L1164) | 1164 | `"                \"semantics\": \"status_of_this_request_only\","` | — |
| [SRC-1AE03B9EC3-L001165](../../agents/web_agent.py#L1165) | 1165 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001166](../../agents/web_agent.py#L1166) | 1166 | `"            result[\"capability_status\"] = self._capability_status_snapshot()"` | — |
| [SRC-1AE03B9EC3-L001167](../../agents/web_agent.py#L1167) | 1167 | `"            return result"` | — |
| [SRC-1AE03B9EC3-L001168](../../agents/web_agent.py#L1168) | 1168 | `""` | — |
| [SRC-1AE03B9EC3-L001169](../../agents/web_agent.py#L1169) | 1169 | `"        capability_phrases = ("` | — |
| [SRC-1AE03B9EC3-L001170](../../agents/web_agent.py#L1170) | 1170 | `"            \"كيف تستطيع مساعدتي\", \"ازاي تقدر تساعدني\", \"ازاي ممكن تساعدني\","` | — |
| [SRC-1AE03B9EC3-L001171](../../agents/web_agent.py#L1171) | 1171 | `"            \"ماذا تستطيع ان تفعل\", \"ما الذي تستطيع فعله\", \"ايه اللي تقدر تعمله\","` | — |
| [SRC-1AE03B9EC3-L001172](../../agents/web_agent.py#L1172) | 1172 | `"            \"what can you do\", \"how can you help me\","` | — |
| [SRC-1AE03B9EC3-L001173](../../agents/web_agent.py#L1173) | 1173 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001174](../../agents/web_agent.py#L1174) | 1174 | `"        if any(term in value for term in capability_phrases):"` | — |
| [SRC-1AE03B9EC3-L001175](../../agents/web_agent.py#L1175) | 1175 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001176](../../agents/web_agent.py#L1176) | 1176 | `"                \"أقدر أساعدك في شرح الأسئلة ووضع خطط عملية، كما يتضمن Omarai مسارًا \""` | — |
| [SRC-1AE03B9EC3-L001177](../../agents/web_agent.py#L1177) | 1177 | `"                \"للبحث في الويب عند الحاجة إلى معلومات حديثة أو روابط أو مقارنة خيارات. \""` | — |
| [SRC-1AE03B9EC3-L001178](../../agents/web_agent.py#L1178) | 1178 | `"                \"سأوضح في كل مهمة ما إذا نُفذ البحث فعلًا وما المصادر التي أمكن جمعها، \""` | — |
| [SRC-1AE03B9EC3-L001179](../../agents/web_agent.py#L1179) | 1179 | `"                \"وما الذي لم يمكن التحقق منه. قد تعمل بعض الموصلات الاختيارية فقط عند \""` | — |
| [SRC-1AE03B9EC3-L001180](../../agents/web_agent.py#L1180) | 1180 | `"                \"ضبط إعداداتها، ولا أضمن الوصول إلى كل موقع أو إلى المجموعات والمنشورات \""` | — |
| [SRC-1AE03B9EC3-L001181](../../agents/web_agent.py#L1181) | 1181 | `"                \"الخاصة. لم أجرِ اختبار اتصال حي في هذه الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L001182](../../agents/web_agent.py#L1182) | 1182 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001183](../../agents/web_agent.py#L1183) | 1183 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001184](../../agents/web_agent.py#L1184) | 1184 | `"            status = self.status()"` | — |
| [SRC-1AE03B9EC3-L001185](../../agents/web_agent.py#L1185) | 1185 | `"            providers = [\"DuckDuckGo HTML\", \"Bing RSS\"]"` | — |
| [SRC-1AE03B9EC3-L001186](../../agents/web_agent.py#L1186) | 1186 | `"            providers.append(\"Google News RSS عند ملاءمة السؤال أو الحاجة إلى معلومات حديثة\")"` | — |
| [SRC-1AE03B9EC3-L001187](../../agents/web_agent.py#L1187) | 1187 | `"            if status.get(\"deepseek_search_api_configured\"):"` | — |
| [SRC-1AE03B9EC3-L001188](../../agents/web_agent.py#L1188) | 1188 | `"                providers.append("` | — |
| [SRC-1AE03B9EC3-L001189](../../agents/web_agent.py#L1189) | 1189 | `"                    \"DeepSeek Search API (مفتاحه مضبوط، لكنه غير مختبر في هذه الإجابة \""` | — |
| [SRC-1AE03B9EC3-L001190](../../agents/web_agent.py#L1190) | 1190 | `"                    \"وقد يستهلك استخدامًا مدفوعًا)\""` | — |
| [SRC-1AE03B9EC3-L001191](../../agents/web_agent.py#L1191) | 1191 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001192](../../agents/web_agent.py#L1192) | 1192 | `"            if status.get(\"brave_search_api_configured\"):"` | — |
| [SRC-1AE03B9EC3-L001193](../../agents/web_agent.py#L1193) | 1193 | `"                providers.append(\"Brave Search API (الإعداد موجود، وليس دليلًا على نجاح الاتصال)\")"` | — |
| [SRC-1AE03B9EC3-L001194](../../agents/web_agent.py#L1194) | 1194 | `"            if status.get(\"tavily_search_api_configured\"):"` | — |
| [SRC-1AE03B9EC3-L001195](../../agents/web_agent.py#L1195) | 1195 | `"                providers.append(\"Tavily Search API (الإعداد موجود، وليس دليلًا على نجاح الاتصال)\")"` | — |
| [SRC-1AE03B9EC3-L001196](../../agents/web_agent.py#L1196) | 1196 | `"            if status.get(\"openrouter_web_search_enabled\"):"` | — |
| [SRC-1AE03B9EC3-L001197](../../agents/web_agent.py#L1197) | 1197 | `"                providers.append(\"بحث OpenRouter المباشر (مفعّل بالإعداد، وقد يستهلك رصيدًا)\")"` | — |
| [SRC-1AE03B9EC3-L001198](../../agents/web_agent.py#L1198) | 1198 | `"            answer = ("` | — |
| [SRC-1AE03B9EC3-L001199](../../agents/web_agent.py#L1199) | 1199 | `"                \"بحسب الكود الحالي، يتضمن Omarai مسار بحث ويب يستخدم: \""` | — |
| [SRC-1AE03B9EC3-L001200](../../agents/web_agent.py#L1200) | 1200 | `"                + \"، \".join(providers)"` | — |
| [SRC-1AE03B9EC3-L001201](../../agents/web_agent.py#L1201) | 1201 | `"                + \". هذه قائمة بالموصلات المضمّنة أو المهيأة، وليست إثباتًا بأنها نجحت \""` | — |
| [SRC-1AE03B9EC3-L001202](../../agents/web_agent.py#L1202) | 1202 | `"                \"في هذه اللحظة. لم أنفّذ اختبار اتصال حي في هذه الإجابة، لذلك لا أستطيع \""` | — |
| [SRC-1AE03B9EC3-L001203](../../agents/web_agent.py#L1203) | 1203 | `"                \"تأكيد توافر الشبكة الآن. عند طلب بحث فعلي، ينبغي أن يوضح التقرير ما إذا \""` | — |
| [SRC-1AE03B9EC3-L001204](../../agents/web_agent.py#L1204) | 1204 | `"                \"بدأت المحاولة، وما الموصلات التي أعادت نتائج، وما الصفحات التي أمكن قراءة \""` | — |
| [SRC-1AE03B9EC3-L001205](../../agents/web_agent.py#L1205) | 1205 | `"                \"محتواها. لا يوجد وصول مضمون إلى كل الإنترنت أو إلى المحتوى الخاص.\""` | — |
| [SRC-1AE03B9EC3-L001206](../../agents/web_agent.py#L1206) | 1206 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001207](../../agents/web_agent.py#L1207) | 1207 | `"        result = self._local_answer_result(question, answer, \"capability_answer\")"` | — |
| [SRC-1AE03B9EC3-L001208](../../agents/web_agent.py#L1208) | 1208 | `"        result[\"capability_status\"] = self._capability_status_snapshot()"` | — |
| [SRC-1AE03B9EC3-L001209](../../agents/web_agent.py#L1209) | 1209 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L001210](../../agents/web_agent.py#L1210) | 1210 | `""` | — |
| [SRC-1AE03B9EC3-L001211](../../agents/web_agent.py#L1211) | 1211 | `"    def _answer_without_search("` | — |
| [SRC-1AE03B9EC3-L001212](../../agents/web_agent.py#L1212) | 1212 | `"        self, question: str, history: list[dict[str, str]]"` | — |
| [SRC-1AE03B9EC3-L001213](../../agents/web_agent.py#L1213) | 1213 | `"    ) -> dict[str, Any] \| None:"` | — |
| [SRC-1AE03B9EC3-L001214](../../agents/web_agent.py#L1214) | 1214 | `"        \"\"\"Answer stable informational questions with the configured LLM, without fake citations.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001215](../../agents/web_agent.py#L1215) | 1215 | `"        if not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L001216](../../agents/web_agent.py#L1216) | 1216 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L001217](../../agents/web_agent.py#L1217) | 1217 | `"        messages: list[dict[str, str]] = ["` | — |
| [SRC-1AE03B9EC3-L001218](../../agents/web_agent.py#L1218) | 1218 | `"            {"` | — |
| [SRC-1AE03B9EC3-L001219](../../agents/web_agent.py#L1219) | 1219 | `"                \"role\": \"system\","` | — |
| [SRC-1AE03B9EC3-L001220](../../agents/web_agent.py#L1220) | 1220 | `"                \"content\": ("` | — |
| [SRC-1AE03B9EC3-L001221](../../agents/web_agent.py#L1221) | 1221 | `"                    \"أنت Omarai، مساعد عربي عملي. أجب مباشرة وباللغة التي استخدمها الشخص، \""` | — |
| [SRC-1AE03B9EC3-L001222](../../agents/web_agent.py#L1222) | 1222 | `"                    \"وافهم المقصود حتى لو كان باللهجة المصرية أو به أخطاء كتابية. هذا المسار \""` | — |
| [SRC-1AE03B9EC3-L001223](../../agents/web_agent.py#L1223) | 1223 | `"                    \"للشرح والمعرفة العامة والأسئلة الحوارية غير المعتمدة على معلومات لحظية. \""` | — |
| [SRC-1AE03B9EC3-L001224](../../agents/web_agent.py#L1224) | 1224 | `"                    \"لا تستخدم أدوات الويب ولا تقل إنك بحثت أو تحققت من مصدر. لا تختلق أرقامًا \""` | — |
| [SRC-1AE03B9EC3-L001225](../../agents/web_agent.py#L1225) | 1225 | `"                    \"أو اقتباسات أو روابط. إذا كان جزء من السؤال يتطلب بيانات حديثة أو تحققًا \""` | — |
| [SRC-1AE03B9EC3-L001226](../../agents/web_agent.py#L1226) | 1226 | `"                    \"خارجيًا، صرّح بذلك بدل الجزم. وضّح عدم اليقين بإيجاز، وأعط إجابة مفيدة \""` | — |
| [SRC-1AE03B9EC3-L001227](../../agents/web_agent.py#L1227) | 1227 | `"                    \"من غير إطالة أو سلسلة تفكير داخلية.\""` | — |
| [SRC-1AE03B9EC3-L001228](../../agents/web_agent.py#L1228) | 1228 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001229](../../agents/web_agent.py#L1229) | 1229 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001230](../../agents/web_agent.py#L1230) | 1230 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L001231](../../agents/web_agent.py#L1231) | 1231 | `"        messages.extend(history[-MAX_HISTORY_ITEMS:])"` | — |
| [SRC-1AE03B9EC3-L001232](../../agents/web_agent.py#L1232) | 1232 | `"        messages.append({\"role\": \"user\", \"content\": question})"` | — |
| [SRC-1AE03B9EC3-L001233](../../agents/web_agent.py#L1233) | 1233 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001234](../../agents/web_agent.py#L1234) | 1234 | `"            answer = self._request_completion("` | — |
| [SRC-1AE03B9EC3-L001235](../../agents/web_agent.py#L1235) | 1235 | `"                messages,"` | — |
| [SRC-1AE03B9EC3-L001236](../../agents/web_agent.py#L1236) | 1236 | `"                max_tokens=1500,"` | — |
| [SRC-1AE03B9EC3-L001237](../../agents/web_agent.py#L1237) | 1237 | `"                temperature=0.2,"` | — |
| [SRC-1AE03B9EC3-L001238](../../agents/web_agent.py#L1238) | 1238 | `"                timeout=self._effective_timeout(min(self.timeout, 28)),"` | — |
| [SRC-1AE03B9EC3-L001239](../../agents/web_agent.py#L1239) | 1239 | `"                model=self.answer_model,"` | — |
| [SRC-1AE03B9EC3-L001240](../../agents/web_agent.py#L1240) | 1240 | `"                enable_web_search=False,"` | — |
| [SRC-1AE03B9EC3-L001241](../../agents/web_agent.py#L1241) | 1241 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001242](../../agents/web_agent.py#L1242) | 1242 | `"        except (RuntimeError, AgentDependencyError):"` | — |
| [SRC-1AE03B9EC3-L001243](../../agents/web_agent.py#L1243) | 1243 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L001244](../../agents/web_agent.py#L1244) | 1244 | `"        # Never turn an overlong completion into a seemingly complete answer by slicing it."` | — |
| [SRC-1AE03B9EC3-L001245](../../agents/web_agent.py#L1245) | 1245 | `"        if len(answer) > 24_000:"` | — |
| [SRC-1AE03B9EC3-L001246](../../agents/web_agent.py#L1246) | 1246 | `"            return None"` | — |
| [SRC-1AE03B9EC3-L001247](../../agents/web_agent.py#L1247) | 1247 | `"        return {"` | — |
| [SRC-1AE03B9EC3-L001248](../../agents/web_agent.py#L1248) | 1248 | `"            \"answer\": answer,"` | — |
| [SRC-1AE03B9EC3-L001249](../../agents/web_agent.py#L1249) | 1249 | `"            \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L001250](../../agents/web_agent.py#L1250) | 1250 | `"            \"search_query\": question,"` | — |
| [SRC-1AE03B9EC3-L001251](../../agents/web_agent.py#L1251) | 1251 | `"            \"search_queries\": [],"` | — |
| [SRC-1AE03B9EC3-L001252](../../agents/web_agent.py#L1252) | 1252 | `"            \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L001253](../../agents/web_agent.py#L1253) | 1253 | `"                \"mode\": \"auto\","` | — |
| [SRC-1AE03B9EC3-L001254](../../agents/web_agent.py#L1254) | 1254 | `"                \"planning_method\": \"general_qa_without_web\","` | — |
| [SRC-1AE03B9EC3-L001255](../../agents/web_agent.py#L1255) | 1255 | `"                \"web_search_skipped\": True,"` | — |
| [SRC-1AE03B9EC3-L001256](../../agents/web_agent.py#L1256) | 1256 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001257](../../agents/web_agent.py#L1257) | 1257 | `"            \"sources\": [],"` | — |
| [SRC-1AE03B9EC3-L001258](../../agents/web_agent.py#L1258) | 1258 | `"            \"used_language_model\": True,"` | — |
| [SRC-1AE03B9EC3-L001259](../../agents/web_agent.py#L1259) | 1259 | `"            \"used_web_search\": False,"` | — |
| [SRC-1AE03B9EC3-L001260](../../agents/web_agent.py#L1260) | 1260 | `"            \"search_attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L001261](../../agents/web_agent.py#L1261) | 1261 | `"            \"used_social_search\": False,"` | — |
| [SRC-1AE03B9EC3-L001262](../../agents/web_agent.py#L1262) | 1262 | `"            \"warnings\": [],"` | — |
| [SRC-1AE03B9EC3-L001263](../../agents/web_agent.py#L1263) | 1263 | `"            \"kind\": \"general_answer\","` | — |
| [SRC-1AE03B9EC3-L001264](../../agents/web_agent.py#L1264) | 1264 | `"            \"research_quality\": \"not_applicable\","` | — |
| [SRC-1AE03B9EC3-L001265](../../agents/web_agent.py#L1265) | 1265 | `"            \"model_calls\": list(self.model_usage),"` | — |
| [SRC-1AE03B9EC3-L001266](../../agents/web_agent.py#L1266) | 1266 | `"        }"` | — |
| [SRC-1AE03B9EC3-L001267](../../agents/web_agent.py#L1267) | 1267 | `""` | — |
| [SRC-1AE03B9EC3-L001268](../../agents/web_agent.py#L1268) | 1268 | `"    def _search_duckduckgo_html(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001269](../../agents/web_agent.py#L1269) | 1269 | `"        import httpx"` | — |
| [SRC-1AE03B9EC3-L001270](../../agents/web_agent.py#L1270) | 1270 | `"        from bs4 import BeautifulSoup"` | — |
| [SRC-1AE03B9EC3-L001271](../../agents/web_agent.py#L1271) | 1271 | `""` | — |
| [SRC-1AE03B9EC3-L001272](../../agents/web_agent.py#L1272) | 1272 | `"        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001273](../../agents/web_agent.py#L1273) | 1273 | `"            \"https://html.duckduckgo.com/html/\","` | — |
| [SRC-1AE03B9EC3-L001274](../../agents/web_agent.py#L1274) | 1274 | `"            params={\"q\": query},"` | — |
| [SRC-1AE03B9EC3-L001275](../../agents/web_agent.py#L1275) | 1275 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001276](../../agents/web_agent.py#L1276) | 1276 | `"                \"User-Agent\": ("` | — |
| [SRC-1AE03B9EC3-L001277](../../agents/web_agent.py#L1277) | 1277 | `"                    \"Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 \""` | — |
| [SRC-1AE03B9EC3-L001278](../../agents/web_agent.py#L1278) | 1278 | `"                    \"(KHTML, like Gecko) Chrome/124.0 Mobile Safari/537.36\""` | — |
| [SRC-1AE03B9EC3-L001279](../../agents/web_agent.py#L1279) | 1279 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001280](../../agents/web_agent.py#L1280) | 1280 | `"                \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001281](../../agents/web_agent.py#L1281) | 1281 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001282](../../agents/web_agent.py#L1282) | 1282 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001283](../../agents/web_agent.py#L1283) | 1283 | `"            # Search provider redirects are not followed automatically. A 3xx is"` | — |
| [SRC-1AE03B9EC3-L001284](../../agents/web_agent.py#L1284) | 1284 | `"            # reported as a provider failure so the host never fetches an unchecked target."` | — |
| [SRC-1AE03B9EC3-L001285](../../agents/web_agent.py#L1285) | 1285 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001286](../../agents/web_agent.py#L1286) | 1286 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001287](../../agents/web_agent.py#L1287) | 1287 | `"        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001288](../../agents/web_agent.py#L1288) | 1288 | `"            raise RuntimeError(f\"HTTP {response.status_code}\")"` | — |
| [SRC-1AE03B9EC3-L001289](../../agents/web_agent.py#L1289) | 1289 | `"        soup = BeautifulSoup(response.text, \"html.parser\")"` | — |
| [SRC-1AE03B9EC3-L001290](../../agents/web_agent.py#L1290) | 1290 | `"        if soup.select_one(\"form#challenge-form, #challenge-form, .anomaly-modal\"):"` | — |
| [SRC-1AE03B9EC3-L001291](../../agents/web_agent.py#L1291) | 1291 | `"            raise RuntimeError(\"anti-bot challenge returned\")"` | — |
| [SRC-1AE03B9EC3-L001292](../../agents/web_agent.py#L1292) | 1292 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001293](../../agents/web_agent.py#L1293) | 1293 | `"        for card in soup.select(\"div.result\"):"` | — |
| [SRC-1AE03B9EC3-L001294](../../agents/web_agent.py#L1294) | 1294 | `"            link = card.select_one(\"a.result__a\")"` | — |
| [SRC-1AE03B9EC3-L001295](../../agents/web_agent.py#L1295) | 1295 | `"            if not link:"` | — |
| [SRC-1AE03B9EC3-L001296](../../agents/web_agent.py#L1296) | 1296 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001297](../../agents/web_agent.py#L1297) | 1297 | `"            url = _public_http_url(self._unwrap_search_url(str(link.get(\"href\", \"\"))))"` | — |
| [SRC-1AE03B9EC3-L001298](../../agents/web_agent.py#L1298) | 1298 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001299](../../agents/web_agent.py#L1299) | 1299 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001300](../../agents/web_agent.py#L1300) | 1300 | `"            snippet_node = card.select_one(\".result__snippet\")"` | — |
| [SRC-1AE03B9EC3-L001301](../../agents/web_agent.py#L1301) | 1301 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001302](../../agents/web_agent.py#L1302) | 1302 | `"                \"title\": _clean_text(link.get_text(\" \", strip=True), 300),"` | — |
| [SRC-1AE03B9EC3-L001303](../../agents/web_agent.py#L1303) | 1303 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001304](../../agents/web_agent.py#L1304) | 1304 | `"                \"snippet\": _clean_text("` | — |
| [SRC-1AE03B9EC3-L001305](../../agents/web_agent.py#L1305) | 1305 | `"                    snippet_node.get_text(\" \", strip=True) if snippet_node else \"\", 1200"` | — |
| [SRC-1AE03B9EC3-L001306](../../agents/web_agent.py#L1306) | 1306 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001307](../../agents/web_agent.py#L1307) | 1307 | `"                \"provider\": \"duckduckgo_html\","` | — |
| [SRC-1AE03B9EC3-L001308](../../agents/web_agent.py#L1308) | 1308 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001309](../../agents/web_agent.py#L1309) | 1309 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001310](../../agents/web_agent.py#L1310) | 1310 | `"                \"published_at\": \"\","` | — |
| [SRC-1AE03B9EC3-L001311](../../agents/web_agent.py#L1311) | 1311 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001312](../../agents/web_agent.py#L1312) | 1312 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001313](../../agents/web_agent.py#L1313) | 1313 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001314](../../agents/web_agent.py#L1314) | 1314 | `"        if not rows and (\"captcha\" in response.text.casefold() or \"anomaly\" in response.text.casefold()):"` | — |
| [SRC-1AE03B9EC3-L001315](../../agents/web_agent.py#L1315) | 1315 | `"            raise RuntimeError(\"anti-bot challenge returned no result cards\")"` | — |
| [SRC-1AE03B9EC3-L001316](../../agents/web_agent.py#L1316) | 1316 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001317](../../agents/web_agent.py#L1317) | 1317 | `""` | — |
| [SRC-1AE03B9EC3-L001318](../../agents/web_agent.py#L1318) | 1318 | `"    def _search_bing_rss(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001319](../../agents/web_agent.py#L1319) | 1319 | `"        import xml.etree.ElementTree as ET"` | — |
| [SRC-1AE03B9EC3-L001320](../../agents/web_agent.py#L1320) | 1320 | `""` | — |
| [SRC-1AE03B9EC3-L001321](../../agents/web_agent.py#L1321) | 1321 | `"        import httpx"` | — |
| [SRC-1AE03B9EC3-L001322](../../agents/web_agent.py#L1322) | 1322 | `""` | — |
| [SRC-1AE03B9EC3-L001323](../../agents/web_agent.py#L1323) | 1323 | `"        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001324](../../agents/web_agent.py#L1324) | 1324 | `"            \"https://www.bing.com/search\","` | — |
| [SRC-1AE03B9EC3-L001325](../../agents/web_agent.py#L1325) | 1325 | `"            params={\"format\": \"rss\", \"q\": query},"` | — |
| [SRC-1AE03B9EC3-L001326](../../agents/web_agent.py#L1326) | 1326 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001327](../../agents/web_agent.py#L1327) | 1327 | `"                \"User-Agent\": ("` | — |
| [SRC-1AE03B9EC3-L001328](../../agents/web_agent.py#L1328) | 1328 | `"                    \"Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 \""` | — |
| [SRC-1AE03B9EC3-L001329](../../agents/web_agent.py#L1329) | 1329 | `"                    \"(KHTML, like Gecko) Chrome/124.0 Mobile Safari/537.36\""` | — |
| [SRC-1AE03B9EC3-L001330](../../agents/web_agent.py#L1330) | 1330 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L001331](../../agents/web_agent.py#L1331) | 1331 | `"                \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001332](../../agents/web_agent.py#L1332) | 1332 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001333](../../agents/web_agent.py#L1333) | 1333 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001334](../../agents/web_agent.py#L1334) | 1334 | `"            # Refuse automatic redirects from public search endpoints; never fetch an"` | — |
| [SRC-1AE03B9EC3-L001335](../../agents/web_agent.py#L1335) | 1335 | `"            # unchecked redirect target as part of a provider search request."` | — |
| [SRC-1AE03B9EC3-L001336](../../agents/web_agent.py#L1336) | 1336 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001337](../../agents/web_agent.py#L1337) | 1337 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001338](../../agents/web_agent.py#L1338) | 1338 | `"        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001339](../../agents/web_agent.py#L1339) | 1339 | `"            raise RuntimeError(f\"HTTP {response.status_code}\")"` | — |
| [SRC-1AE03B9EC3-L001340](../../agents/web_agent.py#L1340) | 1340 | `"        root = ET.fromstring(response.content)"` | — |
| [SRC-1AE03B9EC3-L001341](../../agents/web_agent.py#L1341) | 1341 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001342](../../agents/web_agent.py#L1342) | 1342 | `"        for item in root.iter():"` | — |
| [SRC-1AE03B9EC3-L001343](../../agents/web_agent.py#L1343) | 1343 | `"            if item.tag.rsplit(\"}\", 1)[-1] != \"item\":"` | — |
| [SRC-1AE03B9EC3-L001344](../../agents/web_agent.py#L1344) | 1344 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001345](../../agents/web_agent.py#L1345) | 1345 | `"            fields = {"` | — |
| [SRC-1AE03B9EC3-L001346](../../agents/web_agent.py#L1346) | 1346 | `"                child.tag.rsplit(\"}\", 1)[-1]: (child.text or \"\")"` | — |
| [SRC-1AE03B9EC3-L001347](../../agents/web_agent.py#L1347) | 1347 | `"                for child in item"` | — |
| [SRC-1AE03B9EC3-L001348](../../agents/web_agent.py#L1348) | 1348 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001349](../../agents/web_agent.py#L1349) | 1349 | `"            url = _public_http_url(fields.get(\"link\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001350](../../agents/web_agent.py#L1350) | 1350 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001351](../../agents/web_agent.py#L1351) | 1351 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001352](../../agents/web_agent.py#L1352) | 1352 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001353](../../agents/web_agent.py#L1353) | 1353 | `"                \"title\": _clean_text(fields.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001354](../../agents/web_agent.py#L1354) | 1354 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001355](../../agents/web_agent.py#L1355) | 1355 | `"                \"snippet\": _clean_text(fields.get(\"description\", \"\"), 1200),"` | — |
| [SRC-1AE03B9EC3-L001356](../../agents/web_agent.py#L1356) | 1356 | `"                \"provider\": \"bing_rss\","` | — |
| [SRC-1AE03B9EC3-L001357](../../agents/web_agent.py#L1357) | 1357 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001358](../../agents/web_agent.py#L1358) | 1358 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001359](../../agents/web_agent.py#L1359) | 1359 | `"                \"published_at\": _clean_text(fields.get(\"pubDate\", \"\"), 80),"` | — |
| [SRC-1AE03B9EC3-L001360](../../agents/web_agent.py#L1360) | 1360 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001361](../../agents/web_agent.py#L1361) | 1361 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001362](../../agents/web_agent.py#L1362) | 1362 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001363](../../agents/web_agent.py#L1363) | 1363 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001364](../../agents/web_agent.py#L1364) | 1364 | `""` | — |
| [SRC-1AE03B9EC3-L001365](../../agents/web_agent.py#L1365) | 1365 | `"    def _search_deepseek_api(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001366](../../agents/web_agent.py#L1366) | 1366 | `"        \"\"\"Use DeepSeek's optional Search API as a comparison provider, never by default.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001367](../../agents/web_agent.py#L1367) | 1367 | `"        api_key = os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001368](../../agents/web_agent.py#L1368) | 1368 | `"        if not api_key:"` | — |
| [SRC-1AE03B9EC3-L001369](../../agents/web_agent.py#L1369) | 1369 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001370](../../agents/web_agent.py#L1370) | 1370 | `"        import httpx"` | — |
| [SRC-1AE03B9EC3-L001371](../../agents/web_agent.py#L1371) | 1371 | `""` | — |
| [SRC-1AE03B9EC3-L001372](../../agents/web_agent.py#L1372) | 1372 | `"        response = httpx.post("` | — |
| [SRC-1AE03B9EC3-L001373](../../agents/web_agent.py#L1373) | 1373 | `"            \"https://api.deepseek.com/v1/tools/search\","` | — |
| [SRC-1AE03B9EC3-L001374](../../agents/web_agent.py#L1374) | 1374 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001375](../../agents/web_agent.py#L1375) | 1375 | `"                \"Authorization\": \"Bearer \" + api_key,"` | — |
| [SRC-1AE03B9EC3-L001376](../../agents/web_agent.py#L1376) | 1376 | `"                \"Content-Type\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001377](../../agents/web_agent.py#L1377) | 1377 | `"                \"Accept\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001378](../../agents/web_agent.py#L1378) | 1378 | `"                \"User-Agent\": \"OmaraiResearchAgent/1.0\","` | — |
| [SRC-1AE03B9EC3-L001379](../../agents/web_agent.py#L1379) | 1379 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001380](../../agents/web_agent.py#L1380) | 1380 | `"            json={"` | — |
| [SRC-1AE03B9EC3-L001381](../../agents/web_agent.py#L1381) | 1381 | `"                \"query\": _normalize_search_query(query)[:128] or \"public web search\","` | — |
| [SRC-1AE03B9EC3-L001382](../../agents/web_agent.py#L1382) | 1382 | `"                \"count\": min(MAX_PROVIDER_RESULTS, 10),"` | — |
| [SRC-1AE03B9EC3-L001383](../../agents/web_agent.py#L1383) | 1383 | `"                \"need_content\": False,"` | — |
| [SRC-1AE03B9EC3-L001384](../../agents/web_agent.py#L1384) | 1384 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001385](../../agents/web_agent.py#L1385) | 1385 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001386](../../agents/web_agent.py#L1386) | 1386 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001387](../../agents/web_agent.py#L1387) | 1387 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001388](../../agents/web_agent.py#L1388) | 1388 | `"        response.raise_for_status()"` | — |
| [SRC-1AE03B9EC3-L001389](../../agents/web_agent.py#L1389) | 1389 | `"        payload = response.json()"` | — |
| [SRC-1AE03B9EC3-L001390](../../agents/web_agent.py#L1390) | 1390 | `"        results = payload.get(\"results\", []) if isinstance(payload, dict) else []"` | — |
| [SRC-1AE03B9EC3-L001391](../../agents/web_agent.py#L1391) | 1391 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001392](../../agents/web_agent.py#L1392) | 1392 | `"        for item in results if isinstance(results, list) else []:"` | — |
| [SRC-1AE03B9EC3-L001393](../../agents/web_agent.py#L1393) | 1393 | `"            if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L001394](../../agents/web_agent.py#L1394) | 1394 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001395](../../agents/web_agent.py#L1395) | 1395 | `"            url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001396](../../agents/web_agent.py#L1396) | 1396 | `"            if not url or _blocked_source_url(url):"` | — |
| [SRC-1AE03B9EC3-L001397](../../agents/web_agent.py#L1397) | 1397 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001398](../../agents/web_agent.py#L1398) | 1398 | `"            title = _clean_text(item.get(\"title\", \"\"), 300)"` | — |
| [SRC-1AE03B9EC3-L001399](../../agents/web_agent.py#L1399) | 1399 | `"            summary = item.get(\"summary\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001400](../../agents/web_agent.py#L1400) | 1400 | `"            snippet = item.get(\"snippet\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001401](../../agents/web_agent.py#L1401) | 1401 | `"            if isinstance(summary, str) and summary.strip():"` | — |
| [SRC-1AE03B9EC3-L001402](../../agents/web_agent.py#L1402) | 1402 | `"                snippet = summary"` | — |
| [SRC-1AE03B9EC3-L001403](../../agents/web_agent.py#L1403) | 1403 | `"            if not title or not isinstance(snippet, str) or not snippet.strip():"` | — |
| [SRC-1AE03B9EC3-L001404](../../agents/web_agent.py#L1404) | 1404 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001405](../../agents/web_agent.py#L1405) | 1405 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001406](../../agents/web_agent.py#L1406) | 1406 | `"                \"title\": title,"` | — |
| [SRC-1AE03B9EC3-L001407](../../agents/web_agent.py#L1407) | 1407 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001408](../../agents/web_agent.py#L1408) | 1408 | `"                \"snippet\": _clean_text(snippet, 1600),"` | — |
| [SRC-1AE03B9EC3-L001409](../../agents/web_agent.py#L1409) | 1409 | `"                \"provider\": \"deepseek_search_api\","` | — |
| [SRC-1AE03B9EC3-L001410](../../agents/web_agent.py#L1410) | 1410 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001411](../../agents/web_agent.py#L1411) | 1411 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001412](../../agents/web_agent.py#L1412) | 1412 | `"                \"published_at\": _clean_text(item.get(\"date\", \"\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L001413](../../agents/web_agent.py#L1413) | 1413 | `"                \"publisher_name\": _clean_text(item.get(\"site_name\", \"\") or \"\", 200),"` | — |
| [SRC-1AE03B9EC3-L001414](../../agents/web_agent.py#L1414) | 1414 | `"                \"provider_rerank_score\": item.get(\"rerank_score\"),"` | — |
| [SRC-1AE03B9EC3-L001415](../../agents/web_agent.py#L1415) | 1415 | `"                \"provider_authority_tier\": item.get(\"authority\"),"` | — |
| [SRC-1AE03B9EC3-L001416](../../agents/web_agent.py#L1416) | 1416 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001417](../../agents/web_agent.py#L1417) | 1417 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001418](../../agents/web_agent.py#L1418) | 1418 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001419](../../agents/web_agent.py#L1419) | 1419 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001420](../../agents/web_agent.py#L1420) | 1420 | `""` | — |
| [SRC-1AE03B9EC3-L001421](../../agents/web_agent.py#L1421) | 1421 | `"    def _reset_deepseek_search_budget(self) -> None:"` | — |
| [SRC-1AE03B9EC3-L001422](../../agents/web_agent.py#L1422) | 1422 | `"        \"\"\"Reset the bounded optional Search API request budget for one operation.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001423](../../agents/web_agent.py#L1423) | 1423 | `"        with self._deepseek_budget_lock:"` | — |
| [SRC-1AE03B9EC3-L001424](../../agents/web_agent.py#L1424) | 1424 | `"            self._deepseek_search_requests_reserved = 0"` | — |
| [SRC-1AE03B9EC3-L001425](../../agents/web_agent.py#L1425) | 1425 | `""` | — |
| [SRC-1AE03B9EC3-L001426](../../agents/web_agent.py#L1426) | 1426 | `"    def _reserve_deepseek_search_request(self) -> bool:"` | — |
| [SRC-1AE03B9EC3-L001427](../../agents/web_agent.py#L1427) | 1427 | `"        \"\"\"Reserve one paid search request before concurrent queries invoke the provider.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001428](../../agents/web_agent.py#L1428) | 1428 | `"        if not os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001429](../../agents/web_agent.py#L1429) | 1429 | `"            return False"` | — |
| [SRC-1AE03B9EC3-L001430](../../agents/web_agent.py#L1430) | 1430 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001431](../../agents/web_agent.py#L1431) | 1431 | `"            configured_budget = int("` | — |
| [SRC-1AE03B9EC3-L001432](../../agents/web_agent.py#L1432) | 1432 | `"                os.getenv(\"OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET\", \"1\").strip()"` | — |
| [SRC-1AE03B9EC3-L001433](../../agents/web_agent.py#L1433) | 1433 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001434](../../agents/web_agent.py#L1434) | 1434 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L001435](../../agents/web_agent.py#L1435) | 1435 | `"            configured_budget = 1"` | — |
| [SRC-1AE03B9EC3-L001436](../../agents/web_agent.py#L1436) | 1436 | `"        budget = max(0, min(configured_budget, 3))"` | — |
| [SRC-1AE03B9EC3-L001437](../../agents/web_agent.py#L1437) | 1437 | `"        with self._deepseek_budget_lock:"` | — |
| [SRC-1AE03B9EC3-L001438](../../agents/web_agent.py#L1438) | 1438 | `"            if self._deepseek_search_requests_reserved >= budget:"` | — |
| [SRC-1AE03B9EC3-L001439](../../agents/web_agent.py#L1439) | 1439 | `"                return False"` | — |
| [SRC-1AE03B9EC3-L001440](../../agents/web_agent.py#L1440) | 1440 | `"            self._deepseek_search_requests_reserved += 1"` | — |
| [SRC-1AE03B9EC3-L001441](../../agents/web_agent.py#L1441) | 1441 | `"            return True"` | — |
| [SRC-1AE03B9EC3-L001442](../../agents/web_agent.py#L1442) | 1442 | `""` | — |
| [SRC-1AE03B9EC3-L001443](../../agents/web_agent.py#L1443) | 1443 | `"    def _search_web(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001444](../../agents/web_agent.py#L1444) | 1444 | `"        \"\"\"Run configured search connectors concurrently with isolated failures and relevance checks.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001445](../../agents/web_agent.py#L1445) | 1445 | `"        from agents.research import detect_freshness"` | — |
| [SRC-1AE03B9EC3-L001446](../../agents/web_agent.py#L1446) | 1446 | `""` | — |
| [SRC-1AE03B9EC3-L001447](../../agents/web_agent.py#L1447) | 1447 | `"        query = compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L001448](../../agents/web_agent.py#L1448) | 1448 | `"        if not query:"` | — |
| [SRC-1AE03B9EC3-L001449](../../agents/web_agent.py#L1449) | 1449 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001450](../../agents/web_agent.py#L1450) | 1450 | `"        search_query = _normalize_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L001451](../../agents/web_agent.py#L1451) | 1451 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L001452](../../agents/web_agent.py#L1452) | 1452 | `"        if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L001453](../../agents/web_agent.py#L1453) | 1453 | `"            budget.reserve(\"search_queries\")"` | — |
| [SRC-1AE03B9EC3-L001454](../../agents/web_agent.py#L1454) | 1454 | `"        adapters: list[tuple[str, Any]] = ["` | — |
| [SRC-1AE03B9EC3-L001455](../../agents/web_agent.py#L1455) | 1455 | `"            (\"duckduckgo_html\", self._search_duckduckgo_html),"` | — |
| [SRC-1AE03B9EC3-L001456](../../agents/web_agent.py#L1456) | 1456 | `"            (\"bing_rss\", self._search_bing_rss),"` | — |
| [SRC-1AE03B9EC3-L001457](../../agents/web_agent.py#L1457) | 1457 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L001458](../../agents/web_agent.py#L1458) | 1458 | `"        # Experimental opt-in only: DeepSeek Search is billed per successful request."` | — |
| [SRC-1AE03B9EC3-L001459](../../agents/web_agent.py#L1459) | 1459 | `"        # Do not promote it to primary without a measured comparison."` | — |
| [SRC-1AE03B9EC3-L001460](../../agents/web_agent.py#L1460) | 1460 | `"        if not os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001461](../../agents/web_agent.py#L1461) | 1461 | `"            self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001462](../../agents/web_agent.py#L1462) | 1462 | `"                \"deepseek_search_api\", search_query, \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001463](../../agents/web_agent.py#L1463) | 1463 | `"                error=\"DEEPSEEK_SEARCH_API_KEY is not set\","` | — |
| [SRC-1AE03B9EC3-L001464](../../agents/web_agent.py#L1464) | 1464 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001465](../../agents/web_agent.py#L1465) | 1465 | `"        elif self._reserve_deepseek_search_request():"` | — |
| [SRC-1AE03B9EC3-L001466](../../agents/web_agent.py#L1466) | 1466 | `"            adapters.append((\"deepseek_search_api\", self._search_deepseek_api))"` | — |
| [SRC-1AE03B9EC3-L001467](../../agents/web_agent.py#L1467) | 1467 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001468](../../agents/web_agent.py#L1468) | 1468 | `"            self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001469](../../agents/web_agent.py#L1469) | 1469 | `"                \"deepseek_search_api\", search_query, \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L001470](../../agents/web_agent.py#L1470) | 1470 | `"                error=\"per-operation DeepSeek Search request budget exhausted\","` | — |
| [SRC-1AE03B9EC3-L001471](../../agents/web_agent.py#L1471) | 1471 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001472](../../agents/web_agent.py#L1472) | 1472 | `"        if os.getenv(\"BRAVE_SEARCH_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001473](../../agents/web_agent.py#L1473) | 1473 | `"            adapters.append((\"brave_search_api\", self._search_brave))"` | — |
| [SRC-1AE03B9EC3-L001474](../../agents/web_agent.py#L1474) | 1474 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001475](../../agents/web_agent.py#L1475) | 1475 | `"            self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001476](../../agents/web_agent.py#L1476) | 1476 | `"                \"brave_search_api\", search_query, \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001477](../../agents/web_agent.py#L1477) | 1477 | `"                error=\"BRAVE_SEARCH_API_KEY is not set\","` | — |
| [SRC-1AE03B9EC3-L001478](../../agents/web_agent.py#L1478) | 1478 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001479](../../agents/web_agent.py#L1479) | 1479 | `"        if os.getenv(\"TAVILY_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001480](../../agents/web_agent.py#L1480) | 1480 | `"            adapters.append((\"tavily_search_api\", self._search_tavily))"` | — |
| [SRC-1AE03B9EC3-L001481](../../agents/web_agent.py#L1481) | 1481 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001482](../../agents/web_agent.py#L1482) | 1482 | `"            self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001483](../../agents/web_agent.py#L1483) | 1483 | `"                \"tavily_search_api\", search_query, \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001484](../../agents/web_agent.py#L1484) | 1484 | `"                error=\"TAVILY_API_KEY is not set\","` | — |
| [SRC-1AE03B9EC3-L001485](../../agents/web_agent.py#L1485) | 1485 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001486](../../agents/web_agent.py#L1486) | 1486 | `"        if detect_freshness(search_query):"` | — |
| [SRC-1AE03B9EC3-L001487](../../agents/web_agent.py#L1487) | 1487 | `"            adapters.append((\"google_news_rss\", self._search_news))"` | — |
| [SRC-1AE03B9EC3-L001488](../../agents/web_agent.py#L1488) | 1488 | `""` | — |
| [SRC-1AE03B9EC3-L001489](../../agents/web_agent.py#L1489) | 1489 | `"        async def run_one(name: str, method: Any) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001490](../../agents/web_agent.py#L1490) | 1490 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001491](../../agents/web_agent.py#L1491) | 1491 | `"                if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L001492](../../agents/web_agent.py#L1492) | 1492 | `"                    budget.reserve(\"search_calls\")"` | — |
| [SRC-1AE03B9EC3-L001493](../../agents/web_agent.py#L1493) | 1493 | `"                provider_timeout = self._effective_timeout(10.0)"` | — |
| [SRC-1AE03B9EC3-L001494](../../agents/web_agent.py#L1494) | 1494 | `"                raw = await asyncio.wait_for("` | — |
| [SRC-1AE03B9EC3-L001495](../../agents/web_agent.py#L1495) | 1495 | `"                    asyncio.to_thread(method, search_query), timeout=provider_timeout"` | — |
| [SRC-1AE03B9EC3-L001496](../../agents/web_agent.py#L1496) | 1496 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001497](../../agents/web_agent.py#L1497) | 1497 | `"                if not isinstance(raw, list):"` | — |
| [SRC-1AE03B9EC3-L001498](../../agents/web_agent.py#L1498) | 1498 | `"                    raise TypeError(\"connector returned a non-list result\")"` | — |
| [SRC-1AE03B9EC3-L001499](../../agents/web_agent.py#L1499) | 1499 | `"                accepted: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001500](../../agents/web_agent.py#L1500) | 1500 | `"                rejected = 0"` | — |
| [SRC-1AE03B9EC3-L001501](../../agents/web_agent.py#L1501) | 1501 | `"                rejection_counts = {reason: 0 for reason in _PROVIDER_REJECTION_REASONS}"` | — |
| [SRC-1AE03B9EC3-L001502](../../agents/web_agent.py#L1502) | 1502 | `"                for item in raw:"` | — |
| [SRC-1AE03B9EC3-L001503](../../agents/web_agent.py#L1503) | 1503 | `"                    if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L001504](../../agents/web_agent.py#L1504) | 1504 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001505](../../agents/web_agent.py#L1505) | 1505 | `"                        rejection_counts[\"malformed_candidate\"] += 1"` | — |
| [SRC-1AE03B9EC3-L001506](../../agents/web_agent.py#L1506) | 1506 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001507](../../agents/web_agent.py#L1507) | 1507 | `"                    safe_url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001508](../../agents/web_agent.py#L1508) | 1508 | `"                    if not safe_url:"` | — |
| [SRC-1AE03B9EC3-L001509](../../agents/web_agent.py#L1509) | 1509 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001510](../../agents/web_agent.py#L1510) | 1510 | `"                        rejection_counts[\"invalid_url_or_unsafe_target\"] += 1"` | — |
| [SRC-1AE03B9EC3-L001511](../../agents/web_agent.py#L1511) | 1511 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001512](../../agents/web_agent.py#L1512) | 1512 | `"                    if _blocked_source_url(safe_url):"` | — |
| [SRC-1AE03B9EC3-L001513](../../agents/web_agent.py#L1513) | 1513 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001514](../../agents/web_agent.py#L1514) | 1514 | `"                        rejection_counts[\"blocked_domain\"] += 1"` | — |
| [SRC-1AE03B9EC3-L001515](../../agents/web_agent.py#L1515) | 1515 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001516](../../agents/web_agent.py#L1516) | 1516 | `"                    normalized_item = dict(item)"` | — |
| [SRC-1AE03B9EC3-L001517](../../agents/web_agent.py#L1517) | 1517 | `"                    normalized_item[\"url\"] = safe_url"` | — |
| [SRC-1AE03B9EC3-L001518](../../agents/web_agent.py#L1518) | 1518 | `"                    normalized_item.setdefault(\"provider\", name)"` | — |
| [SRC-1AE03B9EC3-L001519](../../agents/web_agent.py#L1519) | 1519 | `"                    normalized_item.setdefault(\"search_query\", search_query)"` | — |
| [SRC-1AE03B9EC3-L001520](../../agents/web_agent.py#L1520) | 1520 | `"                    evidence = \" \".join(str(normalized_item.get(k) or \"\") for k in (\"title\", \"snippet\"))"` | — |
| [SRC-1AE03B9EC3-L001521](../../agents/web_agent.py#L1521) | 1521 | `"                    if _relevance_ratio(search_query, evidence) < _minimum_relevance_ratio(search_query):"` | — |
| [SRC-1AE03B9EC3-L001522](../../agents/web_agent.py#L1522) | 1522 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001523](../../agents/web_agent.py#L1523) | 1523 | `"                        rejection_counts[\"relevance_below_threshold\"] += 1"` | — |
| [SRC-1AE03B9EC3-L001524](../../agents/web_agent.py#L1524) | 1524 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001525](../../agents/web_agent.py#L1525) | 1525 | `"                    accepted.append(normalized_item)"` | — |
| [SRC-1AE03B9EC3-L001526](../../agents/web_agent.py#L1526) | 1526 | `"                if accepted:"` | — |
| [SRC-1AE03B9EC3-L001527](../../agents/web_agent.py#L1527) | 1527 | `"                    status = \"ok\""` | — |
| [SRC-1AE03B9EC3-L001528](../../agents/web_agent.py#L1528) | 1528 | `"                    error = None"` | — |
| [SRC-1AE03B9EC3-L001529](../../agents/web_agent.py#L1529) | 1529 | `"                elif raw:"` | — |
| [SRC-1AE03B9EC3-L001530](../../agents/web_agent.py#L1530) | 1530 | `"                    status = \"filtered_all\""` | — |
| [SRC-1AE03B9EC3-L001531](../../agents/web_agent.py#L1531) | 1531 | `"                    details = \", \".join("` | — |
| [SRC-1AE03B9EC3-L001532](../../agents/web_agent.py#L1532) | 1532 | `"                        f\"{reason}={count}\" for reason, count in rejection_counts.items() if count"` | — |
| [SRC-1AE03B9EC3-L001533](../../agents/web_agent.py#L1533) | 1533 | `"                    ) or \"no reason counters recorded\""` | — |
| [SRC-1AE03B9EC3-L001534](../../agents/web_agent.py#L1534) | 1534 | `"                    error = f\"all candidates rejected; {details}\""` | — |
| [SRC-1AE03B9EC3-L001535](../../agents/web_agent.py#L1535) | 1535 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001536](../../agents/web_agent.py#L1536) | 1536 | `"                    status = \"no_results\""` | — |
| [SRC-1AE03B9EC3-L001537](../../agents/web_agent.py#L1537) | 1537 | `"                    error = \"connector returned no parseable results\""` | — |
| [SRC-1AE03B9EC3-L001538](../../agents/web_agent.py#L1538) | 1538 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001539](../../agents/web_agent.py#L1539) | 1539 | `"                    name, search_query, status, len(raw), rejected, error,"` | — |
| [SRC-1AE03B9EC3-L001540](../../agents/web_agent.py#L1540) | 1540 | `"                    accepted_count=len(accepted), rejection_counts=rejection_counts if raw else None,"` | — |
| [SRC-1AE03B9EC3-L001541](../../agents/web_agent.py#L1541) | 1541 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001542](../../agents/web_agent.py#L1542) | 1542 | `"                return accepted"` | — |
| [SRC-1AE03B9EC3-L001543](../../agents/web_agent.py#L1543) | 1543 | `"            except RequestBudgetExceeded as exc:"` | — |
| [SRC-1AE03B9EC3-L001544](../../agents/web_agent.py#L1544) | 1544 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001545](../../agents/web_agent.py#L1545) | 1545 | `"                    name, search_query, \"budget_exhausted\", error=str(exc)"` | — |
| [SRC-1AE03B9EC3-L001546](../../agents/web_agent.py#L1546) | 1546 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001547](../../agents/web_agent.py#L1547) | 1547 | `"            except TimeoutError:"` | — |
| [SRC-1AE03B9EC3-L001548](../../agents/web_agent.py#L1548) | 1548 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001549](../../agents/web_agent.py#L1549) | 1549 | `"                    name, search_query, \"timeout\", error=\"provider exceeded its bounded request timeout\""` | — |
| [SRC-1AE03B9EC3-L001550](../../agents/web_agent.py#L1550) | 1550 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001551](../../agents/web_agent.py#L1551) | 1551 | `"            except Exception as exc:  # noqa: BLE001 - isolate a connector without leaking provider bodies/secrets"` | — |
| [SRC-1AE03B9EC3-L001552](../../agents/web_agent.py#L1552) | 1552 | `"                detail = f\"{type(exc).__name__}: {exc}\" if isinstance(exc, RuntimeError) else type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L001553](../../agents/web_agent.py#L1553) | 1553 | `"                status = \"failed\""` | — |
| [SRC-1AE03B9EC3-L001554](../../agents/web_agent.py#L1554) | 1554 | `"                status_match = re.search(r\"(?i)\\bHTTP\\s+(\\d{3})\\b\", str(exc))"` | — |
| [SRC-1AE03B9EC3-L001555](../../agents/web_agent.py#L1555) | 1555 | `"                if status_match:"` | — |
| [SRC-1AE03B9EC3-L001556](../../agents/web_agent.py#L1556) | 1556 | `"                    status_code = int(status_match.group(1))"` | — |
| [SRC-1AE03B9EC3-L001557](../../agents/web_agent.py#L1557) | 1557 | `"                    if status_code == 429:"` | — |
| [SRC-1AE03B9EC3-L001558](../../agents/web_agent.py#L1558) | 1558 | `"                        status = \"rate_limited\""` | — |
| [SRC-1AE03B9EC3-L001559](../../agents/web_agent.py#L1559) | 1559 | `"                    elif status_code in {401, 403}:"` | — |
| [SRC-1AE03B9EC3-L001560](../../agents/web_agent.py#L1560) | 1560 | `"                        status = \"unauthorized\""` | — |
| [SRC-1AE03B9EC3-L001561](../../agents/web_agent.py#L1561) | 1561 | `"                    elif status_code == 202 or 300 <= status_code < 600:"` | — |
| [SRC-1AE03B9EC3-L001562](../../agents/web_agent.py#L1562) | 1562 | `"                        # Do not bypass anti-bot/challenge responses; mark the provider degraded."` | — |
| [SRC-1AE03B9EC3-L001563](../../agents/web_agent.py#L1563) | 1563 | `"                        status = \"http_error\""` | — |
| [SRC-1AE03B9EC3-L001564](../../agents/web_agent.py#L1564) | 1564 | `"                self._record_provider_diagnostic(name, search_query, status, error=detail)"` | — |
| [SRC-1AE03B9EC3-L001565](../../agents/web_agent.py#L1565) | 1565 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001566](../../agents/web_agent.py#L1566) | 1566 | `""` | — |
| [SRC-1AE03B9EC3-L001567](../../agents/web_agent.py#L1567) | 1567 | `"        async def run_all() -> list[list[dict[str, Any]]]:"` | — |
| [SRC-1AE03B9EC3-L001568](../../agents/web_agent.py#L1568) | 1568 | `"            return await asyncio.gather(*(run_one(name, method) for name, method in adapters))"` | — |
| [SRC-1AE03B9EC3-L001569](../../agents/web_agent.py#L1569) | 1569 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001570](../../agents/web_agent.py#L1570) | 1570 | `"            provider_batches = asyncio.run(run_all())"` | — |
| [SRC-1AE03B9EC3-L001571](../../agents/web_agent.py#L1571) | 1571 | `"            combined = [item for batch in provider_batches for item in batch]"` | — |
| [SRC-1AE03B9EC3-L001572](../../agents/web_agent.py#L1572) | 1572 | `"            # Scholarly fallback only for explicit research-shaped queries; reuse"` | — |
| [SRC-1AE03B9EC3-L001573](../../agents/web_agent.py#L1573) | 1573 | `"            # run_one so budget, timeouts, public-URL/SSRF, blocklist and relevance"` | — |
| [SRC-1AE03B9EC3-L001574](../../agents/web_agent.py#L1574) | 1574 | `"            # validation are identical to ordinary search connectors."` | — |
| [SRC-1AE03B9EC3-L001575](../../agents/web_agent.py#L1575) | 1575 | `"            academic_markers = ("` | — |
| [SRC-1AE03B9EC3-L001576](../../agents/web_agent.py#L1576) | 1576 | `"                \"دراسة علمية\", \"دراسات\", \"ابحاث\", \"أبحاث\", \"بحث علمي\","` | — |
| [SRC-1AE03B9EC3-L001577](../../agents/web_agent.py#L1577) | 1577 | `"                \"ورقة علمية\", \"أوراق علمية\", \"academic\", \"research\","` | — |
| [SRC-1AE03B9EC3-L001578](../../agents/web_agent.py#L1578) | 1578 | `"                \"scientific study\", \"research paper\", \"peer reviewed\","` | — |
| [SRC-1AE03B9EC3-L001579](../../agents/web_agent.py#L1579) | 1579 | `"                \"peer-reviewed\", \"scholarly\", \"literature review\","` | — |
| [SRC-1AE03B9EC3-L001580](../../agents/web_agent.py#L1580) | 1580 | `"                \"systematic review\", \"arxiv\", \"openalex\", \"crossref\","` | — |
| [SRC-1AE03B9EC3-L001581](../../agents/web_agent.py#L1581) | 1581 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001582](../../agents/web_agent.py#L1582) | 1582 | `"            if len(combined) < 3 and any(marker in search_query.casefold() for marker in academic_markers):"` | — |
| [SRC-1AE03B9EC3-L001583](../../agents/web_agent.py#L1583) | 1583 | `"                academic_adapters: list[tuple[str, Any]] = ["` | — |
| [SRC-1AE03B9EC3-L001584](../../agents/web_agent.py#L1584) | 1584 | `"                    (\"openalex\", lambda q: search_openalex(q, limit=3)),"` | — |
| [SRC-1AE03B9EC3-L001585](../../agents/web_agent.py#L1585) | 1585 | `"                    (\"arxiv\", lambda q: search_arxiv(q, limit=3)),"` | — |
| [SRC-1AE03B9EC3-L001586](../../agents/web_agent.py#L1586) | 1586 | `"                    (\"crossref\", lambda q: search_crossref(q, limit=3)),"` | — |
| [SRC-1AE03B9EC3-L001587](../../agents/web_agent.py#L1587) | 1587 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L001588](../../agents/web_agent.py#L1588) | 1588 | `""` | — |
| [SRC-1AE03B9EC3-L001589](../../agents/web_agent.py#L1589) | 1589 | `"                async def run_academic_all() -> list[list[dict[str, Any]]]:"` | — |
| [SRC-1AE03B9EC3-L001590](../../agents/web_agent.py#L1590) | 1590 | `"                    return await asyncio.gather("` | — |
| [SRC-1AE03B9EC3-L001591](../../agents/web_agent.py#L1591) | 1591 | `"                        *(run_one(name, method) for name, method in academic_adapters)"` | — |
| [SRC-1AE03B9EC3-L001592](../../agents/web_agent.py#L1592) | 1592 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L001593](../../agents/web_agent.py#L1593) | 1593 | `""` | — |
| [SRC-1AE03B9EC3-L001594](../../agents/web_agent.py#L1594) | 1594 | `"                provider_batches.extend(asyncio.run(run_academic_all()))"` | — |
| [SRC-1AE03B9EC3-L001595](../../agents/web_agent.py#L1595) | 1595 | `"        except RuntimeError as exc:"` | — |
| [SRC-1AE03B9EC3-L001596](../../agents/web_agent.py#L1596) | 1596 | `"            # This method is synchronous by contract; the HTTP server invokes it in worker threads."` | — |
| [SRC-1AE03B9EC3-L001597](../../agents/web_agent.py#L1597) | 1597 | `"            raise RuntimeError(\"تعذر تشغيل مجدول موصلات البحث.\") from exc"` | — |
| [SRC-1AE03B9EC3-L001598](../../agents/web_agent.py#L1598) | 1598 | `"        combined = [item for batch in provider_batches for item in batch]"` | — |
| [SRC-1AE03B9EC3-L001599](../../agents/web_agent.py#L1599) | 1599 | `"        # De-duplicate repeated URLs before ranking/fusion."` | — |
| [SRC-1AE03B9EC3-L001600](../../agents/web_agent.py#L1600) | 1600 | `"        unique: dict[str, dict[str, Any]] = {}"` | — |
| [SRC-1AE03B9EC3-L001601](../../agents/web_agent.py#L1601) | 1601 | `"        for item in combined:"` | — |
| [SRC-1AE03B9EC3-L001602](../../agents/web_agent.py#L1602) | 1602 | `"            key = item[\"url\"].split(\"#\", 1)[0].rstrip(\"/\")"` | — |
| [SRC-1AE03B9EC3-L001603](../../agents/web_agent.py#L1603) | 1603 | `"            if key not in unique or len(str(item.get(\"snippet\") or \"\")) > len(str(unique[key].get(\"snippet\") or \"\")):"` | — |
| [SRC-1AE03B9EC3-L001604](../../agents/web_agent.py#L1604) | 1604 | `"                unique[key] = item"` | — |
| [SRC-1AE03B9EC3-L001605](../../agents/web_agent.py#L1605) | 1605 | `"        if not unique:"` | — |
| [SRC-1AE03B9EC3-L001606](../../agents/web_agent.py#L1606) | 1606 | `"            raise RuntimeError(\"لم تُرجع موصلات البحث نتائج مرتبطة وقابلة للاستخدام.\")"` | — |
| [SRC-1AE03B9EC3-L001607](../../agents/web_agent.py#L1607) | 1607 | `"        return list(unique.values())"` | — |
| [SRC-1AE03B9EC3-L001608](../../agents/web_agent.py#L1608) | 1608 | `""` | — |
| [SRC-1AE03B9EC3-L001609](../../agents/web_agent.py#L1609) | 1609 | `"    def _reserve_search_call(self) -> None:"` | — |
| [SRC-1AE03B9EC3-L001610](../../agents/web_agent.py#L1610) | 1610 | `"        \"\"\"Reserve one outbound search/social-provider request before network I/O.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001611](../../agents/web_agent.py#L1611) | 1611 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L001612](../../agents/web_agent.py#L1612) | 1612 | `"        if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L001613](../../agents/web_agent.py#L1613) | 1613 | `"            budget.reserve(\"search_calls\")"` | — |
| [SRC-1AE03B9EC3-L001614](../../agents/web_agent.py#L1614) | 1614 | `""` | — |
| [SRC-1AE03B9EC3-L001615](../../agents/web_agent.py#L1615) | 1615 | `"    def _search_brave(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001616](../../agents/web_agent.py#L1616) | 1616 | `"        \"\"\"Use Brave's official web-search API when the operator provides an API key.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001617](../../agents/web_agent.py#L1617) | 1617 | `"        api_key = os.getenv(\"BRAVE_SEARCH_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001618](../../agents/web_agent.py#L1618) | 1618 | `"        if not api_key:"` | — |
| [SRC-1AE03B9EC3-L001619](../../agents/web_agent.py#L1619) | 1619 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001620](../../agents/web_agent.py#L1620) | 1620 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001621](../../agents/web_agent.py#L1621) | 1621 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L001622](../../agents/web_agent.py#L1622) | 1622 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L001623](../../agents/web_agent.py#L1623) | 1623 | `"            raise AgentDependencyError(\"حزمة httpx غير مثبتة.\") from exc"` | — |
| [SRC-1AE03B9EC3-L001624](../../agents/web_agent.py#L1624) | 1624 | `"        is_arabic = bool(re.search(r\"[\\u0600-\\u06FF]\", query))"` | — |
| [SRC-1AE03B9EC3-L001625](../../agents/web_agent.py#L1625) | 1625 | `"        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001626](../../agents/web_agent.py#L1626) | 1626 | `"            \"https://api.search.brave.com/res/v1/web/search\","` | — |
| [SRC-1AE03B9EC3-L001627](../../agents/web_agent.py#L1627) | 1627 | `"            params={"` | — |
| [SRC-1AE03B9EC3-L001628](../../agents/web_agent.py#L1628) | 1628 | `"                \"q\": query[:600],"` | — |
| [SRC-1AE03B9EC3-L001629](../../agents/web_agent.py#L1629) | 1629 | `"                \"count\": MAX_PROVIDER_RESULTS,"` | — |
| [SRC-1AE03B9EC3-L001630](../../agents/web_agent.py#L1630) | 1630 | `"                \"country\": \"EG\" if is_arabic else \"US\","` | — |
| [SRC-1AE03B9EC3-L001631](../../agents/web_agent.py#L1631) | 1631 | `"                \"search_lang\": \"ar\" if is_arabic else \"en\","` | — |
| [SRC-1AE03B9EC3-L001632](../../agents/web_agent.py#L1632) | 1632 | `"                \"extra_snippets\": \"true\","` | — |
| [SRC-1AE03B9EC3-L001633](../../agents/web_agent.py#L1633) | 1633 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001634](../../agents/web_agent.py#L1634) | 1634 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001635](../../agents/web_agent.py#L1635) | 1635 | `"                \"Accept\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001636](../../agents/web_agent.py#L1636) | 1636 | `"                \"X-Subscription-Token\": api_key,"` | — |
| [SRC-1AE03B9EC3-L001637](../../agents/web_agent.py#L1637) | 1637 | `"                \"User-Agent\": \"OmaraiResearchAgent/1.0\","` | — |
| [SRC-1AE03B9EC3-L001638](../../agents/web_agent.py#L1638) | 1638 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001639](../../agents/web_agent.py#L1639) | 1639 | `"            timeout=self._effective_timeout(8.5),"` | — |
| [SRC-1AE03B9EC3-L001640](../../agents/web_agent.py#L1640) | 1640 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001641](../../agents/web_agent.py#L1641) | 1641 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001642](../../agents/web_agent.py#L1642) | 1642 | `"        response.raise_for_status()"` | — |
| [SRC-1AE03B9EC3-L001643](../../agents/web_agent.py#L1643) | 1643 | `"        payload = response.json()"` | — |
| [SRC-1AE03B9EC3-L001644](../../agents/web_agent.py#L1644) | 1644 | `"        web_results = payload.get(\"web\", {}).get(\"results\", [])"` | — |
| [SRC-1AE03B9EC3-L001645](../../agents/web_agent.py#L1645) | 1645 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001646](../../agents/web_agent.py#L1646) | 1646 | `"        for item in web_results if isinstance(web_results, list) else []:"` | — |
| [SRC-1AE03B9EC3-L001647](../../agents/web_agent.py#L1647) | 1647 | `"            if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L001648](../../agents/web_agent.py#L1648) | 1648 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001649](../../agents/web_agent.py#L1649) | 1649 | `"            url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001650](../../agents/web_agent.py#L1650) | 1650 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001651](../../agents/web_agent.py#L1651) | 1651 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001652](../../agents/web_agent.py#L1652) | 1652 | `"            snippets = item.get(\"extra_snippets\", [])"` | — |
| [SRC-1AE03B9EC3-L001653](../../agents/web_agent.py#L1653) | 1653 | `"            extra = \" \".join(x for x in snippets if isinstance(x, str)) if isinstance(snippets, list) else \"\""` | — |
| [SRC-1AE03B9EC3-L001654](../../agents/web_agent.py#L1654) | 1654 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001655](../../agents/web_agent.py#L1655) | 1655 | `"                \"title\": _clean_text(item.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001656](../../agents/web_agent.py#L1656) | 1656 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001657](../../agents/web_agent.py#L1657) | 1657 | `"                \"snippet\": _clean_text(item.get(\"description\", \"\") + \" \" + extra, 1600),"` | — |
| [SRC-1AE03B9EC3-L001658](../../agents/web_agent.py#L1658) | 1658 | `"                \"provider\": \"brave_search_api\","` | — |
| [SRC-1AE03B9EC3-L001659](../../agents/web_agent.py#L1659) | 1659 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001660](../../agents/web_agent.py#L1660) | 1660 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001661](../../agents/web_agent.py#L1661) | 1661 | `"                \"published_at\": _clean_text(item.get(\"page_age\", \"\") or item.get(\"published_at\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001662](../../agents/web_agent.py#L1662) | 1662 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001663](../../agents/web_agent.py#L1663) | 1663 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001664](../../agents/web_agent.py#L1664) | 1664 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001665](../../agents/web_agent.py#L1665) | 1665 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001666](../../agents/web_agent.py#L1666) | 1666 | `""` | — |
| [SRC-1AE03B9EC3-L001667](../../agents/web_agent.py#L1667) | 1667 | `"    def _search_tavily(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001668](../../agents/web_agent.py#L1668) | 1668 | `"        \"\"\"Use Tavily's official search API for structured, extractable live web results.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001669](../../agents/web_agent.py#L1669) | 1669 | `"        api_key = os.getenv(\"TAVILY_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001670](../../agents/web_agent.py#L1670) | 1670 | `"        if not api_key:"` | — |
| [SRC-1AE03B9EC3-L001671](../../agents/web_agent.py#L1671) | 1671 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001672](../../agents/web_agent.py#L1672) | 1672 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001673](../../agents/web_agent.py#L1673) | 1673 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L001674](../../agents/web_agent.py#L1674) | 1674 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L001675](../../agents/web_agent.py#L1675) | 1675 | `"            raise AgentDependencyError(\"حزمة httpx غير مثبتة.\") from exc"` | — |
| [SRC-1AE03B9EC3-L001676](../../agents/web_agent.py#L1676) | 1676 | `"        from agents.research import detect_depth, detect_freshness"` | — |
| [SRC-1AE03B9EC3-L001677](../../agents/web_agent.py#L1677) | 1677 | `""` | — |
| [SRC-1AE03B9EC3-L001678](../../agents/web_agent.py#L1678) | 1678 | `"        response = httpx.post("` | — |
| [SRC-1AE03B9EC3-L001679](../../agents/web_agent.py#L1679) | 1679 | `"            \"https://api.tavily.com/search\","` | — |
| [SRC-1AE03B9EC3-L001680](../../agents/web_agent.py#L1680) | 1680 | `"            json={"` | — |
| [SRC-1AE03B9EC3-L001681](../../agents/web_agent.py#L1681) | 1681 | `"                \"api_key\": api_key,"` | — |
| [SRC-1AE03B9EC3-L001682](../../agents/web_agent.py#L1682) | 1682 | `"                \"query\": query[:500],"` | — |
| [SRC-1AE03B9EC3-L001683](../../agents/web_agent.py#L1683) | 1683 | `"                \"search_depth\": \"advanced\" if detect_depth(query) == \"deep\" else \"basic\","` | — |
| [SRC-1AE03B9EC3-L001684](../../agents/web_agent.py#L1684) | 1684 | `"                \"topic\": \"news\" if detect_freshness(query) else \"general\","` | — |
| [SRC-1AE03B9EC3-L001685](../../agents/web_agent.py#L1685) | 1685 | `"                \"max_results\": MAX_PROVIDER_RESULTS,"` | — |
| [SRC-1AE03B9EC3-L001686](../../agents/web_agent.py#L1686) | 1686 | `"                \"include_answer\": False,"` | — |
| [SRC-1AE03B9EC3-L001687](../../agents/web_agent.py#L1687) | 1687 | `"                \"include_raw_content\": False,"` | — |
| [SRC-1AE03B9EC3-L001688](../../agents/web_agent.py#L1688) | 1688 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001689](../../agents/web_agent.py#L1689) | 1689 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001690](../../agents/web_agent.py#L1690) | 1690 | `"                \"Accept\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001691](../../agents/web_agent.py#L1691) | 1691 | `"                \"Content-Type\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001692](../../agents/web_agent.py#L1692) | 1692 | `"                \"User-Agent\": \"OmaraiResearchAgent/1.0\","` | — |
| [SRC-1AE03B9EC3-L001693](../../agents/web_agent.py#L1693) | 1693 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001694](../../agents/web_agent.py#L1694) | 1694 | `"            timeout=self._effective_timeout(8.5),"` | — |
| [SRC-1AE03B9EC3-L001695](../../agents/web_agent.py#L1695) | 1695 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001696](../../agents/web_agent.py#L1696) | 1696 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001697](../../agents/web_agent.py#L1697) | 1697 | `"        response.raise_for_status()"` | — |
| [SRC-1AE03B9EC3-L001698](../../agents/web_agent.py#L1698) | 1698 | `"        payload = response.json()"` | — |
| [SRC-1AE03B9EC3-L001699](../../agents/web_agent.py#L1699) | 1699 | `"        search_results = payload.get(\"results\", [])"` | — |
| [SRC-1AE03B9EC3-L001700](../../agents/web_agent.py#L1700) | 1700 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001701](../../agents/web_agent.py#L1701) | 1701 | `"        for item in search_results if isinstance(search_results, list) else []:"` | — |
| [SRC-1AE03B9EC3-L001702](../../agents/web_agent.py#L1702) | 1702 | `"            if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L001703](../../agents/web_agent.py#L1703) | 1703 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001704](../../agents/web_agent.py#L1704) | 1704 | `"            url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001705](../../agents/web_agent.py#L1705) | 1705 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001706](../../agents/web_agent.py#L1706) | 1706 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001707](../../agents/web_agent.py#L1707) | 1707 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001708](../../agents/web_agent.py#L1708) | 1708 | `"                \"title\": _clean_text(item.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001709](../../agents/web_agent.py#L1709) | 1709 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001710](../../agents/web_agent.py#L1710) | 1710 | `"                \"snippet\": _clean_text(item.get(\"content\", \"\"), 1600),"` | — |
| [SRC-1AE03B9EC3-L001711](../../agents/web_agent.py#L1711) | 1711 | `"                \"provider\": \"tavily_search_api\","` | — |
| [SRC-1AE03B9EC3-L001712](../../agents/web_agent.py#L1712) | 1712 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001713](../../agents/web_agent.py#L1713) | 1713 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001714](../../agents/web_agent.py#L1714) | 1714 | `"                \"published_at\": _clean_text(item.get(\"published_date\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001715](../../agents/web_agent.py#L1715) | 1715 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001716](../../agents/web_agent.py#L1716) | 1716 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001717](../../agents/web_agent.py#L1717) | 1717 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001718](../../agents/web_agent.py#L1718) | 1718 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001719](../../agents/web_agent.py#L1719) | 1719 | `""` | — |
| [SRC-1AE03B9EC3-L001720](../../agents/web_agent.py#L1720) | 1720 | `"    def _search_news(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001721](../../agents/web_agent.py#L1721) | 1721 | `"        \"\"\"Read the public Google News RSS search feed for freshness-sensitive queries.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001722](../../agents/web_agent.py#L1722) | 1722 | `"        import xml.etree.ElementTree as ET"` | — |
| [SRC-1AE03B9EC3-L001723](../../agents/web_agent.py#L1723) | 1723 | `""` | — |
| [SRC-1AE03B9EC3-L001724](../../agents/web_agent.py#L1724) | 1724 | `"        import httpx"` | — |
| [SRC-1AE03B9EC3-L001725](../../agents/web_agent.py#L1725) | 1725 | `""` | — |
| [SRC-1AE03B9EC3-L001726](../../agents/web_agent.py#L1726) | 1726 | `"        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001727](../../agents/web_agent.py#L1727) | 1727 | `"            \"https://news.google.com/rss/search\","` | — |
| [SRC-1AE03B9EC3-L001728](../../agents/web_agent.py#L1728) | 1728 | `"            params={\"q\": query, \"hl\": \"ar\", \"gl\": \"EG\", \"ceid\": \"EG:ar\"},"` | — |
| [SRC-1AE03B9EC3-L001729](../../agents/web_agent.py#L1729) | 1729 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001730](../../agents/web_agent.py#L1730) | 1730 | `"                \"User-Agent\": \"OmaraiResearchBot/1.2\","` | — |
| [SRC-1AE03B9EC3-L001731](../../agents/web_agent.py#L1731) | 1731 | `"                \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001732](../../agents/web_agent.py#L1732) | 1732 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001733](../../agents/web_agent.py#L1733) | 1733 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001734](../../agents/web_agent.py#L1734) | 1734 | `"            # Refuse automatic redirects from public search endpoints; never fetch an"` | — |
| [SRC-1AE03B9EC3-L001735](../../agents/web_agent.py#L1735) | 1735 | `"            # unchecked redirect target as part of a provider search request."` | — |
| [SRC-1AE03B9EC3-L001736](../../agents/web_agent.py#L1736) | 1736 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001737](../../agents/web_agent.py#L1737) | 1737 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001738](../../agents/web_agent.py#L1738) | 1738 | `"        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001739](../../agents/web_agent.py#L1739) | 1739 | `"            raise RuntimeError(f\"HTTP {response.status_code}\")"` | — |
| [SRC-1AE03B9EC3-L001740](../../agents/web_agent.py#L1740) | 1740 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001741](../../agents/web_agent.py#L1741) | 1741 | `"            root = ET.fromstring(response.content)"` | — |
| [SRC-1AE03B9EC3-L001742](../../agents/web_agent.py#L1742) | 1742 | `"        except ET.ParseError as exc:"` | — |
| [SRC-1AE03B9EC3-L001743](../../agents/web_agent.py#L1743) | 1743 | `"            raise RuntimeError(\"invalid RSS XML\") from exc"` | — |
| [SRC-1AE03B9EC3-L001744](../../agents/web_agent.py#L1744) | 1744 | `"        results: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001745](../../agents/web_agent.py#L1745) | 1745 | `"        for item in root.iter():"` | — |
| [SRC-1AE03B9EC3-L001746](../../agents/web_agent.py#L1746) | 1746 | `"            if item.tag.rsplit(\"}\", 1)[-1] != \"item\":"` | — |
| [SRC-1AE03B9EC3-L001747](../../agents/web_agent.py#L1747) | 1747 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001748](../../agents/web_agent.py#L1748) | 1748 | `"            fields = {"` | — |
| [SRC-1AE03B9EC3-L001749](../../agents/web_agent.py#L1749) | 1749 | `"                child.tag.rsplit(\"}\", 1)[-1]: (child.text or \"\")"` | — |
| [SRC-1AE03B9EC3-L001750](../../agents/web_agent.py#L1750) | 1750 | `"                for child in item"` | — |
| [SRC-1AE03B9EC3-L001751](../../agents/web_agent.py#L1751) | 1751 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001752](../../agents/web_agent.py#L1752) | 1752 | `"            url = _public_http_url(fields.get(\"link\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001753](../../agents/web_agent.py#L1753) | 1753 | `"            if not url or _blocked_source_url(url):"` | — |
| [SRC-1AE03B9EC3-L001754](../../agents/web_agent.py#L1754) | 1754 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001755](../../agents/web_agent.py#L1755) | 1755 | `"            # Keep every parseable, safe candidate here. _search_web applies the"` | — |
| [SRC-1AE03B9EC3-L001756](../../agents/web_agent.py#L1756) | 1756 | `"            # shared relevance filter and records accepted/rejected counters."` | — |
| [SRC-1AE03B9EC3-L001757](../../agents/web_agent.py#L1757) | 1757 | `"            # Filtering again in this adapter mislabels a valid feed as no results."` | — |
| [SRC-1AE03B9EC3-L001758](../../agents/web_agent.py#L1758) | 1758 | `"            source_node = next("` | — |
| [SRC-1AE03B9EC3-L001759](../../agents/web_agent.py#L1759) | 1759 | `"                (child for child in item if child.tag.rsplit(\"}\", 1)[-1] == \"source\"),"` | — |
| [SRC-1AE03B9EC3-L001760](../../agents/web_agent.py#L1760) | 1760 | `"                None,"` | — |
| [SRC-1AE03B9EC3-L001761](../../agents/web_agent.py#L1761) | 1761 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001762](../../agents/web_agent.py#L1762) | 1762 | `"            publisher_url = _public_http_url("` | — |
| [SRC-1AE03B9EC3-L001763](../../agents/web_agent.py#L1763) | 1763 | `"                source_node.attrib.get(\"url\", \"\") if source_node is not None else \"\""` | — |
| [SRC-1AE03B9EC3-L001764](../../agents/web_agent.py#L1764) | 1764 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001765](../../agents/web_agent.py#L1765) | 1765 | `"            publisher_name = _clean_text("` | — |
| [SRC-1AE03B9EC3-L001766](../../agents/web_agent.py#L1766) | 1766 | `"                source_node.text if source_node is not None else \"\", 200"` | — |
| [SRC-1AE03B9EC3-L001767](../../agents/web_agent.py#L1767) | 1767 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001768](../../agents/web_agent.py#L1768) | 1768 | `"            publisher_domain = ("` | — |
| [SRC-1AE03B9EC3-L001769](../../agents/web_agent.py#L1769) | 1769 | `"                (urllib.parse.urlparse(publisher_url).hostname or \"\").lower()"` | — |
| [SRC-1AE03B9EC3-L001770](../../agents/web_agent.py#L1770) | 1770 | `"                if publisher_url else \"\""` | — |
| [SRC-1AE03B9EC3-L001771](../../agents/web_agent.py#L1771) | 1771 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001772](../../agents/web_agent.py#L1772) | 1772 | `"            results.append({"` | — |
| [SRC-1AE03B9EC3-L001773](../../agents/web_agent.py#L1773) | 1773 | `"                \"title\": _clean_text(fields.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001774](../../agents/web_agent.py#L1774) | 1774 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001775](../../agents/web_agent.py#L1775) | 1775 | `"                \"snippet\": _clean_text(fields.get(\"description\", \"\"), 1200),"` | — |
| [SRC-1AE03B9EC3-L001776](../../agents/web_agent.py#L1776) | 1776 | `"                \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001777](../../agents/web_agent.py#L1777) | 1777 | `"                \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001778](../../agents/web_agent.py#L1778) | 1778 | `"                \"provider\": \"google_news_rss\","` | — |
| [SRC-1AE03B9EC3-L001779](../../agents/web_agent.py#L1779) | 1779 | `"                \"provider_rank\": len(results) + 1,"` | — |
| [SRC-1AE03B9EC3-L001780](../../agents/web_agent.py#L1780) | 1780 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001781](../../agents/web_agent.py#L1781) | 1781 | `"                \"published_at\": _clean_text(fields.get(\"pubDate\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001782](../../agents/web_agent.py#L1782) | 1782 | `"                \"publisher_name\": publisher_name,"` | — |
| [SRC-1AE03B9EC3-L001783](../../agents/web_agent.py#L1783) | 1783 | `"                \"publisher_url\": publisher_url or \"\","` | — |
| [SRC-1AE03B9EC3-L001784](../../agents/web_agent.py#L1784) | 1784 | `"                \"publisher_domain\": publisher_domain,"` | — |
| [SRC-1AE03B9EC3-L001785](../../agents/web_agent.py#L1785) | 1785 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001786](../../agents/web_agent.py#L1786) | 1786 | `"            if len(results) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001787](../../agents/web_agent.py#L1787) | 1787 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001788](../../agents/web_agent.py#L1788) | 1788 | `"        return results"` | — |
| [SRC-1AE03B9EC3-L001789](../../agents/web_agent.py#L1789) | 1789 | `""` | — |
| [SRC-1AE03B9EC3-L001790](../../agents/web_agent.py#L1790) | 1790 | `"    def _search_social("` | — |
| [SRC-1AE03B9EC3-L001791](../../agents/web_agent.py#L1791) | 1791 | `"        self, query: str, platforms: list[str]"` | — |
| [SRC-1AE03B9EC3-L001792](../../agents/web_agent.py#L1792) | 1792 | `"    ) -> tuple[list[dict[str, Any]], list[str]]:"` | — |
| [SRC-1AE03B9EC3-L001793](../../agents/web_agent.py#L1793) | 1793 | `"        \"\"\"Search public social content through exposed public endpoints only.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001794](../../agents/web_agent.py#L1794) | 1794 | `"        query = compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L001795](../../agents/web_agent.py#L1795) | 1795 | `"        if not query:"` | — |
| [SRC-1AE03B9EC3-L001796](../../agents/web_agent.py#L1796) | 1796 | `"            return [], [\"لم يبدأ البحث الاجتماعي لعدم وجود كلمات موضوعية قابلة للبحث.\"]"` | — |
| [SRC-1AE03B9EC3-L001797](../../agents/web_agent.py#L1797) | 1797 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001798](../../agents/web_agent.py#L1798) | 1798 | `"            import xml.etree.ElementTree as ET"` | — |
| [SRC-1AE03B9EC3-L001799](../../agents/web_agent.py#L1799) | 1799 | `""` | — |
| [SRC-1AE03B9EC3-L001800](../../agents/web_agent.py#L1800) | 1800 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L001801](../../agents/web_agent.py#L1801) | 1801 | `"            from bs4 import BeautifulSoup"` | — |
| [SRC-1AE03B9EC3-L001802](../../agents/web_agent.py#L1802) | 1802 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L001803](../../agents/web_agent.py#L1803) | 1803 | `"            raise AgentDependencyError("` | — |
| [SRC-1AE03B9EC3-L001804](../../agents/web_agent.py#L1804) | 1804 | `"                \"حزم البحث الاجتماعي غير مثبتة. نفّذ: python -m pip install -e .\""` | — |
| [SRC-1AE03B9EC3-L001805](../../agents/web_agent.py#L1805) | 1805 | `"            ) from exc"` | — |
| [SRC-1AE03B9EC3-L001806](../../agents/web_agent.py#L1806) | 1806 | `""` | — |
| [SRC-1AE03B9EC3-L001807](../../agents/web_agent.py#L1807) | 1807 | `"        results: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001808](../../agents/web_agent.py#L1808) | 1808 | `"        warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L001809](../../agents/web_agent.py#L1809) | 1809 | `"        headers = {"` | — |
| [SRC-1AE03B9EC3-L001810](../../agents/web_agent.py#L1810) | 1810 | `"            \"User-Agent\": \"OmaraiResearchBot/1.0 (public-content search; no login)\","` | — |
| [SRC-1AE03B9EC3-L001811](../../agents/web_agent.py#L1811) | 1811 | `"            \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001812](../../agents/web_agent.py#L1812) | 1812 | `"        }"` | — |
| [SRC-1AE03B9EC3-L001813](../../agents/web_agent.py#L1813) | 1813 | `""` | — |
| [SRC-1AE03B9EC3-L001814](../../agents/web_agent.py#L1814) | 1814 | `"        reddit_client_id = os.getenv(\"REDDIT_CLIENT_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001815](../../agents/web_agent.py#L1815) | 1815 | `"        reddit_client_secret = os.getenv(\"REDDIT_CLIENT_SECRET\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001816](../../agents/web_agent.py#L1816) | 1816 | `"        reddit_user_agent = os.getenv("` | — |
| [SRC-1AE03B9EC3-L001817](../../agents/web_agent.py#L1817) | 1817 | `"            \"REDDIT_USER_AGENT\","` | — |
| [SRC-1AE03B9EC3-L001818](../../agents/web_agent.py#L1818) | 1818 | `"            \"web:omarai-research-agent:v0.3 (public-content research)\","` | — |
| [SRC-1AE03B9EC3-L001819](../../agents/web_agent.py#L1819) | 1819 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L001820](../../agents/web_agent.py#L1820) | 1820 | `"        if \"reddit\" in platforms and reddit_client_id and reddit_client_secret:"` | — |
| [SRC-1AE03B9EC3-L001821](../../agents/web_agent.py#L1821) | 1821 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001822](../../agents/web_agent.py#L1822) | 1822 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001823](../../agents/web_agent.py#L1823) | 1823 | `"                token_response = httpx.post("` | — |
| [SRC-1AE03B9EC3-L001824](../../agents/web_agent.py#L1824) | 1824 | `"                    \"https://www.reddit.com/api/v1/access_token\","` | — |
| [SRC-1AE03B9EC3-L001825](../../agents/web_agent.py#L1825) | 1825 | `"                    data={\"grant_type\": \"client_credentials\"},"` | — |
| [SRC-1AE03B9EC3-L001826](../../agents/web_agent.py#L1826) | 1826 | `"                    auth=(reddit_client_id, reddit_client_secret),"` | — |
| [SRC-1AE03B9EC3-L001827](../../agents/web_agent.py#L1827) | 1827 | `"                    headers={\"User-Agent\": reddit_user_agent},"` | — |
| [SRC-1AE03B9EC3-L001828](../../agents/web_agent.py#L1828) | 1828 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001829](../../agents/web_agent.py#L1829) | 1829 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001830](../../agents/web_agent.py#L1830) | 1830 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001831](../../agents/web_agent.py#L1831) | 1831 | `"                if token_response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001832](../../agents/web_agent.py#L1832) | 1832 | `"                    access_token = token_response.json().get(\"access_token\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001833](../../agents/web_agent.py#L1833) | 1833 | `"                    if access_token:"` | — |
| [SRC-1AE03B9EC3-L001834](../../agents/web_agent.py#L1834) | 1834 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001835](../../agents/web_agent.py#L1835) | 1835 | `"                        search_response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001836](../../agents/web_agent.py#L1836) | 1836 | `"                            \"https://oauth.reddit.com/search\","` | — |
| [SRC-1AE03B9EC3-L001837](../../agents/web_agent.py#L1837) | 1837 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L001838](../../agents/web_agent.py#L1838) | 1838 | `"                                \"q\": query,"` | — |
| [SRC-1AE03B9EC3-L001839](../../agents/web_agent.py#L1839) | 1839 | `"                                \"sort\": \"relevance\","` | — |
| [SRC-1AE03B9EC3-L001840](../../agents/web_agent.py#L1840) | 1840 | `"                                \"t\": \"all\","` | — |
| [SRC-1AE03B9EC3-L001841](../../agents/web_agent.py#L1841) | 1841 | `"                                \"limit\": 10,"` | — |
| [SRC-1AE03B9EC3-L001842](../../agents/web_agent.py#L1842) | 1842 | `"                                \"type\": \"link\","` | — |
| [SRC-1AE03B9EC3-L001843](../../agents/web_agent.py#L1843) | 1843 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L001844](../../agents/web_agent.py#L1844) | 1844 | `"                            headers={"` | — |
| [SRC-1AE03B9EC3-L001845](../../agents/web_agent.py#L1845) | 1845 | `"                                **headers,"` | — |
| [SRC-1AE03B9EC3-L001846](../../agents/web_agent.py#L1846) | 1846 | `"                                \"User-Agent\": reddit_user_agent,"` | — |
| [SRC-1AE03B9EC3-L001847](../../agents/web_agent.py#L1847) | 1847 | `"                                \"Authorization\": \"Bearer \" + access_token,"` | — |
| [SRC-1AE03B9EC3-L001848](../../agents/web_agent.py#L1848) | 1848 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L001849](../../agents/web_agent.py#L1849) | 1849 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001850](../../agents/web_agent.py#L1850) | 1850 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001851](../../agents/web_agent.py#L1851) | 1851 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L001852](../../agents/web_agent.py#L1852) | 1852 | `"                        if search_response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001853](../../agents/web_agent.py#L1853) | 1853 | `"                            children = search_response.json().get(\"data\", {}).get(\"children\", [])"` | — |
| [SRC-1AE03B9EC3-L001854](../../agents/web_agent.py#L1854) | 1854 | `"                            rank = 0"` | — |
| [SRC-1AE03B9EC3-L001855](../../agents/web_agent.py#L1855) | 1855 | `"                            for child in children:"` | — |
| [SRC-1AE03B9EC3-L001856](../../agents/web_agent.py#L1856) | 1856 | `"                                post = child.get(\"data\", {}) if isinstance(child, dict) else {}"` | — |
| [SRC-1AE03B9EC3-L001857](../../agents/web_agent.py#L1857) | 1857 | `"                                permalink = str(post.get(\"permalink\") or \"\")"` | — |
| [SRC-1AE03B9EC3-L001858](../../agents/web_agent.py#L1858) | 1858 | `"                                url = _public_http_url("` | — |
| [SRC-1AE03B9EC3-L001859](../../agents/web_agent.py#L1859) | 1859 | `"                                    permalink if permalink.startswith(\"http\")"` | — |
| [SRC-1AE03B9EC3-L001860](../../agents/web_agent.py#L1860) | 1860 | `"                                    else \"https://www.reddit.com\" + permalink"` | — |
| [SRC-1AE03B9EC3-L001861](../../agents/web_agent.py#L1861) | 1861 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L001862](../../agents/web_agent.py#L1862) | 1862 | `"                                if not url:"` | — |
| [SRC-1AE03B9EC3-L001863](../../agents/web_agent.py#L1863) | 1863 | `"                                    continue"` | — |
| [SRC-1AE03B9EC3-L001864](../../agents/web_agent.py#L1864) | 1864 | `"                                rank += 1"` | — |
| [SRC-1AE03B9EC3-L001865](../../agents/web_agent.py#L1865) | 1865 | `"                                snippet = _clean_text(post.get(\"selftext\") or \"\", 1000)"` | — |
| [SRC-1AE03B9EC3-L001866](../../agents/web_agent.py#L1866) | 1866 | `"                                metrics = []"` | — |
| [SRC-1AE03B9EC3-L001867](../../agents/web_agent.py#L1867) | 1867 | `"                                if post.get(\"score\") is not None:"` | — |
| [SRC-1AE03B9EC3-L001868](../../agents/web_agent.py#L1868) | 1868 | `"                                    metrics.append(\"score=\" + str(post[\"score\"]))"` | — |
| [SRC-1AE03B9EC3-L001869](../../agents/web_agent.py#L1869) | 1869 | `"                                if post.get(\"num_comments\") is not None:"` | — |
| [SRC-1AE03B9EC3-L001870](../../agents/web_agent.py#L1870) | 1870 | `"                                    metrics.append(\"comments=\" + str(post[\"num_comments\"]))"` | — |
| [SRC-1AE03B9EC3-L001871](../../agents/web_agent.py#L1871) | 1871 | `"                                if metrics:"` | — |
| [SRC-1AE03B9EC3-L001872](../../agents/web_agent.py#L1872) | 1872 | `"                                    snippet = (snippet + \" \| \" if snippet else \"\") + \", \".join(metrics)"` | — |
| [SRC-1AE03B9EC3-L001873](../../agents/web_agent.py#L1873) | 1873 | `"                                results.append({"` | — |
| [SRC-1AE03B9EC3-L001874](../../agents/web_agent.py#L1874) | 1874 | `"                                    \"title\": _clean_text(post.get(\"title\") or \"Reddit post\", 300),"` | — |
| [SRC-1AE03B9EC3-L001875](../../agents/web_agent.py#L1875) | 1875 | `"                                    \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001876](../../agents/web_agent.py#L1876) | 1876 | `"                                    \"snippet\": snippet,"` | — |
| [SRC-1AE03B9EC3-L001877](../../agents/web_agent.py#L1877) | 1877 | `"                                    \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001878](../../agents/web_agent.py#L1878) | 1878 | `"                                    \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001879](../../agents/web_agent.py#L1879) | 1879 | `"                                    \"provider\": \"reddit_oauth_api\","` | — |
| [SRC-1AE03B9EC3-L001880](../../agents/web_agent.py#L1880) | 1880 | `"                                    \"provider_rank\": rank,"` | — |
| [SRC-1AE03B9EC3-L001881](../../agents/web_agent.py#L1881) | 1881 | `"                                    \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001882](../../agents/web_agent.py#L1882) | 1882 | `"                                    \"published_at\": _clean_text(str(post.get(\"created_utc\") or \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001883](../../agents/web_agent.py#L1883) | 1883 | `"                                })"` | — |
| [SRC-1AE03B9EC3-L001884](../../agents/web_agent.py#L1884) | 1884 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L001885](../../agents/web_agent.py#L1885) | 1885 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L001886](../../agents/web_agent.py#L1886) | 1886 | `"                                f\"Reddit OAuth search unavailable (HTTP {search_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L001887](../../agents/web_agent.py#L1887) | 1887 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L001888](../../agents/web_agent.py#L1888) | 1888 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L001889](../../agents/web_agent.py#L1889) | 1889 | `"                        warnings.append(\"Reddit OAuth did not return an access token.\")"` | — |
| [SRC-1AE03B9EC3-L001890](../../agents/web_agent.py#L1890) | 1890 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001891](../../agents/web_agent.py#L1891) | 1891 | `"                    warnings.append("` | — |
| [SRC-1AE03B9EC3-L001892](../../agents/web_agent.py#L1892) | 1892 | `"                        f\"Reddit OAuth authentication unavailable (HTTP {token_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L001893](../../agents/web_agent.py#L1893) | 1893 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L001894](../../agents/web_agent.py#L1894) | 1894 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L001895](../../agents/web_agent.py#L1895) | 1895 | `"                warnings.append(\"Reddit OAuth search failed for this request.\")"` | — |
| [SRC-1AE03B9EC3-L001896](../../agents/web_agent.py#L1896) | 1896 | `""` | — |
| [SRC-1AE03B9EC3-L001897](../../agents/web_agent.py#L1897) | 1897 | `"        if \"reddit\" in platforms and not any("` | — |
| [SRC-1AE03B9EC3-L001898](../../agents/web_agent.py#L1898) | 1898 | `"            row.get(\"provider\") == \"reddit_oauth_api\" for row in results"` | — |
| [SRC-1AE03B9EC3-L001899](../../agents/web_agent.py#L1899) | 1899 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L001900](../../agents/web_agent.py#L1900) | 1900 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001901](../../agents/web_agent.py#L1901) | 1901 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001902](../../agents/web_agent.py#L1902) | 1902 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001903](../../agents/web_agent.py#L1903) | 1903 | `"                    \"https://www.reddit.com/search.rss\","` | — |
| [SRC-1AE03B9EC3-L001904](../../agents/web_agent.py#L1904) | 1904 | `"                    params={\"q\": query, \"sort\": \"relevance\", \"t\": \"all\", \"limit\": \"8\"},"` | — |
| [SRC-1AE03B9EC3-L001905](../../agents/web_agent.py#L1905) | 1905 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L001906](../../agents/web_agent.py#L1906) | 1906 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001907](../../agents/web_agent.py#L1907) | 1907 | `"                    follow_redirects=False,"` | — |
