# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **007**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L003073 إلى SRC-1AE03B9EC3-L003872
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L003073](../../agents/web_agent.py#L3073) | 3073 | `"                    \"note\": _clean_text(str(exc), 400),"` | — |
| [SRC-1AE03B9EC3-L003074](../../agents/web_agent.py#L3074) | 3074 | `"                }"` | — |
| [SRC-1AE03B9EC3-L003075](../../agents/web_agent.py#L3075) | 3075 | `""` | — |
| [SRC-1AE03B9EC3-L003076](../../agents/web_agent.py#L3076) | 3076 | `"        if not test_social:"` | — |
| [SRC-1AE03B9EC3-L003077](../../agents/web_agent.py#L3077) | 3077 | `"            report[\"checks\"][\"social_search\"] = {"` | — |
| [SRC-1AE03B9EC3-L003078](../../agents/web_agent.py#L3078) | 3078 | `"                \"status\": \"skipped\","` | — |
| [SRC-1AE03B9EC3-L003079](../../agents/web_agent.py#L3079) | 3079 | `"                \"note\": \"Social-source probes were not requested.\","` | — |
| [SRC-1AE03B9EC3-L003080](../../agents/web_agent.py#L3080) | 3080 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003081](../../agents/web_agent.py#L3081) | 3081 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L003082](../../agents/web_agent.py#L3082) | 3082 | `"            configured_platforms = [\"reddit\", \"bluesky\"]"` | — |
| [SRC-1AE03B9EC3-L003083](../../agents/web_agent.py#L3083) | 3083 | `"            optional_connectors = {"` | — |
| [SRC-1AE03B9EC3-L003084](../../agents/web_agent.py#L3084) | 3084 | `"                \"facebook\": bool("` | — |
| [SRC-1AE03B9EC3-L003085](../../agents/web_agent.py#L3085) | 3085 | `"                    os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003086](../../agents/web_agent.py#L3086) | 3086 | `"                    and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003087](../../agents/web_agent.py#L3087) | 3087 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L003088](../../agents/web_agent.py#L3088) | 3088 | `"                \"instagram\": bool("` | — |
| [SRC-1AE03B9EC3-L003089](../../agents/web_agent.py#L3089) | 3089 | `"                    os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003090](../../agents/web_agent.py#L3090) | 3090 | `"                    and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003091](../../agents/web_agent.py#L3091) | 3091 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L003092](../../agents/web_agent.py#L3092) | 3092 | `"                \"x\": bool(os.getenv(\"X_BEARER_TOKEN\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L003093](../../agents/web_agent.py#L3093) | 3093 | `"                \"youtube\": bool(os.getenv(\"YOUTUBE_API_KEY\", \"\").strip()),"` | — |
| [SRC-1AE03B9EC3-L003094](../../agents/web_agent.py#L3094) | 3094 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003095](../../agents/web_agent.py#L3095) | 3095 | `"            configured_platforms.extend("` | — |
| [SRC-1AE03B9EC3-L003096](../../agents/web_agent.py#L3096) | 3096 | `"                platform"` | — |
| [SRC-1AE03B9EC3-L003097](../../agents/web_agent.py#L3097) | 3097 | `"                for platform, is_configured in optional_connectors.items()"` | — |
| [SRC-1AE03B9EC3-L003098](../../agents/web_agent.py#L3098) | 3098 | `"                if is_configured"` | — |
| [SRC-1AE03B9EC3-L003099](../../agents/web_agent.py#L3099) | 3099 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003100](../../agents/web_agent.py#L3100) | 3100 | `"            try:"` | — |
| [SRC-1AE03B9EC3-L003101](../../agents/web_agent.py#L3101) | 3101 | `"                social_results, social_warnings = self._search_social("` | — |
| [SRC-1AE03B9EC3-L003102](../../agents/web_agent.py#L3102) | 3102 | `"                    \"Omarai public connectivity test\", configured_platforms"` | — |
| [SRC-1AE03B9EC3-L003103](../../agents/web_agent.py#L3103) | 3103 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003104](../../agents/web_agent.py#L3104) | 3104 | `"                providers: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L003105](../../agents/web_agent.py#L3105) | 3105 | `"                for source in social_results:"` | — |
| [SRC-1AE03B9EC3-L003106](../../agents/web_agent.py#L3106) | 3106 | `"                    provider = str(source.get(\"provider\") or \"unknown\")"` | — |
| [SRC-1AE03B9EC3-L003107](../../agents/web_agent.py#L3107) | 3107 | `"                    providers[provider] = providers.get(provider, 0) + 1"` | — |
| [SRC-1AE03B9EC3-L003108](../../agents/web_agent.py#L3108) | 3108 | `"                report[\"checks\"][\"social_search\"] = {"` | — |
| [SRC-1AE03B9EC3-L003109](../../agents/web_agent.py#L3109) | 3109 | `"                    \"status\": \"passed\" if social_results else \"degraded\","` | — |
| [SRC-1AE03B9EC3-L003110](../../agents/web_agent.py#L3110) | 3110 | `"                    \"platforms_tested\": configured_platforms,"` | — |
| [SRC-1AE03B9EC3-L003111](../../agents/web_agent.py#L3111) | 3111 | `"                    \"result_count\": len(social_results),"` | — |
| [SRC-1AE03B9EC3-L003112](../../agents/web_agent.py#L3112) | 3112 | `"                    \"provider_counts\": providers,"` | — |
| [SRC-1AE03B9EC3-L003113](../../agents/web_agent.py#L3113) | 3113 | `"                    \"warnings\": [_clean_text(item, 300) for item in social_warnings[:8]],"` | — |
| [SRC-1AE03B9EC3-L003114](../../agents/web_agent.py#L3114) | 3114 | `"                    \"note\": ("` | — |
| [SRC-1AE03B9EC3-L003115](../../agents/web_agent.py#L3115) | 3115 | `"                        \"Public-source request(s) returned results.\""` | — |
| [SRC-1AE03B9EC3-L003116](../../agents/web_agent.py#L3116) | 3116 | `"                        if social_results"` | — |
| [SRC-1AE03B9EC3-L003117](../../agents/web_agent.py#L3117) | 3117 | `"                        else \"No parseable public social results were returned. This does not establish that the platform is offline.\""` | — |
| [SRC-1AE03B9EC3-L003118](../../agents/web_agent.py#L3118) | 3118 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L003119](../../agents/web_agent.py#L3119) | 3119 | `"                }"` | — |
| [SRC-1AE03B9EC3-L003120](../../agents/web_agent.py#L3120) | 3120 | `"            except (RuntimeError, AgentDependencyError, ValueError, OSError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003121](../../agents/web_agent.py#L3121) | 3121 | `"                report[\"checks\"][\"social_search\"] = {"` | — |
| [SRC-1AE03B9EC3-L003122](../../agents/web_agent.py#L3122) | 3122 | `"                    \"status\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L003123](../../agents/web_agent.py#L3123) | 3123 | `"                    \"platforms_tested\": configured_platforms,"` | — |
| [SRC-1AE03B9EC3-L003124](../../agents/web_agent.py#L3124) | 3124 | `"                    \"result_count\": 0,"` | — |
| [SRC-1AE03B9EC3-L003125](../../agents/web_agent.py#L3125) | 3125 | `"                    \"note\": _clean_text(str(exc), 400),"` | — |
| [SRC-1AE03B9EC3-L003126](../../agents/web_agent.py#L3126) | 3126 | `"                }"` | — |
| [SRC-1AE03B9EC3-L003127](../../agents/web_agent.py#L3127) | 3127 | `""` | — |
| [SRC-1AE03B9EC3-L003128](../../agents/web_agent.py#L3128) | 3128 | `"        report[\"model_usage\"] = list(self.model_usage)"` | — |
| [SRC-1AE03B9EC3-L003129](../../agents/web_agent.py#L3129) | 3129 | `"        report[\"elapsed_ms\"] = round((time.monotonic() - started) * 1000)"` | — |
| [SRC-1AE03B9EC3-L003130](../../agents/web_agent.py#L3130) | 3130 | `"        statuses = [check.get(\"status\") for check in report[\"checks\"].values()]"` | — |
| [SRC-1AE03B9EC3-L003131](../../agents/web_agent.py#L3131) | 3131 | `"        report[\"overall_status\"] = ("` | — |
| [SRC-1AE03B9EC3-L003132](../../agents/web_agent.py#L3132) | 3132 | `"            \"passed\""` | — |
| [SRC-1AE03B9EC3-L003133](../../agents/web_agent.py#L3133) | 3133 | `"            if all(status in {\"passed\", \"skipped\"} for status in statuses)"` | — |
| [SRC-1AE03B9EC3-L003134](../../agents/web_agent.py#L3134) | 3134 | `"            else \"degraded\""` | — |
| [SRC-1AE03B9EC3-L003135](../../agents/web_agent.py#L3135) | 3135 | `"            if any(status in {\"passed\", \"degraded\"} for status in statuses)"` | — |
| [SRC-1AE03B9EC3-L003136](../../agents/web_agent.py#L3136) | 3136 | `"            else \"failed\""` | — |
| [SRC-1AE03B9EC3-L003137](../../agents/web_agent.py#L3137) | 3137 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003138](../../agents/web_agent.py#L3138) | 3138 | `"        return report"` | — |
| [SRC-1AE03B9EC3-L003139](../../agents/web_agent.py#L3139) | 3139 | `""` | — |
| [SRC-1AE03B9EC3-L003140](../../agents/web_agent.py#L3140) | 3140 | `"    def answer("` | — |
| [SRC-1AE03B9EC3-L003141](../../agents/web_agent.py#L3141) | 3141 | `"        self, question: str, history: Any = None, mode: str = \"auto\""` | — |
| [SRC-1AE03B9EC3-L003142](../../agents/web_agent.py#L3142) | 3142 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L003143](../../agents/web_agent.py#L3143) | 3143 | `"        \"\"\"Run one answer with an isolated, observable resource budget.\"\"\""` | — |
| [SRC-1AE03B9EC3-L003144](../../agents/web_agent.py#L3144) | 3144 | `"        previous_budget = getattr(self, \"_request_budget\", None)"` | — |
| [SRC-1AE03B9EC3-L003145](../../agents/web_agent.py#L3145) | 3145 | `"        self.generation_diagnostics = []"` | — |
| [SRC-1AE03B9EC3-L003146](../../agents/web_agent.py#L3146) | 3146 | `"        budget = RequestBudget.from_environment()"` | — |
| [SRC-1AE03B9EC3-L003147](../../agents/web_agent.py#L3147) | 3147 | `"        self._request_budget = budget"` | — |
| [SRC-1AE03B9EC3-L003148](../../agents/web_agent.py#L3148) | 3148 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L003149](../../agents/web_agent.py#L3149) | 3149 | `"            result = self._answer_with_budget(question, history, mode)"` | — |
| [SRC-1AE03B9EC3-L003150](../../agents/web_agent.py#L3150) | 3150 | `"        except RequestBudgetExceeded as exc:"` | — |
| [SRC-1AE03B9EC3-L003151](../../agents/web_agent.py#L3151) | 3151 | `"            safe_question = ("` | — |
| [SRC-1AE03B9EC3-L003152](../../agents/web_agent.py#L3152) | 3152 | `"                question.strip()[:MAX_QUESTION_CHARS]"` | — |
| [SRC-1AE03B9EC3-L003153](../../agents/web_agent.py#L3153) | 3153 | `"                if isinstance(question, str)"` | — |
| [SRC-1AE03B9EC3-L003154](../../agents/web_agent.py#L3154) | 3154 | `"                else \"\""` | — |
| [SRC-1AE03B9EC3-L003155](../../agents/web_agent.py#L3155) | 3155 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003156](../../agents/web_agent.py#L3156) | 3156 | `"            budget_at_failure = budget.snapshot()"` | — |
| [SRC-1AE03B9EC3-L003157](../../agents/web_agent.py#L3157) | 3157 | `"            search_attempted = budget_at_failure[\"counts\"][\"search_calls\"] > 0"` | — |
| [SRC-1AE03B9EC3-L003158](../../agents/web_agent.py#L3158) | 3158 | `"            result = {"` | — |
| [SRC-1AE03B9EC3-L003159](../../agents/web_agent.py#L3159) | 3159 | `"                \"answer\": ("` | — |
| [SRC-1AE03B9EC3-L003160](../../agents/web_agent.py#L3160) | 3160 | `"                    \"توقفت العملية لأن ميزانية الوقت أو الموارد المحددة لهذا الطلب \""` | — |
| [SRC-1AE03B9EC3-L003161](../../agents/web_agent.py#L3161) | 3161 | `"                    \"قد استُنفدت. لم أتمكن من إكمال البحث ضمن الحدود الحالية؛ \""` | — |
| [SRC-1AE03B9EC3-L003162](../../agents/web_agent.py#L3162) | 3162 | `"                    \"لا تعتبر هذه النتيجة بحثًا مكتملًا.\""` | — |
| [SRC-1AE03B9EC3-L003163](../../agents/web_agent.py#L3163) | 3163 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L003164](../../agents/web_agent.py#L3164) | 3164 | `"                \"question\": safe_question,"` | — |
| [SRC-1AE03B9EC3-L003165](../../agents/web_agent.py#L3165) | 3165 | `"                \"search_query\": safe_question,"` | — |
| [SRC-1AE03B9EC3-L003166](../../agents/web_agent.py#L3166) | 3166 | `"                \"search_queries\": [],"` | — |
| [SRC-1AE03B9EC3-L003167](../../agents/web_agent.py#L3167) | 3167 | `"                \"search_report\": {"` | — |
| [SRC-1AE03B9EC3-L003168](../../agents/web_agent.py#L3168) | 3168 | `"                    \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L003169](../../agents/web_agent.py#L3169) | 3169 | `"                    \"search_outcome\": ("` | — |
| [SRC-1AE03B9EC3-L003170](../../agents/web_agent.py#L3170) | 3170 | `"                        \"unknown_after_budget_exhaustion\""` | — |
| [SRC-1AE03B9EC3-L003171](../../agents/web_agent.py#L3171) | 3171 | `"                        if search_attempted"` | — |
| [SRC-1AE03B9EC3-L003172](../../agents/web_agent.py#L3172) | 3172 | `"                        else \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L003173](../../agents/web_agent.py#L3173) | 3173 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L003174](../../agents/web_agent.py#L3174) | 3174 | `"                    \"insufficient_evidence\": True,"` | — |
| [SRC-1AE03B9EC3-L003175](../../agents/web_agent.py#L3175) | 3175 | `"                    \"budget_exhausted\": True,"` | — |
| [SRC-1AE03B9EC3-L003176](../../agents/web_agent.py#L3176) | 3176 | `"                    \"warnings\": [str(exc)],"` | — |
| [SRC-1AE03B9EC3-L003177](../../agents/web_agent.py#L3177) | 3177 | `"                },"` | — |
| [SRC-1AE03B9EC3-L003178](../../agents/web_agent.py#L3178) | 3178 | `"                \"sources\": [],"` | — |
| [SRC-1AE03B9EC3-L003179](../../agents/web_agent.py#L3179) | 3179 | `"                \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L003180](../../agents/web_agent.py#L3180) | 3180 | `"                \"citation_validation\": {\"status\": \"not_checked\"},"` | — |
| [SRC-1AE03B9EC3-L003181](../../agents/web_agent.py#L3181) | 3181 | `"                \"answer_coverage\": {},"` | — |
| [SRC-1AE03B9EC3-L003182](../../agents/web_agent.py#L3182) | 3182 | `"                \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L003183](../../agents/web_agent.py#L3183) | 3183 | `"                \"used_web_search\": False,"` | — |
| [SRC-1AE03B9EC3-L003184](../../agents/web_agent.py#L3184) | 3184 | `"                \"search_attempted\": search_attempted,"` | — |
| [SRC-1AE03B9EC3-L003185](../../agents/web_agent.py#L3185) | 3185 | `"                \"used_social_search\": False,"` | — |
| [SRC-1AE03B9EC3-L003186](../../agents/web_agent.py#L3186) | 3186 | `"                \"warnings\": [str(exc)],"` | — |
| [SRC-1AE03B9EC3-L003187](../../agents/web_agent.py#L3187) | 3187 | `"                \"kind\": \"web_fallback\","` | — |
| [SRC-1AE03B9EC3-L003188](../../agents/web_agent.py#L3188) | 3188 | `"                \"final_answer_status\": \"budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L003189](../../agents/web_agent.py#L3189) | 3189 | `"                \"intent_route\": \"BUDGET_EXHAUSTED\","` | — |
| [SRC-1AE03B9EC3-L003190](../../agents/web_agent.py#L3190) | 3190 | `"                \"intent_route_reason\": \"request_budget_exhausted\","` | — |
| [SRC-1AE03B9EC3-L003191](../../agents/web_agent.py#L3191) | 3191 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003192](../../agents/web_agent.py#L3192) | 3192 | `"        finally:"` | — |
| [SRC-1AE03B9EC3-L003193](../../agents/web_agent.py#L3193) | 3193 | `"            budget_summary = budget.snapshot()"` | — |
| [SRC-1AE03B9EC3-L003194](../../agents/web_agent.py#L3194) | 3194 | `"            self._request_budget = previous_budget"` | — |
| [SRC-1AE03B9EC3-L003195](../../agents/web_agent.py#L3195) | 3195 | `""` | — |
| [SRC-1AE03B9EC3-L003196](../../agents/web_agent.py#L3196) | 3196 | `"        result[\"request_budget\"] = budget_summary"` | — |
| [SRC-1AE03B9EC3-L003197](../../agents/web_agent.py#L3197) | 3197 | `"        result[\"generation_diagnostics\"] = list(self.generation_diagnostics[-12:])"` | — |
| [SRC-1AE03B9EC3-L003198](../../agents/web_agent.py#L3198) | 3198 | `"        if \"final_answer_status\" not in result:"` | — |
| [SRC-1AE03B9EC3-L003199](../../agents/web_agent.py#L3199) | 3199 | `"            if result.get(\"kind\") in {\"capability_answer\", \"local_conversation\"}:"` | — |
| [SRC-1AE03B9EC3-L003200](../../agents/web_agent.py#L3200) | 3200 | `"                final_answer_status = \"local_response_no_generation\""` | — |
| [SRC-1AE03B9EC3-L003201](../../agents/web_agent.py#L3201) | 3201 | `"            elif result.get(\"kind\") == \"insufficient_evidence\":"` | — |
| [SRC-1AE03B9EC3-L003202](../../agents/web_agent.py#L3202) | 3202 | `"                final_answer_status = \"insufficient_evidence_no_generation\""` | — |
| [SRC-1AE03B9EC3-L003203](../../agents/web_agent.py#L3203) | 3203 | `"            elif result.get(\"used_language_model\") is True:"` | — |
| [SRC-1AE03B9EC3-L003204](../../agents/web_agent.py#L3204) | 3204 | `"                final_answer_status = \"model_answer_generated\""` | — |
| [SRC-1AE03B9EC3-L003205](../../agents/web_agent.py#L3205) | 3205 | `"            elif self.generation_diagnostics:"` | — |
| [SRC-1AE03B9EC3-L003206](../../agents/web_agent.py#L3206) | 3206 | `"                final_answer_status = ("` | — |
| [SRC-1AE03B9EC3-L003207](../../agents/web_agent.py#L3207) | 3207 | `"                    \"generation_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L003208](../../agents/web_agent.py#L3208) | 3208 | `"                    if result.get(\"sources\")"` | — |
| [SRC-1AE03B9EC3-L003209](../../agents/web_agent.py#L3209) | 3209 | `"                    else \"generation_failed\""` | — |
| [SRC-1AE03B9EC3-L003210](../../agents/web_agent.py#L3210) | 3210 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003211](../../agents/web_agent.py#L3211) | 3211 | `"            elif result.get(\"kind\") == \"clarification\":"` | — |
| [SRC-1AE03B9EC3-L003212](../../agents/web_agent.py#L3212) | 3212 | `"                final_answer_status = \"clarification_required\""` | — |
| [SRC-1AE03B9EC3-L003213](../../agents/web_agent.py#L3213) | 3213 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L003214](../../agents/web_agent.py#L3214) | 3214 | `"                final_answer_status = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L003215](../../agents/web_agent.py#L3215) | 3215 | `"            result[\"final_answer_status\"] = final_answer_status"` | — |
| [SRC-1AE03B9EC3-L003216](../../agents/web_agent.py#L3216) | 3216 | `"        if isinstance(result.get(\"search_report\"), dict):"` | — |
| [SRC-1AE03B9EC3-L003217](../../agents/web_agent.py#L3217) | 3217 | `"            result[\"search_report\"][\"request_budget\"] = budget_summary"` | — |
| [SRC-1AE03B9EC3-L003218](../../agents/web_agent.py#L3218) | 3218 | `"        if budget_summary[\"deadline_exceeded\"]:"` | — |
| [SRC-1AE03B9EC3-L003219](../../agents/web_agent.py#L3219) | 3219 | `"            result.setdefault(\"warnings\", []).append("` | — |
| [SRC-1AE03B9EC3-L003220](../../agents/web_agent.py#L3220) | 3220 | `"                \"انتهت نافذة الوقت المحددة للطلب أو جرى تجاوزها قليلًا أثناء إنهاء اتصال جارٍ.\""` | — |
| [SRC-1AE03B9EC3-L003221](../../agents/web_agent.py#L3221) | 3221 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003222](../../agents/web_agent.py#L3222) | 3222 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L003223](../../agents/web_agent.py#L3223) | 3223 | `""` | — |
| [SRC-1AE03B9EC3-L003224](../../agents/web_agent.py#L3224) | 3224 | `"    def _answer_with_budget("` | — |
| [SRC-1AE03B9EC3-L003225](../../agents/web_agent.py#L3225) | 3225 | `"        self, question: str, history: Any = None, mode: str = \"auto\""` | — |
| [SRC-1AE03B9EC3-L003226](../../agents/web_agent.py#L3226) | 3226 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L003227](../../agents/web_agent.py#L3227) | 3227 | `"        if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-1AE03B9EC3-L003228](../../agents/web_agent.py#L3228) | 3228 | `"            raise ValueError(\"اكتب سؤالًا غير فارغ.\")"` | — |
| [SRC-1AE03B9EC3-L003229](../../agents/web_agent.py#L3229) | 3229 | `"        question = question.strip()"` | — |
| [SRC-1AE03B9EC3-L003230](../../agents/web_agent.py#L3230) | 3230 | `"        if len(question) > MAX_QUESTION_CHARS:"` | — |
| [SRC-1AE03B9EC3-L003231](../../agents/web_agent.py#L3231) | 3231 | `"            raise ValueError(f\"السؤال طويل جدًا؛ الحد الأقصى {MAX_QUESTION_CHARS} حرف.\")"` | — |
| [SRC-1AE03B9EC3-L003232](../../agents/web_agent.py#L3232) | 3232 | `"        clean_history = self._sanitize_history(history)"` | — |
| [SRC-1AE03B9EC3-L003233](../../agents/web_agent.py#L3233) | 3233 | `"        self._reset_deepseek_search_budget()"` | — |
| [SRC-1AE03B9EC3-L003234](../../agents/web_agent.py#L3234) | 3234 | `"        self.server_search_sources = []"` | — |
| [SRC-1AE03B9EC3-L003235](../../agents/web_agent.py#L3235) | 3235 | `"        self.model_usage = []"` | — |
| [SRC-1AE03B9EC3-L003236](../../agents/web_agent.py#L3236) | 3236 | `"        self.generation_diagnostics = []"` | — |
| [SRC-1AE03B9EC3-L003237](../../agents/web_agent.py#L3237) | 3237 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L003238](../../agents/web_agent.py#L3238) | 3238 | `"            self._provider_diagnostics = []"` | — |
| [SRC-1AE03B9EC3-L003239](../../agents/web_agent.py#L3239) | 3239 | `"        clean_mode = mode.strip().lower() if isinstance(mode, str) else \"auto\""` | — |
| [SRC-1AE03B9EC3-L003240](../../agents/web_agent.py#L3240) | 3240 | `"        if clean_mode not in {\"auto\", \"deep\", \"latest\", \"social\"}:"` | — |
| [SRC-1AE03B9EC3-L003241](../../agents/web_agent.py#L3241) | 3241 | `"            raise ValueError(\"نمط البحث غير مدعوم. اختر auto أو deep أو latest أو social.\")"` | — |
| [SRC-1AE03B9EC3-L003242](../../agents/web_agent.py#L3242) | 3242 | `"        current_search_status_question = self._is_current_search_status_question(question)"` | — |
| [SRC-1AE03B9EC3-L003243](../../agents/web_agent.py#L3243) | 3243 | `"        # Explicit UI modes control research tasks, but must not turn a status"` | — |
| [SRC-1AE03B9EC3-L003244](../../agents/web_agent.py#L3244) | 3244 | `"        # question about this answer into a new web-search request."` | — |
| [SRC-1AE03B9EC3-L003245](../../agents/web_agent.py#L3245) | 3245 | `"        routing_mode = \"auto\" if current_search_status_question else clean_mode"` | — |
| [SRC-1AE03B9EC3-L003246](../../agents/web_agent.py#L3246) | 3246 | `"        decision = route_intent("` | — |
| [SRC-1AE03B9EC3-L003247](../../agents/web_agent.py#L3247) | 3247 | `"            question,"` | — |
| [SRC-1AE03B9EC3-L003248](../../agents/web_agent.py#L3248) | 3248 | `"            clean_history,"` | — |
| [SRC-1AE03B9EC3-L003249](../../agents/web_agent.py#L3249) | 3249 | `"            routing_mode,"` | — |
| [SRC-1AE03B9EC3-L003250](../../agents/web_agent.py#L3250) | 3250 | `"            capability_question=self._is_self_question(question),"` | — |
| [SRC-1AE03B9EC3-L003251](../../agents/web_agent.py#L3251) | 3251 | `"            requires_web=self._requires_web_research(question, routing_mode),"` | — |
| [SRC-1AE03B9EC3-L003252](../../agents/web_agent.py#L3252) | 3252 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003253](../../agents/web_agent.py#L3253) | 3253 | `"        intent_route = str(decision[\"route\"])"` | — |
| [SRC-1AE03B9EC3-L003254](../../agents/web_agent.py#L3254) | 3254 | `"        intent_reason = str(decision[\"reason\"])"` | — |
| [SRC-1AE03B9EC3-L003255](../../agents/web_agent.py#L3255) | 3255 | `""` | — |
| [SRC-1AE03B9EC3-L003256](../../agents/web_agent.py#L3256) | 3256 | `"        if intent_route == \"LOCAL\":"` | — |
| [SRC-1AE03B9EC3-L003257](../../agents/web_agent.py#L3257) | 3257 | `"            if self._is_self_question(question):"` | — |
| [SRC-1AE03B9EC3-L003258](../../agents/web_agent.py#L3258) | 3258 | `"                local_result = self._self_description_answer(question)"` | — |
| [SRC-1AE03B9EC3-L003259](../../agents/web_agent.py#L3259) | 3259 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L003260](../../agents/web_agent.py#L3260) | 3260 | `"                local_result = self._local_answer_result("` | — |
| [SRC-1AE03B9EC3-L003261](../../agents/web_agent.py#L3261) | 3261 | `"                    question, self._local_conversation_reply(question), \"local_conversation\""` | — |
| [SRC-1AE03B9EC3-L003262](../../agents/web_agent.py#L3262) | 3262 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003263](../../agents/web_agent.py#L3263) | 3263 | `"            return self._annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L003264](../../agents/web_agent.py#L3264) | 3264 | `"                local_result, intent_route, intent_reason, clean_mode"` | — |
| [SRC-1AE03B9EC3-L003265](../../agents/web_agent.py#L3265) | 3265 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003266](../../agents/web_agent.py#L3266) | 3266 | `""` | — |
| [SRC-1AE03B9EC3-L003267](../../agents/web_agent.py#L3267) | 3267 | `"        if intent_route == \"CLARIFY\":"` | — |
| [SRC-1AE03B9EC3-L003268](../../agents/web_agent.py#L3268) | 3268 | `"            return self._clarification_result(question, clean_mode, decision)"` | — |
| [SRC-1AE03B9EC3-L003269](../../agents/web_agent.py#L3269) | 3269 | `""` | — |
| [SRC-1AE03B9EC3-L003270](../../agents/web_agent.py#L3270) | 3270 | `"        if intent_route == \"MODEL_ONLY\":"` | — |
| [SRC-1AE03B9EC3-L003271](../../agents/web_agent.py#L3271) | 3271 | `"            general_answer = self._answer_without_search(question, clean_history)"` | — |
| [SRC-1AE03B9EC3-L003272](../../agents/web_agent.py#L3272) | 3272 | `"            if general_answer is not None:"` | — |
| [SRC-1AE03B9EC3-L003273](../../agents/web_agent.py#L3273) | 3273 | `"                return self._annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L003274](../../agents/web_agent.py#L3274) | 3274 | `"                    general_answer, intent_route, intent_reason, clean_mode"` | — |
| [SRC-1AE03B9EC3-L003275](../../agents/web_agent.py#L3275) | 3275 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003276](../../agents/web_agent.py#L3276) | 3276 | `"            # Preserve the existing degraded-mode behavior when generation is unavailable:"` | — |
| [SRC-1AE03B9EC3-L003277](../../agents/web_agent.py#L3277) | 3277 | `"            # run the current web pipeline rather than fabricate a model-only answer."` | — |
| [SRC-1AE03B9EC3-L003278](../../agents/web_agent.py#L3278) | 3278 | `"            intent_route = \"WEB_SIMPLE\""` | — |
| [SRC-1AE03B9EC3-L003279](../../agents/web_agent.py#L3279) | 3279 | `"            intent_reason = \"model_unavailable_fallback_to_existing_web_research\""` | — |
| [SRC-1AE03B9EC3-L003280](../../agents/web_agent.py#L3280) | 3280 | `""` | — |
| [SRC-1AE03B9EC3-L003281](../../agents/web_agent.py#L3281) | 3281 | `"        plan = self._plan_search(question, clean_history)"` | — |
| [SRC-1AE03B9EC3-L003282](../../agents/web_agent.py#L3282) | 3282 | `"        plan[\"mode\"] = clean_mode"` | — |
| [SRC-1AE03B9EC3-L003283](../../agents/web_agent.py#L3283) | 3283 | `"        plan[\"intent_route\"] = intent_route"` | — |
| [SRC-1AE03B9EC3-L003284](../../agents/web_agent.py#L3284) | 3284 | `"        plan[\"intent_route_reason\"] = intent_reason"` | — |
| [SRC-1AE03B9EC3-L003285](../../agents/web_agent.py#L3285) | 3285 | `"        if clean_mode == \"auto\" and intent_route == \"WEB_DEEP\":"` | — |
| [SRC-1AE03B9EC3-L003286](../../agents/web_agent.py#L3286) | 3286 | `"            plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L003287](../../agents/web_agent.py#L3287) | 3287 | `"        if clean_mode == \"auto\":"` | — |
| [SRC-1AE03B9EC3-L003288](../../agents/web_agent.py#L3288) | 3288 | `"            normalized_question = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L003289](../../agents/web_agent.py#L3289) | 3289 | `"            deep_terms = ("` | — |
| [SRC-1AE03B9EC3-L003290](../../agents/web_agent.py#L3290) | 3290 | `"                \"بحث عميق\", \"بحث معمق\", \"بحث شامل\", \"بالتفصيل\", \"قارن\", \"مقارنة\","` | — |
| [SRC-1AE03B9EC3-L003291](../../agents/web_agent.py#L3291) | 3291 | `"                \"تحقق\", \"استقصاء\", \"deep research\", \"comprehensive\", \"in-depth\", \"compare\","` | — |
| [SRC-1AE03B9EC3-L003292](../../agents/web_agent.py#L3292) | 3292 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003293](../../agents/web_agent.py#L3293) | 3293 | `"            explicit_deep = intent_route == \"WEB_DEEP\" or any("` | — |
| [SRC-1AE03B9EC3-L003294](../../agents/web_agent.py#L3294) | 3294 | `"                term in normalized_question for term in deep_terms"` | — |
| [SRC-1AE03B9EC3-L003295](../../agents/web_agent.py#L3295) | 3295 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003296](../../agents/web_agent.py#L3296) | 3296 | `"            if not explicit_deep:"` | — |
| [SRC-1AE03B9EC3-L003297](../../agents/web_agent.py#L3297) | 3297 | `"                # The planner may overclassify short lookups as deep research. Preserve"` | — |
| [SRC-1AE03B9EC3-L003298](../../agents/web_agent.py#L3298) | 3298 | `"                # the user's actual intent first and cap routine searches to three queries."` | — |
| [SRC-1AE03B9EC3-L003299](../../agents/web_agent.py#L3299) | 3299 | `"                fallback_queries = fallback_plan(question, clean_history).get(\"queries\") or [question]"` | — |
| [SRC-1AE03B9EC3-L003300](../../agents/web_agent.py#L3300) | 3300 | `"                model_queries = plan.get(\"queries\") or []"` | — |
| [SRC-1AE03B9EC3-L003301](../../agents/web_agent.py#L3301) | 3301 | `"                if self._is_navigation_request(question):"` | — |
| [SRC-1AE03B9EC3-L003302](../../agents/web_agent.py#L3302) | 3302 | `"                    subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L003303](../../agents/web_agent.py#L3303) | 3303 | `"                        r\"^(?:ابحث\|بحث\|دور\|اعثر)\\s+(?:عن\|على)?\\s*\","` | — |
| [SRC-1AE03B9EC3-L003304](../../agents/web_agent.py#L3304) | 3304 | `"                        \"\","` | — |
| [SRC-1AE03B9EC3-L003305](../../agents/web_agent.py#L3305) | 3305 | `"                        str(fallback_queries[0]),"` | — |
| [SRC-1AE03B9EC3-L003306](../../agents/web_agent.py#L3306) | 3306 | `"                    ).strip() or question"` | — |
| [SRC-1AE03B9EC3-L003307](../../agents/web_agent.py#L3307) | 3307 | `"                    plan_queries = ["` | — |
| [SRC-1AE03B9EC3-L003308](../../agents/web_agent.py#L3308) | 3308 | `"                        subject,"` | — |
| [SRC-1AE03B9EC3-L003309](../../agents/web_agent.py#L3309) | 3309 | `"                        subject + \" الموقع الرسمي\","` | — |
| [SRC-1AE03B9EC3-L003310](../../agents/web_agent.py#L3310) | 3310 | `"                        subject + \" official website\","` | — |
| [SRC-1AE03B9EC3-L003311](../../agents/web_agent.py#L3311) | 3311 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L003312](../../agents/web_agent.py#L3312) | 3312 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L003313](../../agents/web_agent.py#L3313) | 3313 | `"                    plan_queries = [fallback_queries[0]] + model_queries"` | — |
| [SRC-1AE03B9EC3-L003314](../../agents/web_agent.py#L3314) | 3314 | `"                plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L003315](../../agents/web_agent.py#L3315) | 3315 | `"                    query.strip() for query in plan_queries if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L003316](../../agents/web_agent.py#L3316) | 3316 | `"                ))[:3]"` | — |
| [SRC-1AE03B9EC3-L003317](../../agents/web_agent.py#L3317) | 3317 | `"                plan[\"depth\"] = \"standard\""` | — |
| [SRC-1AE03B9EC3-L003318](../../agents/web_agent.py#L3318) | 3318 | `"        base_query = (plan.get(\"queries\") or [question])[0]"` | — |
| [SRC-1AE03B9EC3-L003319](../../agents/web_agent.py#L3319) | 3319 | `"        if clean_mode == \"auto\" and intent_route == \"WEB_DEEP\":"` | — |
| [SRC-1AE03B9EC3-L003320](../../agents/web_agent.py#L3320) | 3320 | `"            deep_candidates = ["` | — |
| [SRC-1AE03B9EC3-L003321](../../agents/web_agent.py#L3321) | 3321 | `"                f\"{base_query} official sources evidence\","` | — |
| [SRC-1AE03B9EC3-L003322](../../agents/web_agent.py#L3322) | 3322 | `"                f\"{base_query} risks limitations alternatives\","` | — |
| [SRC-1AE03B9EC3-L003323](../../agents/web_agent.py#L3323) | 3323 | `"                f\"{base_query} recent data reviews comparison\","` | — |
| [SRC-1AE03B9EC3-L003324](../../agents/web_agent.py#L3324) | 3324 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L003325](../../agents/web_agent.py#L3325) | 3325 | `"            plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L003326](../../agents/web_agent.py#L3326) | 3326 | `"                (plan.get(\"queries\") or [])[:5] + deep_candidates"` | — |
| [SRC-1AE03B9EC3-L003327](../../agents/web_agent.py#L3327) | 3327 | `"            ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L003328](../../agents/web_agent.py#L3328) | 3328 | `"            base_query = (plan.get(\"queries\") or [question])[0]"` | — |
| [SRC-1AE03B9EC3-L003329](../../agents/web_agent.py#L3329) | 3329 | `"        # Explicit user-selected modes are control inputs. They do not bypass source"` | — |
| [SRC-1AE03B9EC3-L003330](../../agents/web_agent.py#L3330) | 3330 | `"        # validation and never permit private-source access."` | — |
| [SRC-1AE03B9EC3-L003331](../../agents/web_agent.py#L3331) | 3331 | `"        if clean_mode == \"deep\":"` | — |
| [SRC-1AE03B9EC3-L003332](../../agents/web_agent.py#L3332) | 3332 | `"            plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L003333](../../agents/web_agent.py#L3333) | 3333 | `"            candidates = ["` | — |
| [SRC-1AE03B9EC3-L003334](../../agents/web_agent.py#L3334) | 3334 | `"                f\"{base_query} official sources data reports\","` | — |
| [SRC-1AE03B9EC3-L003335](../../agents/web_agent.py#L3335) | 3335 | `"                f\"{base_query} risks limitations alternatives\","` | — |
| [SRC-1AE03B9EC3-L003336](../../agents/web_agent.py#L3336) | 3336 | `"                f\"{base_query} case studies recent analysis\","` | — |
| [SRC-1AE03B9EC3-L003337](../../agents/web_agent.py#L3337) | 3337 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L003338](../../agents/web_agent.py#L3338) | 3338 | `"            # Keep query budget for evidence-gap searches if first-round coverage is weak."` | — |
| [SRC-1AE03B9EC3-L003339](../../agents/web_agent.py#L3339) | 3339 | `"            plan[\"queries\"] = list(dict.fromkeys((plan.get(\"queries\") or [])[:3] + candidates))["` | — |
| [SRC-1AE03B9EC3-L003340](../../agents/web_agent.py#L3340) | 3340 | `"                :MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L003341](../../agents/web_agent.py#L3341) | 3341 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L003342](../../agents/web_agent.py#L3342) | 3342 | `"        elif clean_mode == \"latest\":"` | — |
| [SRC-1AE03B9EC3-L003343](../../agents/web_agent.py#L3343) | 3343 | `"            plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L003344](../../agents/web_agent.py#L3344) | 3344 | `"            candidates = ["` | — |
| [SRC-1AE03B9EC3-L003345](../../agents/web_agent.py#L3345) | 3345 | `"                f\"{base_query} latest news updates {dt.datetime.now().year}\","` | — |
| [SRC-1AE03B9EC3-L003346](../../agents/web_agent.py#L3346) | 3346 | `"                f\"{base_query} recent official announcement\","` | — |
| [SRC-1AE03B9EC3-L003347](../../agents/web_agent.py#L3347) | 3347 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L003348](../../agents/web_agent.py#L3348) | 3348 | `"            plan[\"queries\"] = list(dict.fromkeys((plan.get(\"queries\") or [])[:6] + candidates))["` | — |
| [SRC-1AE03B9EC3-L003349](../../agents/web_agent.py#L3349) | 3349 | `"                :MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L003350](../../agents/web_agent.py#L3350) | 3350 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L003351](../../agents/web_agent.py#L3351) | 3351 | `"        elif clean_mode == \"social\":"` | — |
| [SRC-1AE03B9EC3-L003352](../../agents/web_agent.py#L3352) | 3352 | `"            plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L003353](../../agents/web_agent.py#L3353) | 3353 | `"            if not plan.get(\"platforms\"):"` | — |
| [SRC-1AE03B9EC3-L003354](../../agents/web_agent.py#L3354) | 3354 | `"                plan[\"platforms\"] = [\"reddit\", \"bluesky\", \"youtube\"]"` | — |
| [SRC-1AE03B9EC3-L003355](../../agents/web_agent.py#L3355) | 3355 | `"            from agents.research import SOCIAL_DOMAINS"` | — |
| [SRC-1AE03B9EC3-L003356](../../agents/web_agent.py#L3356) | 3356 | `"            candidates = ["` | — |
| [SRC-1AE03B9EC3-L003357](../../agents/web_agent.py#L3357) | 3357 | `"                f\"site:{SOCIAL_DOMAINS[name]} {base_query}\""` | — |
| [SRC-1AE03B9EC3-L003358](../../agents/web_agent.py#L3358) | 3358 | `"                for name in plan[\"platforms\"][:3]"` | — |
| [SRC-1AE03B9EC3-L003359](../../agents/web_agent.py#L3359) | 3359 | `"                if name in SOCIAL_DOMAINS"` | — |
| [SRC-1AE03B9EC3-L003360](../../agents/web_agent.py#L3360) | 3360 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L003361](../../agents/web_agent.py#L3361) | 3361 | `"            plan[\"queries\"] = list(dict.fromkeys((plan.get(\"queries\") or [])[:5] + candidates))["` | — |
| [SRC-1AE03B9EC3-L003362](../../agents/web_agent.py#L3362) | 3362 | `"                :MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L003363](../../agents/web_agent.py#L3363) | 3363 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L003364](../../agents/web_agent.py#L3364) | 3364 | `"        if intent_route == \"LEAD_GENERATION\" and clean_mode == \"auto\":"` | — |
| [SRC-1AE03B9EC3-L003365](../../agents/web_agent.py#L3365) | 3365 | `"            # Prospect discovery needs buyer-intent queries and public social signals,"` | — |
| [SRC-1AE03B9EC3-L003366](../../agents/web_agent.py#L3366) | 3366 | `"            # not just broad pages advertising the requested product."` | — |
| [SRC-1AE03B9EC3-L003367](../../agents/web_agent.py#L3367) | 3367 | `"            plan[\"queries\"] = self._lead_generation_queries(question, plan.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L003368](../../agents/web_agent.py#L3368) | 3368 | `"            plan[\"depth\"] = \"standard\""` | — |
| [SRC-1AE03B9EC3-L003369](../../agents/web_agent.py#L3369) | 3369 | `"            plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L003370](../../agents/web_agent.py#L3370) | 3370 | `"            plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L003371](../../agents/web_agent.py#L3371) | 3371 | `"            allowed_public_platforms = [\"reddit\", \"bluesky\"]"` | — |
| [SRC-1AE03B9EC3-L003372](../../agents/web_agent.py#L3372) | 3372 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L003373](../../agents/web_agent.py#L3373) | 3373 | `"                os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003374](../../agents/web_agent.py#L3374) | 3374 | `"                and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003375](../../agents/web_agent.py#L3375) | 3375 | `"            ):"` | — |
| [SRC-1AE03B9EC3-L003376](../../agents/web_agent.py#L3376) | 3376 | `"                allowed_public_platforms.append(\"facebook\")"` | — |
| [SRC-1AE03B9EC3-L003377](../../agents/web_agent.py#L3377) | 3377 | `"            if os.getenv(\"X_BEARER_TOKEN\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L003378](../../agents/web_agent.py#L3378) | 3378 | `"                allowed_public_platforms.append(\"x\")"` | — |
| [SRC-1AE03B9EC3-L003379](../../agents/web_agent.py#L3379) | 3379 | `"            if os.getenv(\"YOUTUBE_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L003380](../../agents/web_agent.py#L3380) | 3380 | `"                allowed_public_platforms.append(\"youtube\")"` | — |
| [SRC-1AE03B9EC3-L003381](../../agents/web_agent.py#L3381) | 3381 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L003382](../../agents/web_agent.py#L3382) | 3382 | `"                os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003383](../../agents/web_agent.py#L3383) | 3383 | `"                and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L003384](../../agents/web_agent.py#L3384) | 3384 | `"            ):"` | — |
| [SRC-1AE03B9EC3-L003385](../../agents/web_agent.py#L3385) | 3385 | `"                allowed_public_platforms.append(\"instagram\")"` | — |
| [SRC-1AE03B9EC3-L003386](../../agents/web_agent.py#L3386) | 3386 | `"            plan[\"platforms\"] = list(dict.fromkeys(allowed_public_platforms))"` | — |
| [SRC-1AE03B9EC3-L003387](../../agents/web_agent.py#L3387) | 3387 | `""` | — |
| [SRC-1AE03B9EC3-L003388](../../agents/web_agent.py#L3388) | 3388 | `"        sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L003389](../../agents/web_agent.py#L3389) | 3389 | `"        search_warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L003390](../../agents/web_agent.py#L3390) | 3390 | `"        report: dict[str, Any] = {}"` | — |
| [SRC-1AE03B9EC3-L003391](../../agents/web_agent.py#L3391) | 3391 | `"        # Scope diagnostic evidence to this research attempt; a reused WebAgent must not"` | — |
| [SRC-1AE03B9EC3-L003392](../../agents/web_agent.py#L3392) | 3392 | `"        # accidentally inherit provider attempts from an earlier question."` | — |
| [SRC-1AE03B9EC3-L003393](../../agents/web_agent.py#L3393) | 3393 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L003394](../../agents/web_agent.py#L3394) | 3394 | `"            research_diagnostic_baseline = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L003395](../../agents/web_agent.py#L3395) | 3395 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L003396](../../agents/web_agent.py#L3396) | 3396 | `"            sources, search_warnings, report = self._collect_research(plan)"` | — |
| [SRC-1AE03B9EC3-L003397](../../agents/web_agent.py#L3397) | 3397 | `"        except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003398](../../agents/web_agent.py#L3398) | 3398 | `"            search_warnings.append(str(exc))"` | — |
| [SRC-1AE03B9EC3-L003399](../../agents/web_agent.py#L3399) | 3399 | `"            baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L003400](../../agents/web_agent.py#L3400) | 3400 | `"            with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L003401](../../agents/web_agent.py#L3401) | 3401 | `"                failure_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L003402](../../agents/web_agent.py#L3402) | 3402 | `"                    item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L003403](../../agents/web_agent.py#L3403) | 3403 | `"                    if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L003404](../../agents/web_agent.py#L3404) | 3404 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L003405](../../agents/web_agent.py#L3405) | 3405 | `"            provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L003406](../../agents/web_agent.py#L3406) | 3406 | `"                item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L003407](../../agents/web_agent.py#L3407) | 3407 | `"                for item in failure_diagnostics"` | — |
| [SRC-1AE03B9EC3-L003408](../../agents/web_agent.py#L3408) | 3408 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003409](../../agents/web_agent.py#L3409) | 3409 | `"            report = {"` | — |
| [SRC-1AE03B9EC3-L003410](../../agents/web_agent.py#L3410) | 3410 | `"                \"queries_planned\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-1AE03B9EC3-L003411](../../agents/web_agent.py#L3411) | 3411 | `"                # The exact query count is unknowable when the pipeline fails before it"` | — |
| [SRC-1AE03B9EC3-L003412](../../agents/web_agent.py#L3412) | 3412 | `"                # returns its report. A provider diagnostic may still prove an attempt."` | — |
| [SRC-1AE03B9EC3-L003413](../../agents/web_agent.py#L3413) | 3413 | `"                \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L003414](../../agents/web_agent.py#L3414) | 3414 | `"                \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L003415](../../agents/web_agent.py#L3415) | 3415 | `"                \"search_attempted\": True if provider_attempt_observed else None,"` | — |
| [SRC-1AE03B9EC3-L003416](../../agents/web_agent.py#L3416) | 3416 | `"                \"search_outcome\": ("` | — |
| [SRC-1AE03B9EC3-L003417](../../agents/web_agent.py#L3417) | 3417 | `"                    \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L003418](../../agents/web_agent.py#L3418) | 3418 | `"                    if provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L003419](../../agents/web_agent.py#L3419) | 3419 | `"                    else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L003420](../../agents/web_agent.py#L3420) | 3420 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L003421](../../agents/web_agent.py#L3421) | 3421 | `"                \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L003422](../../agents/web_agent.py#L3422) | 3422 | `"                \"unique_sources\": None,"` | — |
| [SRC-1AE03B9EC3-L003423](../../agents/web_agent.py#L3423) | 3423 | `"                \"pages_fetched\": None,"` | — |
| [SRC-1AE03B9EC3-L003424](../../agents/web_agent.py#L3424) | 3424 | `"                \"providers_used\": [],"` | — |
| [SRC-1AE03B9EC3-L003425](../../agents/web_agent.py#L3425) | 3425 | `"                \"provider_counts\": None,"` | — |
| [SRC-1AE03B9EC3-L003426](../../agents/web_agent.py#L3426) | 3426 | `"                \"platform_counts\": {},"` | — |
| [SRC-1AE03B9EC3-L003427](../../agents/web_agent.py#L3427) | 3427 | `"                \"social_direct_results\": None,"` | — |
| [SRC-1AE03B9EC3-L003428](../../agents/web_agent.py#L3428) | 3428 | `"                \"provider_diagnostics\": failure_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L003429](../../agents/web_agent.py#L3429) | 3429 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L003430](../../agents/web_agent.py#L3430) | 3430 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L003431](../../agents/web_agent.py#L3431) | 3431 | `"                \"evidence_signals\": evidence_signal_report([], plan.get(\"freshness\", \"any\")),"` | — |
| [SRC-1AE03B9EC3-L003432](../../agents/web_agent.py#L3432) | 3432 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003433](../../agents/web_agent.py#L3433) | 3433 | `"        # Final relevance check is intentionally repeated after fusion, before any answer LLM call."` | — |
| [SRC-1AE03B9EC3-L003434](../../agents/web_agent.py#L3434) | 3434 | `"        filtered_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L003435](../../agents/web_agent.py#L3435) | 3435 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L003436](../../agents/web_agent.py#L3436) | 3436 | `"            if \"user_supplied_url\" in source.get(\"providers\", []):"` | — |
| [SRC-1AE03B9EC3-L003437](../../agents/web_agent.py#L3437) | 3437 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L003438](../../agents/web_agent.py#L3438) | 3438 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L003439](../../agents/web_agent.py#L3439) | 3439 | `"            candidate_queries = source.get(\"queries\") or plan.get(\"queries\") or [question]"` | — |
| [SRC-1AE03B9EC3-L003440](../../agents/web_agent.py#L3440) | 3440 | `"            if any(self._source_matches_query(str(q), source) for q in candidate_queries):"` | — |
| [SRC-1AE03B9EC3-L003441](../../agents/web_agent.py#L3441) | 3441 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L003442](../../agents/web_agent.py#L3442) | 3442 | `"        sources = filtered_sources"` | — |
| [SRC-1AE03B9EC3-L003443](../../agents/web_agent.py#L3443) | 3443 | `"        search_warning = \"؛ \".join(search_warnings) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L003444](../../agents/web_agent.py#L3444) | 3444 | `"        independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L003445](../../agents/web_agent.py#L3445) | 3445 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L003446](../../agents/web_agent.py#L3446) | 3446 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L003447](../../agents/web_agent.py#L3447) | 3447 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L003448](../../agents/web_agent.py#L3448) | 3448 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L003449](../../agents/web_agent.py#L3449) | 3449 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003450](../../agents/web_agent.py#L3450) | 3450 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L003451](../../agents/web_agent.py#L3451) | 3451 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003452](../../agents/web_agent.py#L3452) | 3452 | `"        independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L003453](../../agents/web_agent.py#L3453) | 3453 | `"        # A user-requested page summary is a different task from open-ended research:"` | — |
| [SRC-1AE03B9EC3-L003454](../../agents/web_agent.py#L3454) | 3454 | `"        # one successfully extracted, explicitly supplied page can support a summary,"` | — |
| [SRC-1AE03B9EC3-L003455](../../agents/web_agent.py#L3455) | 3455 | `"        # but must never be presented as independently corroborated research."` | — |
| [SRC-1AE03B9EC3-L003456](../../agents/web_agent.py#L3456) | 3456 | `"        has_read_user_supplied_page = any("` | — |
| [SRC-1AE03B9EC3-L003457](../../agents/web_agent.py#L3457) | 3457 | `"            \"user_supplied_url\" in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L003458](../../agents/web_agent.py#L3458) | 3458 | `"            and bool(source.get(\"page_fetched\"))"` | — |
| [SRC-1AE03B9EC3-L003459](../../agents/web_agent.py#L3459) | 3459 | `"            and bool(str(source.get(\"page_text\") or \"\").strip())"` | — |
| [SRC-1AE03B9EC3-L003460](../../agents/web_agent.py#L3460) | 3460 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L003461](../../agents/web_agent.py#L3461) | 3461 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003462](../../agents/web_agent.py#L3462) | 3462 | `"        single_source_page_summary = ("` | — |
| [SRC-1AE03B9EC3-L003463](../../agents/web_agent.py#L3463) | 3463 | `"            has_read_user_supplied_page"` | — |
| [SRC-1AE03B9EC3-L003464](../../agents/web_agent.py#L3464) | 3464 | `"            and len(sources) == 1"` | — |
| [SRC-1AE03B9EC3-L003465](../../agents/web_agent.py#L3465) | 3465 | `"            and len(independent_domains) == 1"` | — |
| [SRC-1AE03B9EC3-L003466](../../agents/web_agent.py#L3466) | 3466 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003467](../../agents/web_agent.py#L3467) | 3467 | `"        if single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L003468](../../agents/web_agent.py#L3468) | 3468 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L003469](../../agents/web_agent.py#L3469) | 3469 | `"                \"هذا ملخص للرابط الذي قدمته فقط؛ لم يتم تأكيد محتواه من مصدر مستقل آخر.\""` | — |
| [SRC-1AE03B9EC3-L003470](../../agents/web_agent.py#L3470) | 3470 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003471](../../agents/web_agent.py#L3471) | 3471 | `"            search_warning = \"؛ \".join(search_warnings)"` | — |
| [SRC-1AE03B9EC3-L003472](../../agents/web_agent.py#L3472) | 3472 | `"        # Link-finding and lead-discovery are actionable discovery tasks, not broad"` | — |
| [SRC-1AE03B9EC3-L003473](../../agents/web_agent.py#L3473) | 3473 | `"        # fact-checking. Keep useful candidates visible while explicitly labelling them"` | — |
| [SRC-1AE03B9EC3-L003474](../../agents/web_agent.py#L3474) | 3474 | `"        # as uncorroborated instead of refusing a lone result as if it were no result."` | — |
| [SRC-1AE03B9EC3-L003475](../../agents/web_agent.py#L3475) | 3475 | `"        navigation_request = self._is_navigation_request(question)"` | — |
| [SRC-1AE03B9EC3-L003476](../../agents/web_agent.py#L3476) | 3476 | `"        lead_request = intent_route == \"LEAD_GENERATION\" or self._is_lead_search(question)"` | — |
| [SRC-1AE03B9EC3-L003477](../../agents/web_agent.py#L3477) | 3477 | `"        listing_request = self._is_listing_discovery(question)"` | — |
| [SRC-1AE03B9EC3-L003478](../../agents/web_agent.py#L3478) | 3478 | `"        lead_evidence_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L003479](../../agents/web_agent.py#L3479) | 3479 | `"        related_lead_results_count = 0"` | — |
| [SRC-1AE03B9EC3-L003480](../../agents/web_agent.py#L3480) | 3480 | `"        if lead_request:"` | — |
| [SRC-1AE03B9EC3-L003481](../../agents/web_agent.py#L3481) | 3481 | `"            related_lead_results_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L003482](../../agents/web_agent.py#L3482) | 3482 | `"            for source in sources:"` | — |
| [SRC-1AE03B9EC3-L003483](../../agents/web_agent.py#L3483) | 3483 | `"                signal = self._lead_intent_evidence(source)"` | — |
| [SRC-1AE03B9EC3-L003484](../../agents/web_agent.py#L3484) | 3484 | `"                if signal:"` | — |
| [SRC-1AE03B9EC3-L003485](../../agents/web_agent.py#L3485) | 3485 | `"                    source[\"lead_qualification\"] = \"public_buyer_intent_signal\""` | — |
| [SRC-1AE03B9EC3-L003486](../../agents/web_agent.py#L3486) | 3486 | `"                    source[\"lead_intent_evidence\"] = signal"` | — |
| [SRC-1AE03B9EC3-L003487](../../agents/web_agent.py#L3487) | 3487 | `"                    lead_evidence_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L003488](../../agents/web_agent.py#L3488) | 3488 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L003489](../../agents/web_agent.py#L3489) | 3489 | `"                    source[\"lead_qualification\"] = \"related_result_not_lead\""` | — |
| [SRC-1AE03B9EC3-L003490](../../agents/web_agent.py#L3490) | 3490 | `"            lead_research_incomplete = ("` | — |
| [SRC-1AE03B9EC3-L003491](../../agents/web_agent.py#L3491) | 3491 | `"                not sources"` | — |
| [SRC-1AE03B9EC3-L003492](../../agents/web_agent.py#L3492) | 3492 | `"                and report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L003493](../../agents/web_agent.py#L3493) | 3493 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003494](../../agents/web_agent.py#L3494) | 3494 | `"            report[\"lead_generation\"] = {"` | — |
| [SRC-1AE03B9EC3-L003495](../../agents/web_agent.py#L3495) | 3495 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L003496](../../agents/web_agent.py#L3496) | 3496 | `"                    \"research_incomplete\" if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L003497](../../agents/web_agent.py#L3497) | 3497 | `"                    else \"candidate_signals_found\" if lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L003498](../../agents/web_agent.py#L3498) | 3498 | `"                    else \"no_qualified_candidates_found\""` | — |
| [SRC-1AE03B9EC3-L003499](../../agents/web_agent.py#L3499) | 3499 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L003500](../../agents/web_agent.py#L3500) | 3500 | `"                \"candidate_signal_count\": ("` | — |
| [SRC-1AE03B9EC3-L003501](../../agents/web_agent.py#L3501) | 3501 | `"                    None if lead_research_incomplete else len(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L003502](../../agents/web_agent.py#L3502) | 3502 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L003503](../../agents/web_agent.py#L3503) | 3503 | `"                \"related_results_reviewed\": ("` | — |
| [SRC-1AE03B9EC3-L003504](../../agents/web_agent.py#L3504) | 3504 | `"                    None if lead_research_incomplete else related_lead_results_count"` | — |
| [SRC-1AE03B9EC3-L003505](../../agents/web_agent.py#L3505) | 3505 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L003506](../../agents/web_agent.py#L3506) | 3506 | `"                \"qualification_rule\": \"explicit_public_buyer_intent_phrase\","` | — |
| [SRC-1AE03B9EC3-L003507](../../agents/web_agent.py#L3507) | 3507 | `"                \"identity_verified\": False,"` | — |
| [SRC-1AE03B9EC3-L003508](../../agents/web_agent.py#L3508) | 3508 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003509](../../agents/web_agent.py#L3509) | 3509 | `"            if not lead_evidence_sources:"` | — |
| [SRC-1AE03B9EC3-L003510](../../agents/web_agent.py#L3510) | 3510 | `"                if sources:"` | — |
| [SRC-1AE03B9EC3-L003511](../../agents/web_agent.py#L3511) | 3511 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L003512](../../agents/web_agent.py#L3512) | 3512 | `"                        \"لم أعثر على إشارة نصية واضحة تثبت أن أي نتيجة في هذه الجولة تتعلق بشخص \""` | — |
| [SRC-1AE03B9EC3-L003513](../../agents/web_agent.py#L3513) | 3513 | `"                        \"يريد الشراء. راجعت \""` | — |
| [SRC-1AE03B9EC3-L003514](../../agents/web_agent.py#L3514) | 3514 | `"                        + str(len(sources))"` | — |
| [SRC-1AE03B9EC3-L003515](../../agents/web_agent.py#L3515) | 3515 | `"                        + \" نتيجة مرتبطة بالموضوع، لكنني لم أعتبر إعلانات البيع أو صفحات السوق \""` | — |
| [SRC-1AE03B9EC3-L003516](../../agents/web_agent.py#L3516) | 3516 | `"                        \"عملاء محتملين. الروابط أدناه نتائج مرتبطة بالموضوع فقط وليست عملاء.\""` | — |
| [SRC-1AE03B9EC3-L003517](../../agents/web_agent.py#L3517) | 3517 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003518](../../agents/web_agent.py#L3518) | 3518 | `"                elif report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L003519](../../agents/web_agent.py#L3519) | 3519 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L003520](../../agents/web_agent.py#L3520) | 3520 | `"                        \"تعطل مسار البحث أو لم يمكن تأكيد اكتماله؛ لذلك لا أستطيع تحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L003521](../../agents/web_agent.py#L3521) | 3521 | `"                        \"كانت هناك نتائج تصلح كعملاء محتملين في هذه الجولة.\""` | — |
| [SRC-1AE03B9EC3-L003522](../../agents/web_agent.py#L3522) | 3522 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003523](../../agents/web_agent.py#L3523) | 3523 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L003524](../../agents/web_agent.py#L3524) | 3524 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L003525](../../agents/web_agent.py#L3525) | 3525 | `"                        \"لم تظهر نتائج قابلة للاستخدام تثبت نية شراء في هذه الجولة. هذا لا يثبت \""` | — |
| [SRC-1AE03B9EC3-L003526](../../agents/web_agent.py#L3526) | 3526 | `"                        \"عدم وجود عملاء؛ بل يعني أن البحث الحالي لم يعثر على دليل كافٍ.\""` | — |
| [SRC-1AE03B9EC3-L003527](../../agents/web_agent.py#L3527) | 3527 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003528](../../agents/web_agent.py#L3528) | 3528 | `"                report[\"research_quality\"] = \"failed\""` | — |
| [SRC-1AE03B9EC3-L003529](../../agents/web_agent.py#L3529) | 3529 | `"                # Distinguish zero qualified signals from unknown counts after an exception."` | — |
| [SRC-1AE03B9EC3-L003530](../../agents/web_agent.py#L3530) | 3530 | `"                report[\"usable_sources_after_filtering\"] = ("` | — |
| [SRC-1AE03B9EC3-L003531](../../agents/web_agent.py#L3531) | 3531 | `"                    None if lead_research_incomplete else len(sources)"` | — |
| [SRC-1AE03B9EC3-L003532](../../agents/web_agent.py#L3532) | 3532 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003533](../../agents/web_agent.py#L3533) | 3533 | `"                report[\"evidence_signals\"] = ("` | — |
| [SRC-1AE03B9EC3-L003534](../../agents/web_agent.py#L3534) | 3534 | `"                    None if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L003535](../../agents/web_agent.py#L3535) | 3535 | `"                    else evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L003536](../../agents/web_agent.py#L3536) | 3536 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003537](../../agents/web_agent.py#L3537) | 3537 | `"                public_related_sources = [{"` | — |
| [SRC-1AE03B9EC3-L003538](../../agents/web_agent.py#L3538) | 3538 | `"                    \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L003539](../../agents/web_agent.py#L3539) | 3539 | `"                    \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L003540](../../agents/web_agent.py#L3540) | 3540 | `"                    \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L003541](../../agents/web_agent.py#L3541) | 3541 | `"                    \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L003542](../../agents/web_agent.py#L3542) | 3542 | `"                    \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L003543](../../agents/web_agent.py#L3543) | 3543 | `"                    \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L003544](../../agents/web_agent.py#L3544) | 3544 | `"                    \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L003545](../../agents/web_agent.py#L3545) | 3545 | `"                    \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L003546](../../agents/web_agent.py#L3546) | 3546 | `"                    \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L003547](../../agents/web_agent.py#L3547) | 3547 | `"                    \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L003548](../../agents/web_agent.py#L3548) | 3548 | `"                    \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L003549](../../agents/web_agent.py#L3549) | 3549 | `"                    \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L003550](../../agents/web_agent.py#L3550) | 3550 | `"                    \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L003551](../../agents/web_agent.py#L3551) | 3551 | `"                    \"lead_qualification\": \"related_result_not_lead\","` | — |
| [SRC-1AE03B9EC3-L003552](../../agents/web_agent.py#L3552) | 3552 | `"                } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L003553](../../agents/web_agent.py#L3553) | 3553 | `"                return {"` | — |
| [SRC-1AE03B9EC3-L003554](../../agents/web_agent.py#L3554) | 3554 | `"                    \"answer\": lead_answer,"` | — |
| [SRC-1AE03B9EC3-L003555](../../agents/web_agent.py#L3555) | 3555 | `"                    \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L003556](../../agents/web_agent.py#L3556) | 3556 | `"                    \"search_query\": (plan.get(\"queries\") or [question])[0],"` | — |
| [SRC-1AE03B9EC3-L003557](../../agents/web_agent.py#L3557) | 3557 | `"                    \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L003558](../../agents/web_agent.py#L3558) | 3558 | `"                    \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L003559](../../agents/web_agent.py#L3559) | 3559 | `"                        \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L003560](../../agents/web_agent.py#L3560) | 3560 | `"                        \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L003561](../../agents/web_agent.py#L3561) | 3561 | `"                        \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L003562](../../agents/web_agent.py#L3562) | 3562 | `"                        \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L003563](../../agents/web_agent.py#L3563) | 3563 | `"                        \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L003564](../../agents/web_agent.py#L3564) | 3564 | `"                        \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L003565](../../agents/web_agent.py#L3565) | 3565 | `"                        \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L003566](../../agents/web_agent.py#L3566) | 3566 | `"                        \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L003567](../../agents/web_agent.py#L3567) | 3567 | `"                        \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L003568](../../agents/web_agent.py#L3568) | 3568 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L003569](../../agents/web_agent.py#L3569) | 3569 | `"                    \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L003570](../../agents/web_agent.py#L3570) | 3570 | `"                    \"sources\": public_related_sources,"` | — |
| [SRC-1AE03B9EC3-L003571](../../agents/web_agent.py#L3571) | 3571 | `"                    \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L003572](../../agents/web_agent.py#L3572) | 3572 | `"                    \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L003573](../../agents/web_agent.py#L3573) | 3573 | `"                    \"search_attempted\": report.get("` | — |
| [SRC-1AE03B9EC3-L003574](../../agents/web_agent.py#L3574) | 3574 | `"                        \"search_attempted\","` | — |
| [SRC-1AE03B9EC3-L003575](../../agents/web_agent.py#L3575) | 3575 | `"                        bool(report.get(\"queries_attempted\", 0)),"` | — |
| [SRC-1AE03B9EC3-L003576](../../agents/web_agent.py#L3576) | 3576 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L003577](../../agents/web_agent.py#L3577) | 3577 | `"                    \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L003578](../../agents/web_agent.py#L3578) | 3578 | `"                    \"warnings\": [lead_answer],"` | — |
| [SRC-1AE03B9EC3-L003579](../../agents/web_agent.py#L3579) | 3579 | `"                    \"kind\": \"lead_discovery_no_qualified_candidates\","` | — |
| [SRC-1AE03B9EC3-L003580](../../agents/web_agent.py#L3580) | 3580 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L003581](../../agents/web_agent.py#L3581) | 3581 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L003582](../../agents/web_agent.py#L3582) | 3582 | `"                    \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L003583](../../agents/web_agent.py#L3583) | 3583 | `"                }"` | — |
| [SRC-1AE03B9EC3-L003584](../../agents/web_agent.py#L3584) | 3584 | `"            # Only explicit public buyer-intent signals may be synthesized as lead candidates."` | — |
| [SRC-1AE03B9EC3-L003585](../../agents/web_agent.py#L3585) | 3585 | `"            sources = lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L003586](../../agents/web_agent.py#L3586) | 3586 | `"            report[\"evidence_signals\"] = evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L003587](../../agents/web_agent.py#L3587) | 3587 | `"            report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L003588](../../agents/web_agent.py#L3588) | 3588 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L003589](../../agents/web_agent.py#L3589) | 3589 | `"            report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L003590](../../agents/web_agent.py#L3590) | 3590 | `"            independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L003591](../../agents/web_agent.py#L3591) | 3591 | `"                registrable_domain("` | — |
| [SRC-1AE03B9EC3-L003592](../../agents/web_agent.py#L3592) | 3592 | `"                    source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L003593](../../agents/web_agent.py#L3593) | 3593 | `"                    or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L003594](../../agents/web_agent.py#L3594) | 3594 | `"                    or \"\""` | — |
| [SRC-1AE03B9EC3-L003595](../../agents/web_agent.py#L3595) | 3595 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003596](../../agents/web_agent.py#L3596) | 3596 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L003597](../../agents/web_agent.py#L3597) | 3597 | `"            }"` | — |
| [SRC-1AE03B9EC3-L003598](../../agents/web_agent.py#L3598) | 3598 | `"            independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L003599](../../agents/web_agent.py#L3599) | 3599 | `"        single_source_navigation = navigation_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L003600](../../agents/web_agent.py#L3600) | 3600 | `"        single_source_social = bool(plan.get(\"social_focus\")) and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L003601](../../agents/web_agent.py#L3601) | 3601 | `"        single_source_lead = lead_request and bool(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L003602](../../agents/web_agent.py#L3602) | 3602 | `"        single_source_listing = listing_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L003603](../../agents/web_agent.py#L3603) | 3603 | `"        task_specific_partial_evidence = ("` | — |
| [SRC-1AE03B9EC3-L003604](../../agents/web_agent.py#L3604) | 3604 | `"            single_source_page_summary"` | — |
| [SRC-1AE03B9EC3-L003605](../../agents/web_agent.py#L3605) | 3605 | `"            or single_source_navigation"` | — |
| [SRC-1AE03B9EC3-L003606](../../agents/web_agent.py#L3606) | 3606 | `"            or single_source_social"` | — |
| [SRC-1AE03B9EC3-L003607](../../agents/web_agent.py#L3607) | 3607 | `"            or single_source_lead"` | — |
| [SRC-1AE03B9EC3-L003608](../../agents/web_agent.py#L3608) | 3608 | `"            or single_source_listing"` | — |
| [SRC-1AE03B9EC3-L003609](../../agents/web_agent.py#L3609) | 3609 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003610](../../agents/web_agent.py#L3610) | 3610 | `"        needs_corroboration = len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L003611](../../agents/web_agent.py#L3611) | 3611 | `"        evidence_repair: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L003612](../../agents/web_agent.py#L3612) | 3612 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L003613](../../agents/web_agent.py#L3613) | 3613 | `"            \"max_extra_queries\": 1,"` | — |
| [SRC-1AE03B9EC3-L003614](../../agents/web_agent.py#L3614) | 3614 | `"            \"reason\": \"initial_evidence_gate_satisfied\" if not needs_corroboration else \"not_attempted\","` | — |
| [SRC-1AE03B9EC3-L003615](../../agents/web_agent.py#L3615) | 3615 | `"        }"` | — |
| [SRC-1AE03B9EC3-L003616](../../agents/web_agent.py#L3616) | 3616 | `"        if needs_corroboration:"` | — |
| [SRC-1AE03B9EC3-L003617](../../agents/web_agent.py#L3617) | 3617 | `"            if task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L003618](../../agents/web_agent.py#L3618) | 3618 | `"                evidence_repair[\"reason\"] = \"task_specific_partial_evidence\""` | — |
| [SRC-1AE03B9EC3-L003619](../../agents/web_agent.py#L3619) | 3619 | `"            elif plan.get(\"social_focus\"):"` | — |
| [SRC-1AE03B9EC3-L003620](../../agents/web_agent.py#L3620) | 3620 | `"                evidence_repair[\"reason\"] = \"social_search_not_retried\""` | — |
| [SRC-1AE03B9EC3-L003621](../../agents/web_agent.py#L3621) | 3621 | `"            elif plan.get(\"depth\") == \"deep\" or report.get(\"expansion_queries\"):"` | — |
| [SRC-1AE03B9EC3-L003622](../../agents/web_agent.py#L3622) | 3622 | `"                evidence_repair[\"reason\"] = \"deep_research_already_expanded\""` | — |
| [SRC-1AE03B9EC3-L003623](../../agents/web_agent.py#L3623) | 3623 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L003624](../../agents/web_agent.py#L3624) | 3624 | `"                original_queries = ["` | — |
| [SRC-1AE03B9EC3-L003625](../../agents/web_agent.py#L3625) | 3625 | `"                    str(item).strip()"` | — |
| [SRC-1AE03B9EC3-L003626](../../agents/web_agent.py#L3626) | 3626 | `"                    for item in plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L003627](../../agents/web_agent.py#L3627) | 3627 | `"                    if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L003628](../../agents/web_agent.py#L3628) | 3628 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L003629](../../agents/web_agent.py#L3629) | 3629 | `"                base_query = original_queries[0] if original_queries else question"` | — |
| [SRC-1AE03B9EC3-L003630](../../agents/web_agent.py#L3630) | 3630 | `"                suffix = ("` | — |
| [SRC-1AE03B9EC3-L003631](../../agents/web_agent.py#L3631) | 3631 | `"                    \"latest official primary source\""` | — |
| [SRC-1AE03B9EC3-L003632](../../agents/web_agent.py#L3632) | 3632 | `"                    if plan.get(\"freshness\") == \"current\""` | — |
| [SRC-1AE03B9EC3-L003633](../../agents/web_agent.py#L3633) | 3633 | `"                    else \"official primary source data\""` | — |
| [SRC-1AE03B9EC3-L003634](../../agents/web_agent.py#L3634) | 3634 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003635](../../agents/web_agent.py#L3635) | 3635 | `"                repair_query = f\"{base_query} {suffix}\"[:500].strip()"` | — |
| [SRC-1AE03B9EC3-L003636](../../agents/web_agent.py#L3636) | 3636 | `"                known_queries = {"` | — |
| [SRC-1AE03B9EC3-L003637](../../agents/web_agent.py#L3637) | 3637 | `"                    _normalize_search_query(item).casefold()"` | — |
| [SRC-1AE03B9EC3-L003638](../../agents/web_agent.py#L3638) | 3638 | `"                    for item in original_queries"` | — |
| [SRC-1AE03B9EC3-L003639](../../agents/web_agent.py#L3639) | 3639 | `"                }"` | — |
| [SRC-1AE03B9EC3-L003640](../../agents/web_agent.py#L3640) | 3640 | `"                if _normalize_search_query(repair_query).casefold() in known_queries:"` | — |
| [SRC-1AE03B9EC3-L003641](../../agents/web_agent.py#L3641) | 3641 | `"                    repair_query = f\"{base_query} independent corroborating evidence\"[:500].strip()"` | — |
| [SRC-1AE03B9EC3-L003642](../../agents/web_agent.py#L3642) | 3642 | `"                if _normalize_search_query(repair_query).casefold() not in known_queries:"` | — |
| [SRC-1AE03B9EC3-L003643](../../agents/web_agent.py#L3643) | 3643 | `"                    initial_source_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L003644](../../agents/web_agent.py#L3644) | 3644 | `"                    initial_domain_count = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L003645](../../agents/web_agent.py#L3645) | 3645 | `"                    evidence_repair[\"attempted\"] = True"` | — |
| [SRC-1AE03B9EC3-L003646](../../agents/web_agent.py#L3646) | 3646 | `"                    evidence_repair[\"reason\"] = \"thin_or_unrelated_initial_evidence\""` | — |
| [SRC-1AE03B9EC3-L003647](../../agents/web_agent.py#L3647) | 3647 | `"                    evidence_repair[\"query\"] = repair_query"` | — |
| [SRC-1AE03B9EC3-L003648](../../agents/web_agent.py#L3648) | 3648 | `"                    repair_plan = dict(plan)"` | — |
| [SRC-1AE03B9EC3-L003649](../../agents/web_agent.py#L3649) | 3649 | `"                    repair_plan.update({"` | — |
| [SRC-1AE03B9EC3-L003650](../../agents/web_agent.py#L3650) | 3650 | `"                        \"queries\": [repair_query],"` | — |
| [SRC-1AE03B9EC3-L003651](../../agents/web_agent.py#L3651) | 3651 | `"                        \"depth\": \"standard\","` | — |
| [SRC-1AE03B9EC3-L003652](../../agents/web_agent.py#L3652) | 3652 | `"                        \"social_focus\": False,"` | — |
| [SRC-1AE03B9EC3-L003653](../../agents/web_agent.py#L3653) | 3653 | `"                        \"platforms\": [],"` | — |
| [SRC-1AE03B9EC3-L003654](../../agents/web_agent.py#L3654) | 3654 | `"                        \"direct_urls\": [],"` | — |
| [SRC-1AE03B9EC3-L003655](../../agents/web_agent.py#L3655) | 3655 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L003656](../../agents/web_agent.py#L3656) | 3656 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L003657](../../agents/web_agent.py#L3657) | 3657 | `"                        repair_sources, repair_warnings, repair_report = self._collect_research("` | — |
| [SRC-1AE03B9EC3-L003658](../../agents/web_agent.py#L3658) | 3658 | `"                            repair_plan"` | — |
| [SRC-1AE03B9EC3-L003659](../../agents/web_agent.py#L3659) | 3659 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003660](../../agents/web_agent.py#L3660) | 3660 | `"                    except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L003661](../../agents/web_agent.py#L3661) | 3661 | `"                        repair_sources = []"` | — |
| [SRC-1AE03B9EC3-L003662](../../agents/web_agent.py#L3662) | 3662 | `"                        repair_warnings = []"` | — |
| [SRC-1AE03B9EC3-L003663](../../agents/web_agent.py#L3663) | 3663 | `"                        repair_report = {"` | — |
| [SRC-1AE03B9EC3-L003664](../../agents/web_agent.py#L3664) | 3664 | `"                            \"queries_planned\": 1,"` | — |
| [SRC-1AE03B9EC3-L003665](../../agents/web_agent.py#L3665) | 3665 | `"                            \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L003666](../../agents/web_agent.py#L3666) | 3666 | `"                            \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L003667](../../agents/web_agent.py#L3667) | 3667 | `"                            \"search_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L003668](../../agents/web_agent.py#L3668) | 3668 | `"                            \"search_outcome\": \"unknown_after_research_error\","` | — |
| [SRC-1AE03B9EC3-L003669](../../agents/web_agent.py#L3669) | 3669 | `"                            \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L003670](../../agents/web_agent.py#L3670) | 3670 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L003671](../../agents/web_agent.py#L3671) | 3671 | `"                        search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L003672](../../agents/web_agent.py#L3672) | 3672 | `"                            \"تعذر تنفيذ محاولة البحث الإضافية المحدودة (\""` | — |
| [SRC-1AE03B9EC3-L003673](../../agents/web_agent.py#L3673) | 3673 | `"                            + type(exc).__name__ + \").\""` | — |
| [SRC-1AE03B9EC3-L003674](../../agents/web_agent.py#L3674) | 3674 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003675](../../agents/web_agent.py#L3675) | 3675 | `"                    search_warnings.extend(repair_warnings)"` | — |
| [SRC-1AE03B9EC3-L003676](../../agents/web_agent.py#L3676) | 3676 | `"                    evidence_repair[\"attempted_query_count\"] = 1"` | — |
| [SRC-1AE03B9EC3-L003677](../../agents/web_agent.py#L3677) | 3677 | `"                    evidence_repair[\"initial_source_count\"] = initial_source_count"` | — |
| [SRC-1AE03B9EC3-L003678](../../agents/web_agent.py#L3678) | 3678 | `"                    evidence_repair[\"initial_independent_domain_count\"] = initial_domain_count"` | — |
| [SRC-1AE03B9EC3-L003679](../../agents/web_agent.py#L3679) | 3679 | `"                    evidence_repair[\"new_sources_added\"] = 0"` | — |
| [SRC-1AE03B9EC3-L003680](../../agents/web_agent.py#L3680) | 3680 | `"                    source_indexes: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L003681](../../agents/web_agent.py#L3681) | 3681 | `"                    for source_index, source in enumerate(sources):"` | — |
| [SRC-1AE03B9EC3-L003682](../../agents/web_agent.py#L3682) | 3682 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L003683](../../agents/web_agent.py#L3683) | 3683 | `"                        if source_key:"` | — |
| [SRC-1AE03B9EC3-L003684](../../agents/web_agent.py#L3684) | 3684 | `"                            source_indexes.setdefault(source_key, source_index)"` | — |
| [SRC-1AE03B9EC3-L003685](../../agents/web_agent.py#L3685) | 3685 | `"                    relevant_queries = list(dict.fromkeys([question] + original_queries))"` | — |
| [SRC-1AE03B9EC3-L003686](../../agents/web_agent.py#L3686) | 3686 | `"                    for source in repair_sources:"` | — |
| [SRC-1AE03B9EC3-L003687](../../agents/web_agent.py#L3687) | 3687 | `"                        if not isinstance(source, dict):"` | — |
| [SRC-1AE03B9EC3-L003688](../../agents/web_agent.py#L3688) | 3688 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L003689](../../agents/web_agent.py#L3689) | 3689 | `"                        if not any("` | — |
| [SRC-1AE03B9EC3-L003690](../../agents/web_agent.py#L3690) | 3690 | `"                            self._source_matches_query(candidate, source)"` | — |
| [SRC-1AE03B9EC3-L003691](../../agents/web_agent.py#L3691) | 3691 | `"                            for candidate in relevant_queries if candidate"` | — |
| [SRC-1AE03B9EC3-L003692](../../agents/web_agent.py#L3692) | 3692 | `"                        ):"` | — |
| [SRC-1AE03B9EC3-L003693](../../agents/web_agent.py#L3693) | 3693 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L003694](../../agents/web_agent.py#L3694) | 3694 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L003695](../../agents/web_agent.py#L3695) | 3695 | `"                        if not source_key:"` | — |
| [SRC-1AE03B9EC3-L003696](../../agents/web_agent.py#L3696) | 3696 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L003697](../../agents/web_agent.py#L3697) | 3697 | `"                        existing_index = source_indexes.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L003698](../../agents/web_agent.py#L3698) | 3698 | `"                        if existing_index is None:"` | — |
| [SRC-1AE03B9EC3-L003699](../../agents/web_agent.py#L3699) | 3699 | `"                            source_indexes[source_key] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L003700](../../agents/web_agent.py#L3700) | 3700 | `"                            sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L003701](../../agents/web_agent.py#L3701) | 3701 | `"                            evidence_repair[\"new_sources_added\"] += 1"` | — |
| [SRC-1AE03B9EC3-L003702](../../agents/web_agent.py#L3702) | 3702 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L003703](../../agents/web_agent.py#L3703) | 3703 | `"                        existing_source = sources[existing_index]"` | — |
| [SRC-1AE03B9EC3-L003704](../../agents/web_agent.py#L3704) | 3704 | `"                        providers = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L003705](../../agents/web_agent.py#L3705) | 3705 | `"                            list(existing_source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L003706](../../agents/web_agent.py#L3706) | 3706 | `"                            + list(source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L003707](../../agents/web_agent.py#L3707) | 3707 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L003708](../../agents/web_agent.py#L3708) | 3708 | `"                        source_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L003709](../../agents/web_agent.py#L3709) | 3709 | `"                            list(existing_source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L003710](../../agents/web_agent.py#L3710) | 3710 | `"                            + list(source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L003711](../../agents/web_agent.py#L3711) | 3711 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L003712](../../agents/web_agent.py#L3712) | 3712 | `"                        if source.get(\"page_fetched\") and not existing_source.get(\"page_fetched\"):"` | — |
| [SRC-1AE03B9EC3-L003713](../../agents/web_agent.py#L3713) | 3713 | `"                            merged_source = dict(existing_source)"` | — |
| [SRC-1AE03B9EC3-L003714](../../agents/web_agent.py#L3714) | 3714 | `"                            merged_source.update(source)"` | — |
| [SRC-1AE03B9EC3-L003715](../../agents/web_agent.py#L3715) | 3715 | `"                            merged_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L003716](../../agents/web_agent.py#L3716) | 3716 | `"                            merged_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L003717](../../agents/web_agent.py#L3717) | 3717 | `"                            sources[existing_index] = merged_source"` | — |
| [SRC-1AE03B9EC3-L003718](../../agents/web_agent.py#L3718) | 3718 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L003719](../../agents/web_agent.py#L3719) | 3719 | `"                            existing_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L003720](../../agents/web_agent.py#L3720) | 3720 | `"                            existing_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L003721](../../agents/web_agent.py#L3721) | 3721 | `"                    sources.sort("` | — |
| [SRC-1AE03B9EC3-L003722](../../agents/web_agent.py#L3722) | 3722 | `"                        key=lambda item: float(item.get(\"rank_score\", 0) or 0),"` | — |
| [SRC-1AE03B9EC3-L003723](../../agents/web_agent.py#L3723) | 3723 | `"                        reverse=True,"` | — |
| [SRC-1AE03B9EC3-L003724](../../agents/web_agent.py#L3724) | 3724 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003725](../../agents/web_agent.py#L3725) | 3725 | `"                    plan[\"queries\"] = list(dict.fromkeys(original_queries + [repair_query]))"` | — |
| [SRC-1AE03B9EC3-L003726](../../agents/web_agent.py#L3726) | 3726 | `"                    independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L003727](../../agents/web_agent.py#L3727) | 3727 | `"                        registrable_domain("` | — |
| [SRC-1AE03B9EC3-L003728](../../agents/web_agent.py#L3728) | 3728 | `"                            source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L003729](../../agents/web_agent.py#L3729) | 3729 | `"                            or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L003730](../../agents/web_agent.py#L3730) | 3730 | `"                            or \"\""` | — |
| [SRC-1AE03B9EC3-L003731](../../agents/web_agent.py#L3731) | 3731 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003732](../../agents/web_agent.py#L3732) | 3732 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L003733](../../agents/web_agent.py#L3733) | 3733 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L003734](../../agents/web_agent.py#L3734) | 3734 | `"                    independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L003735](../../agents/web_agent.py#L3735) | 3735 | `"                    needs_corroboration = ("` | — |
| [SRC-1AE03B9EC3-L003736](../../agents/web_agent.py#L3736) | 3736 | `"                        len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L003737](../../agents/web_agent.py#L3737) | 3737 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003738](../../agents/web_agent.py#L3738) | 3738 | `"                    evidence_repair.update({"` | — |
| [SRC-1AE03B9EC3-L003739](../../agents/web_agent.py#L3739) | 3739 | `"                        \"final_source_count\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L003740](../../agents/web_agent.py#L3740) | 3740 | `"                        \"final_independent_domain_count\": len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L003741](../../agents/web_agent.py#L3741) | 3741 | `"                        \"recovered\": not needs_corroboration,"` | — |
| [SRC-1AE03B9EC3-L003742](../../agents/web_agent.py#L3742) | 3742 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L003743](../../agents/web_agent.py#L3743) | 3743 | `"                    evidence_repair[\"reason\"] = ("` | — |
| [SRC-1AE03B9EC3-L003744](../../agents/web_agent.py#L3744) | 3744 | `"                        \"single_bounded_retry_still_insufficient\""` | — |
| [SRC-1AE03B9EC3-L003745](../../agents/web_agent.py#L3745) | 3745 | `"                        if needs_corroboration else \"evidence_gate_recovered\""` | — |
| [SRC-1AE03B9EC3-L003746](../../agents/web_agent.py#L3746) | 3746 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003747](../../agents/web_agent.py#L3747) | 3747 | `"                    report[\"queries_planned\"] = int(report.get(\"queries_planned\", 0) or 0) + int("` | — |
| [SRC-1AE03B9EC3-L003748](../../agents/web_agent.py#L3748) | 3748 | `"                        repair_report.get(\"queries_planned\", 1) or 0"` | — |
| [SRC-1AE03B9EC3-L003749](../../agents/web_agent.py#L3749) | 3749 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003750](../../agents/web_agent.py#L3750) | 3750 | `"                    initial_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L003751](../../agents/web_agent.py#L3751) | 3751 | `"                    repair_attempt_count = repair_report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L003752](../../agents/web_agent.py#L3752) | 3752 | `"                    if initial_attempt_count is None or repair_attempt_count is None:"` | — |
| [SRC-1AE03B9EC3-L003753](../../agents/web_agent.py#L3753) | 3753 | `"                        report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L003754](../../agents/web_agent.py#L3754) | 3754 | `"                        report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L003755](../../agents/web_agent.py#L3755) | 3755 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L003756](../../agents/web_agent.py#L3756) | 3756 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L003757](../../agents/web_agent.py#L3757) | 3757 | `"                            report[\"queries_attempted\"] = max(0, int(initial_attempt_count or 0)) + max("` | — |
| [SRC-1AE03B9EC3-L003758](../../agents/web_agent.py#L3758) | 3758 | `"                                0, int(repair_attempt_count or 0)"` | — |
| [SRC-1AE03B9EC3-L003759](../../agents/web_agent.py#L3759) | 3759 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L003760](../../agents/web_agent.py#L3760) | 3760 | `"                            report[\"queries_attempted_known\"] = True"` | — |
| [SRC-1AE03B9EC3-L003761](../../agents/web_agent.py#L3761) | 3761 | `"                        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L003762](../../agents/web_agent.py#L3762) | 3762 | `"                            report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L003763](../../agents/web_agent.py#L3763) | 3763 | `"                            report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L003764](../../agents/web_agent.py#L3764) | 3764 | `"                    report[\"query_results\"] = list(report.get(\"query_results\", [])) + list("` | — |
| [SRC-1AE03B9EC3-L003765](../../agents/web_agent.py#L3765) | 3765 | `"                        repair_report.get(\"query_results\", [])"` | — |
| [SRC-1AE03B9EC3-L003766](../../agents/web_agent.py#L3766) | 3766 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003767](../../agents/web_agent.py#L3767) | 3767 | `"                    merged_providers = {"` | — |
| [SRC-1AE03B9EC3-L003768](../../agents/web_agent.py#L3768) | 3768 | `"                        provider"` | — |
| [SRC-1AE03B9EC3-L003769](../../agents/web_agent.py#L3769) | 3769 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L003770](../../agents/web_agent.py#L3770) | 3770 | `"                        for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L003771](../../agents/web_agent.py#L3771) | 3771 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L003772](../../agents/web_agent.py#L3772) | 3772 | `"                    report[\"providers_used\"] = sorted(merged_providers)"` | — |
| [SRC-1AE03B9EC3-L003773](../../agents/web_agent.py#L3773) | 3773 | `"                    report[\"provider_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L003774](../../agents/web_agent.py#L3774) | 3774 | `"                        provider: sum("` | — |
| [SRC-1AE03B9EC3-L003775](../../agents/web_agent.py#L3775) | 3775 | `"                            provider in source.get(\"providers\", []) for source in sources"` | — |
| [SRC-1AE03B9EC3-L003776](../../agents/web_agent.py#L3776) | 3776 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003777](../../agents/web_agent.py#L3777) | 3777 | `"                        for provider in merged_providers"` | — |
| [SRC-1AE03B9EC3-L003778](../../agents/web_agent.py#L3778) | 3778 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L003779](../../agents/web_agent.py#L3779) | 3779 | `"                    report[\"platform_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L003780](../../agents/web_agent.py#L3780) | 3780 | `"                        str(source.get(\"platform\", \"web\")): sum("` | — |
| [SRC-1AE03B9EC3-L003781](../../agents/web_agent.py#L3781) | 3781 | `"                            str(other.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L003782](../../agents/web_agent.py#L3782) | 3782 | `"                            == str(source.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L003783](../../agents/web_agent.py#L3783) | 3783 | `"                            for other in sources"` | — |
| [SRC-1AE03B9EC3-L003784](../../agents/web_agent.py#L3784) | 3784 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L003785](../../agents/web_agent.py#L3785) | 3785 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L003786](../../agents/web_agent.py#L3786) | 3786 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L003787](../../agents/web_agent.py#L3787) | 3787 | `"                    report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L003788](../../agents/web_agent.py#L3788) | 3788 | `"                    report[\"pages_fetched\"] = sum("` | — |
| [SRC-1AE03B9EC3-L003789](../../agents/web_agent.py#L3789) | 3789 | `"                        bool(source.get(\"page_fetched\")) for source in sources"` | — |
| [SRC-1AE03B9EC3-L003790](../../agents/web_agent.py#L3790) | 3790 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003791](../../agents/web_agent.py#L3791) | 3791 | `"                    report[\"independent_sources\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L003792](../../agents/web_agent.py#L3792) | 3792 | `"                    report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L003793](../../agents/web_agent.py#L3793) | 3793 | `"                    report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L003794](../../agents/web_agent.py#L3794) | 3794 | `"                        sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L003795](../../agents/web_agent.py#L3795) | 3795 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003796](../../agents/web_agent.py#L3796) | 3796 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L003797](../../agents/web_agent.py#L3797) | 3797 | `"                    evidence_repair[\"reason\"] = \"repair_query_was_not_distinct\""` | — |
| [SRC-1AE03B9EC3-L003798](../../agents/web_agent.py#L3798) | 3798 | `"        report[\"evidence_repair\"] = evidence_repair"` | — |
| [SRC-1AE03B9EC3-L003799](../../agents/web_agent.py#L3799) | 3799 | `"        baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L003800](../../agents/web_agent.py#L3800) | 3800 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L003801](../../agents/web_agent.py#L3801) | 3801 | `"            current_research_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L003802](../../agents/web_agent.py#L3802) | 3802 | `"                item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L003803](../../agents/web_agent.py#L3803) | 3803 | `"                if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L003804](../../agents/web_agent.py#L3804) | 3804 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L003805](../../agents/web_agent.py#L3805) | 3805 | `"        report[\"provider_diagnostics\"] = current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L003806](../../agents/web_agent.py#L3806) | 3806 | `"        provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L003807](../../agents/web_agent.py#L3807) | 3807 | `"            item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L003808](../../agents/web_agent.py#L3808) | 3808 | `"            for item in current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L003809](../../agents/web_agent.py#L3809) | 3809 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003810](../../agents/web_agent.py#L3810) | 3810 | `"        raw_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L003811](../../agents/web_agent.py#L3811) | 3811 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L003812](../../agents/web_agent.py#L3812) | 3812 | `"            queries_attempted = ("` | — |
| [SRC-1AE03B9EC3-L003813](../../agents/web_agent.py#L3813) | 3813 | `"                None if raw_attempt_count is None"` | — |
| [SRC-1AE03B9EC3-L003814](../../agents/web_agent.py#L3814) | 3814 | `"                else max(0, int(raw_attempt_count or 0))"` | — |
| [SRC-1AE03B9EC3-L003815](../../agents/web_agent.py#L3815) | 3815 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003816](../../agents/web_agent.py#L3816) | 3816 | `"        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L003817](../../agents/web_agent.py#L3817) | 3817 | `"            queries_attempted = None"` | — |
| [SRC-1AE03B9EC3-L003818](../../agents/web_agent.py#L3818) | 3818 | `"        if queries_attempted is not None:"` | — |
| [SRC-1AE03B9EC3-L003819](../../agents/web_agent.py#L3819) | 3819 | `"            search_attempted = ("` | — |
| [SRC-1AE03B9EC3-L003820](../../agents/web_agent.py#L3820) | 3820 | `"                queries_attempted > 0"` | — |
| [SRC-1AE03B9EC3-L003821](../../agents/web_agent.py#L3821) | 3821 | `"                or provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L003822](../../agents/web_agent.py#L3822) | 3822 | `"                or report.get(\"search_attempted\") is True"` | — |
| [SRC-1AE03B9EC3-L003823](../../agents/web_agent.py#L3823) | 3823 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003824](../../agents/web_agent.py#L3824) | 3824 | `"        elif provider_attempt_observed or report.get(\"search_attempted\") is True:"` | — |
| [SRC-1AE03B9EC3-L003825](../../agents/web_agent.py#L3825) | 3825 | `"            search_attempted = True"` | — |
| [SRC-1AE03B9EC3-L003826](../../agents/web_agent.py#L3826) | 3826 | `"        elif isinstance(report.get(\"search_attempted\"), bool):"` | — |
| [SRC-1AE03B9EC3-L003827](../../agents/web_agent.py#L3827) | 3827 | `"            search_attempted = report[\"search_attempted\"]"` | — |
| [SRC-1AE03B9EC3-L003828](../../agents/web_agent.py#L3828) | 3828 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L003829](../../agents/web_agent.py#L3829) | 3829 | `"            search_attempted = None"` | — |
| [SRC-1AE03B9EC3-L003830](../../agents/web_agent.py#L3830) | 3830 | `"        report[\"queries_attempted\"] = queries_attempted"` | — |
| [SRC-1AE03B9EC3-L003831](../../agents/web_agent.py#L3831) | 3831 | `"        report[\"queries_attempted_known\"] = queries_attempted is not None"` | — |
| [SRC-1AE03B9EC3-L003832](../../agents/web_agent.py#L3832) | 3832 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L003833](../../agents/web_agent.py#L3833) | 3833 | `"        previous_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L003834](../../agents/web_agent.py#L3834) | 3834 | `"        if previous_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L003835](../../agents/web_agent.py#L3835) | 3835 | `"            if provider_attempt_observed or search_attempted is True:"` | — |
| [SRC-1AE03B9EC3-L003836](../../agents/web_agent.py#L3836) | 3836 | `"                search_outcome = \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L003837](../../agents/web_agent.py#L3837) | 3837 | `"            elif search_attempted is False:"` | — |
| [SRC-1AE03B9EC3-L003838](../../agents/web_agent.py#L3838) | 3838 | `"                search_outcome = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L003839](../../agents/web_agent.py#L3839) | 3839 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L003840](../../agents/web_agent.py#L3840) | 3840 | `"                search_outcome = \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L003841](../../agents/web_agent.py#L3841) | 3841 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L003842](../../agents/web_agent.py#L3842) | 3842 | `"            search_outcome = ("` | — |
| [SRC-1AE03B9EC3-L003843](../../agents/web_agent.py#L3843) | 3843 | `"                \"attempted_with_usable_sources\" if search_attempted is True and sources"` | — |
| [SRC-1AE03B9EC3-L003844](../../agents/web_agent.py#L3844) | 3844 | `"                else \"attempted_no_usable_sources\" if search_attempted is True"` | — |
| [SRC-1AE03B9EC3-L003845](../../agents/web_agent.py#L3845) | 3845 | `"                else \"not_attempted\" if search_attempted is False"` | — |
| [SRC-1AE03B9EC3-L003846](../../agents/web_agent.py#L3846) | 3846 | `"                else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L003847](../../agents/web_agent.py#L3847) | 3847 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003848](../../agents/web_agent.py#L3848) | 3848 | `"        report[\"search_outcome\"] = search_outcome"` | — |
| [SRC-1AE03B9EC3-L003849](../../agents/web_agent.py#L3849) | 3849 | `"        if search_outcome in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L003850](../../agents/web_agent.py#L3850) | 3850 | `"            report[\"usable_sources_after_filtering\"] = None"` | — |
| [SRC-1AE03B9EC3-L003851](../../agents/web_agent.py#L3851) | 3851 | `"            report[\"unique_sources\"] = None"` | — |
| [SRC-1AE03B9EC3-L003852](../../agents/web_agent.py#L3852) | 3852 | `"            report[\"pages_fetched\"] = None"` | — |
| [SRC-1AE03B9EC3-L003853](../../agents/web_agent.py#L3853) | 3853 | `"            report[\"provider_counts\"] = None"` | — |
| [SRC-1AE03B9EC3-L003854](../../agents/web_agent.py#L3854) | 3854 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L003855](../../agents/web_agent.py#L3855) | 3855 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L003856](../../agents/web_agent.py#L3856) | 3856 | `"            if report.get(\"unique_sources\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L003857](../../agents/web_agent.py#L3857) | 3857 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L003858](../../agents/web_agent.py#L3858) | 3858 | `"            if report.get(\"pages_fetched\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L003859](../../agents/web_agent.py#L3859) | 3859 | `"                report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L003860](../../agents/web_agent.py#L3860) | 3860 | `"        report[\"research_quality_semantics\"] = \"process_coverage_not_factual_probability\""` | — |
| [SRC-1AE03B9EC3-L003861](../../agents/web_agent.py#L3861) | 3861 | `"        report[\"distinct_registrable_domains\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L003862](../../agents/web_agent.py#L3862) | 3862 | `"        report[\"independent_sources\"] = len(independent_domains)  # Legacy alias; not editorial independence."` | — |
| [SRC-1AE03B9EC3-L003863](../../agents/web_agent.py#L3863) | 3863 | `"        report[\"independent_sources_field_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L003864](../../agents/web_agent.py#L3864) | 3864 | `"            \"legacy_compatibility_alias_for_distinct_registrable_domain_count\""` | — |
| [SRC-1AE03B9EC3-L003865](../../agents/web_agent.py#L3865) | 3865 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003866](../../agents/web_agent.py#L3866) | 3866 | `"        report[\"source_diversity_semantics\"] = ("` | — |
| [SRC-1AE03B9EC3-L003867](../../agents/web_agent.py#L3867) | 3867 | `"            \"distinct_registrable_domains_not_editorial_independence\""` | — |
| [SRC-1AE03B9EC3-L003868](../../agents/web_agent.py#L3868) | 3868 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003869](../../agents/web_agent.py#L3869) | 3869 | `"        report[\"editorial_independence_status\"] = \"not_assessed\""` | — |
| [SRC-1AE03B9EC3-L003870](../../agents/web_agent.py#L3870) | 3870 | `"        if len(independent_domains) >= 2:"` | — |
| [SRC-1AE03B9EC3-L003871](../../agents/web_agent.py#L3871) | 3871 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L003872](../../agents/web_agent.py#L3872) | 3872 | `"                \"تعدد النطاقات المسجلة لا يثبت الاستقلال التحريري؛ قد تنقل المواقع عن المصدر الأصلي نفسه.\""` | — |
