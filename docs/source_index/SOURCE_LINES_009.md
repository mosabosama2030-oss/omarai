# Omarai Source Lines

<!-- ملف مولّد آليًا بواسطة docs/generate_index.py؛ لا تعدّله يدويًا. -->

- الصفحة: **009**
- سجلات الأسطر: **800**
- النطاق: SRC-1AE03B9EC3-L003845 إلى SRC-1AE03B9EC3-L004644
- الفهرس الرئيسي: [SOURCE LINES INDEX](../SOURCE_LINES_INDEX.md)

## الوكيل والمنطق

### FILE-1AE03B9EC3 — [agents/web_agent.py](../../agents/web_agent.py#L1)

- النوع: **Python**
- نطاق الفهرسة: جرد الملف + AST Python

| كود السطر | السطر | النص الكامل للسطر | كود الوسم |
|---|---:|---|---|
| [SRC-1AE03B9EC3-L003845](../../agents/web_agent.py#L3845) | 3845 | `"                    result[\"search_report\"][\"answer_integrity\"] = answer_integrity"` | — |
| [SRC-1AE03B9EC3-L003846](../../agents/web_agent.py#L3846) | 3846 | `"                    result[\"search_report\"][\"task_fulfillment_status\"] = fulfillment_status"` | — |
| [SRC-1AE03B9EC3-L003847](../../agents/web_agent.py#L3847) | 3847 | `"            except (AttributeError, KeyError, TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L003848](../../agents/web_agent.py#L3848) | 3848 | `"                # Auxiliary integrity screening never replaces the actual answer."` | — |
| [SRC-1AE03B9EC3-L003849](../../agents/web_agent.py#L3849) | 3849 | `"                result[\"answer_integrity\"] = {"` | — |
| [SRC-1AE03B9EC3-L003850](../../agents/web_agent.py#L3850) | 3850 | `"                    \"method\": \"deterministic_lexical_screen_only\","` | — |
| [SRC-1AE03B9EC3-L003851](../../agents/web_agent.py#L3851) | 3851 | `"                    \"status\": \"not_run\","` | — |
| [SRC-1AE03B9EC3-L003852](../../agents/web_agent.py#L3852) | 3852 | `"                    \"semantic_verification\": False,"` | — |
| [SRC-1AE03B9EC3-L003853](../../agents/web_agent.py#L3853) | 3853 | `"                    \"independent_fact_check\": False,"` | — |
| [SRC-1AE03B9EC3-L003854](../../agents/web_agent.py#L3854) | 3854 | `"                    \"error_class\": \"integrity_screen_error\","` | — |
| [SRC-1AE03B9EC3-L003855](../../agents/web_agent.py#L3855) | 3855 | `"                }"` | — |
| [SRC-1AE03B9EC3-L003856](../../agents/web_agent.py#L3856) | 3856 | `"                result.setdefault(\"warnings\", []).append("` | — |
| [SRC-1AE03B9EC3-L003857](../../agents/web_agent.py#L3857) | 3857 | `"                    \"تعذر تشغيل الفحص اللفظي الأولي لسلامة الأدلة؛ لم يُعدّ ذلك إثباتًا أو نفيًا لصحة الإجابة.\""` | — |
| [SRC-1AE03B9EC3-L003858](../../agents/web_agent.py#L3858) | 3858 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003859](../../agents/web_agent.py#L3859) | 3859 | `"        if \"final_answer_status\" not in result:"` | — |
| [SRC-1AE03B9EC3-L003860](../../agents/web_agent.py#L3860) | 3860 | `"            if result.get(\"kind\") in {\"capability_answer\", \"local_conversation\"}:"` | — |
| [SRC-1AE03B9EC3-L003861](../../agents/web_agent.py#L3861) | 3861 | `"                final_answer_status = \"local_response_no_generation\""` | — |
| [SRC-1AE03B9EC3-L003862](../../agents/web_agent.py#L3862) | 3862 | `"            elif result.get(\"kind\") == \"insufficient_evidence\":"` | — |
| [SRC-1AE03B9EC3-L003863](../../agents/web_agent.py#L3863) | 3863 | `"                final_answer_status = \"insufficient_evidence_no_generation\""` | — |
| [SRC-1AE03B9EC3-L003864](../../agents/web_agent.py#L3864) | 3864 | `"            elif result.get(\"used_language_model\") is True:"` | — |
| [SRC-1AE03B9EC3-L003865](../../agents/web_agent.py#L3865) | 3865 | `"                final_answer_status = \"model_answer_generated\""` | — |
| [SRC-1AE03B9EC3-L003866](../../agents/web_agent.py#L3866) | 3866 | `"            elif self.generation_diagnostics:"` | — |
| [SRC-1AE03B9EC3-L003867](../../agents/web_agent.py#L3867) | 3867 | `"                final_answer_status = ("` | — |
| [SRC-1AE03B9EC3-L003868](../../agents/web_agent.py#L3868) | 3868 | `"                    \"generation_failed_with_source_fallback\""` | — |
| [SRC-1AE03B9EC3-L003869](../../agents/web_agent.py#L3869) | 3869 | `"                    if result.get(\"sources\")"` | — |
| [SRC-1AE03B9EC3-L003870](../../agents/web_agent.py#L3870) | 3870 | `"                    else \"generation_failed\""` | — |
| [SRC-1AE03B9EC3-L003871](../../agents/web_agent.py#L3871) | 3871 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003872](../../agents/web_agent.py#L3872) | 3872 | `"            elif result.get(\"kind\") == \"clarification\":"` | — |
| [SRC-1AE03B9EC3-L003873](../../agents/web_agent.py#L3873) | 3873 | `"                final_answer_status = \"clarification_required\""` | — |
| [SRC-1AE03B9EC3-L003874](../../agents/web_agent.py#L3874) | 3874 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L003875](../../agents/web_agent.py#L3875) | 3875 | `"                final_answer_status = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L003876](../../agents/web_agent.py#L3876) | 3876 | `"            result[\"final_answer_status\"] = final_answer_status"` | — |
| [SRC-1AE03B9EC3-L003877](../../agents/web_agent.py#L3877) | 3877 | `"        if isinstance(result.get(\"search_report\"), dict):"` | — |
| [SRC-1AE03B9EC3-L003878](../../agents/web_agent.py#L3878) | 3878 | `"            result[\"search_report\"][\"request_budget\"] = budget_summary"` | — |
| [SRC-1AE03B9EC3-L003879](../../agents/web_agent.py#L3879) | 3879 | `"        if budget_summary[\"deadline_exceeded\"]:"` | — |
| [SRC-1AE03B9EC3-L003880](../../agents/web_agent.py#L3880) | 3880 | `"            result.setdefault(\"warnings\", []).append("` | — |
| [SRC-1AE03B9EC3-L003881](../../agents/web_agent.py#L3881) | 3881 | `"                \"انتهت نافذة الوقت المحددة للطلب أو جرى تجاوزها قليلًا أثناء إنهاء اتصال جارٍ.\""` | — |
| [SRC-1AE03B9EC3-L003882](../../agents/web_agent.py#L3882) | 3882 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003883](../../agents/web_agent.py#L3883) | 3883 | `"        return result"` | — |
| [SRC-1AE03B9EC3-L003884](../../agents/web_agent.py#L3884) | 3884 | `""` | — |
| [SRC-1AE03B9EC3-L003885](../../agents/web_agent.py#L3885) | 3885 | `"    def _answer_with_budget("` | — |
| [SRC-1AE03B9EC3-L003886](../../agents/web_agent.py#L3886) | 3886 | `"        self, question: str, history: Any = None, mode: str = \"auto\""` | — |
| [SRC-1AE03B9EC3-L003887](../../agents/web_agent.py#L3887) | 3887 | `"    ) -> dict[str, Any]:"` | — |
| [SRC-1AE03B9EC3-L003888](../../agents/web_agent.py#L3888) | 3888 | `"        if not isinstance(question, str) or not question.strip():"` | — |
| [SRC-1AE03B9EC3-L003889](../../agents/web_agent.py#L3889) | 3889 | `"            raise ValueError(\"اكتب سؤالًا غير فارغ.\")"` | — |
| [SRC-1AE03B9EC3-L003890](../../agents/web_agent.py#L3890) | 3890 | `"        question = question.strip()"` | — |
| [SRC-1AE03B9EC3-L003891](../../agents/web_agent.py#L3891) | 3891 | `"        if len(question) > MAX_QUESTION_CHARS:"` | — |
| [SRC-1AE03B9EC3-L003892](../../agents/web_agent.py#L3892) | 3892 | `"            raise ValueError(f\"السؤال طويل جدًا؛ الحد الأقصى {MAX_QUESTION_CHARS} حرف.\")"` | — |
| [SRC-1AE03B9EC3-L003893](../../agents/web_agent.py#L3893) | 3893 | `"        clean_history = self._sanitize_history(history)"` | — |
| [SRC-1AE03B9EC3-L003894](../../agents/web_agent.py#L3894) | 3894 | `"        self._reset_deepseek_search_budget()"` | — |
| [SRC-1AE03B9EC3-L003895](../../agents/web_agent.py#L3895) | 3895 | `"        self.server_search_sources = []"` | — |
| [SRC-1AE03B9EC3-L003896](../../agents/web_agent.py#L3896) | 3896 | `"        self.model_usage = []"` | — |
| [SRC-1AE03B9EC3-L003897](../../agents/web_agent.py#L3897) | 3897 | `"        self.generation_diagnostics = []"` | — |
| [SRC-1AE03B9EC3-L003898](../../agents/web_agent.py#L3898) | 3898 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L003899](../../agents/web_agent.py#L3899) | 3899 | `"            self._provider_diagnostics = []"` | — |
| [SRC-1AE03B9EC3-L003900](../../agents/web_agent.py#L3900) | 3900 | `"        clean_mode = mode.strip().lower() if isinstance(mode, str) else \"auto\""` | — |
| [SRC-1AE03B9EC3-L003901](../../agents/web_agent.py#L3901) | 3901 | `"        if clean_mode not in {\"auto\", \"deep\", \"latest\", \"social\"}:"` | — |
| [SRC-1AE03B9EC3-L003902](../../agents/web_agent.py#L3902) | 3902 | `"            raise ValueError(\"نمط البحث غير مدعوم. اختر auto أو deep أو latest أو social.\")"` | — |
| [SRC-1AE03B9EC3-L003903](../../agents/web_agent.py#L3903) | 3903 | `"        current_search_status_question = self._is_current_search_status_question(question)"` | — |
| [SRC-1AE03B9EC3-L003904](../../agents/web_agent.py#L3904) | 3904 | `"        # Explicit UI modes control research tasks, but must not turn a status"` | — |
| [SRC-1AE03B9EC3-L003905](../../agents/web_agent.py#L3905) | 3905 | `"        # question about this answer into a new web-search request."` | — |
| [SRC-1AE03B9EC3-L003906](../../agents/web_agent.py#L3906) | 3906 | `"        routing_mode = \"auto\" if current_search_status_question else clean_mode"` | — |
| [SRC-1AE03B9EC3-L003907](../../agents/web_agent.py#L3907) | 3907 | `"        decision = route_intent("` | — |
| [SRC-1AE03B9EC3-L003908](../../agents/web_agent.py#L3908) | 3908 | `"            question,"` | — |
| [SRC-1AE03B9EC3-L003909](../../agents/web_agent.py#L3909) | 3909 | `"            clean_history,"` | — |
| [SRC-1AE03B9EC3-L003910](../../agents/web_agent.py#L3910) | 3910 | `"            routing_mode,"` | — |
| [SRC-1AE03B9EC3-L003911](../../agents/web_agent.py#L3911) | 3911 | `"            capability_question=self._is_self_question(question),"` | — |
| [SRC-1AE03B9EC3-L003912](../../agents/web_agent.py#L3912) | 3912 | `"            requires_web=self._requires_web_research(question, routing_mode),"` | — |
| [SRC-1AE03B9EC3-L003913](../../agents/web_agent.py#L3913) | 3913 | `"        )"` | — |
| [SRC-1AE03B9EC3-L003914](../../agents/web_agent.py#L3914) | 3914 | `"        intent_route = str(decision[\"route\"])"` | — |
| [SRC-1AE03B9EC3-L003915](../../agents/web_agent.py#L3915) | 3915 | `"        intent_reason = str(decision[\"reason\"])"` | — |
| [SRC-1AE03B9EC3-L003916](../../agents/web_agent.py#L3916) | 3916 | `""` | — |
| [SRC-1AE03B9EC3-L003917](../../agents/web_agent.py#L3917) | 3917 | `"        if intent_route == \"LOCAL\":"` | — |
| [SRC-1AE03B9EC3-L003918](../../agents/web_agent.py#L3918) | 3918 | `"            if self._is_self_question(question):"` | — |
| [SRC-1AE03B9EC3-L003919](../../agents/web_agent.py#L3919) | 3919 | `"                local_result = self._self_description_answer(question)"` | — |
| [SRC-1AE03B9EC3-L003920](../../agents/web_agent.py#L3920) | 3920 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L003921](../../agents/web_agent.py#L3921) | 3921 | `"                local_result = self._local_answer_result("` | — |
| [SRC-1AE03B9EC3-L003922](../../agents/web_agent.py#L3922) | 3922 | `"                    question, self._local_conversation_reply(question), \"local_conversation\""` | — |
| [SRC-1AE03B9EC3-L003923](../../agents/web_agent.py#L3923) | 3923 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003924](../../agents/web_agent.py#L3924) | 3924 | `"            return self._annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L003925](../../agents/web_agent.py#L3925) | 3925 | `"                local_result, intent_route, intent_reason, clean_mode"` | — |
| [SRC-1AE03B9EC3-L003926](../../agents/web_agent.py#L3926) | 3926 | `"            )"` | — |
| [SRC-1AE03B9EC3-L003927](../../agents/web_agent.py#L3927) | 3927 | `""` | — |
| [SRC-1AE03B9EC3-L003928](../../agents/web_agent.py#L3928) | 3928 | `"        if intent_route == \"CLARIFY\":"` | — |
| [SRC-1AE03B9EC3-L003929](../../agents/web_agent.py#L3929) | 3929 | `"            return self._clarification_result(question, clean_mode, decision)"` | — |
| [SRC-1AE03B9EC3-L003930](../../agents/web_agent.py#L3930) | 3930 | `""` | — |
| [SRC-1AE03B9EC3-L003931](../../agents/web_agent.py#L3931) | 3931 | `"        if intent_route == \"MODEL_ONLY\":"` | — |
| [SRC-1AE03B9EC3-L003932](../../agents/web_agent.py#L3932) | 3932 | `"            general_answer = self._answer_without_search(question, clean_history)"` | — |
| [SRC-1AE03B9EC3-L003933](../../agents/web_agent.py#L3933) | 3933 | `"            if general_answer is not None:"` | — |
| [SRC-1AE03B9EC3-L003934](../../agents/web_agent.py#L3934) | 3934 | `"                return self._annotate_intent_route("` | — |
| [SRC-1AE03B9EC3-L003935](../../agents/web_agent.py#L3935) | 3935 | `"                    general_answer, intent_route, intent_reason, clean_mode"` | — |
| [SRC-1AE03B9EC3-L003936](../../agents/web_agent.py#L3936) | 3936 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003937](../../agents/web_agent.py#L3937) | 3937 | `"            # Preserve the existing degraded-mode behavior when generation is unavailable:"` | — |
| [SRC-1AE03B9EC3-L003938](../../agents/web_agent.py#L3938) | 3938 | `"            # run the current web pipeline rather than fabricate a model-only answer."` | — |
| [SRC-1AE03B9EC3-L003939](../../agents/web_agent.py#L3939) | 3939 | `"            intent_route = \"WEB_SIMPLE\""` | — |
| [SRC-1AE03B9EC3-L003940](../../agents/web_agent.py#L3940) | 3940 | `"            intent_reason = \"model_unavailable_fallback_to_existing_web_research\""` | — |
| [SRC-1AE03B9EC3-L003941](../../agents/web_agent.py#L3941) | 3941 | `""` | — |
| [SRC-1AE03B9EC3-L003942](../../agents/web_agent.py#L3942) | 3942 | `"        plan = self._plan_search(question, clean_history)"` | — |
| [SRC-1AE03B9EC3-L003943](../../agents/web_agent.py#L3943) | 3943 | `"        plan[\"mode\"] = clean_mode"` | — |
| [SRC-1AE03B9EC3-L003944](../../agents/web_agent.py#L3944) | 3944 | `"        plan[\"intent_route\"] = intent_route"` | — |
| [SRC-1AE03B9EC3-L003945](../../agents/web_agent.py#L3945) | 3945 | `"        plan[\"intent_route_reason\"] = intent_reason"` | — |
| [SRC-1AE03B9EC3-L003946](../../agents/web_agent.py#L3946) | 3946 | `"        # Normalize planner output before depth/mode expansion so a raw instruction-only"` | — |
| [SRC-1AE03B9EC3-L003947](../../agents/web_agent.py#L3947) | 3947 | `"        # prompt cannot seed synthetic generic queries when the topic is empty."` | — |
| [SRC-1AE03B9EC3-L003948](../../agents/web_agent.py#L3948) | 3948 | `"        raw_plan_queries = plan.get(\"queries\") or []"` | — |
| [SRC-1AE03B9EC3-L003949](../../agents/web_agent.py#L3949) | 3949 | `"        if not isinstance(raw_plan_queries, list):"` | — |
| [SRC-1AE03B9EC3-L003950](../../agents/web_agent.py#L3950) | 3950 | `"            raw_plan_queries = []"` | — |
| [SRC-1AE03B9EC3-L003951](../../agents/web_agent.py#L3951) | 3951 | `"        normalized_plan_queries = []"` | — |
| [SRC-1AE03B9EC3-L003952](../../agents/web_agent.py#L3952) | 3952 | `"        for raw_query in raw_plan_queries:"` | — |
| [SRC-1AE03B9EC3-L003953](../../agents/web_agent.py#L3953) | 3953 | `"            if not isinstance(raw_query, str) or not raw_query.strip():"` | — |
| [SRC-1AE03B9EC3-L003954](../../agents/web_agent.py#L3954) | 3954 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L003955](../../agents/web_agent.py#L3955) | 3955 | `"            compacted_query = compact_search_query(raw_query)"` | — |
| [SRC-1AE03B9EC3-L003956](../../agents/web_agent.py#L3956) | 3956 | `"            if ("` | — |
| [SRC-1AE03B9EC3-L003957](../../agents/web_agent.py#L3957) | 3957 | `"                compacted_query"` | — |
| [SRC-1AE03B9EC3-L003958](../../agents/web_agent.py#L3958) | 3958 | `"                and _relevance_query_tokens(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L003959](../../agents/web_agent.py#L3959) | 3959 | `"                and compacted_query not in normalized_plan_queries"` | — |
| [SRC-1AE03B9EC3-L003960](../../agents/web_agent.py#L3960) | 3960 | `"            ):"` | — |
| [SRC-1AE03B9EC3-L003961](../../agents/web_agent.py#L3961) | 3961 | `"                normalized_plan_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L003962](../../agents/web_agent.py#L3962) | 3962 | `"        plan[\"queries\"] = normalized_plan_queries[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L003963](../../agents/web_agent.py#L3963) | 3963 | `"        # Preserve the requested mode in diagnostics even when no usable query exists."` | — |
| [SRC-1AE03B9EC3-L003964](../../agents/web_agent.py#L3964) | 3964 | `"        if clean_mode == \"deep\":"` | — |
| [SRC-1AE03B9EC3-L003965](../../agents/web_agent.py#L3965) | 3965 | `"            plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L003966](../../agents/web_agent.py#L3966) | 3966 | `"        elif clean_mode == \"latest\":"` | — |
| [SRC-1AE03B9EC3-L003967](../../agents/web_agent.py#L3967) | 3967 | `"            plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L003968](../../agents/web_agent.py#L3968) | 3968 | `"        elif clean_mode == \"social\":"` | — |
| [SRC-1AE03B9EC3-L003969](../../agents/web_agent.py#L3969) | 3969 | `"            plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L003970](../../agents/web_agent.py#L3970) | 3970 | `"            if not plan.get(\"platforms\"):"` | — |
| [SRC-1AE03B9EC3-L003971](../../agents/web_agent.py#L3971) | 3971 | `"                plan[\"platforms\"] = [\"reddit\", \"bluesky\", \"youtube\"]"` | — |
| [SRC-1AE03B9EC3-L003972](../../agents/web_agent.py#L3972) | 3972 | `""` | — |
| [SRC-1AE03B9EC3-L003973](../../agents/web_agent.py#L3973) | 3973 | `"        if plan.get(\"queries\"):"` | — |
| [SRC-1AE03B9EC3-L003974](../../agents/web_agent.py#L3974) | 3974 | `"            if clean_mode == \"auto\" and intent_route == \"WEB_DEEP\":"` | — |
| [SRC-1AE03B9EC3-L003975](../../agents/web_agent.py#L3975) | 3975 | `"                plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L003976](../../agents/web_agent.py#L3976) | 3976 | `"            if clean_mode == \"auto\":"` | — |
| [SRC-1AE03B9EC3-L003977](../../agents/web_agent.py#L3977) | 3977 | `"                normalized_question = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L003978](../../agents/web_agent.py#L3978) | 3978 | `"                deep_terms = ("` | — |
| [SRC-1AE03B9EC3-L003979](../../agents/web_agent.py#L3979) | 3979 | `"                    \"بحث عميق\", \"بحث معمق\", \"بحث شامل\", \"بالتفصيل\", \"قارن\", \"مقارنة\","` | — |
| [SRC-1AE03B9EC3-L003980](../../agents/web_agent.py#L3980) | 3980 | `"                    \"تحقق\", \"استقصاء\", \"deep research\", \"comprehensive\", \"in-depth\", \"compare\","` | — |
| [SRC-1AE03B9EC3-L003981](../../agents/web_agent.py#L3981) | 3981 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003982](../../agents/web_agent.py#L3982) | 3982 | `"                explicit_deep = intent_route == \"WEB_DEEP\" or any("` | — |
| [SRC-1AE03B9EC3-L003983](../../agents/web_agent.py#L3983) | 3983 | `"                    term in normalized_question for term in deep_terms"` | — |
| [SRC-1AE03B9EC3-L003984](../../agents/web_agent.py#L3984) | 3984 | `"                )"` | — |
| [SRC-1AE03B9EC3-L003985](../../agents/web_agent.py#L3985) | 3985 | `"                if not explicit_deep:"` | — |
| [SRC-1AE03B9EC3-L003986](../../agents/web_agent.py#L3986) | 3986 | `"                    # The planner may overclassify short lookups as deep research. Preserve"` | — |
| [SRC-1AE03B9EC3-L003987](../../agents/web_agent.py#L3987) | 3987 | `"                    # the user's actual intent first and cap routine searches to three queries."` | — |
| [SRC-1AE03B9EC3-L003988](../../agents/web_agent.py#L3988) | 3988 | `"                    fallback_plan_queries = ("` | — |
| [SRC-1AE03B9EC3-L003989](../../agents/web_agent.py#L3989) | 3989 | `"                        fallback_plan(question, clean_history).get(\"queries\") or []"` | — |
| [SRC-1AE03B9EC3-L003990](../../agents/web_agent.py#L3990) | 3990 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L003991](../../agents/web_agent.py#L3991) | 3991 | `"                    fallback_queries = ["` | — |
| [SRC-1AE03B9EC3-L003992](../../agents/web_agent.py#L3992) | 3992 | `"                        compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L003993](../../agents/web_agent.py#L3993) | 3993 | `"                        for query in fallback_plan_queries"` | — |
| [SRC-1AE03B9EC3-L003994](../../agents/web_agent.py#L3994) | 3994 | `"                        if isinstance(query, str)"` | — |
| [SRC-1AE03B9EC3-L003995](../../agents/web_agent.py#L3995) | 3995 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L003996](../../agents/web_agent.py#L3996) | 3996 | `"                    fallback_queries = [query for query in fallback_queries if query]"` | — |
| [SRC-1AE03B9EC3-L003997](../../agents/web_agent.py#L3997) | 3997 | `"                    model_queries = ["` | — |
| [SRC-1AE03B9EC3-L003998](../../agents/web_agent.py#L3998) | 3998 | `"                        compact_search_query(query)"` | — |
| [SRC-1AE03B9EC3-L003999](../../agents/web_agent.py#L3999) | 3999 | `"                        for query in (plan.get(\"queries\") or [])"` | — |
| [SRC-1AE03B9EC3-L004000](../../agents/web_agent.py#L4000) | 4000 | `"                        if isinstance(query, str)"` | — |
| [SRC-1AE03B9EC3-L004001](../../agents/web_agent.py#L4001) | 4001 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L004002](../../agents/web_agent.py#L4002) | 4002 | `"                    model_queries = [query for query in model_queries if query]"` | — |
| [SRC-1AE03B9EC3-L004003](../../agents/web_agent.py#L4003) | 4003 | `"                    if self._is_navigation_request(question):"` | — |
| [SRC-1AE03B9EC3-L004004](../../agents/web_agent.py#L4004) | 4004 | `"                        navigation_seed = ("` | — |
| [SRC-1AE03B9EC3-L004005](../../agents/web_agent.py#L4005) | 4005 | `"                            fallback_queries[0] if fallback_queries"` | — |
| [SRC-1AE03B9EC3-L004006](../../agents/web_agent.py#L4006) | 4006 | `"                            else model_queries[0] if model_queries"` | — |
| [SRC-1AE03B9EC3-L004007](../../agents/web_agent.py#L4007) | 4007 | `"                            else \"\""` | — |
| [SRC-1AE03B9EC3-L004008](../../agents/web_agent.py#L4008) | 4008 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004009](../../agents/web_agent.py#L4009) | 4009 | `"                        subject = re.sub("` | — |
| [SRC-1AE03B9EC3-L004010](../../agents/web_agent.py#L4010) | 4010 | `"                            r\"^(?:ابحث\|بحث\|دور\|اعثر)\\s+(?:عن\|على)?\\s*\","` | — |
| [SRC-1AE03B9EC3-L004011](../../agents/web_agent.py#L4011) | 4011 | `"                            \"\","` | — |
| [SRC-1AE03B9EC3-L004012](../../agents/web_agent.py#L4012) | 4012 | `"                            navigation_seed,"` | — |
| [SRC-1AE03B9EC3-L004013](../../agents/web_agent.py#L4013) | 4013 | `"                        ).strip()"` | — |
| [SRC-1AE03B9EC3-L004014](../../agents/web_agent.py#L4014) | 4014 | `"                        plan_queries = ("` | — |
| [SRC-1AE03B9EC3-L004015](../../agents/web_agent.py#L4015) | 4015 | `"                            ["` | — |
| [SRC-1AE03B9EC3-L004016](../../agents/web_agent.py#L4016) | 4016 | `"                                subject,"` | — |
| [SRC-1AE03B9EC3-L004017](../../agents/web_agent.py#L4017) | 4017 | `"                                subject + \" الموقع الرسمي\","` | — |
| [SRC-1AE03B9EC3-L004018](../../agents/web_agent.py#L4018) | 4018 | `"                                subject + \" official website\","` | — |
| [SRC-1AE03B9EC3-L004019](../../agents/web_agent.py#L4019) | 4019 | `"                            ]"` | — |
| [SRC-1AE03B9EC3-L004020](../../agents/web_agent.py#L4020) | 4020 | `"                            if subject else []"` | — |
| [SRC-1AE03B9EC3-L004021](../../agents/web_agent.py#L4021) | 4021 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004022](../../agents/web_agent.py#L4022) | 4022 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L004023](../../agents/web_agent.py#L4023) | 4023 | `"                        plan_queries = (fallback_queries[:1] or model_queries[:1]) + model_queries"` | — |
| [SRC-1AE03B9EC3-L004024](../../agents/web_agent.py#L4024) | 4024 | `"                    plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004025](../../agents/web_agent.py#L4025) | 4025 | `"                        query.strip() for query in plan_queries if isinstance(query, str) and query.strip()"` | — |
| [SRC-1AE03B9EC3-L004026](../../agents/web_agent.py#L4026) | 4026 | `"                    ))[:3]"` | — |
| [SRC-1AE03B9EC3-L004027](../../agents/web_agent.py#L4027) | 4027 | `"                    plan[\"depth\"] = \"standard\""` | — |
| [SRC-1AE03B9EC3-L004028](../../agents/web_agent.py#L4028) | 4028 | `"            base_query = (plan.get(\"queries\") or [\"\"])[0]"` | — |
| [SRC-1AE03B9EC3-L004029](../../agents/web_agent.py#L4029) | 4029 | `"            if clean_mode == \"auto\" and intent_route == \"WEB_DEEP\" and base_query:"` | — |
| [SRC-1AE03B9EC3-L004030](../../agents/web_agent.py#L4030) | 4030 | `"                deep_candidates = ["` | — |
| [SRC-1AE03B9EC3-L004031](../../agents/web_agent.py#L4031) | 4031 | `"                    f\"{base_query} official sources evidence\","` | — |
| [SRC-1AE03B9EC3-L004032](../../agents/web_agent.py#L4032) | 4032 | `"                    f\"{base_query} risks limitations alternatives\","` | — |
| [SRC-1AE03B9EC3-L004033](../../agents/web_agent.py#L4033) | 4033 | `"                    f\"{base_query} recent data reviews comparison\","` | — |
| [SRC-1AE03B9EC3-L004034](../../agents/web_agent.py#L4034) | 4034 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004035](../../agents/web_agent.py#L4035) | 4035 | `"                normalized_question = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L004036](../../agents/web_agent.py#L4036) | 4036 | `"                property_terms = ("` | — |
| [SRC-1AE03B9EC3-L004037](../../agents/web_agent.py#L4037) | 4037 | `"                    \"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"فيلا\", \"فلل\","` | — |
| [SRC-1AE03B9EC3-L004038](../../agents/web_agent.py#L4038) | 4038 | `"                    \"apartment\", \"apartments\", \"flat\", \"real estate\", \"property\", \"house\", \"villa\","` | — |
| [SRC-1AE03B9EC3-L004039](../../agents/web_agent.py#L4039) | 4039 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004040](../../agents/web_agent.py#L4040) | 4040 | `"                if self._is_listing_discovery(question) and any("` | — |
| [SRC-1AE03B9EC3-L004041](../../agents/web_agent.py#L4041) | 4041 | `"                    term in normalized_question for term in property_terms"` | — |
| [SRC-1AE03B9EC3-L004042](../../agents/web_agent.py#L4042) | 4042 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004043](../../agents/web_agent.py#L4043) | 4043 | `"                    deep_candidates.extend(["` | — |
| [SRC-1AE03B9EC3-L004044](../../agents/web_agent.py#L4044) | 4044 | `"                        f\"{base_query} إعلانات عقارية ومواقع العقارات\","` | — |
| [SRC-1AE03B9EC3-L004045](../../agents/web_agent.py#L4045) | 4045 | `"                        f\"{base_query} متوسط أسعار السوق للمتر\","` | — |
| [SRC-1AE03B9EC3-L004046](../../agents/web_agent.py#L4046) | 4046 | `"                        f\"{base_query} مواصفات الوحدات والمساحات وطرق السداد\","` | — |
| [SRC-1AE03B9EC3-L004047](../../agents/web_agent.py#L4047) | 4047 | `"                    ])"` | — |
| [SRC-1AE03B9EC3-L004048](../../agents/web_agent.py#L4048) | 4048 | `"                plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004049](../../agents/web_agent.py#L4049) | 4049 | `"                    (plan.get(\"queries\") or [])[:5] + deep_candidates"` | — |
| [SRC-1AE03B9EC3-L004050](../../agents/web_agent.py#L4050) | 4050 | `"                ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004051](../../agents/web_agent.py#L4051) | 4051 | `"                base_query = (plan.get(\"queries\") or [\"\"])[0]"` | — |
| [SRC-1AE03B9EC3-L004052](../../agents/web_agent.py#L4052) | 4052 | `"            # Explicit user-selected modes are control inputs. They do not bypass source"` | — |
| [SRC-1AE03B9EC3-L004053](../../agents/web_agent.py#L4053) | 4053 | `"            # validation and never permit private-source access."` | — |
| [SRC-1AE03B9EC3-L004054](../../agents/web_agent.py#L4054) | 4054 | `"            if clean_mode == \"deep\":"` | — |
| [SRC-1AE03B9EC3-L004055](../../agents/web_agent.py#L4055) | 4055 | `"                plan[\"depth\"] = \"deep\""` | — |
| [SRC-1AE03B9EC3-L004056](../../agents/web_agent.py#L4056) | 4056 | `"                candidates = ["` | — |
| [SRC-1AE03B9EC3-L004057](../../agents/web_agent.py#L4057) | 4057 | `"                    f\"{base_query} official sources data reports\","` | — |
| [SRC-1AE03B9EC3-L004058](../../agents/web_agent.py#L4058) | 4058 | `"                    f\"{base_query} risks limitations alternatives\","` | — |
| [SRC-1AE03B9EC3-L004059](../../agents/web_agent.py#L4059) | 4059 | `"                    f\"{base_query} case studies recent analysis\","` | — |
| [SRC-1AE03B9EC3-L004060](../../agents/web_agent.py#L4060) | 4060 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004061](../../agents/web_agent.py#L4061) | 4061 | `"                normalized_question = _normalize_search_query(question).casefold()"` | — |
| [SRC-1AE03B9EC3-L004062](../../agents/web_agent.py#L4062) | 4062 | `"                property_terms = ("` | — |
| [SRC-1AE03B9EC3-L004063](../../agents/web_agent.py#L4063) | 4063 | `"                    \"شقه\", \"شقق\", \"عقار\", \"عقارات\", \"فيلا\", \"فلل\","` | — |
| [SRC-1AE03B9EC3-L004064](../../agents/web_agent.py#L4064) | 4064 | `"                    \"apartment\", \"apartments\", \"flat\", \"real estate\", \"property\", \"house\", \"villa\","` | — |
| [SRC-1AE03B9EC3-L004065](../../agents/web_agent.py#L4065) | 4065 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004066](../../agents/web_agent.py#L4066) | 4066 | `"                if self._is_listing_discovery(question) and any("` | — |
| [SRC-1AE03B9EC3-L004067](../../agents/web_agent.py#L4067) | 4067 | `"                    term in normalized_question for term in property_terms"` | — |
| [SRC-1AE03B9EC3-L004068](../../agents/web_agent.py#L4068) | 4068 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004069](../../agents/web_agent.py#L4069) | 4069 | `"                    candidates.extend(["` | — |
| [SRC-1AE03B9EC3-L004070](../../agents/web_agent.py#L4070) | 4070 | `"                        f\"{base_query} إعلانات عقارية ومواقع العقارات\","` | — |
| [SRC-1AE03B9EC3-L004071](../../agents/web_agent.py#L4071) | 4071 | `"                        f\"{base_query} متوسط أسعار السوق للمتر\","` | — |
| [SRC-1AE03B9EC3-L004072](../../agents/web_agent.py#L4072) | 4072 | `"                        f\"{base_query} مواصفات الوحدات والمساحات وطرق السداد\","` | — |
| [SRC-1AE03B9EC3-L004073](../../agents/web_agent.py#L4073) | 4073 | `"                    ])"` | — |
| [SRC-1AE03B9EC3-L004074](../../agents/web_agent.py#L4074) | 4074 | `"                # Keep query budget for evidence-gap searches if first-round coverage is weak."` | — |
| [SRC-1AE03B9EC3-L004075](../../agents/web_agent.py#L4075) | 4075 | `"                plan[\"queries\"] = list(dict.fromkeys((plan.get(\"queries\") or [])[:3] + candidates))["` | — |
| [SRC-1AE03B9EC3-L004076](../../agents/web_agent.py#L4076) | 4076 | `"                    :MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L004077](../../agents/web_agent.py#L4077) | 4077 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004078](../../agents/web_agent.py#L4078) | 4078 | `"            elif clean_mode == \"latest\":"` | — |
| [SRC-1AE03B9EC3-L004079](../../agents/web_agent.py#L4079) | 4079 | `"                plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L004080](../../agents/web_agent.py#L4080) | 4080 | `"                if self._is_navigation_request(question):"` | — |
| [SRC-1AE03B9EC3-L004081](../../agents/web_agent.py#L4081) | 4081 | `"                    # Preserve link-finding intent in the latest mode. Appending broad"` | — |
| [SRC-1AE03B9EC3-L004082](../../agents/web_agent.py#L4082) | 4082 | `"                    # news modifiers here can turn \"find the official website\" into"` | — |
| [SRC-1AE03B9EC3-L004083](../../agents/web_agent.py#L4083) | 4083 | `"                    # a news-search task and hide the destination the user requested."` | — |
| [SRC-1AE03B9EC3-L004084](../../agents/web_agent.py#L4084) | 4084 | `"                    candidates = ["` | — |
| [SRC-1AE03B9EC3-L004085](../../agents/web_agent.py#L4085) | 4085 | `"                        base_query,"` | — |
| [SRC-1AE03B9EC3-L004086](../../agents/web_agent.py#L4086) | 4086 | `"                        f\"{base_query} الموقع الرسمي\","` | — |
| [SRC-1AE03B9EC3-L004087](../../agents/web_agent.py#L4087) | 4087 | `"                        f\"{base_query} official website\","` | — |
| [SRC-1AE03B9EC3-L004088](../../agents/web_agent.py#L4088) | 4088 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L004089](../../agents/web_agent.py#L4089) | 4089 | `"                    plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004090](../../agents/web_agent.py#L4090) | 4090 | `"                        candidates + (plan.get(\"queries\") or [])[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004091](../../agents/web_agent.py#L4091) | 4091 | `"                    ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004092](../../agents/web_agent.py#L4092) | 4092 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L004093](../../agents/web_agent.py#L4093) | 4093 | `"                    candidates = ["` | — |
| [SRC-1AE03B9EC3-L004094](../../agents/web_agent.py#L4094) | 4094 | `"                        f\"{base_query} latest news updates {dt.datetime.now().year}\","` | — |
| [SRC-1AE03B9EC3-L004095](../../agents/web_agent.py#L4095) | 4095 | `"                        f\"{base_query} recent official announcement\","` | — |
| [SRC-1AE03B9EC3-L004096](../../agents/web_agent.py#L4096) | 4096 | `"                    ]"` | — |
| [SRC-1AE03B9EC3-L004097](../../agents/web_agent.py#L4097) | 4097 | `"                    plan[\"queries\"] = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004098](../../agents/web_agent.py#L4098) | 4098 | `"                        (plan.get(\"queries\") or [])[:6] + candidates"` | — |
| [SRC-1AE03B9EC3-L004099](../../agents/web_agent.py#L4099) | 4099 | `"                    ))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004100](../../agents/web_agent.py#L4100) | 4100 | `"            elif clean_mode == \"social\":"` | — |
| [SRC-1AE03B9EC3-L004101](../../agents/web_agent.py#L4101) | 4101 | `"                plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L004102](../../agents/web_agent.py#L4102) | 4102 | `"                if not plan.get(\"platforms\"):"` | — |
| [SRC-1AE03B9EC3-L004103](../../agents/web_agent.py#L4103) | 4103 | `"                    plan[\"platforms\"] = [\"reddit\", \"bluesky\", \"youtube\"]"` | — |
| [SRC-1AE03B9EC3-L004104](../../agents/web_agent.py#L4104) | 4104 | `"                from agents.research import SOCIAL_DOMAINS"` | — |
| [SRC-1AE03B9EC3-L004105](../../agents/web_agent.py#L4105) | 4105 | `"                candidates = ["` | — |
| [SRC-1AE03B9EC3-L004106](../../agents/web_agent.py#L4106) | 4106 | `"                    f\"site:{SOCIAL_DOMAINS[name]} {base_query}\""` | — |
| [SRC-1AE03B9EC3-L004107](../../agents/web_agent.py#L4107) | 4107 | `"                    for name in plan[\"platforms\"][:3]"` | — |
| [SRC-1AE03B9EC3-L004108](../../agents/web_agent.py#L4108) | 4108 | `"                    if name in SOCIAL_DOMAINS"` | — |
| [SRC-1AE03B9EC3-L004109](../../agents/web_agent.py#L4109) | 4109 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004110](../../agents/web_agent.py#L4110) | 4110 | `"                plan[\"queries\"] = list(dict.fromkeys((plan.get(\"queries\") or [])[:5] + candidates))["` | — |
| [SRC-1AE03B9EC3-L004111](../../agents/web_agent.py#L4111) | 4111 | `"                    :MAX_PLAN_QUERIES"` | — |
| [SRC-1AE03B9EC3-L004112](../../agents/web_agent.py#L4112) | 4112 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004113](../../agents/web_agent.py#L4113) | 4113 | `"            if intent_route == \"LEAD_GENERATION\" and clean_mode == \"auto\":"` | — |
| [SRC-1AE03B9EC3-L004114](../../agents/web_agent.py#L4114) | 4114 | `"                # Prospect discovery needs buyer-intent queries and public social signals,"` | — |
| [SRC-1AE03B9EC3-L004115](../../agents/web_agent.py#L4115) | 4115 | `"                # not just broad pages advertising the requested product."` | — |
| [SRC-1AE03B9EC3-L004116](../../agents/web_agent.py#L4116) | 4116 | `"                plan[\"queries\"] = self._lead_generation_queries(question, plan.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L004117](../../agents/web_agent.py#L4117) | 4117 | `"                plan[\"depth\"] = \"standard\""` | — |
| [SRC-1AE03B9EC3-L004118](../../agents/web_agent.py#L4118) | 4118 | `"                plan[\"freshness\"] = \"current\""` | — |
| [SRC-1AE03B9EC3-L004119](../../agents/web_agent.py#L4119) | 4119 | `"                plan[\"social_focus\"] = True"` | — |
| [SRC-1AE03B9EC3-L004120](../../agents/web_agent.py#L4120) | 4120 | `"                allowed_public_platforms = [\"reddit\", \"bluesky\"]"` | — |
| [SRC-1AE03B9EC3-L004121](../../agents/web_agent.py#L4121) | 4121 | `"                if ("` | — |
| [SRC-1AE03B9EC3-L004122](../../agents/web_agent.py#L4122) | 4122 | `"                    os.getenv(\"FACEBOOK_PAGE_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L004123](../../agents/web_agent.py#L4123) | 4123 | `"                    and os.getenv(\"FACEBOOK_PAGE_IDS\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L004124](../../agents/web_agent.py#L4124) | 4124 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004125](../../agents/web_agent.py#L4125) | 4125 | `"                    allowed_public_platforms.append(\"facebook\")"` | — |
| [SRC-1AE03B9EC3-L004126](../../agents/web_agent.py#L4126) | 4126 | `"                if os.getenv(\"X_BEARER_TOKEN\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L004127](../../agents/web_agent.py#L4127) | 4127 | `"                    allowed_public_platforms.append(\"x\")"` | — |
| [SRC-1AE03B9EC3-L004128](../../agents/web_agent.py#L4128) | 4128 | `"                if os.getenv(\"YOUTUBE_API_KEY\", \"\").strip():"` | — |
| [SRC-1AE03B9EC3-L004129](../../agents/web_agent.py#L4129) | 4129 | `"                    allowed_public_platforms.append(\"youtube\")"` | — |
| [SRC-1AE03B9EC3-L004130](../../agents/web_agent.py#L4130) | 4130 | `"                if ("` | — |
| [SRC-1AE03B9EC3-L004131](../../agents/web_agent.py#L4131) | 4131 | `"                    os.getenv(\"INSTAGRAM_USER_ID\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L004132](../../agents/web_agent.py#L4132) | 4132 | `"                    and os.getenv(\"INSTAGRAM_ACCESS_TOKEN\", \"\").strip()"` | — |
| [SRC-1AE03B9EC3-L004133](../../agents/web_agent.py#L4133) | 4133 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004134](../../agents/web_agent.py#L4134) | 4134 | `"                    allowed_public_platforms.append(\"instagram\")"` | — |
| [SRC-1AE03B9EC3-L004135](../../agents/web_agent.py#L4135) | 4135 | `"                plan[\"platforms\"] = list(dict.fromkeys(allowed_public_platforms))"` | — |
| [SRC-1AE03B9EC3-L004136](../../agents/web_agent.py#L4136) | 4136 | `""` | — |
| [SRC-1AE03B9EC3-L004137](../../agents/web_agent.py#L4137) | 4137 | `"        final_topic_queries = []"` | — |
| [SRC-1AE03B9EC3-L004138](../../agents/web_agent.py#L4138) | 4138 | `"        for raw_query in plan.get(\"queries\", []):"` | — |
| [SRC-1AE03B9EC3-L004139](../../agents/web_agent.py#L4139) | 4139 | `"            if not isinstance(raw_query, str) or not raw_query.strip():"` | — |
| [SRC-1AE03B9EC3-L004140](../../agents/web_agent.py#L4140) | 4140 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L004141](../../agents/web_agent.py#L4141) | 4141 | `"            compacted_query = compact_search_query(raw_query)"` | — |
| [SRC-1AE03B9EC3-L004142](../../agents/web_agent.py#L4142) | 4142 | `"            if compacted_query and _relevance_query_tokens(compacted_query):"` | — |
| [SRC-1AE03B9EC3-L004143](../../agents/web_agent.py#L4143) | 4143 | `"                final_topic_queries.append(compacted_query)"` | — |
| [SRC-1AE03B9EC3-L004144](../../agents/web_agent.py#L4144) | 4144 | `"        plan[\"queries\"] = list(dict.fromkeys(final_topic_queries))[:MAX_PLAN_QUERIES]"` | — |
| [SRC-1AE03B9EC3-L004145](../../agents/web_agent.py#L4145) | 4145 | `""` | — |
| [SRC-1AE03B9EC3-L004146](../../agents/web_agent.py#L4146) | 4146 | `"        sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L004147](../../agents/web_agent.py#L4147) | 4147 | `"        search_warnings: list[str] = []"` | — |
| [SRC-1AE03B9EC3-L004148](../../agents/web_agent.py#L4148) | 4148 | `"        report: dict[str, Any] = {}"` | — |
| [SRC-1AE03B9EC3-L004149](../../agents/web_agent.py#L4149) | 4149 | `"        # Scope diagnostic evidence to this research attempt; a reused WebAgent must not"` | — |
| [SRC-1AE03B9EC3-L004150](../../agents/web_agent.py#L4150) | 4150 | `"        # accidentally inherit provider attempts from an earlier question."` | — |
| [SRC-1AE03B9EC3-L004151](../../agents/web_agent.py#L4151) | 4151 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L004152](../../agents/web_agent.py#L4152) | 4152 | `"            research_diagnostic_baseline = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L004153](../../agents/web_agent.py#L4153) | 4153 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L004154](../../agents/web_agent.py#L4154) | 4154 | `"            sources, search_warnings, report = self._collect_research(plan)"` | — |
| [SRC-1AE03B9EC3-L004155](../../agents/web_agent.py#L4155) | 4155 | `"        except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L004156](../../agents/web_agent.py#L4156) | 4156 | `"            search_warnings.append(str(exc))"` | — |
| [SRC-1AE03B9EC3-L004157](../../agents/web_agent.py#L4157) | 4157 | `"            baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L004158](../../agents/web_agent.py#L4158) | 4158 | `"            with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L004159](../../agents/web_agent.py#L4159) | 4159 | `"                failure_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L004160](../../agents/web_agent.py#L4160) | 4160 | `"                    item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004161](../../agents/web_agent.py#L4161) | 4161 | `"                    if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L004162](../../agents/web_agent.py#L4162) | 4162 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004163](../../agents/web_agent.py#L4163) | 4163 | `"            provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L004164](../../agents/web_agent.py#L4164) | 4164 | `"                item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L004165](../../agents/web_agent.py#L4165) | 4165 | `"                for item in failure_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004166](../../agents/web_agent.py#L4166) | 4166 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004167](../../agents/web_agent.py#L4167) | 4167 | `"            report = {"` | — |
| [SRC-1AE03B9EC3-L004168](../../agents/web_agent.py#L4168) | 4168 | `"                \"queries_planned\": len(plan.get(\"queries\", [])),"` | — |
| [SRC-1AE03B9EC3-L004169](../../agents/web_agent.py#L4169) | 4169 | `"                # The exact query count is unknowable when the pipeline fails before it"` | — |
| [SRC-1AE03B9EC3-L004170](../../agents/web_agent.py#L4170) | 4170 | `"                # returns its report. A provider diagnostic may still prove an attempt."` | — |
| [SRC-1AE03B9EC3-L004171](../../agents/web_agent.py#L4171) | 4171 | `"                \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L004172](../../agents/web_agent.py#L4172) | 4172 | `"                \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L004173](../../agents/web_agent.py#L4173) | 4173 | `"                \"search_attempted\": True if provider_attempt_observed else None,"` | — |
| [SRC-1AE03B9EC3-L004174](../../agents/web_agent.py#L4174) | 4174 | `"                \"search_outcome\": ("` | — |
| [SRC-1AE03B9EC3-L004175](../../agents/web_agent.py#L4175) | 4175 | `"                    \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L004176](../../agents/web_agent.py#L4176) | 4176 | `"                    if provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L004177](../../agents/web_agent.py#L4177) | 4177 | `"                    else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L004178](../../agents/web_agent.py#L4178) | 4178 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004179](../../agents/web_agent.py#L4179) | 4179 | `"                \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L004180](../../agents/web_agent.py#L4180) | 4180 | `"                \"unique_sources\": None,"` | — |
| [SRC-1AE03B9EC3-L004181](../../agents/web_agent.py#L4181) | 4181 | `"                \"pages_fetched\": None,"` | — |
| [SRC-1AE03B9EC3-L004182](../../agents/web_agent.py#L4182) | 4182 | `"                \"providers_used\": [],"` | — |
| [SRC-1AE03B9EC3-L004183](../../agents/web_agent.py#L4183) | 4183 | `"                \"provider_counts\": None,"` | — |
| [SRC-1AE03B9EC3-L004184](../../agents/web_agent.py#L4184) | 4184 | `"                \"platform_counts\": {},"` | — |
| [SRC-1AE03B9EC3-L004185](../../agents/web_agent.py#L4185) | 4185 | `"                \"social_direct_results\": None,"` | — |
| [SRC-1AE03B9EC3-L004186](../../agents/web_agent.py#L4186) | 4186 | `"                \"provider_diagnostics\": failure_diagnostics,"` | — |
| [SRC-1AE03B9EC3-L004187](../../agents/web_agent.py#L4187) | 4187 | `"                \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L004188](../../agents/web_agent.py#L4188) | 4188 | `"                \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L004189](../../agents/web_agent.py#L4189) | 4189 | `"                \"evidence_signals\": evidence_signal_report([], plan.get(\"freshness\", \"any\")),"` | — |
| [SRC-1AE03B9EC3-L004190](../../agents/web_agent.py#L4190) | 4190 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004191](../../agents/web_agent.py#L4191) | 4191 | `"        # Final relevance check is intentionally repeated after fusion, before any answer LLM call."` | — |
| [SRC-1AE03B9EC3-L004192](../../agents/web_agent.py#L4192) | 4192 | `"        filtered_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L004193](../../agents/web_agent.py#L4193) | 4193 | `"        for source in sources:"` | — |
| [SRC-1AE03B9EC3-L004194](../../agents/web_agent.py#L4194) | 4194 | `"            if \"user_supplied_url\" in source.get(\"providers\", []):"` | — |
| [SRC-1AE03B9EC3-L004195](../../agents/web_agent.py#L4195) | 4195 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004196](../../agents/web_agent.py#L4196) | 4196 | `"                continue"` | — |
| [SRC-1AE03B9EC3-L004197](../../agents/web_agent.py#L4197) | 4197 | `"            candidate_queries = ("` | — |
| [SRC-1AE03B9EC3-L004198](../../agents/web_agent.py#L4198) | 4198 | `"                source.get(\"queries\")"` | — |
| [SRC-1AE03B9EC3-L004199](../../agents/web_agent.py#L4199) | 4199 | `"                or plan.get(\"queries\")"` | — |
| [SRC-1AE03B9EC3-L004200](../../agents/web_agent.py#L4200) | 4200 | `"                or [compact_search_query(question)]"` | — |
| [SRC-1AE03B9EC3-L004201](../../agents/web_agent.py#L4201) | 4201 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004202](../../agents/web_agent.py#L4202) | 4202 | `"            if any(self._source_matches_query(str(q), source) for q in candidate_queries):"` | — |
| [SRC-1AE03B9EC3-L004203](../../agents/web_agent.py#L4203) | 4203 | `"                filtered_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004204](../../agents/web_agent.py#L4204) | 4204 | `"        sources = filtered_sources"` | — |
| [SRC-1AE03B9EC3-L004205](../../agents/web_agent.py#L4205) | 4205 | `"        search_warning = \"؛ \".join(search_warnings) if search_warnings else None"` | — |
| [SRC-1AE03B9EC3-L004206](../../agents/web_agent.py#L4206) | 4206 | `"        independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L004207](../../agents/web_agent.py#L4207) | 4207 | `"            registrable_domain("` | — |
| [SRC-1AE03B9EC3-L004208](../../agents/web_agent.py#L4208) | 4208 | `"                source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L004209](../../agents/web_agent.py#L4209) | 4209 | `"                or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L004210](../../agents/web_agent.py#L4210) | 4210 | `"                or \"\""` | — |
| [SRC-1AE03B9EC3-L004211](../../agents/web_agent.py#L4211) | 4211 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004212](../../agents/web_agent.py#L4212) | 4212 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L004213](../../agents/web_agent.py#L4213) | 4213 | `"        }"` | — |
| [SRC-1AE03B9EC3-L004214](../../agents/web_agent.py#L4214) | 4214 | `"        independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L004215](../../agents/web_agent.py#L4215) | 4215 | `"        # A user-requested page summary is a different task from open-ended research:"` | — |
| [SRC-1AE03B9EC3-L004216](../../agents/web_agent.py#L4216) | 4216 | `"        # one successfully extracted, explicitly supplied page can support a summary,"` | — |
| [SRC-1AE03B9EC3-L004217](../../agents/web_agent.py#L4217) | 4217 | `"        # but must never be presented as independently corroborated research."` | — |
| [SRC-1AE03B9EC3-L004218](../../agents/web_agent.py#L4218) | 4218 | `"        has_read_user_supplied_page = any("` | — |
| [SRC-1AE03B9EC3-L004219](../../agents/web_agent.py#L4219) | 4219 | `"            \"user_supplied_url\" in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L004220](../../agents/web_agent.py#L4220) | 4220 | `"            and bool(source.get(\"page_fetched\"))"` | — |
| [SRC-1AE03B9EC3-L004221](../../agents/web_agent.py#L4221) | 4221 | `"            and bool(str(source.get(\"page_text\") or \"\").strip())"` | — |
| [SRC-1AE03B9EC3-L004222](../../agents/web_agent.py#L4222) | 4222 | `"            for source in sources"` | — |
| [SRC-1AE03B9EC3-L004223](../../agents/web_agent.py#L4223) | 4223 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004224](../../agents/web_agent.py#L4224) | 4224 | `"        single_source_page_summary = ("` | — |
| [SRC-1AE03B9EC3-L004225](../../agents/web_agent.py#L4225) | 4225 | `"            has_read_user_supplied_page"` | — |
| [SRC-1AE03B9EC3-L004226](../../agents/web_agent.py#L4226) | 4226 | `"            and len(sources) == 1"` | — |
| [SRC-1AE03B9EC3-L004227](../../agents/web_agent.py#L4227) | 4227 | `"            and len(independent_domains) == 1"` | — |
| [SRC-1AE03B9EC3-L004228](../../agents/web_agent.py#L4228) | 4228 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004229](../../agents/web_agent.py#L4229) | 4229 | `"        if single_source_page_summary:"` | — |
| [SRC-1AE03B9EC3-L004230](../../agents/web_agent.py#L4230) | 4230 | `"            search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004231](../../agents/web_agent.py#L4231) | 4231 | `"                \"هذا ملخص للرابط الذي قدمته فقط؛ لم يتم تأكيد محتواه من مصدر مستقل آخر.\""` | — |
| [SRC-1AE03B9EC3-L004232](../../agents/web_agent.py#L4232) | 4232 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004233](../../agents/web_agent.py#L4233) | 4233 | `"            search_warning = \"؛ \".join(search_warnings)"` | — |
| [SRC-1AE03B9EC3-L004234](../../agents/web_agent.py#L4234) | 4234 | `"        # Link-finding and lead-discovery are actionable discovery tasks, not broad"` | — |
| [SRC-1AE03B9EC3-L004235](../../agents/web_agent.py#L4235) | 4235 | `"        # fact-checking. Keep useful candidates visible while explicitly labelling them"` | — |
| [SRC-1AE03B9EC3-L004236](../../agents/web_agent.py#L4236) | 4236 | `"        # as uncorroborated instead of refusing a lone result as if it were no result."` | — |
| [SRC-1AE03B9EC3-L004237](../../agents/web_agent.py#L4237) | 4237 | `"        navigation_request = self._is_navigation_request(question)"` | — |
| [SRC-1AE03B9EC3-L004238](../../agents/web_agent.py#L4238) | 4238 | `"        lead_request = intent_route == \"LEAD_GENERATION\" or self._is_lead_search(question)"` | — |
| [SRC-1AE03B9EC3-L004239](../../agents/web_agent.py#L4239) | 4239 | `"        listing_request = self._is_listing_discovery(question)"` | — |
| [SRC-1AE03B9EC3-L004240](../../agents/web_agent.py#L4240) | 4240 | `"        lead_evidence_sources: list[dict[str, Any]] = []"` | — |
| [SRC-1AE03B9EC3-L004241](../../agents/web_agent.py#L4241) | 4241 | `"        related_lead_results_count = 0"` | — |
| [SRC-1AE03B9EC3-L004242](../../agents/web_agent.py#L4242) | 4242 | `"        if lead_request:"` | — |
| [SRC-1AE03B9EC3-L004243](../../agents/web_agent.py#L4243) | 4243 | `"            related_lead_results_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004244](../../agents/web_agent.py#L4244) | 4244 | `"            for source in sources:"` | — |
| [SRC-1AE03B9EC3-L004245](../../agents/web_agent.py#L4245) | 4245 | `"                signal = self._lead_intent_evidence(source)"` | — |
| [SRC-1AE03B9EC3-L004246](../../agents/web_agent.py#L4246) | 4246 | `"                if signal:"` | — |
| [SRC-1AE03B9EC3-L004247](../../agents/web_agent.py#L4247) | 4247 | `"                    source[\"lead_qualification\"] = \"public_buyer_intent_signal\""` | — |
| [SRC-1AE03B9EC3-L004248](../../agents/web_agent.py#L4248) | 4248 | `"                    source[\"lead_intent_evidence\"] = signal"` | — |
| [SRC-1AE03B9EC3-L004249](../../agents/web_agent.py#L4249) | 4249 | `"                    lead_evidence_sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004250](../../agents/web_agent.py#L4250) | 4250 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L004251](../../agents/web_agent.py#L4251) | 4251 | `"                    source[\"lead_qualification\"] = \"related_result_not_lead\""` | — |
| [SRC-1AE03B9EC3-L004252](../../agents/web_agent.py#L4252) | 4252 | `"            lead_research_incomplete = ("` | — |
| [SRC-1AE03B9EC3-L004253](../../agents/web_agent.py#L4253) | 4253 | `"                not sources"` | — |
| [SRC-1AE03B9EC3-L004254](../../agents/web_agent.py#L4254) | 4254 | `"                and report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES"` | — |
| [SRC-1AE03B9EC3-L004255](../../agents/web_agent.py#L4255) | 4255 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004256](../../agents/web_agent.py#L4256) | 4256 | `"            report[\"lead_generation\"] = {"` | — |
| [SRC-1AE03B9EC3-L004257](../../agents/web_agent.py#L4257) | 4257 | `"                \"status\": ("` | — |
| [SRC-1AE03B9EC3-L004258](../../agents/web_agent.py#L4258) | 4258 | `"                    \"research_incomplete\" if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L004259](../../agents/web_agent.py#L4259) | 4259 | `"                    else \"candidate_signals_found\" if lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L004260](../../agents/web_agent.py#L4260) | 4260 | `"                    else \"no_qualified_candidates_found\""` | — |
| [SRC-1AE03B9EC3-L004261](../../agents/web_agent.py#L4261) | 4261 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004262](../../agents/web_agent.py#L4262) | 4262 | `"                \"candidate_signal_count\": ("` | — |
| [SRC-1AE03B9EC3-L004263](../../agents/web_agent.py#L4263) | 4263 | `"                    None if lead_research_incomplete else len(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L004264](../../agents/web_agent.py#L4264) | 4264 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004265](../../agents/web_agent.py#L4265) | 4265 | `"                \"related_results_reviewed\": ("` | — |
| [SRC-1AE03B9EC3-L004266](../../agents/web_agent.py#L4266) | 4266 | `"                    None if lead_research_incomplete else related_lead_results_count"` | — |
| [SRC-1AE03B9EC3-L004267](../../agents/web_agent.py#L4267) | 4267 | `"                ),"` | — |
| [SRC-1AE03B9EC3-L004268](../../agents/web_agent.py#L4268) | 4268 | `"                \"qualification_rule\": \"explicit_public_buyer_intent_phrase\","` | — |
| [SRC-1AE03B9EC3-L004269](../../agents/web_agent.py#L4269) | 4269 | `"                \"identity_verified\": False,"` | — |
| [SRC-1AE03B9EC3-L004270](../../agents/web_agent.py#L4270) | 4270 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004271](../../agents/web_agent.py#L4271) | 4271 | `"            if not lead_evidence_sources:"` | — |
| [SRC-1AE03B9EC3-L004272](../../agents/web_agent.py#L4272) | 4272 | `"                if sources:"` | — |
| [SRC-1AE03B9EC3-L004273](../../agents/web_agent.py#L4273) | 4273 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L004274](../../agents/web_agent.py#L4274) | 4274 | `"                        \"لم أعثر على إشارة نصية واضحة تثبت أن أي نتيجة في هذه الجولة تتعلق بشخص \""` | — |
| [SRC-1AE03B9EC3-L004275](../../agents/web_agent.py#L4275) | 4275 | `"                        \"يريد الشراء. راجعت \""` | — |
| [SRC-1AE03B9EC3-L004276](../../agents/web_agent.py#L4276) | 4276 | `"                        + str(len(sources))"` | — |
| [SRC-1AE03B9EC3-L004277](../../agents/web_agent.py#L4277) | 4277 | `"                        + \" نتيجة مرتبطة بالموضوع، لكنني لم أعتبر إعلانات البيع أو صفحات السوق \""` | — |
| [SRC-1AE03B9EC3-L004278](../../agents/web_agent.py#L4278) | 4278 | `"                        \"عملاء محتملين. الروابط أدناه نتائج مرتبطة بالموضوع فقط وليست عملاء.\""` | — |
| [SRC-1AE03B9EC3-L004279](../../agents/web_agent.py#L4279) | 4279 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004280](../../agents/web_agent.py#L4280) | 4280 | `"                elif report.get(\"search_outcome\") in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L004281](../../agents/web_agent.py#L4281) | 4281 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L004282](../../agents/web_agent.py#L4282) | 4282 | `"                        \"تعطل مسار البحث أو لم يمكن تأكيد اكتماله؛ لذلك لا أستطيع تحديد ما إذا \""` | — |
| [SRC-1AE03B9EC3-L004283](../../agents/web_agent.py#L4283) | 4283 | `"                        \"كانت هناك نتائج تصلح كعملاء محتملين في هذه الجولة.\""` | — |
| [SRC-1AE03B9EC3-L004284](../../agents/web_agent.py#L4284) | 4284 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004285](../../agents/web_agent.py#L4285) | 4285 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L004286](../../agents/web_agent.py#L4286) | 4286 | `"                    lead_answer = ("` | — |
| [SRC-1AE03B9EC3-L004287](../../agents/web_agent.py#L4287) | 4287 | `"                        \"لم تظهر نتائج قابلة للاستخدام تثبت نية شراء في هذه الجولة. هذا لا يثبت \""` | — |
| [SRC-1AE03B9EC3-L004288](../../agents/web_agent.py#L4288) | 4288 | `"                        \"عدم وجود عملاء؛ بل يعني أن البحث الحالي لم يعثر على دليل كافٍ.\""` | — |
| [SRC-1AE03B9EC3-L004289](../../agents/web_agent.py#L4289) | 4289 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004290](../../agents/web_agent.py#L4290) | 4290 | `"                report[\"research_quality\"] = \"failed\""` | — |
| [SRC-1AE03B9EC3-L004291](../../agents/web_agent.py#L4291) | 4291 | `"                # Distinguish zero qualified signals from unknown counts after an exception."` | — |
| [SRC-1AE03B9EC3-L004292](../../agents/web_agent.py#L4292) | 4292 | `"                report[\"usable_sources_after_filtering\"] = ("` | — |
| [SRC-1AE03B9EC3-L004293](../../agents/web_agent.py#L4293) | 4293 | `"                    None if lead_research_incomplete else len(sources)"` | — |
| [SRC-1AE03B9EC3-L004294](../../agents/web_agent.py#L4294) | 4294 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004295](../../agents/web_agent.py#L4295) | 4295 | `"                report[\"evidence_signals\"] = ("` | — |
| [SRC-1AE03B9EC3-L004296](../../agents/web_agent.py#L4296) | 4296 | `"                    None if lead_research_incomplete"` | — |
| [SRC-1AE03B9EC3-L004297](../../agents/web_agent.py#L4297) | 4297 | `"                    else evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L004298](../../agents/web_agent.py#L4298) | 4298 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004299](../../agents/web_agent.py#L4299) | 4299 | `"                public_related_sources = [{"` | — |
| [SRC-1AE03B9EC3-L004300](../../agents/web_agent.py#L4300) | 4300 | `"                    \"title\": source.get(\"title\") or \"نتيجة ويب\","` | — |
| [SRC-1AE03B9EC3-L004301](../../agents/web_agent.py#L4301) | 4301 | `"                    \"url\": source[\"url\"],"` | — |
| [SRC-1AE03B9EC3-L004302](../../agents/web_agent.py#L4302) | 4302 | `"                    \"snippet\": source.get(\"snippet\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004303](../../agents/web_agent.py#L4303) | 4303 | `"                    \"page_fetched\": bool(source.get(\"page_fetched\")),"` | — |
| [SRC-1AE03B9EC3-L004304](../../agents/web_agent.py#L4304) | 4304 | `"                    \"providers\": source.get(\"providers\", []),"` | — |
| [SRC-1AE03B9EC3-L004305](../../agents/web_agent.py#L4305) | 4305 | `"                    \"queries\": source.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L004306](../../agents/web_agent.py#L4306) | 4306 | `"                    \"platform\": source.get(\"platform\", \"web\"),"` | — |
| [SRC-1AE03B9EC3-L004307](../../agents/web_agent.py#L4307) | 4307 | `"                    \"domain\": source.get(\"domain\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004308](../../agents/web_agent.py#L4308) | 4308 | `"                    \"source_class\": source.get(\"source_class\", \"general\"),"` | — |
| [SRC-1AE03B9EC3-L004309](../../agents/web_agent.py#L4309) | 4309 | `"                    \"published_at\": source.get(\"published_at\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004310](../../agents/web_agent.py#L4310) | 4310 | `"                    \"publisher_name\": source.get(\"publisher_name\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004311](../../agents/web_agent.py#L4311) | 4311 | `"                    \"publisher_url\": source.get(\"publisher_url\", \"\"),"` | — |
| [SRC-1AE03B9EC3-L004312](../../agents/web_agent.py#L4312) | 4312 | `"                    \"rank_score\": round(float(source.get(\"rank_score\", 0)), 6),"` | — |
| [SRC-1AE03B9EC3-L004313](../../agents/web_agent.py#L4313) | 4313 | `"                    \"lead_qualification\": \"related_result_not_lead\","` | — |
| [SRC-1AE03B9EC3-L004314](../../agents/web_agent.py#L4314) | 4314 | `"                } for source in sources]"` | — |
| [SRC-1AE03B9EC3-L004315](../../agents/web_agent.py#L4315) | 4315 | `"                return {"` | — |
| [SRC-1AE03B9EC3-L004316](../../agents/web_agent.py#L4316) | 4316 | `"                    \"answer\": lead_answer,"` | — |
| [SRC-1AE03B9EC3-L004317](../../agents/web_agent.py#L4317) | 4317 | `"                    \"question\": question,"` | — |
| [SRC-1AE03B9EC3-L004318](../../agents/web_agent.py#L4318) | 4318 | `"                    \"search_query\": (plan.get(\"queries\") or [\"\"])[0],"` | — |
| [SRC-1AE03B9EC3-L004319](../../agents/web_agent.py#L4319) | 4319 | `"                    \"search_queries\": plan.get(\"queries\", []),"` | — |
| [SRC-1AE03B9EC3-L004320](../../agents/web_agent.py#L4320) | 4320 | `"                    \"research_plan\": {"` | — |
| [SRC-1AE03B9EC3-L004321](../../agents/web_agent.py#L4321) | 4321 | `"                        \"depth\": plan.get(\"depth\", \"standard\"),"` | — |
| [SRC-1AE03B9EC3-L004322](../../agents/web_agent.py#L4322) | 4322 | `"                        \"freshness\": plan.get(\"freshness\", \"any\"),"` | — |
| [SRC-1AE03B9EC3-L004323](../../agents/web_agent.py#L4323) | 4323 | `"                        \"social_focus\": bool(plan.get(\"social_focus\")),"` | — |
| [SRC-1AE03B9EC3-L004324](../../agents/web_agent.py#L4324) | 4324 | `"                        \"platforms\": plan.get(\"platforms\", []),"` | — |
| [SRC-1AE03B9EC3-L004325](../../agents/web_agent.py#L4325) | 4325 | `"                        \"mode\": clean_mode,"` | — |
| [SRC-1AE03B9EC3-L004326](../../agents/web_agent.py#L4326) | 4326 | `"                        \"direct_urls_provided\": len(plan.get(\"direct_urls\", [])),"` | — |
| [SRC-1AE03B9EC3-L004327](../../agents/web_agent.py#L4327) | 4327 | `"                        \"planning_method\": plan.get(\"planning_method\", \"deterministic_fallback\"),"` | — |
| [SRC-1AE03B9EC3-L004328](../../agents/web_agent.py#L4328) | 4328 | `"                        \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L004329](../../agents/web_agent.py#L4329) | 4329 | `"                        \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L004330](../../agents/web_agent.py#L4330) | 4330 | `"                    },"` | — |
| [SRC-1AE03B9EC3-L004331](../../agents/web_agent.py#L4331) | 4331 | `"                    \"search_report\": report,"` | — |
| [SRC-1AE03B9EC3-L004332](../../agents/web_agent.py#L4332) | 4332 | `"                    \"sources\": public_related_sources,"` | — |
| [SRC-1AE03B9EC3-L004333](../../agents/web_agent.py#L4333) | 4333 | `"                    \"used_language_model\": False,"` | — |
| [SRC-1AE03B9EC3-L004334](../../agents/web_agent.py#L4334) | 4334 | `"                    \"used_web_search\": bool(sources),"` | — |
| [SRC-1AE03B9EC3-L004335](../../agents/web_agent.py#L4335) | 4335 | `"                    \"search_attempted\": report.get("` | — |
| [SRC-1AE03B9EC3-L004336](../../agents/web_agent.py#L4336) | 4336 | `"                        \"search_attempted\","` | — |
| [SRC-1AE03B9EC3-L004337](../../agents/web_agent.py#L4337) | 4337 | `"                        bool(report.get(\"queries_attempted\", 0)),"` | — |
| [SRC-1AE03B9EC3-L004338](../../agents/web_agent.py#L4338) | 4338 | `"                    ),"` | — |
| [SRC-1AE03B9EC3-L004339](../../agents/web_agent.py#L4339) | 4339 | `"                    \"used_social_search\": bool(report.get(\"social_direct_results\", 0)),"` | — |
| [SRC-1AE03B9EC3-L004340](../../agents/web_agent.py#L4340) | 4340 | `"                    \"warnings\": [lead_answer],"` | — |
| [SRC-1AE03B9EC3-L004341](../../agents/web_agent.py#L4341) | 4341 | `"                    \"kind\": \"lead_discovery_no_qualified_candidates\","` | — |
| [SRC-1AE03B9EC3-L004342](../../agents/web_agent.py#L4342) | 4342 | `"                    \"intent_route\": intent_route,"` | — |
| [SRC-1AE03B9EC3-L004343](../../agents/web_agent.py#L4343) | 4343 | `"                    \"intent_route_reason\": intent_reason,"` | — |
| [SRC-1AE03B9EC3-L004344](../../agents/web_agent.py#L4344) | 4344 | `"                    \"research_quality\": \"failed\","` | — |
| [SRC-1AE03B9EC3-L004345](../../agents/web_agent.py#L4345) | 4345 | `"                }"` | — |
| [SRC-1AE03B9EC3-L004346](../../agents/web_agent.py#L4346) | 4346 | `"            # Only explicit public buyer-intent signals may be synthesized as lead candidates."` | — |
| [SRC-1AE03B9EC3-L004347](../../agents/web_agent.py#L4347) | 4347 | `"            sources = lead_evidence_sources"` | — |
| [SRC-1AE03B9EC3-L004348](../../agents/web_agent.py#L4348) | 4348 | `"            report[\"evidence_signals\"] = evidence_signal_report(sources, plan.get(\"freshness\", \"any\"))"` | — |
| [SRC-1AE03B9EC3-L004349](../../agents/web_agent.py#L4349) | 4349 | `"            report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004350](../../agents/web_agent.py#L4350) | 4350 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004351](../../agents/web_agent.py#L4351) | 4351 | `"            report[\"pages_fetched\"] = sum(bool(source.get(\"page_fetched\")) for source in sources)"` | — |
| [SRC-1AE03B9EC3-L004352](../../agents/web_agent.py#L4352) | 4352 | `"            independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L004353](../../agents/web_agent.py#L4353) | 4353 | `"                registrable_domain("` | — |
| [SRC-1AE03B9EC3-L004354](../../agents/web_agent.py#L4354) | 4354 | `"                    source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L004355](../../agents/web_agent.py#L4355) | 4355 | `"                    or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L004356](../../agents/web_agent.py#L4356) | 4356 | `"                    or \"\""` | — |
| [SRC-1AE03B9EC3-L004357](../../agents/web_agent.py#L4357) | 4357 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004358](../../agents/web_agent.py#L4358) | 4358 | `"                for source in sources"` | — |
| [SRC-1AE03B9EC3-L004359](../../agents/web_agent.py#L4359) | 4359 | `"            }"` | — |
| [SRC-1AE03B9EC3-L004360](../../agents/web_agent.py#L4360) | 4360 | `"            independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L004361](../../agents/web_agent.py#L4361) | 4361 | `"        single_source_navigation = navigation_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L004362](../../agents/web_agent.py#L4362) | 4362 | `"        single_source_social = bool(plan.get(\"social_focus\")) and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L004363](../../agents/web_agent.py#L4363) | 4363 | `"        single_source_lead = lead_request and bool(lead_evidence_sources)"` | — |
| [SRC-1AE03B9EC3-L004364](../../agents/web_agent.py#L4364) | 4364 | `"        single_source_listing = listing_request and bool(sources)"` | — |
| [SRC-1AE03B9EC3-L004365](../../agents/web_agent.py#L4365) | 4365 | `"        task_specific_partial_evidence = ("` | — |
| [SRC-1AE03B9EC3-L004366](../../agents/web_agent.py#L4366) | 4366 | `"            single_source_page_summary"` | — |
| [SRC-1AE03B9EC3-L004367](../../agents/web_agent.py#L4367) | 4367 | `"            or single_source_navigation"` | — |
| [SRC-1AE03B9EC3-L004368](../../agents/web_agent.py#L4368) | 4368 | `"            or single_source_social"` | — |
| [SRC-1AE03B9EC3-L004369](../../agents/web_agent.py#L4369) | 4369 | `"            or single_source_lead"` | — |
| [SRC-1AE03B9EC3-L004370](../../agents/web_agent.py#L4370) | 4370 | `"            or single_source_listing"` | — |
| [SRC-1AE03B9EC3-L004371](../../agents/web_agent.py#L4371) | 4371 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004372](../../agents/web_agent.py#L4372) | 4372 | `"        needs_corroboration = len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L004373](../../agents/web_agent.py#L4373) | 4373 | `"        evidence_repair: dict[str, Any] = {"` | — |
| [SRC-1AE03B9EC3-L004374](../../agents/web_agent.py#L4374) | 4374 | `"            \"attempted\": False,"` | — |
| [SRC-1AE03B9EC3-L004375](../../agents/web_agent.py#L4375) | 4375 | `"            \"max_extra_queries\": 1,"` | — |
| [SRC-1AE03B9EC3-L004376](../../agents/web_agent.py#L4376) | 4376 | `"            \"reason\": \"initial_evidence_gate_satisfied\" if not needs_corroboration else \"not_attempted\","` | — |
| [SRC-1AE03B9EC3-L004377](../../agents/web_agent.py#L4377) | 4377 | `"        }"` | — |
| [SRC-1AE03B9EC3-L004378](../../agents/web_agent.py#L4378) | 4378 | `"        if needs_corroboration and not plan.get(\"queries\"):"` | — |
| [SRC-1AE03B9EC3-L004379](../../agents/web_agent.py#L4379) | 4379 | `"            evidence_repair[\"reason\"] = \"no_topic_query_available\""` | — |
| [SRC-1AE03B9EC3-L004380](../../agents/web_agent.py#L4380) | 4380 | `"        elif needs_corroboration:"` | — |
| [SRC-1AE03B9EC3-L004381](../../agents/web_agent.py#L4381) | 4381 | `"            if task_specific_partial_evidence:"` | — |
| [SRC-1AE03B9EC3-L004382](../../agents/web_agent.py#L4382) | 4382 | `"                evidence_repair[\"reason\"] = \"task_specific_partial_evidence\""` | — |
| [SRC-1AE03B9EC3-L004383](../../agents/web_agent.py#L4383) | 4383 | `"            elif plan.get(\"social_focus\"):"` | — |
| [SRC-1AE03B9EC3-L004384](../../agents/web_agent.py#L4384) | 4384 | `"                evidence_repair[\"reason\"] = \"social_search_not_retried\""` | — |
| [SRC-1AE03B9EC3-L004385](../../agents/web_agent.py#L4385) | 4385 | `"            elif plan.get(\"depth\") == \"deep\" or report.get(\"expansion_queries\"):"` | — |
| [SRC-1AE03B9EC3-L004386](../../agents/web_agent.py#L4386) | 4386 | `"                evidence_repair[\"reason\"] = \"deep_research_already_expanded\""` | — |
| [SRC-1AE03B9EC3-L004387](../../agents/web_agent.py#L4387) | 4387 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004388](../../agents/web_agent.py#L4388) | 4388 | `"                original_queries = ["` | — |
| [SRC-1AE03B9EC3-L004389](../../agents/web_agent.py#L4389) | 4389 | `"                    str(item).strip()"` | — |
| [SRC-1AE03B9EC3-L004390](../../agents/web_agent.py#L4390) | 4390 | `"                    for item in plan.get(\"queries\", [])"` | — |
| [SRC-1AE03B9EC3-L004391](../../agents/web_agent.py#L4391) | 4391 | `"                    if isinstance(item, str) and item.strip()"` | — |
| [SRC-1AE03B9EC3-L004392](../../agents/web_agent.py#L4392) | 4392 | `"                ]"` | — |
| [SRC-1AE03B9EC3-L004393](../../agents/web_agent.py#L4393) | 4393 | `"                base_query = ("` | — |
| [SRC-1AE03B9EC3-L004394](../../agents/web_agent.py#L4394) | 4394 | `"                    original_queries[0]"` | — |
| [SRC-1AE03B9EC3-L004395](../../agents/web_agent.py#L4395) | 4395 | `"                    if original_queries"` | — |
| [SRC-1AE03B9EC3-L004396](../../agents/web_agent.py#L4396) | 4396 | `"                    else compact_search_query(question)"` | — |
| [SRC-1AE03B9EC3-L004397](../../agents/web_agent.py#L4397) | 4397 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004398](../../agents/web_agent.py#L4398) | 4398 | `"                suffix = ("` | — |
| [SRC-1AE03B9EC3-L004399](../../agents/web_agent.py#L4399) | 4399 | `"                    \"latest official primary source\""` | — |
| [SRC-1AE03B9EC3-L004400](../../agents/web_agent.py#L4400) | 4400 | `"                    if plan.get(\"freshness\") == \"current\""` | — |
| [SRC-1AE03B9EC3-L004401](../../agents/web_agent.py#L4401) | 4401 | `"                    else \"official primary source data\""` | — |
| [SRC-1AE03B9EC3-L004402](../../agents/web_agent.py#L4402) | 4402 | `"                )"` | — |
| [SRC-1AE03B9EC3-L004403](../../agents/web_agent.py#L4403) | 4403 | `"                repair_query = compact_search_query(f\"{base_query} {suffix}\")"` | — |
| [SRC-1AE03B9EC3-L004404](../../agents/web_agent.py#L4404) | 4404 | `"                if not repair_query or not _relevance_query_tokens(repair_query):"` | — |
| [SRC-1AE03B9EC3-L004405](../../agents/web_agent.py#L4405) | 4405 | `"                    evidence_repair[\"reason\"] = \"no_topic_query_available\""` | — |
| [SRC-1AE03B9EC3-L004406](../../agents/web_agent.py#L4406) | 4406 | `"                    repair_query = \"\""` | — |
| [SRC-1AE03B9EC3-L004407](../../agents/web_agent.py#L4407) | 4407 | `"                known_queries = {"` | — |
| [SRC-1AE03B9EC3-L004408](../../agents/web_agent.py#L4408) | 4408 | `"                    _normalize_search_query(item).casefold()"` | — |
| [SRC-1AE03B9EC3-L004409](../../agents/web_agent.py#L4409) | 4409 | `"                    for item in original_queries"` | — |
| [SRC-1AE03B9EC3-L004410](../../agents/web_agent.py#L4410) | 4410 | `"                }"` | — |
| [SRC-1AE03B9EC3-L004411](../../agents/web_agent.py#L4411) | 4411 | `"                if repair_query and _normalize_search_query(repair_query).casefold() in known_queries:"` | — |
| [SRC-1AE03B9EC3-L004412](../../agents/web_agent.py#L4412) | 4412 | `"                    repair_query = compact_search_query("` | — |
| [SRC-1AE03B9EC3-L004413](../../agents/web_agent.py#L4413) | 4413 | `"                        f\"{base_query} independent corroborating evidence\""` | — |
| [SRC-1AE03B9EC3-L004414](../../agents/web_agent.py#L4414) | 4414 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004415](../../agents/web_agent.py#L4415) | 4415 | `"                if repair_query and _relevance_query_tokens(repair_query) and ("` | — |
| [SRC-1AE03B9EC3-L004416](../../agents/web_agent.py#L4416) | 4416 | `"                    _normalize_search_query(repair_query).casefold() not in known_queries"` | — |
| [SRC-1AE03B9EC3-L004417](../../agents/web_agent.py#L4417) | 4417 | `"                ):"` | — |
| [SRC-1AE03B9EC3-L004418](../../agents/web_agent.py#L4418) | 4418 | `"                    initial_source_count = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004419](../../agents/web_agent.py#L4419) | 4419 | `"                    initial_domain_count = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L004420](../../agents/web_agent.py#L4420) | 4420 | `"                    evidence_repair[\"attempted\"] = True"` | — |
| [SRC-1AE03B9EC3-L004421](../../agents/web_agent.py#L4421) | 4421 | `"                    evidence_repair[\"reason\"] = \"thin_or_unrelated_initial_evidence\""` | — |
| [SRC-1AE03B9EC3-L004422](../../agents/web_agent.py#L4422) | 4422 | `"                    evidence_repair[\"query\"] = repair_query"` | — |
| [SRC-1AE03B9EC3-L004423](../../agents/web_agent.py#L4423) | 4423 | `"                    repair_plan = dict(plan)"` | — |
| [SRC-1AE03B9EC3-L004424](../../agents/web_agent.py#L4424) | 4424 | `"                    repair_plan.update({"` | — |
| [SRC-1AE03B9EC3-L004425](../../agents/web_agent.py#L4425) | 4425 | `"                        \"queries\": [repair_query],"` | — |
| [SRC-1AE03B9EC3-L004426](../../agents/web_agent.py#L4426) | 4426 | `"                        \"depth\": \"standard\","` | — |
| [SRC-1AE03B9EC3-L004427](../../agents/web_agent.py#L4427) | 4427 | `"                        \"social_focus\": False,"` | — |
| [SRC-1AE03B9EC3-L004428](../../agents/web_agent.py#L4428) | 4428 | `"                        \"platforms\": [],"` | — |
| [SRC-1AE03B9EC3-L004429](../../agents/web_agent.py#L4429) | 4429 | `"                        \"direct_urls\": [],"` | — |
| [SRC-1AE03B9EC3-L004430](../../agents/web_agent.py#L4430) | 4430 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L004431](../../agents/web_agent.py#L4431) | 4431 | `"                    try:"` | — |
| [SRC-1AE03B9EC3-L004432](../../agents/web_agent.py#L4432) | 4432 | `"                        repair_sources, repair_warnings, repair_report = self._collect_research("` | — |
| [SRC-1AE03B9EC3-L004433](../../agents/web_agent.py#L4433) | 4433 | `"                            repair_plan"` | — |
| [SRC-1AE03B9EC3-L004434](../../agents/web_agent.py#L4434) | 4434 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004435](../../agents/web_agent.py#L4435) | 4435 | `"                    except (RuntimeError, AgentDependencyError, ValueError) as exc:"` | — |
| [SRC-1AE03B9EC3-L004436](../../agents/web_agent.py#L4436) | 4436 | `"                        repair_sources = []"` | — |
| [SRC-1AE03B9EC3-L004437](../../agents/web_agent.py#L4437) | 4437 | `"                        repair_warnings = []"` | — |
| [SRC-1AE03B9EC3-L004438](../../agents/web_agent.py#L4438) | 4438 | `"                        repair_report = {"` | — |
| [SRC-1AE03B9EC3-L004439](../../agents/web_agent.py#L4439) | 4439 | `"                            \"queries_planned\": 1,"` | — |
| [SRC-1AE03B9EC3-L004440](../../agents/web_agent.py#L4440) | 4440 | `"                            \"queries_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L004441](../../agents/web_agent.py#L4441) | 4441 | `"                            \"queries_attempted_known\": False,"` | — |
| [SRC-1AE03B9EC3-L004442](../../agents/web_agent.py#L4442) | 4442 | `"                            \"search_attempted\": None,"` | — |
| [SRC-1AE03B9EC3-L004443](../../agents/web_agent.py#L4443) | 4443 | `"                            \"search_outcome\": \"unknown_after_research_error\","` | — |
| [SRC-1AE03B9EC3-L004444](../../agents/web_agent.py#L4444) | 4444 | `"                            \"usable_sources_after_filtering\": None,"` | — |
| [SRC-1AE03B9EC3-L004445](../../agents/web_agent.py#L4445) | 4445 | `"                        }"` | — |
| [SRC-1AE03B9EC3-L004446](../../agents/web_agent.py#L4446) | 4446 | `"                        search_warnings.append("` | — |
| [SRC-1AE03B9EC3-L004447](../../agents/web_agent.py#L4447) | 4447 | `"                            \"تعذر تنفيذ محاولة البحث الإضافية المحدودة (\""` | — |
| [SRC-1AE03B9EC3-L004448](../../agents/web_agent.py#L4448) | 4448 | `"                            + type(exc).__name__ + \").\""` | — |
| [SRC-1AE03B9EC3-L004449](../../agents/web_agent.py#L4449) | 4449 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004450](../../agents/web_agent.py#L4450) | 4450 | `"                    search_warnings.extend(repair_warnings)"` | — |
| [SRC-1AE03B9EC3-L004451](../../agents/web_agent.py#L4451) | 4451 | `"                    evidence_repair[\"attempted_query_count\"] = 1"` | — |
| [SRC-1AE03B9EC3-L004452](../../agents/web_agent.py#L4452) | 4452 | `"                    evidence_repair[\"initial_source_count\"] = initial_source_count"` | — |
| [SRC-1AE03B9EC3-L004453](../../agents/web_agent.py#L4453) | 4453 | `"                    evidence_repair[\"initial_independent_domain_count\"] = initial_domain_count"` | — |
| [SRC-1AE03B9EC3-L004454](../../agents/web_agent.py#L4454) | 4454 | `"                    evidence_repair[\"new_sources_added\"] = 0"` | — |
| [SRC-1AE03B9EC3-L004455](../../agents/web_agent.py#L4455) | 4455 | `"                    source_indexes: dict[str, int] = {}"` | — |
| [SRC-1AE03B9EC3-L004456](../../agents/web_agent.py#L4456) | 4456 | `"                    for source_index, source in enumerate(sources):"` | — |
| [SRC-1AE03B9EC3-L004457](../../agents/web_agent.py#L4457) | 4457 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L004458](../../agents/web_agent.py#L4458) | 4458 | `"                        if source_key:"` | — |
| [SRC-1AE03B9EC3-L004459](../../agents/web_agent.py#L4459) | 4459 | `"                            source_indexes.setdefault(source_key, source_index)"` | — |
| [SRC-1AE03B9EC3-L004460](../../agents/web_agent.py#L4460) | 4460 | `"                    relevant_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004461](../../agents/web_agent.py#L4461) | 4461 | `"                        query"` | — |
| [SRC-1AE03B9EC3-L004462](../../agents/web_agent.py#L4462) | 4462 | `"                        for query in ("` | — |
| [SRC-1AE03B9EC3-L004463](../../agents/web_agent.py#L4463) | 4463 | `"                            compact_search_query(question),"` | — |
| [SRC-1AE03B9EC3-L004464](../../agents/web_agent.py#L4464) | 4464 | `"                            *("` | — |
| [SRC-1AE03B9EC3-L004465](../../agents/web_agent.py#L4465) | 4465 | `"                                compact_search_query(candidate)"` | — |
| [SRC-1AE03B9EC3-L004466](../../agents/web_agent.py#L4466) | 4466 | `"                                for candidate in original_queries"` | — |
| [SRC-1AE03B9EC3-L004467](../../agents/web_agent.py#L4467) | 4467 | `"                                if isinstance(candidate, str)"` | — |
| [SRC-1AE03B9EC3-L004468](../../agents/web_agent.py#L4468) | 4468 | `"                            ),"` | — |
| [SRC-1AE03B9EC3-L004469](../../agents/web_agent.py#L4469) | 4469 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004470](../../agents/web_agent.py#L4470) | 4470 | `"                        if query"` | — |
| [SRC-1AE03B9EC3-L004471](../../agents/web_agent.py#L4471) | 4471 | `"                    ))"` | — |
| [SRC-1AE03B9EC3-L004472](../../agents/web_agent.py#L4472) | 4472 | `"                    for source in repair_sources:"` | — |
| [SRC-1AE03B9EC3-L004473](../../agents/web_agent.py#L4473) | 4473 | `"                        if not isinstance(source, dict):"` | — |
| [SRC-1AE03B9EC3-L004474](../../agents/web_agent.py#L4474) | 4474 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L004475](../../agents/web_agent.py#L4475) | 4475 | `"                        if not any("` | — |
| [SRC-1AE03B9EC3-L004476](../../agents/web_agent.py#L4476) | 4476 | `"                            self._source_matches_query(candidate, source)"` | — |
| [SRC-1AE03B9EC3-L004477](../../agents/web_agent.py#L4477) | 4477 | `"                            for candidate in relevant_queries if candidate"` | — |
| [SRC-1AE03B9EC3-L004478](../../agents/web_agent.py#L4478) | 4478 | `"                        ):"` | — |
| [SRC-1AE03B9EC3-L004479](../../agents/web_agent.py#L4479) | 4479 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L004480](../../agents/web_agent.py#L4480) | 4480 | `"                        source_key = self._normalized_source_url_key(source.get(\"url\"))"` | — |
| [SRC-1AE03B9EC3-L004481](../../agents/web_agent.py#L4481) | 4481 | `"                        if not source_key:"` | — |
| [SRC-1AE03B9EC3-L004482](../../agents/web_agent.py#L4482) | 4482 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L004483](../../agents/web_agent.py#L4483) | 4483 | `"                        existing_index = source_indexes.get(source_key)"` | — |
| [SRC-1AE03B9EC3-L004484](../../agents/web_agent.py#L4484) | 4484 | `"                        if existing_index is None:"` | — |
| [SRC-1AE03B9EC3-L004485](../../agents/web_agent.py#L4485) | 4485 | `"                            source_indexes[source_key] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004486](../../agents/web_agent.py#L4486) | 4486 | `"                            sources.append(source)"` | — |
| [SRC-1AE03B9EC3-L004487](../../agents/web_agent.py#L4487) | 4487 | `"                            evidence_repair[\"new_sources_added\"] += 1"` | — |
| [SRC-1AE03B9EC3-L004488](../../agents/web_agent.py#L4488) | 4488 | `"                            continue"` | — |
| [SRC-1AE03B9EC3-L004489](../../agents/web_agent.py#L4489) | 4489 | `"                        existing_source = sources[existing_index]"` | — |
| [SRC-1AE03B9EC3-L004490](../../agents/web_agent.py#L4490) | 4490 | `"                        providers = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004491](../../agents/web_agent.py#L4491) | 4491 | `"                            list(existing_source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L004492](../../agents/web_agent.py#L4492) | 4492 | `"                            + list(source.get(\"providers\", []))"` | — |
| [SRC-1AE03B9EC3-L004493](../../agents/web_agent.py#L4493) | 4493 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L004494](../../agents/web_agent.py#L4494) | 4494 | `"                        source_queries = list(dict.fromkeys("` | — |
| [SRC-1AE03B9EC3-L004495](../../agents/web_agent.py#L4495) | 4495 | `"                            list(existing_source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L004496](../../agents/web_agent.py#L4496) | 4496 | `"                            + list(source.get(\"queries\", []))"` | — |
| [SRC-1AE03B9EC3-L004497](../../agents/web_agent.py#L4497) | 4497 | `"                        ))"` | — |
| [SRC-1AE03B9EC3-L004498](../../agents/web_agent.py#L4498) | 4498 | `"                        if source.get(\"page_fetched\") and not existing_source.get(\"page_fetched\"):"` | — |
| [SRC-1AE03B9EC3-L004499](../../agents/web_agent.py#L4499) | 4499 | `"                            merged_source = dict(existing_source)"` | — |
| [SRC-1AE03B9EC3-L004500](../../agents/web_agent.py#L4500) | 4500 | `"                            merged_source.update(source)"` | — |
| [SRC-1AE03B9EC3-L004501](../../agents/web_agent.py#L4501) | 4501 | `"                            merged_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L004502](../../agents/web_agent.py#L4502) | 4502 | `"                            merged_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L004503](../../agents/web_agent.py#L4503) | 4503 | `"                            sources[existing_index] = merged_source"` | — |
| [SRC-1AE03B9EC3-L004504](../../agents/web_agent.py#L4504) | 4504 | `"                        else:"` | — |
| [SRC-1AE03B9EC3-L004505](../../agents/web_agent.py#L4505) | 4505 | `"                            existing_source[\"providers\"] = providers"` | — |
| [SRC-1AE03B9EC3-L004506](../../agents/web_agent.py#L4506) | 4506 | `"                            existing_source[\"queries\"] = source_queries"` | — |
| [SRC-1AE03B9EC3-L004507](../../agents/web_agent.py#L4507) | 4507 | `"                    sources.sort("` | — |
| [SRC-1AE03B9EC3-L004508](../../agents/web_agent.py#L4508) | 4508 | `"                        key=lambda item: float(item.get(\"rank_score\", 0) or 0),"` | — |
| [SRC-1AE03B9EC3-L004509](../../agents/web_agent.py#L4509) | 4509 | `"                        reverse=True,"` | — |
| [SRC-1AE03B9EC3-L004510](../../agents/web_agent.py#L4510) | 4510 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004511](../../agents/web_agent.py#L4511) | 4511 | `"                    plan[\"queries\"] = list(dict.fromkeys(original_queries + [repair_query]))"` | — |
| [SRC-1AE03B9EC3-L004512](../../agents/web_agent.py#L4512) | 4512 | `"                    independent_domains = {"` | — |
| [SRC-1AE03B9EC3-L004513](../../agents/web_agent.py#L4513) | 4513 | `"                        registrable_domain("` | — |
| [SRC-1AE03B9EC3-L004514](../../agents/web_agent.py#L4514) | 4514 | `"                            source.get(\"domain\")"` | — |
| [SRC-1AE03B9EC3-L004515](../../agents/web_agent.py#L4515) | 4515 | `"                            or urllib.parse.urlparse(source.get(\"url\", \"\")).hostname"` | — |
| [SRC-1AE03B9EC3-L004516](../../agents/web_agent.py#L4516) | 4516 | `"                            or \"\""` | — |
| [SRC-1AE03B9EC3-L004517](../../agents/web_agent.py#L4517) | 4517 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004518](../../agents/web_agent.py#L4518) | 4518 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L004519](../../agents/web_agent.py#L4519) | 4519 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L004520](../../agents/web_agent.py#L4520) | 4520 | `"                    independent_domains.discard(\"\")"` | — |
| [SRC-1AE03B9EC3-L004521](../../agents/web_agent.py#L4521) | 4521 | `"                    needs_corroboration = ("` | — |
| [SRC-1AE03B9EC3-L004522](../../agents/web_agent.py#L4522) | 4522 | `"                        len(sources) < 2 or len(independent_domains) < 2"` | — |
| [SRC-1AE03B9EC3-L004523](../../agents/web_agent.py#L4523) | 4523 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004524](../../agents/web_agent.py#L4524) | 4524 | `"                    evidence_repair.update({"` | — |
| [SRC-1AE03B9EC3-L004525](../../agents/web_agent.py#L4525) | 4525 | `"                        \"final_source_count\": len(sources),"` | — |
| [SRC-1AE03B9EC3-L004526](../../agents/web_agent.py#L4526) | 4526 | `"                        \"final_independent_domain_count\": len(independent_domains),"` | — |
| [SRC-1AE03B9EC3-L004527](../../agents/web_agent.py#L4527) | 4527 | `"                        \"recovered\": not needs_corroboration,"` | — |
| [SRC-1AE03B9EC3-L004528](../../agents/web_agent.py#L4528) | 4528 | `"                    })"` | — |
| [SRC-1AE03B9EC3-L004529](../../agents/web_agent.py#L4529) | 4529 | `"                    evidence_repair[\"reason\"] = ("` | — |
| [SRC-1AE03B9EC3-L004530](../../agents/web_agent.py#L4530) | 4530 | `"                        \"single_bounded_retry_still_insufficient\""` | — |
| [SRC-1AE03B9EC3-L004531](../../agents/web_agent.py#L4531) | 4531 | `"                        if needs_corroboration else \"evidence_gate_recovered\""` | — |
| [SRC-1AE03B9EC3-L004532](../../agents/web_agent.py#L4532) | 4532 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004533](../../agents/web_agent.py#L4533) | 4533 | `"                    report[\"queries_planned\"] = int(report.get(\"queries_planned\", 0) or 0) + int("` | — |
| [SRC-1AE03B9EC3-L004534](../../agents/web_agent.py#L4534) | 4534 | `"                        repair_report.get(\"queries_planned\", 1) or 0"` | — |
| [SRC-1AE03B9EC3-L004535](../../agents/web_agent.py#L4535) | 4535 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004536](../../agents/web_agent.py#L4536) | 4536 | `"                    initial_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L004537](../../agents/web_agent.py#L4537) | 4537 | `"                    repair_attempt_count = repair_report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L004538](../../agents/web_agent.py#L4538) | 4538 | `"                    if initial_attempt_count is None or repair_attempt_count is None:"` | — |
| [SRC-1AE03B9EC3-L004539](../../agents/web_agent.py#L4539) | 4539 | `"                        report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L004540](../../agents/web_agent.py#L4540) | 4540 | `"                        report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L004541](../../agents/web_agent.py#L4541) | 4541 | `"                    else:"` | — |
| [SRC-1AE03B9EC3-L004542](../../agents/web_agent.py#L4542) | 4542 | `"                        try:"` | — |
| [SRC-1AE03B9EC3-L004543](../../agents/web_agent.py#L4543) | 4543 | `"                            report[\"queries_attempted\"] = max(0, int(initial_attempt_count or 0)) + max("` | — |
| [SRC-1AE03B9EC3-L004544](../../agents/web_agent.py#L4544) | 4544 | `"                                0, int(repair_attempt_count or 0)"` | — |
| [SRC-1AE03B9EC3-L004545](../../agents/web_agent.py#L4545) | 4545 | `"                            )"` | — |
| [SRC-1AE03B9EC3-L004546](../../agents/web_agent.py#L4546) | 4546 | `"                            report[\"queries_attempted_known\"] = True"` | — |
| [SRC-1AE03B9EC3-L004547](../../agents/web_agent.py#L4547) | 4547 | `"                        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L004548](../../agents/web_agent.py#L4548) | 4548 | `"                            report[\"queries_attempted\"] = None"` | — |
| [SRC-1AE03B9EC3-L004549](../../agents/web_agent.py#L4549) | 4549 | `"                            report[\"queries_attempted_known\"] = False"` | — |
| [SRC-1AE03B9EC3-L004550](../../agents/web_agent.py#L4550) | 4550 | `"                    report[\"query_results\"] = list(report.get(\"query_results\", [])) + list("` | — |
| [SRC-1AE03B9EC3-L004551](../../agents/web_agent.py#L4551) | 4551 | `"                        repair_report.get(\"query_results\", [])"` | — |
| [SRC-1AE03B9EC3-L004552](../../agents/web_agent.py#L4552) | 4552 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004553](../../agents/web_agent.py#L4553) | 4553 | `"                    merged_providers = {"` | — |
| [SRC-1AE03B9EC3-L004554](../../agents/web_agent.py#L4554) | 4554 | `"                        provider"` | — |
| [SRC-1AE03B9EC3-L004555](../../agents/web_agent.py#L4555) | 4555 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L004556](../../agents/web_agent.py#L4556) | 4556 | `"                        for provider in source.get(\"providers\", [])"` | — |
| [SRC-1AE03B9EC3-L004557](../../agents/web_agent.py#L4557) | 4557 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L004558](../../agents/web_agent.py#L4558) | 4558 | `"                    report[\"providers_used\"] = sorted(merged_providers)"` | — |
| [SRC-1AE03B9EC3-L004559](../../agents/web_agent.py#L4559) | 4559 | `"                    report[\"provider_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L004560](../../agents/web_agent.py#L4560) | 4560 | `"                        provider: sum("` | — |
| [SRC-1AE03B9EC3-L004561](../../agents/web_agent.py#L4561) | 4561 | `"                            provider in source.get(\"providers\", []) for source in sources"` | — |
| [SRC-1AE03B9EC3-L004562](../../agents/web_agent.py#L4562) | 4562 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004563](../../agents/web_agent.py#L4563) | 4563 | `"                        for provider in merged_providers"` | — |
| [SRC-1AE03B9EC3-L004564](../../agents/web_agent.py#L4564) | 4564 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L004565](../../agents/web_agent.py#L4565) | 4565 | `"                    report[\"platform_counts\"] = {"` | — |
| [SRC-1AE03B9EC3-L004566](../../agents/web_agent.py#L4566) | 4566 | `"                        str(source.get(\"platform\", \"web\")): sum("` | — |
| [SRC-1AE03B9EC3-L004567](../../agents/web_agent.py#L4567) | 4567 | `"                            str(other.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L004568](../../agents/web_agent.py#L4568) | 4568 | `"                            == str(source.get(\"platform\", \"web\"))"` | — |
| [SRC-1AE03B9EC3-L004569](../../agents/web_agent.py#L4569) | 4569 | `"                            for other in sources"` | — |
| [SRC-1AE03B9EC3-L004570](../../agents/web_agent.py#L4570) | 4570 | `"                        )"` | — |
| [SRC-1AE03B9EC3-L004571](../../agents/web_agent.py#L4571) | 4571 | `"                        for source in sources"` | — |
| [SRC-1AE03B9EC3-L004572](../../agents/web_agent.py#L4572) | 4572 | `"                    }"` | — |
| [SRC-1AE03B9EC3-L004573](../../agents/web_agent.py#L4573) | 4573 | `"                    report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004574](../../agents/web_agent.py#L4574) | 4574 | `"                    report[\"pages_fetched\"] = sum("` | — |
| [SRC-1AE03B9EC3-L004575](../../agents/web_agent.py#L4575) | 4575 | `"                        bool(source.get(\"page_fetched\")) for source in sources"` | — |
| [SRC-1AE03B9EC3-L004576](../../agents/web_agent.py#L4576) | 4576 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004577](../../agents/web_agent.py#L4577) | 4577 | `"                    report[\"independent_sources\"] = len(independent_domains)"` | — |
| [SRC-1AE03B9EC3-L004578](../../agents/web_agent.py#L4578) | 4578 | `"                    report[\"provider_diagnostics\"] = list(self._provider_diagnostics)"` | — |
| [SRC-1AE03B9EC3-L004579](../../agents/web_agent.py#L4579) | 4579 | `"                    report[\"evidence_signals\"] = evidence_signal_report("` | — |
| [SRC-1AE03B9EC3-L004580](../../agents/web_agent.py#L4580) | 4580 | `"                        sources, plan.get(\"freshness\", \"any\")"` | — |
| [SRC-1AE03B9EC3-L004581](../../agents/web_agent.py#L4581) | 4581 | `"                    )"` | — |
| [SRC-1AE03B9EC3-L004582](../../agents/web_agent.py#L4582) | 4582 | `"                else:"` | — |
| [SRC-1AE03B9EC3-L004583](../../agents/web_agent.py#L4583) | 4583 | `"                    evidence_repair[\"reason\"] = \"repair_query_was_not_distinct\""` | — |
| [SRC-1AE03B9EC3-L004584](../../agents/web_agent.py#L4584) | 4584 | `"        report[\"evidence_repair\"] = evidence_repair"` | — |
| [SRC-1AE03B9EC3-L004585](../../agents/web_agent.py#L4585) | 4585 | `"        baseline_diagnostic_ids = {id(item) for item in research_diagnostic_baseline}"` | — |
| [SRC-1AE03B9EC3-L004586](../../agents/web_agent.py#L4586) | 4586 | `"        with self._provider_diagnostics_lock:"` | — |
| [SRC-1AE03B9EC3-L004587](../../agents/web_agent.py#L4587) | 4587 | `"            current_research_diagnostics = ["` | — |
| [SRC-1AE03B9EC3-L004588](../../agents/web_agent.py#L4588) | 4588 | `"                item for item in self._provider_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004589](../../agents/web_agent.py#L4589) | 4589 | `"                if id(item) not in baseline_diagnostic_ids"` | — |
| [SRC-1AE03B9EC3-L004590](../../agents/web_agent.py#L4590) | 4590 | `"            ]"` | — |
| [SRC-1AE03B9EC3-L004591](../../agents/web_agent.py#L4591) | 4591 | `"        report[\"provider_diagnostics\"] = current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004592](../../agents/web_agent.py#L4592) | 4592 | `"        provider_attempt_observed = any("` | — |
| [SRC-1AE03B9EC3-L004593](../../agents/web_agent.py#L4593) | 4593 | `"            item.get(\"status\") in _SEARCH_ATTEMPT_DIAGNOSTIC_STATUSES"` | — |
| [SRC-1AE03B9EC3-L004594](../../agents/web_agent.py#L4594) | 4594 | `"            for item in current_research_diagnostics"` | — |
| [SRC-1AE03B9EC3-L004595](../../agents/web_agent.py#L4595) | 4595 | `"        )"` | — |
| [SRC-1AE03B9EC3-L004596](../../agents/web_agent.py#L4596) | 4596 | `"        raw_attempt_count = report.get(\"queries_attempted\", 0)"` | — |
| [SRC-1AE03B9EC3-L004597](../../agents/web_agent.py#L4597) | 4597 | `"        try:"` | — |
| [SRC-1AE03B9EC3-L004598](../../agents/web_agent.py#L4598) | 4598 | `"            queries_attempted = ("` | — |
| [SRC-1AE03B9EC3-L004599](../../agents/web_agent.py#L4599) | 4599 | `"                None if raw_attempt_count is None"` | — |
| [SRC-1AE03B9EC3-L004600](../../agents/web_agent.py#L4600) | 4600 | `"                else max(0, int(raw_attempt_count or 0))"` | — |
| [SRC-1AE03B9EC3-L004601](../../agents/web_agent.py#L4601) | 4601 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004602](../../agents/web_agent.py#L4602) | 4602 | `"        except (TypeError, ValueError):"` | — |
| [SRC-1AE03B9EC3-L004603](../../agents/web_agent.py#L4603) | 4603 | `"            queries_attempted = None"` | — |
| [SRC-1AE03B9EC3-L004604](../../agents/web_agent.py#L4604) | 4604 | `"        if queries_attempted is not None:"` | — |
| [SRC-1AE03B9EC3-L004605](../../agents/web_agent.py#L4605) | 4605 | `"            search_attempted = ("` | — |
| [SRC-1AE03B9EC3-L004606](../../agents/web_agent.py#L4606) | 4606 | `"                queries_attempted > 0"` | — |
| [SRC-1AE03B9EC3-L004607](../../agents/web_agent.py#L4607) | 4607 | `"                or provider_attempt_observed"` | — |
| [SRC-1AE03B9EC3-L004608](../../agents/web_agent.py#L4608) | 4608 | `"                or report.get(\"search_attempted\") is True"` | — |
| [SRC-1AE03B9EC3-L004609](../../agents/web_agent.py#L4609) | 4609 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004610](../../agents/web_agent.py#L4610) | 4610 | `"        elif provider_attempt_observed or report.get(\"search_attempted\") is True:"` | — |
| [SRC-1AE03B9EC3-L004611](../../agents/web_agent.py#L4611) | 4611 | `"            search_attempted = True"` | — |
| [SRC-1AE03B9EC3-L004612](../../agents/web_agent.py#L4612) | 4612 | `"        elif isinstance(report.get(\"search_attempted\"), bool):"` | — |
| [SRC-1AE03B9EC3-L004613](../../agents/web_agent.py#L4613) | 4613 | `"            search_attempted = report[\"search_attempted\"]"` | — |
| [SRC-1AE03B9EC3-L004614](../../agents/web_agent.py#L4614) | 4614 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L004615](../../agents/web_agent.py#L4615) | 4615 | `"            search_attempted = None"` | — |
| [SRC-1AE03B9EC3-L004616](../../agents/web_agent.py#L4616) | 4616 | `"        report[\"queries_attempted\"] = queries_attempted"` | — |
| [SRC-1AE03B9EC3-L004617](../../agents/web_agent.py#L4617) | 4617 | `"        report[\"queries_attempted_known\"] = queries_attempted is not None"` | — |
| [SRC-1AE03B9EC3-L004618](../../agents/web_agent.py#L4618) | 4618 | `"        report[\"search_attempted\"] = search_attempted"` | — |
| [SRC-1AE03B9EC3-L004619](../../agents/web_agent.py#L4619) | 4619 | `"        previous_search_outcome = report.get(\"search_outcome\")"` | — |
| [SRC-1AE03B9EC3-L004620](../../agents/web_agent.py#L4620) | 4620 | `"        if previous_search_outcome in _RESEARCH_ERROR_OUTCOMES and not sources:"` | — |
| [SRC-1AE03B9EC3-L004621](../../agents/web_agent.py#L4621) | 4621 | `"            if provider_attempt_observed or search_attempted is True:"` | — |
| [SRC-1AE03B9EC3-L004622](../../agents/web_agent.py#L4622) | 4622 | `"                search_outcome = \"attempted_research_error\""` | — |
| [SRC-1AE03B9EC3-L004623](../../agents/web_agent.py#L4623) | 4623 | `"            elif search_attempted is False:"` | — |
| [SRC-1AE03B9EC3-L004624](../../agents/web_agent.py#L4624) | 4624 | `"                search_outcome = \"not_attempted\""` | — |
| [SRC-1AE03B9EC3-L004625](../../agents/web_agent.py#L4625) | 4625 | `"            else:"` | — |
| [SRC-1AE03B9EC3-L004626](../../agents/web_agent.py#L4626) | 4626 | `"                search_outcome = \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L004627](../../agents/web_agent.py#L4627) | 4627 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L004628](../../agents/web_agent.py#L4628) | 4628 | `"            search_outcome = ("` | — |
| [SRC-1AE03B9EC3-L004629](../../agents/web_agent.py#L4629) | 4629 | `"                \"attempted_with_usable_sources\" if search_attempted is True and sources"` | — |
| [SRC-1AE03B9EC3-L004630](../../agents/web_agent.py#L4630) | 4630 | `"                else \"attempted_no_usable_sources\" if search_attempted is True"` | — |
| [SRC-1AE03B9EC3-L004631](../../agents/web_agent.py#L4631) | 4631 | `"                else \"not_attempted\" if search_attempted is False"` | — |
| [SRC-1AE03B9EC3-L004632](../../agents/web_agent.py#L4632) | 4632 | `"                else \"unknown_after_research_error\""` | — |
| [SRC-1AE03B9EC3-L004633](../../agents/web_agent.py#L4633) | 4633 | `"            )"` | — |
| [SRC-1AE03B9EC3-L004634](../../agents/web_agent.py#L4634) | 4634 | `"        report[\"search_outcome\"] = search_outcome"` | — |
| [SRC-1AE03B9EC3-L004635](../../agents/web_agent.py#L4635) | 4635 | `"        if search_outcome in _RESEARCH_ERROR_OUTCOMES:"` | — |
| [SRC-1AE03B9EC3-L004636](../../agents/web_agent.py#L4636) | 4636 | `"            report[\"usable_sources_after_filtering\"] = None"` | — |
| [SRC-1AE03B9EC3-L004637](../../agents/web_agent.py#L4637) | 4637 | `"            report[\"unique_sources\"] = None"` | — |
| [SRC-1AE03B9EC3-L004638](../../agents/web_agent.py#L4638) | 4638 | `"            report[\"pages_fetched\"] = None"` | — |
| [SRC-1AE03B9EC3-L004639](../../agents/web_agent.py#L4639) | 4639 | `"            report[\"provider_counts\"] = None"` | — |
| [SRC-1AE03B9EC3-L004640](../../agents/web_agent.py#L4640) | 4640 | `"        else:"` | — |
| [SRC-1AE03B9EC3-L004641](../../agents/web_agent.py#L4641) | 4641 | `"            report[\"usable_sources_after_filtering\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004642](../../agents/web_agent.py#L4642) | 4642 | `"            if report.get(\"unique_sources\") is None and sources:"` | — |
| [SRC-1AE03B9EC3-L004643](../../agents/web_agent.py#L4643) | 4643 | `"                report[\"unique_sources\"] = len(sources)"` | — |
| [SRC-1AE03B9EC3-L004644](../../agents/web_agent.py#L4644) | 4644 | `"            if report.get(\"pages_fetched\") is None and sources:"` | — |
