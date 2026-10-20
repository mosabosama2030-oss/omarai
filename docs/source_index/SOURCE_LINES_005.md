# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **005**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L001145 إلى SRC-1AE03B9EC3-L001944
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L001145](../../agents/web_agent.py#L1145) | 1145 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001146](../../agents/web_agent.py#L1146) | 1146 | `"                \"snippet\": _clean_text(snippet, 1600),"` | — |
| [SRC-1AE03B9EC3-L001147](../../agents/web_agent.py#L1147) | 1147 | `"                \"provider\": \"deepseek_search_api\","` | — |
| [SRC-1AE03B9EC3-L001148](../../agents/web_agent.py#L1148) | 1148 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001149](../../agents/web_agent.py#L1149) | 1149 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001150](../../agents/web_agent.py#L1150) | 1150 | `"                \"published_at\": _clean_text(item.get(\"date\", \"\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L001151](../../agents/web_agent.py#L1151) | 1151 | `"                \"publisher_name\": _clean_text(item.get(\"site_name\", \"\") or \"\", 200),"` | — |
| [SRC-1AE03B9EC3-L001152](../../agents/web_agent.py#L1152) | 1152 | `"                \"provider_rerank_score\": item.get(\"rerank_score\"),"` | — |
| [SRC-1AE03B9EC3-L001153](../../agents/web_agent.py#L1153) | 1153 | `"                \"provider_authority_tier\": item.get(\"authority\"),"` | — |
| [SRC-1AE03B9EC3-L001154](../../agents/web_agent.py#L1154) | 1154 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001155](../../agents/web_agent.py#L1155) | 1155 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001156](../../agents/web_agent.py#L1156) | 1156 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001157](../../agents/web_agent.py#L1157) | 1157 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001158](../../agents/web_agent.py#L1158) | 1158 | `""` | — |
| [SRC-1AE03B9EC3-L001159](../../agents/web_agent.py#L1159) | 1159 | `"    def _reset_deepseek_search_budget(self) -> None:"` | — |
| [SRC-1AE03B9EC3-L001160](../../agents/web_agent.py#L1160) | 1160 | `"        \"\"\"Reset the bounded optional Search API request budget for one operation.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001161](../../agents/web_agent.py#L1161) | 1161 | `"        with self._deepseek_budget_lock:"` | — |
| [SRC-1AE03B9EC3-L001162](../../agents/web_agent.py#L1162) | 1162 | `"            self._deepseek_search_requests_reserved = 0"` | — |
| [SRC-1AE03B9EC3-L001163](../../agents/web_agent.py#L1163) | 1163 | `""` | — |
| [SRC-1AE03B9EC3-L001164](../../agents/web_agent.py#L1164) | 1164 | `"    def _reserve_deepseek_search_request(self) -> bool:"` | — |
| [SRC-1AE03B9EC3-L001165](../../agents/web_agent.py#L1165) | 1165 | `"        \"\"\"Reserve one paid search request before concurrent queries invoke the provider.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001166](../../agents/web_agent.py#L1166) | 1166 | `"        if not os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001167](../../agents/web_agent.py#L1167) | 1167 | `"            return False"` | — |
| [SRC-1AE03B9EC3-L001168](../../agents/web_agent.py#L1168) | 1168 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001169](../../agents/web_agent.py#L1169) | 1169 | `"            configured_budget = int("` | — |
| [SRC-1AE03B9EC3-L001170](../../agents/web_agent.py#L1170) | 1170 | `"                os.getenv(\"OMARAI_DEEPSEEK_SEARCH_REQUEST_BUDGET\", \"1\").strip()"` | — |
| [SRC-1AE03B9EC3-L001171](../../agents/web_agent.py#L1171) | 1171 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001172](../../agents/web_agent.py#L1172) | 1172 | `"        except ValueError:"` | — |
| [SRC-1AE03B9EC3-L001173](../../agents/web_agent.py#L1173) | 1173 | `"            configured_budget = 1"` | — |
| [SRC-1AE03B9EC3-L001174](../../agents/web_agent.py#L1174) | 1174 | `"        budget = max(0, min(configured_budget, 3))"` | — |
| [SRC-1AE03B9EC3-L001175](../../agents/web_agent.py#L1175) | 1175 | `"        with self._deepseek_budget_lock:"` | — |
| [SRC-1AE03B9EC3-L001176](../../agents/web_agent.py#L1176) | 1176 | `"            if self._deepseek_search_requests_reserved >= budget:"` | — |
| [SRC-1AE03B9EC3-L001177](../../agents/web_agent.py#L1177) | 1177 | `"                return False"` | — |
| [SRC-1AE03B9EC3-L001178](../../agents/web_agent.py#L1178) | 1178 | `"            self._deepseek_search_requests_reserved += 1"` | — |
| [SRC-1AE03B9EC3-L001179](../../agents/web_agent.py#L1179) | 1179 | `"            return True"` | — |
| [SRC-1AE03B9EC3-L001180](../../agents/web_agent.py#L1180) | 1180 | `""` | — |
| [SRC-1AE03B9EC3-L001181](../../agents/web_agent.py#L1181) | 1181 | `"    def _search_web(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001182](../../agents/web_agent.py#L1182) | 1182 | `"        \"\"\"Run configured search connectors concurrently with isolated failures and relevance checks.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001183](../../agents/web_agent.py#L1183) | 1183 | `"        from agents.research import detect_freshness"` | — |
| [SRC-1AE03B9EC3-L001184](../../agents/web_agent.py#L1184) | 1184 | `""` | — |
| [SRC-1AE03B9EC3-L001185](../../agents/web_agent.py#L1185) | 1185 | `"        search_query = _normalize_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L001186](../../agents/web_agent.py#L1186) | 1186 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L001187](../../agents/web_agent.py#L1187) | 1187 | `"        if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L001188](../../agents/web_agent.py#L1188) | 1188 | `"            budget.reserve(\"search_queries\")"` | — |
| [SRC-1AE03B9EC3-L001189](../../agents/web_agent.py#L1189) | 1189 | `"        adapters: list[tuple[str, Any]] = ["` | — |
| [SRC-1AE03B9EC3-L001190](../../agents/web_agent.py#L1190) | 1190 | `"            (\"duckduckgo_html\", self._search_duckduckgo_html),"` | — |
| [SRC-1AE03B9EC3-L001191](../../agents/web_agent.py#L1191) | 1191 | `"            (\"bing_rss\", self._search_bing_rss),"` | — |
| [SRC-1AE03B9EC3-L001192](../../agents/web_agent.py#L1192) | 1192 | `"        ]"` | — |
| [SRC-1AE03B9EC3-L001193](../../agents/web_agent.py#L1193) | 1193 | `"        # Experimental opt-in only: DeepSeek Search is billed per successful request."` | — |
| [SRC-1AE03B9EC3-L001194](../../agents/web_agent.py#L1194) | 1194 | `"        # Do not promote it to primary without a measured comparison."` | — |
| [SRC-1AE03B9EC3-L001195](../../agents/web_agent.py#L1195) | 1195 | `"        if not os.getenv(\"DEEPSEEK_SEARCH_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001196](../../agents/web_agent.py#L1196) | 1196 | `"            self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001197](../../agents/web_agent.py#L1197) | 1197 | `"                \"deepseek_search_api\", search_query, \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001198](../../agents/web_agent.py#L1198) | 1198 | `"                error=\"DEEPSEEK_SEARCH_API_KEY is not set\","` | — |
| [SRC-1AE03B9EC3-L001199](../../agents/web_agent.py#L1199) | 1199 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001200](../../agents/web_agent.py#L1200) | 1200 | `"        elif self._reserve_deepseek_search_request():"` | — |
| [SRC-1AE03B9EC3-L001201](../../agents/web_agent.py#L1201) | 1201 | `"            adapters.append((\"deepseek_search_api\", self._search_deepseek_api))"` | — |
| [SRC-1AE03B9EC3-L001202](../../agents/web_agent.py#L1202) | 1202 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001203](../../agents/web_agent.py#L1203) | 1203 | `"            self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001204](../../agents/web_agent.py#L1204) | 1204 | `"                \"deepseek_search_api\", search_query, \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L001205](../../agents/web_agent.py#L1205) | 1205 | `"                error=\"per-operation DeepSeek Search request budget exhausted\","` | — |
| [SRC-1AE03B9EC3-L001206](../../agents/web_agent.py#L1206) | 1206 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001207](../../agents/web_agent.py#L1207) | 1207 | `"        if os.getenv(\"BRAVE_SEARCH_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001208](../../agents/web_agent.py#L1208) | 1208 | `"            adapters.append((\"brave_search_api\", self._search_brave))"` | — |
| [SRC-1AE03B9EC3-L001209](../../agents/web_agent.py#L1209) | 1209 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001210](../../agents/web_agent.py#L1210) | 1210 | `"            self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001211](../../agents/web_agent.py#L1211) | 1211 | `"                \"brave_search_api\", search_query, \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001212](../../agents/web_agent.py#L1212) | 1212 | `"                error=\"BRAVE_SEARCH_API_KEY is not set\","` | — |
| [SRC-1AE03B9EC3-L001213](../../agents/web_agent.py#L1213) | 1213 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001214](../../agents/web_agent.py#L1214) | 1214 | `"        if os.getenv(\"TAVILY_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001215](../../agents/web_agent.py#L1215) | 1215 | `"            adapters.append((\"tavily_search_api\", self._search_tavily))"` | — |
| [SRC-1AE03B9EC3-L001216](../../agents/web_agent.py#L1216) | 1216 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L001217](../../agents/web_agent.py#L1217) | 1217 | `"            self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001218](../../agents/web_agent.py#L1218) | 1218 | `"                \"tavily_search_api\", search_query, \"not_configured\","` | — |
| [SRC-1AE03B9EC3-L001219](../../agents/web_agent.py#L1219) | 1219 | `"                error=\"TAVILY_API_KEY is not set\","` | — |
| [SRC-1AE03B9EC3-L001220](../../agents/web_agent.py#L1220) | 1220 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001221](../../agents/web_agent.py#L1221) | 1221 | `"        if detect_freshness(search_query):"` | — |
| [SRC-1AE03B9EC3-L001222](../../agents/web_agent.py#L1222) | 1222 | `"            adapters.append((\"google_news_rss\", self._search_news))"` | — |
| [SRC-1AE03B9EC3-L001223](../../agents/web_agent.py#L1223) | 1223 | `""` | — |
| [SRC-1AE03B9EC3-L001224](../../agents/web_agent.py#L1224) | 1224 | `"        async def run_one(name: str, method: Any) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001225](../../agents/web_agent.py#L1225) | 1225 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001226](../../agents/web_agent.py#L1226) | 1226 | `"                if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L001227](../../agents/web_agent.py#L1227) | 1227 | `"                    budget.reserve(\"search_calls\")"` | — |
| [SRC-1AE03B9EC3-L001228](../../agents/web_agent.py#L1228) | 1228 | `"                provider_timeout = self._effective_timeout(10.0)"` | — |
| [SRC-1AE03B9EC3-L001229](../../agents/web_agent.py#L1229) | 1229 | `"                raw = await asyncio.wait_for("` | — |
| [SRC-1AE03B9EC3-L001230](../../agents/web_agent.py#L1230) | 1230 | `"                    asyncio.to_thread(method, search_query), timeout=provider_timeout"` | — |
| [SRC-1AE03B9EC3-L001231](../../agents/web_agent.py#L1231) | 1231 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001232](../../agents/web_agent.py#L1232) | 1232 | `"                if not isinstance(raw, list):"` | — |
| [SRC-1AE03B9EC3-L001233](../../agents/web_agent.py#L1233) | 1233 | `"                    raise TypeError(\"connector returned a non-list result\")"` | — |
| [SRC-1AE03B9EC3-L001234](../../agents/web_agent.py#L1234) | 1234 | `"                accepted: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001235](../../agents/web_agent.py#L1235) | 1235 | `"                rejected = 0"` | — |
| [SRC-1AE03B9EC3-L001236](../../agents/web_agent.py#L1236) | 1236 | `"                for item in raw:"` | — |
| [SRC-1AE03B9EC3-L001237](../../agents/web_agent.py#L1237) | 1237 | `"                    if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L001238](../../agents/web_agent.py#L1238) | 1238 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001239](../../agents/web_agent.py#L1239) | 1239 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001240](../../agents/web_agent.py#L1240) | 1240 | `"                    safe_url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001241](../../agents/web_agent.py#L1241) | 1241 | `"                    if not safe_url or _blocked_source_url(safe_url):"` | — |
| [SRC-1AE03B9EC3-L001242](../../agents/web_agent.py#L1242) | 1242 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001243](../../agents/web_agent.py#L1243) | 1243 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001244](../../agents/web_agent.py#L1244) | 1244 | `"                    normalized_item = dict(item)"` | — |
| [SRC-1AE03B9EC3-L001245](../../agents/web_agent.py#L1245) | 1245 | `"                    normalized_item[\"url\"] = safe_url"` | — |
| [SRC-1AE03B9EC3-L001246](../../agents/web_agent.py#L1246) | 1246 | `"                    normalized_item.setdefault(\"provider\", name)"` | — |
| [SRC-1AE03B9EC3-L001247](../../agents/web_agent.py#L1247) | 1247 | `"                    normalized_item.setdefault(\"search_query\", search_query)"` | — |
| [SRC-1AE03B9EC3-L001248](../../agents/web_agent.py#L1248) | 1248 | `"                    evidence = \" \".join(str(normalized_item.get(k) or \"\") for k in (\"title\", \"snippet\"))"` | — |
| [SRC-1AE03B9EC3-L001249](../../agents/web_agent.py#L1249) | 1249 | `"                    if _relevance_ratio(search_query, evidence) < 0.20:"` | — |
| [SRC-1AE03B9EC3-L001250](../../agents/web_agent.py#L1250) | 1250 | `"                        rejected += 1"` | — |
| [SRC-1AE03B9EC3-L001251](../../agents/web_agent.py#L1251) | 1251 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L001252](../../agents/web_agent.py#L1252) | 1252 | `"                    accepted.append(normalized_item)"` | — |
| [SRC-1AE03B9EC3-L001253](../../agents/web_agent.py#L1253) | 1253 | `"                if accepted:"` | — |
| [SRC-1AE03B9EC3-L001254](../../agents/web_agent.py#L1254) | 1254 | `"                    status = \"ok\""` | — |
| [SRC-1AE03B9EC3-L001255](../../agents/web_agent.py#L1255) | 1255 | `"                    error = None"` | — |
| [SRC-1AE03B9EC3-L001256](../../agents/web_agent.py#L1256) | 1256 | `"                elif raw:"` | — |
| [SRC-1AE03B9EC3-L001257](../../agents/web_agent.py#L1257) | 1257 | `"                    status = \"filtered_all\""` | — |
| [SRC-1AE03B9EC3-L001258](../../agents/web_agent.py#L1258) | 1258 | `"                    error = \"all candidates failed URL/domain/relevance checks\""` | — |
| [SRC-1AE03B9EC3-L001259](../../agents/web_agent.py#L1259) | 1259 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001260](../../agents/web_agent.py#L1260) | 1260 | `"                    status = \"no_results\""` | — |
| [SRC-1AE03B9EC3-L001261](../../agents/web_agent.py#L1261) | 1261 | `"                    error = \"connector returned no parseable results\""` | — |
| [SRC-1AE03B9EC3-L001262](../../agents/web_agent.py#L1262) | 1262 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001263](../../agents/web_agent.py#L1263) | 1263 | `"                    name, search_query, status, len(accepted), rejected, error"` | — |
| [SRC-1AE03B9EC3-L001264](../../agents/web_agent.py#L1264) | 1264 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001265](../../agents/web_agent.py#L1265) | 1265 | `"                return accepted"` | — |
| [SRC-1AE03B9EC3-L001266](../../agents/web_agent.py#L1266) | 1266 | `"            except RequestBudgetExceeded as exc:"` | — |
| [SRC-1AE03B9EC3-L001267](../../agents/web_agent.py#L1267) | 1267 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001268](../../agents/web_agent.py#L1268) | 1268 | `"                    name, search_query, \"budget_exhausted\", error=str(exc)"` | — |
| [SRC-1AE03B9EC3-L001269](../../agents/web_agent.py#L1269) | 1269 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001270](../../agents/web_agent.py#L1270) | 1270 | `"            except TimeoutError:"` | — |
| [SRC-1AE03B9EC3-L001271](../../agents/web_agent.py#L1271) | 1271 | `"                self._record_provider_diagnostic("` | — |
| [SRC-1AE03B9EC3-L001272](../../agents/web_agent.py#L1272) | 1272 | `"                    name, search_query, \"timeout\", error=\"provider exceeded its bounded request timeout\""` | — |
| [SRC-1AE03B9EC3-L001273](../../agents/web_agent.py#L1273) | 1273 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001274](../../agents/web_agent.py#L1274) | 1274 | `"            except Exception as exc:  # noqa: BLE001 - isolate a connector without leaking provider bodies/secrets"` | — |
| [SRC-1AE03B9EC3-L001275](../../agents/web_agent.py#L1275) | 1275 | `"                detail = f\"{type(exc).__name__}: {exc}\" if isinstance(exc, RuntimeError) else type(exc).__name__"` | — |
| [SRC-1AE03B9EC3-L001276](../../agents/web_agent.py#L1276) | 1276 | `"                self._record_provider_diagnostic(name, search_query, \"failed\", error=detail)"` | — |
| [SRC-1AE03B9EC3-L001277](../../agents/web_agent.py#L1277) | 1277 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001278](../../agents/web_agent.py#L1278) | 1278 | `""` | — |
| [SRC-1AE03B9EC3-L001279](../../agents/web_agent.py#L1279) | 1279 | `"        async def run_all() -> list[list[dict[str, Any]]]:"` | — |
| [SRC-1AE03B9EC3-L001280](../../agents/web_agent.py#L1280) | 1280 | `"            return await asyncio.gather(*(run_one(name, method) for name, method in adapters))"` | — |
| [SRC-1AE03B9EC3-L001281](../../agents/web_agent.py#L1281) | 1281 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001282](../../agents/web_agent.py#L1282) | 1282 | `"            provider_batches = asyncio.run(run_all())"` | — |
| [SRC-1AE03B9EC3-L001283](../../agents/web_agent.py#L1283) | 1283 | `"        except RuntimeError as exc:"` | — |
| [SRC-1AE03B9EC3-L001284](../../agents/web_agent.py#L1284) | 1284 | `"            # This method is synchronous by contract; the HTTP server invokes it in worker threads."` | — |
| [SRC-1AE03B9EC3-L001285](../../agents/web_agent.py#L1285) | 1285 | `"            raise RuntimeError(\"تعذر تشغيل مجدول موصلات البحث.\") from exc"` | — |
| [SRC-1AE03B9EC3-L001286](../../agents/web_agent.py#L1286) | 1286 | `"        combined = [item for batch in provider_batches for item in batch]"` | — |
| [SRC-1AE03B9EC3-L001287](../../agents/web_agent.py#L1287) | 1287 | `"        # De-duplicate repeated URLs before ranking/fusion."` | — |
| [SRC-1AE03B9EC3-L001288](../../agents/web_agent.py#L1288) | 1288 | `"        unique: dict[str, dict[str, Any]] = {}"` | — |
| [SRC-1AE03B9EC3-L001289](../../agents/web_agent.py#L1289) | 1289 | `"        for item in combined:"` | — |
| [SRC-1AE03B9EC3-L001290](../../agents/web_agent.py#L1290) | 1290 | `"            key = item[\"url\"].split(\"#\", 1)[0].rstrip(\"/\")"` | — |
| [SRC-1AE03B9EC3-L001291](../../agents/web_agent.py#L1291) | 1291 | `"            if key not in unique or len(str(item.get(\"snippet\") or \"\")) > len(str(unique[key].get(\"snippet\") or \"\")):"` | — |
| [SRC-1AE03B9EC3-L001292](../../agents/web_agent.py#L1292) | 1292 | `"                unique[key] = item"` | — |
| [SRC-1AE03B9EC3-L001293](../../agents/web_agent.py#L1293) | 1293 | `"        if not unique:"` | — |
| [SRC-1AE03B9EC3-L001294](../../agents/web_agent.py#L1294) | 1294 | `"            raise RuntimeError(\"لم تُرجع موصلات البحث نتائج مرتبطة وقابلة للاستخدام.\")"` | — |
| [SRC-1AE03B9EC3-L001295](../../agents/web_agent.py#L1295) | 1295 | `"        return list(unique.values())"` | — |
| [SRC-1AE03B9EC3-L001296](../../agents/web_agent.py#L1296) | 1296 | `""` | — |
| [SRC-1AE03B9EC3-L001297](../../agents/web_agent.py#L1297) | 1297 | `"    def _reserve_search_call(self) -> None:"` | — |
| [SRC-1AE03B9EC3-L001298](../../agents/web_agent.py#L1298) | 1298 | `"        \"\"\"Reserve one outbound search/social-provider request before network I/O.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001299](../../agents/web_agent.py#L1299) | 1299 | `"        budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L001300](../../agents/web_agent.py#L1300) | 1300 | `"        if budget is not None:"` | — |
| [SRC-1AE03B9EC3-L001301](../../agents/web_agent.py#L1301) | 1301 | `"            budget.reserve(\"search_calls\")"` | — |
| [SRC-1AE03B9EC3-L001302](../../agents/web_agent.py#L1302) | 1302 | `""` | — |
| [SRC-1AE03B9EC3-L001303](../../agents/web_agent.py#L1303) | 1303 | `"    def _search_brave(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001304](../../agents/web_agent.py#L1304) | 1304 | `"        \"\"\"Use Brave's official web-search API when the operator provides an API key.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001305](../../agents/web_agent.py#L1305) | 1305 | `"        api_key = os.getenv(\"BRAVE_SEARCH_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001306](../../agents/web_agent.py#L1306) | 1306 | `"        if not api_key:"` | — |
| [SRC-1AE03B9EC3-L001307](../../agents/web_agent.py#L1307) | 1307 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001308](../../agents/web_agent.py#L1308) | 1308 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001309](../../agents/web_agent.py#L1309) | 1309 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L001310](../../agents/web_agent.py#L1310) | 1310 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L001311](../../agents/web_agent.py#L1311) | 1311 | `"            raise AgentDependencyError(\"حزمة httpx غير مثبتة.\") from exc"` | — |
| [SRC-1AE03B9EC3-L001312](../../agents/web_agent.py#L1312) | 1312 | `"        is_arabic = bool(re.search(r\"[\\u0600-\\u06FF]\", query))"` | — |
| [SRC-1AE03B9EC3-L001313](../../agents/web_agent.py#L1313) | 1313 | `"        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001314](../../agents/web_agent.py#L1314) | 1314 | `"            \"https://api.search.brave.com/res/v1/web/search\","` | — |
| [SRC-1AE03B9EC3-L001315](../../agents/web_agent.py#L1315) | 1315 | `"            params={"` | — |
| [SRC-1AE03B9EC3-L001316](../../agents/web_agent.py#L1316) | 1316 | `"                \"q\": query[:600],"` | — |
| [SRC-1AE03B9EC3-L001317](../../agents/web_agent.py#L1317) | 1317 | `"                \"count\": MAX_PROVIDER_RESULTS,"` | — |
| [SRC-1AE03B9EC3-L001318](../../agents/web_agent.py#L1318) | 1318 | `"                \"country\": \"EG\" if is_arabic else \"US\","` | — |
| [SRC-1AE03B9EC3-L001319](../../agents/web_agent.py#L1319) | 1319 | `"                \"search_lang\": \"ar\" if is_arabic else \"en\","` | — |
| [SRC-1AE03B9EC3-L001320](../../agents/web_agent.py#L1320) | 1320 | `"                \"extra_snippets\": \"true\","` | — |
| [SRC-1AE03B9EC3-L001321](../../agents/web_agent.py#L1321) | 1321 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001322](../../agents/web_agent.py#L1322) | 1322 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001323](../../agents/web_agent.py#L1323) | 1323 | `"                \"Accept\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001324](../../agents/web_agent.py#L1324) | 1324 | `"                \"X-Subscription-Token\": api_key,"` | — |
| [SRC-1AE03B9EC3-L001325](../../agents/web_agent.py#L1325) | 1325 | `"                \"User-Agent\": \"OmaraiResearchAgent/1.0\","` | — |
| [SRC-1AE03B9EC3-L001326](../../agents/web_agent.py#L1326) | 1326 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001327](../../agents/web_agent.py#L1327) | 1327 | `"            timeout=self._effective_timeout(8.5),"` | — |
| [SRC-1AE03B9EC3-L001328](../../agents/web_agent.py#L1328) | 1328 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001329](../../agents/web_agent.py#L1329) | 1329 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001330](../../agents/web_agent.py#L1330) | 1330 | `"        response.raise_for_status()"` | — |
| [SRC-1AE03B9EC3-L001331](../../agents/web_agent.py#L1331) | 1331 | `"        payload = response.json()"` | — |
| [SRC-1AE03B9EC3-L001332](../../agents/web_agent.py#L1332) | 1332 | `"        web_results = payload.get(\"web\", {}).get(\"results\", [])"` | — |
| [SRC-1AE03B9EC3-L001333](../../agents/web_agent.py#L1333) | 1333 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001334](../../agents/web_agent.py#L1334) | 1334 | `"        for item in web_results if isinstance(web_results, list) else []:"` | — |
| [SRC-1AE03B9EC3-L001335](../../agents/web_agent.py#L1335) | 1335 | `"            if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L001336](../../agents/web_agent.py#L1336) | 1336 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001337](../../agents/web_agent.py#L1337) | 1337 | `"            url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001338](../../agents/web_agent.py#L1338) | 1338 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001339](../../agents/web_agent.py#L1339) | 1339 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001340](../../agents/web_agent.py#L1340) | 1340 | `"            snippets = item.get(\"extra_snippets\", [])"` | — |
| [SRC-1AE03B9EC3-L001341](../../agents/web_agent.py#L1341) | 1341 | `"            extra = \" \".join(x for x in snippets if isinstance(x, str)) if isinstance(snippets, list) else \"\""` | — |
| [SRC-1AE03B9EC3-L001342](../../agents/web_agent.py#L1342) | 1342 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001343](../../agents/web_agent.py#L1343) | 1343 | `"                \"title\": _clean_text(item.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001344](../../agents/web_agent.py#L1344) | 1344 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001345](../../agents/web_agent.py#L1345) | 1345 | `"                \"snippet\": _clean_text(item.get(\"description\", \"\") + \" \" + extra, 1600),"` | — |
| [SRC-1AE03B9EC3-L001346](../../agents/web_agent.py#L1346) | 1346 | `"                \"provider\": \"brave_search_api\","` | — |
| [SRC-1AE03B9EC3-L001347](../../agents/web_agent.py#L1347) | 1347 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001348](../../agents/web_agent.py#L1348) | 1348 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001349](../../agents/web_agent.py#L1349) | 1349 | `"                \"published_at\": _clean_text(item.get(\"page_age\", \"\") or item.get(\"published_at\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001350](../../agents/web_agent.py#L1350) | 1350 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001351](../../agents/web_agent.py#L1351) | 1351 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001352](../../agents/web_agent.py#L1352) | 1352 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001353](../../agents/web_agent.py#L1353) | 1353 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001354](../../agents/web_agent.py#L1354) | 1354 | `""` | — |
| [SRC-1AE03B9EC3-L001355](../../agents/web_agent.py#L1355) | 1355 | `"    def _search_tavily(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001356](../../agents/web_agent.py#L1356) | 1356 | `"        \"\"\"Use Tavily's official search API for structured, extractable live web results.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001357](../../agents/web_agent.py#L1357) | 1357 | `"        api_key = os.getenv(\"TAVILY_API_KEY\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001358](../../agents/web_agent.py#L1358) | 1358 | `"        if not api_key:"` | — |
| [SRC-1AE03B9EC3-L001359](../../agents/web_agent.py#L1359) | 1359 | `"            return []"` | — |
| [SRC-1AE03B9EC3-L001360](../../agents/web_agent.py#L1360) | 1360 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001361](../../agents/web_agent.py#L1361) | 1361 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L001362](../../agents/web_agent.py#L1362) | 1362 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L001363](../../agents/web_agent.py#L1363) | 1363 | `"            raise AgentDependencyError(\"حزمة httpx غير مثبتة.\") from exc"` | — |
| [SRC-1AE03B9EC3-L001364](../../agents/web_agent.py#L1364) | 1364 | `"        from agents.research import detect_depth, detect_freshness"` | — |
| [SRC-1AE03B9EC3-L001365](../../agents/web_agent.py#L1365) | 1365 | `""` | — |
| [SRC-1AE03B9EC3-L001366](../../agents/web_agent.py#L1366) | 1366 | `"        response = httpx.post("` | — |
| [SRC-1AE03B9EC3-L001367](../../agents/web_agent.py#L1367) | 1367 | `"            \"https://api.tavily.com/search\","` | — |
| [SRC-1AE03B9EC3-L001368](../../agents/web_agent.py#L1368) | 1368 | `"            json={"` | — |
| [SRC-1AE03B9EC3-L001369](../../agents/web_agent.py#L1369) | 1369 | `"                \"api_key\": api_key,"` | — |
| [SRC-1AE03B9EC3-L001370](../../agents/web_agent.py#L1370) | 1370 | `"                \"query\": query[:500],"` | — |
| [SRC-1AE03B9EC3-L001371](../../agents/web_agent.py#L1371) | 1371 | `"                \"search_depth\": \"advanced\" if detect_depth(query) == \"deep\" else \"basic\","` | — |
| [SRC-1AE03B9EC3-L001372](../../agents/web_agent.py#L1372) | 1372 | `"                \"topic\": \"news\" if detect_freshness(query) else \"general\","` | — |
| [SRC-1AE03B9EC3-L001373](../../agents/web_agent.py#L1373) | 1373 | `"                \"max_results\": MAX_PROVIDER_RESULTS,"` | — |
| [SRC-1AE03B9EC3-L001374](../../agents/web_agent.py#L1374) | 1374 | `"                \"include_answer\": False,"` | — |
| [SRC-1AE03B9EC3-L001375](../../agents/web_agent.py#L1375) | 1375 | `"                \"include_raw_content\": False,"` | — |
| [SRC-1AE03B9EC3-L001376](../../agents/web_agent.py#L1376) | 1376 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001377](../../agents/web_agent.py#L1377) | 1377 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001378](../../agents/web_agent.py#L1378) | 1378 | `"                \"Accept\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001379](../../agents/web_agent.py#L1379) | 1379 | `"                \"Content-Type\": \"application/json\","` | — |
| [SRC-1AE03B9EC3-L001380](../../agents/web_agent.py#L1380) | 1380 | `"                \"User-Agent\": \"OmaraiResearchAgent/1.0\","` | — |
| [SRC-1AE03B9EC3-L001381](../../agents/web_agent.py#L1381) | 1381 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001382](../../agents/web_agent.py#L1382) | 1382 | `"            timeout=self._effective_timeout(8.5),"` | — |
| [SRC-1AE03B9EC3-L001383](../../agents/web_agent.py#L1383) | 1383 | `"            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001384](../../agents/web_agent.py#L1384) | 1384 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001385](../../agents/web_agent.py#L1385) | 1385 | `"        response.raise_for_status()"` | — |
| [SRC-1AE03B9EC3-L001386](../../agents/web_agent.py#L1386) | 1386 | `"        payload = response.json()"` | — |
| [SRC-1AE03B9EC3-L001387](../../agents/web_agent.py#L1387) | 1387 | `"        search_results = payload.get(\"results\", [])"` | — |
| [SRC-1AE03B9EC3-L001388](../../agents/web_agent.py#L1388) | 1388 | `"        rows: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001389](../../agents/web_agent.py#L1389) | 1389 | `"        for item in search_results if isinstance(search_results, list) else []:"` | — |
| [SRC-1AE03B9EC3-L001390](../../agents/web_agent.py#L1390) | 1390 | `"            if not isinstance(item, dict):"` | — |
| [SRC-1AE03B9EC3-L001391](../../agents/web_agent.py#L1391) | 1391 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001392](../../agents/web_agent.py#L1392) | 1392 | `"            url = _public_http_url(item.get(\"url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001393](../../agents/web_agent.py#L1393) | 1393 | `"            if not url:"` | — |
| [SRC-1AE03B9EC3-L001394](../../agents/web_agent.py#L1394) | 1394 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001395](../../agents/web_agent.py#L1395) | 1395 | `"            rows.append({"` | — |
| [SRC-1AE03B9EC3-L001396](../../agents/web_agent.py#L1396) | 1396 | `"                \"title\": _clean_text(item.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001397](../../agents/web_agent.py#L1397) | 1397 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001398](../../agents/web_agent.py#L1398) | 1398 | `"                \"snippet\": _clean_text(item.get(\"content\", \"\"), 1600),"` | — |
| [SRC-1AE03B9EC3-L001399](../../agents/web_agent.py#L1399) | 1399 | `"                \"provider\": \"tavily_search_api\","` | — |
| [SRC-1AE03B9EC3-L001400](../../agents/web_agent.py#L1400) | 1400 | `"                \"provider_rank\": len(rows) + 1,"` | — |
| [SRC-1AE03B9EC3-L001401](../../agents/web_agent.py#L1401) | 1401 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001402](../../agents/web_agent.py#L1402) | 1402 | `"                \"published_at\": _clean_text(item.get(\"published_date\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001403](../../agents/web_agent.py#L1403) | 1403 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001404](../../agents/web_agent.py#L1404) | 1404 | `"            if len(rows) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001405](../../agents/web_agent.py#L1405) | 1405 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001406](../../agents/web_agent.py#L1406) | 1406 | `"        return rows"` | — |
| [SRC-1AE03B9EC3-L001407](../../agents/web_agent.py#L1407) | 1407 | `""` | — |
| [SRC-1AE03B9EC3-L001408](../../agents/web_agent.py#L1408) | 1408 | `"    def _search_news(self, query: str) -> list[dict[str, Any]]:"` | — |
| [SRC-1AE03B9EC3-L001409](../../agents/web_agent.py#L1409) | 1409 | `"        \"\"\"Read the public Google News RSS search feed for freshness-sensitive queries.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001410](../../agents/web_agent.py#L1410) | 1410 | `"        import xml.etree.ElementTree as ET"` | — |
| [SRC-1AE03B9EC3-L001411](../../agents/web_agent.py#L1411) | 1411 | `""` | — |
| [SRC-1AE03B9EC3-L001412](../../agents/web_agent.py#L1412) | 1412 | `"        import httpx"` | — |
| [SRC-1AE03B9EC3-L001413](../../agents/web_agent.py#L1413) | 1413 | `""` | — |
| [SRC-1AE03B9EC3-L001414](../../agents/web_agent.py#L1414) | 1414 | `"        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001415](../../agents/web_agent.py#L1415) | 1415 | `"            \"https://news.google.com/rss/search\","` | — |
| [SRC-1AE03B9EC3-L001416](../../agents/web_agent.py#L1416) | 1416 | `"            params={\"q\": query, \"hl\": \"ar\", \"gl\": \"EG\", \"ceid\": \"EG:ar\"},"` | — |
| [SRC-1AE03B9EC3-L001417](../../agents/web_agent.py#L1417) | 1417 | `"            headers={"` | — |
| [SRC-1AE03B9EC3-L001418](../../agents/web_agent.py#L1418) | 1418 | `"                \"User-Agent\": \"OmaraiResearchBot/1.2\","` | — |
| [SRC-1AE03B9EC3-L001419](../../agents/web_agent.py#L1419) | 1419 | `"                \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001420](../../agents/web_agent.py#L1420) | 1420 | `"            },"` | — |
| [SRC-1AE03B9EC3-L001421](../../agents/web_agent.py#L1421) | 1421 | `"            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001422](../../agents/web_agent.py#L1422) | 1422 | `"            follow_redirects=True,"` | — |
| [SRC-1AE03B9EC3-L001423](../../agents/web_agent.py#L1423) | 1423 | `"        )"` | — |
| [SRC-1AE03B9EC3-L001424](../../agents/web_agent.py#L1424) | 1424 | `"        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001425](../../agents/web_agent.py#L1425) | 1425 | `"            raise RuntimeError(f\"HTTP {response.status_code}\")"` | — |
| [SRC-1AE03B9EC3-L001426](../../agents/web_agent.py#L1426) | 1426 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001427](../../agents/web_agent.py#L1427) | 1427 | `"            root = ET.fromstring(response.content)"` | — |
| [SRC-1AE03B9EC3-L001428](../../agents/web_agent.py#L1428) | 1428 | `"        except ET.ParseError as exc:"` | — |
| [SRC-1AE03B9EC3-L001429](../../agents/web_agent.py#L1429) | 1429 | `"            raise RuntimeError(\"invalid RSS XML\") from exc"` | — |
| [SRC-1AE03B9EC3-L001430](../../agents/web_agent.py#L1430) | 1430 | `"        results: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001431](../../agents/web_agent.py#L1431) | 1431 | `"        for item in root.iter():"` | — |
| [SRC-1AE03B9EC3-L001432](../../agents/web_agent.py#L1432) | 1432 | `"            if item.tag.rsplit(\"}\", 1)[-1] != \"item\":"` | — |
| [SRC-1AE03B9EC3-L001433](../../agents/web_agent.py#L1433) | 1433 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001434](../../agents/web_agent.py#L1434) | 1434 | `"            fields = {"` | — |
| [SRC-1AE03B9EC3-L001435](../../agents/web_agent.py#L1435) | 1435 | `"                child.tag.rsplit(\"}\", 1)[-1]: (child.text or \"\")"` | — |
| [SRC-1AE03B9EC3-L001436](../../agents/web_agent.py#L1436) | 1436 | `"                for child in item"` | — |
| [SRC-1AE03B9EC3-L001437](../../agents/web_agent.py#L1437) | 1437 | `"            }"` | — |
| [SRC-1AE03B9EC3-L001438](../../agents/web_agent.py#L1438) | 1438 | `"            url = _public_http_url(fields.get(\"link\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001439](../../agents/web_agent.py#L1439) | 1439 | `"            if not url or _blocked_source_url(url):"` | — |
| [SRC-1AE03B9EC3-L001440](../../agents/web_agent.py#L1440) | 1440 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001441](../../agents/web_agent.py#L1441) | 1441 | `"            evidence = \" \".join((fields.get(\"title\", \"\"), fields.get(\"description\", \"\")))"` | — |
| [SRC-1AE03B9EC3-L001442](../../agents/web_agent.py#L1442) | 1442 | `"            if _relevance_ratio(query, evidence) < 0.20:"` | — |
| [SRC-1AE03B9EC3-L001443](../../agents/web_agent.py#L1443) | 1443 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L001444](../../agents/web_agent.py#L1444) | 1444 | `"            source_node = next("` | — |
| [SRC-1AE03B9EC3-L001445](../../agents/web_agent.py#L1445) | 1445 | `"                (child for child in item if child.tag.rsplit(\"}\", 1)[-1] == \"source\"),"` | — |
| [SRC-1AE03B9EC3-L001446](../../agents/web_agent.py#L1446) | 1446 | `"                None,"` | — |
| [SRC-1AE03B9EC3-L001447](../../agents/web_agent.py#L1447) | 1447 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001448](../../agents/web_agent.py#L1448) | 1448 | `"            publisher_url = _public_http_url("` | — |
| [SRC-1AE03B9EC3-L001449](../../agents/web_agent.py#L1449) | 1449 | `"                source_node.attrib.get(\"url\", \"\") if source_node is not None else \"\""` | — |
| [SRC-1AE03B9EC3-L001450](../../agents/web_agent.py#L1450) | 1450 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001451](../../agents/web_agent.py#L1451) | 1451 | `"            publisher_name = _clean_text("` | — |
| [SRC-1AE03B9EC3-L001452](../../agents/web_agent.py#L1452) | 1452 | `"                source_node.text if source_node is not None else \"\", 200"` | — |
| [SRC-1AE03B9EC3-L001453](../../agents/web_agent.py#L1453) | 1453 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001454](../../agents/web_agent.py#L1454) | 1454 | `"            publisher_domain = ("` | — |
| [SRC-1AE03B9EC3-L001455](../../agents/web_agent.py#L1455) | 1455 | `"                (urllib.parse.urlparse(publisher_url).hostname or \"\").lower()"` | — |
| [SRC-1AE03B9EC3-L001456](../../agents/web_agent.py#L1456) | 1456 | `"                if publisher_url else \"\""` | — |
| [SRC-1AE03B9EC3-L001457](../../agents/web_agent.py#L1457) | 1457 | `"            )"` | — |
| [SRC-1AE03B9EC3-L001458](../../agents/web_agent.py#L1458) | 1458 | `"            results.append({"` | — |
| [SRC-1AE03B9EC3-L001459](../../agents/web_agent.py#L1459) | 1459 | `"                \"title\": _clean_text(fields.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001460](../../agents/web_agent.py#L1460) | 1460 | `"                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001461](../../agents/web_agent.py#L1461) | 1461 | `"                \"snippet\": _clean_text(fields.get(\"description\", \"\"), 1200),"` | — |
| [SRC-1AE03B9EC3-L001462](../../agents/web_agent.py#L1462) | 1462 | `"                \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001463](../../agents/web_agent.py#L1463) | 1463 | `"                \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001464](../../agents/web_agent.py#L1464) | 1464 | `"                \"provider\": \"google_news_rss\","` | — |
| [SRC-1AE03B9EC3-L001465](../../agents/web_agent.py#L1465) | 1465 | `"                \"provider_rank\": len(results) + 1,"` | — |
| [SRC-1AE03B9EC3-L001466](../../agents/web_agent.py#L1466) | 1466 | `"                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001467](../../agents/web_agent.py#L1467) | 1467 | `"                \"published_at\": _clean_text(fields.get(\"pubDate\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001468](../../agents/web_agent.py#L1468) | 1468 | `"                \"publisher_name\": publisher_name,"` | — |
| [SRC-1AE03B9EC3-L001469](../../agents/web_agent.py#L1469) | 1469 | `"                \"publisher_url\": publisher_url or \"\","` | — |
| [SRC-1AE03B9EC3-L001470](../../agents/web_agent.py#L1470) | 1470 | `"                \"publisher_domain\": publisher_domain,"` | — |
| [SRC-1AE03B9EC3-L001471](../../agents/web_agent.py#L1471) | 1471 | `"            })"` | — |
| [SRC-1AE03B9EC3-L001472](../../agents/web_agent.py#L1472) | 1472 | `"            if len(results) >= MAX_PROVIDER_RESULTS:"` | — |
| [SRC-1AE03B9EC3-L001473](../../agents/web_agent.py#L1473) | 1473 | `"                break"` | — |
| [SRC-1AE03B9EC3-L001474](../../agents/web_agent.py#L1474) | 1474 | `"        return results"` | — |
| [SRC-1AE03B9EC3-L001475](../../agents/web_agent.py#L1475) | 1475 | `""` | — |
| [SRC-1AE03B9EC3-L001476](../../agents/web_agent.py#L1476) | 1476 | `"    def _search_social("` | — |
| [SRC-1AE03B9EC3-L001477](../../agents/web_agent.py#L1477) | 1477 | `"        self, query: str, platforms: list[str]"` | — |
| [SRC-1AE03B9EC3-L001478](../../agents/web_agent.py#L1478) | 1478 | `"    ) -> tuple[list[dict[str, Any]], list[str]]:"` | — |
| [SRC-1AE03B9EC3-L001479](../../agents/web_agent.py#L1479) | 1479 | `"        \"\"\"Search public social content through exposed public endpoints only.\"\"\""` | — |
| [SRC-1AE03B9EC3-L001480](../../agents/web_agent.py#L1480) | 1480 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L001481](../../agents/web_agent.py#L1481) | 1481 | `"            import xml.etree.ElementTree as ET"` | — |
| [SRC-1AE03B9EC3-L001482](../../agents/web_agent.py#L1482) | 1482 | `""` | — |
| [SRC-1AE03B9EC3-L001483](../../agents/web_agent.py#L1483) | 1483 | `"            import httpx"` | — |
| [SRC-1AE03B9EC3-L001484](../../agents/web_agent.py#L1484) | 1484 | `"            from bs4 import BeautifulSoup"` | — |
| [SRC-1AE03B9EC3-L001485](../../agents/web_agent.py#L1485) | 1485 | `"        except ImportError as exc:"` | — |
| [SRC-1AE03B9EC3-L001486](../../agents/web_agent.py#L1486) | 1486 | `"            raise AgentDependencyError("` | — |
| [SRC-1AE03B9EC3-L001487](../../agents/web_agent.py#L1487) | 1487 | `"                \"حزم البحث الاجتماعي غير مثبتة. نفّذ: python -m pip install -e .\""` | — |
| [SRC-1AE03B9EC3-L001488](../../agents/web_agent.py#L1488) | 1488 | `"            ) from exc"` | — |
| [SRC-1AE03B9EC3-L001489](../../agents/web_agent.py#L1489) | 1489 | `""` | — |
| [SRC-1AE03B9EC3-L001490](../../agents/web_agent.py#L1490) | 1490 | `"        results: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L001491](../../agents/web_agent.py#L1491) | 1491 | `"        warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L001492](../../agents/web_agent.py#L1492) | 1492 | `"        headers = {"` | — |
| [SRC-1AE03B9EC3-L001493](../../agents/web_agent.py#L1493) | 1493 | `"            \"User-Agent\": \"OmaraiResearchBot/1.0 (public-content search; no login)\","` | — |
| [SRC-1AE03B9EC3-L001494](../../agents/web_agent.py#L1494) | 1494 | `"            \"Accept-Language\": \"ar,en;q=0.9\","` | — |
| [SRC-1AE03B9EC3-L001495](../../agents/web_agent.py#L1495) | 1495 | `"        }"` | — |
| [SRC-1AE03B9EC3-L001496](../../agents/web_agent.py#L1496) | 1496 | `""` | — |
| [SRC-1AE03B9EC3-L001497](../../agents/web_agent.py#L1497) | 1497 | `"        reddit_client_id = os.getenv(\"REDDIT_CLIENT_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001498](../../agents/web_agent.py#L1498) | 1498 | `"        reddit_client_secret = os.getenv(\"REDDIT_CLIENT_SECRET\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001499](../../agents/web_agent.py#L1499) | 1499 | `"        reddit_user_agent = os.getenv("` | — |
| [SRC-1AE03B9EC3-L001500](../../agents/web_agent.py#L1500) | 1500 | `"            \"REDDIT_USER_AGENT\","` | — |
| [SRC-1AE03B9EC3-L001501](../../agents/web_agent.py#L1501) | 1501 | `"            \"web:omarai-research-agent:v0.3 (public-content research)\","` | — |
| [SRC-1AE03B9EC3-L001502](../../agents/web_agent.py#L1502) | 1502 | `"        ).strip()"` | — |
| [SRC-1AE03B9EC3-L001503](../../agents/web_agent.py#L1503) | 1503 | `"        if \"reddit\" in platforms and reddit_client_id and reddit_client_secret:"` | — |
| [SRC-1AE03B9EC3-L001504](../../agents/web_agent.py#L1504) | 1504 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001505](../../agents/web_agent.py#L1505) | 1505 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001506](../../agents/web_agent.py#L1506) | 1506 | `"                token_response = httpx.post("` | — |
| [SRC-1AE03B9EC3-L001507](../../agents/web_agent.py#L1507) | 1507 | `"                    \"https://www.reddit.com/api/v1/access_token\","` | — |
| [SRC-1AE03B9EC3-L001508](../../agents/web_agent.py#L1508) | 1508 | `"                    data={\"grant_type\": \"client_credentials\"},"` | — |
| [SRC-1AE03B9EC3-L001509](../../agents/web_agent.py#L1509) | 1509 | `"                    auth=(reddit_client_id, reddit_client_secret),"` | — |
| [SRC-1AE03B9EC3-L001510](../../agents/web_agent.py#L1510) | 1510 | `"                    headers={\"User-Agent\": reddit_user_agent},"` | — |
| [SRC-1AE03B9EC3-L001511](../../agents/web_agent.py#L1511) | 1511 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001512](../../agents/web_agent.py#L1512) | 1512 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001513](../../agents/web_agent.py#L1513) | 1513 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001514](../../agents/web_agent.py#L1514) | 1514 | `"                if token_response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001515](../../agents/web_agent.py#L1515) | 1515 | `"                    access_token = token_response.json().get(\"access_token\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001516](../../agents/web_agent.py#L1516) | 1516 | `"                    if access_token:"` | — |
| [SRC-1AE03B9EC3-L001517](../../agents/web_agent.py#L1517) | 1517 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001518](../../agents/web_agent.py#L1518) | 1518 | `"                        search_response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001519](../../agents/web_agent.py#L1519) | 1519 | `"                            \"https://oauth.reddit.com/search\","` | — |
| [SRC-1AE03B9EC3-L001520](../../agents/web_agent.py#L1520) | 1520 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L001521](../../agents/web_agent.py#L1521) | 1521 | `"                                \"q\": query,"` | — |
| [SRC-1AE03B9EC3-L001522](../../agents/web_agent.py#L1522) | 1522 | `"                                \"sort\": \"relevance\","` | — |
| [SRC-1AE03B9EC3-L001523](../../agents/web_agent.py#L1523) | 1523 | `"                                \"t\": \"all\","` | — |
| [SRC-1AE03B9EC3-L001524](../../agents/web_agent.py#L1524) | 1524 | `"                                \"limit\": 10,"` | — |
| [SRC-1AE03B9EC3-L001525](../../agents/web_agent.py#L1525) | 1525 | `"                                \"type\": \"link\","` | — |
| [SRC-1AE03B9EC3-L001526](../../agents/web_agent.py#L1526) | 1526 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L001527](../../agents/web_agent.py#L1527) | 1527 | `"                            headers={"` | — |
| [SRC-1AE03B9EC3-L001528](../../agents/web_agent.py#L1528) | 1528 | `"                                **headers,"` | — |
| [SRC-1AE03B9EC3-L001529](../../agents/web_agent.py#L1529) | 1529 | `"                                \"User-Agent\": reddit_user_agent,"` | — |
| [SRC-1AE03B9EC3-L001530](../../agents/web_agent.py#L1530) | 1530 | `"                                \"Authorization\": \"Bearer \" + access_token,"` | — |
| [SRC-1AE03B9EC3-L001531](../../agents/web_agent.py#L1531) | 1531 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L001532](../../agents/web_agent.py#L1532) | 1532 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001533](../../agents/web_agent.py#L1533) | 1533 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001534](../../agents/web_agent.py#L1534) | 1534 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L001535](../../agents/web_agent.py#L1535) | 1535 | `"                        if search_response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001536](../../agents/web_agent.py#L1536) | 1536 | `"                            children = search_response.json().get(\"data\", {}).get(\"children\", [])"` | — |
| [SRC-1AE03B9EC3-L001537](../../agents/web_agent.py#L1537) | 1537 | `"                            rank = 0"` | — |
| [SRC-1AE03B9EC3-L001538](../../agents/web_agent.py#L1538) | 1538 | `"                            for child in children:"` | — |
| [SRC-1AE03B9EC3-L001539](../../agents/web_agent.py#L1539) | 1539 | `"                                post = child.get(\"data\", {}) if isinstance(child, dict) else {}"` | — |
| [SRC-1AE03B9EC3-L001540](../../agents/web_agent.py#L1540) | 1540 | `"                                permalink = str(post.get(\"permalink\") or \"\")"` | — |
| [SRC-1AE03B9EC3-L001541](../../agents/web_agent.py#L1541) | 1541 | `"                                url = _public_http_url("` | — |
| [SRC-1AE03B9EC3-L001542](../../agents/web_agent.py#L1542) | 1542 | `"                                    permalink if permalink.startswith(\"http\")"` | — |
| [SRC-1AE03B9EC3-L001543](../../agents/web_agent.py#L1543) | 1543 | `"                                    else \"https://www.reddit.com\" + permalink"` | — |
| [SRC-1AE03B9EC3-L001544](../../agents/web_agent.py#L1544) | 1544 | `"                                )"` | — |
| [SRC-1AE03B9EC3-L001545](../../agents/web_agent.py#L1545) | 1545 | `"                                if not url:"` | — |
| [SRC-1AE03B9EC3-L001546](../../agents/web_agent.py#L1546) | 1546 | `"                                    continue"` | — |
| [SRC-1AE03B9EC3-L001547](../../agents/web_agent.py#L1547) | 1547 | `"                                rank += 1"` | — |
| [SRC-1AE03B9EC3-L001548](../../agents/web_agent.py#L1548) | 1548 | `"                                snippet = _clean_text(post.get(\"selftext\") or \"\", 1000)"` | — |
| [SRC-1AE03B9EC3-L001549](../../agents/web_agent.py#L1549) | 1549 | `"                                metrics = []"` | — |
| [SRC-1AE03B9EC3-L001550](../../agents/web_agent.py#L1550) | 1550 | `"                                if post.get(\"score\") is not None:"` | — |
| [SRC-1AE03B9EC3-L001551](../../agents/web_agent.py#L1551) | 1551 | `"                                    metrics.append(\"score=\" + str(post[\"score\"]))"` | — |
| [SRC-1AE03B9EC3-L001552](../../agents/web_agent.py#L1552) | 1552 | `"                                if post.get(\"num_comments\") is not None:"` | — |
| [SRC-1AE03B9EC3-L001553](../../agents/web_agent.py#L1553) | 1553 | `"                                    metrics.append(\"comments=\" + str(post[\"num_comments\"]))"` | — |
| [SRC-1AE03B9EC3-L001554](../../agents/web_agent.py#L1554) | 1554 | `"                                if metrics:"` | — |
| [SRC-1AE03B9EC3-L001555](../../agents/web_agent.py#L1555) | 1555 | `"                                    snippet = (snippet + \" \| \" if snippet else \"\") + \", \".join(metrics)"` | — |
| [SRC-1AE03B9EC3-L001556](../../agents/web_agent.py#L1556) | 1556 | `"                                results.append({"` | — |
| [SRC-1AE03B9EC3-L001557](../../agents/web_agent.py#L1557) | 1557 | `"                                    \"title\": _clean_text(post.get(\"title\") or \"Reddit post\", 300),"` | — |
| [SRC-1AE03B9EC3-L001558](../../agents/web_agent.py#L1558) | 1558 | `"                                    \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001559](../../agents/web_agent.py#L1559) | 1559 | `"                                    \"snippet\": snippet,"` | — |
| [SRC-1AE03B9EC3-L001560](../../agents/web_agent.py#L1560) | 1560 | `"                                    \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001561](../../agents/web_agent.py#L1561) | 1561 | `"                                    \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001562](../../agents/web_agent.py#L1562) | 1562 | `"                                    \"provider\": \"reddit_oauth_api\","` | — |
| [SRC-1AE03B9EC3-L001563](../../agents/web_agent.py#L1563) | 1563 | `"                                    \"provider_rank\": rank,"` | — |
| [SRC-1AE03B9EC3-L001564](../../agents/web_agent.py#L1564) | 1564 | `"                                    \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001565](../../agents/web_agent.py#L1565) | 1565 | `"                                    \"published_at\": _clean_text(str(post.get(\"created_utc\") or \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001566](../../agents/web_agent.py#L1566) | 1566 | `"                                })"` | — |
| [SRC-1AE03B9EC3-L001567](../../agents/web_agent.py#L1567) | 1567 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L001568](../../agents/web_agent.py#L1568) | 1568 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L001569](../../agents/web_agent.py#L1569) | 1569 | `"                                f\"Reddit OAuth search unavailable (HTTP {search_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L001570](../../agents/web_agent.py#L1570) | 1570 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L001571](../../agents/web_agent.py#L1571) | 1571 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L001572](../../agents/web_agent.py#L1572) | 1572 | `"                        warnings.append(\"Reddit OAuth did not return an access token.\")"` | — |
| [SRC-1AE03B9EC3-L001573](../../agents/web_agent.py#L1573) | 1573 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001574](../../agents/web_agent.py#L1574) | 1574 | `"                    warnings.append("` | — |
| [SRC-1AE03B9EC3-L001575](../../agents/web_agent.py#L1575) | 1575 | `"                        f\"Reddit OAuth authentication unavailable (HTTP {token_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L001576](../../agents/web_agent.py#L1576) | 1576 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L001577](../../agents/web_agent.py#L1577) | 1577 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L001578](../../agents/web_agent.py#L1578) | 1578 | `"                warnings.append(\"Reddit OAuth search failed for this request.\")"` | — |
| [SRC-1AE03B9EC3-L001579](../../agents/web_agent.py#L1579) | 1579 | `""` | — |
| [SRC-1AE03B9EC3-L001580](../../agents/web_agent.py#L1580) | 1580 | `"        if \"reddit\" in platforms and not any("` | — |
| [SRC-1AE03B9EC3-L001581](../../agents/web_agent.py#L1581) | 1581 | `"            row.get(\"provider\") == \"reddit_oauth_api\" for row in results"` | — |
| [SRC-1AE03B9EC3-L001582](../../agents/web_agent.py#L1582) | 1582 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L001583](../../agents/web_agent.py#L1583) | 1583 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001584](../../agents/web_agent.py#L1584) | 1584 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001585](../../agents/web_agent.py#L1585) | 1585 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001586](../../agents/web_agent.py#L1586) | 1586 | `"                    \"https://www.reddit.com/search.rss\","` | — |
| [SRC-1AE03B9EC3-L001587](../../agents/web_agent.py#L1587) | 1587 | `"                    params={\"q\": query, \"sort\": \"relevance\", \"t\": \"all\", \"limit\": \"8\"},"` | — |
| [SRC-1AE03B9EC3-L001588](../../agents/web_agent.py#L1588) | 1588 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L001589](../../agents/web_agent.py#L1589) | 1589 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001590](../../agents/web_agent.py#L1590) | 1590 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001591](../../agents/web_agent.py#L1591) | 1591 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001592](../../agents/web_agent.py#L1592) | 1592 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001593](../../agents/web_agent.py#L1593) | 1593 | `"                    root = ET.fromstring(response.content)"` | — |
| [SRC-1AE03B9EC3-L001594](../../agents/web_agent.py#L1594) | 1594 | `"                    for item in root.iter():"` | — |
| [SRC-1AE03B9EC3-L001595](../../agents/web_agent.py#L1595) | 1595 | `"                        if item.tag.rsplit(\"}\", 1)[-1] != \"item\":"` | — |
| [SRC-1AE03B9EC3-L001596](../../agents/web_agent.py#L1596) | 1596 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001597](../../agents/web_agent.py#L1597) | 1597 | `"                        fields = {"` | — |
| [SRC-1AE03B9EC3-L001598](../../agents/web_agent.py#L1598) | 1598 | `"                            child.tag.rsplit(\"}\", 1)[-1]: (child.text or \"\")"` | — |
| [SRC-1AE03B9EC3-L001599](../../agents/web_agent.py#L1599) | 1599 | `"                            for child in item"` | — |
| [SRC-1AE03B9EC3-L001600](../../agents/web_agent.py#L1600) | 1600 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L001601](../../agents/web_agent.py#L1601) | 1601 | `"                        url = _public_http_url(fields.get(\"link\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001602](../../agents/web_agent.py#L1602) | 1602 | `"                        if not url or \"reddit.com/\" not in url:"` | — |
| [SRC-1AE03B9EC3-L001603](../../agents/web_agent.py#L1603) | 1603 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001604](../../agents/web_agent.py#L1604) | 1604 | `"                        description = BeautifulSoup("` | — |
| [SRC-1AE03B9EC3-L001605](../../agents/web_agent.py#L1605) | 1605 | `"                            fields.get(\"description\", \"\"), \"html.parser\""` | — |
| [SRC-1AE03B9EC3-L001606](../../agents/web_agent.py#L1606) | 1606 | `"                        ).get_text(\" \", strip=True)"` | — |
| [SRC-1AE03B9EC3-L001607](../../agents/web_agent.py#L1607) | 1607 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L001608](../../agents/web_agent.py#L1608) | 1608 | `"                            \"title\": _clean_text(fields.get(\"title\", \"\"), 300),"` | — |
| [SRC-1AE03B9EC3-L001609](../../agents/web_agent.py#L1609) | 1609 | `"                            \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001610](../../agents/web_agent.py#L1610) | 1610 | `"                            \"snippet\": _clean_text(description, 1200),"` | — |
| [SRC-1AE03B9EC3-L001611](../../agents/web_agent.py#L1611) | 1611 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001612](../../agents/web_agent.py#L1612) | 1612 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001613](../../agents/web_agent.py#L1613) | 1613 | `"                            \"provider\": \"reddit_public_rss\","` | — |
| [SRC-1AE03B9EC3-L001614](../../agents/web_agent.py#L1614) | 1614 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L001615](../../agents/web_agent.py#L1615) | 1615 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L001616](../../agents/web_agent.py#L1616) | 1616 | `"                                if row.get(\"provider\") == \"reddit_public_rss\""` | — |
| [SRC-1AE03B9EC3-L001617](../../agents/web_agent.py#L1617) | 1617 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L001618](../../agents/web_agent.py#L1618) | 1618 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001619](../../agents/web_agent.py#L1619) | 1619 | `"                            \"published_at\": _clean_text(fields.get(\"pubDate\", \"\"), 100),"` | — |
| [SRC-1AE03B9EC3-L001620](../../agents/web_agent.py#L1620) | 1620 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L001621](../../agents/web_agent.py#L1621) | 1621 | `"                        if sum(row.get(\"provider\") == \"reddit_public_rss\" for row in results) >= 8:"` | — |
| [SRC-1AE03B9EC3-L001622](../../agents/web_agent.py#L1622) | 1622 | `"                            break"` | — |
| [SRC-1AE03B9EC3-L001623](../../agents/web_agent.py#L1623) | 1623 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001624](../../agents/web_agent.py#L1624) | 1624 | `"                    warnings.append(f\"Reddit public RSS unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L001625](../../agents/web_agent.py#L1625) | 1625 | `"            except (httpx.HTTPError, OSError, ValueError, ET.ParseError):"` | — |
| [SRC-1AE03B9EC3-L001626](../../agents/web_agent.py#L1626) | 1626 | `"                warnings.append(\"Reddit public RSS unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L001627](../../agents/web_agent.py#L1627) | 1627 | `""` | — |
| [SRC-1AE03B9EC3-L001628](../../agents/web_agent.py#L1628) | 1628 | `"        if \"bluesky\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L001629](../../agents/web_agent.py#L1629) | 1629 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001630](../../agents/web_agent.py#L1630) | 1630 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001631](../../agents/web_agent.py#L1631) | 1631 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001632](../../agents/web_agent.py#L1632) | 1632 | `"                    \"https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts\","` | — |
| [SRC-1AE03B9EC3-L001633](../../agents/web_agent.py#L1633) | 1633 | `"                    params={\"q\": query, \"limit\": 10},"` | — |
| [SRC-1AE03B9EC3-L001634](../../agents/web_agent.py#L1634) | 1634 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L001635](../../agents/web_agent.py#L1635) | 1635 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001636](../../agents/web_agent.py#L1636) | 1636 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001637](../../agents/web_agent.py#L1637) | 1637 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001638](../../agents/web_agent.py#L1638) | 1638 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001639](../../agents/web_agent.py#L1639) | 1639 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L001640](../../agents/web_agent.py#L1640) | 1640 | `"                    for item in data.get(\"posts\", []):"` | — |
| [SRC-1AE03B9EC3-L001641](../../agents/web_agent.py#L1641) | 1641 | `"                        post = item.get(\"post\", {})"` | — |
| [SRC-1AE03B9EC3-L001642](../../agents/web_agent.py#L1642) | 1642 | `"                        record = post.get(\"record\", {})"` | — |
| [SRC-1AE03B9EC3-L001643](../../agents/web_agent.py#L1643) | 1643 | `"                        author = post.get(\"author\", {})"` | — |
| [SRC-1AE03B9EC3-L001644](../../agents/web_agent.py#L1644) | 1644 | `"                        uri = post.get(\"uri\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001645](../../agents/web_agent.py#L1645) | 1645 | `"                        rkey = uri.rsplit(\"/\", 1)[-1]"` | — |
| [SRC-1AE03B9EC3-L001646](../../agents/web_agent.py#L1646) | 1646 | `"                        handle = author.get(\"handle\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001647](../../agents/web_agent.py#L1647) | 1647 | `"                        if not handle or not rkey:"` | — |
| [SRC-1AE03B9EC3-L001648](../../agents/web_agent.py#L1648) | 1648 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001649](../../agents/web_agent.py#L1649) | 1649 | `"                        url = f\"https://bsky.app/profile/{handle}/post/{rkey}\""` | — |
| [SRC-1AE03B9EC3-L001650](../../agents/web_agent.py#L1650) | 1650 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L001651](../../agents/web_agent.py#L1651) | 1651 | `"                            \"title\": _clean_text(author.get(\"displayName\") or handle, 300),"` | — |
| [SRC-1AE03B9EC3-L001652](../../agents/web_agent.py#L1652) | 1652 | `"                            \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001653](../../agents/web_agent.py#L1653) | 1653 | `"                            \"snippet\": _clean_text(record.get(\"text\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L001654](../../agents/web_agent.py#L1654) | 1654 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001655](../../agents/web_agent.py#L1655) | 1655 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001656](../../agents/web_agent.py#L1656) | 1656 | `"                            \"provider\": \"bluesky_public_search\","` | — |
| [SRC-1AE03B9EC3-L001657](../../agents/web_agent.py#L1657) | 1657 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L001658](../../agents/web_agent.py#L1658) | 1658 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L001659](../../agents/web_agent.py#L1659) | 1659 | `"                                if row.get(\"provider\") == \"bluesky_public_search\""` | — |
| [SRC-1AE03B9EC3-L001660](../../agents/web_agent.py#L1660) | 1660 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L001661](../../agents/web_agent.py#L1661) | 1661 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001662](../../agents/web_agent.py#L1662) | 1662 | `"                            \"published_at\": _clean_text(post.get(\"indexedAt\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L001663](../../agents/web_agent.py#L1663) | 1663 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L001664](../../agents/web_agent.py#L1664) | 1664 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001665](../../agents/web_agent.py#L1665) | 1665 | `"                    warnings.append(f\"Bluesky public search unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L001666](../../agents/web_agent.py#L1666) | 1666 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L001667](../../agents/web_agent.py#L1667) | 1667 | `"                warnings.append(\"Bluesky public search unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L001668](../../agents/web_agent.py#L1668) | 1668 | `""` | — |
| [SRC-1AE03B9EC3-L001669](../../agents/web_agent.py#L1669) | 1669 | `"        if \"facebook\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L001670](../../agents/web_agent.py#L1670) | 1670 | `"            fb_token = os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001671](../../agents/web_agent.py#L1671) | 1671 | `"            page_ids = ["` | — |
| [SRC-1AE03B9EC3-L001672](../../agents/web_agent.py#L1672) | 1672 | `"                value.strip()"` | — |
| [SRC-1AE03B9EC3-L001673](../../agents/web_agent.py#L1673) | 1673 | `"                for value in os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").split(\",\")"` | — |
| [SRC-1AE03B9EC3-L001674](../../agents/web_agent.py#L1674) | 1674 | `"                if value.strip()"` | — |
| [SRC-1AE03B9EC3-L001675](../../agents/web_agent.py#L1675) | 1675 | `"            ][:5]"` | — |
| [SRC-1AE03B9EC3-L001676](../../agents/web_agent.py#L1676) | 1676 | `"            graph_version = os.getenv(\"META_GRAPH_VERSION\", \"v25.0\").strip()"` | — |
| [SRC-1AE03B9EC3-L001677](../../agents/web_agent.py#L1677) | 1677 | `"            if fb_token and page_ids:"` | — |
| [SRC-1AE03B9EC3-L001678](../../agents/web_agent.py#L1678) | 1678 | `"                # Scope direct reading to page IDs supplied by the operator and the"` | — |
| [SRC-1AE03B9EC3-L001679](../../agents/web_agent.py#L1679) | 1679 | `"                # permissions granted to this token. This is not global Facebook search."` | — |
| [SRC-1AE03B9EC3-L001680](../../agents/web_agent.py#L1680) | 1680 | `"                query_terms = {"` | — |
| [SRC-1AE03B9EC3-L001681](../../agents/web_agent.py#L1681) | 1681 | `"                    word.casefold()"` | — |
| [SRC-1AE03B9EC3-L001682](../../agents/web_agent.py#L1682) | 1682 | `"                    for word in re.findall(r\"[\\w\\u0600-\\u06FF]+\", query, flags=re.UNICODE)"` | — |
| [SRC-1AE03B9EC3-L001683](../../agents/web_agent.py#L1683) | 1683 | `"                    if len(word) >= 3"` | — |
| [SRC-1AE03B9EC3-L001684](../../agents/web_agent.py#L1684) | 1684 | `"                }"` | — |
| [SRC-1AE03B9EC3-L001685](../../agents/web_agent.py#L1685) | 1685 | `"                for page_id in page_ids:"` | — |
| [SRC-1AE03B9EC3-L001686](../../agents/web_agent.py#L1686) | 1686 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L001687](../../agents/web_agent.py#L1687) | 1687 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001688](../../agents/web_agent.py#L1688) | 1688 | `"                        response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001689](../../agents/web_agent.py#L1689) | 1689 | `"                            f\"https://graph.facebook.com/{graph_version}/{page_id}/posts\","` | — |
| [SRC-1AE03B9EC3-L001690](../../agents/web_agent.py#L1690) | 1690 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L001691](../../agents/web_agent.py#L1691) | 1691 | `"                                \"fields\": ("` | — |
| [SRC-1AE03B9EC3-L001692](../../agents/web_agent.py#L1692) | 1692 | `"                                    \"message,permalink_url,created_time,\""` | — |
| [SRC-1AE03B9EC3-L001693](../../agents/web_agent.py#L1693) | 1693 | `"                                    \"comments.limit(10){message,created_time,like_count}\""` | — |
| [SRC-1AE03B9EC3-L001694](../../agents/web_agent.py#L1694) | 1694 | `"                                ),"` | — |
| [SRC-1AE03B9EC3-L001695](../../agents/web_agent.py#L1695) | 1695 | `"                                \"limit\": 10,"` | — |
| [SRC-1AE03B9EC3-L001696](../../agents/web_agent.py#L1696) | 1696 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L001697](../../agents/web_agent.py#L1697) | 1697 | `"                            headers={"` | — |
| [SRC-1AE03B9EC3-L001698](../../agents/web_agent.py#L1698) | 1698 | `"                                **headers,"` | — |
| [SRC-1AE03B9EC3-L001699](../../agents/web_agent.py#L1699) | 1699 | `"                                \"Authorization\": \"Bearer \" + fb_token,"` | — |
| [SRC-1AE03B9EC3-L001700](../../agents/web_agent.py#L1700) | 1700 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L001701](../../agents/web_agent.py#L1701) | 1701 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001702](../../agents/web_agent.py#L1702) | 1702 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001703](../../agents/web_agent.py#L1703) | 1703 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L001704](../../agents/web_agent.py#L1704) | 1704 | `"                        if response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001705](../../agents/web_agent.py#L1705) | 1705 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L001706](../../agents/web_agent.py#L1706) | 1706 | `"                                \"Facebook Pages API unavailable for one configured page \""` | — |
| [SRC-1AE03B9EC3-L001707](../../agents/web_agent.py#L1707) | 1707 | `"                                f\"(HTTP {response.status_code}); verify page ownership, token and permissions.\""` | — |
| [SRC-1AE03B9EC3-L001708](../../agents/web_agent.py#L1708) | 1708 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L001709](../../agents/web_agent.py#L1709) | 1709 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001710](../../agents/web_agent.py#L1710) | 1710 | `"                        posts = response.json().get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L001711](../../agents/web_agent.py#L1711) | 1711 | `"                        rank = 0"` | — |
| [SRC-1AE03B9EC3-L001712](../../agents/web_agent.py#L1712) | 1712 | `"                        for post in posts:"` | — |
| [SRC-1AE03B9EC3-L001713](../../agents/web_agent.py#L1713) | 1713 | `"                            message = _clean_text(post.get(\"message\") or \"\", 1400)"` | — |
| [SRC-1AE03B9EC3-L001714](../../agents/web_agent.py#L1714) | 1714 | `"                            comments = post.get(\"comments\", {}).get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L001715](../../agents/web_agent.py#L1715) | 1715 | `"                            comment_text = ["` | — |
| [SRC-1AE03B9EC3-L001716](../../agents/web_agent.py#L1716) | 1716 | `"                                _clean_text(item.get(\"message\") or \"\", 500)"` | — |
| [SRC-1AE03B9EC3-L001717](../../agents/web_agent.py#L1717) | 1717 | `"                                for item in comments"` | — |
| [SRC-1AE03B9EC3-L001718](../../agents/web_agent.py#L1718) | 1718 | `"                                if isinstance(item, dict) and item.get(\"message\")"` | — |
| [SRC-1AE03B9EC3-L001719](../../agents/web_agent.py#L1719) | 1719 | `"                            ]"` | — |
| [SRC-1AE03B9EC3-L001720](../../agents/web_agent.py#L1720) | 1720 | `"                            searchable = (message + \" \" + \" \".join(comment_text)).casefold()"` | — |
| [SRC-1AE03B9EC3-L001721](../../agents/web_agent.py#L1721) | 1721 | `"                            matched = sum(term in searchable for term in query_terms)"` | — |
| [SRC-1AE03B9EC3-L001722](../../agents/web_agent.py#L1722) | 1722 | `"                            if query_terms and matched == 0:"` | — |
| [SRC-1AE03B9EC3-L001723](../../agents/web_agent.py#L1723) | 1723 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L001724](../../agents/web_agent.py#L1724) | 1724 | `"                            permalink = _public_http_url(post.get(\"permalink_url\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001725](../../agents/web_agent.py#L1725) | 1725 | `"                            if not permalink:"` | — |
| [SRC-1AE03B9EC3-L001726](../../agents/web_agent.py#L1726) | 1726 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L001727](../../agents/web_agent.py#L1727) | 1727 | `"                            rank += 1"` | — |
| [SRC-1AE03B9EC3-L001728](../../agents/web_agent.py#L1728) | 1728 | `"                            excerpt = message"` | — |
| [SRC-1AE03B9EC3-L001729](../../agents/web_agent.py#L1729) | 1729 | `"                            if comment_text:"` | — |
| [SRC-1AE03B9EC3-L001730](../../agents/web_agent.py#L1730) | 1730 | `"                                excerpt = ("` | — |
| [SRC-1AE03B9EC3-L001731](../../agents/web_agent.py#L1731) | 1731 | `"                                    excerpt + \"\\n\\nتعليقات عامة على المنشور:\\n\""` | — |
| [SRC-1AE03B9EC3-L001732](../../agents/web_agent.py#L1732) | 1732 | `"                                    if excerpt else \"تعليقات عامة على المنشور:\\n\""` | — |
| [SRC-1AE03B9EC3-L001733](../../agents/web_agent.py#L1733) | 1733 | `"                                ) + \"\\n— \".join(comment_text)"` | — |
| [SRC-1AE03B9EC3-L001734](../../agents/web_agent.py#L1734) | 1734 | `"                            results.append({"` | — |
| [SRC-1AE03B9EC3-L001735](../../agents/web_agent.py#L1735) | 1735 | `"                                \"title\": _clean_text(message or \"Facebook public Page post\", 300),"` | — |
| [SRC-1AE03B9EC3-L001736](../../agents/web_agent.py#L1736) | 1736 | `"                                \"url\": permalink,"` | — |
| [SRC-1AE03B9EC3-L001737](../../agents/web_agent.py#L1737) | 1737 | `"                                \"snippet\": _clean_text(excerpt, 1800),"` | — |
| [SRC-1AE03B9EC3-L001738](../../agents/web_agent.py#L1738) | 1738 | `"                                \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001739](../../agents/web_agent.py#L1739) | 1739 | `"                                \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001740](../../agents/web_agent.py#L1740) | 1740 | `"                                \"provider\": \"facebook_pages_api\","` | — |
| [SRC-1AE03B9EC3-L001741](../../agents/web_agent.py#L1741) | 1741 | `"                                \"provider_rank\": rank,"` | — |
| [SRC-1AE03B9EC3-L001742](../../agents/web_agent.py#L1742) | 1742 | `"                                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001743](../../agents/web_agent.py#L1743) | 1743 | `"                                \"published_at\": _clean_text(post.get(\"created_time\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L001744](../../agents/web_agent.py#L1744) | 1744 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L001745](../../agents/web_agent.py#L1745) | 1745 | `"                            if rank >= 10:"` | — |
| [SRC-1AE03B9EC3-L001746](../../agents/web_agent.py#L1746) | 1746 | `"                                break"` | — |
| [SRC-1AE03B9EC3-L001747](../../agents/web_agent.py#L1747) | 1747 | `"                    except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L001748](../../agents/web_agent.py#L1748) | 1748 | `"                        warnings.append(\"Facebook Pages API failed for one configured page.\")"` | — |
| [SRC-1AE03B9EC3-L001749](../../agents/web_agent.py#L1749) | 1749 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L001750](../../agents/web_agent.py#L1750) | 1750 | `"                warnings.append("` | — |
| [SRC-1AE03B9EC3-L001751](../../agents/web_agent.py#L1751) | 1751 | `"                    \"Facebook direct API is not configured for specific pages; indexed public Facebook pages are still searched.\""` | — |
| [SRC-1AE03B9EC3-L001752](../../agents/web_agent.py#L1752) | 1752 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001753](../../agents/web_agent.py#L1753) | 1753 | `""` | — |
| [SRC-1AE03B9EC3-L001754](../../agents/web_agent.py#L1754) | 1754 | `"        if \"instagram\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L001755](../../agents/web_agent.py#L1755) | 1755 | `"            ig_user_id = os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001756](../../agents/web_agent.py#L1756) | 1756 | `"            ig_token = os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L001757](../../agents/web_agent.py#L1757) | 1757 | `"            graph_version = os.getenv(\"META_GRAPH_VERSION\", \"v25.0\").strip()"` | — |
| [SRC-1AE03B9EC3-L001758](../../agents/web_agent.py#L1758) | 1758 | `"            if ig_user_id and ig_token:"` | — |
| [SRC-1AE03B9EC3-L001759](../../agents/web_agent.py#L1759) | 1759 | `"                # The official Hashtag Search API returns public hashtag media only."` | — |
| [SRC-1AE03B9EC3-L001760](../../agents/web_agent.py#L1760) | 1760 | `"                # It does not search every Instagram post or bypass private accounts."` | — |
| [SRC-1AE03B9EC3-L001761](../../agents/web_agent.py#L1761) | 1761 | `"                hashtags = re.findall(r\"#([\\w\\u0600-\\u06FF]+)\", query, flags=re.UNICODE)"` | — |
| [SRC-1AE03B9EC3-L001762](../../agents/web_agent.py#L1762) | 1762 | `"                if not hashtags:"` | — |
| [SRC-1AE03B9EC3-L001763](../../agents/web_agent.py#L1763) | 1763 | `"                    words = re.findall(r\"[\\w\\u0600-\\u06FF]+\", query, flags=re.UNICODE)"` | — |
| [SRC-1AE03B9EC3-L001764](../../agents/web_agent.py#L1764) | 1764 | `"                    stopwords = {"` | — |
| [SRC-1AE03B9EC3-L001765](../../agents/web_agent.py#L1765) | 1765 | `"                        \"ابحث\", \"بحث\", \"عن\", \"في\", \"على\", \"من\", \"مع\", \"تجارب\","` | — |
| [SRC-1AE03B9EC3-L001766](../../agents/web_agent.py#L1766) | 1766 | `"                        \"الناس\", \"العملاء\", \"منشورات\", \"تعليقات\", \"مواقع\", \"التواصل\","` | — |
| [SRC-1AE03B9EC3-L001767](../../agents/web_agent.py#L1767) | 1767 | `"                        \"الاجتماعي\", \"public\", \"search\", \"social\", \"media\", \"posts\","` | — |
| [SRC-1AE03B9EC3-L001768](../../agents/web_agent.py#L1768) | 1768 | `"                        \"find\", \"about\", \"with\", \"the\", \"and\", \"for\","` | — |
| [SRC-1AE03B9EC3-L001769](../../agents/web_agent.py#L1769) | 1769 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L001770](../../agents/web_agent.py#L1770) | 1770 | `"                    useful = ["` | — |
| [SRC-1AE03B9EC3-L001771](../../agents/web_agent.py#L1771) | 1771 | `"                        word for word in words"` | — |
| [SRC-1AE03B9EC3-L001772](../../agents/web_agent.py#L1772) | 1772 | `"                        if len(word) >= 3 and word.casefold() not in stopwords"` | — |
| [SRC-1AE03B9EC3-L001773](../../agents/web_agent.py#L1773) | 1773 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L001774](../../agents/web_agent.py#L1774) | 1774 | `"                    if useful:"` | — |
| [SRC-1AE03B9EC3-L001775](../../agents/web_agent.py#L1775) | 1775 | `"                        hashtags = [\"_\".join(useful[:3])]"` | — |
| [SRC-1AE03B9EC3-L001776](../../agents/web_agent.py#L1776) | 1776 | `"                # Meta limits unique hashtag searches over a rolling week; keep this"` | — |
| [SRC-1AE03B9EC3-L001777](../../agents/web_agent.py#L1777) | 1777 | `"                # connector conservative and use no more than two tags per user request."` | — |
| [SRC-1AE03B9EC3-L001778](../../agents/web_agent.py#L1778) | 1778 | `"                for hashtag in list(dict.fromkeys(hashtags))[:1]:"` | — |
| [SRC-1AE03B9EC3-L001779](../../agents/web_agent.py#L1779) | 1779 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L001780](../../agents/web_agent.py#L1780) | 1780 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001781](../../agents/web_agent.py#L1781) | 1781 | `"                        search_response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001782](../../agents/web_agent.py#L1782) | 1782 | `"                            f\"https://graph.facebook.com/{graph_version}/ig_hashtag_search\","` | — |
| [SRC-1AE03B9EC3-L001783](../../agents/web_agent.py#L1783) | 1783 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L001784](../../agents/web_agent.py#L1784) | 1784 | `"                                \"user_id\": ig_user_id,"` | — |
| [SRC-1AE03B9EC3-L001785](../../agents/web_agent.py#L1785) | 1785 | `"                                \"q\": hashtag,"` | — |
| [SRC-1AE03B9EC3-L001786](../../agents/web_agent.py#L1786) | 1786 | `"                                \"fields\": \"id,name\","` | — |
| [SRC-1AE03B9EC3-L001787](../../agents/web_agent.py#L1787) | 1787 | `"                                \"access_token\": ig_token,"` | — |
| [SRC-1AE03B9EC3-L001788](../../agents/web_agent.py#L1788) | 1788 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L001789](../../agents/web_agent.py#L1789) | 1789 | `"                            headers=headers,"` | — |
| [SRC-1AE03B9EC3-L001790](../../agents/web_agent.py#L1790) | 1790 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001791](../../agents/web_agent.py#L1791) | 1791 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001792](../../agents/web_agent.py#L1792) | 1792 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L001793](../../agents/web_agent.py#L1793) | 1793 | `"                        if search_response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001794](../../agents/web_agent.py#L1794) | 1794 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L001795](../../agents/web_agent.py#L1795) | 1795 | `"                                \"Instagram Graph API hashtag search unavailable \""` | — |
| [SRC-1AE03B9EC3-L001796](../../agents/web_agent.py#L1796) | 1796 | `"                                f\"(HTTP {search_response.status_code}); check permissions and access.\""` | — |
| [SRC-1AE03B9EC3-L001797](../../agents/web_agent.py#L1797) | 1797 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L001798](../../agents/web_agent.py#L1798) | 1798 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001799](../../agents/web_agent.py#L1799) | 1799 | `"                        tag_data = search_response.json().get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L001800](../../agents/web_agent.py#L1800) | 1800 | `"                        if not tag_data:"` | — |
| [SRC-1AE03B9EC3-L001801](../../agents/web_agent.py#L1801) | 1801 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001802](../../agents/web_agent.py#L1802) | 1802 | `"                        hashtag_id = tag_data[0].get(\"id\")"` | — |
| [SRC-1AE03B9EC3-L001803](../../agents/web_agent.py#L1803) | 1803 | `"                        if not hashtag_id:"` | — |
| [SRC-1AE03B9EC3-L001804](../../agents/web_agent.py#L1804) | 1804 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001805](../../agents/web_agent.py#L1805) | 1805 | `"                        self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001806](../../agents/web_agent.py#L1806) | 1806 | `"                        media_response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001807](../../agents/web_agent.py#L1807) | 1807 | `"                            f\"https://graph.facebook.com/{graph_version}/{hashtag_id}/recent_media\","` | — |
| [SRC-1AE03B9EC3-L001808](../../agents/web_agent.py#L1808) | 1808 | `"                            params={"` | — |
| [SRC-1AE03B9EC3-L001809](../../agents/web_agent.py#L1809) | 1809 | `"                                \"user_id\": ig_user_id,"` | — |
| [SRC-1AE03B9EC3-L001810](../../agents/web_agent.py#L1810) | 1810 | `"                                \"fields\": \"id,caption,media_type,permalink,timestamp,like_count,comments_count\","` | — |
| [SRC-1AE03B9EC3-L001811](../../agents/web_agent.py#L1811) | 1811 | `"                                \"limit\": 20,"` | — |
| [SRC-1AE03B9EC3-L001812](../../agents/web_agent.py#L1812) | 1812 | `"                                \"access_token\": ig_token,"` | — |
| [SRC-1AE03B9EC3-L001813](../../agents/web_agent.py#L1813) | 1813 | `"                            },"` | — |
| [SRC-1AE03B9EC3-L001814](../../agents/web_agent.py#L1814) | 1814 | `"                            headers=headers,"` | — |
| [SRC-1AE03B9EC3-L001815](../../agents/web_agent.py#L1815) | 1815 | `"                            timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001816](../../agents/web_agent.py#L1816) | 1816 | `"                            follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001817](../../agents/web_agent.py#L1817) | 1817 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L001818](../../agents/web_agent.py#L1818) | 1818 | `"                        if media_response.status_code != 200:"` | — |
| [SRC-1AE03B9EC3-L001819](../../agents/web_agent.py#L1819) | 1819 | `"                            warnings.append("` | — |
| [SRC-1AE03B9EC3-L001820](../../agents/web_agent.py#L1820) | 1820 | `"                                \"Instagram public hashtag media unavailable \""` | — |
| [SRC-1AE03B9EC3-L001821](../../agents/web_agent.py#L1821) | 1821 | `"                                f\"(HTTP {media_response.status_code}).\""` | — |
| [SRC-1AE03B9EC3-L001822](../../agents/web_agent.py#L1822) | 1822 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L001823](../../agents/web_agent.py#L1823) | 1823 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001824](../../agents/web_agent.py#L1824) | 1824 | `"                        items = media_response.json().get(\"data\", [])"` | — |
| [SRC-1AE03B9EC3-L001825](../../agents/web_agent.py#L1825) | 1825 | `"                        for item in items:"` | — |
| [SRC-1AE03B9EC3-L001826](../../agents/web_agent.py#L1826) | 1826 | `"                            url = _public_http_url(item.get(\"permalink\", \"\"))"` | — |
| [SRC-1AE03B9EC3-L001827](../../agents/web_agent.py#L1827) | 1827 | `"                            if not url:"` | — |
| [SRC-1AE03B9EC3-L001828](../../agents/web_agent.py#L1828) | 1828 | `"                                continue"` | — |
| [SRC-1AE03B9EC3-L001829](../../agents/web_agent.py#L1829) | 1829 | `"                            metrics = []"` | — |
| [SRC-1AE03B9EC3-L001830](../../agents/web_agent.py#L1830) | 1830 | `"                            if item.get(\"like_count\") is not None:"` | — |
| [SRC-1AE03B9EC3-L001831](../../agents/web_agent.py#L1831) | 1831 | `"                                metrics.append(\"likes=\" + str(item[\"like_count\"]))"` | — |
| [SRC-1AE03B9EC3-L001832](../../agents/web_agent.py#L1832) | 1832 | `"                            if item.get(\"comments_count\") is not None:"` | — |
| [SRC-1AE03B9EC3-L001833](../../agents/web_agent.py#L1833) | 1833 | `"                                metrics.append(\"comments=\" + str(item[\"comments_count\"]))"` | — |
| [SRC-1AE03B9EC3-L001834](../../agents/web_agent.py#L1834) | 1834 | `"                            caption = _clean_text(item.get(\"caption\") or \"\", 1200)"` | — |
| [SRC-1AE03B9EC3-L001835](../../agents/web_agent.py#L1835) | 1835 | `"                            if metrics:"` | — |
| [SRC-1AE03B9EC3-L001836](../../agents/web_agent.py#L1836) | 1836 | `"                                caption = (caption + \" \| \" if caption else \"\") + \", \".join(metrics)"` | — |
| [SRC-1AE03B9EC3-L001837](../../agents/web_agent.py#L1837) | 1837 | `"                            results.append({"` | — |
| [SRC-1AE03B9EC3-L001838](../../agents/web_agent.py#L1838) | 1838 | `"                                \"title\": \"Instagram public hashtag: #\" + hashtag,"` | — |
| [SRC-1AE03B9EC3-L001839](../../agents/web_agent.py#L1839) | 1839 | `"                                \"url\": url,"` | — |
| [SRC-1AE03B9EC3-L001840](../../agents/web_agent.py#L1840) | 1840 | `"                                \"snippet\": caption,"` | — |
| [SRC-1AE03B9EC3-L001841](../../agents/web_agent.py#L1841) | 1841 | `"                                \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001842](../../agents/web_agent.py#L1842) | 1842 | `"                                \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001843](../../agents/web_agent.py#L1843) | 1843 | `"                                \"provider\": \"instagram_graph_api\","` | — |
| [SRC-1AE03B9EC3-L001844](../../agents/web_agent.py#L1844) | 1844 | `"                                \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L001845](../../agents/web_agent.py#L1845) | 1845 | `"                                    row for row in results"` | — |
| [SRC-1AE03B9EC3-L001846](../../agents/web_agent.py#L1846) | 1846 | `"                                    if row.get(\"provider\") == \"instagram_graph_api\""` | — |
| [SRC-1AE03B9EC3-L001847](../../agents/web_agent.py#L1847) | 1847 | `"                                ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L001848](../../agents/web_agent.py#L1848) | 1848 | `"                                \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001849](../../agents/web_agent.py#L1849) | 1849 | `"                                \"published_at\": _clean_text(item.get(\"timestamp\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L001850](../../agents/web_agent.py#L1850) | 1850 | `"                            })"` | — |
| [SRC-1AE03B9EC3-L001851](../../agents/web_agent.py#L1851) | 1851 | `"                    except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L001852](../../agents/web_agent.py#L1852) | 1852 | `"                        warnings.append(\"Instagram Graph API search failed for a requested hashtag.\")"` | — |
| [SRC-1AE03B9EC3-L001853](../../agents/web_agent.py#L1853) | 1853 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L001854](../../agents/web_agent.py#L1854) | 1854 | `"                warnings.append("` | — |
| [SRC-1AE03B9EC3-L001855](../../agents/web_agent.py#L1855) | 1855 | `"                    \"Instagram direct API is not configured; indexed public Instagram pages are still searched.\""` | — |
| [SRC-1AE03B9EC3-L001856](../../agents/web_agent.py#L1856) | 1856 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001857](../../agents/web_agent.py#L1857) | 1857 | `""` | — |
| [SRC-1AE03B9EC3-L001858](../../agents/web_agent.py#L1858) | 1858 | `"        if \"x\" in platforms and os.getenv(\"X_BEARER_TOKEN\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001859](../../agents/web_agent.py#L1859) | 1859 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001860](../../agents/web_agent.py#L1860) | 1860 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001861](../../agents/web_agent.py#L1861) | 1861 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001862](../../agents/web_agent.py#L1862) | 1862 | `"                    \"https://api.x.com/2/tweets/search/recent\","` | — |
| [SRC-1AE03B9EC3-L001863](../../agents/web_agent.py#L1863) | 1863 | `"                    params={"` | — |
| [SRC-1AE03B9EC3-L001864](../../agents/web_agent.py#L1864) | 1864 | `"                        \"query\": query + \" -is:retweet\","` | — |
| [SRC-1AE03B9EC3-L001865](../../agents/web_agent.py#L1865) | 1865 | `"                        \"max_results\": 10,"` | — |
| [SRC-1AE03B9EC3-L001866](../../agents/web_agent.py#L1866) | 1866 | `"                        \"tweet.fields\": \"created_at,lang,public_metrics,author_id\","` | — |
| [SRC-1AE03B9EC3-L001867](../../agents/web_agent.py#L1867) | 1867 | `"                        \"expansions\": \"author_id\","` | — |
| [SRC-1AE03B9EC3-L001868](../../agents/web_agent.py#L1868) | 1868 | `"                        \"user.fields\": \"name,username\","` | — |
| [SRC-1AE03B9EC3-L001869](../../agents/web_agent.py#L1869) | 1869 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L001870](../../agents/web_agent.py#L1870) | 1870 | `"                    headers={"` | — |
| [SRC-1AE03B9EC3-L001871](../../agents/web_agent.py#L1871) | 1871 | `"                        **headers,"` | — |
| [SRC-1AE03B9EC3-L001872](../../agents/web_agent.py#L1872) | 1872 | `"                        \"Authorization\": \"Bearer \" + os.getenv(\"X_BEARER_TOKEN\", \"\").strip(),"` | — |
| [SRC-1AE03B9EC3-L001873](../../agents/web_agent.py#L1873) | 1873 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L001874](../../agents/web_agent.py#L1874) | 1874 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001875](../../agents/web_agent.py#L1875) | 1875 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001876](../../agents/web_agent.py#L1876) | 1876 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001877](../../agents/web_agent.py#L1877) | 1877 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001878](../../agents/web_agent.py#L1878) | 1878 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L001879](../../agents/web_agent.py#L1879) | 1879 | `"                    authors = {"` | — |
| [SRC-1AE03B9EC3-L001880](../../agents/web_agent.py#L1880) | 1880 | `"                        user.get(\"id\"): user"` | — |
| [SRC-1AE03B9EC3-L001881](../../agents/web_agent.py#L1881) | 1881 | `"                        for user in data.get(\"includes\", {}).get(\"users\", [])"` | — |
| [SRC-1AE03B9EC3-L001882](../../agents/web_agent.py#L1882) | 1882 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L001883](../../agents/web_agent.py#L1883) | 1883 | `"                    for item in data.get(\"data\", []):"` | — |
| [SRC-1AE03B9EC3-L001884](../../agents/web_agent.py#L1884) | 1884 | `"                        author = authors.get(item.get(\"author_id\"), {})"` | — |
| [SRC-1AE03B9EC3-L001885](../../agents/web_agent.py#L1885) | 1885 | `"                        username = author.get(\"username\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001886](../../agents/web_agent.py#L1886) | 1886 | `"                        post_id = item.get(\"id\", \"\")"` | — |
| [SRC-1AE03B9EC3-L001887](../../agents/web_agent.py#L1887) | 1887 | `"                        if not username or not post_id:"` | — |
| [SRC-1AE03B9EC3-L001888](../../agents/web_agent.py#L1888) | 1888 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001889](../../agents/web_agent.py#L1889) | 1889 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L001890](../../agents/web_agent.py#L1890) | 1890 | `"                            \"title\": _clean_text(author.get(\"name\") or username, 300),"` | — |
| [SRC-1AE03B9EC3-L001891](../../agents/web_agent.py#L1891) | 1891 | `"                            \"url\": f\"https://x.com/{username}/status/{post_id}\","` | — |
| [SRC-1AE03B9EC3-L001892](../../agents/web_agent.py#L1892) | 1892 | `"                            \"snippet\": _clean_text(item.get(\"text\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L001893](../../agents/web_agent.py#L1893) | 1893 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001894](../../agents/web_agent.py#L1894) | 1894 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001895](../../agents/web_agent.py#L1895) | 1895 | `"                            \"provider\": \"x_official_api\","` | — |
| [SRC-1AE03B9EC3-L001896](../../agents/web_agent.py#L1896) | 1896 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L001897](../../agents/web_agent.py#L1897) | 1897 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L001898](../../agents/web_agent.py#L1898) | 1898 | `"                                if row.get(\"provider\") == \"x_official_api\""` | — |
| [SRC-1AE03B9EC3-L001899](../../agents/web_agent.py#L1899) | 1899 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L001900](../../agents/web_agent.py#L1900) | 1900 | `"                            \"search_query\": query,"` | — |
| [SRC-1AE03B9EC3-L001901](../../agents/web_agent.py#L1901) | 1901 | `"                            \"published_at\": _clean_text(item.get(\"created_at\") or \"\", 100),"` | — |
| [SRC-1AE03B9EC3-L001902](../../agents/web_agent.py#L1902) | 1902 | `"                        })"` | — |
| [SRC-1AE03B9EC3-L001903](../../agents/web_agent.py#L1903) | 1903 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L001904](../../agents/web_agent.py#L1904) | 1904 | `"                    warnings.append(f\"X API unavailable (HTTP {response.status_code})\")"` | — |
| [SRC-1AE03B9EC3-L001905](../../agents/web_agent.py#L1905) | 1905 | `"            except (httpx.HTTPError, OSError, ValueError, KeyError, TypeError):"` | — |
| [SRC-1AE03B9EC3-L001906](../../agents/web_agent.py#L1906) | 1906 | `"                warnings.append(\"X API unavailable for this request\")"` | — |
| [SRC-1AE03B9EC3-L001907](../../agents/web_agent.py#L1907) | 1907 | `"        elif \"x\" in platforms:"` | — |
| [SRC-1AE03B9EC3-L001908](../../agents/web_agent.py#L1908) | 1908 | `"            warnings.append(\"X direct API is not configured; indexed public X pages are still searched.\")"` | — |
| [SRC-1AE03B9EC3-L001909](../../agents/web_agent.py#L1909) | 1909 | `""` | — |
| [SRC-1AE03B9EC3-L001910](../../agents/web_agent.py#L1910) | 1910 | `"        if \"youtube\" in platforms and os.getenv(\"YOUTUBE_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L001911](../../agents/web_agent.py#L1911) | 1911 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L001912](../../agents/web_agent.py#L1912) | 1912 | `"                self._reserve_search_call()"` | — |
| [SRC-1AE03B9EC3-L001913](../../agents/web_agent.py#L1913) | 1913 | `"                response = httpx.get("` | — |
| [SRC-1AE03B9EC3-L001914](../../agents/web_agent.py#L1914) | 1914 | `"                    \"https://www.googleapis.com/youtube/v3/search\","` | — |
| [SRC-1AE03B9EC3-L001915](../../agents/web_agent.py#L1915) | 1915 | `"                    params={"` | — |
| [SRC-1AE03B9EC3-L001916](../../agents/web_agent.py#L1916) | 1916 | `"                        \"part\": \"snippet\","` | — |
| [SRC-1AE03B9EC3-L001917](../../agents/web_agent.py#L1917) | 1917 | `"                        \"q\": query,"` | — |
| [SRC-1AE03B9EC3-L001918](../../agents/web_agent.py#L1918) | 1918 | `"                        \"type\": \"video\","` | — |
| [SRC-1AE03B9EC3-L001919](../../agents/web_agent.py#L1919) | 1919 | `"                        \"maxResults\": 8,"` | — |
| [SRC-1AE03B9EC3-L001920](../../agents/web_agent.py#L1920) | 1920 | `"                        \"key\": os.getenv(\"YOUTUBE_API_KEY\", \"\").strip(),"` | — |
| [SRC-1AE03B9EC3-L001921](../../agents/web_agent.py#L1921) | 1921 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L001922](../../agents/web_agent.py#L1922) | 1922 | `"                    headers=headers,"` | — |
| [SRC-1AE03B9EC3-L001923](../../agents/web_agent.py#L1923) | 1923 | `"                    timeout=self._effective_timeout(9.0),"` | — |
| [SRC-1AE03B9EC3-L001924](../../agents/web_agent.py#L1924) | 1924 | `"                    follow_redirects=False,"` | — |
| [SRC-1AE03B9EC3-L001925](../../agents/web_agent.py#L1925) | 1925 | `"                )"` | — |
| [SRC-1AE03B9EC3-L001926](../../agents/web_agent.py#L1926) | 1926 | `"                if response.status_code == 200:"` | — |
| [SRC-1AE03B9EC3-L001927](../../agents/web_agent.py#L1927) | 1927 | `"                    data = response.json()"` | — |
| [SRC-1AE03B9EC3-L001928](../../agents/web_agent.py#L1928) | 1928 | `"                    for item in data.get(\"items\", []):"` | — |
| [SRC-1AE03B9EC3-L001929](../../agents/web_agent.py#L1929) | 1929 | `"                        video_id = item.get(\"id\", {}).get(\"videoId\")"` | — |
| [SRC-1AE03B9EC3-L001930](../../agents/web_agent.py#L1930) | 1930 | `"                        snippet = item.get(\"snippet\", {})"` | — |
| [SRC-1AE03B9EC3-L001931](../../agents/web_agent.py#L1931) | 1931 | `"                        if not video_id:"` | — |
| [SRC-1AE03B9EC3-L001932](../../agents/web_agent.py#L1932) | 1932 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L001933](../../agents/web_agent.py#L1933) | 1933 | `"                        results.append({"` | — |
| [SRC-1AE03B9EC3-L001934](../../agents/web_agent.py#L1934) | 1934 | `"                            \"title\": _clean_text(snippet.get(\"title\") or \"\", 300),"` | — |
| [SRC-1AE03B9EC3-L001935](../../agents/web_agent.py#L1935) | 1935 | `"                            \"url\": f\"https://www.youtube.com/watch?v={video_id}\","` | — |
| [SRC-1AE03B9EC3-L001936](../../agents/web_agent.py#L1936) | 1936 | `"                            \"snippet\": _clean_text(snippet.get(\"description\") or \"\", 1200),"` | — |
| [SRC-1AE03B9EC3-L001937](../../agents/web_agent.py#L1937) | 1937 | `"                            \"page_text\": \"\","` | — |
| [SRC-1AE03B9EC3-L001938](../../agents/web_agent.py#L1938) | 1938 | `"                            \"page_fetched\": False,"` | — |
| [SRC-1AE03B9EC3-L001939](../../agents/web_agent.py#L1939) | 1939 | `"                            \"provider\": \"youtube_data_api\","` | — |
| [SRC-1AE03B9EC3-L001940](../../agents/web_agent.py#L1940) | 1940 | `"                            \"provider_rank\": len(["` | — |
| [SRC-1AE03B9EC3-L001941](../../agents/web_agent.py#L1941) | 1941 | `"                                row for row in results"` | — |
| [SRC-1AE03B9EC3-L001942](../../agents/web_agent.py#L1942) | 1942 | `"                                if row.get(\"provider\") == \"youtube_data_api\""` | — |
| [SRC-1AE03B9EC3-L001943](../../agents/web_agent.py#L1943) | 1943 | `"                            ]) + 1,"` | — |
| [SRC-1AE03B9EC3-L001944](../../agents/web_agent.py#L1944) | 1944 | `"                            \"search_query\": query,"` | — |
