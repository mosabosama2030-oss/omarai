# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **009**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L004101 إلى SRC-1AE03B9EC3-L004900
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L004101](../../agents/web_agent.py#L4101) | 4101 | `"            search_warnings.append(str(exc))"` | — |
| [SRC-1AE03B9EC3-L004102](../../agents/web_agent.py#L4102) | 4102 | `"            baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L004103](../../agents/web_agent.py#L4103) | 4103 | `"            with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L004104](../../agents/web_agent.py#L4104) | 4104 | `"                failure_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L004105](../../agents/web_agent.py#L4105) | 4105 | `"                    item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004106](../../agents/web_agent.py#L4106) | 4106 | `"                    if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L004107](../../agents/web_agent.py#L4107) | 4107 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004108](../../agents/web_agent.py#L4108) | 4108 | `"            provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L004109](../../agents/web_agent.py#L4109) | 4109 | `"                item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L004110](../../agents/web_agent.py#L4110) | 4110 | `"                for item in failure_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004111](../../agents/web_agent.py#L4111) | 4111 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004112](../../agents/web_agent.py#L4112) | 4112 | `"            report = {"` | — |
| [SRC-1AE03B9EC3-L004113](../../agents/web_agent.py#L4113) | 4113 | `"                \"queries_planned\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-1AE03B9EC3-L004114](../../agents/web_agent.py#L4114) | 4114 | `"                # The exact query count is unknowable when the pipeline fails before it"` | — |
| [SRC-1AE03B9EC3-L004115](../../agents/web_agent.py#L4115) | 4115 | `"                # returns its report. A provider diagnostic may still prove an attempt."` | — |
| [SRC-1AE03B9EC3-L004116](../../agents/web_agent.py#L4116) | 4116 | `"                \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L004117](../../agents/web_agent.py#L4117) | 4117 | `"                \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L004118](../../agents/web_agent.py#L4118) | 4118 | `"                \"search_attempted\": True if provider_attempt_observed else None,"` | — |
| [SRC-1AE03B9EC3-L004119](../../agents/web_agent.py#L4119) | 4119 | `"                \"search_outcome\": ("` | — |
| [SRC-1AE03B9EC3-L004120](../../agents/web_agent.py#L4120) | 4120 | `"                    \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L004121](../../agents/web_agent.py#L4121) | 4121 | `"                    if provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L004122](../../agents/web_agent.py#L4122) | 4122 | `"                    else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L004123](../../agents/web_agent.py#L4123) | 4123 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004124](../../agents/web_agent.py#L4124) | 4124 | `"                \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L004125](../../agents/web_agent.py#L4125) | 4125 | `"                \"unique_sources\": None,"` | — |
| [SRC-1AE03B9EC3-L004126](../../agents/web_agent.py#L4126) | 4126 | `"                \"pages_fetched\": None,"` | — |
| [SRC-1AE03B9EC3-L004127](../../agents/web_agent.py#L4127) | 4127 | `"                \"providers_used\": [],"` | — |
| [SRC-1AE03B9EC3-L004128](../../agents/web_agent.py#L4128) | 4128 | `"                \"provider_counts\": None,"` | — |
| [SRC-1AE03B9EC3-L004129](../../agents/web_agent.py#L4129) | 4129 | `"                \"platform_counts\": {},"` | — |
| [SRC-1AE03B9EC3-L004130](../../agents/web_agent.py#L4130) | 4130 | `"                \"social_direct_results\": None,"` | — |
| [SRC-1AE03B9EC3-L004131](../../agents/web_agent.py#L4131) | 4131 | `"                \"provider_diagnostics\": failure_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L004132](../../agents/web_agent.py#L4132) | 4132 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L004133](../../agents/web_agent.py#L4133) | 4133 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L004134](../../agents/web_agent.py#L4134) | 4134 | `"                \"evidence_signals\": evidence_signal_report([], plan.get(\"freshness\", \"any\")),"` | — |
| [SRC-1AE03B9EC3-L004135](../../agents/web_agent.py#L4135) | 4135 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004136](../../agents/web_agent.py#L4136) | 4136 | `"        # Final relevance check is intentionally repeated after fusion, before any answer LLM call."` | — |
| [SRC-1AE03B9EC3-L004137](../../agents/web_agent.py#L4137) | 4137 | `"        filtered_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L004138](../../agents/web_agent.py#L4138) | 4138 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L004139](../../agents/web_agent.py#L4139) | 4139 | `"            if \"user_supplied_url\" in source.get(\"providers\", []):"` | — |
| [SRC-1AE03B9EC3-L004140](../../agents/web_agent.py#L4140) | 4140 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004141](../../agents/web_agent.py#L4141) | 4141 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L004142](../../agents/web_agent.py#L4142) | 4142 | `"            candidate_queries = ("` | — |
| [SRC-1AE03B9EC3-L004143](../../agents/web_agent.py#L4143) | 4143 | `"                source.get(\"queries\")"` | — |
| [SRC-1AE03B9EC3-L004144](../../agents/web_agent.py#L4144) | 4144 | `"                or plan.get(\"queries\")"` | — |
| [SRC-1AE03B9EC3-L004145](../../agents/web_agent.py#L4145) | 4145 | `"                or [compact_search_query(question)]"` | — |
| [SRC-1AE03B9EC3-L004146](../../agents/web_agent.py#L4146) | 4146 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004147](../../agents/web_agent.py#L4147) | 4147 | `"            if any(self._source_matches_query(str(q), source) for q in candidate_queries):"` | — |
| [SRC-1AE03B9EC3-L004148](../../agents/web_agent.py#L4148) | 4148 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004149](../../agents/web_agent.py#L4149) | 4149 | `"        sources = filtered_sources"` | — |
| [SRC-1AE03B9EC3-L004150](../../agents/web_agent.py#L4150) | 4150 | `"        search_warning = \"؛ \".join(search_warnings) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L004151](../../agents/web_agent.py#L4151) | 4151 | `"        independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L004152](../../agents/web_agent.py#L4152) | 4152 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L004153](../../agents/web_agent.py#L4153) | 4153 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L004154](../../agents/web_agent.py#L4154) | 4154 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L004155](../../agents/web_agent.py#L4155) | 4155 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L004156](../../agents/web_agent.py#L4156) | 4156 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004157](../../agents/web_agent.py#L4157) | 4157 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L004158](../../agents/web_agent.py#L4158) | 4158 | `"        }"` | — |
| [SRC-1AE03B9EC3-L004159](../../agents/web_agent.py#L4159) | 4159 | `"        independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L004160](../../agents/web_agent.py#L4160) | 4160 | `"        # A user-requested page summary is a different task from open-ended research:"` | — |
| [SRC-1AE03B9EC3-L004161](../../agents/web_agent.py#L4161) | 4161 | `"        # one successfully extracted, explicitly supplied page can support a summary,"` | — |
| [SRC-1AE03B9EC3-L004162](../../agents/web_agent.py#L4162) | 4162 | `"        # but must never be presented as independently corroborated research."` | — |
| [SRC-1AE03B9EC3-L004163](../../agents/web_agent.py#L4163) | 4163 | `"        has_read_user_supplied_page = any("` | — |
| [SRC-1AE03B9EC3-L004164](../../agents/web_agent.py#L4164) | 4164 | `"            \"user_supplied_url\" in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L004165](../../agents/web_agent.py#L4165) | 4165 | `"            and bool(source.get(\"page_fetched\"))"` | — |
| [SRC-1AE03B9EC3-L004166](../../agents/web_agent.py#L4166) | 4166 | `"            and bool(str(source.get(\"page_text\") or \"\").strip())"` | — |
| [SRC-1AE03B9EC3-L004167](../../agents/web_agent.py#L4167) | 4167 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L004168](../../agents/web_agent.py#L4168) | 4168 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004169](../../agents/web_agent.py#L4169) | 4169 | `"        single_source_page_summary = ("` | — |
| [SRC-1AE03B9EC3-L004170](../../agents/web_agent.py#L4170) | 4170 | `"            has_read_user_supplied_page"` | — |
| [SRC-1AE03B9EC3-L004171](../../agents/web_agent.py#L4171) | 4171 | `"            and len(sources) == 1"` | — |
| [SRC-1AE03B9EC3-L004172](../../agents/web_agent.py#L4172) | 4172 | `"            and len(independent_domains) == 1"` | — |
| [SRC-1AE03B9EC3-L004173](../../agents/web_agent.py#L4173) | 4173 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004174](../../agents/web_agent.py#L4174) | 4174 | `"        if single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L004175](../../agents/web_agent.py#L4175) | 4175 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004176](../../agents/web_agent.py#L4176) | 4176 | `"                \"هذا ملخص للرابط الذي قدمته فقط؛ لم يتم تأكيد محتواه من مصدر مستقل آخر.\""` | — |
| [SRC-1AE03B9EC3-L004177](../../agents/web_agent.py#L4177) | 4177 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004178](../../agents/web_agent.py#L4178) | 4178 | `"            search_warning = \"؛ \".join(search_warnings)"` | — |
| [SRC-1AE03B9EC3-L004179](../../agents/web_agent.py#L4179) | 4179 | `"        # Link-finding and lead-discovery are actionable discovery tasks, not broad"` | — |
| [SRC-1AE03B9EC3-L004180](../../agents/web_agent.py#L4180) | 4180 | `"        # fact-checking. Keep useful candidates visible while explicitly labelling them"` | — |
| [SRC-1AE03B9EC3-L004181](../../agents/web_agent.py#L4181) | 4181 | `"        # as uncorroborated instead of refusing a lone result as if it were no result."` | — |
| [SRC-1AE03B9EC3-L004182](../../agents/web_agent.py#L4182) | 4182 | `"        navigation_request = self._is_navigation_request(question)"` | — |
| [SRC-1AE03B9EC3-L004183](../../agents/web_agent.py#L4183) | 4183 | `"        lead_request = intent_route == \"LEAD_GENERATION\" or self._is_lead_search(question)"` | — |
| [SRC-1AE03B9EC3-L004184](../../agents/web_agent.py#L4184) | 4184 | `"        listing_request = self._is_listing_discovery(question)"` | — |
| [SRC-1AE03B9EC3-L004185](../../agents/web_agent.py#L4185) | 4185 | `"        lead_evidence_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L004186](../../agents/web_agent.py#L4186) | 4186 | `"        related_lead_results_count = 0"` | — |
| [SRC-1AE03B9EC3-L004187](../../agents/web_agent.py#L4187) | 4187 | `"        if lead_request:"` | — |
| [SRC-1AE03B9EC3-L004188](../../agents/web_agent.py#L4188) | 4188 | `"            related_lead_results_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004189](../../agents/web_agent.py#L4189) | 4189 | `"            for source in sources:"` | — |
| [SRC-1AE03B9EC3-L004190](../../agents/web_agent.py#L4190) | 4190 | `"                signal = self._lead_intent_evidence(source)"` | — |
| [SRC-1AE03B9EC3-L004191](../../agents/web_agent.py#L4191) | 4191 | `"                if signal:"` | — |
| [SRC-1AE03B9EC3-L004192](../../agents/web_agent.py#L4192) | 4192 | `"                    source[\"lead_qualification\"] = \"public_buyer_intent_signal\""` | — |
| [SRC-1AE03B9EC3-L004193](../../agents/web_agent.py#L4193) | 4193 | `"                    source[\"lead_intent_evidence\"] = signal"` | — |
| [SRC-1AE03B9EC3-L004194](../../agents/web_agent.py#L4194) | 4194 | `"                    lead_evidence_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004195](../../agents/web_agent.py#L4195) | 4195 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L004196](../../agents/web_agent.py#L4196) | 4196 | `"                    source[\"lead_qualification\"] = \"related_result_not_lead\""` | — |
| [SRC-1AE03B9EC3-L004197](../../agents/web_agent.py#L4197) | 4197 | `"            lead_research_incomplete = ("` | — |
| [SRC-1AE03B9EC3-L004198](../../agents/web_agent.py#L4198) | 4198 | `"                not sources"` | — |
| [SRC-1AE03B9EC3-L004199](../../agents/web_agent.py#L4199) | 4199 | `"                and report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L004200](../../agents/web_agent.py#L4200) | 4200 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004201](../../agents/web_agent.py#L4201) | 4201 | `"            report[\"lead_generation\"] = {"` | — |
| [SRC-1AE03B9EC3-L004202](../../agents/web_agent.py#L4202) | 4202 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L004203](../../agents/web_agent.py#L4203) | 4203 | `"                    \"research_incomplete\" if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L004204](../../agents/web_agent.py#L4204) | 4204 | `"                    else \"candidate_signals_found\" if lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L004205](../../agents/web_agent.py#L4205) | 4205 | `"                    else \"no_qualified_candidates_found\""` | — |
| [SRC-1AE03B9EC3-L004206](../../agents/web_agent.py#L4206) | 4206 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004207](../../agents/web_agent.py#L4207) | 4207 | `"                \"candidate_signal_count\": ("` | — |
| [SRC-1AE03B9EC3-L004208](../../agents/web_agent.py#L4208) | 4208 | `"                    None if lead_research_incomplete else len(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L004209](../../agents/web_agent.py#L4209) | 4209 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004210](../../agents/web_agent.py#L4210) | 4210 | `"                \"related_results_reviewed\": ("` | — |
| [SRC-1AE03B9EC3-L004211](../../agents/web_agent.py#L4211) | 4211 | `"                    None if lead_research_incomplete else related_lead_results_count"` | — |
| [SRC-1AE03B9EC3-L004212](../../agents/web_agent.py#L4212) | 4212 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004213](../../agents/web_agent.py#L4213) | 4213 | `"                \"qualification_rule\": \"explicit_public_buyer_intent_phrase\","` | — |
| [SRC-1AE03B9EC3-L004214](../../agents/web_agent.py#L4214) | 4214 | `"                \"identity_verified\": False,"` | — |
| [SRC-1AE03B9EC3-L004215](../../agents/web_agent.py#L4215) | 4215 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004216](../../agents/web_agent.py#L4216) | 4216 | `"            if not lead_evidence_sources:"` | — |
| [SRC-1AE03B9EC3-L004217](../../agents/web_agent.py#L4217) | 4217 | `"                if sources:"` | — |
| [SRC-1AE03B9EC3-L004218](../../agents/web_agent.py#L4218) | 4218 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L004219](../../agents/web_agent.py#L4219) | 4219 | `"                        \"لم أعثر على إشارة نصية واضحة تثبت أن أي نتيجة في هذه الجولة تتعلق بشخص \""` | — |
| [SRC-1AE03B9EC3-L004220](../../agents/web_agent.py#L4220) | 4220 | `"                        \"يريد الشراء. راجعت \""` | — |
| [SRC-1AE03B9EC3-L004221](../../agents/web_agent.py#L4221) | 4221 | `"                        + str(len(sources))"` | — |
| [SRC-1AE03B9EC3-L004222](../../agents/web_agent.py#L4222) | 4222 | `"                        + \" نتيجة مرتبطة بالموضوع، لكنني لم أعتبر إعلانات البيع أو صفحات السوق \""` | — |
| [SRC-1AE03B9EC3-L004223](../../agents/web_agent.py#L4223) | 4223 | `"                        \"عملاء محتملين. الروابط أدناه نتائج مرتبطة بالموضوع فقط وليست عملاء.\""` | — |
| [SRC-1AE03B9EC3-L004224](../../agents/web_agent.py#L4224) | 4224 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004225](../../agents/web_agent.py#L4225) | 4225 | `"                elif report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L004226](../../agents/web_agent.py#L4226) | 4226 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L004227](../../agents/web_agent.py#L4227) | 4227 | `"                        \"تعطل مسار البحث أو لم يمكن تأكيد اكتماله؛ لذلك لا أستطيع تحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L004228](../../agents/web_agent.py#L4228) | 4228 | `"                        \"كانت هناك نتائج تصلح كعملاء محتملين في هذه الجولة.\""` | — |
| [SRC-1AE03B9EC3-L004229](../../agents/web_agent.py#L4229) | 4229 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004230](../../agents/web_agent.py#L4230) | 4230 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L004231](../../agents/web_agent.py#L4231) | 4231 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L004232](../../agents/web_agent.py#L4232) | 4232 | `"                        \"لم تظهر نتائج قابلة للاستخدام تثبت نية شراء في هذه الجولة. هذا لا يثبت \""` | — |
| [SRC-1AE03B9EC3-L004233](../../agents/web_agent.py#L4233) | 4233 | `"                        \"عدم وجود عملاء؛ بل يعني أن البحث الحالي لم يعثر على دليل كافٍ.\""` | — |
| [SRC-1AE03B9EC3-L004234](../../agents/web_agent.py#L4234) | 4234 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004235](../../agents/web_agent.py#L4235) | 4235 | `"                report[\"research_quality\"] = \"failed\""` | — |
| [SRC-1AE03B9EC3-L004236](../../agents/web_agent.py#L4236) | 4236 | `"                # Distinguish zero qualified signals from unknown counts after an exception."` | — |
| [SRC-1AE03B9EC3-L004237](../../agents/web_agent.py#L4237) | 4237 | `"                report[\"usable_sources_after_filtering\"] = ("` | — |
| [SRC-1AE03B9EC3-L004238](../../agents/web_agent.py#L4238) | 4238 | `"                    None if lead_research_incomplete else len(sources)"` | — |
| [SRC-1AE03B9EC3-L004239](../../agents/web_agent.py#L4239) | 4239 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004240](../../agents/web_agent.py#L4240) | 4240 | `"                report[\"evidence_signals\"] = ("` | — |
| [SRC-1AE03B9EC3-L004241](../../agents/web_agent.py#L4241) | 4241 | `"                    None if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L004242](../../agents/web_agent.py#L4242) | 4242 | `"                    else evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L004243](../../agents/web_agent.py#L4243) | 4243 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004244](../../agents/web_agent.py#L4244) | 4244 | `"                public_related_sources = [{"` | — |
| [SRC-1AE03B9EC3-L004245](../../agents/web_agent.py#L4245) | 4245 | `"                    \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L004246](../../agents/web_agent.py#L4246) | 4246 | `"                    \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L004247](../../agents/web_agent.py#L4247) | 4247 | `"                    \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004248](../../agents/web_agent.py#L4248) | 4248 | `"                    \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L004249](../../agents/web_agent.py#L4249) | 4249 | `"                    \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L004250](../../agents/web_agent.py#L4250) | 4250 | `"                    \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L004251](../../agents/web_agent.py#L4251) | 4251 | `"                    \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L004252](../../agents/web_agent.py#L4252) | 4252 | `"                    \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004253](../../agents/web_agent.py#L4253) | 4253 | `"                    \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L004254](../../agents/web_agent.py#L4254) | 4254 | `"                    \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004255](../../agents/web_agent.py#L4255) | 4255 | `"                    \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004256](../../agents/web_agent.py#L4256) | 4256 | `"                    \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004257](../../agents/web_agent.py#L4257) | 4257 | `"                    \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L004258](../../agents/web_agent.py#L4258) | 4258 | `"                    \"lead_qualification\": \"related_result_not_lead\","` | — |
| [SRC-1AE03B9EC3-L004259](../../agents/web_agent.py#L4259) | 4259 | `"                } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L004260](../../agents/web_agent.py#L4260) | 4260 | `"                return {"` | — |
| [SRC-1AE03B9EC3-L004261](../../agents/web_agent.py#L4261) | 4261 | `"                    \"answer\": lead_answer,"` | — |
| [SRC-1AE03B9EC3-L004262](../../agents/web_agent.py#L4262) | 4262 | `"                    \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L004263](../../agents/web_agent.py#L4263) | 4263 | `"                    \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L004264](../../agents/web_agent.py#L4264) | 4264 | `"                    \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L004265](../../agents/web_agent.py#L4265) | 4265 | `"                    \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L004266](../../agents/web_agent.py#L4266) | 4266 | `"                        \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L004267](../../agents/web_agent.py#L4267) | 4267 | `"                        \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L004268](../../agents/web_agent.py#L4268) | 4268 | `"                        \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L004269](../../agents/web_agent.py#L4269) | 4269 | `"                        \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L004270](../../agents/web_agent.py#L4270) | 4270 | `"                        \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L004271](../../agents/web_agent.py#L4271) | 4271 | `"                        \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L004272](../../agents/web_agent.py#L4272) | 4272 | `"                        \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L004273](../../agents/web_agent.py#L4273) | 4273 | `"                        \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L004274](../../agents/web_agent.py#L4274) | 4274 | `"                        \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L004275](../../agents/web_agent.py#L4275) | 4275 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L004276](../../agents/web_agent.py#L4276) | 4276 | `"                    \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L004277](../../agents/web_agent.py#L4277) | 4277 | `"                    \"sources\": public_related_sources,"` | — |
| [SRC-1AE03B9EC3-L004278](../../agents/web_agent.py#L4278) | 4278 | `"                    \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L004279](../../agents/web_agent.py#L4279) | 4279 | `"                    \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L004280](../../agents/web_agent.py#L4280) | 4280 | `"                    \"search_attempted\": report.get("` | — |
| [SRC-1AE03B9EC3-L004281](../../agents/web_agent.py#L4281) | 4281 | `"                        \"search_attempted\","` | — |
| [SRC-1AE03B9EC3-L004282](../../agents/web_agent.py#L4282) | 4282 | `"                        bool(report.get(\"queries_attempted\", 0)),"` | — |
| [SRC-1AE03B9EC3-L004283](../../agents/web_agent.py#L4283) | 4283 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L004284](../../agents/web_agent.py#L4284) | 4284 | `"                    \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L004285](../../agents/web_agent.py#L4285) | 4285 | `"                    \"warnings\": [lead_answer],"` | — |
| [SRC-1AE03B9EC3-L004286](../../agents/web_agent.py#L4286) | 4286 | `"                    \"kind\": \"lead_discovery_no_qualified_candidates\","` | — |
| [SRC-1AE03B9EC3-L004287](../../agents/web_agent.py#L4287) | 4287 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L004288](../../agents/web_agent.py#L4288) | 4288 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L004289](../../agents/web_agent.py#L4289) | 4289 | `"                    \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L004290](../../agents/web_agent.py#L4290) | 4290 | `"                }"` | — |
| [SRC-1AE03B9EC3-L004291](../../agents/web_agent.py#L4291) | 4291 | `"            # Only explicit public buyer-intent signals may be synthesized as lead candidates."` | — |
| [SRC-1AE03B9EC3-L004292](../../agents/web_agent.py#L4292) | 4292 | `"            sources = lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L004293](../../agents/web_agent.py#L4293) | 4293 | `"            report[\"evidence_signals\"] = evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L004294](../../agents/web_agent.py#L4294) | 4294 | `"            report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004295](../../agents/web_agent.py#L4295) | 4295 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004296](../../agents/web_agent.py#L4296) | 4296 | `"            report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L004297](../../agents/web_agent.py#L4297) | 4297 | `"            independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L004298](../../agents/web_agent.py#L4298) | 4298 | `"                registrable_domain("` | — |
| [SRC-1AE03B9EC3-L004299](../../agents/web_agent.py#L4299) | 4299 | `"                    source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L004300](../../agents/web_agent.py#L4300) | 4300 | `"                    or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L004301](../../agents/web_agent.py#L4301) | 4301 | `"                    or \"\""` | — |
| [SRC-1AE03B9EC3-L004302](../../agents/web_agent.py#L4302) | 4302 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004303](../../agents/web_agent.py#L4303) | 4303 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L004304](../../agents/web_agent.py#L4304) | 4304 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004305](../../agents/web_agent.py#L4305) | 4305 | `"            independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L004306](../../agents/web_agent.py#L4306) | 4306 | `"        single_source_navigation = navigation_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L004307](../../agents/web_agent.py#L4307) | 4307 | `"        single_source_social = bool(plan.get(\"social_focus\")) and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L004308](../../agents/web_agent.py#L4308) | 4308 | `"        single_source_lead = lead_request and bool(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L004309](../../agents/web_agent.py#L4309) | 4309 | `"        single_source_listing = listing_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L004310](../../agents/web_agent.py#L4310) | 4310 | `"        task_specific_partial_evidence = ("` | — |
| [SRC-1AE03B9EC3-L004311](../../agents/web_agent.py#L4311) | 4311 | `"            single_source_page_summary"` | — |
| [SRC-1AE03B9EC3-L004312](../../agents/web_agent.py#L4312) | 4312 | `"            or single_source_navigation"` | — |
| [SRC-1AE03B9EC3-L004313](../../agents/web_agent.py#L4313) | 4313 | `"            or single_source_social"` | — |
| [SRC-1AE03B9EC3-L004314](../../agents/web_agent.py#L4314) | 4314 | `"            or single_source_lead"` | — |
| [SRC-1AE03B9EC3-L004315](../../agents/web_agent.py#L4315) | 4315 | `"            or single_source_listing"` | — |
| [SRC-1AE03B9EC3-L004316](../../agents/web_agent.py#L4316) | 4316 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004317](../../agents/web_agent.py#L4317) | 4317 | `"        needs_corroboration = len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L004318](../../agents/web_agent.py#L4318) | 4318 | `"        evidence_repair: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L004319](../../agents/web_agent.py#L4319) | 4319 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L004320](../../agents/web_agent.py#L4320) | 4320 | `"            \"max_extra_queries\": 1,"` | — |
| [SRC-1AE03B9EC3-L004321](../../agents/web_agent.py#L4321) | 4321 | `"            \"reason\": \"initial_evidence_gate_satisfied\" if not needs_corroboration else \"not_attempted\","` | — |
| [SRC-1AE03B9EC3-L004322](../../agents/web_agent.py#L4322) | 4322 | `"        }"` | — |
| [SRC-1AE03B9EC3-L004323](../../agents/web_agent.py#L4323) | 4323 | `"        if needs_corroboration and not plan.get(\"queries\"):"` | — |
| [SRC-1AE03B9EC3-L004324](../../agents/web_agent.py#L4324) | 4324 | `"            evidence_repair[\"reason\"] = \"no_topic_query_available\""` | — |
| [SRC-1AE03B9EC3-L004325](../../agents/web_agent.py#L4325) | 4325 | `"        elif needs_corroboration:"` | — |
| [SRC-1AE03B9EC3-L004326](../../agents/web_agent.py#L4326) | 4326 | `"            if task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L004327](../../agents/web_agent.py#L4327) | 4327 | `"                evidence_repair[\"reason\"] = \"task_specific_partial_evidence\""` | — |
| [SRC-1AE03B9EC3-L004328](../../agents/web_agent.py#L4328) | 4328 | `"            elif plan.get(\"social_focus\"):"` | — |
| [SRC-1AE03B9EC3-L004329](../../agents/web_agent.py#L4329) | 4329 | `"                evidence_repair[\"reason\"] = \"social_search_not_retried\""` | — |
| [SRC-1AE03B9EC3-L004330](../../agents/web_agent.py#L4330) | 4330 | `"            elif plan.get(\"depth\") == \"deep\" or report.get(\"expansion_queries\"):"` | — |
| [SRC-1AE03B9EC3-L004331](../../agents/web_agent.py#L4331) | 4331 | `"                evidence_repair[\"reason\"] = \"deep_research_already_expanded\""` | — |
| [SRC-1AE03B9EC3-L004332](../../agents/web_agent.py#L4332) | 4332 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004333](../../agents/web_agent.py#L4333) | 4333 | `"                original_queries = ["` | — |
| [SRC-1AE03B9EC3-L004334](../../agents/web_agent.py#L4334) | 4334 | `"                    str(item).strip()"` | — |
| [SRC-1AE03B9EC3-L004335](../../agents/web_agent.py#L4335) | 4335 | `"                    for item in plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L004336](../../agents/web_agent.py#L4336) | 4336 | `"                    if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L004337](../../agents/web_agent.py#L4337) | 4337 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004338](../../agents/web_agent.py#L4338) | 4338 | `"                base_query = ("` | — |
| [SRC-1AE03B9EC3-L004339](../../agents/web_agent.py#L4339) | 4339 | `"                    original_queries[0]"` | — |
| [SRC-1AE03B9EC3-L004340](../../agents/web_agent.py#L4340) | 4340 | `"                    if original_queries"` | — |
| [SRC-1AE03B9EC3-L004341](../../agents/web_agent.py#L4341) | 4341 | `"                    else compact_search_query(question)"` | — |
| [SRC-1AE03B9EC3-L004342](../../agents/web_agent.py#L4342) | 4342 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004343](../../agents/web_agent.py#L4343) | 4343 | `"                suffix = ("` | — |
| [SRC-1AE03B9EC3-L004344](../../agents/web_agent.py#L4344) | 4344 | `"                    \"latest official primary source\""` | — |
| [SRC-1AE03B9EC3-L004345](../../agents/web_agent.py#L4345) | 4345 | `"                    if plan.get(\"freshness\") == \"current\""` | — |
| [SRC-1AE03B9EC3-L004346](../../agents/web_agent.py#L4346) | 4346 | `"                    else \"official primary source data\""` | — |
| [SRC-1AE03B9EC3-L004347](../../agents/web_agent.py#L4347) | 4347 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004348](../../agents/web_agent.py#L4348) | 4348 | `"                repair_query = compact_search_query(f\"{base_query} {suffix}\")"` | — |
| [SRC-1AE03B9EC3-L004349](../../agents/web_agent.py#L4349) | 4349 | `"                known_queries = {"` | — |
| [SRC-1AE03B9EC3-L004350](../../agents/web_agent.py#L4350) | 4350 | `"                    _normalize_search_query(item).casefold()"` | — |
| [SRC-1AE03B9EC3-L004351](../../agents/web_agent.py#L4351) | 4351 | `"                    for item in original_queries"` | — |
| [SRC-1AE03B9EC3-L004352](../../agents/web_agent.py#L4352) | 4352 | `"                }"` | — |
| [SRC-1AE03B9EC3-L004353](../../agents/web_agent.py#L4353) | 4353 | `"                if _normalize_search_query(repair_query).casefold() in known_queries:"` | — |
| [SRC-1AE03B9EC3-L004354](../../agents/web_agent.py#L4354) | 4354 | `"                    repair_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L004355](../../agents/web_agent.py#L4355) | 4355 | `"                        f\"{base_query} independent corroborating evidence\""` | — |
| [SRC-1AE03B9EC3-L004356](../../agents/web_agent.py#L4356) | 4356 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004357](../../agents/web_agent.py#L4357) | 4357 | `"                if _normalize_search_query(repair_query).casefold() not in known_queries:"` | — |
| [SRC-1AE03B9EC3-L004358](../../agents/web_agent.py#L4358) | 4358 | `"                    initial_source_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004359](../../agents/web_agent.py#L4359) | 4359 | `"                    initial_domain_count = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L004360](../../agents/web_agent.py#L4360) | 4360 | `"                    evidence_repair[\"attempted\"] = True"` | — |
| [SRC-1AE03B9EC3-L004361](../../agents/web_agent.py#L4361) | 4361 | `"                    evidence_repair[\"reason\"] = \"thin_or_unrelated_initial_evidence\""` | — |
| [SRC-1AE03B9EC3-L004362](../../agents/web_agent.py#L4362) | 4362 | `"                    evidence_repair[\"query\"] = repair_query"` | — |
| [SRC-1AE03B9EC3-L004363](../../agents/web_agent.py#L4363) | 4363 | `"                    repair_plan = dict(plan)"` | — |
| [SRC-1AE03B9EC3-L004364](../../agents/web_agent.py#L4364) | 4364 | `"                    repair_plan.update({"` | — |
| [SRC-1AE03B9EC3-L004365](../../agents/web_agent.py#L4365) | 4365 | `"                        \"queries\": [repair_query],"` | — |
| [SRC-1AE03B9EC3-L004366](../../agents/web_agent.py#L4366) | 4366 | `"                        \"depth\": \"standard\","` | — |
| [SRC-1AE03B9EC3-L004367](../../agents/web_agent.py#L4367) | 4367 | `"                        \"social_focus\": False,"` | — |
| [SRC-1AE03B9EC3-L004368](../../agents/web_agent.py#L4368) | 4368 | `"                        \"platforms\": [],"` | — |
| [SRC-1AE03B9EC3-L004369](../../agents/web_agent.py#L4369) | 4369 | `"                        \"direct_urls\": [],"` | — |
| [SRC-1AE03B9EC3-L004370](../../agents/web_agent.py#L4370) | 4370 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L004371](../../agents/web_agent.py#L4371) | 4371 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L004372](../../agents/web_agent.py#L4372) | 4372 | `"                        repair_sources, repair_warnings, repair_report = self._collect_research("` | — |
| [SRC-1AE03B9EC3-L004373](../../agents/web_agent.py#L4373) | 4373 | `"                            repair_plan"` | — |
| [SRC-1AE03B9EC3-L004374](../../agents/web_agent.py#L4374) | 4374 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004375](../../agents/web_agent.py#L4375) | 4375 | `"                    except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L004376](../../agents/web_agent.py#L4376) | 4376 | `"                        repair_sources = []"` | — |
| [SRC-1AE03B9EC3-L004377](../../agents/web_agent.py#L4377) | 4377 | `"                        repair_warnings = []"` | — |
| [SRC-1AE03B9EC3-L004378](../../agents/web_agent.py#L4378) | 4378 | `"                        repair_report = {"` | — |
| [SRC-1AE03B9EC3-L004379](../../agents/web_agent.py#L4379) | 4379 | `"                            \"queries_planned\": 1,"` | — |
| [SRC-1AE03B9EC3-L004380](../../agents/web_agent.py#L4380) | 4380 | `"                            \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L004381](../../agents/web_agent.py#L4381) | 4381 | `"                            \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L004382](../../agents/web_agent.py#L4382) | 4382 | `"                            \"search_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L004383](../../agents/web_agent.py#L4383) | 4383 | `"                            \"search_outcome\": \"unknown_after_research_error\","` | — |
| [SRC-1AE03B9EC3-L004384](../../agents/web_agent.py#L4384) | 4384 | `"                            \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L004385](../../agents/web_agent.py#L4385) | 4385 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L004386](../../agents/web_agent.py#L4386) | 4386 | `"                        search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004387](../../agents/web_agent.py#L4387) | 4387 | `"                            \"تعذر تنفيذ محاولة البحث الإضافية المحدودة (\""` | — |
| [SRC-1AE03B9EC3-L004388](../../agents/web_agent.py#L4388) | 4388 | `"                            + type(exc).__name__ + \").\""` | — |
| [SRC-1AE03B9EC3-L004389](../../agents/web_agent.py#L4389) | 4389 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004390](../../agents/web_agent.py#L4390) | 4390 | `"                    search_warnings.extend(repair_warnings)"` | — |
| [SRC-1AE03B9EC3-L004391](../../agents/web_agent.py#L4391) | 4391 | `"                    evidence_repair[\"attempted_query_count\"] = 1"` | — |
| [SRC-1AE03B9EC3-L004392](../../agents/web_agent.py#L4392) | 4392 | `"                    evidence_repair[\"initial_source_count\"] = initial_source_count"` | — |
| [SRC-1AE03B9EC3-L004393](../../agents/web_agent.py#L4393) | 4393 | `"                    evidence_repair[\"initial_independent_domain_count\"] = initial_domain_count"` | — |
| [SRC-1AE03B9EC3-L004394](../../agents/web_agent.py#L4394) | 4394 | `"                    evidence_repair[\"new_sources_added\"] = 0"` | — |
| [SRC-1AE03B9EC3-L004395](../../agents/web_agent.py#L4395) | 4395 | `"                    source_indexes: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L004396](../../agents/web_agent.py#L4396) | 4396 | `"                    for source_index, source in enumerate(sources):"` | — |
| [SRC-1AE03B9EC3-L004397](../../agents/web_agent.py#L4397) | 4397 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L004398](../../agents/web_agent.py#L4398) | 4398 | `"                        if source_key:"` | — |
| [SRC-1AE03B9EC3-L004399](../../agents/web_agent.py#L4399) | 4399 | `"                            source_indexes.setdefault(source_key, source_index)"` | — |
| [SRC-1AE03B9EC3-L004400](../../agents/web_agent.py#L4400) | 4400 | `"                    relevant_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004401](../../agents/web_agent.py#L4401) | 4401 | `"                        query"` | — |
| [SRC-1AE03B9EC3-L004402](../../agents/web_agent.py#L4402) | 4402 | `"                        for query in ("` | — |
| [SRC-1AE03B9EC3-L004403](../../agents/web_agent.py#L4403) | 4403 | `"                            compact_search_query(question),"` | — |
| [SRC-1AE03B9EC3-L004404](../../agents/web_agent.py#L4404) | 4404 | `"                            *("` | — |
| [SRC-1AE03B9EC3-L004405](../../agents/web_agent.py#L4405) | 4405 | `"                                compact_search_query(candidate)"` | — |
| [SRC-1AE03B9EC3-L004406](../../agents/web_agent.py#L4406) | 4406 | `"                                for candidate in original_queries"` | — |
| [SRC-1AE03B9EC3-L004407](../../agents/web_agent.py#L4407) | 4407 | `"                                if isinstance(candidate, str)"` | — |
| [SRC-1AE03B9EC3-L004408](../../agents/web_agent.py#L4408) | 4408 | `"                            ),"` | — |
| [SRC-1AE03B9EC3-L004409](../../agents/web_agent.py#L4409) | 4409 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004410](../../agents/web_agent.py#L4410) | 4410 | `"                        if query"` | — |
| [SRC-1AE03B9EC3-L004411](../../agents/web_agent.py#L4411) | 4411 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L004412](../../agents/web_agent.py#L4412) | 4412 | `"                    for source in repair_sources:"` | — |
| [SRC-1AE03B9EC3-L004413](../../agents/web_agent.py#L4413) | 4413 | `"                        if not isinstance(source, dict):"` | — |
| [SRC-1AE03B9EC3-L004414](../../agents/web_agent.py#L4414) | 4414 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L004415](../../agents/web_agent.py#L4415) | 4415 | `"                        if not any("` | — |
| [SRC-1AE03B9EC3-L004416](../../agents/web_agent.py#L4416) | 4416 | `"                            self._source_matches_query(candidate, source)"` | — |
| [SRC-1AE03B9EC3-L004417](../../agents/web_agent.py#L4417) | 4417 | `"                            for candidate in relevant_queries if candidate"` | — |
| [SRC-1AE03B9EC3-L004418](../../agents/web_agent.py#L4418) | 4418 | `"                        ):"` | — |
| [SRC-1AE03B9EC3-L004419](../../agents/web_agent.py#L4419) | 4419 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L004420](../../agents/web_agent.py#L4420) | 4420 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L004421](../../agents/web_agent.py#L4421) | 4421 | `"                        if not source_key:"` | — |
| [SRC-1AE03B9EC3-L004422](../../agents/web_agent.py#L4422) | 4422 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L004423](../../agents/web_agent.py#L4423) | 4423 | `"                        existing_index = source_indexes.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L004424](../../agents/web_agent.py#L4424) | 4424 | `"                        if existing_index is None:"` | — |
| [SRC-1AE03B9EC3-L004425](../../agents/web_agent.py#L4425) | 4425 | `"                            source_indexes[source_key] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004426](../../agents/web_agent.py#L4426) | 4426 | `"                            sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004427](../../agents/web_agent.py#L4427) | 4427 | `"                            evidence_repair[\"new_sources_added\"] += 1"` | — |
| [SRC-1AE03B9EC3-L004428](../../agents/web_agent.py#L4428) | 4428 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L004429](../../agents/web_agent.py#L4429) | 4429 | `"                        existing_source = sources[existing_index]"` | — |
| [SRC-1AE03B9EC3-L004430](../../agents/web_agent.py#L4430) | 4430 | `"                        providers = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004431](../../agents/web_agent.py#L4431) | 4431 | `"                            list(existing_source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L004432](../../agents/web_agent.py#L4432) | 4432 | `"                            + list(source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L004433](../../agents/web_agent.py#L4433) | 4433 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L004434](../../agents/web_agent.py#L4434) | 4434 | `"                        source_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004435](../../agents/web_agent.py#L4435) | 4435 | `"                            list(existing_source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L004436](../../agents/web_agent.py#L4436) | 4436 | `"                            + list(source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L004437](../../agents/web_agent.py#L4437) | 4437 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L004438](../../agents/web_agent.py#L4438) | 4438 | `"                        if source.get(\"page_fetched\") and not existing_source.get(\"page_fetched\"):"` | — |
| [SRC-1AE03B9EC3-L004439](../../agents/web_agent.py#L4439) | 4439 | `"                            merged_source = dict(existing_source)"` | — |
| [SRC-1AE03B9EC3-L004440](../../agents/web_agent.py#L4440) | 4440 | `"                            merged_source.update(source)"` | — |
| [SRC-1AE03B9EC3-L004441](../../agents/web_agent.py#L4441) | 4441 | `"                            merged_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L004442](../../agents/web_agent.py#L4442) | 4442 | `"                            merged_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L004443](../../agents/web_agent.py#L4443) | 4443 | `"                            sources[existing_index] = merged_source"` | — |
| [SRC-1AE03B9EC3-L004444](../../agents/web_agent.py#L4444) | 4444 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L004445](../../agents/web_agent.py#L4445) | 4445 | `"                            existing_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L004446](../../agents/web_agent.py#L4446) | 4446 | `"                            existing_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L004447](../../agents/web_agent.py#L4447) | 4447 | `"                    sources.sort("` | — |
| [SRC-1AE03B9EC3-L004448](../../agents/web_agent.py#L4448) | 4448 | `"                        key=lambda item: float(item.get(\"rank_score\", 0) or 0),"` | — |
| [SRC-1AE03B9EC3-L004449](../../agents/web_agent.py#L4449) | 4449 | `"                        reverse=True,"` | — |
| [SRC-1AE03B9EC3-L004450](../../agents/web_agent.py#L4450) | 4450 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004451](../../agents/web_agent.py#L4451) | 4451 | `"                    plan[\"queries\"] = list(dict.fromkeys(original_queries + [repair_query]))"` | — |
| [SRC-1AE03B9EC3-L004452](../../agents/web_agent.py#L4452) | 4452 | `"                    independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L004453](../../agents/web_agent.py#L4453) | 4453 | `"                        registrable_domain("` | — |
| [SRC-1AE03B9EC3-L004454](../../agents/web_agent.py#L4454) | 4454 | `"                            source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L004455](../../agents/web_agent.py#L4455) | 4455 | `"                            or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L004456](../../agents/web_agent.py#L4456) | 4456 | `"                            or \"\""` | — |
| [SRC-1AE03B9EC3-L004457](../../agents/web_agent.py#L4457) | 4457 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004458](../../agents/web_agent.py#L4458) | 4458 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L004459](../../agents/web_agent.py#L4459) | 4459 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L004460](../../agents/web_agent.py#L4460) | 4460 | `"                    independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L004461](../../agents/web_agent.py#L4461) | 4461 | `"                    needs_corroboration = ("` | — |
| [SRC-1AE03B9EC3-L004462](../../agents/web_agent.py#L4462) | 4462 | `"                        len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L004463](../../agents/web_agent.py#L4463) | 4463 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004464](../../agents/web_agent.py#L4464) | 4464 | `"                    evidence_repair.update({"` | — |
| [SRC-1AE03B9EC3-L004465](../../agents/web_agent.py#L4465) | 4465 | `"                        \"final_source_count\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L004466](../../agents/web_agent.py#L4466) | 4466 | `"                        \"final_independent_domain_count\": len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L004467](../../agents/web_agent.py#L4467) | 4467 | `"                        \"recovered\": not needs_corroboration,"` | — |
| [SRC-1AE03B9EC3-L004468](../../agents/web_agent.py#L4468) | 4468 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L004469](../../agents/web_agent.py#L4469) | 4469 | `"                    evidence_repair[\"reason\"] = ("` | — |
| [SRC-1AE03B9EC3-L004470](../../agents/web_agent.py#L4470) | 4470 | `"                        \"single_bounded_retry_still_insufficient\""` | — |
| [SRC-1AE03B9EC3-L004471](../../agents/web_agent.py#L4471) | 4471 | `"                        if needs_corroboration else \"evidence_gate_recovered\""` | — |
| [SRC-1AE03B9EC3-L004472](../../agents/web_agent.py#L4472) | 4472 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004473](../../agents/web_agent.py#L4473) | 4473 | `"                    report[\"queries_planned\"] = int(report.get(\"queries_planned\", 0) or 0) + int("` | — |
| [SRC-1AE03B9EC3-L004474](../../agents/web_agent.py#L4474) | 4474 | `"                        repair_report.get(\"queries_planned\", 1) or 0"` | — |
| [SRC-1AE03B9EC3-L004475](../../agents/web_agent.py#L4475) | 4475 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004476](../../agents/web_agent.py#L4476) | 4476 | `"                    initial_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L004477](../../agents/web_agent.py#L4477) | 4477 | `"                    repair_attempt_count = repair_report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L004478](../../agents/web_agent.py#L4478) | 4478 | `"                    if initial_attempt_count is None or repair_attempt_count is None:"` | — |
| [SRC-1AE03B9EC3-L004479](../../agents/web_agent.py#L4479) | 4479 | `"                        report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L004480](../../agents/web_agent.py#L4480) | 4480 | `"                        report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L004481](../../agents/web_agent.py#L4481) | 4481 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L004482](../../agents/web_agent.py#L4482) | 4482 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L004483](../../agents/web_agent.py#L4483) | 4483 | `"                            report[\"queries_attempted\"] = max(0, int(initial_attempt_count or 0)) + max("` | — |
| [SRC-1AE03B9EC3-L004484](../../agents/web_agent.py#L4484) | 4484 | `"                                0, int(repair_attempt_count or 0)"` | — |
| [SRC-1AE03B9EC3-L004485](../../agents/web_agent.py#L4485) | 4485 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L004486](../../agents/web_agent.py#L4486) | 4486 | `"                            report[\"queries_attempted_known\"] = True"` | — |
| [SRC-1AE03B9EC3-L004487](../../agents/web_agent.py#L4487) | 4487 | `"                        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L004488](../../agents/web_agent.py#L4488) | 4488 | `"                            report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L004489](../../agents/web_agent.py#L4489) | 4489 | `"                            report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L004490](../../agents/web_agent.py#L4490) | 4490 | `"                    report[\"query_results\"] = list(report.get(\"query_results\", [])) + list("` | — |
| [SRC-1AE03B9EC3-L004491](../../agents/web_agent.py#L4491) | 4491 | `"                        repair_report.get(\"query_results\", [])"` | — |
| [SRC-1AE03B9EC3-L004492](../../agents/web_agent.py#L4492) | 4492 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004493](../../agents/web_agent.py#L4493) | 4493 | `"                    merged_providers = {"` | — |
| [SRC-1AE03B9EC3-L004494](../../agents/web_agent.py#L4494) | 4494 | `"                        provider"` | — |
| [SRC-1AE03B9EC3-L004495](../../agents/web_agent.py#L4495) | 4495 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L004496](../../agents/web_agent.py#L4496) | 4496 | `"                        for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L004497](../../agents/web_agent.py#L4497) | 4497 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L004498](../../agents/web_agent.py#L4498) | 4498 | `"                    report[\"providers_used\"] = sorted(merged_providers)"` | — |
| [SRC-1AE03B9EC3-L004499](../../agents/web_agent.py#L4499) | 4499 | `"                    report[\"provider_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L004500](../../agents/web_agent.py#L4500) | 4500 | `"                        provider: sum("` | — |
| [SRC-1AE03B9EC3-L004501](../../agents/web_agent.py#L4501) | 4501 | `"                            provider in source.get(\"providers\", []) for source in sources"` | — |
| [SRC-1AE03B9EC3-L004502](../../agents/web_agent.py#L4502) | 4502 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004503](../../agents/web_agent.py#L4503) | 4503 | `"                        for provider in merged_providers"` | — |
| [SRC-1AE03B9EC3-L004504](../../agents/web_agent.py#L4504) | 4504 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L004505](../../agents/web_agent.py#L4505) | 4505 | `"                    report[\"platform_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L004506](../../agents/web_agent.py#L4506) | 4506 | `"                        str(source.get(\"platform\", \"web\")): sum("` | — |
| [SRC-1AE03B9EC3-L004507](../../agents/web_agent.py#L4507) | 4507 | `"                            str(other.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L004508](../../agents/web_agent.py#L4508) | 4508 | `"                            == str(source.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L004509](../../agents/web_agent.py#L4509) | 4509 | `"                            for other in sources"` | — |
| [SRC-1AE03B9EC3-L004510](../../agents/web_agent.py#L4510) | 4510 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004511](../../agents/web_agent.py#L4511) | 4511 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L004512](../../agents/web_agent.py#L4512) | 4512 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L004513](../../agents/web_agent.py#L4513) | 4513 | `"                    report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004514](../../agents/web_agent.py#L4514) | 4514 | `"                    report[\"pages_fetched\"] = sum("` | — |
| [SRC-1AE03B9EC3-L004515](../../agents/web_agent.py#L4515) | 4515 | `"                        bool(source.get(\"page_fetched\")) for source in sources"` | — |
| [SRC-1AE03B9EC3-L004516](../../agents/web_agent.py#L4516) | 4516 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004517](../../agents/web_agent.py#L4517) | 4517 | `"                    report[\"independent_sources\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L004518](../../agents/web_agent.py#L4518) | 4518 | `"                    report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L004519](../../agents/web_agent.py#L4519) | 4519 | `"                    report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L004520](../../agents/web_agent.py#L4520) | 4520 | `"                        sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L004521](../../agents/web_agent.py#L4521) | 4521 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004522](../../agents/web_agent.py#L4522) | 4522 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L004523](../../agents/web_agent.py#L4523) | 4523 | `"                    evidence_repair[\"reason\"] = \"repair_query_was_not_distinct\""` | — |
| [SRC-1AE03B9EC3-L004524](../../agents/web_agent.py#L4524) | 4524 | `"        report[\"evidence_repair\"] = evidence_repair"` | — |
| [SRC-1AE03B9EC3-L004525](../../agents/web_agent.py#L4525) | 4525 | `"        baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L004526](../../agents/web_agent.py#L4526) | 4526 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L004527](../../agents/web_agent.py#L4527) | 4527 | `"            current_research_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L004528](../../agents/web_agent.py#L4528) | 4528 | `"                item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004529](../../agents/web_agent.py#L4529) | 4529 | `"                if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L004530](../../agents/web_agent.py#L4530) | 4530 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L004531](../../agents/web_agent.py#L4531) | 4531 | `"        report[\"provider_diagnostics\"] = current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004532](../../agents/web_agent.py#L4532) | 4532 | `"        provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L004533](../../agents/web_agent.py#L4533) | 4533 | `"            item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L004534](../../agents/web_agent.py#L4534) | 4534 | `"            for item in current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004535](../../agents/web_agent.py#L4535) | 4535 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004536](../../agents/web_agent.py#L4536) | 4536 | `"        raw_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L004537](../../agents/web_agent.py#L4537) | 4537 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L004538](../../agents/web_agent.py#L4538) | 4538 | `"            queries_attempted = ("` | — |
| [SRC-1AE03B9EC3-L004539](../../agents/web_agent.py#L4539) | 4539 | `"                None if raw_attempt_count is None"` | — |
| [SRC-1AE03B9EC3-L004540](../../agents/web_agent.py#L4540) | 4540 | `"                else max(0, int(raw_attempt_count or 0))"` | — |
| [SRC-1AE03B9EC3-L004541](../../agents/web_agent.py#L4541) | 4541 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004542](../../agents/web_agent.py#L4542) | 4542 | `"        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L004543](../../agents/web_agent.py#L4543) | 4543 | `"            queries_attempted = None"` | — |
| [SRC-1AE03B9EC3-L004544](../../agents/web_agent.py#L4544) | 4544 | `"        if queries_attempted is not None:"` | — |
| [SRC-1AE03B9EC3-L004545](../../agents/web_agent.py#L4545) | 4545 | `"            search_attempted = ("` | — |
| [SRC-1AE03B9EC3-L004546](../../agents/web_agent.py#L4546) | 4546 | `"                queries_attempted > 0"` | — |
| [SRC-1AE03B9EC3-L004547](../../agents/web_agent.py#L4547) | 4547 | `"                or provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L004548](../../agents/web_agent.py#L4548) | 4548 | `"                or report.get(\"search_attempted\") is True"` | — |
| [SRC-1AE03B9EC3-L004549](../../agents/web_agent.py#L4549) | 4549 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004550](../../agents/web_agent.py#L4550) | 4550 | `"        elif provider_attempt_observed or report.get(\"search_attempted\") is True:"` | — |
| [SRC-1AE03B9EC3-L004551](../../agents/web_agent.py#L4551) | 4551 | `"            search_attempted = True"` | — |
| [SRC-1AE03B9EC3-L004552](../../agents/web_agent.py#L4552) | 4552 | `"        elif isinstance(report.get(\"search_attempted\"), bool):"` | — |
| [SRC-1AE03B9EC3-L004553](../../agents/web_agent.py#L4553) | 4553 | `"            search_attempted = report[\"search_attempted\"]"` | — |
| [SRC-1AE03B9EC3-L004554](../../agents/web_agent.py#L4554) | 4554 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L004555](../../agents/web_agent.py#L4555) | 4555 | `"            search_attempted = None"` | — |
| [SRC-1AE03B9EC3-L004556](../../agents/web_agent.py#L4556) | 4556 | `"        report[\"queries_attempted\"] = queries_attempted"` | — |
| [SRC-1AE03B9EC3-L004557](../../agents/web_agent.py#L4557) | 4557 | `"        report[\"queries_attempted_known\"] = queries_attempted is not None"` | — |
| [SRC-1AE03B9EC3-L004558](../../agents/web_agent.py#L4558) | 4558 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L004559](../../agents/web_agent.py#L4559) | 4559 | `"        previous_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L004560](../../agents/web_agent.py#L4560) | 4560 | `"        if previous_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L004561](../../agents/web_agent.py#L4561) | 4561 | `"            if provider_attempt_observed or search_attempted is True:"` | — |
| [SRC-1AE03B9EC3-L004562](../../agents/web_agent.py#L4562) | 4562 | `"                search_outcome = \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L004563](../../agents/web_agent.py#L4563) | 4563 | `"            elif search_attempted is False:"` | — |
| [SRC-1AE03B9EC3-L004564](../../agents/web_agent.py#L4564) | 4564 | `"                search_outcome = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L004565](../../agents/web_agent.py#L4565) | 4565 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004566](../../agents/web_agent.py#L4566) | 4566 | `"                search_outcome = \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L004567](../../agents/web_agent.py#L4567) | 4567 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L004568](../../agents/web_agent.py#L4568) | 4568 | `"            search_outcome = ("` | — |
| [SRC-1AE03B9EC3-L004569](../../agents/web_agent.py#L4569) | 4569 | `"                \"attempted_with_usable_sources\" if search_attempted is True and sources"` | — |
| [SRC-1AE03B9EC3-L004570](../../agents/web_agent.py#L4570) | 4570 | `"                else \"attempted_no_usable_sources\" if search_attempted is True"` | — |
| [SRC-1AE03B9EC3-L004571](../../agents/web_agent.py#L4571) | 4571 | `"                else \"not_attempted\" if search_attempted is False"` | — |
| [SRC-1AE03B9EC3-L004572](../../agents/web_agent.py#L4572) | 4572 | `"                else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L004573](../../agents/web_agent.py#L4573) | 4573 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004574](../../agents/web_agent.py#L4574) | 4574 | `"        report[\"search_outcome\"] = search_outcome"` | — |
| [SRC-1AE03B9EC3-L004575](../../agents/web_agent.py#L4575) | 4575 | `"        if search_outcome in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L004576](../../agents/web_agent.py#L4576) | 4576 | `"            report[\"usable_sources_after_filtering\"] = None"` | — |
| [SRC-1AE03B9EC3-L004577](../../agents/web_agent.py#L4577) | 4577 | `"            report[\"unique_sources\"] = None"` | — |
| [SRC-1AE03B9EC3-L004578](../../agents/web_agent.py#L4578) | 4578 | `"            report[\"pages_fetched\"] = None"` | — |
| [SRC-1AE03B9EC3-L004579](../../agents/web_agent.py#L4579) | 4579 | `"            report[\"provider_counts\"] = None"` | — |
| [SRC-1AE03B9EC3-L004580](../../agents/web_agent.py#L4580) | 4580 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L004581](../../agents/web_agent.py#L4581) | 4581 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004582](../../agents/web_agent.py#L4582) | 4582 | `"            if report.get(\"unique_sources\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L004583](../../agents/web_agent.py#L4583) | 4583 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004584](../../agents/web_agent.py#L4584) | 4584 | `"            if report.get(\"pages_fetched\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L004585](../../agents/web_agent.py#L4585) | 4585 | `"                report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L004586](../../agents/web_agent.py#L4586) | 4586 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L004587](../../agents/web_agent.py#L4587) | 4587 | `"        report[\"distinct_registrable_domains\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L004588](../../agents/web_agent.py#L4588) | 4588 | `"        report[\"independent_sources\"] = len(independent_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L004589](../../agents/web_agent.py#L4589) | 4589 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L004590](../../agents/web_agent.py#L4590) | 4590 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L004591](../../agents/web_agent.py#L4591) | 4591 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004592](../../agents/web_agent.py#L4592) | 4592 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L004593](../../agents/web_agent.py#L4593) | 4593 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L004594](../../agents/web_agent.py#L4594) | 4594 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004595](../../agents/web_agent.py#L4595) | 4595 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L004596](../../agents/web_agent.py#L4596) | 4596 | `"        if len(independent_domains) >= 2:"` | — |
| [SRC-1AE03B9EC3-L004597](../../agents/web_agent.py#L4597) | 4597 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004598](../../agents/web_agent.py#L4598) | 4598 | `"                \"تعدد النطاقات المسجلة لا يثبت الاستقلال التحريري؛ قد تنقل المواقع عن المصدر الأصلي نفسه.\""` | — |
| [SRC-1AE03B9EC3-L004599](../../agents/web_agent.py#L4599) | 4599 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004600](../../agents/web_agent.py#L4600) | 4600 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L004601](../../agents/web_agent.py#L4601) | 4601 | `"        if needs_corroboration and single_source_navigation and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L004602](../../agents/web_agent.py#L4602) | 4602 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004603](../../agents/web_agent.py#L4603) | 4603 | `"                \"هذه نتيجة مرشحة لطلب العثور على موقع/رابط؛ لم تُثبت رسميتها أو صحتها \""` | — |
| [SRC-1AE03B9EC3-L004604](../../agents/web_agent.py#L4604) | 4604 | `"                \"من مصدر مستقل، لذا راجع الرابط قبل الاعتماد عليه.\""` | — |
| [SRC-1AE03B9EC3-L004605](../../agents/web_agent.py#L4605) | 4605 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004606](../../agents/web_agent.py#L4606) | 4606 | `"        if needs_corroboration and (single_source_social or single_source_lead) and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L004607](../../agents/web_agent.py#L4607) | 4607 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004608](../../agents/web_agent.py#L4608) | 4608 | `"                \"هذه إشارات بحث أولية وليست تحققًا مستقلًا من هوية العميل أو نيته؛ \""` | — |
| [SRC-1AE03B9EC3-L004609](../../agents/web_agent.py#L4609) | 4609 | `"                \"راجع المنشور وتاريخه وسياقه قبل التواصل أو اتخاذ قرار.\""` | — |
| [SRC-1AE03B9EC3-L004610](../../agents/web_agent.py#L4610) | 4610 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004611](../../agents/web_agent.py#L4611) | 4611 | `"        if needs_corroboration and single_source_listing and not single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L004612](../../agents/web_agent.py#L4612) | 4612 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004613](../../agents/web_agent.py#L4613) | 4613 | `"                \"هذه إعلانات/قوائم مرشحة فقط. قد تكون منتهية أو غير دقيقة؛ تحقق من السعر \""` | — |
| [SRC-1AE03B9EC3-L004614](../../agents/web_agent.py#L4614) | 4614 | `"                \"والتوافر ومصدر الإعلان واطلب تأكيدًا حديثًا قبل دفع مال أو مشاركة بيانات.\""` | — |
| [SRC-1AE03B9EC3-L004615](../../agents/web_agent.py#L4615) | 4615 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004616](../../agents/web_agent.py#L4616) | 4616 | `"        search_warning = \"؛ \".join(dict.fromkeys(search_warnings)) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L004617](../../agents/web_agent.py#L4617) | 4617 | `"        if needs_corroboration and not task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L004618](../../agents/web_agent.py#L4618) | 4618 | `"            if search_outcome == \"unknown_after_research_error\":"` | — |
| [SRC-1AE03B9EC3-L004619](../../agents/web_agent.py#L4619) | 4619 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004620](../../agents/web_agent.py#L4620) | 4620 | `"                    \"تعذر إكمال مسار البحث بسبب خطأ، ولا توجد بيانات كافية لتحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L004621](../../agents/web_agent.py#L4621) | 4621 | `"                    \"كانت محاولة البحث قد اكتملت أو كم نتيجة جُمعت. لذلك لا أستطيع الجزم \""` | — |
| [SRC-1AE03B9EC3-L004622](../../agents/web_agent.py#L4622) | 4622 | `"                    \"بأن البحث لم يُنفّذ أو أن الإنترنت لم يُعد نتائج. لم أتمكن من تقديم \""` | — |
| [SRC-1AE03B9EC3-L004623](../../agents/web_agent.py#L4623) | 4623 | `"                    \"إجابة مكتملة؛ أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L004624](../../agents/web_agent.py#L4624) | 4624 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004625](../../agents/web_agent.py#L4625) | 4625 | `"            elif search_outcome == \"attempted_research_error\":"` | — |
| [SRC-1AE03B9EC3-L004626](../../agents/web_agent.py#L4626) | 4626 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004627](../../agents/web_agent.py#L4627) | 4627 | `"                    \"توجد قرائن تشغيلية على بدء محاولة بحث، لكن مسار البحث فشل قبل إنتاج \""` | — |
| [SRC-1AE03B9EC3-L004628](../../agents/web_agent.py#L4628) | 4628 | `"                    \"تقرير مكتمل. لا أستطيع تحديد عدد النتائج أو المصادر القابلة للاستخدام، \""` | — |
| [SRC-1AE03B9EC3-L004629](../../agents/web_agent.py#L4629) | 4629 | `"                    \"لذلك لن أخمّن. أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L004630](../../agents/web_agent.py#L4630) | 4630 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004631](../../agents/web_agent.py#L4631) | 4631 | `"            elif search_outcome == \"attempted_no_usable_sources\":"` | — |
| [SRC-1AE03B9EC3-L004632](../../agents/web_agent.py#L4632) | 4632 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004633](../../agents/web_agent.py#L4633) | 4633 | `"                    \"جرت محاولة البحث، لكن لم تتوفر مصادر صالحة وكافية للإجابة بعد تصفية \""` | — |
| [SRC-1AE03B9EC3-L004634](../../agents/web_agent.py#L4634) | 4634 | `"                    \"النتائج. هذا لا يثبت أن جميع المواقع أو الإنترنت غير متاح؛ لن أخمّن \""` | — |
| [SRC-1AE03B9EC3-L004635](../../agents/web_agent.py#L4635) | 4635 | `"                    \"أو أقدّم نتيجة غير مدعومة. جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L004636](../../agents/web_agent.py#L4636) | 4636 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004637](../../agents/web_agent.py#L4637) | 4637 | `"            elif search_outcome == \"not_attempted\":"` | — |
| [SRC-1AE03B9EC3-L004638](../../agents/web_agent.py#L4638) | 4638 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004639](../../agents/web_agent.py#L4639) | 4639 | `"                    \"لم تبدأ محاولة بحث ويب لهذا الطلب، لذلك لا تتوفر لدي أدلة ويب حالية \""` | — |
| [SRC-1AE03B9EC3-L004640](../../agents/web_agent.py#L4640) | 4640 | `"                    \"كافية للإجابة. لن أقدّم نتيجة غير مدعومة؛ أعد المحاولة أو اطلب بحثًا \""` | — |
| [SRC-1AE03B9EC3-L004641](../../agents/web_agent.py#L4641) | 4641 | `"                    \"صريحًا إذا كان ذلك مناسبًا.\""` | — |
| [SRC-1AE03B9EC3-L004642](../../agents/web_agent.py#L4642) | 4642 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004643](../../agents/web_agent.py#L4643) | 4643 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004644](../../agents/web_agent.py#L4644) | 4644 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004645](../../agents/web_agent.py#L4645) | 4645 | `"                    \"لم أجد معلومات موثوقة كافية مرتبطة بسؤالك من نطاقين مسجلين مختلفين على الأقل. \""` | — |
| [SRC-1AE03B9EC3-L004646](../../agents/web_agent.py#L4646) | 4646 | `"                    \"اختلاف النطاقات لا يثبت الاستقلال التحريري. لن أخمّن أو أقدّم نتيجة غير مدعومة؛ \""` | — |
| [SRC-1AE03B9EC3-L004647](../../agents/web_agent.py#L4647) | 4647 | `"                    \"جرّب صياغة أدق أو أعد المحاولة لاحقًا.\""` | — |
| [SRC-1AE03B9EC3-L004648](../../agents/web_agent.py#L4648) | 4648 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004649](../../agents/web_agent.py#L4649) | 4649 | `"            public_sources = [{"` | — |
| [SRC-1AE03B9EC3-L004650](../../agents/web_agent.py#L4650) | 4650 | `"                \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L004651](../../agents/web_agent.py#L4651) | 4651 | `"                \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L004652](../../agents/web_agent.py#L4652) | 4652 | `"                \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004653](../../agents/web_agent.py#L4653) | 4653 | `"                \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L004654](../../agents/web_agent.py#L4654) | 4654 | `"                \"page_fetch_status\": source.get(\"page_fetch_status\", \"unknown\"),"` | — |
| [SRC-1AE03B9EC3-L004655](../../agents/web_agent.py#L4655) | 4655 | `"                \"page_fetch_error_class\": source.get(\"page_fetch_error_class\"),"` | — |
| [SRC-1AE03B9EC3-L004656](../../agents/web_agent.py#L4656) | 4656 | `"                \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L004657](../../agents/web_agent.py#L4657) | 4657 | `"                \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L004658](../../agents/web_agent.py#L4658) | 4658 | `"                \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L004659](../../agents/web_agent.py#L4659) | 4659 | `"                \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004660](../../agents/web_agent.py#L4660) | 4660 | `"                \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L004661](../../agents/web_agent.py#L4661) | 4661 | `"                \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004662](../../agents/web_agent.py#L4662) | 4662 | `"                \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004663](../../agents/web_agent.py#L4663) | 4663 | `"                \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004664](../../agents/web_agent.py#L4664) | 4664 | `"                \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L004665](../../agents/web_agent.py#L4665) | 4665 | `"                \"lead_qualification\": source.get(\"lead_qualification\"),"` | — |
| [SRC-1AE03B9EC3-L004666](../../agents/web_agent.py#L4666) | 4666 | `"                \"lead_intent_evidence\": source.get(\"lead_intent_evidence\"),"` | — |
| [SRC-1AE03B9EC3-L004667](../../agents/web_agent.py#L4667) | 4667 | `"            } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L004668](../../agents/web_agent.py#L4668) | 4668 | `"            citation_validation = self._citation_validation_metadata("` | — |
| [SRC-1AE03B9EC3-L004669](../../agents/web_agent.py#L4669) | 4669 | `"                reason, 0, [], \"not_run\""` | — |
| [SRC-1AE03B9EC3-L004670](../../agents/web_agent.py#L4670) | 4670 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004671](../../agents/web_agent.py#L4671) | 4671 | `"            citation_validation[\"status\"] = \"not_applicable_no_generated_answer\""` | — |
| [SRC-1AE03B9EC3-L004672](../../agents/web_agent.py#L4672) | 4672 | `"            coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L004673](../../agents/web_agent.py#L4673) | 4673 | `"            answer_coverage = {"` | — |
| [SRC-1AE03B9EC3-L004674](../../agents/web_agent.py#L4674) | 4674 | `"                \"method\": \"explicit_criteria_heuristic\","` | — |
| [SRC-1AE03B9EC3-L004675](../../agents/web_agent.py#L4675) | 4675 | `"                \"targets\": coverage_targets,"` | — |
| [SRC-1AE03B9EC3-L004676](../../agents/web_agent.py#L4676) | 4676 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L004677](../../agents/web_agent.py#L4677) | 4677 | `"                    \"not_reviewed_insufficient_evidence\""` | — |
| [SRC-1AE03B9EC3-L004678](../../agents/web_agent.py#L4678) | 4678 | `"                    if coverage_targets else \"no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L004679](../../agents/web_agent.py#L4679) | 4679 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004680](../../agents/web_agent.py#L4680) | 4680 | `"                \"automatically_graded\": False,"` | — |
| [SRC-1AE03B9EC3-L004681](../../agents/web_agent.py#L4681) | 4681 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004682](../../agents/web_agent.py#L4682) | 4682 | `"            answer_integrity = audit_answer_integrity(question, reason, sources, coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L004683](../../agents/web_agent.py#L4683) | 4683 | `"            answer_coverage[\"target_checks\"] = answer_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L004684](../../agents/web_agent.py#L4684) | 4684 | `"            answer_coverage[\"potentially_missing_target_count\"] = answer_integrity[\"potentially_missing_target_count\"]"` | — |
| [SRC-1AE03B9EC3-L004685](../../agents/web_agent.py#L4685) | 4685 | `"            answer_coverage[\"lexical_screen_method\"] = \"deterministic_lexical_screen_only_not_semantic_grading\""` | — |
| [SRC-1AE03B9EC3-L004686](../../agents/web_agent.py#L4686) | 4686 | `"            task_fulfillment_status = ("` | — |
| [SRC-1AE03B9EC3-L004687](../../agents/web_agent.py#L4687) | 4687 | `"                \"not_assessed_insufficient_evidence\" if coverage_targets"` | — |
| [SRC-1AE03B9EC3-L004688](../../agents/web_agent.py#L4688) | 4688 | `"                else \"not_machine_assessed_no_explicit_targets_detected\""` | — |
| [SRC-1AE03B9EC3-L004689](../../agents/web_agent.py#L4689) | 4689 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004690](../../agents/web_agent.py#L4690) | 4690 | `"            answer_coverage[\"task_fulfillment_status\"] = task_fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L004691](../../agents/web_agent.py#L4691) | 4691 | `"            research_failed = search_outcome in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L004692](../../agents/web_agent.py#L4692) | 4692 | `"            report.update({"` | — |
| [SRC-1AE03B9EC3-L004693](../../agents/web_agent.py#L4693) | 4693 | `"                # When collection failed, an empty local list is not evidence that"` | — |
| [SRC-1AE03B9EC3-L004694](../../agents/web_agent.py#L4694) | 4694 | `"                # the remote search returned zero sources; preserve unknown counts."` | — |
| [SRC-1AE03B9EC3-L004695](../../agents/web_agent.py#L4695) | 4695 | `"                \"unique_sources\": None if research_failed else len(sources),"` | — |
| [SRC-1AE03B9EC3-L004696](../../agents/web_agent.py#L4696) | 4696 | `"                \"independent_sources\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L004697](../../agents/web_agent.py#L4697) | 4697 | `"                \"distinct_registrable_domains\": None if research_failed else len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L004698](../../agents/web_agent.py#L4698) | 4698 | `"                \"pages_fetched\": ("` | — |
| [SRC-1AE03B9EC3-L004699](../../agents/web_agent.py#L4699) | 4699 | `"                    None if research_failed"` | — |
| [SRC-1AE03B9EC3-L004700](../../agents/web_agent.py#L4700) | 4700 | `"                    else sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L004701](../../agents/web_agent.py#L4701) | 4701 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004702](../../agents/web_agent.py#L4702) | 4702 | `"                \"provider_diagnostics\": current_research_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L004703](../../agents/web_agent.py#L4703) | 4703 | `"                \"insufficient_evidence\": True,"` | — |
| [SRC-1AE03B9EC3-L004704](../../agents/web_agent.py#L4704) | 4704 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L004705](../../agents/web_agent.py#L4705) | 4705 | `"                \"citation_check\": citation_validation[\"status\"],"` | — |
| [SRC-1AE03B9EC3-L004706](../../agents/web_agent.py#L4706) | 4706 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L004707](../../agents/web_agent.py#L4707) | 4707 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L004708](../../agents/web_agent.py#L4708) | 4708 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L004709](../../agents/web_agent.py#L4709) | 4709 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L004710](../../agents/web_agent.py#L4710) | 4710 | `"                \"connector_summary\": report.get(\"connector_summary\") or self._connector_status_summary("` | — |
| [SRC-1AE03B9EC3-L004711](../../agents/web_agent.py#L4711) | 4711 | `"                    current_research_diagnostics, sources"` | — |
| [SRC-1AE03B9EC3-L004712](../../agents/web_agent.py#L4712) | 4712 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004713](../../agents/web_agent.py#L4713) | 4713 | `"            })"` | — |
| [SRC-1AE03B9EC3-L004714](../../agents/web_agent.py#L4714) | 4714 | `"            return {"` | — |
| [SRC-1AE03B9EC3-L004715](../../agents/web_agent.py#L4715) | 4715 | `"                \"answer\": reason,"` | — |
| [SRC-1AE03B9EC3-L004716](../../agents/web_agent.py#L4716) | 4716 | `"                \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L004717](../../agents/web_agent.py#L4717) | 4717 | `"                \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L004718](../../agents/web_agent.py#L4718) | 4718 | `"                \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L004719](../../agents/web_agent.py#L4719) | 4719 | `"                \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L004720](../../agents/web_agent.py#L4720) | 4720 | `"                    \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L004721](../../agents/web_agent.py#L4721) | 4721 | `"                    \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L004722](../../agents/web_agent.py#L4722) | 4722 | `"                    \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L004723](../../agents/web_agent.py#L4723) | 4723 | `"                    \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L004724](../../agents/web_agent.py#L4724) | 4724 | `"                    \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L004725](../../agents/web_agent.py#L4725) | 4725 | `"                    \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L004726](../../agents/web_agent.py#L4726) | 4726 | `"                    \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L004727](../../agents/web_agent.py#L4727) | 4727 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L004728](../../agents/web_agent.py#L4728) | 4728 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L004729](../../agents/web_agent.py#L4729) | 4729 | `"                },"` | — |
| [SRC-1AE03B9EC3-L004730](../../agents/web_agent.py#L4730) | 4730 | `"                \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L004731](../../agents/web_agent.py#L4731) | 4731 | `"                \"sources\": public_sources,"` | — |
| [SRC-1AE03B9EC3-L004732](../../agents/web_agent.py#L4732) | 4732 | `"                \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L004733](../../agents/web_agent.py#L4733) | 4733 | `"                \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L004734](../../agents/web_agent.py#L4734) | 4734 | `"                \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L004735](../../agents/web_agent.py#L4735) | 4735 | `"                \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L004736](../../agents/web_agent.py#L4736) | 4736 | `"                \"warnings\": list(dict.fromkeys(search_warnings + [reason])),"` | — |
| [SRC-1AE03B9EC3-L004737](../../agents/web_agent.py#L4737) | 4737 | `"                \"kind\": \"insufficient_evidence\","` | — |
| [SRC-1AE03B9EC3-L004738](../../agents/web_agent.py#L4738) | 4738 | `"                \"final_answer_status\": \"insufficient_evidence_no_generation\","` | — |
| [SRC-1AE03B9EC3-L004739](../../agents/web_agent.py#L4739) | 4739 | `"                \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L004740](../../agents/web_agent.py#L4740) | 4740 | `"                \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L004741](../../agents/web_agent.py#L4741) | 4741 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L004742](../../agents/web_agent.py#L4742) | 4742 | `"                \"citation_validation\": citation_validation,"` | — |
| [SRC-1AE03B9EC3-L004743](../../agents/web_agent.py#L4743) | 4743 | `"                \"answer_coverage\": answer_coverage,"` | — |
| [SRC-1AE03B9EC3-L004744](../../agents/web_agent.py#L4744) | 4744 | `"                \"answer_integrity\": answer_integrity,"` | — |
| [SRC-1AE03B9EC3-L004745](../../agents/web_agent.py#L4745) | 4745 | `"                \"task_fulfillment_status\": task_fulfillment_status,"` | — |
| [SRC-1AE03B9EC3-L004746](../../agents/web_agent.py#L4746) | 4746 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004747](../../agents/web_agent.py#L4747) | 4747 | `""` | — |
| [SRC-1AE03B9EC3-L004748](../../agents/web_agent.py#L4748) | 4748 | `"        answer = \"\""` | — |
| [SRC-1AE03B9EC3-L004749](../../agents/web_agent.py#L4749) | 4749 | `"        used_llm = False"` | — |
| [SRC-1AE03B9EC3-L004750](../../agents/web_agent.py#L4750) | 4750 | `"        llm_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L004751](../../agents/web_agent.py#L4751) | 4751 | `"        generation_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L004752](../../agents/web_agent.py#L4752) | 4752 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L004753](../../agents/web_agent.py#L4753) | 4753 | `"            answer = self._generate("` | — |
| [SRC-1AE03B9EC3-L004754](../../agents/web_agent.py#L4754) | 4754 | `"                question,"` | — |
| [SRC-1AE03B9EC3-L004755](../../agents/web_agent.py#L4755) | 4755 | `"                clean_history,"` | — |
| [SRC-1AE03B9EC3-L004756](../../agents/web_agent.py#L4756) | 4756 | `"                sources,"` | — |
| [SRC-1AE03B9EC3-L004757](../../agents/web_agent.py#L4757) | 4757 | `"                search_warning,"` | — |
| [SRC-1AE03B9EC3-L004758](../../agents/web_agent.py#L4758) | 4758 | `"                research_plan=plan,"` | — |
| [SRC-1AE03B9EC3-L004759](../../agents/web_agent.py#L4759) | 4759 | `"                search_report=report,"` | — |
| [SRC-1AE03B9EC3-L004760](../../agents/web_agent.py#L4760) | 4760 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004761](../../agents/web_agent.py#L4761) | 4761 | `"            used_llm = True"` | — |
| [SRC-1AE03B9EC3-L004762](../../agents/web_agent.py#L4762) | 4762 | `"            if self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L004763](../../agents/web_agent.py#L4763) | 4763 | `"                existing_urls = {item.get(\"url\") for item in sources}"` | — |
| [SRC-1AE03B9EC3-L004764](../../agents/web_agent.py#L4764) | 4764 | `"                relevance_queries = []"` | — |
| [SRC-1AE03B9EC3-L004765](../../agents/web_agent.py#L4765) | 4765 | `"                planned_queries = plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L004766](../../agents/web_agent.py#L4766) | 4766 | `"                if not isinstance(planned_queries, list):"` | — |
| [SRC-1AE03B9EC3-L004767](../../agents/web_agent.py#L4767) | 4767 | `"                    planned_queries = []"` | — |
| [SRC-1AE03B9EC3-L004768](../../agents/web_agent.py#L4768) | 4768 | `"                for candidate_query in [question, *planned_queries]:"` | — |
| [SRC-1AE03B9EC3-L004769](../../agents/web_agent.py#L4769) | 4769 | `"                    if not isinstance(candidate_query, str):"` | — |
| [SRC-1AE03B9EC3-L004770](../../agents/web_agent.py#L4770) | 4770 | `"                        continue"` | — |
| [SRC-1AE03B9EC3-L004771](../../agents/web_agent.py#L4771) | 4771 | `"                    compacted_query = compact_search_query(candidate_query)"` | — |
| [SRC-1AE03B9EC3-L004772](../../agents/web_agent.py#L4772) | 4772 | `"                    if compacted_query and compacted_query not in relevance_queries:"` | — |
| [SRC-1AE03B9EC3-L004773](../../agents/web_agent.py#L4773) | 4773 | `"                        relevance_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L004774](../../agents/web_agent.py#L4774) | 4774 | `"                for item in self.server_search_sources:"` | — |
| [SRC-1AE03B9EC3-L004775](../../agents/web_agent.py#L4775) | 4775 | `"                    source_text = \" \".join(("` | — |
| [SRC-1AE03B9EC3-L004776](../../agents/web_agent.py#L4776) | 4776 | `"                        item.get(\"title\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004777](../../agents/web_agent.py#L4777) | 4777 | `"                        item.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004778](../../agents/web_agent.py#L4778) | 4778 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L004779](../../agents/web_agent.py#L4779) | 4779 | `"                    if ("` | — |
| [SRC-1AE03B9EC3-L004780](../../agents/web_agent.py#L4780) | 4780 | `"                        relevance_queries"` | — |
| [SRC-1AE03B9EC3-L004781](../../agents/web_agent.py#L4781) | 4781 | `"                        and item[\"url\"] not in existing_urls"` | — |
| [SRC-1AE03B9EC3-L004782](../../agents/web_agent.py#L4782) | 4782 | `"                        and not _blocked_source_url(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L004783](../../agents/web_agent.py#L4783) | 4783 | `"                        and any("` | — |
| [SRC-1AE03B9EC3-L004784](../../agents/web_agent.py#L4784) | 4784 | `"                            _relevance_ratio(candidate_query, source_text) >= 0.20"` | — |
| [SRC-1AE03B9EC3-L004785](../../agents/web_agent.py#L4785) | 4785 | `"                            for candidate_query in relevance_queries"` | — |
| [SRC-1AE03B9EC3-L004786](../../agents/web_agent.py#L4786) | 4786 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004787](../../agents/web_agent.py#L4787) | 4787 | `"                    ):"` | — |
| [SRC-1AE03B9EC3-L004788](../../agents/web_agent.py#L4788) | 4788 | `"                        sources.append(item)"` | — |
| [SRC-1AE03B9EC3-L004789](../../agents/web_agent.py#L4789) | 4789 | `"                        existing_urls.add(item[\"url\"])"` | — |
| [SRC-1AE03B9EC3-L004790](../../agents/web_agent.py#L4790) | 4790 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004791](../../agents/web_agent.py#L4791) | 4791 | `"                provider_counts = dict(report.get(\"provider_counts\", {}))"` | — |
| [SRC-1AE03B9EC3-L004792](../../agents/web_agent.py#L4792) | 4792 | `"                provider_counts[\"openrouter_web_search\"] = len(self.server_search_sources)"` | — |
| [SRC-1AE03B9EC3-L004793](../../agents/web_agent.py#L4793) | 4793 | `"                report[\"provider_counts\"] = provider_counts"` | — |
| [SRC-1AE03B9EC3-L004794](../../agents/web_agent.py#L4794) | 4794 | `"                providers_used = list(report.get(\"providers_used\", []))"` | — |
| [SRC-1AE03B9EC3-L004795](../../agents/web_agent.py#L4795) | 4795 | `"                if \"openrouter_web_search\" not in providers_used:"` | — |
| [SRC-1AE03B9EC3-L004796](../../agents/web_agent.py#L4796) | 4796 | `"                    providers_used.append(\"openrouter_web_search\")"` | — |
| [SRC-1AE03B9EC3-L004797](../../agents/web_agent.py#L4797) | 4797 | `"                report[\"providers_used\"] = providers_used"` | — |
| [SRC-1AE03B9EC3-L004798](../../agents/web_agent.py#L4798) | 4798 | `"                report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L004799](../../agents/web_agent.py#L4799) | 4799 | `"                    sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L004800](../../agents/web_agent.py#L4800) | 4800 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004801](../../agents/web_agent.py#L4801) | 4801 | `"        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L004802](../../agents/web_agent.py#L4802) | 4802 | `"            llm_warning = str(exc)"` | — |
| [SRC-1AE03B9EC3-L004803](../../agents/web_agent.py#L4803) | 4803 | `"            generation_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L004804](../../agents/web_agent.py#L4804) | 4804 | `"            if generation_budget_exhausted:"` | — |
| [SRC-1AE03B9EC3-L004805](../../agents/web_agent.py#L4805) | 4805 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004806](../../agents/web_agent.py#L4806) | 4806 | `"                    \"استُنفدت ميزانية محاولات النماذج قبل اكتمال الإجابة التحليلية. \""` | — |
| [SRC-1AE03B9EC3-L004807](../../agents/web_agent.py#L4807) | 4807 | `"                    \"أعرض مقتطفات المصادر المتاحة فقط، ولا أعتبر المهمة مكتملة.\""` | — |
| [SRC-1AE03B9EC3-L004808](../../agents/web_agent.py#L4808) | 4808 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004809](../../agents/web_agent.py#L4809) | 4809 | `"            elif not self.api_key:"` | — |
| [SRC-1AE03B9EC3-L004810](../../agents/web_agent.py#L4810) | 4810 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004811](../../agents/web_agent.py#L4811) | 4811 | `"                    \"تم البحث، لكن الفهم التوليدي غير مفعّل بعد. اضبط OPENROUTER_API_KEY \""` | — |
| [SRC-1AE03B9EC3-L004812](../../agents/web_agent.py#L4812) | 4812 | `"                    \"في Termux لتفعيل تخطيط البحث والإجابة باللغة الطبيعية.\""` | — |
| [SRC-1AE03B9EC3-L004813](../../agents/web_agent.py#L4813) | 4813 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004814](../../agents/web_agent.py#L4814) | 4814 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004815](../../agents/web_agent.py#L4815) | 4815 | `"                reason = ("` | — |
| [SRC-1AE03B9EC3-L004816](../../agents/web_agent.py#L4816) | 4816 | `"                    \"اكتمل البحث، لكن تعذر توليد إجابة تحليلية. أعرض لك مقتطفات المصادر \""` | — |
| [SRC-1AE03B9EC3-L004817](../../agents/web_agent.py#L4817) | 4817 | `"                    \"المتاحة بدلًا من اختلاق إجابة.\""` | — |
| [SRC-1AE03B9EC3-L004818](../../agents/web_agent.py#L4818) | 4818 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004819](../../agents/web_agent.py#L4819) | 4819 | `"            answer = _fallback_answer(sources, reason)"` | — |
| [SRC-1AE03B9EC3-L004820](../../agents/web_agent.py#L4820) | 4820 | `""` | — |
| [SRC-1AE03B9EC3-L004821](../../agents/web_agent.py#L4821) | 4821 | `"        coverage_targets = self._question_coverage_targets(question)"` | — |
| [SRC-1AE03B9EC3-L004822](../../agents/web_agent.py#L4822) | 4822 | `"        coverage_repair_status = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L004823](../../agents/web_agent.py#L4823) | 4823 | `"        coverage_repair_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L004824](../../agents/web_agent.py#L4824) | 4824 | `"        review_status = \"not_run\""` | — |
| [SRC-1AE03B9EC3-L004825](../../agents/web_agent.py#L4825) | 4825 | `"        review_warning: str \| None = None"` | — |
| [SRC-1AE03B9EC3-L004826](../../agents/web_agent.py#L4826) | 4826 | `"        review_budget_exhausted = False"` | — |
| [SRC-1AE03B9EC3-L004827](../../agents/web_agent.py#L4827) | 4827 | `"        if used_llm and sources:"` | — |
| [SRC-1AE03B9EC3-L004828](../../agents/web_agent.py#L4828) | 4828 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L004829](../../agents/web_agent.py#L4829) | 4829 | `"                answer = self._review_answer(question, answer, sources[:MAX_LLM_CITED_SOURCES])"` | — |
| [SRC-1AE03B9EC3-L004830](../../agents/web_agent.py#L4830) | 4830 | `"                review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L004831](../../agents/web_agent.py#L4831) | 4831 | `"            except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L004832](../../agents/web_agent.py#L4832) | 4832 | `"                review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L004833](../../agents/web_agent.py#L4833) | 4833 | `"                review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L004834](../../agents/web_agent.py#L4834) | 4834 | `"                review_warning = ("` | — |
| [SRC-1AE03B9EC3-L004835](../../agents/web_agent.py#L4835) | 4835 | `"                    \"استُنفدت ميزانية النماذج قبل اكتمال تدقيق الإجابة؛ لذلك لن أعرض المسودة \""` | — |
| [SRC-1AE03B9EC3-L004836](../../agents/web_agent.py#L4836) | 4836 | `"                    \"بوصفها إجابة مكتملة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد عليها.\""` | — |
| [SRC-1AE03B9EC3-L004837](../../agents/web_agent.py#L4837) | 4837 | `"                    if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L004838](../../agents/web_agent.py#L4838) | 4838 | `"                    else"` | — |
| [SRC-1AE03B9EC3-L004839](../../agents/web_agent.py#L4839) | 4839 | `"                    \"تعذر تدقيق الادعاءات مقابل نصوص المصادر؛ لذلك لن أتعامل مع المسودة \""` | — |
| [SRC-1AE03B9EC3-L004840](../../agents/web_agent.py#L4840) | 4840 | `"                    \"كإجابة مؤكدة. أرفقت مقتطفات المصادر المتاحة بدل الاعتماد على المسودة.\""` | — |
| [SRC-1AE03B9EC3-L004841](../../agents/web_agent.py#L4841) | 4841 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004842](../../agents/web_agent.py#L4842) | 4842 | `"                answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L004843](../../agents/web_agent.py#L4843) | 4843 | `"        if ("` | — |
| [SRC-1AE03B9EC3-L004844](../../agents/web_agent.py#L4844) | 4844 | `"            coverage_targets"` | — |
| [SRC-1AE03B9EC3-L004845](../../agents/web_agent.py#L4845) | 4845 | `"            and review_status == \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L004846](../../agents/web_agent.py#L4846) | 4846 | `"            and sources"` | — |
| [SRC-1AE03B9EC3-L004847](../../agents/web_agent.py#L4847) | 4847 | `"            and self.api_key"` | — |
| [SRC-1AE03B9EC3-L004848](../../agents/web_agent.py#L4848) | 4848 | `"        ):"` | — |
| [SRC-1AE03B9EC3-L004849](../../agents/web_agent.py#L4849) | 4849 | `"            initial_integrity = audit_answer_integrity(question, answer, sources, coverage_targets)"` | — |
| [SRC-1AE03B9EC3-L004850](../../agents/web_agent.py#L4850) | 4850 | `"            missing_targets = ["` | — |
| [SRC-1AE03B9EC3-L004851](../../agents/web_agent.py#L4851) | 4851 | `"                item[\"target\"] for item in initial_integrity[\"target_coverage\"]"` | — |
| [SRC-1AE03B9EC3-L004852](../../agents/web_agent.py#L4852) | 4852 | `"                if item[\"status\"] == \"possibly_missing\""` | — |
| [SRC-1AE03B9EC3-L004853](../../agents/web_agent.py#L4853) | 4853 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L004854](../../agents/web_agent.py#L4854) | 4854 | `"            if not missing_targets:"` | — |
| [SRC-1AE03B9EC3-L004855](../../agents/web_agent.py#L4855) | 4855 | `"                coverage_repair_status = \"not_needed_lexical_signals_found\""` | — |
| [SRC-1AE03B9EC3-L004856](../../agents/web_agent.py#L4856) | 4856 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004857](../../agents/web_agent.py#L4857) | 4857 | `"                coverage_repair_status = \"attempted\""` | — |
| [SRC-1AE03B9EC3-L004858](../../agents/web_agent.py#L4858) | 4858 | `"                try:"` | — |
| [SRC-1AE03B9EC3-L004859](../../agents/web_agent.py#L4859) | 4859 | `"                    repaired_answer = self._repair_answer_coverage("` | — |
| [SRC-1AE03B9EC3-L004860](../../agents/web_agent.py#L4860) | 4860 | `"                        question, answer, sources, missing_targets"` | — |
| [SRC-1AE03B9EC3-L004861](../../agents/web_agent.py#L4861) | 4861 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004862](../../agents/web_agent.py#L4862) | 4862 | `"                    if repaired_answer.strip() != answer.strip():"` | — |
| [SRC-1AE03B9EC3-L004863](../../agents/web_agent.py#L4863) | 4863 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L004864](../../agents/web_agent.py#L4864) | 4864 | `"                            reaudit_answer = self._review_answer("` | — |
| [SRC-1AE03B9EC3-L004865](../../agents/web_agent.py#L4865) | 4865 | `"                                question,"` | — |
| [SRC-1AE03B9EC3-L004866](../../agents/web_agent.py#L4866) | 4866 | `"                                repaired_answer,"` | — |
| [SRC-1AE03B9EC3-L004867](../../agents/web_agent.py#L4867) | 4867 | `"                                sources[:MAX_LLM_CITED_SOURCES],"` | — |
| [SRC-1AE03B9EC3-L004868](../../agents/web_agent.py#L4868) | 4868 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L004869](../../agents/web_agent.py#L4869) | 4869 | `"                            answer = reaudit_answer"` | — |
| [SRC-1AE03B9EC3-L004870](../../agents/web_agent.py#L4870) | 4870 | `"                            coverage_repair_status = \"revised_and_reaudited\""` | — |
| [SRC-1AE03B9EC3-L004871](../../agents/web_agent.py#L4871) | 4871 | `"                            review_status = \"model_claim_audit_completed\""` | — |
| [SRC-1AE03B9EC3-L004872](../../agents/web_agent.py#L4872) | 4872 | `"                        except (RuntimeError, AgentDependencyError, RequestBudgetExceeded) as exc:"` | — |
| [SRC-1AE03B9EC3-L004873](../../agents/web_agent.py#L4873) | 4873 | `"                            review_status = \"model_claim_audit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L004874](../../agents/web_agent.py#L4874) | 4874 | `"                            review_budget_exhausted = isinstance(exc, RequestBudgetExceeded)"` | — |
| [SRC-1AE03B9EC3-L004875](../../agents/web_agent.py#L4875) | 4875 | `"                            coverage_repair_status = ("` | — |
| [SRC-1AE03B9EC3-L004876](../../agents/web_agent.py#L4876) | 4876 | `"                                \"reaudit_budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L004877](../../agents/web_agent.py#L4877) | 4877 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L004878](../../agents/web_agent.py#L4878) | 4878 | `"                                else \"reaudit_unavailable\""` | — |
| [SRC-1AE03B9EC3-L004879](../../agents/web_agent.py#L4879) | 4879 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L004880](../../agents/web_agent.py#L4880) | 4880 | `"                            review_warning = ("` | — |
| [SRC-1AE03B9EC3-L004881](../../agents/web_agent.py#L4881) | 4881 | `"                                \"استُنفدت ميزانية النماذج قبل إعادة تدقيق الإجابة المعدلة؛ \""` | — |
| [SRC-1AE03B9EC3-L004882](../../agents/web_agent.py#L4882) | 4882 | `"                                \"لذلك لن أعرض النص المعدل بوصفه إجابة مكتملة، وأعرض مقتطفات المصادر بدلًا منه.\""` | — |
| [SRC-1AE03B9EC3-L004883](../../agents/web_agent.py#L4883) | 4883 | `"                                if review_budget_exhausted"` | — |
| [SRC-1AE03B9EC3-L004884](../../agents/web_agent.py#L4884) | 4884 | `"                                else"` | — |
| [SRC-1AE03B9EC3-L004885](../../agents/web_agent.py#L4885) | 4885 | `"                                \"تعذرت إعادة تدقيق الإجابة المعدلة مقابل الأدلة؛ لذلك لن أعرضها بوصفها إجابة مكتملة، \""` | — |
| [SRC-1AE03B9EC3-L004886](../../agents/web_agent.py#L4886) | 4886 | `"                                \"وأعرض مقتطفات المصادر بدلًا منها.\""` | — |
| [SRC-1AE03B9EC3-L004887](../../agents/web_agent.py#L4887) | 4887 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L004888](../../agents/web_agent.py#L4888) | 4888 | `"                            answer = _fallback_answer(sources, review_warning)"` | — |
| [SRC-1AE03B9EC3-L004889](../../agents/web_agent.py#L4889) | 4889 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L004890](../../agents/web_agent.py#L4890) | 4890 | `"                        coverage_repair_status = \"no_change_gap_unresolved\""` | — |
| [SRC-1AE03B9EC3-L004891](../../agents/web_agent.py#L4891) | 4891 | `"                        coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L004892](../../agents/web_agent.py#L4892) | 4892 | `"                            \"رصد الفحص اللفظي محورًا قد يكون ناقصًا، لكن محاولة الإصلاح لم تغيّر الإجابة؛ \""` | — |
| [SRC-1AE03B9EC3-L004893](../../agents/web_agent.py#L4893) | 4893 | `"                            \"تحقق من تغطية هذا المحور يدويًا.\""` | — |
| [SRC-1AE03B9EC3-L004894](../../agents/web_agent.py#L4894) | 4894 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004895](../../agents/web_agent.py#L4895) | 4895 | `"                except RequestBudgetExceeded:"` | — |
| [SRC-1AE03B9EC3-L004896](../../agents/web_agent.py#L4896) | 4896 | `"                    coverage_repair_status = \"budget_exhausted\""` | — |
| [SRC-1AE03B9EC3-L004897](../../agents/web_agent.py#L4897) | 4897 | `"                    coverage_repair_warning = ("` | — |
| [SRC-1AE03B9EC3-L004898](../../agents/web_agent.py#L4898) | 4898 | `"                        \"استُنفدت ميزانية النماذج قبل محاولة إصلاح محور قد يكون ناقصًا؛ \""` | — |
| [SRC-1AE03B9EC3-L004899](../../agents/web_agent.py#L4899) | 4899 | `"                        \"لا تعتبر التغطية مكتملة دون مراجعة المحور المذكور.\""` | — |
| [SRC-1AE03B9EC3-L004900](../../agents/web_agent.py#L4900) | 4900 | `"                    )"` | — |
